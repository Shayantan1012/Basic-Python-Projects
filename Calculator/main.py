from art import logo
print(logo)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

oparator={
        '+':add,
        '-':sub,
        '*':mul,
        '/':div,
    }
    
def cal():
    should_continue=True
    num1=int(input("Give the first number->"))
    while(should_continue):
        opa=(input("Give the  oparator symbol->"))
        if(opa=='+' or opa=='-' or opa=='/' or opa=='*'):
            oparation=oparator[opa]
            num2=int(input("Give the second number->"))
            answer=oparation(num1,num2)
            print(f"{num1} {opa} {num2} = {answer}")

            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
                num1 = answer
            else:
                should_continue = False
        else:
            print("Give a valid oparator symbol!!!")
            continue        
            
cal()            

