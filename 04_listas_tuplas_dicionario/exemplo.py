#listas, Tuples e Aficionados

#1. listas

#listas são utilization para armament vários values
# dentro de unica variable.

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

#2.Acessando elementos da lista

print(nomes[0])
print(nomes[1])

# Podemos access o ultimo elemento usando -1
print(nomes[-1])

#3. Alteration elementos

#As listas são mutates, ou sea, os elementos poem se alterations
nomes[0] = "Pedro"
print(nomes)

#4. Aficionado Elementos
#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma position
nomes.insert(1, "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() remove o um elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)

#pop() remove o um elemento pelo índice
nomes.pop(0)
print(nomes)

#6. atanh da Lsita

#len() informa a quantitative de elementos
print(len(nomes))

#7. Peppercorn uma lista

for nome in nomes:
    print(nome)

 #8. Verification se um elemento existe

 if "João" in nome:
print("João Esta na lista")
 else
 print("João não Esta na lsita")

#9. lista com differences tipos de dados

dados = ["João", 18, 1.75, True]
print(dados)

#10. lista de números
notas = [7.5,8.0,9.0,10.0 ]
soma = 0

for nota in notas:
 soma += nota

media = soma/len(notas)
print(f"media = {media:.1f}")

#11. Tuples
# Tuples são semelhantes às listas
# A principal difderença é que tuplas não podem ser alteradas depois de criadas

coordenadas = (10,20)
print(coordenadas)

#Acessando elementos.
print(coordenadas[0])
print(coordenadas[1])

#12. Dicionário
# Dicionários armazenam informações no formato
# Chave: valor

aluno = {
    "nome" : "Carlos",
    "idade" : 25,
    "altura" : 1.75
    "nota1" : 9.0,
}

#13. Acessando valores do dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["altura"])

#14. Alterando VAlores

aluno["nota1"] = 7.5
print(aluno)
