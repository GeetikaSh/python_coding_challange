```
This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below  that are multiples of 3 or 5, we get 3,5,6,9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below .
```
def multiple_3or_5(n):
    def sum_of_multiples(k):
        m = (n - 1) // k
        return k * m * (m + 1) // 2

    total_sum = sum_of_multiples(3) + sum_of_multiples(5) - sum_of_multiples(15)
    print(total_sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multiple_3or_5(n)
