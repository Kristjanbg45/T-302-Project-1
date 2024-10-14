
from .abstract_processor import AbstractProcessor



class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment: str, next_processor=None):
        """
        Initializes the processor with the specified environment.
        
        :param environment: The environment string (e.g., 'production').
        :param next_processor: The next processor in the chain (optional).
        """
        super().__init__(next_processor)
       
       
        self.environment = environment



    def handle(self, log_data: dict) -> dict:
        """
        Adds the environment information to the log data.
        
        :param log_data: The log data dictionary.
        :return: Log data with the added environment.
        """
        log_data['environment'] = self.environment
        return log_data
    

    







