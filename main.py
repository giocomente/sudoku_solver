import cv2
import numpy as np


img = cv2.imread("img/SudokuGrid1.jpg", cv2.IMREAD_GRAYSCALE)

def show_image(img, title, dst):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title,900,600)
    cv2.imshow(title, np.hstack((img, dst)))
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def pre_process_image(img, skip_dilate = False):
    proc = cv2.GaussianBlur(img.copy(), (9,9), 0)
    proc = cv2.adaptiveThreshold(proc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
    proc = cv2.bitwise_not(proc, proc)
    if not skip_dilate:
      #kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]],np.uint8)
      kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
      proc = cv2.dilate(proc, kernel)
    return proc

def findCorners(img):
    contours, hierarchy  = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    polygon = contours[0]

    bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in polygon]), key=operator.itemgetter(1))

    top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    return [polygon[top_left][0], polygon[top_right][0], polygon[bottom_right][0], polygon[bottom_left][0]]

def display_points(in_img, points, radius=5, colour=(0, 0, 255)):
    img = in_img.copy()
    if len(colour) == 3:
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for point in points:
        cv2.circle(img, tuple(int(x) for x in point), radius, colour, -1)
    show_image(img,"display_points")
    return img

def main():
    processed = pre_process_image(img)
    #show_image(img, "Processed Image", processed)
    corners = findCorners(processed)
    display_points(processed, corners)
    return 0

if __name__ == "__main__":
    main()

