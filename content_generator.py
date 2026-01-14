import os
from openai import OpenAI

def generate_content(topic="最新のテクノロジー動向"):
    """
    OpenAI APIを使用して記事のタイトルと本文を生成する
    """
    client = OpenAI() # 環境変数 OPENAI_API_KEY を使用
    
    prompt = f"""
    あなたはプロのブロガーです。
    テーマ: {topic}
    
    以下の形式でNOTEの記事を生成してください。
    
    【タイトル】
    (ここに魅力的なタイトル)
    
    【本文】
    (ここに読者の興味を引く、有益な内容の本文。Markdown形式で。)
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "あなたは有益な情報を発信するNOTEクリエイターです。"},
            {"role": "user", "content": prompt}
        ]
    )
    
    full_text = response.choices[0].message.content
    
    # タイトルと本文を分離（簡易的な実装）
    try:
        title_part = full_text.split("【タイトル】")[1].split("【本文】")[0].strip()
        body_part = full_text.split("【本文】")[1].strip()
    except IndexError:
        title_part = f"{topic}について"
        body_part = full_text
        
    return title_part, body_part

if __name__ == "__main__":
    title, body = generate_content()
    print(f"Title: {title}")
    print(f"Body length: {len(body)}")
