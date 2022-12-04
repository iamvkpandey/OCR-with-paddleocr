* In order to make environment setup to run OCR_project, please follow the below mentioned steps:
	1. Create a folder in the local directory and unzip all the files in this folder.
	2. Open command prompt and run the "requirements.txt" [ pip install -r requirements.txt ]
	3. Run the "menu.py" file only and choose the option to perform task.
    4. Paste the image with path
        example: C:\Users\dell\Music\project_ocr\test_images\1181-receipt.jpg
    You can use images from test_images folder.

######## project flow ######
1. I have trained the model with "receipt" and "non receipt" data with DenseNet pre-trained model.
    a. you can use Model_training.ipynb file in google colab.
2. Then saved the weights from above binary classification model i.e best_model.h5
3. augumentation.py is used to perform preprocessing on receipt so getter better output from OCR
4. ocr_inferance.py file contain all function like text_extraction() with Paddleocr

NOTE: In order to run paddleocr use python 3.8 version only


## Why paddleocr?
I have used tesseract but accuracy was too bad so switched to paddleocr because it uses CRNN and has high accuracy.