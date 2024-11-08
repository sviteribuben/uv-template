# UV CI Template

A FastAPI project template with UV package manager and CI integration.

## 🚀 Features

- FastAPI web framework
- UV package manager for dependency management
- Docker support
- Ruff for code formatting and linting
- Pytest for testing
- Logging configuration

## 📋 Prerequisites

- Python 3.13+
- Docker Desktop
- UV package manager

## 🛠 Installation

1. Clone the repository:

-----

Install project dependencies:

```bash
uv sync
```

## Development

### Local Development

1. Run FastAPI application locally:

```bash
uv run uvicorn main:app --port 8000 --reload
```

2. Run code formatting and linting:

```bash
uv run ruff format .
```
3. Run tests:
```bash
uv run pytest
```
### Docker Development

Build and run the application in Docker:
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## ⚙️ Configuration

- Project dependencies and settings are managed in `pyproject.toml`
- Ruff is configured for code formatting and linting
- Pytest is set up for testing
- Logging configuration is available for different environments

## 🌐 API Endpoints

- `GET /`: Returns a "Hello from FastAPI!" message

## 🧪 Testing

Tests are located in the `tests/` directory. Run the test suite using:
```bash
uv run pytest
```


## 🔍 Project Structure
```
uv-ci-template/
|── main.py # FastAPI application
├── tests/
│ └── tests.py # Test suite
├── Dockerfile # Docker configuration
├── pyproject.toml # Project configuration
├── uv.lock # Libs and dependencies
└── README.md
```


## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📫 Contact

[@Sviteribuben](https://t.me/Sviteribuben) - Dmitry Boldyrev
