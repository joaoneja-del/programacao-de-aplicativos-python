# O que é uma função?
# Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ela permite organizar e reutilizar o código.

# 1. Criando uma função
# Utilizar a palavra def para criar uma função.
def saudacao():
    print("Olá, seja bem-vindo!")

# A chamada da função deve ficar fora do corpo da função
saudacao()


# 2. Função com parâmetro
def saudacao2(nome=None):
    print(f"Olá, {nome}")

saudacao2("Ana")


# 3. Mais de um Parâmetro
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria", 17)


# 4. Função com cálculo
def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

somar(5, 3)


# 5. Retornando um valor
# O return devolve um valor para o local onde a função foi chamada
def somar2(numero1, numero2):
    return numero1 + numero2

resultado = somar2(10, 20)
print(resultado)


# 6. Função com Condição
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificar_idade(20))


# 7. Parâmetro com valor padrão
# Podemos definir um valor padrão para um parâmetro
def saudacao3(nome: str = "Aluno"):
    print(f"Olá, {nome}")

saudacao3()
saudacao3("João")


# 8. Vários Parâmetros
def calcular_media(nota1=0, nota2=0, nota3=0):
    media = (nota1 + nota2 + nota3) / 3
    return media

media_final = calcular_media(8.0, 7.5, 9.0)
print(f"Média: {media_final:.2f}")

#9. Funcoes para organizar um programa
def cadastarProduto():
   nome =  input("Digite o nome do produto")
   preco = float(input("Digite o preço do produto"))
   return nome, preco

def exibirProduto(nome, preco):
   print("\n==== Produto ======")
   print(f"nome {nome}")
   print(f"Preço: R${preco}")

nome , preco = cadastarProduto()
exibirProduto(nome, preco)