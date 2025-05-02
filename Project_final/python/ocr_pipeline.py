import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Load the image in grayscale
img = cv2.imread("../images/hello.png", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not found."

# Apply CLAHE (local contrast enhancement)
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
img_clahe = clahe.apply(img)

# Crop to content (bounding box)
_, mask = cv2.threshold(img_clahe, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
coords = cv2.findNonZero(mask)
x, y, w, h = cv2.boundingRect(coords)
cropped = img_clahe[y:y+h, x:x+w]

# Resize to fixed height and center on canvas
target_height = 32
scale = target_height / h
resized = cv2.resize(cropped, (int(w * scale), target_height))
canvas = 255 * np.ones((32, 128), dtype=np.uint8)
x_offset = (128 - resized.shape[1]) // 2
canvas[:, x_offset:x_offset + resized.shape[1]] = resized
processed = canvas

# Slight blur to reduce noise
blurred = cv2.GaussianBlur(processed, (3, 3), 0)

# ---------- TIME THE THRESHOLDING ----------
start = time.time()

# Apply both Otsu and Adaptive Thresholding
binary_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
binary_adapt = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 3)
binary_combined = cv2.bitwise_and(binary_otsu, binary_adapt)

end = time.time()
print(f"Software thresholding time: {end - start:.6f} seconds")
# -------------------------------------------

# Save to Verilog input
np.savetxt("../verilog/input_pixels.txt", binary_combined.flatten(), fmt="%d")

# Save PNG and show image
plt.figure(figsize=(10, 4))
plt.imshow(binary_combined, cmap='gray')
plt.title("Final Thresholded Output (SW)")
plt.axis('off')
plt.tight_layout()
plt.savefig("../results/final_combined_threshold.png")
plt.show()
