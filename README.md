# Cookiecutter Python Clean Architecture

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Template project based on Clean Architecture for Python on  [Cookiecutter](https://github.com/cookiecutter/cookiecutter), includes production-ready containers using Docker and Docker Compose.

- If you have problems with this template, please open issues don't send emails to the maintainers.

## Features
- Works with Python 3.9 (easy to change interpreter and linux distro in main `Dockerfile`)
- Optimized dev and prod envs and settings.
- Docker support using `docker compose` for dev and prod envs.
- Tests template and db fixtures using `pytest`.
- DB integration using `SQLAlchemy` with migration boilerplate included.
- Customizable PostgresSQL version.
- Preconfig Github Actions for formatting and testeable code.
- Precommit config for maintenabled code.

![Clean Architecture](https://res.cloudinary.com/dodpsiyv0/image/upload/v1662352392/IMG_0444_p7yscl.png)