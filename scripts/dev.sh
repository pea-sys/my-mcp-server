#!/bin/bash
# 開発サーバー起動スクリプト

echo "Starting MCP Development Server..."

# 環境変数の設定
export MCP_LOG_LEVEL=DEBUG
export ENABLE_REMOTE_DEBUG=true

# 仮想環境のアクティベート
source .venv/bin/activate

# 開発サーバーの起動
echo "Server starting with debug mode enabled..."
python -m src.server