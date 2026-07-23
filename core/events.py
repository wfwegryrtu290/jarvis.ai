from core.logger import logger


class EventBus:

    def __init__(self):

        self.listeners = {}

    def subscribe(self, event, callback):
        """
        Регистрира слушател за събитие.
        """

        if event not in self.listeners:
            self.listeners[event] = []

        if callback not in self.listeners[event]:
            self.listeners[event].append(callback)

    def unsubscribe(self, event, callback):
        """
        Премахва слушател.
        """

        if event not in self.listeners:
            return

        if callback in self.listeners[event]:
            self.listeners[event].remove(callback)

            if not self.listeners[event]:
                del self.listeners[event]

    def emit(self, event, data=None):
        """
        Изпраща събитие към всички слушатели.
        """

        listeners = self.listeners.get(event, [])

        logger.debug(f"📡 Event: {event}")

        for callback in listeners:

            try:
                callback(data)

            except Exception as e:
                logger.exception(e)

    def clear(self):
        """
        Изчиства всички слушатели.
        """

        self.listeners.clear()

    def has_event(self, event):

        return event in self.listeners

    def events(self):

        return list(self.listeners.keys())

    def count(self):

        return len(self.listeners)

    def listener_count(self, event):

        return len(self.listeners.get(event, []))


bus = EventBus()
