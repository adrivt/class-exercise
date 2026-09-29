import argparse
import logging
import sys
from pathlib import Path
import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    # Create a Path object from args.input.
    data_path = Path(args.input)
    # Inside a try block, load that path using pd.read_csv().
    try: 
        df = pd.read_csv(data_path)
        logger.info("Successfully loaded data from %s", data_path)
    except FileNotFoundError:
        logger.error("File not found: %s", data_path)
        sys.exit(1)
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.

    # TODO 5:
    # Call show_overview().
    # Log an INFO message.
    show_overview(df)
    logger.info("Displayed overview of the data")

    # TODO 6:
    # Call remove_duplicates().
    df = remove_duplicates(df)
    logger.info("Removed duplicates, remaining rows: %s", len(df))

    # Call drop_missing_rows().
    df = drop_missing_rows(df)
    logger.info("Dropped rows with missing values, remaining rows: %s", len(df))

if __name__ == "__main__":
    main()
