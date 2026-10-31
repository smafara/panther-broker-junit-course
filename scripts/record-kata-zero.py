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

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'presentation/intro-junit-kata-zero/public/terminal'
JDK = '25.0.5.0+8-zulu'
HOME = Path(os.environ.get('SDKMAN_DIR', str(Path.home() / '.sdkman'))) / 'candidates/java' / JDK
ENV = dict(os.environ, JAVA_HOME=str(HOME), PATH=str(HOME / 'bin') + os.pathsep + os.environ['PATH'],
           TERM='xterm-256color', PS1='panther$ ', PS2='> ', LC_ALL='en_US.UTF-8')
version = subprocess.run([str(HOME / 'bin/java'), '-XshowSettings:properties', '-version'],
                         env=ENV, capture_output=True, text=True, check=True).stderr
assert 'java.runtime.version = 25.0.5+8-LTS' in version and 'Azul Systems, Inc.' in version
SOURCE = Path('src/main/java/mx/azc/uam/pantherbroker')


def record(work, name, command, menu, expected, tokens):
    master, slave = pty.openpty()
    fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack('HHHH', 20, 100, 0, 0))
    # A real interactive shell supplies the prompt and echoes the automated input.
    process = subprocess.Popen(['/bin/sh', '-i'], cwd=work, env=ENV,
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
                wait_for('Hasta luego.' if choice == '0' else '0. Salir', offset)
        wait_for('panther$ ', offset)
        offset = len(output)
        type_text('echo "Salida: $?"\n')
        wait_for(f'Salida: {expected}\r\n', offset)
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
with tempfile.TemporaryDirectory(prefix='panther-recording-') as directory:
    work = Path(directory)
    (work / 'mvnw').symlink_to(ROOT / 'mvnw')
    (work / '.mvn').symlink_to(ROOT / '.mvn', target_is_directory=True)
    stages = {}
    for label, original in [('manual-original', 'after/01-naive-fractions'),
                            ('manual-fractional', 'after/01-naive-fractions'),
                            ('tests-buggy', 'after/02-first-test'),
                            ('tests-fixed', 'after/02-first-test')]:
        stage = work / label
        shutil.copytree(ROOT / 'kata-zero' / original, stage, ignore=shutil.ignore_patterns('target'))
        stages[label] = stage
    main = stages['manual-fractional'] / SOURCE / 'Main.java'
    main.write_text(main.read_text().replace('int[] prices = {100, 100};', 'int[] prices = {150, 100};'))
    helper = stages['tests-buggy'] / SOURCE / 'RebalanceCalculator.java'
    helper.write_text(helper.read_text().replace('targetValue / (double) price', 'targetValue / price'))
    # Precompile console examples, so the recordings focus on execution. Tests still run Maven.
    for label in ('manual-original', 'manual-fractional'):
        subprocess.run([str(work / 'mvnw'), '-B', '-ntp', '-f', str(stages[label] / 'pom.xml'), 'compile'],
                       env=ENV, capture_output=True, check=True)
    scenarios = {}
    for name in ('manual-original', 'manual-fractional'):
        scenarios[name] = record(stages[name], name,
                                 'java -cp target/classes mx.azc.uam.pantherbroker.Main', True, 0,
                                 ['Hasta luego.', 'VENDER META ' + ('2.0' if name.endswith('original') else '4.0')])
    for name, stage, arguments, exit_code, count in [
        ('tests-original-green', 'tests-buggy', '-Dtest=OriginalExamplesTest ', 0, 'Tests run: 2, Failures: 0'),
        ('tests-fractional-red', 'tests-buggy', '', 1, 'Tests run: 3, Failures: 1'),
        ('tests-fixed-green', 'tests-fixed', '', 0, 'Tests run: 3, Failures: 0'),
    ]:
        scenarios[name] = record(stages[stage], name, f'../mvnw -B -ntp {arguments}test', False, exit_code,
                                 [count, 'BUILD SUCCESS' if exit_code == 0 else 'BUILD FAILURE'])
(DEST / 'recordings.json').write_text(json.dumps(dict(jdk=JDK,
    provenance='Sesiones PTY reales en formato asciicast v2. Entradas automatizadas con pausas; salida completa sin editar. Directorios temporales; preparación fuera de la grabación. Reproductor limita pausas inactivas a dos segundos.',
    scenarios=scenarios), ensure_ascii=False, indent=2) + '\n')
