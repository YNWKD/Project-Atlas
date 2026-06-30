from config import VERSION, DEVELOPER, ENVIRONMENT
from commands import handle_command


def main():
    print("=" * 50)
    print("           Welcome to Project ATLAS")
    print("=" * 50)
    print()
    print("Status      : Online")
    print(f"Version     : {VERSION}")
    print(f"Developer   : {DEVELOPER}")
    print(f"Environment : {ENVIRONMENT}")
    print()
    print("Atlas is ready.")
    print()

    while True:
        command = input("Atlas > ")

        if not handle_command(command):
            break


if __name__ == "__main__":
    main()