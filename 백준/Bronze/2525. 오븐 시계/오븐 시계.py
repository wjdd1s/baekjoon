A, B = map(int, input().split())
C = int(input())

if B+C==60:
    if A+1==24:
        print(0, 0)
    else:
        print(A+1,0)
    

if B+C<60:
    print(A, B+C)

if B+C>60:
    if A+1 == 24:
        A -= 23
        B = (B+C)-60*((B+C)//60)
        print(A, B)
    else:
        A = A+(B+C)//60
        B = (B+C)-60*((B+C)//60)
        if A >= 24:
            A -=24
        else:
            pass
        
        print(A, B)