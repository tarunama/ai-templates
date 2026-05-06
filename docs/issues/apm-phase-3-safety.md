# APM導入 Phase 3: 外部依存とMCPの安全基準

## 背景
APMで外部package、skill、plugin、MCP serverを追加する場合、エージェントの振る舞いや実行権限に影響する可能性があります。追加前に許可基準を定義します。

## スコープ
- 外部依存の許可基準
- version / tag / commit hash 固定の方針
- MCP server の認証情報、ネットワーク通信、実行権限の確認観点
- Safety / Policy テンプレートへの影響確認

## タスク
- [x] 外部依存の信頼性確認項目を定義する
- [x] MCP server追加時の確認項目を定義する
- [x] version固定またはlockfile更新のルールを定義する
- [x] `docs/templates/safety-policy.md` への反映要否を判断する
- [x] `docs/templates/change-log.md` に変更を記録する

## 完了条件
- [x] 外部依存を追加する前のレビューチェックリストがある
- [x] MCP serverを追加する場合の安全確認項目がある
- [x] 追加可否の判断基準がREADMEまたは関連ドキュメントに明記されている

## 依存関係
- Phase 1またはPhase 2でAPMの基本運用が整理されていること

## 実装メモ
- `docs/apm-security-review.md` に外部依存とMCP serverの安全レビュー基準を追加しました。
- `docs/templates/safety-policy.md` にAPM外部依存・MCP安全確認欄を追加しました。
- Phase 3では外部package、MCP server、CI設定は追加していません。
