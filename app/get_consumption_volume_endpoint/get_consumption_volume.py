from fastapi import APIRouter, Request

from .schemas import ConsumptionRequest,ConsumptionResponse

import pandas as pd

router = APIRouter(
    prefix="/consumption"
)

@router.post("/volume")
async def get_consumption_prediction(request: Request,consumption_request: ConsumptionRequest):

    consumption_model = request.app.state.consumption_model

    feature_space ={
        "Year":[consumption_request.year],
        "Month":[consumption_request.month],
        "Day":[consumption_request.day],
        "Hour":[consumption_request.hour]
    }

    transformed_feature_space = pd.DataFrame.from_dict(feature_space)

    consumption_volume = consumption_model.predict(transformed_feature_space)

    return ConsumptionResponse(consumption_volume=consumption_volume)