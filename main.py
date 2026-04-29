from agent import Agent

def main():
    agent = Agent()

    while True:
        user_input = input("Enter your request: ")

        if user_input.lower() == "exit":
            break

        result = agent.process_input(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()