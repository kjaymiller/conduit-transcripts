---
description: '<p>00:00 Introduction</p><p>01:11 Yaniv’s background and intro to Searchium
  &amp; GSI</p><p>04:12 Ways to consume the APU acceleration for vector search</p><p>05:39
  Power consumption dimension in vector search </p><p>7:40 Place of the platform in
  terms of applications, use cases and developer experience</p><p>12:06 Advantages
  of APU Vector Search Plugins for Elasticsearch and OpenSearch compared to their
  own implementations</p><p>17:54 Everyone needs to save: the economic profile of
  the APU solution</p><p>20:51 Features and ANN algorithms in the solution</p><p>24:23
  Consumers most interested in dedicated hardware for vector search vs SaaS</p><p>27:08
  Vector Database or a relevance oriented application?</p><p>33:51 Where to go with
  vector search?</p><p>42:38 How Vector Search fits into Search</p><p>48:58 Role of
  the human in the AI loop</p><p>58:05 The missing bit in the AI/ML/Search space</p><p>1:06:37
  Magical WHY question</p><p>1:09:54 Announcements</p><p>- Searchium vector search:
  <a href="https://searchium.ai/">https://searchium.ai/</a></p><p>- Dr. Avidan Akerib,
  founder behind the APU technology: <a href="https://www.linkedin.com/in/avidan-akerib-phd-bbb35b12/">https://www.linkedin.com/in/avidan-akerib-phd-bbb35b12/</a></p><p>-
  OpenSearch benchmark for performance tuning: <a href="https://betterprogramming.pub/tired-of-troubleshooting-idle-search-resources-use-opensearch-benchmark-for-performance-tuning-d4277c9f724">https://betterprogramming.pub/tired-of-troubleshooting-idle-search-resources-use-opensearch-benchmark-for-performance-tuning-d4277c9f724</a></p><p>-
  APU KNN plugin for OpenSearch: <a href="https://towardsdatascience.com/bolster-opensearch-performance-with-5-simple-steps-ca7d21234f6b">https://towardsdatascience.com/bolster-opensearch-performance-with-5-simple-steps-ca7d21234f6b</a></p><p>-
  Multilingual and Multimodal Search with Hardware Acceleration: <a href="https://blog.muves.io/multilingual-and-multimodal-vector-search-with-hardware-acceleration-2091a825de78">https://blog.muves.io/multilingual-and-multimodal-vector-search-with-hardware-acceleration-2091a825de78</a></p><p>-
  Muves talk at Berlin Buzzwords, where we have utilized GSI APU: <a href="https://blog.muves.io/muves-at-berlin-buzzwords-2022-3150eef01c4">https://blog.muves.io/muves-at-berlin-buzzwords-2022-3150eef01c4</a></p><p>-
  Not All Vector Databases are made equal: <a href="https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696">https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696</a></p><p>Episode
  on YouTube: <a href="https://youtu.be/EerdWRPuqd4">https://youtu.be/EerdWRPuqd4</a></p><p>Podcast
  design: Saurabh Rai: <a href="https://twitter.com/srvbhr">https://twitter.com/srvbhr</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20221221_081200_2671d7352871b25bd4959821449e1a69.jpg
pub_date: Wed, 21 Dec 2022 20:35:43 GMT
title: Yaniv Vaknin - Director of Product, Searchium - Hardware accelerated vector
  search
url: https://rss.com/podcasts/vector-podcast/752549
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 23.56, "text": " Hello,
  vector podcast is here. We again continue to roll in this season 2 of this podcast.",
  "tokens": [50364, 2425, 11, 8062, 7367, 307, 510, 13, 492, 797, 2354, 281, 3373,
  294, 341, 3196, 568, 295, 341, 7367, 13, 51542], "temperature": 0.0, "avg_logprob":
  -0.42507251103719074, "compression_ratio": 1.1111111111111112, "no_speech_prob":
  0.11455044895410538}, {"id": 1, "seek": 2356, "start": 23.56, "end": 31.6, "text":
  " Today I have a very interesting guest, Yanny Vaknin, who is the director of product
  at Searchum.", "tokens": [50364, 2692, 286, 362, 257, 588, 1880, 8341, 11, 398,
  11612, 691, 514, 22955, 11, 567, 307, 264, 5391, 295, 1674, 412, 17180, 449, 13,
  50766], "temperature": 0.0, "avg_logprob": -0.4544465201241629, "compression_ratio":
  1.4766839378238341, "no_speech_prob": 0.44815152883529663}, {"id": 2, "seek": 2356,
  "start": 31.6, "end": 36.8, "text": " If you''ve read my blog post on not all vector
  databases, I made equal.", "tokens": [50766, 759, 291, 600, 1401, 452, 6968, 2183,
  322, 406, 439, 8062, 22380, 11, 286, 1027, 2681, 13, 51026], "temperature": 0.0,
  "avg_logprob": -0.4544465201241629, "compression_ratio": 1.4766839378238341, "no_speech_prob":
  0.44815152883529663}, {"id": 3, "seek": 2356, "start": 36.8, "end": 41.239999999999995,
  "text": " One of the vector databases, all like technologies, stood out.", "tokens":
  [51026, 1485, 295, 264, 8062, 22380, 11, 439, 411, 7943, 11, 9371, 484, 13, 51248],
  "temperature": 0.0, "avg_logprob": -0.4544465201241629, "compression_ratio": 1.4766839378238341,
  "no_speech_prob": 0.44815152883529663}, {"id": 4, "seek": 2356, "start": 41.239999999999995,
  "end": 47.239999999999995, "text": " And it''s a technology made by GSI, technology
  company.", "tokens": [51248, 400, 309, 311, 257, 2899, 1027, 538, 460, 20262, 11,
  2899, 2237, 13, 51548], "temperature": 0.0, "avg_logprob": -0.4544465201241629,
  "compression_ratio": 1.4766839378238341, "no_speech_prob": 0.44815152883529663},
  {"id": 5, "seek": 4724, "start": 47.28, "end": 51.28, "text": " And it''s implementing
  a hardware for vector search.", "tokens": [50366, 400, 309, 311, 18114, 257, 8837,
  337, 8062, 3164, 13, 50566], "temperature": 0.0, "avg_logprob": -0.2543359221073619,
  "compression_ratio": 1.5333333333333334, "no_speech_prob": 0.029213469475507736},
  {"id": 6, "seek": 4724, "start": 51.28, "end": 57.480000000000004, "text": " It''s
  very rare that this thing exists or this approach exists on the market today.",
  "tokens": [50566, 467, 311, 588, 5892, 300, 341, 551, 8198, 420, 341, 3109, 8198,
  322, 264, 2142, 965, 13, 50876], "temperature": 0.0, "avg_logprob": -0.2543359221073619,
  "compression_ratio": 1.5333333333333334, "no_speech_prob": 0.029213469475507736},
  {"id": 7, "seek": 4724, "start": 57.480000000000004, "end": 60.440000000000005,
  "text": " And I''m super excited to talk to Yanny Vaknin.", "tokens": [50876, 400,
  286, 478, 1687, 2919, 281, 751, 281, 398, 11612, 691, 514, 22955, 13, 51024], "temperature":
  0.0, "avg_logprob": -0.2543359221073619, "compression_ratio": 1.5333333333333334,
  "no_speech_prob": 0.029213469475507736}, {"id": 8, "seek": 4724, "start": 60.440000000000005,
  "end": 61.440000000000005, "text": " How are you, Yanny Vaknin?", "tokens": [51024,
  1012, 366, 291, 11, 398, 11612, 691, 514, 22955, 30, 51074], "temperature": 0.0,
  "avg_logprob": -0.2543359221073619, "compression_ratio": 1.5333333333333334, "no_speech_prob":
  0.029213469475507736}, {"id": 9, "seek": 4724, "start": 61.440000000000005, "end":
  62.64, "text": " Hey.", "tokens": [51074, 1911, 13, 51134], "temperature": 0.0,
  "avg_logprob": -0.2543359221073619, "compression_ratio": 1.5333333333333334, "no_speech_prob":
  0.029213469475507736}, {"id": 10, "seek": 4724, "start": 62.64, "end": 65.48, "text":
  " Great. Thanks for having me, maybe, Mietri.", "tokens": [51134, 3769, 13, 2561,
  337, 1419, 385, 11, 1310, 11, 376, 1684, 470, 13, 51276], "temperature": 0.0, "avg_logprob":
  -0.2543359221073619, "compression_ratio": 1.5333333333333334, "no_speech_prob":
  0.029213469475507736}, {"id": 11, "seek": 4724, "start": 65.48, "end": 70.72, "text":
  " Yeah. I''m really glad you joined and found time in your business schedule.",
  "tokens": [51276, 865, 13, 286, 478, 534, 5404, 291, 6869, 293, 1352, 565, 294,
  428, 1606, 7567, 13, 51538], "temperature": 0.0, "avg_logprob": -0.2543359221073619,
  "compression_ratio": 1.5333333333333334, "no_speech_prob": 0.029213469475507736},
  {"id": 12, "seek": 4724, "start": 70.72, "end": 75.68, "text": " So can you first
  explain how searchum and GSI are related?", "tokens": [51538, 407, 393, 291, 700,
  2903, 577, 3164, 449, 293, 460, 20262, 366, 4077, 30, 51786], "temperature": 0.0,
  "avg_logprob": -0.2543359221073619, "compression_ratio": 1.5333333333333334, "no_speech_prob":
  0.029213469475507736}, {"id": 13, "seek": 7568, "start": 75.68, "end": 83.28, "text":
  " And maybe at the same time, if you could traditionally introduce yourself and
  talk about your background and how you got here.", "tokens": [50364, 400, 1310,
  412, 264, 912, 565, 11, 498, 291, 727, 19067, 5366, 1803, 293, 751, 466, 428, 3678,
  293, 577, 291, 658, 510, 13, 50744], "temperature": 0.0, "avg_logprob": -0.24611820318760017,
  "compression_ratio": 1.5849056603773586, "no_speech_prob": 0.006571581587195396},
  {"id": 14, "seek": 7568, "start": 83.28, "end": 87.0, "text": " Yeah. So maybe I
  will start with quick introduction.", "tokens": [50744, 865, 13, 407, 1310, 286,
  486, 722, 365, 1702, 9339, 13, 50930], "temperature": 0.0, "avg_logprob": -0.24611820318760017,
  "compression_ratio": 1.5849056603773586, "no_speech_prob": 0.006571581587195396},
  {"id": 15, "seek": 7568, "start": 87.0, "end": 91.88000000000001, "text": " So I''m
  director of product at Searchum AI.", "tokens": [50930, 407, 286, 478, 5391, 295,
  1674, 412, 17180, 449, 7318, 13, 51174], "temperature": 0.0, "avg_logprob": -0.24611820318760017,
  "compression_ratio": 1.5849056603773586, "no_speech_prob": 0.006571581587195396},
  {"id": 16, "seek": 7568, "start": 91.88000000000001, "end": 104.44000000000001,
  "text": " Searchum AI is a SaaS platform for ML search application, based on purpose
  build AI chip for search applications.", "tokens": [51174, 17180, 449, 7318, 307,
  257, 49733, 3663, 337, 21601, 3164, 3861, 11, 2361, 322, 4334, 1322, 7318, 11409,
  337, 3164, 5821, 13, 51802], "temperature": 0.0, "avg_logprob": -0.24611820318760017,
  "compression_ratio": 1.5849056603773586, "no_speech_prob": 0.006571581587195396},
  {"id": 17, "seek": 10444, "start": 104.44, "end": 118.67999999999999, "text": "
  Prior to this role, I''ve worked at AWS as a machine learning specialist where I''ve
  worked with broad spectrum of top t top tier tech companies.", "tokens": [50364,
  24032, 281, 341, 3090, 11, 286, 600, 2732, 412, 17650, 382, 257, 3479, 2539, 17008,
  689, 286, 600, 2732, 365, 4152, 11143, 295, 1192, 256, 1192, 12362, 7553, 3431,
  13, 51076], "temperature": 0.0, "avg_logprob": -0.23917608003358584, "compression_ratio":
  1.5804878048780489, "no_speech_prob": 0.062350302934646606}, {"id": 18, "seek":
  10444, "start": 118.67999999999999, "end": 121.44, "text": " Trying to help them
  in their machine learning domain.", "tokens": [51076, 20180, 281, 854, 552, 294,
  641, 3479, 2539, 9274, 13, 51214], "temperature": 0.0, "avg_logprob": -0.23917608003358584,
  "compression_ratio": 1.5804878048780489, "no_speech_prob": 0.062350302934646606},
  {"id": 19, "seek": 10444, "start": 121.44, "end": 133.68, "text": " And I was super
  excited from the revolution of the like the fifth revolution, the AI revolution
  with cool stuff of NLP search.", "tokens": [51214, 400, 286, 390, 1687, 2919, 490,
  264, 8894, 295, 264, 411, 264, 9266, 8894, 11, 264, 7318, 8894, 365, 1627, 1507,
  295, 426, 45196, 3164, 13, 51826], "temperature": 0.0, "avg_logprob": -0.23917608003358584,
  "compression_ratio": 1.5804878048780489, "no_speech_prob": 0.062350302934646606},
  {"id": 20, "seek": 13368, "start": 133.68, "end": 137.32, "text": " Unstructed data
  structure data.", "tokens": [50364, 1156, 372, 1757, 292, 1412, 3877, 1412, 13,
  50546], "temperature": 0.0, "avg_logprob": -0.3357957971507105, "compression_ratio":
  1.3680981595092025, "no_speech_prob": 0.025602206587791443}, {"id": 21, "seek":
  13368, "start": 137.32, "end": 146.08, "text": " I''ve worked with various companies
  cyber, fintech e-commerce, etc.", "tokens": [50546, 286, 600, 2732, 365, 3683, 3431,
  13411, 11, 283, 686, 5023, 308, 12, 26926, 11, 5183, 13, 50984], "temperature":
  0.0, "avg_logprob": -0.3357957971507105, "compression_ratio": 1.3680981595092025,
  "no_speech_prob": 0.025602206587791443}, {"id": 22, "seek": 13368, "start": 146.08,
  "end": 157.12, "text": " I was co founder and CEO of deep sea AI, which was the
  first computer vision based system for open water drowning detection.", "tokens":
  [50984, 286, 390, 598, 14917, 293, 9282, 295, 2452, 4158, 7318, 11, 597, 390, 264,
  700, 3820, 5201, 2361, 1185, 337, 1269, 1281, 37198, 17784, 13, 51536], "temperature":
  0.0, "avg_logprob": -0.3357957971507105, "compression_ratio": 1.3680981595092025,
  "no_speech_prob": 0.025602206587791443}, {"id": 23, "seek": 15712, "start": 157.12,
  "end": 161.24, "text": " So we are the SaaS solution of GSI.", "tokens": [50364,
  407, 321, 366, 264, 49733, 3827, 295, 460, 20262, 13, 50570], "temperature": 0.0,
  "avg_logprob": -0.2721675025092231, "compression_ratio": 1.445414847161572, "no_speech_prob":
  0.04016530513763428}, {"id": 24, "seek": 15712, "start": 161.24, "end": 165.44,
  "text": " GSI acquired an Israeli startup a few years ago.", "tokens": [50570, 460,
  20262, 17554, 364, 19974, 18578, 257, 1326, 924, 2057, 13, 50780], "temperature":
  0.0, "avg_logprob": -0.2721675025092231, "compression_ratio": 1.445414847161572,
  "no_speech_prob": 0.04016530513763428}, {"id": 25, "seek": 15712, "start": 165.44,
  "end": 172.52, "text": " And the founder is Dr. Avidan Krib, which is one of the
  smartest guy that I ever met.", "tokens": [50780, 400, 264, 14917, 307, 2491, 13,
  11667, 31675, 591, 2024, 11, 597, 307, 472, 295, 264, 41491, 2146, 300, 286, 1562,
  1131, 13, 51134], "temperature": 0.0, "avg_logprob": -0.2721675025092231, "compression_ratio":
  1.445414847161572, "no_speech_prob": 0.04016530513763428}, {"id": 26, "seek": 15712,
  "start": 172.52, "end": 177.0, "text": " And during this PhD, he invented a new
  concept.", "tokens": [51134, 400, 1830, 341, 14476, 11, 415, 14479, 257, 777, 3410,
  13, 51358], "temperature": 0.0, "avg_logprob": -0.2721675025092231, "compression_ratio":
  1.445414847161572, "no_speech_prob": 0.04016530513763428}, {"id": 27, "seek": 15712,
  "start": 177.0, "end": 186.88, "text": " So traditionally, CPU is communicating
  with the memory and then you have like challenges of bottleneck, IO, etc.", "tokens":
  [51358, 407, 19067, 11, 13199, 307, 17559, 365, 264, 4675, 293, 550, 291, 362, 411,
  4759, 295, 44641, 547, 11, 39839, 11, 5183, 13, 51852], "temperature": 0.0, "avg_logprob":
  -0.2721675025092231, "compression_ratio": 1.445414847161572, "no_speech_prob": 0.04016530513763428},
  {"id": 28, "seek": 18688, "start": 186.88, "end": 193.6, "text": " But when you
  build the new concept, you build a memory that is the processor.", "tokens": [50364,
  583, 562, 291, 1322, 264, 777, 3410, 11, 291, 1322, 257, 4675, 300, 307, 264, 15321,
  13, 50700], "temperature": 0.0, "avg_logprob": -0.19830200407240126, "compression_ratio":
  1.7880434782608696, "no_speech_prob": 0.004914760589599609}, {"id": 29, "seek":
  18688, "start": 193.6, "end": 197.76, "text": " So all of the computation is happening
  inside the memory.", "tokens": [50700, 407, 439, 295, 264, 24903, 307, 2737, 1854,
  264, 4675, 13, 50908], "temperature": 0.0, "avg_logprob": -0.19830200407240126,
  "compression_ratio": 1.7880434782608696, "no_speech_prob": 0.004914760589599609},
  {"id": 30, "seek": 18688, "start": 197.76, "end": 213.88, "text": " You can guess
  that when you''re running heavy or intensive intensive memory applications, if all
  of the processing is happening inside the memory, you can get a single digit millisecond
  latency.", "tokens": [50908, 509, 393, 2041, 300, 562, 291, 434, 2614, 4676, 420,
  18957, 18957, 4675, 5821, 11, 498, 439, 295, 264, 9007, 307, 2737, 1854, 264, 4675,
  11, 291, 393, 483, 257, 2167, 14293, 27940, 18882, 27043, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.19830200407240126, "compression_ratio": 1.7880434782608696,
  "no_speech_prob": 0.004914760589599609}, {"id": 31, "seek": 21388, "start": 213.88,
  "end": 222.72, "text": " Yeah, so GSI acquired the Israeli startup and we are based
  in Israel.", "tokens": [50364, 865, 11, 370, 460, 20262, 17554, 264, 19974, 18578,
  293, 321, 366, 2361, 294, 5674, 13, 50806], "temperature": 0.0, "avg_logprob": -0.24529946018272722,
  "compression_ratio": 1.4240837696335078, "no_speech_prob": 0.21629437804222107},
  {"id": 32, "seek": 21388, "start": 222.72, "end": 228.6, "text": " We have an R&D
  team of approximately 40 to 50 people.", "tokens": [50806, 492, 362, 364, 497, 5,
  35, 1469, 295, 10447, 3356, 281, 2625, 561, 13, 51100], "temperature": 0.0, "avg_logprob":
  -0.24529946018272722, "compression_ratio": 1.4240837696335078, "no_speech_prob":
  0.21629437804222107}, {"id": 33, "seek": 21388, "start": 228.6, "end": 235.0, "text":
  " In order to scale it, we started searching AI because it''s super hard to scale
  hardware.", "tokens": [51100, 682, 1668, 281, 4373, 309, 11, 321, 1409, 10808, 7318,
  570, 309, 311, 1687, 1152, 281, 4373, 8837, 13, 51420], "temperature": 0.0, "avg_logprob":
  -0.24529946018272722, "compression_ratio": 1.4240837696335078, "no_speech_prob":
  0.21629437804222107}, {"id": 34, "seek": 21388, "start": 235.0, "end": 240.8, "text":
  " So today we are offering this unique hardware on the cloud.", "tokens": [51420,
  407, 965, 321, 366, 8745, 341, 3845, 8837, 322, 264, 4588, 13, 51710], "temperature":
  0.0, "avg_logprob": -0.24529946018272722, "compression_ratio": 1.4240837696335078,
  "no_speech_prob": 0.21629437804222107}, {"id": 35, "seek": 24080, "start": 240.8,
  "end": 251.56, "text": " It can be AWS, GCP or any other cloud and customers can
  consume it as a SaaS platform.", "tokens": [50364, 467, 393, 312, 17650, 11, 460,
  20049, 420, 604, 661, 4588, 293, 4581, 393, 14732, 309, 382, 257, 49733, 3663, 13,
  50902], "temperature": 0.0, "avg_logprob": -0.22140585658061934, "compression_ratio":
  1.419811320754717, "no_speech_prob": 0.04357348009943962}, {"id": 36, "seek": 24080,
  "start": 251.56, "end": 253.16000000000003, "text": " Yeah, makes sense.", "tokens":
  [50902, 865, 11, 1669, 2020, 13, 50982], "temperature": 0.0, "avg_logprob": -0.22140585658061934,
  "compression_ratio": 1.419811320754717, "no_speech_prob": 0.04357348009943962},
  {"id": 37, "seek": 24080, "start": 253.16000000000003, "end": 261.16, "text": "
  But there is still an option to if I want to have a completely on-premise sort of
  like setup, right?", "tokens": [50982, 583, 456, 307, 920, 364, 3614, 281, 498,
  286, 528, 281, 362, 257, 2584, 322, 12, 29403, 908, 1333, 295, 411, 8657, 11, 558,
  30, 51382], "temperature": 0.0, "avg_logprob": -0.22140585658061934, "compression_ratio":
  1.419811320754717, "no_speech_prob": 0.04357348009943962}, {"id": 38, "seek": 24080,
  "start": 261.16, "end": 268.0, "text": " In principle, I could have bought like
  the APU cards, APU being a associative processing unit.", "tokens": [51382, 682,
  8665, 11, 286, 727, 362, 4243, 411, 264, 5372, 52, 5632, 11, 5372, 52, 885, 257,
  4180, 1166, 9007, 4985, 13, 51724], "temperature": 0.0, "avg_logprob": -0.22140585658061934,
  "compression_ratio": 1.419811320754717, "no_speech_prob": 0.04357348009943962},
  {"id": 39, "seek": 26800, "start": 268.0, "end": 272.56, "text": " Cards and like
  install them similar to what I would do with GPU. Is that right?", "tokens": [50364,
  383, 2287, 293, 411, 3625, 552, 2531, 281, 437, 286, 576, 360, 365, 18407, 13, 1119,
  300, 558, 30, 50592], "temperature": 0.0, "avg_logprob": -0.20464169081821237, "compression_ratio":
  1.6140350877192982, "no_speech_prob": 0.052067022770643234}, {"id": 40, "seek":
  26800, "start": 272.56, "end": 273.64, "text": " Yeah, yeah, totally.", "tokens":
  [50592, 865, 11, 1338, 11, 3879, 13, 50646], "temperature": 0.0, "avg_logprob":
  -0.20464169081821237, "compression_ratio": 1.6140350877192982, "no_speech_prob":
  0.052067022770643234}, {"id": 41, "seek": 26800, "start": 273.64, "end": 276.64,
  "text": " Yeah, so there are two types of implementation.", "tokens": [50646, 865,
  11, 370, 456, 366, 732, 3467, 295, 11420, 13, 50796], "temperature": 0.0, "avg_logprob":
  -0.20464169081821237, "compression_ratio": 1.6140350877192982, "no_speech_prob":
  0.052067022770643234}, {"id": 42, "seek": 26800, "start": 276.64, "end": 282.24,
  "text": " The first one is on-prem and the second is via the cloud.", "tokens":
  [50796, 440, 700, 472, 307, 322, 12, 29403, 293, 264, 1150, 307, 5766, 264, 4588,
  13, 51076], "temperature": 0.0, "avg_logprob": -0.20464169081821237, "compression_ratio":
  1.6140350877192982, "no_speech_prob": 0.052067022770643234}, {"id": 43, "seek":
  26800, "start": 282.24, "end": 297.4, "text": " There are various configurations
  and in terms of if for instance, customers that would like to consume it as an on-prem
  solution, there are various capabilities.", "tokens": [51076, 821, 366, 3683, 31493,
  293, 294, 2115, 295, 498, 337, 5197, 11, 4581, 300, 576, 411, 281, 14732, 309, 382,
  364, 322, 12, 29403, 3827, 11, 456, 366, 3683, 10862, 13, 51834], "temperature":
  0.0, "avg_logprob": -0.20464169081821237, "compression_ratio": 1.6140350877192982,
  "no_speech_prob": 0.052067022770643234}, {"id": 44, "seek": 29740, "start": 297.4,
  "end": 307.76, "text": " And one of the major things about this hardware accelerator
  is the power consumption.", "tokens": [50364, 400, 472, 295, 264, 2563, 721, 466,
  341, 8837, 39889, 307, 264, 1347, 12126, 13, 50882], "temperature": 0.0, "avg_logprob":
  -0.13492685045514788, "compression_ratio": 1.6388888888888888, "no_speech_prob":
  0.006789816077798605}, {"id": 45, "seek": 29740, "start": 307.76, "end": 316.03999999999996,
  "text": " So comparing it to CPU or GPU, it is like can be 5% or 10% of the power
  consumption.", "tokens": [50882, 407, 15763, 309, 281, 13199, 420, 18407, 11, 309,
  307, 411, 393, 312, 1025, 4, 420, 1266, 4, 295, 264, 1347, 12126, 13, 51296], "temperature":
  0.0, "avg_logprob": -0.13492685045514788, "compression_ratio": 1.6388888888888888,
  "no_speech_prob": 0.006789816077798605}, {"id": 46, "seek": 29740, "start": 316.03999999999996,
  "end": 327.03999999999996, "text": " So companies that are running heavy workloads
  of GPU and CPU, the total cost of ownership for them is the power consumption.",
  "tokens": [51296, 407, 3431, 300, 366, 2614, 4676, 32452, 295, 18407, 293, 13199,
  11, 264, 3217, 2063, 295, 15279, 337, 552, 307, 264, 1347, 12126, 13, 51846], "temperature":
  0.0, "avg_logprob": -0.13492685045514788, "compression_ratio": 1.6388888888888888,
  "no_speech_prob": 0.006789816077798605}, {"id": 47, "seek": 32704, "start": 327.04,
  "end": 328.44, "text": " And other factors.", "tokens": [50364, 400, 661, 6771,
  13, 50434], "temperature": 0.0, "avg_logprob": -0.1871465618690748, "compression_ratio":
  1.6371681415929205, "no_speech_prob": 0.018471654504537582}, {"id": 48, "seek":
  32704, "start": 328.44, "end": 339.96000000000004, "text": " So on-prem customers
  can reduce the infrastructure cost in terms of the total cost of ownership, power
  consumption, etc.", "tokens": [50434, 407, 322, 12, 29403, 4581, 393, 5407, 264,
  6896, 2063, 294, 2115, 295, 264, 3217, 2063, 295, 15279, 11, 1347, 12126, 11, 5183,
  13, 51010], "temperature": 0.0, "avg_logprob": -0.1871465618690748, "compression_ratio":
  1.6371681415929205, "no_speech_prob": 0.018471654504537582}, {"id": 49, "seek":
  32704, "start": 339.96000000000004, "end": 341.0, "text": " Yeah, this is really
  cool.", "tokens": [51010, 865, 11, 341, 307, 534, 1627, 13, 51062], "temperature":
  0.0, "avg_logprob": -0.1871465618690748, "compression_ratio": 1.6371681415929205,
  "no_speech_prob": 0.018471654504537582}, {"id": 50, "seek": 32704, "start": 341.0,
  "end": 348.20000000000005, "text": " And I think it''s not very frequently that
  we mentioned power consumption as one of the dimensions on this podcast.", "tokens":
  [51062, 400, 286, 519, 309, 311, 406, 588, 10374, 300, 321, 2835, 1347, 12126, 382,
  472, 295, 264, 12819, 322, 341, 7367, 13, 51422], "temperature": 0.0, "avg_logprob":
  -0.1871465618690748, "compression_ratio": 1.6371681415929205, "no_speech_prob":
  0.018471654504537582}, {"id": 51, "seek": 32704, "start": 348.20000000000005, "end":
  354.36, "text": " I mean, I think it''s crucial of course for the planet and also
  for the electricity bill.", "tokens": [51422, 286, 914, 11, 286, 519, 309, 311,
  11462, 295, 1164, 337, 264, 5054, 293, 611, 337, 264, 10356, 2961, 13, 51730], "temperature":
  0.0, "avg_logprob": -0.1871465618690748, "compression_ratio": 1.6371681415929205,
  "no_speech_prob": 0.018471654504537582}, {"id": 52, "seek": 35436, "start": 354.36,
  "end": 360.76, "text": " And how the electricity costs skyrocketing, you know, and
  I think it''s quite important.", "tokens": [50364, 400, 577, 264, 10356, 5497, 5443,
  37463, 278, 11, 291, 458, 11, 293, 286, 519, 309, 311, 1596, 1021, 13, 50684], "temperature":
  0.0, "avg_logprob": -0.30089751533840015, "compression_ratio": 1.446927374301676,
  "no_speech_prob": 0.10110354423522949}, {"id": 53, "seek": 35436, "start": 360.76,
  "end": 363.36, "text": " Yeah, sorry.", "tokens": [50684, 865, 11, 2597, 13, 50814],
  "temperature": 0.0, "avg_logprob": -0.30089751533840015, "compression_ratio": 1.446927374301676,
  "no_speech_prob": 0.10110354423522949}, {"id": 54, "seek": 35436, "start": 363.36,
  "end": 378.24, "text": " No, I was just kind of alluding to this fact that it''s
  very like you should not skip it in kind of assessing a system or like a vector
  search solution, right.", "tokens": [50814, 883, 11, 286, 390, 445, 733, 295, 439,
  33703, 281, 341, 1186, 300, 309, 311, 588, 411, 291, 820, 406, 10023, 309, 294,
  733, 295, 34348, 257, 1185, 420, 411, 257, 8062, 3164, 3827, 11, 558, 13, 51558],
  "temperature": 0.0, "avg_logprob": -0.30089751533840015, "compression_ratio": 1.446927374301676,
  "no_speech_prob": 0.10110354423522949}, {"id": 55, "seek": 37824, "start": 378.24,
  "end": 388.88, "text": " Not only focusing entirely on the offering itself, like
  you should still worry about how it will scale in different dimensions.", "tokens":
  [50364, 1726, 787, 8416, 7696, 322, 264, 8745, 2564, 11, 411, 291, 820, 920, 3292,
  466, 577, 309, 486, 4373, 294, 819, 12819, 13, 50896], "temperature": 0.0, "avg_logprob":
  -0.24110528628031414, "compression_ratio": 1.4516129032258065, "no_speech_prob":
  0.5214963555335999}, {"id": 56, "seek": 37824, "start": 388.88, "end": 393.92, "text":
  " I''m glad you guys also worry about the power consumption part.", "tokens": [50896,
  286, 478, 5404, 291, 1074, 611, 3292, 466, 264, 1347, 12126, 644, 13, 51148], "temperature":
  0.0, "avg_logprob": -0.24110528628031414, "compression_ratio": 1.4516129032258065,
  "no_speech_prob": 0.5214963555335999}, {"id": 57, "seek": 37824, "start": 393.92,
  "end": 400.8, "text": " Yeah, low carbon footprint is a major issue right now and
  especially in Europe.", "tokens": [51148, 865, 11, 2295, 5954, 24222, 307, 257,
  2563, 2734, 558, 586, 293, 2318, 294, 3315, 13, 51492], "temperature": 0.0, "avg_logprob":
  -0.24110528628031414, "compression_ratio": 1.4516129032258065, "no_speech_prob":
  0.5214963555335999}, {"id": 58, "seek": 40080, "start": 401.76, "end": 412.88, "text":
  " Usually developers when they are launching the AWS instances, so they choose by
  parameters of virtual CPU, RAM, etc.", "tokens": [50412, 11419, 8849, 562, 436,
  366, 18354, 264, 17650, 14519, 11, 370, 436, 2826, 538, 9834, 295, 6374, 13199,
  11, 14561, 11, 5183, 13, 50968], "temperature": 0.0, "avg_logprob": -0.23259834096401552,
  "compression_ratio": 1.6018957345971565, "no_speech_prob": 0.06344892084598541},
  {"id": 59, "seek": 40080, "start": 412.88, "end": 430.72, "text": " And they are
  not aware of the carbon footprint, but when you are running it on-prem, this is
  a major parameters and this is a key parameter to, you know, taking a decision what
  is the right platform or right is the right.", "tokens": [50968, 400, 436, 366,
  406, 3650, 295, 264, 5954, 24222, 11, 457, 562, 291, 366, 2614, 309, 322, 12, 29403,
  11, 341, 307, 257, 2563, 9834, 293, 341, 307, 257, 2141, 13075, 281, 11, 291, 458,
  11, 1940, 257, 3537, 437, 307, 264, 558, 3663, 420, 558, 307, 264, 558, 13, 51860],
  "temperature": 0.0, "avg_logprob": -0.23259834096401552, "compression_ratio": 1.6018957345971565,
  "no_speech_prob": 0.06344892084598541}, {"id": 60, "seek": 43072, "start": 430.72,
  "end": 433.72, "text": " Hardware for you.", "tokens": [50364, 11817, 3039, 337,
  291, 13, 50514], "temperature": 0.0, "avg_logprob": -0.25560032028749763, "compression_ratio":
  1.6411483253588517, "no_speech_prob": 0.020188316702842712}, {"id": 61, "seek":
  43072, "start": 433.72, "end": 447.72, "text": " So totally agree, but, you know,
  I believe in an agree with you, we should take it into consideration and assume
  for cloud providers to integrate cloud providers like AWS, GCP, Azure.", "tokens":
  [50514, 407, 3879, 3986, 11, 457, 11, 291, 458, 11, 286, 1697, 294, 364, 3986, 365,
  291, 11, 321, 820, 747, 309, 666, 12381, 293, 6552, 337, 4588, 11330, 281, 13365,
  4588, 11330, 411, 17650, 11, 460, 20049, 11, 11969, 13, 51214], "temperature": 0.0,
  "avg_logprob": -0.25560032028749763, "compression_ratio": 1.6411483253588517, "no_speech_prob":
  0.020188316702842712}, {"id": 62, "seek": 43072, "start": 447.72, "end": 457.72,
  "text": " This can be, you know, critical for them and we are in conversation with
  some of the company of some of the cloud providers that I mentioned.", "tokens":
  [51214, 639, 393, 312, 11, 291, 458, 11, 4924, 337, 552, 293, 321, 366, 294, 3761,
  365, 512, 295, 264, 2237, 295, 512, 295, 264, 4588, 11330, 300, 286, 2835, 13, 51714],
  "temperature": 0.0, "avg_logprob": -0.25560032028749763, "compression_ratio": 1.6411483253588517,
  "no_speech_prob": 0.020188316702842712}, {"id": 63, "seek": 45772, "start": 457.72,
  "end": 459.72, "text": " Yeah, this sounds great.", "tokens": [50364, 865, 11, 341,
  3263, 869, 13, 50464], "temperature": 0.0, "avg_logprob": -0.19881485034893084,
  "compression_ratio": 1.4977168949771689, "no_speech_prob": 0.008465241640806198},
  {"id": 64, "seek": 45772, "start": 459.72, "end": 473.72, "text": " If we move a
  little bit closer to the algorithm side, so this is a kind of like dedicated hardware
  and as far as I understood also based on our brain buzz, buzzwords presentation.",
  "tokens": [50464, 759, 321, 1286, 257, 707, 857, 4966, 281, 264, 9284, 1252, 11,
  370, 341, 307, 257, 733, 295, 411, 8374, 8837, 293, 382, 1400, 382, 286, 7320, 611,
  2361, 322, 527, 3567, 13036, 11, 13036, 13832, 5860, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.19881485034893084, "compression_ratio": 1.4977168949771689,
  "no_speech_prob": 0.008465241640806198}, {"id": 65, "seek": 45772, "start": 473.72,
  "end": 478.72, "text": " This hardware can support not only vector search, but some
  other scenarios, right.", "tokens": [51164, 639, 8837, 393, 1406, 406, 787, 8062,
  3164, 11, 457, 512, 661, 15077, 11, 558, 13, 51414], "temperature": 0.0, "avg_logprob":
  -0.19881485034893084, "compression_ratio": 1.4977168949771689, "no_speech_prob":
  0.008465241640806198}, {"id": 66, "seek": 45772, "start": 478.72, "end": 482.72,
  "text": " Like for image processing related tasks.", "tokens": [51414, 1743, 337,
  3256, 9007, 4077, 9608, 13, 51614], "temperature": 0.0, "avg_logprob": -0.19881485034893084,
  "compression_ratio": 1.4977168949771689, "no_speech_prob": 0.008465241640806198},
  {"id": 67, "seek": 48272, "start": 482.72, "end": 494.72, "text": " So is there
  any kind of like constraint on what type of vector search algorithm you can implement
  or is it doesn''t it doesn''t have any constraint.", "tokens": [50364, 407, 307,
  456, 604, 733, 295, 411, 25534, 322, 437, 2010, 295, 8062, 3164, 9284, 291, 393,
  4445, 420, 307, 309, 1177, 380, 309, 1177, 380, 362, 604, 25534, 13, 50964], "temperature":
  0.0, "avg_logprob": -0.16377704899485518, "compression_ratio": 1.6559633027522935,
  "no_speech_prob": 0.036446474492549896}, {"id": 68, "seek": 48272, "start": 494.72,
  "end": 495.72, "text": " Yeah, yeah.", "tokens": [50964, 865, 11, 1338, 13, 51014],
  "temperature": 0.0, "avg_logprob": -0.16377704899485518, "compression_ratio": 1.6559633027522935,
  "no_speech_prob": 0.036446474492549896}, {"id": 69, "seek": 48272, "start": 495.72,
  "end": 508.72, "text": " So I think that the biggest challenge today is when you
  are developing hardly can develop like a state of the art hardware, but I think
  the major challenge is how do you integrate it with the community.", "tokens": [51014,
  407, 286, 519, 300, 264, 3880, 3430, 965, 307, 562, 291, 366, 6416, 13572, 393,
  1499, 411, 257, 1785, 295, 264, 1523, 8837, 11, 457, 286, 519, 264, 2563, 3430,
  307, 577, 360, 291, 13365, 309, 365, 264, 1768, 13, 51664], "temperature": 0.0,
  "avg_logprob": -0.16377704899485518, "compression_ratio": 1.6559633027522935, "no_speech_prob":
  0.036446474492549896}, {"id": 70, "seek": 50872, "start": 508.72, "end": 511.72,
  "text": " And video I''ve done it.", "tokens": [50364, 400, 960, 286, 600, 1096,
  309, 13, 50514], "temperature": 0.0, "avg_logprob": -0.2465040169510187, "compression_ratio":
  1.3426573426573427, "no_speech_prob": 0.042637743055820465}, {"id": 71, "seek":
  50872, "start": 511.72, "end": 516.72, "text": " Very good with the CUDA and it
  should be part of the ecosystem.", "tokens": [50514, 4372, 665, 365, 264, 29777,
  7509, 293, 309, 820, 312, 644, 295, 264, 11311, 13, 50764], "temperature": 0.0,
  "avg_logprob": -0.2465040169510187, "compression_ratio": 1.3426573426573427, "no_speech_prob":
  0.042637743055820465}, {"id": 72, "seek": 50872, "start": 516.72, "end": 523.72,
  "text": " So in terms of applications here, we have like another application for
  image processing, it is based on.", "tokens": [50764, 407, 294, 2115, 295, 5821,
  510, 11, 321, 362, 411, 1071, 3861, 337, 3256, 9007, 11, 309, 307, 2361, 322, 13,
  51114], "temperature": 0.0, "avg_logprob": -0.2465040169510187, "compression_ratio":
  1.3426573426573427, "no_speech_prob": 0.042637743055820465}, {"id": 73, "seek":
  52372, "start": 523.72, "end": 537.72, "text": " So, say it''s set light images
  and radar images and we can process it like faster in a few orders of magnitude
  comparing to Jeep and video GPU.", "tokens": [50364, 407, 11, 584, 309, 311, 992,
  1442, 5267, 293, 16544, 5267, 293, 321, 393, 1399, 309, 411, 4663, 294, 257, 1326,
  9470, 295, 15668, 15763, 281, 31748, 293, 960, 18407, 13, 51064], "temperature":
  0.0, "avg_logprob": -0.4312035151890346, "compression_ratio": 1.2456140350877194,
  "no_speech_prob": 0.2566491961479187}, {"id": 74, "seek": 53772, "start": 537.72,
  "end": 547.72, "text": " So, we have in the past we had a few other applications
  for a genome and the molecules and today we are.", "tokens": [50364, 407, 11, 321,
  362, 294, 264, 1791, 321, 632, 257, 1326, 661, 5821, 337, 257, 1049, 423, 293, 264,
  13093, 293, 965, 321, 366, 13, 50864], "temperature": 0.0, "avg_logprob": -0.2518039927763097,
  "compression_ratio": 1.6698564593301435, "no_speech_prob": 0.6177324056625366},
  {"id": 75, "seek": 53772, "start": 547.72, "end": 558.72, "text": " We would like
  to you know to focus on on the biggest challenges like I believe that you know searches
  and you know we can elaborate about it later on.", "tokens": [50864, 492, 576, 411,
  281, 291, 458, 281, 1879, 322, 322, 264, 3880, 4759, 411, 286, 1697, 300, 291, 458,
  26701, 293, 291, 458, 321, 393, 20945, 466, 309, 1780, 322, 13, 51414], "temperature":
  0.0, "avg_logprob": -0.2518039927763097, "compression_ratio": 1.6698564593301435,
  "no_speech_prob": 0.6177324056625366}, {"id": 76, "seek": 53772, "start": 558.72,
  "end": 566.72, "text": " Search is still broken and this is a huge market and so
  our focus right now is on the search.", "tokens": [51414, 17180, 307, 920, 5463,
  293, 341, 307, 257, 2603, 2142, 293, 370, 527, 1879, 558, 586, 307, 322, 264, 3164,
  13, 51814], "temperature": 0.0, "avg_logprob": -0.2518039927763097, "compression_ratio":
  1.6698564593301435, "no_speech_prob": 0.6177324056625366}, {"id": 77, "seek": 56672,
  "start": 566.72, "end": 578.72, "text": " And we actually have to spend it to other
  solutions as well like image processing and we already have a solution and a customer
  for this solution.", "tokens": [50364, 400, 321, 767, 362, 281, 3496, 309, 281,
  661, 6547, 382, 731, 411, 3256, 9007, 293, 321, 1217, 362, 257, 3827, 293, 257,
  5474, 337, 341, 3827, 13, 50964], "temperature": 0.0, "avg_logprob": -0.2831337792532785,
  "compression_ratio": 1.5467625899280575, "no_speech_prob": 0.017435187473893166},
  {"id": 78, "seek": 56672, "start": 578.72, "end": 585.72, "text": " And then one
  of our efforts is to build an ecosystem around this so.", "tokens": [50964, 400,
  550, 472, 295, 527, 6484, 307, 281, 1322, 364, 11311, 926, 341, 370, 13, 51314],
  "temperature": 0.0, "avg_logprob": -0.2831337792532785, "compression_ratio": 1.5467625899280575,
  "no_speech_prob": 0.017435187473893166}, {"id": 79, "seek": 58572, "start": 585.72,
  "end": 597.72, "text": " Hopefully soon we will launch our Python compiler so developers
  can write their code on Python and then you know run it.", "tokens": [50364, 10429,
  2321, 321, 486, 4025, 527, 15329, 31958, 370, 8849, 393, 2464, 641, 3089, 322, 15329,
  293, 550, 291, 458, 1190, 309, 13, 50964], "temperature": 0.0, "avg_logprob": -0.2535075407761794,
  "compression_ratio": 1.4210526315789473, "no_speech_prob": 0.20332691073417664},
  {"id": 80, "seek": 58572, "start": 597.72, "end": 605.72, "text": " Simulnglessly
  on on our APU without you know trying to learn a new framework or a new language.",
  "tokens": [50964, 3998, 425, 872, 12048, 322, 322, 527, 5372, 52, 1553, 291, 458,
  1382, 281, 1466, 257, 777, 8388, 420, 257, 777, 2856, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.2535075407761794, "compression_ratio": 1.4210526315789473,
  "no_speech_prob": 0.20332691073417664}, {"id": 81, "seek": 60572, "start": 605.72,
  "end": 622.72, "text": " So, this is another direction that we are working we are
  trying I think one of the biggest challenges today is you know to simplifying the
  technological stack for developers so they are working with the common frameworks
  or languages they don''t want to learn it.", "tokens": [50364, 407, 11, 341, 307,
  1071, 3513, 300, 321, 366, 1364, 321, 366, 1382, 286, 519, 472, 295, 264, 3880,
  4759, 965, 307, 291, 458, 281, 6883, 5489, 264, 18439, 8630, 337, 8849, 370, 436,
  366, 1364, 365, 264, 2689, 29834, 420, 8650, 436, 500, 380, 528, 281, 1466, 309,
  13, 51214], "temperature": 0.0, "avg_logprob": -0.15087122387356228, "compression_ratio":
  1.5232558139534884, "no_speech_prob": 0.1232721135020256}, {"id": 82, "seek": 62272,
  "start": 622.72, "end": 626.72, "text": " So, they they they would like you know
  to stay with the.", "tokens": [50364, 407, 11, 436, 436, 436, 576, 411, 291, 458,
  281, 1754, 365, 264, 13, 50564], "temperature": 0.0, "avg_logprob": -0.2130439905019907,
  "compression_ratio": 1.6488095238095237, "no_speech_prob": 0.2192198485136032},
  {"id": 83, "seek": 62272, "start": 626.72, "end": 633.72, "text": " With the languages
  that are familiar and you know the learning curve is not always.", "tokens": [50564,
  2022, 264, 8650, 300, 366, 4963, 293, 291, 458, 264, 2539, 7605, 307, 406, 1009,
  13, 50914], "temperature": 0.0, "avg_logprob": -0.2130439905019907, "compression_ratio":
  1.6488095238095237, "no_speech_prob": 0.2192198485136032}, {"id": 84, "seek": 62272,
  "start": 633.72, "end": 643.72, "text": " They don''t always have time for you know
  to learn a new framework so we are trying to simplify the integration with their
  current stack.", "tokens": [50914, 814, 500, 380, 1009, 362, 565, 337, 291, 458,
  281, 1466, 257, 777, 8388, 370, 321, 366, 1382, 281, 20460, 264, 10980, 365, 641,
  2190, 8630, 13, 51414], "temperature": 0.0, "avg_logprob": -0.2130439905019907,
  "compression_ratio": 1.6488095238095237, "no_speech_prob": 0.2192198485136032},
  {"id": 85, "seek": 64372, "start": 643.72, "end": 654.72, "text": " One of our solution
  is is a plugin on top of elastic and open search and which they are offering a vector
  search today but and we can talk about it but.", "tokens": [50364, 1485, 295, 527,
  3827, 307, 307, 257, 23407, 322, 1192, 295, 17115, 293, 1269, 3164, 293, 597, 436,
  366, 8745, 257, 8062, 3164, 965, 457, 293, 321, 393, 751, 466, 309, 457, 13, 50914],
  "temperature": 0.0, "avg_logprob": -0.18903590221794284, "compression_ratio": 1.4803149606299213,
  "no_speech_prob": 0.04933660104870796}, {"id": 86, "seek": 64372, "start": 654.72,
  "end": 659.72, "text": " So we have a plugin on top of this.", "tokens": [50914,
  407, 321, 362, 257, 23407, 322, 1192, 295, 341, 13, 51164], "temperature": 0.0,
  "avg_logprob": -0.18903590221794284, "compression_ratio": 1.4803149606299213, "no_speech_prob":
  0.04933660104870796}, {"id": 87, "seek": 65972, "start": 659.72, "end": 670.72,
  "text": " Search applications because some of some of the customers would like you
  know to stay with their curing the last or open search so we built a plugin on top
  of it and we are.", "tokens": [50364, 17180, 5821, 570, 512, 295, 512, 295, 264,
  4581, 576, 411, 291, 458, 281, 1754, 365, 641, 1262, 278, 264, 1036, 420, 1269,
  3164, 370, 321, 3094, 257, 23407, 322, 1192, 295, 309, 293, 321, 366, 13, 50914],
  "temperature": 0.0, "avg_logprob": -0.18826780821147718, "compression_ratio": 1.5304878048780488,
  "no_speech_prob": 0.050167303532361984}, {"id": 88, "seek": 65972, "start": 670.72,
  "end": 677.72, "text": " We are talking with search engines and vector database
  in order to implement.", "tokens": [50914, 492, 366, 1417, 365, 3164, 12982, 293,
  8062, 8149, 294, 1668, 281, 4445, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.18826780821147718, "compression_ratio": 1.5304878048780488, "no_speech_prob":
  0.050167303532361984}, {"id": 89, "seek": 67772, "start": 677.72, "end": 693.72,
  "text": " Our solution with their solution and I think in terms of like the the
  landscape so we are we are not perceived the vector search engines and vector database
  as competitors.", "tokens": [50364, 2621, 3827, 365, 641, 3827, 293, 286, 519, 294,
  2115, 295, 411, 264, 264, 9661, 370, 321, 366, 321, 366, 406, 19049, 264, 8062,
  3164, 12982, 293, 8062, 8149, 382, 18333, 13, 51164], "temperature": 0.0, "avg_logprob":
  -0.18520394961039224, "compression_ratio": 1.4333333333333333, "no_speech_prob":
  0.27227693796157837}, {"id": 90, "seek": 69372, "start": 693.72, "end": 706.72,
  "text": " My perception is that they are potential they are partners and better
  together and you know to give a greater value for their customers reducing the infrastructure
  cost and give.", "tokens": [50364, 1222, 12860, 307, 300, 436, 366, 3995, 436, 366,
  4462, 293, 1101, 1214, 293, 291, 458, 281, 976, 257, 5044, 2158, 337, 641, 4581,
  12245, 264, 6896, 2063, 293, 976, 13, 51014], "temperature": 0.0, "avg_logprob":
  -0.1768174171447754, "compression_ratio": 1.424, "no_speech_prob": 0.0941043272614479},
  {"id": 91, "seek": 70672, "start": 706.72, "end": 720.72, "text": " So the lower
  latency with the same without sacrificing accuracy so yeah we are you know trying
  to be part of the ecosystem and you know to help them and.", "tokens": [50364, 407,
  264, 3126, 27043, 365, 264, 912, 1553, 42294, 14170, 370, 1338, 321, 366, 291, 458,
  1382, 281, 312, 644, 295, 264, 11311, 293, 291, 458, 281, 854, 552, 293, 13, 51064],
  "temperature": 0.4, "avg_logprob": -0.2978116726053172, "compression_ratio": 1.6449704142011834,
  "no_speech_prob": 0.11550034582614899}, {"id": 92, "seek": 70672, "start": 720.72,
  "end": 728.72, "text": " To help customer scale there and improve their scale their
  search applications yeah yeah this is interesting you touched on.", "tokens": [51064,
  1407, 854, 5474, 4373, 456, 293, 3470, 641, 4373, 641, 3164, 5821, 1338, 1338, 341,
  307, 1880, 291, 9828, 322, 13, 51464], "temperature": 0.4, "avg_logprob": -0.2978116726053172,
  "compression_ratio": 1.6449704142011834, "no_speech_prob": 0.11550034582614899},
  {"id": 93, "seek": 72872, "start": 728.72, "end": 747.72, "text": " You know being
  like a competitor to vector database I think it''s interesting topic in general
  because on one hand if you take all vector database players they kind of look at
  each other as competitors probably but at the same time as all of you players are
  sharing the.", "tokens": [50364, 509, 458, 885, 411, 257, 27266, 281, 8062, 8149,
  286, 519, 309, 311, 1880, 4829, 294, 2674, 570, 322, 472, 1011, 498, 291, 747, 439,
  8062, 8149, 4150, 436, 733, 295, 574, 412, 1184, 661, 382, 18333, 1391, 457, 412,
  264, 912, 565, 382, 439, 295, 291, 4150, 366, 5414, 264, 13, 51314], "temperature":
  0.0, "avg_logprob": -0.11730776514325823, "compression_ratio": 1.5823529411764705,
  "no_speech_prob": 0.3203605115413666}, {"id": 94, "seek": 74772, "start": 747.72,
  "end": 774.72, "text": " You know the approach the documentation the how you think
  about yourself I think it also helps cumulatively to the whole market but I wasn''t
  also wanted to drill in a bit into this elastic search and open search plugin so
  essentially like what elastic search team has been doing recently and I think they
  released now some updates in version 8.5 where you can you can do things like hybrid
  search right but this is all based on.", "tokens": [50364, 509, 458, 264, 3109,
  264, 14333, 264, 577, 291, 519, 466, 1803, 286, 519, 309, 611, 3665, 12713, 425,
  19020, 281, 264, 1379, 2142, 457, 286, 2067, 380, 611, 1415, 281, 11392, 294, 257,
  857, 666, 341, 17115, 3164, 293, 1269, 3164, 23407, 370, 4476, 411, 437, 17115,
  3164, 1469, 575, 668, 884, 3938, 293, 286, 519, 436, 4736, 586, 512, 9205, 294,
  3037, 1649, 13, 20, 689, 291, 393, 291, 393, 360, 721, 411, 13051, 3164, 558, 457,
  341, 307, 439, 2361, 322, 13, 51714], "temperature": 0.0, "avg_logprob": -0.14674968933791258,
  "compression_ratio": 1.705179282868526, "no_speech_prob": 0.42380788922309875},
  {"id": 95, "seek": 77472, "start": 774.72, "end": 776.72, "text": " On the.", "tokens":
  [50364, 1282, 264, 13, 50464], "temperature": 0.0, "avg_logprob": -0.26192683093952684,
  "compression_ratio": 1.3529411764705883, "no_speech_prob": 0.0295390747487545},
  {"id": 96, "seek": 77472, "start": 776.72, "end": 784.72, "text": " A and an implementation
  on top of Lucin so it''s all inside Java so it kind of runs in the same gvm right.",
  "tokens": [50464, 316, 293, 364, 11420, 322, 1192, 295, 9593, 259, 370, 309, 311,
  439, 1854, 10745, 370, 309, 733, 295, 6676, 294, 264, 912, 290, 85, 76, 558, 13,
  50864], "temperature": 0.0, "avg_logprob": -0.26192683093952684, "compression_ratio":
  1.3529411764705883, "no_speech_prob": 0.0295390747487545}, {"id": 97, "seek": 77472,
  "start": 784.72, "end": 791.72, "text": " The approach that you you guys have implemented
  it''s basically like a.", "tokens": [50864, 440, 3109, 300, 291, 291, 1074, 362,
  12270, 309, 311, 1936, 411, 257, 13, 51214], "temperature": 0.0, "avg_logprob":
  -0.26192683093952684, "compression_ratio": 1.3529411764705883, "no_speech_prob":
  0.0295390747487545}, {"id": 98, "seek": 79172, "start": 791.72, "end": 811.72, "text":
  " A vector search backend right which kind of runs somewhere else let''s see if
  we''re using the cloud offering but at the same time it feels like a sort of like
  native to elastic search so I don''t need to do much right I just need to install
  the plugin of course I need to have credentials.", "tokens": [50364, 316, 8062,
  3164, 38087, 558, 597, 733, 295, 6676, 4079, 1646, 718, 311, 536, 498, 321, 434,
  1228, 264, 4588, 8745, 457, 412, 264, 912, 565, 309, 3417, 411, 257, 1333, 295,
  411, 8470, 281, 17115, 3164, 370, 286, 500, 380, 643, 281, 360, 709, 558, 286, 445,
  643, 281, 3625, 264, 23407, 295, 1164, 286, 643, 281, 362, 27404, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.11885370107797476, "compression_ratio": 1.5683060109289617,
  "no_speech_prob": 0.4349227547645569}, {"id": 99, "seek": 81172, "start": 811.72,
  "end": 838.72, "text": " And what I wanted to say is that it feels like you expand
  the capabilities of elastic search beyond what what it offers in a way that you
  can actually remove the load of vector search away from it to another back and right
  can you talk a bit more on the unit cost on on this kind of unit economy and and
  and sort of advantages of the approach that that you have implemented.", "tokens":
  [50364, 400, 437, 286, 1415, 281, 584, 307, 300, 309, 3417, 411, 291, 5268, 264,
  10862, 295, 17115, 3164, 4399, 437, 437, 309, 7736, 294, 257, 636, 300, 291, 393,
  767, 4159, 264, 3677, 295, 8062, 3164, 1314, 490, 309, 281, 1071, 646, 293, 558,
  393, 291, 751, 257, 857, 544, 322, 264, 4985, 2063, 322, 322, 341, 733, 295, 4985,
  5010, 293, 293, 293, 1333, 295, 14906, 295, 264, 3109, 300, 300, 291, 362, 12270,
  13, 51714], "temperature": 0.0, "avg_logprob": -0.11812107563018799, "compression_ratio":
  1.7077625570776256, "no_speech_prob": 0.05050776153802872}, {"id": 100, "seek":
  83872, "start": 838.72, "end": 861.72, "text": " Yeah, this is a great point actually
  so but we are trying to decouple storage and compute so let''s say for instance
  customer with elastic or open search and they they''re having like tens of clusters
  and they would like you know to scale it and to optimize it so we are running on
  top of of elastic and you can.", "tokens": [50364, 865, 11, 341, 307, 257, 869,
  935, 767, 370, 457, 321, 366, 1382, 281, 979, 263, 781, 6725, 293, 14722, 370, 718,
  311, 584, 337, 5197, 5474, 365, 17115, 420, 1269, 3164, 293, 436, 436, 434, 1419,
  411, 10688, 295, 23313, 293, 436, 576, 411, 291, 458, 281, 4373, 309, 293, 281,
  19719, 309, 370, 321, 366, 2614, 322, 1192, 295, 295, 17115, 293, 291, 393, 13,
  51514], "temperature": 0.0, "avg_logprob": -0.12943125442719797, "compression_ratio":
  1.5897435897435896, "no_speech_prob": 0.023487763479351997}, {"id": 101, "seek":
  86172, "start": 861.72, "end": 881.72, "text": " Our solution is kind of the compute
  for elastic so they can run and scale and reduce the infrastructure cost because
  you know all of these is is a is a question of how many machines do you run okay
  so you can get like 99.9 recall it and or accuracy.", "tokens": [50364, 2621, 3827,
  307, 733, 295, 264, 14722, 337, 17115, 370, 436, 393, 1190, 293, 4373, 293, 5407,
  264, 6896, 2063, 570, 291, 458, 439, 295, 613, 307, 307, 257, 307, 257, 1168, 295,
  577, 867, 8379, 360, 291, 1190, 1392, 370, 291, 393, 483, 411, 11803, 13, 24, 9901,
  309, 293, 420, 14170, 13, 51364], "temperature": 0.0, "avg_logprob": -0.15338777673655543,
  "compression_ratio": 1.5182926829268293, "no_speech_prob": 0.10750913619995117},
  {"id": 102, "seek": 88172, "start": 881.72, "end": 893.72, "text": " And you can
  get like single digit millisecond latency but in terms of the infrastructure costs
  so you know one of the biggest challenges today for enterprises is the.", "tokens":
  [50364, 400, 291, 393, 483, 411, 2167, 14293, 27940, 18882, 27043, 457, 294, 2115,
  295, 264, 6896, 5497, 370, 291, 458, 472, 295, 264, 3880, 4759, 965, 337, 29034,
  307, 264, 13, 50964], "temperature": 0.0, "avg_logprob": -0.1948120525905064, "compression_ratio":
  1.360655737704918, "no_speech_prob": 0.06562619656324387}, {"id": 103, "seek": 89372,
  "start": 893.72, "end": 922.72, "text": " The low margins due to heavy infrastructure
  applications so if you are running GPU on the cloud or like heavy machines with
  big machines with high memory it''s great in terms of the business because it''s
  great in terms of the dev team in terms of we are getting great performance high
  recall but again when you''re moving and you''re discussing on on the business side.",
  "tokens": [50414, 440, 2295, 30317, 3462, 281, 4676, 6896, 5821, 370, 498, 291,
  366, 2614, 18407, 322, 264, 4588, 420, 411, 4676, 8379, 365, 955, 8379, 365, 1090,
  4675, 309, 311, 869, 294, 2115, 295, 264, 1606, 570, 309, 311, 869, 294, 2115, 295,
  264, 1905, 1469, 294, 2115, 295, 321, 366, 1242, 869, 3389, 1090, 9901, 457, 797,
  562, 291, 434, 2684, 293, 291, 434, 10850, 322, 322, 264, 1606, 1252, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.1383481927820154, "compression_ratio": 1.7345971563981042,
  "no_speech_prob": 0.14363382756710052}, {"id": 104, "seek": 92372, "start": 923.72,
  "end": 952.72, "text": " So in terms of the margins and the profit of the companies
  and today it''s a big issue you know with companies that are having the challenge
  of being profitable so we are trying and we add like a few benchmarks we are trying
  to reduce the infrastructure cost so instead of 10 machines it can be two machines
  and and our accelerator our.", "tokens": [50364, 407, 294, 2115, 295, 264, 30317,
  293, 264, 7475, 295, 264, 3431, 293, 965, 309, 311, 257, 955, 2734, 291, 458, 365,
  3431, 300, 366, 1419, 264, 3430, 295, 885, 21608, 370, 321, 366, 1382, 293, 321,
  909, 411, 257, 1326, 43751, 321, 366, 1382, 281, 5407, 264, 6896, 2063, 370, 2602,
  295, 1266, 8379, 309, 393, 312, 732, 8379, 293, 293, 527, 39889, 527, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.12335879560829936, "compression_ratio": 1.6834170854271358,
  "no_speech_prob": 0.009290657006204128}, {"id": 105, "seek": 95372, "start": 953.72,
  "end": 977.72, "text": " For APU and with that you can you know scale it and you
  know one one other interesting thing is like many companies are talking about the
  scale challenge about the one billion scale challenge so and you know data is exploding
  right because you know today they are.", "tokens": [50364, 1171, 5372, 52, 293,
  365, 300, 291, 393, 291, 458, 4373, 309, 293, 291, 458, 472, 472, 661, 1880, 551,
  307, 411, 867, 3431, 366, 1417, 466, 264, 4373, 3430, 466, 264, 472, 5218, 4373,
  3430, 370, 293, 291, 458, 1412, 307, 35175, 558, 570, 291, 458, 965, 436, 366, 13,
  51564], "temperature": 0.0, "avg_logprob": -0.1617334019054066, "compression_ratio":
  1.6815286624203822, "no_speech_prob": 0.02717452310025692}, {"id": 106, "seek":
  97772, "start": 977.72, "end": 1006.72, "text": " 80 zetabytes and 10 years ago
  it was like 16 so essentially like data is growing very fast and I assume that in
  the next couple of years it will grow exponentially and 90% of this data and the
  data that is created every year is unstructured so you know this is the cliche of
  finding a needle in a haystack.", "tokens": [50364, 4688, 710, 302, 24538, 293,
  1266, 924, 2057, 309, 390, 411, 3165, 370, 4476, 411, 1412, 307, 4194, 588, 2370,
  293, 286, 6552, 300, 294, 264, 958, 1916, 295, 924, 309, 486, 1852, 37330, 293,
  4289, 4, 295, 341, 1412, 293, 264, 1412, 300, 307, 2942, 633, 1064, 307, 18799,
  46847, 370, 291, 458, 341, 307, 264, 46705, 295, 5006, 257, 11037, 294, 257, 4842,
  372, 501, 13, 51814], "temperature": 0.0, "avg_logprob": -0.131530331893706, "compression_ratio":
  1.5612244897959184, "no_speech_prob": 0.050234563648700714}, {"id": 107, "seek":
  100772, "start": 1007.72, "end": 1036.72, "text": " So in terms of and I assume
  more and more companies will face the scale challenge like above one billion and
  I know that this is a challenge for some of the search engine companies you know
  scaling to hundreds of millions and billions and I had a conversation with one of
  the biggest e-commerce in in Asia and he told me yeah our our challenges to scale
  they have like two billion.", "tokens": [50364, 407, 294, 2115, 295, 293, 286, 6552,
  544, 293, 544, 3431, 486, 1851, 264, 4373, 3430, 411, 3673, 472, 5218, 293, 286,
  458, 300, 341, 307, 257, 3430, 337, 512, 295, 264, 3164, 2848, 3431, 291, 458, 21589,
  281, 6779, 295, 6803, 293, 17375, 293, 286, 632, 257, 3761, 365, 472, 295, 264,
  3880, 308, 12, 26926, 294, 294, 10038, 293, 415, 1907, 385, 1338, 527, 527, 4759,
  281, 4373, 436, 362, 411, 732, 5218, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.12570935487747192, "compression_ratio": 1.7720930232558139, "no_speech_prob":
  0.013040537014603615}, {"id": 108, "seek": 103672, "start": 1036.72, "end": 1065.72,
  "text": " Index and again the infrastructure cost is a major issue I read a post
  by Amazon''s CFO and like a week ago and their focus right now is reducing the infrastructure
  cost for their customers and any solution that can reduce the infrastructure cost
  for enterprises I think it''s a major issue for.", "tokens": [50364, 33552, 293,
  797, 264, 6896, 2063, 307, 257, 2563, 2734, 286, 1401, 257, 2183, 538, 6795, 311,
  383, 18067, 293, 411, 257, 1243, 2057, 293, 641, 1879, 558, 586, 307, 12245, 264,
  6896, 2063, 337, 641, 4581, 293, 604, 3827, 300, 393, 5407, 264, 6896, 2063, 337,
  29034, 286, 519, 309, 311, 257, 2563, 2734, 337, 13, 51814], "temperature": 0.0,
  "avg_logprob": -0.16459927793409004, "compression_ratio": 1.723529411764706, "no_speech_prob":
  0.02813696302473545}, {"id": 109, "seek": 106572, "start": 1065.72, "end": 1074.72,
  "text": " Not only R&D teams but business and decision-makers in enterprises.",
  "tokens": [50364, 1726, 787, 497, 5, 35, 5491, 457, 1606, 293, 3537, 12, 15870,
  294, 29034, 13, 50814], "temperature": 0.0, "avg_logprob": -0.144998599956562, "compression_ratio":
  1.6153846153846154, "no_speech_prob": 0.07004126906394958}, {"id": 110, "seek":
  106572, "start": 1074.72, "end": 1091.72, "text": " Yeah well I will I will pull
  for that link so we can also include it in the in the show notes some of our listeners
  by the way find it quite educational to have all this additional links and study
  materials and I think we can also include that that''s super super cool.", "tokens":
  [50814, 865, 731, 286, 486, 286, 486, 2235, 337, 300, 2113, 370, 321, 393, 611,
  4090, 309, 294, 264, 294, 264, 855, 5570, 512, 295, 527, 23274, 538, 264, 636, 915,
  309, 1596, 10189, 281, 362, 439, 341, 4497, 6123, 293, 2979, 5319, 293, 286, 519,
  321, 393, 611, 4090, 300, 300, 311, 1687, 1687, 1627, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.144998599956562, "compression_ratio": 1.6153846153846154,
  "no_speech_prob": 0.07004126906394958}, {"id": 111, "seek": 109172, "start": 1091.72,
  "end": 1115.72, "text": " So in a way like your challenges that you basically need
  to as you said there are low margins right for this big players everyone tries to
  stay profitable so in a way your challenges to not only fit into that narrow kind
  of window but also be profitable yourself right so like you like provide that acceleration.",
  "tokens": [50364, 407, 294, 257, 636, 411, 428, 4759, 300, 291, 1936, 643, 281,
  382, 291, 848, 456, 366, 2295, 30317, 558, 337, 341, 955, 4150, 1518, 9898, 281,
  1754, 21608, 370, 294, 257, 636, 428, 4759, 281, 406, 787, 3318, 666, 300, 9432,
  733, 295, 4910, 457, 611, 312, 21608, 1803, 558, 370, 411, 291, 411, 2893, 300,
  17162, 13, 51564], "temperature": 0.0, "avg_logprob": -0.15088989621117002, "compression_ratio":
  1.7049180327868851, "no_speech_prob": 0.5821470022201538}, {"id": 112, "seek": 111572,
  "start": 1115.72, "end": 1125.72, "text": " What do you think where do you stand
  today on that I do you think there is a lot still to do or do you think it''s already
  something that companies can try.", "tokens": [50364, 708, 360, 291, 519, 689, 360,
  291, 1463, 965, 322, 300, 286, 360, 291, 519, 456, 307, 257, 688, 920, 281, 360,
  420, 360, 291, 519, 309, 311, 1217, 746, 300, 3431, 393, 853, 13, 50864], "temperature":
  0.0, "avg_logprob": -0.17950748072730172, "compression_ratio": 1.681081081081081,
  "no_speech_prob": 0.1673039197921753}, {"id": 113, "seek": 111572, "start": 1125.72,
  "end": 1143.72, "text": " Yeah so today we have like the first generation of our
  AI chip the APU the potential of improving our hardware and our bill of material
  of our hardware and", "tokens": [50864, 865, 370, 965, 321, 362, 411, 264, 700,
  5125, 295, 527, 7318, 11409, 264, 5372, 52, 264, 3995, 295, 11470, 527, 8837, 293,
  527, 2961, 295, 2527, 295, 527, 8837, 293, 51764], "temperature": 0.0, "avg_logprob":
  -0.17950748072730172, "compression_ratio": 1.681081081081081, "no_speech_prob":
  0.1673039197921753}, {"id": 114, "seek": 114372, "start": 1143.72, "end": 1157.72,
  "text": " generally speaking next year we launch our second generation so for instance
  if today we can you know in terms of performance we are talking about single double
  digit millisecond latency with one APU.", "tokens": [50364, 5101, 4124, 958, 1064,
  321, 4025, 527, 1150, 5125, 370, 337, 5197, 498, 965, 321, 393, 291, 458, 294, 2115,
  295, 3389, 321, 366, 1417, 466, 2167, 3834, 14293, 27940, 18882, 27043, 365, 472,
  5372, 52, 13, 51064], "temperature": 0.0, "avg_logprob": -0.17996202032250094, "compression_ratio":
  1.6909871244635193, "no_speech_prob": 0.09651032835245132}, {"id": 115, "seek":
  114372, "start": 1157.72, "end": 1172.72, "text": " Next year we will launch our
  second generation it will be more than 10x faster so I think we are just scratching
  the tip of the iceberg so the I think that the hardware challenge is solved but.",
  "tokens": [51064, 3087, 1064, 321, 486, 4025, 527, 1150, 5125, 309, 486, 312, 544,
  813, 1266, 87, 4663, 370, 286, 519, 321, 366, 445, 29699, 264, 4125, 295, 264, 38880,
  370, 264, 286, 519, 300, 264, 8837, 3430, 307, 13041, 457, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.17996202032250094, "compression_ratio": 1.6909871244635193,
  "no_speech_prob": 0.09651032835245132}, {"id": 116, "seek": 117272, "start": 1172.72,
  "end": 1189.72, "text": " You know every week we have like a new implementation
  and improving our performance on the software layer so we have a few layers we have
  the hardware layers so I spoke about it like the first generation and the second
  generation.", "tokens": [50364, 509, 458, 633, 1243, 321, 362, 411, 257, 777, 11420,
  293, 11470, 527, 3389, 322, 264, 4722, 4583, 370, 321, 362, 257, 1326, 7914, 321,
  362, 264, 8837, 7914, 370, 286, 7179, 466, 309, 411, 264, 700, 5125, 293, 264, 1150,
  5125, 13, 51214], "temperature": 0.0, "avg_logprob": -0.1168725439842711, "compression_ratio":
  1.6312056737588652, "no_speech_prob": 0.009129791520535946}, {"id": 117, "seek":
  118972, "start": 1189.72, "end": 1198.72, "text": " I believe that there there''s
  a huge potential in terms of optimizing our software layer because it is.", "tokens":
  [50364, 286, 1697, 300, 456, 456, 311, 257, 2603, 3995, 294, 2115, 295, 40425, 527,
  4722, 4583, 570, 309, 307, 13, 50814], "temperature": 0.0, "avg_logprob": -0.08955100003410787,
  "compression_ratio": 1.7117647058823529, "no_speech_prob": 0.07505377382040024},
  {"id": 118, "seek": 118972, "start": 1198.72, "end": 1202.72, "text": " We are trying
  to reinvent search so.", "tokens": [50814, 492, 366, 1382, 281, 33477, 3164, 370,
  13, 51014], "temperature": 0.0, "avg_logprob": -0.08955100003410787, "compression_ratio":
  1.7117647058823529, "no_speech_prob": 0.07505377382040024}, {"id": 119, "seek":
  118972, "start": 1202.72, "end": 1214.72, "text": " I think there''s a huge potential
  on on the hardware side but I think we are just we are just we didn''t even start
  to optimize our software performance.", "tokens": [51014, 286, 519, 456, 311, 257,
  2603, 3995, 322, 322, 264, 8837, 1252, 457, 286, 519, 321, 366, 445, 321, 366, 445,
  321, 994, 380, 754, 722, 281, 19719, 527, 4722, 3389, 13, 51614], "temperature":
  0.0, "avg_logprob": -0.08955100003410787, "compression_ratio": 1.7117647058823529,
  "no_speech_prob": 0.07505377382040024}, {"id": 120, "seek": 121472, "start": 1214.72,
  "end": 1233.72, "text": " Recently we found a new implementation to improve the
  latency by reduce the latency by 40% like it was two weeks ago so hopefully we will
  launch it to production in the upcoming in the next up upcoming weeks.", "tokens":
  [50364, 20072, 321, 1352, 257, 777, 11420, 281, 3470, 264, 27043, 538, 5407, 264,
  27043, 538, 3356, 4, 411, 309, 390, 732, 3259, 2057, 370, 4696, 321, 486, 4025,
  309, 281, 4265, 294, 264, 11500, 294, 264, 958, 493, 11500, 3259, 13, 51314], "temperature":
  0.0, "avg_logprob": -0.10941989686754015, "compression_ratio": 1.5182481751824817,
  "no_speech_prob": 0.12799666821956635}, {"id": 121, "seek": 123372, "start": 1233.72,
  "end": 1250.72, "text": " So and in terms of your question yeah I think we are just
  at the beginning and I believe that we can optimize both on the on the hardware
  and the software layer and hopefully it will be very profitable.", "tokens": [50364,
  407, 293, 294, 2115, 295, 428, 1168, 1338, 286, 519, 321, 366, 445, 412, 264, 2863,
  293, 286, 1697, 300, 321, 393, 19719, 1293, 322, 264, 322, 264, 8837, 293, 264,
  4722, 4583, 293, 4696, 309, 486, 312, 588, 21608, 13, 51214], "temperature": 0.0,
  "avg_logprob": -0.11150744756062826, "compression_ratio": 1.4225352112676057, "no_speech_prob":
  0.15878064930438995}, {"id": 122, "seek": 125072, "start": 1250.72, "end": 1277.72,
  "text": " Sounds great I mean in general it was since I have a had exposure to it
  as we implemented the image search demo it was quite interesting how you know how
  easy it was to set it up right so it like and and you don''t need to worry about
  that hardware thing yeah it acts a little bit like a black box but on the other
  hand it''s very scalable so.", "tokens": [50364, 14576, 869, 286, 914, 294, 2674,
  309, 390, 1670, 286, 362, 257, 632, 10420, 281, 309, 382, 321, 12270, 264, 3256,
  3164, 10723, 309, 390, 1596, 1880, 577, 291, 458, 577, 1858, 309, 390, 281, 992,
  309, 493, 558, 370, 309, 411, 293, 293, 291, 500, 380, 643, 281, 3292, 466, 300,
  8837, 551, 1338, 309, 10672, 257, 707, 857, 411, 257, 2211, 2424, 457, 322, 264,
  661, 1011, 309, 311, 588, 38481, 370, 13, 51714], "temperature": 0.0, "avg_logprob":
  -0.11460753332210492, "compression_ratio": 1.6009389671361502, "no_speech_prob":
  0.30056703090667725}, {"id": 123, "seek": 127772, "start": 1277.72, "end": 1305.72,
  "text": " And you guys also have I will make sure to link this you also published
  the is called neural hashing algorithm right which you which you use one of the
  algorithms that you have implemented it would also be equal to drill in into that
  direction but I mean in general it was fairly straightforward how you know how we
  upload the data how it gets indexed and then how we can query.", "tokens": [50364,
  400, 291, 1074, 611, 362, 286, 486, 652, 988, 281, 2113, 341, 291, 611, 6572, 264,
  307, 1219, 18161, 575, 571, 9284, 558, 597, 291, 597, 291, 764, 472, 295, 264, 14642,
  300, 291, 362, 12270, 309, 576, 611, 312, 2681, 281, 11392, 294, 666, 300, 3513,
  457, 286, 914, 294, 2674, 309, 390, 6457, 15325, 577, 291, 458, 577, 321, 6580,
  264, 1412, 577, 309, 2170, 8186, 292, 293, 550, 577, 321, 393, 14581, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.11058735847473145, "compression_ratio": 1.6725663716814159,
  "no_speech_prob": 0.02938235178589821}, {"id": 124, "seek": 130572, "start": 1305.72,
  "end": 1326.72, "text": " Yeah I was just thinking to take it a little bit deeper
  can you talk to some of the features you know many of the vector database players
  they say why do you need vector databases because first of all if you took files
  for example a similar framework you wouldn''t have the filter support right and
  of course in.", "tokens": [50364, 865, 286, 390, 445, 1953, 281, 747, 309, 257,
  707, 857, 7731, 393, 291, 751, 281, 512, 295, 264, 4122, 291, 458, 867, 295, 264,
  8062, 8149, 4150, 436, 584, 983, 360, 291, 643, 8062, 22380, 570, 700, 295, 439,
  498, 291, 1890, 7098, 337, 1365, 257, 2531, 8388, 291, 2759, 380, 362, 264, 6608,
  1406, 558, 293, 295, 1164, 294, 13, 51414], "temperature": 0.0, "avg_logprob": -0.11486555590774074,
  "compression_ratio": 1.555, "no_speech_prob": 0.004475673194974661}, {"id": 125,
  "seek": 132672, "start": 1327.1200000000001, "end": 1343.72, "text": " In real application
  like such app you do need filters alongside the whatever retriever you implement
  right keyword or vector so can you talk a bit more about features and maybe also
  touch on the algorithms that you guys have implemented.", "tokens": [50384, 682,
  957, 3861, 411, 1270, 724, 291, 360, 643, 15995, 12385, 264, 2035, 19817, 331, 291,
  4445, 558, 20428, 420, 8062, 370, 393, 291, 751, 257, 857, 544, 466, 4122, 293,
  1310, 611, 2557, 322, 264, 14642, 300, 291, 1074, 362, 12270, 13, 51214], "temperature":
  0.0, "avg_logprob": -0.14714757432328893, "compression_ratio": 1.490566037735849,
  "no_speech_prob": 0.00956221204251051}, {"id": 126, "seek": 134372, "start": 1344.72,
  "end": 1354.72, "text": " Yeah yeah so there are various types of features and implementations
  we are working with you know the common.", "tokens": [50414, 865, 1338, 370, 456,
  366, 3683, 3467, 295, 4122, 293, 4445, 763, 321, 366, 1364, 365, 291, 458, 264,
  2689, 13, 50914], "temperature": 0.0, "avg_logprob": -0.16258420944213867, "compression_ratio":
  1.46, "no_speech_prob": 0.029695376753807068}, {"id": 127, "seek": 134372, "start":
  1356.72, "end": 1365.72, "text": " Algorithms it can be either flat search for applications
  like it can be a face recognition where you need to.", "tokens": [51014, 35014,
  6819, 2592, 309, 393, 312, 2139, 4962, 3164, 337, 5821, 411, 309, 393, 312, 257,
  1851, 11150, 689, 291, 643, 281, 13, 51464], "temperature": 0.0, "avg_logprob":
  -0.16258420944213867, "compression_ratio": 1.46, "no_speech_prob": 0.029695376753807068},
  {"id": 128, "seek": 136572, "start": 1365.72, "end": 1386.72, "text": " Search any
  every record we have implementations of the a nm i vf and new implementation of
  hnsw on our apu and pre filter and other features one of one of our.", "tokens":
  [50364, 17180, 604, 633, 2136, 321, 362, 4445, 763, 295, 264, 257, 297, 76, 741,
  371, 69, 293, 777, 11420, 295, 276, 3695, 86, 322, 527, 1882, 84, 293, 659, 6608,
  293, 661, 4122, 472, 295, 472, 295, 527, 13, 51414], "temperature": 0.0, "avg_logprob":
  -0.4684944152832031, "compression_ratio": 1.4587155963302751, "no_speech_prob":
  0.07207847386598587}, {"id": 129, "seek": 138672, "start": 1386.72, "end": 1401.72,
  "text": " One of the areas that we would like to focus is as you mentioned is is
  to simplify so we can you know you can work with it as a as a black box and install
  the plugin and work with your.", "tokens": [50364, 1485, 295, 264, 3179, 300, 321,
  576, 411, 281, 1879, 307, 382, 291, 2835, 307, 307, 281, 20460, 370, 321, 393, 291,
  458, 291, 393, 589, 365, 309, 382, 257, 382, 257, 2211, 2424, 293, 3625, 264, 23407,
  293, 589, 365, 428, 13, 51114], "temperature": 0.0, "avg_logprob": -0.14856313137297936,
  "compression_ratio": 1.4453125, "no_speech_prob": 0.022032681852579117}, {"id":
  130, "seek": 140172, "start": 1401.72, "end": 1413.72, "text": " With your technological
  stack and with your search application either elastic open search or a vector search
  engine or vector database.", "tokens": [50364, 2022, 428, 18439, 8630, 293, 365,
  428, 3164, 3861, 2139, 17115, 1269, 3164, 420, 257, 8062, 3164, 2848, 420, 8062,
  8149, 13, 50964], "temperature": 0.0, "avg_logprob": -0.2360800046187181, "compression_ratio":
  1.3917525773195876, "no_speech_prob": 0.028889549896121025}, {"id": 131, "seek":
  141372, "start": 1414.72, "end": 1437.72, "text": " And pre filter as you mentioned
  is supported and I think that we should focus on simplifying this is our biggest
  challenge simplifying the work with our platform and creating more integrations
  and more connectors not not on the feature level but in terms of you know working
  with the the ecosystem this is this is our main.", "tokens": [50414, 400, 659, 6608,
  382, 291, 2835, 307, 8104, 293, 286, 519, 300, 321, 820, 1879, 322, 6883, 5489,
  341, 307, 527, 3880, 3430, 6883, 5489, 264, 589, 365, 527, 3663, 293, 4084, 544,
  3572, 763, 293, 544, 31865, 406, 406, 322, 264, 4111, 1496, 457, 294, 2115, 295,
  291, 458, 1364, 365, 264, 264, 11311, 341, 307, 341, 307, 527, 2135, 13, 51564],
  "temperature": 0.0, "avg_logprob": -0.1380288673169685, "compression_ratio": 1.6649484536082475,
  "no_speech_prob": 0.08103273063898087}, {"id": 132, "seek": 143772, "start": 1437.72,
  "end": 1457.72, "text": " We are in focus right now and again improving the performance
  because we are you know customer obsessed and we would like our customer to get
  the lowest infrastructure cost and with without sacrificing latency and.", "tokens":
  [50364, 492, 366, 294, 1879, 558, 586, 293, 797, 11470, 264, 3389, 570, 321, 366,
  291, 458, 5474, 16923, 293, 321, 576, 411, 527, 5474, 281, 483, 264, 12437, 6896,
  2063, 293, 365, 1553, 42294, 27043, 293, 13, 51364], "temperature": 0.0, "avg_logprob":
  -0.33304762840270996, "compression_ratio": 1.5063291139240507, "no_speech_prob":
  0.07368817180395126}, {"id": 133, "seek": 143772, "start": 1457.72, "end": 1460.72,
  "text": " Sorry and the accuracy.", "tokens": [51364, 4919, 293, 264, 14170, 13,
  51514], "temperature": 0.0, "avg_logprob": -0.33304762840270996, "compression_ratio":
  1.5063291139240507, "no_speech_prob": 0.07368817180395126}, {"id": 134, "seek":
  146072, "start": 1461.72, "end": 1480.72, "text": " Yeah that makes sense and especially
  like to do this at scale right I know that some of the players they say that it''s
  very rare that there are clients with more than you dozens of millions of items
  right but today you already mentioned that there are clients.", "tokens": [50414,
  865, 300, 1669, 2020, 293, 2318, 411, 281, 360, 341, 412, 4373, 558, 286, 458, 300,
  512, 295, 264, 4150, 436, 584, 300, 309, 311, 588, 5892, 300, 456, 366, 6982, 365,
  544, 813, 291, 18431, 295, 6803, 295, 4754, 558, 457, 965, 291, 1217, 2835, 300,
  456, 366, 6982, 13, 51364], "temperature": 0.0, "avg_logprob": -0.13310369144786488,
  "compression_ratio": 1.625, "no_speech_prob": 0.09243606775999069}, {"id": 135,
  "seek": 148072, "start": 1480.72, "end": 1505.72, "text": " Which have you know
  more than a billion items maybe more than two billion items so do you think that
  going forward you will see more of these second you know type of players with more
  data or do you think that there is still a use for dedicated hardware for this kind
  of smaller scale players.", "tokens": [50364, 3013, 362, 291, 458, 544, 813, 257,
  5218, 4754, 1310, 544, 813, 732, 5218, 4754, 370, 360, 291, 519, 300, 516, 2128,
  291, 486, 536, 544, 295, 613, 1150, 291, 458, 2010, 295, 4150, 365, 544, 1412, 420,
  360, 291, 519, 300, 456, 307, 920, 257, 764, 337, 8374, 8837, 337, 341, 733, 295,
  4356, 4373, 4150, 13, 51614], "temperature": 0.0, "avg_logprob": -0.11741599728984217,
  "compression_ratio": 1.7650602409638554, "no_speech_prob": 0.12625530362129211},
  {"id": 136, "seek": 150572, "start": 1506.72, "end": 1534.72, "text": " Yeah yeah
  absolutely agree with you I think that in terms of the scale challenge we are we
  are working with with customers and some of them here as you mentioned like tens
  of billions but moving forward I think most of the enterprises and the big companies
  will move forward and they will scale to one billion 10 billion and maybe even more.",
  "tokens": [50414, 865, 1338, 3122, 3986, 365, 291, 286, 519, 300, 294, 2115, 295,
  264, 4373, 3430, 321, 366, 321, 366, 1364, 365, 365, 4581, 293, 512, 295, 552, 510,
  382, 291, 2835, 411, 10688, 295, 17375, 457, 2684, 2128, 286, 519, 881, 295, 264,
  29034, 293, 264, 955, 3431, 486, 1286, 2128, 293, 436, 486, 4373, 281, 472, 5218,
  1266, 5218, 293, 1310, 754, 544, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.12302655759065048, "compression_ratio": 1.7309644670050761, "no_speech_prob":
  0.10071995854377747}, {"id": 137, "seek": 153472, "start": 1534.72, "end": 1563.72,
  "text": " In terms of like the ecosystem so my two cents is that companies are stealing
  the concept of keyboard search for some applications TF IDF at bm 25 for some for
  some application it''s a good solution and you know you don''t need an hammer for
  a screw driver.", "tokens": [50414, 682, 2115, 295, 411, 264, 11311, 370, 452, 732,
  14941, 307, 300, 3431, 366, 19757, 264, 3410, 295, 10186, 3164, 337, 512, 5821,
  40964, 7348, 37, 412, 272, 76, 3552, 337, 512, 337, 512, 3861, 309, 311, 257, 665,
  3827, 293, 291, 458, 291, 500, 380, 643, 364, 13017, 337, 257, 5630, 6787, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.27452639529579564, "compression_ratio": 1.4912280701754386,
  "no_speech_prob": 0.04111647233366966}, {"id": 138, "seek": 156472, "start": 1564.72,
  "end": 1584.72, "text": " So that''s the problem right so for some use cases keyboard
  search is a good fit and this is like you know part of the concept of vibrate search
  and so I think we are still we''re we''re the beginning of the the vector search
  if I may call it the vector search revolution when you know where you can have the.",
  "tokens": [50364, 407, 300, 311, 264, 1154, 558, 370, 337, 512, 764, 3331, 10186,
  3164, 307, 257, 665, 3318, 293, 341, 307, 411, 291, 458, 644, 295, 264, 3410, 295,
  11666, 4404, 3164, 293, 370, 286, 519, 321, 366, 920, 321, 434, 321, 434, 264, 2863,
  295, 264, 264, 8062, 3164, 498, 286, 815, 818, 309, 264, 8062, 3164, 8894, 562,
  291, 458, 689, 291, 393, 362, 264, 13, 51364], "temperature": 0.0, "avg_logprob":
  -0.2443498692042391, "compression_ratio": 1.6451612903225807, "no_speech_prob":
  0.048471856862306595}, {"id": 139, "seek": 158472, "start": 1584.72, "end": 1613.72,
  "text": " Back concept like any unstructured data we were usually we are talking
  about text but there are broad areas that we could you know develop some cool stuff
  for as I mentioned genome audio video search we have a notebook with you know website
  notebook with video search and again the the there''s a broad spectrum of applications
  that companies can develop some cool stuff cool stuff.", "tokens": [50364, 5833,
  3410, 411, 604, 18799, 46847, 1412, 321, 645, 2673, 321, 366, 1417, 466, 2487, 457,
  456, 366, 4152, 3179, 300, 321, 727, 291, 458, 1499, 512, 1627, 1507, 337, 382,
  286, 2835, 1049, 423, 6278, 960, 3164, 321, 362, 257, 21060, 365, 291, 458, 3144,
  21060, 365, 960, 3164, 293, 797, 264, 264, 456, 311, 257, 4152, 11143, 295, 5821,
  300, 3431, 393, 1499, 512, 1627, 1507, 1627, 1507, 13, 51814], "temperature": 0.0,
  "avg_logprob": -0.2134912078445022, "compression_ratio": 1.7720930232558139, "no_speech_prob":
  0.3108038604259491}, {"id": 140, "seek": 161472, "start": 1614.72, "end": 1627.72,
  "text": " And we are you know excited to see brilliant ideas and start up that are
  developing applications on top of of these vector search applications.", "tokens":
  [50364, 400, 321, 366, 291, 458, 2919, 281, 536, 10248, 3487, 293, 722, 493, 300,
  366, 6416, 5821, 322, 1192, 295, 295, 613, 8062, 3164, 5821, 13, 51014], "temperature":
  0.0, "avg_logprob": -0.18827401569911412, "compression_ratio": 1.5495049504950495,
  "no_speech_prob": 0.04221174120903015}, {"id": 141, "seek": 161472, "start": 1627.72,
  "end": 1640.72, "text": " Yeah you touch on that topic by the way which I also spoke
  to to some extent on the haystack conference in Berlin where I gave a keynote also
  make sure to give the link.", "tokens": [51014, 865, 291, 2557, 322, 300, 4829,
  538, 264, 636, 597, 286, 611, 7179, 281, 281, 512, 8396, 322, 264, 4842, 372, 501,
  7586, 294, 13848, 689, 286, 2729, 257, 33896, 611, 652, 988, 281, 976, 264, 2113,
  13, 51664], "temperature": 0.0, "avg_logprob": -0.18827401569911412, "compression_ratio":
  1.5495049504950495, "no_speech_prob": 0.04221174120903015}, {"id": 142, "seek":
  164072, "start": 1640.72, "end": 1669.72, "text": " Back turnbull said that let''s
  stop calling it vector search because and I don''t know how I really interested
  to really interested to hear your thoughts on that because in principle you you
  and I being product managers like if we think about some problem to solve right
  let''s say we want to introduce I don''t know question answering component in our
  search engines it''s not like we would probably if we didn''t know that we probably
  wouldn''t say oh I know how to solve it it''s vector search.", "tokens": [50364,
  5833, 1261, 37290, 848, 300, 718, 311, 1590, 5141, 309, 8062, 3164, 570, 293, 286,
  500, 380, 458, 577, 286, 534, 3102, 281, 534, 3102, 281, 1568, 428, 4598, 322, 300,
  570, 294, 8665, 291, 291, 293, 286, 885, 1674, 14084, 411, 498, 321, 519, 466, 512,
  1154, 281, 5039, 558, 718, 311, 584, 321, 528, 281, 5366, 286, 500, 380, 458, 1168,
  13430, 6542, 294, 527, 3164, 12982, 309, 311, 406, 411, 321, 576, 1391, 498, 321,
  994, 380, 458, 300, 321, 1391, 2759, 380, 584, 1954, 286, 458, 577, 281, 5039, 309,
  309, 311, 8062, 3164, 13, 51814], "temperature": 0.0, "avg_logprob": -0.12146264603994425,
  "compression_ratio": 1.8593155893536122, "no_speech_prob": 0.1279418170452118},
  {"id": 143, "seek": 166972, "start": 1669.72, "end": 1698.72, "text": " And so instead
  he was saying you know let''s call it relevance application right or relevance oriented
  application what''s your broad take on this you touched on this as well like people
  are not yet aware of this revolution it''s probably already happening but people
  don''t know what to do with it right and I just yesterday saw it with from one user
  saying can you actually explain what what can I do with it.", "tokens": [50364,
  400, 370, 2602, 415, 390, 1566, 291, 458, 718, 311, 818, 309, 32684, 3861, 558,
  420, 32684, 21841, 3861, 437, 311, 428, 4152, 747, 322, 341, 291, 9828, 322, 341,
  382, 731, 411, 561, 366, 406, 1939, 3650, 295, 341, 8894, 309, 311, 1391, 1217,
  2737, 457, 561, 500, 380, 458, 437, 281, 360, 365, 309, 558, 293, 286, 445, 5186,
  1866, 309, 365, 490, 472, 4195, 1566, 393, 291, 767, 2903, 437, 437, 393, 286, 360,
  365, 309, 13, 51814], "temperature": 0.0, "avg_logprob": -0.11065818014599028, "compression_ratio":
  1.7319148936170212, "no_speech_prob": 0.05738554149866104}, {"id": 144, "seek":
  169872, "start": 1698.72, "end": 1708.72, "text": " So do you think that the world
  is still let''s say the world of software development is still awakening to this
  new field.", "tokens": [50364, 407, 360, 291, 519, 300, 264, 1002, 307, 920, 718,
  311, 584, 264, 1002, 295, 4722, 3250, 307, 920, 31550, 281, 341, 777, 2519, 13,
  50864], "temperature": 0.0, "avg_logprob": -0.35846584359395134, "compression_ratio":
  1.8982300884955752, "no_speech_prob": 0.05404602363705635}, {"id": 145, "seek":
  169872, "start": 1708.72, "end": 1727.72, "text": " Yeah yeah absolutely I fully
  agree with you essentially when I''m talking with developers and I''m saying we
  are I''m talking again we are working on vector search they are like asking vector
  what and I think that most of the developers and this is one of the things that
  I''m going to do is I''m going to do it.", "tokens": [50864, 865, 1338, 3122, 286,
  4498, 3986, 365, 291, 4476, 562, 286, 478, 1417, 365, 8849, 293, 286, 478, 1566,
  321, 366, 286, 478, 1417, 797, 321, 366, 1364, 322, 8062, 3164, 436, 366, 411, 3365,
  8062, 437, 293, 286, 519, 300, 881, 295, 264, 8849, 293, 341, 307, 472, 295, 264,
  721, 300, 286, 478, 516, 281, 360, 307, 286, 478, 516, 281, 360, 309, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.35846584359395134, "compression_ratio": 1.8982300884955752,
  "no_speech_prob": 0.05404602363705635}, {"id": 146, "seek": 172772, "start": 1727.72,
  "end": 1756.72, "text": " And this is one of our challenges is to democratize AI
  and machine learning so in terms of technology my perspective and is that technology
  is an enabler if the best solution is vector search great it can you know outperform
  on on various applications but the technology on a product perspective so you are
  trying to create value I think that the first lesson of a product.", "tokens": [50364,
  400, 341, 307, 472, 295, 527, 4759, 307, 281, 37221, 1125, 7318, 293, 3479, 2539,
  370, 294, 2115, 295, 2899, 452, 4585, 293, 307, 300, 2899, 307, 364, 465, 455, 1918,
  498, 264, 1151, 3827, 307, 8062, 3164, 869, 309, 393, 291, 458, 484, 26765, 322,
  322, 3683, 5821, 457, 264, 2899, 322, 257, 1674, 4585, 370, 291, 366, 1382, 281,
  1884, 2158, 286, 519, 300, 264, 700, 6898, 295, 257, 1674, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.15559538308676188, "compression_ratio": 1.6801801801801801,
  "no_speech_prob": 0.004189042840152979}, {"id": 147, "seek": 175672, "start": 1756.72,
  "end": 1772.72, "text": " The second lesson of a product is to create value for
  your customer that''s it simple as that and what is the technology and what is under
  the hood and what is inside the black box it really doesn''t matter.", "tokens":
  [50364, 440, 1150, 6898, 295, 257, 1674, 307, 281, 1884, 2158, 337, 428, 5474, 300,
  311, 309, 2199, 382, 300, 293, 437, 307, 264, 2899, 293, 437, 307, 833, 264, 13376,
  293, 437, 307, 1854, 264, 2211, 2424, 309, 534, 1177, 380, 1871, 13, 51164], "temperature":
  0.2, "avg_logprob": -0.16074164370273022, "compression_ratio": 1.5073529411764706,
  "no_speech_prob": 0.01169244758784771}, {"id": 148, "seek": 177272, "start": 1772.72,
  "end": 1796.72, "text": " In terms of technology yeah there''s you know and we are
  like it''s a crazy time for developers in terms of the AI machine learning revolution
  stable diffusion generative generative AI and I''ve heard about that they are going
  open AI planning to launch the new GPT for.", "tokens": [50364, 682, 2115, 295,
  2899, 1338, 456, 311, 291, 458, 293, 321, 366, 411, 309, 311, 257, 3219, 565, 337,
  8849, 294, 2115, 295, 264, 7318, 3479, 2539, 8894, 8351, 25242, 1337, 1166, 1337,
  1166, 7318, 293, 286, 600, 2198, 466, 300, 436, 366, 516, 1269, 7318, 5038, 281,
  4025, 264, 777, 26039, 51, 337, 13, 51564], "temperature": 0.0, "avg_logprob": -0.15446628958491956,
  "compression_ratio": 1.4833333333333334, "no_speech_prob": 0.08518822491168976},
  {"id": 149, "seek": 179672, "start": 1796.72, "end": 1825.72, "text": " And the
  pace of innovation is is totally crazy so and it''s really hard to keep it to keep
  it simple to simplify it when when people are asking you you know there''s the grandmother
  test for startup state in plain English explain your idea in a plain English super
  challenging you know to simplify so when you know when developers or companies asking
  what is vector search I''m using the.", "tokens": [50364, 400, 264, 11638, 295,
  8504, 307, 307, 3879, 3219, 370, 293, 309, 311, 534, 1152, 281, 1066, 309, 281,
  1066, 309, 2199, 281, 20460, 309, 562, 562, 561, 366, 3365, 291, 291, 458, 456,
  311, 264, 14317, 1500, 337, 18578, 1785, 294, 11121, 3669, 2903, 428, 1558, 294,
  257, 11121, 3669, 1687, 7595, 291, 458, 281, 20460, 370, 562, 291, 458, 562, 8849,
  420, 3431, 3365, 437, 307, 8062, 3164, 286, 478, 1228, 264, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.1611012801145896, "compression_ratio": 1.7579908675799087,
  "no_speech_prob": 0.048631180077791214}, {"id": 150, "seek": 182672, "start": 1826.72,
  "end": 1851.72, "text": " The example of you know transforming words in the case
  of text to numbers it''s easy for us to compare numbers right we know that three
  is is close or similar to four right but what is the connection between king and
  queen okay so how do you represent it as a number.", "tokens": [50364, 440, 1365,
  295, 291, 458, 27210, 2283, 294, 264, 1389, 295, 2487, 281, 3547, 309, 311, 1858,
  337, 505, 281, 6794, 3547, 558, 321, 458, 300, 1045, 307, 307, 1998, 420, 2531,
  281, 1451, 558, 457, 437, 307, 264, 4984, 1296, 4867, 293, 12206, 1392, 370, 577,
  360, 291, 2906, 309, 382, 257, 1230, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.17193661705922272, "compression_ratio": 1.5647058823529412, "no_speech_prob":
  0.007253407966345549}, {"id": 151, "seek": 185172, "start": 1851.72, "end": 1880.72,
  "text": " So if you if you are trying again again I''m trying to super simplified
  if you are trying to build an equation what is the connection between king and queen
  so you can say king plus men minus woman equals to queen so you are you''re trying
  to represent it as numbers so this is the concept of vector you are representing
  I''m going to say.", "tokens": [50364, 407, 498, 291, 498, 291, 366, 1382, 797,
  797, 286, 478, 1382, 281, 1687, 26335, 498, 291, 366, 1382, 281, 1322, 364, 5367,
  437, 307, 264, 4984, 1296, 4867, 293, 12206, 370, 291, 393, 584, 4867, 1804, 1706,
  3175, 3059, 6915, 281, 12206, 370, 291, 366, 291, 434, 1382, 281, 2906, 309, 382,
  3547, 370, 341, 307, 264, 3410, 295, 8062, 291, 366, 13460, 286, 478, 516, 281,
  584, 13, 51814], "temperature": 0.0, "avg_logprob": -0.26626050794446793, "compression_ratio":
  1.8064516129032258, "no_speech_prob": 0.0976535975933075}, {"id": 152, "seek": 188072,
  "start": 1880.72, "end": 1909.72, "text": " So I''m trying to make sure that you
  are understanding and unstructured data and it can be you know with image image
  embedding etc and then I think like you know most of the tech companies today their
  core technology is search okay let''s take if you are looking for a movie it''s
  it''s Netflix if you are would like you know to hear something cool or your podcast
  so you are running query on Spotify vector podcast and you will get the.", "tokens":
  [50364, 407, 286, 478, 1382, 281, 652, 988, 300, 291, 366, 3701, 293, 18799, 46847,
  1412, 293, 309, 393, 312, 291, 458, 365, 3256, 3256, 12240, 3584, 5183, 293, 550,
  286, 519, 411, 291, 458, 881, 295, 264, 7553, 3431, 965, 641, 4965, 2899, 307, 3164,
  1392, 718, 311, 747, 498, 291, 366, 1237, 337, 257, 3169, 309, 311, 309, 311, 12778,
  498, 291, 366, 576, 411, 291, 458, 281, 1568, 746, 1627, 420, 428, 7367, 370, 291,
  366, 2614, 14581, 322, 29036, 8062, 7367, 293, 291, 486, 483, 264, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.3485026258103391, "compression_ratio": 1.7389558232931728,
  "no_speech_prob": 0.22334259748458862}, {"id": 153, "seek": 190972, "start": 1909.72,
  "end": 1938.72, "text": " Dmitry''s podcast you would like to buy a dress or and
  you you are trying to do it very simple you don''t usually more more of the let''s
  take for instance e-commerce right so most of the consumers don''t have the time
  and the patient to run you know SQL queries you know filter these filter that they
  would like to write it in a simple English or or in a different language okay yeah
  so let''s take for an example and.", "tokens": [50364, 413, 3508, 627, 311, 7367,
  291, 576, 411, 281, 2256, 257, 5231, 420, 293, 291, 291, 366, 1382, 281, 360, 309,
  588, 2199, 291, 500, 380, 2673, 544, 544, 295, 264, 718, 311, 747, 337, 5197, 308,
  12, 26926, 558, 370, 881, 295, 264, 11883, 500, 380, 362, 264, 565, 293, 264, 4537,
  281, 1190, 291, 458, 19200, 24109, 291, 458, 6608, 613, 6608, 300, 436, 576, 411,
  281, 2464, 309, 294, 257, 2199, 3669, 420, 420, 294, 257, 819, 2856, 1392, 1338,
  370, 718, 311, 747, 337, 364, 1365, 293, 13, 51814], "temperature": 0.4, "avg_logprob":
  -0.18317365144428455, "compression_ratio": 1.7107438016528926, "no_speech_prob":
  0.01184324361383915}, {"id": 154, "seek": 193972, "start": 1939.72, "end": 1968.72,
  "text": " Girl in Asia she would like to purchase a red and white short sleeve dress
  up until the the vector search revolution she didn''t had the option to do it so
  usually she will get like a similar result it will not always be red and white with
  short sleeve dress and what about the challenge of the language okay so if our English
  is not so great and she would like to purchase something.", "tokens": [50364, 8502,
  294, 10038, 750, 576, 411, 281, 8110, 257, 2182, 293, 2418, 2099, 21138, 5231, 493,
  1826, 264, 264, 8062, 3164, 8894, 750, 994, 380, 632, 264, 3614, 281, 360, 309,
  370, 2673, 750, 486, 483, 411, 257, 2531, 1874, 309, 486, 406, 1009, 312, 2182,
  293, 2418, 365, 2099, 21138, 5231, 293, 437, 466, 264, 3430, 295, 264, 2856, 1392,
  370, 498, 527, 3669, 307, 406, 370, 869, 293, 750, 576, 411, 281, 8110, 746, 13,
  51814], "temperature": 0.0, "avg_logprob": -0.12148785591125488, "compression_ratio":
  1.7813953488372094, "no_speech_prob": 0.04090399667620659}, {"id": 155, "seek":
  196972, "start": 1969.72, "end": 1999.68, "text": " An Amazon eBay or any other
  e-commerce so the challenge of language so essentially vector search is breaking
  the barrier of the language and the the barrier of understanding what is your what
  is your question or what is your query so I think that in terms of you know and
  there''s a broad discussion about it democratizing AI what is the added value of.",
  "tokens": [50364, 1107, 6795, 33803, 420, 604, 661, 308, 12, 26926, 370, 264, 3430,
  295, 2856, 370, 4476, 8062, 3164, 307, 7697, 264, 13357, 295, 264, 2856, 293, 264,
  264, 13357, 295, 3701, 437, 307, 428, 437, 307, 428, 1168, 420, 437, 307, 428, 14581,
  370, 286, 519, 300, 294, 2115, 295, 291, 458, 293, 456, 311, 257, 4152, 5017, 466,
  309, 37221, 3319, 7318, 437, 307, 264, 3869, 2158, 295, 13, 51862], "temperature":
  0.0, "avg_logprob": -0.1465297333181721, "compression_ratio": 1.7170731707317073,
  "no_speech_prob": 0.037404220551252365}, {"id": 156, "seek": 199972, "start": 1999.72,
  "end": 2027.04, "text": " AI so you know you have like autonomous cars and this
  is great but you know breaking barriers the language barrier with the multilingual
  model and and some other cool stuff this is this is I think something that is doing
  really good for the ecosystem and for consumer and the people that you know they
  have like a barrier of a language so.", "tokens": [50364, 7318, 370, 291, 458, 291,
  362, 411, 23797, 5163, 293, 341, 307, 869, 457, 291, 458, 7697, 13565, 264, 2856,
  13357, 365, 264, 2120, 38219, 2316, 293, 293, 512, 661, 1627, 1507, 341, 307, 341,
  307, 286, 519, 746, 300, 307, 884, 534, 665, 337, 264, 11311, 293, 337, 9711, 293,
  264, 561, 300, 291, 458, 436, 362, 411, 257, 13357, 295, 257, 2856, 370, 13, 51730],
  "temperature": 0.0, "avg_logprob": -0.153001526423863, "compression_ratio": 1.774869109947644,
  "no_speech_prob": 0.06908848136663437}, {"id": 157, "seek": 202704, "start": 2027.96,
  "end": 2047.76, "text": " This is a great example what is the added value of vector
  search yeah I agree I mean all of the examples that you brought up you know if you
  if you look at how you would tackle I don''t know like red short sleeve dress with
  the more traditional approach I guess you will need to build some kind of.", "tokens":
  [50410, 639, 307, 257, 869, 1365, 437, 307, 264, 3869, 2158, 295, 8062, 3164, 1338,
  286, 3986, 286, 914, 439, 295, 264, 5110, 300, 291, 3038, 493, 291, 458, 498, 291,
  498, 291, 574, 412, 577, 291, 576, 14896, 286, 500, 380, 458, 411, 2182, 2099, 21138,
  5231, 365, 264, 544, 5164, 3109, 286, 2041, 291, 486, 643, 281, 1322, 512, 733,
  295, 13, 51400], "temperature": 0.0, "avg_logprob": -0.13978313332173362, "compression_ratio":
  1.5549738219895288, "no_speech_prob": 0.024568524211645126}, {"id": 158, "seek":
  204776, "start": 2047.76, "end": 2068.76, "text": " Query understanding system but
  even then like even if after you''ve built it let''s say you you will run filters
  on your data right but that that also means you do need to have the filters but
  but if you don''t have them if you don''t have the values in those fields in your
  documents right so what if you want you have like and this is by the way not.",
  "tokens": [50364, 2326, 2109, 3701, 1185, 457, 754, 550, 411, 754, 498, 934, 291,
  600, 3094, 309, 718, 311, 584, 291, 291, 486, 1190, 15995, 322, 428, 1412, 558,
  457, 300, 300, 611, 1355, 291, 360, 643, 281, 362, 264, 15995, 457, 457, 498, 291,
  500, 380, 362, 552, 498, 291, 500, 380, 362, 264, 4190, 294, 729, 7909, 294, 428,
  8512, 558, 370, 437, 498, 291, 528, 291, 362, 411, 293, 341, 307, 538, 264, 636,
  406, 13, 51414], "temperature": 0.0, "avg_logprob": -0.21288911795910495, "compression_ratio":
  1.8031088082901554, "no_speech_prob": 0.04797352850437164}, {"id": 159, "seek":
  206876, "start": 2068.76, "end": 2094.92, "text": " It''s very unusual like I used
  to see I used to oversee a project in e-commerce space where we would get data from
  new providers all the time right so one of the issues was to map them back to our
  ontology but at the same time they would they would miss a lot of like field values
  right so what would you put there so they give you some description and then they
  give you the image on a set of images.", "tokens": [50364, 467, 311, 588, 10901,
  411, 286, 1143, 281, 536, 286, 1143, 281, 46543, 257, 1716, 294, 308, 12, 26926,
  1901, 689, 321, 576, 483, 1412, 490, 777, 11330, 439, 264, 565, 558, 370, 472, 295,
  264, 2663, 390, 281, 4471, 552, 646, 281, 527, 6592, 1793, 457, 412, 264, 912, 565,
  436, 576, 436, 576, 1713, 257, 688, 295, 411, 2519, 4190, 558, 370, 437, 576, 291,
  829, 456, 370, 436, 976, 291, 512, 3855, 293, 550, 436, 976, 291, 264, 3256, 322,
  257, 992, 295, 5267, 13, 51672], "temperature": 0.0, "avg_logprob": -0.19501097305961276,
  "compression_ratio": 1.7621145374449338, "no_speech_prob": 0.3938063681125641},
  {"id": 160, "seek": 209492, "start": 2095.32, "end": 2108.2400000000002, "text":
  " So like with with conventional not conventional but like more traditional approach
  of search right keyword search you''re kind of like stuck right what would you do
  there and I guess of course people do solve it in some way but.", "tokens": [50384,
  407, 411, 365, 365, 16011, 406, 16011, 457, 411, 544, 5164, 3109, 295, 3164, 558,
  20428, 3164, 291, 434, 733, 295, 411, 5541, 558, 437, 576, 291, 360, 456, 293, 286,
  2041, 295, 1164, 561, 360, 5039, 309, 294, 512, 636, 457, 13, 51030], "temperature":
  0.0, "avg_logprob": -0.18719393412272137, "compression_ratio": 1.6473988439306357,
  "no_speech_prob": 0.020178183913230896}, {"id": 161, "seek": 209492, "start": 2108.8,
  "end": 2112.7200000000003, "text": " Instead you could just apply vector search
  right and and.", "tokens": [51058, 7156, 291, 727, 445, 3079, 8062, 3164, 558, 293,
  293, 13, 51254], "temperature": 0.0, "avg_logprob": -0.18719393412272137, "compression_ratio":
  1.6473988439306357, "no_speech_prob": 0.020178183913230896}, {"id": 162, "seek":
  211272, "start": 2113.64, "end": 2127.56, "text": " Even though I say just there
  is still some challenge for example with model fine tuning and things like that
  can you talk a bit more to this maybe new challenges that this field opens of course
  it gives us.", "tokens": [50410, 2754, 1673, 286, 584, 445, 456, 307, 920, 512,
  3430, 337, 1365, 365, 2316, 2489, 15164, 293, 721, 411, 300, 393, 291, 751, 257,
  857, 544, 281, 341, 1310, 777, 4759, 300, 341, 2519, 9870, 295, 1164, 309, 2709,
  505, 13, 51106], "temperature": 0.0, "avg_logprob": -0.11314863628811306, "compression_ratio":
  1.4405594405594406, "no_speech_prob": 0.0452168732881546}, {"id": 163, "seek": 212756,
  "start": 2128.16, "end": 2145.2, "text": " opportunities it gives us advantages
  it solves some you know painstaking issues that we had before but what do we need
  to focus on going forward then once we deploy such systems beyond only hardware
  part but also like on this algorithm side.", "tokens": [50394, 4786, 309, 2709,
  505, 14906, 309, 39890, 512, 291, 458, 1822, 372, 2456, 2663, 300, 321, 632, 949,
  457, 437, 360, 321, 643, 281, 1879, 322, 516, 2128, 550, 1564, 321, 7274, 1270,
  3652, 4399, 787, 8837, 644, 457, 611, 411, 322, 341, 9284, 1252, 13, 51246], "temperature":
  0.0, "avg_logprob": -0.3053676986694336, "compression_ratio": 1.4968944099378882,
  "no_speech_prob": 0.05416077747941017}, {"id": 164, "seek": 214520, "start": 2146.16,
  "end": 2171.2799999999997, "text": " Yeah you know this is this is a great question
  because it resonates with one of your blog post recent blog post where you published
  the Google''s research about e-commerce companies in the US losing 300 billion dollars
  due to search abandonment in the US only.", "tokens": [50412, 865, 291, 458, 341,
  307, 341, 307, 257, 869, 1168, 570, 309, 41051, 365, 472, 295, 428, 6968, 2183,
  5162, 6968, 2183, 689, 291, 6572, 264, 3329, 311, 2132, 466, 308, 12, 26926, 3431,
  294, 264, 2546, 7027, 6641, 5218, 3808, 3462, 281, 3164, 9072, 518, 294, 264, 2546,
  787, 13, 51668], "temperature": 0.0, "avg_logprob": -0.2387984882701527, "compression_ratio":
  1.48, "no_speech_prob": 0.08114374428987503}, {"id": 165, "seek": 217128, "start":
  2172.0400000000004, "end": 2196.84, "text": " And again this is crazy number because
  if you have like I would like to buy a green polo shirt and I really want to buy
  a green polo shirt and the e-commerce got this green polo shirt inside in the in
  the warehouse or in the inventory and they can find the match we can find the match
  for this for this challenge.", "tokens": [50402, 400, 797, 341, 307, 3219, 1230,
  570, 498, 291, 362, 411, 286, 576, 411, 281, 2256, 257, 3092, 1180, 78, 8336, 293,
  286, 534, 528, 281, 2256, 257, 3092, 1180, 78, 8336, 293, 264, 308, 12, 26926, 658,
  341, 3092, 1180, 78, 8336, 1854, 294, 264, 294, 264, 22244, 420, 294, 264, 14228,
  293, 436, 393, 915, 264, 2995, 321, 393, 915, 264, 2995, 337, 341, 337, 341, 3430,
  13, 51642], "temperature": 0.0, "avg_logprob": -0.22432667500263936, "compression_ratio":
  1.8520710059171597, "no_speech_prob": 0.04939769208431244}, {"id": 166, "seek":
  219684, "start": 2197.84, "end": 2219.56, "text": " This is this is the you challenge
  but in terms of of and again this is just one one example but you know our mission
  is to back to break this barrier for for developers it''s not only e-commerce so
  expanding it to searching blocks okay if you would like to find.", "tokens": [50414,
  639, 307, 341, 307, 264, 291, 3430, 457, 294, 2115, 295, 295, 293, 797, 341, 307,
  445, 472, 472, 1365, 457, 291, 458, 527, 4447, 307, 281, 646, 281, 1821, 341, 13357,
  337, 337, 8849, 309, 311, 406, 787, 308, 12, 26926, 370, 14702, 309, 281, 10808,
  8474, 1392, 498, 291, 576, 411, 281, 915, 13, 51500], "temperature": 0.0, "avg_logprob":
  -0.2289884090423584, "compression_ratio": 1.5535714285714286, "no_speech_prob":
  0.0221580658107996}, {"id": 167, "seek": 221956, "start": 2220.52, "end": 2245.72,
  "text": " And anomaly or you would like to understand what is the root cause when
  you''re and you have like a software system logs and you would like to to understand
  and to find some anomalies or even fintech e-commerce and other areas I think that
  there''s some cool stuff over there so one one way.", "tokens": [50412, 400, 42737,
  420, 291, 576, 411, 281, 1223, 437, 307, 264, 5593, 3082, 562, 291, 434, 293, 291,
  362, 411, 257, 4722, 1185, 20820, 293, 291, 576, 411, 281, 281, 1223, 293, 281,
  915, 512, 24769, 48872, 420, 754, 283, 686, 5023, 308, 12, 26926, 293, 661, 3179,
  286, 519, 300, 456, 311, 512, 1627, 1507, 670, 456, 370, 472, 472, 636, 13, 51672],
  "temperature": 0.0, "avg_logprob": -0.17895628801032679, "compression_ratio": 1.670520231213873,
  "no_speech_prob": 0.06978459656238556}, {"id": 168, "seek": 224572, "start": 2246.2799999999997,
  "end": 2270.68, "text": " And you know to move forward is if you would like to use
  let''s take for instance Siri I would like to buy with your audio right I would
  like to buy a red and white short sleeve dress below 100 dollar.", "tokens": [50392,
  400, 291, 458, 281, 1286, 2128, 307, 498, 291, 576, 411, 281, 764, 718, 311, 747,
  337, 5197, 33682, 286, 576, 411, 281, 2256, 365, 428, 6278, 558, 286, 576, 411,
  281, 2256, 257, 2182, 293, 2418, 2099, 21138, 5231, 2507, 2319, 7241, 13, 51612],
  "temperature": 0.0, "avg_logprob": -0.23003037770589194, "compression_ratio": 1.5037593984962405,
  "no_speech_prob": 0.06288184970617294}, {"id": 169, "seek": 227068, "start": 2270.68,
  "end": 2298.72, "text": " Okay so you can this is a simple thing for you know consumers
  but you know technology wise this is the you challenge so the first challenge is
  to convert the audio to text and today there''s you know you can convert it directly
  to vectors and then you can run this query but again you need to filter because
  if you want.", "tokens": [50412, 1033, 370, 291, 393, 341, 307, 257, 2199, 551,
  337, 291, 458, 11883, 457, 291, 458, 2899, 10829, 341, 307, 264, 291, 3430, 370,
  264, 700, 3430, 307, 281, 7620, 264, 6278, 281, 2487, 293, 965, 456, 311, 291, 458,
  291, 393, 7620, 309, 3838, 281, 18875, 293, 550, 291, 393, 1190, 341, 14581, 457,
  797, 291, 643, 281, 6608, 570, 498, 291, 528, 13, 51766], "temperature": 0.0, "avg_logprob":
  -0.1768792797537411, "compression_ratio": 1.7722222222222221, "no_speech_prob":
  0.03726491704583168}, {"id": 170, "seek": 230068, "start": 2300.68, "end": 2330.6,
  "text": " Something that is below 100 so usually it''s the price field so I think
  this is the biggest challenge that the consumers or people can communicate in a
  natural way with the computer with audio and say it very simple without you know
  trying to to run a complicated SQL queries etc so I think this is the like the the
  holy grail of of the audio.", "tokens": [50364, 6595, 300, 307, 2507, 2319, 370,
  2673, 309, 311, 264, 3218, 2519, 370, 286, 519, 341, 307, 264, 3880, 3430, 300,
  264, 11883, 420, 561, 393, 7890, 294, 257, 3303, 636, 365, 264, 3820, 365, 6278,
  293, 584, 309, 588, 2199, 1553, 291, 458, 1382, 281, 281, 1190, 257, 6179, 19200,
  24109, 5183, 370, 286, 519, 341, 307, 264, 411, 264, 264, 10622, 1295, 388, 295,
  295, 264, 6278, 13, 51860], "temperature": 0.0, "avg_logprob": -0.32119361668416896,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.019489077851176262},
  {"id": 171, "seek": 233068, "start": 2330.68, "end": 2356.44, "text": " Machine
  learning to process this query and give you like the example and when you are purchase
  when you would like to purchase it on a certain website it will give you the place
  order page and you will get all of the details you will see the type of the dress
  and it will give you the right result and it will be below 100.", "tokens": [50364,
  22155, 2539, 281, 1399, 341, 14581, 293, 976, 291, 411, 264, 1365, 293, 562, 291,
  366, 8110, 562, 291, 576, 411, 281, 8110, 309, 322, 257, 1629, 3144, 309, 486, 976,
  291, 264, 1081, 1668, 3028, 293, 291, 486, 483, 439, 295, 264, 4365, 291, 486, 536,
  264, 2010, 295, 264, 5231, 293, 309, 486, 976, 291, 264, 558, 1874, 293, 309, 486,
  312, 2507, 2319, 13, 51652], "temperature": 0.0, "avg_logprob": -0.18584509298835003,
  "compression_ratio": 1.8352272727272727, "no_speech_prob": 0.011681396514177322},
  {"id": 172, "seek": 235644, "start": 2356.44, "end": 2369.32, "text": " The 100
  dollar and I think this is the way or this is a direction that we we can move forward
  with this technology.", "tokens": [50364, 440, 2319, 7241, 293, 286, 519, 341, 307,
  264, 636, 420, 341, 307, 257, 3513, 300, 321, 321, 393, 1286, 2128, 365, 341, 2899,
  13, 51008], "temperature": 0.0, "avg_logprob": -0.2316394962676584, "compression_ratio":
  1.603864734299517, "no_speech_prob": 0.18350249528884888}, {"id": 173, "seek": 235644,
  "start": 2370.12, "end": 2386.36, "text": " Yeah yeah that sounds great so in principle
  like so so that our listeners that present a new one will understand is that vector
  search really opens doors to new types of data right new modalities as they say
  so like.", "tokens": [51048, 865, 1338, 300, 3263, 869, 370, 294, 8665, 411, 370,
  370, 300, 527, 23274, 300, 1974, 257, 777, 472, 486, 1223, 307, 300, 8062, 3164,
  534, 9870, 8077, 281, 777, 3467, 295, 1412, 558, 777, 1072, 16110, 382, 436, 584,
  370, 411, 13, 51860], "temperature": 0.0, "avg_logprob": -0.2316394962676584, "compression_ratio":
  1.603864734299517, "no_speech_prob": 0.18350249528884888}, {"id": 174, "seek": 238644,
  "start": 2386.44, "end": 2416.2000000000003, "text": " Previously it was maybe only
  text modality even if you saw pictures on the on the monitor or on your phone as
  you know as response to your query it doesn''t necessarily mean that that query
  really was kind of grasping the best parts of that image like it would actually
  understand what what is in the image but with vector search you can also implement
  that and for example using clip model or some other model where you can.", "tokens":
  [50364, 33606, 309, 390, 1310, 787, 2487, 1072, 1860, 754, 498, 291, 1866, 5242,
  322, 264, 322, 264, 6002, 420, 322, 428, 2593, 382, 291, 458, 382, 4134, 281, 428,
  14581, 309, 1177, 380, 4725, 914, 300, 300, 14581, 534, 390, 733, 295, 29444, 3381,
  264, 1151, 3166, 295, 300, 3256, 411, 309, 576, 767, 1223, 437, 437, 307, 294, 264,
  3256, 457, 365, 8062, 3164, 291, 393, 611, 4445, 300, 293, 337, 1365, 1228, 7353,
  2316, 420, 512, 661, 2316, 689, 291, 393, 13, 51852], "temperature": 0.0, "avg_logprob":
  -0.1135278679858679, "compression_ratio": 1.7306122448979593, "no_speech_prob":
  0.022312765941023827}, {"id": 175, "seek": 241644, "start": 2417.4, "end": 2418.04,
  "text": " Really.", "tokens": [50412, 4083, 13, 50444], "temperature": 0.0, "avg_logprob":
  -0.2591490396639196, "compression_ratio": 1.6682692307692308, "no_speech_prob":
  0.008501578122377396}, {"id": 176, "seek": 241644, "start": 2419.32, "end": 2436.6,
  "text": " Infer meaning from that picture right and what you are saying is that
  in the future and maybe this is to some extent happening already is that we can
  also cross modalities between voice and text right so like what I''m saying it can
  it can represent as a vector and then.", "tokens": [50508, 682, 612, 3620, 490,
  300, 3036, 558, 293, 437, 291, 366, 1566, 307, 300, 294, 264, 2027, 293, 1310, 341,
  307, 281, 512, 8396, 2737, 1217, 307, 300, 321, 393, 611, 3278, 1072, 16110, 1296,
  3177, 293, 2487, 558, 370, 411, 437, 286, 478, 1566, 309, 393, 309, 393, 2906, 382,
  257, 8062, 293, 550, 13, 51372], "temperature": 0.0, "avg_logprob": -0.2591490396639196,
  "compression_ratio": 1.6682692307692308, "no_speech_prob": 0.008501578122377396},
  {"id": 177, "seek": 241644, "start": 2437.48, "end": 2442.84, "text": " Find an
  image or find a video right it''s like a lot of applications.", "tokens": [51416,
  11809, 364, 3256, 420, 915, 257, 960, 558, 309, 311, 411, 257, 688, 295, 5821, 13,
  51684], "temperature": 0.0, "avg_logprob": -0.2591490396639196, "compression_ratio":
  1.6682692307692308, "no_speech_prob": 0.008501578122377396}, {"id": 178, "seek":
  244284, "start": 2442.84, "end": 2471.88, "text": " Yeah yeah yeah totally yeah
  exactly and you know if you are working with your Instagram and you found like a
  nice celeb that is wearing a nice dress and you would like to buy something that
  is similar so with image search you can find like a similar and find me the find
  me this dress or the most relevant dress or the most the closest dress the.", "tokens":
  [50372, 865, 1338, 1338, 3879, 1338, 2293, 293, 291, 458, 498, 291, 366, 1364, 365,
  428, 5281, 293, 291, 1352, 411, 257, 1481, 1769, 28512, 300, 307, 4769, 257, 1481,
  5231, 293, 291, 576, 411, 281, 2256, 746, 300, 307, 2531, 370, 365, 3256, 3164,
  291, 393, 915, 411, 257, 2531, 293, 915, 385, 264, 915, 385, 341, 5231, 420, 264,
  881, 7340, 5231, 420, 264, 881, 264, 13699, 5231, 264, 13, 51816], "temperature":
  0.0, "avg_logprob": -0.2532351983560098, "compression_ratio": 1.8804347826086956,
  "no_speech_prob": 0.0316493846476078}, {"id": 179, "seek": 247284, "start": 2472.84,
  "end": 2487.1600000000003, "text": " Closes example of this dress and yeah yeah
  there are various options you know this is just one example you know of how to monetize
  Instagram or a tick talk where you know consumers can.", "tokens": [50364, 2033,
  4201, 1365, 295, 341, 5231, 293, 1338, 1338, 456, 366, 3683, 3956, 291, 458, 341,
  307, 445, 472, 1365, 291, 458, 295, 577, 281, 15556, 1125, 5281, 420, 257, 5204,
  751, 689, 291, 458, 11883, 393, 13, 51080], "temperature": 0.0, "avg_logprob": -0.4102802276611328,
  "compression_ratio": 1.4785714285714286, "no_speech_prob": 0.010825091041624546},
  {"id": 180, "seek": 247284, "start": 2488.2000000000003, "end": 2490.52, "text":
  " Watch their favorite.", "tokens": [51132, 7277, 641, 2954, 13, 51248], "temperature":
  0.0, "avg_logprob": -0.4102802276611328, "compression_ratio": 1.4785714285714286,
  "no_speech_prob": 0.010825091041624546}, {"id": 181, "seek": 249052, "start": 2490.52,
  "end": 2491.56, "text": " them.", "tokens": [50364, 552, 13, 50416], "temperature":
  0.0, "avg_logprob": -0.3449482295824134, "compression_ratio": 1.7577092511013215,
  "no_speech_prob": 0.07154249399900436}, {"id": 182, "seek": 249052, "start": 2492.2,
  "end": 2508.36, "text": " The celeb that they are following and if they were seeing
  something this is great so I want to purchase it and in terms of monetization and
  in terms of the added value of the customer take take this you take this platform
  says that.", "tokens": [50448, 440, 1769, 28512, 300, 436, 366, 3480, 293, 498,
  436, 645, 2577, 746, 341, 307, 869, 370, 286, 528, 281, 8110, 309, 293, 294, 2115,
  295, 15556, 2144, 293, 294, 2115, 295, 264, 3869, 2158, 295, 264, 5474, 747, 747,
  341, 291, 747, 341, 3663, 1619, 300, 13, 51256], "temperature": 0.0, "avg_logprob":
  -0.3449482295824134, "compression_ratio": 1.7577092511013215, "no_speech_prob":
  0.07154249399900436}, {"id": 183, "seek": 249052, "start": 2510.2, "end": 2520.44,
  "text": " Any commerce platform okay this is like a fresh concept but this is ways
  this is a way for companies to monetize the platform it''s not a social media it
  can be.", "tokens": [51348, 2639, 26320, 3663, 1392, 341, 307, 411, 257, 4451, 3410,
  457, 341, 307, 2098, 341, 307, 257, 636, 337, 3431, 281, 15556, 1125, 264, 3663,
  309, 311, 406, 257, 2093, 3021, 309, 393, 312, 13, 51860], "temperature": 0.0, "avg_logprob":
  -0.3449482295824134, "compression_ratio": 1.7577092511013215, "no_speech_prob":
  0.07154249399900436}, {"id": 184, "seek": 252052, "start": 2520.52, "end": 2528.6,
  "text": " e-commerce and it can be super simple because you know up until now they
  they''ve seen like a nice dress or a nice.", "tokens": [50364, 308, 12, 26926, 293,
  309, 393, 312, 1687, 2199, 570, 291, 458, 493, 1826, 586, 436, 436, 600, 1612, 411,
  257, 1481, 5231, 420, 257, 1481, 13, 50768], "temperature": 0.0, "avg_logprob":
  -0.2727415385999178, "compression_ratio": 1.7136752136752136, "no_speech_prob":
  0.006026688031852245}, {"id": 185, "seek": 252052, "start": 2529.88, "end": 2538.04,
  "text": " A shirt but they cannot do with it they cannot purchase it they don''t
  know how to explain to the machine or the computer.", "tokens": [50832, 316, 8336,
  457, 436, 2644, 360, 365, 309, 436, 2644, 8110, 309, 436, 500, 380, 458, 577, 281,
  2903, 281, 264, 3479, 420, 264, 3820, 13, 51240], "temperature": 0.0, "avg_logprob":
  -0.2727415385999178, "compression_ratio": 1.7136752136752136, "no_speech_prob":
  0.006026688031852245}, {"id": 186, "seek": 252052, "start": 2539.8, "end": 2550.44,
  "text": " What what is the type of the of the clothing that they would like to buy
  so yeah that there are various options and yeah i''m eager to see what are the applications.",
  "tokens": [51328, 708, 437, 307, 264, 2010, 295, 264, 295, 264, 11502, 300, 436,
  576, 411, 281, 2256, 370, 1338, 300, 456, 366, 3683, 3956, 293, 1338, 741, 478,
  18259, 281, 536, 437, 366, 264, 5821, 13, 51860], "temperature": 0.0, "avg_logprob":
  -0.2727415385999178, "compression_ratio": 1.7136752136752136, "no_speech_prob":
  0.006026688031852245}, {"id": 187, "seek": 255052, "start": 2550.52, "end": 2556.6,
  "text": " That you know developers and the entrepreneurs will develop with this
  technology.", "tokens": [50364, 663, 291, 458, 8849, 293, 264, 12639, 486, 1499,
  365, 341, 2899, 13, 50668], "temperature": 0.0, "avg_logprob": -0.2868285993250405,
  "compression_ratio": 1.5916666666666666, "no_speech_prob": 0.006189994513988495},
  {"id": 188, "seek": 255052, "start": 2557.48, "end": 2567.88, "text": " Yeah that
  sounds great one of the apps that you just kind of reminded me of is I think it
  was James Briggs who built the kind of simple demo.", "tokens": [50712, 865, 300,
  3263, 869, 472, 295, 264, 7733, 300, 291, 445, 733, 295, 15920, 385, 295, 307, 286,
  519, 309, 390, 5678, 1603, 32555, 567, 3094, 264, 733, 295, 2199, 10723, 13, 51232],
  "temperature": 0.0, "avg_logprob": -0.2868285993250405, "compression_ratio": 1.5916666666666666,
  "no_speech_prob": 0.006189994513988495}, {"id": 189, "seek": 255052, "start": 2568.68,
  "end": 2580.44, "text": " Using the recent model called whisper from open AI so
  you can actually you know like on YouTube today how you find things is basically
  mostly based on titles.", "tokens": [51272, 11142, 264, 5162, 2316, 1219, 26018,
  490, 1269, 7318, 370, 291, 393, 767, 291, 458, 411, 322, 3088, 965, 577, 291, 915,
  721, 307, 1936, 5240, 2361, 322, 12992, 13, 51860], "temperature": 0.0, "avg_logprob":
  -0.2868285993250405, "compression_ratio": 1.5916666666666666, "no_speech_prob":
  0.006189994513988495}, {"id": 190, "seek": 258052, "start": 2580.52, "end": 2582.68,
  "text": " I believe this is what people type.", "tokens": [50364, 286, 1697, 341,
  307, 437, 561, 2010, 13, 50472], "temperature": 0.0, "avg_logprob": -0.27641512552897135,
  "compression_ratio": 1.588235294117647, "no_speech_prob": 0.012654316611588001},
  {"id": 191, "seek": 258052, "start": 2583.96, "end": 2603.0, "text": " But then
  he built a demo where he can land in the precise time code which contains the answer
  to your question you know that could be really interesting like it just to think
  about it at the unlocks even more what you said in the beginning like we have this
  is a device of data and so on.", "tokens": [50536, 583, 550, 415, 3094, 257, 10723,
  689, 415, 393, 2117, 294, 264, 13600, 565, 3089, 597, 8306, 264, 1867, 281, 428,
  1168, 291, 458, 300, 727, 312, 534, 1880, 411, 309, 445, 281, 519, 466, 309, 412,
  264, 517, 34896, 754, 544, 437, 291, 848, 294, 264, 2863, 411, 321, 362, 341, 307,
  257, 4302, 295, 1412, 293, 370, 322, 13, 51488], "temperature": 0.0, "avg_logprob":
  -0.27641512552897135, "compression_ratio": 1.588235294117647, "no_speech_prob":
  0.012654316611588001}, {"id": 192, "seek": 260300, "start": 2603.56, "end": 2612.12,
  "text": " But like we are not able to unlock the data right it''s just sitting there
  waiting to be discovered so to say.", "tokens": [50392, 583, 411, 321, 366, 406,
  1075, 281, 11634, 264, 1412, 558, 309, 311, 445, 3798, 456, 3806, 281, 312, 6941,
  370, 281, 584, 13, 50820], "temperature": 0.0, "avg_logprob": -0.14792193375624618,
  "compression_ratio": 1.5728155339805825, "no_speech_prob": 0.020676447078585625},
  {"id": 193, "seek": 260300, "start": 2613.56, "end": 2630.04, "text": " Yeah it''s
  really cool I wanted to spend a bit of time on the search topic itself so you did
  mention this search abandonment issue which is like an e-commerce but but in general
  if we if we think about search field.", "tokens": [50892, 865, 309, 311, 534, 1627,
  286, 1415, 281, 3496, 257, 857, 295, 565, 322, 264, 3164, 4829, 2564, 370, 291,
  630, 2152, 341, 3164, 9072, 518, 2734, 597, 307, 411, 364, 308, 12, 26926, 457,
  457, 294, 2674, 498, 321, 498, 321, 519, 466, 3164, 2519, 13, 51716], "temperature":
  0.0, "avg_logprob": -0.14792193375624618, "compression_ratio": 1.5728155339805825,
  "no_speech_prob": 0.020676447078585625}, {"id": 194, "seek": 263004, "start": 2630.04,
  "end": 2659.88, "text": " On a much larger scale and I think Daniel tanky-lank also
  said about it that when search engine doesn''t work you are blamed but when it does
  work you don''t hear anything it''s like people take it for granted it''s kind of
  like water from the tap I guess right if it''s the right analogy so what do you
  think of the search field in general like where do you think vector search field
  fits in and what''s the role of this hybrid.", "tokens": [50412, 1282, 257, 709,
  4833, 4373, 293, 286, 519, 8033, 5466, 88, 12, 75, 657, 611, 848, 466, 309, 300,
  562, 3164, 2848, 1177, 380, 589, 291, 366, 32027, 457, 562, 309, 775, 589, 291,
  500, 380, 1568, 1340, 309, 311, 411, 561, 747, 309, 337, 12344, 309, 311, 733, 295,
  411, 1281, 490, 264, 5119, 286, 2041, 558, 498, 309, 311, 264, 558, 21663, 370,
  437, 360, 291, 519, 295, 264, 3164, 2519, 294, 2674, 411, 689, 360, 291, 519, 8062,
  3164, 2519, 9001, 294, 293, 437, 311, 264, 3090, 295, 341, 13051, 13, 51856], "temperature":
  0.0, "avg_logprob": -0.20772019612420464, "compression_ratio": 1.726530612244898,
  "no_speech_prob": 0.03149003908038139}, {"id": 195, "seek": 266004, "start": 2660.04,
  "end": 2674.36, "text": " Approach where you have this keywords versus which are
  more familiar to users versus vector search so where would you take this yourself
  right as a product manager having unlimited resources where would you where would
  you go.", "tokens": [50364, 29551, 608, 689, 291, 362, 341, 21009, 5717, 597, 366,
  544, 4963, 281, 5022, 5717, 8062, 3164, 370, 689, 576, 291, 747, 341, 1803, 558,
  382, 257, 1674, 6598, 1419, 21950, 3593, 689, 576, 291, 689, 576, 291, 352, 13,
  51080], "temperature": 0.0, "avg_logprob": -0.2025515428229944, "compression_ratio":
  1.703125, "no_speech_prob": 0.007938697934150696}, {"id": 196, "seek": 266004, "start":
  2675.64, "end": 2686.36, "text": " Yeah this is this is an interesting question
  yeah so I think that search is still an unsold problem.", "tokens": [51144, 865,
  341, 307, 341, 307, 364, 1880, 1168, 1338, 370, 286, 519, 300, 3164, 307, 920, 364,
  517, 45537, 1154, 13, 51680], "temperature": 0.0, "avg_logprob": -0.2025515428229944,
  "compression_ratio": 1.703125, "no_speech_prob": 0.007938697934150696}, {"id": 197,
  "seek": 268636, "start": 2686.36, "end": 2715.96, "text": " And you know in order
  to find the right object or the right the the most accurate type of data we are
  still we have a lot of work to develop this ecosystem and you know to build the
  multimodals and multilingual and I think that the big tech companies are doing some
  great job with this.", "tokens": [50412, 400, 291, 458, 294, 1668, 281, 915, 264,
  558, 2657, 420, 264, 558, 264, 264, 881, 8559, 2010, 295, 1412, 321, 366, 920, 321,
  362, 257, 688, 295, 589, 281, 1499, 341, 11311, 293, 291, 458, 281, 1322, 264, 32972,
  378, 1124, 293, 2120, 38219, 293, 286, 519, 300, 264, 955, 7553, 3431, 366, 884,
  512, 869, 1691, 365, 341, 13, 51844], "temperature": 0.0, "avg_logprob": -0.19534264504909515,
  "compression_ratio": 1.6067415730337078, "no_speech_prob": 0.042302731424570084},
  {"id": 198, "seek": 271636, "start": 2716.36, "end": 2741.1600000000003, "text":
  " With this stuff like open and I and the other folks and hybrid searches is is
  a is a very interesting concept I believe that we for some applications it can be
  a good a good way to solve their challenges but I think that the one of the most
  important.", "tokens": [50364, 2022, 341, 1507, 411, 1269, 293, 286, 293, 264, 661,
  4024, 293, 13051, 26701, 307, 307, 257, 307, 257, 588, 1880, 3410, 286, 1697, 300,
  321, 337, 512, 5821, 309, 393, 312, 257, 665, 257, 665, 636, 281, 5039, 641, 4759,
  457, 286, 519, 300, 264, 472, 295, 264, 881, 1021, 13, 51604], "temperature": 0.0,
  "avg_logprob": -0.22703027725219727, "compression_ratio": 1.539877300613497, "no_speech_prob":
  0.009138207882642746}, {"id": 199, "seek": 274116, "start": 2742.12, "end": 2749.72,
  "text": " Pilar is that you should and again I''ve learned that the data but yes
  that they are like the concept.", "tokens": [50412, 430, 2202, 307, 300, 291, 820,
  293, 797, 286, 600, 3264, 300, 264, 1412, 457, 2086, 300, 436, 366, 411, 264, 3410,
  13, 50792], "temperature": 0.0, "avg_logprob": -0.2210918468433422, "compression_ratio":
  1.8785046728971964, "no_speech_prob": 0.23245413601398468}, {"id": 200, "seek":
  274116, "start": 2751.48, "end": 2768.48, "text": " Of moving backwards from the
  custom what is I don''t have solution if we have a discussion with a customer we
  are asking what is the problem that you would like to solve and this is like you
  should be focused what what is the problem that you would like to solve like more
  than 50% of your discussion.", "tokens": [50880, 2720, 2684, 12204, 490, 264, 2375,
  437, 307, 286, 500, 380, 362, 3827, 498, 321, 362, 257, 5017, 365, 257, 5474, 321,
  366, 3365, 437, 307, 264, 1154, 300, 291, 576, 411, 281, 5039, 293, 341, 307, 411,
  291, 820, 312, 5178, 437, 437, 307, 264, 1154, 300, 291, 576, 411, 281, 5039, 411,
  544, 813, 2625, 4, 295, 428, 5017, 13, 51730], "temperature": 0.0, "avg_logprob":
  -0.2210918468433422, "compression_ratio": 1.8785046728971964, "no_speech_prob":
  0.23245413601398468}, {"id": 201, "seek": 276848, "start": 2769.2, "end": 2795.2400000000002,
  "text": " And if you don''t have a good fit it''s not a good fit if you did the
  vector search technology is not a good fit we would say it to the customer we are
  not trying you know to fit into a space that you know keyword search is a great
  solution so I think it''s the focus should be around the problem space so trying
  to figure out what is their pain point or what is their customers pain point.",
  "tokens": [50400, 400, 498, 291, 500, 380, 362, 257, 665, 3318, 309, 311, 406, 257,
  665, 3318, 498, 291, 630, 264, 8062, 3164, 2899, 307, 406, 257, 665, 3318, 321,
  576, 584, 309, 281, 264, 5474, 321, 366, 406, 1382, 291, 458, 281, 3318, 666, 257,
  1901, 300, 291, 458, 20428, 3164, 307, 257, 869, 3827, 370, 286, 519, 309, 311,
  264, 1879, 820, 312, 926, 264, 1154, 1901, 370, 1382, 281, 2573, 484, 437, 307,
  641, 1822, 935, 420, 437, 307, 641, 4581, 1822, 935, 13, 51702], "temperature":
  0.0, "avg_logprob": -0.1458975009703904, "compression_ratio": 1.8428571428571427,
  "no_speech_prob": 0.02312430925667286}, {"id": 202, "seek": 279524, "start": 2796.04,
  "end": 2821.3999999999996, "text": " Is it the accuracy for some for some applications
  we we spoke with the fraud detection company and for their use case like keyword
  search was good enough solution great so go go go ahead and we don''t want to disturb
  you so I think the focus should be around the the problem and the challenge and
  then again.", "tokens": [50404, 1119, 309, 264, 14170, 337, 512, 337, 512, 5821,
  321, 321, 7179, 365, 264, 14560, 17784, 2237, 293, 337, 641, 764, 1389, 411, 20428,
  3164, 390, 665, 1547, 3827, 869, 370, 352, 352, 352, 2286, 293, 321, 500, 380, 528,
  281, 18071, 291, 370, 286, 519, 264, 1879, 820, 312, 926, 264, 264, 1154, 293, 264,
  3430, 293, 550, 797, 13, 51672], "temperature": 0.0, "avg_logprob": -0.1825513693002554,
  "compression_ratio": 1.5989583333333333, "no_speech_prob": 0.04490693286061287},
  {"id": 203, "seek": 282140, "start": 2821.4, "end": 2849.64, "text": " Focus on
  what is the the challenge that they would like to achieve or what is the what is
  the potential of the solution and sometimes we are talking about recall is it the
  most important parameter for some of the for some of the customers and 90% is good
  enough for the use case but for mission mission critically should be mission critical
  applications.", "tokens": [50412, 21862, 322, 437, 307, 264, 264, 3430, 300, 436,
  576, 411, 281, 4584, 420, 437, 307, 264, 437, 307, 264, 3995, 295, 264, 3827, 293,
  2171, 321, 366, 1417, 466, 9901, 307, 309, 264, 881, 1021, 13075, 337, 512, 295,
  264, 337, 512, 295, 264, 4581, 293, 4289, 4, 307, 665, 1547, 337, 264, 764, 1389,
  457, 337, 4447, 4447, 22797, 820, 312, 4447, 4924, 5821, 13, 51776], "temperature":
  0.0, "avg_logprob": -0.2280451774597168, "compression_ratio": 1.77, "no_speech_prob":
  0.05462859943509102}, {"id": 204, "seek": 285140, "start": 2851.96, "end": 2863.2400000000002,
  "text": " It should be 99.99% right so I think it''s it''s a matter to some extent
  it''s it''s an issue of what is the problem and what is the KPI that you would like
  to achieve.", "tokens": [50392, 467, 820, 312, 11803, 13, 8494, 4, 558, 370, 286,
  519, 309, 311, 309, 311, 257, 1871, 281, 512, 8396, 309, 311, 309, 311, 364, 2734,
  295, 437, 307, 264, 1154, 293, 437, 307, 264, 591, 31701, 300, 291, 576, 411, 281,
  4584, 13, 50956], "temperature": 0.0, "avg_logprob": -0.12031129914887097, "compression_ratio":
  1.757847533632287, "no_speech_prob": 0.012550857849419117}, {"id": 205, "seek":
  285140, "start": 2863.92, "end": 2880.52, "text": " Would you like to optimize the
  recall great we would optimize it if you would like to reduce the infrastructure
  cost with the same KPI recall of X and you have latency of X and it''s a good enough
  and maybe it can be latency so.", "tokens": [50990, 6068, 291, 411, 281, 19719,
  264, 9901, 869, 321, 576, 19719, 309, 498, 291, 576, 411, 281, 5407, 264, 6896,
  2063, 365, 264, 912, 591, 31701, 9901, 295, 1783, 293, 291, 362, 27043, 295, 1783,
  293, 309, 311, 257, 665, 1547, 293, 1310, 309, 393, 312, 27043, 370, 13, 51820],
  "temperature": 0.0, "avg_logprob": -0.12031129914887097, "compression_ratio": 1.757847533632287,
  "no_speech_prob": 0.012550857849419117}, {"id": 206, "seek": 288140, "start": 2881.8,
  "end": 2900.84, "text": " For instance, Amazon published a research that every 100
  milliseconds let it see equals to 1% of the revenue so if the revenue is $1 billion
  then 100 milliseconds of latency equals to 10 million.", "tokens": [50384, 1171,
  5197, 11, 6795, 6572, 257, 2132, 300, 633, 2319, 34184, 718, 309, 536, 6915, 281,
  502, 4, 295, 264, 9324, 370, 498, 264, 9324, 307, 1848, 16, 5218, 550, 2319, 34184,
  295, 27043, 6915, 281, 1266, 2459, 13, 51336], "temperature": 0.0, "avg_logprob":
  -0.236592616675035, "compression_ratio": 1.5064935064935066, "no_speech_prob": 0.011023120023310184},
  {"id": 207, "seek": 288140, "start": 2901.88, "end": 2903.6800000000003, "text":
  " This is a huge impact for companies.", "tokens": [51388, 639, 307, 257, 2603,
  2712, 337, 3431, 13, 51478], "temperature": 0.0, "avg_logprob": -0.236592616675035,
  "compression_ratio": 1.5064935064935066, "no_speech_prob": 0.011023120023310184},
  {"id": 208, "seek": 290368, "start": 2904.16, "end": 2921.8399999999997, "text":
  " So I think the main the main question is what is the problem that you would like
  to solve what is the pain point and starting from the customer and then work backwards
  to find if you have like a good solution and if a solution is a is a good fit.",
  "tokens": [50388, 407, 286, 519, 264, 2135, 264, 2135, 1168, 307, 437, 307, 264,
  1154, 300, 291, 576, 411, 281, 5039, 437, 307, 264, 1822, 935, 293, 2891, 490, 264,
  5474, 293, 550, 589, 12204, 281, 915, 498, 291, 362, 411, 257, 665, 3827, 293, 498,
  257, 3827, 307, 257, 307, 257, 665, 3318, 13, 51272], "temperature": 0.0, "avg_logprob":
  -0.2868145565653956, "compression_ratio": 1.8523809523809525, "no_speech_prob":
  0.04083620756864548}, {"id": 209, "seek": 290368, "start": 2922.3199999999997, "end":
  2931.64, "text": " And again, there are various concept keyword search is a great
  solution vector search is a great solution and I read searches a good solution.",
  "tokens": [51296, 400, 797, 11, 456, 366, 3683, 3410, 20428, 3164, 307, 257, 869,
  3827, 8062, 3164, 307, 257, 869, 3827, 293, 286, 1401, 26701, 257, 665, 3827, 13,
  51762], "temperature": 0.0, "avg_logprob": -0.2868145565653956, "compression_ratio":
  1.8523809523809525, "no_speech_prob": 0.04083620756864548}, {"id": 210, "seek":
  293164, "start": 2932.44, "end": 2937.3199999999997, "text": " The the big I think
  the biggest question is what is the problem that the customer would like to solve.",
  "tokens": [50404, 440, 264, 955, 286, 519, 264, 3880, 1168, 307, 437, 307, 264,
  1154, 300, 264, 5474, 576, 411, 281, 5039, 13, 50648], "temperature": 0.0, "avg_logprob":
  -0.18510849835121468, "compression_ratio": 1.58, "no_speech_prob": 0.03003217838704586},
  {"id": 211, "seek": 293164, "start": 2937.64, "end": 2952.7999999999997, "text":
  " Yeah, I think you put it really brilliantly because it''s very easy to get into
  my new show of tweaking things like on the software side and saying I have the best
  algorithm right or I have the fastest or whatever.", "tokens": [50664, 865, 11,
  286, 519, 291, 829, 309, 534, 8695, 42580, 570, 309, 311, 588, 1858, 281, 483, 666,
  452, 777, 855, 295, 6986, 2456, 721, 411, 322, 264, 4722, 1252, 293, 1566, 286,
  362, 264, 1151, 9284, 558, 420, 286, 362, 264, 14573, 420, 2035, 13, 51422], "temperature":
  0.0, "avg_logprob": -0.18510849835121468, "compression_ratio": 1.58, "no_speech_prob":
  0.03003217838704586}, {"id": 212, "seek": 295280, "start": 2953.2000000000003, "end":
  2962.0800000000004, "text": " But then if you if you forget that I guess the most
  important dimension for your customer maybe it''s power consumption that we mentioned
  previously or something else right.", "tokens": [50384, 583, 550, 498, 291, 498,
  291, 2870, 300, 286, 2041, 264, 881, 1021, 10139, 337, 428, 5474, 1310, 309, 311,
  1347, 12126, 300, 321, 2835, 8046, 420, 746, 1646, 558, 13, 50828], "temperature":
  0.0, "avg_logprob": -0.20031770746758643, "compression_ratio": 1.6984126984126984,
  "no_speech_prob": 0.06714273244142532}, {"id": 213, "seek": 295280, "start": 2962.96,
  "end": 2964.4, "text": " But but also what you said.", "tokens": [50872, 583, 457,
  611, 437, 291, 848, 13, 50944], "temperature": 0.0, "avg_logprob": -0.20031770746758643,
  "compression_ratio": 1.6984126984126984, "no_speech_prob": 0.06714273244142532},
  {"id": 214, "seek": 295280, "start": 2966.0, "end": 2982.4, "text": " How you can
  think like the way Amazon did it right that they think big right they say okay of
  all these dollars we we earned how much actually we wasted on on you know latency
  and also how much of clients we kind of lost right.", "tokens": [51024, 1012, 291,
  393, 519, 411, 264, 636, 6795, 630, 309, 558, 300, 436, 519, 955, 558, 436, 584,
  1392, 295, 439, 613, 3808, 321, 321, 12283, 577, 709, 767, 321, 19496, 322, 322,
  291, 458, 27043, 293, 611, 577, 709, 295, 6982, 321, 733, 295, 2731, 558, 13, 51844],
  "temperature": 0.0, "avg_logprob": -0.20031770746758643, "compression_ratio": 1.6984126984126984,
  "no_speech_prob": 0.06714273244142532}, {"id": 215, "seek": 298240, "start": 2982.4,
  "end": 2996.1600000000003, "text": " Or potential clients because if if the server
  doesn''t respond soon enough then and it''s only average right 100 millisecond maybe
  for some it looks like more like closer to second including their own internet connection.",
  "tokens": [50364, 1610, 3995, 6982, 570, 498, 498, 264, 7154, 1177, 380, 4196, 2321,
  1547, 550, 293, 309, 311, 787, 4274, 558, 2319, 27940, 18882, 1310, 337, 512, 309,
  1542, 411, 544, 411, 4966, 281, 1150, 3009, 641, 1065, 4705, 4984, 13, 51052], "temperature":
  0.0, "avg_logprob": -0.2873264983460143, "compression_ratio": 1.594488188976378,
  "no_speech_prob": 0.008880238980054855}, {"id": 216, "seek": 298240, "start": 2996.7200000000003,
  "end": 3004.1600000000003, "text": " And they might just give up and say hard this
  is not working today I will go and check something else I will forget about what
  I wanted to buy.", "tokens": [51080, 400, 436, 1062, 445, 976, 493, 293, 584, 1152,
  341, 307, 406, 1364, 965, 286, 486, 352, 293, 1520, 746, 1646, 286, 486, 2870, 466,
  437, 286, 1415, 281, 2256, 13, 51452], "temperature": 0.0, "avg_logprob": -0.2873264983460143,
  "compression_ratio": 1.594488188976378, "no_speech_prob": 0.008880238980054855},
  {"id": 217, "seek": 298240, "start": 3004.4, "end": 3005.6, "text": " So right.",
  "tokens": [51464, 407, 558, 13, 51524], "temperature": 0.0, "avg_logprob": -0.2873264983460143,
  "compression_ratio": 1.594488188976378, "no_speech_prob": 0.008880238980054855},
  {"id": 218, "seek": 298240, "start": 3006.96, "end": 3008.1600000000003, "text":
  " Yeah, this is very interesting.", "tokens": [51592, 865, 11, 341, 307, 588, 1880,
  13, 51652], "temperature": 0.0, "avg_logprob": -0.2873264983460143, "compression_ratio":
  1.594488188976378, "no_speech_prob": 0.008880238980054855}, {"id": 219, "seek":
  300816, "start": 3008.72, "end": 3035.2, "text": " Also like you you you you you
  brought up some some topic behind the scenes like on the role of human in this whole
  loop I also want to pick your brain on that you know there is one direction in AI
  saying this is going to be a whole automatic thing you don''t need to do anything
  it will decide for you which is also by the way a little bit worrisome if the yeah
  it''s going to decide for everything.", "tokens": [50392, 2743, 411, 291, 291, 291,
  291, 291, 3038, 493, 512, 512, 4829, 2261, 264, 8026, 411, 322, 264, 3090, 295,
  1952, 294, 341, 1379, 6367, 286, 611, 528, 281, 1888, 428, 3567, 322, 300, 291,
  458, 456, 307, 472, 3513, 294, 7318, 1566, 341, 307, 516, 281, 312, 257, 1379, 12509,
  551, 291, 500, 380, 643, 281, 360, 1340, 309, 486, 4536, 337, 291, 597, 307, 611,
  538, 264, 636, 257, 707, 857, 469, 5714, 423, 498, 264, 1338, 309, 311, 516, 281,
  4536, 337, 1203, 13, 51716], "temperature": 0.0, "avg_logprob": -0.18203064635559751,
  "compression_ratio": 1.7723214285714286, "no_speech_prob": 0.028258956968784332},
  {"id": 220, "seek": 303520, "start": 3035.2, "end": 3064.96, "text": " But but even
  going back to earth like where do you see humans will play a role in some sense
  we are slower right then machines in some sense I think we are still faster for
  example in creating things but even they are the machines that tapping into it but
  like connected with MLOPS topics also machine learning operations and connected
  with bias and data that we collect to tell you what the real thing is.", "tokens":
  [50392, 583, 457, 754, 516, 646, 281, 4120, 411, 689, 360, 291, 536, 6255, 486,
  862, 257, 3090, 294, 512, 2020, 321, 366, 14009, 558, 550, 8379, 294, 512, 2020,
  286, 519, 321, 366, 920, 4663, 337, 1365, 294, 4084, 721, 457, 754, 436, 366, 264,
  8379, 300, 21444, 666, 309, 457, 411, 4582, 365, 21601, 46, 6273, 8378, 611, 3479,
  2539, 7705, 293, 4582, 365, 12577, 293, 1412, 300, 321, 2500, 281, 980, 291, 437,
  264, 957, 551, 307, 13, 51852], "temperature": 0.0, "avg_logprob": -0.39790858992611067,
  "compression_ratio": 1.7276595744680852, "no_speech_prob": 0.027755936607718468},
  {"id": 221, "seek": 306520, "start": 3065.2, "end": 3075.8399999999997, "text":
  " Train models or maybe some other dimension that I''m missing that you think human
  is going to play a role can you can you expand a little bit on that yeah.", "tokens":
  [50364, 28029, 5245, 420, 1310, 512, 661, 10139, 300, 286, 478, 5361, 300, 291,
  519, 1952, 307, 516, 281, 862, 257, 3090, 393, 291, 393, 291, 5268, 257, 707, 857,
  322, 300, 1338, 13, 50896], "temperature": 0.0, "avg_logprob": -0.181281694224183,
  "compression_ratio": 1.5837837837837838, "no_speech_prob": 0.00645774370059371},
  {"id": 222, "seek": 306520, "start": 3076.3199999999997, "end": 3085.04, "text":
  " So actually I wrote about it in medium about the MLOPS challenge and and the human
  in the loop and what is the place of human in the loop.", "tokens": [50920, 407,
  767, 286, 4114, 466, 309, 294, 6399, 466, 264, 21601, 46, 6273, 3430, 293, 293,
  264, 1952, 294, 264, 6367, 293, 437, 307, 264, 1081, 295, 1952, 294, 264, 6367,
  13, 51356], "temperature": 0.0, "avg_logprob": -0.181281694224183, "compression_ratio":
  1.5837837837837838, "no_speech_prob": 0.00645774370059371}, {"id": 223, "seek":
  308504, "start": 3085.04, "end": 3095.44, "text": " Essentially I believe that machine
  learning is a decision support system okay I believe that the human as.", "tokens":
  [50364, 23596, 286, 1697, 300, 3479, 2539, 307, 257, 3537, 1406, 1185, 1392, 286,
  1697, 300, 264, 1952, 382, 13, 50884], "temperature": 0.0, "avg_logprob": -0.31867987012106275,
  "compression_ratio": 1.6096256684491979, "no_speech_prob": 0.011864340864121914},
  {"id": 224, "seek": 308504, "start": 3096.16, "end": 3114.96, "text": " As a huge
  or important significant role in helping the machine to decide and where a good
  way to automate processes is to use the machine and to set a threshold okay so for
  instance if you were.", "tokens": [50920, 1018, 257, 2603, 420, 1021, 4776, 3090,
  294, 4315, 264, 3479, 281, 4536, 293, 689, 257, 665, 636, 281, 31605, 7555, 307,
  281, 764, 264, 3479, 293, 281, 992, 257, 14678, 1392, 370, 337, 5197, 498, 291,
  645, 13, 51860], "temperature": 0.0, "avg_logprob": -0.31867987012106275, "compression_ratio":
  1.6096256684491979, "no_speech_prob": 0.011864340864121914}, {"id": 225, "seek":
  311504, "start": 3115.04, "end": 3133.2799999999997, "text": " We''re talking about
  cyber cyber security challenge so you can decide that the threshold is below 0.7
  is a good enough and you don''t that like the sock teams will will check this anomaly
  and then again you are reducing.", "tokens": [50364, 492, 434, 1417, 466, 13411,
  13411, 3825, 3430, 370, 291, 393, 4536, 300, 264, 14678, 307, 2507, 1958, 13, 22,
  307, 257, 665, 1547, 293, 291, 500, 380, 300, 411, 264, 35302, 5491, 486, 486, 1520,
  341, 42737, 293, 550, 797, 291, 366, 12245, 13, 51276], "temperature": 0.0, "avg_logprob":
  -0.25792349601278497, "compression_ratio": 1.4630872483221478, "no_speech_prob":
  0.006134802475571632}, {"id": 226, "seek": 313328, "start": 3133.28, "end": 3154.2400000000002,
  "text": " The main power cost because you are automating and you are sending queries
  or a stream of data to analyze that they would you know fine tune the model and
  then you can create a learning model right so it''s a human in the loop the human
  is giving a feedback to the model and then you can.", "tokens": [50364, 440, 2135,
  1347, 2063, 570, 291, 366, 3553, 990, 293, 291, 366, 7750, 24109, 420, 257, 4309,
  295, 1412, 281, 12477, 300, 436, 576, 291, 458, 2489, 10864, 264, 2316, 293, 550,
  291, 393, 1884, 257, 2539, 2316, 558, 370, 309, 311, 257, 1952, 294, 264, 6367,
  264, 1952, 307, 2902, 257, 5824, 281, 264, 2316, 293, 550, 291, 393, 13, 51412],
  "temperature": 0.0, "avg_logprob": -0.21799991314227765, "compression_ratio": 1.6783625730994152,
  "no_speech_prob": 0.36805739998817444}, {"id": 227, "seek": 315424, "start": 3154.24,
  "end": 3164.8799999999997, "text": " Detect data drift if it''s not automated you
  know there there are solutions that are good that you know data drift etc but again.",
  "tokens": [50364, 4237, 557, 1412, 19699, 498, 309, 311, 406, 18473, 291, 458, 456,
  456, 366, 6547, 300, 366, 665, 300, 291, 458, 1412, 19699, 5183, 457, 797, 13, 50896],
  "temperature": 0.0, "avg_logprob": -0.27783331189836774, "compression_ratio": 1.6348314606741574,
  "no_speech_prob": 0.42037612199783325}, {"id": 228, "seek": 315424, "start": 3166.3999999999996,
  "end": 3182.56, "text": " My my two cents is that fully automated systems we are
  not ready yet for it and I believe that in order and then again we don''t like all
  of the anomalies will be.", "tokens": [50972, 1222, 452, 732, 14941, 307, 300, 4498,
  18473, 3652, 321, 366, 406, 1919, 1939, 337, 309, 293, 286, 1697, 300, 294, 1668,
  293, 550, 797, 321, 500, 380, 411, 439, 295, 264, 24769, 48872, 486, 312, 13, 51780],
  "temperature": 0.0, "avg_logprob": -0.27783331189836774, "compression_ratio": 1.6348314606741574,
  "no_speech_prob": 0.42037612199783325}, {"id": 229, "seek": 318256, "start": 3182.56,
  "end": 3207.12, "text": " Tested by a human again because you have the false positive
  fatigue or a lot fatigue in in the cyber domain so I believe that a combination
  or the hybrid model where you can define a certain threshold and send it to a human
  to run a sanity check and you know i''ve worked with many data scientist and.",
  "tokens": [50364, 9279, 292, 538, 257, 1952, 797, 570, 291, 362, 264, 7908, 3353,
  20574, 420, 257, 688, 20574, 294, 294, 264, 13411, 9274, 370, 286, 1697, 300, 257,
  6562, 420, 264, 13051, 2316, 689, 291, 393, 6964, 257, 1629, 14678, 293, 2845, 309,
  281, 257, 1952, 281, 1190, 257, 47892, 1520, 293, 291, 458, 741, 600, 2732, 365,
  867, 1412, 12662, 293, 13, 51592], "temperature": 0.0, "avg_logprob": -0.29117217208399915,
  "compression_ratio": 1.5625, "no_speech_prob": 0.059261504560709}, {"id": 230, "seek":
  320712, "start": 3207.12, "end": 3220.24, "text": " The the always like you know
  to improve the state of the art model and improve the f 1 score for from 99 to 99.9.",
  "tokens": [50364, 440, 264, 1009, 411, 291, 458, 281, 3470, 264, 1785, 295, 264,
  1523, 2316, 293, 3470, 264, 283, 502, 6175, 337, 490, 11803, 281, 11803, 13, 24,
  13, 51020], "temperature": 0.0, "avg_logprob": -0.2649727463722229, "compression_ratio":
  1.2282608695652173, "no_speech_prob": 0.18493223190307617}, {"id": 231, "seek":
  322024, "start": 3221.2, "end": 3242.3199999999997, "text": " But what is the the
  impact on the business is it is it important enough for the business to invest resources
  in this in this in this research or not like five data scientists are running and
  testing and optimizing the hyper parameter.", "tokens": [50412, 583, 437, 307, 264,
  264, 2712, 322, 264, 1606, 307, 309, 307, 309, 1021, 1547, 337, 264, 1606, 281,
  1963, 3593, 294, 341, 294, 341, 294, 341, 2132, 420, 406, 411, 1732, 1412, 7708,
  366, 2614, 293, 4997, 293, 40425, 264, 9848, 13075, 13, 51468], "temperature": 0.0,
  "avg_logprob": -0.2605609893798828, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.07706615328788757}, {"id": 232, "seek": 324232, "start": 3242.32, "end": 3261.92,
  "text": " For months but what is the business what is the impact on the business
  so essentially I believe that and and again it resonates with the search domain
  so I believe that companies that will be smart enough to integrate the human and
  the loop mechanism where they can find you know.", "tokens": [50364, 1171, 2493,
  457, 437, 307, 264, 1606, 437, 307, 264, 2712, 322, 264, 1606, 370, 4476, 286, 1697,
  300, 293, 293, 797, 309, 41051, 365, 264, 3164, 9274, 370, 286, 1697, 300, 3431,
  300, 486, 312, 4069, 1547, 281, 13365, 264, 1952, 293, 264, 6367, 7513, 689, 436,
  393, 915, 291, 458, 13, 51344], "temperature": 0.0, "avg_logprob": -0.25503315841942503,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.0723816305398941}, {"id":
  233, "seek": 326192, "start": 3261.92, "end": 3287.92, "text": " Measure KPIs like
  the clicks on on the on the first result how many clicks on the first result or
  any other KPIs and then if it''s a good model then great we should keep it you know
  if it''s not broken don''t touch it but if something is not working the mechanism
  or something that there''s a drift in the data so we can you know.", "tokens": [50364,
  41436, 41371, 6802, 411, 264, 18521, 322, 322, 264, 322, 264, 700, 1874, 577, 867,
  18521, 322, 264, 700, 1874, 420, 604, 661, 41371, 6802, 293, 550, 498, 309, 311,
  257, 665, 2316, 550, 869, 321, 820, 1066, 309, 291, 458, 498, 309, 311, 406, 5463,
  500, 380, 2557, 309, 457, 498, 746, 307, 406, 1364, 264, 7513, 420, 746, 300, 456,
  311, 257, 19699, 294, 264, 1412, 370, 321, 393, 291, 458, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.1777657973460662, "compression_ratio": 1.7157894736842105,
  "no_speech_prob": 0.24126069247722626}, {"id": 234, "seek": 328792, "start": 3287.92,
  "end": 3292.4, "text": " Research research it again and find what is the root cause
  and then.", "tokens": [50364, 10303, 2132, 309, 797, 293, 915, 437, 307, 264, 5593,
  3082, 293, 550, 13, 50588], "temperature": 0.0, "avg_logprob": -0.25997584379172023,
  "compression_ratio": 1.7307692307692308, "no_speech_prob": 0.051333919167518616},
  {"id": 235, "seek": 328792, "start": 3293.2400000000002, "end": 3304.08, "text":
  " Human will detect or machine will will detect it so I believe that this this is
  the question of of layers so you have like the machine learning layer and then.",
  "tokens": [50630, 10294, 486, 5531, 420, 3479, 486, 486, 5531, 309, 370, 286, 1697,
  300, 341, 341, 307, 264, 1168, 295, 295, 7914, 370, 291, 362, 411, 264, 3479, 2539,
  4583, 293, 550, 13, 51172], "temperature": 0.0, "avg_logprob": -0.25997584379172023,
  "compression_ratio": 1.7307692307692308, "no_speech_prob": 0.051333919167518616},
  {"id": 236, "seek": 328792, "start": 3304.8, "end": 3314.52, "text": " ML obstacles
  like you can you know auto ML and the hyper parameter optimization and data drift
  and model drift and other tools but.", "tokens": [51208, 21601, 17735, 411, 291,
  393, 291, 458, 8399, 21601, 293, 264, 9848, 13075, 19618, 293, 1412, 19699, 293,
  2316, 19699, 293, 661, 3873, 457, 13, 51694], "temperature": 0.0, "avg_logprob":
  -0.25997584379172023, "compression_ratio": 1.7307692307692308, "no_speech_prob":
  0.051333919167518616}, {"id": 237, "seek": 331452, "start": 3314.52, "end": 3329.08,
  "text": " We are I don''t think we are ready to fully automated all of the process
  and yeah this is like a great question for instance autonomous cars are we ready
  yet or not.", "tokens": [50364, 492, 366, 286, 500, 380, 519, 321, 366, 1919, 281,
  4498, 18473, 439, 295, 264, 1399, 293, 1338, 341, 307, 411, 257, 869, 1168, 337,
  5197, 23797, 5163, 366, 321, 1919, 1939, 420, 406, 13, 51092], "temperature": 0.0,
  "avg_logprob": -0.3535003344217936, "compression_ratio": 1.5740740740740742, "no_speech_prob":
  0.03337598219513893}, {"id": 238, "seek": 331452, "start": 3330.6, "end": 3338.52,
  "text": " This is I think this is the the challenge of the data science ecosystem
  in the next years.", "tokens": [51168, 639, 307, 286, 519, 341, 307, 264, 264, 3430,
  295, 264, 1412, 3497, 11311, 294, 264, 958, 924, 13, 51564], "temperature": 0.0,
  "avg_logprob": -0.3535003344217936, "compression_ratio": 1.5740740740740742, "no_speech_prob":
  0.03337598219513893}, {"id": 239, "seek": 333852, "start": 3339.32, "end": 3341.88,
  "text": " Yeah I think it''s also like.", "tokens": [50404, 865, 286, 519, 309,
  311, 611, 411, 13, 50532], "temperature": 0.0, "avg_logprob": -0.2300984448400037,
  "compression_ratio": 1.5133689839572193, "no_speech_prob": 0.042004186660051346},
  {"id": 240, "seek": 333852, "start": 3343.32, "end": 3359.0, "text": " Our psychological
  readiness to accept this solutions rights maybe previously when we didn''t have
  let''s say elevator so everyone was walking up the stairs and no one really complained
  but then when the first elevator arrived maybe people were like really.", "tokens":
  [50604, 2621, 14346, 34954, 281, 3241, 341, 6547, 4601, 1310, 8046, 562, 321, 994,
  380, 362, 718, 311, 584, 18782, 370, 1518, 390, 4494, 493, 264, 13471, 293, 572,
  472, 534, 33951, 457, 550, 562, 264, 700, 18782, 6678, 1310, 561, 645, 411, 534,
  13, 51388], "temperature": 0.0, "avg_logprob": -0.2300984448400037, "compression_ratio":
  1.5133689839572193, "no_speech_prob": 0.042004186660051346}, {"id": 241, "seek":
  335900, "start": 3359.56, "end": 3366.2, "text": " You know looking at it with open
  eyes and like what is this should they trust it will I get interrupt in it or something
  you know.", "tokens": [50392, 509, 458, 1237, 412, 309, 365, 1269, 2575, 293, 411,
  437, 307, 341, 820, 436, 3361, 309, 486, 286, 483, 12729, 294, 309, 420, 746, 291,
  458, 13, 50724], "temperature": 0.0, "avg_logprob": -0.21883544246707343, "compression_ratio":
  1.8192307692307692, "no_speech_prob": 0.04302505776286125}, {"id": 242, "seek":
  335900, "start": 3367.08, "end": 3370.6, "text": " So the same I think goes to what
  you just raised as the.", "tokens": [50768, 407, 264, 912, 286, 519, 1709, 281,
  437, 291, 445, 6005, 382, 264, 13, 50944], "temperature": 0.0, "avg_logprob": -0.21883544246707343,
  "compression_ratio": 1.8192307692307692, "no_speech_prob": 0.04302505776286125},
  {"id": 243, "seek": 335900, "start": 3372.04, "end": 3378.2, "text": " You know
  self driving cars you know I think it was ill and mask saying I don''t remember
  exactly the stats but something let''s say one and a thousand.", "tokens": [51016,
  509, 458, 2698, 4840, 5163, 291, 458, 286, 519, 309, 390, 3171, 293, 6094, 1566,
  286, 500, 380, 1604, 2293, 264, 18152, 457, 746, 718, 311, 584, 472, 293, 257, 4714,
  13, 51324], "temperature": 0.0, "avg_logprob": -0.21883544246707343, "compression_ratio":
  1.8192307692307692, "no_speech_prob": 0.04302505776286125}, {"id": 244, "seek":
  335900, "start": 3379.0, "end": 3388.76, "text": " You know so it avoids basically
  nine hundred ninety nine you know cases bad cases so would you trust that or do
  you need like it to be.", "tokens": [51364, 509, 458, 370, 309, 3641, 3742, 1936,
  4949, 3262, 25063, 4949, 291, 458, 3331, 1578, 3331, 370, 576, 291, 3361, 300, 420,
  360, 291, 643, 411, 309, 281, 312, 13, 51852], "temperature": 0.0, "avg_logprob":
  -0.21883544246707343, "compression_ratio": 1.8192307692307692, "no_speech_prob":
  0.04302505776286125}, {"id": 245, "seek": 338900, "start": 3389.0, "end": 3412.92,
  "text": " Even bigger number and so on so forth so like complete thousands so it''s
  never mistaken but what about cases where it''s hard to decide right like you inevitably
  going to crush the car now you need to choose where like to the human or maybe to
  to the I don''t know for to the tree or something which hurts the driver and stuff
  like that right so.", "tokens": [50364, 2754, 3801, 1230, 293, 370, 322, 370, 5220,
  370, 411, 3566, 5383, 370, 309, 311, 1128, 21333, 457, 437, 466, 3331, 689, 309,
  311, 1152, 281, 4536, 558, 411, 291, 28171, 516, 281, 10321, 264, 1032, 586, 291,
  643, 281, 2826, 689, 411, 281, 264, 1952, 420, 1310, 281, 281, 264, 286, 500, 380,
  458, 337, 281, 264, 4230, 420, 746, 597, 11051, 264, 6787, 293, 1507, 411, 300,
  558, 370, 13, 51560], "temperature": 0.0, "avg_logprob": -0.13961144497520045, "compression_ratio":
  1.6618357487922706, "no_speech_prob": 0.006587734445929527}, {"id": 246, "seek":
  341292, "start": 3412.92, "end": 3442.76, "text": " So this I think the same the
  same decisions that we would be making as humans then algorithms should make and
  I think what humans or humanity has hard time with is probably accepting the fact
  that someone else is going to make the decision right so yeah it''s yeah it''s a
  revolution you know you mentioned the elevator but you know the famous story of
  the end report with the horses and the cars why should we.", "tokens": [50412, 407,
  341, 286, 519, 264, 912, 264, 912, 5327, 300, 321, 576, 312, 1455, 382, 6255, 550,
  14642, 820, 652, 293, 286, 519, 437, 6255, 420, 10243, 575, 1152, 565, 365, 307,
  1391, 17391, 264, 1186, 300, 1580, 1646, 307, 516, 281, 652, 264, 3537, 558, 370,
  1338, 309, 311, 1338, 309, 311, 257, 8894, 291, 458, 291, 2835, 264, 18782, 457,
  291, 458, 264, 4618, 1657, 295, 264, 917, 2275, 365, 264, 13112, 293, 264, 5163,
  983, 820, 321, 13, 51856], "temperature": 0.0, "avg_logprob": -0.23662346885317848,
  "compression_ratio": 1.8097345132743363, "no_speech_prob": 0.03795231878757477},
  {"id": 247, "seek": 344292, "start": 3442.92, "end": 3450.92, "text": " Need the
  cars right so it''s a it''s a revolution I think that most of.", "tokens": [50364,
  16984, 264, 5163, 558, 370, 309, 311, 257, 309, 311, 257, 8894, 286, 519, 300, 881,
  295, 13, 50764], "temperature": 0.0, "avg_logprob": -0.24705459822469683, "compression_ratio":
  1.6031746031746033, "no_speech_prob": 0.005872825160622597}, {"id": 248, "seek":
  344292, "start": 3451.92, "end": 3471.92, "text": " The features that we are working
  on improving the quality of life and people you know can automate processes and
  and on focus in their you know in their family and instead of doing some complicated
  task they can you know focus their.", "tokens": [50814, 440, 4122, 300, 321, 366,
  1364, 322, 11470, 264, 3125, 295, 993, 293, 561, 291, 458, 393, 31605, 7555, 293,
  293, 322, 1879, 294, 641, 291, 458, 294, 641, 1605, 293, 2602, 295, 884, 512, 6179,
  5633, 436, 393, 291, 458, 1879, 641, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.24705459822469683, "compression_ratio": 1.6031746031746033, "no_speech_prob":
  0.005872825160622597}, {"id": 249, "seek": 347292, "start": 3472.92, "end": 3490.92,
  "text": " Time on innovation or you know play football or soccer whatever they want
  and you know makes our life easier to some extent yeah and we believe collectively
  that vector search is going to help there i.", "tokens": [50364, 6161, 322, 8504,
  420, 291, 458, 862, 7346, 420, 15469, 2035, 436, 528, 293, 291, 458, 1669, 527,
  993, 3571, 281, 512, 8396, 1338, 293, 321, 1697, 24341, 300, 8062, 3164, 307, 516,
  281, 854, 456, 741, 13, 51264], "temperature": 0.0, "avg_logprob": -0.1753052756899879,
  "compression_ratio": 1.4460431654676258, "no_speech_prob": 0.035924822092056274},
  {"id": 250, "seek": 349092, "start": 3490.92, "end": 3511.92, "text": " I really
  like also to of course ask this my philosophical question but before that i was
  thinking like what do you think on the field in general the vector search and maybe
  including search and machine learning what do a lot is happening but what do you
  think is still missing from your perspective.", "tokens": [50364, 286, 534, 411,
  611, 281, 295, 1164, 1029, 341, 452, 25066, 1168, 457, 949, 300, 741, 390, 1953,
  411, 437, 360, 291, 519, 322, 264, 2519, 294, 2674, 264, 8062, 3164, 293, 1310,
  3009, 3164, 293, 3479, 2539, 437, 360, 257, 688, 307, 2737, 457, 437, 360, 291,
  519, 307, 920, 5361, 490, 428, 4585, 13, 51414], "temperature": 0.0, "avg_logprob":
  -0.11387457847595214, "compression_ratio": 1.6611111111111112, "no_speech_prob":
  0.16490373015403748}, {"id": 251, "seek": 351192, "start": 3512.92, "end": 3515.92,
  "text": " Something that maybe we need to fix.", "tokens": [50414, 6595, 300, 1310,
  321, 643, 281, 3191, 13, 50564], "temperature": 0.0, "avg_logprob": -0.12341706202580378,
  "compression_ratio": 1.6476683937823835, "no_speech_prob": 0.03781450539827347},
  {"id": 252, "seek": 351192, "start": 3516.92, "end": 3540.92, "text": " To be more
  efficient yeah I think it''s it''s it''s education simplifying the concept of search
  I think this is the should be our main focus so education generating content and
  again I really like the grandmother test simplifying not like super complicated
  mathematical equations etc.", "tokens": [50614, 1407, 312, 544, 7148, 1338, 286,
  519, 309, 311, 309, 311, 309, 311, 3309, 6883, 5489, 264, 3410, 295, 3164, 286,
  519, 341, 307, 264, 820, 312, 527, 2135, 1879, 370, 3309, 17746, 2701, 293, 797,
  286, 534, 411, 264, 14317, 1500, 6883, 5489, 406, 411, 1687, 6179, 18894, 11787,
  5183, 13, 51814], "temperature": 0.0, "avg_logprob": -0.12341706202580378, "compression_ratio":
  1.6476683937823835, "no_speech_prob": 0.03781450539827347}, {"id": 253, "seek":
  354192, "start": 3541.92, "end": 3565.92, "text": " So I think it''s education we
  are you know the ecosystem is trying to generate high quality content videos a YouTube
  blog post we we are trying to contribute to this effort as well.", "tokens": [50364,
  407, 286, 519, 309, 311, 3309, 321, 366, 291, 458, 264, 11311, 307, 1382, 281, 8460,
  1090, 3125, 2701, 2145, 257, 3088, 6968, 2183, 321, 321, 366, 1382, 281, 10586,
  281, 341, 4630, 382, 731, 13, 51564], "temperature": 0.0, "avg_logprob": -0.3443129539489746,
  "compression_ratio": 1.3333333333333333, "no_speech_prob": 0.025917518883943558},
  {"id": 254, "seek": 356592, "start": 3565.92, "end": 3593.92, "text": " We are doing
  enough and you know it can be like high school or universities so but again this
  is vector search is technology it''s an enabler it''s not the it''s not the objective
  it''s not the it''s not the target but in order to unlock the potential of vector
  search and machine learning and transform and so on all of these cool stuff we should.",
  "tokens": [50364, 492, 366, 884, 1547, 293, 291, 458, 309, 393, 312, 411, 1090,
  1395, 420, 11779, 370, 457, 797, 341, 307, 8062, 3164, 307, 2899, 309, 311, 364,
  465, 455, 1918, 309, 311, 406, 264, 309, 311, 406, 264, 10024, 309, 311, 406, 264,
  309, 311, 406, 264, 3779, 457, 294, 1668, 281, 11634, 264, 3995, 295, 8062, 3164,
  293, 3479, 2539, 293, 4088, 293, 370, 322, 439, 295, 613, 1627, 1507, 321, 820,
  13, 51764], "temperature": 0.0, "avg_logprob": -0.16971482986058944, "compression_ratio":
  1.7323232323232323, "no_speech_prob": 0.40467748045921326}, {"id": 255, "seek":
  359392, "start": 3593.92, "end": 3615.92, "text": " Invest some of our resources
  in education and learning and training and you know unlock the potential that every
  developer can kill build a vector vector search based application in in every field
  like it can be as I mentioned before health care,", "tokens": [50364, 14008, 512,
  295, 527, 3593, 294, 3309, 293, 2539, 293, 3097, 293, 291, 458, 11634, 264, 3995,
  300, 633, 10754, 393, 1961, 1322, 257, 8062, 8062, 3164, 2361, 3861, 294, 294, 633,
  2519, 411, 309, 393, 312, 382, 286, 2835, 949, 1585, 1127, 11, 51464], "temperature":
  0.0, "avg_logprob": -0.20028056701024374, "compression_ratio": 1.5471698113207548,
  "no_speech_prob": 0.029232246801257133}, {"id": 256, "seek": 361592, "start": 3615.92,
  "end": 3642.92, "text": " care, FinTech education and any other domain that manufacturing
  or any other domain that you would like that is bigger to solve some problem I think
  we should you know simplified similar to the revolution of auto ml so instead of
  you know processing and labeling images etc.", "tokens": [50364, 1127, 11, 3773,
  36050, 3309, 293, 604, 661, 9274, 300, 11096, 420, 604, 661, 9274, 300, 291, 576,
  411, 300, 307, 3801, 281, 5039, 512, 1154, 286, 519, 321, 820, 291, 458, 26335,
  2531, 281, 264, 8894, 295, 8399, 23271, 370, 2602, 295, 291, 458, 9007, 293, 40244,
  5267, 5183, 13, 51714], "temperature": 0.0, "avg_logprob": -0.2777529629794034,
  "compression_ratio": 1.5657142857142856, "no_speech_prob": 0.3736276924610138},
  {"id": 257, "seek": 364292, "start": 3642.92, "end": 3671.92, "text": " You have
  like an auto auto ml tool or solution and your provision you provision the data
  labeling it and then the under the hood the auto ml model will run the experiments
  find the right algorithm find the right hyper parameters optimizing them you can
  define what is the what is the KPI that you would like to optimize.", "tokens":
  [50364, 509, 362, 411, 364, 8399, 8399, 23271, 2290, 420, 3827, 293, 428, 17225,
  291, 17225, 264, 1412, 40244, 309, 293, 550, 264, 833, 264, 13376, 264, 8399, 23271,
  2316, 486, 1190, 264, 12050, 915, 264, 558, 9284, 915, 264, 558, 9848, 9834, 40425,
  552, 291, 393, 6964, 437, 307, 264, 437, 307, 264, 591, 31701, 300, 291, 576, 411,
  281, 19719, 13, 51814], "temperature": 0.0, "avg_logprob": -0.15898974736531576,
  "compression_ratio": 1.7204301075268817, "no_speech_prob": 0.3567464053630829},
  {"id": 258, "seek": 367192, "start": 3671.92, "end": 3700.92, "text": " If it''s
  f1 score or recall or whatever and then you will get the model and if you would
  like to deep dive you will get the code so you know generating models with low code
  so this is another and another area that we should focus in but you know to some
  extent I believe that education training and generating high quality content.",
  "tokens": [50364, 759, 309, 311, 283, 16, 6175, 420, 9901, 420, 2035, 293, 550,
  291, 486, 483, 264, 2316, 293, 498, 291, 576, 411, 281, 2452, 9192, 291, 486, 483,
  264, 3089, 370, 291, 458, 17746, 5245, 365, 2295, 3089, 370, 341, 307, 1071, 293,
  1071, 1859, 300, 321, 820, 1879, 294, 457, 291, 458, 281, 512, 8396, 286, 1697,
  300, 3309, 3097, 293, 17746, 1090, 3125, 2701, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.13065814971923828, "compression_ratio": 1.7098445595854923, "no_speech_prob":
  0.07434297353029251}, {"id": 259, "seek": 370092, "start": 3700.92, "end": 3706.92,
  "text": " So it should be our focus right now.", "tokens": [50364, 407, 309, 820,
  312, 527, 1879, 558, 586, 13, 50664], "temperature": 0.0, "avg_logprob": -0.17756898403167726,
  "compression_ratio": 1.6396396396396395, "no_speech_prob": 0.048153337091207504},
  {"id": 260, "seek": 370092, "start": 3706.92, "end": 3729.92, "text": " Yeah I think
  you put it really well and I would probably even add to this that yes there is content
  which kind of like promotes someone''s solution right but at the same time you really
  want to educate like why should people even care about your solution so you need
  to take few steps back and explain what are we talking about.", "tokens": [50664,
  865, 286, 519, 291, 829, 309, 534, 731, 293, 286, 576, 1391, 754, 909, 281, 341,
  300, 2086, 456, 307, 2701, 597, 733, 295, 411, 36015, 1580, 311, 3827, 558, 457,
  412, 264, 912, 565, 291, 534, 528, 281, 16092, 411, 983, 820, 561, 754, 1127, 466,
  428, 3827, 370, 291, 643, 281, 747, 1326, 4439, 646, 293, 2903, 437, 366, 321, 1417,
  466, 13, 51814], "temperature": 0.0, "avg_logprob": -0.17756898403167726, "compression_ratio":
  1.6396396396396395, "no_speech_prob": 0.048153337091207504}, {"id": 261, "seek":
  372992, "start": 3729.92, "end": 3757.92, "text": " You know what problems exist
  that you are trying to that you are targeting right so I still if I was asking the
  same question to myself I still see a lot of content which is much more promotional
  than it should be because in the beginning of this revolution you still need to
  explain what is happening what the hell is going on you know why why because the
  reaction could be also from the incumbent players that they will say no this is
  not.", "tokens": [50364, 509, 458, 437, 2740, 2514, 300, 291, 366, 1382, 281, 300,
  291, 366, 17918, 558, 370, 286, 920, 498, 286, 390, 3365, 264, 912, 1168, 281, 2059,
  286, 920, 536, 257, 688, 295, 2701, 597, 307, 709, 544, 41790, 813, 309, 820, 312,
  570, 294, 264, 2863, 295, 341, 8894, 291, 920, 643, 281, 2903, 437, 307, 2737, 437,
  264, 4921, 307, 516, 322, 291, 458, 983, 983, 570, 264, 5480, 727, 312, 611, 490,
  264, 45539, 4150, 300, 436, 486, 584, 572, 341, 307, 406, 13, 51764], "temperature":
  0.2, "avg_logprob": -0.10864009437980232, "compression_ratio": 1.778225806451613,
  "no_speech_prob": 0.0878516212105751}, {"id": 262, "seek": 375792, "start": 3757.92,
  "end": 3777.92, "text": " No this is not no this is not where things are going they
  will go go back to their clients and say the same but like you should not position
  it that way you should you should explain as you said like start from the problem
  right start from what is your actual business and product target.", "tokens": [50364,
  883, 341, 307, 406, 572, 341, 307, 406, 689, 721, 366, 516, 436, 486, 352, 352,
  646, 281, 641, 6982, 293, 584, 264, 912, 457, 411, 291, 820, 406, 2535, 309, 300,
  636, 291, 820, 291, 820, 2903, 382, 291, 848, 411, 722, 490, 264, 1154, 558, 722,
  490, 437, 307, 428, 3539, 1606, 293, 1674, 3779, 13, 51364], "temperature": 0.0,
  "avg_logprob": -0.0915422131938319, "compression_ratio": 1.7349397590361446, "no_speech_prob":
  0.07426150888204575}, {"id": 263, "seek": 377792, "start": 3777.92, "end": 3803.92,
  "text": " And I guess this is not something that many engineers asking themselves
  some of them some of the best that I know do some of the best data scientists do
  as well they don''t code before they understood what is being asked of them and
  I think it''s an amazing skill and this is exactly where education also helps like
  why should also data scientists or engineers care about this new new field.", "tokens":
  [50364, 400, 286, 2041, 341, 307, 406, 746, 300, 867, 11955, 3365, 2969, 512, 295,
  552, 512, 295, 264, 1151, 300, 286, 458, 360, 512, 295, 264, 1151, 1412, 7708, 360,
  382, 731, 436, 500, 380, 3089, 949, 436, 7320, 437, 307, 885, 2351, 295, 552, 293,
  286, 519, 309, 311, 364, 2243, 5389, 293, 341, 307, 2293, 689, 3309, 611, 3665,
  411, 983, 820, 611, 1412, 7708, 420, 11955, 1127, 466, 341, 777, 777, 2519, 13,
  51664], "temperature": 0.0, "avg_logprob": -0.07445611357688904, "compression_ratio":
  1.8093023255813954, "no_speech_prob": 0.07346794754266739}, {"id": 264, "seek":
  380392, "start": 3803.92, "end": 3826.92, "text": " Yeah, yeah, this is super important
  and yeah, we should honestly we should you know when I''m saying again internally
  we should improve the quality of the content and not trying you know to sell our
  solution just to explain for software developer without the background in machine
  learning.", "tokens": [50364, 865, 11, 1338, 11, 341, 307, 1687, 1021, 293, 1338,
  11, 321, 820, 6095, 321, 820, 291, 458, 562, 286, 478, 1566, 797, 19501, 321, 820,
  3470, 264, 3125, 295, 264, 2701, 293, 406, 1382, 291, 458, 281, 3607, 527, 3827,
  445, 281, 2903, 337, 4722, 10754, 1553, 264, 3678, 294, 3479, 2539, 13, 51514],
  "temperature": 0.0, "avg_logprob": -0.16991370299766803, "compression_ratio": 1.5706521739130435,
  "no_speech_prob": 0.057909753173589706}, {"id": 265, "seek": 382692, "start": 3826.92,
  "end": 3855.92, "text": " And to simplify it for him and to explain what is the
  concept what is the trade off between the concept and again to give him the option
  to understand what is happening and issue decide what is the best tool for him is
  it a screwdriver is it an hammer it will understand the bits and bytes but and the
  trade off and and give him the the full picture about what what are the problems.",
  "tokens": [50414, 400, 281, 20460, 309, 337, 796, 293, 281, 2903, 437, 307, 264,
  3410, 437, 307, 264, 4923, 766, 1296, 264, 3410, 293, 797, 281, 976, 796, 264, 3614,
  281, 1223, 437, 307, 2737, 293, 2734, 4536, 437, 307, 264, 1151, 2290, 337, 796,
  307, 309, 257, 27282, 307, 309, 364, 13017, 309, 486, 1223, 264, 9239, 293, 36088,
  457, 293, 264, 4923, 766, 293, 293, 976, 796, 264, 264, 1577, 3036, 466, 437, 437,
  366, 264, 2740, 13, 51814], "temperature": 0.0, "avg_logprob": -0.17395376276086877,
  "compression_ratio": 1.9441624365482233, "no_speech_prob": 0.16073961555957794},
  {"id": 266, "seek": 385692, "start": 3856.92, "end": 3865.92, "text": " Yeah, I
  think it''s a great question.", "tokens": [50364, 865, 11, 286, 519, 309, 311, 257,
  869, 1168, 13, 50814], "temperature": 0.4, "avg_logprob": -0.45776950353863594,
  "compression_ratio": 1.670940170940171, "no_speech_prob": 0.07698927819728851},
  {"id": 267, "seek": 385692, "start": 3865.92, "end": 3872.92, "text": " It was in
  cons of every solution and you know you will take the decision.", "tokens": [50814,
  467, 390, 294, 1014, 295, 633, 3827, 293, 291, 458, 291, 486, 747, 264, 3537, 13,
  51164], "temperature": 0.4, "avg_logprob": -0.45776950353863594, "compression_ratio":
  1.670940170940171, "no_speech_prob": 0.07698927819728851}, {"id": 268, "seek": 385692,
  "start": 3872.92, "end": 3882.92, "text": " Yeah, exactly and I think if we decade
  more some of the players doing doing really great job there and I am looking forward
  also to see some blog posts you already mentioned the notebooks that you guys are
  publishing on your website and I believe that was searching website right.", "tokens":
  [51164, 865, 11, 2293, 293, 286, 519, 498, 321, 10378, 544, 512, 295, 264, 4150,
  884, 884, 534, 869, 1691, 456, 293, 286, 669, 1237, 2128, 611, 281, 536, 512, 6968,
  12300, 291, 1217, 2835, 264, 43782, 300, 291, 1074, 366, 17832, 322, 428, 3144,
  293, 286, 1697, 300, 390, 10808, 3144, 558, 13, 51664], "temperature": 0.4, "avg_logprob":
  -0.45776950353863594, "compression_ratio": 1.670940170940171, "no_speech_prob":
  0.07698927819728851}, {"id": 269, "seek": 388292, "start": 3882.92, "end": 3894.92,
  "text": " Now that I learned that you really care about the topic I think it''s
  important to create and share and maybe educate the educators and give the example
  so I think this is really great.", "tokens": [50364, 823, 300, 286, 3264, 300, 291,
  534, 1127, 466, 264, 4829, 286, 519, 309, 311, 1021, 281, 1884, 293, 2073, 293,
  1310, 16092, 264, 22819, 293, 976, 264, 1365, 370, 286, 519, 341, 307, 534, 869,
  13, 50964], "temperature": 0.0, "avg_logprob": -0.13913886687334845, "compression_ratio":
  1.597938144329897, "no_speech_prob": 0.0948852077126503}, {"id": 270, "seek": 388292,
  "start": 3894.92, "end": 3908.92, "text": " Yeah, yeah, one example the great blog
  was that one of our software developer wrote is how to optimize open search workloads.",
  "tokens": [50964, 865, 11, 1338, 11, 472, 1365, 264, 869, 6968, 390, 300, 472, 295,
  527, 4722, 10754, 4114, 307, 577, 281, 19719, 1269, 3164, 32452, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.13913886687334845, "compression_ratio": 1.597938144329897,
  "no_speech_prob": 0.0948852077126503}, {"id": 271, "seek": 390892, "start": 3908.92,
  "end": 3937.92, "text": " So again it''s not we have a plugin on top of it, but
  he wrote about what are the options without you know writing about our solution
  and what are the options out they can our customers can optimize it and another
  interesting blog post that we will publish soon is you know benchmarking one of
  the things that we should improve in our ecosystem is to decide on on a standard
  tool that will.", "tokens": [50364, 407, 797, 309, 311, 406, 321, 362, 257, 23407,
  322, 1192, 295, 309, 11, 457, 415, 4114, 466, 437, 366, 264, 3956, 1553, 291, 458,
  3579, 466, 527, 3827, 293, 437, 366, 264, 3956, 484, 436, 393, 527, 4581, 393, 19719,
  309, 293, 1071, 1880, 6968, 2183, 300, 321, 486, 11374, 2321, 307, 291, 458, 18927,
  278, 472, 295, 264, 721, 300, 321, 820, 3470, 294, 527, 11311, 307, 281, 4536, 322,
  322, 257, 3832, 2290, 300, 486, 13, 51814], "temperature": 0.0, "avg_logprob": -0.1335151051900473,
  "compression_ratio": 1.728888888888889, "no_speech_prob": 0.01586165279150009},
  {"id": 272, "seek": 393792, "start": 3937.92, "end": 3965.92, "text": " Help us
  to decide what is the KPI and the benchmark there are various benchmark over there
  i''m familiar we are familiar with rally and the elastic benchmark i haven''t seen
  like a good benchmark industry standard in in the vector search there was the challenge
  of big a and one year ago two years ago, but again I don''t think we have.", "tokens":
  [50364, 10773, 505, 281, 4536, 437, 307, 264, 591, 31701, 293, 264, 18927, 456,
  366, 3683, 18927, 670, 456, 741, 478, 4963, 321, 366, 4963, 365, 17584, 293, 264,
  17115, 18927, 741, 2378, 380, 1612, 411, 257, 665, 18927, 3518, 3832, 294, 294,
  264, 8062, 3164, 456, 390, 264, 3430, 295, 955, 257, 293, 472, 1064, 2057, 732,
  924, 2057, 11, 457, 797, 286, 500, 380, 519, 321, 362, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.22193279005076788, "compression_ratio": 1.6818181818181819,
  "no_speech_prob": 0.03456810489296913}, {"id": 273, "seek": 396592, "start": 3965.92,
  "end": 3980.92, "text": " Good tool today, but so one of our developers wrote out
  to run the benchmark tool so it was like open search benchmark how to use this benchmark
  and what is the.", "tokens": [50364, 2205, 2290, 965, 11, 457, 370, 472, 295, 527,
  8849, 4114, 484, 281, 1190, 264, 18927, 2290, 370, 309, 390, 411, 1269, 3164, 18927,
  577, 281, 764, 341, 18927, 293, 437, 307, 264, 13, 51114], "temperature": 0.0, "avg_logprob":
  -0.18407570688348068, "compression_ratio": 1.412280701754386, "no_speech_prob":
  0.039454713463783264}, {"id": 274, "seek": 398092, "start": 3980.92, "end": 4004.92,
  "text": " Beats and bytes and tips how to understand the benchmark tools so yeah
  I think that starting from the education and then offering customers to check your
  solution yeah sounds great i think maybe even by the time this podcast is published
  we have that new blog as well.", "tokens": [50364, 879, 1720, 293, 36088, 293, 6082,
  577, 281, 1223, 264, 18927, 3873, 370, 1338, 286, 519, 300, 2891, 490, 264, 3309,
  293, 550, 8745, 4581, 281, 1520, 428, 3827, 1338, 3263, 869, 741, 519, 1310, 754,
  538, 264, 565, 341, 7367, 307, 6572, 321, 362, 300, 777, 6968, 382, 731, 13, 51564],
  "temperature": 0.0, "avg_logprob": -0.15552491274746982, "compression_ratio": 1.5491329479768785,
  "no_speech_prob": 0.2141244113445282}, {"id": 275, "seek": 400492, "start": 4004.92,
  "end": 4031.92, "text": " Hey, I''m really excited to be chatting to you today,
  I mean it''s attached a lot of deep topics i''m sure we could have gone for longer,
  but I was also really curious to ask you this magical why question you know the
  same way as you said don''t think about software think about the problem that you''re
  solving the reason i''m asking why question is because I truly believe.", "tokens":
  [50364, 1911, 11, 286, 478, 534, 2919, 281, 312, 24654, 281, 291, 965, 11, 286,
  914, 309, 311, 8570, 257, 688, 295, 2452, 8378, 741, 478, 988, 321, 727, 362, 2780,
  337, 2854, 11, 457, 286, 390, 611, 534, 6369, 281, 1029, 291, 341, 12066, 983, 1168,
  291, 458, 264, 912, 636, 382, 291, 848, 500, 380, 519, 466, 4722, 519, 466, 264,
  1154, 300, 291, 434, 12606, 264, 1778, 741, 478, 3365, 983, 1168, 307, 570, 286,
  4908, 1697, 13, 51714], "temperature": 0.0, "avg_logprob": -0.1777872471582322,
  "compression_ratio": 1.6255506607929515, "no_speech_prob": 0.3613390326499939},
  {"id": 276, "seek": 403192, "start": 4031.92, "end": 4060.92, "text": " But if you
  don''t understand why you do things then you''re kind of like flying through things
  right so you might as well regret some sometime later maybe you train the muscle
  but still i don''t think it''s a good sensible approach in your life so i''m really
  interested given all your experience in in machine learning and product management
  software development why are you excited to work on vector search search whatever
  is it that you do day today.", "tokens": [50364, 583, 498, 291, 500, 380, 1223,
  983, 291, 360, 721, 550, 291, 434, 733, 295, 411, 7137, 807, 721, 558, 370, 291,
  1062, 382, 731, 10879, 512, 15053, 1780, 1310, 291, 3847, 264, 8679, 457, 920, 741,
  500, 380, 519, 309, 311, 257, 665, 25380, 3109, 294, 428, 993, 370, 741, 478, 534,
  3102, 2212, 439, 428, 1752, 294, 294, 3479, 2539, 293, 1674, 4592, 4722, 3250, 983,
  366, 291, 2919, 281, 589, 322, 8062, 3164, 3164, 2035, 307, 309, 300, 291, 360,
  786, 965, 13, 51814], "temperature": 0.0, "avg_logprob": -0.11619693241762312, "compression_ratio":
  1.6905660377358491, "no_speech_prob": 0.023022204637527466}, {"id": 277, "seek":
  406192, "start": 4062.32, "end": 4083.04, "text": " Yeah, I think this is a great
  question I really like the why combinator accelerator approach for building products
  build something that customers like or love and essentially you know we are building
  some trying to build some cool stuff and make.", "tokens": [50384, 865, 11, 286,
  519, 341, 307, 257, 869, 1168, 286, 534, 411, 264, 983, 2512, 31927, 39889, 3109,
  337, 2390, 3383, 1322, 746, 300, 4581, 411, 420, 959, 293, 4476, 291, 458, 321,
  366, 2390, 512, 1382, 281, 1322, 512, 1627, 1507, 293, 652, 13, 51420], "temperature":
  0.0, "avg_logprob": -0.24081407274518693, "compression_ratio": 1.5279503105590062,
  "no_speech_prob": 0.02774079144001007}, {"id": 278, "seek": 408304, "start": 4083.04,
  "end": 4110.04, "text": " People''s life easier happier i gave an example of the
  girl from Asia so this is this is I think one of our mission but it''s not only
  the girl from Asia that would like to purchase a red short sleeve dress it''s the
  DevOps that is trying to find the right log and instead of working it for hours
  it will take him.", "tokens": [50364, 3432, 311, 993, 3571, 20423, 741, 2729, 364,
  1365, 295, 264, 2013, 490, 10038, 370, 341, 307, 341, 307, 286, 519, 472, 295, 527,
  4447, 457, 309, 311, 406, 787, 264, 2013, 490, 10038, 300, 576, 411, 281, 8110,
  257, 2182, 2099, 21138, 5231, 309, 311, 264, 43051, 300, 307, 1382, 281, 915, 264,
  558, 3565, 293, 2602, 295, 1364, 309, 337, 2496, 309, 486, 747, 796, 13, 51714],
  "temperature": 0.0, "avg_logprob": -0.1759140756395128, "compression_ratio": 1.5707070707070707,
  "no_speech_prob": 0.19459618628025055}, {"id": 279, "seek": 411004, "start": 4110.04,
  "end": 4127.04, "text": " Seconds okay so essentially our mission and i''m excited
  that i''m working on this topic it''s to make the the consumers businesses and enterprises
  life easier.", "tokens": [50364, 5736, 82, 1392, 370, 4476, 527, 4447, 293, 741,
  478, 2919, 300, 741, 478, 1364, 322, 341, 4829, 309, 311, 281, 652, 264, 264, 11883,
  6011, 293, 29034, 993, 3571, 13, 51214], "temperature": 0.0, "avg_logprob": -0.2132699966430664,
  "compression_ratio": 1.3305084745762712, "no_speech_prob": 0.0479571595788002},
  {"id": 280, "seek": 412704, "start": 4127.24, "end": 4136.44, "text": " And so I
  think it''s a very simple statement of the why and I believe that this is this is
  my mission or this is our mission.", "tokens": [50374, 400, 370, 286, 519, 309,
  311, 257, 588, 2199, 5629, 295, 264, 983, 293, 286, 1697, 300, 341, 307, 341, 307,
  452, 4447, 420, 341, 307, 527, 4447, 13, 50834], "temperature": 0.0, "avg_logprob":
  -0.17513853406149243, "compression_ratio": 1.5471698113207548, "no_speech_prob":
  0.09198193997144699}, {"id": 281, "seek": 412704, "start": 4137.5199999999995, "end":
  4144.24, "text": " And and to some extent I think that this is like a doing good
  perspective so you know you have like.", "tokens": [50888, 400, 293, 281, 512, 8396,
  286, 519, 300, 341, 307, 411, 257, 884, 665, 4585, 370, 291, 458, 291, 362, 411,
  13, 51224], "temperature": 0.0, "avg_logprob": -0.17513853406149243, "compression_ratio":
  1.5471698113207548, "no_speech_prob": 0.09198193997144699}, {"id": 282, "seek":
  412704, "start": 4146.12, "end": 4149.6, "text": " gambling company is.", "tokens":
  [51318, 27077, 2237, 307, 13, 51492], "temperature": 0.0, "avg_logprob": -0.17513853406149243,
  "compression_ratio": 1.5471698113207548, "no_speech_prob": 0.09198193997144699},
  {"id": 283, "seek": 414960, "start": 4150.6, "end": 4173.6, "text": " building some
  stuff and building applications and i''m my approach is you know building things
  that will help the humanity so i''m exciting that this is the things that i''m working
  on and by the way this was in my previous startup when we tried to save life right
  drowning detection.", "tokens": [50414, 2390, 512, 1507, 293, 2390, 5821, 293, 741,
  478, 452, 3109, 307, 291, 458, 2390, 721, 300, 486, 854, 264, 10243, 370, 741, 478,
  4670, 300, 341, 307, 264, 721, 300, 741, 478, 1364, 322, 293, 538, 264, 636, 341,
  390, 294, 452, 3894, 18578, 562, 321, 3031, 281, 3155, 993, 558, 37198, 17784, 13,
  51564], "temperature": 0.0, "avg_logprob": -0.1816116106712212, "compression_ratio":
  1.6149425287356323, "no_speech_prob": 0.017696810886263847}, {"id": 284, "seek":
  417360, "start": 4173.6, "end": 4184.6, "text": " and you issue residential pool
  open water and you know save life and if we can you know save life maybe for health
  applications.", "tokens": [50364, 293, 291, 2734, 17389, 7005, 1269, 1281, 293,
  291, 458, 3155, 993, 293, 498, 321, 393, 291, 458, 3155, 993, 1310, 337, 1585, 5821,
  13, 50914], "temperature": 0.0, "avg_logprob": -0.3255566564099542, "compression_ratio":
  1.5975609756097562, "no_speech_prob": 0.03280489891767502}, {"id": 285, "seek":
  417360, "start": 4185.6, "end": 4193.84, "text": " detecting cancer with the image
  embeddings or some other cool stuff i''m super excited that this is the domain that
  we are working on.", "tokens": [50964, 40237, 5592, 365, 264, 3256, 12240, 29432,
  420, 512, 661, 1627, 1507, 741, 478, 1687, 2919, 300, 341, 307, 264, 9274, 300,
  321, 366, 1364, 322, 13, 51376], "temperature": 0.0, "avg_logprob": -0.3255566564099542,
  "compression_ratio": 1.5975609756097562, "no_speech_prob": 0.03280489891767502},
  {"id": 286, "seek": 419384, "start": 4194.4400000000005, "end": 4202.360000000001,
  "text": " yeah this is this is very relatable in this fantastic that you''re bringing
  this up you know how we can actually improve life.", "tokens": [50394, 1338, 341,
  307, 341, 307, 588, 42355, 294, 341, 5456, 300, 291, 434, 5062, 341, 493, 291, 458,
  577, 321, 393, 767, 3470, 993, 13, 50790], "temperature": 0.0, "avg_logprob": -0.21439705954657662,
  "compression_ratio": 1.6648936170212767, "no_speech_prob": 0.021486863493919373},
  {"id": 287, "seek": 419384, "start": 4203.56, "end": 4204.64, "text": " beside building.",
  "tokens": [50850, 15726, 2390, 13, 50904], "temperature": 0.0, "avg_logprob": -0.21439705954657662,
  "compression_ratio": 1.6648936170212767, "no_speech_prob": 0.021486863493919373},
  {"id": 288, "seek": 419384, "start": 4205.360000000001, "end": 4207.84, "text":
  " great products or products that sell.", "tokens": [50940, 869, 3383, 420, 3383,
  300, 3607, 13, 51064], "temperature": 0.0, "avg_logprob": -0.21439705954657662,
  "compression_ratio": 1.6648936170212767, "no_speech_prob": 0.021486863493919373},
  {"id": 289, "seek": 419384, "start": 4208.92, "end": 4218.16, "text": " This is
  this is amazing and to conclude is there any announcement that you want to make
  from the from your side of from search room.", "tokens": [51118, 639, 307, 341,
  307, 2243, 293, 281, 16886, 307, 456, 604, 12847, 300, 291, 528, 281, 652, 490,
  264, 490, 428, 1252, 295, 490, 3164, 1808, 13, 51580], "temperature": 0.0, "avg_logprob":
  -0.21439705954657662, "compression_ratio": 1.6648936170212767, "no_speech_prob":
  0.021486863493919373}, {"id": 290, "seek": 421816, "start": 4218.5199999999995,
  "end": 4219.16, "text": " A. I.", "tokens": [50382, 316, 13, 286, 13, 50414], "temperature":
  0.0, "avg_logprob": -0.40305386559437895, "compression_ratio": 1.42, "no_speech_prob":
  0.021343037486076355}, {"id": 291, "seek": 421816, "start": 4220.16, "end": 4224.48,
  "text": " yeah yeah so i''m very excited because we are building.", "tokens": [50464,
  1338, 1338, 370, 741, 478, 588, 2919, 570, 321, 366, 2390, 13, 50680], "temperature":
  0.0, "avg_logprob": -0.40305386559437895, "compression_ratio": 1.42, "no_speech_prob":
  0.021343037486076355}, {"id": 292, "seek": 421816, "start": 4225.96, "end": 4235.32,
  "text": " some cool stuff so the first one we launch our search you may i platform
  where we offer customers a free tier to check our.", "tokens": [50754, 512, 1627,
  1507, 370, 264, 700, 472, 321, 4025, 527, 3164, 291, 815, 741, 3663, 689, 321, 2626,
  4581, 257, 1737, 12362, 281, 1520, 527, 13, 51222], "temperature": 0.0, "avg_logprob":
  -0.40305386559437895, "compression_ratio": 1.42, "no_speech_prob": 0.021343037486076355},
  {"id": 293, "seek": 421816, "start": 4236.5199999999995, "end": 4239.32, "text":
  " platform and again it''s not.", "tokens": [51282, 3663, 293, 797, 309, 311, 406,
  13, 51422], "temperature": 0.0, "avg_logprob": -0.40305386559437895, "compression_ratio":
  1.42, "no_speech_prob": 0.021343037486076355}, {"id": 294, "seek": 423932, "start":
  4240.32, "end": 4252.32, "text": " fully working we are not supporting all of the
  features but it this is very important it is very important for us to get your feedback
  so i encourage you to check it and to.", "tokens": [50414, 4498, 1364, 321, 366,
  406, 7231, 439, 295, 264, 4122, 457, 309, 341, 307, 588, 1021, 309, 307, 588, 1021,
  337, 505, 281, 483, 428, 5824, 370, 741, 5373, 291, 281, 1520, 309, 293, 281, 13,
  51014], "temperature": 0.0, "avg_logprob": -0.1634552323973024, "compression_ratio":
  1.7142857142857142, "no_speech_prob": 0.06491108238697052}, {"id": 295, "seek":
  423932, "start": 4253.32, "end": 4257.32, "text": " send me an email or send my
  team an email or in our support.", "tokens": [51064, 2845, 385, 364, 3796, 420,
  2845, 452, 1469, 364, 3796, 420, 294, 527, 1406, 13, 51264], "temperature": 0.0,
  "avg_logprob": -0.1634552323973024, "compression_ratio": 1.7142857142857142, "no_speech_prob":
  0.06491108238697052}, {"id": 296, "seek": 423932, "start": 4258.32, "end": 4265.32,
  "text": " give your feedback don''t be a gentle with us we are trying you know to
  build.", "tokens": [51314, 976, 428, 5824, 500, 380, 312, 257, 6424, 365, 505, 321,
  366, 1382, 291, 458, 281, 1322, 13, 51664], "temperature": 0.0, "avg_logprob": -0.1634552323973024,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.06491108238697052},
  {"id": 297, "seek": 426532, "start": 4266.32, "end": 4269.32, "text": " things that
  developers would like and.", "tokens": [50414, 721, 300, 8849, 576, 411, 293, 13,
  50564], "temperature": 0.0, "avg_logprob": -0.14582645359323987, "compression_ratio":
  1.58, "no_speech_prob": 0.026000134646892548}, {"id": 298, "seek": 426532, "start":
  4270.32, "end": 4281.32, "text": " we are very focused on the customer so this is
  the first announcement and every feedback is valuable next year we will launch our
  second generation where we can offer.", "tokens": [50614, 321, 366, 588, 5178, 322,
  264, 5474, 370, 341, 307, 264, 700, 12847, 293, 633, 5824, 307, 8263, 958, 1064,
  321, 486, 4025, 527, 1150, 5125, 689, 321, 393, 2626, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.14582645359323987, "compression_ratio": 1.58, "no_speech_prob":
  0.026000134646892548}, {"id": 299, "seek": 426532, "start": 4282.32, "end": 4293.32,
  "text": " better performance more than 10x we have a few new implementations and
  in terms of performance and hopefully.", "tokens": [51214, 1101, 3389, 544, 813,
  1266, 87, 321, 362, 257, 1326, 777, 4445, 763, 293, 294, 2115, 295, 3389, 293, 4696,
  13, 51764], "temperature": 0.0, "avg_logprob": -0.14582645359323987, "compression_ratio":
  1.58, "no_speech_prob": 0.026000134646892548}, {"id": 300, "seek": 429332, "start":
  4294.32, "end": 4296.32, "text": " at the beginning of.", "tokens": [50414, 412,
  264, 2863, 295, 13, 50514], "temperature": 0.0, "avg_logprob": -0.18840161809381448,
  "compression_ratio": 1.4794520547945205, "no_speech_prob": 0.019750285893678665},
  {"id": 301, "seek": 429332, "start": 4296.32, "end": 4307.32, "text": " 2023 we
  will release our python compiler and some other cool stuff so we are working on
  a few vectors if I may use.", "tokens": [50514, 44377, 321, 486, 4374, 527, 38797,
  31958, 293, 512, 661, 1627, 1507, 370, 321, 366, 1364, 322, 257, 1326, 18875, 498,
  286, 815, 764, 13, 51064], "temperature": 0.0, "avg_logprob": -0.18840161809381448,
  "compression_ratio": 1.4794520547945205, "no_speech_prob": 0.019750285893678665},
  {"id": 302, "seek": 429332, "start": 4307.32, "end": 4314.32, "text": " vectors
  and yeah on the software on the hardware on the system user experience.", "tokens":
  [51064, 18875, 293, 1338, 322, 264, 4722, 322, 264, 8837, 322, 264, 1185, 4195,
  1752, 13, 51414], "temperature": 0.0, "avg_logprob": -0.18840161809381448, "compression_ratio":
  1.4794520547945205, "no_speech_prob": 0.019750285893678665}, {"id": 303, "seek":
  431432, "start": 4315.32, "end": 4319.32, "text": " And the user interface and to
  simplify it.", "tokens": [50414, 400, 264, 4195, 9226, 293, 281, 20460, 309, 13,
  50614], "temperature": 0.0, "avg_logprob": -0.1834882762697008, "compression_ratio":
  1.5642458100558658, "no_speech_prob": 0.03493248298764229}, {"id": 304, "seek":
  431432, "start": 4320.32, "end": 4326.32, "text": " yeah so this is the things that
  we are working right now and we will be happy to be in touch.", "tokens": [50664,
  1338, 370, 341, 307, 264, 721, 300, 321, 366, 1364, 558, 586, 293, 321, 486, 312,
  2055, 281, 312, 294, 2557, 13, 50964], "temperature": 0.0, "avg_logprob": -0.1834882762697008,
  "compression_ratio": 1.5642458100558658, "no_speech_prob": 0.03493248298764229},
  {"id": 305, "seek": 431432, "start": 4327.32, "end": 4335.32, "text": " sounds great
  thanks you have looks like your plate is full of really exciting things so all the
  best.", "tokens": [51014, 3263, 869, 3231, 291, 362, 1542, 411, 428, 5924, 307,
  1577, 295, 534, 4670, 721, 370, 439, 264, 1151, 13, 51414], "temperature": 0.0,
  "avg_logprob": -0.1834882762697008, "compression_ratio": 1.5642458100558658, "no_speech_prob":
  0.03493248298764229}, {"id": 306, "seek": 431432, "start": 4335.32, "end": 4339.32,
  "text": " to you and your team i know some of them.", "tokens": [51414, 281, 291,
  293, 428, 1469, 741, 458, 512, 295, 552, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.1834882762697008, "compression_ratio": 1.5642458100558658, "no_speech_prob":
  0.03493248298764229}, {"id": 307, "seek": 433932, "start": 4340.32, "end": 4350.32,
  "text": " yeah it''s it''s amazing that you guys are building this and i''m really
  looking forward to gen 2 of of the APU hardware as well.", "tokens": [50414, 1338,
  309, 311, 309, 311, 2243, 300, 291, 1074, 366, 2390, 341, 293, 741, 478, 534, 1237,
  2128, 281, 1049, 568, 295, 295, 264, 5372, 52, 8837, 382, 731, 13, 50914], "temperature":
  0.0, "avg_logprob": -0.27265625, "compression_ratio": 1.6968325791855203, "no_speech_prob":
  0.05698372796177864}, {"id": 308, "seek": 433932, "start": 4351.32, "end": 4356.32,
  "text": " yeah and all the best we will stay in touch thank you very much for this
  episode.", "tokens": [50964, 1338, 293, 439, 264, 1151, 321, 486, 1754, 294, 2557,
  1309, 291, 588, 709, 337, 341, 3500, 13, 51214], "temperature": 0.0, "avg_logprob":
  -0.27265625, "compression_ratio": 1.6968325791855203, "no_speech_prob": 0.05698372796177864},
  {"id": 309, "seek": 433932, "start": 4358.32, "end": 4368.32, "text": " yeah thank
  you very much the mid tree was a pleasure talking with you you know super interesting
  stuff I can you know talk for hours about this the man you know it''s.", "tokens":
  [51314, 1338, 1309, 291, 588, 709, 264, 2062, 4230, 390, 257, 6834, 1417, 365, 291,
  291, 458, 1687, 1880, 1507, 286, 393, 291, 458, 751, 337, 2496, 466, 341, 264, 587,
  291, 458, 309, 311, 13, 51814], "temperature": 0.0, "avg_logprob": -0.27265625,
  "compression_ratio": 1.6968325791855203, "no_speech_prob": 0.05698372796177864},
  {"id": 310, "seek": 436932, "start": 4369.32, "end": 4376.32, "text": " i''m excited
  that working this domain and really looking forward to you know.", "tokens": [50364,
  741, 478, 2919, 300, 1364, 341, 9274, 293, 534, 1237, 2128, 281, 291, 458, 13, 50714],
  "temperature": 0.0, "avg_logprob": -0.3031829062928545, "compression_ratio": 1.4596774193548387,
  "no_speech_prob": 0.006817470770329237}, {"id": 311, "seek": 436932, "start": 4376.32,
  "end": 4381.32, "text": " hear from the community fantastic thanks so much and if.",
  "tokens": [50714, 1568, 490, 264, 1768, 5456, 3231, 370, 709, 293, 498, 13, 50964],
  "temperature": 0.0, "avg_logprob": -0.3031829062928545, "compression_ratio": 1.4596774193548387,
  "no_speech_prob": 0.006817470770329237}, {"id": 312, "seek": 436932, "start": 4381.32,
  "end": 4383.32, "text": " thank you for now.", "tokens": [50964, 1309, 291, 337,
  586, 13, 51064], "temperature": 0.0, "avg_logprob": -0.3031829062928545, "compression_ratio":
  1.4596774193548387, "no_speech_prob": 0.006817470770329237}, {"id": 313, "seek":
  436932, "start": 4383.32, "end": 4386.32, "text": " thank you very much bye bye.",
  "tokens": [51064, 1309, 291, 588, 709, 6543, 6543, 13, 51214], "temperature": 0.0,
  "avg_logprob": -0.3031829062928545, "compression_ratio": 1.4596774193548387, "no_speech_prob":
  0.006817470770329237}, {"id": 314, "seek": 439932, "start": 4399.32, "end": 4410.32,
  "text": " music playing", "tokens": [50364, 1318, 2433, 50914], "temperature": 0.0,
  "avg_logprob": -0.9839839935302734, "compression_ratio": 0.6190476190476191, "no_speech_prob":
  0.8395236730575562}]'
---

Hello, vector podcast is here. We again continue to roll in this season 2 of this podcast. Today I have a very interesting guest, Yanny Vaknin, who is the director of product at Searchum. If you've read my blog post on not all vector databases, I made equal.
One of the vector databases, all like technologies, stood out. And it's a technology made by GSI, technology company. And it's implementing a hardware for vector search. It's very rare that this thing exists or this approach exists on the market today. And I'm super excited to talk to Yanny Vaknin.
How are you, Yanny Vaknin? Hey. Great. Thanks for having me, maybe, Mietri. Yeah. I'm really glad you joined and found time in your business schedule.
So can you first explain how searchum and GSI are related? And maybe at the same time, if you could traditionally introduce yourself and talk about your background and how you got here. Yeah. So maybe I will start with quick introduction. So I'm director of product at Searchum AI.
Searchum AI is a SaaS platform for ML search application, based on purpose build AI chip for search applications. Prior to this role, I've worked at AWS as a machine learning specialist where I've worked with broad spectrum of top t top tier tech companies.
Trying to help them in their machine learning domain. And I was super excited from the revolution of the like the fifth revolution, the AI revolution with cool stuff of NLP search. Unstructed data structure data. I've worked with various companies cyber, fintech e-commerce, etc.
I was co founder and CEO of deep sea AI, which was the first computer vision based system for open water drowning detection. So we are the SaaS solution of GSI. GSI acquired an Israeli startup a few years ago. And the founder is Dr. Avidan Krib, which is one of the smartest guy that I ever met.
And during this PhD, he invented a new concept. So traditionally, CPU is communicating with the memory and then you have like challenges of bottleneck, IO, etc. But when you build the new concept, you build a memory that is the processor. So all of the computation is happening inside the memory.
You can guess that when you're running heavy or intensive intensive memory applications, if all of the processing is happening inside the memory, you can get a single digit millisecond latency. Yeah, so GSI acquired the Israeli startup and we are based in Israel.
We have an R&D team of approximately 40 to 50 people. In order to scale it, we started searching AI because it's super hard to scale hardware. So today we are offering this unique hardware on the cloud. It can be AWS, GCP or any other cloud and customers can consume it as a SaaS platform.
Yeah, makes sense. But there is still an option to if I want to have a completely on-premise sort of like setup, right? In principle, I could have bought like the APU cards, APU being a associative processing unit. Cards and like install them similar to what I would do with GPU.
Is that right? Yeah, yeah, totally. Yeah, so there are two types of implementation. The first one is on-prem and the second is via the cloud.
There are various configurations and in terms of if for instance, customers that would like to consume it as an on-prem solution, there are various capabilities. And one of the major things about this hardware accelerator is the power consumption.
So comparing it to CPU or GPU, it is like can be 5% or 10% of the power consumption. So companies that are running heavy workloads of GPU and CPU, the total cost of ownership for them is the power consumption. And other factors.
So on-prem customers can reduce the infrastructure cost in terms of the total cost of ownership, power consumption, etc. Yeah, this is really cool. And I think it's not very frequently that we mentioned power consumption as one of the dimensions on this podcast.
I mean, I think it's crucial of course for the planet and also for the electricity bill. And how the electricity costs skyrocketing, you know, and I think it's quite important. Yeah, sorry.
No, I was just kind of alluding to this fact that it's very like you should not skip it in kind of assessing a system or like a vector search solution, right. Not only focusing entirely on the offering itself, like you should still worry about how it will scale in different dimensions.
I'm glad you guys also worry about the power consumption part. Yeah, low carbon footprint is a major issue right now and especially in Europe. Usually developers when they are launching the AWS instances, so they choose by parameters of virtual CPU, RAM, etc.
And they are not aware of the carbon footprint, but when you are running it on-prem, this is a major parameters and this is a key parameter to, you know, taking a decision what is the right platform or right is the right. Hardware for you.
So totally agree, but, you know, I believe in an agree with you, we should take it into consideration and assume for cloud providers to integrate cloud providers like AWS, GCP, Azure.
This can be, you know, critical for them and we are in conversation with some of the company of some of the cloud providers that I mentioned. Yeah, this sounds great.
If we move a little bit closer to the algorithm side, so this is a kind of like dedicated hardware and as far as I understood also based on our brain buzz, buzzwords presentation. This hardware can support not only vector search, but some other scenarios, right.
Like for image processing related tasks. So is there any kind of like constraint on what type of vector search algorithm you can implement or is it doesn't it doesn't have any constraint. Yeah, yeah.
So I think that the biggest challenge today is when you are developing hardly can develop like a state of the art hardware, but I think the major challenge is how do you integrate it with the community. And video I've done it. Very good with the CUDA and it should be part of the ecosystem.
So in terms of applications here, we have like another application for image processing, it is based on. So, say it's set light images and radar images and we can process it like faster in a few orders of magnitude comparing to Jeep and video GPU.
So, we have in the past we had a few other applications for a genome and the molecules and today we are. We would like to you know to focus on on the biggest challenges like I believe that you know searches and you know we can elaborate about it later on.
Search is still broken and this is a huge market and so our focus right now is on the search. And we actually have to spend it to other solutions as well like image processing and we already have a solution and a customer for this solution.
And then one of our efforts is to build an ecosystem around this so. Hopefully soon we will launch our Python compiler so developers can write their code on Python and then you know run it. Simulnglessly on on our APU without you know trying to learn a new framework or a new language.
So, this is another direction that we are working we are trying I think one of the biggest challenges today is you know to simplifying the technological stack for developers so they are working with the common frameworks or languages they don't want to learn it.
So, they they they would like you know to stay with the. With the languages that are familiar and you know the learning curve is not always. They don't always have time for you know to learn a new framework so we are trying to simplify the integration with their current stack.
One of our solution is is a plugin on top of elastic and open search and which they are offering a vector search today but and we can talk about it but. So we have a plugin on top of this.
Search applications because some of some of the customers would like you know to stay with their curing the last or open search so we built a plugin on top of it and we are. We are talking with search engines and vector database in order to implement.
Our solution with their solution and I think in terms of like the the landscape so we are we are not perceived the vector search engines and vector database as competitors.
My perception is that they are potential they are partners and better together and you know to give a greater value for their customers reducing the infrastructure cost and give.
So the lower latency with the same without sacrificing accuracy so yeah we are you know trying to be part of the ecosystem and you know to help them and. To help customer scale there and improve their scale their search applications yeah yeah this is interesting you touched on.
You know being like a competitor to vector database I think it's interesting topic in general because on one hand if you take all vector database players they kind of look at each other as competitors probably but at the same time as all of you players are sharing the.
 You know the approach the documentation the how you think about yourself I think it also helps cumulatively to the whole market but I wasn't also wanted to drill in a bit into this elastic search and open search plugin so essentially like what elastic search team has been doing recently and I think they released now some updates in version 8.
5 where you can you can do things like hybrid search right but this is all based on. On the. A and an implementation on top of Lucin so it's all inside Java so it kind of runs in the same gvm right. The approach that you you guys have implemented it's basically like a.
A vector search backend right which kind of runs somewhere else let's see if we're using the cloud offering but at the same time it feels like a sort of like native to elastic search so I don't need to do much right I just need to install the plugin of course I need to have credentials.
 And what I wanted to say is that it feels like you expand the capabilities of elastic search beyond what what it offers in a way that you can actually remove the load of vector search away from it to another back and right can you talk a bit more on the unit cost on on this kind of unit economy and and and sort of advantages of the approach that that you have implemented.
 Yeah, this is a great point actually so but we are trying to decouple storage and compute so let's say for instance customer with elastic or open search and they they're having like tens of clusters and they would like you know to scale it and to optimize it so we are running on top of of elastic and you can.
Our solution is kind of the compute for elastic so they can run and scale and reduce the infrastructure cost because you know all of these is is a is a question of how many machines do you run okay so you can get like 99.9 recall it and or accuracy.
And you can get like single digit millisecond latency but in terms of the infrastructure costs so you know one of the biggest challenges today for enterprises is the.
 The low margins due to heavy infrastructure applications so if you are running GPU on the cloud or like heavy machines with big machines with high memory it's great in terms of the business because it's great in terms of the dev team in terms of we are getting great performance high recall but again when you're moving and you're discussing on on the business side.
 So in terms of the margins and the profit of the companies and today it's a big issue you know with companies that are having the challenge of being profitable so we are trying and we add like a few benchmarks we are trying to reduce the infrastructure cost so instead of 10 machines it can be two machines and and our accelerator our.
For APU and with that you can you know scale it and you know one one other interesting thing is like many companies are talking about the scale challenge about the one billion scale challenge so and you know data is exploding right because you know today they are.
 80 zetabytes and 10 years ago it was like 16 so essentially like data is growing very fast and I assume that in the next couple of years it will grow exponentially and 90% of this data and the data that is created every year is unstructured so you know this is the cliche of finding a needle in a haystack.
 So in terms of and I assume more and more companies will face the scale challenge like above one billion and I know that this is a challenge for some of the search engine companies you know scaling to hundreds of millions and billions and I had a conversation with one of the biggest e-commerce in in Asia and he told me yeah our our challenges to scale they have like two billion.
Index and again the infrastructure cost is a major issue I read a post by Amazon's CFO and like a week ago and their focus right now is reducing the infrastructure cost for their customers and any solution that can reduce the infrastructure cost for enterprises I think it's a major issue for.
Not only R&D teams but business and decision-makers in enterprises.
Yeah well I will I will pull for that link so we can also include it in the in the show notes some of our listeners by the way find it quite educational to have all this additional links and study materials and I think we can also include that that's super super cool.
 So in a way like your challenges that you basically need to as you said there are low margins right for this big players everyone tries to stay profitable so in a way your challenges to not only fit into that narrow kind of window but also be profitable yourself right so like you like provide that acceleration.
What do you think where do you stand today on that I do you think there is a lot still to do or do you think it's already something that companies can try.
 Yeah so today we have like the first generation of our AI chip the APU the potential of improving our hardware and our bill of material of our hardware and generally speaking next year we launch our second generation so for instance if today we can you know in terms of performance we are talking about single double digit millisecond latency with one APU.
Next year we will launch our second generation it will be more than 10x faster so I think we are just scratching the tip of the iceberg so the I think that the hardware challenge is solved but.
You know every week we have like a new implementation and improving our performance on the software layer so we have a few layers we have the hardware layers so I spoke about it like the first generation and the second generation.
I believe that there there's a huge potential in terms of optimizing our software layer because it is. We are trying to reinvent search so. I think there's a huge potential on on the hardware side but I think we are just we are just we didn't even start to optimize our software performance.
Recently we found a new implementation to improve the latency by reduce the latency by 40% like it was two weeks ago so hopefully we will launch it to production in the upcoming in the next up upcoming weeks.
So and in terms of your question yeah I think we are just at the beginning and I believe that we can optimize both on the on the hardware and the software layer and hopefully it will be very profitable.
 Sounds great I mean in general it was since I have a had exposure to it as we implemented the image search demo it was quite interesting how you know how easy it was to set it up right so it like and and you don't need to worry about that hardware thing yeah it acts a little bit like a black box but on the other hand it's very scalable so.
 And you guys also have I will make sure to link this you also published the is called neural hashing algorithm right which you which you use one of the algorithms that you have implemented it would also be equal to drill in into that direction but I mean in general it was fairly straightforward how you know how we upload the data how it gets indexed and then how we can query.
 Yeah I was just thinking to take it a little bit deeper can you talk to some of the features you know many of the vector database players they say why do you need vector databases because first of all if you took files for example a similar framework you wouldn't have the filter support right and of course in.
In real application like such app you do need filters alongside the whatever retriever you implement right keyword or vector so can you talk a bit more about features and maybe also touch on the algorithms that you guys have implemented.
Yeah yeah so there are various types of features and implementations we are working with you know the common. Algorithms it can be either flat search for applications like it can be a face recognition where you need to.
Search any every record we have implementations of the a nm i vf and new implementation of hnsw on our apu and pre filter and other features one of one of our.
One of the areas that we would like to focus is as you mentioned is is to simplify so we can you know you can work with it as a as a black box and install the plugin and work with your.
With your technological stack and with your search application either elastic open search or a vector search engine or vector database.
 And pre filter as you mentioned is supported and I think that we should focus on simplifying this is our biggest challenge simplifying the work with our platform and creating more integrations and more connectors not not on the feature level but in terms of you know working with the the ecosystem this is this is our main.
We are in focus right now and again improving the performance because we are you know customer obsessed and we would like our customer to get the lowest infrastructure cost and with without sacrificing latency and. Sorry and the accuracy.
Yeah that makes sense and especially like to do this at scale right I know that some of the players they say that it's very rare that there are clients with more than you dozens of millions of items right but today you already mentioned that there are clients.
Which have you know more than a billion items maybe more than two billion items so do you think that going forward you will see more of these second you know type of players with more data or do you think that there is still a use for dedicated hardware for this kind of smaller scale players.
 Yeah yeah absolutely agree with you I think that in terms of the scale challenge we are we are working with with customers and some of them here as you mentioned like tens of billions but moving forward I think most of the enterprises and the big companies will move forward and they will scale to one billion 10 billion and maybe even more.
In terms of like the ecosystem so my two cents is that companies are stealing the concept of keyboard search for some applications TF IDF at bm 25 for some for some application it's a good solution and you know you don't need an hammer for a screw driver.
 So that's the problem right so for some use cases keyboard search is a good fit and this is like you know part of the concept of vibrate search and so I think we are still we're we're the beginning of the the vector search if I may call it the vector search revolution when you know where you can have the.
 Back concept like any unstructured data we were usually we are talking about text but there are broad areas that we could you know develop some cool stuff for as I mentioned genome audio video search we have a notebook with you know website notebook with video search and again the the there's a broad spectrum of applications that companies can develop some cool stuff cool stuff.
And we are you know excited to see brilliant ideas and start up that are developing applications on top of of these vector search applications.
Yeah you touch on that topic by the way which I also spoke to to some extent on the haystack conference in Berlin where I gave a keynote also make sure to give the link.
 Back turnbull said that let's stop calling it vector search because and I don't know how I really interested to really interested to hear your thoughts on that because in principle you you and I being product managers like if we think about some problem to solve right let's say we want to introduce I don't know question answering component in our search engines it's not like we would probably if we didn't know that we probably wouldn't say oh I know how to solve it it's vector search.
 And so instead he was saying you know let's call it relevance application right or relevance oriented application what's your broad take on this you touched on this as well like people are not yet aware of this revolution it's probably already happening but people don't know what to do with it right and I just yesterday saw it with from one user saying can you actually explain what what can I do with it.
So do you think that the world is still let's say the world of software development is still awakening to this new field.
 Yeah yeah absolutely I fully agree with you essentially when I'm talking with developers and I'm saying we are I'm talking again we are working on vector search they are like asking vector what and I think that most of the developers and this is one of the things that I'm going to do is I'm going to do it.
 And this is one of our challenges is to democratize AI and machine learning so in terms of technology my perspective and is that technology is an enabler if the best solution is vector search great it can you know outperform on on various applications but the technology on a product perspective so you are trying to create value I think that the first lesson of a product.
The second lesson of a product is to create value for your customer that's it simple as that and what is the technology and what is under the hood and what is inside the black box it really doesn't matter.
In terms of technology yeah there's you know and we are like it's a crazy time for developers in terms of the AI machine learning revolution stable diffusion generative generative AI and I've heard about that they are going open AI planning to launch the new GPT for.
 And the pace of innovation is is totally crazy so and it's really hard to keep it to keep it simple to simplify it when when people are asking you you know there's the grandmother test for startup state in plain English explain your idea in a plain English super challenging you know to simplify so when you know when developers or companies asking what is vector search I'm using the.
The example of you know transforming words in the case of text to numbers it's easy for us to compare numbers right we know that three is is close or similar to four right but what is the connection between king and queen okay so how do you represent it as a number.
 So if you if you are trying again again I'm trying to super simplified if you are trying to build an equation what is the connection between king and queen so you can say king plus men minus woman equals to queen so you are you're trying to represent it as numbers so this is the concept of vector you are representing I'm going to say.
 So I'm trying to make sure that you are understanding and unstructured data and it can be you know with image image embedding etc and then I think like you know most of the tech companies today their core technology is search okay let's take if you are looking for a movie it's it's Netflix if you are would like you know to hear something cool or your podcast so you are running query on Spotify vector podcast and you will get the.
 Dmitry's podcast you would like to buy a dress or and you you are trying to do it very simple you don't usually more more of the let's take for instance e-commerce right so most of the consumers don't have the time and the patient to run you know SQL queries you know filter these filter that they would like to write it in a simple English or or in a different language okay yeah so let's take for an example and.
 Girl in Asia she would like to purchase a red and white short sleeve dress up until the the vector search revolution she didn't had the option to do it so usually she will get like a similar result it will not always be red and white with short sleeve dress and what about the challenge of the language okay so if our English is not so great and she would like to purchase something.
 An Amazon eBay or any other e-commerce so the challenge of language so essentially vector search is breaking the barrier of the language and the the barrier of understanding what is your what is your question or what is your query so I think that in terms of you know and there's a broad discussion about it democratizing AI what is the added value of.
 AI so you know you have like autonomous cars and this is great but you know breaking barriers the language barrier with the multilingual model and and some other cool stuff this is this is I think something that is doing really good for the ecosystem and for consumer and the people that you know they have like a barrier of a language so.
This is a great example what is the added value of vector search yeah I agree I mean all of the examples that you brought up you know if you if you look at how you would tackle I don't know like red short sleeve dress with the more traditional approach I guess you will need to build some kind of.
 Query understanding system but even then like even if after you've built it let's say you you will run filters on your data right but that that also means you do need to have the filters but but if you don't have them if you don't have the values in those fields in your documents right so what if you want you have like and this is by the way not.
 It's very unusual like I used to see I used to oversee a project in e-commerce space where we would get data from new providers all the time right so one of the issues was to map them back to our ontology but at the same time they would they would miss a lot of like field values right so what would you put there so they give you some description and then they give you the image on a set of images.
So like with with conventional not conventional but like more traditional approach of search right keyword search you're kind of like stuck right what would you do there and I guess of course people do solve it in some way but. Instead you could just apply vector search right and and.
Even though I say just there is still some challenge for example with model fine tuning and things like that can you talk a bit more to this maybe new challenges that this field opens of course it gives us.
opportunities it gives us advantages it solves some you know painstaking issues that we had before but what do we need to focus on going forward then once we deploy such systems beyond only hardware part but also like on this algorithm side.
Yeah you know this is this is a great question because it resonates with one of your blog post recent blog post where you published the Google's research about e-commerce companies in the US losing 300 billion dollars due to search abandonment in the US only.
 And again this is crazy number because if you have like I would like to buy a green polo shirt and I really want to buy a green polo shirt and the e-commerce got this green polo shirt inside in the in the warehouse or in the inventory and they can find the match we can find the match for this for this challenge.
This is this is the you challenge but in terms of of and again this is just one one example but you know our mission is to back to break this barrier for for developers it's not only e-commerce so expanding it to searching blocks okay if you would like to find.
And anomaly or you would like to understand what is the root cause when you're and you have like a software system logs and you would like to to understand and to find some anomalies or even fintech e-commerce and other areas I think that there's some cool stuff over there so one one way.
And you know to move forward is if you would like to use let's take for instance Siri I would like to buy with your audio right I would like to buy a red and white short sleeve dress below 100 dollar.
 Okay so you can this is a simple thing for you know consumers but you know technology wise this is the you challenge so the first challenge is to convert the audio to text and today there's you know you can convert it directly to vectors and then you can run this query but again you need to filter because if you want.
 Something that is below 100 so usually it's the price field so I think this is the biggest challenge that the consumers or people can communicate in a natural way with the computer with audio and say it very simple without you know trying to to run a complicated SQL queries etc so I think this is the like the the holy grail of of the audio.
 Machine learning to process this query and give you like the example and when you are purchase when you would like to purchase it on a certain website it will give you the place order page and you will get all of the details you will see the type of the dress and it will give you the right result and it will be below 100.
The 100 dollar and I think this is the way or this is a direction that we we can move forward with this technology.
Yeah yeah that sounds great so in principle like so so that our listeners that present a new one will understand is that vector search really opens doors to new types of data right new modalities as they say so like.
 Previously it was maybe only text modality even if you saw pictures on the on the monitor or on your phone as you know as response to your query it doesn't necessarily mean that that query really was kind of grasping the best parts of that image like it would actually understand what what is in the image but with vector search you can also implement that and for example using clip model or some other model where you can.
Really. Infer meaning from that picture right and what you are saying is that in the future and maybe this is to some extent happening already is that we can also cross modalities between voice and text right so like what I'm saying it can it can represent as a vector and then.
Find an image or find a video right it's like a lot of applications.
 Yeah yeah yeah totally yeah exactly and you know if you are working with your Instagram and you found like a nice celeb that is wearing a nice dress and you would like to buy something that is similar so with image search you can find like a similar and find me the find me this dress or the most relevant dress or the most the closest dress the.
Closes example of this dress and yeah yeah there are various options you know this is just one example you know of how to monetize Instagram or a tick talk where you know consumers can. Watch their favorite. them.
The celeb that they are following and if they were seeing something this is great so I want to purchase it and in terms of monetization and in terms of the added value of the customer take take this you take this platform says that.
Any commerce platform okay this is like a fresh concept but this is ways this is a way for companies to monetize the platform it's not a social media it can be. e-commerce and it can be super simple because you know up until now they they've seen like a nice dress or a nice.
A shirt but they cannot do with it they cannot purchase it they don't know how to explain to the machine or the computer. What what is the type of the of the clothing that they would like to buy so yeah that there are various options and yeah i'm eager to see what are the applications.
That you know developers and the entrepreneurs will develop with this technology. Yeah that sounds great one of the apps that you just kind of reminded me of is I think it was James Briggs who built the kind of simple demo.
Using the recent model called whisper from open AI so you can actually you know like on YouTube today how you find things is basically mostly based on titles. I believe this is what people type.
But then he built a demo where he can land in the precise time code which contains the answer to your question you know that could be really interesting like it just to think about it at the unlocks even more what you said in the beginning like we have this is a device of data and so on.
But like we are not able to unlock the data right it's just sitting there waiting to be discovered so to say.
Yeah it's really cool I wanted to spend a bit of time on the search topic itself so you did mention this search abandonment issue which is like an e-commerce but but in general if we if we think about search field.
 On a much larger scale and I think Daniel tanky-lank also said about it that when search engine doesn't work you are blamed but when it does work you don't hear anything it's like people take it for granted it's kind of like water from the tap I guess right if it's the right analogy so what do you think of the search field in general like where do you think vector search field fits in and what's the role of this hybrid.
Approach where you have this keywords versus which are more familiar to users versus vector search so where would you take this yourself right as a product manager having unlimited resources where would you where would you go.
Yeah this is this is an interesting question yeah so I think that search is still an unsold problem.
And you know in order to find the right object or the right the the most accurate type of data we are still we have a lot of work to develop this ecosystem and you know to build the multimodals and multilingual and I think that the big tech companies are doing some great job with this.
With this stuff like open and I and the other folks and hybrid searches is is a is a very interesting concept I believe that we for some applications it can be a good a good way to solve their challenges but I think that the one of the most important.
Pilar is that you should and again I've learned that the data but yes that they are like the concept.
 Of moving backwards from the custom what is I don't have solution if we have a discussion with a customer we are asking what is the problem that you would like to solve and this is like you should be focused what what is the problem that you would like to solve like more than 50% of your discussion.
 And if you don't have a good fit it's not a good fit if you did the vector search technology is not a good fit we would say it to the customer we are not trying you know to fit into a space that you know keyword search is a great solution so I think it's the focus should be around the problem space so trying to figure out what is their pain point or what is their customers pain point.
 Is it the accuracy for some for some applications we we spoke with the fraud detection company and for their use case like keyword search was good enough solution great so go go go ahead and we don't want to disturb you so I think the focus should be around the the problem and the challenge and then again.
 Focus on what is the the challenge that they would like to achieve or what is the what is the potential of the solution and sometimes we are talking about recall is it the most important parameter for some of the for some of the customers and 90% is good enough for the use case but for mission mission critically should be mission critical applications.
It should be 99.99% right so I think it's it's a matter to some extent it's it's an issue of what is the problem and what is the KPI that you would like to achieve.
Would you like to optimize the recall great we would optimize it if you would like to reduce the infrastructure cost with the same KPI recall of X and you have latency of X and it's a good enough and maybe it can be latency so.
For instance, Amazon published a research that every 100 milliseconds let it see equals to 1% of the revenue so if the revenue is $1 billion then 100 milliseconds of latency equals to 10 million. This is a huge impact for companies.
So I think the main the main question is what is the problem that you would like to solve what is the pain point and starting from the customer and then work backwards to find if you have like a good solution and if a solution is a is a good fit.
And again, there are various concept keyword search is a great solution vector search is a great solution and I read searches a good solution. The the big I think the biggest question is what is the problem that the customer would like to solve.
Yeah, I think you put it really brilliantly because it's very easy to get into my new show of tweaking things like on the software side and saying I have the best algorithm right or I have the fastest or whatever.
But then if you if you forget that I guess the most important dimension for your customer maybe it's power consumption that we mentioned previously or something else right. But but also what you said.
How you can think like the way Amazon did it right that they think big right they say okay of all these dollars we we earned how much actually we wasted on on you know latency and also how much of clients we kind of lost right.
Or potential clients because if if the server doesn't respond soon enough then and it's only average right 100 millisecond maybe for some it looks like more like closer to second including their own internet connection.
And they might just give up and say hard this is not working today I will go and check something else I will forget about what I wanted to buy. So right. Yeah, this is very interesting.
 Also like you you you you you brought up some some topic behind the scenes like on the role of human in this whole loop I also want to pick your brain on that you know there is one direction in AI saying this is going to be a whole automatic thing you don't need to do anything it will decide for you which is also by the way a little bit worrisome if the yeah it's going to decide for everything.
 But but even going back to earth like where do you see humans will play a role in some sense we are slower right then machines in some sense I think we are still faster for example in creating things but even they are the machines that tapping into it but like connected with MLOPS topics also machine learning operations and connected with bias and data that we collect to tell you what the real thing is.
Train models or maybe some other dimension that I'm missing that you think human is going to play a role can you can you expand a little bit on that yeah. So actually I wrote about it in medium about the MLOPS challenge and and the human in the loop and what is the place of human in the loop.
Essentially I believe that machine learning is a decision support system okay I believe that the human as.
As a huge or important significant role in helping the machine to decide and where a good way to automate processes is to use the machine and to set a threshold okay so for instance if you were. We're talking about cyber cyber security challenge so you can decide that the threshold is below 0.
7 is a good enough and you don't that like the sock teams will will check this anomaly and then again you are reducing.
The main power cost because you are automating and you are sending queries or a stream of data to analyze that they would you know fine tune the model and then you can create a learning model right so it's a human in the loop the human is giving a feedback to the model and then you can.
Detect data drift if it's not automated you know there there are solutions that are good that you know data drift etc but again. My my two cents is that fully automated systems we are not ready yet for it and I believe that in order and then again we don't like all of the anomalies will be.
 Tested by a human again because you have the false positive fatigue or a lot fatigue in in the cyber domain so I believe that a combination or the hybrid model where you can define a certain threshold and send it to a human to run a sanity check and you know i've worked with many data scientist and.
The the always like you know to improve the state of the art model and improve the f 1 score for from 99 to 99.9.
But what is the the impact on the business is it is it important enough for the business to invest resources in this in this in this research or not like five data scientists are running and testing and optimizing the hyper parameter.
For months but what is the business what is the impact on the business so essentially I believe that and and again it resonates with the search domain so I believe that companies that will be smart enough to integrate the human and the loop mechanism where they can find you know.
 Measure KPIs like the clicks on on the on the first result how many clicks on the first result or any other KPIs and then if it's a good model then great we should keep it you know if it's not broken don't touch it but if something is not working the mechanism or something that there's a drift in the data so we can you know.
Research research it again and find what is the root cause and then. Human will detect or machine will will detect it so I believe that this this is the question of of layers so you have like the machine learning layer and then.
ML obstacles like you can you know auto ML and the hyper parameter optimization and data drift and model drift and other tools but. We are I don't think we are ready to fully automated all of the process and yeah this is like a great question for instance autonomous cars are we ready yet or not.
This is I think this is the the challenge of the data science ecosystem in the next years. Yeah I think it's also like.
Our psychological readiness to accept this solutions rights maybe previously when we didn't have let's say elevator so everyone was walking up the stairs and no one really complained but then when the first elevator arrived maybe people were like really.
You know looking at it with open eyes and like what is this should they trust it will I get interrupt in it or something you know. So the same I think goes to what you just raised as the.
You know self driving cars you know I think it was ill and mask saying I don't remember exactly the stats but something let's say one and a thousand. You know so it avoids basically nine hundred ninety nine you know cases bad cases so would you trust that or do you need like it to be.
 Even bigger number and so on so forth so like complete thousands so it's never mistaken but what about cases where it's hard to decide right like you inevitably going to crush the car now you need to choose where like to the human or maybe to to the I don't know for to the tree or something which hurts the driver and stuff like that right so.
 So this I think the same the same decisions that we would be making as humans then algorithms should make and I think what humans or humanity has hard time with is probably accepting the fact that someone else is going to make the decision right so yeah it's yeah it's a revolution you know you mentioned the elevator but you know the famous story of the end report with the horses and the cars why should we.
Need the cars right so it's a it's a revolution I think that most of.
The features that we are working on improving the quality of life and people you know can automate processes and and on focus in their you know in their family and instead of doing some complicated task they can you know focus their.
Time on innovation or you know play football or soccer whatever they want and you know makes our life easier to some extent yeah and we believe collectively that vector search is going to help there i.
 I really like also to of course ask this my philosophical question but before that i was thinking like what do you think on the field in general the vector search and maybe including search and machine learning what do a lot is happening but what do you think is still missing from your perspective.
Something that maybe we need to fix.
To be more efficient yeah I think it's it's it's education simplifying the concept of search I think this is the should be our main focus so education generating content and again I really like the grandmother test simplifying not like super complicated mathematical equations etc.
So I think it's education we are you know the ecosystem is trying to generate high quality content videos a YouTube blog post we we are trying to contribute to this effort as well.
 We are doing enough and you know it can be like high school or universities so but again this is vector search is technology it's an enabler it's not the it's not the objective it's not the it's not the target but in order to unlock the potential of vector search and machine learning and transform and so on all of these cool stuff we should.
 Invest some of our resources in education and learning and training and you know unlock the potential that every developer can kill build a vector vector search based application in in every field like it can be as I mentioned before health care, care, FinTech education and any other domain that manufacturing or any other domain that you would like that is bigger to solve some problem I think we should you know simplified similar to the revolution of auto ml so instead of you know processing and labeling images etc.
 You have like an auto auto ml tool or solution and your provision you provision the data labeling it and then the under the hood the auto ml model will run the experiments find the right algorithm find the right hyper parameters optimizing them you can define what is the what is the KPI that you would like to optimize.
 If it's f1 score or recall or whatever and then you will get the model and if you would like to deep dive you will get the code so you know generating models with low code so this is another and another area that we should focus in but you know to some extent I believe that education training and generating high quality content.
So it should be our focus right now.
 Yeah I think you put it really well and I would probably even add to this that yes there is content which kind of like promotes someone's solution right but at the same time you really want to educate like why should people even care about your solution so you need to take few steps back and explain what are we talking about.
 You know what problems exist that you are trying to that you are targeting right so I still if I was asking the same question to myself I still see a lot of content which is much more promotional than it should be because in the beginning of this revolution you still need to explain what is happening what the hell is going on you know why why because the reaction could be also from the incumbent players that they will say no this is not.
No this is not no this is not where things are going they will go go back to their clients and say the same but like you should not position it that way you should you should explain as you said like start from the problem right start from what is your actual business and product target.
 And I guess this is not something that many engineers asking themselves some of them some of the best that I know do some of the best data scientists do as well they don't code before they understood what is being asked of them and I think it's an amazing skill and this is exactly where education also helps like why should also data scientists or engineers care about this new new field.
Yeah, yeah, this is super important and yeah, we should honestly we should you know when I'm saying again internally we should improve the quality of the content and not trying you know to sell our solution just to explain for software developer without the background in machine learning.
 And to simplify it for him and to explain what is the concept what is the trade off between the concept and again to give him the option to understand what is happening and issue decide what is the best tool for him is it a screwdriver is it an hammer it will understand the bits and bytes but and the trade off and and give him the the full picture about what what are the problems.
Yeah, I think it's a great question. It was in cons of every solution and you know you will take the decision.
Yeah, exactly and I think if we decade more some of the players doing doing really great job there and I am looking forward also to see some blog posts you already mentioned the notebooks that you guys are publishing on your website and I believe that was searching website right.
Now that I learned that you really care about the topic I think it's important to create and share and maybe educate the educators and give the example so I think this is really great.
Yeah, yeah, one example the great blog was that one of our software developer wrote is how to optimize open search workloads.
 So again it's not we have a plugin on top of it, but he wrote about what are the options without you know writing about our solution and what are the options out they can our customers can optimize it and another interesting blog post that we will publish soon is you know benchmarking one of the things that we should improve in our ecosystem is to decide on on a standard tool that will.
 Help us to decide what is the KPI and the benchmark there are various benchmark over there i'm familiar we are familiar with rally and the elastic benchmark i haven't seen like a good benchmark industry standard in in the vector search there was the challenge of big a and one year ago two years ago, but again I don't think we have.
Good tool today, but so one of our developers wrote out to run the benchmark tool so it was like open search benchmark how to use this benchmark and what is the.
Beats and bytes and tips how to understand the benchmark tools so yeah I think that starting from the education and then offering customers to check your solution yeah sounds great i think maybe even by the time this podcast is published we have that new blog as well.
 Hey, I'm really excited to be chatting to you today, I mean it's attached a lot of deep topics i'm sure we could have gone for longer, but I was also really curious to ask you this magical why question you know the same way as you said don't think about software think about the problem that you're solving the reason i'm asking why question is because I truly believe.
 But if you don't understand why you do things then you're kind of like flying through things right so you might as well regret some sometime later maybe you train the muscle but still i don't think it's a good sensible approach in your life so i'm really interested given all your experience in in machine learning and product management software development why are you excited to work on vector search search whatever is it that you do day today.
Yeah, I think this is a great question I really like the why combinator accelerator approach for building products build something that customers like or love and essentially you know we are building some trying to build some cool stuff and make.
 People's life easier happier i gave an example of the girl from Asia so this is this is I think one of our mission but it's not only the girl from Asia that would like to purchase a red short sleeve dress it's the DevOps that is trying to find the right log and instead of working it for hours it will take him.
Seconds okay so essentially our mission and i'm excited that i'm working on this topic it's to make the the consumers businesses and enterprises life easier. And so I think it's a very simple statement of the why and I believe that this is this is my mission or this is our mission.
And and to some extent I think that this is like a doing good perspective so you know you have like. gambling company is.
building some stuff and building applications and i'm my approach is you know building things that will help the humanity so i'm exciting that this is the things that i'm working on and by the way this was in my previous startup when we tried to save life right drowning detection.
and you issue residential pool open water and you know save life and if we can you know save life maybe for health applications. detecting cancer with the image embeddings or some other cool stuff i'm super excited that this is the domain that we are working on.
yeah this is this is very relatable in this fantastic that you're bringing this up you know how we can actually improve life. beside building. great products or products that sell.
This is this is amazing and to conclude is there any announcement that you want to make from the from your side of from search room. A. I. yeah yeah so i'm very excited because we are building.
some cool stuff so the first one we launch our search you may i platform where we offer customers a free tier to check our. platform and again it's not.
fully working we are not supporting all of the features but it this is very important it is very important for us to get your feedback so i encourage you to check it and to. send me an email or send my team an email or in our support.
give your feedback don't be a gentle with us we are trying you know to build. things that developers would like and. we are very focused on the customer so this is the first announcement and every feedback is valuable next year we will launch our second generation where we can offer.
better performance more than 10x we have a few new implementations and in terms of performance and hopefully. at the beginning of. 2023 we will release our python compiler and some other cool stuff so we are working on a few vectors if I may use.
vectors and yeah on the software on the hardware on the system user experience. And the user interface and to simplify it. yeah so this is the things that we are working right now and we will be happy to be in touch.
sounds great thanks you have looks like your plate is full of really exciting things so all the best. to you and your team i know some of them. yeah it's it's amazing that you guys are building this and i'm really looking forward to gen 2 of of the APU hardware as well.
yeah and all the best we will stay in touch thank you very much for this episode. yeah thank you very much the mid tree was a pleasure talking with you you know super interesting stuff I can you know talk for hours about this the man you know it's.
i'm excited that working this domain and really looking forward to you know. hear from the community fantastic thanks so much and if. thank you for now. thank you very much bye bye. music playing