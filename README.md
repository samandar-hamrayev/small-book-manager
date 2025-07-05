````markdown
# 📚 Book Manager – Django REST Framework Project

**Book Manager** is a simple and extensible Django REST Framework application that allows you to manage books using full CRUD (Create, Read, Update, Delete) functionality. It follows a clean, three-layered architecture for better separation of concerns and maintainability.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/samandar-hamrayev/small-book-manager.git
cd book_manager
````

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# or install manually:
# pip install django djangorestframework
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

🌐 Your application will be available at: `http://localhost:8000`

---

## 🔧 API Usage

### Available Endpoints

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/api/books/`      | Retrieve all books    |
| POST   | `/api/books/`      | Create a new book     |
| GET    | `/api/books/<id>/` | Retrieve a book by ID |
| PUT    | `/api/books/<id>/` | Update a book         |
| DELETE | `/api/books/<id>/` | Delete a book         |

### Example Payload for POST/PUT

```json
{
  "title": "Sample Book",
  "author": "John Doe",
  "isbn": "1234567890123",
  "publication_date": "2025-01-01"
}
```

---

## 🔐 Admin Panel

The Django admin interface is available at:

📍 `http://localhost:8000/admin/`

To access it, create a superuser:

```bash
python manage.py createsuperuser
```

Then log in using your credentials to manage books via the web interface.

---

## 🧱 Project Structure

This project uses a **three-layered architecture**:

* **Presentation Layer**: Handles incoming HTTP requests (`views.py`)
* **Service Layer**: Contains business logic (`services.py`)
* **Data Layer**: Defines data models (`models.py`)

This approach makes the codebase clean, modular, and easier to maintain or extend.

---

## ⚙️ Default Configuration

* **Database**: SQLite (can be replaced with PostgreSQL or MySQL)
* **Framework**: Django 4+ with Django REST Framework
* **Environment**: Python 3.9+
