# Гиперпараметры
VOCAB_SIZE = 2000
EPOCHS = 2
PHRASES_PER_CLASS = 500
EMBED_DIM = 16
LSTM_UNITS = 64
EXTRA_LSTM = False

# Топ-25 криптовалют
value_list = [
    "bitcoin", "ethereum", "tether", "binance", "usdcoin", "xrp", "solana", "cardano",
    "avalanche", "polkadot", "dogecoin", "shibainu", "polygon", "tron", "uniswap",
    "cosmos", "litecoin", "chainlink", "near", "ftx", "bitcoincash", "stellar", 
    "algorand", "vechain", "filecoin"
]

# Метрики
metrics_list = ["price", "market cap", "volume", "circulating supply", "max supply"]

# Список слов
extended_word_list = [
    "send", "fetch", "check", "price", "rate", "cost", "transfer", "value", 
    "market", "update", "compare", "info", "details", "show", "get", "pull", 
    "pr", "vol", "mcap", "csupply", "msupply", "stats", "data", "req", "ask"
]
