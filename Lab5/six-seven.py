def create_acronym (text):
    '''
    >>> create_acronym("random access memory")
    'RAM - random access memory'
    '''
    texts = []
    while True:
        if text.find("\n") != -1:
            texts.append(text[0:text.find("\n")])
            text = text[text.find("\n") + 1:]
        else:
            texts.append(text)
            break
    actonym = ""
    texts_len = len(texts)
    for i in range(texts_len):
        text = texts[i].split()
        len_text = len(text)
        for j in range(len_text):
            actonym += str((text[j][0].upper()))
        if i == texts_len - 1:
            actonym += " - " + str(texts[i])
            break
        actonym += " - " + str(texts[i]) + "\n"
    return actonym

def caesar_encode (message, key):
    '''
    >>> caesar_encode ("computer", 3)
    'frpsxwhu'
    >>> caesar_encode ("hello world", 8)
    'pmttw ewztl'
    '''
    encode = ""
    message = message.lower()
    if key >= 26:
        part = key // 26
        key = key - 26 * part
    len_message = len(message)
    for i in range(len_message):
        if message[i] == " ":
            encode += " "
            continue
        if ord(message[i]) + key >= 123:
            encode += chr(ord(message[i]) + key - 26)
            continue
        encode += chr(ord(message[i]) + key)
    return encode

print(caesar_encode ("cat", 22))

def caesar_decode (message, key):
    '''
    >>> caesar_decode ("favorite yogogort", 35)
    'wrmfizkv pfxfxfik'
    >>> caesar_decode ("hello minecraft", 4)
    'dahhk iejaynwbp'
    '''
    decode = ""
    message = message.lower()
    if key >= 26:
        part = key // 26
        key = key - 26 * part
    len_message = len(message)
    for i in range(len_message):
        if message[i] == " ":
            decode += " "
            continue
        if ord(message[i]) - key <= 96:
            decode += chr(ord(message[i]) - key + 26)
            continue
        decode += chr(ord(message[i]) - key)
    return decode
