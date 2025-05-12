from datetime import datetime
from pydantic import BaseModel, field_validator


class AccelerometerData(BaseModel):
    x: int
    y: int
    z: int


class GpsData(BaseModel):
    latitude: float
    longitude: float


class AgentData(BaseModel):
    accelerometer: AccelerometerData
    gps: GpsData
    timestamp: datetime
    user_id: int

    @classmethod
    @field_validator("timestamp", mode="before")
    def parse_timestamp(cls, value):
        # Convert the timestamp to a datetime object
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(value)
        except (TypeError, ValueError):
            raise ValueError(
                "Invalid timestamp format. Expected ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)."
            )