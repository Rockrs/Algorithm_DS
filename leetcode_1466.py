from collections import defaultdict,deque
class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:

        output = 0
        edge_set = set()
        visited = set()
        adj = defaultdict(list)
        adj_stk = [0]
        visited.add(0)

        for edge in edges:
            edge_set.add(tuple(edge))
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        while adj_stk!=[]:
            p =adj_stk.pop()
            for neigh in adj[p]:
                if neigh not in visited:
                    if (p,neigh) in edge_set:
                        output+=1
                    visited.add(neigh)
                    adj_stk.append(neigh)

        return output
