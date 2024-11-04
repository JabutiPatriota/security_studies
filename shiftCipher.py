# In using this code, work with upperCase characters, whithout backspaces and with at least one character

from collections import Counter
from operator import itemgetter

# Function that implements the shift cipher (mod 26)
def shiftCipher(shift, message):
    messageList = list(message) # Create the "listified" object of the message
    messageListAscNorm = map(lambda x: ord(x) - 65, messageList) # Transform the list characters using ASCII, A = 0
    messageListAscNormShifted = map(lambda x: (x + shift) % 26, messageListAscNorm) # Shifting characters
    cipherTextList = map(lambda x: chr(x + 65), messageListAscNormShifted) # Retransform the list shifted using ASCII, A = 0
    cipherText = ''.join(cipherTextList) # Retransform the list of characters into a string object
    
    print(f'Cipher Text: {cipherText}')

    return(cipherText)


# Function that decrypts the shift cipher (brute force mode)
def hardDecrypt_shiftCipher(cipherText):
    cipherTextList = list(cipherText) # Create the "listified" object of the cipherText
    cipherTextListAscNorm = list(map(lambda x: ord(x) - 65, cipherTextList)) # Transform the list characters using ASCII, A = 0
    for shift in range(1,26): # All shift possibles
        cipherTextListAscNormDeshifted = map(lambda x: (x - shift) % 26, cipherTextListAscNorm.copy()) # Deshifting characters
        plainTextList = map(lambda x: chr(x + 65), cipherTextListAscNormDeshifted) # Retransform the list deshifted using ASCII, A = 0
        plainText = ''.join(plainTextList) # Retransform the list of characters into a string object

        print(f'Brute Force Decrypt - Shift: {shift}; Plain Text: {plainText}')


# Function that decrypts the shift cipher (based on most frequency of letters - letter A)
def frequencyDecrypt_shiftCipher(cipherText):
    counter = Counter(cipherText) # creating Counter object of the cipherText
    countDict = dict(counter) # Transforming counter to dict object
    countDictSorted = sorted(countDict.items(), key = itemgetter(1), reverse=True) # Sorting the dict object in a list of tuples based on frequency of characters
    shift = ord(countDictSorted[0][0]) - 65 # Assuming that A is the letter that appers more than all (A = 65 ASCII)
    cipherTextList = list(cipherText) # Create the "listified" object of the cipherText
    cipherTextListAscNorm = list(map(lambda x: ord(x) - 65, cipherTextList)) # Transform the list characters using ASCII, A = 0
    cipherTextListAscNormDeshifted = map(lambda x: (x - shift) % 26, cipherTextListAscNorm.copy()) # Deshifting characters
    plainTextList = map(lambda x: chr(x + 65), cipherTextListAscNormDeshifted) # Retransform the list deshifted using ASCII, A = 0
    plainText = ''.join(plainTextList) # Retransform the list of characters into a string object

    print(f'Frequency Decrypt - Shift: {shift}; Plain Text: {plainText}')
    
    return(plainText)


# Testing
hardDecrypt_shiftCipher(shiftCipher(17,"OSENHORDOSANEIS"))
frequencyDecrypt_shiftCipher(shiftCipher(7, "TESTANDOCOMUMAFRASEEMQUEALETRAQUEMAISAPARECEEALETRAADEABACATE"))
    