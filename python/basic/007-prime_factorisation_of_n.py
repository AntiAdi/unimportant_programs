def prime_factorisaton(n, factors={}, check=2) :
    if n == 1 :
        return factors
    elif n%check==0 :
        if check in factors :
            factors[check] = factors[check] + 1
        else :
            factors[check] = 1
        return prime_factorisaton(n/check, factors, check)
    else :
        return prime_factorisaton(n, factors, check+1)

    
number = (int)(input("Enter a number : "))
print("Prime Factors :", prime_factorisaton(number))
