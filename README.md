# Steps to get running:

Before:
```
brew install python@3.14
brew install postgresql@18
```

Create virtual env:
```
python3 -m venv venv
```
start venv:
```
source .venv/bin/activate
```
or if using fish shell:
```
. venv/bin/activate.fish
```

then:
```
pip3 install -r requirements.txt
```
```
npm install --prefix frontend
```

db
```
brew services start postgresql
```
check if it is running with 
```
brew services list
```
```
brew services stop postgresql
```

backend
```
source .venv/bin/activate
```
```
./backend/manage.py runserver
```
http://127.0.0.1:8000/api/add?a=1&b=2
http://127.0.0.1:8000/api/docs

frontend
```
npm install --prefix frontend
```
```
npm run dev --prefix frontend
```

other
update requirements:
```
pipreqs . --ignore .venv,venv,tests --force
```