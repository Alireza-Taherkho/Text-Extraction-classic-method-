import cv2 as cv
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
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
    blur = cv.GaussianBlur(gray, (3,3), 3)
    edges = cv.Canny(blur, 50, 200)
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)
    
    cv.drawContours(img_copy, sorted_contours, -1, (0,255,0), 3)

    return sorted_contours, img_copy, edges
# -----


def perspective_extractor(contours, img):
    for c in contours:
        x,y,w,h = cv.boundingRect(c)

        accuracy = 0.03 * cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, accuracy, True)
        if len(approx) == 4:
            break

    input_points = np.float32(approx)
    output_inputs = np.float32([[0, 0],
                                [0, y+h],
                                [x+w, y+h],
                                [x+w, 0]])

    M = cv.getPerspectiveTransform(input_points, output_inputs)
    perspective = cv.warpPerspective(img, M, (x+w, y+h))

    return perspective
# -----




img = cv.imread(r"images\entxt7.jpg")
img = resize(img)
contours, res, edges = contour_extractor(img)
perspective_img = perspective_extractor(contours, img)



cv.imshow('img', img)
cv.imshow('res', res)
cv.imshow('edges', edges)
cv.imshow('perspective_img', perspective_img)
cv.waitKey()
cv.destroyAllWindows()




































