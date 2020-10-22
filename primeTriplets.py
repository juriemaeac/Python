primes = []

def prime_num(lim):
    if lim < 1: return
    for i in range(2, int(lim**0.5) + 1):
        if lim % i == 0:
            return False
    return True   

def triangle(lim):
    count = 0
    column = 1
    for i in range(1, lim+1):
        for j in range(1, i+1):
            if count == lim:    
                break
            else:
                count += 1 
            if count in primes:
                print('\033[1;31;49m' + str(count) + '\033[1;30;49m', end=' ')    
            else:
                print('\033[1;30;49m' + str(count) + '\033[1;30;49m', end=' ')    
                
        column += 1        
        print ()    
        
        if count == lim:
            break
        else :
            pass
        
    for num in primes:      
        print (num)

lim = int(input("Enter value:  "))

if lim > 1000000:
    print("Invalid value. Please try again.")
    exit()
elif lim <= 0:
    print("Invalid value. Please try again.")
else:
    pass
    
for i in range(2,lim+1):
    if prime_num(i):
        primes.append(i)
  
triangle(lim)