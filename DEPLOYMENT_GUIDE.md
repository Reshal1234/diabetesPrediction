# Diabetes Prediction Web App - Deployment Guide

## Current Status
✅ **App is fully functional and running locally**

Your Streamlit diabetes prediction web application is ready to deploy!

## What You Have
- `app.py` - Streamlit web application
- `requirements.txt` - Python dependencies
- `diabetes_model.pkl` - Trained ML model
- `scaler.pkl` - Feature scaler
- `.streamlit/config.toml` - Streamlit configuration

## Deployment Steps

### Step 1: Prepare Your Repository

```bash
cd "c:\Users\ASUS\Desktop\btp - Copy"

# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit: Diabetes prediction app"
```

### Step 2: Deploy to Streamlit Cloud (Recommended - Free)

#### Option A: Using Streamlit Cloud UI (Easiest)

1. **Create a GitHub Account** (if you don't have one)
   - Go to https://github.com and sign up

2. **Push Your Code to GitHub**
   ```bash
   # Create a new repository on GitHub, then:
   git remote add origin https://github.com/YOUR_USERNAME/diabetes-prediction.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your GitHub repository, branch, and `app.py` file
   - Click "Deploy"
   - Your app will be live in minutes!

#### Example Streamlit Cloud URL:
`https://diabetes-prediction-your-username.streamlit.app`

---

### Step 3: Alternative Deployments

#### Option B: Deploy to Heroku (Paid, $5-7/month)

1. **Install Heroku CLI**
   - Download from https://devcenter.heroku.com/articles/heroku-cli

2. **Create Procfile** (save as `Procfile` in project root):
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

#### Option C: Docker + Any Cloud Server

1. **Create Dockerfile** (save in project root):
   ```dockerfile
   FROM python:3.12-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and Run Locally**:
   ```bash
   docker build -t diabetes-app .
   docker run -p 8501:8501 diabetes-app
   ```

3. **Deploy to Cloud**:
   - AWS Elastic Container Service
   - Google Cloud Run
   - DigitalOcean App Platform

---

## Testing Your Deployment

Once deployed, test with sample data:

**Test Case 1 - Negative (No Diabetes)**
- Pregnancies: 1
- Glucose: 100
- Blood Pressure: 70
- Skin Thickness: 20
- Insulin: 80
- BMI: 25.0
- Diabetes Pedigree Function: 0.5
- Age: 35
- Expected: NEGATIVE (Low Risk)

**Test Case 2 - Positive (Diabetes)**
- Pregnancies: 8
- Glucose: 180
- Blood Pressure: 90
- Skin Thickness: 30
- Insulin: 150
- BMI: 35.0
- Diabetes Pedigree Function: 0.8
- Age: 50
- Expected: POSITIVE (High Risk)

---

## File Structure for Deployment

```
diabetes-prediction/
├── app.py                 # Main Streamlit app
├── diabetes_model.pkl     # Trained model
├── scaler.pkl            # Feature scaler
├── pima_diabetes_data.csv # Dataset (optional)
├── requirements.txt       # Dependencies
├── .gitignore            # Git ignore file
├── .streamlit/
│   └── config.toml       # Streamlit config
├── Dockerfile            # For Docker deployment
├── Procfile              # For Heroku deployment
└── README.md             # Project documentation
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Ensure all packages in `requirements.txt` are installed
```bash
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: diabetes_model.pkl"
**Solution**: Make sure `.pkl` files are in the same directory as `app.py`

### Issue: App runs locally but fails after deployment
**Solution**: 
- Check that all files are committed to Git
- Verify file paths don't use absolute paths
- Check logs in deployment platform (Streamlit Cloud shows logs)

---

## Recommended: Streamlit Cloud (My Choice)

**Why Streamlit Cloud?**
- ✅ 100% Free forever for public apps
- ✅ One-click deployment from GitHub
- ✅ Auto-deploys on every Git push
- ✅ Built-in SSL/HTTPS
- ✅ Automatic scaling
- ✅ Perfect for projects and portfolios

**Steps:**
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Click "New app" → Select your repo → Deploy
4. Done! Share the public URL with anyone

---

## API Usage (if needed)

If you want to use this model via API instead of web interface, here's a Flask example:

```python
# api.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])
    scaled = scaler.transform(input_df)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0]
    
    return jsonify({
        'prediction': 'Diabetes' if pred == 1 else 'No Diabetes',
        'confidence': float(prob[pred] * 100)
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Support & Documentation

- **Streamlit Docs**: https://docs.streamlit.io
- **GitHub Help**: https://docs.github.com
- **Heroku Docs**: https://devcenter.heroku.com
- **Docker Docs**: https://docs.docker.com

---

## Next Steps

1. Choose your deployment platform (recommend: **Streamlit Cloud**)
2. Set up GitHub repository
3. Deploy your app
4. Share the live URL with friends and instructors
5. Document the deployment in your project report

**Your app is ready for production!** 🚀
