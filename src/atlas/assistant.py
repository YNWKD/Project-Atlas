from config import (
    APP_NAME,
    ASSISTANT_NAME,
    VERSION,
    DEVELOPER,
    ENVIRONMENT,
)

from commands import handle_command
from logger import logger


class RIO:
    def __init__(self):
        self.name = ASSISTANT_NAME
        self.version = VERSION
        self.developer = DEVELOPER
        self.environment = ENVIRONMENT

    def display_banner(self):
        print("=" * 50)
        print(f"        Welcome to {APP_NAME}")
        print("=" * 50)
        print()
        print("Status      : Online")
        print(f"Assistant   : {self.name}")
        print(f"Version     : {self.version}")
        print(f"Developer   : {self.developer}")
        print(f"Environment : {self.environment}")
        print()
        print(f"{self.name} is ready.")
        print()

    def run(self):
        self.display_banner()

        logger.info("RIO started.")

        while True:
            command = input(f"{self.name} > ")

            logger.info(f"Command received: {command}")

            if not handle_command(command):
                logger.info("RIO shutting down.")
                break
