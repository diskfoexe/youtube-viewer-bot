#!/usr/bin/env bash

# Exit on error
set -e

echo "Installing Google Chrome..."

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

echo "✅ Chrome installed."
echo "🔍 Checking Chrome installation..."
which google-chrome || echo "❌ google-chrome not found"
google-chrome --version || echo "❌ google-chrome not available"
