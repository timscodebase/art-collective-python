# Gemini Project Context: Artist Collective

This document provides the context for Gemini to assist with building the "Artist Collective" web application. The project has moved beyond the initial POC phase and now includes multiple apps and a richer tech stack.

## Core Project Components

1.  **`landing` app**: Handles the main welcome page and user authentication (signup/login/logout).
2.  **`gallery` app**: Manages image uploads, the main gallery slider, artist profile pages, and the commenting system.
3.  **`chat` app**: Provides real-time chat room functionality using Django Channels.
4.  **`site_settings` app**: A singleton model, managed via the Django Admin, to control site-wide features like the gallery slider's behavior.

## Tech Stack

All code generation and assistance should adhere to this stack.

-   **Language:** `Python 3.11+`
-   **Framework:** `Django` (latest stable version) with `Channels` for real-time features.
-   **Database:** `SQLite`
-   **Frontend:**
    -   `Django Template Language (DTL)` for server-side rendering.
    -   `Pico.css` for base styling.
    -   `Splide.js` for the main gallery slider.
    -   Vanilla JavaScript for WebSocket connections in the chat application.
    -   Custom CSS for styling thumbnails and other elements.
-   **Image Handling:** Django's built-in `ImageField` for local media storage.
-   **Environment:** Assumes a standard Python `venv` virtual environment on macOS with **Redis** available for the Channels layer.

## Key Preferences & Rules for Gemini

-   **Prioritize Django's built-in features** where applicable, but integrate cleanly with external libraries like Splide.js.
-   **Provide complete, full-file code snippets** when adding new features or fixing bugs to avoid confusion.
-   **Explain Django & Channels Concepts:** When providing code for new features, add brief explanations for Django-specific patterns, especially for Channels and asynchronous code.
-   **Adhere to the multi-app structure:** When adding new, distinct functionality, propose creating a new app for it.