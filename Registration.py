from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk
import re
import mysql.connector
import subprocess
import sqlite3



global_username=""
#Application configurations
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 1450,750



def submit_login_details(username,password):
    global global_username
    global_username=username
    try:
        # Establish a connection to the database
        connection =  sqlite3.connect("userinfo.db")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        # Define the INSERT query
        insert_query = "INSERT INTO userlogin (username, password) VALUES (?,?)"

        # Execute the query with the provided values
        cursor.execute(insert_query, (username, password))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display a success message or perform any additional actions
        msg1=CTkMessagebox(title="Success", message="Login details submitted succesfully",icon="check", option_1="Ok")
        if msg1.get()=="Ok":
            msg1.destroy()


    except sqlite3.Error as error:
        # Handle any errors that occur during the process
        msg2=CTkMessagebox(title="Error", message=error,icon="cancel", option_1="Ok")
        if msg2.get()=="Ok":
            msg2.destroy()


def submit_contact_details(email,mobileno,icc):
    try:
        # Establish a connection to the database
        connection =  sqlite3.connect("userinfo.db")
        username=global_username
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the INSERT query
        insert_query = "INSERT INTO usercontact (username,email, icc,mobileno ) VALUES (?,?,?,?)"

        # Execute the query with the provided values
        cursor.execute(insert_query, (username,email, icc,mobileno ))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display a success message or perform any additional actions
        msg1=CTkMessagebox(title="Success", message="Contact details submitted succesfully",icon="check", option_1="Ok")
        if msg1.get()=="Ok":
            msg1.destroy()


    except sqlite3.Error as error:
        print(error)
        # Handle any errors that occur during the process
        msg2=CTkMessagebox(title="Error", message=f"Submission Unsuccesfully",icon="cancel", option_1="Ok")
        if msg2.get()=="Ok":
            msg2.destroy()


def submit_personal_details(firstname,lastname,gender,dateofbirth,country,state,city):
    try:
        # Establish a connection to the database
        connection =  sqlite3.connect("userinfo.db")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        username=str(global_username)
        # Define the INSERT query
        insert_query = "INSERT INTO userpersonal(username,firstname,lastname,gender,dateofbirth,country,state,city) VALUES (?, ?, ?, ?, ?, ?, ?,?)"

        # Execute the query with the provided values
        cursor.execute(insert_query, (username,firstname,lastname,gender,dateofbirth,country,state,city))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display a success message or perform any additional actions
        msg1=CTkMessagebox(title="Success", message="Personal details submitted succesfully",icon="check", option_1="Ok")
        if msg1.get()=="Ok":
            msg1.destroy()


    except sqlite3.Error as error:
        # Handle any errors that occur during the process
        print(error)
        msg2=CTkMessagebox(title="Error", message=f"Submission Unsuccesfully",icon="cancel", option_1="Ok")
        if msg2.get()=="Ok":
            msg2.destroy()
    

def submit_tandc_details(tandc_status):
    try:
        # Establish a connection to the database
        connection =  sqlite3.connect("userinfo.db")
        username=global_username
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the UPDATE query
        update_query = "UPDATE usercontact SET tandc_status=? WHERE username=?"

        # Execute the query with the provided values
        cursor.execute(update_query, (tandc_status,username))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display a success message or perform any additional actions
        msg1=CTkMessagebox(title="Success", message="Terms and condition details submitted succesfully",icon="check", option_1="Ok")
        if msg1.get()=="Ok":
            msg1.destroy()

    except sqlite3.Error as error:
        # Handle any errors that occur during the process
        msg2=CTkMessagebox(title="Error", message=f"Submission Unsuccesfully",icon="cancel", option_1="Ok")
        if msg2.get()=="Ok":
            msg2.destroy()



class MyFramelogin(ctk.CTkFrame):
    

    def lsubmit(self):
        global global_username
        global_username=self.ruename.get()
        self.password=self.repwd.get()
        self.username=self.ruename.get()
        self.textptompt=f"Login Details\nUsername:\n"+self.username+f"\npassword:\n"+self.password+f"\nConfirm details"
        self.msg = CTkMessagebox(title="Confirm", message=self.textptompt,icon="question", option_1="No",option_2="Yes")
        if self.msg.get()=="Yes":
            #submit Login details to DBMS
            submit_login_details(self.username, self.password)
            self.msg.destroy()
            
        elif self.msg.get()=="No":
            self.msg.destroy()
    
    def validate_password(self,event):
        password = self.repwd.get()
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=(.*[@$!%*?&]){0,1})[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern, password):
            return True
        else:
            error_label = ctk.CTkLabel(self, text=f"Password must be at least 8 characters long,\ncontain both uppercase and lowercase letters,\nand have at most 1 special character.", font=("Arial", 12,"bold"), text_color="red")
            error_label.grid(row=3,column=1, rowspan=2,columnspan=1, padx=10, pady=5, sticky="w")
            self.after(5000, error_label.destroy)
            self.repwd.delete(0, tk.END)  # Clear the password entry field
            self.repwd.focus_set()
            return False
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        

        #Label for login detail display
        self.label = ctk.CTkLabel(self,text="Login Details",font=("arial",15,"italic"))
        self.label.grid(row=0, column=0,columnspan=2, padx=20,pady=20,sticky="nswe")

        #label1 for username
        self.runame=ctk.CTkLabel(self, text="Username:",font=("arial",25,"italic"))
        self.runame.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for username
        self.ruename=ctk.CTkEntry(self,placeholder_text="Username",font=("Arial",20,"italic"))
        self.ruename.grid(row=1,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        #label2 for password
        self.rpwd=ctk.CTkLabel(self, text="Password:",font=("arial",25,"italic"))
        self.rpwd.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for password
        self.repwd=ctk.CTkEntry(self,placeholder_text="Password",show="*",font=("Arial",20,"italic"))
        self.repwd.grid(row=2,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        self.repwd.bind("<Return>", self.validate_password)  # Bind validation to FocusOut event
        #label2 for password conditions
        self.condition=f"Password must be atleast 8 characters,\ncontain both upper and lower case,\nmust have 1 special symbol"
        self.conpwd=ctk.CTkLabel(self, text=self.condition,font=("arial",15,"italic"),justify=tk.LEFT)
        self.conpwd.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
        #button for submission login frame
        self.submit=ctk.CTkButton(self,text="Submit",command=self.lsubmit)
        self.submit.grid(row=4, column=0,columnspan=1,padx=20, pady=20,sticky="nsew")

class MyFramecontact(ctk.CTkFrame):
    def csubmit(self):
        self.email=self.rueemail.get()
        self.mobile_no=self.remno.get()
        self.icc=str(self.ccd_var.get())
        
        self.textptompt=f"Contact Details\nEmail:\n"+self.email+f"\nMobile No:\n"+self.mobile_no+f"\nConfirm details"
        self.msg = CTkMessagebox(title="Confirm", message=self.textptompt,icon="question", option_1="Yes")
        if self.msg.get()=="Yes":
            #submit contact details to DBMS
            submit_contact_details(self.email,self.mobile_no,self.icc)
            self.msg.destroy()

        
    def validate_email(self,event):
        self.email= self.rueemail.get()
        pattern=r"^[a-z][a-z0-9]*@(?:gmail|rediffmail|outlook|hotmail)\.com$"
        if re.match(pattern, self.email):
            return True
        else:
            error_label = ctk.CTkLabel(self, text=f"Invalid Email", font=("Arial", 12,"bold"), text_color="red")
            error_label.grid(row=4,column=1, padx=10, pady=5, sticky="w")
            self.after(5000, error_label.destroy)
            self.rueemail.delete(0, tk.END)  # Clear the password entry field
            self.rueemail.focus_set()
            return False

    def validate_mobileno(self,event):
        self.mobileno= self.remno.get()
        pattern=r"^\d{10}$"
        if re.match(pattern, self.mobileno):
            return True
        else:
            error_label = ctk.CTkLabel(self, text=f"Invalid Mobile No.", font=("Arial", 12,"bold"), text_color="red")
            error_label.grid(row=4,column=1,padx=10, pady=5, sticky="w")
            self.after(5000, error_label.destroy)
            self.remno.delete(0, tk.END)  # Clear the password entry field
            self.remno.focus_set()
            return False
    def ccd_callback(self):
        #call back for country code
        pass

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # header for frame:
        self.label = ctk.CTkLabel(self,text="Contact Details",font=("arial",15,"italic"))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky="nswe")

        #label1 for email
        self.ruemail=ctk.CTkLabel(self, text="Email:",font=("arial",25,"italic"))
        self.ruemail.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for email
        self.rueemail=ctk.CTkEntry(self,placeholder_text="xxxxx@gmail.com",font=("Arial",20,"italic"))
        self.rueemail.grid(row=1,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        self.rueemail.bind("<Return>", self.validate_email)  # Bind validation to FocusOut event
        #label for ccd
        self.ccdl=ctk.CTkLabel(self, text="ICC:",font=("arial",25,"italic"))
        self.ccdl.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
        #combobox for seleting country calling code ccd
        self.ccd_var=ctk.StringVar(value=0)
        self.ccd = ctk.CTkComboBox(self, values=["+91","+1","+44","+81"], variable=self.ccd_var)
        self.ccd.grid(row=2 ,column=1,padx=10 ,pady=10 ,sticky="nsew")
        self.ccd.bind("<<ComboboxSelected>>", self.ccd_callback)


        #label2 for mobile no
        self.rmno=ctk.CTkLabel(self, text="Mobile No:",font=("arial",25,"italic"))
        self.rmno.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for mobile no.
        self.remno=ctk.CTkEntry(self,placeholder_text="Mobile No.",font=("Arial",20,"italic"))
        self.remno.grid(row=3,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        self.remno.bind("<Return>", self.validate_mobileno)  # Bind validation to FocusOut event
        #button for submission Contact frame
        self.submit=ctk.CTkButton(self,text="Submit",command=self.csubmit)
        self.submit.grid(row=4, column=0,columnspan=1,padx=20, pady=20,sticky="nsew")

class MyFramepersonal(ctk.CTkFrame):
    def psubmit(self):
        self.firstname=self.refname.get()
        self.lastname=self.relname.get()
        self.gender=self.rgender.get()
        self.dateofbirth=(self.red.get()+"/"+self.rem.get()+"/"+self.rey.get())
        self.country=self.rec.get()
        self.state=self.res.get()
        self.city=self.recity.get()

        self.textptompt=f"\nConfirm submission"
        self.msg = CTkMessagebox(title="Confirm", message=self.textptompt,icon="question", option_1="Yes")

        if self.msg.get()=="Yes":
            #submit personal details to DBMS
            submit_personal_details(self.firstname,self.lastname,self.gender,self.dateofbirth,self.country,self.state,self.city)
            self.msg.destroy()
        



    def rgender_callback(self):
        #gender callback function
        pass


    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self,text="Personal Details",font=("arial",15,"italic"))
        self.label.grid(row=0, column=0,columnspan=4, padx=20,pady=20,sticky="nswe")

        #label1 for First name
        self.rfname=ctk.CTkLabel(self, text="First name:",font=("arial",25,"italic"))
        self.rfname.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for first name
        self.refname=ctk.CTkEntry(self,placeholder_text="----",font=("Arial",20,"italic"))
        self.refname.grid(row=1,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        #label1 for Last  name
        self.rlname=ctk.CTkLabel(self, text="Last name:",font=("arial",25,"italic"))
        self.rlname.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
        #entry field for last name
        self.relname=ctk.CTkEntry(self,placeholder_text="----",font=("Arial",20,"italic"))
        self.relname.grid(row=2,column=1,padx=10,pady=10,columnspan=3,sticky="nsew")
        #label for Gender
        self.ccdl=ctk.CTkLabel(self, text="Gender:",font=("arial",25,"italic"))
        self.ccdl.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
        #combobox for Gender
        self.rgender_var=ctk.StringVar(value="Null")
        self.rgender = ctk.CTkComboBox(self, values=["Male","Female","Transgender","Others"], variable=self.rgender_var)
        self.rgender.grid(row=3 ,column=1,padx=10 ,pady=10 ,sticky="nsew")
        self.rgender.bind("<<ComboboxSelected>>", self.rgender_callback)
        #label for date of birth
        self.rdob=ctk.CTkLabel(self,text="Date Of Birth:",font=("arial",25,"italic"))
        self.rdob.grid(row=1,column=3,columnspan=2,padx=10,pady=10,sticky="nsew")
        #date
        self.rd=ctk.CTkLabel(self,text="Date:",font=("arial",25,"italic"))
        self.rd.grid(row=2,column=3,padx=10,pady=10,sticky="nsew")
        #date entry
        self.red=ctk.CTkEntry(self,placeholder_text="1 to 31",font=("Arial",20,"italic"))
        self.red.grid(row=2,column=4,padx=10,pady=10,sticky="nsew")
        #month
        self.rm=ctk.CTkLabel(self,text="Month:",font=("arial",25,"italic"))
        self.rm.grid(row=3,column=3,padx=10,pady=10,sticky="nsew")
        #month entry
        self.rem=ctk.CTkEntry(self,placeholder_text="1 to 12",font=("Arial",20,"italic"))
        self.rem.grid(row=3,column=4,padx=10,pady=10,sticky="nsew")
        #year
        self.ry=ctk.CTkLabel(self,text="Year:",font=("arial",25,"italic"))
        self.ry.grid(row=4,column=3,padx=10,pady=10,sticky="nsew")
        #year entry
        self.rey=ctk.CTkEntry(self,placeholder_text="1950 to current",font=("Arial",20,"italic"))
        self.rey.grid(row=4,column=4,padx=10,pady=10,sticky="nsew")
        #Country
        self.rc=ctk.CTkLabel(self,text="Country:",font=("arial",25,"italic"))
        self.rc.grid(row=5,column=0,padx=10,pady=10,sticky="nsew")
        #country entry
        self.rec=ctk.CTkEntry(self,placeholder_text="----",font=("Arial",20,"italic"))
        self.rec.grid(row=5,column=1,padx=10,pady=10,sticky="nsew")
        #state
        self.rs=ctk.CTkLabel(self,text="State:",font=("arial",25,"italic"))
        self.rs.grid(row=5,column=3,padx=10,pady=10,sticky="nsew")
        #state entry
        self.res=ctk.CTkEntry(self,placeholder_text="----",font=("Arial",20,"italic"))
        self.res.grid(row=5,column=4,padx=10,pady=10,sticky="nsew")
        #city
        self.rcity=ctk.CTkLabel(self,text="City:",font=("arial",25,"italic"))
        self.rcity.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")
        #city entry
        self.recity=ctk.CTkEntry(self,placeholder_text="----",font=("Arial",20,"italic"))
        self.recity.grid(row=6,column=1,padx=10,pady=10,sticky="nsew")
        #buttion for personal frame
        self.submit=ctk.CTkButton(self,text="Submit",command=self.psubmit)
        self.submit.grid(row=7, column=0,columnspan=1,padx=20, pady=20,sticky="nsew")

class MyFrametandc(ctk.CTkFrame):
    def tandc_agree(self):
        #tandc_agree function
        pass
    
    
    def tsubmit(self):
        self.tandc_status=self.tandca.get()
        print(type(self.tandc_status))
        #submit Tandc AGREEMENT STATUS TO dbms
        submit_tandc_details(self.tandc_status)
        Registration_app.destroy()

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.text=f"Your Details will be recorded for future login purposes.\nPlease remember your password and username details\nclick the checkbox to agree with our terms and conditions"
        self.tandc=ctk.CTkLabel(self,text=self.text,font=("Helvetiva",20,"italic"))
        self.tandc.grid(row=0,column=0,columnspan=1,padx=10,pady=10,sticky="nswe")
        self.check_var = ctk.StringVar(value="off")
        self.tandca= ctk.CTkCheckBox(self, text="I agree with the above Tems and Conditions",variable=self.check_var, onvalue="on", offvalue="off")
        self.tandca.grid(row=1,column=0,columnspan=1,padx=10,pady=10,sticky="nswe")
        #buttion for tandc frame
        self.submit=ctk.CTkButton(self,text="Submit",command=self.tsubmit)
        self.submit.grid(row=7, column=0,columnspan=1,padx=20, pady=20,sticky="nsew")





class Registrationapp(ctk.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Registration")

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

        #header for "Registration Details"
        header_label = ctk.CTkLabel(self, text="Registration Form", font=("Helvetiva",30,"italic"))
        header_label.grid(row=0, columnspan=3, padx=10,pady=10,sticky="nsew")

        #frame login related setting on page
        self.login_frame = MyFramelogin(master=self)
        self.login_frame.grid(row=1, column=0,columnspan=1, padx=10, pady=10, sticky="nsew")

        #frame contact related setting on page
        self.contact_frame = MyFramecontact(master=self)
        self.contact_frame.grid(row=1, column=2,columnspan=1, padx=10, pady=10, sticky="nsew")

        #frame personal related setting on page
        self.personal_frame = MyFramepersonal(master=self)
        self.personal_frame.grid(row=1, column=1,columnspan=1, padx=10, pady=10, sticky="nsew")

        #frame with terms and conditions
        self.tandc_frame=MyFrametandc(master=self)
        self.tandc_frame.grid(row=2, column=0,columnspan=2, padx=10, pady=10, sticky="nsew")



if __name__=="__main__":
    Registration_app=Registrationapp()
    Registration_app.mainloop()