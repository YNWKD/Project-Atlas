from commands import handle_command


class Assistant:
    def __init__(self):
        self.name = "Atlas"

    def start(self):
        print(f"{self.name} is ready.")
        print()

        while True:
            command = input(f"{self.name} > ")

            if not handle_command(command):
                break