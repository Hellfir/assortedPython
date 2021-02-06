def collatz(n):
    #goes through a collatz sequence for a number
    sequence = []
    while n > 1:
        sequence.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = (n*3)+1
    return(sequence)

def pfactor(n):
    #returns prime factors of a number
    divisors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            divisors.append(divisor)
            n = n/divisor
            divisor = 2
        else:
            divisor = divisor + 1
    return(divisors)
