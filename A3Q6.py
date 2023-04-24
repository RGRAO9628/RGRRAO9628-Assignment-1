# Get three sides of a triangle from the user
a = int(input("Enter length of side a: "))
b = int(input("Enter length of side b: "))
c = int(input("Enter length of side c: "))

# Check if the given input lengths can form a triangle
if a > b + c or b > a + c or c > a + b:
    print("No")
else:
    print("Yes")
