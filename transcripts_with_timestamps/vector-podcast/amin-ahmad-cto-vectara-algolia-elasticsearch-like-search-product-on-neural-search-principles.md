---
description: '<p>YouTube: <a target="_blank" rel="noopener noreferrer nofollow" href="https://www.youtube.com/watch?v=e2tZ6HD4I44">https://www.youtube.com/watch?v=e2tZ6HD4I44</a></p><p>Update:
  ZIR.AI has relaunched as Vectara: <a target="_blank" rel="noopener noreferrer nofollow"
  href="https://vectara.com/">https://vectara.com/</a></p><p>Topics:</p><p>00:00 Intro</p><p>00:54
  Amin’s background at Google Research and affinity to NLP and vector search field</p><p>05:28
  Main focus areas of ZIR.AI in neural search</p><p>07:26 Does the company offer neural
  network training to clients? Other support provided with ranking and document format
  conversions</p><p>08:51 Usage of open source vs developing own tech</p><p>10:17
  The core of ZIR.AI product</p><p>14:36 API support, communication protocols and
  P95/P99 SLAs, dedicated pools of encoders</p><p>17:13 Speeding up single node /
  single customer throughput and challenge of productionizing off the shelf models,
  like BERT</p><p>23:01 Distilling transformer models and why it can be out of reach
  of smaller companies</p><p>25:07 Techniques for data augmentation from Amin’s and
  Dmitry’s practice (key search team: margin loss)</p><p>30:03 Vector search algorithms
  used in ZIR.AI and the need for boolean logic in company’s client base</p><p>33:51
  Dynamics of open source in vector search space and cloud players: Google, Amazon,
  Microsoft</p><p>36:03 Implementing a multilingual search with BM25 vs neural search
  and impact on business</p><p>38:56 Is vector search a hype similar to big data few
  years ago? Prediction for vector search algorithms influence relations databases</p><p>43:09
  Is there a need to combine BM25 with neural search? Ideas from Amin and features
  offered in ZIR.AI product</p><p>51:31 Increasing the robustness of search — or simply
  making it to work</p><p>55:10 How will Search Engineer profession change with neural
  search in the game?</p><p>Get a $100 discount (first month free) for a 50mb plan,
  using the code VectorPodcast (no lock-in, you can cancel any time): <a target="_blank"
  rel="noopener noreferrer nofollow" href="https://zir-ai.com/signup/user">https://zir-ai.com/signup/user</a></p>'
image_url: https://media.rss.com/vector-podcast/20220216_040237_4d74468969220e3376998953833bb185.jpg
pub_date: Wed, 16 Feb 2022 16:14:37 GMT
title: Amin Ahmad - CTO, Vectara - Algolia / Elasticsearch-like search product on
  neural search principles
url: https://rss.com/podcasts/vector-podcast/393967
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 21.080000000000002,
  "text": " Hello, vector podcast is here and today we''re going to be talking with
  Amin Ahmed, co-founder", "tokens": [50364, 2425, 11, 8062, 7367, 307, 510, 293,
  965, 321, 434, 516, 281, 312, 1417, 365, 2012, 259, 39189, 11, 598, 12, 33348, 51418],
  "temperature": 0.0, "avg_logprob": -0.3554973602294922, "compression_ratio": 1.1293103448275863,
  "no_speech_prob": 0.09521778672933578}, {"id": 1, "seek": 0, "start": 21.080000000000002,
  "end": 24.16, "text": " and CEO of the company called ZIR AI.", "tokens": [51418,
  293, 9282, 295, 264, 2237, 1219, 1176, 7740, 7318, 13, 51572], "temperature": 0.0,
  "avg_logprob": -0.3554973602294922, "compression_ratio": 1.1293103448275863, "no_speech_prob":
  0.09521778672933578}, {"id": 2, "seek": 2416, "start": 24.16, "end": 30.2, "text":
  " I''m really, really excited to talk to Amin because basically he''s innovating
  in this space,", "tokens": [50364, 286, 478, 534, 11, 534, 2919, 281, 751, 281,
  2012, 259, 570, 1936, 415, 311, 5083, 990, 294, 341, 1901, 11, 50666], "temperature":
  0.0, "avg_logprob": -0.24888961335532686, "compression_ratio": 1.644, "no_speech_prob":
  0.18610267341136932}, {"id": 3, "seek": 2416, "start": 30.2, "end": 34.56, "text":
  " his company is innovating in this space of bringing vector search to practice
  and also", "tokens": [50666, 702, 2237, 307, 5083, 990, 294, 341, 1901, 295, 5062,
  8062, 3164, 281, 3124, 293, 611, 50884], "temperature": 0.0, "avg_logprob": -0.24888961335532686,
  "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932}, {"id": 4, "seek":
  2416, "start": 34.56, "end": 36.36, "text": " making it usable.", "tokens": [50884,
  1455, 309, 29975, 13, 50974], "temperature": 0.0, "avg_logprob": -0.24888961335532686,
  "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932}, {"id": 5, "seek":
  2416, "start": 36.36, "end": 38.16, "text": " Hey, I mean, how are you?", "tokens":
  [50974, 1911, 11, 286, 914, 11, 577, 366, 291, 30, 51064], "temperature": 0.0, "avg_logprob":
  -0.24888961335532686, "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932},
  {"id": 6, "seek": 2416, "start": 38.16, "end": 39.96, "text": " I''m doing fine.",
  "tokens": [51064, 286, 478, 884, 2489, 13, 51154], "temperature": 0.0, "avg_logprob":
  -0.24888961335532686, "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932},
  {"id": 7, "seek": 2416, "start": 39.96, "end": 40.96, "text": " Thank you.", "tokens":
  [51154, 1044, 291, 13, 51204], "temperature": 0.0, "avg_logprob": -0.24888961335532686,
  "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932}, {"id": 8, "seek":
  2416, "start": 40.96, "end": 41.96, "text": " Thanks for having me.", "tokens":
  [51204, 2561, 337, 1419, 385, 13, 51254], "temperature": 0.0, "avg_logprob": -0.24888961335532686,
  "compression_ratio": 1.644, "no_speech_prob": 0.18610267341136932}, {"id": 9, "seek":
  2416, "start": 41.96, "end": 42.96, "text": " Awesome.", "tokens": [51254, 10391,
  13, 51304], "temperature": 0.0, "avg_logprob": -0.24888961335532686, "compression_ratio":
  1.644, "no_speech_prob": 0.18610267341136932}, {"id": 10, "seek": 2416, "start":
  42.96, "end": 43.96, "text": " Thanks for joining.", "tokens": [51304, 2561, 337,
  5549, 13, 51354], "temperature": 0.0, "avg_logprob": -0.24888961335532686, "compression_ratio":
  1.644, "no_speech_prob": 0.18610267341136932}, {"id": 11, "seek": 2416, "start":
  43.96, "end": 50.16, "text": " And I know it''s almost like festive times, so it''s
  probably quite a packed schedule for", "tokens": [51354, 400, 286, 458, 309, 311,
  1920, 411, 42729, 1413, 11, 370, 309, 311, 1391, 1596, 257, 13265, 7567, 337, 51664],
  "temperature": 0.0, "avg_logprob": -0.24888961335532686, "compression_ratio": 1.644,
  "no_speech_prob": 0.18610267341136932}, {"id": 12, "seek": 2416, "start": 50.16,
  "end": 53.64, "text": " you otherwise as well.", "tokens": [51664, 291, 5911, 382,
  731, 13, 51838], "temperature": 0.0, "avg_logprob": -0.24888961335532686, "compression_ratio":
  1.644, "no_speech_prob": 0.18610267341136932}, {"id": 13, "seek": 5364, "start":
  53.64, "end": 58.0, "text": " So yeah, I was thinking let''s traditionally start
  with the introduction.", "tokens": [50364, 407, 1338, 11, 286, 390, 1953, 718, 311,
  19067, 722, 365, 264, 9339, 13, 50582], "temperature": 0.0, "avg_logprob": -0.3188347524526168,
  "compression_ratio": 1.4660633484162895, "no_speech_prob": 0.0052063073962926865},
  {"id": 14, "seek": 5364, "start": 58.0, "end": 65.92, "text": " Like, can you please
  tell me a bit of background before ZIR AI and OZIR AI is a startup and", "tokens":
  [50582, 1743, 11, 393, 291, 1767, 980, 385, 257, 857, 295, 3678, 949, 1176, 7740,
  7318, 293, 422, 57, 7740, 7318, 307, 257, 18578, 293, 50978], "temperature": 0.0,
  "avg_logprob": -0.3188347524526168, "compression_ratio": 1.4660633484162895, "no_speech_prob":
  0.0052063073962926865}, {"id": 15, "seek": 5364, "start": 65.92, "end": 68.2, "text":
  " you''re rolling at ZIR AI?", "tokens": [50978, 291, 434, 9439, 412, 1176, 7740,
  7318, 30, 51092], "temperature": 0.0, "avg_logprob": -0.3188347524526168, "compression_ratio":
  1.4660633484162895, "no_speech_prob": 0.0052063073962926865}, {"id": 16, "seek":
  5364, "start": 68.2, "end": 71.92, "text": " Yes, sure.", "tokens": [51092, 1079,
  11, 988, 13, 51278], "temperature": 0.0, "avg_logprob": -0.3188347524526168, "compression_ratio":
  1.4660633484162895, "no_speech_prob": 0.0052063073962926865}, {"id": 17, "seek":
  5364, "start": 71.92, "end": 76.16, "text": " Me and my co-founder, we started ZIR
  AI in 2020.", "tokens": [51278, 1923, 293, 452, 598, 12, 33348, 11, 321, 1409, 1176,
  7740, 7318, 294, 4808, 13, 51490], "temperature": 0.0, "avg_logprob": -0.3188347524526168,
  "compression_ratio": 1.4660633484162895, "no_speech_prob": 0.0052063073962926865},
  {"id": 18, "seek": 5364, "start": 76.16, "end": 78.16, "text": " Before that, we
  were both working at Google.", "tokens": [51490, 4546, 300, 11, 321, 645, 1293,
  1364, 412, 3329, 13, 51590], "temperature": 0.0, "avg_logprob": -0.3188347524526168,
  "compression_ratio": 1.4660633484162895, "no_speech_prob": 0.0052063073962926865},
  {"id": 19, "seek": 5364, "start": 78.16, "end": 82.44, "text": " I had been there
  since 2010.", "tokens": [51590, 286, 632, 668, 456, 1670, 9657, 13, 51804], "temperature":
  0.0, "avg_logprob": -0.3188347524526168, "compression_ratio": 1.4660633484162895,
  "no_speech_prob": 0.0052063073962926865}, {"id": 20, "seek": 8244, "start": 82.44,
  "end": 92.72, "text": " I worked in Google Research, focused on NLP and language
  understanding with machine learning.", "tokens": [50364, 286, 2732, 294, 3329, 10303,
  11, 5178, 322, 426, 45196, 293, 2856, 3701, 365, 3479, 2539, 13, 50878], "temperature":
  0.0, "avg_logprob": -0.166553709242079, "compression_ratio": 1.4851485148514851,
  "no_speech_prob": 0.002010730793699622}, {"id": 21, "seek": 8244, "start": 92.72,
  "end": 95.84, "text": " Prior to that, I had worked many other places in the industry.",
  "tokens": [50878, 24032, 281, 300, 11, 286, 632, 2732, 867, 661, 3190, 294, 264,
  3518, 13, 51034], "temperature": 0.0, "avg_logprob": -0.166553709242079, "compression_ratio":
  1.4851485148514851, "no_speech_prob": 0.002010730793699622}, {"id": 22, "seek":
  8244, "start": 95.84, "end": 101.4, "text": " So I''ve been in the industry about
  24 or 25 years now.", "tokens": [51034, 407, 286, 600, 668, 294, 264, 3518, 466,
  4022, 420, 3552, 924, 586, 13, 51312], "temperature": 0.0, "avg_logprob": -0.166553709242079,
  "compression_ratio": 1.4851485148514851, "no_speech_prob": 0.002010730793699622},
  {"id": 23, "seek": 8244, "start": 101.4, "end": 111.0, "text": " And around 2017,
  the team that I was working on in Google Research actually became known", "tokens":
  [51312, 400, 926, 6591, 11, 264, 1469, 300, 286, 390, 1364, 322, 294, 3329, 10303,
  767, 3062, 2570, 51792], "temperature": 0.0, "avg_logprob": -0.166553709242079,
  "compression_ratio": 1.4851485148514851, "no_speech_prob": 0.002010730793699622},
  {"id": 24, "seek": 11100, "start": 111.0, "end": 114.08, "text": " for Gmail Smart
  Reply.", "tokens": [50364, 337, 36732, 12923, 3696, 356, 13, 50518], "temperature":
  0.0, "avg_logprob": -0.27677382797491357, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.07919315248727798}, {"id": 25, "seek": 11100, "start": 114.08,
  "end": 115.08, "text": " If you remember that feature.", "tokens": [50518, 759,
  291, 1604, 300, 4111, 13, 50568], "temperature": 0.0, "avg_logprob": -0.27677382797491357,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.07919315248727798},
  {"id": 26, "seek": 11100, "start": 115.08, "end": 117.0, "text": " Yeah, that''s
  an excellent feature.", "tokens": [50568, 865, 11, 300, 311, 364, 7103, 4111, 13,
  50664], "temperature": 0.0, "avg_logprob": -0.27677382797491357, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.07919315248727798}, {"id": 27, "seek": 11100,
  "start": 117.0, "end": 120.0, "text": " The moment I saw it, it was like, wow, that''s
  fantastic.", "tokens": [50664, 440, 1623, 286, 1866, 309, 11, 309, 390, 411, 11,
  6076, 11, 300, 311, 5456, 13, 50814], "temperature": 0.0, "avg_logprob": -0.27677382797491357,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.07919315248727798},
  {"id": 28, "seek": 11100, "start": 120.0, "end": 121.0, "text": " Yeah.", "tokens":
  [50814, 865, 13, 50864], "temperature": 0.0, "avg_logprob": -0.27677382797491357,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.07919315248727798},
  {"id": 29, "seek": 11100, "start": 121.0, "end": 122.0, "text": " Yeah, and it was
  impressive.", "tokens": [50864, 865, 11, 293, 309, 390, 8992, 13, 50914], "temperature":
  0.0, "avg_logprob": -0.27677382797491357, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.07919315248727798}, {"id": 30, "seek": 11100, "start": 122.0,
  "end": 126.08, "text": " And I would say maybe it was a very practical application
  of NLP that went, that was deployed", "tokens": [50914, 400, 286, 576, 584, 1310,
  309, 390, 257, 588, 8496, 3861, 295, 426, 45196, 300, 1437, 11, 300, 390, 17826,
  51118], "temperature": 0.0, "avg_logprob": -0.27677382797491357, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.07919315248727798}, {"id": 31, "seek": 11100,
  "start": 126.08, "end": 128.56, "text": " on a very large scale.", "tokens": [51118,
  322, 257, 588, 2416, 4373, 13, 51242], "temperature": 0.0, "avg_logprob": -0.27677382797491357,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.07919315248727798},
  {"id": 32, "seek": 11100, "start": 128.56, "end": 131.84, "text": " So that was
  the research group that I was a part of.", "tokens": [51242, 407, 300, 390, 264,
  2132, 1594, 300, 286, 390, 257, 644, 295, 13, 51406], "temperature": 0.0, "avg_logprob":
  -0.27677382797491357, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.07919315248727798}, {"id": 33, "seek": 11100, "start": 131.84, "end": 136.96,
  "text": " It was under Rakers, while that was developed in collaboration with some
  others.", "tokens": [51406, 467, 390, 833, 497, 19552, 11, 1339, 300, 390, 4743,
  294, 9363, 365, 512, 2357, 13, 51662], "temperature": 0.0, "avg_logprob": -0.27677382797491357,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.07919315248727798},
  {"id": 34, "seek": 13696, "start": 136.96, "end": 145.56, "text": " Anyway, around
  that time, I became very interested in using neural networks for more general purpose",
  "tokens": [50364, 5684, 11, 926, 300, 565, 11, 286, 3062, 588, 3102, 294, 1228,
  18161, 9590, 337, 544, 2674, 4334, 50794], "temperature": 0.0, "avg_logprob": -0.17008631317703812,
  "compression_ratio": 1.663003663003663, "no_speech_prob": 0.062159594148397446},
  {"id": 35, "seek": 13696, "start": 145.56, "end": 147.32, "text": " information
  retrieval.", "tokens": [50794, 1589, 19817, 3337, 13, 50882], "temperature": 0.0,
  "avg_logprob": -0.17008631317703812, "compression_ratio": 1.663003663003663, "no_speech_prob":
  0.062159594148397446}, {"id": 36, "seek": 13696, "start": 147.32, "end": 152.44,
  "text": " And I specifically formulated this question answering over a large corpus.",
  "tokens": [50882, 400, 286, 4682, 48936, 341, 1168, 13430, 670, 257, 2416, 1181,
  31624, 13, 51138], "temperature": 0.0, "avg_logprob": -0.17008631317703812, "compression_ratio":
  1.663003663003663, "no_speech_prob": 0.062159594148397446}, {"id": 37, "seek": 13696,
  "start": 152.44, "end": 157.88, "text": " And at the time, I mean, Bert, when it
  was released a year later, changed this idea.", "tokens": [51138, 400, 412, 264,
  565, 11, 286, 914, 11, 29594, 11, 562, 309, 390, 4736, 257, 1064, 1780, 11, 3105,
  341, 1558, 13, 51410], "temperature": 0.0, "avg_logprob": -0.17008631317703812,
  "compression_ratio": 1.663003663003663, "no_speech_prob": 0.062159594148397446},
  {"id": 38, "seek": 13696, "start": 157.88, "end": 162.48000000000002, "text": "
  But at the time, a lot of people would approach a machine learning problem from
  scratch.", "tokens": [51410, 583, 412, 264, 565, 11, 257, 688, 295, 561, 576, 3109,
  257, 3479, 2539, 1154, 490, 8459, 13, 51640], "temperature": 0.0, "avg_logprob":
  -0.17008631317703812, "compression_ratio": 1.663003663003663, "no_speech_prob":
  0.062159594148397446}, {"id": 39, "seek": 13696, "start": 162.48000000000002, "end":
  166.48000000000002, "text": " It would take a completely uninitialized neural network
  and then try to train it.", "tokens": [51640, 467, 576, 747, 257, 2584, 517, 259,
  270, 831, 1602, 18161, 3209, 293, 550, 853, 281, 3847, 309, 13, 51840], "temperature":
  0.0, "avg_logprob": -0.17008631317703812, "compression_ratio": 1.663003663003663,
  "no_speech_prob": 0.062159594148397446}, {"id": 40, "seek": 16648, "start": 166.48,
  "end": 173.0, "text": " And when the models get big and deep, mostly you don''t
  have enough data for your task.", "tokens": [50364, 400, 562, 264, 5245, 483, 955,
  293, 2452, 11, 5240, 291, 500, 380, 362, 1547, 1412, 337, 428, 5633, 13, 50690],
  "temperature": 0.0, "avg_logprob": -0.14112989334833054, "compression_ratio": 1.5891472868217054,
  "no_speech_prob": 0.0020516153890639544}, {"id": 41, "seek": 16648, "start": 173.0,
  "end": 178.51999999999998, "text": " And it also, you know, that doesn''t jive very
  well with if you think about how humans approach", "tokens": [50690, 400, 309, 611,
  11, 291, 458, 11, 300, 1177, 380, 361, 488, 588, 731, 365, 498, 291, 519, 466, 577,
  6255, 3109, 50966], "temperature": 0.0, "avg_logprob": -0.14112989334833054, "compression_ratio":
  1.5891472868217054, "no_speech_prob": 0.0020516153890639544}, {"id": 42, "seek":
  16648, "start": 178.51999999999998, "end": 179.51999999999998, "text": " a task.",
  "tokens": [50966, 257, 5633, 13, 51016], "temperature": 0.0, "avg_logprob": -0.14112989334833054,
  "compression_ratio": 1.5891472868217054, "no_speech_prob": 0.0020516153890639544},
  {"id": 43, "seek": 16648, "start": 179.51999999999998, "end": 183.95999999999998,
  "text": " If you ask me to answer a question or to read a message from a medical
  textbook, I may", "tokens": [51016, 759, 291, 1029, 385, 281, 1867, 257, 1168, 420,
  281, 1401, 257, 3636, 490, 257, 4625, 25591, 11, 286, 815, 51238], "temperature":
  0.0, "avg_logprob": -0.14112989334833054, "compression_ratio": 1.5891472868217054,
  "no_speech_prob": 0.0020516153890639544}, {"id": 44, "seek": 16648, "start": 183.95999999999998,
  "end": 188.92, "text": " not be a doctor, but my understanding of the English language
  will allow me to get some", "tokens": [51238, 406, 312, 257, 4631, 11, 457, 452,
  3701, 295, 264, 3669, 2856, 486, 2089, 385, 281, 483, 512, 51486], "temperature":
  0.0, "avg_logprob": -0.14112989334833054, "compression_ratio": 1.5891472868217054,
  "no_speech_prob": 0.0020516153890639544}, {"id": 45, "seek": 16648, "start": 188.92,
  "end": 192.2, "text": " of the information content from that passage.", "tokens":
  [51486, 295, 264, 1589, 2701, 490, 300, 11497, 13, 51650], "temperature": 0.0, "avg_logprob":
  -0.14112989334833054, "compression_ratio": 1.5891472868217054, "no_speech_prob":
  0.0020516153890639544}, {"id": 46, "seek": 19220, "start": 192.2, "end": 197.6,
  "text": " So in the same way, I was thinking that if a neural network is truly understanding
  language", "tokens": [50364, 407, 294, 264, 912, 636, 11, 286, 390, 1953, 300, 498,
  257, 18161, 3209, 307, 4908, 3701, 2856, 50634], "temperature": 0.0, "avg_logprob":
  -0.151705795459533, "compression_ratio": 1.5974025974025974, "no_speech_prob": 0.0024464698508381844},
  {"id": 47, "seek": 19220, "start": 197.6, "end": 200.72, "text": " in the way that
  people do, it should have this property.", "tokens": [50634, 294, 264, 636, 300,
  561, 360, 11, 309, 820, 362, 341, 4707, 13, 50790], "temperature": 0.0, "avg_logprob":
  -0.151705795459533, "compression_ratio": 1.5974025974025974, "no_speech_prob": 0.0024464698508381844},
  {"id": 48, "seek": 19220, "start": 200.72, "end": 205.92, "text": " And it should
  be possible to train a general purpose neural network that without fine tuning",
  "tokens": [50790, 400, 309, 820, 312, 1944, 281, 3847, 257, 2674, 4334, 18161, 3209,
  300, 1553, 2489, 15164, 51050], "temperature": 0.0, "avg_logprob": -0.151705795459533,
  "compression_ratio": 1.5974025974025974, "no_speech_prob": 0.0024464698508381844},
  {"id": 49, "seek": 19220, "start": 205.92, "end": 211.32, "text": " in a specific
  domain can also work reasonably well.", "tokens": [51050, 294, 257, 2685, 9274,
  393, 611, 589, 23551, 731, 13, 51320], "temperature": 0.0, "avg_logprob": -0.151705795459533,
  "compression_ratio": 1.5974025974025974, "no_speech_prob": 0.0024464698508381844},
  {"id": 50, "seek": 19220, "start": 211.32, "end": 213.2, "text": " So I set out
  to build this thing.", "tokens": [51320, 407, 286, 992, 484, 281, 1322, 341, 551,
  13, 51414], "temperature": 0.0, "avg_logprob": -0.151705795459533, "compression_ratio":
  1.5974025974025974, "no_speech_prob": 0.0024464698508381844}, {"id": 51, "seek":
  19220, "start": 213.2, "end": 216.92, "text": " And that was my research program
  in 2017.", "tokens": [51414, 400, 300, 390, 452, 2132, 1461, 294, 6591, 13, 51600],
  "temperature": 0.0, "avg_logprob": -0.151705795459533, "compression_ratio": 1.5974025974025974,
  "no_speech_prob": 0.0024464698508381844}, {"id": 52, "seek": 21692, "start": 216.92,
  "end": 223.72, "text": " And we were actually able to launch the first iteration
  of that model in a product called", "tokens": [50364, 400, 321, 645, 767, 1075,
  281, 4025, 264, 700, 24784, 295, 300, 2316, 294, 257, 1674, 1219, 50704], "temperature":
  0.0, "avg_logprob": -0.2097498807040128, "compression_ratio": 1.6374045801526718,
  "no_speech_prob": 0.007150536868721247}, {"id": 53, "seek": 21692, "start": 223.72,
  "end": 225.64, "text": " Google Talk to Books.", "tokens": [50704, 3329, 8780, 281,
  33843, 13, 50800], "temperature": 0.0, "avg_logprob": -0.2097498807040128, "compression_ratio":
  1.6374045801526718, "no_speech_prob": 0.007150536868721247}, {"id": 54, "seek":
  21692, "start": 225.64, "end": 230.56, "text": " So to, and I''m saying this to
  my knowledge, I would love if someone corrected me in the", "tokens": [50800, 407,
  281, 11, 293, 286, 478, 1566, 341, 281, 452, 3601, 11, 286, 576, 959, 498, 1580,
  31687, 385, 294, 264, 51046], "temperature": 0.0, "avg_logprob": -0.2097498807040128,
  "compression_ratio": 1.6374045801526718, "no_speech_prob": 0.007150536868721247},
  {"id": 55, "seek": 21692, "start": 230.56, "end": 232.72, "text": " comments section
  here.", "tokens": [51046, 3053, 3541, 510, 13, 51154], "temperature": 0.0, "avg_logprob":
  -0.2097498807040128, "compression_ratio": 1.6374045801526718, "no_speech_prob":
  0.007150536868721247}, {"id": 56, "seek": 21692, "start": 232.72, "end": 237.88,
  "text": " This is Google Talk to Books is the first large scale end-to-end demonstration
  of a neural", "tokens": [51154, 639, 307, 3329, 8780, 281, 33843, 307, 264, 700,
  2416, 4373, 917, 12, 1353, 12, 521, 16520, 295, 257, 18161, 51412], "temperature":
  0.0, "avg_logprob": -0.2097498807040128, "compression_ratio": 1.6374045801526718,
  "no_speech_prob": 0.007150536868721247}, {"id": 57, "seek": 21692, "start": 237.88,
  "end": 240.2, "text": " information retrieval system.", "tokens": [51412, 1589,
  19817, 3337, 1185, 13, 51528], "temperature": 0.0, "avg_logprob": -0.2097498807040128,
  "compression_ratio": 1.6374045801526718, "no_speech_prob": 0.007150536868721247},
  {"id": 58, "seek": 21692, "start": 240.2, "end": 246.88, "text": " So it is a search
  over a corpus of around 200,000 books from the Google Books corpus.", "tokens":
  [51528, 407, 309, 307, 257, 3164, 670, 257, 1181, 31624, 295, 926, 2331, 11, 1360,
  3642, 490, 264, 3329, 33843, 1181, 31624, 13, 51862], "temperature": 0.0, "avg_logprob":
  -0.2097498807040128, "compression_ratio": 1.6374045801526718, "no_speech_prob":
  0.007150536868721247}, {"id": 59, "seek": 24688, "start": 246.88, "end": 250.72,
  "text": " But it''s done entirely with vector search.", "tokens": [50364, 583, 309,
  311, 1096, 7696, 365, 8062, 3164, 13, 50556], "temperature": 0.0, "avg_logprob":
  -0.22665776704487048, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.0012818914838135242}, {"id": 60, "seek": 24688, "start": 250.72, "end": 254.07999999999998,
  "text": " And I''m not aware of anything before that.", "tokens": [50556, 400, 286,
  478, 406, 3650, 295, 1340, 949, 300, 13, 50724], "temperature": 0.0, "avg_logprob":
  -0.22665776704487048, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.0012818914838135242}, {"id": 61, "seek": 24688, "start": 254.07999999999998, "end":
  256.88, "text": " So the neural network is very important here.", "tokens": [50724,
  407, 264, 18161, 3209, 307, 588, 1021, 510, 13, 50864], "temperature": 0.0, "avg_logprob":
  -0.22665776704487048, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.0012818914838135242}, {"id": 62, "seek": 24688, "start": 256.88, "end": 262.12,
  "text": " I, not part of the team that conceived this idea and I was not actively
  working on it.", "tokens": [50864, 286, 11, 406, 644, 295, 264, 1469, 300, 34898,
  341, 1558, 293, 286, 390, 406, 13022, 1364, 322, 309, 13, 51126], "temperature":
  0.0, "avg_logprob": -0.22665776704487048, "compression_ratio": 1.6153846153846154,
  "no_speech_prob": 0.0012818914838135242}, {"id": 63, "seek": 24688, "start": 262.12,
  "end": 267.08, "text": " They had a neural network which wasn''t producing good
  enough results.", "tokens": [51126, 814, 632, 257, 18161, 3209, 597, 2067, 380,
  10501, 665, 1547, 3542, 13, 51374], "temperature": 0.0, "avg_logprob": -0.22665776704487048,
  "compression_ratio": 1.6153846153846154, "no_speech_prob": 0.0012818914838135242},
  {"id": 64, "seek": 24688, "start": 267.08, "end": 272.24, "text": " And we put in
  this more general purpose question answering your network and the results dramatically",
  "tokens": [51374, 400, 321, 829, 294, 341, 544, 2674, 4334, 1168, 13430, 428, 3209,
  293, 264, 3542, 17548, 51632], "temperature": 0.0, "avg_logprob": -0.22665776704487048,
  "compression_ratio": 1.6153846153846154, "no_speech_prob": 0.0012818914838135242},
  {"id": 65, "seek": 24688, "start": 272.24, "end": 273.24, "text": " improved.",
  "tokens": [51632, 9689, 13, 51682], "temperature": 0.0, "avg_logprob": -0.22665776704487048,
  "compression_ratio": 1.6153846153846154, "no_speech_prob": 0.0012818914838135242},
  {"id": 66, "seek": 27324, "start": 273.24, "end": 275.8, "text": " This was basically
  the first rollout.", "tokens": [50364, 639, 390, 1936, 264, 700, 3373, 346, 13,
  50492], "temperature": 0.0, "avg_logprob": -0.170166015625, "compression_ratio":
  1.5798319327731092, "no_speech_prob": 0.00768980011343956}, {"id": 67, "seek": 27324,
  "start": 275.8, "end": 281.40000000000003, "text": " But then what I observed over
  the subsequent years was that I was able to take exactly", "tokens": [50492, 583,
  550, 437, 286, 13095, 670, 264, 19962, 924, 390, 300, 286, 390, 1075, 281, 747,
  2293, 50772], "temperature": 0.0, "avg_logprob": -0.170166015625, "compression_ratio":
  1.5798319327731092, "no_speech_prob": 0.00768980011343956}, {"id": 68, "seek": 27324,
  "start": 281.40000000000003, "end": 287.88, "text": " the same neural network and
  apply it in at least six different products within Google.", "tokens": [50772, 264,
  912, 18161, 3209, 293, 3079, 309, 294, 412, 1935, 2309, 819, 3383, 1951, 3329, 13,
  51096], "temperature": 0.0, "avg_logprob": -0.170166015625, "compression_ratio":
  1.5798319327731092, "no_speech_prob": 0.00768980011343956}, {"id": 69, "seek": 27324,
  "start": 287.88, "end": 296.04, "text": " And this is what convinced me of the business
  value of what had been demonstrated here.", "tokens": [51096, 400, 341, 307, 437,
  12561, 385, 295, 264, 1606, 2158, 295, 437, 632, 668, 18772, 510, 13, 51504], "temperature":
  0.0, "avg_logprob": -0.170166015625, "compression_ratio": 1.5798319327731092, "no_speech_prob":
  0.00768980011343956}, {"id": 70, "seek": 27324, "start": 296.04, "end": 301.64,
  "text": " This could actually improve metrics and products used by millions of people.",
  "tokens": [51504, 639, 727, 767, 3470, 16367, 293, 3383, 1143, 538, 6803, 295, 561,
  13, 51784], "temperature": 0.0, "avg_logprob": -0.170166015625, "compression_ratio":
  1.5798319327731092, "no_speech_prob": 0.00768980011343956}, {"id": 71, "seek": 30164,
  "start": 301.64, "end": 307.44, "text": " And so this was essentially the genesis
  of the idea of the ZRAI.", "tokens": [50364, 400, 370, 341, 390, 4476, 264, 1049,
  9374, 295, 264, 1558, 295, 264, 1176, 3750, 40, 13, 50654], "temperature": 0.0,
  "avg_logprob": -0.2683603161963347, "compression_ratio": 1.5597014925373134, "no_speech_prob":
  0.0020390308927744627}, {"id": 72, "seek": 30164, "start": 307.44, "end": 312.71999999999997,
  "text": " We started me in my co-founder in 2020 and the objective is to provide
  something like", "tokens": [50654, 492, 1409, 385, 294, 452, 598, 12, 33348, 294,
  4808, 293, 264, 10024, 307, 281, 2893, 746, 411, 50918], "temperature": 0.0, "avg_logprob":
  -0.2683603161963347, "compression_ratio": 1.5597014925373134, "no_speech_prob":
  0.0020390308927744627}, {"id": 73, "seek": 30164, "start": 312.71999999999997, "end":
  317.71999999999997, "text": " elastic search or algolia, except using the principles
  of neural information retrieval.", "tokens": [50918, 17115, 3164, 420, 3501, 29760,
  11, 3993, 1228, 264, 9156, 295, 18161, 1589, 19817, 3337, 13, 51168], "temperature":
  0.0, "avg_logprob": -0.2683603161963347, "compression_ratio": 1.5597014925373134,
  "no_speech_prob": 0.0020390308927744627}, {"id": 74, "seek": 30164, "start": 317.71999999999997,
  "end": 325.03999999999996, "text": " So as you know, elastic search and algolia
  are based on the BM25 algorithm fundamentally.", "tokens": [51168, 407, 382, 291,
  458, 11, 17115, 3164, 293, 3501, 29760, 366, 2361, 322, 264, 15901, 6074, 9284,
  17879, 13, 51534], "temperature": 0.0, "avg_logprob": -0.2683603161963347, "compression_ratio":
  1.5597014925373134, "no_speech_prob": 0.0020390308927744627}, {"id": 75, "seek":
  30164, "start": 325.03999999999996, "end": 327.64, "text": " So yeah, so that''s
  what we''ve been doing for the last two years.", "tokens": [51534, 407, 1338, 11,
  370, 300, 311, 437, 321, 600, 668, 884, 337, 264, 1036, 732, 924, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.2683603161963347, "compression_ratio": 1.5597014925373134,
  "no_speech_prob": 0.0020390308927744627}, {"id": 76, "seek": 30164, "start": 327.64,
  "end": 329.2, "text": " Yeah, this is fantastic.", "tokens": [51664, 865, 11, 341,
  307, 5456, 13, 51742], "temperature": 0.0, "avg_logprob": -0.2683603161963347, "compression_ratio":
  1.5597014925373134, "no_speech_prob": 0.0020390308927744627}, {"id": 77, "seek":
  32920, "start": 329.2, "end": 334.84, "text": " I mean, it''s fantastic also that
  you bring your experience from such a large company innovating", "tokens": [50364,
  286, 914, 11, 309, 311, 5456, 611, 300, 291, 1565, 428, 1752, 490, 1270, 257, 2416,
  2237, 5083, 990, 50646], "temperature": 0.0, "avg_logprob": -0.21437828063964845,
  "compression_ratio": 1.5193798449612403, "no_speech_prob": 0.003055588575080037},
  {"id": 78, "seek": 32920, "start": 334.84, "end": 336.32, "text": " in search, right?",
  "tokens": [50646, 294, 3164, 11, 558, 30, 50720], "temperature": 0.0, "avg_logprob":
  -0.21437828063964845, "compression_ratio": 1.5193798449612403, "no_speech_prob":
  0.003055588575080037}, {"id": 79, "seek": 32920, "start": 336.32, "end": 341.48,
  "text": " Over to, you know, the rest of the world essentially, right?", "tokens":
  [50720, 4886, 281, 11, 291, 458, 11, 264, 1472, 295, 264, 1002, 4476, 11, 558, 30,
  50978], "temperature": 0.0, "avg_logprob": -0.21437828063964845, "compression_ratio":
  1.5193798449612403, "no_speech_prob": 0.003055588575080037}, {"id": 80, "seek":
  32920, "start": 341.48, "end": 346.52, "text": " So that I believe your goal is
  to apply this with as many clients as possible.", "tokens": [50978, 407, 300, 286,
  1697, 428, 3387, 307, 281, 3079, 341, 365, 382, 867, 6982, 382, 1944, 13, 51230],
  "temperature": 0.0, "avg_logprob": -0.21437828063964845, "compression_ratio": 1.5193798449612403,
  "no_speech_prob": 0.003055588575080037}, {"id": 81, "seek": 32920, "start": 346.52,
  "end": 351.03999999999996, "text": " And are you focusing mostly on NLP at the moment,
  natural language processing?", "tokens": [51230, 400, 366, 291, 8416, 5240, 322,
  426, 45196, 412, 264, 1623, 11, 3303, 2856, 9007, 30, 51456], "temperature": 0.0,
  "avg_logprob": -0.21437828063964845, "compression_ratio": 1.5193798449612403, "no_speech_prob":
  0.003055588575080037}, {"id": 82, "seek": 32920, "start": 351.03999999999996, "end":
  356.08, "text": " Yeah, so well, we''re focused from a customer''s perspective.",
  "tokens": [51456, 865, 11, 370, 731, 11, 321, 434, 5178, 490, 257, 5474, 311, 4585,
  13, 51708], "temperature": 0.0, "avg_logprob": -0.21437828063964845, "compression_ratio":
  1.5193798449612403, "no_speech_prob": 0.003055588575080037}, {"id": 83, "seek":
  35608, "start": 356.08, "end": 359.28, "text": " We provide a tech search solution.",
  "tokens": [50364, 492, 2893, 257, 7553, 3164, 3827, 13, 50524], "temperature": 0.0,
  "avg_logprob": -0.2024254384248153, "compression_ratio": 1.6018099547511313, "no_speech_prob":
  0.001940710935741663}, {"id": 84, "seek": 35608, "start": 359.28, "end": 366.03999999999996,
  "text": " Now, one of the beauties of embedding based techniques is that in your
  network,", "tokens": [50524, 823, 11, 472, 295, 264, 1869, 530, 295, 12240, 3584,
  2361, 7512, 307, 300, 294, 428, 3209, 11, 50862], "temperature": 0.0, "avg_logprob":
  -0.2024254384248153, "compression_ratio": 1.6018099547511313, "no_speech_prob":
  0.001940710935741663}, {"id": 85, "seek": 35608, "start": 366.03999999999996, "end":
  372.03999999999996, "text": " you can go beyond text and you can embed images, video
  and other types of media", "tokens": [50862, 291, 393, 352, 4399, 2487, 293, 291,
  393, 12240, 5267, 11, 960, 293, 661, 3467, 295, 3021, 51162], "temperature": 0.0,
  "avg_logprob": -0.2024254384248153, "compression_ratio": 1.6018099547511313, "no_speech_prob":
  0.001940710935741663}, {"id": 86, "seek": 35608, "start": 372.03999999999996, "end":
  374.28, "text": " into a common embedding space.", "tokens": [51162, 666, 257, 2689,
  12240, 3584, 1901, 13, 51274], "temperature": 0.0, "avg_logprob": -0.2024254384248153,
  "compression_ratio": 1.6018099547511313, "no_speech_prob": 0.001940710935741663},
  {"id": 87, "seek": 35608, "start": 374.28, "end": 378.32, "text": " So that is where
  this company will eventually go.", "tokens": [51274, 407, 300, 307, 689, 341, 2237,
  486, 4728, 352, 13, 51476], "temperature": 0.0, "avg_logprob": -0.2024254384248153,
  "compression_ratio": 1.6018099547511313, "no_speech_prob": 0.001940710935741663},
  {"id": 88, "seek": 35608, "start": 378.32, "end": 384.15999999999997, "text": "
  But my roots are in NLP and I think that tech search by itself is a large area",
  "tokens": [51476, 583, 452, 10669, 366, 294, 426, 45196, 293, 286, 519, 300, 7553,
  3164, 538, 2564, 307, 257, 2416, 1859, 51768], "temperature": 0.0, "avg_logprob":
  -0.2024254384248153, "compression_ratio": 1.6018099547511313, "no_speech_prob":
  0.001940710935741663}, {"id": 89, "seek": 38416, "start": 384.16, "end": 385.6,
  "text": " that takes an effort to do well.", "tokens": [50364, 300, 2516, 364, 4630,
  281, 360, 731, 13, 50436], "temperature": 0.0, "avg_logprob": -0.21838103584621263,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.002856289502233267},
  {"id": 90, "seek": 38416, "start": 385.6, "end": 388.96000000000004, "text": " So
  that''s where we''re focused initially.", "tokens": [50436, 407, 300, 311, 689,
  321, 434, 5178, 9105, 13, 50604], "temperature": 0.0, "avg_logprob": -0.21838103584621263,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.002856289502233267},
  {"id": 91, "seek": 38416, "start": 388.96000000000004, "end": 390.36, "text": "
  Yeah, that makes total sense.", "tokens": [50604, 865, 11, 300, 1669, 3217, 2020,
  13, 50674], "temperature": 0.0, "avg_logprob": -0.21838103584621263, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.002856289502233267}, {"id": 92, "seek":
  38416, "start": 390.36, "end": 396.56, "text": " But as you said, you know, vector
  search is not kind of constrained by the application", "tokens": [50674, 583, 382,
  291, 848, 11, 291, 458, 11, 8062, 3164, 307, 406, 733, 295, 38901, 538, 264, 3861,
  50984], "temperature": 0.0, "avg_logprob": -0.21838103584621263, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.002856289502233267}, {"id": 93, "seek":
  38416, "start": 396.56, "end": 398.88000000000005, "text": " as long as you can
  embed it, right?", "tokens": [50984, 382, 938, 382, 291, 393, 12240, 309, 11, 558,
  30, 51100], "temperature": 0.0, "avg_logprob": -0.21838103584621263, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.002856289502233267}, {"id": 94, "seek":
  38416, "start": 398.88000000000005, "end": 404.0, "text": " And plus all these multimodal
  scenarios where you can combine, let''s say,", "tokens": [51100, 400, 1804, 439,
  613, 32972, 378, 304, 15077, 689, 291, 393, 10432, 11, 718, 311, 584, 11, 51356],
  "temperature": 0.0, "avg_logprob": -0.21838103584621263, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.002856289502233267}, {"id": 95, "seek": 38416, "start": 404.0,
  "end": 408.04, "text": " your camera pointed at something and then you''re talking
  to it and then you can kind of", "tokens": [51356, 428, 2799, 10932, 412, 746, 293,
  550, 291, 434, 1417, 281, 309, 293, 550, 291, 393, 733, 295, 51558], "temperature":
  0.0, "avg_logprob": -0.21838103584621263, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.002856289502233267}, {"id": 96, "seek": 38416, "start": 408.04,
  "end": 411.48, "text": " get some textual matches and suggestions, right?", "tokens":
  [51558, 483, 512, 2487, 901, 10676, 293, 13396, 11, 558, 30, 51730], "temperature":
  0.0, "avg_logprob": -0.21838103584621263, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.002856289502233267}, {"id": 97, "seek": 41148, "start": 411.48,
  "end": 414.36, "text": " So that could be a very rich experience.", "tokens": [50364,
  407, 300, 727, 312, 257, 588, 4593, 1752, 13, 50508], "temperature": 0.0, "avg_logprob":
  -0.21947385646678783, "compression_ratio": 1.5818815331010454, "no_speech_prob":
  0.0024948555510491133}, {"id": 98, "seek": 41148, "start": 414.36, "end": 415.16,
  "text": " Right, right.", "tokens": [50508, 1779, 11, 558, 13, 50548], "temperature":
  0.0, "avg_logprob": -0.21947385646678783, "compression_ratio": 1.5818815331010454,
  "no_speech_prob": 0.0024948555510491133}, {"id": 99, "seek": 41148, "start": 415.16,
  "end": 422.16, "text": " And that particular application is actually achievable
  now, even in an all text platform,", "tokens": [50548, 400, 300, 1729, 3861, 307,
  767, 3538, 17915, 586, 11, 754, 294, 364, 439, 2487, 3663, 11, 50898], "temperature":
  0.0, "avg_logprob": -0.21947385646678783, "compression_ratio": 1.5818815331010454,
  "no_speech_prob": 0.0024948555510491133}, {"id": 100, "seek": 41148, "start": 422.16,
  "end": 424.6, "text": " if you feed the transcripts in.", "tokens": [50898, 498,
  291, 3154, 264, 24444, 82, 294, 13, 51020], "temperature": 0.0, "avg_logprob": -0.21947385646678783,
  "compression_ratio": 1.5818815331010454, "no_speech_prob": 0.0024948555510491133},
  {"id": 101, "seek": 41148, "start": 424.6, "end": 430.04, "text": " And these neural
  network approaches tend to work especially well with natural speech,", "tokens":
  [51020, 400, 613, 18161, 3209, 11587, 3928, 281, 589, 2318, 731, 365, 3303, 6218,
  11, 51292], "temperature": 0.0, "avg_logprob": -0.21947385646678783, "compression_ratio":
  1.5818815331010454, "no_speech_prob": 0.0024948555510491133}, {"id": 102, "seek":
  41148, "start": 430.04, "end": 431.44, "text": " both as query input.", "tokens":
  [51292, 1293, 382, 14581, 4846, 13, 51362], "temperature": 0.0, "avg_logprob": -0.21947385646678783,
  "compression_ratio": 1.5818815331010454, "no_speech_prob": 0.0024948555510491133},
  {"id": 103, "seek": 41148, "start": 431.44, "end": 436.68, "text": " So this is
  why they''re often used in technologies like Assistant or Alexa.", "tokens": [51362,
  407, 341, 307, 983, 436, 434, 2049, 1143, 294, 7943, 411, 14890, 420, 22595, 13,
  51624], "temperature": 0.0, "avg_logprob": -0.21947385646678783, "compression_ratio":
  1.5818815331010454, "no_speech_prob": 0.0024948555510491133}, {"id": 104, "seek":
  41148, "start": 436.68, "end": 440.08000000000004, "text": " Because people, when
  they speak, it''s obviously much different than when you''re typing keywords", "tokens":
  [51624, 1436, 561, 11, 562, 436, 1710, 11, 309, 311, 2745, 709, 819, 813, 562, 291,
  434, 18444, 21009, 51794], "temperature": 0.0, "avg_logprob": -0.21947385646678783,
  "compression_ratio": 1.5818815331010454, "no_speech_prob": 0.0024948555510491133},
  {"id": 105, "seek": 44008, "start": 440.08, "end": 443.12, "text": " in a search
  box with your keyboard.", "tokens": [50364, 294, 257, 3164, 2424, 365, 428, 10186,
  13, 50516], "temperature": 0.0, "avg_logprob": -0.22153741805279842, "compression_ratio":
  1.708185053380783, "no_speech_prob": 0.0015338828088715672}, {"id": 106, "seek":
  44008, "start": 443.12, "end": 447.03999999999996, "text": " But then also when
  searching over natural language text like transcripts.", "tokens": [50516, 583,
  550, 611, 562, 10808, 670, 3303, 2856, 2487, 411, 24444, 82, 13, 50712], "temperature":
  0.0, "avg_logprob": -0.22153741805279842, "compression_ratio": 1.708185053380783,
  "no_speech_prob": 0.0015338828088715672}, {"id": 107, "seek": 44008, "start": 447.03999999999996,
  "end": 448.24, "text": " Yeah, absolutely.", "tokens": [50712, 865, 11, 3122, 13,
  50772], "temperature": 0.0, "avg_logprob": -0.22153741805279842, "compression_ratio":
  1.708185053380783, "no_speech_prob": 0.0015338828088715672}, {"id": 108, "seek":
  44008, "start": 448.24, "end": 453.03999999999996, "text": " And when you say neural
  networks, you know, some of them, let''s say, vector database providers", "tokens":
  [50772, 400, 562, 291, 584, 18161, 9590, 11, 291, 458, 11, 512, 295, 552, 11, 718,
  311, 584, 11, 8062, 8149, 11330, 51012], "temperature": 0.0, "avg_logprob": -0.22153741805279842,
  "compression_ratio": 1.708185053380783, "no_speech_prob": 0.0015338828088715672},
  {"id": 109, "seek": 44008, "start": 453.03999999999996, "end": 457.71999999999997,
  "text": " and vendors on the market, they give you sort of this machinery.", "tokens":
  [51012, 293, 22056, 322, 264, 2142, 11, 436, 976, 291, 1333, 295, 341, 27302, 13,
  51246], "temperature": 0.0, "avg_logprob": -0.22153741805279842, "compression_ratio":
  1.708185053380783, "no_speech_prob": 0.0015338828088715672}, {"id": 110, "seek":
  44008, "start": 457.71999999999997, "end": 459.03999999999996, "text": " You can
  plug in some models.", "tokens": [51246, 509, 393, 5452, 294, 512, 5245, 13, 51312],
  "temperature": 0.0, "avg_logprob": -0.22153741805279842, "compression_ratio": 1.708185053380783,
  "no_speech_prob": 0.0015338828088715672}, {"id": 111, "seek": 44008, "start": 459.03999999999996,
  "end": 463.71999999999997, "text": " They also have some models available, let''s
  say, from hugging face.", "tokens": [51312, 814, 611, 362, 512, 5245, 2435, 11,
  718, 311, 584, 11, 490, 41706, 1851, 13, 51546], "temperature": 0.0, "avg_logprob":
  -0.22153741805279842, "compression_ratio": 1.708185053380783, "no_speech_prob":
  0.0015338828088715672}, {"id": 112, "seek": 44008, "start": 463.71999999999997,
  "end": 469.56, "text": " In your case, in case of ZRI, are you innovating in this
  space of creating this neural networks", "tokens": [51546, 682, 428, 1389, 11, 294,
  1389, 295, 1176, 5577, 11, 366, 291, 5083, 990, 294, 341, 1901, 295, 4084, 341,
  18161, 9590, 51838], "temperature": 0.0, "avg_logprob": -0.22153741805279842, "compression_ratio":
  1.708185053380783, "no_speech_prob": 0.0015338828088715672}, {"id": 113, "seek":
  46956, "start": 469.56, "end": 471.16, "text": " for your clients?", "tokens": [50364,
  337, 428, 6982, 30, 50444], "temperature": 0.0, "avg_logprob": -0.18582420349121093,
  "compression_ratio": 1.6156716417910448, "no_speech_prob": 0.002171857515349984},
  {"id": 114, "seek": 46956, "start": 471.16, "end": 475.24, "text": " Yes, we are
  approaching the problem holistically.", "tokens": [50444, 1079, 11, 321, 366, 14908,
  264, 1154, 4091, 20458, 13, 50648], "temperature": 0.0, "avg_logprob": -0.18582420349121093,
  "compression_ratio": 1.6156716417910448, "no_speech_prob": 0.002171857515349984},
  {"id": 115, "seek": 46956, "start": 475.24, "end": 481.48, "text": " So we''re,
  you know, the vector database is one critical component of a neural information",
  "tokens": [50648, 407, 321, 434, 11, 291, 458, 11, 264, 8062, 8149, 307, 472, 4924,
  6542, 295, 257, 18161, 1589, 50960], "temperature": 0.0, "avg_logprob": -0.18582420349121093,
  "compression_ratio": 1.6156716417910448, "no_speech_prob": 0.002171857515349984},
  {"id": 116, "seek": 46956, "start": 481.48, "end": 483.08, "text": " retrieval system.",
  "tokens": [50960, 19817, 3337, 1185, 13, 51040], "temperature": 0.0, "avg_logprob":
  -0.18582420349121093, "compression_ratio": 1.6156716417910448, "no_speech_prob":
  0.002171857515349984}, {"id": 117, "seek": 46956, "start": 483.08, "end": 488.56,
  "text": " But there''s other pieces, for instance, like the re-ranking piece or
  the neural network", "tokens": [51040, 583, 456, 311, 661, 3755, 11, 337, 5197,
  11, 411, 264, 319, 12, 20479, 278, 2522, 420, 264, 18161, 3209, 51314], "temperature":
  0.0, "avg_logprob": -0.18582420349121093, "compression_ratio": 1.6156716417910448,
  "no_speech_prob": 0.002171857515349984}, {"id": 118, "seek": 46956, "start": 488.56,
  "end": 490.2, "text": " that produces the embeddings.", "tokens": [51314, 300, 14725,
  264, 12240, 29432, 13, 51396], "temperature": 0.0, "avg_logprob": -0.18582420349121093,
  "compression_ratio": 1.6156716417910448, "no_speech_prob": 0.002171857515349984},
  {"id": 119, "seek": 46956, "start": 490.2, "end": 492.76, "text": " And all of these
  need to work in coordination and tandem.", "tokens": [51396, 400, 439, 295, 613,
  643, 281, 589, 294, 21252, 293, 48120, 13, 51524], "temperature": 0.0, "avg_logprob":
  -0.18582420349121093, "compression_ratio": 1.6156716417910448, "no_speech_prob":
  0.002171857515349984}, {"id": 120, "seek": 46956, "start": 492.76, "end": 497.04,
  "text": " Ideally, when they do, you can squeeze a lot more performance out of this
  system.", "tokens": [51524, 40817, 11, 562, 436, 360, 11, 291, 393, 13578, 257,
  688, 544, 3389, 484, 295, 341, 1185, 13, 51738], "temperature": 0.0, "avg_logprob":
  -0.18582420349121093, "compression_ratio": 1.6156716417910448, "no_speech_prob":
  0.002171857515349984}, {"id": 121, "seek": 49704, "start": 497.04, "end": 502.44,
  "text": " So yes, our focus is on, we even handle data ingestion.", "tokens": [50364,
  407, 2086, 11, 527, 1879, 307, 322, 11, 321, 754, 4813, 1412, 3957, 31342, 13, 50634],
  "temperature": 0.0, "avg_logprob": -0.17426842037994084, "compression_ratio": 1.5756302521008403,
  "no_speech_prob": 0.0017174474196508527}, {"id": 122, "seek": 49704, "start": 502.44,
  "end": 504.28000000000003, "text": " It''s not a big area of focus.", "tokens":
  [50634, 467, 311, 406, 257, 955, 1859, 295, 1879, 13, 50726], "temperature": 0.0,
  "avg_logprob": -0.17426842037994084, "compression_ratio": 1.5756302521008403, "no_speech_prob":
  0.0017174474196508527}, {"id": 123, "seek": 49704, "start": 504.28000000000003,
  "end": 511.24, "text": " But the reality is that you have to make your experiences
  as easy as possible for widespread", "tokens": [50726, 583, 264, 4103, 307, 300,
  291, 362, 281, 652, 428, 5235, 382, 1858, 382, 1944, 337, 22679, 51074], "temperature":
  0.0, "avg_logprob": -0.17426842037994084, "compression_ratio": 1.5756302521008403,
  "no_speech_prob": 0.0017174474196508527}, {"id": 124, "seek": 49704, "start": 511.24,
  "end": 512.9200000000001, "text": " adoption, I think.", "tokens": [51074, 19215,
  11, 286, 519, 13, 51158], "temperature": 0.0, "avg_logprob": -0.17426842037994084,
  "compression_ratio": 1.5756302521008403, "no_speech_prob": 0.0017174474196508527},
  {"id": 125, "seek": 49704, "start": 512.9200000000001, "end": 519.64, "text": "
  So we allow our customers to just shovel in, you know, PDF documents and all kinds
  of", "tokens": [51158, 407, 321, 2089, 527, 4581, 281, 445, 29789, 294, 11, 291,
  458, 11, 17752, 8512, 293, 439, 3685, 295, 51494], "temperature": 0.0, "avg_logprob":
  -0.17426842037994084, "compression_ratio": 1.5756302521008403, "no_speech_prob":
  0.0017174474196508527}, {"id": 126, "seek": 49704, "start": 519.64, "end": 521.04,
  "text": " other formats.", "tokens": [51494, 661, 25879, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.17426842037994084, "compression_ratio": 1.5756302521008403,
  "no_speech_prob": 0.0017174474196508527}, {"id": 127, "seek": 49704, "start": 521.04,
  "end": 522.52, "text": " We perform the text extraction.", "tokens": [51564, 492,
  2042, 264, 2487, 30197, 13, 51638], "temperature": 0.0, "avg_logprob": -0.17426842037994084,
  "compression_ratio": 1.5756302521008403, "no_speech_prob": 0.0017174474196508527},
  {"id": 128, "seek": 49704, "start": 522.52, "end": 524.48, "text": " We perform
  the segmentation of the document.", "tokens": [51638, 492, 2042, 264, 9469, 399,
  295, 264, 4166, 13, 51736], "temperature": 0.0, "avg_logprob": -0.17426842037994084,
  "compression_ratio": 1.5756302521008403, "no_speech_prob": 0.0017174474196508527},
  {"id": 129, "seek": 52448, "start": 524.48, "end": 529.32, "text": " And we actually
  do the encoding with the neural network, build the vector database and then", "tokens":
  [50364, 400, 321, 767, 360, 264, 43430, 365, 264, 18161, 3209, 11, 1322, 264, 8062,
  8149, 293, 550, 50606], "temperature": 0.0, "avg_logprob": -0.22864268596907308,
  "compression_ratio": 1.68259385665529, "no_speech_prob": 0.020112542435526848},
  {"id": 130, "seek": 52448, "start": 529.32, "end": 531.24, "text": " handle the
  serving as well.", "tokens": [50606, 4813, 264, 8148, 382, 731, 13, 50702], "temperature":
  0.0, "avg_logprob": -0.22864268596907308, "compression_ratio": 1.68259385665529,
  "no_speech_prob": 0.020112542435526848}, {"id": 131, "seek": 52448, "start": 531.24,
  "end": 533.72, "text": " Yeah, so it sounds like an all-around solution.", "tokens":
  [50702, 865, 11, 370, 309, 3263, 411, 364, 439, 12, 25762, 3827, 13, 50826], "temperature":
  0.0, "avg_logprob": -0.22864268596907308, "compression_ratio": 1.68259385665529,
  "no_speech_prob": 0.020112542435526848}, {"id": 132, "seek": 52448, "start": 533.72,
  "end": 537.8000000000001, "text": " And I mean, it''s very typical, you know, in
  some sense kind of to bring some algorithm", "tokens": [50826, 400, 286, 914, 11,
  309, 311, 588, 7476, 11, 291, 458, 11, 294, 512, 2020, 733, 295, 281, 1565, 512,
  9284, 51030], "temperature": 0.0, "avg_logprob": -0.22864268596907308, "compression_ratio":
  1.68259385665529, "no_speech_prob": 0.020112542435526848}, {"id": 133, "seek": 52448,
  "start": 537.8000000000001, "end": 541.12, "text": " or some idea to the market,
  but like it doesn''t have any connectors.", "tokens": [51030, 420, 512, 1558, 281,
  264, 2142, 11, 457, 411, 309, 1177, 380, 362, 604, 31865, 13, 51196], "temperature":
  0.0, "avg_logprob": -0.22864268596907308, "compression_ratio": 1.68259385665529,
  "no_speech_prob": 0.020112542435526848}, {"id": 134, "seek": 52448, "start": 541.12,
  "end": 542.84, "text": " Okay, how do I feed data into it?", "tokens": [51196, 1033,
  11, 577, 360, 286, 3154, 1412, 666, 309, 30, 51282], "temperature": 0.0, "avg_logprob":
  -0.22864268596907308, "compression_ratio": 1.68259385665529, "no_speech_prob": 0.020112542435526848},
  {"id": 135, "seek": 52448, "start": 542.84, "end": 545.52, "text": " Or maybe there
  is like a simple demo.", "tokens": [51282, 1610, 1310, 456, 307, 411, 257, 2199,
  10723, 13, 51416], "temperature": 0.0, "avg_logprob": -0.22864268596907308, "compression_ratio":
  1.68259385665529, "no_speech_prob": 0.020112542435526848}, {"id": 136, "seek": 52448,
  "start": 545.52, "end": 547.76, "text": " And yeah, nothing beyond that.", "tokens":
  [51416, 400, 1338, 11, 1825, 4399, 300, 13, 51528], "temperature": 0.0, "avg_logprob":
  -0.22864268596907308, "compression_ratio": 1.68259385665529, "no_speech_prob": 0.020112542435526848},
  {"id": 137, "seek": 52448, "start": 547.76, "end": 553.44, "text": " But it sounds
  like you are taking the kind of all-around approach.", "tokens": [51528, 583, 309,
  3263, 411, 291, 366, 1940, 264, 733, 295, 439, 12, 25762, 3109, 13, 51812], "temperature":
  0.0, "avg_logprob": -0.22864268596907308, "compression_ratio": 1.68259385665529,
  "no_speech_prob": 0.020112542435526848}, {"id": 138, "seek": 55344, "start": 553.44,
  "end": 560.1600000000001, "text": " And have you been looking to implement everything
  yourself or are you also kind of reusing some", "tokens": [50364, 400, 362, 291,
  668, 1237, 281, 4445, 1203, 1803, 420, 366, 291, 611, 733, 295, 319, 7981, 512,
  50700], "temperature": 0.0, "avg_logprob": -0.2266206643016068, "compression_ratio":
  1.6, "no_speech_prob": 0.0018445164896547794}, {"id": 139, "seek": 55344, "start":
  560.1600000000001, "end": 566.6800000000001, "text": " of the open source pipelines,
  you know, like for example, for embedding or for document", "tokens": [50700, 295,
  264, 1269, 4009, 40168, 11, 291, 458, 11, 411, 337, 1365, 11, 337, 12240, 3584,
  420, 337, 4166, 51026], "temperature": 0.0, "avg_logprob": -0.2266206643016068,
  "compression_ratio": 1.6, "no_speech_prob": 0.0018445164896547794}, {"id": 140,
  "seek": 55344, "start": 566.6800000000001, "end": 569.36, "text": " conversions
  and so on?", "tokens": [51026, 42256, 293, 370, 322, 30, 51160], "temperature":
  0.0, "avg_logprob": -0.2266206643016068, "compression_ratio": 1.6, "no_speech_prob":
  0.0018445164896547794}, {"id": 141, "seek": 55344, "start": 569.36, "end": 577.12,
  "text": " Yeah, we are using open source as much as we can and where we think it
  makes sense.", "tokens": [51160, 865, 11, 321, 366, 1228, 1269, 4009, 382, 709,
  382, 321, 393, 293, 689, 321, 519, 309, 1669, 2020, 13, 51548], "temperature": 0.0,
  "avg_logprob": -0.2266206643016068, "compression_ratio": 1.6, "no_speech_prob":
  0.0018445164896547794}, {"id": 142, "seek": 55344, "start": 577.12, "end": 581.84,
  "text": " So for instance, for content extraction, there''s a Pashitika, which is
  a very good framework.", "tokens": [51548, 407, 337, 5197, 11, 337, 2701, 30197,
  11, 456, 311, 257, 430, 1299, 270, 5439, 11, 597, 307, 257, 588, 665, 8388, 13,
  51784], "temperature": 0.0, "avg_logprob": -0.2266206643016068, "compression_ratio":
  1.6, "no_speech_prob": 0.0018445164896547794}, {"id": 143, "seek": 58184, "start":
  581.84, "end": 586.5600000000001, "text": " But then there are certain document
  types for which there are better alternatives out", "tokens": [50364, 583, 550,
  456, 366, 1629, 4166, 3467, 337, 597, 456, 366, 1101, 20478, 484, 50600], "temperature":
  0.0, "avg_logprob": -0.2829961858244024, "compression_ratio": 1.7132075471698114,
  "no_speech_prob": 0.0045359134674072266}, {"id": 144, "seek": 58184, "start": 586.5600000000001,
  "end": 587.5600000000001, "text": " there.", "tokens": [50600, 456, 13, 50650],
  "temperature": 0.0, "avg_logprob": -0.2829961858244024, "compression_ratio": 1.7132075471698114,
  "no_speech_prob": 0.0045359134674072266}, {"id": 145, "seek": 58184, "start": 587.5600000000001,
  "end": 592.6, "text": " And, you know, we''ve had certain customers for which PDF
  extraction, for instance, was a priority.", "tokens": [50650, 400, 11, 291, 458,
  11, 321, 600, 632, 1629, 4581, 337, 597, 17752, 30197, 11, 337, 5197, 11, 390, 257,
  9365, 13, 50902], "temperature": 0.0, "avg_logprob": -0.2829961858244024, "compression_ratio":
  1.7132075471698114, "no_speech_prob": 0.0045359134674072266}, {"id": 146, "seek":
  58184, "start": 592.6, "end": 597.32, "text": " And we discovered some shortfalls
  with Tick-N-We went and we researched and found there''s better", "tokens": [50902,
  400, 321, 6941, 512, 2099, 18542, 365, 314, 618, 12, 45, 12, 4360, 1437, 293, 321,
  37098, 293, 1352, 456, 311, 1101, 51138], "temperature": 0.0, "avg_logprob": -0.2829961858244024,
  "compression_ratio": 1.7132075471698114, "no_speech_prob": 0.0045359134674072266},
  {"id": 147, "seek": 58184, "start": 597.32, "end": 598.32, "text": " alternatives
  out there.", "tokens": [51138, 20478, 484, 456, 13, 51188], "temperature": 0.0,
  "avg_logprob": -0.2829961858244024, "compression_ratio": 1.7132075471698114, "no_speech_prob":
  0.0045359134674072266}, {"id": 148, "seek": 58184, "start": 598.32, "end": 599.8000000000001,
  "text": " And so we''ve got those implemented.", "tokens": [51188, 400, 370, 321,
  600, 658, 729, 12270, 13, 51262], "temperature": 0.0, "avg_logprob": -0.2829961858244024,
  "compression_ratio": 1.7132075471698114, "no_speech_prob": 0.0045359134674072266},
  {"id": 149, "seek": 58184, "start": 599.8000000000001, "end": 602.32, "text": "
  But we didn''t write a PDF extractor from scratch, obviously.", "tokens": [51262,
  583, 321, 994, 380, 2464, 257, 17752, 8947, 284, 490, 8459, 11, 2745, 13, 51388],
  "temperature": 0.0, "avg_logprob": -0.2829961858244024, "compression_ratio": 1.7132075471698114,
  "no_speech_prob": 0.0045359134674072266}, {"id": 150, "seek": 58184, "start": 602.32,
  "end": 605.5600000000001, "text": " That''s too much for a two-man company to do.",
  "tokens": [51388, 663, 311, 886, 709, 337, 257, 732, 12, 1601, 2237, 281, 360, 13,
  51550], "temperature": 0.0, "avg_logprob": -0.2829961858244024, "compression_ratio":
  1.7132075471698114, "no_speech_prob": 0.0045359134674072266}, {"id": 151, "seek":
  60556, "start": 605.56, "end": 612.56, "text": " So yeah, we''re trying to really
  combine the best of breed in every area and create a cohesive", "tokens": [50364,
  407, 1338, 11, 321, 434, 1382, 281, 534, 10432, 264, 1151, 295, 18971, 294, 633,
  1859, 293, 1884, 257, 43025, 50714], "temperature": 0.0, "avg_logprob": -0.21462676308371803,
  "compression_ratio": 1.6090225563909775, "no_speech_prob": 0.08632315695285797},
  {"id": 152, "seek": 60556, "start": 612.56, "end": 617.28, "text": " system that
  just works out of the box quite well for a broad range of use cases.", "tokens":
  [50714, 1185, 300, 445, 1985, 484, 295, 264, 2424, 1596, 731, 337, 257, 4152, 3613,
  295, 764, 3331, 13, 50950], "temperature": 0.0, "avg_logprob": -0.21462676308371803,
  "compression_ratio": 1.6090225563909775, "no_speech_prob": 0.08632315695285797},
  {"id": 153, "seek": 60556, "start": 617.28, "end": 618.76, "text": " Oh yeah, that''s
  awesome.", "tokens": [50950, 876, 1338, 11, 300, 311, 3476, 13, 51024], "temperature":
  0.0, "avg_logprob": -0.21462676308371803, "compression_ratio": 1.6090225563909775,
  "no_speech_prob": 0.08632315695285797}, {"id": 154, "seek": 60556, "start": 618.76,
  "end": 625.16, "text": " And it''s also great to hear that you reuse open source
  software, you know, at least initially", "tokens": [51024, 400, 309, 311, 611, 869,
  281, 1568, 300, 291, 26225, 1269, 4009, 4722, 11, 291, 458, 11, 412, 1935, 9105,
  51344], "temperature": 0.0, "avg_logprob": -0.21462676308371803, "compression_ratio":
  1.6090225563909775, "no_speech_prob": 0.08632315695285797}, {"id": 155, "seek":
  60556, "start": 625.16, "end": 628.5999999999999, "text": " or maybe you can find
  two minutes, so to say.", "tokens": [51344, 420, 1310, 291, 393, 915, 732, 2077,
  11, 370, 281, 584, 13, 51516], "temperature": 0.0, "avg_logprob": -0.21462676308371803,
  "compression_ratio": 1.6090225563909775, "no_speech_prob": 0.08632315695285797},
  {"id": 156, "seek": 60556, "start": 628.5999999999999, "end": 633.68, "text": "
  But yeah, I mean, also that''s amazing because you can quickly kind of build your
  product", "tokens": [51516, 583, 1338, 11, 286, 914, 11, 611, 300, 311, 2243, 570,
  291, 393, 2661, 733, 295, 1322, 428, 1674, 51770], "temperature": 0.0, "avg_logprob":
  -0.21462676308371803, "compression_ratio": 1.6090225563909775, "no_speech_prob":
  0.08632315695285797}, {"id": 157, "seek": 63368, "start": 633.68, "end": 635.68,
  "text": " and focus on the goal.", "tokens": [50364, 293, 1879, 322, 264, 3387,
  13, 50464], "temperature": 0.0, "avg_logprob": -0.26846617519265353, "compression_ratio":
  1.5919282511210762, "no_speech_prob": 0.012865211814641953}, {"id": 158, "seek":
  63368, "start": 635.68, "end": 641.9599999999999, "text": " Yeah, and now that we
  approached this more kind of closely, can you actually describe what", "tokens":
  [50464, 865, 11, 293, 586, 300, 321, 17247, 341, 544, 733, 295, 8185, 11, 393, 291,
  767, 6786, 437, 50778], "temperature": 0.0, "avg_logprob": -0.26846617519265353,
  "compression_ratio": 1.5919282511210762, "no_speech_prob": 0.012865211814641953},
  {"id": 159, "seek": 63368, "start": 641.9599999999999, "end": 643.4799999999999,
  "text": " is your product today?", "tokens": [50778, 307, 428, 1674, 965, 30, 50854],
  "temperature": 0.0, "avg_logprob": -0.26846617519265353, "compression_ratio": 1.5919282511210762,
  "no_speech_prob": 0.012865211814641953}, {"id": 160, "seek": 63368, "start": 643.4799999999999,
  "end": 645.4, "text": " So as a client, what can I get?", "tokens": [50854, 407,
  382, 257, 6423, 11, 437, 393, 286, 483, 30, 50950], "temperature": 0.0, "avg_logprob":
  -0.26846617519265353, "compression_ratio": 1.5919282511210762, "no_speech_prob":
  0.012865211814641953}, {"id": 161, "seek": 63368, "start": 645.4, "end": 647.7199999999999,
  "text": " What can I, what kind of support you also provide?", "tokens": [50950,
  708, 393, 286, 11, 437, 733, 295, 1406, 291, 611, 2893, 30, 51066], "temperature":
  0.0, "avg_logprob": -0.26846617519265353, "compression_ratio": 1.5919282511210762,
  "no_speech_prob": 0.012865211814641953}, {"id": 162, "seek": 63368, "start": 647.7199999999999,
  "end": 650.52, "text": " But first, can you start with the product itself?", "tokens":
  [51066, 583, 700, 11, 393, 291, 722, 365, 264, 1674, 2564, 30, 51206], "temperature":
  0.0, "avg_logprob": -0.26846617519265353, "compression_ratio": 1.5919282511210762,
  "no_speech_prob": 0.012865211814641953}, {"id": 163, "seek": 63368, "start": 650.52,
  "end": 652.3199999999999, "text": " Yes.", "tokens": [51206, 1079, 13, 51296], "temperature":
  0.0, "avg_logprob": -0.26846617519265353, "compression_ratio": 1.5919282511210762,
  "no_speech_prob": 0.012865211814641953}, {"id": 164, "seek": 63368, "start": 652.3199999999999,
  "end": 658.24, "text": " So to describe it abstractly, and then I''ll explain very
  concretely what I mean.", "tokens": [51296, 407, 281, 6786, 309, 12649, 356, 11,
  293, 550, 286, 603, 2903, 588, 39481, 736, 437, 286, 914, 13, 51592], "temperature":
  0.0, "avg_logprob": -0.26846617519265353, "compression_ratio": 1.5919282511210762,
  "no_speech_prob": 0.012865211814641953}, {"id": 165, "seek": 65824, "start": 658.24,
  "end": 664.5600000000001, "text": " I would say that we''re a cloud platform as
  a service for text retrieval or text search.", "tokens": [50364, 286, 576, 584,
  300, 321, 434, 257, 4588, 3663, 382, 257, 2643, 337, 2487, 19817, 3337, 420, 2487,
  3164, 13, 50680], "temperature": 0.0, "avg_logprob": -0.1612650916689918, "compression_ratio":
  1.76, "no_speech_prob": 0.11757352203130722}, {"id": 166, "seek": 65824, "start":
  664.5600000000001, "end": 671.48, "text": " So the way it looks is we have two main
  APIs, one for indexing content and the other for", "tokens": [50680, 407, 264, 636,
  309, 1542, 307, 321, 362, 732, 2135, 21445, 11, 472, 337, 8186, 278, 2701, 293,
  264, 661, 337, 51026], "temperature": 0.0, "avg_logprob": -0.1612650916689918, "compression_ratio":
  1.76, "no_speech_prob": 0.11757352203130722}, {"id": 167, "seek": 65824, "start":
  671.48, "end": 673.24, "text": " running queries on the content.", "tokens": [51026,
  2614, 24109, 322, 264, 2701, 13, 51114], "temperature": 0.0, "avg_logprob": -0.1612650916689918,
  "compression_ratio": 1.76, "no_speech_prob": 0.11757352203130722}, {"id": 168, "seek":
  65824, "start": 673.24, "end": 677.4, "text": " So an organization would come and
  they would index a large amount of content.", "tokens": [51114, 407, 364, 4475,
  576, 808, 293, 436, 576, 8186, 257, 2416, 2372, 295, 2701, 13, 51322], "temperature":
  0.0, "avg_logprob": -0.1612650916689918, "compression_ratio": 1.76, "no_speech_prob":
  0.11757352203130722}, {"id": 169, "seek": 65824, "start": 677.4, "end": 682.6800000000001,
  "text": " They might index periodically or incrementally as well over time.", "tokens":
  [51322, 814, 1062, 8186, 38916, 420, 26200, 379, 382, 731, 670, 565, 13, 51586],
  "temperature": 0.0, "avg_logprob": -0.1612650916689918, "compression_ratio": 1.76,
  "no_speech_prob": 0.11757352203130722}, {"id": 170, "seek": 65824, "start": 682.6800000000001,
  "end": 687.64, "text": " And this would accrete in an index and then subsequently
  they would come and they would", "tokens": [51586, 400, 341, 576, 1317, 7600, 294,
  364, 8186, 293, 550, 26514, 436, 576, 808, 293, 436, 576, 51834], "temperature":
  0.0, "avg_logprob": -0.1612650916689918, "compression_ratio": 1.76, "no_speech_prob":
  0.11757352203130722}, {"id": 171, "seek": 68764, "start": 687.64, "end": 693.16,
  "text": " run generally natural language text queries against that corpus and we
  would return the", "tokens": [50364, 1190, 5101, 3303, 2856, 2487, 24109, 1970,
  300, 1181, 31624, 293, 321, 576, 2736, 264, 50640], "temperature": 0.0, "avg_logprob":
  -0.16679914961469935, "compression_ratio": 1.61864406779661, "no_speech_prob": 0.0009590925765223801},
  {"id": 172, "seek": 68764, "start": 693.16, "end": 695.4, "text": " best matches.",
  "tokens": [50640, 1151, 10676, 13, 50752], "temperature": 0.0, "avg_logprob": -0.16679914961469935,
  "compression_ratio": 1.61864406779661, "no_speech_prob": 0.0009590925765223801},
  {"id": 173, "seek": 68764, "start": 695.4, "end": 700.84, "text": " So what we actually
  provide and how that looks on our platform.", "tokens": [50752, 407, 437, 321, 767,
  2893, 293, 577, 300, 1542, 322, 527, 3663, 13, 51024], "temperature": 0.0, "avg_logprob":
  -0.16679914961469935, "compression_ratio": 1.61864406779661, "no_speech_prob": 0.0009590925765223801},
  {"id": 174, "seek": 68764, "start": 700.84, "end": 705.36, "text": " So we, you
  essentially, you know, you come and you sign up just the way you would sign", "tokens":
  [51024, 407, 321, 11, 291, 4476, 11, 291, 458, 11, 291, 808, 293, 291, 1465, 493,
  445, 264, 636, 291, 576, 1465, 51250], "temperature": 0.0, "avg_logprob": -0.16679914961469935,
  "compression_ratio": 1.61864406779661, "no_speech_prob": 0.0009590925765223801},
  {"id": 175, "seek": 68764, "start": 705.36, "end": 711.68, "text": " up for an AWS
  account, you''re dropped into an admin console.", "tokens": [51250, 493, 337, 364,
  17650, 2696, 11, 291, 434, 8119, 666, 364, 24236, 11076, 13, 51566], "temperature":
  0.0, "avg_logprob": -0.16679914961469935, "compression_ratio": 1.61864406779661,
  "no_speech_prob": 0.0009590925765223801}, {"id": 176, "seek": 68764, "start": 711.68,
  "end": 714.48, "text": " Everything you can do in the admin console can be done
  through APIs.", "tokens": [51566, 5471, 291, 393, 360, 294, 264, 24236, 11076, 393,
  312, 1096, 807, 21445, 13, 51706], "temperature": 0.0, "avg_logprob": -0.16679914961469935,
  "compression_ratio": 1.61864406779661, "no_speech_prob": 0.0009590925765223801},
  {"id": 177, "seek": 71448, "start": 714.48, "end": 717.88, "text": " We''re basically
  focused on again, a platform.", "tokens": [50364, 492, 434, 1936, 5178, 322, 797,
  11, 257, 3663, 13, 50534], "temperature": 0.0, "avg_logprob": -0.20046348571777345,
  "compression_ratio": 1.6676923076923076, "no_speech_prob": 0.13901077210903168},
  {"id": 178, "seek": 71448, "start": 717.88, "end": 720.8000000000001, "text": "
  So we''re accessible through GRPC and rest.", "tokens": [50534, 407, 321, 434, 9515,
  807, 10903, 12986, 293, 1472, 13, 50680], "temperature": 0.0, "avg_logprob": -0.20046348571777345,
  "compression_ratio": 1.6676923076923076, "no_speech_prob": 0.13901077210903168},
  {"id": 179, "seek": 71448, "start": 720.8000000000001, "end": 725.0, "text": " The
  platform, the console is basically to allow you to, you know, point and click and
  quickly", "tokens": [50680, 440, 3663, 11, 264, 11076, 307, 1936, 281, 2089, 291,
  281, 11, 291, 458, 11, 935, 293, 2052, 293, 2661, 50890], "temperature": 0.0, "avg_logprob":
  -0.20046348571777345, "compression_ratio": 1.6676923076923076, "no_speech_prob":
  0.13901077210903168}, {"id": 180, "seek": 71448, "start": 725.0, "end": 727.32,
  "text": " experiment and discover the value of the system.", "tokens": [50890, 5120,
  293, 4411, 264, 2158, 295, 264, 1185, 13, 51006], "temperature": 0.0, "avg_logprob":
  -0.20046348571777345, "compression_ratio": 1.6676923076923076, "no_speech_prob":
  0.13901077210903168}, {"id": 181, "seek": 71448, "start": 727.32, "end": 732.9200000000001,
  "text": " Because our vision was that within, within 15 to 30 minutes, someone from
  an organization", "tokens": [51006, 1436, 527, 5201, 390, 300, 1951, 11, 1951, 2119,
  281, 2217, 2077, 11, 1580, 490, 364, 4475, 51286], "temperature": 0.0, "avg_logprob":
  -0.20046348571777345, "compression_ratio": 1.6676923076923076, "no_speech_prob":
  0.13901077210903168}, {"id": 182, "seek": 71448, "start": 732.9200000000001, "end":
  736.32, "text": " should be able to come, drop their documents into the system and
  determine whether or not", "tokens": [51286, 820, 312, 1075, 281, 808, 11, 3270,
  641, 8512, 666, 264, 1185, 293, 6997, 1968, 420, 406, 51456], "temperature": 0.0,
  "avg_logprob": -0.20046348571777345, "compression_ratio": 1.6676923076923076, "no_speech_prob":
  0.13901077210903168}, {"id": 183, "seek": 71448, "start": 736.32, "end": 738.08,
  "text": " it''s even going to meet their needs.", "tokens": [51456, 309, 311, 754,
  516, 281, 1677, 641, 2203, 13, 51544], "temperature": 0.0, "avg_logprob": -0.20046348571777345,
  "compression_ratio": 1.6676923076923076, "no_speech_prob": 0.13901077210903168},
  {"id": 184, "seek": 71448, "start": 738.08, "end": 743.8000000000001, "text": "
  And then if it does, they can consult the documentation and learn how to use the
  APIs and get", "tokens": [51544, 400, 550, 498, 309, 775, 11, 436, 393, 7189, 264,
  14333, 293, 1466, 577, 281, 764, 264, 21445, 293, 483, 51830], "temperature": 0.0,
  "avg_logprob": -0.20046348571777345, "compression_ratio": 1.6676923076923076, "no_speech_prob":
  0.13901077210903168}, {"id": 185, "seek": 74380, "start": 743.8, "end": 745.64,
  "text": " a proper integration going.", "tokens": [50364, 257, 2296, 10980, 516,
  13, 50456], "temperature": 0.0, "avg_logprob": -0.17702918333165785, "compression_ratio":
  1.6074766355140186, "no_speech_prob": 0.0005752904107794166}, {"id": 186, "seek":
  74380, "start": 745.64, "end": 750.68, "text": " So we organize collections of documents
  into what are called corpora.", "tokens": [50456, 407, 321, 13859, 16641, 295, 8512,
  666, 437, 366, 1219, 6804, 64, 13, 50708], "temperature": 0.0, "avg_logprob": -0.17702918333165785,
  "compression_ratio": 1.6074766355140186, "no_speech_prob": 0.0005752904107794166},
  {"id": 187, "seek": 74380, "start": 750.68, "end": 754.24, "text": " So one corpus
  is essentially, it''s a customer defined entity.", "tokens": [50708, 407, 472, 1181,
  31624, 307, 4476, 11, 309, 311, 257, 5474, 7642, 13977, 13, 50886], "temperature":
  0.0, "avg_logprob": -0.17702918333165785, "compression_ratio": 1.6074766355140186,
  "no_speech_prob": 0.0005752904107794166}, {"id": 188, "seek": 74380, "start": 754.24,
  "end": 760.28, "text": " It groups related documents that they want to search together
  as a unit.", "tokens": [50886, 467, 3935, 4077, 8512, 300, 436, 528, 281, 3164,
  1214, 382, 257, 4985, 13, 51188], "temperature": 0.0, "avg_logprob": -0.17702918333165785,
  "compression_ratio": 1.6074766355140186, "no_speech_prob": 0.0005752904107794166},
  {"id": 189, "seek": 74380, "start": 760.28, "end": 767.0, "text": " We allow, you
  know, the customer to define any number of corpora, there''s limits depending",
  "tokens": [51188, 492, 2089, 11, 291, 458, 11, 264, 5474, 281, 6964, 604, 1230,
  295, 6804, 64, 11, 456, 311, 10406, 5413, 51524], "temperature": 0.0, "avg_logprob":
  -0.17702918333165785, "compression_ratio": 1.6074766355140186, "no_speech_prob":
  0.0005752904107794166}, {"id": 190, "seek": 74380, "start": 767.0, "end": 769.16,
  "text": " on the account type.", "tokens": [51524, 322, 264, 2696, 2010, 13, 51632],
  "temperature": 0.0, "avg_logprob": -0.17702918333165785, "compression_ratio": 1.6074766355140186,
  "no_speech_prob": 0.0005752904107794166}, {"id": 191, "seek": 76916, "start": 769.16,
  "end": 775.64, "text": " And then you can essentially drag and drop the documents
  into the web browser, into the", "tokens": [50364, 400, 550, 291, 393, 4476, 5286,
  293, 3270, 264, 8512, 666, 264, 3670, 11185, 11, 666, 264, 50688], "temperature":
  0.0, "avg_logprob": -0.21588961791992187, "compression_ratio": 1.7798507462686568,
  "no_speech_prob": 0.0041803279891610146}, {"id": 192, "seek": 76916, "start": 775.64,
  "end": 776.64, "text": " corpus upload.", "tokens": [50688, 1181, 31624, 6580, 13,
  50738], "temperature": 0.0, "avg_logprob": -0.21588961791992187, "compression_ratio":
  1.7798507462686568, "no_speech_prob": 0.0041803279891610146}, {"id": 193, "seek":
  76916, "start": 776.64, "end": 779.4399999999999, "text": " It''ll be, there''s
  about a seven minute latency.", "tokens": [50738, 467, 603, 312, 11, 456, 311, 466,
  257, 3407, 3456, 27043, 13, 50878], "temperature": 0.0, "avg_logprob": -0.21588961791992187,
  "compression_ratio": 1.7798507462686568, "no_speech_prob": 0.0041803279891610146},
  {"id": 194, "seek": 76916, "start": 779.4399999999999, "end": 780.76, "text": "
  And then you can start running queries.", "tokens": [50878, 400, 550, 291, 393,
  722, 2614, 24109, 13, 50944], "temperature": 0.0, "avg_logprob": -0.21588961791992187,
  "compression_ratio": 1.7798507462686568, "no_speech_prob": 0.0041803279891610146},
  {"id": 195, "seek": 76916, "start": 780.76, "end": 785.24, "text": " And when you
  run, we have a hosted UI that makes it easy to see the results kind of on", "tokens":
  [50944, 400, 562, 291, 1190, 11, 321, 362, 257, 19204, 15682, 300, 1669, 309, 1858,
  281, 536, 264, 3542, 733, 295, 322, 51168], "temperature": 0.0, "avg_logprob": -0.21588961791992187,
  "compression_ratio": 1.7798507462686568, "no_speech_prob": 0.0041803279891610146},
  {"id": 196, "seek": 76916, "start": 785.24, "end": 786.9599999999999, "text": "
  the spot in the browser.", "tokens": [51168, 264, 4008, 294, 264, 11185, 13, 51254],
  "temperature": 0.0, "avg_logprob": -0.21588961791992187, "compression_ratio": 1.7798507462686568,
  "no_speech_prob": 0.0041803279891610146}, {"id": 197, "seek": 76916, "start": 786.9599999999999,
  "end": 791.48, "text": " But when you run queries through our interface, you also
  have our, our, our API is, you also", "tokens": [51254, 583, 562, 291, 1190, 24109,
  807, 527, 9226, 11, 291, 611, 362, 527, 11, 527, 11, 527, 9362, 307, 11, 291, 611,
  51480], "temperature": 0.0, "avg_logprob": -0.21588961791992187, "compression_ratio":
  1.7798507462686568, "no_speech_prob": 0.0041803279891610146}, {"id": 198, "seek":
  76916, "start": 791.48, "end": 798.1999999999999, "text": " have the ability to
  run one query against multiple corpora and merge the results.", "tokens": [51480,
  362, 264, 3485, 281, 1190, 472, 14581, 1970, 3866, 1181, 79, 3252, 293, 22183, 264,
  3542, 13, 51816], "temperature": 0.0, "avg_logprob": -0.21588961791992187, "compression_ratio":
  1.7798507462686568, "no_speech_prob": 0.0041803279891610146}, {"id": 199, "seek":
  79820, "start": 798.2, "end": 805.6, "text": " So we also support the ability to
  attach metadata as your indexing content, attach metadata", "tokens": [50364, 407,
  321, 611, 1406, 264, 3485, 281, 5085, 26603, 382, 428, 8186, 278, 2701, 11, 5085,
  26603, 50734], "temperature": 0.0, "avg_logprob": -0.21361607638272373, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.0029648279305547476}, {"id": 200, "seek":
  79820, "start": 805.6, "end": 809.8000000000001, "text": " that then is returned
  to you in the search results.", "tokens": [50734, 300, 550, 307, 8752, 281, 291,
  294, 264, 3164, 3542, 13, 50944], "temperature": 0.0, "avg_logprob": -0.21361607638272373,
  "compression_ratio": 1.6784313725490196, "no_speech_prob": 0.0029648279305547476},
  {"id": 201, "seek": 79820, "start": 809.8000000000001, "end": 815.0400000000001,
  "text": " So that would allow you to, to join to let''s say another system on your
  end.", "tokens": [50944, 407, 300, 576, 2089, 291, 281, 11, 281, 3917, 281, 718,
  311, 584, 1071, 1185, 322, 428, 917, 13, 51206], "temperature": 0.0, "avg_logprob":
  -0.21361607638272373, "compression_ratio": 1.6784313725490196, "no_speech_prob":
  0.0029648279305547476}, {"id": 202, "seek": 79820, "start": 815.0400000000001, "end":
  818.0, "text": " But those are, those are some of the features that we provide.",
  "tokens": [51206, 583, 729, 366, 11, 729, 366, 512, 295, 264, 4122, 300, 321, 2893,
  13, 51354], "temperature": 0.0, "avg_logprob": -0.21361607638272373, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.0029648279305547476}, {"id": 203, "seek":
  79820, "start": 818.0, "end": 819.0, "text": " Yeah.", "tokens": [51354, 865, 13,
  51404], "temperature": 0.0, "avg_logprob": -0.21361607638272373, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.0029648279305547476}, {"id": 204, "seek":
  79820, "start": 819.0, "end": 821.84, "text": " So it sounds like it''s a self service
  system, right?", "tokens": [51404, 407, 309, 3263, 411, 309, 311, 257, 2698, 2643,
  1185, 11, 558, 30, 51546], "temperature": 0.0, "avg_logprob": -0.21361607638272373,
  "compression_ratio": 1.6784313725490196, "no_speech_prob": 0.0029648279305547476},
  {"id": 205, "seek": 79820, "start": 821.84, "end": 827.6800000000001, "text": "
  And so if I was a client of yours, I could like get a subscription trial subscription",
  "tokens": [51546, 400, 370, 498, 286, 390, 257, 6423, 295, 6342, 11, 286, 727, 411,
  483, 257, 17231, 7308, 17231, 51838], "temperature": 0.0, "avg_logprob": -0.21361607638272373,
  "compression_ratio": 1.6784313725490196, "no_speech_prob": 0.0029648279305547476},
  {"id": 206, "seek": 82768, "start": 827.68, "end": 832.16, "text": " maybe then
  upload my document corpus.", "tokens": [50364, 1310, 550, 6580, 452, 4166, 1181,
  31624, 13, 50588], "temperature": 0.0, "avg_logprob": -0.2156848714809225, "compression_ratio":
  1.524229074889868, "no_speech_prob": 0.0041611953638494015}, {"id": 207, "seek":
  82768, "start": 832.16, "end": 834.76, "text": " How big a corpus could I upload
  on a trial?", "tokens": [50588, 1012, 955, 257, 1181, 31624, 727, 286, 6580, 322,
  257, 7308, 30, 50718], "temperature": 0.0, "avg_logprob": -0.2156848714809225, "compression_ratio":
  1.524229074889868, "no_speech_prob": 0.0041611953638494015}, {"id": 208, "seek":
  82768, "start": 834.76, "end": 838.7199999999999, "text": " Do you have any limitation
  there at this point?", "tokens": [50718, 1144, 291, 362, 604, 27432, 456, 412, 341,
  935, 30, 50916], "temperature": 0.0, "avg_logprob": -0.2156848714809225, "compression_ratio":
  1.524229074889868, "no_speech_prob": 0.0041611953638494015}, {"id": 209, "seek":
  82768, "start": 838.7199999999999, "end": 843.9599999999999, "text": " So our general
  trial has been 15 megabytes of text.", "tokens": [50916, 407, 527, 2674, 7308, 575,
  668, 2119, 10816, 24538, 295, 2487, 13, 51178], "temperature": 0.0, "avg_logprob":
  -0.2156848714809225, "compression_ratio": 1.524229074889868, "no_speech_prob": 0.0041611953638494015},
  {"id": 210, "seek": 82768, "start": 843.9599999999999, "end": 846.3599999999999,
  "text": " And I''ll explain what that translates to.", "tokens": [51178, 400, 286,
  603, 2903, 437, 300, 28468, 281, 13, 51298], "temperature": 0.0, "avg_logprob":
  -0.2156848714809225, "compression_ratio": 1.524229074889868, "no_speech_prob": 0.0041611953638494015},
  {"id": 211, "seek": 82768, "start": 846.3599999999999, "end": 851.12, "text": "
  I was, I was, I was just working with another customer.", "tokens": [51298, 286,
  390, 11, 286, 390, 11, 286, 390, 445, 1364, 365, 1071, 5474, 13, 51536], "temperature":
  0.0, "avg_logprob": -0.2156848714809225, "compression_ratio": 1.524229074889868,
  "no_speech_prob": 0.0041611953638494015}, {"id": 212, "seek": 82768, "start": 851.12,
  "end": 855.88, "text": " And they had about one gigabyte of PDFs that we put into
  a corpus.", "tokens": [51536, 400, 436, 632, 466, 472, 8741, 34529, 295, 17752,
  82, 300, 321, 829, 666, 257, 1181, 31624, 13, 51774], "temperature": 0.0, "avg_logprob":
  -0.2156848714809225, "compression_ratio": 1.524229074889868, "no_speech_prob": 0.0041611953638494015},
  {"id": 213, "seek": 85588, "start": 855.88, "end": 859.52, "text": " And then that
  turned out to be about 48 megabytes of text.", "tokens": [50364, 400, 550, 300,
  3574, 484, 281, 312, 466, 11174, 10816, 24538, 295, 2487, 13, 50546], "temperature":
  0.0, "avg_logprob": -0.18534351607500496, "compression_ratio": 1.6091954022988506,
  "no_speech_prob": 0.000489726779051125}, {"id": 214, "seek": 85588, "start": 859.52,
  "end": 862.52, "text": " So the, the billing is by the actual extracted textual
  content.", "tokens": [50546, 407, 264, 11, 264, 35618, 307, 538, 264, 3539, 34086,
  2487, 901, 2701, 13, 50696], "temperature": 0.0, "avg_logprob": -0.18534351607500496,
  "compression_ratio": 1.6091954022988506, "no_speech_prob": 0.000489726779051125},
  {"id": 215, "seek": 85588, "start": 862.52, "end": 869.32, "text": " So 15 megabytes
  is actually a decent data set, several hundred documents you can imagine.", "tokens":
  [50696, 407, 2119, 10816, 24538, 307, 767, 257, 8681, 1412, 992, 11, 2940, 3262,
  8512, 291, 393, 3811, 13, 51036], "temperature": 0.0, "avg_logprob": -0.18534351607500496,
  "compression_ratio": 1.6091954022988506, "no_speech_prob": 0.000489726779051125},
  {"id": 216, "seek": 85588, "start": 869.32, "end": 873.76, "text": " So, but we
  have, we have plans that go much larger and we have customers that are indexing",
  "tokens": [51036, 407, 11, 457, 321, 362, 11, 321, 362, 5482, 300, 352, 709, 4833,
  293, 321, 362, 4581, 300, 366, 8186, 278, 51258], "temperature": 0.0, "avg_logprob":
  -0.18534351607500496, "compression_ratio": 1.6091954022988506, "no_speech_prob":
  0.000489726779051125}, {"id": 217, "seek": 85588, "start": 873.76, "end": 874.76,
  "text": " far more data.", "tokens": [51258, 1400, 544, 1412, 13, 51308], "temperature":
  0.0, "avg_logprob": -0.18534351607500496, "compression_ratio": 1.6091954022988506,
  "no_speech_prob": 0.000489726779051125}, {"id": 218, "seek": 85588, "start": 874.76,
  "end": 877.12, "text": " Yeah, yeah, sounds great.", "tokens": [51308, 865, 11,
  1338, 11, 3263, 869, 13, 51426], "temperature": 0.0, "avg_logprob": -0.18534351607500496,
  "compression_ratio": 1.6091954022988506, "no_speech_prob": 0.000489726779051125},
  {"id": 219, "seek": 85588, "start": 877.12, "end": 878.32, "text": " And then what
  happens next?", "tokens": [51426, 400, 550, 437, 2314, 958, 30, 51486], "temperature":
  0.0, "avg_logprob": -0.18534351607500496, "compression_ratio": 1.6091954022988506,
  "no_speech_prob": 0.000489726779051125}, {"id": 220, "seek": 85588, "start": 878.32,
  "end": 879.32, "text": " So let''s say I''m happy.", "tokens": [51486, 407, 718,
  311, 584, 286, 478, 2055, 13, 51536], "temperature": 0.0, "avg_logprob": -0.18534351607500496,
  "compression_ratio": 1.6091954022988506, "no_speech_prob": 0.000489726779051125},
  {"id": 221, "seek": 85588, "start": 879.32, "end": 881.04, "text": " I want to move
  forward.", "tokens": [51536, 286, 528, 281, 1286, 2128, 13, 51622], "temperature":
  0.0, "avg_logprob": -0.18534351607500496, "compression_ratio": 1.6091954022988506,
  "no_speech_prob": 0.000489726779051125}, {"id": 222, "seek": 88104, "start": 881.04,
  "end": 886.64, "text": " Now you said that there are APIs that I can start kind
  of introducing inside my prototype", "tokens": [50364, 823, 291, 848, 300, 456,
  366, 21445, 300, 286, 393, 722, 733, 295, 15424, 1854, 452, 19475, 50644], "temperature":
  0.0, "avg_logprob": -0.2055803680419922, "compression_ratio": 1.5, "no_speech_prob":
  0.0828024297952652}, {"id": 223, "seek": 88104, "start": 886.64, "end": 888.64,
  "text": " or my existing back end.", "tokens": [50644, 420, 452, 6741, 646, 917,
  13, 50744], "temperature": 0.0, "avg_logprob": -0.2055803680419922, "compression_ratio":
  1.5, "no_speech_prob": 0.0828024297952652}, {"id": 224, "seek": 88104, "start":
  888.64, "end": 889.64, "text": " Is that right?", "tokens": [50744, 1119, 300, 558,
  30, 50794], "temperature": 0.0, "avg_logprob": -0.2055803680419922, "compression_ratio":
  1.5, "no_speech_prob": 0.0828024297952652}, {"id": 225, "seek": 88104, "start":
  889.64, "end": 891.16, "text": " Yeah, that''s right.", "tokens": [50794, 865, 11,
  300, 311, 558, 13, 50870], "temperature": 0.0, "avg_logprob": -0.2055803680419922,
  "compression_ratio": 1.5, "no_speech_prob": 0.0828024297952652}, {"id": 226, "seek":
  88104, "start": 891.16, "end": 897.52, "text": " So we, we support primarily we
  promote a gRPC interface because it''s high performance", "tokens": [50870, 407,
  321, 11, 321, 1406, 10029, 321, 9773, 257, 290, 49, 12986, 9226, 570, 309, 311,
  1090, 3389, 51188], "temperature": 0.0, "avg_logprob": -0.2055803680419922, "compression_ratio":
  1.5, "no_speech_prob": 0.0828024297952652}, {"id": 227, "seek": 88104, "start":
  897.52, "end": 898.52, "text": " low latency.", "tokens": [51188, 2295, 27043, 13,
  51238], "temperature": 0.0, "avg_logprob": -0.2055803680419922, "compression_ratio":
  1.5, "no_speech_prob": 0.0828024297952652}, {"id": 228, "seek": 88104, "start":
  898.52, "end": 901.04, "text": " We also do have a rest interface.", "tokens": [51238,
  492, 611, 360, 362, 257, 1472, 9226, 13, 51364], "temperature": 0.0, "avg_logprob":
  -0.2055803680419922, "compression_ratio": 1.5, "no_speech_prob": 0.0828024297952652},
  {"id": 229, "seek": 88104, "start": 901.04, "end": 904.36, "text": " We have fully
  authenticated APIs.", "tokens": [51364, 492, 362, 4498, 9214, 3587, 21445, 13, 51530],
  "temperature": 0.0, "avg_logprob": -0.2055803680419922, "compression_ratio": 1.5,
  "no_speech_prob": 0.0828024297952652}, {"id": 230, "seek": 88104, "start": 904.36,
  "end": 907.76, "text": " So we use OAuth 2.0 that standard.", "tokens": [51530,
  407, 321, 764, 48424, 2910, 568, 13, 15, 300, 3832, 13, 51700], "temperature": 0.0,
  "avg_logprob": -0.2055803680419922, "compression_ratio": 1.5, "no_speech_prob":
  0.0828024297952652}, {"id": 231, "seek": 90776, "start": 907.76, "end": 913.68,
  "text": " So you would give credentials to your servers and they would use those
  credentials to establish", "tokens": [50364, 407, 291, 576, 976, 27404, 281, 428,
  15909, 293, 436, 576, 764, 729, 27404, 281, 8327, 50660], "temperature": 0.0, "avg_logprob":
  -0.24384072449830202, "compression_ratio": 1.6139705882352942, "no_speech_prob":
  0.04690662771463394}, {"id": 232, "seek": 90776, "start": 913.68, "end": 919.04,
  "text": " an authenticated session with the platform and then run, run queries for
  you at a very", "tokens": [50660, 364, 9214, 3587, 5481, 365, 264, 3663, 293, 550,
  1190, 11, 1190, 24109, 337, 291, 412, 257, 588, 50928], "temperature": 0.0, "avg_logprob":
  -0.24384072449830202, "compression_ratio": 1.6139705882352942, "no_speech_prob":
  0.04690662771463394}, {"id": 233, "seek": 90776, "start": 919.04, "end": 921.04,
  "text": " high rate.", "tokens": [50928, 1090, 3314, 13, 51028], "temperature":
  0.0, "avg_logprob": -0.24384072449830202, "compression_ratio": 1.6139705882352942,
  "no_speech_prob": 0.04690662771463394}, {"id": 234, "seek": 90776, "start": 921.04,
  "end": 922.52, "text": " We scale horizontally.", "tokens": [51028, 492, 4373, 33796,
  13, 51102], "temperature": 0.0, "avg_logprob": -0.24384072449830202, "compression_ratio":
  1.6139705882352942, "no_speech_prob": 0.04690662771463394}, {"id": 235, "seek":
  90776, "start": 922.52, "end": 927.28, "text": " We can go up to hundreds of QPS,
  though we haven''t had a customer that''s needed such", "tokens": [51102, 492, 393,
  352, 493, 281, 6779, 295, 1249, 6273, 11, 1673, 321, 2378, 380, 632, 257, 5474,
  300, 311, 2978, 1270, 51340], "temperature": 0.0, "avg_logprob": -0.24384072449830202,
  "compression_ratio": 1.6139705882352942, "no_speech_prob": 0.04690662771463394},
  {"id": 236, "seek": 90776, "start": 927.28, "end": 929.92, "text": " a high rate,
  but we''re capable of that.", "tokens": [51340, 257, 1090, 3314, 11, 457, 321, 434,
  8189, 295, 300, 13, 51472], "temperature": 0.0, "avg_logprob": -0.24384072449830202,
  "compression_ratio": 1.6139705882352942, "no_speech_prob": 0.04690662771463394},
  {"id": 237, "seek": 90776, "start": 929.92, "end": 930.92, "text": " Yeah, yeah.",
  "tokens": [51472, 865, 11, 1338, 13, 51522], "temperature": 0.0, "avg_logprob":
  -0.24384072449830202, "compression_ratio": 1.6139705882352942, "no_speech_prob":
  0.04690662771463394}, {"id": 238, "seek": 90776, "start": 930.92, "end": 937.72,
  "text": " And you also mentioned that you maintain certain like SLA guarantees like
  P99 latency", "tokens": [51522, 400, 291, 611, 2835, 300, 291, 6909, 1629, 411,
  318, 11435, 32567, 411, 430, 8494, 27043, 51862], "temperature": 0.0, "avg_logprob":
  -0.24384072449830202, "compression_ratio": 1.6139705882352942, "no_speech_prob":
  0.04690662771463394}, {"id": 239, "seek": 93772, "start": 937.72, "end": 944.96,
  "text": " can you speak a bit about that and also like how much of that accounts
  for client need", "tokens": [50364, 393, 291, 1710, 257, 857, 466, 300, 293, 611,
  411, 577, 709, 295, 300, 9402, 337, 6423, 643, 50726], "temperature": 0.0, "avg_logprob":
  -0.24096171752266263, "compression_ratio": 1.5541125541125542, "no_speech_prob":
  0.0018748895963653922}, {"id": 240, "seek": 93772, "start": 944.96, "end": 947.84,
  "text": " versus what you are building for the future.", "tokens": [50726, 5717,
  437, 291, 366, 2390, 337, 264, 2027, 13, 50870], "temperature": 0.0, "avg_logprob":
  -0.24096171752266263, "compression_ratio": 1.5541125541125542, "no_speech_prob":
  0.0018748895963653922}, {"id": 241, "seek": 93772, "start": 947.84, "end": 950.8000000000001,
  "text": " And this is a good question.", "tokens": [50870, 400, 341, 307, 257, 665,
  1168, 13, 51018], "temperature": 0.0, "avg_logprob": -0.24096171752266263, "compression_ratio":
  1.5541125541125542, "no_speech_prob": 0.0018748895963653922}, {"id": 242, "seek":
  93772, "start": 950.8000000000001, "end": 957.1600000000001, "text": " So in terms
  of client need, we really haven''t had any client that''s required anything better",
  "tokens": [51018, 407, 294, 2115, 295, 6423, 643, 11, 321, 534, 2378, 380, 632,
  604, 6423, 300, 311, 4739, 1340, 1101, 51336], "temperature": 0.0, "avg_logprob":
  -0.24096171752266263, "compression_ratio": 1.5541125541125542, "no_speech_prob":
  0.0018748895963653922}, {"id": 243, "seek": 93772, "start": 957.1600000000001, "end":
  960.64, "text": " than 200 milliseconds.", "tokens": [51336, 813, 2331, 34184, 13,
  51510], "temperature": 0.0, "avg_logprob": -0.24096171752266263, "compression_ratio":
  1.5541125541125542, "no_speech_prob": 0.0018748895963653922}, {"id": 244, "seek":
  93772, "start": 960.64, "end": 963.36, "text": " Now there''s a potential client
  that we''re working with.", "tokens": [51510, 823, 456, 311, 257, 3995, 6423, 300,
  321, 434, 1364, 365, 13, 51646], "temperature": 0.0, "avg_logprob": -0.24096171752266263,
  "compression_ratio": 1.5541125541125542, "no_speech_prob": 0.0018748895963653922},
  {"id": 245, "seek": 93772, "start": 963.36, "end": 965.24, "text": " They''re not
  yet acclaimed.", "tokens": [51646, 814, 434, 406, 1939, 1317, 22642, 13, 51740],
  "temperature": 0.0, "avg_logprob": -0.24096171752266263, "compression_ratio": 1.5541125541125542,
  "no_speech_prob": 0.0018748895963653922}, {"id": 246, "seek": 96524, "start": 965.24,
  "end": 973.72, "text": " They''re looking for more like 50 to 60 milliseconds because
  essentially the look up into our system", "tokens": [50364, 814, 434, 1237, 337,
  544, 411, 2625, 281, 4060, 34184, 570, 4476, 264, 574, 493, 666, 527, 1185, 50788],
  "temperature": 0.0, "avg_logprob": -0.17719637883173955, "compression_ratio": 1.490990990990991,
  "no_speech_prob": 0.005780704785138369}, {"id": 247, "seek": 96524, "start": 973.72,
  "end": 977.88, "text": " is only one part of their overall request handling process.",
  "tokens": [50788, 307, 787, 472, 644, 295, 641, 4787, 5308, 13175, 1399, 13, 50996],
  "temperature": 0.0, "avg_logprob": -0.17719637883173955, "compression_ratio": 1.490990990990991,
  "no_speech_prob": 0.005780704785138369}, {"id": 248, "seek": 96524, "start": 977.88,
  "end": 980.04, "text": " So they have a much tighter budget.", "tokens": [50996,
  407, 436, 362, 257, 709, 30443, 4706, 13, 51104], "temperature": 0.0, "avg_logprob":
  -0.17719637883173955, "compression_ratio": 1.490990990990991, "no_speech_prob":
  0.005780704785138369}, {"id": 249, "seek": 96524, "start": 980.04, "end": 984.04,
  "text": " In practice, what we''re seeing on our platform for our customers today
  aggregated over", "tokens": [51104, 682, 3124, 11, 437, 321, 434, 2577, 322, 527,
  3663, 337, 527, 4581, 965, 16743, 770, 670, 51304], "temperature": 0.0, "avg_logprob":
  -0.17719637883173955, "compression_ratio": 1.490990990990991, "no_speech_prob":
  0.005780704785138369}, {"id": 250, "seek": 96524, "start": 984.04, "end": 988.76,
  "text": " all queries is a P99 of around 130 milliseconds.", "tokens": [51304, 439,
  24109, 307, 257, 430, 8494, 295, 926, 19966, 34184, 13, 51540], "temperature": 0.0,
  "avg_logprob": -0.17719637883173955, "compression_ratio": 1.490990990990991, "no_speech_prob":
  0.005780704785138369}, {"id": 251, "seek": 98876, "start": 988.76, "end": 991.92,
  "text": " Our P50 is about 60 milliseconds.", "tokens": [50364, 2621, 430, 2803,
  307, 466, 4060, 34184, 13, 50522], "temperature": 0.0, "avg_logprob": -0.14299837180546351,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.015431715175509453},
  {"id": 252, "seek": 98876, "start": 991.92, "end": 995.8, "text": " And this has
  been sufficient for our customers.", "tokens": [50522, 400, 341, 575, 668, 11563,
  337, 527, 4581, 13, 50716], "temperature": 0.0, "avg_logprob": -0.14299837180546351,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.015431715175509453},
  {"id": 253, "seek": 98876, "start": 995.8, "end": 1001.4399999999999, "text": "
  For customers that have tighter requirements, we actually have many different ways
  to address", "tokens": [50716, 1171, 4581, 300, 362, 30443, 7728, 11, 321, 767,
  362, 867, 819, 2098, 281, 2985, 50998], "temperature": 0.0, "avg_logprob": -0.14299837180546351,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.015431715175509453},
  {"id": 254, "seek": 98876, "start": 1001.4399999999999, "end": 1002.4399999999999,
  "text": " it.", "tokens": [50998, 309, 13, 51048], "temperature": 0.0, "avg_logprob":
  -0.14299837180546351, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.015431715175509453}, {"id": 255, "seek": 98876, "start": 1002.4399999999999, "end":
  1004.56, "text": " So actually the main latency is not from the vector database.",
  "tokens": [51048, 407, 767, 264, 2135, 27043, 307, 406, 490, 264, 8062, 8149, 13,
  51154], "temperature": 0.0, "avg_logprob": -0.14299837180546351, "compression_ratio":
  1.6840148698884758, "no_speech_prob": 0.015431715175509453}, {"id": 256, "seek":
  98876, "start": 1004.56, "end": 1006.88, "text": " The vector database is generally
  quite fast.", "tokens": [51154, 440, 8062, 8149, 307, 5101, 1596, 2370, 13, 51270],
  "temperature": 0.0, "avg_logprob": -0.14299837180546351, "compression_ratio": 1.6840148698884758,
  "no_speech_prob": 0.015431715175509453}, {"id": 257, "seek": 98876, "start": 1006.88,
  "end": 1009.3199999999999, "text": " It''s the neural network that has to do the
  text encoding.", "tokens": [51270, 467, 311, 264, 18161, 3209, 300, 575, 281, 360,
  264, 2487, 43430, 13, 51392], "temperature": 0.0, "avg_logprob": -0.14299837180546351,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.015431715175509453},
  {"id": 258, "seek": 98876, "start": 1009.3199999999999, "end": 1011.52, "text":
  " That''s the bottleneck.", "tokens": [51392, 663, 311, 264, 44641, 547, 13, 51502],
  "temperature": 0.0, "avg_logprob": -0.14299837180546351, "compression_ratio": 1.6840148698884758,
  "no_speech_prob": 0.015431715175509453}, {"id": 259, "seek": 98876, "start": 1011.52,
  "end": 1018.4399999999999, "text": " So we have the ability to set up dedicated
  pools of encoders, neural networks that do", "tokens": [51502, 407, 321, 362, 264,
  3485, 281, 992, 493, 8374, 28688, 295, 2058, 378, 433, 11, 18161, 9590, 300, 360,
  51848], "temperature": 0.0, "avg_logprob": -0.14299837180546351, "compression_ratio":
  1.6840148698884758, "no_speech_prob": 0.015431715175509453}, {"id": 260, "seek":
  101844, "start": 1018.44, "end": 1021.2, "text": " this encoding of four customers.",
  "tokens": [50364, 341, 43430, 295, 1451, 4581, 13, 50502], "temperature": 0.0, "avg_logprob":
  -0.2530548725653132, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.011765317991375923}, {"id": 261, "seek": 101844, "start": 1021.2, "end": 1028.48,
  "text": " So we scale and we''re cost efficient by sharing the pool across all customers.",
  "tokens": [50502, 407, 321, 4373, 293, 321, 434, 2063, 7148, 538, 5414, 264, 7005,
  2108, 439, 4581, 13, 50866], "temperature": 0.0, "avg_logprob": -0.2530548725653132,
  "compression_ratio": 1.6153846153846154, "no_speech_prob": 0.011765317991375923},
  {"id": 262, "seek": 101844, "start": 1028.48, "end": 1032.1200000000001, "text":
  " But for customers that have very stringent needs, we can set up dedicated pools
  for them.", "tokens": [50866, 583, 337, 4581, 300, 362, 588, 6798, 317, 2203, 11,
  321, 393, 992, 493, 8374, 28688, 337, 552, 13, 51048], "temperature": 0.0, "avg_logprob":
  -0.2530548725653132, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.011765317991375923}, {"id": 263, "seek": 101844, "start": 1032.1200000000001,
  "end": 1039.64, "text": " But even when you go, let''s say single customer, single
  node, maybe GPU node, there are still", "tokens": [51048, 583, 754, 562, 291, 352,
  11, 718, 311, 584, 2167, 5474, 11, 2167, 9984, 11, 1310, 18407, 9984, 11, 456, 366,
  920, 51424], "temperature": 0.0, "avg_logprob": -0.2530548725653132, "compression_ratio":
  1.6153846153846154, "no_speech_prob": 0.011765317991375923}, {"id": 264, "seek":
  101844, "start": 1039.64, "end": 1042.96, "text": " theoretical boundary to how
  fast it can be.", "tokens": [51424, 20864, 12866, 281, 577, 2370, 309, 393, 312,
  13, 51590], "temperature": 0.0, "avg_logprob": -0.2530548725653132, "compression_ratio":
  1.6153846153846154, "no_speech_prob": 0.011765317991375923}, {"id": 265, "seek":
  101844, "start": 1042.96, "end": 1048.3600000000001, "text": " Let''s say if I take
  an off-the-shelf birth model, and if I throw 768 dimensions,", "tokens": [51590,
  961, 311, 584, 498, 286, 747, 364, 766, 12, 3322, 12, 46626, 3965, 2316, 11, 293,
  498, 286, 3507, 1614, 27102, 12819, 11, 51860], "temperature": 0.0, "avg_logprob":
  -0.2530548725653132, "compression_ratio": 1.6153846153846154, "no_speech_prob":
  0.011765317991375923}, {"id": 266, "seek": 104836, "start": 1048.36, "end": 1050.6799999999998,
  "text": " what''s going to happen?", "tokens": [50364, 437, 311, 516, 281, 1051,
  30, 50480], "temperature": 0.0, "avg_logprob": -0.32399056174538354, "compression_ratio":
  1.5757575757575757, "no_speech_prob": 0.022683139890432358}, {"id": 267, "seek":
  104836, "start": 1050.6799999999998, "end": 1054.04, "text": " How can I fine tune
  it on the speed size?", "tokens": [50480, 1012, 393, 286, 2489, 10864, 309, 322,
  264, 3073, 2744, 30, 50648], "temperature": 0.0, "avg_logprob": -0.32399056174538354,
  "compression_ratio": 1.5757575757575757, "no_speech_prob": 0.022683139890432358},
  {"id": 268, "seek": 104836, "start": 1054.04, "end": 1059.28, "text": " Yeah, well,
  let me address two things that you said there.", "tokens": [50648, 865, 11, 731,
  11, 718, 385, 2985, 732, 721, 300, 291, 848, 456, 13, 50910], "temperature": 0.0,
  "avg_logprob": -0.32399056174538354, "compression_ratio": 1.5757575757575757, "no_speech_prob":
  0.022683139890432358}, {"id": 269, "seek": 104836, "start": 1059.28, "end": 1065.6799999999998,
  "text": " So the off-the-shelf birth model is a very common approach that many companies
  are trying", "tokens": [50910, 407, 264, 766, 12, 3322, 12, 46626, 3965, 2316, 307,
  257, 588, 2689, 3109, 300, 867, 3431, 366, 1382, 51230], "temperature": 0.0, "avg_logprob":
  -0.32399056174538354, "compression_ratio": 1.5757575757575757, "no_speech_prob":
  0.022683139890432358}, {"id": 270, "seek": 104836, "start": 1065.6799999999998,
  "end": 1066.84, "text": " to productionize NLP.", "tokens": [51230, 281, 4265, 1125,
  426, 45196, 13, 51288], "temperature": 0.0, "avg_logprob": -0.32399056174538354,
  "compression_ratio": 1.5757575757575757, "no_speech_prob": 0.022683139890432358},
  {"id": 271, "seek": 104836, "start": 1066.84, "end": 1070.08, "text": " They use
  it because birth has a phenomenal accuracy.", "tokens": [51288, 814, 764, 309, 570,
  3965, 575, 257, 17778, 14170, 13, 51450], "temperature": 0.0, "avg_logprob": -0.32399056174538354,
  "compression_ratio": 1.5757575757575757, "no_speech_prob": 0.022683139890432358},
  {"id": 272, "seek": 104836, "start": 1070.08, "end": 1072.32, "text": " You fine
  tune it with a little bit of data.", "tokens": [51450, 509, 2489, 10864, 309, 365,
  257, 707, 857, 295, 1412, 13, 51562], "temperature": 0.0, "avg_logprob": -0.32399056174538354,
  "compression_ratio": 1.5757575757575757, "no_speech_prob": 0.022683139890432358},
  {"id": 273, "seek": 104836, "start": 1072.32, "end": 1076.6, "text": " And everyone
  always hits the same problem that is very difficult to productionize.", "tokens":
  [51562, 400, 1518, 1009, 8664, 264, 912, 1154, 300, 307, 588, 2252, 281, 4265, 1125,
  13, 51776], "temperature": 0.0, "avg_logprob": -0.32399056174538354, "compression_ratio":
  1.5757575757575757, "no_speech_prob": 0.022683139890432358}, {"id": 274, "seek":
  107660, "start": 1076.6, "end": 1082.36, "text": " And even at a place like Google,
  they didn''t productionize birth.", "tokens": [50364, 400, 754, 412, 257, 1081,
  411, 3329, 11, 436, 994, 380, 4265, 1125, 3965, 13, 50652], "temperature": 0.0,
  "avg_logprob": -0.18467098016005296, "compression_ratio": 1.6653061224489796, "no_speech_prob":
  0.006023973226547241}, {"id": 275, "seek": 107660, "start": 1082.36, "end": 1084.84,
  "text": " They had to distill birth and productionize it.", "tokens": [50652, 814,
  632, 281, 42923, 3965, 293, 4265, 1125, 309, 13, 50776], "temperature": 0.0, "avg_logprob":
  -0.18467098016005296, "compression_ratio": 1.6653061224489796, "no_speech_prob":
  0.006023973226547241}, {"id": 276, "seek": 107660, "start": 1084.84, "end": 1088.52,
  "text": " And distillation requires a lot of expertise.", "tokens": [50776, 400,
  42923, 399, 7029, 257, 688, 295, 11769, 13, 50960], "temperature": 0.0, "avg_logprob":
  -0.18467098016005296, "compression_ratio": 1.6653061224489796, "no_speech_prob":
  0.006023973226547241}, {"id": 277, "seek": 107660, "start": 1088.52, "end": 1092.52,
  "text": " It''s out of the reach, I think, of most companies.", "tokens": [50960,
  467, 311, 484, 295, 264, 2524, 11, 286, 519, 11, 295, 881, 3431, 13, 51160], "temperature":
  0.0, "avg_logprob": -0.18467098016005296, "compression_ratio": 1.6653061224489796,
  "no_speech_prob": 0.006023973226547241}, {"id": 278, "seek": 107660, "start": 1092.52,
  "end": 1099.6399999999999, "text": " So as good as the results look in a staging
  environment, that''s not really a practical", "tokens": [51160, 407, 382, 665, 382,
  264, 3542, 574, 294, 257, 41085, 2823, 11, 300, 311, 406, 534, 257, 8496, 51516],
  "temperature": 0.0, "avg_logprob": -0.18467098016005296, "compression_ratio": 1.6653061224489796,
  "no_speech_prob": 0.006023973226547241}, {"id": 279, "seek": 107660, "start": 1099.6399999999999,
  "end": 1100.6399999999999, "text": " to productionize that.", "tokens": [51516,
  281, 4265, 1125, 300, 13, 51566], "temperature": 0.0, "avg_logprob": -0.18467098016005296,
  "compression_ratio": 1.6653061224489796, "no_speech_prob": 0.006023973226547241},
  {"id": 280, "seek": 107660, "start": 1100.6399999999999, "end": 1105.3999999999999,
  "text": " And that comes back to the original point that we tried to make the right
  choices where", "tokens": [51566, 400, 300, 1487, 646, 281, 264, 3380, 935, 300,
  321, 3031, 281, 652, 264, 558, 7994, 689, 51804], "temperature": 0.0, "avg_logprob":
  -0.18467098016005296, "compression_ratio": 1.6653061224489796, "no_speech_prob":
  0.006023973226547241}, {"id": 281, "seek": 110540, "start": 1105.4, "end": 1108.96,
  "text": " if we were deploying birth, either it would be enormously expensive for
  us because we''d", "tokens": [50364, 498, 321, 645, 34198, 3965, 11, 2139, 309,
  576, 312, 39669, 5124, 337, 505, 570, 321, 1116, 50542], "temperature": 0.0, "avg_logprob":
  -0.24159034480893515, "compression_ratio": 1.6495176848874598, "no_speech_prob":
  0.0007520999060943723}, {"id": 282, "seek": 110540, "start": 1108.96, "end": 1114.88,
  "text": " have to be using GPU instances or TPU instances, or we would have very
  high latencies.", "tokens": [50542, 362, 281, 312, 1228, 18407, 14519, 420, 314,
  8115, 14519, 11, 420, 321, 576, 362, 588, 1090, 4465, 6464, 13, 50838], "temperature":
  0.0, "avg_logprob": -0.24159034480893515, "compression_ratio": 1.6495176848874598,
  "no_speech_prob": 0.0007520999060943723}, {"id": 283, "seek": 110540, "start": 1114.88,
  "end": 1119.0400000000002, "text": " So we have a model that produces similar performance,
  but it runs much faster.", "tokens": [50838, 407, 321, 362, 257, 2316, 300, 14725,
  2531, 3389, 11, 457, 309, 6676, 709, 4663, 13, 51046], "temperature": 0.0, "avg_logprob":
  -0.24159034480893515, "compression_ratio": 1.6495176848874598, "no_speech_prob":
  0.0007520999060943723}, {"id": 284, "seek": 110540, "start": 1119.0400000000002,
  "end": 1121.68, "text": " It''s still transformer-based.", "tokens": [51046, 467,
  311, 920, 31782, 12, 6032, 13, 51178], "temperature": 0.0, "avg_logprob": -0.24159034480893515,
  "compression_ratio": 1.6495176848874598, "no_speech_prob": 0.0007520999060943723},
  {"id": 285, "seek": 110540, "start": 1121.68, "end": 1125.6000000000001, "text":
  " Coming to your second point, I think your main question, your original question,
  was actually", "tokens": [51178, 12473, 281, 428, 1150, 935, 11, 286, 519, 428,
  2135, 1168, 11, 428, 3380, 1168, 11, 390, 767, 51374], "temperature": 0.0, "avg_logprob":
  -0.24159034480893515, "compression_ratio": 1.6495176848874598, "no_speech_prob":
  0.0007520999060943723}, {"id": 286, "seek": 110540, "start": 1125.6000000000001,
  "end": 1129.96, "text": " what''s the theoretical limit of performance that we can
  achieve in terms of are you asking", "tokens": [51374, 437, 311, 264, 20864, 4948,
  295, 3389, 300, 321, 393, 4584, 294, 2115, 295, 366, 291, 3365, 51592], "temperature":
  0.0, "avg_logprob": -0.24159034480893515, "compression_ratio": 1.6495176848874598,
  "no_speech_prob": 0.0007520999060943723}, {"id": 287, "seek": 110540, "start": 1129.96,
  "end": 1131.68, "text": " from a latency perspective?", "tokens": [51592, 490, 257,
  27043, 4585, 30, 51678], "temperature": 0.0, "avg_logprob": -0.24159034480893515,
  "compression_ratio": 1.6495176848874598, "no_speech_prob": 0.0007520999060943723},
  {"id": 288, "seek": 110540, "start": 1131.68, "end": 1133.92, "text": " Yeah, a
  latency.", "tokens": [51678, 865, 11, 257, 27043, 13, 51790], "temperature": 0.0,
  "avg_logprob": -0.24159034480893515, "compression_ratio": 1.6495176848874598, "no_speech_prob":
  0.0007520999060943723}, {"id": 289, "seek": 113392, "start": 1133.92, "end": 1138.76,
  "text": " So I''ll say this.", "tokens": [50364, 407, 286, 603, 584, 341, 13, 50606],
  "temperature": 0.0, "avg_logprob": -0.22485659672663763, "compression_ratio": 1.3526011560693643,
  "no_speech_prob": 0.007748408708721399}, {"id": 290, "seek": 113392, "start": 1138.76,
  "end": 1146.8000000000002, "text": " When it comes to the vector database, you probably
  know this better than I do.", "tokens": [50606, 1133, 309, 1487, 281, 264, 8062,
  8149, 11, 291, 1391, 458, 341, 1101, 813, 286, 360, 13, 51008], "temperature": 0.0,
  "avg_logprob": -0.22485659672663763, "compression_ratio": 1.3526011560693643, "no_speech_prob":
  0.007748408708721399}, {"id": 291, "seek": 113392, "start": 1146.8000000000002,
  "end": 1159.1200000000001, "text": " If it''s indexed and quantized correctly on
  our last stuff, even running on CPUs, you", "tokens": [51008, 759, 309, 311, 8186,
  292, 293, 4426, 1602, 8944, 322, 527, 1036, 1507, 11, 754, 2614, 322, 13199, 82,
  11, 291, 51624], "temperature": 0.0, "avg_logprob": -0.22485659672663763, "compression_ratio":
  1.3526011560693643, "no_speech_prob": 0.007748408708721399}, {"id": 292, "seek":
  113392, "start": 1159.1200000000001, "end": 1162.6000000000001, "text": " can get
  down to three, four milliseconds of latency.", "tokens": [51624, 393, 483, 760,
  281, 1045, 11, 1451, 34184, 295, 27043, 13, 51798], "temperature": 0.0, "avg_logprob":
  -0.22485659672663763, "compression_ratio": 1.3526011560693643, "no_speech_prob":
  0.007748408708721399}, {"id": 293, "seek": 116260, "start": 1162.6, "end": 1166.6799999999998,
  "text": " It depends on so many trade-offs, like how much recolor you will decircify
  and other things", "tokens": [50364, 467, 5946, 322, 370, 867, 4923, 12, 19231,
  11, 411, 577, 709, 850, 36182, 291, 486, 979, 347, 66, 2505, 293, 661, 721, 50568],
  "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio": 1.6,
  "no_speech_prob": 0.05158064886927605}, {"id": 294, "seek": 116260, "start": 1166.6799999999998,
  "end": 1167.6799999999998, "text": " like that.", "tokens": [50568, 411, 300, 13,
  50618], "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio":
  1.6, "no_speech_prob": 0.05158064886927605}, {"id": 295, "seek": 116260, "start":
  1167.6799999999998, "end": 1169.1599999999999, "text": " What are the dimensions
  of the vector?", "tokens": [50618, 708, 366, 264, 12819, 295, 264, 8062, 30, 50692],
  "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio": 1.6,
  "no_speech_prob": 0.05158064886927605}, {"id": 296, "seek": 116260, "start": 1169.1599999999999,
  "end": 1175.1999999999998, "text": " But I think that we found that to be quite
  feasible for our system.", "tokens": [50692, 583, 286, 519, 300, 321, 1352, 300,
  281, 312, 1596, 26648, 337, 527, 1185, 13, 50994], "temperature": 0.0, "avg_logprob":
  -0.2549551474947889, "compression_ratio": 1.6, "no_speech_prob": 0.05158064886927605},
  {"id": 297, "seek": 116260, "start": 1175.1999999999998, "end": 1177.1999999999998,
  "text": " We don''t do 768 dimensions.", "tokens": [50994, 492, 500, 380, 360, 24733,
  23, 12819, 13, 51094], "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio":
  1.6, "no_speech_prob": 0.05158064886927605}, {"id": 298, "seek": 116260, "start":
  1177.1999999999998, "end": 1180.76, "text": " Our neural nets produce a little bit
  less, but still it''s comparable.", "tokens": [51094, 2621, 18161, 36170, 5258,
  257, 707, 857, 1570, 11, 457, 920, 309, 311, 25323, 13, 51272], "temperature": 0.0,
  "avg_logprob": -0.2549551474947889, "compression_ratio": 1.6, "no_speech_prob":
  0.05158064886927605}, {"id": 299, "seek": 116260, "start": 1180.76, "end": 1183.04,
  "text": " It''s not that far off.", "tokens": [51272, 467, 311, 406, 300, 1400,
  766, 13, 51386], "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio":
  1.6, "no_speech_prob": 0.05158064886927605}, {"id": 300, "seek": 116260, "start":
  1183.04, "end": 1189.8799999999999, "text": " In terms of the neural network, I
  would say that transformers are required for proper", "tokens": [51386, 682, 2115,
  295, 264, 18161, 3209, 11, 286, 576, 584, 300, 4088, 433, 366, 4739, 337, 2296,
  51728], "temperature": 0.0, "avg_logprob": -0.2549551474947889, "compression_ratio":
  1.6, "no_speech_prob": 0.05158064886927605}, {"id": 301, "seek": 116260, "start":
  1189.8799999999999, "end": 1190.8799999999999, "text": " language understanding.",
  "tokens": [51728, 2856, 3701, 13, 51778], "temperature": 0.0, "avg_logprob": -0.2549551474947889,
  "compression_ratio": 1.6, "no_speech_prob": 0.05158064886927605}, {"id": 302, "seek":
  119088, "start": 1190.96, "end": 1195.3600000000001, "text": " One of the things
  I didn''t mention about our system was I think that we were basically", "tokens":
  [50368, 1485, 295, 264, 721, 286, 994, 380, 2152, 466, 527, 1185, 390, 286, 519,
  300, 321, 645, 1936, 50588], "temperature": 0.0, "avg_logprob": -0.3187896465433055,
  "compression_ratio": 1.6223175965665235, "no_speech_prob": 0.007115307729691267},
  {"id": 303, "seek": 119088, "start": 1195.3600000000001, "end": 1200.7600000000002,
  "text": " one of the first teams back in 2017 to incorporate transformers production
  architecture.", "tokens": [50588, 472, 295, 264, 700, 5491, 646, 294, 6591, 281,
  16091, 4088, 433, 4265, 9482, 13, 50858], "temperature": 0.0, "avg_logprob": -0.3187896465433055,
  "compression_ratio": 1.6223175965665235, "no_speech_prob": 0.007115307729691267},
  {"id": 304, "seek": 119088, "start": 1200.7600000000002, "end": 1205.48, "text":
  " This was my colleagues, Noah Constant.", "tokens": [50858, 639, 390, 452, 7734,
  11, 20895, 37413, 13, 51094], "temperature": 0.0, "avg_logprob": -0.3187896465433055,
  "compression_ratio": 1.6223175965665235, "no_speech_prob": 0.007115307729691267},
  {"id": 305, "seek": 119088, "start": 1205.48, "end": 1207.2800000000002, "text":
  " He was actually one of our colleagues.", "tokens": [51094, 634, 390, 767, 472,
  295, 527, 7734, 13, 51184], "temperature": 0.0, "avg_logprob": -0.3187896465433055,
  "compression_ratio": 1.6223175965665235, "no_speech_prob": 0.007115307729691267},
  {"id": 306, "seek": 119088, "start": 1207.2800000000002, "end": 1211.0400000000002,
  "text": " Previously being in our team was on the original transformer paper.",
  "tokens": [51184, 33606, 885, 294, 527, 1469, 390, 322, 264, 3380, 31782, 3035,
  13, 51372], "temperature": 0.0, "avg_logprob": -0.3187896465433055, "compression_ratio":
  1.6223175965665235, "no_speech_prob": 0.007115307729691267}, {"id": 307, "seek":
  119088, "start": 1211.0400000000002, "end": 1214.2, "text": " He was in Google Brain
  at that time doing that research.", "tokens": [51372, 634, 390, 294, 3329, 29783,
  412, 300, 565, 884, 300, 2132, 13, 51530], "temperature": 0.0, "avg_logprob": -0.3187896465433055,
  "compression_ratio": 1.6223175965665235, "no_speech_prob": 0.007115307729691267},
  {"id": 308, "seek": 121420, "start": 1214.2, "end": 1220.3600000000001, "text":
  " We wanted to productionize a plan to a model.", "tokens": [50364, 492, 1415, 281,
  4265, 1125, 257, 1393, 281, 257, 2316, 13, 50672], "temperature": 0.0, "avg_logprob":
  -0.30803849962022567, "compression_ratio": 1.584033613445378, "no_speech_prob":
  0.024104176089167595}, {"id": 309, "seek": 121420, "start": 1220.3600000000001,
  "end": 1225.04, "text": " Noah basically spent a couple of months, took that research
  level code and got it to production", "tokens": [50672, 20895, 1936, 4418, 257,
  1916, 295, 2493, 11, 1890, 300, 2132, 1496, 3089, 293, 658, 309, 281, 4265, 50906],
  "temperature": 0.0, "avg_logprob": -0.30803849962022567, "compression_ratio": 1.584033613445378,
  "no_speech_prob": 0.024104176089167595}, {"id": 310, "seek": 121420, "start": 1225.04,
  "end": 1226.04, "text": " quality.", "tokens": [50906, 3125, 13, 50956], "temperature":
  0.0, "avg_logprob": -0.30803849962022567, "compression_ratio": 1.584033613445378,
  "no_speech_prob": 0.024104176089167595}, {"id": 311, "seek": 121420, "start": 1226.04,
  "end": 1232.2, "text": " Talk to books is actually being powered by a very early
  transformer based model.", "tokens": [50956, 8780, 281, 3642, 307, 767, 885, 17786,
  538, 257, 588, 2440, 31782, 2361, 2316, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.30803849962022567, "compression_ratio": 1.584033613445378, "no_speech_prob":
  0.024104176089167595}, {"id": 312, "seek": 121420, "start": 1232.2, "end": 1238.6000000000001,
  "text": " We saw an enormous performance jump in our metrics, doing nothing other
  than switching to transformers.", "tokens": [51264, 492, 1866, 364, 11322, 3389,
  3012, 294, 527, 16367, 11, 884, 1825, 661, 813, 16493, 281, 4088, 433, 13, 51584],
  "temperature": 0.0, "avg_logprob": -0.30803849962022567, "compression_ratio": 1.584033613445378,
  "no_speech_prob": 0.024104176089167595}, {"id": 313, "seek": 121420, "start": 1238.6000000000001,
  "end": 1241.3600000000001, "text": " I''ve never seen such a big jump in any...",
  "tokens": [51584, 286, 600, 1128, 1612, 1270, 257, 955, 3012, 294, 604, 485, 51722],
  "temperature": 0.0, "avg_logprob": -0.30803849962022567, "compression_ratio": 1.584033613445378,
  "no_speech_prob": 0.024104176089167595}, {"id": 314, "seek": 124136, "start": 1241.36,
  "end": 1243.52, "text": " Our metrics, we were looking at F1.", "tokens": [50364,
  2621, 16367, 11, 321, 645, 1237, 412, 479, 16, 13, 50472], "temperature": 0.0, "avg_logprob":
  -0.33342599215572827, "compression_ratio": 1.3980099502487562, "no_speech_prob":
  0.010498964227735996}, {"id": 315, "seek": 124136, "start": 1243.52, "end": 1251.9199999999998,
  "text": " Our F1 jumped from 30% to 38%.", "tokens": [50472, 2621, 479, 16, 13864,
  490, 2217, 4, 281, 12843, 6856, 50892], "temperature": 0.0, "avg_logprob": -0.33342599215572827,
  "compression_ratio": 1.3980099502487562, "no_speech_prob": 0.010498964227735996},
  {"id": 316, "seek": 124136, "start": 1251.9199999999998, "end": 1253.7199999999998,
  "text": " Just by switching to transformers.", "tokens": [50892, 1449, 538, 16493,
  281, 4088, 433, 13, 50982], "temperature": 0.0, "avg_logprob": -0.33342599215572827,
  "compression_ratio": 1.3980099502487562, "no_speech_prob": 0.010498964227735996},
  {"id": 317, "seek": 124136, "start": 1253.7199999999998, "end": 1259.04, "text":
  " Not changing the training data or the evaluation objective, just making this one
  change in the", "tokens": [50982, 1726, 4473, 264, 3097, 1412, 420, 264, 13344,
  10024, 11, 445, 1455, 341, 472, 1319, 294, 264, 51248], "temperature": 0.0, "avg_logprob":
  -0.33342599215572827, "compression_ratio": 1.3980099502487562, "no_speech_prob":
  0.010498964227735996}, {"id": 318, "seek": 124136, "start": 1259.04, "end": 1261.04,
  "text": " architecture of the neural network.", "tokens": [51248, 9482, 295, 264,
  18161, 3209, 13, 51348], "temperature": 0.0, "avg_logprob": -0.33342599215572827,
  "compression_ratio": 1.3980099502487562, "no_speech_prob": 0.010498964227735996},
  {"id": 319, "seek": 124136, "start": 1261.04, "end": 1265.6, "text": " I would consider
  that''s an absolute requirement.", "tokens": [51348, 286, 576, 1949, 300, 311, 364,
  8236, 11695, 13, 51576], "temperature": 0.0, "avg_logprob": -0.33342599215572827,
  "compression_ratio": 1.3980099502487562, "no_speech_prob": 0.010498964227735996},
  {"id": 320, "seek": 126560, "start": 1265.6, "end": 1272.6, "text": " I would also
  say that I''m not very familiar with the economics of GPU scaling because it''s",
  "tokens": [50364, 286, 576, 611, 584, 300, 286, 478, 406, 588, 4963, 365, 264, 14564,
  295, 18407, 21589, 570, 309, 311, 50714], "temperature": 0.0, "avg_logprob": -0.279806750944291,
  "compression_ratio": 1.4609053497942386, "no_speech_prob": 0.01739194616675377},
  {"id": 321, "seek": 126560, "start": 1272.6, "end": 1274.76, "text": " generally
  kind of expensive.", "tokens": [50714, 5101, 733, 295, 5124, 13, 50822], "temperature":
  0.0, "avg_logprob": -0.279806750944291, "compression_ratio": 1.4609053497942386,
  "no_speech_prob": 0.01739194616675377}, {"id": 322, "seek": 126560, "start": 1274.76,
  "end": 1280.0, "text": " Our neural networks are actually designed to run reasonably
  well on CPUs.", "tokens": [50822, 2621, 18161, 9590, 366, 767, 4761, 281, 1190,
  23551, 731, 322, 13199, 82, 13, 51084], "temperature": 0.0, "avg_logprob": -0.279806750944291,
  "compression_ratio": 1.4609053497942386, "no_speech_prob": 0.01739194616675377},
  {"id": 323, "seek": 126560, "start": 1280.0, "end": 1287.56, "text": " There''s
  also these tips like obviously Google''s got the TPU, but Amazon has Inferencia.",
  "tokens": [51084, 821, 311, 611, 613, 6082, 411, 2745, 3329, 311, 658, 264, 314,
  8115, 11, 457, 6795, 575, 682, 612, 268, 2755, 13, 51462], "temperature": 0.0, "avg_logprob":
  -0.279806750944291, "compression_ratio": 1.4609053497942386, "no_speech_prob": 0.01739194616675377},
  {"id": 324, "seek": 126560, "start": 1287.56, "end": 1291.32, "text": " We''re still
  kind of experimenting with what we can do with latency there.", "tokens": [51462,
  492, 434, 920, 733, 295, 29070, 365, 437, 321, 393, 360, 365, 27043, 456, 13, 51650],
  "temperature": 0.0, "avg_logprob": -0.279806750944291, "compression_ratio": 1.4609053497942386,
  "no_speech_prob": 0.01739194616675377}, {"id": 325, "seek": 129132, "start": 1291.32,
  "end": 1301.4399999999998, "text": " I think that you can count on about 20 to 30
  milliseconds of latency at the low end from", "tokens": [50364, 286, 519, 300, 291,
  393, 1207, 322, 466, 945, 281, 2217, 34184, 295, 27043, 412, 264, 2295, 917, 490,
  50870], "temperature": 0.0, "avg_logprob": -0.22534859807867752, "compression_ratio":
  1.5853658536585367, "no_speech_prob": 0.003443585243076086}, {"id": 326, "seek":
  129132, "start": 1301.4399999999998, "end": 1306.1599999999999, "text": " coming
  from the encoding process unless you start moving to GPU or something and then you",
  "tokens": [50870, 1348, 490, 264, 43430, 1399, 5969, 291, 722, 2684, 281, 18407,
  420, 746, 293, 550, 291, 51106], "temperature": 0.0, "avg_logprob": -0.22534859807867752,
  "compression_ratio": 1.5853658536585367, "no_speech_prob": 0.003443585243076086},
  {"id": 327, "seek": 129132, "start": 1306.1599999999999, "end": 1311.84, "text":
  " might be able to do maybe 5 to 10 milliseconds.", "tokens": [51106, 1062, 312,
  1075, 281, 360, 1310, 1025, 281, 1266, 34184, 13, 51390], "temperature": 0.0, "avg_logprob":
  -0.22534859807867752, "compression_ratio": 1.5853658536585367, "no_speech_prob":
  0.003443585243076086}, {"id": 328, "seek": 129132, "start": 1311.84, "end": 1319.1599999999999,
  "text": " If you put that all together, it seems to me realistically you can shoot
  for 30 to 40 milliseconds", "tokens": [51390, 759, 291, 829, 300, 439, 1214, 11,
  309, 2544, 281, 385, 40734, 291, 393, 3076, 337, 2217, 281, 3356, 34184, 51756],
  "temperature": 0.0, "avg_logprob": -0.22534859807867752, "compression_ratio": 1.5853658536585367,
  "no_speech_prob": 0.003443585243076086}, {"id": 329, "seek": 131916, "start": 1319.16,
  "end": 1323.72, "text": " would be pretty aggressive in terms of what you can get
  at the lower bound.", "tokens": [50364, 576, 312, 1238, 10762, 294, 2115, 295, 437,
  291, 393, 483, 412, 264, 3126, 5472, 13, 50592], "temperature": 0.0, "avg_logprob":
  -0.28014289226728617, "compression_ratio": 1.5524193548387097, "no_speech_prob":
  0.2558579444885254}, {"id": 330, "seek": 131916, "start": 1323.72, "end": 1327.52,
  "text": " And maybe for many companies out there, this will be okay.", "tokens":
  [50592, 400, 1310, 337, 867, 3431, 484, 456, 11, 341, 486, 312, 1392, 13, 50782],
  "temperature": 0.0, "avg_logprob": -0.28014289226728617, "compression_ratio": 1.5524193548387097,
  "no_speech_prob": 0.2558579444885254}, {"id": 331, "seek": 131916, "start": 1327.52,
  "end": 1333.3600000000001, "text": " As long as they don''t run web scale type of
  deployment, maybe they can scale per region", "tokens": [50782, 1018, 938, 382,
  436, 500, 380, 1190, 3670, 4373, 2010, 295, 19317, 11, 1310, 436, 393, 4373, 680,
  4458, 51074], "temperature": 0.0, "avg_logprob": -0.28014289226728617, "compression_ratio":
  1.5524193548387097, "no_speech_prob": 0.2558579444885254}, {"id": 332, "seek": 131916,
  "start": 1333.3600000000001, "end": 1337.92, "text": " or per zone or whatever it
  is that makes sense to them.", "tokens": [51074, 420, 680, 6668, 420, 2035, 309,
  307, 300, 1669, 2020, 281, 552, 13, 51302], "temperature": 0.0, "avg_logprob": -0.28014289226728617,
  "compression_ratio": 1.5524193548387097, "no_speech_prob": 0.2558579444885254},
  {"id": 333, "seek": 131916, "start": 1337.92, "end": 1343.0800000000002, "text":
  " I think sounds like 30 to 40 milliseconds could be quite an okay speed.", "tokens":
  [51302, 286, 519, 3263, 411, 2217, 281, 3356, 34184, 727, 312, 1596, 364, 1392,
  3073, 13, 51560], "temperature": 0.0, "avg_logprob": -0.28014289226728617, "compression_ratio":
  1.5524193548387097, "no_speech_prob": 0.2558579444885254}, {"id": 334, "seek": 131916,
  "start": 1343.0800000000002, "end": 1344.92, "text": " We''re talking about latency
  there.", "tokens": [51560, 492, 434, 1417, 466, 27043, 456, 13, 51652], "temperature":
  0.0, "avg_logprob": -0.28014289226728617, "compression_ratio": 1.5524193548387097,
  "no_speech_prob": 0.2558579444885254}, {"id": 335, "seek": 134492, "start": 1344.92,
  "end": 1349.2, "text": " I think that''s a perfectly acceptable speed even for web
  search or something.", "tokens": [50364, 286, 519, 300, 311, 257, 6239, 15513, 3073,
  754, 337, 3670, 3164, 420, 746, 13, 50578], "temperature": 0.0, "avg_logprob": -0.3164606730143229,
  "compression_ratio": 1.6148409893992932, "no_speech_prob": 0.3439730107784271},
  {"id": 336, "seek": 134492, "start": 1349.2, "end": 1353.8000000000002, "text":
  " That''s literally the blink of an eye, 40 milliseconds.", "tokens": [50578, 663,
  311, 3736, 264, 24667, 295, 364, 3313, 11, 3356, 34184, 13, 50808], "temperature":
  0.0, "avg_logprob": -0.3164606730143229, "compression_ratio": 1.6148409893992932,
  "no_speech_prob": 0.3439730107784271}, {"id": 337, "seek": 134492, "start": 1353.8000000000002,
  "end": 1358.76, "text": " I think the other thing to note is that these solutions
  are very horizontally scalable.", "tokens": [50808, 286, 519, 264, 661, 551, 281,
  3637, 307, 300, 613, 6547, 366, 588, 33796, 38481, 13, 51056], "temperature": 0.0,
  "avg_logprob": -0.3164606730143229, "compression_ratio": 1.6148409893992932, "no_speech_prob":
  0.3439730107784271}, {"id": 338, "seek": 134492, "start": 1358.76, "end": 1363.96,
  "text": " In terms of serving any given throughput, you just scale the neural network
  and code", "tokens": [51056, 682, 2115, 295, 8148, 604, 2212, 44629, 11, 291, 445,
  4373, 264, 18161, 3209, 293, 3089, 51316], "temperature": 0.0, "avg_logprob": -0.3164606730143229,
  "compression_ratio": 1.6148409893992932, "no_speech_prob": 0.3439730107784271},
  {"id": 339, "seek": 134492, "start": 1363.96, "end": 1369.96, "text": " or pools
  and you can replicate the vector database if using FIAS for instance you start up",
  "tokens": [51316, 420, 28688, 293, 291, 393, 25356, 264, 8062, 8149, 498, 1228,
  479, 40, 3160, 337, 5197, 291, 722, 493, 51616], "temperature": 0.0, "avg_logprob":
  -0.3164606730143229, "compression_ratio": 1.6148409893992932, "no_speech_prob":
  0.3439730107784271}, {"id": 340, "seek": 134492, "start": 1369.96, "end": 1370.96,
  "text": " replicas.", "tokens": [51616, 3248, 9150, 13, 51666], "temperature": 0.0,
  "avg_logprob": -0.3164606730143229, "compression_ratio": 1.6148409893992932, "no_speech_prob":
  0.3439730107784271}, {"id": 341, "seek": 134492, "start": 1370.96, "end": 1372.8400000000001,
  "text": " You can basically get almost unlimited throughput.", "tokens": [51666,
  509, 393, 1936, 483, 1920, 21950, 44629, 13, 51760], "temperature": 0.0, "avg_logprob":
  -0.3164606730143229, "compression_ratio": 1.6148409893992932, "no_speech_prob":
  0.3439730107784271}, {"id": 342, "seek": 137284, "start": 1372.84, "end": 1375.1599999999999,
  "text": " It just depends on how much money you have to throw at the problem.",
  "tokens": [50364, 467, 445, 5946, 322, 577, 709, 1460, 291, 362, 281, 3507, 412,
  264, 1154, 13, 50480], "temperature": 0.0, "avg_logprob": -0.24277473077541445,
  "compression_ratio": 1.6446886446886446, "no_speech_prob": 0.060518525540828705},
  {"id": 343, "seek": 137284, "start": 1375.1599999999999, "end": 1378.76, "text":
  " So if you need 500 QPS, bring up more hardware.", "tokens": [50480, 407, 498,
  291, 643, 5923, 1249, 6273, 11, 1565, 493, 544, 8837, 13, 50660], "temperature":
  0.0, "avg_logprob": -0.24277473077541445, "compression_ratio": 1.6446886446886446,
  "no_speech_prob": 0.060518525540828705}, {"id": 344, "seek": 137284, "start": 1378.76,
  "end": 1381.84, "text": " If you need 5000 QPS, you can bring up more hardware and
  do it.", "tokens": [50660, 759, 291, 643, 23777, 1249, 6273, 11, 291, 393, 1565,
  493, 544, 8837, 293, 360, 309, 13, 50814], "temperature": 0.0, "avg_logprob": -0.24277473077541445,
  "compression_ratio": 1.6446886446886446, "no_speech_prob": 0.060518525540828705},
  {"id": 345, "seek": 137284, "start": 1381.84, "end": 1383.3999999999999, "text":
  " Yeah, absolutely.", "tokens": [50814, 865, 11, 3122, 13, 50892], "temperature":
  0.0, "avg_logprob": -0.24277473077541445, "compression_ratio": 1.6446886446886446,
  "no_speech_prob": 0.060518525540828705}, {"id": 346, "seek": 137284, "start": 1383.3999999999999,
  "end": 1389.4399999999998, "text": " I also wanted to tap into what you said that
  distilling bird would be beyond reach for", "tokens": [50892, 286, 611, 1415, 281,
  5119, 666, 437, 291, 848, 300, 1483, 7345, 5255, 576, 312, 4399, 2524, 337, 51194],
  "temperature": 0.0, "avg_logprob": -0.24277473077541445, "compression_ratio": 1.6446886446886446,
  "no_speech_prob": 0.060518525540828705}, {"id": 347, "seek": 137284, "start": 1389.4399999999998,
  "end": 1390.4399999999998, "text": " many companies.", "tokens": [51194, 867, 3431,
  13, 51244], "temperature": 0.0, "avg_logprob": -0.24277473077541445, "compression_ratio":
  1.6446886446886446, "no_speech_prob": 0.060518525540828705}, {"id": 348, "seek":
  137284, "start": 1390.4399999999998, "end": 1394.12, "text": " Can you open up a
  little bit and also can you share with our audience what do you mean by", "tokens":
  [51244, 1664, 291, 1269, 493, 257, 707, 857, 293, 611, 393, 291, 2073, 365, 527,
  4034, 437, 360, 291, 914, 538, 51428], "temperature": 0.0, "avg_logprob": -0.24277473077541445,
  "compression_ratio": 1.6446886446886446, "no_speech_prob": 0.060518525540828705},
  {"id": 349, "seek": 137284, "start": 1394.12, "end": 1395.12, "text": " distilling?",
  "tokens": [51428, 1483, 7345, 30, 51478], "temperature": 0.0, "avg_logprob": -0.24277473077541445,
  "compression_ratio": 1.6446886446886446, "no_speech_prob": 0.060518525540828705},
  {"id": 350, "seek": 137284, "start": 1395.12, "end": 1398.8, "text": " Maybe some
  of our subscribers don''t know that.", "tokens": [51478, 2704, 512, 295, 527, 11092,
  500, 380, 458, 300, 13, 51662], "temperature": 0.0, "avg_logprob": -0.24277473077541445,
  "compression_ratio": 1.6446886446886446, "no_speech_prob": 0.060518525540828705},
  {"id": 351, "seek": 139880, "start": 1399.6399999999999, "end": 1403.28, "text":
  " So in the nutshell, and also why do you think that it''s so hard to do?", "tokens":
  [50406, 407, 294, 264, 37711, 11, 293, 611, 983, 360, 291, 519, 300, 309, 311, 370,
  1152, 281, 360, 30, 50588], "temperature": 0.0, "avg_logprob": -0.28881819248199464,
  "compression_ratio": 1.6582914572864322, "no_speech_prob": 0.006933798547834158},
  {"id": 352, "seek": 139880, "start": 1405.28, "end": 1414.0, "text": " Okay, well,
  so what distillation of a neural network refers to is taking a very large neural",
  "tokens": [50688, 1033, 11, 731, 11, 370, 437, 42923, 399, 295, 257, 18161, 3209,
  14942, 281, 307, 1940, 257, 588, 2416, 18161, 51124], "temperature": 0.0, "avg_logprob":
  -0.28881819248199464, "compression_ratio": 1.6582914572864322, "no_speech_prob":
  0.006933798547834158}, {"id": 353, "seek": 139880, "start": 1414.0, "end": 1419.8,
  "text": " network and neural network with a lot of parameters, it''s called billions
  of parameters, which", "tokens": [51124, 3209, 293, 18161, 3209, 365, 257, 688,
  295, 9834, 11, 309, 311, 1219, 17375, 295, 9834, 11, 597, 51414], "temperature":
  0.0, "avg_logprob": -0.28881819248199464, "compression_ratio": 1.6582914572864322,
  "no_speech_prob": 0.006933798547834158}, {"id": 354, "seek": 139880, "start": 1419.8,
  "end": 1425.8799999999999, "text": " is very accurate but cannot reasonably be run
  on a production workload.", "tokens": [51414, 307, 588, 8559, 457, 2644, 23551,
  312, 1190, 322, 257, 4265, 20139, 13, 51718], "temperature": 0.0, "avg_logprob":
  -0.28881819248199464, "compression_ratio": 1.6582914572864322, "no_speech_prob":
  0.006933798547834158}, {"id": 355, "seek": 142588, "start": 1425.88, "end": 1431.1200000000001,
  "text": " And training a much smaller model that captures as much of the performance
  of the original", "tokens": [50364, 400, 3097, 257, 709, 4356, 2316, 300, 27986,
  382, 709, 295, 264, 3389, 295, 264, 3380, 50626], "temperature": 0.0, "avg_logprob":
  -0.1924495469956171, "compression_ratio": 1.6610169491525424, "no_speech_prob":
  0.04053569585084915}, {"id": 356, "seek": 142588, "start": 1431.1200000000001, "end":
  1437.64, "text": " model as possible, but fitting inside the engineering parameters
  of your production system.", "tokens": [50626, 2316, 382, 1944, 11, 457, 15669,
  1854, 264, 7043, 9834, 295, 428, 4265, 1185, 13, 50952], "temperature": 0.0, "avg_logprob":
  -0.1924495469956171, "compression_ratio": 1.6610169491525424, "no_speech_prob":
  0.04053569585084915}, {"id": 357, "seek": 142588, "start": 1437.64, "end": 1443.1200000000001,
  "text": " So able to for instance run an inference within 50 milliseconds.", "tokens":
  [50952, 407, 1075, 281, 337, 5197, 1190, 364, 38253, 1951, 2625, 34184, 13, 51226],
  "temperature": 0.0, "avg_logprob": -0.1924495469956171, "compression_ratio": 1.6610169491525424,
  "no_speech_prob": 0.04053569585084915}, {"id": 358, "seek": 142588, "start": 1443.1200000000001,
  "end": 1450.5600000000002, "text": " So the way that distillation normally happens
  is you use the parent model is called the teacher", "tokens": [51226, 407, 264,
  636, 300, 42923, 399, 5646, 2314, 307, 291, 764, 264, 2596, 2316, 307, 1219, 264,
  5027, 51598], "temperature": 0.0, "avg_logprob": -0.1924495469956171, "compression_ratio":
  1.6610169491525424, "no_speech_prob": 0.04053569585084915}, {"id": 359, "seek":
  142588, "start": 1450.5600000000002, "end": 1455.3200000000002, "text": " model
  and you do a large scale labeling of data.", "tokens": [51598, 2316, 293, 291, 360,
  257, 2416, 4373, 40244, 295, 1412, 13, 51836], "temperature": 0.0, "avg_logprob":
  -0.1924495469956171, "compression_ratio": 1.6610169491525424, "no_speech_prob":
  0.04053569585084915}, {"id": 360, "seek": 145532, "start": 1455.32, "end": 1460.8,
  "text": " And essentially the student model, the small model that you''re training
  needs to learn", "tokens": [50364, 400, 4476, 264, 3107, 2316, 11, 264, 1359, 2316,
  300, 291, 434, 3097, 2203, 281, 1466, 50638], "temperature": 0.0, "avg_logprob":
  -0.15440780558484665, "compression_ratio": 1.7854077253218885, "no_speech_prob":
  0.00035531993489712477}, {"id": 361, "seek": 145532, "start": 1460.8, "end": 1463.0,
  "text": " to make the same predictions.", "tokens": [50638, 281, 652, 264, 912,
  21264, 13, 50748], "temperature": 0.0, "avg_logprob": -0.15440780558484665, "compression_ratio":
  1.7854077253218885, "no_speech_prob": 0.00035531993489712477}, {"id": 362, "seek":
  145532, "start": 1463.0, "end": 1470.08, "text": " And interestingly, it gets as
  much bang for the buck in terms of training from learning", "tokens": [50748, 400,
  25873, 11, 309, 2170, 382, 709, 8550, 337, 264, 14894, 294, 2115, 295, 3097, 490,
  2539, 51102], "temperature": 0.0, "avg_logprob": -0.15440780558484665, "compression_ratio":
  1.7854077253218885, "no_speech_prob": 0.00035531993489712477}, {"id": 363, "seek":
  145532, "start": 1470.08, "end": 1474.9199999999998, "text": " to make the correct
  predictions as it does from learning to, you know, assign probabilities", "tokens":
  [51102, 281, 652, 264, 3006, 21264, 382, 309, 775, 490, 2539, 281, 11, 291, 458,
  11, 6269, 33783, 51344], "temperature": 0.0, "avg_logprob": -0.15440780558484665,
  "compression_ratio": 1.7854077253218885, "no_speech_prob": 0.00035531993489712477},
  {"id": 364, "seek": 145532, "start": 1474.9199999999998, "end": 1476.9199999999998,
  "text": " to the incorrect predictions.", "tokens": [51344, 281, 264, 18424, 21264,
  13, 51444], "temperature": 0.0, "avg_logprob": -0.15440780558484665, "compression_ratio":
  1.7854077253218885, "no_speech_prob": 0.00035531993489712477}, {"id": 365, "seek":
  145532, "start": 1476.9199999999998, "end": 1483.4399999999998, "text": " So the
  reason I''m saying that distillation is difficult is there''s, I think it approaches",
  "tokens": [51444, 407, 264, 1778, 286, 478, 1566, 300, 42923, 399, 307, 2252, 307,
  456, 311, 11, 286, 519, 309, 11587, 51770], "temperature": 0.0, "avg_logprob": -0.15440780558484665,
  "compression_ratio": 1.7854077253218885, "no_speech_prob": 0.00035531993489712477},
  {"id": 366, "seek": 148344, "start": 1483.44, "end": 1485.6000000000001, "text":
  " to it, it''s still a fairly open research topic.", "tokens": [50364, 281, 309,
  11, 309, 311, 920, 257, 6457, 1269, 2132, 4829, 13, 50472], "temperature": 0.0,
  "avg_logprob": -0.20257222311837333, "compression_ratio": 1.6029411764705883, "no_speech_prob":
  0.09794837236404419}, {"id": 367, "seek": 148344, "start": 1485.6000000000001, "end":
  1487.48, "text": " There''s a lot of active research.", "tokens": [50472, 821, 311,
  257, 688, 295, 4967, 2132, 13, 50566], "temperature": 0.0, "avg_logprob": -0.20257222311837333,
  "compression_ratio": 1.6029411764705883, "no_speech_prob": 0.09794837236404419},
  {"id": 368, "seek": 148344, "start": 1487.48, "end": 1490.6000000000001, "text":
  " I haven''t looked in the last couple of years as possible that there might be
  frameworks", "tokens": [50566, 286, 2378, 380, 2956, 294, 264, 1036, 1916, 295,
  924, 382, 1944, 300, 456, 1062, 312, 29834, 50722], "temperature": 0.0, "avg_logprob":
  -0.20257222311837333, "compression_ratio": 1.6029411764705883, "no_speech_prob":
  0.09794837236404419}, {"id": 369, "seek": 148344, "start": 1490.6000000000001, "end":
  1492.88, "text": " out there now that make this much easier.", "tokens": [50722,
  484, 456, 586, 300, 652, 341, 709, 3571, 13, 50836], "temperature": 0.0, "avg_logprob":
  -0.20257222311837333, "compression_ratio": 1.6029411764705883, "no_speech_prob":
  0.09794837236404419}, {"id": 370, "seek": 148344, "start": 1492.88, "end": 1499.56,
  "text": " But certainly while I was at Google in 2018, 1920 time frame distillation
  was generally", "tokens": [50836, 583, 3297, 1339, 286, 390, 412, 3329, 294, 6096,
  11, 22003, 565, 3920, 42923, 399, 390, 5101, 51170], "temperature": 0.0, "avg_logprob":
  -0.20257222311837333, "compression_ratio": 1.6029411764705883, "no_speech_prob":
  0.09794837236404419}, {"id": 371, "seek": 148344, "start": 1499.56, "end": 1504.0,
  "text": " a topic that was tackled by entire teams working over a quarter or two,
  at least for the", "tokens": [51170, 257, 4829, 300, 390, 9426, 1493, 538, 2302,
  5491, 1364, 670, 257, 6555, 420, 732, 11, 412, 1935, 337, 264, 51392], "temperature":
  0.0, "avg_logprob": -0.20257222311837333, "compression_ratio": 1.6029411764705883,
  "no_speech_prob": 0.09794837236404419}, {"id": 372, "seek": 148344, "start": 1504.0,
  "end": 1505.48, "text": " most serious production systems.", "tokens": [51392, 881,
  3156, 4265, 3652, 13, 51466], "temperature": 0.0, "avg_logprob": -0.20257222311837333,
  "compression_ratio": 1.6029411764705883, "no_speech_prob": 0.09794837236404419},
  {"id": 373, "seek": 148344, "start": 1505.48, "end": 1507.48, "text": " That''s
  how it was used to go.", "tokens": [51466, 663, 311, 577, 309, 390, 1143, 281, 352,
  13, 51566], "temperature": 0.0, "avg_logprob": -0.20257222311837333, "compression_ratio":
  1.6029411764705883, "no_speech_prob": 0.09794837236404419}, {"id": 374, "seek":
  148344, "start": 1507.48, "end": 1508.48, "text": " Yeah.", "tokens": [51566, 865,
  13, 51616], "temperature": 0.0, "avg_logprob": -0.20257222311837333, "compression_ratio":
  1.6029411764705883, "no_speech_prob": 0.09794837236404419}, {"id": 375, "seek":
  148344, "start": 1508.48, "end": 1511.92, "text": " And definitely when it comes
  to collecting data as you rightly not just, you know, it''s", "tokens": [51616,
  400, 2138, 562, 309, 1487, 281, 12510, 1412, 382, 291, 32879, 406, 445, 11, 291,
  458, 11, 309, 311, 51788], "temperature": 0.0, "avg_logprob": -0.20257222311837333,
  "compression_ratio": 1.6029411764705883, "no_speech_prob": 0.09794837236404419},
  {"id": 376, "seek": 151192, "start": 1511.92, "end": 1517.1200000000001, "text":
  " not something you can easily scale unless you have some clever technique for data
  augmentation.", "tokens": [50364, 406, 746, 291, 393, 3612, 4373, 5969, 291, 362,
  512, 13494, 6532, 337, 1412, 14501, 19631, 13, 50624], "temperature": 0.0, "avg_logprob":
  -0.2160141626993815, "compression_ratio": 1.6570397111913358, "no_speech_prob":
  0.009416880086064339}, {"id": 377, "seek": 151192, "start": 1517.1200000000001,
  "end": 1523.0, "text": " And even then, like for text, as I was eluding in previous
  podcasts, you know, like if you", "tokens": [50624, 400, 754, 550, 11, 411, 337,
  2487, 11, 382, 286, 390, 806, 33703, 294, 3894, 24045, 11, 291, 458, 11, 411, 498,
  291, 50918], "temperature": 0.0, "avg_logprob": -0.2160141626993815, "compression_ratio":
  1.6570397111913358, "no_speech_prob": 0.009416880086064339}, {"id": 378, "seek":
  151192, "start": 1523.0, "end": 1527.5600000000002, "text": " have like a London
  is the capital of Great Britain, you cannot put any random city there", "tokens":
  [50918, 362, 411, 257, 7042, 307, 264, 4238, 295, 3769, 12960, 11, 291, 2644, 829,
  604, 4974, 2307, 456, 51146], "temperature": 0.0, "avg_logprob": -0.2160141626993815,
  "compression_ratio": 1.6570397111913358, "no_speech_prob": 0.009416880086064339},
  {"id": 379, "seek": 151192, "start": 1527.5600000000002, "end": 1529.0800000000002,
  "text": " in that specific sentence, right?", "tokens": [51146, 294, 300, 2685,
  8174, 11, 558, 30, 51222], "temperature": 0.0, "avg_logprob": -0.2160141626993815,
  "compression_ratio": 1.6570397111913358, "no_speech_prob": 0.009416880086064339},
  {"id": 380, "seek": 151192, "start": 1529.0800000000002, "end": 1530.0800000000002,
  "text": " Right.", "tokens": [51222, 1779, 13, 51272], "temperature": 0.0, "avg_logprob":
  -0.2160141626993815, "compression_ratio": 1.6570397111913358, "no_speech_prob":
  0.009416880086064339}, {"id": 381, "seek": 151192, "start": 1530.0800000000002,
  "end": 1531.0800000000002, "text": " Right.", "tokens": [51272, 1779, 13, 51322],
  "temperature": 0.0, "avg_logprob": -0.2160141626993815, "compression_ratio": 1.6570397111913358,
  "no_speech_prob": 0.009416880086064339}, {"id": 382, "seek": 151192, "start": 1531.0800000000002,
  "end": 1532.0800000000002, "text": " Right.", "tokens": [51322, 1779, 13, 51372],
  "temperature": 0.0, "avg_logprob": -0.2160141626993815, "compression_ratio": 1.6570397111913358,
  "no_speech_prob": 0.009416880086064339}, {"id": 383, "seek": 151192, "start": 1532.0800000000002,
  "end": 1533.0800000000002, "text": " Yeah, you need to have certain control.", "tokens":
  [51372, 865, 11, 291, 643, 281, 362, 1629, 1969, 13, 51422], "temperature": 0.0,
  "avg_logprob": -0.2160141626993815, "compression_ratio": 1.6570397111913358, "no_speech_prob":
  0.009416880086064339}, {"id": 384, "seek": 151192, "start": 1533.0800000000002,
  "end": 1539.68, "text": " But there are still ways to, for example, use retrieval
  itself to augment your data set,", "tokens": [51422, 583, 456, 366, 920, 2098, 281,
  11, 337, 1365, 11, 764, 19817, 3337, 2564, 281, 29919, 428, 1412, 992, 11, 51752],
  "temperature": 0.0, "avg_logprob": -0.2160141626993815, "compression_ratio": 1.6570397111913358,
  "no_speech_prob": 0.009416880086064339}, {"id": 385, "seek": 153968, "start": 1539.68,
  "end": 1540.68, "text": " right?", "tokens": [50364, 558, 30, 50414], "temperature":
  0.0, "avg_logprob": -0.19192072653001355, "compression_ratio": 1.6620209059233448,
  "no_speech_prob": 0.014143800362944603}, {"id": 386, "seek": 153968, "start": 1540.68,
  "end": 1543.52, "text": " For example, if you need more entities, you can find them
  through retrieval, maybe even", "tokens": [50414, 1171, 1365, 11, 498, 291, 643,
  544, 16667, 11, 291, 393, 915, 552, 807, 19817, 3337, 11, 1310, 754, 50556], "temperature":
  0.0, "avg_logprob": -0.19192072653001355, "compression_ratio": 1.6620209059233448,
  "no_speech_prob": 0.014143800362944603}, {"id": 387, "seek": 153968, "start": 1543.52,
  "end": 1546.0, "text": " through vector search, by the way.", "tokens": [50556,
  807, 8062, 3164, 11, 538, 264, 636, 13, 50680], "temperature": 0.0, "avg_logprob":
  -0.19192072653001355, "compression_ratio": 1.6620209059233448, "no_speech_prob":
  0.014143800362944603}, {"id": 388, "seek": 153968, "start": 1546.0, "end": 1549.0,
  "text": " I don''t know if somebody experimented with that already.", "tokens":
  [50680, 286, 500, 380, 458, 498, 2618, 5120, 292, 365, 300, 1217, 13, 50830], "temperature":
  0.0, "avg_logprob": -0.19192072653001355, "compression_ratio": 1.6620209059233448,
  "no_speech_prob": 0.014143800362944603}, {"id": 389, "seek": 153968, "start": 1549.0,
  "end": 1553.5600000000002, "text": " But there are other techniques like kind of
  producing these negative examples and as you", "tokens": [50830, 583, 456, 366,
  661, 7512, 411, 733, 295, 10501, 613, 3671, 5110, 293, 382, 291, 51058], "temperature":
  0.0, "avg_logprob": -0.19192072653001355, "compression_ratio": 1.6620209059233448,
  "no_speech_prob": 0.014143800362944603}, {"id": 390, "seek": 153968, "start": 1553.5600000000002,
  "end": 1554.5600000000002, "text": " alluded to, right?", "tokens": [51058, 33919,
  281, 11, 558, 30, 51108], "temperature": 0.0, "avg_logprob": -0.19192072653001355,
  "compression_ratio": 1.6620209059233448, "no_speech_prob": 0.014143800362944603},
  {"id": 391, "seek": 153968, "start": 1554.5600000000002, "end": 1559.96, "text":
  " So you need to have as many negative also as many positive so that your model
  is balanced,", "tokens": [51108, 407, 291, 643, 281, 362, 382, 867, 3671, 611, 382,
  867, 3353, 370, 300, 428, 2316, 307, 13902, 11, 51378], "temperature": 0.0, "avg_logprob":
  -0.19192072653001355, "compression_ratio": 1.6620209059233448, "no_speech_prob":
  0.014143800362944603}, {"id": 392, "seek": 153968, "start": 1559.96, "end": 1560.96,
  "text": " right?", "tokens": [51378, 558, 30, 51428], "temperature": 0.0, "avg_logprob":
  -0.19192072653001355, "compression_ratio": 1.6620209059233448, "no_speech_prob":
  0.014143800362944603}, {"id": 393, "seek": 153968, "start": 1560.96, "end": 1567.8400000000001,
  "text": " And that goes to a general model training topic, which is a year to your
  point.", "tokens": [51428, 400, 300, 1709, 281, 257, 2674, 2316, 3097, 4829, 11,
  597, 307, 257, 1064, 281, 428, 935, 13, 51772], "temperature": 0.0, "avg_logprob":
  -0.19192072653001355, "compression_ratio": 1.6620209059233448, "no_speech_prob":
  0.014143800362944603}, {"id": 394, "seek": 153968, "start": 1567.8400000000001,
  "end": 1568.8400000000001, "text": " Yes.", "tokens": [51772, 1079, 13, 51822],
  "temperature": 0.0, "avg_logprob": -0.19192072653001355, "compression_ratio": 1.6620209059233448,
  "no_speech_prob": 0.014143800362944603}, {"id": 395, "seek": 156884, "start": 1568.84,
  "end": 1597.6, "text": " And I think that''s one of the key to producing a neural
  retriever that can outperform BM25", "tokens": [50364, 400, 286, 519, 300, 311,
  472, 295, 264, 2141, 281, 10501, 257, 18161, 19817, 331, 300, 393, 484, 26765, 15901,
  6074, 51802], "temperature": 0.2, "avg_logprob": -0.8956533813476563, "compression_ratio":
  1.0344827586206897, "no_speech_prob": 0.03218916431069374}, {"id": 396, "seek":
  159760, "start": 1597.6, "end": 1598.6, "text": " in every workload.", "tokens":
  [50364, 294, 633, 20139, 13, 50414], "temperature": 0.0, "avg_logprob": -0.32192740853377216,
  "compression_ratio": 1.6608996539792387, "no_speech_prob": 0.3511809706687927},
  {"id": 397, "seek": 159760, "start": 1598.6, "end": 1600.6, "text": " No, so it''s
  an excellent point.", "tokens": [50414, 883, 11, 370, 309, 311, 364, 7103, 935,
  13, 50514], "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio":
  1.6608996539792387, "no_speech_prob": 0.3511809706687927}, {"id": 398, "seek": 159760,
  "start": 1600.6, "end": 1601.6, "text": " Yeah.", "tokens": [50514, 865, 13, 50564],
  "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio": 1.6608996539792387,
  "no_speech_prob": 0.3511809706687927}, {"id": 399, "seek": 159760, "start": 1601.6,
  "end": 1607.48, "text": " Also, I just reminded me of one challenge that we''ve
  been solving in my team actually earlier", "tokens": [50564, 2743, 11, 286, 445,
  15920, 385, 295, 472, 3430, 300, 321, 600, 668, 12606, 294, 452, 1469, 767, 3071,
  50858], "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio":
  1.6608996539792387, "no_speech_prob": 0.3511809706687927}, {"id": 400, "seek": 159760,
  "start": 1607.48, "end": 1610.6399999999999, "text": " with building like a job
  search engine system.", "tokens": [50858, 365, 2390, 411, 257, 1691, 3164, 2848,
  1185, 13, 51016], "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio":
  1.6608996539792387, "no_speech_prob": 0.3511809706687927}, {"id": 401, "seek": 159760,
  "start": 1610.6399999999999, "end": 1615.6, "text": " And you know, like when you
  evaluate the performance, let''s say precision or when it kind", "tokens": [51016,
  400, 291, 458, 11, 411, 562, 291, 13059, 264, 3389, 11, 718, 311, 584, 18356, 420,
  562, 309, 733, 51264], "temperature": 0.0, "avg_logprob": -0.32192740853377216,
  "compression_ratio": 1.6608996539792387, "no_speech_prob": 0.3511809706687927},
  {"id": 402, "seek": 159760, "start": 1615.6, "end": 1620.9199999999998, "text":
  " of, we call it misrecall, so how frequently it mis triggers to query, shouldn''t
  have actually", "tokens": [51264, 295, 11, 321, 818, 309, 3346, 13867, 336, 11,
  370, 577, 10374, 309, 3346, 22827, 281, 14581, 11, 4659, 380, 362, 767, 51530],
  "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio": 1.6608996539792387,
  "no_speech_prob": 0.3511809706687927}, {"id": 403, "seek": 159760, "start": 1620.9199999999998,
  "end": 1622.1599999999999, "text": " triggered.", "tokens": [51530, 21710, 13, 51592],
  "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio": 1.6608996539792387,
  "no_speech_prob": 0.3511809706687927}, {"id": 404, "seek": 159760, "start": 1622.1599999999999,
  "end": 1627.1599999999999, "text": " And you know, like the basic challenge there
  is, okay, I have this job queries, which I", "tokens": [51592, 400, 291, 458, 11,
  411, 264, 3875, 3430, 456, 307, 11, 1392, 11, 286, 362, 341, 1691, 24109, 11, 597,
  286, 51842], "temperature": 0.0, "avg_logprob": -0.32192740853377216, "compression_ratio":
  1.6608996539792387, "no_speech_prob": 0.3511809706687927}, {"id": 405, "seek": 162716,
  "start": 1627.16, "end": 1630.44, "text": " can mind from certain sources.", "tokens":
  [50364, 393, 1575, 490, 1629, 7139, 13, 50528], "temperature": 0.0, "avg_logprob":
  -0.1821998636773292, "compression_ratio": 1.6742081447963801, "no_speech_prob":
  0.001221410115249455}, {"id": 406, "seek": 162716, "start": 1630.44, "end": 1634.92,
  "text": " But then you can as negative examples, you can pick everything else, right?",
  "tokens": [50528, 583, 550, 291, 393, 382, 3671, 5110, 11, 291, 393, 1888, 1203,
  1646, 11, 558, 30, 50752], "temperature": 0.0, "avg_logprob": -0.1821998636773292,
  "compression_ratio": 1.6742081447963801, "no_speech_prob": 0.001221410115249455},
  {"id": 407, "seek": 162716, "start": 1634.92, "end": 1639.68, "text": " But that
  everything else doesn''t actually count because just to give you an example, let''s",
  "tokens": [50752, 583, 300, 1203, 1646, 1177, 380, 767, 1207, 570, 445, 281, 976,
  291, 364, 1365, 11, 718, 311, 50990], "temperature": 0.0, "avg_logprob": -0.1821998636773292,
  "compression_ratio": 1.6742081447963801, "no_speech_prob": 0.001221410115249455},
  {"id": 408, "seek": 162716, "start": 1639.68, "end": 1644.16, "text": " say when
  I say find full-time job in London, right?", "tokens": [50990, 584, 562, 286, 584,
  915, 1577, 12, 3766, 1691, 294, 7042, 11, 558, 30, 51214], "temperature": 0.0, "avg_logprob":
  -0.1821998636773292, "compression_ratio": 1.6742081447963801, "no_speech_prob":
  0.001221410115249455}, {"id": 409, "seek": 162716, "start": 1644.16, "end": 1647.8000000000002,
  "text": " So that''s just a typical query.", "tokens": [51214, 407, 300, 311, 445,
  257, 7476, 14581, 13, 51396], "temperature": 0.0, "avg_logprob": -0.1821998636773292,
  "compression_ratio": 1.6742081447963801, "no_speech_prob": 0.001221410115249455},
  {"id": 410, "seek": 162716, "start": 1647.8000000000002, "end": 1654.88, "text":
  " You are really interested to find that slightly negative example, which says,
  let''s say,", "tokens": [51396, 509, 366, 534, 3102, 281, 915, 300, 4748, 3671,
  1365, 11, 597, 1619, 11, 718, 311, 584, 11, 51750], "temperature": 0.0, "avg_logprob":
  -0.1821998636773292, "compression_ratio": 1.6742081447963801, "no_speech_prob":
  0.001221410115249455}, {"id": 411, "seek": 165488, "start": 1654.88, "end": 1657.8000000000002,
  "text": " something hours of some office, right?", "tokens": [50364, 746, 2496,
  295, 512, 3398, 11, 558, 30, 50510], "temperature": 0.0, "avg_logprob": -0.1791841578933428,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.13948795199394226},
  {"id": 412, "seek": 165488, "start": 1657.8000000000002, "end": 1660.0400000000002,
  "text": " Which is not about job search anymore.", "tokens": [50510, 3013, 307,
  406, 466, 1691, 3164, 3602, 13, 50622], "temperature": 0.0, "avg_logprob": -0.1791841578933428,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.13948795199394226},
  {"id": 413, "seek": 165488, "start": 1660.0400000000002, "end": 1662.96, "text":
  " It''s about points of interest search, maybe.", "tokens": [50622, 467, 311, 466,
  2793, 295, 1179, 3164, 11, 1310, 13, 50768], "temperature": 0.0, "avg_logprob":
  -0.1791841578933428, "compression_ratio": 1.6538461538461537, "no_speech_prob":
  0.13948795199394226}, {"id": 414, "seek": 165488, "start": 1662.96, "end": 1669.0400000000002,
  "text": " And so you really want to have those examples to see, okay, does your
  model, you know, is", "tokens": [50768, 400, 370, 291, 534, 528, 281, 362, 729,
  5110, 281, 536, 11, 1392, 11, 775, 428, 2316, 11, 291, 458, 11, 307, 51072], "temperature":
  0.0, "avg_logprob": -0.1791841578933428, "compression_ratio": 1.6538461538461537,
  "no_speech_prob": 0.13948795199394226}, {"id": 415, "seek": 165488, "start": 1669.0400000000002,
  "end": 1671.24, "text": " able to differentiate between them?", "tokens": [51072,
  1075, 281, 23203, 1296, 552, 30, 51182], "temperature": 0.0, "avg_logprob": -0.1791841578933428,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.13948795199394226},
  {"id": 416, "seek": 165488, "start": 1671.24, "end": 1679.4, "text": " And I guess
  checklist paper is another example where they go like beyond, you know, imaginary",
  "tokens": [51182, 400, 286, 2041, 30357, 3035, 307, 1071, 1365, 689, 436, 352, 411,
  4399, 11, 291, 458, 11, 26164, 51590], "temperature": 0.0, "avg_logprob": -0.1791841578933428,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.13948795199394226},
  {"id": 417, "seek": 165488, "start": 1679.4, "end": 1683.96, "text": " in a way
  that saying, okay, you can actually fulfill this criteria and you can actually",
  "tokens": [51590, 294, 257, 636, 300, 1566, 11, 1392, 11, 291, 393, 767, 13875,
  341, 11101, 293, 291, 393, 767, 51818], "temperature": 0.0, "avg_logprob": -0.1791841578933428,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.13948795199394226},
  {"id": 418, "seek": 168396, "start": 1683.96, "end": 1687.48, "text": " check your
  model on various, very suspects.", "tokens": [50364, 1520, 428, 2316, 322, 3683,
  11, 588, 35667, 13, 50540], "temperature": 0.0, "avg_logprob": -0.2075612407085324,
  "compression_ratio": 1.7900763358778626, "no_speech_prob": 0.014408075250685215},
  {"id": 419, "seek": 168396, "start": 1687.48, "end": 1688.48, "text": " Right, right.",
  "tokens": [50540, 1779, 11, 558, 13, 50590], "temperature": 0.0, "avg_logprob":
  -0.2075612407085324, "compression_ratio": 1.7900763358778626, "no_speech_prob":
  0.014408075250685215}, {"id": 420, "seek": 168396, "start": 1688.48, "end": 1689.48,
  "text": " Right.", "tokens": [50590, 1779, 13, 50640], "temperature": 0.0, "avg_logprob":
  -0.2075612407085324, "compression_ratio": 1.7900763358778626, "no_speech_prob":
  0.014408075250685215}, {"id": 421, "seek": 168396, "start": 1689.48, "end": 1693.88,
  "text": " And is that something that you like, how did you go about addressing that
  in your research?", "tokens": [50640, 400, 307, 300, 746, 300, 291, 411, 11, 577,
  630, 291, 352, 466, 14329, 300, 294, 428, 2132, 30, 50860], "temperature": 0.0,
  "avg_logprob": -0.2075612407085324, "compression_ratio": 1.7900763358778626, "no_speech_prob":
  0.014408075250685215}, {"id": 422, "seek": 168396, "start": 1693.88, "end": 1699.0,
  "text": " I mean, you know, what we did is that actually, if you look, it was like
  one of the early,", "tokens": [50860, 286, 914, 11, 291, 458, 11, 437, 321, 630,
  307, 300, 767, 11, 498, 291, 574, 11, 309, 390, 411, 472, 295, 264, 2440, 11, 51116],
  "temperature": 0.0, "avg_logprob": -0.2075612407085324, "compression_ratio": 1.7900763358778626,
  "no_speech_prob": 0.014408075250685215}, {"id": 423, "seek": 168396, "start": 1699.0,
  "end": 1703.72, "text": " early papers, you know, the reason I like reading papers
  is because you can bring some", "tokens": [51116, 2440, 10577, 11, 291, 458, 11,
  264, 1778, 286, 411, 3760, 10577, 307, 570, 291, 393, 1565, 512, 51352], "temperature":
  0.0, "avg_logprob": -0.2075612407085324, "compression_ratio": 1.7900763358778626,
  "no_speech_prob": 0.014408075250685215}, {"id": 424, "seek": 168396, "start": 1703.72,
  "end": 1707.0, "text": " ideas from one paper to some other domain.", "tokens":
  [51352, 3487, 490, 472, 3035, 281, 512, 661, 9274, 13, 51516], "temperature": 0.0,
  "avg_logprob": -0.2075612407085324, "compression_ratio": 1.7900763358778626, "no_speech_prob":
  0.014408075250685215}, {"id": 425, "seek": 168396, "start": 1707.0, "end": 1712.1200000000001,
  "text": " And so the paper was about sentiment analysis where one of the challenge
  was back then when", "tokens": [51516, 400, 370, 264, 3035, 390, 466, 16149, 5215,
  689, 472, 295, 264, 3430, 390, 646, 550, 562, 51772], "temperature": 0.0, "avg_logprob":
  -0.2075612407085324, "compression_ratio": 1.7900763358778626, "no_speech_prob":
  0.014408075250685215}, {"id": 426, "seek": 171212, "start": 1712.12, "end": 1716.6,
  "text": " it was dictionary-based systems, you know, how do I expand my positive
  dictionary?", "tokens": [50364, 309, 390, 25890, 12, 6032, 3652, 11, 291, 458, 11,
  577, 360, 286, 5268, 452, 3353, 25890, 30, 50588], "temperature": 0.0, "avg_logprob":
  -0.15576336509303043, "compression_ratio": 1.824390243902439, "no_speech_prob":
  0.006721757352352142}, {"id": 427, "seek": 171212, "start": 1716.6, "end": 1719.08,
  "text": " How do I expand my negative dictionary?", "tokens": [50588, 1012, 360,
  286, 5268, 452, 3671, 25890, 30, 50712], "temperature": 0.0, "avg_logprob": -0.15576336509303043,
  "compression_ratio": 1.824390243902439, "no_speech_prob": 0.006721757352352142},
  {"id": 428, "seek": 171212, "start": 1719.08, "end": 1725.28, "text": " And what
  they propose there is that you can use a retrieval system where you say, okay,",
  "tokens": [50712, 400, 437, 436, 17421, 456, 307, 300, 291, 393, 764, 257, 19817,
  3337, 1185, 689, 291, 584, 11, 1392, 11, 51022], "temperature": 0.0, "avg_logprob":
  -0.15576336509303043, "compression_ratio": 1.824390243902439, "no_speech_prob":
  0.006721757352352142}, {"id": 429, "seek": 171212, "start": 1725.28, "end": 1732.0,
  "text": " you take an instance from a positive dictionary, let''s say it''s good,
  okay.", "tokens": [51022, 291, 747, 364, 5197, 490, 257, 3353, 25890, 11, 718, 311,
  584, 309, 311, 665, 11, 1392, 13, 51358], "temperature": 0.0, "avg_logprob": -0.15576336509303043,
  "compression_ratio": 1.824390243902439, "no_speech_prob": 0.006721757352352142},
  {"id": 430, "seek": 171212, "start": 1732.0, "end": 1738.52, "text": " And then
  you search with a pattern where you say good and then a blank and you just let",
  "tokens": [51358, 400, 550, 291, 3164, 365, 257, 5102, 689, 291, 584, 665, 293,
  550, 257, 8247, 293, 291, 445, 718, 51684], "temperature": 0.0, "avg_logprob": -0.15576336509303043,
  "compression_ratio": 1.824390243902439, "no_speech_prob": 0.006721757352352142},
  {"id": 431, "seek": 173852, "start": 1738.52, "end": 1745.24, "text": " your search
  engine tell you what good is occurring with in the sentences or text, right?", "tokens":
  [50364, 428, 3164, 2848, 980, 291, 437, 665, 307, 18386, 365, 294, 264, 16579, 420,
  2487, 11, 558, 30, 50700], "temperature": 0.0, "avg_logprob": -0.17335914682458947,
  "compression_ratio": 1.6784313725490196, "no_speech_prob": 0.006699309218674898},
  {"id": 432, "seek": 173852, "start": 1745.24, "end": 1746.84, "text": " And the
  same for the bad one.", "tokens": [50700, 400, 264, 912, 337, 264, 1578, 472, 13,
  50780], "temperature": 0.0, "avg_logprob": -0.17335914682458947, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.006699309218674898}, {"id": 433, "seek":
  173852, "start": 1746.84, "end": 1751.44, "text": " Then they run some clustering
  on it so that you can actually pick more representative items", "tokens": [50780,
  1396, 436, 1190, 512, 596, 48673, 322, 309, 370, 300, 291, 393, 767, 1888, 544,
  12424, 4754, 51010], "temperature": 0.0, "avg_logprob": -0.17335914682458947, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.006699309218674898}, {"id": 434, "seek":
  173852, "start": 1751.44, "end": 1752.92, "text": " from your data set.", "tokens":
  [51010, 490, 428, 1412, 992, 13, 51084], "temperature": 0.0, "avg_logprob": -0.17335914682458947,
  "compression_ratio": 1.6784313725490196, "no_speech_prob": 0.006699309218674898},
  {"id": 435, "seek": 173852, "start": 1752.92, "end": 1757.56, "text": " And in principle,
  you could apply a similar technique with the job queries, right?", "tokens": [51084,
  400, 294, 8665, 11, 291, 727, 3079, 257, 2531, 6532, 365, 264, 1691, 24109, 11,
  558, 30, 51316], "temperature": 0.0, "avg_logprob": -0.17335914682458947, "compression_ratio":
  1.6784313725490196, "no_speech_prob": 0.006699309218674898}, {"id": 436, "seek":
  173852, "start": 1757.56, "end": 1764.96, "text": " And we didn''t go that far,
  but we actually did try to use our own search engine to essentially,", "tokens":
  [51316, 400, 321, 994, 380, 352, 300, 1400, 11, 457, 321, 767, 630, 853, 281, 764,
  527, 1065, 3164, 2848, 281, 4476, 11, 51686], "temperature": 0.0, "avg_logprob":
  -0.17335914682458947, "compression_ratio": 1.6784313725490196, "no_speech_prob":
  0.006699309218674898}, {"id": 437, "seek": 173852, "start": 1764.96, "end": 1767.72,
  "text": " you know, augment.", "tokens": [51686, 291, 458, 11, 29919, 13, 51824],
  "temperature": 0.0, "avg_logprob": -0.17335914682458947, "compression_ratio": 1.6784313725490196,
  "no_speech_prob": 0.006699309218674898}, {"id": 438, "seek": 176772, "start": 1767.72,
  "end": 1771.1200000000001, "text": " And then there''s another potential technique
  that might help their short of introducing", "tokens": [50364, 400, 550, 456, 311,
  1071, 3995, 6532, 300, 1062, 854, 641, 2099, 295, 15424, 50534], "temperature":
  0.0, "avg_logprob": -0.219615770422894, "compression_ratio": 2.0, "no_speech_prob":
  0.020148206502199173}, {"id": 439, "seek": 176772, "start": 1771.1200000000001,
  "end": 1772.1200000000001, "text": " hard negatives.", "tokens": [50534, 1152, 40019,
  13, 50584], "temperature": 0.0, "avg_logprob": -0.219615770422894, "compression_ratio":
  2.0, "no_speech_prob": 0.020148206502199173}, {"id": 440, "seek": 176772, "start":
  1772.1200000000001, "end": 1776.92, "text": " It''s easier than introducing hard
  negatives just to add like what they call a margin loss,", "tokens": [50584, 467,
  311, 3571, 813, 15424, 1152, 40019, 445, 281, 909, 411, 437, 436, 818, 257, 10270,
  4470, 11, 50824], "temperature": 0.0, "avg_logprob": -0.219615770422894, "compression_ratio":
  2.0, "no_speech_prob": 0.020148206502199173}, {"id": 441, "seek": 176772, "start":
  1776.92, "end": 1781.72, "text": " which is to essentially just say that the separation
  in the score that the neural network", "tokens": [50824, 597, 307, 281, 4476, 445,
  584, 300, 264, 14634, 294, 264, 6175, 300, 264, 18161, 3209, 51064], "temperature":
  0.0, "avg_logprob": -0.219615770422894, "compression_ratio": 2.0, "no_speech_prob":
  0.020148206502199173}, {"id": 442, "seek": 176772, "start": 1781.72, "end": 1787.44,
  "text": " assign the positive example versus the negative examples has to be large.",
  "tokens": [51064, 6269, 264, 3353, 1365, 5717, 264, 3671, 5110, 575, 281, 312, 2416,
  13, 51350], "temperature": 0.0, "avg_logprob": -0.219615770422894, "compression_ratio":
  2.0, "no_speech_prob": 0.020148206502199173}, {"id": 443, "seek": 176772, "start":
  1787.44, "end": 1792.96, "text": " So you sign some lambda and it has to be, essentially,
  you handicap the scores of the positive", "tokens": [51350, 407, 291, 1465, 512,
  13607, 293, 309, 575, 281, 312, 11, 4476, 11, 291, 45975, 264, 13444, 295, 264,
  3353, 51626], "temperature": 0.0, "avg_logprob": -0.219615770422894, "compression_ratio":
  2.0, "no_speech_prob": 0.020148206502199173}, {"id": 444, "seek": 176772, "start":
  1792.96, "end": 1797.2, "text": " examples by that lambda and it forces the neural
  network to introduce more separation.", "tokens": [51626, 5110, 538, 300, 13607,
  293, 309, 5874, 264, 18161, 3209, 281, 5366, 544, 14634, 13, 51838], "temperature":
  0.0, "avg_logprob": -0.219615770422894, "compression_ratio": 2.0, "no_speech_prob":
  0.020148206502199173}, {"id": 445, "seek": 179720, "start": 1797.2, "end": 1802.2,
  "text": " So sometimes that can be helpful, even if you haven''t generated hard
  negatives.", "tokens": [50364, 407, 2171, 300, 393, 312, 4961, 11, 754, 498, 291,
  2378, 380, 10833, 1152, 40019, 13, 50614], "temperature": 0.0, "avg_logprob": -0.23219970294407435,
  "compression_ratio": 1.6074074074074074, "no_speech_prob": 0.0014588504564017057},
  {"id": 446, "seek": 179720, "start": 1802.2, "end": 1805.3600000000001, "text":
  " Yeah, yeah, absolutely.", "tokens": [50614, 865, 11, 1338, 11, 3122, 13, 50772],
  "temperature": 0.0, "avg_logprob": -0.23219970294407435, "compression_ratio": 1.6074074074074074,
  "no_speech_prob": 0.0014588504564017057}, {"id": 447, "seek": 179720, "start": 1805.3600000000001,
  "end": 1810.3600000000001, "text": " Maybe we can also cite some papers in this
  podcast, you know, like especially you mentioned", "tokens": [50772, 2704, 321,
  393, 611, 37771, 512, 10577, 294, 341, 7367, 11, 291, 458, 11, 411, 2318, 291, 2835,
  51022], "temperature": 0.0, "avg_logprob": -0.23219970294407435, "compression_ratio":
  1.6074074074074074, "no_speech_prob": 0.0014588504564017057}, {"id": 448, "seek":
  179720, "start": 1810.3600000000001, "end": 1811.3600000000001, "text": " some papers.",
  "tokens": [51022, 512, 10577, 13, 51072], "temperature": 0.0, "avg_logprob": -0.23219970294407435,
  "compression_ratio": 1.6074074074074074, "no_speech_prob": 0.0014588504564017057},
  {"id": 449, "seek": 179720, "start": 1811.3600000000001, "end": 1816.24, "text":
  " And I will try to find this sentiment analysis paper, although I think it''s probably
  like", "tokens": [51072, 400, 286, 486, 853, 281, 915, 341, 16149, 5215, 3035, 11,
  4878, 286, 519, 309, 311, 1391, 411, 51316], "temperature": 0.0, "avg_logprob":
  -0.23219970294407435, "compression_ratio": 1.6074074074074074, "no_speech_prob":
  0.0014588504564017057}, {"id": 450, "seek": 179720, "start": 1816.24, "end": 1819.52,
  "text": " five, six years old or maybe even older.", "tokens": [51316, 1732, 11,
  2309, 924, 1331, 420, 1310, 754, 4906, 13, 51480], "temperature": 0.0, "avg_logprob":
  -0.23219970294407435, "compression_ratio": 1.6074074074074074, "no_speech_prob":
  0.0014588504564017057}, {"id": 451, "seek": 179720, "start": 1819.52, "end": 1822.6000000000001,
  "text": " But I mean, this idea is still live forward, I think.", "tokens": [51480,
  583, 286, 914, 11, 341, 1558, 307, 920, 1621, 2128, 11, 286, 519, 13, 51634], "temperature":
  0.0, "avg_logprob": -0.23219970294407435, "compression_ratio": 1.6074074074074074,
  "no_speech_prob": 0.0014588504564017057}, {"id": 452, "seek": 179720, "start": 1822.6000000000001,
  "end": 1825.88, "text": " And like we shouldn''t forget about them.", "tokens":
  [51634, 400, 411, 321, 4659, 380, 2870, 466, 552, 13, 51798], "temperature": 0.0,
  "avg_logprob": -0.23219970294407435, "compression_ratio": 1.6074074074074074, "no_speech_prob":
  0.0014588504564017057}, {"id": 453, "seek": 182588, "start": 1825.88, "end": 1836.3200000000002,
  "text": " And if we go back to your product, so basically, like you said that you
  also kind of look", "tokens": [50364, 400, 498, 321, 352, 646, 281, 428, 1674, 11,
  370, 1936, 11, 411, 291, 848, 300, 291, 611, 733, 295, 574, 50886], "temperature":
  0.0, "avg_logprob": -0.2596008555094401, "compression_ratio": 1.510752688172043,
  "no_speech_prob": 0.008051185868680477}, {"id": 454, "seek": 182588, "start": 1836.3200000000002,
  "end": 1842.0, "text": " at using some of the existing algorithms in vector search,
  can you name them?", "tokens": [50886, 412, 1228, 512, 295, 264, 6741, 14642, 294,
  8062, 3164, 11, 393, 291, 1315, 552, 30, 51170], "temperature": 0.0, "avg_logprob":
  -0.2596008555094401, "compression_ratio": 1.510752688172043, "no_speech_prob": 0.008051185868680477},
  {"id": 455, "seek": 182588, "start": 1842.0, "end": 1846.2, "text": " Or is this
  some kind of secret or are you customizing them as well?", "tokens": [51170, 1610,
  307, 341, 512, 733, 295, 4054, 420, 366, 291, 2375, 3319, 552, 382, 731, 30, 51380],
  "temperature": 0.0, "avg_logprob": -0.2596008555094401, "compression_ratio": 1.510752688172043,
  "no_speech_prob": 0.008051185868680477}, {"id": 456, "seek": 182588, "start": 1846.2,
  "end": 1849.4, "text": " So for the vector search, specifically.", "tokens": [51380,
  407, 337, 264, 8062, 3164, 11, 4682, 13, 51540], "temperature": 0.0, "avg_logprob":
  -0.2596008555094401, "compression_ratio": 1.510752688172043, "no_speech_prob": 0.008051185868680477},
  {"id": 457, "seek": 182588, "start": 1849.4, "end": 1850.4, "text": " Yeah.", "tokens":
  [51540, 865, 13, 51590], "temperature": 0.0, "avg_logprob": -0.2596008555094401,
  "compression_ratio": 1.510752688172043, "no_speech_prob": 0.008051185868680477},
  {"id": 458, "seek": 185040, "start": 1850.92, "end": 1857.96, "text": " I think
  we can say that we know we at our core, we do take advantage of phase or fire.",
  "tokens": [50390, 286, 519, 321, 393, 584, 300, 321, 458, 321, 412, 527, 4965, 11,
  321, 360, 747, 5002, 295, 5574, 420, 2610, 13, 50742], "temperature": 0.0, "avg_logprob":
  -0.36677643625359785, "compression_ratio": 1.5330396475770924, "no_speech_prob":
  0.12372417002916336}, {"id": 459, "seek": 185040, "start": 1857.96, "end": 1858.96,
  "text": " So I''m not exactly right.", "tokens": [50742, 407, 286, 478, 406, 2293,
  558, 13, 50792], "temperature": 0.0, "avg_logprob": -0.36677643625359785, "compression_ratio":
  1.5330396475770924, "no_speech_prob": 0.12372417002916336}, {"id": 460, "seek":
  185040, "start": 1858.96, "end": 1859.96, "text": " I don''t pronounce that from.",
  "tokens": [50792, 286, 500, 380, 19567, 300, 490, 13, 50842], "temperature": 0.0,
  "avg_logprob": -0.36677643625359785, "compression_ratio": 1.5330396475770924, "no_speech_prob":
  0.12372417002916336}, {"id": 461, "seek": 185040, "start": 1859.96, "end": 1860.96,
  "text": " No, but nobody knows.", "tokens": [50842, 883, 11, 457, 5079, 3255, 13,
  50892], "temperature": 0.0, "avg_logprob": -0.36677643625359785, "compression_ratio":
  1.5330396475770924, "no_speech_prob": 0.12372417002916336}, {"id": 462, "seek":
  185040, "start": 1860.96, "end": 1864.3600000000001, "text": " I think everyone
  says they own weight.", "tokens": [50892, 286, 519, 1518, 1619, 436, 1065, 3364,
  13, 51062], "temperature": 0.0, "avg_logprob": -0.36677643625359785, "compression_ratio":
  1.5330396475770924, "no_speech_prob": 0.12372417002916336}, {"id": 463, "seek":
  185040, "start": 1864.3600000000001, "end": 1872.2800000000002, "text": " In my
  opinion, it''s just an excellently designed system with a team that''s actively
  maintaining", "tokens": [51062, 682, 452, 4800, 11, 309, 311, 445, 364, 45817, 2276,
  4761, 1185, 365, 257, 1469, 300, 311, 13022, 14916, 51458], "temperature": 0.0,
  "avg_logprob": -0.36677643625359785, "compression_ratio": 1.5330396475770924, "no_speech_prob":
  0.12372417002916336}, {"id": 464, "seek": 185040, "start": 1872.2800000000002, "end":
  1876.44, "text": " it and there are obviously experts in that field.", "tokens":
  [51458, 309, 293, 456, 366, 2745, 8572, 294, 300, 2519, 13, 51666], "temperature":
  0.0, "avg_logprob": -0.36677643625359785, "compression_ratio": 1.5330396475770924,
  "no_speech_prob": 0.12372417002916336}, {"id": 465, "seek": 187644, "start": 1876.44,
  "end": 1885.72, "text": " One of the features that customers have requested from
  us is the ability to mix in predicate", "tokens": [50364, 1485, 295, 264, 4122,
  300, 4581, 362, 16436, 490, 505, 307, 264, 3485, 281, 2890, 294, 3852, 8700, 50828],
  "temperature": 0.0, "avg_logprob": -0.2067992023585998, "compression_ratio": 1.6736401673640167,
  "no_speech_prob": 0.04804878681898117}, {"id": 466, "seek": 187644, "start": 1885.72,
  "end": 1887.88, "text": " predicates and traditional Boolean logic.", "tokens":
  [50828, 47336, 1024, 293, 5164, 23351, 28499, 9952, 13, 50936], "temperature": 0.0,
  "avg_logprob": -0.2067992023585998, "compression_ratio": 1.6736401673640167, "no_speech_prob":
  0.04804878681898117}, {"id": 467, "seek": 187644, "start": 1887.88, "end": 1893.0800000000002,
  "text": " So you might have this corpus of documents and they all have this, every
  document has", "tokens": [50936, 407, 291, 1062, 362, 341, 1181, 31624, 295, 8512,
  293, 436, 439, 362, 341, 11, 633, 4166, 575, 51196], "temperature": 0.0, "avg_logprob":
  -0.2067992023585998, "compression_ratio": 1.6736401673640167, "no_speech_prob":
  0.04804878681898117}, {"id": 468, "seek": 187644, "start": 1893.0800000000002, "end":
  1895.68, "text": " this metadata, which is the date it was published.", "tokens":
  [51196, 341, 26603, 11, 597, 307, 264, 4002, 309, 390, 6572, 13, 51326], "temperature":
  0.0, "avg_logprob": -0.2067992023585998, "compression_ratio": 1.6736401673640167,
  "no_speech_prob": 0.04804878681898117}, {"id": 469, "seek": 187644, "start": 1895.68,
  "end": 1898.48, "text": " And then you might want to say, okay, give me the most
  relevant matches for the query,", "tokens": [51326, 400, 550, 291, 1062, 528, 281,
  584, 11, 1392, 11, 976, 385, 264, 881, 7340, 10676, 337, 264, 14581, 11, 51466],
  "temperature": 0.0, "avg_logprob": -0.2067992023585998, "compression_ratio": 1.6736401673640167,
  "no_speech_prob": 0.04804878681898117}, {"id": 470, "seek": 187644, "start": 1898.48,
  "end": 1901.56, "text": " but only for documents published in 2021.", "tokens":
  [51466, 457, 787, 337, 8512, 6572, 294, 7201, 13, 51620], "temperature": 0.0, "avg_logprob":
  -0.2067992023585998, "compression_ratio": 1.6736401673640167, "no_speech_prob":
  0.04804878681898117}, {"id": 471, "seek": 190156, "start": 1901.56, "end": 1907.84,
  "text": " This is like a very crisp selection criteria and this selects a subset
  of the corpus.", "tokens": [50364, 639, 307, 411, 257, 588, 22952, 9450, 11101,
  293, 341, 3048, 82, 257, 25993, 295, 264, 1181, 31624, 13, 50678], "temperature":
  0.0, "avg_logprob": -0.2956766278556224, "compression_ratio": 1.5619469026548674,
  "no_speech_prob": 0.009947966784238815}, {"id": 472, "seek": 190156, "start": 1907.84,
  "end": 1914.2, "text": " So this is actually something that we have not launched
  yet, but we''ve been actively working", "tokens": [50678, 407, 341, 307, 767, 746,
  300, 321, 362, 406, 8730, 1939, 11, 457, 321, 600, 668, 13022, 1364, 50996], "temperature":
  0.0, "avg_logprob": -0.2956766278556224, "compression_ratio": 1.5619469026548674,
  "no_speech_prob": 0.009947966784238815}, {"id": 473, "seek": 190156, "start": 1914.2,
  "end": 1917.28, "text": " on and will probably launch in Q1.", "tokens": [50996,
  322, 293, 486, 1391, 4025, 294, 1249, 16, 13, 51150], "temperature": 0.0, "avg_logprob":
  -0.2956766278556224, "compression_ratio": 1.5619469026548674, "no_speech_prob":
  0.009947966784238815}, {"id": 474, "seek": 190156, "start": 1917.28, "end": 1926.3999999999999,
  "text": " I believe, I recently added the support Google vertex matching engine,
  I think, is a recent", "tokens": [51150, 286, 1697, 11, 286, 3938, 3869, 264, 1406,
  3329, 28162, 14324, 2848, 11, 286, 519, 11, 307, 257, 5162, 51606], "temperature":
  0.0, "avg_logprob": -0.2956766278556224, "compression_ratio": 1.5619469026548674,
  "no_speech_prob": 0.009947966784238815}, {"id": 475, "seek": 190156, "start": 1926.3999999999999,
  "end": 1927.3999999999999, "text": " offering.", "tokens": [51606, 8745, 13, 51656],
  "temperature": 0.0, "avg_logprob": -0.2956766278556224, "compression_ratio": 1.5619469026548674,
  "no_speech_prob": 0.009947966784238815}, {"id": 476, "seek": 190156, "start": 1927.3999999999999,
  "end": 1929.3999999999999, "text": " They also claim to have this support.", "tokens":
  [51656, 814, 611, 3932, 281, 362, 341, 1406, 13, 51756], "temperature": 0.0, "avg_logprob":
  -0.2956766278556224, "compression_ratio": 1.5619469026548674, "no_speech_prob":
  0.009947966784238815}, {"id": 477, "seek": 192940, "start": 1929.4, "end": 1932.16,
  "text": " It''s important, many of our customers have asked for the same thing.",
  "tokens": [50364, 467, 311, 1021, 11, 867, 295, 527, 4581, 362, 2351, 337, 264,
  912, 551, 13, 50502], "temperature": 0.0, "avg_logprob": -0.28342952284702033, "compression_ratio":
  1.6223776223776223, "no_speech_prob": 0.04829133301973343}, {"id": 478, "seek":
  192940, "start": 1932.16, "end": 1939.0, "text": " So we''ve started from a FIAS,
  but we have been customizing it.", "tokens": [50502, 407, 321, 600, 1409, 490, 257,
  479, 40, 3160, 11, 457, 321, 362, 668, 2375, 3319, 309, 13, 50844], "temperature":
  0.0, "avg_logprob": -0.28342952284702033, "compression_ratio": 1.6223776223776223,
  "no_speech_prob": 0.04829133301973343}, {"id": 479, "seek": 192940, "start": 1939.0,
  "end": 1940.2, "text": " Yeah, yeah, sounds good.", "tokens": [50844, 865, 11, 1338,
  11, 3263, 665, 13, 50904], "temperature": 0.0, "avg_logprob": -0.28342952284702033,
  "compression_ratio": 1.6223776223776223, "no_speech_prob": 0.04829133301973343},
  {"id": 480, "seek": 192940, "start": 1940.2, "end": 1945.16, "text": " So basically
  some other companies call it symbolic filtering and that''s what I think you", "tokens":
  [50904, 407, 1936, 512, 661, 3431, 818, 309, 25755, 30822, 293, 300, 311, 437, 286,
  519, 291, 51152], "temperature": 0.0, "avg_logprob": -0.28342952284702033, "compression_ratio":
  1.6223776223776223, "no_speech_prob": 0.04829133301973343}, {"id": 481, "seek":
  192940, "start": 1945.16, "end": 1946.16, "text": " refer to, right?", "tokens":
  [51152, 2864, 281, 11, 558, 30, 51202], "temperature": 0.0, "avg_logprob": -0.28342952284702033,
  "compression_ratio": 1.6223776223776223, "no_speech_prob": 0.04829133301973343},
  {"id": 482, "seek": 192940, "start": 1946.16, "end": 1951.16, "text": " So I can
  have certain categorical variables, so to say in my data and I can filter by it,",
  "tokens": [51202, 407, 286, 393, 362, 1629, 19250, 804, 9102, 11, 370, 281, 584,
  294, 452, 1412, 293, 286, 393, 6608, 538, 309, 11, 51452], "temperature": 0.0, "avg_logprob":
  -0.28342952284702033, "compression_ratio": 1.6223776223776223, "no_speech_prob":
  0.04829133301973343}, {"id": 483, "seek": 192940, "start": 1951.16, "end": 1952.16,
  "text": " right?", "tokens": [51452, 558, 30, 51502], "temperature": 0.0, "avg_logprob":
  -0.28342952284702033, "compression_ratio": 1.6223776223776223, "no_speech_prob":
  0.04829133301973343}, {"id": 484, "seek": 192940, "start": 1952.16, "end": 1953.16,
  "text": " Exactly, right.", "tokens": [51502, 7587, 11, 558, 13, 51552], "temperature":
  0.0, "avg_logprob": -0.28342952284702033, "compression_ratio": 1.6223776223776223,
  "no_speech_prob": 0.04829133301973343}, {"id": 485, "seek": 192940, "start": 1953.16,
  "end": 1958.76, "text": " Yeah, so I think vanilla fires of face doesn''t have this
  functionality as far as I know.", "tokens": [51552, 865, 11, 370, 286, 519, 17528,
  15044, 295, 1851, 1177, 380, 362, 341, 14980, 382, 1400, 382, 286, 458, 13, 51832],
  "temperature": 0.0, "avg_logprob": -0.28342952284702033, "compression_ratio": 1.6223776223776223,
  "no_speech_prob": 0.04829133301973343}, {"id": 486, "seek": 195876, "start": 1958.76,
  "end": 1961.16, "text": " And so essentially you''ll have to kind of extend it.",
  "tokens": [50364, 400, 370, 4476, 291, 603, 362, 281, 733, 295, 10101, 309, 13,
  50484], "temperature": 0.0, "avg_logprob": -0.1534564899948408, "compression_ratio":
  1.6216216216216217, "no_speech_prob": 0.0035870415158569813}, {"id": 487, "seek":
  195876, "start": 1961.16, "end": 1965.32, "text": " And do you plan to keep it to
  yourself, which is perfectly fine, or are you also able", "tokens": [50484, 400,
  360, 291, 1393, 281, 1066, 309, 281, 1803, 11, 597, 307, 6239, 2489, 11, 420, 366,
  291, 611, 1075, 50692], "temperature": 0.0, "avg_logprob": -0.1534564899948408,
  "compression_ratio": 1.6216216216216217, "no_speech_prob": 0.0035870415158569813},
  {"id": 488, "seek": 195876, "start": 1965.32, "end": 1972.12, "text": " to contribute
  it back to the FIAS open source project?", "tokens": [50692, 281, 10586, 309, 646,
  281, 264, 479, 40, 3160, 1269, 4009, 1716, 30, 51032], "temperature": 0.0, "avg_logprob":
  -0.1534564899948408, "compression_ratio": 1.6216216216216217, "no_speech_prob":
  0.0035870415158569813}, {"id": 489, "seek": 195876, "start": 1972.12, "end": 1977.16,
  "text": " So I think what I''ve noticed about the authors of FIAS is that they want
  to keep the product", "tokens": [51032, 407, 286, 519, 437, 286, 600, 5694, 466,
  264, 16552, 295, 479, 40, 3160, 307, 300, 436, 528, 281, 1066, 264, 1674, 51284],
  "temperature": 0.0, "avg_logprob": -0.1534564899948408, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.0035870415158569813}, {"id": 490, "seek": 195876, "start": 1977.16,
  "end": 1981.28, "text": " very focused on being a first class vector engine.", "tokens":
  [51284, 588, 5178, 322, 885, 257, 700, 1508, 8062, 2848, 13, 51490], "temperature":
  0.0, "avg_logprob": -0.1534564899948408, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.0035870415158569813}, {"id": 491, "seek": 195876, "start": 1981.28,
  "end": 1986.52, "text": " And these are essentially augmentations that they''re
  not interested in pulling in.", "tokens": [51490, 400, 613, 366, 4476, 29919, 763,
  300, 436, 434, 406, 3102, 294, 8407, 294, 13, 51752], "temperature": 0.0, "avg_logprob":
  -0.1534564899948408, "compression_ratio": 1.6216216216216217, "no_speech_prob":
  0.0035870415158569813}, {"id": 492, "seek": 198652, "start": 1986.52, "end": 1992.2,
  "text": " And I think they would see it as scope creep, which is probably fair.",
  "tokens": [50364, 400, 286, 519, 436, 576, 536, 309, 382, 11923, 9626, 11, 597,
  307, 1391, 3143, 13, 50648], "temperature": 0.0, "avg_logprob": -0.218062345798199,
  "compression_ratio": 1.7581967213114753, "no_speech_prob": 0.0031924243085086346},
  {"id": 493, "seek": 198652, "start": 1992.2, "end": 1995.2, "text": " That said,
  would we contribute it as open source?", "tokens": [50648, 663, 848, 11, 576, 321,
  10586, 309, 382, 1269, 4009, 30, 50798], "temperature": 0.0, "avg_logprob": -0.218062345798199,
  "compression_ratio": 1.7581967213114753, "no_speech_prob": 0.0031924243085086346},
  {"id": 494, "seek": 198652, "start": 1995.2, "end": 1998.0, "text": " Like we could
  still contribute it back as open source.", "tokens": [50798, 1743, 321, 727, 920,
  10586, 309, 646, 382, 1269, 4009, 13, 50938], "temperature": 0.0, "avg_logprob":
  -0.218062345798199, "compression_ratio": 1.7581967213114753, "no_speech_prob": 0.0031924243085086346},
  {"id": 495, "seek": 198652, "start": 1998.0, "end": 2002.0, "text": " In fact, down
  the line we could potentially make our entire stack open source.", "tokens": [50938,
  682, 1186, 11, 760, 264, 1622, 321, 727, 7263, 652, 527, 2302, 8630, 1269, 4009,
  13, 51138], "temperature": 0.0, "avg_logprob": -0.218062345798199, "compression_ratio":
  1.7581967213114753, "no_speech_prob": 0.0031924243085086346}, {"id": 496, "seek":
  198652, "start": 2002.0, "end": 2010.4, "text": " I think some of the abusiveness
  of that, say, in regards to elastic and how it''s worked,", "tokens": [51138, 286,
  519, 512, 295, 264, 48819, 8477, 295, 300, 11, 584, 11, 294, 14258, 281, 17115,
  293, 577, 309, 311, 2732, 11, 51558], "temperature": 0.0, "avg_logprob": -0.218062345798199,
  "compression_ratio": 1.7581967213114753, "no_speech_prob": 0.0031924243085086346},
  {"id": 497, "seek": 198652, "start": 2010.4, "end": 2014.08, "text": " where you
  have these very large companies that essentially contribute very little, but", "tokens":
  [51558, 689, 291, 362, 613, 588, 2416, 3431, 300, 4476, 10586, 588, 707, 11, 457,
  51742], "temperature": 0.0, "avg_logprob": -0.218062345798199, "compression_ratio":
  1.7581967213114753, "no_speech_prob": 0.0031924243085086346}, {"id": 498, "seek":
  201408, "start": 2014.08, "end": 2022.0, "text": " they take advantage of their
  ability to launch platforms as a service like Amazon can.", "tokens": [50364, 436,
  747, 5002, 295, 641, 3485, 281, 4025, 9473, 382, 257, 2643, 411, 6795, 393, 13,
  50760], "temperature": 0.0, "avg_logprob": -0.29417976379394534, "compression_ratio":
  1.5254901960784313, "no_speech_prob": 0.014069268479943275}, {"id": 499, "seek":
  201408, "start": 2022.0, "end": 2023.8, "text": " That''s kind of scared us.", "tokens":
  [50760, 663, 311, 733, 295, 5338, 505, 13, 50850], "temperature": 0.0, "avg_logprob":
  -0.29417976379394534, "compression_ratio": 1.5254901960784313, "no_speech_prob":
  0.014069268479943275}, {"id": 500, "seek": 201408, "start": 2023.8, "end": 2028.36,
  "text": " I think in the short term, we''re not doing that, but that''s certainly
  something we could", "tokens": [50850, 286, 519, 294, 264, 2099, 1433, 11, 321,
  434, 406, 884, 300, 11, 457, 300, 311, 3297, 746, 321, 727, 51078], "temperature":
  0.0, "avg_logprob": -0.29417976379394534, "compression_ratio": 1.5254901960784313,
  "no_speech_prob": 0.014069268479943275}, {"id": 501, "seek": 201408, "start": 2028.36,
  "end": 2030.56, "text": " plan on doing in the longer term.", "tokens": [51078,
  1393, 322, 884, 294, 264, 2854, 1433, 13, 51188], "temperature": 0.0, "avg_logprob":
  -0.29417976379394534, "compression_ratio": 1.5254901960784313, "no_speech_prob":
  0.014069268479943275}, {"id": 502, "seek": 201408, "start": 2030.56, "end": 2031.56,
  "text": " Yeah.", "tokens": [51188, 865, 13, 51238], "temperature": 0.0, "avg_logprob":
  -0.29417976379394534, "compression_ratio": 1.5254901960784313, "no_speech_prob":
  0.014069268479943275}, {"id": 503, "seek": 201408, "start": 2031.56, "end": 2038.04,
  "text": " And I mean, of course, the dynamics of open source is not necessarily
  solved, especially as", "tokens": [51238, 400, 286, 914, 11, 295, 1164, 11, 264,
  15679, 295, 1269, 4009, 307, 406, 4725, 13041, 11, 2318, 382, 51562], "temperature":
  0.0, "avg_logprob": -0.29417976379394534, "compression_ratio": 1.5254901960784313,
  "no_speech_prob": 0.014069268479943275}, {"id": 504, "seek": 201408, "start": 2038.04,
  "end": 2040.48, "text": " you''ve brought up this example with the elastic, right?",
  "tokens": [51562, 291, 600, 3038, 493, 341, 1365, 365, 264, 17115, 11, 558, 30,
  51684], "temperature": 0.0, "avg_logprob": -0.29417976379394534, "compression_ratio":
  1.5254901960784313, "no_speech_prob": 0.014069268479943275}, {"id": 505, "seek":
  204048, "start": 2040.48, "end": 2044.8, "text": " And they''re kind of battle between
  elastic and Amazon.", "tokens": [50364, 400, 436, 434, 733, 295, 4635, 1296, 17115,
  293, 6795, 13, 50580], "temperature": 0.0, "avg_logprob": -0.22550853836202175,
  "compression_ratio": 1.6108949416342413, "no_speech_prob": 0.043774936348199844},
  {"id": 506, "seek": 204048, "start": 2044.8, "end": 2049.8, "text": " But like for
  some companies, it still works as a starter.", "tokens": [50580, 583, 411, 337,
  512, 3431, 11, 309, 920, 1985, 382, 257, 22465, 13, 50830], "temperature": 0.0,
  "avg_logprob": -0.22550853836202175, "compression_ratio": 1.6108949416342413, "no_speech_prob":
  0.043774936348199844}, {"id": 507, "seek": 204048, "start": 2049.8, "end": 2051.6,
  "text": " You can enter this community.", "tokens": [50830, 509, 393, 3242, 341,
  1768, 13, 50920], "temperature": 0.0, "avg_logprob": -0.22550853836202175, "compression_ratio":
  1.6108949416342413, "no_speech_prob": 0.043774936348199844}, {"id": 508, "seek":
  204048, "start": 2051.6, "end": 2053.8, "text": " You start building the community
  around you.", "tokens": [50920, 509, 722, 2390, 264, 1768, 926, 291, 13, 51030],
  "temperature": 0.0, "avg_logprob": -0.22550853836202175, "compression_ratio": 1.6108949416342413,
  "no_speech_prob": 0.043774936348199844}, {"id": 509, "seek": 204048, "start": 2053.8,
  "end": 2055.64, "text": " And so they bring back ideas.", "tokens": [51030, 400,
  370, 436, 1565, 646, 3487, 13, 51122], "temperature": 0.0, "avg_logprob": -0.22550853836202175,
  "compression_ratio": 1.6108949416342413, "no_speech_prob": 0.043774936348199844},
  {"id": 510, "seek": 204048, "start": 2055.64, "end": 2058.52, "text": " They feed
  in new use cases to you.", "tokens": [51122, 814, 3154, 294, 777, 764, 3331, 281,
  291, 13, 51266], "temperature": 0.0, "avg_logprob": -0.22550853836202175, "compression_ratio":
  1.6108949416342413, "no_speech_prob": 0.043774936348199844}, {"id": 511, "seek":
  204048, "start": 2058.52, "end": 2061.4, "text": " And maybe they even implement
  some features, right?", "tokens": [51266, 400, 1310, 436, 754, 4445, 512, 4122,
  11, 558, 30, 51410], "temperature": 0.0, "avg_logprob": -0.22550853836202175, "compression_ratio":
  1.6108949416342413, "no_speech_prob": 0.043774936348199844}, {"id": 512, "seek":
  204048, "start": 2061.4, "end": 2066.92, "text": " And is this something that you''ve
  been thinking as well along these lines?", "tokens": [51410, 400, 307, 341, 746,
  300, 291, 600, 668, 1953, 382, 731, 2051, 613, 3876, 30, 51686], "temperature":
  0.0, "avg_logprob": -0.22550853836202175, "compression_ratio": 1.6108949416342413,
  "no_speech_prob": 0.043774936348199844}, {"id": 513, "seek": 204048, "start": 2066.92,
  "end": 2069.04, "text": " Well, I definitely see your point.", "tokens": [51686,
  1042, 11, 286, 2138, 536, 428, 935, 13, 51792], "temperature": 0.0, "avg_logprob":
  -0.22550853836202175, "compression_ratio": 1.6108949416342413, "no_speech_prob":
  0.043774936348199844}, {"id": 514, "seek": 206904, "start": 2069.04, "end": 2070.04,
  "text": " I definitely see your point.", "tokens": [50364, 286, 2138, 536, 428,
  935, 13, 50414], "temperature": 0.0, "avg_logprob": -0.25695695072771557, "compression_ratio":
  1.526829268292683, "no_speech_prob": 0.0011328626424074173}, {"id": 515, "seek":
  206904, "start": 2070.04, "end": 2078.04, "text": " At the same time, we also do
  have some competition in the space.", "tokens": [50414, 1711, 264, 912, 565, 11,
  321, 611, 360, 362, 512, 6211, 294, 264, 1901, 13, 50814], "temperature": 0.0, "avg_logprob":
  -0.25695695072771557, "compression_ratio": 1.526829268292683, "no_speech_prob":
  0.0011328626424074173}, {"id": 516, "seek": 206904, "start": 2078.04, "end": 2086.32,
  "text": " We''re still in the early days, but 2021, in particular, saw the launch
  of several competitors.", "tokens": [50814, 492, 434, 920, 294, 264, 2440, 1708,
  11, 457, 7201, 11, 294, 1729, 11, 1866, 264, 4025, 295, 2940, 18333, 13, 51228],
  "temperature": 0.0, "avg_logprob": -0.25695695072771557, "compression_ratio": 1.526829268292683,
  "no_speech_prob": 0.0011328626424074173}, {"id": 517, "seek": 206904, "start": 2086.32,
  "end": 2091.12, "text": " And even Microsoft is in the mix now, Microsoft''s semantic
  search.", "tokens": [51228, 400, 754, 8116, 307, 294, 264, 2890, 586, 11, 8116,
  311, 47982, 3164, 13, 51468], "temperature": 0.0, "avg_logprob": -0.25695695072771557,
  "compression_ratio": 1.526829268292683, "no_speech_prob": 0.0011328626424074173},
  {"id": 518, "seek": 206904, "start": 2091.12, "end": 2094.8, "text": " I think it''s
  still in beta, Amazon launch Kendra in 2020.", "tokens": [51468, 286, 519, 309,
  311, 920, 294, 9861, 11, 6795, 4025, 20891, 424, 294, 4808, 13, 51652], "temperature":
  0.0, "avg_logprob": -0.25695695072771557, "compression_ratio": 1.526829268292683,
  "no_speech_prob": 0.0011328626424074173}, {"id": 519, "seek": 209480, "start": 2094.8,
  "end": 2100.1200000000003, "text": " I think that they probably get the credit for
  launching the first platform as a service", "tokens": [50364, 286, 519, 300, 436,
  1391, 483, 264, 5397, 337, 18354, 264, 700, 3663, 382, 257, 2643, 50630], "temperature":
  0.0, "avg_logprob": -0.19223769098265558, "compression_ratio": 1.6779661016949152,
  "no_speech_prob": 0.010225232690572739}, {"id": 520, "seek": 209480, "start": 2100.1200000000003,
  "end": 2102.7200000000003, "text": " neural information retrieval system.", "tokens":
  [50630, 18161, 1589, 19817, 3337, 1185, 13, 50760], "temperature": 0.0, "avg_logprob":
  -0.19223769098265558, "compression_ratio": 1.6779661016949152, "no_speech_prob":
  0.010225232690572739}, {"id": 521, "seek": 209480, "start": 2102.7200000000003,
  "end": 2109.04, "text": " So in both of the cases, both of those systems, by the
  way, I think that they actually are", "tokens": [50760, 407, 294, 1293, 295, 264,
  3331, 11, 1293, 295, 729, 3652, 11, 538, 264, 636, 11, 286, 519, 300, 436, 767,
  366, 51076], "temperature": 0.0, "avg_logprob": -0.19223769098265558, "compression_ratio":
  1.6779661016949152, "no_speech_prob": 0.010225232690572739}, {"id": 522, "seek":
  209480, "start": 2109.04, "end": 2115.2400000000002, "text": " fundamentally based
  on a VM25 search, followed by re-ranking with the neural network.", "tokens": [51076,
  17879, 2361, 322, 257, 18038, 6074, 3164, 11, 6263, 538, 319, 12, 20479, 278, 365,
  264, 18161, 3209, 13, 51386], "temperature": 0.0, "avg_logprob": -0.19223769098265558,
  "compression_ratio": 1.6779661016949152, "no_speech_prob": 0.010225232690572739},
  {"id": 523, "seek": 209480, "start": 2115.2400000000002, "end": 2119.2200000000003,
  "text": " This is what I''ve gathered from their own product marketing material,
  which is still", "tokens": [51386, 639, 307, 437, 286, 600, 13032, 490, 641, 1065,
  1674, 6370, 2527, 11, 597, 307, 920, 51585], "temperature": 0.0, "avg_logprob":
  -0.19223769098265558, "compression_ratio": 1.6779661016949152, "no_speech_prob":
  0.010225232690572739}, {"id": 524, "seek": 209480, "start": 2119.2200000000003,
  "end": 2120.2200000000003, "text": " in neural search.", "tokens": [51585, 294,
  18161, 3164, 13, 51635], "temperature": 0.0, "avg_logprob": -0.19223769098265558,
  "compression_ratio": 1.6779661016949152, "no_speech_prob": 0.010225232690572739},
  {"id": 525, "seek": 209480, "start": 2120.2200000000003, "end": 2124.4, "text":
  " It just has a difference out of pros and cons versus like straight retrieval from
  a vector", "tokens": [51635, 467, 445, 575, 257, 2649, 484, 295, 6267, 293, 1014,
  5717, 411, 2997, 19817, 3337, 490, 257, 8062, 51844], "temperature": 0.0, "avg_logprob":
  -0.19223769098265558, "compression_ratio": 1.6779661016949152, "no_speech_prob":
  0.010225232690572739}, {"id": 526, "seek": 212440, "start": 2124.4, "end": 2125.4,
  "text": " database.", "tokens": [50364, 8149, 13, 50414], "temperature": 0.0, "avg_logprob":
  -0.21398587954246392, "compression_ratio": 1.703125, "no_speech_prob": 0.011719164438545704},
  {"id": 527, "seek": 212440, "start": 2125.4, "end": 2132.48, "text": " So, for instance,
  just to give you one quick example, a multilingual search, VM25 is not", "tokens":
  [50414, 407, 11, 337, 5197, 11, 445, 281, 976, 291, 472, 1702, 1365, 11, 257, 2120,
  38219, 3164, 11, 18038, 6074, 307, 406, 50768], "temperature": 0.0, "avg_logprob":
  -0.21398587954246392, "compression_ratio": 1.703125, "no_speech_prob": 0.011719164438545704},
  {"id": 528, "seek": 212440, "start": 2132.48, "end": 2134.6800000000003, "text":
  " going to work for a multilingual search.", "tokens": [50768, 516, 281, 589, 337,
  257, 2120, 38219, 3164, 13, 50878], "temperature": 0.0, "avg_logprob": -0.21398587954246392,
  "compression_ratio": 1.703125, "no_speech_prob": 0.011719164438545704}, {"id": 529,
  "seek": 212440, "start": 2134.6800000000003, "end": 2139.7200000000003, "text":
  " You have queries coming in different languages, documents in different languages.",
  "tokens": [50878, 509, 362, 24109, 1348, 294, 819, 8650, 11, 8512, 294, 819, 8650,
  13, 51130], "temperature": 0.0, "avg_logprob": -0.21398587954246392, "compression_ratio":
  1.703125, "no_speech_prob": 0.011719164438545704}, {"id": 530, "seek": 212440, "start":
  2139.7200000000003, "end": 2145.04, "text": " VM25 won''t work there, nor will a
  re-rank on a VM25 results approach work over there,", "tokens": [51130, 18038, 6074,
  1582, 380, 589, 456, 11, 6051, 486, 257, 319, 12, 20479, 322, 257, 18038, 6074,
  3542, 3109, 589, 670, 456, 11, 51396], "temperature": 0.0, "avg_logprob": -0.21398587954246392,
  "compression_ratio": 1.703125, "no_speech_prob": 0.011719164438545704}, {"id": 531,
  "seek": 212440, "start": 2145.04, "end": 2148.84, "text": " because the VM25 has
  to bring something back to re-ranking.", "tokens": [51396, 570, 264, 18038, 6074,
  575, 281, 1565, 746, 646, 281, 319, 12, 20479, 278, 13, 51586], "temperature": 0.0,
  "avg_logprob": -0.21398587954246392, "compression_ratio": 1.703125, "no_speech_prob":
  0.011719164438545704}, {"id": 532, "seek": 212440, "start": 2148.84, "end": 2153.52,
  "text": " Well, in the case of our system, you can check on some of the demos.",
  "tokens": [51586, 1042, 11, 294, 264, 1389, 295, 527, 1185, 11, 291, 393, 1520,
  322, 512, 295, 264, 33788, 13, 51820], "temperature": 0.0, "avg_logprob": -0.21398587954246392,
  "compression_ratio": 1.703125, "no_speech_prob": 0.011719164438545704}, {"id": 533,
  "seek": 215352, "start": 2153.52, "end": 2158.08, "text": " We can actually embed
  across languages into a shared embedding space.", "tokens": [50364, 492, 393, 767,
  12240, 2108, 8650, 666, 257, 5507, 12240, 3584, 1901, 13, 50592], "temperature":
  0.0, "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312,
  "no_speech_prob": 0.01436303649097681}, {"id": 534, "seek": 215352, "start": 2158.08,
  "end": 2160.64, "text": " And so you can search across languages.", "tokens": [50592,
  400, 370, 291, 393, 3164, 2108, 8650, 13, 50720], "temperature": 0.0, "avg_logprob":
  -0.24934017986332604, "compression_ratio": 1.6450381679389312, "no_speech_prob":
  0.01436303649097681}, {"id": 535, "seek": 215352, "start": 2160.64, "end": 2163.64,
  "text": " That''s something which you need a vector database for.", "tokens": [50720,
  663, 311, 746, 597, 291, 643, 257, 8062, 8149, 337, 13, 50870], "temperature": 0.0,
  "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312, "no_speech_prob":
  0.01436303649097681}, {"id": 536, "seek": 215352, "start": 2163.64, "end": 2164.64,
  "text": " Yeah, exactly.", "tokens": [50870, 865, 11, 2293, 13, 50920], "temperature":
  0.0, "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312,
  "no_speech_prob": 0.01436303649097681}, {"id": 537, "seek": 215352, "start": 2164.64,
  "end": 2171.52, "text": " So you go multilingual on the first stage of retrieving
  the data dates, right?", "tokens": [50920, 407, 291, 352, 2120, 38219, 322, 264,
  700, 3233, 295, 19817, 798, 264, 1412, 11691, 11, 558, 30, 51264], "temperature":
  0.0, "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312,
  "no_speech_prob": 0.01436303649097681}, {"id": 538, "seek": 215352, "start": 2171.52,
  "end": 2175.56, "text": " And I think this multilingual search in general, I think
  it has so much potential.", "tokens": [51264, 400, 286, 519, 341, 2120, 38219, 3164,
  294, 2674, 11, 286, 519, 309, 575, 370, 709, 3995, 13, 51466], "temperature": 0.0,
  "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312, "no_speech_prob":
  0.01436303649097681}, {"id": 539, "seek": 215352, "start": 2175.56, "end": 2181.0,
  "text": " I don''t know if Google is using it already, to some extent, but like
  even like at smaller", "tokens": [51466, 286, 500, 380, 458, 498, 3329, 307, 1228,
  309, 1217, 11, 281, 512, 8396, 11, 457, 411, 754, 411, 412, 4356, 51738], "temperature":
  0.0, "avg_logprob": -0.24934017986332604, "compression_ratio": 1.6450381679389312,
  "no_speech_prob": 0.01436303649097681}, {"id": 540, "seek": 218100, "start": 2181.0,
  "end": 2186.6, "text": " scale, instead of configuring, let''s say, solar.", "tokens":
  [50364, 4373, 11, 2602, 295, 6662, 1345, 11, 718, 311, 584, 11, 7936, 13, 50644],
  "temperature": 0.0, "avg_logprob": -0.2809359414236886, "compression_ratio": 1.4792626728110598,
  "no_speech_prob": 0.061261195689439774}, {"id": 541, "seek": 218100, "start": 2186.6,
  "end": 2189.0, "text": " We keep mentioning last search a lot.", "tokens": [50644,
  492, 1066, 18315, 1036, 3164, 257, 688, 13, 50764], "temperature": 0.0, "avg_logprob":
  -0.2809359414236886, "compression_ratio": 1.4792626728110598, "no_speech_prob":
  0.061261195689439774}, {"id": 542, "seek": 218100, "start": 2189.0, "end": 2192.0,
  "text": " They didn''t pay for these podcasts.", "tokens": [50764, 814, 994, 380,
  1689, 337, 613, 24045, 13, 50914], "temperature": 0.0, "avg_logprob": -0.2809359414236886,
  "compression_ratio": 1.4792626728110598, "no_speech_prob": 0.061261195689439774},
  {"id": 543, "seek": 218100, "start": 2192.0, "end": 2196.08, "text": " But I''m
  just saying, let''s say Apache solar, or Lycene, right?", "tokens": [50914, 583,
  286, 478, 445, 1566, 11, 718, 311, 584, 46597, 7936, 11, 420, 12687, 66, 1450, 11,
  558, 30, 51118], "temperature": 0.0, "avg_logprob": -0.2809359414236886, "compression_ratio":
  1.4792626728110598, "no_speech_prob": 0.061261195689439774}, {"id": 544, "seek":
  218100, "start": 2196.08, "end": 2202.24, "text": " So you''ll have to kind of like,
  yeah, go a long, long, long way to achieve it.", "tokens": [51118, 407, 291, 603,
  362, 281, 733, 295, 411, 11, 1338, 11, 352, 257, 938, 11, 938, 11, 938, 636, 281,
  4584, 309, 13, 51426], "temperature": 0.0, "avg_logprob": -0.2809359414236886, "compression_ratio":
  1.4792626728110598, "no_speech_prob": 0.061261195689439774}, {"id": 545, "seek":
  218100, "start": 2202.24, "end": 2207.56, "text": " But like, okay, now Lycene released
  H&SW in 9.0 version.", "tokens": [51426, 583, 411, 11, 1392, 11, 586, 12687, 66,
  1450, 4736, 389, 5, 50, 54, 294, 1722, 13, 15, 3037, 13, 51692], "temperature":
  0.0, "avg_logprob": -0.2809359414236886, "compression_ratio": 1.4792626728110598,
  "no_speech_prob": 0.061261195689439774}, {"id": 546, "seek": 220756, "start": 2207.56,
  "end": 2213.92, "text": " And so in principle, you could embed your documents using
  multilingual model and retrieve", "tokens": [50364, 400, 370, 294, 8665, 11, 291,
  727, 12240, 428, 8512, 1228, 2120, 38219, 2316, 293, 30254, 50682], "temperature":
  0.0, "avg_logprob": -0.2174994945526123, "compression_ratio": 1.5104166666666667,
  "no_speech_prob": 0.0037523882929235697}, {"id": 547, "seek": 220756, "start": 2213.92,
  "end": 2215.84, "text": " them in the same way, right?", "tokens": [50682, 552,
  294, 264, 912, 636, 11, 558, 30, 50778], "temperature": 0.0, "avg_logprob": -0.2174994945526123,
  "compression_ratio": 1.5104166666666667, "no_speech_prob": 0.0037523882929235697},
  {"id": 548, "seek": 220756, "start": 2215.84, "end": 2225.16, "text": " So do you
  see huge potential for the market, you know, for the multilinguality?", "tokens":
  [50778, 407, 360, 291, 536, 2603, 3995, 337, 264, 2142, 11, 291, 458, 11, 337, 264,
  2120, 38219, 507, 30, 51244], "temperature": 0.0, "avg_logprob": -0.2174994945526123,
  "compression_ratio": 1.5104166666666667, "no_speech_prob": 0.0037523882929235697},
  {"id": 549, "seek": 220756, "start": 2225.16, "end": 2234.08, "text": " No, there
  have been some studies that showed that when eBay introduced automatic translator",
  "tokens": [51244, 883, 11, 456, 362, 668, 512, 5313, 300, 4712, 300, 562, 33803,
  7268, 12509, 35223, 51690], "temperature": 0.0, "avg_logprob": -0.2174994945526123,
  "compression_ratio": 1.5104166666666667, "no_speech_prob": 0.0037523882929235697},
  {"id": 550, "seek": 223408, "start": 2234.08, "end": 2238.48, "text": " tools, there
  was a significant increase.", "tokens": [50364, 3873, 11, 456, 390, 257, 4776, 3488,
  13, 50584], "temperature": 0.0, "avg_logprob": -0.22587434595281428, "compression_ratio":
  1.6818181818181819, "no_speech_prob": 0.07370851188898087}, {"id": 551, "seek":
  223408, "start": 2238.48, "end": 2242.6, "text": " It was a few, I think, you know,
  a few percentage points of increase in commerce on their", "tokens": [50584, 467,
  390, 257, 1326, 11, 286, 519, 11, 291, 458, 11, 257, 1326, 9668, 2793, 295, 3488,
  294, 26320, 322, 641, 50790], "temperature": 0.0, "avg_logprob": -0.22587434595281428,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.07370851188898087},
  {"id": 552, "seek": 223408, "start": 2242.6, "end": 2246.96, "text": " platform,
  which translated to hundreds and hundreds of millions of dollars.", "tokens": [50790,
  3663, 11, 597, 16805, 281, 6779, 293, 6779, 295, 6803, 295, 3808, 13, 51008], "temperature":
  0.0, "avg_logprob": -0.22587434595281428, "compression_ratio": 1.6818181818181819,
  "no_speech_prob": 0.07370851188898087}, {"id": 553, "seek": 223408, "start": 2246.96,
  "end": 2252.2799999999997, "text": " So the, you know, the advancements that have
  been made in machine translation and now,", "tokens": [51008, 407, 264, 11, 291,
  458, 11, 264, 7295, 1117, 300, 362, 668, 1027, 294, 3479, 12853, 293, 586, 11, 51274],
  "temperature": 0.0, "avg_logprob": -0.22587434595281428, "compression_ratio": 1.6818181818181819,
  "no_speech_prob": 0.07370851188898087}, {"id": 554, "seek": 223408, "start": 2252.2799999999997,
  "end": 2258.36, "text": " and she like, cross-lingual retrieval, will serve to further
  break down barriers to commerce", "tokens": [51274, 293, 750, 411, 11, 3278, 12,
  1688, 901, 19817, 3337, 11, 486, 4596, 281, 3052, 1821, 760, 13565, 281, 26320,
  51578], "temperature": 0.0, "avg_logprob": -0.22587434595281428, "compression_ratio":
  1.6818181818181819, "no_speech_prob": 0.07370851188898087}, {"id": 555, "seek":
  223408, "start": 2258.36, "end": 2259.36, "text": " at least.", "tokens": [51578,
  412, 1935, 13, 51628], "temperature": 0.0, "avg_logprob": -0.22587434595281428,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.07370851188898087},
  {"id": 556, "seek": 223408, "start": 2259.36, "end": 2262.0, "text": " And in a
  way that''s commercially very valuable.", "tokens": [51628, 400, 294, 257, 636,
  300, 311, 41751, 588, 8263, 13, 51760], "temperature": 0.0, "avg_logprob": -0.22587434595281428,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.07370851188898087},
  {"id": 557, "seek": 226200, "start": 2262.0, "end": 2267.12, "text": " But speaking
  more broadly, I think that what I would be very interested to see is how", "tokens":
  [50364, 583, 4124, 544, 19511, 11, 286, 519, 300, 437, 286, 576, 312, 588, 3102,
  281, 536, 307, 577, 50620], "temperature": 0.0, "avg_logprob": -0.26387407973005966,
  "compression_ratio": 1.4761904761904763, "no_speech_prob": 0.007855252362787724},
  {"id": 558, "seek": 226200, "start": 2267.12, "end": 2277.48, "text": " vector databases
  evolve and merge into traditional database technology or into systems like", "tokens":
  [50620, 8062, 22380, 16693, 293, 22183, 666, 5164, 8149, 2899, 420, 666, 3652, 411,
  51138], "temperature": 0.0, "avg_logprob": -0.26387407973005966, "compression_ratio":
  1.4761904761904763, "no_speech_prob": 0.007855252362787724}, {"id": 559, "seek":
  226200, "start": 2277.48, "end": 2280.64, "text": " Lucene, like information retrieval
  systems.", "tokens": [51138, 9593, 1450, 11, 411, 1589, 19817, 3337, 3652, 13, 51296],
  "temperature": 0.0, "avg_logprob": -0.26387407973005966, "compression_ratio": 1.4761904761904763,
  "no_speech_prob": 0.007855252362787724}, {"id": 560, "seek": 226200, "start": 2280.64,
  "end": 2285.92, "text": " Because at the moment, you know, you have FIAS, it''s
  kind of a separate discreet entity.", "tokens": [51296, 1436, 412, 264, 1623, 11,
  291, 458, 11, 291, 362, 479, 40, 3160, 11, 309, 311, 733, 295, 257, 4994, 2983,
  4751, 13977, 13, 51560], "temperature": 0.0, "avg_logprob": -0.26387407973005966,
  "compression_ratio": 1.4761904761904763, "no_speech_prob": 0.007855252362787724},
  {"id": 561, "seek": 228592, "start": 2285.92, "end": 2292.4, "text": " But longer
  term, just, you know, conceptually, in a way, very low-dimensional vector database",
  "tokens": [50364, 583, 2854, 1433, 11, 445, 11, 291, 458, 11, 3410, 671, 11, 294,
  257, 636, 11, 588, 2295, 12, 18759, 8062, 8149, 50688], "temperature": 0.0, "avg_logprob":
  -0.20521536327543713, "compression_ratio": 1.619047619047619, "no_speech_prob":
  0.31724634766578674}, {"id": 562, "seek": 228592, "start": 2292.4, "end": 2297.6,
  "text": " technology has already made its way into my sequel and Postgres with the
  spatial extensions", "tokens": [50688, 2899, 575, 1217, 1027, 1080, 636, 666, 452,
  20622, 293, 10223, 45189, 365, 264, 23598, 25129, 50948], "temperature": 0.0, "avg_logprob":
  -0.20521536327543713, "compression_ratio": 1.619047619047619, "no_speech_prob":
  0.31724634766578674}, {"id": 563, "seek": 228592, "start": 2297.6, "end": 2301.36,
  "text": " that they''ve supported for many years.", "tokens": [50948, 300, 436,
  600, 8104, 337, 867, 924, 13, 51136], "temperature": 0.0, "avg_logprob": -0.20521536327543713,
  "compression_ratio": 1.619047619047619, "no_speech_prob": 0.31724634766578674},
  {"id": 564, "seek": 228592, "start": 2301.36, "end": 2307.16, "text": " The quadri
  algorithm for doing, you know, sublinear lookups on a map.", "tokens": [51136, 440,
  10787, 470, 9284, 337, 884, 11, 291, 458, 11, 1422, 28263, 574, 7528, 322, 257,
  4471, 13, 51426], "temperature": 0.0, "avg_logprob": -0.20521536327543713, "compression_ratio":
  1.619047619047619, "no_speech_prob": 0.31724634766578674}, {"id": 565, "seek": 228592,
  "start": 2307.16, "end": 2309.56, "text": " Those spatial extensions have been around
  for a while.", "tokens": [51426, 3950, 23598, 25129, 362, 668, 926, 337, 257, 1339,
  13, 51546], "temperature": 0.0, "avg_logprob": -0.20521536327543713, "compression_ratio":
  1.619047619047619, "no_speech_prob": 0.31724634766578674}, {"id": 566, "seek": 228592,
  "start": 2309.56, "end": 2314.6, "text": " You can easily imagine that in the future,
  once people start to understand how useful vector", "tokens": [51546, 509, 393,
  3612, 3811, 300, 294, 264, 2027, 11, 1564, 561, 722, 281, 1223, 577, 4420, 8062,
  51798], "temperature": 0.0, "avg_logprob": -0.20521536327543713, "compression_ratio":
  1.619047619047619, "no_speech_prob": 0.31724634766578674}, {"id": 567, "seek": 231460,
  "start": 2314.6, "end": 2321.64, "text": " embeddings can be, and that''s established,
  that you''ll have a, you know, columns of vector", "tokens": [50364, 12240, 29432,
  393, 312, 11, 293, 300, 311, 7545, 11, 300, 291, 603, 362, 257, 11, 291, 458, 11,
  13766, 295, 8062, 50716], "temperature": 0.0, "avg_logprob": -0.25377947256105754,
  "compression_ratio": 1.6088560885608856, "no_speech_prob": 0.004319720435887575},
  {"id": 568, "seek": 231460, "start": 2321.64, "end": 2327.3199999999997, "text":
  " type in a relational database and be able to simply build an index and perform,
  you know,", "tokens": [50716, 2010, 294, 257, 38444, 8149, 293, 312, 1075, 281,
  2935, 1322, 364, 8186, 293, 2042, 11, 291, 458, 11, 51000], "temperature": 0.0,
  "avg_logprob": -0.25377947256105754, "compression_ratio": 1.6088560885608856, "no_speech_prob":
  0.004319720435887575}, {"id": 569, "seek": 231460, "start": 2327.3199999999997,
  "end": 2331.24, "text": " fast nearest neighbor searches straight from Postgres.",
  "tokens": [51000, 2370, 23831, 5987, 26701, 2997, 490, 10223, 45189, 13, 51196],
  "temperature": 0.0, "avg_logprob": -0.25377947256105754, "compression_ratio": 1.6088560885608856,
  "no_speech_prob": 0.004319720435887575}, {"id": 570, "seek": 231460, "start": 2331.24,
  "end": 2334.0, "text": " So I think that''s an exciting future to contemplate.",
  "tokens": [51196, 407, 286, 519, 300, 311, 364, 4670, 2027, 281, 19935, 473, 13,
  51334], "temperature": 0.0, "avg_logprob": -0.25377947256105754, "compression_ratio":
  1.6088560885608856, "no_speech_prob": 0.004319720435887575}, {"id": 571, "seek":
  231460, "start": 2334.0, "end": 2336.68, "text": " And I see that eventually it
  will go there.", "tokens": [51334, 400, 286, 536, 300, 4728, 309, 486, 352, 456,
  13, 51468], "temperature": 0.0, "avg_logprob": -0.25377947256105754, "compression_ratio":
  1.6088560885608856, "no_speech_prob": 0.004319720435887575}, {"id": 572, "seek":
  231460, "start": 2336.68, "end": 2338.92, "text": " That sounds really interesting,
  Lake.", "tokens": [51468, 663, 3263, 534, 1880, 11, 10582, 13, 51580], "temperature":
  0.0, "avg_logprob": -0.25377947256105754, "compression_ratio": 1.6088560885608856,
  "no_speech_prob": 0.004319720435887575}, {"id": 573, "seek": 231460, "start": 2338.92,
  "end": 2342.7999999999997, "text": " Do you think that vector searches in general
  is a hype right now?", "tokens": [51580, 1144, 291, 519, 300, 8062, 26701, 294,
  2674, 307, 257, 24144, 558, 586, 30, 51774], "temperature": 0.0, "avg_logprob":
  -0.25377947256105754, "compression_ratio": 1.6088560885608856, "no_speech_prob":
  0.004319720435887575}, {"id": 574, "seek": 234280, "start": 2342.8, "end": 2346.1600000000003,
  "text": " I think the way big data was few years ago.", "tokens": [50364, 286, 519,
  264, 636, 955, 1412, 390, 1326, 924, 2057, 13, 50532], "temperature": 0.0, "avg_logprob":
  -0.23654603958129883, "compression_ratio": 1.5271966527196652, "no_speech_prob":
  0.0058137052692472935}, {"id": 575, "seek": 234280, "start": 2346.1600000000003,
  "end": 2355.36, "text": " No, no, it''s not hype because, again, I saw neural information
  techniques, backed by vector", "tokens": [50532, 883, 11, 572, 11, 309, 311, 406,
  24144, 570, 11, 797, 11, 286, 1866, 18161, 1589, 7512, 11, 20391, 538, 8062, 50992],
  "temperature": 0.0, "avg_logprob": -0.23654603958129883, "compression_ratio": 1.5271966527196652,
  "no_speech_prob": 0.0058137052692472935}, {"id": 576, "seek": 234280, "start": 2355.36,
  "end": 2359.4, "text": " databases, making a big difference in many products at
  Google.", "tokens": [50992, 22380, 11, 1455, 257, 955, 2649, 294, 867, 3383, 412,
  3329, 13, 51194], "temperature": 0.0, "avg_logprob": -0.23654603958129883, "compression_ratio":
  1.5271966527196652, "no_speech_prob": 0.0058137052692472935}, {"id": 577, "seek":
  234280, "start": 2359.4, "end": 2365.52, "text": " So I think where it is right
  now is that there''s a few big companies, like the Fang type", "tokens": [51194,
  407, 286, 519, 689, 309, 307, 558, 586, 307, 300, 456, 311, 257, 1326, 955, 3431,
  11, 411, 264, 25409, 2010, 51500], "temperature": 0.0, "avg_logprob": -0.23654603958129883,
  "compression_ratio": 1.5271966527196652, "no_speech_prob": 0.0058137052692472935},
  {"id": 578, "seek": 234280, "start": 2365.52, "end": 2370.5600000000004, "text":
  " companies in Silicon Valley, that have the expertise to take advantage of it.",
  "tokens": [51500, 3431, 294, 25351, 10666, 11, 300, 362, 264, 11769, 281, 747, 5002,
  295, 309, 13, 51752], "temperature": 0.0, "avg_logprob": -0.23654603958129883, "compression_ratio":
  1.5271966527196652, "no_speech_prob": 0.0058137052692472935}, {"id": 579, "seek":
  237056, "start": 2370.56, "end": 2372.88, "text": " It''s not being commoditized
  yet.", "tokens": [50364, 467, 311, 406, 885, 19931, 270, 1602, 1939, 13, 50480],
  "temperature": 0.0, "avg_logprob": -0.28119694685735624, "compression_ratio": 1.5611510791366907,
  "no_speech_prob": 0.04782700911164284}, {"id": 580, "seek": 237056, "start": 2372.88,
  "end": 2377.2, "text": " So it''s definitely not hype, but it''s got a few years
  to go before it enters a mainstream", "tokens": [50480, 407, 309, 311, 2138, 406,
  24144, 11, 457, 309, 311, 658, 257, 1326, 924, 281, 352, 949, 309, 18780, 257, 15960,
  50696], "temperature": 0.0, "avg_logprob": -0.28119694685735624, "compression_ratio":
  1.5611510791366907, "no_speech_prob": 0.04782700911164284}, {"id": 581, "seek":
  237056, "start": 2377.2, "end": 2378.2, "text": " consciousness.", "tokens": [50696,
  10081, 13, 50746], "temperature": 0.0, "avg_logprob": -0.28119694685735624, "compression_ratio":
  1.5611510791366907, "no_speech_prob": 0.04782700911164284}, {"id": 582, "seek":
  237056, "start": 2378.2, "end": 2379.2, "text": " Yeah, for sure.", "tokens": [50746,
  865, 11, 337, 988, 13, 50796], "temperature": 0.0, "avg_logprob": -0.28119694685735624,
  "compression_ratio": 1.5611510791366907, "no_speech_prob": 0.04782700911164284},
  {"id": 583, "seek": 237056, "start": 2379.2, "end": 2384.88, "text": " But like
  to your point, like maybe at some point, vector search will become, let''s say,",
  "tokens": [50796, 583, 411, 281, 428, 935, 11, 411, 1310, 412, 512, 935, 11, 8062,
  3164, 486, 1813, 11, 718, 311, 584, 11, 51080], "temperature": 0.0, "avg_logprob":
  -0.28119694685735624, "compression_ratio": 1.5611510791366907, "no_speech_prob":
  0.04782700911164284}, {"id": 584, "seek": 237056, "start": 2384.88, "end": 2393.2,
  "text": " part of Postgres or my SQL or whatever other like, kind of traditional,
  so to say, database,", "tokens": [51080, 644, 295, 10223, 45189, 420, 452, 19200,
  420, 2035, 661, 411, 11, 733, 295, 5164, 11, 370, 281, 584, 11, 8149, 11, 51496],
  "temperature": 0.0, "avg_logprob": -0.28119694685735624, "compression_ratio": 1.5611510791366907,
  "no_speech_prob": 0.04782700911164284}, {"id": 585, "seek": 237056, "start": 2393.2,
  "end": 2397.36, "text": " which is traditional is in its widely used.", "tokens":
  [51496, 597, 307, 5164, 307, 294, 1080, 13371, 1143, 13, 51704], "temperature":
  0.0, "avg_logprob": -0.28119694685735624, "compression_ratio": 1.5611510791366907,
  "no_speech_prob": 0.04782700911164284}, {"id": 586, "seek": 237056, "start": 2397.36,
  "end": 2399.92, "text": " And then you''ve seen already also introduced it, right?",
  "tokens": [51704, 400, 550, 291, 600, 1612, 1217, 611, 7268, 309, 11, 558, 30, 51832],
  "temperature": 0.0, "avg_logprob": -0.28119694685735624, "compression_ratio": 1.5611510791366907,
  "no_speech_prob": 0.04782700911164284}, {"id": 587, "seek": 239992, "start": 2399.92,
  "end": 2403.0, "text": " Lucine now has H&SW.", "tokens": [50364, 9593, 533, 586,
  575, 389, 5, 50, 54, 13, 50518], "temperature": 0.0, "avg_logprob": -0.22172396523611887,
  "compression_ratio": 1.4948979591836735, "no_speech_prob": 0.01975647732615471},
  {"id": 588, "seek": 239992, "start": 2403.0, "end": 2412.16, "text": " You can go
  and argue to the point, okay, maybe Lucine index layout might not be kind of", "tokens":
  [50518, 509, 393, 352, 293, 9695, 281, 264, 935, 11, 1392, 11, 1310, 9593, 533,
  8186, 13333, 1062, 406, 312, 733, 295, 50976], "temperature": 0.0, "avg_logprob":
  -0.22172396523611887, "compression_ratio": 1.4948979591836735, "no_speech_prob":
  0.01975647732615471}, {"id": 589, "seek": 239992, "start": 2412.16, "end": 2419.0,
  "text": " optimally designed for, you know, nearest neighbor retrieval because,
  because like if you", "tokens": [50976, 5028, 379, 4761, 337, 11, 291, 458, 11,
  23831, 5987, 19817, 3337, 570, 11, 570, 411, 498, 291, 51318], "temperature": 0.0,
  "avg_logprob": -0.22172396523611887, "compression_ratio": 1.4948979591836735, "no_speech_prob":
  0.01975647732615471}, {"id": 590, "seek": 239992, "start": 2419.0, "end": 2425.2400000000002,
  "text": " look at five methods or H&SW, you know, like it''s some graph method or
  it''s a way to partition", "tokens": [51318, 574, 412, 1732, 7150, 420, 389, 5,
  50, 54, 11, 291, 458, 11, 411, 309, 311, 512, 4295, 3170, 420, 309, 311, 257, 636,
  281, 24808, 51630], "temperature": 0.0, "avg_logprob": -0.22172396523611887, "compression_ratio":
  1.4948979591836735, "no_speech_prob": 0.01975647732615471}, {"id": 591, "seek":
  242524, "start": 2425.24, "end": 2428.9599999999996, "text": " your space in the
  scene, you partition it by segments.", "tokens": [50364, 428, 1901, 294, 264, 4145,
  11, 291, 24808, 309, 538, 19904, 13, 50550], "temperature": 0.0, "avg_logprob":
  -0.24098337173461915, "compression_ratio": 1.5737051792828685, "no_speech_prob":
  0.059421613812446594}, {"id": 592, "seek": 242524, "start": 2428.9599999999996,
  "end": 2430.9199999999996, "text": " And that''s kind of like given, right?", "tokens":
  [50550, 400, 300, 311, 733, 295, 411, 2212, 11, 558, 30, 50648], "temperature":
  0.0, "avg_logprob": -0.24098337173461915, "compression_ratio": 1.5737051792828685,
  "no_speech_prob": 0.059421613812446594}, {"id": 593, "seek": 242524, "start": 2430.9199999999996,
  "end": 2434.2, "text": " Because it''s designed for inverted index.", "tokens":
  [50648, 1436, 309, 311, 4761, 337, 38969, 8186, 13, 50812], "temperature": 0.0,
  "avg_logprob": -0.24098337173461915, "compression_ratio": 1.5737051792828685, "no_speech_prob":
  0.059421613812446594}, {"id": 594, "seek": 242524, "start": 2434.2, "end": 2440.52,
  "text": " But again, on Twitter somewhere, I saw it with from one Lucine commeter
  who said, maybe", "tokens": [50812, 583, 797, 11, 322, 5794, 4079, 11, 286, 1866,
  309, 365, 490, 472, 9593, 533, 800, 2398, 567, 848, 11, 1310, 51128], "temperature":
  0.0, "avg_logprob": -0.24098337173461915, "compression_ratio": 1.5737051792828685,
  "no_speech_prob": 0.059421613812446594}, {"id": 595, "seek": 242524, "start": 2440.52,
  "end": 2447.7599999999998, "text": " this will by itself open up some new opportunities
  because you''ll have a separate vector space index", "tokens": [51128, 341, 486,
  538, 2564, 1269, 493, 512, 777, 4786, 570, 291, 603, 362, 257, 4994, 8062, 1901,
  8186, 51490], "temperature": 0.0, "avg_logprob": -0.24098337173461915, "compression_ratio":
  1.5737051792828685, "no_speech_prob": 0.059421613812446594}, {"id": 596, "seek":
  242524, "start": 2447.7599999999998, "end": 2449.64, "text": " per segment, right?",
  "tokens": [51490, 680, 9469, 11, 558, 30, 51584], "temperature": 0.0, "avg_logprob":
  -0.24098337173461915, "compression_ratio": 1.5737051792828685, "no_speech_prob":
  0.059421613812446594}, {"id": 597, "seek": 242524, "start": 2449.64, "end": 2452.56,
  "text": " And maybe you can design some features around that.", "tokens": [51584,
  400, 1310, 291, 393, 1715, 512, 4122, 926, 300, 13, 51730], "temperature": 0.0,
  "avg_logprob": -0.24098337173461915, "compression_ratio": 1.5737051792828685, "no_speech_prob":
  0.059421613812446594}, {"id": 598, "seek": 245256, "start": 2452.56, "end": 2458.44,
  "text": " So it sounds like you still see the potential for merging these technologies
  in the future", "tokens": [50364, 407, 309, 3263, 411, 291, 920, 536, 264, 3995,
  337, 44559, 613, 7943, 294, 264, 2027, 50658], "temperature": 0.0, "avg_logprob":
  -0.260723876953125, "compression_ratio": 1.5960784313725491, "no_speech_prob": 0.030855737626552582},
  {"id": 599, "seek": 245256, "start": 2458.44, "end": 2461.16, "text": " and then
  bringing additional benefit.", "tokens": [50658, 293, 550, 5062, 4497, 5121, 13,
  50794], "temperature": 0.0, "avg_logprob": -0.260723876953125, "compression_ratio":
  1.5960784313725491, "no_speech_prob": 0.030855737626552582}, {"id": 600, "seek":
  245256, "start": 2461.16, "end": 2463.88, "text": " Well, yes, I can''t really speak
  for Lucine.", "tokens": [50794, 1042, 11, 2086, 11, 286, 393, 380, 534, 1710, 337,
  9593, 533, 13, 50930], "temperature": 0.0, "avg_logprob": -0.260723876953125, "compression_ratio":
  1.5960784313725491, "no_speech_prob": 0.030855737626552582}, {"id": 601, "seek":
  245256, "start": 2463.88, "end": 2466.4, "text": " I haven''t taken time to study
  that implementation.", "tokens": [50930, 286, 2378, 380, 2726, 565, 281, 2979, 300,
  11420, 13, 51056], "temperature": 0.0, "avg_logprob": -0.260723876953125, "compression_ratio":
  1.5960784313725491, "no_speech_prob": 0.030855737626552582}, {"id": 602, "seek":
  245256, "start": 2466.4, "end": 2468.68, "text": " How it was done is I think you
  know more about it than me.", "tokens": [51056, 1012, 309, 390, 1096, 307, 286,
  519, 291, 458, 544, 466, 309, 813, 385, 13, 51170], "temperature": 0.0, "avg_logprob":
  -0.260723876953125, "compression_ratio": 1.5960784313725491, "no_speech_prob": 0.030855737626552582},
  {"id": 603, "seek": 245256, "start": 2468.68, "end": 2476.12, "text": " But I was
  seeing that eventually relational databases could and might, you know, implement",
  "tokens": [51170, 583, 286, 390, 2577, 300, 4728, 38444, 22380, 727, 293, 1062,
  11, 291, 458, 11, 4445, 51542], "temperature": 0.0, "avg_logprob": -0.260723876953125,
  "compression_ratio": 1.5960784313725491, "no_speech_prob": 0.030855737626552582},
  {"id": 604, "seek": 245256, "start": 2476.12, "end": 2479.24, "text": " indexes,
  vector indexes directly.", "tokens": [51542, 8186, 279, 11, 8062, 8186, 279, 3838,
  13, 51698], "temperature": 0.0, "avg_logprob": -0.260723876953125, "compression_ratio":
  1.5960784313725491, "no_speech_prob": 0.030855737626552582}, {"id": 605, "seek":
  247924, "start": 2479.24, "end": 2482.9199999999996, "text": " I''m not sure that
  I can see any technical reason why that wouldn''t be possible, basically.", "tokens":
  [50364, 286, 478, 406, 988, 300, 286, 393, 536, 604, 6191, 1778, 983, 300, 2759,
  380, 312, 1944, 11, 1936, 13, 50548], "temperature": 0.0, "avg_logprob": -0.22915748014288434,
  "compression_ratio": 1.5714285714285714, "no_speech_prob": 0.002577786101028323},
  {"id": 606, "seek": 247924, "start": 2482.9199999999996, "end": 2487.7999999999997,
  "text": " And it could potentially be very, very useful as neural networks, you
  know, go more and", "tokens": [50548, 400, 309, 727, 7263, 312, 588, 11, 588, 4420,
  382, 18161, 9590, 11, 291, 458, 11, 352, 544, 293, 50792], "temperature": 0.0, "avg_logprob":
  -0.22915748014288434, "compression_ratio": 1.5714285714285714, "no_speech_prob":
  0.002577786101028323}, {"id": 607, "seek": 247924, "start": 2487.7999999999997,
  "end": 2489.68, "text": " more mainstream for embedding.", "tokens": [50792, 544,
  15960, 337, 12240, 3584, 13, 50886], "temperature": 0.0, "avg_logprob": -0.22915748014288434,
  "compression_ratio": 1.5714285714285714, "no_speech_prob": 0.002577786101028323},
  {"id": 608, "seek": 247924, "start": 2489.68, "end": 2493.8799999999997, "text":
  " Yeah, I mean, it sounds like one logical step forward.", "tokens": [50886, 865,
  11, 286, 914, 11, 309, 3263, 411, 472, 14978, 1823, 2128, 13, 51096], "temperature":
  0.0, "avg_logprob": -0.22915748014288434, "compression_ratio": 1.5714285714285714,
  "no_speech_prob": 0.002577786101028323}, {"id": 609, "seek": 247924, "start": 2493.8799999999997,
  "end": 2501.2799999999997, "text": " Maybe it will not be kind of scalable as a
  pure vector database, but like on a small", "tokens": [51096, 2704, 309, 486, 406,
  312, 733, 295, 38481, 382, 257, 6075, 8062, 8149, 11, 457, 411, 322, 257, 1359,
  51466], "temperature": 0.0, "avg_logprob": -0.22915748014288434, "compression_ratio":
  1.5714285714285714, "no_speech_prob": 0.002577786101028323}, {"id": 610, "seek":
  247924, "start": 2501.2799999999997, "end": 2507.8399999999997, "text": " like amount
  of data, let''s say when my SQL or Oracle or other databases, they introduce", "tokens":
  [51466, 411, 2372, 295, 1412, 11, 718, 311, 584, 562, 452, 19200, 420, 25654, 420,
  661, 22380, 11, 436, 5366, 51794], "temperature": 0.0, "avg_logprob": -0.22915748014288434,
  "compression_ratio": 1.5714285714285714, "no_speech_prob": 0.002577786101028323},
  {"id": 611, "seek": 247924, "start": 2507.8399999999997, "end": 2509.0, "text":
  " full text search, right?", "tokens": [51794, 1577, 2487, 3164, 11, 558, 30, 51852],
  "temperature": 0.0, "avg_logprob": -0.22915748014288434, "compression_ratio": 1.5714285714285714,
  "no_speech_prob": 0.002577786101028323}, {"id": 612, "seek": 250900, "start": 2509.0,
  "end": 2511.16, "text": " And initially it wasn''t there, right?", "tokens": [50364,
  400, 9105, 309, 2067, 380, 456, 11, 558, 30, 50472], "temperature": 0.0, "avg_logprob":
  -0.2620651623434272, "compression_ratio": 1.681992337164751, "no_speech_prob": 0.00325383385643363},
  {"id": 613, "seek": 250900, "start": 2511.16, "end": 2512.16, "text": " Right.",
  "tokens": [50472, 1779, 13, 50522], "temperature": 0.0, "avg_logprob": -0.2620651623434272,
  "compression_ratio": 1.681992337164751, "no_speech_prob": 0.00325383385643363},
  {"id": 614, "seek": 250900, "start": 2512.16, "end": 2519.36, "text": " What restricts
  you from, you know, introducing another field with embedding and actually running",
  "tokens": [50522, 708, 7694, 82, 291, 490, 11, 291, 458, 11, 15424, 1071, 2519,
  365, 12240, 3584, 293, 767, 2614, 50882], "temperature": 0.0, "avg_logprob": -0.2620651623434272,
  "compression_ratio": 1.681992337164751, "no_speech_prob": 0.00325383385643363},
  {"id": 615, "seek": 250900, "start": 2519.36, "end": 2521.36, "text": " your vector
  retrieval there?", "tokens": [50882, 428, 8062, 19817, 3337, 456, 30, 50982], "temperature":
  0.0, "avg_logprob": -0.2620651623434272, "compression_ratio": 1.681992337164751,
  "no_speech_prob": 0.00325383385643363}, {"id": 616, "seek": 250900, "start": 2521.36,
  "end": 2522.36, "text": " Right.", "tokens": [50982, 1779, 13, 51032], "temperature":
  0.0, "avg_logprob": -0.2620651623434272, "compression_ratio": 1.681992337164751,
  "no_speech_prob": 0.00325383385643363}, {"id": 617, "seek": 250900, "start": 2522.36,
  "end": 2523.36, "text": " Yeah.", "tokens": [51032, 865, 13, 51082], "temperature":
  0.0, "avg_logprob": -0.2620651623434272, "compression_ratio": 1.681992337164751,
  "no_speech_prob": 0.00325383385643363}, {"id": 618, "seek": 250900, "start": 2523.36,
  "end": 2529.64, "text": " And I think it also, it comes down to this that, okay,
  FICE is always going to give you,", "tokens": [51082, 400, 286, 519, 309, 611, 11,
  309, 1487, 760, 281, 341, 300, 11, 1392, 11, 479, 13663, 307, 1009, 516, 281, 976,
  291, 11, 51396], "temperature": 0.0, "avg_logprob": -0.2620651623434272, "compression_ratio":
  1.681992337164751, "no_speech_prob": 0.00325383385643363}, {"id": 619, "seek": 250900,
  "start": 2529.64, "end": 2531.72, "text": " you know, the maximum performance.",
  "tokens": [51396, 291, 458, 11, 264, 6674, 3389, 13, 51500], "temperature": 0.0,
  "avg_logprob": -0.2620651623434272, "compression_ratio": 1.681992337164751, "no_speech_prob":
  0.00325383385643363}, {"id": 620, "seek": 250900, "start": 2531.72, "end": 2536.92,
  "text": " So, you know, there''s going to be some subset of engineering teams that
  need that performance", "tokens": [51500, 407, 11, 291, 458, 11, 456, 311, 516,
  281, 312, 512, 25993, 295, 7043, 5491, 300, 643, 300, 3389, 51760], "temperature":
  0.0, "avg_logprob": -0.2620651623434272, "compression_ratio": 1.681992337164751,
  "no_speech_prob": 0.00325383385643363}, {"id": 621, "seek": 250900, "start": 2536.92,
  "end": 2538.64, "text": " and that''s where they''re going to go.", "tokens": [51760,
  293, 300, 311, 689, 436, 434, 516, 281, 352, 13, 51846], "temperature": 0.0, "avg_logprob":
  -0.2620651623434272, "compression_ratio": 1.681992337164751, "no_speech_prob": 0.00325383385643363},
  {"id": 622, "seek": 253864, "start": 2538.7599999999998, "end": 2543.16, "text":
  " What about the mass market, you know, the Fortune 500 companies and things and
  they''re dealing", "tokens": [50370, 708, 466, 264, 2758, 2142, 11, 291, 458, 11,
  264, 38508, 5923, 3431, 293, 721, 293, 436, 434, 6260, 50590], "temperature": 0.0,
  "avg_logprob": -0.2629668572369744, "compression_ratio": 1.6474358974358974, "no_speech_prob":
  0.006068071350455284}, {"id": 623, "seek": 253864, "start": 2543.16, "end": 2547.2799999999997,
  "text": " with problems at such a scale where it''s not necessary to go there.",
  "tokens": [50590, 365, 2740, 412, 1270, 257, 4373, 689, 309, 311, 406, 4818, 281,
  352, 456, 13, 50796], "temperature": 0.0, "avg_logprob": -0.2629668572369744, "compression_ratio":
  1.6474358974358974, "no_speech_prob": 0.006068071350455284}, {"id": 624, "seek":
  253864, "start": 2547.2799999999997, "end": 2551.6, "text": " And if it''s just
  in the database, even if it''s only giving me 80% of the total performance,", "tokens":
  [50796, 400, 498, 309, 311, 445, 294, 264, 8149, 11, 754, 498, 309, 311, 787, 2902,
  385, 4688, 4, 295, 264, 3217, 3389, 11, 51012], "temperature": 0.0, "avg_logprob":
  -0.2629668572369744, "compression_ratio": 1.6474358974358974, "no_speech_prob":
  0.006068071350455284}, {"id": 625, "seek": 253864, "start": 2551.6, "end": 2552.6,
  "text": " that''s good enough.", "tokens": [51012, 300, 311, 665, 1547, 13, 51062],
  "temperature": 0.0, "avg_logprob": -0.2629668572369744, "compression_ratio": 1.6474358974358974,
  "no_speech_prob": 0.006068071350455284}, {"id": 626, "seek": 253864, "start": 2552.6,
  "end": 2558.52, "text": " And in a way, that pragmatic tradeoff is what''s underlying
  Zerae I''s existence because", "tokens": [51062, 400, 294, 257, 636, 11, 300, 46904,
  4923, 4506, 307, 437, 311, 14217, 1176, 1663, 68, 286, 311, 9123, 570, 51358], "temperature":
  0.0, "avg_logprob": -0.2629668572369744, "compression_ratio": 1.6474358974358974,
  "no_speech_prob": 0.006068071350455284}, {"id": 627, "seek": 253864, "start": 2558.52,
  "end": 2563.0, "text": " people often ask, I can get better performance on my data
  set.", "tokens": [51358, 561, 2049, 1029, 11, 286, 393, 483, 1101, 3389, 322, 452,
  1412, 992, 13, 51582], "temperature": 0.0, "avg_logprob": -0.2629668572369744, "compression_ratio":
  1.6474358974358974, "no_speech_prob": 0.006068071350455284}, {"id": 628, "seek":
  253864, "start": 2563.0, "end": 2568.6, "text": " If I find tune, a bird model and
  then distilled the bird model is like, yes, that''s true.", "tokens": [51582, 759,
  286, 915, 10864, 11, 257, 5255, 2316, 293, 550, 1483, 6261, 264, 5255, 2316, 307,
  411, 11, 2086, 11, 300, 311, 2074, 13, 51862], "temperature": 0.0, "avg_logprob":
  -0.2629668572369744, "compression_ratio": 1.6474358974358974, "no_speech_prob":
  0.006068071350455284}, {"id": 629, "seek": 256860, "start": 2568.88, "end": 2573.0,
  "text": " We''re aiming to give you a neural network and a full experience that
  will give you like", "tokens": [50378, 492, 434, 20253, 281, 976, 291, 257, 18161,
  3209, 293, 257, 1577, 1752, 300, 486, 976, 291, 411, 50584], "temperature": 0.0,
  "avg_logprob": -0.2220158760364239, "compression_ratio": 1.5648854961832062, "no_speech_prob":
  0.0027911229990422726}, {"id": 630, "seek": 256860, "start": 2573.0, "end": 2577.04,
  "text": " 80% of the performance that you might be able to achieve, which is still
  better than you", "tokens": [50584, 4688, 4, 295, 264, 3389, 300, 291, 1062, 312,
  1075, 281, 4584, 11, 597, 307, 920, 1101, 813, 291, 50786], "temperature": 0.0,
  "avg_logprob": -0.2220158760364239, "compression_ratio": 1.5648854961832062, "no_speech_prob":
  0.0027911229990422726}, {"id": 631, "seek": 256860, "start": 2577.04, "end": 2579.04,
  "text": " get just from a keyword search.", "tokens": [50786, 483, 445, 490, 257,
  20428, 3164, 13, 50886], "temperature": 0.0, "avg_logprob": -0.2220158760364239,
  "compression_ratio": 1.5648854961832062, "no_speech_prob": 0.0027911229990422726},
  {"id": 632, "seek": 256860, "start": 2579.04, "end": 2584.48, "text": " But the
  reality is, you know, how many companies have the budget to have NLP engineers and",
  "tokens": [50886, 583, 264, 4103, 307, 11, 291, 458, 11, 577, 867, 3431, 362, 264,
  4706, 281, 362, 426, 45196, 11955, 293, 51158], "temperature": 0.0, "avg_logprob":
  -0.2220158760364239, "compression_ratio": 1.5648854961832062, "no_speech_prob":
  0.0027911229990422726}, {"id": 633, "seek": 256860, "start": 2584.48, "end": 2586.2799999999997,
  "text": " data science and squeeze out that extra performance?", "tokens": [51158,
  1412, 3497, 293, 13578, 484, 300, 2857, 3389, 30, 51248], "temperature": 0.0, "avg_logprob":
  -0.2220158760364239, "compression_ratio": 1.5648854961832062, "no_speech_prob":
  0.0027911229990422726}, {"id": 634, "seek": 256860, "start": 2586.2799999999997,
  "end": 2588.7999999999997, "text": " It''s just not important in a lot of cases.",
  "tokens": [51248, 467, 311, 445, 406, 1021, 294, 257, 688, 295, 3331, 13, 51374],
  "temperature": 0.0, "avg_logprob": -0.2220158760364239, "compression_ratio": 1.5648854961832062,
  "no_speech_prob": 0.0027911229990422726}, {"id": 635, "seek": 256860, "start": 2588.7999999999997,
  "end": 2590.3199999999997, "text": " Yeah, exactly.", "tokens": [51374, 865, 11,
  2293, 13, 51450], "temperature": 0.0, "avg_logprob": -0.2220158760364239, "compression_ratio":
  1.5648854961832062, "no_speech_prob": 0.0027911229990422726}, {"id": 636, "seek":
  259032, "start": 2590.32, "end": 2601.1200000000003, "text": " And do you think
  that, you know, there is still a need to find a way to combine BM25 or", "tokens":
  [50364, 400, 360, 291, 519, 300, 11, 291, 458, 11, 456, 307, 920, 257, 643, 281,
  915, 257, 636, 281, 10432, 15901, 6074, 420, 50904], "temperature": 0.0, "avg_logprob":
  -0.2468852233886719, "compression_ratio": 1.638655462184874, "no_speech_prob": 0.005492100492119789},
  {"id": 637, "seek": 259032, "start": 2601.1200000000003, "end": 2605.6800000000003,
  "text": " whatever you have there, like the idea of Spark Search with the results
  from the nearest", "tokens": [50904, 2035, 291, 362, 456, 11, 411, 264, 1558, 295,
  23424, 17180, 365, 264, 3542, 490, 264, 23831, 51132], "temperature": 0.0, "avg_logprob":
  -0.2468852233886719, "compression_ratio": 1.638655462184874, "no_speech_prob": 0.005492100492119789},
  {"id": 638, "seek": 259032, "start": 2605.6800000000003, "end": 2607.0800000000004,
  "text": " neighbor search?", "tokens": [51132, 5987, 3164, 30, 51202], "temperature":
  0.0, "avg_logprob": -0.2468852233886719, "compression_ratio": 1.638655462184874,
  "no_speech_prob": 0.005492100492119789}, {"id": 639, "seek": 259032, "start": 2607.0800000000004,
  "end": 2609.2400000000002, "text": " Like have you been thinking about it?", "tokens":
  [51202, 1743, 362, 291, 668, 1953, 466, 309, 30, 51310], "temperature": 0.0, "avg_logprob":
  -0.2468852233886719, "compression_ratio": 1.638655462184874, "no_speech_prob": 0.005492100492119789},
  {"id": 640, "seek": 259032, "start": 2609.2400000000002, "end": 2614.4, "text":
  " Have you seen your clients kind of thinking about it or asking about it?", "tokens":
  [51310, 3560, 291, 1612, 428, 6982, 733, 295, 1953, 466, 309, 420, 3365, 466, 309,
  30, 51568], "temperature": 0.0, "avg_logprob": -0.2468852233886719, "compression_ratio":
  1.638655462184874, "no_speech_prob": 0.005492100492119789}, {"id": 641, "seek":
  259032, "start": 2614.4, "end": 2618.32, "text": " There''s a very interesting paper
  from Google about two years ago, Dave Dobson and I''m", "tokens": [51568, 821, 311,
  257, 588, 1880, 3035, 490, 3329, 466, 732, 924, 2057, 11, 11017, 1144, 929, 266,
  293, 286, 478, 51764], "temperature": 0.0, "avg_logprob": -0.2468852233886719, "compression_ratio":
  1.638655462184874, "no_speech_prob": 0.005492100492119789}, {"id": 642, "seek":
  261832, "start": 2618.32, "end": 2621.32, "text": " forgetting the other individuals.",
  "tokens": [50364, 25428, 264, 661, 5346, 13, 50514], "temperature": 0.0, "avg_logprob":
  -0.3059347735510932, "compression_ratio": 1.4413145539906103, "no_speech_prob":
  0.012042051181197166}, {"id": 643, "seek": 261832, "start": 2621.32, "end": 2629.56,
  "text": " They specifically on this topic, you can obviously model a BM25 search
  as, you know,", "tokens": [50514, 814, 4682, 322, 341, 4829, 11, 291, 393, 2745,
  2316, 257, 15901, 6074, 3164, 382, 11, 291, 458, 11, 50926], "temperature": 0.0,
  "avg_logprob": -0.3059347735510932, "compression_ratio": 1.4413145539906103, "no_speech_prob":
  0.012042051181197166}, {"id": 644, "seek": 261832, "start": 2629.56, "end": 2632.2400000000002,
  "text": " multiplication of Spark''s matrices.", "tokens": [50926, 27290, 295, 23424,
  311, 32284, 13, 51060], "temperature": 0.0, "avg_logprob": -0.3059347735510932,
  "compression_ratio": 1.4413145539906103, "no_speech_prob": 0.012042051181197166},
  {"id": 645, "seek": 261832, "start": 2632.2400000000002, "end": 2638.96, "text":
  " And so you can imagine your vectors essentially having a dense part produced by
  a neural network", "tokens": [51060, 400, 370, 291, 393, 3811, 428, 18875, 4476,
  1419, 257, 18011, 644, 7126, 538, 257, 18161, 3209, 51396], "temperature": 0.0,
  "avg_logprob": -0.3059347735510932, "compression_ratio": 1.4413145539906103, "no_speech_prob":
  0.012042051181197166}, {"id": 646, "seek": 261832, "start": 2638.96, "end": 2643.32,
  "text": " for instance, and then a very sparse tail or something.", "tokens": [51396,
  337, 5197, 11, 293, 550, 257, 588, 637, 11668, 6838, 420, 746, 13, 51614], "temperature":
  0.0, "avg_logprob": -0.3059347735510932, "compression_ratio": 1.4413145539906103,
  "no_speech_prob": 0.012042051181197166}, {"id": 647, "seek": 264332, "start": 2643.32,
  "end": 2650.6400000000003, "text": " And you actually want to perform dot products
  and how do you do it efficiently?", "tokens": [50364, 400, 291, 767, 528, 281, 2042,
  5893, 3383, 293, 577, 360, 291, 360, 309, 19621, 30, 50730], "temperature": 0.0,
  "avg_logprob": -0.2595584930912141, "compression_ratio": 1.704225352112676, "no_speech_prob":
  0.02395879663527012}, {"id": 648, "seek": 264332, "start": 2650.6400000000003, "end":
  2654.96, "text": " And the paper was going into some fascinating techniques for
  how to do that well.", "tokens": [50730, 400, 264, 3035, 390, 516, 666, 512, 10343,
  7512, 337, 577, 281, 360, 300, 731, 13, 50946], "temperature": 0.0, "avg_logprob":
  -0.2595584930912141, "compression_ratio": 1.704225352112676, "no_speech_prob": 0.02395879663527012},
  {"id": 649, "seek": 264332, "start": 2654.96, "end": 2657.7200000000003, "text":
  " So your question was like, do you see these merging?", "tokens": [50946, 407,
  428, 1168, 390, 411, 11, 360, 291, 536, 613, 44559, 30, 51084], "temperature": 0.0,
  "avg_logprob": -0.2595584930912141, "compression_ratio": 1.704225352112676, "no_speech_prob":
  0.02395879663527012}, {"id": 650, "seek": 264332, "start": 2657.7200000000003, "end":
  2663.28, "text": " And I think that, you know, I actually brought this up with the
  folks at Fires.", "tokens": [51084, 400, 286, 519, 300, 11, 291, 458, 11, 286, 767,
  3038, 341, 493, 365, 264, 4024, 412, 479, 3145, 13, 51362], "temperature": 0.0,
  "avg_logprob": -0.2595584930912141, "compression_ratio": 1.704225352112676, "no_speech_prob":
  0.02395879663527012}, {"id": 651, "seek": 264332, "start": 2663.28, "end": 2665.0800000000004,
  "text": " Is this something on your roadmap?", "tokens": [51362, 1119, 341, 746,
  322, 428, 35738, 30, 51452], "temperature": 0.0, "avg_logprob": -0.2595584930912141,
  "compression_ratio": 1.704225352112676, "no_speech_prob": 0.02395879663527012},
  {"id": 652, "seek": 264332, "start": 2665.0800000000004, "end": 2666.36, "text":
  " Is this something you''re interested in?", "tokens": [51452, 1119, 341, 746, 291,
  434, 3102, 294, 30, 51516], "temperature": 0.0, "avg_logprob": -0.2595584930912141,
  "compression_ratio": 1.704225352112676, "no_speech_prob": 0.02395879663527012},
  {"id": 653, "seek": 264332, "start": 2666.36, "end": 2668.44, "text": " They said,
  no, we''re not interested in this.", "tokens": [51516, 814, 848, 11, 572, 11, 321,
  434, 406, 3102, 294, 341, 13, 51620], "temperature": 0.0, "avg_logprob": -0.2595584930912141,
  "compression_ratio": 1.704225352112676, "no_speech_prob": 0.02395879663527012},
  {"id": 654, "seek": 264332, "start": 2668.44, "end": 2673.28, "text": " They''re
  specifically focused on either sparse or dense, but not high.", "tokens": [51620,
  814, 434, 4682, 5178, 322, 2139, 637, 11668, 420, 18011, 11, 457, 406, 1090, 13,
  51862], "temperature": 0.0, "avg_logprob": -0.2595584930912141, "compression_ratio":
  1.704225352112676, "no_speech_prob": 0.02395879663527012}, {"id": 655, "seek": 267328,
  "start": 2673.28, "end": 2677.28, "text": " And I think that it''s going to come
  down to this.", "tokens": [50364, 400, 286, 519, 300, 309, 311, 516, 281, 808, 760,
  281, 341, 13, 50564], "temperature": 0.0, "avg_logprob": -0.23729058150406723, "compression_ratio":
  1.5982142857142858, "no_speech_prob": 0.0033037937246263027}, {"id": 656, "seek":
  267328, "start": 2677.28, "end": 2687.28, "text": " If the utility of this sparse
  hybrid can be shown, then the technology is going to follow and try to create",
  "tokens": [50564, 759, 264, 14877, 295, 341, 637, 11668, 13051, 393, 312, 4898,
  11, 550, 264, 2899, 307, 516, 281, 1524, 293, 853, 281, 1884, 51064], "temperature":
  0.0, "avg_logprob": -0.23729058150406723, "compression_ratio": 1.5982142857142858,
  "no_speech_prob": 0.0033037937246263027}, {"id": 657, "seek": 267328, "start": 2687.28,
  "end": 2689.28, "text": " efficient implementations of it.", "tokens": [51064, 7148,
  4445, 763, 295, 309, 13, 51164], "temperature": 0.0, "avg_logprob": -0.23729058150406723,
  "compression_ratio": 1.5982142857142858, "no_speech_prob": 0.0033037937246263027},
  {"id": 658, "seek": 267328, "start": 2689.28, "end": 2695.28, "text": " I think
  that there are certainly classes of queries for which BM25 can''t be beat.", "tokens":
  [51164, 286, 519, 300, 456, 366, 3297, 5359, 295, 24109, 337, 597, 15901, 6074,
  393, 380, 312, 4224, 13, 51464], "temperature": 0.0, "avg_logprob": -0.23729058150406723,
  "compression_ratio": 1.5982142857142858, "no_speech_prob": 0.0033037937246263027},
  {"id": 659, "seek": 267328, "start": 2695.28, "end": 2700.28, "text": " And the
  exact keyword matching is going to be the correct way to do it in the future.",
  "tokens": [51464, 400, 264, 1900, 20428, 14324, 307, 516, 281, 312, 264, 3006, 636,
  281, 360, 309, 294, 264, 2027, 13, 51714], "temperature": 0.0, "avg_logprob": -0.23729058150406723,
  "compression_ratio": 1.5982142857142858, "no_speech_prob": 0.0033037937246263027},
  {"id": 660, "seek": 270028, "start": 2700.28, "end": 2704.28, "text": " So then
  you can take a few different strategies.", "tokens": [50364, 407, 550, 291, 393,
  747, 257, 1326, 819, 9029, 13, 50564], "temperature": 0.0, "avg_logprob": -0.11681803432079631,
  "compression_ratio": 1.7777777777777777, "no_speech_prob": 0.008699117228388786},
  {"id": 661, "seek": 270028, "start": 2704.28, "end": 2711.28, "text": " You can
  either try to classify the query when it''s received and then dispatch it to the
  correct back end.", "tokens": [50564, 509, 393, 2139, 853, 281, 33872, 264, 14581,
  562, 309, 311, 4613, 293, 550, 36729, 309, 281, 264, 3006, 646, 917, 13, 50914],
  "temperature": 0.0, "avg_logprob": -0.11681803432079631, "compression_ratio": 1.7777777777777777,
  "no_speech_prob": 0.008699117228388786}, {"id": 662, "seek": 270028, "start": 2711.28,
  "end": 2716.28, "text": " Or you can dispatch it to a sparse and a dense index and
  then merge with a re-ranger.", "tokens": [50914, 1610, 291, 393, 36729, 309, 281,
  257, 637, 11668, 293, 257, 18011, 8186, 293, 550, 22183, 365, 257, 319, 12, 81,
  3176, 13, 51164], "temperature": 0.0, "avg_logprob": -0.11681803432079631, "compression_ratio":
  1.7777777777777777, "no_speech_prob": 0.008699117228388786}, {"id": 663, "seek":
  270028, "start": 2716.28, "end": 2727.28, "text": " Or you can do this like truly
  hybrid system where you''re simultaneously doing the multiplication on the sparse
  and the dense pieces and producing a final list in like in one shot, not relying
  on a re-ranger.", "tokens": [51164, 1610, 291, 393, 360, 341, 411, 4908, 13051,
  1185, 689, 291, 434, 16561, 884, 264, 27290, 322, 264, 637, 11668, 293, 264, 18011,
  3755, 293, 10501, 257, 2572, 1329, 294, 411, 294, 472, 3347, 11, 406, 24140, 322,
  257, 319, 12, 81, 3176, 13, 51714], "temperature": 0.0, "avg_logprob": -0.11681803432079631,
  "compression_ratio": 1.7777777777777777, "no_speech_prob": 0.008699117228388786},
  {"id": 664, "seek": 272728, "start": 2727.28, "end": 2733.28, "text": " So it''s
  still an open area of research.", "tokens": [50364, 407, 309, 311, 920, 364, 1269,
  1859, 295, 2132, 13, 50664], "temperature": 0.0, "avg_logprob": -0.18982413208600388,
  "compression_ratio": 1.5194805194805194, "no_speech_prob": 0.0942075327038765},
  {"id": 665, "seek": 272728, "start": 2733.28, "end": 2734.28, "text": " Exactly.",
  "tokens": [50664, 7587, 13, 50714], "temperature": 0.0, "avg_logprob": -0.18982413208600388,
  "compression_ratio": 1.5194805194805194, "no_speech_prob": 0.0942075327038765},
  {"id": 666, "seek": 272728, "start": 2734.28, "end": 2736.28, "text": " And two
  things.", "tokens": [50714, 400, 732, 721, 13, 50814], "temperature": 0.0, "avg_logprob":
  -0.18982413208600388, "compression_ratio": 1.5194805194805194, "no_speech_prob":
  0.0942075327038765}, {"id": 667, "seek": 272728, "start": 2736.28, "end": 2739.28,
  "text": " Like I''m looking at it from the point of view of a customer.", "tokens":
  [50814, 1743, 286, 478, 1237, 412, 309, 490, 264, 935, 295, 1910, 295, 257, 5474,
  13, 50964], "temperature": 0.0, "avg_logprob": -0.18982413208600388, "compression_ratio":
  1.5194805194805194, "no_speech_prob": 0.0942075327038765}, {"id": 668, "seek": 272728,
  "start": 2739.28, "end": 2742.28, "text": " Let''s say I already have the M25 platform,
  right?", "tokens": [50964, 961, 311, 584, 286, 1217, 362, 264, 376, 6074, 3663,
  11, 558, 30, 51114], "temperature": 0.0, "avg_logprob": -0.18982413208600388, "compression_ratio":
  1.5194805194805194, "no_speech_prob": 0.0942075327038765}, {"id": 669, "seek": 272728,
  "start": 2742.28, "end": 2743.28, "text": " Base platform.", "tokens": [51114, 21054,
  3663, 13, 51164], "temperature": 0.0, "avg_logprob": -0.18982413208600388, "compression_ratio":
  1.5194805194805194, "no_speech_prob": 0.0942075327038765}, {"id": 670, "seek": 272728,
  "start": 2743.28, "end": 2746.28, "text": " And so I''m curious.", "tokens": [51164,
  400, 370, 286, 478, 6369, 13, 51314], "temperature": 0.0, "avg_logprob": -0.18982413208600388,
  "compression_ratio": 1.5194805194805194, "no_speech_prob": 0.0942075327038765},
  {"id": 671, "seek": 272728, "start": 2746.28, "end": 2749.28, "text": " Okay. So
  I''m curious to see what vector search can bring me.", "tokens": [51314, 1033, 13,
  407, 286, 478, 6369, 281, 536, 437, 8062, 3164, 393, 1565, 385, 13, 51464], "temperature":
  0.0, "avg_logprob": -0.18982413208600388, "compression_ratio": 1.5194805194805194,
  "no_speech_prob": 0.0942075327038765}, {"id": 672, "seek": 272728, "start": 2749.28,
  "end": 2755.28, "text": " And maybe I''m thinking about introducing this as an explorative
  search feature.", "tokens": [51464, 400, 1310, 286, 478, 1953, 466, 15424, 341,
  382, 364, 24765, 1166, 3164, 4111, 13, 51764], "temperature": 0.0, "avg_logprob":
  -0.18982413208600388, "compression_ratio": 1.5194805194805194, "no_speech_prob":
  0.0942075327038765}, {"id": 673, "seek": 275528, "start": 2755.28, "end": 2761.28,
  "text": " So because I''m not sure if it''s going to fly for my documents or for
  my items in the database, right?", "tokens": [50364, 407, 570, 286, 478, 406, 988,
  498, 309, 311, 516, 281, 3603, 337, 452, 8512, 420, 337, 452, 4754, 294, 264, 8149,
  11, 558, 30, 50664], "temperature": 0.0, "avg_logprob": -0.13929992344068445, "compression_ratio":
  1.6754716981132076, "no_speech_prob": 0.0034120010677725077}, {"id": 674, "seek":
  275528, "start": 2761.28, "end": 2769.28, "text": " So that''s one potential to
  think about, okay, as you said, I can actually route this query to both sparse and
  dense retrieval.", "tokens": [50664, 407, 300, 311, 472, 3995, 281, 519, 466, 11,
  1392, 11, 382, 291, 848, 11, 286, 393, 767, 7955, 341, 14581, 281, 1293, 637, 11668,
  293, 18011, 19817, 3337, 13, 51064], "temperature": 0.0, "avg_logprob": -0.13929992344068445,
  "compression_ratio": 1.6754716981132076, "no_speech_prob": 0.0034120010677725077},
  {"id": 675, "seek": 275528, "start": 2769.28, "end": 2773.28, "text": " And then
  maybe combine them in some linear formula, even.", "tokens": [51064, 400, 550, 1310,
  10432, 552, 294, 512, 8213, 8513, 11, 754, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.13929992344068445, "compression_ratio": 1.6754716981132076, "no_speech_prob":
  0.0034120010677725077}, {"id": 676, "seek": 275528, "start": 2773.28, "end": 2782.28,
  "text": " And I can give like a smaller score, lower score to, to, or wait to the
  dense part and then higher to the sparse part because I still believe in sparse
  part.", "tokens": [51264, 400, 286, 393, 976, 411, 257, 4356, 6175, 11, 3126, 6175,
  281, 11, 281, 11, 420, 1699, 281, 264, 18011, 644, 293, 550, 2946, 281, 264, 637,
  11668, 644, 570, 286, 920, 1697, 294, 637, 11668, 644, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.13929992344068445, "compression_ratio": 1.6754716981132076,
  "no_speech_prob": 0.0034120010677725077}, {"id": 677, "seek": 278228, "start": 2782.28,
  "end": 2786.28, "text": " And that''s how my users are expecting results to be there.",
  "tokens": [50364, 400, 300, 311, 577, 452, 5022, 366, 9650, 3542, 281, 312, 456,
  13, 50564], "temperature": 0.0, "avg_logprob": -0.1715029529017261, "compression_ratio":
  1.6131386861313868, "no_speech_prob": 0.0059082768857479095}, {"id": 678, "seek":
  278228, "start": 2786.28, "end": 2789.28, "text": " But then maybe I can surface
  some magic like Q and A, right?", "tokens": [50564, 583, 550, 1310, 286, 393, 3753,
  512, 5585, 411, 1249, 293, 316, 11, 558, 30, 50714], "temperature": 0.0, "avg_logprob":
  -0.1715029529017261, "compression_ratio": 1.6131386861313868, "no_speech_prob":
  0.0059082768857479095}, {"id": 679, "seek": 278228, "start": 2789.28, "end": 2792.28,
  "text": " So they asked the question and I can give them the answer.", "tokens":
  [50714, 407, 436, 2351, 264, 1168, 293, 286, 393, 976, 552, 264, 1867, 13, 50864],
  "temperature": 0.0, "avg_logprob": -0.1715029529017261, "compression_ratio": 1.6131386861313868,
  "no_speech_prob": 0.0059082768857479095}, {"id": 680, "seek": 278228, "start": 2792.28,
  "end": 2794.28, "text": " And that might be really interesting.", "tokens": [50864,
  400, 300, 1062, 312, 534, 1880, 13, 50964], "temperature": 0.0, "avg_logprob": -0.1715029529017261,
  "compression_ratio": 1.6131386861313868, "no_speech_prob": 0.0059082768857479095},
  {"id": 681, "seek": 278228, "start": 2794.28, "end": 2798.28, "text": " And the
  second point, there was a paper called beer.", "tokens": [50964, 400, 264, 1150,
  935, 11, 456, 390, 257, 3035, 1219, 8795, 13, 51164], "temperature": 0.0, "avg_logprob":
  -0.1715029529017261, "compression_ratio": 1.6131386861313868, "no_speech_prob":
  0.0059082768857479095}, {"id": 682, "seek": 278228, "start": 2798.28, "end": 2803.28,
  "text": " B E I R. I will make sure that all of the papers will be linked here in
  the show notes.", "tokens": [51164, 363, 462, 286, 497, 13, 286, 486, 652, 988,
  300, 439, 295, 264, 10577, 486, 312, 9408, 510, 294, 264, 855, 5570, 13, 51414],
  "temperature": 0.0, "avg_logprob": -0.1715029529017261, "compression_ratio": 1.6131386861313868,
  "no_speech_prob": 0.0059082768857479095}, {"id": 683, "seek": 278228, "start": 2803.28,
  "end": 2810.28, "text": " But that paper actually compared a dense retrieval versus
  BM25 on a number of tasks.", "tokens": [51414, 583, 300, 3035, 767, 5347, 257, 18011,
  19817, 3337, 5717, 15901, 6074, 322, 257, 1230, 295, 9608, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.1715029529017261, "compression_ratio": 1.6131386861313868,
  "no_speech_prob": 0.0059082768857479095}, {"id": 684, "seek": 281028, "start": 2810.28,
  "end": 2813.28, "text": " Right? So you can have a search.", "tokens": [50364, 1779,
  30, 407, 291, 393, 362, 257, 3164, 13, 50514], "temperature": 0.0, "avg_logprob":
  -0.16128367236536792, "compression_ratio": 1.6216216216216217, "no_speech_prob":
  0.01648273691534996}, {"id": 685, "seek": 281028, "start": 2813.28, "end": 2817.28,
  "text": " You can have a question answering and leaves goes on.", "tokens": [50514,
  509, 393, 362, 257, 1168, 13430, 293, 5510, 1709, 322, 13, 50714], "temperature":
  0.0, "avg_logprob": -0.16128367236536792, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.01648273691534996}, {"id": 686, "seek": 281028, "start": 2817.28,
  "end": 2821.28, "text": " And so what they showed is that BM25 is fairly competitive.",
  "tokens": [50714, 400, 370, 437, 436, 4712, 307, 300, 15901, 6074, 307, 6457, 10043,
  13, 50914], "temperature": 0.0, "avg_logprob": -0.16128367236536792, "compression_ratio":
  1.6216216216216217, "no_speech_prob": 0.01648273691534996}, {"id": 687, "seek":
  281028, "start": 2821.28, "end": 2827.28, "text": " It actually is above dense retrieval
  methods like on zero, zero short retrieval.", "tokens": [50914, 467, 767, 307, 3673,
  18011, 19817, 3337, 7150, 411, 322, 4018, 11, 4018, 2099, 19817, 3337, 13, 51214],
  "temperature": 0.0, "avg_logprob": -0.16128367236536792, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.01648273691534996}, {"id": 688, "seek": 281028, "start": 2827.28,
  "end": 2829.28, "text": " Right? So like you didn''t find you in this model.", "tokens":
  [51214, 1779, 30, 407, 411, 291, 994, 380, 915, 291, 294, 341, 2316, 13, 51314],
  "temperature": 0.0, "avg_logprob": -0.16128367236536792, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.01648273691534996}, {"id": 689, "seek": 281028, "start": 2829.28,
  "end": 2833.28, "text": " So you just took them off the shelf. Here is the task.
  Let''s compare. Right?", "tokens": [51314, 407, 291, 445, 1890, 552, 766, 264, 15222,
  13, 1692, 307, 264, 5633, 13, 961, 311, 6794, 13, 1779, 30, 51514], "temperature":
  0.0, "avg_logprob": -0.16128367236536792, "compression_ratio": 1.6216216216216217,
  "no_speech_prob": 0.01648273691534996}, {"id": 690, "seek": 281028, "start": 2833.28,
  "end": 2835.28, "text": " BM25 is very stable.", "tokens": [51514, 15901, 6074,
  307, 588, 8351, 13, 51614], "temperature": 0.0, "avg_logprob": -0.16128367236536792,
  "compression_ratio": 1.6216216216216217, "no_speech_prob": 0.01648273691534996},
  {"id": 691, "seek": 281028, "start": 2835.28, "end": 2838.28, "text": " So just
  few models actually outperformed it.", "tokens": [51614, 407, 445, 1326, 5245, 767,
  484, 610, 22892, 309, 13, 51764], "temperature": 0.0, "avg_logprob": -0.16128367236536792,
  "compression_ratio": 1.6216216216216217, "no_speech_prob": 0.01648273691534996},
  {"id": 692, "seek": 283828, "start": 2838.28, "end": 2845.28, "text": " And so in
  that sense, it sounds like BM25 is here to stay. What do you think?", "tokens":
  [50364, 400, 370, 294, 300, 2020, 11, 309, 3263, 411, 15901, 6074, 307, 510, 281,
  1754, 13, 708, 360, 291, 519, 30, 50714], "temperature": 0.0, "avg_logprob": -0.17544059753417968,
  "compression_ratio": 1.5267489711934157, "no_speech_prob": 0.13621282577514648},
  {"id": 693, "seek": 283828, "start": 2845.28, "end": 2847.28, "text": " I agree
  with you.", "tokens": [50714, 286, 3986, 365, 291, 13, 50814], "temperature": 0.0,
  "avg_logprob": -0.17544059753417968, "compression_ratio": 1.5267489711934157, "no_speech_prob":
  0.13621282577514648}, {"id": 694, "seek": 283828, "start": 2847.28, "end": 2859.28,
  "text": " And again, this is where our scope is as a company is on building an end
  to end information retrieval pipeline, which means that, okay, today, we have a
  neural dense retrieval.", "tokens": [50814, 400, 797, 11, 341, 307, 689, 527, 11923,
  307, 382, 257, 2237, 307, 322, 2390, 364, 917, 281, 917, 1589, 19817, 3337, 15517,
  11, 597, 1355, 300, 11, 1392, 11, 965, 11, 321, 362, 257, 18161, 18011, 19817, 3337,
  13, 51414], "temperature": 0.0, "avg_logprob": -0.17544059753417968, "compression_ratio":
  1.5267489711934157, "no_speech_prob": 0.13621282577514648}, {"id": 695, "seek":
  283828, "start": 2859.28, "end": 2862.28, "text": " Because the M25 has been done,
  right?", "tokens": [51414, 1436, 264, 376, 6074, 575, 668, 1096, 11, 558, 30, 51564],
  "temperature": 0.0, "avg_logprob": -0.17544059753417968, "compression_ratio": 1.5267489711934157,
  "no_speech_prob": 0.13621282577514648}, {"id": 696, "seek": 283828, "start": 2862.28,
  "end": 2863.28, "text": " It''s in the scene.", "tokens": [51564, 467, 311, 294,
  264, 4145, 13, 51614], "temperature": 0.0, "avg_logprob": -0.17544059753417968,
  "compression_ratio": 1.5267489711934157, "no_speech_prob": 0.13621282577514648},
  {"id": 697, "seek": 283828, "start": 2863.28, "end": 2865.28, "text": " It''s well
  understood how to implement it.", "tokens": [51614, 467, 311, 731, 7320, 577, 281,
  4445, 309, 13, 51714], "temperature": 0.0, "avg_logprob": -0.17544059753417968,
  "compression_ratio": 1.5267489711934157, "no_speech_prob": 0.13621282577514648},
  {"id": 698, "seek": 286528, "start": 2865.28, "end": 2871.28, "text": " Although
  there are some tricks to actually make the M25 work even better than my off the
  shelf implementations.", "tokens": [50364, 5780, 456, 366, 512, 11733, 281, 767,
  652, 264, 376, 6074, 589, 754, 1101, 813, 452, 766, 264, 15222, 4445, 763, 13, 50664],
  "temperature": 0.0, "avg_logprob": -0.15374137445823433, "compression_ratio": 1.578125,
  "no_speech_prob": 0.021132908761501312}, {"id": 699, "seek": 286528, "start": 2871.28,
  "end": 2873.28, "text": " But what.", "tokens": [50664, 583, 437, 13, 50764], "temperature":
  0.0, "avg_logprob": -0.15374137445823433, "compression_ratio": 1.578125, "no_speech_prob":
  0.021132908761501312}, {"id": 700, "seek": 286528, "start": 2873.28, "end": 2881.28,
  "text": " Where we want to eventually get to is we could potentially build the BM25
  and dense indexes for our customers.", "tokens": [50764, 2305, 321, 528, 281, 4728,
  483, 281, 307, 321, 727, 7263, 1322, 264, 15901, 6074, 293, 18011, 8186, 279, 337,
  527, 4581, 13, 51164], "temperature": 0.0, "avg_logprob": -0.15374137445823433,
  "compression_ratio": 1.578125, "no_speech_prob": 0.021132908761501312}, {"id": 701,
  "seek": 286528, "start": 2881.28, "end": 2883.28, "text": " And then return.", "tokens":
  [51164, 400, 550, 2736, 13, 51264], "temperature": 0.0, "avg_logprob": -0.15374137445823433,
  "compression_ratio": 1.578125, "no_speech_prob": 0.021132908761501312}, {"id": 702,
  "seek": 286528, "start": 2883.28, "end": 2886.28, "text": " We''re trying to just
  serve the best results possible.", "tokens": [51264, 492, 434, 1382, 281, 445, 4596,
  264, 1151, 3542, 1944, 13, 51414], "temperature": 0.0, "avg_logprob": -0.15374137445823433,
  "compression_ratio": 1.578125, "no_speech_prob": 0.021132908761501312}, {"id": 703,
  "seek": 286528, "start": 2886.28, "end": 2891.28, "text": " So for instance, you
  could take even sometimes even very simple heuristics work single word queries.",
  "tokens": [51414, 407, 337, 5197, 11, 291, 727, 747, 754, 2171, 754, 588, 2199,
  415, 374, 6006, 589, 2167, 1349, 24109, 13, 51664], "temperature": 0.0, "avg_logprob":
  -0.15374137445823433, "compression_ratio": 1.578125, "no_speech_prob": 0.021132908761501312},
  {"id": 704, "seek": 289128, "start": 2891.28, "end": 2896.28, "text": " Often BM25
  is how you want to serve them, not not not from a dense index.", "tokens": [50364,
  20043, 15901, 6074, 307, 577, 291, 528, 281, 4596, 552, 11, 406, 406, 406, 490,
  257, 18011, 8186, 13, 50614], "temperature": 0.0, "avg_logprob": -0.13678568601608276,
  "compression_ratio": 1.7098976109215016, "no_speech_prob": 0.08786576986312866},
  {"id": 705, "seek": 289128, "start": 2896.28, "end": 2900.28, "text": " So if it''s
  a single word query, okay, you''re going to be on 25 search.", "tokens": [50614,
  407, 498, 309, 311, 257, 2167, 1349, 14581, 11, 1392, 11, 291, 434, 516, 281, 312,
  322, 3552, 3164, 13, 50814], "temperature": 0.0, "avg_logprob": -0.13678568601608276,
  "compression_ratio": 1.7098976109215016, "no_speech_prob": 0.08786576986312866},
  {"id": 706, "seek": 289128, "start": 2900.28, "end": 2903.28, "text": " If it''s
  anything longer than one word run, then search.", "tokens": [50814, 759, 309, 311,
  1340, 2854, 813, 472, 1349, 1190, 11, 550, 3164, 13, 50964], "temperature": 0.0,
  "avg_logprob": -0.13678568601608276, "compression_ratio": 1.7098976109215016, "no_speech_prob":
  0.08786576986312866}, {"id": 707, "seek": 289128, "start": 2903.28, "end": 2908.28,
  "text": " That''s not a very principled approach. I''m just pointing out that, you
  know, what''s going on behind the scenes.", "tokens": [50964, 663, 311, 406, 257,
  588, 3681, 15551, 3109, 13, 286, 478, 445, 12166, 484, 300, 11, 291, 458, 11, 437,
  311, 516, 322, 2261, 264, 8026, 13, 51214], "temperature": 0.0, "avg_logprob": -0.13678568601608276,
  "compression_ratio": 1.7098976109215016, "no_speech_prob": 0.08786576986312866},
  {"id": 708, "seek": 289128, "start": 2908.28, "end": 2919.28, "text": " That''s
  the intelligence of the platform to provide and we''re not really restricted or
  married to a vector database or only a vector database, powering powering the search
  of this platform.", "tokens": [51214, 663, 311, 264, 7599, 295, 264, 3663, 281,
  2893, 293, 321, 434, 406, 534, 20608, 420, 5259, 281, 257, 8062, 8149, 420, 787,
  257, 8062, 8149, 11, 1347, 278, 1347, 278, 264, 3164, 295, 341, 3663, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.13678568601608276, "compression_ratio": 1.7098976109215016,
  "no_speech_prob": 0.08786576986312866}, {"id": 709, "seek": 291928, "start": 2919.28,
  "end": 2922.28, "text": " Yeah, yeah, that makes sense.", "tokens": [50364, 865,
  11, 1338, 11, 300, 1669, 2020, 13, 50514], "temperature": 0.0, "avg_logprob": -0.32465085116299713,
  "compression_ratio": 1.6121495327102804, "no_speech_prob": 0.026882139965891838},
  {"id": 710, "seek": 291928, "start": 2922.28, "end": 2935.28, "text": " So is does
  that manifest in some way in your product that I as a user can have the flexibility
  and how my search is processed is going to go the sparse route or is it going to
  go the the density tree will.", "tokens": [50514, 407, 307, 775, 300, 10067, 294,
  512, 636, 294, 428, 1674, 300, 286, 382, 257, 4195, 393, 362, 264, 12635, 293, 577,
  452, 3164, 307, 18846, 307, 516, 281, 352, 264, 637, 11668, 7955, 420, 307, 309,
  516, 281, 352, 264, 264, 10305, 4230, 486, 13, 51164], "temperature": 0.0, "avg_logprob":
  -0.32465085116299713, "compression_ratio": 1.6121495327102804, "no_speech_prob":
  0.026882139965891838}, {"id": 711, "seek": 291928, "start": 2935.28, "end": 2940.28,
  "text": " No, we don''t so at the moment we''re only doing the answer tree will
  because we feel like that''s the interest.", "tokens": [51164, 883, 11, 321, 500,
  380, 370, 412, 264, 1623, 321, 434, 787, 884, 264, 1867, 4230, 486, 570, 321, 841,
  411, 300, 311, 264, 1179, 13, 51414], "temperature": 0.0, "avg_logprob": -0.32465085116299713,
  "compression_ratio": 1.6121495327102804, "no_speech_prob": 0.026882139965891838},
  {"id": 712, "seek": 294028, "start": 2940.28, "end": 2947.28, "text": " We can add
  that we can add the BM25 parts without a lot of difficulty in six months from now
  or something like that.", "tokens": [50364, 492, 393, 909, 300, 321, 393, 909, 264,
  15901, 6074, 3166, 1553, 257, 688, 295, 10360, 294, 2309, 2493, 490, 586, 420, 746,
  411, 300, 13, 50714], "temperature": 0.0, "avg_logprob": -0.1677037779107151, "compression_ratio":
  1.6093023255813954, "no_speech_prob": 0.1522897183895111}, {"id": 713, "seek": 294028,
  "start": 2947.28, "end": 2954.28, "text": " So, but we do provide a few different
  flavors of the dense retrieval because there''s a few.", "tokens": [50714, 407,
  11, 457, 321, 360, 2893, 257, 1326, 819, 16303, 295, 264, 18011, 19817, 3337, 570,
  456, 311, 257, 1326, 13, 51064], "temperature": 0.0, "avg_logprob": -0.1677037779107151,
  "compression_ratio": 1.6093023255813954, "no_speech_prob": 0.1522897183895111},
  {"id": 714, "seek": 294028, "start": 2954.28, "end": 2960.28, "text": " There''s
  question answering so the user puts it or query answering the user puts a query
  in and then you''re trying to find good responses.", "tokens": [51064, 821, 311,
  1168, 13430, 370, 264, 4195, 8137, 309, 420, 14581, 13430, 264, 4195, 8137, 257,
  14581, 294, 293, 550, 291, 434, 1382, 281, 915, 665, 13019, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.1677037779107151, "compression_ratio": 1.6093023255813954,
  "no_speech_prob": 0.1522897183895111}, {"id": 715, "seek": 296028, "start": 2960.28,
  "end": 2972.28, "text": " There''s also another task which is semantic similarity,
  which is closely related, but it''s like I make a statement and I just want to find
  similar statements so my statement is not necessarily a question that I''m looking
  for an answer to.", "tokens": [50364, 821, 311, 611, 1071, 5633, 597, 307, 47982,
  32194, 11, 597, 307, 8185, 4077, 11, 457, 309, 311, 411, 286, 652, 257, 5629, 293,
  286, 445, 528, 281, 915, 2531, 12363, 370, 452, 5629, 307, 406, 4725, 257, 1168,
  300, 286, 478, 1237, 337, 364, 1867, 281, 13, 50964], "temperature": 0.0, "avg_logprob":
  -0.15994347965016084, "compression_ratio": 1.8826291079812207, "no_speech_prob":
  0.048425037413835526}, {"id": 716, "seek": 296028, "start": 2972.28, "end": 2984.28,
  "text": " I just want to find semantically similar statements and then the other
  thing is question question similarity often comes up it comes up usually in the
  not not in.", "tokens": [50964, 286, 445, 528, 281, 915, 4361, 49505, 2531, 12363,
  293, 550, 264, 661, 551, 307, 1168, 1168, 32194, 2049, 1487, 493, 309, 1487, 493,
  2673, 294, 264, 406, 406, 294, 13, 51564], "temperature": 0.0, "avg_logprob": -0.15994347965016084,
  "compression_ratio": 1.8826291079812207, "no_speech_prob": 0.048425037413835526},
  {"id": 717, "seek": 298428, "start": 2984.28, "end": 2991.28, "text": " Well, you''ve
  seen it in Google for instance when you type with query and then it says people
  also ask these questions and they get these similar questions right.", "tokens":
  [50364, 1042, 11, 291, 600, 1612, 309, 294, 3329, 337, 5197, 562, 291, 2010, 365,
  14581, 293, 550, 309, 1619, 561, 611, 1029, 613, 1651, 293, 436, 483, 613, 2531,
  1651, 558, 13, 50714], "temperature": 0.0, "avg_logprob": -0.12817928194999695,
  "compression_ratio": 1.7479674796747968, "no_speech_prob": 0.010657334700226784},
  {"id": 718, "seek": 298428, "start": 2991.28, "end": 3002.28, "text": " So there''s
  use cases for question question similarity and so we support all three of those
  modes of operation and we allow at query time our customers to specify which mode
  they''re trying to run it.", "tokens": [50714, 407, 456, 311, 764, 3331, 337, 1168,
  1168, 32194, 293, 370, 321, 1406, 439, 1045, 295, 729, 14068, 295, 6916, 293, 321,
  2089, 412, 14581, 565, 527, 4581, 281, 16500, 597, 4391, 436, 434, 1382, 281, 1190,
  309, 13, 51264], "temperature": 0.0, "avg_logprob": -0.12817928194999695, "compression_ratio":
  1.7479674796747968, "no_speech_prob": 0.010657334700226784}, {"id": 719, "seek":
  298428, "start": 3002.28, "end": 3007.28, "text": " Yeah, yeah, that makes sense
  that makes a lot of sense and of course.", "tokens": [51264, 865, 11, 1338, 11,
  300, 1669, 2020, 300, 1669, 257, 688, 295, 2020, 293, 295, 1164, 13, 51514], "temperature":
  0.0, "avg_logprob": -0.12817928194999695, "compression_ratio": 1.7479674796747968,
  "no_speech_prob": 0.010657334700226784}, {"id": 720, "seek": 300728, "start": 3007.28,
  "end": 3032.28, "text": " One thing that I keep thinking about is let''s say when
  we introduce the sparse search let''s say Bm 25 and some customer comes in and it''s
  not English language it''s something else right then you need to bring in also the
  tokenization and other things from maybe from Lucene and of course, Lucene is a
  library in principle it could be wrapped in a Docker image and you can do that job
  right.", "tokens": [50364, 1485, 551, 300, 286, 1066, 1953, 466, 307, 718, 311,
  584, 562, 321, 5366, 264, 637, 11668, 3164, 718, 311, 584, 363, 76, 3552, 293, 512,
  5474, 1487, 294, 293, 309, 311, 406, 3669, 2856, 309, 311, 746, 1646, 558, 550,
  291, 643, 281, 1565, 294, 611, 264, 14862, 2144, 293, 661, 721, 490, 1310, 490,
  9593, 1450, 293, 295, 1164, 11, 9593, 1450, 307, 257, 6405, 294, 8665, 309, 727,
  312, 14226, 294, 257, 33772, 3256, 293, 291, 393, 360, 300, 1691, 558, 13, 51614],
  "temperature": 0.0, "avg_logprob": -0.2221856920906667, "compression_ratio": 1.6208333333333333,
  "no_speech_prob": 0.13411051034927368}, {"id": 721, "seek": 303228, "start": 3032.28,
  "end": 3040.28, "text": " But then the question is can you easily married so that
  it is production grade between different platforms and languages.", "tokens": [50364,
  583, 550, 264, 1168, 307, 393, 291, 3612, 5259, 370, 300, 309, 307, 4265, 7204,
  1296, 819, 9473, 293, 8650, 13, 50764], "temperature": 0.0, "avg_logprob": -0.19335718557868206,
  "compression_ratio": 1.5454545454545454, "no_speech_prob": 0.03915693610906601},
  {"id": 722, "seek": 303228, "start": 3040.28, "end": 3050.28, "text": " And it''s
  surprising Lucene has come a long way so there''s come long in terms of providing
  a good sense out of defaults out of the box in terms of stop wordless and stemming
  but I have.", "tokens": [50764, 400, 309, 311, 8830, 9593, 1450, 575, 808, 257,
  938, 636, 370, 456, 311, 808, 938, 294, 2115, 295, 6530, 257, 665, 2020, 484, 295,
  7576, 82, 484, 295, 264, 2424, 294, 2115, 295, 1590, 1349, 1832, 293, 12312, 2810,
  457, 286, 362, 13, 51264], "temperature": 0.0, "avg_logprob": -0.19335718557868206,
  "compression_ratio": 1.5454545454545454, "no_speech_prob": 0.03915693610906601},
  {"id": 723, "seek": 305028, "start": 3051.28, "end": 3062.28, "text": " My daughter
  school started using this like a product that manages communication between the
  school and the parents and that thing was clearly using.", "tokens": [50414, 1222,
  4653, 1395, 1409, 1228, 341, 411, 257, 1674, 300, 22489, 6101, 1296, 264, 1395,
  293, 264, 3152, 293, 300, 551, 390, 4448, 1228, 13, 50964], "temperature": 0.0,
  "avg_logprob": -0.151140343059193, "compression_ratio": 1.7095435684647302, "no_speech_prob":
  0.09328672289848328}, {"id": 724, "seek": 305028, "start": 3062.28, "end": 3077.28,
  "text": " You know, Lucene or solar elastic search and they didn''t have the stemming
  configured properly and I didn''t know as possible to misto misconfigure that so
  I was searching for vaccine and it couldn''t find find it because it was vaccination
  in the title over there.", "tokens": [50964, 509, 458, 11, 9593, 1450, 420, 7936,
  17115, 3164, 293, 436, 994, 380, 362, 264, 12312, 2810, 30538, 6108, 293, 286, 994,
  380, 458, 382, 1944, 281, 3544, 78, 3346, 1671, 20646, 540, 300, 370, 286, 390,
  10808, 337, 7007, 293, 309, 2809, 380, 915, 915, 309, 570, 309, 390, 16498, 294,
  264, 4876, 670, 456, 13, 51714], "temperature": 0.0, "avg_logprob": -0.151140343059193,
  "compression_ratio": 1.7095435684647302, "no_speech_prob": 0.09328672289848328},
  {"id": 725, "seek": 307728, "start": 3077.28, "end": 3089.28, "text": " So yeah,
  so with the with the neurosurgeon is kind of a little bit more bullet proof, you
  know, it''s it''s a bit more immune to these kinds of mistakes and those misspellings
  very easily.", "tokens": [50364, 407, 1338, 11, 370, 365, 264, 365, 264, 28813,
  374, 11641, 307, 733, 295, 257, 707, 857, 544, 11632, 8177, 11, 291, 458, 11, 309,
  311, 309, 311, 257, 857, 544, 11992, 281, 613, 3685, 295, 8038, 293, 729, 1713,
  49241, 1109, 588, 3612, 13, 50964], "temperature": 0.0, "avg_logprob": -0.20593896204111528,
  "compression_ratio": 1.6680161943319838, "no_speech_prob": 0.049178414046764374},
  {"id": 726, "seek": 307728, "start": 3089.28, "end": 3102.28, "text": " Yeah, yeah,
  especially I think there is also a paper about I think it was from Google you know
  to train on bite level and so you will not be constrained by okay the complexity
  of the language because you have like bite level.", "tokens": [50964, 865, 11, 1338,
  11, 2318, 286, 519, 456, 307, 611, 257, 3035, 466, 286, 519, 309, 390, 490, 3329,
  291, 458, 281, 3847, 322, 7988, 1496, 293, 370, 291, 486, 406, 312, 38901, 538,
  1392, 264, 14024, 295, 264, 2856, 570, 291, 362, 411, 7988, 1496, 13, 51614], "temperature":
  0.0, "avg_logprob": -0.20593896204111528, "compression_ratio": 1.6680161943319838,
  "no_speech_prob": 0.049178414046764374}, {"id": 727, "seek": 310228, "start": 3102.28,
  "end": 3111.28, "text": " Definitions and and so in principle your model should
  be robust to typos and misspellings and so on and some of them come from speech
  right so.", "tokens": [50364, 46245, 2451, 293, 293, 370, 294, 8665, 428, 2316,
  820, 312, 13956, 281, 2125, 329, 293, 1713, 49241, 1109, 293, 370, 322, 293, 512,
  295, 552, 808, 490, 6218, 558, 370, 13, 50814], "temperature": 0.0, "avg_logprob":
  -0.09581869076459835, "compression_ratio": 1.7211538461538463, "no_speech_prob":
  0.06103605777025223}, {"id": 728, "seek": 310228, "start": 3112.28, "end": 3127.28,
  "text": " Exactly exactly yeah and it sounds like interesting like the example you
  brought up with your daughter school like system like it sounds like largely search
  is still broken it''s like like the moment you go to some.", "tokens": [50864, 7587,
  2293, 1338, 293, 309, 3263, 411, 1880, 411, 264, 1365, 291, 3038, 493, 365, 428,
  4653, 1395, 411, 1185, 411, 309, 3263, 411, 11611, 3164, 307, 920, 5463, 309, 311,
  411, 411, 264, 1623, 291, 352, 281, 512, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.09581869076459835, "compression_ratio": 1.7211538461538463, "no_speech_prob":
  0.06103605777025223}, {"id": 729, "seek": 312728, "start": 3127.28, "end": 3154.28,
  "text": " System which is let''s say for public use right like it''s not necessarily
  designed for for findability there it exists and you know like like Daniel tanker
  lung I think he says like the funny part of search industry in general is that when
  search engine works nobody will go and praise you they just use it when it doesn''t
  work they will blame you so you always air on on that.", "tokens": [50364, 8910,
  597, 307, 718, 311, 584, 337, 1908, 764, 558, 411, 309, 311, 406, 4725, 4761, 337,
  337, 915, 2310, 456, 309, 8198, 293, 291, 458, 411, 411, 8033, 5466, 260, 16730,
  286, 519, 415, 1619, 411, 264, 4074, 644, 295, 3164, 3518, 294, 2674, 307, 300,
  562, 3164, 2848, 1985, 5079, 486, 352, 293, 13286, 291, 436, 445, 764, 309, 562,
  309, 1177, 380, 589, 436, 486, 10127, 291, 370, 291, 1009, 1988, 322, 322, 300,
  13, 51714], "temperature": 0.0, "avg_logprob": -0.20001648693549923, "compression_ratio":
  1.6491228070175439, "no_speech_prob": 0.06799925118684769}, {"id": 730, "seek":
  315428, "start": 3154.28, "end": 3163.28, "text": " How do you feel about that like
  is this also the potential for your company to go and fix many of these broken use
  cases.", "tokens": [50364, 1012, 360, 291, 841, 466, 300, 411, 307, 341, 611, 264,
  3995, 337, 428, 2237, 281, 352, 293, 3191, 867, 295, 613, 5463, 764, 3331, 13, 50814],
  "temperature": 0.0, "avg_logprob": -0.1565423398404508, "compression_ratio": 1.591549295774648,
  "no_speech_prob": 0.08269992470741272}, {"id": 731, "seek": 315428, "start": 3163.28,
  "end": 3182.28, "text": " Well that certainly that certainly actually our vision
  that we will make it very easy for SAS companies to provide a much more in Google
  like search experience in their products so when it comes to web say that let''s.",
  "tokens": [50814, 1042, 300, 3297, 300, 3297, 767, 527, 5201, 300, 321, 486, 652,
  309, 588, 1858, 337, 33441, 3431, 281, 2893, 257, 709, 544, 294, 3329, 411, 3164,
  1752, 294, 641, 3383, 370, 562, 309, 1487, 281, 3670, 584, 300, 718, 311, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.1565423398404508, "compression_ratio": 1.591549295774648,
  "no_speech_prob": 0.08269992470741272}, {"id": 732, "seek": 318228, "start": 3182.28,
  "end": 3191.28, "text": " Into two categories SAS companies and website owners when
  it comes to website owners I think the search for websites is really used because.",
  "tokens": [50364, 23373, 732, 10479, 33441, 3431, 293, 3144, 7710, 562, 309, 1487,
  281, 3144, 7710, 286, 519, 264, 3164, 337, 12891, 307, 534, 1143, 570, 13, 50814],
  "temperature": 0.0, "avg_logprob": -0.160246471563975, "compression_ratio": 1.8588235294117648,
  "no_speech_prob": 0.237690269947052}, {"id": 733, "seek": 318228, "start": 3192.28,
  "end": 3210.28, "text": " And it becomes like a cyclical thing it''s really used
  companies therefore don''t invest any money in improving it it''s really used because
  it''s not good and basically Google does enough a good enough job actually indexing
  well sites so site owners have accepted that Google is going to be the front door
  into their into their website.", "tokens": [50864, 400, 309, 3643, 411, 257, 19474,
  804, 551, 309, 311, 534, 1143, 3431, 4412, 500, 380, 1963, 604, 1460, 294, 11470,
  309, 309, 311, 534, 1143, 570, 309, 311, 406, 665, 293, 1936, 3329, 775, 1547, 257,
  665, 1547, 1691, 767, 8186, 278, 731, 7533, 370, 3621, 7710, 362, 9035, 300, 3329,
  307, 516, 281, 312, 264, 1868, 2853, 666, 641, 666, 641, 3144, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.160246471563975, "compression_ratio": 1.8588235294117648,
  "no_speech_prob": 0.237690269947052}, {"id": 734, "seek": 321028, "start": 3210.28,
  "end": 3237.28, "text": " On the other hand I think it''s it is obviously dangerous
  for them to because you''ve had sites that essentially get obliterated when Google
  changes you know their quality guidelines and they they drop off the front page
  and the traffic goes down by 95% suddenly and there''s no way to recover from it
  so it would be good first to be able to provide a good search experience on the
  websites but I think they don''t do it for the cost involved and they don''t know
  how to and certainly.", "tokens": [50364, 1282, 264, 661, 1011, 286, 519, 309, 311,
  309, 307, 2745, 5795, 337, 552, 281, 570, 291, 600, 632, 7533, 300, 4476, 483, 23740,
  1681, 770, 562, 3329, 2962, 291, 458, 641, 3125, 12470, 293, 436, 436, 3270, 766,
  264, 1868, 3028, 293, 264, 6419, 1709, 760, 538, 13420, 4, 5800, 293, 456, 311,
  572, 636, 281, 8114, 490, 309, 370, 309, 576, 312, 665, 700, 281, 312, 1075, 281,
  2893, 257, 665, 3164, 1752, 322, 264, 12891, 457, 286, 519, 436, 500, 380, 360,
  309, 337, 264, 2063, 3288, 293, 436, 500, 380, 458, 577, 281, 293, 3297, 13, 51714],
  "temperature": 0.0, "avg_logprob": -0.09170211278475247, "compression_ratio": 1.6783216783216783,
  "no_speech_prob": 0.03175082057714462}, {"id": 735, "seek": 323728, "start": 3237.28,
  "end": 3253.6800000000003, "text": " Algolia and elastic are making that easier
  particularly algolia but there''s still a lot better that it could be made coming
  to SAS companies there they''re talking about data that''s private the communications
  of the school to the parents are not on the web somewhere they can be indexed by
  Google.", "tokens": [50364, 35014, 29760, 293, 17115, 366, 1455, 300, 3571, 4098,
  3501, 29760, 457, 456, 311, 920, 257, 688, 1101, 300, 309, 727, 312, 1027, 1348,
  281, 33441, 3431, 456, 436, 434, 1417, 466, 1412, 300, 311, 4551, 264, 15163, 295,
  264, 1395, 281, 264, 3152, 366, 406, 322, 264, 3670, 4079, 436, 393, 312, 8186,
  292, 538, 3329, 13, 51184], "temperature": 0.0, "avg_logprob": -0.14748193884408603,
  "compression_ratio": 1.688976377952756, "no_speech_prob": 0.005614744499325752},
  {"id": 736, "seek": 323728, "start": 3254.1600000000003, "end": 3261.88, "text":
  " So I feel like what I''ve noticed in the last few years is that some sort of search
  feature is present in most of these products now.", "tokens": [51208, 407, 286,
  841, 411, 437, 286, 600, 5694, 294, 264, 1036, 1326, 924, 307, 300, 512, 1333, 295,
  3164, 4111, 307, 1974, 294, 881, 295, 613, 3383, 586, 13, 51594], "temperature":
  0.0, "avg_logprob": -0.14748193884408603, "compression_ratio": 1.688976377952756,
  "no_speech_prob": 0.005614744499325752}, {"id": 737, "seek": 326188, "start": 3261.88,
  "end": 3291.48, "text": " But yes it''s usually not tuned maybe not even set up
  correctly and it doesn''t work well and there''s a lot of room for improvement so
  I think these these neural search technologies let you you know really easily improve
  the quality easily if you''ve got a set of simple APIs and that''s what we provide
  our APIs basically look like elastic or Algolia''s index documents and you never
  know there''s a neural network running.", "tokens": [50364, 583, 2086, 309, 311,
  2673, 406, 10870, 1310, 406, 754, 992, 493, 8944, 293, 309, 1177, 380, 589, 731,
  293, 456, 311, 257, 688, 295, 1808, 337, 10444, 370, 286, 519, 613, 613, 18161,
  3164, 7943, 718, 291, 291, 458, 534, 3612, 3470, 264, 3125, 3612, 498, 291, 600,
  658, 257, 992, 295, 2199, 21445, 293, 300, 311, 437, 321, 2893, 527, 21445, 1936,
  574, 411, 17115, 420, 35014, 29760, 311, 8186, 8512, 293, 291, 1128, 458, 456, 311,
  257, 18161, 3209, 2614, 13, 51844], "temperature": 0.0, "avg_logprob": -0.1850170486274807,
  "compression_ratio": 1.672, "no_speech_prob": 0.027591120451688766}, {"id": 738,
  "seek": 329188, "start": 3291.88, "end": 3300.0, "text": " And the background at
  all and it''s not important just the queries go in and the results come out but
  these results are far far better than what you would get from a keyword search.",
  "tokens": [50364, 400, 264, 3678, 412, 439, 293, 309, 311, 406, 1021, 445, 264,
  24109, 352, 294, 293, 264, 3542, 808, 484, 457, 613, 3542, 366, 1400, 1400, 1101,
  813, 437, 291, 576, 483, 490, 257, 20428, 3164, 13, 50770], "temperature": 0.0,
  "avg_logprob": -0.19768850008646646, "compression_ratio": 1.6425855513307985, "no_speech_prob":
  0.009925175458192825}, {"id": 739, "seek": 329188, "start": 3301.0, "end": 3308.88,
  "text": " So so I think there''s a lot of scope particularly for SAS companies for
  for neural search.", "tokens": [50820, 407, 370, 286, 519, 456, 311, 257, 688, 295,
  11923, 4098, 337, 33441, 3431, 337, 337, 18161, 3164, 13, 51214], "temperature":
  0.0, "avg_logprob": -0.19768850008646646, "compression_ratio": 1.6425855513307985,
  "no_speech_prob": 0.009925175458192825}, {"id": 740, "seek": 329188, "start": 3309.36,
  "end": 3321.36, "text": " Yeah yeah absolutely I actually wanted to ask you just
  a question came to my mind I''ve been reading the book about I think about relevant
  search it''s called by.", "tokens": [51238, 865, 1338, 3122, 286, 767, 1415, 281,
  1029, 291, 445, 257, 1168, 1361, 281, 452, 1575, 286, 600, 668, 3760, 264, 1446,
  466, 286, 519, 466, 7340, 3164, 309, 311, 1219, 538, 13, 51838], "temperature":
  0.0, "avg_logprob": -0.19768850008646646, "compression_ratio": 1.6425855513307985,
  "no_speech_prob": 0.009925175458192825}, {"id": 741, "seek": 332188, "start": 3321.88,
  "end": 3329.88, "text": " Doctor and ball and other authors I might be not remembering
  exactly but this book you know it goes chapter after chapter wait says.", "tokens":
  [50364, 10143, 293, 2594, 293, 661, 16552, 286, 1062, 312, 406, 20719, 2293, 457,
  341, 1446, 291, 458, 309, 1709, 7187, 934, 7187, 1699, 1619, 13, 50764], "temperature":
  0.0, "avg_logprob": -0.22046729974579393, "compression_ratio": 1.4655172413793103,
  "no_speech_prob": 0.004405877087265253}, {"id": 742, "seek": 332188, "start": 3330.4,
  "end": 3338.12, "text": " Okay let''s just take it from the first principles you
  have a search to ask you have documents you need to start with like.", "tokens":
  [50790, 1033, 718, 311, 445, 747, 309, 490, 264, 700, 9156, 291, 362, 257, 3164,
  281, 1029, 291, 362, 8512, 291, 643, 281, 722, 365, 411, 13, 51176], "temperature":
  0.0, "avg_logprob": -0.22046729974579393, "compression_ratio": 1.4655172413793103,
  "no_speech_prob": 0.004405877087265253}, {"id": 743, "seek": 333812, "start": 3338.6,
  "end": 3359.04, "text": " tokenization and by the way if you make a mistake that
  it will be not findable and then you move one level up and then you start thinking
  okay what about the model okay TF IDF BM25 what are the trade of Sunson and so they
  teach you to become a search engineer and then they proceed to ranking and so on
  so forth and my question is like.", "tokens": [50388, 14862, 2144, 293, 538, 264,
  636, 498, 291, 652, 257, 6146, 300, 309, 486, 312, 406, 915, 712, 293, 550, 291,
  1286, 472, 1496, 493, 293, 550, 291, 722, 1953, 1392, 437, 466, 264, 2316, 1392,
  40964, 7348, 37, 15901, 6074, 437, 366, 264, 4923, 295, 6163, 3015, 293, 370, 436,
  2924, 291, 281, 1813, 257, 3164, 11403, 293, 550, 436, 8991, 281, 17833, 293, 370,
  322, 370, 5220, 293, 452, 1168, 307, 411, 13, 51410], "temperature": 0.0, "avg_logprob":
  -0.24452042881446548, "compression_ratio": 1.6, "no_speech_prob": 0.14902831614017487},
  {"id": 744, "seek": 335904, "start": 3360.04, "end": 3373.04, "text": " What do
  you think is going to be the change in the search engine profession going forward
  once neural search will hit the mass market because when I was the search engineer.",
  "tokens": [50414, 708, 360, 291, 519, 307, 516, 281, 312, 264, 1319, 294, 264, 3164,
  2848, 7032, 516, 2128, 1564, 18161, 3164, 486, 2045, 264, 2758, 2142, 570, 562,
  286, 390, 264, 3164, 11403, 13, 51064], "temperature": 0.0, "avg_logprob": -0.20458857218424478,
  "compression_ratio": 1.6974789915966386, "no_speech_prob": 0.019305700436234474},
  {"id": 745, "seek": 335904, "start": 3374.2799999999997, "end": 3388.52, "text":
  " Like I looked at the scene and solar and I I didn''t question much I just went
  and like implemented some changes some parsers some plugins or modified the behavior
  of some of some algorithm right by extending that class by the way.", "tokens":
  [51126, 1743, 286, 2956, 412, 264, 4145, 293, 7936, 293, 286, 286, 994, 380, 1168,
  709, 286, 445, 1437, 293, 411, 12270, 512, 2962, 512, 21156, 433, 512, 33759, 420,
  15873, 264, 5223, 295, 512, 295, 512, 9284, 558, 538, 24360, 300, 1508, 538, 264,
  636, 13, 51838], "temperature": 0.0, "avg_logprob": -0.20458857218424478, "compression_ratio":
  1.6974789915966386, "no_speech_prob": 0.019305700436234474}, {"id": 746, "seek":
  338904, "start": 3389.04, "end": 3412.04, "text": " The scene was not it was making
  a lot of classes final and in Java and so I cannot actually extend them so I had
  to copy the entire like package and then and then rename all these classes so there
  is no like namespace clash but that''s okay nowhere it''s at some point I was worried
  that I will probably reintroduce the scene all the way in my ID because I had to
  touch multiple parts.", "tokens": [50364, 440, 4145, 390, 406, 309, 390, 1455, 257,
  688, 295, 5359, 2572, 293, 294, 10745, 293, 370, 286, 2644, 767, 10101, 552, 370,
  286, 632, 281, 5055, 264, 2302, 411, 7372, 293, 550, 293, 550, 36741, 439, 613,
  5359, 370, 456, 307, 572, 411, 5288, 17940, 36508, 457, 300, 311, 1392, 11159, 309,
  311, 412, 512, 935, 286, 390, 5804, 300, 286, 486, 1391, 319, 38132, 384, 264, 4145,
  439, 264, 636, 294, 452, 7348, 570, 286, 632, 281, 2557, 3866, 3166, 13, 51514],
  "temperature": 0.0, "avg_logprob": -0.23042189937898483, "compression_ratio": 1.6946902654867257,
  "no_speech_prob": 0.011080016382038593}, {"id": 747, "seek": 341204, "start": 3412.04,
  "end": 3437.88, "text": " But so I felt like I''m in control more or less right
  not because it''s on not not only because it''s open source but because I could
  read the code I could talk to people I could read books I could read blogs and I
  could experiment myself right and that made me I believe a search engineer in that
  company even though the company''s goal was not to build you know searches service
  we were building the product.", "tokens": [50364, 583, 370, 286, 2762, 411, 286,
  478, 294, 1969, 544, 420, 1570, 558, 406, 570, 309, 311, 322, 406, 406, 787, 570,
  309, 311, 1269, 4009, 457, 570, 286, 727, 1401, 264, 3089, 286, 727, 751, 281, 561,
  286, 727, 1401, 3642, 286, 727, 1401, 31038, 293, 286, 727, 5120, 2059, 558, 293,
  300, 1027, 385, 286, 1697, 257, 3164, 11403, 294, 300, 2237, 754, 1673, 264, 2237,
  311, 3387, 390, 406, 281, 1322, 291, 458, 26701, 2643, 321, 645, 2390, 264, 1674,
  13, 51656], "temperature": 0.0, "avg_logprob": -0.15382315895774148, "compression_ratio":
  1.7885462555066078, "no_speech_prob": 0.07129093259572983}, {"id": 748, "seek":
  343788, "start": 3438.2000000000003, "end": 3443.96, "text": " How do you do happen
  it thoughts around like how neural search will change the landscape of this job.",
  "tokens": [50380, 1012, 360, 291, 360, 1051, 309, 4598, 926, 411, 577, 18161, 3164,
  486, 1319, 264, 9661, 295, 341, 1691, 13, 50668], "temperature": 0.0, "avg_logprob":
  -0.2286097764968872, "compression_ratio": 1.625615763546798, "no_speech_prob": 0.0033826478756964207},
  {"id": 749, "seek": 343788, "start": 3447.08, "end": 3449.96, "text": " Well that''s
  a that''s an excellent question.", "tokens": [50824, 1042, 300, 311, 257, 300, 311,
  364, 7103, 1168, 13, 50968], "temperature": 0.0, "avg_logprob": -0.2286097764968872,
  "compression_ratio": 1.625615763546798, "no_speech_prob": 0.0033826478756964207},
  {"id": 750, "seek": 343788, "start": 3451.6, "end": 3453.8, "text": " Well a few
  a few thoughts on that topic.", "tokens": [51050, 1042, 257, 1326, 257, 1326, 4598,
  322, 300, 4829, 13, 51160], "temperature": 0.0, "avg_logprob": -0.2286097764968872,
  "compression_ratio": 1.625615763546798, "no_speech_prob": 0.0033826478756964207},
  {"id": 751, "seek": 343788, "start": 3454.92, "end": 3456.52, "text": " Neural search
  is going to make it.", "tokens": [51216, 1734, 1807, 3164, 307, 516, 281, 652, 309,
  13, 51296], "temperature": 0.0, "avg_logprob": -0.2286097764968872, "compression_ratio":
  1.625615763546798, "no_speech_prob": 0.0033826478756964207}, {"id": 752, "seek":
  343788, "start": 3458.6800000000003, "end": 3467.12, "text": " Easier it''s going
  to require less expertise to put together high quality search experiences and furthermore.",
  "tokens": [51404, 46879, 811, 309, 311, 516, 281, 3651, 1570, 11769, 281, 829, 1214,
  1090, 3125, 3164, 5235, 293, 3052, 3138, 13, 51826], "temperature": 0.0, "avg_logprob":
  -0.2286097764968872, "compression_ratio": 1.625615763546798, "no_speech_prob": 0.0033826478756964207},
  {"id": 753, "seek": 346788, "start": 3468.36, "end": 3474.7200000000003, "text":
  " The advantage the companies like Google or Microsoft have from click data it''s
  still going to be there but it''s going to diminish.", "tokens": [50388, 440, 5002,
  264, 3431, 411, 3329, 420, 8116, 362, 490, 2052, 1412, 309, 311, 920, 516, 281,
  312, 456, 457, 309, 311, 516, 281, 48696, 13, 50706], "temperature": 0.0, "avg_logprob":
  -0.19499053955078124, "compression_ratio": 1.50253807106599, "no_speech_prob": 0.00915265642106533},
  {"id": 754, "seek": 346788, "start": 3475.52, "end": 3487.32, "text": " And I think
  that''s actually why maybe I''m biased here and misreading it you see a lot of search
  engine companies starting up in the last year or two you''ve got meva.", "tokens":
  [50746, 400, 286, 519, 300, 311, 767, 983, 1310, 286, 478, 28035, 510, 293, 3346,
  35908, 309, 291, 536, 257, 688, 295, 3164, 2848, 3431, 2891, 493, 294, 264, 1036,
  1064, 420, 732, 291, 600, 658, 385, 2757, 13, 51336], "temperature": 0.0, "avg_logprob":
  -0.19499053955078124, "compression_ratio": 1.50253807106599, "no_speech_prob": 0.00915265642106533},
  {"id": 755, "seek": 348732, "start": 3487.88, "end": 3494.84, "text": " Kagi I think
  the head of sales force research has started his own engine I''ve even heard some
  rumors you don''t.", "tokens": [50392, 591, 20291, 286, 519, 264, 1378, 295, 5763,
  3464, 2132, 575, 1409, 702, 1065, 2848, 286, 600, 754, 2198, 512, 21201, 291, 500,
  380, 13, 50740], "temperature": 0.0, "avg_logprob": -0.405896199213994, "compression_ratio":
  1.599078341013825, "no_speech_prob": 0.07359088957309723}, {"id": 756, "seek": 348732,
  "start": 3497.6400000000003, "end": 3513.0800000000004, "text": " Right right I
  heard some movie Apple Richard so yeah exactly so to maybe some rumors Apple might
  be trying to do something like that and it''s it''s basically because the amount
  of effort it takes now I think has gone down significantly.", "tokens": [50880,
  1779, 558, 286, 2198, 512, 3169, 6373, 9809, 370, 1338, 2293, 370, 281, 1310, 512,
  21201, 6373, 1062, 312, 1382, 281, 360, 746, 411, 300, 293, 309, 311, 309, 311,
  1936, 570, 264, 2372, 295, 4630, 309, 2516, 586, 286, 519, 575, 2780, 760, 10591,
  13, 51652], "temperature": 0.0, "avg_logprob": -0.405896199213994, "compression_ratio":
  1.599078341013825, "no_speech_prob": 0.07359088957309723}, {"id": 757, "seek": 351308,
  "start": 3513.96, "end": 3519.96, "text": " So I think that that''s going to be
  one of the effects of neural.", "tokens": [50408, 407, 286, 519, 300, 300, 311,
  516, 281, 312, 472, 295, 264, 5065, 295, 18161, 13, 50708], "temperature": 0.0,
  "avg_logprob": -0.39067249913369456, "compression_ratio": 1.5791666666666666, "no_speech_prob":
  0.016968876123428345}, {"id": 758, "seek": 351308, "start": 3521.08, "end": 3528.6,
  "text": " And I also expect it just like you know a losing has been around for a
  long time I mean maybe the early 2000''s 2000.", "tokens": [50764, 400, 286, 611,
  2066, 309, 445, 411, 291, 458, 257, 7027, 575, 668, 926, 337, 257, 938, 565, 286,
  914, 1310, 264, 2440, 8132, 311, 8132, 13, 51140], "temperature": 0.0, "avg_logprob":
  -0.39067249913369456, "compression_ratio": 1.5791666666666666, "no_speech_prob":
  0.016968876123428345}, {"id": 759, "seek": 351308, "start": 3529.4, "end": 3541.24,
  "text": " 99 to 9 I think when that cutting started learning Java and as a side
  product project he decided to implement Lucene and so he started the whole community
  and then Hadoop followed and so on so far.", "tokens": [51180, 11803, 281, 1722,
  286, 519, 562, 300, 6492, 1409, 2539, 10745, 293, 382, 257, 1252, 1674, 1716, 415,
  3047, 281, 4445, 9593, 1450, 293, 370, 415, 1409, 264, 1379, 1768, 293, 550, 389,
  1573, 404, 6263, 293, 370, 322, 370, 1400, 13, 51772], "temperature": 0.0, "avg_logprob":
  -0.39067249913369456, "compression_ratio": 1.5791666666666666, "no_speech_prob":
  0.016968876123428345}, {"id": 760, "seek": 354124, "start": 3541.3199999999997,
  "end": 3548.12, "text": " Yeah okay because I yeah I remember from a time ago so
  I think that in the same way there will be an open source.", "tokens": [50368, 865,
  1392, 570, 286, 1338, 286, 1604, 490, 257, 565, 2057, 370, 286, 519, 300, 294, 264,
  912, 636, 456, 486, 312, 364, 1269, 4009, 13, 50708], "temperature": 0.0, "avg_logprob":
  -0.19038545763170397, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.0064502740278840065}, {"id": 761, "seek": 354124, "start": 3549.08, "end": 3557.3999999999996,
  "text": " Neural thing it might come under the cover of Lucene or it might be a
  separate Apache project and and eventually it''s going to be the go to solution.",
  "tokens": [50756, 1734, 1807, 551, 309, 1062, 808, 833, 264, 2060, 295, 9593, 1450,
  420, 309, 1062, 312, 257, 4994, 46597, 1716, 293, 293, 4728, 309, 311, 516, 281,
  312, 264, 352, 281, 3827, 13, 51172], "temperature": 0.0, "avg_logprob": -0.19038545763170397,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0064502740278840065},
  {"id": 762, "seek": 354124, "start": 3558.52, "end": 3568.9199999999996, "text":
  " So what companies like mine are doing right now is you know this technology is
  still pretty new and we''re feeling in the gap and we''re also providing like a
  completely hosted solution which has some some value on its own.", "tokens": [51228,
  407, 437, 3431, 411, 3892, 366, 884, 558, 586, 307, 291, 458, 341, 2899, 307, 920,
  1238, 777, 293, 321, 434, 2633, 294, 264, 7417, 293, 321, 434, 611, 6530, 411, 257,
  2584, 19204, 3827, 597, 575, 512, 512, 2158, 322, 1080, 1065, 13, 51748], "temperature":
  0.0, "avg_logprob": -0.19038545763170397, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0064502740278840065}, {"id": 763, "seek": 356892, "start": 3569.88,
  "end": 3578.28, "text": " But I think longer term that''s why I see things headed
  because you know we''re getting into these very good general performance neural
  networks.", "tokens": [50412, 583, 286, 519, 2854, 1433, 300, 311, 983, 286, 536,
  721, 12798, 570, 291, 458, 321, 434, 1242, 666, 613, 588, 665, 2674, 3389, 18161,
  9590, 13, 50832], "temperature": 0.0, "avg_logprob": -0.1267379685944202, "compression_ratio":
  1.686131386861314, "no_speech_prob": 0.004201448056846857}, {"id": 764, "seek":
  356892, "start": 3580.2000000000003, "end": 3589.2400000000002, "text": " Systems
  like Bert that can just perform well on a wide range of tasks and then you have
  like you know t5 and now mt5 and you can go across like 100 different languages
  as well.", "tokens": [50928, 27059, 411, 29594, 300, 393, 445, 2042, 731, 322, 257,
  4874, 3613, 295, 9608, 293, 550, 291, 362, 411, 291, 458, 256, 20, 293, 586, 275,
  83, 20, 293, 291, 393, 352, 2108, 411, 2319, 819, 8650, 382, 731, 13, 51380], "temperature":
  0.0, "avg_logprob": -0.1267379685944202, "compression_ratio": 1.686131386861314,
  "no_speech_prob": 0.004201448056846857}, {"id": 765, "seek": 356892, "start": 3590.36,
  "end": 3596.44, "text": " So there will eventually be models that are good enough
  and someone''s going to take the effort to distill them into something that runs
  well.", "tokens": [51436, 407, 456, 486, 4728, 312, 5245, 300, 366, 665, 1547, 293,
  1580, 311, 516, 281, 747, 264, 4630, 281, 42923, 552, 666, 746, 300, 6676, 731,
  13, 51740], "temperature": 0.0, "avg_logprob": -0.1267379685944202, "compression_ratio":
  1.686131386861314, "no_speech_prob": 0.004201448056846857}, {"id": 766, "seek":
  359644, "start": 3597.4, "end": 3603.88, "text": " And and you know anybody in any
  organization will be able to to download and use it the way to use Lucene today.",
  "tokens": [50412, 400, 293, 291, 458, 4472, 294, 604, 4475, 486, 312, 1075, 281,
  281, 5484, 293, 764, 309, 264, 636, 281, 764, 9593, 1450, 965, 13, 50736], "temperature":
  0.0, "avg_logprob": -0.15026896794637043, "compression_ratio": 1.6929824561403508,
  "no_speech_prob": 0.01676947996020317}, {"id": 767, "seek": 359644, "start": 3603.88,
  "end": 3608.36, "text": " I think that''s where things will be but it might be it
  might be five years before we reach that point.", "tokens": [50736, 286, 519, 300,
  311, 689, 721, 486, 312, 457, 309, 1062, 312, 309, 1062, 312, 1732, 924, 949, 321,
  2524, 300, 935, 13, 50960], "temperature": 0.0, "avg_logprob": -0.15026896794637043,
  "compression_ratio": 1.6929824561403508, "no_speech_prob": 0.01676947996020317},
  {"id": 768, "seek": 359644, "start": 3609.16, "end": 3619.88, "text": " Yeah yeah
  and I mean to take this thought forward from here like like maybe the profession
  do you think the profession will change in such a way that instead of tweaking.",
  "tokens": [51000, 865, 1338, 293, 286, 914, 281, 747, 341, 1194, 2128, 490, 510,
  411, 411, 1310, 264, 7032, 360, 291, 519, 264, 7032, 486, 1319, 294, 1270, 257,
  636, 300, 2602, 295, 6986, 2456, 13, 51536], "temperature": 0.0, "avg_logprob":
  -0.15026896794637043, "compression_ratio": 1.6929824561403508, "no_speech_prob":
  0.01676947996020317}, {"id": 769, "seek": 361988, "start": 3620.44, "end": 3628.84,
  "text": " The index configuration to make your search kind of work better like increase
  recall and you know not suffer from decreased precision.", "tokens": [50392, 440,
  8186, 11694, 281, 652, 428, 3164, 733, 295, 589, 1101, 411, 3488, 9901, 293, 291,
  458, 406, 9753, 490, 24436, 18356, 13, 50812], "temperature": 0.0, "avg_logprob":
  -0.2006618037368312, "compression_ratio": 1.5561224489795917, "no_speech_prob":
  0.0060213725082576275}, {"id": 770, "seek": 361988, "start": 3629.8, "end": 3639.2400000000002,
  "text": " You will move more like into okay here is the problem and this of the
  shelf network doesn''t work I have to fine tune it so you become a little bit more
  like a researcher.", "tokens": [50860, 509, 486, 1286, 544, 411, 666, 1392, 510,
  307, 264, 1154, 293, 341, 295, 264, 15222, 3209, 1177, 380, 589, 286, 362, 281,
  2489, 10864, 309, 370, 291, 1813, 257, 707, 857, 544, 411, 257, 21751, 13, 51332],
  "temperature": 0.0, "avg_logprob": -0.2006618037368312, "compression_ratio": 1.5561224489795917,
  "no_speech_prob": 0.0060213725082576275}, {"id": 771, "seek": 363924, "start": 3639.9599999999996,
  "end": 3666.9199999999996, "text": " Yeah so that''s an excellent point I think
  one of the key components in these systems and that we have not built yet in our
  system but it''s in the it''s in the blueprints is some kind of a feedback mechanism
  you''ll notice this in Kendra though for instance thumbs up thumbs down on the results
  for instance where you indicate what''s good and what''s bad and then even with
  a small amount of that data you can start to train a re-ranker.", "tokens": [50400,
  865, 370, 300, 311, 364, 7103, 935, 286, 519, 472, 295, 264, 2141, 6677, 294, 613,
  3652, 293, 300, 321, 362, 406, 3094, 1939, 294, 527, 1185, 457, 309, 311, 294, 264,
  309, 311, 294, 264, 888, 23547, 47523, 307, 512, 733, 295, 257, 5824, 7513, 291,
  603, 3449, 341, 294, 20891, 424, 1673, 337, 5197, 8838, 493, 8838, 760, 322, 264,
  3542, 337, 5197, 689, 291, 13330, 437, 311, 665, 293, 437, 311, 1578, 293, 550,
  754, 365, 257, 1359, 2372, 295, 300, 1412, 291, 393, 722, 281, 3847, 257, 319, 12,
  20479, 260, 13, 51748], "temperature": 0.0, "avg_logprob": -0.1648145294189453,
  "compression_ratio": 1.7182539682539681, "no_speech_prob": 0.011909730732440948},
  {"id": 772, "seek": 366692, "start": 3667.48, "end": 3677.16, "text": " And I think
  that in the presence of like the volumes of data that you get on an internal application
  let''s say you''re going to get a few thousand items of feedback.", "tokens": [50392,
  400, 286, 519, 300, 294, 264, 6814, 295, 411, 264, 22219, 295, 1412, 300, 291, 483,
  322, 364, 6920, 3861, 718, 311, 584, 291, 434, 516, 281, 483, 257, 1326, 4714, 4754,
  295, 5824, 13, 50876], "temperature": 0.0, "avg_logprob": -0.16178493089573356,
  "compression_ratio": 1.657370517928287, "no_speech_prob": 0.003004827070981264},
  {"id": 773, "seek": 366692, "start": 3677.8, "end": 3691.56, "text": " Training
  a re-ranker is probably the most effective thing that you can do that data whether
  it''s a random for a free rank or you take a cross attention on your network and
  you fine tune it but you can significantly improve the search quality that way.",
  "tokens": [50908, 20620, 257, 319, 12, 20479, 260, 307, 1391, 264, 881, 4942, 551,
  300, 291, 393, 360, 300, 1412, 1968, 309, 311, 257, 4974, 337, 257, 1737, 6181,
  420, 291, 747, 257, 3278, 3202, 322, 428, 3209, 293, 291, 2489, 10864, 309, 457,
  291, 393, 10591, 3470, 264, 3164, 3125, 300, 636, 13, 51596], "temperature": 0.0,
  "avg_logprob": -0.16178493089573356, "compression_ratio": 1.657370517928287, "no_speech_prob":
  0.003004827070981264}, {"id": 774, "seek": 369156, "start": 3691.56, "end": 3712.92,
  "text": " So so so I think that the the machinery for doing all of that can also
  be part of the open source offering because because it''s it''s very broadly applicable
  and can be used by basically anyone because like you say this is the problem that
  that then comes up is like I want to give feedback on this results so the system
  can improve itself.", "tokens": [50364, 407, 370, 370, 286, 519, 300, 264, 264,
  27302, 337, 884, 439, 295, 300, 393, 611, 312, 644, 295, 264, 1269, 4009, 8745,
  570, 570, 309, 311, 309, 311, 588, 19511, 21142, 293, 393, 312, 1143, 538, 1936,
  2878, 570, 411, 291, 584, 341, 307, 264, 1154, 300, 300, 550, 1487, 493, 307, 411,
  286, 528, 281, 976, 5824, 322, 341, 3542, 370, 264, 1185, 393, 3470, 2564, 13, 51432],
  "temperature": 0.0, "avg_logprob": -0.16626375015467815, "compression_ratio": 1.6699507389162562,
  "no_speech_prob": 0.025836151093244553}, {"id": 775, "seek": 371292, "start": 3713.7200000000003,
  "end": 3728.12, "text": " Yeah yeah absolutely so you kind of create the flywheel
  of success right so that you you bring the data back and then the model retrain
  and so on so forth but there is also there are also like interesting challenges
  like in your old network like catastrophic forgetting.", "tokens": [50404, 865,
  1338, 3122, 370, 291, 733, 295, 1884, 264, 3603, 22830, 295, 2245, 558, 370, 300,
  291, 291, 1565, 264, 1412, 646, 293, 550, 264, 2316, 1533, 7146, 293, 370, 322,
  370, 5220, 457, 456, 307, 611, 456, 366, 611, 411, 1880, 4759, 411, 294, 428, 1331,
  3209, 411, 34915, 25428, 13, 51124], "temperature": 0.0, "avg_logprob": -0.14932635522657825,
  "compression_ratio": 1.7480314960629921, "no_speech_prob": 0.15311677753925323},
  {"id": 776, "seek": 371292, "start": 3728.6800000000003, "end": 3740.92, "text":
  " Like is this something that you''ve been thinking maybe back at Google or now
  with your clients something that kind of you need to keep innovating or solve it
  some other way.", "tokens": [51152, 1743, 307, 341, 746, 300, 291, 600, 668, 1953,
  1310, 646, 412, 3329, 420, 586, 365, 428, 6982, 746, 300, 733, 295, 291, 643, 281,
  1066, 5083, 990, 420, 5039, 309, 512, 661, 636, 13, 51764], "temperature": 0.0,
  "avg_logprob": -0.14932635522657825, "compression_ratio": 1.7480314960629921, "no_speech_prob":
  0.15311677753925323}, {"id": 777, "seek": 374092, "start": 3740.92, "end": 3770.84,
  "text": " Yeah so I am familiar with the concept of catastrophic forgetting I honestly
  haven''t studied it very much in the context of of these large language models like
  Bert although in general the approach of you know taking a Bert type model and fine
  tuning seems seems to be working well but but then you''re essentially talking about
  taking after has been fine tuned on one task and then fine tuning for different
  task and it''s going to be a great deal.", "tokens": [50400, 865, 370, 286, 669,
  4963, 365, 264, 3410, 295, 34915, 25428, 286, 6095, 2378, 380, 9454, 309, 588, 709,
  294, 264, 4319, 295, 295, 613, 2416, 2856, 5245, 411, 29594, 4878, 294, 2674, 264,
  3109, 295, 291, 458, 1940, 257, 29594, 2010, 2316, 293, 2489, 15164, 2544, 2544,
  281, 312, 1364, 731, 457, 457, 550, 291, 434, 4476, 1417, 466, 1940, 934, 575, 668,
  2489, 10870, 322, 472, 5633, 293, 550, 2489, 15164, 337, 819, 5633, 293, 309, 311,
  516, 281, 312, 257, 869, 2028, 13, 51860], "temperature": 0.0, "avg_logprob": -0.3113837510012509,
  "compression_ratio": 1.7192307692307693, "no_speech_prob": 0.007751050870865583},
  {"id": 778, "seek": 377092, "start": 3770.92, "end": 3781.28, "text": " Because
  I do think it''s going to get solved because it increases its abilities on the first
  task. And yeah I guess I don''t know how much of an issue that''s that''s going
  to be in the context as information retrieval.", "tokens": [50364, 1436, 286, 360,
  519, 309, 311, 516, 281, 483, 13041, 570, 309, 8637, 1080, 11582, 322, 264, 700,
  5633, 13, 400, 1338, 286, 2041, 286, 500, 380, 458, 577, 709, 295, 364, 2734, 300,
  311, 300, 311, 516, 281, 312, 294, 264, 4319, 382, 1589, 19817, 3337, 13, 50882],
  "temperature": 0.8, "avg_logprob": -0.6311803098584785, "compression_ratio": 1.7327044025157232,
  "no_speech_prob": 0.011484101414680481}, {"id": 779, "seek": 377092, "start": 3781.64,
  "end": 3796.28, "text": " Yeah I mean another thing like if you are familiar with
  learning to rank for example, which may or may not involve in your own network it
  may also be based on decision tree like lambda marked for example, you know when
  you receive a new batch of clicks or downloads or whatever events you have in the
  system and you retrain that model.", "tokens": [50900, 865, 286, 914, 1071, 551,
  411, 498, 291, 366, 4963, 365, 2539, 281, 6181, 337, 1365, 11, 597, 815, 420, 815,
  406, 9494, 294, 428, 1065, 3209, 309, 815, 611, 312, 2361, 322, 3537, 4230, 411,
  13607, 12658, 337, 1365, 11, 291, 458, 562, 291, 4774, 257, 777, 15245, 295, 18521,
  420, 36553, 420, 2035, 3931, 291, 362, 294, 264, 1185, 293, 291, 1533, 7146, 300,
  2316, 13, 51632], "temperature": 0.8, "avg_logprob": -0.6311803098584785, "compression_ratio":
  1.7327044025157232, "no_speech_prob": 0.011484101414680481}, {"id": 780, "seek":
  379628, "start": 3796.28, "end": 3800.0, "text": " clicks or downloads or whatever
  events you have in the system and you", "tokens": [50364, 18521, 420, 36553, 420,
  2035, 3931, 291, 362, 294, 264, 1185, 293, 291, 50550], "temperature": 0.0, "avg_logprob":
  -0.2876692842846074, "compression_ratio": 1.7263513513513513, "no_speech_prob":
  0.43136316537857056}, {"id": 781, "seek": 379628, "start": 3800.0, "end": 3804.7200000000003,
  "text": " retain that model, it will also forget what it knew about the previous
  state,", "tokens": [50550, 18340, 300, 2316, 11, 309, 486, 611, 2870, 437, 309,
  2586, 466, 264, 3894, 1785, 11, 50786], "temperature": 0.0, "avg_logprob": -0.2876692842846074,
  "compression_ratio": 1.7263513513513513, "no_speech_prob": 0.43136316537857056},
  {"id": 782, "seek": 379628, "start": 3804.7200000000003, "end": 3810.1600000000003,
  "text": " right? It''s very natural and it probably is we can associate it with
  human life", "tokens": [50786, 558, 30, 467, 311, 588, 3303, 293, 309, 1391, 307,
  321, 393, 14644, 309, 365, 1952, 993, 51058], "temperature": 0.0, "avg_logprob":
  -0.2876692842846074, "compression_ratio": 1.7263513513513513, "no_speech_prob":
  0.43136316537857056}, {"id": 783, "seek": 379628, "start": 3810.1600000000003, "end":
  3813.6400000000003, "text": " as well in some sense, although they say the older
  you get, the earlier", "tokens": [51058, 382, 731, 294, 512, 2020, 11, 4878, 436,
  584, 264, 4906, 291, 483, 11, 264, 3071, 51232], "temperature": 0.0, "avg_logprob":
  -0.2876692842846074, "compression_ratio": 1.7263513513513513, "no_speech_prob":
  0.43136316537857056}, {"id": 784, "seek": 379628, "start": 3813.6400000000003, "end":
  3817.8, "text": " memories you will actually remember, you might forget what happened
  yesterday,", "tokens": [51232, 8495, 291, 486, 767, 1604, 11, 291, 1062, 2870, 437,
  2011, 5186, 11, 51440], "temperature": 0.0, "avg_logprob": -0.2876692842846074,
  "compression_ratio": 1.7263513513513513, "no_speech_prob": 0.43136316537857056},
  {"id": 785, "seek": 379628, "start": 3817.8, "end": 3821.1200000000003, "text":
  " but you remember what happened like 50 years ago. But like, yeah,", "tokens":
  [51440, 457, 291, 1604, 437, 2011, 411, 2625, 924, 2057, 13, 583, 411, 11, 1338,
  11, 51606], "temperature": 0.0, "avg_logprob": -0.2876692842846074, "compression_ratio":
  1.7263513513513513, "no_speech_prob": 0.43136316537857056}, {"id": 786, "seek":
  379628, "start": 3821.1200000000003, "end": 3824.0800000000004, "text": " what''s
  probably noticing that with myself. Yeah, me too, actually,", "tokens": [51606,
  437, 311, 1391, 21814, 300, 365, 2059, 13, 865, 11, 385, 886, 11, 767, 11, 51754],
  "temperature": 0.0, "avg_logprob": -0.2876692842846074, "compression_ratio": 1.7263513513513513,
  "no_speech_prob": 0.43136316537857056}, {"id": 787, "seek": 382408, "start": 3824.3199999999997,
  "end": 3827.84, "text": " because days go by and I''m like, okay, what''s going
  on? But then you go,", "tokens": [50376, 570, 1708, 352, 538, 293, 286, 478, 411,
  11, 1392, 11, 437, 311, 516, 322, 30, 583, 550, 291, 352, 11, 50552], "temperature":
  0.0, "avg_logprob": -0.20278196167527585, "compression_ratio": 1.6641509433962265,
  "no_speech_prob": 0.01039421558380127}, {"id": 788, "seek": 382408, "start": 3827.84,
  "end": 3833.16, "text": " okay, when I was a kid, I remember something. But like
  neural networks are", "tokens": [50552, 1392, 11, 562, 286, 390, 257, 1636, 11,
  286, 1604, 746, 13, 583, 411, 18161, 9590, 366, 50818], "temperature": 0.0, "avg_logprob":
  -0.20278196167527585, "compression_ratio": 1.6641509433962265, "no_speech_prob":
  0.01039421558380127}, {"id": 789, "seek": 382408, "start": 3833.16, "end": 3836.4,
  "text": " probably a little bit different, or at least the present neural networks.",
  "tokens": [50818, 1391, 257, 707, 857, 819, 11, 420, 412, 1935, 264, 1974, 18161,
  9590, 13, 50980], "temperature": 0.0, "avg_logprob": -0.20278196167527585, "compression_ratio":
  1.6641509433962265, "no_speech_prob": 0.01039421558380127}, {"id": 790, "seek":
  382408, "start": 3837.7999999999997, "end": 3843.0, "text": " Right. So I think
  when you when you retrain the model, like you have to", "tokens": [51050, 1779,
  13, 407, 286, 519, 562, 291, 562, 291, 1533, 7146, 264, 2316, 11, 411, 291, 362,
  281, 51310], "temperature": 0.0, "avg_logprob": -0.20278196167527585, "compression_ratio":
  1.6641509433962265, "no_speech_prob": 0.01039421558380127}, {"id": 791, "seek":
  382408, "start": 3843.0, "end": 3846.64, "text": " retrain otherwise, it will drift,
  right? I think Google also has a paper", "tokens": [51310, 1533, 7146, 5911, 11,
  309, 486, 19699, 11, 558, 30, 286, 519, 3329, 611, 575, 257, 3035, 51492], "temperature":
  0.0, "avg_logprob": -0.20278196167527585, "compression_ratio": 1.6641509433962265,
  "no_speech_prob": 0.01039421558380127}, {"id": 792, "seek": 382408, "start": 3846.64,
  "end": 3852.04, "text": " about that, like kind of checking the consistency of your
  machine learning", "tokens": [51492, 466, 300, 11, 411, 733, 295, 8568, 264, 14416,
  295, 428, 3479, 2539, 51762], "temperature": 0.0, "avg_logprob": -0.20278196167527585,
  "compression_ratio": 1.6641509433962265, "no_speech_prob": 0.01039421558380127},
  {"id": 793, "seek": 385204, "start": 3852.04, "end": 3855.8, "text": " pipeline
  and your model. So it doesn''t drift and just explode in the eyes of", "tokens":
  [50364, 15517, 293, 428, 2316, 13, 407, 309, 1177, 380, 19699, 293, 445, 21411,
  294, 264, 2575, 295, 50552], "temperature": 0.0, "avg_logprob": -0.22144873529417902,
  "compression_ratio": 1.7234848484848484, "no_speech_prob": 0.019363148137927055},
  {"id": 794, "seek": 385204, "start": 3855.8, "end": 3859.88, "text": " the front
  of the eyes of the user, right? So you have to keep retraining it.", "tokens": [50552,
  264, 1868, 295, 264, 2575, 295, 264, 4195, 11, 558, 30, 407, 291, 362, 281, 1066,
  49356, 1760, 309, 13, 50756], "temperature": 0.0, "avg_logprob": -0.22144873529417902,
  "compression_ratio": 1.7234848484848484, "no_speech_prob": 0.019363148137927055},
  {"id": 795, "seek": 385204, "start": 3860.64, "end": 3864.64, "text": " But but
  then that also means that it will forget things. Maybe they were quite", "tokens":
  [50794, 583, 457, 550, 300, 611, 1355, 300, 309, 486, 2870, 721, 13, 2704, 436,
  645, 1596, 50994], "temperature": 0.0, "avg_logprob": -0.22144873529417902, "compression_ratio":
  1.7234848484848484, "no_speech_prob": 0.019363148137927055}, {"id": 796, "seek":
  385204, "start": 3864.64, "end": 3869.64, "text": " important. Maybe they are not
  high probability anymore, but they still are", "tokens": [50994, 1021, 13, 2704,
  436, 366, 406, 1090, 8482, 3602, 11, 457, 436, 920, 366, 51244], "temperature":
  0.0, "avg_logprob": -0.22144873529417902, "compression_ratio": 1.7234848484848484,
  "no_speech_prob": 0.019363148137927055}, {"id": 797, "seek": 385204, "start": 3869.64,
  "end": 3875.08, "text": " true. But the network has forgotten about them. Right,
  right, right. Yeah,", "tokens": [51244, 2074, 13, 583, 264, 3209, 575, 11832, 466,
  552, 13, 1779, 11, 558, 11, 558, 13, 865, 11, 51516], "temperature": 0.0, "avg_logprob":
  -0.22144873529417902, "compression_ratio": 1.7234848484848484, "no_speech_prob":
  0.019363148137927055}, {"id": 798, "seek": 385204, "start": 3875.08, "end": 3882.0,
  "text": " then yeah, that makes sense. Yeah. Anyway, it was it was a great talking",
  "tokens": [51516, 550, 1338, 11, 300, 1669, 2020, 13, 865, 13, 5684, 11, 309, 390,
  309, 390, 257, 869, 1417, 51862], "temperature": 0.0, "avg_logprob": -0.22144873529417902,
  "compression_ratio": 1.7234848484848484, "no_speech_prob": 0.019363148137927055},
  {"id": 799, "seek": 388200, "start": 3882.0, "end": 3886.36, "text": " to you, but
  I still want to close off. And before we go to some announcement for", "tokens":
  [50364, 281, 291, 11, 457, 286, 920, 528, 281, 1998, 766, 13, 400, 949, 321, 352,
  281, 512, 12847, 337, 50582], "temperature": 0.0, "avg_logprob": -0.24063308839875508,
  "compression_ratio": 1.758364312267658, "no_speech_prob": 0.01530259195715189},
  {"id": 800, "seek": 388200, "start": 3886.36, "end": 3891.16, "text": " you, I''m
  thinking like I''m asking this question to different to all guests and", "tokens":
  [50582, 291, 11, 286, 478, 1953, 411, 286, 478, 3365, 341, 1168, 281, 819, 281,
  439, 9804, 293, 50822], "temperature": 0.0, "avg_logprob": -0.24063308839875508,
  "compression_ratio": 1.758364312267658, "no_speech_prob": 0.01530259195715189},
  {"id": 801, "seek": 388200, "start": 3891.16, "end": 3896.56, "text": " different
  guests take it differently. But I really would like to hear your view", "tokens":
  [50822, 819, 9804, 747, 309, 7614, 13, 583, 286, 534, 576, 411, 281, 1568, 428,
  1910, 51092], "temperature": 0.0, "avg_logprob": -0.24063308839875508, "compression_ratio":
  1.758364312267658, "no_speech_prob": 0.01530259195715189}, {"id": 802, "seek": 388200,
  "start": 3896.96, "end": 3901.72, "text": " on that question of why it''s a little
  bit more philosophical. Like like in a", "tokens": [51112, 322, 300, 1168, 295,
  983, 309, 311, 257, 707, 857, 544, 25066, 13, 1743, 411, 294, 257, 51350], "temperature":
  0.0, "avg_logprob": -0.24063308839875508, "compression_ratio": 1.758364312267658,
  "no_speech_prob": 0.01530259195715189}, {"id": 803, "seek": 388200, "start": 3901.72,
  "end": 3906.24, "text": " way, like you had a stable job at Google, a lot of challenge,
  a lot of data,", "tokens": [51350, 636, 11, 411, 291, 632, 257, 8351, 1691, 412,
  3329, 11, 257, 688, 295, 3430, 11, 257, 688, 295, 1412, 11, 51576], "temperature":
  0.0, "avg_logprob": -0.24063308839875508, "compression_ratio": 1.758364312267658,
  "no_speech_prob": 0.01530259195715189}, {"id": 804, "seek": 388200, "start": 3906.36,
  "end": 3911.0, "text": " a lot of user impact. Like as you said, like Autorripe
  Live feature was enabled", "tokens": [51582, 257, 688, 295, 4195, 2712, 13, 1743,
  382, 291, 848, 11, 411, 6049, 284, 470, 494, 10385, 4111, 390, 15172, 51814], "temperature":
  0.0, "avg_logprob": -0.24063308839875508, "compression_ratio": 1.758364312267658,
  "no_speech_prob": 0.01530259195715189}, {"id": 805, "seek": 391100, "start": 3911.0,
  "end": 3916.88, "text": " and to like millions and millions of users. So then you
  then you decided to go to", "tokens": [50364, 293, 281, 411, 6803, 293, 6803, 295,
  5022, 13, 407, 550, 291, 550, 291, 3047, 281, 352, 281, 50658], "temperature": 0.0,
  "avg_logprob": -0.2420102528163365, "compression_ratio": 1.626984126984127, "no_speech_prob":
  0.004987666383385658}, {"id": 806, "seek": 391100, "start": 3916.88, "end": 3922.0,
  "text": " to build your startup and that''s a nice nice kind of way to experience
  like another", "tokens": [50658, 281, 1322, 428, 18578, 293, 300, 311, 257, 1481,
  1481, 733, 295, 636, 281, 1752, 411, 1071, 50914], "temperature": 0.0, "avg_logprob":
  -0.2420102528163365, "compression_ratio": 1.626984126984127, "no_speech_prob": 0.004987666383385658},
  {"id": 807, "seek": 391100, "start": 3922.0, "end": 3927.8, "text": " side of things.
  But why specifically neural search? What drives you to to work on it?", "tokens":
  [50914, 1252, 295, 721, 13, 583, 983, 4682, 18161, 3164, 30, 708, 11754, 291, 281,
  281, 589, 322, 309, 30, 51204], "temperature": 0.0, "avg_logprob": -0.2420102528163365,
  "compression_ratio": 1.626984126984127, "no_speech_prob": 0.004987666383385658},
  {"id": 808, "seek": 391100, "start": 3929.08, "end": 3935.48, "text": " Well, what
  attracted me to I was initially attracted very much to the idea of", "tokens": [51268,
  1042, 11, 437, 15912, 385, 281, 286, 390, 9105, 15912, 588, 709, 281, 264, 1558,
  295, 51588], "temperature": 0.0, "avg_logprob": -0.2420102528163365, "compression_ratio":
  1.626984126984127, "no_speech_prob": 0.004987666383385658}, {"id": 809, "seek":
  391100, "start": 3935.48, "end": 3940.36, "text": " automated reasoning. And then
  of course, that comes if it''s current incarnation,", "tokens": [51588, 18473, 21577,
  13, 400, 550, 295, 1164, 11, 300, 1487, 498, 309, 311, 2190, 49988, 11, 51832],
  "temperature": 0.0, "avg_logprob": -0.2420102528163365, "compression_ratio": 1.626984126984127,
  "no_speech_prob": 0.004987666383385658}, {"id": 810, "seek": 394036, "start": 3940.36,
  "end": 3946.6800000000003, "text": " it''s machine learning. And so I started to
  learn about that. And I had this", "tokens": [50364, 309, 311, 3479, 2539, 13, 400,
  370, 286, 1409, 281, 1466, 466, 300, 13, 400, 286, 632, 341, 50680], "temperature":
  0.0, "avg_logprob": -0.24763920542958018, "compression_ratio": 1.5236220472440944,
  "no_speech_prob": 0.0061943805776536465}, {"id": 811, "seek": 394036, "start": 3946.6800000000003,
  "end": 3951.08, "text": " opportunity to work with the Ray Kurzweil who joined Google,
  I think around 2012.", "tokens": [50680, 2650, 281, 589, 365, 264, 10883, 45307,
  826, 388, 567, 6869, 3329, 11, 286, 519, 926, 9125, 13, 50900], "temperature": 0.0,
  "avg_logprob": -0.24763920542958018, "compression_ratio": 1.5236220472440944, "no_speech_prob":
  0.0061943805776536465}, {"id": 812, "seek": 394036, "start": 3952.04, "end": 3956.36,
  "text": " I knew about him. He''s a very inspirational figure. And he was specifically",
  "tokens": [50948, 286, 2586, 466, 796, 13, 634, 311, 257, 588, 33554, 2573, 13,
  400, 415, 390, 4682, 51164], "temperature": 0.0, "avg_logprob": -0.24763920542958018,
  "compression_ratio": 1.5236220472440944, "no_speech_prob": 0.0061943805776536465},
  {"id": 813, "seek": 394036, "start": 3956.36, "end": 3960.08, "text": " working
  on language understanding because he saw that as being very critical", "tokens":
  [51164, 1364, 322, 2856, 3701, 570, 415, 1866, 300, 382, 885, 588, 4924, 51350],
  "temperature": 0.0, "avg_logprob": -0.24763920542958018, "compression_ratio": 1.5236220472440944,
  "no_speech_prob": 0.0061943805776536465}, {"id": 814, "seek": 394036, "start": 3961.08,
  "end": 3968.2400000000002, "text": " to advancement in artificial intelligence.
  So so you know, then beyond that,", "tokens": [51400, 281, 35764, 294, 11677, 7599,
  13, 407, 370, 291, 458, 11, 550, 4399, 300, 11, 51758], "temperature": 0.0, "avg_logprob":
  -0.24763920542958018, "compression_ratio": 1.5236220472440944, "no_speech_prob":
  0.0061943805776536465}, {"id": 815, "seek": 396824, "start": 3968.24, "end": 3972.0,
  "text": " I would say those are my broad interests. But then I just worked in this
  area", "tokens": [50364, 286, 576, 584, 729, 366, 452, 4152, 8847, 13, 583, 550,
  286, 445, 2732, 294, 341, 1859, 50552], "temperature": 0.0, "avg_logprob": -0.15510095868791854,
  "compression_ratio": 1.6135458167330676, "no_speech_prob": 0.00186805403791368},
  {"id": 816, "seek": 396824, "start": 3972.0, "end": 3978.16, "text": " specifically
  for eight years. And I think I became quite good at what I was doing.", "tokens":
  [50552, 4682, 337, 3180, 924, 13, 400, 286, 519, 286, 3062, 1596, 665, 412, 437,
  286, 390, 884, 13, 50860], "temperature": 0.0, "avg_logprob": -0.15510095868791854,
  "compression_ratio": 1.6135458167330676, "no_speech_prob": 0.00186805403791368},
  {"id": 817, "seek": 396824, "start": 3978.16, "end": 3983.24, "text": " And then
  also saw that what I was doing post 2017 in particular with this", "tokens": [50860,
  400, 550, 611, 1866, 300, 437, 286, 390, 884, 2183, 6591, 294, 1729, 365, 341, 51114],
  "temperature": 0.0, "avg_logprob": -0.15510095868791854, "compression_ratio": 1.6135458167330676,
  "no_speech_prob": 0.00186805403791368}, {"id": 818, "seek": 396824, "start": 3983.24,
  "end": 3991.8799999999997, "text": " neural network based retrieval had a lot of
  applicability to products. And you know,", "tokens": [51114, 18161, 3209, 2361,
  19817, 3337, 632, 257, 688, 295, 2580, 2310, 281, 3383, 13, 400, 291, 458, 11, 51546],
  "temperature": 0.0, "avg_logprob": -0.15510095868791854, "compression_ratio": 1.6135458167330676,
  "no_speech_prob": 0.00186805403791368}, {"id": 819, "seek": 396824, "start": 3991.8799999999997,
  "end": 3996.8799999999997, "text": " I think that being in a research team or research
  team has a different type of focus.", "tokens": [51546, 286, 519, 300, 885, 294,
  257, 2132, 1469, 420, 2132, 1469, 575, 257, 819, 2010, 295, 1879, 13, 51796], "temperature":
  0.0, "avg_logprob": -0.15510095868791854, "compression_ratio": 1.6135458167330676,
  "no_speech_prob": 0.00186805403791368}, {"id": 820, "seek": 399688, "start": 3997.6800000000003,
  "end": 4002.0, "text": " There''s a lot of focus on on publishing papers and things,
  but not necessarily a lot of", "tokens": [50404, 821, 311, 257, 688, 295, 1879,
  322, 322, 17832, 10577, 293, 721, 11, 457, 406, 4725, 257, 688, 295, 50620], "temperature":
  0.0, "avg_logprob": -0.15346144013485666, "compression_ratio": 1.644927536231884,
  "no_speech_prob": 0.006761382799595594}, {"id": 821, "seek": 399688, "start": 4002.0,
  "end": 4008.88, "text": " interest or appetite for building platform. So in that
  way, maybe this wasn''t really the right place", "tokens": [50620, 1179, 420, 23996,
  337, 2390, 3663, 13, 407, 294, 300, 636, 11, 1310, 341, 2067, 380, 534, 264, 558,
  1081, 50964], "temperature": 0.0, "avg_logprob": -0.15346144013485666, "compression_ratio":
  1.644927536231884, "no_speech_prob": 0.006761382799595594}, {"id": 822, "seek":
  399688, "start": 4008.88, "end": 4016.0, "text": " to attempt that kind of work.
  But to me, I''m an engineer as well. So this is this is very interesting.", "tokens":
  [50964, 281, 5217, 300, 733, 295, 589, 13, 583, 281, 385, 11, 286, 478, 364, 11403,
  382, 731, 13, 407, 341, 307, 341, 307, 588, 1880, 13, 51320], "temperature": 0.0,
  "avg_logprob": -0.15346144013485666, "compression_ratio": 1.644927536231884, "no_speech_prob":
  0.006761382799595594}, {"id": 823, "seek": 399688, "start": 4017.52, "end": 4020.7200000000003,
  "text": " And I''m not sure if I''m answering your question, but that''s some of
  my motivation.", "tokens": [51396, 400, 286, 478, 406, 988, 498, 286, 478, 13430,
  428, 1168, 11, 457, 300, 311, 512, 295, 452, 12335, 13, 51556], "temperature": 0.0,
  "avg_logprob": -0.15346144013485666, "compression_ratio": 1.644927536231884, "no_speech_prob":
  0.006761382799595594}, {"id": 824, "seek": 399688, "start": 4020.7200000000003,
  "end": 4026.6400000000003, "text": " No, you do. I mean, essentially, I''m currently
  leading a search team. And yeah,", "tokens": [51556, 883, 11, 291, 360, 13, 286,
  914, 11, 4476, 11, 286, 478, 4362, 5775, 257, 3164, 1469, 13, 400, 1338, 11, 51852],
  "temperature": 0.0, "avg_logprob": -0.15346144013485666, "compression_ratio": 1.644927536231884,
  "no_speech_prob": 0.006761382799595594}, {"id": 825, "seek": 402664, "start": 4026.64,
  "end": 4031.2799999999997, "text": " you know, our KPIs is like, okay, how many
  papers you published, how many patents you can file.", "tokens": [50364, 291, 458,
  11, 527, 41371, 6802, 307, 411, 11, 1392, 11, 577, 867, 10577, 291, 6572, 11, 577,
  867, 38142, 291, 393, 3991, 13, 50596], "temperature": 0.0, "avg_logprob": -0.13301255702972412,
  "compression_ratio": 1.6597222222222223, "no_speech_prob": 0.003590879263356328},
  {"id": 826, "seek": 402664, "start": 4032.72, "end": 4038.24, "text": " But also
  when you start thinking, okay, what impact am I making, right? There is not that
  much room", "tokens": [50668, 583, 611, 562, 291, 722, 1953, 11, 1392, 11, 437,
  2712, 669, 286, 1455, 11, 558, 30, 821, 307, 406, 300, 709, 1808, 50944], "temperature":
  0.0, "avg_logprob": -0.13301255702972412, "compression_ratio": 1.6597222222222223,
  "no_speech_prob": 0.003590879263356328}, {"id": 827, "seek": 402664, "start": 4038.24,
  "end": 4044.96, "text": " to think about creating, maybe you can create a vision,
  but you might not necessarily tie it", "tokens": [50944, 281, 519, 466, 4084, 11,
  1310, 291, 393, 1884, 257, 5201, 11, 457, 291, 1062, 406, 4725, 7582, 309, 51280],
  "temperature": 0.0, "avg_logprob": -0.13301255702972412, "compression_ratio": 1.6597222222222223,
  "no_speech_prob": 0.003590879263356328}, {"id": 828, "seek": 402664, "start": 4044.96,
  "end": 4050.0, "text": " in back to the day-to-day scenarios of users. You have
  to be part of engineering, probably,", "tokens": [51280, 294, 646, 281, 264, 786,
  12, 1353, 12, 810, 15077, 295, 5022, 13, 509, 362, 281, 312, 644, 295, 7043, 11,
  1391, 11, 51532], "temperature": 0.0, "avg_logprob": -0.13301255702972412, "compression_ratio":
  1.6597222222222223, "no_speech_prob": 0.003590879263356328}, {"id": 829, "seek":
  402664, "start": 4050.0, "end": 4054.8799999999997, "text": " to start delivering
  these things at which point you are no longer a researcher. So it sounds like",
  "tokens": [51532, 281, 722, 14666, 613, 721, 412, 597, 935, 291, 366, 572, 2854,
  257, 21751, 13, 407, 309, 3263, 411, 51776], "temperature": 0.0, "avg_logprob":
  -0.13301255702972412, "compression_ratio": 1.6597222222222223, "no_speech_prob":
  0.003590879263356328}, {"id": 830, "seek": 405488, "start": 4055.28, "end": 4060.32,
  "text": " you managed to combine both of these engineering and research at ZRI.",
  "tokens": [50384, 291, 6453, 281, 10432, 1293, 295, 613, 7043, 293, 2132, 412, 1176,
  5577, 13, 50636], "temperature": 0.0, "avg_logprob": -0.1666931254523141, "compression_ratio":
  1.6840148698884758, "no_speech_prob": 0.004649677779525518}, {"id": 831, "seek":
  405488, "start": 4062.32, "end": 4069.84, "text": " Yes, yes. It''s kind of both
  of the passions together in one company. And if we''re successful,", "tokens": [50736,
  1079, 11, 2086, 13, 467, 311, 733, 295, 1293, 295, 264, 30640, 1214, 294, 472, 2237,
  13, 400, 498, 321, 434, 4406, 11, 51112], "temperature": 0.0, "avg_logprob": -0.1666931254523141,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.004649677779525518},
  {"id": 832, "seek": 405488, "start": 4069.84, "end": 4074.08, "text": " and we can
  take it into the future, the research end of the program is something that I''d
  really", "tokens": [51112, 293, 321, 393, 747, 309, 666, 264, 2027, 11, 264, 2132,
  917, 295, 264, 1461, 307, 746, 300, 286, 1116, 534, 51324], "temperature": 0.0,
  "avg_logprob": -0.1666931254523141, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.004649677779525518}, {"id": 833, "seek": 405488, "start": 4074.08, "end": 4079.52,
  "text": " like to ramp up a lot. Since we started, honestly, there''s been more
  engineering and less research.", "tokens": [51324, 411, 281, 12428, 493, 257, 688,
  13, 4162, 321, 1409, 11, 6095, 11, 456, 311, 668, 544, 7043, 293, 1570, 2132, 13,
  51596], "temperature": 0.0, "avg_logprob": -0.1666931254523141, "compression_ratio":
  1.6840148698884758, "no_speech_prob": 0.004649677779525518}, {"id": 834, "seek":
  405488, "start": 4080.7200000000003, "end": 4084.1600000000003, "text": " The training,
  the neural networks was at the early stage of the company, and then we haven''t",
  "tokens": [51656, 440, 3097, 11, 264, 18161, 9590, 390, 412, 264, 2440, 3233, 295,
  264, 2237, 11, 293, 550, 321, 2378, 380, 51828], "temperature": 0.0, "avg_logprob":
  -0.1666931254523141, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.004649677779525518}, {"id": 835, "seek": 408416, "start": 4084.16, "end": 4093.04,
  "text": " revisited it since then. But I think 2022 is going to be, first of all,
  it''s going to be a", "tokens": [50364, 20767, 1226, 309, 1670, 550, 13, 583, 286,
  519, 20229, 307, 516, 281, 312, 11, 700, 295, 439, 11, 309, 311, 516, 281, 312,
  257, 50808], "temperature": 0.0, "avg_logprob": -0.1808463136355082, "compression_ratio":
  1.482905982905983, "no_speech_prob": 0.003978653345257044}, {"id": 836, "seek":
  408416, "start": 4093.04, "end": 4099.5199999999995, "text": " big year for this
  industry. Beyond Pinecon getting funding, I was recently looking Gina AI,", "tokens":
  [50808, 955, 1064, 337, 341, 3518, 13, 19707, 33531, 1671, 1242, 6137, 11, 286,
  390, 3938, 1237, 34711, 7318, 11, 51132], "temperature": 0.0, "avg_logprob": -0.1808463136355082,
  "compression_ratio": 1.482905982905983, "no_speech_prob": 0.003978653345257044},
  {"id": 837, "seek": 408416, "start": 4099.5199999999995, "end": 4104.72, "text":
  " if you''re familiar with them. They, I think raised $30 million, it was in TechCrunch.",
  "tokens": [51132, 498, 291, 434, 4963, 365, 552, 13, 814, 11, 286, 519, 6005, 1848,
  3446, 2459, 11, 309, 390, 294, 13795, 38750, 1680, 13, 51392], "temperature": 0.0,
  "avg_logprob": -0.1808463136355082, "compression_ratio": 1.482905982905983, "no_speech_prob":
  0.003978653345257044}, {"id": 838, "seek": 408416, "start": 4105.5199999999995,
  "end": 4112.24, "text": " So the industry is starting to get some notice. And for
  us as well, we expect,", "tokens": [51432, 407, 264, 3518, 307, 2891, 281, 483,
  512, 3449, 13, 400, 337, 505, 382, 731, 11, 321, 2066, 11, 51768], "temperature":
  0.0, "avg_logprob": -0.1808463136355082, "compression_ratio": 1.482905982905983,
  "no_speech_prob": 0.003978653345257044}, {"id": 839, "seek": 411224, "start": 4113.2,
  "end": 4116.08, "text": " we expect to really expand in 2022.", "tokens": [50412,
  321, 2066, 281, 534, 5268, 294, 20229, 13, 50556], "temperature": 0.0, "avg_logprob":
  -0.1880799461813534, "compression_ratio": 1.683794466403162, "no_speech_prob": 0.014929133467376232},
  {"id": 840, "seek": 411224, "start": 4116.08, "end": 4123.12, "text": " Oh, yeah,
  fantastic. And I mean, one manager that I worked with used to say that you need
  to first", "tokens": [50556, 876, 11, 1338, 11, 5456, 13, 400, 286, 914, 11, 472,
  6598, 300, 286, 2732, 365, 1143, 281, 584, 300, 291, 643, 281, 700, 50908], "temperature":
  0.0, "avg_logprob": -0.1880799461813534, "compression_ratio": 1.683794466403162,
  "no_speech_prob": 0.014929133467376232}, {"id": 841, "seek": 411224, "start": 4123.12,
  "end": 4128.88, "text": " build the plumbing. And that''s your engineering work.
  Once you have the plumbing, you can stand on", "tokens": [50908, 1322, 264, 39993,
  13, 400, 300, 311, 428, 7043, 589, 13, 3443, 291, 362, 264, 39993, 11, 291, 393,
  1463, 322, 51196], "temperature": 0.0, "avg_logprob": -0.1880799461813534, "compression_ratio":
  1.683794466403162, "no_speech_prob": 0.014929133467376232}, {"id": 842, "seek":
  411224, "start": 4128.88, "end": 4133.76, "text": " it and actually fix some other
  things, high level. And that''s where you will probably come back to", "tokens":
  [51196, 309, 293, 767, 3191, 512, 661, 721, 11, 1090, 1496, 13, 400, 300, 311, 689,
  291, 486, 1391, 808, 646, 281, 51440], "temperature": 0.0, "avg_logprob": -0.1880799461813534,
  "compression_ratio": 1.683794466403162, "no_speech_prob": 0.014929133467376232},
  {"id": 843, "seek": 411224, "start": 4134.32, "end": 4138.719999999999, "text":
  " training neural networks and actually nailing that use case for your customers.
  Sounds really", "tokens": [51468, 3097, 18161, 9590, 293, 767, 10173, 278, 300,
  764, 1389, 337, 428, 4581, 13, 14576, 534, 51688], "temperature": 0.0, "avg_logprob":
  -0.1880799461813534, "compression_ratio": 1.683794466403162, "no_speech_prob": 0.014929133467376232},
  {"id": 844, "seek": 413872, "start": 4138.72, "end": 4146.88, "text": " exciting.
  This was really packed and so much thinking that you brought in. And also some",
  "tokens": [50364, 4670, 13, 639, 390, 534, 13265, 293, 370, 709, 1953, 300, 291,
  3038, 294, 13, 400, 611, 512, 50772], "temperature": 0.0, "avg_logprob": -0.13732930525992681,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.007298737298697233},
  {"id": 845, "seek": 413872, "start": 4146.88, "end": 4151.52, "text": " discoveries
  during this conversation. I really enjoyed it. I''m just thinking, is there something",
  "tokens": [50772, 28400, 1830, 341, 3761, 13, 286, 534, 4626, 309, 13, 286, 478,
  445, 1953, 11, 307, 456, 746, 51004], "temperature": 0.0, "avg_logprob": -0.13732930525992681,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.007298737298697233},
  {"id": 846, "seek": 413872, "start": 4151.52, "end": 4155.6, "text": " you would
  like to announce from your product side, something that our listeners can try?",
  "tokens": [51004, 291, 576, 411, 281, 7478, 490, 428, 1674, 1252, 11, 746, 300,
  527, 23274, 393, 853, 30, 51208], "temperature": 0.0, "avg_logprob": -0.13732930525992681,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.007298737298697233},
  {"id": 847, "seek": 413872, "start": 4157.6, "end": 4161.52, "text": " Well, thank
  you. Thank you for the opportunity. I think what I would say is that if", "tokens":
  [51308, 1042, 11, 1309, 291, 13, 1044, 291, 337, 264, 2650, 13, 286, 519, 437, 286,
  576, 584, 307, 300, 498, 51504], "temperature": 0.0, "avg_logprob": -0.13732930525992681,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.007298737298697233},
  {"id": 848, "seek": 413872, "start": 4162.16, "end": 4166.320000000001, "text":
  " what we''ve been talking about is interesting and if someone would like to try
  it out,", "tokens": [51536, 437, 321, 600, 668, 1417, 466, 307, 1880, 293, 498,
  1580, 576, 411, 281, 853, 309, 484, 11, 51744], "temperature": 0.0, "avg_logprob":
  -0.13732930525992681, "compression_ratio": 1.6818181818181819, "no_speech_prob":
  0.007298737298697233}, {"id": 849, "seek": 416632, "start": 4167.28, "end": 4173.12,
  "text": " then we''ve created a special promo code. We''re currently in a closed
  beta. So we''re accepting", "tokens": [50412, 550, 321, 600, 2942, 257, 2121, 26750,
  3089, 13, 492, 434, 4362, 294, 257, 5395, 9861, 13, 407, 321, 434, 17391, 50704],
  "temperature": 0.0, "avg_logprob": -0.136667534856513, "compression_ratio": 1.583673469387755,
  "no_speech_prob": 0.008405245840549469}, {"id": 850, "seek": 416632, "start": 4173.12,
  "end": 4178.16, "text": " customers, but kind of on a case by case basis. But we''ve
  created a promo code for listeners of this", "tokens": [50704, 4581, 11, 457, 733,
  295, 322, 257, 1389, 538, 1389, 5143, 13, 583, 321, 600, 2942, 257, 26750, 3089,
  337, 23274, 295, 341, 50956], "temperature": 0.0, "avg_logprob": -0.136667534856513,
  "compression_ratio": 1.583673469387755, "no_speech_prob": 0.008405245840549469},
  {"id": 851, "seek": 416632, "start": 4178.16, "end": 4183.12, "text": " podcast.
  I think I''m going to, I''m sure the exact code with you. And then you can post
  it in the", "tokens": [50956, 7367, 13, 286, 519, 286, 478, 516, 281, 11, 286, 478,
  988, 264, 1900, 3089, 365, 291, 13, 400, 550, 291, 393, 2183, 309, 294, 264, 51204],
  "temperature": 0.0, "avg_logprob": -0.136667534856513, "compression_ratio": 1.583673469387755,
  "no_speech_prob": 0.008405245840549469}, {"id": 852, "seek": 416632, "start": 4183.12,
  "end": 4191.599999999999, "text": " comments to the video. But essentially would
  give, give you a 50 megabyte account, which is much", "tokens": [51204, 3053, 281,
  264, 960, 13, 583, 4476, 576, 976, 11, 976, 291, 257, 2625, 10816, 34529, 2696,
  11, 597, 307, 709, 51628], "temperature": 0.0, "avg_logprob": -0.136667534856513,
  "compression_ratio": 1.583673469387755, "no_speech_prob": 0.008405245840549469},
  {"id": 853, "seek": 419160, "start": 4191.68, "end": 4198.56, "text": " larger than
  our standard trial account by about a factor of three for one month. If you want
  to just", "tokens": [50368, 4833, 813, 527, 3832, 7308, 2696, 538, 466, 257, 5952,
  295, 1045, 337, 472, 1618, 13, 759, 291, 528, 281, 445, 50712], "temperature": 0.0,
  "avg_logprob": -0.12828274242213514, "compression_ratio": 1.6442953020134228, "no_speech_prob":
  0.01291816495358944}, {"id": 854, "seek": 419160, "start": 4198.56, "end": 4202.96,
  "text": " try out the system that we''ve been talking about. This is fantastic.
  Thank you, Amin, for this", "tokens": [50712, 853, 484, 264, 1185, 300, 321, 600,
  668, 1417, 466, 13, 639, 307, 5456, 13, 1044, 291, 11, 2012, 259, 11, 337, 341,
  50932], "temperature": 0.0, "avg_logprob": -0.12828274242213514, "compression_ratio":
  1.6442953020134228, "no_speech_prob": 0.01291816495358944}, {"id": 855, "seek":
  419160, "start": 4202.96, "end": 4209.76, "text": " opportunity. I''m sure some
  listeners will take this into use and build some cool vector search", "tokens":
  [50932, 2650, 13, 286, 478, 988, 512, 23274, 486, 747, 341, 666, 764, 293, 1322,
  512, 1627, 8062, 3164, 51272], "temperature": 0.0, "avg_logprob": -0.12828274242213514,
  "compression_ratio": 1.6442953020134228, "no_speech_prob": 0.01291816495358944},
  {"id": 856, "seek": 419160, "start": 4209.76, "end": 4215.84, "text": " applications
  for their products. That would be great. Yeah, it was a pleasure to talk to you.
  I hope", "tokens": [51272, 5821, 337, 641, 3383, 13, 663, 576, 312, 869, 13, 865,
  11, 309, 390, 257, 6834, 281, 751, 281, 291, 13, 286, 1454, 51576], "temperature":
  0.0, "avg_logprob": -0.12828274242213514, "compression_ratio": 1.6442953020134228,
  "no_speech_prob": 0.01291816495358944}, {"id": 857, "seek": 419160, "start": 4215.84,
  "end": 4220.88, "text": " we can talk at some point down the road as well. And I
  wish you all the best in the future. In the", "tokens": [51576, 321, 393, 751, 412,
  512, 935, 760, 264, 3060, 382, 731, 13, 400, 286, 3172, 291, 439, 264, 1151, 294,
  264, 2027, 13, 682, 264, 51828], "temperature": 0.0, "avg_logprob": -0.12828274242213514,
  "compression_ratio": 1.6442953020134228, "no_speech_prob": 0.01291816495358944},
  {"id": 858, "seek": 422088, "start": 4220.96, "end": 4227.52, "text": " next year
  with your ambition and also with reaching to clients and getting contracts. And",
  "tokens": [50368, 958, 1064, 365, 428, 22814, 293, 611, 365, 9906, 281, 6982, 293,
  1242, 13952, 13, 400, 50696], "temperature": 0.0, "avg_logprob": -0.22535778724983946,
  "compression_ratio": 1.5942857142857143, "no_speech_prob": 0.00485513499006629},
  {"id": 859, "seek": 422088, "start": 4228.4800000000005, "end": 4234.0, "text":
  " all the best to you on that front. It was my pleasure to talk to you and hopefully
  to see you", "tokens": [50744, 439, 264, 1151, 281, 291, 322, 300, 1868, 13, 467,
  390, 452, 6834, 281, 751, 281, 291, 293, 4696, 281, 536, 291, 51020], "temperature":
  0.0, "avg_logprob": -0.22535778724983946, "compression_ratio": 1.5942857142857143,
  "no_speech_prob": 0.00485513499006629}, {"id": 860, "seek": 422088, "start": 4234.0,
  "end": 4239.68, "text": " next year as well. Thank you so much. It was good talking
  to you too. Thank you, Amin. Bye-bye.", "tokens": [51020, 958, 1064, 382, 731, 13,
  1044, 291, 370, 709, 13, 467, 390, 665, 1417, 281, 291, 886, 13, 1044, 291, 11,
  2012, 259, 13, 4621, 12, 6650, 13, 51304], "temperature": 0.0, "avg_logprob": -0.22535778724983946,
  "compression_ratio": 1.5942857142857143, "no_speech_prob": 0.00485513499006629}]'
---

Hello, vector podcast is here and today we're going to be talking with Amin Ahmed, co-founder and CEO of the company called ZIR AI.
I'm really, really excited to talk to Amin because basically he's innovating in this space, his company is innovating in this space of bringing vector search to practice and also making it usable. Hey, I mean, how are you? I'm doing fine. Thank you. Thanks for having me. Awesome.
Thanks for joining. And I know it's almost like festive times, so it's probably quite a packed schedule for you otherwise as well. So yeah, I was thinking let's traditionally start with the introduction.
Like, can you please tell me a bit of background before ZIR AI and OZIR AI is a startup and you're rolling at ZIR AI? Yes, sure. Me and my co-founder, we started ZIR AI in 2020. Before that, we were both working at Google. I had been there since 2010.
I worked in Google Research, focused on NLP and language understanding with machine learning. Prior to that, I had worked many other places in the industry. So I've been in the industry about 24 or 25 years now.
And around 2017, the team that I was working on in Google Research actually became known for Gmail Smart Reply. If you remember that feature. Yeah, that's an excellent feature. The moment I saw it, it was like, wow, that's fantastic. Yeah. Yeah, and it was impressive.
And I would say maybe it was a very practical application of NLP that went, that was deployed on a very large scale. So that was the research group that I was a part of. It was under Rakers, while that was developed in collaboration with some others.
Anyway, around that time, I became very interested in using neural networks for more general purpose information retrieval. And I specifically formulated this question answering over a large corpus. And at the time, I mean, Bert, when it was released a year later, changed this idea.
But at the time, a lot of people would approach a machine learning problem from scratch. It would take a completely uninitialized neural network and then try to train it. And when the models get big and deep, mostly you don't have enough data for your task.
And it also, you know, that doesn't jive very well with if you think about how humans approach a task.
If you ask me to answer a question or to read a message from a medical textbook, I may not be a doctor, but my understanding of the English language will allow me to get some of the information content from that passage.
So in the same way, I was thinking that if a neural network is truly understanding language in the way that people do, it should have this property. And it should be possible to train a general purpose neural network that without fine tuning in a specific domain can also work reasonably well.
So I set out to build this thing. And that was my research program in 2017. And we were actually able to launch the first iteration of that model in a product called Google Talk to Books. So to, and I'm saying this to my knowledge, I would love if someone corrected me in the comments section here.
This is Google Talk to Books is the first large scale end-to-end demonstration of a neural information retrieval system. So it is a search over a corpus of around 200,000 books from the Google Books corpus. But it's done entirely with vector search. And I'm not aware of anything before that.
So the neural network is very important here. I, not part of the team that conceived this idea and I was not actively working on it. They had a neural network which wasn't producing good enough results.
And we put in this more general purpose question answering your network and the results dramatically improved. This was basically the first rollout.
But then what I observed over the subsequent years was that I was able to take exactly the same neural network and apply it in at least six different products within Google. And this is what convinced me of the business value of what had been demonstrated here.
This could actually improve metrics and products used by millions of people. And so this was essentially the genesis of the idea of the ZRAI.
We started me in my co-founder in 2020 and the objective is to provide something like elastic search or algolia, except using the principles of neural information retrieval. So as you know, elastic search and algolia are based on the BM25 algorithm fundamentally.
So yeah, so that's what we've been doing for the last two years. Yeah, this is fantastic.
I mean, it's fantastic also that you bring your experience from such a large company innovating in search, right? Over to, you know, the rest of the world essentially, right? So that I believe your goal is to apply this with as many clients as possible.
And are you focusing mostly on NLP at the moment, natural language processing? Yeah, so well, we're focused from a customer's perspective. We provide a tech search solution.
Now, one of the beauties of embedding based techniques is that in your network, you can go beyond text and you can embed images, video and other types of media into a common embedding space. So that is where this company will eventually go.
But my roots are in NLP and I think that tech search by itself is a large area that takes an effort to do well. So that's where we're focused initially. Yeah, that makes total sense.
But as you said, you know, vector search is not kind of constrained by the application as long as you can embed it, right?
And plus all these multimodal scenarios where you can combine, let's say, your camera pointed at something and then you're talking to it and then you can kind of get some textual matches and suggestions, right? So that could be a very rich experience.
Right, right. And that particular application is actually achievable now, even in an all text platform, if you feed the transcripts in. And these neural network approaches tend to work especially well with natural speech, both as query input.
So this is why they're often used in technologies like Assistant or Alexa. Because people, when they speak, it's obviously much different than when you're typing keywords in a search box with your keyboard. But then also when searching over natural language text like transcripts. Yeah, absolutely.
And when you say neural networks, you know, some of them, let's say, vector database providers and vendors on the market, they give you sort of this machinery. You can plug in some models. They also have some models available, let's say, from hugging face.
In your case, in case of ZRI, are you innovating in this space of creating this neural networks for your clients? Yes, we are approaching the problem holistically. So we're, you know, the vector database is one critical component of a neural information retrieval system.
But there's other pieces, for instance, like the re-ranking piece or the neural network that produces the embeddings. And all of these need to work in coordination and tandem. Ideally, when they do, you can squeeze a lot more performance out of this system.
So yes, our focus is on, we even handle data ingestion. It's not a big area of focus. But the reality is that you have to make your experiences as easy as possible for widespread adoption, I think. So we allow our customers to just shovel in, you know, PDF documents and all kinds of other formats.
We perform the text extraction. We perform the segmentation of the document. And we actually do the encoding with the neural network, build the vector database and then handle the serving as well. Yeah, so it sounds like an all-around solution.
And I mean, it's very typical, you know, in some sense kind of to bring some algorithm or some idea to the market, but like it doesn't have any connectors. Okay, how do I feed data into it? Or maybe there is like a simple demo. And yeah, nothing beyond that.
But it sounds like you are taking the kind of all-around approach.
And have you been looking to implement everything yourself or are you also kind of reusing some of the open source pipelines, you know, like for example, for embedding or for document conversions and so on? Yeah, we are using open source as much as we can and where we think it makes sense.
So for instance, for content extraction, there's a Pashitika, which is a very good framework. But then there are certain document types for which there are better alternatives out there. And, you know, we've had certain customers for which PDF extraction, for instance, was a priority.
And we discovered some shortfalls with Tick-N-We went and we researched and found there's better alternatives out there. And so we've got those implemented. But we didn't write a PDF extractor from scratch, obviously. That's too much for a two-man company to do.
So yeah, we're trying to really combine the best of breed in every area and create a cohesive system that just works out of the box quite well for a broad range of use cases. Oh yeah, that's awesome.
And it's also great to hear that you reuse open source software, you know, at least initially or maybe you can find two minutes, so to say. But yeah, I mean, also that's amazing because you can quickly kind of build your product and focus on the goal.
Yeah, and now that we approached this more kind of closely, can you actually describe what is your product today? So as a client, what can I get? What can I, what kind of support you also provide? But first, can you start with the product itself? Yes.
So to describe it abstractly, and then I'll explain very concretely what I mean. I would say that we're a cloud platform as a service for text retrieval or text search. So the way it looks is we have two main APIs, one for indexing content and the other for running queries on the content.
So an organization would come and they would index a large amount of content. They might index periodically or incrementally as well over time.
And this would accrete in an index and then subsequently they would come and they would run generally natural language text queries against that corpus and we would return the best matches. So what we actually provide and how that looks on our platform.
So we, you essentially, you know, you come and you sign up just the way you would sign up for an AWS account, you're dropped into an admin console. Everything you can do in the admin console can be done through APIs. We're basically focused on again, a platform.
So we're accessible through GRPC and rest. The platform, the console is basically to allow you to, you know, point and click and quickly experiment and discover the value of the system.
Because our vision was that within, within 15 to 30 minutes, someone from an organization should be able to come, drop their documents into the system and determine whether or not it's even going to meet their needs.
And then if it does, they can consult the documentation and learn how to use the APIs and get a proper integration going. So we organize collections of documents into what are called corpora. So one corpus is essentially, it's a customer defined entity.
It groups related documents that they want to search together as a unit. We allow, you know, the customer to define any number of corpora, there's limits depending on the account type. And then you can essentially drag and drop the documents into the web browser, into the corpus upload.
It'll be, there's about a seven minute latency. And then you can start running queries. And when you run, we have a hosted UI that makes it easy to see the results kind of on the spot in the browser.
But when you run queries through our interface, you also have our, our, our API is, you also have the ability to run one query against multiple corpora and merge the results.
So we also support the ability to attach metadata as your indexing content, attach metadata that then is returned to you in the search results. So that would allow you to, to join to let's say another system on your end. But those are, those are some of the features that we provide. Yeah.
So it sounds like it's a self service system, right? And so if I was a client of yours, I could like get a subscription trial subscription maybe then upload my document corpus.
How big a corpus could I upload on a trial? Do you have any limitation there at this point? So our general trial has been 15 megabytes of text. And I'll explain what that translates to. I was, I was, I was just working with another customer.
And they had about one gigabyte of PDFs that we put into a corpus. And then that turned out to be about 48 megabytes of text. So the, the billing is by the actual extracted textual content. So 15 megabytes is actually a decent data set, several hundred documents you can imagine.
So, but we have, we have plans that go much larger and we have customers that are indexing far more data. Yeah, yeah, sounds great. And then what happens next? So let's say I'm happy. I want to move forward.
Now you said that there are APIs that I can start kind of introducing inside my prototype or my existing back end. Is that right? Yeah, that's right. So we, we support primarily we promote a gRPC interface because it's high performance low latency. We also do have a rest interface.
We have fully authenticated APIs. So we use OAuth 2.0 that standard. So you would give credentials to your servers and they would use those credentials to establish an authenticated session with the platform and then run, run queries for you at a very high rate. We scale horizontally.
We can go up to hundreds of QPS, though we haven't had a customer that's needed such a high rate, but we're capable of that. Yeah, yeah.
And you also mentioned that you maintain certain like SLA guarantees like P99 latency can you speak a bit about that and also like how much of that accounts for client need versus what you are building for the future. And this is a good question.
So in terms of client need, we really haven't had any client that's required anything better than 200 milliseconds. Now there's a potential client that we're working with. They're not yet acclaimed.
They're looking for more like 50 to 60 milliseconds because essentially the look up into our system is only one part of their overall request handling process. So they have a much tighter budget.
In practice, what we're seeing on our platform for our customers today aggregated over all queries is a P99 of around 130 milliseconds. Our P50 is about 60 milliseconds. And this has been sufficient for our customers.
For customers that have tighter requirements, we actually have many different ways to address it. So actually the main latency is not from the vector database. The vector database is generally quite fast. It's the neural network that has to do the text encoding. That's the bottleneck.
So we have the ability to set up dedicated pools of encoders, neural networks that do this encoding of four customers. So we scale and we're cost efficient by sharing the pool across all customers. But for customers that have very stringent needs, we can set up dedicated pools for them.
But even when you go, let's say single customer, single node, maybe GPU node, there are still theoretical boundary to how fast it can be.
Let's say if I take an off-the-shelf birth model, and if I throw 768 dimensions, what's going to happen? How can I fine tune it on the speed size? Yeah, well, let me address two things that you said there.
So the off-the-shelf birth model is a very common approach that many companies are trying to productionize NLP. They use it because birth has a phenomenal accuracy. You fine tune it with a little bit of data. And everyone always hits the same problem that is very difficult to productionize.
And even at a place like Google, they didn't productionize birth. They had to distill birth and productionize it. And distillation requires a lot of expertise. It's out of the reach, I think, of most companies.
So as good as the results look in a staging environment, that's not really a practical to productionize that.
And that comes back to the original point that we tried to make the right choices where if we were deploying birth, either it would be enormously expensive for us because we'd have to be using GPU instances or TPU instances, or we would have very high latencies.
So we have a model that produces similar performance, but it runs much faster. It's still transformer-based.
Coming to your second point, I think your main question, your original question, was actually what's the theoretical limit of performance that we can achieve in terms of are you asking from a latency perspective? Yeah, a latency. So I'll say this.
When it comes to the vector database, you probably know this better than I do. If it's indexed and quantized correctly on our last stuff, even running on CPUs, you can get down to three, four milliseconds of latency.
It depends on so many trade-offs, like how much recolor you will decircify and other things like that. What are the dimensions of the vector? But I think that we found that to be quite feasible for our system. We don't do 768 dimensions.
Our neural nets produce a little bit less, but still it's comparable. It's not that far off. In terms of the neural network, I would say that transformers are required for proper language understanding.
One of the things I didn't mention about our system was I think that we were basically one of the first teams back in 2017 to incorporate transformers production architecture. This was my colleagues, Noah Constant. He was actually one of our colleagues.
Previously being in our team was on the original transformer paper. He was in Google Brain at that time doing that research. We wanted to productionize a plan to a model. Noah basically spent a couple of months, took that research level code and got it to production quality.
Talk to books is actually being powered by a very early transformer based model. We saw an enormous performance jump in our metrics, doing nothing other than switching to transformers. I've never seen such a big jump in any... Our metrics, we were looking at F1. Our F1 jumped from 30% to 38%.
Just by switching to transformers. Not changing the training data or the evaluation objective, just making this one change in the architecture of the neural network. I would consider that's an absolute requirement.
I would also say that I'm not very familiar with the economics of GPU scaling because it's generally kind of expensive. Our neural networks are actually designed to run reasonably well on CPUs. There's also these tips like obviously Google's got the TPU, but Amazon has Inferencia.
We're still kind of experimenting with what we can do with latency there.
I think that you can count on about 20 to 30 milliseconds of latency at the low end from coming from the encoding process unless you start moving to GPU or something and then you might be able to do maybe 5 to 10 milliseconds.
If you put that all together, it seems to me realistically you can shoot for 30 to 40 milliseconds would be pretty aggressive in terms of what you can get at the lower bound. And maybe for many companies out there, this will be okay.
As long as they don't run web scale type of deployment, maybe they can scale per region or per zone or whatever it is that makes sense to them. I think sounds like 30 to 40 milliseconds could be quite an okay speed. We're talking about latency there.
I think that's a perfectly acceptable speed even for web search or something. That's literally the blink of an eye, 40 milliseconds. I think the other thing to note is that these solutions are very horizontally scalable.
In terms of serving any given throughput, you just scale the neural network and code or pools and you can replicate the vector database if using FIAS for instance you start up replicas. You can basically get almost unlimited throughput.
It just depends on how much money you have to throw at the problem. So if you need 500 QPS, bring up more hardware. If you need 5000 QPS, you can bring up more hardware and do it. Yeah, absolutely.
I also wanted to tap into what you said that distilling bird would be beyond reach for many companies. Can you open up a little bit and also can you share with our audience what do you mean by distilling? Maybe some of our subscribers don't know that.
So in the nutshell, and also why do you think that it's so hard to do?
Okay, well, so what distillation of a neural network refers to is taking a very large neural network and neural network with a lot of parameters, it's called billions of parameters, which is very accurate but cannot reasonably be run on a production workload.
And training a much smaller model that captures as much of the performance of the original model as possible, but fitting inside the engineering parameters of your production system. So able to for instance run an inference within 50 milliseconds.
So the way that distillation normally happens is you use the parent model is called the teacher model and you do a large scale labeling of data. And essentially the student model, the small model that you're training needs to learn to make the same predictions.
And interestingly, it gets as much bang for the buck in terms of training from learning to make the correct predictions as it does from learning to, you know, assign probabilities to the incorrect predictions.
So the reason I'm saying that distillation is difficult is there's, I think it approaches to it, it's still a fairly open research topic. There's a lot of active research.
I haven't looked in the last couple of years as possible that there might be frameworks out there now that make this much easier.
But certainly while I was at Google in 2018, 1920 time frame distillation was generally a topic that was tackled by entire teams working over a quarter or two, at least for the most serious production systems. That's how it was used to go. Yeah.
And definitely when it comes to collecting data as you rightly not just, you know, it's not something you can easily scale unless you have some clever technique for data augmentation.
And even then, like for text, as I was eluding in previous podcasts, you know, like if you have like a London is the capital of Great Britain, you cannot put any random city there in that specific sentence, right? Right. Right. Right. Yeah, you need to have certain control.
But there are still ways to, for example, use retrieval itself to augment your data set, right? For example, if you need more entities, you can find them through retrieval, maybe even through vector search, by the way. I don't know if somebody experimented with that already.
But there are other techniques like kind of producing these negative examples and as you alluded to, right? So you need to have as many negative also as many positive so that your model is balanced, right? And that goes to a general model training topic, which is a year to your point. Yes.
And I think that's one of the key to producing a neural retriever that can outperform BM25 in every workload. No, so it's an excellent point. Yeah. Also, I just reminded me of one challenge that we've been solving in my team actually earlier with building like a job search engine system.
And you know, like when you evaluate the performance, let's say precision or when it kind of, we call it misrecall, so how frequently it mis triggers to query, shouldn't have actually triggered.
And you know, like the basic challenge there is, okay, I have this job queries, which I can mind from certain sources.
But then you can as negative examples, you can pick everything else, right? But that everything else doesn't actually count because just to give you an example, let's say when I say find full-time job in London, right? So that's just a typical query.
You are really interested to find that slightly negative example, which says, let's say, something hours of some office, right? Which is not about job search anymore. It's about points of interest search, maybe.
And so you really want to have those examples to see, okay, does your model, you know, is able to differentiate between them?
And I guess checklist paper is another example where they go like beyond, you know, imaginary in a way that saying, okay, you can actually fulfill this criteria and you can actually check your model on various, very suspects.
Right, right. Right.
And is that something that you like, how did you go about addressing that in your research?
I mean, you know, what we did is that actually, if you look, it was like one of the early, early papers, you know, the reason I like reading papers is because you can bring some ideas from one paper to some other domain.
And so the paper was about sentiment analysis where one of the challenge was back then when it was dictionary-based systems, you know, how do I expand my positive dictionary? How do I expand my negative dictionary?
And what they propose there is that you can use a retrieval system where you say, okay, you take an instance from a positive dictionary, let's say it's good, okay.
And then you search with a pattern where you say good and then a blank and you just let your search engine tell you what good is occurring with in the sentences or text, right? And the same for the bad one.
Then they run some clustering on it so that you can actually pick more representative items from your data set.
And in principle, you could apply a similar technique with the job queries, right? And we didn't go that far, but we actually did try to use our own search engine to essentially, you know, augment.
And then there's another potential technique that might help their short of introducing hard negatives.
It's easier than introducing hard negatives just to add like what they call a margin loss, which is to essentially just say that the separation in the score that the neural network assign the positive example versus the negative examples has to be large.
So you sign some lambda and it has to be, essentially, you handicap the scores of the positive examples by that lambda and it forces the neural network to introduce more separation. So sometimes that can be helpful, even if you haven't generated hard negatives. Yeah, yeah, absolutely.
Maybe we can also cite some papers in this podcast, you know, like especially you mentioned some papers. And I will try to find this sentiment analysis paper, although I think it's probably like five, six years old or maybe even older. But I mean, this idea is still live forward, I think.
And like we shouldn't forget about them.
And if we go back to your product, so basically, like you said that you also kind of look at using some of the existing algorithms in vector search, can you name them? Or is this some kind of secret or are you customizing them as well? So for the vector search, specifically. Yeah.
I think we can say that we know we at our core, we do take advantage of phase or fire. So I'm not exactly right. I don't pronounce that from. No, but nobody knows. I think everyone says they own weight.
In my opinion, it's just an excellently designed system with a team that's actively maintaining it and there are obviously experts in that field. One of the features that customers have requested from us is the ability to mix in predicate predicates and traditional Boolean logic.
So you might have this corpus of documents and they all have this, every document has this metadata, which is the date it was published. And then you might want to say, okay, give me the most relevant matches for the query, but only for documents published in 2021.
This is like a very crisp selection criteria and this selects a subset of the corpus. So this is actually something that we have not launched yet, but we've been actively working on and will probably launch in Q1.
I believe, I recently added the support Google vertex matching engine, I think, is a recent offering. They also claim to have this support. It's important, many of our customers have asked for the same thing. So we've started from a FIAS, but we have been customizing it. Yeah, yeah, sounds good.
So basically some other companies call it symbolic filtering and that's what I think you refer to, right? So I can have certain categorical variables, so to say in my data and I can filter by it, right? Exactly, right.
Yeah, so I think vanilla fires of face doesn't have this functionality as far as I know. And so essentially you'll have to kind of extend it.
And do you plan to keep it to yourself, which is perfectly fine, or are you also able to contribute it back to the FIAS open source project? So I think what I've noticed about the authors of FIAS is that they want to keep the product very focused on being a first class vector engine.
And these are essentially augmentations that they're not interested in pulling in. And I think they would see it as scope creep, which is probably fair. That said, would we contribute it as open source? Like we could still contribute it back as open source.
In fact, down the line we could potentially make our entire stack open source.
I think some of the abusiveness of that, say, in regards to elastic and how it's worked, where you have these very large companies that essentially contribute very little, but they take advantage of their ability to launch platforms as a service like Amazon can. That's kind of scared us.
I think in the short term, we're not doing that, but that's certainly something we could plan on doing in the longer term. Yeah.
And I mean, of course, the dynamics of open source is not necessarily solved, especially as you've brought up this example with the elastic, right? And they're kind of battle between elastic and Amazon. But like for some companies, it still works as a starter. You can enter this community.
You start building the community around you. And so they bring back ideas. They feed in new use cases to you. And maybe they even implement some features, right? And is this something that you've been thinking as well along these lines? Well, I definitely see your point.
I definitely see your point. At the same time, we also do have some competition in the space. We're still in the early days, but 2021, in particular, saw the launch of several competitors. And even Microsoft is in the mix now, Microsoft's semantic search.
I think it's still in beta, Amazon launch Kendra in 2020. I think that they probably get the credit for launching the first platform as a service neural information retrieval system.
So in both of the cases, both of those systems, by the way, I think that they actually are fundamentally based on a VM25 search, followed by re-ranking with the neural network. This is what I've gathered from their own product marketing material, which is still in neural search.
It just has a difference out of pros and cons versus like straight retrieval from a vector database. So, for instance, just to give you one quick example, a multilingual search, VM25 is not going to work for a multilingual search.
You have queries coming in different languages, documents in different languages. VM25 won't work there, nor will a re-rank on a VM25 results approach work over there, because the VM25 has to bring something back to re-ranking. Well, in the case of our system, you can check on some of the demos.
We can actually embed across languages into a shared embedding space. And so you can search across languages. That's something which you need a vector database for. Yeah, exactly.
So you go multilingual on the first stage of retrieving the data dates, right? And I think this multilingual search in general, I think it has so much potential.
I don't know if Google is using it already, to some extent, but like even like at smaller scale, instead of configuring, let's say, solar. We keep mentioning last search a lot. They didn't pay for these podcasts.
But I'm just saying, let's say Apache solar, or Lycene, right? So you'll have to kind of like, yeah, go a long, long, long way to achieve it. But like, okay, now Lycene released H&SW in 9.0 version.
And so in principle, you could embed your documents using multilingual model and retrieve them in the same way, right? So do you see huge potential for the market, you know, for the multilinguality?
No, there have been some studies that showed that when eBay introduced automatic translator tools, there was a significant increase.
It was a few, I think, you know, a few percentage points of increase in commerce on their platform, which translated to hundreds and hundreds of millions of dollars.
So the, you know, the advancements that have been made in machine translation and now, and she like, cross-lingual retrieval, will serve to further break down barriers to commerce at least. And in a way that's commercially very valuable.
But speaking more broadly, I think that what I would be very interested to see is how vector databases evolve and merge into traditional database technology or into systems like Lucene, like information retrieval systems.
Because at the moment, you know, you have FIAS, it's kind of a separate discreet entity.
But longer term, just, you know, conceptually, in a way, very low-dimensional vector database technology has already made its way into my sequel and Postgres with the spatial extensions that they've supported for many years. The quadri algorithm for doing, you know, sublinear lookups on a map.
Those spatial extensions have been around for a while.
 You can easily imagine that in the future, once people start to understand how useful vector embeddings can be, and that's established, that you'll have a, you know, columns of vector type in a relational database and be able to simply build an index and perform, you know, fast nearest neighbor searches straight from Postgres.
So I think that's an exciting future to contemplate. And I see that eventually it will go there. That sounds really interesting, Lake. Do you think that vector searches in general is a hype right now? I think the way big data was few years ago.
No, no, it's not hype because, again, I saw neural information techniques, backed by vector databases, making a big difference in many products at Google.
So I think where it is right now is that there's a few big companies, like the Fang type companies in Silicon Valley, that have the expertise to take advantage of it. It's not being commoditized yet.
So it's definitely not hype, but it's got a few years to go before it enters a mainstream consciousness. Yeah, for sure.
But like to your point, like maybe at some point, vector search will become, let's say, part of Postgres or my SQL or whatever other like, kind of traditional, so to say, database, which is traditional is in its widely used.
And then you've seen already also introduced it, right? Lucine now has H&SW.
 You can go and argue to the point, okay, maybe Lucine index layout might not be kind of optimally designed for, you know, nearest neighbor retrieval because, because like if you look at five methods or H&SW, you know, like it's some graph method or it's a way to partition your space in the scene, you partition it by segments.
And that's kind of like given, right? Because it's designed for inverted index.
But again, on Twitter somewhere, I saw it with from one Lucine commeter who said, maybe this will by itself open up some new opportunities because you'll have a separate vector space index per segment, right? And maybe you can design some features around that.
So it sounds like you still see the potential for merging these technologies in the future and then bringing additional benefit. Well, yes, I can't really speak for Lucine. I haven't taken time to study that implementation. How it was done is I think you know more about it than me.
But I was seeing that eventually relational databases could and might, you know, implement indexes, vector indexes directly. I'm not sure that I can see any technical reason why that wouldn't be possible, basically.
And it could potentially be very, very useful as neural networks, you know, go more and more mainstream for embedding. Yeah, I mean, it sounds like one logical step forward.
Maybe it will not be kind of scalable as a pure vector database, but like on a small like amount of data, let's say when my SQL or Oracle or other databases, they introduce full text search, right? And initially it wasn't there, right? Right.
What restricts you from, you know, introducing another field with embedding and actually running your vector retrieval there? Right. Yeah. And I think it also, it comes down to this that, okay, FICE is always going to give you, you know, the maximum performance.
So, you know, there's going to be some subset of engineering teams that need that performance and that's where they're going to go. What about the mass market, you know, the Fortune 500 companies and things and they're dealing with problems at such a scale where it's not necessary to go there.
And if it's just in the database, even if it's only giving me 80% of the total performance, that's good enough. And in a way, that pragmatic tradeoff is what's underlying Zerae I's existence because people often ask, I can get better performance on my data set.
If I find tune, a bird model and then distilled the bird model is like, yes, that's true. We're aiming to give you a neural network and a full experience that will give you like 80% of the performance that you might be able to achieve, which is still better than you get just from a keyword search.
But the reality is, you know, how many companies have the budget to have NLP engineers and data science and squeeze out that extra performance? It's just not important in a lot of cases. Yeah, exactly.
And do you think that, you know, there is still a need to find a way to combine BM25 or whatever you have there, like the idea of Spark Search with the results from the nearest neighbor search? Like have you been thinking about it?
Have you seen your clients kind of thinking about it or asking about it? There's a very interesting paper from Google about two years ago, Dave Dobson and I'm forgetting the other individuals.
They specifically on this topic, you can obviously model a BM25 search as, you know, multiplication of Spark's matrices. And so you can imagine your vectors essentially having a dense part produced by a neural network for instance, and then a very sparse tail or something.
And you actually want to perform dot products and how do you do it efficiently? And the paper was going into some fascinating techniques for how to do that well. So your question was like, do you see these merging? And I think that, you know, I actually brought this up with the folks at Fires.
Is this something on your roadmap? Is this something you're interested in? They said, no, we're not interested in this. They're specifically focused on either sparse or dense, but not high. And I think that it's going to come down to this.
If the utility of this sparse hybrid can be shown, then the technology is going to follow and try to create efficient implementations of it. I think that there are certainly classes of queries for which BM25 can't be beat.
And the exact keyword matching is going to be the correct way to do it in the future. So then you can take a few different strategies. You can either try to classify the query when it's received and then dispatch it to the correct back end.
Or you can dispatch it to a sparse and a dense index and then merge with a re-ranger. Or you can do this like truly hybrid system where you're simultaneously doing the multiplication on the sparse and the dense pieces and producing a final list in like in one shot, not relying on a re-ranger.
So it's still an open area of research. Exactly. And two things. Like I'm looking at it from the point of view of a customer. Let's say I already have the M25 platform, right? Base platform. And so I'm curious. Okay. So I'm curious to see what vector search can bring me.
And maybe I'm thinking about introducing this as an explorative search feature.
So because I'm not sure if it's going to fly for my documents or for my items in the database, right? So that's one potential to think about, okay, as you said, I can actually route this query to both sparse and dense retrieval. And then maybe combine them in some linear formula, even.
And I can give like a smaller score, lower score to, to, or wait to the dense part and then higher to the sparse part because I still believe in sparse part. And that's how my users are expecting results to be there.
But then maybe I can surface some magic like Q and A, right? So they asked the question and I can give them the answer. And that might be really interesting. And the second point, there was a paper called beer. B E I R. I will make sure that all of the papers will be linked here in the show notes.
But that paper actually compared a dense retrieval versus BM25 on a number of tasks. Right? So you can have a search. You can have a question answering and leaves goes on. And so what they showed is that BM25 is fairly competitive.
It actually is above dense retrieval methods like on zero, zero short retrieval. Right? So like you didn't find you in this model. So you just took them off the shelf. Here is the task. Let's compare. Right? BM25 is very stable. So just few models actually outperformed it.
And so in that sense, it sounds like BM25 is here to stay. What do you think? I agree with you. And again, this is where our scope is as a company is on building an end to end information retrieval pipeline, which means that, okay, today, we have a neural dense retrieval.
Because the M25 has been done, right? It's in the scene. It's well understood how to implement it. Although there are some tricks to actually make the M25 work even better than my off the shelf implementations. But what.
Where we want to eventually get to is we could potentially build the BM25 and dense indexes for our customers. And then return. We're trying to just serve the best results possible. So for instance, you could take even sometimes even very simple heuristics work single word queries.
Often BM25 is how you want to serve them, not not not from a dense index. So if it's a single word query, okay, you're going to be on 25 search. If it's anything longer than one word run, then search. That's not a very principled approach.
I'm just pointing out that, you know, what's going on behind the scenes. That's the intelligence of the platform to provide and we're not really restricted or married to a vector database or only a vector database, powering powering the search of this platform. Yeah, yeah, that makes sense.
So is does that manifest in some way in your product that I as a user can have the flexibility and how my search is processed is going to go the sparse route or is it going to go the the density tree will.
No, we don't so at the moment we're only doing the answer tree will because we feel like that's the interest. We can add that we can add the BM25 parts without a lot of difficulty in six months from now or something like that.
So, but we do provide a few different flavors of the dense retrieval because there's a few. There's question answering so the user puts it or query answering the user puts a query in and then you're trying to find good responses.
There's also another task which is semantic similarity, which is closely related, but it's like I make a statement and I just want to find similar statements so my statement is not necessarily a question that I'm looking for an answer to.
I just want to find semantically similar statements and then the other thing is question question similarity often comes up it comes up usually in the not not in.
Well, you've seen it in Google for instance when you type with query and then it says people also ask these questions and they get these similar questions right.
So there's use cases for question question similarity and so we support all three of those modes of operation and we allow at query time our customers to specify which mode they're trying to run it. Yeah, yeah, that makes sense that makes a lot of sense and of course.
 One thing that I keep thinking about is let's say when we introduce the sparse search let's say Bm 25 and some customer comes in and it's not English language it's something else right then you need to bring in also the tokenization and other things from maybe from Lucene and of course, Lucene is a library in principle it could be wrapped in a Docker image and you can do that job right.
But then the question is can you easily married so that it is production grade between different platforms and languages.
And it's surprising Lucene has come a long way so there's come long in terms of providing a good sense out of defaults out of the box in terms of stop wordless and stemming but I have.
My daughter school started using this like a product that manages communication between the school and the parents and that thing was clearly using.
You know, Lucene or solar elastic search and they didn't have the stemming configured properly and I didn't know as possible to misto misconfigure that so I was searching for vaccine and it couldn't find find it because it was vaccination in the title over there.
So yeah, so with the with the neurosurgeon is kind of a little bit more bullet proof, you know, it's it's a bit more immune to these kinds of mistakes and those misspellings very easily.
Yeah, yeah, especially I think there is also a paper about I think it was from Google you know to train on bite level and so you will not be constrained by okay the complexity of the language because you have like bite level.
Definitions and and so in principle your model should be robust to typos and misspellings and so on and some of them come from speech right so.
Exactly exactly yeah and it sounds like interesting like the example you brought up with your daughter school like system like it sounds like largely search is still broken it's like like the moment you go to some.
 System which is let's say for public use right like it's not necessarily designed for for findability there it exists and you know like like Daniel tanker lung I think he says like the funny part of search industry in general is that when search engine works nobody will go and praise you they just use it when it doesn't work they will blame you so you always air on on that.
How do you feel about that like is this also the potential for your company to go and fix many of these broken use cases.
Well that certainly that certainly actually our vision that we will make it very easy for SAS companies to provide a much more in Google like search experience in their products so when it comes to web say that let's.
Into two categories SAS companies and website owners when it comes to website owners I think the search for websites is really used because.
 And it becomes like a cyclical thing it's really used companies therefore don't invest any money in improving it it's really used because it's not good and basically Google does enough a good enough job actually indexing well sites so site owners have accepted that Google is going to be the front door into their into their website.
 On the other hand I think it's it is obviously dangerous for them to because you've had sites that essentially get obliterated when Google changes you know their quality guidelines and they they drop off the front page and the traffic goes down by 95% suddenly and there's no way to recover from it so it would be good first to be able to provide a good search experience on the websites but I think they don't do it for the cost involved and they don't know how to and certainly.
Algolia and elastic are making that easier particularly algolia but there's still a lot better that it could be made coming to SAS companies there they're talking about data that's private the communications of the school to the parents are not on the web somewhere they can be indexed by Google.
So I feel like what I've noticed in the last few years is that some sort of search feature is present in most of these products now.
 But yes it's usually not tuned maybe not even set up correctly and it doesn't work well and there's a lot of room for improvement so I think these these neural search technologies let you you know really easily improve the quality easily if you've got a set of simple APIs and that's what we provide our APIs basically look like elastic or Algolia's index documents and you never know there's a neural network running.
And the background at all and it's not important just the queries go in and the results come out but these results are far far better than what you would get from a keyword search. So so I think there's a lot of scope particularly for SAS companies for for neural search.
Yeah yeah absolutely I actually wanted to ask you just a question came to my mind I've been reading the book about I think about relevant search it's called by. Doctor and ball and other authors I might be not remembering exactly but this book you know it goes chapter after chapter wait says.
Okay let's just take it from the first principles you have a search to ask you have documents you need to start with like.
 tokenization and by the way if you make a mistake that it will be not findable and then you move one level up and then you start thinking okay what about the model okay TF IDF BM25 what are the trade of Sunson and so they teach you to become a search engineer and then they proceed to ranking and so on so forth and my question is like.
What do you think is going to be the change in the search engine profession going forward once neural search will hit the mass market because when I was the search engineer.
Like I looked at the scene and solar and I I didn't question much I just went and like implemented some changes some parsers some plugins or modified the behavior of some of some algorithm right by extending that class by the way.
 The scene was not it was making a lot of classes final and in Java and so I cannot actually extend them so I had to copy the entire like package and then and then rename all these classes so there is no like namespace clash but that's okay nowhere it's at some point I was worried that I will probably reintroduce the scene all the way in my ID because I had to touch multiple parts.
 But so I felt like I'm in control more or less right not because it's on not not only because it's open source but because I could read the code I could talk to people I could read books I could read blogs and I could experiment myself right and that made me I believe a search engineer in that company even though the company's goal was not to build you know searches service we were building the product.
How do you do happen it thoughts around like how neural search will change the landscape of this job. Well that's a that's an excellent question. Well a few a few thoughts on that topic. Neural search is going to make it.
Easier it's going to require less expertise to put together high quality search experiences and furthermore. The advantage the companies like Google or Microsoft have from click data it's still going to be there but it's going to diminish.
And I think that's actually why maybe I'm biased here and misreading it you see a lot of search engine companies starting up in the last year or two you've got meva. Kagi I think the head of sales force research has started his own engine I've even heard some rumors you don't.
Right right I heard some movie Apple Richard so yeah exactly so to maybe some rumors Apple might be trying to do something like that and it's it's basically because the amount of effort it takes now I think has gone down significantly.
So I think that that's going to be one of the effects of neural. And I also expect it just like you know a losing has been around for a long time I mean maybe the early 2000's 2000.
99 to 9 I think when that cutting started learning Java and as a side product project he decided to implement Lucene and so he started the whole community and then Hadoop followed and so on so far.
Yeah okay because I yeah I remember from a time ago so I think that in the same way there will be an open source. Neural thing it might come under the cover of Lucene or it might be a separate Apache project and and eventually it's going to be the go to solution.
So what companies like mine are doing right now is you know this technology is still pretty new and we're feeling in the gap and we're also providing like a completely hosted solution which has some some value on its own.
But I think longer term that's why I see things headed because you know we're getting into these very good general performance neural networks.
Systems like Bert that can just perform well on a wide range of tasks and then you have like you know t5 and now mt5 and you can go across like 100 different languages as well.
So there will eventually be models that are good enough and someone's going to take the effort to distill them into something that runs well. And and you know anybody in any organization will be able to to download and use it the way to use Lucene today.
I think that's where things will be but it might be it might be five years before we reach that point. Yeah yeah and I mean to take this thought forward from here like like maybe the profession do you think the profession will change in such a way that instead of tweaking.
The index configuration to make your search kind of work better like increase recall and you know not suffer from decreased precision.
You will move more like into okay here is the problem and this of the shelf network doesn't work I have to fine tune it so you become a little bit more like a researcher.
 Yeah so that's an excellent point I think one of the key components in these systems and that we have not built yet in our system but it's in the it's in the blueprints is some kind of a feedback mechanism you'll notice this in Kendra though for instance thumbs up thumbs down on the results for instance where you indicate what's good and what's bad and then even with a small amount of that data you can start to train a re-ranker.
And I think that in the presence of like the volumes of data that you get on an internal application let's say you're going to get a few thousand items of feedback.
Training a re-ranker is probably the most effective thing that you can do that data whether it's a random for a free rank or you take a cross attention on your network and you fine tune it but you can significantly improve the search quality that way.
 So so so I think that the the machinery for doing all of that can also be part of the open source offering because because it's it's very broadly applicable and can be used by basically anyone because like you say this is the problem that that then comes up is like I want to give feedback on this results so the system can improve itself.
Yeah yeah absolutely so you kind of create the flywheel of success right so that you you bring the data back and then the model retrain and so on so forth but there is also there are also like interesting challenges like in your old network like catastrophic forgetting.
Like is this something that you've been thinking maybe back at Google or now with your clients something that kind of you need to keep innovating or solve it some other way.
 Yeah so I am familiar with the concept of catastrophic forgetting I honestly haven't studied it very much in the context of of these large language models like Bert although in general the approach of you know taking a Bert type model and fine tuning seems seems to be working well but but then you're essentially talking about taking after has been fine tuned on one task and then fine tuning for different task and it's going to be a great deal.
Because I do think it's going to get solved because it increases its abilities on the first task. And yeah I guess I don't know how much of an issue that's that's going to be in the context as information retrieval.
 Yeah I mean another thing like if you are familiar with learning to rank for example, which may or may not involve in your own network it may also be based on decision tree like lambda marked for example, you know when you receive a new batch of clicks or downloads or whatever events you have in the system and you retrain that model.
clicks or downloads or whatever events you have in the system and you retain that model, it will also forget what it knew about the previous state, right?
It's very natural and it probably is we can associate it with human life as well in some sense, although they say the older you get, the earlier memories you will actually remember, you might forget what happened yesterday, but you remember what happened like 50 years ago.
But like, yeah, what's probably noticing that with myself. Yeah, me too, actually, because days go by and I'm like, okay, what's going on? But then you go, okay, when I was a kid, I remember something.
But like neural networks are probably a little bit different, or at least the present neural networks. Right.
So I think when you when you retrain the model, like you have to retrain otherwise, it will drift, right? I think Google also has a paper about that, like kind of checking the consistency of your machine learning pipeline and your model.
So it doesn't drift and just explode in the eyes of the front of the eyes of the user, right? So you have to keep retraining it. But but then that also means that it will forget things. Maybe they were quite important. Maybe they are not high probability anymore, but they still are true.
But the network has forgotten about them. Right, right, right. Yeah, then yeah, that makes sense. Yeah. Anyway, it was it was a great talking to you, but I still want to close off.
And before we go to some announcement for you, I'm thinking like I'm asking this question to different to all guests and different guests take it differently. But I really would like to hear your view on that question of why it's a little bit more philosophical.
Like like in a way, like you had a stable job at Google, a lot of challenge, a lot of data, a lot of user impact. Like as you said, like Autorripe Live feature was enabled and to like millions and millions of users.
So then you then you decided to go to to build your startup and that's a nice nice kind of way to experience like another side of things.
But why specifically neural search? What drives you to to work on it? Well, what attracted me to I was initially attracted very much to the idea of automated reasoning. And then of course, that comes if it's current incarnation, it's machine learning. And so I started to learn about that.
And I had this opportunity to work with the Ray Kurzweil who joined Google, I think around 2012. I knew about him. He's a very inspirational figure. And he was specifically working on language understanding because he saw that as being very critical to advancement in artificial intelligence.
So so you know, then beyond that, I would say those are my broad interests. But then I just worked in this area specifically for eight years. And I think I became quite good at what I was doing.
And then also saw that what I was doing post 2017 in particular with this neural network based retrieval had a lot of applicability to products. And you know, I think that being in a research team or research team has a different type of focus.
There's a lot of focus on on publishing papers and things, but not necessarily a lot of interest or appetite for building platform. So in that way, maybe this wasn't really the right place to attempt that kind of work. But to me, I'm an engineer as well. So this is this is very interesting.
And I'm not sure if I'm answering your question, but that's some of my motivation. No, you do. I mean, essentially, I'm currently leading a search team. And yeah, you know, our KPIs is like, okay, how many papers you published, how many patents you can file.
But also when you start thinking, okay, what impact am I making, right? There is not that much room to think about creating, maybe you can create a vision, but you might not necessarily tie it in back to the day-to-day scenarios of users.
You have to be part of engineering, probably, to start delivering these things at which point you are no longer a researcher. So it sounds like you managed to combine both of these engineering and research at ZRI. Yes, yes. It's kind of both of the passions together in one company.
And if we're successful, and we can take it into the future, the research end of the program is something that I'd really like to ramp up a lot. Since we started, honestly, there's been more engineering and less research.
The training, the neural networks was at the early stage of the company, and then we haven't revisited it since then. But I think 2022 is going to be, first of all, it's going to be a big year for this industry.
Beyond Pinecon getting funding, I was recently looking Gina AI, if you're familiar with them. They, I think raised $30 million, it was in TechCrunch. So the industry is starting to get some notice. And for us as well, we expect, we expect to really expand in 2022. Oh, yeah, fantastic.
And I mean, one manager that I worked with used to say that you need to first build the plumbing. And that's your engineering work. Once you have the plumbing, you can stand on it and actually fix some other things, high level.
And that's where you will probably come back to training neural networks and actually nailing that use case for your customers. Sounds really exciting. This was really packed and so much thinking that you brought in. And also some discoveries during this conversation. I really enjoyed it.
I'm just thinking, is there something you would like to announce from your product side, something that our listeners can try? Well, thank you. Thank you for the opportunity.
I think what I would say is that if what we've been talking about is interesting and if someone would like to try it out, then we've created a special promo code. We're currently in a closed beta. So we're accepting customers, but kind of on a case by case basis.
But we've created a promo code for listeners of this podcast. I think I'm going to, I'm sure the exact code with you. And then you can post it in the comments to the video.
But essentially would give, give you a 50 megabyte account, which is much larger than our standard trial account by about a factor of three for one month. If you want to just try out the system that we've been talking about. This is fantastic. Thank you, Amin, for this opportunity.
I'm sure some listeners will take this into use and build some cool vector search applications for their products. That would be great. Yeah, it was a pleasure to talk to you. I hope we can talk at some point down the road as well. And I wish you all the best in the future.
In the next year with your ambition and also with reaching to clients and getting contracts. And all the best to you on that front. It was my pleasure to talk to you and hopefully to see you next year as well. Thank you so much. It was good talking to you too. Thank you, Amin. Bye-bye.