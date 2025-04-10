Here's a simplified and concise `README.md` file that you can copy and paste directly into your `book_manager/` directory. It focuses on the essentials: how to set up, run, and use the project, without extra details like troubleshooting or contribution guidelines.

```markdown
# Book Manager - Django REST Framework Project

A simple Django REST Framework application for managing books with CRUD operations using a three-layered architecture.

## Setup and Running

1. **Clone the project**
   ```bash
   git clone https://github.com/samandar-hamrayev/small-book-manager.git
   cd book_manager
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt # or pip install djangorestframework django
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

   The app will run at `http://localhost:8000`.

## Usage

### API Endpoints

| Method | Endpoint          | Action            |
|--------|-------------------|-------------------|
| GET    | `/api/books/`     | List all books    |
| POST   | `/api/books/`     | Add a new book    |
| GET    | `/api/books/<id>/`| View a book       |
| PUT    | `/api/books/<id>/`| Update a book     |
| DELETE | `/api/books/<id>/`| Delete a book     |

### Example Request (POST/PUT)
```json
{
    "title": "Sample Book",
    "author": "John Doe",
    "isbn": "1234567890123",
    "publication_date": "2025-01-01"
}
```

### Admin Interface
- URL: `http://localhost:8000/admin/`
- Create a superuser to access:
  ```bash
  python manage.py createsuperuser
  ```
- Log in to manage books via the web interface.

## How It Works

- **Presentation**: API views handle requests (`views.py`)
- **Logic**: `BookService` manages operations (`services.py`)
- **Data**: `Book` model stores data (`models.py`)

## Notes
- Uses SQLite database by default.
- All views are class-based for better structure.
```

### Instructions
1. Copy the entire content above.
2. Open or create `README.md` in the `book_manager/` directory.
3. Paste the content and save the file.

This version is:
- Short and to the point
- Focused on setup, running, and basic usage
- Includes only the essentials (API endpoints, admin access, and a brief architecture note)
- Ready for immediate copy-paste use

Let me know if you need any adjustments!