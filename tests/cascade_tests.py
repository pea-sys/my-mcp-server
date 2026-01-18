class Layer3CascadeTests:
  async def test_travel_planning_cascade(self):
    # 旅行計画；複数のツールを連携
    mcp_server = TravelPlanningMCPServer()

    # シナリオ：東京から大阪への旅行
    context = {
      "origin": "Tokyo",
      "destination": "Osaka",
      "date": "2024-07-15"
    }

    # 一連の呼び出しをシミュレート
    weather_result = await mcp_server.call_tool("get weather", {"city": "Osaka", "date", context["date"]})

    transport_result = await mcp_server.call_tool("seach_transport", {"from": context["origin"], "to": context["destination"]})

    #結果の整合性を検証
    assert weather_result["status"] == "success"
    assert transport_result["option"] is not None
    assert len(transport_result["option"]) > 0