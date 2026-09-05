# DMMビジネスAI研修｜講座概要作成プラグイン

講座資料PDFとワーク使用ファイルをもとに、講師共有用の「講座概要」を作成するChatGPT Work／Codex向けプラグインです。

リポジトリ：`kogureatsushi-hue/dmm-ai-lecture-guidance`
対象者：講師、講座制作メンバー、プラグイン管理者

## 現在の状態

| 項目 | 状態 |
|---|---|
| プラグイン名 | DMMビジネスAI研修｜講座概要作成プラグイン |
| プラグインID | `dmm-business-ai-course-overview` |
| Skill表示名 | 講座概要作成 |
| Skill ID | `course-overview-generator` |
| バージョン | 0.1.0 |
| プラグイン本体・配布設定 | 収録済み。静的検証済み |
| reference・テンプレート・検証スクリプト | 収録済み |
| Day1・Day2サンプル | MD／DOCXを収録済み |
| ChatGPT Workへのインポート | 未実施 |
| 利用対象者・グループ | 未設定 |
| 最終同期 | 未実施 |
| ローカルCodexでの実呼び出し | 未実施 |

## できること

1. 講座資料PDFとワーク使用ファイルを確認する。
2. 講座概要、章構成、タイムテーブル、ポイント、注意点を整理する。
3. 不明な演習時間などを利用者へ確認する。
4. 作業プレビューMDを作成する。
5. 利用者の承認後、Word形式へ変換する。
6. 指定されたGoogle Driveフォルダへ保存する。

## 利用開始までの流れ

### ChatGPT Work

1. GitHubの招待を承認する。
2. このREADMEで、ChatGPT Workへのインポート状況を確認する。
3. プラグイン一覧から「DMMビジネスAI研修｜講座概要作成プラグイン」をインストールする。
4. 新しいチャットで「講座概要作成」を選択する。
5. 講座資料PDF、ワーク使用ファイル、講座時間、保存先を指定する。

管理者がインストール済みの状態で配布した場合、手順3は不要です。詳細は[ChatGPT-Workでの使い方](docs/ChatGPT-Workでの使い方.md)を確認してください。

### ローカルCodex

GitHubからリポジトリを取得し、`plugins/dmm-business-ai-course-overview/skills/course-overview-generator`をCodexから参照できる状態にします。詳細は[ローカルCodexでの使い方](docs/ローカルCodexでの使い方.md)を確認してください。

## 基本的な依頼例

~~~text
講座概要を作成してください。

講座資料：添付のPDF
ワーク使用ファイル：＜Google DriveフォルダURL＞
講座時間：3時間（休憩10分×2回）
出力先：＜Google DriveフォルダURL＞

最初に作業プレビューMDを作成し、確認後にWordへ変換してください。
~~~

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
│  └ 初回登録チェックリスト.md
├ CHANGELOG.md
└ README.md
~~~

## サンプルの扱い

`examples`には、Google Antigravity Day1・Day2で作成した講座概要を収録しています。構成、粒度、Wordの見た目を確認するための参考資料です。講座固有の製品名、時間、注意事項を、新しい講座へそのまま流用しないでください。

## 更新

Skillやreferenceを更新する場合は、[Skill更新手順](docs/Skill更新手順.md)に従ってください。更新内容は`CHANGELOG.md`へ記録します。

初回登録の検証状況と、ChatGPT Workへ配布する前に残っている作業は[初回登録チェックリスト](docs/初回登録チェックリスト.md)で確認できます。

## 問い合わせ

不具合や改善提案は、対象リポジトリのIssueへ次を記載してください。

- 使用環境（ChatGPT Work／ローカルCodex）
- プラグインのバージョン
- 入力資料の種類
- 実行した依頼内容
- 期待した結果と実際の結果
- 機密情報を除いたエラー内容
