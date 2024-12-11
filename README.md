Classification Problem for Loan Default Prediction

NBFC:
This repository contains a project for predicting loan approvals based on customer data. The project involves Exploratory Data Analysis (EDA) to uncover insights and relationships within the data and the implementation of three machine learning models: Random Forest, Logistic Regression, and AdaBoost. The model with the highest accuracy is selected for deployment.

Table of Contents:
Introduction
Project Workflow
Dataset Description 
EDA (Exploratory Data Analysis) 
Machine Learning Models 
Model Selection 
Results
How to Run Dependencies 

Conclusion:
Introduction:
The goal of this project is to predict whether a loan application will be approved based on various applicant details. The prediction can assist financial institutions in making informed decisions efficiently.

Project Workflow:
Data preprocessing: Handle missing values, encode categorical variables, and scale numerical features.
Exploratory Data Analysis: Identify patterns and relationships in the dataset.
Model training: Train three models (Random Forest, Logistic Regression, AdaBoost).
Model evaluation: Compare model performance metrics. 
Model selection: Select the model with the highest accuracy. 
Dataset Description: The dataset contains the following features:

ApplicantIncome: Income of the applicant
LoanAmount: Loan amount requested
Loan_Amount_Term: Term of the loan
Credit_History: Credit history of the applicant
Loan_Status: Target variable (1: Approved, 0: Not Approved)
EDA (Exploratory Data Analysis) The EDA phase involves:

> Distribution analysis of numerical and categorical features. 
> Identifying correlations between features and the target variable.
> Handling outliers and missing data. 
> Visualizing important patterns using plots such as histograms, box plots, and scatter plots.
> Machine Learning Models The following models were implemented:

AdaBoost: Achieved an accuracy of 77% 
Logistic Regression: Achieved an accuracy of 74%. 
Random Forest: It ranges between 76-80% 
Model Selection: A separate file, model_selection.ipynb, is included in this repository. This script automatically selects the model with the highest accuracy, As their are minor differnce in a accuray of random forest and adaboost

When randomforest accuracy is 76 then it will select the Adaboost as preferred model. If its greater than 76% then it will select Random forest.
