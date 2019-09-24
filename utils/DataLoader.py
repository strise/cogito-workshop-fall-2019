from datetime import date, timedelta

import pandas as pd
from typing import List
import os

from model.TimestampedText import TimestampedText


class DataLoader:
    data_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data"))

    @staticmethod
    def load_dataset_from_file() -> List[TimestampedText]:
        path = os.path.join(DataLoader.data_dir, "dataset.csv")
        column_names = ["published", "text"]
        data = pd.read_csv(path, delimiter=";", names=column_names)
        dataset = []
        for _, row in data.iterrows():
            entry = TimestampedText(row["text"], row["published"])
            dataset.append(entry)
        return dataset

    @staticmethod
    def load_stopwords_file() -> List[str]:
        path = os.path.join(DataLoader.data_dir, "eng_stopwords.txt")
        column_names = ["sw"]
        data = pd.read_csv(path, names=column_names)
        stopwords = []
        for _, row in data.iterrows():
            stopwords.append(row["sw"])
        return stopwords

    @staticmethod
    def load_utd_results() -> List[float]:
        file = open(os.path.join(DataLoader.data_dir, "man_utd_points_per_week.csv"), "r")
        points_per_week = []
        for line in file.readlines():
            points_per_week.append(float(line))
        return points_per_week
