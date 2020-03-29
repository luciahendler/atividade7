peso = float(input("Digite seu peso, em quilogramas: "))
altura = float(input("Digite sua altura, em metros e com separador '.': "))

imc = peso/(altura**2)

print("Seu IMC é: ", round(imc,2))