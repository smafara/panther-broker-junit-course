#!/usr/bin/env python3
"""Verifica la historia y, con --captures, registra salidas reales para las diapositivas."""
import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
JDK = '25.0.5.0+8-zulu'
java_home = Path(os.environ.get('SDKMAN_DIR', str(Path.home() / '.sdkman'))) / 'candidates/java' / JDK
if not (java_home / 'bin/java').exists():
    raise SystemExit(f'Instala el JDK del curso: sdk install java {JDK}')
env = os.environ.copy()
env.update(JAVA_HOME=str(java_home), PATH=str(java_home / 'bin') + os.pathsep + env.get('PATH', ''))
java = str(java_home / 'bin/java')
version = subprocess.run([java, '-XshowSettings:properties', '-version'], capture_output=True, text=True, check=True, env=env)
assert 'java.runtime.version = 25.0.5+8-LTS' in version.stderr
assert 'java.vendor = Azul Systems, Inc.' in version.stderr
parser = argparse.ArgumentParser()
parser.add_argument('--captures', action='store_true', help='Genera PNG, SVG y extractos reales; requiere PyMuPDF')
parser.add_argument('--render-only', action='store_true', help='Regenera imágenes desde el manifiesto existente sin repetir Maven')
args = parser.parse_args()
if args.captures or args.render_only:
    import pymupdf

wrapper = str(ROOT / 'mvnw')
stages = [ROOT / 'kata-zero' / p for p in ['before', 'after/01-naive-fractions', 'after/02-first-test']]
source = Path('src/main/java/mx/azc/uam/pantherbroker')
records = {}


def maven(project, *goals, expected=0):
    command = [wrapper, '-B', '-ntp', '-f', str(project / 'pom.xml'), *goals]
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)
    assert result.returncode == expected, result.stdout + result.stderr
    return result


def console(project, input_text='2\n40\n60\n0\n'):
    result = subprocess.run([java, '-cp', str(project / 'target/classes'), 'mx.azc.uam.pantherbroker.Main'],
                            input=input_text, env=env, capture_output=True, text=True, check=True, timeout=10)
    assert not result.stderr, result.stderr
    return result.stdout


def plan_excerpt(output):
    return '\n'.join(line for line in output.splitlines() if line.startswith(('Valor total:', 'Plan sugerido', 'VENDER ', 'COMPRAR '))) + '\n'


def test_excerpt(output):
    clean = re.sub(r'\x1b\[[0-9;]*m', '', output)
    lines = clean.splitlines()
    running = [line for line in lines if 'Running mx.azc.uam.pantherbroker' in line]
    failures = [line for line in lines if line.startswith('org.opentest4j.AssertionFailedError:')]
    summary = [line for line in lines if 'Tests run:' in line and 'Time elapsed:' not in line]
    result = [line for line in lines if 'BUILD SUCCESS' in line or 'BUILD FAILURE' in line]
    assert summary and result, output
    return '\n'.join(running + failures + [summary[-1], result[-1]]) + '\n'


def write_captures(records):
    destination = ROOT / 'presentation/intro-junit-kata-zero/public/terminal'
    destination.mkdir(parents=True, exist_ok=True)
    for name, item in records.items():
        text = item['text']
        (destination / f'{name}.txt').write_text(text)
        lines = text.splitlines()
        width, line_height, font_size = 1520, 45, 28
        height = 115 + len(lines) * line_height
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
               f'<rect width="{width}" height="{height}" fill="#080e18"/>',
               f'<path d="M0 65H{width}" stroke="#304253"/>',
               '<circle cx="29" cy="32" r="7" fill="#ef7185"/><circle cx="54" cy="32" r="7" fill="#e5c36b"/><circle cx="79" cy="32" r="7" fill="#5ee0a1"/>',
               f'<text x="112" y="40" font-family="Arial,sans-serif" font-size="22" fill="#b1c5da">{html.escape(item["title"])}</text>']
        for index, line in enumerate(lines):
            color = '#fda4af' if any(token in line for token in ['[ERROR]', 'AssertionFailedError', 'BUILD FAILURE']) else ('#5eead4' if 'BUILD SUCCESS' in line or 'Failures: 0' in line else '#e2e8f0')
            svg.append(f'<text x="30" y="{112 + index * line_height}" font-family="monospace" font-size="{font_size}" fill="{color}" xml:space="preserve">{html.escape(line)}</text>')
        svg.append('</svg>')
        data='\n'.join(svg)
        (destination / f'{name}.svg').write_text(data)
        image = pymupdf.open(stream=data.encode(), filetype='svg')
        pdf = pymupdf.open('pdf', image.convert_to_pdf())
        pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(str(destination / f'{name}.png'))
    (destination / 'manifest.json').write_text(json.dumps(dict(jdk=JDK, provenance='Extractos de ejecuciones reales; encabezados y colores agregados para legibilidad. No son fotografías de una ventana de terminal.', scenarios=records), ensure_ascii=False, indent=2)+'\n')
    print(f'{len(records)} capturas renderizadas desde salidas reales, con texto y manifiesto: OK')

if args.render_only:
    saved = json.loads((ROOT / 'presentation/intro-junit-kata-zero/public/terminal/manifest.json').read_text())
    write_captures(saved['scenarios'])
    raise SystemExit(0)

print(f'JDK: {java_home}')
build = maven(ROOT, 'clean', 'verify')
assert 'BUILD SUCCESS' in build.stdout
print('Maven reactor: BUILD SUCCESS, suite corregida de tres pruebas')

baseline = [console(stage, '1\n2\n40\n60\n1\n0\n') for stage in stages]
for index, output in enumerate(baseline):
    expected = '2' if index == 0 else '2.0'
    assert f'VENDER META {expected} acciones' in output
    assert f'COMPRAR AAPL {expected} acciones' in output
    assert output.count('META: 10 acciones a 100 USD') == 2
    assert output.count('AAPL: 10 acciones a 100 USD') == 2
    alternate = console(stages[index], '2\n50\n50\n0\n')
    assert 'Plan sugerido' in alternate and 'VENDER ' not in alternate and 'COMPRAR ' not in alternate
    alternate = console(stages[index], '2\n30\n70\n0\n')
    four = '4' if index == 0 else '4.0'
    assert f'VENDER META {four} acciones' in alternate and f'COMPRAR AAPL {four} acciones' in alternate
    assert 'sumar 100%' in console(stages[index], '2\n40\n50\n0\n')
    assert 'sumar 100%' in console(stages[index], '2\nabc\n60\n0\n')
    for inputs, message in [('2\n40\n60\n2\n40\n60\n0\n', 'Plan sugerido'), ('99\n0\n', 'Opción no válida.'), ('', 'Hasta luego.')]:
        assert message in console(stages[index], inputs)
records['intro-whole-shares'] = dict(title='Panther Broker · acciones completas', text=plan_excerpt(baseline[0]), exitCode=0)
records['manual-original'] = dict(title='El caso manual de siempre · versión double', text=plan_excerpt(baseline[1]), exitCode=0)

with tempfile.TemporaryDirectory(prefix='kata-zero-intro-') as directory:
    for index, stage in enumerate(stages):
        copy = Path(directory) / str(index)
        shutil.copytree(stage, copy, ignore=shutil.ignore_patterns('target'))
        main = copy / source / 'Main.java'
        original = main.read_text()
        assert original.count('int[] prices = {100, 100};') == 1
        main.write_text(original.replace('int[] prices = {100, 100};', 'int[] prices = {150, 100};'))
        maven(copy, 'compile')
        output = console(copy)
        expected = '4' if index == 0 else ('4.0' if index == 1 else '3.333333333333333')
        assert f'VENDER META {expected} acciones' in output, output
        if index == 1:
            records['manual-fractional'] = dict(title='Nuevos valores · mismo programa double', text=plan_excerpt(output), exitCode=0)

    red = Path(directory) / 'red'
    shutil.copytree(stages[2], red, ignore=shutil.ignore_patterns('target'))
    helper = red / source / 'RebalanceCalculator.java'
    correct = helper.read_text()
    assert 'targetValue / (double) price' in correct
    helper.write_text(correct.replace('targetValue / (double) price', 'targetValue / price'))
    original_green = maven(red, '-Dtest=OriginalExamplesTest', 'test')
    assert 'Tests run: 2, Failures: 0, Errors: 0, Skipped: 0' in original_green.stdout
    records['tests-original-green'] = dict(title='Dos pruebas del ejemplo original · calculador con defecto', text=test_excerpt(original_green.stdout), exitCode=0)
    fractional_red = maven(red, 'test', expected=1)
    assert 'expected: <-3.333333> but was: <-4.0>' in fractional_red.stdout
    assert 'Tests run: 3, Failures: 1, Errors: 0, Skipped: 0' in fractional_red.stdout
    records['tests-fractional-red'] = dict(title='Agregamos el caso fraccionario · aparece la falla', text=test_excerpt(fractional_red.stdout), exitCode=1)

assert 'Tests run: 3, Failures: 0, Errors: 0, Skipped: 0' in build.stdout
records['tests-fixed-green'] = dict(title='Misma suite · división corregida', text=test_excerpt(build.stdout), exitCode=0)
print('27 ejecuciones de consola y casos original-verde / fraccionario-rojo / corregido-verde: OK')

if args.captures:
    write_captures(records)
