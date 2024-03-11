#function
#it is a group of statementa is repetedly required then it is not recommended to write the same code again and again separately we have to define these satements as a single unit and we can call that unit any number of times based on our requirement this unit is nothing but function. 

#advantages of function
#1. we can avoid code duplicacy
#2. we can make the code more readable and understandable
#3. we can make the code more reusable
#4. we can make the code more manageable

#types of functions
#1. built-in functions
#2. user defined functions

#built-in functions
#these functions are already defined in python and we can use them directly
#1. print()
#2. input()
#3. eval()
#4. type()
#5. id()
#6. int()   etc

#user defined functions
#these functions are defined by the user based on his requirement and we can use them any number of times based on our requirement. 
#we can define the function by using def keyword and we can call the function by using function name.

#1. function without arguments and without return value
#2. function with arguments and without return value
#3. function without arguments and with return value
#4. function with arguments and with return value

#syntax of function
#def function_name(parameters):
    #function body
    #return value

# def wish():
#     print("hello World")
#     print("good morning")
#     print("how are you")
# wish() #calling the function

#parameterized function
#def wish(name):
#    print("hello",name,"good morning")
#wish(input("enter your name: "))

#write a function to take number as input and print the square value of that number
#def sq(num):
#    print("the square value of",num,"is:",num*num)
#sq(int(input("enter a number: ")))

#function can return a value by using return statement

x=int(input("enter 1st number: "))
y=int(input("enter 2nd number: "))
def add(a,b):
    return a+b
print("the sum of two numbers is:",add(x,y))

#positional arguments

#def wish(name,msg):
#    print("hello",name,msg)
#wish("sai","good morning")

#defualt arguments
#def wish(name="sai",msg="good morning"):
#    print("hello",name,msg)
#wish()
#wish("ravi")

#keyword arguments
#def wish(name,msg):
#    print("hello",name,msg)
#wish(msg="good morning",name="sai")

#variable length arguments
#*args
#def sum(*n):
#    total=0
#    for x in n:
#        total=total+x
#    print("the sum is:",total)
#sum(10,20)

#keyword variable length arguments
#**kwargs   
def display(**kwargs):
   for k,v in kwargs.items():
       print(k,"=",v)
display(name="sai",marks=100,age=23)



