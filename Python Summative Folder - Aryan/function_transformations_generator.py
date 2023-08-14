# Why write function transformations by hand when you could write code to do
# it for you (that probably takes longer than just writing the function
# transformations

# Uses desmos notation
# You have to do the fraction ones manually, but since I have like 2 of those
# I'm not going to write additional code for them

num_functions = int(input('How many functions do you have? '))
functions = []
for i in range(num_functions):
    long_function = str(input("Give me your function: "))
    short_function = long_function.replace('left', '')
    short_function = short_function.replace('right','')
    short_function = short_function.replace('\\', '')
    last_opening_curly_thing = short_function.rfind('{')
    short_function = short_function[0:last_opening_curly_thing]
    short_function = short_function.replace('{', '')
    short_function = short_function.replace('}','')
    functions.append(short_function)
    
for i, equation in enumerate(functions, start=1):
    print(f"{i}. {equation}")



