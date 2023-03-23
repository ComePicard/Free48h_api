from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def read_root():
    return {"MV-FLOW-LP-API": "HELLO"}
