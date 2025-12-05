Power Consumption Predictor
Overview

Power Consumption Predictor is a machine-learning project that trains an XGBoost regression model on 13 years of hourly electricity consumption data from Statnett (Norway’s transmission system operator).
Given four simple inputs:

Year

Month

Day

Hour

the model predicts the total power consumption for that timestamp.

This project serves as a practical baseline forecaster for electricity demand analysis, load estimation, and energy-system experimentation.

Dataset

Source: Statnett Open Data
https://www.statnett.no/for-aktorer-i-kraftbransjen/tall-og-data-fra-kraftsystemet/last-ned-grunndata/

Granularity: Hourly demand data

Coverage: 13 years (exact range depends on downloaded dataset)

Target Variable: Electricity consumption (MW)

Features Used:

Year – captures long-term trends

Month – captures seasonal variation

Day – captures intra-month patterns

Hour – captures daily consumption cycles

Data is loaded, cleaned, and transformed into model-ready features during the training stage.


Model Description

Algorithm

The project uses XGBoost Regressor, a gradient-boosted decision-tree model well suited for forecasting tasks involving structured time-based features.

Training Setup

Train/test split: last portion of dataset held out for evaluation

Model saved as: xgb_model.pkl


Evaluation Metrics

The model is evaluated using:

R² (Coefficient of Determination)

RMSE (Root Mean Squared Error)

MSE (Mean Squared Error)

R2:   0.84

RMSE: 1218.10

MSE: 1483770.51 




Future Enhancements

Add weather features: temperature, wind speed, humidity

Add lag feature engineering

Implement rolling time-series validation

Deploy to cloud (Azure, AWS, GCP, Fly.io, etc.)

Add Dockerfile + CI pipeline

Build a frontend dashboard for visualization

