# FastAPI Architectural Demonstration

This project is a demonstration created to showcase a clean, layered architecture for building applications with FastAPI. Its primary goal is to serve as a reference for folder structure and separation of concerns, not to be a fully functional or production-ready application.

## Key Concepts Demonstrated

### 1. Layered Architecture

The codebase is structured in a classic three-layer pattern to promote separation of concerns:

-   **Routes (`routes.py`):** The API layer. Handles HTTP request/response, data validation (Pydantic), and calls the appropriate service. It does not contain any business logic.
-   **Services (`services.py`):** The business logic layer. It orchestrates operations, calling the repository to access data.
-   **Repository (`repository.py`):** The data access layer. It is responsible for all communication with the data source.

### 2. Modular Folder Structure

The application is broken down into feature-based modules (`/app/users`, `/app/items`, `/app/auth`). Each module is self-contained and includes its own routes, services, repository, and data models. This makes the codebase easy to navigate and scale.

### 3. Authentication Components

The `/app/auth` module contains the building blocks for a token-based authentication system:

-   **Password Hashing:** Uses `bcrypt` to securely hash and verify user passwords (`auth/services.py`).
-   **Token Generation:** Uses `pyjwt` to create JWT access tokens upon successful login (`auth/services.py`).

## Intentional "Flaws" for Demonstration Purposes

The following are deliberate design choices made to keep the demonstration focused on architecture:

-   **In-Memory Database:** The repository layer uses a simple Python `list` as a "database" (`database/database.py`). This avoids the need for a real database setup, allowing one to focus purely on the application code structure.
-   **Disconnected Auth Endpoints:** The `register` and `login` endpoints are fully defined in `auth/routes.py` but are **intentionally not connected** to the main FastAPI app in `main.py`. This serves to demonstrate how the authentication routes and services are structured in isolation.
-   **No Active Route Protection:** While the login endpoint can generate a JWT, no API routes are configured to require this token for access. This isolates the demonstration of token *creation* from the concept of token *validation* and route protection.

