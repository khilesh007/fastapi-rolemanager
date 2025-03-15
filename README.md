
# FastAPI RoleManager

This project is a FastAPI-based application that allows user management with Role-Based Access Control (RBAC). It supports user registration, login, and CRUD operations with role-based permissions (Admin and User). The application uses PostgreSQL for database storage and Alembic for database migrations.

## Features:
- User Registration (Admin & Normal User)
- JWT Authentication
- Role-Based Access Control (Admin: create, update, delete. User: read only)
- CRUD operations for Projects (Admin: manage, User: view)

## API Endpoints:
### 1️⃣ Register a User (Admin & Normal User)

- **Admin User:**
  - Endpoint: `POST /users/register`
  - Body:
    ```json
    {
      "username": "admin_user",
      "password": "adminpass",
      "role": "admin"
    }
    ```
  - **Expected Response:**
    ```json
    {
      "message": "User registered successfully"
    }
    ```
  
- **Normal User:**
  - Endpoint: `POST /users/register`
  - Body:
    ```json
    {
      "username": "normal_user",
      "password": "userpass",
      "role": "user"
    }
    ```
  - **Expected Response:**
    ```json
    {
      "message": "User registered successfully"
    }
    ```

### 2️⃣ Login and Get Token (Admin & User)
- **Admin User:**
  - Endpoint: `POST /users/token`
  - Form Data:
    - `username: admin_user`
    - `password: adminpass`
  - **Expected Response:**
    ```json
    {
      "access_token": "<JWT_TOKEN>",
      "token_type": "bearer"
    }
    ```
  
- **Normal User:**
  - Endpoint: `POST /users/token`
  - Form Data:
    - `username: normal_user`
    - `password: userpass`
  - **Expected Response:**
    ```json
    {
      "access_token": "<JWT_TOKEN>",
      "token_type": "bearer"
    }
    ```

### 3️⃣ Fetch All Projects (Admin & User)
- **Admin:**
  - Endpoint: `GET /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Response:**
    ```json
    []
    ```
  
- **Normal User:**
  - Endpoint: `GET /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Response:**
    ```json
    []
    ```

### 4️⃣ Create a Project (Admin Allowed, User Forbidden)
- **Admin User:**
  - Endpoint: `POST /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - Body:
    ```json
    {
      "name": "Project 1",
      "description": "This is the first project."
    }
    ```
  - **Expected Response:**
    ```json
    {
      "id": 1,
      "name": "Project 1",
      "description": "This is the first project.",
      "owner_id": 1
    }
    ```
  
- **Normal User:**
  - Endpoint: `POST /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - Body:
    ```json
    {
      "name": "Unauthorized Project",
      "description": "This should not work."
    }
    ```
  - **Expected Error Response:**
    ```json
    {
      "detail": "Not authorized"
    }
    ```

### 5️⃣ Fetch All Projects Again (Admin & User)
- **Admin:**
  - Endpoint: `GET /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Project 1",
        "description": "This is the first project.",
        "owner_id": 1
      }
    ]
    ```

- **Normal User:**
  - Endpoint: `GET /projects/`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Project 1",
        "description": "This is the first project.",
        "owner_id": 1
      }
    ]
    ```

### 6️⃣ Update a Project (Admin Allowed, User Forbidden)
- **Admin User:**
  - Endpoint: `PUT /projects/1`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - Body:
    ```json
    {
      "name": "Updated Project",
      "description": "This project has been updated."
    }
    ```
  - **Expected Response:**
    ```json
    {
      "id": 1,
      "name": "Updated Project",
      "description": "This project has been updated.",
      "owner_id": 1
    }
    ```

- **Normal User:**
  - Endpoint: `PUT /projects/1`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - Body:
    ```json
    {
      "name": "User Updated",
      "description": "User should not be able to update."
    }
    ```
  - **Expected Error Response:**
    ```json
    {
      "detail": "Not authorized"
    }
    ```

### 7️⃣ Delete a Project (Admin Allowed, User Forbidden)
- **Admin User:**
  - Endpoint: `DELETE /projects/1`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Response:**
    ```json
    {
      "message": "Project deleted successfully"
    }
    ```

- **Normal User:**
  - Endpoint: `DELETE /projects/1`
  - Headers: `Authorization: Bearer <JWT_TOKEN>`
  - **Expected Error Response:**
    ```json
    {
      "detail": "Not authorized"
    }
    ```

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/khilesh007/fastapi-rolemanager.git
cd fastapi-rolemanager
```

### 2. Set up a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Modify the `.env` file in the root directory of the project and add your PostgreSQL credentials and SECRET_KEY.:

```text
DATABASE_URL=postgresql://<username>:<password>@<host>/<database_name>
```

### 5. Apply Migrations
Run Alembic migrations to set up the database schema:

```bash
alembic upgrade head
```

### 6. Run the Application
Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will be running on `http://127.0.0.1:8000`.


---

## Additional Configuration
No additional configurations are needed beyond the `.env` setup for the database URL.

---

## Dependencies
- **FastAPI**: Web framework for building APIs
- **SQLAlchemy**: ORM for database interaction
- **SQLModel**: Pydantic-based models for SQLAlchemy
- **Alembic**: Database migrations
- **PostgreSQL**: Database for storing data
- **Passlib**: Password hashing and verification
- **Python-dotenv**: For loading environment variables
