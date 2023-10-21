# InvertedCaesar_Cipher_Decryption


This Python program allows you to decrypt messages that have been encrypted using an Inverted Caesar cipher. The Inverted Caesar cipher is a type of substitution cipher that shuffles the alphabet. By iterating through all possible keys (k), you can decrypt the ciphertext and identify the original message.

Usage
1.Ensure you have Python installed on your system.

2.Copy and paste the provided Python code into a Python environment or script.

3.Modify the ciphertext variable with the encrypted message that you want to decrypt.

4.Run the program. It will iterate through all possible keys from 1 to the length of the alphabet, decrypt the ciphertext for each key, and print the results.

5.Examine the decrypted texts and their corresponding keys to identify the correct decryption.

Function Explanation
The encrypt function is used to encrypt a plaintext message using the Inverted Caesar cipher with a specified key k.

The decrypt function is used to decrypt a ciphertext message using the Inverted Caesar cipher with a specified key k. It utilizes the encrypt function with a negative key to perform the decryption.

The brute_force function is the main tool for decrypting the message. It iterates through all possible keys, decrypts the ciphertext for each key, and prints the decrypted text along with the corresponding key.

Example Usage
Here's an example of how to use the code:

python
Copy code
# Call the brute_force function with the given ciphertext
ciphertext = "kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"
brute_force(ciphertext)
The program will display all possible plaintext and key combinations. Look for the one that makes the most sense in the context of your message to identify the correct decryption.