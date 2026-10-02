# 動画の情報を読むための3秒サンプル

2026-10-02。自作の合成素材です。実案件・人物・商品・顧客データを含みません。
Claude Codeの練習repositoryにありますが、このフォルダの確認にClaudeや有料サービスは不要です。

sample.mp4: testsrc2による640×360、30fps、3秒の映像。H.264/AAC、音声2チャンネル。
channels.wav: 24,000Hz、16bitのPCM stereo。左440Hz、右660Hz、3秒の合成音。
sample.srt: 架空字幕2件。0.000〜1.200秒と1.500〜3.000秒。
probe.py: Python標準ライブラリでffprobeを呼び、読み取り結果を表示。素材は書き換えません。

Python 3と導入済みのFFmpeg/ffprobeが必要です。ソフトの自動インストールは行いません。
ZIPを新しいフォルダへ展開し、media-practiceフォルダでターミナルを開きます。

```bash
ffprobe -version
python3 probe.py sample.mp4
```

表示されるstreamsのvideoはcodec_name=h264、width=640、height=360、r_frame_rateとavg_frame_rateは30/1。
audioはcodec_name=aac、channels=2、sample_rate=24000。formatのdurationは3.000000。
format_nameに複数の名称が出るのはcontainer demuxerの表記です。

```bash
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,channels:format=duration -of json sample.mp4
```

2チャンネルという表示だけでは、両側に目的の声があるかは分かりません。
channels.wavは小さい音量から聞き、片側ずつ再生して違いを確認するための素材です。実機での聴取は未実施です。
字幕を読み込む場合はsample.srtを同じ長さのsequenceへ置き、表示・消える時点を再生で確かめます。
SRTが動画と同じフォルダにあるだけで、すべてのplayerが自動表示するわけではありません。
Premiereでのimport/export、字幕表示、音声mapping、色表示の実機操作は未実施です。

数値を読めることは、作品の品質、VFRの確定、納品先との互換性の証明ではありません。
実案件では指定された納品仕様と、書き出したファイルの再生も別に確認します。

一次資料: https://ffmpeg.org/ffprobe.html
生成元の仕様: https://ffmpeg.org/ffmpeg-filters.html#testsrc2
