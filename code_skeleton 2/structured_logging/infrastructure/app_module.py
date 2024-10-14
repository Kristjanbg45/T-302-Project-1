from injector import Module, provider, singleton
from structured_logging.sinks.consolesink import ConsoleSink
from structured_logging.sinks.filesink import FileSink
from structured_logging.logger.logger import Logger
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.command_queue.queue import Queue





#uses singleton and provider for DI

class AppModule(Module):

    @singleton
    @provider
    def provide_queue(self) -> Queue:
        """sets the delay to 2 secs"""
        return Queue(async_delay_seconds = 2)



    @singleton
    @provider
    def provide_logger_config(self) -> LoggerConfig:
        """sets an instance of config"""
        sink = ConsoleSink()  #we can also use filesink
        processor = NullProcessor()
        return LoggerConfig(
            sink=sink,
            processor=processor,
            is_async=True,
            async_wait_delay_in_seconds=2
        )

    @singleton
    @provider
    def provide_logger(self, queue: Queue, logger_config: LoggerConfig) -> Logger:
        """logger instance using the queue and config"""
        return Logger(logger_config=logger_config, logging_queue=queue)
    


    



