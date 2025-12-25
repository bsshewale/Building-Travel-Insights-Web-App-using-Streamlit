import pandas as pd
from .config import ALLOWED_PACKAGE_TYPES

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Hotel Details'].fillna('Not Available', inplace=True)
    df['Airline'].fillna('Not Available', inplace=True)
    df['Onwards Return Flight Time'].fillna('Not Available', inplace=True)
    df['Sightseeing Places Covered'].fillna('Not Available', inplace=True)
    df['Cancellation Rules'].fillna('Not Available', inplace=True)

    df.drop(columns=["Flight Stops", "Meals", "Initial Payment For Booking", "Date Change Rules"], inplace=True)

    df['Travel Date'] = pd.to_datetime(df['Travel Date'], format='%d-%m-%Y', errors='coerce')

    df = df[df['Package Type'].isin(ALLOWED_PACKAGE_TYPES)]
    df.drop(['Company', 'Crawl Timestamp'], axis=1, inplace=True)

    df['Hotel_Info'] = df['Hotel Details'].str.cat(df['Destination'], sep='|')
    return df
