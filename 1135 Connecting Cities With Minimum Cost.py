# There are n cities numbered from 1 to n.

# You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

# Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

# Example 1:



# Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation: 
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
# Example 2:



# Input: n = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation: 
# There is no way to connect all cities even if all edges are used.
 

# Note:

# 1 <= n <= 10000
# 1 <= connections.length <= 10000
# 1 <= connections[i][0], connections[i][1] <= n
# 0 <= connections[i][2] <= 105
# connections[i][0] != connections[i][1]



def minimumCost(n, connections):
    ## Union find
    ## sort edges by weight and union the second node to the first node
    ## sum the weight if a sceond node is not connected before the union
    ## return -1 if some nodes can not be unioned

    connections.sort(key=lambda x: x[2])

    parent = list(range(n+1))
    rank = [0] * (n + 1)
    weights = [0] * (n + 1)
    nodes = set()

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y, weight):
        xroot = find(x)
        yroot = find(y)

        if xroot == yroot: return

        if rank[xroot] < rank[yroot]:
            xroot, yroot = yroot, xroot

        parent[yroot] = xroot
        rank[xroot] = max(rank[xroot], rank[yroot] + 1)
        weights[xroot] += weights[yroot] + weight
        weights[yroot] = 0


    for x, y, weight in connections:
        union(x, y, weight)
        nodes.add(x)
        nodes.add(y)


    if len(nodes) < n:
        return -1

    final_weights = [weight for weight in weights if weight > 0]
    
    return final_weights[0] if len(final_weights) == 1 else -1
