# Artist Collective - Python POC Planning Doc

A high-level planning document for a Proof of Concept (POC) of the online artist collective. The goal is to rapidly validate the core functionality: users can sign up, upload art, and view it in a gallery.

---
## POC Features

The scope is intentionally limited to these core features:

- [ ] **User Authentication**
  - [ ] User registration page
  - [ ] User login / logout
- [ ] **Image Management**
  - [ ] A simple form for logged-in users to upload an image and give it a title.
- [ ] **Gallery Display**
  - [ ] A public page showing all uploaded images in a simple grid.
  - [ ] A user-specific page showing only the art they have uploaded.
- [ ] **Admin Interface**
  - [ ] Use the built-in Django admin to manage users and uploads.

---
## Deferred Features

These features from the original plan are **out of scope** for the initial POC but can be added later:

- [ ] Encrypted chat rooms
- [ ] Sales portal and e-commerce integration
- [ ] Advanced gallery customization (themes, sharing, paid/free)
- [ ] Image rating, sorting, and discovery pages

---
## Tech Stack

This stack is chosen for maximum development speed and simplicity.

- **Framework:** **Django** - A "batteries-included" Python framework that provides the ORM, admin panel, and authentication system out of the box.
- **Database:** **SQLite** - The default Django database for development. It's simple, serverless, and perfect for a POC.
- **Image Storage:** **Local File Storage** - For the POC, images will be stored on the same server the app is running on (`/media/` directory).
- **Frontend:** **Django Templates** - Standard server-rendered HTML. We can add a minimal CSS framework like [Pico.css](https://picocss.com/) for basic styling without writing any CSS.

---
## Next Steps

1.  Set up a new Django project.
2.  Create a `gallery` app within the project.
3.  Define the `ImageUpload` model in `models.py` (with fields for title, image, and a foreign key to the User).
4.  Create the views and forms needed for user registration and image uploading.
5.  Define the URL patterns in `urls.py` to route traffic to the correct views.
6.  Build the basic HTML templates for the gallery and upload pages.
