from fastapi import APIRouter, HTTPException

from data.db import models
from schemas.models import MLModel, ModelUpdate

router = APIRouter(prefix='/models', tags=['Models'])


@router.get("/")
def get_all_models():
    return models


@router.post("/", status_code=201)
def create_model(model: MLModel):
    model_id = max(models, default=0) + 1
    models[model_id] = model
    return {"model_id": model_id, "model": model}


@router.get("/{model_id}")
def get_model(model_id: int):
    if model_id not in models:
        raise HTTPException(
            status_code=404, 
            detail='Not found'
        )
    return models[model_id]


@router.patch('/{model_id}')
def update_model(model_id: int, updates: ModelUpdate):
    if model_id not in models:
        raise HTTPException(
            status_code=404, 
            detail='Not found'
        )
    model = models[model_id]
    update_data = updates.model_dump(exclude_unset=True)
    updated_model = model.model_copy(update=update_data)
    models[model_id] = updated_model
    return updated_model
