from structured_logging.command_queue.command import Command

class LoggingCommand(Command):
    def __init__(self, logger, log_data: dict):
        """sets up the logger and log data"""
        self.logger = logger  
        self.log_data = log_data  

    def execute(self):
        """Override the execute method to log data to the sink."""
        self.logger._log_to_sink(self.log_data)
