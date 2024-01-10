# data science: medical insurance project (multiple parts)
# part 1: python syntax


age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# age change
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
print(f"This person's insurance cost is {insurance_cost} dollars.")

age += 4

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in cost of insurance after increading the age by 4 years is {change_in_insurance_cost} dollars.")

# bmi change
age = 28
bmi += 3.1

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {new_insurance_cost} dollars.")

# sex change
bmi = 26.2
sex = 1

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated cost for being male instead of female is {new_insurance_cost} dollars.")

# number of children change
sex = 0
num_of_children = 4

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated insurance cost after adding 1 child is {new_insurance_cost} dollars.")

# smoker change
num_of_children = 3
smoker = 1

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated insurance cost for a smoker is {new_insurance_cost} dollars.")
