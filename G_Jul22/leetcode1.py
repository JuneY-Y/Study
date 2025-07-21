class Solution(object):
    def findCircleNum(self, isConnected):
        
        n=len(isConnected)
        visited=set()

        def dfs(i):
            for j in range(n):