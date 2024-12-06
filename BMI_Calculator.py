# provide a weight recommendation for a healty BMI
print("  THE GREATEST WEALTH IS HEALTH  ")
print("     HEALTHY BMI IS 22.5  ")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height/100
BMI = weight / (height_in_meters**2)
print(BMI)

if (BMI < 16):
    print("Your are severely underweight", BMI )
elif(BMI >= 16 and BMI < 18.5):
    print("Your are Underweight", BMI )
elif(BMI >= 18.5 and BMI < 24):
    print("Your are Healty", BMI )
elif(BMI >= 24 and BMI < 30):
    print("Your are Overweight", BMI )
elif(BMI >=30):
    print("You are Obese", BMI )


