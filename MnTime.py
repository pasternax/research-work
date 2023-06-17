import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('New_Mn_values2.xlsx')
df.columns = df.columns.str.replace('time', '')
target_column_numbers = [5, 10, 15, 23, 33, 63]
target_values = [3300, 6900, 7100, 12500, 11400, 10900]
percent = 0.1
results = []

for col_num, target_value, target_col_num in zip(target_column_numbers, target_values, target_column_numbers):
    column = df.iloc[:, col_num]
    closest_values = column.apply(lambda x: abs(x - target_value)).nsmallest(int(len(df) * percent))
    closest_indexes = closest_values.index
    values = df.iloc[closest_indexes, :4]
    results.append((closest_values, closest_indexes, values))

output_df = pd.DataFrame()
for result, target_value in zip(results, target_values):
    closest_values, closest_indexes, values = result
    values['Target Value'] = target_value
    values['Closest Value'] = closest_values
    values['Index'] = closest_indexes
    output_df = pd.concat([output_df, values], ignore_index=True)
output_df.to_excel('twentypercent.xlsx', index=False)