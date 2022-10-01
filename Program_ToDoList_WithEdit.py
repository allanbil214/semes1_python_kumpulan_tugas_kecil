listTodo = ['To Do List | Kosong']

def Main():
    intRange = len(listTodo)

    def checkKosong():
        if intRange == 0:
            listTodo.append('To Do List | Kosong')
            
    def showTodo():
        for nganu in range(intRange):
            if listTodo[0] == 'To Do List | Kosong':  
                print(listTodo[nganu])     
                listTodo.pop(0)
            else:                
                print(nganu+1, '.', listTodo[nganu])
                
    menu = ['1. Tambah\t| To Do List',
            '2. Coret\t| To Do List',
            '3. Edit\t\t| To Do List',
            '4. Keluar\t| Dari Aplikasi']

    def showMenu():
        for x in menu:
            print(x)

    print('______________________________')
    print('| PROGRAM TO-DO LIST |')
    print('______________________________')

    print('------------------------------')
    showTodo()
    print('------------------------------')

    input('Tekan Enter Untuk Melihat Menu.')

    print('Menu')

    showMenu()

    inputan = input('Pilih Menu : ')

    if inputan == '1':
        subInput1 = input('Tambah Aktifitas : ')
        listTodo.append(subInput1)
        intRange += 1
        Main()        
    elif inputan == '2':
        subInput2 = input('Coret Aktifitas : ')
        if subInput2.isnumeric():
            poppy = int(subInput2) - 1
            listTodo.pop(poppy)
            intRange -= 1
            checkKosong()
            Main()
        else:
            listTodo.remove(subInput2)
            intRange -= 1
            checkKosong()
            Main()
    elif inputan == '3':
        subInput2 = input('Edit Aktifitas : ')
        
    elif inputan == '4':
        print('Keluar')
    else:
        print('Input salah!')
        Main()

Main()