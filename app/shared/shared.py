from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType", bound=BaseModel)

async def inserts(
    data: BaseModel,
    model: Type[ModelType],           
    db: Session
):
    nueva = model(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

async def search_by_id(
    search_num: int,
    model: Type[ModelType],
    db: Session
) -> ModelType:
    nueva = db.get(model, search_num)
    if not nueva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found"
        )
    return nueva

async def updates(
    data: SchemaType,
    model: Type[ModelType],
    db: Session
):
    nueva = search_by_id(data.id, model, db, current_user)
    
    actualizar = data.model_dump(exclude_unset=True)
    actualizar.pop("id", None)

    for key, value in actualizar.items():
        setattr(nueva, key, value)
    
    db.commit()
    db.refresh(nueva)

    return nueva

async def deletes(
    num_del: int,
    model: Type[ModelType],
    db: Session
):
    try:
        elim = db.get(model, num_del)
        db.delete(elim)
        db.commit()
        return None
    except:
        raise HTTPException(status_code=404, detail="Not found")

async def search_all(
    model: Type[ModelType],
    db: Session
) -> SchemaType:
    stmt = select(model)
    query = db.execute(stmt).scalars()
    return query

async def search_by_name(
    search_query: str,
    column,
    model: Type[ModelType],
    db: Session
) -> list[ModelType]:
    stmt = select(model).where(column.ilike(f"%{search_query}%"))
    nueva = db.execute(stmt).scalars()
    if not nueva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found"
        )
    return nueva