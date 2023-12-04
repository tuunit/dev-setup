FROM mcr.microsoft.com/devcontainers/go:1.21-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends pre-commit vim && \
    mkdir -p /go/pkg && \
    chmod -R vscode:golang /go/pkg

RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash && \
    go install sigs.k8s.io/kind@v0.19.0
