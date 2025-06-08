import cv2
import numpy as np
import argparse
import os
import time
from hardware_interface import simulate_threshold_hw

# Setup output folder
os.makedirs("results", exist_ok=True)

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl_img = clahe.apply(img)
    cropped = cl_img[10:-10, 10:-10]
    resized = cv2.resize(cropped, (128, 32))
    blurred = cv2.GaussianBlur(resized, (3, 3), 0)
    return blurred

def threshold_software(img):
    start = time.time()
    _, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)
    combined = cv2.bitwise_and(th1, th2)
    end = time.time()
    print(f"[SW] Software thresholding time: {end - start:.6f} seconds")
    return combined

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default="sample.jpg")
    parser.add_argument("--use_hw", action="store_true", help="Use hardware thresholding")
    args = parser.parse_args()

    img = preprocess_image(args.image)

    if args.use_hw:
        print("[INFO] Using hardware-accelerated thresholding...")
        hw_out = simulate_threshold_hw(img)
        cv2.imwrite("results/threshold_hw_output.png", hw_out * 255)
    else:
        print("[INFO] Using software OpenCV thresholding...")
        sw_out = threshold_software(img)
        cv2.imwrite("results/final_combined_threshold.png", sw_out)

if __name__ == "__main__":
    main()
