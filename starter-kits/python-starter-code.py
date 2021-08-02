# Happy Birthday MLH

# Starter Codes for Python Language

# Hello World

print("Hello, World!")

# Factorial of a Number

def factorial(n) :
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1) # recursive call
def fact(n):
    for i in range (1 , n+1):
        print ("%2d! = %d" %(i, factorial(i)))
        try:
            var = int (input (" enter a number-"))
            fact (var)
        except Exception as e:
            print("error!!",e)
        else:
            print("you sucessfully entered integer")
if __name__== "__main__":
    fact(n)
    while True:
        again=input("do you want to process again:y/n-\n")
        if again=='y':
            even_odd()
        else:
            print("thank you for been here.....your are exiting from here.........bye bye!!!!")
            exit()

# Check for even or odd

def even_odd():
    try:
        num = int (input ("enter a number-"))
    except Exception as e:
        print("error!!!!!!!!!!.........try again",e)
        even_odd()
    else:
        print("your result is that")
        if num > 1:
            if (num % 2) == 0:
                print ("the number you entered is even number")
            else:
                print ("the number you entered is odd number")

if __name__== "__main__":
    even_odd()
    while True:
        again=input("do you want to process again:y/n-\n")
        if again=='y':
            even_odd()
        else:
            print("thank you for been here.....your are exiting from here.........bye bye!!!!")
            exit()

# Check for Armstrong Number

def armstrong():
    return armstrong()

def main():
     num = int(input("Enter a number:-"))
     if num =='x':
        Break

     else:
      number = int (num)
      total = 0
      temp = number
      while temp > 0:
        digit = temp % 10
        total += digit **3
        temp //=10
     if number == total:

        print ("this is a armstrong no.=",num)

     else:
         print("this is not an armstrong no. =",num)


if __name__ =='__main__':
    main()
    while True:
        again = input("do you want to continue:y/n=\n").lower()
        if again == 'y':
            main()
        else:
            print("bye bye you are exiting from the program")
            exit()

# Check for a leap year or not

def leap():
    return leap()
def main():
    try:
        year = int(input("enter a year-").strip())
    except Exception as e:
        print("error!!!",e)
    else:
        print("nice..you entered a valid input")
        if (year % 4)== 0:
            if (year % 100) ==0:
                if (year % 400)==0:
                     print("{0} is leap year" .format (year))

                else:
                     print ("{0} is not leap year". format(year))

            else:
                 print ("{0} is leap year".format(year))

        else:
             print ("{0} is not leap year" .format(year))
if __name__ == '__main__':
    main()
    while True:
       again= input("do you want to process again:y/n:").lower()
       if again=='y':
           main()
       else:
           print("bye bye..........!!!\nyou exit from the program")
           exit()

# How to use Turtle

import turtle as t
p = t.pen()
p.color('yellow','red')

p.begin_fill()

while True:
    p.forward(400)
    p.left(170)
    if abs(p.pos()) < 1 :
        p.end_fill()
        break

# How to create functions

def hello(*args):
    print()
    print()

    # print(args[:])
    # print("With for loop ")

    for var in args:
        print("Here is your args = ", var)


print("hello()")
hello()

print("\n\n hello(1,2,3,4,5,6)")
hello(1, 2, 3, 4, 5, 6)

print("\n\nhello('python','helllo',1,2,3,4,5)")
hello("python", "helllo", 1, 2, 3, 4, 5)

print("\n\n hello([1,2,3],'hello','a','b')")
hello([1, 2, 3], "hello", 'a', 'b')

# Decorators


def info(**kwargs):
    for name in kwargs:
        print("hello!!!", name)


def info(**kwargs):
    for name in kwargs:
        print("hello!!! key= ", " value = ", kwargs[name])


info(name='prathima', age=25, addr='hyd')


def decorator(old_value):
    def inner(**kwargs):
        for var in kwargs:
            print(name, "=", kwargs[var])

    return inner


def decorate(old_fun):
    def inner(**kwargs):
        print(var, "=", kwargs[var])

    return inner


new_info = decorate(info)
new_info(name='prathima', age=25, addr='hyd')


## Hope this .py Source File helped you in getting the key concepts of basic Python programming