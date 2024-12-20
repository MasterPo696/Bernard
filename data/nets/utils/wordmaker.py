import random, re

def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower().strip()

def random_case(word):
    """Случайно меняем регистр слова для большего разнообразия."""
    return word.lower() if random.random() < 0.5 else word.upper()

def generate_phrases(word_list, value_list, metrics_list, phrases_per_class=50):
    """
    Генерирует фразы, содержащие криптовалюту, метрику и случайные слова.
    """
    phrases = []
    for value in value_list:
        for metric in metrics_list:
            for _ in range(phrases_per_class):
                num_words = random.randint(1, 5)  
                chosen_words = random.sample(word_list, min(num_words, len(word_list)))

                chosen_words = [random_case(w) for w in chosen_words]
                val_word = random_case(value)
                met_word = random_case(metric)

                phrase_words = chosen_words + [val_word, met_word]
                random.shuffle(phrase_words)
                phrase = " ".join(phrase_words)
                
                # Метка: криптовалюта_метрика (нижний регистр)
                label = f"{value}_{metric.replace(' ', '_')}"
                phrases.append((phrase, label))
    return phrases
