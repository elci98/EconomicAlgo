from typing import List
import  numpy as np
import copy

def build_graph(valuations:List[List[int]]):
    ans = [ [] for _ in valuations]
    size = len(valuations)

    valuations_copy = copy.deepcopy(valuations)
    for i in range(len(valuations)): # iterate every person
        valuations_copy[i].sort(reverse=True)
        for sorted_value in valuations_copy[i]: # iterate every value

            index = valuations[i].index(sorted_value)

            if not ans[i].__contains__(index):
                ans[i].append(index)
            else:
                start_index = 1
                while ans[i].__contains__(index):
                    index = valuations[i].index(sorted_value,start_index)
                    start_index += 1
                ans[i].append(index)
    print(ans)




if __name__ == "__main__":
    build_graph([
        [200,500,500],
        [100,100,900],
        [180,190,180]
    ])

