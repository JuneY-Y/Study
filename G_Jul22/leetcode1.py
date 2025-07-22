class Solution(object):
    def findCircleNum(self, isConnected):
       ## isConnected=[[1,1,0],[1,1,0],[0,0,1]]
        n=len(isConnected)
        visited=set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        count=0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        return count