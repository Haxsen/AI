import cv2
import numpy as np

def findPath(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return path
  for node in graph[start]:
    if node not in path:
      newpath = findPath(graph, node, end, path)
      if newpath:
        return newpath
      return None

def findDegree(adjList, n):
    _in = [0] * n
    out = [0] * n

    for i in range(0, len(adjList)):

        List = adjList[i]
        out[i] = len(List)
        for j in range(0, len(List)):
            _in[List[j]] += 1
    print("Vertex\tIn\tOut")
    for k in range(0, n):
        print(str(k) + "\t" + str(_in[k]) + "\t" + str(out[k]))

def findAllPaths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = findAllPaths(graph, node, end, path)
    for newpath in newpaths:
      paths.append(newpath)
  return paths

graph1 ={
'6':['4'],
'4':['5','3'],
'5':['1','2','4'],
'3':['4', '2'],
'2':['3', '1','2'],
'1':['5', '2']
}

graph2 ={
'e':['b'],
'a':['e','b'],
'b':['e','a','d'],
'd':['a', 'b'],
'c':['d']
}

graph3 ={
'7':['11','8'],
'5':['11'],
'3':['8','10'],
'11':['9', '10'],
'8':['9'],
'2':[],
'9':[],
'10':[]
}

graph4 ={
'a':['b'],
'b':['c','d','e'],
'c':['e'],
'd':['e'],
'e':['f'],
'f':[],
'g':['d']
}

n = len(graph4)
print('n is ', n)

print("\nGraph Paths: ")
print(findPath(graph1, '6', '1'))
print(findPath(graph2, 'c', 'c'))
print(findPath(graph3, '7', '9'))
print(findPath(graph4, 'a', 'f'))

print("\nAll Possible Paths:")
print(findAllPaths(graph4, 'a', 'f'))
print(findAllPaths(graph3, '7', '9'))

for key in graph1:
    print(key,' - ',graph1[key],' Degree: ',len(graph1[key]))

for key in graph2:
    print(key,' - ',graph2[key],' Degree: ',len(graph2[key]))

for key in graph3:
    print(key,' - ',graph3[key],' Out-Degree: ',len(graph3[key]))

print("\nIn-Degree of graph1")
for key in graph1:
    count=0
    for key2 in graph1:
        r=graph1[key2]
        for i in range(len(r)):
            if key==r[i]:
                count=count+1
    print(key+" : ",count)

print("\nIn-Degree of graph2")
for key in graph2:
    count=0
    for key2 in graph2:
        r=graph2[key2]
        for i in range(len(r)):
            if key==r[i]:
                count=count+1
    print(key+" : ",count)