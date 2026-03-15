#1622. Fancy Sequence

class Fancy:

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # We need to store a value x such that (x * mul + add) % MOD == val
        # So, x = (val - add) * mul^(-1) % MOD
        # We use pow(self.mul, self.MOD - 2, self.MOD) for modular inverse
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        raw_val = ((val - self.add) * inv_mul) % self.MOD
        self.seq.append(raw_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Apply the current global multiplier and adder to the raw value
        return (self.seq[idx] * self.mul + self.add) % self.MOD
    
# Time Complexity:
# - append: O(1)
# - addAll: O(1)
# - multAll: O(1)
# - getIndex: O(1)
# Space Complexity: O(n), where n is the number of elements appended to the sequence.