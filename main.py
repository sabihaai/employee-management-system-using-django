from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognitation_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("face recognization system")

#first_image
        img=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\h1.jpg")
        img=img.resize((1300,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)


#bg image
        img4=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\bg.jpg")
        img4=img4.resize((1300,620),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=130,width=1300,height=620)


# employee button
        img5=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\1.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5)
        b1.place(x=250,y=50,width=150,height=150)
        

        b1=Button(bg_image,text= "Employee Details",font=("times new roman",15,"bold"),bg="black",fg="White")
        b1.place(x=250,y=200,width=150,height=50)


# button detector
        img6=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\2.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_image,image=self.photoimg6)
        b2.place(x=450,y=50,width=150,height=150)
        

        b2=Button(bg_image,text= "Face Detector",font=("times new roman",15,"bold"),bg="black",fg="White")
        b2.place(x=450,y=200,width=150,height=50)



#Attendance button
        img7=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\3.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_image,image=self.photoimg7)
        b3.place(x=650,y=50,width=150,height=150)
        

        b3=Button(bg_image,text= "Attendance",font=("times new roman",15,"bold"),bg="black",fg="White")
        b3.place(x=650,y=200,width=150,height=50)

 #help button
        img8=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\4.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_image,image=self.photoimg8)
        b4.place(x=850,y=50,width=150,height=150)
        

        b4=Button(bg_image,text= "Help Desk",font=("times new roman",15,"bold"),bg="black",fg="White")
        b4.place(x=850,y=200,width=150,height=50)

#train button

        img9=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\5.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_image,image=self.photoimg9)
        b5.place(x=250,y=300,width=150,height=150)
        

        b5=Button(bg_image,text= "Train Data",font=("times new roman",15,"bold"),bg="black",fg="White")
        b5.place(x=250,y=450,width=150,height=50)
        

#photos button

        img10=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\6.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_image,image=self.photoimg10)
        b6.place(x=450,y=300,width=150,height=150)
        

        b6=Button(bg_image,text= "Photos",font=("times new roman",15,"bold"),bg="black",fg="White")
        b6.place(x=450,y=450,width=150,height=50)

#developer button
        img11=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\7.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_image,image=self.photoimg11)
        b7.place(x=650,y=300,width=150,height=150)
        

        b7=Button(bg_image,text= "Developer",font=("times new roman",15,"bold"),bg="black",fg="White")
        b7.place(x=650,y=450,width=150,height=50)


#exit button
        img12=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\8.jpg")
        img12=img12.resize((150,150),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8=Button(bg_image,image=self.photoimg12)
        b8.place(x=850,y=300,width=150,height=150)
        
        b8=Button(bg_image,text= "Exit",font=("times new roman",15,"bold"),bg="black",fg="White")
        b8.place(x=850,y=450,width=150,height=50)


if __name__ == "__main__":
    root=Tk()
    obj= Face_recognitation_system(root)
    root.mainloop()

