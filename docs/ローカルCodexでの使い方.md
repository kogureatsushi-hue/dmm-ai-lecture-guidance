# ローカルCodexでの使い方

> **状態：利用開始前のガイドです。** このリポジトリにはSkill本体が未収録です。リポジトリの取得はできますが、Skillの導入と実行は、本体追加後に行います。

## 対象と前提

対象はCodex CLIまたはCodex IDE拡張の利用者です。Skill表示名は「講座概要作成」、IDは `course-overview-generator` です。

Privateリポジトリへのアクセス、Codexを利用できる環境、講座PDF、ワーク使用ファイル、出力先を用意します。Google Drive連携を使わない場合は、必要な資料をローカルへ準備します。

DOCX生成に必要なライブラリ・セットアップ手順は、原本の実装を確認してから確定します。現段階でPython等の特定バージョンを推測して案内しません。

## GitHubアクセスからSkill有効化まで

### 1. 招待を承認する

招待を受けたGitHubアカウントでログインし、以下のリポジトリのREADMEとdocsを閲覧できることを確認します。

`https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance`

開けない場合は、ログイン中のアカウント、招待承認、URLを確認します。

### 2. リポジトリを取得する

GitHubへの認証が整った環境で実行します。

```bash
git clone https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance.git
cd dmm-ai-lecture-guidance
```

Gitを使わない場合は、GitHubのCodeからZIPを取得する方法もあります。今回の変更が作業ブランチにある間は、そのブランチを選んで確認してください。更新されたREADMEがmainへ反映されるまでは、mainのファイル構成は変わりません。

### 3. 本体と導入先を確認する

**現在はここで停止します。** 既存資料には、Skillの親ディレクトリについて `plugins/course-overview/` と `plugins/dmm-business-ai-course-overview/` の2種類の表記があります。原本未取得のため、導入コマンドのパスはまだ確定していません。

本体追加時に、登録担当者が以下を確定します。

- `SKILL.md` の実在パスとSkill ID。
- references、assets、scriptsなどの参照先。
- ユーザー用Skillとして導入するか、対象プロジェクト内だけで使うか。
- コピーやリンクを使う場合のOS別手順。
- 同名の既存Skillとの重複・上書きを避ける方法。

未確認のパスでインストールを試したり、同名フォルダを削除したりしないでください。

### 4. 本体追加・導入後に有効化を確認する

OpenAI公式では、Codex CLI・IDE拡張で `/skills` または `$` による明示指定が案内されています。実際の一覧に `course-overview-generator` が表示されることを確認してから、以下を依頼します。

```text
$course-overview-generator

講座概要作成の開始前チェックをしてください。
まだファイルの作成や保存は行わず、必要な入力情報だけを一覧で示してください。
```

## 講座ごとの入力と出力を分ける

既存手順書では、次の作業フォルダ構成を想定しています。

```text
work/
└ <course-name>/
   ├ input/
   │  ├ course.pdf
   │  └ work-files/
   └ output/
```

これは入力資料と出力の整理例であり、プラグイン本体の配置ではありません。最新版のPDFを使い、旧版を残す場合はOLDなどへ分けます。パスワード、APIキー、個人情報をリポジトリへコミットしません。

## 本体導入後の利用手順

講座の作業フォルダでCodexを起動するか、そのフォルダをIDEで開きます。

```text
$course-overview-generator

input/course.pdfとinput/work-filesの内容をもとに、講師共有用の講座概要を作成してください。
講座時間：＜全体時間＞
休憩：＜回数と時間＞
最初にoutputへMarkdownの作業プレビューを作成してください。
資料から確定できない演習時間などは質問してください。
私が承認するまでDOCXを作成しないでください。
```

Markdownの5見出し、資料との整合、合計時間、演習名・実施時間、使用ファイル名を確認します。修正後に次のように承認します。

```text
Markdownの内容を確定します。DOCXへ変換し、レイアウトを確認してください。
問題がなければoutputへ保存してください。
```

Google Drive連携が利用できる場合は、その機能と権限を確認して保存します。利用できない環境では、ローカル成果物を確認してから指定のDriveフォルダへ手動アップロードします。

## 更新・問い合わせ

更新は[Skill更新手順](Skill更新手順.md)を確認します。問い合わせには、OS、CLI/IDEの別、リポジトリのコミット、Skill表示の有無、試した操作、機密情報を除いたエラーを添えます。

## この整理版の出典

既存の「ローカルCodexでの使い方.md」「README.md」の確認できた記載をもとに整理しました。原本の全文コピーではありません。資料間のパスの表記差は、実在パスが不明なまま統一せず、未確定として残しています。

公式参照：[Build skills](https://learn.chatgpt.com/docs/build-skills)。確認日：2026-09-05。本Skillのインストール・実行テストは未実施です。
