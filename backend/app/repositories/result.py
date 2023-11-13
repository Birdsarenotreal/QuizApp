from app.schemas.quiz.schema import Result, ResultIn, ResultOut, UserOut
from core.repository.base import BaseRepository
from core.database import models
from core.database.models import User as UserModel
from tortoise.transactions import in_transaction

class ResultRepository(BaseRepository[Result]):
    def __init__(self):
        super().__init__(schema=ResultOut, create_schema=ResultIn, db_model=models.Result)

    async def get_top_performer(self) -> UserOut:
        # Define the raw SQL query for the highest score
        raw_query = """
            SELECT user_id, SUM(score) as total_score
            FROM result
            GROUP BY user_id
            ORDER BY total_score DESC
            LIMIT 1;
        """

        # Execute the raw SQL query inside a transaction
        async with in_transaction() as connection:
            results = await connection.execute_query_dict(raw_query)

            # Process the results
            if results:
                # Since we're using LIMIT 1, we can get the first result directly
                top_result = results[0]
                # Fetch the user object from the database
                top_user = await UserModel.get(id=top_result['user_id']).prefetch_related('results')
                return await UserOut.from_tortoise_orm(top_user)
            else:
                print("No users found or no scores to sum.")
                return None

    async def get_least_correct_results_user(self) -> UserOut:
        # Define the raw SQL query
        raw_query = """
            SELECT user_id, SUM(score) as total_score
            FROM result
            GROUP BY user_id
            ORDER BY total_score ASC
            LIMIT 1;
        """

        # Execute the raw SQL query inside a transaction
        async with in_transaction() as connection:
            results = await connection.execute_query_dict(raw_query)

            # Process the results
            if results:
                # Since we're using LIMIT 1, we can get the first result directly
                least_correct_result = results[0]
                # If you need to return the user object, fetch it from the database
                least_correct_user = await UserModel.get(id=least_correct_result['user_id']).prefetch_related('results')
                return await UserOut.from_tortoise_orm(least_correct_user)
            else:
                print("No users found or no scores to sum.")
                return None
