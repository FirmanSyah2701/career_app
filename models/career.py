from pydantic import BaseModel
from typing import Union

class CareerPlanning(BaseModel):
    cp_one: str
    cp_two: str

class CareerExploration(BaseModel):
    ce_one: str
    ce_two: str

class MakeCareerDecisions(BaseModel):
    mcd_one: str
    mcd_two: str
    mcd_three: str

class WorldWorkInformation(BaseModel):
    wwi_one: str
    wwi_two: str
    wwi_three: str
    wwi_four: str
    wwi_five: str

class PreferedGroupWork(BaseModel):
    pgw_one: str
    pgw_two: str
    pgw_three: str

class Career(BaseModel):
    career_planning: Union[CareerPlanning, None] = None
    career_exploration: Union[CareerExploration, None] = None
    make_career_decisions: Union[MakeCareerDecisions, None] = None
    world_of_work_information: Union[WorldWorkInformation, None] = None
    prefered_group_work: Union[PreferedGroupWork, None] = None