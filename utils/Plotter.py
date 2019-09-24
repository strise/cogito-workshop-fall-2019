import random
from typing import List
import matplotlib.pyplot as plt

from utils.DataLoader import DataLoader


class Plotter:
    @staticmethod
    def line_plot(datapoints: List[float]) -> None:
        plt.plot(datapoints)
        plt.show()

    @staticmethod
    def dual_line_plot(datapoints_a: List[float], datapoints_b: List[float], labels: List[str]) -> None:
        if len(labels) < 2:
            labels = ["A", "B"]
        plt.plot(datapoints_a, label=labels[0])
        plt.plot(datapoints_b, label=labels[1])
        plt.legend()
        plt.show()
