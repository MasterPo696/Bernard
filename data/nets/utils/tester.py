from data.nets.crypto.words import extended_word_list


experiment_configs = [
    {
        "name": "HighEpochBase",
        "word_list": extended_word_list,
        "phrases_per_class": 500,
        "epochs": 2,
        "embed_dim": 16,
        "lstm_units": 64,
        "extra_lstm": False
    },
    {
        "name": "HighEpochExtraLSTM",
        "word_list": extended_word_list,
        "phrases_per_class": 500,
        "epochs": 2,
        "embed_dim": 16,
        "lstm_units": 64,
        "extra_lstm": True
    }
]


def net_tester_basic(value_list, metrics_list, extended_word_list, experiment_configs):
    # Настройки экспериментов: увеличим количество эпох для лучшего обучения
    
    experiment_configs = [
        {
            "name": "HighEpochBase",
            "word_list": extended_word_list,
            "phrases_per_class": 500,  # Больше фраз на класс
            "epochs": 2,              # Увеличили эпохи
            "embed_dim": 16,
            "lstm_units": 64,
            "extra_lstm": False
        },
        {
            "name": "HighEpochExtraLSTM",
            "word_list": extended_word_list,
            "phrases_per_class": 500,
            "epochs": 2,              # Еще больше эпох
            "embed_dim": 16,
            "lstm_units": 64,
            "extra_lstm": True
        }
    ]


    histories = []
    final_model = None
    final_tokenizer = None
    final_label_encoder = None
    final_input_length = None

    i = 0
    for config in experiment_configs:
        print(f"Запуск эксперимента: {config['name']}")
        X_train, X_test, y_train, y_test, tokenizer, label_encoder, padded_sequences = prepare_data(
            config["word_list"], value_list, metrics_list, phrases_per_class=config["phrases_per_class"], vocab_size=2000
        )
        input_length = padded_sequences.shape[1]
        num_classes = len(label_encoder.classes_)

        model = create_model(
            vocab_size=2000,
            embed_dim=config["embed_dim"],
            input_length=input_length,
            num_classes=num_classes,
            lstm_units=config["lstm_units"],
            extra_lstm=config["extra_lstm"]
        )

        history = model.fit(
            X_train, y_train,
            epochs=config["epochs"],
            batch_size=32,       # Можно немного увеличить batch_size, для ускорения
            validation_data=(X_test, y_test),
            verbose=1
        )
        histories.append((config["name"], history))
        
        # Сохраняем последнюю модель как "финальную"
        final_model = model
        final_tokenizer = tokenizer
        final_label_encoder = label_encoder
        final_input_length = input_length

    # Сохраняем веса финальной модели
    final_model.save_weights(f"model_weights{i}.h5")
    print("Веса модели сохранены в model_weights.h5")
