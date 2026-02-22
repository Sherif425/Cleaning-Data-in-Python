import pandas as pd

ride_share_df = pd.read_csv("./datasets/ride_sharing_new.csv")
print("ride sharing info : ", ride_share_df.info())
print("-----------------------------")
print("ride sharing description:  ", ride_share_df.describe())

#convert user_type from integer to category
ride_share_df['user_type_cat'] = ride_share_df['user_type'].astype('category')