# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para determinar la categoría según el IMC
def determinar_categoria(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

# Solicitar al usuario su peso en kilogramos y altura en metros
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
altura = float(input("Por favor, ingresa tu altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Determinar la categoría
categoria = determinar_categoria(imc)

# Mostrar el resultado
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría de IMC: {categoria}")
