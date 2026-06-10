import cv2 as cv
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import easyocr
# -----


def resize(img):
    while True:
        if img.shape[0] > 900 or img.shape[1] > 900:
            img = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2), cv.INTER_AREA)
        else:
            break
    return img
# ----- 



def contour_extractor(img):
    img_copy = img.copy()
    # !!!!!!


    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), 2)
    edges = cv.Canny(blur, 50, 200)
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)
    
    cv.drawContours(img_copy, sorted_contours, -1, (0,255,0), 3)

    return sorted_contours, img_copy, edges
# -----



def text_detection(img):
    copyimg = img.copy()
    gray_copy = cv.cvtColor(copyimg, cv.COLOR_BGR2GRAY)
    thereshold = cv.adaptiveThreshold(gray_copy, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 3)

    text_list = []
    result = reader.readtext(thereshold)
    for (bbox, text, prob) in result:
        (tl, tr, br, bl) = bbox

        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        cv.rectangle(copyimg, tl, br, (0,255,0), 1)
        text_list.append(text)


    return copyimg, text_list
# -----



def perspective_extractor(contours, img):
    loop = 10

    
    for c in contours:
        if loop == 0:
            return img, False
            

        x,y,w,h = cv.boundingRect(c)

        accuracy = 0.03 * cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, accuracy, True)
        if len(approx) == 4:
            loop -= 1

            input_points = np.float32(approx)
            output_inputs = np.float32([[0, y+h],
                                        [x+w, y+h],
                                        [x+w, 0],
                                        [0, 0]])

            M = cv.getPerspectiveTransform(input_points, output_inputs)
            perspective = cv.warpPerspective(img, M, (x+w, y+h))

            rotated_img = cv.rotate(perspective, cv.ROTATE_180)

            finnal_img, text_list = text_detection(rotated_img)

            if text_list != []:
                break

    if text_list == []:
        text_list = False

    

    return finnal_img, text_list
# -----

    




reader = easyocr.Reader(['en'], gpu=False)
img = cv.imread(r"images\entxt5.jpg")
img = resize(img)
contours, res, edges = contour_extractor(img)
finnal_img, texts = perspective_extractor(contours, img)

print(texts)




cv.imshow('res', res)
cv.imshow('finnal_img', finnal_img)
cv.waitKey()
cv.destroyAllWindows()




































