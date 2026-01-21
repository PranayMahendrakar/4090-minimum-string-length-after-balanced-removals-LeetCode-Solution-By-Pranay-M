class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        # We can remove any balanced substring
        # The minimum remaining is |count_a - count_b|
        # because we can always pair up a's and b's to remove
        count_a = s.count('a')
        count_b = s.count('b')
        return abs(count_a - count_b)