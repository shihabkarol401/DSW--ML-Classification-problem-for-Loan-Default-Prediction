# Classification Problem for Loan Default Prediction
This repository contains a project for predicting loan approvals based on customer data. The project involves Exploratory Data Analysis (EDA) to uncover insights and relationships within the data and the implementation of three machine learning models: Random Forest, Logistic Regression, and AdaBoost. The model with the highest accuracy is selected for deployment.

# Project Workflow
1. Data preprocessing: Handle missing values, encode categorical variables, and scale numerical features.
2. Exploratory Data Analysis: Identify patterns and relationships in the dataset.
3. Model training: Train three models (Random Forest, Logistic Regression, AdaBoost).
4. Model evaluation: Compare model performance metrics.
5. Model selection: Select the model with the highest accuracy.
   
# Dataset Description
The dataset contains the following features:
1. ApplicantIncome: Income of the applicant.
2. LoanAmount: Loan amount requested.
3. Loan_Amount_Term: Term of the loan.
4. Credit_History: Credit history of the applicant.
5. Loan_Status: Target variable (1: Approved, 0: Not Approved).
   
# EDA (Exploratory Data Analysis)
The EDA phase involves:
1. Distribution analysis of numerical and categorical features.
2. Identifying correlations between features and the target variable./
3. Handling outliers and missing data.
4. Visualizing important patterns using plots such as histograms, box plots, and scatter plots.
   
# Machine Learning Models
The following models were implemented:
1. AdaBoost: Achieved an accuracy of 77%
2. Logistic Regression: Achieved an accuracy of 74%.
3. Random Forest: It ranges between 76 80%

# Model Selection

A separate file, model_selection.ipynb, is included in this repository. This script automatically selects the model with the highest accuracy, As their are minor differnce in a accuray of random forest and adaboost so when randomforest accuracy is 76 then it will select the Adaboost as preferred model. if its greater than 76% then it will select Random forest.
