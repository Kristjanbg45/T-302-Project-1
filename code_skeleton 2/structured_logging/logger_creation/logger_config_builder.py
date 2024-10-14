from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink
from structured_logging.sinks.consolesink import ConsoleSink
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.sinks.filesink import FileSink  





class LoggerConfigBuilder:
    def __init__(self):
        self.sink: ISink = ConsoleSink()
        #set the default to consolesink
        self.processor: IProcessor = NullProcessor()
        #set the default to nullprocessor
        self.is_async: bool = False
        #sets the default to synchronous
        self.async_wait_delay_in_seconds: int = 0
        #starts at 0 seconds

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        """just use the custom sink for logging"""
        self.sink = sink
        return self
        

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        """uses a filesink for a file path"""
        self.sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        """uses a console sink for a filepath"""
        self.sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder': 
        """puts async with specified delay"""
        self.is_async = True
        self.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        """makes the environment in the log"""
        self.environment = environment
        return self


    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        """adds a processor to the log"""
        self.processor = processor
        return self

    def _clear(self):
        """resets all of the config to default"""
        self.sink = ConsoleSink()
        self.processor = NullProcessor()
        self.is_async = False
        self.async_wait_delay_in_seconds = 0
        self.environment = Environment
        

    def build(self) -> LoggerConfig:
        """builds the loggerconfig setup"""
        return LoggerConfig(
            sink=self.sink,
            processor=self.processor,
            is_async=self.is_async,
            async_wait_delay_in_seconds=self.async_wait_delay_in_seconds,
            environment=self.environment
        )











