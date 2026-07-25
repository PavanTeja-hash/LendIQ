"""Load the raw loan dataset and clean it: missing values, duplicates, outliers."""

import pandas as pd

RAW_PATH = "data/raw/credit_risk_dataset.csv"
PROCESSED_PATH = "data/processed/credit_risk_clean.csv"


def load_raw_data(path: str = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    # Data-entry error: 5 rows report an implausible age (max was 144).
    df = df[df["person_age"] <= 100]

    # person_emp_length: drop the 887 rows missing this value, then the 2 rows
    # with implausible values (max was 123 years). Dropping is acceptable here
    # because together they are under 3% of the data.
    df = df.dropna(subset=["person_emp_length"])
    df = df[df["person_emp_length"] <= 60]

    # loan_int_rate is missing for ~9.6% of rows - too many to drop. Interest rate
    # is strongly determined by loan grade (median 7.5% for A vs 20.2% for G), so
    # impute each missing value with the median rate of its own grade rather than
    # a single global median.
    df["loan_int_rate"] = df.groupby("loan_grade")["loan_int_rate"].transform(
        lambda s: s.fillna(s.median())
    )

    return df.reset_index(drop=True)


def save_processed_data(df: pd.DataFrame, path: str = PROCESSED_PATH) -> None:
    df.to_csv(path, index=False)


if __name__ == "__main__":
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    save_processed_data(clean_df)
    print(f"Raw rows: {len(raw_df)} -> Cleaned rows: {len(clean_df)}")
    print(f"Missing values left:\n{clean_df.isnull().sum()[clean_df.isnull().sum() > 0]}")
