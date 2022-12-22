def affine_encode(text: str, key_a: int, key_b: str, alphabet: str) -> str:
    """
    !!!Ключи должны быть взаимопростыми.
    Функция зашифрования.
    text - сообщение, котороу нужно зашифровать.
    alphabet - алфавит.
    key_a, key_b - ключи.
    """
    
    if len(alphabet) % key_a == 0:
        return 'error in key'
    else:
        encoded_text = ''
        for i in range(len(text)):
            for j in range(len(alphabet)):
                if text[i] not in alphabet:
                    encoded_text += text[i]
                    break
                if text[i] == alphabet[j]:
                    bin = (key_a * j + key_b) % len(alphabet)
                    encoded_text += alphabet[bin]
                    break
    return encoded_text


def affine_decode(text: str, key_a: int, key_b: int, alphabet: str) -> str:
    """
    !!!Ключи должны быть взаимопростыми.
    Функция зашифрования.
    text - сообщение, котороу нужно расшифровать.
    alphabet - алфавит.
    key_a, key_b - ключи.
    """
    if len(alphabet) % key_a == 0:
        return 'error in key'
    else:
        decoded_text = ''
        for i in range(len(alphabet)):
            if (key_a * i) % len(alphabet) == 1:
                key_a = i
        for i in range(len(text)):
            for j in range(len(alphabet)):
                if text[i] not in alphabet:
                    decoded_text += text[i]
                    break
                if text[i] == alphabet[j]:
                    bin = ((j - key_b) * key_a) % len(alphabet)
                    decoded_text += alphabet[bin]
                    break
    return decoded_text
