**Backend Django with GraphQL**

**Main Features:**

- **Product and Category Management:** Utilizing Django models, the application enables the creation, reading, updating, and deletion of products and categories.

- **GraphQL for Efficient Queries:** The integration of GraphQL provides an efficient way to perform specific queries to obtain precise data according to the clients' needs.

- **CRUD Operations:** GraphQL mutations have been implemented to perform CRUD operations on products and categories, including creation, deletion, and updating of the same.

**Getting Started (After Cloning the Repository):**

1. **Create and Activate a Virtual Environment:**
   - Run `python -m venv env` to create a virtual environment named `env`.
   - Activate the environment with `source env/bin/activate` (Windows: `env\Scripts\activate`).

2. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install required libraries.

3. **Configure Database:**
   - Create your MySQL database and configure credentials in the `settings.py` file.

4. **Run Django Migrations:**
   - Run `python manage.py migrate` to apply database schema changes.

5. **Create a Superuser:**
   - Run `python manage.py createsuperuser` to create an initial superuser for administrative access.

6. **Start Development Server:**
   - Run `python manage.py runserver` to start the Django development server.

7. **Access Administration Panel:**
   - Open your web browser and navigate to `http://127.0.0.1:8000/admin/` to access the administration panel.

**Important:**
The `.env` file stores sensitive information like database credentials and secret keys.

**Structure of the .env File:**

```
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DB_ENGINE=
DB_NAME=
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_PORT=
MY_SECRET_KEY=
```

**Instructions for Using .env:**

1. Create a text file named `.env` in your project's root directory.
2. Copy and paste the above content into the `.env` file.
3. Replace the placeholder values with your specific database credentials and secret keys.
