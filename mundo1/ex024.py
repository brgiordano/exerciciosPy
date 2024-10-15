# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input("Digite o nome da cidade: ").strip())
print("A cidade \"{}\" {} começa com a palavra \"{}\"{}".format
      (cidade.title(),
       '' if cidade.upper().startswith("SANTO") else "não",
       "SANTO",
       '.' if cidade.upper().startswith("SANTO") else f", mas sim com a palavra \"{cidade.split()[0]}\"."))