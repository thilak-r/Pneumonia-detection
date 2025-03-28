

Note:
To download trained model, [click here](https://www.kaggle.com/code/thilak02/pneunomia-detection-by-thilak/output)

# Pneumonia Detection 🩺

## **Project Overview**
This project is a deep learning-based system designed to detect pneumonia from chest X-ray images. By leveraging the power of **ResNet18** architecture, the model classifies X-ray images as either **Normal** or **Pneumonia** with high accuracy. The system is built to aid healthcare professionals in making accurate diagnoses quickly and effectively.

---
--
⭐ If you like this project, don't forget to give it a star on GitHub!  

---
<a href="https://github.com/thilak-r/liver-fabrosis-detection/blob/main/Original-ResNet-18-Architecture.png">
  <img src="https://raw.githubusercontent.com/thilak-r/liver-fabrosis-detection/main/Original-ResNet-18-Architecture.png" 
       alt="Original ResNet-18 Architecture" 
       style="max-width: 100%; height: auto; display: block; margin: auto;">
</a>

---
## **Key Features**
- **Deep Learning-Powered**: Utilizes **ResNet18**, a state-of-the-art convolutional neural network architecture.
- **Binary Classification**: Classifies X-ray images into two categories: **Normal** and **Pneumonia**.
- **User-Friendly Interface**: Drag-and-drop functionality with an additional "Choose File" option for uploading images.
- **Performance Metrics**: Includes confusion matrix, classification report, and ROC curve for detailed performance evaluation.
- **Real-Time Predictions**: Provides instant predictions with confidence scores for uploaded X-ray images.

---

## **Technologies Used**

| **Technology**       | **Description**                                                                |
|-----------------------|--------------------------------------------------------------------------------|
| **Python**           | Core programming language for model training and implementation                |
| **PyTorch**          | Deep learning framework for training and fine-tuning the ResNet18 model        |
| **Flask**            | Lightweight web framework for building the application backend                 |
| **HTML/CSS**         | Frontend for the user interface, including drag-and-drop and animations         |
| **Bootstrap**        | CSS framework for styling and responsive design                                |
| **Matplotlib/Seaborn**| Used for visualizing confusion matrix, ROC curve, and training performance     |

---

## **Project Structure**

```plaintext
.
├── app.py                # Backend Flask application
├── static/               # Folder containing CSS, JavaScript, and images for the frontend
├── templates/            # Folder containing HTML templates
│   └── index.html        # Main HTML file for the user interface
├── pneumonia_model.pth   # Trained PyTorch model (not included due to size limits)
├── requirements.txt      # Dependencies for the project
├── README.md             # Project documentation
└── datasets/             # Folder for training and testing datasets

```
---

## 🚀 **How to Run This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/thilak-r/Pneumonia-detection.git
   cd Pneumonia-detection

2. Install Dependencies: 
Run the following command to install all required dependencies:
   ```bash 
   pip install -r requirements.txt

3. Run the Flask App
Start the Flask application by running:
   ```bash
   python app.py

4. Open Your Browser
Navigate to the following address in your web browser to access the application:
   ```bash
   http://127.0.0.1:5000
---

### 🙌 **Contributors**
#### [Thilak R](https://github.com/thilak-r) <br>
#### under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu) <br>
---

❤️ Thank You!
Thank you for checking out our project! We hope this inspires you to explore the intersection of AI and healthcare. Feel free to reach out for questions, suggestions, or collaborations.

<br><br>

   
