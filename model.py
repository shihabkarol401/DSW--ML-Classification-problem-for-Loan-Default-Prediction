import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

class LoanRepaymentModel:
    def __init__(self):
        self.model_lr = LogisticRegression()
        self.model_rf = RandomForestClassifier()
        self.preprocessor = None

    def load(self, train_data):
        """Load and preprocess the data."""
        # Handle missing values
        train_data.fillna(train_data.mean(), inplace=True)
        for col in train_data.select_dtypes(include=['object']).columns:
            train_data[col].fillna(train_data[col].mode()[0], inplace=True)

        # Split features and target
        X = train_data.drop('loan_status', axis=1)
        y = train_data['loan_status']

        # Define categorical and numerical columns
        categorical_cols = X.select_dtypes(include=['object']).columns
        numerical_cols = X.select_dtypes(include=[np.number]).columns

        # Create a preprocessor
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(), categorical_cols)
            ])

        # Fit and transform the data
        X_processed = self.preprocessor.fit_transform(X)
        return X_processed, y

    def train(self, X, y):
        """Train Logistic Regression and Random Forest models."""
        self.model_lr.fit(X, y)
        self.model_rf.fit(X, y)

    def test(self, X, y):
        """Evaluate models using various metrics."""
        predictions_lr = self.model_lr.predict(X)
        predictions_rf = self.model_rf.predict(X)

        metrics = {
            'Logistic Regression': {
                'accuracy': accuracy_score(y, predictions_lr),
                'precision': precision_score(y, predictions_lr),
                'recall': recall_score(y, predictions_lr),
                'f1_score': f1_score(y, predictions_lr),
                'roc_auc': roc_auc_score(y, predictions_lr)
            },
            'Random Forest': {
                'accuracy': accuracy_score(y, predictions_rf),
                'precision': precision_score(y, predictions_rf),
                'recall': recall_score(y, predictions_rf),
                'f1_score': f1_score(y, predictions_rf),
                'roc_auc': roc_auc_score(y, predictions_rf)
            }
        }
        return metrics

    def predict(self, new_data):
        """Generate predictions for new data."""
        # Preprocess the new data using the same preprocessor
        new_data_processed = self.preprocessor.transform(new_data)
        
        # Generate predictions using both models
        predictions_lr = self.model_lr.predict(new_data_processed)
        predictions_rf = self.model_rf.predict(new_data_processed)

        return predictions_lr, predictions_rf