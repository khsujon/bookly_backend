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
4. **Run the application**
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


