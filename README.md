# ai-templates

## クイックスタート（30分）
1. `docs/templates/prompt-spec.md` をコピーし、目的・入出力・制約を最小限で記入します。
2. `docs/templates/model-decision-record.md` に候補モデル、選定理由、却下理由を記録します。
3. `docs/templates/eval-cases.md` で代表ケースを作成し、`python3 scripts/run-eval.py --eval-file docs/templates/eval-cases.md` で評価結果を生成します。
4. `docs/templates/safety-policy.md` を確認し、リスクとガードレールを更新します。
5. `docs/templates/ai-pr-template.md` を使って PR を作成します。

## 変更内容と更新テンプレート
| 変更内容 | 更新するテンプレート |
| --- | --- |
| Prompt 変更時 | `docs/templates/prompt-spec.md`, `docs/templates/eval-cases.md` |
| Model 変更時 | `docs/templates/model-decision-record.md`, `docs/templates/eval-cases.md` |
| 評価ケース変更時 | `docs/templates/eval-cases.md` |
| Safety / Policy 変更時 | `docs/templates/safety-policy.md`, `docs/templates/eval-cases.md` |
| 運用手順変更時 | `docs/templates/operations-runbook.md` |
| AI変更の PR 作成時 | `docs/templates/ai-pr-template.md` |

## 評価結果の生成
- 評価ケースの「判定 (Pass/Fail)」列を記入したあと、次のコマンドで PR に貼り付ける評価結果を生成します。

  ```bash
  python3 scripts/run-eval.py --eval-file docs/templates/eval-cases.md
  ```

- 未記入テンプレートの構造確認だけを行う場合は `--allow-template` を付けます。

## CIでの評価
- GitHub Actions の `Evaluation` ワークフローで、Pull Request と `main` への push 時に評価ケース Markdown を確認します。
- 既定では `docs/templates/eval-cases.md` を `--allow-template` 付きで実行し、テンプレート未記入でも構造確認として扱います。
- 手動実行時は `eval_file` 入力で評価対象 Markdown を指定できます。
- 評価結果は GitHub Actions の Step Summary に出力されます。

## 運用メモ
- Pull Request のタイトルと説明は日本語で記載してください（`.github/pull_request_template.md` を使用）。
- AI変更時は `docs/templates/ai-pr-template.md` を利用してください。
- 変更時は必ず `docs/templates/change-log.md` を更新してください。
- Issue テンプレートは `.github/ISSUE_TEMPLATE/` に配置しています。

## APM導入計画
- Phase 0 調査: `docs/apm-adoption.md`
- Phase 1 最小構成PoC: `apm.yml`
- Phase 1以降のIssue下書き: `docs/issues/README.md`

### APMの位置づけ
- APMは既存のクイックスタートや `docs/templates/` の利用順を置き換えず、エージェント設定を再現しやすくする補助手段として利用します。
- 初期導入では外部packageやMCP serverを追加せず、最小構成から検証します。

### 初回セットアップ
1. APM CLIをインストールし、`apm --version` で利用可能なことを確認します（macOS/Linux: `curl -sSL https://aka.ms/apm-unix | sh`、Windows PowerShell: `irm https://aka.ms/apm-windows | iex`）。
2. 変更内容を確認するため、まず `apm install --dry-run` を実行します。
3. 問題がなければ `apm install` を実行します。
4. `apm.lock.yaml` が生成または更新された場合は、`git diff -- apm.yml apm.lock.yaml` で差分を確認します。
5. テンプレート評価の構造確認として `python3 scripts/run-eval.py --eval-file docs/templates/eval-cases.md --allow-template` を実行します。

### APM関連ファイルの更新ルール
- `apm.yml` を変更した場合は、APM CLIを利用できる環境で `apm install --dry-run` と `apm install` を確認してください。
- `apm.lock.yaml` は `apm install` が安定して成功し、差分を確認できた時点でコミット対象にします。
- 外部packageやMCP serverの追加は、Phase 3で安全基準を定義してから実施します。
- APM関連ファイルを追加・変更する場合は、`docs/templates/change-log.md` に変更内容を記録してください。

## Codexでの利用
- Codex はリポジトリ直下の `AGENTS.md` をプロジェクト指示ファイルとして参照します。
- このリポジトリは Markdown テンプレート中心のため、変更時はリンク先・見出し・表記ゆれなどの軽量な静的確認を実施してください。
- 振る舞いや使い方が変わる場合は `README.md` と `docs/templates/change-log.md` を更新してください。

## AIドキュメントテンプレート
- 利用順ガイド: `docs/templates/README.md`
- Prompt 要件定義: `docs/templates/prompt-spec.md`
- 評価ケース: `docs/templates/eval-cases.md`
- 安全性ポリシー: `docs/templates/safety-policy.md`
- モデル選定記録: `docs/templates/model-decision-record.md`
- 運用Runbook: `docs/templates/operations-runbook.md`
- 変更履歴: `docs/templates/change-log.md`
- AI変更向けPRテンプレート: `docs/templates/ai-pr-template.md`
