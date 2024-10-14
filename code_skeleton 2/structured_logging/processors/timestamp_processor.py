

from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime

class TimestampProcessor(AbstractProcessor):
    def handle(self, log_data: dict) -> dict:
        """
        Adds the current timestamp to the log data.
        
        :param log_data: The log data dictionary.
        :return: Log data with the added timestamp.
        """
        log_data['timestamp'] = datetime.now().isoformat()  # Add current timestamp
        return log_data








