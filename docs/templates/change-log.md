# AI変更履歴テンプレート

前提テンプレート: operations-runbook.md
後続テンプレート: ai-pr-template.md


## 変更履歴
| 日付 | 種別 | 変更内容 | 目的 | 影響範囲 | 検証結果 | 参照した評価結果ID | 担当 |
|---|---|---|---|---|---|---|---|
| 2026-05-06 | Docs | APM導入 Phase 0 調査を追加 | APM導入前の可否・制約を整理 | README, docs/apm-adoption.md | Markdown構成確認済み | - | Codex |
| 2026-05-06 | Docs | APM導入 Phase 1以降のIssue下書きを追加 | Phase 0以降の作業をIssue化できるようにする | README, docs/apm-adoption.md, docs/issues/ | Markdown構成確認済み | - | Codex |
| 2026-05-06 | APM/AgentConfig | APM導入 Phase 1 最小構成PoCを実装 | 外部依存なしでAPM manifestを導入 | apm.yml, .gitignore, README, docs/apm-adoption.md, docs/issues/apm-phase-1-poc.md | YAML/Markdown構成確認済み | - | Codex |
| 2026-05-06 | Docs | APM導入 Phase 2 ドキュメント反映を実装 | APM利用手順と既存テンプレート運用の関係を明確化 | README, docs/apm-adoption.md, docs/templates/README.md, docs/issues/apm-phase-2-docs.md | Markdown構成確認済み | - | Codex |
| 2026-05-06 | Safety | APM導入 Phase 3 安全レビュー基準を実装 | 外部依存とMCP server追加時の許可基準を明確化 | README, docs/apm-adoption.md, docs/apm-security-review.md, docs/templates/safety-policy.md, docs/issues/apm-phase-3-safety.md | Markdown構成確認済み | - | Codex |
| 2026-05-06 | Eval | 評価ケースMarkdownをCIで確認するワークフローを追加 | PRとmain更新時に評価結果を自動生成する | .github/workflows/evaluation.yml, README | `python3 scripts/run-eval.py --eval-file docs/templates/eval-cases.md --allow-template` 実行済み | - | Codex |
| 2026-05-06 | APM/AgentConfig | APM導入 Phase 4 CIワークフローを追加 | APM関連変更時にCLI導入とdry-runを確認する | .github/workflows/apm.yml, docs/templates/change-log.md | YAML構成確認済み | - | Codex |
| YYYY-MM-DD | Prompt/Model/Eval/Safety/Docs/APM/AgentConfig |  |  |  |  |  |  |

## 種別ごとの記録
### Prompt変更
- 変更前:
- 変更後:
- 想定影響:

### Model変更
- 変更前:
- 変更後:
- 想定影響:

### Eval変更
- 変更前:
- 変更後:
- 想定影響:
- 検証コマンド: `python3 scripts/run-eval.py --eval-file <評価ケースMarkdown>`

### Safety変更
- 変更前:
- 変更後:
- 想定影響:

### Docs変更
- 変更前:
- 変更後:
- 想定影響:

### APM/AgentConfig変更
- 変更前:
- 変更後:
- 対象ファイル:
- 想定影響:
- 検証コマンド: `apm install` または `apm audit`
