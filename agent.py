import random

class AIAgent:
    def __init__(self, name="MiniAgent"):
        self.name = name

    def decide_action(self, environment_state):
        """
        Simple agent logic:
        Returns a random action based on the environment state.
        """
        actions = ["move_left", "move_right", "move_up", "move_down", "stay"]
        # Here you can add more complex logic or ML-based decisions
        action = random.choice(actions)
        return action
