This notebook contains the program that can retrieve stock price of any company and predict its future stock price.

Libraries required to run this-
---googlesearch   # for doing a search on google for the company's stock price.
---yahoo_finance_api2   # for retrieving the stock data of the company from yahoo finance
---tensorflow/keras    # for training and running the Recurrent Neural Network

The model takes the average of HIGH and LOW of the stock to get a balanced price of the stock.
Since this is a RNN, it considers the sequence of data is very important however we do not take the dates into consideration as it does not affect the model.
