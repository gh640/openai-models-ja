# OpenAI 社が提供するモデルの一覧（日本語）

**最終更新日: 2024/12/18**

OpenAI 社が提供するモデルの一覧です。
基本的に最新のものが各表の一番上に並んでいます。

可能なときに更新していきます。
最終更新日が古い場合は公式にあたってください。

---

## フラッグシップモデル

### GPT-4o

知性の高いフラッグシップモデル（複雑・マルチステップなタスク向き）

- 入力: テキスト・画像 / 出力: テキスト
- コンテキスト長: 1.28 万
- 入力: 5 ドル / 出力: 15 ドル

### GPT-4o mini

安くて性能の高い小さなモデル（軽量なタスク向き）

- 入力: テキスト・画像 / 出力: テキスト
- コンテキスト長: 1.28 万
- 入力: 0.15 ドル / 出力 0.60 ドル

コストはいずれも 100 万トークンあたり。

### o1-preview と o1-mini **Beta**

新しい推論モデルの新しいシリーズ（難しい問題解決向き）

- 入出力: テキストのみ
- コンテキスト長: 1.28 万
- o1-preview: 入力: 15 ドル / 出力: 60 ドル
- o1-mini: 入力: 3 ドル / 出力: 12 ドル

## 継続的なモデルアップグレード

以下のモデルはそのときどきの最新版のモデルを指す。

- `chatgpt-4o-latest`
- `gpt-4o`
- `gpt-4o-mini`
- `gpt-4-turbo`
- `gpt-4`
- `gpt-3.5-turbo`

実際に使われたモデルの情報はレスポンスオブジェクトで確認できる。

> ## Continuous model upgrades
> 
> `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `gpt-4`, and `gpt-3.5-turbo` point to their respective latest model version. You can verify this by looking at the [response object](https://platform.openai.com/docs/api-reference/chat/object) after sending a request. The response will include the specific model version used (e.g. `gpt-3.5-turbo-1106`). The `chatgpt-4o-latest` model version continuously points to the version of [GPT-4o](https://chatgpt.com/) used in ChatGPT, and is updated frequently. With the exception of `chatgpt-4o-latest`, we offer pinned model versions that developers can continue using for at least three months after an updated model has been introduced.
> 
> Learn more about model deprecation on our [deprecation page](https://platform.openai.com/docs/deprecations).

## GPT-4o

OpenAI が提供する最も先進的なマルチモーダル（テキスト・画像の入力とテキストの出力ができる）モデル。
4o の o は omni を意味する。
GPT-4 Turbo と同じ高い知能を持ちながらはるかに効率的で、テキスト生成は 2 倍速くコストは 50% 低減されている。
さらに、 OpenAI の他のモデルよりも優れた視覚認識能力と非英語言語でのパフォーマンスを持つ。

モデル | 説明 | コンテキストウィンドウ | 最大出力トークン | トレーニングデータ
--- | --- | --- | --- | ---
`chatgpt-4o-latest` | ChatGPT で使用される GPT-4o のバージョンに継続的にアップデートされるダイナミックなモデル | 128,000 | 16,384 | 2024/10 まで
`gpt-4o` | GPT-4o モデル。最も先進的なマルチモーダルフラッグシップモデル。 GPT-4 Trubo よりも安価で高速。現在 `gpt-4o-2024-08-06` を指す。 | 128,000 | 16,384 | 2023/10 まで
`gpt-4o-2024-11-20` | GPT-4o の 2024/11/20 の最新スナップショット。 | 128,000 | 16,384 | 2023/10 まで
`gpt-4o-2024-08-06` | Structured Outputs をサポートする最新のスナップショット | 128,000 | 16,384 | 2024/10 まで
`gpt-4o-2024-05-13` | 現在 `gpt-4o` が指すモデル | 128,000 | 4,096 | 2023/10 まで

> [!NOTE]
> `chatgpt-4o-latest` は開発者・研究者向け。本番環境での使用には日付ありの GPT モデルが推奨される。

### 料金

モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン）
--- | --- | ---
`chatgpt-4o-latest` | $5 | $15
`gpt-4o` | $2.5 | $10
`gpt-4o-2024-11-20` | $2.5 | $10
`gpt-4o-2024-08-06` | $2.5 | $10
`gpt-4o-2024-05-13` | $5 | $15

> [!NOTE]
> `gpt-4o` と `gpt-4o-2024-11-20` と `gpt-4o-2024-08-06` にはインプットトークンのキャッシュ機能がある。キャッシュされたトークンは半額（ 50% ）。

画像入力は 150px x 150px に対して:

モデル | 価格
--- | ---
`chatgpt-4o-latest` | $0.001275
`gpt-4o` | $0.000638
`gpt-4o-2024-08-06` | $0.000638
`gpt-4o-2024-05-13` | $0.001275

- Batch API の価格は通常の価格の 50%

インプット・アウトプットともに価格は GPT 4 Turbo の 50% で、トークン化効率も大幅に向上している。

> [!NOTE]
> 後発の `gpt-4o-2024-08-06` の方が `gpt-4o-2024-05-13` よりも単価が低いのは間違いではありません。

> By switching to the new `gpt-4o-2024-08-06`, developers save 50% on inputs ($2.50/1M input tokens) and 33% on outputs ($10.00/1M output tokens) compared to `gpt-4o-2024-05-13`.
>
> [Introducing Structured Outputs in the API | OpenAI](https://openai.com/index/introducing-structured-outputs-in-the-api/)

> [!NOTE]
> 後発の `gpt-4o` の方が `gpt-4-turbo` よりも単価が低いのは間違いではありません。

> It (=GPT-4o) matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50% cheaper in the API.
> 
> [Hello GPT-4o | OpenAI](https://openai.com/index/hello-gpt-4o/)

## GPT-4o mini

OpenAI が提供する、小さなモデルカテゴリにおける最も先進的なモデル。
そしてこれまでで最も安いモデルでもある。
`gpt-3.5-turbo` と同等に高速でありながらよりも高い性能を持つ。

| モデル | 説明 | コンテキストウィンドウ | 最大出力トークン | トレーニングデータ |
| --- | --- | --- | --- | --- |
| `gpt-4o-mini` | 安くて性能の高い小さなモデル。現在 `gpt-4o-mini-2024-07-18` を指す。 | 128,000 | 16,384 | 2023/10 まで |
| `gpt-4o-mini-2024-07-18` | 現在 `gpt-4o-mini` が指すモデル | 128,000 | 16,384 | 2023/10 まで |

### 料金

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-4o-mini` | $0.15 | $0.60 |
| `gpt-4o-mini-2024-07-18` | $0.15 | $0.60 |

> [!NOTE]
> `gpt-4o-mini` と `gpt-4o-mini-2024-07-18` にはインプットトークンのキャッシュ機能がある。キャッシュされたトークンは半額（ 50% ）。

- 画像入力は 150px x 150px で $0.001275 （ `gpt-4o` と同じ）
- Batch API の価格は通常の価格の 50%

## GPT-4o と GPT-4o-mini の Realtime **Beta**

GPT-4o と GPT-4o-mini の Realtime モデルのプレビューリリース。
これらのモデルは WebRTC や WebSocket のインタフェースを使った音声とテキストの入力に対応できる。
詳しくは [Realtime API ガイド](https://platform.openai.com/docs/guides/realtime) 。

| モデル | 説明 | コンテキストウィンドウ | 最大出力トークン |
| --- | --- | --- | --- |
| `gpt-4o-realtime-preview` | `gpt-4o-realtime-preview-2024-10-01` を指す | 128,000 | 4,096 |
| `gpt-4o-realtime-preview-2024-12-17` | - | 128,000 | 4,096 |
| `gpt-4o-realtime-preview-2024-10-01` | - | 128,000 | 4,096 |
| `gpt-4o-mini-realtime-preview` | `gpt-4o-mini-realtime-preview-2024-12-17` を指す | 128,000 | 4,096 |
| `gpt-4o-mini-realtime-preview-2024-12-17` | - | 128,000 | 4,096 |

### 料金

テキスト:

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-4o-realtime-preview` | $5 | $20 |
| `gpt-4o-realtime-preview-2024-12-17` | $5 | $20 |
| `gpt-4o-realtime-preview-2024-10-01` | $5 | $20 |
| `gpt-4o-mini-realtime-preview` | $0.6 | $2.4 |
| `gpt-4o-mini-realtime-preview-2024-12-17` | $0.6 | $2.4 |

> [!NOTE]
- 入力にはキャッシュ機能がありキャッシュされたトークンは半額（ 50% ）

音声:

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-4o-realtime-preview` | $100 | $200 |
| `gpt-4o-realtime-preview-2024-12-17` |  $40 | $80 |
| `gpt-4o-realtime-preview-2024-10-01` |  $100 | $200 |
| `gpt-4o-mini-realtime-preview` | $10 | $20 |
| `gpt-4o-mini-realtime-preview-2024-12-17` | $10 | $20 |

> [!NOTE]
- 入力にはキャッシュ機能がありキャッシュされたトークンは 80 - 95% ほど安い

## GPT-4o Audio **Beta**

GPT-4o の Audio モデルのプレビューリリース。
これらのモデルは音声の入出力が可能で Chat Completions REST API で使用可能。
詳しくは [Audio 生成ガイド](https://platform.openai.com/docs/guides/audio) 。

| モデル | 説明 | コンテキストウィンドウ | 最大出力トークン |
| --- | --- | --- | --- |
| `gpt-4o-audio-preview` | `gpt-4o-audio-preview-2024-10-01` を指す | 128,000 | 16,384 |
| `gpt-4o-audio-preview-2024-12-17` | - | 128,000 | 16,384 |
| `gpt-4o-audio-preview-2024-10-01` | - | 128,000 | 16,384 |

## 料金

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-4o-audio-preview` |  $100 | $200 |
| `gpt-4o-audio-preview-2024-12-17` |  $40 | $80 |
| `gpt-4o-audio-preview-2024-10-01` |  $100 | $200 |

音声 1 分あたりのおおよその価格:

| モデル | インプット | アウトプット |
| --- | --- | --- |
| `gpt-4o-audio-preview-2024-12-17` | $0.024 | 0.096 |
| `gpt-4o-audio-preview-2024-10-01` | $0.06 | $0.24 |

## o1-preview と o1-mini

複雑な推論を行うように強化学習でトレーニングされた大規模モデル。
回答を返す前に考えて、長い内部的な Chain of thought を生成してからユーザーに返答を返す。
科学的推論に長けている。

- Codeforces: 競技プログラミングの質問で 89 パーセンタイル
- AIME: 数学でアメリカの学生のトップ 500 に匹敵
- GPQA: 物理・生物学・化学の問題で人間の PhD レベルの正確さ

| モデル | 説明 | コンテキストウィンドウ | 最大出力トークン | トレーニングデータ |
| --- | --- | --- | --- | --- |
| `o1-preview` | さまざまな領域で難しい問題を解けるよう設計された推論モデル。 `o1` モデルの早期プレビュー。 | 128,000 | 32,768 | 2023/10 まで |
| `o1-mini` | コーディング・数学・科学で特に優れた高速で安価な推論モデル | 128,000 | 65,536 | 2023/10 まで |

### 料金

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `o1-preview` | $15 | $60 |
| `o1-preview-2024-09-12` | $15 | $60 |
| `o1-mini` | $3 | $12 |
| `o1-mini-2024-09-12` | $3 | $12 |

## GPT-4 Turbo と GPT-4

大規模なマルチモーダル（テキスト・画像の入力とテキストの出力ができる）モデル。

| モデル | 説明 | コンテキストウィンドウ | トレーニングデータ |
| --- | --- | --- | --- |
| `gpt-4-turbo` | GPT-4 Turbo with Vision モデル。ビジョン機能付きの最新の GPT-4 Turbo 。ビジョンリクエストで JSON モードとファンクションコーリングを利用可。現在 `gpt-4-turbo-2024-04-09` を指す。 | 128,000 トークン | 2023/12 まで |
| `gpt-4-turbo-2024-04-09` | GPT-4 Turbo with Vision モデル。ビジョンリクエストで JSON モードとファンクションコーリングを利用可。 | 128,000 トークン | 2023/12 まで |
| `gpt-4-turbo-preview` | 現在 `gpt-4-0125-preview` を指す。 | 128,000 トークン | 2023/12 まで |
| `gpt-4-0125-preview` | GPT-4 Turbo preview モデル。 [詳細](https://openai.com/index/new-embedding-models-and-api-updates/) | 128,000 トークン | 2023/12 まで |
| `gpt-4-1106-preview` | GPT-4 Turbo モデル。プロダクショントラフィック向けではない。 [詳細](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) | 128,000 トークン | 2023/04 まで |
| `gpt-4` | 現在 `gpt-4-0613` を指す。 | 8,192 トークン | 2021/09 まで |
| `gpt-4-0613` | `gpt-4` の 2023/06/13 時点のスナップショット。ファンクションコーリングサポートの改善あり。 | 8,192 トークン | 2021/09 まで |
| `gpt-4-0314` | **Legacy**<br>`gpt-4` の 2023/03/14 時点のスナップショット。 | 8,192 トークン | 2021/09 まで |

> [!TIP]
> モデル名に 4 桁の数字が入っているものはリリース日の月日を表すようです（少し場当たり的に付けられている感じがするので将来的にルールがかわるかもしれません）。
> 年の情報は含まれていないため少しややこしいですが、新しいものから並べると `gpt-4-0125-preview` > `gpt-4-1106-preview` > `gpt-4-0613` となります。

### 料金

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-4-turbo-2024-04-09` | $10 | $30 |
| `gpt-4` | $30 | $60 |
| `gpt-4-32k` | $60 | $120 |

画像入力は 150px x 150px で $0.00255 。

多くの基本的なタスクでは GPT-4 と GPT-3.5 の差は大きくない。しかし、より複雑な推論状況では GPT-4 はこれまでのどのモデルよりもはるかに能力が高い。

> [!NOTE]
> 後発の `gpt-4-turbo` の方が `gpt-4` よりも単価が低いのは間違いではありません。

> GPT-4 Turbo is more capable and has knowledge of world events up to April 2023. It has a 128k context window so it can fit the equivalent of more than 300 pages of text in a single prompt. We also optimized its performance so we are able to offer GPT-4 Turbo at a 3x cheaper price for input tokens and a 2x cheaper price for output tokens compared to GPT-4.
>
> [New models and developer products announced at DevDay](https://openai.com/index/new-models-and-developer-products-announced-at-devday/)

## GPT-3.5 Turbo

GPT-3.5 を改善した、自然言語やコードを理解・生成できるモデル群。

| モデル | 説明 | コンテキストウィンドウ | トレーニングデータ |
| --- | --- | --- | --- |
| `gpt-3.5-turbo-0125` | **New**<br>最新の **GPT 3.5 Turbo** モデル。 [詳細](https://openai.com/index/new-embedding-models-and-api-updates/#:~:text=Other%20new%20models%20and%20lower%20pricing) | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo` | 現在 `3.5-turbo-0125` を指す。 | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo-1106` | GPT-3.5 Turbo モデル。インストラクションへの対応・ JSON モード・再現可能な出力・パラレルファンクションコーリングなどの改善あり。 [詳細](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo-instruct` | GPT-3 時代と近い能力。レガシー Completions エンドポイントとの互換性あり、 Chat Completions との互換性なし。 | 4,096 トークン | 2021/09 まで |
| `gpt-3.5-turbo-16k` | **Legacy**<br>現在 `gpt-3.5-turbo-16k-0613` を指す。 | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo-0613` | **Legacy**<br>`gpt-3.5-turbo` の 2023/06/13 時点のスナップショット。 2024/06/13 に deprecated 予定。 | 4,096 トークン | 2021/09 まで |
| `gpt-3.5-turbo-16k-0613` | **Legacy**<br>`gpt-3.5-16k-turbo` の 2023/06/13 時点のスナップショット。 2024/06/13 に deprecated 予定。 | 16,385 トークン | 2021/09 まで |

> [!TIP]
> こちらもモデル名に 4 桁の数字が入っているものはリリース日の月日を表すようです。
> 年の情報は含まれていないため少しややこしいですが、新しいものから並べると `gpt-3.5-turbo-0125` > `gpt-3-turbo-1106` > `gpt-3-turbo-0613` となります。

### 料金

| モデル | インプット（ 1M トークン） | アウトプット（ 1M トークン） |
| --- | --- | --- |
| `gpt-3.5-turbo-0125` | $0.5 | $1.5 |
| `gpt-3.5-turbo-instruct` | $1.5 | $2.0 |

## アシスタント API

> [!TIP]
> アシスタント API では各チャットモデルが利用できます。

### 料金

| ツール | インプット |
| --- | --- |
| Code interpreter | $0.03 / セッション |
| Retrieval | $0.20 / GB / アシスタント / 日（ 2024/03/01 まで無料） |

## DALL·E

自然言語のプロンプトを与えて画像を生成・編集できるモデル。

| モデル | 説明 |
| --- | --- |
| `dall-e-3` | 最新の **DALL·E 3** モデル。 2023/11 リリース。 [詳細](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) |
| `dall-e-2` | ひとつ前の DALL·E モデル。 2022/11 リリース。オリジナルモデルよりも 4 倍以上の解像度のリアルで精確な第 2 世代 DALL·E モデル。 |

### 料金

| モデル | 品質 | 解像度 | 料金（ 1 画像） |
| --- | --- | --- | --- |
| `dall-e-3` | Standard | 1024×1024 | $0.040 |
|  | Standard | 1024×1792, 1792×1024 | $0.080 |
|  | HD | 1024×1024 | $0.080 |
|  | HD | 1024×1792, 1792×1024 | $0.120 |
| `dall-e-2` |  | 1024×1024 | $0.020 |
|  |  | 512×512 | $0.018 |
|  |  | 256×256 | $0.016 |

## TTS

テキストを自然な発話データに変換できるモデル群。
TTS は Text-To-Speech の略。

| モデル | 説明 |
| --- | --- |
| `tts-1` | 最新の Text-to-Speech モデル。リアルタイム生成向けでスピード優先。 |
| `tts-1-hd` | 最新の Text-to-Speech 1 モデル。品質優先。 |

### 料金

| モデル | 料金 |
| --- | --- |
| `tts-1` |	$0.015 / 1K 文字 |
| `tts-1-hd` | $0.030 / 1K 文字 |

## Whisper

音声をテキストに変換できるモデル。
マルチタスクで多言語音声認識・音声翻訳・言語識別も可能。
現在モデル名 `whisper-1` で Whisper v2-large モデルが利用可能。

| モデル | 説明 |
| --- | --- |
| `whisper-1` | Whisper v2-large モデル。 |

現在オープンソースバージョンと OpenAI の API で利用できるバージョンに違いは無いが、 API の方は推論過程の最適化により高速化されている。

### 料金

| モデル | 料金 |
| --- | --- |
| `whisper-1` |	$0.006 / 分（端数は近い秒に丸められる） |

## Embeddings

テキストを数値形式に変換できるモデル群。
最新のモデルについては [告知のブログ投稿](https://openai.com/index/new-embedding-models-and-api-updates/) に詳細あり。

| モデル | 説明 | 出力の次元 |
| --- | --- | --- |
| `text-embedding-3-large` | **New**<br>**Embedding V3 large** <br>英語とその他の言語の両方で最も能力の高い embedding モデル。 [詳細](https://openai.com/index/new-embedding-models-and-api-updates/) | 3,072 |
| `text-embedding-3-small` | **New**<br>**Embedding V3 small** <br>第 2 世代の ada embedding モデルからパフォーマンスを改善。 [詳細](https://openai.com/index/new-embedding-models-and-api-updates/) | 1,536 |
| `text-embedding-ada-002` | 第 2 世代で最も能力の高い embedding モデル。 16 個の第 1 世代モデルの置き換え。 [詳細](https://openai.com/index/new-and-improved-embedding-model/) | 1,536 |

### 料金

| モデル | 使用（ 1k トークン） |
| --- | --- |
| `text-embedding-3-large` | $0.00013 |
| `text-embedding-3-small` | $0.00002 |
| `ada v2` | $0.00010 |

## Moderation

テキストがセンシティブであったり安全でなかったりすることを検出できる、ファインチューニングされたモデル。

| モデル | 説明 | 最大トークン |
| --- | --- | --- |
| `omni-moderation-latest` | 現在 `omni-moderation-2024-09-26` を指す。 | 32,768 |
| `omni-moderation-2024-09-26` | マルチモーダルもでレーションモデルの最新バージョン。テキストと画像の分析が可能。 | 32,768 |
| `text-moderation-latest` | 現在 `text-moderation-007` を指す。 | 32,768 |
| `text-moderation-stable` | 現在 `text-moderation-007` を指す。 | 32,768 |
| `text-moderation-007` | すべてのカテゴリーで最も能力の高い moderation モデル。 [詳細](https://openai.com/index/new-embedding-models-and-api-updates/) | 32,768 |

## GPT base

自然言語やコードを理解・生成できるがインストラクションでの学習ができないモデル群。
オリジナルの GPT-3 ベースモデルの置き換えとして作られた。
レガシーな Completions API を使う。
ほとんどのユーザーにはこれらではなく GPT-3.5 か GPT-4 の利用が推奨される。

| モデル | 説明 | 最大トークン | トレーニングデータ |
| --- | --- | --- | --- |
| `babbage-002` | GPT-3 `ada` と `babbage` ベースモデルの置き換え。 | 16,384 トークン | 2021/09 まで |
| `davinci-002` | GPT-3 `curie` と `davinci` ベースモデルの置き換え。  | 16,384 トークン | 2021/09 まで |

### 料金

| モデル | 使用（ 1k トークン） |
| --- | --- |
| `davinci-002` | $0.0020 |
| `babbage-002` | $0.0004 |

## データの使用ポリシー

2023/03/01 時点で（明示的にオプトインしないかぎり） OpenAI API に送信されたデータは OpenAI のモデルのトレーングには使わない、とのこと。
ただし、不正使用の特定のためにデータは最長 30 日間保持されることがある。

> [!NOTE]
> デフォルトの使用ポリシーはエンドポイントごとに異なるため公式ドキュメンテーションを参考してください。

このデータポリシーは API 経由ではない ChatGPT や DALL·E Labs のサービスには適用されない（つまり、 ChatGPT や DALL·E Labs でユーザーが送信したデータはモデルのトレーニングに使用されることがある）。

> ## How we use your data
> 
> Your data is your data.
> 
> As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly opt-in to share data with us, such as by [providing feedback in the Playground](https://help.openai.com/en/articles/9883556-providing-feedback-in-the-api-playground)). One advantage to opting in is that the models may get better at your use case over time.
> 
> To help identify abuse, API data may be retained for up to 30 days, after which it will be deleted (unless otherwise required by law). For trusted customers with sensitive applications, zero data retention may be available. With zero data retention, request and response bodies are not persisted to any logging mechanism and exist only in memory in order to serve the request.
>
> Note that this data policy does not apply to OpenAI's non-API consumer services like [ChatGPT](https://chat.openai.com/) or [DALL·E Labs](https://labs.openai.com/).
>
> https://platform.openai.com/docs/models/how-we-use-your-data

## Deprecated

非推奨となったモデルの全リストと代替案。

> [!NOTE]
> シャットダウン日が過ぎているものは除外しています。

## 2024-10-02: Assistants API beta v1

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| OpenAI-Beta: assistants=v1 | OpenAI-Beta: assistants=v2 | 2024-12-18 |

## 2024-08-29: babbage-002 と davinci-002 のファインチューニングトレーニング

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `babbage-002` の新たなファインチューニング | `gpt-4o-mini` | 2024/10/28 |
| `davinci-002` の新たなファインチューニング | `gpt-4o-mini` | 2024/10/28 |

## 2024/06/06: GPT-4-32K とビジョンプレビューモデル

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `gpt-4-32k` | `gpt-4o` | 2025/06/06 |
| `gpt-4-32k-0613` | `gpt-4o` | 2025/06/06 |
| `gpt-4-32k-0314` | `gpt-4o` | 2025/06/06 |
| `gpt-4-vision-preview` | `gpt-4o` | 2025/12/06 |
| `gpt-4-1106-vision-preview` | `gpt-4o` | 2025/12/06 |

### 2023/11/06: チャットモデルのアップデート

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `gpt-3.5-turbo-0613` | `gpt-3.5-turbo-1106` | 2024/06/13 |
| `gpt-3.5-turbo-16k-0613` | `gpt-3.5-turbo-1106` | 2024/06/13 |

### 2023/06/13: チャットモデルのアップデート

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `gpt-3.5-turbo-0301` | `gpt-3.5-turbo-0613` | 早ければ 2024/06/13 |
| `gpt-4-0314` | `gpt-4-0613` | 早ければ 2024/06/13 |
| `gpt-4-32k-0314` | `gpt-4-32k-0613` | 早ければ 2024/06/13 |

## 公式ページ

- [Models - OpenAI API](https://platform.openai.com/docs/models)
- [Deprecations - OpenAI API](https://platform.openai.com/docs/deprecations)
- [Pricing | OpenAI](https://openai.com/api/pricing/)

## その他参考文献

- [OpenAI - Wikipedia](https://en.wikipedia.org/wiki/OpenAI)
