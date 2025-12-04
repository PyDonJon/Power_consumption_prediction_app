from pydantic import BaseModel

class ConsumptionRequest(BaseModel):
    year: int
    month: int
    day: int
    hour: int

class ConsumptionResponse(BaseModel):
    consumption_volume: float    