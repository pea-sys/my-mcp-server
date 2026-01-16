from datetime import datetime
from typing import Dict, List, Any
import json

class ErrorTracker:
    def __init__(self):
        self.errors: List[Dict[str, Any]] = []
        self.error_count: Dict[str, int] = {}

    def log_error(self, error:Exception , context: Dict[str, Any]) ->  None:
      error_type = type(error).__name__

      error_info = {
          "timestamp": datetime.utcnow().isoformat(),
          "type": error_type,
          "message": str(error),
          "context": context,
          "stack_trace": traceback.format_exc()
      }
      # エラーリストに追加
      self.errors.append(error_info)
      #エラーカウントを更新
      self.error_count[error_type] = self.error_count.get(error_type, 0) + 1
      # ログに記録
      logger.error(f"Error tracked: {json.dumps(error_info, indent=2)}")
      #特定のエラーが頻発している場合はアラート
      if self.error_count[error_type] > 10:
          logger.critical(f"Error {error_type} has occured {self.error_count[error_type]} times.")

    def get_error_summary(self) -> Dict[str, Any]:
      """エラーの統計情報を取得"""
        return {
            "total_errors": len(self.errors),
            "error_counts": self.error_count,
            "recent_errors": self.errors[-10:]  # 最新5件のエラー
        }


    error_tracker = ErrorTracker()
    