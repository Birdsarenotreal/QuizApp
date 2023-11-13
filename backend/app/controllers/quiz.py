from app.repositories import QuizRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Quiz, QuizOut

class QuizController(BaseController[Quiz]):
    def __init__(self, quiz_repository: QuizRepository):
        super().__init__(model=Quiz, repository=quiz_repository)

    async def get_most_popular_quiz(self) -> QuizOut:
        # Call the repository method to get the most popular quiz
        most_popular_quiz = await self.repository.get_most_popular_quiz()
        if most_popular_quiz:
            return most_popular_quiz
        else:
            # Handle the case when there is no such quiz
            # You might want to raise an HTTPException with a 404 status code here
            # or return an appropriate response
            raise HTTPException(status_code=404, detail="No quiz found with the most results.")
    