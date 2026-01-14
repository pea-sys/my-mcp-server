import asyncio
import importlib.metadata
import mcp
from mcp.server import Server
import mcp.types as types

async def test_installation():
    """MCPインストールの検証"""
    print("MCPインストールテスト開始...")

    # バージョンの確認
    print(f"MCPバージョン: {importlib.metadata.version('mcp')}")

    # サーバー作成のテスト
    try:
        server = Server("test_server")
        print("サーバー作成成功")
    except Exception as e:
        print(f"サーバー作成失敗: {e}")
        return 

    @server.list_tools()
    async def test_tool() -> list[types.TextContent]:
        return [types.TextContent(text="Hello MCP!")]
    
    print("✓ ツール登録成功")
    print("\nインストール完了!MCPサーバー開発の準備が出来ました。")

if __name__ == "__main__":
    asyncio.run(test_installation())