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
        self.history = []

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

    def show_history(self):
        if not self.history:
            print("No commands yet.")
            return

        print("Command History:")
        for index, command in enumerate(self.history, start=1):
            print(f"{index}. {command}")

    def run(self):
        self.display_banner()

        logger.info("RIO started.")

        while True:
            command = input(f"{self.name} > ")
            self.history.append(command)

            logger.info(f"Command received: {command}")

            # Built-in assistant command
            if command.strip().lower() == "history":
                self.show_history()
                continue

            # All other commands
            if not handle_command(command):
                logger.info("RIO shutting down.")
                break
