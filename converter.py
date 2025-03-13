import cv2
import os
import numpy as np
import preprocess

#zuragnii path avaad ugsun txt file-d binary dursleliig bichne
def converter(image_path="alphabet\\images\\a.png", end_path="alphabet\\binary\\output_array.txt"):
    
    #har, tsagaan bolon saraal bolgoj huvirgana
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    #budeg saarliig tsagaan, tod saarliig har gej uzeed 0,1 eer durslene
    _, binary_img = cv2.threshold(img, 128, 1, cv2.THRESH_BINARY)

    #durslelee hadgalna
    np.savetxt(end_path, binary_img, fmt="%d")
    
#26n usgee bugdiig ni durslene
def main():
    image_path = "alphabet\\images\\"
    binary_path = "alphabet\\binary\\"
    for letter_image in os.listdir(image_path):
        letter, _ = os.path.splitext(letter_image)
        
        text_path = os.path.join(binary_path, letter + ".txt")
        letter_path = os.path.join(image_path, letter + ".png")
        converter(letter_path, text_path)
        
        preprocess.remove_space(text_path)

if __name__ == "__main__":
    main()
