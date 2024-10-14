from .abstract_processor import AbstractProcessor


class NullProcessor(AbstractProcessor):
    def handle(self, log_data: dict) -> dict:
        """
        This processor does nothing to the log data.
        
        :param log_data: The log data dictionary.
        :return: Unmodified log data.
        """
        return log_data
    



    