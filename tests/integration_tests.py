class Layer2IntegrationTests:
    async def test_mcp_tool_registration(self):
        # MCPサーバーの初期化
        mcp_server = WeatherMCPServer()

        # ツールが登録されていることを確認
        tools = await mcp_server.list_tools()
        assert "get weather" in [t.name for t in tools]

        # ツールのスキーマを検証
        weather_tool = next(t for t in tools if t.name == "get weather")
        assert "city" in weather_tool.schema["properties"]
        assert weather_tool.para,eters.required == ["city"]