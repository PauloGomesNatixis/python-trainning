import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('offers.csv')

# Create the total_reward column
df['total_reward'] = df['reward'] * df['difficulty']

# Create the reward_per_day column
df['reward_per_day'] = df['total_reward'] / df['duration']

# Save the transformed DataFrame to a new CSV file
df.to_csv('transformed_offers.csv', index=False)
