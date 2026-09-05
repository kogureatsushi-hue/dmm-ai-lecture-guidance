# Skill更新手順

## この文書について

公開リポジトリで管理する「講座概要作成」Skillを更新し、Codex利用者へ安全に配布するための手順です。ChatGPT Workへの反映は補助手順として扱います。

- 正本：`kogureatsushi-hue/dmm-ai-lecture-guidance`の`main`
- Skill ID：`course-overview-generator`
- プラグインID：`dmm-business-ai-course-overview`

## 基本方針

- Publicリポジトリの`main`を正本とする。
- 閲覧・インストールは公開し、書き込みは管理者と更新担当者に限定する。
- mainを直接編集せず、作業ブランチとPull Requestを使用する。
- Skill本体、reference、テンプレート、検証処理、利用手順を同じリポジトリで管理する。
- 利用者の端末にインストールされたSkillを直接編集しない。
- 共通ルールと講座固有情報を分ける。
- 実際の講座PDF、顧客ファイル、認証情報、非公開URLをコミットしない。
- 出力形式に影響する変更では、MDとDOCXの両方を確認する。

## 役割

| 役割 | GitHub権限 | 主な作業 |
|---|---|---|
| リポジトリ管理者 | 管理 | 権限管理、ブランチ保護、リリース管理 |
| Skill更新担当者 | 書き込み | ブランチ作成、更新、テスト、Pull Request作成 |
| レビュー担当者 | レビュー | 変更内容、テスト結果、出力品質の確認 |
| 一般利用者 | 不要 | PublicリポジトリからSkillを導入し、Issueを報告 |
| ChatGPT Work管理者 | 原則不要 | 必要な場合のみマーケットプレイス登録・同期・配布設定 |

## ファイルごとの役割

| 変更内容 | 主な更新先 |
|---|---|
| Skillの発動条件、入力、処理順、質問・停止条件 | `SKILL.md` |
| 構成、タイムテーブル、確認基準 | `references/` |
| MD・DOCXの定型フォーマット | `assets/` |
| 時間計算や検証などの確定処理 | `scripts/` |
| 公開確認済みの回帰テスト用資料 | `examples/` |
| 利用者・管理者向け手順 | `docs/`、`README.md` |
| プラグイン名、バージョン、同梱Skill | `.codex-plugin/plugin.json` |
| ChatGPT Work向けの配布一覧 | `.agents/plugins/marketplace.json` |

## 更新手順

### 1. 変更内容を整理する

Issueまたは作業メモへ、次を記録します。

- 現在の問題と期待する動作
- 変更対象と影響範囲
- 確認に使う公開可能なサンプル
- 完了条件と利用者側の対応

機密情報を含む入力ファイルやスクリーンショットは、PublicなIssueへ添付しないでください。

### 2. 最新版と作業ブランチを用意する

~~~bash
git switch main
git pull --ff-only
git switch -c update/<short-description>
~~~

ローカルに未コミットの変更がある場合は、内容を確認してから進めます。利用者の変更を破棄しないでください。

### 3. 適切なファイルを更新する

- 発動条件や処理順を変える：`SKILL.md`
- 判断基準や文章ルールを変える：`references/`
- 見た目や定型フォーマットを変える：`assets/`
- 確定的な計算・変換を変える：`scripts/`
- 利用方法だけを変える：`docs/`または`README.md`

講座固有の製品名、モデル名、プラン制限などは共通ルールへ固定せず、入力資料から確認する規則として記述します。

### 4. 構文と安全性を確認する

- `SKILL.md`のfrontmatterに`name`と`description`がある。
- references、assets、scriptsへの参照パスが存在する。
- `marketplace.json`と`plugin.json`が有効なJSONである。
- 存在しないツール、ファイル、権限を前提にしていない。
- APIキー、認証情報、個人情報、顧客情報、非公開URLがない。
- `examples`へ追加する資料の公開許可を確認している。

### 5. 動作テストを行う

| テスト | 確認内容 |
|---|---|
| 明示呼び出し | `$course-overview-generator`を指定して動く |
| 間接呼び出し | 対象業務をdescriptionから認識できる |
| 不完全な入力 | 不足情報を推測せず質問できる |
| 対象外の依頼 | 関係のない依頼で誤作動しない |
| 境界ケース | 矛盾、欠損、複数版がある場合に安全に止まれる |

回帰確認では、少なくとも次を確認します。

- 必須の5見出しがある。
- 演習とハンズオンが区別されている。
- 演習名と受講生の実施時間がタイムテーブルにある。
- 講座時間、休憩、各区分の合計が一致している。
- MDの承認前にDOCXを作成していない。
- DOCXの表、見出し、余白、改ページが崩れていない。
- 指定した保存先以外へ書き込んでいない。

### 6. 文書、バージョン、変更履歴を更新する

利用方法や出力形式が変わる場合は、README、利用手順、サンプルも同じPull Requestで更新します。

プラグインはセマンティックバージョニングを基本とします。

| 種別 | 例 | バージョン |
|---|---|---|
| 誤字、説明補足、互換性のある修正 | 1.0.0 → 1.0.1 | PATCH |
| 新しい入力形式や機能の追加 | 1.0.0 → 1.1.0 | MINOR |
| 必須入力や出力形式の非互換変更 | 1.0.0 → 2.0.0 | MAJOR |

`.codex-plugin/plugin.json`のversionと`CHANGELOG.md`を更新します。

### 7. Pull Requestを作成する

~~~bash
git status
git diff
git add <変更したファイル>
git commit -m "Update course overview workflow"
git push -u origin update/<short-description>
~~~

Pull Requestには次を記載します。

- 変更理由と変更ファイル
- 変更前後の利用方法
- 実施したテスト
- 利用者への影響と更新方法
- ロールバック方法

### 8. レビューしてmainへ反映する

変更内容、根拠、確認ゲート、公開可否、他講座への影響を確認します。承認後にmainへマージし、必要に応じてタグを作成します。

## 利用環境への反映

### Codex（標準）

- 新規利用者：READMEのURLを指定してSkill Installerから導入する。
- 既存利用者：CHANGELOGを確認して最新版へ更新する。
- 更新が認識されない場合：Codexを再起動する。

### ChatGPT Work（任意）

登録済みの場合は、ワークスペース管理者が「Admin」→「Plugins」→「Marketplaces」で「Sync now」を実行します。同期後、バージョンと利用ポリシーを確認します。

## ロールバック

問題が見つかった場合はmain上のファイルを直接書き戻さず、revert用のPull Requestを使用します。

1. 問題が発生したコミットまたはバージョンを特定する。
2. 直前の安定版を確認する。
3. revert用ブランチを作成する。
4. 回帰テストを行う。
5. Pull Requestをマージし、CHANGELOGへ記録する。

## 更新時に行わないこと

- mainブランチを直接編集する。
- 利用者の端末にあるSkillだけを修正する。
- 根拠のない仕様を標準ルールとして追加する。
- MD確認前にDOCXを自動公開する。
- APIキー、認証情報、個人情報、顧客情報をコミットする。
- 公開許可のないPDF、ワーク素材、成果物を追加する。
- テストせずバージョンだけを更新する。

## リリース確認表

| 項目 | 確認 |
|---|---|
| 変更理由と完了条件が明確である | □ |
| 変更対象が適切である | □ |
| Skillの構文と参照パスを確認した | □ |
| 起動テストと回帰確認を行った | □ |
| 公開できない情報がない | □ |
| READMEと利用手順を更新した | □ |
| バージョンとCHANGELOGを更新した | □ |
| Pull Requestで差分を確認した | □ |
| mainへの反映を確認した | □ |
| Codexで最新版を確認した | □ |
| 必要な場合のみChatGPT Workを同期した | □ |

## 公式情報

- [Build skills | ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills)
- [Package your plugin | OpenAI Developers](https://developers.openai.com/plugins/build/plugins)
- [Plugin management | ChatGPT Learn](https://learn.chatgpt.com/docs/enterprise/plugin-management)
