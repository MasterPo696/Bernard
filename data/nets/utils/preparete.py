from data.nets.utils.wordmaker import generate_phrases, clean_text

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from config import VOCAB_SIZE

def prepare_data(word_list, value_list, metrics_list, phrases_per_class=500, vocab_size=VOCAB_SIZE):
    """
    Увеличили phrases_per_class и vocab_size для более богатого словаря.
    """
    data = generate_phrases(word_list, value_list, metrics_list, phrases_per_class=phrases_per_class)
    texts = [clean_text(item[0]) for item in data]
    labels = [item[1] for item in data]

    # Кодирование меток
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)

    # Токенизация
    tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, padding="post")

    X_train, X_test, y_train, y_test = train_test_split(
        padded_sequences, encoded_labels, test_size=0.2, random_state=42
    )

    return (X_train, X_test, y_train, y_test, tokenizer, label_encoder, padded_sequences)


