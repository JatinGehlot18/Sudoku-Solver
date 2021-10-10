import time

start = time.time()
a = 0


def nextempty(graph):
    for x in range(0, 9):
        for y in range(0, 9):
            if graph[x][y] == 0:
                return x, y
    return -1, -1


def checking(graph, i, j, e):
    rowok = all([e != graph[x][j] for x in range(0, 9)])
    if rowok:
        columnok = all([e != graph[i][x] for x in range(0, 9)])
        if columnok:
            cordx = 3*(i//3)
            cordy = 3*(j//3)
            for x in range(cordx, cordx+3):
                for y in range(cordy, cordy+3):
                    if graph[x][y] == e:
                        return False
            return True
    return False


def solvesoduku(graph, i, j):

    global a

    i, j = nextempty(graph)
    if i == -1:
        return True

    for e in range(1, 10):
        if checking(graph, i, j, e):
            graph[i][j] = e
            if solvesoduku(graph, i, j):
                return True

            a += 1
            graph[i][j] = 0
    return False


graph = []

for i in range(0, 9):
    b = input()
    lists = []
    for j in range(0, 9):
        c = int(b[j*2])
        lists.append(c)
    graph.append(lists)

print("\n")

if solvesoduku(graph, 0, 0):
    for i in range(9):
        for j in range(9):
            if j == 8:
                print(graph[i][j], end="\n")
            else:
                print(graph[i][j], end=" ")
    print(a)

end = time.time()
print(end-start)
