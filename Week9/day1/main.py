from orchestrator import Orchestrator

def main():
    system = Orchestrator()

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        result = system.run(user_input)
        print("\nFINAL ANSWER:\n", result)

if __name__ == "__main__":
    main()