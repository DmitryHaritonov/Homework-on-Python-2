N = int(input('Введите число N: '))
k  = 1
c = 2 ** k
while (c) <= N:
   
    if (c) > N:
        break
    else:
        if(c % 2 == 0):
         k +=1

print(c)

