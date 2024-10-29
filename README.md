# Logistic Regression Example

Logistic regression is a statistical model used for binary classification. It predicts the probability that a given input belongs to a particular class (like 0 or 1).

## Project Overview

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

## Requirements

- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`
