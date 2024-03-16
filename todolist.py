import tkinter as tk
import sqlite3

def tablo_olustur():
    baglanti = sqlite3.connect("db_todo.db") # Database bağlantısını sağlar.
    cursor = baglanti.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mission2 (mission_name TEXT)''')
    baglanti.commit()
    baglanti.close()

def veri_kaydet():
    baglanti = sqlite3.connect("db_todo.db")
    cursor = baglanti.cursor()
    cursor.execute('''DELETE FROM mission2''')  # Önceki verileri temizler.
    for i in range(listbox.size()):
        veri = listbox.get(i)
        cursor.execute('''INSERT INTO mission2 (mission_name) VALUES (?)''', (veri,))
    baglanti.commit()
    baglanti.close()

def veri_yukle():
    baglanti = sqlite3.connect("db_todo.db")
    cursor = baglanti.cursor()
    cursor.execute('''SELECT mission_name FROM mission2''')
    mission = cursor.fetchall()
    for veri in mission:
        listbox.insert(tk.END, veri[0])
    baglanti.close()

def listbox_item_ekle():
    veri = gorev_entry.get()
    listbox.insert(tk.END, veri)
    veri_kaydet()  # Yeni veriyi kaydeder.

def listbox_item_sil():
    secili = listbox.curselection()
    if secili:
        index = secili[0]
        listbox.delete(index)
        veri_kaydet()  # Silinen veriyi kaydeder.

def home(): #arayüz oluşturur. Yeni pencere açılır ve işlemler burada yapılır.
    global listbox, gorev_entry, home_page
    home_page = tk.Tk()
    home_page.title("To Do List Page")
    
    screen_width = home_page.winfo_screenwidth()
    screen_height = home_page.winfo_screenheight()
   
    window_width = 700
    window_height = 600
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    home_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    home_page.configure(bg="white")

    label = tk.Label(home_page, text="Görev: ")
    label.pack(pady=20)

    gorev_entry = tk.Entry(home_page, width=40)
    gorev_entry.pack(pady=10)

    g_button=tk.Button(home_page,text="Ekle",command=listbox_item_ekle)
    g_button.pack(pady=10)

    label2= tk.Label(home_page,text="Görevler")
    label2.pack(pady=20)

    d_button=tk.Button(home_page,text="Sil",command=listbox_item_sil)
    d_button.pack(pady=20)

    listbox = tk.Listbox(home_page)
    listbox.pack(padx=10,pady=10)

    tablo_olustur()

    veri_yukle()

    home_page.mainloop()

if __name__ == '__main__':
    home()
