height=float(input("enter the height in m "))
weight=float(input("enter the weight in kg"))
bmi=weight/height**2
if bmi < 18.5:
  print("underweight")
elif 18.5<=bmi<25:
  print("normal weight")
elif 25<=bmi<30:
  print("over weight")
elif bmi>=30:
  print("obese")