h = int(input("Введите Ваш рост в см: "))
m = float(input("Введите Ваш вес в кг: "))
BMI = m/((h/100)**2)
print (round(BMI,2))
if BMI <= 16:
    print ("Выраженный дефицит массы тела")
elif 16 < BMI < 18.5:
    print ("Недостаточная (дефицит) масса тела")
elif 18.5 <= BMI <= 24.49:
    print ("Норма")
elif 25 <= BMI < 30:
    print ("Избыточная масса тела (предожирение)")
elif 30 <= BMI < 35:
    print ("Ожирение первой степени")
elif 35 <= BMI < 40:
    print ("Ожирение второй степени")
elif 40 <= BMI:
    print ("Ожирение третьей степени (морбидное)")