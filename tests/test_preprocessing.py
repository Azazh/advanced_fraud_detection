import pandas as pd
from src.preprocessing import handle_missing_values, clean_data

def test_handle_missing_values():
    df = pd.DataFrame({'A': [1, None, 3], 'B': ['x', 'y', None]})
    result = handle_missing_values(df)
    assert result.isnull().sum().sum() == 0

def test_clean_data():
    df = pd.DataFrame({'signup_time': ['2023-01-01', '2023-02-01'], 'purchase_time': ['2023-01-02', None]})
    result = clean_data(df)
    assert result['purchase_time'].isnull().sum() == 0