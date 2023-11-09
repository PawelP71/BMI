print('Kalkulator BMI')
weight = float(input('Podaj masę ciała w kilogramach '))
height = float(input('Podaj wzrost w metrach '))
BMI = (weight / height**2)
print('wynik:', BMI)
if BMI < 18.5:
    print('niedowaga')
elif 18.5 <= BMI < 24.9:
    print('w normie')
elif 25 <= BMI < 29.9:
    print('nadwaga')
elif BMI > 30:
    print('otyłość')
