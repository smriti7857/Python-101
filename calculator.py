
# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
def addorsub(a,b,oper):
    if(oper=="add"):
        return (a+b)
    elif(oper=="subtract"):
        return (a-b) 
    else:
       return "Invalid operation"   
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
oper=input("Enter the operation to perform with the two mnumbers: ")
result=addorsub(a,b,oper)
print(result)

