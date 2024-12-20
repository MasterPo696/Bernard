import re
import random
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from data.nets.crypto.net import crypto_net
from data.nets.weather.net import weather_net




def main():
    # crypto_net()
    weather_net()
    return


if __name__ == "__main__":
    main()
