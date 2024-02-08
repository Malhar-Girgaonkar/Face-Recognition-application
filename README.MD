# Face Recognition Application

## Introduction

This Project made to help the users identify human face using OpenCC and harrcascade algorithm.This application can detect face in 3 inputs which are
- Image
- Video
- Webcam

## CNN Architecture
 
| Layer (type)                     | Output Shape          | Param   |
| ---------------------------------|-----------------------|---------|
| conv2d_81 (Conv2D)               | (None, 254, 254, 16)  | 448      |
| max_pooling2d_45 (MaxPooling2D)   | (None, 128, 128, 16)  | 0       |
| conv2d_82 (Conv2D)               | (None, 126, 126, 32)  | 4640    |
| max_pooling2d_46 (MaxPooling2D)   | (None, 63, 63, 32)    | 0       |
| conv2d_83 (Conv2D)               | (None, 61, 61, 64)    | 18496   |
| conv2d_84 (Conv2D)               | (None, 59, 59, 64)    | 36928   |
| max_pooling2d_47 (MaxPooling2D)   | (None, 29, 29, 64)    | 0       |
| conv2d_85 (Conv2D)               | (None, 27, 27, 128)   | 73856   |
| conv2d_86 (Conv2D)               | (None, 25, 25, 128)   | 147584  |
| max_pooling2d_48 (MaxPooling2D)   | (None, 12, 12, 128)   | 0       |
| conv2d_87 (Conv2D)               | (None, 10, 10, 256)   | 295168  |
| conv2d_88 (Conv2D)               | (None, 8, 8, 256)     | 590080  |
| conv2d_89 (Conv2D)               | (None, 6, 6, 256)     | 590080  |
| max_pooling2d_49 (MaxPooling2D)   | (None, 3, 3, 256)     | 0       |
| flatten_9 (Flatten)              | (None, 2304)          | 0       |
| dense_27 (Dense)                  | (None, 512)           | 1180160 |
| dense_28 (Dense)                  | (None, 512)           | 262656  |
| dense_29 (Dense)                  | (None, 2)             | 2565    |

                                                                 

## Technological Stack
- Python
- TensorFlow and Keras (Machine Learning)
- PIL (Python Imaging Library)
- Numpy (Accelerated vector computing)
- OpenCV (Computer vision)
- OS (For os related interractions)
- Shutil (For images copying and dataset creation)
- Matplotlib (for graphical visualization)

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
