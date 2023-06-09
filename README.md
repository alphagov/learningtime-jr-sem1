# Simple Containerised System Health Checker
Create a basic containerised application that periodically checks the health of a system and logs the results. 

## Features:
A Dockerised application that pings a /health-check endpoint on a website I will provide every 60 seconds

Logs the result to a database, along with a timestamp and success or failure state

Renders the result as an HTML page that lists all previous checks

Choose a linting tool and apply code standards to your application :pylint?

Add checks using github actions to enforce that tests and code quality checks must pass before allowing merge to `main`

Document how a new developer can get the application working locally in a README.md

Present back to the group with some slides explaining the difference between Docker, Docker compose and how your implementation works. Cover some of the advantages / disadvantages as you see them?

Can we add a second service that relies on the one you’ve dockerised (a frontend relying on an API perhaps?) Can you add it so the two get spun up and can work together.

## Run health-checker with PostgreSQL using Docker Compose

`docker-compose build` to build the images required.

`docker-compose up` to start up the containers.

## How to run stand alone container using Docker

Build the health-checker Docker image by running the following command:
`docker build -t health-checker .`
Once the image is built, you can run a container using the following command:
`docker run health-checker`

##Access from a browser

Once the services are running, visit the app on http://localhost:4000

## How to access the backend PostgresDB

Run `psql -U postgres` within the database Docker container.

`\dt+` displays all tables in extended view.
`SELECT * FROM response_times;` queries all data from the response_times table.
`DROP TABLE response_times;` to delete the table.