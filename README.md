# Artist Collective - Python POC

This project is a Proof of Concept (POC) for an online art gallery built with Python and Django. The goal is to create a simple application where users can register, upload their art, and view it in a gallery.

---

## Prerequisites

-   Python 3.11+
-   Git

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd artist_collective_project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the Admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

---

## Running the Development Server

1.  **Start the server:**
    ```bash
    python manage.py runserver
    ```

2.  **Open your browser** to `http://127.0.0.1:8000` to view the application.

3.  **Access the Admin panel** at `http://127.0.0.1:8000/admin`.
