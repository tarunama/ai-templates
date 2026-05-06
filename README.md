# ai-templates

## クイックスタート（30分）
1. `docs/templates/prompt-spec.md` をコピーし、目的・入出力・制約を最小限で記入します。
2. `docs/templates/model-decision-record.md` に候補モデル、選定理由、却下理由を記録します。
3. `docs/templates/eval-cases.md` で代表ケースを作成し、初回評価を実施します。
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

## 運用メモ
- Pull Request のタイトルと説明は日本語で記載してください（`.github/pull_request_template.md` を使用）。
- AI変更時は `docs/templates/ai-pr-template.md` を利用してください。
- 変更時は必ず `docs/templates/change-log.md` を更新してください。
- Issue テンプレートは `.github/ISSUE_TEMPLATE/` に配置しています。

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
