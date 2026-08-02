class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest = candies[0]
        result = []

        for c in candies:
            if c > highest:
                highest = c
        for c in candies:
            result.append(c + extraCandies >= highest)
        return result