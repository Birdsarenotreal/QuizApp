from app.repositories import CategoryRepository
from core.controller import BaseController
from app.schemas.quiz.schema import Category,CategoryOut



class CategoryController(BaseController[Category]):
    def __init__(self, category_repository: CategoryRepository):
        super().__init__(model=Category, repository=category_repository)

    async def get_most_popular_category(self) -> CategoryOut:
        most_popular_category = await self.repository.get_most_popular_category()
        if most_popular_category:
            return most_popular_category
        else:
            # If no category found, you can decide to return a default message or raise an exception
            raise HTTPException(status_code=404, detail="No popular category found.")
