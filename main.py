alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)

def brute_force(ciphertext):
    for k in range(1, len(alphabet)):
        decrypted_text = decrypt(ciphertext, k)
        print(f"Key (k): {k}, Decrypted Text: {decrypted_text}")

# Call the brute_force function with the given ciphertext
ciphertext = "kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"
brute_force(ciphertext)
