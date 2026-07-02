from config import VERSION


def handle_command(command):
    command = command.strip().lower()

    if command == "hello":
        print("Hello, YNWKD!")

    elif command == "version":
        print(f"RIO v{VERSION}")

    elif command == "help":
        print("Available commands:")
        print("  hello")
        print("  version")
        print("  help")
        print("  exit")

    elif command == "exit":
        print("Goodbye!")
        return False

    else:
        print("Unknown command. Type 'help'.")

    return True
