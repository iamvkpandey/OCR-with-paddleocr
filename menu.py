import warnings
warnings.filterwarnings("ignore")

from ocr_inferance import *

#### below will display the menu
ab = ''
while  ab!='e':
    ab = input("chose from below below:\n 1. Press 1 to check if image is a receipt and extract words \n 2. Press 'e' to exit\n")

    if ab == '1':
        x = input("Enter the image with full path\n")
        img, image = get_image(x)

        text_extraction(image,img)
        print('='*80)

