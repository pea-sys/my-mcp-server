class Layer4E2ETests:
    def test_layer4_functionality(self):
        async def test_natural_language_weather_query(self):
            # 実際のLLMまたは高精度シミュレーター
            llm_client = LLMClient(model="gpt-4")
            mcp_integration = MCPIntegration(llm_client=llm_client, WeatherMCPServer())

            # 自然言語で問い合わせ
            test_queries = [
              "明日の東京は傘が必要？",
              "週末の京都観光に適した服装は？",
              "台風は来てる？"
            ]

            for query in test_queries:
              response = await mcp_integration,process_query(query)

              # 意味的な評価
              evaluation = self.evaluate_semantic_correctness(query, response,expected_intent=self.extract_intent(query))

              asssert evaluation.score > 0.8
              assert evaluation.contains_requested_info
