from config import VERSION, DEVELOPER, ENVIRONMENT
from assistant import Assistant


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

    atlas = Assistant()

    atlas.start()


if __name__ == "__main__":
    main()