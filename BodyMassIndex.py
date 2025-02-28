# Exercise 3 
# calculating BMI and health condition accordingly(also attached is seperate file)
# Body Mass Index (BMI) = weight(kg)/height2(m2)

Persons_weight = float(input('Enter your weight in (Kg): '))
Persons_height = float(input('Enter your height in (m): '))
BMI_of_person = Persons_weight/ (Persons_height ** 2)

print(f"Your BMI is: {BMI_of_person}")
if BMI_of_person <18.5: 
    print('You are in the “underweight” range.')
elif 18.5<= BMI_of_person <=24.9 :
    print('You are in the “Normal” range.')
elif 25<= BMI_of_person<=29.9:
    print('You are in the “overweight” range.')
else: 
    print('You are Obese')