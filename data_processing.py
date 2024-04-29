import pandas as pd

def load_data():
    data20 = pd.read_excel(r"D:\SGP\DATA\updated Data Of 2020.xlsx")
    df20 = pd.DataFrame(data20)
    data21 = pd.read_excel(r"D:\SGP\DATA\updated Data Of 2021.xlsx")
    df21 = pd.DataFrame(data21)
    data22 = pd.read_excel(r"D:\SGP\DATA\updated Data Of 2022.xlsx")
    df22 = pd.DataFrame(data22)
    data23 = pd.read_excel(r"D:\SGP\DATA\updated Data Of 2023.xlsx")
    df23 = pd.DataFrame(data23)

    df1 = pd.DataFrame(df20)
    df1['Name'] = df1['Inst_Name'].astype(str) + " - " + df1['Course_name']
    df2 = pd.DataFrame(df21)
    df2['Name'] = df2['Inst_Name'].astype(str) + " - " + df2['Course_name']
    df3 = pd.DataFrame(df22)
    df3['Name'] = df3['Inst_Name'].astype(str) + " - " + df3['Course_name']
    df4 = pd.DataFrame(df23)
    df4['Name'] = df4['Inst_Name'].astype(str) + " - " + df4['Course_name']

    df1.drop("Inst_Name", axis="columns", inplace=True)
    df1.drop("Course_name", axis="columns", inplace=True)
    df2.drop("Inst_Name", axis="columns", inplace=True)
    df2.drop("Course_name", axis="columns", inplace=True)
    df3.drop("Inst_Name", axis="columns", inplace=True)
    df3.drop("Course_name", axis="columns", inplace=True)
    df4.drop("Inst_Name", axis="columns", inplace=True)
    df4.drop("Course_name", axis="columns", inplace=True)

    return pd.concat([df1, df2, df3, df4])

def process_data(all_df, entered_rank):
    # Filter rows with ranks greater than the entered rank
    filtered_rows = all_df[all_df['Rank'] > entered_rank]

    if filtered_rows.empty:
        return "No rows found with rank greater than " + str(entered_rank)
    else:
        # Find duplicate names and calculate mean rank
        duplicates = filtered_rows[filtered_rows.duplicated(subset='Name', keep=False)]
        consolidated_rows = []

        for name, group in duplicates.groupby('Name'):
            mean_rank = group['Rank'].mean()
            consolidated_rows.append({'Name': name, 'Mean Rank': mean_rank})

        # Handle names that are not repeated
        unique_names = filtered_rows[~filtered_rows['Name'].isin(duplicates['Name'])]
        for idx, row in unique_names.iterrows():
            consolidated_rows.append({'Name': row['Name'], 'Mean Rank': row['Rank']})

        # Create a new dataframe from consolidated rows
        consolidated_df = pd.DataFrame(consolidated_rows)

        # Sort the consolidated dataframe by mean rank in ascending order
        sorted_df = consolidated_df.sort_values(by='Mean Rank').reset_index(drop=True)

        return sorted_df
