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

## Running locally
run db with docker-compose
`docker-compose -f local.yml up -d db`

set .env file like .env.example

