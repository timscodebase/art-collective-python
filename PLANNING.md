# Artist Collective - Python POC Planning Doc

A high-level planning document for a Proof of Concept (POC) of the online artist collective. The goal is to rapidly validate the core functionality: users can sign up, upload art, and view it in a gallery.

---

## Project Status

The initial POC goals have been met, and the codebase has undergone a significant review and refactoring phase. Several new features have also been implemented.

### Completed POC Features

- **User Authentication**: Full user registration, login, and logout functionality is in place.
- **Image Management**: Authenticated users can upload images with a title via a simple form.
- **Gallery Display**: A main gallery page displays all images, and a user-specific gallery shows a user's own uploads.
- **Admin Interface**: Django's admin is configured for managing users and images.

### Additional Implemented Features

- **Commenting System**: Users can add and delete their own comments on images.
- **Chat Rooms**: A real-time chat application where users can create and join rooms.
- **User Profiles**: User-specific galleries now function as profile pages, showing user info.
- **Standardized Thumbnails**: All gallery pages now use a 3x2 grid with 16:9 aspect ratio thumbnails.

---

## Deferred Features

These features from the original plan remain out of scope for now:

- Advanced chat features (e.g., encryption, private messages).
- Sales portal and e-commerce integration.
- Advanced gallery customization (themes, sharing, paid/free).
- Image rating, sorting, and discovery pages.

---

## Tech Stack

- **Framework:** **Django**
- **Database:** **SQLite**
- **Image Storage:** **Local File Storage** (`/media/` directory).
- **Frontend:** **Django Templates** with **Pico.css**.

--
## Next Steps

1. **Plan Next Feature Sprint**: Decide which "Deferred Feature" to tackle next.
2. **Continue Refinement**: Address any new bugs or areas for improvement as they arise.
