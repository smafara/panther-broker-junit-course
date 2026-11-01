#!/usr/bin/env python3
"""Record actual PTY sessions as asciicast v2. Scripted input, unedited output."""
import codecs
import errno
import fcntl
import json
import os
from pathlib import Path
import pty
import select
import shutil
import signal
import struct
import subprocess
import tempfile
import termios
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'presentation/primeros-pasos-junit/public/terminal'
JDK = '25.0.5.0+8-zulu'
JDK_HOME = Path(os.environ.get('SDKMAN_DIR', str(Path.home() / '.sdkman'))) / 'candidates/java' / JDK
ENV = dict(os.environ, JAVA_HOME=str(JDK_HOME), PATH=str(JDK_HOME / 'bin') + os.pathsep + os.environ['PATH'],
           TERM='xterm-256color', PS1='panther$ ', PS2='> ', LC_ALL='en_US.UTF-8')
version = subprocess.run([str(JDK_HOME / 'bin/java'), '-XshowSettings:properties', '-version'],
                         env=ENV, capture_output=True, text=True, check=True).stderr
assert 'java.runtime.version = 25.0.5+8-LTS' in version and 'Azul Systems, Inc.' in version
SOURCE = Path('src/main/java/mx/azc/uam/pantherbroker')


def record(work, name, command, menu, expected, tokens):
    master, slave = pty.openpty()
    fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack('HHHH', 20, 100, 0, 0))
    # A real interactive shell supplies the prompt and echoes the automated input.
    # Capture the last status through the prompt, outside the visible terminal stream.
    shell_env = dict(ENV, PS1='$(printf "%s" "$?" > .recording-exit)panther$ ')
    process = subprocess.Popen(['/bin/sh', '-i'], cwd=work, env=shell_env,
                               stdin=slave, stdout=slave, stderr=slave, start_new_session=True)
    os.close(slave)
    start = time.monotonic()
    events, output = [], ''
    decoder = codecs.getincrementaldecoder('utf-8')()

    def drain(duration):
        nonlocal output
        end = time.monotonic() + duration
        while time.monotonic() < end:
            if not select.select([master], [], [], min(.05, max(0, end - time.monotonic())))[0]:
                continue
            try:
                data = os.read(master, 65536)
            except OSError as error:
                if error.errno == errno.EIO:
                    return
                raise
            if not data:
                return
            text = decoder.decode(data)
            if text:
                events.append([round(time.monotonic() - start, 6), 'o', text])
                output += text

    def wait_for(token, offset=0):
        deadline = time.monotonic() + 120
        while token not in output[offset:]:
            if time.monotonic() > deadline:
                raise RuntimeError(f'Timeout waiting for {token}: {output}')
            drain(.05)

    def type_text(text):
        for char in text:
            os.write(master, char.encode())
            drain(.035)

    try:
        wait_for('panther$ ')
        # Clear shell startup messages before the actual demonstration begins.
        type_text('clear\n')
        drain(.4)
        offset = len(output)
        type_text(command + '\n')
        if menu:
            wait_for('0. Salir', offset)
            for choice in ('1', '2', '0'):
                drain(1)
                offset = len(output)
                type_text(choice + '\n')
                if choice == '2':
                    wait_for('Objetivo para META (%):', offset)
                    type_text('40\n')
                    wait_for('Objetivo para AAPL (%):', offset)
                    type_text('60\n')
                wait_for('Hasta luego.' if choice == '0' else '0. Salir', offset)
        wait_for('panther$ ', offset)
        assert int((work / '.recording-exit').read_text()) == expected
        drain(1.5)
        assert all(token in output for token in tokens), output
        header = dict(version=2, width=100, height=20, title=name,
                      env={'TERM': ENV['TERM'], 'SHELL': '/bin/sh'},
                      duration=events[-1][0], command=command)
        (DEST / f'{name}.cast').write_text('\n'.join(json.dumps(row, ensure_ascii=False)
                                                    for row in [header, *events]) + '\n')
        print(f'{name}: {events[-1][0]:.1f}s, exit {expected}', flush=True)
        return dict(file=f'{name}.cast', command=command, exitCode=expected, duration=events[-1][0])
    finally:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait(timeout=5)
        os.close(master)


DEST.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='panther-primeros-pasos-') as directory:
    work = Path(directory)
    (work / 'mvnw').symlink_to(ROOT / 'mvnw')
    (work / '.mvn').symlink_to(ROOT / '.mvn', target_is_directory=True)
    project = work / 'primeros-pasos-junit/after'
    project.parent.mkdir(parents=True)
    shutil.copytree(ROOT / 'primeros-pasos-junit/after', project, ignore=shutil.ignore_patterns('target'))
    name = 'primera-prueba'
    command = './mvnw -B -ntp -f primeros-pasos-junit/after/pom.xml test'
    item = record(work, name, command, False, 0, ['Tests run: 1, Failures: 0', 'BUILD SUCCESS'])
    report = project / 'target/surefire-reports/TEST-mx.azc.uam.pantherbroker.RebalanceCalculatorTest.xml'
    cases = ET.parse(report).getroot().findall('testcase')
    assert len(cases) == 1 and cases[0].attrib['name'] == 'buysTwoSharesWhenBelowTarget'
    assert all(cases[0].find(tag) is None for tag in ('failure', 'error', 'skipped'))
    tests = [dict(name=cases[0].attrib['name'], status='passed')]
    item['tests'] = tests
    (DEST / 'recordings.json').write_text(json.dumps(dict(jdk=JDK, provenance='Sesión PTY real; entrada automatizada, salida sin editar.', scenario=item), ensure_ascii=False, indent=2) + '\n')
    data = ROOT / 'presentation/primeros-pasos-junit/data'
    data.mkdir(exist_ok=True)
    (data / 'test-results.json').write_text(json.dumps({name: tests}, indent=2) + '\n')
    # Static print fallback derived from the real XML report and successful exit.
    suite = ET.parse(report).getroot()
    summary = f"Tests run: {suite.attrib['tests']}, Failures: {suite.attrib['failures']}, Errors: {suite.attrib['errors']}, Skipped: {suite.attrib['skipped']}"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="240"><rect width="1200" height="240" fill="#0b1220"/><text x="30" y="90" font-family="monospace" font-size="27" fill="#e2e8f0">{summary}</text><text x="30" y="155" font-family="monospace" font-size="27" fill="#5eead4">BUILD SUCCESS</text></svg>"""
    (DEST / f'{name}.svg').write_text(svg)
    import pymupdf
    image = pymupdf.open(stream=svg.encode(), filetype='svg')
    pdf = pymupdf.open('pdf', image.convert_to_pdf())
    pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(str(DEST / f'{name}.png'))
