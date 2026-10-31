# TP04: Containerization and Big Data Environment Deployment Using Docker

**Module:** Big Data Analytics  
**Department:** Computer Science, Faculty of Exact Sciences, University of Eloued  
**Master 2:** AI & Data Science (2026/2027)  

---

## 📌 Educational Objectives
- Understand Docker images, containers, volumes, networks, and port mapping.
- Manage Docker containers with basic CLI commands.
- Build custom Docker images for data processing pipelines.
- Orchestrate environments using Docker Compose.

---

## 🛠 Tasks Implementation

### Task 1 & 2: Image Creation, Push & Pull
- Built a custom Python environment using a `Dockerfile`.
- Pushed and pulled the image to/from Docker Hub: `touahriahouda4/tp3-analytics:v1`.

### Task 3: Containers, Network & Port Mapping
- Created an isolated bridge network: `tp04-net`.
- Launched 3 containers (`c1`, `c2`, `c3`) attached to the network with host port bindings (`8081`, `8082`, `8083`).
- Verified network connectivity and IP assignments via `docker network inspect`.

### Task 4: Docker Compose Deployment
- Defined application services and volume mappings using `compose.yaml`.
- Executed lifecycle management:
  - `docker compose up --build`
  - `docker compose ps -a`
  - `docker compose down`

---

## 📝 Answers to Questions & Lab Report

### Task 5 Questions:
1. **What problem does Docker Compose solve?**  
   Docker Compose simplifies managing multi-container Docker applications. Instead of running numerous complex `docker run` commands with repetitive network, port, and volume flags, Compose allows declarative configuration in a single YAML file, launching and shutting down the entire stack with unified commands.

2. **Comparison between `docker run` and `docker compose up`:**
   - `docker run`: Operates on a single container at a time; configurations are passed via command-line flags, which is error-prone for distributed systems.
   - `docker compose up`: Manages multi-container stacks, builds images, creates networks, and mounts volumes declaratively based on a configuration file.

3. **How could you extend the Compose project to include a database service?**  
   By adding a database definition (e.g., PostgreSQL or MongoDB) under the `services:` block, establishing shared networks, setting environment variables for credentials, and mounting a persistent volume for database storage.

### Summary Questions:
- **What is Docker, and why is it useful in data-science projects?**  
  Docker is a platform for containerizing applications within lightweight, portable environments. In Data Science, it eliminates the "it works on my machine" issue, guarantees reproducibility across different development/production setups, and resolves dependency conflicts between ML and big data libraries.
- **Difference between a Docker image and a container:**  
  A **Docker Image** is a read-only, immutable template containing the OS layer, runtime, dependencies, and code. A **Docker Container** is a runnable, isolated runtime instance created from that image with a read-write layer.
- **Purpose of Dockerfile instructions:**  
  - `FROM`: Defines the base image.
  - `WORKDIR`: Sets the working directory inside the container.
  - `COPY`: Copies files from the host machine to the container file system.
  - `RUN`: Executes build-time commands (e.g., installing packages).
  - `CMD`: Specifies the default command executed when the container starts up.
