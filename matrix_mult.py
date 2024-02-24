import time
def NormalMult(matrixA,matrixB,ma,mb):
    matrixc = [0.0 for i in range(ma*ma)]
    for i in range(ma):
        for j in range(mb):
            temp = 0.0
            for k in range(ma):
                temp += matrixA[i*ma + k] * matrixB[k*mb + j]
            matrixc[i*ma + j] = temp
    print("Matrix C:")
    for i in range(10):
        print(matrixc[i], end=" ")
    #for i in range(ma):
    #    for j in range(mb):
    #        print(matrixc[i*ma + j], end=" ")
    #    print()










print("Hello, I am matrix_mult.py")
print("Menu:")
print("1. Multiply two matrices Normal")
print("2. Multiply two matrices line by line")
print("3. Multiply two matrices by block")
mode = int(input("Enter the mode: "))
print("Matrix size lins=cols:")
n = int(input())
mb= n
ma = n
matrixa =[]
for i in range(ma):
    for j in range(ma):
        matrixa.append(1.0)

matrixb =[]

for i in range(mb):
    for j in range(mb):
        matrixb.append( i+1)
start_time = time.time()
match mode:
    case 1:
        NormalMult(matrixa, matrixb,ma,mb)
    case 2:
        print("Not yet implemented")
    case 3:
        print("Not yet implemented")
    case _:
        print("Invalid mode")
end_time = time.time()

print("Execution time: ", end_time-start_time)
