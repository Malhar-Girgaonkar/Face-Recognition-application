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
appWidth, appHeight = 380,475

class MyFramevidrecog(ctk.CTkFrame):

    def redirectmain(self):
        self.master.withdraw()
        #finding current script directory
        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        # Construct the relative path to Mainpage.py
        mainpage_path = os.path.join(current_script_directory, "Mainpage.py")
        subprocess.run(["Python",mainpage_path])
        self.master.destroy()

    def selectvid(self):
        #get video location
        self.vid_destination_path="app data/videos"
        self.vid_source_path=filedialog.askopenfilename(initialdir="D:",title="Select Vidoes",filetypes=(("All files","*.*"),("MP4 files","*.mp4"),("MKV files","*.mkv"),("MOV files","*.mov")))
        #if video source= video destination then vid_path=imgsource
        if(self.vid_source_path!=os.path.join(self.vid_destination_path, os.path.basename(self.vid_source_path))):
            #move video to location D:/CS Project/Projects/AI projects/2-2 project/app data/videos
            self.vid_path=shutil.copy(self.vid_source_path, self.vid_destination_path)
            
        else:
            self.vid_path=self.vid_source_path
        # Update the label text with the new img_path
        self.vidpathlabel.configure(text=self.vid_path)

    def clean(self):
        #delete all videos in folder D:\CS Project\Projects\AI projects\2-2 project\app data\videos
        # Iterate over all the files in the directory
        self.directory_path="app data\\videos"
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            try:
                if os.path.isfile(file_path):
                    # Delete the file
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
            
    def facerecognition(self):
        #create face descriptor using harrcascade algorithm
        self.fd=cv2.CascadeClassifier('app data\Dependencies\haarcascade_frontalface_default.xml')
        #load video with given path here img is a single fram eof video
        self.video_location=self.vid_path
        cam=cv2.VideoCapture(self.video_location)
        while True:
            bool,frame=cam.read()
            if(bool==True):
                print("Frame loaded")
            self.grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            self.cam_xy=self.fd.detectMultiScale(self.grey_frame)
            for(x,y,w,h) in self.cam_xy:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                print("face coordinates:",self.cam_xy)
            cv2.imshow("Video",frame)
            key=cv2.waitKey(1)
            if key==113 or key==81:
                break


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vid_path=""
        #label to select video
        self.infolabel = ctk.CTkLabel(self,text="Select video:",anchor="center",font=("arial",15,"italic"))
        self.infolabel.grid(row=0, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button for Redirect to select file
        self.buttonvid=ctk.CTkButton(self,text="Video",command=self.selectvid)
        self.buttonvid.grid(row=1, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to show file path considered
        self.vidpathlabel = ctk.CTkLabel(self,text=self.vid_path,anchor="center",font=("arial",10,"italic"))
        self.vidpathlabel.grid(row=2, column=0,columnspan=1,rowspan=2,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.buttonfrstart=ctk.CTkButton(self,text="Deteect Faces",command=self.facerecognition)
        self.buttonfrstart.grid(row=4, column=0,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to clear video load in application folder
        self.clearvidlabel = ctk.CTkLabel(self,text="Clean loaded videos",anchor="center",font=("arial",14,"italic"))
        self.clearvidlabel.grid(row=5, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.cleanvideos=ctk.CTkButton(self,text="clean",command=self.clean)
        self.cleanvideos.grid(row=5, column=1,columnspan=1,padx=20, pady=20,sticky="ew")
        #label to go back to Mainpage.py
        self.mainlabel = ctk.CTkLabel(self,text="next",anchor="center",font=("arial",18,"italic"))
        self.mainlabel.grid(row=6, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #button to start face detection
        self.buttonmain=ctk.CTkButton(self,text="Main Page",command=self.redirectmain)
        self.buttonmain.grid(row=6, column=1,columnspan=1,padx=20, pady=20,sticky="ew")

class VidFRapp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Video Face Recognition")
        
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
        self.header=ctk.CTkLabel(self,text="Video Based Face Recognition",font=("Helvetiva",25,"italic"),anchor="center")
        self.header.grid(row=0,column=0, padx=10, pady=10, sticky="nsew")
        #frame for face recognition
        self.vidrecog_frame = MyFramevidrecog(master=self)
        self.vidrecog_frame.grid(row=1, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")
        self.vidrecog_frame._set_dimensions(width=400,height=300)




if __name__=="__main__":
    VidFR_app=VidFRapp()
    VidFR_app.mainloop()