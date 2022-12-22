def affine_reccurent_encode(text: str, alphabet: list, key_a1:int, key_a2: int, key_b1:int, key_b2: int) -> str:
    """
    Функция зашифрования.
    text - сообщение, котороу нужно зашифровать.
    alphabet - алфавит.
    key_a1 итд - ключи.
    """
    keys_a = [key_a1, key_a2]
    keys_b = [key_b1, key_b2]
    lenght = len(alphabet)
    lenght_text = len(text)
    encoded_text = ''
    cnt = 0


    for i in range(2, lenght_text): # Считаем ключи.
        keys_a.append((keys_a[i - 1] * keys_a[i - 2]) % lenght)
        keys_b.append((keys_b[i - 1] + keys_b[i - 2]) % lenght) 
        
    for i in range(lenght_text):
        for j in range(lenght):
            if text[i] not in alphabet:
                encoded_text += text[i]
                break
            if text[i] == alphabet[j]:
                bin = ((keys_a[cnt] * j + keys_b[cnt]) % lenght)
                encoded_text += alphabet[bin]
                cnt += 1
                
    return encoded_text

                    
def affine_reccurent_decode(text: str, alphabet: list, key_a1:int, key_a2: int, key_b1:int, key_b2: int) -> str:
    """
    Функция расшифрования.
    text - сообщение, котороу нужно расшифровать.
    alphabet - алфавит.
    key_a1 итд - ключи.
    """
    keys_a = [key_a1, key_a2]
    keys_b = [key_b1, key_b2]
    lenght = len(alphabet)
    lenght_text = len(text)
    decoded_text = ''
    cnt = 0

    for i in range(2, lenght_text): # Считаем ключи.
        keys_a.append((keys_a[i - 1] * keys_a[i - 2]) % lenght)
        keys_b.append((keys_b[i - 1] + keys_b[i - 2]) % lenght)
    print(keys_a, keys_b)
    

    for i in range(lenght_text):
        for j in range(lenght):
            if text[i] not in alphabet:
                decoded_text += text[i]
                break
            if text[i] == alphabet[j]:
                temp = 0
                for num in range(lenght):
                    if (keys_a[cnt] * num) % lenght == 1:
                        temp = num
                        print(temp)
                bin = (((j - keys_b[cnt]) * temp) % lenght)
                decoded_text += alphabet[bin]
                cnt += 1

    return decoded_text
