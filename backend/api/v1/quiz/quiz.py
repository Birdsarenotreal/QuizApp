from fastapi import APIRouter, Depends, HTTPException
from app.controllers import QuizController  # Import the QuizController
# from app.schemas.quiz.schema import FeedbackIn, FeedbackOut, Feedback as FeedbackSchema
from app.schemas.quiz.schema import QuizIn, QuizOut, Quiz as QuizSchema
from typing import List
from core.factory import Factory

quiz_router = APIRouter()

@quiz_router.get("/")
async def get_all_quizzes(controller: QuizController = Depends(Factory().get_quiz_controller)) -> List[QuizOut]:
    return await controller.repository.get_all()

@quiz_router.get("/{id}")
async def get_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    quiz = await controller.get_by_id(id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@quiz_router.post("/", response_model=QuizOut)
async def create_quiz(quiz: QuizIn, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    return await controller.add(quiz)

@quiz_router.put("/{id}", response_model=QuizOut)
async def update_quiz(id: int, quiz: QuizIn, controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    return await controller.update(id, quiz)

@quiz_router.delete("/{id}")
async def delete_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)):  
    await controller.delete(id)
    return {"message": "Quiz deleted successfully"}

@quiz_router.get("/most-popular-quiz/", response_model=QuizOut)
async def get_most_popular_quiz(controller: QuizController = Depends(Factory().get_quiz_controller)) -> QuizOut:
    try:
        # This will call the controller method and should return a single QuizOut
        return await controller.get_most_popular_quiz()
    except HTTPException as http_ex:
        # Re-raise the HTTPException
        raise http_ex
    except Exception as e:
        # For any other exceptions, return a generic error response
        raise HTTPException(status_code=500, detail=str(e))
    