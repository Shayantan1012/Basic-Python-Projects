letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random;

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

size=nr_letters+nr_symbols+nr_numbers;
final_password=""
while(len(final_password)!=size):
    char=random.randint(0,2)
    if(char==1 and nr_letters ):
        ans_letters=str(letters[random.randint(0,len(letters)-1)])
        final_password+=ans_letters
        nr_letters-=1;
    
    elif(char==2 and nr_symbols):
        ans_symbols=str(symbols[random.randint(0,len(symbols)-1)])
        final_password+=ans_symbols
        nr_symbols-=1

    elif(char==0 and nr_numbers):
        ans_numbers=str(numbers[random.randint(0,len(numbers)-1)])
        final_password+=ans_numbers
        nr_numbers-=1
        
print(f"The final password is->{final_password}")
 