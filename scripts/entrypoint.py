import sys
import signal
import pathlib
import subprocess
import app


def main():
    path = pathlib.Path(app.__file__).parent.resolve()
    command = ["bokeh", "serve", str(path)] + sys.argv[1:]

    try:
        proc = subprocess.Popen(command)
        proc.wait()
    except KeyboardInterrupt:
        proc.send_signal(signal.SIGINT)
