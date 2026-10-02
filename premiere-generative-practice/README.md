# Premiere Generative Media Tool: 生成前の練習セット

確認日: 2026-10-02。Python 3.9以降の標準ライブラリだけで入力ファイルを確認できます。
このセットはPremiereの設定へ自動適用されません。クラウド生成・課金・クレジット消費を実行しません。
Premiereでの生成と出力の品質は未確認です。生成結果の動画も同梱していません。

## ファイル

- `video-prompt.txt`: 架空の無地の箱を描く独自の依頼例。個人情報、ブランド、撮影者の体験は含めません。
- `settings-record.csv`: 実際の画面で選んだモデル・設定・見積クレジットなどを書き込む記録表。初期値はUNCONFIRMEDで、推奨設定ではありません。
- `review-checklist.md`: 生成後に形、位置、動き、設定、用途を確認する項目。
- `check_sample.py`: 入力ファイルの存在と記録表の列を読むだけの確認コード。

## 入力ファイルの確認

ZIPを展開した`premiere-generative-practice`フォルダで実行します。

```bash
python3 check_sample.py
```

`PASS: input files ready; no Premiere generation executed.`が出れば、入力ファイルの確認成功です。
Premiereの動作や、生成の成功を示すメッセージではありません。Python未導入なら公式配布元を確認してください。

## 自分のPremiereで試す場合

1. 練習用プロジェクトとシーケンスを用意します。
2. ToolsパネルでGenerative Media Toolを選び、対象範囲をタイムライン上で指定します。
3. `video-prompt.txt`の依頼例を入力します。Modelで使えるモデルを選びます。
4. 選んだモデルで表示される寸法、比率、fps、長さ等を実際に読み、`settings-record.csv`へ記録します。項目や選択肢はモデルにより異なります。
5. この例は参照画像なし、音声なしで始める提案です。Audioの選択肢もモデルによります。
6. 生成前に見積クレジットと、自分の利用条件・残高を確認します。合わない場合は生成せず終了します。
7. 実際に生成する場合はGenerateを選び、追加されたクリップを`review-checklist.md`に沿って確認します。

生成はインターネット接続を使うクラウド処理です。モデルの提供は地域や契約によります。
同じプロンプトやseedで同じ結果になる、特定の形や寸法が必ず保たれる、と保証するセットではありません。
生成前の素材・設定確認と、生成後の編集・出力確認は別に実施してください。
独自の文面とチェック項目は、自分の用途に合わせて編集して使えます。

## 一次資料

- https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-overview.html
- https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generate-media-with-generative-media-tool.html
- https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-faq.html
- https://www.python.org/downloads/macos/
