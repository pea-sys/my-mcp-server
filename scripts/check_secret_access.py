import requests
from datetime import
import json

def check_secret_access_logs(org_name,repo_name,token,days=7):
    """過去n日間のシークレットアクセスログを確認"""

    # Audit APIのエンドポイント
    url = f"https://api.github.com/repos/{org_name}/{repo_name}/audit-log"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 過去７日間のログを取得
    since = (datetime.now() - timedelta(days=days)).isoformat() + "Z"
    params = {
        "phrase":"action_secret",
        "include": "all",
        "since": since
    }

    response = requests.get(url, headers=headers, params=params)
    log

    # 異常なアクセスパターンの検出
    suspicious_activities = []
    for log in logs:
        if log.get('action') == 'secret.access':
          timestamp= datetime.fromisoformat(log['created_at'].replace('Z', '+00:00'))
          if timestamp.hour < 6 or timestamp.hour > 22:
            suspicious_activities.append({
              'time': log['created_at'],
              'actor': log['actor'],
              'ip': log.get('actor_ip', 'Unknown'),
              'secret_name': log.get('secret_name', 'Unknown')
            })
    return suspicious_activities

# 使用例
if __name__ == "__main__":
    suspicious = check_secret_access_logs("myorg", "myrepo", "ghp_xxxxx")
    if suspicious:
        print("警告：以下の異常なアクセスが検出されました：")
        for activity in suspicious:
            print(f" - {activity['time']}: {activity['actor']} ({activity['ip']}) が {activity['secret_name']}にアクセス")