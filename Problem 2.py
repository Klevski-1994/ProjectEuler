#Problem 2
#Calculates the sum of all even Fibonacci numbers below a specific value (in this case 4,000,000)

fibonacci = [1,2]
sum_total = 0
def fibonacci_even_sum():
    global sum_total
    global fibonacci
    if fibonacci[1]<4000000:
        if fibonacci[1]/2 == fibonacci[1]//2:
            sum_total += fibonacci[1]
        fib_temp = fibonacci[0]
        fibonacci[0] = fibonacci[1]
        fibonacci[1] += fib_temp 
        fibonacci_even_sum()
    else:
        print(sum_total)
        
fibonacci_even_sum()
