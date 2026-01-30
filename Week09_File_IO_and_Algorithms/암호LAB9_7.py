def encrypt(text, key):

    result = ""

    for char in text:
        if 'a' <= char <= 'z':
            new_num = ord(char) + key
            
            if new_num > ord('z'):
                new_num -= 26
                
            result += chr(new_num)
            
        elif 'A' <= char <= 'Z':
            new_num = ord(char) + key
            
            if new_num > ord('Z'):
                new_num -= 26
                
            result += chr(new_num)
            
        else:
            result += char
            
    return result



input_text = input("평문: ")
shift_key = 3
encrypted_text = encrypt(input_text, shift_key)

print(f"암호문: {encrypted_text}")