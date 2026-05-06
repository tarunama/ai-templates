# AIドキュメントテンプレート利用順

以下の順番でテンプレートを利用してください。

1. `prompt-spec.md`
2. `model-decision-record.md`
3. `eval-cases.md`
4. `safety-policy.md`
5. `operations-runbook.md`
6. `change-log.md`
7. `ai-pr-template.md`

## APM利用時の補足
- APMはエージェント設定の再現性を高める補助手段です。上記のテンプレート利用順は変更しません。
- `apm.yml` または `apm.lock.yaml` を変更した場合は、`change-log.md` に変更内容を記録してください。
- 外部packageやMCP serverの追加は、安全基準を確認してから実施してください。
