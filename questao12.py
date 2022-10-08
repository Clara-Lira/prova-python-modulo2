glossario = {'python': 'É uma linguagem de programação.',
             'framework' : 'É uma abstração que une códigos comuns entre vários projetos de software provendo uma funcionalidade genérica.' ,
             'java' : 'É uma linguagem de programação orientada a objetos.',
             'idl' : 'É uma linguagem de programação usada para análise de dados.',
             'logica de programacao' : 'É a organização coesa de uma sequência de instruções voltadas à resolução de um problema.'}

nenhumaPalavraDigitada = 'Essa palavra não consta no nosso dicionário!'

bemVindo = 'Bem-Vindo ao nosso dicionário!'
print(bemVindo)

palavra = input('Digite uma palavra: ')

if palavra == 'python':
    print(glossario['python'])

elif palavra == 'framework':
    print(glossario['framework'])

elif palavra == 'java':
    print(glossario['java'])

elif palavra == 'idl':
    print(glossario['idl'])

elif palavra == 'logica de programacao':
    print(glossario['logica de programacao'])

else:
  print(nenhumaPalavraDigitada)