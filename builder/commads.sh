docker network create -d bridge m4c-network
python3 ./builder/init.py
docker-compose up

echo DATABASE_URL=postgres://user:pass@m4c-database/m4c-db > .env