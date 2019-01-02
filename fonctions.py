import donnees.py
import os.path
from random import randrange

def input_name() :
    """ Demande le nom et test la présence du fichier de score puis actualise et affiche le score de départ."""
    
    player_name = str(input("Quel est votre nom ?"))
    
    
    if os.path.isfile(score):
        score_dict{}
        with open(scores, 'w') as score_dict:

    else:
        with open(scores, "r") as score_dict:

        if (name in score_dict)
            player_score = score_dict.value[player_name]
        else:
            with open(scores, 'w') as score_dict:
                score_name.write(0)
                score = 0

    return (name, score)

      
    
def choose_word() :
    """ Le programme choisi un mot dans une liste au hasard et renvoi un mot sous forme de liste ainsi que le mot du pendu. """

    word = words_list[random.randrange(len(words_list))]
    word = word.split()
    word_pendu = list("X" * len(word))
    return (word, word_pendu)

def input_char() :
    """ L'app demande une lettre puis la compare avec les lettres du mot et renvoi le mot du pendu. """ 
    
    letter_guessed = input("Entrez une lettre pour devenier le mot")
    
    for i,letter_guessed in enumerate(word):
        if letter_guessed[i] ==  word_pendu[i]
            word_pendu[i] = letter_guessed[i]
    
    return word_pendu
        
def print_word(word_pendu) :
    """ Ecrit à l'écran les lettres du mot du pendu séparées par un espace. """
    
    for index_letter in word:
        print(word_pendu[index_letter] + " ")
    