import cv2
import pytesseract
from PIL import Image

# Path to Tesseract executable (adjust to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = r'C:\Users\Admin\OneDrive\Pictures\TestImage.jpg'
image = cv2.imread(image_path)

# Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(denoised, 150, 255, cv2.THRESH_BINARY)

# Optional: Deskew
coords = cv2.findNonZero(binary)
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle
(h, w) = binary.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
deskewed = cv2.warpAffine(binary, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# Perform OCR
text = pytesseract.image_to_string(deskewed)

# Output
print("Detected Text:")
print(text)
