# Diabetes Prediction Web Application

A machine learning-powered web application that predicts the likelihood of diabetes based on patient health metrics using an Ensemble Voting Classifier.

## Features

✨ **Interactive Web Interface**
- User-friendly form for entering patient health data
- Real-time predictions with confidence scores
- Risk level assessment (Low, Moderate, High)
- Probability breakdown visualization

🤖 **Advanced ML Model**
- **Ensemble Voting Classifier** combining:
  - Support Vector Machine (SVM)
  - Random Forest Classifier
  - XGBoost Classifier
- Trained on Pima Indians Diabetes Dataset
- 10-Fold Cross-Validation for accuracy verification
- 88.94% accuracy with high recall for medical safety

📊 **Model Explainability**
- SHAP values for global feature importance
- LIME for local patient-specific explanations
- Partial Dependence Plots

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with scikit-learn, XGBoost
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Interpretability**: SHAP, LIME

## Installation

### Prerequisites
- Python 3.10+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Input Parameters

| Parameter | Range | Unit |
|-----------|-------|------|
| Pregnancies | 0-15 | Number |
| Glucose | 0-300 | mg/dL |
| Blood Pressure | 0-200 | mmHg |
| Skin Thickness | 0-100 | mm |
| Insulin | 0-900 | mu U/ml |
| BMI | 10-60 | kg/m² |
| Diabetes Pedigree Function | 0-2.5 | Score |
| Age | 18-100 | Years |

### Output

- **Prediction**: Diabetes/No Diabetes
- **Confidence**: Probability percentage (0-100%)
- **Risk Level**: Low (0-30%), Moderate (30-60%), High (60-100%)
- **Probability Breakdown**: Individual probabilities for both classes

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions on deploying to:
- Streamlit Cloud (Free) ⭐ Recommended
- Heroku
- Docker + Cloud Server
- AWS / Google Cloud / Azure

### Quick Deployment to Streamlit Cloud

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Select your repository and deploy
4. Your app is live!

Live Demo: [Your Streamlit Cloud URL]

## Project Structure

```
diabetes-prediction/
├── app.py                      # Main Streamlit application
├── diabetes_model.pkl          # Trained ensemble model
├── scaler.pkl                  # Feature scaler
├── pima_diabetes_data.csv      # Training dataset
├── diabetes_prediction.ipynb   # Model training notebook
├── requirements.txt            # Python dependencies
├── .streamlit/config.toml      # Streamlit configuration
├── DEPLOYMENT_GUIDE.md         # Deployment instructions
└── README.md                   # This file
```

## Model Performance

### Test Accuracy (Single Train-Test Split)
- **Ensemble Voting**: 87.66%
- **Random Forest**: 87.66%
- **XGBoost**: 86.36%
- **SVM**: 83.12%

### 10-Fold Cross-Validation Results (Rigorous Evaluation)
```
Ensemble Voting: 88.94% ± 3.48%
Random Forest: 88.80% ± 3.29%
XGBoost: 88.67% ± 2.73%
SVM: 85.28% ± 4.04%
Neural Network: 85.42% ± 3.53%
```

### Clinical Metrics
- **Sensitivity (Recall)**: High - prioritizes detecting true diabetes cases
- **Specificity**: Balanced to avoid excessive false alarms

### Feature Importance
Top features influencing prediction:
1. **Glucose** - Most important predictor
2. **Insulin** - Strong indicator
3. **BMI** - Body mass index correlation
4. **Skin Thickness** - Related to insulin resistance
5. **Age** - Age-related risk factor
6. **Pregnancies** - Historical factor

## Medical Disclaimer

⚠️ **IMPORTANT**: This application is for educational purposes only and should NOT be used as a substitute for professional medical diagnosis or treatment. Always consult a qualified healthcare provider for medical advice and diagnosis.

## Data Source

**Pima Indians Diabetes Dataset**
- Source: National Institute of Diabetes and Digestive and Kidney Diseases
- Instances: 768 patients
- Features: 8 medical measurements
- Target: Diabetes (Yes/No)

## License

This project is open source and available under the MIT License.

## Author

Your Name / Team Name
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## Acknowledgments

- Pima Indians Diabetes Dataset from Kaggle
- Scikit-learn, XGBoost, Streamlit communities
- SHAP and LIME for model explainability

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements

- [ ] Add more medical datasets
- [ ] Implement multi-disease prediction
- [ ] Add patient history tracking
- [ ] Integration with healthcare systems
- [ ] Mobile app version
- [ ] Real-time model updates
- [ ] User authentication & data privacy

---

**Status**: ✅ Production Ready  
**Last Updated**: May 2026  
**Version**: 1.0.0
