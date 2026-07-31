from aegis.kernel.kernel import AegisKernel
from aegis.version import __version__


def print_banner() -> None:
    print("=" * 60)
    print(f"Aegis AI v{__version__}")
    print("=" * 60)


def print_help() -> None:
    print()
    print("Available commands:")
    print("  /help      Show this help")
    print("  /provider  Show active provider")
    print("  /history   Show conversation history")
    print("  /clear     Clear conversation")
    print("  /shell     Run an allowed shell command")
    print()


def handle_command(kernel: AegisKernel, prompt: str) -> bool:
    if prompt == "/help":
        print_help()
        return True

    if prompt == "/provider":
        print()
        print(f"Active provider: {kernel.ai.active_provider}")
        print()
        return True

    if prompt == "/history":
        print()

        if not kernel.session.messages:
            print("No conversation yet.")
        else:
            for message in kernel.session.messages:
                print(f"{message.role}: {message.content}")

        print()
        return True

    if prompt == "/clear":
        kernel.session.clear()
        print()
        print("Conversation cleared.")
        print()
        return True

    if prompt.startswith("/shell "):
        command = prompt.removeprefix("/shell ").strip()

        print()
        print(kernel.tools.execute("shell", command))
        print()
        return True

    return False


def main() -> None:
    print_banner()

    kernel = AegisKernel()

    print()
    print("Provider :", kernel.router.active)
    print("Type 'exit' to quit.")
    print("Type '/help' for commands.")
    print()

    while True:
        prompt = input("You > ").strip()

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit"}:
            print("\nGoodbye.")
            break

        if handle_command(kernel, prompt):
            continue

        print("Aegis > ", end="", flush=True)

        for chunk in kernel.ai.stream(prompt):
            print(chunk, end="", flush=True)

        print("\n")
