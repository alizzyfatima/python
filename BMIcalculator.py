height=float(input("Enter your Height in m:"))
weight=float(input("Enter your weight in kg:"))
BMI=weight/(height)**2
print("Your BMI is", BMI)

if BMI <= 18.4:
     print("you are underwight.Eat more roti")
elif BMI <= 24.9:
     print("you are healthy.Very nice")
elif BMI <= 29.9:
     print("you are overweight.Go workout ")
elif BMI <= 34.9:
     print("you are severely over weight.Workout and eat healthy")
elif BMI <= 39.9:
     print("you are OBESE.")
else:
     print("you are severely OBESE.")

