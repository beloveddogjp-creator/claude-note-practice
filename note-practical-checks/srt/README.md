# 字幕の本文だけを変える練習

original.srtは架空の6字幕です。edited-example.srtは、手作業で作った2件の候補を採用した例です。AIの実際の回答ではありません。manual-proposals.jsonで番号・原文・修正案を見比べます。

1. original.srtを別名のedited.srtへ複製します。元ファイルは残します。
2. 番号と原文が一致する候補の本文だけを直します。数字だけの本文「2」も保全します。
3. このsrtフォルダのターミナルで、Python 3を使って次を実行します。

```sh
python3 check_structure.py original.srt edited.srt
```

PASSは件数・番号・順番・時刻が一致したという意味です。文章の意味、正しい表記、表示時間内での読みやすさ、実映像との同期は確認していません。採用した本文だけが変わったか、エディターでの差分比較と実際の再生も必要です。ファイルは書き換えません。

配布例を先に確認する場合は、edited.srtの代わりにedited-example.srtを指定します。
