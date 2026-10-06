class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        total_cost = 0
        edges_connected = 0
        
        # minDist[i] stores the minimum distance to connect node i to the MST
        min_dist = [float('inf')] * n
        # visited[i] tracks whether node i is already included in the MST
        visited = [False] * n
        
        # Start with node 0
        min_dist[0] = 0
        
        while edges_connected < n:
            curr_node = -1
            curr_min_dist = float('inf')
            
            # Find the unvisited node with the minimum distance to the current MST
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_min_dist:
                    curr_min_dist = min_dist[i]
                    curr_node = i
            
            # Add the selected node to the MST
            visited[curr_node] = True
            total_cost += curr_min_dist
            edges_connected += 1
            
            # Update min_dist for adjacent unvisited nodes
            x1, y1 = points[curr_node]
            for next_node in range(n):
                if not visited[next_node]:
                    x2, y2 = points[next_node]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist
                        
        return total_cost