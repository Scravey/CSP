'''
python Lists and Loops
======================

Directions
----------

** Problem 1 **

Given a positive integer N, define the '3N+1' sequence starting from N as follows:
If N is an even number, then divide N by two; but if N is odd, then multiple N by 3 and add 1.
Continue to generate numbers in this way until N becomes equal to 1.

For example, starting with N=3, which is odd, we multiply by 3 and add 1, giving N = 3*3+1 = 10.  Then, since N is even, we divide by 2, giving N= 10/2 = 5.  We continue in this way, stopping when we reach 1, giving the complete sequence:
    3, 10, 5, 16, 8, 4, 2, 1

Write your code below:
'''
n = int(input("Type your desired number:"))
print("Your number is " + str(n) + ".")

while n != 1:
    if n % 2 == 0:
        n /= 2
        print("The number is now " + str(n))
    else:
        n *= 3
        n += 1
        print("The number is now " + str(n))

print("The number 1 has been reached, stopping.")

'''
** Problem 2 **

Gross = 144 eggs
Dozen = 12 eggs
Remainder =  Number of eggs left over (< 12)

Write a code snippet that asks the user how many eggs she has and then tells the user how many gross of eggs, dozen eggs, and the remainder of eggs.

For example, if the user says that she has 1342 eggs, then your program would respond with:

Your number of eggs is 9 gross, 3 dozen, and 10.


Write your code below:
'''

e = int(input("Type your egg amount here:"))
print("You have " + str(e) + " eggs.")

g = e / 144
d = e % 144 / 12
c = e % 144 % 12 /1

print("Gross = " + str(int(g)) + "  Dozen = " + str(int(d)) + "  Leftover = "+ str(int(c)))
