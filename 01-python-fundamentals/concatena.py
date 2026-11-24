name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("=====================")

#Alternativas de concatenação 1 :
#print("Nome do filme:",name)
#print("Ano de lançamento:",yearLaunch)
#print("Nota do filme:",noteMovie)

#Alternativa numero 2

print("nome do filme:", name, "\nAno de Lançamento:", yearLaunch,"\nNota do filme:", noteMovie)

#Alternativa numero 3
print(f"Nome do jogo: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}\n"
      )