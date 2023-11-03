from fastapi import APIRouter

from .quiz import quiz_router

quizzes_router = APIRouter()
quizzes_router.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])

__all__ = ["quizzes_router"]
