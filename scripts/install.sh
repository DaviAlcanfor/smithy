#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv não encontrado. Instale com: sudo dnf install -y uv" >&2
    exit 1
fi

uv tool install --force "$repo_root"
