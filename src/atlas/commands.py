from config import VERSION, DEVELOPER, ENVIRONMENT
from ai_service import ask_ai
from memory_service import remember, recall, load_memory

import os
import platform
import sys
from datetime import datetime


AI_MODEL = "qwen2.5:3b"


def hello_command():
    print("Hello, YNWKD!")


def version_command():
    print(f"RIO v{VERSION}")


def about_command():
    memory_count = len(load_memory())

    print("\n==============================")
    print("RIO ASSISTANT")
    print("==============================")
    print(f"Version        : {VERSION}")
    print(f"Developer      : {DEVELOPER}")
    print(f"Environment    : {ENVIRONMENT}")
    print()
    print("Features")
    print("------------------------------")
    print(f"AI Model       : {AI_MODEL}")
    print("AI             : Enabled")
    print("Memory         : Enabled")
    print(f"Memory Entries : {memory_count}")
    print("Logger         : Enabled")
    print("History        : Enabled")
    print()
    print("Future Services")
    print("------------------------------")
    print("Hermes Agent   : Not Installed")
    print("Telegram Bot   : Not Connected")
    print("Smart Home     : Not Connected")
    print("==============================")
    print()


def help_command():
    print("Available commands:")
    print("  hello")
    print("  version")
    print("  about")
    print("  help")
    print("  ask")
    print("  remember")
    print("  recall")
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


def time_command():
    print(datetime.now().strftime("%H:%M:%S"))


def date_command():
    print(datetime.now().strftime("%d %B %Y"))


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


def ask_command(prompt=""):
    if not prompt.strip():
        prompt = input("Ask RIO AI > ").strip()

    if not prompt:
        print("Please enter a question.")
        return

    print("\nThinking...\n")

    response = ask_ai(prompt)

    print(response)


def remember_command(text=""):
    if not text.strip():
        text = input("Remember > ").strip()

    if not text:
        print("Nothing to remember.")
        return

    remember(text)


def recall_command(keyword=""):
    recall(keyword)


COMMANDS = {
    "hello": hello_command,
    "version": version_command,
    "about": about_command,
    "help": help_command,
    "ask": ask_command,
    "remember": remember_command,
    "recall": recall_command,
    "exit": exit_command,
    "time": time_command,
    "date": date_command,
    "pwd": pwd_command,
    "whoami": whoami_command,
    "system": system_command,
    "python": python_command,
}


def handle_command(command):
    parts = command.strip().split(maxsplit=1)

    if not parts:
        return True

    command_name = parts[0].lower()
    argument = parts[1] if len(parts) > 1 else ""

    if command_name in COMMANDS:

        if command_name in ["ask", "remember", "recall"]:
            COMMANDS[command_name](argument)
        else:
            COMMANDS[command_name]()

        if command_name == "exit":
            return False

        return True

    print("Unknown command. Type 'help'.")
    return True