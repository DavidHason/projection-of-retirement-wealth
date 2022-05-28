# Projection of Retirement Wealth - Predicting your account balance in retiremnt age
## Introduction
The objective of this training estimate (task-1) is to predict the account balance of an bank customer with dataset in 2016 and 2017 using Pythonv 3.7. The dataset wa sourced from the CFD which is one of the largest company in supperannuation in Australia. This report is organized as follows:

1- Overview section describes the dataset used and the features in this dataset.

2- Data Preparation section covers data cleaning and data preparation steps.

3- Data Exploration section explores dataset features and their inter-relationships.

4- Methodology section describes how to estimate the customer's account balance in the retirement age 67 and Program flowchart.

5- Summary and Conclusions section provides a summary of our work and presents our findings.

## Overview:
Project Objective:
Our goal is to see if we can predict an individual's account balance in retired age 67 years within an acceptable increase or decrease in comparison with the amount of current account balance. we will predict account balance in age 67 based on the amount of median growth of the account balance in previous years and curent customer's account balance.

## Target Feature:
Our target feature is account balance in age 67 years.

## Insights:
The account balance of those customers is decreasing all years from 2013 to 2019 makes the projection of account balance nonrealistic and accurate based on our method of median growth in retired age not realistic, however using the median of previous balances is to specify a overal view of balance history of customers inevitable since there are a lot of outlier data points.(see below graphs)

## Summary and Conclusions:
Using the median growth of previous account balances able us to project the account balance in retired age. In addition, our method has some significant issues for those customers are an outlier, and also those who have a high degree of fluctuation in their account balance. This method works very well for most of the cases. A good next step might involve adding some interaction terms and maybe some other higher new features like seifa index to our prediction calculation to improve the prediction accuracy. For instance, we can define a new variable based on the seifa index number and name it as "seifa_coefficient".
