from functions_arq import *
import requests

def line():
    print('-'*50)


def header(msg):
    line()
    print(msg.center(50))
    line()
def show(menu):
    line()
    c = 1
    for i in menu:
        print(f'{c} - {i}')
        c+=1
    line()

def readInt(number):
    while True:
        try:
            entry = int(input(number))
        except:
            print('ENTER A NUMBER! ')
        else:
            return entry
def register():
    while True:
        a = open('registers.txt', 'r')
        ok = True
        name = input('Type your name: ').lower()
        for line in a:
            n = line.split(';')
            if n[0] == name:
                print('existing name, create another')
                ok = False
                break
        if ok:
            break
    password = input('Create your password: ')
    number_home = readInt('Type your number home: ')
    address = find_cep('Type your CEP: ',number_home)
    cep = address['cep']
    street = address['logradouro']
    number = address['numero']
    return addingRecords(name,password,cep,street,number)

def login():
    while True:
        ok = False
        a = open('registers.txt', 'r')
        name = input('Type your name: ')
        password = input('Type your password: ')
        for line in a:
            n = line.strip().split(';')
            if n[0] == name and n[1] == password:
                print('Login successful!')
                ok = True
                break
        if ok:
            break
        print('incorrect name or password')
def find_cep(num, num_home):
    while True:
        cep = input(num)
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            data['numero'] = num_home
            return data
        else:
            print(f"Erro ao buscar o CEP: {response.status_code}")

def validate_edit(name):
    a = open('registers.txt', 'r')
    all = a.readlines()
    ok = False
    while True:
        index = 0
        nick = input(name)
        for i in all:
            n = i.split(';')
            if nick == n[0]:
                ok = True
                break
            index+=1
        if ok:
            return index
        else:
            print('name not found')
def edit():
    with open('registers.txt', 'r') as a:
        all = a.readlines()

    for i in all:
        name = i.split(';')
        print(name[0])
    validate = validate_edit('Type name that you would like to edit: ')
    all[validate] = register()
    with open('registers.txt', 'w') as a:
        a.writelines(all)

def delete():
    with open('registers.txt','r') as a:
        all = a.readlines()
    for i in all:
        name = i.split(';')
        print(name[0])
    validate = validate_edit('Type name that you would like to edit: ')
    all.pop(validate)
    with open('registers.txt', 'w') as a:
        a.writelines(all)

