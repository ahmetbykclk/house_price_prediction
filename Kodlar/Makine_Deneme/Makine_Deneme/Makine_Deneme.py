import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
import numpy as np
from sklearn import model_selection
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_excel("emlakjet.xlsx")

df = df[["brut_metrekare","binanin_yasi","binanin_kat_sayisi","net_metrekare","oda_sayisi","bulundugu_kat",
         "isitma_tipi","fiyat"]]
X = df.drop(["fiyat"], axis = 1)
y = df["fiyat"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.26, random_state = 144)
params = {"colsample_bytree":[0.4,0.5,0.6],
         "learning_rate":[0.01,0.02,0.09],
         "max_depth":[2,3,4,5,6],
         "n_estimators":[100,200,500,2000]}
xgb = XGBRegressor()
grid = GridSearchCV(xgb, params, cv = 10, n_jobs = -1, verbose = 2)
grid.fit(X_train, y_train)
print(" Results from Grid Search " )
print("\n The best estimator across ALL searched params:\n",grid.best_estimator_)
print("\n The best score across ALL searched params:\n",grid.best_score_)
print("\n The best parameters across ALL searched params:\n",grid.best_params_)