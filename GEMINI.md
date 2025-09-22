# Gemini Project Context: Artist Collective (Python POC)

This document provides the context for Gemini to assist with building a Proof of Concept (POC) for the "Artist Collective" web application. The primary goal is **speed of development** to validate the core idea.

## Core Objectives (Proof of Concept)

The project scope is strictly limited to the following features to ensure rapid progress:

1.  **User Authentication:** Full signup, login, and logout functionality using Django's built-in system.
2.  **Image Uploading:** A protected view where authenticated users can upload an image file and add a title.
3.  **Simple Gallery:** A public page that displays all uploaded images in a grid.
4.  **Admin Panel:** Leverage the built-in Django Admin for all data management (users, images).

## Tech Stack

All code generation and assistance should strictly adhere to this stack. **Simplicity is the top priority.**

-   **Language:** `Python 3.11+`
-   **Framework:** `Django` (latest stable version)
-   **Database:** `SQLite` (the development default, no other database needed for the POC)
-   **Frontend:**
    -   `Django Template Language (DTL)` for server-side rendering.
    -   `Pico.css` for all styling. Please use its standard classes.
    -   **Constraint:** No custom CSS, JavaScript, or frontend frameworks (like Svelte, React, etc.) should be used for this POC.
-   **Image Handling:** Django's built-in `ImageField`, configured for local media storage.
-   **Environment:** All commands and instructions should assume a standard Python `venv` virtual environment on macOS.

## Key Preferences & Rules for Gemini

-   **Prioritize Django's built-in features** (e.g., `AuthenticationForm`, `ModelForms`, generic Class-Based Views) to minimize custom code.
-   **Explain Django Concepts:** When providing code, please add brief explanations for Django-specific patterns or "magic."
-   **Focus on the POC:** If I ask for a feature outside the defined scope (like chat or payments), please remind me that it's a deferred goal and we should focus on the POC first.
-   **Code First:** When I ask for help with a feature, provide the complete, working code snippet first, followed by the explanation.

## Initial File Structure
