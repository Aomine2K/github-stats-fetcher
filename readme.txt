# GitHub Stats Fetcher

## Description

This is a simple Python script that fetches data from the GitHub API for a given user and displays basic account statistics in a formatted table.

The application is containerized using Docker, so it can be run without installing Python locally.

---

## How to Run

### 1. Build the Docker image

```bash
docker build -t github-stats .
```

### 2. Run the container

```bash
docker run --rm github-stats
```

---

## Configuration

To use your own GitHub account, edit the `USERNAME` variable in `app.py`:

```python
USERNAME = "your_username"
```
