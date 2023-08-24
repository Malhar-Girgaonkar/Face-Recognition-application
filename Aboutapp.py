from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 825,500


class MyFrameinfo(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets onto the frame...
        self.info="""                        What does this app do?
                        -This application is used to detect face in image,video,web camera feed


                     What Technologies are used?
                        -CustomTkinter for Gui
                        -OpenCV library for computer vision
                        -DBMS for user data storage
                        -Python as programing language
                        -Harcascade algorithm for AI detection


                     What facilities does this application provide?
                        -User Registration and Login service
                        -Face Detection facalities
                        -Recording user and their activity in app
                        -Interractive and modern looking GUI


                     About Developer
                        -This application was developed by Malhar Girgaonkar from MREC,
                         2-2 semister in year 2023 as a project """
        self.label = ctk.CTkLabel(self,text=self.info,anchor="w",font=("arial",15,"italic"))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky="nsew")
        



class aboutappapp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("About App")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(True,True)

        self.header = ctk.CTkLabel(self,text="About Application",anchor="center",font=("Helvetiva",30,"bold"))
        self.header.grid(row=0,columnspan=1, column=0, padx=15,pady=15,sticky="nsew")
        self.header._set_dimensions(width=800,height=100)

        self.info_frame=MyFrameinfo(master=self)
        self.info_frame.grid(row=1,columnspan=1, column=0, padx=15,pady=15,sticky="nsew")
        self.info_frame._set_dimensions(width=400,height=300)


        
        


        
    
    
        
                        
                                        
                                        

                                         

if __name__=="__main__":
    aboutapp_app=aboutappapp()
    aboutapp_app.mainloop()