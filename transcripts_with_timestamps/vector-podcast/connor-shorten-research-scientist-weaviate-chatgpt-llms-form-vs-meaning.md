---
description: '<p>Topics:</p><p>00:00 Intro</p><p>01:54 Things Connor learnt in the
  past year that changed his perception of Vector Search</p><p>02:42 Is search becoming
  conversational?</p><p>05:46 Connor asks Dmitry: How Large Language Models will change
  Search?</p><p>08:39 Vector Search Pyramid</p><p>09:53 Large models, data, Form vs
  Meaning and octopus underneath the ocean</p><p>13:25 Examples of getting help from
  ChatGPT and how it compares to web search today</p><p>18:32 Classical search engines
  with URLs for verification vs ChatGPT-style answers</p><p>20:15 Hybrid search: keywords
  + semantic retrieval</p><p>23:12 Connor asks Dmitry about his experience with sparse
  retrieval</p><p>28:08 SPLADE vectors</p><p>34:10 OOD-DiskANN: handling the out-of-distribution
  queries, and nuances of sparse vs dense indexing and search</p><p>39:54 Ways to
  debug a query case in dense retrieval (spoiler: it is a challenge!)</p><p>44:47
  Intricacies of teaching ML models to understand your data and re-vectorization</p><p>49:23
  Local IDF vs global IDF and how dense search can approach this issue</p><p>54:00
  Realtime index</p><p>59:01 Natural language to SQL</p><p>1:04:47 Turning text into
  a causal DAG</p><p>1:10:41 Engineering and Research as two highly intelligent disciplines</p><p>1:18:34
  Podcast search</p><p>1:25:24 Ref2Vec for recommender systems</p><p>1:29:48 Announcements</p><p>For
  Show Notes, please check out the YouTube episode below.</p><p>This episode on YouTube:
  <a href="https://www.youtube.com/watch?v=2Q-7taLZ374">https://www.youtube.com/watch?v=2Q-7taLZ374</a></p><p>Podcast
  design: Saurabh Rai: <a href="https://twitter.com/srvbhr">https://twitter.com/srvbhr</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20230311_070307_5788fcdf763e7dd822dd4b0bbb59f9b6.jpg
pub_date: Sat, 11 Mar 2023 19:38:10 GMT
title: Connor Shorten - Research Scientist, Weaviate - ChatGPT, LLMs, Form vs Meaning
url: https://rss.com/podcasts/vector-podcast/861832
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 28.46, "text": " Hello
  there, vector podcasts. Season 2, and to them super super super excited to have",
  "tokens": [50364, 2425, 456, 11, 8062, 24045, 13, 16465, 568, 11, 293, 281, 552,
  1687, 1687, 1687, 2919, 281, 362, 51787], "temperature": 0.0, "avg_logprob": -0.5331543142145331,
  "compression_ratio": 1.1333333333333333, "no_speech_prob": 0.11617506295442581},
  {"id": 1, "seek": 2846, "start": 28.46, "end": 35.58, "text": " a reappearance of
  corner shortened on vector podcasts. We recorded like a year ago about that time.",
  "tokens": [50364, 257, 35638, 14881, 719, 295, 4538, 45183, 322, 8062, 24045, 13,
  492, 8287, 411, 257, 1064, 2057, 466, 300, 565, 13, 50720], "temperature": 0.0,
  "avg_logprob": -0.3013858393618935, "compression_ratio": 1.578512396694215, "no_speech_prob":
  0.28037235140800476}, {"id": 2, "seek": 2846, "start": 35.58, "end": 43.74, "text":
  " Something''s changed. He is a research scientist at Semi Technologies, the company
  behind VB8.", "tokens": [50720, 6595, 311, 3105, 13, 634, 307, 257, 2132, 12662,
  412, 318, 13372, 46993, 11, 264, 2237, 2261, 691, 33, 23, 13, 51128], "temperature":
  0.0, "avg_logprob": -0.3013858393618935, "compression_ratio": 1.578512396694215,
  "no_speech_prob": 0.28037235140800476}, {"id": 3, "seek": 2846, "start": 44.38,
  "end": 49.019999999999996, "text": " Here you can see an episode with Bob, and here
  you can see the episode with Connor as well.", "tokens": [51160, 1692, 291, 393,
  536, 364, 3500, 365, 6085, 11, 293, 510, 291, 393, 536, 264, 3500, 365, 33133, 382,
  731, 13, 51392], "temperature": 0.0, "avg_logprob": -0.3013858393618935, "compression_ratio":
  1.578512396694215, "no_speech_prob": 0.28037235140800476}, {"id": 4, "seek": 2846,
  "start": 51.019999999999996, "end": 56.94, "text": " And back then when we were
  talking, Connor, you''ve been a lot into basketball. Do you still play", "tokens":
  [51492, 400, 646, 550, 562, 321, 645, 1417, 11, 33133, 11, 291, 600, 668, 257, 688,
  666, 11767, 13, 1144, 291, 920, 862, 51788], "temperature": 0.0, "avg_logprob":
  -0.3013858393618935, "compression_ratio": 1.578512396694215, "no_speech_prob": 0.28037235140800476},
  {"id": 5, "seek": 5694, "start": 56.94, "end": 63.099999999999994, "text": " basketball?
  Yeah, I still play a little bit. And I''ll add also to that that I think you also",
  "tokens": [50364, 11767, 30, 865, 11, 286, 920, 862, 257, 707, 857, 13, 400, 286,
  603, 909, 611, 281, 300, 300, 286, 519, 291, 611, 50672], "temperature": 0.0, "avg_logprob":
  -0.30982985245554073, "compression_ratio": 1.55, "no_speech_prob": 0.02928188629448414},
  {"id": 6, "seek": 5694, "start": 63.099999999999994, "end": 69.5, "text": " have
  podcasts with Eddie and Laura, also in the queue of we''ve read. We''ll add that.
  Exactly.", "tokens": [50672, 362, 24045, 365, 23911, 293, 13220, 11, 611, 294, 264,
  18639, 295, 321, 600, 1401, 13, 492, 603, 909, 300, 13, 7587, 13, 50992], "temperature":
  0.0, "avg_logprob": -0.30982985245554073, "compression_ratio": 1.55, "no_speech_prob":
  0.02928188629448414}, {"id": 7, "seek": 5694, "start": 70.22, "end": 76.62, "text":
  " And I remember like you''ve been big on computer vision, data augmentation back
  then, and you", "tokens": [51028, 400, 286, 1604, 411, 291, 600, 668, 955, 322,
  3820, 5201, 11, 1412, 14501, 19631, 646, 550, 11, 293, 291, 51348], "temperature":
  0.0, "avg_logprob": -0.30982985245554073, "compression_ratio": 1.55, "no_speech_prob":
  0.02928188629448414}, {"id": 8, "seek": 5694, "start": 76.62, "end": 83.42, "text":
  " first like guinea pig task was you know some capturing baskets in the basketball
  game. And I", "tokens": [51348, 700, 411, 695, 31940, 8120, 5633, 390, 291, 458,
  512, 23384, 42853, 294, 264, 11767, 1216, 13, 400, 286, 51688], "temperature": 0.0,
  "avg_logprob": -0.30982985245554073, "compression_ratio": 1.55, "no_speech_prob":
  0.02928188629448414}, {"id": 9, "seek": 8342, "start": 83.42, "end": 89.42, "text":
  " wonder if you continued working on that at some point. Yeah, I think about it
  every now and then,", "tokens": [50364, 2441, 498, 291, 7014, 1364, 322, 300, 412,
  512, 935, 13, 865, 11, 286, 519, 466, 309, 633, 586, 293, 550, 11, 50664], "temperature":
  0.0, "avg_logprob": -0.1597790410441737, "compression_ratio": 1.7359154929577465,
  "no_speech_prob": 0.01220800168812275}, {"id": 10, "seek": 8342, "start": 89.42,
  "end": 94.46000000000001, "text": " but I''ve been so captivated by the natural
  language processing and the tech search honestly. I", "tokens": [50664, 457, 286,
  600, 668, 370, 40769, 770, 538, 264, 3303, 2856, 9007, 293, 264, 7553, 3164, 6095,
  13, 286, 50916], "temperature": 0.0, "avg_logprob": -0.1597790410441737, "compression_ratio":
  1.7359154929577465, "no_speech_prob": 0.01220800168812275}, {"id": 11, "seek": 8342,
  "start": 94.46000000000001, "end": 101.42, "text": " still think about image search
  a bit, but yeah, the tech search to me is just it''s just so exciting.", "tokens":
  [50916, 920, 519, 466, 3256, 3164, 257, 857, 11, 457, 1338, 11, 264, 7553, 3164,
  281, 385, 307, 445, 309, 311, 445, 370, 4670, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.1597790410441737, "compression_ratio": 1.7359154929577465, "no_speech_prob":
  0.01220800168812275}, {"id": 12, "seek": 8342, "start": 101.42, "end": 105.74000000000001,
  "text": " It feels like there''s so much that you can do with it. And yeah, it''s
  really been it''s been an", "tokens": [51264, 467, 3417, 411, 456, 311, 370, 709,
  300, 291, 393, 360, 365, 309, 13, 400, 1338, 11, 309, 311, 534, 668, 309, 311, 668,
  364, 51480], "temperature": 0.0, "avg_logprob": -0.1597790410441737, "compression_ratio":
  1.7359154929577465, "no_speech_prob": 0.01220800168812275}, {"id": 13, "seek": 8342,
  "start": 105.74000000000001, "end": 110.7, "text": " intense year. I''ve learned
  so much and I think it''ll be a totally different podcast with respect to like",
  "tokens": [51480, 9447, 1064, 13, 286, 600, 3264, 370, 709, 293, 286, 519, 309,
  603, 312, 257, 3879, 819, 7367, 365, 3104, 281, 411, 51728], "temperature": 0.0,
  "avg_logprob": -0.1597790410441737, "compression_ratio": 1.7359154929577465, "no_speech_prob":
  0.01220800168812275}, {"id": 14, "seek": 11070, "start": 110.86, "end": 117.98,
  "text": " what I''m this talking about. Yeah, yeah, absolutely. I actually love
  to start also by asking you,", "tokens": [50372, 437, 286, 478, 341, 1417, 466,
  13, 865, 11, 1338, 11, 3122, 13, 286, 767, 959, 281, 722, 611, 538, 3365, 291, 11,
  50728], "temperature": 0.0, "avg_logprob": -0.19961551867033306, "compression_ratio":
  1.5761316872427984, "no_speech_prob": 0.009259650483727455}, {"id": 15, "seek":
  11070, "start": 117.98, "end": 123.66, "text": " what do you feel you''ve learned
  in this year that has changed something fundamentally in how you", "tokens": [50728,
  437, 360, 291, 841, 291, 600, 3264, 294, 341, 1064, 300, 575, 3105, 746, 17879,
  294, 577, 291, 51012], "temperature": 0.0, "avg_logprob": -0.19961551867033306,
  "compression_ratio": 1.5761316872427984, "no_speech_prob": 0.009259650483727455},
  {"id": 16, "seek": 11070, "start": 123.66, "end": 131.98000000000002, "text": "
  perceive vector search today versus back then and year ago? Yeah, that''s a big
  question. I think", "tokens": [51012, 20281, 8062, 3164, 965, 5717, 646, 550, 293,
  1064, 2057, 30, 865, 11, 300, 311, 257, 955, 1168, 13, 286, 519, 51428], "temperature":
  0.0, "avg_logprob": -0.19961551867033306, "compression_ratio": 1.5761316872427984,
  "no_speech_prob": 0.009259650483727455}, {"id": 17, "seek": 11070, "start": 131.98000000000002,
  "end": 137.26, "text": " I''m definitely with we V8. I''ve learned a lot about having
  like kind of the user focus, the", "tokens": [51428, 286, 478, 2138, 365, 321, 691,
  23, 13, 286, 600, 3264, 257, 688, 466, 1419, 411, 733, 295, 264, 4195, 1879, 11,
  264, 51692], "temperature": 0.0, "avg_logprob": -0.19961551867033306, "compression_ratio":
  1.5761316872427984, "no_speech_prob": 0.009259650483727455}, {"id": 18, "seek":
  13726, "start": 137.26, "end": 142.14, "text": " product focus definitely way more
  engineering understanding of the distributed data system,", "tokens": [50364, 1674,
  1879, 2138, 636, 544, 7043, 3701, 295, 264, 12631, 1412, 1185, 11, 50608], "temperature":
  0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 19, "seek": 13726, "start": 142.14,
  "end": 147.1, "text": " replication, cap theorem, all these kind of things. So like
  the knowledge of the engineering", "tokens": [50608, 39911, 11, 1410, 20904, 11,
  439, 613, 733, 295, 721, 13, 407, 411, 264, 3601, 295, 264, 7043, 50856], "temperature":
  0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 20, "seek": 13726, "start": 147.1,
  "end": 152.22, "text": " around it in addition to sort of the machine learning research
  about like how to vector representations", "tokens": [50856, 926, 309, 294, 4500,
  281, 1333, 295, 264, 3479, 2539, 2132, 466, 411, 577, 281, 8062, 33358, 51112],
  "temperature": 0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 21, "seek": 13726, "start": 152.22,
  "end": 156.7, "text": " get optimized with deep learning models and then you know,
  this whole retrieve and read research.", "tokens": [51112, 483, 26941, 365, 2452,
  2539, 5245, 293, 550, 291, 458, 11, 341, 1379, 30254, 293, 1401, 2132, 13, 51336],
  "temperature": 0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 22, "seek": 13726, "start": 156.7,
  "end": 161.34, "text": " And overall the space is evolved in such an amazing way
  and it''s just really exciting.", "tokens": [51336, 400, 4787, 264, 1901, 307, 14178,
  294, 1270, 364, 2243, 636, 293, 309, 311, 445, 534, 4670, 13, 51568], "temperature":
  0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 23, "seek": 13726, "start": 161.89999999999998,
  "end": 166.62, "text": " Yeah, absolutely. I''ve been I''ve been also following
  all different things reading papers,", "tokens": [51596, 865, 11, 3122, 13, 286,
  600, 668, 286, 600, 668, 611, 3480, 439, 819, 721, 3760, 10577, 11, 51832], "temperature":
  0.0, "avg_logprob": -0.1706287120950633, "compression_ratio": 1.7112462006079028,
  "no_speech_prob": 0.0024359251838177443}, {"id": 24, "seek": 16662, "start": 166.62,
  "end": 171.98000000000002, "text": " you know, implementing clip, but I still feel
  like I miss out on so many things and I really hope", "tokens": [50364, 291, 458,
  11, 18114, 7353, 11, 457, 286, 920, 841, 411, 286, 1713, 484, 322, 370, 867, 721,
  293, 286, 534, 1454, 50632], "temperature": 0.0, "avg_logprob": -0.11819670372402545,
  "compression_ratio": 1.5959183673469388, "no_speech_prob": 0.001943264389410615},
  {"id": 25, "seek": 16662, "start": 171.98000000000002, "end": 181.1, "text": " we
  will cover some of them today. And we on the verge of I think maybe witnessing a
  change in", "tokens": [50632, 321, 486, 2060, 512, 295, 552, 965, 13, 400, 321,
  322, 264, 37164, 295, 286, 519, 1310, 39233, 257, 1319, 294, 51088], "temperature":
  0.0, "avg_logprob": -0.11819670372402545, "compression_ratio": 1.5959183673469388,
  "no_speech_prob": 0.001943264389410615}, {"id": 26, "seek": 16662, "start": 181.1,
  "end": 188.62, "text": " the search paradigm, you know, with chat GPT. I first I
  wanted to sort of get your first reaction", "tokens": [51088, 264, 3164, 24709,
  11, 291, 458, 11, 365, 5081, 26039, 51, 13, 286, 700, 286, 1415, 281, 1333, 295,
  483, 428, 700, 5480, 51464], "temperature": 0.0, "avg_logprob": -0.11819670372402545,
  "compression_ratio": 1.5959183673469388, "no_speech_prob": 0.001943264389410615},
  {"id": 27, "seek": 16662, "start": 188.62, "end": 195.34, "text": " on this. Obviously
  you tested it. I also tested it actually with when I published my recent blog post",
  "tokens": [51464, 322, 341, 13, 7580, 291, 8246, 309, 13, 286, 611, 8246, 309, 767,
  365, 562, 286, 6572, 452, 5162, 6968, 2183, 51800], "temperature": 0.0, "avg_logprob":
  -0.11819670372402545, "compression_ratio": 1.5959183673469388, "no_speech_prob":
  0.001943264389410615}, {"id": 28, "seek": 19534, "start": 195.34, "end": 201.5,
  "text": " on neural search frameworks. And I was like just stuck on creating a title
  and I asked chat GPT,", "tokens": [50364, 322, 18161, 3164, 29834, 13, 400, 286,
  390, 411, 445, 5541, 322, 4084, 257, 4876, 293, 286, 2351, 5081, 26039, 51, 11,
  50672], "temperature": 0.0, "avg_logprob": -0.17986619472503662, "compression_ratio":
  1.6623376623376624, "no_speech_prob": 0.0016417858423665166}, {"id": 29, "seek":
  19534, "start": 201.5, "end": 206.78, "text": " can you come up with a title and
  came up with a reasonably good title and I actually used it without", "tokens":
  [50672, 393, 291, 808, 493, 365, 257, 4876, 293, 1361, 493, 365, 257, 23551, 665,
  4876, 293, 286, 767, 1143, 309, 1553, 50936], "temperature": 0.0, "avg_logprob":
  -0.17986619472503662, "compression_ratio": 1.6623376623376624, "no_speech_prob":
  0.0016417858423665166}, {"id": 30, "seek": 19534, "start": 206.78, "end": 212.38,
  "text": " editing. And I read a bunch of other stories, you know, like for example,
  how you can avoid", "tokens": [50936, 10000, 13, 400, 286, 1401, 257, 3840, 295,
  661, 3676, 11, 291, 458, 11, 411, 337, 1365, 11, 577, 291, 393, 5042, 51216], "temperature":
  0.0, "avg_logprob": -0.17986619472503662, "compression_ratio": 1.6623376623376624,
  "no_speech_prob": 0.0016417858423665166}, {"id": 31, "seek": 19534, "start": 213.02,
  "end": 220.7, "text": " fines, for wrong parking and stuff. But then there is this
  discussion going on, you know, like", "tokens": [51248, 37989, 11, 337, 2085, 9893,
  293, 1507, 13, 583, 550, 456, 307, 341, 5017, 516, 322, 11, 291, 458, 11, 411, 51632],
  "temperature": 0.0, "avg_logprob": -0.17986619472503662, "compression_ratio": 1.6623376623376624,
  "no_speech_prob": 0.0016417858423665166}, {"id": 32, "seek": 22070, "start": 220.78,
  "end": 224.29999999999998, "text": " how it may change search. But before that,
  what was your impression of chat GPT?", "tokens": [50368, 577, 309, 815, 1319, 3164,
  13, 583, 949, 300, 11, 437, 390, 428, 9995, 295, 5081, 26039, 51, 30, 50544], "temperature":
  0.0, "avg_logprob": -0.14310882831441946, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.018956175073981285}, {"id": 33, "seek": 22070, "start": 225.82,
  "end": 232.7, "text": " Yeah, well, I think like everyone else sort of in in this
  like reading about say Google''s", "tokens": [50620, 865, 11, 731, 11, 286, 519,
  411, 1518, 1646, 1333, 295, 294, 294, 341, 411, 3760, 466, 584, 3329, 311, 50964],
  "temperature": 0.0, "avg_logprob": -0.14310882831441946, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.018956175073981285}, {"id": 34, "seek": 22070, "start": 232.7,
  "end": 237.89999999999998, "text": " flan model or, you know, that we''ve been kind
  of reading about a lot of these large language", "tokens": [50964, 932, 282, 2316,
  420, 11, 291, 458, 11, 300, 321, 600, 668, 733, 295, 3760, 466, 257, 688, 295, 613,
  2416, 2856, 51224], "temperature": 0.0, "avg_logprob": -0.14310882831441946, "compression_ratio":
  1.5957446808510638, "no_speech_prob": 0.018956175073981285}, {"id": 35, "seek":
  22070, "start": 237.89999999999998, "end": 242.62, "text": " models, but we haven''t
  actually really gotten to use them. I think Facebook''s OPT model was on", "tokens":
  [51224, 5245, 11, 457, 321, 2378, 380, 767, 534, 5768, 281, 764, 552, 13, 286, 519,
  4384, 311, 23324, 51, 2316, 390, 322, 51460], "temperature": 0.0, "avg_logprob":
  -0.14310882831441946, "compression_ratio": 1.5957446808510638, "no_speech_prob":
  0.018956175073981285}, {"id": 36, "seek": 22070, "start": 242.62, "end": 247.89999999999998,
  "text": " hugging face and I played with that and back in back at the time, I was
  mostly like the few", "tokens": [51460, 41706, 1851, 293, 286, 3737, 365, 300, 293,
  646, 294, 646, 412, 264, 565, 11, 286, 390, 5240, 411, 264, 1326, 51724], "temperature":
  0.0, "avg_logprob": -0.14310882831441946, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.018956175073981285}, {"id": 37, "seek": 24790, "start": 247.9,
  "end": 251.98000000000002, "text": " shot learning part was like the part that was
  so exciting where you could, you know, give it like", "tokens": [50364, 3347, 2539,
  644, 390, 411, 264, 644, 300, 390, 370, 4670, 689, 291, 727, 11, 291, 458, 11, 976,
  309, 411, 50568], "temperature": 0.0, "avg_logprob": -0.15204935488493546, "compression_ratio":
  1.721830985915493, "no_speech_prob": 0.004537984728813171}, {"id": 38, "seek": 24790,
  "start": 251.98000000000002, "end": 256.14, "text": " for example, of a task and
  then it could just instantly learn the task and that''s like pretty", "tokens":
  [50568, 337, 1365, 11, 295, 257, 5633, 293, 550, 309, 727, 445, 13518, 1466, 264,
  5633, 293, 300, 311, 411, 1238, 50776], "temperature": 0.0, "avg_logprob": -0.15204935488493546,
  "compression_ratio": 1.721830985915493, "no_speech_prob": 0.004537984728813171},
  {"id": 39, "seek": 24790, "start": 256.14, "end": 261.1, "text": " surprising for
  people who''ve been doing supervised learning optimization for a long time. And
  so", "tokens": [50776, 8830, 337, 561, 567, 600, 668, 884, 46533, 2539, 19618, 337,
  257, 938, 565, 13, 400, 370, 51024], "temperature": 0.0, "avg_logprob": -0.15204935488493546,
  "compression_ratio": 1.721830985915493, "no_speech_prob": 0.004537984728813171},
  {"id": 40, "seek": 24790, "start": 261.1, "end": 266.22, "text": " mostly my thinking
  was a few shot learning, but this chat GPT thing, this reinforced learning from",
  "tokens": [51024, 5240, 452, 1953, 390, 257, 1326, 3347, 2539, 11, 457, 341, 5081,
  26039, 51, 551, 11, 341, 31365, 2539, 490, 51280], "temperature": 0.0, "avg_logprob":
  -0.15204935488493546, "compression_ratio": 1.721830985915493, "no_speech_prob":
  0.004537984728813171}, {"id": 41, "seek": 24790, "start": 266.22, "end": 273.42,
  "text": " human feedback, this like I mean the way that it can talk is just mind
  blowing. It''s I''m so amazed by", "tokens": [51280, 1952, 5824, 11, 341, 411, 286,
  914, 264, 636, 300, 309, 393, 751, 307, 445, 1575, 15068, 13, 467, 311, 286, 478,
  370, 20507, 538, 51640], "temperature": 0.0, "avg_logprob": -0.15204935488493546,
  "compression_ratio": 1.721830985915493, "no_speech_prob": 0.004537984728813171},
  {"id": 42, "seek": 27342, "start": 273.90000000000003, "end": 279.42, "text": "
  and I think yeah, it''s really unlocked a lot of thinking about the importance of
  prompting to", "tokens": [50388, 293, 286, 519, 1338, 11, 309, 311, 534, 30180,
  257, 688, 295, 1953, 466, 264, 7379, 295, 12391, 278, 281, 50664], "temperature":
  0.0, "avg_logprob": -0.11184623461811483, "compression_ratio": 1.7619047619047619,
  "no_speech_prob": 0.004762864205986261}, {"id": 43, "seek": 27342, "start": 279.42,
  "end": 283.98, "text": " me and what prompting means. I used to think that was just
  kind of like a task description idea,", "tokens": [50664, 385, 293, 437, 12391,
  278, 1355, 13, 286, 1143, 281, 519, 300, 390, 445, 733, 295, 411, 257, 5633, 3855,
  1558, 11, 50892], "temperature": 0.0, "avg_logprob": -0.11184623461811483, "compression_ratio":
  1.7619047619047619, "no_speech_prob": 0.004762864205986261}, {"id": 44, "seek":
  27342, "start": 283.98, "end": 289.1, "text": " which it still kind of is, but it''s
  like the nuances of it are so much. And yeah, I''d really", "tokens": [50892, 597,
  309, 920, 733, 295, 307, 11, 457, 309, 311, 411, 264, 38775, 295, 309, 366, 370,
  709, 13, 400, 1338, 11, 286, 1116, 534, 51148], "temperature": 0.0, "avg_logprob":
  -0.11184623461811483, "compression_ratio": 1.7619047619047619, "no_speech_prob":
  0.004762864205986261}, {"id": 45, "seek": 27342, "start": 289.1, "end": 294.54,
  "text": " love to like dive into this topic of large language models and search
  and I have a few different", "tokens": [51148, 959, 281, 411, 9192, 666, 341, 4829,
  295, 2416, 2856, 5245, 293, 3164, 293, 286, 362, 257, 1326, 819, 51420], "temperature":
  0.0, "avg_logprob": -0.11184623461811483, "compression_ratio": 1.7619047619047619,
  "no_speech_prob": 0.004762864205986261}, {"id": 46, "seek": 27342, "start": 294.54,
  "end": 299.26, "text": " dimensions of how I''m kind of thinking about these two
  things relating to each other, but since I''ve", "tokens": [51420, 12819, 295, 577,
  286, 478, 733, 295, 1953, 466, 613, 732, 721, 23968, 281, 1184, 661, 11, 457, 1670,
  286, 600, 51656], "temperature": 0.0, "avg_logprob": -0.11184623461811483, "compression_ratio":
  1.7619047619047619, "no_speech_prob": 0.004762864205986261}, {"id": 47, "seek":
  29926, "start": 299.65999999999997, "end": 305.65999999999997, "text": " brought
  up prompting, I kind of want to stay on this one quickly. So Bob and Jerry Lou showed
  me this", "tokens": [50384, 3038, 493, 12391, 278, 11, 286, 733, 295, 528, 281,
  1754, 322, 341, 472, 2661, 13, 407, 6085, 293, 17454, 7272, 4712, 385, 341, 50684],
  "temperature": 0.0, "avg_logprob": -0.14329574067713852, "compression_ratio": 1.7377622377622377,
  "no_speech_prob": 0.0004865841183345765}, {"id": 48, "seek": 29926, "start": 305.65999999999997,
  "end": 312.21999999999997, "text": " thing called GPT index and GPT index has this
  strategy for prompting GPT for summarization. It has", "tokens": [50684, 551, 1219,
  26039, 51, 8186, 293, 26039, 51, 8186, 575, 341, 5206, 337, 12391, 278, 26039, 51,
  337, 14611, 2144, 13, 467, 575, 51012], "temperature": 0.0, "avg_logprob": -0.14329574067713852,
  "compression_ratio": 1.7377622377622377, "no_speech_prob": 0.0004865841183345765},
  {"id": 49, "seek": 29926, "start": 312.21999999999997, "end": 316.38, "text": "
  other things, but this is one thing that just really stood out to me and there are
  like two strategies", "tokens": [51012, 661, 721, 11, 457, 341, 307, 472, 551, 300,
  445, 534, 9371, 484, 281, 385, 293, 456, 366, 411, 732, 9029, 51220], "temperature":
  0.0, "avg_logprob": -0.14329574067713852, "compression_ratio": 1.7377622377622377,
  "no_speech_prob": 0.0004865841183345765}, {"id": 50, "seek": 29926, "start": 316.38,
  "end": 323.18, "text": " you can use to summarize long text with the large language
  model. You can either create and refine", "tokens": [51220, 291, 393, 764, 281,
  20858, 938, 2487, 365, 264, 2416, 2856, 2316, 13, 509, 393, 2139, 1884, 293, 33906,
  51560], "temperature": 0.0, "avg_logprob": -0.14329574067713852, "compression_ratio":
  1.7377622377622377, "no_speech_prob": 0.0004865841183345765}, {"id": 51, "seek":
  29926, "start": 323.18, "end": 327.42, "text": " where you go paragraph by paragraph
  and you say like you start up by please write a summary of", "tokens": [51560, 689,
  291, 352, 18865, 538, 18865, 293, 291, 584, 411, 291, 722, 493, 538, 1767, 2464,
  257, 12691, 295, 51772], "temperature": 0.0, "avg_logprob": -0.14329574067713852,
  "compression_ratio": 1.7377622377622377, "no_speech_prob": 0.0004865841183345765},
  {"id": 52, "seek": 32742, "start": 327.42, "end": 332.38, "text": " this long text,
  you''ll receive a paragraph by paragraph and then it iteratively updates a summary",
  "tokens": [50364, 341, 938, 2487, 11, 291, 603, 4774, 257, 18865, 538, 18865, 293,
  550, 309, 17138, 19020, 9205, 257, 12691, 50612], "temperature": 0.0, "avg_logprob":
  -0.10319620931250417, "compression_ratio": 1.8631178707224334, "no_speech_prob":
  0.0023818169720470905}, {"id": 53, "seek": 32742, "start": 332.38, "end": 336.7,
  "text": " or you can have this tree where you you know you chunk it up like you
  know as a tree and then you", "tokens": [50612, 420, 291, 393, 362, 341, 4230, 689,
  291, 291, 458, 291, 16635, 309, 493, 411, 291, 458, 382, 257, 4230, 293, 550, 291,
  50828], "temperature": 0.0, "avg_logprob": -0.10319620931250417, "compression_ratio":
  1.8631178707224334, "no_speech_prob": 0.0023818169720470905}, {"id": 54, "seek":
  32742, "start": 336.7, "end": 342.86, "text": " couple it like recursively and then
  build up the summary that way. So this kind of thing about like", "tokens": [50828,
  1916, 309, 411, 20560, 3413, 293, 550, 1322, 493, 264, 12691, 300, 636, 13, 407,
  341, 733, 295, 551, 466, 411, 51136], "temperature": 0.0, "avg_logprob": -0.10319620931250417,
  "compression_ratio": 1.8631178707224334, "no_speech_prob": 0.0023818169720470905},
  {"id": 55, "seek": 32742, "start": 342.86, "end": 348.3, "text": " how we use these
  large language models all of it is so interesting and so I guess kind of yeah,",
  "tokens": [51136, 577, 321, 764, 613, 2416, 2856, 5245, 439, 295, 309, 307, 370,
  1880, 293, 370, 286, 2041, 733, 295, 1338, 11, 51408], "temperature": 0.0, "avg_logprob":
  -0.10319620931250417, "compression_ratio": 1.8631178707224334, "no_speech_prob":
  0.0023818169720470905}, {"id": 56, "seek": 32742, "start": 348.3, "end": 353.02000000000004,
  "text": " let me pass it back to you and I''m curious like how do you think large
  language models will change", "tokens": [51408, 718, 385, 1320, 309, 646, 281, 291,
  293, 286, 478, 6369, 411, 577, 360, 291, 519, 2416, 2856, 5245, 486, 1319, 51644],
  "temperature": 0.0, "avg_logprob": -0.10319620931250417, "compression_ratio": 1.8631178707224334,
  "no_speech_prob": 0.0023818169720470905}, {"id": 57, "seek": 35302, "start": 353.41999999999996,
  "end": 361.65999999999997, "text": " search? Yeah, I mean I''m still kind of learning
  it and I having you know built search engine before", "tokens": [50384, 3164, 30,
  865, 11, 286, 914, 286, 478, 920, 733, 295, 2539, 309, 293, 286, 1419, 291, 458,
  3094, 3164, 2848, 949, 50796], "temperature": 0.0, "avg_logprob": -0.15071534073871115,
  "compression_ratio": 1.6134453781512605, "no_speech_prob": 0.0015915316762402654},
  {"id": 58, "seek": 35302, "start": 361.65999999999997, "end": 369.5, "text": " vector
  search you know using like TFIDF basically. I knew the cost of doing it wrong you
  know", "tokens": [50796, 8062, 3164, 291, 458, 1228, 411, 40964, 2777, 37, 1936,
  13, 286, 2586, 264, 2063, 295, 884, 309, 2085, 291, 458, 51188], "temperature":
  0.0, "avg_logprob": -0.15071534073871115, "compression_ratio": 1.6134453781512605,
  "no_speech_prob": 0.0015915316762402654}, {"id": 59, "seek": 35302, "start": 369.5,
  "end": 377.34, "text": " or sort of focusing too much on precision and then paying
  a huge bill because of that. So like", "tokens": [51188, 420, 1333, 295, 8416, 886,
  709, 322, 18356, 293, 550, 6229, 257, 2603, 2961, 570, 295, 300, 13, 407, 411, 51580],
  "temperature": 0.0, "avg_logprob": -0.15071534073871115, "compression_ratio": 1.6134453781512605,
  "no_speech_prob": 0.0015915316762402654}, {"id": 60, "seek": 35302, "start": 377.34,
  "end": 382.46, "text": " our search engine for example back in the days when we
  indexed on sentence level in alpha sense", "tokens": [51580, 527, 3164, 2848, 337,
  1365, 646, 294, 264, 1708, 562, 321, 8186, 292, 322, 8174, 1496, 294, 8961, 2020,
  51836], "temperature": 0.0, "avg_logprob": -0.15071534073871115, "compression_ratio":
  1.6134453781512605, "no_speech_prob": 0.0015915316762402654}, {"id": 61, "seek":
  38246, "start": 382.62, "end": 390.21999999999997, "text": " would eat something
  like half a terabyte memory and you know memory was never cheap like it was", "tokens":
  [50372, 576, 1862, 746, 411, 1922, 257, 1796, 34529, 4675, 293, 291, 458, 4675,
  390, 1128, 7084, 411, 309, 390, 50752], "temperature": 0.0, "avg_logprob": -0.1213303876210408,
  "compression_ratio": 1.6724137931034482, "no_speech_prob": 0.0009250330622307956},
  {"id": 62, "seek": 38246, "start": 390.21999999999997, "end": 398.38, "text": "
  very expensive even back then and so we had to figure out ways to retain precision,
  not lose recall", "tokens": [50752, 588, 5124, 754, 646, 550, 293, 370, 321, 632,
  281, 2573, 484, 2098, 281, 18340, 18356, 11, 406, 3624, 9901, 51160], "temperature":
  0.0, "avg_logprob": -0.1213303876210408, "compression_ratio": 1.6724137931034482,
  "no_speech_prob": 0.0009250330622307956}, {"id": 63, "seek": 38246, "start": 398.38,
  "end": 402.7, "text": " or maybe even increase recall because there was a problem
  with this precision oriented search", "tokens": [51160, 420, 1310, 754, 3488, 9901,
  570, 456, 390, 257, 1154, 365, 341, 18356, 21841, 3164, 51376], "temperature": 0.0,
  "avg_logprob": -0.1213303876210408, "compression_ratio": 1.6724137931034482, "no_speech_prob":
  0.0009250330622307956}, {"id": 64, "seek": 38246, "start": 403.58, "end": 409.82,
  "text": " and stay within the budget right so when I think about language models
  myself and I also worked at", "tokens": [51420, 293, 1754, 1951, 264, 4706, 558,
  370, 562, 286, 519, 466, 2856, 5245, 2059, 293, 286, 611, 2732, 412, 51732], "temperature":
  0.0, "avg_logprob": -0.1213303876210408, "compression_ratio": 1.6724137931034482,
  "no_speech_prob": 0.0009250330622307956}, {"id": 65, "seek": 40982, "start": 409.82,
  "end": 417.5, "text": " silo AI at one large client you know applying these models
  at web scale. The problem at web", "tokens": [50364, 3425, 78, 7318, 412, 472, 2416,
  6423, 291, 458, 9275, 613, 5245, 412, 3670, 4373, 13, 440, 1154, 412, 3670, 50748],
  "temperature": 0.0, "avg_logprob": -0.11600063112046984, "compression_ratio": 1.7112068965517242,
  "no_speech_prob": 0.0005339415511116385}, {"id": 66, "seek": 40982, "start": 417.5,
  "end": 423.34, "text": " scale is that you really need to go sub-second and not
  just sub-second you need to go like 10 milliseconds", "tokens": [50748, 4373, 307,
  300, 291, 534, 643, 281, 352, 1422, 12, 27375, 293, 406, 445, 1422, 12, 27375, 291,
  643, 281, 352, 411, 1266, 34184, 51040], "temperature": 0.0, "avg_logprob": -0.11600063112046984,
  "compression_ratio": 1.7112068965517242, "no_speech_prob": 0.0005339415511116385},
  {"id": 67, "seek": 40982, "start": 423.34, "end": 429.1, "text": " or so because
  all of these adapt because you have so many components in the search engine it''s
  also", "tokens": [51040, 420, 370, 570, 439, 295, 613, 6231, 570, 291, 362, 370,
  867, 6677, 294, 264, 3164, 2848, 309, 311, 611, 51328], "temperature": 0.0, "avg_logprob":
  -0.11600063112046984, "compression_ratio": 1.7112068965517242, "no_speech_prob":
  0.0005339415511116385}, {"id": 68, "seek": 40982, "start": 429.1, "end": 436.46,
  "text": " multilingual it''s also serving a specific country you know with that
  specific latency requirements", "tokens": [51328, 2120, 38219, 309, 311, 611, 8148,
  257, 2685, 1941, 291, 458, 365, 300, 2685, 27043, 7728, 51696], "temperature": 0.0,
  "avg_logprob": -0.11600063112046984, "compression_ratio": 1.7112068965517242, "no_speech_prob":
  0.0005339415511116385}, {"id": 69, "seek": 43646, "start": 436.46, "end": 442.62,
  "text": " and stuff and and then there is indexing how quickly you can index things
  right because you may", "tokens": [50364, 293, 1507, 293, 293, 550, 456, 307, 8186,
  278, 577, 2661, 291, 393, 8186, 721, 558, 570, 291, 815, 50672], "temperature":
  0.0, "avg_logprob": -0.11366842325451304, "compression_ratio": 1.7962962962962963,
  "no_speech_prob": 0.0016883693169802427}, {"id": 70, "seek": 43646, "start": 442.62,
  "end": 447.5, "text": " also face bottlenecks there so these these are the things
  that I keep thinking about but also the", "tokens": [50672, 611, 1851, 44641, 2761,
  456, 370, 613, 613, 366, 264, 721, 300, 286, 1066, 1953, 466, 457, 611, 264, 50916],
  "temperature": 0.0, "avg_logprob": -0.11366842325451304, "compression_ratio": 1.7962962962962963,
  "no_speech_prob": 0.0016883693169802427}, {"id": 71, "seek": 43646, "start": 447.5,
  "end": 453.97999999999996, "text": " thing that we talked a year ago in the port
  in the same podcast vector podcast is that you know the", "tokens": [50916, 551,
  300, 321, 2825, 257, 1064, 2057, 294, 264, 2436, 294, 264, 912, 7367, 8062, 7367,
  307, 300, 291, 458, 264, 51240], "temperature": 0.0, "avg_logprob": -0.11366842325451304,
  "compression_ratio": 1.7962962962962963, "no_speech_prob": 0.0016883693169802427},
  {"id": 72, "seek": 43646, "start": 453.97999999999996, "end": 460.85999999999996,
  "text": " models like trained by Microsoft for instance I can hardly imagine deploying
  them today in my", "tokens": [51240, 5245, 411, 8895, 538, 8116, 337, 5197, 286,
  393, 13572, 3811, 34198, 552, 965, 294, 452, 51584], "temperature": 0.0, "avg_logprob":
  -0.11366842325451304, "compression_ratio": 1.7962962962962963, "no_speech_prob":
  0.0016883693169802427}, {"id": 73, "seek": 43646, "start": 460.85999999999996, "end":
  466.14, "text": " practical setting because they will have like billions of parameters
  and so they will be probably", "tokens": [51584, 8496, 3287, 570, 436, 486, 362,
  411, 17375, 295, 9834, 293, 370, 436, 486, 312, 1391, 51848], "temperature": 0.0,
  "avg_logprob": -0.11366842325451304, "compression_ratio": 1.7962962962962963, "no_speech_prob":
  0.0016883693169802427}, {"id": 74, "seek": 46614, "start": 466.14, "end": 471.9,
  "text": " slower and also how do I fine tune them how much server capacity I will
  need to fine tune them and", "tokens": [50364, 14009, 293, 611, 577, 360, 286, 2489,
  10864, 552, 577, 709, 7154, 6042, 286, 486, 643, 281, 2489, 10864, 552, 293, 50652],
  "temperature": 0.0, "avg_logprob": -0.10158433697440407, "compression_ratio": 1.6986899563318778,
  "no_speech_prob": 0.0009660437935963273}, {"id": 75, "seek": 46614, "start": 471.9,
  "end": 479.34, "text": " so that''s why I thought you know from the discussion with
  multi-peach right he pointed me to the", "tokens": [50652, 370, 300, 311, 983, 286,
  1194, 291, 458, 490, 264, 5017, 365, 4825, 12, 494, 608, 558, 415, 10932, 385, 281,
  264, 51024], "temperature": 0.0, "avg_logprob": -0.10158433697440407, "compression_ratio":
  1.6986899563318778, "no_speech_prob": 0.0009660437935963273}, {"id": 76, "seek":
  46614, "start": 479.34, "end": 487.5, "text": " Atlas paper where they basically
  are able to with a few examples fine tune the model so quickly", "tokens": [51024,
  32485, 3035, 689, 436, 1936, 366, 1075, 281, 365, 257, 1326, 5110, 2489, 10864,
  264, 2316, 370, 2661, 51432], "temperature": 0.0, "avg_logprob": -0.10158433697440407,
  "compression_ratio": 1.6986899563318778, "no_speech_prob": 0.0009660437935963273},
  {"id": 77, "seek": 46614, "start": 488.38, "end": 493.41999999999996, "text": "
  and it will have substantially less parameters so it becomes more practical you
  know both on fine", "tokens": [51476, 293, 309, 486, 362, 30797, 1570, 9834, 370,
  309, 3643, 544, 8496, 291, 458, 1293, 322, 2489, 51728], "temperature": 0.0, "avg_logprob":
  -0.10158433697440407, "compression_ratio": 1.6986899563318778, "no_speech_prob":
  0.0009660437935963273}, {"id": 78, "seek": 49342, "start": 493.42, "end": 499.18,
  "text": " tuning side and also on serving side and these are the topics that I keep
  thinking before I enter the", "tokens": [50364, 15164, 1252, 293, 611, 322, 8148,
  1252, 293, 613, 366, 264, 8378, 300, 286, 1066, 1953, 949, 286, 3242, 264, 50652],
  "temperature": 0.0, "avg_logprob": -0.11291148519923544, "compression_ratio": 1.8228782287822878,
  "no_speech_prob": 0.010798160918056965}, {"id": 79, "seek": 49342, "start": 499.82,
  "end": 504.94, "text": " is it chat GPT is it sexy is it cool is it answering my
  questions you know can I actually", "tokens": [50684, 307, 309, 5081, 26039, 51,
  307, 309, 13701, 307, 309, 1627, 307, 309, 13430, 452, 1651, 291, 458, 393, 286,
  767, 50940], "temperature": 0.0, "avg_logprob": -0.11291148519923544, "compression_ratio":
  1.8228782287822878, "no_speech_prob": 0.010798160918056965}, {"id": 80, "seek":
  49342, "start": 504.94, "end": 511.1, "text": " deploy it and not have angry faces
  from DevOps saying hey you just crossed all the like we are low", "tokens": [50940,
  7274, 309, 293, 406, 362, 6884, 8475, 490, 43051, 1566, 4177, 291, 445, 14622, 439,
  264, 411, 321, 366, 2295, 51248], "temperature": 0.0, "avg_logprob": -0.11291148519923544,
  "compression_ratio": 1.8228782287822878, "no_speech_prob": 0.010798160918056965},
  {"id": 81, "seek": 49342, "start": 511.1, "end": 516.3000000000001, "text": " margin
  on search and you are just you know way above that so sorry we cannot deploy this
  so these are", "tokens": [51248, 10270, 322, 3164, 293, 291, 366, 445, 291, 458,
  636, 3673, 300, 370, 2597, 321, 2644, 7274, 341, 370, 613, 366, 51508], "temperature":
  0.0, "avg_logprob": -0.11291148519923544, "compression_ratio": 1.8228782287822878,
  "no_speech_prob": 0.010798160918056965}, {"id": 82, "seek": 49342, "start": 516.3000000000001,
  "end": 522.62, "text": " the questions I''m thinking about a lot yeah that I think
  there''s a couple things in pack and no one''s", "tokens": [51508, 264, 1651, 286,
  478, 1953, 466, 257, 688, 1338, 300, 286, 519, 456, 311, 257, 1916, 721, 294, 2844,
  293, 572, 472, 311, 51824], "temperature": 0.0, "avg_logprob": -0.11291148519923544,
  "compression_ratio": 1.8228782287822878, "no_speech_prob": 0.010798160918056965},
  {"id": 83, "seek": 52262, "start": 522.62, "end": 527.26, "text": " helped me develop
  the abstraction around the end-to-end search framework more than you so thank you",
  "tokens": [50364, 4254, 385, 1499, 264, 37765, 926, 264, 917, 12, 1353, 12, 521,
  3164, 8388, 544, 813, 291, 370, 1309, 291, 50596], "temperature": 0.0, "avg_logprob":
  -0.1812877655029297, "compression_ratio": 1.798780487804878, "no_speech_prob": 0.004123232793062925},
  {"id": 84, "seek": 52262, "start": 527.26, "end": 531.1, "text": " so with the with
  the pyramid diagrams and these kind of things it''s so helpful and yeah you", "tokens":
  [50596, 370, 365, 264, 365, 264, 25950, 36709, 293, 613, 733, 295, 721, 309, 311,
  370, 4961, 293, 1338, 291, 50788], "temperature": 0.0, "avg_logprob": -0.1812877655029297,
  "compression_ratio": 1.798780487804878, "no_speech_prob": 0.004123232793062925},
  {"id": 85, "seek": 52262, "start": 531.1, "end": 535.74, "text": " mentioned like
  the approximate nearest neighbor then one up you have where I see is the information",
  "tokens": [50788, 2835, 411, 264, 30874, 23831, 5987, 550, 472, 493, 291, 362, 689,
  286, 536, 307, 264, 1589, 51020], "temperature": 0.0, "avg_logprob": -0.1812877655029297,
  "compression_ratio": 1.798780487804878, "no_speech_prob": 0.004123232793062925},
  {"id": 86, "seek": 52262, "start": 535.74, "end": 540.94, "text": " retrieval layer
  where you have the you know dense vector search BM25 split covert that layer and",
  "tokens": [51020, 19817, 3337, 4583, 689, 291, 362, 264, 291, 458, 18011, 8062,
  3164, 15901, 6074, 7472, 45985, 300, 4583, 293, 51280], "temperature": 0.0, "avg_logprob":
  -0.1812877655029297, "compression_ratio": 1.798780487804878, "no_speech_prob": 0.004123232793062925},
  {"id": 87, "seek": 52262, "start": 540.94, "end": 546.54, "text": " then at the
  top you have like what I think is going to be the chat GPT layer that''s like that
  would", "tokens": [51280, 550, 412, 264, 1192, 291, 362, 411, 437, 286, 519, 307,
  516, 281, 312, 264, 5081, 26039, 51, 4583, 300, 311, 411, 300, 576, 51560], "temperature":
  0.0, "avg_logprob": -0.1812877655029297, "compression_ratio": 1.798780487804878,
  "no_speech_prob": 0.004123232793062925}, {"id": 88, "seek": 52262, "start": 546.54,
  "end": 549.5, "text": " be my current predict and we''re going to talk about neural
  search frameworks that they can do more on", "tokens": [51560, 312, 452, 2190, 6069,
  293, 321, 434, 516, 281, 751, 466, 18161, 3164, 29834, 300, 436, 393, 360, 544,
  322, 51708], "temperature": 0.0, "avg_logprob": -0.1812877655029297, "compression_ratio":
  1.798780487804878, "no_speech_prob": 0.004123232793062925}, {"id": 89, "seek": 54950,
  "start": 549.5, "end": 560.62, "text": " the wv8 podcast yeah well maybe to just
  say a little bit one of our favorite partners that we''ve", "tokens": [50364, 264,
  261, 85, 23, 7367, 1338, 731, 1310, 281, 445, 584, 257, 707, 857, 472, 295, 527,
  2954, 4462, 300, 321, 600, 50920], "temperature": 0.0, "avg_logprob": -0.1459484100341797,
  "compression_ratio": 1.5685483870967742, "no_speech_prob": 0.0014912751503288746},
  {"id": 90, "seek": 54950, "start": 560.62, "end": 566.38, "text": " been working
  with is neural magic and neural magic is doing sparsity inference acceleration where",
  "tokens": [50920, 668, 1364, 365, 307, 18161, 5585, 293, 18161, 5585, 307, 884,
  637, 685, 507, 38253, 17162, 689, 51208], "temperature": 0.0, "avg_logprob": -0.1459484100341797,
  "compression_ratio": 1.5685483870967742, "no_speech_prob": 0.0014912751503288746},
  {"id": 91, "seek": 54950, "start": 566.38, "end": 571.9, "text": " they''ve recently
  one of their papers is about getting the 175 billion parameter GPT model to run",
  "tokens": [51208, 436, 600, 3938, 472, 295, 641, 10577, 307, 466, 1242, 264, 41165,
  5218, 13075, 26039, 51, 2316, 281, 1190, 51484], "temperature": 0.0, "avg_logprob":
  -0.1459484100341797, "compression_ratio": 1.5685483870967742, "no_speech_prob":
  0.0014912751503288746}, {"id": 92, "seek": 54950, "start": 571.9, "end": 577.74,
  "text": " on a single GPU I know that you know you can probably compile these large
  language models on like", "tokens": [51484, 322, 257, 2167, 18407, 286, 458, 300,
  291, 458, 291, 393, 1391, 31413, 613, 2416, 2856, 5245, 322, 411, 51776], "temperature":
  0.0, "avg_logprob": -0.1459484100341797, "compression_ratio": 1.5685483870967742,
  "no_speech_prob": 0.0014912751503288746}, {"id": 93, "seek": 57774, "start": 577.74,
  "end": 583.66, "text": " Nvidia Triton server and do it that way but I think that
  this sparsity acceleration for CPUs", "tokens": [50364, 46284, 1765, 270, 266, 7154,
  293, 360, 309, 300, 636, 457, 286, 519, 300, 341, 637, 685, 507, 17162, 337, 13199,
  82, 50660], "temperature": 0.0, "avg_logprob": -0.08642537173102884, "compression_ratio":
  1.6101694915254237, "no_speech_prob": 0.0023990909103304148}, {"id": 94, "seek":
  57774, "start": 583.66, "end": 588.0600000000001, "text": " is just incredibly exciting
  for that particular dimension of it and yeah I think what you said", "tokens": [50660,
  307, 445, 6252, 4670, 337, 300, 1729, 10139, 295, 309, 293, 1338, 286, 519, 437,
  291, 848, 50880], "temperature": 0.0, "avg_logprob": -0.08642537173102884, "compression_ratio":
  1.6101694915254237, "no_speech_prob": 0.0023990909103304148}, {"id": 95, "seek":
  57774, "start": 588.0600000000001, "end": 596.86, "text": " inspired so many ideas
  yeah I sort of like like what I value in your approach is that you run", "tokens":
  [50880, 7547, 370, 867, 3487, 1338, 286, 1333, 295, 411, 411, 437, 286, 2158, 294,
  428, 3109, 307, 300, 291, 1190, 51320], "temperature": 0.0, "avg_logprob": -0.08642537173102884,
  "compression_ratio": 1.6101694915254237, "no_speech_prob": 0.0023990909103304148},
  {"id": 96, "seek": 57774, "start": 597.58, "end": 602.78, "text": " probably like
  a basketball player converted into a marathon runner with the same capacity you
  have", "tokens": [51356, 1391, 411, 257, 11767, 4256, 16424, 666, 257, 27601, 24376,
  365, 264, 912, 6042, 291, 362, 51616], "temperature": 0.0, "avg_logprob": -0.08642537173102884,
  "compression_ratio": 1.6101694915254237, "no_speech_prob": 0.0023990909103304148},
  {"id": 97, "seek": 60278, "start": 602.78, "end": 609.66, "text": " to play a game
  you know that you basically run super quick and fast and long distances you know",
  "tokens": [50364, 281, 862, 257, 1216, 291, 458, 300, 291, 1936, 1190, 1687, 1702,
  293, 2370, 293, 938, 22182, 291, 458, 50708], "temperature": 0.0, "avg_logprob":
  -0.08211185281926936, "compression_ratio": 1.7065217391304348, "no_speech_prob":
  0.004629852715879679}, {"id": 98, "seek": 60278, "start": 609.66, "end": 614.4599999999999,
  "text": " on the research side and I love this approach really really because it
  opens up a lot of", "tokens": [50708, 322, 264, 2132, 1252, 293, 286, 959, 341,
  3109, 534, 534, 570, 309, 9870, 493, 257, 688, 295, 50948], "temperature": 0.0,
  "avg_logprob": -0.08211185281926936, "compression_ratio": 1.7065217391304348, "no_speech_prob":
  0.004629852715879679}, {"id": 99, "seek": 60278, "start": 614.4599999999999, "end":
  620.86, "text": " opportunities I sort of like because I come from the engineering
  background yeah I did my PhD", "tokens": [50948, 4786, 286, 1333, 295, 411, 570,
  286, 808, 490, 264, 7043, 3678, 1338, 286, 630, 452, 14476, 51268], "temperature":
  0.0, "avg_logprob": -0.08211185281926936, "compression_ratio": 1.7065217391304348,
  "no_speech_prob": 0.004629852715879679}, {"id": 100, "seek": 60278, "start": 620.86,
  "end": 627.02, "text": " but it was like 11 years ago so I most of my time I spent
  in production you know great systems", "tokens": [51268, 457, 309, 390, 411, 2975,
  924, 2057, 370, 286, 881, 295, 452, 565, 286, 4418, 294, 4265, 291, 458, 869, 3652,
  51576], "temperature": 0.0, "avg_logprob": -0.08211185281926936, "compression_ratio":
  1.7065217391304348, "no_speech_prob": 0.004629852715879679}, {"id": 101, "seek":
  60278, "start": 627.02, "end": 632.4599999999999, "text": " and every time you just
  try to move a little bit like okay let''s add this and oh the cost is this", "tokens":
  [51576, 293, 633, 565, 291, 445, 853, 281, 1286, 257, 707, 857, 411, 1392, 718,
  311, 909, 341, 293, 1954, 264, 2063, 307, 341, 51848], "temperature": 0.0, "avg_logprob":
  -0.08211185281926936, "compression_ratio": 1.7065217391304348, "no_speech_prob":
  0.004629852715879679}, {"id": 102, "seek": 63246, "start": 632.46, "end": 639.1800000000001,
  "text": " oh sorry okay it will take me now to two more weeks to index my content
  so and we have", "tokens": [50364, 1954, 2597, 1392, 309, 486, 747, 385, 586, 281,
  732, 544, 3259, 281, 8186, 452, 2701, 370, 293, 321, 362, 50700], "temperature":
  0.0, "avg_logprob": -0.09236274368461521, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.001577185234054923}, {"id": 103, "seek": 63246, "start": 639.1800000000001,
  "end": 645.4200000000001, "text": " for this what is the use case so you trickle
  back to like almost like product level management", "tokens": [50700, 337, 341,
  437, 307, 264, 764, 1389, 370, 291, 4282, 306, 646, 281, 411, 1920, 411, 1674, 1496,
  4592, 51012], "temperature": 0.0, "avg_logprob": -0.09236274368461521, "compression_ratio":
  1.709090909090909, "no_speech_prob": 0.001577185234054923}, {"id": 104, "seek":
  63246, "start": 646.38, "end": 651.02, "text": " and so you will get these questions
  inevitably like okay why are we doing this like what''s the", "tokens": [51060,
  293, 370, 291, 486, 483, 613, 1651, 28171, 411, 1392, 983, 366, 321, 884, 341, 411,
  437, 311, 264, 51292], "temperature": 0.0, "avg_logprob": -0.09236274368461521,
  "compression_ratio": 1.709090909090909, "no_speech_prob": 0.001577185234054923},
  {"id": 105, "seek": 63246, "start": 651.02, "end": 657.4200000000001, "text": "
  actual trade off what''s the benefit of bringing this into production right and
  but at the same time", "tokens": [51292, 3539, 4923, 766, 437, 311, 264, 5121, 295,
  5062, 341, 666, 4265, 558, 293, 457, 412, 264, 912, 565, 51612], "temperature":
  0.0, "avg_logprob": -0.09236274368461521, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.001577185234054923}, {"id": 106, "seek": 65742, "start": 657.42,
  "end": 663.26, "text": " I''m fascinated by this I mean this will not stop for sure
  right would you agree to that statement", "tokens": [50364, 286, 478, 24597, 538,
  341, 286, 914, 341, 486, 406, 1590, 337, 988, 558, 576, 291, 3986, 281, 300, 5629,
  50656], "temperature": 0.0, "avg_logprob": -0.21674811045328776, "compression_ratio":
  1.6455696202531647, "no_speech_prob": 0.000719190516974777}, {"id": 107, "seek":
  65742, "start": 664.86, "end": 672.2199999999999, "text": " yeah I think and there''s
  uh so I know Hagen Faces recently published their they open source of data", "tokens":
  [50736, 1338, 286, 519, 293, 456, 311, 2232, 370, 286, 458, 389, 4698, 479, 2116,
  3938, 6572, 641, 436, 1269, 4009, 295, 1412, 51104], "temperature": 0.0, "avg_logprob":
  -0.21674811045328776, "compression_ratio": 1.6455696202531647, "no_speech_prob":
  0.000719190516974777}, {"id": 108, "seek": 65742, "start": 672.2199999999999, "end":
  678.4599999999999, "text": " said they did with surge AI on getting these um human
  annotations to train the reward model in", "tokens": [51104, 848, 436, 630, 365,
  18989, 7318, 322, 1242, 613, 1105, 1952, 25339, 763, 281, 3847, 264, 7782, 2316,
  294, 51416], "temperature": 0.0, "avg_logprob": -0.21674811045328776, "compression_ratio":
  1.6455696202531647, "no_speech_prob": 0.000719190516974777}, {"id": 109, "seek":
  65742, "start": 678.4599999999999, "end": 684.2199999999999, "text": " the reinforced
  learning human feedback strategy so I think they''ll they''ll be an open sourcing
  of", "tokens": [51416, 264, 31365, 2539, 1952, 5824, 5206, 370, 286, 519, 436, 603,
  436, 603, 312, 364, 1269, 11006, 2175, 295, 51704], "temperature": 0.0, "avg_logprob":
  -0.21674811045328776, "compression_ratio": 1.6455696202531647, "no_speech_prob":
  0.000719190516974777}, {"id": 110, "seek": 68422, "start": 684.22, "end": 688.46,
  "text": " the data of the data that you need to train the models and then yeah I
  think pretty soon they''ll", "tokens": [50364, 264, 1412, 295, 264, 1412, 300, 291,
  643, 281, 3847, 264, 5245, 293, 550, 1338, 286, 519, 1238, 2321, 436, 603, 50576],
  "temperature": 0.0, "avg_logprob": -0.10111456650954026, "compression_ratio": 1.789090909090909,
  "no_speech_prob": 0.0008320531924255192}, {"id": 111, "seek": 68422, "start": 688.46,
  "end": 694.86, "text": " be open source versions of it I think open AI um I I''m
  very curious about this like kind of data", "tokens": [50576, 312, 1269, 4009, 9606,
  295, 309, 286, 519, 1269, 7318, 1105, 286, 286, 478, 588, 6369, 466, 341, 411, 733,
  295, 1412, 50896], "temperature": 0.0, "avg_logprob": -0.10111456650954026, "compression_ratio":
  1.789090909090909, "no_speech_prob": 0.0008320531924255192}, {"id": 112, "seek":
  68422, "start": 694.86, "end": 699.9, "text": " flywheel idea whereby open sourcing
  the model they spend a ton of money on letting you use it for free", "tokens": [50896,
  3603, 22830, 1558, 36998, 1269, 11006, 2175, 264, 2316, 436, 3496, 257, 2952, 295,
  1460, 322, 8295, 291, 764, 309, 337, 1737, 51148], "temperature": 0.0, "avg_logprob":
  -0.10111456650954026, "compression_ratio": 1.789090909090909, "no_speech_prob":
  0.0008320531924255192}, {"id": 113, "seek": 68422, "start": 699.9, "end": 705.4200000000001,
  "text": " but then they get the data of how you want to use it and so very curious
  how that leads to more", "tokens": [51148, 457, 550, 436, 483, 264, 1412, 295, 577,
  291, 528, 281, 764, 309, 293, 370, 588, 6369, 577, 300, 6689, 281, 544, 51424],
  "temperature": 0.0, "avg_logprob": -0.10111456650954026, "compression_ratio": 1.789090909090909,
  "no_speech_prob": 0.0008320531924255192}, {"id": 114, "seek": 68422, "start": 706.22,
  "end": 711.6600000000001, "text": " to a better model my PhD advisor is a world
  class expert in class imbalance like understanding that", "tokens": [51464, 281,
  257, 1101, 2316, 452, 14476, 19161, 307, 257, 1002, 1508, 5844, 294, 1508, 43007,
  411, 3701, 300, 51736], "temperature": 0.0, "avg_logprob": -0.10111456650954026,
  "compression_ratio": 1.789090909090909, "no_speech_prob": 0.0008320531924255192},
  {"id": 115, "seek": 71166, "start": 711.66, "end": 716.4599999999999, "text": "
  machine learning models they do not perform well on long tail you know if you have
  an imbalance", "tokens": [50364, 3479, 2539, 5245, 436, 360, 406, 2042, 731, 322,
  938, 6838, 291, 458, 498, 291, 362, 364, 43007, 50604], "temperature": 0.0, "avg_logprob":
  -0.13602939673832484, "compression_ratio": 1.718978102189781, "no_speech_prob":
  0.0011256723664700985}, {"id": 116, "seek": 71166, "start": 716.4599999999999, "end":
  721.66, "text": " data so it''s a lot of like the bias discussion things like that
  so I''m I''m curious maybe it helps", "tokens": [50604, 1412, 370, 309, 311, 257,
  688, 295, 411, 264, 12577, 5017, 721, 411, 300, 370, 286, 478, 286, 478, 6369, 1310,
  309, 3665, 50864], "temperature": 0.0, "avg_logprob": -0.13602939673832484, "compression_ratio":
  1.718978102189781, "no_speech_prob": 0.0011256723664700985}, {"id": 117, "seek":
  71166, "start": 721.66, "end": 728.06, "text": " the long tail getting all this
  data yeah it''s still not exactly how it will get better I think", "tokens": [50864,
  264, 938, 6838, 1242, 439, 341, 1412, 1338, 309, 311, 920, 406, 2293, 577, 309,
  486, 483, 1101, 286, 519, 51184], "temperature": 0.0, "avg_logprob": -0.13602939673832484,
  "compression_ratio": 1.718978102189781, "no_speech_prob": 0.0011256723664700985},
  {"id": 118, "seek": 71166, "start": 729.02, "end": 733.5799999999999, "text": "
  one thing I''ve said previously is like there was this paper from Emily Bender and
  um", "tokens": [51232, 472, 551, 286, 600, 848, 8046, 307, 411, 456, 390, 341, 3035,
  490, 15034, 363, 3216, 293, 1105, 51460], "temperature": 0.0, "avg_logprob": -0.13602939673832484,
  "compression_ratio": 1.718978102189781, "no_speech_prob": 0.0011256723664700985},
  {"id": 119, "seek": 71166, "start": 734.38, "end": 740.38, "text": " caller is the
  last name sorry it but it''s called unmeaning understanding in big data and it makes",
  "tokens": [51500, 48324, 307, 264, 1036, 1315, 2597, 309, 457, 309, 311, 1219, 517,
  1398, 8415, 3701, 294, 955, 1412, 293, 309, 1669, 51800], "temperature": 0.0, "avg_logprob":
  -0.13602939673832484, "compression_ratio": 1.718978102189781, "no_speech_prob":
  0.0011256723664700985}, {"id": 120, "seek": 74038, "start": 740.38, "end": 744.7,
  "text": " this argument that it''s like language models by predicting the next token
  will never achieve", "tokens": [50364, 341, 6770, 300, 309, 311, 411, 2856, 5245,
  538, 32884, 264, 958, 14862, 486, 1128, 4584, 50580], "temperature": 0.0, "avg_logprob":
  -0.11707884986121375, "compression_ratio": 1.84375, "no_speech_prob": 0.0022324423771351576},
  {"id": 121, "seek": 74038, "start": 744.7, "end": 751.18, "text": " meaning because
  it''s like an octopus underneath the ocean of two stranded islanders and it''s just",
  "tokens": [50580, 3620, 570, 309, 311, 411, 364, 27962, 7223, 264, 7810, 295, 732,
  44394, 6077, 433, 293, 309, 311, 445, 50904], "temperature": 0.0, "avg_logprob":
  -0.11707884986121375, "compression_ratio": 1.84375, "no_speech_prob": 0.0022324423771351576},
  {"id": 122, "seek": 74038, "start": 751.18, "end": 756.06, "text": " mimicking their
  language but if it if something like a bear is to show up on the island and it goes",
  "tokens": [50904, 12247, 10401, 641, 2856, 457, 498, 309, 498, 746, 411, 257, 6155,
  307, 281, 855, 493, 322, 264, 6077, 293, 309, 1709, 51148], "temperature": 0.0,
  "avg_logprob": -0.11707884986121375, "compression_ratio": 1.84375, "no_speech_prob":
  0.0022324423771351576}, {"id": 123, "seek": 74038, "start": 756.06, "end": 759.98,
  "text": " help a bear then the octopus is like oh I don''t know what a bear is like
  yeah I''ll do more", "tokens": [51148, 854, 257, 6155, 550, 264, 27962, 307, 411,
  1954, 286, 500, 380, 458, 437, 257, 6155, 307, 411, 1338, 286, 603, 360, 544, 51344],
  "temperature": 0.0, "avg_logprob": -0.11707884986121375, "compression_ratio": 1.84375,
  "no_speech_prob": 0.0022324423771351576}, {"id": 124, "seek": 74038, "start": 761.26,
  "end": 765.34, "text": " but I think what we''re seeing with the reinforcement learning
  thing is that it''s like it''s", "tokens": [51408, 457, 286, 519, 437, 321, 434,
  2577, 365, 264, 29280, 2539, 551, 307, 300, 309, 311, 411, 309, 311, 51612], "temperature":
  0.0, "avg_logprob": -0.11707884986121375, "compression_ratio": 1.84375, "no_speech_prob":
  0.0022324423771351576}, {"id": 125, "seek": 76534, "start": 765.34, "end": 769.34,
  "text": " acting it''s there''s there''s this other paper called experience grounds
  language", "tokens": [50364, 6577, 309, 311, 456, 311, 456, 311, 341, 661, 3035,
  1219, 1752, 19196, 2856, 50564], "temperature": 0.0, "avg_logprob": -0.1400560292330655,
  "compression_ratio": 1.9036144578313252, "no_speech_prob": 0.0016971861477941275},
  {"id": 126, "seek": 76534, "start": 769.34, "end": 776.14, "text": " it''s about
  you you need to it''s like the levels of sort of developing meaning and one of it
  is", "tokens": [50564, 309, 311, 466, 291, 291, 643, 281, 309, 311, 411, 264, 4358,
  295, 1333, 295, 6416, 3620, 293, 472, 295, 309, 307, 50904], "temperature": 0.0,
  "avg_logprob": -0.1400560292330655, "compression_ratio": 1.9036144578313252, "no_speech_prob":
  0.0016971861477941275}, {"id": 127, "seek": 76534, "start": 776.14, "end": 781.6600000000001,
  "text": " like about the importance of acting acting in your environment I''m I''m
  kind of going around right", "tokens": [50904, 411, 466, 264, 7379, 295, 6577, 6577,
  294, 428, 2823, 286, 478, 286, 478, 733, 295, 516, 926, 558, 51180], "temperature":
  0.0, "avg_logprob": -0.1400560292330655, "compression_ratio": 1.9036144578313252,
  "no_speech_prob": 0.0016971861477941275}, {"id": 128, "seek": 76534, "start": 781.6600000000001,
  "end": 786.86, "text": " here but I also see like this causal inference stuff and
  uh Judea Pearl has this ladder of causality", "tokens": [51180, 510, 457, 286, 611,
  536, 411, 341, 38755, 38253, 1507, 293, 2232, 36521, 64, 24639, 575, 341, 18325,
  295, 3302, 1860, 51440], "temperature": 0.0, "avg_logprob": -0.1400560292330655,
  "compression_ratio": 1.9036144578313252, "no_speech_prob": 0.0016971861477941275},
  {"id": 129, "seek": 76534, "start": 786.86, "end": 792.7800000000001, "text": "
  where uh it''s you act you make interventions but then the the the the top of the
  ladder of causality", "tokens": [51440, 689, 2232, 309, 311, 291, 605, 291, 652,
  20924, 457, 550, 264, 264, 264, 264, 1192, 295, 264, 18325, 295, 3302, 1860, 51736],
  "temperature": 0.0, "avg_logprob": -0.1400560292330655, "compression_ratio": 1.9036144578313252,
  "no_speech_prob": 0.0016971861477941275}, {"id": 130, "seek": 79278, "start": 792.86,
  "end": 798.22, "text": " is you can understand uh counterfactuals and so that last
  part I have no idea how that''s going to", "tokens": [50368, 307, 291, 393, 1223,
  2232, 5682, 44919, 901, 82, 293, 370, 300, 1036, 644, 286, 362, 572, 1558, 577,
  300, 311, 516, 281, 50636], "temperature": 0.0, "avg_logprob": -0.1769057880748402,
  "compression_ratio": 1.7030075187969924, "no_speech_prob": 0.0030927034094929695},
  {"id": 131, "seek": 79278, "start": 798.22, "end": 802.86, "text": " be achieved
  yet but I clearly chat GPT is now like acting so it''s different from the", "tokens":
  [50636, 312, 11042, 1939, 457, 286, 4448, 5081, 26039, 51, 307, 586, 411, 6577,
  370, 309, 311, 819, 490, 264, 50868], "temperature": 0.0, "avg_logprob": -0.1769057880748402,
  "compression_ratio": 1.7030075187969924, "no_speech_prob": 0.0030927034094929695},
  {"id": 132, "seek": 79278, "start": 802.86, "end": 808.22, "text": " yeah yeah the
  next word thing yeah I think what coming back to chat GPT like what um", "tokens":
  [50868, 1338, 1338, 264, 958, 1349, 551, 1338, 286, 519, 437, 1348, 646, 281, 5081,
  26039, 51, 411, 437, 1105, 51136], "temperature": 0.0, "avg_logprob": -0.1769057880748402,
  "compression_ratio": 1.7030075187969924, "no_speech_prob": 0.0030927034094929695},
  {"id": 133, "seek": 79278, "start": 808.9399999999999, "end": 813.9, "text": " impressed
  me maybe the most is uh so I had I had this problem uh I was I was working on",
  "tokens": [51172, 11679, 385, 1310, 264, 881, 307, 2232, 370, 286, 632, 286, 632,
  341, 1154, 2232, 286, 390, 286, 390, 1364, 322, 51420], "temperature": 0.0, "avg_logprob":
  -0.1769057880748402, "compression_ratio": 1.7030075187969924, "no_speech_prob":
  0.0030927034094929695}, {"id": 134, "seek": 79278, "start": 813.9, "end": 820.38,
  "text": " billion scale and then search algorithm with with the group of researchers
  and and engineers like", "tokens": [51420, 5218, 4373, 293, 550, 3164, 9284, 365,
  365, 264, 1594, 295, 10309, 293, 293, 11955, 411, 51744], "temperature": 0.0, "avg_logprob":
  -0.1769057880748402, "compression_ratio": 1.7030075187969924, "no_speech_prob":
  0.0030927034094929695}, {"id": 135, "seek": 82038, "start": 820.46, "end": 827.02,
  "text": " almost a year ago so I invented this this algorithm I called it candy
  like of course you know", "tokens": [50368, 1920, 257, 1064, 2057, 370, 286, 14479,
  341, 341, 9284, 286, 1219, 309, 11237, 411, 295, 1164, 291, 458, 50696], "temperature":
  0.0, "avg_logprob": -0.1444146736808445, "compression_ratio": 1.71875, "no_speech_prob":
  0.0003906735510099679}, {"id": 136, "seek": 82038, "start": 827.02, "end": 833.9,
  "text": " not not meaning my surname but in any case with a k um it''s all open
  source and GitHub I''ll make", "tokens": [50696, 406, 406, 3620, 452, 50152, 457,
  294, 604, 1389, 365, 257, 350, 1105, 309, 311, 439, 1269, 4009, 293, 23331, 286,
  603, 652, 51040], "temperature": 0.0, "avg_logprob": -0.1444146736808445, "compression_ratio":
  1.71875, "no_speech_prob": 0.0003906735510099679}, {"id": 137, "seek": 82038, "start":
  833.9, "end": 839.9, "text": " sure to link it and so the the problem was that it
  it would work on 10 million vectors it would work", "tokens": [51040, 988, 281,
  2113, 309, 293, 370, 264, 264, 1154, 390, 300, 309, 309, 576, 589, 322, 1266, 2459,
  18875, 309, 576, 589, 51340], "temperature": 0.0, "avg_logprob": -0.1444146736808445,
  "compression_ratio": 1.71875, "no_speech_prob": 0.0003906735510099679}, {"id": 138,
  "seek": 82038, "start": 839.9, "end": 845.34, "text": " on 100 million vectors but
  it would choke on one billion it would basically run out of memory", "tokens": [51340,
  322, 2319, 2459, 18875, 457, 309, 576, 34427, 322, 472, 5218, 309, 576, 1936, 1190,
  484, 295, 4675, 51612], "temperature": 0.0, "avg_logprob": -0.1444146736808445,
  "compression_ratio": 1.71875, "no_speech_prob": 0.0003906735510099679}, {"id": 139,
  "seek": 84534, "start": 846.14, "end": 851.34, "text": " uh and and I did it entirely
  in python right so maybe I I should have chosen in retrospect some", "tokens": [50404,
  2232, 293, 293, 286, 630, 309, 7696, 294, 38797, 558, 370, 1310, 286, 286, 820,
  362, 8614, 294, 34997, 512, 50664], "temperature": 0.0, "avg_logprob": -0.11971082492750518,
  "compression_ratio": 1.6208333333333333, "no_speech_prob": 0.003358519170433283},
  {"id": 140, "seek": 84534, "start": 851.34, "end": 856.94, "text": " other language
  but in any case I wanted to make this work um I couldn''t I ran out of time and
  I ran", "tokens": [50664, 661, 2856, 457, 294, 604, 1389, 286, 1415, 281, 652, 341,
  589, 1105, 286, 2809, 380, 286, 5872, 484, 295, 565, 293, 286, 5872, 50944], "temperature":
  0.0, "avg_logprob": -0.11971082492750518, "compression_ratio": 1.6208333333333333,
  "no_speech_prob": 0.003358519170433283}, {"id": 141, "seek": 84534, "start": 856.94,
  "end": 863.1800000000001, "text": " out of computer resource because it was given
  to us by Microsoft um for a limited period of time", "tokens": [50944, 484, 295,
  3820, 7684, 570, 309, 390, 2212, 281, 505, 538, 8116, 1105, 337, 257, 5567, 2896,
  295, 565, 51256], "temperature": 0.0, "avg_logprob": -0.11971082492750518, "compression_ratio":
  1.6208333333333333, "no_speech_prob": 0.003358519170433283}, {"id": 142, "seek":
  84534, "start": 864.0600000000001, "end": 870.86, "text": " so what I did is that
  I pasted that code into chat chat GPT and I said yeah first of all I tried", "tokens":
  [51300, 370, 437, 286, 630, 307, 300, 286, 1791, 292, 300, 3089, 666, 5081, 5081,
  26039, 51, 293, 286, 848, 1338, 700, 295, 439, 286, 3031, 51640], "temperature":
  0.0, "avg_logprob": -0.11971082492750518, "compression_ratio": 1.6208333333333333,
  "no_speech_prob": 0.003358519170433283}, {"id": 143, "seek": 87086, "start": 871.02,
  "end": 875.66, "text": " to paste the whole thing but it said well it''s too long
  so I had to focus on a specific part where I", "tokens": [50372, 281, 9163, 264,
  1379, 551, 457, 309, 848, 731, 309, 311, 886, 938, 370, 286, 632, 281, 1879, 322,
  257, 2685, 644, 689, 286, 50604], "temperature": 0.0, "avg_logprob": -0.10811215038447416,
  "compression_ratio": 1.8021582733812949, "no_speech_prob": 0.004470229148864746},
  {"id": 144, "seek": 87086, "start": 875.66, "end": 881.98, "text": " think the the
  problem you know kind of lurks and and it gave me the answer it said okay maybe
  try", "tokens": [50604, 519, 264, 264, 1154, 291, 458, 733, 295, 35583, 1694, 293,
  293, 309, 2729, 385, 264, 1867, 309, 848, 1392, 1310, 853, 50920], "temperature":
  0.0, "avg_logprob": -0.10811215038447416, "compression_ratio": 1.8021582733812949,
  "no_speech_prob": 0.004470229148864746}, {"id": 145, "seek": 87086, "start": 881.98,
  "end": 888.46, "text": " avoid using non-py arrays as much as you do try to pre-allocate
  them try to reset them and actually", "tokens": [50920, 5042, 1228, 2107, 12, 8200,
  41011, 382, 709, 382, 291, 360, 853, 281, 659, 12, 336, 42869, 552, 853, 281, 14322,
  552, 293, 767, 51244], "temperature": 0.0, "avg_logprob": -0.10811215038447416,
  "compression_ratio": 1.8021582733812949, "no_speech_prob": 0.004470229148864746},
  {"id": 146, "seek": 87086, "start": 888.46, "end": 893.02, "text": " I did that
  I just didn''t paste that portion of the code which was doing this so the the system
  didn''t", "tokens": [51244, 286, 630, 300, 286, 445, 994, 380, 9163, 300, 8044,
  295, 264, 3089, 597, 390, 884, 341, 370, 264, 264, 1185, 994, 380, 51472], "temperature":
  0.0, "avg_logprob": -0.10811215038447416, "compression_ratio": 1.8021582733812949,
  "no_speech_prob": 0.004470229148864746}, {"id": 147, "seek": 87086, "start": 893.02,
  "end": 899.1800000000001, "text": " know that but it was on the right on the right
  track but then when I did it a year sorry a day later", "tokens": [51472, 458, 300,
  457, 309, 390, 322, 264, 558, 322, 264, 558, 2837, 457, 550, 562, 286, 630, 309,
  257, 1064, 2597, 257, 786, 1780, 51780], "temperature": 0.0, "avg_logprob": -0.10811215038447416,
  "compression_ratio": 1.8021582733812949, "no_speech_prob": 0.004470229148864746},
  {"id": 148, "seek": 89918, "start": 899.7399999999999, "end": 905.7399999999999,
  "text": " the answer changed the question was exactly same but the answer changed
  and that kind of make me", "tokens": [50392, 264, 1867, 3105, 264, 1168, 390, 2293,
  912, 457, 264, 1867, 3105, 293, 300, 733, 295, 652, 385, 50692], "temperature":
  0.0, "avg_logprob": -0.1409247966294878, "compression_ratio": 1.7300884955752212,
  "no_speech_prob": 0.004194737412035465}, {"id": 149, "seek": 89918, "start": 906.3,
  "end": 913.26, "text": " really like uh what''s going on like is it learning as
  it goes can you explain this part like have", "tokens": [50720, 534, 411, 2232,
  437, 311, 516, 322, 411, 307, 309, 2539, 382, 309, 1709, 393, 291, 2903, 341, 644,
  411, 362, 51068], "temperature": 0.0, "avg_logprob": -0.1409247966294878, "compression_ratio":
  1.7300884955752212, "no_speech_prob": 0.004194737412035465}, {"id": 150, "seek":
  89918, "start": 913.26, "end": 919.7399999999999, "text": " you seen this in his
  behavior like was the casting generation of the yeah chat GPT sorry I was like",
  "tokens": [51068, 291, 1612, 341, 294, 702, 5223, 411, 390, 264, 17301, 5125, 295,
  264, 1338, 5081, 26039, 51, 2597, 286, 390, 411, 51392], "temperature": 0.0, "avg_logprob":
  -0.1409247966294878, "compression_ratio": 1.7300884955752212, "no_speech_prob":
  0.004194737412035465}, {"id": 151, "seek": 89918, "start": 919.7399999999999, "end":
  923.42, "text": " I was trying to follow along with the I think we''re going to
  talk about like approximation error", "tokens": [51392, 286, 390, 1382, 281, 1524,
  2051, 365, 264, 286, 519, 321, 434, 516, 281, 751, 466, 411, 28023, 6713, 51576],
  "temperature": 0.0, "avg_logprob": -0.1409247966294878, "compression_ratio": 1.7300884955752212,
  "no_speech_prob": 0.004194737412035465}, {"id": 152, "seek": 92342, "start": 923.5,
  "end": 929.9799999999999, "text": " with the AN and search as we scale it and I
  know we''re coming back to the chat GPT but I''ll be uh", "tokens": [50368, 365,
  264, 5252, 293, 3164, 382, 321, 4373, 309, 293, 286, 458, 321, 434, 1348, 646, 281,
  264, 5081, 26039, 51, 457, 286, 603, 312, 2232, 50692], "temperature": 0.0, "avg_logprob":
  -0.19311071868635651, "compression_ratio": 1.7445255474452555, "no_speech_prob":
  0.01498115062713623}, {"id": 153, "seek": 92342, "start": 929.9799999999999, "end":
  936.38, "text": " yeah so it''s like uh it''s like a tree decoding where uh it it
  has a probability density on the", "tokens": [50692, 1338, 370, 309, 311, 411, 2232,
  309, 311, 411, 257, 4230, 979, 8616, 689, 2232, 309, 309, 575, 257, 8482, 10305,
  322, 264, 51012], "temperature": 0.0, "avg_logprob": -0.19311071868635651, "compression_ratio":
  1.7445255474452555, "no_speech_prob": 0.01498115062713623}, {"id": 154, "seek":
  92342, "start": 936.38, "end": 940.62, "text": " length of vocabulary and you can
  take several paths through that tree for what you''re going to", "tokens": [51012,
  4641, 295, 19864, 293, 291, 393, 747, 2940, 14518, 807, 300, 4230, 337, 437, 291,
  434, 516, 281, 51224], "temperature": 0.0, "avg_logprob": -0.19311071868635651,
  "compression_ratio": 1.7445255474452555, "no_speech_prob": 0.01498115062713623},
  {"id": 155, "seek": 92342, "start": 940.62, "end": 946.86, "text": " output and
  uh you often randomly sample through the through the tree if that makes sense like
  um", "tokens": [51224, 5598, 293, 2232, 291, 2049, 16979, 6889, 807, 264, 807, 264,
  4230, 498, 300, 1669, 2020, 411, 1105, 51536], "temperature": 0.0, "avg_logprob":
  -0.19311071868635651, "compression_ratio": 1.7445255474452555, "no_speech_prob":
  0.01498115062713623}, {"id": 156, "seek": 92342, "start": 946.86, "end": 951.5,
  "text": " yeah yeah me does but I mean the answer was kind of like in some sense
  these two answers were", "tokens": [51536, 1338, 1338, 385, 775, 457, 286, 914,
  264, 1867, 390, 733, 295, 411, 294, 512, 2020, 613, 732, 6338, 645, 51768], "temperature":
  0.0, "avg_logprob": -0.19311071868635651, "compression_ratio": 1.7445255474452555,
  "no_speech_prob": 0.01498115062713623}, {"id": 157, "seek": 95150, "start": 951.5,
  "end": 956.78, "text": " complementary to each other right and and maybe I could
  go on and say hey what do you mean by", "tokens": [50364, 40705, 281, 1184, 661,
  558, 293, 293, 1310, 286, 727, 352, 322, 293, 584, 4177, 437, 360, 291, 914, 538,
  50628], "temperature": 0.0, "avg_logprob": -0.12264800071716309, "compression_ratio":
  1.719298245614035, "no_speech_prob": 0.001135017373599112}, {"id": 158, "seek":
  95150, "start": 956.78, "end": 963.02, "text": " resetting can you because it didn''t
  provide any uh code examples it would just say reset and I was like", "tokens":
  [50628, 14322, 783, 393, 291, 570, 309, 994, 380, 2893, 604, 2232, 3089, 5110, 309,
  576, 445, 584, 14322, 293, 286, 390, 411, 50940], "temperature": 0.0, "avg_logprob":
  -0.12264800071716309, "compression_ratio": 1.719298245614035, "no_speech_prob":
  0.001135017373599112}, {"id": 159, "seek": 95150, "start": 963.02, "end": 970.06,
  "text": " what do you mean by reset I don''t have such a method like like like so
  I I think that that was maybe", "tokens": [50940, 437, 360, 291, 914, 538, 14322,
  286, 500, 380, 362, 1270, 257, 3170, 411, 411, 411, 370, 286, 286, 519, 300, 300,
  390, 1310, 51292], "temperature": 0.0, "avg_logprob": -0.12264800071716309, "compression_ratio":
  1.719298245614035, "no_speech_prob": 0.001135017373599112}, {"id": 160, "seek":
  95150, "start": 970.7, "end": 977.5, "text": " impressive part of chat GPT and um
  just to close off on that there was a recent discussion on", "tokens": [51324, 8992,
  644, 295, 5081, 26039, 51, 293, 1105, 445, 281, 1998, 766, 322, 300, 456, 390, 257,
  5162, 5017, 322, 51664], "temperature": 0.0, "avg_logprob": -0.12264800071716309,
  "compression_ratio": 1.719298245614035, "no_speech_prob": 0.001135017373599112},
  {"id": 161, "seek": 97750, "start": 977.98, "end": 983.26, "text": " on relevancy
  and matching text like where a lot of these search people see uh there was um",
  "tokens": [50388, 322, 25916, 6717, 293, 14324, 2487, 411, 689, 257, 688, 295, 613,
  3164, 561, 536, 2232, 456, 390, 1105, 50652], "temperature": 0.0, "avg_logprob":
  -0.14471053051692184, "compression_ratio": 1.7432432432432432, "no_speech_prob":
  0.0019175204215571284}, {"id": 162, "seek": 97750, "start": 983.26, "end": 992.3,
  "text": " there was this argument against chat GPT that let''s say if you go um
  you know use uh duck duck go", "tokens": [50652, 456, 390, 341, 6770, 1970, 5081,
  26039, 51, 300, 718, 311, 584, 498, 291, 352, 1105, 291, 458, 764, 2232, 12482,
  12482, 352, 51104], "temperature": 0.0, "avg_logprob": -0.14471053051692184, "compression_ratio":
  1.7432432432432432, "no_speech_prob": 0.0019175204215571284}, {"id": 163, "seek":
  97750, "start": 992.3, "end": 998.86, "text": " today you will see the links right
  you can go and examine the links and you can actually verify the", "tokens": [51104,
  965, 291, 486, 536, 264, 6123, 558, 291, 393, 352, 293, 17496, 264, 6123, 293, 291,
  393, 767, 16888, 264, 51432], "temperature": 0.0, "avg_logprob": -0.14471053051692184,
  "compression_ratio": 1.7432432432432432, "no_speech_prob": 0.0019175204215571284},
  {"id": 164, "seek": 97750, "start": 998.86, "end": 1004.22, "text": " information
  to some extent maybe not to full extent but to some extent in chat GPT you can do
  that", "tokens": [51432, 1589, 281, 512, 8396, 1310, 406, 281, 1577, 8396, 457,
  281, 512, 8396, 294, 5081, 26039, 51, 291, 393, 360, 300, 51700], "temperature":
  0.0, "avg_logprob": -0.14471053051692184, "compression_ratio": 1.7432432432432432,
  "no_speech_prob": 0.0019175204215571284}, {"id": 165, "seek": 100422, "start": 1004.22,
  "end": 1012.78, "text": " there is an answer that''s it so it''s it''s quite a jump
  from being able to kind of seemingly check", "tokens": [50364, 456, 307, 364, 1867,
  300, 311, 309, 370, 309, 311, 309, 311, 1596, 257, 3012, 490, 885, 1075, 281, 733,
  295, 18709, 1520, 50792], "temperature": 0.0, "avg_logprob": -0.09570505402304909,
  "compression_ratio": 1.7568807339449541, "no_speech_prob": 0.00084763701306656},
  {"id": 166, "seek": 100422, "start": 1012.78, "end": 1018.22, "text": " the is it
  trustworthy to well you have no way to do that what do you think of this aspect",
  "tokens": [50792, 264, 307, 309, 39714, 281, 731, 291, 362, 572, 636, 281, 360,
  300, 437, 360, 291, 519, 295, 341, 4171, 51064], "temperature": 0.0, "avg_logprob":
  -0.09570505402304909, "compression_ratio": 1.7568807339449541, "no_speech_prob":
  0.00084763701306656}, {"id": 167, "seek": 100422, "start": 1019.5, "end": 1024.78,
  "text": " yeah that''s brilliant I it makes me think about like well very broadly
  it makes me think about", "tokens": [51128, 1338, 300, 311, 10248, 286, 309, 1669,
  385, 519, 466, 411, 731, 588, 19511, 309, 1669, 385, 519, 466, 51392], "temperature":
  0.0, "avg_logprob": -0.09570505402304909, "compression_ratio": 1.7568807339449541,
  "no_speech_prob": 0.00084763701306656}, {"id": 168, "seek": 100422, "start": 1024.78,
  "end": 1030.38, "text": " artificial general intelligence compared to super intelligence
  sort so to say and like I think about", "tokens": [51392, 11677, 2674, 7599, 5347,
  281, 1687, 7599, 1333, 370, 281, 584, 293, 411, 286, 519, 466, 51672], "temperature":
  0.0, "avg_logprob": -0.09570505402304909, "compression_ratio": 1.7568807339449541,
  "no_speech_prob": 0.00084763701306656}, {"id": 169, "seek": 103038, "start": 1030.46,
  "end": 1035.5800000000002, "text": " the artificial general intelligence and like
  because open AI they''ve published web GPT and", "tokens": [50368, 264, 11677, 2674,
  7599, 293, 411, 570, 1269, 7318, 436, 600, 6572, 3670, 26039, 51, 293, 50624], "temperature":
  0.0, "avg_logprob": -0.16619372817705264, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.0011353311128914356}, {"id": 170, "seek": 103038, "start": 1035.5800000000002,
  "end": 1039.5800000000002, "text": " instruct GPT so instruct GPT is like the reinforcement
  learning from human feedback part", "tokens": [50624, 7232, 26039, 51, 370, 7232,
  26039, 51, 307, 411, 264, 29280, 2539, 490, 1952, 5824, 644, 50824], "temperature":
  0.0, "avg_logprob": -0.16619372817705264, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.0011353311128914356}, {"id": 171, "seek": 103038, "start": 1039.5800000000002,
  "end": 1044.3000000000002, "text": " and then web GPT is like the like the whole
  idea that we''re super excited about at wevea where", "tokens": [50824, 293, 550,
  3670, 26039, 51, 307, 411, 264, 411, 264, 1379, 1558, 300, 321, 434, 1687, 2919,
  466, 412, 321, 303, 64, 689, 51060], "temperature": 0.0, "avg_logprob": -0.16619372817705264,
  "compression_ratio": 1.709090909090909, "no_speech_prob": 0.0011353311128914356},
  {"id": 172, "seek": 103038, "start": 1044.3000000000002, "end": 1050.3000000000002,
  "text": " you search for context to append to the input and then like if you say
  like please uh ground your", "tokens": [51060, 291, 3164, 337, 4319, 281, 34116,
  281, 264, 4846, 293, 550, 411, 498, 291, 584, 411, 1767, 2232, 2727, 428, 51360],
  "temperature": 0.0, "avg_logprob": -0.16619372817705264, "compression_ratio": 1.709090909090909,
  "no_speech_prob": 0.0011353311128914356}, {"id": 173, "seek": 103038, "start": 1050.3000000000002,
  "end": 1055.42, "text": " answer in this information and then it''s a paragraph
  about like how the BM25 algorithm works like", "tokens": [51360, 1867, 294, 341,
  1589, 293, 550, 309, 311, 257, 18865, 466, 411, 577, 264, 15901, 6074, 9284, 1985,
  411, 51616], "temperature": 0.0, "avg_logprob": -0.16619372817705264, "compression_ratio":
  1.709090909090909, "no_speech_prob": 0.0011353311128914356}, {"id": 174, "seek":
  105542, "start": 1055.42, "end": 1060.22, "text": " I use this personally that way
  to hybrid search and understanding it and so like if you give it", "tokens": [50364,
  286, 764, 341, 5665, 300, 636, 281, 13051, 3164, 293, 3701, 309, 293, 370, 411,
  498, 291, 976, 309, 50604], "temperature": 0.0, "avg_logprob": -0.1789126638638771,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.000558963161893189},
  {"id": 175, "seek": 105542, "start": 1060.22, "end": 1066.14, "text": " the context
  it''s so much better and so I think I suspect that chat GBC under the hood does
  something", "tokens": [50604, 264, 4319, 309, 311, 370, 709, 1101, 293, 370, 286,
  519, 286, 9091, 300, 5081, 460, 7869, 833, 264, 13376, 775, 746, 50900], "temperature":
  0.0, "avg_logprob": -0.1789126638638771, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.000558963161893189}, {"id": 176, "seek": 105542, "start": 1066.14,
  "end": 1073.5800000000002, "text": " like a Google or a Bing API search and so it''s
  like general old but um yeah this idea like so", "tokens": [50900, 411, 257, 3329,
  420, 257, 30755, 9362, 3164, 293, 370, 309, 311, 411, 2674, 1331, 457, 1105, 1338,
  341, 1558, 411, 370, 51272], "temperature": 0.0, "avg_logprob": -0.1789126638638771,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.000558963161893189},
  {"id": 177, "seek": 105542, "start": 1073.5800000000002, "end": 1077.9, "text":
  " so so then this idea of super intelligence it uh because I''ve been like can I
  use chat GPT to help", "tokens": [51272, 370, 370, 550, 341, 1558, 295, 1687, 7599,
  309, 2232, 570, 286, 600, 668, 411, 393, 286, 764, 5081, 26039, 51, 281, 854, 51488],
  "temperature": 0.0, "avg_logprob": -0.1789126638638771, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.000558963161893189}, {"id": 178, "seek": 105542, "start": 1077.9,
  "end": 1083.02, "text": " me write like you know blog post survey papers things
  like that are relevant for trying to be a master", "tokens": [51488, 385, 2464,
  411, 291, 458, 6968, 2183, 8984, 10577, 721, 411, 300, 366, 7340, 337, 1382, 281,
  312, 257, 4505, 51744], "temperature": 0.0, "avg_logprob": -0.1789126638638771,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.000558963161893189},
  {"id": 179, "seek": 108302, "start": 1083.02, "end": 1088.94, "text": " of search
  and what I need from it is more so like citation recommendation right like I needed
  to", "tokens": [50364, 295, 3164, 293, 437, 286, 643, 490, 309, 307, 544, 370, 411,
  45590, 11879, 558, 411, 286, 2978, 281, 50660], "temperature": 0.0, "avg_logprob":
  -0.1324155807495117, "compression_ratio": 1.6986899563318778, "no_speech_prob":
  0.002491435268893838}, {"id": 180, "seek": 108302, "start": 1089.98, "end": 1096.46,
  "text": " go into like uh Leo Boystov''s publications and parse it out for me and
  help me understand what he''s", "tokens": [50712, 352, 666, 411, 2232, 19344, 9486,
  372, 5179, 311, 25618, 293, 48377, 309, 484, 337, 385, 293, 854, 385, 1223, 437,
  415, 311, 51036], "temperature": 0.0, "avg_logprob": -0.1324155807495117, "compression_ratio":
  1.6986899563318778, "no_speech_prob": 0.002491435268893838}, {"id": 181, "seek":
  108302, "start": 1096.46, "end": 1104.46, "text": " done so it''s like the specific
  information and then yeah the real I mean u.com also has a really", "tokens": [51036,
  1096, 370, 309, 311, 411, 264, 2685, 1589, 293, 550, 1338, 264, 957, 286, 914, 344,
  13, 1112, 611, 575, 257, 534, 51436], "temperature": 0.0, "avg_logprob": -0.1324155807495117,
  "compression_ratio": 1.6986899563318778, "no_speech_prob": 0.002491435268893838},
  {"id": 182, "seek": 108302, "start": 1104.46, "end": 1109.98, "text": " brilliant
  thing where it''s uh search engine on this panel and then the chat GBC on this side
  so", "tokens": [51436, 10248, 551, 689, 309, 311, 2232, 3164, 2848, 322, 341, 4831,
  293, 550, 264, 5081, 460, 7869, 322, 341, 1252, 370, 51712], "temperature": 0.0,
  "avg_logprob": -0.1324155807495117, "compression_ratio": 1.6986899563318778, "no_speech_prob":
  0.002491435268893838}, {"id": 183, "seek": 110998, "start": 1109.98, "end": 1115.74,
  "text": " it''s like a user interface problem I think yeah yeah but but I mean maybe
  even yeah I totally", "tokens": [50364, 309, 311, 411, 257, 4195, 9226, 1154, 286,
  519, 1338, 1338, 457, 457, 286, 914, 1310, 754, 1338, 286, 3879, 50652], "temperature":
  0.0, "avg_logprob": -0.10471352378090659, "compression_ratio": 1.8309859154929577,
  "no_speech_prob": 0.0036140696611255407}, {"id": 184, "seek": 110998, "start": 1115.74,
  "end": 1122.14, "text": " agree with you that user interface definitely creates
  the bias uh how we like how you use traffic", "tokens": [50652, 3986, 365, 291,
  300, 4195, 9226, 2138, 7829, 264, 12577, 2232, 577, 321, 411, 577, 291, 764, 6419,
  50972], "temperature": 0.0, "avg_logprob": -0.10471352378090659, "compression_ratio":
  1.8309859154929577, "no_speech_prob": 0.0036140696611255407}, {"id": 185, "seek":
  110998, "start": 1122.14, "end": 1128.14, "text": " lights today they go like red
  you know yellow and green they don''t go upside down right and like", "tokens":
  [50972, 5811, 965, 436, 352, 411, 2182, 291, 458, 5566, 293, 3092, 436, 500, 380,
  352, 14119, 760, 558, 293, 411, 51272], "temperature": 0.0, "avg_logprob": -0.10471352378090659,
  "compression_ratio": 1.8309859154929577, "no_speech_prob": 0.0036140696611255407},
  {"id": 186, "seek": 110998, "start": 1128.14, "end": 1133.18, "text": " if you see
  an upside down you will you will think well this is a wrong uh traffic light uh
  I''d rather", "tokens": [51272, 498, 291, 536, 364, 14119, 760, 291, 486, 291, 486,
  519, 731, 341, 307, 257, 2085, 2232, 6419, 1442, 2232, 286, 1116, 2831, 51524],
  "temperature": 0.0, "avg_logprob": -0.10471352378090659, "compression_ratio": 1.8309859154929577,
  "no_speech_prob": 0.0036140696611255407}, {"id": 187, "seek": 113318, "start": 1133.26,
  "end": 1140.46, "text": " not cross here you know but like it''s kind of like similar
  here like with the search engines we are", "tokens": [50368, 406, 3278, 510, 291,
  458, 457, 411, 309, 311, 733, 295, 411, 2531, 510, 411, 365, 264, 3164, 12982, 321,
  366, 50728], "temperature": 0.0, "avg_logprob": -0.14627052635274906, "compression_ratio":
  1.7035398230088497, "no_speech_prob": 0.003619111143052578}, {"id": 188, "seek":
  113318, "start": 1140.46, "end": 1146.78, "text": " used to seeing you know URLs
  and and being able to click there but of course if you take Google or", "tokens":
  [50728, 1143, 281, 2577, 291, 458, 43267, 293, 293, 885, 1075, 281, 2052, 456, 457,
  295, 1164, 498, 291, 747, 3329, 420, 51044], "temperature": 0.0, "avg_logprob":
  -0.14627052635274906, "compression_ratio": 1.7035398230088497, "no_speech_prob":
  0.003619111143052578}, {"id": 189, "seek": 113318, "start": 1146.78, "end": 1151.66,
  "text": " I guess being does that too they also pre-generate this answers answer
  boxes right so you can", "tokens": [51044, 286, 2041, 885, 775, 300, 886, 436, 611,
  659, 12, 21848, 473, 341, 6338, 1867, 9002, 558, 370, 291, 393, 51288], "temperature":
  0.0, "avg_logprob": -0.14627052635274906, "compression_ratio": 1.7035398230088497,
  "no_speech_prob": 0.003619111143052578}, {"id": 190, "seek": 113318, "start": 1151.66,
  "end": 1157.18, "text": " answer you can click there but I don''t think you have
  a URL to verify you know the source of", "tokens": [51288, 1867, 291, 393, 2052,
  456, 457, 286, 500, 380, 519, 291, 362, 257, 12905, 281, 16888, 291, 458, 264, 4009,
  295, 51564], "temperature": 0.0, "avg_logprob": -0.14627052635274906, "compression_ratio":
  1.7035398230088497, "no_speech_prob": 0.003619111143052578}, {"id": 191, "seek":
  115718, "start": 1157.26, "end": 1163.3400000000001, "text": " this information
  if I''m not wrong yeah yeah so they already playing with incorporating this", "tokens":
  [50368, 341, 1589, 498, 286, 478, 406, 2085, 1338, 1338, 370, 436, 1217, 2433, 365,
  33613, 341, 50672], "temperature": 0.0, "avg_logprob": -0.10445472429383476, "compression_ratio":
  1.758364312267658, "no_speech_prob": 0.004276286344975233}, {"id": 192, "seek":
  115718, "start": 1163.3400000000001, "end": 1168.8600000000001, "text": " knowledge
  from a language model right and they they they look at you and of course they also
  want you", "tokens": [50672, 3601, 490, 257, 2856, 2316, 558, 293, 436, 436, 436,
  574, 412, 291, 293, 295, 1164, 436, 611, 528, 291, 50948], "temperature": 0.0, "avg_logprob":
  -0.10445472429383476, "compression_ratio": 1.758364312267658, "no_speech_prob":
  0.004276286344975233}, {"id": 193, "seek": 115718, "start": 1168.8600000000001,
  "end": 1173.1000000000001, "text": " to spend more time on their page which is probably
  not good but we''ll not discuss that", "tokens": [50948, 281, 3496, 544, 565, 322,
  641, 3028, 597, 307, 1391, 406, 665, 457, 321, 603, 406, 2248, 300, 51160], "temperature":
  0.0, "avg_logprob": -0.10445472429383476, "compression_ratio": 1.758364312267658,
  "no_speech_prob": 0.004276286344975233}, {"id": 194, "seek": 115718, "start": 1174.78,
  "end": 1179.74, "text": " so they don''t share the traffic further but but the thing
  is you know they still play with the", "tokens": [51244, 370, 436, 500, 380, 2073,
  264, 6419, 3052, 457, 457, 264, 551, 307, 291, 458, 436, 920, 862, 365, 264, 51492],
  "temperature": 0.0, "avg_logprob": -0.10445472429383476, "compression_ratio": 1.758364312267658,
  "no_speech_prob": 0.004276286344975233}, {"id": 195, "seek": 115718, "start": 1179.74,
  "end": 1186.38, "text": " idea okay what if we try to answer not just with the URL
  and summary but actually with the actual", "tokens": [51492, 1558, 1392, 437, 498,
  321, 853, 281, 1867, 406, 445, 365, 264, 12905, 293, 12691, 457, 767, 365, 264,
  3539, 51824], "temperature": 0.0, "avg_logprob": -0.10445472429383476, "compression_ratio":
  1.758364312267658, "no_speech_prob": 0.004276286344975233}, {"id": 196, "seek":
  118638, "start": 1186.38, "end": 1193.5, "text": " thing right with the actual answer
  oh so that comes into like the extractive versus abstractive", "tokens": [50364,
  551, 558, 365, 264, 3539, 1867, 1954, 370, 300, 1487, 666, 411, 264, 8947, 488,
  5717, 12649, 488, 50720], "temperature": 0.0, "avg_logprob": -0.12067663322374658,
  "compression_ratio": 1.821011673151751, "no_speech_prob": 0.0007553909672424197},
  {"id": 197, "seek": 118638, "start": 1193.5, "end": 1198.46, "text": " and like
  whether you want the question answering models that classify the answers in the
  context", "tokens": [50720, 293, 411, 1968, 291, 528, 264, 1168, 13430, 5245, 300,
  33872, 264, 6338, 294, 264, 4319, 50968], "temperature": 0.0, "avg_logprob": -0.12067663322374658,
  "compression_ratio": 1.821011673151751, "no_speech_prob": 0.0007553909672424197},
  {"id": 198, "seek": 118638, "start": 1199.42, "end": 1203.8200000000002, "text":
  " yeah and yeah I think that still has a place for sure I mean it''s super lightweight
  as I mentioned", "tokens": [51016, 1338, 293, 1338, 286, 519, 300, 920, 575, 257,
  1081, 337, 988, 286, 914, 309, 311, 1687, 22052, 382, 286, 2835, 51236], "temperature":
  0.0, "avg_logprob": -0.12067663322374658, "compression_ratio": 1.821011673151751,
  "no_speech_prob": 0.0007553909672424197}, {"id": 199, "seek": 118638, "start": 1203.8200000000002,
  "end": 1209.3400000000001, "text": " Neural Magic they just did a sparse question
  answering model that can run on CPU super fast and", "tokens": [51236, 1734, 1807,
  16154, 436, 445, 630, 257, 637, 11668, 1168, 13430, 2316, 300, 393, 1190, 322, 13199,
  1687, 2370, 293, 51512], "temperature": 0.0, "avg_logprob": -0.12067663322374658,
  "compression_ratio": 1.821011673151751, "no_speech_prob": 0.0007553909672424197},
  {"id": 200, "seek": 118638, "start": 1209.8200000000002, "end": 1214.7, "text":
  " yeah I think that approach is also just gonna be more cost effective for a while",
  "tokens": [51536, 1338, 286, 519, 300, 3109, 307, 611, 445, 799, 312, 544, 2063,
  4942, 337, 257, 1339, 51780], "temperature": 0.0, "avg_logprob": -0.12067663322374658,
  "compression_ratio": 1.821011673151751, "no_speech_prob": 0.0007553909672424197},
  {"id": 201, "seek": 121470, "start": 1215.02, "end": 1222.3, "text": " yeah exactly
  but you mentioned BM25 and I''m curious like I''ve been trying to approach this
  hybrid", "tokens": [50380, 1338, 2293, 457, 291, 2835, 15901, 6074, 293, 286, 478,
  6369, 411, 286, 600, 668, 1382, 281, 3109, 341, 13051, 50744], "temperature": 0.0,
  "avg_logprob": -0.14191165500217015, "compression_ratio": 1.6724890829694323, "no_speech_prob":
  0.003626579651609063}, {"id": 202, "seek": 121470, "start": 1222.3, "end": 1228.38,
  "text": " search topic but I think you went ahead all right so and I was just wondering
  like what''s your", "tokens": [50744, 3164, 4829, 457, 286, 519, 291, 1437, 2286,
  439, 558, 370, 293, 286, 390, 445, 6359, 411, 437, 311, 428, 51048], "temperature":
  0.0, "avg_logprob": -0.14191165500217015, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.003626579651609063}, {"id": 203, "seek": 121470, "start": 1228.38,
  "end": 1235.98, "text": " take on this topic like can you a little like intro it
  to our listeners but also why do you think", "tokens": [51048, 747, 322, 341, 4829,
  411, 393, 291, 257, 707, 411, 12897, 309, 281, 527, 23274, 457, 611, 983, 360, 291,
  519, 51428], "temperature": 0.0, "avg_logprob": -0.14191165500217015, "compression_ratio":
  1.6724890829694323, "no_speech_prob": 0.003626579651609063}, {"id": 204, "seek":
  121470, "start": 1235.98, "end": 1241.82, "text": " it''s a good idea to to build
  like a hybrid search you know combining keyboard retrieval with", "tokens": [51428,
  309, 311, 257, 665, 1558, 281, 281, 1322, 411, 257, 13051, 3164, 291, 458, 21928,
  10186, 19817, 3337, 365, 51720], "temperature": 0.0, "avg_logprob": -0.14191165500217015,
  "compression_ratio": 1.6724890829694323, "no_speech_prob": 0.003626579651609063},
  {"id": 205, "seek": 124182, "start": 1241.82, "end": 1248.7, "text": " it''s with
  a you know dense retrieval yeah awesome I started by saying this has just been like
  the", "tokens": [50364, 309, 311, 365, 257, 291, 458, 18011, 19817, 3337, 1338,
  3476, 286, 1409, 538, 1566, 341, 575, 445, 668, 411, 264, 50708], "temperature":
  0.0, "avg_logprob": -0.1660457926058988, "compression_ratio": 1.7062937062937062,
  "no_speech_prob": 0.0014643922913819551}, {"id": 206, "seek": 124182, "start": 1248.7,
  "end": 1253.34, "text": " most satisfying project I''ve worked on since I''ve joined
  Wevegate and just being a part of this team", "tokens": [50708, 881, 18348, 1716,
  286, 600, 2732, 322, 1670, 286, 600, 6869, 492, 303, 22514, 293, 445, 885, 257,
  644, 295, 341, 1469, 50940], "temperature": 0.0, "avg_logprob": -0.1660457926058988,
  "compression_ratio": 1.7062937062937062, "no_speech_prob": 0.0014643922913819551},
  {"id": 207, "seek": 124182, "start": 1253.34, "end": 1258.1399999999999, "text":
  " and it''s been you know like a big team working on hybrid search and it''s just
  been an incredible", "tokens": [50940, 293, 309, 311, 668, 291, 458, 411, 257, 955,
  1469, 1364, 322, 13051, 3164, 293, 309, 311, 445, 668, 364, 4651, 51180], "temperature":
  0.0, "avg_logprob": -0.1660457926058988, "compression_ratio": 1.7062937062937062,
  "no_speech_prob": 0.0014643922913819551}, {"id": 208, "seek": 124182, "start": 1258.1399999999999,
  "end": 1264.06, "text": " experience so I guess starting yeah the motivation is
  BM25 has this it builds on term frequency", "tokens": [51180, 1752, 370, 286, 2041,
  2891, 1338, 264, 12335, 307, 15901, 6074, 575, 341, 309, 15182, 322, 1433, 7893,
  51476], "temperature": 0.0, "avg_logprob": -0.1660457926058988, "compression_ratio":
  1.7062937062937062, "no_speech_prob": 0.0014643922913819551}, {"id": 209, "seek":
  124182, "start": 1264.06, "end": 1268.7, "text": " inverse document frequency by
  adding like this binary independence model and the IDF calculation", "tokens": [51476,
  17340, 4166, 7893, 538, 5127, 411, 341, 17434, 14640, 2316, 293, 264, 7348, 37,
  17108, 51708], "temperature": 0.0, "avg_logprob": -0.1660457926058988, "compression_ratio":
  1.7062937062937062, "no_speech_prob": 0.0014643922913819551}, {"id": 210, "seek":
  126870, "start": 1268.7, "end": 1272.78, "text": " and then you also normalize it
  for the length of the document that''s just like these subtle", "tokens": [50364,
  293, 550, 291, 611, 2710, 1125, 309, 337, 264, 4641, 295, 264, 4166, 300, 311, 445,
  411, 613, 13743, 50568], "temperature": 0.0, "avg_logprob": -0.12430707478927354,
  "compression_ratio": 1.7933579335793357, "no_speech_prob": 0.0008278696914203465},
  {"id": 211, "seek": 126870, "start": 1272.78, "end": 1277.26, "text": " differences
  that make it different than TF IDF but you could also use TF IDF in hybrid search
  if", "tokens": [50568, 7300, 300, 652, 309, 819, 813, 40964, 7348, 37, 457, 291,
  727, 611, 764, 40964, 7348, 37, 294, 13051, 3164, 498, 50792], "temperature": 0.0,
  "avg_logprob": -0.12430707478927354, "compression_ratio": 1.7933579335793357, "no_speech_prob":
  0.0008278696914203465}, {"id": 212, "seek": 126870, "start": 1277.26, "end": 1282.06,
  "text": " that''s what you were after and so then you also have the vector search
  and then you have this rank", "tokens": [50792, 300, 311, 437, 291, 645, 934, 293,
  370, 550, 291, 611, 362, 264, 8062, 3164, 293, 550, 291, 362, 341, 6181, 51032],
  "temperature": 0.0, "avg_logprob": -0.12430707478927354, "compression_ratio": 1.7933579335793357,
  "no_speech_prob": 0.0008278696914203465}, {"id": 213, "seek": 126870, "start": 1282.06,
  "end": 1287.02, "text": " fusion so so we look we found this paper where they have
  seven different strategies for rank fusion", "tokens": [51032, 23100, 370, 370,
  321, 574, 321, 1352, 341, 3035, 689, 436, 362, 3407, 819, 9029, 337, 6181, 23100,
  51280], "temperature": 0.0, "avg_logprob": -0.12430707478927354, "compression_ratio":
  1.7933579335793357, "no_speech_prob": 0.0008278696914203465}, {"id": 214, "seek":
  126870, "start": 1287.02, "end": 1294.14, "text": " it''s like rrf board uh I don''t
  know come some but in the end we just went with rrf reciprocal rank", "tokens":
  [51280, 309, 311, 411, 367, 81, 69, 3150, 2232, 286, 500, 380, 458, 808, 512, 457,
  294, 264, 917, 321, 445, 1437, 365, 367, 81, 69, 46948, 6181, 51636], "temperature":
  0.0, "avg_logprob": -0.12430707478927354, "compression_ratio": 1.7933579335793357,
  "no_speech_prob": 0.0008278696914203465}, {"id": 215, "seek": 129414, "start": 1294.14,
  "end": 1299.0200000000002, "text": " fusion which is just erica''s recently published
  a blog post that shows the equation and just", "tokens": [50364, 23100, 597, 307,
  445, 1189, 2262, 311, 3938, 6572, 257, 6968, 2183, 300, 3110, 264, 5367, 293, 445,
  50608], "temperature": 0.0, "avg_logprob": -0.09832319223655844, "compression_ratio":
  1.7168458781362008, "no_speech_prob": 0.008709307760000229}, {"id": 216, "seek":
  129414, "start": 1299.0200000000002, "end": 1303.74, "text": " tells some of our
  thinking around it but it''s where you just combine the ranks compared to say",
  "tokens": [50608, 5112, 512, 295, 527, 1953, 926, 309, 457, 309, 311, 689, 291,
  445, 10432, 264, 21406, 5347, 281, 584, 50844], "temperature": 0.0, "avg_logprob":
  -0.09832319223655844, "compression_ratio": 1.7168458781362008, "no_speech_prob":
  0.008709307760000229}, {"id": 217, "seek": 129414, "start": 1303.74, "end": 1308.14,
  "text": " combining the scores because you know BM25 has a score particularly and
  vector search has like a", "tokens": [50844, 21928, 264, 13444, 570, 291, 458, 15901,
  6074, 575, 257, 6175, 4098, 293, 8062, 3164, 575, 411, 257, 51064], "temperature":
  0.0, "avg_logprob": -0.09832319223655844, "compression_ratio": 1.7168458781362008,
  "no_speech_prob": 0.008709307760000229}, {"id": 218, "seek": 129414, "start": 1308.14,
  "end": 1313.5800000000002, "text": " distance at return so you might look at some
  way of like linearly or non-linearly combining those", "tokens": [51064, 4560, 412,
  2736, 370, 291, 1062, 574, 412, 512, 636, 295, 411, 43586, 420, 2107, 12, 28263,
  356, 21928, 729, 51336], "temperature": 0.0, "avg_logprob": -0.09832319223655844,
  "compression_ratio": 1.7168458781362008, "no_speech_prob": 0.008709307760000229},
  {"id": 219, "seek": 129414, "start": 1313.5800000000002, "end": 1319.5800000000002,
  "text": " scores and I''ve done some experiments with with kind of my thinking around
  it was like okay what", "tokens": [51336, 13444, 293, 286, 600, 1096, 512, 12050,
  365, 365, 733, 295, 452, 1953, 926, 309, 390, 411, 1392, 437, 51636], "temperature":
  0.0, "avg_logprob": -0.09832319223655844, "compression_ratio": 1.7168458781362008,
  "no_speech_prob": 0.008709307760000229}, {"id": 220, "seek": 131958, "start": 1319.58,
  "end": 1325.34, "text": " would be like an optimal alpha per query would that be
  you know maybe like a conditional model like", "tokens": [50364, 576, 312, 411,
  364, 16252, 8961, 680, 14581, 576, 300, 312, 291, 458, 1310, 411, 257, 27708, 2316,
  411, 50652], "temperature": 0.0, "avg_logprob": -0.09418844772597491, "compression_ratio":
  1.7711267605633803, "no_speech_prob": 0.0009331719484180212}, {"id": 221, "seek":
  131958, "start": 1325.34, "end": 1330.62, "text": " so I tried this with the few
  shot learning of gbt3 where you you run a few examples of the optimal alpha", "tokens":
  [50652, 370, 286, 3031, 341, 365, 264, 1326, 3347, 2539, 295, 290, 4517, 18, 689,
  291, 291, 1190, 257, 1326, 5110, 295, 264, 16252, 8961, 50916], "temperature": 0.0,
  "avg_logprob": -0.09418844772597491, "compression_ratio": 1.7711267605633803, "no_speech_prob":
  0.0009331719484180212}, {"id": 222, "seek": 131958, "start": 1330.62, "end": 1335.58,
  "text": " and then you try to see uh you know how would you like to wait BM25 and
  dense vector search given", "tokens": [50916, 293, 550, 291, 853, 281, 536, 2232,
  291, 458, 577, 576, 291, 411, 281, 1699, 15901, 6074, 293, 18011, 8062, 3164, 2212,
  51164], "temperature": 0.0, "avg_logprob": -0.09418844772597491, "compression_ratio":
  1.7711267605633803, "no_speech_prob": 0.0009331719484180212}, {"id": 223, "seek":
  131958, "start": 1335.58, "end": 1340.3799999999999, "text": " this query and see
  if that is productive but I found and this is a very interesting thing because I",
  "tokens": [51164, 341, 14581, 293, 536, 498, 300, 307, 13304, 457, 286, 1352, 293,
  341, 307, 257, 588, 1880, 551, 570, 286, 51404], "temperature": 0.0, "avg_logprob":
  -0.09418844772597491, "compression_ratio": 1.7711267605633803, "no_speech_prob":
  0.0009331719484180212}, {"id": 224, "seek": 131958, "start": 1340.3799999999999,
  "end": 1345.8999999999999, "text": " think people have this idea that BM25 is like
  very interpretable but in my experience it hasn''t been", "tokens": [51404, 519,
  561, 362, 341, 1558, 300, 15901, 6074, 307, 411, 588, 7302, 712, 457, 294, 452,
  1752, 309, 6132, 380, 668, 51680], "temperature": 0.0, "avg_logprob": -0.09418844772597491,
  "compression_ratio": 1.7711267605633803, "no_speech_prob": 0.0009331719484180212},
  {"id": 225, "seek": 134590, "start": 1345.9, "end": 1351.3400000000001, "text":
  " that I when you do when you''re doing longish queries in long documents and maybe
  we can talk about", "tokens": [50364, 300, 286, 562, 291, 360, 562, 291, 434, 884,
  938, 742, 24109, 294, 938, 8512, 293, 1310, 321, 393, 751, 466, 50636], "temperature":
  0.0, "avg_logprob": -0.12145776748657226, "compression_ratio": 1.7545126353790614,
  "no_speech_prob": 0.00052179693011567}, {"id": 226, "seek": 134590, "start": 1351.3400000000001,
  "end": 1358.7, "text": " long queries or short queries but I find that trying to
  decode why it why BM25 was better than dense", "tokens": [50636, 938, 24109, 420,
  2099, 24109, 457, 286, 915, 300, 1382, 281, 979, 1429, 983, 309, 983, 15901, 6074,
  390, 1101, 813, 18011, 51004], "temperature": 0.0, "avg_logprob": -0.12145776748657226,
  "compression_ratio": 1.7545126353790614, "no_speech_prob": 0.00052179693011567},
  {"id": 227, "seek": 134590, "start": 1358.7, "end": 1363.3400000000001, "text":
  " search for some particular query I find that to be impossible and maybe someone
  will prove", "tokens": [51004, 3164, 337, 512, 1729, 14581, 286, 915, 300, 281,
  312, 6243, 293, 1310, 1580, 486, 7081, 51236], "temperature": 0.0, "avg_logprob":
  -0.12145776748657226, "compression_ratio": 1.7545126353790614, "no_speech_prob":
  0.00052179693011567}, {"id": 228, "seek": 134590, "start": 1363.3400000000001, "end":
  1368.46, "text": " it wrong and I''ll look forward to seeing that honestly but like
  there''s this example that we have", "tokens": [51236, 309, 2085, 293, 286, 603,
  574, 2128, 281, 2577, 300, 6095, 457, 411, 456, 311, 341, 1365, 300, 321, 362, 51492],
  "temperature": 0.0, "avg_logprob": -0.12145776748657226, "compression_ratio": 1.7545126353790614,
  "no_speech_prob": 0.00052179693011567}, {"id": 229, "seek": 134590, "start": 1368.46,
  "end": 1372.5400000000002, "text": " as you know erica was developing the weviate
  error demonstration of hybrid search where the query", "tokens": [51492, 382, 291,
  458, 1189, 2262, 390, 6416, 264, 321, 4917, 473, 6713, 16520, 295, 13051, 3164,
  689, 264, 14581, 51696], "temperature": 0.0, "avg_logprob": -0.12145776748657226,
  "compression_ratio": 1.7545126353790614, "no_speech_prob": 0.00052179693011567},
  {"id": 230, "seek": 137254, "start": 1372.94, "end": 1377.58, "text": " how to catch
  an elaskin Pollock and the idea being that the dense vector search contributes",
  "tokens": [50384, 577, 281, 3745, 364, 806, 3863, 259, 31304, 1560, 293, 264, 1558,
  885, 300, 264, 18011, 8062, 3164, 32035, 50616], "temperature": 0.0, "avg_logprob":
  -0.17256110055106028, "compression_ratio": 1.7202797202797202, "no_speech_prob":
  0.003874595509842038}, {"id": 231, "seek": 137254, "start": 1377.58, "end": 1383.26,
  "text": " the disambiguation of catch that it prefers to fishing and that BM25 is
  specific to elaskin Pollock", "tokens": [50616, 264, 717, 2173, 328, 16073, 295,
  3745, 300, 309, 44334, 281, 10180, 293, 300, 15901, 6074, 307, 2685, 281, 806, 3863,
  259, 31304, 1560, 50900], "temperature": 0.0, "avg_logprob": -0.17256110055106028,
  "compression_ratio": 1.7202797202797202, "no_speech_prob": 0.003874595509842038},
  {"id": 232, "seek": 137254, "start": 1383.98, "end": 1388.3799999999999, "text":
  " but I haven''t been able to just like inspect that kind of behavior as I look
  through the beer benchmarks", "tokens": [50936, 457, 286, 2378, 380, 668, 1075,
  281, 445, 411, 15018, 300, 733, 295, 5223, 382, 286, 574, 807, 264, 8795, 43751,
  51156], "temperature": 0.0, "avg_logprob": -0.17256110055106028, "compression_ratio":
  1.7202797202797202, "no_speech_prob": 0.003874595509842038}, {"id": 233, "seek":
  137254, "start": 1388.3799999999999, "end": 1393.58, "text": " that just I''m super
  excited to talk about that and how we''ve been evaluating it but you know let",
  "tokens": [51156, 300, 445, 286, 478, 1687, 2919, 281, 751, 466, 300, 293, 577,
  321, 600, 668, 27479, 309, 457, 291, 458, 718, 51416], "temperature": 0.0, "avg_logprob":
  -0.17256110055106028, "compression_ratio": 1.7202797202797202, "no_speech_prob":
  0.003874595509842038}, {"id": 234, "seek": 137254, "start": 1393.58, "end": 1398.46,
  "text": " me let me pass it back to you and ask about your experience with them
  BM25 or like the keyword and", "tokens": [51416, 385, 718, 385, 1320, 309, 646,
  281, 291, 293, 1029, 466, 428, 1752, 365, 552, 15901, 6074, 420, 411, 264, 20428,
  293, 51660], "temperature": 0.0, "avg_logprob": -0.17256110055106028, "compression_ratio":
  1.7202797202797202, "no_speech_prob": 0.003874595509842038}, {"id": 235, "seek":
  139846, "start": 1398.46, "end": 1401.98, "text": " the dense search particularly
  because then I''d like to kind of take the topic to just", "tokens": [50364, 264,
  18011, 3164, 4098, 570, 550, 286, 1116, 411, 281, 733, 295, 747, 264, 4829, 281,
  445, 50540], "temperature": 0.0, "avg_logprob": -0.19791771116710843, "compression_ratio":
  1.5478260869565217, "no_speech_prob": 0.0031987582333385944}, {"id": 236, "seek":
  139846, "start": 1401.98, "end": 1407.82, "text": " arbitrary combinations of retrieval
  methods not just be in 25 and say DPR or whatever", "tokens": [50540, 23211, 21267,
  295, 19817, 3337, 7150, 406, 445, 312, 294, 3552, 293, 584, 413, 15958, 420, 2035,
  50832], "temperature": 0.0, "avg_logprob": -0.19791771116710843, "compression_ratio":
  1.5478260869565217, "no_speech_prob": 0.0031987582333385944}, {"id": 237, "seek":
  139846, "start": 1408.3, "end": 1414.14, "text": " yeah I think I remember even
  before the dense search appeared on the scene we were", "tokens": [50856, 1338,
  286, 519, 286, 1604, 754, 949, 264, 18011, 3164, 8516, 322, 264, 4145, 321, 645,
  51148], "temperature": 0.0, "avg_logprob": -0.19791771116710843, "compression_ratio":
  1.5478260869565217, "no_speech_prob": 0.0031987582333385944}, {"id": 238, "seek":
  139846, "start": 1414.94, "end": 1423.1000000000001, "text": " experimenting with
  sort of like making TFI DF which is BM25 is like an addon like BM25 I think stands",
  "tokens": [51188, 29070, 365, 1333, 295, 411, 1455, 314, 38568, 48336, 597, 307,
  15901, 6074, 307, 411, 364, 909, 266, 411, 15901, 6074, 286, 519, 7382, 51596],
  "temperature": 0.0, "avg_logprob": -0.19791771116710843, "compression_ratio": 1.5478260869565217,
  "no_speech_prob": 0.0031987582333385944}, {"id": 239, "seek": 142310, "start": 1423.1,
  "end": 1435.1, "text": " for best match so period so solved problem solved but you
  know like one of the questions the", "tokens": [50364, 337, 1151, 2995, 370, 2896,
  370, 13041, 1154, 13041, 457, 291, 458, 411, 472, 295, 264, 1651, 264, 50964], "temperature":
  0.0, "avg_logprob": -0.152951251628787, "compression_ratio": 1.8235294117647058,
  "no_speech_prob": 0.0009885996114462614}, {"id": 240, "seek": 142310, "start": 1435.1,
  "end": 1439.6599999999999, "text": " the reason I love working with product managers
  and at the moment I am a product manager so I", "tokens": [50964, 264, 1778, 286,
  959, 1364, 365, 1674, 14084, 293, 412, 264, 1623, 286, 669, 257, 1674, 6598, 370,
  286, 51192], "temperature": 0.0, "avg_logprob": -0.152951251628787, "compression_ratio":
  1.8235294117647058, "no_speech_prob": 0.0009885996114462614}, {"id": 241, "seek":
  142310, "start": 1439.6599999999999, "end": 1443.98, "text": " took the other side
  of this thing maybe we can talk more about it in the VV8 podcast but", "tokens":
  [51192, 1890, 264, 661, 1252, 295, 341, 551, 1310, 321, 393, 751, 544, 466, 309,
  294, 264, 691, 53, 23, 7367, 457, 51408], "temperature": 0.0, "avg_logprob": -0.152951251628787,
  "compression_ratio": 1.8235294117647058, "no_speech_prob": 0.0009885996114462614},
  {"id": 242, "seek": 142310, "start": 1444.78, "end": 1449.1799999999998, "text":
  " you know the reason I love talking to product managers is because they don''t
  know anything maybe", "tokens": [51448, 291, 458, 264, 1778, 286, 959, 1417, 281,
  1674, 14084, 307, 570, 436, 500, 380, 458, 1340, 1310, 51668], "temperature": 0.0,
  "avg_logprob": -0.152951251628787, "compression_ratio": 1.8235294117647058, "no_speech_prob":
  0.0009885996114462614}, {"id": 243, "seek": 144918, "start": 1449.18, "end": 1455.74,
  "text": " they don''t know that much about algorithms as you and they don''t code
  maybe as much as you", "tokens": [50364, 436, 500, 380, 458, 300, 709, 466, 14642,
  382, 291, 293, 436, 500, 380, 3089, 1310, 382, 709, 382, 291, 50692], "temperature":
  0.0, "avg_logprob": -0.09844538929698231, "compression_ratio": 1.7488372093023257,
  "no_speech_prob": 0.008044441230595112}, {"id": 244, "seek": 144918, "start": 1456.3,
  "end": 1462.8600000000001, "text": " but they do care for they are the stakeholders
  of the end result right so when they go out talk", "tokens": [50720, 457, 436, 360,
  1127, 337, 436, 366, 264, 17779, 295, 264, 917, 1874, 558, 370, 562, 436, 352, 484,
  751, 51048], "temperature": 0.0, "avg_logprob": -0.09844538929698231, "compression_ratio":
  1.7488372093023257, "no_speech_prob": 0.008044441230595112}, {"id": 245, "seek":
  144918, "start": 1462.8600000000001, "end": 1468.78, "text": " to sales or to the
  end users they will not get a question which alpha you have used now coming", "tokens":
  [51048, 281, 5763, 420, 281, 264, 917, 5022, 436, 486, 406, 483, 257, 1168, 597,
  8961, 291, 362, 1143, 586, 1348, 51344], "temperature": 0.0, "avg_logprob": -0.09844538929698231,
  "compression_ratio": 1.7488372093023257, "no_speech_prob": 0.008044441230595112},
  {"id": 246, "seek": 144918, "start": 1468.78, "end": 1476.7, "text": " back to your
  to your example right they will say hey I typed cat three times in my query and
  I", "tokens": [51344, 646, 281, 428, 281, 428, 1365, 558, 436, 486, 584, 4177, 286,
  33941, 3857, 1045, 1413, 294, 452, 14581, 293, 286, 51740], "temperature": 0.0,
  "avg_logprob": -0.09844538929698231, "compression_ratio": 1.7488372093023257, "no_speech_prob":
  0.008044441230595112}, {"id": 247, "seek": 147670, "start": 1476.7, "end": 1481.5,
  "text": " still see that the document that mentions it once is at the top how can
  you explain this", "tokens": [50364, 920, 536, 300, 264, 4166, 300, 23844, 309,
  1564, 307, 412, 264, 1192, 577, 393, 291, 2903, 341, 50604], "temperature": 0.0,
  "avg_logprob": -0.16222241867420284, "compression_ratio": 1.6592920353982301, "no_speech_prob":
  0.006021835841238499}, {"id": 248, "seek": 147670, "start": 1482.8600000000001,
  "end": 1488.7, "text": " I will try to link there is a consulting company I think
  they''re based in Boston actually by the way", "tokens": [50672, 286, 486, 853,
  281, 2113, 456, 307, 257, 23682, 2237, 286, 519, 436, 434, 2361, 294, 12333, 767,
  538, 264, 636, 50964], "temperature": 0.0, "avg_logprob": -0.16222241867420284,
  "compression_ratio": 1.6592920353982301, "no_speech_prob": 0.006021835841238499},
  {"id": 249, "seek": 147670, "start": 1489.5800000000002, "end": 1496.8600000000001,
  "text": " I just forget their name key and via something so they have a really great
  presentation on", "tokens": [51008, 286, 445, 2870, 641, 1315, 2141, 293, 5766,
  746, 370, 436, 362, 257, 534, 869, 5860, 322, 51372], "temperature": 0.0, "avg_logprob":
  -0.16222241867420284, "compression_ratio": 1.6592920353982301, "no_speech_prob":
  0.006021835841238499}, {"id": 250, "seek": 147670, "start": 1496.8600000000001,
  "end": 1504.22, "text": " haystack life I believe where they go super deep and I
  recommend you watch it super super deep", "tokens": [51372, 4842, 372, 501, 993,
  286, 1697, 689, 436, 352, 1687, 2452, 293, 286, 2748, 291, 1159, 309, 1687, 1687,
  2452, 51740], "temperature": 0.0, "avg_logprob": -0.16222241867420284, "compression_ratio":
  1.6592920353982301, "no_speech_prob": 0.006021835841238499}, {"id": 251, "seek":
  150422, "start": 1504.22, "end": 1510.78, "text": " on how TF IDF screws up our
  understanding of how things should work what they don''t you know", "tokens": [50364,
  322, 577, 40964, 7348, 37, 13050, 493, 527, 3701, 295, 577, 721, 820, 589, 437,
  436, 500, 380, 291, 458, 50692], "temperature": 0.0, "avg_logprob": -0.110720269033842,
  "compression_ratio": 1.8492063492063493, "no_speech_prob": 0.0060023353435099125},
  {"id": 252, "seek": 150422, "start": 1510.78, "end": 1516.8600000000001, "text":
  " and they go by you know how many times you know the word cat is mentioned in the
  document versus", "tokens": [50692, 293, 436, 352, 538, 291, 458, 577, 867, 1413,
  291, 458, 264, 1349, 3857, 307, 2835, 294, 264, 4166, 5717, 50996], "temperature":
  0.0, "avg_logprob": -0.110720269033842, "compression_ratio": 1.8492063492063493,
  "no_speech_prob": 0.0060023353435099125}, {"id": 253, "seek": 150422, "start": 1516.8600000000001,
  "end": 1521.1000000000001, "text": " how many times it''s it''s mentioned in the
  query and you can do all this combinatorial you know", "tokens": [50996, 577, 867,
  1413, 309, 311, 309, 311, 2835, 294, 264, 14581, 293, 291, 393, 360, 439, 341, 2512,
  31927, 831, 291, 458, 51208], "temperature": 0.0, "avg_logprob": -0.110720269033842,
  "compression_ratio": 1.8492063492063493, "no_speech_prob": 0.0060023353435099125},
  {"id": 254, "seek": 150422, "start": 1521.1000000000001, "end": 1527.02, "text":
  " combinations and then they kind of like explain what you would do to kind of solve
  it right", "tokens": [51208, 21267, 293, 550, 436, 733, 295, 411, 2903, 437, 291,
  576, 360, 281, 733, 295, 5039, 309, 558, 51504], "temperature": 0.0, "avg_logprob":
  -0.110720269033842, "compression_ratio": 1.8492063492063493, "no_speech_prob": 0.0060023353435099125},
  {"id": 255, "seek": 150422, "start": 1527.58, "end": 1533.18, "text": " and you
  you basically develop this situation another another thing is that I found useful",
  "tokens": [51532, 293, 291, 291, 1936, 1499, 341, 2590, 1071, 1071, 551, 307, 300,
  286, 1352, 4420, 51812], "temperature": 0.0, "avg_logprob": -0.110720269033842,
  "compression_ratio": 1.8492063492063493, "no_speech_prob": 0.0060023353435099125},
  {"id": 256, "seek": 153318, "start": 1534.0600000000002, "end": 1539.5, "text":
  " and it also mentioned in the relevant search book by Dr. Nbal and Jerry Bareman",
  "tokens": [50408, 293, 309, 611, 2835, 294, 264, 7340, 3164, 1446, 538, 2491, 13,
  426, 2645, 293, 17454, 4156, 15023, 50680], "temperature": 0.0, "avg_logprob": -0.20245776456945083,
  "compression_ratio": 1.7096774193548387, "no_speech_prob": 0.0024194736033678055},
  {"id": 257, "seek": 153318, "start": 1540.7, "end": 1547.26, "text": " that you
  can you can use like if you would use like let''s say elastic search or similar
  system", "tokens": [50740, 300, 291, 393, 291, 393, 764, 411, 498, 291, 576, 764,
  411, 718, 311, 584, 17115, 3164, 420, 2531, 1185, 51068], "temperature": 0.0, "avg_logprob":
  -0.20245776456945083, "compression_ratio": 1.7096774193548387, "no_speech_prob":
  0.0024194736033678055}, {"id": 258, "seek": 153318, "start": 1547.26, "end": 1554.3,
  "text": " or solar you could actually build a function which explains the query
  step by step right so it", "tokens": [51068, 420, 7936, 291, 727, 767, 1322, 257,
  2445, 597, 13948, 264, 14581, 1823, 538, 1823, 558, 370, 309, 51420], "temperature":
  0.0, "avg_logprob": -0.20245776456945083, "compression_ratio": 1.7096774193548387,
  "no_speech_prob": 0.0024194736033678055}, {"id": 259, "seek": 153318, "start": 1554.3,
  "end": 1560.8600000000001, "text": " basically prints you the tree of how it actually
  came up with that final answer with that final score", "tokens": [51420, 1936, 22305,
  291, 264, 4230, 295, 577, 309, 767, 1361, 493, 365, 300, 2572, 1867, 365, 300, 2572,
  6175, 51748], "temperature": 0.0, "avg_logprob": -0.20245776456945083, "compression_ratio":
  1.7096774193548387, "no_speech_prob": 0.0024194736033678055}, {"id": 260, "seek":
  156086, "start": 1561.5, "end": 1566.4599999999998, "text": " and how you know that
  specific field like for example at TomTom we would I cannot go into much", "tokens":
  [50396, 293, 577, 291, 458, 300, 2685, 2519, 411, 337, 1365, 412, 5041, 23442, 321,
  576, 286, 2644, 352, 666, 709, 50644], "temperature": 0.0, "avg_logprob": -0.15901314128528943,
  "compression_ratio": 1.574468085106383, "no_speech_prob": 0.001898866961710155},
  {"id": 261, "seek": 156086, "start": 1566.4599999999998, "end": 1571.58, "text":
  " specifics what we do at TomTom but basically the geographic search right so you
  type some", "tokens": [50644, 28454, 437, 321, 360, 412, 5041, 23442, 457, 1936,
  264, 32318, 3164, 558, 370, 291, 2010, 512, 50900], "temperature": 0.0, "avg_logprob":
  -0.15901314128528943, "compression_ratio": 1.574468085106383, "no_speech_prob":
  0.001898866961710155}, {"id": 262, "seek": 156086, "start": 1571.58, "end": 1579.1799999999998,
  "text": " destination let''s say an address or maybe a P.O.I name point of interest
  like a shop and it''s", "tokens": [50900, 12236, 718, 311, 584, 364, 2985, 420,
  1310, 257, 430, 13, 46, 13, 40, 1315, 935, 295, 1179, 411, 257, 3945, 293, 309,
  311, 51280], "temperature": 0.0, "avg_logprob": -0.15901314128528943, "compression_ratio":
  1.574468085106383, "no_speech_prob": 0.001898866961710155}, {"id": 263, "seek":
  156086, "start": 1579.1799999999998, "end": 1585.6599999999999, "text": " multilingual
  as well right so obviously your query may hit by accident sometimes in a wrong",
  "tokens": [51280, 2120, 38219, 382, 731, 558, 370, 2745, 428, 14581, 815, 2045,
  538, 6398, 2171, 294, 257, 2085, 51604], "temperature": 0.0, "avg_logprob": -0.15901314128528943,
  "compression_ratio": 1.574468085106383, "no_speech_prob": 0.001898866961710155},
  {"id": 264, "seek": 158566, "start": 1586.38, "end": 1595.42, "text": " language
  field and so the only way to know this is to print that query execution formula
  if you", "tokens": [50400, 2856, 2519, 293, 370, 264, 787, 636, 281, 458, 341, 307,
  281, 4482, 300, 14581, 15058, 8513, 498, 291, 50852], "temperature": 0.0, "avg_logprob":
  -0.139484571373981, "compression_ratio": 1.6756756756756757, "no_speech_prob": 0.0042036147788167},
  {"id": 265, "seek": 158566, "start": 1595.42, "end": 1602.0600000000002, "text":
  " will right and so you will see okay ah it hit in that in that let''s say I don''t
  know a French", "tokens": [50852, 486, 558, 293, 370, 291, 486, 536, 1392, 3716,
  309, 2045, 294, 300, 294, 300, 718, 311, 584, 286, 500, 380, 458, 257, 5522, 51184],
  "temperature": 0.0, "avg_logprob": -0.139484571373981, "compression_ratio": 1.6756756756756757,
  "no_speech_prob": 0.0042036147788167}, {"id": 266, "seek": 158566, "start": 1602.0600000000002,
  "end": 1607.8200000000002, "text": " uh but I wasn''t intending French I was doing
  German or something why did it do that and you", "tokens": [51184, 2232, 457, 286,
  2067, 380, 560, 2029, 5522, 286, 390, 884, 6521, 420, 746, 983, 630, 309, 360, 300,
  293, 291, 51472], "temperature": 0.0, "avg_logprob": -0.139484571373981, "compression_ratio":
  1.6756756756756757, "no_speech_prob": 0.0042036147788167}, {"id": 267, "seek": 158566,
  "start": 1607.8200000000002, "end": 1613.3400000000001, "text": " start reasoning
  about how did I create the tokens because when you tokenize your text it''s", "tokens":
  [51472, 722, 21577, 466, 577, 630, 286, 1884, 264, 22667, 570, 562, 291, 14862,
  1125, 428, 2487, 309, 311, 51748], "temperature": 0.0, "avg_logprob": -0.139484571373981,
  "compression_ratio": 1.6756756756756757, "no_speech_prob": 0.0042036147788167},
  {"id": 268, "seek": 161334, "start": 1613.34, "end": 1619.5, "text": " same problem
  is as in then search in a way like when you split text into paragraphs or sentences",
  "tokens": [50364, 912, 1154, 307, 382, 294, 550, 3164, 294, 257, 636, 411, 562,
  291, 7472, 2487, 666, 48910, 420, 16579, 50672], "temperature": 0.0, "avg_logprob":
  -0.10424212975935503, "compression_ratio": 1.9441624365482233, "no_speech_prob":
  0.0008838446228764951}, {"id": 269, "seek": 161334, "start": 1619.5, "end": 1626.3799999999999,
  "text": " there you need to split the tokens how you do split the tokens is dependent
  on how you model", "tokens": [50672, 456, 291, 643, 281, 7472, 264, 22667, 577,
  291, 360, 7472, 264, 22667, 307, 12334, 322, 577, 291, 2316, 51016], "temperature":
  0.0, "avg_logprob": -0.10424212975935503, "compression_ratio": 1.9441624365482233,
  "no_speech_prob": 0.0008838446228764951}, {"id": 270, "seek": 161334, "start": 1626.3799999999999,
  "end": 1631.82, "text": " the semantics of what you are converting to to a token
  so you should not convert string to a token", "tokens": [51016, 264, 4361, 45298,
  295, 437, 291, 366, 29942, 281, 281, 257, 14862, 370, 291, 820, 406, 7620, 6798,
  281, 257, 14862, 51288], "temperature": 0.0, "avg_logprob": -0.10424212975935503,
  "compression_ratio": 1.9441624365482233, "no_speech_prob": 0.0008838446228764951},
  {"id": 271, "seek": 161334, "start": 1631.82, "end": 1638.22, "text": " you should
  convert meaning to a token so if you capture meaning in that token then you''re
  done", "tokens": [51288, 291, 820, 7620, 3620, 281, 257, 14862, 370, 498, 291, 7983,
  3620, 294, 300, 14862, 550, 291, 434, 1096, 51608], "temperature": 0.0, "avg_logprob":
  -0.10424212975935503, "compression_ratio": 1.9441624365482233, "no_speech_prob":
  0.0008838446228764951}, {"id": 272, "seek": 163822, "start": 1638.3, "end": 1643.98,
  "text": " in a way but then coming back to your question I cannot answer it fully
  now but I highly recommend", "tokens": [50368, 294, 257, 636, 457, 550, 1348, 646,
  281, 428, 1168, 286, 2644, 1867, 309, 4498, 586, 457, 286, 5405, 2748, 50652], "temperature":
  0.0, "avg_logprob": -0.11653264720788163, "compression_ratio": 1.6228813559322033,
  "no_speech_prob": 0.004954421427100897}, {"id": 273, "seek": 163822, "start": 1643.98,
  "end": 1650.7, "text": " that that talk um by can be so you know like you need to
  you need to see how term frequencies", "tokens": [50652, 300, 300, 751, 1105, 538,
  393, 312, 370, 291, 458, 411, 291, 643, 281, 291, 643, 281, 536, 577, 1433, 20250,
  50988], "temperature": 0.0, "avg_logprob": -0.11653264720788163, "compression_ratio":
  1.6228813559322033, "no_speech_prob": 0.004954421427100897}, {"id": 274, "seek":
  163822, "start": 1650.7, "end": 1656.8600000000001, "text": " and inverse document
  frequencies play together and also like in BM25 versus TFID if you have the", "tokens":
  [50988, 293, 17340, 4166, 20250, 862, 1214, 293, 611, 411, 294, 15901, 6074, 5717,
  40964, 2777, 498, 291, 362, 264, 51296], "temperature": 0.0, "avg_logprob": -0.11653264720788163,
  "compression_ratio": 1.6228813559322033, "no_speech_prob": 0.004954421427100897},
  {"id": 275, "seek": 163822, "start": 1656.8600000000001, "end": 1662.78, "text":
  " term saturation issue which is kind of mitigated in BM25 to some extent right
  so meeting that", "tokens": [51296, 1433, 27090, 2734, 597, 307, 733, 295, 15699,
  770, 294, 15901, 6074, 281, 512, 8396, 558, 370, 3440, 300, 51592], "temperature":
  0.0, "avg_logprob": -0.11653264720788163, "compression_ratio": 1.6228813559322033,
  "no_speech_prob": 0.004954421427100897}, {"id": 276, "seek": 166278, "start": 1662.86,
  "end": 1670.06, "text": " if you have two documents um sorry if you have two terms
  which occur like one is like million times", "tokens": [50368, 498, 291, 362, 732,
  8512, 1105, 2597, 498, 291, 362, 732, 2115, 597, 5160, 411, 472, 307, 411, 2459,
  1413, 50728], "temperature": 0.0, "avg_logprob": -0.14323609808216925, "compression_ratio":
  1.6554621848739495, "no_speech_prob": 0.0007610110333189368}, {"id": 277, "seek":
  166278, "start": 1670.06, "end": 1676.46, "text": " and the other one one million
  plus one TFID will be unable to distinguish between these two but like", "tokens":
  [50728, 293, 264, 661, 472, 472, 2459, 1804, 472, 40964, 2777, 486, 312, 11299,
  281, 20206, 1296, 613, 732, 457, 411, 51048], "temperature": 0.0, "avg_logprob":
  -0.14323609808216925, "compression_ratio": 1.6554621848739495, "no_speech_prob":
  0.0007610110333189368}, {"id": 278, "seek": 166278, "start": 1676.46, "end": 1682.1399999999999,
  "text": " BM25 is still sensitive to these things and that''s why it''s a little
  better right so I think it", "tokens": [51048, 15901, 6074, 307, 920, 9477, 281,
  613, 721, 293, 300, 311, 983, 309, 311, 257, 707, 1101, 558, 370, 286, 519, 309,
  51332], "temperature": 0.0, "avg_logprob": -0.14323609808216925, "compression_ratio":
  1.6554621848739495, "no_speech_prob": 0.0007610110333189368}, {"id": 279, "seek":
  166278, "start": 1682.1399999999999, "end": 1688.86, "text": " solves this term
  saturation issue I don''t know if I answered your question but no yeah I think um",
  "tokens": [51332, 39890, 341, 1433, 27090, 2734, 286, 500, 380, 458, 498, 286, 10103,
  428, 1168, 457, 572, 1338, 286, 519, 1105, 51668], "temperature": 0.0, "avg_logprob":
  -0.14323609808216925, "compression_ratio": 1.6554621848739495, "no_speech_prob":
  0.0007610110333189368}, {"id": 280, "seek": 168886, "start": 1688.9399999999998,
  "end": 1695.5, "text": " so yeah a couple things I really want to continue on this
  TFID versus BM25 and then", "tokens": [50368, 370, 1338, 257, 1916, 721, 286, 534,
  528, 281, 2354, 322, 341, 40964, 2777, 5717, 15901, 6074, 293, 550, 50696], "temperature":
  0.0, "avg_logprob": -0.16922562986939818, "compression_ratio": 1.6608695652173913,
  "no_speech_prob": 0.004990188404917717}, {"id": 281, "seek": 168886, "start": 1695.5,
  "end": 1701.9799999999998, "text": " adverse displayed to it I think you''re I think
  this like pseudo relevance feedback is that like the", "tokens": [50696, 27590,
  16372, 281, 309, 286, 519, 291, 434, 286, 519, 341, 411, 35899, 32684, 5824, 307,
  300, 411, 264, 51020], "temperature": 0.0, "avg_logprob": -0.16922562986939818,
  "compression_ratio": 1.6608695652173913, "no_speech_prob": 0.004990188404917717},
  {"id": 282, "seek": 168886, "start": 1701.9799999999998, "end": 1708.06, "text":
  " phrase I give to show that like um if you''re searching with BM25 you say if you
  had added this key", "tokens": [51020, 9535, 286, 976, 281, 855, 300, 411, 1105,
  498, 291, 434, 10808, 365, 15901, 6074, 291, 584, 498, 291, 632, 3869, 341, 2141,
  51324], "temperature": 0.0, "avg_logprob": -0.16922562986939818, "compression_ratio":
  1.6608695652173913, "no_speech_prob": 0.004990188404917717}, {"id": 283, "seek":
  168886, "start": 1708.06, "end": 1713.02, "text": " like you have the gold document
  and you''re like how would I have modified the query to produce that", "tokens":
  [51324, 411, 291, 362, 264, 3821, 4166, 293, 291, 434, 411, 577, 576, 286, 362,
  15873, 264, 14581, 281, 5258, 300, 51572], "temperature": 0.0, "avg_logprob": -0.16922562986939818,
  "compression_ratio": 1.6608695652173913, "no_speech_prob": 0.004990188404917717},
  {"id": 284, "seek": 171302, "start": 1713.1, "end": 1718.7, "text": " document is
  it so I think that yeah that''s one way another way is to how would you modify the",
  "tokens": [50368, 4166, 307, 309, 370, 286, 519, 300, 1338, 300, 311, 472, 636,
  1071, 636, 307, 281, 577, 576, 291, 16927, 264, 50648], "temperature": 0.0, "avg_logprob":
  -0.16671668342922044, "compression_ratio": 2.0672268907563027, "no_speech_prob":
  0.004055447410792112}, {"id": 285, "seek": 171302, "start": 1718.7, "end": 1724.78,
  "text": " indexing that''s more in your control right so how you would modify the
  indexing for example you would", "tokens": [50648, 8186, 278, 300, 311, 544, 294,
  428, 1969, 558, 370, 577, 291, 576, 16927, 264, 8186, 278, 337, 1365, 291, 576,
  50952], "temperature": 0.0, "avg_logprob": -0.16671668342922044, "compression_ratio":
  2.0672268907563027, "no_speech_prob": 0.004055447410792112}, {"id": 286, "seek":
  171302, "start": 1724.78, "end": 1729.18, "text": " in some cases you can remove
  the applicates or something right so like you don''t you don''t need them", "tokens":
  [50952, 294, 512, 3331, 291, 393, 4159, 264, 2580, 1024, 420, 746, 558, 370, 411,
  291, 500, 380, 291, 500, 380, 643, 552, 51172], "temperature": 0.0, "avg_logprob":
  -0.16671668342922044, "compression_ratio": 2.0672268907563027, "no_speech_prob":
  0.004055447410792112}, {"id": 287, "seek": 171302, "start": 1729.18, "end": 1733.82,
  "text": " or something like that you can you can or you can split the term by numbers
  or something right if", "tokens": [51172, 420, 746, 411, 300, 291, 393, 291, 393,
  420, 291, 393, 7472, 264, 1433, 538, 3547, 420, 746, 558, 498, 51404], "temperature":
  0.0, "avg_logprob": -0.16671668342922044, "compression_ratio": 2.0672268907563027,
  "no_speech_prob": 0.004055447410792112}, {"id": 288, "seek": 171302, "start": 1733.82,
  "end": 1738.46, "text": " they happen to occur inside the term something like I''m
  making these examples but I''m saying that", "tokens": [51404, 436, 1051, 281, 5160,
  1854, 264, 1433, 746, 411, 286, 478, 1455, 613, 5110, 457, 286, 478, 1566, 300,
  51636], "temperature": 0.0, "avg_logprob": -0.16671668342922044, "compression_ratio":
  2.0672268907563027, "no_speech_prob": 0.004055447410792112}, {"id": 289, "seek":
  173846, "start": 1738.46, "end": 1742.8600000000001, "text": " you have more control
  in the indexing than in the query but in the in the query you can model", "tokens":
  [50364, 291, 362, 544, 1969, 294, 264, 8186, 278, 813, 294, 264, 14581, 457, 294,
  264, 294, 264, 14581, 291, 393, 2316, 50584], "temperature": 0.0, "avg_logprob":
  -0.16090306082924644, "compression_ratio": 1.8317307692307692, "no_speech_prob":
  0.0031507625244557858}, {"id": 290, "seek": 173846, "start": 1742.8600000000001,
  "end": 1749.3400000000001, "text": " like query similarity for example right so
  yeah oh that''s super interesting yeah the the way that", "tokens": [50584, 411,
  14581, 32194, 337, 1365, 558, 370, 1338, 1954, 300, 311, 1687, 1880, 1338, 264,
  264, 636, 300, 50908], "temperature": 0.0, "avg_logprob": -0.16090306082924644,
  "compression_ratio": 1.8317307692307692, "no_speech_prob": 0.0031507625244557858},
  {"id": 291, "seek": 173846, "start": 1749.3400000000001, "end": 1754.6200000000001,
  "text": " you do like the text preprocessing like stemming stopper removal all that
  all that that bag of", "tokens": [50908, 291, 360, 411, 264, 2487, 2666, 340, 780,
  278, 411, 12312, 2810, 1590, 610, 17933, 439, 300, 439, 300, 300, 3411, 295, 51172],
  "temperature": 0.0, "avg_logprob": -0.16090306082924644, "compression_ratio": 1.8317307692307692,
  "no_speech_prob": 0.0031507625244557858}, {"id": 292, "seek": 173846, "start": 1755.98,
  "end": 1761.9, "text": " that''s what I hope dense vector search can kill all that
  I hope you can just like anything can", "tokens": [51240, 300, 311, 437, 286, 1454,
  18011, 8062, 3164, 393, 1961, 439, 300, 286, 1454, 291, 393, 445, 411, 1340, 393,
  51536], "temperature": 0.0, "avg_logprob": -0.16090306082924644, "compression_ratio":
  1.8317307692307692, "no_speech_prob": 0.0031507625244557858}, {"id": 293, "seek":
  176190, "start": 1761.9, "end": 1769.98, "text": " go into it yeah and but um yeah
  and so I think there''s this this thing called like decoding the", "tokens": [50364,
  352, 666, 309, 1338, 293, 457, 1105, 1338, 293, 370, 286, 519, 456, 311, 341, 341,
  551, 1219, 411, 979, 8616, 264, 50768], "temperature": 0.0, "avg_logprob": -0.11056596827956866,
  "compression_ratio": 1.9061224489795918, "no_speech_prob": 7.760502921883017e-05},
  {"id": 294, "seek": 176190, "start": 1769.98, "end": 1773.9, "text": " latent space
  of a vector search model on that other idea of what query would have produced this",
  "tokens": [50768, 48994, 1901, 295, 257, 8062, 3164, 2316, 322, 300, 661, 1558,
  295, 437, 14581, 576, 362, 7126, 341, 50964], "temperature": 0.0, "avg_logprob":
  -0.11056596827956866, "compression_ratio": 1.9061224489795918, "no_speech_prob":
  7.760502921883017e-05}, {"id": 295, "seek": 176190, "start": 1773.9, "end": 1779.02,
  "text": " where you would take the you would train a language model on document
  query pairs and then", "tokens": [50964, 689, 291, 576, 747, 264, 291, 576, 3847,
  257, 2856, 2316, 322, 4166, 14581, 15494, 293, 550, 51220], "temperature": 0.0,
  "avg_logprob": -0.11056596827956866, "compression_ratio": 1.9061224489795918, "no_speech_prob":
  7.760502921883017e-05}, {"id": 296, "seek": 176190, "start": 1779.02, "end": 1783.1000000000001,
  "text": " it would generate a query that would have matched the document maybe that''s
  useful but", "tokens": [51220, 309, 576, 8460, 257, 14581, 300, 576, 362, 21447,
  264, 4166, 1310, 300, 311, 4420, 457, 51424], "temperature": 0.0, "avg_logprob":
  -0.11056596827956866, "compression_ratio": 1.9061224489795918, "no_speech_prob":
  7.760502921883017e-05}, {"id": 297, "seek": 176190, "start": 1783.1000000000001,
  "end": 1788.7800000000002, "text": " but I''m also I''m very curious what you think
  about this idea of split vectors so split vectors is", "tokens": [51424, 457, 286,
  478, 611, 286, 478, 588, 6369, 437, 291, 519, 466, 341, 1558, 295, 7472, 18875,
  370, 7472, 18875, 307, 51708], "temperature": 0.0, "avg_logprob": -0.11056596827956866,
  "compression_ratio": 1.9061224489795918, "no_speech_prob": 7.760502921883017e-05},
  {"id": 298, "seek": 178878, "start": 1788.78, "end": 1795.98, "text": " like you
  keep the mass language modeling head and so you encode the thing into the vectors
  so the", "tokens": [50364, 411, 291, 1066, 264, 2758, 2856, 15983, 1378, 293, 370,
  291, 2058, 1429, 264, 551, 666, 264, 18875, 370, 264, 50724], "temperature": 0.0,
  "avg_logprob": -0.07786177689174437, "compression_ratio": 2.0638297872340425, "no_speech_prob":
  0.0008971040369942784}, {"id": 299, "seek": 178878, "start": 1795.98, "end": 1801.18,
  "text": " mass language modeling head always only takes in a vector as input you
  always would mask out whatever", "tokens": [50724, 2758, 2856, 15983, 1378, 1009,
  787, 2516, 294, 257, 8062, 382, 4846, 291, 1009, 576, 6094, 484, 2035, 50984], "temperature":
  0.0, "avg_logprob": -0.07786177689174437, "compression_ratio": 2.0638297872340425,
  "no_speech_prob": 0.0008971040369942784}, {"id": 300, "seek": 178878, "start": 1801.18,
  "end": 1806.1399999999999, "text": " the mass token was and then send just that
  vector to the mass language modeling head that will produce", "tokens": [50984,
  264, 2758, 14862, 390, 293, 550, 2845, 445, 300, 8062, 281, 264, 2758, 2856, 15983,
  1378, 300, 486, 5258, 51232], "temperature": 0.0, "avg_logprob": -0.07786177689174437,
  "compression_ratio": 2.0638297872340425, "no_speech_prob": 0.0008971040369942784},
  {"id": 301, "seek": 178878, "start": 1806.1399999999999, "end": 1812.1399999999999,
  "text": " like a sparse distribution over what would replace it and so I think the
  the idea behind", "tokens": [51232, 411, 257, 637, 11668, 7316, 670, 437, 576, 7406,
  309, 293, 370, 286, 519, 264, 264, 1558, 2261, 51532], "temperature": 0.0, "avg_logprob":
  -0.07786177689174437, "compression_ratio": 2.0638297872340425, "no_speech_prob":
  0.0008971040369942784}, {"id": 302, "seek": 178878, "start": 1812.1399999999999,
  "end": 1816.46, "text": " split is that you do that for each token and then you
  just kind of average all the vocabulary", "tokens": [51532, 7472, 307, 300, 291,
  360, 300, 337, 1184, 14862, 293, 550, 291, 445, 733, 295, 4274, 439, 264, 19864,
  51748], "temperature": 0.0, "avg_logprob": -0.07786177689174437, "compression_ratio":
  2.0638297872340425, "no_speech_prob": 0.0008971040369942784}, {"id": 303, "seek":
  181646, "start": 1816.54, "end": 1823.02, "text": " distributions and that gives
  you a sparse vector that represents like the like happy euphoric", "tokens": [50368,
  37870, 293, 300, 2709, 291, 257, 637, 11668, 8062, 300, 8855, 411, 264, 411, 2055,
  2228, 950, 16345, 50692], "temperature": 0.0, "avg_logprob": -0.1260408688617009,
  "compression_ratio": 1.7880184331797235, "no_speech_prob": 0.011306462809443474},
  {"id": 304, "seek": 181646, "start": 1823.02, "end": 1830.6200000000001, "text":
  " ecstatic like the kind of synonyms behind it do you like that kind of idea yeah
  yeah uh uh I like that", "tokens": [50692, 11437, 34632, 411, 264, 733, 295, 5451,
  2526, 2592, 2261, 309, 360, 291, 411, 300, 733, 295, 1558, 1338, 1338, 2232, 2232,
  286, 411, 300, 51072], "temperature": 0.0, "avg_logprob": -0.1260408688617009, "compression_ratio":
  1.7880184331797235, "no_speech_prob": 0.011306462809443474}, {"id": 305, "seek":
  181646, "start": 1832.14, "end": 1838.54, "text": " the fact that I think we can
  step back from like this dense vector limitations and go back and", "tokens": [51148,
  264, 1186, 300, 286, 519, 321, 393, 1823, 646, 490, 411, 341, 18011, 8062, 15705,
  293, 352, 646, 293, 51468], "temperature": 0.0, "avg_logprob": -0.1260408688617009,
  "compression_ratio": 1.7880184331797235, "no_speech_prob": 0.011306462809443474},
  {"id": 306, "seek": 181646, "start": 1838.54, "end": 1844.14, "text": " try to capture
  what sparse vectors do because if I don''t know if you watch the episode with duck",
  "tokens": [51468, 853, 281, 7983, 437, 637, 11668, 18875, 360, 570, 498, 286, 500,
  380, 458, 498, 291, 1159, 264, 3500, 365, 12482, 51748], "temperature": 0.0, "avg_logprob":
  -0.1260408688617009, "compression_ratio": 1.7880184331797235, "no_speech_prob":
  0.011306462809443474}, {"id": 307, "seek": 184414, "start": 1844.14, "end": 1849.1000000000001,
  "text": " Turnbull but he actually shed the light on on this really well by saying
  hey if you if you take the", "tokens": [50364, 7956, 37290, 457, 415, 767, 14951,
  264, 1442, 322, 322, 341, 534, 731, 538, 1566, 4177, 498, 291, 498, 291, 747, 264,
  50612], "temperature": 0.0, "avg_logprob": -0.14839756604537224, "compression_ratio":
  1.8221343873517786, "no_speech_prob": 0.0030631099361926317}, {"id": 308, "seek":
  184414, "start": 1849.1000000000001, "end": 1856.22, "text": " keyword retrieval
  inverted index you deal with like probably hundreds of thousands of dimensions",
  "tokens": [50612, 20428, 19817, 3337, 38969, 8186, 291, 2028, 365, 411, 1391, 6779,
  295, 5383, 295, 12819, 50968], "temperature": 0.0, "avg_logprob": -0.14839756604537224,
  "compression_ratio": 1.8221343873517786, "no_speech_prob": 0.0030631099361926317},
  {"id": 309, "seek": 184414, "start": 1856.22, "end": 1863.1000000000001, "text":
  " unless millions unless billions like in some of the indexes we had at least million
  per term right", "tokens": [50968, 5969, 6803, 5969, 17375, 411, 294, 512, 295,
  264, 8186, 279, 321, 632, 412, 1935, 2459, 680, 1433, 558, 51312], "temperature":
  0.0, "avg_logprob": -0.14839756604537224, "compression_ratio": 1.8221343873517786,
  "no_speech_prob": 0.0030631099361926317}, {"id": 310, "seek": 184414, "start": 1863.1000000000001,
  "end": 1868.0600000000002, "text": " so that''s like million positions most of which
  are zeros because this term doesn''t occur", "tokens": [51312, 370, 300, 311, 411,
  2459, 8432, 881, 295, 597, 366, 35193, 570, 341, 1433, 1177, 380, 5160, 51560],
  "temperature": 0.0, "avg_logprob": -0.14839756604537224, "compression_ratio": 1.8221343873517786,
  "no_speech_prob": 0.0030631099361926317}, {"id": 311, "seek": 184414, "start": 1869.0200000000002,
  "end": 1873.9, "text": " you know in in specific doc but like doc id but like it
  occurs like in a few", "tokens": [51608, 291, 458, 294, 294, 2685, 3211, 457, 411,
  3211, 4496, 457, 411, 309, 11843, 411, 294, 257, 1326, 51852], "temperature": 0.0,
  "avg_logprob": -0.14839756604537224, "compression_ratio": 1.8221343873517786, "no_speech_prob":
  0.0030631099361926317}, {"id": 312, "seek": 187390, "start": 1873.98, "end": 1880.5400000000002,
  "text": " and so in dense retrieval you sort of like compress all of these to let''s
  say 256 dimensions", "tokens": [50368, 293, 370, 294, 18011, 19817, 3337, 291, 1333,
  295, 411, 14778, 439, 295, 613, 281, 718, 311, 584, 3552, 21, 12819, 50696], "temperature":
  0.0, "avg_logprob": -0.15437527611142113, "compression_ratio": 1.7598425196850394,
  "no_speech_prob": 5.92911419516895e-05}, {"id": 313, "seek": 187390, "start": 1880.5400000000002,
  "end": 1886.14, "text": " and inherently you lose the precision right so it becomes
  more like recall oriented", "tokens": [50696, 293, 27993, 291, 3624, 264, 18356,
  558, 370, 309, 3643, 544, 411, 9901, 21841, 50976], "temperature": 0.0, "avg_logprob":
  -0.15437527611142113, "compression_ratio": 1.7598425196850394, "no_speech_prob":
  5.92911419516895e-05}, {"id": 314, "seek": 187390, "start": 1887.1000000000001,
  "end": 1892.3000000000002, "text": " rather than you know in sparse you you basically
  like what also it means spars is that", "tokens": [51024, 2831, 813, 291, 458, 294,
  637, 11668, 291, 291, 1936, 411, 437, 611, 309, 1355, 637, 685, 307, 300, 51284],
  "temperature": 0.0, "avg_logprob": -0.15437527611142113, "compression_ratio": 1.7598425196850394,
  "no_speech_prob": 5.92911419516895e-05}, {"id": 315, "seek": 187390, "start": 1893.18,
  "end": 1898.0600000000002, "text": " this is probably like a little bit like going
  back to n and algorithms right so like an inverted", "tokens": [51328, 341, 307,
  1391, 411, 257, 707, 857, 411, 516, 646, 281, 297, 293, 14642, 558, 370, 411, 364,
  38969, 51572], "temperature": 0.0, "avg_logprob": -0.15437527611142113, "compression_ratio":
  1.7598425196850394, "no_speech_prob": 5.92911419516895e-05}, {"id": 316, "seek":
  187390, "start": 1898.0600000000002, "end": 1903.1000000000001, "text": " index
  it''s basically like a hash table so I have this term it''s like order one look
  up", "tokens": [51572, 8186, 309, 311, 1936, 411, 257, 22019, 3199, 370, 286, 362,
  341, 1433, 309, 311, 411, 1668, 472, 574, 493, 51824], "temperature": 0.0, "avg_logprob":
  -0.15437527611142113, "compression_ratio": 1.7598425196850394, "no_speech_prob":
  5.92911419516895e-05}, {"id": 317, "seek": 190310, "start": 1903.6599999999999,
  "end": 1909.26, "text": " in the hash table and then you leapfrog you use this leapfrog
  algorithm implemented really well", "tokens": [50392, 294, 264, 22019, 3199, 293,
  550, 291, 19438, 69, 6675, 291, 764, 341, 19438, 69, 6675, 9284, 12270, 534, 731,
  50672], "temperature": 0.0, "avg_logprob": -0.14221199904337967, "compression_ratio":
  1.7256637168141593, "no_speech_prob": 0.0008186838822439313}, {"id": 318, "seek":
  190310, "start": 1909.26, "end": 1917.1799999999998, "text": " in leucine for example
  how you jump over long strides of consecutive doc id''s because you don''t", "tokens":
  [50672, 294, 476, 1311, 533, 337, 1365, 577, 291, 3012, 670, 938, 1056, 1875, 295,
  30497, 3211, 4496, 311, 570, 291, 500, 380, 51068], "temperature": 0.0, "avg_logprob":
  -0.14221199904337967, "compression_ratio": 1.7256637168141593, "no_speech_prob":
  0.0008186838822439313}, {"id": 319, "seek": 190310, "start": 1917.1799999999998,
  "end": 1923.1, "text": " really need to examine them in an antiquity let''s say
  if it''s cat and dog you know you know that cat", "tokens": [51068, 534, 643, 281,
  17496, 552, 294, 364, 41036, 507, 718, 311, 584, 498, 309, 311, 3857, 293, 3000,
  291, 458, 291, 458, 300, 3857, 51364], "temperature": 0.0, "avg_logprob": -0.14221199904337967,
  "compression_ratio": 1.7256637168141593, "no_speech_prob": 0.0008186838822439313},
  {"id": 320, "seek": 190310, "start": 1923.1, "end": 1930.78, "text": " occurs in
  the document id5 well I don''t know like 10 let''s say and for dog you are on on
  on three", "tokens": [51364, 11843, 294, 264, 4166, 4496, 20, 731, 286, 500, 380,
  458, 411, 1266, 718, 311, 584, 293, 337, 3000, 291, 366, 322, 322, 322, 1045, 51748],
  "temperature": 0.0, "avg_logprob": -0.14221199904337967, "compression_ratio": 1.7256637168141593,
  "no_speech_prob": 0.0008186838822439313}, {"id": 321, "seek": 193078, "start": 1930.78,
  "end": 1936.3, "text": " so you can leapfrog all the way to 10 you don''t really
  need to check all this in because they will", "tokens": [50364, 370, 291, 393, 19438,
  69, 6675, 439, 264, 636, 281, 1266, 291, 500, 380, 534, 643, 281, 1520, 439, 341,
  294, 570, 436, 486, 50640], "temperature": 0.0, "avg_logprob": -0.10259765233748998,
  "compression_ratio": 1.879245283018868, "no_speech_prob": 0.0011099160183221102},
  {"id": 322, "seek": 193078, "start": 1936.3, "end": 1942.78, "text": " never occur
  together so for or query that''s another story because that''s a union but for and
  query", "tokens": [50640, 1128, 5160, 1214, 370, 337, 420, 14581, 300, 311, 1071,
  1657, 570, 300, 311, 257, 11671, 457, 337, 293, 14581, 50964], "temperature": 0.0,
  "avg_logprob": -0.10259765233748998, "compression_ratio": 1.879245283018868, "no_speech_prob":
  0.0011099160183221102}, {"id": 323, "seek": 193078, "start": 1942.78, "end": 1947.5,
  "text": " it''s an intersection so you always need an intersection you can then
  stop early because you don''t need", "tokens": [50964, 309, 311, 364, 15236, 370,
  291, 1009, 643, 364, 15236, 291, 393, 550, 1590, 2440, 570, 291, 500, 380, 643,
  51200], "temperature": 0.0, "avg_logprob": -0.10259765233748998, "compression_ratio":
  1.879245283018868, "no_speech_prob": 0.0011099160183221102}, {"id": 324, "seek":
  193078, "start": 1947.5, "end": 1953.82, "text": " 100,000 results on the screen
  right and I''m still actually curious on how would you know when to", "tokens":
  [51200, 2319, 11, 1360, 3542, 322, 264, 2568, 558, 293, 286, 478, 920, 767, 6369,
  322, 577, 576, 291, 458, 562, 281, 51516], "temperature": 0.0, "avg_logprob": -0.10259765233748998,
  "compression_ratio": 1.879245283018868, "no_speech_prob": 0.0011099160183221102},
  {"id": 325, "seek": 193078, "start": 1953.82, "end": 1959.74, "text": " stop because
  what if you didn''t find the document that is even more relevant that what you have
  seen", "tokens": [51516, 1590, 570, 437, 498, 291, 994, 380, 915, 264, 4166, 300,
  307, 754, 544, 7340, 300, 437, 291, 362, 1612, 51812], "temperature": 0.0, "avg_logprob":
  -0.10259765233748998, "compression_ratio": 1.879245283018868, "no_speech_prob":
  0.0011099160183221102}, {"id": 326, "seek": 195974, "start": 1959.74, "end": 1964.06,
  "text": " so far but that''s like a matter of debate I guess but then you start
  scoring them and then", "tokens": [50364, 370, 1400, 457, 300, 311, 411, 257, 1871,
  295, 7958, 286, 2041, 457, 550, 291, 722, 22358, 552, 293, 550, 50580], "temperature":
  0.0, "avg_logprob": -0.17003371498801492, "compression_ratio": 1.7827715355805243,
  "no_speech_prob": 0.011692658066749573}, {"id": 327, "seek": 195974, "start": 1964.06,
  "end": 1969.42, "text": " sorting them were relevance right yeah sorry if I''m a
  little behind them so is this referring to", "tokens": [50580, 32411, 552, 645,
  32684, 558, 1338, 2597, 498, 286, 478, 257, 707, 2261, 552, 370, 307, 341, 13761,
  281, 50848], "temperature": 0.0, "avg_logprob": -0.17003371498801492, "compression_ratio":
  1.7827715355805243, "no_speech_prob": 0.011692658066749573}, {"id": 328, "seek":
  195974, "start": 1969.42, "end": 1975.02, "text": " how you can use like an inverted
  index to calculate the BM25 scores so I would you know with my", "tokens": [50848,
  577, 291, 393, 764, 411, 364, 38969, 8186, 281, 8873, 264, 15901, 6074, 13444, 370,
  286, 576, 291, 458, 365, 452, 51128], "temperature": 0.0, "avg_logprob": -0.17003371498801492,
  "compression_ratio": 1.7827715355805243, "no_speech_prob": 0.011692658066749573},
  {"id": 329, "seek": 195974, "start": 1975.02, "end": 1980.38, "text": " document
  collection if dog appears I you know dog and the documents so that when I''m calculating",
  "tokens": [51128, 4166, 5765, 498, 3000, 7038, 286, 291, 458, 3000, 293, 264, 8512,
  370, 300, 562, 286, 478, 28258, 51396], "temperature": 0.0, "avg_logprob": -0.17003371498801492,
  "compression_ratio": 1.7827715355805243, "no_speech_prob": 0.011692658066749573},
  {"id": 330, "seek": 195974, "start": 1980.94, "end": 1987.74, "text": " yeah yeah
  but like the the the the I guess the comparison I wanted to make to dance search
  that", "tokens": [51424, 1338, 1338, 457, 411, 264, 264, 264, 264, 286, 2041, 264,
  9660, 286, 1415, 281, 652, 281, 4489, 3164, 300, 51764], "temperature": 0.0, "avg_logprob":
  -0.17003371498801492, "compression_ratio": 1.7827715355805243, "no_speech_prob":
  0.011692658066749573}, {"id": 331, "seek": 198774, "start": 1987.82, "end": 1993.26,
  "text": " like an old vector search is that they are on the on the base data structure
  first of all you have a", "tokens": [50368, 411, 364, 1331, 8062, 3164, 307, 300,
  436, 366, 322, 264, 322, 264, 3096, 1412, 3877, 700, 295, 439, 291, 362, 257, 50640],
  "temperature": 0.0, "avg_logprob": -0.11560722224968524, "compression_ratio": 1.871212121212121,
  "no_speech_prob": 0.0028415711130946875}, {"id": 332, "seek": 198774, "start": 1993.26,
  "end": 1999.5, "text": " choice of the algorithm you want to use but let''s say
  we take hnsw which is the most popular right", "tokens": [50640, 3922, 295, 264,
  9284, 291, 528, 281, 764, 457, 718, 311, 584, 321, 747, 276, 3695, 86, 597, 307,
  264, 881, 3743, 558, 50952], "temperature": 0.0, "avg_logprob": -0.11560722224968524,
  "compression_ratio": 1.871212121212121, "no_speech_prob": 0.0028415711130946875},
  {"id": 333, "seek": 198774, "start": 1999.5, "end": 2005.98, "text": " also implemented
  in v8 I know but like you don''t know when you enter the first layer you don''t
  know", "tokens": [50952, 611, 12270, 294, 371, 23, 286, 458, 457, 411, 291, 500,
  380, 458, 562, 291, 3242, 264, 700, 4583, 291, 500, 380, 458, 51276], "temperature":
  0.0, "avg_logprob": -0.11560722224968524, "compression_ratio": 1.871212121212121,
  "no_speech_prob": 0.0028415711130946875}, {"id": 334, "seek": 198774, "start": 2005.98,
  "end": 2011.82, "text": " where exactly you will end up like so like with hash table
  I know exactly where I''m entering and I", "tokens": [51276, 689, 2293, 291, 486,
  917, 493, 411, 370, 411, 365, 22019, 3199, 286, 458, 2293, 689, 286, 478, 11104,
  293, 286, 51568], "temperature": 0.0, "avg_logprob": -0.11560722224968524, "compression_ratio":
  1.871212121212121, "no_speech_prob": 0.0028415711130946875}, {"id": 335, "seek":
  198774, "start": 2011.82, "end": 2016.86, "text": " know that I''m exactly in the
  right place right and you know you can also expand your query with", "tokens": [51568,
  458, 300, 286, 478, 2293, 294, 264, 558, 1081, 558, 293, 291, 458, 291, 393, 611,
  5268, 428, 14581, 365, 51820], "temperature": 0.0, "avg_logprob": -0.11560722224968524,
  "compression_ratio": 1.871212121212121, "no_speech_prob": 0.0028415711130946875},
  {"id": 336, "seek": 201686, "start": 2016.86, "end": 2021.6599999999999, "text":
  " synonyms then you enter more more points in the hash table and you start traversing
  all of them", "tokens": [50364, 5451, 2526, 2592, 550, 291, 3242, 544, 544, 2793,
  294, 264, 22019, 3199, 293, 291, 722, 23149, 278, 439, 295, 552, 50604], "temperature":
  0.0, "avg_logprob": -0.1212303990903108, "compression_ratio": 1.8028673835125448,
  "no_speech_prob": 0.00046189434942789376}, {"id": 337, "seek": 201686, "start":
  2022.2199999999998, "end": 2028.78, "text": " in parallel and you come up with the
  answer but in dance search you need to like accept the uncertainty", "tokens": [50632,
  294, 8952, 293, 291, 808, 493, 365, 264, 1867, 457, 294, 4489, 3164, 291, 643, 281,
  411, 3241, 264, 15697, 50960], "temperature": 0.0, "avg_logprob": -0.1212303990903108,
  "compression_ratio": 1.8028673835125448, "no_speech_prob": 0.00046189434942789376},
  {"id": 338, "seek": 201686, "start": 2028.78, "end": 2034.54, "text": " of navigating
  that graph you don''t know where it will land it has certain limitations and trade-offs",
  "tokens": [50960, 295, 32054, 300, 4295, 291, 500, 380, 458, 689, 309, 486, 2117,
  309, 575, 1629, 15705, 293, 4923, 12, 19231, 51248], "temperature": 0.0, "avg_logprob":
  -0.1212303990903108, "compression_ratio": 1.8028673835125448, "no_speech_prob":
  0.00046189434942789376}, {"id": 339, "seek": 201686, "start": 2035.1799999999998,
  "end": 2040.86, "text": " and then it will pull up you know some nearest neighbors
  and probably you should be happy with them", "tokens": [51280, 293, 550, 309, 486,
  2235, 493, 291, 458, 512, 23831, 12512, 293, 1391, 291, 820, 312, 2055, 365, 552,
  51564], "temperature": 0.0, "avg_logprob": -0.1212303990903108, "compression_ratio":
  1.8028673835125448, "no_speech_prob": 0.00046189434942789376}, {"id": 340, "seek":
  201686, "start": 2040.86, "end": 2046.06, "text": " because oh otherwise you need
  to do it twice so that price and so on you see what I mean right so like", "tokens":
  [51564, 570, 1954, 5911, 291, 643, 281, 360, 309, 6091, 370, 300, 3218, 293, 370,
  322, 291, 536, 437, 286, 914, 558, 370, 411, 51824], "temperature": 0.0, "avg_logprob":
  -0.1212303990903108, "compression_ratio": 1.8028673835125448, "no_speech_prob":
  0.00046189434942789376}, {"id": 341, "seek": 204606, "start": 2046.06, "end": 2052.06,
  "text": " they are fundamentally different also on search side oh in like this stochastic
  nature of the", "tokens": [50364, 436, 366, 17879, 819, 611, 322, 3164, 1252, 1954,
  294, 411, 341, 342, 8997, 2750, 3687, 295, 264, 50664], "temperature": 0.0, "avg_logprob":
  -0.26909617787783907, "compression_ratio": 1.6540084388185654, "no_speech_prob":
  0.0017145555466413498}, {"id": 342, "seek": 204606, "start": 2053.42, "end": 2059.5,
  "text": " yeah and also I read this paper called OOD disganan that talks about how
  much the distribution shift can", "tokens": [50732, 1338, 293, 611, 286, 1401, 341,
  3035, 1219, 422, 14632, 717, 1275, 282, 300, 6686, 466, 577, 709, 264, 7316, 5513,
  393, 51036], "temperature": 0.0, "avg_logprob": -0.26909617787783907, "compression_ratio":
  1.6540084388185654, "no_speech_prob": 0.0017145555466413498}, {"id": 343, "seek":
  204606, "start": 2059.5, "end": 2065.58, "text": " impact the graph based vimana
  so vimana is like hnsw but you flatten it so there''s no longer the", "tokens":
  [51036, 2712, 264, 4295, 2361, 371, 36497, 370, 371, 36497, 307, 411, 276, 3695,
  86, 457, 291, 24183, 309, 370, 456, 311, 572, 2854, 264, 51340], "temperature":
  0.0, "avg_logprob": -0.26909617787783907, "compression_ratio": 1.6540084388185654,
  "no_speech_prob": 0.0017145555466413498}, {"id": 344, "seek": 204606, "start": 2065.58,
  "end": 2069.82, "text": " hierarchy of layers it''s like all the same thing and
  then you can put it on disk and it''s like a", "tokens": [51340, 22333, 295, 7914,
  309, 311, 411, 439, 264, 912, 551, 293, 550, 291, 393, 829, 309, 322, 12355, 293,
  309, 311, 411, 257, 51552], "temperature": 0.0, "avg_logprob": -0.26909617787783907,
  "compression_ratio": 1.6540084388185654, "no_speech_prob": 0.0017145555466413498},
  {"id": 345, "seek": 206982, "start": 2069.82, "end": 2077.82, "text": " little cheaper
  run I think yeah it''s fascinating the whole indexing the part that that''s like
  kind", "tokens": [50364, 707, 12284, 1190, 286, 519, 1338, 309, 311, 10343, 264,
  1379, 8186, 278, 264, 644, 300, 300, 311, 411, 733, 50764], "temperature": 0.0,
  "avg_logprob": -0.2313916761796553, "compression_ratio": 1.737556561085973, "no_speech_prob":
  0.0035739107988774776}, {"id": 346, "seek": 206982, "start": 2077.82, "end": 2085.5,
  "text": " of the the meat of this especially from wavy aspect of that''s where I
  see and in addition to", "tokens": [50764, 295, 264, 264, 4615, 295, 341, 2318,
  490, 261, 15498, 4171, 295, 300, 311, 689, 286, 536, 293, 294, 4500, 281, 51148],
  "temperature": 0.0, "avg_logprob": -0.2313916761796553, "compression_ratio": 1.737556561085973,
  "no_speech_prob": 0.0035739107988774776}, {"id": 347, "seek": 206982, "start": 2085.5,
  "end": 2090.06, "text": " you know the ux and making it like a very developer friendly
  to well there''s a few sides to it", "tokens": [51148, 291, 458, 264, 344, 87, 293,
  1455, 309, 411, 257, 588, 10754, 9208, 281, 731, 456, 311, 257, 1326, 4881, 281,
  309, 51376], "temperature": 0.0, "avg_logprob": -0.2313916761796553, "compression_ratio":
  1.737556561085973, "no_speech_prob": 0.0035739107988774776}, {"id": 348, "seek":
  206982, "start": 2090.06, "end": 2095.1800000000003, "text": " because there''s
  also the distributed database part and you know all the written and go laying the",
  "tokens": [51376, 570, 456, 311, 611, 264, 12631, 8149, 644, 293, 291, 458, 439,
  264, 3720, 293, 352, 14903, 264, 51632], "temperature": 0.0, "avg_logprob": -0.2313916761796553,
  "compression_ratio": 1.737556561085973, "no_speech_prob": 0.0035739107988774776},
  {"id": 349, "seek": 209518, "start": 2095.18, "end": 2100.94, "text": " concurrency
  control you know the replication of the backups like all these kind of things like
  that", "tokens": [50364, 23702, 10457, 1969, 291, 458, 264, 39911, 295, 264, 50160,
  411, 439, 613, 733, 295, 721, 411, 300, 50652], "temperature": 0.0, "avg_logprob":
  -0.16611063591787747, "compression_ratio": 1.7925925925925925, "no_speech_prob":
  0.0009586364612914622}, {"id": 350, "seek": 209518, "start": 2100.94, "end": 2105.02,
  "text": " so it''s definitely like some things to but that approximate nearest neighbor
  search and I know that", "tokens": [50652, 370, 309, 311, 2138, 411, 512, 721, 281,
  457, 300, 30874, 23831, 5987, 3164, 293, 286, 458, 300, 50856], "temperature": 0.0,
  "avg_logprob": -0.16611063591787747, "compression_ratio": 1.7925925925925925, "no_speech_prob":
  0.0009586364612914622}, {"id": 351, "seek": 209518, "start": 2105.02, "end": 2108.7,
  "text": " you have this experience with you know I''ve listened to a ton of your
  talks and you''re you", "tokens": [50856, 291, 362, 341, 1752, 365, 291, 458, 286,
  600, 13207, 281, 257, 2952, 295, 428, 6686, 293, 291, 434, 291, 51040], "temperature":
  0.0, "avg_logprob": -0.16611063591787747, "compression_ratio": 1.7925925925925925,
  "no_speech_prob": 0.0009586364612914622}, {"id": 352, "seek": 209518, "start": 2108.7,
  "end": 2118.62, "text": " introduced me to the a and n benchmarks but yeah that
  I see that there is being like three levels", "tokens": [51040, 7268, 385, 281,
  264, 257, 293, 297, 43751, 457, 1338, 300, 286, 536, 300, 456, 307, 885, 411, 1045,
  4358, 51536], "temperature": 0.0, "avg_logprob": -0.16611063591787747, "compression_ratio":
  1.7925925925925925, "no_speech_prob": 0.0009586364612914622}, {"id": 353, "seek":
  209518, "start": 2118.62, "end": 2124.7, "text": " of errors that come that propagate
  up there''s the errors from hnsw and say product quantization", "tokens": [51536,
  295, 13603, 300, 808, 300, 48256, 493, 456, 311, 264, 13603, 490, 276, 3695, 86,
  293, 584, 1674, 4426, 2144, 51840], "temperature": 0.0, "avg_logprob": -0.16611063591787747,
  "compression_ratio": 1.7925925925925925, "no_speech_prob": 0.0009586364612914622},
  {"id": 354, "seek": 212518, "start": 2125.58, "end": 2129.8999999999996, "text":
  " then there''s the errors from the vector representations to begin with and then
  there''s maybe", "tokens": [50384, 550, 456, 311, 264, 13603, 490, 264, 8062, 33358,
  281, 1841, 365, 293, 550, 456, 311, 1310, 50600], "temperature": 0.0, "avg_logprob":
  -0.09709692446984977, "compression_ratio": 1.8113207547169812, "no_speech_prob":
  0.0017972294008359313}, {"id": 355, "seek": 212518, "start": 2129.8999999999996,
  "end": 2134.62, "text": " the errors and like the question answering model so if
  you wanted to have like you know natural", "tokens": [50600, 264, 13603, 293, 411,
  264, 1168, 13430, 2316, 370, 498, 291, 1415, 281, 362, 411, 291, 458, 3303, 50836],
  "temperature": 0.0, "avg_logprob": -0.09709692446984977, "compression_ratio": 1.8113207547169812,
  "no_speech_prob": 0.0017972294008359313}, {"id": 356, "seek": 212518, "start": 2134.62,
  "end": 2139.74, "text": " questions open domain qa you''re looking at like three
  layers of cascading errors that are sort of", "tokens": [50836, 1651, 1269, 9274,
  9505, 64, 291, 434, 1237, 412, 411, 1045, 7914, 295, 3058, 66, 8166, 13603, 300,
  366, 1333, 295, 51092], "temperature": 0.0, "avg_logprob": -0.09709692446984977,
  "compression_ratio": 1.8113207547169812, "no_speech_prob": 0.0017972294008359313},
  {"id": 357, "seek": 212518, "start": 2139.74, "end": 2146.8599999999997, "text":
  " unrelated to each other yeah exactly people really brilliantly that you like and
  I think if I may", "tokens": [51092, 38967, 281, 1184, 661, 1338, 2293, 561, 534,
  8695, 42580, 300, 291, 411, 293, 286, 519, 498, 286, 815, 51448], "temperature":
  0.0, "avg_logprob": -0.09709692446984977, "compression_ratio": 1.8113207547169812,
  "no_speech_prob": 0.0017972294008359313}, {"id": 358, "seek": 212518, "start": 2146.8599999999997,
  "end": 2152.7799999999997, "text": " summarize it you know I anyway to you know
  kind of where this hat of the person who is creating", "tokens": [51448, 20858,
  309, 291, 458, 286, 4033, 281, 291, 458, 733, 295, 689, 341, 2385, 295, 264, 954,
  567, 307, 4084, 51744], "temperature": 0.0, "avg_logprob": -0.09709692446984977,
  "compression_ratio": 1.8113207547169812, "no_speech_prob": 0.0017972294008359313},
  {"id": 359, "seek": 215278, "start": 2153.26, "end": 2157.5, "text": " this doctor
  search pyramid and stuff I''m not the only guy doing this but I keep doing this
  because", "tokens": [50388, 341, 4631, 3164, 25950, 293, 1507, 286, 478, 406, 264,
  787, 2146, 884, 341, 457, 286, 1066, 884, 341, 570, 50600], "temperature": 0.0,
  "avg_logprob": -0.11128556100945723, "compression_ratio": 1.7467248908296944, "no_speech_prob":
  0.005856184288859367}, {"id": 360, "seek": 215278, "start": 2157.5, "end": 2163.6600000000003,
  "text": " it helps me to stay comfortable in the topic and sort of okay I''m looking
  at it from this angle and", "tokens": [50600, 309, 3665, 385, 281, 1754, 4619, 294,
  264, 4829, 293, 1333, 295, 1392, 286, 478, 1237, 412, 309, 490, 341, 5802, 293,
  50908], "temperature": 0.0, "avg_logprob": -0.11128556100945723, "compression_ratio":
  1.7467248908296944, "no_speech_prob": 0.005856184288859367}, {"id": 361, "seek":
  215278, "start": 2163.6600000000003, "end": 2168.46, "text": " if you accept it
  stay with me if you don''t you know you may you may as well augment it or something",
  "tokens": [50908, 498, 291, 3241, 309, 1754, 365, 385, 498, 291, 500, 380, 291,
  458, 291, 815, 291, 815, 382, 731, 29919, 309, 420, 746, 51148], "temperature":
  0.0, "avg_logprob": -0.11128556100945723, "compression_ratio": 1.7467248908296944,
  "no_speech_prob": 0.005856184288859367}, {"id": 362, "seek": 215278, "start": 2168.46,
  "end": 2177.02, "text": " like you did earlier with some levels and you know like
  it''s just you need to accept that uncertainty", "tokens": [51148, 411, 291, 630,
  3071, 365, 512, 4358, 293, 291, 458, 411, 309, 311, 445, 291, 643, 281, 3241, 300,
  15697, 51576], "temperature": 0.0, "avg_logprob": -0.11128556100945723, "compression_ratio":
  1.7467248908296944, "no_speech_prob": 0.005856184288859367}, {"id": 363, "seek":
  217702, "start": 2177.02, "end": 2183.18, "text": " like you explained and also
  that uncertainty that you know like in this can and paper they they", "tokens":
  [50364, 411, 291, 8825, 293, 611, 300, 15697, 300, 291, 458, 411, 294, 341, 393,
  293, 3035, 436, 436, 50672], "temperature": 0.0, "avg_logprob": -0.14449211608531864,
  "compression_ratio": 1.7612612612612613, "no_speech_prob": 0.0013236373197287321},
  {"id": 364, "seek": 217702, "start": 2183.18, "end": 2191.42, "text": " explicitly
  show that in hnsw you may have unreachable nodes and they counted something like
  1000", "tokens": [50672, 20803, 855, 300, 294, 276, 3695, 86, 291, 815, 362, 517,
  16226, 712, 13891, 293, 436, 20150, 746, 411, 9714, 51084], "temperature": 0.0,
  "avg_logprob": -0.14449211608531864, "compression_ratio": 1.7612612612612613, "no_speech_prob":
  0.0013236373197287321}, {"id": 365, "seek": 217702, "start": 2191.42, "end": 2196.38,
  "text": " nodes were completely unreachable from any point in the graph like no
  matter how you search how long", "tokens": [51084, 13891, 645, 2584, 517, 16226,
  712, 490, 604, 935, 294, 264, 4295, 411, 572, 1871, 577, 291, 3164, 577, 938, 51332],
  "temperature": 0.0, "avg_logprob": -0.14449211608531864, "compression_ratio": 1.7612612612612613,
  "no_speech_prob": 0.0013236373197287321}, {"id": 366, "seek": 217702, "start": 2196.38,
  "end": 2202.54, "text": " you search what are the values for your e f and m parameters
  during index construction and search", "tokens": [51332, 291, 3164, 437, 366, 264,
  4190, 337, 428, 308, 283, 293, 275, 9834, 1830, 8186, 6435, 293, 3164, 51640], "temperature":
  0.0, "avg_logprob": -0.14449211608531864, "compression_ratio": 1.7612612612612613,
  "no_speech_prob": 0.0013236373197287321}, {"id": 367, "seek": 220254, "start": 2202.54,
  "end": 2209.74, "text": " you just don''t reach them and and that''s I think that''s
  somewhat similar to the inverted index", "tokens": [50364, 291, 445, 500, 380, 2524,
  552, 293, 293, 300, 311, 286, 519, 300, 311, 8344, 2531, 281, 264, 38969, 8186,
  50724], "temperature": 0.0, "avg_logprob": -0.08930057829076593, "compression_ratio":
  1.7897196261682242, "no_speech_prob": 0.0024230084381997585}, {"id": 368, "seek":
  220254, "start": 2209.74, "end": 2217.5, "text": " search where you have like one
  million uh doc IDs per term how do you know when to stop it''s also", "tokens":
  [50724, 3164, 689, 291, 362, 411, 472, 2459, 2232, 3211, 48212, 680, 1433, 577,
  360, 291, 458, 562, 281, 1590, 309, 311, 611, 51112], "temperature": 0.0, "avg_logprob":
  -0.08930057829076593, "compression_ratio": 1.7897196261682242, "no_speech_prob":
  0.0024230084381997585}, {"id": 369, "seek": 220254, "start": 2217.5, "end": 2223.5,
  "text": " like you may never reach the documents that you should have visited but
  you just deliberately", "tokens": [51112, 411, 291, 815, 1128, 2524, 264, 8512,
  300, 291, 820, 362, 11220, 457, 291, 445, 23506, 51412], "temperature": 0.0, "avg_logprob":
  -0.08930057829076593, "compression_ratio": 1.7897196261682242, "no_speech_prob":
  0.0024230084381997585}, {"id": 370, "seek": 220254, "start": 2223.5, "end": 2229.1,
  "text": " decided to stop you know prematurely because you don''t have time you
  have to you know return the", "tokens": [51412, 3047, 281, 1590, 291, 458, 34877,
  356, 570, 291, 500, 380, 362, 565, 291, 362, 281, 291, 458, 2736, 264, 51692], "temperature":
  0.0, "avg_logprob": -0.08930057829076593, "compression_ratio": 1.7897196261682242,
  "no_speech_prob": 0.0024230084381997585}, {"id": 371, "seek": 222910, "start": 2229.1,
  "end": 2234.46, "text": " documents within night and 10 milliseconds so you have
  to make trade-offs um but they are", "tokens": [50364, 8512, 1951, 1818, 293, 1266,
  34184, 370, 291, 362, 281, 652, 4923, 12, 19231, 1105, 457, 436, 366, 50632], "temperature":
  0.0, "avg_logprob": -0.18803446220629144, "compression_ratio": 1.8611111111111112,
  "no_speech_prob": 0.0033102077431976795}, {"id": 372, "seek": 222910, "start": 2235.1,
  "end": 2240.46, "text": " ordered naturally in in the increasing order of doc IDs
  right they''re not ordered by does", "tokens": [50664, 8866, 8195, 294, 294, 264,
  5662, 1668, 295, 3211, 48212, 558, 436, 434, 406, 8866, 538, 775, 50932], "temperature":
  0.0, "avg_logprob": -0.18803446220629144, "compression_ratio": 1.8611111111111112,
  "no_speech_prob": 0.0033102077431976795}, {"id": 373, "seek": 222910, "start": 2240.46,
  "end": 2245.2599999999998, "text": " this question answer anything does this does
  this document know anything about cats or it just", "tokens": [50932, 341, 1168,
  1867, 1340, 775, 341, 775, 341, 4166, 458, 1340, 466, 11111, 420, 309, 445, 51172],
  "temperature": 0.0, "avg_logprob": -0.18803446220629144, "compression_ratio": 1.8611111111111112,
  "no_speech_prob": 0.0033102077431976795}, {"id": 374, "seek": 222910, "start": 2245.2599999999998,
  "end": 2250.38, "text": " not mentions them and passing you know does this document
  knows anything about tweeter does it", "tokens": [51172, 406, 23844, 552, 293, 8437,
  291, 458, 775, 341, 4166, 3255, 1340, 466, 6986, 2398, 775, 309, 51428], "temperature":
  0.0, "avg_logprob": -0.18803446220629144, "compression_ratio": 1.8611111111111112,
  "no_speech_prob": 0.0033102077431976795}, {"id": 375, "seek": 222910, "start": 2250.38,
  "end": 2256.7, "text": " describe tweeter or just says you know please contact me
  on twitter here is my twitter handle right", "tokens": [51428, 6786, 6986, 2398,
  420, 445, 1619, 291, 458, 1767, 3385, 385, 322, 21439, 510, 307, 452, 21439, 4813,
  558, 51744], "temperature": 0.0, "avg_logprob": -0.18803446220629144, "compression_ratio":
  1.8611111111111112, "no_speech_prob": 0.0033102077431976795}, {"id": 376, "seek":
  225670, "start": 2256.7799999999997, "end": 2263.1, "text": " like complete noise
  uh so so you see what I mean right so like there are I think in both approaches",
  "tokens": [50368, 411, 3566, 5658, 2232, 370, 370, 291, 536, 437, 286, 914, 558,
  370, 411, 456, 366, 286, 519, 294, 1293, 11587, 50684], "temperature": 0.0, "avg_logprob":
  -0.12651849080281086, "compression_ratio": 1.7207207207207207, "no_speech_prob":
  0.005413600243628025}, {"id": 377, "seek": 225670, "start": 2263.1, "end": 2269.5,
  "text": " like on fundamental level on data structure level we deal with this fundamental
  limitations", "tokens": [50684, 411, 322, 8088, 1496, 322, 1412, 3877, 1496, 321,
  2028, 365, 341, 8088, 15705, 51004], "temperature": 0.0, "avg_logprob": -0.12651849080281086,
  "compression_ratio": 1.7207207207207207, "no_speech_prob": 0.005413600243628025},
  {"id": 378, "seek": 225670, "start": 2269.5, "end": 2276.7799999999997, "text":
  " like gravity law like you cannot jump off and and fly to moon or to Mars right
  without additional", "tokens": [51004, 411, 12110, 2101, 411, 291, 2644, 3012, 766,
  293, 293, 3603, 281, 7135, 420, 281, 9692, 558, 1553, 4497, 51368], "temperature":
  0.0, "avg_logprob": -0.12651849080281086, "compression_ratio": 1.7207207207207207,
  "no_speech_prob": 0.005413600243628025}, {"id": 379, "seek": 225670, "start": 2276.7799999999997,
  "end": 2283.02, "text": " like thrust and devices and stuff yeah so do you feel
  the same like does it resonate oh yeah", "tokens": [51368, 411, 24030, 293, 5759,
  293, 1507, 1338, 370, 360, 291, 841, 264, 912, 411, 775, 309, 34285, 1954, 1338,
  51680], "temperature": 0.0, "avg_logprob": -0.12651849080281086, "compression_ratio":
  1.7207207207207207, "no_speech_prob": 0.005413600243628025}, {"id": 380, "seek":
  228302, "start": 2283.02, "end": 2288.3, "text": " well firstly thank you that you
  just explained that concept to me for the first time I''m just", "tokens": [50364,
  731, 27376, 1309, 291, 300, 291, 445, 8825, 300, 3410, 281, 385, 337, 264, 700,
  565, 286, 478, 445, 50628], "temperature": 0.0, "avg_logprob": -0.13358652482339,
  "compression_ratio": 1.8807692307692307, "no_speech_prob": 0.002361142775043845},
  {"id": 381, "seek": 228302, "start": 2288.3, "end": 2294.54, "text": " I''m just
  now alive on the podcast understanding that concept but yeah it''s very it''s very
  cool like", "tokens": [50628, 286, 478, 445, 586, 5465, 322, 264, 7367, 3701, 300,
  3410, 457, 1338, 309, 311, 588, 309, 311, 588, 1627, 411, 50940], "temperature":
  0.0, "avg_logprob": -0.13358652482339, "compression_ratio": 1.8807692307692307,
  "no_speech_prob": 0.002361142775043845}, {"id": 382, "seek": 228302, "start": 2294.54,
  "end": 2301.18, "text": " the um sorting the inverted index to prioritize documents
  maybe by clicks like clicks would be like", "tokens": [50940, 264, 1105, 32411,
  264, 38969, 8186, 281, 25164, 8512, 1310, 538, 18521, 411, 18521, 576, 312, 411,
  51272], "temperature": 0.0, "avg_logprob": -0.13358652482339, "compression_ratio":
  1.8807692307692307, "no_speech_prob": 0.002361142775043845}, {"id": 383, "seek":
  228302, "start": 2301.18, "end": 2306.3, "text": " like the most sensible thing
  if it''s like web pages so to say and you sort the documents and then", "tokens":
  [51272, 411, 264, 881, 25380, 551, 498, 309, 311, 411, 3670, 7183, 370, 281, 584,
  293, 291, 1333, 264, 8512, 293, 550, 51528], "temperature": 0.0, "avg_logprob":
  -0.13358652482339, "compression_ratio": 1.8807692307692307, "no_speech_prob": 0.002361142775043845},
  {"id": 384, "seek": 228302, "start": 2307.18, "end": 2311.98, "text": " you yeah
  you have some kind you could probably calculate how much time you have to search
  and how", "tokens": [51572, 291, 1338, 291, 362, 512, 733, 291, 727, 1391, 8873,
  577, 709, 565, 291, 362, 281, 3164, 293, 577, 51812], "temperature": 0.0, "avg_logprob":
  -0.13358652482339, "compression_ratio": 1.8807692307692307, "no_speech_prob": 0.002361142775043845},
  {"id": 385, "seek": 231198, "start": 2311.98, "end": 2318.62, "text": " much that
  lets you go into the invert index yeah super interesting I I think it''s very interesting
  for", "tokens": [50364, 709, 300, 6653, 291, 352, 666, 264, 33966, 8186, 1338, 1687,
  1880, 286, 286, 519, 309, 311, 588, 1880, 337, 50696], "temperature": 0.0, "avg_logprob":
  -0.14204045523584416, "compression_ratio": 1.8254545454545454, "no_speech_prob":
  0.00039322589873336256}, {"id": 386, "seek": 231198, "start": 2318.62, "end": 2323.82,
  "text": " wevia with the with the hybrid search in the beam 25 index because I I
  know the inverted index has", "tokens": [50696, 321, 11617, 365, 264, 365, 264,
  13051, 3164, 294, 264, 14269, 3552, 8186, 570, 286, 286, 458, 264, 38969, 8186,
  575, 50956], "temperature": 0.0, "avg_logprob": -0.14204045523584416, "compression_ratio":
  1.8254545454545454, "no_speech_prob": 0.00039322589873336256}, {"id": 387, "seek":
  231198, "start": 2323.82, "end": 2329.42, "text": " been explored because we have
  this uh like neuro symbolic search where you would annotate properties", "tokens":
  [50956, 668, 24016, 570, 321, 362, 341, 2232, 411, 16499, 25755, 3164, 689, 291,
  576, 25339, 473, 7221, 51236], "temperature": 0.0, "avg_logprob": -0.14204045523584416,
  "compression_ratio": 1.8254545454545454, "no_speech_prob": 0.00039322589873336256},
  {"id": 388, "seek": 231198, "start": 2329.42, "end": 2334.7, "text": " like you
  you''re searching through let''s say you have a billion sneaker images but you''ve
  also labeled", "tokens": [51236, 411, 291, 291, 434, 10808, 807, 718, 311, 584,
  291, 362, 257, 5218, 9244, 4003, 5267, 457, 291, 600, 611, 21335, 51500], "temperature":
  0.0, "avg_logprob": -0.14204045523584416, "compression_ratio": 1.8254545454545454,
  "no_speech_prob": 0.00039322589873336256}, {"id": 389, "seek": 231198, "start":
  2335.26, "end": 2341.1, "text": " the color they are so you have red is the color
  and then you can use that to filter the search so", "tokens": [51528, 264, 2017,
  436, 366, 370, 291, 362, 2182, 307, 264, 2017, 293, 550, 291, 393, 764, 300, 281,
  6608, 264, 3164, 370, 51820], "temperature": 0.0, "avg_logprob": -0.14204045523584416,
  "compression_ratio": 1.8254545454545454, "no_speech_prob": 0.00039322589873336256},
  {"id": 390, "seek": 234110, "start": 2341.1, "end": 2346.2999999999997, "text":
  " there''s definitely been some foundation in pre filtering and integrating uh these
  kind of symbolic", "tokens": [50364, 456, 311, 2138, 668, 512, 7030, 294, 659, 30822,
  293, 26889, 2232, 613, 733, 295, 25755, 50624], "temperature": 0.0, "avg_logprob":
  -0.16630622796845018, "compression_ratio": 1.719298245614035, "no_speech_prob":
  0.0005538312834687531}, {"id": 391, "seek": 234110, "start": 2346.2999999999997,
  "end": 2350.86, "text": " inverted indexes with h and s w so it''s not like the
  first time we''ve yet it''s ever exploring that", "tokens": [50624, 38969, 8186,
  279, 365, 276, 293, 262, 261, 370, 309, 311, 406, 411, 264, 700, 565, 321, 600,
  1939, 309, 311, 1562, 12736, 300, 50852], "temperature": 0.0, "avg_logprob": -0.16630622796845018,
  "compression_ratio": 1.719298245614035, "no_speech_prob": 0.0005538312834687531},
  {"id": 392, "seek": 234110, "start": 2350.86, "end": 2356.7799999999997, "text":
  " but I yeah there''s definitely nuances with the beam 25 because of the cardinality
  of how many terms", "tokens": [50852, 457, 286, 1338, 456, 311, 2138, 38775, 365,
  264, 14269, 3552, 570, 295, 264, 2920, 259, 1860, 295, 577, 867, 2115, 51148], "temperature":
  0.0, "avg_logprob": -0.16630622796845018, "compression_ratio": 1.719298245614035,
  "no_speech_prob": 0.0005538312834687531}, {"id": 393, "seek": 234110, "start": 2356.7799999999997,
  "end": 2362.22, "text": " you like with the document I think you''re splitting it
  I don''t know 300 words right like 300", "tokens": [51148, 291, 411, 365, 264, 4166,
  286, 519, 291, 434, 30348, 309, 286, 500, 380, 458, 6641, 2283, 558, 411, 6641,
  51420], "temperature": 0.0, "avg_logprob": -0.16630622796845018, "compression_ratio":
  1.719298245614035, "no_speech_prob": 0.0005538312834687531}, {"id": 394, "seek":
  234110, "start": 2362.22, "end": 2369.1, "text": " 300 words per property so the
  just the size of it um I mean starting to go into the thinking around", "tokens":
  [51420, 6641, 2283, 680, 4707, 370, 264, 445, 264, 2744, 295, 309, 1105, 286, 914,
  2891, 281, 352, 666, 264, 1953, 926, 51764], "temperature": 0.0, "avg_logprob":
  -0.16630622796845018, "compression_ratio": 1.719298245614035, "no_speech_prob":
  0.0005538312834687531}, {"id": 395, "seek": 236910, "start": 2369.1, "end": 2373.66,
  "text": " like the sizes of things it inspired me when when you''re mentioning the
  compression bottleneck from", "tokens": [50364, 411, 264, 11602, 295, 721, 309,
  7547, 385, 562, 562, 291, 434, 18315, 264, 19355, 44641, 547, 490, 50592], "temperature":
  0.0, "avg_logprob": -0.1977031628290812, "compression_ratio": 1.6629213483146068,
  "no_speech_prob": 0.0011094966903328896}, {"id": 396, "seek": 236910, "start": 2373.66,
  "end": 2380.06, "text": " sparse to dense I was thinking like okay let''s say we
  have 384 dimensional vectors that have 32 bits", "tokens": [50592, 637, 11668, 281,
  18011, 286, 390, 1953, 411, 1392, 718, 311, 584, 321, 362, 12843, 19, 18795, 18875,
  300, 362, 8858, 9239, 50912], "temperature": 0.0, "avg_logprob": -0.1977031628290812,
  "compression_ratio": 1.6629213483146068, "no_speech_prob": 0.0011094966903328896},
  {"id": 397, "seek": 236910, "start": 2380.06, "end": 2391.02, "text": " per uh vector
  position like what is that is that is that 384 or 324 or 32 or you know like that",
  "tokens": [50912, 680, 2232, 8062, 2535, 411, 437, 307, 300, 307, 300, 307, 300,
  12843, 19, 420, 8858, 19, 420, 8858, 420, 291, 458, 411, 300, 51460], "temperature":
  0.0, "avg_logprob": -0.1977031628290812, "compression_ratio": 1.6629213483146068,
  "no_speech_prob": 0.0011094966903328896}, {"id": 398, "seek": 239102, "start": 2391.1,
  "end": 2399.5, "text": " it''s still a massive common tutorial space right yes exactly
  exactly and and and you said like", "tokens": [50368, 309, 311, 920, 257, 5994,
  2689, 7073, 1901, 558, 2086, 2293, 2293, 293, 293, 293, 291, 848, 411, 50788], "temperature":
  0.0, "avg_logprob": -0.17165842721628588, "compression_ratio": 1.768181818181818,
  "no_speech_prob": 0.0045879557728767395}, {"id": 399, "seek": 239102, "start": 2399.5,
  "end": 2405.82, "text": " is it even the model that captures everything we need
  to capture right it in all of these are numbers", "tokens": [50788, 307, 309, 754,
  264, 2316, 300, 27986, 1203, 321, 643, 281, 7983, 558, 309, 294, 439, 295, 613,
  366, 3547, 51104], "temperature": 0.0, "avg_logprob": -0.17165842721628588, "compression_ratio":
  1.768181818181818, "no_speech_prob": 0.0045879557728767395}, {"id": 400, "seek":
  239102, "start": 2405.82, "end": 2411.1, "text": " of course it''s kind of number
  representation of the models understanding well understanding in", "tokens": [51104,
  295, 1164, 309, 311, 733, 295, 1230, 10290, 295, 264, 5245, 3701, 731, 3701, 294,
  51368], "temperature": 0.0, "avg_logprob": -0.17165842721628588, "compression_ratio":
  1.768181818181818, "no_speech_prob": 0.0045879557728767395}, {"id": 401, "seek":
  239102, "start": 2411.1, "end": 2419.18, "text": " quotes of of the objects that
  we index uh but I guess like for me like um and you''re way ahead in", "tokens":
  [51368, 19963, 295, 295, 264, 6565, 300, 321, 8186, 2232, 457, 286, 2041, 411, 337,
  385, 411, 1105, 293, 291, 434, 636, 2286, 294, 51772], "temperature": 0.0, "avg_logprob":
  -0.17165842721628588, "compression_ratio": 1.768181818181818, "no_speech_prob":
  0.0045879557728767395}, {"id": 402, "seek": 241918, "start": 2419.18, "end": 2427.2599999999998,
  "text": " this I feel like that uh with VBA development like um of me you know what
  matters to me when I was", "tokens": [50364, 341, 286, 841, 411, 300, 2232, 365,
  691, 9295, 3250, 411, 1105, 295, 385, 291, 458, 437, 7001, 281, 385, 562, 286, 390,
  50768], "temperature": 0.0, "avg_logprob": -0.09768871684650798, "compression_ratio":
  1.6694214876033058, "no_speech_prob": 0.0009292639442719519}, {"id": 403, "seek":
  241918, "start": 2427.2599999999998, "end": 2434.3799999999997, "text": " like a
  search engineer day to day is what tools not necessarily tools as in specific programs
  but like", "tokens": [50768, 411, 257, 3164, 11403, 786, 281, 786, 307, 437, 3873,
  406, 4725, 3873, 382, 294, 2685, 4268, 457, 411, 51124], "temperature": 0.0, "avg_logprob":
  -0.09768871684650798, "compression_ratio": 1.6694214876033058, "no_speech_prob":
  0.0009292639442719519}, {"id": 404, "seek": 241918, "start": 2434.3799999999997,
  "end": 2441.74, "text": " tools as in algorithms approaches I have to control the
  process right so if somebody comes up and says", "tokens": [51124, 3873, 382, 294,
  14642, 11587, 286, 362, 281, 1969, 264, 1399, 558, 370, 498, 2618, 1487, 493, 293,
  1619, 51492], "temperature": 0.0, "avg_logprob": -0.09768871684650798, "compression_ratio":
  1.6694214876033058, "no_speech_prob": 0.0009292639442719519}, {"id": 405, "seek":
  241918, "start": 2441.74, "end": 2447.4199999999996, "text": " hey can you look
  in this query can you debug it first of all like explain queries one brilliant way",
  "tokens": [51492, 4177, 393, 291, 574, 294, 341, 14581, 393, 291, 24083, 309, 700,
  295, 439, 411, 2903, 24109, 472, 10248, 636, 51776], "temperature": 0.0, "avg_logprob":
  -0.09768871684650798, "compression_ratio": 1.6694214876033058, "no_speech_prob":
  0.0009292639442719519}, {"id": 406, "seek": 244742, "start": 2447.58, "end": 2452.3,
  "text": " of doing it and that''s where you start but then once you understood aha
  there is a problem that it", "tokens": [50372, 295, 884, 309, 293, 300, 311, 689,
  291, 722, 457, 550, 1564, 291, 7320, 47340, 456, 307, 257, 1154, 300, 309, 50608],
  "temperature": 0.0, "avg_logprob": -0.09644802411397298, "compression_ratio": 1.7234042553191489,
  "no_speech_prob": 0.0033991020172834396}, {"id": 407, "seek": 244742, "start": 2452.3,
  "end": 2459.26, "text": " hits this field or I give too much of a boost uh in this
  situation what should I do so you start like", "tokens": [50608, 8664, 341, 2519,
  420, 286, 976, 886, 709, 295, 257, 9194, 2232, 294, 341, 2590, 437, 820, 286, 360,
  370, 291, 722, 411, 50956], "temperature": 0.0, "avg_logprob": -0.09644802411397298,
  "compression_ratio": 1.7234042553191489, "no_speech_prob": 0.0033991020172834396},
  {"id": 408, "seek": 244742, "start": 2459.26, "end": 2464.54, "text": " tweaking
  these parameters and you have these tools in your hands right you can do that in
  vector search", "tokens": [50956, 6986, 2456, 613, 9834, 293, 291, 362, 613, 3873,
  294, 428, 2377, 558, 291, 393, 360, 300, 294, 8062, 3164, 51220], "temperature":
  0.0, "avg_logprob": -0.09644802411397298, "compression_ratio": 1.7234042553191489,
  "no_speech_prob": 0.0033991020172834396}, {"id": 409, "seek": 244742, "start": 2464.54,
  "end": 2470.62, "text": " I I don''t know like I have like probably fine tuning
  as one tool right so like if clip stops working", "tokens": [51220, 286, 286, 500,
  380, 458, 411, 286, 362, 411, 1391, 2489, 15164, 382, 472, 2290, 558, 370, 411,
  498, 7353, 10094, 1364, 51524], "temperature": 0.0, "avg_logprob": -0.09644802411397298,
  "compression_ratio": 1.7234042553191489, "no_speech_prob": 0.0033991020172834396},
  {"id": 410, "seek": 247062, "start": 2470.7, "end": 2478.8599999999997, "text":
  " on these images I can go and fine tune or bird um but what else do I have like
  I can also tune some", "tokens": [50368, 322, 613, 5267, 286, 393, 352, 293, 2489,
  10864, 420, 5255, 1105, 457, 437, 1646, 360, 286, 362, 411, 286, 393, 611, 10864,
  512, 50776], "temperature": 0.0, "avg_logprob": -0.19422662024404488, "compression_ratio":
  1.7117903930131004, "no_speech_prob": 0.0026084675919264555}, {"id": 411, "seek":
  247062, "start": 2478.8599999999997, "end": 2485.5, "text": " parameters in hnsw
  or gskn and so or something I can make all these thousand nodes reachable like",
  "tokens": [50776, 9834, 294, 276, 77, 82, 86, 420, 290, 5161, 77, 293, 370, 420,
  746, 286, 393, 652, 439, 613, 4714, 13891, 2524, 712, 411, 51108], "temperature":
  0.0, "avg_logprob": -0.19422662024404488, "compression_ratio": 1.7117903930131004,
  "no_speech_prob": 0.0026084675919264555}, {"id": 412, "seek": 247062, "start": 2485.5,
  "end": 2492.94, "text": " they didn''t this can and I can choose disk over RAM if
  I want to save on you know on cost and stuff", "tokens": [51108, 436, 994, 380,
  341, 393, 293, 286, 393, 2826, 12355, 670, 14561, 498, 286, 528, 281, 3155, 322,
  291, 458, 322, 2063, 293, 1507, 51480], "temperature": 0.0, "avg_logprob": -0.19422662024404488,
  "compression_ratio": 1.7117903930131004, "no_speech_prob": 0.0026084675919264555},
  {"id": 413, "seek": 247062, "start": 2492.94, "end": 2499.66, "text": " but what
  else do I have as a control to actually go and debug and fix that specific query
  like", "tokens": [51480, 457, 437, 1646, 360, 286, 362, 382, 257, 1969, 281, 767,
  352, 293, 24083, 293, 3191, 300, 2685, 14581, 411, 51816], "temperature": 0.0, "avg_logprob":
  -0.19422662024404488, "compression_ratio": 1.7117903930131004, "no_speech_prob":
  0.0026084675919264555}, {"id": 414, "seek": 249966, "start": 2499.8199999999997,
  "end": 2507.74, "text": " what has been your experience on that or maybe thinking
  uh yeah I think you''ve named them all", "tokens": [50372, 437, 575, 668, 428, 1752,
  322, 300, 420, 1310, 1953, 2232, 1338, 286, 519, 291, 600, 4926, 552, 439, 50768],
  "temperature": 0.0, "avg_logprob": -0.14236458672417535, "compression_ratio": 1.6578947368421053,
  "no_speech_prob": 0.0008320417255163193}, {"id": 415, "seek": 249966, "start": 2510.62,
  "end": 2518.94, "text": " I mean I know I''ve seen like um like the tuning of the
  EF construction as you mentioned with hnsw and", "tokens": [50912, 286, 914, 286,
  458, 286, 600, 1612, 411, 1105, 411, 264, 15164, 295, 264, 462, 37, 6435, 382, 291,
  2835, 365, 276, 77, 82, 86, 293, 51328], "temperature": 0.0, "avg_logprob": -0.14236458672417535,
  "compression_ratio": 1.6578947368421053, "no_speech_prob": 0.0008320417255163193},
  {"id": 416, "seek": 249966, "start": 2518.94, "end": 2522.8599999999997, "text":
  " I guess something that I''m really excited about with these beer benchmarks and
  maybe I can", "tokens": [51328, 286, 2041, 746, 300, 286, 478, 534, 2919, 466, 365,
  613, 8795, 43751, 293, 1310, 286, 393, 51524], "temperature": 0.0, "avg_logprob":
  -0.14236458672417535, "compression_ratio": 1.6578947368421053, "no_speech_prob":
  0.0008320417255163193}, {"id": 417, "seek": 249966, "start": 2522.8599999999997,
  "end": 2526.94, "text": " introduce it now because I think it helps with this idea
  of model selection in terms of the", "tokens": [51524, 5366, 309, 586, 570, 286,
  519, 309, 3665, 365, 341, 1558, 295, 2316, 9450, 294, 2115, 295, 264, 51728], "temperature":
  0.0, "avg_logprob": -0.14236458672417535, "compression_ratio": 1.6578947368421053,
  "no_speech_prob": 0.0008320417255163193}, {"id": 418, "seek": 252694, "start": 2526.94,
  "end": 2531.7400000000002, "text": " user''s perspective on how can I debug my system
  how do I fix my search system so the beer", "tokens": [50364, 4195, 311, 4585, 322,
  577, 393, 286, 24083, 452, 1185, 577, 360, 286, 3191, 452, 3164, 1185, 370, 264,
  8795, 50604], "temperature": 0.0, "avg_logprob": -0.18612978751199288, "compression_ratio":
  1.7715355805243447, "no_speech_prob": 0.0014933764468878508}, {"id": 419, "seek":
  252694, "start": 2531.7400000000002, "end": 2537.18, "text": " benchmarks is it''s
  about diverse text retrieval so you know it''s like arguana NF corpus track", "tokens":
  [50604, 43751, 307, 309, 311, 466, 9521, 2487, 19817, 3337, 370, 291, 458, 309,
  311, 411, 3882, 84, 2095, 13576, 1181, 31624, 2837, 50876], "temperature": 0.0,
  "avg_logprob": -0.18612978751199288, "compression_ratio": 1.7715355805243447, "no_speech_prob":
  0.0014933764468878508}, {"id": 420, "seek": 252694, "start": 2537.18, "end": 2542.54,
  "text": " covid is the difference is instead of saying that the search image net
  is going to be ms marco", "tokens": [50876, 25616, 307, 264, 2649, 307, 2602, 295,
  1566, 300, 264, 3164, 3256, 2533, 307, 516, 281, 312, 275, 82, 1849, 1291, 51144],
  "temperature": 0.0, "avg_logprob": -0.18612978751199288, "compression_ratio": 1.7715355805243447,
  "no_speech_prob": 0.0014933764468878508}, {"id": 421, "seek": 252694, "start": 2542.54,
  "end": 2547.42, "text": " which is you know like 10 million being passages and like
  a million labeled query so it''s like the", "tokens": [51144, 597, 307, 291, 458,
  411, 1266, 2459, 885, 31589, 293, 411, 257, 2459, 21335, 14581, 370, 309, 311, 411,
  264, 51388], "temperature": 0.0, "avg_logprob": -0.18612978751199288, "compression_ratio":
  1.7715355805243447, "no_speech_prob": 0.0014933764468878508}, {"id": 422, "seek":
  252694, "start": 2547.42, "end": 2552.62, "text": " image net idea of like this
  general source of it like image net is like a massive collection of", "tokens":
  [51388, 3256, 2533, 1558, 295, 411, 341, 2674, 4009, 295, 309, 411, 3256, 2533,
  307, 411, 257, 5994, 5765, 295, 51648], "temperature": 0.0, "avg_logprob": -0.18612978751199288,
  "compression_ratio": 1.7715355805243447, "no_speech_prob": 0.0014933764468878508},
  {"id": 423, "seek": 255262, "start": 2552.7, "end": 2558.22, "text": " images labeled
  in a bunch of categories so it''s like it''s like is ms marco the search image net",
  "tokens": [50368, 5267, 21335, 294, 257, 3840, 295, 10479, 370, 309, 311, 411, 309,
  311, 411, 307, 275, 82, 1849, 1291, 264, 3164, 3256, 2533, 50644], "temperature":
  0.0, "avg_logprob": -0.1820291356837496, "compression_ratio": 1.7117117117117118,
  "no_speech_prob": 0.001304032513871789}, {"id": 424, "seek": 255262, "start": 2558.22,
  "end": 2562.94, "text": " but it seems like instead we''re going for diversity with
  beer and I think also if we all if we", "tokens": [50644, 457, 309, 2544, 411, 2602,
  321, 434, 516, 337, 8811, 365, 8795, 293, 286, 519, 611, 498, 321, 439, 498, 321,
  50880], "temperature": 0.0, "avg_logprob": -0.1820291356837496, "compression_ratio":
  1.7117117117117118, "no_speech_prob": 0.001304032513871789}, {"id": 425, "seek":
  255262, "start": 2562.94, "end": 2569.02, "text": " want to talk about intent intents
  and instructions further I think actually beer is I think beer had", "tokens": [50880,
  528, 281, 751, 466, 8446, 560, 791, 293, 9415, 3052, 286, 519, 767, 8795, 307, 286,
  519, 8795, 632, 51184], "temperature": 0.0, "avg_logprob": -0.1820291356837496,
  "compression_ratio": 1.7117117117117118, "no_speech_prob": 0.001304032513871789},
  {"id": 426, "seek": 255262, "start": 2569.02, "end": 2577.74, "text": " another
  there''s latte like L O T T E capital T''s like they go they go beverages right
  so", "tokens": [51184, 1071, 456, 311, 37854, 411, 441, 422, 314, 314, 462, 4238,
  314, 311, 411, 436, 352, 436, 352, 47401, 558, 370, 51620], "temperature": 0.0,
  "avg_logprob": -0.1820291356837496, "compression_ratio": 1.7117117117117118, "no_speech_prob":
  0.001304032513871789}, {"id": 427, "seek": 257774, "start": 2577.8199999999997,
  "end": 2584.7799999999997, "text": " yeah so there''s like an equivalent to beer
  and then there''s also miracle which is for", "tokens": [50368, 1338, 370, 456,
  311, 411, 364, 10344, 281, 8795, 293, 550, 456, 311, 611, 14660, 597, 307, 337,
  50716], "temperature": 0.0, "avg_logprob": -0.10939262531421802, "compression_ratio":
  1.8825910931174088, "no_speech_prob": 0.0031901560723781586}, {"id": 428, "seek":
  257774, "start": 2584.7799999999997, "end": 2589.8999999999996, "text": " multilingual
  so there''s a lot of these like diverse text retrieval and then and then it''s",
  "tokens": [50716, 2120, 38219, 370, 456, 311, 257, 688, 295, 613, 411, 9521, 2487,
  19817, 3337, 293, 550, 293, 550, 309, 311, 50972], "temperature": 0.0, "avg_logprob":
  -0.10939262531421802, "compression_ratio": 1.8825910931174088, "no_speech_prob":
  0.0031901560723781586}, {"id": 429, "seek": 257774, "start": 2589.8999999999996,
  "end": 2594.7, "text": " expanding where you would label it with the instructions
  as well and I don''t remember the names", "tokens": [50972, 14702, 689, 291, 576,
  7645, 309, 365, 264, 9415, 382, 731, 293, 286, 500, 380, 1604, 264, 5288, 51212],
  "temperature": 0.0, "avg_logprob": -0.10939262531421802, "compression_ratio": 1.8825910931174088,
  "no_speech_prob": 0.0031901560723781586}, {"id": 430, "seek": 257774, "start": 2594.7,
  "end": 2598.2999999999997, "text": " of these data sets off the top of my head because
  it''s very new but I know this paper called task", "tokens": [51212, 295, 613, 1412,
  6352, 766, 264, 1192, 295, 452, 1378, 570, 309, 311, 588, 777, 457, 286, 458, 341,
  3035, 1219, 5633, 51392], "temperature": 0.0, "avg_logprob": -0.10939262531421802,
  "compression_ratio": 1.8825910931174088, "no_speech_prob": 0.0031901560723781586},
  {"id": 431, "seek": 257774, "start": 2598.2999999999997, "end": 2602.8599999999997,
  "text": " aware retrieval with instructions and I think there''s a model another
  paper with a model called", "tokens": [51392, 3650, 19817, 3337, 365, 9415, 293,
  286, 519, 456, 311, 257, 2316, 1071, 3035, 365, 257, 2316, 1219, 51620], "temperature":
  0.0, "avg_logprob": -0.10939262531421802, "compression_ratio": 1.8825910931174088,
  "no_speech_prob": 0.0031901560723781586}, {"id": 432, "seek": 260286, "start": 2602.86,
  "end": 2607.6600000000003, "text": " instructor so this is idea where you also label
  with the intent but but anyways let me go back", "tokens": [50364, 18499, 370, 341,
  307, 1558, 689, 291, 611, 7645, 365, 264, 8446, 457, 457, 13448, 718, 385, 352,
  646, 50604], "temperature": 0.0, "avg_logprob": -0.11106062293948984, "compression_ratio":
  1.9266666666666667, "no_speech_prob": 0.007401135750114918}, {"id": 433, "seek":
  260286, "start": 2607.6600000000003, "end": 2612.46, "text": " to the focus on like
  how does a user debug the search system and say how can I fix it so the idea", "tokens":
  [50604, 281, 264, 1879, 322, 411, 577, 775, 257, 4195, 24083, 264, 3164, 1185, 293,
  584, 577, 393, 286, 3191, 309, 370, 264, 1558, 50844], "temperature": 0.0, "avg_logprob":
  -0.11106062293948984, "compression_ratio": 1.9266666666666667, "no_speech_prob":
  0.007401135750114918}, {"id": 434, "seek": 260286, "start": 2612.46, "end": 2616.86,
  "text": " with the beer benchmarks like one idea would be that we could test several
  different models and you", "tokens": [50844, 365, 264, 8795, 43751, 411, 472, 1558,
  576, 312, 300, 321, 727, 1500, 2940, 819, 5245, 293, 291, 51064], "temperature":
  0.0, "avg_logprob": -0.11106062293948984, "compression_ratio": 1.9266666666666667,
  "no_speech_prob": 0.007401135750114918}, {"id": 435, "seek": 260286, "start": 2616.86,
  "end": 2622.7000000000003, "text": " could maybe say like okay well I''m building
  a nutrition I''m building a nutrition search apps I''m", "tokens": [51064, 727,
  1310, 584, 411, 1392, 731, 286, 478, 2390, 257, 14718, 286, 478, 2390, 257, 14718,
  3164, 7733, 286, 478, 51356], "temperature": 0.0, "avg_logprob": -0.11106062293948984,
  "compression_ratio": 1.9266666666666667, "no_speech_prob": 0.007401135750114918},
  {"id": 436, "seek": 260286, "start": 2622.7000000000003, "end": 2627.26, "text":
  " like I''m like bodybuilding.com or something like that and so you would look at
  the NF corpus", "tokens": [51356, 411, 286, 478, 411, 1772, 28126, 13, 1112, 420,
  746, 411, 300, 293, 370, 291, 576, 574, 412, 264, 13576, 1181, 31624, 51584], "temperature":
  0.0, "avg_logprob": -0.11106062293948984, "compression_ratio": 1.9266666666666667,
  "no_speech_prob": 0.007401135750114918}, {"id": 437, "seek": 260286, "start": 2628.06,
  "end": 2631.5, "text": " results and you would see the performance of the different
  models and that would maybe help you", "tokens": [51624, 3542, 293, 291, 576, 536,
  264, 3389, 295, 264, 819, 5245, 293, 300, 576, 1310, 854, 291, 51796], "temperature":
  0.0, "avg_logprob": -0.11106062293948984, "compression_ratio": 1.9266666666666667,
  "no_speech_prob": 0.007401135750114918}, {"id": 438, "seek": 263150, "start": 2631.5,
  "end": 2637.42, "text": " take a different model off the shelf but then what you''re
  saying with like fine tuning it I suspect", "tokens": [50364, 747, 257, 819, 2316,
  766, 264, 15222, 457, 550, 437, 291, 434, 1566, 365, 411, 2489, 15164, 309, 286,
  9091, 50660], "temperature": 0.0, "avg_logprob": -0.1886826145405672, "compression_ratio":
  1.6752136752136753, "no_speech_prob": 0.0004842080525122583}, {"id": 439, "seek":
  263150, "start": 2637.42, "end": 2643.58, "text": " that fine tuning is going to
  be a super powerful lever I think if you find like and maybe later", "tokens": [50660,
  300, 2489, 15164, 307, 516, 281, 312, 257, 1687, 4005, 12451, 286, 519, 498, 291,
  915, 411, 293, 1310, 1780, 50968], "temperature": 0.0, "avg_logprob": -0.1886826145405672,
  "compression_ratio": 1.6752136752136753, "no_speech_prob": 0.0004842080525122583},
  {"id": 440, "seek": 263150, "start": 2645.34, "end": 2652.14, "text": " there''s
  so many topics I want to talk to you about. Like with the idea of I''ve been building
  a", "tokens": [51056, 456, 311, 370, 867, 8378, 286, 528, 281, 751, 281, 291, 466,
  13, 1743, 365, 264, 1558, 295, 286, 600, 668, 2390, 257, 51396], "temperature":
  0.0, "avg_logprob": -0.1886826145405672, "compression_ratio": 1.6752136752136753,
  "no_speech_prob": 0.0004842080525122583}, {"id": 441, "seek": 263150, "start": 2652.14,
  "end": 2656.86, "text": " Wevey-A demo of the podcast search so I''ve been taking
  the Wevey-A podcast parsing the transcriptions", "tokens": [51396, 492, 5603, 12,
  32, 10723, 295, 264, 7367, 3164, 370, 286, 600, 668, 1940, 264, 492, 5603, 12, 32,
  7367, 21156, 278, 264, 24444, 626, 51632], "temperature": 0.0, "avg_logprob": -0.1886826145405672,
  "compression_ratio": 1.6752136752136753, "no_speech_prob": 0.0004842080525122583},
  {"id": 442, "seek": 265686, "start": 2656.86, "end": 2662.7000000000003, "text":
  " and putting them in there in my temptation to like fine tune it and start thinking
  about this", "tokens": [50364, 293, 3372, 552, 294, 456, 294, 452, 30423, 281, 411,
  2489, 10864, 309, 293, 722, 1953, 466, 341, 50656], "temperature": 0.0, "avg_logprob":
  -0.14244754757501382, "compression_ratio": 1.7818181818181817, "no_speech_prob":
  0.0026202411390841007}, {"id": 443, "seek": 265686, "start": 2663.34, "end": 2668.94,
  "text": " positive negative construction for that I mean I think in general with
  Wevey-A we''re kind of you", "tokens": [50688, 3353, 3671, 6435, 337, 300, 286,
  914, 286, 519, 294, 2674, 365, 492, 5603, 12, 32, 321, 434, 733, 295, 291, 50968],
  "temperature": 0.0, "avg_logprob": -0.14244754757501382, "compression_ratio": 1.7818181818181817,
  "no_speech_prob": 0.0026202411390841007}, {"id": 444, "seek": 265686, "start": 2668.94,
  "end": 2675.02, "text": " know letting like you know we use open AI models co-hear
  models, hugging face models and it''s like", "tokens": [50968, 458, 8295, 411, 291,
  458, 321, 764, 1269, 7318, 5245, 598, 12, 675, 289, 5245, 11, 41706, 1851, 5245,
  293, 309, 311, 411, 51272], "temperature": 0.0, "avg_logprob": -0.14244754757501382,
  "compression_ratio": 1.7818181818181817, "no_speech_prob": 0.0026202411390841007},
  {"id": 445, "seek": 265686, "start": 2675.02, "end": 2679.82, "text": " we''re not
  really training the models but it''s just such an interesting thing to tune I know
  Gina AI''s", "tokens": [51272, 321, 434, 406, 534, 3097, 264, 5245, 457, 309, 311,
  445, 1270, 364, 1880, 551, 281, 10864, 286, 458, 34711, 7318, 311, 51512], "temperature":
  0.0, "avg_logprob": -0.14244754757501382, "compression_ratio": 1.7818181818181817,
  "no_speech_prob": 0.0026202411390841007}, {"id": 446, "seek": 265686, "start": 2679.82,
  "end": 2685.26, "text": " fine tuner is extremely interesting that I do find myself
  like constantly pulled in that direction", "tokens": [51512, 2489, 4267, 260, 307,
  4664, 1880, 300, 286, 360, 915, 2059, 411, 6460, 7373, 294, 300, 3513, 51784], "temperature":
  0.0, "avg_logprob": -0.14244754757501382, "compression_ratio": 1.7818181818181817,
  "no_speech_prob": 0.0026202411390841007}, {"id": 447, "seek": 268526, "start": 2685.26,
  "end": 2692.5400000000004, "text": " of like wanting to train models. Yeah absolutely
  I''ve been when we when we presented Mewves", "tokens": [50364, 295, 411, 7935,
  281, 3847, 5245, 13, 865, 3122, 286, 600, 668, 562, 321, 562, 321, 8212, 376, 1023,
  977, 50728], "temperature": 0.0, "avg_logprob": -0.20249184141767787, "compression_ratio":
  1.6379310344827587, "no_speech_prob": 0.002138295443728566}, {"id": 448, "seek":
  268526, "start": 2692.5400000000004, "end": 2699.1000000000004, "text": " at Berlin
  Buzzwords last year now we actually said we also have Mewver which is the component
  to", "tokens": [50728, 412, 13848, 29209, 13832, 1036, 1064, 586, 321, 767, 848,
  321, 611, 362, 376, 1023, 331, 597, 307, 264, 6542, 281, 51056], "temperature":
  0.0, "avg_logprob": -0.20249184141767787, "compression_ratio": 1.6379310344827587,
  "no_speech_prob": 0.002138295443728566}, {"id": 449, "seek": 268526, "start": 2699.7400000000002,
  "end": 2705.1800000000003, "text": " allowing you to fine tune a model we kind of
  like don''t have it for prime time but I''ve been like", "tokens": [51088, 8293,
  291, 281, 2489, 10864, 257, 2316, 321, 733, 295, 411, 500, 380, 362, 309, 337, 5835,
  565, 457, 286, 600, 668, 411, 51360], "temperature": 0.0, "avg_logprob": -0.20249184141767787,
  "compression_ratio": 1.6379310344827587, "no_speech_prob": 0.002138295443728566},
  {"id": 450, "seek": 268526, "start": 2705.1800000000003, "end": 2711.5800000000004,
  "text": " really fascinated kind of coding a bit of that and and checking how well
  it can can work in a", "tokens": [51360, 534, 24597, 733, 295, 17720, 257, 857,
  295, 300, 293, 293, 8568, 577, 731, 309, 393, 393, 589, 294, 257, 51680], "temperature":
  0.0, "avg_logprob": -0.20249184141767787, "compression_ratio": 1.6379310344827587,
  "no_speech_prob": 0.002138295443728566}, {"id": 451, "seek": 271158, "start": 2711.58,
  "end": 2719.66, "text": " more generic way you know because I think fine tuner allows
  you to plug in several models you know", "tokens": [50364, 544, 19577, 636, 291,
  458, 570, 286, 519, 2489, 4267, 260, 4045, 291, 281, 5452, 294, 2940, 5245, 291,
  458, 50768], "temperature": 0.0, "avg_logprob": -0.13279383669617356, "compression_ratio":
  1.8679245283018868, "no_speech_prob": 0.0018931633094325662}, {"id": 452, "seek":
  271158, "start": 2719.66, "end": 2724.94, "text": " and like because different models
  have different inputs they have different like setting to train", "tokens": [50768,
  293, 411, 570, 819, 5245, 362, 819, 15743, 436, 362, 819, 411, 3287, 281, 3847,
  51032], "temperature": 0.0, "avg_logprob": -0.13279383669617356, "compression_ratio":
  1.8679245283018868, "no_speech_prob": 0.0018931633094325662}, {"id": 453, "seek":
  271158, "start": 2724.94, "end": 2730.2999999999997, "text": " and fine tune and
  so you need to be aware of that like Clip is that is a kind of two tower in a way",
  "tokens": [51032, 293, 2489, 10864, 293, 370, 291, 643, 281, 312, 3650, 295, 300,
  411, 2033, 647, 307, 300, 307, 257, 733, 295, 732, 10567, 294, 257, 636, 51300],
  "temperature": 0.0, "avg_logprob": -0.13279383669617356, "compression_ratio": 1.8679245283018868,
  "no_speech_prob": 0.0018931633094325662}, {"id": 454, "seek": 271158, "start": 2730.2999999999997,
  "end": 2739.18, "text": " right so you do need text you do need the image but I
  think I feel like coming back to the question", "tokens": [51300, 558, 370, 291,
  360, 643, 2487, 291, 360, 643, 264, 3256, 457, 286, 519, 286, 841, 411, 1348, 646,
  281, 264, 1168, 51744], "temperature": 0.0, "avg_logprob": -0.13279383669617356,
  "compression_ratio": 1.8679245283018868, "no_speech_prob": 0.0018931633094325662},
  {"id": 455, "seek": 273918, "start": 2739.2599999999998, "end": 2744.54, "text":
  " like what tools I have I feel like fine tuning and I feel like you agree to that
  the fine tuning is", "tokens": [50368, 411, 437, 3873, 286, 362, 286, 841, 411,
  2489, 15164, 293, 286, 841, 411, 291, 3986, 281, 300, 264, 2489, 15164, 307, 50632],
  "temperature": 0.0, "avg_logprob": -0.08822442094484965, "compression_ratio": 1.9704433497536946,
  "no_speech_prob": 0.00464021647349}, {"id": 456, "seek": 273918, "start": 2744.54,
  "end": 2751.98, "text": " one way that should be more available to the masses should
  be more available to the users in a way", "tokens": [50632, 472, 636, 300, 820,
  312, 544, 2435, 281, 264, 23935, 820, 312, 544, 2435, 281, 264, 5022, 294, 257,
  636, 51004], "temperature": 0.0, "avg_logprob": -0.08822442094484965, "compression_ratio":
  1.9704433497536946, "no_speech_prob": 0.00464021647349}, {"id": 457, "seek": 273918,
  "start": 2751.98, "end": 2759.98, "text": " that they are aware of this tool and
  they know you know best sort of like know how how to use them", "tokens": [51004,
  300, 436, 366, 3650, 295, 341, 2290, 293, 436, 458, 291, 458, 1151, 1333, 295, 411,
  458, 577, 577, 281, 764, 552, 51404], "temperature": 0.0, "avg_logprob": -0.08822442094484965,
  "compression_ratio": 1.9704433497536946, "no_speech_prob": 0.00464021647349}, {"id":
  458, "seek": 273918, "start": 2759.98, "end": 2765.2599999999998, "text": " and
  also pitfalls you may fall into and I think this is what you brilliantly described
  like a year ago", "tokens": [51404, 293, 611, 10147, 18542, 291, 815, 2100, 666,
  293, 286, 519, 341, 307, 437, 291, 8695, 42580, 7619, 411, 257, 1064, 2057, 51668],
  "temperature": 0.0, "avg_logprob": -0.08822442094484965, "compression_ratio": 1.9704433497536946,
  "no_speech_prob": 0.00464021647349}, {"id": 459, "seek": 276526, "start": 2765.42,
  "end": 2771.5, "text": " in the context of computer vision like data augmentation
  right so like it''s one thing that you can feed", "tokens": [50372, 294, 264, 4319,
  295, 3820, 5201, 411, 1412, 14501, 19631, 558, 370, 411, 309, 311, 472, 551, 300,
  291, 393, 3154, 50676], "temperature": 0.0, "avg_logprob": -0.09499218820155352,
  "compression_ratio": 1.8254716981132075, "no_speech_prob": 0.004000214394181967},
  {"id": 460, "seek": 276526, "start": 2773.5800000000004, "end": 2779.26, "text":
  " you can feed some manual examples but how far you can go and like in your basketball
  example", "tokens": [50780, 291, 393, 3154, 512, 9688, 5110, 457, 577, 1400, 291,
  393, 352, 293, 411, 294, 428, 11767, 1365, 51064], "temperature": 0.0, "avg_logprob":
  -0.09499218820155352, "compression_ratio": 1.8254716981132075, "no_speech_prob":
  0.004000214394181967}, {"id": 461, "seek": 276526, "start": 2779.26, "end": 2784.38,
  "text": " like you''ve been manually labeling some examples like you run out of
  patience in a way right", "tokens": [51064, 411, 291, 600, 668, 16945, 40244, 512,
  5110, 411, 291, 1190, 484, 295, 14826, 294, 257, 636, 558, 51320], "temperature":
  0.0, "avg_logprob": -0.09499218820155352, "compression_ratio": 1.8254716981132075,
  "no_speech_prob": 0.004000214394181967}, {"id": 462, "seek": 276526, "start": 2784.38,
  "end": 2791.26, "text": " okay you can hire people to do that but is that scalable
  probably not and also new trends come up", "tokens": [51320, 1392, 291, 393, 11158,
  561, 281, 360, 300, 457, 307, 300, 38481, 1391, 406, 293, 611, 777, 13892, 808,
  493, 51664], "temperature": 0.0, "avg_logprob": -0.09499218820155352, "compression_ratio":
  1.8254716981132075, "no_speech_prob": 0.004000214394181967}, {"id": 463, "seek":
  279126, "start": 2791.26, "end": 2796.86, "text": " like if you take a business
  specifically working on e-commerce or I don''t know full text document", "tokens":
  [50364, 411, 498, 291, 747, 257, 1606, 4682, 1364, 322, 308, 12, 26926, 420, 286,
  500, 380, 458, 1577, 2487, 4166, 50644], "temperature": 0.0, "avg_logprob": -0.20285599807213092,
  "compression_ratio": 1.6380090497737556, "no_speech_prob": 0.00987403653562069},
  {"id": 464, "seek": 279126, "start": 2796.86, "end": 2802.38, "text": " search you
  know things come up every week maybe right so like I don''t know Tesla releasing",
  "tokens": [50644, 3164, 291, 458, 721, 808, 493, 633, 1243, 1310, 558, 370, 411,
  286, 500, 380, 458, 13666, 16327, 50920], "temperature": 0.0, "avg_logprob": -0.20285599807213092,
  "compression_ratio": 1.6380090497737556, "no_speech_prob": 0.00987403653562069},
  {"id": 465, "seek": 279126, "start": 2802.38, "end": 2807.6600000000003, "text":
  " cyber truck and you don''t have it in the in the model so it actually like in
  your example", "tokens": [50920, 13411, 5898, 293, 291, 500, 380, 362, 309, 294,
  264, 294, 264, 2316, 370, 309, 767, 411, 294, 428, 1365, 51184], "temperature":
  0.0, "avg_logprob": -0.20285599807213092, "compression_ratio": 1.6380090497737556,
  "no_speech_prob": 0.00987403653562069}, {"id": 466, "seek": 279126, "start": 2808.2200000000003,
  "end": 2815.42, "text": " what was it with the ocean and like yeah I hear you say
  like how to catch an Alaska", "tokens": [51212, 437, 390, 309, 365, 264, 7810, 293,
  411, 1338, 286, 1568, 291, 584, 411, 577, 281, 3745, 364, 19553, 51572], "temperature":
  0.0, "avg_logprob": -0.20285599807213092, "compression_ratio": 1.6380090497737556,
  "no_speech_prob": 0.00987403653562069}, {"id": 467, "seek": 281542, "start": 2815.58,
  "end": 2822.06, "text": " Pollock and then let''s pretend that Alaska Pollock is
  a new fish that like you maybe with", "tokens": [50372, 31304, 1560, 293, 550, 718,
  311, 11865, 300, 19553, 31304, 1560, 307, 257, 777, 3506, 300, 411, 291, 1310, 365,
  50696], "temperature": 0.0, "avg_logprob": -0.18749222225613063, "compression_ratio":
  1.6755555555555555, "no_speech_prob": 0.004145725630223751}, {"id": 468, "seek":
  281542, "start": 2822.06, "end": 2828.38, "text": " vector search you may try to
  find what could be the most similar object but it may also be wrong", "tokens":
  [50696, 8062, 3164, 291, 815, 853, 281, 915, 437, 727, 312, 264, 881, 2531, 2657,
  457, 309, 815, 611, 312, 2085, 51012], "temperature": 0.0, "avg_logprob": -0.18749222225613063,
  "compression_ratio": 1.6755555555555555, "no_speech_prob": 0.004145725630223751},
  {"id": 469, "seek": 281542, "start": 2828.38, "end": 2836.38, "text": " right or
  in the case when the distance is so big that it doesn''t make sense anymore to consider",
  "tokens": [51012, 558, 420, 294, 264, 1389, 562, 264, 4560, 307, 370, 955, 300,
  309, 1177, 380, 652, 2020, 3602, 281, 1949, 51412], "temperature": 0.0, "avg_logprob":
  -0.18749222225613063, "compression_ratio": 1.6755555555555555, "no_speech_prob":
  0.004145725630223751}, {"id": 470, "seek": 281542, "start": 2836.38, "end": 2842.86,
  "text": " this as a candidate right so yeah so this is this is very interesting
  like and I hear that you", "tokens": [51412, 341, 382, 257, 11532, 558, 370, 1338,
  370, 341, 307, 341, 307, 588, 1880, 411, 293, 286, 1568, 300, 291, 51736], "temperature":
  0.0, "avg_logprob": -0.18749222225613063, "compression_ratio": 1.6755555555555555,
  "no_speech_prob": 0.004145725630223751}, {"id": 471, "seek": 284286, "start": 2843.34,
  "end": 2851.02, "text": " you really want to like dive into fine tuning topic as
  well right yeah well that idea is", "tokens": [50388, 291, 534, 528, 281, 411, 9192,
  666, 2489, 15164, 4829, 382, 731, 558, 1338, 731, 300, 1558, 307, 50772], "temperature":
  0.0, "avg_logprob": -0.12928794897519624, "compression_ratio": 1.7649253731343284,
  "no_speech_prob": 0.0054238829761743546}, {"id": 472, "seek": 284286, "start": 2851.02,
  "end": 2856.3, "text": " amazing because there this argument and I also when I interviewed
  multi-peach he gave me these", "tokens": [50772, 2243, 570, 456, 341, 6770, 293,
  286, 611, 562, 286, 19770, 4825, 12, 494, 608, 415, 2729, 385, 613, 51036], "temperature":
  0.0, "avg_logprob": -0.12928794897519624, "compression_ratio": 1.7649253731343284,
  "no_speech_prob": 0.0054238829761743546}, {"id": 473, "seek": 284286, "start": 2856.3,
  "end": 2860.86, "text": " three reasons to favor the retrieve then read approach
  to large language models and one of which", "tokens": [51036, 1045, 4112, 281, 2294,
  264, 30254, 550, 1401, 3109, 281, 2416, 2856, 5245, 293, 472, 295, 597, 51264],
  "temperature": 0.0, "avg_logprob": -0.12928794897519624, "compression_ratio": 1.7649253731343284,
  "no_speech_prob": 0.0054238829761743546}, {"id": 474, "seek": 284286, "start": 2860.86,
  "end": 2865.1, "text": " was this idea that you can swap out the information to
  update it with new information cyber truck", "tokens": [51264, 390, 341, 1558, 300,
  291, 393, 18135, 484, 264, 1589, 281, 5623, 309, 365, 777, 1589, 13411, 5898, 51476],
  "temperature": 0.0, "avg_logprob": -0.12928794897519624, "compression_ratio": 1.7649253731343284,
  "no_speech_prob": 0.0054238829761743546}, {"id": 475, "seek": 284286, "start": 2865.1,
  "end": 2868.46, "text": " becomes a new thing and then you can put it in the context
  and now the language model just has", "tokens": [51476, 3643, 257, 777, 551, 293,
  550, 291, 393, 829, 309, 294, 264, 4319, 293, 586, 264, 2856, 2316, 445, 575, 51644],
  "temperature": 0.0, "avg_logprob": -0.12928794897519624, "compression_ratio": 1.7649253731343284,
  "no_speech_prob": 0.0054238829761743546}, {"id": 476, "seek": 286846, "start": 2868.46,
  "end": 2873.5, "text": " the reason across the context but then as you say the embedding
  model doesn''t know about the new", "tokens": [50364, 264, 1778, 2108, 264, 4319,
  457, 550, 382, 291, 584, 264, 12240, 3584, 2316, 1177, 380, 458, 466, 264, 777,
  50616], "temperature": 0.0, "avg_logprob": -0.13318120914956796, "compression_ratio":
  1.7397260273972603, "no_speech_prob": 0.0051767039112746716}, {"id": 477, "seek":
  286846, "start": 2873.5, "end": 2878.94, "text": " thing so the embedding model
  you know also isn''t going to pick it up and so yeah I think that", "tokens": [50616,
  551, 370, 264, 12240, 3584, 2316, 291, 458, 611, 1943, 380, 516, 281, 1888, 309,
  493, 293, 370, 1338, 286, 519, 300, 50888], "temperature": 0.0, "avg_logprob": -0.13318120914956796,
  "compression_ratio": 1.7397260273972603, "no_speech_prob": 0.0051767039112746716},
  {"id": 478, "seek": 286846, "start": 2878.94, "end": 2883.7400000000002, "text":
  " continuous updating one idea that I''m just incredibly excited about I haven''t
  figured out how to", "tokens": [50888, 10957, 25113, 472, 1558, 300, 286, 478, 445,
  6252, 2919, 466, 286, 2378, 380, 8932, 484, 577, 281, 51128], "temperature": 0.0,
  "avg_logprob": -0.13318120914956796, "compression_ratio": 1.7397260273972603, "no_speech_prob":
  0.0051767039112746716}, {"id": 479, "seek": 286846, "start": 2883.7400000000002,
  "end": 2890.86, "text": " make this work yet but the idea would be you you''re the
  ML ops problem of this is you need to", "tokens": [51128, 652, 341, 589, 1939, 457,
  264, 1558, 576, 312, 291, 291, 434, 264, 21601, 44663, 1154, 295, 341, 307, 291,
  643, 281, 51484], "temperature": 0.0, "avg_logprob": -0.13318120914956796, "compression_ratio":
  1.7397260273972603, "no_speech_prob": 0.0051767039112746716}, {"id": 480, "seek":
  289086, "start": 2890.94, "end": 2902.46, "text": " re-vectorize your data set which
  yeah so the solution maybe is that you could vectorize like a", "tokens": [50368,
  319, 12, 303, 1672, 1125, 428, 1412, 992, 597, 1338, 370, 264, 3827, 1310, 307,
  300, 291, 727, 8062, 1125, 411, 257, 50944], "temperature": 0.0, "avg_logprob":
  -0.26922842172475964, "compression_ratio": 1.5051546391752577, "no_speech_prob":
  0.0041251578368246555}, {"id": 481, "seek": 289086, "start": 2902.46, "end": 2909.6600000000003,
  "text": " thousand representative documents and my hypothesis is that the proximity
  graph from I want to say", "tokens": [50944, 4714, 12424, 8512, 293, 452, 17291,
  307, 300, 264, 27632, 4295, 490, 286, 528, 281, 584, 51304], "temperature": 0.0,
  "avg_logprob": -0.26922842172475964, "compression_ratio": 1.5051546391752577, "no_speech_prob":
  0.0041251578368246555}, {"id": 482, "seek": 289086, "start": 2909.6600000000003,
  "end": 2915.82, "text": " Vamanum or Southern H and SW because I barely understand
  graph neural networks let alone trying to", "tokens": [51304, 691, 6147, 449, 420,
  13724, 389, 293, 20346, 570, 286, 10268, 1223, 4295, 18161, 9590, 718, 3312, 1382,
  281, 51612], "temperature": 0.0, "avg_logprob": -0.26922842172475964, "compression_ratio":
  1.5051546391752577, "no_speech_prob": 0.0041251578368246555}, {"id": 483, "seek":
  291582, "start": 2915.82, "end": 2922.38, "text": " make it a hierarchical neural
  network but like if it''s if it''s the proximity graph maybe you can", "tokens":
  [50364, 652, 309, 257, 35250, 804, 18161, 3209, 457, 411, 498, 309, 311, 498, 309,
  311, 264, 27632, 4295, 1310, 291, 393, 50692], "temperature": 0.0, "avg_logprob":
  -0.11983980451311384, "compression_ratio": 2.086206896551724, "no_speech_prob":
  0.003155354643240571}, {"id": 484, "seek": 291582, "start": 2923.1800000000003,
  "end": 2928.06, "text": " it''s like it''s like it''s like a psycho again it''s
  very similar to like image to image translation", "tokens": [50732, 309, 311, 411,
  309, 311, 411, 309, 311, 411, 257, 33355, 797, 309, 311, 588, 2531, 281, 411, 3256,
  281, 3256, 12853, 50976], "temperature": 0.0, "avg_logprob": -0.11983980451311384,
  "compression_ratio": 2.086206896551724, "no_speech_prob": 0.003155354643240571},
  {"id": 485, "seek": 291582, "start": 2928.06, "end": 2932.7000000000003, "text":
  " or any kind of you know it''s a vector space to vector space translation and so
  you you know you", "tokens": [50976, 420, 604, 733, 295, 291, 458, 309, 311, 257,
  8062, 1901, 281, 8062, 1901, 12853, 293, 370, 291, 291, 458, 291, 51208], "temperature":
  0.0, "avg_logprob": -0.11983980451311384, "compression_ratio": 2.086206896551724,
  "no_speech_prob": 0.003155354643240571}, {"id": 486, "seek": 291582, "start": 2932.7000000000003,
  "end": 2937.1000000000004, "text": " input the vector output the change in vector
  and so can you vectorize like a thousand and then", "tokens": [51208, 4846, 264,
  8062, 5598, 264, 1319, 294, 8062, 293, 370, 393, 291, 8062, 1125, 411, 257, 4714,
  293, 550, 51428], "temperature": 0.0, "avg_logprob": -0.11983980451311384, "compression_ratio":
  2.086206896551724, "no_speech_prob": 0.003155354643240571}, {"id": 487, "seek":
  291582, "start": 2937.1000000000004, "end": 2943.6600000000003, "text": " propagate
  that throughout the graph it or throughout the corpus and maybe that proximity graph
  has", "tokens": [51428, 48256, 300, 3710, 264, 4295, 309, 420, 3710, 264, 1181,
  31624, 293, 1310, 300, 27632, 4295, 575, 51756], "temperature": 0.0, "avg_logprob":
  -0.11983980451311384, "compression_ratio": 2.086206896551724, "no_speech_prob":
  0.003155354643240571}, {"id": 488, "seek": 294366, "start": 2943.66, "end": 2949.8199999999997,
  "text": " some kind of bias that facilitates the optimization task or maybe the
  graph neural network thing is", "tokens": [50364, 512, 733, 295, 12577, 300, 10217,
  30035, 264, 19618, 5633, 420, 1310, 264, 4295, 18161, 3209, 551, 307, 50672], "temperature":
  0.0, "avg_logprob": -0.12414924109854349, "compression_ratio": 1.6398305084745763,
  "no_speech_prob": 0.0008932074997574091}, {"id": 489, "seek": 294366, "start": 2949.8199999999997,
  "end": 2954.2999999999997, "text": " too much overhead and you''re better off just
  having like a transformer that takes into vector outputs", "tokens": [50672, 886,
  709, 19922, 293, 291, 434, 1101, 766, 445, 1419, 411, 257, 31782, 300, 2516, 666,
  8062, 23930, 50896], "temperature": 0.0, "avg_logprob": -0.12414924109854349, "compression_ratio":
  1.6398305084745763, "no_speech_prob": 0.0008932074997574091}, {"id": 490, "seek":
  294366, "start": 2954.2999999999997, "end": 2960.94, "text": " a vector but yeah
  that this idea of like how do you continually update your embedding models", "tokens":
  [50896, 257, 8062, 457, 1338, 300, 341, 1558, 295, 411, 577, 360, 291, 22277, 5623,
  428, 12240, 3584, 5245, 51228], "temperature": 0.0, "avg_logprob": -0.12414924109854349,
  "compression_ratio": 1.6398305084745763, "no_speech_prob": 0.0008932074997574091},
  {"id": 491, "seek": 294366, "start": 2961.58, "end": 2966.54, "text": " it''s fascinating
  right yeah yeah especially the ML ops aspect of it as you''ve mentioned like", "tokens":
  [51260, 309, 311, 10343, 558, 1338, 1338, 2318, 264, 21601, 44663, 4171, 295, 309,
  382, 291, 600, 2835, 411, 51508], "temperature": 0.0, "avg_logprob": -0.12414924109854349,
  "compression_ratio": 1.6398305084745763, "no_speech_prob": 0.0008932074997574091},
  {"id": 492, "seek": 296654, "start": 2966.62, "end": 2974.62, "text": " if if we
  were to insert new neighbors into the existing graph right would that change", "tokens":
  [50368, 498, 498, 321, 645, 281, 8969, 777, 12512, 666, 264, 6741, 4295, 558, 576,
  300, 1319, 50768], "temperature": 0.0, "avg_logprob": -0.13443925163962625, "compression_ratio":
  1.6403508771929824, "no_speech_prob": 0.002118273638188839}, {"id": 493, "seek":
  296654, "start": 2975.9, "end": 2981.34, "text": " it favors something more recent
  or would it like break something that we didn''t want to break and", "tokens": [50832,
  309, 40554, 746, 544, 5162, 420, 576, 309, 411, 1821, 746, 300, 321, 994, 380, 528,
  281, 1821, 293, 51104], "temperature": 0.0, "avg_logprob": -0.13443925163962625,
  "compression_ratio": 1.6403508771929824, "no_speech_prob": 0.002118273638188839},
  {"id": 494, "seek": 296654, "start": 2981.34, "end": 2985.74, "text": " things but
  but in some sense if you think about coming back like we are still in the realm
  of", "tokens": [51104, 721, 457, 457, 294, 512, 2020, 498, 291, 519, 466, 1348,
  646, 411, 321, 366, 920, 294, 264, 15355, 295, 51324], "temperature": 0.0, "avg_logprob":
  -0.13443925163962625, "compression_ratio": 1.6403508771929824, "no_speech_prob":
  0.002118273638188839}, {"id": 495, "seek": 296654, "start": 2985.74, "end": 2995.74,
  "text": " this hybrid search topic in a way right if you look at BM25 OTF idea of
  approach right so if you", "tokens": [51324, 341, 13051, 3164, 4829, 294, 257, 636,
  558, 498, 291, 574, 412, 15901, 6074, 38617, 37, 1558, 295, 3109, 558, 370, 498,
  291, 51824], "temperature": 0.0, "avg_logprob": -0.13443925163962625, "compression_ratio":
  1.6403508771929824, "no_speech_prob": 0.002118273638188839}, {"id": 496, "seek":
  299574, "start": 2995.74, "end": 3002.62, "text": " compute so you''re I so you
  term frequency is only dependent on this document right so that''s fine", "tokens":
  [50364, 14722, 370, 291, 434, 286, 370, 291, 1433, 7893, 307, 787, 12334, 322, 341,
  4166, 558, 370, 300, 311, 2489, 50708], "temperature": 0.0, "avg_logprob": -0.10091669419232537,
  "compression_ratio": 1.8232558139534885, "no_speech_prob": 0.0011172413360327482},
  {"id": 497, "seek": 299574, "start": 3002.62, "end": 3008.62, "text": " it''s kind
  of the independent of all other documents but your inverse document frequency is
  dependent", "tokens": [50708, 309, 311, 733, 295, 264, 6695, 295, 439, 661, 8512,
  457, 428, 17340, 4166, 7893, 307, 12334, 51008], "temperature": 0.0, "avg_logprob":
  -0.10091669419232537, "compression_ratio": 1.8232558139534885, "no_speech_prob":
  0.0011172413360327482}, {"id": 498, "seek": 299574, "start": 3008.62, "end": 3013.74,
  "text": " on the whole corpus which is indexed in that chart by the way that''s
  another like big topic which", "tokens": [51008, 322, 264, 1379, 1181, 31624, 597,
  307, 8186, 292, 294, 300, 6927, 538, 264, 636, 300, 311, 1071, 411, 955, 4829, 597,
  51264], "temperature": 0.0, "avg_logprob": -0.10091669419232537, "compression_ratio":
  1.8232558139534885, "no_speech_prob": 0.0011172413360327482}, {"id": 499, "seek":
  299574, "start": 3013.74, "end": 3020.8599999999997, "text": " is kind of like crossing
  the boundary of is this just infrastructure issue in slash engineering", "tokens":
  [51264, 307, 733, 295, 411, 14712, 264, 12866, 295, 307, 341, 445, 6896, 2734, 294,
  17330, 7043, 51620], "temperature": 0.0, "avg_logprob": -0.10091669419232537, "compression_ratio":
  1.8232558139534885, "no_speech_prob": 0.0011172413360327482}, {"id": 500, "seek":
  302086, "start": 3021.02, "end": 3029.1800000000003, "text": " is this kind of like
  research issue and it''s like it''s fuzzy it''s it''s it''s it''s a blend and so
  for", "tokens": [50372, 307, 341, 733, 295, 411, 2132, 2734, 293, 309, 311, 411,
  309, 311, 34710, 309, 311, 309, 311, 309, 311, 309, 311, 257, 10628, 293, 370, 337,
  50780], "temperature": 0.0, "avg_logprob": -0.1481343078613281, "compression_ratio":
  1.6647727272727273, "no_speech_prob": 0.0016965331742540002}, {"id": 501, "seek":
  302086, "start": 3029.1800000000003, "end": 3041.7400000000002, "text": " that chart
  you''re gonna have that local idea unless you build a a higher level cache which
  will", "tokens": [50780, 300, 6927, 291, 434, 799, 362, 300, 2654, 1558, 5969, 291,
  1322, 257, 257, 2946, 1496, 19459, 597, 486, 51408], "temperature": 0.0, "avg_logprob":
  -0.1481343078613281, "compression_ratio": 1.6647727272727273, "no_speech_prob":
  0.0016965331742540002}, {"id": 502, "seek": 302086, "start": 3041.7400000000002,
  "end": 3048.06, "text": " keep track of each individual chart''s idea and roll it
  up to the global idea and like if you look", "tokens": [51408, 1066, 2837, 295,
  1184, 2609, 6927, 311, 1558, 293, 3373, 309, 493, 281, 264, 4338, 1558, 293, 411,
  498, 291, 574, 51724], "temperature": 0.0, "avg_logprob": -0.1481343078613281, "compression_ratio":
  1.6647727272727273, "no_speech_prob": 0.0016965331742540002}, {"id": 503, "seek":
  304806, "start": 3048.7799999999997, "end": 3055.74, "text": " at Apache Solar I
  think I believe they had a country module or something implementing this", "tokens":
  [50400, 412, 46597, 22385, 286, 519, 286, 1697, 436, 632, 257, 1941, 10088, 420,
  746, 18114, 341, 50748], "temperature": 0.0, "avg_logprob": -0.17180637831098577,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.002612438751384616},
  {"id": 504, "seek": 304806, "start": 3057.02, "end": 3062.22, "text": " where you
  can actually implement a global cache with IDF which will live on top of the", "tokens":
  [50812, 689, 291, 393, 767, 4445, 257, 4338, 19459, 365, 7348, 37, 597, 486, 1621,
  322, 1192, 295, 264, 51072], "temperature": 0.0, "avg_logprob": -0.17180637831098577,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.002612438751384616},
  {"id": 505, "seek": 304806, "start": 3062.22, "end": 3067.18, "text": " chart and
  now you''re coming back to MLOBS you need to make sure it never dies because if
  it dies you", "tokens": [51072, 6927, 293, 586, 291, 434, 1348, 646, 281, 376, 20184,
  8176, 291, 643, 281, 652, 988, 309, 1128, 2714, 570, 498, 309, 2714, 291, 51320],
  "temperature": 0.0, "avg_logprob": -0.17180637831098577, "compression_ratio": 1.5932203389830508,
  "no_speech_prob": 0.002612438751384616}, {"id": 506, "seek": 304806, "start": 3067.18,
  "end": 3074.7, "text": " go back to like the chart level IDF and so that becomes
  dependent on okay I have managed to stuff", "tokens": [51320, 352, 646, 281, 411,
  264, 6927, 1496, 7348, 37, 293, 370, 300, 3643, 12334, 322, 1392, 286, 362, 6453,
  281, 1507, 51696], "temperature": 0.0, "avg_logprob": -0.17180637831098577, "compression_ratio":
  1.5932203389830508, "no_speech_prob": 0.002612438751384616}, {"id": 507, "seek":
  307470, "start": 3075.66, "end": 3083.2599999999998, "text": " stuff a lot of documents
  about cats in this chart so the IDF is like this and then I", "tokens": [50412,
  1507, 257, 688, 295, 8512, 466, 11111, 294, 341, 6927, 370, 264, 7348, 37, 307,
  411, 341, 293, 550, 286, 50792], "temperature": 0.0, "avg_logprob": -0.1194376641131462,
  "compression_ratio": 1.7757009345794392, "no_speech_prob": 0.002432736800983548},
  {"id": 508, "seek": 307470, "start": 3083.2599999999998, "end": 3088.2999999999997,
  "text": " stuff a lot of documents on dogs here so they become like unbalanced if
  you if you know what I mean", "tokens": [50792, 1507, 257, 688, 295, 8512, 322,
  7197, 510, 370, 436, 1813, 411, 517, 40251, 498, 291, 498, 291, 458, 437, 286, 914,
  51044], "temperature": 0.0, "avg_logprob": -0.1194376641131462, "compression_ratio":
  1.7757009345794392, "no_speech_prob": 0.002432736800983548}, {"id": 509, "seek":
  307470, "start": 3088.2999999999997, "end": 3097.98, "text": " so they it''s not
  a healthy mix of term statistics in your collection right and that will influence
  a", "tokens": [51044, 370, 436, 309, 311, 406, 257, 4627, 2890, 295, 1433, 12523,
  294, 428, 5765, 558, 293, 300, 486, 6503, 257, 51528], "temperature": 0.0, "avg_logprob":
  -0.1194376641131462, "compression_ratio": 1.7757009345794392, "no_speech_prob":
  0.002432736800983548}, {"id": 510, "seek": 307470, "start": 3097.98, "end": 3104.46,
  "text": " lot of things like you may say in some cases it''s okay but in some other
  cases it may not work", "tokens": [51528, 688, 295, 721, 411, 291, 815, 584, 294,
  512, 3331, 309, 311, 1392, 457, 294, 512, 661, 3331, 309, 815, 406, 589, 51852],
  "temperature": 0.0, "avg_logprob": -0.1194376641131462, "compression_ratio": 1.7757009345794392,
  "no_speech_prob": 0.002432736800983548}, {"id": 511, "seek": 310446, "start": 3104.46,
  "end": 3110.78, "text": " if your query contains you know both concepts and they
  are unequally represented somehow", "tokens": [50364, 498, 428, 14581, 8306, 291,
  458, 1293, 10392, 293, 436, 366, 2251, 358, 379, 10379, 6063, 50680], "temperature":
  0.0, "avg_logprob": -0.10266880872772961, "compression_ratio": 1.691588785046729,
  "no_speech_prob": 0.0019075166201218963}, {"id": 512, "seek": 310446, "start": 3111.42,
  "end": 3117.5, "text": " in your in your collection right so so I mean does it make
  sense I mean so it''s like you do have", "tokens": [50712, 294, 428, 294, 428, 5765,
  558, 370, 370, 286, 914, 775, 309, 652, 2020, 286, 914, 370, 309, 311, 411, 291,
  360, 362, 51016], "temperature": 0.0, "avg_logprob": -0.10266880872772961, "compression_ratio":
  1.691588785046729, "no_speech_prob": 0.0019075166201218963}, {"id": 513, "seek":
  310446, "start": 3117.5, "end": 3122.86, "text": " limitations also and and not
  limitations but maybe I should pose it in more positive way", "tokens": [51016,
  15705, 611, 293, 293, 406, 15705, 457, 1310, 286, 820, 10774, 309, 294, 544, 3353,
  636, 51284], "temperature": 0.0, "avg_logprob": -0.10266880872772961, "compression_ratio":
  1.691588785046729, "no_speech_prob": 0.0019075166201218963}, {"id": 514, "seek":
  310446, "start": 3122.86, "end": 3129.18, "text": " research tasks right so such
  challenges what should we do and I hope that in some sense", "tokens": [51284, 2132,
  9608, 558, 370, 1270, 4759, 437, 820, 321, 360, 293, 286, 1454, 300, 294, 512, 2020,
  51600], "temperature": 0.0, "avg_logprob": -0.10266880872772961, "compression_ratio":
  1.691588785046729, "no_speech_prob": 0.0019075166201218963}, {"id": 515, "seek":
  312918, "start": 3129.2599999999998, "end": 3135.58, "text": " dense search is pushing
  us to think more and more about this and maybe some things will back lash", "tokens":
  [50368, 18011, 3164, 307, 7380, 505, 281, 519, 544, 293, 544, 466, 341, 293, 1310,
  512, 721, 486, 646, 35275, 50684], "temperature": 0.0, "avg_logprob": -0.1685879718826478,
  "compression_ratio": 1.7242990654205608, "no_speech_prob": 0.001397663843818009},
  {"id": 516, "seek": 312918, "start": 3135.58, "end": 3143.74, "text": " from vector
  search back to the you know classical keyword retrieval and maybe some new data",
  "tokens": [50684, 490, 8062, 3164, 646, 281, 264, 291, 458, 13735, 20428, 19817,
  3337, 293, 1310, 512, 777, 1412, 51092], "temperature": 0.0, "avg_logprob": -0.1685879718826478,
  "compression_ratio": 1.7242990654205608, "no_speech_prob": 0.001397663843818009},
  {"id": 517, "seek": 312918, "start": 3143.74, "end": 3150.14, "text": " structures
  will even emerge to to tackle these things yeah I think that idea that you''re",
  "tokens": [51092, 9227, 486, 754, 21511, 281, 281, 14896, 613, 721, 1338, 286, 519,
  300, 1558, 300, 291, 434, 51412], "temperature": 0.0, "avg_logprob": -0.1685879718826478,
  "compression_ratio": 1.7242990654205608, "no_speech_prob": 0.001397663843818009},
  {"id": 518, "seek": 312918, "start": 3150.54, "end": 3157.74, "text": " describing
  on the IDF caching it''s super interesting I think it is it is inspiring me just",
  "tokens": [51432, 16141, 322, 264, 7348, 37, 269, 2834, 309, 311, 1687, 1880, 286,
  519, 309, 307, 309, 307, 15883, 385, 445, 51792], "temperature": 0.0, "avg_logprob":
  -0.1685879718826478, "compression_ratio": 1.7242990654205608, "no_speech_prob":
  0.001397663843818009}, {"id": 519, "seek": 315774, "start": 3157.74, "end": 3160.9399999999996,
  "text": " thinking generally about how we''re trading knowledge on this thing in
  general and having this", "tokens": [50364, 1953, 5101, 466, 577, 321, 434, 9529,
  3601, 322, 341, 551, 294, 2674, 293, 1419, 341, 50524], "temperature": 0.0, "avg_logprob":
  -0.11796992840153156, "compression_ratio": 1.7822878228782288, "no_speech_prob":
  0.0029816513415426016}, {"id": 520, "seek": 315774, "start": 3160.9399999999996,
  "end": 3165.5, "text": " podcast and having this content and this communication
  and how we''ve you know done like our first", "tokens": [50524, 7367, 293, 1419,
  341, 2701, 293, 341, 6101, 293, 577, 321, 600, 291, 458, 1096, 411, 527, 700, 50752],
  "temperature": 0.0, "avg_logprob": -0.11796992840153156, "compression_ratio": 1.7822878228782288,
  "no_speech_prob": 0.0029816513415426016}, {"id": 521, "seek": 315774, "start": 3165.5,
  "end": 3170.7799999999997, "text": " iteration of BN25 and yeah like learning so
  much about the index structure it is really really", "tokens": [50752, 24784, 295,
  363, 45, 6074, 293, 1338, 411, 2539, 370, 709, 466, 264, 8186, 3877, 309, 307, 534,
  534, 51016], "temperature": 0.0, "avg_logprob": -0.11796992840153156, "compression_ratio":
  1.7822878228782288, "no_speech_prob": 0.0029816513415426016}, {"id": 522, "seek":
  315774, "start": 3170.7799999999997, "end": 3176.22, "text": " interesting I was
  thinking about like oh well how about displayed vectors could could we just kind",
  "tokens": [51016, 1880, 286, 390, 1953, 466, 411, 1954, 731, 577, 466, 16372, 18875,
  727, 727, 321, 445, 733, 51288], "temperature": 0.0, "avg_logprob": -0.11796992840153156,
  "compression_ratio": 1.7822878228782288, "no_speech_prob": 0.0029816513415426016},
  {"id": 523, "seek": 315774, "start": 3176.22, "end": 3180.2999999999997, "text":
  " of update the mass language modeling head to get the new terms and would that
  be easier than this", "tokens": [51288, 295, 5623, 264, 2758, 2856, 15983, 1378,
  281, 483, 264, 777, 2115, 293, 576, 300, 312, 3571, 813, 341, 51492], "temperature":
  0.0, "avg_logprob": -0.11796992840153156, "compression_ratio": 1.7822878228782288,
  "no_speech_prob": 0.0029816513415426016}, {"id": 524, "seek": 318030, "start": 3180.38,
  "end": 3187.5800000000004, "text": " kind of global cache I like idea and is it
  more forward thinking and then yeah it''s really", "tokens": [50368, 733, 295, 4338,
  19459, 286, 411, 1558, 293, 307, 309, 544, 2128, 1953, 293, 550, 1338, 309, 311,
  534, 50728], "temperature": 0.0, "avg_logprob": -0.11349851351517898, "compression_ratio":
  1.8695652173913044, "no_speech_prob": 0.0012161463964730501}, {"id": 525, "seek":
  318030, "start": 3187.5800000000004, "end": 3192.38, "text": " interesting I think
  maybe one other idea is this thing called colbert which is like a token level",
  "tokens": [50728, 1880, 286, 519, 1310, 472, 661, 1558, 307, 341, 551, 1219, 1173,
  4290, 597, 307, 411, 257, 14862, 1496, 50968], "temperature": 0.0, "avg_logprob":
  -0.11349851351517898, "compression_ratio": 1.8695652173913044, "no_speech_prob":
  0.0012161463964730501}, {"id": 526, "seek": 318030, "start": 3192.38, "end": 3197.7400000000002,
  "text": " representation thing where it''s like they call it late interaction where
  first you do the you know", "tokens": [50968, 10290, 551, 689, 309, 311, 411, 436,
  818, 309, 3469, 9285, 689, 700, 291, 360, 264, 291, 458, 51236], "temperature":
  0.0, "avg_logprob": -0.11349851351517898, "compression_ratio": 1.8695652173913044,
  "no_speech_prob": 0.0012161463964730501}, {"id": 527, "seek": 318030, "start": 3197.7400000000002,
  "end": 3202.0600000000004, "text": " the standard vector search but then you keep
  the token vectors for each of the vectors and", "tokens": [51236, 264, 3832, 8062,
  3164, 457, 550, 291, 1066, 264, 14862, 18875, 337, 1184, 295, 264, 18875, 293, 51452],
  "temperature": 0.0, "avg_logprob": -0.11349851351517898, "compression_ratio": 1.8695652173913044,
  "no_speech_prob": 0.0012161463964730501}, {"id": 528, "seek": 318030, "start": 3202.0600000000004,
  "end": 3205.82, "text": " and then you do that and then they''ve had efficiency
  improvements on that so like I think they", "tokens": [51452, 293, 550, 291, 360,
  300, 293, 550, 436, 600, 632, 10493, 13797, 322, 300, 370, 411, 286, 519, 436, 51640],
  "temperature": 0.0, "avg_logprob": -0.11349851351517898, "compression_ratio": 1.8695652173913044,
  "no_speech_prob": 0.0012161463964730501}, {"id": 529, "seek": 320582, "start": 3205.9,
  "end": 3210.94, "text": " in the original colbert they they''ve recently published
  this paper I know Christopher Pots and", "tokens": [50368, 294, 264, 3380, 1173,
  4290, 436, 436, 600, 3938, 6572, 341, 3035, 286, 458, 20649, 430, 1971, 293, 50620],
  "temperature": 0.0, "avg_logprob": -0.2349657041836629, "compression_ratio": 1.7269372693726937,
  "no_speech_prob": 0.00920638907700777}, {"id": 530, "seek": 320582, "start": 3210.94,
  "end": 3216.06, "text": " Omar Kataba I''m sorry I don''t know like I''ll show my
  best like no give everyone credit all the time", "tokens": [50620, 33784, 8365,
  5509, 286, 478, 2597, 286, 500, 380, 458, 411, 286, 603, 855, 452, 1151, 411, 572,
  976, 1518, 5397, 439, 264, 565, 50876], "temperature": 0.0, "avg_logprob": -0.2349657041836629,
  "compression_ratio": 1.7269372693726937, "no_speech_prob": 0.00920638907700777},
  {"id": 531, "seek": 320582, "start": 3217.7400000000002, "end": 3222.1400000000003,
  "text": " but in this paper they describe it like the original colbert is like in
  154 gigabyte", "tokens": [50960, 457, 294, 341, 3035, 436, 6786, 309, 411, 264,
  3380, 1173, 4290, 307, 411, 294, 2119, 19, 8741, 34529, 51180], "temperature": 0.0,
  "avg_logprob": -0.2349657041836629, "compression_ratio": 1.7269372693726937, "no_speech_prob":
  0.00920638907700777}, {"id": 532, "seek": 320582, "start": 3223.9, "end": 3229.02,
  "text": " index compared to like one gigabyte with other methods and so so yeah
  like efficient indexing", "tokens": [51268, 8186, 5347, 281, 411, 472, 8741, 34529,
  365, 661, 7150, 293, 370, 370, 1338, 411, 7148, 8186, 278, 51524], "temperature":
  0.0, "avg_logprob": -0.2349657041836629, "compression_ratio": 1.7269372693726937,
  "no_speech_prob": 0.00920638907700777}, {"id": 533, "seek": 320582, "start": 3229.02,
  "end": 3234.54, "text": " and I''m definitely running a van but it is like a big
  thing to unpack there''s so much depth to", "tokens": [51524, 293, 286, 478, 2138,
  2614, 257, 3161, 457, 309, 307, 411, 257, 955, 551, 281, 26699, 456, 311, 370, 709,
  7161, 281, 51800], "temperature": 0.0, "avg_logprob": -0.2349657041836629, "compression_ratio":
  1.7269372693726937, "no_speech_prob": 0.00920638907700777}, {"id": 534, "seek":
  323454, "start": 3234.54, "end": 3239.18, "text": " this and that''s what makes
  working in this field so exciting is that there''s so much opportunity", "tokens":
  [50364, 341, 293, 300, 311, 437, 1669, 1364, 294, 341, 2519, 370, 4670, 307, 300,
  456, 311, 370, 709, 2650, 50596], "temperature": 0.0, "avg_logprob": -0.11373717384000795,
  "compression_ratio": 1.8052434456928839, "no_speech_prob": 0.0044932859018445015},
  {"id": 535, "seek": 323454, "start": 3239.18, "end": 3245.2599999999998, "text":
  " so much to explore yeah yeah and so much unsolved as well I don''t I don''t know
  if you wanted to", "tokens": [50596, 370, 709, 281, 6839, 1338, 1338, 293, 370,
  709, 2693, 29110, 382, 731, 286, 500, 380, 286, 500, 380, 458, 498, 291, 1415, 281,
  50900], "temperature": 0.0, "avg_logprob": -0.11373717384000795, "compression_ratio":
  1.8052434456928839, "no_speech_prob": 0.0044932859018445015}, {"id": 536, "seek":
  323454, "start": 3245.2599999999998, "end": 3251.58, "text": " continue a thought
  oh no sorry yeah I was just yeah I mean we are branching out but like actually",
  "tokens": [50900, 2354, 257, 1194, 1954, 572, 2597, 1338, 286, 390, 445, 1338, 286,
  914, 321, 366, 9819, 278, 484, 457, 411, 767, 51216], "temperature": 0.0, "avg_logprob":
  -0.11373717384000795, "compression_ratio": 1.8052434456928839, "no_speech_prob":
  0.0044932859018445015}, {"id": 537, "seek": 323454, "start": 3251.58, "end": 3257.1,
  "text": " one thing that you just reminded me there was a maybe I should start writing
  a book or something", "tokens": [51216, 472, 551, 300, 291, 445, 15920, 385, 456,
  390, 257, 1310, 286, 820, 722, 3579, 257, 1446, 420, 746, 51492], "temperature":
  0.0, "avg_logprob": -0.11373717384000795, "compression_ratio": 1.8052434456928839,
  "no_speech_prob": 0.0044932859018445015}, {"id": 538, "seek": 323454, "start": 3257.1,
  "end": 3261.66, "text": " because like the moment I remember this I should write
  a chapter and then keep adding and then", "tokens": [51492, 570, 411, 264, 1623,
  286, 1604, 341, 286, 820, 2464, 257, 7187, 293, 550, 1066, 5127, 293, 550, 51720],
  "temperature": 0.0, "avg_logprob": -0.11373717384000795, "compression_ratio": 1.8052434456928839,
  "no_speech_prob": 0.0044932859018445015}, {"id": 539, "seek": 326166, "start": 3261.66,
  "end": 3269.3399999999997, "text": " publish it maybe you can be my author or something
  yeah that was just thinking it was was it like", "tokens": [50364, 11374, 309, 1310,
  291, 393, 312, 452, 3793, 420, 746, 1338, 300, 390, 445, 1953, 309, 390, 390, 309,
  411, 50748], "temperature": 0.0, "avg_logprob": -0.165740966796875, "compression_ratio":
  1.56, "no_speech_prob": 0.0037940277252346277}, {"id": 540, "seek": 326166, "start":
  3269.3399999999997, "end": 3274.8599999999997, "text": " 10 years ago on Berlin
  buzzwords there was a presentation by one of the engineers at Twitter I don''t",
  "tokens": [50748, 1266, 924, 2057, 322, 13848, 13036, 13832, 456, 390, 257, 5860,
  538, 472, 295, 264, 11955, 412, 5794, 286, 500, 380, 51024], "temperature": 0.0,
  "avg_logprob": -0.165740966796875, "compression_ratio": 1.56, "no_speech_prob":
  0.0037940277252346277}, {"id": 541, "seek": 326166, "start": 3274.8599999999997,
  "end": 3281.3399999999997, "text": " know if he''s still a Twitter and I forgot
  his name I remember he was German working out from", "tokens": [51024, 458, 498,
  415, 311, 920, 257, 5794, 293, 286, 5298, 702, 1315, 286, 1604, 415, 390, 6521,
  1364, 484, 490, 51348], "temperature": 0.0, "avg_logprob": -0.165740966796875, "compression_ratio":
  1.56, "no_speech_prob": 0.0037940277252346277}, {"id": 542, "seek": 326166, "start":
  3281.3399999999997, "end": 3289.8199999999997, "text": " San Francisco and he basically
  coming back to that issue with you know sorted document ideas right", "tokens":
  [51348, 5271, 12279, 293, 415, 1936, 1348, 646, 281, 300, 2734, 365, 291, 458, 25462,
  4166, 3487, 558, 51772], "temperature": 0.0, "avg_logprob": -0.165740966796875,
  "compression_ratio": 1.56, "no_speech_prob": 0.0037940277252346277}, {"id": 543,
  "seek": 329166, "start": 3292.14, "end": 3298.2999999999997, "text": " what they
  did at Twitter first of all you know the scale of Twitter is such that you cannot
  possibly store", "tokens": [50388, 437, 436, 630, 412, 5794, 700, 295, 439, 291,
  458, 264, 4373, 295, 5794, 307, 1270, 300, 291, 2644, 6264, 3531, 50696], "temperature":
  0.0, "avg_logprob": -0.11831770081450974, "compression_ratio": 1.6424581005586592,
  "no_speech_prob": 0.0027366860304027796}, {"id": 544, "seek": 329166, "start": 3299.8999999999996,
  "end": 3306.3799999999997, "text": " Lucine index on disk and then go and retrieve
  it because well it''s just way too slow right", "tokens": [50776, 9593, 533, 8186,
  322, 12355, 293, 550, 352, 293, 30254, 309, 570, 731, 309, 311, 445, 636, 886, 2964,
  558, 51100], "temperature": 0.0, "avg_logprob": -0.11831770081450974, "compression_ratio":
  1.6424581005586592, "no_speech_prob": 0.0027366860304027796}, {"id": 545, "seek":
  329166, "start": 3308.2999999999997, "end": 3315.42, "text": " what they did is
  that they moved the whole index into memory right so they had to rewrite Lucine",
  "tokens": [51196, 437, 436, 630, 307, 300, 436, 4259, 264, 1379, 8186, 666, 4675,
  558, 370, 436, 632, 281, 28132, 9593, 533, 51552], "temperature": 0.0, "avg_logprob":
  -0.11831770081450974, "compression_ratio": 1.6424581005586592, "no_speech_prob":
  0.0027366860304027796}, {"id": 546, "seek": 331542, "start": 3316.14, "end": 3324.14,
  "text": " to kind of like this memory friendly data structure and one thing they
  did in particular", "tokens": [50400, 281, 733, 295, 411, 341, 4675, 9208, 1412,
  3877, 293, 472, 551, 436, 630, 294, 1729, 50800], "temperature": 0.0, "avg_logprob":
  -0.12157423794269562, "compression_ratio": 1.6467065868263473, "no_speech_prob":
  0.002458452247083187}, {"id": 547, "seek": 331542, "start": 3324.14, "end": 3329.82,
  "text": " is that as tweets come in each tweet is a document it gets its unique
  document they deem", "tokens": [50800, 307, 300, 382, 25671, 808, 294, 1184, 15258,
  307, 257, 4166, 309, 2170, 1080, 3845, 4166, 436, 368, 443, 51084], "temperature":
  0.0, "avg_logprob": -0.12157423794269562, "compression_ratio": 1.6467065868263473,
  "no_speech_prob": 0.002458452247083187}, {"id": 548, "seek": 331542, "start": 3330.94,
  "end": 3341.66, "text": " and they would append this new document ID to the postings
  list in the end right so for this term", "tokens": [51140, 293, 436, 576, 34116,
  341, 777, 4166, 7348, 281, 264, 2183, 1109, 1329, 294, 264, 917, 558, 370, 337,
  341, 1433, 51676], "temperature": 0.0, "avg_logprob": -0.12157423794269562, "compression_ratio":
  1.6467065868263473, "no_speech_prob": 0.002458452247083187}, {"id": 549, "seek":
  334166, "start": 3341.74, "end": 3347.98, "text": " so they would decompose it into
  terms back and then they would know okay I need now to update that", "tokens": [50368,
  370, 436, 576, 22867, 541, 309, 666, 2115, 646, 293, 550, 436, 576, 458, 1392, 286,
  643, 586, 281, 5623, 300, 50680], "temperature": 0.0, "avg_logprob": -0.1141032636835334,
  "compression_ratio": 1.8894230769230769, "no_speech_prob": 0.0034279569517821074},
  {"id": 550, "seek": 334166, "start": 3347.98, "end": 3354.54, "text": " specific
  terms posting list so the posting list is just the array of dock IDs so they would
  put", "tokens": [50680, 2685, 2115, 15978, 1329, 370, 264, 15978, 1329, 307, 445,
  264, 10225, 295, 20929, 48212, 370, 436, 576, 829, 51008], "temperature": 0.0, "avg_logprob":
  -0.1141032636835334, "compression_ratio": 1.8894230769230769, "no_speech_prob":
  0.0034279569517821074}, {"id": 551, "seek": 334166, "start": 3354.54, "end": 3362.2999999999997,
  "text": " that Twitter tweets dock ID in the end and as the new searcher comes in
  searching tweets they would", "tokens": [51008, 300, 5794, 25671, 20929, 7348, 294,
  264, 917, 293, 382, 264, 777, 3164, 260, 1487, 294, 10808, 25671, 436, 576, 51396],
  "temperature": 0.0, "avg_logprob": -0.1141032636835334, "compression_ratio": 1.8894230769230769,
  "no_speech_prob": 0.0034279569517821074}, {"id": 552, "seek": 334166, "start": 3362.2999999999997,
  "end": 3369.3399999999997, "text": " read backwards from the end they wouldn''t
  read from the beginning of so basically what they did is", "tokens": [51396, 1401,
  12204, 490, 264, 917, 436, 2759, 380, 1401, 490, 264, 2863, 295, 370, 1936, 437,
  436, 630, 307, 51748], "temperature": 0.0, "avg_logprob": -0.1141032636835334, "compression_ratio":
  1.8894230769230769, "no_speech_prob": 0.0034279569517821074}, {"id": 553, "seek":
  336934, "start": 3369.34, "end": 3377.1800000000003, "text": " that they kind of
  like encoded the temporal nature of tweets and people what end users wanting to",
  "tokens": [50364, 300, 436, 733, 295, 411, 2058, 12340, 264, 30881, 3687, 295, 25671,
  293, 561, 437, 917, 5022, 7935, 281, 50756], "temperature": 0.0, "avg_logprob":
  -0.1760385943130708, "compression_ratio": 1.6954022988505748, "no_speech_prob":
  0.0023509797174483538}, {"id": 554, "seek": 336934, "start": 3377.1800000000003,
  "end": 3382.1400000000003, "text": " search and view the tweets which are the most
  fresh so like like I don''t know if like you are the", "tokens": [50756, 3164, 293,
  1910, 264, 25671, 597, 366, 264, 881, 4451, 370, 411, 411, 286, 500, 380, 458, 498,
  411, 291, 366, 264, 51004], "temperature": 0.0, "avg_logprob": -0.1760385943130708,
  "compression_ratio": 1.6954022988505748, "no_speech_prob": 0.0023509797174483538},
  {"id": 555, "seek": 336934, "start": 3382.1400000000003, "end": 3393.02, "text":
  " heavy user of Twitter I do you know like on Twitter like when I log in and I check
  my timeline like", "tokens": [51004, 4676, 4195, 295, 5794, 286, 360, 291, 458,
  411, 322, 5794, 411, 562, 286, 3565, 294, 293, 286, 1520, 452, 12933, 411, 51548],
  "temperature": 0.0, "avg_logprob": -0.1760385943130708, "compression_ratio": 1.6954022988505748,
  "no_speech_prob": 0.0023509797174483538}, {"id": 556, "seek": 339302, "start": 3393.02,
  "end": 3399.66, "text": " usually I see something super fresh and then I keep scrolling
  but like not like anti-props to", "tokens": [50364, 2673, 286, 536, 746, 1687, 4451,
  293, 550, 286, 1066, 29053, 457, 411, 406, 411, 6061, 12, 4318, 1878, 281, 50696],
  "temperature": 0.0, "avg_logprob": -0.10612969813139542, "compression_ratio": 1.6885964912280702,
  "no_speech_prob": 0.003580134827643633}, {"id": 557, "seek": 339302, "start": 3399.66,
  "end": 3404.94, "text": " Twitter but it''s it''s a nightmare to search on Twitter
  like when I search something I know existed", "tokens": [50696, 5794, 457, 309,
  311, 309, 311, 257, 18724, 281, 3164, 322, 5794, 411, 562, 286, 3164, 746, 286,
  458, 13135, 50960], "temperature": 0.0, "avg_logprob": -0.10612969813139542, "compression_ratio":
  1.6885964912280702, "no_speech_prob": 0.003580134827643633}, {"id": 558, "seek":
  339302, "start": 3404.94, "end": 3413.18, "text": " like a week ago there is no
  way for me to find it unless I know the exact tweet ID right and so at", "tokens":
  [50960, 411, 257, 1243, 2057, 456, 307, 572, 636, 337, 385, 281, 915, 309, 5969,
  286, 458, 264, 1900, 15258, 7348, 558, 293, 370, 412, 51372], "temperature": 0.0,
  "avg_logprob": -0.10612969813139542, "compression_ratio": 1.6885964912280702, "no_speech_prob":
  0.003580134827643633}, {"id": 559, "seek": 339302, "start": 3413.18, "end": 3419.18,
  "text": " some point I was even indexing tweets actually direct messages I had with
  few people you know", "tokens": [51372, 512, 935, 286, 390, 754, 8186, 278, 25671,
  767, 2047, 7897, 286, 632, 365, 1326, 561, 291, 458, 51672], "temperature": 0.0,
  "avg_logprob": -0.10612969813139542, "compression_ratio": 1.6885964912280702, "no_speech_prob":
  0.003580134827643633}, {"id": 560, "seek": 341918, "start": 3419.5, "end": 3426.8599999999997,
  "text": " in solar and then basically searching them so because it was way faster
  than searching them on", "tokens": [50380, 294, 7936, 293, 550, 1936, 10808, 552,
  370, 570, 309, 390, 636, 4663, 813, 10808, 552, 322, 50748], "temperature": 0.0,
  "avg_logprob": -0.10192070450893669, "compression_ratio": 1.7217391304347827, "no_speech_prob":
  0.006082917097955942}, {"id": 561, "seek": 341918, "start": 3426.8599999999997,
  "end": 3432.94, "text": " Twitter because like if you have 5,000 direct messages
  scrolling through them will take half a day", "tokens": [50748, 5794, 570, 411,
  498, 291, 362, 1025, 11, 1360, 2047, 7897, 29053, 807, 552, 486, 747, 1922, 257,
  786, 51052], "temperature": 0.0, "avg_logprob": -0.10192070450893669, "compression_ratio":
  1.7217391304347827, "no_speech_prob": 0.006082917097955942}, {"id": 562, "seek":
  341918, "start": 3432.94, "end": 3437.74, "text": " so because they keep loading
  and loading so basically what I''m trying to say is that they optimize the", "tokens":
  [51052, 370, 570, 436, 1066, 15114, 293, 15114, 370, 1936, 437, 286, 478, 1382,
  281, 584, 307, 300, 436, 19719, 264, 51292], "temperature": 0.0, "avg_logprob":
  -0.10192070450893669, "compression_ratio": 1.7217391304347827, "no_speech_prob":
  0.006082917097955942}, {"id": 563, "seek": 341918, "start": 3437.74, "end": 3443.98,
  "text": " data structure for the nature of usage of Twitter in such a way that they
  bias to the recent tweets", "tokens": [51292, 1412, 3877, 337, 264, 3687, 295, 14924,
  295, 5794, 294, 1270, 257, 636, 300, 436, 12577, 281, 264, 5162, 25671, 51604],
  "temperature": 0.0, "avg_logprob": -0.10192070450893669, "compression_ratio": 1.7217391304347827,
  "no_speech_prob": 0.006082917097955942}, {"id": 564, "seek": 344398, "start": 3443.98,
  "end": 3450.78, "text": " and they don''t care if you will have to spend a day retrieving
  like super all tweet like it''s", "tokens": [50364, 293, 436, 500, 380, 1127, 498,
  291, 486, 362, 281, 3496, 257, 786, 19817, 798, 411, 1687, 439, 15258, 411, 309,
  311, 50704], "temperature": 0.0, "avg_logprob": -0.15530645030818574, "compression_ratio":
  1.6132596685082874, "no_speech_prob": 0.0012151519767940044}, {"id": 565, "seek":
  344398, "start": 3450.78, "end": 3457.26, "text": " like so my new user use case
  for them for the majority of users 99% of users will only want to see", "tokens":
  [50704, 411, 370, 452, 777, 4195, 764, 1389, 337, 552, 337, 264, 6286, 295, 5022,
  11803, 4, 295, 5022, 486, 787, 528, 281, 536, 51028], "temperature": 0.0, "avg_logprob":
  -0.15530645030818574, "compression_ratio": 1.6132596685082874, "no_speech_prob":
  0.0012151519767940044}, {"id": 566, "seek": 344398, "start": 3457.26, "end": 3465.1,
  "text": " and consume the latest thing so in some sense this is kind of the effect
  of optimizing to the usage", "tokens": [51028, 293, 14732, 264, 6792, 551, 370,
  294, 512, 2020, 341, 307, 733, 295, 264, 1802, 295, 40425, 281, 264, 14924, 51420],
  "temperature": 0.0, "avg_logprob": -0.15530645030818574, "compression_ratio": 1.6132596685082874,
  "no_speech_prob": 0.0012151519767940044}, {"id": 567, "seek": 346510, "start": 3465.3399999999997,
  "end": 3474.46, "text": " like what you say we could optimize you know like split
  or or similar you know sparse lllm or something", "tokens": [50376, 411, 437, 291,
  584, 321, 727, 19719, 291, 458, 411, 7472, 420, 420, 2531, 291, 458, 637, 11668,
  287, 285, 76, 420, 746, 50832], "temperature": 0.0, "avg_logprob": -0.16317145029703775,
  "compression_ratio": 1.7085714285714286, "no_speech_prob": 0.030532527714967728},
  {"id": 568, "seek": 346510, "start": 3475.18, "end": 3482.86, "text": " to kind
  of like learn you know that latest beat and maybe there is a high chance of it being",
  "tokens": [50868, 281, 733, 295, 411, 1466, 291, 458, 300, 6792, 4224, 293, 1310,
  456, 307, 257, 1090, 2931, 295, 309, 885, 51252], "temperature": 0.0, "avg_logprob":
  -0.16317145029703775, "compression_ratio": 1.7085714285714286, "no_speech_prob":
  0.030532527714967728}, {"id": 569, "seek": 346510, "start": 3482.86, "end": 3488.38,
  "text": " retrieved as well so we might as well bias the system to that but then
  of course there is catastrophic", "tokens": [51252, 19817, 937, 382, 731, 370, 321,
  1062, 382, 731, 12577, 264, 1185, 281, 300, 457, 550, 295, 1164, 456, 307, 34915,
  51528], "temperature": 0.0, "avg_logprob": -0.16317145029703775, "compression_ratio":
  1.7085714285714286, "no_speech_prob": 0.030532527714967728}, {"id": 570, "seek":
  348838, "start": 3488.38, "end": 3497.1800000000003, "text": " forgetting thing
  and stuff like that. Yeah there''s no is yes not an easy problem to continually
  update", "tokens": [50364, 25428, 551, 293, 1507, 411, 300, 13, 865, 456, 311, 572,
  307, 2086, 406, 364, 1858, 1154, 281, 22277, 5623, 50804], "temperature": 0.0, "avg_logprob":
  -0.22320730968188213, "compression_ratio": 1.7456140350877194, "no_speech_prob":
  0.03158165514469147}, {"id": 571, "seek": 348838, "start": 3497.1800000000003, "end":
  3503.02, "text": " the mlm head either it would be maybe worth adding that this
  mlm head insplay doesn''t need to be like", "tokens": [50804, 264, 23271, 76, 1378,
  2139, 309, 576, 312, 1310, 3163, 5127, 300, 341, 23271, 76, 1378, 1028, 2858, 1177,
  380, 643, 281, 312, 411, 51096], "temperature": 0.0, "avg_logprob": -0.22320730968188213,
  "compression_ratio": 1.7456140350877194, "no_speech_prob": 0.03158165514469147},
  {"id": 572, "seek": 348838, "start": 3503.02, "end": 3508.78, "text": " a billion
  parameters well maybe a billion would be good but it doesn''t need to be a hundred
  billion", "tokens": [51096, 257, 5218, 9834, 731, 1310, 257, 5218, 576, 312, 665,
  457, 309, 1177, 380, 643, 281, 312, 257, 3262, 5218, 51384], "temperature": 0.0,
  "avg_logprob": -0.22320730968188213, "compression_ratio": 1.7456140350877194, "no_speech_prob":
  0.03158165514469147}, {"id": 573, "seek": 348838, "start": 3508.78, "end": 3513.42,
  "text": " or like yeah that''s such a fascinating nugget of system design you just
  shared at the Twitter", "tokens": [51384, 420, 411, 1338, 300, 311, 1270, 257, 10343,
  30279, 847, 295, 1185, 1715, 291, 445, 5507, 412, 264, 5794, 51616], "temperature":
  0.0, "avg_logprob": -0.22320730968188213, "compression_ratio": 1.7456140350877194,
  "no_speech_prob": 0.03158165514469147}, {"id": 574, "seek": 351342, "start": 3513.82,
  "end": 3519.7400000000002, "text": " thing and yeah it''s really interesting I''ve
  seen this other company called perplexity AI that", "tokens": [50384, 551, 293,
  1338, 309, 311, 534, 1880, 286, 600, 1612, 341, 661, 2237, 1219, 680, 18945, 507,
  7318, 300, 50680], "temperature": 0.0, "avg_logprob": -0.23074384706210246, "compression_ratio":
  1.6821428571428572, "no_speech_prob": 0.04397216811776161}, {"id": 575, "seek":
  351342, "start": 3519.7400000000002, "end": 3526.46, "text": " Ravine Shrinivas
  is I think he''s a founder CEO of it and it''s cool because he was he worked on",
  "tokens": [50680, 497, 706, 533, 1160, 12629, 24759, 307, 286, 519, 415, 311, 257,
  14917, 9282, 295, 309, 293, 309, 311, 1627, 570, 415, 390, 415, 2732, 322, 51016],
  "temperature": 0.0, "avg_logprob": -0.23074384706210246, "compression_ratio": 1.6821428571428572,
  "no_speech_prob": 0.04397216811776161}, {"id": 576, "seek": 351342, "start": 3526.46,
  "end": 3531.58, "text": " curl with Peter Rebele on this contrastive representation
  learning for robotics where they''re", "tokens": [51016, 22591, 365, 6508, 1300,
  650, 306, 322, 341, 8712, 488, 10290, 2539, 337, 34145, 689, 436, 434, 51272], "temperature":
  0.0, "avg_logprob": -0.23074384706210246, "compression_ratio": 1.6821428571428572,
  "no_speech_prob": 0.04397216811776161}, {"id": 577, "seek": 351342, "start": 3531.58,
  "end": 3535.98, "text": " you know they''re doing the same kind of idea vector optimization
  to learn a state space for", "tokens": [51272, 291, 458, 436, 434, 884, 264, 912,
  733, 295, 1558, 8062, 19618, 281, 1466, 257, 1785, 1901, 337, 51492], "temperature":
  0.0, "avg_logprob": -0.23074384706210246, "compression_ratio": 1.6821428571428572,
  "no_speech_prob": 0.04397216811776161}, {"id": 578, "seek": 351342, "start": 3535.98,
  "end": 3539.42, "text": " robotic control on so I think it''s really cool that now
  he''s working on the search space too but", "tokens": [51492, 30468, 1969, 322,
  370, 286, 519, 309, 311, 534, 1627, 300, 586, 415, 311, 1364, 322, 264, 3164, 1901,
  886, 457, 51664], "temperature": 0.0, "avg_logprob": -0.23074384706210246, "compression_ratio":
  1.6821428571428572, "no_speech_prob": 0.04397216811776161}, {"id": 579, "seek":
  353942, "start": 3540.2200000000003, "end": 3546.38, "text": " they have it''s like
  the other approach is like natural language to SQL it''s something like that where",
  "tokens": [50404, 436, 362, 309, 311, 411, 264, 661, 3109, 307, 411, 3303, 2856,
  281, 19200, 309, 311, 746, 411, 300, 689, 50712], "temperature": 0.0, "avg_logprob":
  -0.12814520741557026, "compression_ratio": 1.7757847533632287, "no_speech_prob":
  0.002866260940209031}, {"id": 580, "seek": 353942, "start": 3546.38, "end": 3551.82,
  "text": " like instead of and I''m getting a little off topic but it''s like kind
  of related to Twitter and", "tokens": [50712, 411, 2602, 295, 293, 286, 478, 1242,
  257, 707, 766, 4829, 457, 309, 311, 411, 733, 295, 4077, 281, 5794, 293, 50984],
  "temperature": 0.0, "avg_logprob": -0.12814520741557026, "compression_ratio": 1.7757847533632287,
  "no_speech_prob": 0.002866260940209031}, {"id": 581, "seek": 353942, "start": 3551.82,
  "end": 3557.42, "text": " it''s about like putting tweets into you know data stores
  and then parsing natural language queries", "tokens": [50984, 309, 311, 466, 411,
  3372, 25671, 666, 291, 458, 1412, 9512, 293, 550, 21156, 278, 3303, 2856, 24109,
  51264], "temperature": 0.0, "avg_logprob": -0.12814520741557026, "compression_ratio":
  1.7757847533632287, "no_speech_prob": 0.002866260940209031}, {"id": 582, "seek":
  353942, "start": 3557.42, "end": 3563.7400000000002, "text": " into the SQL but
  so that''s like another idea I guess is like you would parse the query yeah I think",
  "tokens": [51264, 666, 264, 19200, 457, 370, 300, 311, 411, 1071, 1558, 286, 2041,
  307, 411, 291, 576, 48377, 264, 14581, 1338, 286, 519, 51580], "temperature": 0.0,
  "avg_logprob": -0.12814520741557026, "compression_ratio": 1.7757847533632287, "no_speech_prob":
  0.002866260940209031}, {"id": 583, "seek": 356374, "start": 3563.74, "end": 3568.9399999999996,
  "text": " I''m already explaining what do you think about that idea like you you
  take the query and you turn", "tokens": [50364, 286, 478, 1217, 13468, 437, 360,
  291, 519, 466, 300, 1558, 411, 291, 291, 747, 264, 14581, 293, 291, 1261, 50624],
  "temperature": 0.0, "avg_logprob": -0.18142625057336056, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.0068636685609817505}, {"id": 584, "seek": 356374, "start": 3568.9399999999996,
  "end": 3576.9399999999996, "text": " it into an SQL query in like that''s it yes
  yes I know what you mean it''s like it''s very similar I", "tokens": [50624, 309,
  666, 364, 19200, 14581, 294, 411, 300, 311, 309, 2086, 2086, 286, 458, 437, 291,
  914, 309, 311, 411, 309, 311, 588, 2531, 286, 51024], "temperature": 0.0, "avg_logprob":
  -0.18142625057336056, "compression_ratio": 1.7399103139013452, "no_speech_prob":
  0.0068636685609817505}, {"id": 585, "seek": 356374, "start": 3576.9399999999996,
  "end": 3585.1, "text": " think deep said did that right so you can or maybe it''s
  opposite I''m not sure but like if you have a", "tokens": [51024, 519, 2452, 848,
  630, 300, 558, 370, 291, 393, 420, 1310, 309, 311, 6182, 286, 478, 406, 988, 457,
  411, 498, 291, 362, 257, 51432], "temperature": 0.0, "avg_logprob": -0.18142625057336056,
  "compression_ratio": 1.7399103139013452, "no_speech_prob": 0.0068636685609817505},
  {"id": 586, "seek": 356374, "start": 3586.4599999999996, "end": 3592.7, "text":
  " probably the same if you have like a table right you know with fields and rows
  I don''t know", "tokens": [51500, 1391, 264, 912, 498, 291, 362, 411, 257, 3199,
  558, 291, 458, 365, 7909, 293, 13241, 286, 500, 380, 458, 51812], "temperature":
  0.0, "avg_logprob": -0.18142625057336056, "compression_ratio": 1.7399103139013452,
  "no_speech_prob": 0.0068636685609817505}, {"id": 587, "seek": 359270, "start": 3592.7,
  "end": 3600.3799999999997, "text": " let''s say list of mountains with their heights
  and so on so you can actually have a question what", "tokens": [50364, 718, 311,
  584, 1329, 295, 10233, 365, 641, 25930, 293, 370, 322, 370, 291, 393, 767, 362,
  257, 1168, 437, 50748], "temperature": 0.0, "avg_logprob": -0.1367633125998757,
  "compression_ratio": 1.4057971014492754, "no_speech_prob": 0.0006770919426344335},
  {"id": 588, "seek": 359270, "start": 3600.3799999999997, "end": 3608.62, "text":
  " is the tallest mountain in Europe or Asia you could turn that query in natural
  language into SQL", "tokens": [50748, 307, 264, 42075, 6937, 294, 3315, 420, 10038,
  291, 727, 1261, 300, 14581, 294, 3303, 2856, 666, 19200, 51160], "temperature":
  0.0, "avg_logprob": -0.1367633125998757, "compression_ratio": 1.4057971014492754,
  "no_speech_prob": 0.0006770919426344335}, {"id": 589, "seek": 360862, "start": 3608.62,
  "end": 3616.7, "text": " command and say you know select you know mountains from
  this mountains table", "tokens": [50364, 5622, 293, 584, 291, 458, 3048, 291, 458,
  10233, 490, 341, 10233, 3199, 50768], "temperature": 0.0, "avg_logprob": -0.18023523124488625,
  "compression_ratio": 1.4396551724137931, "no_speech_prob": 0.020022448152303696},
  {"id": 590, "seek": 360862, "start": 3619.5, "end": 3630.14, "text": " order by
  height reverse right descending and so I like this idea and in fact actually I''ve",
  "tokens": [50908, 1668, 538, 6681, 9943, 558, 40182, 293, 370, 286, 411, 341, 1558,
  293, 294, 1186, 767, 286, 600, 51440], "temperature": 0.0, "avg_logprob": -0.18023523124488625,
  "compression_ratio": 1.4396551724137931, "no_speech_prob": 0.020022448152303696},
  {"id": 591, "seek": 363014, "start": 3631.1, "end": 3637.98, "text": " I think first
  of all this is already doable right so I''m fine just stood with like with the deep",
  "tokens": [50412, 286, 519, 700, 295, 439, 341, 307, 1217, 41183, 558, 370, 286,
  478, 2489, 445, 9371, 365, 411, 365, 264, 2452, 50756], "temperature": 0.0, "avg_logprob":
  -0.19213569770425054, "compression_ratio": 1.4753086419753085, "no_speech_prob":
  0.003279930679127574}, {"id": 592, "seek": 363014, "start": 3637.98, "end": 3643.74,
  "text": " set doing that in haystack but I also came across this idea", "tokens":
  [50756, 992, 884, 300, 294, 4842, 372, 501, 457, 286, 611, 1361, 2108, 341, 1558,
  51044], "temperature": 0.0, "avg_logprob": -0.19213569770425054, "compression_ratio":
  1.4753086419753085, "no_speech_prob": 0.003279930679127574}, {"id": 593, "seek":
  363014, "start": 3646.94, "end": 3654.7799999999997, "text": " during my PhD research
  because so the problem there I believe was that it was like", "tokens": [51204,
  1830, 452, 14476, 2132, 570, 370, 264, 1154, 456, 286, 1697, 390, 300, 309, 390,
  411, 51596], "temperature": 0.0, "avg_logprob": -0.19213569770425054, "compression_ratio":
  1.4753086419753085, "no_speech_prob": 0.003279930679127574}, {"id": 594, "seek":
  365478, "start": 3655.7400000000002, "end": 3664.78, "text": " these engineers working
  on building aircrafts and so they had to read a ton of manuals", "tokens": [50412,
  613, 11955, 1364, 322, 2390, 9465, 82, 293, 370, 436, 632, 281, 1401, 257, 2952,
  295, 9688, 82, 50864], "temperature": 0.0, "avg_logprob": -0.10964665105265956,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.0014665609924122691},
  {"id": 595, "seek": 365478, "start": 3665.6600000000003, "end": 3671.26, "text":
  " but once you read the manual you still need to go and look up that specific number
  somewhere in", "tokens": [50908, 457, 1564, 291, 1401, 264, 9688, 291, 920, 643,
  281, 352, 293, 574, 493, 300, 2685, 1230, 4079, 294, 51188], "temperature": 0.0,
  "avg_logprob": -0.10964665105265956, "compression_ratio": 1.631578947368421, "no_speech_prob":
  0.0014665609924122691}, {"id": 596, "seek": 365478, "start": 3671.26, "end": 3678.3,
  "text": " the database right so so basically they do like multiple multiple hop
  approach and that may take", "tokens": [51188, 264, 8149, 558, 370, 370, 1936, 436,
  360, 411, 3866, 3866, 3818, 3109, 293, 300, 815, 747, 51540], "temperature": 0.0,
  "avg_logprob": -0.10964665105265956, "compression_ratio": 1.631578947368421, "no_speech_prob":
  0.0014665609924122691}, {"id": 597, "seek": 367830, "start": 3678.38, "end": 3684.86,
  "text": " like forever like you first of all you need to crunch through a ton of
  you know text material and then", "tokens": [50368, 411, 5680, 411, 291, 700, 295,
  439, 291, 643, 281, 13386, 807, 257, 2952, 295, 291, 458, 2487, 2527, 293, 550,
  50692], "temperature": 0.0, "avg_logprob": -0.0821292241414388, "compression_ratio":
  1.720524017467249, "no_speech_prob": 0.0033134587574750185}, {"id": 598, "seek":
  367830, "start": 3684.86, "end": 3689.6600000000003, "text": " somehow summarize
  it and then okay now I need to go and look up that that number in the database",
  "tokens": [50692, 6063, 20858, 309, 293, 550, 1392, 586, 286, 643, 281, 352, 293,
  574, 493, 300, 300, 1230, 294, 264, 8149, 50932], "temperature": 0.0, "avg_logprob":
  -0.0821292241414388, "compression_ratio": 1.720524017467249, "no_speech_prob": 0.0033134587574750185},
  {"id": 599, "seek": 367830, "start": 3689.6600000000003, "end": 3697.42, "text":
  " but what if you could ask a natural language question to the manuals then convert
  that to a SQL", "tokens": [50932, 457, 437, 498, 291, 727, 1029, 257, 3303, 2856,
  1168, 281, 264, 9688, 82, 550, 7620, 300, 281, 257, 19200, 51320], "temperature":
  0.0, "avg_logprob": -0.0821292241414388, "compression_ratio": 1.720524017467249,
  "no_speech_prob": 0.0033134587574750185}, {"id": 600, "seek": 367830, "start": 3697.42,
  "end": 3703.5, "text": " command which would know to go and look up in that specific
  database table and give you the answer", "tokens": [51320, 5622, 597, 576, 458,
  281, 352, 293, 574, 493, 294, 300, 2685, 8149, 3199, 293, 976, 291, 264, 1867, 51624],
  "temperature": 0.0, "avg_logprob": -0.0821292241414388, "compression_ratio": 1.720524017467249,
  "no_speech_prob": 0.0033134587574750185}, {"id": 601, "seek": 370350, "start": 3703.5,
  "end": 3707.26, "text": " so like the manual doesn''t have it but it has some instructions
  how to find it", "tokens": [50364, 370, 411, 264, 9688, 1177, 380, 362, 309, 457,
  309, 575, 512, 9415, 577, 281, 915, 309, 50552], "temperature": 0.0, "avg_logprob":
  -0.14709170452960127, "compression_ratio": 1.6443298969072164, "no_speech_prob":
  0.004668624140322208}, {"id": 602, "seek": 370350, "start": 3708.06, "end": 3713.42,
  "text": " and then you would kind of like convert that into through this metal language
  convert that into", "tokens": [50592, 293, 550, 291, 576, 733, 295, 411, 7620, 300,
  666, 807, 341, 5760, 2856, 7620, 300, 666, 50860], "temperature": 0.0, "avg_logprob":
  -0.14709170452960127, "compression_ratio": 1.6443298969072164, "no_speech_prob":
  0.004668624140322208}, {"id": 603, "seek": 370350, "start": 3713.42, "end": 3720.62,
  "text": " SQL and then get that answer right and this was like pre-dense retrieval
  in era obviously", "tokens": [50860, 19200, 293, 550, 483, 300, 1867, 558, 293,
  341, 390, 411, 659, 12, 67, 1288, 19817, 3337, 294, 4249, 2745, 51220], "temperature":
  0.0, "avg_logprob": -0.14709170452960127, "compression_ratio": 1.6443298969072164,
  "no_speech_prob": 0.004668624140322208}, {"id": 604, "seek": 370350, "start": 3720.62,
  "end": 3724.38, "text": " but I think I still feel like it has the merit to like",
  "tokens": [51220, 457, 286, 519, 286, 920, 841, 411, 309, 575, 264, 24527, 281,
  411, 51408], "temperature": 0.0, "avg_logprob": -0.14709170452960127, "compression_ratio":
  1.6443298969072164, "no_speech_prob": 0.004668624140322208}, {"id": 605, "seek":
  372438, "start": 3724.54, "end": 3735.9, "text": " well I guess two things I think
  first there''s this problem where you search like for error line manual", "tokens":
  [50372, 731, 286, 2041, 732, 721, 286, 519, 700, 456, 311, 341, 1154, 689, 291,
  3164, 411, 337, 6713, 1622, 9688, 50940], "temperature": 0.0, "avg_logprob": -0.1503126621246338,
  "compression_ratio": 1.730593607305936, "no_speech_prob": 0.012029404751956463},
  {"id": 606, "seek": 372438, "start": 3735.9, "end": 3741.9, "text": " some specific
  detail and it''s like in result seven like it almost got it like it''s not like",
  "tokens": [50940, 512, 2685, 2607, 293, 309, 311, 411, 294, 1874, 3407, 411, 309,
  1920, 658, 309, 411, 309, 311, 406, 411, 51240], "temperature": 0.0, "avg_logprob":
  -0.1503126621246338, "compression_ratio": 1.730593607305936, "no_speech_prob": 0.012029404751956463},
  {"id": 607, "seek": 372438, "start": 3741.9, "end": 3747.34, "text": " not in the
  top 100 but it''s seven and to that problem is where I think this GPT index", "tokens":
  [51240, 406, 294, 264, 1192, 2319, 457, 309, 311, 3407, 293, 281, 300, 1154, 307,
  689, 286, 519, 341, 26039, 51, 8186, 51512], "temperature": 0.0, "avg_logprob":
  -0.1503126621246338, "compression_ratio": 1.730593607305936, "no_speech_prob": 0.012029404751956463},
  {"id": 608, "seek": 372438, "start": 3748.38, "end": 3753.42, "text": " like recursive
  summarization or create and refine summarization I think that''ll solve that problem",
  "tokens": [51564, 411, 20560, 488, 14611, 2144, 420, 1884, 293, 33906, 14611, 2144,
  286, 519, 300, 603, 5039, 300, 1154, 51816], "temperature": 0.0, "avg_logprob":
  -0.1503126621246338, "compression_ratio": 1.730593607305936, "no_speech_prob": 0.012029404751956463},
  {"id": 609, "seek": 375438, "start": 3755.1, "end": 3760.2200000000003, "text":
  " and yeah well so I then coming back to this idea of natural language to SQL and
  like structured", "tokens": [50400, 293, 1338, 731, 370, 286, 550, 1348, 646, 281,
  341, 1558, 295, 3303, 2856, 281, 19200, 293, 411, 18519, 50656], "temperature":
  0.0, "avg_logprob": -0.0855837253609089, "compression_ratio": 1.8653061224489795,
  "no_speech_prob": 0.001480748294852674}, {"id": 610, "seek": 375438, "start": 3760.2200000000003,
  "end": 3765.5, "text": " unstructured data on the other end you can also parse the
  tables into text and so I''ve seen that", "tokens": [50656, 18799, 46847, 1412,
  322, 264, 661, 917, 291, 393, 611, 48377, 264, 8020, 666, 2487, 293, 370, 286, 600,
  1612, 300, 50920], "temperature": 0.0, "avg_logprob": -0.0855837253609089, "compression_ratio":
  1.8653061224489795, "no_speech_prob": 0.001480748294852674}, {"id": 611, "seek":
  375438, "start": 3765.5, "end": 3771.42, "text": " done too there''s like wiki tables
  to text and so me personally my favorite application is", "tokens": [50920, 1096,
  886, 456, 311, 411, 261, 9850, 8020, 281, 2487, 293, 370, 385, 5665, 452, 2954,
  3861, 307, 51216], "temperature": 0.0, "avg_logprob": -0.0855837253609089, "compression_ratio":
  1.8653061224489795, "no_speech_prob": 0.001480748294852674}, {"id": 612, "seek":
  375438, "start": 3772.2200000000003, "end": 3775.5, "text": " is scientific literature
  mining and searching through scientific papers and so", "tokens": [51256, 307, 8134,
  10394, 15512, 293, 10808, 807, 8134, 10577, 293, 370, 51420], "temperature": 0.0,
  "avg_logprob": -0.0855837253609089, "compression_ratio": 1.8653061224489795, "no_speech_prob":
  0.001480748294852674}, {"id": 613, "seek": 375438, "start": 3776.2200000000003,
  "end": 3782.06, "text": " you could parse out the tables to turn like the results
  tables to turn it into natural language", "tokens": [51456, 291, 727, 48377, 484,
  264, 8020, 281, 1261, 411, 264, 3542, 8020, 281, 1261, 309, 666, 3303, 2856, 51748],
  "temperature": 0.0, "avg_logprob": -0.0855837253609089, "compression_ratio": 1.8653061224489795,
  "no_speech_prob": 0.001480748294852674}, {"id": 614, "seek": 378206, "start": 3782.14,
  "end": 3786.2999999999997, "text": " and I mean there''s so many fascinating things
  so it''s like with a knowledge let''s say like a", "tokens": [50368, 293, 286, 914,
  456, 311, 370, 867, 10343, 721, 370, 309, 311, 411, 365, 257, 3601, 718, 311, 584,
  411, 257, 50576], "temperature": 0.0, "avg_logprob": -0.14234181876494506, "compression_ratio":
  1.7898832684824904, "no_speech_prob": 0.002435698639601469}, {"id": 615, "seek":
  378206, "start": 3786.2999999999997, "end": 3791.74, "text": " knowledge graph the
  idea of the knowledge graph is if I have Demetri Khan host the vector", "tokens":
  [50576, 3601, 4295, 264, 1558, 295, 264, 3601, 4295, 307, 498, 286, 362, 4686, 302,
  470, 18136, 3975, 264, 8062, 50848], "temperature": 0.0, "avg_logprob": -0.14234181876494506,
  "compression_ratio": 1.7898832684824904, "no_speech_prob": 0.002435698639601469},
  {"id": 616, "seek": 378206, "start": 3791.74, "end": 3798.14, "text": " podcast
  is a product manager at Tom Tom I with knowledge graph I can you know I compress
  the", "tokens": [50848, 7367, 307, 257, 1674, 6598, 412, 5041, 5041, 286, 365, 3601,
  4295, 286, 393, 291, 458, 286, 14778, 264, 51168], "temperature": 0.0, "avg_logprob":
  -0.14234181876494506, "compression_ratio": 1.7898832684824904, "no_speech_prob":
  0.002435698639601469}, {"id": 617, "seek": 378206, "start": 3798.14, "end": 3803.82,
  "text": " representation of all these facts into one structure compared to having
  the set of sentences", "tokens": [51168, 10290, 295, 439, 613, 9130, 666, 472, 3877,
  5347, 281, 1419, 264, 992, 295, 16579, 51452], "temperature": 0.0, "avg_logprob":
  -0.14234181876494506, "compression_ratio": 1.7898832684824904, "no_speech_prob":
  0.002435698639601469}, {"id": 618, "seek": 378206, "start": 3803.82, "end": 3810.7799999999997,
  "text": " right and yeah so maybe if I can kind of plug something I''ve done so
  I have this paper that", "tokens": [51452, 558, 293, 1338, 370, 1310, 498, 286,
  393, 733, 295, 5452, 746, 286, 600, 1096, 370, 286, 362, 341, 3035, 300, 51800],
  "temperature": 0.0, "avg_logprob": -0.14234181876494506, "compression_ratio": 1.7898832684824904,
  "no_speech_prob": 0.002435698639601469}, {"id": 619, "seek": 381078, "start": 3810.78,
  "end": 3817.1800000000003, "text": " will be published pretty soon it''s about it''s
  in the Florida Atlantic University PhD it''s an", "tokens": [50364, 486, 312, 6572,
  1238, 2321, 309, 311, 466, 309, 311, 294, 264, 9117, 20233, 3535, 14476, 309, 311,
  364, 50684], "temperature": 0.0, "avg_logprob": -0.09633703685942151, "compression_ratio":
  1.6091205211726385, "no_speech_prob": 0.0012176918098703027}, {"id": 620, "seek":
  381078, "start": 3817.1800000000003, "end": 3821.82, "text": " interdisciplinary
  team with the College of Nursing and a local healthcare system so we have electronic",
  "tokens": [50684, 38280, 1469, 365, 264, 6745, 295, 42655, 293, 257, 2654, 8884,
  1185, 370, 321, 362, 10092, 50916], "temperature": 0.0, "avg_logprob": -0.09633703685942151,
  "compression_ratio": 1.6091205211726385, "no_speech_prob": 0.0012176918098703027},
  {"id": 621, "seek": 381078, "start": 3821.82, "end": 3827.02, "text": " health records
  that describe COVID-19 patients and we''re trying to predict survival outcome treatment",
  "tokens": [50916, 1585, 7724, 300, 6786, 4566, 12, 3405, 4209, 293, 321, 434, 1382,
  281, 6069, 12559, 9700, 5032, 51176], "temperature": 0.0, "avg_logprob": -0.09633703685942151,
  "compression_ratio": 1.6091205211726385, "no_speech_prob": 0.0012176918098703027},
  {"id": 622, "seek": 381078, "start": 3827.02, "end": 3833.1800000000003, "text":
  " forecasting prognosis all that kind of stuff and so the the thing that we explored
  in this paper is", "tokens": [51176, 44331, 447, 4568, 8211, 439, 300, 733, 295,
  1507, 293, 370, 264, 264, 551, 300, 321, 24016, 294, 341, 3035, 307, 51484], "temperature":
  0.0, "avg_logprob": -0.09633703685942151, "compression_ratio": 1.6091205211726385,
  "no_speech_prob": 0.0012176918098703027}, {"id": 623, "seek": 381078, "start": 3833.1800000000003,
  "end": 3837.82, "text": " let''s switch from the structured tabular data to parsing
  it into natural language text and let''s", "tokens": [51484, 718, 311, 3679, 490,
  264, 18519, 4421, 1040, 1412, 281, 21156, 278, 309, 666, 3303, 2856, 2487, 293,
  718, 311, 51716], "temperature": 0.0, "avg_logprob": -0.09633703685942151, "compression_ratio":
  1.6091205211726385, "no_speech_prob": 0.0012176918098703027}, {"id": 624, "seek":
  383782, "start": 3837.82, "end": 3842.6200000000003, "text": " turn it into like
  clinical narratives or let''s do this thing where you do if X if feature name",
  "tokens": [50364, 1261, 309, 666, 411, 9115, 28016, 420, 718, 311, 360, 341, 551,
  689, 291, 360, 498, 1783, 498, 4111, 1315, 50604], "temperature": 0.0, "avg_logprob":
  -0.16866170528323152, "compression_ratio": 1.6725663716814159, "no_speech_prob":
  0.0018300743540748954}, {"id": 625, "seek": 383782, "start": 3842.6200000000003,
  "end": 3848.86, "text": " equals if feature name equals then label right yeah so
  there''s a paper from the University of", "tokens": [50604, 6915, 498, 4111, 1315,
  6915, 550, 7645, 558, 1338, 370, 456, 311, 257, 3035, 490, 264, 3535, 295, 50916],
  "temperature": 0.0, "avg_logprob": -0.16866170528323152, "compression_ratio": 1.6725663716814159,
  "no_speech_prob": 0.0018300743540748954}, {"id": 626, "seek": 383782, "start": 3848.86,
  "end": 3854.06, "text": " Wisconsin called language interface fine tuning where
  they do that same idea but it''s you know like", "tokens": [50916, 17977, 1219,
  2856, 9226, 2489, 15164, 689, 436, 360, 300, 912, 1558, 457, 309, 311, 291, 458,
  411, 51176], "temperature": 0.0, "avg_logprob": -0.16866170528323152, "compression_ratio":
  1.6725663716814159, "no_speech_prob": 0.0018300743540748954}, {"id": 627, "seek":
  383782, "start": 3854.06, "end": 3859.34, "text": " the UCI machine learning repository
  data sets so so I think I know that I''ve taken like a", "tokens": [51176, 264,
  14079, 40, 3479, 2539, 25841, 1412, 6352, 370, 370, 286, 519, 286, 458, 300, 286,
  600, 2726, 411, 257, 51440], "temperature": 0.0, "avg_logprob": -0.16866170528323152,
  "compression_ratio": 1.6725663716814159, "no_speech_prob": 0.0018300743540748954},
  {"id": 628, "seek": 385934, "start": 3860.3, "end": 3865.9, "text": " walker and
  also to think it''s cool it''s cool I''m sure now listeners will be like what",
  "tokens": [50412, 1792, 260, 293, 611, 281, 519, 309, 311, 1627, 309, 311, 1627,
  286, 478, 988, 586, 23274, 486, 312, 411, 437, 50692], "temperature": 0.0, "avg_logprob":
  -0.23830837899066032, "compression_ratio": 1.7096774193548387, "no_speech_prob":
  0.00744063314050436}, {"id": 629, "seek": 385934, "start": 3867.58, "end": 3874.54,
  "text": " but I know like it''s it''s also what I heard from my listeners for example
  in the podcast is that", "tokens": [50776, 457, 286, 458, 411, 309, 311, 309, 311,
  611, 437, 286, 2198, 490, 452, 23274, 337, 1365, 294, 264, 7367, 307, 300, 51124],
  "temperature": 0.0, "avg_logprob": -0.23830837899066032, "compression_ratio": 1.7096774193548387,
  "no_speech_prob": 0.00744063314050436}, {"id": 630, "seek": 385934, "start": 3874.54,
  "end": 3880.94, "text": " they actually do use this episode as an educational material
  so that''s why you know if we can", "tokens": [51124, 436, 767, 360, 764, 341, 3500,
  382, 364, 10189, 2527, 370, 300, 311, 983, 291, 458, 498, 321, 393, 51444], "temperature":
  0.0, "avg_logprob": -0.23830837899066032, "compression_ratio": 1.7096774193548387,
  "no_speech_prob": 0.00744063314050436}, {"id": 631, "seek": 385934, "start": 3880.94,
  "end": 3888.1400000000003, "text": " stuff as many links to papers and your work
  they can go and study this yeah go go go I do some", "tokens": [51444, 1507, 382,
  867, 6123, 281, 10577, 293, 428, 589, 436, 393, 352, 293, 2979, 341, 1338, 352,
  352, 352, 286, 360, 512, 51804], "temperature": 0.0, "avg_logprob": -0.23830837899066032,
  "compression_ratio": 1.7096774193548387, "no_speech_prob": 0.00744063314050436},
  {"id": 632, "seek": 388814, "start": 3888.14, "end": 3892.06, "text": " rise I guess
  the question is like how are we thinking about structured and unstructured data",
  "tokens": [50364, 6272, 286, 2041, 264, 1168, 307, 411, 577, 366, 321, 1953, 466,
  18519, 293, 18799, 46847, 1412, 50560], "temperature": 0.0, "avg_logprob": -0.09133323838439168,
  "compression_ratio": 1.896551724137931, "no_speech_prob": 0.0011382680386304855},
  {"id": 633, "seek": 388814, "start": 3895.98, "end": 3900.22, "text": " the deep
  learning systems you could parse out the structure into unstructure and then you
  have", "tokens": [50756, 264, 2452, 2539, 3652, 291, 727, 48377, 484, 264, 3877,
  666, 18799, 2885, 293, 550, 291, 362, 50968], "temperature": 0.0, "avg_logprob":
  -0.09133323838439168, "compression_ratio": 1.896551724137931, "no_speech_prob":
  0.0011382680386304855}, {"id": 634, "seek": 388814, "start": 3900.22, "end": 3906.22,
  "text": " the transfer learning is really easy right yeah yes or you can keep the
  structure and then maybe you", "tokens": [50968, 264, 5003, 2539, 307, 534, 1858,
  558, 1338, 2086, 420, 291, 393, 1066, 264, 3877, 293, 550, 1310, 291, 51268], "temperature":
  0.0, "avg_logprob": -0.09133323838439168, "compression_ratio": 1.896551724137931,
  "no_speech_prob": 0.0011382680386304855}, {"id": 635, "seek": 388814, "start": 3906.22,
  "end": 3911.9, "text": " can learn a better representation thanks to the structure
  and with that question my interest has", "tokens": [51268, 393, 1466, 257, 1101,
  10290, 3231, 281, 264, 3877, 293, 365, 300, 1168, 452, 1179, 575, 51552], "temperature":
  0.0, "avg_logprob": -0.09133323838439168, "compression_ratio": 1.896551724137931,
  "no_speech_prob": 0.0011382680386304855}, {"id": 636, "seek": 391190, "start": 3911.9,
  "end": 3919.34, "text": " been really heavily in these causal digs and this idea
  of creating structured causal relationships", "tokens": [50364, 668, 534, 10950,
  294, 613, 38755, 2528, 82, 293, 341, 1558, 295, 4084, 18519, 38755, 6159, 50736],
  "temperature": 0.0, "avg_logprob": -0.12853460533674374, "compression_ratio": 1.7589285714285714,
  "no_speech_prob": 0.0002419095835648477}, {"id": 637, "seek": 391190, "start": 3919.34,
  "end": 3926.06, "text": " between variables I still have no idea how that really
  how you can take like Wikipedia text and turn", "tokens": [50736, 1296, 9102, 286,
  920, 362, 572, 1558, 577, 300, 534, 577, 291, 393, 747, 411, 28999, 2487, 293, 1261,
  51072], "temperature": 0.0, "avg_logprob": -0.12853460533674374, "compression_ratio":
  1.7589285714285714, "no_speech_prob": 0.0002419095835648477}, {"id": 638, "seek":
  391190, "start": 3926.06, "end": 3931.7400000000002, "text": " it into a causal
  diagram but I have an idea of like if and it comes back to this agi versus super",
  "tokens": [51072, 309, 666, 257, 38755, 10686, 457, 286, 362, 364, 1558, 295, 411,
  498, 293, 309, 1487, 646, 281, 341, 623, 72, 5717, 1687, 51356], "temperature":
  0.0, "avg_logprob": -0.12853460533674374, "compression_ratio": 1.7589285714285714,
  "no_speech_prob": 0.0002419095835648477}, {"id": 639, "seek": 391190, "start": 3931.7400000000002,
  "end": 3937.98, "text": " intelligence idea if I have a super intelligence and it''s
  reading search literature I want it to", "tokens": [51356, 7599, 1558, 498, 286,
  362, 257, 1687, 7599, 293, 309, 311, 3760, 3164, 10394, 286, 528, 309, 281, 51668],
  "temperature": 0.0, "avg_logprob": -0.12853460533674374, "compression_ratio": 1.7589285714285714,
  "no_speech_prob": 0.0002419095835648477}, {"id": 640, "seek": 393798, "start": 3937.98,
  "end": 3944.3, "text": " have some kind of causal diagram of our current model of
  search stuff so like it has some model", "tokens": [50364, 362, 512, 733, 295, 38755,
  10686, 295, 527, 2190, 2316, 295, 3164, 1507, 370, 411, 309, 575, 512, 2316, 50680],
  "temperature": 0.0, "avg_logprob": -0.15768590084342068, "compression_ratio": 1.6652360515021458,
  "no_speech_prob": 0.0013338078279048204}, {"id": 641, "seek": 393798, "start": 3944.3,
  "end": 3950.94, "text": " of how BM25 is index the limitations of it''s blade this
  representation this MLOVs problem it has", "tokens": [50680, 295, 577, 15901, 6074,
  307, 8186, 264, 15705, 295, 309, 311, 10959, 341, 10290, 341, 21601, 46, 53, 82,
  1154, 309, 575, 51012], "temperature": 0.0, "avg_logprob": -0.15768590084342068,
  "compression_ratio": 1.6652360515021458, "no_speech_prob": 0.0013338078279048204},
  {"id": 642, "seek": 393798, "start": 3950.94, "end": 3954.94, "text": " like some
  structured representation of all these problems such that when the new batch of
  archive", "tokens": [51012, 411, 512, 18519, 10290, 295, 439, 613, 2740, 1270, 300,
  562, 264, 777, 15245, 295, 23507, 51212], "temperature": 0.0, "avg_logprob": -0.15768590084342068,
  "compression_ratio": 1.6652360515021458, "no_speech_prob": 0.0013338078279048204},
  {"id": 643, "seek": 393798, "start": 3954.94, "end": 3961.98, "text": " papers or
  tweets you know however the news is coming into it or experiments right it looks
  at its", "tokens": [51212, 10577, 420, 25671, 291, 458, 4461, 264, 2583, 307, 1348,
  666, 309, 420, 12050, 558, 309, 1542, 412, 1080, 51564], "temperature": 0.0, "avg_logprob":
  -0.15768590084342068, "compression_ratio": 1.6652360515021458, "no_speech_prob":
  0.0013338078279048204}, {"id": 644, "seek": 396198, "start": 3961.98, "end": 3967.82,
  "text": " causal diagram to say like this violated my this this claim like because
  that''s the thing you see", "tokens": [50364, 38755, 10686, 281, 584, 411, 341,
  33239, 452, 341, 341, 3932, 411, 570, 300, 311, 264, 551, 291, 536, 50656], "temperature":
  0.0, "avg_logprob": -0.1391257480182479, "compression_ratio": 1.9173228346456692,
  "no_speech_prob": 0.001286407234147191}, {"id": 645, "seek": 396198, "start": 3967.82,
  "end": 3973.5, "text": " a paper like autoregressive models as as search engines
  or you see like what''s the name of that", "tokens": [50656, 257, 3035, 411, 1476,
  418, 3091, 488, 5245, 382, 382, 3164, 12982, 420, 291, 536, 411, 437, 311, 264,
  1315, 295, 300, 50940], "temperature": 0.0, "avg_logprob": -0.1391257480182479,
  "compression_ratio": 1.9173228346456692, "no_speech_prob": 0.001286407234147191},
  {"id": 646, "seek": 396198, "start": 3973.5, "end": 3978.22, "text": " where it''s
  like transformers is a differentiable search index like you see some title like
  that that", "tokens": [50940, 689, 309, 311, 411, 4088, 433, 307, 257, 819, 9364,
  3164, 8186, 411, 291, 536, 512, 4876, 411, 300, 300, 51176], "temperature": 0.0,
  "avg_logprob": -0.1391257480182479, "compression_ratio": 1.9173228346456692, "no_speech_prob":
  0.001286407234147191}, {"id": 647, "seek": 396198, "start": 3978.22, "end": 3983.26,
  "text": " violates your causal diagram of why things are the way they are and that''s
  what like inspires your", "tokens": [51176, 3448, 1024, 428, 38755, 10686, 295,
  983, 721, 366, 264, 636, 436, 366, 293, 300, 311, 437, 411, 32566, 428, 51428],
  "temperature": 0.0, "avg_logprob": -0.1391257480182479, "compression_ratio": 1.9173228346456692,
  "no_speech_prob": 0.001286407234147191}, {"id": 648, "seek": 396198, "start": 3983.26,
  "end": 3990.78, "text": " interest so that''s that particular angle of it is yeah
  yeah I''m not mostly thinking I haven''t", "tokens": [51428, 1179, 370, 300, 311,
  300, 1729, 5802, 295, 309, 307, 1338, 1338, 286, 478, 406, 5240, 1953, 286, 2378,
  380, 51804], "temperature": 0.0, "avg_logprob": -0.1391257480182479, "compression_ratio":
  1.9173228346456692, "no_speech_prob": 0.001286407234147191}, {"id": 649, "seek":
  399078, "start": 3990.78, "end": 3997.9, "text": " explored this topic myself yet
  but so let''s say if you take a language model like bird which was", "tokens": [50364,
  24016, 341, 4829, 2059, 1939, 457, 370, 718, 311, 584, 498, 291, 747, 257, 2856,
  2316, 411, 5255, 597, 390, 50720], "temperature": 0.0, "avg_logprob": -0.09836694929334852,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.0019612188916653395},
  {"id": 650, "seek": 399078, "start": 3997.9, "end": 4006.7000000000003, "text":
  " kind of like you could say statically trained once on Wikipedia or news content
  right but the world", "tokens": [50720, 733, 295, 411, 291, 727, 584, 2219, 984,
  8895, 1564, 322, 28999, 420, 2583, 2701, 558, 457, 264, 1002, 51160], "temperature":
  0.0, "avg_logprob": -0.09836694929334852, "compression_ratio": 1.696969696969697,
  "no_speech_prob": 0.0019612188916653395}, {"id": 651, "seek": 399078, "start": 4006.7000000000003,
  "end": 4013.02, "text": " is changing every single day right your model doesn''t
  so what you could do is that you could", "tokens": [51160, 307, 4473, 633, 2167,
  786, 558, 428, 2316, 1177, 380, 370, 437, 291, 727, 360, 307, 300, 291, 727, 51476],
  "temperature": 0.0, "avg_logprob": -0.09836694929334852, "compression_ratio": 1.696969696969697,
  "no_speech_prob": 0.0019612188916653395}, {"id": 652, "seek": 399078, "start": 4013.02,
  "end": 4020.0600000000004, "text": " introduce knowledge back to the model and I''m
  still like on the on the brisk of kind of exploring this", "tokens": [51476, 5366,
  3601, 646, 281, 264, 2316, 293, 286, 478, 920, 411, 322, 264, 322, 264, 738, 7797,
  295, 733, 295, 12736, 341, 51828], "temperature": 0.0, "avg_logprob": -0.09836694929334852,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.0019612188916653395},
  {"id": 653, "seek": 402006, "start": 4020.06, "end": 4027.02, "text": " I think
  new tremors talked about it recently like how you can incorporate knowledge in the",
  "tokens": [50364, 286, 519, 777, 7813, 830, 2825, 466, 309, 3938, 411, 577, 291,
  393, 16091, 3601, 294, 264, 50712], "temperature": 0.0, "avg_logprob": -0.1502657166446548,
  "compression_ratio": 1.6637554585152838, "no_speech_prob": 0.0011547771282494068},
  {"id": 654, "seek": 402006, "start": 4027.02, "end": 4032.46, "text": " language
  model so for instance what like the way I see this before I even like read this
  paper", "tokens": [50712, 2856, 2316, 370, 337, 5197, 437, 411, 264, 636, 286, 536,
  341, 949, 286, 754, 411, 1401, 341, 3035, 50984], "temperature": 0.0, "avg_logprob":
  -0.1502657166446548, "compression_ratio": 1.6637554585152838, "no_speech_prob":
  0.0011547771282494068}, {"id": 655, "seek": 402006, "start": 4032.46, "end": 4039.2599999999998,
  "text": " so I could probably try to invent reinvent the wheel is that so the language
  model might figure out", "tokens": [50984, 370, 286, 727, 1391, 853, 281, 7962,
  33477, 264, 5589, 307, 300, 370, 264, 2856, 2316, 1062, 2573, 484, 51324], "temperature":
  0.0, "avg_logprob": -0.1502657166446548, "compression_ratio": 1.6637554585152838,
  "no_speech_prob": 0.0011547771282494068}, {"id": 656, "seek": 402006, "start": 4040.14,
  "end": 4045.58, "text": " that the question is about the president of the United
  States that specific one let''s say Obama", "tokens": [51368, 300, 264, 1168, 307,
  466, 264, 3868, 295, 264, 2824, 3040, 300, 2685, 472, 718, 311, 584, 9560, 51640],
  "temperature": 0.0, "avg_logprob": -0.1502657166446548, "compression_ratio": 1.6637554585152838,
  "no_speech_prob": 0.0011547771282494068}, {"id": 657, "seek": 404558, "start": 4045.66,
  "end": 4053.02, "text": " something but then the question is is Obama still the
  president of the United States and so now the", "tokens": [50368, 746, 457, 550,
  264, 1168, 307, 307, 9560, 920, 264, 3868, 295, 264, 2824, 3040, 293, 370, 586,
  264, 50736], "temperature": 0.0, "avg_logprob": -0.18145058606121992, "compression_ratio":
  1.5326633165829147, "no_speech_prob": 0.004877268336713314}, {"id": 658, "seek":
  404558, "start": 4053.02, "end": 4058.54, "text": " language model is kind of like
  hentik app that says well I actually don''t have last I know like chat", "tokens":
  [50736, 2856, 2316, 307, 733, 295, 411, 276, 317, 1035, 724, 300, 1619, 731, 286,
  767, 500, 380, 362, 1036, 286, 458, 411, 5081, 51012], "temperature": 0.0, "avg_logprob":
  -0.18145058606121992, "compression_ratio": 1.5326633165829147, "no_speech_prob":
  0.004877268336713314}, {"id": 659, "seek": 404558, "start": 4058.54, "end": 4067.9,
  "text": " gpd does that right like I was trained by 2021 so I have no idea what
  happened in 2022 sorry goodbye but", "tokens": [51012, 290, 79, 67, 775, 300, 558,
  411, 286, 390, 8895, 538, 7201, 370, 286, 362, 572, 1558, 437, 2011, 294, 20229,
  2597, 12084, 457, 51480], "temperature": 0.0, "avg_logprob": -0.18145058606121992,
  "compression_ratio": 1.5326633165829147, "no_speech_prob": 0.004877268336713314},
  {"id": 660, "seek": 406790, "start": 4067.9, "end": 4075.42, "text": " like it could
  actually say it could say I figured out the context I know roughly what you''re
  asking", "tokens": [50364, 411, 309, 727, 767, 584, 309, 727, 584, 286, 8932, 484,
  264, 4319, 286, 458, 9810, 437, 291, 434, 3365, 50740], "temperature": 0.0, "avg_logprob":
  -0.10059656567043729, "compression_ratio": 1.8714285714285714, "no_speech_prob":
  0.005412782076746225}, {"id": 661, "seek": 406790, "start": 4075.42, "end": 4081.9,
  "text": " this is the person I know this person I know that what what the president
  means I know the the", "tokens": [50740, 341, 307, 264, 954, 286, 458, 341, 954,
  286, 458, 300, 437, 437, 264, 3868, 1355, 286, 458, 264, 264, 51064], "temperature":
  0.0, "avg_logprob": -0.10059656567043729, "compression_ratio": 1.8714285714285714,
  "no_speech_prob": 0.005412782076746225}, {"id": 662, "seek": 406790, "start": 4081.9,
  "end": 4087.26, "text": " country United States but you''re asking me a factual
  question so what it could do is actually it could", "tokens": [51064, 1941, 2824,
  3040, 457, 291, 434, 3365, 385, 257, 48029, 1168, 370, 437, 309, 727, 360, 307,
  767, 309, 727, 51332], "temperature": 0.0, "avg_logprob": -0.10059656567043729,
  "compression_ratio": 1.8714285714285714, "no_speech_prob": 0.005412782076746225},
  {"id": 663, "seek": 406790, "start": 4087.26, "end": 4094.78, "text": " go and ask
  a knowledge graph which is updated without recalculating the the embeddings which
  is", "tokens": [51332, 352, 293, 1029, 257, 3601, 4295, 597, 307, 10588, 1553, 850,
  304, 2444, 990, 264, 264, 12240, 29432, 597, 307, 51708], "temperature": 0.0, "avg_logprob":
  -0.10059656567043729, "compression_ratio": 1.8714285714285714, "no_speech_prob":
  0.005412782076746225}, {"id": 664, "seek": 409478, "start": 4095.5, "end": 4101.18,
  "text": " solving them all of this problem right so it''s it''s it''s another data
  structure you know it''s", "tokens": [50400, 12606, 552, 439, 295, 341, 1154, 558,
  370, 309, 311, 309, 311, 309, 311, 1071, 1412, 3877, 291, 458, 309, 311, 50684],
  "temperature": 0.0, "avg_logprob": -0.1401343510068696, "compression_ratio": 1.8862745098039215,
  "no_speech_prob": 0.006909992545843124}, {"id": 665, "seek": 409478, "start": 4101.18,
  "end": 4109.18, "text": " a knowledge graph it''s being updated as we go and so
  it goes and says hey let''s coming back to your", "tokens": [50684, 257, 3601, 4295,
  309, 311, 885, 10588, 382, 321, 352, 293, 370, 309, 1709, 293, 1619, 4177, 718,
  311, 1348, 646, 281, 428, 51084], "temperature": 0.0, "avg_logprob": -0.1401343510068696,
  "compression_ratio": 1.8862745098039215, "no_speech_prob": 0.006909992545843124},
  {"id": 666, "seek": 409478, "start": 4109.18, "end": 4113.66, "text": " question
  on on structured language like in in graph systems you also need to form your query",
  "tokens": [51084, 1168, 322, 322, 18519, 2856, 411, 294, 294, 4295, 3652, 291, 611,
  643, 281, 1254, 428, 14581, 51308], "temperature": 0.0, "avg_logprob": -0.1401343510068696,
  "compression_ratio": 1.8862745098039215, "no_speech_prob": 0.006909992545843124},
  {"id": 667, "seek": 409478, "start": 4113.66, "end": 4118.7, "text": " in a certain
  way so it forms the query in a certain way and traverses the graph and then checks",
  "tokens": [51308, 294, 257, 1629, 636, 370, 309, 6422, 264, 14581, 294, 257, 1629,
  636, 293, 23149, 279, 264, 4295, 293, 550, 13834, 51560], "temperature": 0.0, "avg_logprob":
  -0.1401343510068696, "compression_ratio": 1.8862745098039215, "no_speech_prob":
  0.006909992545843124}, {"id": 668, "seek": 409478, "start": 4118.7, "end": 4124.22,
  "text": " is Obama the president the answer is no it goes back all the way to maybe
  a language model I don''t", "tokens": [51560, 307, 9560, 264, 3868, 264, 1867, 307,
  572, 309, 1709, 646, 439, 264, 636, 281, 1310, 257, 2856, 2316, 286, 500, 380, 51836],
  "temperature": 0.0, "avg_logprob": -0.1401343510068696, "compression_ratio": 1.8862745098039215,
  "no_speech_prob": 0.006909992545843124}, {"id": 669, "seek": 412422, "start": 4124.22,
  "end": 4129.66, "text": " mean some other layer and basically presents the answer
  to the user right yeah so that''s just one", "tokens": [50364, 914, 512, 661, 4583,
  293, 1936, 13533, 264, 1867, 281, 264, 4195, 558, 1338, 370, 300, 311, 445, 472,
  50636], "temperature": 0.0, "avg_logprob": -0.18993494645604547, "compression_ratio":
  1.6866197183098592, "no_speech_prob": 0.0010349360527470708}, {"id": 670, "seek":
  412422, "start": 4129.66, "end": 4136.860000000001, "text": " thought before even
  dove into this topic of incorporating knowledge in elabs I would probably think",
  "tokens": [50636, 1194, 949, 754, 23287, 666, 341, 4829, 295, 33613, 3601, 294,
  806, 17243, 286, 576, 1391, 519, 50996], "temperature": 0.0, "avg_logprob": -0.18993494645604547,
  "compression_ratio": 1.6866197183098592, "no_speech_prob": 0.0010349360527470708},
  {"id": 671, "seek": 412422, "start": 4136.860000000001, "end": 4143.18, "text":
  " like that yeah I love that you brother that knowledge graph it''s like and that''s
  kind of like", "tokens": [50996, 411, 300, 1338, 286, 959, 300, 291, 3708, 300,
  3601, 4295, 309, 311, 411, 293, 300, 311, 733, 295, 411, 51312], "temperature":
  0.0, "avg_logprob": -0.18993494645604547, "compression_ratio": 1.6866197183098592,
  "no_speech_prob": 0.0010349360527470708}, {"id": 672, "seek": 412422, "start": 4143.18,
  "end": 4147.02, "text": " GBT index as well as laying chain I can''t believe I haven''t
  brought that up until now we can talk", "tokens": [51312, 460, 33853, 8186, 382,
  731, 382, 14903, 5021, 286, 393, 380, 1697, 286, 2378, 380, 3038, 300, 493, 1826,
  586, 321, 393, 751, 51504], "temperature": 0.0, "avg_logprob": -0.18993494645604547,
  "compression_ratio": 1.6866197183098592, "no_speech_prob": 0.0010349360527470708},
  {"id": 673, "seek": 412422, "start": 4147.02, "end": 4150.62, "text": " about that
  more in the neural search frameworks discussion on the review podcast but like",
  "tokens": [51504, 466, 300, 544, 294, 264, 18161, 3164, 29834, 5017, 322, 264, 3131,
  7367, 457, 411, 51684], "temperature": 0.0, "avg_logprob": -0.18993494645604547,
  "compression_ratio": 1.6866197183098592, "no_speech_prob": 0.0010349360527470708},
  {"id": 674, "seek": 415062, "start": 4151.26, "end": 4157.74, "text": " this idea
  of different kinds of external memory and I don''t know what''s wrong with my brain
  today", "tokens": [50396, 341, 1558, 295, 819, 3685, 295, 8320, 4675, 293, 286,
  500, 380, 458, 437, 311, 2085, 365, 452, 3567, 965, 50720], "temperature": 0.0,
  "avg_logprob": -0.18490333557128907, "compression_ratio": 1.7155555555555555, "no_speech_prob":
  0.004891827702522278}, {"id": 675, "seek": 415062, "start": 4157.74, "end": 4163.42,
  "text": " and I keep like branching into completely I don''t think it''s wrong I
  think it''s the right setting", "tokens": [50720, 293, 286, 1066, 411, 9819, 278,
  666, 2584, 286, 500, 380, 519, 309, 311, 2085, 286, 519, 309, 311, 264, 558, 3287,
  51004], "temperature": 0.0, "avg_logprob": -0.18490333557128907, "compression_ratio":
  1.7155555555555555, "no_speech_prob": 0.004891827702522278}, {"id": 676, "seek":
  415062, "start": 4164.14, "end": 4171.98, "text": " it''s just not suitable with
  the coding or something but um like so I was recently talking with", "tokens": [51040,
  309, 311, 445, 406, 12873, 365, 264, 17720, 420, 746, 457, 1105, 411, 370, 286,
  390, 3938, 1417, 365, 51432], "temperature": 0.0, "avg_logprob": -0.18490333557128907,
  "compression_ratio": 1.7155555555555555, "no_speech_prob": 0.004891827702522278},
  {"id": 677, "seek": 415062, "start": 4171.98, "end": 4178.14, "text": " Shukri who
  just joined we''ve got as well about um about this idea of metadata re-ranking so
  one", "tokens": [51432, 1160, 2034, 470, 567, 445, 6869, 321, 600, 658, 382, 731,
  466, 1105, 466, 341, 1558, 295, 26603, 319, 12, 20479, 278, 370, 472, 51740], "temperature":
  0.0, "avg_logprob": -0.18490333557128907, "compression_ratio": 1.7155555555555555,
  "no_speech_prob": 0.004891827702522278}, {"id": 678, "seek": 417814, "start": 4178.14,
  "end": 4183.34, "text": " approach is you have the xg boost re-ranker where you
  take in the bm25 score the vector", "tokens": [50364, 3109, 307, 291, 362, 264,
  2031, 70, 9194, 319, 12, 20479, 260, 689, 291, 747, 294, 264, 272, 76, 6074, 6175,
  264, 8062, 50624], "temperature": 0.0, "avg_logprob": -0.1727287483215332, "compression_ratio":
  1.755868544600939, "no_speech_prob": 0.00125303294043988}, {"id": 679, "seek": 417814,
  "start": 4183.34, "end": 4190.9400000000005, "text": " distance and then also symbolic
  features as the input to the re to the xg boost re-ranker", "tokens": [50624, 4560,
  293, 550, 611, 25755, 4122, 382, 264, 4846, 281, 264, 319, 281, 264, 2031, 70, 9194,
  319, 12, 20479, 260, 51004], "temperature": 0.0, "avg_logprob": -0.1727287483215332,
  "compression_ratio": 1.755868544600939, "no_speech_prob": 0.00125303294043988},
  {"id": 680, "seek": 417814, "start": 4191.900000000001, "end": 4198.62, "text":
  " so the thing he was okay do we want to store this metadata in weveate as well
  or do we go get it", "tokens": [51052, 370, 264, 551, 415, 390, 1392, 360, 321,
  528, 281, 3531, 341, 26603, 294, 321, 303, 473, 382, 731, 420, 360, 321, 352, 483,
  309, 51388], "temperature": 0.0, "avg_logprob": -0.1727287483215332, "compression_ratio":
  1.755868544600939, "no_speech_prob": 0.00125303294043988}, {"id": 681, "seek": 417814,
  "start": 4198.62, "end": 4203.58, "text": " from redis or feature store something
  like that where we get that kind of property and so it''s like", "tokens": [51388,
  490, 2182, 271, 420, 4111, 3531, 746, 411, 300, 689, 321, 483, 300, 733, 295, 4707,
  293, 370, 309, 311, 411, 51636], "temperature": 0.0, "avg_logprob": -0.1727287483215332,
  "compression_ratio": 1.755868544600939, "no_speech_prob": 0.00125303294043988},
  {"id": 682, "seek": 420358, "start": 4203.66, "end": 4208.46, "text": " the knowledge
  graph the idea connects to that because it''s like okay are we going to build",
  "tokens": [50368, 264, 3601, 4295, 264, 1558, 16967, 281, 300, 570, 309, 311, 411,
  1392, 366, 321, 516, 281, 1322, 50608], "temperature": 0.0, "avg_logprob": -0.10494468171717757,
  "compression_ratio": 1.8409090909090908, "no_speech_prob": 0.00548475980758667},
  {"id": 683, "seek": 420358, "start": 4208.46, "end": 4214.0599999999995, "text":
  " the knowledge graph in weveate should it live in weveate or should we plug weveate
  in with something", "tokens": [50608, 264, 3601, 4295, 294, 321, 303, 473, 820,
  309, 1621, 294, 321, 303, 473, 420, 820, 321, 5452, 321, 303, 473, 294, 365, 746,
  50888], "temperature": 0.0, "avg_logprob": -0.10494468171717757, "compression_ratio":
  1.8409090909090908, "no_speech_prob": 0.00548475980758667}, {"id": 684, "seek":
  420358, "start": 4214.0599999999995, "end": 4219.74, "text": " like Neo4j or or
  is it a top level controller like the neural search frameworks thing you''re describing",
  "tokens": [50888, 411, 24458, 19, 73, 420, 420, 307, 309, 257, 1192, 1496, 10561,
  411, 264, 18161, 3164, 29834, 551, 291, 434, 16141, 51172], "temperature": 0.0,
  "avg_logprob": -0.10494468171717757, "compression_ratio": 1.8409090909090908, "no_speech_prob":
  0.00548475980758667}, {"id": 685, "seek": 420358, "start": 4219.74, "end": 4226.38,
  "text": " where it''s you know something that hooks into weveate and hooks into
  Neo4j relational AI tiger", "tokens": [51172, 689, 309, 311, 291, 458, 746, 300,
  26485, 666, 321, 303, 473, 293, 26485, 666, 24458, 19, 73, 38444, 7318, 21432, 51504],
  "temperature": 0.0, "avg_logprob": -0.10494468171717757, "compression_ratio": 1.8409090909090908,
  "no_speech_prob": 0.00548475980758667}, {"id": 686, "seek": 420358, "start": 4226.38,
  "end": 4232.7, "text": " graph I don''t know all the rdf ontology technologies but
  you know like it has separate and it''s", "tokens": [51504, 4295, 286, 500, 380,
  458, 439, 264, 367, 45953, 6592, 1793, 7943, 457, 291, 458, 411, 309, 575, 4994,
  293, 309, 311, 51820], "temperature": 0.0, "avg_logprob": -0.10494468171717757,
  "compression_ratio": 1.8409090909090908, "no_speech_prob": 0.00548475980758667},
  {"id": 687, "seek": 423270, "start": 4232.7, "end": 4237.099999999999, "text": "
  a higher level that picks between the indexes so it''s yeah it''s like what kind
  of technology is", "tokens": [50364, 257, 2946, 1496, 300, 16137, 1296, 264, 8186,
  279, 370, 309, 311, 1338, 309, 311, 411, 437, 733, 295, 2899, 307, 50584], "temperature":
  0.0, "avg_logprob": -0.1382554520008176, "compression_ratio": 1.732394366197183,
  "no_speech_prob": 0.004590496886521578}, {"id": 688, "seek": 423270, "start": 4237.099999999999,
  "end": 4243.74, "text": " built and weveate and that''s not even really up to me
  you know exactly but I think it''s kind of", "tokens": [50584, 3094, 293, 321, 303,
  473, 293, 300, 311, 406, 754, 534, 493, 281, 385, 291, 458, 2293, 457, 286, 519,
  309, 311, 733, 295, 50916], "temperature": 0.0, "avg_logprob": -0.1382554520008176,
  "compression_ratio": 1.732394366197183, "no_speech_prob": 0.004590496886521578},
  {"id": 689, "seek": 423270, "start": 4243.74, "end": 4251.42, "text": " fun to brainstorm
  with you like what like we kind of like intuitively find this limitations", "tokens":
  [50916, 1019, 281, 35245, 365, 291, 411, 437, 411, 321, 733, 295, 411, 46506, 915,
  341, 15705, 51300], "temperature": 0.0, "avg_logprob": -0.1382554520008176, "compression_ratio":
  1.732394366197183, "no_speech_prob": 0.004590496886521578}, {"id": 690, "seek":
  423270, "start": 4251.42, "end": 4256.7, "text": " together and at the same time
  this limitations may lead to future discoveries like on", "tokens": [51300, 1214,
  293, 412, 264, 912, 565, 341, 15705, 815, 1477, 281, 2027, 28400, 411, 322, 51564],
  "temperature": 0.0, "avg_logprob": -0.1382554520008176, "compression_ratio": 1.732394366197183,
  "no_speech_prob": 0.004590496886521578}, {"id": 691, "seek": 425670, "start": 4256.94,
  "end": 4263.9, "text": " engineering and research and like when I was giving this
  keynote at Haystack where by the way", "tokens": [50376, 7043, 293, 2132, 293, 411,
  562, 286, 390, 2902, 341, 33896, 412, 8721, 372, 501, 689, 538, 264, 636, 50724],
  "temperature": 0.0, "avg_logprob": -0.21135190604389578, "compression_ratio": 1.7212121212121212,
  "no_speech_prob": 0.0046159327030181885}, {"id": 692, "seek": 425670, "start": 4263.9,
  "end": 4273.82, "text": " weveate guys will surprise and another guys as well like
  I didn''t I didn''t feel bold enough to", "tokens": [50724, 321, 303, 473, 1074,
  486, 6365, 293, 1071, 1074, 382, 731, 411, 286, 994, 380, 286, 994, 380, 841, 11928,
  1547, 281, 51220], "temperature": 0.0, "avg_logprob": -0.21135190604389578, "compression_ratio":
  1.7212121212121212, "no_speech_prob": 0.0046159327030181885}, {"id": 693, "seek":
  425670, "start": 4273.82, "end": 4280.54, "text": " say this but I think I will
  say this now at least that I feel like engineering and research are", "tokens":
  [51220, 584, 341, 457, 286, 519, 286, 486, 584, 341, 586, 412, 1935, 300, 286, 841,
  411, 7043, 293, 2132, 366, 51556], "temperature": 0.0, "avg_logprob": -0.21135190604389578,
  "compression_ratio": 1.7212121212121212, "no_speech_prob": 0.0046159327030181885},
  {"id": 694, "seek": 428054, "start": 4280.54, "end": 4288.14, "text": " kind of
  like indistinguishable in the amount of intelligent power you need to put into this
  to", "tokens": [50364, 733, 295, 411, 1016, 468, 7050, 742, 712, 294, 264, 2372,
  295, 13232, 1347, 291, 643, 281, 829, 666, 341, 281, 50744], "temperature": 0.0,
  "avg_logprob": -0.10643237760697288, "compression_ratio": 1.6946902654867257, "no_speech_prob":
  0.004193662665784359}, {"id": 695, "seek": 428054, "start": 4288.14, "end": 4294.94,
  "text": " solve it because it''s not like given right like if this data structure
  inverted index is designed", "tokens": [50744, 5039, 309, 570, 309, 311, 406, 411,
  2212, 558, 411, 498, 341, 1412, 3877, 38969, 8186, 307, 4761, 51084], "temperature":
  0.0, "avg_logprob": -0.10643237760697288, "compression_ratio": 1.6946902654867257,
  "no_speech_prob": 0.004193662665784359}, {"id": 696, "seek": 428054, "start": 4294.94,
  "end": 4302.62, "text": " like this and you do have the the issue of early termination
  because you cannot like waste so many", "tokens": [51084, 411, 341, 293, 291, 360,
  362, 264, 264, 2734, 295, 2440, 1433, 2486, 570, 291, 2644, 411, 5964, 370, 867,
  51468], "temperature": 0.0, "avg_logprob": -0.10643237760697288, "compression_ratio":
  1.6946902654867257, "no_speech_prob": 0.004193662665784359}, {"id": 697, "seek":
  428054, "start": 4302.62, "end": 4309.98, "text": " CPU cycles then like okay without
  reading papers can you go and solve it like being just an", "tokens": [51468, 13199,
  17796, 550, 411, 1392, 1553, 3760, 10577, 393, 291, 352, 293, 5039, 309, 411, 885,
  445, 364, 51836], "temperature": 0.0, "avg_logprob": -0.10643237760697288, "compression_ratio":
  1.6946902654867257, "no_speech_prob": 0.004193662665784359}, {"id": 698, "seek":
  430998, "start": 4309.98, "end": 4316.379999999999, "text": " engineer so to say
  no you can''t it''s like it''s it''s super hard like you need to start coming up
  with", "tokens": [50364, 11403, 370, 281, 584, 572, 291, 393, 380, 309, 311, 411,
  309, 311, 309, 311, 1687, 1152, 411, 291, 643, 281, 722, 1348, 493, 365, 50684],
  "temperature": 0.0, "avg_logprob": -0.12398037543663612, "compression_ratio": 1.6896551724137931,
  "no_speech_prob": 0.005147337447851896}, {"id": 699, "seek": 430998, "start": 4316.379999999999,
  "end": 4322.54, "text": " like new vector space model which was invented when in
  60s 70s I don''t know so like can you come", "tokens": [50684, 411, 777, 8062, 1901,
  2316, 597, 390, 14479, 562, 294, 4060, 82, 5285, 82, 286, 500, 380, 458, 370, 411,
  393, 291, 808, 50992], "temperature": 0.0, "avg_logprob": -0.12398037543663612,
  "compression_ratio": 1.6896551724137931, "no_speech_prob": 0.005147337447851896},
  {"id": 700, "seek": 430998, "start": 4322.54, "end": 4330.86, "text": " up with
  like completing your model it''s it''s it''s equally hard as in research when okay
  you know", "tokens": [50992, 493, 365, 411, 19472, 428, 2316, 309, 311, 309, 311,
  309, 311, 12309, 1152, 382, 294, 2132, 562, 1392, 291, 458, 51408], "temperature":
  0.0, "avg_logprob": -0.12398037543663612, "compression_ratio": 1.6896551724137931,
  "no_speech_prob": 0.005147337447851896}, {"id": 701, "seek": 430998, "start": 4330.86,
  "end": 4337.259999999999, "text": " that SOTA is now this can I beat it somehow
  but it''s not like you''re just beating sort of for the", "tokens": [51408, 300,
  318, 5068, 32, 307, 586, 341, 393, 286, 4224, 309, 6063, 457, 309, 311, 406, 411,
  291, 434, 445, 13497, 1333, 295, 337, 264, 51728], "temperature": 0.0, "avg_logprob":
  -0.12398037543663612, "compression_ratio": 1.6896551724137931, "no_speech_prob":
  0.005147337447851896}, {"id": 702, "seek": 433726, "start": 4337.26, "end": 4342.7,
  "text": " sake of it maybe some people do but like I would take a stance of not
  doing that like I would", "tokens": [50364, 9717, 295, 309, 1310, 512, 561, 360,
  457, 411, 286, 576, 747, 257, 21033, 295, 406, 884, 300, 411, 286, 576, 50636],
  "temperature": 0.0, "avg_logprob": -0.09483429693406628, "compression_ratio": 1.7212389380530972,
  "no_speech_prob": 0.004677057731896639}, {"id": 703, "seek": 433726, "start": 4343.42,
  "end": 4348.7, "text": " try to solve an existing problem right so I do want to
  surface as you said more relevant document", "tokens": [50672, 853, 281, 5039, 364,
  6741, 1154, 558, 370, 286, 360, 528, 281, 3753, 382, 291, 848, 544, 7340, 4166,
  50936], "temperature": 0.0, "avg_logprob": -0.09483429693406628, "compression_ratio":
  1.7212389380530972, "no_speech_prob": 0.004677057731896639}, {"id": 704, "seek":
  433726, "start": 4348.7, "end": 4356.3, "text": " to the top or maybe even the passage
  maybe in a number so I keep pushing for that so both of these", "tokens": [50936,
  281, 264, 1192, 420, 1310, 754, 264, 11497, 1310, 294, 257, 1230, 370, 286, 1066,
  7380, 337, 300, 370, 1293, 295, 613, 51316], "temperature": 0.0, "avg_logprob":
  -0.09483429693406628, "compression_ratio": 1.7212389380530972, "no_speech_prob":
  0.004677057731896639}, {"id": 705, "seek": 433726, "start": 4356.3, "end": 4363.5,
  "text": " to me they''re like they require so much intelligence so that they become
  indistinguishable in some", "tokens": [51316, 281, 385, 436, 434, 411, 436, 3651,
  370, 709, 7599, 370, 300, 436, 1813, 1016, 468, 7050, 742, 712, 294, 512, 51676],
  "temperature": 0.0, "avg_logprob": -0.09483429693406628, "compression_ratio": 1.7212389380530972,
  "no_speech_prob": 0.004677057731896639}, {"id": 706, "seek": 436350, "start": 4363.5,
  "end": 4370.06, "text": " sense like what exactly are you now solving the MLOPS
  problem are you solving the you know the", "tokens": [50364, 2020, 411, 437, 2293,
  366, 291, 586, 12606, 264, 21601, 46, 6273, 1154, 366, 291, 12606, 264, 291, 458,
  264, 50692], "temperature": 0.0, "avg_logprob": -0.2587367466517857, "compression_ratio":
  1.7914691943127963, "no_speech_prob": 0.006465723272413015}, {"id": 707, "seek":
  436350, "start": 4370.06, "end": 4375.1, "text": " inverted index data structure
  limitation problem or are you solving how do I retrain the", "tokens": [50692, 38969,
  8186, 1412, 3877, 27432, 1154, 420, 366, 291, 12606, 577, 360, 286, 1533, 7146,
  264, 50944], "temperature": 0.0, "avg_logprob": -0.2587367466517857, "compression_ratio":
  1.7914691943127963, "no_speech_prob": 0.006465723272413015}, {"id": 708, "seek":
  436350, "start": 4375.1, "end": 4380.38, "text": " embeddings how did you train
  the model or fine tune the model and I don''t recompute the embeddings", "tokens":
  [50944, 12240, 29432, 577, 630, 291, 3847, 264, 2316, 420, 2489, 10864, 264, 2316,
  293, 286, 500, 380, 48000, 1169, 264, 12240, 29432, 51208], "temperature": 0.0,
  "avg_logprob": -0.2587367466517857, "compression_ratio": 1.7914691943127963, "no_speech_prob":
  0.006465723272413015}, {"id": 709, "seek": 436350, "start": 4380.38, "end": 4389.26,
  "text": " because it''s a way to expand so it''s to pay the bill yes does it does
  it resonate with you like", "tokens": [51208, 570, 309, 311, 257, 636, 281, 5268,
  370, 309, 311, 281, 1689, 264, 2961, 2086, 775, 309, 775, 309, 34285, 365, 291,
  411, 51652], "temperature": 0.0, "avg_logprob": -0.2587367466517857, "compression_ratio":
  1.7914691943127963, "no_speech_prob": 0.006465723272413015}, {"id": 710, "seek":
  438926, "start": 4389.34, "end": 4395.66, "text": " what what are your thoughts
  of that yeah our ct oeddy and delocca has written about product engineering", "tokens":
  [50368, 437, 437, 366, 428, 4598, 295, 300, 1338, 527, 269, 83, 277, 292, 3173,
  293, 1103, 905, 496, 575, 3720, 466, 1674, 7043, 50684], "temperature": 0.0, "avg_logprob":
  -0.2882191875193379, "compression_ratio": 1.7612612612612613, "no_speech_prob":
  0.017625700682401657}, {"id": 711, "seek": 438926, "start": 4395.66, "end": 4401.18,
  "text": " and like on this meta on this meta of like how do these decisions get
  made and it''s like I think", "tokens": [50684, 293, 411, 322, 341, 19616, 322,
  341, 19616, 295, 411, 577, 360, 613, 5327, 483, 1027, 293, 309, 311, 411, 286, 519,
  50960], "temperature": 0.0, "avg_logprob": -0.2882191875193379, "compression_ratio":
  1.7612612612612613, "no_speech_prob": 0.017625700682401657}, {"id": 712, "seek":
  438926, "start": 4401.18, "end": 4407.9800000000005, "text": " there''s a book called
  change my office I have a bookshelf behind me I used to be in podcasts and", "tokens":
  [50960, 456, 311, 257, 1446, 1219, 1319, 452, 3398, 286, 362, 257, 1446, 46626,
  2261, 385, 286, 1143, 281, 312, 294, 24045, 293, 51300], "temperature": 0.0, "avg_logprob":
  -0.2882191875193379, "compression_ratio": 1.7612612612612613, "no_speech_prob":
  0.017625700682401657}, {"id": 713, "seek": 438926, "start": 4407.9800000000005,
  "end": 4415.9800000000005, "text": " I''d be like it''s that yeah yeah I still have
  it actually yes but it''s like it''s like ask your", "tokens": [51300, 286, 1116,
  312, 411, 309, 311, 300, 1338, 1338, 286, 920, 362, 309, 767, 2086, 457, 309, 311,
  411, 309, 311, 411, 1029, 428, 51700], "temperature": 0.0, "avg_logprob": -0.2882191875193379,
  "compression_ratio": 1.7612612612612613, "no_speech_prob": 0.017625700682401657},
  {"id": 714, "seek": 441598, "start": 4415.98, "end": 4422.0599999999995, "text":
  " developer is a title something like that about and well okay so that maybe maybe
  I got a little", "tokens": [50364, 10754, 307, 257, 4876, 746, 411, 300, 466, 293,
  731, 1392, 370, 300, 1310, 1310, 286, 658, 257, 707, 50668], "temperature": 0.0,
  "avg_logprob": -0.13517168830422793, "compression_ratio": 1.8333333333333333, "no_speech_prob":
  0.0015687869163230062}, {"id": 715, "seek": 441598, "start": 4422.0599999999995,
  "end": 4429.099999999999, "text": " off with this idea of research and engineering
  I think the the scientist is very like a metrics", "tokens": [50668, 766, 365, 341,
  1558, 295, 2132, 293, 7043, 286, 519, 264, 264, 12662, 307, 588, 411, 257, 16367,
  51020], "temperature": 0.0, "avg_logprob": -0.13517168830422793, "compression_ratio":
  1.8333333333333333, "no_speech_prob": 0.0015687869163230062}, {"id": 716, "seek":
  441598, "start": 4429.099999999999, "end": 4435.58, "text": " oriented in a different
  way like the the engineer like the the diversity of the tests and the data", "tokens":
  [51020, 21841, 294, 257, 819, 636, 411, 264, 264, 11403, 411, 264, 264, 8811, 295,
  264, 6921, 293, 264, 1412, 51344], "temperature": 0.0, "avg_logprob": -0.13517168830422793,
  "compression_ratio": 1.8333333333333333, "no_speech_prob": 0.0015687869163230062},
  {"id": 717, "seek": 441598, "start": 4435.58, "end": 4441.82, "text": " collection
  is more important when you''re the when you''re the scientist sort of uh yeah the
  the", "tokens": [51344, 5765, 307, 544, 1021, 562, 291, 434, 264, 562, 291, 434,
  264, 12662, 1333, 295, 2232, 1338, 264, 264, 51656], "temperature": 0.0, "avg_logprob":
  -0.13517168830422793, "compression_ratio": 1.8333333333333333, "no_speech_prob":
  0.0015687869163230062}, {"id": 718, "seek": 444182, "start": 4441.82, "end": 4447.34,
  "text": " engineer needs to build like smoke tests sort of where whereas I see the
  scientist needs to like", "tokens": [50364, 11403, 2203, 281, 1322, 411, 8439, 6921,
  1333, 295, 689, 9735, 286, 536, 264, 12662, 2203, 281, 411, 50640], "temperature":
  0.0, "avg_logprob": -0.1600402726067437, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 0.00013123801909387112}, {"id": 719, "seek": 444182, "start":
  4447.34, "end": 4451.9, "text": " have a very rigorous data collection kind of because
  that''s sort of how I see the distinction", "tokens": [50640, 362, 257, 588, 29882,
  1412, 5765, 733, 295, 570, 300, 311, 1333, 295, 577, 286, 536, 264, 16844, 50868],
  "temperature": 0.0, "avg_logprob": -0.1600402726067437, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 0.00013123801909387112}, {"id": 720, "seek": 444182, "start":
  4451.9, "end": 4457.98, "text": " and responsibility sort of is that makes sense
  yeah it does it does actually yeah you you uh you gave a", "tokens": [50868, 293,
  6357, 1333, 295, 307, 300, 1669, 2020, 1338, 309, 775, 309, 775, 767, 1338, 291,
  291, 2232, 291, 2729, 257, 51172], "temperature": 0.0, "avg_logprob": -0.1600402726067437,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 0.00013123801909387112},
  {"id": 721, "seek": 444182, "start": 4457.98, "end": 4464.54, "text": " very good
  distinctive you know feature what I was trying to say is that like in engineering
  you still", "tokens": [51172, 588, 665, 27766, 291, 458, 4111, 437, 286, 390, 1382,
  281, 584, 307, 300, 411, 294, 7043, 291, 920, 51500], "temperature": 0.0, "avg_logprob":
  -0.1600402726067437, "compression_ratio": 1.8846153846153846, "no_speech_prob":
  0.00013123801909387112}, {"id": 722, "seek": 444182, "start": 4464.54, "end": 4470.78,
  "text": " have a plethora of options like it''s combinatorial explosions in certain
  cases there are also", "tokens": [51500, 362, 257, 499, 302, 7013, 295, 3956, 411,
  309, 311, 2512, 31927, 831, 36872, 294, 1629, 3331, 456, 366, 611, 51812], "temperature":
  0.0, "avg_logprob": -0.1600402726067437, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 0.00013123801909387112}, {"id": 723, "seek": 447078, "start":
  4470.78, "end": 4476.38, "text": " mundane parts in both of these right so like
  we are not talking about them but like they do exist", "tokens": [50364, 43497,
  3166, 294, 1293, 295, 613, 558, 370, 411, 321, 366, 406, 1417, 466, 552, 457, 411,
  436, 360, 2514, 50644], "temperature": 0.0, "avg_logprob": -0.06802671220567491,
  "compression_ratio": 1.724890829694323, "no_speech_prob": 0.0008137279073707759},
  {"id": 724, "seek": 447078, "start": 4476.38, "end": 4483.34, "text": " but like
  you do have these points like okay should I branch this way or that way should I
  step back", "tokens": [50644, 457, 411, 291, 360, 362, 613, 2793, 411, 1392, 820,
  286, 9819, 341, 636, 420, 300, 636, 820, 286, 1823, 646, 50992], "temperature":
  0.0, "avg_logprob": -0.06802671220567491, "compression_ratio": 1.724890829694323,
  "no_speech_prob": 0.0008137279073707759}, {"id": 725, "seek": 447078, "start": 4483.34,
  "end": 4490.139999999999, "text": " and rethink and and that''s yeah but I agree
  I agree you you gave a really good example of like in", "tokens": [50992, 293, 34595,
  293, 293, 300, 311, 1338, 457, 286, 3986, 286, 3986, 291, 291, 2729, 257, 534, 665,
  1365, 295, 411, 294, 51332], "temperature": 0.0, "avg_logprob": -0.06802671220567491,
  "compression_ratio": 1.724890829694323, "no_speech_prob": 0.0008137279073707759},
  {"id": 726, "seek": 447078, "start": 4490.139999999999, "end": 4498.219999999999,
  "text": " research I do care about data so much in engineering it''s probably the
  quality assurance department", "tokens": [51332, 2132, 286, 360, 1127, 466, 1412,
  370, 709, 294, 7043, 309, 311, 1391, 264, 3125, 32189, 5882, 51736], "temperature":
  0.0, "avg_logprob": -0.06802671220567491, "compression_ratio": 1.724890829694323,
  "no_speech_prob": 0.0008137279073707759}, {"id": 727, "seek": 449822, "start": 4498.7,
  "end": 4504.22, "text": " is going to worry about okay what data we''re going to
  feed into the system to try to kind of maybe", "tokens": [50388, 307, 516, 281,
  3292, 466, 1392, 437, 1412, 321, 434, 516, 281, 3154, 666, 264, 1185, 281, 853,
  281, 733, 295, 1310, 50664], "temperature": 0.0, "avg_logprob": -0.12567006780746134,
  "compression_ratio": 1.7292576419213974, "no_speech_prob": 0.0021686244290322065},
  {"id": 728, "seek": 449822, "start": 4504.22, "end": 4511.26, "text": " break it
  and see limits and where it breaks what do we need to fix um or is it kind of like
  stable", "tokens": [50664, 1821, 309, 293, 536, 10406, 293, 689, 309, 9857, 437,
  360, 321, 643, 281, 3191, 1105, 420, 307, 309, 733, 295, 411, 8351, 51016], "temperature":
  0.0, "avg_logprob": -0.12567006780746134, "compression_ratio": 1.7292576419213974,
  "no_speech_prob": 0.0021686244290322065}, {"id": 729, "seek": 449822, "start": 4511.26,
  "end": 4517.5, "text": " what it proved enough to release you know things like that
  so but yeah I think if I can stay on this", "tokens": [51016, 437, 309, 14617, 1547,
  281, 4374, 291, 458, 721, 411, 300, 370, 457, 1338, 286, 519, 498, 286, 393, 1754,
  322, 341, 51328], "temperature": 0.0, "avg_logprob": -0.12567006780746134, "compression_ratio":
  1.7292576419213974, "no_speech_prob": 0.0021686244290322065}, {"id": 730, "seek":
  449822, "start": 4517.5, "end": 4523.02, "text": " a little more I think this like
  generalization testing like the industry of quality assurance but", "tokens": [51328,
  257, 707, 544, 286, 519, 341, 411, 2674, 2144, 4997, 411, 264, 3518, 295, 3125,
  32189, 457, 51604], "temperature": 0.0, "avg_logprob": -0.12567006780746134, "compression_ratio":
  1.7292576419213974, "no_speech_prob": 0.0021686244290322065}, {"id": 731, "seek":
  452302, "start": 4523.02, "end": 4529.42, "text": " 4D learning is is going to be
  really fascinating I''m like excited like how I think when we first met", "tokens":
  [50364, 1017, 35, 2539, 307, 307, 516, 281, 312, 534, 10343, 286, 478, 411, 2919,
  411, 577, 286, 519, 562, 321, 700, 1131, 50684], "temperature": 0.0, "avg_logprob":
  -0.1162019177017925, "compression_ratio": 1.8059701492537314, "no_speech_prob":
  0.005159751046448946}, {"id": 732, "seek": 452302, "start": 4529.42, "end": 4534.860000000001,
  "text": " you had written this um not all vector databases are equal and I thought
  that was so insightful", "tokens": [50684, 291, 632, 3720, 341, 1105, 406, 439,
  8062, 22380, 366, 2681, 293, 286, 1194, 300, 390, 370, 46401, 50956], "temperature":
  0.0, "avg_logprob": -0.1162019177017925, "compression_ratio": 1.8059701492537314,
  "no_speech_prob": 0.005159751046448946}, {"id": 733, "seek": 452302, "start": 4534.860000000001,
  "end": 4539.740000000001, "text": " because it was like a you told the story of
  an emerging market and that was so interesting I", "tokens": [50956, 570, 309, 390,
  411, 257, 291, 1907, 264, 1657, 295, 364, 14989, 2142, 293, 300, 390, 370, 1880,
  286, 51200], "temperature": 0.0, "avg_logprob": -0.1162019177017925, "compression_ratio":
  1.8059701492537314, "no_speech_prob": 0.005159751046448946}, {"id": 734, "seek":
  452302, "start": 4539.740000000001, "end": 4544.3, "text": " really look forward
  to seeing like the story of the emerging market around generalization testing",
  "tokens": [51200, 534, 574, 2128, 281, 2577, 411, 264, 1657, 295, 264, 14989, 2142,
  926, 2674, 2144, 4997, 51428], "temperature": 0.0, "avg_logprob": -0.1162019177017925,
  "compression_ratio": 1.8059701492537314, "no_speech_prob": 0.005159751046448946},
  {"id": 735, "seek": 452302, "start": 4544.3, "end": 4550.38, "text": " I think like
  um like with the beer benchmarks that kind of thing where it''s like you create
  some", "tokens": [51428, 286, 519, 411, 1105, 411, 365, 264, 8795, 43751, 300, 733,
  295, 551, 689, 309, 311, 411, 291, 1884, 512, 51732], "temperature": 0.0, "avg_logprob":
  -0.1162019177017925, "compression_ratio": 1.8059701492537314, "no_speech_prob":
  0.005159751046448946}, {"id": 736, "seek": 455038, "start": 4550.38, "end": 4556.7,
  "text": " million scale data set and have the NDCG recall precision with all these
  queries I think maybe", "tokens": [50364, 2459, 4373, 1412, 992, 293, 362, 264,
  426, 25619, 38, 9901, 18356, 365, 439, 613, 24109, 286, 519, 1310, 50680], "temperature":
  0.0, "avg_logprob": -0.1972413106007619, "compression_ratio": 1.6597222222222223,
  "no_speech_prob": 0.0011497298255562782}, {"id": 737, "seek": 455038, "start": 4556.7,
  "end": 4563.02, "text": " also this idea of like AB testing with models is going
  to be more popular I was when I went to", "tokens": [50680, 611, 341, 1558, 295,
  411, 13838, 4997, 365, 5245, 307, 516, 281, 312, 544, 3743, 286, 390, 562, 286,
  1437, 281, 50996], "temperature": 0.0, "avg_logprob": -0.1972413106007619, "compression_ratio":
  1.6597222222222223, "no_speech_prob": 0.0011497298255562782}, {"id": 738, "seek":
  455038, "start": 4563.02, "end": 4568.7, "text": " Neurops this year and there is
  this talk from Dr. Juhau came about interaction centric AI and", "tokens": [50996,
  1734, 374, 3370, 341, 1064, 293, 456, 307, 341, 751, 490, 2491, 13, 508, 3232, 1459,
  1361, 466, 9285, 1489, 1341, 7318, 293, 51280], "temperature": 0.0, "avg_logprob":
  -0.1972413106007619, "compression_ratio": 1.6597222222222223, "no_speech_prob":
  0.0011497298255562782}, {"id": 739, "seek": 455038, "start": 4568.7, "end": 4573.9800000000005,
  "text": " how that might differ from the first paradigm of model centric AI where
  say you judge the image", "tokens": [51280, 577, 300, 1062, 743, 490, 264, 700,
  24709, 295, 2316, 1489, 1341, 7318, 689, 584, 291, 6995, 264, 3256, 51544], "temperature":
  0.0, "avg_logprob": -0.1972413106007619, "compression_ratio": 1.6597222222222223,
  "no_speech_prob": 0.0011497298255562782}, {"id": 740, "seek": 455038, "start": 4573.9800000000005,
  "end": 4579.9800000000005, "text": " generation model purely based on like inception
  score for shade is tends to feature spaces in real", "tokens": [51544, 5125, 2316,
  17491, 2361, 322, 411, 49834, 6175, 337, 11466, 307, 12258, 281, 4111, 7673, 294,
  957, 51844], "temperature": 0.0, "avg_logprob": -0.1972413106007619, "compression_ratio":
  1.6597222222222223, "no_speech_prob": 0.0011497298255562782}, {"id": 741, "seek":
  457998, "start": 4579.98, "end": 4586.299999999999, "text": " images and then to
  data centric AI which is like I think snorkel AI is very responsible for like",
  "tokens": [50364, 5267, 293, 550, 281, 1412, 1489, 1341, 7318, 597, 307, 411, 286,
  519, 2406, 284, 7124, 7318, 307, 588, 6250, 337, 411, 50680], "temperature": 0.0,
  "avg_logprob": -0.12746190216581701, "compression_ratio": 1.8403041825095057, "no_speech_prob":
  0.000681009201798588}, {"id": 742, "seek": 457998, "start": 4586.94, "end": 4591.099999999999,
  "text": " branding that term and making it so popular but it''s like you''re really
  focusing on the curation", "tokens": [50712, 27279, 300, 1433, 293, 1455, 309, 370,
  3743, 457, 309, 311, 411, 291, 434, 534, 8416, 322, 264, 1262, 399, 50920], "temperature":
  0.0, "avg_logprob": -0.12746190216581701, "compression_ratio": 1.8403041825095057,
  "no_speech_prob": 0.000681009201798588}, {"id": 743, "seek": 457998, "start": 4591.099999999999,
  "end": 4596.94, "text": " of data like your language model is like mosaic and oslatus
  pub med gpt it''s about like you have", "tokens": [50920, 295, 1412, 411, 428, 2856,
  2316, 307, 411, 275, 42261, 293, 3003, 75, 37926, 1535, 1205, 290, 662, 309, 311,
  466, 411, 291, 362, 51212], "temperature": 0.0, "avg_logprob": -0.12746190216581701,
  "compression_ratio": 1.8403041825095057, "no_speech_prob": 0.000681009201798588},
  {"id": 744, "seek": 457998, "start": 4596.94, "end": 4602.139999999999, "text":
  " this particular data and you like clean it and you make it awesome and then I
  think interaction", "tokens": [51212, 341, 1729, 1412, 293, 291, 411, 2541, 309,
  293, 291, 652, 309, 3476, 293, 550, 286, 519, 9285, 51472], "temperature": 0.0,
  "avg_logprob": -0.12746190216581701, "compression_ratio": 1.8403041825095057, "no_speech_prob":
  0.000681009201798588}, {"id": 745, "seek": 457998, "start": 4602.139999999999, "end":
  4608.7, "text": " centric AI is like a new way to evaluate models where it''s like
  AB testing driven kind of or like", "tokens": [51472, 1489, 1341, 7318, 307, 411,
  257, 777, 636, 281, 13059, 5245, 689, 309, 311, 411, 13838, 4997, 9555, 733, 295,
  420, 411, 51800], "temperature": 0.0, "avg_logprob": -0.12746190216581701, "compression_ratio":
  1.8403041825095057, "no_speech_prob": 0.000681009201798588}, {"id": 746, "seek":
  460870, "start": 4608.78, "end": 4613.099999999999, "text": " how quickly can you
  perform a test I don''t know if I''ve gotten too else topic but", "tokens": [50368,
  577, 2661, 393, 291, 2042, 257, 1500, 286, 500, 380, 458, 498, 286, 600, 5768, 886,
  1646, 4829, 457, 50584], "temperature": 0.0, "avg_logprob": -0.1621275169904842,
  "compression_ratio": 1.6807511737089202, "no_speech_prob": 0.006173889618366957},
  {"id": 747, "seek": 460870, "start": 4613.099999999999, "end": 4621.26, "text":
  " no I think it''s it''s exactly the topic to focus on if we are serious about you
  know putting", "tokens": [50584, 572, 286, 519, 309, 311, 309, 311, 2293, 264, 4829,
  281, 1879, 322, 498, 321, 366, 3156, 466, 291, 458, 3372, 50992], "temperature":
  0.0, "avg_logprob": -0.1621275169904842, "compression_ratio": 1.6807511737089202,
  "no_speech_prob": 0.006173889618366957}, {"id": 748, "seek": 460870, "start": 4621.26,
  "end": 4626.46, "text": " these things out in production like you do need you do
  need to have and provide an evidence", "tokens": [50992, 613, 721, 484, 294, 4265,
  411, 291, 360, 643, 291, 360, 643, 281, 362, 293, 2893, 364, 4467, 51252], "temperature":
  0.0, "avg_logprob": -0.1621275169904842, "compression_ratio": 1.6807511737089202,
  "no_speech_prob": 0.006173889618366957}, {"id": 749, "seek": 460870, "start": 4626.46,
  "end": 4633.179999999999, "text": " to the stakeholders that and to yourself that
  this dust hold water and we can release it and", "tokens": [51252, 281, 264, 17779,
  300, 293, 281, 1803, 300, 341, 8634, 1797, 1281, 293, 321, 393, 4374, 309, 293,
  51588], "temperature": 0.0, "avg_logprob": -0.1621275169904842, "compression_ratio":
  1.6807511737089202, "no_speech_prob": 0.006173889618366957}, {"id": 750, "seek":
  463318, "start": 4633.18, "end": 4638.780000000001, "text": " it''s not going to
  show something you know in discriminate to the users that they will be", "tokens":
  [50364, 309, 311, 406, 516, 281, 855, 746, 291, 458, 294, 47833, 281, 264, 5022,
  300, 436, 486, 312, 50644], "temperature": 0.0, "avg_logprob": -0.1542003059387207,
  "compression_ratio": 1.7756653992395437, "no_speech_prob": 0.002740477677434683},
  {"id": 751, "seek": 463318, "start": 4638.780000000001, "end": 4644.38, "text":
  " completely you know puzzled and stuff or maybe you know there are all these numerous
  examples when", "tokens": [50644, 2584, 291, 458, 18741, 1493, 293, 1507, 420, 1310,
  291, 458, 456, 366, 439, 613, 12546, 5110, 562, 50924], "temperature": 0.0, "avg_logprob":
  -0.1542003059387207, "compression_ratio": 1.7756653992395437, "no_speech_prob":
  0.002740477677434683}, {"id": 752, "seek": 463318, "start": 4645.5, "end": 4650.3,
  "text": " like Google search when they I think incorporated some distilled version
  of bird when they", "tokens": [50980, 411, 3329, 3164, 562, 436, 286, 519, 21654,
  512, 1483, 6261, 3037, 295, 5255, 562, 436, 51220], "temperature": 0.0, "avg_logprob":
  -0.1542003059387207, "compression_ratio": 1.7756653992395437, "no_speech_prob":
  0.002740477677434683}, {"id": 753, "seek": 463318, "start": 4650.3, "end": 4654.62,
  "text": " would flip the meaning and they would say you do take this medicine but
  actually in the", "tokens": [51220, 576, 7929, 264, 3620, 293, 436, 576, 584, 291,
  360, 747, 341, 7195, 457, 767, 294, 264, 51436], "temperature": 0.0, "avg_logprob":
  -0.1542003059387207, "compression_ratio": 1.7756653992395437, "no_speech_prob":
  0.002740477677434683}, {"id": 754, "seek": 463318, "start": 4655.42, "end": 4661.1,
  "text": " prescription it says you do not take that medicine or vice versa you know
  because it''s not sensitive", "tokens": [51476, 22456, 309, 1619, 291, 360, 406,
  747, 300, 7195, 420, 11964, 25650, 291, 458, 570, 309, 311, 406, 9477, 51760], "temperature":
  0.0, "avg_logprob": -0.1542003059387207, "compression_ratio": 1.7756653992395437,
  "no_speech_prob": 0.002740477677434683}, {"id": 755, "seek": 466110, "start": 4661.1,
  "end": 4668.780000000001, "text": " to negations and stuff so like I totally agree
  I''m with you on that like how do we QA", "tokens": [50364, 281, 2485, 763, 293,
  1507, 370, 411, 286, 3879, 3986, 286, 478, 365, 291, 322, 300, 411, 577, 360, 321,
  1249, 32, 50748], "temperature": 0.0, "avg_logprob": -0.1914225589023547, "compression_ratio":
  1.6306306306306306, "no_speech_prob": 0.003131803823634982}, {"id": 756, "seek":
  466110, "start": 4670.38, "end": 4675.9800000000005, "text": " quality of sure you
  know that the systems that release and I think the open AI", "tokens": [50828, 3125,
  295, 988, 291, 458, 300, 264, 3652, 300, 4374, 293, 286, 519, 264, 1269, 7318, 51108],
  "temperature": 0.0, "avg_logprob": -0.1914225589023547, "compression_ratio": 1.6306306306306306,
  "no_speech_prob": 0.003131803823634982}, {"id": 757, "seek": 466110, "start": 4675.9800000000005,
  "end": 4682.3, "text": " team did that brilliant trick in a way that they said hey
  here is the chat GPT go test it and they", "tokens": [51108, 1469, 630, 300, 10248,
  4282, 294, 257, 636, 300, 436, 848, 4177, 510, 307, 264, 5081, 26039, 51, 352, 1500,
  309, 293, 436, 51424], "temperature": 0.0, "avg_logprob": -0.1914225589023547, "compression_ratio":
  1.6306306306306306, "no_speech_prob": 0.003131803823634982}, {"id": 758, "seek":
  466110, "start": 4682.3, "end": 4690.54, "text": " get like million users in the
  first few days because they actually do need some extra brains to do", "tokens":
  [51424, 483, 411, 2459, 5022, 294, 264, 700, 1326, 1708, 570, 436, 767, 360, 643,
  512, 2857, 15442, 281, 360, 51836], "temperature": 0.0, "avg_logprob": -0.1914225589023547,
  "compression_ratio": 1.6306306306306306, "no_speech_prob": 0.003131803823634982},
  {"id": 759, "seek": 469110, "start": 4691.1, "end": 4697.18, "text": " go and test
  in different like scenarios and see where it breaks maybe it doesn''t make sense
  anymore so", "tokens": [50364, 352, 293, 1500, 294, 819, 411, 15077, 293, 536, 689,
  309, 9857, 1310, 309, 1177, 380, 652, 2020, 3602, 370, 50668], "temperature": 0.0,
  "avg_logprob": -0.22550534142388237, "compression_ratio": 1.7004405286343611, "no_speech_prob":
  0.0018624988151714206}, {"id": 760, "seek": 469110, "start": 4697.18, "end": 4704.3,
  "text": " yeah it''s my understanding that''s how like scale AI became the kings
  is that you know like labeled data", "tokens": [50668, 1338, 309, 311, 452, 3701,
  300, 311, 577, 411, 4373, 7318, 3062, 264, 21581, 307, 300, 291, 458, 411, 21335,
  1412, 51024], "temperature": 0.0, "avg_logprob": -0.22550534142388237, "compression_ratio":
  1.7004405286343611, "no_speech_prob": 0.0018624988151714206}, {"id": 761, "seek":
  469110, "start": 4705.34, "end": 4709.5, "text": " like mechanical Turk I think
  Sir J.I. is something that''s emerging that I''ve been seeing", "tokens": [51076,
  411, 12070, 15714, 286, 519, 6144, 508, 13, 40, 13, 307, 746, 300, 311, 14989, 300,
  286, 600, 668, 2577, 51284], "temperature": 0.0, "avg_logprob": -0.22550534142388237,
  "compression_ratio": 1.7004405286343611, "no_speech_prob": 0.0018624988151714206},
  {"id": 762, "seek": 469110, "start": 4710.22, "end": 4718.54, "text": " yeah it''s
  really interesting yeah exactly um yeah um I was I was wondering um you you also",
  "tokens": [51320, 1338, 309, 311, 534, 1880, 1338, 2293, 1105, 1338, 1105, 286,
  390, 286, 390, 6359, 1105, 291, 291, 611, 51736], "temperature": 0.0, "avg_logprob":
  -0.22550534142388237, "compression_ratio": 1.7004405286343611, "no_speech_prob":
  0.0018624988151714206}, {"id": 763, "seek": 471854, "start": 4719.18, "end": 4725.58,
  "text": " worked on this podcast search and you had the opinion that Whisper has
  some bottlenecks I", "tokens": [50396, 2732, 322, 341, 7367, 3164, 293, 291, 632,
  264, 4800, 300, 41132, 610, 575, 512, 44641, 2761, 286, 50716], "temperature": 0.0,
  "avg_logprob": -0.1904923915863037, "compression_ratio": 1.71875, "no_speech_prob":
  0.005402225535362959}, {"id": 764, "seek": 471854, "start": 4725.58, "end": 4730.7,
  "text": " wonder if you if you want to like tap into that a little bit yeah so I''d
  love to tell this story so", "tokens": [50716, 2441, 498, 291, 498, 291, 528, 281,
  411, 5119, 666, 300, 257, 707, 857, 1338, 370, 286, 1116, 959, 281, 980, 341, 1657,
  370, 50972], "temperature": 0.0, "avg_logprob": -0.1904923915863037, "compression_ratio":
  1.71875, "no_speech_prob": 0.005402225535362959}, {"id": 765, "seek": 471854, "start":
  4730.7, "end": 4737.9, "text": " uh so it comes the kind of story behind it is uh
  so Boris power at open AI tweeted uh so they", "tokens": [50972, 2232, 370, 309,
  1487, 264, 733, 295, 1657, 2261, 309, 307, 2232, 370, 27158, 1347, 412, 1269, 7318,
  25646, 2232, 370, 436, 51332], "temperature": 0.0, "avg_logprob": -0.1904923915863037,
  "compression_ratio": 1.71875, "no_speech_prob": 0.005402225535362959}, {"id": 766,
  "seek": 471854, "start": 4737.9, "end": 4743.58, "text": " they cut the prices for
  the open AI embeddings and and Boris is pointing out how cheap it would be to",
  "tokens": [51332, 436, 1723, 264, 7901, 337, 264, 1269, 7318, 12240, 29432, 293,
  293, 27158, 307, 12166, 484, 577, 7084, 309, 576, 312, 281, 51616], "temperature":
  0.0, "avg_logprob": -0.1904923915863037, "compression_ratio": 1.71875, "no_speech_prob":
  0.005402225535362959}, {"id": 767, "seek": 474358, "start": 4743.58, "end": 4749.5,
  "text": " index a massive podcast like the Joe Rogan podcast so that''s how I was
  like hey I have a podcast", "tokens": [50364, 8186, 257, 5994, 7367, 411, 264, 6807,
  11860, 282, 7367, 370, 300, 311, 577, 286, 390, 411, 4177, 286, 362, 257, 7367,
  50660], "temperature": 0.0, "avg_logprob": -0.202735349867079, "compression_ratio":
  1.7832512315270936, "no_speech_prob": 0.0017639321740716696}, {"id": 768, "seek":
  474358, "start": 4754.54, "end": 4759.0199999999995, "text": " and you have a vector
  podcast and we did also but so I started to be", "tokens": [50912, 293, 291, 362,
  257, 8062, 7367, 293, 321, 630, 611, 457, 370, 286, 1409, 281, 312, 51136], "temperature":
  0.0, "avg_logprob": -0.202735349867079, "compression_ratio": 1.7832512315270936,
  "no_speech_prob": 0.0017639321740716696}, {"id": 769, "seek": 474358, "start": 4760.38,
  "end": 4764.0599999999995, "text": " you know I started doing this where you you
  know you take the audio files then you put them into", "tokens": [51204, 291, 458,
  286, 1409, 884, 341, 689, 291, 291, 458, 291, 747, 264, 6278, 7098, 550, 291, 829,
  552, 666, 51388], "temperature": 0.0, "avg_logprob": -0.202735349867079, "compression_ratio":
  1.7832512315270936, "no_speech_prob": 0.0017639321740716696}, {"id": 770, "seek":
  474358, "start": 4764.0599999999995, "end": 4768.14, "text": " Whisper I also tried
  like uh descript is something that I like a lot I''ve been using descript for a",
  "tokens": [51388, 41132, 610, 286, 611, 3031, 411, 2232, 31280, 307, 746, 300, 286,
  411, 257, 688, 286, 600, 668, 1228, 31280, 337, 257, 51592], "temperature": 0.0,
  "avg_logprob": -0.202735349867079, "compression_ratio": 1.7832512315270936, "no_speech_prob":
  0.0017639321740716696}, {"id": 771, "seek": 476814, "start": 4768.14, "end": 4777.5,
  "text": " long time for editing videos and so it''s like you still because you it''s
  very the podcast transcriptions", "tokens": [50364, 938, 565, 337, 10000, 2145,
  293, 370, 309, 311, 411, 291, 920, 570, 291, 309, 311, 588, 264, 7367, 24444, 626,
  50832], "temperature": 0.0, "avg_logprob": -0.09911531017672631, "compression_ratio":
  1.8130841121495327, "no_speech_prob": 0.0007956991321407259}, {"id": 772, "seek":
  476814, "start": 4777.5, "end": 4783.26, "text": " you still want to edit them a
  bit you you have like uh and like like if you were yes how I''m", "tokens": [50832,
  291, 920, 528, 281, 8129, 552, 257, 857, 291, 291, 362, 411, 2232, 293, 411, 411,
  498, 291, 645, 2086, 577, 286, 478, 51120], "temperature": 0.0, "avg_logprob": -0.09911531017672631,
  "compression_ratio": 1.8130841121495327, "no_speech_prob": 0.0007956991321407259},
  {"id": 773, "seek": 476814, "start": 4783.26, "end": 4788.46, "text": " pausing
  right now I''m talking about but the transcriptions it''s not quite what you want
  to like", "tokens": [51120, 2502, 7981, 558, 586, 286, 478, 1417, 466, 457, 264,
  24444, 626, 309, 311, 406, 1596, 437, 291, 528, 281, 411, 51380], "temperature":
  0.0, "avg_logprob": -0.09911531017672631, "compression_ratio": 1.8130841121495327,
  "no_speech_prob": 0.0007956991321407259}, {"id": 774, "seek": 476814, "start": 4788.46,
  "end": 4794.46, "text": " index to this idea of like how do we create a knowledge
  base from these podcasts because these", "tokens": [51380, 8186, 281, 341, 1558,
  295, 411, 577, 360, 321, 1884, 257, 3601, 3096, 490, 613, 24045, 570, 613, 51680],
  "temperature": 0.0, "avg_logprob": -0.09911531017672631, "compression_ratio": 1.8130841121495327,
  "no_speech_prob": 0.0007956991321407259}, {"id": 775, "seek": 479446, "start": 4794.46,
  "end": 4799.66, "text": " podcasts is so like we''ve covered so many topics and
  it''s so it''s kind of easier to do it like", "tokens": [50364, 24045, 307, 370,
  411, 321, 600, 5343, 370, 867, 8378, 293, 309, 311, 370, 309, 311, 733, 295, 3571,
  281, 360, 309, 411, 50624], "temperature": 0.0, "avg_logprob": -0.11640775100044583,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.00045416783541440964},
  {"id": 776, "seek": 479446, "start": 4799.66, "end": 4805.18, "text": " this than
  to be writing all this down and then and also it''s very collaborative uh like the
  podcast", "tokens": [50624, 341, 813, 281, 312, 3579, 439, 341, 760, 293, 550, 293,
  611, 309, 311, 588, 16555, 2232, 411, 264, 7367, 50900], "temperature": 0.0, "avg_logprob":
  -0.11640775100044583, "compression_ratio": 1.8171641791044777, "no_speech_prob":
  0.00045416783541440964}, {"id": 777, "seek": 479446, "start": 4805.18, "end": 4811.18,
  "text": " you get more people involved it''s like a community building thing is
  so yeah that idea of creating", "tokens": [50900, 291, 483, 544, 561, 3288, 309,
  311, 411, 257, 1768, 2390, 551, 307, 370, 1338, 300, 1558, 295, 4084, 51200], "temperature":
  0.0, "avg_logprob": -0.11640775100044583, "compression_ratio": 1.8171641791044777,
  "no_speech_prob": 0.00045416783541440964}, {"id": 778, "seek": 479446, "start":
  4811.18, "end": 4815.9800000000005, "text": " knowledge bases out of podcasts like
  what would you write your interest on a scale of one to 10", "tokens": [51200, 3601,
  17949, 484, 295, 24045, 411, 437, 576, 291, 2464, 428, 1179, 322, 257, 4373, 295,
  472, 281, 1266, 51440], "temperature": 0.0, "avg_logprob": -0.11640775100044583,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.00045416783541440964},
  {"id": 779, "seek": 479446, "start": 4815.9800000000005, "end": 4823.9, "text":
  " of having a vector podcast I mean I would love to join to join the you know to
  join the geek here", "tokens": [51440, 295, 1419, 257, 8062, 7367, 286, 914, 286,
  576, 959, 281, 3917, 281, 3917, 264, 291, 458, 281, 3917, 264, 36162, 510, 51836],
  "temperature": 0.0, "avg_logprob": -0.11640775100044583, "compression_ratio": 1.8171641791044777,
  "no_speech_prob": 0.00045416783541440964}, {"id": 780, "seek": 482390, "start":
  4823.9, "end": 4829.98, "text": " so because I do like I was rewatching the episode
  with you Danny here we go and you were like", "tokens": [50364, 370, 570, 286, 360,
  411, 286, 390, 319, 15219, 278, 264, 3500, 365, 291, 16682, 510, 321, 352, 293,
  291, 645, 411, 50668], "temperature": 0.0, "avg_logprob": -0.12673758593472567,
  "compression_ratio": 1.859375, "no_speech_prob": 0.00475694052875042}, {"id": 781,
  "seek": 482390, "start": 4829.98, "end": 4835.179999999999, "text": " exploding
  with knowledge right like in a way you''re branching out a lot today as well exploding",
  "tokens": [50668, 35175, 365, 3601, 558, 411, 294, 257, 636, 291, 434, 9819, 278,
  484, 257, 688, 965, 382, 731, 35175, 50928], "temperature": 0.0, "avg_logprob":
  -0.12673758593472567, "compression_ratio": 1.859375, "no_speech_prob": 0.00475694052875042},
  {"id": 782, "seek": 482390, "start": 4835.179999999999, "end": 4840.62, "text":
  " with knowledge because you you read all these papers you try things you share
  you know like google", "tokens": [50928, 365, 3601, 570, 291, 291, 1401, 439, 613,
  10577, 291, 853, 721, 291, 2073, 291, 458, 411, 20742, 51200], "temperature": 0.0,
  "avg_logprob": -0.12673758593472567, "compression_ratio": 1.859375, "no_speech_prob":
  0.00475694052875042}, {"id": 783, "seek": 482390, "start": 4840.62, "end": 4847.58,
  "text": " collapse and stuff but like like how do I tap into this knowledge like
  it''s it''s very synchronous", "tokens": [51200, 15584, 293, 1507, 457, 411, 411,
  577, 360, 286, 5119, 666, 341, 3601, 411, 309, 311, 309, 311, 588, 44743, 51548],
  "temperature": 0.0, "avg_logprob": -0.12673758593472567, "compression_ratio": 1.859375,
  "no_speech_prob": 0.00475694052875042}, {"id": 784, "seek": 482390, "start": 4847.58,
  "end": 4853.259999999999, "text": " right I have to like there is no way to like
  random jump into hey where did he talk about", "tokens": [51548, 558, 286, 362,
  281, 411, 456, 307, 572, 636, 281, 411, 4974, 3012, 666, 4177, 689, 630, 415, 751,
  466, 51832], "temperature": 0.0, "avg_logprob": -0.12673758593472567, "compression_ratio":
  1.859375, "no_speech_prob": 0.00475694052875042}, {"id": 785, "seek": 485390, "start":
  4854.0599999999995, "end": 4860.219999999999, "text": " you know that model from
  Microsoft like I don''t know unless I have the time code I don''t have a", "tokens":
  [50372, 291, 458, 300, 2316, 490, 8116, 411, 286, 500, 380, 458, 5969, 286, 362,
  264, 565, 3089, 286, 500, 380, 362, 257, 50680], "temperature": 0.0, "avg_logprob":
  -0.147407560932393, "compression_ratio": 1.669603524229075, "no_speech_prob": 0.003405550494790077},
  {"id": 786, "seek": 485390, "start": 4860.219999999999, "end": 4867.9, "text": "
  way to do that right so yeah yeah and I what that''s what inspires me so much with
  I want to fine-tune", "tokens": [50680, 636, 281, 360, 300, 558, 370, 1338, 1338,
  293, 286, 437, 300, 311, 437, 32566, 385, 370, 709, 365, 286, 528, 281, 2489, 12,
  83, 2613, 51064], "temperature": 0.0, "avg_logprob": -0.147407560932393, "compression_ratio":
  1.669603524229075, "no_speech_prob": 0.003405550494790077}, {"id": 787, "seek":
  485390, "start": 4867.9, "end": 4874.78, "text": " these models so badly just on
  the uh turn taking as the positive labeling and yeah I think", "tokens": [51064,
  613, 5245, 370, 13425, 445, 322, 264, 2232, 1261, 1940, 382, 264, 3353, 40244, 293,
  1338, 286, 519, 51408], "temperature": 0.0, "avg_logprob": -0.147407560932393, "compression_ratio":
  1.669603524229075, "no_speech_prob": 0.003405550494790077}, {"id": 788, "seek":
  485390, "start": 4875.82, "end": 4880.379999999999, "text": " can you expand a bit
  more on that what do you mean uh okay Conor says I want to talk about", "tokens":
  [51460, 393, 291, 5268, 257, 857, 544, 322, 300, 437, 360, 291, 914, 2232, 1392,
  2656, 284, 1619, 286, 528, 281, 751, 466, 51688], "temperature": 0.0, "avg_logprob":
  -0.147407560932393, "compression_ratio": 1.669603524229075, "no_speech_prob": 0.003405550494790077},
  {"id": 789, "seek": 488038, "start": 4880.38, "end": 4884.78, "text": " the turn
  taking Demetri can you expand on that more on what that means Conor okay it''s like",
  "tokens": [50364, 264, 1261, 1940, 4686, 302, 470, 393, 291, 5268, 322, 300, 544,
  322, 437, 300, 1355, 2656, 284, 1392, 309, 311, 411, 50584], "temperature": 0.0,
  "avg_logprob": -0.29456416420314624, "compression_ratio": 1.8009478672985781, "no_speech_prob":
  0.0036261503119021654}, {"id": 790, "seek": 488038, "start": 4886.86, "end": 4893.34,
  "text": " this is how you do the positive thing that''s like potentially like that
  yeah yeah yeah and like if", "tokens": [50688, 341, 307, 577, 291, 360, 264, 3353,
  551, 300, 311, 411, 7263, 411, 300, 1338, 1338, 1338, 293, 411, 498, 51012], "temperature":
  0.0, "avg_logprob": -0.29456416420314624, "compression_ratio": 1.8009478672985781,
  "no_speech_prob": 0.0036261503119021654}, {"id": 791, "seek": 488038, "start": 4893.34,
  "end": 4898.22, "text": " you want to have more examples of what Conor said like
  you could like augment with Conor''s", "tokens": [51012, 291, 528, 281, 362, 544,
  5110, 295, 437, 2656, 284, 848, 411, 291, 727, 411, 29919, 365, 2656, 284, 311,
  51256], "temperature": 0.0, "avg_logprob": -0.29456416420314624, "compression_ratio":
  1.8009478672985781, "no_speech_prob": 0.0036261503119021654}, {"id": 792, "seek":
  488038, "start": 4898.22, "end": 4905.58, "text": " uh statements uh oh like sentences
  yeah yeah and just the I feel like the potential of it is crazy", "tokens": [51256,
  2232, 12363, 2232, 1954, 411, 16579, 1338, 1338, 293, 445, 264, 286, 841, 411, 264,
  3995, 295, 309, 307, 3219, 51624], "temperature": 0.0, "avg_logprob": -0.29456416420314624,
  "compression_ratio": 1.8009478672985781, "no_speech_prob": 0.0036261503119021654},
  {"id": 793, "seek": 490558, "start": 4906.14, "end": 4911.1, "text": " I also think
  like we''re gonna see it like hooked into say Spotify are these big platforms that",
  "tokens": [50392, 286, 611, 519, 411, 321, 434, 799, 536, 309, 411, 20410, 666,
  584, 29036, 366, 613, 955, 9473, 300, 50640], "temperature": 0.0, "avg_logprob":
  -0.10304287627891258, "compression_ratio": 1.9291338582677164, "no_speech_prob":
  0.0051459879614412785}, {"id": 794, "seek": 490558, "start": 4911.1, "end": 4915.82,
  "text": " organize podcasts and I think it''ll help you like discover like because
  something else it''s like", "tokens": [50640, 13859, 24045, 293, 286, 519, 309,
  603, 854, 291, 411, 4411, 411, 570, 746, 1646, 309, 311, 411, 50876], "temperature":
  0.0, "avg_logprob": -0.10304287627891258, "compression_ratio": 1.9291338582677164,
  "no_speech_prob": 0.0051459879614412785}, {"id": 795, "seek": 490558, "start": 4915.82,
  "end": 4920.86, "text": " I love how you do this vector search podcast and I''m
  also doing a vector search podcast and it''s like", "tokens": [50876, 286, 959,
  577, 291, 360, 341, 8062, 3164, 7367, 293, 286, 478, 611, 884, 257, 8062, 3164,
  7367, 293, 309, 311, 411, 51128], "temperature": 0.0, "avg_logprob": -0.10304287627891258,
  "compression_ratio": 1.9291338582677164, "no_speech_prob": 0.0051459879614412785},
  {"id": 796, "seek": 490558, "start": 4920.86, "end": 4926.14, "text": " who else
  is out there doing like maybe a recommendation podcast or like you know like it''s
  like", "tokens": [51128, 567, 1646, 307, 484, 456, 884, 411, 1310, 257, 11879, 7367,
  420, 411, 291, 458, 411, 309, 311, 411, 51392], "temperature": 0.0, "avg_logprob":
  -0.10304287627891258, "compression_ratio": 1.9291338582677164, "no_speech_prob":
  0.0051459879614412785}, {"id": 797, "seek": 490558, "start": 4926.14, "end": 4931.26,
  "text": " this kind of discovery about the people because podcasting is very like
  collaborative it is a medium", "tokens": [51392, 341, 733, 295, 12114, 466, 264,
  561, 570, 7367, 278, 307, 588, 411, 16555, 309, 307, 257, 6399, 51648], "temperature":
  0.0, "avg_logprob": -0.10304287627891258, "compression_ratio": 1.9291338582677164,
  "no_speech_prob": 0.0051459879614412785}, {"id": 798, "seek": 493126, "start": 4931.34,
  "end": 4937.26, "text": " right like it is not like you you can''t do it by yourself
  no like it''s like it''s it''s almost like", "tokens": [50368, 558, 411, 309, 307,
  406, 411, 291, 291, 393, 380, 360, 309, 538, 1803, 572, 411, 309, 311, 411, 309,
  311, 309, 311, 1920, 411, 50664], "temperature": 0.0, "avg_logprob": -0.13954882277655847,
  "compression_ratio": 1.7782805429864252, "no_speech_prob": 0.009568842127919197},
  {"id": 799, "seek": 493126, "start": 4937.26, "end": 4942.860000000001, "text":
  " the thing uh like stand up comedian so anyone who is presenting you do need the
  audience because", "tokens": [50664, 264, 551, 2232, 411, 1463, 493, 30212, 370,
  2878, 567, 307, 15578, 291, 360, 643, 264, 4034, 570, 50944], "temperature": 0.0,
  "avg_logprob": -0.13954882277655847, "compression_ratio": 1.7782805429864252, "no_speech_prob":
  0.009568842127919197}, {"id": 800, "seek": 493126, "start": 4942.860000000001, "end":
  4951.34, "text": " you simply do not generate the 3d-ness of your thoughts in absence
  of people like it''s very hard", "tokens": [50944, 291, 2935, 360, 406, 8460, 264,
  805, 67, 12, 1287, 295, 428, 4598, 294, 17145, 295, 561, 411, 309, 311, 588, 1152,
  51368], "temperature": 0.0, "avg_logprob": -0.13954882277655847, "compression_ratio":
  1.7782805429864252, "no_speech_prob": 0.009568842127919197}, {"id": 801, "seek":
  493126, "start": 4951.34, "end": 4958.06, "text": " to do and then same thing happens
  here right now like when we exchange like I like I have like a full", "tokens":
  [51368, 281, 360, 293, 550, 912, 551, 2314, 510, 558, 586, 411, 562, 321, 7742,
  411, 286, 411, 286, 362, 411, 257, 1577, 51704], "temperature": 0.0, "avg_logprob":
  -0.13954882277655847, "compression_ratio": 1.7782805429864252, "no_speech_prob":
  0.009568842127919197}, {"id": 802, "seek": 495806, "start": 4958.14, "end": 4962.860000000001,
  "text": " shade of these notes and stuff right so I wouldn''t be able like what
  like do I do you know", "tokens": [50368, 11466, 295, 613, 5570, 293, 1507, 558,
  370, 286, 2759, 380, 312, 1075, 411, 437, 411, 360, 286, 360, 291, 458, 50604],
  "temperature": 0.0, "avg_logprob": -0.17972396047491776, "compression_ratio": 1.7735849056603774,
  "no_speech_prob": 0.02152528241276741}, {"id": 803, "seek": 495806, "start": 4962.860000000001,
  "end": 4969.660000000001, "text": " these things do I know some of these things
  you know it''s like a vote if working in your memory but", "tokens": [50604, 613,
  721, 360, 286, 458, 512, 295, 613, 721, 291, 458, 309, 311, 411, 257, 4740, 498,
  1364, 294, 428, 4675, 457, 50944], "temperature": 0.0, "avg_logprob": -0.17972396047491776,
  "compression_ratio": 1.7735849056603774, "no_speech_prob": 0.02152528241276741},
  {"id": 804, "seek": 495806, "start": 4969.660000000001, "end": 4975.42, "text":
  " like coming back to whisper like just to get it right you you''re saying it''s
  still a bottle neck", "tokens": [50944, 411, 1348, 646, 281, 26018, 411, 445, 281,
  483, 309, 558, 291, 291, 434, 1566, 309, 311, 920, 257, 7817, 6189, 51232], "temperature":
  0.0, "avg_logprob": -0.17972396047491776, "compression_ratio": 1.7735849056603774,
  "no_speech_prob": 0.02152528241276741}, {"id": 805, "seek": 495806, "start": 4975.42,
  "end": 4981.1, "text": " in your opinion in what way okay well I''d hate to be like
  quoted as saying it''s not good", "tokens": [51232, 294, 428, 4800, 294, 437, 636,
  1392, 731, 286, 1116, 4700, 281, 312, 411, 30047, 382, 1566, 309, 311, 406, 665,
  51516], "temperature": 0.0, "avg_logprob": -0.17972396047491776, "compression_ratio":
  1.7735849056603774, "no_speech_prob": 0.02152528241276741}, {"id": 806, "seek":
  498110, "start": 4981.1, "end": 4989.26, "text": " if it''s not the same thing which
  I value you know it''s not yeah so if you''re creating a podcast", "tokens": [50364,
  498, 309, 311, 406, 264, 912, 551, 597, 286, 2158, 291, 458, 309, 311, 406, 1338,
  370, 498, 291, 434, 4084, 257, 7367, 50772], "temperature": 0.0, "avg_logprob":
  -0.22395217895507813, "compression_ratio": 1.7953488372093023, "no_speech_prob":
  0.008322718553245068}, {"id": 807, "seek": 498110, "start": 4989.26, "end": 4994.700000000001,
  "text": " search app you like there''s still needs to be a little more parsing I
  don''t know if you need to find", "tokens": [50772, 3164, 724, 291, 411, 456, 311,
  920, 2203, 281, 312, 257, 707, 544, 21156, 278, 286, 500, 380, 458, 498, 291, 643,
  281, 915, 51044], "temperature": 0.0, "avg_logprob": -0.22395217895507813, "compression_ratio":
  1.7953488372093023, "no_speech_prob": 0.008322718553245068}, {"id": 808, "seek":
  498110, "start": 4994.700000000001, "end": 5001.42, "text": " I don''t know if you
  need to correct one and then fine tune so because I''ve also been playing a", "tokens":
  [51044, 286, 500, 380, 458, 498, 291, 643, 281, 3006, 472, 293, 550, 2489, 10864,
  370, 570, 286, 600, 611, 668, 2433, 257, 51380], "temperature": 0.0, "avg_logprob":
  -0.22395217895507813, "compression_ratio": 1.7953488372093023, "no_speech_prob":
  0.008322718553245068}, {"id": 809, "seek": 498110, "start": 5001.42, "end": 5005.740000000001,
  "text": " little bit more about chat gbc and as as I''ve been learning about this
  kind of like sequential", "tokens": [51380, 707, 857, 544, 466, 5081, 290, 65, 66,
  293, 382, 382, 286, 600, 668, 2539, 466, 341, 733, 295, 411, 42881, 51596], "temperature":
  0.0, "avg_logprob": -0.22395217895507813, "compression_ratio": 1.7953488372093023,
  "no_speech_prob": 0.008322718553245068}, {"id": 810, "seek": 500574, "start": 5005.74,
  "end": 5011.9, "text": " prompting from gbc index and chain about learning like
  how you can get chat gbc to maybe clean", "tokens": [50364, 12391, 278, 490, 290,
  65, 66, 8186, 293, 5021, 466, 2539, 411, 577, 291, 393, 483, 5081, 290, 65, 66,
  281, 1310, 2541, 50672], "temperature": 0.0, "avg_logprob": -0.1080804583670079,
  "compression_ratio": 1.6711711711711712, "no_speech_prob": 0.00440682889893651},
  {"id": 811, "seek": 500574, "start": 5011.9, "end": 5017.98, "text": " up a podcast
  transcription but there''s like still a pretty fat pretty difficult manual", "tokens":
  [50672, 493, 257, 7367, 35288, 457, 456, 311, 411, 920, 257, 1238, 4046, 1238, 2252,
  9688, 50976], "temperature": 0.0, "avg_logprob": -0.1080804583670079, "compression_ratio":
  1.6711711711711712, "no_speech_prob": 0.00440682889893651}, {"id": 812, "seek":
  500574, "start": 5017.98, "end": 5025.0199999999995, "text": " cleaning effort in
  the middle of that yeah actually I can resonate with that like I''ve I''ve worked",
  "tokens": [50976, 8924, 4630, 294, 264, 2808, 295, 300, 1338, 767, 286, 393, 34285,
  365, 300, 411, 286, 600, 286, 600, 2732, 51328], "temperature": 0.0, "avg_logprob":
  -0.1080804583670079, "compression_ratio": 1.6711711711711712, "no_speech_prob":
  0.00440682889893651}, {"id": 813, "seek": 500574, "start": 5025.9, "end": 5032.54,
  "text": " with one startup helping them to do speech to text right and first of
  all one one issue is", "tokens": [51372, 365, 472, 18578, 4315, 552, 281, 360, 6218,
  281, 2487, 558, 293, 700, 295, 439, 472, 472, 2734, 307, 51704], "temperature":
  0.0, "avg_logprob": -0.1080804583670079, "compression_ratio": 1.6711711711711712,
  "no_speech_prob": 0.00440682889893651}, {"id": 814, "seek": 503254, "start": 5032.54,
  "end": 5038.7, "text": " very similar with low resource so to say languages in an
  OPs that if you don''t have a model", "tokens": [50364, 588, 2531, 365, 2295, 7684,
  370, 281, 584, 8650, 294, 364, 422, 23043, 300, 498, 291, 500, 380, 362, 257, 2316,
  50672], "temperature": 0.0, "avg_logprob": -0.1805364415886697, "compression_ratio":
  1.669603524229075, "no_speech_prob": 0.00454159639775753}, {"id": 815, "seek": 503254,
  "start": 5038.7, "end": 5044.62, "text": " trained on a lot of examples or maybe
  they''ve been trained on some TV shows and you are doing", "tokens": [50672, 8895,
  322, 257, 688, 295, 5110, 420, 1310, 436, 600, 668, 8895, 322, 512, 3558, 3110,
  293, 291, 366, 884, 50968], "temperature": 0.0, "avg_logprob": -0.1805364415886697,
  "compression_ratio": 1.669603524229075, "no_speech_prob": 0.00454159639775753},
  {"id": 816, "seek": 503254, "start": 5045.42, "end": 5053.18, "text": " and a user
  speech stuff you know the topics are different the style is different everything
  is", "tokens": [51008, 293, 257, 4195, 6218, 1507, 291, 458, 264, 8378, 366, 819,
  264, 3758, 307, 819, 1203, 307, 51396], "temperature": 0.0, "avg_logprob": -0.1805364415886697,
  "compression_ratio": 1.669603524229075, "no_speech_prob": 0.00454159639775753},
  {"id": 817, "seek": 503254, "start": 5053.18, "end": 5059.58, "text": " different
  and so it breaks and so I was also eluding to the topic of fine tuning there but
  exactly", "tokens": [51396, 819, 293, 370, 309, 9857, 293, 370, 286, 390, 611, 806,
  33703, 281, 264, 4829, 295, 2489, 15164, 456, 457, 2293, 51716], "temperature":
  0.0, "avg_logprob": -0.1805364415886697, "compression_ratio": 1.669603524229075,
  "no_speech_prob": 0.00454159639775753}, {"id": 818, "seek": 505958, "start": 5059.58,
  "end": 5066.38, "text": " what you said the problem was the output was so noisy
  that I had to write and what I called like", "tokens": [50364, 437, 291, 848, 264,
  1154, 390, 264, 5598, 390, 370, 24518, 300, 286, 632, 281, 2464, 293, 437, 286,
  1219, 411, 50704], "temperature": 0.0, "avg_logprob": -0.12566911797774466, "compression_ratio":
  1.6943231441048034, "no_speech_prob": 0.01362245436757803}, {"id": 819, "seek":
  505958, "start": 5066.38, "end": 5073.42, "text": " an LPLayer which would go and
  you know change things for instance if you say 25 and it actually", "tokens": [50704,
  364, 441, 21593, 11167, 597, 576, 352, 293, 291, 458, 1319, 721, 337, 5197, 498,
  291, 584, 3552, 293, 309, 767, 51056], "temperature": 0.0, "avg_logprob": -0.12566911797774466,
  "compression_ratio": 1.6943231441048034, "no_speech_prob": 0.01362245436757803},
  {"id": 820, "seek": 505958, "start": 5073.42, "end": 5079.82, "text": " spells it
  out with letters you you will collapse that to a number you know but sometimes it
  would", "tokens": [51056, 25053, 309, 484, 365, 7825, 291, 291, 486, 15584, 300,
  281, 257, 1230, 291, 458, 457, 2171, 309, 576, 51376], "temperature": 0.0, "avg_logprob":
  -0.12566911797774466, "compression_ratio": 1.6943231441048034, "no_speech_prob":
  0.01362245436757803}, {"id": 821, "seek": 505958, "start": 5079.82, "end": 5085.9,
  "text": " do it in problematic places and you''re like oh no don''t do that don''t
  do it here you know so like", "tokens": [51376, 360, 309, 294, 19011, 3190, 293,
  291, 434, 411, 1954, 572, 500, 380, 360, 300, 500, 380, 360, 309, 510, 291, 458,
  370, 411, 51680], "temperature": 0.0, "avg_logprob": -0.12566911797774466, "compression_ratio":
  1.6943231441048034, "no_speech_prob": 0.01362245436757803}, {"id": 822, "seek":
  508590, "start": 5085.9, "end": 5094.86, "text": " it''s just like an aftermath
  you know thing and you would wish that the model having enough context", "tokens":
  [50364, 309, 311, 445, 411, 364, 34095, 291, 458, 551, 293, 291, 576, 3172, 300,
  264, 2316, 1419, 1547, 4319, 50812], "temperature": 0.0, "avg_logprob": -0.19235638512505426,
  "compression_ratio": 1.7477477477477477, "no_speech_prob": 0.005314115434885025},
  {"id": 823, "seek": 508590, "start": 5094.86, "end": 5102.299999999999, "text":
  " and knowledge about the world should do it right as it transcribes rather than
  you do this as", "tokens": [50812, 293, 3601, 466, 264, 1002, 820, 360, 309, 558,
  382, 309, 1145, 1142, 6446, 2831, 813, 291, 360, 341, 382, 51184], "temperature":
  0.0, "avg_logprob": -0.19235638512505426, "compression_ratio": 1.7477477477477477,
  "no_speech_prob": 0.005314115434885025}, {"id": 824, "seek": 508590, "start": 5102.299999999999,
  "end": 5108.219999999999, "text": " as a aftermath yeah yeah exactly I''m thinking
  the same way and he''s like it''s a text layer afterwards", "tokens": [51184, 382,
  257, 34095, 1338, 1338, 2293, 286, 478, 1953, 264, 912, 636, 293, 415, 311, 411,
  309, 311, 257, 2487, 4583, 10543, 51480], "temperature": 0.0, "avg_logprob": -0.19235638512505426,
  "compression_ratio": 1.7477477477477477, "no_speech_prob": 0.005314115434885025},
  {"id": 825, "seek": 508590, "start": 5108.7, "end": 5113.58, "text": " yeah yeah
  exactly yeah super cool and then maybe like as we''re wrapping up the podcast if
  you", "tokens": [51504, 1338, 1338, 2293, 1338, 1687, 1627, 293, 550, 1310, 411,
  382, 321, 434, 21993, 493, 264, 7367, 498, 291, 51748], "temperature": 0.0, "avg_logprob":
  -0.19235638512505426, "compression_ratio": 1.7477477477477477, "no_speech_prob":
  0.005314115434885025}, {"id": 826, "seek": 511358, "start": 5113.58, "end": 5118.46,
  "text": " let me quickly tell you about ref to veck and sort of the pivot into recommendation
  and well so to", "tokens": [50364, 718, 385, 2661, 980, 291, 466, 1895, 281, 1241,
  547, 293, 1333, 295, 264, 14538, 666, 11879, 293, 731, 370, 281, 50608], "temperature":
  0.0, "avg_logprob": -0.209107967691684, "compression_ratio": 1.8588235294117648,
  "no_speech_prob": 0.00044177277595736086}, {"id": 827, "seek": 511358, "start":
  5118.46, "end": 5123.26, "text": " start off ref to veck is about and it''s about
  utilizing we VH data model a little more so", "tokens": [50608, 722, 766, 1895,
  281, 1241, 547, 307, 466, 293, 309, 311, 466, 26775, 321, 691, 39, 1412, 2316, 257,
  707, 544, 370, 50848], "temperature": 0.0, "avg_logprob": -0.209107967691684, "compression_ratio":
  1.8588235294117648, "no_speech_prob": 0.00044177277595736086}, {"id": 828, "seek":
  511358, "start": 5123.9, "end": 5128.22, "text": " we VH data model is designed
  where you have different classes so this class could be", "tokens": [50880, 321,
  691, 39, 1412, 2316, 307, 4761, 689, 291, 362, 819, 5359, 370, 341, 1508, 727, 312,
  51096], "temperature": 0.0, "avg_logprob": -0.209107967691684, "compression_ratio":
  1.8588235294117648, "no_speech_prob": 0.00044177277595736086}, {"id": 829, "seek":
  511358, "start": 5129.0199999999995, "end": 5135.1, "text": " products this class
  could be user so you know like tables and SQL we have different data objects like",
  "tokens": [51136, 3383, 341, 1508, 727, 312, 4195, 370, 291, 458, 411, 8020, 293,
  19200, 321, 362, 819, 1412, 6565, 411, 51440], "temperature": 0.0, "avg_logprob":
  -0.209107967691684, "compression_ratio": 1.8588235294117648, "no_speech_prob": 0.00044177277595736086},
  {"id": 830, "seek": 511358, "start": 5135.1, "end": 5140.54, "text": " the high-level
  ideas of designing data objects and then you have graph relations between them like",
  "tokens": [51440, 264, 1090, 12, 12418, 3487, 295, 14685, 1412, 6565, 293, 550,
  291, 362, 4295, 2299, 1296, 552, 411, 51712], "temperature": 0.0, "avg_logprob":
  -0.209107967691684, "compression_ratio": 1.8588235294117648, "no_speech_prob": 0.00044177277595736086},
  {"id": 831, "seek": 514054, "start": 5140.54, "end": 5148.78, "text": " user-like
  products so the simplest thing is that then you can represent the user as the average",
  "tokens": [50364, 4195, 12, 4092, 3383, 370, 264, 22811, 551, 307, 300, 550, 291,
  393, 2906, 264, 4195, 382, 264, 4274, 50776], "temperature": 0.0, "avg_logprob":
  -0.11452786675814924, "compression_ratio": 1.9896373056994818, "no_speech_prob":
  0.000347577384673059}, {"id": 832, "seek": 514054, "start": 5148.78, "end": 5154.38,
  "text": " vector of the products that the user liked and then you can rank with
  you can re-rank with that", "tokens": [50776, 8062, 295, 264, 3383, 300, 264, 4195,
  4501, 293, 550, 291, 393, 6181, 365, 291, 393, 319, 12, 20479, 365, 300, 51056],
  "temperature": 0.0, "avg_logprob": -0.11452786675814924, "compression_ratio": 1.9896373056994818,
  "no_speech_prob": 0.000347577384673059}, {"id": 833, "seek": 514054, "start": 5154.38,
  "end": 5158.06, "text": " or you could just search with that vector that that could
  be your search vector or you could have", "tokens": [51056, 420, 291, 727, 445,
  3164, 365, 300, 8062, 300, 300, 727, 312, 428, 3164, 8062, 420, 291, 727, 362, 51240],
  "temperature": 0.0, "avg_logprob": -0.11452786675814924, "compression_ratio": 1.9896373056994818,
  "no_speech_prob": 0.000347577384673059}, {"id": 834, "seek": 514054, "start": 5158.06,
  "end": 5165.1, "text": " some other search like restaurants in Boston and because
  I live in Boston and you know like oh", "tokens": [51240, 512, 661, 3164, 411, 11486,
  294, 12333, 293, 570, 286, 1621, 294, 12333, 293, 291, 458, 411, 1954, 51592], "temperature":
  0.0, "avg_logprob": -0.11452786675814924, "compression_ratio": 1.9896373056994818,
  "no_speech_prob": 0.000347577384673059}, {"id": 835, "seek": 516510, "start": 5165.26,
  "end": 5171.820000000001, "text": " sorry I didn''t mean to give away Boston in
  the query say I my my query is Italian restaurants", "tokens": [50372, 2597, 286,
  994, 380, 914, 281, 976, 1314, 12333, 294, 264, 14581, 584, 286, 452, 452, 14581,
  307, 10003, 11486, 50700], "temperature": 0.0, "avg_logprob": -0.1631138406950852,
  "compression_ratio": 1.9038461538461537, "no_speech_prob": 0.0005800747312605381},
  {"id": 836, "seek": 516510, "start": 5171.820000000001, "end": 5177.18, "text":
  " and because it sees that Connor likes restaurant I don''t know like some north
  and Italian restaurants", "tokens": [50700, 293, 570, 309, 8194, 300, 33133, 5902,
  6383, 286, 500, 380, 458, 411, 512, 6830, 293, 10003, 11486, 50968], "temperature":
  0.0, "avg_logprob": -0.1631138406950852, "compression_ratio": 1.9038461538461537,
  "no_speech_prob": 0.0005800747312605381}, {"id": 837, "seek": 516510, "start": 5177.18,
  "end": 5182.38, "text": " one way that like it knows that I''m in Boston so it will
  it can personalize just using that vector", "tokens": [50968, 472, 636, 300, 411,
  309, 3255, 300, 286, 478, 294, 12333, 370, 309, 486, 309, 393, 2973, 1125, 445,
  1228, 300, 8062, 51228], "temperature": 0.0, "avg_logprob": -0.1631138406950852,
  "compression_ratio": 1.9038461538461537, "no_speech_prob": 0.0005800747312605381},
  {"id": 838, "seek": 516510, "start": 5183.58, "end": 5187.5, "text": " to re-rank
  to only show me restaurants in Boston because if you show me a restaurant in Chicago
  it''s", "tokens": [51288, 281, 319, 12, 20479, 281, 787, 855, 385, 11486, 294, 12333,
  570, 498, 291, 855, 385, 257, 6383, 294, 9525, 309, 311, 51484], "temperature":
  0.0, "avg_logprob": -0.1631138406950852, "compression_ratio": 1.9038461538461537,
  "no_speech_prob": 0.0005800747312605381}, {"id": 839, "seek": 516510, "start": 5187.5,
  "end": 5194.38, "text": " like useless so so so that''s kind of the first idea is
  this kind of like average the vectors to get", "tokens": [51484, 411, 14115, 370,
  370, 370, 300, 311, 733, 295, 264, 700, 1558, 307, 341, 733, 295, 411, 4274, 264,
  18875, 281, 483, 51828], "temperature": 0.0, "avg_logprob": -0.1631138406950852,
  "compression_ratio": 1.9038461538461537, "no_speech_prob": 0.0005800747312605381},
  {"id": 840, "seek": 519438, "start": 5194.38, "end": 5199.1, "text": " the centroid
  but then there''s this idea where and I learned this from talking to Martin Grootendorce",
  "tokens": [50364, 264, 1489, 6490, 457, 550, 456, 311, 341, 1558, 689, 293, 286,
  3264, 341, 490, 1417, 281, 9184, 12981, 310, 521, 284, 384, 50600], "temperature":
  0.0, "avg_logprob": -0.13192123124579422, "compression_ratio": 1.7392857142857143,
  "no_speech_prob": 0.004371500574052334}, {"id": 841, "seek": 519438, "start": 5199.1,
  "end": 5203.18, "text": " about his burtopic library and I highly recommend people
  check that out it''s such a cool way of", "tokens": [50600, 466, 702, 2779, 83,
  40216, 6405, 293, 286, 5405, 2748, 561, 1520, 300, 484, 309, 311, 1270, 257, 1627,
  636, 295, 50804], "temperature": 0.0, "avg_logprob": -0.13192123124579422, "compression_ratio":
  1.7392857142857143, "no_speech_prob": 0.004371500574052334}, {"id": 842, "seek":
  519438, "start": 5203.18, "end": 5208.86, "text": " visualizing vector spaces but
  this like HDB scan clustering so he was describing the difference", "tokens": [50804,
  5056, 3319, 8062, 7673, 457, 341, 411, 12149, 33, 11049, 596, 48673, 370, 415, 390,
  16141, 264, 2649, 51088], "temperature": 0.0, "avg_logprob": -0.13192123124579422,
  "compression_ratio": 1.7392857142857143, "no_speech_prob": 0.004371500574052334},
  {"id": 843, "seek": 519438, "start": 5208.86, "end": 5213.900000000001, "text":
  " between HDB scan and k-means clustering for how they produce centroids but and
  so HDB scan has", "tokens": [51088, 1296, 12149, 33, 11049, 293, 350, 12, 1398,
  599, 596, 48673, 337, 577, 436, 5258, 1489, 340, 3742, 457, 293, 370, 12149, 33,
  11049, 575, 51340], "temperature": 0.0, "avg_logprob": -0.13192123124579422, "compression_ratio":
  1.7392857142857143, "no_speech_prob": 0.004371500574052334}, {"id": 844, "seek":
  519438, "start": 5213.900000000001, "end": 5218.22, "text": " this very cool like
  density clustering thing but regardless of the clustering you use I just I like",
  "tokens": [51340, 341, 588, 1627, 411, 10305, 596, 48673, 551, 457, 10060, 295,
  264, 596, 48673, 291, 764, 286, 445, 286, 411, 51556], "temperature": 0.0, "avg_logprob":
  -0.13192123124579422, "compression_ratio": 1.7392857142857143, "no_speech_prob":
  0.004371500574052334}, {"id": 845, "seek": 521822, "start": 5218.22, "end": 5223.66,
  "text": " HDB scan a lot but so let''s say we get three centroids like I like Nike
  shoes a data", "tokens": [50364, 12149, 33, 11049, 257, 688, 457, 370, 718, 311,
  584, 321, 483, 1045, 1489, 340, 3742, 411, 286, 411, 30397, 6654, 257, 1412, 50636],
  "temperature": 0.0, "avg_logprob": -0.14020287139075144, "compression_ratio": 1.7969348659003832,
  "no_speech_prob": 0.0009895404800772667}, {"id": 846, "seek": 521822, "start": 5223.66,
  "end": 5228.860000000001, "text": " shoes and Jordan shoes and you have these three
  centroids so you can use those three centroids", "tokens": [50636, 6654, 293, 10979,
  6654, 293, 291, 362, 613, 1045, 1489, 340, 3742, 370, 291, 393, 764, 729, 1045,
  1489, 340, 3742, 50896], "temperature": 0.0, "avg_logprob": -0.14020287139075144,
  "compression_ratio": 1.7969348659003832, "no_speech_prob": 0.0009895404800772667},
  {"id": 847, "seek": 521822, "start": 5228.860000000001, "end": 5233.5, "text": "
  is three average vectors from their respective clusters to re-rank with as well
  have some kind", "tokens": [50896, 307, 1045, 4274, 18875, 490, 641, 23649, 23313,
  281, 319, 12, 20479, 365, 382, 731, 362, 512, 733, 51128], "temperature": 0.0, "avg_logprob":
  -0.14020287139075144, "compression_ratio": 1.7969348659003832, "no_speech_prob":
  0.0009895404800772667}, {"id": 848, "seek": 521822, "start": 5233.5, "end": 5239.1,
  "text": " of diversity and results and then there is just this thinking around so
  so yes there that that''s", "tokens": [51128, 295, 8811, 293, 3542, 293, 550, 456,
  307, 445, 341, 1953, 926, 370, 370, 2086, 456, 300, 300, 311, 51408], "temperature":
  0.0, "avg_logprob": -0.14020287139075144, "compression_ratio": 1.7969348659003832,
  "no_speech_prob": 0.0009895404800772667}, {"id": 849, "seek": 521822, "start": 5239.1,
  "end": 5245.02, "text": " the recommendation pivot and then there''s this idea of
  like top level index and I''m stealing that", "tokens": [51408, 264, 11879, 14538,
  293, 550, 456, 311, 341, 1558, 295, 411, 1192, 1496, 8186, 293, 286, 478, 19757,
  300, 51704], "temperature": 0.0, "avg_logprob": -0.14020287139075144, "compression_ratio":
  1.7969348659003832, "no_speech_prob": 0.0009895404800772667}, {"id": 850, "seek":
  524502, "start": 5245.02, "end": 5251.5, "text": " kind of terminology from gpt
  index because what gpt index does is to represent a long document", "tokens": [50364,
  733, 295, 27575, 490, 290, 662, 8186, 570, 437, 290, 662, 8186, 775, 307, 281, 2906,
  257, 938, 4166, 50688], "temperature": 0.0, "avg_logprob": -0.1530308370236997,
  "compression_ratio": 1.830827067669173, "no_speech_prob": 0.0008654801640659571},
  {"id": 851, "seek": 524502, "start": 5251.5, "end": 5256.540000000001, "text": "
  you have again that tree summarization where you could say this is for obviously
  right and it''s", "tokens": [50688, 291, 362, 797, 300, 4230, 14611, 2144, 689,
  291, 727, 584, 341, 307, 337, 2745, 558, 293, 309, 311, 50940], "temperature": 0.0,
  "avg_logprob": -0.1530308370236997, "compression_ratio": 1.830827067669173, "no_speech_prob":
  0.0008654801640659571}, {"id": 852, "seek": 524502, "start": 5256.540000000001,
  "end": 5261.5, "text": " for and you summarize these two and then summarize one
  and see if this like top level index where you", "tokens": [50940, 337, 293, 291,
  20858, 613, 732, 293, 550, 20858, 472, 293, 536, 498, 341, 411, 1192, 1496, 8186,
  689, 291, 51188], "temperature": 0.0, "avg_logprob": -0.1530308370236997, "compression_ratio":
  1.830827067669173, "no_speech_prob": 0.0008654801640659571}, {"id": 853, "seek":
  524502, "start": 5261.5, "end": 5265.42, "text": " search through this layer first
  and this layer and so it''s like if you''re asking question like", "tokens": [51188,
  3164, 807, 341, 4583, 700, 293, 341, 4583, 293, 370, 309, 311, 411, 498, 291, 434,
  3365, 1168, 411, 51384], "temperature": 0.0, "avg_logprob": -0.1530308370236997,
  "compression_ratio": 1.830827067669173, "no_speech_prob": 0.0008654801640659571},
  {"id": 854, "seek": 524502, "start": 5265.42, "end": 5270.3, "text": " what was
  Barack Obama''s legacy and then you have the symbolic filter of the titles of the
  Wikipedia", "tokens": [51384, 437, 390, 31705, 9560, 311, 11711, 293, 550, 291,
  362, 264, 25755, 6608, 295, 264, 12992, 295, 264, 28999, 51628], "temperature":
  0.0, "avg_logprob": -0.1530308370236997, "compression_ratio": 1.830827067669173,
  "no_speech_prob": 0.0008654801640659571}, {"id": 855, "seek": 527030, "start": 5270.3,
  "end": 5276.3, "text": " pages and you have where title equals Barack Obama like
  that top level search will like super", "tokens": [50364, 7183, 293, 291, 362, 689,
  4876, 6915, 31705, 9560, 411, 300, 1192, 1496, 3164, 486, 411, 1687, 50664], "temperature":
  0.0, "avg_logprob": -0.18939610062358536, "compression_ratio": 1.7954545454545454,
  "no_speech_prob": 0.002997712232172489}, {"id": 856, "seek": 527030, "start": 5276.3,
  "end": 5280.3, "text": " simplified the search space because now you''re just looking
  in the Barack Obama article and there", "tokens": [50664, 26335, 264, 3164, 1901,
  570, 586, 291, 434, 445, 1237, 294, 264, 31705, 9560, 7222, 293, 456, 50864], "temperature":
  0.0, "avg_logprob": -0.18939610062358536, "compression_ratio": 1.7954545454545454,
  "no_speech_prob": 0.002997712232172489}, {"id": 857, "seek": 527030, "start": 5280.3,
  "end": 5287.5, "text": " at all Wikipedia so I think reftivect also in the use of
  having constructing top level indexes by", "tokens": [50864, 412, 439, 28999, 370,
  286, 519, 1895, 83, 592, 557, 611, 294, 264, 764, 295, 1419, 39969, 1192, 1496,
  8186, 279, 538, 51224], "temperature": 0.0, "avg_logprob": -0.18939610062358536,
  "compression_ratio": 1.7954545454545454, "no_speech_prob": 0.002997712232172489},
  {"id": 858, "seek": 527030, "start": 5288.7, "end": 5293.26, "text": " you know
  having document has passage has passage has passage again in the we get data model",
  "tokens": [51284, 291, 458, 1419, 4166, 575, 11497, 575, 11497, 575, 11497, 797,
  294, 264, 321, 483, 1412, 2316, 51512], "temperature": 0.0, "avg_logprob": -0.18939610062358536,
  "compression_ratio": 1.7954545454545454, "no_speech_prob": 0.002997712232172489},
  {"id": 859, "seek": 527030, "start": 5293.820000000001, "end": 5298.3, "text": "
  it can be it''s just like I think it''s a really interesting way that we''re trying
  to use this", "tokens": [51540, 309, 393, 312, 309, 311, 445, 411, 286, 519, 309,
  311, 257, 534, 1880, 636, 300, 321, 434, 1382, 281, 764, 341, 51764], "temperature":
  0.0, "avg_logprob": -0.18939610062358536, "compression_ratio": 1.7954545454545454,
  "no_speech_prob": 0.002997712232172489}, {"id": 860, "seek": 529830, "start": 5298.3,
  "end": 5303.02, "text": " cross-reference graph structure to move embeddings through
  the graph another idea and I know", "tokens": [50364, 3278, 12, 265, 5158, 4295,
  3877, 281, 1286, 12240, 29432, 807, 264, 4295, 1071, 1558, 293, 286, 458, 50600],
  "temperature": 0.0, "avg_logprob": -0.14686332430158341, "compression_ratio": 1.936,
  "no_speech_prob": 0.002331739291548729}, {"id": 861, "seek": 529830, "start": 5303.02,
  "end": 5308.14, "text": " like doing a thousand ideas like it could be having like
  a graph convolutional network where okay so", "tokens": [50600, 411, 884, 257, 4714,
  3487, 411, 309, 727, 312, 1419, 411, 257, 4295, 45216, 304, 3209, 689, 1392, 370,
  50856], "temperature": 0.0, "avg_logprob": -0.14686332430158341, "compression_ratio":
  1.936, "no_speech_prob": 0.002331739291548729}, {"id": 862, "seek": 529830, "start":
  5308.14, "end": 5316.22, "text": " you have user-like product has brand okay let''s
  just make it a three-class graph like that and so", "tokens": [50856, 291, 362,
  4195, 12, 4092, 1674, 575, 3360, 1392, 718, 311, 445, 652, 309, 257, 1045, 12, 11665,
  4295, 411, 300, 293, 370, 51260], "temperature": 0.0, "avg_logprob": -0.14686332430158341,
  "compression_ratio": 1.936, "no_speech_prob": 0.002331739291548729}, {"id": 863,
  "seek": 529830, "start": 5316.22, "end": 5322.06, "text": " you have this this graph
  and you need to send the you need to aggregate the embeddings through the", "tokens":
  [51260, 291, 362, 341, 341, 4295, 293, 291, 643, 281, 2845, 264, 291, 643, 281,
  26118, 264, 12240, 29432, 807, 264, 51552], "temperature": 0.0, "avg_logprob": -0.14686332430158341,
  "compression_ratio": 1.936, "no_speech_prob": 0.002331739291548729}, {"id": 864,
  "seek": 529830, "start": 5322.06, "end": 5326.78, "text": " graph so now it''s like
  should we just average should we try some kind of like nonlinear graph", "tokens":
  [51552, 4295, 370, 586, 309, 311, 411, 820, 321, 445, 4274, 820, 321, 853, 512,
  733, 295, 411, 2107, 28263, 4295, 51788], "temperature": 0.0, "avg_logprob": -0.14686332430158341,
  "compression_ratio": 1.936, "no_speech_prob": 0.002331739291548729}, {"id": 865,
  "seek": 532678, "start": 5326.86, "end": 5331.58, "text": " convolutional network
  and the graph convolutional network being beneficial because a graph network", "tokens":
  [50368, 45216, 304, 3209, 293, 264, 4295, 45216, 304, 3209, 885, 14072, 570, 257,
  4295, 3209, 50604], "temperature": 0.0, "avg_logprob": -0.170864847780184, "compression_ratio":
  1.869281045751634, "no_speech_prob": 0.005384357180446386}, {"id": 866, "seek":
  532678, "start": 5331.58, "end": 5336.7, "text": " can handle like arbitrary number
  of inputs that''s sort of like isn''t like a fixed input size like", "tokens": [50604,
  393, 4813, 411, 23211, 1230, 295, 15743, 300, 311, 1333, 295, 411, 1943, 380, 411,
  257, 6806, 4846, 2744, 411, 50860], "temperature": 0.0, "avg_logprob": -0.170864847780184,
  "compression_ratio": 1.869281045751634, "no_speech_prob": 0.005384357180446386},
  {"id": 867, "seek": 532678, "start": 5336.7, "end": 5341.98, "text": " transformers
  you would like zero-pad it to 512 tokens or the convolutional network is it''s",
  "tokens": [50860, 4088, 433, 291, 576, 411, 4018, 12, 13647, 309, 281, 1025, 4762,
  22667, 420, 264, 45216, 304, 3209, 307, 309, 311, 51124], "temperature": 0.0, "avg_logprob":
  -0.170864847780184, "compression_ratio": 1.869281045751634, "no_speech_prob": 0.005384357180446386},
  {"id": 868, "seek": 532678, "start": 5341.98, "end": 5346.94, "text": " like kind
  of flexible but generally it''s like very flexible to the number of inputs and so
  I hope", "tokens": [51124, 411, 733, 295, 11358, 457, 5101, 309, 311, 411, 588,
  11358, 281, 264, 1230, 295, 15743, 293, 370, 286, 1454, 51372], "temperature": 0.0,
  "avg_logprob": -0.170864847780184, "compression_ratio": 1.869281045751634, "no_speech_prob":
  0.005384357180446386}, {"id": 869, "seek": 532678, "start": 5346.94, "end": 5351.42,
  "text": " that was an okay tour of reftivect and I know I''m trying to get in a
  little bit start it''s amazing", "tokens": [51372, 300, 390, 364, 1392, 3512, 295,
  1895, 83, 592, 557, 293, 286, 458, 286, 478, 1382, 281, 483, 294, 257, 707, 857,
  722, 309, 311, 2243, 51596], "temperature": 0.0, "avg_logprob": -0.170864847780184,
  "compression_ratio": 1.869281045751634, "no_speech_prob": 0.005384357180446386},
  {"id": 870, "seek": 532678, "start": 5351.42, "end": 5356.38, "text": " actually
  and I think I hope we can maybe discuss in subsequent episodes as well because",
  "tokens": [51596, 767, 293, 286, 519, 286, 1454, 321, 393, 1310, 2248, 294, 19962,
  9313, 382, 731, 570, 51844], "temperature": 0.0, "avg_logprob": -0.170864847780184,
  "compression_ratio": 1.869281045751634, "no_speech_prob": 0.005384357180446386},
  {"id": 871, "seek": 535678, "start": 5356.94, "end": 5362.62, "text": " the topic
  of personalization is also very interesting and like for someone who says okay we
  just", "tokens": [50372, 264, 4829, 295, 2973, 2144, 307, 611, 588, 1880, 293, 411,
  337, 1580, 567, 1619, 1392, 321, 445, 50656], "temperature": 0.0, "avg_logprob":
  -0.11284814722397749, "compression_ratio": 1.6896551724137931, "no_speech_prob":
  0.001495433272793889}, {"id": 872, "seek": 535678, "start": 5362.62, "end": 5367.82,
  "text": " have this fixed vectors computed from the content how the hell we can
  actually bring the user", "tokens": [50656, 362, 341, 6806, 18875, 40610, 490, 264,
  2701, 577, 264, 4921, 321, 393, 767, 1565, 264, 4195, 50916], "temperature": 0.0,
  "avg_logprob": -0.11284814722397749, "compression_ratio": 1.6896551724137931, "no_speech_prob":
  0.001495433272793889}, {"id": 873, "seek": 535678, "start": 5368.46, "end": 5374.46,
  "text": " and this is what you''ve described this is what I perceive from it I think
  this is an excellent topic", "tokens": [50948, 293, 341, 307, 437, 291, 600, 7619,
  341, 307, 437, 286, 20281, 490, 309, 286, 519, 341, 307, 364, 7103, 4829, 51248],
  "temperature": 0.0, "avg_logprob": -0.11284814722397749, "compression_ratio": 1.6896551724137931,
  "no_speech_prob": 0.001495433272793889}, {"id": 874, "seek": 535678, "start": 5374.46,
  "end": 5383.34, "text": " and this kind of opens up opportunities for vector search
  to appeal to to the you know search engine", "tokens": [51248, 293, 341, 733, 295,
  9870, 493, 4786, 337, 8062, 3164, 281, 13668, 281, 281, 264, 291, 458, 3164, 2848,
  51692], "temperature": 0.0, "avg_logprob": -0.11284814722397749, "compression_ratio":
  1.6896551724137931, "no_speech_prob": 0.001495433272793889}, {"id": 875, "seek":
  538334, "start": 5383.42, "end": 5391.42, "text": " builder so maybe some other
  engines like recommendation and so but I think we have a ton of material", "tokens":
  [50368, 27377, 370, 1310, 512, 661, 12982, 411, 11879, 293, 370, 457, 286, 519,
  321, 362, 257, 2952, 295, 2527, 50768], "temperature": 0.0, "avg_logprob": -0.267131980406035,
  "compression_ratio": 1.7526881720430108, "no_speech_prob": 0.010554177686572075},
  {"id": 876, "seek": 538334, "start": 5391.42, "end": 5396.62, "text": " I really
  love talking to you maybe before we close off is there something you wanted to announce",
  "tokens": [50768, 286, 534, 959, 1417, 281, 291, 1310, 949, 321, 1998, 766, 307,
  456, 746, 291, 1415, 281, 7478, 51028], "temperature": 0.0, "avg_logprob": -0.267131980406035,
  "compression_ratio": 1.7526881720430108, "no_speech_prob": 0.010554177686572075},
  {"id": 877, "seek": 538334, "start": 5396.62, "end": 5402.3, "text": " to to the
  audience of vector podcast oh yeah I think it was so we have toured a lot of things
  but", "tokens": [51028, 281, 281, 264, 4034, 295, 8062, 7367, 1954, 1338, 286, 519,
  309, 390, 370, 321, 362, 10095, 986, 257, 688, 295, 721, 457, 51312], "temperature":
  0.0, "avg_logprob": -0.267131980406035, "compression_ratio": 1.7526881720430108,
  "no_speech_prob": 0.010554177686572075}, {"id": 878, "seek": 538334, "start": 5402.3,
  "end": 5407.58, "text": " I really hope that you check out the weve 8 beer benchmarks
  repository so this is a recent effort", "tokens": [51312, 286, 534, 1454, 300, 291,
  1520, 484, 264, 321, 303, 1649, 8795, 43751, 25841, 370, 341, 307, 257, 5162, 4630,
  51576], "temperature": 0.0, "avg_logprob": -0.267131980406035, "compression_ratio":
  1.7526881720430108, "no_speech_prob": 0.010554177686572075}, {"id": 879, "seek":
  538334, "start": 5407.58, "end": 5412.06, "text": " around hybrid search coming
  back to that in a long conversation I really thought it was forever", "tokens":
  [51576, 926, 13051, 3164, 1348, 646, 281, 300, 294, 257, 938, 3761, 286, 534, 1194,
  309, 390, 5680, 51800], "temperature": 0.0, "avg_logprob": -0.267131980406035, "compression_ratio":
  1.7526881720430108, "no_speech_prob": 0.010554177686572075}, {"id": 880, "seek":
  541206, "start": 5412.06, "end": 5420.54, "text": " ago but like the hybrid search
  thing has been tested with with the beer benchmarks and so there''s", "tokens":
  [50364, 2057, 457, 411, 264, 13051, 3164, 551, 575, 668, 8246, 365, 365, 264, 8795,
  43751, 293, 370, 456, 311, 50788], "temperature": 0.0, "avg_logprob": -0.1590147664991476,
  "compression_ratio": 2.0121951219512195, "no_speech_prob": 0.002758374437689781},
  {"id": 881, "seek": 541206, "start": 5420.54, "end": 5425.02, "text": " there''s
  like scales there''s like small scale beer medium scale larger scale so right now
  there''s", "tokens": [50788, 456, 311, 411, 17408, 456, 311, 411, 1359, 4373, 8795,
  6399, 4373, 4833, 4373, 370, 558, 586, 456, 311, 51012], "temperature": 0.0, "avg_logprob":
  -0.1590147664991476, "compression_ratio": 2.0121951219512195, "no_speech_prob":
  0.002758374437689781}, {"id": 882, "seek": 541206, "start": 5425.02, "end": 5429.580000000001,
  "text": " the larger scale and some medium scale I''m at smaller scale and some
  medium scale and right now we''re", "tokens": [51012, 264, 4833, 4373, 293, 512,
  6399, 4373, 286, 478, 412, 4356, 4373, 293, 512, 6399, 4373, 293, 558, 586, 321,
  434, 51240], "temperature": 0.0, "avg_logprob": -0.1590147664991476, "compression_ratio":
  2.0121951219512195, "no_speech_prob": 0.002758374437689781}, {"id": 883, "seek":
  541206, "start": 5429.580000000001, "end": 5435.900000000001, "text": " working
  on the backups but this is all based on so we''ve got 1.15 had backups where you
  can you know", "tokens": [51240, 1364, 322, 264, 50160, 457, 341, 307, 439, 2361,
  322, 370, 321, 600, 658, 502, 13, 5211, 632, 50160, 689, 291, 393, 291, 458, 51556],
  "temperature": 0.0, "avg_logprob": -0.1590147664991476, "compression_ratio": 2.0121951219512195,
  "no_speech_prob": 0.002758374437689781}, {"id": 884, "seek": 541206, "start": 5436.54,
  "end": 5441.740000000001, "text": " back up the weve 8 instance to have like a file
  that lets you just restore the weve 8 instance so", "tokens": [51588, 646, 493,
  264, 321, 303, 1649, 5197, 281, 362, 411, 257, 3991, 300, 6653, 291, 445, 15227,
  264, 321, 303, 1649, 5197, 370, 51848], "temperature": 0.0, "avg_logprob": -0.1590147664991476,
  "compression_ratio": 2.0121951219512195, "no_speech_prob": 0.002758374437689781},
  {"id": 885, "seek": 544174, "start": 5441.74, "end": 5445.26, "text": " you don''t
  need to import the data it''s like you know it''s like with the face indexes how
  you can", "tokens": [50364, 291, 500, 380, 643, 281, 974, 264, 1412, 309, 311, 411,
  291, 458, 309, 311, 411, 365, 264, 1851, 8186, 279, 577, 291, 393, 50540], "temperature":
  0.0, "avg_logprob": -0.0960767210022477, "compression_ratio": 1.8643410852713178,
  "no_speech_prob": 0.0001514465839136392}, {"id": 886, "seek": 544174, "start": 5445.26,
  "end": 5451.82, "text": " just read index so so now what you can do is you can just
  load the weve 8 index and so why this", "tokens": [50540, 445, 1401, 8186, 370,
  370, 586, 437, 291, 393, 360, 307, 291, 393, 445, 3677, 264, 321, 303, 1649, 8186,
  293, 370, 983, 341, 50868], "temperature": 0.0, "avg_logprob": -0.0960767210022477,
  "compression_ratio": 1.8643410852713178, "no_speech_prob": 0.0001514465839136392},
  {"id": 887, "seek": 544174, "start": 5451.82, "end": 5456.219999999999, "text":
  " is so exciting to me is I''ve I''ve always been really interested in like hug
  and face data sets or", "tokens": [50868, 307, 370, 4670, 281, 385, 307, 286, 600,
  286, 600, 1009, 668, 534, 3102, 294, 411, 8777, 293, 1851, 1412, 6352, 420, 51088],
  "temperature": 0.0, "avg_logprob": -0.0960767210022477, "compression_ratio": 1.8643410852713178,
  "no_speech_prob": 0.0001514465839136392}, {"id": 888, "seek": 544174, "start": 5456.219999999999,
  "end": 5463.42, "text": " papers with codes papers with data like this organization
  of data and I used to think with like", "tokens": [51088, 10577, 365, 14211, 10577,
  365, 1412, 411, 341, 4475, 295, 1412, 293, 286, 1143, 281, 519, 365, 411, 51448],
  "temperature": 0.0, "avg_logprob": -0.0960767210022477, "compression_ratio": 1.8643410852713178,
  "no_speech_prob": 0.0001514465839136392}, {"id": 889, "seek": 544174, "start": 5463.42,
  "end": 5468.78, "text": " weve 8''s Wikipedia demo that it would need to be like
  live always hosted like you click try it", "tokens": [51448, 321, 303, 1649, 311,
  28999, 10723, 300, 309, 576, 643, 281, 312, 411, 1621, 1009, 19204, 411, 291, 2052,
  853, 309, 51716], "temperature": 0.0, "avg_logprob": -0.0960767210022477, "compression_ratio":
  1.8643410852713178, "no_speech_prob": 0.0001514465839136392}, {"id": 890, "seek":
  546878, "start": 5468.78, "end": 5473.34, "text": " now and then it''s like boom
  you''re in the console and you can query it but I think with these with", "tokens":
  [50364, 586, 293, 550, 309, 311, 411, 9351, 291, 434, 294, 264, 11076, 293, 291,
  393, 14581, 309, 457, 286, 519, 365, 613, 365, 50592], "temperature": 0.0, "avg_logprob":
  -0.09469001019587282, "compression_ratio": 1.850187265917603, "no_speech_prob":
  0.0037916619330644608}, {"id": 891, "seek": 546878, "start": 5473.34, "end": 5478.38,
  "text": " this repo where you just download the Docker file for weve 8 it''s like
  three it''s like two lines of", "tokens": [50592, 341, 49040, 689, 291, 445, 5484,
  264, 33772, 3991, 337, 321, 303, 1649, 309, 311, 411, 1045, 309, 311, 411, 732,
  3876, 295, 50844], "temperature": 0.0, "avg_logprob": -0.09469001019587282, "compression_ratio":
  1.850187265917603, "no_speech_prob": 0.0037916619330644608}, {"id": 892, "seek":
  546878, "start": 5478.38, "end": 5483.9, "text": " code where you do Docker compose
  up and then Python restore the name of the data set you want and I", "tokens": [50844,
  3089, 689, 291, 360, 33772, 35925, 493, 293, 550, 15329, 15227, 264, 1315, 295,
  264, 1412, 992, 291, 528, 293, 286, 51120], "temperature": 0.0, "avg_logprob": -0.09469001019587282,
  "compression_ratio": 1.850187265917603, "no_speech_prob": 0.0037916619330644608},
  {"id": 893, "seek": 546878, "start": 5483.9, "end": 5490.86, "text": " think that''s
  just as easy as having some always hosted demo so yeah I hope and I think the other",
  "tokens": [51120, 519, 300, 311, 445, 382, 1858, 382, 1419, 512, 1009, 19204, 10723,
  370, 1338, 286, 1454, 293, 286, 519, 264, 661, 51468], "temperature": 0.0, "avg_logprob":
  -0.09469001019587282, "compression_ratio": 1.850187265917603, "no_speech_prob":
  0.0037916619330644608}, {"id": 894, "seek": 546878, "start": 5490.86, "end": 5495.5,
  "text": " thing is with with hybrid search another thing that excites me so much
  is it''s like if it''s vector", "tokens": [51468, 551, 307, 365, 365, 13051, 3164,
  1071, 551, 300, 1624, 3324, 385, 370, 709, 307, 309, 311, 411, 498, 309, 311, 8062,
  51700], "temperature": 0.0, "avg_logprob": -0.09469001019587282, "compression_ratio":
  1.850187265917603, "no_speech_prob": 0.0037916619330644608}, {"id": 895, "seek":
  549550, "start": 5495.5, "end": 5500.46, "text": " search only it''s like you could
  argue well why don''t I just use the face index then but I think", "tokens": [50364,
  3164, 787, 309, 311, 411, 291, 727, 9695, 731, 983, 500, 380, 286, 445, 764, 264,
  1851, 8186, 550, 457, 286, 519, 50612], "temperature": 0.0, "avg_logprob": -0.08975315960970792,
  "compression_ratio": 1.7572463768115942, "no_speech_prob": 0.0017455018823966384},
  {"id": 896, "seek": 549550, "start": 5500.46, "end": 5506.38, "text": " because
  it''s got the BM25 and the vector search is starting to offer more value with like
  how it", "tokens": [50612, 570, 309, 311, 658, 264, 15901, 6074, 293, 264, 8062,
  3164, 307, 2891, 281, 2626, 544, 2158, 365, 411, 577, 309, 50908], "temperature":
  0.0, "avg_logprob": -0.08975315960970792, "compression_ratio": 1.7572463768115942,
  "no_speech_prob": 0.0017455018823966384}, {"id": 897, "seek": 549550, "start": 5506.38,
  "end": 5511.26, "text": " can help you with your information retrieval research
  yeah and in general that''s just something", "tokens": [50908, 393, 854, 291, 365,
  428, 1589, 19817, 3337, 2132, 1338, 293, 294, 2674, 300, 311, 445, 746, 51152],
  "temperature": 0.0, "avg_logprob": -0.08975315960970792, "compression_ratio": 1.7572463768115942,
  "no_speech_prob": 0.0017455018823966384}, {"id": 898, "seek": 549550, "start": 5511.26,
  "end": 5515.18, "text": " that is very important to me is trying to figure out how
  to connect with the information retrieval", "tokens": [51152, 300, 307, 588, 1021,
  281, 385, 307, 1382, 281, 2573, 484, 577, 281, 1745, 365, 264, 1589, 19817, 3337,
  51348], "temperature": 0.0, "avg_logprob": -0.08975315960970792, "compression_ratio":
  1.7572463768115942, "no_speech_prob": 0.0017455018823966384}, {"id": 899, "seek":
  549550, "start": 5515.18, "end": 5519.9, "text": " research I think the beer benchmarks
  presents a really exciting way to do it I do have some ideas", "tokens": [51348,
  2132, 286, 519, 264, 8795, 43751, 13533, 257, 534, 4670, 636, 281, 360, 309, 286,
  360, 362, 512, 3487, 51584], "temperature": 0.0, "avg_logprob": -0.08975315960970792,
  "compression_ratio": 1.7572463768115942, "no_speech_prob": 0.0017455018823966384},
  {"id": 900, "seek": 551990, "start": 5519.9, "end": 5526.299999999999, "text": "
  on how users would be interested in it because I think the idea of beer benchmarks
  is maybe you look", "tokens": [50364, 322, 577, 5022, 576, 312, 3102, 294, 309,
  570, 286, 519, 264, 1558, 295, 8795, 43751, 307, 1310, 291, 574, 50684], "temperature":
  0.0, "avg_logprob": -0.13011157954180683, "compression_ratio": 1.7392857142857143,
  "no_speech_prob": 0.005386746022850275}, {"id": 901, "seek": 551990, "start": 5526.299999999999,
  "end": 5532.299999999999, "text": " at it and you say okay NF corpus or trec covid
  or natural questions like very similar to what the", "tokens": [50684, 412, 309,
  293, 291, 584, 1392, 13576, 1181, 31624, 420, 2192, 66, 25616, 420, 3303, 1651,
  411, 588, 2531, 281, 437, 264, 50984], "temperature": 0.0, "avg_logprob": -0.13011157954180683,
  "compression_ratio": 1.7392857142857143, "no_speech_prob": 0.005386746022850275},
  {"id": 902, "seek": 551990, "start": 5532.299999999999, "end": 5538.379999999999,
  "text": " app that I''m building but I think with chat gbt you could probably loop
  through your documents and", "tokens": [50984, 724, 300, 286, 478, 2390, 457, 286,
  519, 365, 5081, 290, 4517, 291, 727, 1391, 6367, 807, 428, 8512, 293, 51288], "temperature":
  0.0, "avg_logprob": -0.13011157954180683, "compression_ratio": 1.7392857142857143,
  "no_speech_prob": 0.005386746022850275}, {"id": 903, "seek": 551990, "start": 5538.379999999999,
  "end": 5543.66, "text": " generate queries gold like those would be the gold documents
  for those queries and you can do", "tokens": [51288, 8460, 24109, 3821, 411, 729,
  576, 312, 264, 3821, 8512, 337, 729, 24109, 293, 291, 393, 360, 51552], "temperature":
  0.0, "avg_logprob": -0.13011157954180683, "compression_ratio": 1.7392857142857143,
  "no_speech_prob": 0.005386746022850275}, {"id": 904, "seek": 551990, "start": 5543.66,
  "end": 5547.099999999999, "text": " the same kind of evaluation testing where as
  you mentioned you want to see how that approximate", "tokens": [51552, 264, 912,
  733, 295, 13344, 4997, 689, 382, 291, 2835, 291, 528, 281, 536, 577, 300, 30874,
  51724], "temperature": 0.0, "avg_logprob": -0.13011157954180683, "compression_ratio":
  1.7392857142857143, "no_speech_prob": 0.005386746022850275}, {"id": 905, "seek":
  554710, "start": 5547.1, "end": 5551.660000000001, "text": " nearest neighbor error
  cascades into the representation error and see what that means for your", "tokens":
  [50364, 23831, 5987, 6713, 3058, 66, 2977, 666, 264, 10290, 6713, 293, 536, 437,
  300, 1355, 337, 428, 50592], "temperature": 0.0, "avg_logprob": -0.15286540985107422,
  "compression_ratio": 1.7105263157894737, "no_speech_prob": 0.01797335408627987},
  {"id": 906, "seek": 554710, "start": 5551.660000000001, "end": 5557.900000000001,
  "text": " particular problem so I hope people check it out I hope find an interesting
  yeah that''s a that''s a", "tokens": [50592, 1729, 1154, 370, 286, 1454, 561, 1520,
  309, 484, 286, 1454, 915, 364, 1880, 1338, 300, 311, 257, 300, 311, 257, 50904],
  "temperature": 0.0, "avg_logprob": -0.15286540985107422, "compression_ratio": 1.7105263157894737,
  "no_speech_prob": 0.01797335408627987}, {"id": 907, "seek": 554710, "start": 5557.900000000001,
  "end": 5565.18, "text": " ton super packed thanks so much what I like in this discussion
  compared to to the last 20 years ago", "tokens": [50904, 2952, 1687, 13265, 3231,
  370, 709, 437, 286, 411, 294, 341, 5017, 5347, 281, 281, 264, 1036, 945, 924, 2057,
  51268], "temperature": 0.0, "avg_logprob": -0.15286540985107422, "compression_ratio":
  1.7105263157894737, "no_speech_prob": 0.01797335408627987}, {"id": 908, "seek":
  554710, "start": 5565.18, "end": 5572.54, "text": " is that you continue to explode
  with knowledge and I hope you will continue doing that thanks so", "tokens": [51268,
  307, 300, 291, 2354, 281, 21411, 365, 3601, 293, 286, 1454, 291, 486, 2354, 884,
  300, 3231, 370, 51636], "temperature": 0.0, "avg_logprob": -0.15286540985107422,
  "compression_ratio": 1.7105263157894737, "no_speech_prob": 0.01797335408627987},
  {"id": 909, "seek": 557254, "start": 5572.54, "end": 5578.7, "text": " much for
  your time today corner and yeah looking forward to talk more yeah thank you so much",
  "tokens": [50364, 709, 337, 428, 565, 965, 4538, 293, 1338, 1237, 2128, 281, 751,
  544, 1338, 1309, 291, 370, 709, 50672], "temperature": 0.0, "avg_logprob": -0.29194930504108296,
  "compression_ratio": 1.7054794520547945, "no_speech_prob": 0.03523525595664978},
  {"id": 910, "seek": 557254, "start": 5578.7, "end": 5586.46, "text": " to me try
  to feel like the vector podcast is like the super bowl of search podcast so thank
  you so", "tokens": [50672, 281, 385, 853, 281, 841, 411, 264, 8062, 7367, 307, 411,
  264, 1687, 6571, 295, 3164, 7367, 370, 1309, 291, 370, 51060], "temperature": 0.0,
  "avg_logprob": -0.29194930504108296, "compression_ratio": 1.7054794520547945, "no_speech_prob":
  0.03523525595664978}, {"id": 911, "seek": 557254, "start": 5586.46, "end": 5592.38,
  "text": " much thank you so much Connor yeah enjoy your day bye bye", "tokens":
  [51060, 709, 1309, 291, 370, 709, 33133, 1338, 2103, 428, 786, 6543, 6543, 51356],
  "temperature": 0.0, "avg_logprob": -0.29194930504108296, "compression_ratio": 1.7054794520547945,
  "no_speech_prob": 0.03523525595664978}]'
---

Hello there, vector podcasts. Season 2, and to them super super super excited to have a reappearance of corner shortened on vector podcasts. We recorded like a year ago about that time. Something's changed. He is a research scientist at Semi Technologies, the company behind VB8.
Here you can see an episode with Bob, and here you can see the episode with Connor as well. And back then when we were talking, Connor, you've been a lot into basketball. Do you still play basketball? Yeah, I still play a little bit.
And I'll add also to that that I think you also have podcasts with Eddie and Laura, also in the queue of we've read. We'll add that. Exactly.
And I remember like you've been big on computer vision, data augmentation back then, and you first like guinea pig task was you know some capturing baskets in the basketball game. And I wonder if you continued working on that at some point.
Yeah, I think about it every now and then, but I've been so captivated by the natural language processing and the tech search honestly. I still think about image search a bit, but yeah, the tech search to me is just it's just so exciting. It feels like there's so much that you can do with it.
And yeah, it's really been it's been an intense year. I've learned so much and I think it'll be a totally different podcast with respect to like what I'm this talking about. Yeah, yeah, absolutely.
I actually love to start also by asking you, what do you feel you've learned in this year that has changed something fundamentally in how you perceive vector search today versus back then and year ago? Yeah, that's a big question. I think I'm definitely with we V8.
I've learned a lot about having like kind of the user focus, the product focus definitely way more engineering understanding of the distributed data system, replication, cap theorem, all these kind of things.
So like the knowledge of the engineering around it in addition to sort of the machine learning research about like how to vector representations get optimized with deep learning models and then you know, this whole retrieve and read research.
And overall the space is evolved in such an amazing way and it's just really exciting. Yeah, absolutely.
I've been I've been also following all different things reading papers, you know, implementing clip, but I still feel like I miss out on so many things and I really hope we will cover some of them today.
And we on the verge of I think maybe witnessing a change in the search paradigm, you know, with chat GPT. I first I wanted to sort of get your first reaction on this. Obviously you tested it. I also tested it actually with when I published my recent blog post on neural search frameworks.
And I was like just stuck on creating a title and I asked chat GPT, can you come up with a title and came up with a reasonably good title and I actually used it without editing. And I read a bunch of other stories, you know, like for example, how you can avoid fines, for wrong parking and stuff.
But then there is this discussion going on, you know, like how it may change search.
But before that, what was your impression of chat GPT? Yeah, well, I think like everyone else sort of in in this like reading about say Google's flan model or, you know, that we've been kind of reading about a lot of these large language models, but we haven't actually really gotten to use them.
 I think Facebook's OPT model was on hugging face and I played with that and back in back at the time, I was mostly like the few shot learning part was like the part that was so exciting where you could, you know, give it like for example, of a task and then it could just instantly learn the task and that's like pretty surprising for people who've been doing supervised learning optimization for a long time.
And so mostly my thinking was a few shot learning, but this chat GPT thing, this reinforced learning from human feedback, this like I mean the way that it can talk is just mind blowing.
It's I'm so amazed by and I think yeah, it's really unlocked a lot of thinking about the importance of prompting to me and what prompting means. I used to think that was just kind of like a task description idea, which it still kind of is, but it's like the nuances of it are so much.
And yeah, I'd really love to like dive into this topic of large language models and search and I have a few different dimensions of how I'm kind of thinking about these two things relating to each other, but since I've brought up prompting, I kind of want to stay on this one quickly.
So Bob and Jerry Lou showed me this thing called GPT index and GPT index has this strategy for prompting GPT for summarization.
It has other things, but this is one thing that just really stood out to me and there are like two strategies you can use to summarize long text with the large language model.
 You can either create and refine where you go paragraph by paragraph and you say like you start up by please write a summary of this long text, you'll receive a paragraph by paragraph and then it iteratively updates a summary or you can have this tree where you you know you chunk it up like you know as a tree and then you couple it like recursively and then build up the summary that way.
So this kind of thing about like how we use these large language models all of it is so interesting and so I guess kind of yeah, let me pass it back to you and I'm curious like how do you think large language models will change search?
Yeah, I mean I'm still kind of learning it and I having you know built search engine before vector search you know using like TFIDF basically.
I knew the cost of doing it wrong you know or sort of focusing too much on precision and then paying a huge bill because of that.
 So like our search engine for example back in the days when we indexed on sentence level in alpha sense would eat something like half a terabyte memory and you know memory was never cheap like it was very expensive even back then and so we had to figure out ways to retain precision, not lose recall or maybe even increase recall because there was a problem with this precision oriented search and stay within the budget right so when I think about language models myself and I also worked at silo AI at one large client you know applying these models at web scale.
 The problem at web scale is that you really need to go sub-second and not just sub-second you need to go like 10 milliseconds or so because all of these adapt because you have so many components in the search engine it's also multilingual it's also serving a specific country you know with that specific latency requirements and stuff and and then there is indexing how quickly you can index things right because you may also face bottlenecks there so these these are the things that I keep thinking about but also the thing that we talked a year ago in the port in the same podcast vector podcast is that you know the models like trained by Microsoft for instance I can hardly imagine deploying them today in my practical setting because they will have like billions of parameters and so they will be probably slower and also how do I fine tune them how much server capacity I will need to fine tune them and so that's why I thought you know from the discussion with multi-peach right he pointed me to the Atlas paper where they basically are able to with a few examples fine tune the model so quickly and it will have substantially less parameters so it becomes more practical you know both on fine tuning side and also on serving side and these are the topics that I keep thinking before I enter the is it chat GPT is it sexy is it cool is it answering my questions you know can I actually deploy it and not have angry faces from DevOps saying hey you just crossed all the like we are low margin on search and you are just you know way above that so sorry we cannot deploy this so these are the questions I'm thinking about a lot yeah that I think there's a couple things in pack and no one's helped me develop the abstraction around the end-to-end search framework more than you so thank you so with the with the pyramid diagrams and these kind of things it's so helpful and yeah you mentioned like the approximate nearest neighbor then one up you have where I see is the information retrieval layer where you have the you know dense vector search BM25 split covert that layer and then at the top you have like what I think is going to be the chat GPT layer that's like that would be my current predict and we're going to talk about neural search frameworks that they can do more on the wv8 podcast yeah well maybe to just say a little bit one of our favorite partners that we've been working with is neural magic and neural magic is doing sparsity inference acceleration where they've recently one of their papers is about getting the 175 billion parameter GPT model to run on a single GPU I know that you know you can probably compile these large language models on like Nvidia Triton server and do it that way but I think that this sparsity acceleration for CPUs is just incredibly exciting for that particular dimension of it and yeah I think what you said inspired so many ideas yeah I sort of like like what I value in your approach is that you run probably like a basketball player converted into a marathon runner with the same capacity you have to play a game you know that you basically run super quick and fast and long distances you know on the research side and I love this approach really really because it opens up a lot of opportunities I sort of like because I come from the engineering background yeah I did my PhD but it was like 11 years ago so I most of my time I spent in production you know great systems and every time you just try to move a little bit like okay let's add this and oh the cost is this oh sorry okay it will take me now to two more weeks to index my content so and we have for this what is the use case so you trickle back to like almost like product level management and so you will get these questions inevitably like okay why are we doing this like what's the actual trade off what's the benefit of bringing this into production right and but at the same time I'm fascinated by this I mean this will not stop for sure right would you agree to that statement yeah I think and there's uh so I know Hagen Faces recently published their they open source of data said they did with surge AI on getting these um human annotations to train the reward model in the reinforced learning human feedback strategy so I think they'll they'll be an open sourcing of the data of the data that you need to train the models and then yeah I think pretty soon they'll be open source versions of it I think open AI um I I'm very curious about this like kind of data flywheel idea whereby open sourcing the model they spend a ton of money on letting you use it for free but then they get the data of how you want to use it and so very curious how that leads to more to a better model my PhD advisor is a world class expert in class imbalance like understanding that machine learning models they do not perform well on long tail you know if you have an imbalance data so it's a lot of like the bias discussion things like that so I'm I'm curious maybe it helps the long tail getting all this data yeah it's still not exactly how it will get better I think one thing I've said previously is like there was this paper from Emily Bender and um caller is the last name sorry it but it's called unmeaning understanding in big data and it makes this argument that it's like language models by predicting the next token will never achieve meaning because it's like an octopus underneath the ocean of two stranded islanders and it's just mimicking their language but if it if something like a bear is to show up on the island and it goes help a bear then the octopus is like oh I don't know what a bear is like yeah I'll do more but I think what we're seeing with the reinforcement learning thing is that it's like it's acting it's there's there's this other paper called experience grounds language it's about you you need to it's like the levels of sort of developing meaning and one of it is like about the importance of acting acting in your environment I'm I'm kind of going around right here but I also see like this causal inference stuff and uh Judea Pearl has this ladder of causality where uh it's you act you make interventions but then the the the the top of the ladder of causality is you can understand uh counterfactuals and so that last part I have no idea how that's going to be achieved yet but I clearly chat GPT is now like acting so it's different from the yeah yeah the next word thing yeah I think what coming back to chat GPT like what um impressed me maybe the most is uh so I had I had this problem uh I was I was working on billion scale and then search algorithm with with the group of researchers and and engineers like almost a year ago so I invented this this algorithm I called it candy like of course you know not not meaning my surname but in any case with a k um it's all open source and GitHub I'll make sure to link it and so the the problem was that it it would work on 10 million vectors it would work on 100 million vectors but it would choke on one billion it would basically run out of memory uh and and I did it entirely in python right so maybe I I should have chosen in retrospect some other language but in any case I wanted to make this work um I couldn't I ran out of time and I ran out of computer resource because it was given to us by Microsoft um for a limited period of time so what I did is that I pasted that code into chat chat GPT and I said yeah first of all I tried to paste the whole thing but it said well it's too long so I had to focus on a specific part where I think the the problem you know kind of lurks and and it gave me the answer it said okay maybe try avoid using non-py arrays as much as you do try to pre-allocate them try to reset them and actually I did that I just didn't paste that portion of the code which was doing this so the the system didn't know that but it was on the right on the right track but then when I did it a year sorry a day later the answer changed the question was exactly same but the answer changed and that kind of make me really like uh what's going on like is it learning as it goes can you explain this part like have you seen this in his behavior like was the casting generation of the yeah chat GPT sorry I was like I was trying to follow along with the I think we're going to talk about like approximation error with the AN and search as we scale it and I know we're coming back to the chat GPT but I'll be uh yeah so it's like uh it's like a tree decoding where uh it it has a probability density on the length of vocabulary and you can take several paths through that tree for what you're going to output and uh you often randomly sample through the through the tree if that makes sense like um yeah yeah me does but I mean the answer was kind of like in some sense these two answers were complementary to each other right and and maybe I could go on and say hey what do you mean by resetting can you because it didn't provide any uh code examples it would just say reset and I was like what do you mean by reset I don't have such a method like like like so I I think that that was maybe impressive part of chat GPT and um just to close off on that there was a recent discussion on on relevancy and matching text like where a lot of these search people see uh there was um there was this argument against chat GPT that let's say if you go um you know use uh duck duck go today you will see the links right you can go and examine the links and you can actually verify the information to some extent maybe not to full extent but to some extent in chat GPT you can do that there is an answer that's it so it's it's quite a jump from being able to kind of seemingly check the is it trustworthy to well you have no way to do that what do you think of this aspect yeah that's brilliant I it makes me think about like well very broadly it makes me think about artificial general intelligence compared to super intelligence sort so to say and like I think about the artificial general intelligence and like because open AI they've published web GPT and instruct GPT so instruct GPT is like the reinforcement learning from human feedback part and then web GPT is like the like the whole idea that we're super excited about at wevea where you search for context to append to the input and then like if you say like please uh ground your answer in this information and then it's a paragraph about like how the BM25 algorithm works like I use this personally that way to hybrid search and understanding it and so like if you give it the context it's so much better and so I think I suspect that chat GBC under the hood does something like a Google or a Bing API search and so it's like general old but um yeah this idea like so so so then this idea of super intelligence it uh because I've been like can I use chat GPT to help me write like you know blog post survey papers things like that are relevant for trying to be a master of search and what I need from it is more so like citation recommendation right like I needed to go into like uh Leo Boystov's publications and parse it out for me and help me understand what he's done so it's like the specific information and then yeah the real I mean u.
com also has a really brilliant thing where it's uh search engine on this panel and then the chat GBC on this side so it's like a user interface problem I think yeah yeah but but I mean maybe even yeah I totally agree with you that user interface definitely creates the bias uh how we like how you use traffic lights today they go like red you know yellow and green they don't go upside down right and like if you see an upside down you will you will think well this is a wrong uh traffic light uh I'd rather not cross here you know but like it's kind of like similar here like with the search engines we are used to seeing you know URLs and and being able to click there but of course if you take Google or I guess being does that too they also pre-generate this answers answer boxes right so you can answer you can click there but I don't think you have a URL to verify you know the source of this information if I'm not wrong yeah yeah so they already playing with incorporating this knowledge from a language model right and they they they look at you and of course they also want you to spend more time on their page which is probably not good but we'll not discuss that so they don't share the traffic further but but the thing is you know they still play with the idea okay what if we try to answer not just with the URL and summary but actually with the actual thing right with the actual answer oh so that comes into like the extractive versus abstractive and like whether you want the question answering models that classify the answers in the context yeah and yeah I think that still has a place for sure I mean it's super lightweight as I mentioned Neural Magic they just did a sparse question answering model that can run on CPU super fast and yeah I think that approach is also just gonna be more cost effective for a while yeah exactly but you mentioned BM25 and I'm curious like I've been trying to approach this hybrid search topic but I think you went ahead all right so and I was just wondering like what's your take on this topic like can you a little like intro it to our listeners but also why do you think it's a good idea to to build like a hybrid search you know combining keyboard retrieval with it's with a you know dense retrieval yeah awesome I started by saying this has just been like the most satisfying project I've worked on since I've joined Wevegate and just being a part of this team and it's been you know like a big team working on hybrid search and it's just been an incredible experience so I guess starting yeah the motivation is BM25 has this it builds on term frequency inverse document frequency by adding like this binary independence model and the IDF calculation and then you also normalize it for the length of the document that's just like these subtle differences that make it different than TF IDF but you could also use TF IDF in hybrid search if that's what you were after and so then you also have the vector search and then you have this rank fusion so so we look we found this paper where they have seven different strategies for rank fusion it's like rrf board uh I don't know come some but in the end we just went with rrf reciprocal rank fusion which is just erica's recently published a blog post that shows the equation and just tells some of our thinking around it but it's where you just combine the ranks compared to say combining the scores because you know BM25 has a score particularly and vector search has like a distance at return so you might look at some way of like linearly or non-linearly combining those scores and I've done some experiments with with kind of my thinking around it was like okay what would be like an optimal alpha per query would that be you know maybe like a conditional model like so I tried this with the few shot learning of gbt3 where you you run a few examples of the optimal alpha and then you try to see uh you know how would you like to wait BM25 and dense vector search given this query and see if that is productive but I found and this is a very interesting thing because I think people have this idea that BM25 is like very interpretable but in my experience it hasn't been that I when you do when you're doing longish queries in long documents and maybe we can talk about long queries or short queries but I find that trying to decode why it why BM25 was better than dense search for some particular query I find that to be impossible and maybe someone will prove it wrong and I'll look forward to seeing that honestly but like there's this example that we have as you know erica was developing the weviate error demonstration of hybrid search where the query how to catch an elaskin Pollock and the idea being that the dense vector search contributes the disambiguation of catch that it prefers to fishing and that BM25 is specific to elaskin Pollock but I haven't been able to just like inspect that kind of behavior as I look through the beer benchmarks that just I'm super excited to talk about that and how we've been evaluating it but you know let me let me pass it back to you and ask about your experience with them BM25 or like the keyword and the dense search particularly because then I'd like to kind of take the topic to just arbitrary combinations of retrieval methods not just be in 25 and say DPR or whatever yeah I think I remember even before the dense search appeared on the scene we were experimenting with sort of like making TFI DF which is BM25 is like an addon like BM25 I think stands for best match so period so solved problem solved but you know like one of the questions the the reason I love working with product managers and at the moment I am a product manager so I took the other side of this thing maybe we can talk more about it in the VV8 podcast but you know the reason I love talking to product managers is because they don't know anything maybe they don't know that much about algorithms as you and they don't code maybe as much as you but they do care for they are the stakeholders of the end result right so when they go out talk to sales or to the end users they will not get a question which alpha you have used now coming back to your to your example right they will say hey I typed cat three times in my query and I still see that the document that mentions it once is at the top how can you explain this I will try to link there is a consulting company I think they're based in Boston actually by the way I just forget their name key and via something so they have a really great presentation on haystack life I believe where they go super deep and I recommend you watch it super super deep on how TF IDF screws up our understanding of how things should work what they don't you know and they go by you know how many times you know the word cat is mentioned in the document versus how many times it's it's mentioned in the query and you can do all this combinatorial you know combinations and then they kind of like explain what you would do to kind of solve it right and you you basically develop this situation another another thing is that I found useful and it also mentioned in the relevant search book by Dr.
 Nbal and Jerry Bareman that you can you can use like if you would use like let's say elastic search or similar system or solar you could actually build a function which explains the query step by step right so it basically prints you the tree of how it actually came up with that final answer with that final score and how you know that specific field like for example at TomTom we would I cannot go into much specifics what we do at TomTom but basically the geographic search right so you type some destination let's say an address or maybe a P.
O.
I name point of interest like a shop and it's multilingual as well right so obviously your query may hit by accident sometimes in a wrong language field and so the only way to know this is to print that query execution formula if you will right and so you will see okay ah it hit in that in that let's say I don't know a French uh but I wasn't intending French I was doing German or something why did it do that and you start reasoning about how did I create the tokens because when you tokenize your text it's same problem is as in then search in a way like when you split text into paragraphs or sentences there you need to split the tokens how you do split the tokens is dependent on how you model the semantics of what you are converting to to a token so you should not convert string to a token you should convert meaning to a token so if you capture meaning in that token then you're done in a way but then coming back to your question I cannot answer it fully now but I highly recommend that that talk um by can be so you know like you need to you need to see how term frequencies and inverse document frequencies play together and also like in BM25 versus TFID if you have the term saturation issue which is kind of mitigated in BM25 to some extent right so meeting that if you have two documents um sorry if you have two terms which occur like one is like million times and the other one one million plus one TFID will be unable to distinguish between these two but like BM25 is still sensitive to these things and that's why it's a little better right so I think it solves this term saturation issue I don't know if I answered your question but no yeah I think um so yeah a couple things I really want to continue on this TFID versus BM25 and then adverse displayed to it I think you're I think this like pseudo relevance feedback is that like the phrase I give to show that like um if you're searching with BM25 you say if you had added this key like you have the gold document and you're like how would I have modified the query to produce that document is it so I think that yeah that's one way another way is to how would you modify the indexing that's more in your control right so how you would modify the indexing for example you would in some cases you can remove the applicates or something right so like you don't you don't need them or something like that you can you can or you can split the term by numbers or something right if they happen to occur inside the term something like I'm making these examples but I'm saying that you have more control in the indexing than in the query but in the in the query you can model like query similarity for example right so yeah oh that's super interesting yeah the the way that you do like the text preprocessing like stemming stopper removal all that all that that bag of that's what I hope dense vector search can kill all that I hope you can just like anything can go into it yeah and but um yeah and so I think there's this this thing called like decoding the latent space of a vector search model on that other idea of what query would have produced this where you would take the you would train a language model on document query pairs and then it would generate a query that would have matched the document maybe that's useful but but I'm also I'm very curious what you think about this idea of split vectors so split vectors is like you keep the mass language modeling head and so you encode the thing into the vectors so the mass language modeling head always only takes in a vector as input you always would mask out whatever the mass token was and then send just that vector to the mass language modeling head that will produce like a sparse distribution over what would replace it and so I think the the idea behind split is that you do that for each token and then you just kind of average all the vocabulary distributions and that gives you a sparse vector that represents like the like happy euphoric ecstatic like the kind of synonyms behind it do you like that kind of idea yeah yeah uh uh I like that the fact that I think we can step back from like this dense vector limitations and go back and try to capture what sparse vectors do because if I don't know if you watch the episode with duck Turnbull but he actually shed the light on on this really well by saying hey if you if you take the keyword retrieval inverted index you deal with like probably hundreds of thousands of dimensions unless millions unless billions like in some of the indexes we had at least million per term right so that's like million positions most of which are zeros because this term doesn't occur you know in in specific doc but like doc id but like it occurs like in a few and so in dense retrieval you sort of like compress all of these to let's say 256 dimensions and inherently you lose the precision right so it becomes more like recall oriented rather than you know in sparse you you basically like what also it means spars is that this is probably like a little bit like going back to n and algorithms right so like an inverted index it's basically like a hash table so I have this term it's like order one look up in the hash table and then you leapfrog you use this leapfrog algorithm implemented really well in leucine for example how you jump over long strides of consecutive doc id's because you don't really need to examine them in an antiquity let's say if it's cat and dog you know you know that cat occurs in the document id5 well I don't know like 10 let's say and for dog you are on on on three so you can leapfrog all the way to 10 you don't really need to check all this in because they will never occur together so for or query that's another story because that's a union but for and query it's an intersection so you always need an intersection you can then stop early because you don't need 100,000 results on the screen right and I'm still actually curious on how would you know when to stop because what if you didn't find the document that is even more relevant that what you have seen so far but that's like a matter of debate I guess but then you start scoring them and then sorting them were relevance right yeah sorry if I'm a little behind them so is this referring to how you can use like an inverted index to calculate the BM25 scores so I would you know with my document collection if dog appears I you know dog and the documents so that when I'm calculating yeah yeah but like the the the the I guess the comparison I wanted to make to dance search that like an old vector search is that they are on the on the base data structure first of all you have a choice of the algorithm you want to use but let's say we take hnsw which is the most popular right also implemented in v8 I know but like you don't know when you enter the first layer you don't know where exactly you will end up like so like with hash table I know exactly where I'm entering and I know that I'm exactly in the right place right and you know you can also expand your query with synonyms then you enter more more points in the hash table and you start traversing all of them in parallel and you come up with the answer but in dance search you need to like accept the uncertainty of navigating that graph you don't know where it will land it has certain limitations and trade-offs and then it will pull up you know some nearest neighbors and probably you should be happy with them because oh otherwise you need to do it twice so that price and so on you see what I mean right so like they are fundamentally different also on search side oh in like this stochastic nature of the yeah and also I read this paper called OOD disganan that talks about how much the distribution shift can impact the graph based vimana so vimana is like hnsw but you flatten it so there's no longer the hierarchy of layers it's like all the same thing and then you can put it on disk and it's like a little cheaper run I think yeah it's fascinating the whole indexing the part that that's like kind of the the meat of this especially from wavy aspect of that's where I see and in addition to you know the ux and making it like a very developer friendly to well there's a few sides to it because there's also the distributed database part and you know all the written and go laying the concurrency control you know the replication of the backups like all these kind of things like that so it's definitely like some things to but that approximate nearest neighbor search and I know that you have this experience with you know I've listened to a ton of your talks and you're you introduced me to the a and n benchmarks but yeah that I see that there is being like three levels of errors that come that propagate up there's the errors from hnsw and say product quantization then there's the errors from the vector representations to begin with and then there's maybe the errors and like the question answering model so if you wanted to have like you know natural questions open domain qa you're looking at like three layers of cascading errors that are sort of unrelated to each other yeah exactly people really brilliantly that you like and I think if I may summarize it you know I anyway to you know kind of where this hat of the person who is creating this doctor search pyramid and stuff I'm not the only guy doing this but I keep doing this because it helps me to stay comfortable in the topic and sort of okay I'm looking at it from this angle and if you accept it stay with me if you don't you know you may you may as well augment it or something like you did earlier with some levels and you know like it's just you need to accept that uncertainty like you explained and also that uncertainty that you know like in this can and paper they they explicitly show that in hnsw you may have unreachable nodes and they counted something like 1000 nodes were completely unreachable from any point in the graph like no matter how you search how long you search what are the values for your e f and m parameters during index construction and search you just don't reach them and and that's I think that's somewhat similar to the inverted index search where you have like one million uh doc IDs per term how do you know when to stop it's also like you may never reach the documents that you should have visited but you just deliberately decided to stop you know prematurely because you don't have time you have to you know return the documents within night and 10 milliseconds so you have to make trade-offs um but they are ordered naturally in in the increasing order of doc IDs right they're not ordered by does this question answer anything does this does this document know anything about cats or it just not mentions them and passing you know does this document knows anything about tweeter does it describe tweeter or just says you know please contact me on twitter here is my twitter handle right like complete noise uh so so you see what I mean right so like there are I think in both approaches like on fundamental level on data structure level we deal with this fundamental limitations like gravity law like you cannot jump off and and fly to moon or to Mars right without additional like thrust and devices and stuff yeah so do you feel the same like does it resonate oh yeah well firstly thank you that you just explained that concept to me for the first time I'm just I'm just now alive on the podcast understanding that concept but yeah it's very it's very cool like the um sorting the inverted index to prioritize documents maybe by clicks like clicks would be like like the most sensible thing if it's like web pages so to say and you sort the documents and then you yeah you have some kind you could probably calculate how much time you have to search and how much that lets you go into the invert index yeah super interesting I I think it's very interesting for wevia with the with the hybrid search in the beam 25 index because I I know the inverted index has been explored because we have this uh like neuro symbolic search where you would annotate properties like you you're searching through let's say you have a billion sneaker images but you've also labeled the color they are so you have red is the color and then you can use that to filter the search so there's definitely been some foundation in pre filtering and integrating uh these kind of symbolic inverted indexes with h and s w so it's not like the first time we've yet it's ever exploring that but I yeah there's definitely nuances with the beam 25 because of the cardinality of how many terms you like with the document I think you're splitting it I don't know 300 words right like 300 300 words per property so the just the size of it um I mean starting to go into the thinking around like the sizes of things it inspired me when when you're mentioning the compression bottleneck from sparse to dense I was thinking like okay let's say we have 384 dimensional vectors that have 32 bits per uh vector position like what is that is that is that 384 or 324 or 32 or you know like that it's still a massive common tutorial space right yes exactly exactly and and and you said like is it even the model that captures everything we need to capture right it in all of these are numbers of course it's kind of number representation of the models understanding well understanding in quotes of of the objects that we index uh but I guess like for me like um and you're way ahead in this I feel like that uh with VBA development like um of me you know what matters to me when I was like a search engineer day to day is what tools not necessarily tools as in specific programs but like tools as in algorithms approaches I have to control the process right so if somebody comes up and says hey can you look in this query can you debug it first of all like explain queries one brilliant way of doing it and that's where you start but then once you understood aha there is a problem that it hits this field or I give too much of a boost uh in this situation what should I do so you start like tweaking these parameters and you have these tools in your hands right you can do that in vector search I I don't know like I have like probably fine tuning as one tool right so like if clip stops working on these images I can go and fine tune or bird um but what else do I have like I can also tune some parameters in hnsw or gskn and so or something I can make all these thousand nodes reachable like they didn't this can and I can choose disk over RAM if I want to save on you know on cost and stuff but what else do I have as a control to actually go and debug and fix that specific query like what has been your experience on that or maybe thinking uh yeah I think you've named them all I mean I know I've seen like um like the tuning of the EF construction as you mentioned with hnsw and I guess something that I'm really excited about with these beer benchmarks and maybe I can introduce it now because I think it helps with this idea of model selection in terms of the user's perspective on how can I debug my system how do I fix my search system so the beer benchmarks is it's about diverse text retrieval so you know it's like arguana NF corpus track covid is the difference is instead of saying that the search image net is going to be ms marco which is you know like 10 million being passages and like a million labeled query so it's like the image net idea of like this general source of it like image net is like a massive collection of images labeled in a bunch of categories so it's like it's like is ms marco the search image net but it seems like instead we're going for diversity with beer and I think also if we all if we want to talk about intent intents and instructions further I think actually beer is I think beer had another there's latte like L O T T E capital T's like they go they go beverages right so yeah so there's like an equivalent to beer and then there's also miracle which is for multilingual so there's a lot of these like diverse text retrieval and then and then it's expanding where you would label it with the instructions as well and I don't remember the names of these data sets off the top of my head because it's very new but I know this paper called task aware retrieval with instructions and I think there's a model another paper with a model called instructor so this is idea where you also label with the intent but but anyways let me go back to the focus on like how does a user debug the search system and say how can I fix it so the idea with the beer benchmarks like one idea would be that we could test several different models and you could maybe say like okay well I'm building a nutrition I'm building a nutrition search apps I'm like I'm like bodybuilding.
com or something like that and so you would look at the NF corpus results and you would see the performance of the different models and that would maybe help you take a different model off the shelf but then what you're saying with like fine tuning it I suspect that fine tuning is going to be a super powerful lever I think if you find like and maybe later there's so many topics I want to talk to you about.
 Like with the idea of I've been building a Wevey-A demo of the podcast search so I've been taking the Wevey-A podcast parsing the transcriptions and putting them in there in my temptation to like fine tune it and start thinking about this positive negative construction for that I mean I think in general with Wevey-A we're kind of you know letting like you know we use open AI models co-hear models, hugging face models and it's like we're not really training the models but it's just such an interesting thing to tune I know Gina AI's fine tuner is extremely interesting that I do find myself like constantly pulled in that direction of like wanting to train models.
 Yeah absolutely I've been when we when we presented Mewves at Berlin Buzzwords last year now we actually said we also have Mewver which is the component to allowing you to fine tune a model we kind of like don't have it for prime time but I've been like really fascinated kind of coding a bit of that and and checking how well it can can work in a more generic way you know because I think fine tuner allows you to plug in several models you know and like because different models have different inputs they have different like setting to train and fine tune and so you need to be aware of that like Clip is that is a kind of two tower in a way right so you do need text you do need the image but I think I feel like coming back to the question like what tools I have I feel like fine tuning and I feel like you agree to that the fine tuning is one way that should be more available to the masses should be more available to the users in a way that they are aware of this tool and they know you know best sort of like know how how to use them and also pitfalls you may fall into and I think this is what you brilliantly described like a year ago in the context of computer vision like data augmentation right so like it's one thing that you can feed you can feed some manual examples but how far you can go and like in your basketball example like you've been manually labeling some examples like you run out of patience in a way right okay you can hire people to do that but is that scalable probably not and also new trends come up like if you take a business specifically working on e-commerce or I don't know full text document search you know things come up every week maybe right so like I don't know Tesla releasing cyber truck and you don't have it in the in the model so it actually like in your example what was it with the ocean and like yeah I hear you say like how to catch an Alaska Pollock and then let's pretend that Alaska Pollock is a new fish that like you maybe with vector search you may try to find what could be the most similar object but it may also be wrong right or in the case when the distance is so big that it doesn't make sense anymore to consider this as a candidate right so yeah so this is this is very interesting like and I hear that you you really want to like dive into fine tuning topic as well right yeah well that idea is amazing because there this argument and I also when I interviewed multi-peach he gave me these three reasons to favor the retrieve then read approach to large language models and one of which was this idea that you can swap out the information to update it with new information cyber truck becomes a new thing and then you can put it in the context and now the language model just has the reason across the context but then as you say the embedding model doesn't know about the new thing so the embedding model you know also isn't going to pick it up and so yeah I think that continuous updating one idea that I'm just incredibly excited about I haven't figured out how to make this work yet but the idea would be you you're the ML ops problem of this is you need to re-vectorize your data set which yeah so the solution maybe is that you could vectorize like a thousand representative documents and my hypothesis is that the proximity graph from I want to say Vamanum or Southern H and SW because I barely understand graph neural networks let alone trying to make it a hierarchical neural network but like if it's if it's the proximity graph maybe you can it's like it's like it's like a psycho again it's very similar to like image to image translation or any kind of you know it's a vector space to vector space translation and so you you know you input the vector output the change in vector and so can you vectorize like a thousand and then propagate that throughout the graph it or throughout the corpus and maybe that proximity graph has some kind of bias that facilitates the optimization task or maybe the graph neural network thing is too much overhead and you're better off just having like a transformer that takes into vector outputs a vector but yeah that this idea of like how do you continually update your embedding models it's fascinating right yeah yeah especially the ML ops aspect of it as you've mentioned like if if we were to insert new neighbors into the existing graph right would that change it favors something more recent or would it like break something that we didn't want to break and things but but in some sense if you think about coming back like we are still in the realm of this hybrid search topic in a way right if you look at BM25 OTF idea of approach right so if you compute so you're I so you term frequency is only dependent on this document right so that's fine it's kind of the independent of all other documents but your inverse document frequency is dependent on the whole corpus which is indexed in that chart by the way that's another like big topic which is kind of like crossing the boundary of is this just infrastructure issue in slash engineering is this kind of like research issue and it's like it's fuzzy it's it's it's it's a blend and so for that chart you're gonna have that local idea unless you build a a higher level cache which will keep track of each individual chart's idea and roll it up to the global idea and like if you look at Apache Solar I think I believe they had a country module or something implementing this where you can actually implement a global cache with IDF which will live on top of the chart and now you're coming back to MLOBS you need to make sure it never dies because if it dies you go back to like the chart level IDF and so that becomes dependent on okay I have managed to stuff stuff a lot of documents about cats in this chart so the IDF is like this and then I stuff a lot of documents on dogs here so they become like unbalanced if you if you know what I mean so they it's not a healthy mix of term statistics in your collection right and that will influence a lot of things like you may say in some cases it's okay but in some other cases it may not work if your query contains you know both concepts and they are unequally represented somehow in your in your collection right so so I mean does it make sense I mean so it's like you do have limitations also and and not limitations but maybe I should pose it in more positive way research tasks right so such challenges what should we do and I hope that in some sense dense search is pushing us to think more and more about this and maybe some things will back lash from vector search back to the you know classical keyword retrieval and maybe some new data structures will even emerge to to tackle these things yeah I think that idea that you're describing on the IDF caching it's super interesting I think it is it is inspiring me just thinking generally about how we're trading knowledge on this thing in general and having this podcast and having this content and this communication and how we've you know done like our first iteration of BN25 and yeah like learning so much about the index structure it is really really interesting I was thinking about like oh well how about displayed vectors could could we just kind of update the mass language modeling head to get the new terms and would that be easier than this kind of global cache I like idea and is it more forward thinking and then yeah it's really interesting I think maybe one other idea is this thing called colbert which is like a token level representation thing where it's like they call it late interaction where first you do the you know the standard vector search but then you keep the token vectors for each of the vectors and and then you do that and then they've had efficiency improvements on that so like I think they in the original colbert they they've recently published this paper I know Christopher Pots and Omar Kataba I'm sorry I don't know like I'll show my best like no give everyone credit all the time but in this paper they describe it like the original colbert is like in 154 gigabyte index compared to like one gigabyte with other methods and so so yeah like efficient indexing and I'm definitely running a van but it is like a big thing to unpack there's so much depth to this and that's what makes working in this field so exciting is that there's so much opportunity so much to explore yeah yeah and so much unsolved as well I don't I don't know if you wanted to continue a thought oh no sorry yeah I was just yeah I mean we are branching out but like actually one thing that you just reminded me there was a maybe I should start writing a book or something because like the moment I remember this I should write a chapter and then keep adding and then publish it maybe you can be my author or something yeah that was just thinking it was was it like 10 years ago on Berlin buzzwords there was a presentation by one of the engineers at Twitter I don't know if he's still a Twitter and I forgot his name I remember he was German working out from San Francisco and he basically coming back to that issue with you know sorted document ideas right what they did at Twitter first of all you know the scale of Twitter is such that you cannot possibly store Lucine index on disk and then go and retrieve it because well it's just way too slow right what they did is that they moved the whole index into memory right so they had to rewrite Lucine to kind of like this memory friendly data structure and one thing they did in particular is that as tweets come in each tweet is a document it gets its unique document they deem and they would append this new document ID to the postings list in the end right so for this term so they would decompose it into terms back and then they would know okay I need now to update that specific terms posting list so the posting list is just the array of dock IDs so they would put that Twitter tweets dock ID in the end and as the new searcher comes in searching tweets they would read backwards from the end they wouldn't read from the beginning of so basically what they did is that they kind of like encoded the temporal nature of tweets and people what end users wanting to search and view the tweets which are the most fresh so like like I don't know if like you are the heavy user of Twitter I do you know like on Twitter like when I log in and I check my timeline like usually I see something super fresh and then I keep scrolling but like not like anti-props to Twitter but it's it's a nightmare to search on Twitter like when I search something I know existed like a week ago there is no way for me to find it unless I know the exact tweet ID right and so at some point I was even indexing tweets actually direct messages I had with few people you know in solar and then basically searching them so because it was way faster than searching them on Twitter because like if you have 5,000 direct messages scrolling through them will take half a day so because they keep loading and loading so basically what I'm trying to say is that they optimize the data structure for the nature of usage of Twitter in such a way that they bias to the recent tweets and they don't care if you will have to spend a day retrieving like super all tweet like it's like so my new user use case for them for the majority of users 99% of users will only want to see and consume the latest thing so in some sense this is kind of the effect of optimizing to the usage like what you say we could optimize you know like split or or similar you know sparse lllm or something to kind of like learn you know that latest beat and maybe there is a high chance of it being retrieved as well so we might as well bias the system to that but then of course there is catastrophic forgetting thing and stuff like that.
 Yeah there's no is yes not an easy problem to continually update the mlm head either it would be maybe worth adding that this mlm head insplay doesn't need to be like a billion parameters well maybe a billion would be good but it doesn't need to be a hundred billion or like yeah that's such a fascinating nugget of system design you just shared at the Twitter thing and yeah it's really interesting I've seen this other company called perplexity AI that Ravine Shrinivas is I think he's a founder CEO of it and it's cool because he was he worked on curl with Peter Rebele on this contrastive representation learning for robotics where they're you know they're doing the same kind of idea vector optimization to learn a state space for robotic control on so I think it's really cool that now he's working on the search space too but they have it's like the other approach is like natural language to SQL it's something like that where like instead of and I'm getting a little off topic but it's like kind of related to Twitter and it's about like putting tweets into you know data stores and then parsing natural language queries into the SQL but so that's like another idea I guess is like you would parse the query yeah I think I'm already explaining what do you think about that idea like you you take the query and you turn it into an SQL query in like that's it yes yes I know what you mean it's like it's very similar I think deep said did that right so you can or maybe it's opposite I'm not sure but like if you have a probably the same if you have like a table right you know with fields and rows I don't know let's say list of mountains with their heights and so on so you can actually have a question what is the tallest mountain in Europe or Asia you could turn that query in natural language into SQL command and say you know select you know mountains from this mountains table order by height reverse right descending and so I like this idea and in fact actually I've I think first of all this is already doable right so I'm fine just stood with like with the deep set doing that in haystack but I also came across this idea during my PhD research because so the problem there I believe was that it was like these engineers working on building aircrafts and so they had to read a ton of manuals but once you read the manual you still need to go and look up that specific number somewhere in the database right so so basically they do like multiple multiple hop approach and that may take like forever like you first of all you need to crunch through a ton of you know text material and then somehow summarize it and then okay now I need to go and look up that that number in the database but what if you could ask a natural language question to the manuals then convert that to a SQL command which would know to go and look up in that specific database table and give you the answer so like the manual doesn't have it but it has some instructions how to find it and then you would kind of like convert that into through this metal language convert that into SQL and then get that answer right and this was like pre-dense retrieval in era obviously but I think I still feel like it has the merit to like well I guess two things I think first there's this problem where you search like for error line manual some specific detail and it's like in result seven like it almost got it like it's not like not in the top 100 but it's seven and to that problem is where I think this GPT index like recursive summarization or create and refine summarization I think that'll solve that problem and yeah well so I then coming back to this idea of natural language to SQL and like structured unstructured data on the other end you can also parse the tables into text and so I've seen that done too there's like wiki tables to text and so me personally my favorite application is is scientific literature mining and searching through scientific papers and so you could parse out the tables to turn like the results tables to turn it into natural language and I mean there's so many fascinating things so it's like with a knowledge let's say like a knowledge graph the idea of the knowledge graph is if I have Demetri Khan host the vector podcast is a product manager at Tom Tom I with knowledge graph I can you know I compress the representation of all these facts into one structure compared to having the set of sentences right and yeah so maybe if I can kind of plug something I've done so I have this paper that will be published pretty soon it's about it's in the Florida Atlantic University PhD it's an interdisciplinary team with the College of Nursing and a local healthcare system so we have electronic health records that describe COVID-19 patients and we're trying to predict survival outcome treatment forecasting prognosis all that kind of stuff and so the the thing that we explored in this paper is let's switch from the structured tabular data to parsing it into natural language text and let's turn it into like clinical narratives or let's do this thing where you do if X if feature name equals if feature name equals then label right yeah so there's a paper from the University of Wisconsin called language interface fine tuning where they do that same idea but it's you know like the UCI machine learning repository data sets so so I think I know that I've taken like a walker and also to think it's cool it's cool I'm sure now listeners will be like what but I know like it's it's also what I heard from my listeners for example in the podcast is that they actually do use this episode as an educational material so that's why you know if we can stuff as many links to papers and your work they can go and study this yeah go go go I do some rise I guess the question is like how are we thinking about structured and unstructured data the deep learning systems you could parse out the structure into unstructure and then you have the transfer learning is really easy right yeah yes or you can keep the structure and then maybe you can learn a better representation thanks to the structure and with that question my interest has been really heavily in these causal digs and this idea of creating structured causal relationships between variables I still have no idea how that really how you can take like Wikipedia text and turn it into a causal diagram but I have an idea of like if and it comes back to this agi versus super intelligence idea if I have a super intelligence and it's reading search literature I want it to have some kind of causal diagram of our current model of search stuff so like it has some model of how BM25 is index the limitations of it's blade this representation this MLOVs problem it has like some structured representation of all these problems such that when the new batch of archive papers or tweets you know however the news is coming into it or experiments right it looks at its causal diagram to say like this violated my this this claim like because that's the thing you see a paper like autoregressive models as as search engines or you see like what's the name of that where it's like transformers is a differentiable search index like you see some title like that that violates your causal diagram of why things are the way they are and that's what like inspires your interest so that's that particular angle of it is yeah yeah I'm not mostly thinking I haven't explored this topic myself yet but so let's say if you take a language model like bird which was kind of like you could say statically trained once on Wikipedia or news content right but the world is changing every single day right your model doesn't so what you could do is that you could introduce knowledge back to the model and I'm still like on the on the brisk of kind of exploring this I think new tremors talked about it recently like how you can incorporate knowledge in the language model so for instance what like the way I see this before I even like read this paper so I could probably try to invent reinvent the wheel is that so the language model might figure out that the question is about the president of the United States that specific one let's say Obama something but then the question is is Obama still the president of the United States and so now the language model is kind of like hentik app that says well I actually don't have last I know like chat gpd does that right like I was trained by 2021 so I have no idea what happened in 2022 sorry goodbye but like it could actually say it could say I figured out the context I know roughly what you're asking this is the person I know this person I know that what what the president means I know the the country United States but you're asking me a factual question so what it could do is actually it could go and ask a knowledge graph which is updated without recalculating the the embeddings which is solving them all of this problem right so it's it's it's another data structure you know it's a knowledge graph it's being updated as we go and so it goes and says hey let's coming back to your question on on structured language like in in graph systems you also need to form your query in a certain way so it forms the query in a certain way and traverses the graph and then checks is Obama the president the answer is no it goes back all the way to maybe a language model I don't mean some other layer and basically presents the answer to the user right yeah so that's just one thought before even dove into this topic of incorporating knowledge in elabs I would probably think like that yeah I love that you brother that knowledge graph it's like and that's kind of like GBT index as well as laying chain I can't believe I haven't brought that up until now we can talk about that more in the neural search frameworks discussion on the review podcast but like this idea of different kinds of external memory and I don't know what's wrong with my brain today and I keep like branching into completely I don't think it's wrong I think it's the right setting it's just not suitable with the coding or something but um like so I was recently talking with Shukri who just joined we've got as well about um about this idea of metadata re-ranking so one approach is you have the xg boost re-ranker where you take in the bm25 score the vector distance and then also symbolic features as the input to the re to the xg boost re-ranker so the thing he was okay do we want to store this metadata in weveate as well or do we go get it from redis or feature store something like that where we get that kind of property and so it's like the knowledge graph the idea connects to that because it's like okay are we going to build the knowledge graph in weveate should it live in weveate or should we plug weveate in with something like Neo4j or or is it a top level controller like the neural search frameworks thing you're describing where it's you know something that hooks into weveate and hooks into Neo4j relational AI tiger graph I don't know all the rdf ontology technologies but you know like it has separate and it's a higher level that picks between the indexes so it's yeah it's like what kind of technology is built and weveate and that's not even really up to me you know exactly but I think it's kind of fun to brainstorm with you like what like we kind of like intuitively find this limitations together and at the same time this limitations may lead to future discoveries like on engineering and research and like when I was giving this keynote at Haystack where by the way weveate guys will surprise and another guys as well like I didn't I didn't feel bold enough to say this but I think I will say this now at least that I feel like engineering and research are kind of like indistinguishable in the amount of intelligent power you need to put into this to solve it because it's not like given right like if this data structure inverted index is designed like this and you do have the the issue of early termination because you cannot like waste so many CPU cycles then like okay without reading papers can you go and solve it like being just an engineer so to say no you can't it's like it's it's super hard like you need to start coming up with like new vector space model which was invented when in 60s 70s I don't know so like can you come up with like completing your model it's it's it's equally hard as in research when okay you know that SOTA is now this can I beat it somehow but it's not like you're just beating sort of for the sake of it maybe some people do but like I would take a stance of not doing that like I would try to solve an existing problem right so I do want to surface as you said more relevant document to the top or maybe even the passage maybe in a number so I keep pushing for that so both of these to me they're like they require so much intelligence so that they become indistinguishable in some sense like what exactly are you now solving the MLOPS problem are you solving the you know the inverted index data structure limitation problem or are you solving how do I retrain the embeddings how did you train the model or fine tune the model and I don't recompute the embeddings because it's a way to expand so it's to pay the bill yes does it does it resonate with you like what what are your thoughts of that yeah our ct oeddy and delocca has written about product engineering and like on this meta on this meta of like how do these decisions get made and it's like I think there's a book called change my office I have a bookshelf behind me I used to be in podcasts and I'd be like it's that yeah yeah I still have it actually yes but it's like it's like ask your developer is a title something like that about and well okay so that maybe maybe I got a little off with this idea of research and engineering I think the the scientist is very like a metrics oriented in a different way like the the engineer like the the diversity of the tests and the data collection is more important when you're the when you're the scientist sort of uh yeah the the engineer needs to build like smoke tests sort of where whereas I see the scientist needs to like have a very rigorous data collection kind of because that's sort of how I see the distinction and responsibility sort of is that makes sense yeah it does it does actually yeah you you uh you gave a very good distinctive you know feature what I was trying to say is that like in engineering you still have a plethora of options like it's combinatorial explosions in certain cases there are also mundane parts in both of these right so like we are not talking about them but like they do exist but like you do have these points like okay should I branch this way or that way should I step back and rethink and and that's yeah but I agree I agree you you gave a really good example of like in research I do care about data so much in engineering it's probably the quality assurance department is going to worry about okay what data we're going to feed into the system to try to kind of maybe break it and see limits and where it breaks what do we need to fix um or is it kind of like stable what it proved enough to release you know things like that so but yeah I think if I can stay on this a little more I think this like generalization testing like the industry of quality assurance but 4D learning is is going to be really fascinating I'm like excited like how I think when we first met you had written this um not all vector databases are equal and I thought that was so insightful because it was like a you told the story of an emerging market and that was so interesting I really look forward to seeing like the story of the emerging market around generalization testing I think like um like with the beer benchmarks that kind of thing where it's like you create some million scale data set and have the NDCG recall precision with all these queries I think maybe also this idea of like AB testing with models is going to be more popular I was when I went to Neurops this year and there is this talk from Dr.
 Juhau came about interaction centric AI and how that might differ from the first paradigm of model centric AI where say you judge the image generation model purely based on like inception score for shade is tends to feature spaces in real images and then to data centric AI which is like I think snorkel AI is very responsible for like branding that term and making it so popular but it's like you're really focusing on the curation of data like your language model is like mosaic and oslatus pub med gpt it's about like you have this particular data and you like clean it and you make it awesome and then I think interaction centric AI is like a new way to evaluate models where it's like AB testing driven kind of or like how quickly can you perform a test I don't know if I've gotten too else topic but no I think it's it's exactly the topic to focus on if we are serious about you know putting these things out in production like you do need you do need to have and provide an evidence to the stakeholders that and to yourself that this dust hold water and we can release it and it's not going to show something you know in discriminate to the users that they will be completely you know puzzled and stuff or maybe you know there are all these numerous examples when like Google search when they I think incorporated some distilled version of bird when they would flip the meaning and they would say you do take this medicine but actually in the prescription it says you do not take that medicine or vice versa you know because it's not sensitive to negations and stuff so like I totally agree I'm with you on that like how do we QA quality of sure you know that the systems that release and I think the open AI team did that brilliant trick in a way that they said hey here is the chat GPT go test it and they get like million users in the first few days because they actually do need some extra brains to do go and test in different like scenarios and see where it breaks maybe it doesn't make sense anymore so yeah it's my understanding that's how like scale AI became the kings is that you know like labeled data like mechanical Turk I think Sir J.
I.
 is something that's emerging that I've been seeing yeah it's really interesting yeah exactly um yeah um I was I was wondering um you you also worked on this podcast search and you had the opinion that Whisper has some bottlenecks I wonder if you if you want to like tap into that a little bit yeah so I'd love to tell this story so uh so it comes the kind of story behind it is uh so Boris power at open AI tweeted uh so they they cut the prices for the open AI embeddings and and Boris is pointing out how cheap it would be to index a massive podcast like the Joe Rogan podcast so that's how I was like hey I have a podcast and you have a vector podcast and we did also but so I started to be you know I started doing this where you you know you take the audio files then you put them into Whisper I also tried like uh descript is something that I like a lot I've been using descript for a long time for editing videos and so it's like you still because you it's very the podcast transcriptions you still want to edit them a bit you you have like uh and like like if you were yes how I'm pausing right now I'm talking about but the transcriptions it's not quite what you want to like index to this idea of like how do we create a knowledge base from these podcasts because these podcasts is so like we've covered so many topics and it's so it's kind of easier to do it like this than to be writing all this down and then and also it's very collaborative uh like the podcast you get more people involved it's like a community building thing is so yeah that idea of creating knowledge bases out of podcasts like what would you write your interest on a scale of one to 10 of having a vector podcast I mean I would love to join to join the you know to join the geek here so because I do like I was rewatching the episode with you Danny here we go and you were like exploding with knowledge right like in a way you're branching out a lot today as well exploding with knowledge because you you read all these papers you try things you share you know like google collapse and stuff but like like how do I tap into this knowledge like it's it's very synchronous right I have to like there is no way to like random jump into hey where did he talk about you know that model from Microsoft like I don't know unless I have the time code I don't have a way to do that right so yeah yeah and I what that's what inspires me so much with I want to fine-tune these models so badly just on the uh turn taking as the positive labeling and yeah I think can you expand a bit more on that what do you mean uh okay Conor says I want to talk about the turn taking Demetri can you expand on that more on what that means Conor okay it's like this is how you do the positive thing that's like potentially like that yeah yeah yeah and like if you want to have more examples of what Conor said like you could like augment with Conor's uh statements uh oh like sentences yeah yeah and just the I feel like the potential of it is crazy I also think like we're gonna see it like hooked into say Spotify are these big platforms that organize podcasts and I think it'll help you like discover like because something else it's like I love how you do this vector search podcast and I'm also doing a vector search podcast and it's like who else is out there doing like maybe a recommendation podcast or like you know like it's like this kind of discovery about the people because podcasting is very like collaborative it is a medium right like it is not like you you can't do it by yourself no like it's like it's it's almost like the thing uh like stand up comedian so anyone who is presenting you do need the audience because you simply do not generate the 3d-ness of your thoughts in absence of people like it's very hard to do and then same thing happens here right now like when we exchange like I like I have like a full shade of these notes and stuff right so I wouldn't be able like what like do I do you know these things do I know some of these things you know it's like a vote if working in your memory but like coming back to whisper like just to get it right you you're saying it's still a bottle neck in your opinion in what way okay well I'd hate to be like quoted as saying it's not good if it's not the same thing which I value you know it's not yeah so if you're creating a podcast search app you like there's still needs to be a little more parsing I don't know if you need to find I don't know if you need to correct one and then fine tune so because I've also been playing a little bit more about chat gbc and as as I've been learning about this kind of like sequential prompting from gbc index and chain about learning like how you can get chat gbc to maybe clean up a podcast transcription but there's like still a pretty fat pretty difficult manual cleaning effort in the middle of that yeah actually I can resonate with that like I've I've worked with one startup helping them to do speech to text right and first of all one one issue is very similar with low resource so to say languages in an OPs that if you don't have a model trained on a lot of examples or maybe they've been trained on some TV shows and you are doing and a user speech stuff you know the topics are different the style is different everything is different and so it breaks and so I was also eluding to the topic of fine tuning there but exactly what you said the problem was the output was so noisy that I had to write and what I called like an LPLayer which would go and you know change things for instance if you say 25 and it actually spells it out with letters you you will collapse that to a number you know but sometimes it would do it in problematic places and you're like oh no don't do that don't do it here you know so like it's just like an aftermath you know thing and you would wish that the model having enough context and knowledge about the world should do it right as it transcribes rather than you do this as as a aftermath yeah yeah exactly I'm thinking the same way and he's like it's a text layer afterwards yeah yeah exactly yeah super cool and then maybe like as we're wrapping up the podcast if you let me quickly tell you about ref to veck and sort of the pivot into recommendation and well so to start off ref to veck is about and it's about utilizing we VH data model a little more so we VH data model is designed where you have different classes so this class could be products this class could be user so you know like tables and SQL we have different data objects like the high-level ideas of designing data objects and then you have graph relations between them like user-like products so the simplest thing is that then you can represent the user as the average vector of the products that the user liked and then you can rank with you can re-rank with that or you could just search with that vector that that could be your search vector or you could have some other search like restaurants in Boston and because I live in Boston and you know like oh sorry I didn't mean to give away Boston in the query say I my my query is Italian restaurants and because it sees that Connor likes restaurant I don't know like some north and Italian restaurants one way that like it knows that I'm in Boston so it will it can personalize just using that vector to re-rank to only show me restaurants in Boston because if you show me a restaurant in Chicago it's like useless so so so that's kind of the first idea is this kind of like average the vectors to get the centroid but then there's this idea where and I learned this from talking to Martin Grootendorce about his burtopic library and I highly recommend people check that out it's such a cool way of visualizing vector spaces but this like HDB scan clustering so he was describing the difference between HDB scan and k-means clustering for how they produce centroids but and so HDB scan has this very cool like density clustering thing but regardless of the clustering you use I just I like HDB scan a lot but so let's say we get three centroids like I like Nike shoes a data shoes and Jordan shoes and you have these three centroids so you can use those three centroids is three average vectors from their respective clusters to re-rank with as well have some kind of diversity and results and then there is just this thinking around so so yes there that that's the recommendation pivot and then there's this idea of like top level index and I'm stealing that kind of terminology from gpt index because what gpt index does is to represent a long document you have again that tree summarization where you could say this is for obviously right and it's for and you summarize these two and then summarize one and see if this like top level index where you search through this layer first and this layer and so it's like if you're asking question like what was Barack Obama's legacy and then you have the symbolic filter of the titles of the Wikipedia pages and you have where title equals Barack Obama like that top level search will like super simplified the search space because now you're just looking in the Barack Obama article and there at all Wikipedia so I think reftivect also in the use of having constructing top level indexes by you know having document has passage has passage has passage again in the we get data model it can be it's just like I think it's a really interesting way that we're trying to use this cross-reference graph structure to move embeddings through the graph another idea and I know like doing a thousand ideas like it could be having like a graph convolutional network where okay so you have user-like product has brand okay let's just make it a three-class graph like that and so you have this this graph and you need to send the you need to aggregate the embeddings through the graph so now it's like should we just average should we try some kind of like nonlinear graph convolutional network and the graph convolutional network being beneficial because a graph network can handle like arbitrary number of inputs that's sort of like isn't like a fixed input size like transformers you would like zero-pad it to 512 tokens or the convolutional network is it's like kind of flexible but generally it's like very flexible to the number of inputs and so I hope that was an okay tour of reftivect and I know I'm trying to get in a little bit start it's amazing actually and I think I hope we can maybe discuss in subsequent episodes as well because the topic of personalization is also very interesting and like for someone who says okay we just have this fixed vectors computed from the content how the hell we can actually bring the user and this is what you've described this is what I perceive from it I think this is an excellent topic and this kind of opens up opportunities for vector search to appeal to to the you know search engine builder so maybe some other engines like recommendation and so but I think we have a ton of material I really love talking to you maybe before we close off is there something you wanted to announce to to the audience of vector podcast oh yeah I think it was so we have toured a lot of things but I really hope that you check out the weve 8 beer benchmarks repository so this is a recent effort around hybrid search coming back to that in a long conversation I really thought it was forever ago but like the hybrid search thing has been tested with with the beer benchmarks and so there's there's like scales there's like small scale beer medium scale larger scale so right now there's the larger scale and some medium scale I'm at smaller scale and some medium scale and right now we're working on the backups but this is all based on so we've got 1.
15 had backups where you can you know back up the weve 8 instance to have like a file that lets you just restore the weve 8 instance so you don't need to import the data it's like you know it's like with the face indexes how you can just read index so so now what you can do is you can just load the weve 8 index and so why this is so exciting to me is I've I've always been really interested in like hug and face data sets or papers with codes papers with data like this organization of data and I used to think with like weve 8's Wikipedia demo that it would need to be like live always hosted like you click try it now and then it's like boom you're in the console and you can query it but I think with these with this repo where you just download the Docker file for weve 8 it's like three it's like two lines of code where you do Docker compose up and then Python restore the name of the data set you want and I think that's just as easy as having some always hosted demo so yeah I hope and I think the other thing is with with hybrid search another thing that excites me so much is it's like if it's vector search only it's like you could argue well why don't I just use the face index then but I think because it's got the BM25 and the vector search is starting to offer more value with like how it can help you with your information retrieval research yeah and in general that's just something that is very important to me is trying to figure out how to connect with the information retrieval research I think the beer benchmarks presents a really exciting way to do it I do have some ideas on how users would be interested in it because I think the idea of beer benchmarks is maybe you look at it and you say okay NF corpus or trec covid or natural questions like very similar to what the app that I'm building but I think with chat gbt you could probably loop through your documents and generate queries gold like those would be the gold documents for those queries and you can do the same kind of evaluation testing where as you mentioned you want to see how that approximate nearest neighbor error cascades into the representation error and see what that means for your particular problem so I hope people check it out I hope find an interesting yeah that's a that's a ton super packed thanks so much what I like in this discussion compared to to the last 20 years ago is that you continue to explode with knowledge and I hope you will continue doing that thanks so much for your time today corner and yeah looking forward to talk more yeah thank you so much to me try to feel like the vector podcast is like the super bowl of search podcast so thank you so much thank you so much Connor yeah enjoy your day bye bye