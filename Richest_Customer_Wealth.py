# My original solution:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m, n = len(accounts), len(accounts[0])
        wealths = [None] * m
        for i in range(m):
            wealths[i] = sum(accounts[i])
        return max(wealths)

# Others' solutions:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
--------------------------------------------------------------
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts) # Using generator
--------------------------------------------------------------
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(customer) for customer in accounts]) # Using list comprehension
