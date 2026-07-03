#!/bin/bash

echo "============================================"
echo "🚨 ADVANCED DEVOPS MONITORING AUTOMATION 🚨"
echo "============================================"

echo -e "\n🔍 Checking Backend Container Status..."

# Step 1: Run a targeted Docker command to check if python_app is running
# The '-q' flag means 'quiet'—it just checks for the container ID cleanly
docker compose ps backend_app | grep "Up" > /dev/null 2>&1

# Step 2: Grab the exit code of that Docker command immediately!
STATUS_CODE=$?

# Step 3: Use conditional logic to handle the result
if [ $STATUS_CODE -eq 0 ]; then
    echo "✅ SUCCESS: backend_app container is up and responsive."
    echo "--------------------------------------------"
    echo "📋 Recent Application Activity:"
    docker compose logs backend_app --tail 3
else
    echo "❌ CRITICAL ERROR: backend_app container is DOWN or UNREACHABLE!"
    echo "--------------------------------------------"
    echo "⚠️ Alerting engineering team... (Simulated)"
fi

echo -e "\n============================================"
