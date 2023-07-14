import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error


df = pd.read_excel("emlakjet.xlsx")

df = df[["brut_metrekare","binanin_yasi","binanin_kat_sayisi","net_metrekare","oda_sayisi","bulundugu_kat",
         "isitma_tipi","fiyat"]]
X = df.drop(["fiyat"], axis = 1)
y = df["fiyat"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.27, random_state = 11)

xgb = XGBRegressor()
xgb1 = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.09, max_depth = 2, n_estimators = 1000)
model_xgb = xgb1.fit(X_train, y_train)
print(model_xgb.predict(X_test))
predictions = model_xgb.predict(X_test)
print(y_test)
print(model_xgb.score(X_test, y_test))
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)
print(np.sqrt(-1*(cross_val_score(model_xgb, X_test, y_test, cv=11, scoring='neg_mean_squared_error'))).mean())
importance = pd.DataFrame({"Importance": model_xgb.feature_importances_},
                         index=X_train.columns)
print(importance)
plt.figure(figsize=(10,10))
plt.scatter(y_test, model_xgb.predict(X_test), c='crimson')
plt.yscale('log')
plt.xscale('log')

p1 = max(max(model_xgb.predict(X_test)), max(y_test))
p2 = min(min(model_xgb.predict(X_test)), min(y_test))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('True Values', fontsize=15)
plt.ylabel('Predictions', fontsize=15)
plt.axis('equal')
plt.show()
corr_matrix=df.corr()
plt.xticks(range(len(corr_matrix.columns)),\
           corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)),
           corr_matrix.columns)
plt.imshow(corr_matrix, cmap="viridis", interpolation="nearest")
plt.colorbar()
plt.show()