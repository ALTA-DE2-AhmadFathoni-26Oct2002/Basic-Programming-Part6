def caesar(offset, input_str):
    ans = ""
    for i in range (len(input_str)):
        karakter = input_str[i]
    
        if karakter ==  " ":
            ans += " "
        elif (karakter.isupper()):
            ans += chr((ord(karakter) + offset-65)%26+65)
        else:
            ans += chr((ord(karakter) + offset-97)%26+97)
    return ans

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl