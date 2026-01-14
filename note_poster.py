import requests
import json
import markdown

class NotePoster:
    def __init__(self, session_cookie):
        self.cookies = {"note_session": session_cookie}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def post_article(self, title, body_markdown):
        body_html = markdown.markdown(body_markdown)
        url = "https://note.com/api/v1/text_notes"
        payload = {"name": title, "body": body_html, "status": "draft"}
        
        print("--- NOTE API DEBUG INFO ---" )
        try:
            response = requests.post(url, headers=self.headers, cookies=self.cookies, json=payload)
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}") # ここに本当の原因が表示されます
            
            if response.status_code in [200, 201]:
                data = response.json()
                return data
            else:
                return None
        except Exception as e:
            print(f"Network Error: {e}")
            return None

    def publish_article(self, note_id):
        return True
