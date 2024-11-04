import itertools

lettersUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function that implements the transposition cypher
def transpositionCipher(key, plainText):
    for i in range(len(key) - len(plainText) % len(key)):  # Completing the plaintext with letters untill len(plaintext) % len(key) == 0
        plainText += lettersUpperCase[i % 26]  

    print(f"Plaintext is {plainText}")     

    listedKey = list(key)                   # list of the input key letters                               
    listedPlainText = list(plainText)       # list of the input plaintext
    cipherStrings = []                      # list that will receive each key char corresponding string, with the key, in a tuple
    sortedCipherStrings = []                # sorted list of key char corresponding strings

    for keyCharIndex in range(len(listedKey)):                                      # for each index of the key's list                                
        lettersCiphered = []                                                        # list that will construct the cipher strings corresponding to each key
        for textCharIndex in range(len(listedPlainText)):                           # for each index of the plaintext characters list
            if textCharIndex % len(listedKey) == keyCharIndex:                      # if the plaintext char index corresponds to the key index
                lettersCiphered.append(listedPlainText[textCharIndex])              # add plaintext char to the cipher string list
        cipherStrings.append((listedKey[keyCharIndex],''.join(lettersCiphered)))    # add the tuple of cipher string and key to the list of cipher strings

    sortedCipherStrings = sorted(cipherStrings)                                                 # receives sorted cipher strings based on keys
    sortedCipherStrings = map(lambda keyStringTuple: keyStringTuple[1], sortedCipherStrings)    # erase the tuples and keys, preserving the cipher strings

    cipherText = ''.join(sortedCipherStrings)       # final ciphertext is generated concatenating the sorted cipher strings
    
    print(cipherText)
    return cipherText


def decrypt_transposition(cipherText, max_cols):
    for cols in range(2, max_cols + 1):                             # Trying different columns length, until the max parameter
        rows = len(cipherText) // cols                              # finding the number of rows
        
        matrix = ['' for _ in range(cols)]                          # Creating a cols matrix
                                                                
        # Fill the matrix based on columns
        index = 0                                                   # index of letters in ciphertext
        for col in range(cols):                                     # for each column
            for row in range(rows):                                 # for each row
                if index < len(cipherText):                         # if we are not in the end of the ciphertext
                    matrix[col] += cipherText[index]                # fill the corresponding matrix term with the letter
                    index += 1                                      # increment index
        
        decrypted_message = ''
        print(matrix)

        for matrixInstance in itertools.permutations(matrix):       # Consider all possibles of columns combinations (permutations)
            for i in range(rows):                                   # Read row by row
                for col in matrixInstance:
                    decrypted_message += col[i]
            
            # Print the decripted text attempt
            print(f"Cols: {cols}, Decrypted: {decrypted_message}")

            decrypted_message = ''

decrypt_transposition(transpositionCipher("MEGA", "TESTECRIPTOGRAFIA"), 4)