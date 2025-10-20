# Spark

A simple in-the-moment idea capture tool. No more context-switching between code and a different notes app. Future plans include having a popup overlay to launch the app from whichever window you have open.

Spark remembers what context you were in through the directory you saved a note in. GUI version will remember the context through what window you had open

## How to run

Open PowerShell in the project root and run:

1. Install dependancies and create virtual environment:

    ```bash
    uv sync

    source .venv/bin/Activate # Windows
    source .venv/bin/activate # Linux
    ```

2. Run database migrations:

    ```bash
    cd src/database

    alembic upgrade head
    ```

3. Run the app:

    In the root directory, run:

    ```bash
    python main.py add "new note" # to create a new note
    python main.py list # for all notes in your current dir
    python main.py list --all # for all the notes in the database
    python main.py delete <id> # to delete a note through it's id
    ```
