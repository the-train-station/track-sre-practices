#!/bin/bash
# Traffic generator: hits the app endpoints with realistic patterns.
# More reads than writes, varied timing between requests.

APP_URL="http://app:8080"

echo "Waiting for app to be ready..."
until curl -sf "$APP_URL/" > /dev/null 2>&1; do
  sleep 1
done
echo "App is ready. Generating traffic..."

while true; do
  # 50% GET /
  curl -sf "$APP_URL/" > /dev/null 2>&1
  sleep 0.1

  # 35% GET /api/data
  if [ $((RANDOM % 100)) -lt 70 ]; then
    curl -sf "$APP_URL/api/data" > /dev/null 2>&1
    sleep 0.1
  fi

  # 15% POST /api/submit
  if [ $((RANDOM % 100)) -lt 30 ]; then
    curl -sf -X POST "$APP_URL/api/submit" > /dev/null 2>&1
    sleep 0.1
  fi

  # Vary the pace slightly
  sleep "0.$(( RANDOM % 3 + 1 ))"
done
