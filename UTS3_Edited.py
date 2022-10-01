# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:44:48 2021

@author: Lenovo
"""

todolist = ["Aku akan Makan", "Aku akan mandi", "Aku akan belajar"]
def main():

    jumlah = len(todolist)
    print(jumlah)
    def list_todo():
        if jumlah == 0:
            list_todo.append(todolist)
            
    def show_todo():
        for daftar in range(jumlah):
                print(daftar+1, ".", todolist[daftar])   
    
    main_menu = ["1. TAMBAH TO DO LIST", 
                 "2. HAPUS TO DO LIST", 
                 "3. KELUAR TO DO LIST"]
    
    def liat_menu():
        for liat in main_menu:
            print(liat)

            
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    show_todo()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("---------------------------")
    
    print("Tekan enter untuk melihat Menu")
    
    print("Menu:")

    
    
    liat_menu()
    
    pilih_menu = input("Pilih Menu: ")
    
    if pilih_menu == '1':
        input1 = input("Tambah Aktivitas:")
        todolist.append(input1)
        jumlah += 1
        main()
    elif pilih_menu == '2':
        input2 = input("Hapus Aktivitas:")
        if input2.isnumeric():
            gone = int(input2)-1
            todolist.pop(gone)
            jumlah -= 1
            main()
        else:
            todolist.remove(input2)
            jumlah -= 1
            main()
    elif pilih_menu == '3':
        print("Keluar")
    else:
        print("Input Salah")
             
main()