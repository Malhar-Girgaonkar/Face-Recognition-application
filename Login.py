from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk
import mysql.connector
import subprocess
import sqlite3




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 400,300

class MyFrameLogin(ctk.CTkFrame):

    def authenticate(self):
        db=sqlite3.connect("userinfo.db")
        mycursor=db.cursor()
        querry = "SELECT COUNT(*) FROM userlogin WHERE username = ? AND password = ?"
        values = (self.username,self.password)
        mycursor.execute(querry, values)
        result = mycursor.fetchone()
        if result[0] > 0:
            # Username and password combination exists in the table
            self.response=CTkMessagebox(self,title="Log In",message="Login Successfull",icon="check",option_1="Next")
            if self.response.get()=="Next":
                #go to Mainpage.py
                self.master.withdraw()
                subprocess.run(["Python","Mainpage.py"])
                self.response.destroy()
                self.master.destroy()
        else:
            # Username and password combination doesn't exist in the table
            self.msg3=CTkMessagebox(self,title="Error",message="Login Unsuccessfull",icon="cancel",option_1="Retry",option_2="Cancel")
            if self.msg3.get()=="Retry":
                #go to Home.py
                self.msg3.destroy()
            elif self.msg3.get()=="Cancel":
                self.msg3.destroy()
                login_app.destroy()
        db.close()

    def verify(self):
        self.password=self.epwd.get()
        self.username=self.uename.get()
        self.response=CTkMessagebox(title="login status",icon="check",message=f"\nusername:"+self.username+f"\npassword:"+self.password,option_1="No",option_2="Yes")
        if self.response.get()=="Yes":
            self.authenticate()
            self.response.destroy()
        elif self.response.get()=="No":
            self.response.destroy()

    def redirect(self):
        subprocess.run(["Python","Registration.py"])

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #label1 for username
        self.uname=ctk.CTkLabel(self, text="Username:",font=("arial",25,"italic"))
        self.uname.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
        #entry field for username
        self.uename=ctk.CTkEntry(self,placeholder_text="Username",font=("Arial",20,"italic"))
        self.uename.grid(row=0,column=2,padx=20,pady=20,columnspan=3,sticky="ew")
        #label2 for password
        self.pwd=ctk.CTkLabel(self, text="Password:",font=("arial",25,"italic"))
        self.pwd.grid(row=1,column=0,padx=20,pady=20,sticky="ew")
        #entry field for password
        self.epwd=ctk.CTkEntry(self,placeholder_text="Password",show="*",font=("Arial",20,"italic"))
        self.epwd.grid(row=1,column=2,padx=20,pady=20,columnspan=3,sticky="ew")
        #label2 for Registration if not registered
        self.reg=ctk.CTkLabel(self, text="First time?",font=("arial",15,"italic"))
        self.reg.grid(row=2,column=0,padx=20,pady=20,sticky="ew")
        #button for Redirect to registration
        self.breg=ctk.CTkButton(self,text="Register",command=self.redirect)
        self.breg.grid(row=2, column=1,columnspan=2,padx=20, pady=20,sticky="ew")
        #button for submission
        self.submit=ctk.CTkButton(self,text="Submit",command=self.verify)
        self.submit.grid(row=3, column=1,columnspan=2,padx=20, pady=20,sticky="ew")



class loginapp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("login")
        
        # Calculate the coordinates for centering the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - appWidth) // 2
        y_position = (screen_height - appHeight) // 2

        # Set the geometry of the window to open it at the center
        self.geometry(f"{appWidth}x{appHeight}+{x_position}+{y_position}")
        self.resizable(True, True)
        self.attributes('-topmost', True)

        #frame login related setting on page
        self.login_frame = MyFrameLogin(master=self)
        self.login_frame.grid(row=1, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")



if __name__=="__main__":
    login_app=loginapp()
    login_app.mainloop()