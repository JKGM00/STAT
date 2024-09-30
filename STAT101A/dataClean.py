import pandas as pd

def clean_data(df):
    # Replace missing values with the mean of each column in: 'I am currently employed at least part-time', 'I identify as having a mental illness' and 16 other columns
    df = df.fillna({'I am currently employed at least part-time': df['I am currently employed at least part-time'].mean(), 'I identify as having a mental illness': df['I identify as having a mental illness'].mean(), 'I have my own computer separate from a smart phone': df['I have my own computer separate from a smart phone'].mean(), 'I have been hospitalized before for my mental illness': df['I have been hospitalized before for my mental illness'].mean(), 'I am legally disabled': df['I am legally disabled'].mean(), 'I have my regular access to the internet': df['I have my regular access to the internet'].mean(), 'I live with my parents': df['I live with my parents'].mean(), 'I have a gap in my resume': df['I have a gap in my resume'].mean(), 'Total length of any gaps in my resume in\xa0months.': df['Total length of any gaps in my resume in\xa0months.'].mean(), 'Annual income (including any social welfare programs) in USD': df['Annual income (including any social welfare programs) in USD'].mean(), 'I am unemployed': df['I am unemployed'].mean(), 'I read outside of work and school': df['I read outside of work and school'].mean(), 'Annual income from social welfare programs': df['Annual income from social welfare programs'].mean(), 'I receive food stamps': df['I receive food stamps'].mean(), 'I am on section 8 housing': df['I am on section 8 housing'].mean(), 'How many times were you hospitalized for your mental illness': df['How many times were you hospitalized for your mental illness'].mean(), 'Anxiety': df['Anxiety'].mean(), 'Depression': df['Depression'].mean()})
    # Replace missing values with the mode of each column in: 'Tiredness'
    df = df.fillna({'Tiredness': df['Tiredness'].mode()[0]})
    # Replace missing values with the most common value of each column in: 'Region'
    df = df.fillna({'Region': df['Region'].mode()[0]})
    # Replace missing values with the mode of each column in: 'How many days were you hospitalized for your mental illness'
    df = df.fillna({'How many days were you hospitalized for your mental illness': df['How many days were you hospitalized for your mental illness'].mode()[0]})
    # Replace missing values with the mode of each column in: 'Lack of concentration'
    df = df.fillna({'Lack of concentration': df['Lack of concentration'].mode()[0]})
    # Drop rows with missing data in column: 'Compulsive behavior'
    df = df.dropna(subset=['Compulsive behavior'])
    # Split text using string '-' in column: 'Age'
    loc_0 = df.columns.get_loc('Age')
    df_split = df['Age'].str.split(pat='-', expand=True).add_prefix('Age_')
    df = pd.concat([df.iloc[:, :loc_0], df_split, df.iloc[:, loc_0:]], axis=1)
    df = df.drop(columns=['Age'])
    # Replace all instances of "18" with "24" in column: 'Age_0'
    df['Age_0'] = df['Age_0'].str.replace("18", "24", case=False, regex=False)
    # Replace all instances of "45" with "53" in column: 'Age_0'
    df['Age_0'] = df['Age_0'].str.replace("45", "53", case=False, regex=False)
    # Replace all instances of "30" with "37" in column: 'Age_0'
    df['Age_0'] = df['Age_0'].str.replace("30", "37", case=False, regex=False)
    # Replace all instances of "> 60" with "62" in column: 'Age_0'
    df['Age_0'] = df['Age_0'].str.replace("> 60", "62", case=False, regex=False)
    # Drop column: 'Age_1'
    df = df.drop(columns=['Age_1'])
    # Change column type to int32 for column: 'Age_0'
    df = df.astype({'Age_0': 'int32'})
    # Rename column 'Age_0' to 'Mean Age'
    df = df.rename(columns={'Age_0': 'Mean Age'})
    return df

# Loaded variable 'df' from URI: c:\Users\User\Desktop\Python\STAT101A\Data_Raw.csv
df = pd.read_csv(r'c:\Users\User\Desktop\Python\STAT101A\Data_Raw.csv')

df_clean = clean_data(df.copy())
df_clean.head()