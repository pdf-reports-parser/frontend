import logging

from typer import Typer

from frontend.config import config
from frontend.app import create_app

logging.basicConfig(level=logging.DEBUG)

typer_app = Typer()


@typer_app.command(help='Start base service')
def run():
    app = create_app()
    app.run(host=config.app_host, port=config.app_port, debug=config.debug)


if __name__ == '__main__':
    typer_app()
