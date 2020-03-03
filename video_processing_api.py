from flask import Flask, render_template, request,session,flash,abort
import sqlite3 as sql
import cv2
import pytesseract
# import Os module to start the audio file
import os 
from gtts import gTTS 


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'oh_so_secret'

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
videocap = cv2.VideoCapture('video.mp4')

# FUNCTION TO CONVERT LIST INTO STRING
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

lst = []
# FUNCTION FOR READ TEXT FROM IMAGE USING TESSETACT
def getFrames(sec):
    videocap.set(cv2.CAP_PROP_POS_MSEC , sec*1000)
    hasFrames , images = videocap.read()
    if hasFrames:
        text = pytesseract.image_to_string(images)
        lst.append(text)
    return hasFrames

sec = 0
count = 1
framesPerSec = 2
@app.route('/api/upload', methods=['POST', 'GET'])
def upload():
    vdeo = request.files['video']
    videocap = cv2.VideoCapture('video.mp4')
    sucess = getFrames(sec)
    while sucess:
        count = count +1
        sec = sec + framesPerSec
        sec = round(sec,2)
        sucess = getFrames(sec)
    # CODE FOR AUDIO
    mytext = ""
    mytext = listToString(lst);
    # Language we want to use 
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("output.mp3") 
    # Play the converted file 
    os.system("start output.mp3") 
    return 0



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=4000)