# Overload Classification with Synthetic Sensor Data

[Türkçe](README.tr.md)

## Overview

A completed final project for the Turkish Artificial Intelligence Academy machine learning course. It explores overload classification using synthetic voltage, current and temperature data.

The dataset is generated for experimentation, rather than collected from deployed physical sensors.

## Contribution

I completed this technical project with my project teammate. We carried out the development and evaluation ourselves.

## Workflow

1. Generate synthetic sensor data, including missing and anomalous values.
2. Clean the data and prepare features.
3. Train and compare Logistic Regression, Random Forest and Gradient Boosting models.
4. Evaluate classification performance using recall and ROC-AUC.

## Run

With Python installed, run these commands from the repository directory:

```bash
python -m pip install -r requirements.txt
python veri_uret.py
python model_egit.py
```

Data generation may replace the existing generated dataset.

## Limitations

Evaluation concerns synthetic data. It does not establish performance on real hardware or demonstrate advance prediction of future overload events. Report results together with the model, test-set size and data-splitting procedure.

## Status

Completed educational project.



### 🚀 How to Run
1. Create and activate a virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate the data first: `python veri_uret.py`
4. Train the model: `python model_egit.py`
