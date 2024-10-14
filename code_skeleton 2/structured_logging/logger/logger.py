from typing import Any, Iterable
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig


class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue

    def log(self, **kwargs: Iterable[Any]):
        processed_data = kwargs
        processor = self.__logger_config.processor

        while processor is not None:
            processed_data = processor.process(processed_data)
            processor = processor.next_processor

        # Step 2: Create the logging command
        if self.__logger_config.is_async:
            # Create a command to add to the queue
            self.__logging_queue.add_command(self.__create_logging_command(processed_data))
        else:
            # Log synchronously
            self.__log_to_sink(processed_data)

    def __log_to_sink(self, log_data: dict):
        """Logs the data to the configured sink."""
        self.__logger_config.sink.sink_data(log_data)

    def __create_logging_command(self, log_data: dict):
        """Creates a command to log the data asynchronously."""
        def command():
            self.__log_to_sink(log_data)
        return command
