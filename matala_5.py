# Question 1
import numpy as np
from typing import List

class Agent:

    values = []

    def __init__(self, value):
        self.values = value

    def item_value(self, item_index:int) ->float:
        assert item_index < len(self.values)
        return self.values[item_index]

def is_EF1(agents:List[Agent], bundles:List[List[int]]) ->bool:
    for i in range(len(agents)):
        for j in range(i+1, len(agents)):
            if envy_check(agents[i], agents[j], bundles[i], bundles[j]):
                return True

    return False

# check if agent_1 has no envy of agent_2
# also if agent_2 has no envy of agent_1
def envy_check(agent_1:Agent, agent_2:Agent, bundle_1:List[int], bundle_2:List[int]):

    # first check
    agent_1_satisfaction = calculate_items_value(agent_1, bundle_1, bundle_2)
    print(agent_1_satisfaction)
    agent_2_satisfaction = calculate_items_value(agent_2, bundle_2, bundle_1)
    print(agent_2_satisfaction)
    both_satisfied = agent_1_satisfaction and agent_2_satisfaction

    # further check with the delete of one item each time
    i, j = 0, 0
    while not both_satisfied and i < len(bundle_1) and j < len(bundle_2):
        agent_1_satisfaction = calculate_items_value(agent_1, bundle_1, np.delete(np.array(bundle_2), j)) \
            if not agent_1_satisfaction \
            else True
        agent_2_satisfaction = calculate_items_value(agent_2, bundle_2, np.delete(np.array(bundle_1), j)) \
            if not agent_2_satisfaction \
            else True
        both_satisfied = agent_1_satisfaction and agent_2_satisfaction
        i, j = i+1, j+1
    return both_satisfied

# summerize items value in agent eyes
def calculate_items_value(agent:Agent, bundle_1:List[int], bundle_2:List[int]):
    value_1 = sum(agent.item_value(item) for item in bundle_1)
    value_2 = sum(agent.item_value(item) for item in bundle_2)
    print(value_1,">=",value_2, end=" ")
    return value_1 >= value_2


if __name__ == "__main__":
    # false example
    agent1 = Agent([0, 40, 5, 15, 20, 0])
    agent2 = Agent([30, 30, 30, 5, 2.5, 2.5])
    print("\n",is_EF1([agent1, agent2], [[0, 1, 2], [3, 4, 5]]),"\n")

    # true example
    agent1 = Agent([20, 10, 15, 15, 20, 0])
    agent2 = Agent([30, 20, 10, 15, 22.5, 2.5])
    print("\n", is_EF1([agent1, agent2], [[0, 1, 2], [3, 4, 5]]))
