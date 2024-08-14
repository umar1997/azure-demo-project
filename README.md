# Azure Demo Project


## Application Architecture
![Architecture](./Images/architecture.png)


## Azure Services

![AzureServices](./Images/azure-services.png)

## **[Azure Blob Storage Documentation](demoStorage/README.md)**
## **[Azure Container Registrty Documentation](demoContainerRegistry/README.md)**
## **[Azure PostgreSQL Database Documentation](demoPostgres/README.md)**
## **[Azure VM Documentation](demoApp/README.md)**
## **[Azure Function Documentation](demoAzureFunction/README.md)**


## Running the Application

### On Azure VM
1. SSH into the VM from your Local System (Enabling Port Forwarding on the Application Port)
```shell
ssh -L 15085:localhost:15080 umar-admin@20.174.10.146
# You will be prompted to give your password
umar-admin@20.174.10.146's password:
```

2. Pull the Docker Image from the ACR
```shell
sudo docker pull aiappliedsciences.azurecr.io/team_app:latest     
```

3. Run the docker-compose to start the application
```shell
docker compose -f docker/docker-compose-azure.yaml up -d
```

4. Close the application
```shell
docker compose -f docker/docker-compose-azure.yaml down
```

## On Local System
1. Git Clone the Repo
```shell
git clone https://github.com/umar1997/azure-demo-project.git
```

2. Create a virtual environment and install python libraries
```shell
python3 -m venv demoEnv
```
```shell
source demoEnv/bin/activate
```
```shell
pip install -r requirements.txt
```

3. Create a .env_azure file (Path: ~/azure-demo-project/demoApp/.env)
```shell
POSTGRES_CONNECTION_STRING=postgresql://umar:umar_password@db:5432/demo_postgres_db
BLOB_STORAGE_CONTAINER_NAME=team-data
BLOB_STORAGE_ACCOUNT_NAME=readinggroupstorage
BLOB_STORAGE_ACCOUNT_KEY=LWl*************AStrR5/DQ==
```

4. Build the docker image
```shell
docker build -f docker/Dockerfile.app -t umar/demo_app:base .
```

5. Run the docker-compose to start the application
```shell
docker compose -f docker/docker-compose-local.yaml up -d
```

6. Close the application
```shell
docker compose -f docker/docker-compose-local.yaml down
```
