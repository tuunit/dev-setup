#FROM mcr.microsoft.com/devcontainers/go:1.21-bookworm
FROM mcr.microsoft.com/devcontainers/go:0-1.19

RUN apt-get update && \
    apt-get install -y --no-install-recommends pre-commit vim && \
    mkdir -p /go/pkg && \
    chmod -R a+w /go/pkg
