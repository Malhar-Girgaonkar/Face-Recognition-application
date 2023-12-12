from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk
import subprocess
import cv2
import os



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 443,270

class MyFrameWCrecog(ctk.CTkFrame):
    def redirectmain(self):
        self.master.withdraw()
        #finding current script directory
        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        # Construct the relative path to Mainpage.py
        mainpage_path = os.path.join(current_script_directory, "Mainpage.py")
        subprocess.run(["Python",mainpage_path])
        self.master.destroy()

    def facerecognition(self):
        #create face descriptor using harcascade algorithm
        self.fd=cv2.CascadeClassifier('app data\Dependencies\haarcascade_frontalface_default.xml')
        #use videoCapture(0) where 0 specifies webcamera input
        self.cam=cv2.VideoCapture(0)
        #iterate through frames in self.cam
        while True:
            bool,frame=self.cam.read()
            if(bool!=True):
                #show unable to load frame messagebox
                CTkMessagebox(title="Error", message="Unable to load frames",icon="error", option_1="Yes")
            self.grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            self.cam_xy=self.fd.detectMultiScale(self.grey_frame)
            for(x,y,w,h) in self.cam_xy:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                print("face coordinates:",self.cam_xy)
            #Show frame with bounding box
            cv2.imshow("Webcam",frame)
            #wait for entering key Q or q to exit webcam
            key=cv2.waitKey(1)
            if key==113 or key==81:
                break
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #label webcam details
        self.infolabel = ctk.CTkLabel(self,text="Use Webcam for detection:",anchor="center",font=("arial",18,"italic"))
        self.infolabel.grid(row=0, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.buttonfrstart=ctk.CTkButton(self,text="Deteect Faces",command=self.facerecognition)
        self.buttonfrstart.grid(row=1, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to go back to Mainpage.py
        self.mainlabel = ctk.CTkLabel(self,text="next",anchor="center",font=("arial",18,"italic"))
        self.mainlabel.grid(row=2, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to go back to Mainpage.py
        self.buttonmain=ctk.CTkButton(self,text="Main Page",command=self.redirectmain)
        self.buttonmain.grid(row=2, column=1,columnspan=1,padx=20, pady=20,sticky="ew")

class WCFRapp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Webcam Face Recognition")
        
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
        self.header=ctk.CTkLabel(self,text="Webcam Based Face Recognition",font=("Helvetiva",25,"italic"),anchor="center")
        self.header.grid(row=0,column=0, padx=10, pady=10, sticky="nsew")
        #frame for face recognition
        self.WCrecog_frame = MyFrameWCrecog(master=self)
        self.WCrecog_frame.grid(row=1, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")
        self.WCrecog_frame._set_dimensions(width=300,height=300)





if __name__=="__main__":
    WCFR_app=WCFRapp()
    WCFR_app.mainloop()