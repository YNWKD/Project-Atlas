def main():
    print("=" * 50)
    print("           Welcome to Project ATLAS")
    print("=" * 50)
    print()
    print("Status      : Online")
    print("Version     : 0.2.0")
    print("Developer   : YNWKD")
    print("Environment : Ubuntu WSL")
    print()
    print("Atlas is ready.")
    print()

    while True:
        command = input("Atlas > ")

        if command == "hello":
            print("Hello, YNWKD!")

        elif command == "version":
            print("Atlas Core v0.2.0")

        elif command == "help":
            print("Available commands:")
            print("  hello")
            print("  version")
            print("  help")
            print("  exit")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()