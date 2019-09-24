from datetime import date
from typing import List, Any

import nltk
from textblob import TextBlob

from model.TimestampedText import TimestampedText
from utils.DataLoader import DataLoader
from utils.Misc import group_entries_by_week, sort_entries_by_date
from utils.Plotter import Plotter


def remove_junk_content(dataset: List[TimestampedText]) -> List[TimestampedText]:
    def is_junk(doc: TimestampedText) -> bool:
        pass

    smooth_content = [d for d in dataset if not is_junk(d)]
    return smooth_content


def filter_on_language(dataset: List[TimestampedText]) -> List[TimestampedText]:
    eng_stopwords = DataLoader.load_stopwords_file()

    def is_english(doc: TimestampedText) -> bool:
        pass

    eng_content = [d for d in dataset if is_english(d)]
    return eng_content


def relevant_sentences(dataset: List[TimestampedText]) -> List[TimestampedText]:
    ole_g_aliases = ["Solskjaer", "Solskjær"]

    def contains_phrase(sentence: str, phrases: List[str]) -> bool:
        pass

    timestamped_OGS_sentences = []
    for d in dataset:
        for sent in d.sentences():
            if contains_phrase(sent, ole_g_aliases):
                timestamped_OGS_sentences.append(TimestampedText(sent, d.published))

    return timestamped_OGS_sentences


def generate_sentiment_scores(timestamped_OGS_sentences: List[TimestampedText]) -> List[float]:
    sentences_from_previous_season = [
        o for o in timestamped_OGS_sentences
        if date(2018, 12, 18) < date.fromtimestamp(o.published / 1000) <= date(2019, 5, 13)
    ]
    grouped_by_week = group_entries_by_week(sentences_from_previous_season)
    pass


def most_used_adjectives(timestamped_OGS_sentences: List[TimestampedText]) -> List[str]:
    pass


def run_pipeline() -> List[TimestampedText]:
    dataset = DataLoader.load_dataset_from_file()
    print(f"Loaded dataset with {len(dataset)} entries")
    no_junk_in_my_trunk = remove_junk_content(dataset)
    print(f"Junk removal removed {len(dataset) - len(no_junk_in_my_trunk)}. {len(no_junk_in_my_trunk)} remaining.")
    only_english_entries = filter_on_language(no_junk_in_my_trunk)
    print(f"Language filter removed {len(no_junk_in_my_trunk) - len(only_english_entries)}. {len(only_english_entries)} remaining.")
    only_relevant = relevant_sentences(only_english_entries)
    print(len(only_relevant), "sentences selected.")
    return only_relevant


def plot_sentiment_against_utd_results(sentiment_per_week: List[float]) -> None:
    utd_results = DataLoader.load_utd_results()
    max_sent = max(sentiment_per_week)
    aligned_sentiment = [s / max_sent for s in sentiment_per_week]
    Plotter.dual_line_plot(aligned_sentiment, utd_results, labels=["sentiment", "ppw"])


if __name__ == "__main__":
    processed_items = run_pipeline()
    # Kommenter ut dersom du gjør oppgave 4, forslag 1
    # sentiment = generate_sentiment_scores(processed_items)
    # plot_sentiment_against_utd_results(sentiment)
    
    # Kommenter ut dersom du gjør oppgave 4, forslag 2
    # adjectives = most_used_adjectives(processed_items)
