from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from data.nets.utils.wordmaker import clean_text
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from data.nets.crypto.words import VOCAB_SIZE, PHRASES_PER_CLASS, EMBED_DIM ,LSTM_UNITS, EXTRA_LSTM
from data.nets.utils.wordmaker import generate_phrases




class CryptoModelTrainer:
    def __init__(self, vocab_size=VOCAB_SIZE):
        self.vocab_size = vocab_size
        self.model = None
        self.tokenizer = None
        self.label_encoder = None
        self.input_length = None

    def prepare_data(self, word_list, value_list, metrics_list, phrases_per_class=PHRASES_PER_CLASS):
        data = generate_phrases(word_list, value_list, metrics_list, phrases_per_class=phrases_per_class)
        texts = [clean_text(item[0]) for item in data]
        labels = [item[1] for item in data]

        # Кодирование меток
        label_encoder = LabelEncoder()
        encoded_labels = label_encoder.fit_transform(labels)

        # Токенизация
        tokenizer = Tokenizer(num_words=self.vocab_size, oov_token="<OOV>")
        tokenizer.fit_on_texts(texts)
        sequences = tokenizer.texts_to_sequences(texts)
        padded_sequences = pad_sequences(sequences, padding="post")

        X_train, X_test, y_train, y_test = train_test_split(
            padded_sequences, encoded_labels, test_size=0.2, random_state=42
        )

        self.label_encoder = label_encoder
        self.tokenizer = tokenizer
        self.input_length = padded_sequences.shape[1]

        return X_train, X_test, y_train, y_test

    def create_model(self, embed_dim=EMBED_DIM, input_length=None, num_classes=None, lstm_units=LSTM_UNITS, extra_lstm=EXTRA_LSTM):
        if input_length is None:
            input_length = self.input_length
        model = Sequential()
        model.add(Embedding(self.vocab_size, embed_dim, input_length=input_length))
        model.add(LSTM(lstm_units, return_sequences=extra_lstm))
        # Без второго LSTM слоя, т.к. extra_lstm=False
        model.add(Dense(32, activation="relu"))
        model.add(Dense(num_classes, activation="softmax"))
        model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        return model

    def predict_class(self, text):
        cleaned = clean_text(text)
        sequence = self.tokenizer.texts_to_sequences([cleaned])
        padded_sequence = pad_sequences(sequence, padding="post", maxlen=self.input_length)
        prediction = self.model.predict(padded_sequence)
        class_index = np.argmax(prediction)
        return self.label_encoder.inverse_transform([class_index])[0]

    def load_weights_into_new_model(self, DATA_PATH, embed_dim=EMBED_DIM, lstm_units=LSTM_UNITS, extra_lstm=EXTRA_LSTM):
        num_classes = len(self.label_encoder.classes_)
        new_model = self.create_model(embed_dim, self.input_length, num_classes, lstm_units, extra_lstm)
        new_model.load_weights(DATA_PATH+"model_weights.h5")
        self.model = new_model
        print("Веса успешно загружены в новую модель.")
