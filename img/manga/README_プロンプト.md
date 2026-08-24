# meeting.html の漫画コマ — 生成プロンプト

⚠ Gemini API の無料枠は画像生成が **limit: 0** (課金を有効にしないと1枚も出ない)。
⭐ Canva の Magic Media か GPT で作って, **このフォルダに下記のファイル名で置けば自動で表示される**。
⭐ 画像が無い間, コマ枠は自動で消えるのでページは崩れない。

推奨サイズ = 横長 (16:9 前後)。

---

## 共通の指定 (全部の頭に付ける)

```
Japanese manga illustration, black ink line art with soft grey screentone, clean, warm, gently humorous. Ordinary Japanese office workers. Simple uncluttered background, white background, horizontal composition. ABSOLUTELY NO TEXT, no letters, no speech bubbles, no signage anywhere.
```

⚠ **文字は必ず入れさせない。**セリフは HTML 側の吹き出しで出している。

---

## 1. `p1_silent.jpg` — 課題提起

```
A meeting room table with five people. One person has gone quiet and is looking down at their hands, while the others keep talking past them without noticing.
```

キャプション = この人がいつ黙ったか、覚えている人はいません

## 2. `p2_record.jpg` — 録る

```
The same meeting room, an ordinary meeting in progress, with a small video camera on a tripod quietly recording in the corner. Nobody is posing for it.
```

キャプション = 最初は気になります。3回目には忘れます

## 3. `p3_watch.jpg` — 観る

```
The same team sitting together facing a large monitor, watching a recording of themselves in a meeting. Their expressions are a mix of surprise and awkward recognition.
```

キャプション = 自分の映像を観るのは、正直きまずいです

## 4. `p4_roleplay.jpg` — やってみる

```
Two of the team members standing up and acting out a conversation again in front of their seated colleagues, trying it a different way. Slightly awkward but engaged.
```

キャプション = やり直すと、だいたい笑いが起きます

## 5. `p5_twocoaches.jpg` — 2人で観る

```
Two facilitators in their fifties sitting side by side watching the same screen. One is pointing at the structure of what is happening, the other is watching the people's faces. Different attention, same screen.
```

キャプション = 同じ画面を観ていても、追っているものが違います
