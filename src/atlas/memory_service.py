import json
import os


MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "memory.json"
)


def load_memory():
    """
    Load all memories from memory.json.
    """

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_memory(memories):
    """
    Save the memory list back to memory.json.
    """

    with open(MEMORY_FILE, "w") as file:
        json.dump(memories, file, indent=4)


def remember(text):
    """
    Store a new memory.
    """

    memories = load_memory()

    memories.append(text)

    save_memory(memories)

    print("Memory saved.")


def recall(keyword=""):
    """
    Recall memories.

    If no keyword is supplied,
    show every stored memory.
    """

    memories = load_memory()

    if not memories:
        print("No memories found.")
        return

    if not keyword:

        print("\nStored Memories:\n")

        for index, memory in enumerate(memories, start=1):
            print(f"{index}. {memory}")

        return

    results = []

    for memory in memories:
        if keyword.lower() in memory.lower():
            results.append(memory)

    if not results:
        print("No matching memories found.")
        return

    print()

    for index, memory in enumerate(results, start=1):
        print(f"{index}. {memory}")
