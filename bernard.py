import logging
import hashlib


class Bernard:
    def __init__(self, name, version):
        self.__name = name  # Приватный атрибут
        self.__version = version  # Приватный атрибут
        self.__tasks = []  # Список задач
        self.__logs = []  # Логирование действий
        self.__stop_word_hash = None  # Хэш стоп-слова

    # Приватные методы
    def __log_action(self, action):
        """Логирует действия робота."""
        self.__logs.append(action)

    def __hash_stop_word(self, stop_word):
        """Хэширует стоп-слово."""
        return hashlib.sha256(stop_word.encode()).hexdigest()

    # Публичные методы
    def add_stop_word(self, stop_word):
        """Добавляет стоп-слово."""
        hashed = self.__hash_stop_word(stop_word)
        if hashed in self.__stop_words:
            return f"Стоп-слово '{stop_word}' уже добавлено."
        self.__stop_words[hashed] = stop_word
        self.__log_action(f"Stop word added: {stop_word}")
        return f"Стоп-слово '{stop_word}' добавлено."

    def remove_stop_word(self, stop_word):
        """Удаляет стоп-слово."""
        hashed = self.__hash_stop_word(stop_word)
        if hashed in self.__stop_words:
            del self.__stop_words[hashed]
            self.__log_action(f"Stop word removed: {stop_word}")
            return f"Стоп-слово '{stop_word}' удалено."
        return f"Стоп-слово '{stop_word}' не найдено."

    def list_stop_words(self):
        """Возвращает список стоп-слов."""
        self.__log_action("Listed stop words")
        if not self.__stop_words:
            return "Стоп-слова отсутствуют."
        return "Стоп-слова:\n" + "\n".join(self.__stop_words.values())

    def parse_text(self, text):
        """Парсит текст и ищет стоп-слова."""
        self.__log_action(f"Parsed text: {text}")
        detected = [
            word for word in text.split() if self.__hash_stop_word(word) in self.__stop_words
        ]
        if detected:
            return f"Обнаружены стоп-слова: {', '.join(detected)}"
        return "Стоп-слова не найдены в тексте."

    def greet(self):
        """Приветствие пользователя."""
        self.__log_action("Greeting user")
        return f"Привет! Я {self.__name}, твой помощник версии {self.__version}."

    def add_task(self, task):
        """Добавление задачи в список задач."""
        self.__log_action(f"Task added: {task}")
        self.__tasks.append(task)
        return f"Задача '{task}' добавлена."

    def list_tasks(self):
        """Вывод списка задач."""
        self.__log_action("Listed tasks")
        if not self.__tasks:
            return "У вас пока нет задач."
        return "Ваши задачи:\n" + "\n".join(f"- {task}" for task in self.__tasks)

    def complete_task(self, task):
        """Завершение задачи."""
        if task in self.__tasks:
            self.__tasks.remove(task)
            self.__log_action(f"Task completed: {task}")
            return f"Задача '{task}' выполнена."
        else:
            self.__log_action(f"Attempted to complete non-existing task: {task}")
            return f"Задача '{task}' не найдена."

    def fetch_date_time(self):
        """Получение текущей даты и времени."""
        from datetime import datetime
        self.__log_action("Fetched date and time")
        now = datetime.now()
        return now.strftime("Сегодня: %d.%m.%Y, время: %H:%M:%S")

    def help(self):
        """Список доступных команд."""
        self.__log_action("Displayed help")
        return (
            "Команды:\n"
            "- greet(): приветствие.\n"
            "- add_task(task): добавить задачу.\n"
            "- list_tasks(): список задач.\n"
            "- complete_task(task): завершить задачу.\n"
            "- fetch_date_time(): текущее время.\n"
            "- add_stop_word(word): добавить стоп-слово.\n"
            "- remove_stop_word(word): удалить стоп-слово.\n"
            "- list_stop_words(): список стоп-слов.\n"
            "- parse_text(text): парсинг текста на наличие стоп-слов.\n"
            "- help(): помощь."
        )

    def get_logs(self):
        """Получение логов действий."""
        return "\n".join(self.__logs)


# Пример использования
if __name__ == "__main__":
    bot = Bernard("RoboHelper", "1.0")
    print(bot.greet())
    print(bot.add_stop_word("стоп"))
    print(bot.add_stop_word("анализ"))
    print(bot.list_stop_words())
    print(bot.parse_text("Это текст для анализа с ключевым словом стоп."))
    print(bot.parse_text("Тут ничего такого нет."))
    print(bot.remove_stop_word("анализ"))
    print(bot.list_stop_words())
    print(bot.get_logs())
