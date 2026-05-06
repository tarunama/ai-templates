# APM導入 Phase 2: ドキュメント反映

## 背景
Phase 1のPoC結果を利用者が再現できるように、APMの利用手順を既存ドキュメントへ反映します。

## スコープ
- README の APM導入計画セクション更新
- 必要に応じた `docs/apm-adoption.md` の更新
- テンプレート利用順や変更履歴との関係整理

## タスク
- [x] Phase 1の検証結果を確認する
- [x] 初回セットアップ手順をREADMEに追記する
- [x] `apm.yml` / `apm.lock.yaml` の更新ルールを明記する
- [x] 既存のクイックスタート手順との関係を明記する
- [x] `docs/templates/change-log.md` に変更を記録する

## 完了条件
- [x] 利用者がREADMEだけでAPM利用開始手順を把握できる
- [x] APM関連ファイル更新時の記録先が明確になっている
- [x] 既存テンプレート運用との優先関係が明確になっている

## 依存関係
- Phase 1のPoC結果が整理されていること

## 実装メモ
- READMEにAPMの位置づけ、初回セットアップ、更新ルールを追加しました。
- `docs/templates/README.md` にAPM利用時の補足を追加しました。
- Phase 2では外部package、MCP server、CI設定は追加していません。
