from django.shortcuts import render,redirect
from .models import Faces
import cv2
import os

# Create your views here.
def detectface(request):
    if request.method == 'POST':
        filetostore = request.FILES.get('image')
        # filetostore.rename()
        obj = Faces.objects.create(phototostore=filetostore)
        obj.save()
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        img = cv2.imread('test.jpg')
        # Convert into grayscale
        gray = cv2.cvtColor(filetostore, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        # cv2.imshow('img', img)
        # cv2.waitKey()
        # file = Files.objects.get()
        file_name = (filetostore.files)
        print(os.path.basename(file_name.name))

        context = {
            # filename = filetostore
            'filename':file_name,

        }
        return render(request,'detectfaceoutput.html',context=context)
    else:
        context = {
        }
        return render(request,'detectface.html',context=context)


# def detectifface(img):
    # # Load the cascade
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # # Read the input image
    # img = cv2.imread('test.jpg')
    # # Convert into grayscale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # Detect faces
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # # Draw rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # # Display the output
    # cv2.imshow('img', img)
    # cv2.waitKey()
