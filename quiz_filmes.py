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
print(f"\nVocê acertou {pontos} de 3 perguntas.")
    