from datetime import date
from enum import Enum
from typing import Optional, List

from fastapi import APIRouter, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field

app1 = APIRouter()

"""Path Parameters and Number Validations 路径参数和数字验证"""
@app1.get("/path/parameters")
def path_params01():
    return {"message": "This is a message"}

@app1.get("/path/{parameters}")  # 函数的顺序就是路由的顺序
def path_prams02(parameters: str):
    return {"message": parameters}

class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"

@app1.get("/enum/{city}")  # 枚举类型的参数
async def latest(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": city, "confirmed": 1492, "death": 7}
    if city == CityName.Beijing:
        return {"city_name": city, "confirmed": 971, "death": 9}
    return {"city_name": city, "latest": "unknown"}

@app1.get("/files/{file_path:path}")  # 通过path parameters传递文件路径
def filepath(file_path: str):
    return f"The file path is {file_path}"

@app1.get("/path_/{num}")
def path_params_validate(
    # 数值进行校验大于1小于10
    num: int = Path(..., title="Your Number", description="不可描述", ge=1, le=10),
):
    return num
