import logging
import sys
from pathlib import Path

from datetime import datetime

def setup_logging(level="INFO", log_to_file=True):
  """MCPサーバ用のロギング設定

  Args:
      level (str): ログレベル (例: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
      log_to_file (bool): ファイルへのログ出力を有効にするかどうか
  
  Returns:
      logging.Logger: 設定されたロガーオブジェクト
  """

  # ログディレクトリの作成
  log_dir = Path("logs")
  log_dir.mkdir(exist_ok=True)

  # ログフォーマットの定義
  formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

  # ルートロガーの取得とレベル設定
  logger = logging.getLogger("mcp_server")
  logger.setLevel(level)

  # コンソールハンドラーの設定
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)

  # ファイルハンドラーの設定
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)

  # ファイルハンドラーの設定
  if log_to_file:
    log_filename = log_dir / f"mcp_server_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

  return logger

logger = setup_logging(level="DEBUG")