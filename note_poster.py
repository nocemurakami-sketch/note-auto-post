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
        
        print(f"Sending request to NOTE..." )
        response = requests.post(url, headers=self.headers, cookies=self.cookies, json=payload)
        
        if response.status_code in [200, 201]:
            data = response.json()
            # 投稿成功時にIDを表示して、確実に届いたか確認できるようにする
            note_id = data.get('data', {}).get('id', 'unknown')
            print(f"Successfully created draft! ID: {note_id}")
            return data
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    def publish_article(self, note_id):
        return True # 今回は下書き確認を優先するため簡略化
