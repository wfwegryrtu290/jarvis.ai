from datetime import datetime
import traceback


class Logger:

    def _log(self, level, text):

        print(f"[{level} {datetime.now():%Y-%m-%d %H:%M:%S}] {text}")

    def debug(self, text):

        self._log("DEBUG", text)

    def info(self, text):

        self._log("INFO", text)

    def warning(self, text):

        self._log("WARNING", text)

    def error(self, text):

        self._log("ERROR", text)

    def critical(self, text):

        self._log("CRITICAL", text)

    def exception(self, text):

        self._log("EXCEPTION", text)
        traceback.print_exc()


logger = Logger()