from collections import defaultdict,deque
class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:

        output = 0
        edge_set = set()        # Set for storing edges
        visited = set()         # Set for tracking visited edges while doing DFS
        adj = defaultdict(list) # Dictioanry to store adjacent/neighbours
        adj_stk = [0]           # stack to be used for DFS
        visited.add(0)          # Initialize visited set with 0


        #Procedure to store edges as a set and make dictionary for each node with value as neighbours
        for edge in edges:
            edge_set.add(tuple(edge))
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # Simple DFS to check for each node with its neighbour wheather they need to be modofied or not
        while adj_stk!=[]:
            p =adj_stk.pop()
            for neigh in adj[p]:
                if neigh not in visited:
                    if (p,neigh) in edge_set:
                        output+=1
                    visited.add(neigh)
                    adj_stk.append(neigh)

        return output
