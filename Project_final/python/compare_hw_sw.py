import numpy as np
import matplotlib.pyplot as plt

# Load software (OpenCV) output
sw = np.loadtxt("../verilog/input_pixels.txt", dtype=np.uint8).reshape(32, 128)

# Load hardware (Verilog) output
with open("../verilog/verilog_output.txt", "r") as f:
    hw_raw = f.readlines()

# Clean and filter hardware output
hw_clean = [int(line.strip()) for line in hw_raw if line.strip().isdigit()]

# Check if we have exactly 4096 values
if len(hw_clean) < 4096:
    raise ValueError(f"Expected 4096 values from Verilog, got only {len(hw_clean)}.")

# Convert to image array
hw = np.array(hw_clean[:4096], dtype=np.uint8) * 255
hw = hw.reshape(32, 128)

# Side-by-side plot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Software Threshold (Python)")
plt.imshow(sw, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Hardware Threshold (Verilog)")
plt.imshow(hw, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.savefig("../results/comparison.png")
plt.show()
