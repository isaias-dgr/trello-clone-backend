from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field

from uuid import UUID, uuid4

from typing import Optional
from decimal import Decimal

class TaskMove(BaseModel):
    id: UUID
    status: str
    position: Optional[Decimal] = None
    next_to: Optional[UUID] = None
    prev_to: Optional[UUID] = None

class TaskCreate(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    status: str
    depto: str
    position: Decimal
    comments: list[UUID]
    attachments: list[UUID]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskRead(TaskCreate):

    class Config:
        orm_mode = True