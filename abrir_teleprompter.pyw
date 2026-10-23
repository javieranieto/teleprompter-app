# -*- coding: utf-8 -*-
"""Teleprompter, por Javier Nieto. Para usarlo SIN internet.

Abre el teleprompter como sitio local (http://127.0.0.1:47317), no como archivo.

POR QUE EXISTE
--------------
Abierto con doble clic, el teleprompter es un `file://`, y en ese origen Chrome NO
recuerda el permiso del microfono. "Seguir mi voz" se reinicia cada vez que Chrome
corta el reconocimiento (al final de cada frase o toma), y cada reinicio volvia a
pedir permiso.
En http://127.0.0.1 Chrome si guarda el permiso: se da una vez y ya.

El PUERTO ES FIJO A PROPOSITO: el permiso se guarda por puerto. Si cambia, lo vuelve
a pedir (una vez). Y lo guardado en el navegador (texto, ajustes) tambien es por
puerto.

Es .pyw para que no abra consola. Si ya hay un teleprompter sirviendo en ese puerto,
solo abre el navegador. El servidor se apaga solo tras 12 horas.
"""
import functools
import http.server
import pathlib
import socketserver
import sys
import threading
import time
import urllib.request
import webbrowser

PUERTO = 47317
CARPETA = pathlib.Path(__file__).resolve().parent
URL = f"http://127.0.0.1:{PUERTO}/index.html"
MARCA = b"<title>Teleprompter</title>"


def ya_sirve_el_nuestro() -> bool:
    try:
        with urllib.request.urlopen(URL, timeout=1.5) as r:
            return MARCA in r.read(4096)
    except Exception:
        return False


def avisar(texto: str) -> None:
    try:
        import tkinter.messagebox as mb
        mb.showerror("Teleprompter", texto)
    except Exception:
        print(texto, file=sys.stderr)


class Silencioso(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def end_headers(self):
        # Que una version nueva del teleprompter se vea al recargar, sin cache vieja.
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


def main() -> None:
    if ya_sirve_el_nuestro():
        webbrowser.open(URL)
        return
    try:
        servidor = socketserver.ThreadingTCPServer(
            ("127.0.0.1", PUERTO), functools.partial(Silencioso, directory=str(CARPETA)))
    except OSError:
        avisar(f"El puerto {PUERTO} lo esta usando otro programa.\n"
               f"Cierra ese programa, o abre index.html con doble clic "
               f"(funciona, pero el microfono pedira permiso a cada rato).")
        return
    servidor.daemon_threads = True
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    if not ya_sirve_el_nuestro():
        avisar("El servidor arranco pero no contesta con el teleprompter. Avisale a Claude.")
        return
    webbrowser.open(URL)
    time.sleep(12 * 3600)
    servidor.shutdown()


if __name__ == "__main__":
    main()
