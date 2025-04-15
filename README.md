# Snowflake Buildkite Plugin

![Build Status](https://img.shields.io/github/actions/workflow/status/thummisetti/snowflake-buildkite-plugin/build.yml?branch=main)
![License](https://img.shields.io/github/license/thummisetti/snowflake-buildkite-plugin)
![Version](https://img.shields.io/github/v/release/thummisetti/snowflake-buildkite-plugin)

## Overview

The **Snowflake Buildkite Plugin** integrates Snowflake with Buildkite pipelines, enabling seamless execution of Snowflake SQL commands and scripts within your CI/CD workflows.

## Features

- Run SQL queries against Snowflake within Buildkite pipelines
- Automate schema migrations and data updates
- Secure authentication via environment variables
- Supports multiple Snowflake accounts

## Installation

To use this plugin, add the following to your `pipeline.yml`:

```yaml
steps:
  - label: "Run Snowflake Query"
    plugins:
      - thummisetti/snowflake-buildkite-plugin#v1.0.0:
          account: "my-snowflake-account"
          user: "buildkite_user"
          password: "BUILDKITE_PLUGIN_SNOWFLAKE_PASSWORD"
          database: "my_database"
          schema: "public"
          sql: "SELECT * FROM my_table;"
```

## Usage Examples

### Running a Query

```yaml
steps:
  - label: "Fetch Data"
    plugins:
      - thummisetti/snowflake-buildkite-plugin#v1.0.0:
          sql: "SELECT COUNT(*) FROM users;"
```

### Executing a Script

```yaml
steps:
  - label: "Run SQL Script"
    plugins:
      - thummisetti/snowflake-buildkite-plugin#v1.0.0:
          script: "migrations/schema_update.sql"
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

## License

This project is licensed under the [MIT License](LICENSE).

## Support

For issues and feature requests, please open an issue in the [GitHub repository](https://github.com/thummisetti/snowflake-buildkite-plugin/issues).

## Roadmap

Planned enhancements include:
- Support for stored procedures
- Enhanced error handling
- Integration with secrets managers

Stay tuned for updates!

