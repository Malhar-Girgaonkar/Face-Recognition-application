# Face Recognition Application

## Introduction

This Project made to help the users identify human face using OpenCC and harrcascade algorithm.This application can detect face in 3 inputs which are
- Image
- Video
- Webcam

The application also provides the facility to print the bounding box region in terminal and also highlights it on the image , video , webcam footage.A person can login and register to the application and these details are stored in a database.For first time users we have code that helps install dependencies and create the database structure.

## Database Structure:
 
- Database Details:
	- Name:userinfo
	- If using mysql.connect
		- Host: localhost
		- Username: root
		- Password: root
	- if using sqlite3 no need of user credentials
	- Tables:"userlogin","userpersonal","usercontact"

- Table Details: userlogin
  - Primary Key: username
  - Attributes:
 	  - username (VARCHAR, 20)
	  - password (VARCHAR, 20)

- Table Details: userpersonal
  - Primary Key: username
  - Foreign Key: username (references userlogin.username)
  - Attributes:
	  - username (VARCHAR, 20)
	  - firstname (CHAR, 20)
	  - lastname (CHAR, 20)
	  - gender (ENUM: 'Male', 'Female', 'Transgender', 'Others')
	  - dateofbirth (VARCHAR, 10)
	  - country (CHAR, 20)
	  - state (CHAR, 20)
	  - city (CHAR, 20)

- Table Details: usercontact
  - Primary Key: username
  - Foreign Key: username (references userlogin.username)
  - Attributes:
	  - username (VARCHAR, 20)
	  - email (VARCHAR, 40)
	  - icc (ENUM: '+91', '+1', '+44', '+81')
	  - mobileno (INT, 10)
	  - tandc_status (ENUM: 'on', 'off')

## Technological Stack

- CTkMessagebox
- customtkinter (and its submodules)
- tkinter (and its submodules)
- mysql.connector
- subprocess
- PIL (Image, ImageTk)
- cv2 (OpenCV)
- os
- shutil
- importlib
- sqlite3

## Directory structure

- 2-2 project:
	- app data:
		- Database:
			- (stuff related to database and mysql)

			- databasecreatelite.py=(code to create sqlite3 userinfo.db)
		- Dependencies:
			- harrcascade_frontalface_default.xml.=(it is the face recognition algorithm i am using)

			- databasedependencies.py=(It is a program that creates required database and table if they do not exist)

			- requirements.py=(It is a program that checks if required modules or packages are installed and if not installs them)

		- icons:
			- (Icons that can or are used in application)

		- images:
			- (This directory contains images that you will load to application to do action on)

		- videos:
			- (This directory contains videos that you will load to application to do action on) 

	- Build:It is a floder created by pyinstaller during creation of exe file

	- Dist:It is created by pyinstaller to store login.py file's executable version
		- Login.exe=It is the login file's executable version

	- Aboutapp.py=(Contains information about application)

	- ImageFaceRecogniton.py=(Contains code for gui and image based face recognition)

	- Login.py=(It has code for gui and login functionality)

	- mainpage.py=(It has code for gui and mainpage to acess whole applications features)

	- mysqlconn.py=(it has mysql connection features and code snippet to access,create table,delete,truncate,select database)

	- Registration.py=(It has code for gui and Registration functionality)

	- sqlite3conn.py=(It has code to interract with sqlite3 database directly)

	- userinfo.db=(It is the databse i am using in place of mysql and it uses sqlite3)

	- VideoFaceRecogniton.py=(Contains code for gui and Video based face recognition)

	- WebcamFaceRecogniton.py=(Contains code for gui and Webcam based face recognition)

## Code Function

- First run the `dependency.py` and `requirement.py` to set the database and modules.
- open the application folder in vscode/cmd or click the .exe file to run it if available.
- Login page is entry point of application.
- For first time users register and then login.
- After login you would be directed to mainpage wherer you can select what input format you want to work with and proceed.
- In image and video formats for working with respective ddata the selected image/video is stored in application directory in `Appdata/image` or `Appdata/video`.
- Remember to clear the stored data to avoid use of excessive storage.
- Use application to recognize face in input.
- Close application

## Application Images

Following application images:

- Registeration and login.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201305.png" alt="Registration" width="400" height="300"/>
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201157.png" alt="Login" width="400" height="300"/>
</div>

- Image and video based face recognition.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201056.png" alt="Image Face Recognition" width="400" height="300"/>
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201335.png" alt="Video Face Recognition" width="400" height="300"/>
</div>

- Webcam based Image recogniton and Mainpage.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201400.png" alt="Webcam Face Recognition" width="400" height="300"/>
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201221.png" alt="Mainpage" width="400" height="300"/>
</div>

- About Application and Database.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201431.png" alt="About App" width="400" height="300"/>
  <img src="https://github.com/Malhar-Girgaonkar/Face-Recognition-application/blob/master/Demo%20Images/Screenshot%202023-09-10%20201624.png" alt="Database" width="400" height="300"/>
</div>

## License

This project is licensed under MIT.

## About Author

This code is written by Malhar Girgaonkar of MREC and was made using customtkinter, opencv and other relevent modules. This projecct is a gateway into understanding how concepts like DBMS, applications , file storage, github, face recognition work in an application.

## Contact 

- Email: [malhargirgaonkar@gmail.com](mailto:malhargirgaonkar@gmail.com)
- Linkedin : [Malhar Girgaonkar](https://www.linkedin.com/in/malhar-girgaonkar-b9223a28a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- Github : [Malhar Girgankar](https://github.com/Malhar-Girgaonkar)

## Contributions

Contributions to Face recognition applications are welcome. If you encounter issues or have ideas for improvement, please open an issue or submit a pull request.
