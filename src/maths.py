def findOddEven(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"


def findfibbonaci(n):
    numx = 0
    numy = 1
    
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        for i in range(2,n+1):
            
            numz = numy +numx
            numx =numy
            numy = numz
        return numz

if __name__ == "__main__":
    x = findOddEven(5)
    print("x is: ", x)
    y = findfibbonaci(3)
    print("y is: ", y)

