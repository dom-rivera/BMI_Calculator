#Hello Everyone!
#The project below is a coding challenge from Udemy 100 Days of Code-
#The Complete Python Pro Bootcamp 2023
##### BMI Project ####
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
float_height = float(height)
float_weight = float(weight)
bmi = float_weight / float_height ** 2
int_bmi = int(bmi)
print(int_bmi)