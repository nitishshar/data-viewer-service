Install dev dependencies

pip install black
pip install isort   
pip install autoflake

Install Test Dependencies

pip install pytest 

Install project requirements

pip install fastapi
pip install uvicorn


formatting

black .
isort -rc .
autoflake --in-place -r api