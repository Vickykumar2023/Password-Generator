from tkinter import *       # pip install pillow
import string
import random       # pip install random



root=Tk()
root.configure(bg="green")
root.title("Password Generator Develop By Vicky Kumar")
root.geometry("500x500")


#====================== delete Funcation============================
        
def delete():
    password_Field.delete(ANCHOR)
#============generater Funcation ==============================
def generater():
    small_alphabet=string.ascii_lowercase
    cpital_alphabet=string.ascii_uppercase
    number=string.digits
    special_character=string.punctuation
   #====Week funcation================================================
   
    week=small_alphabet
    #  Medium Funcation ======================================
    v=small_alphabet+cpital_alphabet+number
    
    # Strong Funcation ======================================
    all=small_alphabet+cpital_alphabet+number+special_character
    length_9=int(length_Entry.get())
    
   
    #====================================================================
    if choice.get()==1:
        password_Field.insert(0,random.sample(week,length_9))
     
    if choice.get()==2:
        password_Field.insert(0,random.sample(v,length_9))   
   
        
    if choice.get()==3:
        password_Field.insert(0,random.sample(all,length_9))
        

# ==== font Style================
choice=IntVar()
Font=('arial',12,"bold")

# ===========password Generater===============
passwordLabel=Label(root,text="Password Generator", font=("time new roman",26,"bold"),bg="cadetblue",fg="white")
passwordLabel.place(x=0,y=0,width=500,height=50)

#==================Week Password ======================
weak=Radiobutton(root,text="Weak Password",value=1,variable=choice,font=Font,bg="orange",fg="black")
weak.place(x=30,y=310,width=200)

#=============Medium Password==============================
medium=Radiobutton(root,text="Medium Password",value=2,variable=choice,font=Font,bg="orange",fg="black")
medium.place(x=30,y=350,width=200)

# ===================Strong Password ======================================
Strong=Radiobutton(root,text="Strong Password",value=3,variable=choice,font=Font,bg="orange",fg="black")
Strong.place(x=260,y=310,width=200)

#=======================Password Length =============================
length=Label(root,text="Password Length",font=Font,bg='red', fg="white")
length.place(x=50,y=390,width=400)

# =====================passWord Size or Length in the input ==================
length_Entry=Spinbox(root,from_=5,to_=9999,font=Font)
length_Entry.place(x=150,y=420,width=150)


# ============Generate Button  ========================
generat_button=Button(root,text="Generat",font=Font,bg='blue',command=generater)
generat_button.place(x=25,y=450,width=450,height=40)

#========== Output Box =================================
password_Field=Listbox(root,width=25,bd=2,font=("arial,10,bold"),bg="yellow")
password_Field.place(x=15,y=52,width=450,height=250)

#====================== Copy Button ================================
copy_button=Button(root,text="Delete",font=Font,bg="orange",fg="black",command=delete)
copy_button.place(x=260,y=350,width=200)



mainloop()