import graphUI
import sys
import math  
from node_color import green

global_graph = None
adjecency = None
edges = None

def Adjacency(graph):
	global_graph = graph
	#print(global_graph)
	global adjecency
	adjecency = []
	for i in range(len(global_graph)):
		adjecency.append(global_graph[i][1])
	return adjecency

	pass

def Distance(a, b):
	xa = a[0]
	xb = b[0]
	ya = a[1]
	yb = b[1]
	distance = math.sqrt(pow(xa-xb,2) + pow(yb-ya,2))
	return distance

	pass

def takeSecond(elem):
	return elem[1]
	pass

def takeThird(elem):
	return elem[2]
	pass

def drawPath0(visited_list,graph,edge_id,edges):
    print(visited_list)
    length = len(visited_list)
    next_index = 1
    for x in range(len(visited_list) - 1):
        adjecency_node = graph[visited_list[x]][1]
        while next_index < length and visited_list[next_index] in adjecency_node: 		
            edges[edge_id(visited_list[x],visited_list[next_index])][1] = green
            graphUI.updateUI()
            next_index += 1


def drawPath1(visited_list,graph,edge_id,edges):
    for x in range(1,len(visited_list)):
        edges[edge_id(visited_list[x][0], visited_list[x][1])][1] = green
        graphUI.updateUI()
    pass

def drawPath2(visited_list,graph,edge_id,edges):
    for x in range(0,len(visited_list) - 1):
        edges[edge_id(visited_list[x], visited_list[x+1])][1] = green
        graphUI.updateUI()
        x += 2
    pass
