print ( '========= No. 1 =========' )
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
print ("My prediction: 5")

print ('========= No. 2 =========' )

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
print ("My prediction: Error")

print ('========= No. 3 =========' ) 
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
print ("My prediction: 10")


print ('========= No. 4 =========' )
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
print ("My prediction: 10")

print ('========= No. 5 =========' )
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
print ("My prediction: 5")

print ('========= No. 6 =========')
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
print ("My prediction: 8")

print ('========= No. 7 =========' )
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
print ("My prediction: 7")

print ('========= No. 8 =========' )
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
print ("My prediction: 7")

print ('========= No. 9 =========')
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print ("My prediction: 3, 3, 6")

print ('========= No. 10 =========')
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
print ("My prediction: 10")

print ('========= No. 11 =========' )
#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
print ("My prediction: 500, 500, 300, 300")

print ('========= No. 12 =========')
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
print ("My prediction: 500, 500, 300, 300")

print ('========= No. 13 =========' )
#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
print ("My prediction: 500, 500, 300")

print ('========= No. 14 =========' )
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
print ("My prediction: 1, 3, 2")

print ('========= No. 15 =========' )
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
print ("My prediction: 1 3")