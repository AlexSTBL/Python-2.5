
def check(graph, source, destination):
    for i in graph[source]:
        if destination in graph[source]:
            print("Signal")
            break
        else:
            print("Signal cannot reached")
            break
   

adj_list = [[0,1,2],
            [1,2],
            [2,0,3],
            [3,4],
            [4]]
             
x = int(input("Starting point: "))
y = int(input("Destination: " ))
check(adj_list, x, y)


