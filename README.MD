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

-Table Details: userpersonal

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

- able Details: usercontact

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

## Code functioning
- First we create the dataset from data that we have in two folders for which we have code written in notebook.It splits data into folders as train and validation and each has two categories as AI or Human.
- Then we visualize data using matplotlib.
- There is a section to remove dodgy images which i have not used but was made if we create dataset that is cluttered or dirty.
- Then we start neural network training by importing important functions from `tensorflow`.
- Then we create training data generator and validation data generator.
- Then we visualize data in data generators.
- Implement steps for `EarlyStopping` and `ModelCheckpoint` to help prevent excessive training and save model when we hit a training plateau.
- Then we create the CNN architecture using `sequential` and gain it's summary.
- Then we complile model with `Adam` optimizerloss, loss = `binary_crossentropy`, metric = `accuracy`.
- Then at last we train the model with `model.fit` and save  history.
- the model ran for 4 epochs and finally had following stats loss: 0.0353, accuracy: 0.9908, val_loss: 0.2212, val_accuracy: 0.9461.
- Finally we load model and test it on new data in final section.

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
