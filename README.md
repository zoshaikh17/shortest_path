# Shortest_Path
In this project, I tried to design, implement, and test a greedy algorithm (Dijkstra’s Algorithm) and
a dynamic programming algorithm (Bellman Ford) in order to find the shortest path to go to other buildings
from the Computer Science Building.

## Dijkstra’s Algorithm
Algorithm:
1. Create a set for a shortest path tree that keeps track of vertices included in shortest path tree, i.e., whose
minimum distance from source is calculated and finalized. Initially, this set is empty.
2. Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE.
Assign distance value as 0 for the source vertex so that it is picked first.
3. While shortest path tree set doesn’t include all vertices
• Pick a vertex u which is not there in shortest path tree and has minimum distance value.
• Include u to shortest path tree
• Update distance value of all adjacent vertices of u. To update the distance values, iterate through
all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and
weight of edge u-v, is less than the distance value of v, then update the distance value of v.

## Bellman-Ford Algorithm
Algorithm:
1. Create an array dist[] of size |V| with all values as infinite except dist[src] where source is source vertex.
2. Calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in graph.
• each edge u-v If dist[v] > dist[u] + weight of edge uv, then update dist[v] dist[v] = dist[u] + weight
of edge uv
3. If there is a negative weight cycle in graph. For each edge u-v,
If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle”
4. Step 2 guarantees the shortest distances if the graph doesn’t contain a negative weight cycle. If we iterate
through all edges one more time and get a shorter path for any vertex, then there is a negative weight
cycle.

## Result
![Dijkstra](https://user-images.githubusercontent.com/55362861/107860008-c2ac6500-6e02-11eb-8225-4a08709cc2c1.PNG)
![Bellman](https://user-images.githubusercontent.com/55362861/107860007-c213ce80-6e02-11eb-8e8c-885aa63842a9.PNG)


