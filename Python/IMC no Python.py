def imc():
    peso=float(input("Digite o seu peso(em kg): "))
    altura=float(input("Digite a sua altura(em metros): "))
    imc=peso/altura**2
    print("Seu imc é de ", imc)

def repeticao():
    sexo=str(input("Qual o seu sexo?M/F  "))  

sexo=str(input("Qual o seu sexo?M/F  "))   

if sexo=='M' or sexo=='m':
    print(imc())
    if imc < 18.5:
        print("Segundo o seu resultado, você está abaixo do peso. Cuide-se melhor!S2")
    elif imc >= 18.5 and imc <= 24.9:
        print("Segundo o seu resultado, você está no seu peso normal. Parabéns!")
    elif imc >= 25 and imc <= 29.9:
        print("Segundo o seu resultado, você está com sobrepeso. Cuidado!")
    elif imc >= 30 and imc <= 34.9:
        print("Segundo o seu reultado, você está obesidade classe I. Cuide-se melhor!S2")
    elif imc >= 35 and imc <= 39.9:
        print("Segundo o seu resultado, você está com obesidade classe II. Cuidado com sua saúde!S2")
    elif imc >= 40:
        print("Segundo o seu resultado, você precisa de um médico.")
                  
elif sexo=='F' or sexo=='f':
    print(imc())
    if imc < 18.5:
        print("Segundo o seu resultado, você está abaixo do peso. Cuide-se melhor!S2")
    elif imc >= 18.5 and imc <= 24.9:
        print("Segundo o seu resultado, você está no seu peso normal. Parabéns!")
    elif imc >= 25 and imc <= 29.9:
        print("Segundo o seu resultado, você está com sobrepeso. Cuidado!")
    elif imc >= 30 and imc <= 34.9:
        print("Segundo o seu reultado, você está obesidade classe I. Cuide-se melhor!S2")
    elif imc >= 35 and imc <= 39.9:
        print("Segundo o seu resultado, você está com obesidade classe II. Cuidado com sua saúde!S2")
    elif imc >= 40:
        print("Segundo o seu resultado, você precisa de um médico.")
else:
    print("Resposta inválida!")
    repeticao()
    if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':
                print(imc())
    elif sexo != 'M' or sexo != 'm' or sexo != 'F' or sexo != 'f':
                print("Resposta inválida!")    
                repeticao() 
        
