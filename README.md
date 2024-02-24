# User Behavior Analysis (UBA) Project

## Table of Contents
1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Implementation Details](#implementation-details)
4. [Results](#results)
5. [Conclusion](#conclusion)

## Introduction
User Behavior Analysis (UBA) is a cybersecurity approach focused on understanding and monitoring user behavior within a system. This project implements UBA using the Flask web framework, enabling the tracking of user actions such as login, data access, and transactions. The implementation includes data collection, baseline behavior definition, behavior analytics engine, anomaly detection, and suspicious activity triggers.

## Technology Stack
- ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white): Flask is a micro web framework written in Python. It is used in this project for building the web application that tracks user actions.
- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white): Python is a versatile programming language used for various tasks in this project, including backend development, data analysis, and scripting.
- ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white): Pandas is a Python library used for data manipulation and analysis. It is utilized in this project for logging user activity data into Excel files.
- ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=flat&logo=jupyter&logoColor=white): Jupyter Notebook is an open-source web application that allows users to create and share documents containing live code, equations, visualizations, and narrative text. It is used in this project for descriptive and visual analysis of collected data.
- ![Python Logging Library](https://img.shields.io/badge/-Python%20Logging-3776AB?style=flat&logo=python&logoColor=white): The Python logging library is used for logging alerts and suspicious activity triggers in this project.

## Implementation Details
### Data Collection
- User activity data, including login times, IP addresses, and actions, are collected and stored.
- Flask API endpoints (/login, /data, /transaction) are set up to systematically document user activity details.
- Data is logged into an Excel file using Python's Pandas library.

### Analysis of Data Collected and Baseline Behavior Definition
- User interactions with API calls are mimicked for data analysis.
- Descriptive and visual analysis is performed on the gathered data using Jupyter Notebook.
- Baseline behavior is established based on observed patterns.

### Behavior Analytics Engine
- An effective behavior analytics engine is developed to compare user activity data with the established baseline.
- An analyze user activity function systematically compares user activity details with baseline behavior to identify anomalies.

### Anomaly Detection and Suspicious Activity Triggers
- Anomalies detected by the behavior analytics engine trigger alerts logged using the Python logging library.
- Comprehensive logs allow administrators to review and respond to suspicious activity.

## Results
Simulated user activities were captured and stored, and data analysis was performed to identify regular patterns. Baseline rules were defined for login times, IP addresses, data access, and transactions. Descriptive and visual analysis helped establish these baseline rules. The behavior analytics engine successfully detected anomalies in simulated malicious activity.

## Conclusion
Implementing User Behavior Analysis enhances security by proactively detecting and responding to anomalies in user behavior. This project demonstrated the importance of monitoring user behavior in securing web APIs and provided insights into potential security threats. Future advancements could include incorporating machine learning for more efficient anomaly detection.
