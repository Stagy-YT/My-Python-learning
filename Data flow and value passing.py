def get_two_number():
    num1 = int(input("Enter your fist number!: "))
    num2 = int(input("Enter your second number!: "))
    return num1, num2 

def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum 

def multiply_sum(addition):
    final_numb = addition * int(input("Enter the final value you would like to multiply by!: "))
    return final_numb

def last_action(multiply):
    print(f"The number you ended up with after all this math was {multiply}")



a, b = get_two_number()
add = add_two_numbers(a, b)
multiply = multiply_sum(add)
show_final = last_action(multiply)

#4/19/26, This teaches how me how to pass data from function to function using paramaters!
