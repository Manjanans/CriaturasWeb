from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_batallas():
    return {"message": "Endpoint for all batallas"}
