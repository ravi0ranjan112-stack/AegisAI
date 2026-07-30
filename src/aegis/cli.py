from aegis.kernel.kernel import AegisKernel
from aegis.version import __version__


def main() -> None:
    print("=" * 60)
    print(f"Aegis AI v{__version__}")
    print("=" * 60)

    kernel = AegisKernel()

    print()
    print("Provider :", kernel.router.active)
    print("Type 'exit' to quit.")
    print()

    while True:
        prompt = input("You > ").strip()

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit"}:
            print("\nGoodbye.")
            break

        response = kernel.ai.ask(prompt)

        print(f"Aegis > {response}")
        print()
