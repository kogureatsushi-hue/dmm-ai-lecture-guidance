# Codexでの使い方

## この文書について

公開GitHubリポジトリから「講座概要作成」Skillをインストールし、Codexで講座概要を作成する手順です。初めて利用する方は、上から順に進めてください。

- リポジトリ：`https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance`
- Skill ID：`course-overview-generator`
- Skillの場所：`plugins/dmm-business-ai-course-overview/skills/course-overview-generator`

## 事前準備

- Codex CLI、対応するIDE拡張、またはChatGPTデスクトップアプリを利用できること
- GitHubへアクセスできること
- 講座資料PDFとワーク使用ファイルを閲覧できること
- DOCXを作成する場合は、成果物を保存できる作業フォルダがあること

Skillは、以下の公開URLをCodexへ伝えてインストールします。

## 推奨：Skill Installerで導入する

### 1. インストールを依頼する

Codexで次の内容を実行します。

~~~text
$skill-installer を使って、次の公開リポジトリからSkillをインストールしてください。
https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance/tree/main/plugins/dmm-business-ai-course-overview/skills/course-overview-generator
~~~

### 2. Skillを確認する

インストール完了後、次のターンで利用できます。Codex CLIまたはIDE拡張では`/skills`を実行するか、入力欄で`$course-overview-generator`を検索します。

表示されない場合はCodexを再起動し、再度確認してください。

### 3. 動作確認をする

~~~text
$course-overview-generator を使って、講座概要作成の開始前チェックをしてください。
まだファイルは作成せず、必要な入力情報だけを一覧で示してください。
~~~

講座資料、ワーク使用ファイル、講座時間、出力先などが提示されれば導入確認は完了です。

## 更新担当者：リポジトリをcloneする

Skillや手順書を変更する担当者は、リポジトリをcloneします。

~~~bash
git clone https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance.git
cd dmm-ai-lecture-guidance
~~~

変更はmainへ直接行わず、作業ブランチとPull Requestを使用してください。Skillを実際の利用環境へ導入するときは、前項のSkill Installerを使用します。

## 入力ファイルを準備する

Google Drive連携を使用しない場合は、講座ごとに作業フォルダを分けます。

~~~text
＜講座名＞/
├ input/
│  ├ course.pdf
│  └ work-files/
└ output/
~~~

- `input`には、その講座で使用するPDFとワークファイルだけを置きます。
- `output`には作業プレビューMDと、承認後のDOCXを保存します。
- 別講座の入力ファイルや古い版を同じフォルダへ混在させないでください。
- 顧客情報、個人情報、APIキーなどを公開リポジトリへコミットしないでください。

## 講座概要を作成する

講座の作業フォルダでCodexを開き、次のように依頼します。

~~~text
$course-overview-generator を使って、講師共有用の講座概要を作成してください。

講座資料：input/course.pdf
ワーク使用ファイル：input/work-files
講座時間：3時間（休憩10分×2回）
出力先：output

最初にMarkdownで作業プレビューを作成し、私の確認が終わるまでDOCXへ変換しないでください。
不明な演習時間や講座固有の条件は、推測せず質問してください。
~~~

Google Drive連携が利用できる場合は、ローカルパスの代わりに閲覧可能なフォルダURLと保存先URLを指定できます。

## 確認の流れ

1. CodexがPDFとワーク使用ファイルを確認する。
2. 不足資料や不明な演習時間について質問する。
3. 作業プレビューMDを作成する。
4. 利用者が内容、時間、注意点を確認して修正を依頼する。
5. 利用者が明示的に承認する。
6. CodexがDOCXを作成し、レイアウトを確認する。
7. 指定のローカルフォルダまたはGoogle Driveへ保存する。

MDでは、少なくとも次を確認してください。

- 「講座の概要」「章構成」「タイムテーブル」「ポイント」「注意点」がある。
- 演習とハンズオンが区別されている。
- 演習名と受講生の実施時間が内容列にある。
- 講座時間、休憩、各区分の合計が一致している。
- PDFやワークファイルにない情報を事実として追加していない。
- 講師が事前に伝える内容と進行上の注意が具体的である。

## Skillを更新する

Skill Installerで導入した利用者は、`CHANGELOG.md`で更新内容を確認してから最新版を再導入します。既存のSkillがあるため再導入できない場合は、Codexが案内するインストール先を確認し、`course-overview-generator`だけを更新してください。ほかのSkillや設定は削除しないでください。

cloneしている更新担当者は、次のコマンドで最新版を取得します。

~~~bash
git switch main
git pull --ff-only
~~~

更新が認識されない場合はCodexを再起動します。

## トラブル時の確認

### Skillが表示されない

- インストール結果にエラーがなかったか確認する。
- URLがSkillフォルダまで含まれているか確認する。
- `/skills`または`$course-overview-generator`で検索する。
- Codexを再起動する。

### PDFやワークファイルを読めない

- ファイルパスが正しいか確認する。
- Codexから読み取れる作業フォルダ内にあるか確認する。
- Google Driveの場合は、接続と閲覧権限を確認する。

### DOCXを作成できない

- MDの内容を明示的に承認したか確認する。
- 出力先への書き込み権限を確認する。
- DOCX作成後のレイアウト確認まで依頼しているか確認する。

### 別講座の情報が混ざる

- 講座ごとに新しい作業フォルダを使用する。
- 過去講座の入力ファイルが`input`に残っていないか確認する。
- サンプルの固有情報を新しい講座へ流用していないか確認する。

## 公式情報

- [Build skills | ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills)
- [Package your plugin | OpenAI Developers](https://developers.openai.com/plugins/build/plugins)
