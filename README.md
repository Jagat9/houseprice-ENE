# houseprice-ENE
this is the house price prediction end to end model DATA SOURCE https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data

ABOUT FILES
usa housing.csv -data file
asgi.pu Django -starter file in case of jango framework 
finale model.csv- like the test csv file for testing my internal prediction data 
home.html - The html page of the output
manage.py - Django system file
prediction.py - main model prediction and Api to jango 
setting,url,wsgi,views - system file for Django
Views.py - view the results and API for html and Django

ABOUT THE DATA
train.csv - the training set
test.csv - the test set
data_description.txt - full description of each column, originally prepared by Dean De Cock but lightly edited to match the column names used here
sample_submission.csv - a benchmark submission from a linear regression on year and month of sale, lot square footage, and number of bedrooms

CODE AND TOOLS USED
Imputing missing values by proceeding sequentially through the data

Transforming some numerical variables that seem really categorical

Label Encoding some categorical variables that may contain information in their ordering set

Box Cox Transformation of skewed features (instead of log-transformation) : This gave me a slightly better result both on leaderboard and cross-validation.

Getting dummy variables for categorical features.
