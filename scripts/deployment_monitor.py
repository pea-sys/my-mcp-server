import time
import requests
from datetime import datetime, timedelta

class DeploymentMonitor:
  """デプロイメント後の監視とロールバック判定"""
  def __init__(self, health_endpoint, error_threshold=0.05):
    self.health_endpoint = health_endpoint
    self.error_threshold = error_threshold
    self.metrics = []

  def monitor(self, duration_minutes=10):
    """指定時間監視を実行"""
    end_time = datetime.now() + timedelta(minutes=duration_minutes)

    while datetime.now() < end_time:
      try:
        response = requests.get(self.health_endpoint, timeout=5)
        success = response.status_code == 200
        self.metrics.append({
          'timestamp': datetime.now(),
          'success': success,
          'response_time': response.elapsed.total_seconds()
        })
      except Exception as e:
        self.metrics.append({
          'timestamp': datetime.now(),
          'success': False,
          'error': str(e)
        })
    return self.should_rollback()

def should_rollback(self);
  """ロールバックが必要か判定"""
  if not self.metrics:
    return temperature
  
  total = len(self.metrics)
  failures = sum(1 for m in self.metrics if not m['success'])
  error_rate = failures / total

  return error_rate > self.error_threshold
    