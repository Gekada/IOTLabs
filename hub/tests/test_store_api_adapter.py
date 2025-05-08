import requests
import unittest
from unittest.mock import Mock, patch
from app.adapters.store_api_adapter import StoreApiAdapter
from app.entities.agent_data import AccelerometerData, AgentData, GpsData
from app.entities.processed_agent_data import ProcessedAgentData

class TestStoreApiAdapter(unittest.TestCase):
    def setUp(self):
        # Create the StoreApiAdapter instance
        self.store_api_adapter = StoreApiAdapter(api_base_url="http://test-api.com")
    @patch.object(requests, "post")
    def test_save_data_success(self, mock_post):
        # Test successful saving of data to the Store API
        # Sample processed road data
        agent_data = AgentData(
            user_id=1,
            accelerometer=AccelerometerData(
                x=0.1,
                y=0.2,
                z=0.3,
            ),
            gps=GpsData(
                latitude=10.123,
                longitude=20.456,
            ),
            timestamp="2023-07-21T12:34:56Z",
        )
        processed_data = ProcessedAgentData(road_state="normal", agent_data=agent_data)
        # Mock the response from the Store API
        mock_response = Mock(status_code=201)  # 201 indicates successful creation
        mock_post.return_value = mock_response
        # Call the save_data method
        result = self.store_api_adapter.save_data(processed_data)
        # Ensure that the post method of the mock is called with the correct arguments
        mock_post.assert_called_once_with(
            "http://test-api.com/agent_data", json=processed_data.model_dump()
        )
        # Ensure that the result is True, indicating successful saving
        self.assertTrue(result)
    @patch.object(requests, "post")
    def test_save_data_failure(self, mock_post):
        # Test failure to save data to the Store API
        # Sample processed road data
        agent_data = AgentData(
            user_id=1,
            accelerometer=AccelerometerData(
                x=0.1,
                y=0.2,
                z=0.3,
            ),
            gps=GpsData(
                latitude=10.123,
                longitude=20.456,
            ),
            timestamp="2023-07-21T12:34:56Z",
        )
        processed_data = ProcessedAgentData(road_state="normal", agent_data=agent_data)
        # Mock the response from the Store API
        mock_response = Mock(status_code=400)  # 400 indicates a client error
        mock_post.return_value = mock_response
        # Call the save_data method
        result = self.store_api_adapter.save_data(processed_data)
        # Ensure that the post method of the mock is called with the correct arguments
        mock_post.assert_called_once_with(
            "http://test-api.com/agent_data", json=processed_data.model_dump()
        )
        # Ensure that the result is False, indicating failure to save
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
