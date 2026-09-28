from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Directory API",
    description="CRUD API for managing employees",
    version="1.0.0",
)


@app.post(
    "/employees",
    response_model=schemas.EmployeeResponse,
    status_code=201,
)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
):
    existing_employee = (
        db.query(models.Employee)
        .filter(models.Employee.email == employee.email)
        .first()
    )

    if existing_employee:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    return crud.create_employee(db, employee)


@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    return employee


@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db),
):
    existing_employee = crud.get_employee(db, employee_id)

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    email_owner = (
        db.query(models.Employee)
        .filter(
            models.Employee.email == employee.email,
            models.Employee.id != employee_id,
        )
        .first()
    )

    if email_owner:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    return crud.update_employee(db, employee_id, employee)


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    return {"message": "Employee deleted successfully"}