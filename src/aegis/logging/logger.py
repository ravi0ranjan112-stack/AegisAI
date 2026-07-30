import logging
from pathlib import Path


class Logger:
    _configured = False

    @classmethod
    def setup(cls) -> logging.Logger:
        if cls._configured:
            return logging.getLogger("aegis")

        Path("logs").mkdir(exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)-8s | %(message)s",
            handlers=[
                logging.FileHandler("logs/aegis.log"),
                logging.StreamHandler(),
            ],
        )

        cls._configured = True
        return logging.getLogger("aegis")
