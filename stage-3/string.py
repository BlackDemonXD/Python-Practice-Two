#num=3                    #Number of class Integer
num=3.4                   #Number of class float
print(type(num))
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2   #Reminder of a division


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num=1
num=num+1 #or num+=1
print(num)
 
print(abs(-3))
print(round(3.75))
print(round(3.75, 1)) #Round to the first digit after the deicmal

num_1=3
num_2=4
print(num_1==num_2)  #Check if Num 1 and num 2 are equal
print(num_1!=num_2)  #Check if Num 1 and num 2 are NOT equal
print(num_1>num_2)   #Check if Num 1 is greater than Num 2
print(num_1<num_2)   #Check if Num 1 is less than Num 2
print(num_1<=num_2)  #Check if Num 1 is less than equal to Num 2
print(num_1>=num_2)  #Check if num 2 is greater than equal to Num 2

num_3='100'
num_4='200'
print(num_3+num_4)   #Binds the values instead of adding them

num_3=int(num_3)
num_4=int(num_4)
print(num_3+num_4)   #Telling it to take num_3 and num_4 as integers instead and then adding them gives the desired result