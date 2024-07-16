from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    result=""
    shift=shift%len(alphabet)
    if(direction=="encode"):
        shift*=1
        for letter in text:
            position=alphabet.index(letter)
            position+=shift
            result+=alphabet[position]
    elif(direction=='decode'):
        shift*=(-1)
        for letter in text:
            position=alphabet.index(letter)
            position+=shift
            result+=alphabet[position]
    return result     
should_end=False
while(not should_end):
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))
 result=caesar(direction,text,shift)
 print(f"The {direction} result is ->{result}")
 restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
 if restart == "no":
    should_end = True
    print("Goodbye")
