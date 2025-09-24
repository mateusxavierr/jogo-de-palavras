
# 🎮 Jogo de Palavras — Python (CLI)

Um jogo de adivinhação simples no terminal, onde o jogador precisa descobrir uma palavra de **5 letras** chutando uma letra por vez.

## 🚀 Como funciona
- O jogo escolhe aleatoriamente uma palavra de 5 letras de uma lista predefinida.  
- O jogador digita **uma letra por vez**.  
- Letras corretas aparecem na posição certa, as demais permanecem ocultas com `*`.  
- O jogo termina quando a palavra é adivinhada.  

## 📌 Exemplo de jogo
```
COMO FUNCIONA O JOGO: você tentará acertar uma palavra de 5 letras.
Se você acertar a letra, ela aparecerá na resposta, se você errar, nada vai aparecer.

Tentativa 1: digite uma letra: a
*a*a*

Tentativa 2: digite uma letra: s
*asa*

Tentativa 3: digite uma letra: c
casa*

Você ganhou o jogo com 7 tentativas! Parabéns!
```

## 📂 Estrutura
```
word_game.py   # Script principal do jogo
```

## ▶️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/jogo-de-palavras.git
   ```
2. Entre na pasta:
   ```bash
   cd jogo-de-palavras
   ```
3. Execute o script:
   ```bash
   python3 word_game.py
   ```

## 🛠️ Tecnologias
- Python 3  
- Biblioteca padrão `random`  

## 📄 Licença
Projeto livre para estudos e uso pessoal.
