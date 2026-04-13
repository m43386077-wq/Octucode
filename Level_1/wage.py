# حساب المساحة
length = float(input("Please type lenght: "))
width = float(input("Please type width: "))
total_area = length * width

# حساب الأجرة
wage_per_square_meter = float(input("Please type wage per square meter: "))
total_wage = total_area * wage_per_square_meter

# طباعة النتائج
print(f"The total area is: {total_area}")
print(f"The total wage is: {total_wage}$")
