Introduction
In this project, we take the input of the desired house’s properties, such as its area, number of rooms, and the floor it is located on. Subsequently, a machine learning model is developed using this input data to estimate the price, which is then displayed to the users as an output.

Steps Involved
1- Importing house price data

2- Data visualization

3-Data labeling

4- Creating a machine learning model

5- Explaining the model with shap values

6- Creating an application interface

Importing House Price Data
I used Selenium for scraping data from the Emlakjet website. The data was scraped from Kapaklı/Tekirdağ/Turkey. The scraped data was saved to an Excel file.

I made my project in Turkish. Here are the English translations of my columns:

Category
Gross Square Meter
Age of the Building
Number of Floors of the Building
Usage Status
Ad Creation Date
Type
Net Square Meter
Number of Rooms
Floor Location
Heating Type
Price

Data Visualization
I used the Matplotlib library for data visualization. 

Data Labeling
We will use the scikit-learn (sklearn) library for preprocessing our data. We need to label our data for the machine learning model.

Creating a Machine Learning Model
For the machine learning model, I used the XGBoost algorithm. The properties I utilized include Gross Square Meter, Age of the Building, Number of Floors of the Building, Net Square Meter, Number of Rooms, Floor Location, and Heating Type. With these properties, our machine learning model will predict the appropriate price for the house.
![Actual predict plot](https://github.com/ahmetbykclk/house_price_prediction/assets/64368104/96e7a779-4b4e-45b0-bac0-e29e89b76a2b)

Explaining The Model With Shap Values
Using Shap, we can analyze our model and visualize its behavior. With this capability, we can effectively explain our machine learning model.
![ShapFeatureImportance](https://github.com/ahmetbykclk/house_price_prediction/assets/64368104/baf4c7d7-a3c6-4b65-9a4c-90ca329782c6)

Creating an Application Interface
For the interface of our application, I used the Tkinter library from Python. After completing the interface, we should use our algorithm to calculate and predict the price for this house.

![App-BeforeUse](https://github.com/ahmetbykclk/house_price_prediction/assets/64368104/0c66de9d-c3e4-4c47-ab6d-9fd1e5db131b)
![App-AfterUse](https://github.com/ahmetbykclk/house_price_prediction/assets/64368104/2861b378-16c7-4b65-90d6-9dbb9d1756b2)

I aimed to create a simple interface, but you can enhance it to make it more visually appealing and user-friendly.
