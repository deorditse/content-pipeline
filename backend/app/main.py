"""FastAPI placeholder for the content pipeline backend."""

try:
    from fastapi import FastAPI
except ImportError:  # keep placeholder import-safe before deps are installed
    FastAPI = None


if FastAPI is not None:
    app = FastAPI(title="Content Pipeline API", version="0.0.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}
else:
    app = None
