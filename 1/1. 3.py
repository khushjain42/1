"""Write a program that asks the user for a number of seconds and prints out
how many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.
[Hint: Use the //operator to get minutes and the % operator to get seconds.]"""
x=int(input("please enter time in seconds"))
y=x//60
z=x%60
print("minutes",int(y))
print("seconds",int(z))
