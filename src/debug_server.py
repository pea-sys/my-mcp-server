import os
import debugpy

def setup_debugging():
    """リモートデバッグを有効化"""
    if os.getenv("ENABLE_REMOTE_DEBUGGER", "").lower() == "true":
        debug_port = int(os.getenv("DEBUG_PORT", "5678"))
        debugpy.listen(("0.0.0.0", debug_port))
        print(f"Remote debugging enabled on port {debug_port}. Waiting for client to attach...")

        if os.getenv("WAIT_FOR_DEBUGGER", "").lower() == "true":
            debugpy.wait_for_client()
            print("Client attached, continuing execution.")

if __name__ == "__main__":
    setup_debugging()
    #MCPサーバーの起動コードをここに追加