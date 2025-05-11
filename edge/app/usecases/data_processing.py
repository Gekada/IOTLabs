from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    road_state: str = "normal"

    value = agent_data.accelerometer.z

    if value <= 15000:
        road_state = "pothole"
    elif value >= 17000:
        road_state = "bump"

    return ProcessedAgentData(road_state=road_state, agent_data=agent_data)