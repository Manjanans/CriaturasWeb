from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_criaturas():
    return {"message": "Endpoint for all criaturas"}
