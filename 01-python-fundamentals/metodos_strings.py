movieName = "Top Gun"
movieDescription = """
    Top Gun é um filme de ação e drama lançado em 1986, dirigido por Tony Scott e estrelado por Tom Cruise. A história segue a vida de Pete "Maverick" Mitchell, um talentoso piloto da Marinha dos Estados Unidos, enquanto ele compete para se tornar o melhor piloto de caça da escola de elite Top Gun. O filme é conhecido por suas emocionantes cenas de voo, trilha sonora icônica e pelo desenvolvimento do personagem principal, explorando temas de coragem, amizade e superação.
"""
print(movieName.upper()) # tudo em maiúsculo
print(movieName.lower()) # tudo em minúsculo
print(movieName.capitalize()) #Primeira letra maíscula
print(movieName.title()) # Primeira letra maiúscula
print(movieName.center(50, "-")) # Retorna string com caracteres de preenchimento centralizados
print(movieName.find("u")) # Retorna o índice da primeira ocorrência do caractere "u" na string, ou -1 se não encontrado
print(movieName.replace("Top", "Matrix")) # Substitui a palavra "Top"   
