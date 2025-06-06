#!/bin/bash

# Automated installer for ngrok v3 (Linux 64-bit)
echo "🔧 Downloading ngrok v3..."
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

echo "📦 Extracting ngrok archive..."
tar -xvzf ngrok-v3-stable-linux-amd64.tgz

echo "🚀 Moving ngrok binary to /usr/local/bin..."
sudo mv ngrok /usr/local/bin

echo "✅ Installation complete. Verifying version..."
ngrok version
