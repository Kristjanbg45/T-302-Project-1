import json
from .i_sink import ISink

class FileSink(ISink):
    def __init__(self, file_path: str): #here all the logs will be written
        self.file_path = file_path

    def sink_data(self, data: dict):
        """Implements the sink_data method to log data to a file."""

        #we might need try and except here? append mode
        with open(self.file_path, 'a') as file:
            file.write(json.dumps(data) + '\n')
