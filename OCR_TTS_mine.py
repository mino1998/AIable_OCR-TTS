import cv2
import os
import speech_recognition as sr
from gtts import gTTS
import time
import playsound
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename ='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def tesseract(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')
    os.remove(filename)
    return text

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('Camera Window', frame)
        key=cv2.waitKey(1) & 0xFF
        text=tesseract(frame)
        speak(text)

        if (key==27):
            break
cap.release()
cv2.destroyAllWindows()