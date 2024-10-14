
from injector import Module, Binder, singleton

from structured_logging.configuration.logger_config import LoggerConfig


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    def configure(self, binder: Binder) -> None:
        # Bind LoggerConfig to the provided instance as a singleton
        binder.bind(LoggerConfig, to=self.__logger_config, scope=singleton)
        
        # Example: Bind an interface to its implementation
        # binder.bind(ISomeService, to=SomeService, scope=singleton)
        
        # You can bind other dependencies similarly
