# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 == parent2:
            return

        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        typeOne = UnionFind(n + 1)
        typeTwo = UnionFind(n +1)
        ans = 0 
        edges.sort(key = lambda x:-x[0])
        
        for t , a , b in edges:
            if t ==  3:
                if typeOne.find(a) == typeOne.find(b) and typeTwo.find(a) == typeTwo.find(b):
                    ans += 1
                else:
                    if typeOne.find(a) != typeOne.find(b):
                        typeOne.union(a , b)
                    
                    if typeTwo.find(a) != typeTwo.find(b):
                        typeTwo.union(a , b)

            elif t == 2:
                if typeTwo.find(a) != typeTwo.find(b):
                    typeTwo.union(a , b)
                else:
                    ans += 1
            else:
                if typeOne.find(a) != typeOne.find(b):
                    typeOne.union(a , b)

                else:
                    ans +=1


        return ans if typeOne.size[typeOne.find(1)] == typeTwo.size[typeTwo.find(1)] == n else -1





        
        