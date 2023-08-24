from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from customtkinter import filedialog
import tkinter as tk
import subprocess
import cv2
import os
import shutil


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 402,477

class MyFrameimgrecog(ctk.CTkFrame):
    def selectimg(self):
        #get image location
        self.img_destination_path="app data/images"
        self.img_source_path=filedialog.askopenfilename(initialdir="D:",title="Select Image",filetypes=(("All files","*.*"),("PNG files","*.png"),("JPG files","*.jpg"),("JPEG files","*.jpeg")))
        #if image source= image destination then img_path=imgsource
        if(self.img_source_path!=os.path.join(self.img_destination_path, os.path.basename(self.img_source_path))):
            #move image to location D:/CS Project/Projects/AI projects/2-2 project/app data/images
            self.img_path=shutil.copy(self.img_source_path, self.img_destination_path)
            
        else:
            self.img_path=self.img_source_path
        # Update the label text with the new img_path
        self.imgpathlabel.configure(text=self.img_path)

    def clean(self):
        #delete all images in folder D:\CS Project\Projects\AI projects\2-2 project\app data\images
        # Iterate over all the files in the directory
        self.directory_path="app data\images"
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            try:
                if os.path.isfile(file_path):
                    # Delete the file
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
            
    def facerecognition(self):
        #create face descriptor using harcascade algorithm
        self.fd=cv2.CascadeClassifier('app data\Dependencies\haarcascade_frontalface_default.xml')
        #load image with given path
        self.image_location=self.img_path
        self.img=cv2.imread(self.image_location)
        #convert to gray scale
        self.grey_img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        #detect multiple faces in image
        fd_xy=self.fd.detectMultiScale(self.grey_img)
        #Iterate through original image to mark bounding box
        for(x,y,w,h) in fd_xy:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),(0,255,0),2)
        #show output image with bounded faces
        cv2.imshow("Image",self.img)
        cv2.waitKey()

    def redirectmain(self):
        self.master.withdraw()
        subprocess.run(["Python","Mainpage.py"])
        self.response.destroy()
        self.master.destroy()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_path=""
        #label to select image
        self.infolabel = ctk.CTkLabel(self,text="Select image:",anchor="center",font=("arial",15,"italic"))
        self.infolabel.grid(row=0, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button for Redirect to select file
        self.buttonimg=ctk.CTkButton(self,text="Image",command=self.selectimg)
        self.buttonimg.grid(row=1, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to show file path considered
        self.imgpathlabel = ctk.CTkLabel(self,text=self.img_path,anchor="center",font=("arial",10,"italic"))
        self.imgpathlabel.grid(row=2, column=0,columnspan=1,rowspan=2,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.buttonfrstart=ctk.CTkButton(self,text="Deteect Faces",command=self.facerecognition)
        self.buttonfrstart.grid(row=4, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to clear image load in application folder
        self.clearimglabel = ctk.CTkLabel(self,text="Clean loaded images",anchor="center",font=("arial",18,"italic"))
        self.clearimglabel.grid(row=5, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.cleanimages=ctk.CTkButton(self,text="clean",command=self.clean)
        self.cleanimages.grid(row=5, column=1,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to go back to Mainpage.py
        self.mainlabel = ctk.CTkLabel(self,text="next",anchor="center",font=("arial",18,"italic"))
        self.mainlabel.grid(row=6, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to go to Mainpage.py
        self.buttonmain=ctk.CTkButton(self,text="Main Page",command=self.redirectmain)
        self.buttonmain.grid(row=6, column=1,columnspan=1,padx=20, pady=20,sticky="ew")







class ImgFRapp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Image Face Recognition")
        
        # Calculate the coordinates for centering the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - appWidth) // 2
        y_position = (screen_height - appHeight) // 2
        # Set the geometry of the window to open it at the center
        self.geometry(f"{appWidth}x{appHeight}+{x_position}+{y_position}")
        self.resizable(True, True)
        self.attributes('-topmost', True)
        #label for header
        self.header=ctk.CTkLabel(self,text="Image Based Face Recognition",font=("Helvetiva",25,"italic"),anchor="center")
        self.header.grid(row=0,column=0, padx=10, pady=10, sticky="nsew")
        #frame for face recognition
        self.imgrecog_frame = MyFrameimgrecog(master=self)
        self.imgrecog_frame.grid(row=1, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")
        self.imgrecog_frame._set_dimensions(width=300,height=300)





if __name__=="__main__":
    ImgFR_app=ImgFRapp()
    ImgFR_app.mainloop()