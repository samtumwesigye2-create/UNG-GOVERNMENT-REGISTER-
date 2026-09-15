# UNG-GOVERNMENT-REGISTER

Uganda National Grid register for 25 government system workspaces.

## Railway

The repository is production-ready for Railway. Railway reads `railway.toml`, installs `requirements.txt`, starts FastAPI with Uvicorn on `$PORT`, and checks `/health`.

## Routes

- `/` — Government systems register UI
- `/health` — deployment health check
- `/api/systems` — machine-readable 25-system registry
- `/{slug}` — registered workspace route for each system

The register currently provides the deployment shell and routes. Each ministry/institution application can be connected to its registered route as its implementation is added.
