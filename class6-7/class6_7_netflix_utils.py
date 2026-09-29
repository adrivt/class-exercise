from pathlib import Path
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug("Dataframe shape: %s", df.shape)
    print("First 5 rows: %s", df.head())
    print("Column names: %s", df.columns)
    print(df.info())
    print(df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before= len(df)
    df=df.drop_duplicates()
    after=len(df)
    logger.debug("Before: %s, After: %s", before, after)
    return df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before=len(df)
    no_nas=df.dropna()
    after=len(no_nas)
    df=no_nas
    logger.debug("Before: %s, After: %s", before, after)
    return df