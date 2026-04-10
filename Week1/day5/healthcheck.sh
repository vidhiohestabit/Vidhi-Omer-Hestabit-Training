#!/bin/bash

URL="http://localhost:3000"
LOG_FILE="./logs/health.log"

while true
do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

  if [ "$STATUS" -ne 200 ]; then
    echo "$(date) ❌ Server DOWN (status: $STATUS)" >> "$LOG_FILE"
  fi

  sleep 10
done
