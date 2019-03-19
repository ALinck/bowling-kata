

class BowlingGame:

    def __init__(self):
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        score = 0
        i = 0
        for frame in range(10):
            if self._is_strike(i):
                score += 10 + self._strike_bonus(i)
                i += 1
            elif self._is_spare(i):
                score += 10 + self._spare_bonus(i)
                i += 2
            else:
                score += self._rolls[i] + self._rolls[i+1]
                i += 2
        return score

    def _is_strike(self, i):
        return self._rolls[i] == 10

    def _is_spare(self, i):
        return self._rolls[i] + self._rolls[i+1] == 10

    def _strike_bonus(self, i):
        return self._rolls[i+1] + self._rolls[i+2]

    def _spare_bonus(self, i):
        return self._rolls[i+2]