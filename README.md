# Portfolio Test

This project is a simple Django-based portfolio website starter. It includes a basic Django project structure and is ready to be extended with your own pages, styling, and content.

## Project structure

- `my_portfolio_code/` — Django project package
- `my_portfolio_code/manage.py` — management script for running development commands
- `MyPortfolio/` — local virtual environment

## Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Getting started

1. Activate the virtual environment:

   ```bash
   MyPortfolio\\Scripts\\activate
   ```

2. Run the development server:

   ```bash
   python my_portfolio_code/manage.py runserver
   ```

3. Open your browser at:

   ```text
   http://127.0.0.1:8000/
   ```

## Useful commands

- Create migrations:

  ```bash
  python my_portfolio_code/manage.py makemigrations
  ```

- Apply migrations:

  ```bash
  python my_portfolio_code/manage.py migrate
  ```

- Create a superuser:

  ```bash
  python my_portfolio_code/manage.py createsuperuser
  ```

## Notes

This repository currently contains the default Django starter project configuration. You can customize the app, add templates, and build out your portfolio from here.
