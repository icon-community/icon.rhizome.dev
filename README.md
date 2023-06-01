# RHIZOME Governance Tracker

This project implements a governance tracker for the ICON network.

## How to Run Locally

1. Clone the repo.
2. From the project directory, run `npm install` to install JS dependencies.
3. From the project directory, run `poetry shell` and `poetry install` to install the Python dependencies.
4. Run a local instance with `npm run dev`.

## How to Deploy

A Dockerfile is included with the project. For easy deployment to Fly.io, a `fly.toml` is included as well – just run `flyctl launch`.