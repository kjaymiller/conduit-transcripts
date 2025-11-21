---
description: '<p>This episode on YouTube: <a target="_blank" rel="noopener noreferrer
  nofollow" href="https://www.youtube.com/watch?v=PNB70TbQUBE">https://www.youtube.com/watch?v=PNB70TbQUBE</a></p><p></p><p>Alessandro''s
  talk on Hybrid Search with Apache Solr Reciprocal Rank Fusion: <a target="_blank"
  rel="noopener noreferrer nofollow" href="https://www.youtube.com/watch?v=8x2cbT5CCEM&amp;list=PLq-odUc2x7i8jHpa6PHGzmxfAPEz-c-on&amp;index=5">https://www.youtube.com/watch?v=8x2cbT5CCEM&amp;list=PLq-odUc2x7i8jHpa6PHGzmxfAPEz-c-on&amp;index=5</a></p><p></p><p>00:00
  Intro</p><p>00:50 Alessandro''s take on the bbuzz''24 conference</p><p>01:25 What
  and value of hybrid search</p><p>04:55 Explainability of vector search results to
  users</p><p>09:27 Explainability of vector search results to search engineers</p><p>13:12
  State of hybrid search in Apache Solr</p><p>14:32 What''s in Reciprocal Rank Fusion
  beyond round-robin?</p><p>18:30 Open source for LLMs</p><p>22:48 How we should approach
  this issue in business and research</p><p>26:12 How to maintain the status of an
  open-source LLM / system</p><p>30:06 Prompt engineering (hope and determinism)</p><p>34:03
  DSpy</p><p>35:16 What''s next in Solr</p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20241107_011152_a59e71acc05fe03f850677d583f5111a.png
pub_date: Thu, 07 Nov 2024 13:59:44 GMT
title: Berlin Buzzwords 2024 - Alessandro Benedetti - LLMs in Solr
url: https://rss.com/podcasts/vector-podcast/1741381
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 20.92, "text": " All
  right, Dr. Podcast and here I have Alessandra Benedetti with me his second time
  on the", "tokens": [50364, 1057, 558, 11, 2491, 13, 29972, 293, 510, 286, 362, 967,
  442, 18401, 39753, 12495, 365, 385, 702, 1150, 565, 322, 264, 51410], "temperature":
  0.0, "avg_logprob": -0.45390538471501046, "compression_ratio": 1.2936507936507937,
  "no_speech_prob": 0.30223244428634644}, {"id": 1, "seek": 0, "start": 20.92, "end":
  27.8, "text": " podcast actually and exactly about same place we recorded two years
  ago.", "tokens": [51410, 7367, 767, 293, 2293, 466, 912, 1081, 321, 8287, 732, 924,
  2057, 13, 51754], "temperature": 0.0, "avg_logprob": -0.45390538471501046, "compression_ratio":
  1.2936507936507937, "no_speech_prob": 0.30223244428634644}, {"id": 2, "seek": 2780,
  "start": 27.8, "end": 32.4, "text": " I remember on Berlin was works. Yeah, we were
  here. Yeah, I guess I got 22.", "tokens": [50364, 286, 1604, 322, 13848, 390, 1985,
  13, 865, 11, 321, 645, 510, 13, 865, 11, 286, 2041, 286, 658, 5853, 13, 50594],
  "temperature": 0.0, "avg_logprob": -0.45363426208496094, "compression_ratio": 1.6929824561403508,
  "no_speech_prob": 0.42002952098846436}, {"id": 3, "seek": 2780, "start": 32.4, "end":
  38.2, "text": " It was. It was by the way a lot no easier if you remember them now
  but was", "tokens": [50594, 467, 390, 13, 467, 390, 538, 264, 636, 257, 688, 572,
  3571, 498, 291, 1604, 552, 586, 457, 390, 50884], "temperature": 0.0, "avg_logprob":
  -0.45363426208496094, "compression_ratio": 1.6929824561403508, "no_speech_prob":
  0.42002952098846436}, {"id": 4, "seek": 2780, "start": 38.2, "end": 46.44, "text":
  " closing day that we like people. Yeah, but I think it''s almost end of day as",
  "tokens": [50884, 10377, 786, 300, 321, 411, 561, 13, 865, 11, 457, 286, 519, 309,
  311, 1920, 917, 295, 786, 382, 51296], "temperature": 0.0, "avg_logprob": -0.45363426208496094,
  "compression_ratio": 1.6929824561403508, "no_speech_prob": 0.42002952098846436},
  {"id": 5, "seek": 2780, "start": 46.44, "end": 51.8, "text": " well here. First
  day of the conference and yeah, I wanted to chat with you.", "tokens": [51296, 731,
  510, 13, 2386, 786, 295, 264, 7586, 293, 1338, 11, 286, 1415, 281, 5081, 365, 291,
  13, 51564], "temperature": 0.0, "avg_logprob": -0.45363426208496094, "compression_ratio":
  1.6929824561403508, "no_speech_prob": 0.42002952098846436}, {"id": 6, "seek": 2780,
  "start": 51.8, "end": 56.88, "text": " How do you like the conference so far? So
  has been so far like a great conference.", "tokens": [51564, 1012, 360, 291, 411,
  264, 7586, 370, 1400, 30, 407, 575, 668, 370, 1400, 411, 257, 869, 7586, 13, 51818],
  "temperature": 0.0, "avg_logprob": -0.45363426208496094, "compression_ratio": 1.6929824561403508,
  "no_speech_prob": 0.42002952098846436}, {"id": 7, "seek": 5688, "start": 56.88,
  "end": 61.92, "text": " We''ve been seeing like many talks about the language modern
  integration with search.", "tokens": [50364, 492, 600, 668, 2577, 411, 867, 6686,
  466, 264, 2856, 4363, 10980, 365, 3164, 13, 50616], "temperature": 0.0, "avg_logprob":
  -0.4918078522184002, "compression_ratio": 1.6269430051813472, "no_speech_prob":
  0.013902271166443825}, {"id": 8, "seek": 5688, "start": 61.92, "end": 68.60000000000001,
  "text": " So that''s the biggest new trend. Vector based search is still quite a
  strong", "tokens": [50616, 407, 300, 311, 264, 3880, 777, 6028, 13, 691, 20814,
  2361, 3164, 307, 920, 1596, 257, 2068, 50950], "temperature": 0.0, "avg_logprob":
  -0.4918078522184002, "compression_ratio": 1.6269430051813472, "no_speech_prob":
  0.013902271166443825}, {"id": 9, "seek": 5688, "start": 68.60000000000001, "end":
  75.0, "text": " topic and in general with testing also like evaluation and explainability",
  "tokens": [50950, 4829, 293, 294, 2674, 365, 4997, 611, 411, 13344, 293, 2903, 2310,
  51270], "temperature": 0.0, "avg_logprob": -0.4918078522184002, "compression_ratio":
  1.6269430051813472, "no_speech_prob": 0.013902271166443825}, {"id": 10, "seek":
  5688, "start": 75.0, "end": 80.04, "text": " discussions around like vector based
  search or in general language models. And", "tokens": [51270, 11088, 926, 411, 8062,
  2361, 3164, 420, 294, 2674, 2856, 5245, 13, 400, 51522], "temperature": 0.0, "avg_logprob":
  -0.4918078522184002, "compression_ratio": 1.6269430051813472, "no_speech_prob":
  0.013902271166443825}, {"id": 11, "seek": 8004, "start": 80.48, "end": 88.32000000000001,
  "text": " and my thoughts was about hybrid search. Hybrid search. Yeah, so you work
  a lot on", "tokens": [50386, 293, 452, 4598, 390, 466, 13051, 3164, 13, 47088, 3164,
  13, 865, 11, 370, 291, 589, 257, 688, 322, 50778], "temperature": 0.0, "avg_logprob":
  -0.3404139738816481, "compression_ratio": 1.5765306122448979, "no_speech_prob":
  0.01298623625189066}, {"id": 12, "seek": 8004, "start": 88.32000000000001, "end":
  91.80000000000001, "text": " on solar right that''s your kind of like playground
  and that''s where you", "tokens": [50778, 322, 7936, 558, 300, 311, 428, 733, 295,
  411, 24646, 293, 300, 311, 689, 291, 50952], "temperature": 0.0, "avg_logprob":
  -0.3404139738816481, "compression_ratio": 1.5765306122448979, "no_speech_prob":
  0.01298623625189066}, {"id": 13, "seek": 8004, "start": 91.80000000000001, "end":
  98.2, "text": " integrate things but also then I heard that like guys at Reddit
  are using the", "tokens": [50952, 13365, 721, 457, 611, 550, 286, 2198, 300, 411,
  1074, 412, 32210, 366, 1228, 264, 51272], "temperature": 0.0, "avg_logprob": -0.3404139738816481,
  "compression_ratio": 1.5765306122448979, "no_speech_prob": 0.01298623625189066},
  {"id": 14, "seek": 8004, "start": 98.2, "end": 105.12, "text": " work that you''ve
  been doing also in solar. So that''s amazing. Tell me more a", "tokens": [51272,
  589, 300, 291, 600, 668, 884, 611, 294, 7936, 13, 407, 300, 311, 2243, 13, 5115,
  385, 544, 257, 51618], "temperature": 0.0, "avg_logprob": -0.3404139738816481, "compression_ratio":
  1.5765306122448979, "no_speech_prob": 0.01298623625189066}, {"id": 15, "seek": 10512,
  "start": 105.12, "end": 109.92, "text": " bit more about what is hybrid search right?
  How do you see it? What''s the value?", "tokens": [50364, 857, 544, 466, 437, 307,
  13051, 3164, 558, 30, 1012, 360, 291, 536, 309, 30, 708, 311, 264, 2158, 30, 50604],
  "temperature": 0.0, "avg_logprob": -0.30045333949998876, "compression_ratio": 1.6891891891891893,
  "no_speech_prob": 0.001479180995374918}, {"id": 16, "seek": 10512, "start": 109.92,
  "end": 115.84, "text": " And and basically maybe what are the challenges that you
  needed to solve and", "tokens": [50604, 400, 293, 1936, 1310, 437, 366, 264, 4759,
  300, 291, 2978, 281, 5039, 293, 50900], "temperature": 0.0, "avg_logprob": -0.30045333949998876,
  "compression_ratio": 1.6891891891891893, "no_speech_prob": 0.001479180995374918},
  {"id": 17, "seek": 10512, "start": 115.84, "end": 123.68, "text": " you still see
  related to hybrid search? So the first point and the reason I", "tokens": [50900,
  291, 920, 536, 4077, 281, 13051, 3164, 30, 407, 264, 700, 935, 293, 264, 1778, 286,
  51292], "temperature": 0.0, "avg_logprob": -0.30045333949998876, "compression_ratio":
  1.6891891891891893, "no_speech_prob": 0.001479180995374918}, {"id": 18, "seek":
  10512, "start": 123.68, "end": 126.96000000000001, "text": " decided to start working
  a little bit more in hybrid search and", "tokens": [51292, 3047, 281, 722, 1364,
  257, 707, 857, 544, 294, 13051, 3164, 293, 51456], "temperature": 0.0, "avg_logprob":
  -0.30045333949998876, "compression_ratio": 1.6891891891891893, "no_speech_prob":
  0.001479180995374918}, {"id": 19, "seek": 10512, "start": 126.96000000000001, "end":
  131.4, "text": " contributing this even our rank vision to solar is because of the
  limitations", "tokens": [51456, 19270, 341, 754, 527, 6181, 5201, 281, 7936, 307,
  570, 295, 264, 15705, 51678], "temperature": 0.0, "avg_logprob": -0.30045333949998876,
  "compression_ratio": 1.6891891891891893, "no_speech_prob": 0.001479180995374918},
  {"id": 20, "seek": 13140, "start": 131.4, "end": 136.56, "text": " of vector based
  search. So vector based search of course introduces like the", "tokens": [50364,
  295, 8062, 2361, 3164, 13, 407, 8062, 2361, 3164, 295, 1164, 31472, 411, 264, 50622],
  "temperature": 0.0, "avg_logprob": -0.3414122263590495, "compression_ratio": 1.6703296703296704,
  "no_speech_prob": 0.002649236237630248}, {"id": 21, "seek": 13140, "start": 136.56,
  "end": 145.48000000000002, "text": " ability of closing the semantic gaps with light
  queries and documents with some", "tokens": [50622, 3485, 295, 10377, 264, 47982,
  15031, 365, 1442, 24109, 293, 8512, 365, 512, 51068], "temperature": 0.0, "avg_logprob":
  -0.3414122263590495, "compression_ratio": 1.6703296703296704, "no_speech_prob":
  0.002649236237630248}, {"id": 22, "seek": 13140, "start": 145.48000000000002, "end":
  150.6, "text": " some limitations right? So the explainability bar for example is
  an aspect I", "tokens": [51068, 512, 15705, 558, 30, 407, 264, 2903, 2310, 2159,
  337, 1365, 307, 364, 4171, 286, 51324], "temperature": 0.0, "avg_logprob": -0.3414122263590495,
  "compression_ratio": 1.6703296703296704, "no_speech_prob": 0.002649236237630248},
  {"id": 23, "seek": 13140, "start": 150.6, "end": 156.84, "text": " care a lot and
  it''s just very difficult to explain vector based search", "tokens": [51324, 1127,
  257, 688, 293, 309, 311, 445, 588, 2252, 281, 2903, 8062, 2361, 3164, 51636], "temperature":
  0.0, "avg_logprob": -0.3414122263590495, "compression_ratio": 1.6703296703296704,
  "no_speech_prob": 0.002649236237630248}, {"id": 24, "seek": 15684, "start": 156.84,
  "end": 161.96, "text": " results. Yeah, we have I dimensional. So many many dimensions
  in the", "tokens": [50364, 3542, 13, 865, 11, 321, 362, 286, 18795, 13, 407, 867,
  867, 12819, 294, 264, 50620], "temperature": 0.0, "avg_logprob": -0.30894758534985917,
  "compression_ratio": 1.8226600985221675, "no_speech_prob": 0.011387085542082787},
  {"id": 25, "seek": 15684, "start": 161.96, "end": 166.92000000000002, "text": "
  vectors and humans are not really good in managing many dimensions. We live in",
  "tokens": [50620, 18875, 293, 6255, 366, 406, 534, 665, 294, 11642, 867, 12819,
  13, 492, 1621, 294, 50868], "temperature": 0.0, "avg_logprob": -0.30894758534985917,
  "compression_ratio": 1.8226600985221675, "no_speech_prob": 0.011387085542082787},
  {"id": 26, "seek": 15684, "start": 166.92000000000002, "end": 172.12, "text": "
  a three dimensional world and this even difficult for us to to understand", "tokens":
  [50868, 257, 1045, 18795, 1002, 293, 341, 754, 2252, 337, 505, 281, 281, 1223, 51128],
  "temperature": 0.0, "avg_logprob": -0.30894758534985917, "compression_ratio": 1.8226600985221675,
  "no_speech_prob": 0.011387085542082787}, {"id": 27, "seek": 15684, "start": 172.12,
  "end": 181.0, "text": " life for dimensional life. Yeah, then we have like many
  elements in those", "tokens": [51128, 993, 337, 18795, 993, 13, 865, 11, 550, 321,
  362, 411, 867, 4959, 294, 729, 51572], "temperature": 0.0, "avg_logprob": -0.30894758534985917,
  "compression_ratio": 1.8226600985221675, "no_speech_prob": 0.011387085542082787},
  {"id": 28, "seek": 15684, "start": 181.0, "end": 186.44, "text": " vectors. So each
  feature in the vector doesn''t have like a meaning for the", "tokens": [51572, 18875,
  13, 407, 1184, 4111, 294, 264, 8062, 1177, 380, 362, 411, 257, 3620, 337, 264, 51844],
  "temperature": 0.0, "avg_logprob": -0.30894758534985917, "compression_ratio": 1.8226600985221675,
  "no_speech_prob": 0.011387085542082787}, {"id": 29, "seek": 18644, "start": 186.44,
  "end": 193.8, "text": " humans. So you have like 768 dimensions in your vectors
  and there''s no single", "tokens": [50364, 6255, 13, 407, 291, 362, 411, 24733,
  23, 12819, 294, 428, 18875, 293, 456, 311, 572, 2167, 50732], "temperature": 0.0,
  "avg_logprob": -0.2223291189774223, "compression_ratio": 1.6812227074235808, "no_speech_prob":
  0.0009225498070009053}, {"id": 30, "seek": 18644, "start": 193.8, "end": 198.35999999999999,
  "text": " dimension that means something semantic. So it''s just the output of some",
  "tokens": [50732, 10139, 300, 1355, 746, 47982, 13, 407, 309, 311, 445, 264, 5598,
  295, 512, 50960], "temperature": 0.0, "avg_logprob": -0.2223291189774223, "compression_ratio":
  1.6812227074235808, "no_speech_prob": 0.0009225498070009053}, {"id": 31, "seek":
  18644, "start": 198.35999999999999, "end": 204.36, "text": " machiner model but
  we can interpret like what it is. And we can interpret what", "tokens": [50960,
  2246, 4564, 2316, 457, 321, 393, 7302, 411, 437, 309, 307, 13, 400, 321, 393, 7302,
  437, 51260], "temperature": 0.0, "avg_logprob": -0.2223291189774223, "compression_ratio":
  1.6812227074235808, "no_speech_prob": 0.0009225498070009053}, {"id": 32, "seek":
  18644, "start": 204.36, "end": 210.6, "text": " would happen if that feature goes
  higher or lower. I mean does a higher value for", "tokens": [51260, 576, 1051, 498,
  300, 4111, 1709, 2946, 420, 3126, 13, 286, 914, 775, 257, 2946, 2158, 337, 51572],
  "temperature": 0.0, "avg_logprob": -0.2223291189774223, "compression_ratio": 1.6812227074235808,
  "no_speech_prob": 0.0009225498070009053}, {"id": 33, "seek": 18644, "start": 210.6,
  "end": 215.64, "text": " that feature means higher relevance or not? You can''t
  really do that with", "tokens": [51572, 300, 4111, 1355, 2946, 32684, 420, 406,
  30, 509, 393, 380, 534, 360, 300, 365, 51824], "temperature": 0.0, "avg_logprob":
  -0.2223291189774223, "compression_ratio": 1.6812227074235808, "no_speech_prob":
  0.0009225498070009053}, {"id": 34, "seek": 21564, "start": 215.64, "end": 223.16,
  "text": " vector based search. So these kind of problems. Yeah, start to have like
  an", "tokens": [50364, 8062, 2361, 3164, 13, 407, 613, 733, 295, 2740, 13, 865,
  11, 722, 281, 362, 411, 364, 50740], "temperature": 0.0, "avg_logprob": -0.3771527189957468,
  "compression_ratio": 1.6073298429319371, "no_speech_prob": 0.001931108650751412},
  {"id": 35, "seek": 21564, "start": 223.16, "end": 227.79999999999998, "text": "
  input. Right. So you have like your clients using vector based search. They are",
  "tokens": [50740, 4846, 13, 1779, 13, 407, 291, 362, 411, 428, 6982, 1228, 8062,
  2361, 3164, 13, 814, 366, 50972], "temperature": 0.0, "avg_logprob": -0.3771527189957468,
  "compression_ratio": 1.6073298429319371, "no_speech_prob": 0.001931108650751412},
  {"id": 36, "seek": 21564, "start": 227.79999999999998, "end": 234.92, "text": "
  happy and then they are not and they want to explain for example, yeah, what happens.",
  "tokens": [50972, 2055, 293, 550, 436, 366, 406, 293, 436, 528, 281, 2903, 337,
  1365, 11, 1338, 11, 437, 2314, 13, 51328], "temperature": 0.0, "avg_logprob": -0.3771527189957468,
  "compression_ratio": 1.6073298429319371, "no_speech_prob": 0.001931108650751412},
  {"id": 37, "seek": 21564, "start": 234.92, "end": 242.83999999999997, "text": "
  Yeah, and another limitation is keyword based matching. So by the", "tokens": [51328,
  865, 11, 293, 1071, 27432, 307, 20428, 2361, 14324, 13, 407, 538, 264, 51724], "temperature":
  0.0, "avg_logprob": -0.3771527189957468, "compression_ratio": 1.6073298429319371,
  "no_speech_prob": 0.001931108650751412}, {"id": 38, "seek": 24284, "start": 243.8,
  "end": 249.16, "text": " vector based search try to solve the vocabulary in his
  best problem. So if you have terms in", "tokens": [50412, 8062, 2361, 3164, 853,
  281, 5039, 264, 19864, 294, 702, 1151, 1154, 13, 407, 498, 291, 362, 2115, 294,
  50680], "temperature": 0.0, "avg_logprob": -0.2516821637565707, "compression_ratio":
  1.7548076923076923, "no_speech_prob": 0.0053239986300468445}, {"id": 39, "seek":
  24284, "start": 249.16, "end": 255.8, "text": " your vocabulary that''s different
  from the vocabulary used for queries. Yeah. At the same time,", "tokens": [50680,
  428, 19864, 300, 311, 819, 490, 264, 19864, 1143, 337, 24109, 13, 865, 13, 1711,
  264, 912, 565, 11, 51012], "temperature": 0.0, "avg_logprob": -0.2516821637565707,
  "compression_ratio": 1.7548076923076923, "no_speech_prob": 0.0053239986300468445},
  {"id": 40, "seek": 24284, "start": 255.8, "end": 263.16, "text": " users are used
  to have keyword matching documents in their response. So when you don''t", "tokens":
  [51012, 5022, 366, 1143, 281, 362, 20428, 14324, 8512, 294, 641, 4134, 13, 407,
  562, 291, 500, 380, 51380], "temperature": 0.0, "avg_logprob": -0.2516821637565707,
  "compression_ratio": 1.7548076923076923, "no_speech_prob": 0.0053239986300468445},
  {"id": 41, "seek": 24284, "start": 263.16, "end": 268.6, "text": " provide keyword
  matching document in their response, they''re going to be like problems and", "tokens":
  [51380, 2893, 20428, 14324, 4166, 294, 641, 4134, 11, 436, 434, 516, 281, 312, 411,
  2740, 293, 51652], "temperature": 0.0, "avg_logprob": -0.2516821637565707, "compression_ratio":
  1.7548076923076923, "no_speech_prob": 0.0053239986300468445}, {"id": 42, "seek":
  26860, "start": 268.6, "end": 273.88, "text": " questions. Yeah. Why do I see this
  now? And why I don''t see for example this title.", "tokens": [50364, 1651, 13,
  865, 13, 1545, 360, 286, 536, 341, 586, 30, 400, 983, 286, 500, 380, 536, 337, 1365,
  341, 4876, 13, 50628], "temperature": 0.0, "avg_logprob": -0.3079527034315952, "compression_ratio":
  1.5863636363636364, "no_speech_prob": 0.003633220912888646}, {"id": 43, "seek":
  26860, "start": 273.88, "end": 280.84000000000003, "text": " Oh yeah. So without
  any search, the idea is to mitigate those problems. So mix up", "tokens": [50628,
  876, 1338, 13, 407, 1553, 604, 3164, 11, 264, 1558, 307, 281, 27336, 729, 2740,
  13, 407, 2890, 493, 50976], "temperature": 0.0, "avg_logprob": -0.3079527034315952,
  "compression_ratio": 1.5863636363636364, "no_speech_prob": 0.003633220912888646},
  {"id": 44, "seek": 26860, "start": 281.48, "end": 287.96000000000004, "text": "
  different query results sets. Potentially like vector based search results and traditional",
  "tokens": [51008, 819, 14581, 3542, 6352, 13, 9145, 3137, 411, 8062, 2361, 3164,
  3542, 293, 5164, 51332], "temperature": 0.0, "avg_logprob": -0.3079527034315952,
  "compression_ratio": 1.5863636363636364, "no_speech_prob": 0.003633220912888646},
  {"id": 45, "seek": 26860, "start": 287.96000000000004, "end": 293.64000000000004,
  "text": " keyword based search results. Yeah. Get back one result set. Yeah. Let''s
  try to combine both", "tokens": [51332, 20428, 2361, 3164, 3542, 13, 865, 13, 3240,
  646, 472, 1874, 992, 13, 865, 13, 961, 311, 853, 281, 10432, 1293, 51616], "temperature":
  0.0, "avg_logprob": -0.3079527034315952, "compression_ratio": 1.5863636363636364,
  "no_speech_prob": 0.003633220912888646}, {"id": 46, "seek": 29364, "start": 293.64,
  "end": 299.88, "text": " words. Interesting. And if we kind of step forward from
  this, let''s say we deployed hybrid search,", "tokens": [50364, 2283, 13, 14711,
  13, 400, 498, 321, 733, 295, 1823, 2128, 490, 341, 11, 718, 311, 584, 321, 17826,
  13051, 3164, 11, 50676], "temperature": 0.0, "avg_logprob": -0.16302698113945094,
  "compression_ratio": 1.5925925925925926, "no_speech_prob": 0.0038669852074235678},
  {"id": 47, "seek": 29364, "start": 301.15999999999997, "end": 309.4, "text": " so
  now it basically takes some similar documents from keyword hits and then another
  one from vector.", "tokens": [50740, 370, 586, 309, 1936, 2516, 512, 2531, 8512,
  490, 20428, 8664, 293, 550, 1071, 472, 490, 8062, 13, 51152], "temperature": 0.0,
  "avg_logprob": -0.16302698113945094, "compression_ratio": 1.5925925925925926, "no_speech_prob":
  0.0038669852074235678}, {"id": 48, "seek": 29364, "start": 310.36, "end": 315.4,
  "text": " You still get those documents that do not have keyword matches, right,
  from the vector space.", "tokens": [51200, 509, 920, 483, 729, 8512, 300, 360, 406,
  362, 20428, 10676, 11, 558, 11, 490, 264, 8062, 1901, 13, 51452], "temperature":
  0.0, "avg_logprob": -0.16302698113945094, "compression_ratio": 1.5925925925925926,
  "no_speech_prob": 0.0038669852074235678}, {"id": 49, "seek": 29364, "start": 316.2,
  "end": 321.56, "text": " Do you know or maybe you have employed some ways of explaining
  to the user why they see them?", "tokens": [51492, 1144, 291, 458, 420, 1310, 291,
  362, 20115, 512, 2098, 295, 13468, 281, 264, 4195, 983, 436, 536, 552, 30, 51760],
  "temperature": 0.0, "avg_logprob": -0.16302698113945094, "compression_ratio": 1.5925925925925926,
  "no_speech_prob": 0.0038669852074235678}, {"id": 50, "seek": 32156, "start": 321.88,
  "end": 329.0, "text": " So that''s an interesting point actually at the discussion
  recently about how can we explain better", "tokens": [50380, 407, 300, 311, 364,
  1880, 935, 767, 412, 264, 5017, 3938, 466, 577, 393, 321, 2903, 1101, 50736], "temperature":
  0.0, "avg_logprob": -0.3099801502530537, "compression_ratio": 1.6256983240223464,
  "no_speech_prob": 0.0008720722398720682}, {"id": 51, "seek": 32156, "start": 329.0,
  "end": 335.4, "text": " by vector based search. So we mentioned already all the
  problems. We''ve explained the what can we do", "tokens": [50736, 538, 8062, 2361,
  3164, 13, 407, 321, 2835, 1217, 439, 264, 2740, 13, 492, 600, 8825, 264, 437, 393,
  321, 360, 51056], "temperature": 0.0, "avg_logprob": -0.3099801502530537, "compression_ratio":
  1.6256983240223464, "no_speech_prob": 0.0008720722398720682}, {"id": 52, "seek":
  32156, "start": 335.4, "end": 342.76, "text": " bet. So there are other approaches
  that just cure dense vector based search such as learned", "tokens": [51056, 778,
  13, 407, 456, 366, 661, 11587, 300, 445, 13698, 18011, 8062, 2361, 3164, 1270, 382,
  3264, 51424], "temperature": 0.0, "avg_logprob": -0.3099801502530537, "compression_ratio":
  1.6256983240223464, "no_speech_prob": 0.0008720722398720682}, {"id": 53, "seek":
  34276, "start": 342.76, "end": 350.68, "text": " sparse retrieval for example, where
  you learn query or document expansion term candidates", "tokens": [50364, 637, 11668,
  19817, 3337, 337, 1365, 11, 689, 291, 1466, 14581, 420, 4166, 11260, 1433, 11255,
  50760], "temperature": 0.0, "avg_logprob": -0.18904660240052237, "compression_ratio":
  1.574468085106383, "no_speech_prob": 0.01907644234597683}, {"id": 54, "seek": 34276,
  "start": 351.56, "end": 359.71999999999997, "text": " based on learned models. So
  based on the probability you will expand your queries with additional terms.", "tokens":
  [50804, 2361, 322, 3264, 5245, 13, 407, 2361, 322, 264, 8482, 291, 486, 5268, 428,
  24109, 365, 4497, 2115, 13, 51212], "temperature": 0.0, "avg_logprob": -0.18904660240052237,
  "compression_ratio": 1.574468085106383, "no_speech_prob": 0.01907644234597683},
  {"id": 55, "seek": 34276, "start": 360.84, "end": 366.44, "text": " So that''s a
  little bit more explainable because at least you get back from the machine learning
  model", "tokens": [51268, 407, 300, 311, 257, 707, 857, 544, 2903, 712, 570, 412,
  1935, 291, 483, 646, 490, 264, 3479, 2539, 2316, 51548], "temperature": 0.0, "avg_logprob":
  -0.18904660240052237, "compression_ratio": 1.574468085106383, "no_speech_prob":
  0.01907644234597683}, {"id": 56, "seek": 36644, "start": 366.52, "end": 373.48,
  "text": " alternative terms for the queries and the document. Yeah. It''s still
  a first layer of explainability.", "tokens": [50368, 8535, 2115, 337, 264, 24109,
  293, 264, 4166, 13, 865, 13, 467, 311, 920, 257, 700, 4583, 295, 2903, 2310, 13,
  50716], "temperature": 0.0, "avg_logprob": -0.3070507049560547, "compression_ratio":
  1.6130434782608696, "no_speech_prob": 0.009303648956120014}, {"id": 57, "seek":
  36644, "start": 373.48, "end": 378.36, "text": " So you have some that''s like additional
  concepts. So it''s easier to understand.", "tokens": [50716, 407, 291, 362, 512,
  300, 311, 411, 4497, 10392, 13, 407, 309, 311, 3571, 281, 1223, 13, 50960], "temperature":
  0.0, "avg_logprob": -0.3070507049560547, "compression_ratio": 1.6130434782608696,
  "no_speech_prob": 0.009303648956120014}, {"id": 58, "seek": 36644, "start": 378.36,
  "end": 384.28, "text": " Still you have the probability assigned to their pair.
  So if it goes wrong, you may end up with", "tokens": [50960, 8291, 291, 362, 264,
  8482, 13279, 281, 641, 6119, 13, 407, 498, 309, 1709, 2085, 11, 291, 815, 917, 493,
  365, 51256], "temperature": 0.0, "avg_logprob": -0.3070507049560547, "compression_ratio":
  1.6130434782608696, "no_speech_prob": 0.009303648956120014}, {"id": 59, "seek":
  36644, "start": 385.08, "end": 390.28, "text": " unreasonable terms. So not perfect.
  A little bit better, maybe a little bit more explainable.", "tokens": [51296, 41730,
  2115, 13, 407, 406, 2176, 13, 316, 707, 857, 1101, 11, 1310, 257, 707, 857, 544,
  2903, 712, 13, 51556], "temperature": 0.0, "avg_logprob": -0.3070507049560547, "compression_ratio":
  1.6130434782608696, "no_speech_prob": 0.009303648956120014}, {"id": 60, "seek":
  39028, "start": 391.23999999999995, "end": 399.23999999999995, "text": " And then
  there are approaches such callvert where you encode your sentence, not just to just
  one", "tokens": [50412, 400, 550, 456, 366, 11587, 1270, 818, 3281, 689, 291, 2058,
  1429, 428, 8174, 11, 406, 445, 281, 445, 472, 50812], "temperature": 0.0, "avg_logprob":
  -0.35245581234202666, "compression_ratio": 1.6054054054054054, "no_speech_prob":
  0.015376309864223003}, {"id": 61, "seek": 39028, "start": 399.23999999999995, "end":
  405.55999999999995, "text": " vector back to a sequence of vectors. So multiple
  vectors, one pair for an action. And you do the same", "tokens": [50812, 8062, 646,
  281, 257, 8310, 295, 18875, 13, 407, 3866, 18875, 11, 472, 6119, 337, 364, 3069,
  13, 400, 291, 360, 264, 912, 51128], "temperature": 0.0, "avg_logprob": -0.35245581234202666,
  "compression_ratio": 1.6054054054054054, "no_speech_prob": 0.015376309864223003},
  {"id": 62, "seek": 39028, "start": 405.55999999999995, "end": 413.88, "text": "
  for your documents. And then you you basically return results based on the similarity
  between not", "tokens": [51128, 337, 428, 8512, 13, 400, 550, 291, 291, 1936, 2736,
  3542, 2361, 322, 264, 32194, 1296, 406, 51544], "temperature": 0.0, "avg_logprob":
  -0.35245581234202666, "compression_ratio": 1.6054054054054054, "no_speech_prob":
  0.015376309864223003}, {"id": 63, "seek": 41388, "start": 413.88, "end": 419.64,
  "text": " just a single query vector and the document vector, but multiple query
  vectors. So each query", "tokens": [50364, 445, 257, 2167, 14581, 8062, 293, 264,
  4166, 8062, 11, 457, 3866, 14581, 18875, 13, 407, 1184, 14581, 50652], "temperature":
  0.0, "avg_logprob": -0.20008046139952956, "compression_ratio": 1.8413461538461537,
  "no_speech_prob": 0.003499676939100027}, {"id": 64, "seek": 41388, "start": 419.64,
  "end": 425.48, "text": " at each query vector, which is meant to be probably a term
  with the terms in the document. So you", "tokens": [50652, 412, 1184, 14581, 8062,
  11, 597, 307, 4140, 281, 312, 1391, 257, 1433, 365, 264, 2115, 294, 264, 4166, 13,
  407, 291, 50944], "temperature": 0.0, "avg_logprob": -0.20008046139952956, "compression_ratio":
  1.8413461538461537, "no_speech_prob": 0.003499676939100027}, {"id": 65, "seek":
  41388, "start": 425.48, "end": 431.48, "text": " may be able to highlight the terms
  in the document that are close to the terms in the query. Yeah.", "tokens": [50944,
  815, 312, 1075, 281, 5078, 264, 2115, 294, 264, 4166, 300, 366, 1998, 281, 264,
  2115, 294, 264, 14581, 13, 865, 13, 51244], "temperature": 0.0, "avg_logprob": -0.20008046139952956,
  "compression_ratio": 1.8413461538461537, "no_speech_prob": 0.003499676939100027},
  {"id": 66, "seek": 41388, "start": 432.2, "end": 436.52, "text": " Also in this
  case, of course, it''s just a first layer of explainability because then if this",
  "tokens": [51280, 2743, 294, 341, 1389, 11, 295, 1164, 11, 309, 311, 445, 257, 700,
  4583, 295, 2903, 2310, 570, 550, 498, 341, 51496], "temperature": 0.0, "avg_logprob":
  -0.20008046139952956, "compression_ratio": 1.8413461538461537, "no_speech_prob":
  0.003499676939100027}, {"id": 67, "seek": 43652, "start": 436.52, "end": 442.03999999999996,
  "text": " goes wrong, of course, again, you have sequences of vectors. So you can
  get like a sort of", "tokens": [50364, 1709, 2085, 11, 295, 1164, 11, 797, 11, 291,
  362, 22978, 295, 18875, 13, 407, 291, 393, 483, 411, 257, 1333, 295, 50640], "temperature":
  0.0, "avg_logprob": -0.24840266579075865, "compression_ratio": 1.5646551724137931,
  "no_speech_prob": 0.002190630417317152}, {"id": 68, "seek": 43652, "start": 443.79999999999995,
  "end": 452.44, "text": " itm up of what query terms match is like, more or less
  the document ones, but still not perfect.", "tokens": [50728, 309, 76, 493, 295,
  437, 14581, 2115, 2995, 307, 411, 11, 544, 420, 1570, 264, 4166, 2306, 11, 457,
  920, 406, 2176, 13, 51160], "temperature": 0.0, "avg_logprob": -0.24840266579075865,
  "compression_ratio": 1.5646551724137931, "no_speech_prob": 0.002190630417317152},
  {"id": 69, "seek": 43652, "start": 452.44, "end": 456.44, "text": " Yeah, sure.
  Of course, it''s kind of like maybe experimentation that is required,", "tokens":
  [51160, 865, 11, 988, 13, 2720, 1164, 11, 309, 311, 733, 295, 411, 1310, 37142,
  300, 307, 4739, 11, 51360], "temperature": 0.0, "avg_logprob": -0.24840266579075865,
  "compression_ratio": 1.5646551724137931, "no_speech_prob": 0.002190630417317152},
  {"id": 70, "seek": 43652, "start": 456.44, "end": 463.56, "text": " right? What
  works for you? What what what is the end product? But maybe one question is for
  me", "tokens": [51360, 558, 30, 708, 1985, 337, 291, 30, 708, 437, 437, 307, 264,
  917, 1674, 30, 583, 1310, 472, 1168, 307, 337, 385, 51716], "temperature": 0.0,
  "avg_logprob": -0.24840266579075865, "compression_ratio": 1.5646551724137931, "no_speech_prob":
  0.002190630417317152}, {"id": 71, "seek": 46356, "start": 463.56, "end": 469.56,
  "text": " as a user, right? Let''s say I''m using solar and you offer hybrid search
  now. Are you already", "tokens": [50364, 382, 257, 4195, 11, 558, 30, 961, 311,
  584, 286, 478, 1228, 7936, 293, 291, 2626, 13051, 3164, 586, 13, 2014, 291, 1217,
  50664], "temperature": 0.0, "avg_logprob": -0.14990426018124536, "compression_ratio":
  1.6464285714285714, "no_speech_prob": 0.004965724423527718}, {"id": 72, "seek":
  46356, "start": 469.56, "end": 476.6, "text": " offering or will you consider at
  some point offering the capability to ingrain what you just said", "tokens": [50664,
  8745, 420, 486, 291, 1949, 412, 512, 935, 8745, 264, 13759, 281, 3957, 7146, 437,
  291, 445, 848, 51016], "temperature": 0.0, "avg_logprob": -0.14990426018124536,
  "compression_ratio": 1.6464285714285714, "no_speech_prob": 0.004965724423527718},
  {"id": 73, "seek": 46356, "start": 476.6, "end": 481.08, "text": " into let''s say
  highlighter in solar that will it will actually build me the snippet", "tokens":
  [51016, 666, 718, 311, 584, 40455, 294, 7936, 300, 486, 309, 486, 767, 1322, 385,
  264, 35623, 302, 51240], "temperature": 0.0, "avg_logprob": -0.14990426018124536,
  "compression_ratio": 1.6464285714285714, "no_speech_prob": 0.004965724423527718},
  {"id": 74, "seek": 46356, "start": 481.8, "end": 486.2, "text": " regardless of
  the source of that document, whether it''s keyboard or vector. That''s a very",
  "tokens": [51276, 10060, 295, 264, 4009, 295, 300, 4166, 11, 1968, 309, 311, 10186,
  420, 8062, 13, 663, 311, 257, 588, 51496], "temperature": 0.0, "avg_logprob": -0.14990426018124536,
  "compression_ratio": 1.6464285714285714, "no_speech_prob": 0.004965724423527718},
  {"id": 75, "seek": 46356, "start": 486.2, "end": 491.8, "text": " interesting question
  because there are in my opinion two layers of explainability for engineers.", "tokens":
  [51496, 1880, 1168, 570, 456, 366, 294, 452, 4800, 732, 7914, 295, 2903, 2310, 337,
  11955, 13, 51776], "temperature": 0.0, "avg_logprob": -0.14990426018124536, "compression_ratio":
  1.6464285714285714, "no_speech_prob": 0.004965724423527718}, {"id": 76, "seek":
  49180, "start": 492.04, "end": 496.2, "text": " So we need to work on the engine
  and change the ranking, change the matching", "tokens": [50376, 407, 321, 643, 281,
  589, 322, 264, 2848, 293, 1319, 264, 17833, 11, 1319, 264, 14324, 50584], "temperature":
  0.0, "avg_logprob": -0.4303919954119988, "compression_ratio": 1.6653846153846155,
  "no_speech_prob": 0.005520969163626432}, {"id": 77, "seek": 49180, "start": 497.8,
  "end": 501.8, "text": " and user''s equipment. Yeah. So a user that just want to
  know why for example,", "tokens": [50664, 293, 4195, 311, 5927, 13, 865, 13, 407,
  257, 4195, 300, 445, 528, 281, 458, 983, 337, 1365, 11, 50864], "temperature": 0.0,
  "avg_logprob": -0.4303919954119988, "compression_ratio": 1.6653846153846155, "no_speech_prob":
  0.005520969163626432}, {"id": 78, "seek": 49180, "start": 501.8, "end": 507.08000000000004,
  "text": " what is there and for user''s finability actually, my company, we design
  and develop the", "tokens": [50864, 437, 307, 456, 293, 337, 4195, 311, 962, 2310,
  767, 11, 452, 2237, 11, 321, 1715, 293, 1499, 264, 51128], "temperature": 0.0, "avg_logprob":
  -0.4303919954119988, "compression_ratio": 1.6653846153846155, "no_speech_prob":
  0.005520969163626432}, {"id": 79, "seek": 49180, "start": 507.08000000000004, "end":
  513.8, "text": " highlighter. We call the neural highlighter that takes in input
  the wireless model and in the response,", "tokens": [51128, 40455, 13, 492, 818,
  264, 18161, 40455, 300, 2516, 294, 4846, 264, 14720, 2316, 293, 294, 264, 4134,
  11, 51464], "temperature": 0.0, "avg_logprob": -0.4303919954119988, "compression_ratio":
  1.6653846153846155, "no_speech_prob": 0.005520969163626432}, {"id": 80, "seek":
  49180, "start": 513.8, "end": 519.0, "text": " will I like the snippet for each
  result in documents, not based on let''s say on match,", "tokens": [51464, 486,
  286, 411, 264, 35623, 302, 337, 1184, 1874, 294, 8512, 11, 406, 2361, 322, 718,
  311, 584, 322, 2995, 11, 51724], "temperature": 0.0, "avg_logprob": -0.4303919954119988,
  "compression_ratio": 1.6653846153846155, "no_speech_prob": 0.005520969163626432},
  {"id": 81, "seek": 51900, "start": 519.0, "end": 524.2, "text": " but based on the
  question as a system powered by a level model. Yeah. So in this way,", "tokens":
  [50364, 457, 2361, 322, 264, 1168, 382, 257, 1185, 17786, 538, 257, 1496, 2316,
  13, 865, 13, 407, 294, 341, 636, 11, 50624], "temperature": 0.0, "avg_logprob":
  -0.3864540713174002, "compression_ratio": 1.6692307692307693, "no_speech_prob":
  0.0030129007063806057}, {"id": 82, "seek": 51900, "start": 524.2, "end": 529.16,
  "text": " you will be able to highlight part of the original document that are semantically
  close to the", "tokens": [50624, 291, 486, 312, 1075, 281, 5078, 644, 295, 264,
  3380, 4166, 300, 366, 4361, 49505, 1998, 281, 264, 50872], "temperature": 0.0, "avg_logprob":
  -0.3864540713174002, "compression_ratio": 1.6692307692307693, "no_speech_prob":
  0.0030129007063806057}, {"id": 83, "seek": 51900, "start": 529.16, "end": 532.36,
  "text": " interesting place. Can you say the name again? What was the name? It''s
  called the neural", "tokens": [50872, 1880, 1081, 13, 1664, 291, 584, 264, 1315,
  797, 30, 708, 390, 264, 1315, 30, 467, 311, 1219, 264, 18161, 51032], "temperature":
  0.0, "avg_logprob": -0.3864540713174002, "compression_ratio": 1.6692307692307693,
  "no_speech_prob": 0.0030129007063806057}, {"id": 84, "seek": 51900, "start": 532.36,
  "end": 537.0, "text": " highlighter. Neural neural highlighter. So it''s your proprietary
  product right now. Yes.", "tokens": [51032, 40455, 13, 1734, 1807, 18161, 40455,
  13, 407, 309, 311, 428, 38992, 1674, 558, 586, 13, 1079, 13, 51264], "temperature":
  0.0, "avg_logprob": -0.3864540713174002, "compression_ratio": 1.6692307692307693,
  "no_speech_prob": 0.0030129007063806057}, {"id": 85, "seek": 51900, "start": 537.0,
  "end": 542.04, "text": " It''s a lot of synths, right? Yes. Right now, yes. We may
  contribute it to a", "tokens": [51264, 467, 311, 257, 688, 295, 10657, 82, 11, 558,
  30, 1079, 13, 1779, 586, 11, 2086, 13, 492, 815, 10586, 309, 281, 257, 51516], "temperature":
  0.0, "avg_logprob": -0.3864540713174002, "compression_ratio": 1.6692307692307693,
  "no_speech_prob": 0.0030129007063806057}, {"id": 86, "seek": 54204, "start": 542.04,
  "end": 547.3199999999999, "text": " open source integer. I don''t know. Right now
  is one of our products. But I mean,", "tokens": [50364, 1269, 4009, 24922, 13, 286,
  500, 380, 458, 13, 1779, 586, 307, 472, 295, 527, 3383, 13, 583, 286, 914, 11, 50628],
  "temperature": 0.0, "avg_logprob": -0.38971791501905095, "compression_ratio": 1.6772908366533865,
  "no_speech_prob": 0.031038612127304077}, {"id": 87, "seek": 54204, "start": 547.3199999999999,
  "end": 552.12, "text": " it''s a feature that you, is it offered as a standalone
  component? It''s a plugin.", "tokens": [50628, 309, 311, 257, 4111, 300, 291, 11,
  307, 309, 8059, 382, 257, 37454, 6542, 30, 467, 311, 257, 23407, 13, 50868], "temperature":
  0.0, "avg_logprob": -0.38971791501905095, "compression_ratio": 1.6772908366533865,
  "no_speech_prob": 0.031038612127304077}, {"id": 88, "seek": 54204, "start": 552.12,
  "end": 556.1999999999999, "text": " It''s a plugin. So you ins it''s a plugin to
  pull it. It''s a plugin. That''s the value", "tokens": [50868, 467, 311, 257, 23407,
  13, 407, 291, 1028, 309, 311, 257, 23407, 281, 2235, 309, 13, 467, 311, 257, 23407,
  13, 663, 311, 264, 2158, 51072], "temperature": 0.0, "avg_logprob": -0.38971791501905095,
  "compression_ratio": 1.6772908366533865, "no_speech_prob": 0.031038612127304077},
  {"id": 89, "seek": 54204, "start": 556.1999999999999, "end": 561.16, "text": " prop
  as well, right? It doesn''t always need to be open. It''s something I can plug in
  and", "tokens": [51072, 2365, 382, 731, 11, 558, 30, 467, 1177, 380, 1009, 643,
  281, 312, 1269, 13, 467, 311, 746, 286, 393, 5452, 294, 293, 51320], "temperature":
  0.0, "avg_logprob": -0.38971791501905095, "compression_ratio": 1.6772908366533865,
  "no_speech_prob": 0.031038612127304077}, {"id": 90, "seek": 54204, "start": 561.7199999999999,
  "end": 566.28, "text": " exactly. It takes in input the wireless model. Yeah. It''s
  a response point. So you can", "tokens": [51348, 2293, 13, 467, 2516, 294, 4846,
  264, 14720, 2316, 13, 865, 13, 467, 311, 257, 4134, 935, 13, 407, 291, 393, 51576],
  "temperature": 0.0, "avg_logprob": -0.38971791501905095, "compression_ratio": 1.6772908366533865,
  "no_speech_prob": 0.031038612127304077}, {"id": 91, "seek": 56628, "start": 567.0,
  "end": 572.68, "text": " write. So that will help to explain results to the users,
  right? And you also mentioned,", "tokens": [50400, 2464, 13, 407, 300, 486, 854,
  281, 2903, 3542, 281, 264, 5022, 11, 558, 30, 400, 291, 611, 2835, 11, 50684], "temperature":
  0.0, "avg_logprob": -0.2052457250397781, "compression_ratio": 1.841897233201581,
  "no_speech_prob": 0.014821712858974934}, {"id": 92, "seek": 56628, "start": 572.68,
  "end": 576.76, "text": " right? It''s thanks for doing this distinction, making
  this distinction that there is also", "tokens": [50684, 558, 30, 467, 311, 3231,
  337, 884, 341, 16844, 11, 1455, 341, 16844, 300, 456, 307, 611, 50888], "temperature":
  0.0, "avg_logprob": -0.2052457250397781, "compression_ratio": 1.841897233201581,
  "no_speech_prob": 0.014821712858974934}, {"id": 93, "seek": 56628, "start": 576.76,
  "end": 582.04, "text": " explainability for the engineers that is also important.
  So can you a bit explain what you mean?", "tokens": [50888, 2903, 2310, 337, 264,
  11955, 300, 307, 611, 1021, 13, 407, 393, 291, 257, 857, 2903, 437, 291, 914, 30,
  51152], "temperature": 0.0, "avg_logprob": -0.2052457250397781, "compression_ratio":
  1.841897233201581, "no_speech_prob": 0.014821712858974934}, {"id": 94, "seek": 56628,
  "start": 582.04, "end": 586.92, "text": " Explainability for the engineers because
  I care about it a lot of force. But I used to be an", "tokens": [51152, 39574, 2310,
  337, 264, 11955, 570, 286, 1127, 466, 309, 257, 688, 295, 3464, 13, 583, 286, 1143,
  281, 312, 364, 51396], "temperature": 0.0, "avg_logprob": -0.2052457250397781, "compression_ratio":
  1.841897233201581, "no_speech_prob": 0.014821712858974934}, {"id": 95, "seek": 56628,
  "start": 586.92, "end": 593.3199999999999, "text": " engineer full time. And I need
  to know how, like, how to do it, how to tweak something. But also,", "tokens": [51396,
  11403, 1577, 565, 13, 400, 286, 643, 281, 458, 577, 11, 411, 11, 577, 281, 360,
  309, 11, 577, 281, 29879, 746, 13, 583, 611, 11, 51716], "temperature": 0.0, "avg_logprob":
  -0.2052457250397781, "compression_ratio": 1.841897233201581, "no_speech_prob": 0.014821712858974934},
  {"id": 96, "seek": 59332, "start": 593.32, "end": 597.6400000000001, "text": " can
  I explain to myself that what I tweaked is actually the right thing, right? So,",
  "tokens": [50364, 393, 286, 2903, 281, 2059, 300, 437, 286, 6986, 7301, 307, 767,
  264, 558, 551, 11, 558, 30, 407, 11, 50580], "temperature": 0.0, "avg_logprob":
  -0.17626971988887577, "compression_ratio": 1.6383928571428572, "no_speech_prob":
  0.0027192109264433384}, {"id": 97, "seek": 59332, "start": 597.6400000000001, "end":
  603.5600000000001, "text": " you know, kind of the process of engineering the. Yes.
  So in solar, for example, there is a debug", "tokens": [50580, 291, 458, 11, 733,
  295, 264, 1399, 295, 7043, 264, 13, 1079, 13, 407, 294, 7936, 11, 337, 1365, 11,
  456, 307, 257, 24083, 50876], "temperature": 0.0, "avg_logprob": -0.17626971988887577,
  "compression_ratio": 1.6383928571428572, "no_speech_prob": 0.0027192109264433384},
  {"id": 98, "seek": 59332, "start": 603.5600000000001, "end": 611.5600000000001,
  "text": " component that give you the ability to engineer to expand the response
  with the information about", "tokens": [50876, 6542, 300, 976, 291, 264, 3485, 281,
  11403, 281, 5268, 264, 4134, 365, 264, 1589, 466, 51276], "temperature": 0.0, "avg_logprob":
  -0.17626971988887577, "compression_ratio": 1.6383928571428572, "no_speech_prob":
  0.0027192109264433384}, {"id": 99, "seek": 59332, "start": 611.5600000000001, "end":
  617.1600000000001, "text": " how the score was calculated. So in solar, when you
  have a query and you have a result,", "tokens": [51276, 577, 264, 6175, 390, 15598,
  13, 407, 294, 7936, 11, 562, 291, 362, 257, 14581, 293, 291, 362, 257, 1874, 11,
  51556], "temperature": 0.0, "avg_logprob": -0.17626971988887577, "compression_ratio":
  1.6383928571428572, "no_speech_prob": 0.0027192109264433384}, {"id": 100, "seek":
  61716, "start": 617.16, "end": 623.0, "text": " a score is calculated for that result
  for that query. And this core will impact the ranking.", "tokens": [50364, 257,
  6175, 307, 15598, 337, 300, 1874, 337, 300, 14581, 13, 400, 341, 4965, 486, 2712,
  264, 17833, 13, 50656], "temperature": 0.0, "avg_logprob": -0.26591312885284424,
  "compression_ratio": 1.7033492822966507, "no_speech_prob": 0.011101032607257366},
  {"id": 101, "seek": 61716, "start": 623.0, "end": 630.36, "text": " So, descending
  order, literally, right from the highest core to the lowest. And normally,", "tokens":
  [50656, 407, 11, 40182, 1668, 11, 3736, 11, 558, 490, 264, 6343, 4965, 281, 264,
  12437, 13, 400, 5646, 11, 51024], "temperature": 0.0, "avg_logprob": -0.26591312885284424,
  "compression_ratio": 1.7033492822966507, "no_speech_prob": 0.011101032607257366},
  {"id": 102, "seek": 61716, "start": 630.36, "end": 637.56, "text": " this core is
  explained showing why you get that mathematical calculations from the term", "tokens":
  [51024, 341, 4965, 307, 8825, 4099, 983, 291, 483, 300, 18894, 20448, 490, 264,
  1433, 51384], "temperature": 0.0, "avg_logprob": -0.26591312885284424, "compression_ratio":
  1.7033492822966507, "no_speech_prob": 0.011101032607257366}, {"id": 103, "seek":
  61716, "start": 637.56, "end": 643.48, "text": " frequencies. Yeah. The length of
  the document field, the average length of the field,", "tokens": [51384, 20250,
  13, 865, 13, 440, 4641, 295, 264, 4166, 2519, 11, 264, 4274, 4641, 295, 264, 2519,
  11, 51680], "temperature": 0.0, "avg_logprob": -0.26591312885284424, "compression_ratio":
  1.7033492822966507, "no_speech_prob": 0.011101032607257366}, {"id": 104, "seek":
  64348, "start": 643.48, "end": 649.08, "text": " the document, frequency, hour,
  error, a term was, for example, and so on and so forth.", "tokens": [50364, 264,
  4166, 11, 7893, 11, 1773, 11, 6713, 11, 257, 1433, 390, 11, 337, 1365, 11, 293,
  370, 322, 293, 370, 5220, 13, 50644], "temperature": 0.0, "avg_logprob": -0.3125187590882018,
  "compression_ratio": 1.6017316017316017, "no_speech_prob": 0.007342732511460781},
  {"id": 105, "seek": 64348, "start": 649.08, "end": 654.44, "text": " So long mathematical
  expression that are readable to the user and you can understand, okay,", "tokens":
  [50644, 407, 938, 18894, 6114, 300, 366, 49857, 281, 264, 4195, 293, 291, 393, 1223,
  11, 1392, 11, 50912], "temperature": 0.0, "avg_logprob": -0.3125187590882018, "compression_ratio":
  1.6017316017316017, "no_speech_prob": 0.007342732511460781}, {"id": 106, "seek":
  64348, "start": 654.44, "end": 660.52, "text": " I was aiming for this field to
  impact the score. Let''s see, let''s see, really impact the score.", "tokens": [50912,
  286, 390, 20253, 337, 341, 2519, 281, 2712, 264, 6175, 13, 961, 311, 536, 11, 718,
  311, 536, 11, 534, 2712, 264, 6175, 13, 51216], "temperature": 0.0, "avg_logprob":
  -0.3125187590882018, "compression_ratio": 1.6017316017316017, "no_speech_prob":
  0.007342732511460781}, {"id": 107, "seek": 64348, "start": 662.12, "end": 667.32,
  "text": " With better research right now, the only explanation that you get from
  an engineer perspective,", "tokens": [51296, 2022, 1101, 2132, 558, 586, 11, 264,
  787, 10835, 300, 291, 483, 490, 364, 11403, 4585, 11, 51556], "temperature": 0.0,
  "avg_logprob": -0.3125187590882018, "compression_ratio": 1.6017316017316017, "no_speech_prob":
  0.007342732511460781}, {"id": 108, "seek": 66732, "start": 667.32, "end": 674.84,
  "text": " literally is within the top K. So this document was within a top K with
  a cosine similarity between", "tokens": [50364, 3736, 307, 1951, 264, 1192, 591,
  13, 407, 341, 4166, 390, 1951, 257, 1192, 591, 365, 257, 23565, 32194, 1296, 50740],
  "temperature": 0.0, "avg_logprob": -0.23210259701343292, "compression_ratio": 1.6594827586206897,
  "no_speech_prob": 0.010490495711565018}, {"id": 109, "seek": 66732, "start": 674.84,
  "end": 680.2, "text": " the query vector and the document vector. That''s not really
  helpful. It''s just confirming what''s", "tokens": [50740, 264, 14581, 8062, 293,
  264, 4166, 8062, 13, 663, 311, 406, 534, 4961, 13, 467, 311, 445, 42861, 437, 311,
  51008], "temperature": 0.0, "avg_logprob": -0.23210259701343292, "compression_ratio":
  1.6594827586206897, "no_speech_prob": 0.010490495711565018}, {"id": 110, "seek":
  66732, "start": 680.2, "end": 685.48, "text": " you know already, right? I mean,
  yeah, it''s in the top K, it was written. So one of the ideas I was", "tokens":
  [51008, 291, 458, 1217, 11, 558, 30, 286, 914, 11, 1338, 11, 309, 311, 294, 264,
  1192, 591, 11, 309, 390, 3720, 13, 407, 472, 295, 264, 3487, 286, 390, 51272], "temperature":
  0.0, "avg_logprob": -0.23210259701343292, "compression_ratio": 1.6594827586206897,
  "no_speech_prob": 0.010490495711565018}, {"id": 111, "seek": 66732, "start": 685.48,
  "end": 691.48, "text": " thinking of, because actually quite far from the implementation
  is to explain the reason", "tokens": [51272, 1953, 295, 11, 570, 767, 1596, 1400,
  490, 264, 11420, 307, 281, 2903, 264, 1778, 51572], "temperature": 0.0, "avg_logprob":
  -0.23210259701343292, "compression_ratio": 1.6594827586206897, "no_speech_prob":
  0.010490495711565018}, {"id": 112, "seek": 69148, "start": 691.64, "end": 700.76,
  "text": " document in the results set, showing examples of, so the language models
  used to return embedded,", "tokens": [50372, 4166, 294, 264, 3542, 992, 11, 4099,
  5110, 295, 11, 370, 264, 2856, 5245, 1143, 281, 2736, 16741, 11, 50828], "temperature":
  0.0, "avg_logprob": -0.3550327212311501, "compression_ratio": 1.7990867579908676,
  "no_speech_prob": 0.0023939379025250673}, {"id": 113, "seek": 69148, "start": 701.4,
  "end": 708.84, "text": " were fine tuned on sentence similarity. So this means there
  were pair of sentences with similar", "tokens": [50860, 645, 2489, 10870, 322, 8174,
  32194, 13, 407, 341, 1355, 456, 645, 6119, 295, 16579, 365, 2531, 51232], "temperature":
  0.0, "avg_logprob": -0.3550327212311501, "compression_ratio": 1.7990867579908676,
  "no_speech_prob": 0.0023939379025250673}, {"id": 114, "seek": 69148, "start": 708.84,
  "end": 714.6, "text": " meaning and pair of sentences with this similar meaning
  in a way that to learn how to encode this", "tokens": [51232, 3620, 293, 6119, 295,
  16579, 365, 341, 2531, 3620, 294, 257, 636, 300, 281, 1466, 577, 281, 2058, 1429,
  341, 51520], "temperature": 0.0, "avg_logprob": -0.3550327212311501, "compression_ratio":
  1.7990867579908676, "no_speech_prob": 0.0023939379025250673}, {"id": 115, "seek":
  69148, "start": 714.6, "end": 721.08, "text": " amount. So I think it could be very
  interesting if to explain the reason a document is being returned.", "tokens": [51520,
  2372, 13, 407, 286, 519, 309, 727, 312, 588, 1880, 498, 281, 2903, 264, 1778, 257,
  4166, 307, 885, 8752, 13, 51844], "temperature": 0.0, "avg_logprob": -0.3550327212311501,
  "compression_ratio": 1.7990867579908676, "no_speech_prob": 0.0023939379025250673},
  {"id": 116, "seek": 72148, "start": 721.72, "end": 729.4, "text": " Because of vector
  cells, you show like a snippet, say, because there are, there is this similar",
  "tokens": [50376, 1436, 295, 8062, 5438, 11, 291, 855, 411, 257, 35623, 302, 11,
  584, 11, 570, 456, 366, 11, 456, 307, 341, 2531, 50760], "temperature": 0.0, "avg_logprob":
  -0.2672163780699385, "compression_ratio": 1.6565217391304348, "no_speech_prob":
  0.002177764428779483}, {"id": 117, "seek": 72148, "start": 729.4, "end": 737.0,
  "text": " pairs of sentences and this is this similar sentence, in the way that
  then potentially the engineer", "tokens": [50760, 15494, 295, 16579, 293, 341, 307,
  341, 2531, 8174, 11, 294, 264, 636, 300, 550, 7263, 264, 11403, 51140], "temperature":
  0.0, "avg_logprob": -0.2672163780699385, "compression_ratio": 1.6565217391304348,
  "no_speech_prob": 0.002177764428779483}, {"id": 118, "seek": 72148, "start": 737.0,
  "end": 741.48, "text": " can go back and realize, okay, let''s take a look to the
  original training data, for example,", "tokens": [51140, 393, 352, 646, 293, 4325,
  11, 1392, 11, 718, 311, 747, 257, 574, 281, 264, 3380, 3097, 1412, 11, 337, 1365,
  11, 51364], "temperature": 0.0, "avg_logprob": -0.2672163780699385, "compression_ratio":
  1.6565217391304348, "no_speech_prob": 0.002177764428779483}, {"id": 119, "seek":
  72148, "start": 742.2, "end": 748.6, "text": " did I cover the example well or maybe
  they are wrong? So I see like, oh, these two sentences", "tokens": [51400, 630,
  286, 2060, 264, 1365, 731, 420, 1310, 436, 366, 2085, 30, 407, 286, 536, 411, 11,
  1954, 11, 613, 732, 16579, 51720], "temperature": 0.0, "avg_logprob": -0.2672163780699385,
  "compression_ratio": 1.6565217391304348, "no_speech_prob": 0.002177764428779483},
  {"id": 120, "seek": 74860, "start": 748.6800000000001, "end": 755.96, "text": "
  are shown as similar, but they are not so. It''s just an idea, you know, study it.",
  "tokens": [50368, 366, 4898, 382, 2531, 11, 457, 436, 366, 406, 370, 13, 467, 311,
  445, 364, 1558, 11, 291, 458, 11, 2979, 309, 13, 50732], "temperature": 0.0, "avg_logprob":
  -0.2456328894502373, "compression_ratio": 1.6801801801801801, "no_speech_prob":
  0.015567686408758163}, {"id": 121, "seek": 74860, "start": 755.96, "end": 761.72,
  "text": " Wow, that''s very interesting, because as you said, it''s very limiting
  today to just know that", "tokens": [50732, 3153, 11, 300, 311, 588, 1880, 11, 570,
  382, 291, 848, 11, 309, 311, 588, 22083, 965, 281, 445, 458, 300, 51020], "temperature":
  0.0, "avg_logprob": -0.2456328894502373, "compression_ratio": 1.6801801801801801,
  "no_speech_prob": 0.015567686408758163}, {"id": 122, "seek": 74860, "start": 761.72,
  "end": 768.28, "text": " geometric search happened and this is the result. Yeah,
  that''s amazing. I mean, it''s really interesting", "tokens": [51020, 33246, 3164,
  2011, 293, 341, 307, 264, 1874, 13, 865, 11, 300, 311, 2243, 13, 286, 914, 11, 309,
  311, 534, 1880, 51348], "temperature": 0.0, "avg_logprob": -0.2456328894502373,
  "compression_ratio": 1.6801801801801801, "no_speech_prob": 0.015567686408758163},
  {"id": 123, "seek": 74860, "start": 768.28, "end": 774.36, "text": " that with this
  work, you are not really just taking something and applying to implementation,",
  "tokens": [51348, 300, 365, 341, 589, 11, 291, 366, 406, 534, 445, 1940, 746, 293,
  9275, 281, 11420, 11, 51652], "temperature": 0.0, "avg_logprob": -0.2456328894502373,
  "compression_ratio": 1.6801801801801801, "no_speech_prob": 0.015567686408758163},
  {"id": 124, "seek": 77436, "start": 774.36, "end": 779.08, "text": " right? Like,
  I mean, implementing a plugin, but you actually go into the space of exploring",
  "tokens": [50364, 558, 30, 1743, 11, 286, 914, 11, 18114, 257, 23407, 11, 457, 291,
  767, 352, 666, 264, 1901, 295, 12736, 50600], "temperature": 0.0, "avg_logprob":
  -0.11868926882743835, "compression_ratio": 1.6239669421487604, "no_speech_prob":
  0.005990014877170324}, {"id": 125, "seek": 77436, "start": 779.08, "end": 784.6,
  "text": " thing because it''s not like everything is done, right? And maybe in some
  companies, it has been done,", "tokens": [50600, 551, 570, 309, 311, 406, 411, 1203,
  307, 1096, 11, 558, 30, 400, 1310, 294, 512, 3431, 11, 309, 575, 668, 1096, 11,
  50876], "temperature": 0.0, "avg_logprob": -0.11868926882743835, "compression_ratio":
  1.6239669421487604, "no_speech_prob": 0.005990014877170324}, {"id": 126, "seek":
  77436, "start": 784.6, "end": 790.76, "text": " but they are not open sourcing,
  right? And so you need to do the search, the search of the solution.", "tokens":
  [50876, 457, 436, 366, 406, 1269, 11006, 2175, 11, 558, 30, 400, 370, 291, 643,
  281, 360, 264, 3164, 11, 264, 3164, 295, 264, 3827, 13, 51184], "temperature": 0.0,
  "avg_logprob": -0.11868926882743835, "compression_ratio": 1.6239669421487604, "no_speech_prob":
  0.005990014877170324}, {"id": 127, "seek": 77436, "start": 790.76, "end": 799.0,
  "text": " That''s very interesting. So in terms of functionality today, hybrid search
  is already available in", "tokens": [51184, 663, 311, 588, 1880, 13, 407, 294, 2115,
  295, 14980, 965, 11, 13051, 3164, 307, 1217, 2435, 294, 51596], "temperature": 0.0,
  "avg_logprob": -0.11868926882743835, "compression_ratio": 1.6239669421487604, "no_speech_prob":
  0.005990014877170324}, {"id": 128, "seek": 79900, "start": 799.0, "end": 806.44,
  "text": " solar, right? Is it already released? And big portion? Yeah, so there
  are different ways", "tokens": [50364, 7936, 11, 558, 30, 1119, 309, 1217, 4736,
  30, 400, 955, 8044, 30, 865, 11, 370, 456, 366, 819, 2098, 50736], "temperature":
  0.0, "avg_logprob": -0.27918898540994397, "compression_ratio": 1.6311111111111112,
  "no_speech_prob": 0.002884520683437586}, {"id": 129, "seek": 79900, "start": 806.44,
  "end": 814.36, "text": " I need search can be performed in solar. So right now,
  we saw 9.6. There are ways of combining", "tokens": [50736, 286, 643, 3164, 393,
  312, 10332, 294, 7936, 13, 407, 558, 586, 11, 321, 1866, 1722, 13, 21, 13, 821,
  366, 2098, 295, 21928, 51132], "temperature": 0.0, "avg_logprob": -0.27918898540994397,
  "compression_ratio": 1.6311111111111112, "no_speech_prob": 0.002884520683437586},
  {"id": 130, "seek": 79900, "start": 814.36, "end": 820.84, "text": " results from
  electrical search and vector-based search and then re-rank them, for example,",
  "tokens": [51132, 3542, 490, 12147, 3164, 293, 8062, 12, 6032, 3164, 293, 550, 319,
  12, 20479, 552, 11, 337, 1365, 11, 51456], "temperature": 0.0, "avg_logprob": -0.27918898540994397,
  "compression_ratio": 1.6311111111111112, "no_speech_prob": 0.002884520683437586},
  {"id": 131, "seek": 79900, "start": 820.84, "end": 827.4, "text": " using learning
  pranks. So you give like different ways to different factors. So for example,",
  "tokens": [51456, 1228, 2539, 582, 14592, 13, 407, 291, 976, 411, 819, 2098, 281,
  819, 6771, 13, 407, 337, 1365, 11, 51784], "temperature": 0.0, "avg_logprob": -0.27918898540994397,
  "compression_ratio": 1.6311111111111112, "no_speech_prob": 0.002884520683437586},
  {"id": 132, "seek": 82740, "start": 827.4, "end": 832.92, "text": " the vector-based
  core or the traditional core. Yeah. What is coming next, which was the topic of
  my", "tokens": [50364, 264, 8062, 12, 6032, 4965, 420, 264, 5164, 4965, 13, 865,
  13, 708, 307, 1348, 958, 11, 597, 390, 264, 4829, 295, 452, 50640], "temperature":
  0.0, "avg_logprob": -0.21674437661772794, "compression_ratio": 1.5991902834008098,
  "no_speech_prob": 0.009263226762413979}, {"id": 133, "seek": 82740, "start": 832.92,
  "end": 840.28, "text": " talk is the receiver rank user. So that''s coming with
  solar 9.7. So I guess in a couple of months,", "tokens": [50640, 751, 307, 264,
  20086, 6181, 4195, 13, 407, 300, 311, 1348, 365, 7936, 1722, 13, 22, 13, 407, 286,
  2041, 294, 257, 1916, 295, 2493, 11, 51008], "temperature": 0.0, "avg_logprob":
  -0.21674437661772794, "compression_ratio": 1.5991902834008098, "no_speech_prob":
  0.009263226762413979}, {"id": 134, "seek": 82740, "start": 840.28, "end": 845.9599999999999,
  "text": " we''re going to release it. Nice. And that is a way of adding hybrid search
  that is independent on", "tokens": [51008, 321, 434, 516, 281, 4374, 309, 13, 5490,
  13, 400, 300, 307, 257, 636, 295, 5127, 13051, 3164, 300, 307, 6695, 322, 51292],
  "temperature": 0.0, "avg_logprob": -0.21674437661772794, "compression_ratio": 1.5991902834008098,
  "no_speech_prob": 0.009263226762413979}, {"id": 135, "seek": 82740, "start": 845.9599999999999,
  "end": 853.0799999999999, "text": " this core and just based on the ranking of the
  results. So you mix the different rank lists. Yeah,", "tokens": [51292, 341, 4965,
  293, 445, 2361, 322, 264, 17833, 295, 264, 3542, 13, 407, 291, 2890, 264, 819, 6181,
  14511, 13, 865, 11, 51648], "temperature": 0.0, "avg_logprob": -0.21674437661772794,
  "compression_ratio": 1.5991902834008098, "no_speech_prob": 0.009263226762413979},
  {"id": 136, "seek": 85308, "start": 853.1600000000001, "end": 859.08, "text": "
  they can be two, maybe more. Yeah. It''s support more supported, not just two. And
  then you combine them", "tokens": [50368, 436, 393, 312, 732, 11, 1310, 544, 13,
  865, 13, 467, 311, 1406, 544, 8104, 11, 406, 445, 732, 13, 400, 550, 291, 10432,
  552, 50664], "temperature": 0.0, "avg_logprob": -0.23221522790414315, "compression_ratio":
  1.7300380228136882, "no_speech_prob": 0.0019908398389816284}, {"id": 137, "seek":
  85308, "start": 859.08, "end": 864.2, "text": " based on the position of the documents
  in the different rank list. Yeah. The higher the position", "tokens": [50664, 2361,
  322, 264, 2535, 295, 264, 8512, 294, 264, 819, 6181, 1329, 13, 865, 13, 440, 2946,
  264, 2535, 50920], "temperature": 0.0, "avg_logprob": -0.23221522790414315, "compression_ratio":
  1.7300380228136882, "no_speech_prob": 0.0019908398389816284}, {"id": 138, "seek":
  85308, "start": 864.2, "end": 869.5600000000001, "text": " in the ranking, the best
  the probability that the document is going to end up in a higher", "tokens": [50920,
  294, 264, 17833, 11, 264, 1151, 264, 8482, 300, 264, 4166, 307, 516, 281, 917, 493,
  294, 257, 2946, 51188], "temperature": 0.0, "avg_logprob": -0.23221522790414315,
  "compression_ratio": 1.7300380228136882, "no_speech_prob": 0.0019908398389816284},
  {"id": 139, "seek": 85308, "start": 869.5600000000001, "end": 875.0, "text": " final
  result set. Yeah, yeah. Actually, when I was maybe you can help me understand this,
  but", "tokens": [51188, 2572, 1874, 992, 13, 865, 11, 1338, 13, 5135, 11, 562, 286,
  390, 1310, 291, 393, 854, 385, 1223, 341, 11, 457, 51460], "temperature": 0.0, "avg_logprob":
  -0.23221522790414315, "compression_ratio": 1.7300380228136882, "no_speech_prob":
  0.0019908398389816284}, {"id": 140, "seek": 85308, "start": 875.0, "end": 880.9200000000001,
  "text": " when we were trying reciprocal rank fusion with another search engine,",
  "tokens": [51460, 562, 321, 645, 1382, 46948, 6181, 23100, 365, 1071, 3164, 2848,
  11, 51756], "temperature": 0.0, "avg_logprob": -0.23221522790414315, "compression_ratio":
  1.7300380228136882, "no_speech_prob": 0.0019908398389816284}, {"id": 141, "seek":
  88308, "start": 883.32, "end": 889.24, "text": " we actually found implementation.
  So we could kind of plug it in and Python code, very quickly.", "tokens": [50376,
  321, 767, 1352, 11420, 13, 407, 321, 727, 733, 295, 5452, 309, 294, 293, 15329,
  3089, 11, 588, 2661, 13, 50672], "temperature": 0.0, "avg_logprob": -0.2510400325693983,
  "compression_ratio": 1.5591836734693878, "no_speech_prob": 0.0028847292996942997},
  {"id": 142, "seek": 88308, "start": 889.64, "end": 894.44, "text": " But then when
  we looked at the code, one of my engineers said, this looks like round,", "tokens":
  [50692, 583, 550, 562, 321, 2956, 412, 264, 3089, 11, 472, 295, 452, 11955, 848,
  11, 341, 1542, 411, 3098, 11, 50932], "temperature": 0.0, "avg_logprob": -0.2510400325693983,
  "compression_ratio": 1.5591836734693878, "no_speech_prob": 0.0028847292996942997},
  {"id": 143, "seek": 88308, "start": 894.44, "end": 901.4000000000001, "text": "
  raw, and algorithm essentially. There is nothing particularly peculiar about it
  or tunable about it,", "tokens": [50932, 8936, 11, 293, 9284, 4476, 13, 821, 307,
  1825, 4098, 27149, 466, 309, 420, 4267, 712, 466, 309, 11, 51280], "temperature":
  0.0, "avg_logprob": -0.2510400325693983, "compression_ratio": 1.5591836734693878,
  "no_speech_prob": 0.0028847292996942997}, {"id": 144, "seek": 88308, "start": 901.4000000000001,
  "end": 907.96, "text": " which probably is not true, but I''m not sure what''s your
  take on this. So it felt like you have two", "tokens": [51280, 597, 1391, 307, 406,
  2074, 11, 457, 286, 478, 406, 988, 437, 311, 428, 747, 322, 341, 13, 407, 309, 2762,
  411, 291, 362, 732, 51608], "temperature": 0.0, "avg_logprob": -0.2510400325693983,
  "compression_ratio": 1.5591836734693878, "no_speech_prob": 0.0028847292996942997},
  {"id": 145, "seek": 90796, "start": 908.44, "end": 913.48, "text": " lists and you
  basically just take the starting from the top, you take like in order, you know,",
  "tokens": [50388, 14511, 293, 291, 1936, 445, 747, 264, 2891, 490, 264, 1192, 11,
  291, 747, 411, 294, 1668, 11, 291, 458, 11, 50640], "temperature": 0.0, "avg_logprob":
  -0.17123609973538306, "compression_ratio": 1.7785977859778597, "no_speech_prob":
  0.012419326230883598}, {"id": 146, "seek": 90796, "start": 913.48, "end": 919.24,
  "text": " these documents and you combine a blend at least, right? But if you wanted
  to pay attention to", "tokens": [50640, 613, 8512, 293, 291, 10432, 257, 10628,
  412, 1935, 11, 558, 30, 583, 498, 291, 1415, 281, 1689, 3202, 281, 50928], "temperature":
  0.0, "avg_logprob": -0.17123609973538306, "compression_ratio": 1.7785977859778597,
  "no_speech_prob": 0.012419326230883598}, {"id": 147, "seek": 90796, "start": 919.24,
  "end": 923.96, "text": " some signals from these documents, you know, based on their
  features or or maybe you wanted to", "tokens": [50928, 512, 12354, 490, 613, 8512,
  11, 291, 458, 11, 2361, 322, 641, 4122, 420, 420, 1310, 291, 1415, 281, 51164],
  "temperature": 0.0, "avg_logprob": -0.17123609973538306, "compression_ratio": 1.7785977859778597,
  "no_speech_prob": 0.012419326230883598}, {"id": 148, "seek": 90796, "start": 923.96,
  "end": 928.6800000000001, "text": " introduce a logic on top of this, right? So
  you want to say, let''s say in the context of geographic", "tokens": [51164, 5366,
  257, 9952, 322, 1192, 295, 341, 11, 558, 30, 407, 291, 528, 281, 584, 11, 718, 311,
  584, 294, 264, 4319, 295, 32318, 51400], "temperature": 0.0, "avg_logprob": -0.17123609973538306,
  "compression_ratio": 1.7785977859778597, "no_speech_prob": 0.012419326230883598},
  {"id": 149, "seek": 90796, "start": 928.6800000000001, "end": 936.36, "text": "
  search, I want to find in top three results, I want to see a super popular B.O.I.
  and I know what", "tokens": [51400, 3164, 11, 286, 528, 281, 915, 294, 1192, 1045,
  3542, 11, 286, 528, 281, 536, 257, 1687, 3743, 363, 13, 46, 13, 40, 13, 293, 286,
  458, 437, 51784], "temperature": 0.0, "avg_logprob": -0.17123609973538306, "compression_ratio":
  1.7785977859778597, "no_speech_prob": 0.012419326230883598}, {"id": 150, "seek":
  93636, "start": 936.36, "end": 942.44, "text": " popular means. Another second result
  could be, I don''t know, the closest one or maybe vice versa,", "tokens": [50364,
  3743, 1355, 13, 3996, 1150, 1874, 727, 312, 11, 286, 500, 380, 458, 11, 264, 13699,
  472, 420, 1310, 11964, 25650, 11, 50668], "temperature": 0.0, "avg_logprob": -0.22435011044897216,
  "compression_ratio": 1.5362903225806452, "no_speech_prob": 0.001863835728727281},
  {"id": 151, "seek": 93636, "start": 942.44, "end": 949.48, "text": " depends. And
  so on so forth. So I have some kind of rules in embed and then maybe it stops becoming",
  "tokens": [50668, 5946, 13, 400, 370, 322, 370, 5220, 13, 407, 286, 362, 512, 733,
  295, 4474, 294, 12240, 293, 550, 1310, 309, 10094, 5617, 51020], "temperature":
  0.0, "avg_logprob": -0.22435011044897216, "compression_ratio": 1.5362903225806452,
  "no_speech_prob": 0.001863835728727281}, {"id": 152, "seek": 93636, "start": 949.48,
  "end": 957.64, "text": " RRE, already, right? But I still go going, taking a step
  backwards. Did I explain it right?", "tokens": [51020, 497, 3850, 11, 1217, 11,
  558, 30, 583, 286, 920, 352, 516, 11, 1940, 257, 1823, 12204, 13, 2589, 286, 2903,
  309, 558, 30, 51428], "temperature": 0.0, "avg_logprob": -0.22435011044897216, "compression_ratio":
  1.5362903225806452, "no_speech_prob": 0.001863835728727281}, {"id": 153, "seek":
  93636, "start": 957.64, "end": 963.24, "text": " Or other some parameters and RRE
  that I could kind of be tuning a bit to have the different", "tokens": [51428, 1610,
  661, 512, 9834, 293, 497, 3850, 300, 286, 727, 733, 295, 312, 15164, 257, 857, 281,
  362, 264, 819, 51708], "temperature": 0.0, "avg_logprob": -0.22435011044897216,
  "compression_ratio": 1.5362903225806452, "no_speech_prob": 0.001863835728727281},
  {"id": 154, "seek": 96324, "start": 963.24, "end": 970.76, "text": " outcome? There''s
  not much to tune to be honest. So you got it right. It''s not only around", "tokens":
  [50364, 9700, 30, 821, 311, 406, 709, 281, 10864, 281, 312, 3245, 13, 407, 291,
  658, 309, 558, 13, 467, 311, 406, 787, 926, 50740], "temperature": 0.0, "avg_logprob":
  -0.27971843083699544, "compression_ratio": 1.7718631178707225, "no_speech_prob":
  0.010089404881000519}, {"id": 155, "seek": 96324, "start": 970.76, "end": 975.96,
  "text": " roaming, because what you do is basically you give a new score to the
  documents that are based on", "tokens": [50740, 42680, 11, 570, 437, 291, 360, 307,
  1936, 291, 976, 257, 777, 6175, 281, 264, 8512, 300, 366, 2361, 322, 51000], "temperature":
  0.0, "avg_logprob": -0.27971843083699544, "compression_ratio": 1.7718631178707225,
  "no_speech_prob": 0.010089404881000519}, {"id": 156, "seek": 96324, "start": 975.96,
  "end": 981.88, "text": " all the rankings of that document in the results list.
  So it''s not like in Perliving where, for", "tokens": [51000, 439, 264, 36550, 295,
  300, 4166, 294, 264, 3542, 1329, 13, 407, 309, 311, 406, 411, 294, 3026, 75, 2123,
  689, 11, 337, 51296], "temperature": 0.0, "avg_logprob": -0.27971843083699544, "compression_ratio":
  1.7718631178707225, "no_speech_prob": 0.010089404881000519}, {"id": 157, "seek":
  96324, "start": 981.88, "end": 986.12, "text": " example, you go with one document,
  you pick from one range of lists and then to the other", "tokens": [51296, 1365,
  11, 291, 352, 365, 472, 4166, 11, 291, 1888, 490, 472, 3613, 295, 14511, 293, 550,
  281, 264, 661, 51508], "temperature": 0.0, "avg_logprob": -0.27971843083699544,
  "compression_ratio": 1.7718631178707225, "no_speech_prob": 0.010089404881000519},
  {"id": 158, "seek": 96324, "start": 986.12, "end": 991.72, "text": " list, you pick
  another and then you choose which one should I go next. It''s more about life,",
  "tokens": [51508, 1329, 11, 291, 1888, 1071, 293, 550, 291, 2826, 597, 472, 820,
  286, 352, 958, 13, 467, 311, 544, 466, 993, 11, 51788], "temperature": 0.0, "avg_logprob":
  -0.27971843083699544, "compression_ratio": 1.7718631178707225, "no_speech_prob":
  0.010089404881000519}, {"id": 159, "seek": 99172, "start": 991.8000000000001, "end":
  996.2, "text": " let''s see this document how many times it appears in the ranking
  list and where it appears in", "tokens": [50368, 718, 311, 536, 341, 4166, 577,
  867, 1413, 309, 7038, 294, 264, 17833, 1329, 293, 689, 309, 7038, 294, 50588], "temperature":
  0.0, "avg_logprob": -0.1817004893085744, "compression_ratio": 1.8319327731092436,
  "no_speech_prob": 0.006877677980810404}, {"id": 160, "seek": 99172, "start": 996.2,
  "end": 1002.44, "text": " the ranking list and let''s build this new score. So the
  more you are in the top positions,", "tokens": [50588, 264, 17833, 1329, 293, 718,
  311, 1322, 341, 777, 6175, 13, 407, 264, 544, 291, 366, 294, 264, 1192, 8432, 11,
  50900], "temperature": 0.0, "avg_logprob": -0.1817004893085744, "compression_ratio":
  1.8319327731092436, "no_speech_prob": 0.006877677980810404}, {"id": 161, "seek":
  99172, "start": 1002.44, "end": 1006.2, "text": " the more likely you end up in
  the top position of the final result list.", "tokens": [50900, 264, 544, 3700, 291,
  917, 493, 294, 264, 1192, 2535, 295, 264, 2572, 1874, 1329, 13, 51088], "temperature":
  0.0, "avg_logprob": -0.1817004893085744, "compression_ratio": 1.8319327731092436,
  "no_speech_prob": 0.006877677980810404}, {"id": 162, "seek": 99172, "start": 1007.24,
  "end": 1012.52, "text": " Given that, you''re absolutely right that if you want
  to be like more advanced ranking", "tokens": [51140, 18600, 300, 11, 291, 434, 3122,
  558, 300, 498, 291, 528, 281, 312, 411, 544, 7339, 17833, 51404], "temperature":
  0.0, "avg_logprob": -0.1817004893085744, "compression_ratio": 1.8319327731092436,
  "no_speech_prob": 0.006877677980810404}, {"id": 163, "seek": 99172, "start": 1012.52,
  "end": 1018.36, "text": " systems, potentially like with different phases, different
  steps, it makes complete sense to", "tokens": [51404, 3652, 11, 7263, 411, 365,
  819, 18764, 11, 819, 4439, 11, 309, 1669, 3566, 2020, 281, 51696], "temperature":
  0.0, "avg_logprob": -0.1817004893085744, "compression_ratio": 1.8319327731092436,
  "no_speech_prob": 0.006877677980810404}, {"id": 164, "seek": 101836, "start": 1018.36,
  "end": 1025.8, "text": " maybe build your original candidate sets with receiver
  or infusion. And then you re-rank,", "tokens": [50364, 1310, 1322, 428, 3380, 11532,
  6352, 365, 20086, 420, 1536, 5704, 13, 400, 550, 291, 319, 12, 20479, 11, 50736],
  "temperature": 0.0, "avg_logprob": -0.3586759567260742, "compression_ratio": 1.6697247706422018,
  "no_speech_prob": 0.0059024677611887455}, {"id": 165, "seek": 101836, "start": 1026.52,
  "end": 1032.2, "text": " for example, using learning to rank and many features where
  you can have like, again, maybe", "tokens": [50772, 337, 1365, 11, 1228, 2539, 281,
  6181, 293, 867, 4122, 689, 291, 393, 362, 411, 11, 797, 11, 1310, 51056], "temperature":
  0.0, "avg_logprob": -0.3586759567260742, "compression_ratio": 1.6697247706422018,
  "no_speech_prob": 0.0059024677611887455}, {"id": 166, "seek": 101836, "start": 1032.2,
  "end": 1037.88, "text": " the vector distances one feature, the similarity we want
  to feel from a expert perspective,", "tokens": [51056, 264, 8062, 22182, 472, 4111,
  11, 264, 32194, 321, 528, 281, 841, 490, 257, 5844, 4585, 11, 51340], "temperature":
  0.0, "avg_logprob": -0.3586759567260742, "compression_ratio": 1.6697247706422018,
  "no_speech_prob": 0.0059024677611887455}, {"id": 167, "seek": 101836, "start": 1038.44,
  "end": 1045.08, "text": " popularity, geographical distance and many other features.
  And then you apply learning for", "tokens": [51368, 19301, 11, 39872, 4560, 293,
  867, 661, 4122, 13, 400, 550, 291, 3079, 2539, 337, 51700], "temperature": 0.0,
  "avg_logprob": -0.3586759567260742, "compression_ratio": 1.6697247706422018, "no_speech_prob":
  0.0059024677611887455}, {"id": 168, "seek": 104508, "start": 1045.08, "end": 1050.12,
  "text": " example, so you train a machine learning model to identify these weights.
  It makes perfect sense", "tokens": [50364, 1365, 11, 370, 291, 3847, 257, 3479,
  2539, 2316, 281, 5876, 613, 17443, 13, 467, 1669, 2176, 2020, 50616], "temperature":
  0.0, "avg_logprob": -0.31095361272129446, "compression_ratio": 1.6797153024911031,
  "no_speech_prob": 0.004169780295342207}, {"id": 169, "seek": 104508, "start": 1050.12,
  "end": 1056.36, "text": " in my opinion. I believe receiver, rank, fusion and in
  general, like let''s call them simple", "tokens": [50616, 294, 452, 4800, 13, 286,
  1697, 20086, 11, 6181, 11, 23100, 293, 294, 2674, 11, 411, 718, 311, 818, 552, 2199,
  50928], "temperature": 0.0, "avg_logprob": -0.31095361272129446, "compression_ratio":
  1.6797153024911031, "no_speech_prob": 0.004169780295342207}, {"id": 170, "seek":
  104508, "start": 1056.36, "end": 1060.6, "text": " approaches with our research,
  because if you take a look to the algorithm of receiver or rank fusion,", "tokens":
  [50928, 11587, 365, 527, 2132, 11, 570, 498, 291, 747, 257, 574, 281, 264, 9284,
  295, 20086, 420, 6181, 23100, 11, 51140], "temperature": 0.0, "avg_logprob": -0.31095361272129446,
  "compression_ratio": 1.6797153024911031, "no_speech_prob": 0.004169780295342207},
  {"id": 171, "seek": 104508, "start": 1060.6, "end": 1066.84, "text": " it''s not
  the core, it''s actually open and open algorithm from 2009. But this opened the",
  "tokens": [51140, 309, 311, 406, 264, 4965, 11, 309, 311, 767, 1269, 293, 1269,
  9284, 490, 11453, 13, 583, 341, 5625, 264, 51452], "temperature": 0.0, "avg_logprob":
  -0.31095361272129446, "compression_ratio": 1.6797153024911031, "no_speech_prob":
  0.004169780295342207}, {"id": 172, "seek": 104508, "start": 1066.84, "end": 1071.96,
  "text": " doors in my opinion to build your original candidate set and then potentially
  like, yeah, you", "tokens": [51452, 8077, 294, 452, 4800, 281, 1322, 428, 3380,
  11532, 992, 293, 550, 7263, 411, 11, 1338, 11, 291, 51708], "temperature": 0.0,
  "avg_logprob": -0.31095361272129446, "compression_ratio": 1.6797153024911031, "no_speech_prob":
  0.004169780295342207}, {"id": 173, "seek": 107196, "start": 1071.96, "end": 1076.76,
  "text": " re-rank it okay. Yeah, yeah, yeah, she''s not random, it''s okay, she''s
  already some", "tokens": [50364, 319, 12, 20479, 309, 1392, 13, 865, 11, 1338, 11,
  1338, 11, 750, 311, 406, 4974, 11, 309, 311, 1392, 11, 750, 311, 1217, 512, 50604],
  "temperature": 0.0, "avg_logprob": -0.2948504647055825, "compression_ratio": 1.5948275862068966,
  "no_speech_prob": 0.014064047485589981}, {"id": 174, "seek": 107196, "start": 1076.76,
  "end": 1084.68, "text": " reasons to be there. And of course, like in any case,
  those without saying that we do need to have", "tokens": [50604, 4112, 281, 312,
  456, 13, 400, 295, 1164, 11, 411, 294, 604, 1389, 11, 729, 1553, 1566, 300, 321,
  360, 643, 281, 362, 51000], "temperature": 0.0, "avg_logprob": -0.2948504647055825,
  "compression_ratio": 1.5948275862068966, "no_speech_prob": 0.014064047485589981},
  {"id": 175, "seek": 107196, "start": 1084.68, "end": 1091.48, "text": " some method
  of combining these completely disparate spaces of scores, right? Into one. And that
  could", "tokens": [51000, 512, 3170, 295, 21928, 613, 2584, 14548, 473, 7673, 295,
  13444, 11, 558, 30, 23373, 472, 13, 400, 300, 727, 51340], "temperature": 0.0, "avg_logprob":
  -0.2948504647055825, "compression_ratio": 1.5948275862068966, "no_speech_prob":
  0.014064047485589981}, {"id": 176, "seek": 107196, "start": 1091.48, "end": 1096.76,
  "text": " be actually even like different search engines operating on keyword level
  because they", "tokens": [51340, 312, 767, 754, 411, 819, 3164, 12982, 7447, 322,
  20428, 1496, 570, 436, 51604], "temperature": 0.0, "avg_logprob": -0.2948504647055825,
  "compression_ratio": 1.5948275862068966, "no_speech_prob": 0.014064047485589981},
  {"id": 177, "seek": 109676, "start": 1096.76, "end": 1102.28, "text": " output different
  scores, right? So maybe even potentially I''m thinking separate charts of your",
  "tokens": [50364, 5598, 819, 13444, 11, 558, 30, 407, 1310, 754, 7263, 286, 478,
  1953, 4994, 17767, 295, 428, 50640], "temperature": 0.0, "avg_logprob": -0.25208108880546654,
  "compression_ratio": 1.5672268907563025, "no_speech_prob": 0.005187679082155228},
  {"id": 178, "seek": 109676, "start": 1102.28, "end": 1109.32, "text": " data that
  also have their own idea, right? Local idea. So, yeah, incomparable, right? Awesome.",
  "tokens": [50640, 1412, 300, 611, 362, 641, 1065, 1558, 11, 558, 30, 22755, 1558,
  13, 407, 11, 1338, 11, 14036, 42012, 11, 558, 30, 10391, 13, 50992], "temperature":
  0.0, "avg_logprob": -0.25208108880546654, "compression_ratio": 1.5672268907563025,
  "no_speech_prob": 0.005187679082155228}, {"id": 179, "seek": 109676, "start": 1110.36,
  "end": 1117.0, "text": " We also, not related to this completely different topic,
  like there was also a keynote today about", "tokens": [51044, 492, 611, 11, 406,
  4077, 281, 341, 2584, 819, 4829, 11, 411, 456, 390, 611, 257, 33896, 965, 466, 51376],
  "temperature": 0.0, "avg_logprob": -0.25208108880546654, "compression_ratio": 1.5672268907563025,
  "no_speech_prob": 0.005187679082155228}, {"id": 180, "seek": 109676, "start": 1118.36,
  "end": 1123.96, "text": " sort of what open source means, right? And without, of
  course, criticizing, but some", "tokens": [51444, 1333, 295, 437, 1269, 4009, 1355,
  11, 558, 30, 400, 1553, 11, 295, 1164, 11, 45474, 11, 457, 512, 51724], "temperature":
  0.0, "avg_logprob": -0.25208108880546654, "compression_ratio": 1.5672268907563025,
  "no_speech_prob": 0.005187679082155228}, {"id": 181, "seek": 112396, "start": 1123.96,
  "end": 1130.1200000000001, "text": " companies were mentioned on this context where
  they claim that the LLMs are open source, but when", "tokens": [50364, 3431, 645,
  2835, 322, 341, 4319, 689, 436, 3932, 300, 264, 441, 43, 26386, 366, 1269, 4009,
  11, 457, 562, 50672], "temperature": 0.0, "avg_logprob": -0.18427793369736784, "compression_ratio":
  1.6785714285714286, "no_speech_prob": 0.002929717767983675}, {"id": 182, "seek":
  112396, "start": 1130.1200000000001, "end": 1136.52, "text": " you look at the licenses,
  they are restrictive, they actually do not allow you to use them", "tokens": [50672,
  291, 574, 412, 264, 32821, 11, 436, 366, 43220, 11, 436, 767, 360, 406, 2089, 291,
  281, 764, 552, 50992], "temperature": 0.0, "avg_logprob": -0.18427793369736784,
  "compression_ratio": 1.6785714285714286, "no_speech_prob": 0.002929717767983675},
  {"id": 183, "seek": 112396, "start": 1136.52, "end": 1142.76, "text": " independently,
  right? And kind of go and serve your customers. But you also just mentioned", "tokens":
  [50992, 21761, 11, 558, 30, 400, 733, 295, 352, 293, 4596, 428, 4581, 13, 583, 291,
  611, 445, 2835, 51304], "temperature": 0.0, "avg_logprob": -0.18427793369736784,
  "compression_ratio": 1.6785714285714286, "no_speech_prob": 0.002929717767983675},
  {"id": 184, "seek": 112396, "start": 1142.76, "end": 1148.92, "text": " what the
  code was started recording is that there are also cases where model can be open
  source,", "tokens": [51304, 437, 264, 3089, 390, 1409, 6613, 307, 300, 456, 366,
  611, 3331, 689, 2316, 393, 312, 1269, 4009, 11, 51612], "temperature": 0.0, "avg_logprob":
  -0.18427793369736784, "compression_ratio": 1.6785714285714286, "no_speech_prob":
  0.002929717767983675}, {"id": 185, "seek": 114892, "start": 1149.0, "end": 1154.6000000000001,
  "text": " and it''s kind of like more or less abiding the principles of open source
  spirit, but then", "tokens": [50368, 293, 309, 311, 733, 295, 411, 544, 420, 1570,
  410, 2819, 264, 9156, 295, 1269, 4009, 3797, 11, 457, 550, 50648], "temperature":
  0.0, "avg_logprob": -0.12047401889339908, "compression_ratio": 1.832512315270936,
  "no_speech_prob": 0.0020599726121872663}, {"id": 186, "seek": 114892, "start": 1156.04,
  "end": 1161.96, "text": " contract, but then the data that it was trained on is
  not open source or the methods that were", "tokens": [50720, 4364, 11, 457, 550,
  264, 1412, 300, 309, 390, 8895, 322, 307, 406, 1269, 4009, 420, 264, 7150, 300,
  645, 51016], "temperature": 0.0, "avg_logprob": -0.12047401889339908, "compression_ratio":
  1.832512315270936, "no_speech_prob": 0.0020599726121872663}, {"id": 187, "seek":
  114892, "start": 1161.96, "end": 1169.24, "text": " applied to the data are not
  open source, right? So to me, it sounds so important to keep kind of", "tokens":
  [51016, 6456, 281, 264, 1412, 366, 406, 1269, 4009, 11, 558, 30, 407, 281, 385,
  11, 309, 3263, 370, 1021, 281, 1066, 733, 295, 51380], "temperature": 0.0, "avg_logprob":
  -0.12047401889339908, "compression_ratio": 1.832512315270936, "no_speech_prob":
  0.0020599726121872663}, {"id": 188, "seek": 114892, "start": 1169.24, "end": 1175.16,
  "text": " declaring what open source is, what are the principles, right? And maybe
  this keynote also", "tokens": [51380, 40374, 437, 1269, 4009, 307, 11, 437, 366,
  264, 9156, 11, 558, 30, 400, 1310, 341, 33896, 611, 51676], "temperature": 0.0,
  "avg_logprob": -0.12047401889339908, "compression_ratio": 1.832512315270936, "no_speech_prob":
  0.0020599726121872663}, {"id": 189, "seek": 117516, "start": 1175.24, "end": 1180.1200000000001,
  "text": " shed some light, but you also, it seems like this topic is also very close
  to you, and you", "tokens": [50368, 14951, 512, 1442, 11, 457, 291, 611, 11, 309,
  2544, 411, 341, 4829, 307, 611, 588, 1998, 281, 291, 11, 293, 291, 50612], "temperature":
  0.0, "avg_logprob": -0.20703210001406464, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.008307372219860554}, {"id": 190, "seek": 117516, "start": 1180.1200000000001,
  "end": 1186.44, "text": " are in the open source contributing a lot, you are the
  commuter, like can you can you share your", "tokens": [50612, 366, 294, 264, 1269,
  4009, 19270, 257, 688, 11, 291, 366, 264, 800, 20314, 11, 411, 393, 291, 393, 291,
  2073, 428, 50928], "temperature": 0.0, "avg_logprob": -0.20703210001406464, "compression_ratio":
  1.6724890829694323, "no_speech_prob": 0.008307372219860554}, {"id": 191, "seek":
  117516, "start": 1186.44, "end": 1192.68, "text": " vision on what is open source,
  what are the implications for how this field should be developing?", "tokens": [50928,
  5201, 322, 437, 307, 1269, 4009, 11, 437, 366, 264, 16602, 337, 577, 341, 2519,
  820, 312, 6416, 30, 51240], "temperature": 0.0, "avg_logprob": -0.20703210001406464,
  "compression_ratio": 1.6724890829694323, "no_speech_prob": 0.008307372219860554},
  {"id": 192, "seek": 117516, "start": 1194.0400000000002, "end": 1200.44, "text":
  " I think it''s a huge problem, especially because nowadays open washing, which
  is like the practice", "tokens": [51308, 286, 519, 309, 311, 257, 2603, 1154, 11,
  2318, 570, 13434, 1269, 13836, 11, 597, 307, 411, 264, 3124, 51628], "temperature":
  0.0, "avg_logprob": -0.20703210001406464, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.008307372219860554}, {"id": 193, "seek": 120044, "start": 1200.52,
  "end": 1206.2, "text": " of associating openness to something that potentially is
  not really fully open, is happening a lot.", "tokens": [50368, 295, 4180, 990, 36200,
  281, 746, 300, 7263, 307, 406, 534, 4498, 1269, 11, 307, 2737, 257, 688, 13, 50652],
  "temperature": 0.0, "avg_logprob": -0.21035854790800362, "compression_ratio": 1.751131221719457,
  "no_speech_prob": 0.0067875441163778305}, {"id": 194, "seek": 120044, "start": 1206.2,
  "end": 1212.76, "text": " Here''s open source is cool, open source show like a good
  habit, so you''re the good guys if you", "tokens": [50652, 1692, 311, 1269, 4009,
  307, 1627, 11, 1269, 4009, 855, 411, 257, 665, 7164, 11, 370, 291, 434, 264, 665,
  1074, 498, 291, 50980], "temperature": 0.0, "avg_logprob": -0.21035854790800362,
  "compression_ratio": 1.751131221719457, "no_speech_prob": 0.0067875441163778305},
  {"id": 195, "seek": 120044, "start": 1212.76, "end": 1219.0800000000002, "text":
  " if you do open source. So as you said, we are not going to make names of companies
  or association", "tokens": [50980, 498, 291, 360, 1269, 4009, 13, 407, 382, 291,
  848, 11, 321, 366, 406, 516, 281, 652, 5288, 295, 3431, 420, 14598, 51296], "temperature":
  0.0, "avg_logprob": -0.21035854790800362, "compression_ratio": 1.751131221719457,
  "no_speech_prob": 0.0067875441163778305}, {"id": 196, "seek": 120044, "start": 1219.0800000000002,
  "end": 1224.04, "text": " that claim, for example, they lar language model were
  open source, but lar language models are", "tokens": [51296, 300, 3932, 11, 337,
  1365, 11, 436, 1613, 2856, 2316, 645, 1269, 4009, 11, 457, 1613, 2856, 5245, 366,
  51544], "temperature": 0.0, "avg_logprob": -0.21035854790800362, "compression_ratio":
  1.751131221719457, "no_speech_prob": 0.0067875441163778305}, {"id": 197, "seek":
  122404, "start": 1224.12, "end": 1231.08, "text": " complex systems. So the outputs,
  the final light waves on the neural network is just one little part", "tokens":
  [50368, 3997, 3652, 13, 407, 264, 23930, 11, 264, 2572, 1442, 9417, 322, 264, 18161,
  3209, 307, 445, 472, 707, 644, 50716], "temperature": 0.0, "avg_logprob": -0.21566313963669997,
  "compression_ratio": 1.7155555555555555, "no_speech_prob": 0.007961480878293514},
  {"id": 198, "seek": 122404, "start": 1231.08, "end": 1237.8, "text": " of the entire
  picture. Those lar language models are normally pre-trained on huge quantities of",
  "tokens": [50716, 295, 264, 2302, 3036, 13, 3950, 1613, 2856, 5245, 366, 5646, 659,
  12, 17227, 2001, 322, 2603, 22927, 295, 51052], "temperature": 0.0, "avg_logprob":
  -0.21566313963669997, "compression_ratio": 1.7155555555555555, "no_speech_prob":
  0.007961480878293514}, {"id": 199, "seek": 122404, "start": 1237.8, "end": 1246.84,
  "text": " data with a pre-training algorithm. So the pre-training data and the pre-training
  code,", "tokens": [51052, 1412, 365, 257, 659, 12, 17227, 1760, 9284, 13, 407, 264,
  659, 12, 17227, 1760, 1412, 293, 264, 659, 12, 17227, 1760, 3089, 11, 51504], "temperature":
  0.0, "avg_logprob": -0.21566313963669997, "compression_ratio": 1.7155555555555555,
  "no_speech_prob": 0.007961480878293514}, {"id": 200, "seek": 122404, "start": 1247.96,
  "end": 1253.8, "text": " is it open? Is it not? I mean, many times it''s not, not
  only not, it''s not open, it''s not even known,", "tokens": [51560, 307, 309, 1269,
  30, 1119, 309, 406, 30, 286, 914, 11, 867, 1413, 309, 311, 406, 11, 406, 787, 406,
  11, 309, 311, 406, 1269, 11, 309, 311, 406, 754, 2570, 11, 51852], "temperature":
  0.0, "avg_logprob": -0.21566313963669997, "compression_ratio": 1.7155555555555555,
  "no_speech_prob": 0.007961480878293514}, {"id": 201, "seek": 125404, "start": 1254.04,
  "end": 1261.48, "text": " what kind of data is just generic internet scale data.
  What about the fine tuning them? So", "tokens": [50364, 437, 733, 295, 1412, 307,
  445, 19577, 4705, 4373, 1412, 13, 708, 466, 264, 2489, 15164, 552, 30, 407, 50736],
  "temperature": 0.0, "avg_logprob": -0.18889763534709972, "compression_ratio": 1.619047619047619,
  "no_speech_prob": 0.0021331042516976595}, {"id": 202, "seek": 125404, "start": 1261.48,
  "end": 1265.6399999999999, "text": " once you get the pre-training, which is the
  unsupervised part, where you just explore the web,", "tokens": [50736, 1564, 291,
  483, 264, 659, 12, 17227, 1760, 11, 597, 307, 264, 2693, 12879, 24420, 644, 11,
  689, 291, 445, 6839, 264, 3670, 11, 50944], "temperature": 0.0, "avg_logprob": -0.18889763534709972,
  "compression_ratio": 1.619047619047619, "no_speech_prob": 0.0021331042516976595},
  {"id": 203, "seek": 125404, "start": 1265.6399999999999, "end": 1271.6399999999999,
  "text": " that''s pretty simple, then you want to fine tune for specific tasks,
  like sentence similarity or", "tokens": [50944, 300, 311, 1238, 2199, 11, 550, 291,
  528, 281, 2489, 10864, 337, 2685, 9608, 11, 411, 8174, 32194, 420, 51244], "temperature":
  0.0, "avg_logprob": -0.18889763534709972, "compression_ratio": 1.619047619047619,
  "no_speech_prob": 0.0021331042516976595}, {"id": 204, "seek": 125404, "start": 1272.28,
  "end": 1277.72, "text": " instruction following or, I don''t know, summarization,
  any kind of task you want to use the", "tokens": [51276, 10951, 3480, 420, 11, 286,
  500, 380, 458, 11, 14611, 2144, 11, 604, 733, 295, 5633, 291, 528, 281, 764, 264,
  51548], "temperature": 0.0, "avg_logprob": -0.18889763534709972, "compression_ratio":
  1.619047619047619, "no_speech_prob": 0.0021331042516976595}, {"id": 205, "seek":
  127772, "start": 1278.68, "end": 1284.84, "text": " and to do that normally using
  an additional training data set that is particularly designed for", "tokens": [50412,
  293, 281, 360, 300, 5646, 1228, 364, 4497, 3097, 1412, 992, 300, 307, 4098, 4761,
  337, 50720], "temperature": 0.0, "avg_logprob": -0.20213103020328216, "compression_ratio":
  1.835820895522388, "no_speech_prob": 0.005818348843604326}, {"id": 206, "seek":
  127772, "start": 1284.84, "end": 1291.16, "text": " that fine tuning task. And again,
  is that open? So do you communicate and then you make it available?", "tokens":
  [50720, 300, 2489, 15164, 5633, 13, 400, 797, 11, 307, 300, 1269, 30, 407, 360,
  291, 7890, 293, 550, 291, 652, 309, 2435, 30, 51036], "temperature": 0.0, "avg_logprob":
  -0.20213103020328216, "compression_ratio": 1.835820895522388, "no_speech_prob":
  0.005818348843604326}, {"id": 207, "seek": 127772, "start": 1292.1200000000001,
  "end": 1298.28, "text": " And the code for fine tuning, do you make it available?
  The output of the pre-training,", "tokens": [51084, 400, 264, 3089, 337, 2489, 15164,
  11, 360, 291, 652, 309, 2435, 30, 440, 5598, 295, 264, 659, 12, 17227, 1760, 11,
  51392], "temperature": 0.0, "avg_logprob": -0.20213103020328216, "compression_ratio":
  1.835820895522388, "no_speech_prob": 0.005818348843604326}, {"id": 208, "seek":
  127772, "start": 1298.28, "end": 1303.32, "text": " do you make it available separately
  from the output of the fine, the documentation,", "tokens": [51392, 360, 291, 652,
  309, 2435, 14759, 490, 264, 5598, 295, 264, 2489, 11, 264, 14333, 11, 51644], "temperature":
  0.0, "avg_logprob": -0.20213103020328216, "compression_ratio": 1.835820895522388,
  "no_speech_prob": 0.005818348843604326}, {"id": 209, "seek": 130332, "start": 1303.3999999999999,
  "end": 1310.28, "text": " any data that explains what is done, why you found it?
  So I''ve read like an interesting paper that", "tokens": [50368, 604, 1412, 300,
  13948, 437, 307, 1096, 11, 983, 291, 1352, 309, 30, 407, 286, 600, 1401, 411, 364,
  1880, 3035, 300, 50712], "temperature": 0.0, "avg_logprob": -0.43238083745392275,
  "compression_ratio": 1.5336787564766838, "no_speech_prob": 0.022216973826289177},
  {"id": 210, "seek": 130332, "start": 1310.28, "end": 1316.9199999999998, "text":
  " I guess we can share, like, as a comment from a university, they were like comparing
  all these aspects", "tokens": [50712, 286, 2041, 321, 393, 2073, 11, 411, 11, 382,
  257, 2871, 490, 257, 5454, 11, 436, 645, 411, 15763, 439, 613, 7270, 51044], "temperature":
  0.0, "avg_logprob": -0.43238083745392275, "compression_ratio": 1.5336787564766838,
  "no_speech_prob": 0.022216973826289177}, {"id": 211, "seek": 130332, "start": 1316.9199999999998,
  "end": 1324.76, "text": " for the MS models and how famous like open source of the
  MS models actually behaved on each of", "tokens": [51044, 337, 264, 7395, 5245,
  293, 577, 4618, 411, 1269, 4009, 295, 264, 7395, 5245, 767, 48249, 322, 1184, 295,
  51436], "temperature": 0.0, "avg_logprob": -0.43238083745392275, "compression_ratio":
  1.5336787564766838, "no_speech_prob": 0.022216973826289177}, {"id": 212, "seek":
  132476, "start": 1324.76, "end": 1332.68, "text": " these columns and would be surprising
  how a small percentage of these like, you know, big layers", "tokens": [50364, 613,
  13766, 293, 576, 312, 8830, 577, 257, 1359, 9668, 295, 613, 411, 11, 291, 458, 11,
  955, 7914, 50760], "temperature": 0.0, "avg_logprob": -0.237389407315097, "compression_ratio":
  1.6551724137931034, "no_speech_prob": 0.004554250277578831}, {"id": 213, "seek":
  132476, "start": 1332.68, "end": 1337.48, "text": " are actually open sourcing everything.
  So it''s not just the license that as you said correctly,", "tokens": [50760, 366,
  767, 1269, 11006, 2175, 1203, 13, 407, 309, 311, 406, 445, 264, 10476, 300, 382,
  291, 848, 8944, 11, 51000], "temperature": 0.0, "avg_logprob": -0.237389407315097,
  "compression_ratio": 1.6551724137931034, "no_speech_prob": 0.004554250277578831},
  {"id": 214, "seek": 132476, "start": 1337.48, "end": 1342.76, "text": " sometimes
  it''s limiting, but literally like the components shirt, sometimes it''s just the
  final", "tokens": [51000, 2171, 309, 311, 22083, 11, 457, 3736, 411, 264, 6677,
  8336, 11, 2171, 309, 311, 445, 264, 2572, 51264], "temperature": 0.0, "avg_logprob":
  -0.237389407315097, "compression_ratio": 1.6551724137931034, "no_speech_prob": 0.004554250277578831},
  {"id": 215, "seek": 132476, "start": 1344.2, "end": 1348.68, "text": " which is,
  is it helpful? I mean, in open source, you want to cooperate, you want to improve
  the", "tokens": [51336, 597, 307, 11, 307, 309, 4961, 30, 286, 914, 11, 294, 1269,
  4009, 11, 291, 528, 281, 26667, 11, 291, 528, 281, 3470, 264, 51560], "temperature":
  0.0, "avg_logprob": -0.237389407315097, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.004554250277578831}, {"id": 216, "seek": 134868, "start": 1348.68,
  "end": 1354.92, "text": " code, like in normal code, you have access to everything
  and you can like improve, you can", "tokens": [50364, 3089, 11, 411, 294, 2710,
  3089, 11, 291, 362, 2105, 281, 1203, 293, 291, 393, 411, 3470, 11, 291, 393, 50676],
  "temperature": 0.0, "avg_logprob": -0.331269619511623, "compression_ratio": 1.6218487394957983,
  "no_speech_prob": 0.003783289110288024}, {"id": 217, "seek": 134868, "start": 1354.92,
  "end": 1360.68, "text": " help the community. If you just access the ways, you can
  use it, but can you, for example, improve", "tokens": [50676, 854, 264, 1768, 13,
  759, 291, 445, 2105, 264, 2098, 11, 291, 393, 764, 309, 11, 457, 393, 291, 11, 337,
  1365, 11, 3470, 50964], "temperature": 0.0, "avg_logprob": -0.331269619511623, "compression_ratio":
  1.6218487394957983, "no_speech_prob": 0.003783289110288024}, {"id": 218, "seek":
  134868, "start": 1360.68, "end": 1367.16, "text": " it? Can you understand if it''s
  fair? In the data you was there? Yes. Yeah, it''s really difficult.", "tokens":
  [50964, 309, 30, 1664, 291, 1223, 498, 309, 311, 3143, 30, 682, 264, 1412, 291,
  390, 456, 30, 1079, 13, 865, 11, 309, 311, 534, 2252, 13, 51288], "temperature":
  0.0, "avg_logprob": -0.331269619511623, "compression_ratio": 1.6218487394957983,
  "no_speech_prob": 0.003783289110288024}, {"id": 219, "seek": 134868, "start": 1367.16,
  "end": 1373.8, "text": " Yeah. And so, what do you think these discussions should
  start or maybe it''s ongoing? Are you part", "tokens": [51288, 865, 13, 400, 370,
  11, 437, 360, 291, 519, 613, 11088, 820, 722, 420, 1310, 309, 311, 10452, 30, 2014,
  291, 644, 51620], "temperature": 0.0, "avg_logprob": -0.331269619511623, "compression_ratio":
  1.6218487394957983, "no_speech_prob": 0.003783289110288024}, {"id": 220, "seek":
  137380, "start": 1373.8, "end": 1381.48, "text": " of some discussion? And how does
  it impact business and maybe research? Right? Because there are", "tokens": [50364,
  295, 512, 5017, 30, 400, 577, 775, 309, 2712, 1606, 293, 1310, 2132, 30, 1779, 30,
  1436, 456, 366, 50748], "temperature": 0.0, "avg_logprob": -0.20948582310830394,
  "compression_ratio": 1.5668016194331984, "no_speech_prob": 0.019500738009810448},
  {"id": 221, "seek": 137380, "start": 1381.48, "end": 1390.28, "text": " different
  sides of this coin. Many of these things emerge in the academia space, but then
  they move", "tokens": [50748, 819, 4881, 295, 341, 11464, 13, 5126, 295, 613, 721,
  21511, 294, 264, 28937, 1901, 11, 457, 550, 436, 1286, 51188], "temperature": 0.0,
  "avg_logprob": -0.20948582310830394, "compression_ratio": 1.5668016194331984, "no_speech_prob":
  0.019500738009810448}, {"id": 222, "seek": 137380, "start": 1390.28, "end": 1396.84,
  "text": " to create value on the business side, but it could also be vice versa.
  So what do you think?", "tokens": [51188, 281, 1884, 2158, 322, 264, 1606, 1252,
  11, 457, 309, 727, 611, 312, 11964, 25650, 13, 407, 437, 360, 291, 519, 30, 51516],
  "temperature": 0.0, "avg_logprob": -0.20948582310830394, "compression_ratio": 1.5668016194331984,
  "no_speech_prob": 0.019500738009810448}, {"id": 223, "seek": 137380, "start": 1397.6399999999999,
  "end": 1403.24, "text": " What are we going to address this? So I know that the
  open source initiative, which is a group of", "tokens": [51556, 708, 366, 321, 516,
  281, 2985, 341, 30, 407, 286, 458, 300, 264, 1269, 4009, 11552, 11, 597, 307, 257,
  1594, 295, 51836], "temperature": 0.0, "avg_logprob": -0.20948582310830394, "compression_ratio":
  1.5668016194331984, "no_speech_prob": 0.019500738009810448}, {"id": 224, "seek":
  140324, "start": 1403.24, "end": 1409.4, "text": " people that directly directly
  open source manifest, so I try to basically think to ways of the", "tokens": [50364,
  561, 300, 3838, 3838, 1269, 4009, 10067, 11, 370, 286, 853, 281, 1936, 519, 281,
  2098, 295, 264, 50672], "temperature": 0.0, "avg_logprob": -0.2789993502876975,
  "compression_ratio": 1.7416267942583732, "no_speech_prob": 0.005888727493584156},
  {"id": 225, "seek": 140324, "start": 1409.4, "end": 1416.44, "text": " finding open
  source is they are working on a definition of open source for AI models.", "tokens":
  [50672, 5006, 1269, 4009, 307, 436, 366, 1364, 322, 257, 7123, 295, 1269, 4009,
  337, 7318, 5245, 13, 51024], "temperature": 0.0, "avg_logprob": -0.2789993502876975,
  "compression_ratio": 1.7416267942583732, "no_speech_prob": 0.005888727493584156},
  {"id": 226, "seek": 140324, "start": 1417.24, "end": 1423.56, "text": " We are going
  to see hopefully soon enough, a definition of what it means for a model to be",
  "tokens": [51064, 492, 366, 516, 281, 536, 4696, 2321, 1547, 11, 257, 7123, 295,
  437, 309, 1355, 337, 257, 2316, 281, 312, 51380], "temperature": 0.0, "avg_logprob":
  -0.2789993502876975, "compression_ratio": 1.7416267942583732, "no_speech_prob":
  0.005888727493584156}, {"id": 227, "seek": 140324, "start": 1423.56, "end": 1429.0,
  "text": " open source. And that is going to be great, because at that point it''s
  not a matter of like,", "tokens": [51380, 1269, 4009, 13, 400, 300, 307, 516, 281,
  312, 869, 11, 570, 412, 300, 935, 309, 311, 406, 257, 1871, 295, 411, 11, 51652],
  "temperature": 0.0, "avg_logprob": -0.2789993502876975, "compression_ratio": 1.7416267942583732,
  "no_speech_prob": 0.005888727493584156}, {"id": 228, "seek": 142900, "start": 1429.56,
  "end": 1436.84, "text": " I believe it''s open, and I claim it''s open. It''s open
  for its notes. And everything is covered", "tokens": [50392, 286, 1697, 309, 311,
  1269, 11, 293, 286, 3932, 309, 311, 1269, 13, 467, 311, 1269, 337, 1080, 5570, 13,
  400, 1203, 307, 5343, 50756], "temperature": 0.0, "avg_logprob": -0.2756321716308594,
  "compression_ratio": 1.5604395604395604, "no_speech_prob": 0.010949679650366306},
  {"id": 229, "seek": 142900, "start": 1436.84, "end": 1443.8, "text": " by a license
  that is going to be open or not. In terms of like impolination between like the",
  "tokens": [50756, 538, 257, 10476, 300, 307, 516, 281, 312, 1269, 420, 406, 13,
  682, 2115, 295, 411, 704, 401, 2486, 1296, 411, 264, 51104], "temperature": 0.0,
  "avg_logprob": -0.2756321716308594, "compression_ratio": 1.5604395604395604, "no_speech_prob":
  0.010949679650366306}, {"id": 230, "seek": 142900, "start": 1443.8, "end": 1453.16,
  "text": " academia and the industry, I think probably that''s the most, I mean,
  this period is so important", "tokens": [51104, 28937, 293, 264, 3518, 11, 286,
  519, 1391, 300, 311, 264, 881, 11, 286, 914, 11, 341, 2896, 307, 370, 1021, 51572],
  "temperature": 0.0, "avg_logprob": -0.2756321716308594, "compression_ratio": 1.5604395604395604,
  "no_speech_prob": 0.010949679650366306}, {"id": 231, "seek": 145316, "start": 1453.88,
  "end": 1459.5600000000002, "text": " to see like cross pollination, because there
  are like many models that for example are", "tokens": [50400, 281, 536, 411, 3278,
  6418, 2486, 11, 570, 456, 366, 411, 867, 5245, 300, 337, 1365, 366, 50684], "temperature":
  0.0, "avg_logprob": -0.28062552940554736, "compression_ratio": 1.7962085308056872,
  "no_speech_prob": 0.013462143950164318}, {"id": 232, "seek": 145316, "start": 1459.5600000000002,
  "end": 1466.1200000000001, "text": " designed and contributed by the academia that
  must then be used by organizations and the other", "tokens": [50684, 4761, 293,
  18434, 538, 264, 28937, 300, 1633, 550, 312, 1143, 538, 6150, 293, 264, 661, 51012],
  "temperature": 0.0, "avg_logprob": -0.28062552940554736, "compression_ratio": 1.7962085308056872,
  "no_speech_prob": 0.013462143950164318}, {"id": 233, "seek": 145316, "start": 1466.1200000000001,
  "end": 1470.28, "text": " way around, because of course there are like a lot of
  money involved in training and free training", "tokens": [51012, 636, 926, 11, 570,
  295, 1164, 456, 366, 411, 257, 688, 295, 1460, 3288, 294, 3097, 293, 1737, 3097,
  51220], "temperature": 0.0, "avg_logprob": -0.28062552940554736, "compression_ratio":
  1.7962085308056872, "no_speech_prob": 0.013462143950164318}, {"id": 234, "seek":
  145316, "start": 1470.28, "end": 1477.24, "text": " and fine training on the algorithm
  of the models. So many, I mean, only few actually organizations", "tokens": [51220,
  293, 2489, 3097, 322, 264, 9284, 295, 264, 5245, 13, 407, 867, 11, 286, 914, 11,
  787, 1326, 767, 6150, 51568], "temperature": 0.0, "avg_logprob": -0.28062552940554736,
  "compression_ratio": 1.7962085308056872, "no_speech_prob": 0.013462143950164318},
  {"id": 235, "seek": 147724, "start": 1477.24, "end": 1483.48, "text": " are able
  to do this. So they should try, I mean, ideally to make it as open as possible in
  a way", "tokens": [50364, 366, 1075, 281, 360, 341, 13, 407, 436, 820, 853, 11,
  286, 914, 11, 22915, 281, 652, 309, 382, 1269, 382, 1944, 294, 257, 636, 50676],
  "temperature": 0.0, "avg_logprob": -0.3184212154812283, "compression_ratio": 1.5991379310344827,
  "no_speech_prob": 0.00343546480871737}, {"id": 236, "seek": 147724, "start": 1483.48,
  "end": 1488.6, "text": " that then universities can focus on small components and
  potentially help in some more.", "tokens": [50676, 300, 550, 11779, 393, 1879, 322,
  1359, 6677, 293, 7263, 854, 294, 512, 544, 13, 50932], "temperature": 0.0, "avg_logprob":
  -0.3184212154812283, "compression_ratio": 1.5991379310344827, "no_speech_prob":
  0.00343546480871737}, {"id": 237, "seek": 147724, "start": 1488.6, "end": 1495.88,
  "text": " Yeah, yeah. I mean, you know, pre-training and internet scale is incredibly
  expensive from", "tokens": [50932, 865, 11, 1338, 13, 286, 914, 11, 291, 458, 11,
  659, 12, 17227, 1760, 293, 4705, 4373, 307, 6252, 5124, 490, 51296], "temperature":
  0.0, "avg_logprob": -0.3184212154812283, "compression_ratio": 1.5991379310344827,
  "no_speech_prob": 0.00343546480871737}, {"id": 238, "seek": 147724, "start": 1495.88,
  "end": 1505.0, "text": " energy perspective especially. So I hope, you know, we
  reach the point where everything is open", "tokens": [51296, 2281, 4585, 2318, 13,
  407, 286, 1454, 11, 291, 458, 11, 321, 2524, 264, 935, 689, 1203, 307, 1269, 51752],
  "temperature": 0.0, "avg_logprob": -0.3184212154812283, "compression_ratio": 1.5991379310344827,
  "no_speech_prob": 0.00343546480871737}, {"id": 239, "seek": 150500, "start": 1505.8,
  "end": 1511.48, "text": " enough for also smaller organizations and academia organizations
  to 12.", "tokens": [50404, 1547, 337, 611, 4356, 6150, 293, 28937, 6150, 281, 2272,
  13, 50688], "temperature": 0.0, "avg_logprob": -0.2461254657843174, "compression_ratio":
  1.5980861244019138, "no_speech_prob": 0.009635263122618198}, {"id": 240, "seek":
  150500, "start": 1511.48, "end": 1515.32, "text": " Yeah, it''s very interesting
  because there is always going to be this kind of", "tokens": [50688, 865, 11, 309,
  311, 588, 1880, 570, 456, 307, 1009, 516, 281, 312, 341, 733, 295, 50880], "temperature":
  0.0, "avg_logprob": -0.2461254657843174, "compression_ratio": 1.5980861244019138,
  "no_speech_prob": 0.009635263122618198}, {"id": 241, "seek": 150500, "start": 1516.84,
  "end": 1522.6, "text": " play between, okay, this big company has all the servers,
  they need to train the model.", "tokens": [50956, 862, 1296, 11, 1392, 11, 341,
  955, 2237, 575, 439, 264, 15909, 11, 436, 643, 281, 3847, 264, 2316, 13, 51244],
  "temperature": 0.0, "avg_logprob": -0.2461254657843174, "compression_ratio": 1.5980861244019138,
  "no_speech_prob": 0.009635263122618198}, {"id": 242, "seek": 150500, "start": 1522.6,
  "end": 1529.72, "text": " So they can also decide how they will do it and not kind
  of disclose, but then maybe the question", "tokens": [51244, 407, 436, 393, 611,
  4536, 577, 436, 486, 360, 309, 293, 406, 733, 295, 36146, 11, 457, 550, 1310, 264,
  1168, 51600], "temperature": 0.0, "avg_logprob": -0.2461254657843174, "compression_ratio":
  1.5980861244019138, "no_speech_prob": 0.009635263122618198}, {"id": 243, "seek":
  152972, "start": 1529.8, "end": 1535.32, "text": " that we need to be disputing
  and sort of discussing is that they still don''t have all the data", "tokens": [50368,
  300, 321, 643, 281, 312, 37669, 278, 293, 1333, 295, 10850, 307, 300, 436, 920,
  500, 380, 362, 439, 264, 1412, 50644], "temperature": 0.0, "avg_logprob": -0.12686287459506784,
  "compression_ratio": 1.6986899563318778, "no_speech_prob": 0.005662213079631329},
  {"id": 244, "seek": 152972, "start": 1535.32, "end": 1540.04, "text": " to train
  on, right? Potentially. Like there have been some cases mentioned in the keynote,
  you know,", "tokens": [50644, 281, 3847, 322, 11, 558, 30, 9145, 3137, 13, 1743,
  456, 362, 668, 512, 3331, 2835, 294, 264, 33896, 11, 291, 458, 11, 50880], "temperature":
  0.0, "avg_logprob": -0.12686287459506784, "compression_ratio": 1.6986899563318778,
  "no_speech_prob": 0.005662213079631329}, {"id": 245, "seek": 152972, "start": 1540.04,
  "end": 1548.52, "text": " when some company, we will not name the company, it goes
  and trains it on some articles of famous", "tokens": [50880, 562, 512, 2237, 11,
  321, 486, 406, 1315, 264, 2237, 11, 309, 1709, 293, 16329, 309, 322, 512, 11290,
  295, 4618, 51304], "temperature": 0.0, "avg_logprob": -0.12686287459506784, "compression_ratio":
  1.6986899563318778, "no_speech_prob": 0.005662213079631329}, {"id": 246, "seek":
  152972, "start": 1548.52, "end": 1553.64, "text": " publishing house, right? And
  now that publishing house is unhappy because they say you took our", "tokens": [51304,
  17832, 1782, 11, 558, 30, 400, 586, 300, 17832, 1782, 307, 22172, 570, 436, 584,
  291, 1890, 527, 51560], "temperature": 0.0, "avg_logprob": -0.12686287459506784,
  "compression_ratio": 1.6986899563318778, "no_speech_prob": 0.005662213079631329},
  {"id": 247, "seek": 155364, "start": 1553.72, "end": 1559.0, "text": " articles
  without us knowing this. Now, it now it kind of evokes this question, okay,", "tokens":
  [50368, 11290, 1553, 505, 5276, 341, 13, 823, 11, 309, 586, 309, 733, 295, 1073,
  8606, 341, 1168, 11, 1392, 11, 50632], "temperature": 0.0, "avg_logprob": -0.20279652731759207,
  "compression_ratio": 1.7056603773584906, "no_speech_prob": 0.009502504952251911},
  {"id": 248, "seek": 155364, "start": 1560.2, "end": 1564.44, "text": " when I was
  reading this article, there was probably some license which said you can", "tokens":
  [50692, 562, 286, 390, 3760, 341, 7222, 11, 456, 390, 1391, 512, 10476, 597, 848,
  291, 393, 50904], "temperature": 0.0, "avg_logprob": -0.20279652731759207, "compression_ratio":
  1.7056603773584906, "no_speech_prob": 0.009502504952251911}, {"id": 249, "seek":
  155364, "start": 1564.44, "end": 1570.1200000000001, "text": " not, you can do this,
  but not this, maybe there is something hidden, right? But only now we started",
  "tokens": [50904, 406, 11, 291, 393, 360, 341, 11, 457, 406, 341, 11, 1310, 456,
  307, 746, 7633, 11, 558, 30, 583, 787, 586, 321, 1409, 51188], "temperature": 0.0,
  "avg_logprob": -0.20279652731759207, "compression_ratio": 1.7056603773584906, "no_speech_prob":
  0.009502504952251911}, {"id": 250, "seek": 155364, "start": 1570.1200000000001,
  "end": 1575.48, "text": " discussing these things, right? And that''s very interesting
  topic, but do you think that,", "tokens": [51188, 10850, 613, 721, 11, 558, 30,
  400, 300, 311, 588, 1880, 4829, 11, 457, 360, 291, 519, 300, 11, 51456], "temperature":
  0.0, "avg_logprob": -0.20279652731759207, "compression_ratio": 1.7056603773584906,
  "no_speech_prob": 0.009502504952251911}, {"id": 251, "seek": 155364, "start": 1576.76,
  "end": 1582.5200000000002, "text": " you know, when the companies will be, let''s
  say, they have open source to model and they have", "tokens": [51520, 291, 458,
  11, 562, 264, 3431, 486, 312, 11, 718, 311, 584, 11, 436, 362, 1269, 4009, 281,
  2316, 293, 436, 362, 51808], "temperature": 0.0, "avg_logprob": -0.20279652731759207,
  "compression_ratio": 1.7056603773584906, "no_speech_prob": 0.009502504952251911},
  {"id": 252, "seek": 158364, "start": 1583.64, "end": 1591.5600000000002, "text":
  " checked everything on that manifesto or on that contract. Do you think that there
  will be still a", "tokens": [50364, 10033, 1203, 322, 300, 10067, 78, 420, 322,
  300, 4364, 13, 1144, 291, 519, 300, 456, 486, 312, 920, 257, 50760], "temperature":
  0.0, "avg_logprob": -0.17116400689789743, "compression_ratio": 1.5736842105263158,
  "no_speech_prob": 0.0038147710729390383}, {"id": 253, "seek": 158364, "start": 1591.5600000000002,
  "end": 1598.92, "text": " need for some maybe tooling or some process to kind of
  continuously maintain the status of this", "tokens": [50760, 643, 337, 512, 1310,
  46593, 420, 512, 1399, 281, 733, 295, 15684, 6909, 264, 6558, 295, 341, 51128],
  "temperature": 0.0, "avg_logprob": -0.17116400689789743, "compression_ratio": 1.5736842105263158,
  "no_speech_prob": 0.0038147710729390383}, {"id": 254, "seek": 158364, "start": 1598.92,
  "end": 1605.8000000000002, "text": " model as open source because it may well happen
  that, you know, either the company or research institute,", "tokens": [51128, 2316,
  382, 1269, 4009, 570, 309, 815, 731, 1051, 300, 11, 291, 458, 11, 2139, 264, 2237,
  420, 2132, 26860, 11, 51472], "temperature": 0.0, "avg_logprob": -0.17116400689789743,
  "compression_ratio": 1.5736842105263158, "no_speech_prob": 0.0038147710729390383},
  {"id": 255, "seek": 160580, "start": 1605.8, "end": 1613.0, "text": " they go and
  accidentally use some data that doesn''t anymore confirm, confirm, like,", "tokens":
  [50364, 436, 352, 293, 15715, 764, 512, 1412, 300, 1177, 380, 3602, 9064, 11, 9064,
  11, 411, 11, 50724], "temperature": 0.0, "avg_logprob": -0.27423079470370676, "compression_ratio":
  1.6017316017316017, "no_speech_prob": 0.024271303787827492}, {"id": 256, "seek":
  160580, "start": 1613.0, "end": 1619.56, "text": " comply with this contract, right?
  First of all, without other lands, do you think such thing", "tokens": [50724, 27956,
  365, 341, 4364, 11, 558, 30, 2386, 295, 439, 11, 1553, 661, 5949, 11, 360, 291,
  519, 1270, 551, 51052], "temperature": 0.0, "avg_logprob": -0.27423079470370676,
  "compression_ratio": 1.6017316017316017, "no_speech_prob": 0.024271303787827492},
  {"id": 257, "seek": 160580, "start": 1619.56, "end": 1626.52, "text": " exists,
  would say, for Apache Solar or you see that no one will find a library that is not
  the", "tokens": [51052, 8198, 11, 576, 584, 11, 337, 46597, 22385, 420, 291, 536,
  300, 572, 472, 486, 915, 257, 6405, 300, 307, 406, 264, 51400], "temperature": 0.0,
  "avg_logprob": -0.27423079470370676, "compression_ratio": 1.6017316017316017, "no_speech_prob":
  0.024271303787827492}, {"id": 258, "seek": 160580, "start": 1626.52, "end": 1632.04,
  "text": " license that it has to be, plugs it in and we do a release of you seeing
  a solar. I think there is", "tokens": [51400, 10476, 300, 309, 575, 281, 312, 11,
  33899, 309, 294, 293, 321, 360, 257, 4374, 295, 291, 2577, 257, 7936, 13, 286, 519,
  456, 307, 51676], "temperature": 0.0, "avg_logprob": -0.27423079470370676, "compression_ratio":
  1.6017316017316017, "no_speech_prob": 0.024271303787827492}, {"id": 259, "seek":
  163204, "start": 1632.04, "end": 1639.08, "text": " some checker, right? Yeah. So
  these applies to certain extent to code as well, right? So you", "tokens": [50364,
  512, 1520, 260, 11, 558, 30, 865, 13, 407, 613, 13165, 281, 1629, 8396, 281, 3089,
  382, 731, 11, 558, 30, 407, 291, 50716], "temperature": 0.0, "avg_logprob": -0.2993272997669338,
  "compression_ratio": 1.5601659751037344, "no_speech_prob": 0.012124263681471348},
  {"id": 260, "seek": 163204, "start": 1639.08, "end": 1645.72, "text": " are a contributor.
  When you sign basically the, let''s say contract with the Apache Solar", "tokens":
  [50716, 366, 257, 42859, 13, 1133, 291, 1465, 1936, 264, 11, 718, 311, 584, 4364,
  365, 264, 46597, 22385, 51048], "temperature": 0.0, "avg_logprob": -0.2993272997669338,
  "compression_ratio": 1.5601659751037344, "no_speech_prob": 0.012124263681471348},
  {"id": 261, "seek": 163204, "start": 1645.72, "end": 1651.6399999999999, "text":
  " Foundation, you are sure that any kind of contribution you do is your own. So
  there''s not", "tokens": [51048, 10335, 11, 291, 366, 988, 300, 604, 733, 295, 13150,
  291, 360, 307, 428, 1065, 13, 407, 456, 311, 406, 51344], "temperature": 0.0, "avg_logprob":
  -0.2993272997669338, "compression_ratio": 1.5601659751037344, "no_speech_prob":
  0.012124263681471348}, {"id": 262, "seek": 163204, "start": 1651.6399999999999,
  "end": 1656.76, "text": " being COVID, for example, that was not COVID-rided and
  the sort of thing. It''s genuinely created by you.", "tokens": [51344, 885, 4566,
  11, 337, 1365, 11, 300, 390, 406, 4566, 12, 81, 2112, 293, 264, 1333, 295, 551,
  13, 467, 311, 17839, 2942, 538, 291, 13, 51600], "temperature": 0.0, "avg_logprob":
  -0.2993272997669338, "compression_ratio": 1.5601659751037344, "no_speech_prob":
  0.012124263681471348}, {"id": 263, "seek": 165676, "start": 1656.76, "end": 1663.72,
  "text": " It''s genuinely created by you. So to certain extent, that would be a
  similar thing to", "tokens": [50364, 467, 311, 17839, 2942, 538, 291, 13, 407, 281,
  1629, 8396, 11, 300, 576, 312, 257, 2531, 551, 281, 50712], "temperature": 0.0,
  "avg_logprob": -0.2459466912773218, "compression_ratio": 1.7264150943396226, "no_speech_prob":
  0.008565830998122692}, {"id": 264, "seek": 165676, "start": 1664.28, "end": 1670.04,
  "text": " potentially add some training data. I think probably it''s a little bit
  less likely that", "tokens": [50740, 7263, 909, 512, 3097, 1412, 13, 286, 519, 1391,
  309, 311, 257, 707, 857, 1570, 3700, 300, 51028], "temperature": 0.0, "avg_logprob":
  -0.2459466912773218, "compression_ratio": 1.7264150943396226, "no_speech_prob":
  0.008565830998122692}, {"id": 265, "seek": 165676, "start": 1670.04, "end": 1674.92,
  "text": " like in an existing large-language model, for example, someone would contribute
  a little more", "tokens": [51028, 411, 294, 364, 6741, 2416, 12, 25241, 20473, 2316,
  11, 337, 1365, 11, 1580, 576, 10586, 257, 707, 544, 51272], "temperature": 0.0,
  "avg_logprob": -0.2459466912773218, "compression_ratio": 1.7264150943396226, "no_speech_prob":
  0.008565830998122692}, {"id": 266, "seek": 165676, "start": 1674.92, "end": 1679.8,
  "text": " data. I mean, it''s more likely that maybe you you would change a little
  bit the code, for example,", "tokens": [51272, 1412, 13, 286, 914, 11, 309, 311,
  544, 3700, 300, 1310, 291, 291, 576, 1319, 257, 707, 857, 264, 3089, 11, 337, 1365,
  11, 51516], "temperature": 0.0, "avg_logprob": -0.2459466912773218, "compression_ratio":
  1.7264150943396226, "no_speech_prob": 0.008565830998122692}, {"id": 267, "seek":
  167980, "start": 1679.8, "end": 1687.08, "text": " responsible of fine tuning and
  it sort of things. But still, I think there will be this layer of", "tokens": [50364,
  6250, 295, 2489, 15164, 293, 309, 1333, 295, 721, 13, 583, 920, 11, 286, 519, 456,
  486, 312, 341, 4583, 295, 50728], "temperature": 0.0, "avg_logprob": -0.3745559345592152,
  "compression_ratio": 1.651063829787234, "no_speech_prob": 0.012674327939748764},
  {"id": 268, "seek": 167980, "start": 1687.08, "end": 1693.6399999999999, "text":
  " responsibility that wouldn''t wait on the shoulders of the contributors because
  of course, you kind of", "tokens": [50728, 6357, 300, 2759, 380, 1699, 322, 264,
  10245, 295, 264, 45627, 570, 295, 1164, 11, 291, 733, 295, 51056], "temperature":
  0.0, "avg_logprob": -0.3745559345592152, "compression_ratio": 1.651063829787234,
  "no_speech_prob": 0.012674327939748764}, {"id": 269, "seek": 167980, "start": 1693.6399999999999,
  "end": 1701.8799999999999, "text": " have control on these single individuals. And
  you need to have like this sort of layer where the", "tokens": [51056, 362, 1969,
  322, 613, 2167, 5346, 13, 400, 291, 643, 281, 362, 411, 341, 1333, 295, 4583, 689,
  264, 51468], "temperature": 0.0, "avg_logprob": -0.3745559345592152, "compression_ratio":
  1.651063829787234, "no_speech_prob": 0.012674327939748764}, {"id": 270, "seek":
  167980, "start": 1701.8799999999999, "end": 1708.2, "text": " no-profit, the Schopen
  source project protects itself from. Yeah. Because I can imagine that", "tokens":
  [51468, 572, 12, 14583, 11, 264, 2065, 15752, 4009, 1716, 22583, 2564, 490, 13,
  865, 13, 1436, 286, 393, 3811, 300, 51784], "temperature": 0.0, "avg_logprob": -0.3745559345592152,
  "compression_ratio": 1.651063829787234, "no_speech_prob": 0.012674327939748764},
  {"id": 271, "seek": 170820, "start": 1708.2, "end": 1713.48, "text": " again, it''s
  probably putting it to extremes, but there could be eventually some tooling where",
  "tokens": [50364, 797, 11, 309, 311, 1391, 3372, 309, 281, 41119, 11, 457, 456,
  727, 312, 4728, 512, 46593, 689, 50628], "temperature": 0.0, "avg_logprob": -0.14282908682095802,
  "compression_ratio": 1.7017543859649122, "no_speech_prob": 0.011533819139003754},
  {"id": 272, "seek": 170820, "start": 1713.48, "end": 1718.68, "text": " you take
  the model and you introspect its behavior and you can make a guess on which data
  it was", "tokens": [50628, 291, 747, 264, 2316, 293, 291, 560, 28713, 1080, 5223,
  293, 291, 393, 652, 257, 2041, 322, 597, 1412, 309, 390, 50888], "temperature":
  0.0, "avg_logprob": -0.14282908682095802, "compression_ratio": 1.7017543859649122,
  "no_speech_prob": 0.011533819139003754}, {"id": 273, "seek": 170820, "start": 1718.68,
  "end": 1723.56, "text": " trained. Potentially. Or at least find some similarities
  with how it produces. I mean, there", "tokens": [50888, 8895, 13, 9145, 3137, 13,
  1610, 412, 1935, 915, 512, 24197, 365, 577, 309, 14725, 13, 286, 914, 11, 456, 51132],
  "temperature": 0.0, "avg_logprob": -0.14282908682095802, "compression_ratio": 1.7017543859649122,
  "no_speech_prob": 0.011533819139003754}, {"id": 274, "seek": 170820, "start": 1723.56,
  "end": 1729.96, "text": " been some attacks, so to say, right? So you can actually
  probe the model and see what it outputs,", "tokens": [51132, 668, 512, 8122, 11,
  370, 281, 584, 11, 558, 30, 407, 291, 393, 767, 22715, 264, 2316, 293, 536, 437,
  309, 23930, 11, 51452], "temperature": 0.0, "avg_logprob": -0.14282908682095802,
  "compression_ratio": 1.7017543859649122, "no_speech_prob": 0.011533819139003754},
  {"id": 275, "seek": 170820, "start": 1729.96, "end": 1735.64, "text": " right? You
  can even break some models sometimes. That''s true. So that''s more like on the
  hacker side or", "tokens": [51452, 558, 30, 509, 393, 754, 1821, 512, 5245, 2171,
  13, 663, 311, 2074, 13, 407, 300, 311, 544, 411, 322, 264, 38155, 1252, 420, 51736],
  "temperature": 0.0, "avg_logprob": -0.14282908682095802, "compression_ratio": 1.7017543859649122,
  "no_speech_prob": 0.011533819139003754}, {"id": 276, "seek": 173564, "start": 1736.2,
  "end": 1741.96, "text": " the the bad hacker side. But I mean, there probably will
  be tooling. Do you think it''s possible that", "tokens": [50392, 264, 264, 1578,
  38155, 1252, 13, 583, 286, 914, 11, 456, 1391, 486, 312, 46593, 13, 1144, 291, 519,
  309, 311, 1944, 300, 50680], "temperature": 0.0, "avg_logprob": -0.16953527927398682,
  "compression_ratio": 1.6638655462184875, "no_speech_prob": 0.001762103638611734},
  {"id": 277, "seek": 173564, "start": 1741.96, "end": 1747.16, "text": " there will
  be tooling kind of checking the model and and making some hypothesis. And as you
  said,", "tokens": [50680, 456, 486, 312, 46593, 733, 295, 8568, 264, 2316, 293,
  293, 1455, 512, 17291, 13, 400, 382, 291, 848, 11, 50940], "temperature": 0.0, "avg_logprob":
  -0.16953527927398682, "compression_ratio": 1.6638655462184875, "no_speech_prob":
  0.001762103638611734}, {"id": 278, "seek": 173564, "start": 1747.88, "end": 1754.8400000000001,
  "text": " once caught, that organization will kind of lose its trust, right? So
  obviously, everyone wants to be", "tokens": [50976, 1564, 5415, 11, 300, 4475, 486,
  733, 295, 3624, 1080, 3361, 11, 558, 30, 407, 2745, 11, 1518, 2738, 281, 312, 51324],
  "temperature": 0.0, "avg_logprob": -0.16953527927398682, "compression_ratio": 1.6638655462184875,
  "no_speech_prob": 0.001762103638611734}, {"id": 279, "seek": 173564, "start": 1754.8400000000001,
  "end": 1760.44, "text": " kind of accountable and so on. But then there could be
  a flip side of that that you can kind of", "tokens": [51324, 733, 295, 18024, 293,
  370, 322, 13, 583, 550, 456, 727, 312, 257, 7929, 1252, 295, 300, 300, 291, 393,
  733, 295, 51604], "temperature": 0.0, "avg_logprob": -0.16953527927398682, "compression_ratio":
  1.6638655462184875, "no_speech_prob": 0.001762103638611734}, {"id": 280, "seek":
  176044, "start": 1761.16, "end": 1769.3200000000002, "text": " accidentally assume
  that they did it, but that''s not true, right? Now that becomes a very hard", "tokens":
  [50400, 15715, 6552, 300, 436, 630, 309, 11, 457, 300, 311, 406, 2074, 11, 558,
  30, 823, 300, 3643, 257, 588, 1152, 50808], "temperature": 0.0, "avg_logprob": -0.25752168231540257,
  "compression_ratio": 1.471502590673575, "no_speech_prob": 0.002589970361441374},
  {"id": 281, "seek": 176044, "start": 1769.3200000000002, "end": 1778.76, "text":
  " debate, right? So it''s an area which I think deserves exploration and study.
  And I believe that''s", "tokens": [50808, 7958, 11, 558, 30, 407, 309, 311, 364,
  1859, 597, 286, 519, 17037, 16197, 293, 2979, 13, 400, 286, 1697, 300, 311, 51280],
  "temperature": 0.0, "avg_logprob": -0.25752168231540257, "compression_ratio": 1.471502590673575,
  "no_speech_prob": 0.002589970361441374}, {"id": 282, "seek": 176044, "start": 1780.6000000000001,
  "end": 1787.16, "text": " being accountable of like the data you use and disclosing
  it, of course, is the first step.", "tokens": [51372, 885, 18024, 295, 411, 264,
  1412, 291, 764, 293, 17092, 6110, 309, 11, 295, 1164, 11, 307, 264, 700, 1823, 13,
  51700], "temperature": 0.0, "avg_logprob": -0.25752168231540257, "compression_ratio":
  1.471502590673575, "no_speech_prob": 0.002589970361441374}, {"id": 283, "seek":
  178716, "start": 1787.8000000000002, "end": 1793.96, "text": " But then also validating
  that companies send the truth, for example, I think it''s going to be", "tokens":
  [50396, 583, 550, 611, 7363, 990, 300, 3431, 2845, 264, 3494, 11, 337, 1365, 11,
  286, 519, 309, 311, 516, 281, 312, 50704], "temperature": 0.0, "avg_logprob": -0.2601023244333791,
  "compression_ratio": 1.5458333333333334, "no_speech_prob": 0.05368422344326973},
  {"id": 284, "seek": 178716, "start": 1793.96, "end": 1801.24, "text": " important
  to build trust and to make sure that what you display is actually what happens.",
  "tokens": [50704, 1021, 281, 1322, 3361, 293, 281, 652, 988, 300, 437, 291, 4674,
  307, 767, 437, 2314, 13, 51068], "temperature": 0.0, "avg_logprob": -0.2601023244333791,
  "compression_ratio": 1.5458333333333334, "no_speech_prob": 0.05368422344326973},
  {"id": 285, "seek": 178716, "start": 1801.72, "end": 1807.64, "text": " Because
  we never know. It''s very interesting. Was there some other topic you wanted to
  cover?", "tokens": [51092, 1436, 321, 1128, 458, 13, 467, 311, 588, 1880, 13, 3027,
  456, 512, 661, 4829, 291, 1415, 281, 2060, 30, 51388], "temperature": 0.0, "avg_logprob":
  -0.2601023244333791, "compression_ratio": 1.5458333333333334, "no_speech_prob":
  0.05368422344326973}, {"id": 286, "seek": 178716, "start": 1807.64, "end": 1815.5600000000002,
  "text": " I mean, are you also working on Raga or anything of that or evaluating
  the LLAM based search?", "tokens": [51388, 286, 914, 11, 366, 291, 611, 1364, 322,
  497, 9286, 420, 1340, 295, 300, 420, 27479, 264, 441, 43, 2865, 2361, 3164, 30,
  51784], "temperature": 0.0, "avg_logprob": -0.2601023244333791, "compression_ratio":
  1.5458333333333334, "no_speech_prob": 0.05368422344326973}, {"id": 287, "seek":
  181556, "start": 1815.56, "end": 1820.76, "text": " We are working on many different
  integration with LLAM models. Retriol passage generation is one", "tokens": [50364,
  492, 366, 1364, 322, 867, 819, 10980, 365, 441, 43, 2865, 5245, 13, 11495, 470,
  401, 11497, 5125, 307, 472, 50624], "temperature": 0.0, "avg_logprob": -0.3106827069354314,
  "compression_ratio": 1.606694560669456, "no_speech_prob": 0.0042394609190523624},
  {"id": 288, "seek": 181556, "start": 1820.76, "end": 1826.6, "text": " of it. Nugro
  language parsing, for example, is another so moving from Nugro language to structured",
  "tokens": [50624, 295, 309, 13, 426, 697, 340, 2856, 21156, 278, 11, 337, 1365,
  11, 307, 1071, 370, 2684, 490, 426, 697, 340, 2856, 281, 18519, 50916], "temperature":
  0.0, "avg_logprob": -0.3106827069354314, "compression_ratio": 1.606694560669456,
  "no_speech_prob": 0.0042394609190523624}, {"id": 289, "seek": 181556, "start": 1826.6,
  "end": 1832.44, "text": " queries. Yeah. Probably the last thing we can discuss,
  the last topic we can discuss is prompt", "tokens": [50916, 24109, 13, 865, 13,
  9210, 264, 1036, 551, 321, 393, 2248, 11, 264, 1036, 4829, 321, 393, 2248, 307,
  12391, 51208], "temperature": 0.0, "avg_logprob": -0.3106827069354314, "compression_ratio":
  1.606694560669456, "no_speech_prob": 0.0042394609190523624}, {"id": 290, "seek":
  181556, "start": 1832.44, "end": 1838.9199999999998, "text": " engineering. Yeah.
  Briefly, because yes, it''s this naming convention is something that really", "tokens":
  [51208, 7043, 13, 865, 13, 39805, 356, 11, 570, 2086, 11, 309, 311, 341, 25290,
  10286, 307, 746, 300, 534, 51532], "temperature": 0.0, "avg_logprob": -0.3106827069354314,
  "compression_ratio": 1.606694560669456, "no_speech_prob": 0.0042394609190523624},
  {"id": 291, "seek": 183892, "start": 1838.92, "end": 1844.28, "text": " hurts me
  because it''s not engineering at all in my opinion because you''re just attempting
  to", "tokens": [50364, 11051, 385, 570, 309, 311, 406, 7043, 412, 439, 294, 452,
  4800, 570, 291, 434, 445, 22001, 281, 50632], "temperature": 0.0, "avg_logprob":
  -0.2131224782843339, "compression_ratio": 1.7142857142857142, "no_speech_prob":
  0.02166379988193512}, {"id": 292, "seek": 183892, "start": 1844.28, "end": 1851.0800000000002,
  "text": " communicate with something and you don''t know what to expect. Because
  I''ve seen, I mean, I''ve seen", "tokens": [50632, 7890, 365, 746, 293, 291, 500,
  380, 458, 437, 281, 2066, 13, 1436, 286, 600, 1612, 11, 286, 914, 11, 286, 600,
  1612, 50972], "temperature": 0.0, "avg_logprob": -0.2131224782843339, "compression_ratio":
  1.7142857142857142, "no_speech_prob": 0.02166379988193512}, {"id": 293, "seek":
  183892, "start": 1851.0800000000002, "end": 1857.88, "text": " tools today with
  people saying, you write this prompt and you hope you get this response. Yeah.",
  "tokens": [50972, 3873, 965, 365, 561, 1566, 11, 291, 2464, 341, 12391, 293, 291,
  1454, 291, 483, 341, 4134, 13, 865, 13, 51312], "temperature": 0.0, "avg_logprob":
  -0.2131224782843339, "compression_ratio": 1.7142857142857142, "no_speech_prob":
  0.02166379988193512}, {"id": 294, "seek": 183892, "start": 1857.88, "end": 1863.8000000000002,
  "text": " You type this prompt and you ask, please give me the response. She is,
  to me, something that is,", "tokens": [51312, 509, 2010, 341, 12391, 293, 291, 1029,
  11, 1767, 976, 385, 264, 4134, 13, 1240, 307, 11, 281, 385, 11, 746, 300, 307, 11,
  51608], "temperature": 0.0, "avg_logprob": -0.2131224782843339, "compression_ratio":
  1.7142857142857142, "no_speech_prob": 0.02166379988193512}, {"id": 295, "seek":
  186380, "start": 1864.2, "end": 1869.3999999999999, "text": " not scientific at
  all. It''s not scientific. It''s not scientific. It''s not science. You can''t just",
  "tokens": [50384, 406, 8134, 412, 439, 13, 467, 311, 406, 8134, 13, 467, 311, 406,
  8134, 13, 467, 311, 406, 3497, 13, 509, 393, 380, 445, 50644], "temperature": 0.0,
  "avg_logprob": -0.3429580373862355, "compression_ratio": 1.7370892018779343, "no_speech_prob":
  0.05421893671154976}, {"id": 296, "seek": 186380, "start": 1869.3999999999999, "end":
  1875.96, "text": " be comfortable. Yeah, you can be comfortable. Yeah. So there''s,
  in my opinion, just to give", "tokens": [50644, 312, 4619, 13, 865, 11, 291, 393,
  312, 4619, 13, 865, 13, 407, 456, 311, 11, 294, 452, 4800, 11, 445, 281, 976, 50972],
  "temperature": 0.0, "avg_logprob": -0.3429580373862355, "compression_ratio": 1.7370892018779343,
  "no_speech_prob": 0.05421893671154976}, {"id": 297, "seek": 186380, "start": 1875.96,
  "end": 1884.12, "text": " you short, a big margin of improvement there to interact
  with LLAM in a more program idea.", "tokens": [50972, 291, 2099, 11, 257, 955, 10270,
  295, 10444, 456, 281, 4648, 365, 441, 43, 2865, 294, 257, 544, 1461, 1558, 13, 51380],
  "temperature": 0.0, "avg_logprob": -0.3429580373862355, "compression_ratio": 1.7370892018779343,
  "no_speech_prob": 0.05421893671154976}, {"id": 298, "seek": 186380, "start": 1885.24,
  "end": 1891.8799999999999, "text": " I want to specify it as with rules and get
  back a response that satisfies those rules. If", "tokens": [51436, 286, 528, 281,
  16500, 309, 382, 365, 4474, 293, 483, 646, 257, 4134, 300, 44271, 729, 4474, 13,
  759, 51768], "temperature": 0.0, "avg_logprob": -0.3429580373862355, "compression_ratio":
  1.7370892018779343, "no_speech_prob": 0.05421893671154976}, {"id": 299, "seek":
  189188, "start": 1891.88, "end": 1896.5200000000002, "text": " I want to select
  an item from a list, I want to select an item from the list. I wonder", "tokens":
  [50364, 286, 528, 281, 3048, 364, 3174, 490, 257, 1329, 11, 286, 528, 281, 3048,
  364, 3174, 490, 264, 1329, 13, 286, 2441, 50596], "temperature": 0.0, "avg_logprob":
  -0.22088693633792908, "compression_ratio": 1.9572649572649572, "no_speech_prob":
  0.019875723868608475}, {"id": 300, "seek": 189188, "start": 1896.5200000000002,
  "end": 1902.1200000000001, "text": " LLAM is more than to be able to just select
  the item from the list. I''m not 80% of the time,", "tokens": [50596, 441, 43, 2865,
  307, 544, 813, 281, 312, 1075, 281, 445, 3048, 264, 3174, 490, 264, 1329, 13, 286,
  478, 406, 4688, 4, 295, 264, 565, 11, 50876], "temperature": 0.0, "avg_logprob":
  -0.22088693633792908, "compression_ratio": 1.9572649572649572, "no_speech_prob":
  0.019875723868608475}, {"id": 301, "seek": 189188, "start": 1902.1200000000001,
  "end": 1907.0800000000002, "text": " select the item on the list and 20% of the
  time, select the item and give me an explanation.", "tokens": [50876, 3048, 264,
  3174, 322, 264, 1329, 293, 945, 4, 295, 264, 565, 11, 3048, 264, 3174, 293, 976,
  385, 364, 10835, 13, 51124], "temperature": 0.0, "avg_logprob": -0.22088693633792908,
  "compression_ratio": 1.9572649572649572, "no_speech_prob": 0.019875723868608475},
  {"id": 302, "seek": 189188, "start": 1907.96, "end": 1914.44, "text": " I just wanted
  the item from the list. Yeah. And right now, I''ve seen, and we will see", "tokens":
  [51168, 286, 445, 1415, 264, 3174, 490, 264, 1329, 13, 865, 13, 400, 558, 586, 11,
  286, 600, 1612, 11, 293, 321, 486, 536, 51492], "temperature": 0.0, "avg_logprob":
  -0.22088693633792908, "compression_ratio": 1.9572649572649572, "no_speech_prob":
  0.019875723868608475}, {"id": 303, "seek": 189188, "start": 1914.44, "end": 1919.0,
  "text": " the conference because I''ve seen in the agenda, there are a lot of many
  talks about trying to solve", "tokens": [51492, 264, 7586, 570, 286, 600, 1612,
  294, 264, 9829, 11, 456, 366, 257, 688, 295, 867, 6686, 466, 1382, 281, 5039, 51720],
  "temperature": 0.0, "avg_logprob": -0.22088693633792908, "compression_ratio": 1.9572649572649572,
  "no_speech_prob": 0.019875723868608475}, {"id": 304, "seek": 191900, "start": 1919.08,
  "end": 1925.72, "text": " this problem. But right now, what I''ve seen as a possible
  solution is just like you post validates", "tokens": [50368, 341, 1154, 13, 583,
  558, 586, 11, 437, 286, 600, 1612, 382, 257, 1944, 3827, 307, 445, 411, 291, 2183,
  7363, 1024, 50700], "temperature": 0.0, "avg_logprob": -0.22727550677399136, "compression_ratio":
  1.7025089605734767, "no_speech_prob": 0.02385595068335533}, {"id": 305, "seek":
  191900, "start": 1926.52, "end": 1932.52, "text": " the response and you go back.
  Like, okay, yeah, I asked for a specific JSON in the response.", "tokens": [50740,
  264, 4134, 293, 291, 352, 646, 13, 1743, 11, 1392, 11, 1338, 11, 286, 2351, 337,
  257, 2685, 31828, 294, 264, 4134, 13, 51040], "temperature": 0.0, "avg_logprob":
  -0.22727550677399136, "compression_ratio": 1.7025089605734767, "no_speech_prob":
  0.02385595068335533}, {"id": 306, "seek": 191900, "start": 1932.52, "end": 1938.92,
  "text": " There are mistakes. It''s like, it''s not a possible JSON. I say, I go
  back to the LLAM and I say,", "tokens": [51040, 821, 366, 8038, 13, 467, 311, 411,
  11, 309, 311, 406, 257, 1944, 31828, 13, 286, 584, 11, 286, 352, 646, 281, 264,
  441, 43, 2865, 293, 286, 584, 11, 51360], "temperature": 0.0, "avg_logprob": -0.22727550677399136,
  "compression_ratio": 1.7025089605734767, "no_speech_prob": 0.02385595068335533},
  {"id": 307, "seek": 191900, "start": 1938.92, "end": 1943.48, "text": " this is
  not a possible JSON. Can you fix it? And again, and again, and again, which is not
  really", "tokens": [51360, 341, 307, 406, 257, 1944, 31828, 13, 1664, 291, 3191,
  309, 30, 400, 797, 11, 293, 797, 11, 293, 797, 11, 597, 307, 406, 534, 51588], "temperature":
  0.0, "avg_logprob": -0.22727550677399136, "compression_ratio": 1.7025089605734767,
  "no_speech_prob": 0.02385595068335533}, {"id": 308, "seek": 191900, "start": 1943.48,
  "end": 1948.6, "text": " something you want to go to production. So in short, in
  my opinion, like using LLAM with", "tokens": [51588, 746, 291, 528, 281, 352, 281,
  4265, 13, 407, 294, 2099, 11, 294, 452, 4800, 11, 411, 1228, 441, 43, 2865, 365,
  51844], "temperature": 0.0, "avg_logprob": -0.22727550677399136, "compression_ratio":
  1.7025089605734767, "no_speech_prob": 0.02385595068335533}, {"id": 309, "seek":
  194860, "start": 1948.6, "end": 1954.6799999999998, "text": " models, program, I
  right now is full for approval concepts. But would I bring to production like",
  "tokens": [50364, 5245, 11, 1461, 11, 286, 558, 586, 307, 1577, 337, 13317, 10392,
  13, 583, 576, 286, 1565, 281, 4265, 411, 50668], "temperature": 0.0, "avg_logprob":
  -0.3336199788213934, "compression_ratio": 1.5872340425531914, "no_speech_prob":
  0.008671130985021591}, {"id": 310, "seek": 194860, "start": 1955.1599999999999,
  "end": 1959.56, "text": " out of the box like these sort of approaches? I want,
  because I wouldn''t, you know,", "tokens": [50692, 484, 295, 264, 2424, 411, 613,
  1333, 295, 11587, 30, 286, 528, 11, 570, 286, 2759, 380, 11, 291, 458, 11, 50912],
  "temperature": 0.0, "avg_logprob": -0.3336199788213934, "compression_ratio": 1.5872340425531914,
  "no_speech_prob": 0.008671130985021591}, {"id": 311, "seek": 194860, "start": 1959.56,
  "end": 1967.3999999999999, "text": " brings, I want to bring something that is deterministic.
  Yeah. It does what I want to do 100%", "tokens": [50912, 5607, 11, 286, 528, 281,
  1565, 746, 300, 307, 15957, 3142, 13, 865, 13, 467, 775, 437, 286, 528, 281, 360,
  2319, 4, 51304], "temperature": 0.0, "avg_logprob": -0.3336199788213934, "compression_ratio":
  1.5872340425531914, "no_speech_prob": 0.008671130985021591}, {"id": 312, "seek":
  194860, "start": 1967.3999999999999, "end": 1973.32, "text": " of the time. Sometimes.
  And I don''t want to hope. It''s a good thing. Well, I want to make it work.", "tokens":
  [51304, 295, 264, 565, 13, 4803, 13, 400, 286, 500, 380, 528, 281, 1454, 13, 467,
  311, 257, 665, 551, 13, 1042, 11, 286, 528, 281, 652, 309, 589, 13, 51600], "temperature":
  0.0, "avg_logprob": -0.3336199788213934, "compression_ratio": 1.5872340425531914,
  "no_speech_prob": 0.008671130985021591}, {"id": 313, "seek": 197332, "start": 1973.8799999999999,
  "end": 1979.6399999999999, "text": " Yeah, but it''s also like I see it''s very
  interesting topic, by the way, but I also see some level of", "tokens": [50392,
  865, 11, 457, 309, 311, 611, 411, 286, 536, 309, 311, 588, 1880, 4829, 11, 538,
  264, 636, 11, 457, 286, 611, 536, 512, 1496, 295, 50680], "temperature": 0.0, "avg_logprob":
  -0.15326243952700966, "compression_ratio": 1.7136752136752136, "no_speech_prob":
  0.040132369846105576}, {"id": 314, "seek": 197332, "start": 1979.6399999999999,
  "end": 1987.0, "text": " contradiction that to like between non deterministic and
  hallucinating model essentially hallucinating", "tokens": [50680, 34937, 300, 281,
  411, 1296, 2107, 15957, 3142, 293, 35212, 8205, 2316, 4476, 35212, 8205, 51048],
  "temperature": 0.0, "avg_logprob": -0.15326243952700966, "compression_ratio": 1.7136752136752136,
  "no_speech_prob": 0.040132369846105576}, {"id": 315, "seek": 197332, "start": 1987.0,
  "end": 1993.32, "text": " by design because it keeps predicting the terms, right?
  And some level of determinism as you just", "tokens": [51048, 538, 1715, 570, 309,
  5965, 32884, 264, 2115, 11, 558, 30, 400, 512, 1496, 295, 15957, 1434, 382, 291,
  445, 51364], "temperature": 0.0, "avg_logprob": -0.15326243952700966, "compression_ratio":
  1.7136752136752136, "no_speech_prob": 0.040132369846105576}, {"id": 316, "seek":
  197332, "start": 1993.32, "end": 1999.8, "text": " explained, right? But I guess,
  but I guess at the same time, someone might say that our life is not", "tokens":
  [51364, 8825, 11, 558, 30, 583, 286, 2041, 11, 457, 286, 2041, 412, 264, 912, 565,
  11, 1580, 1062, 584, 300, 527, 993, 307, 406, 51688], "temperature": 0.0, "avg_logprob":
  -0.15326243952700966, "compression_ratio": 1.7136752136752136, "no_speech_prob":
  0.040132369846105576}, {"id": 317, "seek": 199980, "start": 1999.8, "end": 2005.8,
  "text": " that deterministic, many moving parts and we still find a way to, I don''t
  know, leave it and then", "tokens": [50364, 300, 15957, 3142, 11, 867, 2684, 3166,
  293, 321, 920, 915, 257, 636, 281, 11, 286, 500, 380, 458, 11, 1856, 309, 293, 550,
  50664], "temperature": 0.0, "avg_logprob": -0.21954883915362972, "compression_ratio":
  1.5659574468085107, "no_speech_prob": 0.004681337624788284}, {"id": 318, "seek":
  199980, "start": 2005.8, "end": 2010.36, "text": " build something, right? Yeah,
  there''s something that moves. I think, you know, it''s the first,", "tokens": [50664,
  1322, 746, 11, 558, 30, 865, 11, 456, 311, 746, 300, 6067, 13, 286, 519, 11, 291,
  458, 11, 309, 311, 264, 700, 11, 50892], "temperature": 0.0, "avg_logprob": -0.21954883915362972,
  "compression_ratio": 1.5659574468085107, "no_speech_prob": 0.004681337624788284},
  {"id": 319, "seek": 199980, "start": 2010.36, "end": 2015.8799999999999, "text":
  " anyway, we are experiencing, in my opinion, at first, that in these new worlds,",
  "tokens": [50892, 4033, 11, 321, 366, 11139, 11, 294, 452, 4800, 11, 412, 700, 11,
  300, 294, 613, 777, 13401, 11, 51168], "temperature": 0.0, "avg_logprob": -0.21954883915362972,
  "compression_ratio": 1.5659574468085107, "no_speech_prob": 0.004681337624788284},
  {"id": 320, "seek": 199980, "start": 2016.52, "end": 2024.28, "text": " of AI big
  models. So I think it''s fair. They were born to auto complete text, to generate
  text.", "tokens": [51200, 295, 7318, 955, 5245, 13, 407, 286, 519, 309, 311, 3143,
  13, 814, 645, 4232, 281, 8399, 3566, 2487, 11, 281, 8460, 2487, 13, 51588], "temperature":
  0.0, "avg_logprob": -0.21954883915362972, "compression_ratio": 1.5659574468085107,
  "no_speech_prob": 0.004681337624788284}, {"id": 321, "seek": 202428, "start": 2024.36,
  "end": 2031.16, "text": " And now we are trying to use them to do tasks. Yes. Which
  is okay. We as humans use language to,", "tokens": [50368, 400, 586, 321, 366, 1382,
  281, 764, 552, 281, 360, 9608, 13, 1079, 13, 3013, 307, 1392, 13, 492, 382, 6255,
  764, 2856, 281, 11, 50708], "temperature": 0.0, "avg_logprob": -0.29556469800995616,
  "compression_ratio": 1.6093189964157706, "no_speech_prob": 0.007484468165785074},
  {"id": 322, "seek": 202428, "start": 2031.72, "end": 2037.56, "text": " to task.
  Yeah. So I just guess, and then we end up with programming. Yes.", "tokens": [50736,
  281, 5633, 13, 865, 13, 407, 286, 445, 2041, 11, 293, 550, 321, 917, 493, 365, 9410,
  13, 1079, 13, 51028], "temperature": 0.0, "avg_logprob": -0.29556469800995616, "compression_ratio":
  1.6093189964157706, "no_speech_prob": 0.007484468165785074}, {"id": 323, "seek":
  202428, "start": 2037.56, "end": 2041.96, "text": " Computers, right? So let''s
  play it in a little bit more that would be programmable. Yeah.", "tokens": [51028,
  37804, 433, 11, 558, 30, 407, 718, 311, 862, 309, 294, 257, 707, 857, 544, 300,
  576, 312, 37648, 712, 13, 865, 13, 51248], "temperature": 0.0, "avg_logprob": -0.29556469800995616,
  "compression_ratio": 1.6093189964157706, "no_speech_prob": 0.007484468165785074},
  {"id": 324, "seek": 202428, "start": 2042.52, "end": 2048.12, "text": " I mean,
  it doesn''t remind a bit. I haven''t explored it, but to mention GSPY, the packaging,",
  "tokens": [51276, 286, 914, 11, 309, 1177, 380, 4160, 257, 857, 13, 286, 2378, 380,
  24016, 309, 11, 457, 281, 2152, 460, 27921, 56, 11, 264, 16836, 11, 51556], "temperature":
  0.0, "avg_logprob": -0.29556469800995616, "compression_ratio": 1.6093189964157706,
  "no_speech_prob": 0.007484468165785074}, {"id": 325, "seek": 202428, "start": 2048.12,
  "end": 2053.0, "text": " probably you heard about it, right? Which replaces the
  prompt engineering with more programmable", "tokens": [51556, 1391, 291, 2198, 466,
  309, 11, 558, 30, 3013, 46734, 264, 12391, 7043, 365, 544, 37648, 712, 51800], "temperature":
  0.0, "avg_logprob": -0.29556469800995616, "compression_ratio": 1.6093189964157706,
  "no_speech_prob": 0.007484468165785074}, {"id": 326, "seek": 205300, "start": 2053.0,
  "end": 2057.48, "text": " sort of way of doing it. I still don''t know how it works,
  but I know that some of the engineers", "tokens": [50364, 1333, 295, 636, 295, 884,
  309, 13, 286, 920, 500, 380, 458, 577, 309, 1985, 11, 457, 286, 458, 300, 512, 295,
  264, 11955, 50588], "temperature": 0.0, "avg_logprob": -0.2574625748854417, "compression_ratio":
  1.59915611814346, "no_speech_prob": 0.006268244236707687}, {"id": 327, "seek": 205300,
  "start": 2057.48, "end": 2064.44, "text": " in my team applied it quite successfully
  to generate some synthetic queries. So that was very", "tokens": [50588, 294, 452,
  1469, 6456, 309, 1596, 10727, 281, 8460, 512, 23420, 24109, 13, 407, 300, 390, 588,
  50936], "temperature": 0.0, "avg_logprob": -0.2574625748854417, "compression_ratio":
  1.59915611814346, "no_speech_prob": 0.006268244236707687}, {"id": 328, "seek": 205300,
  "start": 2064.44, "end": 2071.24, "text": " interesting. Have you played with it?
  Do you know? So my team, we''ve been playing with it for one", "tokens": [50936,
  1880, 13, 3560, 291, 3737, 365, 309, 30, 1144, 291, 458, 30, 407, 452, 1469, 11,
  321, 600, 668, 2433, 365, 309, 337, 472, 51276], "temperature": 0.0, "avg_logprob":
  -0.2574625748854417, "compression_ratio": 1.59915611814346, "no_speech_prob": 0.006268244236707687},
  {"id": 329, "seek": 205300, "start": 2071.24, "end": 2076.36, "text": " of the bros
  of conceptual concepts for doing other language processing, for structure solar",
  "tokens": [51276, 295, 264, 738, 329, 295, 24106, 10392, 337, 884, 661, 2856, 9007,
  11, 337, 3877, 7936, 51532], "temperature": 0.0, "avg_logprob": -0.2574625748854417,
  "compression_ratio": 1.59915611814346, "no_speech_prob": 0.006268244236707687},
  {"id": 330, "seek": 207636, "start": 2076.36, "end": 2085.7200000000003, "text":
  " queries. And I think it''s a nice first step. Still is giving you like an in-direction
  between", "tokens": [50364, 24109, 13, 400, 286, 519, 309, 311, 257, 1481, 700,
  1823, 13, 8291, 307, 2902, 291, 411, 364, 294, 12, 18267, 882, 1296, 50832], "temperature":
  0.0, "avg_logprob": -0.2512031212831155, "compression_ratio": 1.529100529100529,
  "no_speech_prob": 0.017910394817590714}, {"id": 331, "seek": 207636, "start": 2086.28,
  "end": 2094.2000000000003, "text": " the prompt and the way to write a prompt. So
  you have like classes, the mimic, the programming", "tokens": [50860, 264, 12391,
  293, 264, 636, 281, 2464, 257, 12391, 13, 407, 291, 362, 411, 5359, 11, 264, 31075,
  11, 264, 9410, 51256], "temperature": 0.0, "avg_logprob": -0.2512031212831155, "compression_ratio":
  1.529100529100529, "no_speech_prob": 0.017910394817590714}, {"id": 332, "seek":
  207636, "start": 2094.2000000000003, "end": 2100.6800000000003, "text": " language,
  but then ends up as prompt. Yeah. I see. You are not sure that you will get what
  you want.", "tokens": [51256, 2856, 11, 457, 550, 5314, 493, 382, 12391, 13, 865,
  13, 286, 536, 13, 509, 366, 406, 988, 300, 291, 486, 483, 437, 291, 528, 13, 51580],
  "temperature": 0.0, "avg_logprob": -0.2512031212831155, "compression_ratio": 1.529100529100529,
  "no_speech_prob": 0.017910394817590714}, {"id": 333, "seek": 210068, "start": 2101.56,
  "end": 2106.3599999999997, "text": " But it''s a first attempt. Yeah. Yeah. I think
  it''s okay. I mean, we will improve that.", "tokens": [50408, 583, 309, 311, 257,
  700, 5217, 13, 865, 13, 865, 13, 286, 519, 309, 311, 1392, 13, 286, 914, 11, 321,
  486, 3470, 300, 13, 50648], "temperature": 0.0, "avg_logprob": -0.34599586633535534,
  "compression_ratio": 1.6803652968036529, "no_speech_prob": 0.09725619107484818},
  {"id": 334, "seek": 210068, "start": 2106.3599999999997, "end": 2113.08, "text":
  " It feels maybe like maybe first baby step in a way that it''s not a work to the
  state that you mentioned.", "tokens": [50648, 467, 3417, 1310, 411, 1310, 700, 3186,
  1823, 294, 257, 636, 300, 309, 311, 406, 257, 589, 281, 264, 1785, 300, 291, 2835,
  13, 50984], "temperature": 0.0, "avg_logprob": -0.34599586633535534, "compression_ratio":
  1.6803652968036529, "no_speech_prob": 0.09725619107484818}, {"id": 335, "seek":
  210068, "start": 2113.08, "end": 2118.44, "text": " Yeah. That''s not a conflict
  solution, but it''s great. So what''s next that you''re working on?", "tokens":
  [50984, 865, 13, 663, 311, 406, 257, 6596, 3827, 11, 457, 309, 311, 869, 13, 407,
  437, 311, 958, 300, 291, 434, 1364, 322, 30, 51252], "temperature": 0.0, "avg_logprob":
  -0.34599586633535534, "compression_ratio": 1.6803652968036529, "no_speech_prob":
  0.09725619107484818}, {"id": 336, "seek": 210068, "start": 2118.44, "end": 2126.04,
  "text": " That you want to disclose? Yeah. So first of all, I want you to bring
  and merge the", "tokens": [51252, 663, 291, 528, 281, 36146, 30, 865, 13, 407, 700,
  295, 439, 11, 286, 528, 291, 281, 1565, 293, 22183, 264, 51632], "temperature":
  0.0, "avg_logprob": -0.34599586633535534, "compression_ratio": 1.6803652968036529,
  "no_speech_prob": 0.09725619107484818}, {"id": 337, "seek": 212604, "start": 2126.12,
  "end": 2131.48, "text": " hybrid search receiver rank fusion to solar, which is
  coming nine to seven. So I''m very close to", "tokens": [50368, 13051, 3164, 20086,
  6181, 23100, 281, 7936, 11, 597, 307, 1348, 4949, 281, 3407, 13, 407, 286, 478,
  588, 1998, 281, 50636], "temperature": 0.0, "avg_logprob": -0.30727564903997606,
  "compression_ratio": 1.634453781512605, "no_speech_prob": 0.02329128421843052},
  {"id": 338, "seek": 212604, "start": 2131.48, "end": 2138.44, "text": " the men.
  Awesome. For that. We are, we got some funding from the European Union to work on
  solar.", "tokens": [50636, 264, 1706, 13, 10391, 13, 1171, 300, 13, 492, 366, 11,
  321, 658, 512, 6137, 490, 264, 6473, 8133, 281, 589, 322, 7936, 13, 50984], "temperature":
  0.0, "avg_logprob": -0.30727564903997606, "compression_ratio": 1.634453781512605,
  "no_speech_prob": 0.02329128421843052}, {"id": 339, "seek": 212604, "start": 2138.44,
  "end": 2146.12, "text": " So that''s like that. So we''re going to be able to contribute
  more vector-based search capabilities,", "tokens": [50984, 407, 300, 311, 411, 300,
  13, 407, 321, 434, 516, 281, 312, 1075, 281, 10586, 544, 8062, 12, 6032, 3164, 10862,
  11, 51368], "temperature": 0.0, "avg_logprob": -0.30727564903997606, "compression_ratio":
  1.634453781512605, "no_speech_prob": 0.02329128421843052}, {"id": 340, "seek": 212604,
  "start": 2146.12, "end": 2150.84, "text": " better integrations we''ve learned into
  rank, better integration with like inference and points", "tokens": [51368, 1101,
  3572, 763, 321, 600, 3264, 666, 6181, 11, 1101, 10980, 365, 411, 38253, 293, 2793,
  51604], "temperature": 0.0, "avg_logprob": -0.30727564903997606, "compression_ratio":
  1.634453781512605, "no_speech_prob": 0.02329128421843052}, {"id": 341, "seek": 215084,
  "start": 2151.0, "end": 2158.6000000000004, "text": " to make it a little bit more
  transparent. That''s it. And still in the work like multivalued supports", "tokens":
  [50372, 281, 652, 309, 257, 707, 857, 544, 12737, 13, 663, 311, 309, 13, 400, 920,
  294, 264, 589, 411, 2120, 3576, 5827, 9346, 50752], "temperature": 0.0, "avg_logprob":
  -0.2574143608411153, "compression_ratio": 1.7419354838709677, "no_speech_prob":
  0.0034876083955168724}, {"id": 342, "seek": 215084, "start": 2159.48, "end": 2166.04,
  "text": " for vector-based search in solar. And there are like some pieces in losing
  to speed up and", "tokens": [50796, 337, 8062, 12, 6032, 3164, 294, 7936, 13, 400,
  456, 366, 411, 512, 3755, 294, 7027, 281, 3073, 493, 293, 51124], "temperature":
  0.0, "avg_logprob": -0.2574143608411153, "compression_ratio": 1.7419354838709677,
  "no_speech_prob": 0.0034876083955168724}, {"id": 343, "seek": 215084, "start": 2166.04,
  "end": 2172.52, "text": " improve optimized vector-based search that are not yet
  in solar. And that''s among my top", "tokens": [51124, 3470, 26941, 8062, 12, 6032,
  3164, 300, 366, 406, 1939, 294, 7936, 13, 400, 300, 311, 3654, 452, 1192, 51448],
  "temperature": 0.0, "avg_logprob": -0.2574143608411153, "compression_ratio": 1.7419354838709677,
  "no_speech_prob": 0.0034876083955168724}, {"id": 344, "seek": 215084, "start": 2172.52,
  "end": 2177.96, "text": " priority. So this is in short. This is fantastic. This
  is fantastic. And of course, it''s all open", "tokens": [51448, 9365, 13, 407, 341,
  307, 294, 2099, 13, 639, 307, 5456, 13, 639, 307, 5456, 13, 400, 295, 1164, 11,
  309, 311, 439, 1269, 51720], "temperature": 0.0, "avg_logprob": -0.2574143608411153,
  "compression_ratio": 1.7419354838709677, "no_speech_prob": 0.0034876083955168724},
  {"id": 345, "seek": 217796, "start": 2177.96, "end": 2184.92, "text": " source and
  you know, yeah, and then like anyone can join, but maybe we can also make a call
  out and", "tokens": [50364, 4009, 293, 291, 458, 11, 1338, 11, 293, 550, 411, 2878,
  393, 3917, 11, 457, 1310, 321, 393, 611, 652, 257, 818, 484, 293, 50712], "temperature":
  0.0, "avg_logprob": -0.2784245129927848, "compression_ratio": 1.6512605042016806,
  "no_speech_prob": 0.019747542217373848}, {"id": 346, "seek": 217796, "start": 2184.92,
  "end": 2191.96, "text": " say that, I mean, everyone that wants to contribute, you
  know, the more the merrier. Yeah, I actually enjoy", "tokens": [50712, 584, 300,
  11, 286, 914, 11, 1518, 300, 2738, 281, 10586, 11, 291, 458, 11, 264, 544, 264,
  3551, 7326, 13, 865, 11, 286, 767, 2103, 51064], "temperature": 0.0, "avg_logprob":
  -0.2784245129927848, "compression_ratio": 1.6512605042016806, "no_speech_prob":
  0.019747542217373848}, {"id": 347, "seek": 217796, "start": 2191.96, "end": 2200.6,
  "text": " like even though I don''t do solar or only seen today, I am still reading
  the main news. And", "tokens": [51064, 411, 754, 1673, 286, 500, 380, 360, 7936,
  420, 787, 1612, 965, 11, 286, 669, 920, 3760, 264, 2135, 2583, 13, 400, 51496],
  "temperature": 0.0, "avg_logprob": -0.2784245129927848, "compression_ratio": 1.6512605042016806,
  "no_speech_prob": 0.019747542217373848}, {"id": 348, "seek": 217796, "start": 2200.6,
  "end": 2205.4, "text": " and for the most part, I''m reading the lesson one. So
  sometimes I see your discussion as well", "tokens": [51496, 293, 337, 264, 881,
  644, 11, 286, 478, 3760, 264, 6898, 472, 13, 407, 2171, 286, 536, 428, 5017, 382,
  731, 51736], "temperature": 0.0, "avg_logprob": -0.2784245129927848, "compression_ratio":
  1.6512605042016806, "no_speech_prob": 0.019747542217373848}, {"id": 349, "seek":
  220540, "start": 2205.48, "end": 2209.7200000000003, "text": " and you where you
  say, actually, by the way, I''m working on this hybrid search. I did this", "tokens":
  [50368, 293, 291, 689, 291, 584, 11, 767, 11, 538, 264, 636, 11, 286, 478, 1364,
  322, 341, 13051, 3164, 13, 286, 630, 341, 50580], "temperature": 0.0, "avg_logprob":
  -0.209297700361772, "compression_ratio": 1.7269372693726937, "no_speech_prob": 0.01697641797363758},
  {"id": 350, "seek": 220540, "start": 2209.7200000000003, "end": 2216.12, "text":
  " and this. So maybe it will influence you. And I also love the the culture where
  you do not really", "tokens": [50580, 293, 341, 13, 407, 1310, 309, 486, 6503, 291,
  13, 400, 286, 611, 959, 264, 264, 3713, 689, 291, 360, 406, 534, 50900], "temperature":
  0.0, "avg_logprob": -0.209297700361772, "compression_ratio": 1.7269372693726937,
  "no_speech_prob": 0.01697641797363758}, {"id": 351, "seek": 220540, "start": 2216.12,
  "end": 2221.8, "text": " enforce or impose your solution. You just say just for
  you to know, maybe it will be useful. And", "tokens": [50900, 24825, 420, 26952,
  428, 3827, 13, 509, 445, 584, 445, 337, 291, 281, 458, 11, 1310, 309, 486, 312,
  4420, 13, 400, 51184], "temperature": 0.0, "avg_logprob": -0.209297700361772, "compression_ratio":
  1.7269372693726937, "no_speech_prob": 0.01697641797363758}, {"id": 352, "seek":
  220540, "start": 2221.8, "end": 2227.1600000000003, "text": " someone says, yeah,
  awesome. I especially love that that discussion. I forgot the particular topic,",
  "tokens": [51184, 1580, 1619, 11, 1338, 11, 3476, 13, 286, 2318, 959, 300, 300,
  5017, 13, 286, 5298, 264, 1729, 4829, 11, 51452], "temperature": 0.0, "avg_logprob":
  -0.209297700361772, "compression_ratio": 1.7269372693726937, "no_speech_prob": 0.01697641797363758},
  {"id": 353, "seek": 220540, "start": 2227.1600000000003, "end": 2234.12, "text":
  " but I remember it was a recent one. It''s a recent one. So keep up your great
  work.", "tokens": [51452, 457, 286, 1604, 309, 390, 257, 5162, 472, 13, 467, 311,
  257, 5162, 472, 13, 407, 1066, 493, 428, 869, 589, 13, 51800], "temperature": 0.0,
  "avg_logprob": -0.209297700361772, "compression_ratio": 1.7269372693726937, "no_speech_prob":
  0.01697641797363758}, {"id": 354, "seek": 223412, "start": 2234.12, "end": 2239.48,
  "text": " And it''s always a pleasure to talk to you and it looks like it''s a tradition
  that we started", "tokens": [50364, 400, 309, 311, 1009, 257, 6834, 281, 751, 281,
  291, 293, 309, 1542, 411, 309, 311, 257, 6994, 300, 321, 1409, 50632], "temperature":
  0.0, "avg_logprob": -0.5495441436767579, "compression_ratio": 1.3529411764705883,
  "no_speech_prob": 0.12901513278484344}, {"id": 355, "seek": 223412, "start": 2239.48,
  "end": 2245.64, "text": " meeting in the same sort of early flood words. In the
  end now. Yeah, so every two years, we", "tokens": [50632, 3440, 294, 264, 912, 1333,
  295, 2440, 10481, 2283, 13, 682, 264, 917, 586, 13, 865, 11, 370, 633, 732, 924,
  11, 321, 50940], "temperature": 0.0, "avg_logprob": -0.5495441436767579, "compression_ratio":
  1.3529411764705883, "no_speech_prob": 0.12901513278484344}, {"id": 356, "seek":
  224564, "start": 2245.64, "end": 2250.04, "text": " see a lot of people. Yeah, there
  are a lot of people. So fantastic. Thank you so much,", "tokens": [50364, 536, 257,
  688, 295, 561, 13, 865, 11, 456, 366, 257, 688, 295, 561, 13, 407, 5456, 13, 1044,
  291, 370, 709, 11, 50584], "temperature": 0.0, "avg_logprob": -0.9803078969319662,
  "compression_ratio": 1.162162162162162, "no_speech_prob": 0.5407794117927551}, {"id":
  357, "seek": 225004, "start": 2250.04, "end": 2253.4, "text": " LeSando. And anyway,
  my reaction to the conference. Thank you. Thank you.", "tokens": [50364, 1456, 50,
  1806, 13, 400, 4033, 11, 452, 5480, 281, 264, 7586, 13, 1044, 291, 13, 1044, 291,
  13, 50532], "temperature": 0.0, "avg_logprob": -0.6104109504006126, "compression_ratio":
  1.028169014084507, "no_speech_prob": 0.5935039520263672}]'
---

All right, Dr. Podcast and here I have Alessandra Benedetti with me his second time on the podcast actually and exactly about same place we recorded two years ago. I remember on Berlin was works. Yeah, we were here. Yeah, I guess I got 22. It was.
It was by the way a lot no easier if you remember them now but was closing day that we like people. Yeah, but I think it's almost end of day as well here. First day of the conference and yeah, I wanted to chat with you.
How do you like the conference so far? So has been so far like a great conference. We've been seeing like many talks about the language modern integration with search. So that's the biggest new trend.
Vector based search is still quite a strong topic and in general with testing also like evaluation and explainability discussions around like vector based search or in general language models. And and my thoughts was about hybrid search. Hybrid search.
Yeah, so you work a lot on on solar right that's your kind of like playground and that's where you integrate things but also then I heard that like guys at Reddit are using the work that you've been doing also in solar. So that's amazing.
Tell me more a bit more about what is hybrid search right? How do you see it? What's the value? And and basically maybe what are the challenges that you needed to solve and you still see related to hybrid search?
So the first point and the reason I decided to start working a little bit more in hybrid search and contributing this even our rank vision to solar is because of the limitations of vector based search.
So vector based search of course introduces like the ability of closing the semantic gaps with light queries and documents with some some limitations right? So the explainability bar for example is an aspect I care a lot and it's just very difficult to explain vector based search results.
Yeah, we have I dimensional. So many many dimensions in the vectors and humans are not really good in managing many dimensions. We live in a three dimensional world and this even difficult for us to to understand life for dimensional life. Yeah, then we have like many elements in those vectors.
So each feature in the vector doesn't have like a meaning for the humans. So you have like 768 dimensions in your vectors and there's no single dimension that means something semantic. So it's just the output of some machiner model but we can interpret like what it is.
And we can interpret what would happen if that feature goes higher or lower. I mean does a higher value for that feature means higher relevance or not? You can't really do that with vector based search. So these kind of problems. Yeah, start to have like an input. Right.
So you have like your clients using vector based search. They are happy and then they are not and they want to explain for example, yeah, what happens. Yeah, and another limitation is keyword based matching. So by the vector based search try to solve the vocabulary in his best problem.
So if you have terms in your vocabulary that's different from the vocabulary used for queries. Yeah. At the same time, users are used to have keyword matching documents in their response.
So when you don't provide keyword matching document in their response, they're going to be like problems and questions. Yeah. Why do I see this now? And why I don't see for example this title. Oh yeah. So without any search, the idea is to mitigate those problems.
So mix up different query results sets. Potentially like vector based search results and traditional keyword based search results. Yeah. Get back one result set. Yeah. Let's try to combine both words. Interesting.
And if we kind of step forward from this, let's say we deployed hybrid search, so now it basically takes some similar documents from keyword hits and then another one from vector. You still get those documents that do not have keyword matches, right, from the vector space.
Do you know or maybe you have employed some ways of explaining to the user why they see them? So that's an interesting point actually at the discussion recently about how can we explain better by vector based search. So we mentioned already all the problems. We've explained the what can we do bet.
So there are other approaches that just cure dense vector based search such as learned sparse retrieval for example, where you learn query or document expansion term candidates based on learned models. So based on the probability you will expand your queries with additional terms.
So that's a little bit more explainable because at least you get back from the machine learning model alternative terms for the queries and the document. Yeah. It's still a first layer of explainability. So you have some that's like additional concepts. So it's easier to understand.
Still you have the probability assigned to their pair. So if it goes wrong, you may end up with unreasonable terms. So not perfect. A little bit better, maybe a little bit more explainable.
And then there are approaches such callvert where you encode your sentence, not just to just one vector back to a sequence of vectors. So multiple vectors, one pair for an action. And you do the same for your documents.
And then you you basically return results based on the similarity between not just a single query vector and the document vector, but multiple query vectors. So each query at each query vector, which is meant to be probably a term with the terms in the document.
So you may be able to highlight the terms in the document that are close to the terms in the query. Yeah. Also in this case, of course, it's just a first layer of explainability because then if this goes wrong, of course, again, you have sequences of vectors.
So you can get like a sort of itm up of what query terms match is like, more or less the document ones, but still not perfect. Yeah, sure.
Of course, it's kind of like maybe experimentation that is required, right? What works for you? What what what is the end product? But maybe one question is for me as a user, right? Let's say I'm using solar and you offer hybrid search now.
Are you already offering or will you consider at some point offering the capability to ingrain what you just said into let's say highlighter in solar that will it will actually build me the snippet regardless of the source of that document, whether it's keyboard or vector.
That's a very interesting question because there are in my opinion two layers of explainability for engineers. So we need to work on the engine and change the ranking, change the matching and user's equipment. Yeah.
So a user that just want to know why for example, what is there and for user's finability actually, my company, we design and develop the highlighter.
We call the neural highlighter that takes in input the wireless model and in the response, will I like the snippet for each result in documents, not based on let's say on match, but based on the question as a system powered by a level model. Yeah.
So in this way, you will be able to highlight part of the original document that are semantically close to the interesting place. Can you say the name again? What was the name? It's called the neural highlighter. Neural neural highlighter. So it's your proprietary product right now. Yes.
It's a lot of synths, right? Yes. Right now, yes. We may contribute it to a open source integer. I don't know. Right now is one of our products. But I mean, it's a feature that you, is it offered as a standalone component? It's a plugin. It's a plugin. So you ins it's a plugin to pull it.
It's a plugin. That's the value prop as well, right? It doesn't always need to be open. It's something I can plug in and exactly. It takes in input the wireless model. Yeah. It's a response point. So you can write.
So that will help to explain results to the users, right? And you also mentioned, right? It's thanks for doing this distinction, making this distinction that there is also explainability for the engineers that is also important.
So can you a bit explain what you mean? Explainability for the engineers because I care about it a lot of force. But I used to be an engineer full time. And I need to know how, like, how to do it, how to tweak something.
But also, can I explain to myself that what I tweaked is actually the right thing, right? So, you know, kind of the process of engineering the. Yes.
So in solar, for example, there is a debug component that give you the ability to engineer to expand the response with the information about how the score was calculated. So in solar, when you have a query and you have a result, a score is calculated for that result for that query.
And this core will impact the ranking. So, descending order, literally, right from the highest core to the lowest. And normally, this core is explained showing why you get that mathematical calculations from the term frequencies. Yeah.
The length of the document field, the average length of the field, the document, frequency, hour, error, a term was, for example, and so on and so forth. So long mathematical expression that are readable to the user and you can understand, okay, I was aiming for this field to impact the score.
Let's see, let's see, really impact the score. With better research right now, the only explanation that you get from an engineer perspective, literally is within the top K. So this document was within a top K with a cosine similarity between the query vector and the document vector.
That's not really helpful. It's just confirming what's you know already, right? I mean, yeah, it's in the top K, it was written.
So one of the ideas I was thinking of, because actually quite far from the implementation is to explain the reason document in the results set, showing examples of, so the language models used to return embedded, were fine tuned on sentence similarity.
So this means there were pair of sentences with similar meaning and pair of sentences with this similar meaning in a way that to learn how to encode this amount. So I think it could be very interesting if to explain the reason a document is being returned.
 Because of vector cells, you show like a snippet, say, because there are, there is this similar pairs of sentences and this is this similar sentence, in the way that then potentially the engineer can go back and realize, okay, let's take a look to the original training data, for example, did I cover the example well or maybe they are wrong?
So I see like, oh, these two sentences are shown as similar, but they are not so.
It's just an idea, you know, study it. Wow, that's very interesting, because as you said, it's very limiting today to just know that geometric search happened and this is the result. Yeah, that's amazing.
I mean, it's really interesting that with this work, you are not really just taking something and applying to implementation, right? Like, I mean, implementing a plugin, but you actually go into the space of exploring thing because it's not like everything is done, right?
And maybe in some companies, it has been done, but they are not open sourcing, right? And so you need to do the search, the search of the solution.
That's very interesting. So in terms of functionality today, hybrid search is already available in solar, right? Is it already released? And big portion? Yeah, so there are different ways I need search can be performed in solar. So right now, we saw 9.6.
There are ways of combining results from electrical search and vector-based search and then re-rank them, for example, using learning pranks. So you give like different ways to different factors. So for example, the vector-based core or the traditional core. Yeah.
What is coming next, which was the topic of my talk is the receiver rank user. So that's coming with solar 9.7. So I guess in a couple of months, we're going to release it. Nice. And that is a way of adding hybrid search that is independent on this core and just based on the ranking of the results.
So you mix the different rank lists. Yeah, they can be two, maybe more. Yeah. It's support more supported, not just two. And then you combine them based on the position of the documents in the different rank list. Yeah.
The higher the position in the ranking, the best the probability that the document is going to end up in a higher final result set. Yeah, yeah.
Actually, when I was maybe you can help me understand this, but when we were trying reciprocal rank fusion with another search engine, we actually found implementation. So we could kind of plug it in and Python code, very quickly.
But then when we looked at the code, one of my engineers said, this looks like round, raw, and algorithm essentially. There is nothing particularly peculiar about it or tunable about it, which probably is not true, but I'm not sure what's your take on this.
So it felt like you have two lists and you basically just take the starting from the top, you take like in order, you know, these documents and you combine a blend at least, right?
But if you wanted to pay attention to some signals from these documents, you know, based on their features or or maybe you wanted to introduce a logic on top of this, right?
So you want to say, let's say in the context of geographic search, I want to find in top three results, I want to see a super popular B.
O.I. and I know what popular means. Another second result could be, I don't know, the closest one or maybe vice versa, depends. And so on so forth. So I have some kind of rules in embed and then maybe it stops becoming RRE, already, right? But I still go going, taking a step backwards.
Did I explain it right? Or other some parameters and RRE that I could kind of be tuning a bit to have the different outcome? There's not much to tune to be honest. So you got it right.
It's not only around roaming, because what you do is basically you give a new score to the documents that are based on all the rankings of that document in the results list.
So it's not like in Perliving where, for example, you go with one document, you pick from one range of lists and then to the other list, you pick another and then you choose which one should I go next.
It's more about life, let's see this document how many times it appears in the ranking list and where it appears in the ranking list and let's build this new score. So the more you are in the top positions, the more likely you end up in the top position of the final result list.
Given that, you're absolutely right that if you want to be like more advanced ranking systems, potentially like with different phases, different steps, it makes complete sense to maybe build your original candidate sets with receiver or infusion.
And then you re-rank, for example, using learning to rank and many features where you can have like, again, maybe the vector distances one feature, the similarity we want to feel from a expert perspective, popularity, geographical distance and many other features.
And then you apply learning for example, so you train a machine learning model to identify these weights. It makes perfect sense in my opinion.
I believe receiver, rank, fusion and in general, like let's call them simple approaches with our research, because if you take a look to the algorithm of receiver or rank fusion, it's not the core, it's actually open and open algorithm from 2009.
But this opened the doors in my opinion to build your original candidate set and then potentially like, yeah, you re-rank it okay. Yeah, yeah, yeah, she's not random, it's okay, she's already some reasons to be there.
And of course, like in any case, those without saying that we do need to have some method of combining these completely disparate spaces of scores, right? Into one.
And that could be actually even like different search engines operating on keyword level because they output different scores, right? So maybe even potentially I'm thinking separate charts of your data that also have their own idea, right? Local idea. So, yeah, incomparable, right? Awesome.
We also, not related to this completely different topic, like there was also a keynote today about sort of what open source means, right?
And without, of course, criticizing, but some companies were mentioned on this context where they claim that the LLMs are open source, but when you look at the licenses, they are restrictive, they actually do not allow you to use them independently, right? And kind of go and serve your customers.
 But you also just mentioned what the code was started recording is that there are also cases where model can be open source, and it's kind of like more or less abiding the principles of open source spirit, but then contract, but then the data that it was trained on is not open source or the methods that were applied to the data are not open source, right?
So to me, it sounds so important to keep kind of declaring what open source is, what are the principles, right?
 And maybe this keynote also shed some light, but you also, it seems like this topic is also very close to you, and you are in the open source contributing a lot, you are the commuter, like can you can you share your vision on what is open source, what are the implications for how this field should be developing?
I think it's a huge problem, especially because nowadays open washing, which is like the practice of associating openness to something that potentially is not really fully open, is happening a lot.
Here's open source is cool, open source show like a good habit, so you're the good guys if you if you do open source.
So as you said, we are not going to make names of companies or association that claim, for example, they lar language model were open source, but lar language models are complex systems. So the outputs, the final light waves on the neural network is just one little part of the entire picture.
Those lar language models are normally pre-trained on huge quantities of data with a pre-training algorithm.
So the pre-training data and the pre-training code, is it open? Is it not? I mean, many times it's not, not only not, it's not open, it's not even known, what kind of data is just generic internet scale data.
What about the fine tuning them?
 So once you get the pre-training, which is the unsupervised part, where you just explore the web, that's pretty simple, then you want to fine tune for specific tasks, like sentence similarity or instruction following or, I don't know, summarization, any kind of task you want to use the and to do that normally using an additional training data set that is particularly designed for that fine tuning task.
And again, is that open? So do you communicate and then you make it available? And the code for fine tuning, do you make it available?
The output of the pre-training, do you make it available separately from the output of the fine, the documentation, any data that explains what is done, why you found it?
 So I've read like an interesting paper that I guess we can share, like, as a comment from a university, they were like comparing all these aspects for the MS models and how famous like open source of the MS models actually behaved on each of these columns and would be surprising how a small percentage of these like, you know, big layers are actually open sourcing everything.
So it's not just the license that as you said correctly, sometimes it's limiting, but literally like the components shirt, sometimes it's just the final which is, is it helpful?
I mean, in open source, you want to cooperate, you want to improve the code, like in normal code, you have access to everything and you can like improve, you can help the community.
If you just access the ways, you can use it, but can you, for example, improve it? Can you understand if it's fair? In the data you was there? Yes. Yeah, it's really difficult. Yeah.
And so, what do you think these discussions should start or maybe it's ongoing? Are you part of some discussion? And how does it impact business and maybe research? Right? Because there are different sides of this coin.
Many of these things emerge in the academia space, but then they move to create value on the business side, but it could also be vice versa.
So what do you think? What are we going to address this?
So I know that the open source initiative, which is a group of people that directly directly open source manifest, so I try to basically think to ways of the finding open source is they are working on a definition of open source for AI models.
We are going to see hopefully soon enough, a definition of what it means for a model to be open source. And that is going to be great, because at that point it's not a matter of like, I believe it's open, and I claim it's open. It's open for its notes.
And everything is covered by a license that is going to be open or not.
 In terms of like impolination between like the academia and the industry, I think probably that's the most, I mean, this period is so important to see like cross pollination, because there are like many models that for example are designed and contributed by the academia that must then be used by organizations and the other way around, because of course there are like a lot of money involved in training and free training and fine training on the algorithm of the models.
So many, I mean, only few actually organizations are able to do this. So they should try, I mean, ideally to make it as open as possible in a way that then universities can focus on small components and potentially help in some more. Yeah, yeah.
I mean, you know, pre-training and internet scale is incredibly expensive from energy perspective especially. So I hope, you know, we reach the point where everything is open enough for also smaller organizations and academia organizations to 12.
Yeah, it's very interesting because there is always going to be this kind of play between, okay, this big company has all the servers, they need to train the model.
So they can also decide how they will do it and not kind of disclose, but then maybe the question that we need to be disputing and sort of discussing is that they still don't have all the data to train on, right? Potentially.
Like there have been some cases mentioned in the keynote, you know, when some company, we will not name the company, it goes and trains it on some articles of famous publishing house, right? And now that publishing house is unhappy because they say you took our articles without us knowing this.
Now, it now it kind of evokes this question, okay, when I was reading this article, there was probably some license which said you can not, you can do this, but not this, maybe there is something hidden, right? But only now we started discussing these things, right?
And that's very interesting topic, but do you think that, you know, when the companies will be, let's say, they have open source to model and they have checked everything on that manifesto or on that contract.
 Do you think that there will be still a need for some maybe tooling or some process to kind of continuously maintain the status of this model as open source because it may well happen that, you know, either the company or research institute, they go and accidentally use some data that doesn't anymore confirm, confirm, like, comply with this contract, right?
First of all, without other lands, do you think such thing exists, would say, for Apache Solar or you see that no one will find a library that is not the license that it has to be, plugs it in and we do a release of you seeing a solar.
I think there is some checker, right? Yeah. So these applies to certain extent to code as well, right? So you are a contributor. When you sign basically the, let's say contract with the Apache Solar Foundation, you are sure that any kind of contribution you do is your own.
So there's not being COVID, for example, that was not COVID-rided and the sort of thing. It's genuinely created by you. It's genuinely created by you. So to certain extent, that would be a similar thing to potentially add some training data.
I think probably it's a little bit less likely that like in an existing large-language model, for example, someone would contribute a little more data. I mean, it's more likely that maybe you you would change a little bit the code, for example, responsible of fine tuning and it sort of things.
But still, I think there will be this layer of responsibility that wouldn't wait on the shoulders of the contributors because of course, you kind of have control on these single individuals.
And you need to have like this sort of layer where the no-profit, the Schopen source project protects itself from. Yeah.
Because I can imagine that again, it's probably putting it to extremes, but there could be eventually some tooling where you take the model and you introspect its behavior and you can make a guess on which data it was trained. Potentially. Or at least find some similarities with how it produces.
I mean, there been some attacks, so to say, right? So you can actually probe the model and see what it outputs, right? You can even break some models sometimes. That's true. So that's more like on the hacker side or the the bad hacker side. But I mean, there probably will be tooling.
Do you think it's possible that there will be tooling kind of checking the model and and making some hypothesis. And as you said, once caught, that organization will kind of lose its trust, right? So obviously, everyone wants to be kind of accountable and so on.
But then there could be a flip side of that that you can kind of accidentally assume that they did it, but that's not true, right? Now that becomes a very hard debate, right? So it's an area which I think deserves exploration and study.
And I believe that's being accountable of like the data you use and disclosing it, of course, is the first step. But then also validating that companies send the truth, for example, I think it's going to be important to build trust and to make sure that what you display is actually what happens.
Because we never know. It's very interesting. Was there some other topic you wanted to cover? I mean, are you also working on Raga or anything of that or evaluating the LLAM based search? We are working on many different integration with LLAM models. Retriol passage generation is one of it.
Nugro language parsing, for example, is another so moving from Nugro language to structured queries. Yeah. Probably the last thing we can discuss, the last topic we can discuss is prompt engineering. Yeah.
Briefly, because yes, it's this naming convention is something that really hurts me because it's not engineering at all in my opinion because you're just attempting to communicate with something and you don't know what to expect.
Because I've seen, I mean, I've seen tools today with people saying, you write this prompt and you hope you get this response. Yeah. You type this prompt and you ask, please give me the response. She is, to me, something that is, not scientific at all. It's not scientific. It's not scientific.
It's not science. You can't just be comfortable. Yeah, you can be comfortable. Yeah. So there's, in my opinion, just to give you short, a big margin of improvement there to interact with LLAM in a more program idea.
I want to specify it as with rules and get back a response that satisfies those rules. If I want to select an item from a list, I want to select an item from the list. I wonder LLAM is more than to be able to just select the item from the list.
I'm not 80% of the time, select the item on the list and 20% of the time, select the item and give me an explanation. I just wanted the item from the list. Yeah.
And right now, I've seen, and we will see the conference because I've seen in the agenda, there are a lot of many talks about trying to solve this problem. But right now, what I've seen as a possible solution is just like you post validates the response and you go back.
Like, okay, yeah, I asked for a specific JSON in the response. There are mistakes. It's like, it's not a possible JSON. I say, I go back to the LLAM and I say, this is not a possible JSON. Can you fix it? And again, and again, and again, which is not really something you want to go to production.
So in short, in my opinion, like using LLAM with models, program, I right now is full for approval concepts. But would I bring to production like out of the box like these sort of approaches? I want, because I wouldn't, you know, brings, I want to bring something that is deterministic. Yeah.
It does what I want to do 100% of the time. Sometimes. And I don't want to hope. It's a good thing. Well, I want to make it work.
Yeah, but it's also like I see it's very interesting topic, by the way, but I also see some level of contradiction that to like between non deterministic and hallucinating model essentially hallucinating by design because it keeps predicting the terms, right?
And some level of determinism as you just explained, right? But I guess, but I guess at the same time, someone might say that our life is not that deterministic, many moving parts and we still find a way to, I don't know, leave it and then build something, right? Yeah, there's something that moves.
I think, you know, it's the first, anyway, we are experiencing, in my opinion, at first, that in these new worlds, of AI big models. So I think it's fair. They were born to auto complete text, to generate text. And now we are trying to use them to do tasks. Yes. Which is okay.
We as humans use language to, to task. Yeah. So I just guess, and then we end up with programming. Yes. Computers, right? So let's play it in a little bit more that would be programmable. Yeah. I mean, it doesn't remind a bit.
I haven't explored it, but to mention GSPY, the packaging, probably you heard about it, right? Which replaces the prompt engineering with more programmable sort of way of doing it.
I still don't know how it works, but I know that some of the engineers in my team applied it quite successfully to generate some synthetic queries. So that was very interesting.
Have you played with it? Do you know? So my team, we've been playing with it for one of the bros of conceptual concepts for doing other language processing, for structure solar queries. And I think it's a nice first step.
Still is giving you like an in-direction between the prompt and the way to write a prompt. So you have like classes, the mimic, the programming language, but then ends up as prompt. Yeah. I see. You are not sure that you will get what you want. But it's a first attempt. Yeah. Yeah.
I think it's okay. I mean, we will improve that. It feels maybe like maybe first baby step in a way that it's not a work to the state that you mentioned. Yeah. That's not a conflict solution, but it's great. So what's next that you're working on? That you want to disclose? Yeah.
So first of all, I want you to bring and merge the hybrid search receiver rank fusion to solar, which is coming nine to seven. So I'm very close to the men. Awesome. For that. We are, we got some funding from the European Union to work on solar. So that's like that.
So we're going to be able to contribute more vector-based search capabilities, better integrations we've learned into rank, better integration with like inference and points to make it a little bit more transparent. That's it.
And still in the work like multivalued supports for vector-based search in solar. And there are like some pieces in losing to speed up and improve optimized vector-based search that are not yet in solar. And that's among my top priority. So this is in short. This is fantastic. This is fantastic.
And of course, it's all open source and you know, yeah, and then like anyone can join, but maybe we can also make a call out and say that, I mean, everyone that wants to contribute, you know, the more the merrier.
Yeah, I actually enjoy like even though I don't do solar or only seen today, I am still reading the main news. And and for the most part, I'm reading the lesson one. So sometimes I see your discussion as well and you where you say, actually, by the way, I'm working on this hybrid search.
I did this and this. So maybe it will influence you. And I also love the the culture where you do not really enforce or impose your solution. You just say just for you to know, maybe it will be useful. And someone says, yeah, awesome. I especially love that that discussion.
I forgot the particular topic, but I remember it was a recent one. It's a recent one. So keep up your great work. And it's always a pleasure to talk to you and it looks like it's a tradition that we started meeting in the same sort of early flood words. In the end now.
Yeah, so every two years, we see a lot of people. Yeah, there are a lot of people. So fantastic. Thank you so much, LeSando. And anyway, my reaction to the conference. Thank you. Thank you.