# Logistic Regression Example

Logistic regression is a statistical model used for binary classification. It predicts the probability that a given input belongs to a particular class (like 0 or 1). This project demonstrates two applications of logistic regression: one for classifying houses based on their area size, and another for predicting high-growth IT job roles based on projected growth by 2030.

## Example 1: House Classification Based on Area; Overview

This project involves a dataset of houses with features such as area, bedrooms, bathrooms, floors, year built, location, condition, and garage status. The goal is to predict a binary label (`0` or `1`) based on whether the area of a house exceeds a specific threshold (e.g., 3000 sq. ft.). This threshold is used to distinguish between two classes: small (0) and large (1) houses.

## Dataset

The dataset contains the following columns:
- `Id`: Unique identifier for each house
- `Area`: The total area of the house
- `Bedrooms`: Number of bedrooms
- `Bathrooms`: Number of bathrooms
- `Floors`: Number of floors
- `YearBuilt`: Year the house was built
- `Location`: General location of the house (e.g., Downtown, Suburban, Rural, Urban)
- `Condition`: Condition of the house (e.g., Excellent, Good, Fair, Poor)
- `Garage`: Indicates if the house has a garage
- `Price`: The price of the house

## Steps

1. **Data Preparation**: Load the dataset, inspect for any missing values, and create a binary label column (`Label`) based on a chosen area threshold.
2. **Feature Selection**: Use `Area` as the input feature (`X`) and the newly created `Label` as the target variable (`y`).
3. **Data Splitting**: Split the data into training and testing sets to evaluate the model's performance.
4. **Model Training**: Train a logistic regression model on the training data.
5. **Model Evaluation**:
   - Calculate the accuracy score and confusion matrix to assess the model's performance.
   - Generate a classification report to analyze `precision`, `recall`, and `f1-score`.
6. **Visualization**: Plot the logistic regression curve along with actual data points to visualize the probability of belonging to class 1 as a function of `Area`.

## Example 2: High-Growth IT Job Classification; Overview
This project uses a dataset of IT job roles with their projected growth by 2030. The objective is to classify whether a job role is expected to have high growth (1) or not (0) based on a projected growth threshold (e.g., 100%).

## Dataset

The IT job dataset contains the following columns:
-`Domain`: Technology domain of the job (e.g., Cloud Computing, Cybersecurity, Data Analytics)
-`Job Title`: Title of the job role (e.g., Analyst, Engineer, Manager)
-`Projected Growth by 2030`: Projected growth rate for the job role by 2030

## Steps

1. **Data Preparation**: Load the dataset, check for missing values, and create a binary label (`Label`) based on whether the Projected Growth by 2030 exceeds a specific threshold (e.g., 100).
2. **Feature Selection**: Use `Projected Growth by 2030` as the input feature (`X`) and Label as the target variable (`y`).
3. **Data Splitting**: Split the data into training and testing sets.
4. **Model Training**: Train a logistic regression model on the training data.
5. **Model Evaluation**: Compute accuracy, confusion matrix, and classification report.
6. **Visualization**: Plot the logistic regression curve to visualize the probability of high growth based on projected growth.

## Requirements

- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`
