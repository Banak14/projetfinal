# Final Project: Mental Health Condition Analysis in the Workplace

## Objective
The objective of this project is to analyze the impact of various workplace factors on employees' mental health conditions, including Anxiety, Burnout, and Depression. The analysis focuses on identifying patterns, relationships, and important features using data analytics techniques and visualizations.

## Business Problem
The project is driven by a business need to understand mental health conditions in the workplace and their correlation with work-life balance, stress levels, and work environment. By providing insights into these relationships, businesses can enhance employee well-being programs and improve productivity.

## Dataset

Source: The dataset contains information on various employee-related features, such as gender, job role, stress levels, hours worked per week, social isolation, and more.

Key Features:

- Age, Gender, Job Role, Industry
- Work Location (Remote, Onsite, Hybrid)
- Work-Life Balance, Stress Level, and Sleep Quality
- Mental Health Condition (Target variable)

## Methodology
This project follows the full data analytics pipeline:

1 .Data Cleaning and Preprocessing:

- Handling missing values.
- Encoding categorical variables such as Job Role, Work Location.
- Creating interaction terms between key features (e.g., stress levels and work location).
- Applying SMOTE for class imbalance treatment.

2 .Exploratory Data Analysis:

- Visualization of the relationship between stress levels, work-life balance, and mental health.
- Identification of patterns through bar plots, heatmaps, and pair plots.
- EDA and visualization tools were crucial for deriving insights from the dataset, guiding the feature selection and model development process.

3 .Feature Engineering:

- Interaction terms such as 'Stress_Work_Location.'
- Binning of continuous variables such as 'Age' into categories (Young, Mid, Senior).

4 .API Integration:

- A Flask-based API was created to serve the processed data, providing access to key insights and allowing users to view data and statistics in a dynamic manner.
- The API enables a user-friendly interface for accessing analysis results, enhancing the accessibility of the data insights

5 .Modeling:

Implemented multiple machine learning models:
- Logistic Regression
- Random Forest
- Decision Tree
- Gradient Boosting
- Support Vector Classifier (SVC)

Hyperparameter tuning and model evaluation using accuracy and classification reports.
Addressing class imbalance with SMOTE and weighted models.

6 .Results and Insights:

- Random Forest achieved the best performance in terms of accuracy and balanced predictions across mental health conditions.
- Feature importance analysis revealed stress level, work-life balance, and work location as significant contributors to mental health conditions.

## Results

Best Model: Random Forest with an accuracy of 0.65.

Key Insights:

- Employees working onsite experience more stress, leading to higher instances of Burnout and Anxiety.
- Balanced work-life conditions reduce the probability of developing mental health issues.
- High stress levels correlate directly with a rise in mental health concerns, particularly Burnout.

## Visualization
- Visualizations were done using Tableau and Matplotlib. Tableau dashboards provide interactive insights into the data, making it easy to identify trends and make data-driven decisions.

## Tools & Libraries
- Python: For data analysis and machine learning (pandas, scikit-learn, imblearn, etc.).
- Flask: For API integration, allowing users to access data insights.
- SQLAlchemy: For efficient data handling and storage using MySQL.
- Tableau: For building interactive dashboards.
- PowerPoint: For final project presentation.

## Conclusion

The analysis underscores the importance of work-life balance, stress management, and appropriate work environments for improving employees' mental health. This project provides actionable insights for businesses to take proactive steps toward enhancing workplace well-being.

