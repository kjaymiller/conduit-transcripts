---
description: '<p>Topics:</p><p>00:00 Introduction</p><p>01:21 Jo Kristian’s background
  in Search / Recommendations since 2001 in Fast Search &amp; Transfer (FAST)</p><p>03:16
  Nice words about Trondheim</p><p>04:37 Role of NTNU in supplying search talent and
  having roots in FAST </p><p>05:33 History of Vespa from keyword search</p><p>09:00
  Architecture of Vespa and programming language choice: C++ (content layer), Java
  (HTTP requests and search plugins) and Python (pyvespa)</p><p>13:45 How Python API
  enables evaluation of the latest ML models with Vespa and ONNX support</p><p>17:04
  Tensor data structure in Vespa and its use cases</p><p>22:23 Multi-stage ranking
  pipeline use cases with Vespa</p><p>24:37 Optimizing your ranker for top 1. Bonus:
  cool search course mentioned!</p><p>30:18 Fascination of Query Understanding, ways
  to implement and its role in search UX</p><p>33:34 You need to have investment to
  get great results in search</p><p>35:30 Game-changing vector search in Vespa and
  impact of MS Marco Passage Ranking</p><p>38:44 User aspect of vector search algorithms</p><p>43:19
  Approximate vs exact nearest neighbor search tradeoffs</p><p>47:58 Misconceptions
  in neural search</p><p>52:06 Ranking competitions, idea generation and BERT bi-encoder
  dream</p><p>56:19 Helping wider community through improving search over CORD-19
  dataset</p><p>58:13 Multimodal search is where vector search shines</p><p>1:01:14
  Power of building fully-fledged demos</p><p>1:04:47 How to combine vector search
  with sparse search: Reciprocal Rank Fusion</p><p>1:10:37 The philosophical WHY question:
  Jo Kristian’s drive in the search field</p><p>1:21:43 Announcement on the coming
  features from Vespa</p><p>- Jo Kristian’s Twitter: <a href="https://twitter.com/jobergum">https://twitter.com/jobergum</a></p><p>-
  Dmitry’s Twitter: <a href="https://twitter.com/DmitryKan">https://twitter.com/DmitryKan</a></p><p>For
  the Show Notes check: <a href="https://www.youtube.com/watch?v=UxEdoXtA9oM">https://www.youtube.com/watch?v=UxEdoXtA9oM</a></p>'
image_url: https://media.rss.com/vector-podcast/20220412_120408_e18078d3137041275301d6bf045caa0e.jpg
pub_date: Tue, 12 Apr 2022 12:29:08 GMT
title: Jo Bergum - Distinguished Engineer, Yahoo! Vespa - Journey of Vespa from Sparse
  into Neural Search
url: https://rss.com/podcasts/vector-podcast/452635
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 22.28, "text": " Everyone,
  Vector Podcast is here. I hope you have been waiting for another episode.", "tokens":
  [50364, 5198, 11, 691, 20814, 29972, 307, 510, 13, 286, 1454, 291, 362, 668, 3806,
  337, 1071, 3500, 13, 51478], "temperature": 0.0, "avg_logprob": -0.4239329383486793,
  "compression_ratio": 1.2727272727272727, "no_speech_prob": 0.14029882848262787},
  {"id": 1, "seek": 0, "start": 22.28, "end": 28.88, "text": " And today I have a
  rock star with me. Joe Christian Bergum, a distinguished engineer", "tokens": [51478,
  400, 965, 286, 362, 257, 3727, 3543, 365, 385, 13, 6807, 5778, 27511, 449, 11, 257,
  21702, 11403, 51808], "temperature": 0.0, "avg_logprob": -0.4239329383486793, "compression_ratio":
  1.2727272727272727, "no_speech_prob": 0.14029882848262787}, {"id": 2, "seek": 2888,
  "start": 28.88, "end": 34.4, "text": " with Yahoo. And he has been super vocal in
  the field of Vector Search. And he has been", "tokens": [50364, 365, 41757, 13,
  400, 415, 575, 668, 1687, 11657, 294, 264, 2519, 295, 691, 20814, 17180, 13, 400,
  415, 575, 668, 50640], "temperature": 0.0, "avg_logprob": -0.27326652125308387,
  "compression_ratio": 1.5799086757990868, "no_speech_prob": 0.36996251344680786},
  {"id": 3, "seek": 2888, "start": 34.4, "end": 39.92, "text": " also advocating for
  one of the famous Vector Search engines and actually like a platform.", "tokens":
  [50640, 611, 32050, 337, 472, 295, 264, 4618, 691, 20814, 17180, 12982, 293, 767,
  411, 257, 3663, 13, 50916], "temperature": 0.0, "avg_logprob": -0.27326652125308387,
  "compression_ratio": 1.5799086757990868, "no_speech_prob": 0.36996251344680786},
  {"id": 4, "seek": 2888, "start": 39.92, "end": 44.8, "text": " Shirley Jo can talk
  more about it called Vespa. Hey Joe, how are you doing?", "tokens": [50916, 43275,
  3139, 393, 751, 544, 466, 309, 1219, 691, 279, 4306, 13, 1911, 6807, 11, 577, 366,
  291, 884, 30, 51160], "temperature": 0.0, "avg_logprob": -0.27326652125308387, "compression_ratio":
  1.5799086757990868, "no_speech_prob": 0.36996251344680786}, {"id": 5, "seek": 2888,
  "start": 46.4, "end": 52.239999999999995, "text": " Hey Dimitri, I''m good, thanks.
  How are you? I''m great. Thank you very much for taking time to", "tokens": [51240,
  1911, 20975, 270, 470, 11, 286, 478, 665, 11, 3231, 13, 1012, 366, 291, 30, 286,
  478, 869, 13, 1044, 291, 588, 709, 337, 1940, 565, 281, 51532], "temperature": 0.0,
  "avg_logprob": -0.27326652125308387, "compression_ratio": 1.5799086757990868, "no_speech_prob":
  0.36996251344680786}, {"id": 6, "seek": 5224, "start": 52.24, "end": 60.400000000000006,
  "text": " talk to me. It''s fantastic being here on your show. It''s become so popular.
  Thank you for that", "tokens": [50364, 751, 281, 385, 13, 467, 311, 5456, 885, 510,
  322, 428, 855, 13, 467, 311, 1813, 370, 3743, 13, 1044, 291, 337, 300, 50772], "temperature":
  0.0, "avg_logprob": -0.1979934310913086, "compression_ratio": 1.6153846153846154,
  "no_speech_prob": 0.0923013761639595}, {"id": 7, "seek": 5224, "start": 60.400000000000006,
  "end": 68.32000000000001, "text": " introduction. I''m not sure if I''m a rock star.
  It''s really interesting to be here. I really", "tokens": [50772, 9339, 13, 286,
  478, 406, 988, 498, 286, 478, 257, 3727, 3543, 13, 467, 311, 534, 1880, 281, 312,
  510, 13, 286, 534, 51168], "temperature": 0.0, "avg_logprob": -0.1979934310913086,
  "compression_ratio": 1.6153846153846154, "no_speech_prob": 0.0923013761639595},
  {"id": 8, "seek": 5224, "start": 68.32000000000001, "end": 74.64, "text": " look
  forward for our conversation on Vector Search and maybe we''ll touch on language
  models as well.", "tokens": [51168, 574, 2128, 337, 527, 3761, 322, 691, 20814,
  17180, 293, 1310, 321, 603, 2557, 322, 2856, 5245, 382, 731, 13, 51484], "temperature":
  0.0, "avg_logprob": -0.1979934310913086, "compression_ratio": 1.6153846153846154,
  "no_speech_prob": 0.0923013761639595}, {"id": 9, "seek": 5224, "start": 74.64, "end":
  80.4, "text": " And they''ll talk a little bit about Vespa and the technology in
  Vespa. I''m really excited.", "tokens": [51484, 400, 436, 603, 751, 257, 707, 857,
  466, 691, 279, 4306, 293, 264, 2899, 294, 691, 279, 4306, 13, 286, 478, 534, 2919,
  13, 51772], "temperature": 0.0, "avg_logprob": -0.1979934310913086, "compression_ratio":
  1.6153846153846154, "no_speech_prob": 0.0923013761639595}, {"id": 10, "seek": 8040,
  "start": 81.04, "end": 86.96000000000001, "text": " Yeah, I''m looking forward to
  that. And I mean, you are a rock star. I can hear you every way on", "tokens": [50396,
  865, 11, 286, 478, 1237, 2128, 281, 300, 13, 400, 286, 914, 11, 291, 366, 257, 3727,
  3543, 13, 286, 393, 1568, 291, 633, 636, 322, 50692], "temperature": 0.0, "avg_logprob":
  -0.16460328249587225, "compression_ratio": 1.58008658008658, "no_speech_prob": 0.12272235006093979},
  {"id": 11, "seek": 8040, "start": 86.96000000000001, "end": 96.24000000000001, "text":
  " Twitter and LinkedIn and blogging. And so what else? So this has been like this.
  And I''m really", "tokens": [50692, 5794, 293, 20657, 293, 6968, 3249, 13, 400,
  370, 437, 1646, 30, 407, 341, 575, 668, 411, 341, 13, 400, 286, 478, 534, 51156],
  "temperature": 0.0, "avg_logprob": -0.16460328249587225, "compression_ratio": 1.58008658008658,
  "no_speech_prob": 0.12272235006093979}, {"id": 12, "seek": 8040, "start": 96.24000000000001,
  "end": 103.60000000000001, "text": " glad to hear to talk to you here today. And
  so as a tradition, could you please introduce yourself", "tokens": [51156, 5404,
  281, 1568, 281, 751, 281, 291, 510, 965, 13, 400, 370, 382, 257, 6994, 11, 727,
  291, 1767, 5366, 1803, 51524], "temperature": 0.0, "avg_logprob": -0.16460328249587225,
  "compression_ratio": 1.58008658008658, "no_speech_prob": 0.12272235006093979}, {"id":
  13, "seek": 8040, "start": 103.60000000000001, "end": 107.28, "text": " however
  you want to know the detail you want and we''ll take it from there?", "tokens":
  [51524, 4461, 291, 528, 281, 458, 264, 2607, 291, 528, 293, 321, 603, 747, 309,
  490, 456, 30, 51708], "temperature": 0.0, "avg_logprob": -0.16460328249587225, "compression_ratio":
  1.58008658008658, "no_speech_prob": 0.12272235006093979}, {"id": 14, "seek": 10728,
  "start": 107.36, "end": 115.68, "text": " Yeah. Yeah, so my name is Joe Christian
  and I work for Yahoo. And I''ve been working for Yahoo''s", "tokens": [50368, 865,
  13, 865, 11, 370, 452, 1315, 307, 6807, 5778, 293, 286, 589, 337, 41757, 13, 400,
  286, 600, 668, 1364, 337, 41757, 311, 50784], "temperature": 0.0, "avg_logprob":
  -0.22470376298234268, "compression_ratio": 1.5078534031413613, "no_speech_prob":
  0.04876043647527695}, {"id": 15, "seek": 10728, "start": 115.68, "end": 124.56,
  "text": " is 2007. My current role in Yahoo is distinguished engineer and I work
  on the Vespa platform.", "tokens": [50784, 307, 12656, 13, 1222, 2190, 3090, 294,
  41757, 307, 21702, 11403, 293, 286, 589, 322, 264, 691, 279, 4306, 3663, 13, 51228],
  "temperature": 0.0, "avg_logprob": -0.22470376298234268, "compression_ratio": 1.5078534031413613,
  "no_speech_prob": 0.04876043647527695}, {"id": 16, "seek": 10728, "start": 125.12,
  "end": 132.88, "text": " And I''ve been working on Search and Recommendations since
  about 2001. When I joined a company here", "tokens": [51256, 400, 286, 600, 668,
  1364, 322, 17180, 293, 49545, 521, 763, 1670, 466, 16382, 13, 1133, 286, 6869, 257,
  2237, 510, 51644], "temperature": 0.0, "avg_logprob": -0.22470376298234268, "compression_ratio":
  1.5078534031413613, "no_speech_prob": 0.04876043647527695}, {"id": 17, "seek": 13288,
  "start": 132.88, "end": 139.04, "text": " as an intern during my studies, a company
  called Fast Search and Transfer, an Norwegian company.", "tokens": [50364, 382,
  364, 2154, 1830, 452, 5313, 11, 257, 2237, 1219, 15968, 17180, 293, 35025, 11, 364,
  34875, 2237, 13, 50672], "temperature": 0.0, "avg_logprob": -0.21663724113913144,
  "compression_ratio": 1.6088888888888888, "no_speech_prob": 0.014461626298725605},
  {"id": 18, "seek": 13288, "start": 140.07999999999998, "end": 144.64, "text": "
  Back then they were doing web search with this web search engine called alldevab.com.",
  "tokens": [50724, 5833, 550, 436, 645, 884, 3670, 3164, 365, 341, 3670, 3164, 2848,
  1219, 439, 40343, 455, 13, 1112, 13, 50952], "temperature": 0.0, "avg_logprob":
  -0.21663724113913144, "compression_ratio": 1.6088888888888888, "no_speech_prob":
  0.014461626298725605}, {"id": 19, "seek": 13288, "start": 145.2, "end": 152.48,
  "text": " So they started around 98 I think trying to compete with Google and so
  on. And then Yahoo came", "tokens": [50980, 407, 436, 1409, 926, 20860, 286, 519,
  1382, 281, 11831, 365, 3329, 293, 370, 322, 13, 400, 550, 41757, 1361, 51344], "temperature":
  0.0, "avg_logprob": -0.21663724113913144, "compression_ratio": 1.6088888888888888,
  "no_speech_prob": 0.014461626298725605}, {"id": 20, "seek": 13288, "start": 152.48,
  "end": 157.68, "text": " along and bought the web search division. The team here
  in Toronto. They also bought", "tokens": [51344, 2051, 293, 4243, 264, 3670, 3164,
  10044, 13, 440, 1469, 510, 294, 14140, 13, 814, 611, 4243, 51604], "temperature":
  0.0, "avg_logprob": -0.21663724113913144, "compression_ratio": 1.6088888888888888,
  "no_speech_prob": 0.014461626298725605}, {"id": 21, "seek": 15768, "start": 158.56,
  "end": 168.96, "text": " all the way star and so on. So that was back in 2003. And
  in 2004, Vespa was born. So and I joined", "tokens": [50408, 439, 264, 636, 3543,
  293, 370, 322, 13, 407, 300, 390, 646, 294, 16416, 13, 400, 294, 15817, 11, 691,
  279, 4306, 390, 4232, 13, 407, 293, 286, 6869, 50928], "temperature": 0.0, "avg_logprob":
  -0.24940004348754882, "compression_ratio": 1.5372340425531914, "no_speech_prob":
  0.007330908440053463}, {"id": 22, "seek": 15768, "start": 170.32, "end": 178.8,
  "text": " I actually worked in Fast in the enterprise search division for some time,
  three years. And then", "tokens": [50996, 286, 767, 2732, 294, 15968, 294, 264,
  14132, 3164, 10044, 337, 512, 565, 11, 1045, 924, 13, 400, 550, 51420], "temperature":
  0.0, "avg_logprob": -0.24940004348754882, "compression_ratio": 1.5372340425531914,
  "no_speech_prob": 0.007330908440053463}, {"id": 23, "seek": 15768, "start": 178.8,
  "end": 186.64000000000001, "text": " I joined Yahoo in 2007. And since then I''m
  been here working on search and Vespa in Yahoo. So", "tokens": [51420, 286, 6869,
  41757, 294, 12656, 13, 400, 1670, 550, 286, 478, 668, 510, 1364, 322, 3164, 293,
  691, 279, 4306, 294, 41757, 13, 407, 51812], "temperature": 0.0, "avg_logprob":
  -0.24940004348754882, "compression_ratio": 1.5372340425531914, "no_speech_prob":
  0.007330908440053463}, {"id": 24, "seek": 18664, "start": 187.27999999999997, "end":
  192.95999999999998, "text": " that''s my background. I also hold a master degree
  in computer science from the Norwegian University", "tokens": [50396, 300, 311,
  452, 3678, 13, 286, 611, 1797, 257, 4505, 4314, 294, 3820, 3497, 490, 264, 34875,
  3535, 50680], "temperature": 0.0, "avg_logprob": -0.23920736208066837, "compression_ratio":
  1.4695652173913043, "no_speech_prob": 0.005616862792521715}, {"id": 25, "seek":
  18664, "start": 192.95999999999998, "end": 198.0, "text": " here in Toronto. Oh
  yeah, that''s great. Actually, by the way, I did visit Toronto Hame.", "tokens":
  [50680, 510, 294, 14140, 13, 876, 1338, 11, 300, 311, 869, 13, 5135, 11, 538, 264,
  636, 11, 286, 630, 3441, 14140, 389, 529, 13, 50932], "temperature": 0.0, "avg_logprob":
  -0.23920736208066837, "compression_ratio": 1.4695652173913043, "no_speech_prob":
  0.005616862792521715}, {"id": 26, "seek": 18664, "start": 198.0, "end": 204.32,
  "text": " Was it 2007 for an interview with one search company? Not fast.", "tokens":
  [50932, 3027, 309, 12656, 337, 364, 4049, 365, 472, 3164, 2237, 30, 1726, 2370,
  13, 51248], "temperature": 0.0, "avg_logprob": -0.23920736208066837, "compression_ratio":
  1.4695652173913043, "no_speech_prob": 0.005616862792521715}, {"id": 27, "seek":
  18664, "start": 206.0, "end": 212.56, "text": " But yeah, it was a great, great
  visit. I mean, I love the city. It''s an amazing place.", "tokens": [51332, 583,
  1338, 11, 309, 390, 257, 869, 11, 869, 3441, 13, 286, 914, 11, 286, 959, 264, 2307,
  13, 467, 311, 364, 2243, 1081, 13, 51660], "temperature": 0.0, "avg_logprob": -0.23920736208066837,
  "compression_ratio": 1.4695652173913043, "no_speech_prob": 0.005616862792521715},
  {"id": 28, "seek": 21256, "start": 213.04, "end": 219.92000000000002, "text": "
  Yeah, it''s an amazing place. And it''s funny what you said about search and", "tokens":
  [50388, 865, 11, 309, 311, 364, 2243, 1081, 13, 400, 309, 311, 4074, 437, 291, 848,
  466, 3164, 293, 50732], "temperature": 0.0, "avg_logprob": -0.257664540234734, "compression_ratio":
  1.4860335195530727, "no_speech_prob": 0.018701262772083282}, {"id": 29, "seek":
  21256, "start": 219.92000000000002, "end": 228.24, "text": " trial because it really
  has a special, maybe special even in Europe because we at one time we had", "tokens":
  [50732, 7308, 570, 309, 534, 575, 257, 2121, 11, 1310, 2121, 754, 294, 3315, 570,
  321, 412, 472, 565, 321, 632, 51148], "temperature": 0.0, "avg_logprob": -0.257664540234734,
  "compression_ratio": 1.4860335195530727, "no_speech_prob": 0.018701262772083282},
  {"id": 30, "seek": 21256, "start": 228.24, "end": 236.32, "text": " both Google,
  Bing and Yahoo here in in in in trial line. So that was a fantastic time. Google",
  "tokens": [51148, 1293, 3329, 11, 30755, 293, 41757, 510, 294, 294, 294, 294, 7308,
  1622, 13, 407, 300, 390, 257, 5456, 565, 13, 3329, 51552], "temperature": 0.0, "avg_logprob":
  -0.257664540234734, "compression_ratio": 1.4860335195530727, "no_speech_prob": 0.018701262772083282},
  {"id": 31, "seek": 23632, "start": 236.95999999999998, "end": 243.51999999999998,
  "text": " shut down their office here in trial line. And but now we have a Microsoft
  is here in", "tokens": [50396, 5309, 760, 641, 3398, 510, 294, 7308, 1622, 13, 400,
  457, 586, 321, 362, 257, 8116, 307, 510, 294, 50724], "temperature": 0.0, "avg_logprob":
  -0.23053432263826068, "compression_ratio": 1.6079295154185023, "no_speech_prob":
  0.013439943082630634}, {"id": 32, "seek": 23632, "start": 243.51999999999998, "end":
  250.32, "text": " in tronheim and also Yahoo as office here in in tronheim. So there''s
  a lot of search technology", "tokens": [50724, 294, 504, 266, 18673, 293, 611, 41757,
  382, 3398, 510, 294, 294, 504, 266, 18673, 13, 407, 456, 311, 257, 688, 295, 3164,
  2899, 51064], "temperature": 0.0, "avg_logprob": -0.23053432263826068, "compression_ratio":
  1.6079295154185023, "no_speech_prob": 0.013439943082630634}, {"id": 33, "seek":
  23632, "start": 250.32, "end": 255.76, "text": " competence here in tronheim. This
  is amazing actually for for relatively small city, but I think", "tokens": [51064,
  39965, 510, 294, 504, 266, 18673, 13, 639, 307, 2243, 767, 337, 337, 7226, 1359,
  2307, 11, 457, 286, 519, 51336], "temperature": 0.0, "avg_logprob": -0.23053432263826068,
  "compression_ratio": 1.6079295154185023, "no_speech_prob": 0.013439943082630634},
  {"id": 34, "seek": 23632, "start": 255.76, "end": 259.84, "text": " Tronheim used
  to be a capital of Norway at some point in back in history. Yeah, in its", "tokens":
  [51336, 1765, 266, 18673, 1143, 281, 312, 257, 4238, 295, 24354, 412, 512, 935,
  294, 646, 294, 2503, 13, 865, 11, 294, 1080, 51540], "temperature": 0.0, "avg_logprob":
  -0.23053432263826068, "compression_ratio": 1.6079295154185023, "no_speech_prob":
  0.013439943082630634}, {"id": 35, "seek": 25984, "start": 259.84, "end": 266.08,
  "text": " on point, back way back in the Viking days. Exactly. So now all these
  Vikings are", "tokens": [50364, 322, 935, 11, 646, 636, 646, 294, 264, 40375, 1708,
  13, 7587, 13, 407, 586, 439, 613, 48761, 366, 50676], "temperature": 0.0, "avg_logprob":
  -0.25572087547995825, "compression_ratio": 1.4979423868312758, "no_speech_prob":
  0.002604901557788253}, {"id": 36, "seek": 25984, "start": 269.52, "end": 276.32,
  "text": " stopped going around with boats and harassing people. Now we developed
  search technology now.", "tokens": [50848, 5936, 516, 926, 365, 17772, 293, 16910,
  278, 561, 13, 823, 321, 4743, 3164, 2899, 586, 13, 51188], "temperature": 0.0, "avg_logprob":
  -0.25572087547995825, "compression_ratio": 1.4979423868312758, "no_speech_prob":
  0.002604901557788253}, {"id": 37, "seek": 25984, "start": 276.32, "end": 284.32,
  "text": " Yeah, such a move. Wow. And I also understood that in tronheim, as you
  said, there is the university.", "tokens": [51188, 865, 11, 1270, 257, 1286, 13,
  3153, 13, 400, 286, 611, 7320, 300, 294, 504, 266, 18673, 11, 382, 291, 848, 11,
  456, 307, 264, 5454, 13, 51588], "temperature": 0.0, "avg_logprob": -0.25572087547995825,
  "compression_ratio": 1.4979423868312758, "no_speech_prob": 0.002604901557788253},
  {"id": 38, "seek": 25984, "start": 284.32, "end": 288.64, "text": " Is it actually
  one of the talent supplies for this industry or engineering in general?", "tokens":
  [51588, 1119, 309, 767, 472, 295, 264, 8301, 11768, 337, 341, 3518, 420, 7043, 294,
  2674, 30, 51804], "temperature": 0.0, "avg_logprob": -0.25572087547995825, "compression_ratio":
  1.4979423868312758, "no_speech_prob": 0.002604901557788253}, {"id": 39, "seek":
  28984, "start": 290.08, "end": 297.76, "text": " Yeah, it is. We have the largest
  technical university in Norway, C and in tronheim. So as an old", "tokens": [50376,
  865, 11, 309, 307, 13, 492, 362, 264, 6443, 6191, 5454, 294, 24354, 11, 383, 293,
  294, 504, 266, 18673, 13, 407, 382, 364, 1331, 50760], "temperature": 0.0, "avg_logprob":
  -0.31427082117053046, "compression_ratio": 1.5105263157894737, "no_speech_prob":
  0.003874805523082614}, {"id": 40, "seek": 28984, "start": 297.76, "end": 306.15999999999997,
  "text": " kind of history and so it''s definitely one of the reasons why the search
  companies evolved.", "tokens": [50760, 733, 295, 2503, 293, 370, 309, 311, 2138,
  472, 295, 264, 4112, 983, 264, 3164, 3431, 14178, 13, 51180], "temperature": 0.0,
  "avg_logprob": -0.31427082117053046, "compression_ratio": 1.5105263157894737, "no_speech_prob":
  0.003874805523082614}, {"id": 41, "seek": 28984, "start": 306.15999999999997, "end":
  313.52, "text": " And the fast search and transfer of the company was founded by
  people coming out of the university", "tokens": [51180, 400, 264, 2370, 3164, 293,
  5003, 295, 264, 2237, 390, 13234, 538, 561, 1348, 484, 295, 264, 5454, 51548], "temperature":
  0.0, "avg_logprob": -0.31427082117053046, "compression_ratio": 1.5105263157894737,
  "no_speech_prob": 0.003874805523082614}, {"id": 42, "seek": 31352, "start": 314.0,
  "end": 319.28, "text": " here. So two point in the east week, very good swing and
  so these two reggae and they they", "tokens": [50388, 510, 13, 407, 732, 935, 294,
  264, 10648, 1243, 11, 588, 665, 11173, 293, 370, 613, 732, 1121, 45534, 293, 436,
  436, 50652], "temperature": 0.0, "avg_logprob": -0.5256483476240557, "compression_ratio":
  1.644736842105263, "no_speech_prob": 0.032441671937704086}, {"id": 43, "seek": 31352,
  "start": 319.28, "end": 324.64, "text": " came they actually started with FTP search
  bucket back in like the night the seven. So and that", "tokens": [50652, 1361, 436,
  767, 1409, 365, 479, 16804, 3164, 13058, 646, 294, 411, 264, 1818, 264, 3407, 13,
  407, 293, 300, 50920], "temperature": 0.0, "avg_logprob": -0.5256483476240557, "compression_ratio":
  1.644736842105263, "no_speech_prob": 0.032441671937704086}, {"id": 44, "seek": 31352,
  "start": 324.64, "end": 331.52, "text": " developed into this web search engine
  and then eventually this became a Westpaw in Yahoo.", "tokens": [50920, 4743, 666,
  341, 3670, 3164, 2848, 293, 550, 4728, 341, 3062, 257, 4055, 79, 1607, 294, 41757,
  13, 51264], "temperature": 0.0, "avg_logprob": -0.5256483476240557, "compression_ratio":
  1.644736842105263, "no_speech_prob": 0.032441671937704086}, {"id": 45, "seek": 31352,
  "start": 332.32, "end": 338.15999999999997, "text": " Oh yeah, yeah, sounds great.
  So I can actually maybe touch on the backgrounds since I''ve mentioned", "tokens":
  [51304, 876, 1338, 11, 1338, 11, 3263, 869, 13, 407, 286, 393, 767, 1310, 2557,
  322, 264, 17336, 1670, 286, 600, 2835, 51596], "temperature": 0.0, "avg_logprob":
  -0.5256483476240557, "compression_ratio": 1.644736842105263, "no_speech_prob": 0.032441671937704086},
  {"id": 46, "seek": 33816, "start": 338.16, "end": 343.52000000000004, "text": "
  now web search and you know how maybe not everybody has heard about Westpaw and
  so Westpaw actually", "tokens": [50364, 586, 3670, 3164, 293, 291, 458, 577, 1310,
  406, 2201, 575, 2198, 466, 4055, 79, 1607, 293, 370, 4055, 79, 1607, 767, 50632],
  "temperature": 0.0, "avg_logprob": -0.15635337220861556, "compression_ratio": 1.6538461538461537,
  "no_speech_prob": 0.008224464021623135}, {"id": 47, "seek": 33816, "start": 344.96000000000004,
  "end": 352.16, "text": " we started developing Westpaw in 2004. So Yahoo said that
  you know we brought you into the company.", "tokens": [50704, 321, 1409, 6416, 4055,
  79, 1607, 294, 15817, 13, 407, 41757, 848, 300, 291, 458, 321, 3038, 291, 666, 264,
  2237, 13, 51064], "temperature": 0.0, "avg_logprob": -0.15635337220861556, "compression_ratio":
  1.6538461538461537, "no_speech_prob": 0.008224464021623135}, {"id": 48, "seek":
  33816, "start": 352.16, "end": 359.12, "text": " We want you to build a vertical
  search platform that we can use across our properties in Yahoo.", "tokens": [51064,
  492, 528, 291, 281, 1322, 257, 9429, 3164, 3663, 300, 321, 393, 764, 2108, 527,
  7221, 294, 41757, 13, 51412], "temperature": 0.0, "avg_logprob": -0.15635337220861556,
  "compression_ratio": 1.6538461538461537, "no_speech_prob": 0.008224464021623135},
  {"id": 49, "seek": 33816, "start": 359.12, "end": 367.28000000000003, "text": "
  So for example, Yahoo finance, Yahoo news, they need to have some kind of search
  engine. So", "tokens": [51412, 407, 337, 1365, 11, 41757, 10719, 11, 41757, 2583,
  11, 436, 643, 281, 362, 512, 733, 295, 3164, 2848, 13, 407, 51820], "temperature":
  0.0, "avg_logprob": -0.15635337220861556, "compression_ratio": 1.6538461538461537,
  "no_speech_prob": 0.008224464021623135}, {"id": 50, "seek": 36728, "start": 367.28,
  "end": 373.59999999999997, "text": " and they gave that task to ask you in trial
  and I''m so they started building Westpaw,", "tokens": [50364, 293, 436, 2729, 300,
  5633, 281, 1029, 291, 294, 7308, 293, 286, 478, 370, 436, 1409, 2390, 4055, 79,
  1607, 11, 50680], "temperature": 0.0, "avg_logprob": -0.21887676643602777, "compression_ratio":
  1.56, "no_speech_prob": 0.0003841678553726524}, {"id": 51, "seek": 36728, "start":
  374.32, "end": 380.23999999999995, "text": " the Westpaw platform using the routes
  and the technology from the web search and putting that", "tokens": [50716, 264,
  4055, 79, 1607, 3663, 1228, 264, 18242, 293, 264, 2899, 490, 264, 3670, 3164, 293,
  3372, 300, 51012], "temperature": 0.0, "avg_logprob": -0.21887676643602777, "compression_ratio":
  1.56, "no_speech_prob": 0.0003841678553726524}, {"id": 52, "seek": 36728, "start":
  380.23999999999995, "end": 391.28, "text": " into a package that the verticals could
  install and use. And then over time this so basically", "tokens": [51012, 666, 257,
  7372, 300, 264, 9429, 82, 727, 3625, 293, 764, 13, 400, 550, 670, 565, 341, 370,
  1936, 51564], "temperature": 0.0, "avg_logprob": -0.21887676643602777, "compression_ratio":
  1.56, "no_speech_prob": 0.0003841678553726524}, {"id": 53, "seek": 39128, "start":
  391.28, "end": 401.35999999999996, "text": " starting with basic BM25 like search
  like keyword search and then gradually Westpaw added more", "tokens": [50364, 2891,
  365, 3875, 15901, 6074, 411, 3164, 411, 20428, 3164, 293, 550, 13145, 4055, 79,
  1607, 3869, 544, 50868], "temperature": 0.0, "avg_logprob": -0.2136540710926056,
  "compression_ratio": 1.4795918367346939, "no_speech_prob": 0.0009724642150104046},
  {"id": 54, "seek": 39128, "start": 401.35999999999996, "end": 410.08, "text": "
  features real time indexing, 10 source aggregations, grouping facets as well. So
  it really developed", "tokens": [50868, 4122, 957, 565, 8186, 278, 11, 1266, 4009,
  16743, 763, 11, 40149, 49752, 382, 731, 13, 407, 309, 534, 4743, 51304], "temperature":
  0.0, "avg_logprob": -0.2136540710926056, "compression_ratio": 1.4795918367346939,
  "no_speech_prob": 0.0009724642150104046}, {"id": 55, "seek": 39128, "start": 411.11999999999995,
  "end": 418.88, "text": " over time and new requirements came in especially when
  we started Westpaw it was around search", "tokens": [51356, 670, 565, 293, 777,
  7728, 1361, 294, 2318, 562, 321, 1409, 4055, 79, 1607, 309, 390, 926, 3164, 51744],
  "temperature": 0.0, "avg_logprob": -0.2136540710926056, "compression_ratio": 1.4795918367346939,
  "no_speech_prob": 0.0009724642150104046}, {"id": 56, "seek": 41888, "start": 419.84,
  "end": 427.76, "text": " but in 2007, 2008 around that time Westpaw''s also started
  to be used more of as a recommendation engine.", "tokens": [50412, 457, 294, 12656,
  11, 10389, 926, 300, 565, 4055, 79, 1607, 311, 611, 1409, 281, 312, 1143, 544, 295,
  382, 257, 11879, 2848, 13, 50808], "temperature": 0.0, "avg_logprob": -0.2582565771566855,
  "compression_ratio": 1.5934065934065933, "no_speech_prob": 0.013602495193481445},
  {"id": 57, "seek": 41888, "start": 427.76, "end": 433.36, "text": " So serving of
  recommendations. So when you go to finance, Yahoo.com and there''s a set of articles",
  "tokens": [50808, 407, 8148, 295, 10434, 13, 407, 562, 291, 352, 281, 10719, 11,
  41757, 13, 1112, 293, 456, 311, 257, 992, 295, 11290, 51088], "temperature": 0.0,
  "avg_logprob": -0.2582565771566855, "compression_ratio": 1.5934065934065933, "no_speech_prob":
  0.013602495193481445}, {"id": 58, "seek": 41888, "start": 434.0, "end": 446.32,
  "text": " that are recommended to you the serving engine doing that is Westpaw.
  And then in 2017,", "tokens": [51120, 300, 366, 9628, 281, 291, 264, 8148, 2848,
  884, 300, 307, 4055, 79, 1607, 13, 400, 550, 294, 6591, 11, 51736], "temperature":
  0.0, "avg_logprob": -0.2582565771566855, "compression_ratio": 1.5934065934065933,
  "no_speech_prob": 0.013602495193481445}, {"id": 59, "seek": 44632, "start": 446.96,
  "end": 454.08, "text": " Yahoo decided that we''re going to open source Westpaw
  to the world. So we open-sourced it using", "tokens": [50396, 41757, 3047, 300,
  321, 434, 516, 281, 1269, 4009, 4055, 79, 1607, 281, 264, 1002, 13, 407, 321, 1269,
  12, 82, 396, 1232, 309, 1228, 50752], "temperature": 0.0, "avg_logprob": -0.1816017598281672,
  "compression_ratio": 1.5706806282722514, "no_speech_prob": 0.010644343681633472},
  {"id": 60, "seek": 44632, "start": 454.08, "end": 463.12, "text": " our Apache tool
  license and we still continue to actively, very actively develop on Westpaw and
  add new", "tokens": [50752, 527, 46597, 2290, 10476, 293, 321, 920, 2354, 281, 13022,
  11, 588, 13022, 1499, 322, 4055, 79, 1607, 293, 909, 777, 51204], "temperature":
  0.0, "avg_logprob": -0.1816017598281672, "compression_ratio": 1.5706806282722514,
  "no_speech_prob": 0.010644343681633472}, {"id": 61, "seek": 44632, "start": 463.12,
  "end": 470.8, "text": " features and so on. So that''s a kind of brief background.
  So Westpaw is not new. It''s really kind of", "tokens": [51204, 4122, 293, 370,
  322, 13, 407, 300, 311, 257, 733, 295, 5353, 3678, 13, 407, 4055, 79, 1607, 307,
  406, 777, 13, 467, 311, 534, 733, 295, 51588], "temperature": 0.0, "avg_logprob":
  -0.1816017598281672, "compression_ratio": 1.5706806282722514, "no_speech_prob":
  0.010644343681633472}, {"id": 62, "seek": 47080, "start": 470.8, "end": 476.56,
  "text": " it has in a very long history and I think that''s also great thing and
  we can talk maybe a little bit", "tokens": [50364, 309, 575, 294, 257, 588, 938,
  2503, 293, 286, 519, 300, 311, 611, 869, 551, 293, 321, 393, 751, 1310, 257, 707,
  857, 50652], "temperature": 0.0, "avg_logprob": -0.1923310226864285, "compression_ratio":
  1.5360824742268042, "no_speech_prob": 0.004410884343087673}, {"id": 63, "seek":
  47080, "start": 476.56, "end": 483.36, "text": " about it because you know we need
  to develop software over time. There are a lot of changes you know", "tokens": [50652,
  466, 309, 570, 291, 458, 321, 643, 281, 1499, 4722, 670, 565, 13, 821, 366, 257,
  688, 295, 2962, 291, 458, 50992], "temperature": 0.0, "avg_logprob": -0.1923310226864285,
  "compression_ratio": 1.5360824742268042, "no_speech_prob": 0.004410884343087673},
  {"id": 64, "seek": 47080, "start": 483.36, "end": 491.84000000000003, "text": "
  in the infrastructure. There was no cloud, public cloud. There were no Kubernetes
  and from 2004.", "tokens": [50992, 294, 264, 6896, 13, 821, 390, 572, 4588, 11,
  1908, 4588, 13, 821, 645, 572, 23145, 293, 490, 15817, 13, 51416], "temperature":
  0.0, "avg_logprob": -0.1923310226864285, "compression_ratio": 1.5360824742268042,
  "no_speech_prob": 0.004410884343087673}, {"id": 65, "seek": 49184, "start": 491.91999999999996,
  "end": 499.91999999999996, "text": " I started in 2007, you know a high power content
  machine, content node machine would have maybe", "tokens": [50368, 286, 1409, 294,
  12656, 11, 291, 458, 257, 1090, 1347, 2701, 3479, 11, 2701, 9984, 3479, 576, 362,
  1310, 50768], "temperature": 0.0, "avg_logprob": -0.22727350286535314, "compression_ratio":
  1.5401069518716577, "no_speech_prob": 0.0069178631529212}, {"id": 66, "seek": 49184,
  "start": 499.91999999999996, "end": 509.03999999999996, "text": " eight things of
  RAM. And it would have maybe maximum 1 gigabit per second network. And if we go",
  "tokens": [50768, 3180, 721, 295, 14561, 13, 400, 309, 576, 362, 1310, 6674, 502,
  8741, 455, 270, 680, 1150, 3209, 13, 400, 498, 321, 352, 51224], "temperature":
  0.0, "avg_logprob": -0.22727350286535314, "compression_ratio": 1.5401069518716577,
  "no_speech_prob": 0.0069178631529212}, {"id": 67, "seek": 49184, "start": 509.03999999999996,
  "end": 516.48, "text": " fast forward, you know, and it will have spinning disks.
  And now we have NVME SSD disks. We have", "tokens": [51224, 2370, 2128, 11, 291,
  458, 11, 293, 309, 486, 362, 15640, 41617, 13, 400, 586, 321, 362, 46512, 15454,
  30262, 41617, 13, 492, 362, 51596], "temperature": 0.0, "avg_logprob": -0.22727350286535314,
  "compression_ratio": 1.5401069518716577, "no_speech_prob": 0.0069178631529212},
  {"id": 68, "seek": 51648, "start": 516.48, "end": 524.64, "text": " nodes with four
  terabytes, potentially of memory, lots of CPU power. So there''s like keeping up",
  "tokens": [50364, 13891, 365, 1451, 1796, 24538, 11, 7263, 295, 4675, 11, 3195,
  295, 13199, 1347, 13, 407, 456, 311, 411, 5145, 493, 50772], "temperature": 0.0,
  "avg_logprob": -0.2013667713512074, "compression_ratio": 1.592274678111588, "no_speech_prob":
  0.007568803150206804}, {"id": 69, "seek": 51648, "start": 525.52, "end": 532.0,
  "text": " in improving the software and adopting it to the hardware and new hardware
  and so on. It''s", "tokens": [50816, 294, 11470, 264, 4722, 293, 32328, 309, 281,
  264, 8837, 293, 777, 8837, 293, 370, 322, 13, 467, 311, 51140], "temperature": 0.0,
  "avg_logprob": -0.2013667713512074, "compression_ratio": 1.592274678111588, "no_speech_prob":
  0.007568803150206804}, {"id": 70, "seek": 51648, "start": 532.0, "end": 537.12,
  "text": " been really fun to watch. I think we did a good job actually making Westpaw
  kind of modern", "tokens": [51140, 668, 534, 1019, 281, 1159, 13, 286, 519, 321,
  630, 257, 665, 1691, 767, 1455, 4055, 79, 1607, 733, 295, 4363, 51396], "temperature":
  0.0, "avg_logprob": -0.2013667713512074, "compression_ratio": 1.592274678111588,
  "no_speech_prob": 0.007568803150206804}, {"id": 71, "seek": 51648, "start": 538.08,
  "end": 544.72, "text": " from something that started in 2004. It turns like really
  an exciting journey and really like", "tokens": [51444, 490, 746, 300, 1409, 294,
  15817, 13, 467, 4523, 411, 534, 364, 4670, 4671, 293, 534, 411, 51776], "temperature":
  0.0, "avg_logprob": -0.2013667713512074, "compression_ratio": 1.592274678111588,
  "no_speech_prob": 0.007568803150206804}, {"id": 72, "seek": 54472, "start": 544.72,
  "end": 550.88, "text": " starting from when you would explain like you know small
  scale servers in the way all the way.", "tokens": [50364, 2891, 490, 562, 291, 576,
  2903, 411, 291, 458, 1359, 4373, 15909, 294, 264, 636, 439, 264, 636, 13, 50672],
  "temperature": 0.0, "avg_logprob": -0.26578508723865857, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.004526263102889061}, {"id": 73, "seek": 54472, "start": 550.88,
  "end": 556.08, "text": " And the technology has changed so much right? The disks
  became faster I guess and you know", "tokens": [50672, 400, 264, 2899, 575, 3105,
  370, 709, 558, 30, 440, 41617, 3062, 4663, 286, 2041, 293, 291, 458, 50932], "temperature":
  0.0, "avg_logprob": -0.26578508723865857, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.004526263102889061}, {"id": 74, "seek": 54472, "start": 556.64,
  "end": 562.0, "text": " the network has become faster. And like I remember like
  in Silicon Valley, Citco, if you", "tokens": [50960, 264, 3209, 575, 1813, 4663,
  13, 400, 411, 286, 1604, 411, 294, 25351, 10666, 11, 18435, 1291, 11, 498, 291,
  51228], "temperature": 0.0, "avg_logprob": -0.26578508723865857, "compression_ratio":
  1.608695652173913, "no_speech_prob": 0.004526263102889061}, {"id": 75, "seek": 54472,
  "start": 562.0, "end": 567.76, "text": " if you watched it, it like they had a case
  when they optimized one module in the system and the", "tokens": [51228, 498, 291,
  6337, 309, 11, 309, 411, 436, 632, 257, 1389, 562, 436, 26941, 472, 10088, 294,
  264, 1185, 293, 264, 51516], "temperature": 0.0, "avg_logprob": -0.26578508723865857,
  "compression_ratio": 1.608695652173913, "no_speech_prob": 0.004526263102889061},
  {"id": 76, "seek": 56776, "start": 567.76, "end": 575.4399999999999, "text": " whole
  system went down because it''s way too fast. So it''s like it sounds like you have
  done quite", "tokens": [50364, 1379, 1185, 1437, 760, 570, 309, 311, 636, 886, 2370,
  13, 407, 309, 311, 411, 309, 3263, 411, 291, 362, 1096, 1596, 50748], "temperature":
  0.0, "avg_logprob": -0.2155465690457091, "compression_ratio": 1.5951417004048583,
  "no_speech_prob": 0.00247886567376554}, {"id": 77, "seek": 56776, "start": 575.4399999999999,
  "end": 581.36, "text": " a bit of job to actually keep this shape of flow. And like
  if I understood correctly, technically", "tokens": [50748, 257, 857, 295, 1691,
  281, 767, 1066, 341, 3909, 295, 3095, 13, 400, 411, 498, 286, 7320, 8944, 11, 12120,
  51044], "temperature": 0.0, "avg_logprob": -0.2155465690457091, "compression_ratio":
  1.5951417004048583, "no_speech_prob": 0.00247886567376554}, {"id": 78, "seek": 56776,
  "start": 581.36, "end": 588.88, "text": " speaking, Westpaw or portion of Westpaw
  is implemented in Java. And then portion in C or C++ and then", "tokens": [51044,
  4124, 11, 4055, 79, 1607, 420, 8044, 295, 4055, 79, 1607, 307, 12270, 294, 10745,
  13, 400, 550, 8044, 294, 383, 420, 383, 25472, 293, 550, 51420], "temperature":
  0.0, "avg_logprob": -0.2155465690457091, "compression_ratio": 1.5951417004048583,
  "no_speech_prob": 0.00247886567376554}, {"id": 79, "seek": 56776, "start": 588.88,
  "end": 595.92, "text": " you also have some Python. And maybe you can talk more
  about the choice of languages and sort of", "tokens": [51420, 291, 611, 362, 512,
  15329, 13, 400, 1310, 291, 393, 751, 544, 466, 264, 3922, 295, 8650, 293, 1333,
  295, 51772], "temperature": 0.0, "avg_logprob": -0.2155465690457091, "compression_ratio":
  1.5951417004048583, "no_speech_prob": 0.00247886567376554}, {"id": 80, "seek": 59592,
  "start": 596.24, "end": 601.76, "text": " culture that there isn''t the team. But
  I''m also curious like around the same time. I''ve actually", "tokens": [50380,
  3713, 300, 456, 1943, 380, 264, 1469, 13, 583, 286, 478, 611, 6369, 411, 926, 264,
  912, 565, 13, 286, 600, 767, 50656], "temperature": 0.0, "avg_logprob": -0.1531265613644622,
  "compression_ratio": 1.5663716814159292, "no_speech_prob": 0.0023909492883831263},
  {"id": 81, "seek": 59592, "start": 601.76, "end": 609.4399999999999, "text": " seen
  was also developing right quite quite fast. Did you kind of look at what that team
  is doing", "tokens": [50656, 1612, 390, 611, 6416, 558, 1596, 1596, 2370, 13, 2589,
  291, 733, 295, 574, 412, 437, 300, 1469, 307, 884, 51040], "temperature": 0.0, "avg_logprob":
  -0.1531265613644622, "compression_ratio": 1.5663716814159292, "no_speech_prob":
  0.0023909492883831263}, {"id": 82, "seek": 59592, "start": 610.24, "end": 613.92,
  "text": " which is like an open source project? Was there something to loan from?",
  "tokens": [51080, 597, 307, 411, 364, 1269, 4009, 1716, 30, 3027, 456, 746, 281,
  10529, 490, 30, 51264], "temperature": 0.0, "avg_logprob": -0.1531265613644622,
  "compression_ratio": 1.5663716814159292, "no_speech_prob": 0.0023909492883831263},
  {"id": 83, "seek": 59592, "start": 618.4799999999999, "end": 623.4399999999999,
  "text": " Yeah, so let me tackle the first questions around Westpaw and the kind
  of languages that", "tokens": [51492, 865, 11, 370, 718, 385, 14896, 264, 700, 1651,
  926, 4055, 79, 1607, 293, 264, 733, 295, 8650, 300, 51740], "temperature": 0.0,
  "avg_logprob": -0.1531265613644622, "compression_ratio": 1.5663716814159292, "no_speech_prob":
  0.0023909492883831263}, {"id": 84, "seek": 62344, "start": 623.44, "end": 631.12,
  "text": " be used. And there''s a lot of things here to cover. So Westpaw is around
  1.7 million", "tokens": [50364, 312, 1143, 13, 400, 456, 311, 257, 688, 295, 721,
  510, 281, 2060, 13, 407, 4055, 79, 1607, 307, 926, 502, 13, 22, 2459, 50748], "temperature":
  0.0, "avg_logprob": -0.14532268478209714, "compression_ratio": 1.5108695652173914,
  "no_speech_prob": 0.0014025408308953047}, {"id": 85, "seek": 62344, "start": 631.12,
  "end": 639.6800000000001, "text": " lines of code, the total Westpaw platform. And
  it''s a roughly 50% is written in Java. And 50%", "tokens": [50748, 3876, 295, 3089,
  11, 264, 3217, 4055, 79, 1607, 3663, 13, 400, 309, 311, 257, 9810, 2625, 4, 307,
  3720, 294, 10745, 13, 400, 2625, 4, 51176], "temperature": 0.0, "avg_logprob": -0.14532268478209714,
  "compression_ratio": 1.5108695652173914, "no_speech_prob": 0.0014025408308953047},
  {"id": 86, "seek": 62344, "start": 639.6800000000001, "end": 647.2, "text": " is
  written in C++. And why do we use two different languages and what are the trade-offs?
  So in the", "tokens": [51176, 307, 3720, 294, 383, 25472, 13, 400, 983, 360, 321,
  764, 732, 819, 8650, 293, 437, 366, 264, 4923, 12, 19231, 30, 407, 294, 264, 51552],
  "temperature": 0.0, "avg_logprob": -0.14532268478209714, "compression_ratio": 1.5108695652173914,
  "no_speech_prob": 0.0014025408308953047}, {"id": 87, "seek": 64720, "start": 647.2,
  "end": 654.0, "text": " Westpaw architecture, we made a clear distinction between
  what we call the cluster that holds the", "tokens": [50364, 4055, 79, 1607, 9482,
  11, 321, 1027, 257, 1850, 16844, 1296, 437, 321, 818, 264, 13630, 300, 9190, 264,
  50704], "temperature": 0.0, "avg_logprob": -0.09892934976622116, "compression_ratio":
  1.6860986547085202, "no_speech_prob": 0.0003257182252127677}, {"id": 88, "seek":
  64720, "start": 654.0, "end": 661.2800000000001, "text": " content where you actually
  index and invert the documents and you have all the data structures for", "tokens":
  [50704, 2701, 689, 291, 767, 8186, 293, 33966, 264, 8512, 293, 291, 362, 439, 264,
  1412, 9227, 337, 51068], "temperature": 0.0, "avg_logprob": -0.09892934976622116,
  "compression_ratio": 1.6860986547085202, "no_speech_prob": 0.0003257182252127677},
  {"id": 89, "seek": 64720, "start": 661.2800000000001, "end": 666.08, "text": " fast
  searching in these data structures. The content layer is written in C++ because
  you''re", "tokens": [51068, 2370, 10808, 294, 613, 1412, 9227, 13, 440, 2701, 4583,
  307, 3720, 294, 383, 25472, 570, 291, 434, 51308], "temperature": 0.0, "avg_logprob":
  -0.09892934976622116, "compression_ratio": 1.6860986547085202, "no_speech_prob":
  0.0003257182252127677}, {"id": 90, "seek": 64720, "start": 666.08, "end": 672.32,
  "text": " managing a lot of data. You have the data that you need to have in memory
  and so on. So", "tokens": [51308, 11642, 257, 688, 295, 1412, 13, 509, 362, 264,
  1412, 300, 291, 643, 281, 362, 294, 4675, 293, 370, 322, 13, 407, 51620], "temperature":
  0.0, "avg_logprob": -0.09892934976622116, "compression_ratio": 1.6860986547085202,
  "no_speech_prob": 0.0003257182252127677}, {"id": 91, "seek": 67232, "start": 672.96,
  "end": 680.96, "text": " and it needs to be fairly efficient. And then on there
  what we call the stateless layer is the", "tokens": [50396, 293, 309, 2203, 281,
  312, 6457, 7148, 13, 400, 550, 322, 456, 437, 321, 818, 264, 2219, 4272, 4583, 307,
  264, 50796], "temperature": 0.0, "avg_logprob": -0.22794599533081056, "compression_ratio":
  1.5483870967741935, "no_speech_prob": 0.0021192936692386866}, {"id": 92, "seek":
  67232, "start": 680.96, "end": 688.96, "text": " layer that actually interacts with
  user requests. So user requests comes in. It''s accepted by", "tokens": [50796,
  4583, 300, 767, 43582, 365, 4195, 12475, 13, 407, 4195, 12475, 1487, 294, 13, 467,
  311, 9035, 538, 51196], "temperature": 0.0, "avg_logprob": -0.22794599533081056,
  "compression_ratio": 1.5483870967741935, "no_speech_prob": 0.0021192936692386866},
  {"id": 93, "seek": 67232, "start": 688.96, "end": 696.5600000000001, "text": " HSP
  server and there you do and that layer is written in Java. So you can also then
  deploy plugins.", "tokens": [51196, 389, 27921, 7154, 293, 456, 291, 360, 293, 300,
  4583, 307, 3720, 294, 10745, 13, 407, 291, 393, 611, 550, 7274, 33759, 13, 51576],
  "temperature": 0.0, "avg_logprob": -0.22794599533081056, "compression_ratio": 1.5483870967741935,
  "no_speech_prob": 0.0021192936692386866}, {"id": 94, "seek": 69656, "start": 696.64,
  "end": 702.4, "text": " You can write your own searcher functions that can dispatch
  the query and get a reply. And you", "tokens": [50368, 509, 393, 2464, 428, 1065,
  3164, 260, 6828, 300, 393, 36729, 264, 14581, 293, 483, 257, 16972, 13, 400, 291,
  50656], "temperature": 0.0, "avg_logprob": -0.1156198952787666, "compression_ratio":
  1.6478260869565218, "no_speech_prob": 0.002656460739672184}, {"id": 95, "seek":
  69656, "start": 702.4, "end": 708.3199999999999, "text": " don''t. It''s transparent
  from a given searcher if you have a 100 node cluster or if you have a", "tokens":
  [50656, 500, 380, 13, 467, 311, 12737, 490, 257, 2212, 3164, 260, 498, 291, 362,
  257, 2319, 9984, 13630, 420, 498, 291, 362, 257, 50952], "temperature": 0.0, "avg_logprob":
  -0.1156198952787666, "compression_ratio": 1.6478260869565218, "no_speech_prob":
  0.002656460739672184}, {"id": 96, "seek": 69656, "start": 708.3199999999999, "end":
  715.3599999999999, "text": " single node cluster. So that''s kind of hidden away
  when you deploy a plugin. So those languages", "tokens": [50952, 2167, 9984, 13630,
  13, 407, 300, 311, 733, 295, 7633, 1314, 562, 291, 7274, 257, 23407, 13, 407, 729,
  8650, 51304], "temperature": 0.0, "avg_logprob": -0.1156198952787666, "compression_ratio":
  1.6478260869565218, "no_speech_prob": 0.002656460739672184}, {"id": 97, "seek":
  69656, "start": 715.3599999999999, "end": 720.9599999999999, "text": " have different
  trade-offs. So it''s a lot easier for people to write plugins using Java without",
  "tokens": [51304, 362, 819, 4923, 12, 19231, 13, 407, 309, 311, 257, 688, 3571,
  337, 561, 281, 2464, 33759, 1228, 10745, 1553, 51584], "temperature": 0.0, "avg_logprob":
  -0.1156198952787666, "compression_ratio": 1.6478260869565218, "no_speech_prob":
  0.002656460739672184}, {"id": 98, "seek": 72096, "start": 721.0400000000001, "end":
  728.32, "text": " shooting themselves in the foot using C++. So in the content layer
  in C++ we don''t allow any kind", "tokens": [50368, 5942, 2969, 294, 264, 2671,
  1228, 383, 25472, 13, 407, 294, 264, 2701, 4583, 294, 383, 25472, 321, 500, 380,
  2089, 604, 733, 50732], "temperature": 0.0, "avg_logprob": -0.22338106099841665,
  "compression_ratio": 1.706140350877193, "no_speech_prob": 0.0014847111888229847},
  {"id": 99, "seek": 72096, "start": 728.32, "end": 733.0400000000001, "text": " of
  plugins. You can contribute or you can contribute to the open source but then it
  needs to be", "tokens": [50732, 295, 33759, 13, 509, 393, 10586, 420, 291, 393,
  10586, 281, 264, 1269, 4009, 457, 550, 309, 2203, 281, 312, 50968], "temperature":
  0.0, "avg_logprob": -0.22338106099841665, "compression_ratio": 1.706140350877193,
  "no_speech_prob": 0.0014847111888229847}, {"id": 100, "seek": 72096, "start": 733.0400000000001,
  "end": 738.4000000000001, "text": " a kind of feature. We don''t allow you to embed
  a library or something into the content layer.", "tokens": [50968, 257, 733, 295,
  4111, 13, 492, 500, 380, 2089, 291, 281, 12240, 257, 6405, 420, 746, 666, 264, 2701,
  4583, 13, 51236], "temperature": 0.0, "avg_logprob": -0.22338106099841665, "compression_ratio":
  1.706140350877193, "no_speech_prob": 0.0014847111888229847}, {"id": 101, "seek":
  72096, "start": 739.12, "end": 744.72, "text": " So that''s a trade-off. So then
  you mentioned Python. We have a Python, what we call pi-wespa which is", "tokens":
  [51272, 407, 300, 311, 257, 4923, 12, 4506, 13, 407, 550, 291, 2835, 15329, 13,
  492, 362, 257, 15329, 11, 437, 321, 818, 3895, 12, 86, 279, 4306, 597, 307, 51552],
  "temperature": 0.0, "avg_logprob": -0.22338106099841665, "compression_ratio": 1.706140350877193,
  "no_speech_prob": 0.0014847111888229847}, {"id": 102, "seek": 74472, "start": 745.44,
  "end": 753.84, "text": " language binding on top of the HDP API. So it''s not of
  the core kind of westpides. It''s an API where we built", "tokens": [50400, 2856,
  17359, 322, 1192, 295, 264, 389, 11373, 9362, 13, 407, 309, 311, 406, 295, 264,
  4965, 733, 295, 7009, 79, 1875, 13, 467, 311, 364, 9362, 689, 321, 3094, 50820],
  "temperature": 0.0, "avg_logprob": -0.34311512154592594, "compression_ratio": 1.5181347150259068,
  "no_speech_prob": 0.004754857160151005}, {"id": 103, "seek": 74472, "start": 755.84,
  "end": 762.32, "text": " around interacting with westpa, doing model evaluation
  and evaluating for example different", "tokens": [50920, 926, 18017, 365, 7009,
  4306, 11, 884, 2316, 13344, 293, 27479, 337, 1365, 819, 51244], "temperature": 0.0,
  "avg_logprob": -0.34311512154592594, "compression_ratio": 1.5181347150259068, "no_speech_prob":
  0.004754857160151005}, {"id": 104, "seek": 74472, "start": 762.32, "end": 768.8000000000001,
  "text": " retrieval and writing strategies. So that''s the kind of language. And
  regarding your scene,", "tokens": [51244, 19817, 3337, 293, 3579, 9029, 13, 407,
  300, 311, 264, 733, 295, 2856, 13, 400, 8595, 428, 4145, 11, 51568], "temperature":
  0.0, "avg_logprob": -0.34311512154592594, "compression_ratio": 1.5181347150259068,
  "no_speech_prob": 0.004754857160151005}, {"id": 105, "seek": 76880, "start": 768.8,
  "end": 775.12, "text": " Apache Lucene. So if I recall correctly, I think Apache
  Lucene started in 1998. So around", "tokens": [50364, 46597, 9593, 1450, 13, 407,
  498, 286, 9901, 8944, 11, 286, 519, 46597, 9593, 1450, 1409, 294, 21404, 13, 407,
  926, 50680], "temperature": 0.0, "avg_logprob": -0.23998415093672903, "compression_ratio":
  1.5836909871244635, "no_speech_prob": 0.004530901554971933}, {"id": 106, "seek":
  76880, "start": 775.12, "end": 782.8, "text": " time. So there''s a lot of inspiration
  of course and it''s not that many ways you can build", "tokens": [50680, 565, 13,
  407, 456, 311, 257, 688, 295, 10249, 295, 1164, 293, 309, 311, 406, 300, 867, 2098,
  291, 393, 1322, 51064], "temperature": 0.0, "avg_logprob": -0.23998415093672903,
  "compression_ratio": 1.5836909871244635, "no_speech_prob": 0.004530901554971933},
  {"id": 107, "seek": 76880, "start": 782.8, "end": 790.3199999999999, "text": " a
  search engine. So I''m losing pretty much, it''s a really good library. So yeah,
  definitely we look", "tokens": [51064, 257, 3164, 2848, 13, 407, 286, 478, 7027,
  1238, 709, 11, 309, 311, 257, 534, 665, 6405, 13, 407, 1338, 11, 2138, 321, 574,
  51440], "temperature": 0.0, "avg_logprob": -0.23998415093672903, "compression_ratio":
  1.5836909871244635, "no_speech_prob": 0.004530901554971933}, {"id": 108, "seek":
  76880, "start": 790.3199999999999, "end": 796.3199999999999, "text": " at what''s
  happening in open source and they have a lot of admiration for the work and the",
  "tokens": [51440, 412, 437, 311, 2737, 294, 1269, 4009, 293, 436, 362, 257, 688,
  295, 44597, 337, 264, 589, 293, 264, 51740], "temperature": 0.0, "avg_logprob":
  -0.23998415093672903, "compression_ratio": 1.5836909871244635, "no_speech_prob":
  0.004530901554971933}, {"id": 109, "seek": 79632, "start": 796.32, "end": 801.6,
  "text": " committers of Apache Lucene. I mean, it''s a great job that they''ve done
  and they''ll be able to", "tokens": [50364, 5599, 1559, 295, 46597, 9593, 1450,
  13, 286, 914, 11, 309, 311, 257, 869, 1691, 300, 436, 600, 1096, 293, 436, 603,
  312, 1075, 281, 50628], "temperature": 0.0, "avg_logprob": -0.24683005923316592,
  "compression_ratio": 1.63135593220339, "no_speech_prob": 0.000335570250172168},
  {"id": 110, "seek": 79632, "start": 801.6, "end": 809.6, "text": " develop this
  over 20 years. And the core difference is between westpun, Apache Lucene is that
  westpun", "tokens": [50628, 1499, 341, 670, 945, 924, 13, 400, 264, 4965, 2649,
  307, 1296, 7009, 79, 409, 11, 46597, 9593, 1450, 307, 300, 7009, 79, 409, 51028],
  "temperature": 0.0, "avg_logprob": -0.24683005923316592, "compression_ratio": 1.63135593220339,
  "no_speech_prob": 0.000335570250172168}, {"id": 111, "seek": 79632, "start": 809.6,
  "end": 814.1600000000001, "text": " is a full kind of engine. So it becomes more
  of like comparing westpun with elastic search or", "tokens": [51028, 307, 257, 1577,
  733, 295, 2848, 13, 407, 309, 3643, 544, 295, 411, 15763, 7009, 79, 409, 365, 17115,
  3164, 420, 51256], "temperature": 0.0, "avg_logprob": -0.24683005923316592, "compression_ratio":
  1.63135593220339, "no_speech_prob": 0.000335570250172168}, {"id": 112, "seek": 79632,
  "start": 814.1600000000001, "end": 821.2, "text": " Apache Zoolar, which is kind
  of an engine on top. So there''s no like westpun library which you", "tokens": [51256,
  46597, 1176, 1092, 289, 11, 597, 307, 733, 295, 364, 2848, 322, 1192, 13, 407, 456,
  311, 572, 411, 7009, 79, 409, 6405, 597, 291, 51608], "temperature": 0.0, "avg_logprob":
  -0.24683005923316592, "compression_ratio": 1.63135593220339, "no_speech_prob": 0.000335570250172168},
  {"id": 113, "seek": 82120, "start": 821.2, "end": 825.76, "text": " can use. You
  have to kind of buy the whole, you have to buy the whole platform.", "tokens": [50364,
  393, 764, 13, 509, 362, 281, 733, 295, 2256, 264, 1379, 11, 291, 362, 281, 2256,
  264, 1379, 3663, 13, 50592], "temperature": 0.0, "avg_logprob": -0.14024956737245833,
  "compression_ratio": 1.7388059701492538, "no_speech_prob": 0.0014419262297451496},
  {"id": 114, "seek": 82120, "start": 826.72, "end": 831.84, "text": " Yes, basically
  like a web server around it and all the components like the nodes and overseer",
  "tokens": [50640, 1079, 11, 1936, 411, 257, 3670, 7154, 926, 309, 293, 439, 264,
  6677, 411, 264, 13891, 293, 11916, 260, 50896], "temperature": 0.0, "avg_logprob":
  -0.14024956737245833, "compression_ratio": 1.7388059701492538, "no_speech_prob":
  0.0014419262297451496}, {"id": 115, "seek": 82120, "start": 831.84, "end": 836.72,
  "text": " and other architectural elements. Yeah, for sure. And on the Python side,
  I''m also curious like", "tokens": [50896, 293, 661, 26621, 4959, 13, 865, 11, 337,
  988, 13, 400, 322, 264, 15329, 1252, 11, 286, 478, 611, 6369, 411, 51140], "temperature":
  0.0, "avg_logprob": -0.14024956737245833, "compression_ratio": 1.7388059701492538,
  "no_speech_prob": 0.0014419262297451496}, {"id": 116, "seek": 82120, "start": 836.72,
  "end": 841.76, "text": " with all the development of models and you know, hugging
  face and you can pretty much find a paper", "tokens": [51140, 365, 439, 264, 3250,
  295, 5245, 293, 291, 458, 11, 41706, 1851, 293, 291, 393, 1238, 709, 915, 257, 3035,
  51392], "temperature": 0.0, "avg_logprob": -0.14024956737245833, "compression_ratio":
  1.7388059701492538, "no_speech_prob": 0.0014419262297451496}, {"id": 117, "seek":
  82120, "start": 841.76, "end": 848.1600000000001, "text": " and then most likely
  there is a model already available in some shape and form. And so the Python", "tokens":
  [51392, 293, 550, 881, 3700, 456, 307, 257, 2316, 1217, 2435, 294, 512, 3909, 293,
  1254, 13, 400, 370, 264, 15329, 51712], "temperature": 0.0, "avg_logprob": -0.14024956737245833,
  "compression_ratio": 1.7388059701492538, "no_speech_prob": 0.0014419262297451496},
  {"id": 118, "seek": 84816, "start": 848.24, "end": 854.24, "text": " layer in westpun
  does it help you know newcomers to kind of easier experiment with these models in",
  "tokens": [50368, 4583, 294, 7009, 79, 409, 775, 309, 854, 291, 458, 40014, 433,
  281, 733, 295, 3571, 5120, 365, 613, 5245, 294, 50668], "temperature": 0.0, "avg_logprob":
  -0.20577346400210733, "compression_ratio": 1.5793991416309012, "no_speech_prob":
  0.0011269384995102882}, {"id": 119, "seek": 84816, "start": 854.24, "end": 862.9599999999999,
  "text": " conjunction with westpun? We do hope so. And that was one of the goals
  for making py westpun.", "tokens": [50668, 27482, 365, 7009, 79, 409, 30, 492, 360,
  1454, 370, 13, 400, 300, 390, 472, 295, 264, 5493, 337, 1455, 10664, 7009, 79, 409,
  13, 51104], "temperature": 0.0, "avg_logprob": -0.20577346400210733, "compression_ratio":
  1.5793991416309012, "no_speech_prob": 0.0011269384995102882}, {"id": 120, "seek":
  84816, "start": 862.9599999999999, "end": 868.64, "text": " So there are different
  kind of use cases where you if you have like a more of a low", "tokens": [51104,
  407, 456, 366, 819, 733, 295, 764, 3331, 689, 291, 498, 291, 362, 411, 257, 544,
  295, 257, 2295, 51388], "temperature": 0.0, "avg_logprob": -0.20577346400210733,
  "compression_ratio": 1.5793991416309012, "no_speech_prob": 0.0011269384995102882},
  {"id": 121, "seek": 84816, "start": 868.64, "end": 874.0799999999999, "text": "
  query volume, maybe you have 200,000 documents or something like that, you know,
  not really", "tokens": [51388, 14581, 5523, 11, 1310, 291, 362, 2331, 11, 1360,
  8512, 420, 746, 411, 300, 11, 291, 458, 11, 406, 534, 51660], "temperature": 0.0,
  "avg_logprob": -0.20577346400210733, "compression_ratio": 1.5793991416309012, "no_speech_prob":
  0.0011269384995102882}, {"id": 122, "seek": 87408, "start": 874.32, "end": 881.2800000000001,
  "text": " not really very low latency and so on. Then you can use Python and do
  embeddings and you can play", "tokens": [50376, 406, 534, 588, 2295, 27043, 293,
  370, 322, 13, 1396, 291, 393, 764, 15329, 293, 360, 12240, 29432, 293, 291, 393,
  862, 50724], "temperature": 0.0, "avg_logprob": -0.16675648790724734, "compression_ratio":
  1.6462882096069869, "no_speech_prob": 0.0017631014343351126}, {"id": 123, "seek":
  87408, "start": 881.2800000000001, "end": 886.32, "text": " then it natively works
  with hugging face and all those libraries that are typically written in", "tokens":
  [50724, 550, 309, 8470, 356, 1985, 365, 41706, 1851, 293, 439, 729, 15148, 300,
  366, 5850, 3720, 294, 50976], "temperature": 0.0, "avg_logprob": -0.16675648790724734,
  "compression_ratio": 1.6462882096069869, "no_speech_prob": 0.0017631014343351126},
  {"id": 124, "seek": 87408, "start": 886.32, "end": 893.84, "text": " Python. And
  then you can use westpun, just purely HTTP based APIs and so on. The other option,",
  "tokens": [50976, 15329, 13, 400, 550, 291, 393, 764, 7009, 79, 409, 11, 445, 17491,
  33283, 2361, 21445, 293, 370, 322, 13, 440, 661, 3614, 11, 51352], "temperature":
  0.0, "avg_logprob": -0.16675648790724734, "compression_ratio": 1.6462882096069869,
  "no_speech_prob": 0.0017631014343351126}, {"id": 125, "seek": 87408, "start": 893.84,
  "end": 899.36, "text": " which is more involved, I have to say, and that is that
  you can take a transformer model,", "tokens": [51352, 597, 307, 544, 3288, 11, 286,
  362, 281, 584, 11, 293, 300, 307, 300, 291, 393, 747, 257, 31782, 2316, 11, 51628],
  "temperature": 0.0, "avg_logprob": -0.16675648790724734, "compression_ratio": 1.6462882096069869,
  "no_speech_prob": 0.0017631014343351126}, {"id": 126, "seek": 89936, "start": 899.44,
  "end": 907.2, "text": " for example, and export it to one X format or on X, which
  is open neural network exchange format.", "tokens": [50368, 337, 1365, 11, 293,
  10725, 309, 281, 472, 1783, 7877, 420, 322, 1783, 11, 597, 307, 1269, 18161, 3209,
  7742, 7877, 13, 50756], "temperature": 0.0, "avg_logprob": -0.15498650868733724,
  "compression_ratio": 1.7174887892376682, "no_speech_prob": 0.005225573666393757},
  {"id": 127, "seek": 89936, "start": 907.2, "end": 916.08, "text": " So that''s a
  kind of open neural network format that multiple companies like Microsoft, I think",
  "tokens": [50756, 407, 300, 311, 257, 733, 295, 1269, 18161, 3209, 7877, 300, 3866,
  3431, 411, 8116, 11, 286, 519, 51200], "temperature": 0.0, "avg_logprob": -0.15498650868733724,
  "compression_ratio": 1.7174887892376682, "no_speech_prob": 0.005225573666393757},
  {"id": 128, "seek": 89936, "start": 916.08, "end": 922.0, "text": " also Facebook
  have rallied around, you know, this open format. So you can take the transformer",
  "tokens": [51200, 611, 4384, 362, 31552, 1091, 926, 11, 291, 458, 11, 341, 1269,
  7877, 13, 407, 291, 393, 747, 264, 31782, 51496], "temperature": 0.0, "avg_logprob":
  -0.15498650868733724, "compression_ratio": 1.7174887892376682, "no_speech_prob":
  0.005225573666393757}, {"id": 129, "seek": 89936, "start": 922.0, "end": 928.72,
  "text": " models from the hugging face library and then you can export it to on
  X and then you can import", "tokens": [51496, 5245, 490, 264, 41706, 1851, 6405,
  293, 550, 291, 393, 10725, 309, 281, 322, 1783, 293, 550, 291, 393, 974, 51832],
  "temperature": 0.0, "avg_logprob": -0.15498650868733724, "compression_ratio": 1.7174887892376682,
  "no_speech_prob": 0.005225573666393757}, {"id": 130, "seek": 92872, "start": 928.72,
  "end": 936.32, "text": " all next models into westpun for evaluation. And westpun
  we integrate with on X runtime,", "tokens": [50364, 439, 958, 5245, 666, 7009, 79,
  409, 337, 13344, 13, 400, 7009, 79, 409, 321, 13365, 365, 322, 1783, 34474, 11,
  50744], "temperature": 0.0, "avg_logprob": -0.22077992497658244, "compression_ratio":
  1.6244541484716157, "no_speech_prob": 0.0015304171247407794}, {"id": 131, "seek":
  92872, "start": 936.32, "end": 941.9200000000001, "text": " which is open source
  library from Microsoft, which has a lot of different language findings,", "tokens":
  [50744, 597, 307, 1269, 4009, 6405, 490, 8116, 11, 597, 575, 257, 688, 295, 819,
  2856, 16483, 11, 51024], "temperature": 0.0, "avg_logprob": -0.22077992497658244,
  "compression_ratio": 1.6244541484716157, "no_speech_prob": 0.0015304171247407794},
  {"id": 132, "seek": 92872, "start": 941.9200000000001, "end": 949.2, "text": " Python,
  C++, Java. So it''s a really great library and we integrate with that. So you don''t
  use", "tokens": [51024, 15329, 11, 383, 25472, 11, 10745, 13, 407, 309, 311, 257,
  534, 869, 6405, 293, 321, 13365, 365, 300, 13, 407, 291, 500, 380, 764, 51388],
  "temperature": 0.0, "avg_logprob": -0.22077992497658244, "compression_ratio": 1.6244541484716157,
  "no_speech_prob": 0.0015304171247407794}, {"id": 133, "seek": 92872, "start": 949.2,
  "end": 954.8000000000001, "text": " it directly, but we have like you can put the
  model here, westpun you can be use it and you can", "tokens": [51388, 309, 3838,
  11, 457, 321, 362, 411, 291, 393, 829, 264, 2316, 510, 11, 7009, 79, 409, 291, 393,
  312, 764, 309, 293, 291, 393, 51668], "temperature": 0.0, "avg_logprob": -0.22077992497658244,
  "compression_ratio": 1.6244541484716157, "no_speech_prob": 0.0015304171247407794},
  {"id": 134, "seek": 95480, "start": 954.88, "end": 961.52, "text": " invoke it and
  so on. And those models and then you''re kind of a trade off between, you know,",
  "tokens": [50368, 41117, 309, 293, 370, 322, 13, 400, 729, 5245, 293, 550, 291,
  434, 733, 295, 257, 4923, 766, 1296, 11, 291, 458, 11, 50700], "temperature": 0.0,
  "avg_logprob": -0.17766854070848034, "compression_ratio": 1.6784452296819787, "no_speech_prob":
  0.006654925644397736}, {"id": 135, "seek": 95480, "start": 962.24, "end": 967.5999999999999,
  "text": " getting to know westpun playing around with it and then, you know, maybe
  low QPS, but in the", "tokens": [50736, 1242, 281, 458, 7009, 79, 409, 2433, 926,
  365, 309, 293, 550, 11, 291, 458, 11, 1310, 2295, 1249, 6273, 11, 457, 294, 264,
  51004], "temperature": 0.0, "avg_logprob": -0.17766854070848034, "compression_ratio":
  1.6784452296819787, "no_speech_prob": 0.006654925644397736}, {"id": 136, "seek":
  95480, "start": 967.5999999999999, "end": 973.1999999999999, "text": " scenario
  where you have a really large scale, you want to do 100,000 per cent back and there''s",
  "tokens": [51004, 9005, 689, 291, 362, 257, 534, 2416, 4373, 11, 291, 528, 281,
  360, 2319, 11, 1360, 680, 1489, 646, 293, 456, 311, 51284], "temperature": 0.0,
  "avg_logprob": -0.17766854070848034, "compression_ratio": 1.6784452296819787, "no_speech_prob":
  0.006654925644397736}, {"id": 137, "seek": 95480, "start": 973.1999999999999, "end":
  977.68, "text": " something like that, then you move it to on X and deploy it actually
  inside the westpun cluster,", "tokens": [51284, 746, 411, 300, 11, 550, 291, 1286,
  309, 281, 322, 1783, 293, 7274, 309, 767, 1854, 264, 7009, 79, 409, 13630, 11, 51508],
  "temperature": 0.0, "avg_logprob": -0.17766854070848034, "compression_ratio": 1.6784452296819787,
  "no_speech_prob": 0.006654925644397736}, {"id": 138, "seek": 95480, "start": 977.68,
  "end": 984.0799999999999, "text": " which has many benefits because then you don''t
  transfer a lot of data over the network and so on,", "tokens": [51508, 597, 575,
  867, 5311, 570, 550, 291, 500, 380, 5003, 257, 688, 295, 1412, 670, 264, 3209, 293,
  370, 322, 11, 51828], "temperature": 0.0, "avg_logprob": -0.17766854070848034, "compression_ratio":
  1.6784452296819787, "no_speech_prob": 0.006654925644397736}, {"id": 139, "seek":
  98408, "start": 984.08, "end": 990.72, "text": " because network is still even,
  you know, within the data centers, maybe the network limitations have", "tokens":
  [50364, 570, 3209, 307, 920, 754, 11, 291, 458, 11, 1951, 264, 1412, 10898, 11,
  1310, 264, 3209, 15705, 362, 50696], "temperature": 0.0, "avg_logprob": -0.20668819386471984,
  "compression_ratio": 1.6431718061674008, "no_speech_prob": 0.0009269010042771697},
  {"id": 140, "seek": 98408, "start": 991.76, "end": 1000.32, "text": " this sold
  so you can get 10 gigs or 25 gigs even, but going cross region, then latency is
  still", "tokens": [50748, 341, 3718, 370, 291, 393, 483, 1266, 34586, 420, 3552,
  34586, 754, 11, 457, 516, 3278, 4458, 11, 550, 27043, 307, 920, 51176], "temperature":
  0.0, "avg_logprob": -0.20668819386471984, "compression_ratio": 1.6431718061674008,
  "no_speech_prob": 0.0009269010042771697}, {"id": 141, "seek": 98408, "start": 1001.0400000000001,
  "end": 1006.5600000000001, "text": " concern and that''s that''s one thing that
  really fascinates me is that we''re still sometimes,", "tokens": [51212, 3136, 293,
  300, 311, 300, 311, 472, 551, 300, 534, 7184, 259, 1024, 385, 307, 300, 321, 434,
  920, 2171, 11, 51488], "temperature": 0.0, "avg_logprob": -0.20668819386471984,
  "compression_ratio": 1.6431718061674008, "no_speech_prob": 0.0009269010042771697},
  {"id": 142, "seek": 98408, "start": 1006.5600000000001, "end": 1012.48, "text":
  " you know, the use cases are bottlenecked by the speed of the light, right? So
  yeah,", "tokens": [51488, 291, 458, 11, 264, 764, 3331, 366, 44641, 44118, 538,
  264, 3073, 295, 264, 1442, 11, 558, 30, 407, 1338, 11, 51784], "temperature": 0.0,
  "avg_logprob": -0.20668819386471984, "compression_ratio": 1.6431718061674008, "no_speech_prob":
  0.0009269010042771697}, {"id": 143, "seek": 101248, "start": 1012.64, "end": 1016.88,
  "text": " going from the east goes to the west coast and the US is easily 100 milliseconds.
  So", "tokens": [50372, 516, 490, 264, 10648, 1709, 281, 264, 7009, 8684, 293, 264,
  2546, 307, 3612, 2319, 34184, 13, 407, 50584], "temperature": 0.0, "avg_logprob":
  -0.2670500095073993, "compression_ratio": 1.5533980582524272, "no_speech_prob":
  0.0024898636620491743}, {"id": 144, "seek": 101248, "start": 1017.9200000000001,
  "end": 1021.36, "text": " hasn''t been yet canceled or sold so yeah, physics.",
  "tokens": [50636, 6132, 380, 668, 1939, 24839, 420, 3718, 370, 1338, 11, 10649,
  13, 50808], "temperature": 0.0, "avg_logprob": -0.2670500095073993, "compression_ratio":
  1.5533980582524272, "no_speech_prob": 0.0024898636620491743}, {"id": 145, "seek":
  101248, "start": 1024.64, "end": 1031.2, "text": " Yeah, this is fantastic and and
  so and also like even before we go into this wonderful world", "tokens": [50972,
  865, 11, 341, 307, 5456, 293, 293, 370, 293, 611, 411, 754, 949, 321, 352, 666,
  341, 3715, 1002, 51300], "temperature": 0.0, "avg_logprob": -0.2670500095073993,
  "compression_ratio": 1.5533980582524272, "no_speech_prob": 0.0024898636620491743},
  {"id": 146, "seek": 101248, "start": 1031.2, "end": 1037.68, "text": " of models
  and latest advancements like I''m still curious also to dig into the item that you",
  "tokens": [51300, 295, 5245, 293, 6792, 7295, 1117, 411, 286, 478, 920, 6369, 611,
  281, 2528, 666, 264, 3174, 300, 291, 51624], "temperature": 0.0, "avg_logprob":
  -0.2670500095073993, "compression_ratio": 1.5533980582524272, "no_speech_prob":
  0.0024898636620491743}, {"id": 147, "seek": 103768, "start": 1037.68, "end": 1044.72,
  "text": " mentioned like you when when you have been evolving westpun over time,
  you found a need to add", "tokens": [50364, 2835, 411, 291, 562, 562, 291, 362,
  668, 21085, 7009, 79, 409, 670, 565, 11, 291, 1352, 257, 643, 281, 909, 50716],
  "temperature": 0.0, "avg_logprob": -0.19216473182935392, "compression_ratio": 1.8046511627906976,
  "no_speech_prob": 0.003391799284145236}, {"id": 148, "seek": 103768, "start": 1044.72,
  "end": 1049.92, "text": " something really interesting, some really interesting
  data structures like tensors you mentioned and", "tokens": [50716, 746, 534, 1880,
  11, 512, 534, 1880, 1412, 9227, 411, 10688, 830, 291, 2835, 293, 50976], "temperature":
  0.0, "avg_logprob": -0.19216473182935392, "compression_ratio": 1.8046511627906976,
  "no_speech_prob": 0.003391799284145236}, {"id": 149, "seek": 103768, "start": 1049.92,
  "end": 1057.6000000000001, "text": " like could you elaborate a bit more on how
  this need arise and also like, you know, what are the", "tokens": [50976, 411, 727,
  291, 20945, 257, 857, 544, 322, 577, 341, 643, 20288, 293, 611, 411, 11, 291, 458,
  11, 437, 366, 264, 51360], "temperature": 0.0, "avg_logprob": -0.19216473182935392,
  "compression_ratio": 1.8046511627906976, "no_speech_prob": 0.003391799284145236},
  {"id": 150, "seek": 103768, "start": 1058.5600000000002, "end": 1064.3200000000002,
  "text": " use cases, typical use cases for it today and also how accessible to an
  average user of westpun", "tokens": [51408, 764, 3331, 11, 7476, 764, 3331, 337,
  309, 965, 293, 611, 577, 9515, 281, 364, 4274, 4195, 295, 7009, 79, 409, 51696],
  "temperature": 0.0, "avg_logprob": -0.19216473182935392, "compression_ratio": 1.8046511627906976,
  "no_speech_prob": 0.003391799284145236}, {"id": 151, "seek": 106432, "start": 1064.32,
  "end": 1073.9199999999998, "text": " so to say. Yeah, so I''ll do a little bit of
  history on that. So the best for document model you", "tokens": [50364, 370, 281,
  584, 13, 865, 11, 370, 286, 603, 360, 257, 707, 857, 295, 2503, 322, 300, 13, 407,
  264, 1151, 337, 4166, 2316, 291, 50844], "temperature": 0.0, "avg_logprob": -0.21822569105360243,
  "compression_ratio": 1.7432432432432432, "no_speech_prob": 0.005370495840907097},
  {"id": 152, "seek": 106432, "start": 1073.9199999999998, "end": 1079.6, "text":
  " write has a fixed kind of you have to have a defined schema in westpun. So you
  have to define it", "tokens": [50844, 2464, 575, 257, 6806, 733, 295, 291, 362,
  281, 362, 257, 7642, 34078, 294, 7009, 79, 409, 13, 407, 291, 362, 281, 6964, 309,
  51128], "temperature": 0.0, "avg_logprob": -0.21822569105360243, "compression_ratio":
  1.7432432432432432, "no_speech_prob": 0.005370495840907097}, {"id": 153, "seek":
  106432, "start": 1079.6, "end": 1085.4399999999998, "text": " for instance, you
  have a document type called document and it has a title, it has maybe some time",
  "tokens": [51128, 337, 5197, 11, 291, 362, 257, 4166, 2010, 1219, 4166, 293, 309,
  575, 257, 4876, 11, 309, 575, 1310, 512, 565, 51420], "temperature": 0.0, "avg_logprob":
  -0.21822569105360243, "compression_ratio": 1.7432432432432432, "no_speech_prob":
  0.005370495840907097}, {"id": 154, "seek": 106432, "start": 1085.4399999999998,
  "end": 1092.0, "text": " stamp, it might be have an integer attribute. So there
  are different like normal document model,", "tokens": [51420, 9921, 11, 309, 1062,
  312, 362, 364, 24922, 19667, 13, 407, 456, 366, 819, 411, 2710, 4166, 2316, 11,
  51748], "temperature": 0.0, "avg_logprob": -0.21822569105360243, "compression_ratio":
  1.7432432432432432, "no_speech_prob": 0.005370495840907097}, {"id": 155, "seek":
  109200, "start": 1092.0, "end": 1099.92, "text": " what you expect from kind of
  any any schema oriented database and we also had vectors so you can do", "tokens":
  [50364, 437, 291, 2066, 490, 733, 295, 604, 604, 34078, 21841, 8149, 293, 321, 611,
  632, 18875, 370, 291, 393, 360, 50760], "temperature": 0.0, "avg_logprob": -0.22447259426116944,
  "compression_ratio": 1.7431192660550459, "no_speech_prob": 0.00042848754674196243},
  {"id": 156, "seek": 109200, "start": 1100.8, "end": 1106.88, "text": " early on
  that you can actually do brute force dot products as part of ranking because that
  was", "tokens": [50804, 2440, 322, 300, 291, 393, 767, 360, 47909, 3464, 5893, 3383,
  382, 644, 295, 17833, 570, 300, 390, 51108], "temperature": 0.0, "avg_logprob":
  -0.22447259426116944, "compression_ratio": 1.7431192660550459, "no_speech_prob":
  0.00042848754674196243}, {"id": 157, "seek": 109200, "start": 1106.88, "end": 1112.72,
  "text": " really popular among in in your you know for various ranking requirements
  you will multiply or", "tokens": [51108, 534, 3743, 3654, 294, 294, 428, 291, 458,
  337, 3683, 17833, 7728, 291, 486, 12972, 420, 51400], "temperature": 0.0, "avg_logprob":
  -0.22447259426116944, "compression_ratio": 1.7431192660550459, "no_speech_prob":
  0.00042848754674196243}, {"id": 158, "seek": 109200, "start": 1112.72, "end": 1117.44,
  "text": " sorry, you will perform multiple different dot products over the documents
  that you you''re", "tokens": [51400, 2597, 11, 291, 486, 2042, 3866, 819, 5893,
  3383, 670, 264, 8512, 300, 291, 291, 434, 51636], "temperature": 0.0, "avg_logprob":
  -0.22447259426116944, "compression_ratio": 1.7431192660550459, "no_speech_prob":
  0.00042848754674196243}, {"id": 159, "seek": 111744, "start": 1117.44, "end": 1126.0800000000002,
  "text": " queried as retreat then in around 2013 2014 the researchers in your outside,
  you know, we really want", "tokens": [50364, 7083, 1091, 382, 15505, 550, 294, 926,
  9012, 8227, 264, 10309, 294, 428, 2380, 11, 291, 458, 11, 321, 534, 528, 50796],
  "temperature": 0.0, "avg_logprob": -0.23751659393310548, "compression_ratio": 1.5181347150259068,
  "no_speech_prob": 0.0006269071018323302}, {"id": 160, "seek": 111744, "start": 1126.0800000000002,
  "end": 1133.28, "text": " to express these type of recommendation models where we
  can use the general concept of tensor so", "tokens": [50796, 281, 5109, 613, 2010,
  295, 11879, 5245, 689, 321, 393, 764, 264, 2674, 3410, 295, 40863, 370, 51156],
  "temperature": 0.0, "avg_logprob": -0.23751659393310548, "compression_ratio": 1.5181347150259068,
  "no_speech_prob": 0.0006269071018323302}, {"id": 161, "seek": 111744, "start": 1133.28,
  "end": 1139.6000000000001, "text": " not just storing a vector in the document but
  even a matrix and they had some use cases around", "tokens": [51156, 406, 445, 26085,
  257, 8062, 294, 264, 4166, 457, 754, 257, 8141, 293, 436, 632, 512, 764, 3331, 926,
  51472], "temperature": 0.0, "avg_logprob": -0.23751659393310548, "compression_ratio":
  1.5181347150259068, "no_speech_prob": 0.0006269071018323302}, {"id": 162, "seek":
  113960, "start": 1140.56, "end": 1147.6, "text": " recommendation. So for instance
  in the in the in the document you can represent in the matrix so", "tokens": [50412,
  11879, 13, 407, 337, 5197, 294, 264, 294, 264, 294, 264, 4166, 291, 393, 2906, 294,
  264, 8141, 370, 50764], "temperature": 0.0, "avg_logprob": -0.16803231693449475,
  "compression_ratio": 1.9646464646464648, "no_speech_prob": 0.0013109511928632855},
  {"id": 163, "seek": 113960, "start": 1147.6, "end": 1155.4399999999998, "text":
  " you can have multiple is this document popular in multiple different categories
  for example that", "tokens": [50764, 291, 393, 362, 3866, 307, 341, 4166, 3743,
  294, 3866, 819, 10479, 337, 1365, 300, 51156], "temperature": 0.0, "avg_logprob":
  -0.16803231693449475, "compression_ratio": 1.9646464646464648, "no_speech_prob":
  0.0013109511928632855}, {"id": 164, "seek": 113960, "start": 1155.4399999999998,
  "end": 1161.6799999999998, "text": " you know this document is popular among people
  that are interested in use this is in the ones that", "tokens": [51156, 291, 458,
  341, 4166, 307, 3743, 3654, 561, 300, 366, 3102, 294, 764, 341, 307, 294, 264, 2306,
  300, 51468], "temperature": 0.0, "avg_logprob": -0.16803231693449475, "compression_ratio":
  1.9646464646464648, "no_speech_prob": 0.0013109511928632855}, {"id": 165, "seek":
  113960, "start": 1161.6799999999998, "end": 1168.08, "text": " they''re interested
  in finance and so on. So it''s a really like complex and complex like that you",
  "tokens": [51468, 436, 434, 3102, 294, 10719, 293, 370, 322, 13, 407, 309, 311,
  257, 534, 411, 3997, 293, 3997, 411, 300, 291, 51788], "temperature": 0.0, "avg_logprob":
  -0.16803231693449475, "compression_ratio": 1.9646464646464648, "no_speech_prob":
  0.0013109511928632855}, {"id": 166, "seek": 116808, "start": 1168.08, "end": 1173.1999999999998,
  "text": " can actually have both the tensors in the in the document side but also
  the query side and then", "tokens": [50364, 393, 767, 362, 1293, 264, 10688, 830,
  294, 264, 294, 264, 4166, 1252, 457, 611, 264, 14581, 1252, 293, 550, 50620], "temperature":
  0.0, "avg_logprob": -0.1717419007245232, "compression_ratio": 1.784037558685446,
  "no_speech_prob": 4.991051537217572e-05}, {"id": 167, "seek": 116808, "start": 1173.1999999999998,
  "end": 1179.84, "text": " you can do during the ranking phase you can evaluate these
  kind of expressions so it''s a really", "tokens": [50620, 291, 393, 360, 1830, 264,
  17833, 5574, 291, 393, 13059, 613, 733, 295, 15277, 370, 309, 311, 257, 534, 50952],
  "temperature": 0.0, "avg_logprob": -0.1717419007245232, "compression_ratio": 1.784037558685446,
  "no_speech_prob": 4.991051537217572e-05}, {"id": 168, "seek": 116808, "start": 1181.4399999999998,
  "end": 1188.6399999999999, "text": " it''s a really powerful the language and one
  example concrete example is we haven''t touched on", "tokens": [51032, 309, 311,
  257, 534, 4005, 264, 2856, 293, 472, 1365, 9859, 1365, 307, 321, 2378, 380, 9828,
  322, 51392], "temperature": 0.0, "avg_logprob": -0.1717419007245232, "compression_ratio":
  1.784037558685446, "no_speech_prob": 4.991051537217572e-05}, {"id": 169, "seek":
  116808, "start": 1188.6399999999999, "end": 1195.1999999999998, "text": " the language
  models and so on but for instance the callbert model which is contextualized late",
  "tokens": [51392, 264, 2856, 5245, 293, 370, 322, 457, 337, 5197, 264, 818, 4290,
  2316, 597, 307, 35526, 1602, 3469, 51720], "temperature": 0.0, "avg_logprob": -0.1717419007245232,
  "compression_ratio": 1.784037558685446, "no_speech_prob": 4.991051537217572e-05},
  {"id": 170, "seek": 119520, "start": 1196.0800000000002, "end": 1203.52, "text":
  " interaction overbert where you actually take the query is not represented as one
  vector", "tokens": [50408, 9285, 670, 4290, 689, 291, 767, 747, 264, 14581, 307,
  406, 10379, 382, 472, 8062, 50780], "temperature": 0.0, "avg_logprob": -0.13808503935608682,
  "compression_ratio": 1.9841269841269842, "no_speech_prob": 0.001746696187183261},
  {"id": 171, "seek": 119520, "start": 1203.52, "end": 1209.04, "text": " but each
  of the terms in the queries represent the desivector and similar on the document
  side", "tokens": [50780, 457, 1184, 295, 264, 2115, 294, 264, 24109, 2906, 264,
  730, 488, 1672, 293, 2531, 322, 264, 4166, 1252, 51056], "temperature": 0.0, "avg_logprob":
  -0.13808503935608682, "compression_ratio": 1.9841269841269842, "no_speech_prob":
  0.001746696187183261}, {"id": 172, "seek": 119520, "start": 1209.04, "end": 1215.28,
  "text": " each of the document terms are represented as a vector and then at runtime
  you retrieve documents", "tokens": [51056, 1184, 295, 264, 4166, 2115, 366, 10379,
  382, 257, 8062, 293, 550, 412, 34474, 291, 30254, 8512, 51368], "temperature": 0.0,
  "avg_logprob": -0.13808503935608682, "compression_ratio": 1.9841269841269842, "no_speech_prob":
  0.001746696187183261}, {"id": 173, "seek": 119520, "start": 1215.28, "end": 1221.44,
  "text": " and then you rank them based on this maximum similarity function so it
  takes the vector of the", "tokens": [51368, 293, 550, 291, 6181, 552, 2361, 322,
  341, 6674, 32194, 2445, 370, 309, 2516, 264, 8062, 295, 264, 51676], "temperature":
  0.0, "avg_logprob": -0.13808503935608682, "compression_ratio": 1.9841269841269842,
  "no_speech_prob": 0.001746696187183261}, {"id": 174, "seek": 122144, "start": 1221.44,
  "end": 1228.72, "text": " first term and then it performs k dot products against
  the vectors of the document terms and then", "tokens": [50364, 700, 1433, 293, 550,
  309, 26213, 350, 5893, 3383, 1970, 264, 18875, 295, 264, 4166, 2115, 293, 550, 50728],
  "temperature": 0.0, "avg_logprob": -0.1543291532076322, "compression_ratio": 1.916256157635468,
  "no_speech_prob": 0.00021294938051141798}, {"id": 175, "seek": 122144, "start":
  1228.72, "end": 1234.0, "text": " you you take the maximum of that score and then
  you do that for all of the terms and the final is", "tokens": [50728, 291, 291,
  747, 264, 6674, 295, 300, 6175, 293, 550, 291, 360, 300, 337, 439, 295, 264, 2115,
  293, 264, 2572, 307, 50992], "temperature": 0.0, "avg_logprob": -0.1543291532076322,
  "compression_ratio": 1.916256157635468, "no_speech_prob": 0.00021294938051141798},
  {"id": 176, "seek": 122144, "start": 1234.0, "end": 1239.6000000000001, "text":
  " the it''s a sum so that was actually one of the things that I personally the tensors
  hadn''t been", "tokens": [50992, 264, 309, 311, 257, 2408, 370, 300, 390, 767, 472,
  295, 264, 721, 300, 286, 5665, 264, 10688, 830, 8782, 380, 668, 51272], "temperature":
  0.0, "avg_logprob": -0.1543291532076322, "compression_ratio": 1.916256157635468,
  "no_speech_prob": 0.00021294938051141798}, {"id": 177, "seek": 122144, "start":
  1239.6000000000001, "end": 1246.0800000000002, "text": " that much used for search
  use cases but more around recommendation use cases when I when I when I", "tokens":
  [51272, 300, 709, 1143, 337, 3164, 764, 3331, 457, 544, 926, 11879, 764, 3331, 562,
  286, 562, 286, 562, 286, 51596], "temperature": 0.0, "avg_logprob": -0.1543291532076322,
  "compression_ratio": 1.916256157635468, "no_speech_prob": 0.00021294938051141798},
  {"id": 178, "seek": 124608, "start": 1246.6399999999999, "end": 1252.48, "text":
  " saw callbert and I saw the maximum operator I was like this is just perfect fit
  for for the best", "tokens": [50392, 1866, 818, 4290, 293, 286, 1866, 264, 6674,
  12973, 286, 390, 411, 341, 307, 445, 2176, 3318, 337, 337, 264, 1151, 50684], "temperature":
  0.0, "avg_logprob": -0.16759918512922994, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.0010916386963799596}, {"id": 179, "seek": 124608, "start": 1252.48,
  "end": 1262.1599999999999, "text": " potential it''s a perfect use case so yeah
  yeah that''s one example yeah awesome once you described", "tokens": [50684, 3995,
  309, 311, 257, 2176, 764, 1389, 370, 1338, 1338, 300, 311, 472, 1365, 1338, 3476,
  1564, 291, 7619, 51168], "temperature": 0.0, "avg_logprob": -0.16759918512922994,
  "compression_ratio": 1.7399103139013452, "no_speech_prob": 0.0010916386963799596},
  {"id": 180, "seek": 124608, "start": 1262.1599999999999, "end": 1266.6399999999999,
  "text": " like when you go like many models today is like okay embedded spas that
  you embed this paragraph", "tokens": [51168, 411, 562, 291, 352, 411, 867, 5245,
  965, 307, 411, 1392, 16741, 637, 296, 300, 291, 12240, 341, 18865, 51392], "temperature":
  0.0, "avg_logprob": -0.16759918512922994, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.0010916386963799596}, {"id": 181, "seek": 124608, "start": 1266.6399999999999,
  "end": 1274.48, "text": " whatever but if if you need to go world level that''s
  like lots of data lots of computation right", "tokens": [51392, 2035, 457, 498,
  498, 291, 643, 281, 352, 1002, 1496, 300, 311, 411, 3195, 295, 1412, 3195, 295,
  24903, 558, 51784], "temperature": 0.0, "avg_logprob": -0.16759918512922994, "compression_ratio":
  1.7399103139013452, "no_speech_prob": 0.0010916386963799596}, {"id": 182, "seek":
  127448, "start": 1275.28, "end": 1281.6, "text": " so how you would even do this
  sounds like tensors have found the use case there", "tokens": [50404, 370, 577,
  291, 576, 754, 360, 341, 3263, 411, 10688, 830, 362, 1352, 264, 764, 1389, 456,
  50720], "temperature": 0.0, "avg_logprob": -0.23685801714316182, "compression_ratio":
  1.8066037735849056, "no_speech_prob": 0.0004518931673374027}, {"id": 183, "seek":
  127448, "start": 1283.1200000000001, "end": 1290.88, "text": " yeah and in in in
  in callbert what when we we represented callbert on less also we did a large sample",
  "tokens": [50796, 1338, 293, 294, 294, 294, 294, 818, 4290, 437, 562, 321, 321,
  10379, 818, 4290, 322, 1570, 611, 321, 630, 257, 2416, 6889, 51184], "temperature":
  0.0, "avg_logprob": -0.23685801714316182, "compression_ratio": 1.8066037735849056,
  "no_speech_prob": 0.0004518931673374027}, {"id": 184, "seek": 127448, "start": 1290.88,
  "end": 1298.08, "text": " application around the ms marker dataset the passage ranking
  dataset of mammoth marker so we made", "tokens": [51184, 3861, 926, 264, 275, 82,
  15247, 28872, 264, 11497, 17833, 28872, 295, 19033, 900, 15247, 370, 321, 1027,
  51544], "temperature": 0.0, "avg_logprob": -0.23685801714316182, "compression_ratio":
  1.8066037735849056, "no_speech_prob": 0.0004518931673374027}, {"id": 185, "seek":
  127448, "start": 1298.08, "end": 1304.0, "text": " a sample app where you can combine
  these different retrieval and ranking strategies and but in our case", "tokens":
  [51544, 257, 6889, 724, 689, 291, 393, 10432, 613, 819, 19817, 3337, 293, 17833,
  9029, 293, 457, 294, 527, 1389, 51840], "temperature": 0.0, "avg_logprob": -0.23685801714316182,
  "compression_ratio": 1.8066037735849056, "no_speech_prob": 0.0004518931673374027},
  {"id": 186, "seek": 130400, "start": 1304.0, "end": 1310.4, "text": " we used callbert
  as a re ranking model and that''s one of the really strength of of espice that",
  "tokens": [50364, 321, 1143, 818, 4290, 382, 257, 319, 17833, 2316, 293, 300, 311,
  472, 295, 264, 534, 3800, 295, 295, 7089, 573, 300, 50684], "temperature": 0.0,
  "avg_logprob": -0.1403299119737413, "compression_ratio": 1.8285714285714285, "no_speech_prob":
  0.00021134539565537125}, {"id": 187, "seek": 130400, "start": 1311.04, "end": 1319.6,
  "text": " we allow you to express really complex retrieval and ranking pipelines
  so that you do a query and", "tokens": [50716, 321, 2089, 291, 281, 5109, 534, 3997,
  19817, 3337, 293, 17833, 40168, 370, 300, 291, 360, 257, 14581, 293, 51144], "temperature":
  0.0, "avg_logprob": -0.1403299119737413, "compression_ratio": 1.8285714285714285,
  "no_speech_prob": 0.00021134539565537125}, {"id": 188, "seek": 130400, "start":
  1319.6, "end": 1324.88, "text": " then each of the nodes involved in the query they
  will do a local ranking or matching and then you", "tokens": [51144, 550, 1184,
  295, 264, 13891, 3288, 294, 264, 14581, 436, 486, 360, 257, 2654, 17833, 420, 14324,
  293, 550, 291, 51408], "temperature": 0.0, "avg_logprob": -0.1403299119737413, "compression_ratio":
  1.8285714285714285, "no_speech_prob": 0.00021134539565537125}, {"id": 189, "seek":
  130400, "start": 1324.88, "end": 1331.2, "text": " could have a second face locally
  on each node and then when you have the kind of global view", "tokens": [51408,
  727, 362, 257, 1150, 1851, 16143, 322, 1184, 9984, 293, 550, 562, 291, 362, 264,
  733, 295, 4338, 1910, 51724], "temperature": 0.0, "avg_logprob": -0.1403299119737413,
  "compression_ratio": 1.8285714285714285, "no_speech_prob": 0.00021134539565537125},
  {"id": 190, "seek": 133120, "start": 1331.28, "end": 1335.8400000000001, "text":
  " after you have done the scatter gather then you can do another re ranking face
  because then you have", "tokens": [50368, 934, 291, 362, 1096, 264, 34951, 5448,
  550, 291, 393, 360, 1071, 319, 17833, 1851, 570, 550, 291, 362, 50596], "temperature":
  0.0, "avg_logprob": -0.15650162469773066, "compression_ratio": 1.7075812274368232,
  "no_speech_prob": 0.0010767659405246377}, {"id": 191, "seek": 133120, "start": 1335.8400000000001,
  "end": 1341.8400000000001, "text": " the global view so there are a lot of possibilities
  to kind of trade off between accuracy and cost", "tokens": [50596, 264, 4338, 1910,
  370, 456, 366, 257, 688, 295, 12178, 281, 733, 295, 4923, 766, 1296, 14170, 293,
  2063, 50896], "temperature": 0.0, "avg_logprob": -0.15650162469773066, "compression_ratio":
  1.7075812274368232, "no_speech_prob": 0.0010767659405246377}, {"id": 192, "seek":
  133120, "start": 1341.8400000000001, "end": 1347.76, "text": " them yeah yeah exactly
  and actually as you''ve been describing this I also realized that", "tokens": [50896,
  552, 1338, 1338, 2293, 293, 767, 382, 291, 600, 668, 16141, 341, 286, 611, 5334,
  300, 51192], "temperature": 0.0, "avg_logprob": -0.15650162469773066, "compression_ratio":
  1.7075812274368232, "no_speech_prob": 0.0010767659405246377}, {"id": 193, "seek":
  133120, "start": 1348.64, "end": 1354.0, "text": " we''ve been recently discussing
  in one of the podcasts about multi-stage runker right so", "tokens": [51236, 321,
  600, 668, 3938, 10850, 294, 472, 295, 264, 24045, 466, 4825, 12, 17882, 367, 3197,
  260, 558, 370, 51504], "temperature": 0.0, "avg_logprob": -0.15650162469773066,
  "compression_ratio": 1.7075812274368232, "no_speech_prob": 0.0010767659405246377},
  {"id": 194, "seek": 133120, "start": 1354.0, "end": 1359.92, "text": " you could
  have either a sparse or dense retrieval but you can then later use your graph algorithm",
  "tokens": [51504, 291, 727, 362, 2139, 257, 637, 11668, 420, 18011, 19817, 3337,
  457, 291, 393, 550, 1780, 764, 428, 4295, 9284, 51800], "temperature": 0.0, "avg_logprob":
  -0.15650162469773066, "compression_ratio": 1.7075812274368232, "no_speech_prob":
  0.0010767659405246377}, {"id": 195, "seek": 135992, "start": 1360.4, "end": 1368.48,
  "text": " to kind of like re rank the items I think it was in the podcast with Yuri
  Markov the author of H&SW algorithm", "tokens": [50388, 281, 733, 295, 411, 319,
  6181, 264, 4754, 286, 519, 309, 390, 294, 264, 7367, 365, 33901, 3934, 5179, 264,
  3793, 295, 389, 5, 50, 54, 9284, 50792], "temperature": 0.0, "avg_logprob": -0.28793848673502603,
  "compression_ratio": 1.4688995215311005, "no_speech_prob": 0.0009381374693475664},
  {"id": 196, "seek": 135992, "start": 1368.48, "end": 1376.88, "text": " and so have
  you have you seen any use cases based on espice you know for multi-stage ranking
  pipeline?", "tokens": [50792, 293, 370, 362, 291, 362, 291, 1612, 604, 764, 3331,
  2361, 322, 7089, 573, 291, 458, 337, 4825, 12, 17882, 17833, 15517, 30, 51212],
  "temperature": 0.0, "avg_logprob": -0.28793848673502603, "compression_ratio": 1.4688995215311005,
  "no_speech_prob": 0.0009381374693475664}, {"id": 197, "seek": 135992, "start": 1379.1200000000001,
  "end": 1388.96, "text": " Definitely I mean so both the search internally in our
  we also see this outside from customers", "tokens": [51324, 12151, 286, 914, 370,
  1293, 264, 3164, 19501, 294, 527, 321, 611, 536, 341, 2380, 490, 4581, 51816], "temperature":
  0.0, "avg_logprob": -0.28793848673502603, "compression_ratio": 1.4688995215311005,
  "no_speech_prob": 0.0009381374693475664}, {"id": 198, "seek": 138896, "start": 1388.96,
  "end": 1394.0, "text": " using last but they do multi-stage retrieval and ranking
  pipelines so there''s basically", "tokens": [50364, 1228, 1036, 457, 436, 360, 4825,
  12, 17882, 19817, 3337, 293, 17833, 40168, 370, 456, 311, 1936, 50616], "temperature":
  0.0, "avg_logprob": -0.15914190106275605, "compression_ratio": 1.7061611374407584,
  "no_speech_prob": 0.0008941815467551351}, {"id": 199, "seek": 138896, "start": 1396.56,
  "end": 1402.56, "text": " the reason why you do it typically is that it''s too expensive
  to evaluate", "tokens": [50744, 264, 1778, 983, 291, 360, 309, 5850, 307, 300, 309,
  311, 886, 5124, 281, 13059, 51044], "temperature": 0.0, "avg_logprob": -0.15914190106275605,
  "compression_ratio": 1.7061611374407584, "no_speech_prob": 0.0008941815467551351},
  {"id": 200, "seek": 138896, "start": 1404.24, "end": 1410.56, "text": " the kind
  of final ranking model over all the documents right so you take some kind of approximation",
  "tokens": [51128, 264, 733, 295, 2572, 17833, 2316, 670, 439, 264, 8512, 558, 370,
  291, 747, 512, 733, 295, 28023, 51444], "temperature": 0.0, "avg_logprob": -0.15914190106275605,
  "compression_ratio": 1.7061611374407584, "no_speech_prob": 0.0008941815467551351},
  {"id": 201, "seek": 138896, "start": 1410.56, "end": 1416.64, "text": " of that
  model and then you execute that as to kind of candidate the treaver and I think
  one of the", "tokens": [51444, 295, 300, 2316, 293, 550, 291, 14483, 300, 382, 281,
  733, 295, 11532, 264, 2192, 20655, 293, 286, 519, 472, 295, 264, 51748], "temperature":
  0.0, "avg_logprob": -0.15914190106275605, "compression_ratio": 1.7061611374407584,
  "no_speech_prob": 0.0008941815467551351}, {"id": 202, "seek": 141664, "start": 1416.72,
  "end": 1423.2800000000002, "text": " we haven''t talked about the vector search
  capabilities of VESPA yet but one of the beauties of VESPA is", "tokens": [50368,
  321, 2378, 380, 2825, 466, 264, 8062, 3164, 10862, 295, 691, 2358, 10297, 1939,
  457, 472, 295, 264, 1869, 530, 295, 691, 2358, 10297, 307, 50696], "temperature":
  0.0, "avg_logprob": -0.16820520765325997, "compression_ratio": 1.72, "no_speech_prob":
  0.0008973479270935059}, {"id": 203, "seek": 141664, "start": 1423.2800000000002,
  "end": 1429.2, "text": " that we after we integrate it approximate nearest neighbor
  searches that you can do a combination", "tokens": [50696, 300, 321, 934, 321, 13365,
  309, 30874, 23831, 5987, 26701, 300, 291, 393, 360, 257, 6562, 50992], "temperature":
  0.0, "avg_logprob": -0.16820520765325997, "compression_ratio": 1.72, "no_speech_prob":
  0.0008973479270935059}, {"id": 204, "seek": 141664, "start": 1430.16, "end": 1435.68,
  "text": " when you actually do the matching and querying that you can combine it
  the regular sparse or", "tokens": [51040, 562, 291, 767, 360, 264, 14324, 293, 7083,
  1840, 300, 291, 393, 10432, 309, 264, 3890, 637, 11668, 420, 51316], "temperature":
  0.0, "avg_logprob": -0.16820520765325997, "compression_ratio": 1.72, "no_speech_prob":
  0.0008973479270935059}, {"id": 205, "seek": 141664, "start": 1435.68, "end": 1442.24,
  "text": " keyword search with a vector search and then you re rank and it''s kind
  of paradigm of having", "tokens": [51316, 20428, 3164, 365, 257, 8062, 3164, 293,
  550, 291, 319, 6181, 293, 309, 311, 733, 295, 24709, 295, 1419, 51644], "temperature":
  0.0, "avg_logprob": -0.16820520765325997, "compression_ratio": 1.72, "no_speech_prob":
  0.0008973479270935059}, {"id": 206, "seek": 144224, "start": 1442.32, "end": 1447.2,
  "text": " multiple stages you know you see that in the question answering pipelines
  as well right or you have", "tokens": [50368, 3866, 10232, 291, 458, 291, 536, 300,
  294, 264, 1168, 13430, 40168, 382, 731, 558, 420, 291, 362, 50612], "temperature":
  0.0, "avg_logprob": -0.1214578769825123, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.002143857069313526}, {"id": 207, "seek": 144224, "start": 1447.68,
  "end": 1454.0, "text": " retriever and then you have what they call a reader right
  so it basically finds some candidate", "tokens": [50636, 19817, 331, 293, 550, 291,
  362, 437, 436, 818, 257, 15149, 558, 370, 309, 1936, 10704, 512, 11532, 50952],
  "temperature": 0.0, "avg_logprob": -0.1214578769825123, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.002143857069313526}, {"id": 208, "seek": 144224, "start": 1454.0,
  "end": 1461.36, "text": " passages from Wikipedia and then extracts in a reader
  but evaluating the reader which is a complex", "tokens": [50952, 31589, 490, 28999,
  293, 550, 8947, 82, 294, 257, 15149, 457, 27479, 264, 15149, 597, 307, 257, 3997,
  51320], "temperature": 0.0, "avg_logprob": -0.1214578769825123, "compression_ratio":
  1.7399103139013452, "no_speech_prob": 0.002143857069313526}, {"id": 209, "seek":
  144224, "start": 1461.36, "end": 1466.24, "text": " typically a transformer model
  where you input both the query and the document at the same time", "tokens": [51320,
  5850, 257, 31782, 2316, 689, 291, 4846, 1293, 264, 14581, 293, 264, 4166, 412, 264,
  912, 565, 51564], "temperature": 0.0, "avg_logprob": -0.1214578769825123, "compression_ratio":
  1.7399103139013452, "no_speech_prob": 0.002143857069313526}, {"id": 210, "seek":
  146624, "start": 1466.32, "end": 1472.56, "text": " into the deep neural network
  it''s very complex to actually evaluate that overall the potential", "tokens": [50368,
  666, 264, 2452, 18161, 3209, 309, 311, 588, 3997, 281, 767, 13059, 300, 4787, 264,
  3995, 50680], "temperature": 0.0, "avg_logprob": -0.19715923982508043, "compression_ratio":
  1.7324561403508771, "no_speech_prob": 0.0029489686712622643}, {"id": 211, "seek":
  146624, "start": 1473.1200000000001, "end": 1479.52, "text": " passages and user
  types. It''s like super intensive and I''m super curious to drill into this topic
  of", "tokens": [50708, 31589, 293, 4195, 3467, 13, 467, 311, 411, 1687, 18957, 293,
  286, 478, 1687, 6369, 281, 11392, 666, 341, 4829, 295, 51028], "temperature": 0.0,
  "avg_logprob": -0.19715923982508043, "compression_ratio": 1.7324561403508771, "no_speech_prob":
  0.0029489686712622643}, {"id": 212, "seek": 146624, "start": 1479.52, "end": 1485.92,
  "text": " like combining you know neural search with sparse search actually before
  that as you''ve been talking", "tokens": [51028, 411, 21928, 291, 458, 18161, 3164,
  365, 637, 11668, 3164, 767, 949, 300, 382, 291, 600, 668, 1417, 51348], "temperature":
  0.0, "avg_logprob": -0.19715923982508043, "compression_ratio": 1.7324561403508771,
  "no_speech_prob": 0.0029489686712622643}, {"id": 213, "seek": 146624, "start": 1485.92,
  "end": 1492.4, "text": " I''ve realized I''m actually now taking a search with machine
  learning course dot by grand ingressol", "tokens": [51348, 286, 600, 5334, 286,
  478, 767, 586, 1940, 257, 3164, 365, 3479, 2539, 1164, 5893, 538, 2697, 3957, 735,
  401, 51672], "temperature": 0.0, "avg_logprob": -0.19715923982508043, "compression_ratio":
  1.7324561403508771, "no_speech_prob": 0.0029489686712622643}, {"id": 214, "seek":
  149240, "start": 1492.5600000000002, "end": 1499.1200000000001, "text": " Daniel
  thank you like it''s a fantastic course I can highly recommend it it''s super intense
  as well", "tokens": [50372, 8033, 1309, 291, 411, 309, 311, 257, 5456, 1164, 286,
  393, 5405, 2748, 309, 309, 311, 1687, 9447, 382, 731, 50700], "temperature": 0.0,
  "avg_logprob": -0.16151119413829984, "compression_ratio": 1.7522522522522523, "no_speech_prob":
  0.005738195031881332}, {"id": 215, "seek": 149240, "start": 1499.1200000000001,
  "end": 1505.76, "text": " and I think yesterday grand mentioned that there are companies
  which you know that they really", "tokens": [50700, 293, 286, 519, 5186, 2697, 2835,
  300, 456, 366, 3431, 597, 291, 458, 300, 436, 534, 51032], "temperature": 0.0, "avg_logprob":
  -0.16151119413829984, "compression_ratio": 1.7522522522522523, "no_speech_prob":
  0.005738195031881332}, {"id": 216, "seek": 149240, "start": 1505.76, "end": 1511.92,
  "text": " need to optimize only like top one or top two results and they have built
  models to optimize only", "tokens": [51032, 643, 281, 19719, 787, 411, 1192, 472,
  420, 1192, 732, 3542, 293, 436, 362, 3094, 5245, 281, 19719, 787, 51340], "temperature":
  0.0, "avg_logprob": -0.16151119413829984, "compression_ratio": 1.7522522522522523,
  "no_speech_prob": 0.005738195031881332}, {"id": 217, "seek": 149240, "start": 1511.92,
  "end": 1518.96, "text": " that top one or top two which sounds like my mind blowing
  right and that was like something maybe", "tokens": [51340, 300, 1192, 472, 420,
  1192, 732, 597, 3263, 411, 452, 1575, 15068, 558, 293, 300, 390, 411, 746, 1310,
  51692], "temperature": 0.0, "avg_logprob": -0.16151119413829984, "compression_ratio":
  1.7522522522522523, "no_speech_prob": 0.005738195031881332}, {"id": 218, "seek":
  151896, "start": 1519.04, "end": 1525.3600000000001, "text": " this applies to web
  scale to some extent and one of my recent experiences is actually in web scale",
  "tokens": [50368, 341, 13165, 281, 3670, 4373, 281, 512, 8396, 293, 472, 295, 452,
  5162, 5235, 307, 767, 294, 3670, 4373, 50684], "temperature": 0.0, "avg_logprob":
  -0.1052474021911621, "compression_ratio": 1.5797872340425532, "no_speech_prob":
  0.0009645342361181974}, {"id": 219, "seek": 151896, "start": 1525.3600000000001,
  "end": 1532.0, "text": " search engine we have a mobile screen and so we can only
  show top three results and the target is", "tokens": [50684, 3164, 2848, 321, 362,
  257, 6013, 2568, 293, 370, 321, 393, 787, 855, 1192, 1045, 3542, 293, 264, 3779,
  307, 51016], "temperature": 0.0, "avg_logprob": -0.1052474021911621, "compression_ratio":
  1.5797872340425532, "no_speech_prob": 0.0009645342361181974}, {"id": 220, "seek":
  151896, "start": 1532.0, "end": 1541.3600000000001, "text": " obviously to have
  a high CTR and so we''ve quickly noticed that if you do a sparse search without
  any", "tokens": [51016, 2745, 281, 362, 257, 1090, 19529, 49, 293, 370, 321, 600,
  2661, 5694, 300, 498, 291, 360, 257, 637, 11668, 3164, 1553, 604, 51484], "temperature":
  0.0, "avg_logprob": -0.1052474021911621, "compression_ratio": 1.5797872340425532,
  "no_speech_prob": 0.0009645342361181974}, {"id": 221, "seek": 154136, "start": 1541.36,
  "end": 1548.6399999999999, "text": " logic on the query whatsoever CTR is very low
  so you have to do some tricks like", "tokens": [50364, 9952, 322, 264, 14581, 17076,
  19529, 49, 307, 588, 2295, 370, 291, 362, 281, 360, 512, 11733, 411, 50728], "temperature":
  0.0, "avg_logprob": -0.09863645059091074, "compression_ratio": 1.6457399103139014,
  "no_speech_prob": 0.003454318270087242}, {"id": 222, "seek": 154136, "start": 1549.1999999999998,
  "end": 1553.52, "text": " query understanding and also trying to increase precision
  at the same time maintaining the", "tokens": [50756, 14581, 3701, 293, 611, 1382,
  281, 3488, 18356, 412, 264, 912, 565, 14916, 264, 50972], "temperature": 0.0, "avg_logprob":
  -0.09863645059091074, "compression_ratio": 1.6457399103139014, "no_speech_prob":
  0.003454318270087242}, {"id": 223, "seek": 154136, "start": 1553.52, "end": 1560.08,
  "text": " diversity of search in some degree so you know basically it''s very easy
  that with sparse search", "tokens": [50972, 8811, 295, 3164, 294, 512, 4314, 370,
  291, 458, 1936, 309, 311, 588, 1858, 300, 365, 637, 11668, 3164, 51300], "temperature":
  0.0, "avg_logprob": -0.09863645059091074, "compression_ratio": 1.6457399103139014,
  "no_speech_prob": 0.003454318270087242}, {"id": 224, "seek": 154136, "start": 1560.08,
  "end": 1567.1999999999998, "text": " you hit just the tip of that iceberg and basically
  say okay I have three teacher jobs for you which", "tokens": [51300, 291, 2045,
  445, 264, 4125, 295, 300, 38880, 293, 1936, 584, 1392, 286, 362, 1045, 5027, 4782,
  337, 291, 597, 51656], "temperature": 0.0, "avg_logprob": -0.09863645059091074,
  "compression_ratio": 1.6457399103139014, "no_speech_prob": 0.003454318270087242},
  {"id": 225, "seek": 156720, "start": 1567.52, "end": 1572.48, "text": " is not that
  interesting because we don''t know if the user is looking for teacher jobs right
  so", "tokens": [50380, 307, 406, 300, 1880, 570, 321, 500, 380, 458, 498, 264, 4195,
  307, 1237, 337, 5027, 4782, 558, 370, 50628], "temperature": 0.0, "avg_logprob":
  -0.1585766077041626, "compression_ratio": 1.7017543859649122, "no_speech_prob":
  0.0016459384933114052}, {"id": 226, "seek": 156720, "start": 1572.48, "end": 1579.92,
  "text": " so that''s that''s like have you seen cases like this I think these are
  really really challenging ones", "tokens": [50628, 370, 300, 311, 300, 311, 411,
  362, 291, 1612, 3331, 411, 341, 286, 519, 613, 366, 534, 534, 7595, 2306, 51000],
  "temperature": 0.0, "avg_logprob": -0.1585766077041626, "compression_ratio": 1.7017543859649122,
  "no_speech_prob": 0.0016459384933114052}, {"id": 227, "seek": 156720, "start": 1581.2,
  "end": 1587.3600000000001, "text": " yeah but generally if you look at the results
  like if you ever rate on MS Markov for example", "tokens": [51064, 1338, 457, 5101,
  498, 291, 574, 412, 264, 3542, 411, 498, 291, 1562, 3314, 322, 7395, 3934, 5179,
  337, 1365, 51372], "temperature": 0.0, "avg_logprob": -0.1585766077041626, "compression_ratio":
  1.7017543859649122, "no_speech_prob": 0.0016459384933114052}, {"id": 228, "seek":
  156720, "start": 1587.3600000000001, "end": 1594.32, "text": " and the official
  metric there which is the mean the reciprocal rank right so if you get the perfect",
  "tokens": [51372, 293, 264, 4783, 20678, 456, 597, 307, 264, 914, 264, 46948, 6181,
  558, 370, 498, 291, 483, 264, 2176, 51720], "temperature": 0.0, "avg_logprob": -0.1585766077041626,
  "compression_ratio": 1.7017543859649122, "no_speech_prob": 0.0016459384933114052},
  {"id": 229, "seek": 159432, "start": 1594.32, "end": 1598.1599999999999, "text":
  " the actual relevant document you''re able to retrieve it and put it in position
  one", "tokens": [50364, 264, 3539, 7340, 4166, 291, 434, 1075, 281, 30254, 309,
  293, 829, 309, 294, 2535, 472, 50556], "temperature": 0.0, "avg_logprob": -0.10449729495578342,
  "compression_ratio": 1.669683257918552, "no_speech_prob": 0.0007100481889210641},
  {"id": 230, "seek": 159432, "start": 1599.04, "end": 1604.32, "text": " that query
  gets a score of one right but if you put it in the second place it''s gonna have
  a score", "tokens": [50600, 300, 14581, 2170, 257, 6175, 295, 472, 558, 457, 498,
  291, 829, 309, 294, 264, 1150, 1081, 309, 311, 799, 362, 257, 6175, 50864], "temperature":
  0.0, "avg_logprob": -0.10449729495578342, "compression_ratio": 1.669683257918552,
  "no_speech_prob": 0.0007100481889210641}, {"id": 231, "seek": 159432, "start": 1604.32,
  "end": 1611.2, "text": " of 0.5 I think that''s really good measure when you talk
  about mobile screen precision at 1 2 3 so", "tokens": [50864, 295, 1958, 13, 20,
  286, 519, 300, 311, 534, 665, 3481, 562, 291, 751, 466, 6013, 2568, 18356, 412,
  502, 568, 805, 370, 51208], "temperature": 0.0, "avg_logprob": -0.10449729495578342,
  "compression_ratio": 1.669683257918552, "no_speech_prob": 0.0007100481889210641},
  {"id": 232, "seek": 159432, "start": 1611.84, "end": 1617.6799999999998, "text":
  " that''s really important but in the kind of retrieval not this stage retrieval
  and ranking", "tokens": [51240, 300, 311, 534, 1021, 457, 294, 264, 733, 295, 19817,
  3337, 406, 341, 3233, 19817, 3337, 293, 17833, 51532], "temperature": 0.0, "avg_logprob":
  -0.10449729495578342, "compression_ratio": 1.669683257918552, "no_speech_prob":
  0.0007100481889210641}, {"id": 233, "seek": 161768, "start": 1617.68, "end": 1625.6000000000001,
  "text": " pipeline it makes sense to spend more of the computational budget within
  the lakes SLA on those", "tokens": [50364, 15517, 309, 1669, 2020, 281, 3496, 544,
  295, 264, 28270, 4706, 1951, 264, 25595, 318, 11435, 322, 729, 50760], "temperature":
  0.0, "avg_logprob": -0.16362902522087097, "compression_ratio": 1.4736842105263157,
  "no_speech_prob": 0.0033677159808576107}, {"id": 234, "seek": 161768, "start": 1625.6000000000001,
  "end": 1633.92, "text": " top K hits right so like in when you go to Google today
  and you do a search probably 100", "tokens": [50760, 1192, 591, 8664, 558, 370,
  411, 294, 562, 291, 352, 281, 3329, 965, 293, 291, 360, 257, 3164, 1391, 2319, 51176],
  "temperature": 0.0, "avg_logprob": -0.16362902522087097, "compression_ratio": 1.4736842105263157,
  "no_speech_prob": 0.0033677159808576107}, {"id": 235, "seek": 161768, "start": 1633.92,
  "end": 1641.44, "text": " million documents will be excluded in just a fraction
  of a millisecond right and then there are", "tokens": [51176, 2459, 8512, 486, 312,
  29486, 294, 445, 257, 14135, 295, 257, 27940, 18882, 558, 293, 550, 456, 366, 51552],
  "temperature": 0.0, "avg_logprob": -0.16362902522087097, "compression_ratio": 1.4736842105263157,
  "no_speech_prob": 0.0033677159808576107}, {"id": 236, "seek": 164144, "start": 1641.44,
  "end": 1648.8, "text": " multiple stages and you can be sure that the kind of the
  the 10 last documents from the previous", "tokens": [50364, 3866, 10232, 293, 291,
  393, 312, 988, 300, 264, 733, 295, 264, 264, 1266, 1036, 8512, 490, 264, 3894, 50732],
  "temperature": 0.0, "avg_logprob": -0.1745302860553448, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.003506377572193742}, {"id": 237, "seek": 164144, "start": 1648.8,
  "end": 1658.3200000000002, "text": " stages that the invest more time or computer
  computational resources on those hits yeah yeah exactly", "tokens": [50732, 10232,
  300, 264, 1963, 544, 565, 420, 3820, 28270, 3593, 322, 729, 8664, 1338, 1338, 2293,
  51208], "temperature": 0.0, "avg_logprob": -0.1745302860553448, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.003506377572193742}, {"id": 238, "seek":
  164144, "start": 1658.3200000000002, "end": 1663.68, "text": " and also the good
  thing is that is that because that''s when I talked about the West", "tokens": [51208,
  293, 611, 264, 665, 551, 307, 300, 307, 300, 570, 300, 311, 562, 286, 2825, 466,
  264, 4055, 51476], "temperature": 0.0, "avg_logprob": -0.1745302860553448, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.003506377572193742}, {"id": 239, "seek":
  164144, "start": 1663.68, "end": 1668.72, "text": " Architecture where you have
  this division between stateless which is doing the scatter gather", "tokens": [51476,
  43049, 689, 291, 362, 341, 10044, 1296, 2219, 4272, 597, 307, 884, 264, 34951, 5448,
  51728], "temperature": 0.0, "avg_logprob": -0.1745302860553448, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.003506377572193742}, {"id": 240, "seek":
  166872, "start": 1669.3600000000001, "end": 1675.04, "text": " and each of the local
  nodes is that basically in a search engine today you need to move", "tokens": [50396,
  293, 1184, 295, 264, 2654, 13891, 307, 300, 1936, 294, 257, 3164, 2848, 965, 291,
  643, 281, 1286, 50680], "temperature": 0.0, "avg_logprob": -0.20608916979157524,
  "compression_ratio": 1.7877358490566038, "no_speech_prob": 0.0054605938494205475},
  {"id": 241, "seek": 166872, "start": 1675.92, "end": 1682.64, "text": " move computations
  both to the data but there''s a lot of talk about you know moving or separating",
  "tokens": [50724, 1286, 2807, 763, 1293, 281, 264, 1412, 457, 456, 311, 257, 688,
  295, 751, 466, 291, 458, 2684, 420, 29279, 51060], "temperature": 0.0, "avg_logprob":
  -0.20608916979157524, "compression_ratio": 1.7877358490566038, "no_speech_prob":
  0.0054605938494205475}, {"id": 242, "seek": 166872, "start": 1682.64, "end": 1690.16,
  "text": " compute from storage which is a huge thing right in the cloud but in search
  in search use cases", "tokens": [51060, 14722, 490, 6725, 597, 307, 257, 2603, 551,
  558, 294, 264, 4588, 457, 294, 3164, 294, 3164, 764, 3331, 51436], "temperature":
  0.0, "avg_logprob": -0.20608916979157524, "compression_ratio": 1.7877358490566038,
  "no_speech_prob": 0.0054605938494205475}, {"id": 243, "seek": 166872, "start": 1690.16,
  "end": 1696.96, "text": " with high triplet high document or you need to be able
  to do both you need to do fast computations", "tokens": [51436, 365, 1090, 1376,
  14657, 1090, 4166, 420, 291, 643, 281, 312, 1075, 281, 360, 1293, 291, 643, 281,
  360, 2370, 2807, 763, 51776], "temperature": 0.0, "avg_logprob": -0.20608916979157524,
  "compression_ratio": 1.7877358490566038, "no_speech_prob": 0.0054605938494205475},
  {"id": 244, "seek": 169696, "start": 1697.92, "end": 1704.88, "text": " across multiple
  nodes and then you transfer data like in last well each of the hits that you can",
  "tokens": [50412, 2108, 3866, 13891, 293, 550, 291, 5003, 1412, 411, 294, 1036,
  731, 1184, 295, 264, 8664, 300, 291, 393, 50760], "temperature": 0.0, "avg_logprob":
  -0.14356700940565628, "compression_ratio": 1.7066666666666668, "no_speech_prob":
  0.0014597148401662707}, {"id": 245, "seek": 169696, "start": 1705.92, "end": 1712.16,
  "text": " include ranking features or so on that the subsequent phases can actually
  use for re-ranking", "tokens": [50812, 4090, 17833, 4122, 420, 370, 322, 300, 264,
  19962, 18764, 393, 767, 764, 337, 319, 12, 20479, 278, 51124], "temperature": 0.0,
  "avg_logprob": -0.14356700940565628, "compression_ratio": 1.7066666666666668, "no_speech_prob":
  0.0014597148401662707}, {"id": 246, "seek": 169696, "start": 1712.72, "end": 1718.64,
  "text": " and the good thing is like I know you''ve done a talk about diversity
  in search results and so on", "tokens": [51152, 293, 264, 665, 551, 307, 411, 286,
  458, 291, 600, 1096, 257, 751, 466, 8811, 294, 3164, 3542, 293, 370, 322, 51448],
  "temperature": 0.0, "avg_logprob": -0.14356700940565628, "compression_ratio": 1.7066666666666668,
  "no_speech_prob": 0.0014597148401662707}, {"id": 247, "seek": 169696, "start": 1718.64,
  "end": 1725.8400000000001, "text": " is that you need to have that global view you
  know in order to kind of optimize for for diversity", "tokens": [51448, 307, 300,
  291, 643, 281, 362, 300, 4338, 1910, 291, 458, 294, 1668, 281, 733, 295, 19719,
  337, 337, 8811, 51808], "temperature": 0.0, "avg_logprob": -0.14356700940565628,
  "compression_ratio": 1.7066666666666668, "no_speech_prob": 0.0014597148401662707},
  {"id": 248, "seek": 172584, "start": 1725.84, "end": 1730.24, "text": " and then
  you can kind of throw away a lot of the hits that you''re not going to show because
  of", "tokens": [50364, 293, 550, 291, 393, 733, 295, 3507, 1314, 257, 688, 295,
  264, 8664, 300, 291, 434, 406, 516, 281, 855, 570, 295, 50584], "temperature": 0.0,
  "avg_logprob": -0.08826788039434524, "compression_ratio": 1.8818897637795275, "no_speech_prob":
  0.0001775760465534404}, {"id": 249, "seek": 172584, "start": 1730.24, "end": 1735.36,
  "text": " kind of business constraints or diversity constraints and you don''t need
  to invoke the heavy model", "tokens": [50584, 733, 295, 1606, 18491, 420, 8811,
  18491, 293, 291, 500, 380, 643, 281, 41117, 264, 4676, 2316, 50840], "temperature":
  0.0, "avg_logprob": -0.08826788039434524, "compression_ratio": 1.8818897637795275,
  "no_speech_prob": 0.0001775760465534404}, {"id": 250, "seek": 172584, "start": 1736.24,
  "end": 1741.9199999999998, "text": " for those hits yeah so yeah I think it''s interesting
  for these kind of pipelines but one thing that", "tokens": [50884, 337, 729, 8664,
  1338, 370, 1338, 286, 519, 309, 311, 1880, 337, 613, 733, 295, 40168, 457, 472,
  551, 300, 51168], "temperature": 0.0, "avg_logprob": -0.08826788039434524, "compression_ratio":
  1.8818897637795275, "no_speech_prob": 0.0001775760465534404}, {"id": 251, "seek":
  172584, "start": 1741.9199999999998, "end": 1748.1599999999999, "text": " is challenging
  regarding both the stage pipelines is that they interact with each other right",
  "tokens": [51168, 307, 7595, 8595, 1293, 264, 3233, 40168, 307, 300, 436, 4648,
  365, 1184, 661, 558, 51480], "temperature": 0.0, "avg_logprob": -0.08826788039434524,
  "compression_ratio": 1.8818897637795275, "no_speech_prob": 0.0001775760465534404},
  {"id": 252, "seek": 172584, "start": 1748.1599999999999, "end": 1754.3999999999999,
  "text": " and if you do if you have like a system for training your model retraining
  the model using", "tokens": [51480, 293, 498, 291, 360, 498, 291, 362, 411, 257,
  1185, 337, 3097, 428, 2316, 49356, 1760, 264, 2316, 1228, 51792], "temperature":
  0.0, "avg_logprob": -0.08826788039434524, "compression_ratio": 1.8818897637795275,
  "no_speech_prob": 0.0001775760465534404}, {"id": 253, "seek": 175440, "start": 1754.4,
  "end": 1759.2800000000002, "text": " statistical features what are users clicking
  on and so on the one of the features then you will", "tokens": [50364, 22820, 4122,
  437, 366, 5022, 9697, 322, 293, 370, 322, 264, 472, 295, 264, 4122, 550, 291, 486,
  50608], "temperature": 0.0, "avg_logprob": -0.15696592440550355, "compression_ratio":
  1.7412280701754386, "no_speech_prob": 0.000270951451966539}, {"id": 254, "seek":
  175440, "start": 1759.2800000000002, "end": 1766.5600000000002, "text": " have some
  biases towards the actual the ranking algorithm that is in place today because that''s
  the", "tokens": [50608, 362, 512, 32152, 3030, 264, 3539, 264, 17833, 9284, 300,
  307, 294, 1081, 965, 570, 300, 311, 264, 50972], "temperature": 0.0, "avg_logprob":
  -0.15696592440550355, "compression_ratio": 1.7412280701754386, "no_speech_prob":
  0.000270951451966539}, {"id": 255, "seek": 175440, "start": 1766.5600000000002,
  "end": 1774.16, "text": " model that is bringing interactions so you basically just
  retrain on the top hits and that was what", "tokens": [50972, 2316, 300, 307, 5062,
  13280, 370, 291, 1936, 445, 1533, 7146, 322, 264, 1192, 8664, 293, 300, 390, 437,
  51352], "temperature": 0.0, "avg_logprob": -0.15696592440550355, "compression_ratio":
  1.7412280701754386, "no_speech_prob": 0.000270951451966539}, {"id": 256, "seek":
  175440, "start": 1774.16, "end": 1781.1200000000001, "text": " we saw on Amazon
  as well as that when they started to improve the retriever so when it''s not actually",
  "tokens": [51352, 321, 1866, 322, 6795, 382, 731, 382, 300, 562, 436, 1409, 281,
  3470, 264, 19817, 331, 370, 562, 309, 311, 406, 767, 51700], "temperature": 0.0,
  "avg_logprob": -0.15696592440550355, "compression_ratio": 1.7412280701754386, "no_speech_prob":
  0.000270951451966539}, {"id": 257, "seek": 178112, "start": 1781.12, "end": 1789.6799999999998,
  "text": " instead of having a BM25 like do BM25 and then rerank they had a mean
  reciprocal rank score of 0.35", "tokens": [50364, 2602, 295, 1419, 257, 15901, 6074,
  411, 360, 15901, 6074, 293, 550, 319, 20479, 436, 632, 257, 914, 46948, 6181, 6175,
  295, 1958, 13, 8794, 50792], "temperature": 0.0, "avg_logprob": -0.14804854600325876,
  "compression_ratio": 1.7844036697247707, "no_speech_prob": 0.0019400801975280046},
  {"id": 258, "seek": 178112, "start": 1789.6799999999998, "end": 1796.8, "text":
  " or something and now after changing into a dense retriever now we''re talking
  about 0.42 or", "tokens": [50792, 420, 746, 293, 586, 934, 4473, 666, 257, 18011,
  19817, 331, 586, 321, 434, 1417, 466, 1958, 13, 15628, 420, 51148], "temperature":
  0.0, "avg_logprob": -0.14804854600325876, "compression_ratio": 1.7844036697247707,
  "no_speech_prob": 0.0019400801975280046}, {"id": 259, "seek": 178112, "start": 1796.8,
  "end": 1802.7199999999998, "text": " something like that so by improving the improving
  the retriever right because the retriever kind of", "tokens": [51148, 746, 411,
  300, 370, 538, 11470, 264, 11470, 264, 19817, 331, 558, 570, 264, 19817, 331, 733,
  295, 51444], "temperature": 0.0, "avg_logprob": -0.14804854600325876, "compression_ratio":
  1.7844036697247707, "no_speech_prob": 0.0019400801975280046}, {"id": 260, "seek":
  178112, "start": 1802.7199999999998, "end": 1808.2399999999998, "text": " sets the
  upper bound you know because the rerank cannot really dream up you know the relevant
  hits", "tokens": [51444, 6352, 264, 6597, 5472, 291, 458, 570, 264, 319, 20479,
  2644, 534, 3055, 493, 291, 458, 264, 7340, 8664, 51720], "temperature": 0.0, "avg_logprob":
  -0.14804854600325876, "compression_ratio": 1.7844036697247707, "no_speech_prob":
  0.0019400801975280046}, {"id": 261, "seek": 180824, "start": 1808.24, "end": 1814.32,
  "text": " if the retriever hasn''t retrieved it right so that''s an important point
  you know in the retriever", "tokens": [50364, 498, 264, 19817, 331, 6132, 380, 19817,
  937, 309, 558, 370, 300, 311, 364, 1021, 935, 291, 458, 294, 264, 19817, 331, 50668],
  "temperature": 0.0, "avg_logprob": -0.11389731501673793, "compression_ratio": 1.8037037037037038,
  "no_speech_prob": 0.0006391859496943653}, {"id": 262, "seek": 180824, "start": 1814.32,
  "end": 1820.24, "text": " and writing stages so exactly and I think we can gradually
  move into neural search and vector search", "tokens": [50668, 293, 3579, 10232,
  370, 2293, 293, 286, 519, 321, 393, 13145, 1286, 666, 18161, 3164, 293, 8062, 3164,
  50964], "temperature": 0.0, "avg_logprob": -0.11389731501673793, "compression_ratio":
  1.8037037037037038, "no_speech_prob": 0.0006391859496943653}, {"id": 263, "seek":
  180824, "start": 1820.24, "end": 1825.68, "text": " but like you know it was one
  of the students question also yes then the same course how much you", "tokens":
  [50964, 457, 411, 291, 458, 309, 390, 472, 295, 264, 1731, 1168, 611, 2086, 550,
  264, 912, 1164, 577, 709, 291, 51236], "temperature": 0.0, "avg_logprob": -0.11389731501673793,
  "compression_ratio": 1.8037037037037038, "no_speech_prob": 0.0006391859496943653},
  {"id": 264, "seek": 180824, "start": 1825.68, "end": 1831.28, "text": " can actually
  solve with the rerunquer if your first stage retriever didn''t even find what the",
  "tokens": [51236, 393, 767, 5039, 365, 264, 43819, 409, 8035, 498, 428, 700, 3233,
  19817, 331, 994, 380, 754, 915, 437, 264, 51516], "temperature": 0.0, "avg_logprob":
  -0.11389731501673793, "compression_ratio": 1.8037037037037038, "no_speech_prob":
  0.0006391859496943653}, {"id": 265, "seek": 180824, "start": 1831.28, "end": 1836.72,
  "text": " user is looking for which means probably the query is not a match for
  this search engine you know", "tokens": [51516, 4195, 307, 1237, 337, 597, 1355,
  1391, 264, 14581, 307, 406, 257, 2995, 337, 341, 3164, 2848, 291, 458, 51788], "temperature":
  0.0, "avg_logprob": -0.11389731501673793, "compression_ratio": 1.8037037037037038,
  "no_speech_prob": 0.0006391859496943653}, {"id": 266, "seek": 183672, "start": 1837.28,
  "end": 1842.64, "text": " let''s say they''re looking for a specific model of a
  phone but they don''t even cell phones right so", "tokens": [50392, 718, 311, 584,
  436, 434, 1237, 337, 257, 2685, 2316, 295, 257, 2593, 457, 436, 500, 380, 754, 2815,
  10216, 558, 370, 50660], "temperature": 0.0, "avg_logprob": -0.15847271479917377,
  "compression_ratio": 1.6899563318777293, "no_speech_prob": 0.0015201332280412316},
  {"id": 267, "seek": 183672, "start": 1843.28, "end": 1848.8, "text": " like and
  I think the response from Daniel Tankilang on this one was that actually you can",
  "tokens": [50692, 411, 293, 286, 519, 264, 4134, 490, 8033, 314, 27203, 25241, 322,
  341, 472, 390, 300, 767, 291, 393, 50968], "temperature": 0.0, "avg_logprob": -0.15847271479917377,
  "compression_ratio": 1.6899563318777293, "no_speech_prob": 0.0015201332280412316},
  {"id": 268, "seek": 183672, "start": 1848.8, "end": 1854.56, "text": " implement
  a query understanding system which will understand the query as much as it can and
  if it", "tokens": [50968, 4445, 257, 14581, 3701, 1185, 597, 486, 1223, 264, 14581,
  382, 709, 382, 309, 393, 293, 498, 309, 51256], "temperature": 0.0, "avg_logprob":
  -0.15847271479917377, "compression_ratio": 1.6899563318777293, "no_speech_prob":
  0.0015201332280412316}, {"id": 269, "seek": 183672, "start": 1854.56, "end": 1860.64,
  "text": " knows that there are no such items in the database don''t even bother
  searching for them and I think", "tokens": [51256, 3255, 300, 456, 366, 572, 1270,
  4754, 294, 264, 8149, 500, 380, 754, 8677, 10808, 337, 552, 293, 286, 519, 51560],
  "temperature": 0.0, "avg_logprob": -0.15847271479917377, "compression_ratio": 1.6899563318777293,
  "no_speech_prob": 0.0015201332280412316}, {"id": 270, "seek": 186064, "start": 1860.72,
  "end": 1868.8000000000002, "text": " this was a really really clever advice on it
  and and and he said that system worked extremely well", "tokens": [50368, 341, 390,
  257, 534, 534, 13494, 5192, 322, 309, 293, 293, 293, 415, 848, 300, 1185, 2732,
  4664, 731, 50772], "temperature": 0.0, "avg_logprob": -0.11532719511734812, "compression_ratio":
  1.6527777777777777, "no_speech_prob": 0.0026600901037454605}, {"id": 271, "seek":
  186064, "start": 1868.8000000000002, "end": 1875.44, "text": " so like for user
  for user satisfaction to save their time right because in the end what we''re",
  "tokens": [50772, 370, 411, 337, 4195, 337, 4195, 18715, 281, 3155, 641, 565, 558,
  570, 294, 264, 917, 437, 321, 434, 51104], "temperature": 0.0, "avg_logprob": -0.11532719511734812,
  "compression_ratio": 1.6527777777777777, "no_speech_prob": 0.0026600901037454605},
  {"id": 272, "seek": 186064, "start": 1875.44, "end": 1881.1200000000001, "text":
  " doing is actually optimizing the user journey which then translates into business
  right so", "tokens": [51104, 884, 307, 767, 40425, 264, 4195, 4671, 597, 550, 28468,
  666, 1606, 558, 370, 51388], "temperature": 0.0, "avg_logprob": -0.11532719511734812,
  "compression_ratio": 1.6527777777777777, "no_speech_prob": 0.0026600901037454605},
  {"id": 273, "seek": 186064, "start": 1881.1200000000001, "end": 1886.0, "text":
  " that was a fantastic example of how you can also talk such search problem", "tokens":
  [51388, 300, 390, 257, 5456, 1365, 295, 577, 291, 393, 611, 751, 1270, 3164, 1154,
  51632], "temperature": 0.0, "avg_logprob": -0.11532719511734812, "compression_ratio":
  1.6527777777777777, "no_speech_prob": 0.0026600901037454605}, {"id": 274, "seek":
  188600, "start": 1886.64, "end": 1895.52, "text": " yeah and that''s one area where
  I wanted to because we''re building all of these sample applications", "tokens":
  [50396, 1338, 293, 300, 311, 472, 1859, 689, 286, 1415, 281, 570, 321, 434, 2390,
  439, 295, 613, 6889, 5821, 50840], "temperature": 0.0, "avg_logprob": -0.12055834664238824,
  "compression_ratio": 1.6939655172413792, "no_speech_prob": 0.0036166973877698183},
  {"id": 275, "seek": 188600, "start": 1895.52, "end": 1900.88, "text": " what you
  can build with VASPA and query understanding has been one of the topics that I wanted
  to build", "tokens": [50840, 437, 291, 393, 1322, 365, 691, 3160, 10297, 293, 14581,
  3701, 575, 668, 472, 295, 264, 8378, 300, 286, 1415, 281, 1322, 51108], "temperature":
  0.0, "avg_logprob": -0.12055834664238824, "compression_ratio": 1.6939655172413792,
  "no_speech_prob": 0.0036166973877698183}, {"id": 276, "seek": 188600, "start": 1900.88,
  "end": 1906.8, "text": " out to to demonstrate you know how to do that especially
  building it using a transformer model", "tokens": [51108, 484, 281, 281, 11698,
  291, 458, 577, 281, 360, 300, 2318, 2390, 309, 1228, 257, 31782, 2316, 51404], "temperature":
  0.0, "avg_logprob": -0.12055834664238824, "compression_ratio": 1.6939655172413792,
  "no_speech_prob": 0.0036166973877698183}, {"id": 277, "seek": 188600, "start": 1906.8,
  "end": 1913.2, "text": " actually so you can have different ways of doing this but
  one way of doing it is to use it as a", "tokens": [51404, 767, 370, 291, 393, 362,
  819, 2098, 295, 884, 341, 457, 472, 636, 295, 884, 309, 307, 281, 764, 309, 382,
  257, 51724], "temperature": 0.0, "avg_logprob": -0.12055834664238824, "compression_ratio":
  1.6939655172413792, "no_speech_prob": 0.0036166973877698183}, {"id": 278, "seek":
  191320, "start": 1913.2, "end": 1921.1200000000001, "text": " multi-label categorization
  problem so given a query here are the intents and their probability", "tokens":
  [50364, 4825, 12, 75, 18657, 19250, 2144, 1154, 370, 2212, 257, 14581, 510, 366,
  264, 560, 791, 293, 641, 8482, 50760], "temperature": 0.0, "avg_logprob": -0.11612093183729384,
  "compression_ratio": 1.709090909090909, "no_speech_prob": 0.0005346767138689756},
  {"id": 279, "seek": 191320, "start": 1922.24, "end": 1927.3600000000001, "text":
  " but what''s stopping me from doing this is that we need to work on kind of open
  data sets now", "tokens": [50816, 457, 437, 311, 12767, 385, 490, 884, 341, 307,
  300, 321, 643, 281, 589, 322, 733, 295, 1269, 1412, 6352, 586, 51072], "temperature":
  0.0, "avg_logprob": -0.11612093183729384, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.0005346767138689756}, {"id": 280, "seek": 191320, "start": 1927.3600000000001,
  "end": 1933.44, "text": " and there are very few query data sets in this way so
  one approximation is actually to train", "tokens": [51072, 293, 456, 366, 588, 1326,
  14581, 1412, 6352, 294, 341, 636, 370, 472, 28023, 307, 767, 281, 3847, 51376],
  "temperature": 0.0, "avg_logprob": -0.11612093183729384, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.0005346767138689756}, {"id": 281, "seek": 191320, "start": 1934.0,
  "end": 1940.8, "text": " using the title so in the e-commerce set you can train
  based on the titles but then you need to", "tokens": [51404, 1228, 264, 4876, 370,
  294, 264, 308, 12, 26926, 992, 291, 393, 3847, 2361, 322, 264, 12992, 457, 550,
  291, 643, 281, 51744], "temperature": 0.0, "avg_logprob": -0.11612093183729384,
  "compression_ratio": 1.709090909090909, "no_speech_prob": 0.0005346767138689756},
  {"id": 282, "seek": 194080, "start": 1940.8, "end": 1947.2, "text": " have some
  kind of label on you know is this you can do it around categories so you have the
  title", "tokens": [50364, 362, 512, 733, 295, 7645, 322, 291, 458, 307, 341, 291,
  393, 360, 309, 926, 10479, 370, 291, 362, 264, 4876, 50684], "temperature": 0.0,
  "avg_logprob": -0.12704996221205767, "compression_ratio": 1.8130841121495327, "no_speech_prob":
  0.0006706691347062588}, {"id": 283, "seek": 194080, "start": 1947.2, "end": 1953.76,
  "text": " of the e-commerce listing and you have the category and the beauty of
  this is that you''re actually", "tokens": [50684, 295, 264, 308, 12, 26926, 22161,
  293, 291, 362, 264, 7719, 293, 264, 6643, 295, 341, 307, 300, 291, 434, 767, 51012],
  "temperature": 0.0, "avg_logprob": -0.12704996221205767, "compression_ratio": 1.8130841121495327,
  "no_speech_prob": 0.0006706691347062588}, {"id": 284, "seek": 194080, "start": 1953.76,
  "end": 1962.48, "text": " mapping free text queries into kind of a fixed predefined
  vocabulary which is the categories", "tokens": [51012, 18350, 1737, 2487, 24109,
  666, 733, 295, 257, 6806, 659, 37716, 19864, 597, 307, 264, 10479, 51448], "temperature":
  0.0, "avg_logprob": -0.12704996221205767, "compression_ratio": 1.8130841121495327,
  "no_speech_prob": 0.0006706691347062588}, {"id": 285, "seek": 194080, "start": 1962.48,
  "end": 1969.52, "text": " and then you can actually eliminate zero hits the zero
  hits problem because you actually no longer", "tokens": [51448, 293, 550, 291, 393,
  767, 13819, 4018, 8664, 264, 4018, 8664, 1154, 570, 291, 767, 572, 2854, 51800],
  "temperature": 0.0, "avg_logprob": -0.12704996221205767, "compression_ratio": 1.8130841121495327,
  "no_speech_prob": 0.0006706691347062588}, {"id": 286, "seek": 196952, "start": 1969.52,
  "end": 1975.04, "text": " retrieving based on on the free text queries but you''re
  retrieving based on the most kind of", "tokens": [50364, 19817, 798, 2361, 322,
  322, 264, 1737, 2487, 24109, 457, 291, 434, 19817, 798, 2361, 322, 264, 881, 733,
  295, 50640], "temperature": 0.0, "avg_logprob": -0.12792613528190402, "compression_ratio":
  2.102222222222222, "no_speech_prob": 0.0007940616924315691}, {"id": 287, "seek":
  196952, "start": 1975.04, "end": 1979.6, "text": " interesting categories so yeah
  so these are really interesting you know topics and that''s one", "tokens": [50640,
  1880, 10479, 370, 1338, 370, 613, 366, 534, 1880, 291, 458, 8378, 293, 300, 311,
  472, 50868], "temperature": 0.0, "avg_logprob": -0.12792613528190402, "compression_ratio":
  2.102222222222222, "no_speech_prob": 0.0007940616924315691}, {"id": 288, "seek":
  196952, "start": 1979.6, "end": 1985.44, "text": " thing that I find you know with
  search you know and why I love being in search is that there''s", "tokens": [50868,
  551, 300, 286, 915, 291, 458, 365, 3164, 291, 458, 293, 983, 286, 959, 885, 294,
  3164, 307, 300, 456, 311, 51160], "temperature": 0.0, "avg_logprob": -0.12792613528190402,
  "compression_ratio": 2.102222222222222, "no_speech_prob": 0.0007940616924315691},
  {"id": 289, "seek": 196952, "start": 1985.44, "end": 1990.56, "text": " there''s
  there''s there''s a ton of things that you can you know build and you know there''s
  query", "tokens": [51160, 456, 311, 456, 311, 456, 311, 257, 2952, 295, 721, 300,
  291, 393, 291, 458, 1322, 293, 291, 458, 456, 311, 14581, 51416], "temperature":
  0.0, "avg_logprob": -0.12792613528190402, "compression_ratio": 2.102222222222222,
  "no_speech_prob": 0.0007940616924315691}, {"id": 290, "seek": 196952, "start": 1990.56,
  "end": 1997.68, "text": " understanding you know there''s facets there''s retrieval
  and ranking dense bars you know and then", "tokens": [51416, 3701, 291, 458, 456,
  311, 49752, 456, 311, 19817, 3337, 293, 17833, 18011, 10228, 291, 458, 293, 550,
  51772], "temperature": 0.0, "avg_logprob": -0.12792613528190402, "compression_ratio":
  2.102222222222222, "no_speech_prob": 0.0007940616924315691}, {"id": 291, "seek":
  199768, "start": 1997.68, "end": 2003.2, "text": " you have the scale of it you
  know how to make it fast you know there''s so many things you know they''re", "tokens":
  [50364, 291, 362, 264, 4373, 295, 309, 291, 458, 577, 281, 652, 309, 2370, 291,
  458, 456, 311, 370, 867, 721, 291, 458, 436, 434, 50640], "temperature": 0.0, "avg_logprob":
  -0.11847272672151264, "compression_ratio": 1.9274193548387097, "no_speech_prob":
  0.0008521171403117478}, {"id": 292, "seek": 199768, "start": 2003.2, "end": 2009.04,
  "text": " just query understanding you know it''s probably you know a full research
  topic you know on", "tokens": [50640, 445, 14581, 3701, 291, 458, 309, 311, 1391,
  291, 458, 257, 1577, 2132, 4829, 291, 458, 322, 50932], "temperature": 0.0, "avg_logprob":
  -0.11847272672151264, "compression_ratio": 1.9274193548387097, "no_speech_prob":
  0.0008521171403117478}, {"id": 293, "seek": 199768, "start": 2009.04, "end": 2015.1200000000001,
  "text": " its own so there''s so many things involved in search so that''s yeah
  yeah it''s like endless journey", "tokens": [50932, 1080, 1065, 370, 456, 311, 370,
  867, 721, 3288, 294, 3164, 370, 300, 311, 1338, 1338, 309, 311, 411, 16144, 4671,
  51236], "temperature": 0.0, "avg_logprob": -0.11847272672151264, "compression_ratio":
  1.9274193548387097, "no_speech_prob": 0.0008521171403117478}, {"id": 294, "seek":
  199768, "start": 2015.1200000000001, "end": 2020.5600000000002, "text": " I agree
  it''s like yeah it is you can also dive into an old piece out of things or you can",
  "tokens": [51236, 286, 3986, 309, 311, 411, 1338, 309, 307, 291, 393, 611, 9192,
  666, 364, 1331, 2522, 484, 295, 721, 420, 291, 393, 51508], "temperature": 0.0,
  "avg_logprob": -0.11847272672151264, "compression_ratio": 1.9274193548387097, "no_speech_prob":
  0.0008521171403117478}, {"id": 295, "seek": 199768, "start": 2020.5600000000002,
  "end": 2026.16, "text": " stay with like scaling of search or query parsing whatever
  that you find passion and maybe your", "tokens": [51508, 1754, 365, 411, 21589,
  295, 3164, 420, 14581, 21156, 278, 2035, 300, 291, 915, 5418, 293, 1310, 428, 51788],
  "temperature": 0.0, "avg_logprob": -0.11847272672151264, "compression_ratio": 1.9274193548387097,
  "no_speech_prob": 0.0008521171403117478}, {"id": 296, "seek": 202616, "start": 2026.16,
  "end": 2031.76, "text": " passion changes over time as well right so you did a bit
  of an LP then you move to query parsing then", "tokens": [50364, 5418, 2962, 670,
  565, 382, 731, 558, 370, 291, 630, 257, 857, 295, 364, 38095, 550, 291, 1286, 281,
  14581, 21156, 278, 550, 50644], "temperature": 0.0, "avg_logprob": -0.13073219873208916,
  "compression_ratio": 1.7412587412587412, "no_speech_prob": 0.00043184225796721876},
  {"id": 297, "seek": 202616, "start": 2031.76, "end": 2037.0400000000002, "text":
  " you move to maybe even scalability or whatever yeah I agree it''s like a fascinating
  topic and also", "tokens": [50644, 291, 1286, 281, 1310, 754, 15664, 2310, 420,
  2035, 1338, 286, 3986, 309, 311, 411, 257, 10343, 4829, 293, 611, 50908], "temperature":
  0.0, "avg_logprob": -0.13073219873208916, "compression_ratio": 1.7412587412587412,
  "no_speech_prob": 0.00043184225796721876}, {"id": 298, "seek": 202616, "start":
  2037.0400000000002, "end": 2042.0, "text": " what fascinates me is that on the other
  side of things users are also not sleeping they''re puzzling", "tokens": [50908,
  437, 7184, 259, 1024, 385, 307, 300, 322, 264, 661, 1252, 295, 721, 5022, 366, 611,
  406, 8296, 436, 434, 18741, 1688, 51156], "temperature": 0.0, "avg_logprob": -0.13073219873208916,
  "compression_ratio": 1.7412587412587412, "no_speech_prob": 0.00043184225796721876},
  {"id": 299, "seek": 202616, "start": 2042.0, "end": 2048.8, "text": " you all the
  time with new queries seasonal changes data changes as well because in mid-size
  a larger", "tokens": [51156, 291, 439, 264, 565, 365, 777, 24109, 27421, 2962, 1412,
  2962, 382, 731, 570, 294, 2062, 12, 27553, 257, 4833, 51496], "temperature": 0.0,
  "avg_logprob": -0.13073219873208916, "compression_ratio": 1.7412587412587412, "no_speech_prob":
  0.00043184225796721876}, {"id": 300, "seek": 202616, "start": 2048.8, "end": 2054.56,
  "text": " company it''s usually work of multiple teams and you know or departments
  some departments looking", "tokens": [51496, 2237, 309, 311, 2673, 589, 295, 3866,
  5491, 293, 291, 458, 420, 15326, 512, 15326, 1237, 51784], "temperature": 0.0, "avg_logprob":
  -0.13073219873208916, "compression_ratio": 1.7412587412587412, "no_speech_prob":
  0.00043184225796721876}, {"id": 301, "seek": 205456, "start": 2054.56, "end": 2059.92,
  "text": " after data some looking after ranking recommendation all the feature collection
  and what not you know", "tokens": [50364, 934, 1412, 512, 1237, 934, 17833, 11879,
  439, 264, 4111, 5765, 293, 437, 406, 291, 458, 50632], "temperature": 0.0, "avg_logprob":
  -0.08208456493559338, "compression_ratio": 1.9308943089430894, "no_speech_prob":
  0.0008439552038908005}, {"id": 302, "seek": 205456, "start": 2059.92, "end": 2065.92,
  "text": " something somewhere can sometimes go wrong and you need to prepare for
  it you need to interact you", "tokens": [50632, 746, 4079, 393, 2171, 352, 2085,
  293, 291, 643, 281, 5940, 337, 309, 291, 643, 281, 4648, 291, 50932], "temperature":
  0.0, "avg_logprob": -0.08208456493559338, "compression_ratio": 1.9308943089430894,
  "no_speech_prob": 0.0008439552038908005}, {"id": 303, "seek": 205456, "start": 2065.92,
  "end": 2070.32, "text": " need to kind of build a system that is resilient and it''s
  it''s a fantastic fantastic space", "tokens": [50932, 643, 281, 733, 295, 1322,
  257, 1185, 300, 307, 23699, 293, 309, 311, 309, 311, 257, 5456, 5456, 1901, 51152],
  "temperature": 0.0, "avg_logprob": -0.08208456493559338, "compression_ratio": 1.9308943089430894,
  "no_speech_prob": 0.0008439552038908005}, {"id": 304, "seek": 205456, "start": 2072.64,
  "end": 2077.12, "text": " yeah it really is and there''s so many methods and that''s
  also one of the things you know people", "tokens": [51268, 1338, 309, 534, 307,
  293, 456, 311, 370, 867, 7150, 293, 300, 311, 611, 472, 295, 264, 721, 291, 458,
  561, 51492], "temperature": 0.0, "avg_logprob": -0.08208456493559338, "compression_ratio":
  1.9308943089430894, "no_speech_prob": 0.0008439552038908005}, {"id": 305, "seek":
  205456, "start": 2077.68, "end": 2081.36, "text": " you know they want to build
  something that is great you know but even if you''re using a", "tokens": [51520,
  291, 458, 436, 528, 281, 1322, 746, 300, 307, 869, 291, 458, 457, 754, 498, 291,
  434, 1228, 257, 51704], "temperature": 0.0, "avg_logprob": -0.08208456493559338,
  "compression_ratio": 1.9308943089430894, "no_speech_prob": 0.0008439552038908005},
  {"id": 306, "seek": 208136, "start": 2081.36, "end": 2086.4, "text": " passion to
  see know if you''re using Westbar you know you need to have kind of some investment
  of", "tokens": [50364, 5418, 281, 536, 458, 498, 291, 434, 1228, 4055, 5356, 291,
  458, 291, 643, 281, 362, 733, 295, 512, 6078, 295, 50616], "temperature": 0.0, "avg_logprob":
  -0.14800088447436952, "compression_ratio": 1.8918918918918919, "no_speech_prob":
  0.001226239139214158}, {"id": 307, "seek": 208136, "start": 2086.4, "end": 2090.96,
  "text": " actually getting great results and that the same thing if you''re using
  like a vector search library or", "tokens": [50616, 767, 1242, 869, 3542, 293, 300,
  264, 912, 551, 498, 291, 434, 1228, 411, 257, 8062, 3164, 6405, 420, 50844], "temperature":
  0.0, "avg_logprob": -0.14800088447436952, "compression_ratio": 1.8918918918918919,
  "no_speech_prob": 0.001226239139214158}, {"id": 308, "seek": 208136, "start": 2091.76,
  "end": 2097.36, "text": " you know you need to have some kind of data pipeline for
  your documents and queries so there''s", "tokens": [50884, 291, 458, 291, 643, 281,
  362, 512, 733, 295, 1412, 15517, 337, 428, 8512, 293, 24109, 370, 456, 311, 51164],
  "temperature": 0.0, "avg_logprob": -0.14800088447436952, "compression_ratio": 1.8918918918918919,
  "no_speech_prob": 0.001226239139214158}, {"id": 309, "seek": 208136, "start": 2097.92,
  "end": 2104.2400000000002, "text": " you know I''m not a huge believer in you know
  none of these technologies really work that well you", "tokens": [51192, 291, 458,
  286, 478, 406, 257, 2603, 23892, 294, 291, 458, 6022, 295, 613, 7943, 534, 589,
  300, 731, 291, 51508], "temperature": 0.0, "avg_logprob": -0.14800088447436952,
  "compression_ratio": 1.8918918918918919, "no_speech_prob": 0.001226239139214158},
  {"id": 310, "seek": 208136, "start": 2104.2400000000002, "end": 2109.36, "text":
  " know out of the box you know it''s it''s such as definitely not a sole problem
  and even if you look", "tokens": [51508, 458, 484, 295, 264, 2424, 291, 458, 309,
  311, 309, 311, 1270, 382, 2138, 406, 257, 12321, 1154, 293, 754, 498, 291, 574,
  51764], "temperature": 0.0, "avg_logprob": -0.14800088447436952, "compression_ratio":
  1.8918918918918919, "no_speech_prob": 0.001226239139214158}, {"id": 311, "seek":
  210936, "start": 2109.36, "end": 2113.6, "text": " at Google you know they''re struggling
  as well you know there are many queries of question answering", "tokens": [50364,
  412, 3329, 291, 458, 436, 434, 9314, 382, 731, 291, 458, 456, 366, 867, 24109, 295,
  1168, 13430, 50576], "temperature": 0.0, "avg_logprob": -0.1325650920038638, "compression_ratio":
  1.9453125, "no_speech_prob": 0.0014266303041949868}, {"id": 312, "seek": 210936,
  "start": 2113.6, "end": 2118.7200000000003, "text": " and so on that they totally
  get wrong you know and people want to build Google but they have like", "tokens":
  [50576, 293, 370, 322, 300, 436, 3879, 483, 2085, 291, 458, 293, 561, 528, 281,
  1322, 3329, 457, 436, 362, 411, 50832], "temperature": 0.0, "avg_logprob": -0.1325650920038638,
  "compression_ratio": 1.9453125, "no_speech_prob": 0.0014266303041949868}, {"id":
  313, "seek": 210936, "start": 2118.7200000000003, "end": 2126.32, "text": " maybe
  two guys you know or or girls you know working on search you know you you you don''t
  build a great", "tokens": [50832, 1310, 732, 1074, 291, 458, 420, 420, 4519, 291,
  458, 1364, 322, 3164, 291, 458, 291, 291, 291, 500, 380, 1322, 257, 869, 51212],
  "temperature": 0.0, "avg_logprob": -0.1325650920038638, "compression_ratio": 1.9453125,
  "no_speech_prob": 0.0014266303041949868}, {"id": 314, "seek": 210936, "start": 2126.32,
  "end": 2132.4, "text": " search experience you know if you''re by a team of two
  two people yeah yeah it''s a huge investment", "tokens": [51212, 3164, 1752, 291,
  458, 498, 291, 434, 538, 257, 1469, 295, 732, 732, 561, 1338, 1338, 309, 311, 257,
  2603, 6078, 51516], "temperature": 0.0, "avg_logprob": -0.1325650920038638, "compression_ratio":
  1.9453125, "no_speech_prob": 0.0014266303041949868}, {"id": 315, "seek": 210936,
  "start": 2132.4, "end": 2139.28, "text": " and also like time investment not just
  like you need to hire a lot of smart people but you need to", "tokens": [51516,
  293, 611, 411, 565, 6078, 406, 445, 411, 291, 643, 281, 11158, 257, 688, 295, 4069,
  561, 457, 291, 643, 281, 51860], "temperature": 0.0, "avg_logprob": -0.1325650920038638,
  "compression_ratio": 1.9453125, "no_speech_prob": 0.0014266303041949868}, {"id":
  316, "seek": 213928, "start": 2139.28, "end": 2144.8, "text": " give them time to
  actually go through all these challenges and you know now that you''ve mentioned",
  "tokens": [50364, 976, 552, 565, 281, 767, 352, 807, 439, 613, 4759, 293, 291, 458,
  586, 300, 291, 600, 2835, 50640], "temperature": 0.0, "avg_logprob": -0.08299543857574462,
  "compression_ratio": 1.7824074074074074, "no_speech_prob": 0.0021586879156529903},
  {"id": 317, "seek": 213928, "start": 2144.8, "end": 2151.76, "text": " vector search
  I''m actually curious like when in Westbar journey you know did you first hear about",
  "tokens": [50640, 8062, 3164, 286, 478, 767, 6369, 411, 562, 294, 4055, 5356, 4671,
  291, 458, 630, 291, 700, 1568, 466, 50988], "temperature": 0.0, "avg_logprob": -0.08299543857574462,
  "compression_ratio": 1.7824074074074074, "no_speech_prob": 0.0021586879156529903},
  {"id": 318, "seek": 213928, "start": 2151.76, "end": 2156.2400000000002, "text":
  " vector search and actually what caught your eye and you know like sometimes even
  today when", "tokens": [50988, 8062, 3164, 293, 767, 437, 5415, 428, 3313, 293,
  291, 458, 411, 2171, 754, 965, 562, 51212], "temperature": 0.0, "avg_logprob": -0.08299543857574462,
  "compression_ratio": 1.7824074074074074, "no_speech_prob": 0.0021586879156529903},
  {"id": 319, "seek": 213928, "start": 2156.2400000000002, "end": 2161.36, "text":
  " companies evaluate whether or not to take the neural search journey or stay with
  this part search", "tokens": [51212, 3431, 13059, 1968, 420, 406, 281, 747, 264,
  18161, 3164, 4671, 420, 1754, 365, 341, 644, 3164, 51468], "temperature": 0.0, "avg_logprob":
  -0.08299543857574462, "compression_ratio": 1.7824074074074074, "no_speech_prob":
  0.0021586879156529903}, {"id": 320, "seek": 216136, "start": 2161.6, "end": 2169.36,
  "text": " journey it is not that obvious actually and and maybe you could share
  some advice there as well but", "tokens": [50376, 4671, 309, 307, 406, 300, 6322,
  767, 293, 293, 1310, 291, 727, 2073, 512, 5192, 456, 382, 731, 457, 50764], "temperature":
  0.0, "avg_logprob": -0.13622127260480607, "compression_ratio": 1.620879120879121,
  "no_speech_prob": 0.003026058431714773}, {"id": 321, "seek": 216136, "start": 2169.36,
  "end": 2180.2400000000002, "text": " maybe first if you could also do a historical
  deep dive there super exciting yeah it''s it''s so we''ve", "tokens": [50764, 1310,
  700, 498, 291, 727, 611, 360, 257, 8584, 2452, 9192, 456, 1687, 4670, 1338, 309,
  311, 309, 311, 370, 321, 600, 51308], "temperature": 0.0, "avg_logprob": -0.13622127260480607,
  "compression_ratio": 1.620879120879121, "no_speech_prob": 0.003026058431714773},
  {"id": 322, "seek": 216136, "start": 2180.2400000000002, "end": 2186.96, "text":
  " been using like dog products and so on for search but it''s been it''s been brute
  force right so", "tokens": [51308, 668, 1228, 411, 3000, 3383, 293, 370, 322, 337,
  3164, 457, 309, 311, 668, 309, 311, 668, 47909, 3464, 558, 370, 51644], "temperature":
  0.0, "avg_logprob": -0.13622127260480607, "compression_ratio": 1.620879120879121,
  "no_speech_prob": 0.003026058431714773}, {"id": 323, "seek": 218696, "start": 2187.44,
  "end": 2196.48, "text": " been able to do brute force vector search in Westbar for
  a long time and then in 2018", "tokens": [50388, 668, 1075, 281, 360, 47909, 3464,
  8062, 3164, 294, 4055, 5356, 337, 257, 938, 565, 293, 550, 294, 6096, 50840], "temperature":
  0.0, "avg_logprob": -0.20160357157389322, "compression_ratio": 1.3656716417910448,
  "no_speech_prob": 0.0004122816026210785}, {"id": 324, "seek": 218696, "start": 2197.84,
  "end": 2208.56, "text": " bird came out and in January 2019 the researchers published
  really great results on them as Marco", "tokens": [50908, 5255, 1361, 484, 293,
  294, 7061, 6071, 264, 10309, 6572, 534, 869, 3542, 322, 552, 382, 26535, 51444],
  "temperature": 0.0, "avg_logprob": -0.20160357157389322, "compression_ratio": 1.3656716417910448,
  "no_speech_prob": 0.0004122816026210785}, {"id": 325, "seek": 220856, "start": 2208.56,
  "end": 2216.24, "text": " Pasadranking and then we like you know this is this bird
  model you know how can we use it you know", "tokens": [50364, 14199, 345, 20479,
  278, 293, 550, 321, 411, 291, 458, 341, 307, 341, 5255, 2316, 291, 458, 577, 393,
  321, 764, 309, 291, 458, 50748], "temperature": 0.0, "avg_logprob": -0.15139446258544922,
  "compression_ratio": 1.95, "no_speech_prob": 0.0015901551814749837}, {"id": 326,
  "seek": 220856, "start": 2216.24, "end": 2221.2, "text": " is it you know there
  are a lot of things you know to get your head around you know what its bird is",
  "tokens": [50748, 307, 309, 291, 458, 456, 366, 257, 688, 295, 721, 291, 458, 281,
  483, 428, 1378, 926, 291, 458, 437, 1080, 5255, 307, 50996], "temperature": 0.0,
  "avg_logprob": -0.15139446258544922, "compression_ratio": 1.95, "no_speech_prob":
  0.0015901551814749837}, {"id": 327, "seek": 220856, "start": 2221.2, "end": 2227.36,
  "text": " and how to use it and then we saw that there basically were two ways of
  of using it either as", "tokens": [50996, 293, 577, 281, 764, 309, 293, 550, 321,
  1866, 300, 456, 1936, 645, 732, 2098, 295, 295, 1228, 309, 2139, 382, 51304], "temperature":
  0.0, "avg_logprob": -0.15139446258544922, "compression_ratio": 1.95, "no_speech_prob":
  0.0015901551814749837}, {"id": 328, "seek": 220856, "start": 2227.36, "end": 2233.12,
  "text": " a representation model where you encode the query and the document independently
  and then you can", "tokens": [51304, 257, 10290, 2316, 689, 291, 2058, 1429, 264,
  14581, 293, 264, 4166, 21761, 293, 550, 291, 393, 51592], "temperature": 0.0, "avg_logprob":
  -0.15139446258544922, "compression_ratio": 1.95, "no_speech_prob": 0.0015901551814749837},
  {"id": 329, "seek": 223312, "start": 2233.2, "end": 2239.52, "text": " build using
  a vector search library you can you build the index of your corpus and then you
  can", "tokens": [50368, 1322, 1228, 257, 8062, 3164, 6405, 291, 393, 291, 1322,
  264, 8186, 295, 428, 1181, 31624, 293, 550, 291, 393, 50684], "temperature": 0.0,
  "avg_logprob": -0.23999903575483575, "compression_ratio": 1.6506550218340612, "no_speech_prob":
  0.0010553663596510887}, {"id": 330, "seek": 223312, "start": 2239.52, "end": 2245.68,
  "text": " retrieve pretty efficiently if you have La Crocs Med Search version so
  that actually was what", "tokens": [50684, 30254, 1238, 19621, 498, 291, 362, 2369,
  18965, 14368, 3982, 17180, 3037, 370, 300, 767, 390, 437, 50992], "temperature":
  0.0, "avg_logprob": -0.23999903575483575, "compression_ratio": 1.6506550218340612,
  "no_speech_prob": 0.0010553663596510887}, {"id": 331, "seek": 223312, "start": 2245.68,
  "end": 2253.44, "text": " motivated us in 2019 we started that work in summer August
  to actually have vector search and then", "tokens": [50992, 14515, 505, 294, 6071,
  321, 1409, 300, 589, 294, 4266, 6897, 281, 767, 362, 8062, 3164, 293, 550, 51380],
  "temperature": 0.0, "avg_logprob": -0.23999903575483575, "compression_ratio": 1.6506550218340612,
  "no_speech_prob": 0.0010553663596510887}, {"id": 332, "seek": 223312, "start": 2254.08,
  "end": 2260.3199999999997, "text": " also in term in Java there are a couple of
  image search use cases around hamming distance", "tokens": [51412, 611, 294, 1433,
  294, 10745, 456, 366, 257, 1916, 295, 3256, 3164, 764, 3331, 926, 36600, 278, 4560,
  51724], "temperature": 0.0, "avg_logprob": -0.23999903575483575, "compression_ratio":
  1.6506550218340612, "no_speech_prob": 0.0010553663596510887}, {"id": 333, "seek":
  226032, "start": 2260.8, "end": 2267.04, "text": " so they were pushing for that
  so there are multiple things and also our users it was open source by", "tokens":
  [50388, 370, 436, 645, 7380, 337, 300, 370, 456, 366, 3866, 721, 293, 611, 527,
  5022, 309, 390, 1269, 4009, 538, 50700], "temperature": 0.0, "avg_logprob": -0.15801701338394827,
  "compression_ratio": 1.7808219178082192, "no_speech_prob": 0.001198856974951923},
  {"id": 334, "seek": 226032, "start": 2267.04, "end": 2272.32, "text": " then so
  users were also asking for it you know can Westbar do vector search you know we
  see that we", "tokens": [50700, 550, 370, 5022, 645, 611, 3365, 337, 309, 291, 458,
  393, 4055, 5356, 360, 8062, 3164, 291, 458, 321, 536, 300, 321, 50964], "temperature":
  0.0, "avg_logprob": -0.15801701338394827, "compression_ratio": 1.7808219178082192,
  "no_speech_prob": 0.001198856974951923}, {"id": 335, "seek": 226032, "start": 2272.32,
  "end": 2278.4, "text": " could represent vectors but it''s not that cost efficient
  if we need to do brute force so then we", "tokens": [50964, 727, 2906, 18875, 457,
  309, 311, 406, 300, 2063, 7148, 498, 321, 643, 281, 360, 47909, 3464, 370, 550,
  321, 51268], "temperature": 0.0, "avg_logprob": -0.15801701338394827, "compression_ratio":
  1.7808219178082192, "no_speech_prob": 0.001198856974951923}, {"id": 336, "seek":
  226032, "start": 2278.4, "end": 2284.0, "text": " start looking at you know it and
  we had all the kind of building pieces we had the tensor the", "tokens": [51268,
  722, 1237, 412, 291, 458, 309, 293, 321, 632, 439, 264, 733, 295, 2390, 3755, 321,
  632, 264, 40863, 264, 51548], "temperature": 0.0, "avg_logprob": -0.15801701338394827,
  "compression_ratio": 1.7808219178082192, "no_speech_prob": 0.001198856974951923},
  {"id": 337, "seek": 228400, "start": 2284.0, "end": 2290.72, "text": " document
  models representing floats and all these numeric fields and so so we had it wasn''t
  a lot", "tokens": [50364, 4166, 5245, 13460, 37878, 293, 439, 613, 7866, 299, 7909,
  293, 370, 370, 321, 632, 309, 2067, 380, 257, 688, 50700], "temperature": 0.0, "avg_logprob":
  -0.11810681960161995, "compression_ratio": 1.6478260869565218, "no_speech_prob":
  0.0007994991610758007}, {"id": 338, "seek": 228400, "start": 2290.72, "end": 2297.28,
  "text": " of work to get all the kind of pieces together but we had to implement
  the algorithm and we did", "tokens": [50700, 295, 589, 281, 483, 439, 264, 733,
  295, 3755, 1214, 457, 321, 632, 281, 4445, 264, 9284, 293, 321, 630, 51028], "temperature":
  0.0, "avg_logprob": -0.11810681960161995, "compression_ratio": 1.6478260869565218,
  "no_speech_prob": 0.0007994991610758007}, {"id": 339, "seek": 228400, "start": 2298.0,
  "end": 2304.16, "text": " we did a pretty I think like one month where we actually
  surveyed multiple algorithms for", "tokens": [51064, 321, 630, 257, 1238, 286, 519,
  411, 472, 1618, 689, 321, 767, 8984, 292, 3866, 14642, 337, 51372], "temperature":
  0.0, "avg_logprob": -0.11810681960161995, "compression_ratio": 1.6478260869565218,
  "no_speech_prob": 0.0007994991610758007}, {"id": 340, "seek": 228400, "start": 2305.2,
  "end": 2310.88, "text": " approximate vector search you know how could they fit
  into the Westbar model of doing things so", "tokens": [51424, 30874, 8062, 3164,
  291, 458, 577, 727, 436, 3318, 666, 264, 4055, 5356, 2316, 295, 884, 721, 370, 51708],
  "temperature": 0.0, "avg_logprob": -0.11810681960161995, "compression_ratio": 1.6478260869565218,
  "no_speech_prob": 0.0007994991610758007}, {"id": 341, "seek": 231088, "start": 2310.88,
  "end": 2316.2400000000002, "text": " that''s the background of kind of why why vector
  search came to Westbar and I was really", "tokens": [50364, 300, 311, 264, 3678,
  295, 733, 295, 983, 983, 8062, 3164, 1361, 281, 4055, 5356, 293, 286, 390, 534,
  50632], "temperature": 0.0, "avg_logprob": -0.15628110278736462, "compression_ratio":
  1.6902654867256637, "no_speech_prob": 0.002095071831718087}, {"id": 342, "seek":
  231088, "start": 2316.2400000000002, "end": 2321.44, "text": " exciting when we
  started working on that because there were a lot of interest in it right so there
  were", "tokens": [50632, 4670, 562, 321, 1409, 1364, 322, 300, 570, 456, 645, 257,
  688, 295, 1179, 294, 309, 558, 370, 456, 645, 50892], "temperature": 0.0, "avg_logprob":
  -0.15628110278736462, "compression_ratio": 1.6902654867256637, "no_speech_prob":
  0.002095071831718087}, {"id": 343, "seek": 231088, "start": 2321.44, "end": 2326.48,
  "text": " people wanted to work on that project so yeah of course because it''s
  something like a bleeding edge", "tokens": [50892, 561, 1415, 281, 589, 322, 300,
  1716, 370, 1338, 295, 1164, 570, 309, 311, 746, 411, 257, 19312, 4691, 51144], "temperature":
  0.0, "avg_logprob": -0.15628110278736462, "compression_ratio": 1.6902654867256637,
  "no_speech_prob": 0.002095071831718087}, {"id": 344, "seek": 231088, "start": 2326.48,
  "end": 2334.1600000000003, "text": " and like a new but also like one of the podcasts
  I mentioned I think it was also with Yuri", "tokens": [51144, 293, 411, 257, 777,
  457, 611, 411, 472, 295, 264, 24045, 286, 2835, 286, 519, 309, 390, 611, 365, 33901,
  51528], "temperature": 0.0, "avg_logprob": -0.15628110278736462, "compression_ratio":
  1.6902654867256637, "no_speech_prob": 0.002095071831718087}, {"id": 345, "seek":
  233416, "start": 2334.16, "end": 2341.12, "text": " Malkov that I''ve I''ve had
  a friend who worked in essentially vector search but he was a mathematician", "tokens":
  [50364, 376, 667, 5179, 300, 286, 600, 286, 600, 632, 257, 1277, 567, 2732, 294,
  4476, 8062, 3164, 457, 415, 390, 257, 48281, 50712], "temperature": 0.0, "avg_logprob":
  -0.119738208546358, "compression_ratio": 1.7161572052401746, "no_speech_prob": 0.01538281049579382},
  {"id": 346, "seek": 233416, "start": 2341.12, "end": 2347.44, "text": " himself
  right so I also viewed it as a pure mathematical concept and I was like yeah he''s
  playing", "tokens": [50712, 3647, 558, 370, 286, 611, 19174, 309, 382, 257, 6075,
  18894, 3410, 293, 286, 390, 411, 1338, 415, 311, 2433, 51028], "temperature": 0.0,
  "avg_logprob": -0.119738208546358, "compression_ratio": 1.7161572052401746, "no_speech_prob":
  0.01538281049579382}, {"id": 347, "seek": 233416, "start": 2347.44, "end": 2352.64,
  "text": " with some theoretical you know advancements and then he actually gave
  a talk at Google you know", "tokens": [51028, 365, 512, 20864, 291, 458, 7295, 1117,
  293, 550, 415, 767, 2729, 257, 751, 412, 3329, 291, 458, 51288], "temperature":
  0.0, "avg_logprob": -0.119738208546358, "compression_ratio": 1.7161572052401746,
  "no_speech_prob": 0.01538281049579382}, {"id": 348, "seek": 233416, "start": 2352.64,
  "end": 2357.44, "text": " as well actually presenting this algorithm and the nearest
  neighbor search essentially and how to", "tokens": [51288, 382, 731, 767, 15578,
  341, 9284, 293, 264, 23831, 5987, 3164, 4476, 293, 577, 281, 51528], "temperature":
  0.0, "avg_logprob": -0.119738208546358, "compression_ratio": 1.7161572052401746,
  "no_speech_prob": 0.01538281049579382}, {"id": 349, "seek": 235744, "start": 2357.44,
  "end": 2364.48, "text": " optimize it and even then I wasn''t like essentially buying
  in and like okay it''s still mathematics", "tokens": [50364, 19719, 309, 293, 754,
  550, 286, 2067, 380, 411, 4476, 6382, 294, 293, 411, 1392, 309, 311, 920, 18666,
  50716], "temperature": 0.0, "avg_logprob": -0.07550488236129925, "compression_ratio":
  1.6899563318777293, "no_speech_prob": 0.00816343817859888}, {"id": 350, "seek":
  235744, "start": 2364.48, "end": 2372.08, "text": " but then when I was reading
  H&SW paper I saw them citing his work I was like wow so now these", "tokens": [50716,
  457, 550, 562, 286, 390, 3760, 389, 5, 50, 54, 3035, 286, 1866, 552, 48749, 702,
  589, 286, 390, 411, 6076, 370, 586, 613, 51096], "temperature": 0.0, "avg_logprob":
  -0.07550488236129925, "compression_ratio": 1.6899563318777293, "no_speech_prob":
  0.00816343817859888}, {"id": 351, "seek": 235744, "start": 2372.08, "end": 2377.92,
  "text": " paths have intersected so now this makes sense and you know usually it
  excites me when it''s put", "tokens": [51096, 14518, 362, 27815, 292, 370, 586,
  341, 1669, 2020, 293, 291, 458, 2673, 309, 1624, 3324, 385, 562, 309, 311, 829,
  51388], "temperature": 0.0, "avg_logprob": -0.07550488236129925, "compression_ratio":
  1.6899563318777293, "no_speech_prob": 0.00816343817859888}, {"id": 352, "seek":
  235744, "start": 2377.92, "end": 2385.68, "text": " into practice is that how you
  felt as well like was mathematics aspect of it like engaging for you", "tokens":
  [51388, 666, 3124, 307, 300, 577, 291, 2762, 382, 731, 411, 390, 18666, 4171, 295,
  309, 411, 11268, 337, 291, 51776], "temperature": 0.0, "avg_logprob": -0.07550488236129925,
  "compression_ratio": 1.6899563318777293, "no_speech_prob": 0.00816343817859888},
  {"id": 353, "seek": 238568, "start": 2385.68, "end": 2393.3599999999997, "text":
  " or did you view it more like an engineering sort of yeah I''m definitely on the
  engineering side", "tokens": [50364, 420, 630, 291, 1910, 309, 544, 411, 364, 7043,
  1333, 295, 1338, 286, 478, 2138, 322, 264, 7043, 1252, 50748], "temperature": 0.0,
  "avg_logprob": -0.12282318904482085, "compression_ratio": 1.8613861386138615, "no_speech_prob":
  0.0004701754660345614}, {"id": 354, "seek": 238568, "start": 2393.3599999999997,
  "end": 2399.8399999999997, "text": " so I''m definitely on the engineering side
  so for example on transformers you know I don''t care", "tokens": [50748, 370, 286,
  478, 2138, 322, 264, 7043, 1252, 370, 337, 1365, 322, 4088, 433, 291, 458, 286,
  500, 380, 1127, 51072], "temperature": 0.0, "avg_logprob": -0.12282318904482085,
  "compression_ratio": 1.8613861386138615, "no_speech_prob": 0.0004701754660345614},
  {"id": 355, "seek": 238568, "start": 2399.8399999999997, "end": 2405.6, "text":
  " about the deep neural network architecture how these interacts you know I basically
  treat", "tokens": [51072, 466, 264, 2452, 18161, 3209, 9482, 577, 613, 43582, 291,
  458, 286, 1936, 2387, 51360], "temperature": 0.0, "avg_logprob": -0.12282318904482085,
  "compression_ratio": 1.8613861386138615, "no_speech_prob": 0.0004701754660345614},
  {"id": 356, "seek": 238568, "start": 2405.6, "end": 2410.7999999999997, "text":
  " as a black box you know this is this is the box and you need a tokenizer for it
  okay what''s the", "tokens": [51360, 382, 257, 2211, 2424, 291, 458, 341, 307, 341,
  307, 264, 2424, 293, 291, 643, 257, 14862, 6545, 337, 309, 1392, 437, 311, 264,
  51620], "temperature": 0.0, "avg_logprob": -0.12282318904482085, "compression_ratio":
  1.8613861386138615, "no_speech_prob": 0.0004701754660345614}, {"id": 357, "seek":
  241080, "start": 2410.8, "end": 2417.04, "text": " tokenizer what''s saying people''s
  output what can I use it for you know I''m not gonna do and they", "tokens": [50364,
  14862, 6545, 437, 311, 1566, 561, 311, 5598, 437, 393, 286, 764, 309, 337, 291,
  458, 286, 478, 406, 799, 360, 293, 436, 50676], "temperature": 0.0, "avg_logprob":
  -0.22658492706634187, "compression_ratio": 1.6455696202531647, "no_speech_prob":
  0.0003873474197462201}, {"id": 358, "seek": 241080, "start": 2417.04, "end": 2422.8,
  "text": " be I mean a lot of research actually study you know how can we build ultimate
  in neural network", "tokens": [50676, 312, 286, 914, 257, 688, 295, 2132, 767, 2979,
  291, 458, 577, 393, 321, 1322, 9705, 294, 18161, 3209, 50964], "temperature": 0.0,
  "avg_logprob": -0.22658492706634187, "compression_ratio": 1.6455696202531647, "no_speech_prob":
  0.0003873474197462201}, {"id": 359, "seek": 241080, "start": 2422.8, "end": 2429.2000000000003,
  "text": " architecture so definitely know from for me that was not the math involved
  but we we have some people", "tokens": [50964, 9482, 370, 2138, 458, 490, 337, 385,
  300, 390, 406, 264, 5221, 3288, 457, 321, 321, 362, 512, 561, 51284], "temperature":
  0.0, "avg_logprob": -0.22658492706634187, "compression_ratio": 1.6455696202531647,
  "no_speech_prob": 0.0003873474197462201}, {"id": 360, "seek": 241080, "start": 2429.2000000000003,
  "end": 2434.96, "text": " in our team with a heavy math background and you know
  they can teach me a little bit about what", "tokens": [51284, 294, 527, 1469, 365,
  257, 4676, 5221, 3678, 293, 291, 458, 436, 393, 2924, 385, 257, 707, 857, 466, 437,
  51572], "temperature": 0.0, "avg_logprob": -0.22658492706634187, "compression_ratio":
  1.6455696202531647, "no_speech_prob": 0.0003873474197462201}, {"id": 361, "seek":
  243496, "start": 2434.96, "end": 2441.04, "text": " it''s a proper distance metric
  and you know why why this one work and this one work so that", "tokens": [50364,
  309, 311, 257, 2296, 4560, 20678, 293, 291, 458, 983, 983, 341, 472, 589, 293, 341,
  472, 589, 370, 300, 50668], "temperature": 0.0, "avg_logprob": -0.16876449584960937,
  "compression_ratio": 1.8269230769230769, "no_speech_prob": 0.0002527958422433585},
  {"id": 362, "seek": 243496, "start": 2441.04, "end": 2447.6, "text": " that was
  really also a learning experience for for me to engage with such core team on this
  feature", "tokens": [50668, 300, 390, 534, 611, 257, 2539, 1752, 337, 337, 385,
  281, 4683, 365, 1270, 4965, 1469, 322, 341, 4111, 50996], "temperature": 0.0, "avg_logprob":
  -0.16876449584960937, "compression_ratio": 1.8269230769230769, "no_speech_prob":
  0.0002527958422433585}, {"id": 363, "seek": 243496, "start": 2448.16, "end": 2454.16,
  "text": " and a huge discussion we had you know who was you know one of my main
  point was that you know", "tokens": [51024, 293, 257, 2603, 5017, 321, 632, 291,
  458, 567, 390, 291, 458, 472, 295, 452, 2135, 935, 390, 300, 291, 458, 51324], "temperature":
  0.0, "avg_logprob": -0.16876449584960937, "compression_ratio": 1.8269230769230769,
  "no_speech_prob": 0.0002527958422433585}, {"id": 364, "seek": 243496, "start": 2454.16,
  "end": 2460.2400000000002, "text": " we need to be able to integrate for users when
  they want to use vector search they want to have", "tokens": [51324, 321, 643, 281,
  312, 1075, 281, 13365, 337, 5022, 562, 436, 528, 281, 764, 8062, 3164, 436, 528,
  281, 362, 51628], "temperature": 0.0, "avg_logprob": -0.16876449584960937, "compression_ratio":
  1.8269230769230769, "no_speech_prob": 0.0002527958422433585}, {"id": 365, "seek":
  246024, "start": 2460.9599999999996, "end": 2466.56, "text": " filters they want
  to be able to express this in our query language so that you can combine", "tokens":
  [50400, 15995, 436, 528, 281, 312, 1075, 281, 5109, 341, 294, 527, 14581, 2856,
  370, 300, 291, 393, 10432, 50680], "temperature": 0.0, "avg_logprob": -0.11005795279214549,
  "compression_ratio": 1.8019323671497585, "no_speech_prob": 0.0026134189683943987},
  {"id": 366, "seek": 246024, "start": 2466.56, "end": 2472.4799999999996, "text":
  " the best of both worlds and and that took really some time you know to to get
  that right and that", "tokens": [50680, 264, 1151, 295, 1293, 13401, 293, 293, 300,
  1890, 534, 512, 565, 291, 458, 281, 281, 483, 300, 558, 293, 300, 50976], "temperature":
  0.0, "avg_logprob": -0.11005795279214549, "compression_ratio": 1.8019323671497585,
  "no_speech_prob": 0.0026134189683943987}, {"id": 367, "seek": 246024, "start": 2472.4799999999996,
  "end": 2477.6, "text": " was really you know really fun to see that that you actually
  can write a query and say that", "tokens": [50976, 390, 534, 291, 458, 534, 1019,
  281, 536, 300, 300, 291, 767, 393, 2464, 257, 14581, 293, 584, 300, 51232], "temperature":
  0.0, "avg_logprob": -0.11005795279214549, "compression_ratio": 1.8019323671497585,
  "no_speech_prob": 0.0026134189683943987}, {"id": 368, "seek": 246024, "start": 2478.16,
  "end": 2483.6, "text": " hey give me documents that are near in vector space then
  filter on this attribute but at the", "tokens": [51260, 4177, 976, 385, 8512, 300,
  366, 2651, 294, 8062, 1901, 550, 6608, 322, 341, 19667, 457, 412, 264, 51532], "temperature":
  0.0, "avg_logprob": -0.11005795279214549, "compression_ratio": 1.8019323671497585,
  "no_speech_prob": 0.0026134189683943987}, {"id": 369, "seek": 248360, "start": 2483.6,
  "end": 2491.2, "text": " same time also compute or retrieve based on the weekend
  query operator which you heard about", "tokens": [50364, 912, 565, 611, 14722, 420,
  30254, 2361, 322, 264, 6711, 14581, 12973, 597, 291, 2198, 466, 50744], "temperature":
  0.0, "avg_logprob": -0.14506806522966867, "compression_ratio": 1.7268518518518519,
  "no_speech_prob": 0.00020996364764869213}, {"id": 370, "seek": 248360, "start":
  2491.2, "end": 2497.44, "text": " weekend which is an optimization technique for
  doing spatial chival and that you could actually", "tokens": [50744, 6711, 597,
  307, 364, 19618, 6532, 337, 884, 23598, 417, 3576, 293, 300, 291, 727, 767, 51056],
  "temperature": 0.0, "avg_logprob": -0.14506806522966867, "compression_ratio": 1.7268518518518519,
  "no_speech_prob": 0.00020996364764869213}, {"id": 371, "seek": 248360, "start":
  2497.44, "end": 2503.44, "text": " express that in the same query and I have to
  say that I was really proud of our effort when", "tokens": [51056, 5109, 300, 294,
  264, 912, 14581, 293, 286, 362, 281, 584, 300, 286, 390, 534, 4570, 295, 527, 4630,
  562, 51356], "temperature": 0.0, "avg_logprob": -0.14506806522966867, "compression_ratio":
  1.7268518518518519, "no_speech_prob": 0.00020996364764869213}, {"id": 372, "seek":
  248360, "start": 2503.44, "end": 2509.52, "text": " when it came out with that and
  and could be able to combine it and that''s really if you look", "tokens": [51356,
  562, 309, 1361, 484, 365, 300, 293, 293, 727, 312, 1075, 281, 10432, 309, 293, 300,
  311, 534, 498, 291, 574, 51660], "temperature": 0.0, "avg_logprob": -0.14506806522966867,
  "compression_ratio": 1.7268518518518519, "no_speech_prob": 0.00020996364764869213},
  {"id": 373, "seek": 250952, "start": 2509.52, "end": 2518.0, "text": " on the future
  side I think vector search it''s been the biggest game changer for us was to actually",
  "tokens": [50364, 322, 264, 2027, 1252, 286, 519, 8062, 3164, 309, 311, 668, 264,
  3880, 1216, 22822, 337, 505, 390, 281, 767, 50788], "temperature": 0.0, "avg_logprob":
  -0.1991895916818202, "compression_ratio": 1.6946902654867257, "no_speech_prob":
  0.0013272097567096353}, {"id": 374, "seek": 250952, "start": 2518.0, "end": 2523.6,
  "text": " integrate vector search because that''s speared a lot of interest into
  VESPO yeah yeah and I can", "tokens": [50788, 13365, 8062, 3164, 570, 300, 311,
  768, 1642, 257, 688, 295, 1179, 666, 691, 2358, 34885, 1338, 1338, 293, 286, 393,
  51068], "temperature": 0.0, "avg_logprob": -0.1991895916818202, "compression_ratio":
  1.6946902654867257, "no_speech_prob": 0.0013272097567096353}, {"id": 375, "seek":
  250952, "start": 2523.6, "end": 2529.6, "text": " actually have people coming in
  you know yeah but I can imagine that vector search can still", "tokens": [51068,
  767, 362, 561, 1348, 294, 291, 458, 1338, 457, 286, 393, 3811, 300, 8062, 3164,
  393, 920, 51368], "temperature": 0.0, "avg_logprob": -0.1991895916818202, "compression_ratio":
  1.6946902654867257, "no_speech_prob": 0.0013272097567096353}, {"id": 376, "seek":
  250952, "start": 2530.48, "end": 2538.8, "text": " be useful in search as well as
  recommendation systems right yeah exactly so so and that''s one of", "tokens": [51412,
  312, 4420, 294, 3164, 382, 731, 382, 11879, 3652, 558, 1338, 2293, 370, 370, 293,
  300, 311, 472, 295, 51828], "temperature": 0.0, "avg_logprob": -0.1991895916818202,
  "compression_ratio": 1.6946902654867257, "no_speech_prob": 0.0013272097567096353},
  {"id": 377, "seek": 253880, "start": 2538.8, "end": 2545.84, "text": " the things
  that you know you see that factorization machines dot products has been used for",
  "tokens": [50364, 264, 721, 300, 291, 458, 291, 536, 300, 5952, 2144, 8379, 5893,
  3383, 575, 668, 1143, 337, 50716], "temperature": 0.0, "avg_logprob": -0.1209275045512635,
  "compression_ratio": 1.7731481481481481, "no_speech_prob": 0.00017274596029892564},
  {"id": 378, "seek": 253880, "start": 2545.84, "end": 2553.04, "text": " recommendation
  for a long time so you basically see the technology for search and recommendation",
  "tokens": [50716, 11879, 337, 257, 938, 565, 370, 291, 1936, 536, 264, 2899, 337,
  3164, 293, 11879, 51076], "temperature": 0.0, "avg_logprob": -0.1209275045512635,
  "compression_ratio": 1.7731481481481481, "no_speech_prob": 0.00017274596029892564},
  {"id": 379, "seek": 253880, "start": 2553.04, "end": 2561.36, "text": " use cases
  kind of merging into the kind of same same space technology space and for those
  type of", "tokens": [51076, 764, 3331, 733, 295, 44559, 666, 264, 733, 295, 912,
  912, 1901, 2899, 1901, 293, 337, 729, 2010, 295, 51492], "temperature": 0.0, "avg_logprob":
  -0.1209275045512635, "compression_ratio": 1.7731481481481481, "no_speech_prob":
  0.00017274596029892564}, {"id": 380, "seek": 253880, "start": 2561.36, "end": 2567.1200000000003,
  "text": " use cases I think VESPO is really strong technology and but the interesting
  thing that I want to", "tokens": [51492, 764, 3331, 286, 519, 691, 2358, 34885,
  307, 534, 2068, 2899, 293, 457, 264, 1880, 551, 300, 286, 528, 281, 51780], "temperature":
  0.0, "avg_logprob": -0.1209275045512635, "compression_ratio": 1.7731481481481481,
  "no_speech_prob": 0.00017274596029892564}, {"id": 381, "seek": 256712, "start":
  2567.12, "end": 2573.6, "text": " mention is that we have people coming in you know
  asking about VESPO thinking that it was a vector", "tokens": [50364, 2152, 307,
  300, 321, 362, 561, 1348, 294, 291, 458, 3365, 466, 691, 2358, 34885, 1953, 300,
  309, 390, 257, 8062, 50688], "temperature": 0.0, "avg_logprob": -0.09232767166629914,
  "compression_ratio": 1.7729257641921397, "no_speech_prob": 0.0006334540667012334},
  {"id": 382, "seek": 256712, "start": 2573.6, "end": 2578.64, "text": " search database
  and then they realized hey you know there''s keywords there''s ranking there''s
  a lot", "tokens": [50688, 3164, 8149, 293, 550, 436, 5334, 4177, 291, 458, 456,
  311, 21009, 456, 311, 17833, 456, 311, 257, 688, 50940], "temperature": 0.0, "avg_logprob":
  -0.09232767166629914, "compression_ratio": 1.7729257641921397, "no_speech_prob":
  0.0006334540667012334}, {"id": 383, "seek": 256712, "start": 2578.64, "end": 2584.96,
  "text": " of other features here you know so that''s been interesting for me you
  know you know I see vector search", "tokens": [50940, 295, 661, 4122, 510, 291,
  458, 370, 300, 311, 668, 1880, 337, 385, 291, 458, 291, 458, 286, 536, 8062, 3164,
  51256], "temperature": 0.0, "avg_logprob": -0.09232767166629914, "compression_ratio":
  1.7729257641921397, "no_speech_prob": 0.0006334540667012334}, {"id": 384, "seek":
  256712, "start": 2584.96, "end": 2592.0, "text": " as a feature of VESPO in this
  whole kind of serving engine but you can use for search and recommendation", "tokens":
  [51256, 382, 257, 4111, 295, 691, 2358, 34885, 294, 341, 1379, 733, 295, 8148, 2848,
  457, 291, 393, 764, 337, 3164, 293, 11879, 51608], "temperature": 0.0, "avg_logprob":
  -0.09232767166629914, "compression_ratio": 1.7729257641921397, "no_speech_prob":
  0.0006334540667012334}, {"id": 385, "seek": 259200, "start": 2592.56, "end": 2599.04,
  "text": " not like I see vector search as a very important feature but it''s like
  one feature of VESPO", "tokens": [50392, 406, 411, 286, 536, 8062, 3164, 382, 257,
  588, 1021, 4111, 457, 309, 311, 411, 472, 4111, 295, 691, 2358, 34885, 50716], "temperature":
  0.0, "avg_logprob": -0.11946787779358611, "compression_ratio": 1.644736842105263,
  "no_speech_prob": 0.0026857887860387564}, {"id": 386, "seek": 259200, "start": 2599.6,
  "end": 2604.56, "text": " yeah I have to admit that part I probably played that
  role in bringing those users onto you", "tokens": [50744, 1338, 286, 362, 281, 9796,
  300, 644, 286, 1391, 3737, 300, 3090, 294, 5062, 729, 5022, 3911, 291, 50992], "temperature":
  0.0, "avg_logprob": -0.11946787779358611, "compression_ratio": 1.644736842105263,
  "no_speech_prob": 0.0026857887860387564}, {"id": 387, "seek": 259200, "start": 2605.2,
  "end": 2609.92, "text": " through that blog post that I will of course mention and
  did mention multiple times and where", "tokens": [51024, 807, 300, 6968, 2183, 300,
  286, 486, 295, 1164, 2152, 293, 630, 2152, 3866, 1413, 293, 689, 51260], "temperature":
  0.0, "avg_logprob": -0.11946787779358611, "compression_ratio": 1.644736842105263,
  "no_speech_prob": 0.0026857887860387564}, {"id": 388, "seek": 259200, "start": 2609.92,
  "end": 2616.32, "text": " I compare multiple you know now seven vector databases
  and I did put VESPO in that corner just to", "tokens": [51260, 286, 6794, 3866,
  291, 458, 586, 3407, 8062, 22380, 293, 286, 630, 829, 691, 2358, 34885, 294, 300,
  4538, 445, 281, 51580], "temperature": 0.0, "avg_logprob": -0.11946787779358611,
  "compression_ratio": 1.644736842105263, "no_speech_prob": 0.0026857887860387564},
  {"id": 389, "seek": 261632, "start": 2616.32, "end": 2622.56, "text": " consider
  only the vector part but I knew that you guys over a lot more and actually still
  learn", "tokens": [50364, 1949, 787, 264, 8062, 644, 457, 286, 2586, 300, 291, 1074,
  670, 257, 688, 544, 293, 767, 920, 1466, 50676], "temperature": 0.0, "avg_logprob":
  -0.07114389330841774, "compression_ratio": 1.6782608695652175, "no_speech_prob":
  0.001639834139496088}, {"id": 390, "seek": 261632, "start": 2622.56, "end": 2627.52,
  "text": " at some point hopefully we''ll use VESPO in some project that I can actually
  evaluate but yeah", "tokens": [50676, 412, 512, 935, 4696, 321, 603, 764, 691, 2358,
  34885, 294, 512, 1716, 300, 286, 393, 767, 13059, 457, 1338, 50924], "temperature":
  0.0, "avg_logprob": -0.07114389330841774, "compression_ratio": 1.6782608695652175,
  "no_speech_prob": 0.001639834139496088}, {"id": 391, "seek": 261632, "start": 2627.52,
  "end": 2633.04, "text": " you absolutely right that some of these systems are actually
  beyond just vector search and you know", "tokens": [50924, 291, 3122, 558, 300,
  512, 295, 613, 3652, 366, 767, 4399, 445, 8062, 3164, 293, 291, 458, 51200], "temperature":
  0.0, "avg_logprob": -0.07114389330841774, "compression_ratio": 1.6782608695652175,
  "no_speech_prob": 0.001639834139496088}, {"id": 392, "seek": 261632, "start": 2633.6000000000004,
  "end": 2638.48, "text": " also the use cases like the way you view this right you
  should actually take a step back and ask", "tokens": [51228, 611, 264, 764, 3331,
  411, 264, 636, 291, 1910, 341, 558, 291, 820, 767, 747, 257, 1823, 646, 293, 1029,
  51472], "temperature": 0.0, "avg_logprob": -0.07114389330841774, "compression_ratio":
  1.6782608695652175, "no_speech_prob": 0.001639834139496088}, {"id": 393, "seek":
  263848, "start": 2638.48, "end": 2645.28, "text": " yourself what is it that you
  are trying to build yeah I think it''s really important and", "tokens": [50364,
  1803, 437, 307, 309, 300, 291, 366, 1382, 281, 1322, 1338, 286, 519, 309, 311, 534,
  1021, 293, 50704], "temperature": 0.0, "avg_logprob": -0.2550050511079676, "compression_ratio":
  1.5080213903743316, "no_speech_prob": 0.0013134075561538339}, {"id": 394, "seek":
  263848, "start": 2646.32, "end": 2653.68, "text": " so when you look at vector search
  and we didn''t so to clarify on the algorithm side after investigating", "tokens":
  [50756, 370, 562, 291, 574, 412, 8062, 3164, 293, 321, 994, 380, 370, 281, 17594,
  322, 264, 9284, 1252, 934, 22858, 51124], "temperature": 0.0, "avg_logprob": -0.2550050511079676,
  "compression_ratio": 1.5080213903743316, "no_speech_prob": 0.0013134075561538339},
  {"id": 395, "seek": 263848, "start": 2653.68, "end": 2661.04, "text": " an oil and
  several techniques we went for your emalco''s H&SW algorithm so we implemented a",
  "tokens": [51124, 364, 3184, 293, 2940, 7512, 321, 1437, 337, 428, 846, 304, 1291,
  311, 389, 5, 50, 54, 9284, 370, 321, 12270, 257, 51492], "temperature": 0.0, "avg_logprob":
  -0.2550050511079676, "compression_ratio": 1.5080213903743316, "no_speech_prob":
  0.0013134075561538339}, {"id": 396, "seek": 266104, "start": 2661.04, "end": 2670.88,
  "text": " version of that to be able to also handle filtering real-time updates
  and so on so but I think", "tokens": [50364, 3037, 295, 300, 281, 312, 1075, 281,
  611, 4813, 30822, 957, 12, 3766, 9205, 293, 370, 322, 370, 457, 286, 519, 50856],
  "temperature": 0.0, "avg_logprob": -0.08852616823636568, "compression_ratio": 1.4864864864864864,
  "no_speech_prob": 0.0005162590532563627}, {"id": 397, "seek": 266104, "start": 2671.52,
  "end": 2680.8, "text": " one discussion that is is not heard that often is that
  vector search when you introduce", "tokens": [50888, 472, 5017, 300, 307, 307, 406,
  2198, 300, 2049, 307, 300, 8062, 3164, 562, 291, 5366, 51352], "temperature": 0.0,
  "avg_logprob": -0.08852616823636568, "compression_ratio": 1.4864864864864864, "no_speech_prob":
  0.0005162590532563627}, {"id": 398, "seek": 266104, "start": 2680.8, "end": 2687.84,
  "text": " kind of H&SW or any technique you are losing some accuracy compared to
  the brute force right", "tokens": [51352, 733, 295, 389, 5, 50, 54, 420, 604, 6532,
  291, 366, 7027, 512, 14170, 5347, 281, 264, 47909, 3464, 558, 51704], "temperature":
  0.0, "avg_logprob": -0.08852616823636568, "compression_ratio": 1.4864864864864864,
  "no_speech_prob": 0.0005162590532563627}, {"id": 399, "seek": 268784, "start": 2688.8,
  "end": 2695.36, "text": " so for example a data set that is called SIFT one million
  documents you can do a single", "tokens": [50412, 370, 337, 1365, 257, 1412, 992,
  300, 307, 1219, 318, 12775, 51, 472, 2459, 8512, 291, 393, 360, 257, 2167, 50740],
  "temperature": 0.0, "avg_logprob": -0.1700624421585438, "compression_ratio": 1.6026785714285714,
  "no_speech_prob": 0.001758672297000885}, {"id": 400, "seek": 268784, "start": 2695.36,
  "end": 2701.6000000000004, "text": " treaded route for search over those one million
  vectors in about a hundred milliseconds", "tokens": [50740, 2192, 12777, 7955, 337,
  3164, 670, 729, 472, 2459, 18875, 294, 466, 257, 3262, 34184, 51052], "temperature":
  0.0, "avg_logprob": -0.1700624421585438, "compression_ratio": 1.6026785714285714,
  "no_speech_prob": 0.001758672297000885}, {"id": 401, "seek": 268784, "start": 2702.32,
  "end": 2710.96, "text": " right but if you do approximate then some parameters of
  H&SW you might get down to 0.1", "tokens": [51088, 558, 457, 498, 291, 360, 30874,
  550, 512, 9834, 295, 389, 5, 50, 54, 291, 1062, 483, 760, 281, 1958, 13, 16, 51520],
  "temperature": 0.0, "avg_logprob": -0.1700624421585438, "compression_ratio": 1.6026785714285714,
  "no_speech_prob": 0.001758672297000885}, {"id": 402, "seek": 268784, "start": 2710.96,
  "end": 2716.6400000000003, "text": " milliseconds as well using a library right
  so it''s a thousand times faster but by doing that you", "tokens": [51520, 34184,
  382, 731, 1228, 257, 6405, 558, 370, 309, 311, 257, 4714, 1413, 4663, 457, 538,
  884, 300, 291, 51804], "temperature": 0.0, "avg_logprob": -0.1700624421585438, "compression_ratio":
  1.6026785714285714, "no_speech_prob": 0.001758672297000885}, {"id": 403, "seek":
  271664, "start": 2716.64, "end": 2723.6, "text": " are losing some accuracy and
  that''s kind of when I see blog posts about approximate vector search", "tokens":
  [50364, 366, 7027, 512, 14170, 293, 300, 311, 733, 295, 562, 286, 536, 6968, 12300,
  466, 30874, 8062, 3164, 50712], "temperature": 0.0, "avg_logprob": -0.12471242178054083,
  "compression_ratio": 1.6054054054054054, "no_speech_prob": 0.0003434710088185966},
  {"id": 404, "seek": 271664, "start": 2723.6, "end": 2730.64, "text": " without mentioning
  the kind of trade-offs between recall and performance then I like you know", "tokens":
  [50712, 1553, 18315, 264, 733, 295, 4923, 12, 19231, 1296, 9901, 293, 3389, 550,
  286, 411, 291, 458, 51064], "temperature": 0.0, "avg_logprob": -0.12471242178054083,
  "compression_ratio": 1.6054054054054054, "no_speech_prob": 0.0003434710088185966},
  {"id": 405, "seek": 271664, "start": 2730.64, "end": 2740.08, "text": " you should
  include the recall numbers because there''s really so it''s really I think it''s
  really important", "tokens": [51064, 291, 820, 4090, 264, 9901, 3547, 570, 456,
  311, 534, 370, 309, 311, 534, 286, 519, 309, 311, 534, 1021, 51536], "temperature":
  0.0, "avg_logprob": -0.12471242178054083, "compression_ratio": 1.6054054054054054,
  "no_speech_prob": 0.0003434710088185966}, {"id": 406, "seek": 274008, "start": 2740.16,
  "end": 2746.56, "text": " for many use cases right it might be that you need to
  do use a brute force because that kind", "tokens": [50368, 337, 867, 764, 3331,
  558, 309, 1062, 312, 300, 291, 643, 281, 360, 764, 257, 47909, 3464, 570, 300, 733,
  50688], "temperature": 0.0, "avg_logprob": -0.23524654743283294, "compression_ratio":
  1.885, "no_speech_prob": 0.002460829447954893}, {"id": 407, "seek": 274008, "start":
  2746.56, "end": 2754.08, "text": " of approximative error that you introduce is
  not acceptable right so we do have use cases in", "tokens": [50688, 295, 8542, 1166,
  6713, 300, 291, 5366, 307, 406, 15513, 558, 370, 321, 360, 362, 764, 3331, 294,
  51064], "temperature": 0.0, "avg_logprob": -0.23524654743283294, "compression_ratio":
  1.885, "no_speech_prob": 0.002460829447954893}, {"id": 408, "seek": 274008, "start":
  2754.08, "end": 2759.68, "text": " now that we actually use we don''t have like
  large amount of documents that we actually use a brute", "tokens": [51064, 586,
  300, 321, 767, 764, 321, 500, 380, 362, 411, 2416, 2372, 295, 8512, 300, 321, 767,
  764, 257, 47909, 51344], "temperature": 0.0, "avg_logprob": -0.23524654743283294,
  "compression_ratio": 1.885, "no_speech_prob": 0.002460829447954893}, {"id": 409,
  "seek": 274008, "start": 2759.68, "end": 2766.16, "text": " force search and best
  but best best supports brute force search so yeah yeah okay so you can", "tokens":
  [51344, 3464, 3164, 293, 1151, 457, 1151, 1151, 9346, 47909, 3464, 3164, 370, 1338,
  1338, 1392, 370, 291, 393, 51668], "temperature": 0.0, "avg_logprob": -0.23524654743283294,
  "compression_ratio": 1.885, "no_speech_prob": 0.002460829447954893}, {"id": 410,
  "seek": 276616, "start": 2766.16, "end": 2772.24, "text": " switch and that''s the
  beauty is that since we support this you just say in the query time you can", "tokens":
  [50364, 3679, 293, 300, 311, 264, 6643, 307, 300, 1670, 321, 1406, 341, 291, 445,
  584, 294, 264, 14581, 565, 291, 393, 50668], "temperature": 0.0, "avg_logprob":
  -0.09092583212741585, "compression_ratio": 1.9014778325123152, "no_speech_prob":
  0.00034351329668425024}, {"id": 411, "seek": 276616, "start": 2772.24, "end": 2780.56,
  "text": " say approximate through your false and that means that you can take a
  query run it using a brute force", "tokens": [50668, 584, 30874, 807, 428, 7908,
  293, 300, 1355, 300, 291, 393, 747, 257, 14581, 1190, 309, 1228, 257, 47909, 3464,
  51084], "temperature": 0.0, "avg_logprob": -0.09092583212741585, "compression_ratio":
  1.9014778325123152, "no_speech_prob": 0.00034351329668425024}, {"id": 412, "seek":
  276616, "start": 2780.56, "end": 2785.2799999999997, "text": " and then you can
  compare the result for the brute force which is exact with the approximation", "tokens":
  [51084, 293, 550, 291, 393, 6794, 264, 1874, 337, 264, 47909, 3464, 597, 307, 1900,
  365, 264, 28023, 51320], "temperature": 0.0, "avg_logprob": -0.09092583212741585,
  "compression_ratio": 1.9014778325123152, "no_speech_prob": 0.00034351329668425024},
  {"id": 413, "seek": 276616, "start": 2785.8399999999997, "end": 2790.72, "text":
  " then you can compute the overlap between those two and that''s typically then
  what''s used in", "tokens": [51348, 550, 291, 393, 14722, 264, 19959, 1296, 729,
  732, 293, 300, 311, 5850, 550, 437, 311, 1143, 294, 51592], "temperature": 0.0,
  "avg_logprob": -0.09092583212741585, "compression_ratio": 1.9014778325123152, "no_speech_prob":
  0.00034351329668425024}, {"id": 414, "seek": 279072, "start": 2790.72, "end": 2797.8399999999997,
  "text": " the recall at k right so I did two blog posts on what I call billion scale
  vector search with with", "tokens": [50364, 264, 9901, 412, 350, 558, 370, 286,
  630, 732, 6968, 12300, 322, 437, 286, 818, 5218, 4373, 8062, 3164, 365, 365, 50720],
  "temperature": 0.0, "avg_logprob": -0.16294440594348278, "compression_ratio": 1.7136563876651982,
  "no_speech_prob": 0.00045209767995402217}, {"id": 415, "seek": 279072, "start":
  2797.8399999999997, "end": 2805.9199999999996, "text": " last one where I did deep
  dive I think into these kind of trade-offs because when you introduce", "tokens":
  [50720, 1036, 472, 689, 286, 630, 2452, 9192, 286, 519, 666, 613, 733, 295, 4923,
  12, 19231, 570, 562, 291, 5366, 51124], "temperature": 0.0, "avg_logprob": -0.16294440594348278,
  "compression_ratio": 1.7136563876651982, "no_speech_prob": 0.00045209767995402217},
  {"id": 416, "seek": 279072, "start": 2805.9199999999996, "end": 2811.52, "text":
  " approximate you also need to build these kind of index structures so in hnsw you
  need to build the", "tokens": [51124, 30874, 291, 611, 643, 281, 1322, 613, 733,
  295, 8186, 9227, 370, 294, 276, 3695, 86, 291, 643, 281, 1322, 264, 51404], "temperature":
  0.0, "avg_logprob": -0.16294440594348278, "compression_ratio": 1.7136563876651982,
  "no_speech_prob": 0.00045209767995402217}, {"id": 417, "seek": 279072, "start":
  2811.52, "end": 2817.6, "text": " graph right which is time and resource taking
  time you know I''m costing memory so there are all", "tokens": [51404, 4295, 558,
  597, 307, 565, 293, 7684, 1940, 565, 291, 458, 286, 478, 37917, 4675, 370, 456,
  366, 439, 51708], "temperature": 0.0, "avg_logprob": -0.16294440594348278, "compression_ratio":
  1.7136563876651982, "no_speech_prob": 0.00045209767995402217}, {"id": 418, "seek":
  281760, "start": 2817.6, "end": 2823.04, "text": " these kind of trade-offs and
  that''s generally I mean generally for search a lot of trade-offs but", "tokens":
  [50364, 613, 733, 295, 4923, 12, 19231, 293, 300, 311, 5101, 286, 914, 5101, 337,
  3164, 257, 688, 295, 4923, 12, 19231, 457, 50636], "temperature": 0.0, "avg_logprob":
  -0.23356497287750244, "compression_ratio": 1.8708133971291867, "no_speech_prob":
  0.002701298100873828}, {"id": 419, "seek": 281760, "start": 2823.04, "end": 2827.6,
  "text": " especially around vector search I call it the jack of old trade-offs because
  there''s so many things", "tokens": [50636, 2318, 926, 8062, 3164, 286, 818, 309,
  264, 7109, 295, 1331, 4923, 12, 19231, 570, 456, 311, 370, 867, 721, 50864], "temperature":
  0.0, "avg_logprob": -0.23356497287750244, "compression_ratio": 1.8708133971291867,
  "no_speech_prob": 0.002701298100873828}, {"id": 420, "seek": 281760, "start": 2827.6,
  "end": 2835.92, "text": " you know to consider you know memory usage this usage
  CPU and so on so yeah that love the term jack", "tokens": [50864, 291, 458, 281,
  1949, 291, 458, 4675, 14924, 341, 14924, 13199, 293, 370, 322, 370, 1338, 300, 959,
  264, 1433, 7109, 51280], "temperature": 0.0, "avg_logprob": -0.23356497287750244,
  "compression_ratio": 1.8708133971291867, "no_speech_prob": 0.002701298100873828},
  {"id": 421, "seek": 281760, "start": 2835.92, "end": 2843.2799999999997, "text":
  " of old feed-offs yeah but it but it really is you know you really have so many
  trade-offs and", "tokens": [51280, 295, 1331, 3154, 12, 19231, 1338, 457, 309, 457,
  309, 534, 307, 291, 458, 291, 534, 362, 370, 867, 4923, 12, 19231, 293, 51648],
  "temperature": 0.0, "avg_logprob": -0.23356497287750244, "compression_ratio": 1.8708133971291867,
  "no_speech_prob": 0.002701298100873828}, {"id": 422, "seek": 284328, "start": 2843.36,
  "end": 2849.6000000000004, "text": " some companies you know maybe you have lots
  of data but you don''t have any real tripe it right", "tokens": [50368, 512, 3431,
  291, 458, 1310, 291, 362, 3195, 295, 1412, 457, 291, 500, 380, 362, 604, 957, 1376,
  494, 309, 558, 50680], "temperature": 0.0, "avg_logprob": -0.15905709599339685,
  "compression_ratio": 1.755980861244019, "no_speech_prob": 0.0010011696722358465},
  {"id": 423, "seek": 284328, "start": 2849.6000000000004, "end": 2856.4, "text":
  " in that case maybe disk a and n or things that basically using disk is is a good
  alternative", "tokens": [50680, 294, 300, 1389, 1310, 12355, 257, 293, 297, 420,
  721, 300, 1936, 1228, 12355, 307, 307, 257, 665, 8535, 51020], "temperature": 0.0,
  "avg_logprob": -0.15905709599339685, "compression_ratio": 1.755980861244019, "no_speech_prob":
  0.0010011696722358465}, {"id": 424, "seek": 284328, "start": 2856.4, "end": 2861.76,
  "text": " because when you''re buying servers in the cloud or renting servers in
  the cloud you pay", "tokens": [51020, 570, 562, 291, 434, 6382, 15909, 294, 264,
  4588, 420, 40598, 15909, 294, 264, 4588, 291, 1689, 51288], "temperature": 0.0,
  "avg_logprob": -0.15905709599339685, "compression_ratio": 1.755980861244019, "no_speech_prob":
  0.0010011696722358465}, {"id": 425, "seek": 284328, "start": 2862.7200000000003,
  "end": 2867.92, "text": " when you want to have this amount of memory you get this
  amount of CPU right there comes in", "tokens": [51336, 562, 291, 528, 281, 362,
  341, 2372, 295, 4675, 291, 483, 341, 2372, 295, 13199, 558, 456, 1487, 294, 51596],
  "temperature": 0.0, "avg_logprob": -0.15905709599339685, "compression_ratio": 1.755980861244019,
  "no_speech_prob": 0.0010011696722358465}, {"id": 426, "seek": 286792, "start": 2868.88,
  "end": 2874.4, "text": " a relationship between the CPU and the memory and and so
  there are different trade-offs around", "tokens": [50412, 257, 2480, 1296, 264,
  13199, 293, 264, 4675, 293, 293, 370, 456, 366, 819, 4923, 12, 19231, 926, 50688],
  "temperature": 0.0, "avg_logprob": -0.13332405868841676, "compression_ratio": 1.7065217391304348,
  "no_speech_prob": 0.0007798340520821512}, {"id": 427, "seek": 286792, "start": 2874.4,
  "end": 2880.0, "text": " you know what what''s actually going to use it for you
  yeah exactly have you heard any other", "tokens": [50688, 291, 458, 437, 437, 311,
  767, 516, 281, 764, 309, 337, 291, 1338, 2293, 362, 291, 2198, 604, 661, 50968],
  "temperature": 0.0, "avg_logprob": -0.13332405868841676, "compression_ratio": 1.7065217391304348,
  "no_speech_prob": 0.0007798340520821512}, {"id": 428, "seek": 286792, "start": 2880.0,
  "end": 2884.7200000000003, "text": " misconceptions about neural search at large
  you know when somebody comes and says hey I want to", "tokens": [50968, 50012, 466,
  18161, 3164, 412, 2416, 291, 458, 562, 2618, 1487, 293, 1619, 4177, 286, 528, 281,
  51204], "temperature": 0.0, "avg_logprob": -0.13332405868841676, "compression_ratio":
  1.7065217391304348, "no_speech_prob": 0.0007798340520821512}, {"id": 429, "seek":
  286792, "start": 2884.7200000000003, "end": 2889.84, "text": " implement a question
  answering system you couldn''t principle use sparse search techniques or", "tokens":
  [51204, 4445, 257, 1168, 13430, 1185, 291, 2809, 380, 8665, 764, 637, 11668, 3164,
  7512, 420, 51460], "temperature": 0.0, "avg_logprob": -0.13332405868841676, "compression_ratio":
  1.7065217391304348, "no_speech_prob": 0.0007798340520821512}, {"id": 430, "seek":
  286792, "start": 2889.84, "end": 2894.56, "text": " like query understanding techniques
  you know to actually almost do it in the rule-based fashion", "tokens": [51460,
  411, 14581, 3701, 7512, 291, 458, 281, 767, 1920, 360, 309, 294, 264, 4978, 12,
  6032, 6700, 51696], "temperature": 0.0, "avg_logprob": -0.13332405868841676, "compression_ratio":
  1.7065217391304348, "no_speech_prob": 0.0007798340520821512}, {"id": 431, "seek":
  289456, "start": 2895.2799999999997, "end": 2902.08, "text": " but like neural search
  on the other hand is like you know new sexy stuff everyone''s to try out so", "tokens":
  [50400, 457, 411, 18161, 3164, 322, 264, 661, 1011, 307, 411, 291, 458, 777, 13701,
  1507, 1518, 311, 281, 853, 484, 370, 50740], "temperature": 0.0, "avg_logprob":
  -0.13166793532993482, "compression_ratio": 1.7174887892376682, "no_speech_prob":
  0.002555578714236617}, {"id": 432, "seek": 289456, "start": 2902.08, "end": 2908.48,
  "text": " the question is like have you heard of any misconceptions or something
  that people think it''s", "tokens": [50740, 264, 1168, 307, 411, 362, 291, 2198,
  295, 604, 50012, 420, 746, 300, 561, 519, 309, 311, 51060], "temperature": 0.0,
  "avg_logprob": -0.13166793532993482, "compression_ratio": 1.7174887892376682, "no_speech_prob":
  0.002555578714236617}, {"id": 433, "seek": 289456, "start": 2908.48, "end": 2916.88,
  "text": " much easier than it is yeah that''s that''s I mean it''s a fantastic question
  I think you know you", "tokens": [51060, 709, 3571, 813, 309, 307, 1338, 300, 311,
  300, 311, 286, 914, 309, 311, 257, 5456, 1168, 286, 519, 291, 458, 291, 51480],
  "temperature": 0.0, "avg_logprob": -0.13166793532993482, "compression_ratio": 1.7174887892376682,
  "no_speech_prob": 0.002555578714236617}, {"id": 434, "seek": 289456, "start": 2916.88,
  "end": 2922.24, "text": " can just sit back you know this is I''m relaxed for a
  few minutes because this is a topic that I", "tokens": [51480, 393, 445, 1394, 646,
  291, 458, 341, 307, 286, 478, 14628, 337, 257, 1326, 2077, 570, 341, 307, 257, 4829,
  300, 286, 51748], "temperature": 0.0, "avg_logprob": -0.13166793532993482, "compression_ratio":
  1.7174887892376682, "no_speech_prob": 0.002555578714236617}, {"id": 435, "seek":
  292224, "start": 2922.24, "end": 2929.12, "text": " really love um yeah so so so
  the first time when we if you look at semantic search especially around", "tokens":
  [50364, 534, 959, 1105, 1338, 370, 370, 370, 264, 700, 565, 562, 321, 498, 291,
  574, 412, 47982, 3164, 2318, 926, 50708], "temperature": 0.0, "avg_logprob": -0.16161622057904254,
  "compression_ratio": 1.9086538461538463, "no_speech_prob": 0.0007816168363206089},
  {"id": 436, "seek": 292224, "start": 2929.12, "end": 2935.9199999999996, "text":
  " vector search if we semantic search might mean a lot but if you look at the kind
  of the typical", "tokens": [50708, 8062, 3164, 498, 321, 47982, 3164, 1062, 914,
  257, 688, 457, 498, 291, 574, 412, 264, 733, 295, 264, 7476, 51048], "temperature":
  0.0, "avg_logprob": -0.16161622057904254, "compression_ratio": 1.9086538461538463,
  "no_speech_prob": 0.0007816168363206089}, {"id": 437, "seek": 292224, "start": 2935.9199999999996,
  "end": 2940.64, "text": " that people use semantics search today is that you have
  this vector search right you have independent", "tokens": [51048, 300, 561, 764,
  4361, 45298, 3164, 965, 307, 300, 291, 362, 341, 8062, 3164, 558, 291, 362, 6695,
  51284], "temperature": 0.0, "avg_logprob": -0.16161622057904254, "compression_ratio":
  1.9086538461538463, "no_speech_prob": 0.0007816168363206089}, {"id": 438, "seek":
  292224, "start": 2940.64, "end": 2946.7999999999997, "text": " query embedding in
  the document embedding and so and if you base this if you take them pre-trained",
  "tokens": [51284, 14581, 12240, 3584, 294, 264, 4166, 12240, 3584, 293, 370, 293,
  498, 291, 3096, 341, 498, 291, 747, 552, 659, 12, 17227, 2001, 51592], "temperature":
  0.0, "avg_logprob": -0.16161622057904254, "compression_ratio": 1.9086538461538463,
  "no_speech_prob": 0.0007816168363206089}, {"id": 439, "seek": 294680, "start": 2946.8,
  "end": 2953.6000000000004, "text": " language model from hugging phase and you just
  pull that model and then you encode your queries", "tokens": [50364, 2856, 2316,
  490, 41706, 5574, 293, 291, 445, 2235, 300, 2316, 293, 550, 291, 2058, 1429, 428,
  24109, 50704], "temperature": 0.0, "avg_logprob": -0.16031797608332848, "compression_ratio":
  1.5978260869565217, "no_speech_prob": 0.0011512160999700427}, {"id": 440, "seek":
  294680, "start": 2953.6000000000004, "end": 2961.6800000000003, "text": " using
  for instance the CLS token or the average over all tokens and the result that you
  will get", "tokens": [50704, 1228, 337, 5197, 264, 12855, 50, 14862, 420, 264, 4274,
  670, 439, 22667, 293, 264, 1874, 300, 291, 486, 483, 51108], "temperature": 0.0,
  "avg_logprob": -0.16031797608332848, "compression_ratio": 1.5978260869565217, "no_speech_prob":
  0.0011512160999700427}, {"id": 441, "seek": 294680, "start": 2961.6800000000003,
  "end": 2970.6400000000003, "text": " from that is not going to compete at all with
  the VM25 right because that language model has not been", "tokens": [51108, 490,
  300, 307, 406, 516, 281, 11831, 412, 439, 365, 264, 18038, 6074, 558, 570, 300,
  2856, 2316, 575, 406, 668, 51556], "temperature": 0.0, "avg_logprob": -0.16031797608332848,
  "compression_ratio": 1.5978260869565217, "no_speech_prob": 0.0011512160999700427},
  {"id": 442, "seek": 297064, "start": 2970.72, "end": 2977.2, "text": " it''s only
  been learned learning how to do mask language model right so it''s basically it''s
  been", "tokens": [50368, 309, 311, 787, 668, 3264, 2539, 577, 281, 360, 6094, 2856,
  2316, 558, 370, 309, 311, 1936, 309, 311, 668, 50692], "temperature": 0.0, "avg_logprob":
  -0.1080835276636584, "compression_ratio": 2.063025210084034, "no_speech_prob": 0.0019760611467063427},
  {"id": 443, "seek": 297064, "start": 2977.2, "end": 2982.16, "text": " trained on
  predicting the next word right so it''s a deep neural network that''s it''s not
  been trained", "tokens": [50692, 8895, 322, 32884, 264, 958, 1349, 558, 370, 309,
  311, 257, 2452, 18161, 3209, 300, 311, 309, 311, 406, 668, 8895, 50940], "temperature":
  0.0, "avg_logprob": -0.1080835276636584, "compression_ratio": 2.063025210084034,
  "no_speech_prob": 0.0019760611467063427}, {"id": 444, "seek": 297064, "start": 2982.16,
  "end": 2989.7599999999998, "text": " for that so it''s basically like taking some
  deep neural network for my vacuum cleaner and put it", "tokens": [50940, 337, 300,
  370, 309, 311, 1936, 411, 1940, 512, 2452, 18161, 3209, 337, 452, 14224, 16532,
  293, 829, 309, 51320], "temperature": 0.0, "avg_logprob": -0.1080835276636584, "compression_ratio":
  2.063025210084034, "no_speech_prob": 0.0019760611467063427}, {"id": 445, "seek":
  297064, "start": 2989.7599999999998, "end": 2995.52, "text": " into my car you know
  to try to try to try the car it''s not been trained for that right so that was",
  "tokens": [51320, 666, 452, 1032, 291, 458, 281, 853, 281, 853, 281, 853, 264, 1032,
  309, 311, 406, 668, 8895, 337, 300, 558, 370, 300, 390, 51608], "temperature": 0.0,
  "avg_logprob": -0.1080835276636584, "compression_ratio": 2.063025210084034, "no_speech_prob":
  0.0019760611467063427}, {"id": 446, "seek": 297064, "start": 2995.52, "end": 2999.2799999999997,
  "text": " one of the things you know when we struggled as well when they looked
  at bird and the other people", "tokens": [51608, 472, 295, 264, 721, 291, 458, 562,
  321, 19023, 382, 731, 562, 436, 2956, 412, 5255, 293, 264, 661, 561, 51796], "temperature":
  0.0, "avg_logprob": -0.1080835276636584, "compression_ratio": 2.063025210084034,
  "no_speech_prob": 0.0019760611467063427}, {"id": 447, "seek": 299928, "start": 2999.44,
  "end": 3004.32, "text": " like oh that''s so great and then we had the engine and
  we could like compare it with VM25 and then", "tokens": [50372, 411, 1954, 300,
  311, 370, 869, 293, 550, 321, 632, 264, 2848, 293, 321, 727, 411, 6794, 309, 365,
  18038, 6074, 293, 550, 50616], "temperature": 0.0, "avg_logprob": -0.15717394633959697,
  "compression_ratio": 1.6861924686192469, "no_speech_prob": 0.001105778617784381},
  {"id": 448, "seek": 299928, "start": 3004.32, "end": 3010.88, "text": " we did bird
  here and there was like these results if you look at the actual information retrieval
  benchmarks", "tokens": [50616, 321, 630, 5255, 510, 293, 456, 390, 411, 613, 3542,
  498, 291, 574, 412, 264, 3539, 1589, 19817, 3337, 43751, 50944], "temperature":
  0.0, "avg_logprob": -0.15717394633959697, "compression_ratio": 1.6861924686192469,
  "no_speech_prob": 0.001105778617784381}, {"id": 449, "seek": 299928, "start": 3010.88,
  "end": 3017.6000000000004, "text": " they''re like the results are not good they''re
  they''re like really so then came the kind of you know", "tokens": [50944, 436,
  434, 411, 264, 3542, 366, 406, 665, 436, 434, 436, 434, 411, 534, 370, 550, 1361,
  264, 733, 295, 291, 458, 51280], "temperature": 0.0, "avg_logprob": -0.15717394633959697,
  "compression_ratio": 1.6861924686192469, "no_speech_prob": 0.001105778617784381},
  {"id": 450, "seek": 299928, "start": 3017.6000000000004, "end": 3024.96, "text":
  " realization I think that''s actually happened around industry as well in 2020
  when the DPR dense", "tokens": [51280, 25138, 286, 519, 300, 311, 767, 2011, 926,
  3518, 382, 731, 294, 4808, 562, 264, 413, 15958, 18011, 51648], "temperature": 0.0,
  "avg_logprob": -0.15717394633959697, "compression_ratio": 1.6861924686192469, "no_speech_prob":
  0.001105778617784381}, {"id": 451, "seek": 302496, "start": 3024.96, "end": 3031.92,
  "text": " passage retriever paper came out from from a Facebook where they trained
  on natural questions", "tokens": [50364, 11497, 19817, 331, 3035, 1361, 484, 490,
  490, 257, 4384, 689, 436, 8895, 322, 3303, 1651, 50712], "temperature": 0.0, "avg_logprob":
  -0.1474355521954988, "compression_ratio": 1.8423645320197044, "no_speech_prob":
  0.0006372269708663225}, {"id": 452, "seek": 302496, "start": 3032.48, "end": 3037.04,
  "text": " the Google dataset they actually trained this dense retriever and the
  dense model using a", "tokens": [50740, 264, 3329, 28872, 436, 767, 8895, 341, 18011,
  19817, 331, 293, 264, 18011, 2316, 1228, 257, 50968], "temperature": 0.0, "avg_logprob":
  -0.1474355521954988, "compression_ratio": 1.8423645320197044, "no_speech_prob":
  0.0006372269708663225}, {"id": 453, "seek": 302496, "start": 3037.04, "end": 3043.12,
  "text": " contrastive loss and hard negative mining so they basically demonstrate
  you know how to actually", "tokens": [50968, 8712, 488, 4470, 293, 1152, 3671, 15512,
  370, 436, 1936, 11698, 291, 458, 577, 281, 767, 51272], "temperature": 0.0, "avg_logprob":
  -0.1474355521954988, "compression_ratio": 1.8423645320197044, "no_speech_prob":
  0.0006372269708663225}, {"id": 454, "seek": 302496, "start": 3043.12, "end": 3048.56,
  "text": " train a dense retriever model and then we actually saw the results were
  much better than than", "tokens": [51272, 3847, 257, 18011, 19817, 331, 2316, 293,
  550, 321, 767, 1866, 264, 3542, 645, 709, 1101, 813, 813, 51544], "temperature":
  0.0, "avg_logprob": -0.1474355521954988, "compression_ratio": 1.8423645320197044,
  "no_speech_prob": 0.0006372269708663225}, {"id": 455, "seek": 304856, "start": 3048.56,
  "end": 3057.2799999999997, "text": " VM25 in that but but it''s a huge so that''s
  one area where I think that people", "tokens": [50364, 18038, 6074, 294, 300, 457,
  457, 309, 311, 257, 2603, 370, 300, 311, 472, 1859, 689, 286, 519, 300, 561, 50800],
  "temperature": 0.0, "avg_logprob": -0.11676137343696925, "compression_ratio": 1.6576576576576576,
  "no_speech_prob": 0.00048137936391867697}, {"id": 456, "seek": 304856, "start":
  3058.08, "end": 3064.48, "text": " just using the pre-trained model might not work
  well especially if it''s not been tuned for retrieval", "tokens": [50840, 445, 1228,
  264, 659, 12, 17227, 2001, 2316, 1062, 406, 589, 731, 2318, 498, 309, 311, 406,
  668, 10870, 337, 19817, 3337, 51160], "temperature": 0.0, "avg_logprob": -0.11676137343696925,
  "compression_ratio": 1.6576576576576576, "no_speech_prob": 0.00048137936391867697},
  {"id": 457, "seek": 304856, "start": 3064.48, "end": 3071.04, "text": " and even
  if you look at MS Marco which is the largest data set out there that you can train",
  "tokens": [51160, 293, 754, 498, 291, 574, 412, 7395, 26535, 597, 307, 264, 6443,
  1412, 992, 484, 456, 300, 291, 393, 3847, 51488], "temperature": 0.0, "avg_logprob":
  -0.11676137343696925, "compression_ratio": 1.6576576576576576, "no_speech_prob":
  0.00048137936391867697}, {"id": 458, "seek": 304856, "start": 3071.04, "end": 3078.16,
  "text": " a model on if you train a model on MS Marco and then you apply that model
  into a different domain", "tokens": [51488, 257, 2316, 322, 498, 291, 3847, 257,
  2316, 322, 7395, 26535, 293, 550, 291, 3079, 300, 2316, 666, 257, 819, 9274, 51844],
  "temperature": 0.0, "avg_logprob": -0.11676137343696925, "compression_ratio": 1.6576576576576576,
  "no_speech_prob": 0.00048137936391867697}, {"id": 459, "seek": 307856, "start":
  3078.64, "end": 3088.08, "text": " so on a different dataset it might not outcompete
  VM25 in fact it actually in many cases it is", "tokens": [50368, 370, 322, 257,
  819, 28872, 309, 1062, 406, 484, 21541, 3498, 18038, 6074, 294, 1186, 309, 767,
  294, 867, 3331, 309, 307, 50840], "temperature": 0.0, "avg_logprob": -0.16981151077773546,
  "compression_ratio": 1.7300884955752212, "no_speech_prob": 0.0013801638269796968},
  {"id": 460, "seek": 307856, "start": 3088.08, "end": 3094.56, "text": " actually
  underperforms compared to VM25 so and that''s why there''s a lot of interest and
  especially", "tokens": [50840, 767, 833, 26765, 82, 5347, 281, 18038, 6074, 370,
  293, 300, 311, 983, 456, 311, 257, 688, 295, 1179, 293, 2318, 51164], "temperature":
  0.0, "avg_logprob": -0.16981151077773546, "compression_ratio": 1.7300884955752212,
  "no_speech_prob": 0.0013801638269796968}, {"id": 461, "seek": 307856, "start": 3095.2,
  "end": 3101.44, "text": " recently is like you know if we combine this exact matching
  you know the actual user search for", "tokens": [51196, 3938, 307, 411, 291, 458,
  498, 321, 10432, 341, 1900, 14324, 291, 458, 264, 3539, 4195, 3164, 337, 51508],
  "temperature": 0.0, "avg_logprob": -0.16981151077773546, "compression_ratio": 1.7300884955752212,
  "no_speech_prob": 0.0013801638269796968}, {"id": 462, "seek": 307856, "start": 3101.44,
  "end": 3107.6, "text": " this phrase but we also have the vector representation
  you know how to combine that and that''s that''s", "tokens": [51508, 341, 9535,
  457, 321, 611, 362, 264, 8062, 10290, 291, 458, 577, 281, 10432, 300, 293, 300,
  311, 300, 311, 51816], "temperature": 0.0, "avg_logprob": -0.16981151077773546,
  "compression_ratio": 1.7300884955752212, "no_speech_prob": 0.0013801638269796968},
  {"id": 463, "seek": 310760, "start": 3107.6, "end": 3115.44, "text": " actually
  two of my colleagues are right now working on the beer dataset to they open the
  PR to", "tokens": [50364, 767, 732, 295, 452, 7734, 366, 558, 586, 1364, 322, 264,
  8795, 28872, 281, 436, 1269, 264, 11568, 281, 50756], "temperature": 0.0, "avg_logprob":
  -0.1751697770841829, "compression_ratio": 1.5991735537190082, "no_speech_prob":
  0.0009115648572333157}, {"id": 464, "seek": 310760, "start": 3115.44, "end": 3123.2799999999997,
  "text": " the to the dataset to include VASP as well and then we will demonstrate
  some methods for combining", "tokens": [50756, 264, 281, 264, 28872, 281, 4090,
  691, 3160, 47, 382, 731, 293, 550, 321, 486, 11698, 512, 7150, 337, 21928, 51148],
  "temperature": 0.0, "avg_logprob": -0.1751697770841829, "compression_ratio": 1.5991735537190082,
  "no_speech_prob": 0.0009115648572333157}, {"id": 465, "seek": 310760, "start": 3123.2799999999997,
  "end": 3128.4, "text": " sparse and dense. Yeah that''s awesome like I''ve read
  the beer paper after you referred it to me", "tokens": [51148, 637, 11668, 293,
  18011, 13, 865, 300, 311, 3476, 411, 286, 600, 1401, 264, 8795, 3035, 934, 291,
  10839, 309, 281, 385, 51404], "temperature": 0.0, "avg_logprob": -0.1751697770841829,
  "compression_ratio": 1.5991735537190082, "no_speech_prob": 0.0009115648572333157},
  {"id": 466, "seek": 310760, "start": 3128.4, "end": 3133.2799999999997, "text":
  " actually and it was quite eye-opening because it does compare not only sort of
  like search engine", "tokens": [51404, 767, 293, 309, 390, 1596, 3313, 12, 404,
  4559, 570, 309, 775, 6794, 406, 787, 1333, 295, 411, 3164, 2848, 51648], "temperature":
  0.0, "avg_logprob": -0.1751697770841829, "compression_ratio": 1.5991735537190082,
  "no_speech_prob": 0.0009115648572333157}, {"id": 467, "seek": 313328, "start": 3133.28,
  "end": 3139.52, "text": " algorithms and approaches but also datasets and tasks
  right which different tasks like searching", "tokens": [50364, 14642, 293, 11587,
  457, 611, 42856, 293, 9608, 558, 597, 819, 9608, 411, 10808, 50676], "temperature":
  0.0, "avg_logprob": -0.08148647176808324, "compression_ratio": 1.628099173553719,
  "no_speech_prob": 0.004539810586720705}, {"id": 468, "seek": 313328, "start": 3139.52,
  "end": 3144.4, "text": " or answering questions may matter quite a lot and so it
  was quite an eye-opening that first of all", "tokens": [50676, 420, 13430, 1651,
  815, 1871, 1596, 257, 688, 293, 370, 309, 390, 1596, 364, 3313, 12, 404, 4559, 300,
  700, 295, 439, 50920], "temperature": 0.0, "avg_logprob": -0.08148647176808324,
  "compression_ratio": 1.628099173553719, "no_speech_prob": 0.004539810586720705},
  {"id": 469, "seek": 313328, "start": 3144.4, "end": 3150.8, "text": " VM25 is fairly
  competitive so it''s not a loser not at all so like you should still consider using
  it", "tokens": [50920, 18038, 6074, 307, 6457, 10043, 370, 309, 311, 406, 257, 24606,
  406, 412, 439, 370, 411, 291, 820, 920, 1949, 1228, 309, 51240], "temperature":
  0.0, "avg_logprob": -0.08148647176808324, "compression_ratio": 1.628099173553719,
  "no_speech_prob": 0.004539810586720705}, {"id": 470, "seek": 313328, "start": 3150.8,
  "end": 3156.48, "text": " like and actually maybe even keeping it as a strong baseline
  in everything you do and I know some", "tokens": [51240, 411, 293, 767, 1310, 754,
  5145, 309, 382, 257, 2068, 20518, 294, 1203, 291, 360, 293, 286, 458, 512, 51524],
  "temperature": 0.0, "avg_logprob": -0.08148647176808324, "compression_ratio": 1.628099173553719,
  "no_speech_prob": 0.004539810586720705}, {"id": 471, "seek": 315648, "start": 3156.56,
  "end": 3164.08, "text": " companies by the way still use TFIDF so maybe they should
  also like first transition to VM25", "tokens": [50368, 3431, 538, 264, 636, 920,
  764, 40964, 2777, 37, 370, 1310, 436, 820, 611, 411, 700, 6034, 281, 18038, 6074,
  50744], "temperature": 0.0, "avg_logprob": -0.1442420482635498, "compression_ratio":
  1.6637554585152838, "no_speech_prob": 0.0011167546035721898}, {"id": 472, "seek":
  315648, "start": 3164.08, "end": 3169.04, "text": " and only then jump to neural
  search techniques are like a denser trivel and and I think you also", "tokens":
  [50744, 293, 787, 550, 3012, 281, 18161, 3164, 7512, 366, 411, 257, 24505, 260,
  1376, 779, 293, 293, 286, 519, 291, 611, 50992], "temperature": 0.0, "avg_logprob":
  -0.1442420482635498, "compression_ratio": 1.6637554585152838, "no_speech_prob":
  0.0011167546035721898}, {"id": 473, "seek": 315648, "start": 3169.04, "end": 3175.2,
  "text": " mentioned that and I saw by the way that you have participated in various
  competitions on denser", "tokens": [50992, 2835, 300, 293, 286, 1866, 538, 264,
  636, 300, 291, 362, 17978, 294, 3683, 26185, 322, 24505, 260, 51300], "temperature":
  0.0, "avg_logprob": -0.1442420482635498, "compression_ratio": 1.6637554585152838,
  "no_speech_prob": 0.0011167546035721898}, {"id": 474, "seek": 315648, "start": 3175.2,
  "end": 3182.88, "text": " trivel and on ranking like can you can you elaborate a
  bit more like what drives your interest", "tokens": [51300, 1376, 779, 293, 322,
  17833, 411, 393, 291, 393, 291, 20945, 257, 857, 544, 411, 437, 11754, 428, 1179,
  51684], "temperature": 0.0, "avg_logprob": -0.1442420482635498, "compression_ratio":
  1.6637554585152838, "no_speech_prob": 0.0011167546035721898}, {"id": 475, "seek":
  318288, "start": 3182.88, "end": 3188.1600000000003, "text": " there because to
  me that sounds more like academic interest in a way right but of course", "tokens":
  [50364, 456, 570, 281, 385, 300, 3263, 544, 411, 7778, 1179, 294, 257, 636, 558,
  457, 295, 1164, 50628], "temperature": 0.0, "avg_logprob": -0.12444192513652232,
  "compression_ratio": 1.6598360655737705, "no_speech_prob": 0.0009809269104152918},
  {"id": 476, "seek": 318288, "start": 3188.1600000000003, "end": 3191.6, "text":
  " you''re also showcasing and probably bringing ideas back to that spa.", "tokens":
  [50628, 291, 434, 611, 29794, 3349, 293, 1391, 5062, 3487, 646, 281, 300, 32543,
  13, 50800], "temperature": 0.0, "avg_logprob": -0.12444192513652232, "compression_ratio":
  1.6598360655737705, "no_speech_prob": 0.0009809269104152918}, {"id": 477, "seek":
  318288, "start": 3194.0, "end": 3199.04, "text": " Yeah so the motivation was actually
  around them as Marco passage ranking and", "tokens": [50920, 865, 370, 264, 12335,
  390, 767, 926, 552, 382, 26535, 11497, 17833, 293, 51172], "temperature": 0.0, "avg_logprob":
  -0.12444192513652232, "compression_ratio": 1.6598360655737705, "no_speech_prob":
  0.0009809269104152918}, {"id": 478, "seek": 318288, "start": 3200.08, "end": 3204.56,
  "text": " where we actually could use this dataset and then our dream when we started
  to", "tokens": [51224, 689, 321, 767, 727, 764, 341, 28872, 293, 550, 527, 3055,
  562, 321, 1409, 281, 51448], "temperature": 0.0, "avg_logprob": -0.12444192513652232,
  "compression_ratio": 1.6598360655737705, "no_speech_prob": 0.0009809269104152918},
  {"id": 479, "seek": 318288, "start": 3205.6, "end": 3211.04, "text": " implement
  vector search was one thing and the other thing was you know how can we represent",
  "tokens": [51500, 4445, 8062, 3164, 390, 472, 551, 293, 264, 661, 551, 390, 291,
  458, 577, 393, 321, 2906, 51772], "temperature": 0.0, "avg_logprob": -0.12444192513652232,
  "compression_ratio": 1.6598360655737705, "no_speech_prob": 0.0009809269104152918},
  {"id": 480, "seek": 321288, "start": 3212.88, "end": 3218.4, "text": " the re-ranking
  using bird in westbound so using the actual bird model inputting both the", "tokens":
  [50364, 264, 319, 12, 20479, 278, 1228, 5255, 294, 7009, 18767, 370, 1228, 264,
  3539, 5255, 2316, 4846, 783, 1293, 264, 50640], "temperature": 0.0, "avg_logprob":
  -0.1886046902163998, "compression_ratio": 1.663677130044843, "no_speech_prob": 0.0004989661974832416},
  {"id": 481, "seek": 321288, "start": 3218.4, "end": 3223.28, "text": " career and
  the document at the same time so that was one dream we had and but we were looking
  at", "tokens": [50640, 3988, 293, 264, 4166, 412, 264, 912, 565, 370, 300, 390,
  472, 3055, 321, 632, 293, 457, 321, 645, 1237, 412, 50884], "temperature": 0.0,
  "avg_logprob": -0.1886046902163998, "compression_ratio": 1.663677130044843, "no_speech_prob":
  0.0004989661974832416}, {"id": 482, "seek": 321288, "start": 3223.28, "end": 3230.48,
  "text": " the results and I think the first paper that we read it read that they
  they used maybe a day", "tokens": [50884, 264, 3542, 293, 286, 519, 264, 700, 3035,
  300, 321, 1401, 309, 1401, 300, 436, 436, 1143, 1310, 257, 786, 51244], "temperature":
  0.0, "avg_logprob": -0.1886046902163998, "compression_ratio": 1.663677130044843,
  "no_speech_prob": 0.0004989661974832416}, {"id": 483, "seek": 321288, "start": 3231.12,
  "end": 3241.04, "text": " to with even with a GPU to actually perform 3600 queries
  right so it was not really you know", "tokens": [51276, 281, 365, 754, 365, 257,
  18407, 281, 767, 2042, 8652, 628, 24109, 558, 370, 309, 390, 406, 534, 291, 458,
  51772], "temperature": 0.0, "avg_logprob": -0.1886046902163998, "compression_ratio":
  1.663677130044843, "no_speech_prob": 0.0004989661974832416}, {"id": 484, "seek":
  324104, "start": 3241.04, "end": 3247.7599999999998, "text": " how can we make this
  practical and then two years later we actually did did beat", "tokens": [50364,
  577, 393, 321, 652, 341, 8496, 293, 550, 732, 924, 1780, 321, 767, 630, 630, 4224,
  50700], "temperature": 0.0, "avg_logprob": -0.1368877410888672, "compression_ratio":
  1.6787330316742082, "no_speech_prob": 0.0004709880449809134}, {"id": 485, "seek":
  324104, "start": 3248.56, "end": 3255.2799999999997, "text": " their benchmark and
  to end represented on westbound and we were doing it less than 100 milliseconds",
  "tokens": [50740, 641, 18927, 293, 281, 917, 10379, 322, 7009, 18767, 293, 321,
  645, 884, 309, 1570, 813, 2319, 34184, 51076], "temperature": 0.0, "avg_logprob":
  -0.1368877410888672, "compression_ratio": 1.6787330316742082, "no_speech_prob":
  0.0004709880449809134}, {"id": 486, "seek": 324104, "start": 3256.0, "end": 3264.56,
  "text": " so on CPU right so but there being a lot of learning to get there but
  that was the motivation to", "tokens": [51112, 370, 322, 13199, 558, 370, 457, 456,
  885, 257, 688, 295, 2539, 281, 483, 456, 457, 300, 390, 264, 12335, 281, 51540],
  "temperature": 0.0, "avg_logprob": -0.1368877410888672, "compression_ratio": 1.6787330316742082,
  "no_speech_prob": 0.0004709880449809134}, {"id": 487, "seek": 324104, "start": 3264.56,
  "end": 3269.92, "text": " kind of demonstrate that you can take this state of the
  art or close to state of the art with", "tokens": [51540, 733, 295, 11698, 300,
  291, 393, 747, 341, 1785, 295, 264, 1523, 420, 1998, 281, 1785, 295, 264, 1523,
  365, 51808], "temperature": 0.0, "avg_logprob": -0.1368877410888672, "compression_ratio":
  1.6787330316742082, "no_speech_prob": 0.0004709880449809134}, {"id": 488, "seek":
  326992, "start": 3269.92, "end": 3276.8, "text": " three-wheel and ranking pipeline
  from an open dataset which is how widely recognized and all the", "tokens": [50364,
  1045, 12, 22830, 293, 17833, 15517, 490, 364, 1269, 28872, 597, 307, 577, 13371,
  9823, 293, 439, 264, 50708], "temperature": 0.0, "avg_logprob": -0.222749733343357,
  "compression_ratio": 1.820754716981132, "no_speech_prob": 0.0006659059436060488},
  {"id": 489, "seek": 326992, "start": 3276.8, "end": 3281.6, "text": " researchers
  are actually publishing papers around it you can actually take that model and use",
  "tokens": [50708, 10309, 366, 767, 17832, 10577, 926, 309, 291, 393, 767, 747, 300,
  2316, 293, 764, 50948], "temperature": 0.0, "avg_logprob": -0.222749733343357, "compression_ratio":
  1.820754716981132, "no_speech_prob": 0.0006659059436060488}, {"id": 490, "seek":
  326992, "start": 3281.6, "end": 3288.08, "text": " westbound and get those results
  you know so it was one way of demonstrating that you can actually", "tokens": [50948,
  7009, 18767, 293, 483, 729, 3542, 291, 458, 370, 309, 390, 472, 636, 295, 29889,
  300, 291, 393, 767, 51272], "temperature": 0.0, "avg_logprob": -0.222749733343357,
  "compression_ratio": 1.820754716981132, "no_speech_prob": 0.0006659059436060488},
  {"id": 491, "seek": 326992, "start": 3288.08, "end": 3293.84, "text": " then you
  can actually use these models with westbound and have it serve in your state so
  that was", "tokens": [51272, 550, 291, 393, 767, 764, 613, 5245, 365, 7009, 18767,
  293, 362, 309, 4596, 294, 428, 1785, 370, 300, 390, 51560], "temperature": 0.0,
  "avg_logprob": -0.222749733343357, "compression_ratio": 1.820754716981132, "no_speech_prob":
  0.0006659059436060488}, {"id": 492, "seek": 329384, "start": 3293.84, "end": 3300.08,
  "text": " actually the motivation not on the kind of science side and so on but
  I have to say that I really", "tokens": [50364, 767, 264, 12335, 406, 322, 264,
  733, 295, 3497, 1252, 293, 370, 322, 457, 286, 362, 281, 584, 300, 286, 534, 50676],
  "temperature": 0.0, "avg_logprob": -0.06640084036465349, "compression_ratio": 1.7824074074074074,
  "no_speech_prob": 0.000877921876963228}, {"id": 493, "seek": 329384, "start": 3301.04,
  "end": 3307.1200000000003, "text": " would encourage everybody that works in search
  to look at some of these open datasets you know", "tokens": [50724, 576, 5373, 2201,
  300, 1985, 294, 3164, 281, 574, 412, 512, 295, 613, 1269, 42856, 291, 458, 51028],
  "temperature": 0.0, "avg_logprob": -0.06640084036465349, "compression_ratio": 1.7824074074074074,
  "no_speech_prob": 0.000877921876963228}, {"id": 494, "seek": 329384, "start": 3307.1200000000003,
  "end": 3313.44, "text": " play with them you know maybe you have some ideas you
  know around search and how to do search and", "tokens": [51028, 862, 365, 552, 291,
  458, 1310, 291, 362, 512, 3487, 291, 458, 926, 3164, 293, 577, 281, 360, 3164, 293,
  51344], "temperature": 0.0, "avg_logprob": -0.06640084036465349, "compression_ratio":
  1.7824074074074074, "no_speech_prob": 0.000877921876963228}, {"id": 495, "seek":
  329384, "start": 3314.32, "end": 3320.1600000000003, "text": " there''s a lot of
  talks about boosting this phrasing you know how actually does that impact the",
  "tokens": [51388, 456, 311, 257, 688, 295, 6686, 466, 43117, 341, 7636, 3349, 291,
  458, 577, 767, 775, 300, 2712, 264, 51680], "temperature": 0.0, "avg_logprob": -0.06640084036465349,
  "compression_ratio": 1.7824074074074074, "no_speech_prob": 0.000877921876963228},
  {"id": 496, "seek": 332016, "start": 3320.16, "end": 3328.3199999999997, "text":
  " results on kind of a dataset and I can really recommend the track COVID which
  is a dataset that was", "tokens": [50364, 3542, 322, 733, 295, 257, 28872, 293,
  286, 393, 534, 2748, 264, 2837, 4566, 597, 307, 257, 28872, 300, 390, 50772], "temperature":
  0.0, "avg_logprob": -0.12790567609998915, "compression_ratio": 1.6623931623931625,
  "no_speech_prob": 0.0004997096839360893}, {"id": 497, "seek": 332016, "start": 3329.44,
  "end": 3336.64, "text": " made at the start of the pandemic and it has about 50
  queries and deep judgments for each of the", "tokens": [50828, 1027, 412, 264, 722,
  295, 264, 5388, 293, 309, 575, 466, 2625, 24109, 293, 2452, 40337, 337, 1184, 295,
  264, 51188], "temperature": 0.0, "avg_logprob": -0.12790567609998915, "compression_ratio":
  1.6623931623931625, "no_speech_prob": 0.0004997096839360893}, {"id": 498, "seek":
  332016, "start": 3336.64, "end": 3341.44, "text": " queries and the collection is
  rather small so you can play with it on a single node and so on so", "tokens": [51188,
  24109, 293, 264, 5765, 307, 2831, 1359, 370, 291, 393, 862, 365, 309, 322, 257,
  2167, 9984, 293, 370, 322, 370, 51428], "temperature": 0.0, "avg_logprob": -0.12790567609998915,
  "compression_ratio": 1.6623931623931625, "no_speech_prob": 0.0004997096839360893},
  {"id": 499, "seek": 332016, "start": 3341.44, "end": 3346.24, "text": " that I will
  really encourage you know people in search to try out you know because then you
  get", "tokens": [51428, 300, 286, 486, 534, 5373, 291, 458, 561, 294, 3164, 281,
  853, 484, 291, 458, 570, 550, 291, 483, 51668], "temperature": 0.0, "avg_logprob":
  -0.12790567609998915, "compression_ratio": 1.6623931623931625, "no_speech_prob":
  0.0004997096839360893}, {"id": 500, "seek": 334624, "start": 3346.24, "end": 3352.3199999999997,
  "text": " the feeling you know does it actually work does it actually you know compare
  it with BM25 what", "tokens": [50364, 264, 2633, 291, 458, 775, 309, 767, 589, 775,
  309, 767, 291, 458, 6794, 309, 365, 15901, 6074, 437, 50668], "temperature": 0.0,
  "avg_logprob": -0.15529566870795355, "compression_ratio": 1.7345132743362832, "no_speech_prob":
  0.0013958995696157217}, {"id": 501, "seek": 334624, "start": 3352.3199999999997,
  "end": 3359.52, "text": " happens if I do phrase matching or do something clever
  you know so I think that''s and and I''m really", "tokens": [50668, 2314, 498, 286,
  360, 9535, 14324, 420, 360, 746, 13494, 291, 458, 370, 286, 519, 300, 311, 293,
  293, 286, 478, 534, 51028], "temperature": 0.0, "avg_logprob": -0.15529566870795355,
  "compression_ratio": 1.7345132743362832, "no_speech_prob": 0.0013958995696157217},
  {"id": 502, "seek": 334624, "start": 3359.52, "end": 3367.12, "text": " not a huge
  fan of anecdotal query examples to see these kind of commercial actors with this
  you know", "tokens": [51028, 406, 257, 2603, 3429, 295, 26652, 38180, 14581, 5110,
  281, 536, 613, 733, 295, 6841, 10037, 365, 341, 291, 458, 51408], "temperature":
  0.0, "avg_logprob": -0.15529566870795355, "compression_ratio": 1.7345132743362832,
  "no_speech_prob": 0.0013958995696157217}, {"id": 503, "seek": 334624, "start": 3367.12,
  "end": 3373.2799999999997, "text": " I''m searching for this on this magic results
  you know I''m more into you know demonstrating that", "tokens": [51408, 286, 478,
  10808, 337, 341, 322, 341, 5585, 3542, 291, 458, 286, 478, 544, 666, 291, 458, 29889,
  300, 51716], "temperature": 0.0, "avg_logprob": -0.15529566870795355, "compression_ratio":
  1.7345132743362832, "no_speech_prob": 0.0013958995696157217}, {"id": 504, "seek":
  337328, "start": 3373.36, "end": 3378.1600000000003, "text": " actually Westpac
  can do this and it has the funding and actually on the real datasets.", "tokens":
  [50368, 767, 4055, 79, 326, 393, 360, 341, 293, 309, 575, 264, 6137, 293, 767, 322,
  264, 957, 42856, 13, 50608], "temperature": 0.0, "avg_logprob": -0.16603803634643555,
  "compression_ratio": 1.7013574660633484, "no_speech_prob": 0.0014825869584456086},
  {"id": 505, "seek": 337328, "start": 3378.88, "end": 3384.7200000000003, "text":
  " Yeah and I agree in the end of the day what matters is first of all can you apply
  this tag as you", "tokens": [50644, 865, 293, 286, 3986, 294, 264, 917, 295, 264,
  786, 437, 7001, 307, 700, 295, 439, 393, 291, 3079, 341, 6162, 382, 291, 50936],
  "temperature": 0.0, "avg_logprob": -0.16603803634643555, "compression_ratio": 1.7013574660633484,
  "no_speech_prob": 0.0014825869584456086}, {"id": 506, "seek": 337328, "start": 3384.7200000000003,
  "end": 3390.4, "text": " said in your real setting right in your domain then another
  thing that you mentioned just now", "tokens": [50936, 848, 294, 428, 957, 3287,
  558, 294, 428, 9274, 550, 1071, 551, 300, 291, 2835, 445, 586, 51220], "temperature":
  0.0, "avg_logprob": -0.16603803634643555, "compression_ratio": 1.7013574660633484,
  "no_speech_prob": 0.0014825869584456086}, {"id": 507, "seek": 337328, "start": 3391.44,
  "end": 3397.6000000000004, "text": " you know the track COVID dataset so maybe as
  the result of your research you might also impact on", "tokens": [51272, 291, 458,
  264, 2837, 4566, 28872, 370, 1310, 382, 264, 1874, 295, 428, 2132, 291, 1062, 611,
  2712, 322, 51580], "temperature": 0.0, "avg_logprob": -0.16603803634643555, "compression_ratio":
  1.7013574660633484, "no_speech_prob": 0.0014825869584456086}, {"id": 508, "seek":
  339760, "start": 3397.6, "end": 3403.2799999999997, "text": " the global situation
  right maybe somewhere locally maybe somebody will use your work to actually", "tokens":
  [50364, 264, 4338, 2590, 558, 1310, 4079, 16143, 1310, 2618, 486, 764, 428, 589,
  281, 767, 50648], "temperature": 0.0, "avg_logprob": -0.14964116977739939, "compression_ratio":
  1.6403508771929824, "no_speech_prob": 0.0006959047168493271}, {"id": 509, "seek":
  339760, "start": 3403.2799999999997, "end": 3411.36, "text": " implement a better
  search system so I think that that''s also a fantastic segue to you know", "tokens":
  [50648, 4445, 257, 1101, 3164, 1185, 370, 286, 519, 300, 300, 311, 611, 257, 5456,
  33850, 281, 291, 458, 51052], "temperature": 0.0, "avg_logprob": -0.14964116977739939,
  "compression_ratio": 1.6403508771929824, "no_speech_prob": 0.0006959047168493271},
  {"id": 510, "seek": 339760, "start": 3412.3199999999997, "end": 3417.68, "text":
  " the the context that you''re doing and that''s actually a very interesting point
  because we had", "tokens": [51100, 264, 264, 4319, 300, 291, 434, 884, 293, 300,
  311, 767, 257, 588, 1880, 935, 570, 321, 632, 51368], "temperature": 0.0, "avg_logprob":
  -0.14964116977739939, "compression_ratio": 1.6403508771929824, "no_speech_prob":
  0.0006959047168493271}, {"id": 511, "seek": 339760, "start": 3419.6, "end": 3426.56,
  "text": " at the start of the pandemic we built a cord 19 search interface that
  we published online so", "tokens": [51464, 412, 264, 722, 295, 264, 5388, 321, 3094,
  257, 12250, 1294, 3164, 9226, 300, 321, 6572, 2950, 370, 51812], "temperature":
  0.0, "avg_logprob": -0.14964116977739939, "compression_ratio": 1.6403508771929824,
  "no_speech_prob": 0.0006959047168493271}, {"id": 512, "seek": 342656, "start": 3426.56,
  "end": 3432.7999999999997, "text": " people who actually go and search this dataset
  and people they were I don''t I don''t recall the", "tokens": [50364, 561, 567,
  767, 352, 293, 3164, 341, 28872, 293, 561, 436, 645, 286, 500, 380, 286, 500, 380,
  9901, 264, 50676], "temperature": 0.0, "avg_logprob": -0.1679816927228655, "compression_ratio":
  1.83203125, "no_speech_prob": 0.0003276356728747487}, {"id": 513, "seek": 342656,
  "start": 3432.7999999999997, "end": 3437.84, "text": " details but it''s still online
  and people actually because of all open source so they forked it and", "tokens":
  [50676, 4365, 457, 309, 311, 920, 2950, 293, 561, 767, 570, 295, 439, 1269, 4009,
  370, 436, 17716, 292, 309, 293, 50928], "temperature": 0.0, "avg_logprob": -0.1679816927228655,
  "compression_ratio": 1.83203125, "no_speech_prob": 0.0003276356728747487}, {"id":
  514, "seek": 342656, "start": 3437.84, "end": 3442.24, "text": " then they started
  using Westpac and based on that and I think it''s a much better shape", "tokens":
  [50928, 550, 436, 1409, 1228, 4055, 79, 326, 293, 2361, 322, 300, 293, 286, 519,
  309, 311, 257, 709, 1101, 3909, 51148], "temperature": 0.0, "avg_logprob": -0.1679816927228655,
  "compression_ratio": 1.83203125, "no_speech_prob": 0.0003276356728747487}, {"id":
  515, "seek": 342656, "start": 3443.04, "end": 3447.92, "text": " that service right
  now than the the cord 19 search that we did so they actually built on that", "tokens":
  [51188, 300, 2643, 558, 586, 813, 264, 264, 12250, 1294, 3164, 300, 321, 630, 370,
  436, 767, 3094, 322, 300, 51432], "temperature": 0.0, "avg_logprob": -0.1679816927228655,
  "compression_ratio": 1.83203125, "no_speech_prob": 0.0003276356728747487}, {"id":
  516, "seek": 342656, "start": 3447.92, "end": 3454.4, "text": " work so so that''s
  that''s great I love to put what I call sample applications you know how what",
  "tokens": [51432, 589, 370, 370, 300, 311, 300, 311, 869, 286, 959, 281, 829, 437,
  286, 818, 6889, 5821, 291, 458, 577, 437, 51756], "temperature": 0.0, "avg_logprob":
  -0.1679816927228655, "compression_ratio": 1.83203125, "no_speech_prob": 0.0003276356728747487},
  {"id": 517, "seek": 345440, "start": 3454.4, "end": 3460.08, "text": " can you build
  with with Westpac and and that''s actually a lot of my time these days are spent
  on", "tokens": [50364, 393, 291, 1322, 365, 365, 4055, 79, 326, 293, 293, 300, 311,
  767, 257, 688, 295, 452, 565, 613, 1708, 366, 4418, 322, 50648], "temperature":
  0.0, "avg_logprob": -0.12521179953774253, "compression_ratio": 1.7568807339449541,
  "no_speech_prob": 0.0006008953205309808}, {"id": 518, "seek": 345440, "start": 3460.64,
  "end": 3467.92, "text": " making these sample applications smooth and easy to to
  work with and especially we''ve been", "tokens": [50676, 1455, 613, 6889, 5821,
  5508, 293, 1858, 281, 281, 589, 365, 293, 2318, 321, 600, 668, 51040], "temperature":
  0.0, "avg_logprob": -0.12521179953774253, "compression_ratio": 1.7568807339449541,
  "no_speech_prob": 0.0006008953205309808}, {"id": 519, "seek": 345440, "start": 3467.92,
  "end": 3473.52, "text": " rather weak on the kind of UI putting together front dance
  and so on so that''s actually some work", "tokens": [51040, 2831, 5336, 322, 264,
  733, 295, 15682, 3372, 1214, 1868, 4489, 293, 370, 322, 370, 300, 311, 767, 512,
  589, 51320], "temperature": 0.0, "avg_logprob": -0.12521179953774253, "compression_ratio":
  1.7568807339449541, "no_speech_prob": 0.0006008953205309808}, {"id": 520, "seek":
  345440, "start": 3473.52, "end": 3479.12, "text": " that I''m doing right now to
  kind of build more of the product you know what can you build with it", "tokens":
  [51320, 300, 286, 478, 884, 558, 586, 281, 733, 295, 1322, 544, 295, 264, 1674,
  291, 458, 437, 393, 291, 1322, 365, 309, 51600], "temperature": 0.0, "avg_logprob":
  -0.12521179953774253, "compression_ratio": 1.7568807339449541, "no_speech_prob":
  0.0006008953205309808}, {"id": 521, "seek": 347912, "start": 3479.12, "end": 3485.6,
  "text": " because people don''t get really excited about looking at Jason I output
  you know to actually see", "tokens": [50364, 570, 561, 500, 380, 483, 534, 2919,
  466, 1237, 412, 11181, 286, 5598, 291, 458, 281, 767, 536, 50688], "temperature":
  0.0, "avg_logprob": -0.14565244562485638, "compression_ratio": 1.8073394495412844,
  "no_speech_prob": 0.0030232362914830446}, {"id": 522, "seek": 347912, "start": 3485.6,
  "end": 3490.72, "text": " some interactions faces facets you know out the completion
  and to actually build that whole experience", "tokens": [50688, 512, 13280, 8475,
  49752, 291, 458, 484, 264, 19372, 293, 281, 767, 1322, 300, 1379, 1752, 50944],
  "temperature": 0.0, "avg_logprob": -0.14565244562485638, "compression_ratio": 1.8073394495412844,
  "no_speech_prob": 0.0030232362914830446}, {"id": 523, "seek": 347912, "start": 3490.72,
  "end": 3496.56, "text": " you know for the for the product people it''s like looking
  at the engine when you actually want to", "tokens": [50944, 291, 458, 337, 264,
  337, 264, 1674, 561, 309, 311, 411, 1237, 412, 264, 2848, 562, 291, 767, 528, 281,
  51236], "temperature": 0.0, "avg_logprob": -0.14565244562485638, "compression_ratio":
  1.8073394495412844, "no_speech_prob": 0.0030232362914830446}, {"id": 524, "seek":
  347912, "start": 3496.56, "end": 3502.08, "text": " maybe look at the car right
  and then you get fascinated by how shiny and sort of sleek it is and", "tokens":
  [51236, 1310, 574, 412, 264, 1032, 558, 293, 550, 291, 483, 24597, 538, 577, 16997,
  293, 1333, 295, 43464, 309, 307, 293, 51512], "temperature": 0.0, "avg_logprob":
  -0.14565244562485638, "compression_ratio": 1.8073394495412844, "no_speech_prob":
  0.0030232362914830446}, {"id": 525, "seek": 350208, "start": 3502.48, "end": 3509.04,
  "text": " then you''re like I''m buying it yes yes I totally hear you there and
  like actually in these", "tokens": [50384, 550, 291, 434, 411, 286, 478, 6382, 309,
  2086, 2086, 286, 3879, 1568, 291, 456, 293, 411, 767, 294, 613, 50712], "temperature":
  0.0, "avg_logprob": -0.10854914983113607, "compression_ratio": 1.7767441860465116,
  "no_speech_prob": 0.0009868770139291883}, {"id": 526, "seek": 350208, "start": 3509.04,
  "end": 3515.2, "text": " use cases you know there are other platforms you know in
  the neural search space also doing multiple", "tokens": [50712, 764, 3331, 291,
  458, 456, 366, 661, 9473, 291, 458, 294, 264, 18161, 3164, 1901, 611, 884, 3866,
  51020], "temperature": 0.0, "avg_logprob": -0.10854914983113607, "compression_ratio":
  1.7767441860465116, "no_speech_prob": 0.0009868770139291883}, {"id": 527, "seek":
  350208, "start": 3515.2, "end": 3522.0, "text": " demos have you been looking into
  the direction of multimodal search does that excite you do you think", "tokens":
  [51020, 33788, 362, 291, 668, 1237, 666, 264, 3513, 295, 32972, 378, 304, 3164,
  775, 300, 1624, 642, 291, 360, 291, 519, 51360], "temperature": 0.0, "avg_logprob":
  -0.10854914983113607, "compression_ratio": 1.7767441860465116, "no_speech_prob":
  0.0009868770139291883}, {"id": 528, "seek": 350208, "start": 3522.88, "end": 3529.84,
  "text": " it''s too much of a bling edge or niche use case or do you think it has
  potential because", "tokens": [51404, 309, 311, 886, 709, 295, 257, 888, 278, 4691,
  420, 19956, 764, 1389, 420, 360, 291, 519, 309, 575, 3995, 570, 51752], "temperature":
  0.0, "avg_logprob": -0.10854914983113607, "compression_ratio": 1.7767441860465116,
  "no_speech_prob": 0.0009868770139291883}, {"id": 529, "seek": 352984, "start": 3530.6400000000003,
  "end": 3535.28, "text": " of the neural search crossing the boundary of text towards
  the image audio and so on", "tokens": [50404, 295, 264, 18161, 3164, 14712, 264,
  12866, 295, 2487, 3030, 264, 3256, 6278, 293, 370, 322, 50636], "temperature": 0.0,
  "avg_logprob": -0.1459303900252941, "compression_ratio": 1.7440758293838863, "no_speech_prob":
  0.0019839617889374495}, {"id": 530, "seek": 352984, "start": 3537.76, "end": 3544.2400000000002,
  "text": " yeah I think multimodal is really where recto search is shining so this
  is the area where you", "tokens": [50760, 1338, 286, 519, 32972, 378, 304, 307,
  534, 689, 11048, 78, 3164, 307, 18269, 370, 341, 307, 264, 1859, 689, 291, 51084],
  "temperature": 0.0, "avg_logprob": -0.1459303900252941, "compression_ratio": 1.7440758293838863,
  "no_speech_prob": 0.0019839617889374495}, {"id": 531, "seek": 352984, "start": 3544.96,
  "end": 3551.84, "text": " it really shines I have some doubts about out of the main
  like we discussed using a vector model", "tokens": [51120, 309, 534, 28056, 286,
  362, 512, 22618, 466, 484, 295, 264, 2135, 411, 321, 7152, 1228, 257, 8062, 2316,
  51464], "temperature": 0.0, "avg_logprob": -0.1459303900252941, "compression_ratio":
  1.7440758293838863, "no_speech_prob": 0.0019839617889374495}, {"id": 532, "seek":
  352984, "start": 3551.84, "end": 3556.8, "text": " for text search if you don''t
  have any label training data and so on and adopted to your data", "tokens": [51464,
  337, 2487, 3164, 498, 291, 500, 380, 362, 604, 7645, 3097, 1412, 293, 370, 322,
  293, 12175, 281, 428, 1412, 51712], "temperature": 0.0, "avg_logprob": -0.1459303900252941,
  "compression_ratio": 1.7440758293838863, "no_speech_prob": 0.0019839617889374495},
  {"id": 533, "seek": 355680, "start": 3557.6000000000004, "end": 3566.1600000000003,
  "text": " using vector search alone for that I think is questionable but looking
  at this multimodal where you", "tokens": [50404, 1228, 8062, 3164, 3312, 337, 300,
  286, 519, 307, 37158, 457, 1237, 412, 341, 32972, 378, 304, 689, 291, 50832], "temperature":
  0.0, "avg_logprob": -0.14201689370070833, "compression_ratio": 1.6901408450704225,
  "no_speech_prob": 0.0010537938214838505}, {"id": 534, "seek": 355680, "start": 3566.1600000000003,
  "end": 3572.32, "text": " combine both a transformer model and a typical image model
  and you train that representation", "tokens": [50832, 10432, 1293, 257, 31782, 2316,
  293, 257, 7476, 3256, 2316, 293, 291, 3847, 300, 10290, 51140], "temperature": 0.0,
  "avg_logprob": -0.14201689370070833, "compression_ratio": 1.6901408450704225, "no_speech_prob":
  0.0010537938214838505}, {"id": 535, "seek": 355680, "start": 3573.04, "end": 3577.84,
  "text": " and from what I''ve seen from these models and we did a sample application
  on this as well", "tokens": [51176, 293, 490, 437, 286, 600, 1612, 490, 613, 5245,
  293, 321, 630, 257, 6889, 3861, 322, 341, 382, 731, 51416], "temperature": 0.0,
  "avg_logprob": -0.14201689370070833, "compression_ratio": 1.6901408450704225, "no_speech_prob":
  0.0010537938214838505}, {"id": 536, "seek": 355680, "start": 3578.5600000000004,
  "end": 3585.92, "text": " using the clip embedding model from from open AI and looking
  at the results I", "tokens": [51452, 1228, 264, 7353, 12240, 3584, 2316, 490, 490,
  1269, 7318, 293, 1237, 412, 264, 3542, 286, 51820], "temperature": 0.0, "avg_logprob":
  -0.14201689370070833, "compression_ratio": 1.6901408450704225, "no_speech_prob":
  0.0010537938214838505}, {"id": 537, "seek": 358592, "start": 3586.48, "end": 3591.84,
  "text": " I have to say that I''m really impressed by kind of just eyeballing I
  don''t have any kind of", "tokens": [50392, 286, 362, 281, 584, 300, 286, 478, 534,
  11679, 538, 733, 295, 445, 38868, 278, 286, 500, 380, 362, 604, 733, 295, 50660],
  "temperature": 0.0, "avg_logprob": -0.1111147953913762, "compression_ratio": 1.8256410256410256,
  "no_speech_prob": 0.0037121912464499474}, {"id": 538, "seek": 358592, "start": 3593.04,
  "end": 3598.48, "text": " I don''t have any hard data sets or but it''s really impressive
  you know what that model can", "tokens": [50720, 286, 500, 380, 362, 604, 1152,
  1412, 6352, 420, 457, 309, 311, 534, 8992, 291, 458, 437, 300, 2316, 393, 50992],
  "temperature": 0.0, "avg_logprob": -0.1111147953913762, "compression_ratio": 1.8256410256410256,
  "no_speech_prob": 0.0037121912464499474}, {"id": 539, "seek": 358592, "start": 3598.48,
  "end": 3605.2000000000003, "text": " can actually do so I definitely think that
  multimodal is it''s very I don''t think it''s", "tokens": [50992, 393, 767, 360,
  370, 286, 2138, 519, 300, 32972, 378, 304, 307, 309, 311, 588, 286, 500, 380, 519,
  309, 311, 51328], "temperature": 0.0, "avg_logprob": -0.1111147953913762, "compression_ratio":
  1.8256410256410256, "no_speech_prob": 0.0037121912464499474}, {"id": 540, "seek":
  358592, "start": 3606.32, "end": 3613.76, "text": " I don''t think it''s that far
  ahead I think because we have interest in representing clip", "tokens": [51384,
  286, 500, 380, 519, 309, 311, 300, 1400, 2286, 286, 519, 570, 321, 362, 1179, 294,
  13460, 7353, 51756], "temperature": 0.0, "avg_logprob": -0.1111147953913762, "compression_ratio":
  1.8256410256410256, "no_speech_prob": 0.0037121912464499474}, {"id": 541, "seek":
  361376, "start": 3614.32, "end": 3619.28, "text": " in best from from actual questions
  I''m actually I''m seeing an email right now you know how to", "tokens": [50392,
  294, 1151, 490, 490, 3539, 1651, 286, 478, 767, 286, 478, 2577, 364, 3796, 558,
  586, 291, 458, 577, 281, 50640], "temperature": 0.0, "avg_logprob": -0.2134443995464279,
  "compression_ratio": 1.7326732673267327, "no_speech_prob": 0.004124809056520462},
  {"id": 542, "seek": 361376, "start": 3620.2400000000002, "end": 3625.2000000000003,
  "text": " they want to help on their schema and definitely they want to use clip",
  "tokens": [50688, 436, 528, 281, 854, 322, 641, 34078, 293, 2138, 436, 528, 281,
  764, 7353, 50936], "temperature": 0.0, "avg_logprob": -0.2134443995464279, "compression_ratio":
  1.7326732673267327, "no_speech_prob": 0.004124809056520462}, {"id": 543, "seek":
  361376, "start": 3625.84, "end": 3631.6800000000003, "text": " yeah so definitely
  I don''t think it''s that advanced at the moment and I think we''ll see", "tokens":
  [50968, 1338, 370, 2138, 286, 500, 380, 519, 309, 311, 300, 7339, 412, 264, 1623,
  293, 286, 519, 321, 603, 536, 51260], "temperature": 0.0, "avg_logprob": -0.2134443995464279,
  "compression_ratio": 1.7326732673267327, "no_speech_prob": 0.004124809056520462},
  {"id": 544, "seek": 361376, "start": 3632.8, "end": 3637.36, "text": " another thing
  that I''m working on right now is that I talked about our sample applications I
  want", "tokens": [51316, 1071, 551, 300, 286, 478, 1364, 322, 558, 586, 307, 300,
  286, 2825, 466, 527, 6889, 5821, 286, 528, 51544], "temperature": 0.0, "avg_logprob":
  -0.2134443995464279, "compression_ratio": 1.7326732673267327, "no_speech_prob":
  0.004124809056520462}, {"id": 545, "seek": 363736, "start": 3637.36, "end": 3643.92,
  "text": " to build a new sample application that demonstrates in a UI in an e-commerce
  setting where you", "tokens": [50364, 281, 1322, 257, 777, 6889, 3861, 300, 31034,
  294, 257, 15682, 294, 364, 308, 12, 26926, 3287, 689, 291, 50692], "temperature":
  0.0, "avg_logprob": -0.13036282857259116, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.002691468223929405}, {"id": 546, "seek": 363736, "start": 3643.92,
  "end": 3650.6400000000003, "text": " combine different kind of fussy matching exact
  matching vector search all in the same query and", "tokens": [50692, 10432, 819,
  733, 295, 283, 26394, 14324, 1900, 14324, 8062, 3164, 439, 294, 264, 912, 14581,
  293, 51028], "temperature": 0.0, "avg_logprob": -0.13036282857259116, "compression_ratio":
  1.6551724137931034, "no_speech_prob": 0.002691468223929405}, {"id": 547, "seek":
  363736, "start": 3650.6400000000003, "end": 3655.84, "text": " then you can have
  some sliders where you actually slide these you know how does the result change",
  "tokens": [51028, 550, 291, 393, 362, 512, 1061, 6936, 689, 291, 767, 4137, 613,
  291, 458, 577, 775, 264, 1874, 1319, 51288], "temperature": 0.0, "avg_logprob":
  -0.13036282857259116, "compression_ratio": 1.6551724137931034, "no_speech_prob":
  0.002691468223929405}, {"id": 548, "seek": 363736, "start": 3655.84, "end": 3661.6,
  "text": " and they change in real time so I just need some help on the on the react
  front end because I''m", "tokens": [51288, 293, 436, 1319, 294, 957, 565, 370, 286,
  445, 643, 512, 854, 322, 264, 322, 264, 4515, 1868, 917, 570, 286, 478, 51576],
  "temperature": 0.0, "avg_logprob": -0.13036282857259116, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.002691468223929405}, {"id": 549, "seek": 366160, "start": 3661.6,
  "end": 3667.6, "text": " not I''m not a great JavaScript programmer I have to admit
  so I need some help on that so yeah but", "tokens": [50364, 406, 286, 478, 406,
  257, 869, 15778, 32116, 286, 362, 281, 9796, 370, 286, 643, 512, 854, 322, 300,
  370, 1338, 457, 50664], "temperature": 0.0, "avg_logprob": -0.1433842764960395,
  "compression_ratio": 1.6302521008403361, "no_speech_prob": 0.0010606141295284033},
  {"id": 550, "seek": 366160, "start": 3667.6, "end": 3673.7599999999998, "text":
  " I definitely think that multimodal vector search has a really has a huge number
  of use cases yeah", "tokens": [50664, 286, 2138, 519, 300, 32972, 378, 304, 8062,
  3164, 575, 257, 534, 575, 257, 2603, 1230, 295, 764, 3331, 1338, 50972], "temperature":
  0.0, "avg_logprob": -0.1433842764960395, "compression_ratio": 1.6302521008403361,
  "no_speech_prob": 0.0010606141295284033}, {"id": 551, "seek": 366160, "start": 3674.7999999999997,
  "end": 3682.64, "text": " I hope that amongst listeners of this podcast maybe there
  are some with front end skills and maybe", "tokens": [51024, 286, 1454, 300, 12918,
  23274, 295, 341, 7367, 1310, 456, 366, 512, 365, 1868, 917, 3942, 293, 1310, 51416],
  "temperature": 0.0, "avg_logprob": -0.1433842764960395, "compression_ratio": 1.6302521008403361,
  "no_speech_prob": 0.0010606141295284033}, {"id": 552, "seek": 366160, "start": 3682.64,
  "end": 3688.3199999999997, "text": " since you''re building this for open source
  you know that might be good use case as well to be", "tokens": [51416, 1670, 291,
  434, 2390, 341, 337, 1269, 4009, 291, 458, 300, 1062, 312, 665, 764, 1389, 382,
  731, 281, 312, 51700], "temperature": 0.0, "avg_logprob": -0.1433842764960395, "compression_ratio":
  1.6302521008403361, "no_speech_prob": 0.0010606141295284033}, {"id": 553, "seek":
  368832, "start": 3688.32, "end": 3694.96, "text": " contributing to this crazy journey
  but we have yeah I mean that would I mean definitely we do see", "tokens": [50364,
  19270, 281, 341, 3219, 4671, 457, 321, 362, 1338, 286, 914, 300, 576, 286, 914,
  2138, 321, 360, 536, 50696], "temperature": 0.0, "avg_logprob": -0.15763405070585362,
  "compression_ratio": 1.7130434782608697, "no_speech_prob": 0.002225163159891963},
  {"id": 554, "seek": 368832, "start": 3694.96, "end": 3702.2400000000002, "text":
  " more involvement and contributions from from the in the kind of community around
  VESPA so I think", "tokens": [50696, 544, 17447, 293, 15725, 490, 490, 264, 294,
  264, 733, 295, 1768, 926, 691, 2358, 10297, 370, 286, 519, 51060], "temperature":
  0.0, "avg_logprob": -0.15763405070585362, "compression_ratio": 1.7130434782608697,
  "no_speech_prob": 0.002225163159891963}, {"id": 555, "seek": 368832, "start": 3702.2400000000002,
  "end": 3707.28, "text": " we build a lot of the last two years of the community
  side and people getting to know more about", "tokens": [51060, 321, 1322, 257, 688,
  295, 264, 1036, 732, 924, 295, 264, 1768, 1252, 293, 561, 1242, 281, 458, 544, 466,
  51312], "temperature": 0.0, "avg_logprob": -0.15763405070585362, "compression_ratio":
  1.7130434782608697, "no_speech_prob": 0.002225163159891963}, {"id": 556, "seek":
  368832, "start": 3707.28, "end": 3713.84, "text": " VESPA and actually starting
  to contribute back both on the sample applications and also documentation", "tokens":
  [51312, 691, 2358, 10297, 293, 767, 2891, 281, 10586, 646, 1293, 322, 264, 6889,
  5821, 293, 611, 14333, 51640], "temperature": 0.0, "avg_logprob": -0.15763405070585362,
  "compression_ratio": 1.7130434782608697, "no_speech_prob": 0.002225163159891963},
  {"id": 557, "seek": 371384, "start": 3713.84, "end": 3718.8, "text": " and also
  we''re seeing our more involved in contributing to the code so definitely yeah",
  "tokens": [50364, 293, 611, 321, 434, 2577, 527, 544, 3288, 294, 19270, 281, 264,
  3089, 370, 2138, 1338, 50612], "temperature": 0.0, "avg_logprob": -0.20125305259620752,
  "compression_ratio": 1.619047619047619, "no_speech_prob": 0.0013368910877034068},
  {"id": 558, "seek": 371384, "start": 3720.8, "end": 3726.56, "text": " so but I
  think it''s from a product side it''s really important for us to and also we have
  a", "tokens": [50712, 370, 457, 286, 519, 309, 311, 490, 257, 1674, 1252, 309, 311,
  534, 1021, 337, 505, 281, 293, 611, 321, 362, 257, 51000], "temperature": 0.0, "avg_logprob":
  -0.20125305259620752, "compression_ratio": 1.619047619047619, "no_speech_prob":
  0.0013368910877034068}, {"id": 559, "seek": 371384, "start": 3726.56, "end": 3732.48,
  "text": " commercial offering of VESPA where you actually have a hosted interface
  hosted solution multi-region", "tokens": [51000, 6841, 8745, 295, 691, 2358, 10297,
  689, 291, 767, 362, 257, 19204, 9226, 19204, 3827, 4825, 12, 3375, 313, 51296],
  "temperature": 0.0, "avg_logprob": -0.20125305259620752, "compression_ratio": 1.619047619047619,
  "no_speech_prob": 0.0013368910877034068}, {"id": 560, "seek": 371384, "start": 3733.6800000000003,
  "end": 3741.36, "text": " and to I think it we want VESPA to be able to run fully
  fledged in your environment if you want", "tokens": [51356, 293, 281, 286, 519,
  309, 321, 528, 691, 2358, 10297, 281, 312, 1075, 281, 1190, 4498, 24114, 3004, 294,
  428, 2823, 498, 291, 528, 51740], "temperature": 0.0, "avg_logprob": -0.20125305259620752,
  "compression_ratio": 1.619047619047619, "no_speech_prob": 0.0013368910877034068},
  {"id": 561, "seek": 374136, "start": 3741.36, "end": 3747.04, "text": " to use it
  because it''s open source it''s our Pasha 20 if you want to use our cloud you are
  welcome", "tokens": [50364, 281, 764, 309, 570, 309, 311, 1269, 4009, 309, 311,
  527, 430, 12137, 945, 498, 291, 528, 281, 764, 527, 4588, 291, 366, 2928, 50648],
  "temperature": 0.0, "avg_logprob": -0.20485071035531852, "compression_ratio": 1.5638297872340425,
  "no_speech_prob": 0.0011292911367490888}, {"id": 562, "seek": 374136, "start": 3747.04,
  "end": 3756.08, "text": " to do that and to kind of have and the same kind of functionality
  and what we add in the cloud is", "tokens": [50648, 281, 360, 300, 293, 281, 733,
  295, 362, 293, 264, 912, 733, 295, 14980, 293, 437, 321, 909, 294, 264, 4588, 307,
  51100], "temperature": 0.0, "avg_logprob": -0.20485071035531852, "compression_ratio":
  1.5638297872340425, "no_speech_prob": 0.0011292911367490888}, {"id": 563, "seek":
  374136, "start": 3756.6400000000003, "end": 3765.84, "text": " CICD pipelines how
  to do multi-region failovers like in the US East US West you can have different",
  "tokens": [51128, 383, 2532, 35, 40168, 577, 281, 360, 4825, 12, 3375, 313, 3061,
  25348, 411, 294, 264, 2546, 6747, 2546, 4055, 291, 393, 362, 819, 51588], "temperature":
  0.0, "avg_logprob": -0.20485071035531852, "compression_ratio": 1.5638297872340425,
  "no_speech_prob": 0.0011292911367490888}, {"id": 564, "seek": 376584, "start": 3765.84,
  "end": 3773.2000000000003, "text": " so all this kind of top and take care of sort
  of take care of nodes failing and whatever you know", "tokens": [50364, 370, 439,
  341, 733, 295, 1192, 293, 747, 1127, 295, 1333, 295, 747, 1127, 295, 13891, 18223,
  293, 2035, 291, 458, 50732], "temperature": 0.0, "avg_logprob": -0.19817033278203644,
  "compression_ratio": 1.864864864864865, "no_speech_prob": 0.0016855113208293915},
  {"id": 565, "seek": 376584, "start": 3773.2000000000003, "end": 3778.7200000000003,
  "text": " the hole the kind of host the experience so and that''s been an issue
  with our sample apps they have", "tokens": [50732, 264, 5458, 264, 733, 295, 3975,
  264, 1752, 370, 293, 300, 311, 668, 364, 2734, 365, 527, 6889, 7733, 436, 362, 51008],
  "temperature": 0.0, "avg_logprob": -0.19817033278203644, "compression_ratio": 1.864864864864865,
  "no_speech_prob": 0.0016855113208293915}, {"id": 566, "seek": 376584, "start": 3778.7200000000003,
  "end": 3783.6800000000003, "text": " been like it has been some friction around
  you know how to deploy them locally how to deploy", "tokens": [51008, 668, 411,
  309, 575, 668, 512, 17710, 926, 291, 458, 577, 281, 7274, 552, 16143, 577, 281,
  7274, 51256], "temperature": 0.0, "avg_logprob": -0.19817033278203644, "compression_ratio":
  1.864864864864865, "no_speech_prob": 0.0016855113208293915}, {"id": 567, "seek":
  376584, "start": 3783.6800000000003, "end": 3788.88, "text": " them to the cloud
  so I''m trying to kind of bring them together so that they they work in in multiple",
  "tokens": [51256, 552, 281, 264, 4588, 370, 286, 478, 1382, 281, 733, 295, 1565,
  552, 1214, 370, 300, 436, 436, 589, 294, 294, 3866, 51516], "temperature": 0.0,
  "avg_logprob": -0.19817033278203644, "compression_ratio": 1.864864864864865, "no_speech_prob":
  0.0016855113208293915}, {"id": 568, "seek": 376584, "start": 3788.88, "end": 3795.1200000000003,
  "text": " environments yeah that''s a lot of sense and I guess it takes a lot of
  engineering effort to", "tokens": [51516, 12388, 1338, 300, 311, 257, 688, 295,
  2020, 293, 286, 2041, 309, 2516, 257, 688, 295, 7043, 4630, 281, 51828], "temperature":
  0.0, "avg_logprob": -0.19817033278203644, "compression_ratio": 1.864864864864865,
  "no_speech_prob": 0.0016855113208293915}, {"id": 569, "seek": 379512, "start": 3795.12,
  "end": 3801.44, "text": " also kind of cover all these different use cases so sounds
  quite exciting and actually demoing", "tokens": [50364, 611, 733, 295, 2060, 439,
  613, 819, 764, 3331, 370, 3263, 1596, 4670, 293, 767, 10723, 278, 50680], "temperature":
  0.0, "avg_logprob": -0.08196961602499318, "compression_ratio": 1.7244444444444444,
  "no_speech_prob": 0.0008621862507425249}, {"id": 570, "seek": 379512, "start": 3801.44,
  "end": 3810.0, "text": " the technology I think you know as you know other vector
  databases have got it and I think it''s a", "tokens": [50680, 264, 2899, 286, 519,
  291, 458, 382, 291, 458, 661, 8062, 22380, 362, 658, 309, 293, 286, 519, 309, 311,
  257, 51108], "temperature": 0.0, "avg_logprob": -0.08196961602499318, "compression_ratio":
  1.7244444444444444, "no_speech_prob": 0.0008621862507425249}, {"id": 571, "seek":
  379512, "start": 3810.0, "end": 3817.3599999999997, "text": " such a low entry for
  especially for non-technical people or those who are in charge of businesses", "tokens":
  [51108, 1270, 257, 2295, 8729, 337, 2318, 337, 2107, 12, 29113, 804, 561, 420, 729,
  567, 366, 294, 4602, 295, 6011, 51476], "temperature": 0.0, "avg_logprob": -0.08196961602499318,
  "compression_ratio": 1.7244444444444444, "no_speech_prob": 0.0008621862507425249},
  {"id": 572, "seek": 379512, "start": 3817.3599999999997, "end": 3823.92, "text":
  " business units to actually make decisions and I think for them you know having
  a relevant demo is", "tokens": [51476, 1606, 6815, 281, 767, 652, 5327, 293, 286,
  519, 337, 552, 291, 458, 1419, 257, 7340, 10723, 307, 51804], "temperature": 0.0,
  "avg_logprob": -0.08196961602499318, "compression_ratio": 1.7244444444444444, "no_speech_prob":
  0.0008621862507425249}, {"id": 573, "seek": 382392, "start": 3823.92, "end": 3830.2400000000002,
  "text": " going to be quite a game changer because if they need to reason about
  your technology only through", "tokens": [50364, 516, 281, 312, 1596, 257, 1216,
  22822, 570, 498, 436, 643, 281, 1778, 466, 428, 2899, 787, 807, 50680], "temperature":
  0.0, "avg_logprob": -0.0946647510972134, "compression_ratio": 1.6835443037974684,
  "no_speech_prob": 0.001372458878904581}, {"id": 574, "seek": 382392, "start": 3830.2400000000002,
  "end": 3838.0, "text": " the eyes of engineers in their company then probably that''s
  that''s much longer path right yeah exactly", "tokens": [50680, 264, 2575, 295,
  11955, 294, 641, 2237, 550, 1391, 300, 311, 300, 311, 709, 2854, 3100, 558, 1338,
  2293, 51068], "temperature": 0.0, "avg_logprob": -0.0946647510972134, "compression_ratio":
  1.6835443037974684, "no_speech_prob": 0.001372458878904581}, {"id": 575, "seek":
  382392, "start": 3838.0, "end": 3844.88, "text": " and I want this experience to
  be as smooth as possible so that you can get started with the sample", "tokens":
  [51068, 293, 286, 528, 341, 1752, 281, 312, 382, 5508, 382, 1944, 370, 300, 291,
  393, 483, 1409, 365, 264, 6889, 51412], "temperature": 0.0, "avg_logprob": -0.0946647510972134,
  "compression_ratio": 1.6835443037974684, "no_speech_prob": 0.001372458878904581},
  {"id": 576, "seek": 382392, "start": 3844.88, "end": 3852.7200000000003, "text":
  " application run it locally get some data into it fire up your front and react
  and you can interact", "tokens": [51412, 3861, 1190, 309, 16143, 483, 512, 1412,
  666, 309, 2610, 493, 428, 1868, 293, 4515, 293, 291, 393, 4648, 51804], "temperature":
  0.0, "avg_logprob": -0.0946647510972134, "compression_ratio": 1.6835443037974684,
  "no_speech_prob": 0.001372458878904581}, {"id": 577, "seek": 385272, "start": 3852.72,
  "end": 3858.64, "text": " with it and if you''re happy with it if you want to share
  with your friends you can upload it to", "tokens": [50364, 365, 309, 293, 498, 291,
  434, 2055, 365, 309, 498, 291, 528, 281, 2073, 365, 428, 1855, 291, 393, 6580, 309,
  281, 50660], "temperature": 0.0, "avg_logprob": -0.13376969362782165, "compression_ratio":
  1.9208333333333334, "no_speech_prob": 0.003531272755935788}, {"id": 578, "seek":
  385272, "start": 3858.64, "end": 3863.8399999999997, "text": " the Westpac Cloud
  and then you can share to URL to your friends and that''s a model that I really",
  "tokens": [50660, 264, 4055, 79, 326, 8061, 293, 550, 291, 393, 2073, 281, 12905,
  281, 428, 1855, 293, 300, 311, 257, 2316, 300, 286, 534, 50920], "temperature":
  0.0, "avg_logprob": -0.13376969362782165, "compression_ratio": 1.9208333333333334,
  "no_speech_prob": 0.003531272755935788}, {"id": 579, "seek": 385272, "start": 3863.8399999999997,
  "end": 3868.8799999999997, "text": " believe in that you can it''s open source so
  you can actually run it locally and then you can", "tokens": [50920, 1697, 294,
  300, 291, 393, 309, 311, 1269, 4009, 370, 291, 393, 767, 1190, 309, 16143, 293,
  550, 291, 393, 51172], "temperature": 0.0, "avg_logprob": -0.13376969362782165,
  "compression_ratio": 1.9208333333333334, "no_speech_prob": 0.003531272755935788},
  {"id": 580, "seek": 385272, "start": 3868.8799999999997, "end": 3873.8399999999997,
  "text": " take the cloud provider can actually take care of the hosting for you
  so that''s", "tokens": [51172, 747, 264, 4588, 12398, 393, 767, 747, 1127, 295,
  264, 16058, 337, 291, 370, 300, 311, 51420], "temperature": 0.0, "avg_logprob":
  -0.13376969362782165, "compression_ratio": 1.9208333333333334, "no_speech_prob":
  0.003531272755935788}, {"id": 581, "seek": 385272, "start": 3875.12, "end": 3880.3999999999996,
  "text": " and right now we actually we are providing like free trials so you don''t
  you only need an email", "tokens": [51484, 293, 558, 586, 321, 767, 321, 366, 6530,
  411, 1737, 12450, 370, 291, 500, 380, 291, 787, 643, 364, 3796, 51748], "temperature":
  0.0, "avg_logprob": -0.13376969362782165, "compression_ratio": 1.9208333333333334,
  "no_speech_prob": 0.003531272755935788}, {"id": 582, "seek": 388040, "start": 3880.48,
  "end": 3884.56, "text": " address for the Westpac Cloud you don''t need a credit
  card or things like that so you can actually", "tokens": [50368, 2985, 337, 264,
  4055, 79, 326, 8061, 291, 500, 380, 643, 257, 5397, 2920, 420, 721, 411, 300, 370,
  291, 393, 767, 50572], "temperature": 0.0, "avg_logprob": -0.14439379085193982,
  "compression_ratio": 1.7740740740740741, "no_speech_prob": 0.0016540519427508116},
  {"id": 583, "seek": 388040, "start": 3884.56, "end": 3890.56, "text": " play it
  play with it and run with we can even leave a link where users can try out", "tokens":
  [50572, 862, 309, 862, 365, 309, 293, 1190, 365, 321, 393, 754, 1856, 257, 2113,
  689, 5022, 393, 853, 484, 50872], "temperature": 0.0, "avg_logprob": -0.14439379085193982,
  "compression_ratio": 1.7740740740740741, "no_speech_prob": 0.0016540519427508116},
  {"id": 584, "seek": 388040, "start": 3891.28, "end": 3896.2400000000002, "text":
  " Westpac and subscribe so I think that will be quite beneficial and actually I
  was thinking like even", "tokens": [50908, 4055, 79, 326, 293, 3022, 370, 286, 519,
  300, 486, 312, 1596, 14072, 293, 767, 286, 390, 1953, 411, 754, 51156], "temperature":
  0.0, "avg_logprob": -0.14439379085193982, "compression_ratio": 1.7740740740740741,
  "no_speech_prob": 0.0016540519427508116}, {"id": 585, "seek": 388040, "start": 3896.2400000000002,
  "end": 3902.8, "text": " though we a little bit drifted in our conversation away
  from better search you did mention the exciting", "tokens": [51156, 1673, 321, 257,
  707, 857, 19699, 292, 294, 527, 3761, 1314, 490, 1101, 3164, 291, 630, 2152, 264,
  4670, 51484], "temperature": 0.0, "avg_logprob": -0.14439379085193982, "compression_ratio":
  1.7740740740740741, "no_speech_prob": 0.0016540519427508116}, {"id": 586, "seek":
  388040, "start": 3902.8, "end": 3908.4, "text": " space of combining you know better
  search with smart search and I wanted to take it from the", "tokens": [51484, 1901,
  295, 21928, 291, 458, 1101, 3164, 365, 4069, 3164, 293, 286, 1415, 281, 747, 309,
  490, 264, 51764], "temperature": 0.0, "avg_logprob": -0.14439379085193982, "compression_ratio":
  1.7740740740740741, "no_speech_prob": 0.0016540519427508116}, {"id": 587, "seek":
  390840, "start": 3908.4, "end": 3914.96, "text": " angle of a non-technical user
  right so let''s say they come to you and they say Joe can you actually", "tokens":
  [50364, 5802, 295, 257, 2107, 12, 29113, 804, 4195, 558, 370, 718, 311, 584, 436,
  808, 281, 291, 293, 436, 584, 6807, 393, 291, 767, 50692], "temperature": 0.0, "avg_logprob":
  -0.11715237990669582, "compression_ratio": 1.7180616740088106, "no_speech_prob":
  0.0014938532840460539}, {"id": 588, "seek": 390840, "start": 3914.96, "end": 3920.4,
  "text": " enlighten me a little bit on how do I combine these things maybe I just
  want to deep my toe and", "tokens": [50692, 18690, 268, 385, 257, 707, 857, 322,
  577, 360, 286, 10432, 613, 721, 1310, 286, 445, 528, 281, 2452, 452, 13976, 293,
  50964], "temperature": 0.0, "avg_logprob": -0.11715237990669582, "compression_ratio":
  1.7180616740088106, "no_speech_prob": 0.0014938532840460539}, {"id": 589, "seek":
  390840, "start": 3920.4, "end": 3927.84, "text": " vector search just to see what
  it cannot cannot do in my domain what would you recommend them to do", "tokens":
  [50964, 8062, 3164, 445, 281, 536, 437, 309, 2644, 2644, 360, 294, 452, 9274, 437,
  576, 291, 2748, 552, 281, 360, 51336], "temperature": 0.0, "avg_logprob": -0.11715237990669582,
  "compression_ratio": 1.7180616740088106, "no_speech_prob": 0.0014938532840460539},
  {"id": 590, "seek": 390840, "start": 3927.84, "end": 3933.6800000000003, "text":
  " assuming that they already have maybe like a smart search engine and maybe they
  are evaluating", "tokens": [51336, 11926, 300, 436, 1217, 362, 1310, 411, 257, 4069,
  3164, 2848, 293, 1310, 436, 366, 27479, 51628], "temperature": 0.0, "avg_logprob":
  -0.11715237990669582, "compression_ratio": 1.7180616740088106, "no_speech_prob":
  0.0014938532840460539}, {"id": 591, "seek": 393368, "start": 3933.7599999999998,
  "end": 3946.08, "text": " Westpac as one candidate yeah so I think the question
  is if you''re using Westpac it''s rather", "tokens": [50368, 4055, 79, 326, 382,
  472, 11532, 1338, 370, 286, 519, 264, 1168, 307, 498, 291, 434, 1228, 4055, 79,
  326, 309, 311, 2831, 50984], "temperature": 0.0, "avg_logprob": -0.16778639088506284,
  "compression_ratio": 1.5666666666666667, "no_speech_prob": 0.005347550846636295},
  {"id": 592, "seek": 393368, "start": 3946.08, "end": 3951.12, "text": " easy to
  do this because you you can express it in the query and then you write the right
  key", "tokens": [50984, 1858, 281, 360, 341, 570, 291, 291, 393, 5109, 309, 294,
  264, 14581, 293, 550, 291, 2464, 264, 558, 2141, 51236], "temperature": 0.0, "avg_logprob":
  -0.16778639088506284, "compression_ratio": 1.5666666666666667, "no_speech_prob":
  0.005347550846636295}, {"id": 593, "seek": 393368, "start": 3951.12, "end": 3956.16,
  "text": " profiles saying that you know this is how going to combine the sparse
  ranking single for example", "tokens": [51236, 23693, 1566, 300, 291, 458, 341,
  307, 577, 516, 281, 10432, 264, 637, 11668, 17833, 2167, 337, 1365, 51488], "temperature":
  0.0, "avg_logprob": -0.16778639088506284, "compression_ratio": 1.5666666666666667,
  "no_speech_prob": 0.005347550846636295}, {"id": 594, "seek": 395616, "start": 3956.16,
  "end": 3964.0, "text": " be on 25 with retrieval for others that are not using Westpac
  using for example elastic search and", "tokens": [50364, 312, 322, 3552, 365, 19817,
  3337, 337, 2357, 300, 366, 406, 1228, 4055, 79, 326, 1228, 337, 1365, 17115, 3164,
  293, 50756], "temperature": 0.0, "avg_logprob": -0.24895044391074878, "compression_ratio":
  1.7731481481481481, "no_speech_prob": 0.0003182266082148999}, {"id": 595, "seek":
  395616, "start": 3964.56, "end": 3969.92, "text": " open source of our shesolar
  what we see is that they build a lot of infrastructure on top of", "tokens": [50784,
  1269, 4009, 295, 527, 402, 279, 401, 289, 437, 321, 536, 307, 300, 436, 1322, 257,
  688, 295, 6896, 322, 1192, 295, 51052], "temperature": 0.0, "avg_logprob": -0.24895044391074878,
  "compression_ratio": 1.7731481481481481, "no_speech_prob": 0.0003182266082148999},
  {"id": 596, "seek": 395616, "start": 3969.92, "end": 3976.72, "text": " these so
  they actually have the ranking layers outside of elastic search right so in that
  case is", "tokens": [51052, 613, 370, 436, 767, 362, 264, 17833, 7914, 2380, 295,
  17115, 3164, 558, 370, 294, 300, 1389, 307, 51392], "temperature": 0.0, "avg_logprob":
  -0.24895044391074878, "compression_ratio": 1.7731481481481481, "no_speech_prob":
  0.0003182266082148999}, {"id": 597, "seek": 395616, "start": 3976.72, "end": 3985.2,
  "text": " you could have kind of a vector search library running at the side of
  elastic search and then", "tokens": [51392, 291, 727, 362, 733, 295, 257, 8062,
  3164, 6405, 2614, 412, 264, 1252, 295, 17115, 3164, 293, 550, 51816], "temperature":
  0.0, "avg_logprob": -0.24895044391074878, "compression_ratio": 1.7731481481481481,
  "no_speech_prob": 0.0003182266082148999}, {"id": 598, "seek": 398520, "start": 3985.8399999999997,
  "end": 3991.6, "text": " retrieve and then you need to you need to keep those two
  data stores in sync and then you can", "tokens": [50396, 30254, 293, 550, 291, 643,
  281, 291, 643, 281, 1066, 729, 732, 1412, 9512, 294, 20271, 293, 550, 291, 393,
  50684], "temperature": 0.0, "avg_logprob": -0.08734472592671712, "compression_ratio":
  1.9077669902912622, "no_speech_prob": 0.000683339312672615}, {"id": 599, "seek":
  398520, "start": 3991.6, "end": 3999.6, "text": " in parallel fetch okay give me
  elastic search your best results and vector search database give me", "tokens":
  [50684, 294, 8952, 23673, 1392, 976, 385, 17115, 3164, 428, 1151, 3542, 293, 8062,
  3164, 8149, 976, 385, 51084], "temperature": 0.0, "avg_logprob": -0.08734472592671712,
  "compression_ratio": 1.9077669902912622, "no_speech_prob": 0.000683339312672615},
  {"id": 600, "seek": 398520, "start": 3999.6, "end": 4006.3999999999996, "text":
  " your best results and then you can use a technique called reciprocal rank fusion
  where you basically", "tokens": [51084, 428, 1151, 3542, 293, 550, 291, 393, 764,
  257, 6532, 1219, 46948, 6181, 23100, 689, 291, 1936, 51424], "temperature": 0.0,
  "avg_logprob": -0.08734472592671712, "compression_ratio": 1.9077669902912622, "no_speech_prob":
  0.000683339312672615}, {"id": 601, "seek": 398520, "start": 4006.3999999999996,
  "end": 4012.56, "text": " merged results based on you know are they are they ranking
  you know it''s the document found in both", "tokens": [51424, 36427, 3542, 2361,
  322, 291, 458, 366, 436, 366, 436, 17833, 291, 458, 309, 311, 264, 4166, 1352, 294,
  1293, 51732], "temperature": 0.0, "avg_logprob": -0.08734472592671712, "compression_ratio":
  1.9077669902912622, "no_speech_prob": 0.000683339312672615}, {"id": 602, "seek":
  401256, "start": 4013.52, "end": 4018.32, "text": " so that''s that''s a powerful
  technique of but you don''t have to actually know anything about", "tokens": [50412,
  370, 300, 311, 300, 311, 257, 4005, 6532, 295, 457, 291, 500, 380, 362, 281, 767,
  458, 1340, 466, 50652], "temperature": 0.0, "avg_logprob": -0.15275844486280418,
  "compression_ratio": 1.7327188940092166, "no_speech_prob": 0.00033098013955168426},
  {"id": 603, "seek": 401256, "start": 4018.32, "end": 4024.0, "text": " the distribution
  of ranking scores and so on so google is writing a lot about reciprocal rank", "tokens":
  [50652, 264, 7316, 295, 17833, 13444, 293, 370, 322, 370, 20742, 307, 3579, 257,
  688, 466, 46948, 6181, 50936], "temperature": 0.0, "avg_logprob": -0.15275844486280418,
  "compression_ratio": 1.7327188940092166, "no_speech_prob": 0.00033098013955168426},
  {"id": 604, "seek": 401256, "start": 4024.0, "end": 4030.56, "text": " fusion so
  it''s interesting direction and that''s one thing we know from Bing and from others
  from", "tokens": [50936, 23100, 370, 309, 311, 1880, 3513, 293, 300, 311, 472, 551,
  321, 458, 490, 30755, 293, 490, 2357, 490, 51264], "temperature": 0.0, "avg_logprob":
  -0.15275844486280418, "compression_ratio": 1.7327188940092166, "no_speech_prob":
  0.00033098013955168426}, {"id": 605, "seek": 401256, "start": 4030.56, "end": 4038.16,
  "text": " from both Bing and from bydo in in China is that they''re doing this kind
  of mix mix retrieval", "tokens": [51264, 490, 1293, 30755, 293, 490, 538, 2595,
  294, 294, 3533, 307, 300, 436, 434, 884, 341, 733, 295, 2890, 2890, 19817, 3337,
  51644], "temperature": 0.0, "avg_logprob": -0.15275844486280418, "compression_ratio":
  1.7327188940092166, "no_speech_prob": 0.00033098013955168426}, {"id": 606, "seek":
  403816, "start": 4039.12, "end": 4044.56, "text": " with different systems for sparse
  signals and then signals but but then you have for the regular", "tokens": [50412,
  365, 819, 3652, 337, 637, 11668, 12354, 293, 550, 12354, 457, 457, 550, 291, 362,
  337, 264, 3890, 50684], "temperature": 0.0, "avg_logprob": -0.23162523905436197,
  "compression_ratio": 1.8066037735849056, "no_speech_prob": 0.004440918564796448},
  {"id": 607, "seek": 403816, "start": 4044.56, "end": 4050.3199999999997, "text":
  " uses you have a lot of moving parts right you have different data stores make
  the manned ship", "tokens": [50684, 4960, 291, 362, 257, 688, 295, 2684, 3166, 558,
  291, 362, 819, 1412, 9512, 652, 264, 587, 9232, 5374, 50972], "temperature": 0.0,
  "avg_logprob": -0.23162523905436197, "compression_ratio": 1.8066037735849056, "no_speech_prob":
  0.004440918564796448}, {"id": 608, "seek": 403816, "start": 4050.3199999999997,
  "end": 4055.6, "text": " and that''s one of the things that we try to our advantage
  is that when you''re using Westbyes that", "tokens": [50972, 293, 300, 311, 472,
  295, 264, 721, 300, 321, 853, 281, 527, 5002, 307, 300, 562, 291, 434, 1228, 4055,
  2322, 279, 300, 51236], "temperature": 0.0, "avg_logprob": -0.23162523905436197,
  "compression_ratio": 1.8066037735849056, "no_speech_prob": 0.004440918564796448},
  {"id": 609, "seek": 403816, "start": 4056.3199999999997, "end": 4061.8399999999997,
  "text": " you know you you get these capabilities in the same engine you don''t
  need to store the data in", "tokens": [51272, 291, 458, 291, 291, 483, 613, 10862,
  294, 264, 912, 2848, 291, 500, 380, 643, 281, 3531, 264, 1412, 294, 51548], "temperature":
  0.0, "avg_logprob": -0.23162523905436197, "compression_ratio": 1.8066037735849056,
  "no_speech_prob": 0.004440918564796448}, {"id": 610, "seek": 406184, "start": 4061.84,
  "end": 4068.7200000000003, "text": " different stores and having consistency problems
  because of that yeah yeah so I will definitely", "tokens": [50364, 819, 9512, 293,
  1419, 14416, 2740, 570, 295, 300, 1338, 1338, 370, 286, 486, 2138, 50708], "temperature":
  0.0, "avg_logprob": -0.20454967169114102, "compression_ratio": 1.6755555555555555,
  "no_speech_prob": 0.00220703799277544}, {"id": 611, "seek": 406184, "start": 4068.7200000000003,
  "end": 4073.6800000000003, "text": " if you''re interested if you''re sitting there
  today with open source or or elastic search", "tokens": [50708, 498, 291, 434, 3102,
  498, 291, 434, 3798, 456, 965, 365, 1269, 4009, 420, 420, 17115, 3164, 50956], "temperature":
  0.0, "avg_logprob": -0.20454967169114102, "compression_ratio": 1.6755555555555555,
  "no_speech_prob": 0.00220703799277544}, {"id": 612, "seek": 406184, "start": 4074.88,
  "end": 4080.6400000000003, "text": " and you don''t want to invest in in in in the
  vast park you could try this batching the query", "tokens": [51016, 293, 291, 500,
  380, 528, 281, 1963, 294, 294, 294, 294, 264, 8369, 3884, 291, 727, 853, 341, 15245,
  278, 264, 14581, 51304], "temperature": 0.0, "avg_logprob": -0.20454967169114102,
  "compression_ratio": 1.6755555555555555, "no_speech_prob": 0.00220703799277544},
  {"id": 613, "seek": 406184, "start": 4080.6400000000003, "end": 4087.76, "text":
  " and doing reciprocal rank fusion yeah yeah it could be like one way to actually
  introduce something", "tokens": [51304, 293, 884, 46948, 6181, 23100, 1338, 1338,
  309, 727, 312, 411, 472, 636, 281, 767, 5366, 746, 51660], "temperature": 0.0, "avg_logprob":
  -0.20454967169114102, "compression_ratio": 1.6755555555555555, "no_speech_prob":
  0.00220703799277544}, {"id": 614, "seek": 408776, "start": 4087.84, "end": 4094.48,
  "text": " from more like semantic search if you view it that way right so that''s
  a great idea because I think", "tokens": [50368, 490, 544, 411, 47982, 3164, 498,
  291, 1910, 309, 300, 636, 558, 370, 300, 311, 257, 869, 1558, 570, 286, 519, 50700],
  "temperature": 0.0, "avg_logprob": -0.14632236256318934, "compression_ratio": 1.7327188940092166,
  "no_speech_prob": 0.00031861523166298866}, {"id": 615, "seek": 408776, "start":
  4095.6800000000003, "end": 4102.08, "text": " there are multiple approaches to this
  and I think if you are within one search engine", "tokens": [50760, 456, 366, 3866,
  11587, 281, 341, 293, 286, 519, 498, 291, 366, 1951, 472, 3164, 2848, 51080], "temperature":
  0.0, "avg_logprob": -0.14632236256318934, "compression_ratio": 1.7327188940092166,
  "no_speech_prob": 0.00031861523166298866}, {"id": 616, "seek": 408776, "start":
  4103.52, "end": 4109.12, "text": " like say VESPA or elastic search open search
  a solar would have you then I think you could in", "tokens": [51152, 411, 584, 691,
  2358, 10297, 420, 17115, 3164, 1269, 3164, 257, 7936, 576, 362, 291, 550, 286, 519,
  291, 727, 294, 51432], "temperature": 0.0, "avg_logprob": -0.14632236256318934,
  "compression_ratio": 1.7327188940092166, "no_speech_prob": 0.00031861523166298866},
  {"id": 617, "seek": 408776, "start": 4109.12, "end": 4116.72, "text": " principle
  experiment with like fusing you know the neural search result with sparse search
  using", "tokens": [51432, 8665, 5120, 365, 411, 283, 7981, 291, 458, 264, 18161,
  3164, 1874, 365, 637, 11668, 3164, 1228, 51812], "temperature": 0.0, "avg_logprob":
  -0.14632236256318934, "compression_ratio": 1.7327188940092166, "no_speech_prob":
  0.00031861523166298866}, {"id": 618, "seek": 411672, "start": 4116.72, "end": 4123.92,
  "text": " some kind of linear combination as you actually retrieve it right yeah
  so so so so you so you can", "tokens": [50364, 512, 733, 295, 8213, 6562, 382, 291,
  767, 30254, 309, 558, 1338, 370, 370, 370, 370, 291, 370, 291, 393, 50724], "temperature":
  0.0, "avg_logprob": -0.1170221306811804, "compression_ratio": 1.835680751173709,
  "no_speech_prob": 0.0007419881876558065}, {"id": 619, "seek": 411672, "start": 4123.92,
  "end": 4129.12, "text": " actually use the linear combination but the great thing
  about this rank fusion is that you don''t", "tokens": [50724, 767, 764, 264, 8213,
  6562, 457, 264, 869, 551, 466, 341, 6181, 23100, 307, 300, 291, 500, 380, 50984],
  "temperature": 0.0, "avg_logprob": -0.1170221306811804, "compression_ratio": 1.835680751173709,
  "no_speech_prob": 0.0007419881876558065}, {"id": 620, "seek": 411672, "start": 4129.12,
  "end": 4136.0, "text": " simply you don''t look at the ranking scores so you basically
  just fuse them by the order of their", "tokens": [50984, 2935, 291, 500, 380, 574,
  412, 264, 17833, 13444, 370, 291, 1936, 445, 31328, 552, 538, 264, 1668, 295, 641,
  51328], "temperature": 0.0, "avg_logprob": -0.1170221306811804, "compression_ratio":
  1.835680751173709, "no_speech_prob": 0.0007419881876558065}, {"id": 621, "seek":
  411672, "start": 4136.0, "end": 4142.8, "text": " returns so you don''t have to
  know anything about the score distribution like EM25 it has basically", "tokens":
  [51328, 11247, 370, 291, 500, 380, 362, 281, 458, 1340, 466, 264, 6175, 7316, 411,
  16237, 6074, 309, 575, 1936, 51668], "temperature": 0.0, "avg_logprob": -0.1170221306811804,
  "compression_ratio": 1.835680751173709, "no_speech_prob": 0.0007419881876558065},
  {"id": 622, "seek": 414280, "start": 4142.8, "end": 4150.56, "text": " unbounded
  it could be 25 it could be 100 to be 5 right so it''s very difficult to to to combine
  that", "tokens": [50364, 517, 18767, 292, 309, 727, 312, 3552, 309, 727, 312, 2319,
  281, 312, 1025, 558, 370, 309, 311, 588, 2252, 281, 281, 281, 10432, 300, 50752],
  "temperature": 0.0, "avg_logprob": -0.17413631900326237, "compression_ratio": 1.6796536796536796,
  "no_speech_prob": 0.0005067753954790533}, {"id": 623, "seek": 414280, "start": 4150.56,
  "end": 4156.16, "text": " using a linear model because you have two signals you
  know and one is number is going to be like this", "tokens": [50752, 1228, 257, 8213,
  2316, 570, 291, 362, 732, 12354, 291, 458, 293, 472, 307, 1230, 307, 516, 281, 312,
  411, 341, 51032], "temperature": 0.0, "avg_logprob": -0.17413631900326237, "compression_ratio":
  1.6796536796536796, "no_speech_prob": 0.0005067753954790533}, {"id": 624, "seek":
  414280, "start": 4156.16, "end": 4162.56, "text": " and now it was going to be between
  0 and 1 so reciprocal rank fusion is definitely you know", "tokens": [51032, 293,
  586, 309, 390, 516, 281, 312, 1296, 1958, 293, 502, 370, 46948, 6181, 23100, 307,
  2138, 291, 458, 51352], "temperature": 0.0, "avg_logprob": -0.17413631900326237,
  "compression_ratio": 1.6796536796536796, "no_speech_prob": 0.0005067753954790533},
  {"id": 625, "seek": 414280, "start": 4163.6, "end": 4170.400000000001, "text": "
  interesting case actually this is super great point and hopefully we can provide
  some links to", "tokens": [51404, 1880, 1389, 767, 341, 307, 1687, 869, 935, 293,
  4696, 321, 393, 2893, 512, 6123, 281, 51744], "temperature": 0.0, "avg_logprob":
  -0.17413631900326237, "compression_ratio": 1.6796536796536796, "no_speech_prob":
  0.0005067753954790533}, {"id": 626, "seek": 417040, "start": 4170.48, "end": 4176.879999999999,
  "text": " this because this technique because I think I heard this question multiple
  times that would you", "tokens": [50368, 341, 570, 341, 6532, 570, 286, 519, 286,
  2198, 341, 1168, 3866, 1413, 300, 576, 291, 50688], "temperature": 0.0, "avg_logprob":
  -0.10547225446586149, "compression_ratio": 1.7813953488372094, "no_speech_prob":
  0.0018489620415493846}, {"id": 627, "seek": 417040, "start": 4176.879999999999,
  "end": 4184.0, "text": " set exactly just now that the score space is completely
  different and they are not compatible with", "tokens": [50688, 992, 2293, 445, 586,
  300, 264, 6175, 1901, 307, 2584, 819, 293, 436, 366, 406, 18218, 365, 51044], "temperature":
  0.0, "avg_logprob": -0.10547225446586149, "compression_ratio": 1.7813953488372094,
  "no_speech_prob": 0.0018489620415493846}, {"id": 628, "seek": 417040, "start": 4184.0,
  "end": 4191.679999999999, "text": " each other and so you have to find a way to
  still interleave them or merge them right so that", "tokens": [51044, 1184, 661,
  293, 370, 291, 362, 281, 915, 257, 636, 281, 920, 728, 306, 946, 552, 420, 22183,
  552, 558, 370, 300, 51428], "temperature": 0.0, "avg_logprob": -0.10547225446586149,
  "compression_ratio": 1.7813953488372094, "no_speech_prob": 0.0018489620415493846},
  {"id": 629, "seek": 417040, "start": 4192.719999999999, "end": 4197.5199999999995,
  "text": " would you set exactly makes sense that you don''t pay attention to the
  score space you actually", "tokens": [51480, 576, 291, 992, 2293, 1669, 2020, 300,
  291, 500, 380, 1689, 3202, 281, 264, 6175, 1901, 291, 767, 51720], "temperature":
  0.0, "avg_logprob": -0.10547225446586149, "compression_ratio": 1.7813953488372094,
  "no_speech_prob": 0.0018489620415493846}, {"id": 630, "seek": 419752, "start": 4197.52,
  "end": 4204.72, "text": " look at the order and you try your best to interleave
  them yeah that makes total sense yeah yeah", "tokens": [50364, 574, 412, 264, 1668,
  293, 291, 853, 428, 1151, 281, 728, 306, 946, 552, 1338, 300, 1669, 3217, 2020,
  1338, 1338, 50724], "temperature": 0.0, "avg_logprob": -0.17798460535256258, "compression_ratio":
  1.7442922374429224, "no_speech_prob": 0.0006731762550771236}, {"id": 631, "seek":
  419752, "start": 4205.52, "end": 4211.52, "text": " there was actually a recent
  recent paper on because there has been more interest in that these", "tokens": [50764,
  456, 390, 767, 257, 5162, 5162, 3035, 322, 570, 456, 575, 668, 544, 1179, 294, 300,
  613, 51064], "temperature": 0.0, "avg_logprob": -0.17798460535256258, "compression_ratio":
  1.7442922374429224, "no_speech_prob": 0.0006731762550771236}, {"id": 632, "seek":
  419752, "start": 4211.52, "end": 4217.92, "text": " dense models alone that they
  generalize not that well what you''re using out of domain and one of", "tokens":
  [51064, 18011, 5245, 3312, 300, 436, 2674, 1125, 406, 300, 731, 437, 291, 434, 1228,
  484, 295, 9274, 293, 472, 295, 51384], "temperature": 0.0, "avg_logprob": -0.17798460535256258,
  "compression_ratio": 1.7442922374429224, "no_speech_prob": 0.0006731762550771236},
  {"id": 633, "seek": 419752, "start": 4217.92, "end": 4223.84, "text": " the things
  that the Google researchers were doing and showed promising results was using this",
  "tokens": [51384, 264, 721, 300, 264, 3329, 10309, 645, 884, 293, 4712, 20257, 3542,
  390, 1228, 341, 51680], "temperature": 0.0, "avg_logprob": -0.17798460535256258,
  "compression_ratio": 1.7442922374429224, "no_speech_prob": 0.0006731762550771236},
  {"id": 634, "seek": 422384, "start": 4223.84, "end": 4230.72, "text": " rank fusion
  and I''ve seen this rank fusion in a multiple Google papers so so it''s very interesting",
  "tokens": [50364, 6181, 23100, 293, 286, 600, 1612, 341, 6181, 23100, 294, 257,
  3866, 3329, 10577, 370, 370, 309, 311, 588, 1880, 50708], "temperature": 0.0, "avg_logprob":
  -0.17916328566414969, "compression_ratio": 1.7105263157894737, "no_speech_prob":
  0.001993240090087056}, {"id": 635, "seek": 422384, "start": 4230.72, "end": 4238.72,
  "text": " the researchers they''re really interested in reciprocal rank fusion so
  yeah sounds like a popular", "tokens": [50708, 264, 10309, 436, 434, 534, 3102,
  294, 46948, 6181, 23100, 370, 1338, 3263, 411, 257, 3743, 51108], "temperature":
  0.0, "avg_logprob": -0.17916328566414969, "compression_ratio": 1.7105263157894737,
  "no_speech_prob": 0.001993240090087056}, {"id": 636, "seek": 422384, "start": 4238.72,
  "end": 4246.0, "text": " technique yes I mean time flies and I really enjoy talking
  it feels like we could record another", "tokens": [51108, 6532, 2086, 286, 914,
  565, 17414, 293, 286, 534, 2103, 1417, 309, 3417, 411, 321, 727, 2136, 1071, 51472],
  "temperature": 0.0, "avg_logprob": -0.17916328566414969, "compression_ratio": 1.7105263157894737,
  "no_speech_prob": 0.001993240090087056}, {"id": 637, "seek": 422384, "start": 4246.0,
  "end": 4252.72, "text": " podcast what do you think I''m talking multiple topics
  but I still really love to pick a brain on", "tokens": [51472, 7367, 437, 360, 291,
  519, 286, 478, 1417, 3866, 8378, 457, 286, 920, 534, 959, 281, 1888, 257, 3567,
  322, 51808], "temperature": 0.0, "avg_logprob": -0.17916328566414969, "compression_ratio":
  1.7105263157894737, "no_speech_prob": 0.001993240090087056}, {"id": 638, "seek":
  425272, "start": 4252.8, "end": 4264.400000000001, "text": " that philosophical
  question and kind of ask you what what keeps you so interested like you are a",
  "tokens": [50368, 300, 25066, 1168, 293, 733, 295, 1029, 291, 437, 437, 5965, 291,
  370, 3102, 411, 291, 366, 257, 50948], "temperature": 0.0, "avg_logprob": -0.1546521027882894,
  "compression_ratio": 1.5769230769230769, "no_speech_prob": 0.0005918564274907112},
  {"id": 639, "seek": 425272, "start": 4264.400000000001, "end": 4271.12, "text":
  " loudmouth behind West Pine general but you also offer a bunch of advice right
  like through your", "tokens": [50948, 6588, 22357, 2261, 4055, 33531, 2674, 457,
  291, 611, 2626, 257, 3840, 295, 5192, 558, 411, 807, 428, 51284], "temperature":
  0.0, "avg_logprob": -0.1546521027882894, "compression_ratio": 1.5769230769230769,
  "no_speech_prob": 0.0005918564274907112}, {"id": 640, "seek": 425272, "start": 4271.12,
  "end": 4277.12, "text": " blogs through your public presentations and even sharing
  papers on Twitter at least for me was", "tokens": [51284, 31038, 807, 428, 1908,
  18964, 293, 754, 5414, 10577, 322, 5794, 412, 1935, 337, 385, 390, 51584], "temperature":
  0.0, "avg_logprob": -0.1546521027882894, "compression_ratio": 1.5769230769230769,
  "no_speech_prob": 0.0005918564274907112}, {"id": 641, "seek": 427712, "start": 4277.12,
  "end": 4283.84, "text": " super helpful that I could you know quickly read the paper
  that you shared but what keeps you", "tokens": [50364, 1687, 4961, 300, 286, 727,
  291, 458, 2661, 1401, 264, 3035, 300, 291, 5507, 457, 437, 5965, 291, 50700], "temperature":
  0.0, "avg_logprob": -0.10353815102879005, "compression_ratio": 1.6803652968036529,
  "no_speech_prob": 0.0009478465071879327}, {"id": 642, "seek": 427712, "start": 4283.84,
  "end": 4290.4, "text": " motivated and interested to stay in this field and also
  specifically you know maybe you think", "tokens": [50700, 14515, 293, 3102, 281,
  1754, 294, 341, 2519, 293, 611, 4682, 291, 458, 1310, 291, 519, 51028], "temperature":
  0.0, "avg_logprob": -0.10353815102879005, "compression_ratio": 1.6803652968036529,
  "no_speech_prob": 0.0009478465071879327}, {"id": 643, "seek": 427712, "start": 4290.4,
  "end": 4296.72, "text": " something is missing in the vector search space or in
  general in in search space that you would like", "tokens": [51028, 746, 307, 5361,
  294, 264, 8062, 3164, 1901, 420, 294, 2674, 294, 294, 3164, 1901, 300, 291, 576,
  411, 51344], "temperature": 0.0, "avg_logprob": -0.10353815102879005, "compression_ratio":
  1.6803652968036529, "no_speech_prob": 0.0009478465071879327}, {"id": 644, "seek":
  427712, "start": 4296.72, "end": 4307.04, "text": " to fix yeah so it''s a great
  philosophical question I think I''m not that excited", "tokens": [51344, 281, 3191,
  1338, 370, 309, 311, 257, 869, 25066, 1168, 286, 519, 286, 478, 406, 300, 2919,
  51860], "temperature": 0.0, "avg_logprob": -0.10353815102879005, "compression_ratio":
  1.6803652968036529, "no_speech_prob": 0.0009478465071879327}, {"id": 645, "seek":
  430712, "start": 4307.12, "end": 4315.76, "text": " about vector search I see that
  as a technique so I''m more like excited about search because I think", "tokens":
  [50364, 466, 8062, 3164, 286, 536, 300, 382, 257, 6532, 370, 286, 478, 544, 411,
  2919, 466, 3164, 570, 286, 519, 50796], "temperature": 0.0, "avg_logprob": -0.13897228240966797,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.001989323878660798},
  {"id": 646, "seek": 430712, "start": 4315.76, "end": 4321.599999999999, "text":
  " it''s such a fascinating problem we touched on it before you know you have query
  categorization", "tokens": [50796, 309, 311, 1270, 257, 10343, 1154, 321, 9828,
  322, 309, 949, 291, 458, 291, 362, 14581, 19250, 2144, 51088], "temperature": 0.0,
  "avg_logprob": -0.13897228240966797, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.001989323878660798}, {"id": 647, "seek": 430712, "start": 4321.599999999999, "end":
  4328.64, "text": " spelling you have so many different aspects of building a great
  search experience and also the", "tokens": [51088, 22254, 291, 362, 370, 867, 819,
  7270, 295, 2390, 257, 869, 3164, 1752, 293, 611, 264, 51440], "temperature": 0.0,
  "avg_logprob": -0.13897228240966797, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.001989323878660798}, {"id": 648, "seek": 430712, "start": 4328.64, "end": 4334.64,
  "text": " scale thing is really appealing for me you know kind of passionate about
  you know how can we do this", "tokens": [51440, 4373, 551, 307, 534, 23842, 337,
  385, 291, 458, 733, 295, 11410, 466, 291, 458, 577, 393, 321, 360, 341, 51740],
  "temperature": 0.0, "avg_logprob": -0.13897228240966797, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.001989323878660798}, {"id": 649, "seek": 433464, "start": 4334.72,
  "end": 4340.8, "text": " billion scale how can we make it fast you know what if
  we need 100,000 queries per second what if", "tokens": [50368, 5218, 4373, 577,
  393, 321, 652, 309, 2370, 291, 458, 437, 498, 321, 643, 2319, 11, 1360, 24109, 680,
  1150, 437, 498, 50672], "temperature": 0.0, "avg_logprob": -0.13269922766886966,
  "compression_ratio": 1.6444444444444444, "no_speech_prob": 0.0014623100869357586},
  {"id": 650, "seek": 433464, "start": 4340.8, "end": 4348.88, "text": " we need to
  update all the documents in real time and within 12 hours or one hour or you know
  where''s", "tokens": [50672, 321, 643, 281, 5623, 439, 264, 8512, 294, 957, 565,
  293, 1951, 2272, 2496, 420, 472, 1773, 420, 291, 458, 689, 311, 51076], "temperature":
  0.0, "avg_logprob": -0.13269922766886966, "compression_ratio": 1.6444444444444444,
  "no_speech_prob": 0.0014623100869357586}, {"id": 651, "seek": 433464, "start": 4348.88,
  "end": 4357.92, "text": " the limits you know where is the cloud going you know
  this compute versus storage can we now move", "tokens": [51076, 264, 10406, 291,
  458, 689, 307, 264, 4588, 516, 291, 458, 341, 14722, 5717, 6725, 393, 321, 586,
  1286, 51528], "temperature": 0.0, "avg_logprob": -0.13269922766886966, "compression_ratio":
  1.6444444444444444, "no_speech_prob": 0.0014623100869357586}, {"id": 652, "seek":
  435792, "start": 4358.88, "end": 4365.68, "text": " more computations out of the
  storage layer there are a lot of these exciting on the kind of system", "tokens":
  [50412, 544, 2807, 763, 484, 295, 264, 6725, 4583, 456, 366, 257, 688, 295, 613,
  4670, 322, 264, 733, 295, 1185, 50752], "temperature": 0.0, "avg_logprob": -0.1777720658675484,
  "compression_ratio": 1.7644444444444445, "no_speech_prob": 0.0009034093818627298},
  {"id": 653, "seek": 435792, "start": 4365.68, "end": 4371.92, "text": " things but
  on them kind of more science things you know how to build a great search experience
  I think", "tokens": [50752, 721, 457, 322, 552, 733, 295, 544, 3497, 721, 291, 458,
  577, 281, 1322, 257, 869, 3164, 1752, 286, 519, 51064], "temperature": 0.0, "avg_logprob":
  -0.1777720658675484, "compression_ratio": 1.7644444444444445, "no_speech_prob":
  0.0009034093818627298}, {"id": 654, "seek": 435792, "start": 4371.92, "end": 4378.0,
  "text": " you need to have this kind of multiple techniques and we didn''t touch
  on it but vector search is", "tokens": [51064, 291, 643, 281, 362, 341, 733, 295,
  3866, 7512, 293, 321, 994, 380, 2557, 322, 309, 457, 8062, 3164, 307, 51368], "temperature":
  0.0, "avg_logprob": -0.1777720658675484, "compression_ratio": 1.7644444444444445,
  "no_speech_prob": 0.0009034093818627298}, {"id": 655, "seek": 435792, "start": 4378.0,
  "end": 4386.0, "text": " one thing sparse search is one other but GBDT models tree
  based models is really ruling the search", "tokens": [51368, 472, 551, 637, 11668,
  3164, 307, 472, 661, 457, 460, 33, 35, 51, 5245, 4230, 2361, 5245, 307, 534, 21437,
  264, 3164, 51768], "temperature": 0.0, "avg_logprob": -0.1777720658675484, "compression_ratio":
  1.7644444444444445, "no_speech_prob": 0.0009034093818627298}, {"id": 656, "seek":
  438600, "start": 4386.16, "end": 4393.6, "text": " or it''s kind of the hammer of
  search because those models on tabular data statistical features", "tokens": [50372,
  420, 309, 311, 733, 295, 264, 13017, 295, 3164, 570, 729, 5245, 322, 4421, 1040,
  1412, 22820, 4122, 50744], "temperature": 0.0, "avg_logprob": -0.14175045911003561,
  "compression_ratio": 1.6163793103448276, "no_speech_prob": 0.0004085246182512492},
  {"id": 657, "seek": 438600, "start": 4393.6, "end": 4398.8, "text": " you know they
  really show promising results and that''s another thing that I think is great",
  "tokens": [50744, 291, 458, 436, 534, 855, 20257, 3542, 293, 300, 311, 1071, 551,
  300, 286, 519, 307, 869, 51004], "temperature": 0.0, "avg_logprob": -0.14175045911003561,
  "compression_ratio": 1.6163793103448276, "no_speech_prob": 0.0004085246182512492},
  {"id": 658, "seek": 438600, "start": 4398.8, "end": 4404.64, "text": " than about
  west based that you can combine these GBDT models newer metals in the same ranking",
  "tokens": [51004, 813, 466, 7009, 2361, 300, 291, 393, 10432, 613, 460, 33, 35,
  51, 5245, 17628, 22548, 294, 264, 912, 17833, 51296], "temperature": 0.0, "avg_logprob":
  -0.14175045911003561, "compression_ratio": 1.6163793103448276, "no_speech_prob":
  0.0004085246182512492}, {"id": 659, "seek": 438600, "start": 4404.64, "end": 4412.0,
  "text": " functions I don''t think that there''s a one single silver bullet for
  retrieval I think there are", "tokens": [51296, 6828, 286, 500, 380, 519, 300, 456,
  311, 257, 472, 2167, 8753, 11632, 337, 19817, 3337, 286, 519, 456, 366, 51664],
  "temperature": 0.0, "avg_logprob": -0.14175045911003561, "compression_ratio": 1.6163793103448276,
  "no_speech_prob": 0.0004085246182512492}, {"id": 660, "seek": 441200, "start": 4412.0,
  "end": 4417.68, "text": " multiple different singles like for instance let''s let''s
  do vector search if you only do vector", "tokens": [50364, 3866, 819, 36334, 411,
  337, 5197, 718, 311, 718, 311, 360, 8062, 3164, 498, 291, 787, 360, 8062, 50648],
  "temperature": 0.0, "avg_logprob": -0.14105597487441054, "compression_ratio": 1.9637096774193548,
  "no_speech_prob": 0.002578939311206341}, {"id": 661, "seek": 441200, "start": 4417.68,
  "end": 4424.48, "text": " search if Google only did vector search only on the text
  right it would basically you have a lot", "tokens": [50648, 3164, 498, 3329, 787,
  630, 8062, 3164, 787, 322, 264, 2487, 558, 309, 576, 1936, 291, 362, 257, 688, 50988],
  "temperature": 0.0, "avg_logprob": -0.14105597487441054, "compression_ratio": 1.9637096774193548,
  "no_speech_prob": 0.002578939311206341}, {"id": 662, "seek": 441200, "start": 4424.48,
  "end": 4430.72, "text": " of duplicates on the web you have low quality content
  you know there''s page rank there other factors", "tokens": [50988, 295, 17154,
  1024, 322, 264, 3670, 291, 362, 2295, 3125, 2701, 291, 458, 456, 311, 3028, 6181,
  456, 661, 6771, 51300], "temperature": 0.0, "avg_logprob": -0.14105597487441054,
  "compression_ratio": 1.9637096774193548, "no_speech_prob": 0.002578939311206341},
  {"id": 663, "seek": 441200, "start": 4430.72, "end": 4436.64, "text": " you know
  it''s not only vector search there''s that kind of different techniques so and so
  that", "tokens": [51300, 291, 458, 309, 311, 406, 787, 8062, 3164, 456, 311, 300,
  733, 295, 819, 7512, 370, 293, 370, 300, 51596], "temperature": 0.0, "avg_logprob":
  -0.14105597487441054, "compression_ratio": 1.9637096774193548, "no_speech_prob":
  0.002578939311206341}, {"id": 664, "seek": 441200, "start": 4436.64, "end": 4441.44,
  "text": " means also that there''s a lot of things new things to learn you know
  how do you do caricaturization", "tokens": [51596, 1355, 611, 300, 456, 311, 257,
  688, 295, 721, 777, 721, 281, 1466, 291, 458, 577, 360, 291, 360, 45732, 267, 374,
  2144, 51836], "temperature": 0.0, "avg_logprob": -0.14105597487441054, "compression_ratio":
  1.9637096774193548, "no_speech_prob": 0.002578939311206341}, {"id": 665, "seek":
  444144, "start": 4441.44, "end": 4448.5599999999995, "text": " you know how do you
  how do you how do you actually determine which facets and then kind of navigation",
  "tokens": [50364, 291, 458, 577, 360, 291, 577, 360, 291, 577, 360, 291, 767, 6997,
  597, 49752, 293, 550, 733, 295, 17346, 50720], "temperature": 0.0, "avg_logprob":
  -0.09995260573270028, "compression_ratio": 1.8576923076923078, "no_speech_prob":
  0.0009046139311976731}, {"id": 666, "seek": 444144, "start": 4448.5599999999995,
  "end": 4455.5199999999995, "text": " you''re going to show to the user and like
  you touched on at the start you know if your user does", "tokens": [50720, 291,
  434, 516, 281, 855, 281, 264, 4195, 293, 411, 291, 9828, 322, 412, 264, 722, 291,
  458, 498, 428, 4195, 775, 51068], "temperature": 0.0, "avg_logprob": -0.09995260573270028,
  "compression_ratio": 1.8576923076923078, "no_speech_prob": 0.0009046139311976731},
  {"id": 667, "seek": 444144, "start": 4455.5199999999995, "end": 4461.28, "text":
  " a query and we don''t have any good results you know should we just slow them
  some random results", "tokens": [51068, 257, 14581, 293, 321, 500, 380, 362, 604,
  665, 3542, 291, 458, 820, 321, 445, 2964, 552, 512, 4974, 3542, 51356], "temperature":
  0.0, "avg_logprob": -0.09995260573270028, "compression_ratio": 1.8576923076923078,
  "no_speech_prob": 0.0009046139311976731}, {"id": 668, "seek": 444144, "start": 4461.28,
  "end": 4466.0, "text": " or should they say that hey you know I''m sorry but we
  don''t have anything for your query so", "tokens": [51356, 420, 820, 436, 584, 300,
  4177, 291, 458, 286, 478, 2597, 457, 321, 500, 380, 362, 1340, 337, 428, 14581,
  370, 51592], "temperature": 0.0, "avg_logprob": -0.09995260573270028, "compression_ratio":
  1.8576923076923078, "no_speech_prob": 0.0009046139311976731}, {"id": 669, "seek":
  444144, "start": 4466.0, "end": 4470.799999999999, "text": " yeah that''s really
  what motivates me is that it''s such a fantastic problem if you''re interested",
  "tokens": [51592, 1338, 300, 311, 534, 437, 42569, 385, 307, 300, 309, 311, 1270,
  257, 5456, 1154, 498, 291, 434, 3102, 51832], "temperature": 0.0, "avg_logprob":
  -0.09995260573270028, "compression_ratio": 1.8576923076923078, "no_speech_prob":
  0.0009046139311976731}, {"id": 670, "seek": 447080, "start": 4470.8, "end": 4477.52,
  "text": " in scale and all these kind of things coming together so yeah yeah thanks
  for that it''s deep and", "tokens": [50364, 294, 4373, 293, 439, 613, 733, 295,
  721, 1348, 1214, 370, 1338, 1338, 3231, 337, 300, 309, 311, 2452, 293, 50700], "temperature":
  0.0, "avg_logprob": -0.09366100392443069, "compression_ratio": 1.7444933920704846,
  "no_speech_prob": 0.0006980682956054807}, {"id": 671, "seek": 447080, "start": 4477.52,
  "end": 4486.24, "text": " it''s very wide and I think it''s like limitless space
  and I hope also that newcomers feel it''s kind", "tokens": [50700, 309, 311, 588,
  4874, 293, 286, 519, 309, 311, 411, 4948, 1832, 1901, 293, 286, 1454, 611, 300,
  40014, 433, 841, 309, 311, 733, 51136], "temperature": 0.0, "avg_logprob": -0.09366100392443069,
  "compression_ratio": 1.7444933920704846, "no_speech_prob": 0.0006980682956054807},
  {"id": 672, "seek": 447080, "start": 4486.24, "end": 4492.16, "text": " of like
  a low bar entry especially and we didn''t touch on this but especially with your
  work and", "tokens": [51136, 295, 411, 257, 2295, 2159, 8729, 2318, 293, 321, 994,
  380, 2557, 322, 341, 457, 2318, 365, 428, 589, 293, 51432], "temperature": 0.0,
  "avg_logprob": -0.09366100392443069, "compression_ratio": 1.7444933920704846, "no_speech_prob":
  0.0006980682956054807}, {"id": 673, "seek": 447080, "start": 4492.16, "end": 4500.08,
  "text": " open source you know the support like you can go and slack or whatever
  tool you''re using to communicate", "tokens": [51432, 1269, 4009, 291, 458, 264,
  1406, 411, 291, 393, 352, 293, 29767, 420, 2035, 2290, 291, 434, 1228, 281, 7890,
  51828], "temperature": 0.0, "avg_logprob": -0.09366100392443069, "compression_ratio":
  1.7444933920704846, "no_speech_prob": 0.0006980682956054807}, {"id": 674, "seek":
  450008, "start": 4500.08, "end": 4508.0, "text": " with your users and actually
  listen and address their concerns questions and hopefully this", "tokens": [50364,
  365, 428, 5022, 293, 767, 2140, 293, 2985, 641, 7389, 1651, 293, 4696, 341, 50760],
  "temperature": 0.0, "avg_logprob": -0.11716015715348094, "compression_ratio": 1.9282051282051282,
  "no_speech_prob": 0.0008709453977644444}, {"id": 675, "seek": 450008, "start": 4508.0,
  "end": 4516.64, "text": " opens more you know more possibilities for newcomers to
  enter yeah I love I love actually", "tokens": [50760, 9870, 544, 291, 458, 544,
  12178, 337, 40014, 433, 281, 3242, 1338, 286, 959, 286, 959, 767, 51192], "temperature":
  0.0, "avg_logprob": -0.11716015715348094, "compression_ratio": 1.9282051282051282,
  "no_speech_prob": 0.0008709453977644444}, {"id": 676, "seek": 450008, "start": 4517.6,
  "end": 4522.4, "text": " it''s actually a weakness as well but I love answering
  questions you know you can see me answering", "tokens": [51240, 309, 311, 767, 257,
  12772, 382, 731, 457, 286, 959, 13430, 1651, 291, 458, 291, 393, 536, 385, 13430,
  51480], "temperature": 0.0, "avg_logprob": -0.11716015715348094, "compression_ratio":
  1.9282051282051282, "no_speech_prob": 0.0008709453977644444}, {"id": 677, "seek":
  450008, "start": 4522.4, "end": 4527.84, "text": " questions on multiple slack spaces
  you know I love people you know asking questions about search", "tokens": [51480,
  1651, 322, 3866, 29767, 7673, 291, 458, 286, 959, 561, 291, 458, 3365, 1651, 466,
  3164, 51752], "temperature": 0.0, "avg_logprob": -0.11716015715348094, "compression_ratio":
  1.9282051282051282, "no_speech_prob": 0.0008709453977644444}, {"id": 678, "seek":
  452784, "start": 4527.84, "end": 4535.52, "text": " so I really love that and I''m
  and what really gets me if someone is struggling with something you know", "tokens":
  [50364, 370, 286, 534, 959, 300, 293, 286, 478, 293, 437, 534, 2170, 385, 498, 1580,
  307, 9314, 365, 746, 291, 458, 50748], "temperature": 0.0, "avg_logprob": -0.13298741897734084,
  "compression_ratio": 1.8364485981308412, "no_speech_prob": 0.0019649919122457504},
  {"id": 679, "seek": 452784, "start": 4535.52, "end": 4541.4400000000005, "text":
  " how can I do this with West Park and I''ll try to explain it you know you have
  to do this and that", "tokens": [50748, 577, 393, 286, 360, 341, 365, 4055, 4964,
  293, 286, 603, 853, 281, 2903, 309, 291, 458, 291, 362, 281, 360, 341, 293, 300,
  51044], "temperature": 0.0, "avg_logprob": -0.13298741897734084, "compression_ratio":
  1.8364485981308412, "no_speech_prob": 0.0019649919122457504}, {"id": 680, "seek":
  452784, "start": 4541.4400000000005, "end": 4545.84, "text": " you know and then
  I like I go back you know at the program saying you know we need to fix this you",
  "tokens": [51044, 291, 458, 293, 550, 286, 411, 286, 352, 646, 291, 458, 412, 264,
  1461, 1566, 291, 458, 321, 643, 281, 3191, 341, 291, 51264], "temperature": 0.0,
  "avg_logprob": -0.13298741897734084, "compression_ratio": 1.8364485981308412, "no_speech_prob":
  0.0019649919122457504}, {"id": 681, "seek": 452784, "start": 4545.84, "end": 4552.400000000001,
  "text": " know we need to make this more easy for people to use right so it''s it''s
  a both way thing and", "tokens": [51264, 458, 321, 643, 281, 652, 341, 544, 1858,
  337, 561, 281, 764, 558, 370, 309, 311, 309, 311, 257, 1293, 636, 551, 293, 51592],
  "temperature": 0.0, "avg_logprob": -0.13298741897734084, "compression_ratio": 1.8364485981308412,
  "no_speech_prob": 0.0019649919122457504}, {"id": 682, "seek": 455240, "start": 4552.48,
  "end": 4557.759999999999, "text": " that''s one thing that I learned in my career
  is that you know listen carefully to your users", "tokens": [50368, 300, 311, 472,
  551, 300, 286, 3264, 294, 452, 3988, 307, 300, 291, 458, 2140, 7500, 281, 428, 5022,
  50632], "temperature": 0.0, "avg_logprob": -0.1503269752759612, "compression_ratio":
  1.760180995475113, "no_speech_prob": 0.0011456109350547194}, {"id": 683, "seek":
  455240, "start": 4558.879999999999, "end": 4565.36, "text": " how they''re using
  the product what are the pain points you know how to how does it feel to get started",
  "tokens": [50688, 577, 436, 434, 1228, 264, 1674, 437, 366, 264, 1822, 2793, 291,
  458, 577, 281, 577, 775, 309, 841, 281, 483, 1409, 51012], "temperature": 0.0, "avg_logprob":
  -0.1503269752759612, "compression_ratio": 1.760180995475113, "no_speech_prob": 0.0011456109350547194},
  {"id": 684, "seek": 455240, "start": 4565.92, "end": 4573.679999999999, "text":
  " are able to progress so that''s that''s really also motivating and and honestly
  I think that some", "tokens": [51040, 366, 1075, 281, 4205, 370, 300, 311, 300,
  311, 534, 611, 41066, 293, 293, 6095, 286, 519, 300, 512, 51428], "temperature":
  0.0, "avg_logprob": -0.1503269752759612, "compression_ratio": 1.760180995475113,
  "no_speech_prob": 0.0011456109350547194}, {"id": 685, "seek": 455240, "start": 4573.679999999999,
  "end": 4581.839999999999, "text": " of the work that we''ve done using some of these
  smaller transformer models has been has an impact", "tokens": [51428, 295, 264,
  589, 300, 321, 600, 1096, 1228, 512, 295, 613, 4356, 31782, 5245, 575, 668, 575,
  364, 2712, 51836], "temperature": 0.0, "avg_logprob": -0.1503269752759612, "compression_ratio":
  1.760180995475113, "no_speech_prob": 0.0011456109350547194}, {"id": 686, "seek":
  458184, "start": 4581.84, "end": 4587.360000000001, "text": " on the industry like
  I got contacted by a person here on Twitter the other day said that you know I",
  "tokens": [50364, 322, 264, 3518, 411, 286, 658, 21546, 538, 257, 954, 510, 322,
  5794, 264, 661, 786, 848, 300, 291, 458, 286, 50640], "temperature": 0.0, "avg_logprob":
  -0.15301656174933773, "compression_ratio": 1.71875, "no_speech_prob": 0.0018938354915007949},
  {"id": 687, "seek": 458184, "start": 4587.360000000001, "end": 4595.04, "text":
  " saw your tweet about these smaller language models like not the birth base that
  people usually", "tokens": [50640, 1866, 428, 15258, 466, 613, 4356, 2856, 5245,
  411, 406, 264, 3965, 3096, 300, 561, 2673, 51024], "temperature": 0.0, "avg_logprob":
  -0.15301656174933773, "compression_ratio": 1.71875, "no_speech_prob": 0.0018938354915007949},
  {"id": 688, "seek": 458184, "start": 4595.04, "end": 4602.88, "text": " turn okay
  but this mini LM model which is a distilled 22 million parameters that actually
  did", "tokens": [51024, 1261, 1392, 457, 341, 8382, 46529, 2316, 597, 307, 257,
  1483, 6261, 5853, 2459, 9834, 300, 767, 630, 51416], "temperature": 0.0, "avg_logprob":
  -0.15301656174933773, "compression_ratio": 1.71875, "no_speech_prob": 0.0018938354915007949},
  {"id": 689, "seek": 458184, "start": 4602.88, "end": 4608.400000000001, "text":
  " the demo that you can run in your browser and it said you know I saw your tweet
  and I went ahead", "tokens": [51416, 264, 10723, 300, 291, 393, 1190, 294, 428,
  11185, 293, 309, 848, 291, 458, 286, 1866, 428, 15258, 293, 286, 1437, 2286, 51692],
  "temperature": 0.0, "avg_logprob": -0.15301656174933773, "compression_ratio": 1.71875,
  "no_speech_prob": 0.0018938354915007949}, {"id": 690, "seek": 460840, "start": 4608.719999999999,
  "end": 4616.5599999999995, "text": " and tried it for my domain which was classification
  of hate speech and then he like did a blog post", "tokens": [50380, 293, 3031, 309,
  337, 452, 9274, 597, 390, 21538, 295, 4700, 6218, 293, 550, 415, 411, 630, 257,
  6968, 2183, 50772], "temperature": 0.0, "avg_logprob": -0.13487017154693604, "compression_ratio":
  1.7312775330396475, "no_speech_prob": 0.003136327490210533}, {"id": 691, "seek":
  460840, "start": 4616.5599999999995, "end": 4621.2, "text": " on it and he mentioned
  me and I think that was really like interesting for me to see that you know", "tokens":
  [50772, 322, 309, 293, 415, 2835, 385, 293, 286, 519, 300, 390, 534, 411, 1880,
  337, 385, 281, 536, 300, 291, 458, 51004], "temperature": 0.0, "avg_logprob": -0.13487017154693604,
  "compression_ratio": 1.7312775330396475, "no_speech_prob": 0.003136327490210533},
  {"id": 692, "seek": 460840, "start": 4621.759999999999, "end": 4627.44, "text":
  " that I could share something that some people could actually make use of even
  if it was outside of", "tokens": [51032, 300, 286, 727, 2073, 746, 300, 512, 561,
  727, 767, 652, 764, 295, 754, 498, 309, 390, 2380, 295, 51316], "temperature": 0.0,
  "avg_logprob": -0.13487017154693604, "compression_ratio": 1.7312775330396475, "no_speech_prob":
  0.003136327490210533}, {"id": 693, "seek": 460840, "start": 4627.44, "end": 4633.36,
  "text": " search show and I learned a lot from especially around the relevance is
  slack space that we are", "tokens": [51316, 3164, 855, 293, 286, 3264, 257, 688,
  490, 2318, 926, 264, 32684, 307, 29767, 1901, 300, 321, 366, 51612], "temperature":
  0.0, "avg_logprob": -0.13487017154693604, "compression_ratio": 1.7312775330396475,
  "no_speech_prob": 0.003136327490210533}, {"id": 694, "seek": 463336, "start": 4633.36,
  "end": 4640.08, "text": " both in the open social connections slack space so a lot
  of discussion there rector search and we", "tokens": [50364, 1293, 294, 264, 1269,
  2093, 9271, 29767, 1901, 370, 257, 688, 295, 5017, 456, 319, 1672, 3164, 293, 321,
  50700], "temperature": 0.0, "avg_logprob": -0.2521303962258732, "compression_ratio":
  1.6756756756756757, "no_speech_prob": 0.0008492626948282123}, {"id": 695, "seek":
  463336, "start": 4640.08, "end": 4646.32, "text": " are you know sharing some blog
  posts and then I ask Greg from Pinecoin a tough question maybe you", "tokens": [50700,
  366, 291, 458, 5414, 512, 6968, 12300, 293, 550, 286, 1029, 11490, 490, 33531, 8562,
  257, 4930, 1168, 1310, 291, 51012], "temperature": 0.0, "avg_logprob": -0.2521303962258732,
  "compression_ratio": 1.6756756756756757, "no_speech_prob": 0.0008492626948282123},
  {"id": 696, "seek": 463336, "start": 4646.32, "end": 4652.08, "text": " know and
  so I really love being there and discussing and I learn a lot from from other people
  like", "tokens": [51012, 458, 293, 370, 286, 534, 959, 885, 456, 293, 10850, 293,
  286, 1466, 257, 688, 490, 490, 661, 561, 411, 51300], "temperature": 0.0, "avg_logprob":
  -0.2521303962258732, "compression_ratio": 1.6756756756756757, "no_speech_prob":
  0.0008492626948282123}, {"id": 697, "seek": 463336, "start": 4652.08, "end": 4657.599999999999,
  "text": " just devins from elastic search and so and I''m from you and especially
  around", "tokens": [51300, 445, 1905, 1292, 490, 17115, 3164, 293, 370, 293, 286,
  478, 490, 291, 293, 2318, 926, 51576], "temperature": 0.0, "avg_logprob": -0.2521303962258732,
  "compression_ratio": 1.6756756756756757, "no_speech_prob": 0.0008492626948282123},
  {"id": 698, "seek": 465760, "start": 4657.92, "end": 4665.280000000001, "text":
  " Berlin best search last year you did the AMA on the vector search and for me like
  one of the key", "tokens": [50380, 13848, 1151, 3164, 1036, 1064, 291, 630, 264,
  6475, 32, 322, 264, 8062, 3164, 293, 337, 385, 411, 472, 295, 264, 2141, 50748],
  "temperature": 0.0, "avg_logprob": -0.16211449846308282, "compression_ratio": 1.7123893805309736,
  "no_speech_prob": 0.01185557059943676}, {"id": 699, "seek": 465760, "start": 4665.280000000001,
  "end": 4672.08, "text": " moments was that Max Irvin your co-host of that he said
  you know what if the user types of phrase", "tokens": [50748, 6065, 390, 300, 7402,
  9151, 4796, 428, 598, 12, 6037, 295, 300, 415, 848, 291, 458, 437, 498, 264, 4195,
  3467, 295, 9535, 51088], "temperature": 0.0, "avg_logprob": -0.16211449846308282,
  "compression_ratio": 1.7123893805309736, "no_speech_prob": 0.01185557059943676},
  {"id": 700, "seek": 465760, "start": 4672.08, "end": 4679.200000000001, "text":
  " query you know actually quote marks I want to search for this exact phrase you
  know don''t show me", "tokens": [51088, 14581, 291, 458, 767, 6513, 10640, 286,
  528, 281, 3164, 337, 341, 1900, 9535, 291, 458, 500, 380, 855, 385, 51444], "temperature":
  0.0, "avg_logprob": -0.16211449846308282, "compression_ratio": 1.7123893805309736,
  "no_speech_prob": 0.01185557059943676}, {"id": 701, "seek": 465760, "start": 4679.200000000001,
  "end": 4684.240000000001, "text": " anything else give me that phrase you know and
  that''s something that is really hard to do with", "tokens": [51444, 1340, 1646,
  976, 385, 300, 9535, 291, 458, 293, 300, 311, 746, 300, 307, 534, 1152, 281, 360,
  365, 51696], "temperature": 0.0, "avg_logprob": -0.16211449846308282, "compression_ratio":
  1.7123893805309736, "no_speech_prob": 0.01185557059943676}, {"id": 702, "seek":
  468424, "start": 4684.24, "end": 4689.92, "text": " vector search alone right because
  you basically map it into this vector space and we do the", "tokens": [50364, 8062,
  3164, 3312, 558, 570, 291, 1936, 4471, 309, 666, 341, 8062, 1901, 293, 321, 360,
  264, 50648], "temperature": 0.0, "avg_logprob": -0.13975758388124662, "compression_ratio":
  1.6977777777777778, "no_speech_prob": 0.0005393280880525708}, {"id": 703, "seek":
  468424, "start": 4689.92, "end": 4695.44, "text": " similarities and that was a
  key takeaway from me and that was a really eye-opener for me you know", "tokens":
  [50648, 24197, 293, 300, 390, 257, 2141, 30681, 490, 385, 293, 300, 390, 257, 534,
  3313, 12, 404, 7971, 337, 385, 291, 458, 50924], "temperature": 0.0, "avg_logprob":
  -0.13975758388124662, "compression_ratio": 1.6977777777777778, "no_speech_prob":
  0.0005393280880525708}, {"id": 704, "seek": 468424, "start": 4695.44, "end": 4702.0,
  "text": " you need to be building out better examples of how actually to combine
  sparse and then single so", "tokens": [50924, 291, 643, 281, 312, 2390, 484, 1101,
  5110, 295, 577, 767, 281, 10432, 637, 11668, 293, 550, 2167, 370, 51252], "temperature":
  0.0, "avg_logprob": -0.13975758388124662, "compression_ratio": 1.6977777777777778,
  "no_speech_prob": 0.0005393280880525708}, {"id": 705, "seek": 468424, "start": 4702.0,
  "end": 4711.28, "text": " yeah this is amazing and what I enjoyed what you said
  is that you keep your practitioner hat on", "tokens": [51252, 1338, 341, 307, 2243,
  293, 437, 286, 4626, 437, 291, 848, 307, 300, 291, 1066, 428, 32125, 2385, 322,
  51716], "temperature": 0.0, "avg_logprob": -0.13975758388124662, "compression_ratio":
  1.6977777777777778, "no_speech_prob": 0.0005393280880525708}, {"id": 706, "seek":
  471128, "start": 4711.28, "end": 4718.639999999999, "text": " so you don''t just
  buy in easily into these new models or you don''t stay on the field of okay I''m",
  "tokens": [50364, 370, 291, 500, 380, 445, 2256, 294, 3612, 666, 613, 777, 5245,
  420, 291, 500, 380, 1754, 322, 264, 2519, 295, 1392, 286, 478, 50732], "temperature":
  0.0, "avg_logprob": -0.07790875434875488, "compression_ratio": 1.7117903930131004,
  "no_speech_prob": 0.0022152839228510857}, {"id": 707, "seek": 471128, "start": 4718.639999999999,
  "end": 4724.8, "text": " only an engineer I don''t even know what machine learning
  is because I think the profession is", "tokens": [50732, 787, 364, 11403, 286, 500,
  380, 754, 458, 437, 3479, 2539, 307, 570, 286, 519, 264, 7032, 307, 51040], "temperature":
  0.0, "avg_logprob": -0.07790875434875488, "compression_ratio": 1.7117903930131004,
  "no_speech_prob": 0.0022152839228510857}, {"id": 708, "seek": 471128, "start": 4724.8,
  "end": 4731.36, "text": " slowly changing and it''s like a blend of skills where
  today you need to succeed as a search engineer", "tokens": [51040, 5692, 4473, 293,
  309, 311, 411, 257, 10628, 295, 3942, 689, 965, 291, 643, 281, 7754, 382, 257, 3164,
  11403, 51368], "temperature": 0.0, "avg_logprob": -0.07790875434875488, "compression_ratio":
  1.7117903930131004, "no_speech_prob": 0.0022152839228510857}, {"id": 709, "seek":
  471128, "start": 4731.36, "end": 4739.36, "text": " and maybe it shouldn''t be called
  the search engineer anymore like I think it needs some new term but", "tokens":
  [51368, 293, 1310, 309, 4659, 380, 312, 1219, 264, 3164, 11403, 3602, 411, 286,
  519, 309, 2203, 512, 777, 1433, 457, 51768], "temperature": 0.0, "avg_logprob":
  -0.07790875434875488, "compression_ratio": 1.7117903930131004, "no_speech_prob":
  0.0022152839228510857}, {"id": 710, "seek": 473936, "start": 4739.36, "end": 4745.679999999999,
  "text": " we will probably be stuck with it for the lack of a better term but eventually
  you will need more", "tokens": [50364, 321, 486, 1391, 312, 5541, 365, 309, 337,
  264, 5011, 295, 257, 1101, 1433, 457, 4728, 291, 486, 643, 544, 50680], "temperature":
  0.0, "avg_logprob": -0.07570054314353249, "compression_ratio": 1.6195652173913044,
  "no_speech_prob": 0.0026735481806099415}, {"id": 711, "seek": 473936, "start": 4745.679999999999,
  "end": 4753.36, "text": " skills under your belt and I think of the work that you
  are doing is amazing in sharing this knowledge", "tokens": [50680, 3942, 833, 428,
  10750, 293, 286, 519, 295, 264, 589, 300, 291, 366, 884, 307, 2243, 294, 5414, 341,
  3601, 51064], "temperature": 0.0, "avg_logprob": -0.07570054314353249, "compression_ratio":
  1.6195652173913044, "no_speech_prob": 0.0026735481806099415}, {"id": 712, "seek":
  473936, "start": 4753.36, "end": 4760.88, "text": " and that people can actually
  reproduce it and I think that''s super super crucial for the progress", "tokens":
  [51064, 293, 300, 561, 393, 767, 29501, 309, 293, 286, 519, 300, 311, 1687, 1687,
  11462, 337, 264, 4205, 51440], "temperature": 0.0, "avg_logprob": -0.07570054314353249,
  "compression_ratio": 1.6195652173913044, "no_speech_prob": 0.0026735481806099415},
  {"id": 713, "seek": 476088, "start": 4760.88, "end": 4768.0, "text": " yeah I mean
  thank you Dimitri that''s that''s really nice of you and you know that''s that''s",
  "tokens": [50364, 1338, 286, 914, 1309, 291, 20975, 270, 470, 300, 311, 300, 311,
  534, 1481, 295, 291, 293, 291, 458, 300, 311, 300, 311, 50720], "temperature": 0.0,
  "avg_logprob": -0.20147931235177177, "compression_ratio": 1.7735849056603774, "no_speech_prob":
  0.009716111235320568}, {"id": 714, "seek": 476088, "start": 4770.16, "end": 4778.24,
  "text": " I yeah I think it''s it''s it''s actually true you know to share and I
  think that what you said you", "tokens": [50828, 286, 1338, 286, 519, 309, 311,
  309, 311, 309, 311, 767, 2074, 291, 458, 281, 2073, 293, 286, 519, 300, 437, 291,
  848, 291, 51232], "temperature": 0.0, "avg_logprob": -0.20147931235177177, "compression_ratio":
  1.7735849056603774, "no_speech_prob": 0.009716111235320568}, {"id": 715, "seek":
  476088, "start": 4778.24, "end": 4787.76, "text": " know building a search team
  today is really hard because especially since deep learning entered", "tokens":
  [51232, 458, 2390, 257, 3164, 1469, 965, 307, 534, 1152, 570, 2318, 1670, 2452,
  2539, 9065, 51708], "temperature": 0.0, "avg_logprob": -0.20147931235177177, "compression_ratio":
  1.7735849056603774, "no_speech_prob": 0.009716111235320568}, {"id": 716, "seek":
  478776, "start": 4787.76, "end": 4794.24, "text": " the search field right so now
  you need to know how to configure and do matching and boosting", "tokens": [50364,
  264, 3164, 2519, 558, 370, 586, 291, 643, 281, 458, 577, 281, 22162, 293, 360, 14324,
  293, 43117, 50688], "temperature": 0.0, "avg_logprob": -0.11616359667831593, "compression_ratio":
  1.8883495145631068, "no_speech_prob": 0.005274524912238121}, {"id": 717, "seek":
  478776, "start": 4794.24, "end": 4800.24, "text": " an elastic search and now you
  also need you know how do I train the dense vector model and you know", "tokens":
  [50688, 364, 17115, 3164, 293, 586, 291, 611, 643, 291, 458, 577, 360, 286, 3847,
  264, 18011, 8062, 2316, 293, 291, 458, 50988], "temperature": 0.0, "avg_logprob":
  -0.11616359667831593, "compression_ratio": 1.8883495145631068, "no_speech_prob":
  0.005274524912238121}, {"id": 718, "seek": 478776, "start": 4800.24, "end": 4806.88,
  "text": " how should I you know should I use birch they use birch large you know
  does it handle multilingual", "tokens": [50988, 577, 820, 286, 291, 458, 820, 286,
  764, 1904, 339, 436, 764, 1904, 339, 2416, 291, 458, 775, 309, 4813, 2120, 38219,
  51320], "temperature": 0.0, "avg_logprob": -0.11616359667831593, "compression_ratio":
  1.8883495145631068, "no_speech_prob": 0.005274524912238121}, {"id": 719, "seek":
  478776, "start": 4806.88, "end": 4812.88, "text": " text does it handle spell correction
  you know they''re always kind of different things you know so", "tokens": [51320,
  2487, 775, 309, 4813, 9827, 19984, 291, 458, 436, 434, 1009, 733, 295, 819, 721,
  291, 458, 370, 51620], "temperature": 0.0, "avg_logprob": -0.11616359667831593,
  "compression_ratio": 1.8883495145631068, "no_speech_prob": 0.005274524912238121},
  {"id": 720, "seek": 481288, "start": 4812.88, "end": 4821.4400000000005, "text":
  " building a search team in 2022 it''s not easy because you need the kind of a mixed
  NLP search you", "tokens": [50364, 2390, 257, 3164, 1469, 294, 20229, 309, 311,
  406, 1858, 570, 291, 643, 264, 733, 295, 257, 7467, 426, 45196, 3164, 291, 50792],
  "temperature": 0.0, "avg_logprob": -0.12078923238834864, "compression_ratio": 1.529100529100529,
  "no_speech_prob": 0.0005237549194134772}, {"id": 721, "seek": 481288, "start": 4821.4400000000005,
  "end": 4825.92, "text": " know there are a lot of different things and that''s what
  I love about it you know and I talked about", "tokens": [50792, 458, 456, 366, 257,
  688, 295, 819, 721, 293, 300, 311, 437, 286, 959, 466, 309, 291, 458, 293, 286,
  2825, 466, 51016], "temperature": 0.0, "avg_logprob": -0.12078923238834864, "compression_ratio":
  1.529100529100529, "no_speech_prob": 0.0005237549194134772}, {"id": 722, "seek":
  481288, "start": 4825.92, "end": 4834.56, "text": " on Twitter and you know in a
  talk I did earlier as well that this neural paradigm shift has", "tokens": [51016,
  322, 5794, 293, 291, 458, 294, 257, 751, 286, 630, 3071, 382, 731, 300, 341, 18161,
  24709, 5513, 575, 51448], "temperature": 0.0, "avg_logprob": -0.12078923238834864,
  "compression_ratio": 1.529100529100529, "no_speech_prob": 0.0005237549194134772},
  {"id": 723, "seek": 483456, "start": 4834.56, "end": 4840.320000000001, "text":
  " opened this kind of knowledge gap you know how to actually successfully apply
  these methods", "tokens": [50364, 5625, 341, 733, 295, 3601, 7417, 291, 458, 577,
  281, 767, 10727, 3079, 613, 7150, 50652], "temperature": 0.0, "avg_logprob": -0.12762591482579022,
  "compression_ratio": 1.6304347826086956, "no_speech_prob": 0.0012347548035904765},
  {"id": 724, "seek": 483456, "start": 4841.280000000001, "end": 4848.56, "text":
  " and also on the technology side that we try to bring you know with VESPA that
  you can kind of", "tokens": [50700, 293, 611, 322, 264, 2899, 1252, 300, 321, 853,
  281, 1565, 291, 458, 365, 691, 2358, 10297, 300, 291, 393, 733, 295, 51064], "temperature":
  0.0, "avg_logprob": -0.12762591482579022, "compression_ratio": 1.6304347826086956,
  "no_speech_prob": 0.0012347548035904765}, {"id": 725, "seek": 483456, "start": 4848.56,
  "end": 4855.92, "text": " combine different techniques we don''t have to throw away
  50 or 300 years of the inverted index", "tokens": [51064, 10432, 819, 7512, 321,
  500, 380, 362, 281, 3507, 1314, 2625, 420, 6641, 924, 295, 264, 38969, 8186, 51432],
  "temperature": 0.0, "avg_logprob": -0.12762591482579022, "compression_ratio": 1.6304347826086956,
  "no_speech_prob": 0.0012347548035904765}, {"id": 726, "seek": 483456, "start": 4855.92,
  "end": 4861.84, "text": " you know we don''t need to throw that away you know it
  still has value it''s going to have value", "tokens": [51432, 291, 458, 321, 500,
  380, 643, 281, 3507, 300, 1314, 291, 458, 309, 920, 575, 2158, 309, 311, 516, 281,
  362, 2158, 51728], "temperature": 0.0, "avg_logprob": -0.12762591482579022, "compression_ratio":
  1.6304347826086956, "no_speech_prob": 0.0012347548035904765}, {"id": 727, "seek":
  486184, "start": 4861.84, "end": 4867.84, "text": " probably forever you know so
  so we don''t have to throw away so that''s interesting but that''s also", "tokens":
  [50364, 1391, 5680, 291, 458, 370, 370, 321, 500, 380, 362, 281, 3507, 1314, 370,
  300, 311, 1880, 457, 300, 311, 611, 50664], "temperature": 0.0, "avg_logprob": -0.1293924635490485,
  "compression_ratio": 1.7706766917293233, "no_speech_prob": 0.000996629474684596},
  {"id": 728, "seek": 486184, "start": 4867.84, "end": 4873.6, "text": " what it''s
  been fascinating and I''ve said numerous times that I don''t think I''ve learned
  that much", "tokens": [50664, 437, 309, 311, 668, 10343, 293, 286, 600, 848, 12546,
  1413, 300, 286, 500, 380, 519, 286, 600, 3264, 300, 709, 50952], "temperature":
  0.0, "avg_logprob": -0.1293924635490485, "compression_ratio": 1.7706766917293233,
  "no_speech_prob": 0.000996629474684596}, {"id": 729, "seek": 486184, "start": 4873.6,
  "end": 4879.360000000001, "text": " in my career that I''ve actually over the last
  three years because reading papers it''s not being", "tokens": [50952, 294, 452,
  3988, 300, 286, 600, 767, 670, 264, 1036, 1045, 924, 570, 3760, 10577, 309, 311,
  406, 885, 51240], "temperature": 0.0, "avg_logprob": -0.1293924635490485, "compression_ratio":
  1.7706766917293233, "no_speech_prob": 0.000996629474684596}, {"id": 730, "seek":
  486184, "start": 4879.360000000001, "end": 4884.4800000000005, "text": " a big kind
  of interest of mine earlier it''s been one of the system side engineering side",
  "tokens": [51240, 257, 955, 733, 295, 1179, 295, 3892, 3071, 309, 311, 668, 472,
  295, 264, 1185, 1252, 7043, 1252, 51496], "temperature": 0.0, "avg_logprob": -0.1293924635490485,
  "compression_ratio": 1.7706766917293233, "no_speech_prob": 0.000996629474684596},
  {"id": 731, "seek": 486184, "start": 4885.52, "end": 4890.400000000001, "text":
  " but that''s been a high-opener for me you know to kind of how to apply these techniques
  and", "tokens": [51548, 457, 300, 311, 668, 257, 1090, 12, 404, 7971, 337, 385,
  291, 458, 281, 733, 295, 577, 281, 3079, 613, 7512, 293, 51792], "temperature":
  0.0, "avg_logprob": -0.1293924635490485, "compression_ratio": 1.7706766917293233,
  "no_speech_prob": 0.000996629474684596}, {"id": 732, "seek": 489040, "start": 4890.96,
  "end": 4897.599999999999, "text": " yeah so and to learn you know and that''s the
  great thing about open source is that you know we can", "tokens": [50392, 1338,
  370, 293, 281, 1466, 291, 458, 293, 300, 311, 264, 869, 551, 466, 1269, 4009, 307,
  300, 291, 458, 321, 393, 50724], "temperature": 0.0, "avg_logprob": -0.0845474296145969,
  "compression_ratio": 1.813397129186603, "no_speech_prob": 0.0017564388690516353},
  {"id": 733, "seek": 489040, "start": 4897.599999999999, "end": 4908.32, "text":
  " share ways of doing things yeah yeah absolutely sharing is caring and so much
  comes back to you", "tokens": [50724, 2073, 2098, 295, 884, 721, 1338, 1338, 3122,
  5414, 307, 15365, 293, 370, 709, 1487, 646, 281, 291, 51260], "temperature": 0.0,
  "avg_logprob": -0.0845474296145969, "compression_ratio": 1.813397129186603, "no_speech_prob":
  0.0017564388690516353}, {"id": 734, "seek": 489040, "start": 4908.32, "end": 4913.5199999999995,
  "text": " as you said you know you get mentioned somewhere and you feel like you
  didn''t do it in vain", "tokens": [51260, 382, 291, 848, 291, 458, 291, 483, 2835,
  4079, 293, 291, 841, 411, 291, 994, 380, 360, 309, 294, 22240, 51520], "temperature":
  0.0, "avg_logprob": -0.0845474296145969, "compression_ratio": 1.813397129186603,
  "no_speech_prob": 0.0017564388690516353}, {"id": 735, "seek": 489040, "start": 4913.5199999999995,
  "end": 4919.36, "text": " but also you might learn something new like a new use
  case and I feel the same you know when", "tokens": [51520, 457, 611, 291, 1062,
  1466, 746, 777, 411, 257, 777, 764, 1389, 293, 286, 841, 264, 912, 291, 458, 562,
  51812], "temperature": 0.0, "avg_logprob": -0.0845474296145969, "compression_ratio":
  1.813397129186603, "no_speech_prob": 0.0017564388690516353}, {"id": 736, "seek":
  491936, "start": 4919.36, "end": 4926.639999999999, "text": " when I blog or when
  some video is viewed by somebody and then somebody says thank you even just", "tokens":
  [50364, 562, 286, 6968, 420, 562, 512, 960, 307, 19174, 538, 2618, 293, 550, 2618,
  1619, 1309, 291, 754, 445, 50728], "temperature": 0.0, "avg_logprob": -0.06558184788144868,
  "compression_ratio": 1.6869565217391305, "no_speech_prob": 0.0007935056346468627},
  {"id": 737, "seek": 491936, "start": 4926.639999999999, "end": 4932.719999999999,
  "text": " multiple months after I did it and you know it''s just an amazing feeling
  it''s like a sense of", "tokens": [50728, 3866, 2493, 934, 286, 630, 309, 293, 291,
  458, 309, 311, 445, 364, 2243, 2633, 309, 311, 411, 257, 2020, 295, 51032], "temperature":
  0.0, "avg_logprob": -0.06558184788144868, "compression_ratio": 1.6869565217391305,
  "no_speech_prob": 0.0007935056346468627}, {"id": 738, "seek": 491936, "start": 4932.719999999999,
  "end": 4941.12, "text": " connection as well especially in these days when we don''t
  maybe meet socially as we used to but", "tokens": [51032, 4984, 382, 731, 2318,
  294, 613, 1708, 562, 321, 500, 380, 1310, 1677, 21397, 382, 321, 1143, 281, 457,
  51452], "temperature": 0.0, "avg_logprob": -0.06558184788144868, "compression_ratio":
  1.6869565217391305, "no_speech_prob": 0.0007935056346468627}, {"id": 739, "seek":
  491936, "start": 4941.679999999999, "end": 4948.5599999999995, "text": " that''s
  a new actually evolutionary new way of connecting and I feel much more comfortable
  and enjoying", "tokens": [51480, 300, 311, 257, 777, 767, 27567, 777, 636, 295,
  11015, 293, 286, 841, 709, 544, 4619, 293, 9929, 51824], "temperature": 0.0, "avg_logprob":
  -0.06558184788144868, "compression_ratio": 1.6869565217391305, "no_speech_prob":
  0.0007935056346468627}, {"id": 740, "seek": 494856, "start": 4948.56, "end": 4957.04,
  "text": " this more detailed conversation so maybe these interactions on Twitter
  they they bring a lot more", "tokens": [50364, 341, 544, 9942, 3761, 370, 1310,
  613, 13280, 322, 5794, 436, 436, 1565, 257, 688, 544, 50788], "temperature": 0.0,
  "avg_logprob": -0.13781012258222025, "compression_ratio": 1.655367231638418, "no_speech_prob":
  0.0008748817490413785}, {"id": 741, "seek": 494856, "start": 4957.04, "end": 4963.92,
  "text": " value and I think this is super super great is there is something that
  you would like to share on", "tokens": [50788, 2158, 293, 286, 519, 341, 307, 1687,
  1687, 869, 307, 456, 307, 746, 300, 291, 576, 411, 281, 2073, 322, 51132], "temperature":
  0.0, "avg_logprob": -0.13781012258222025, "compression_ratio": 1.655367231638418,
  "no_speech_prob": 0.0008748817490413785}, {"id": 742, "seek": 494856, "start": 4963.92,
  "end": 4970.240000000001, "text": " Vespa development or maybe something that users
  might anticipate and maybe you want to point them", "tokens": [51132, 691, 279,
  4306, 3250, 420, 1310, 746, 300, 5022, 1062, 21685, 293, 1310, 291, 528, 281, 935,
  552, 51448], "temperature": 0.0, "avg_logprob": -0.13781012258222025, "compression_ratio":
  1.655367231638418, "no_speech_prob": 0.0008748817490413785}, {"id": 743, "seek":
  497024, "start": 4971.04, "end": 4974.32, "text": " to some tutorial that they might
  you know take a look at", "tokens": [50404, 281, 512, 7073, 300, 436, 1062, 291,
  458, 747, 257, 574, 412, 50568], "temperature": 0.0, "avg_logprob": -0.14266654423304967,
  "compression_ratio": 1.6386138613861385, "no_speech_prob": 0.00326779717579484},
  {"id": 744, "seek": 497024, "start": 4977.84, "end": 4982.5599999999995, "text":
  " yeah so I can give a few product updates of what''s coming from Vespa we are coming",
  "tokens": [50744, 1338, 370, 286, 393, 976, 257, 1326, 1674, 9205, 295, 437, 311,
  1348, 490, 691, 279, 4306, 321, 366, 1348, 50980], "temperature": 0.0, "avg_logprob":
  -0.14266654423304967, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.00326779717579484}, {"id": 745, "seek": 497024, "start": 4983.76, "end": 4990.32,
  "text": " gonna release some integrated dense models for Vespa so though you don''t
  have to export so you", "tokens": [51040, 799, 4374, 512, 10919, 18011, 5245, 337,
  691, 279, 4306, 370, 1673, 291, 500, 380, 362, 281, 10725, 370, 291, 51368], "temperature":
  0.0, "avg_logprob": -0.14266654423304967, "compression_ratio": 1.6386138613861385,
  "no_speech_prob": 0.00326779717579484}, {"id": 746, "seek": 497024, "start": 4990.32,
  "end": 4997.28, "text": " can you can use these models off the shelf and then we
  allow you to tune the Korean coder so you", "tokens": [51368, 393, 291, 393, 764,
  613, 5245, 766, 264, 15222, 293, 550, 321, 2089, 291, 281, 10864, 264, 6933, 17656,
  260, 370, 291, 51716], "temperature": 0.0, "avg_logprob": -0.14266654423304967,
  "compression_ratio": 1.6386138613861385, "no_speech_prob": 0.00326779717579484},
  {"id": 747, "seek": 499728, "start": 4997.28, "end": 5004.08, "text": " have the
  document code is frozen but then you can tune the Korean coder and then show you
  how to", "tokens": [50364, 362, 264, 4166, 3089, 307, 12496, 457, 550, 291, 393,
  10864, 264, 6933, 17656, 260, 293, 550, 855, 291, 577, 281, 50704], "temperature":
  0.0, "avg_logprob": -0.1601293756720725, "compression_ratio": 1.683982683982684,
  "no_speech_prob": 0.0006800630362704396}, {"id": 748, "seek": 499728, "start": 5004.08,
  "end": 5009.36, "text": " combine these combining both dense as far so that''s one
  thing that is coming out other thing is", "tokens": [50704, 10432, 613, 21928, 1293,
  18011, 382, 1400, 370, 300, 311, 472, 551, 300, 307, 1348, 484, 661, 551, 307, 50968],
  "temperature": 0.0, "avg_logprob": -0.1601293756720725, "compression_ratio": 1.683982683982684,
  "no_speech_prob": 0.0006800630362704396}, {"id": 749, "seek": 499728, "start": 5009.36,
  "end": 5017.12, "text": " that we''re taking some steps regarding for love QPS use
  cases because we designed Vespa you know", "tokens": [50968, 300, 321, 434, 1940,
  512, 4439, 8595, 337, 959, 1249, 6273, 764, 3331, 570, 321, 4761, 691, 279, 4306,
  291, 458, 51356], "temperature": 0.0, "avg_logprob": -0.1601293756720725, "compression_ratio":
  1.683982683982684, "no_speech_prob": 0.0006800630362704396}, {"id": 750, "seek":
  499728, "start": 5017.12, "end": 5024.32, "text": " to be kind of low single digit
  male seconds on multiple different use cases but not everybody needs", "tokens":
  [51356, 281, 312, 733, 295, 2295, 2167, 14293, 7133, 3949, 322, 3866, 819, 764,
  3331, 457, 406, 2201, 2203, 51716], "temperature": 0.0, "avg_logprob": -0.1601293756720725,
  "compression_ratio": 1.683982683982684, "no_speech_prob": 0.0006800630362704396},
  {"id": 751, "seek": 502432, "start": 5024.32, "end": 5032.08, "text": " that so
  we''re introducing some new options for memory management so that we can actually
  run", "tokens": [50364, 300, 370, 321, 434, 15424, 512, 777, 3956, 337, 4675, 4592,
  370, 300, 321, 393, 767, 1190, 50752], "temperature": 0.0, "avg_logprob": -0.11968808540931115,
  "compression_ratio": 1.6470588235294117, "no_speech_prob": 0.0025737411342561245},
  {"id": 752, "seek": 502432, "start": 5033.5199999999995, "end": 5039.44, "text":
  " on service with less memory so that''s I think that''s gonna be a game changer
  for certain", "tokens": [50824, 322, 2643, 365, 1570, 4675, 370, 300, 311, 286,
  519, 300, 311, 799, 312, 257, 1216, 22822, 337, 1629, 51120], "temperature": 0.0,
  "avg_logprob": -0.11968808540931115, "compression_ratio": 1.6470588235294117, "no_speech_prob":
  0.0025737411342561245}, {"id": 753, "seek": 502432, "start": 5039.44, "end": 5050.88,
  "text": " use cases that don''t need high throughput low latency so that''s two
  things and yeah that''s I think", "tokens": [51120, 764, 3331, 300, 500, 380, 643,
  1090, 44629, 2295, 27043, 370, 300, 311, 732, 721, 293, 1338, 300, 311, 286, 519,
  51692], "temperature": 0.0, "avg_logprob": -0.11968808540931115, "compression_ratio":
  1.6470588235294117, "no_speech_prob": 0.0025737411342561245}, {"id": 754, "seek":
  505088, "start": 5050.88, "end": 5056.8, "text": " that''s more than enough you
  know and there will there will be some some blogs I think about our", "tokens":
  [50364, 300, 311, 544, 813, 1547, 291, 458, 293, 456, 486, 456, 486, 312, 512, 512,
  31038, 286, 519, 466, 527, 50660], "temperature": 0.0, "avg_logprob": -0.19128237599911896,
  "compression_ratio": 1.6355932203389831, "no_speech_prob": 0.005922040902078152},
  {"id": 755, "seek": 505088, "start": 5056.8, "end": 5065.2, "text": " results on
  the beer beer benchmark yeah yeah that''s and I''m gonna come out also with a blog
  post on", "tokens": [50660, 3542, 322, 264, 8795, 8795, 18927, 1338, 1338, 300,
  311, 293, 286, 478, 799, 808, 484, 611, 365, 257, 6968, 2183, 322, 51080], "temperature":
  0.0, "avg_logprob": -0.19128237599911896, "compression_ratio": 1.6355932203389831,
  "no_speech_prob": 0.005922040902078152}, {"id": 756, "seek": 505088, "start": 5065.2,
  "end": 5071.84, "text": " a technique called span which is a paper for Microsoft
  so m2n represented that on Vespa so it''s", "tokens": [51080, 257, 6532, 1219, 16174,
  597, 307, 257, 3035, 337, 8116, 370, 275, 17, 77, 10379, 300, 322, 691, 279, 4306,
  370, 309, 311, 51412], "temperature": 0.0, "avg_logprob": -0.19128237599911896,
  "compression_ratio": 1.6355932203389831, "no_speech_prob": 0.005922040902078152},
  {"id": 757, "seek": 505088, "start": 5071.84, "end": 5078.56, "text": " really interesting
  technique with the hybrid combination of HMSW and inverted file and you can", "tokens":
  [51412, 534, 1880, 6532, 365, 264, 13051, 6562, 295, 389, 10288, 54, 293, 38969,
  3991, 293, 291, 393, 51748], "temperature": 0.0, "avg_logprob": -0.19128237599911896,
  "compression_ratio": 1.6355932203389831, "no_speech_prob": 0.005922040902078152},
  {"id": 758, "seek": 507856, "start": 5078.56, "end": 5085.04, "text": " represent
  this m2n in Vespa so I''m gonna do a part three of my blog post serial billion scale",
  "tokens": [50364, 2906, 341, 275, 17, 77, 294, 691, 279, 4306, 370, 286, 478, 799,
  360, 257, 644, 1045, 295, 452, 6968, 2183, 17436, 5218, 4373, 50688], "temperature":
  0.0, "avg_logprob": -0.1659896501930811, "compression_ratio": 1.6566523605150214,
  "no_speech_prob": 0.0017443925607949495}, {"id": 759, "seek": 507856, "start": 5085.04,
  "end": 5089.6, "text": " so that''s something I''m looking forward to but right
  now I''m that kind of refracting a lot of", "tokens": [50688, 370, 300, 311, 746,
  286, 478, 1237, 2128, 281, 457, 558, 586, 286, 478, 300, 733, 295, 1895, 1897, 278,
  257, 688, 295, 50916], "temperature": 0.0, "avg_logprob": -0.1659896501930811, "compression_ratio":
  1.6566523605150214, "no_speech_prob": 0.0017443925607949495}, {"id": 760, "seek":
  507856, "start": 5089.6, "end": 5097.04, "text": " the sample applications and so
  on to to get the experience more smoothly yeah yeah sounds fantastic", "tokens":
  [50916, 264, 6889, 5821, 293, 370, 322, 281, 281, 483, 264, 1752, 544, 19565, 1338,
  1338, 3263, 5456, 51288], "temperature": 0.0, "avg_logprob": -0.1659896501930811,
  "compression_ratio": 1.6566523605150214, "no_speech_prob": 0.0017443925607949495},
  {"id": 761, "seek": 507856, "start": 5097.04, "end": 5102.400000000001, "text":
  " looking forward to it and we''ll make sure to link all the blog posts that you
  mentioned especially", "tokens": [51288, 1237, 2128, 281, 309, 293, 321, 603, 652,
  988, 281, 2113, 439, 264, 6968, 12300, 300, 291, 2835, 2318, 51556], "temperature":
  0.0, "avg_logprob": -0.1659896501930811, "compression_ratio": 1.6566523605150214,
  "no_speech_prob": 0.0017443925607949495}, {"id": 762, "seek": 510240, "start": 5102.719999999999,
  "end": 5108.48, "text": " on billion scale vector search and other tutorials that
  you mentioned and this is fantastic thank", "tokens": [50380, 322, 5218, 4373, 8062,
  3164, 293, 661, 17616, 300, 291, 2835, 293, 341, 307, 5456, 1309, 50668], "temperature":
  0.0, "avg_logprob": -0.0654059490525579, "compression_ratio": 1.7345132743362832,
  "no_speech_prob": 0.0033172317780554295}, {"id": 763, "seek": 510240, "start": 5108.48,
  "end": 5115.04, "text": " you for doing this and keep doing this keep finding the
  energy I know it''s stuck sometimes but I", "tokens": [50668, 291, 337, 884, 341,
  293, 1066, 884, 341, 1066, 5006, 264, 2281, 286, 458, 309, 311, 5541, 2171, 457,
  286, 50996], "temperature": 0.0, "avg_logprob": -0.0654059490525579, "compression_ratio":
  1.7345132743362832, "no_speech_prob": 0.0033172317780554295}, {"id": 764, "seek":
  510240, "start": 5115.04, "end": 5121.5199999999995, "text": " think it keeps you
  also awake and sort of like pushing yourself forward and I think the best way to",
  "tokens": [50996, 519, 309, 5965, 291, 611, 15994, 293, 1333, 295, 411, 7380, 1803,
  2128, 293, 286, 519, 264, 1151, 636, 281, 51320], "temperature": 0.0, "avg_logprob":
  -0.0654059490525579, "compression_ratio": 1.7345132743362832, "no_speech_prob":
  0.0033172317780554295}, {"id": 765, "seek": 510240, "start": 5121.5199999999995,
  "end": 5128.4, "text": " use your brain is actually doing something that is useful
  be reading a paper or implementing code", "tokens": [51320, 764, 428, 3567, 307,
  767, 884, 746, 300, 307, 4420, 312, 3760, 257, 3035, 420, 18114, 3089, 51664], "temperature":
  0.0, "avg_logprob": -0.0654059490525579, "compression_ratio": 1.7345132743362832,
  "no_speech_prob": 0.0033172317780554295}, {"id": 766, "seek": 512840, "start": 5128.4,
  "end": 5135.2, "text": " or blogging about it so this is fantastic thanks so much
  for your active contribution", "tokens": [50364, 420, 6968, 3249, 466, 309, 370,
  341, 307, 5456, 3231, 370, 709, 337, 428, 4967, 13150, 50704], "temperature": 0.0,
  "avg_logprob": -0.09214245291317211, "compression_ratio": 1.7342995169082125, "no_speech_prob":
  0.010311142541468143}, {"id": 767, "seek": 512840, "start": 5135.839999999999, "end":
  5143.28, "text": " thank you thank you as well yeah um and I really enjoyed this
  conversation I really hope we can", "tokens": [50736, 1309, 291, 1309, 291, 382,
  731, 1338, 1105, 293, 286, 534, 4626, 341, 3761, 286, 534, 1454, 321, 393, 51108],
  "temperature": 0.0, "avg_logprob": -0.09214245291317211, "compression_ratio": 1.7342995169082125,
  "no_speech_prob": 0.010311142541468143}, {"id": 768, "seek": 512840, "start": 5143.28,
  "end": 5148.799999999999, "text": " record at some point down the road as well if
  you will be open to it and I think we can", "tokens": [51108, 2136, 412, 512, 935,
  760, 264, 3060, 382, 731, 498, 291, 486, 312, 1269, 281, 309, 293, 286, 519, 321,
  393, 51384], "temperature": 0.0, "avg_logprob": -0.09214245291317211, "compression_ratio":
  1.7342995169082125, "no_speech_prob": 0.010311142541468143}, {"id": 769, "seek":
  512840, "start": 5148.799999999999, "end": 5154.879999999999, "text": " cover a
  lot more topics as well but I wish you all the success in your endeavors and stay",
  "tokens": [51384, 2060, 257, 688, 544, 8378, 382, 731, 457, 286, 3172, 291, 439,
  264, 2245, 294, 428, 49608, 293, 1754, 51688], "temperature": 0.0, "avg_logprob":
  -0.09214245291317211, "compression_ratio": 1.7342995169082125, "no_speech_prob":
  0.010311142541468143}, {"id": 770, "seek": 515488, "start": 5154.88, "end": 5162.0,
  "text": " warm and excited about the field yeah I will I mean such an exciting field
  thank you very much", "tokens": [50364, 4561, 293, 2919, 466, 264, 2519, 1338, 286,
  486, 286, 914, 1270, 364, 4670, 2519, 1309, 291, 588, 709, 50720], "temperature":
  0.0, "avg_logprob": -0.1856441705123238, "compression_ratio": 1.1604938271604939,
  "no_speech_prob": 0.018528467044234276}, {"id": 771, "seek": 516200, "start": 5162.0,
  "end": 5172.96, "text": " Dimitri for hosting this and you know we''ll talk later
  on thank you thank you and see you around bye bye", "tokens": [50368, 20975, 270,
  470, 337, 16058, 341, 293, 291, 458, 321, 603, 751, 1780, 322, 1309, 291, 1309,
  291, 293, 536, 291, 926, 6543, 6543, 50912], "temperature": 0.0, "avg_logprob":
  -0.36714546768753614, "compression_ratio": 1.2380952380952381, "no_speech_prob":
  0.050745509564876556}, {"id": 772, "seek": 519200, "start": 5192.0, "end": 5194.8,
  "text": " you", "tokens": [50372, 291, 50504], "temperature": 1.0, "avg_logprob":
  -1.8751850128173828, "compression_ratio": 0.2727272727272727, "no_speech_prob":
  0.39786800742149353}]'
---

Everyone, Vector Podcast is here. I hope you have been waiting for another episode. And today I have a rock star with me. Joe Christian Bergum, a distinguished engineer with Yahoo. And he has been super vocal in the field of Vector Search.
And he has been also advocating for one of the famous Vector Search engines and actually like a platform. Shirley Jo can talk more about it called Vespa. Hey Joe, how are you doing? Hey Dimitri, I'm good, thanks. How are you? I'm great. Thank you very much for taking time to talk to me.
It's fantastic being here on your show. It's become so popular. Thank you for that introduction. I'm not sure if I'm a rock star. It's really interesting to be here. I really look forward for our conversation on Vector Search and maybe we'll touch on language models as well.
And they'll talk a little bit about Vespa and the technology in Vespa. I'm really excited. Yeah, I'm looking forward to that. And I mean, you are a rock star. I can hear you every way on Twitter and LinkedIn and blogging. And so what else? So this has been like this.
And I'm really glad to hear to talk to you here today. And so as a tradition, could you please introduce yourself however you want to know the detail you want and we'll take it from there? Yeah. Yeah, so my name is Joe Christian and I work for Yahoo. And I've been working for Yahoo's is 2007.
My current role in Yahoo is distinguished engineer and I work on the Vespa platform. And I've been working on Search and Recommendations since about 2001. When I joined a company here as an intern during my studies, a company called Fast Search and Transfer, an Norwegian company.
Back then they were doing web search with this web search engine called alldevab.com. So they started around 98 I think trying to compete with Google and so on. And then Yahoo came along and bought the web search division. The team here in Toronto. They also bought all the way star and so on.
So that was back in 2003. And in 2004, Vespa was born. So and I joined I actually worked in Fast in the enterprise search division for some time, three years. And then I joined Yahoo in 2007. And since then I'm been here working on search and Vespa in Yahoo. So that's my background.
I also hold a master degree in computer science from the Norwegian University here in Toronto. Oh yeah, that's great. Actually, by the way, I did visit Toronto Hame. Was it 2007 for an interview with one search company? Not fast. But yeah, it was a great, great visit. I mean, I love the city.
It's an amazing place. Yeah, it's an amazing place. And it's funny what you said about search and trial because it really has a special, maybe special even in Europe because we at one time we had both Google, Bing and Yahoo here in in in in trial line. So that was a fantastic time.
Google shut down their office here in trial line. And but now we have a Microsoft is here in in tronheim and also Yahoo as office here in in tronheim. So there's a lot of search technology competence here in tronheim.
This is amazing actually for for relatively small city, but I think Tronheim used to be a capital of Norway at some point in back in history. Yeah, in its on point, back way back in the Viking days. Exactly. So now all these Vikings are stopped going around with boats and harassing people.
Now we developed search technology now. Yeah, such a move. Wow. And I also understood that in tronheim, as you said, there is the university. Is it actually one of the talent supplies for this industry or engineering in general? Yeah, it is.
We have the largest technical university in Norway, C and in tronheim. So as an old kind of history and so it's definitely one of the reasons why the search companies evolved. And the fast search and transfer of the company was founded by people coming out of the university here.
So two point in the east week, very good swing and so these two reggae and they they came they actually started with FTP search bucket back in like the night the seven. So and that developed into this web search engine and then eventually this became a Westpaw in Yahoo. Oh yeah, yeah, sounds great.
So I can actually maybe touch on the backgrounds since I've mentioned now web search and you know how maybe not everybody has heard about Westpaw and so Westpaw actually we started developing Westpaw in 2004. So Yahoo said that you know we brought you into the company.
We want you to build a vertical search platform that we can use across our properties in Yahoo. So for example, Yahoo finance, Yahoo news, they need to have some kind of search engine.
So and they gave that task to ask you in trial and I'm so they started building Westpaw, the Westpaw platform using the routes and the technology from the web search and putting that into a package that the verticals could install and use.
And then over time this so basically starting with basic BM25 like search like keyword search and then gradually Westpaw added more features real time indexing, 10 source aggregations, grouping facets as well.
So it really developed over time and new requirements came in especially when we started Westpaw it was around search but in 2007, 2008 around that time Westpaw's also started to be used more of as a recommendation engine. So serving of recommendations. So when you go to finance, Yahoo.
com and there's a set of articles that are recommended to you the serving engine doing that is Westpaw. And then in 2017, Yahoo decided that we're going to open source Westpaw to the world.
So we open-sourced it using our Apache tool license and we still continue to actively, very actively develop on Westpaw and add new features and so on. So that's a kind of brief background. So Westpaw is not new.
It's really kind of it has in a very long history and I think that's also great thing and we can talk maybe a little bit about it because you know we need to develop software over time. There are a lot of changes you know in the infrastructure. There was no cloud, public cloud.
There were no Kubernetes and from 2004. I started in 2007, you know a high power content machine, content node machine would have maybe eight things of RAM. And it would have maybe maximum 1 gigabit per second network. And if we go fast forward, you know, and it will have spinning disks.
And now we have NVME SSD disks. We have nodes with four terabytes, potentially of memory, lots of CPU power. So there's like keeping up in improving the software and adopting it to the hardware and new hardware and so on. It's been really fun to watch.
I think we did a good job actually making Westpaw kind of modern from something that started in 2004. It turns like really an exciting journey and really like starting from when you would explain like you know small scale servers in the way all the way.
And the technology has changed so much right? The disks became faster I guess and you know the network has become faster.
And like I remember like in Silicon Valley, Citco, if you if you watched it, it like they had a case when they optimized one module in the system and the whole system went down because it's way too fast.
So it's like it sounds like you have done quite a bit of job to actually keep this shape of flow. And like if I understood correctly, technically speaking, Westpaw or portion of Westpaw is implemented in Java. And then portion in C or C++ and then you also have some Python.
And maybe you can talk more about the choice of languages and sort of culture that there isn't the team. But I'm also curious like around the same time. I've actually seen was also developing right quite quite fast.
Did you kind of look at what that team is doing which is like an open source project? Was there something to loan from? Yeah, so let me tackle the first questions around Westpaw and the kind of languages that be used. And there's a lot of things here to cover. So Westpaw is around 1.
7 million lines of code, the total Westpaw platform. And it's a roughly 50% is written in Java. And 50% is written in C++.
And why do we use two different languages and what are the trade-offs?
So in the Westpaw architecture, we made a clear distinction between what we call the cluster that holds the content where you actually index and invert the documents and you have all the data structures for fast searching in these data structures.
The content layer is written in C++ because you're managing a lot of data. You have the data that you need to have in memory and so on. So and it needs to be fairly efficient. And then on there what we call the stateless layer is the layer that actually interacts with user requests.
So user requests comes in. It's accepted by HSP server and there you do and that layer is written in Java. So you can also then deploy plugins. You can write your own searcher functions that can dispatch the query and get a reply. And you don't.
It's transparent from a given searcher if you have a 100 node cluster or if you have a single node cluster. So that's kind of hidden away when you deploy a plugin. So those languages have different trade-offs.
So it's a lot easier for people to write plugins using Java without shooting themselves in the foot using C++. So in the content layer in C++ we don't allow any kind of plugins. You can contribute or you can contribute to the open source but then it needs to be a kind of feature.
We don't allow you to embed a library or something into the content layer. So that's a trade-off. So then you mentioned Python. We have a Python, what we call pi-wespa which is language binding on top of the HDP API. So it's not of the core kind of westpides.
It's an API where we built around interacting with westpa, doing model evaluation and evaluating for example different retrieval and writing strategies. So that's the kind of language. And regarding your scene, Apache Lucene. So if I recall correctly, I think Apache Lucene started in 1998.
So around time. So there's a lot of inspiration of course and it's not that many ways you can build a search engine. So I'm losing pretty much, it's a really good library.
So yeah, definitely we look at what's happening in open source and they have a lot of admiration for the work and the committers of Apache Lucene. I mean, it's a great job that they've done and they'll be able to develop this over 20 years.
And the core difference is between westpun, Apache Lucene is that westpun is a full kind of engine. So it becomes more of like comparing westpun with elastic search or Apache Zoolar, which is kind of an engine on top. So there's no like westpun library which you can use.
You have to kind of buy the whole, you have to buy the whole platform. Yes, basically like a web server around it and all the components like the nodes and overseer and other architectural elements. Yeah, for sure.
And on the Python side, I'm also curious like with all the development of models and you know, hugging face and you can pretty much find a paper and then most likely there is a model already available in some shape and form.
And so the Python layer in westpun does it help you know newcomers to kind of easier experiment with these models in conjunction with westpun? We do hope so. And that was one of the goals for making py westpun.
So there are different kind of use cases where you if you have like a more of a low query volume, maybe you have 200,000 documents or something like that, you know, not really not really very low latency and so on.
Then you can use Python and do embeddings and you can play then it natively works with hugging face and all those libraries that are typically written in Python. And then you can use westpun, just purely HTTP based APIs and so on.
The other option, which is more involved, I have to say, and that is that you can take a transformer model, for example, and export it to one X format or on X, which is open neural network exchange format.
So that's a kind of open neural network format that multiple companies like Microsoft, I think also Facebook have rallied around, you know, this open format.
So you can take the transformer models from the hugging face library and then you can export it to on X and then you can import all next models into westpun for evaluation.
And westpun we integrate with on X runtime, which is open source library from Microsoft, which has a lot of different language findings, Python, C++, Java. So it's a really great library and we integrate with that.
So you don't use it directly, but we have like you can put the model here, westpun you can be use it and you can invoke it and so on.
 And those models and then you're kind of a trade off between, you know, getting to know westpun playing around with it and then, you know, maybe low QPS, but in the scenario where you have a really large scale, you want to do 100,000 per cent back and there's something like that, then you move it to on X and deploy it actually inside the westpun cluster, which has many benefits because then you don't transfer a lot of data over the network and so on, because network is still even, you know, within the data centers, maybe the network limitations have this sold so you can get 10 gigs or 25 gigs even, but going cross region, then latency is still concern and that's that's one thing that really fascinates me is that we're still sometimes, you know, the use cases are bottlenecked by the speed of the light, right?
So yeah, going from the east goes to the west coast and the US is easily 100 milliseconds.
So hasn't been yet canceled or sold so yeah, physics.
 Yeah, this is fantastic and and so and also like even before we go into this wonderful world of models and latest advancements like I'm still curious also to dig into the item that you mentioned like you when when you have been evolving westpun over time, you found a need to add something really interesting, some really interesting data structures like tensors you mentioned and like could you elaborate a bit more on how this need arise and also like, you know, what are the use cases, typical use cases for it today and also how accessible to an average user of westpun so to say.
Yeah, so I'll do a little bit of history on that. So the best for document model you write has a fixed kind of you have to have a defined schema in westpun.
So you have to define it for instance, you have a document type called document and it has a title, it has maybe some time stamp, it might be have an integer attribute.
 So there are different like normal document model, what you expect from kind of any any schema oriented database and we also had vectors so you can do early on that you can actually do brute force dot products as part of ranking because that was really popular among in in your you know for various ranking requirements you will multiply or sorry, you will perform multiple different dot products over the documents that you you're queried as retreat then in around 2013 2014 the researchers in your outside, you know, we really want to express these type of recommendation models where we can use the general concept of tensor so not just storing a vector in the document but even a matrix and they had some use cases around recommendation.
 So for instance in the in the in the document you can represent in the matrix so you can have multiple is this document popular in multiple different categories for example that you know this document is popular among people that are interested in use this is in the ones that they're interested in finance and so on.
 So it's a really like complex and complex like that you can actually have both the tensors in the in the document side but also the query side and then you can do during the ranking phase you can evaluate these kind of expressions so it's a really it's a really powerful the language and one example concrete example is we haven't touched on the language models and so on but for instance the callbert model which is contextualized late interaction overbert where you actually take the query is not represented as one vector but each of the terms in the queries represent the desivector and similar on the document side each of the document terms are represented as a vector and then at runtime you retrieve documents and then you rank them based on this maximum similarity function so it takes the vector of the first term and then it performs k dot products against the vectors of the document terms and then you you take the maximum of that score and then you do that for all of the terms and the final is the it's a sum so that was actually one of the things that I personally the tensors hadn't been that much used for search use cases but more around recommendation use cases when I when I when I saw callbert and I saw the maximum operator I was like this is just perfect fit for for the best potential it's a perfect use case so yeah yeah that's one example yeah awesome once you described like when you go like many models today is like okay embedded spas that you embed this paragraph whatever but if if you need to go world level that's like lots of data lots of computation right so how you would even do this sounds like tensors have found the use case there yeah and in in in in callbert what when we we represented callbert on less also we did a large sample application around the ms marker dataset the passage ranking dataset of mammoth marker so we made a sample app where you can combine these different retrieval and ranking strategies and but in our case we used callbert as a re ranking model and that's one of the really strength of of espice that we allow you to express really complex retrieval and ranking pipelines so that you do a query and then each of the nodes involved in the query they will do a local ranking or matching and then you could have a second face locally on each node and then when you have the kind of global view after you have done the scatter gather then you can do another re ranking face because then you have the global view so there are a lot of possibilities to kind of trade off between accuracy and cost them yeah yeah exactly and actually as you've been describing this I also realized that we've been recently discussing in one of the podcasts about multi-stage runker right so you could have either a sparse or dense retrieval but you can then later use your graph algorithm to kind of like re rank the items I think it was in the podcast with Yuri Markov the author of H&SW algorithm and so have you have you seen any use cases based on espice you know for multi-stage ranking pipeline?
 Definitely I mean so both the search internally in our we also see this outside from customers using last but they do multi-stage retrieval and ranking pipelines so there's basically the reason why you do it typically is that it's too expensive to evaluate the kind of final ranking model over all the documents right so you take some kind of approximation of that model and then you execute that as to kind of candidate the treaver and I think one of the we haven't talked about the vector search capabilities of VESPA yet but one of the beauties of VESPA is that we after we integrate it approximate nearest neighbor searches that you can do a combination when you actually do the matching and querying that you can combine it the regular sparse or keyword search with a vector search and then you re rank and it's kind of paradigm of having multiple stages you know you see that in the question answering pipelines as well right or you have retriever and then you have what they call a reader right so it basically finds some candidate passages from Wikipedia and then extracts in a reader but evaluating the reader which is a complex typically a transformer model where you input both the query and the document at the same time into the deep neural network it's very complex to actually evaluate that overall the potential passages and user types.
 It's like super intensive and I'm super curious to drill into this topic of like combining you know neural search with sparse search actually before that as you've been talking I've realized I'm actually now taking a search with machine learning course dot by grand ingressol Daniel thank you like it's a fantastic course I can highly recommend it it's super intense as well and I think yesterday grand mentioned that there are companies which you know that they really need to optimize only like top one or top two results and they have built models to optimize only that top one or top two which sounds like my mind blowing right and that was like something maybe this applies to web scale to some extent and one of my recent experiences is actually in web scale search engine we have a mobile screen and so we can only show top three results and the target is obviously to have a high CTR and so we've quickly noticed that if you do a sparse search without any logic on the query whatsoever CTR is very low so you have to do some tricks like query understanding and also trying to increase precision at the same time maintaining the diversity of search in some degree so you know basically it's very easy that with sparse search you hit just the tip of that iceberg and basically say okay I have three teacher jobs for you which is not that interesting because we don't know if the user is looking for teacher jobs right so so that's that's like have you seen cases like this I think these are really really challenging ones yeah but generally if you look at the results like if you ever rate on MS Markov for example and the official metric there which is the mean the reciprocal rank right so if you get the perfect the actual relevant document you're able to retrieve it and put it in position one that query gets a score of one right but if you put it in the second place it's gonna have a score of 0.
5 I think that's really good measure when you talk about mobile screen precision at 1 2 3 so that's really important but in the kind of retrieval not this stage retrieval and ranking pipeline it makes sense to spend more of the computational budget within the lakes SLA on those top K hits right so like in when you go to Google today and you do a search probably 100 million documents will be excluded in just a fraction of a millisecond right and then there are multiple stages and you can be sure that the kind of the the 10 last documents from the previous stages that the invest more time or computer computational resources on those hits yeah yeah exactly and also the good thing is that is that because that's when I talked about the West Architecture where you have this division between stateless which is doing the scatter gather and each of the local nodes is that basically in a search engine today you need to move move computations both to the data but there's a lot of talk about you know moving or separating compute from storage which is a huge thing right in the cloud but in search in search use cases with high triplet high document or you need to be able to do both you need to do fast computations across multiple nodes and then you transfer data like in last well each of the hits that you can include ranking features or so on that the subsequent phases can actually use for re-ranking and the good thing is like I know you've done a talk about diversity in search results and so on is that you need to have that global view you know in order to kind of optimize for for diversity and then you can kind of throw away a lot of the hits that you're not going to show because of kind of business constraints or diversity constraints and you don't need to invoke the heavy model for those hits yeah so yeah I think it's interesting for these kind of pipelines but one thing that is challenging regarding both the stage pipelines is that they interact with each other right and if you do if you have like a system for training your model retraining the model using statistical features what are users clicking on and so on the one of the features then you will have some biases towards the actual the ranking algorithm that is in place today because that's the model that is bringing interactions so you basically just retrain on the top hits and that was what we saw on Amazon as well as that when they started to improve the retriever so when it's not actually instead of having a BM25 like do BM25 and then rerank they had a mean reciprocal rank score of 0.
35 or something and now after changing into a dense retriever now we're talking about 0.
42 or something like that so by improving the improving the retriever right because the retriever kind of sets the upper bound you know because the rerank cannot really dream up you know the relevant hits if the retriever hasn't retrieved it right so that's an important point you know in the retriever and writing stages so exactly and I think we can gradually move into neural search and vector search but like you know it was one of the students question also yes then the same course how much you can actually solve with the rerunquer if your first stage retriever didn't even find what the user is looking for which means probably the query is not a match for this search engine you know let's say they're looking for a specific model of a phone but they don't even cell phones right so like and I think the response from Daniel Tankilang on this one was that actually you can implement a query understanding system which will understand the query as much as it can and if it knows that there are no such items in the database don't even bother searching for them and I think this was a really really clever advice on it and and and he said that system worked extremely well so like for user for user satisfaction to save their time right because in the end what we're doing is actually optimizing the user journey which then translates into business right so that was a fantastic example of how you can also talk such search problem yeah and that's one area where I wanted to because we're building all of these sample applications what you can build with VASPA and query understanding has been one of the topics that I wanted to build out to to demonstrate you know how to do that especially building it using a transformer model actually so you can have different ways of doing this but one way of doing it is to use it as a multi-label categorization problem so given a query here are the intents and their probability but what's stopping me from doing this is that we need to work on kind of open data sets now and there are very few query data sets in this way so one approximation is actually to train using the title so in the e-commerce set you can train based on the titles but then you need to have some kind of label on you know is this you can do it around categories so you have the title of the e-commerce listing and you have the category and the beauty of this is that you're actually mapping free text queries into kind of a fixed predefined vocabulary which is the categories and then you can actually eliminate zero hits the zero hits problem because you actually no longer retrieving based on on the free text queries but you're retrieving based on the most kind of interesting categories so yeah so these are really interesting you know topics and that's one thing that I find you know with search you know and why I love being in search is that there's there's there's there's a ton of things that you can you know build and you know there's query understanding you know there's facets there's retrieval and ranking dense bars you know and then you have the scale of it you know how to make it fast you know there's so many things you know they're just query understanding you know it's probably you know a full research topic you know on its own so there's so many things involved in search so that's yeah yeah it's like endless journey I agree it's like yeah it is you can also dive into an old piece out of things or you can stay with like scaling of search or query parsing whatever that you find passion and maybe your passion changes over time as well right so you did a bit of an LP then you move to query parsing then you move to maybe even scalability or whatever yeah I agree it's like a fascinating topic and also what fascinates me is that on the other side of things users are also not sleeping they're puzzling you all the time with new queries seasonal changes data changes as well because in mid-size a larger company it's usually work of multiple teams and you know or departments some departments looking after data some looking after ranking recommendation all the feature collection and what not you know something somewhere can sometimes go wrong and you need to prepare for it you need to interact you need to kind of build a system that is resilient and it's it's a fantastic fantastic space yeah it really is and there's so many methods and that's also one of the things you know people you know they want to build something that is great you know but even if you're using a passion to see know if you're using Westbar you know you need to have kind of some investment of actually getting great results and that the same thing if you're using like a vector search library or you know you need to have some kind of data pipeline for your documents and queries so there's you know I'm not a huge believer in you know none of these technologies really work that well you know out of the box you know it's it's such as definitely not a sole problem and even if you look at Google you know they're struggling as well you know there are many queries of question answering and so on that they totally get wrong you know and people want to build Google but they have like maybe two guys you know or or girls you know working on search you know you you you don't build a great search experience you know if you're by a team of two two people yeah yeah it's a huge investment and also like time investment not just like you need to hire a lot of smart people but you need to give them time to actually go through all these challenges and you know now that you've mentioned vector search I'm actually curious like when in Westbar journey you know did you first hear about vector search and actually what caught your eye and you know like sometimes even today when companies evaluate whether or not to take the neural search journey or stay with this part search journey it is not that obvious actually and and maybe you could share some advice there as well but maybe first if you could also do a historical deep dive there super exciting yeah it's it's so we've been using like dog products and so on for search but it's been it's been brute force right so been able to do brute force vector search in Westbar for a long time and then in 2018 bird came out and in January 2019 the researchers published really great results on them as Marco Pasadranking and then we like you know this is this bird model you know how can we use it you know is it you know there are a lot of things you know to get your head around you know what its bird is and how to use it and then we saw that there basically were two ways of of using it either as a representation model where you encode the query and the document independently and then you can build using a vector search library you can you build the index of your corpus and then you can retrieve pretty efficiently if you have La Crocs Med Search version so that actually was what motivated us in 2019 we started that work in summer August to actually have vector search and then also in term in Java there are a couple of image search use cases around hamming distance so they were pushing for that so there are multiple things and also our users it was open source by then so users were also asking for it you know can Westbar do vector search you know we see that we could represent vectors but it's not that cost efficient if we need to do brute force so then we start looking at you know it and we had all the kind of building pieces we had the tensor the document models representing floats and all these numeric fields and so so we had it wasn't a lot of work to get all the kind of pieces together but we had to implement the algorithm and we did we did a pretty I think like one month where we actually surveyed multiple algorithms for approximate vector search you know how could they fit into the Westbar model of doing things so that's the background of kind of why why vector search came to Westbar and I was really exciting when we started working on that because there were a lot of interest in it right so there were people wanted to work on that project so yeah of course because it's something like a bleeding edge and like a new but also like one of the podcasts I mentioned I think it was also with Yuri Malkov that I've I've had a friend who worked in essentially vector search but he was a mathematician himself right so I also viewed it as a pure mathematical concept and I was like yeah he's playing with some theoretical you know advancements and then he actually gave a talk at Google you know as well actually presenting this algorithm and the nearest neighbor search essentially and how to optimize it and even then I wasn't like essentially buying in and like okay it's still mathematics but then when I was reading H&SW paper I saw them citing his work I was like wow so now these paths have intersected so now this makes sense and you know usually it excites me when it's put into practice is that how you felt as well like was mathematics aspect of it like engaging for you or did you view it more like an engineering sort of yeah I'm definitely on the engineering side so I'm definitely on the engineering side so for example on transformers you know I don't care about the deep neural network architecture how these interacts you know I basically treat as a black box you know this is this is the box and you need a tokenizer for it okay what's the tokenizer what's saying people's output what can I use it for you know I'm not gonna do and they be I mean a lot of research actually study you know how can we build ultimate in neural network architecture so definitely know from for me that was not the math involved but we we have some people in our team with a heavy math background and you know they can teach me a little bit about what it's a proper distance metric and you know why why this one work and this one work so that that was really also a learning experience for for me to engage with such core team on this feature and a huge discussion we had you know who was you know one of my main point was that you know we need to be able to integrate for users when they want to use vector search they want to have filters they want to be able to express this in our query language so that you can combine the best of both worlds and and that took really some time you know to to get that right and that was really you know really fun to see that that you actually can write a query and say that hey give me documents that are near in vector space then filter on this attribute but at the same time also compute or retrieve based on the weekend query operator which you heard about weekend which is an optimization technique for doing spatial chival and that you could actually express that in the same query and I have to say that I was really proud of our effort when when it came out with that and and could be able to combine it and that's really if you look on the future side I think vector search it's been the biggest game changer for us was to actually integrate vector search because that's speared a lot of interest into VESPO yeah yeah and I can actually have people coming in you know yeah but I can imagine that vector search can still be useful in search as well as recommendation systems right yeah exactly so so and that's one of the things that you know you see that factorization machines dot products has been used for recommendation for a long time so you basically see the technology for search and recommendation use cases kind of merging into the kind of same same space technology space and for those type of use cases I think VESPO is really strong technology and but the interesting thing that I want to mention is that we have people coming in you know asking about VESPO thinking that it was a vector search database and then they realized hey you know there's keywords there's ranking there's a lot of other features here you know so that's been interesting for me you know you know I see vector search as a feature of VESPO in this whole kind of serving engine but you can use for search and recommendation not like I see vector search as a very important feature but it's like one feature of VESPO yeah I have to admit that part I probably played that role in bringing those users onto you through that blog post that I will of course mention and did mention multiple times and where I compare multiple you know now seven vector databases and I did put VESPO in that corner just to consider only the vector part but I knew that you guys over a lot more and actually still learn at some point hopefully we'll use VESPO in some project that I can actually evaluate but yeah you absolutely right that some of these systems are actually beyond just vector search and you know also the use cases like the way you view this right you should actually take a step back and ask yourself what is it that you are trying to build yeah I think it's really important and so when you look at vector search and we didn't so to clarify on the algorithm side after investigating an oil and several techniques we went for your emalco's H&SW algorithm so we implemented a version of that to be able to also handle filtering real-time updates and so on so but I think one discussion that is is not heard that often is that vector search when you introduce kind of H&SW or any technique you are losing some accuracy compared to the brute force right so for example a data set that is called SIFT one million documents you can do a single treaded route for search over those one million vectors in about a hundred milliseconds right but if you do approximate then some parameters of H&SW you might get down to 0.
1 milliseconds as well using a library right so it's a thousand times faster but by doing that you are losing some accuracy and that's kind of when I see blog posts about approximate vector search without mentioning the kind of trade-offs between recall and performance then I like you know you should include the recall numbers because there's really so it's really I think it's really important for many use cases right it might be that you need to do use a brute force because that kind of approximative error that you introduce is not acceptable right so we do have use cases in now that we actually use we don't have like large amount of documents that we actually use a brute force search and best but best best supports brute force search so yeah yeah okay so you can switch and that's the beauty is that since we support this you just say in the query time you can say approximate through your false and that means that you can take a query run it using a brute force and then you can compare the result for the brute force which is exact with the approximation then you can compute the overlap between those two and that's typically then what's used in the recall at k right so I did two blog posts on what I call billion scale vector search with with last one where I did deep dive I think into these kind of trade-offs because when you introduce approximate you also need to build these kind of index structures so in hnsw you need to build the graph right which is time and resource taking time you know I'm costing memory so there are all these kind of trade-offs and that's generally I mean generally for search a lot of trade-offs but especially around vector search I call it the jack of old trade-offs because there's so many things you know to consider you know memory usage this usage CPU and so on so yeah that love the term jack of old feed-offs yeah but it but it really is you know you really have so many trade-offs and some companies you know maybe you have lots of data but you don't have any real tripe it right in that case maybe disk a and n or things that basically using disk is is a good alternative because when you're buying servers in the cloud or renting servers in the cloud you pay when you want to have this amount of memory you get this amount of CPU right there comes in a relationship between the CPU and the memory and and so there are different trade-offs around you know what what's actually going to use it for you yeah exactly have you heard any other misconceptions about neural search at large you know when somebody comes and says hey I want to implement a question answering system you couldn't principle use sparse search techniques or like query understanding techniques you know to actually almost do it in the rule-based fashion but like neural search on the other hand is like you know new sexy stuff everyone's to try out so the question is like have you heard of any misconceptions or something that people think it's much easier than it is yeah that's that's I mean it's a fantastic question I think you know you can just sit back you know this is I'm relaxed for a few minutes because this is a topic that I really love um yeah so so so the first time when we if you look at semantic search especially around vector search if we semantic search might mean a lot but if you look at the kind of the typical that people use semantics search today is that you have this vector search right you have independent query embedding in the document embedding and so and if you base this if you take them pre-trained language model from hugging phase and you just pull that model and then you encode your queries using for instance the CLS token or the average over all tokens and the result that you will get from that is not going to compete at all with the VM25 right because that language model has not been it's only been learned learning how to do mask language model right so it's basically it's been trained on predicting the next word right so it's a deep neural network that's it's not been trained for that so it's basically like taking some deep neural network for my vacuum cleaner and put it into my car you know to try to try to try the car it's not been trained for that right so that was one of the things you know when we struggled as well when they looked at bird and the other people like oh that's so great and then we had the engine and we could like compare it with VM25 and then we did bird here and there was like these results if you look at the actual information retrieval benchmarks they're like the results are not good they're they're like really so then came the kind of you know realization I think that's actually happened around industry as well in 2020 when the DPR dense passage retriever paper came out from from a Facebook where they trained on natural questions the Google dataset they actually trained this dense retriever and the dense model using a contrastive loss and hard negative mining so they basically demonstrate you know how to actually train a dense retriever model and then we actually saw the results were much better than than VM25 in that but but it's a huge so that's one area where I think that people just using the pre-trained model might not work well especially if it's not been tuned for retrieval and even if you look at MS Marco which is the largest data set out there that you can train a model on if you train a model on MS Marco and then you apply that model into a different domain so on a different dataset it might not outcompete VM25 in fact it actually in many cases it is actually underperforms compared to VM25 so and that's why there's a lot of interest and especially recently is like you know if we combine this exact matching you know the actual user search for this phrase but we also have the vector representation you know how to combine that and that's that's actually two of my colleagues are right now working on the beer dataset to they open the PR to the to the dataset to include VASP as well and then we will demonstrate some methods for combining sparse and dense.
 Yeah that's awesome like I've read the beer paper after you referred it to me actually and it was quite eye-opening because it does compare not only sort of like search engine algorithms and approaches but also datasets and tasks right which different tasks like searching or answering questions may matter quite a lot and so it was quite an eye-opening that first of all VM25 is fairly competitive so it's not a loser not at all so like you should still consider using it like and actually maybe even keeping it as a strong baseline in everything you do and I know some companies by the way still use TFIDF so maybe they should also like first transition to VM25 and only then jump to neural search techniques are like a denser trivel and and I think you also mentioned that and I saw by the way that you have participated in various competitions on denser trivel and on ranking like can you can you elaborate a bit more like what drives your interest there because to me that sounds more like academic interest in a way right but of course you're also showcasing and probably bringing ideas back to that spa.
 Yeah so the motivation was actually around them as Marco passage ranking and where we actually could use this dataset and then our dream when we started to implement vector search was one thing and the other thing was you know how can we represent the re-ranking using bird in westbound so using the actual bird model inputting both the career and the document at the same time so that was one dream we had and but we were looking at the results and I think the first paper that we read it read that they they used maybe a day to with even with a GPU to actually perform 3600 queries right so it was not really you know how can we make this practical and then two years later we actually did did beat their benchmark and to end represented on westbound and we were doing it less than 100 milliseconds so on CPU right so but there being a lot of learning to get there but that was the motivation to kind of demonstrate that you can take this state of the art or close to state of the art with three-wheel and ranking pipeline from an open dataset which is how widely recognized and all the researchers are actually publishing papers around it you can actually take that model and use westbound and get those results you know so it was one way of demonstrating that you can actually then you can actually use these models with westbound and have it serve in your state so that was actually the motivation not on the kind of science side and so on but I have to say that I really would encourage everybody that works in search to look at some of these open datasets you know play with them you know maybe you have some ideas you know around search and how to do search and there's a lot of talks about boosting this phrasing you know how actually does that impact the results on kind of a dataset and I can really recommend the track COVID which is a dataset that was made at the start of the pandemic and it has about 50 queries and deep judgments for each of the queries and the collection is rather small so you can play with it on a single node and so on so that I will really encourage you know people in search to try out you know because then you get the feeling you know does it actually work does it actually you know compare it with BM25 what happens if I do phrase matching or do something clever you know so I think that's and and I'm really not a huge fan of anecdotal query examples to see these kind of commercial actors with this you know I'm searching for this on this magic results you know I'm more into you know demonstrating that actually Westpac can do this and it has the funding and actually on the real datasets.
 Yeah and I agree in the end of the day what matters is first of all can you apply this tag as you said in your real setting right in your domain then another thing that you mentioned just now you know the track COVID dataset so maybe as the result of your research you might also impact on the global situation right maybe somewhere locally maybe somebody will use your work to actually implement a better search system so I think that that's also a fantastic segue to you know the the context that you're doing and that's actually a very interesting point because we had at the start of the pandemic we built a cord 19 search interface that we published online so people who actually go and search this dataset and people they were I don't I don't recall the details but it's still online and people actually because of all open source so they forked it and then they started using Westpac and based on that and I think it's a much better shape that service right now than the the cord 19 search that we did so they actually built on that work so so that's that's great I love to put what I call sample applications you know how what can you build with with Westpac and and that's actually a lot of my time these days are spent on making these sample applications smooth and easy to to work with and especially we've been rather weak on the kind of UI putting together front dance and so on so that's actually some work that I'm doing right now to kind of build more of the product you know what can you build with it because people don't get really excited about looking at Jason I output you know to actually see some interactions faces facets you know out the completion and to actually build that whole experience you know for the for the product people it's like looking at the engine when you actually want to maybe look at the car right and then you get fascinated by how shiny and sort of sleek it is and then you're like I'm buying it yes yes I totally hear you there and like actually in these use cases you know there are other platforms you know in the neural search space also doing multiple demos have you been looking into the direction of multimodal search does that excite you do you think it's too much of a bling edge or niche use case or do you think it has potential because of the neural search crossing the boundary of text towards the image audio and so on yeah I think multimodal is really where recto search is shining so this is the area where you it really shines I have some doubts about out of the main like we discussed using a vector model for text search if you don't have any label training data and so on and adopted to your data using vector search alone for that I think is questionable but looking at this multimodal where you combine both a transformer model and a typical image model and you train that representation and from what I've seen from these models and we did a sample application on this as well using the clip embedding model from from open AI and looking at the results I I have to say that I'm really impressed by kind of just eyeballing I don't have any kind of I don't have any hard data sets or but it's really impressive you know what that model can can actually do so I definitely think that multimodal is it's very I don't think it's I don't think it's that far ahead I think because we have interest in representing clip in best from from actual questions I'm actually I'm seeing an email right now you know how to they want to help on their schema and definitely they want to use clip yeah so definitely I don't think it's that advanced at the moment and I think we'll see another thing that I'm working on right now is that I talked about our sample applications I want to build a new sample application that demonstrates in a UI in an e-commerce setting where you combine different kind of fussy matching exact matching vector search all in the same query and then you can have some sliders where you actually slide these you know how does the result change and they change in real time so I just need some help on the on the react front end because I'm not I'm not a great JavaScript programmer I have to admit so I need some help on that so yeah but I definitely think that multimodal vector search has a really has a huge number of use cases yeah I hope that amongst listeners of this podcast maybe there are some with front end skills and maybe since you're building this for open source you know that might be good use case as well to be contributing to this crazy journey but we have yeah I mean that would I mean definitely we do see more involvement and contributions from from the in the kind of community around VESPA so I think we build a lot of the last two years of the community side and people getting to know more about VESPA and actually starting to contribute back both on the sample applications and also documentation and also we're seeing our more involved in contributing to the code so definitely yeah so but I think it's from a product side it's really important for us to and also we have a commercial offering of VESPA where you actually have a hosted interface hosted solution multi-region and to I think it we want VESPA to be able to run fully fledged in your environment if you want to use it because it's open source it's our Pasha 20 if you want to use our cloud you are welcome to do that and to kind of have and the same kind of functionality and what we add in the cloud is CICD pipelines how to do multi-region failovers like in the US East US West you can have different so all this kind of top and take care of sort of take care of nodes failing and whatever you know the hole the kind of host the experience so and that's been an issue with our sample apps they have been like it has been some friction around you know how to deploy them locally how to deploy them to the cloud so I'm trying to kind of bring them together so that they they work in in multiple environments yeah that's a lot of sense and I guess it takes a lot of engineering effort to also kind of cover all these different use cases so sounds quite exciting and actually demoing the technology I think you know as you know other vector databases have got it and I think it's a such a low entry for especially for non-technical people or those who are in charge of businesses business units to actually make decisions and I think for them you know having a relevant demo is going to be quite a game changer because if they need to reason about your technology only through the eyes of engineers in their company then probably that's that's much longer path right yeah exactly and I want this experience to be as smooth as possible so that you can get started with the sample application run it locally get some data into it fire up your front and react and you can interact with it and if you're happy with it if you want to share with your friends you can upload it to the Westpac Cloud and then you can share to URL to your friends and that's a model that I really believe in that you can it's open source so you can actually run it locally and then you can take the cloud provider can actually take care of the hosting for you so that's and right now we actually we are providing like free trials so you don't you only need an email address for the Westpac Cloud you don't need a credit card or things like that so you can actually play it play with it and run with we can even leave a link where users can try out Westpac and subscribe so I think that will be quite beneficial and actually I was thinking like even though we a little bit drifted in our conversation away from better search you did mention the exciting space of combining you know better search with smart search and I wanted to take it from the angle of a non-technical user right so let's say they come to you and they say Joe can you actually enlighten me a little bit on how do I combine these things maybe I just want to deep my toe and vector search just to see what it cannot cannot do in my domain what would you recommend them to do assuming that they already have maybe like a smart search engine and maybe they are evaluating Westpac as one candidate yeah so I think the question is if you're using Westpac it's rather easy to do this because you you can express it in the query and then you write the right key profiles saying that you know this is how going to combine the sparse ranking single for example be on 25 with retrieval for others that are not using Westpac using for example elastic search and open source of our shesolar what we see is that they build a lot of infrastructure on top of these so they actually have the ranking layers outside of elastic search right so in that case is you could have kind of a vector search library running at the side of elastic search and then retrieve and then you need to you need to keep those two data stores in sync and then you can in parallel fetch okay give me elastic search your best results and vector search database give me your best results and then you can use a technique called reciprocal rank fusion where you basically merged results based on you know are they are they ranking you know it's the document found in both so that's that's a powerful technique of but you don't have to actually know anything about the distribution of ranking scores and so on so google is writing a lot about reciprocal rank fusion so it's interesting direction and that's one thing we know from Bing and from others from from both Bing and from bydo in in China is that they're doing this kind of mix mix retrieval with different systems for sparse signals and then signals but but then you have for the regular uses you have a lot of moving parts right you have different data stores make the manned ship and that's one of the things that we try to our advantage is that when you're using Westbyes that you know you you get these capabilities in the same engine you don't need to store the data in different stores and having consistency problems because of that yeah yeah so I will definitely if you're interested if you're sitting there today with open source or or elastic search and you don't want to invest in in in in the vast park you could try this batching the query and doing reciprocal rank fusion yeah yeah it could be like one way to actually introduce something from more like semantic search if you view it that way right so that's a great idea because I think there are multiple approaches to this and I think if you are within one search engine like say VESPA or elastic search open search a solar would have you then I think you could in principle experiment with like fusing you know the neural search result with sparse search using some kind of linear combination as you actually retrieve it right yeah so so so so you so you can actually use the linear combination but the great thing about this rank fusion is that you don't simply you don't look at the ranking scores so you basically just fuse them by the order of their returns so you don't have to know anything about the score distribution like EM25 it has basically unbounded it could be 25 it could be 100 to be 5 right so it's very difficult to to to combine that using a linear model because you have two signals you know and one is number is going to be like this and now it was going to be between 0 and 1 so reciprocal rank fusion is definitely you know interesting case actually this is super great point and hopefully we can provide some links to this because this technique because I think I heard this question multiple times that would you set exactly just now that the score space is completely different and they are not compatible with each other and so you have to find a way to still interleave them or merge them right so that would you set exactly makes sense that you don't pay attention to the score space you actually look at the order and you try your best to interleave them yeah that makes total sense yeah yeah there was actually a recent recent paper on because there has been more interest in that these dense models alone that they generalize not that well what you're using out of domain and one of the things that the Google researchers were doing and showed promising results was using this rank fusion and I've seen this rank fusion in a multiple Google papers so so it's very interesting the researchers they're really interested in reciprocal rank fusion so yeah sounds like a popular technique yes I mean time flies and I really enjoy talking it feels like we could record another podcast what do you think I'm talking multiple topics but I still really love to pick a brain on that philosophical question and kind of ask you what what keeps you so interested like you are a loudmouth behind West Pine general but you also offer a bunch of advice right like through your blogs through your public presentations and even sharing papers on Twitter at least for me was super helpful that I could you know quickly read the paper that you shared but what keeps you motivated and interested to stay in this field and also specifically you know maybe you think something is missing in the vector search space or in general in in search space that you would like to fix yeah so it's a great philosophical question I think I'm not that excited about vector search I see that as a technique so I'm more like excited about search because I think it's such a fascinating problem we touched on it before you know you have query categorization spelling you have so many different aspects of building a great search experience and also the scale thing is really appealing for me you know kind of passionate about you know how can we do this billion scale how can we make it fast you know what if we need 100,000 queries per second what if we need to update all the documents in real time and within 12 hours or one hour or you know where's the limits you know where is the cloud going you know this compute versus storage can we now move more computations out of the storage layer there are a lot of these exciting on the kind of system things but on them kind of more science things you know how to build a great search experience I think you need to have this kind of multiple techniques and we didn't touch on it but vector search is one thing sparse search is one other but GBDT models tree based models is really ruling the search or it's kind of the hammer of search because those models on tabular data statistical features you know they really show promising results and that's another thing that I think is great than about west based that you can combine these GBDT models newer metals in the same ranking functions I don't think that there's a one single silver bullet for retrieval I think there are multiple different singles like for instance let's let's do vector search if you only do vector search if Google only did vector search only on the text right it would basically you have a lot of duplicates on the web you have low quality content you know there's page rank there other factors you know it's not only vector search there's that kind of different techniques so and so that means also that there's a lot of things new things to learn you know how do you do caricaturization you know how do you how do you how do you actually determine which facets and then kind of navigation you're going to show to the user and like you touched on at the start you know if your user does a query and we don't have any good results you know should we just slow them some random results or should they say that hey you know I'm sorry but we don't have anything for your query so yeah that's really what motivates me is that it's such a fantastic problem if you're interested in scale and all these kind of things coming together so yeah yeah thanks for that it's deep and it's very wide and I think it's like limitless space and I hope also that newcomers feel it's kind of like a low bar entry especially and we didn't touch on this but especially with your work and open source you know the support like you can go and slack or whatever tool you're using to communicate with your users and actually listen and address their concerns questions and hopefully this opens more you know more possibilities for newcomers to enter yeah I love I love actually it's actually a weakness as well but I love answering questions you know you can see me answering questions on multiple slack spaces you know I love people you know asking questions about search so I really love that and I'm and what really gets me if someone is struggling with something you know how can I do this with West Park and I'll try to explain it you know you have to do this and that you know and then I like I go back you know at the program saying you know we need to fix this you know we need to make this more easy for people to use right so it's it's a both way thing and that's one thing that I learned in my career is that you know listen carefully to your users how they're using the product what are the pain points you know how to how does it feel to get started are able to progress so that's that's really also motivating and and honestly I think that some of the work that we've done using some of these smaller transformer models has been has an impact on the industry like I got contacted by a person here on Twitter the other day said that you know I saw your tweet about these smaller language models like not the birth base that people usually turn okay but this mini LM model which is a distilled 22 million parameters that actually did the demo that you can run in your browser and it said you know I saw your tweet and I went ahead and tried it for my domain which was classification of hate speech and then he like did a blog post on it and he mentioned me and I think that was really like interesting for me to see that you know that I could share something that some people could actually make use of even if it was outside of search show and I learned a lot from especially around the relevance is slack space that we are both in the open social connections slack space so a lot of discussion there rector search and we are you know sharing some blog posts and then I ask Greg from Pinecoin a tough question maybe you know and so I really love being there and discussing and I learn a lot from from other people like just devins from elastic search and so and I'm from you and especially around Berlin best search last year you did the AMA on the vector search and for me like one of the key moments was that Max Irvin your co-host of that he said you know what if the user types of phrase query you know actually quote marks I want to search for this exact phrase you know don't show me anything else give me that phrase you know and that's something that is really hard to do with vector search alone right because you basically map it into this vector space and we do the similarities and that was a key takeaway from me and that was a really eye-opener for me you know you need to be building out better examples of how actually to combine sparse and then single so yeah this is amazing and what I enjoyed what you said is that you keep your practitioner hat on so you don't just buy in easily into these new models or you don't stay on the field of okay I'm only an engineer I don't even know what machine learning is because I think the profession is slowly changing and it's like a blend of skills where today you need to succeed as a search engineer and maybe it shouldn't be called the search engineer anymore like I think it needs some new term but we will probably be stuck with it for the lack of a better term but eventually you will need more skills under your belt and I think of the work that you are doing is amazing in sharing this knowledge and that people can actually reproduce it and I think that's super super crucial for the progress yeah I mean thank you Dimitri that's that's really nice of you and you know that's that's I yeah I think it's it's it's actually true you know to share and I think that what you said you know building a search team today is really hard because especially since deep learning entered the search field right so now you need to know how to configure and do matching and boosting an elastic search and now you also need you know how do I train the dense vector model and you know how should I you know should I use birch they use birch large you know does it handle multilingual text does it handle spell correction you know they're always kind of different things you know so building a search team in 2022 it's not easy because you need the kind of a mixed NLP search you know there are a lot of different things and that's what I love about it you know and I talked about on Twitter and you know in a talk I did earlier as well that this neural paradigm shift has opened this kind of knowledge gap you know how to actually successfully apply these methods and also on the technology side that we try to bring you know with VESPA that you can kind of combine different techniques we don't have to throw away 50 or 300 years of the inverted index you know we don't need to throw that away you know it still has value it's going to have value probably forever you know so so we don't have to throw away so that's interesting but that's also what it's been fascinating and I've said numerous times that I don't think I've learned that much in my career that I've actually over the last three years because reading papers it's not being a big kind of interest of mine earlier it's been one of the system side engineering side but that's been a high-opener for me you know to kind of how to apply these techniques and yeah so and to learn you know and that's the great thing about open source is that you know we can share ways of doing things yeah yeah absolutely sharing is caring and so much comes back to you as you said you know you get mentioned somewhere and you feel like you didn't do it in vain but also you might learn something new like a new use case and I feel the same you know when when I blog or when some video is viewed by somebody and then somebody says thank you even just multiple months after I did it and you know it's just an amazing feeling it's like a sense of connection as well especially in these days when we don't maybe meet socially as we used to but that's a new actually evolutionary new way of connecting and I feel much more comfortable and enjoying this more detailed conversation so maybe these interactions on Twitter they they bring a lot more value and I think this is super super great is there is something that you would like to share on Vespa development or maybe something that users might anticipate and maybe you want to point them to some tutorial that they might you know take a look at yeah so I can give a few product updates of what's coming from Vespa we are coming gonna release some integrated dense models for Vespa so though you don't have to export so you can you can use these models off the shelf and then we allow you to tune the Korean coder so you have the document code is frozen but then you can tune the Korean coder and then show you how to combine these combining both dense as far so that's one thing that is coming out other thing is that we're taking some steps regarding for love QPS use cases because we designed Vespa you know to be kind of low single digit male seconds on multiple different use cases but not everybody needs that so we're introducing some new options for memory management so that we can actually run on service with less memory so that's I think that's gonna be a game changer for certain use cases that don't need high throughput low latency so that's two things and yeah that's I think that's more than enough you know and there will there will be some some blogs I think about our results on the beer beer benchmark yeah yeah that's and I'm gonna come out also with a blog post on a technique called span which is a paper for Microsoft so m2n represented that on Vespa so it's really interesting technique with the hybrid combination of HMSW and inverted file and you can represent this m2n in Vespa so I'm gonna do a part three of my blog post serial billion scale so that's something I'm looking forward to but right now I'm that kind of refracting a lot of the sample applications and so on to to get the experience more smoothly yeah yeah sounds fantastic looking forward to it and we'll make sure to link all the blog posts that you mentioned especially on billion scale vector search and other tutorials that you mentioned and this is fantastic thank you for doing this and keep doing this keep finding the energy I know it's stuck sometimes but I think it keeps you also awake and sort of like pushing yourself forward and I think the best way to use your brain is actually doing something that is useful be reading a paper or implementing code or blogging about it so this is fantastic thanks so much for your active contribution thank you thank you as well yeah um and I really enjoyed this conversation I really hope we can record at some point down the road as well if you will be open to it and I think we can cover a lot more topics as well but I wish you all the success in your endeavors and stay warm and excited about the field yeah I will I mean such an exciting field thank you very much Dimitri for hosting this and you know we'll talk later on thank you thank you and see you around bye bye you