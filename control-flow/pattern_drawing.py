size = int(input("Enter the size of the pattern:"))
i = 1
while i <= size:
    j = 1
    for j in range(1,size + 1):
       
      print("*", end="")
      j = j +1
    print()
    i = i + 1