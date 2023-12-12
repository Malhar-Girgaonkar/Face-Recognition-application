from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk
from PIL import Image,ImageTk
import subprocess
import os




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 562,405

class Mybuttonframe(ctk.CTkFrame):
    def redirectimg(self):
        self.master.withdraw()
        #finding current script directory
        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        # Construct the relative path to Mainpage.py
        image_face_recognition_path = os.path.join(current_script_directory, "ImageFaceRecognition.py")
        subprocess.run(["Python",image_face_recognition_path])
        self.master.destroy()

    def redirectvid(self):
        self.master.withdraw()
        #finding current script directory
        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        # Construct the relative path to Mainpage.py
        Video_face_recognition_path = os.path.join(current_script_directory, "VideoFaceRecognition.py")
        subprocess.run(["Python",Video_face_recognition_path])
        self.master.destroy()

    def redirectwc(self):
        self.master.withdraw()
        #finding current script directory
        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        # Construct the relative path to Mainpage.py
        webcam_face_recognition_path = os.path.join(current_script_directory, "WebcamFaceRecognition.py")
        subprocess.run(["Python",webcam_face_recognition_path])
        self.master.destroy()


    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #button for Redirect to image face recognition
        self.buttonimg=ctk.CTkButton(self,text="Image",command=self.redirectimg)
        self.buttonimg.grid(row=0, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #button for Redirect to video face recognition
        self.buttonvid=ctk.CTkButton(self,text="video",command=self.redirectvid)
        self.buttonvid.grid(row=0, column=1,columnspan=1,padx=20, pady=20,sticky="ew")
        #button for Redirect to webccam face recognition
        self.buttonwc=ctk.CTkButton(self,text="Webcam",command=self.redirectwc)
        self.buttonwc.grid(row=0, column=2,columnspan=1,padx=20, pady=20,sticky="ew")
        #button to close application
        self.buttonclose=ctk.CTkButton(self,text="close",command=self.master.destroy)
        self.buttonclose.grid(row=1, column=1,columnspan=1,padx=20, pady=20,sticky="ew")


class Mainpageapp(ctk.CTk):
    def optionmenu_callback(self,choice):
        if choice=="Registration":
            #open Registration.py
            #finding current script directory
            current_script_directory = os.path.dirname(os.path.realpath(__file__))
            # Construct the relative path to Mainpage.py
            registration_path = os.path.join(current_script_directory, "Registration.py")
            subprocess.run(["Python",registration_path])
        elif choice=="Login":
            #OPEN login.py
            #finding current script directory
            current_script_directory = os.path.dirname(os.path.realpath(__file__))
            # Construct the relative path to Mainpage.py
            login_path = os.path.join(current_script_directory, "Login.py")
            subprocess.run(["Python",login_path])
        elif choice=="About App":
            #open Aboutapp.py
            #finding current script directory
            current_script_directory = os.path.dirname(os.path.realpath(__file__))
            # Construct the relative path to Aboutapp.py
            Aboutpage_path = os.path.join(current_script_directory, "Aboutapp.py")
            subprocess.run(["Python",Aboutpage_path])


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Main Page")

        # Calculate the coordinates for centering the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - appWidth) // 2
        y_position = (screen_height - appHeight) // 2

        # Set the geometry of the window to open it at the center
        self.geometry(f"{appWidth}x{appHeight}+{x_position}+{y_position}")
        self.resizable(True, True)
        self.attributes('-topmost', True)
        self.resizable(True, True)

        #Option Menu
        optionmenu_var = ctk.StringVar(value="Options")
        optionmenu = ctk.CTkOptionMenu(self, values=["Registration","Login","About App"],variable=optionmenu_var,command=self.optionmenu_callback)
        optionmenu.grid(row=0,rowspan=1,column=0, columnspan=3, padx=10,pady=10,sticky="nsew")
        optionmenu._set_dimensions(width=150,height=25)
        optionmenu.configure(dropdown_font=("arial",14),dynamic_resizing=True)

        #label for options
        self.info="""Welcome to my Project for face Recogniton
        \nYou have following options
        \n1) Face Recogniton via Image
        \n2)Face Recognition via Video
        \n3)Face Recognition via webcam"""
        self.infolabel = ctk.CTkLabel(self,text=self.info,anchor="center",font=("arial",15,"italic"))
        self.infolabel.grid(row=1, column=0,columnspan=3,rowspan=3,padx=20,pady=20,sticky="nsew")
        #placing frame buttons
        self.buttonframe =Mybuttonframe(master=self)
        self.buttonframe.grid(row=4, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")
        self.buttonframe._set_dimensions(width=100,height=500)




if __name__=="__main__":
    mainpage_app=Mainpageapp()
    mainpage_app.mainloop()