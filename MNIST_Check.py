import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

# Load the model
ANN_model = load_model('Handwritten_digit_ann_model_best.h5')

# Function to preprocess the image
def Image_preprocess(image_path):
    I = Image.open(image_path).convert('L')    # Convert to grayscale
    I = I.resize((28,28))                      # Resize for model input
    I = np.array(I) / 255.0                    # Normalize
    I = I.reshape(1, 784)                      # Flatten to (1, 784)
    return I

# Function to handle image selection and prediction
def imageload_predict():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Display image in the GUI
    display_image = Image.open(file_path).resize((100, 100))
    Tkinter_image = ImageTk.PhotoImage(display_image)
    image_panel.config(image=Tkinter_image)
    image_panel.image = Tkinter_image  # Keep a reference to avoid garbage collection

    # Preprocess and predict
    Iprep = Image_preprocess(file_path)
    Prediction = ANN_model.predict(Iprep)
    Digit = np.argmax(Prediction)

    print(f"Predicted Digit: {Digit}")
    result_label.config(text=f"Predicted Digit: {Digit}")

# Build the GUI
root = tk.Tk()
root.title("Digit Recognizer")
root.geometry("400x400")  # Increased height to accommodate image

tk.Button(root, text="Select your image to be processed!", command=imageload_predict).pack(pady=10)

image_panel = tk.Label(root)
image_panel.pack(pady=10)

result_label = tk.Label(root, text='Predicted Digit: ', font=('Arial', 16))
result_label.pack(pady=40)

root.mainloop()