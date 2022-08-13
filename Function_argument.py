#Required arguments

def display_name(name):
    print("1.Required Arguments:")
    print("My name is:", name)
    print("********************************************")
display_name("BetaSpyder")

#Keyword Arguments

def print_details(name,age):
    print("2.Keyword Arguments:")
    print("My name is:",name)
    print("My age is:",age)
    print("********************************************")
print_details(name='Beta',age=40)
#print_details(age=40,name="Beta")

#Default Arguments

def employee(name,age=29):
    print("3.Default Arguments:")
    print("Employee name:",name)
    print("The Age is:",age)
    print("********************************************")
employee("BetaSpyder")

#Variable length Arguments
def rect_area(l,b):
    print("4. Variable-length Argument:")
    print("The area of rectangle is:", l*b)
    print("********************************************")
rect_area(2,6)

