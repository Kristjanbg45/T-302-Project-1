

#FIX


from typing import Any, Iterable
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger_command import LoggingCommand


class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue

    def log(self, **kwargs: Iterable[Any]):
        processed_data = kwargs
        processor = self.__logger_config.processor

        #process through all processors
        while processor is not None:
            processed_data = processor.process(processed_data)
            processor = processor.next_processor


        if self.__logger_config.is_async:
            #add command to the queue
            command = LoggingCommand(self, processed_data)
            self.__logging_queue.add(command)
        else:
            #synchronous log
            self.__log_to_sink(processed_data)

    def __log_to_sink(self, log_data: dict):
        self.__logger_config.sink.sink_data(log_data)


