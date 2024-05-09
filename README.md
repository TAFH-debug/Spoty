# Spoty

This is a simple web application for viewing, discussing and evaluating new trends in the field of music.

## How to launch?

### Database

#### If you have postgresql on your computer installed
You can launch postgresql on your localhost. It should be running on port 5432.

#### Other way by using docker
You should run docker image of postgresql.
In root folder of project:
```
docker-compose up --build
```

### Backend
You need python and pip installed on your computer.

```
cd spoty-svelte
pip install -r requirements.txt
alembic upgrade head
uvicorn spoty:app
```

### Frontend
You need node.js and npm installed on your computer.

```
cd spoty-svelte
npm install
npm run dev --open
```

## Development tracker

- [x] Basic web layout
- [x] User authorization
- [x] Disscussion feature
- [ ] Searching albums
- [x] Docker container

## Usage guide

If you succesfully launched site - it is avaible on port 5147.
Cite url: http://127.0.0.1:5173

There is some example albums that I added by myself.
You can register and then go to the song page and add your review.
In review you can add it's content and score.
![alt text](images/image.png)
If you didn't registered your review wouldn't be sent.
 
Some of the things that I didn't have time to do:

- Error handling 
- Searching (So search bar doesn't work as planned)
