def cipher(decoded_text, shift):
    encoded_text = ""
    for l in decoded_text:
        if l.isalpha():
            encoded_text += chr(((ord(l)-shift)+97)%122) if (ord(l)-shift)<97 else chr(ord(l)-shift)
        else:
            encoded_text += l  
    return encoded_text
            

def decipher(encoded_text, shift):
    decoded_text = ""
    for l in encoded_text:
        if l.isalpha():
            decoded_text += chr((ord(l)+shift)%122+97) if (ord(l)+shift)>122 else chr(ord(l)+shift)
        else:
            decoded_text += l
    return decoded_text

while True:
    print('-----')
    option = input('1 - Decode or 2 - Encode text? ex - to exit: ')
    if option == '1':
        text = input('Enter text to decode: ')
        shift = int(input('Enter a shift value: '))
        print(f'Decoded text: {decipher(text, shift)}')
    elif option == '2':
        text = input('Enter text to encode: ')
        shift = int(input('Enter a shift value: '))
        print(f'Decoded text: {cipher(text, shift)}')
    elif option == 'ex':
        exit()
    else:
        print('Something went wrong, please try again!')
