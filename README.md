# 🧠 Handwritten Digit Recognizer with GUI

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-2.x-red?logo=keras)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A simple yet powerful Handwritten Digit Recognition application using an Artificial Neural Network (ANN) built with TensorFlow and Keras. The app features a user-friendly interface created with Tkinter that allows users to upload an image and get real-time digit predictions.

---

## 💡 Features

- Digit recognition from handwritten images using a trained ANN model
- Intuitive GUI built with Tkinter
- Image preprocessing pipeline (grayscale, resize, normalization)
- Easy image upload and instant prediction
- Sample image dataset for testing
- Model training notebook included

---

## 🔧 How to Use This Repository

This repo has two main purposes:  
**(1) Use the GUI for predictions**  
**(2) Train your own model (optional)**

---

### 🖼️ 1. Use the GUI to Predict Handwritten Digits

> **Pre-requisite:** Python 3.7+ with required packages installed.

#### ✅ Steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/digit-recognizer-gui.git
   cd digit-recognizer-gui
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the GUI**
   ```bash
   python digit_gui.py
   ```

4. **Use the App**
   - Click the **“Select your image to be processed!”** button.
   - Choose an image (you can use ones from the `sample_digits/` folder).
   - View the predicted digit in the app window and console output.

---

### 🧠 2. Train Your Own ANN Model

> Use this if you want to retrain the model from scratch.

#### 🛠️ Steps:

1. Open the notebook:
   ```bash
   jupyter notebook train.ipynb
   ```

2. Run through the cells to:
   - Load and preprocess MNIST dataset
   - Train a simple ANN
   - Save the model as `Handwritten_digit_ann_model_best.h5`

3. Replace the model file used by `digit_gui.py` with your new `.h5` file.

---

## 📁 Project Structure

```
├── digit_gui.py                         # Tkinter GUI application
├── train.ipynb                          # Notebook for training the ANN
├── Handwritten_digit_ann_model_best.h5 # Pre-trained ANN model
├── sample_digits/                       # Folder with test images
├── requirements.txt                     # Project dependencies
└── README.md                            # This file
```

---

## 📦 Requirements

Below is the list of Python dependencies:

```txt
tensorflow
numpy
pillow
matplotlib
jupyter
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 📸 Preview

<!-- Add screenshot here after you upload -->
![App Preview](assets/cover.png)

> ✨ Don't have a screenshot yet? Just run the app and take a screenshot, then upload it under `assets/cover.png`.

---

## 🚀 Future Improvements

- Add canvas to draw digits directly in the app
- Use Convolutional Neural Network (CNN) for improved accuracy
- Display prediction confidence
- Add batch image testing feature
- Polish GUI layout and make it cross-platform responsive

---

## 🏷️ GitHub Tags

```
#python #machine-learning #digit-recognition #tkinter #keras #mnist #gui #deep-learning #ann #computer-vision
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
