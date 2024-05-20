salario = float(input("salario imposto anual"))
taxa=0
if salario<5000:
    taxa = 0
if salario<=85528 and salario > 14260:
    taxa= ((salario/100)*18)-556.2
elif salario >= 85528:
    taxa= (14839.2+(((salario-85528)/100)*32))
taxa=round(taxa,0)
print("o imposto é:",taxa , "reais" )