# 💧 AI Water Quality Checker – Machine Learning + Streamlit

This project predicts whether **water is safe or unsafe for drinking** based on chemical properties using a **Machine Learning classification model**.  
The model is deployed using **Streamlit** so users can interact with the AI by adjusting water parameter values.

---

## 🚀 Features

🔹 Predicts potability (Safe / Unsafe) based on 9 scientific water-quality indicators  
🔹 ML model trained on **real-world water potability dataset**  
🔹 **Interactive UI** built using Streamlit sliders  
🔹 Instant result with **visual success / warning messages**  
🔹 Lightweight & runs locally — no cloud required

---

## 🧠 Machine Learning Model

The dataset is trained using a **Random Forest Classifier**.

📌 Training script → `train_model.py` :contentReference[oaicite:0]{index=0}

Key steps:
- Missing values removed
- Train-test split (80/20)
- Model trained and exported as `model.pkl`

---

## 🖥 Streamlit Web App

The ML model is loaded and used for real-time prediction.

📌 Application script → `app.py` :contentReference[oaicite:1]{index=1}

🔹 Users input water sample parameters through sliders  
🔹 Data is passed to the trained model for prediction  
🔹 Output displayed as:

| Result | Message |
|--------|----------|
| 1 | ✅ Water is SAFE for drinking |
| 0 | ⚠️ Water is UNSAFE for drinking |

---

## 📂 Project Structure

```
├── app.py                 # Streamlit application
├── train_model.py         # Script to train and export model
├── model.pkl              # Trained RandomForest model
├── water_potability.csv   # Dataset used for training
└── README.md              # Project documentation
```

---

## 📊 Dataset

Dataset source: **Water Potability**  
Contains 9 chemical indicators + target variable (`Potability` 0/1) such as:

| Parameter | Description |
|----------|-------------|
| pH | Acidity / Alkalinity |
| Hardness | Mineral concentration |
| Solids | Dissolved solids |
| Chloramines | Disinfectant levels |
| Sulfate | Present minerals |
| Conductivity | Water ion flow capacity |
| Organic Carbon | Impurity level |
| Trihalomethanes | Chemical by-products of water disinfection |
| Turbidity | Clarity of water |

---

## ▶ Run the Project Locally

### 🔹 Step 1 — Install dependencies
```
pip install streamlit numpy pandas scikit-learn
```

### 🔹 Step 2 — Train the model (optional)
```
python train_model.py
```

### 🔹 Step 3 — Run the Streamlit app
```
streamlit run app.py
```

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| ML Model | Random Forest |
| Deployment | Streamlit |
| Libraries | NumPy, Pandas, Scikit-Learn, Pickle |

---

## 📌 Future Enhancements

🔹 Deploy on cloud (Streamlit Cloud / Render / AWS)  
🔹 Add mobile-friendly UI  
🔹 Add confidence score for predictions  
🔹 Explainability using SHAP or LIME visualizations  
🔹 Accept CSV file uploads for batch predictions  

---

## 🤝 Contribution

Contributions and improvements are welcome!  
Feel free to **fork the repository, submit issues, or open pull requests**.

---

## ⭐ Support

If you liked this project, please ⭐ **star the GitHub repo** — it motivates further development!

❤️Author: Hani Patel
⭐Linkedin: http://linkedin.com/in/hani-patel-6a9370265
🔗Email: hanipatel0621@gmail.com
