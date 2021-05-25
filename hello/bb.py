def count_primes(num):
    flag=0
    c=0
    for j in range(0,num+1):
        for i in range(2,int(j**0.5)+1):
            if (j%i==0) :
                flag=1
                break
        else:
            continue
        if flag==0:
            c=c+1
        else:
            continue
    return c 

print(count_primes(100))