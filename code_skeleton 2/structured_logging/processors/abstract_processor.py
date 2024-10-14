#here we will make a abstract method to implement the other processors using template method.

from i_processor import IProcessor

class AbstractProcessor(IProcessor):
    def __init__(self):
        self._next_processor = None

    def set_next(self, processor: 'IProcessor') -> 'IProcessor':
        """
        Sets the next processor in the chain.
        
        :param processor: The next processor to be called in the chain.
        :return: The next processor.
        """
        self._next_processor = processor
        return processor  # Returning this allows chaining easily

    def handle(self, data: dict) -> dict:
        """
        Passes the log data to the next processor in the chain if it exists.
        
        :param data: The log data dictionary to be processed.
        :return: Processed log data.
        """
        if self._next_processor:
            return self._next_processor.handle(data)
        return data  # If no next processor, return the data as-is





#AbstractProcessor: Implements the core functionality for chaining processors.
#NullProcessor: Does nothing, acting as a placeholder or default processor.
#TimestampProcessor: Adds a timestamp to the log data.
#EnvironmentProcessor: Adds environment information (such as "production" or "development").
#Usage: You can chain processors together and modify log data step-by-step.