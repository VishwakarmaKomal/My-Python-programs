# Display the matrix in snake order

r=int(input("enter the number of row"))
c=int(input("enter number of column"))

matrix = []
for i in range(r):
    a=[]
    for j in range(0,c):
        a.append(int(input()))
    matrix.append(a)
# print matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()

print("In snake order")
#print in snake pattern
for i in range(r):
    if i == 0 or i %2== 0:
        for j in range(0,c):
            print(matrix[i][j], end= " ")

    if i % 2 !=0:
        for j in reversed(range(c)):
            print(matrix[i][j], end=" ")

    print()


