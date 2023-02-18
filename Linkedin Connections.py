'''For n number of people and m number of connections. A person can send a message to a person if they are at most their 3rd connection. A first connection is someone who is directly connected to the person, second connection is someone who is connected to the first connection of the person and not the directly connected to the person, a third connection is connected to the first connection of the first connection of the person and so on.... For given n, connections and the person who will send the message, find if the person can send a message to a given person.'''

n = int(input('No. of people: '))
m = int(input('No. of connections: '))
connections = []
for a in range(m):
    lst = input().split(' ')
    lst[0] = int(lst[0])
    lst[1] = int(lst[1])
    connections.append(lst)

k = int(input('The person who wants to send the requests: '))
q = int(input('No. of queries: '))

matrix = []

for i in range(n):
    lst = []
    for j in range(n):
        lst.append(0)
    matrix.append(lst)

for i in connections:
    matrix[i[0] - 1][i[1] - 1] = 1
    matrix[i[1] - 1][i[0] - 1] = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            for a in range(n):
                if matrix[j][a] == 1 and matrix[i][a] == 0 and i != a:
                    matrix[i][a] = 2
        elif matrix[i][j] == 2:
            for a in range(n):
                if matrix[j][a] == 2 and matrix[i][a] == 0 and i != a:
                    matrix[i][a] = 3
        

for z in range(q):
    b = int(input())
    if matrix[k - 1][b - 1] == 1:
        print('Yes1')
    elif matrix[k - 1][b - 1] == 2:
        print('Yes2')
    elif matrix[k - 1][b - 1] == 3:
        print('Yes3')
    else:
        print('No')
