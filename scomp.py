thisset = {"29","23","1", "2", "3", "5", "7", "11","13","17","19"}  

if "23" in thisset:
  print("Yes, '11' is in this set")

def scomponi(n):
    i = 2  # Start from 2, as 1 is not a prime number
    lista = []
    while n > 1:
        if str(i) in thisset and n % i == 0:
            n = n // i
            lista.append(i)
        else:
            i += 1

    print(f"scomposizione è finita e la lista è ::{lista}")
    

#scomponi(76)
scomponi(630)
scomponi(23345)
