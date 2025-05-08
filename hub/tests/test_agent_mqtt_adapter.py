import unittest
from unittest.mock import Mock
import redis
from app.adapters.agent_mqtt_adapter import AgentMQTTAdapter
from app.interfaces.store_gateway import StoreGateway
from app.entities.agent_data import AccelerometerData, AgentData, GpsData
from app.usecases.data_processing import process_agent_data_batch

class TestAgentMQTTAdapter(unittest.TestCase):
    def setUp(self):
        # Create a mock StoreGateway for testing
        self.mock_store_gateway = Mock(spec=StoreGateway)
        self.mock_redis = Mock(spec=redis.Redis)
        # Create the AgentMQTTAdapter instance with the mock StoreGateway
        self.agent_adapter = AgentMQTTAdapter(
            broker_host="test_broker",
            broker_port=1234,
            topic="test_topic",
            store_gateway=self.mock_store_gateway,
            redis_client=self.mock_redis,
            batch_size=1,
        )
    def test_on_message_valid_data(self):
        # Test handling of valid incoming MQTT message
        # (Assuming data is in the correct JSON format)
        valid_json_data = '{"user_id": 1,"accelerometer": {"x": 0.1, "y": 0.2, "z": 0.3}, "gps": {"latitude": 10.123, "longitude": 20.456}, "timestamp": "2023-07-21T12:34:56Z"}'
        mock_msg = Mock(payload=valid_json_data.encode("utf-8"))
        self.mock_redis.llen.return_value = 1
        self.mock_redis.rpop.return_value = valid_json_data
        # Call on_message with the mock message
        self.agent_adapter.on_message(None, None, mock_msg)
        # Ensure that the store_gateway's save_data method is called once with the correct arguments
        expected_agent_data = AgentData(
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
        self.mock_store_gateway.save_data.assert_called_once_with(
            process_agent_data_batch([expected_agent_data])
        )
    def test_on_message_invalid_data(self):
        # Test handling of invalid incoming MQTT message
        # (Assuming data is missing required fields or has incorrect format)
        invalid_json_data = '{"user_id": 1, "accelerometer": {"x": 0.1, "y": 0.2}, "gps": {"latitude": 10.123}, "timestamp": 12345}'
        mock_msg = Mock(payload=invalid_json_data.encode("utf-8"))
        # Call on_message with the mock message
        self.agent_adapter.on_message(None, None, mock_msg)
        # Ensure that the store_gateway's save_data method is not called (due to invalid data)
        self.mock_store_gateway.save_data.assert_not_called()

if __name__ == "__main__":
    unittest.main()
