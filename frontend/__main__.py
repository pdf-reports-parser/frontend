import logging

from typer import Typer

from frontend import config
from frontend.app import create_app

logging.basicConfig(level=logging.DEBUG)

typer_app = Typer()
app_config = config.load_from_env()


@typer_app.command(help='Start base service')
def run():
    app = create_app()
    app.run(host=app_config.app_host, port=app_config.app_port, debug=True)


if __name__ == '__main__':
    typer_app()
