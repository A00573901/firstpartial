def suma(a,b):
  x = a+b
  return x

def resta(a,b):
  x = a-b
  return x

print("dame el primer numero")
a = int(input())
print ("dame el segundo numero")
b = int(input())
print("la suma da",suma(a,b),"y la resta da",resta(a,b))

def multiplication(a,b):
  x = a*b
  return x

def division(a,b):
  x = a/b
  return x

print("give me the first number")
a = int(input())
print("give me the second number")
b = int(input())
print("muliplication is",multiplication(a,b),"and division is",division(a,b))

def converse(km,m):
  m = (int(km)*1000)
  return m
  
print("How many kilometers have you passed through?")
km = int(input())
m = (int(km)*1000)
print("you have runned",converse(km,m),"meters" )

def triangle_area(a,b):
  x = ((int(a))*(int(b)))/2
  return x

print("Give me the base of the triangle")
a = int(input())
print("now the high")
b = int(input())
print("the area of the triangle is",triangle_area(a,b))
