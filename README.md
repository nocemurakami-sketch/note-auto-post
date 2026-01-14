# NOTE 自動投稿システム

このシステムは、AI（OpenAI）を使用して記事を自動生成し、NOTEに自動投稿（または下書き保存）するシステムです。GitHub Actionsを利用してクラウド上で定期実行されます。

## 機能
- **AI記事生成**: 指定したトピックに基づき、OpenAI APIを使用してタイトルと本文を生成します。
- **自動投稿**: 生成した記事をNOTEの非公式API経由で投稿します。
- **スケジュール実行**: GitHub Actionsにより、毎日決まった時間に自動実行されます。

## セットアップ方法

### 1. NOTEのセッション情報の取得
1. ブラウザでNOTEにログインします。
2. デベロッパーツール（F12）を開き、「Application」タブの「Cookies」から `https://note.com` を選択します。
3. `note_session` という名前のCookieの値をコピーします。

### 2. GitHubリポジトリの設定
1. このコードを自分のGitHubリポジトリにアップロードします。
2. リポジトリの `Settings` > `Secrets and variables` > `Actions` に移動します。
3. 以下の `Repository secrets` を登録します：
   - `OPENAI_API_KEY`: OpenAIのAPIキー
   - `NOTE_SESSION`: 先ほどコピーした `note_session` の値

### 3. 動作設定
`.github/workflows/auto_post.yml` 内の環境変数を調整することで、動作を変更できます。
- `POST_TOPIC`: 記事のテーマ
- `AUTO_PUBLISH`: `true` で即時公開、`false` で下書き保存

## 注意事項
- このシステムはNOTEの非公式APIを使用しています。仕様変更により動作しなくなる可能性があります。
- 自動投稿による規約違反等には十分ご注意ください。
