import requests
import json
import markdown

class NotePoster:
    def __init__(self, session_cookie):
        self.session_cookie = session_cookie
        self.base_url = "https://note.com/api/v1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.cookies = {"note_session": session_cookie}

    def post_article(self, title, body_markdown):
        """
        記事を投稿する（下書きとして作成）
        """
        # MarkdownをHTMLに変換（NOTEのAPIはHTML形式を期待する場合が多い）
        body_html = markdown.markdown(body_markdown)
        
        url = f"{self.base_url}/text_notes"
        payload = {
            "name": title,
            "body": body_html,
            "status": "draft", # 最初は下書きとして作成
            "publish_at": None
        }
        
        response = requests.post(
            url, 
            headers=self.headers, 
            cookies=self.cookies, 
            data=json.dumps(payload)
        )
        
                if response.status_code in [200, 201]:
            print("Successfully created draft!")
            # 成功した場合は、エラーにならないようにデータを返す
            return {"data": response.json().get("data", response.json())}

        else:
            print(f"Failed to post: {response.status_code}")
            print(response.text)
            return None

    def publish_article(self, note_id):
        """
        下書きを公開する
        """
        url = f"{self.base_url}/text_notes/{note_id}/publish"
        response = requests.post(
            url, 
            headers=self.headers, 
            cookies=self.cookies
        )
        
        if response.status_code == 200:
            print("Successfully published article!")
            return True
        else:
            print(f"Failed to publish: {response.status_code}")
            return False
