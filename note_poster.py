import requests
import json
import markdown

class NotePoster:
    def __init__(self, session_cookie):
        self.session_cookie = session_cookie
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Note-Session": session_cookie, # ヘッダーにもセッションを入れる
            "Cookie": f"note_session={session_cookie}" # Cookieを文字列として直接指定
        }

    def post_article(self, title, body_markdown):
        body_html = markdown.markdown(body_markdown)
        url = "https://note.com/api/v1/text_notes"
        payload = {"name": title, "body": body_html, "status": "draft"}
        
        print("--- NOTE API DEBUG INFO ---" )
        try:
            # cookiesパラメータを使わず、headersに含めたCookieで送信
            response = requests.post(url, headers=self.headers, json=payload)
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
            
            if response.status_code in [200, 201]:
                return response.json()
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def publish_article(self, note_id):
        return True
