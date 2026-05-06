# APM導入 Phase 5: 通常運用への展開

## 背景
PoC、ドキュメント反映、安全基準、CI検討が完了した後、APMを通常のテンプレート運用に組み込みます。

## スコープ
- APM関連変更を通常PRフローへ組み込む
- 運用Runbookへの反映
- AI変更向けPRテンプレートへの反映要否判断
- 継続的な更新・監査サイクルの整理

## タスク
- [ ] `docs/templates/operations-runbook.md` への反映要否を判断する
- [ ] `docs/templates/ai-pr-template.md` への反映要否を判断する
- [ ] APM関連変更時のレビュー観点を整理する
- [ ] lockfile更新時のレビュー観点を整理する
- [ ] `docs/templates/change-log.md` に変更を記録する

## 完了条件
- [ ] APM関連変更が通常のPR運用で扱える
- [ ] RunbookまたはREADMEに継続運用手順が明記されている
- [ ] APM設定、lockfile、外部依存、MCP追加のレビュー観点が整理されている

## 依存関係
- Phase 1〜4の判断結果が整理されていること
