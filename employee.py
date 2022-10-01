import sqlite3
import sys
import os
from prettytable import PrettyTable

conn    = sqlite3.connect('empolyee.db', timeout=10)
cur     = conn.cursor()

columns = [
    'ID', 'First Name', 'Last Name', 'Address', 'Status', 'Age'
]

def main():
    os.system("cls")
    print('============================')
    print('    Employee Management     ')
    print('============================')

    print('Menu')
    menus = [
        'Daftar karyawan', 'Tambah Karyawan', 'Edit Karyawan', 'Hapus Karyawan'
    ]

    for i,menu in enumerate(menus):
        print(i+1,'. ', menu)
    
    inpmenu = input('Pilih Menu : ')

    if(inpmenu):
        getMenu(inpmenu)
    else:
        main()
        
def getMenu(menu):
    if menu == '1' :
        print(table())
        back()
    elif menu == '2' :
        create()
    elif menu == '3' :
        edit()
    elif menu == '4' :
        delete()
    else:
        main()

def table():
    os.system("cls")
    qSelectKaryawan = "SELECT * FROM employee"
    result          = cur.execute(qSelectKaryawan)
    
    tbl             = PrettyTable()
    tbl.field_names = columns
    for row in result:
        tbl.add_row(row)

    return tbl

def create():
    os.system("cls")
    print('============================')
    print('    Menu Tambah Karywan     ')
    print('============================')

    fname       =input('Enter First Name : ')
    lname       =input('Enter Last Name  : ')
    address      =input('Enter Address    : ') 
    status      =int(input('Aktif = 1; Tidak Akif = 2 [1/2] : '))
    while( status != 1 and status != 2):
        status      = int(input('Aktif = 1; Tidak Akif = 2 [1/2] : '))
    try:
        age         =int(input('Enter Age : '))
    except:
        print("Not valid")
        age         = 0

    # qInsertKaryawan = '''
    #         INSERT INTO employee(first_name, last_name, address, status, age)
    #         VALUES(?, ?, ?, ?, ?)
    # '''
    
    # cur.execute(qInsertKaryawan, (fname, lname, address, status, age))
                
    cur.execute("""insert into employee(first_name, last_name, address, status, age) 
                values(?, ?, ?, ?, ?)""", (fname, lname, address, status, age), )
    conn.commit()
    back()

def edit():
    os.system("cls")
    print('============================')
    print('     Menu Edit Karyawan     ')
    print('============================')

    print(table())
    
    varID                      =int(input('Enter Employee ID : '))
#    print(varID)

#    qSelectKaryawanByID     ="SELECT * FROM employee WHERE employee_id=?" 
#    result                  = cur.execute(qSelectKaryawanByID, (id,) )
    
    result = cur.execute("SELECT * FROM employee WHERE employee_id=?", (varID), )
    
    tbl             = PrettyTable()
    tbl.field_names = columns
    for row in result:
        tbl.add_row(row)

    fname       =input('Enter First Name : ')
    lname       =input('Enter Last Name  : ')
    address      =input('Enter Address    : ') 
    status      =int(input('Aktif = 1; Tidak Akif = 2 [1/2] : '))
    while( status != 1 and status != 2):
        status     = int(input('Aktif = 1; Tidak Akif = 2 [1/2] : '))
    try:
        age         =int(input('Enter Age : '))
    except:
        print("Not valid")
        age         = 0

    confirm         = input('yakin ingin mengupdate data? [Y/N] ? : ')
    if( confirm == 'y' or confirm == 'Y' ):
        
        # qUpdateKaryawan = '''
        #         UPDATE employee set first_name=?, last_name=?, address=?, status=?, age=? WHERE employee_id = ?
        # '''
        # cur.execute(qUpdateKaryawan(fname, lname, address, status, age, id))
        cur.execute("""UPDATE employee set first_name=?, last_name=?, address=?, status=?, age=? 
                    WHERE employee_id = ?""", (fname, lname, address, status, age, varID), )
                    
        conn.commit()
        back()
        sys.exit()   
    else:
        main()

def delete():
    os.system("cls")
    print('============================')
    print('     Menu Hapus Karyawan    ')
    print('============================')


    print(table())
    
    varID                      =int(input('Enter Employee ID : '))

    # qSelectKaryawanByID     ="SELECT * FROM emloyee WHERE employee_id=?" 
    # result                  = cur.execute(qSelectKaryawanByID, (id,) )
    result = cur.execute("SELECT * FROM employee WHERE employee_id=? ", (varID), )


    tbl             = PrettyTable()
    tbl.field_names = columns
    for row in result:
        tbl.add_row(row)
    print(tbl)

    confirm         = input('yakin ingin menghapus data? [Y/N] ? : ')
    if( confirm == 'y' or confirm == 'Y' ):
        # qDeleteKaryawan = '''
        #         DELETE from employee WHERE employee_id = ?
        # '''
        
        # cur.execute(qDeleteKaryawan(id,))
        cur.execute("DELETE from employee WHERE employee_id=? ", (varID), )
        conn.commit()
        
        if cur.rowcount < 1 :
            print('Gagal hapus data')
        else:
            print('Berhasil hapus data')
        
        back()
       
    else:
        main()
    
def back():
    confirm         = input('continue to main menu? [Y/N] ? : ')
    if( confirm == 'y' or confirm == 'Y' ):
        main()
    else:
        sys.exit()   


main()