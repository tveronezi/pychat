# simple chat api with python

```
poetry install
poetry run uvicorn pychat.main:app --reload
poetry build
```

## DB stuff

```
# create a new database revision
poetry run alembic revision -m "users table"
# run the migration update
poetry run alembic upgrade head
# downgrade the database to nothing
poetry run alembic downgrade base
```


## Resources

* https://python-poetry.org/docs/cli
