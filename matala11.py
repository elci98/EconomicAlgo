# Elchanan Mahatsri ID 311326052

from typing import List
import numpy as np
import random
from decimal import Decimal


def f(C:float, i:int, t:float) -> float:
    return C * np.minimum(1, i * t)

def compute_budget(total_budget:float, citizen_votes:List[List]) -> List[float]:

    assert len(citizen_votes) > 0
    subjects_size =  len(citizen_votes[0])
    ans = [0 for _ in range(subjects_size)] # init the answer array
    l, r = 0, 1
    while True:
        t = (l + r) / 2
        for j in range(subjects_size): # iterate every subject
            votes = []
            for citizen_vote in citizen_votes: # create an array containing all votes for subject j
                votes.append(citizen_vote[j])
            for i in range(1,len(citizen_votes)): # fixed votes
                votes.append(f(total_budget, i, t))
            ans[j] = np.median(votes) # calculate the median for each set of votes
        medians_sum = np.sum(ans)
        if medians_sum == total_budget:
            break
        if medians_sum > total_budget:
            r = t
        else:
            l = t

    return ans





if __name__ == "__main__":
    print(compute_budget(100, [[100, 0, 0], [0, 0, 100]]))
    print(compute_budget(30, [[15, 15, 0], [0, 20, 10], [3, 0, 27]]))
    print(compute_budget(100, [[100, 0, 0], [0, 0, 100], [0, 100, 0]]))
    print(compute_budget(30, [
                            [0,0,6,0,0,6,6,6,6],
                            [0,6,0,6,6,6,6,0,0],
                            [6,0,0,6,6,0,0,6,6]
                        ]))


