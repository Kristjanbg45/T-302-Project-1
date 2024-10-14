from client.infrastructure.settings.settings import Settings, LoggingType
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


def create_logger_config(settings: Settings, builder: LoggerConfigBuilder) -> LoggerConfig:
    if settings.logging_type == LoggingType.FILE:
        builder.set_sink("FileSink").set_file_path(settings.logging_file_path)
    else:
        builder.set_sink("ConsoleSink")
    
    # Set the processor, e.g., TimestampProcessor for adding timestamps
    builder.set_processor("TimestampProcessor")
    
    # Configure asynchronous logging if enabled in settings
    builder.set_is_async(settings.logging_is_async)
    builder.set_async_wait_delay_in_seconds(settings.logging_async_delay)
    
    # Optionally, you can also pass the environment (development, staging, production)
    builder.set_processor("EnvironmentProcessor").set_environment(settings.environment.value)
    
    # Build and return the logger configuration
    return builder.build()
