import time
import functools
from typing import Callable, Any
import traceback

def log_execution_time(func: Callable) -> Callable:
    """関数の実行時間を測定してログ出力するデコレーター"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        func_name = func.__name__
        try:
          result = await func(*args, **kwargs)
          execution_time = time.time() - start_time
          logger.info(f"{func_name} took {execution_time:.3f}s")

          # 実行時間が長い場合の警告ログ
          if execution_time > 5.0: 
              logger.warning(f"{func_name} took {execution_time:.3f}s - "
                             "consider optimizing")
          return result
        except Exception as e:
          execution_time = time.time() - start_time
          logger.error(f"{func_name} failed afterafter {execution_time:.3f}s: {e}\n"
                        f"{traceback.format_exc()}")
          raise
      return wrapper