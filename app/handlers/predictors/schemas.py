from pydantic import BaseModel
from typing import List


class PageInfo(BaseModel):
    """
    Общие данные по запросу
    """
    all_docs: int = 0
    output_docs: int = 0


class PredictSchemas(BaseModel):
    machine_number: int
    data: List[List[float]]
    columns: List[str]


class PredictOutput(BaseModel):
    predicts: List[List[float]]


