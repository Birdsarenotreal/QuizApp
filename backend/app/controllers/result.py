# ResultController implementation

from app.repositories import ResultRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Result, UserOut, QuizOut, CategoryOut
from typing import List

class ResultController(BaseController[Result]):
    def __init__(self, result_repository: ResultRepository):
        super().__init__(model=Result, repository=result_repository)

    async def get_top_performer(self) -> UserOut:
        # Call the updated repository method
        top_performer = await self.repository.get_top_performer()
        if top_performer:
            return top_performer
        else:
            # Handle the case when there is no top performer
            # You might want to raise an HTTPException with a 404 status code here
            # or return an appropriate response
            pass

    async def get_least_correct_results_user(self) -> UserOut:
        # Call the updated repository method
        least_correct_results_user = await self.repository.get_least_correct_results_user()
        if least_correct_results_user:
            return least_correct_results_user
        else:
            # Handle the case when there is no such user
            # You might want to raise an HTTPException with a 404 status code here
            # or return an appropriate response
            raise HTTPException(status_code=404, detail="No user found with least correct results.")

