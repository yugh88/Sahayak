from rest_framework.decorators import api_view
from rest_framework.response import Response

from API.serializers import UserSerializer, VendorSerializer
from rest_framework import status
from API.models import CUser, Vendor
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import base64
from io import BytesIO
import torch

from django.shortcuts import get_object_or_404
from deep_translator import GoogleTranslator
from PIL import Image

import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("keras_model.h5", "labels.txt")

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)



@api_view(["POST"])
def describe(request):
    # serializer = ImageSerializer(data=request.DATA)
    # if serializer.is_valid():
    #     serializer.save()
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    decoded_string = base64.b64decode(request.data["data"])
    # Create an image object from the decoded bytes
    image = Image.open(BytesIO(decoded_string))
    results = model([image])
    results.render()
    for im in results.ims:
        buffered = BytesIO()
        im_base64 = Image.fromarray(im)
        im_base64.save(buffered, format="JPEG")
        imgd = base64.b64encode(buffered.getvalue()).decode("utf-8")
        break

    return Response({"data":imgd}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def login(request):
    vendor = get_object_or_404(Vendor, slug=request.data["vendor"])
    del request.data["vendor"]
    user = get_object_or_404(vendor.users, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response(
            {"detail": "Username or password don't match"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    token, created = Token.objects.get_or_create(user=user)
    serial = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serial.data})

@api_view(["POST"])
def signup(request):
    vendor = Vendor.objects.get(slug=request.data["vendor"])
    del request.data["vendor"]
    serial = UserSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        user = CUser.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        vendor.users.add(user)
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serial.data})
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_vendor(request):
    user = get_object_or_404(Vendor, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response(
            {"detail": "Username or password don't match"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serial = UserSerializer(instance=user)
    return Response({"user": serial.data})


@api_view(["POST"])
def signup_vendor(request):
    usr = Vendor.objects.filter(username=request.data["username"])
    serial = VendorSerializer(data=request.data)
    if not usr:
        if serial.is_valid():
            serial.save()
            v = Vendor.objects.get(username=request.data["username"])
            v.set_slug(request.data["username"])
            v.save()
            return Response({"user": serial.data})
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(
            {"detail": "A user with that username already exists."})

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    return Response(
        {
            "status": status.HTTP_200_OK,
            "user": UserSerializer(instance=request.user).data,
        }
    )


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def translate(request):
    translated = GoogleTranslator(
        source=request.data["from"], target=request.data["to"]
    ).translate(request.data["text"])
    return Response({"status": status.HTTP_200_OK, "text": translated})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def transcribe(request):
    translated = {}
    return Response({"status": status.HTTP_200_OK, "text": translated})

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def asl(request):
    decoded_string = base64.b64decode(request.data["data"])
    # Create an image object from the decoded bytes
    img = Image.open(BytesIO(decoded_string))
    hands, img = detector.findHands(img)
    imgSize = 300
    offset = 20
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgOutput = img.copy()
        imgCropShape = imgCrop.shape
        labels = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "H",
            "Hello",
            "Help",
            "I",
            "ily",
            "K",
            "More",
            "please",
            "Thankyou",
            "wait",
            "Y",
        ]
        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
        cv2.rectangle(imgOutput, (x - offset, y - offset-50),
                      (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)
    return Response({"status": status.HTTP_200_OK, "text": ""})