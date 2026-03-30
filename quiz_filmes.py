print("🎬 Bem-vindo ao Quiz de Filmes!")
print("Responda as perguntas abaixo.\n")

pontos = 0

resposta = input("Em que ano foi lançado o filme Matrix? ")

if resposta == "1999":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é 1999.")
resposta = input("Que ator interpreta o personagem principal em Matrix? ")
if resposta.lower() == "keanu reeves":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Keanu Reeves.")
resposta = input("Qual é o bruxo mais famoso do cinema?\n")
if resposta.lower() == "harry potter":
    print("✅ Correto!")
    pontos = pontos + 1
else: 
    print("❌ Errado! A resposta certa é Harry Potter.")
resposta = input("Quem interpreta o personagem principal no filme Marty Supreme (2025)? ")
if resposta.lower() == "timothée chalamet" or resposta.lower() == "timothee chalamet":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Timothée Chalamet.")
resposta = input("Quem dirigiu o filme Marty Supreme (2025)? ")
if resposta.lower() == "josh safdie":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Josh Safdie.")
resposta = input("Qual filme ganhou o Oscar de Melhor Filme em 2020? ")
if resposta.lower() == "parasita" or resposta.lower() == "parasite":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Parasita.")
resposta = input("Qual ator interpreta o Homem de Ferro no Universo Cinematográfico Marvel? ")
if resposta.lower() == "robert downey jr" or resposta.lower() == "robert downey jr.":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Robert Downey Jr.")
resposta = input("Qual é o nome do vilão principal da saga Star Wars? ")
if resposta.lower() == "darth vader":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Darth Vader.")
resposta = input("Em qual cidade se passa o filme O Poderoso Chefão (1972)? ")
if resposta.lower() == "nova york" or resposta.lower() == "new york":
    print("✅ Correto!")
    pontos = pontos + 1
else:
    print("❌ Errado! A resposta certa é Nova York.")
print(f"\nVocê acertou {pontos} de 9 perguntas.")
    