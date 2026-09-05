# ChatGPT Workでの使い方

## この文書について

ChatGPT Workで「DMMビジネスAI研修｜講座概要作成プラグイン」を利用する場合の補助手順です。本プロジェクトの標準ルートはCodexです。ChatGPT Workは、ワークスペース管理者が設定できる場合に使用します。

- 公開リポジトリ：`https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance`
- プラグイン名：DMMビジネスAI研修｜講座概要作成プラグイン
- Skill名：講座概要作成
- Skill ID：`course-overview-generator`

## 重要な制約

- GitHubがPublicでも、利用者が自分でChatGPT Workへプラグインを登録することはできません。
- ワークスペース管理者によるマーケットプレイスのインポートと利用ポリシー設定が必要です。
- 登録はワークスペース単位です。別ワークスペースの利用者には、そのワークスペースの管理者による登録が必要です。
- 管理者と連携できない場合は、[ローカルCodexでの使い方](ローカルCodexでの使い方.md)に切り替えてください。

一般利用者がGitHubアカウントを作成したり、GitHubの招待を承認したりする必要はありません。

## 管理者が行う初回登録

1. ChatGPT Workで「Admin」→「Plugins」を開く。
2. 「Add」→「Import marketplace」を選ぶ。
3. 次の値を入力する。

| 項目 | 入力値 |
|---|---|
| Source | `https://github.com/kogureatsushi-hue/dmm-ai-lecture-guidance` |
| Path | 空欄 |
| Branch, tag, or commit | `main` |

4. GitHubへのアクセスを承認してインポートする。
5. インポート結果で「DMMビジネスAI研修｜講座概要作成プラグイン」を確認する。
6. 利用対象のロールまたはグループに対して、Installation policyを「Available」または「Installed」に設定する。
7. Google Driveを利用する場合は、対象者がGoogle Driveプラグインを使用できることを確認する。

このリポジトリはPublicですが、マーケットプレイスのインポート時にはGitHub接続の承認を求められることがあります。

## 利用者が行うこと

1. ChatGPT Workでプラグイン一覧を開く。
2. 「DMMビジネスAI研修｜講座概要作成プラグイン」を検索する。
3. 表示された場合は「インストール」または「追加」を選ぶ。
4. 新しいチャットで「@」から「講座概要作成」を選ぶ。

管理者が「Installed」として配布している場合、利用者のインストール操作は不要になることがあります。

## 動作確認

~~~text
@講座概要作成
講座概要作成の開始前チェックをしてください。
まだファイルは作成せず、必要な入力情報だけを一覧で示してください。
~~~

必要なPDF、ワーク使用ファイル、講座時間、出力先などが提示されれば、有効化確認は完了です。

## 講座概要を作成する

~~~text
@講座概要作成
講師共有用の講座概要を作成してください。

講座資料：添付のPDF
ワーク使用ファイル：＜Google DriveフォルダURL＞
講座時間：3時間（休憩10分×2回）
出力先：＜Google DriveフォルダURL＞

最初にMarkdownで作業プレビューを作成し、私の確認が終わるまでDOCXへ変換しないでください。
不明な演習時間や講座固有の条件は、推測せず質問してください。
~~~

## 確認の流れ

1. PDFとワーク使用ファイルの読み取り結果を確認する。
2. 演習時間や講座固有条件に関する質問へ回答する。
3. 作業プレビューMDを確認する。
4. 必要な修正を依頼する。
5. 内容を明示的に承認してDOCX作成を依頼する。
6. レイアウトと保存先を確認する。

## 更新の反映

GitHub側の更新は、登録済みマーケットプレイスへ定期的に同期されます。すぐに反映する場合は、管理者が「Admin」→「Plugins」→「Marketplaces」から対象マーケットプレイスを開き、「Sync now」を実行します。

同期後は、プラグインのバージョン、利用対象者、必要なGoogle Driveプラグインの状態を確認してください。

## トラブル時の確認

### プラグインが表示されない

- 管理者によるマーケットプレイス登録が完了しているか確認する。
- 利用者のロールまたはグループに許可されているか確認する。
- プラグイン名「DMMビジネスAI研修｜講座概要作成プラグイン」で検索する。
- 解決できず管理者と連携できない場合はCodex版を使用する。

### GitHubからインポートできない

- SourceがリポジトリURLだけになっているか確認する。
- Pathが空欄、Branchが`main`になっているか確認する。
- GitHub接続を再承認してから再試行する。
- リポジトリがPublicであることを確認する。

### Google Driveを読めない・保存できない

- ChatGPTで接続しているGoogleアカウントを確認する。
- 対象フォルダの閲覧・編集権限を確認する。
- 管理者のアプリ・プラグイン利用ポリシーを確認する。

## 公式情報

- [Plugin management | ChatGPT Learn](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Build skills | ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills)
