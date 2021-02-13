import copy
from collections import defaultdict


class Building:
    def __init__(self):
        self.name = ""
        self.edgeList = []
        self.dist = float("Inf")
        self.prev = None


class Path:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance


def deletemin(source_list):
    min = float("Inf")
    current = None
    for item in source_list:
        if item.dist < min:
            min = item.dist
            current = item
    source_list.remove(current)
    return current


def printGraph(graph, src):
    print('The shortest paths from ' + src + ' to the following destinations:')
    for item in graph:
        if item != src:
            printLine = item + ' (' + str(graph[item].dist) + '): '
            pathList = []
            previous = graph[item].prev
            while previous != src:
                pathList.append(previous)
                previous = graph[previous].prev
            for path in reversed(pathList):
                printLine += path + ' --> '
            printLine += item
            print(printLine)


class Graph:
    # __init__ function
    def __init__(self):
        self.graph = defaultdict(Building)

    # Function to add key:value pair for dictionary
    def add(self, key):
        self.graph[key] = Building()
        self.graph[key].name = key

    def addEdge(self, node1, node2, distance):
        self.graph[node1].edgeList.append(Path(node2, distance))
        self.graph[node2].edgeList.append(Path(node1, distance))

    def dijsktra(self, src):
        fresh_graph = self.graph.copy()
        fresh_graph[src].dist = 0
        unvisited = []
        for item in fresh_graph:
            unvisited.append(fresh_graph[item])
        while unvisited:
            u = deletemin(unvisited)
            for item in u.edgeList:
                if fresh_graph[item.destination].dist > u.dist + item.distance:
                    fresh_graph[item.destination].dist = u.dist + item.distance
                    fresh_graph[item.destination].prev = u.name
        printGraph(fresh_graph, src)
        return fresh_graph

    def bellmanford(self, src):
        fresh_graph = self.graph.copy()
        fresh_graph[src].dist = 0
        for _ in range(fresh_graph.__sizeof__() - 1):
            for vertex in fresh_graph:
                u = fresh_graph[vertex]
                for item in u.edgeList:
                    if fresh_graph[item.destination].dist > u.dist + item.distance:
                        fresh_graph[item.destination].dist = u.dist + item.distance
                        fresh_graph[item.destination].prev = u.name
        printGraph(fresh_graph, src)
        return fresh_graph


g = Graph()
g.add('College Square')
g.add('Prince Center')
g.add('Police Dept')
g.add('Student Health Center')
g.add('Lewis Science Center')
g.add('Computer Science')
g.add('Torreyson Library')
g.add('Old Main')
g.add('Fine Art')
g.add('Student Center')
g.add('Burdick')
g.add('McALister Hall')
g.add('Wingo')
g.add('New Business Building')
g.add('Brewer-Hegeman')
g.add('Bear village Apt.')
g.add('Speech Language Hearing')
g.add('Maintenance College')
g.add('Oak Tree Apt.')

g.addEdge('College Square', 'Lewis Science Center', 200)
g.addEdge('College Square', 'Prince Center', 300)
g.addEdge('Speech Language Hearing', 'Lewis Science Center', 250)
g.addEdge('Computer Science', 'Lewis Science Center', 150)
g.addEdge('Police Dept', 'Prince Center', 100)
g.addEdge('Computer Science', 'Prince Center', 80)
g.addEdge('Torreyson Library', 'Prince Center', 30)
g.addEdge('Torreyson Library', 'Computer Science', 40)
g.addEdge('Burdick', 'Computer Science', 30)
g.addEdge('Burdick', 'Speech Language Hearing', 100)
g.addEdge('Burdick', 'Torreyson Library', 80)
g.addEdge('Old Main', 'Torreyson Library', 30)
g.addEdge('Old Main', 'Police Dept', 200)
g.addEdge('Police Dept', 'Fine Art', 50)
g.addEdge('Police Dept', 'Student Health Center', 100)
g.addEdge('Old Main', 'Fine Art', 90)
g.addEdge('Old Main', 'McALister Hall', 100)
g.addEdge('Fine Art', 'McALister Hall', 180)
g.addEdge('Burdick', 'McALister Hall', 200)
g.addEdge('Burdick', 'Maintenance College', 300)
g.addEdge('Speech Language Hearing', 'Maintenance College', 120)
g.addEdge('McALister Hall', 'Maintenance College', 150)
g.addEdge('Oak Tree Apt.', 'Maintenance College', 160)
g.addEdge('New Business Building', 'Maintenance College', 150)
g.addEdge('Wingo', 'Maintenance College', 100)
g.addEdge('New Business Building', 'Oak Tree Apt.', 30)
g.addEdge('McALister Hall', 'Wingo', 50)
g.addEdge('McALister Hall', 'Student Center', 100)
g.addEdge('Wingo', 'Student Center', 100)
g.addEdge('Fine Art', 'Student Center', 80)
g.addEdge('Student Health Center', 'Student Center', 50)
g.addEdge('New Business Building', 'Student Center', 110)
g.addEdge('New Business Building', 'Wingo', 50)
g.addEdge('Student Health Center', 'Brewer-Hegeman', 200)
g.addEdge('New Business Building', 'Brewer-Hegeman', 20)
g.addEdge('Oak Tree Apt.', 'Brewer-Hegeman', 40)
g.addEdge('Bear village Apt.', 'Brewer-Hegeman', 350)

print('\nFrom Dijkstra\'s algorithm we find:\n----------------------------------------------------------------------')
g.dijsktra('Computer Science')
print('\nFrom Bellman-Ford algorithm we find:\n----------------------------------------------------------------------')
g.bellmanford('Computer Science')
