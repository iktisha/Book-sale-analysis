
import pandas as pd

df = pd.read_csv('Books.csv', quotechar='"', on_bad_lines='skip')

# Clean Number of Reviews
df['Number of Reviews'] = pd.to_numeric(
    df['Number of Reviews'].astype(str).str.replace(',', ''), errors='coerce'
)

# Clean Rating
df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+)').astype(float)

# Clean Price
def clean_price(val):
    if isinstance(val, str):
        if 'from $' in val:
            val = val.split('from $')[-1]
        val = val.replace('$', '')
    try:
        return float(val)
    except:
        return None

df['Price'] = df['Price'].apply(clean_price)

# Clean Rank
df['Rank'] = df['Rank'].astype(str).str.replace('#', '').astype(int)

# Rename columns
df.rename(columns={
    'Book Name': 'Title',
    'Book Author': 'Author',
    'Number of Reviews': 'Reviews',
    'Format': 'Cover_Type'
}, inplace=True)

df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['Price'] = df['Price'].fillna(df['Price'].median())
df['Cover_Type'] = df['Cover_Type'].fillna('Unknown')
df['Reviews'] = df['Reviews'].fillna('Unknown')
print(df.isnull().sum())


df.to_csv("clean_books.csv", index=False)
print("Cleaned dataset saved.")
