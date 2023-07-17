import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import shap
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("emlakjet.xlsx")

df = df[["brut_metrekare", "binanin_yasi", "binanin_kat_sayisi", "net_metrekare", "oda_sayisi", "bulundugu_kat",
         "isitma_tipi", "fiyat"]]
X = df.drop(["fiyat"], axis=1)
y = df["fiyat"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.27, random_state=11)

xgb = XGBRegressor()
xgb1 = XGBRegressor(colsample_bytree=0.6, learning_rate=0.09, max_depth=2, n_estimators=1000)
model_xgb = xgb1.fit(X_train, y_train)

explainer = shap.Explainer(model_xgb)
shap_values = explainer.shap_values(X_test)


shap_interaction_values = explainer.shap_interaction_values(X_test)

shap.summary_plot(shap_interaction_values, X_test, plot_type='dot')

shap_feature_importance = pd.DataFrame(
    {'Feature': X_test.columns, 'Importance': np.abs(shap_values).mean(axis=0)}
).sort_values('Importance', ascending=False)

plt.figure(figsize=(8, 6))
plt.barh(shap_feature_importance['Feature'], shap_feature_importance['Importance'])
plt.xlabel('SHAP Feature Importance')
plt.ylabel('Feature')
plt.title('SHAP Feature Importance')
plt.tight_layout()
plt.savefig("shap_feature_importance.png")

shap.dependence_plot("brut_metrekare", shap_values, X_test)
shap.dependence_plot("binanin_yasi", shap_values, X_test)
shap.dependence_plot("binanin_kat_sayisi", shap_values, X_test)
shap.dependence_plot("net_metrekare", shap_values, X_test)
shap.dependence_plot("oda_sayisi", shap_values, X_test)
shap.dependence_plot("bulundugu_kat", shap_values, X_test)
shap.dependence_plot("isitma_tipi", shap_values, X_test)

shap.summary_plot(shap_values, X_test)




