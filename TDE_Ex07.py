horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

minutosHoras = minutos/60
segundosHoras = (segundos/60) / 60
horasTotais = minutosHoras + segundosHoras + horas
print("minutos: " + str(horasTotais * 60) + "\n" +
    "segundos: " + str((horasTotais * 60) * 60))