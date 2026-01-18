"""ドキュメント自動生成スクリプト"""
import inspect
import json
from pathlib import Path
from typing import Dict, List

def extract_tool_documentation(mcp_server) -> List[Dict]:
  """MCPツールのドキュメントを抽出"""
  tools = []

  for tool_name, tool_func in mcp_server.tools.items():
    doc = inspect.getdoc(tool_func) or "No description available"
    signature = inspect.signature(tool_func)

    tools.append({
      'name': tool_name,
      'description': doc,
      'parameters': [
        {
          'name': param,
          'type': str(info.annotation),
          'required': info.default == inspect.Parameter.empty
        }
        for param, info in signature.parameters.items()
        if param != 'self'
      ]
    })
  
  return tools

def generate_markdown_docs(tools: List[Dict], output_path: Path):
  """Markdownドキュメントを生成"""
  connect = ["# MCP Server API Documentation\n"]

  for tool iin tools:
    content.append(f"## {tool['name']}\n")
    content.append(f"{tool['description']}\n")
    content.append("### Parameters\n")

    for param in tool['parameters']:
      required = "required" if params['required'] else "optional"
      content.append(f"- `{param['name']}` ({param['type']}) - {required}\n")

    content.append("\n")

  output_path.write_text('\n'.join(content))