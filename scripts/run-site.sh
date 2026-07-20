#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HUGO_DIR="$ROOT_DIR/hugo-site"
PUBLIC_DIR="$HUGO_DIR/public"
PORT="${PORT:-8000}"
BUILD_ONLY=false

while [ "$#" -gt 0 ]; do
  case "$1" in
    --build-only)
      BUILD_ONLY=true
      shift
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    *)
      echo "Usage: $0 [--build-only] [--port <port>]" >&2
      exit 1
      ;;
  esac
done

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

require_cmd hugo
require_cmd python3

echo "Building Hugo site..."
(cd "$HUGO_DIR" && hugo --minify)

if [ "$BUILD_ONLY" = true ]; then
  echo "Site built at $PUBLIC_DIR"
  exit 0
fi

echo "Serving site at http://localhost:$PORT"
cd "$PUBLIC_DIR"
python3 -m http.server "$PORT"
