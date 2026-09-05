# 更新履歴

## 0.1.1 - 2026-09-05

- リポジトリをPublicで配布する運用へ変更。
- Codex＋Skill Installerを標準の利用方法に変更。
- GitHubへの利用者招待を前提とする記述を削除。
- ChatGPT Workを、ワークスペース管理者が設定できる場合の補助ルートとして整理。
- README、Codex利用手順、ChatGPT Work利用手順、Skill更新手順、初回登録チェックリストを更新。
- 公開リポジトリへ顧客情報、認証情報、公開許可のない講座資料を保存しないルールを明記。
- 利用者側の移行作業：既存利用者はCHANGELOGを確認し、必要に応じてSkillを最新版へ更新する。

## 0.1.0 - 2026-09-05

- 「DMMビジネスAI研修｜講座概要作成プラグイン」の初期構成を作成。
- `course-overview-generator` Skillを追加。
- PDFとワーク使用ファイルの確認ルールを追加。
- 講座概要の5見出しとタイムテーブル作成ルールを追加。
- MD確認後にWordへ変換する承認ゲートを追加。
- 必須見出しとタイムテーブル合計を確認する検証スクリプトを追加。
- ChatGPT Work、ローカルCodex、Skill更新の手順書を追加。
- Google Antigravity Day1・Day2のサンプルを追加。
- GitHubリポジトリ`kogureatsushi-hue/dmm-ai-lecture-guidance`の初回登録ブランチへ統合。
- Skill ID、配布設定、実在パス、相対リンクの整合を確認。
- Day1・Day2の講座概要MDに対して検証スクリプトを実行。両方とも合計180分で、Day2は未確定の演習時間1件を警告として検出。

### 未実施

- ChatGPT Workへのマーケットプレイスインポートと同期
- ChatGPT WorkでのSkill呼び出し
- ローカルCodexへのインストールとSkill呼び出し
- 新しい講座資料を使ったMD作成からDOCX保存までの通しテスト
