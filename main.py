from functions_main import *
from functions_arq import *
fileExists()
menu = ["REGISTER", 'LOGIN', 'EDIT LOGIN', 'DELETE LOGIN', "EXIT"]

while True:
    show(menu)
    options = readInt('Enter the desired option: ')

    if options == 1:
        header(menu[0])
        register()
    elif options == 2:
        header(menu[1])
        login()
    elif options == 3:
        header(menu[2])
        edit()
    elif options == 4:
        header(menu[3])
        delete()
    elif options == 5:
        header('LEAVING')
        break


