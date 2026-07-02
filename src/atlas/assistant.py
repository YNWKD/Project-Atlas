from config import VERSION, DEVELOPER, ENVIRONMENT
from commands import handle_command


class RIO:
    def __init__(self):
        self.name = "RIO"
        self.version = VERSION
        self.developer = DEVELOPER
        self.environment = ENVIRONMENT

    def display_banner(self):
        print("=" * 50)
        print("              Welcome to Project ATLAS")
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

        while True:
            command = input(f"{self.name} > ")

            if not handle_command(command):
                break
