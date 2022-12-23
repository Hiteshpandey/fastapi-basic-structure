from fastapi import APIRouter
from app.schemas import tools
router = APIRouter()

@router.post('/mx')
def processDomainMx():
  return 1
