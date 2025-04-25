
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

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, make changes, and create a pull request. We welcome contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django for providing a powerful web framework.
- Bootstrap for making it easy to create responsive designs.
