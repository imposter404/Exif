import cv2
import os

def EXIF():
    for filename in os.listdir("pic"):
        image=cv2.imread(os.path.join("pic", filename))
        print(filename)
        os.makedirs('new', exist_ok=True)
        cv2.imwrite('new/'+filename,image)
    print("\n-------------------------------")
    print("Completed")
    print("-------------------------------")
    input()

EXIF()