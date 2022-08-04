#define a function to get the sum fib nums 4 million and under

#track a global list of fib nums
nums = []
#recursive function, taking default a and b terms to be 1, 0
def fib_nums(a=1, b=0):
    
    num = a+b
    #once we have exceeded a value of 4 million, we can be done
    if num >= 4000000:
        return
    #if the number is even, add it to our list
    if num % 2 == 0:
        nums.append(num)
    
    #set the value of b equal to a
    b = a
    #set the value of a equal to our current number
    a = num
    #recursively call
    fib_nums(a, b)

#initial call
fib_nums()

#output to console
print("Sum of even fibonacci numbers under 4 million is: ")
print(sum(nums))
