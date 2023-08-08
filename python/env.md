### Working with envs in python
For all these operations you must import:
```python
import os
```

Set env:
```python
os.environ['MY_VARIABLE'] = 'my_value'
```
Or
```python
os.putenv('MY_VARIABLE', 'my_value')
```

Get Env:
```python
value = os.environ.get('MY_VARIABLE')
```
Or
```python
value = os.environ.get('MY_VARIABLE', 'default_value')
```

How to load configurations from .env file?
Create a `.env` file in root of your project
```
MONGO_URL='mongodb://localhost:27017'
DB_NAME='my_db'
```
Install `python-dotenv`:
```commandline
pip install python-dotenv
```
Load envs:
```python
from dotenv import load_dotenv
load_dotenv()
```
