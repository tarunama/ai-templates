# APM導入 Phase 3: 外部依存とMCPの安全基準

## 背景
APMで外部package、skill、plugin、MCP serverを追加する場合、エージェントの振る舞いや実行権限に影響する可能性があります。追加前に許可基準を定義します。

## スコープ
- 外部依存の許可基準
- version / tag / commit hash 固定の方針
- MCP server の認証情報、ネットワーク通信、実行権限の確認観点
- Safety / Policy テンプレートへの影響確認

## タスク
- [ ] 外部依存の信頼性確認項目を定義する
- [ ] MCP server追加時の確認項目を定義する
- [ ] version固定またはlockfile更新のルールを定義する
- [ ] `docs/templates/safety-policy.md` への反映要否を判断する
- [ ] `docs/templates/change-log.md` に変更を記録する

## 完了条件
- [ ] 外部依存を追加する前のレビューチェックリストがある
- [ ] MCP serverを追加する場合の安全確認項目がある
- [ ] 追加可否の判断基準がREADMEまたは関連ドキュメントに明記されている

## 依存関係
- Phase 1またはPhase 2でAPMの基本運用が整理されていること
