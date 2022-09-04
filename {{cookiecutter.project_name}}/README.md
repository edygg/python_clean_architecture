# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Basic Commands

### Build app services
```commandline
$ docker compose -f local.yml build
```

### Type checks
```commandline
$ docker compose -f local.yml run --rm journeys mypy b1rdo_journeys
```

### Test coverage
```commandline
$ docker compose -f local.yml run --rm journeys pytest --cov=/app
```


### Running tests
```commandline
$ docker compose -f local.yml run --rm journeys pytest
```

### Pre-commit for PRs
Run before create a PR.

```commandline
$ docker compose -f local.yml run --rm journeys pre-commit run --all-files
```

### Create new migration
```commandline
docker compose -f local.yml run --rm journeys alembic revision --autogenerate -m "MESSAGE"
```

### Execute Migrations
```commandline
$ docker compose -f local.yml run --rm journeys alembic upgrade head
```

## Deployment
TDB