# matala 10
# Elchanan Mahatsri ID: 311326052


import cvxpy
import functools
from typing import List

def Nash_budget(total:float, subjects: List[str], preferences:List[List[str]]):

    # There are len(subjects) projects
    projects_size = len(subjects)
    citizens_size = len(preferences)

    allocations = cvxpy.Variable(projects_size)
    allocation = {subjects[i]: allocations[i] for i in range(projects_size)}

    # There are citizens_size citizens.
    # extract their preferences from preferences[i]
    # The total budget is total -> total/citizens_size for each citizen
    donations = [total/citizens_size for _ in range(citizens_size)]
    utilities = []
    for i in range(citizens_size):
        temp = [allocation[project] for project in preferences[i]]
        len(temp) > 0 and utilities.insert(i, temp[0]) # assign value only if temp is not empty
        for j in range(1,len(temp)):
            utilities[i] += temp[j]

    # there are three constraints

    # 1. maximaize sum of logs
    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])

    # 2. v is non negative number
    positivity_constraints = [v >= 0 for v in allocations]

    # 3. the total sum of allocations is exactly the total budget = sum of donations
    sum_constraint = [cvxpy.sum(allocations)==sum(donations)]

    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints = positivity_constraints+sum_constraint)
    problem.solve()

    utility_values = [u.value for u in utilities]
    for i in range(citizens_size): # loop each citizen
        print("\nCitizen {} should donate".format(i), end=" ")
        for project in preferences[i]: # loop each project for this citizen
            print("{} to {}".format(allocation[project].value * donations[i] / utilities[i].value, project), end=", ")


if __name__ == "__main__":
    Nash_budget(500, ['a','b','c','d'], [['a','b'],['a','c'], ['a','d'], ['b','c'], ['a']])