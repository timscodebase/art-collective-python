# Artist Collective - Python POC Planning Doc

A high-level planning document for a Proof of Concept (POC) of the online artist collective. The goal is to rapidly validate the core functionality: users can sign up, upload art, and view it in a gallery.

---
## Project Status

The initial POC goals have been met, and the codebase has undergone a significant review and refactoring phase. Several new features have also been implemented.

### Completed POC Features

-   **User Authentication**: Full user registration, login, and logout functionality is in place.
-   **Image Management**: Authenticated users can upload images with a title via a simple form.
-   **Gallery Display**: A main gallery page displays all images, and a user-specific gallery shows a user's own uploads.
-   **Admin Interface**: Django's admin is configured for managing users and images.

### Additional Implemented Features

-   **Commenting System**: Users can add and delete their own comments on images.
-   **Chat Rooms**: A real-time chat application where users can create and join rooms.
-   **User Profiles**: User-specific galleries now function as profile pages, showing user info.
-   **Standardized Thumbnails**: All gallery pages now use a 3x2 grid with 16:9 aspect ratio thumbnails.

---
## Future Roadmap (Prioritized)

Based on the project's current state, here is a recommended order for tackling future features to get the most impact and build a solid foundation:

### 1. Build the User Panel
    -   **Update Password**: Fundamental security and account management.
    -   **Manage Photos and Albums**: Allow users to list, edit, and delete their uploaded images.
    -   **Change Color Scheme/Theme**: Add personalization options.

### 2. Add Image Rating and Sorting
    -   Introduce community interaction and a way to discover popular art.

### 3. Deployment
    -   Get the project online to a service like Heroku or PythonAnywhere.

---
## Deferred Features (Post-Roadmap)

These items are excellent but will be considered after the prioritized roadmap is complete:

-   Email & Username changes (significant user model changes).
-   Security Refactor & Advanced Chat (enhancements to existing structures).
-   E-commerce Portal (large feature, to be tackled once core features are mature).

---
## Tech Stack

-   **Framework:** **Django**
-   **Database:** **SQLite**
-   **Image Storage:** **Local File Storage** (`/media/` directory).
-   **Frontend:** **Django Templates** with **Pico.css**.
