# Aleem Uddin Ather
# 10/26/2024
# This program prints "Hello World" to the screen 100 times

for _ in range(100):
    print("Hello World")

# Aleem Uddin Ather
# 10/26/2024
# This program prints each number from a list on a new line

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers:
    print(number)

# Aleem Uddin Ather
# 10/26/2024
# This program prints each number and its square on a new line

for number in numbers:
    print(f"Number: {number}, Square: {number ** 2}")

# Aleem Uddin Ather
# 10/26/2024
# This program draws a regular polygon based on user input for the number of sides, length, line color, and fill color

import turtle

# Get user input
num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Set up the turtle
t = turtle.Turtle()
t.color(line_color)
t.fillcolor(fill_color)

# Draw the polygon
t.begin_fill()
for _ in range(num_sides):
    t.forward(side_length)
    t.left(360 / num_sides)
t.end_fill()

# Close the turtle graphics window
turtle.done()
 
 # Aleem Uddin Ather
# 10/26/2024
# This program iterates through integers from 1 to 50 and checks for divisibility by 3, 5, or both

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)
# Aleem Uddin Ather
# 10/26/2024
# This program draws a simple flower-like pattern using turtle graphics

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)  # Set the drawing speed

# Draw a flower pattern
for _ in range(36):
    t.circle(50)
    t.left(10)

# Hide the turtle and close the window
t.hideturtle()
turtle.done()

