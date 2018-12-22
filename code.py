# --------------
import pandas as pd 

# Read the data using pandas module.
df_ipl = pd.read_csv(path)
print(df_ipl.info())
#print(df_ipl.head(5))
#print(df_ipl.shape)
#print(df_ipl.describe())

# Find the list of unique cities where matches were played
unique_cities = df_ipl['city'].unique()
#print("The list of unique cities where matches were played is", unique_cities)

# Find the columns which contains null values if any ?
#print(df_ipl.isnull().sum())

# List down top 5 most played venues
#print(df_ipl['venue'].value_counts()[:5])

# Make a runs count frequency table
#print(df_ipl['runs'].value_counts())

# How many seasons were played and in which year they were played 
df_ipl['year'] = df_ipl['date'].apply(lambda x:x[:4])
#print(df_ipl['year'][:5])
#print(df_ipl['year'].nunique())
#print(df_ipl['year'].unique())

# No. of matches played per season
#print(df_ipl['year'].value_counts())

# Total runs across the seasons
#print(df_ipl.groupby('year').runs.agg(sum))

# Teams who have scored more than 200+ runs. Show the top 10 results
high_scores = df_ipl.groupby(['match_code','team1','team2','inning'])['total'].sum().reset_index()
#print(high_scores[high_scores['total'] >= 200])
#print(df_ipl[high_scores] >= 200)

# What are the chances of chasing 200+ target
high_scores1 = high_scores[high_scores['inning']==1]
print(high_scores1)
high_scores2 = high_scores[high_scores['inning']==2]
print(high_scores2)

merged_high = high_scores1.merge(high_scores2[['match_code','inning','total']],on='match_code')
#print(merged_high.head())
match_greater_200 = merged_high[(merged_high['inning_x']==1) & (merged_high['total_x'] >= 200)]
num_match_greater_inning1_200 = len(match_greater_200)

num_match_greater_inning2_200 = len(match_greater_200[match_greater_200['total_y'] >= match_greater_200['total_x']])
#print(len(num_match_greater_inning2_200))

print(num_match_greater_inning2_200/num_match_greater_inning1_200)

# Which team has the highest win count in their respective seasons ?
#print(df_ipl.head(10))
match_wise_winners = df_ipl.drop_duplicates(subset='match_code',keep='first').reset_index()
#print(match_wise_winners.head(10))
print(match_wise_winners.groupby(['year'])['winner'].value_counts())













