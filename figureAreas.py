#!/usr/bin/env python3
#-*-coding: utf-8 -*-
# calculates different areas
import os
import re
option = "X"

def hello():
    print('Hello!')

def square(L):
	return L*L
 
def area_rectangle(width, height):
    return width * height
 
def print_welcome(name):
    print('Welcome,', name)
 
def circle(radius):
    return 3.14159 * radius ** 2
 
def print_menu():
	os.system('clear')
	os.system('date')
	print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print("Welcome, ", name)
	print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print()
	print("To calculate the area of the desired figure, choice an option.")
	print("\na - Rectangle")
	print("b - Square")
	print("c - Circle")
	print("\nTo exit type q")
	
name = input('Your Name: ')
hello()
print_menu()
print()
print("Option chosen: ", option)
while option not in ("q", "Q"):
	option = input("Option: ")
	if option == "a":
		print("Option A --- Rectangle Area")
		width=float(input("Width: "))
		height=float(input("Height: "))
		print("The area of the rectangle is: ", area_rectangle(width,height))
		print()
		input("Press Enter to continue...")
		print_menu()
	elif option == "b":
		print("Option B --- Square Area")
		L = float(input("Length of square side: "))
		print("The area of the square is: ", square(L))
		print()
		input("Press Enter to continue...")
		print_menu()
	elif option == "c":
		print("Option C --- Circle Area")
		radius = float(input("Radius: "))
		print()
		print("The area of the circle is: ", circle(radius))
		print()
		input("Press Enter to continue...")
		print_menu()
	else:
		input("Option not recognized, press Enter to continue...")
		print_menu()
print("End")
