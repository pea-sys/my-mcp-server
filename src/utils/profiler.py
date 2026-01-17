import cProfile
import pstats
from contextlib import contextmanager
from pathlib import Path

@contextmanager
def profile(name="profile", top_n=10):
  """コードのプロファイリングを行うコンテキストマネージャー

  Args:
    name: プロファイル結果のファイル名
    top_n: 表示する上位N個の結果
  """
  profiler = cProfile.Profile()
  profile.enable()

  try:
    yield profile
  finally:
    profile.disable()
    
    # 結果の集計
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")

    # コンソールに出力
    print(f"\n===Performance Profile: {name} ===")
    stats.print_stats(top_n)

    # ファイルに保存
    profile_dir = Path(f"prifiles")
    profile_dir.mkdir(exist_ok=True)
    stats.dump_stats(profile_dir / f"{name}.prof")