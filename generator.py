import cv2
import numpy as np
import string
from PIL import Image, ImageDraw, ImageFont

#arial font 
font = ImageFont.truetype("arial.ttf", 50)  
image_size = (60, 60)


#26n jijig usgiin zurag uusgene (ascii.lowercase)
for letter in string.ascii_lowercase:
    
    #background color 0 = white
    img = Image.new("L", image_size, color=0)  
    draw = ImageDraw.Draw(img)
    
    #letter color 255=black, esregeeree baij magadgui lmao
    draw.text((10, 5), letter, font=font, fill=255)  

    
    
    img_np = np.array(img)
    _, binary_img = cv2.threshold(img_np, 128, 1, cv2.THRESH_BINARY_INV)

    
    cv2.imwrite(f"alphabet/images/{letter}.png", binary_img * 255)  
