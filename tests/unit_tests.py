class Layer1UnitTests:
  def test_weather_data_parser(self):
    # 外部APIからの生データ
    raw_data = {
      "main":{"temp":20.5, "humidity":65},
      "weather":[{"main":"Clear"}]
    }

    # パーサー関数のテスト
    parsed = parse_weather(raw_data)

    assert parsed['temperature'] == 20.5
    assert parsed['condition'] == "Clear"
    assert parsed['humidity'] == 65
  