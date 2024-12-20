import re
import random
import numpy as np
import matplotlib.pyplot as plt
from data.nets.utils.preparete import prepare_data
from data.nets.utils.wordmaker import generate_phrases
from data.nets.weather.words import extended_word_list, value_list, metrics_list, EPOCHS, VOCAB_SIZE
from data.nets.utils.drawer import draw_results
from data.nets.utils.compiler import CryptoModelTrainer
DATA_PATH = "/Users/masterpo/Desktop/Bernard/data/weigths/weather/"

def weather_net():
    trainer = CryptoModelTrainer(vocab_size=VOCAB_SIZE)
    # Подготовка данных
    X_train, X_test, y_train, y_test = trainer.prepare_data(extended_word_list, value_list, metrics_list)
    num_classes = len(trainer.label_encoder.classes_)

    # Создание и обучение модели
    trainer.model = trainer.create_model(num_classes=num_classes)
    history = trainer.model.fit(
        X_train, y_train,
        epochs=EPOCHS,
        batch_size=32,
        validation_data=(X_test, y_test),
        verbose=1
    )

    # Сохраняем веса модели
    trainer.model.save_weights(DATA_PATH+"model_weights.h5")
    print("Веса модели сохранены в model_weights.h5")

    # Загружаем веса в новую модель
    trainer.load_weights_into_new_model(DATA_PATH)

    # Отрисовываем результаты
    draw_results(history)

    # Предсказания из консоли
    print("\nВведите фразу для предсказания (пустая строка для выхода):")
    while True:
        user_input = input("> ")
        if user_input.strip() == "":
            break
        predicted = trainer.predict_class(user_input)
        print(f"Предсказанный класс: {predicted}")


