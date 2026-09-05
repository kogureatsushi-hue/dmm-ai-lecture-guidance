# DMMビジネスAI研修｜講座概要作成プラグイン

講座資料PDFとワーク使用ファイルをもとに、講師共有用の「講座概要」を作成するCodex向けSkillです。

- 公開リポジトリ：`kogureatsushi-hue/dmm-ai-lecture-guidance`
- 標準の利用環境：Codex CLI／IDE拡張／ChatGPTデスクトップアプリのCodex
- 補助的な利用環境：ChatGPT Work（ワークスペース管理者による登録が必要）
- Skill ID：`course-overview-generator`
- バージョン：0.1.2

## できること

1. 講座資料PDFとワーク使用ファイルを確認する。
2. 「講座の概要」「章構成」「タイムテーブル」「ポイント」「注意点」を整理する。
3. 演習とハンズオンを区別し、不明な演習時間を利用者へ確認する。
4. 作業プレビューMDを作成する。
5. 利用者の承認後にDOCXへ変換する。
6. 利用環境に応じてローカルまたはGoogle Driveへ保存する。

## 最短の利用開始手順

### 1. CodexでSkillをインストールする

Codexを開き、次のように依頼します。

~~~text
$skill-installer を使って、次の公開リポジトリからSkillをインストールしてください。
https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance/tree/main/plugins/dmm-business-ai-course-overview/skills/course-overview-generator
~~~

このPublicリポジトリからSkillをインストールして使用するだけなら、GitHubアカウントは必要ありません。

インストール後、次のターンでSkillを利用できます。候補に表示されない場合はCodexを再起動してください。

### 2. Skillを確認する

Codex CLIまたはIDE拡張で`/skills`を実行するか、入力欄で`$course-overview-generator`を検索します。

### 3. 講座概要を作成する

~~~text
$course-overview-generator を使って、講座概要を作成してください。

講座資料：添付のPDF
ワーク使用ファイル：＜ローカルフォルダまたはGoogle DriveフォルダURL＞
講座時間：3時間（休憩10分×2回）
出力先：＜ローカルフォルダまたはGoogle DriveフォルダURL＞

最初に作業プレビューMDを作成し、私の確認が終わるまでDOCXへ変換しないでください。
不明な演習時間や講座固有の条件は、推測せず質問してください。
~~~

詳しい操作は[Codexでの使い方](docs/Codexでの使い方.md)を確認してください。

## 利用方法の選び方

| 利用方法 | 推奨度 | 管理者設定 | 主な用途 |
|---|---:|---:|---|
| Codex＋Skill Installer | 推奨 | 不要 | 各利用者が自分で導入して講座概要を作成する |
| Codex＋Git clone | 更新担当者向け | 不要 | Skillの修正、テスト、Pull Request作成 |
| ChatGPT Work | 任意 | 必要 | 同一ワークスペース内へプラグインとして配布する |

GitHubリポジトリはPublicです。閲覧・ダウンロードにGitHubからの招待は必要ありません。ChatGPT Workで利用する場合だけ、ワークスペース管理者がマーケットプレイスを登録して利用ポリシーを設定します。詳細は[ChatGPT Workでの使い方](docs/ChatGPT-Workでの使い方.md)を確認してください。

## 入力資料の扱い

この公開リポジトリへ、実際の作業で使用する次の情報をコミットしないでください。

- 顧客名、個人情報、認証情報、APIキー
- 公開許可のない講座PDF、ワークファイル、完成成果物
- アクセス制限付きURLや、URL自体を秘密情報として扱う共有リンク
- 社内限定の手順、未公開情報、契約上公開できない情報

入力資料と生成物は、利用者の作業フォルダまたはアクセス制限されたGoogle Driveで管理します。`examples`には公開確認済みの参考資料だけを収録します。

## リポジトリ構成

~~~text
.
├ .agents/plugins/marketplace.json
├ plugins/dmm-business-ai-course-overview/
│  ├ .codex-plugin/plugin.json
│  └ skills/course-overview-generator/
│     ├ SKILL.md
│     ├ agents/openai.yaml
│     ├ references/
│     ├ assets/
│     └ scripts/validate_course_overview.py
├ examples/
├ docs/
├ CHANGELOG.md
└ README.md
~~~

## サンプルの扱い

`examples`には、Google Antigravity Day1・Day2で作成した講座概要を収録しています。構成、情報量、DOCXの見た目を確認するための参考資料です。講座固有の製品名、時間、注意事項を、新しい講座へそのまま流用しないでください。

## 更新と問い合わせ

更新担当者は[Skill更新手順](docs/Skill更新手順.md)に従い、ブランチとPull Requestを使用してください。変更内容は`CHANGELOG.md`へ記録します。

不具合や改善提案はGitHub Issueへ、機密情報を除いて次を記載してください。

- 使用環境とSkillのバージョン
- 入力資料の種類
- 実行した依頼内容
- 期待した結果と実際の結果
- 再現に必要な最小限の情報

## 関連文書

- [Codexでの使い方](docs/Codexでの使い方.md)
- [ChatGPT Workでの使い方](docs/ChatGPT-Workでの使い方.md)
- [Skill更新手順](docs/Skill更新手順.md)
- [初回登録チェックリスト](docs/初回登録チェックリスト.md)
