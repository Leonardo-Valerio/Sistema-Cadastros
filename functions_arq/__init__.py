
def fileExists():
    try:
        a = open('registers.txt', 'rt')
    except:
        a = open('registers.txt','wt+')
        a.close()

def addingRecords(name, password, cep,street,number):
    try:
        a = open('registers.txt','at')
    except:
        print('error')
    else:
        a.write(f'{name};{password};{cep};{street},{number}\n')
        return f'{name};{password};{cep};{street},{number}\n'
