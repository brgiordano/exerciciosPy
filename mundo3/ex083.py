# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print('-'*60)
print(f"{"Validação de parênteses":^60}")
print('-'*60)

parenteses = []
expressao_correta = False
# por motivos de otimização, resolvi criar essa variável no lugar de fazer:
# if not any(char in expressao for char in "()"):
expressao_contem_parenteses = False

expressao = str(input("Digite uma expressão que utilize parênteses: "))
for c in expressao:
    if c == '(':
        expressao_contem_parenteses = True
        parenteses.append(c)
    elif c == ')':
        expressao_contem_parenteses = True
        if parenteses:
            parenteses.pop()
        else: break

else: # se der break nunca entra aqui, logo a expressão estará incorreta
    if not parenteses:
        expressao_correta = True

if not expressao_contem_parenteses:
    print("A expressão não contém parênteses.")
else:
    print(f"A expressão está {"CORRETA" if expressao_correta else "INCORRETA"} quanto aos parêntesis.")