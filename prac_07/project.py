"""
Estimate: 25 minutes
Actual:   30 minutes
"""


class Project:

    def __init__(self, name, start_date, priority, cost, completion):
        self.completion = completion
        self.cost = cost
        self.priority = priority
        self.start_date = start_date
        self.name = name

    def __str__(self):
        return f"Project: {self.name} Start date: {self.start_date} Cost: {self.cost} Priority: {self.priority}" \
               f" Completion: {self.completion}"

    def get_priority(self):
        return self.priority

    def __lt__(self, other):
        return self.priority - other.priority < 0
