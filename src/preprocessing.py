

#### **2. `src/preprocessing.py`**
#Place reusable preprocessing functions in `src/preprocessing.py`:

#python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    """
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isnull().mean() < 0.05:
            df.dropna(subset=[col], inplace=True)
        else:
            df[col].fillna('Unknown', inplace=True)
    return df

def clean_data(df):
    """
    Perform data cleaning tasks.
    """
    df.drop_duplicates(inplace=True)
    if 'signup_time' in df.columns:
        df['signup_time'] = pd.to_datetime(df['signup_time'])
    if 'purchase_time' in df.columns:
        df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    categorical_cols = ['source', 'browser', 'sex']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
    return df

def map_ip_to_country(fraud_df, ip_country_df):
    """
    Map IP addresses to countries.
    """
    fraud_df['ip_address_int'] = fraud_df['ip_address'].apply(lambda x: int(float(x)))
    merged_df = pd.merge(
        fraud_df,
        ip_country_df,
        how='left',
        left_on='ip_address_int',
        right_on='lower_bound_ip_address'
    )
    merged_df['country'] = merged_df['country'].fillna('Unknown')
    merged_df.drop(columns=['lower_bound_ip_address', 'upper_bound_ip_address'], inplace=True)
    return merged_df

def feature_engineering(df):
    """
    Perform feature engineering.
    """
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.day_name()
    df['transaction_frequency'] = df.groupby('user_id')['user_id'].transform('count')
    df['time_to_action'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600
    return df

def normalize_and_encode(df):
    """
    Normalize numerical features and encode categorical features.
    Exclude the 'class' column from scaling.
    """
    # Separate the target variable ('class') from the rest of the data
    target = df['class']
    df = df.drop(columns=['class'])

    # Scale numerical features (excluding 'class')
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Encode categorical features
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    categorical_cols = df.select_dtypes(include=['category']).columns
    encoded_features = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))

    # Combine scaled numerical features, encoded categorical features, and the target variable
    df = pd.concat([df.drop(columns=categorical_cols), encoded_df], axis=1)
    df['class'] = (target > 0).astype(int)  # Ensure 'class' is binary (0 or 1)

    return df