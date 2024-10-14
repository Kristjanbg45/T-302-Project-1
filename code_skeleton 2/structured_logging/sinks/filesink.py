import json
from .i_sink import ISink

class FileSink(ISink):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def sink_data(self, data: dict):
        """Implements the sink_data method to log data to a file."""
        with open(self.file_path, 'a') as file:
            file.write(json.dumps(data) + '\n')
