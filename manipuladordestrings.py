'''                                      STRINGS

    -->FATIAMENTO:
        frase[9] : Mostra o caractere 9 da frase.
        frase[9:13]: Mostra do caractere 9 até o caractere 13-1
        frase[9:20:2]: Corta do caracttere 9 até o caracttere 19 pulando de 2 em 2 caracteres.
        frase[9:]: Separa do 9 até o fim da string
        frase[:13]: Separa do começo até o caractere 13-1
        frase[:]: Separa toda a string
        frase[9::3]: Separa do caractere 9 até o fim, pulando de 3 em 3



    -->ANÁLISE:
        len(frase): Mostra o número de caracteres da string.
        frase.count(' '): Conta o número de espaços e retorna esse valor.
        frase.count('o',0, 13): Conta o número de caracteres 'o' de 0 a 13-1
        frase.find('li'): Método que retorna a posição em que o argumento começa numa string. Caso não exista, o método retorna o valor -1.
        'Texto' in frase: Retorna um valor booleano que mostra se o argumento está dentro da string.



    -->TRANSFORMAÇÃO:
        frase.replace('Texto', 'Navio'): Substitui numa string, o primeiro argumento do método pelo segundo.
        frase.upper(): Toda a string se transforma em caracteres maiúsculos.
        frase.lower(): Toda a string se transforma em caracteres minúsculos.
        frase.title(): Todas as primeiras letras de cada palavra ficarão em maiúsculo.
        frase.capitalize(): A primeiro primeiro caractere ficará maiúsculo e o resto ficará em minúsculo.
        frase.strip(): Tira todos os espaços do lado direito e do lado esquerdo que não são parte da string.
        frase.rstrip(): Tira todos os espaços à direita.
        frase.lstrip(): Tira todos os espaços à esquerda.



    -->DIVISÃO:
        frase.split(): Separa cada palavra em uma lista com as palavras separadas.



    -->JUNÇÃO:
        '-'.join(frase): Põe dos lados do caractere o argumento(O primeiro caractere só recebe o argumento no lado direito e o final, só do lado esquerdo).
        
'''
