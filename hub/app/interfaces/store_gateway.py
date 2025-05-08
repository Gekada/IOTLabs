from abc import ABC, abstractmethod
from typing import List
from app.entities.processed_agent_data import ProcessedAgentData


class StoreGateway(ABC):
    """
    Abstract class representing the Store Gateway interface.
    All store gateway adapters must implement these methods.
    """

    @abstractmethod
    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        """
        Method to save the processed agent data in the database.
        Parameters:
            processed_agent_data_batch (ProcessedAgentData): The processed agent data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        pass
