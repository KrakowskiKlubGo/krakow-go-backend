# krakow-go-backend
Backend app for krakow go site

overview: 
- Go tournaments with registration, registered players and results uploads
- exporting tournament players to csv
- cloning tournaments
- i18n support - model fields translations
- one time and recurring meetings
- articles with images
- sgf files and image files storage in cloudinary
- PostgeSQL db


todo:
- full dockerize for prod and local
- add redis
- later extend to support many go clubs

## Running localy
run db with docker-compose
`docker-compose -f local.yml up -d db`

set .env file, for example:
```
DB_NAME=krakow_go_db
DB_USER=krakow_go_user
DB_PASSWORD=krakow_go_pass
DB_HOST=localhost
DB_PORT=5432

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=krakow_go_db
POSTGRES_USER=krakow_go_user
POSTGRES_PASSWORD=krakow_go_pass
POSTGRES_EXPOSE_PORT=5432
```
