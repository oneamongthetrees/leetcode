# number of recent calls
class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        x = self.requests[0]
        lower_bound = t - 3000
        while x < lower_bound:
            self.requests.pop(0)
            x = self.requests[0]
        return len(self.requests)