import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


train_data = pd.read_csv("train.tsv", delimiter="\t", header=None)
test_data = pd.read_csv("test.tsv", delimiter="\t", header=None)
train_data = train_data.astype(float)
test_data = test_data.astype(float)


X = train_data.iloc[:, :-1]  # все признаки
y = train_data.iloc[:, -1]  # целевая функция

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
train_error = np.max(np.abs(y - y_pred))
print(train_error)

y_test_pred = model.predict(test_data)
y_test_pred_formatted = [f"{value:.8f}" for value in y_test_pred]
test_data['predict'] = y_test_pred_formatted
test_data['predict'].to_csv('../answer.tsv', index=False, header=False)
