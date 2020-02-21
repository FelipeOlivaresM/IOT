import pandas as pd
import numpy as np
from sklearn import svm

expedia = pd.read_csv('train.csv')
df = expedia.loc[expedia['prop_id'] == 104517]
df = df.loc[df['srch_room_count'] == 1]
df = df.loc[df['visitor_location_country_id'] == 219]
df = df[['date_time', 'price_usd', 'srch_booking_window', 'srch_saturday_night_bool']]

# Data check. 
# data = df[['price_usd', 'srch_booking_window', 'srch_saturday_night_bool']]
# scaler = StandardScaler()
# np_scaled = scaler.fit_transform(data)
# data = pd.DataFrame(np_scaled)
# # train oneclassSVM 
# model = OneClassSVM(nu=outliers_fraction, kernel="rbf", gamma=0.01)
# model.fit(data)
# df['anomaly3'] = pd.Series(model.predict(data))

# fig, ax = plt.subplots(figsize=(10,6))
# a = df.loc[df['anomaly3'] == -1, ['date_time_int', 'price_usd']] #anomaly

# ax.plot(df['date_time_int'], df['price_usd'], color='blue')
# ax.scatter(a['date_time_int'],a['price_usd'], color='red')
# plt.show();