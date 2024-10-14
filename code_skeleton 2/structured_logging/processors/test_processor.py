from structured_logging.processors.timestamp_processor import TimestampProcessor
from structured_logging.processors.environment_processor import EnvironmentProcessor
from structured_logging.processors.null_processor import NullProcessor

# Create processors
timestamp_processor = TimestampProcessor()
environment_processor = EnvironmentProcessor("production")
null_processor = NullProcessor()

# Chain the processors together
timestamp_processor.set_next(environment_processor).set_next(null_processor)

# Create a log entry
log_entry = {
    "message": "A test log entry",
    "level": "info"
}

# Process the log entry through the processor chain
processed_log_entry = timestamp_processor.handle(log_entry)

# Print the processed log entry
print(processed_log_entry)
