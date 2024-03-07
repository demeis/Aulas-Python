num1 = 5
num2 = 7
print(num1+num2)
print(type(num1))
print(type(num2))

#Limitando números decimais:
pi = 3.1415
print(f"O número com duas casas decimais é {pi:.2f}.")

#Variável tipo lógico
d = True
e = False
print(type(d))
print(type(e))

#Comparação
nota = 8
media = 7
aprovado = nota >= media
print(aprovado)

#Entrada de dados
mediaFinal = float(input('Média final da disciplina de 0 a 10 = '))
frequencia = int(input('Frequência da disciplina em porcentagem = '))

if mediaFinal >= 6 and frequencia >= 75:
    print('Aprovado!')
else:
    print('Reprovado!')

#Exercícios:

#1
nome = 'Gustavo'
print(nome)

#2
a = 3
b = 5
print(2*a*3*b)

#3
c = 7
print(a+b+c)

