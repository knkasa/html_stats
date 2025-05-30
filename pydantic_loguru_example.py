from pydantic import BaseModel, ValidationError, field_validator
from loguru import logger
import sys

# Configure Loguru
logger.remove()  # Remove default handler
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    colorize=True
)

# Pydantic model
class User(BaseModel):
    name: str
    age: int
    email: str
    
    @field_validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            logger.warning(f"Name '{v}' doesn't contain a space - might not be full name")
        return v.title()
    
    @field_validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            logger.error(f"Invalid age: {v}")
            raise ValueError("Age must be positive")
        return v

def process_user(data: dict):
    try:
        logger.info(f"Attempting to create user with data: {data}")
        user = User(**data)
        logger.success(f"User created successfully: {user}")
        return user
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    good_data = {"name": "john doe", "age": 30, "email": "john@example.com"}
    bad_data = {"name": "john", "age": -5, "email": "invalid"}
    
    try:
        user1 = process_user(good_data)
        logger.debug(f"User details: {user1.model_dump()}")
        
        user2 = process_user(bad_data)
    except Exception as e:
        logger.critical(f"Application error: {e}")
