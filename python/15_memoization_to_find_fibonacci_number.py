def nth_fibonacci_number(n, fibo_dict={}) :
    if n in fibo_dict.keys() :
        return fibo_dict[n]
    elif n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        fibo_dict[n] = nth_fibonacci_number(n-1, fibo_dict) + nth_fibonacci_number(n-2, fibo_dict)
        return fibo_dict[n]
    


n = int(input("Enter n : "))
print("n'th Fibonacci Number is :", nth_fibonacci_number(n,))