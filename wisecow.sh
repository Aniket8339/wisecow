#!/bin/bash
PORT=4499

if ! command -v cowsay &> /dev/null; then
    echo "cowsay not found!"
    exit 1
fi

if ! command -v fortune &> /dev/null; then
    echo "fortune not found!"
    exit 1
fi

echo "Starting wisecow on port $PORT"

while true; do
    message=$(fortune | cowsay)
    response="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n$message"
    echo -e "$response" | nc -l -p $PORT -q 1
    sleep 0.1
done