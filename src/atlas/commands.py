from config import VERSION


def hello_command():
    print("Hello, YNWKD!")


def version_command():
    print(f"RIO v{VERSION}")


def help_command():
    print("Available commands:")
    print("  hello")
    print("  version")
    print("  help")
    print("  exit")


def exit_command():
    print("Goodbye!")
    return False


COMMANDS = {
    "hello": hello_command,
    "version": version_command,
    "help": help_command,
    "exit": exit_command,
}


def handle_command(command):
    command = command.strip().lower()

    if command in COMMANDS:
        result = COMMANDS[command]()

        if command == "exit":
            return False

        return True

    print("Unknown command. Type 'help'.")
    return True
