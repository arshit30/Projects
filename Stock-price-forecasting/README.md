This notebook contains the program that can retrieve stock price of any company and predict its future stock price.

Libraries required to run this-<br>
---googlesearch         # for doing a search on google for the company's stock price.<br>
---yahoo_finance_api2   # for retrieving the stock data of the company from yahoo finance.<br>
---tensorflow/keras     # for getting the timeseries generator function.<br>
---xgboost              # for running the XGBoost algorithm<br>
<br>
The model takes the average of HIGH and LOW of the stock to get a balanced price of the stock.<br>
It uses the XGBoost algorithm which consumes very low memory and can train the model in a matter of seconds without overfitting.
