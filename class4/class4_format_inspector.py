import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # 
    # TODO:
    df = pd.read_csv("sample.csv")
    logger.info("Filepath:", filepath)
    df.head(3)
    


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TODO:
    with open("sample.json", "r") as f:
        data = json.load(f)
    logger.info("Filepath:", filepath)
    print(data)


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # TODO:
    with open("sample.yaml", "r") as f:
        config = yaml.safe_load(f)
    logger.info("Filepath:", filepath)
    print(config)
    


def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    logging.info(".env is loaded.")
    print(os.getenv("USERNAME"))
    # Do not print passwords, API keys, or other secret values.


def main():
    # TODO:
    data_dir = Path('data')
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    csv_path = data_dir / "sample.csv"
    json_path = data_dir / "sample.json"
    yaml_path = data_dir / "sample.yaml"
    # 3. Call each inspection function using the matching path.
    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)
    # 4. Call inspect_env() without an argument.
    inspect_env()


if __name__ == "__main__":
    main()