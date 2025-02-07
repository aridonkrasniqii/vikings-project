# Vikings Project

## Overview
This project is a web application that displays data on characters from Viking-related sources. The frontend is developed with Angular, and the backend is developed with Django. The application is fully containerized using Docker.

## Requirements
### Scraping
Collect data on Vikings from:
- The TV series "Vikings"
- The TV series "Norsemen"
- The Vikings NFL team

Scrape descriptions, actor information, and photos from these sources.

### Store Data in SQL Database
- Use PostgreSQL to store the scraped data.
- Set up a pipeline to continuously scrape and update the database.

### Web Application
Display the collected data with the following features:
- A table showing all characters, filterable by various criteria.
- Individual pages for each character.
- (Optional) Ability to edit information through the frontend.

## Implementation
### Frontend
- Developed with Angular.
- Three main components represent each model.
- Features: Create, delete, update, list using pagination and search filtering.

### Backend
- Developed with Django.
- Two main apps:
  - **API App:** Communicates with the frontend and provides services.
  - **Scraping App:** Handles all scraping tasks using Celery, Redis, and Selenium.

### Scraping
- **Tasks:** Defined tasks for scraping data.
- **Items:** Structured data items.
- **Pipelines:** Process and store scraped data.
- **Middlewares:** Manage scraping behaviors.
- **Spiders:** Customized spiders for each scraping source.

### Containerization
- The entire application is containerized using Docker.
- Use Docker Compose to start all services with a single command.

## Getting Started
### Prerequisites
- Docker and Docker Compose installed.
- Copy the `.env.example` to `.env` and update the values.

### Setup
#### Clone the repository
```bash
git clone https://github.com/aridonkrasniqii/Vikings-App.git
cd Vikings-App
```

#### Copy and update environment variables
```bash
cp .env.example .env
```

#### Build and start the containers
```bash
docker-compose up --build
```

## API Endpoints
### Vikings API
- **Resource URL:** `http://localhost:8000/api/vikings/`

### Norsemen API
- **Resource URL:** `http://localhost:8000/api/norsemen/`

### NFL Players API
- **Resource URL:** `http://localhost:8000/api/nflplayers/`

## Deployment
Provide details on how to deploy the application.

## Contributing
Guidelines for contributing to the project.

## License
Information about the project's license.



