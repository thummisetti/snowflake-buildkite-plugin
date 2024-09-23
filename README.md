# Snowflake CI/CD SQL Deployment

This repository provides a CI/CD pipeline to automatically deploy SQL DDL to a Snowflake instance when changes are merged to the `master` branch.

## Setup Instructions

### 1. Add Snowflake Credentials

Make sure to add your Snowflake credentials as environment variables, either in your CI/CD pipeline or locally when running the deployment.

#### Required Environment Variables:
- `SNOWFLAKE_USER`: Your Snowflake username.
- `SNOWFLAKE_PASSWORD`: Your Snowflake password.
- `SNOWFLAKE_ACCOUNT`: Your Snowflake account identifier (e.g., `xy12345.us-east-1`).
- `SNOWFLAKE_WAREHOUSE`: The Snowflake warehouse to use.
- `SNOWFLAKE_DATABASE`: The target database.
- `SNOWFLAKE_SCHEMA`: The target schema.

In Buildkite, you can configure these environment variables in your pipeline settings or use a `.env` file.

### 2. Prepare SQL DDL

Place your SQL DDL statement in the `your_ddl.sql` file. This will be executed in your Snowflake instance when the pipeline runs.

### 3. Running Locally

To test the deployment locally, you can use Docker to simulate the pipeline execution:

```bash
docker-compose up --build
```
This will install the dependencies, connect to Snowflake using the provided credentials, and execute the SQL DDL.

### 4. CI-CD Pipeline

When changes are pushed to the master branch, the Buildkite pipeline will automatically trigger and deploy the SQL DDL to Snowflake.

Ensure that the Buildkite pipeline is set up with the .buildkite/pipeline.yml configuration.
Ensure that the required Snowflake environment variables are provided in the Buildkite environment.
On every merge to master, the pipeline will install the dependencies and execute the SQL deployment.

### 5. Troubleshooting

If the deployment fails, ensure that:

The Snowflake credentials are correct and properly passed as environment variables.
The SQL DDL in your_ddl.sql is valid and does not contain syntax errors.
