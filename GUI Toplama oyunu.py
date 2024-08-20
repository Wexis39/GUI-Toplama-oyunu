import tkinter as tk
import random

window = tk.Tk()
window.title("Matematik Oyunu")
window.geometry("360x430")
window.resizable(width=False,height=False)

secilen = ""

score = 0
kolay_score = 10
orta_score = 30
zor_score = 60
extrem_score = 100 

correct_answer = 0
user_answer = 1

def update_score(value):
    global score, correct_answer, user_answer
    skor2.config(text=score)
    if correct_answer == user_answer:
        score += value
        skor2.config(text=score)

def kolay_skor():
    update_score(kolay_score)

def orta_skor():
    update_score(orta_score)

def zor_skor():
    update_score(zor_score)

def extrem_skor():
    update_score(extrem_score)

        
def onaylama():
    global user_answer
    global correct_answer
    try:
        user_answer = int(tag1.get())
        correct_answer = random_sayi1 + random_sayi2
        if user_answer == correct_answer:
            if secilen == "Basit toplama":
                basit_toplama()
                true.config(text="DOĞRU")
                tag1.delete(0,tk.END)
            elif secilen == "Orta toplama":
                orta_toplama()
                true.config(text="DOĞRU")
                tag1.delete(0,tk.END)
            elif secilen == "Zor toplama":
                zor_toplama()
                true.config(text="DOĞRU")
                tag1.delete(0,tk.END)
            elif secilen == "Extrem toplama":
                extrem_toplama()
                true.config(text="DOĞRU")
                tag1.delete(0,tk.END)    
        else:
            false.config(text="YANLIŞ")
            tag1.delete(0,tk.END)
    except:
        false.config(text="Geçersiz Giriş")
        tag1.delete(0,tk.END)    
          

def basit_timer():
    global basit_sure
    if basit_sure > 0:
        sure2.config(text=f"{basit_sure} s")
        basit_sure -= 1
        window.after(2000, basit_timer)
    else:
        false.place(x=50,y=325)
        false.config(text=f"Süre Bitti Puanın: {score}")
        skor2.destroy()
        skor1.destroy()
        sure1.destroy()
        sure2.destroy()
        
def orta_timer():
    global orta_sure
    if orta_sure > 0:
        sure2.config(text=f"{orta_sure} s")
        orta_sure -= 1
        window.after(2000, orta_timer)
    else:
        false.place(x=50,y=325)
        false.config(text=f"Süre Bitti Puanın: {score}")
        skor2.destroy()
        skor1.destroy()
        sure1.destroy()
        sure2.destroy()
        
def zor_timer():
    global zor_sure
    if zor_sure > 0:
        sure2.config(text=f"{zor_sure} s")
        zor_sure -= 1
        window.after(2000, zor_timer)
    else:
        false.place(x=50,y=325)
        false.config(text=f"Süre Bitti Puanın: {score}")
        skor2.destroy()
        skor1.destroy()
        sure1.destroy()
        sure2.destroy()
 
def extrem_timer():
    global extrem_sure
    if extrem_sure > 0:
        sure2.config(text=f"{extrem_sure} s")
        extrem_sure -= 1
        window.after(2000, extrem_timer)
    else:
        false.place(x=50,y=325)
        false.config(text=f"Süre Bitti Puanın: {score}")
        skor2.destroy()
        skor1.destroy()
        sure1.destroy()
        sure2.destroy()               

def reset_timer():
    global basit_sure, orta_sure, zor_sure, extrem_sure
    basit_sure = 20
    orta_sure = 40
    zor_sure = 60
    extrem_sure = 85
    

def clear():
    false.config(text="")
    true.config(text="")

def update_label4():
    label4.config(text=f"{secilen} seçildi")   

def basit_toplama():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    global secilen
    global random_sayi1
    global random_sayi2
    random_sayi1 = random.randint(0,15)
    random_sayi2 = random.randint(0,15)
    gosterge = (random_sayi1,"+",random_sayi2,"=","?")
    label2.config(text=gosterge)
    label2.place(x=100,y=140)
    secilen="Basit toplama"
    sure2.config(text="")
    reset_timer()
    basit_timer()
    update_label4()
    clear()
    kolay_skor()
    
def orta_toplama():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    global secilen
    global random_sayi1
    global random_sayi2
    random_sayi1 = random.randint(5,40)
    random_sayi2 = random.randint(5,40)
    gosterge = (random_sayi1,"+",random_sayi2,"=","?")
    label2.config(text=gosterge)
    label2.place(x=80,y=140)
    secilen="Orta toplama"
    sure2.config(text="")
    reset_timer()
    orta_timer()
    update_label4()
    clear()
    orta_skor()
    
def zor_toplama():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    global secilen
    global random_sayi1
    global random_sayi2
    random_sayi1 = random.randint(60,300)
    random_sayi2 = random.randint(60,300)
    gosterge = (random_sayi1,"+",random_sayi2,"=","?")
    label2.config(text=gosterge)
    label2.place(x=60,y=140)
    secilen="Zor toplama"
    sure2.config(text="")
    reset_timer()
    zor_timer()
    update_label4()
    clear()
    zor_skor()

def extrem_toplama():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    global secilen
    global random_sayi1
    global random_sayi2
    random_sayi1 = random.randint(200,700)
    random_sayi2 = random.randint(200,700)
    gosterge = (random_sayi1,"+",random_sayi2,"=","?")
    label2.config(text=gosterge)
    label2.place(x=60,y=140)
    sure2.config(text="")
    secilen="Extrem toplama"
    reset_timer()
    extrem_timer()
    update_label4()
    clear()
    extrem_skor()
    
   
label1=tk.Label(window,text="Toplama Oyunu",fg="red",font="comic 18 bold")
label1.pack()

label2=tk.Label(window,text="",fg="black",font="comic 30 bold")
label2.place(x=110,y=280)

button1=tk.Button(window,text="Basit",fg="green",font="comic 12 bold",command=basit_toplama)
button1.place(x=30,y=50)

button2=tk.Button(window,text="Orta",fg="green",font="comic 12 bold",command=orta_toplama)
button2.place(x=120,y=50)

button3=tk.Button(window,text="Zor",fg="green",font="comic 12 bold",command=zor_toplama)
button3.place(x=200,y=50)

button4=tk.Button(window,text="Extrem",fg="green",font="comic 12 bold",command=extrem_toplama)
button4.place(x=270,y=50)

label3=tk.Label(window,text="Cevabınız",fg="blue",font="comic 12 italic")
label3.place(x=135,y=206)

label4=tk.Label(window,text="",fg="blue",font="comic 12")
label4.place(x=105,y=100)

tag1 = tk.Entry(window)
tag1.place(x=110,y=240)

button5=tk.Button(window,text="Onayla",fg="black",font="comic 10 bold",command=onaylama)
button5.place(x=142,y=280)

true=tk.Label(window,text="",fg="green",font="comic 20 bold")
true.place(x=117,y=325)

false=tk.Label(window,text="",fg="red",font="comic 20 bold")
false.place(x=117,y=325)

sure1=tk.Label(window,text="Süre: ",fg="black",font="comic 17 bold")
sure1.place(x=20,y=380)

skor1=tk.Label(window,text="Skor: ",fg="black",font="comic 17 bold")
skor1.place(x=230,y=380)

sure2=tk.Label(window,text="",fg="black",font="comic 17 bold")
sure2.place(x=100,y=380)

skor2=tk.Label(window,text="",fg="black",font="comic 17 bold")
skor2.place(x=310,y=380)

window.mainloop()
