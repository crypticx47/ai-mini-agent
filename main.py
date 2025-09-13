from agent import AIAgent

def main():
    agent = AIAgent()
    environment_state = {}  # Simple placeholder
    print(f"AI Agent '{agent.name}' running...")

    for step in range(10):
        action = agent.decide_action(environment_state)
        print(f"Step {step+1}: Agent decides to {action}")

if __name__ == "__main__":
    main()
