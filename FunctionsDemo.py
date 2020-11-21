def say_hi(): #code inside function must be indented
    print("Hello User")

def say_hi_with_parameters(name, age):
    print("Hello "+str(name)+", you are "+str(age))

def cube(num):
    return pow(num, 3)

is_male = True
is_tall = True
def checkMale():
    if is_male and is_tall:  #equivalent of ! in Java in Python is 'not' as in not(is_male) and is_tall
        print("Both male and tall")
    elif is_male or is_tall: 
        print("This is a male or tall")
    else:
        print("This is not a male, and you are short")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
def greaterthanone(num):   
    if num>1:
        return True
    else: return False

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

say_hi()
say_hi_with_parameters("Adithya", 17)
print(cube(4))
checkMale()
print(max_num(2,3, 4))
print(greaterthanone(2))
print(factorial(3))

