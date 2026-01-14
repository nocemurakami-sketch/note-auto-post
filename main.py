import os
import sys
from content_generator import generate_content
from note_poster import NotePoster
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    # 環境変数から設定を取得
    note_session = os.getenv("NOTE_SESSION")
    topic = os.getenv("POST_TOPIC", "最新のテクノロジー動向")
    
    if not note_session:
        print("Error: NOTE_SESSION is not set in environment variables.")
        sys.exit(1)
        
    print(f"Generating content for topic: {topic}...")
    title, body = generate_content(topic)
    
    print(f"Title: {title}")
    
    poster = NotePoster(note_session)
    
    print("Creating draft on NOTE...")
    result = poster.post_article(title, body)
    
    if result and 'data' in result:
        note_id = result['data']['id']
        print(f"Draft created with ID: {note_id}")
        
        # 公開フラグが立っている場合は公開する
        if os.getenv("AUTO_PUBLISH") == "true":
            print("Publishing article...")
            poster.publish_article(note_id)
        else:
            print("Article saved as draft. Please check it on NOTE.")
    else:
        print("Failed to create article.")

if __name__ == "__main__":
    main()
