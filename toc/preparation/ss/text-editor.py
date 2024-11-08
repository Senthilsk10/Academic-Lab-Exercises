content  = ""
def show():
    global content
    print(content)
    
def save():
    file = input('enter the file name to be saved')
    global content
    with open(file,'w') as f:
        f.write(content)
    print(f"content saved to {file}")
  
def read():
    file = input('enter the file name: ')
    global content
    with open(file,'r') as f:
        content = f.read()
    print(f'file loaded from {file}')
    show()
    
def append():
    global content
    content = content + input('enter your content')
    show()
    
print('\t simple text editor\n 1.show \n 2.load \n 3.save \n 4.append \n 5.exit\n')
while True:
    print( "\n1.show \n2.read \n3.save 4.\append 5.exit\n")
    op = int(input("enter you choice: "))
    if op == 1:
        show()
    elif op == 2:
        read()
    elif op == 3:
        save()
    elif op==4:
        append()
    elif op==5:
        break