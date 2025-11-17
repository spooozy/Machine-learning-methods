### About Repository

![Python](https://img.shields.io/badge/Python-3.13.7-blue?logo=python)

This repository contains the conditions and implementation of labs for the course "Machine Learning Methods", including:
1. **Python Basics** - tasks for practicing Python syntax, working with the NumPy library and OOP.
2. **EDA** - Exploratory Data Analysis:
    - Checking the dataset for missingness and outliers using static methods and graphically;
    - Eliminating missingness and outliers;
    - Generating new features;
    - Encoding qualitative features;
    - Feature standardization;
    
    **How to run**: 
    - Open [eda.ipynb](eda.ipynb) in Google Colab;
    - Upload the `coffee_health.csv` dataset from the EDA folder in this repository.
3. **Gradient descent with L2 regularization**. The dataset is generated via `make_regression`. Code is in `Linear_regression.ipynb`.
4. **Binary classification** based on logistic regression, SVM, and CART models. CART is optimized using minimal cost-complexity pruning. Code is in `Classification.ipynb`. Dataset used: `loan_data.csv`
