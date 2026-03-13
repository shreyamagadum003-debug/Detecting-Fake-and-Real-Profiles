# Detecting-Fake-and-Real-Profile 

Here is a **clean and professional README** you can use for your GitHub project, Shreya. Since GitHub uses **Markdown**, I’m writing it in **README.md format**.

---

# Fake Profile Detection System

## Overview

The **Fake Profile Detection System** is a Machine Learning project that identifies whether a social media profile is **real or fake** based on user attributes such as followers, following count, number of posts, bio length, and profile picture availability.

The model analyzes patterns commonly found in fake accounts and predicts the authenticity of a profile.

This project also includes a **web interface built using Streamlit** for easy user interaction.

---

# Problem Statement

Fake accounts are widely used on social media platforms for spam, scams, misinformation, and bot activities.

Detecting such accounts manually is difficult and time-consuming.
This project uses **Machine Learning classification** to automatically detect suspicious profiles.

---

# Features

* Detects **Fake vs Real profiles**
* Uses Machine Learning for prediction
* Interactive **Streamlit web interface**
* User-friendly input fields
* Real-time prediction results
* Clean and responsive UI

---

# Technologies Used

### Programming Language

* Python

### Libraries

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* XGBoost
* pickle
* Streamlit

---

# Machine Learning Workflow

### 1 Data Collection

Dataset containing Instagram profile features was used.

### 2 Data Preprocessing

* Handling missing values
* Converting categorical variables to numeric
* Feature scaling

### 3 Exploratory Data Analysis (EDA)

Visualization of relationships between features and fake accounts.

Examples:

* Followers vs Fake Accounts
* Posts vs Fake Accounts
* Following vs Fake Accounts

### 4 Feature Selection

Important features used:

* profile_pic
* bio_length
* posts
* followers
* following

### 5 Model Training

Classification models were tested.
The final model used **XGBoost** for better performance.

### 6 Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* Confusion Matrix

### 7 Model Saving

The trained model is saved using **pickle**.

---

# Web Application

A web application was built using **Streamlit** where users can enter profile details and get predictions instantly.

User Inputs:

* Profile Picture (Yes/No)
* Bio Length
* Posts
* Followers
* Following

Output:

* Real Profile
* Fake Profile

---

# Project Structure

```
fake-profile-detection/
│
├── dataset/
│   └── instagram_fake.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── model/
│   └── fake_profile_model.pkl
│
├── app.py
├── train_model.py
└── README.md
```

---

# How to Run the Project

### Step 1 Clone Repository

```
git clone https://github.com/yourusername/fake-profile-detection.git
```

### Step 2 Install Dependencies

```
pip install -r requirements.txt
```

### Step 3 Run the Streamlit App

```
streamlit run app.py
```

---

# Future Improvements

* Add more features like username patterns and account age
* Improve accuracy with deep learning models
* Deploy the application online
* Support detection for multiple social media platforms

---

# Author

Shreya Magadum
Computer Science Student
Interested in Artificial Intelligence and Machine Learning.

---

If you want, I can also give you **a much more impressive GitHub README with badges, images, demo GIF, and project screenshots** (those make recruiters notice projects much faster).

# output of Fake Profile
<img width="1882" height="826" alt="Image" src="https://github.com/user-attachments/assets/baf098c4-b845-43df-b78e-8fd2bbe4096f" />

# output of Real Profile
