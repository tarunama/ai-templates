# AI変更履歴テンプレート

前提テンプレート: operations-runbook.md
後続テンプレート: ai-pr-template.md


## 変更履歴
| 日付 | 種別 | 変更内容 | 目的 | 影響範囲 | 検証結果 | 参照した評価結果ID | 担当 |
|---|---|---|---|---|---|---|---|
| 2026-05-06 | Docs | APM導入 Phase 0 調査を追加 | APM導入前の可否・制約を整理 | README, docs/apm-adoption.md | Markdown構成確認済み | - | Codex |
| 2026-05-06 | Docs | APM導入 Phase 1以降のIssue下書きを追加 | Phase 0以降の作業をIssue化できるようにする | README, docs/apm-adoption.md, docs/issues/ | Markdown構成確認済み | - | Codex |
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
