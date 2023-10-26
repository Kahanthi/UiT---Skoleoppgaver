#Prompt the user to enter weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

#Compute BMI
BMI = weight / (height*height) 

#Display result 
print(f"your bmi is {BMI:.3f}")