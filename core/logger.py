from datetime import datetime
from pathlib import Path
import traceback


class Logger:

    def __init__(self):

        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "jarvis.log"

    def _write_file(self, text):

        try:

            with self.log_file.open(
                "a",
                encoding="utf-8"
            ) as f:

                f.write(text + "\n")

        except Exception:
            pass

    def _log(self, level, text):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{level:<9} {timestamp}] {text}"

        print(line)

        self._write_file(line)

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

    def exception(self, error):

        self._log("EXCEPTION", str(error))

        trace = traceback.format_exc()

        print(trace)

        self._write_file(trace)

    def separator(self):

        self._write_file("-" * 80)

    def clear(self):

        try:

            self.log_file.write_text(
                "",
                encoding="utf-8"
            )

        except Exception:
            pass

    def path(self):

        return str(self.log_file)


logger = Logger()
