import json
from .i_sink import ISink

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        """Implements the sink_data method to log data to the console."""
        print(json.dumps(data))
