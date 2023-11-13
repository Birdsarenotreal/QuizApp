from app.schemas.quiz.schema import Category, CategoryIn, CategoryOut
from core.repository.base import BaseRepository
from core.database import models
from core.database.models import Category as CategoryModel
from tortoise.functions import Count , Avg , Sum
from tortoise.expressions import F
from tortoise.exceptions import DoesNotExist

class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(schema=CategoryOut, create_schema=CategoryIn, db_model=models.Category)
        
    async def get_most_popular_category(self) -> CategoryOut:
        # Assuming CategoryOut is a Pydantic model for Category output
        most_popular_category_query = (
            await CategoryModel
            .annotate(quizzes_taken_count=Count('quizs__results'))
            .order_by('-quizzes_taken_count')
            .first()
        )
        if most_popular_category_query:
            return await CategoryOut.from_tortoise_orm(most_popular_category_query)
        else:
            return None