import logging
import json
import time


class JsonFormatter(
    logging.Formatter
):
    def format(
        self,
        record
    ):
        payload = {
            "timestamp": time.time(),
            "level": record.levelname,
            "message": record.getMessage()
        }

        return json.dumps(
            payload
        )


def get_logger(
    name: str
):
    logger = logging.getLogger(
        name
    )

    logger.setLevel(
        logging.INFO
    )

    handler = logging.StreamHandler()

    handler.setFormatter(
        JsonFormatter()
    )

    logger.addHandler(
        handler
    )

    return logger