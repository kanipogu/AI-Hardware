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
    if img is None:
     raise ValueError(f"Could not read image at {image_path}")
    #denoised = cv2.medianBlur(cl_img, 3)
    #cropped = cl_img[10:-10, 10:-10]
    resized = cv2.resize(img, (500, 400))
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(resized)
    blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)
    return blurred

def threshold_software(img):
    start = time.time()
    ''', th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)
    combined = cv2.bitwise_and(th1, th2)'''
    binary = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 15, 5
    )
    kernel = np.ones((2, 2), np.uint8)
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    end = time.time()
    print(f"[SW] Software thresholding time: {end - start:.6f} seconds")
    return binary

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default="sample.jpg")
    parser.add_argument("--use_hw", action="store_true", help="Use hardware thresholding")
    args = parser.parse_args()

    img = preprocess_image(args.image)
    #print(f"[DEBUG] Image shape after preprocessing: {img.shape}")
    
    if args.use_hw:
        print("[INFO] Using hardware-accelerated thresholding...")
        cv2.imwrite("results/debug_hw_input.png", img)
        hw_out = simulate_threshold_hw(img)
        cv2.imwrite("results/threshold_hw_output.png", hw_out * 255)
    else:
        print("[INFO] Using software OpenCV thresholding...")
        sw_out = threshold_software(img)
        cv2.imwrite("results/final_combined_threshold.png", sw_out)

if __name__ == "__main__":
    main()
