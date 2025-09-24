print('COMO FUNCIONA O JOGO: você tentará acertar uma palavra de 5 letras.\nSe você acertar a letra, ela aparecerá na resposta, se você errar, nada vai aparecer.')

import random
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
tentativa = 1
chutes = []
asteriscos = '*****'
var = ''
palavras = ['casas', 'pedra', 'livro', 'piano', 'nuvem', 'campo', 'folha', 'noite', 'limpo', 'pasto', 'sinal', 'gente', 'feira', 'corpo', 'tempo', 'letra', 'porta', 'banco', 'vento', 'salas', 'linha', 'bicho', 'norte', 'massa', 'festa', 'prato', 'sorte', 'grito', 'verao', 'marca', 'risco', 'fruta', 'cinco', 'praia', 'plano', 'beira', 'salto', 'cobra', 'verde', 'roupa', 'baile', 'dente', 'rosto', 'sonho', 'aluno', 'moeda', 'reino', 'cores', 'risos', 'copos', 'chuva', 'vapor', 'trapo', 'troca', 'fundo', 'janes', 'agora', 'papel', 'mundo', 'ponta', 'molho', 'nobre', 'andar', 'velho', 'botao', 'pente', 'balde', 'vidro', 'borda', 'tarde', 'passe', 'galho', 'caixa', 'justo', 'tirar', 'lugar', 'telha', 'puxar', 'frase', 'perto', 'andar', 'pardo', 'lente', 'fraco', 'pular', 'pobre', 'luzia', 'servo', 'magro', 'pesos', 'basta', 'porem', 'carta', 'navio', 'suave', 'sopro', 'vazio', 'morro', 'tenis', 'barco']
palavra = random.choice(palavras)

while True:
    chute = input(f'\nTentativa {tentativa}: digite uma letra: ').lower()

    if chute in chutes:
        print('Você já chutou essa letra')

    elif chute in alfabeto and len(chute) == 1:
        tentativa += 1
        var = ''

        for i in range(len(palavra)):
            if asteriscos[i] == palavra[i]:
                var += palavra[i]
            elif chute == palavra[i]:
                var += chute
            else:
                var += '*'
            
        else:
            asteriscos = var
            chutes += chute
            print(asteriscos)
            
            if asteriscos == palavra:
                print(f'Você ganhou o jogo com {tentativa - 1} tentativas! Parabéns!')
                break
        
    else:
        print('Tentativa inválida')