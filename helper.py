import math
import numpy as np
import cv2


def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def canny(img, low_threshold, hight_threshold):
    return cv2.Canny(img, low_threshold, hight_threshold)


def gaussian_blue(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, vertices, ignore_mask_color)

    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    rightX = np.array([])
    rightY = np.array([])
    leftX = np.array([])
    leftY = np.array([])
    for line in lines:
        for x1, y1, x2, y2 in line:
            sloop = (y2 - y1) / (x2 - x1)
            if abs(sloop) > 0.5:
                if sloop > 0:
                    rightX = np.append(rightX, x1)
                    rightX = np.append(rightX, x2)
                    rightY = np.append(rightY, y1)
                    rightY = np.append(rightY, y2)
                else:
                    leftX = np.append(leftX, x1)
                    leftX = np.append(leftX, x2)
                    leftY = np.append(leftY, y1)
                    leftY = np.append(leftY, y2)
    if len(rightX) > 0 and len(rightY) > 0:
        r_m, r_b = np.polyfit(rightX, rightY, 1)
    
        r_x_2 = np.max(rightX)
        r_y_2 = r_m * r_x_2 + r_b
        r_x_1 = np.min(rightX)
        r_y_1 = r_m * r_x_1 + r_b
        cv2.line(img, (int(r_x_1), int(r_y_1)), (int(r_x_2), int(r_y_2)), color, thickness)
        
    if len(leftX) > 0 and len(leftY) > 0:
        l_m, l_b = np.polyfit(leftX, leftY, 1)
        l_x_1 = np.min(leftX)
        l_y_1 = l_m * l_x_1 + l_b
        l_x_2 = np.max(leftX)
        l_y_2 = l_m * l_x_2 + l_b
        cv2.line(img, (int(l_x_1), int(l_y_1)), (int(l_x_2), int(l_y_2)), color, thickness)


def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img


def weighted_img(img, initial_img, a=0.8, b=1., y=0.):
    return cv2.addWeighted(initial_img, a, img, b, y)


def region_lines(img, vertices):
    for i in range(vertices.shape[1]-1):
        cv2.line(img, tuple(tuple(vertices[:, i])[0]), tuple(tuple(vertices[:, i+1])[0]), (0, 255, 0), 10)
    cv2.line(img, tuple(tuple(vertices[:, vertices.shape[1]-1])[0]), tuple(tuple(vertices[:, 0])[0]), (0, 255, 0), 10) 
