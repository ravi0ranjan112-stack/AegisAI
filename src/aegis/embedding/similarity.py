class Similarity:
    def score(self, left: list[float], right: list[float]) -> float:
        if not left or not right:
            return 0.0

        size = min(len(left), len(right))
        return sum(left[i] * right[i] for i in range(size))
