# krakow-go-backend
currently used krakow go site after many concept changes over years

stack: 
* django with static export using django-distill
* tailwind 
* daisyui
* supabase for db

## todo:
### rewrite this to jekyll or any simpler static site generator...

## Running locally
install django-browser-reload
`pip install 'django-tailwind[reload]'`

run db with docker-compose
`docker-compose -f local.yml up -d db`

set .env file like .env.example

