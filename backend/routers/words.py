from fastapi import APIRouter
from classes.associations import Associations


# Initialize the router
router = APIRouter(prefix="", tags=["words"])





@router.get("/")
def get_words():
    """Return all words as a list"""
    return {Associations("data/words.csv")}

