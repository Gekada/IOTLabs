import logging
from app.adapters.agent_mqtt_adapter import AgentMQTTAdapter
from app.adapters.hub_http_adapter import HubHttpAdapter
from app.adapters.hub_mqtt_adapter import HubMqttAdapter
from config import (
    MQTT_BROKER_HOST,
    MQTT_BROKER_PORT,
    MQTT_TOPIC,
    HUB_URL,
    HUB_MQTT_BROKER_HOST,
    HUB_MQTT_BROKER_PORT,
    HUB_MQTT_TOPIC,
)

if __name__ == "__main__":
    # Configure logging settings
    logging.basicConfig(
        level=logging.INFO,  # Set the log level to INFO (you can use logging.DEBUG for more detailed logs)
        format="[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s",
        handlers=[
            logging.StreamHandler(),  # Output log messages to the console
            logging.FileHandler("app.log"),  # Save log messages to a file
        ],
    )
    # Create an instance of the StoreApiAdapter using the configuration
    # hub_adapter = HubHttpAdapter(
    #     api_base_url=HUB_URL,
    # )
    hub_adapter = HubMqttAdapter(
        broker=HUB_MQTT_BROKER_HOST,
        port=HUB_MQTT_BROKER_PORT,
        topic=HUB_MQTT_TOPIC,
    )
    # Create an instance of the AgentMQTTAdapter using the configuration
    agent_adapter = AgentMQTTAdapter(
        broker_host=MQTT_BROKER_HOST,
        broker_port=MQTT_BROKER_PORT,
        topic=MQTT_TOPIC,
        hub_gateway=hub_adapter,
    )
    try:
        # Connect to the MQTT broker and start listening for messages
        agent_adapter.connect()
        agent_adapter.start()
        # Keep the system running indefinitely (you can add other logic as needed)
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the MQTT adapter and exit gracefully if interrupted by the user
        agent_adapter.stop()
        logging.info("System stopped.")
