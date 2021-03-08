import pygame
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green
from queue import Queue
import custom_func
from itertools import repeat
"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""

def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code

    # Initialize 
    visited = [0 for i in repeat(None,len(graph))]
    #visited = []
    #for x in range(len(graph)):
        #visited.append(0)

    # add the start node to the queue -> 0 is start node
    q = Queue(maxsize = 11)
    q.put(start) 

    pathed = [] # save path we traced
    # set the visited value of node 0 to visited
    visited[start] = 1

    # get adjacency list
    adjacency = custom_func.Adjacency(graph)

    # Set color of node start 
    graph[start][3] = orange
    graphUI.updateUI()

    breaker = False
    while q.empty() == False:
        visit = q.get();
        pathed.append(visit)

        # set color of present vertex 
        graph[visit][3] = yellow
        graphUI.updateUI()
        pygame.time.delay(500)

        # if present vertex is a hang vertex or is a leaf, then we trace back to previous root node

        # find adjacent vertex of the present vertex
        for y in adjacency[visit]:
            # check if route exists and that node is not visited
            if  visited[y] == 0:
                visited[y] = 1; # mark as visited

                # set color 
                graph[y][3] = red;
                graphUI.updateUI();
                pygame.time.delay(500)
                edges[edge_id(visit, y)][1] = white
                graphUI.updateUI()

                if y == goal:
                    graph[y][3] = purple
                    graph[visit][3] = blue
                    graph[start][3] = orange
                    graphUI.updateUI()
                    pathed.append(y)
                    breaker = True
                    break

                # put adjacent vertex to queue
                q.put(y);

        if breaker == True:
            break

        graph[visit][3] = blue
        graphUI.updateUI()


    #print(pathed,graph,edge_id,edges)
    custom_func.drawPath0(pathed,graph,edge_id,edges)
    print("Implement BFS algorithm.")

    # set shortest path color
    pass


pathed = []
visited = [0 for i in repeat(None,100)]
start_vertex = []
present_index = 0
def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    global pathed
    pathed.append(start)
    global start_vertex1
    start_vertex.append(start)

    # Set color of node start
    global visited 
    visited[start] = 1
    graph[start][3] = yellow
    graphUI.updateUI()
    pygame.time.delay(500)
    # get adjacency list
    adjacency = custom_func.Adjacency(graph)

    # if node has no adjacent vertex, then trace back to previous node
    for y in adjacency[start]:
        if visited[y] == 0:
            visited[y] = 1
            graph[y][3] = red
            graphUI.updateUI()
            edges[edge_id(start, y)][1] = white
            graphUI.updateUI()

            if y == goal:
                graph[y][3] = purple
                graph[start_vertex[0]][3] = orange
                graph[start][3] = blue
                graphUI.updateUI()
                pathed.append(goal)
                for x in range(len(pathed) - 1):
                    edges[edge_id(pathed[x], pathed[x + 1])][1] = green
                graphUI.updateUI()
                return False

            graph[start][3] = blue
            graphUI.updateUI()
            return DFS(graph,edges,edge_id,y,goal)
        #continue

    # if present vertex is a hang vertex or is a leaf, then we trace back to previous root node
    graph[start][3] = blue
    graphUI.updateUI()
    if visited[start] == 0:
        visited[start] = 1
    global present_index 
    present_index = pathed.index(start)
    return DFS(graph,edges,edge_id,pathed[present_index - 1],goal)

    print("Implement DFS algorithm.")
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    # initialize
    visited = [0 for i in repeat(None,len(graph))] # list of costed vertex
    closed  = [] # list of reached vertex
    cost    = [] # list contain cost to reach vertex (as a open vertex list)

    # get adjacency list
    adjacency = custom_func.Adjacency(graph)

    # Set color of node start 
    graph[start][3] = orange
    graphUI.updateUI()

    # begin with start node
    visited[start] = 1
    cost.append((start,0,start))  # cost[(this_vertex,cost1,previous_vertex1),(this_vertex2,cost2,previous_vertex2),...]

    breaker = False
    while all(cost) != False:
        visit = cost[0][0]
        previous = cost[0][2]
        closed.append((visit,previous))

        # set present 
        graph[visit][3] = yellow
        graphUI.updateUI()
        pygame.time.delay(500)

        for y in adjacency[visit]:
            # check if route exists and that node is not visited
            if  visited[y] == 0:
                visited[y] = 1                
                
                # set color 
                graph[y][3] = red
                graphUI.updateUI()

                # set all edge between node in a array.
                edges[edge_id(visit, y)][1] = white
                graphUI.updateUI()

                if y == goal:
                    graph[y][3] = purple
                    graph[visit][3] = blue
                    graph[start][3] = orange
                    graphUI.updateUI()
                    closed.append((goal,visit))
                    breaker = True
                    break

                # calculate cost to reach
                from_node = graph[visit][0]
                to_node = graph[y][0]
                present_cost = custom_func.Distance(from_node,to_node)
                present_cost += cost[0][1]
                cost.append((y,present_cost,visit))

        if breaker == True:
            break

        graph[visit][3] = blue
        graphUI.updateUI()

        cost.pop(0)
        cost.sort(key = custom_func.takeSecond) # sort by cost of each vertex

    custom_func.drawPath1(closed,graph,edge_id,edges) # draw found-path

    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    visited = [0 for i in repeat(None,len(graph))] # list of costed vertex
    closed  = [] # list of reached vertex
    cost    = [] # list contain cost to reach vertex (as a open vertex list)

    # get adjacency list
    adjacency = custom_func.Adjacency(graph)

    # Set color of node start 
    graph[start][3] = orange
    graphUI.updateUI()

    # begin with start node
    visited[start] = 1
    cost.append((start,0,0))  # cost[(this_vertex,cost1,f(1)),(this_vertex2,cost2,f(2)),...] 
                            #---- f(x) = g(x) + h(x) whith h(x) is a heuristic function get distance from x to goal
                                 # and g(x) is length of path that we traced

    breaker = False
    while all(cost) != False:
        visit = cost[0][0]
        closed.append(visit)

        # set present 
        graph[visit][3] = yellow
        graphUI.updateUI()
        pygame.time.delay(500)

        for y in adjacency[visit]:
            # check if route exists and that node is not visited
            if  visited[y] == 0:
                visited[y] = 1;                
                
                # set color 
                graph[y][3] = red
                graphUI.updateUI()

                # set all edge between node in a array.
                edges[edge_id(visit, y)][1] = white
                graphUI.updateUI()

                if y == goal:
                    graph[y][3] = purple
                    graph[visit][3] = blue
                    graph[start][3] = orange
                    graphUI.updateUI()
                    closed.append(goal)
                    breaker = True
                    break

                # calculate cost to reach
                # f(x) = g(x) + h(x)
                from_node = graph[visit][0]
                to_node = graph[y][0]
                present_cost = custom_func.Distance(from_node,to_node)  # g(x)
                h_x = custom_func.Distance(graph[y][0],graph[goal][0])  # h(x)
                g_x = h_x + present_cost 
                present_cost += cost[0][1]
                cost.append((y,present_cost,g_x))

        if breaker == True:
            break

        graph[visit][3] = blue
        graphUI.updateUI()

        cost.pop(0)
        cost.sort(key = custom_func.takeThird) # sort by heuristic function

    custom_func.drawPath2(closed,graph,edge_id,edges) # draw found-path


    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()

