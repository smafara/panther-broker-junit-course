# Comprobar resultados con JUnit

Presentación 3 de Panther Broker. Objetivo: expresar una expectativa útil e interpretar una falla. Diez diapositivas con notas en español.

## Ejecutar

```sh
npm install
npm run dev
```

Abrir http://localhost:3032. `npm run build`, `npm run export:pdf` y, con el servidor activo, `npm run check:deck`.

Reutiliza el tema oscuro, Shiki Tokyo Night, encabezados de archivo y TerminalRecording de las primeras presentaciones. Las grabaciones se reproducen automáticamente a0.5×; los resultados proceden de Surefire XML. Los estados se revelan después de terminar la reproducción como recurso didáctico.

## Ejemplos y evidencia

Proyectos Maven: `comprobar-resultados-junit/before` y `after` desde la raíz. Activar `sdk env`. Ambos pasan. El defecto `/10` existe únicamente en la copia temporal de grabación; produce110 en lugar de2, mientras la comprobación positiva pasa.

Regenerar con `scripts/record-comprobar-resultados.py` usando Python con PyMuPDF. Se exige Zulu25.0.5+8 y se conserva salida PTY real. Los PNG para impresión derivan del reporte XML. No se incluyen impuestos, cotizaciones reales ni una política financiera de precisión.

Práctica final: cuenta equilibrada, esperado0. Las notas identifican fragmentos abreviados; los proyectos contienen imports y clases completos.
