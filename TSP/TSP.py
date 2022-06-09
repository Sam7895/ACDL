import time 
import random as r 
answer = [] 
path = [] 
def TSP(graph, visited, currPos, n, count, cost, order): 
  if(count == n and graph[currPos][0]): 
   answer.append(cost + graph[currPos][0]) 
   order.append(1) 
   temp = order.copy() 
   path.append(temp) 
   order.pop() 
  return 
  for i in range(n): 
    if(visited[i] == False and graph[currPos][i]): 
      visited[i] = True 
      order.append(i+1) 
      TSP(graph, visited, i, n, count + 1, cost + graph[currPos][i], order) 
      visited[i] = False 
      order.pop() 
  n = int(input("Enter the number of nodes")) 
  graph = [] 

  for i in range(n): 
    internalList = [] 
    for j in range(n): 
      if i!=j: 
        internalList.append(int(input("Distance between {} and {}:".format(i+1, j+1)))) 
        #internalList.append(r.randint(1,100)) 
      else: 
        internalList.append(0) 
      graph.append(internalList) 
  visited = [False for i in range(n)] 
  visited[0] = True 
  t1 = time.time() 
  order = [1] 
  TSP(graph, visited, 0, n, 1, 0, order) 
  duration = time.time() - t1 
  print("The shortest path is ", path[answer.index(min(answer))]) 
  print("\nShortest Distance is {} \n".format(min(answer))) 
  print('Answer found in ', duration) 

