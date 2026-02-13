# Bookly Backend

A RESTful API backend for a book review application built with FastAPI.

## Tech Stack

- **Python 3.x**
- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Bookly_backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # Linux/Mac
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install required packages**
   ```bash
   pip install pydantic-settings
   pip install asyncpg
   ```

5. **Create requirements file**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Configure database**
   
   Create a `.env` file in the root directory and add your database URL:
   ```env
   DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/bookly_db
   ```

7. **Create configuration file**
   
   Create `src/config.py` with the following content:
   ```python
   from pydantic_settings import BaseSettings, SettingsConfigDict

   class Settings(BaseSettings):
       DATABASE_URL: str

       model_config = SettingsConfigDict(
           env_file=".env", extra="ignore"
       )
   ```

8. **Verify configuration**
   
   Test the configuration in Python REPL:
   ```python
   python
   >>> from src.config import Settings
   >>> s = Settings()
   >>> s.DATABASE_URL
   'postgresql+asyncpg://postgres:your_password@localhost:5432/bookly_db'
   ```

9. **Install SQLModel**
   
   SQLModel combines SQLAlchemy and Pydantic for elegant database interactions:
   ```bash
   pip install sqlmodel
   ```

10. **Set up database engine**
    
    Create `src/db/main.py` with the following content:
    ```python
    from sqlmodel import create_engine
    from sqlalchemy.ext.asyncio import AsyncEngine
    from src.config import Config
    
    # Create an asynchronous engine
    engine = AsyncEngine(
        create_engine(Config.DATABASE_URL, echo=True)
    )
    ```
    
    **Code explanation:**
    - `sqlmodel.create_engine`: Creates a synchronous database engine that manages database connections
    - `sqlalchemy.ext.asyncio.AsyncEngine`: Wraps the sync engine to enable async/await database operations, crucial for FastAPI's async endpoints
    - `Config.DATABASE_URL`: Retrieves the database connection string from environment variables
    - `echo=True`: Enables SQL query logging for debugging (logs all SQL statements to console)
    
    **Why async engine?**
    - Non-blocking I/O operations prevent FastAPI from freezing during database queries
    - Handles multiple concurrent requests efficiently
    - Better performance and scalability for production applications

11. **Run the application**
    ```bash
    uvicorn src.main:app --reload
    ```

## Project Structure

```
src/
├── books/          # Book-related endpoints
│   ├── routes.py   # API routes
│   ├── schemas.py  # Pydantic models
│   └── books_data.py
└── __init__.py
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Future Integration Plan

### Database Integration
- **PostgreSQL/MongoDB** - Migrate from in-memory data to persistent storage
- **SQLAlchemy/Motor** - ORM/ODM for database operations
- **Alembic** - Database migrations management

### Authentication & Authorization
- **JWT tokens** - Secure user authentication
- **OAuth2** - Social login integration (Google, GitHub)
- **Role-based access control** - User permissions and roles

### Advanced Features
- **User management** - Registration, profiles, and settings
- **Review system** - User ratings and reviews for books
- **Search & filtering** - Advanced book search with filters
- **Pagination** - Efficient data retrieval for large datasets
- **File uploads** - Book cover images using cloud storage (AWS S3/Cloudinary)

### Infrastructure
- **Docker** - Containerization for easy deployment
- **CI/CD** - Automated testing and deployment pipeline
- **Redis** - Caching layer for improved performance
- **Logging & monitoring** - Enhanced debugging and analytics

### Frontend Integration
- **CORS configuration** - Support for web/mobile clients
- **WebSocket support** - Real-time notifications
- **API versioning** - Backward compatibility management
