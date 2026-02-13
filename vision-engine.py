import cv2
import numpy as np
import tensorflow as tf
import os

# 1. MATCHING YOUR FOLDER NAMES EXACTLY
# We use the names exactly as they appear in your screenshot
model_path = "model_unquant.tflite"
label_path = "labels.txt"
# Note: If 'labels.txt' fails, try just 'labels' without the .txt
if not os.path.exists(label_path):
    label_path = r"C:\Users\Amit Kumar\Downloads\ecovision2\labels"

# 2. LOAD TFLITE MODEL
print("Checking for AI Brain...")
try:
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    print(" Success: Model Loaded!")
except Exception as e:
    print(f" Error: {e}")
    exit()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 3. LOAD LABELS
class_names = [line.strip() for line in open(label_path, "r").readlines()]

# 4. START CAMERA
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # Pre-process for TFLite
    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0).astype(np.float32)
    img = (img / 127.5) - 1

    # Predict
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    index = np.argmax(output_data[0])
    label = class_names[index]
    confidence = output_data[0][index]

    # UI Overlay
    text = f"{label}: {confidence*100:.0f}%"
    cv2.rectangle(frame, (0, 0), (450, 70), (0,0,0), -1)
    cv2.putText(frame, text, (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("EcoVision Demo", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()