# ローカルCodexでの使い方

## この文書について

この文書は、講座概要作成SkillをCodex CLIまたはCodex IDE拡張で使用する手順をまとめたものです。

Skillの表示名は「講座概要作成」、Skill IDは`course-overview-generator`です。

共有元：`https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance`

## 想定する利用者

- GitHubのPrivateリポジトリを閲覧できる人
- Codex CLIまたはCodex IDE拡張を利用できる人
- Git、ファイル操作、Markdownの確認ができる人
- 必要に応じてGoogle Driveから資料をダウンロードできる人

## ChatGPT Work版との違い

| 項目 | ChatGPT Work | ローカルCodex |
|---|---|---|
| Skillの配布 | 管理者がGitHubのマーケットプレイスを読み込む | リポジトリからSkillをインストールまたは参照する |
| 入力ファイル | チャット添付またはDriveリンク | ローカルファイルまたは利用可能な連携先 |
| 中間成果物 | チャット上のMDと一時ファイル | 作業ディレクトリ内のMD |
| DOCX | Work環境内で生成 | ローカルスクリプトまたは文書作成機能で生成 |
| Drive保存 | 接続済みプラグインから保存 | Drive連携がなければ手動アップロード |

## 事前準備

### 必要なもの

- Codex CLIまたはCodex IDE拡張
- Git
- Privateリポジトリへのアクセス権
- 講座資料PDF
- ワーク使用ファイル一式、または閲覧可能なGoogle Driveフォルダ
- DOCXの保存先

同梱スクリプトは講座概要MDの必須見出しと時間合計を検証するもので、Python 3を使用します。DOCX生成は、利用環境の文書作成機能を使用します。

## GitHubアクセスからSkill有効化まで

本運用では、利用者全員にPrivateリポジトリの閲覧権限を付与します。ローカルCodexの利用者は、次の手順でGitHubへのアクセスからSkillの有効化までを進めます。

| 手順 | 内容 | 完了条件 |
|---:|---|---|
| 1 | リポジトリ管理者から届いたGitHub招待を承認する | 対象リポジトリをブラウザで開ける |
| 2 | READMEと利用手順を確認する | 対象バージョンと前提条件を把握した |
| 3 | リポジトリをcloneする | ローカルにリポジトリが作成された |
| 4 | Skill Installer、リンク、コピーのいずれかでSkillを導入する | SkillフォルダをCodexが参照できる |
| 5 | Codexを起動または再起動する | 最新のSkill情報を読み込んだ |
| 6 | Skill一覧を確認する | course-overview-generatorが表示される |
| 7 | 動作確認用プロンプトを実行する | 必要な入力情報が提示される |

### 1. GitHubの招待を承認する

GitHubから届いたリポジトリ招待を、自分のGitHubアカウントで承認します。共有されたリポジトリURLをブラウザで開き、READMEと「docs」フォルダを閲覧できることを確認してください。

リポジトリを開いたときに404などが表示される場合は、次を確認します。

- 招待を受けたGitHubアカウントでログインしているか
- 招待の承認が完了しているか
- Organization側の追加承認が必要か
- リポジトリURLが正しいか

### 2. リポジトリを取得する

継続的に利用する場合は、更新を取得しやすいGitでのcloneを推奨します。

~~~bash
git clone https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance.git
cd dmm-ai-lecture-guidance
~~~

SSHを使用しない場合は、GitHub上に表示されるHTTPSのclone URLを使用します。

Gitを使わない場合は、「Code」からZIPをダウンロードして展開できます。ただし、更新時は新版を再度ダウンロードする必要があります。

### 3. Skillを導入する

後述の「Skillの入手方法」から、利用環境に合う方法を1つ選びます。初めて利用する人はSkill Installer、リポジトリを継続更新する人はcloneしたフォルダへのシンボリックリンクを推奨します。

### 4. 有効化を確認する

Codexを起動または再起動し、「/skills」または「$」からSkill一覧を確認します。course-overview-generatorが表示されたら、次の確認用プロンプトを実行します。

~~~text
$course-overview-generator

講座概要作成の開始前チェックをしてください。
まだファイルの作成や保存は行わず、必要な入力情報だけを一覧で示してください。
~~~

必要なPDF、ワーク使用ファイル、出力先、講座時間などが提示されれば、有効化確認は完了です。

### 5. 自力で解決できない場合

管理者とのリアルタイム連携を前提にしないため、まずREADMEの導入状況、既知の問題、対象バージョンを確認します。解決しない場合は、GitHubのIssueなど、リポジトリで指定された問い合わせ方法を利用します。

問い合わせには次を含めます。

- 使用環境：Codex CLIまたはIDE拡張
- OS
- リポジトリのバージョンまたはコミット
- 実施した導入方法
- Skill一覧に表示されるか
- エラーメッセージ
- すでに試した対応

## Skillの入手方法

### 方法A：Skill Installerを使用する

Codexでは「$skill-installer」を呼び出し、GitHubリポジトリ内のSkillを指定してインストールできます。Privateリポジトリの場合は、ローカル環境でGitHubへアクセスできる状態にしておきます。

~~~text
$skill-installer

次のGitHubリポジトリにあるcourse-overview-generator Skillをインストールしてください。
リポジトリ：https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance
Skillの場所：plugins/dmm-business-ai-course-overview/skills/course-overview-generator
~~~

インストール後にSkillが表示されない場合は、Codexを再起動します。

### 方法B：リポジトリをクローンして配置する

~~~bash
git clone https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance.git
cd dmm-ai-lecture-guidance
~~~

Skillフォルダをユーザー用Skillディレクトリへコピーするか、シンボリックリンクを作成します。

~~~bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/plugins/dmm-business-ai-course-overview/skills/course-overview-generator" ~/.agents/skills/course-overview-generator
~~~

同名のファイルまたはフォルダが既にある場合、上記のリンク作成は実行せず、既存Skillの入手元とバージョンを確認してください。

### 方法C：リポジトリ内だけで使用する

プロジェクト固有のSkillとして使う場合は、リポジトリの「.agents/skills」配下へSkillを配置します。Codexは、現在の作業ディレクトリからリポジトリルートまでの「.agents/skills」を確認します。

正式なリポジトリ構成では、ChatGPT Work向けプラグインのSkillとローカル用Skillの二重管理が起きないよう、コピーまたはパッケージ処理を自動化します。

## 入力ファイルの準備

Google Drive連携を使用しない場合は、次のように講座単位で作業フォルダを分けます。

~~~text
work/
└ <course-name>/
   ├ input/
   │  ├ course.pdf
   │  └ work-files/
   └ output/
~~~

### ファイル準備のルール

- PDFは最新版だけを「input」に置く。
- 旧版を残す場合は「OLD」フォルダへ分ける。
- ワーク使用ファイルは、Drive上のフォルダ構成をできるだけ維持する。
- パスワード、APIキー、個人情報を含むファイルはリポジトリへコミットしない。
- 講座資料やワークファイルをGit管理する場合は、社内ルールと利用権限を確認する。

## 基本的な使い方

### 1. 講座の作業フォルダでCodexを起動する

~~~bash
cd work/<course-name>
codex
~~~

IDE拡張を使う場合は、同じフォルダをワークスペースとして開きます。

### 2. Skillを明示して依頼する

Codex CLIまたはIDE拡張では、「$」でSkillを指定できます。

~~~text
$course-overview-generator

input/course.pdfとinput/work-filesの内容をもとに、講師共有用の講座概要を作成してください。
講座時間は3時間です。
最初にoutputへMarkdownの作業プレビューを作成してください。
私が承認するまでDOCXを作成しないでください。
資料から確定できない演習時間は質問してください。
~~~

Google Drive連携が利用できる場合は、ローカルの「input/work-files」の代わりにフォルダURLを指定できます。

### 3. 読み取り結果と質問を確認する

CodexがPDF、ワークファイル、既存のファイル名を確認し、章構成と演習候補を整理します。次のような未確定事項があれば、MD完成前またはDOCX化前に回答します。

- 講座全体の時間
- 休憩回数と時間
- 受講生が操作する演習の名称と時間
- ハンズオンと演習の区別
- 講師から事前に案内する内容
- 使用アカウント、AIモデル、プラン制限

### 4. Markdownをレビューする

「output」に作成されたMDを確認します。

~~~text
output/
└ <course-name>_講座概要_作業プレビュー.md
~~~

確認対象は次のとおりです。

- 講座の概要
- 章構成
- タイムテーブル
- ポイント
- 注意点
- 合計時間
- 演習名と受講生の実施時間
- 使用ファイル名
- 資料から確認できない情報の扱い

### 5. DOCX化を承認する

MDが確定したら、次のように依頼します。

~~~text
Markdownの内容を確定します。DOCXへ変換し、レイアウトを確認してください。
問題がなければoutputへ保存してください。
~~~

SkillはDOCXを生成し、ページ画像またはPDFへレンダリングして、表、改ページ、見出し、余白を確認します。

### 6. Google Driveへ保存する

Google Drive連携が利用できる場合は、保存先フォルダを指定してアップロードします。連携がない場合は、「output」に作成されたDOCXを利用者が手動でアップロードします。

## 成果物の例

~~~text
output/
├ <course-name>_講座概要_作業プレビュー.md
└ <course-name>_講座概要.docx
~~~

必要に応じて、検証用PDFやページ画像を一時的に作成します。一時ファイルは完成物と分けて管理します。

## 更新方法

リポジトリをクローンしてシンボリックリンクで使用している場合は、対象リポジトリで更新を取得します。

~~~bash
git pull --ff-only
~~~

コピーして使用している場合は、新版の内容を確認してからSkillフォルダを更新します。既存フォルダを削除または上書きする前に、自分で加えた変更がないか確認してください。

Codexが変更を認識しない場合は、Codexを再起動します。

## トラブル時の確認

### Skillが候補に出ない

- GitHubの招待を承認し、リポジトリを閲覧できるか確認する。
- cloneまたはZIP展開が最後まで完了しているか確認する。
- Skillフォルダ直下に「SKILL.md」があるか確認する。
- 「SKILL.md」にnameとdescriptionがあるか確認する。
- 配置先が「.agents/skills」配下になっているか確認する。
- Codexを再起動する。

### PDFやワークファイルを読めない

- 指定したパスが現在の作業フォルダから参照できるか確認する。
- ファイルが破損していないか、暗号化されていないか確認する。
- Driveリンクの場合は、利用中のアカウントと閲覧権限を確認する。

### DOCXを作成できない

- Pythonと必要ライブラリが導入されているか確認する。
- 生成スクリプトの実行ログを確認する。
- MDを確定する前にDOCX化を依頼していないか確認する。

### 出力内容が別講座と混ざる

- 講座ごとに新しい作業フォルダと会話を使用する。
- 過去講座の資料が「input」に残っていないか確認する。
- サンプル内の講座固有情報を共通ルールとして扱っていないか確認する。

## 公式情報

- [Build skills | ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills)
- [Package your plugin | OpenAI Developers](https://developers.openai.com/plugins/build/plugins)
