def simple_encode(text: str, alphabet: list, new_alphabet: list) -> str:
    '''
    Функция зашифрования.
    text - сообщение, котороу нужно зашифровать.
    alphabet - алфавит.
    new_alphabet - алфавит, на который заменяем наш стандартный алфавит.
    '''
    
    text = text.lower()
    len_alphabet = len(alphabet)
    if text == '':
        return 
    else:
        encoded_text = ''
        text = list(text)
        for i in range(len(text)):
            for j in range(len_alphabet):
                if text[i] == alphabet[j]:
                    encoded_text += new_alphabet[j]
                if text[i] not in alphabet:
                    encoded_text += text[i]
                    break

                
        return encoded_text


def simple_decode(text: str, alphabet: list, new_alphabet: list) -> str:
    '''
    Функция расшифрования.
    text - сообщение, котороу нужно зашифровать.
    alphabet - алфавит.
    new_alphabet - алфавит, на который заменяем наш стандартный алфавит.
    '''

    text = text.lower()
    len_alphabet = len(alphabet)
    if text == '':
        return ''
    else:
        decoded_text = ''
        text = list(text)
        for i in range(len(text)):
            for j in range(len_alphabet):
                if text[i] == new_alphabet[j]:
                    decoded_text += alphabet[j]
                if text[i] not in alphabet:
                    decoded_text += text[i]
                    break

        return decoded_text
