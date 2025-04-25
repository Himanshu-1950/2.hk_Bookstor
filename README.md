
# Bookstore Django Application

This is a simple **Bookstore Management System** built with **Django**. It allows users to view available books, register, log in, and manage books through an admin interface. The system is designed to be easily customizable and extendable.

## Features

- User registration and login
- View list of available books
- Add, edit, and delete books (admin functionality)
- Book detail view with descriptions and prices
- Bootstrap 5 for responsive design

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default, can be configured for MySQL/PostgreSQL)
- **Version Control**: Git

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Git

### Steps to Run the Project Locally

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/bookstore-django.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bookstore-django
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Open a web browser and go to `http://127.0.0.1:8000/` to view the application.

### Admin Interface

Once logged in as an admin, you can manage books via the Django admin panel:

- URL: `http://127.0.0.1:8000/admin/`
- Username and password: Use the superuser credentials created in step 7.

# ScreenShot
### Login Page
![Screenshot 2025-04-25 164528](https://github.com/user-attachments/assets/bcbeb63c-e2e8-4b99-ab04-47725aabc229)

### Add New Book Page
![Screenshot 2025-04-25 164412](https://github.com/user-attachments/assets/22ad45ed-2ae9-421a-858b-7787446f6e8d)

### Books List Page
![WhatsApp Image 2025-04-25 at 19 24 26_47541564](https://github.com/user-attachments/assets/75790168-1c26-4062-b36c-533b33bdae4a)



