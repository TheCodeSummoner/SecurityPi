from reverse.encrypt import encrypt
from reverse.decrypt import decrypt


def brute_force_keys(message):

    # Define possible characters
    data = "abcdefghijklmnopqrstuvwxyz"

    # Test all permutations (27^5 = 14 348 907 possible options)
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    for e in data:
                        # Create a key by combining the letters
                        key = a + b + c + d + e

                        # Decrypt the message
                        d = decrypt(message, key)

                        # Check the frequency of characters, print if a valid (characters only) sentence was found
                        if check_frequency(d) and d.isprintable():
                            print(d + " Key: " + key)


def check_frequency(sentence):

    # TODO: Find something that checks if a sentence / word is a valid english (PyEnchant??)
    # TODO: Or alternatively figure out better frequency analysis
    max = len(sentence.split())
    counter = 0

    if max <=2:
        return False

    for word in sentence.split():
        if wordnet.synsets(word):
            counter += 1

    if max - counter <= 9:
        return True
    else:
        return False


    # Initialise a dictionary to store the number of occurrences of each letter
    frequency = {}

    # Iterate over each character in sentence (after removing white space characters and making everything lowercase)
    for char in sentence.strip().replace(" ", "").lower():

        # Count how many times did the letter occur in the sentence
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # From https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_by_value = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)

    # Retrieve top 11 characters
    chars = "".join(x[0] for x in sorted_by_value[:11])

    # Get common letters of current characters and "etaoinshrdl"
    chars = "".join(char if char in chars else "" for char in "etaoinshrdl")

    # Return True if length of intersection meets the boundary, False otherwise
    if len(chars) >= 6:
        if "@" not in sentence and "#" not in sentence and "$" not in sentence and "%" not in sentence \
                and "^" not in sentence and "&" not in sentence and "{" not in sentence and "}" not in sentence:
            return True

    return False


brute_force_keys(encrypt("You can take the boy out of the country, but you can’t take the country out of the boy.", "aaaaa"))