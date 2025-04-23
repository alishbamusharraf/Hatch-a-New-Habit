class Habit:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.progress = 0

    def complete(self):
        if self.progress < self.goal:
            self.progress += 1

    def is_hatched(self):
        return self.progress >= self.goal
