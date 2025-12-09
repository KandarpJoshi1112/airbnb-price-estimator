
# 🏠 Airbnb Price Estimator — Machine Learning Case Study

Predict the nightly price of an Airbnb listing in Seattle using Machine Learning.
Built with a full **end-to-end data science pipeline** and deployed as an interactive **Streamlit web app**.

🟢 Live Demo: https://airbnb-price-estimator.streamlit.app/

---

### 👨‍💻 Author

**Kandarp Joshi**
📍 India
---
AI & Data Science Developer

🌐  Github: [@Kandarp Joshi](https://github.com/KandarpJoshi1112)
🔗  LinkedIn: [@Kandarp Joshi](https://www.linkedin.com/in/kandarp-joshi-3451231bb/)

## 🚀 Tech Stack

| Area           | Tools               |
| -------------- | ------------------- |
| Language       | Python              |
| ML / Pipeline  | Scikit-Learn        |
| Data Wrangling | Pandas, NumPy       |
| Visualization  | Seaborn, Matplotlib |
| Deployment     | Streamlit           |
| Model Export   | Joblib              |
| Environment    | Virtualenv (venv)   |

---

## 📌 Problem Statement

Airbnb hosts set their nightly price manually.
But pricing depends on:
➡ Location
➡ Number of bedrooms/bathrooms
➡ Reviews, ratings
➡ Guest capacity
➡ Booking flexibility

The goal is to **predict the optimal price** from listing features to help hosts stay competitive.

---

## 📊 Model Performance

| Model Version       | MAE ↓     | R² ↑      |
| ------------------- | --------- | --------- |
| Baseline            | 38.53     | 0.490     |
| + Bathrooms feature | 34.60     | 0.504     |
| + Log Transform     | **32.67** | **0.585** |

📌 Lower MAE = more accurate
📌 Higher R² = explains more variation in prices

➡ Final model is **highly effective** for a feature-only baseline 🎯

---

## 🧠 Key Insights

🔥 Top features influencing price:

* Bedrooms
* Accommodation capacity
* Neighborhood
* Review rating
* Room type

📌 Entire homes ≫ private rooms in pricing
📌 More reviews & better ratings → higher demand → higher price

---

## 🖥️ Web App Preview

<img width="1920" height="1080" alt="Screenshot (243)" src="https://github.com/user-attachments/assets/e7ec425b-583d-47a6-a191-0eda4c301764" />

<img width="1920" height="1080" alt="Screenshot (244)" src="https://github.com/user-attachments/assets/5ea723f3-ecc4-4d20-9664-6debe3c10df1" />



Users can input listing info and get a nightly price **instantly** ⚡

---

## 📂 Project Structure

```
airbnb-price-estimator/
│── app.py                        # Streamlit Web App
│── airbnb_price_model.pkl        # Trained Model
│── notebook/
│   └── Airbnb_Price_Estimator_Case_Study.ipynb
│── requirements.txt
│── README.md
│── venv/                         # (Not uploaded to GitHub)
```

---

## ⚙️ Setup Instructions (Run Locally)

```bash
# Clone this repo
git clone https://github.com/<your-username>/airbnb-price-estimator.git
cd airbnb-price-estimator

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

Open browser →
👉 `http://localhost:8501/`

---

## 🧾 Dataset Used

Seattle Airbnb Open Data
(Source: **Kaggle – Inside Airbnb** project)

---

## 🔧 Model & Deployment Details

* RandomForestRegressor trained on:

  * Bedrooms, Bathrooms, Beds
  * Room Type
  * Neighborhood
  * Reviews & Rating
  * Guest Capacity
  * Instant Bookable Flag
* Target is trained as **log(price)** → improves stability
* One-hot encoding + numeric scaling handled inside **Pipeline**
* Exported using `joblib` for deployment in Streamlit

---

## 🔮 Future Enhancements

* Add amenities text using NLP (e.g., wifi, view, parking)
* Seasonal pricing analysis from calendar data
* SHAP-based model explainability in UI
* Online deployment (Streamlit Cloud / HuggingFace)

---

## ⭐ Contributions & Feedback

Feel free to submit pull requests, issues, or suggestions!

---

If you find this project helpful,
please ⭐ **star the repository** and share your thoughts! 💙

---

# 🔗 Links

📄 Case Study Notebook → `/notebook/Airbnb_Price_Estimator_Case_Study.ipynb`
🖥️ App Code → `/app.py`



