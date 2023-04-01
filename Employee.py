from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("face recognization system")


       #first_image
        img=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\ems.jpg")
        img=img.resize((1300,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)


        #bg image
        img4=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\ash color.jpg")
        img4=img4.resize((1300,620),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=130,width=1300,height=620)


        

        main_frame=Frame(bg_image ,bd=2, bg="white")
        main_frame.place(x=50,y=20,width=1200,height=580)


        #left label frame
         
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"), bg="pink")
        Left_frame.place(x=60,y=10,width=500,height=480)

        #left frame img
        img_left=Image.open(r"C:\Users\EIT\afrin\employee_mngemnt\photos\left_fr.png")
        img_left=img_left.resize((500,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=5,width=500,height=100)

        #current course
        current_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current information",font=("times new roman",12,"bold"), bg="pink")
        current_frame.place(x=0,y=110,width=495,height=100)

         #department combobox
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"), bg="coral")
        dep_label.grid(row=0,column=0)
        dep_combo=ttk.Combobox(current_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo['values']=("Select Department","HR","Robotics","preservation","Accounts","Graphics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=1,pady=5)




         
        
         
       




         #Right label frame
         
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"),bg="pink")
        Right_frame.place(x=580,y=10,width=500,height=480)
    
    










if __name__ == "__main__":
    root=Tk()
    obj= Employee(root)
    root.mainloop()

