import cv2
import pytesseract
# import Os module to start the audio file
import os 
from gtts import gTTS 
class Output:
    BYTES = 'bytes'
    DATAFRAME = 'data.frame'
    DICT = 'dict'
    STRING = 'string'

def image_to_string(
    image, lang=None, config='', nice=0, output_type=Output.STRING, timeout=0,
):
    """
    Returns the result of a Tesseract OCR run on the provided image to string
    """
    args = [image, 'txt', lang, config, nice, timeout]

    return {
        Output.BYTES: lambda: run_and_get_output(*(args + [True])),
        Output.DICT: lambda: {'text': run_and_get_output(*args)},
        Output.STRING: lambda: run_and_get_output(*args),
    }[output_type]()

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
videocap = cv2.VideoCapture('video.mp4')

# FUNCTION TO CONVERT LIST INTO STRING
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

lst = []
# FUNCTION FOR READ TEXT FROM IMAGE USING TESSETACT
def getFrames(sec):
    videocap.set(cv2.CAP_PROP_POS_MSEC , sec*1000)
    hasFrames , images = videocap.read()
    
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg" , images)
        img = cv2.imread("image"+str(count)+".jpg")
        text = image_to_string(img)
        lst.append(text)
    return hasFrames
sec = 0
count = 1
framesPerSec = 2
sucess = getFrames(sec)
while sucess:
    count = count +1
    sec = sec + framesPerSec
    sec = round(sec,2)
    sucess = getFrames(sec)



# CODE FOR AUDIO




img = cv2.imread('news.png')
text = image_to_string(img)
print(text)