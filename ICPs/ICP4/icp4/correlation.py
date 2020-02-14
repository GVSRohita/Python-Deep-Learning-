import pandas as pd


# visualization
import seaborn as sns
import matplotlib.pyplot as plt

##reading data set
train_df = pd.read_csv('../train.csv')


train_df['Sex'] = train_df['Sex'].map( {'female': 1, 'male': 0} )
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=True))
#Correlation value
print("Correlation value", train_df['Survived'].corr(train_df['Sex']))









