from app.schemas.quiz.schema import Quiz, QuizIn, QuizOut
from core.repository.base import BaseRepository
from core.database import models
from core.database.models import Quiz as QuizModel
from tortoise.functions import Count , Avg , Sum
from tortoise.expressions import F
from tortoise.exceptions import DoesNotExist

class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        super().__init__(schema=QuizOut, create_schema=QuizIn, db_model=models.Quiz)
    
    async def get_most_popular_quiz(self) -> QuizOut:
        # We count the number of results for each quiz and order by this count in descending order
        most_popular_quiz_query = (
            await QuizModel
            .annotate(results_count=Count('results'))  # Assuming 'results' is the related name for the Result model
            .order_by('-results_count')
            .first()
        )

        if most_popular_quiz_query:
            return await QuizOut.from_tortoise_orm(most_popular_quiz_query)

        return None