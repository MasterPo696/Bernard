# Гиперпараметры
VOCAB_SIZE = 2000
EPOCHS = 2
PHRASES_PER_CLASS = 500
EMBED_DIM = 16
LSTM_UNITS = 64
EXTRA_LSTM = False

# Список мест (аналог значения криптовалюты)
value_list = [
    "paris", "london", "tokyo", "berlin", "madrid", "rome",
    "ottawa", "washington", "beijing", "moscow", "canberra",
    "brasilia", "new delhi", "cairo", "nairobi", "buenos aires",
    "jakarta", "bangkok", "seoul", "havana", "oslo", "stockholm"
]

# Параметры погоды (аналог метрик криптовалют)
metrics_list = [
    "temperature", "humidity", "rain", "wind", "cloudiness", 
    "forecast", "conditions", "pressure", "climate", "degrees"
]

# Расширенный список слов, используемый для генерации фраз
# Аналогично "extended_word_list" для крипты, но специфичнее для погоды/мест
extended_word_list = [
    "check", "fetch", "what", "weather", "show", "get", "pull", 
    "info", "details", "compare", "update", "data", "stats", 
    "conditions", "current", "forecast", "now", "request", "ask", "please"
]

# Пример фразы, которую может сгенерировать такая система:
# "what weather is in paris"
# Или, например: "fetch current temperature data berlin"
# "check forecast moscow now"
