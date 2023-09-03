# Grocery Data

App for uploading and displaying data about products and retailers stock and promotions using Django backend, React frontend, and DRF api

## Installation and startup

clone repo

cd to root directory

pipenv install (ensure python3.11 is installed)

pipenv shell

cd backend/

python manage.py runserver to run backend

visit 127.0.0.1:8000 to check its running

in another terminal cd frontend

npm start (ensure node is sinatlled)

visit localhost:3000 to check that is running

## extra tech

i used coverage for a nice gui showing me the backend test coverage. You can use this like this:
```
# run test
coverage python manage.py test

# view test coverage in terminal
coverage report

# generate html file that to interact with and see what parts of your code haven't been tested yet
coverage html
```

i used shadcn so i dont need to build out all of my own components. However ran into an issue by desciding to use vanilla react, there isnt much support for that, so ended up spending more time setting this up as expected. If i did this again id use nextjs and start the project in typescript