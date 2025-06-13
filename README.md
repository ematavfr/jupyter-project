# Multi-Project Development Environment

This setup provides a containerized development environment with Traefik reverse proxy, allowing you to access multiple projects via clean URLs.

## Quick Start

1. Start the environment:
   ```bash
   docker-compose up -d
   ```

2. Access services in your browser:
   - **JupyterLab**: http://sites/jupyter
   - **Traefik Dashboard**: http://localhost:8080
   - No password required (token disabled for local development)

3. Stop the environment:
   ```bash
   docker-compose down
   ```

## Directory Structure

- `notebooks/` - Your Jupyter notebooks will be saved here
- `data/` - Place your data files here
- `docker-compose.yml` - Docker configuration with Traefik

## Features

- **Reverse Proxy**: Traefik for routing multiple projects
- **Clean URLs**: Access projects via http://sites/<project-name>
- **JupyterLab**: Data science notebook with Python, R, Julia
- **Persistence**: Notebooks and data are saved to local directories
- **Auto-restart**: Containers restart automatically unless stopped
- **Scalable**: Easy to add new projects

## Adding New Projects

To add a new project (e.g., a web app), add it to the docker-compose.yml:

```yaml
  myapp:
    image: nginx:alpine
    container_name: myapp
    networks:
      - sites
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.myapp.rule=Host(`sites`) && PathPrefix(`/myapp`)"
      - "traefik.http.routers.myapp.entrypoints=web"
      - "traefik.http.services.myapp.loadbalancer.server.port=80"
```

Then access it at: http://sites/myapp

## Requirements

- Docker
- Docker Compose
- `/etc/hosts` entry: `127.0.0.1 sites` (already configured)

