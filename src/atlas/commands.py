from config import VERSION
import os
import platform
import sys
from datetime import datetime


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
    print("  time")
    print("  date")
    print("  pwd")
    print("  whoami")
    print("  system")
    print("  python")


def exit_command():
    print("Goodbye!")
    return False


# 🧠 NEW SYSTEM COMMANDS

def time_command():
    now = datetime.now().strftime("%H:%M:%S")
    print(now)


def date_command():
    now = datetime.now().strftime("%d %B %Y")
    print(now)


def pwd_command():
    print(os.getcwd())


def whoami_command():
    print(os.getenv("USER") or os.getenv("USERNAME"))


def system_command():
    print(platform.system())
    print(platform.version())
    print(platform.machine())


def python_command():
    print(sys.version)


COMMANDS = {
    "hello": hello_command,
    "version": version_command,
    "help": help_command,
    "exit": exit_command,
    "time": time_command,
    "date": date_command,
    "pwd": pwd_command,
    "whoami": whoami_command,
    "system": system_command,
    "python": python_command,
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
