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

## Code functioning
- First run the ``

## License
This project is licensed under MIT.

## About Author
Thus code is written by Malhar Girgaonkar of MREC and was made using datase available at kaggle and wiki. I have modified and reduced the scale of data to fit my model needs. This model is trained on a total of 1.87 GB of data that is of following two categories
- Human made portraits of many kind.
- Ai made portraits that were available on web.

The model was satisfactory and is used in the author's application called M.U.R.A.L. The model trained is very helpful for artists to get the credit that was stolen from them by the new "Gen AI".

link to M.U.R.A.L :  [M.U.R.A.L](https://github.com/Malhar-Girgaonkar/M.U.R.A.L/tree/master)

## Contact 
- Email: [malhargirgaonkarr@gmail.com](mailto:malhargirgaonkarr@gmail.com)
- Linkedin : [Malhar Girgaonkar](https://www.linkedin.com/in/malhar-girgaonkar-b9223a28a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- Github : [Malhar Girgankar](https://github.com/Malhar-Girgaonkar)

## Credits
I would like to give credit to the sources from where i was able to get the datasets that i used in this application.
- Kaggle : [Kaggle.com](https://www.kaggle.com)
- Wiki Art dataset :[WikiArt](https://www.kaggle.com/datasets/sivarazadi/wikiart-art-movementsstyles)

## Contributions
Contributions to AI_Art_vs_Human_Art are welcome. If you encounter issues or have ideas for improvement, please open an issue or submit a pull request.
