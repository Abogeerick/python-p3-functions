#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, ${name}")

def greet_with_default(name="programmer"):
    print("Hello, programmer!")


def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None
    
greet_programmer()
greet("Naureen")
greet_with_default()
greet_with_default("Sunny")
sum_result = add(1, 2)
print(sum_result)
halve_result = halve(4)
print(halve_result)
halve_invalid_result = halve("two")
print(halve_invalid_result)

    

