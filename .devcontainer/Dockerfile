# A small Linux environment with Python pre-installed.
# Using an official Python image keeps setup simple for beginners.
FROM python:3.12-slim

# Install a few basics (git for cloning repos, curl for downloads).
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    bash \
  && rm -rf /var/lib/apt/lists/*

# Install Python packages needed for the demo.
RUN pip install --no-cache-dir pandas matplotlib

# Create a non-admin user (so accidental "system-level" changes are harder).
RUN useradd -m -s /bin/bash codex

USER codex
WORKDIR /workspaces
