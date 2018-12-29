# Equilateral Triangle
high=int(input("Enter the number of row (high):"))
k=2
for row in range(1,high+1):
    for col in range(1,2*high):
        if row+col==high+1 or col-row==high-1:
            print("*",end="")
        elif row==high and col!=k:
            print("*",end="")
            k=k+2
        else:
            print(end=" ")
    print()