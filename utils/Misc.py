from typing import List

from model.TimestampedText import TimestampedText
from datetime import date, timedelta


def sort_entries_by_date(dataset: List[TimestampedText], oldest_first=True) -> List[TimestampedText]:
    return sorted(dataset, key=lambda x: x.published, reverse=(not oldest_first))


def group_entries_by_week(dataset: List[TimestampedText]) -> List[List[TimestampedText]]:
    def get_next_monday(some_date: date) -> date:
        if some_date.weekday() == 0:
            some_date = some_date + timedelta(days=1)
        return some_date + timedelta(days=(0 - some_date.weekday()) % 7)

    if dataset:
        sorted_dataset = sort_entries_by_date(dataset)
        oldest = sorted_dataset[0]
        oldest_date = date.fromtimestamp(oldest.published / 1000)
        previous_monday = oldest_date - timedelta(days=oldest_date.weekday())
        grouped_by_week = []
        num_added = 0
        while num_added < len(sorted_dataset):
            next_monday = get_next_monday(previous_monday)
            this_week = [
                s for s in sorted_dataset if previous_monday <= date.fromtimestamp(s.published / 1000) < next_monday
            ]
            grouped_by_week.append(this_week)
            previous_monday = next_monday
            num_added += len(this_week)
        return grouped_by_week
    else:
        return [[]]
