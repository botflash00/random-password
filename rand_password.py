import random
import string
def random_password(username):
    print(f'Hello {username}, i am here to help you with random password')

def letters():
    letters=string.ascii_letters
    l=[]
    for i in range(8):
        l.append(random.choice(letters))
    return(l)

def numbers():
    numbers='0 1 2 3 4 5 6 7 8 9'.split()
    num=[]
    for i in range(3):
        num.append((random.choice(numbers)))
    return(num)

def special():
    special='@ # $ % & * ! . + ?'.split()
    char=[]
    for i in range(2):
        char.append((random.choice(special)))
    return(char)
    
def satisfied():
    response=input('Are you Satisfed?(Y/n)').lower()
    if response.startswith('n'):
        return True
    else:
        return False

print('Random Password Genrator'.center(30,'*'))
name=input('Enter your name:')
random_password(name)
while True:
    let=letters()
    n=numbers()
    c=special()
    new=let+c+n
    random.shuffle(new)
    print('Your Random Password is:',''.join(new))
    if satisfied():
        continue
    else:
