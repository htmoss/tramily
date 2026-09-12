Steps to get running:

```
source .venv/bin/activate
```
```
pip3 install -r requirements.txt
```
```
cd frontend
```
```
npm install
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
cd frontend
```
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