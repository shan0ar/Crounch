import argparse
import random

def generer_variante_mot(mot):
    # Remplacements spécifiques
    replace = {'a': '@', 'a': 'A', 'A': 'a', 'a' : '4', 'A' : '4', 'A' : '@', 'e': '€', 's' : '5', 'S' : '5', 'o': '0', 'i': '1', 'a': '4', 't': '7', 'T': '7'}
    variant_word = ''.join(replace[c] if c in replace and random.random() < 0.5 else c for c in mot)
    
    return variant_word

def generer_wordlist(mot, number, output):
    mots_generes = set()
    iterations = 0  # Ajout d'un compteur d'itérations
    with open(output, 'w') as f:
        while len(mots_generes) < number and iterations < 2 * number:  # Limiter les itérations pour éviter une boucle infinie
            # Générer une variante sans caractères spéciaux à la fin
            variant_word = generer_variante_mot(mot)
            
            # Générer une variante avec jusqu'à 2 caractères spéciaux dispersés
            caracteres_aleatoires = ''.join(random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?') for _ in range(random.randint(0, 2)))
            position_insertion = random.randint(0, len(variant_word))
            variant_word_with_special_chars = (
                variant_word[:position_insertion] + caracteres_aleatoires + variant_word[position_insertion:]
            )
            
            # Ajouter les mots générés à l'ensemble pour éviter les doublons
            mots_generes.add(variant_word)
            mots_generes.add(variant_word_with_special_chars)
            
            iterations += 1  # Incrémenter le compteur d'itérations
        
        # Écrire les variantes dans le fichier
        for word in mots_generes:
            f.write(word + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wordlist Generator')
    parser.add_argument('mot', type=str)
    parser.add_argument('--number', type=int, default=1000000)
    parser.add_argument('--output', type=str, default='output.dic')
    args = parser.parse_args()

    generer_wordlist(args.mot, args.number, args.output)
