## Installation

you can start by buildiing your virtual env


```bash
  python3 -m venv <name_of_virtualenv>
```
after activating the virtual env. It is time to download required packages.

```bash
  pip install -r requirements.txt
```
Then you have to assign your postgreSQL url to 

```bash
  export DATABASE_URL=postgresql://..

```
or you can create new file named .env 
```bash
  touch .env

```
and inside it 
```bash
  DATABASE_URL=postgresql://..

```

### runnig the server

you can run the server by :


```bash
  uvicorn main:app

```

### generating fake data 

also you can generate some fake data by :

```bash
  python3 fake_data_generator.py

```

### Docker 

a docker file is also available

## Functionality:
after runnig the the server on the same url go to docs route to check the functionality or even interact with API

```bash
  <localhost:port>/docs
```
