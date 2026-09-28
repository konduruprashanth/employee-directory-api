from datetime import datetime

from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    department: str
    designation: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True