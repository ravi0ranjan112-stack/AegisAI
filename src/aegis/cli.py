from aegis.runtime.app import AegisApp


def main() -> None:
    app = AegisApp()

    print(app.start())

    while True:
        try:
            command = input("You > ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        response = app.execute(command)
        print(response)

        if response == "Goodbye.":
            break


if __name__ == "__main__":
    main()
