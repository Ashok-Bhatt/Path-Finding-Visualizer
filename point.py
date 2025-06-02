class aStarPoint:

    def __init__(self, x, y, current_cost, heuristic_cost):
        self.x = x
        self.y = y
        self.current_cost = current_cost
        self.heuristic_cost = heuristic_cost
    
    def __lt__(self, other):
        return (self.current_cost + self.heuristic_cost) < (other.current_cost + other.heuristic_cost)
    

class bestFitSearchPoint:

    def __init__(self, x, y, heuristic_cost):
        self.x = x
        self.y = y
        self.heuristic_cost = heuristic_cost
    
    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost