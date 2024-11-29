# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
print('-'*60)
print(f"{"Reduzindo ainda mais seu programa":^60}")
print('-'*60)
import ex110_moeda as moeda

valor = float(input('Digite um valor: '))
moeda.resumo(valor, 80, 35)
moeda.resumo()
