---
description: '<p>00:00 Introduction</p><p>01:10 Max''s deep experience in search and
  how he transitioned from structured data</p><p>08:28 Query-term dependence problem
  and Max''s perception of the Vector Search field</p><p>12:46 Is vector search a
  solution looking for a problem?</p><p>20:16 How to move embeddings computation from
  GPU to CPU and retain GPU latency?</p><p>27:51 Plug-in neural model into Java? Example
  with a Hugging Face model</p><p>33:02 Web-server Mighty and its philosophy</p><p>35:33
  How Mighty compares to in-DB embedding layer, like Weavite or Vespa</p><p>39:40
  The importance of fault-tolerance in search backends</p><p>43:31 Unit economics
  of Mighty</p><p>50:18 Mighty distribution and supported operating systems</p><p>54:57
  The secret sauce behind Mighty''s insane fast-ness</p><p>59:48 What a customer is
  paying for when buying Mighty</p><p>1:01:45 How will Max track the usage of Mighty:
  is it commercial or research use?</p><p>1:04:39 Role of Open Source Community to
  grow business</p><p>1:10:58 Max''s vision for Mighty connectors to popular vector
  databases</p><p>1:18:09 What tooling is missing beyond Mighty in vector search pipelines</p><p>1:22:34
  Fine-tuning models, metric learning and Max''s call for partnerships</p><p>1:26:37
  MLOps perspective of neural pipelines and Mighty''s role in it</p><p>1:30:04 Mighty
  vs AWS Inferentia vs Hugging Face Infinity</p><p>1:35:50 What''s left in ML for
  those who are not into Python</p><p>1:40:50 The philosophical (and magical) question
  of WHY</p><p>1:48:15 Announcements from Max</p><p>25% discount for the first year
  of using Mighty in your great product / project with promo code VECTOR:</p><p><a
  href="https://bit.ly/3QekTWE">https://bit.ly/3QekTWE</a></p><p>Show notes:</p><p>-
  Max''s blog about BERT and search relevance: <a href="https://opensourceconnections.com/blog/2019/11/05/understanding-bert-and-search-relevance/">https://opensourceconnections.com/blog/2019/11/05/understanding-bert-and-search-relevance/</a></p><p></p><p>-
  Case study and unit economics of Mighty: <a href="https://max.io/blog/encoding-the-federal-register.html">https://max.io/blog/encoding-the-federal-register.html</a></p><p></p><p>-
  Not All Vector Databases Are Made Equal: <a href="https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696">https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696</a></p><p></p><p>Watch
  on YouTube: <a href="https://youtu.be/LnF4hbl1cE4">https://youtu.be/LnF4hbl1cE4</a></p>'
image_url: https://media.rss.com/vector-podcast/20220616_060650_51fed3f5cf98ff1ddb61cc17e11e43be.jpg
pub_date: Thu, 16 Jun 2022 18:27:50 GMT
title: Max Irwin - Founder, MAX.IO - On economics of scale in embedding computation
  with Mighty
url: https://rss.com/podcasts/vector-podcast/522301
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 23.0, "text": " Hello,
  vector podcast is here.", "tokens": [50364, 2425, 11, 8062, 7367, 307, 510, 13,
  51514], "temperature": 0.0, "avg_logprob": -0.7542389956387606, "compression_ratio":
  0.7894736842105263, "no_speech_prob": 0.11571534723043442}, {"id": 1, "seek": 2300,
  "start": 24.0, "end": 27.0, "text": " And today I''m going to be talking to Max
  Irwin.", "tokens": [50414, 400, 965, 286, 478, 516, 281, 312, 1417, 281, 7402, 9151,
  9136, 13, 50564], "temperature": 0.0, "avg_logprob": -0.20569798946380616, "compression_ratio":
  1.4684210526315788, "no_speech_prob": 0.6937023401260376}, {"id": 2, "seek": 2300,
  "start": 27.0, "end": 32.0, "text": " He''s this star in the search engine business
  in search engine world.", "tokens": [50564, 634, 311, 341, 3543, 294, 264, 3164,
  2848, 1606, 294, 3164, 2848, 1002, 13, 50814], "temperature": 0.0, "avg_logprob":
  -0.20569798946380616, "compression_ratio": 1.4684210526315788, "no_speech_prob":
  0.6937023401260376}, {"id": 3, "seek": 2300, "start": 32.0, "end": 36.0, "text":
  " He has been doubling also in NLP a lot.", "tokens": [50814, 634, 575, 668, 33651,
  611, 294, 426, 45196, 257, 688, 13, 51014], "temperature": 0.0, "avg_logprob": -0.20569798946380616,
  "compression_ratio": 1.4684210526315788, "no_speech_prob": 0.6937023401260376},
  {"id": 4, "seek": 2300, "start": 36.0, "end": 39.0, "text": " I don''t know 20 years.
  It''s huge amount of time.", "tokens": [51014, 286, 500, 380, 458, 945, 924, 13,
  467, 311, 2603, 2372, 295, 565, 13, 51164], "temperature": 0.0, "avg_logprob": -0.20569798946380616,
  "compression_ratio": 1.4684210526315788, "no_speech_prob": 0.6937023401260376},
  {"id": 5, "seek": 2300, "start": 39.0, "end": 49.0, "text": " And I mean, he has
  been consulting in this space, also building products.", "tokens": [51164, 400,
  286, 914, 11, 415, 575, 668, 23682, 294, 341, 1901, 11, 611, 2390, 3383, 13, 51664],
  "temperature": 0.0, "avg_logprob": -0.20569798946380616, "compression_ratio": 1.4684210526315788,
  "no_speech_prob": 0.6937023401260376}, {"id": 6, "seek": 4900, "start": 49.0, "end":
  53.0, "text": " And now he''s focusing on building his new product.", "tokens":
  [50364, 400, 586, 415, 311, 8416, 322, 2390, 702, 777, 1674, 13, 50564], "temperature":
  0.0, "avg_logprob": -0.12551216725949887, "compression_ratio": 1.5982905982905984,
  "no_speech_prob": 0.10351726412773132}, {"id": 7, "seek": 4900, "start": 53.0, "end":
  58.0, "text": " And he''s the founder of company called max.io, which is also a
  website.", "tokens": [50564, 400, 415, 311, 264, 14917, 295, 2237, 1219, 11469,
  13, 1004, 11, 597, 307, 611, 257, 3144, 13, 50814], "temperature": 0.0, "avg_logprob":
  -0.12551216725949887, "compression_ratio": 1.5982905982905984, "no_speech_prob":
  0.10351726412773132}, {"id": 8, "seek": 4900, "start": 58.0, "end": 62.0, "text":
  " You can go check it out. And he''s building a mighty inference server.", "tokens":
  [50814, 509, 393, 352, 1520, 309, 484, 13, 400, 415, 311, 2390, 257, 21556, 38253,
  7154, 13, 51014], "temperature": 0.0, "avg_logprob": -0.12551216725949887, "compression_ratio":
  1.5982905982905984, "no_speech_prob": 0.10351726412773132}, {"id": 9, "seek": 4900,
  "start": 62.0, "end": 66.0, "text": " And the number of other tools that I''m sure
  Max will talk about today.", "tokens": [51014, 400, 264, 1230, 295, 661, 3873, 300,
  286, 478, 988, 7402, 486, 751, 466, 965, 13, 51214], "temperature": 0.0, "avg_logprob":
  -0.12551216725949887, "compression_ratio": 1.5982905982905984, "no_speech_prob":
  0.10351726412773132}, {"id": 10, "seek": 4900, "start": 66.0, "end": 67.0, "text":
  " Hey, Max, how are you doing?", "tokens": [51214, 1911, 11, 7402, 11, 577, 366,
  291, 884, 30, 51264], "temperature": 0.0, "avg_logprob": -0.12551216725949887, "compression_ratio":
  1.5982905982905984, "no_speech_prob": 0.10351726412773132}, {"id": 11, "seek": 4900,
  "start": 67.0, "end": 69.0, "text": " I''m doing great. How are you?", "tokens":
  [51264, 286, 478, 884, 869, 13, 1012, 366, 291, 30, 51364], "temperature": 0.0,
  "avg_logprob": -0.12551216725949887, "compression_ratio": 1.5982905982905984, "no_speech_prob":
  0.10351726412773132}, {"id": 12, "seek": 4900, "start": 69.0, "end": 73.0, "text":
  " I''m great. And thanks so much for joining me today.", "tokens": [51364, 286,
  478, 869, 13, 400, 3231, 370, 709, 337, 5549, 385, 965, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.12551216725949887, "compression_ratio": 1.5982905982905984,
  "no_speech_prob": 0.10351726412773132}, {"id": 13, "seek": 7300, "start": 73.0,
  "end": 76.0, "text": " I''m very happy to be talking to you today.", "tokens": [50364,
  286, 478, 588, 2055, 281, 312, 1417, 281, 291, 965, 13, 50514], "temperature": 0.0,
  "avg_logprob": -0.3944159527214206, "compression_ratio": 2.151898734177215, "no_speech_prob":
  0.25695300102233887}, {"id": 14, "seek": 7300, "start": 76.0, "end": 79.0, "text":
  " I''m very happy to be talking to you today.", "tokens": [50514, 286, 478, 588,
  2055, 281, 312, 1417, 281, 291, 965, 13, 50664], "temperature": 0.0, "avg_logprob":
  -0.3944159527214206, "compression_ratio": 2.151898734177215, "no_speech_prob": 0.25695300102233887},
  {"id": 15, "seek": 7300, "start": 79.0, "end": 82.0, "text": " I''m very happy to
  be talking to you today.", "tokens": [50664, 286, 478, 588, 2055, 281, 312, 1417,
  281, 291, 965, 13, 50814], "temperature": 0.0, "avg_logprob": -0.3944159527214206,
  "compression_ratio": 2.151898734177215, "no_speech_prob": 0.25695300102233887},
  {"id": 16, "seek": 7300, "start": 82.0, "end": 84.0, "text": " I''m very happy to
  be talking to you today.", "tokens": [50814, 286, 478, 588, 2055, 281, 312, 1417,
  281, 291, 965, 13, 50914], "temperature": 0.0, "avg_logprob": -0.3944159527214206,
  "compression_ratio": 2.151898734177215, "no_speech_prob": 0.25695300102233887},
  {"id": 17, "seek": 7300, "start": 84.0, "end": 90.0, "text": " And I''m learning
  about my tea and all the things that you''re cooking there.", "tokens": [50914,
  400, 286, 478, 2539, 466, 452, 5817, 293, 439, 264, 721, 300, 291, 434, 6361, 456,
  13, 51214], "temperature": 0.0, "avg_logprob": -0.3944159527214206, "compression_ratio":
  2.151898734177215, "no_speech_prob": 0.25695300102233887}, {"id": 18, "seek": 7300,
  "start": 90.0, "end": 96.0, "text": " But I think as a tradition, could you start
  with introducing yourself first?", "tokens": [51214, 583, 286, 519, 382, 257, 6994,
  11, 727, 291, 722, 365, 15424, 1803, 700, 30, 51514], "temperature": 0.0, "avg_logprob":
  -0.3944159527214206, "compression_ratio": 2.151898734177215, "no_speech_prob": 0.25695300102233887},
  {"id": 19, "seek": 7300, "start": 96.0, "end": 98.0, "text": " Sure. Yeah. Hi.",
  "tokens": [51514, 4894, 13, 865, 13, 2421, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.3944159527214206, "compression_ratio": 2.151898734177215, "no_speech_prob": 0.25695300102233887},
  {"id": 20, "seek": 9800, "start": 98.0, "end": 101.0, "text": " So I''m good to
  go on my own business.", "tokens": [50364, 407, 286, 478, 665, 281, 352, 322, 452,
  1065, 1606, 13, 50514], "temperature": 0.6, "avg_logprob": -0.7845254224889419,
  "compression_ratio": 2.3445945945945947, "no_speech_prob": 0.12286259233951569},
  {"id": 21, "seek": 9800, "start": 101.0, "end": 104.0, "text": " I''m good to go
  on my own business.", "tokens": [50514, 286, 478, 665, 281, 352, 322, 452, 1065,
  1606, 13, 50664], "temperature": 0.6, "avg_logprob": -0.7845254224889419, "compression_ratio":
  2.3445945945945947, "no_speech_prob": 0.12286259233951569}, {"id": 22, "seek": 9800,
  "start": 104.0, "end": 105.0, "text": " So I''m a doctor.", "tokens": [50664, 407,
  286, 478, 257, 4631, 13, 50714], "temperature": 0.6, "avg_logprob": -0.7845254224889419,
  "compression_ratio": 2.3445945945945947, "no_speech_prob": 0.12286259233951569},
  {"id": 23, "seek": 9800, "start": 105.0, "end": 108.0, "text": " I''m a doctor.",
  "tokens": [50714, 286, 478, 257, 4631, 13, 50864], "temperature": 0.6, "avg_logprob":
  -0.7845254224889419, "compression_ratio": 2.3445945945945947, "no_speech_prob":
  0.12286259233951569}, {"id": 24, "seek": 9800, "start": 108.0, "end": 109.0, "text":
  " I''m a doctor.", "tokens": [50864, 286, 478, 257, 4631, 13, 50914], "temperature":
  0.6, "avg_logprob": -0.7845254224889419, "compression_ratio": 2.3445945945945947,
  "no_speech_prob": 0.12286259233951569}, {"id": 25, "seek": 9800, "start": 109.0,
  "end": 110.0, "text": " I''m a doctor.", "tokens": [50914, 286, 478, 257, 4631,
  13, 50964], "temperature": 0.6, "avg_logprob": -0.7845254224889419, "compression_ratio":
  2.3445945945945947, "no_speech_prob": 0.12286259233951569}, {"id": 26, "seek": 9800,
  "start": 110.0, "end": 112.0, "text": " I''m a doctor.", "tokens": [50964, 286,
  478, 257, 4631, 13, 51064], "temperature": 0.6, "avg_logprob": -0.7845254224889419,
  "compression_ratio": 2.3445945945945947, "no_speech_prob": 0.12286259233951569},
  {"id": 27, "seek": 9800, "start": 112.0, "end": 113.0, "text": " I''m a doctor.",
  "tokens": [51064, 286, 478, 257, 4631, 13, 51114], "temperature": 0.6, "avg_logprob":
  -0.7845254224889419, "compression_ratio": 2.3445945945945947, "no_speech_prob":
  0.12286259233951569}, {"id": 28, "seek": 9800, "start": 113.0, "end": 115.0, "text":
  " I''m a doctor.", "tokens": [51114, 286, 478, 257, 4631, 13, 51214], "temperature":
  0.6, "avg_logprob": -0.7845254224889419, "compression_ratio": 2.3445945945945947,
  "no_speech_prob": 0.12286259233951569}, {"id": 29, "seek": 9800, "start": 115.0,
  "end": 116.0, "text": " I''m a doctor.", "tokens": [51214, 286, 478, 257, 4631,
  13, 51264], "temperature": 0.6, "avg_logprob": -0.7845254224889419, "compression_ratio":
  2.3445945945945947, "no_speech_prob": 0.12286259233951569}, {"id": 30, "seek": 9800,
  "start": 116.0, "end": 117.0, "text": " I''m a doctor.", "tokens": [51264, 286,
  478, 257, 4631, 13, 51314], "temperature": 0.6, "avg_logprob": -0.7845254224889419,
  "compression_ratio": 2.3445945945945947, "no_speech_prob": 0.12286259233951569},
  {"id": 31, "seek": 9800, "start": 117.0, "end": 118.0, "text": " I''m a doctor.",
  "tokens": [51314, 286, 478, 257, 4631, 13, 51364], "temperature": 0.6, "avg_logprob":
  -0.7845254224889419, "compression_ratio": 2.3445945945945947, "no_speech_prob":
  0.12286259233951569}, {"id": 32, "seek": 9800, "start": 118.0, "end": 122.0, "text":
  " And sometimes I get a lot of things to do with my career.", "tokens": [51364,
  400, 2171, 286, 483, 257, 688, 295, 721, 281, 360, 365, 452, 3988, 13, 51564], "temperature":
  0.6, "avg_logprob": -0.7845254224889419, "compression_ratio": 2.3445945945945947,
  "no_speech_prob": 0.12286259233951569}, {"id": 33, "seek": 9800, "start": 122.0,
  "end": 126.0, "text": " In fact, when I was a younger, I didn''t do so well in my
  language course.", "tokens": [51564, 682, 1186, 11, 562, 286, 390, 257, 7037, 11,
  286, 994, 380, 360, 370, 731, 294, 452, 2856, 1164, 13, 51764], "temperature": 0.6,
  "avg_logprob": -0.7845254224889419, "compression_ratio": 2.3445945945945947, "no_speech_prob":
  0.12286259233951569}, {"id": 34, "seek": 12600, "start": 126.0, "end": 129.76, "text":
  " started in 2015-2016 with actual product development around NLP.", "tokens": [50364,
  1409, 294, 7546, 12, 41103, 365, 3539, 1674, 3250, 926, 426, 45196, 13, 50552],
  "temperature": 0.0, "avg_logprob": -0.2042112986246745, "compression_ratio": 1.5689655172413792,
  "no_speech_prob": 0.06913179159164429}, {"id": 35, "seek": 12600, "start": 131.6,
  "end": 139.44, "text": " With search, I''ve been doing search since about 2010-2011.
  Again, it''s fuzzy when I actually first started,", "tokens": [50644, 2022, 3164,
  11, 286, 600, 668, 884, 3164, 1670, 466, 9657, 12, 2009, 5348, 13, 3764, 11, 309,
  311, 34710, 562, 286, 767, 700, 1409, 11, 51036], "temperature": 0.0, "avg_logprob":
  -0.2042112986246745, "compression_ratio": 1.5689655172413792, "no_speech_prob":
  0.06913179159164429}, {"id": 36, "seek": 12600, "start": 139.44, "end": 148.32,
  "text": " but I think the first real serious thing I did with search was when I
  went to take my first solar", "tokens": [51036, 457, 286, 519, 264, 700, 957, 3156,
  551, 286, 630, 365, 3164, 390, 562, 286, 1437, 281, 747, 452, 700, 7936, 51480],
  "temperature": 0.0, "avg_logprob": -0.2042112986246745, "compression_ratio": 1.5689655172413792,
  "no_speech_prob": 0.06913179159164429}, {"id": 37, "seek": 12600, "start": 148.32,
  "end": 153.52, "text": " training course, which was one of the, when Lucid Works
  still had solar training and they had", "tokens": [51480, 3097, 1164, 11, 597, 390,
  472, 295, 264, 11, 562, 9593, 327, 27914, 920, 632, 7936, 3097, 293, 436, 632, 51740],
  "temperature": 0.0, "avg_logprob": -0.2042112986246745, "compression_ratio": 1.5689655172413792,
  "no_speech_prob": 0.06913179159164429}, {"id": 38, "seek": 15352, "start": 153.52,
  "end": 160.88000000000002, "text": " contractors coming to give training. So that
  was, that was in 2012, but I''d been messing around", "tokens": [50364, 28377, 1348,
  281, 976, 3097, 13, 407, 300, 390, 11, 300, 390, 294, 9125, 11, 457, 286, 1116,
  668, 23258, 926, 50732], "temperature": 0.0, "avg_logprob": -0.18199107622859453,
  "compression_ratio": 1.5648535564853556, "no_speech_prob": 0.0015786823350936174},
  {"id": 39, "seek": 15352, "start": 160.88000000000002, "end": 168.32000000000002,
  "text": " with engines before that. And I started on an engine called DT Search,
  which was the C++", "tokens": [50732, 365, 12982, 949, 300, 13, 400, 286, 1409,
  322, 364, 2848, 1219, 413, 51, 17180, 11, 597, 390, 264, 383, 25472, 51104], "temperature":
  0.0, "avg_logprob": -0.18199107622859453, "compression_ratio": 1.5648535564853556,
  "no_speech_prob": 0.0015786823350936174}, {"id": 40, "seek": 15352, "start": 171.12,
  "end": 175.12, "text": " closed source engine, but you could buy the code for like
  a thousand dollars a year. So the", "tokens": [51244, 5395, 4009, 2848, 11, 457,
  291, 727, 2256, 264, 3089, 337, 411, 257, 4714, 3808, 257, 1064, 13, 407, 264, 51444],
  "temperature": 0.0, "avg_logprob": -0.18199107622859453, "compression_ratio": 1.5648535564853556,
  "no_speech_prob": 0.0015786823350936174}, {"id": 41, "seek": 15352, "start": 175.12,
  "end": 182.8, "text": " company I was working for, MetiRex, we actually bought the
  code. And I was, I was the newbie with", "tokens": [51444, 2237, 286, 390, 1364,
  337, 11, 6377, 72, 49, 3121, 11, 321, 767, 4243, 264, 3089, 13, 400, 286, 390, 11,
  286, 390, 264, 777, 7392, 365, 51828], "temperature": 0.0, "avg_logprob": -0.18199107622859453,
  "compression_ratio": 1.5648535564853556, "no_speech_prob": 0.0015786823350936174},
  {"id": 42, "seek": 18280, "start": 182.8, "end": 187.92000000000002, "text": " search.
  I mean, we had guys been working with it for a while. And they''d built a whole
  platform", "tokens": [50364, 3164, 13, 286, 914, 11, 321, 632, 1074, 668, 1364,
  365, 309, 337, 257, 1339, 13, 400, 436, 1116, 3094, 257, 1379, 3663, 50620], "temperature":
  0.0, "avg_logprob": -0.17406098819473415, "compression_ratio": 1.5578512396694215,
  "no_speech_prob": 0.0006656002951785922}, {"id": 43, "seek": 18280, "start": 187.92000000000002,
  "end": 194.56, "text": " around DT Search. And then I was starting to show its age.
  So we started shifting over to solar.", "tokens": [50620, 926, 413, 51, 17180, 13,
  400, 550, 286, 390, 2891, 281, 855, 1080, 3205, 13, 407, 321, 1409, 17573, 670,
  281, 7936, 13, 50952], "temperature": 0.0, "avg_logprob": -0.17406098819473415,
  "compression_ratio": 1.5578512396694215, "no_speech_prob": 0.0006656002951785922},
  {"id": 44, "seek": 18280, "start": 196.24, "end": 201.76000000000002, "text": "
  But yeah, since I started that, but well, before that, I did a little bunch of computer",
  "tokens": [51036, 583, 1338, 11, 1670, 286, 1409, 300, 11, 457, 731, 11, 949, 300,
  11, 286, 630, 257, 707, 3840, 295, 3820, 51312], "temperature": 0.0, "avg_logprob":
  -0.17406098819473415, "compression_ratio": 1.5578512396694215, "no_speech_prob":
  0.0006656002951785922}, {"id": 45, "seek": 18280, "start": 201.76000000000002, "end":
  208.4, "text": " programs. So like the 20 years, 22 years-ish stuff that''s in my
  bio, like I''ve been, I graduated", "tokens": [51312, 4268, 13, 407, 411, 264, 945,
  924, 11, 5853, 924, 12, 742, 1507, 300, 311, 294, 452, 12198, 11, 411, 286, 600,
  668, 11, 286, 13693, 51644], "temperature": 0.0, "avg_logprob": -0.17406098819473415,
  "compression_ratio": 1.5578512396694215, "no_speech_prob": 0.0006656002951785922},
  {"id": 46, "seek": 20840, "start": 208.4, "end": 212.96, "text": " university in
  the year 2000, and I''ve been, you know, working professionally software ever since.",
  "tokens": [50364, 5454, 294, 264, 1064, 8132, 11, 293, 286, 600, 668, 11, 291, 458,
  11, 1364, 27941, 4722, 1562, 1670, 13, 50592], "temperature": 0.0, "avg_logprob":
  -0.19830952088038126, "compression_ratio": 1.556910569105691, "no_speech_prob":
  0.0018238467164337635}, {"id": 47, "seek": 20840, "start": 213.76000000000002, "end":
  221.92000000000002, "text": " But with Search, I, I really got interested in in
  Search around 2012, is when I really said,", "tokens": [50632, 583, 365, 17180,
  11, 286, 11, 286, 534, 658, 3102, 294, 294, 17180, 926, 9125, 11, 307, 562, 286,
  534, 848, 11, 51040], "temperature": 0.0, "avg_logprob": -0.19830952088038126, "compression_ratio":
  1.556910569105691, "no_speech_prob": 0.0018238467164337635}, {"id": 48, "seek":
  20840, "start": 221.92000000000002, "end": 226.4, "text": " wow, this is amazing.
  This is so much different from what I''ve been doing before. So that''s when", "tokens":
  [51040, 6076, 11, 341, 307, 2243, 13, 639, 307, 370, 709, 819, 490, 437, 286, 600,
  668, 884, 949, 13, 407, 300, 311, 562, 51264], "temperature": 0.0, "avg_logprob":
  -0.19830952088038126, "compression_ratio": 1.556910569105691, "no_speech_prob":
  0.0018238467164337635}, {"id": 49, "seek": 20840, "start": 226.4, "end": 231.84,
  "text": " I really do have had first into into the problem space in the domain.
  Yeah. And some people say", "tokens": [51264, 286, 534, 360, 362, 632, 700, 666,
  666, 264, 1154, 1901, 294, 264, 9274, 13, 865, 13, 400, 512, 561, 584, 51536], "temperature":
  0.0, "avg_logprob": -0.19830952088038126, "compression_ratio": 1.556910569105691,
  "no_speech_prob": 0.0018238467164337635}, {"id": 50, "seek": 23184, "start": 232.48,
  "end": 239.20000000000002, "text": " that many of us ended up in Search field by
  accident, as well as actually NLP. I''ve been talking", "tokens": [50396, 300, 867,
  295, 505, 4590, 493, 294, 17180, 2519, 538, 6398, 11, 382, 731, 382, 767, 426, 45196,
  13, 286, 600, 668, 1417, 50732], "temperature": 0.0, "avg_logprob": -0.1389677281282386,
  "compression_ratio": 1.6508620689655173, "no_speech_prob": 0.03212380409240723},
  {"id": 51, "seek": 23184, "start": 239.20000000000002, "end": 244.72, "text": "
  to one professor here in the University of Helsinki has built machine translation
  team, very,", "tokens": [50732, 281, 472, 8304, 510, 294, 264, 3535, 295, 45429,
  41917, 575, 3094, 3479, 12853, 1469, 11, 588, 11, 51008], "temperature": 0.0, "avg_logprob":
  -0.1389677281282386, "compression_ratio": 1.6508620689655173, "no_speech_prob":
  0.03212380409240723}, {"id": 52, "seek": 23184, "start": 244.72, "end": 252.72,
  "text": " very strong one. And, and he has built the, the system called Opus. And,
  and, and he actually said", "tokens": [51008, 588, 2068, 472, 13, 400, 11, 293,
  415, 575, 3094, 264, 11, 264, 1185, 1219, 12011, 301, 13, 400, 11, 293, 11, 293,
  415, 767, 848, 51408], "temperature": 0.0, "avg_logprob": -0.1389677281282386, "compression_ratio":
  1.6508620689655173, "no_speech_prob": 0.03212380409240723}, {"id": 53, "seek": 23184,
  "start": 252.72, "end": 259.04, "text": " that he ended up in NLP also by accident
  because it was just an offer from a professor and he", "tokens": [51408, 300, 415,
  4590, 493, 294, 426, 45196, 611, 538, 6398, 570, 309, 390, 445, 364, 2626, 490,
  257, 8304, 293, 415, 51724], "temperature": 0.0, "avg_logprob": -0.1389677281282386,
  "compression_ratio": 1.6508620689655173, "no_speech_prob": 0.03212380409240723},
  {"id": 54, "seek": 25904, "start": 259.04, "end": 263.52000000000004, "text": "
  decided to take it and he turned out to be quite good at it, you know. But he also
  had another", "tokens": [50364, 3047, 281, 747, 309, 293, 415, 3574, 484, 281, 312,
  1596, 665, 412, 309, 11, 291, 458, 13, 583, 415, 611, 632, 1071, 50588], "temperature":
  0.0, "avg_logprob": -0.10589849031888522, "compression_ratio": 1.63135593220339,
  "no_speech_prob": 0.004477100912481546}, {"id": 55, "seek": 25904, "start": 263.52000000000004,
  "end": 268.56, "text": " option just to go and work in in Germany, he''s from Germany,
  to work in Germany in some company,", "tokens": [50588, 3614, 445, 281, 352, 293,
  589, 294, 294, 7244, 11, 415, 311, 490, 7244, 11, 281, 589, 294, 7244, 294, 512,
  2237, 11, 50840], "temperature": 0.0, "avg_logprob": -0.10589849031888522, "compression_ratio":
  1.63135593220339, "no_speech_prob": 0.004477100912481546}, {"id": 56, "seek": 25904,
  "start": 268.56, "end": 274.96000000000004, "text": " database company. And, and,
  and likely he didn''t take that path. How was it for you? How do you feel", "tokens":
  [50840, 8149, 2237, 13, 400, 11, 293, 11, 293, 3700, 415, 994, 380, 747, 300, 3100,
  13, 1012, 390, 309, 337, 291, 30, 1012, 360, 291, 841, 51160], "temperature": 0.0,
  "avg_logprob": -0.10589849031888522, "compression_ratio": 1.63135593220339, "no_speech_prob":
  0.004477100912481546}, {"id": 57, "seek": 25904, "start": 274.96000000000004, "end":
  281.84000000000003, "text": " about yourself and then ending up in the in the in
  this space? That''s a great question. It''s", "tokens": [51160, 466, 1803, 293,
  550, 8121, 493, 294, 264, 294, 264, 294, 341, 1901, 30, 663, 311, 257, 869, 1168,
  13, 467, 311, 51504], "temperature": 0.0, "avg_logprob": -0.10589849031888522, "compression_ratio":
  1.63135593220339, "no_speech_prob": 0.004477100912481546}, {"id": 58, "seek": 28184,
  "start": 281.84, "end": 293.52, "text": " interesting. I feel like ending it up,
  I, it was definitely somewhat accidental. I found, I,", "tokens": [50364, 1880,
  13, 286, 841, 411, 8121, 309, 493, 11, 286, 11, 309, 390, 2138, 8344, 38094, 13,
  286, 1352, 11, 286, 11, 50948], "temperature": 0.0, "avg_logprob": -0.16171821425942814,
  "compression_ratio": 1.572972972972973, "no_speech_prob": 0.0006110819522291422},
  {"id": 59, "seek": 28184, "start": 293.52, "end": 299.03999999999996, "text": "
  I had the pleasure of meeting so many people in search through my different positions
  that I was", "tokens": [50948, 286, 632, 264, 6834, 295, 3440, 370, 867, 561, 294,
  3164, 807, 452, 819, 8432, 300, 286, 390, 51224], "temperature": 0.0, "avg_logprob":
  -0.16171821425942814, "compression_ratio": 1.572972972972973, "no_speech_prob":
  0.0006110819522291422}, {"id": 60, "seek": 28184, "start": 299.03999999999996, "end":
  306.55999999999995, "text": " working with and the varying degrees of expertise.
  I found that a lot of people who got involved with", "tokens": [51224, 1364, 365,
  293, 264, 22984, 5310, 295, 11769, 13, 286, 1352, 300, 257, 688, 295, 561, 567,
  658, 3288, 365, 51600], "temperature": 0.0, "avg_logprob": -0.16171821425942814,
  "compression_ratio": 1.572972972972973, "no_speech_prob": 0.0006110819522291422},
  {"id": 61, "seek": 30656, "start": 306.56, "end": 313.36, "text": " machine learning
  found out about search because TFI, DF and all that stuff is like an algorithm",
  "tokens": [50364, 3479, 2539, 1352, 484, 466, 3164, 570, 314, 38568, 11, 48336,
  293, 439, 300, 1507, 307, 411, 364, 9284, 50704], "temperature": 0.0, "avg_logprob":
  -0.1660832511054145, "compression_ratio": 1.6551724137931034, "no_speech_prob":
  9.055841655936092e-05}, {"id": 62, "seek": 30656, "start": 313.36, "end": 317.28000000000003,
  "text": " and it''s like, oh, there''s this whole language problem behind search,
  so we have to figure out.", "tokens": [50704, 293, 309, 311, 411, 11, 1954, 11,
  456, 311, 341, 1379, 2856, 1154, 2261, 3164, 11, 370, 321, 362, 281, 2573, 484,
  13, 50900], "temperature": 0.0, "avg_logprob": -0.1660832511054145, "compression_ratio":
  1.6551724137931034, "no_speech_prob": 9.055841655936092e-05}, {"id": 63, "seek":
  30656, "start": 317.28000000000003, "end": 321.28000000000003, "text": " And then
  the search people get involved in machine learning because, oh, this language problem",
  "tokens": [50900, 400, 550, 264, 3164, 561, 483, 3288, 294, 3479, 2539, 570, 11,
  1954, 11, 341, 2856, 1154, 51100], "temperature": 0.0, "avg_logprob": -0.1660832511054145,
  "compression_ratio": 1.6551724137931034, "no_speech_prob": 9.055841655936092e-05},
  {"id": 64, "seek": 30656, "start": 321.28000000000003, "end": 329.84000000000003,
  "text": " is horrible. How do we solve it with automation and learning? So I, I
  accidentally stumbled on it", "tokens": [51100, 307, 9263, 13, 1012, 360, 321, 5039,
  309, 365, 17769, 293, 2539, 30, 407, 286, 11, 286, 15715, 36668, 322, 309, 51528],
  "temperature": 0.0, "avg_logprob": -0.1660832511054145, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 9.055841655936092e-05}, {"id": 65, "seek": 32984, "start": 329.84,
  "end": 336.96, "text": " because I took, it was a, it was a role that was in like
  healthcare compliance. And I was", "tokens": [50364, 570, 286, 1890, 11, 309, 390,
  257, 11, 309, 390, 257, 3090, 300, 390, 294, 411, 8884, 15882, 13, 400, 286, 390,
  50720], "temperature": 0.0, "avg_logprob": -0.1749326012351296, "compression_ratio":
  1.705223880597015, "no_speech_prob": 0.0008606132469139993}, {"id": 66, "seek":
  32984, "start": 336.96, "end": 341.03999999999996, "text": " interested in that
  domain specifically and search just happened to be a really important problem",
  "tokens": [50720, 3102, 294, 300, 9274, 4682, 293, 3164, 445, 2011, 281, 312, 257,
  534, 1021, 1154, 50924], "temperature": 0.0, "avg_logprob": -0.1749326012351296,
  "compression_ratio": 1.705223880597015, "no_speech_prob": 0.0008606132469139993},
  {"id": 67, "seek": 32984, "start": 341.03999999999996, "end": 345.03999999999996,
  "text": " in that space. So that''s how I kind of got into the, the technical domain
  of search.", "tokens": [50924, 294, 300, 1901, 13, 407, 300, 311, 577, 286, 733,
  295, 658, 666, 264, 11, 264, 6191, 9274, 295, 3164, 13, 51124], "temperature": 0.0,
  "avg_logprob": -0.1749326012351296, "compression_ratio": 1.705223880597015, "no_speech_prob":
  0.0008606132469139993}, {"id": 68, "seek": 32984, "start": 346.88, "end": 352.79999999999995,
  "text": " And it just was so much more fascinating than like the stuff that I was
  used to with,", "tokens": [51216, 400, 309, 445, 390, 370, 709, 544, 10343, 813,
  411, 264, 1507, 300, 286, 390, 1143, 281, 365, 11, 51512], "temperature": 0.0, "avg_logprob":
  -0.1749326012351296, "compression_ratio": 1.705223880597015, "no_speech_prob": 0.0008606132469139993},
  {"id": 69, "seek": 32984, "start": 352.79999999999995, "end": 358.79999999999995,
  "text": " crud, you know, just create read update delete and just workflow applications,
  which I''d been doing", "tokens": [51512, 941, 532, 11, 291, 458, 11, 445, 1884,
  1401, 5623, 12097, 293, 445, 20993, 5821, 11, 597, 286, 1116, 668, 884, 51812],
  "temperature": 0.0, "avg_logprob": -0.1749326012351296, "compression_ratio": 1.705223880597015,
  "no_speech_prob": 0.0008606132469139993}, {"id": 70, "seek": 35880, "start": 358.8,
  "end": 365.76, "text": " for, you know, 10 to 12 years at that point. Yeah. Yeah,
  I mean, for me, like searching, you know, like,", "tokens": [50364, 337, 11, 291,
  458, 11, 1266, 281, 2272, 924, 412, 300, 935, 13, 865, 13, 865, 11, 286, 914, 11,
  337, 385, 11, 411, 10808, 11, 291, 458, 11, 411, 11, 50712], "temperature": 0.0,
  "avg_logprob": -0.17931307142025957, "compression_ratio": 1.6300813008130082, "no_speech_prob":
  0.00387572986073792}, {"id": 71, "seek": 35880, "start": 366.64, "end": 375.12,
  "text": " I think I started 2002, 2003 academically, but then it was like seven
  years past and I still couldn''t", "tokens": [50756, 286, 519, 286, 1409, 17822,
  11, 16416, 48944, 11, 457, 550, 309, 390, 411, 3407, 924, 1791, 293, 286, 920, 2809,
  380, 51180], "temperature": 0.0, "avg_logprob": -0.17931307142025957, "compression_ratio":
  1.6300813008130082, "no_speech_prob": 0.00387572986073792}, {"id": 72, "seek": 35880,
  "start": 375.12, "end": 380.88, "text": " find a niche or a job for myself because
  there haven''t been then many search companies in Finland", "tokens": [51180, 915,
  257, 19956, 420, 257, 1691, 337, 2059, 570, 456, 2378, 380, 668, 550, 867, 3164,
  3431, 294, 24869, 51468], "temperature": 0.0, "avg_logprob": -0.17931307142025957,
  "compression_ratio": 1.6300813008130082, "no_speech_prob": 0.00387572986073792},
  {"id": 73, "seek": 35880, "start": 380.88, "end": 388.32, "text": " actually at
  that point. And then I found a company which I joined in 2010, AlfaSense. And it
  was", "tokens": [51468, 767, 412, 300, 935, 13, 400, 550, 286, 1352, 257, 2237,
  597, 286, 6869, 294, 9657, 11, 967, 11771, 50, 1288, 13, 400, 309, 390, 51840],
  "temperature": 0.0, "avg_logprob": -0.17931307142025957, "compression_ratio": 1.6300813008130082,
  "no_speech_prob": 0.00387572986073792}, {"id": 74, "seek": 38832, "start": 388.32,
  "end": 394.8, "text": " Apache Solar, you see in everything new, but it was still
  somehow inviting. And I think the first", "tokens": [50364, 46597, 22385, 11, 291,
  536, 294, 1203, 777, 11, 457, 309, 390, 920, 6063, 18202, 13, 400, 286, 519, 264,
  700, 50688], "temperature": 0.0, "avg_logprob": -0.1527200946371064, "compression_ratio":
  1.74822695035461, "no_speech_prob": 0.0015541462926194072}, {"id": 75, "seek": 38832,
  "start": 394.8, "end": 398.71999999999997, "text": " time when I, when I''ve built
  the backend and I was like, okay, somebody is going to use this,", "tokens": [50688,
  565, 562, 286, 11, 562, 286, 600, 3094, 264, 38087, 293, 286, 390, 411, 11, 1392,
  11, 2618, 307, 516, 281, 764, 341, 11, 50884], "temperature": 0.0, "avg_logprob":
  -0.1527200946371064, "compression_ratio": 1.74822695035461, "no_speech_prob": 0.0015541462926194072},
  {"id": 76, "seek": 38832, "start": 398.71999999999997, "end": 404.24, "text": "
  somebody is going to type the queries and we''ll try to find information. So I also
  tried it out", "tokens": [50884, 2618, 307, 516, 281, 2010, 264, 24109, 293, 321,
  603, 853, 281, 915, 1589, 13, 407, 286, 611, 3031, 309, 484, 51160], "temperature":
  0.0, "avg_logprob": -0.1527200946371064, "compression_ratio": 1.74822695035461,
  "no_speech_prob": 0.0015541462926194072}, {"id": 77, "seek": 38832, "start": 404.24,
  "end": 410.56, "text": " and kind of like maybe work, maybe didn''t, I wasn''t the,
  the, the user of this system. I didn''t know", "tokens": [51160, 293, 733, 295,
  411, 1310, 589, 11, 1310, 994, 380, 11, 286, 2067, 380, 264, 11, 264, 11, 264, 4195,
  295, 341, 1185, 13, 286, 994, 380, 458, 51476], "temperature": 0.0, "avg_logprob":
  -0.1527200946371064, "compression_ratio": 1.74822695035461, "no_speech_prob": 0.0015541462926194072},
  {"id": 78, "seek": 38832, "start": 410.56, "end": 415.84, "text": " what to type.
  So I was just grabbing some phrases from the documents and see, okay, does it find
  or not,", "tokens": [51476, 437, 281, 2010, 13, 407, 286, 390, 445, 23771, 512,
  20312, 490, 264, 8512, 293, 536, 11, 1392, 11, 775, 309, 915, 420, 406, 11, 51740],
  "temperature": 0.0, "avg_logprob": -0.1527200946371064, "compression_ratio": 1.74822695035461,
  "no_speech_prob": 0.0015541462926194072}, {"id": 79, "seek": 41584, "start": 415.84,
  "end": 422.08, "text": " you know? So is this something that also like attracted
  you like, okay, findability, right?", "tokens": [50364, 291, 458, 30, 407, 307,
  341, 746, 300, 611, 411, 15912, 291, 411, 11, 1392, 11, 915, 2310, 11, 558, 30,
  50676], "temperature": 0.0, "avg_logprob": -0.14896703474592454, "compression_ratio":
  1.7028112449799198, "no_speech_prob": 0.0015000887215137482}, {"id": 80, "seek":
  41584, "start": 422.08, "end": 426.64, "text": " Like discovery or maybe discovery
  is the next stage, but even the findability itself.", "tokens": [50676, 1743, 12114,
  420, 1310, 12114, 307, 264, 958, 3233, 11, 457, 754, 264, 915, 2310, 2564, 13, 50904],
  "temperature": 0.0, "avg_logprob": -0.14896703474592454, "compression_ratio": 1.7028112449799198,
  "no_speech_prob": 0.0015000887215137482}, {"id": 81, "seek": 41584, "start": 428.15999999999997,
  "end": 431.67999999999995, "text": " Yeah, I guess search was really my first step
  towards", "tokens": [50980, 865, 11, 286, 2041, 3164, 390, 534, 452, 700, 1823,
  3030, 51156], "temperature": 0.0, "avg_logprob": -0.14896703474592454, "compression_ratio":
  1.7028112449799198, "no_speech_prob": 0.0015000887215137482}, {"id": 82, "seek":
  41584, "start": 433.35999999999996, "end": 439.52, "text": " working with real complex
  data that wasn''t so unstructured, unstructured data, right? You kind of,", "tokens":
  [51240, 1364, 365, 957, 3997, 1412, 300, 2067, 380, 370, 18799, 46847, 11, 18799,
  46847, 1412, 11, 558, 30, 509, 733, 295, 11, 51548], "temperature": 0.0, "avg_logprob":
  -0.14896703474592454, "compression_ratio": 1.7028112449799198, "no_speech_prob":
  0.0015000887215137482}, {"id": 83, "seek": 41584, "start": 440.15999999999997, "end":
  444.55999999999995, "text": " you kind of reach a limit with structured data at
  some point of getting stuff into databases,", "tokens": [51580, 291, 733, 295, 2524,
  257, 4948, 365, 18519, 1412, 412, 512, 935, 295, 1242, 1507, 666, 22380, 11, 51800],
  "temperature": 0.0, "avg_logprob": -0.14896703474592454, "compression_ratio": 1.7028112449799198,
  "no_speech_prob": 0.0015000887215137482}, {"id": 84, "seek": 44456, "start": 444.56,
  "end": 447.84, "text": " getting it out and things like that. And you can, you can
  spend a lifetime in that work.", "tokens": [50364, 1242, 309, 484, 293, 721, 411,
  300, 13, 400, 291, 393, 11, 291, 393, 3496, 257, 11364, 294, 300, 589, 13, 50528],
  "temperature": 0.0, "avg_logprob": -0.1303442970651095, "compression_ratio": 1.8975409836065573,
  "no_speech_prob": 0.0005779014900326729}, {"id": 85, "seek": 44456, "start": 448.64,
  "end": 457.44, "text": " But I felt like I''d been doing it for a while. And with,
  with search, it was like this,", "tokens": [50568, 583, 286, 2762, 411, 286, 1116,
  668, 884, 309, 337, 257, 1339, 13, 400, 365, 11, 365, 3164, 11, 309, 390, 411, 341,
  11, 51008], "temperature": 0.0, "avg_logprob": -0.1303442970651095, "compression_ratio":
  1.8975409836065573, "no_speech_prob": 0.0005779014900326729}, {"id": 86, "seek":
  44456, "start": 457.44, "end": 462.4, "text": " this weird world where it''s like
  all this unknown stuff and you don''t know what to do. So it''s", "tokens": [51008,
  341, 3657, 1002, 689, 309, 311, 411, 439, 341, 9841, 1507, 293, 291, 500, 380, 458,
  437, 281, 360, 13, 407, 309, 311, 51256], "temperature": 0.0, "avg_logprob": -0.1303442970651095,
  "compression_ratio": 1.8975409836065573, "no_speech_prob": 0.0005779014900326729},
  {"id": 87, "seek": 44456, "start": 462.4, "end": 466.96, "text": " this unsolved
  problem. I felt like databases and things like that were like this solved problem,",
  "tokens": [51256, 341, 2693, 29110, 1154, 13, 286, 2762, 411, 22380, 293, 721, 411,
  300, 645, 411, 341, 13041, 1154, 11, 51484], "temperature": 0.0, "avg_logprob":
  -0.1303442970651095, "compression_ratio": 1.8975409836065573, "no_speech_prob":
  0.0005779014900326729}, {"id": 88, "seek": 44456, "start": 466.96, "end": 474.0,
  "text": " where search, search wasn''t a solved problem and still isn''t. Now with
  the work, if I had been", "tokens": [51484, 689, 3164, 11, 3164, 2067, 380, 257,
  13041, 1154, 293, 920, 1943, 380, 13, 823, 365, 264, 589, 11, 498, 286, 632, 668,
  51836], "temperature": 0.0, "avg_logprob": -0.1303442970651095, "compression_ratio":
  1.8975409836065573, "no_speech_prob": 0.0005779014900326729}, {"id": 89, "seek":
  47400, "start": 474.0, "end": 478.08, "text": " doing the same database work, that''s
  all no code right now. You can just create the same stuff I", "tokens": [50364,
  884, 264, 912, 8149, 589, 11, 300, 311, 439, 572, 3089, 558, 586, 13, 509, 393,
  445, 1884, 264, 912, 1507, 286, 50568], "temperature": 0.0, "avg_logprob": -0.15399330381363158,
  "compression_ratio": 1.7018867924528303, "no_speech_prob": 0.0005444454145617783},
  {"id": 90, "seek": 47400, "start": 478.08, "end": 481.68, "text": " was doing with
  no code tools. You don''t even have to be a programmer if you don''t want to", "tokens":
  [50568, 390, 884, 365, 572, 3089, 3873, 13, 509, 500, 380, 754, 362, 281, 312, 257,
  32116, 498, 291, 500, 380, 528, 281, 50748], "temperature": 0.0, "avg_logprob":
  -0.15399330381363158, "compression_ratio": 1.7018867924528303, "no_speech_prob":
  0.0005444454145617783}, {"id": 91, "seek": 47400, "start": 482.32, "end": 486.4,
  "text": " with the level that we were doing it, you know, in the mid 2000s. So,",
  "tokens": [50780, 365, 264, 1496, 300, 321, 645, 884, 309, 11, 291, 458, 11, 294,
  264, 2062, 8132, 82, 13, 407, 11, 50984], "temperature": 0.0, "avg_logprob": -0.15399330381363158,
  "compression_ratio": 1.7018867924528303, "no_speech_prob": 0.0005444454145617783},
  {"id": 92, "seek": 47400, "start": 489.12, "end": 495.36, "text": " yeah, now it
  is. And it''s still, it''s still unsolved. Even when we start talking, you know,",
  "tokens": [51120, 1338, 11, 586, 309, 307, 13, 400, 309, 311, 920, 11, 309, 311,
  920, 2693, 29110, 13, 2754, 562, 321, 722, 1417, 11, 291, 458, 11, 51432], "temperature":
  0.0, "avg_logprob": -0.15399330381363158, "compression_ratio": 1.7018867924528303,
  "no_speech_prob": 0.0005444454145617783}, {"id": 93, "seek": 47400, "start": 495.36,
  "end": 499.68, "text": " we''re going to talk about vectors, of course, but vector
  search. But that''s still an unsolved problem.", "tokens": [51432, 321, 434, 516,
  281, 751, 466, 18875, 11, 295, 1164, 11, 457, 8062, 3164, 13, 583, 300, 311, 920,
  364, 2693, 29110, 1154, 13, 51648], "temperature": 0.0, "avg_logprob": -0.15399330381363158,
  "compression_ratio": 1.7018867924528303, "no_speech_prob": 0.0005444454145617783},
  {"id": 94, "seek": 49968, "start": 499.68, "end": 504.8, "text": " It''s like another
  tool, but you still have all these issues that you have to take into account.",
  "tokens": [50364, 467, 311, 411, 1071, 2290, 11, 457, 291, 920, 362, 439, 613, 2663,
  300, 291, 362, 281, 747, 666, 2696, 13, 50620], "temperature": 0.0, "avg_logprob":
  -0.1564168632030487, "compression_ratio": 1.5991735537190082, "no_speech_prob":
  0.006438321899622679}, {"id": 95, "seek": 49968, "start": 505.6, "end": 512.32,
  "text": " Yeah. So endless exploration. Yeah, it''s like infinite quest in many
  ways. There is like a", "tokens": [50660, 865, 13, 407, 16144, 16197, 13, 865, 11,
  309, 311, 411, 13785, 866, 294, 867, 2098, 13, 821, 307, 411, 257, 50996], "temperature":
  0.0, "avg_logprob": -0.1564168632030487, "compression_ratio": 1.5991735537190082,
  "no_speech_prob": 0.006438321899622679}, {"id": 96, "seek": 49968, "start": 512.32,
  "end": 519.84, "text": " limitless amount of tasks to solve. But then, so somehow
  in your career, there was a turn that you", "tokens": [50996, 4948, 1832, 2372,
  295, 9608, 281, 5039, 13, 583, 550, 11, 370, 6063, 294, 428, 3988, 11, 456, 390,
  257, 1261, 300, 291, 51372], "temperature": 0.0, "avg_logprob": -0.1564168632030487,
  "compression_ratio": 1.5991735537190082, "no_speech_prob": 0.006438321899622679},
  {"id": 97, "seek": 49968, "start": 519.84, "end": 528.0, "text": " decided to get
  closer to this vector search field. I just wanted to hear your kind of first reaction,",
  "tokens": [51372, 3047, 281, 483, 4966, 281, 341, 8062, 3164, 2519, 13, 286, 445,
  1415, 281, 1568, 428, 733, 295, 700, 5480, 11, 51780], "temperature": 0.0, "avg_logprob":
  -0.1564168632030487, "compression_ratio": 1.5991735537190082, "no_speech_prob":
  0.006438321899622679}, {"id": 98, "seek": 52800, "start": 528.0, "end": 533.92,
  "text": " like what did you think about it? When did you hear about it? And also,
  what attracted you?", "tokens": [50364, 411, 437, 630, 291, 519, 466, 309, 30, 1133,
  630, 291, 1568, 466, 309, 30, 400, 611, 11, 437, 15912, 291, 30, 50660], "temperature":
  0.0, "avg_logprob": -0.12184692251271215, "compression_ratio": 1.6492890995260663,
  "no_speech_prob": 0.00047050503781065345}, {"id": 99, "seek": 52800, "start": 536.96,
  "end": 542.72, "text": " I''d say the first thing that really attracted me towards
  vector search was the birth paper", "tokens": [50812, 286, 1116, 584, 264, 700,
  551, 300, 534, 15912, 385, 3030, 8062, 3164, 390, 264, 3965, 3035, 51100], "temperature":
  0.0, "avg_logprob": -0.12184692251271215, "compression_ratio": 1.6492890995260663,
  "no_speech_prob": 0.00047050503781065345}, {"id": 100, "seek": 52800, "start": 544.16,
  "end": 548.56, "text": " that was written in 2018, but I didn''t I didn''t come
  across it until 2019.", "tokens": [51172, 300, 390, 3720, 294, 6096, 11, 457, 286,
  994, 380, 286, 994, 380, 808, 2108, 309, 1826, 6071, 13, 51392], "temperature":
  0.0, "avg_logprob": -0.12184692251271215, "compression_ratio": 1.6492890995260663,
  "no_speech_prob": 0.00047050503781065345}, {"id": 101, "seek": 52800, "start": 550.4,
  "end": 554.0, "text": " And Google had written a blog about how they were using
  it for their for their web search.", "tokens": [51484, 400, 3329, 632, 3720, 257,
  6968, 466, 577, 436, 645, 1228, 309, 337, 641, 337, 641, 3670, 3164, 13, 51664],
  "temperature": 0.0, "avg_logprob": -0.12184692251271215, "compression_ratio": 1.6492890995260663,
  "no_speech_prob": 0.00047050503781065345}, {"id": 102, "seek": 55400, "start": 554.96,
  "end": 559.92, "text": " And you know, you could download some Python and get this
  stuff to work.", "tokens": [50412, 400, 291, 458, 11, 291, 727, 5484, 512, 15329,
  293, 483, 341, 1507, 281, 589, 13, 50660], "temperature": 0.0, "avg_logprob": -0.18963942876676235,
  "compression_ratio": 1.4976303317535544, "no_speech_prob": 0.007488514296710491},
  {"id": 103, "seek": 55400, "start": 561.44, "end": 566.08, "text": " But the reason
  why I was so fascinated by that is because of", "tokens": [50736, 583, 264, 1778,
  983, 286, 390, 370, 24597, 538, 300, 307, 570, 295, 50968], "temperature": 0.0,
  "avg_logprob": -0.18963942876676235, "compression_ratio": 1.4976303317535544, "no_speech_prob":
  0.007488514296710491}, {"id": 104, "seek": 55400, "start": 568.4, "end": 577.92,
  "text": " you know, working in search already six years. No, let''s do some math.
  So, you know, eight years at", "tokens": [51084, 291, 458, 11, 1364, 294, 3164,
  1217, 2309, 924, 13, 883, 11, 718, 311, 360, 512, 5221, 13, 407, 11, 291, 458, 11,
  3180, 924, 412, 51560], "temperature": 0.0, "avg_logprob": -0.18963942876676235,
  "compression_ratio": 1.4976303317535544, "no_speech_prob": 0.007488514296710491},
  {"id": 105, "seek": 55400, "start": 577.92, "end": 583.6, "text": " that point,
  I had been stumbling along with the vocabulary problem. The query term", "tokens":
  [51560, 300, 935, 11, 286, 632, 668, 342, 14188, 2051, 365, 264, 19864, 1154, 13,
  440, 14581, 1433, 51844], "temperature": 0.0, "avg_logprob": -0.18963942876676235,
  "compression_ratio": 1.4976303317535544, "no_speech_prob": 0.007488514296710491},
  {"id": 106, "seek": 58360, "start": 583.6, "end": 589.0400000000001, "text": " dependence
  problem, as we call it, where, okay, well, to solve this, you have to create a bunch
  of", "tokens": [50364, 31704, 1154, 11, 382, 321, 818, 309, 11, 689, 11, 1392, 11,
  731, 11, 281, 5039, 341, 11, 291, 362, 281, 1884, 257, 3840, 295, 50636], "temperature":
  0.0, "avg_logprob": -0.19538683104283602, "compression_ratio": 1.7757847533632287,
  "no_speech_prob": 0.0017192689701914787}, {"id": 107, "seek": 58360, "start": 589.0400000000001,
  "end": 593.44, "text": " synonyms and then you get to a certain level of advancement
  and then you create a taxonomy and then", "tokens": [50636, 5451, 2526, 2592, 293,
  550, 291, 483, 281, 257, 1629, 1496, 295, 35764, 293, 550, 291, 1884, 257, 3366,
  23423, 293, 550, 50856], "temperature": 0.0, "avg_logprob": -0.19538683104283602,
  "compression_ratio": 1.7757847533632287, "no_speech_prob": 0.0017192689701914787},
  {"id": 108, "seek": 58360, "start": 593.44, "end": 600.16, "text": " you know, you
  created a knowledge graph. And you know, before before birth, we''d started playing",
  "tokens": [50856, 291, 458, 11, 291, 2942, 257, 3601, 4295, 13, 400, 291, 458, 11,
  949, 949, 3965, 11, 321, 1116, 1409, 2433, 51192], "temperature": 0.0, "avg_logprob":
  -0.19538683104283602, "compression_ratio": 1.7757847533632287, "no_speech_prob":
  0.0017192689701914787}, {"id": 109, "seek": 58360, "start": 600.16, "end": 607.2,
  "text": " around with word to veck and saying, oh, can you know, can these type
  of embeddings be used to solve", "tokens": [51192, 926, 365, 1349, 281, 1241, 547,
  293, 1566, 11, 1954, 11, 393, 291, 458, 11, 393, 613, 2010, 295, 12240, 29432, 312,
  1143, 281, 5039, 51544], "temperature": 0.0, "avg_logprob": -0.19538683104283602,
  "compression_ratio": 1.7757847533632287, "no_speech_prob": 0.0017192689701914787},
  {"id": 110, "seek": 60720, "start": 608.08, "end": 612.48, "text": " this whack-able
  problem with synonyms and knowledge graph vocabulary expansion?", "tokens": [50408,
  341, 42877, 12, 712, 1154, 365, 5451, 2526, 2592, 293, 3601, 4295, 19864, 11260,
  30, 50628], "temperature": 0.0, "avg_logprob": -0.14181370735168458, "compression_ratio":
  1.6451612903225807, "no_speech_prob": 0.001170991687104106}, {"id": 111, "seek":
  60720, "start": 613.12, "end": 618.24, "text": " The answer turned out to be no
  with word to veck. It didn''t work as well as we''d hoped.", "tokens": [50660, 440,
  1867, 3574, 484, 281, 312, 572, 365, 1349, 281, 1241, 547, 13, 467, 994, 380, 589,
  382, 731, 382, 321, 1116, 19737, 13, 50916], "temperature": 0.0, "avg_logprob":
  -0.14181370735168458, "compression_ratio": 1.6451612903225807, "no_speech_prob":
  0.001170991687104106}, {"id": 112, "seek": 60720, "start": 618.24, "end": 624.6400000000001,
  "text": " It helped with some things, but not, but it harmed with others. So it
  produced a lot of noise and", "tokens": [50916, 467, 4254, 365, 512, 721, 11, 457,
  406, 11, 457, 309, 41478, 365, 2357, 13, 407, 309, 7126, 257, 688, 295, 5658, 293,
  51236], "temperature": 0.0, "avg_logprob": -0.14181370735168458, "compression_ratio":
  1.6451612903225807, "no_speech_prob": 0.001170991687104106}, {"id": 113, "seek":
  60720, "start": 624.6400000000001, "end": 629.36, "text": " and you know, maybe
  we didn''t give it a good enough chance, but we saw, okay, we can train this", "tokens":
  [51236, 293, 291, 458, 11, 1310, 321, 994, 380, 976, 309, 257, 665, 1547, 2931,
  11, 457, 321, 1866, 11, 1392, 11, 321, 393, 3847, 341, 51472], "temperature": 0.0,
  "avg_logprob": -0.14181370735168458, "compression_ratio": 1.6451612903225807, "no_speech_prob":
  0.001170991687104106}, {"id": 114, "seek": 60720, "start": 629.36, "end": 635.0400000000001,
  "text": " thing pretty quick and we can get this model from our content. But there''s
  still this problem. So", "tokens": [51472, 551, 1238, 1702, 293, 321, 393, 483,
  341, 2316, 490, 527, 2701, 13, 583, 456, 311, 920, 341, 1154, 13, 407, 51756], "temperature":
  0.0, "avg_logprob": -0.14181370735168458, "compression_ratio": 1.6451612903225807,
  "no_speech_prob": 0.001170991687104106}, {"id": 115, "seek": 63504, "start": 636.0,
  "end": 642.64, "text": " when I started to play around with some of the Python tools
  that were available for", "tokens": [50412, 562, 286, 1409, 281, 862, 926, 365,
  512, 295, 264, 15329, 3873, 300, 645, 2435, 337, 50744], "temperature": 0.0, "avg_logprob":
  -0.15774615427081504, "compression_ratio": 1.6681614349775784, "no_speech_prob":
  0.0004325170593801886}, {"id": 116, "seek": 63504, "start": 643.52, "end": 648.56,
  "text": " for Bert and large language networks, which actually used word to veck
  as the pre-processing step", "tokens": [50788, 337, 29594, 293, 2416, 2856, 9590,
  11, 597, 767, 1143, 1349, 281, 1241, 547, 382, 264, 659, 12, 41075, 278, 1823, 51040],
  "temperature": 0.0, "avg_logprob": -0.15774615427081504, "compression_ratio": 1.6681614349775784,
  "no_speech_prob": 0.0004325170593801886}, {"id": 117, "seek": 63504, "start": 649.8399999999999,
  "end": 654.4, "text": " to get the first to get the first encodings and then with
  first embeddings and then use those", "tokens": [51104, 281, 483, 264, 700, 281,
  483, 264, 700, 2058, 378, 1109, 293, 550, 365, 700, 12240, 29432, 293, 550, 764,
  729, 51332], "temperature": 0.0, "avg_logprob": -0.15774615427081504, "compression_ratio":
  1.6681614349775784, "no_speech_prob": 0.0004325170593801886}, {"id": 118, "seek":
  63504, "start": 654.4, "end": 660.9599999999999, "text": " identifiers to go forward.
  I really saw something there. I saw actual similarity where I didn''t,", "tokens":
  [51332, 2473, 23463, 281, 352, 2128, 13, 286, 534, 1866, 746, 456, 13, 286, 1866,
  3539, 32194, 689, 286, 994, 380, 11, 51660], "temperature": 0.0, "avg_logprob":
  -0.15774615427081504, "compression_ratio": 1.6681614349775784, "no_speech_prob":
  0.0004325170593801886}, {"id": 119, "seek": 66096, "start": 660.96, "end": 666.72,
  "text": " I just saw kind of co-occurrence with word to veck before. Yeah, these
  things are, you see them", "tokens": [50364, 286, 445, 1866, 733, 295, 598, 12,
  905, 14112, 10760, 365, 1349, 281, 1241, 547, 949, 13, 865, 11, 613, 721, 366, 11,
  291, 536, 552, 50652], "temperature": 0.0, "avg_logprob": -0.12455715093397557,
  "compression_ratio": 1.7472527472527473, "no_speech_prob": 0.0007773492834530771},
  {"id": 120, "seek": 66096, "start": 666.72, "end": 671.36, "text": " in the same
  context. But with actual linguistic similarity, the first time I saw that was with",
  "tokens": [50652, 294, 264, 912, 4319, 13, 583, 365, 3539, 43002, 32194, 11, 264,
  700, 565, 286, 1866, 300, 390, 365, 50884], "temperature": 0.0, "avg_logprob": -0.12455715093397557,
  "compression_ratio": 1.7472527472527473, "no_speech_prob": 0.0007773492834530771},
  {"id": 121, "seek": 66096, "start": 671.36, "end": 676.5600000000001, "text": "
  Bert and that''s where all the hype came from. And then the next step with Bert
  is like, okay,", "tokens": [50884, 29594, 293, 300, 311, 689, 439, 264, 24144, 1361,
  490, 13, 400, 550, 264, 958, 1823, 365, 29594, 307, 411, 11, 1392, 11, 51144], "temperature":
  0.0, "avg_logprob": -0.12455715093397557, "compression_ratio": 1.7472527472527473,
  "no_speech_prob": 0.0007773492834530771}, {"id": 122, "seek": 66096, "start": 676.5600000000001,
  "end": 681.2, "text": " I have these vectors. Now what do I do with them? And then
  I said, okay, well, I have to use a", "tokens": [51144, 286, 362, 613, 18875, 13,
  823, 437, 360, 286, 360, 365, 552, 30, 400, 550, 286, 848, 11, 1392, 11, 731, 11,
  286, 362, 281, 764, 257, 51376], "temperature": 0.0, "avg_logprob": -0.12455715093397557,
  "compression_ratio": 1.7472527472527473, "no_speech_prob": 0.0007773492834530771},
  {"id": 123, "seek": 66096, "start": 681.2, "end": 686.88, "text": " dot product,
  right? I have to use a cosine similarity. Okay, let me just do that. And then I
  say,", "tokens": [51376, 5893, 1674, 11, 558, 30, 286, 362, 281, 764, 257, 23565,
  32194, 13, 1033, 11, 718, 385, 445, 360, 300, 13, 400, 550, 286, 584, 11, 51660],
  "temperature": 0.0, "avg_logprob": -0.12455715093397557, "compression_ratio": 1.7472527472527473,
  "no_speech_prob": 0.0007773492834530771}, {"id": 124, "seek": 68688, "start": 686.96,
  "end": 692.16, "text": " oh, you can''t just do that across every vector. It''s
  impossible. You have to do something else.", "tokens": [50368, 1954, 11, 291, 393,
  380, 445, 360, 300, 2108, 633, 8062, 13, 467, 311, 6243, 13, 509, 362, 281, 360,
  746, 1646, 13, 50628], "temperature": 0.0, "avg_logprob": -0.1347291197957872, "compression_ratio":
  1.4646464646464648, "no_speech_prob": 0.0005540549173019826}, {"id": 125, "seek":
  68688, "start": 692.16, "end": 700.64, "text": " And then you go on this learning
  path, right? So that''s where I ended up. And I had actually written", "tokens":
  [50628, 400, 550, 291, 352, 322, 341, 2539, 3100, 11, 558, 30, 407, 300, 311, 689,
  286, 4590, 493, 13, 400, 286, 632, 767, 3720, 51052], "temperature": 0.0, "avg_logprob":
  -0.1347291197957872, "compression_ratio": 1.4646464646464648, "no_speech_prob":
  0.0005540549173019826}, {"id": 126, "seek": 68688, "start": 700.64, "end": 709.4399999999999,
  "text": " a blog post in 2019, you know, about, and I think that post was, you know,
  widely accepted by", "tokens": [51052, 257, 6968, 2183, 294, 6071, 11, 291, 458,
  11, 466, 11, 293, 286, 519, 300, 2183, 390, 11, 291, 458, 11, 13371, 9035, 538,
  51492], "temperature": 0.0, "avg_logprob": -0.1347291197957872, "compression_ratio":
  1.4646464646464648, "no_speech_prob": 0.0005540549173019826}, {"id": 127, "seek":
  70944, "start": 709.44, "end": 718.5600000000001, "text": " community, it''s still
  in the open source connections blog. And it was really, it was really showing like,",
  "tokens": [50364, 1768, 11, 309, 311, 920, 294, 264, 1269, 4009, 9271, 6968, 13,
  400, 309, 390, 534, 11, 309, 390, 534, 4099, 411, 11, 50820], "temperature": 0.0,
  "avg_logprob": -0.1168779797024197, "compression_ratio": 1.7387387387387387, "no_speech_prob":
  0.002807541051879525}, {"id": 128, "seek": 70944, "start": 718.5600000000001, "end":
  723.0400000000001, "text": " hey, this is, this is a change, you know, it''s not
  just Google that''s going to be doing this.", "tokens": [50820, 4177, 11, 341, 307,
  11, 341, 307, 257, 1319, 11, 291, 458, 11, 309, 311, 406, 445, 3329, 300, 311, 516,
  281, 312, 884, 341, 13, 51044], "temperature": 0.0, "avg_logprob": -0.1168779797024197,
  "compression_ratio": 1.7387387387387387, "no_speech_prob": 0.002807541051879525},
  {"id": 129, "seek": 70944, "start": 723.0400000000001, "end": 728.8000000000001,
  "text": " Like, this is really interesting. And a lot of people agreed and there''s,
  there was like this", "tokens": [51044, 1743, 11, 341, 307, 534, 1880, 13, 400,
  257, 688, 295, 561, 9166, 293, 456, 311, 11, 456, 390, 411, 341, 51332], "temperature":
  0.0, "avg_logprob": -0.1168779797024197, "compression_ratio": 1.7387387387387387,
  "no_speech_prob": 0.002807541051879525}, {"id": 130, "seek": 70944, "start": 728.8000000000001,
  "end": 734.6400000000001, "text": " movement that kind of happened after that. And
  a lot of other people were coming to the same", "tokens": [51332, 3963, 300, 733,
  295, 2011, 934, 300, 13, 400, 257, 688, 295, 661, 561, 645, 1348, 281, 264, 912,
  51624], "temperature": 0.0, "avg_logprob": -0.1168779797024197, "compression_ratio":
  1.7387387387387387, "no_speech_prob": 0.002807541051879525}, {"id": 131, "seek":
  73464, "start": 734.64, "end": 742.96, "text": " conclusions, but there were a lot
  of challenges. So with vector search and approximate nearest", "tokens": [50364,
  22865, 11, 457, 456, 645, 257, 688, 295, 4759, 13, 407, 365, 8062, 3164, 293, 30874,
  23831, 50780], "temperature": 0.0, "avg_logprob": -0.1271048684914907, "compression_ratio":
  1.6905829596412556, "no_speech_prob": 0.002390810288488865}, {"id": 132, "seek":
  73464, "start": 742.96, "end": 752.96, "text": " neighbor search, you know, that''s,
  it would, that''s just the tool to solve the problem. It''s like,", "tokens": [50780,
  5987, 3164, 11, 291, 458, 11, 300, 311, 11, 309, 576, 11, 300, 311, 445, 264, 2290,
  281, 5039, 264, 1154, 13, 467, 311, 411, 11, 51280], "temperature": 0.0, "avg_logprob":
  -0.1271048684914907, "compression_ratio": 1.6905829596412556, "no_speech_prob":
  0.002390810288488865}, {"id": 133, "seek": 73464, "start": 752.96, "end": 756.48,
  "text": " you know, you start with this problem over here, and then you go like
  10 steps over here,", "tokens": [51280, 291, 458, 11, 291, 722, 365, 341, 1154,
  670, 510, 11, 293, 550, 291, 352, 411, 1266, 4439, 670, 510, 11, 51456], "temperature":
  0.0, "avg_logprob": -0.1271048684914907, "compression_ratio": 1.6905829596412556,
  "no_speech_prob": 0.002390810288488865}, {"id": 134, "seek": 73464, "start": 756.48,
  "end": 760.64, "text": " and finally, you get to vector searching. Okay, this is,
  this is a potential solution, right?", "tokens": [51456, 293, 2721, 11, 291, 483,
  281, 8062, 10808, 13, 1033, 11, 341, 307, 11, 341, 307, 257, 3995, 3827, 11, 558,
  30, 51664], "temperature": 0.0, "avg_logprob": -0.1271048684914907, "compression_ratio":
  1.6905829596412556, "no_speech_prob": 0.002390810288488865}, {"id": 135, "seek":
  76064, "start": 761.1999999999999, "end": 764.4, "text": " This is the core of the
  potential solution with all this stuff in the middle.", "tokens": [50392, 639, 307,
  264, 4965, 295, 264, 3995, 3827, 365, 439, 341, 1507, 294, 264, 2808, 13, 50552],
  "temperature": 0.0, "avg_logprob": -0.13434708913167318, "compression_ratio": 1.5319148936170213,
  "no_speech_prob": 0.0066062333062291145}, {"id": 136, "seek": 76064, "start": 765.84,
  "end": 772.56, "text": " Yeah, but have you felt that I should read this blog and
  we''ll definitely link it in the show notes.", "tokens": [50624, 865, 11, 457, 362,
  291, 2762, 300, 286, 820, 1401, 341, 6968, 293, 321, 603, 2138, 2113, 309, 294,
  264, 855, 5570, 13, 50960], "temperature": 0.0, "avg_logprob": -0.13434708913167318,
  "compression_ratio": 1.5319148936170213, "no_speech_prob": 0.0066062333062291145},
  {"id": 137, "seek": 76064, "start": 773.1999999999999, "end": 780.96, "text": "
  But sometimes when I look at vector search, let''s say demos or applications or
  algorithms,", "tokens": [50992, 583, 2171, 562, 286, 574, 412, 8062, 3164, 11, 718,
  311, 584, 33788, 420, 5821, 420, 14642, 11, 51380], "temperature": 0.0, "avg_logprob":
  -0.13434708913167318, "compression_ratio": 1.5319148936170213, "no_speech_prob":
  0.0066062333062291145}, {"id": 138, "seek": 76064, "start": 781.92, "end": 788.0,
  "text": " I get a feeling that you might just think, okay, I have a solution. Let
  me find a problem.", "tokens": [51428, 286, 483, 257, 2633, 300, 291, 1062, 445,
  519, 11, 1392, 11, 286, 362, 257, 3827, 13, 961, 385, 915, 257, 1154, 13, 51732],
  "temperature": 0.0, "avg_logprob": -0.13434708913167318, "compression_ratio": 1.5319148936170213,
  "no_speech_prob": 0.0066062333062291145}, {"id": 139, "seek": 78800, "start": 788.0,
  "end": 798.4, "text": " Because it''s, it''s all semitical. I mean, it''s so sexy,
  right? Do you, do you think this is one", "tokens": [50364, 1436, 309, 311, 11,
  309, 311, 439, 4361, 270, 804, 13, 286, 914, 11, 309, 311, 370, 13701, 11, 558,
  30, 1144, 291, 11, 360, 291, 519, 341, 307, 472, 50884], "temperature": 0.0, "avg_logprob":
  -0.2098242441813151, "compression_ratio": 1.566137566137566, "no_speech_prob": 0.008189880289137363},
  {"id": 140, "seek": 78800, "start": 798.4, "end": 804.88, "text": " of the sort
  of misconceptions, you know, in this field, or do you think that it''s well-past
  that already?", "tokens": [50884, 295, 264, 1333, 295, 50012, 11, 291, 458, 11,
  294, 341, 2519, 11, 420, 360, 291, 519, 300, 309, 311, 731, 12, 79, 525, 300, 1217,
  30, 51208], "temperature": 0.0, "avg_logprob": -0.2098242441813151, "compression_ratio":
  1.566137566137566, "no_speech_prob": 0.008189880289137363}, {"id": 141, "seek":
  78800, "start": 805.92, "end": 812.72, "text": " That''s a great question. I don''t
  know if, I don''t think it''s a solution looking for a problem.", "tokens": [51260,
  663, 311, 257, 869, 1168, 13, 286, 500, 380, 458, 498, 11, 286, 500, 380, 519, 309,
  311, 257, 3827, 1237, 337, 257, 1154, 13, 51600], "temperature": 0.0, "avg_logprob":
  -0.2098242441813151, "compression_ratio": 1.566137566137566, "no_speech_prob": 0.008189880289137363},
  {"id": 142, "seek": 81272, "start": 812.72, "end": 818.32, "text": " I don''t think
  that''s true. I think there, it actually does solve some problems.", "tokens": [50364,
  286, 500, 380, 519, 300, 311, 2074, 13, 286, 519, 456, 11, 309, 767, 775, 5039,
  512, 2740, 13, 50644], "temperature": 0.0, "avg_logprob": -0.1123572826385498, "compression_ratio":
  1.7188940092165899, "no_speech_prob": 0.0018509075744077563}, {"id": 143, "seek":
  81272, "start": 819.52, "end": 827.12, "text": " But I do agree that it gets, you
  know, there''s a lot of gray area. And how do you arrive at that", "tokens": [50704,
  583, 286, 360, 3986, 300, 309, 2170, 11, 291, 458, 11, 456, 311, 257, 688, 295,
  10855, 1859, 13, 400, 577, 360, 291, 8881, 412, 300, 51084], "temperature": 0.0,
  "avg_logprob": -0.1123572826385498, "compression_ratio": 1.7188940092165899, "no_speech_prob":
  0.0018509075744077563}, {"id": 144, "seek": 81272, "start": 827.12, "end": 833.28,
  "text": " from, I need to find things as a person? You know, and all the things
  that you have to go through", "tokens": [51084, 490, 11, 286, 643, 281, 915, 721,
  382, 257, 954, 30, 509, 458, 11, 293, 439, 264, 721, 300, 291, 362, 281, 352, 807,
  51392], "temperature": 0.0, "avg_logprob": -0.1123572826385498, "compression_ratio":
  1.7188940092165899, "no_speech_prob": 0.0018509075744077563}, {"id": 145, "seek":
  81272, "start": 833.28, "end": 838.72, "text": " until vector search actually means
  something that is a solution. I think there''s, there''s a lot of", "tokens": [51392,
  1826, 8062, 3164, 767, 1355, 746, 300, 307, 257, 3827, 13, 286, 519, 456, 311, 11,
  456, 311, 257, 688, 295, 51664], "temperature": 0.0, "avg_logprob": -0.1123572826385498,
  "compression_ratio": 1.7188940092165899, "no_speech_prob": 0.0018509075744077563},
  {"id": 146, "seek": 83872, "start": 838.72, "end": 842.24, "text": " people who
  picked it up and say, okay, we could just use this and it''s going to solve, solve
  these", "tokens": [50364, 561, 567, 6183, 309, 493, 293, 584, 11, 1392, 11, 321,
  727, 445, 764, 341, 293, 309, 311, 516, 281, 5039, 11, 5039, 613, 50540], "temperature":
  0.0, "avg_logprob": -0.13758413314819337, "compression_ratio": 1.5766129032258065,
  "no_speech_prob": 0.0017870538868010044}, {"id": 147, "seek": 83872, "start": 842.24,
  "end": 848.4, "text": " problems. But it doesn''t do that, right? Because search
  is not just about similarity, you know, you can", "tokens": [50540, 2740, 13, 583,
  309, 1177, 380, 360, 300, 11, 558, 30, 1436, 3164, 307, 406, 445, 466, 32194, 11,
  291, 458, 11, 291, 393, 50848], "temperature": 0.0, "avg_logprob": -0.13758413314819337,
  "compression_ratio": 1.5766129032258065, "no_speech_prob": 0.0017870538868010044},
  {"id": 148, "seek": 83872, "start": 848.4, "end": 856.64, "text": " express a query
  similarity with a document using TFI DFBM25, you know, the sentence transformer,",
  "tokens": [50848, 5109, 257, 14581, 32194, 365, 257, 4166, 1228, 314, 38568, 48336,
  18345, 6074, 11, 291, 458, 11, 264, 8174, 31782, 11, 51260], "temperature": 0.0,
  "avg_logprob": -0.13758413314819337, "compression_ratio": 1.5766129032258065, "no_speech_prob":
  0.0017870538868010044}, {"id": 149, "seek": 83872, "start": 856.64, "end": 863.2,
  "text": " you know, cosine distance, whatever. But that''s only the similarity.
  There''s also like the,", "tokens": [51260, 291, 458, 11, 23565, 4560, 11, 2035,
  13, 583, 300, 311, 787, 264, 32194, 13, 821, 311, 611, 411, 264, 11, 51588], "temperature":
  0.0, "avg_logprob": -0.13758413314819337, "compression_ratio": 1.5766129032258065,
  "no_speech_prob": 0.0017870538868010044}, {"id": 150, "seek": 86320, "start": 863.2800000000001,
  "end": 868.32, "text": " the need that the person has to what they have. So it''s,
  it''s a bunch of", "tokens": [50368, 264, 643, 300, 264, 954, 575, 281, 437, 436,
  362, 13, 407, 309, 311, 11, 309, 311, 257, 3840, 295, 50620], "temperature": 0.0,
  "avg_logprob": -0.09141857856142838, "compression_ratio": 1.7549407114624507, "no_speech_prob":
  0.00377467623911798}, {"id": 151, "seek": 86320, "start": 869.5200000000001, "end":
  873.84, "text": " candidate documents that are similar, but what''s the actual document
  you need? So that''s where a lot", "tokens": [50680, 11532, 8512, 300, 366, 2531,
  11, 457, 437, 311, 264, 3539, 4166, 291, 643, 30, 407, 300, 311, 689, 257, 688,
  50896], "temperature": 0.0, "avg_logprob": -0.09141857856142838, "compression_ratio":
  1.7549407114624507, "no_speech_prob": 0.00377467623911798}, {"id": 152, "seek":
  86320, "start": 873.84, "end": 878.88, "text": " of other things come into play.
  It''s just one piece in a much larger search or recommendations", "tokens": [50896,
  295, 661, 721, 808, 666, 862, 13, 467, 311, 445, 472, 2522, 294, 257, 709, 4833,
  3164, 420, 10434, 51148], "temperature": 0.0, "avg_logprob": -0.09141857856142838,
  "compression_ratio": 1.7549407114624507, "no_speech_prob": 0.00377467623911798},
  {"id": 153, "seek": 86320, "start": 878.88, "end": 883.76, "text": " platform, you
  know, you still have to take on all the other signals and, you know,", "tokens":
  [51148, 3663, 11, 291, 458, 11, 291, 920, 362, 281, 747, 322, 439, 264, 661, 12354,
  293, 11, 291, 458, 11, 51392], "temperature": 0.0, "avg_logprob": -0.09141857856142838,
  "compression_ratio": 1.7549407114624507, "no_speech_prob": 0.00377467623911798},
  {"id": 154, "seek": 86320, "start": 885.36, "end": 890.48, "text": " common now
  in the, in the more mature platforms is, you know, you have some learning to rank",
  "tokens": [51472, 2689, 586, 294, 264, 11, 294, 264, 544, 14442, 9473, 307, 11,
  291, 458, 11, 291, 362, 512, 2539, 281, 6181, 51728], "temperature": 0.0, "avg_logprob":
  -0.09141857856142838, "compression_ratio": 1.7549407114624507, "no_speech_prob":
  0.00377467623911798}, {"id": 155, "seek": 89048, "start": 890.48, "end": 896.48,
  "text": " algorithm that takes, you know, me and Vector similarity is one, is one
  feature in, in a learning", "tokens": [50364, 9284, 300, 2516, 11, 291, 458, 11,
  385, 293, 691, 20814, 32194, 307, 472, 11, 307, 472, 4111, 294, 11, 294, 257, 2539,
  50664], "temperature": 0.0, "avg_logprob": -0.20427821766246448, "compression_ratio":
  1.6428571428571428, "no_speech_prob": 0.0007845693035051227}, {"id": 156, "seek":
  89048, "start": 896.48, "end": 902.64, "text": " to rank model. Along with, you
  know, BM25 with the title, BM25 with the body, you know, the number of", "tokens":
  [50664, 281, 6181, 2316, 13, 17457, 365, 11, 291, 458, 11, 15901, 6074, 365, 264,
  4876, 11, 15901, 6074, 365, 264, 1772, 11, 291, 458, 11, 264, 1230, 295, 50972],
  "temperature": 0.0, "avg_logprob": -0.20427821766246448, "compression_ratio": 1.6428571428571428,
  "no_speech_prob": 0.0007845693035051227}, {"id": 157, "seek": 89048, "start": 903.36,
  "end": 909.76, "text": " clicks, the date, all this other stuff. And it''s, it''s
  a piece. But the thing that the piece", "tokens": [51008, 18521, 11, 264, 4002,
  11, 439, 341, 661, 1507, 13, 400, 309, 311, 11, 309, 311, 257, 2522, 13, 583, 264,
  551, 300, 264, 2522, 51328], "temperature": 0.0, "avg_logprob": -0.20427821766246448,
  "compression_ratio": 1.6428571428571428, "no_speech_prob": 0.0007845693035051227},
  {"id": 158, "seek": 89048, "start": 909.76, "end": 919.6, "text": " solves is that
  query term dependence problem, whereas like I don''t have to, in a, in a, sometimes,",
  "tokens": [51328, 39890, 307, 300, 14581, 1433, 31704, 1154, 11, 9735, 411, 286,
  500, 380, 362, 281, 11, 294, 257, 11, 294, 257, 11, 2171, 11, 51820], "temperature":
  0.0, "avg_logprob": -0.20427821766246448, "compression_ratio": 1.6428571428571428,
  "no_speech_prob": 0.0007845693035051227}, {"id": 159, "seek": 91960, "start": 919.6,
  "end": 923.9200000000001, "text": " you know, I don''t have to go in and, and craft
  synonyms by hand, and I don''t have this endless task of", "tokens": [50364, 291,
  458, 11, 286, 500, 380, 362, 281, 352, 294, 293, 11, 293, 8448, 5451, 2526, 2592,
  538, 1011, 11, 293, 286, 500, 380, 362, 341, 16144, 5633, 295, 50580], "temperature":
  0.0, "avg_logprob": -0.17329160902235244, "compression_ratio": 1.8160919540229885,
  "no_speech_prob": 0.0018212435534223914}, {"id": 160, "seek": 91960, "start": 923.9200000000001,
  "end": 927.84, "text": " doing that. You just, you kind of have all these other
  tasks that you still have to do, but", "tokens": [50580, 884, 300, 13, 509, 445,
  11, 291, 733, 295, 362, 439, 613, 661, 9608, 300, 291, 920, 362, 281, 360, 11, 457,
  50776], "temperature": 0.0, "avg_logprob": -0.17329160902235244, "compression_ratio":
  1.8160919540229885, "no_speech_prob": 0.0018212435534223914}, {"id": 161, "seek":
  91960, "start": 928.48, "end": 934.8000000000001, "text": " that one maybe has kept
  it bay a little bit. Yeah, yeah, absolutely. I mean, maybe I can", "tokens": [50808,
  300, 472, 1310, 575, 4305, 309, 13642, 257, 707, 857, 13, 865, 11, 1338, 11, 3122,
  13, 286, 914, 11, 1310, 286, 393, 51124], "temperature": 0.0, "avg_logprob": -0.17329160902235244,
  "compression_ratio": 1.8160919540229885, "no_speech_prob": 0.0018212435534223914},
  {"id": 162, "seek": 91960, "start": 935.76, "end": 942.64, "text": " a little bit
  like, restate my question, or sort of like, clarify what I meant, I guess, when
  you read,", "tokens": [51172, 257, 707, 857, 411, 11, 1472, 473, 452, 1168, 11,
  420, 1333, 295, 411, 11, 17594, 437, 286, 4140, 11, 286, 2041, 11, 562, 291, 1401,
  11, 51516], "temperature": 0.0, "avg_logprob": -0.17329160902235244, "compression_ratio":
  1.8160919540229885, "no_speech_prob": 0.0018212435534223914}, {"id": 163, "seek":
  91960, "start": 943.36, "end": 948.72, "text": " I think when you read the paper,
  like, birth or similar papers, they also say, hey, we,", "tokens": [51552, 286,
  519, 562, 291, 1401, 264, 3035, 11, 411, 11, 3965, 420, 2531, 10577, 11, 436, 611,
  584, 11, 4177, 11, 321, 11, 51820], "temperature": 0.0, "avg_logprob": -0.17329160902235244,
  "compression_ratio": 1.8160919540229885, "no_speech_prob": 0.0018212435534223914},
  {"id": 164, "seek": 94960, "start": 950.08, "end": 955.2, "text": " we ran down
  this on downstream task, like sentiment analysis, we also did question answering,",
  "tokens": [50388, 321, 5872, 760, 341, 322, 30621, 5633, 11, 411, 16149, 5215, 11,
  321, 611, 630, 1168, 13430, 11, 50644], "temperature": 0.0, "avg_logprob": -0.13802738811658777,
  "compression_ratio": 1.6276150627615062, "no_speech_prob": 0.0023776732850819826},
  {"id": 165, "seek": 94960, "start": 955.2, "end": 960.4, "text": " we did recommendation,
  all these other things. And it works great. Which kind of like pushes you", "tokens":
  [50644, 321, 630, 11879, 11, 439, 613, 661, 721, 13, 400, 309, 1985, 869, 13, 3013,
  733, 295, 411, 21020, 291, 50904], "temperature": 0.0, "avg_logprob": -0.13802738811658777,
  "compression_ratio": 1.6276150627615062, "no_speech_prob": 0.0023776732850819826},
  {"id": 166, "seek": 94960, "start": 960.4, "end": 966.72, "text": " to think in
  the direction that is this a universal language model or approach that I can now
  take", "tokens": [50904, 281, 519, 294, 264, 3513, 300, 307, 341, 257, 11455, 2856,
  2316, 420, 3109, 300, 286, 393, 586, 747, 51220], "temperature": 0.0, "avg_logprob":
  -0.13802738811658777, "compression_ratio": 1.6276150627615062, "no_speech_prob":
  0.0023776732850819826}, {"id": 167, "seek": 94960, "start": 966.72, "end": 973.2,
  "text": " and apply to everywhere, every task. And the answer is actually no, because,
  hey, I mean, if you are", "tokens": [51220, 293, 3079, 281, 5315, 11, 633, 5633,
  13, 400, 264, 1867, 307, 767, 572, 11, 570, 11, 4177, 11, 286, 914, 11, 498, 291,
  366, 51544], "temperature": 0.0, "avg_logprob": -0.13802738811658777, "compression_ratio":
  1.6276150627615062, "no_speech_prob": 0.0023776732850819826}, {"id": 168, "seek":
  97320, "start": 973.2, "end": 979.9200000000001, "text": " in healthcare and they
  trained on news, it''s not going to work. So the vocabulary still was not", "tokens":
  [50364, 294, 8884, 293, 436, 8895, 322, 2583, 11, 309, 311, 406, 516, 281, 589,
  13, 407, 264, 19864, 920, 390, 406, 50700], "temperature": 0.0, "avg_logprob": -0.16023155428328603,
  "compression_ratio": 1.588235294117647, "no_speech_prob": 0.007176055572926998},
  {"id": 169, "seek": 97320, "start": 979.9200000000001, "end": 986.32, "text": "
  excluded from this journey. So if it''s mismatch, it''s mismatch. But the model
  itself, of course,", "tokens": [50700, 29486, 490, 341, 4671, 13, 407, 498, 309,
  311, 23220, 852, 11, 309, 311, 23220, 852, 13, 583, 264, 2316, 2564, 11, 295, 1164,
  11, 51020], "temperature": 0.0, "avg_logprob": -0.16023155428328603, "compression_ratio":
  1.588235294117647, "no_speech_prob": 0.007176055572926998}, {"id": 170, "seek":
  97320, "start": 986.32, "end": 992.72, "text": " is a clever piece of, you know,
  attack, which you can then take and kind of apply fine tune, maybe,", "tokens":
  [51020, 307, 257, 13494, 2522, 295, 11, 291, 458, 11, 2690, 11, 597, 291, 393, 550,
  747, 293, 733, 295, 3079, 2489, 10864, 11, 1310, 11, 51340], "temperature": 0.0,
  "avg_logprob": -0.16023155428328603, "compression_ratio": 1.588235294117647, "no_speech_prob":
  0.007176055572926998}, {"id": 171, "seek": 97320, "start": 992.72, "end": 1000.72,
  "text": " or retrain on your data. So I think that that''s, that''s one way to look
  at it, right?", "tokens": [51340, 420, 1533, 7146, 322, 428, 1412, 13, 407, 286,
  519, 300, 300, 311, 11, 300, 311, 472, 636, 281, 574, 412, 309, 11, 558, 30, 51740],
  "temperature": 0.0, "avg_logprob": -0.16023155428328603, "compression_ratio": 1.588235294117647,
  "no_speech_prob": 0.007176055572926998}, {"id": 172, "seek": 100072, "start": 1000.96,
  "end": 1010.96, "text": " It is, but I think that we, we see a huge, still a huge
  gap in the domain, right? I think there", "tokens": [50376, 467, 307, 11, 457, 286,
  519, 300, 321, 11, 321, 536, 257, 2603, 11, 920, 257, 2603, 7417, 294, 264, 9274,
  11, 558, 30, 286, 519, 456, 50876], "temperature": 0.0, "avg_logprob": -0.1841632544276226,
  "compression_ratio": 1.5966850828729282, "no_speech_prob": 0.010473725385963917},
  {"id": 173, "seek": 100072, "start": 1010.96, "end": 1016.4, "text": " are a lot
  of organizations that can just make use of retrain models and fine tune them. But,",
  "tokens": [50876, 366, 257, 688, 295, 6150, 300, 393, 445, 652, 764, 295, 1533,
  7146, 5245, 293, 2489, 10864, 552, 13, 583, 11, 51148], "temperature": 0.0, "avg_logprob":
  -0.1841632544276226, "compression_ratio": 1.5966850828729282, "no_speech_prob":
  0.010473725385963917}, {"id": 174, "seek": 100072, "start": 1018.08, "end": 1023.9200000000001,
  "text": " you know, we, I know that there are still domains that you can''t do that.
  Like, if you go up and you", "tokens": [51232, 291, 458, 11, 321, 11, 286, 458,
  300, 456, 366, 920, 25514, 300, 291, 393, 380, 360, 300, 13, 1743, 11, 498, 291,
  352, 493, 293, 291, 51524], "temperature": 0.0, "avg_logprob": -0.1841632544276226,
  "compression_ratio": 1.5966850828729282, "no_speech_prob": 0.010473725385963917},
  {"id": 175, "seek": 102392, "start": 1023.92, "end": 1032.56, "text": " try, you
  know, something that''s fine tuned, like law, right? Law is like its own language.
  I wouldn''t", "tokens": [50364, 853, 11, 291, 458, 11, 746, 300, 311, 2489, 10870,
  11, 411, 2101, 11, 558, 30, 7744, 307, 411, 1080, 1065, 2856, 13, 286, 2759, 380,
  50796], "temperature": 0.0, "avg_logprob": -0.10807442429042098, "compression_ratio":
  1.75, "no_speech_prob": 0.0016423448687419295}, {"id": 176, "seek": 102392, "start":
  1032.56, "end": 1037.68, "text": " even, like law written in English, I wouldn''t
  even call that English. I''d call that, you know, legal", "tokens": [50796, 754,
  11, 411, 2101, 3720, 294, 3669, 11, 286, 2759, 380, 754, 818, 300, 3669, 13, 286,
  1116, 818, 300, 11, 291, 458, 11, 5089, 51052], "temperature": 0.0, "avg_logprob":
  -0.10807442429042098, "compression_ratio": 1.75, "no_speech_prob": 0.0016423448687419295},
  {"id": 177, "seek": 102392, "start": 1037.68, "end": 1046.8, "text": " English,
  right? Because just the structure, the vocabulary, the grammar, all this stuff is
  so", "tokens": [51052, 3669, 11, 558, 30, 1436, 445, 264, 3877, 11, 264, 19864,
  11, 264, 22317, 11, 439, 341, 1507, 307, 370, 51508], "temperature": 0.0, "avg_logprob":
  -0.10807442429042098, "compression_ratio": 1.75, "no_speech_prob": 0.0016423448687419295},
  {"id": 178, "seek": 102392, "start": 1046.8, "end": 1051.92, "text": " different
  than what''s in like a Wikipedia article or in the news or something like that,
  right?", "tokens": [51508, 819, 813, 437, 311, 294, 411, 257, 28999, 7222, 420,
  294, 264, 2583, 420, 746, 411, 300, 11, 558, 30, 51764], "temperature": 0.0, "avg_logprob":
  -0.10807442429042098, "compression_ratio": 1.75, "no_speech_prob": 0.0016423448687419295},
  {"id": 179, "seek": 105192, "start": 1052.4, "end": 1060.0, "text": " So, when you
  try to do a fine tuning on a pretrained model that''s trained on, you know, let''s
  say like", "tokens": [50388, 407, 11, 562, 291, 853, 281, 360, 257, 2489, 15164,
  322, 257, 1162, 31774, 2316, 300, 311, 8895, 322, 11, 291, 458, 11, 718, 311, 584,
  411, 50768], "temperature": 0.0, "avg_logprob": -0.20728203685013288, "compression_ratio":
  1.6434782608695653, "no_speech_prob": 0.0008146049221977592}, {"id": 180, "seek":
  105192, "start": 1060.0, "end": 1065.04, "text": " onto notice 5, which is a bunch
  of collections of like, you know, news, Wikipedia, like general", "tokens": [50768,
  3911, 3449, 1025, 11, 597, 307, 257, 3840, 295, 16641, 295, 411, 11, 291, 458, 11,
  2583, 11, 28999, 11, 411, 2674, 51020], "temperature": 0.0, "avg_logprob": -0.20728203685013288,
  "compression_ratio": 1.6434782608695653, "no_speech_prob": 0.0008146049221977592},
  {"id": 181, "seek": 105192, "start": 1065.04, "end": 1070.88, "text": " knowledge
  that most people use. When you find tune it, there''s still a gap. There''s, there''s",
  "tokens": [51020, 3601, 300, 881, 561, 764, 13, 1133, 291, 915, 10864, 309, 11,
  456, 311, 920, 257, 7417, 13, 821, 311, 11, 456, 311, 51312], "temperature": 0.0,
  "avg_logprob": -0.20728203685013288, "compression_ratio": 1.6434782608695653, "no_speech_prob":
  0.0008146049221977592}, {"id": 182, "seek": 105192, "start": 1070.88, "end": 1078.48,
  "text": " something missing, right? Because the original trained model was lacking
  this context.", "tokens": [51312, 746, 5361, 11, 558, 30, 1436, 264, 3380, 8895,
  2316, 390, 20889, 341, 4319, 13, 51692], "temperature": 0.0, "avg_logprob": -0.20728203685013288,
  "compression_ratio": 1.6434782608695653, "no_speech_prob": 0.0008146049221977592},
  {"id": 183, "seek": 107848, "start": 1079.2, "end": 1087.52, "text": " And that''s,
  that''s only for the content also. That''s just, that''s just the content. And when
  people", "tokens": [50400, 400, 300, 311, 11, 300, 311, 787, 337, 264, 2701, 611,
  13, 663, 311, 445, 11, 300, 311, 445, 264, 2701, 13, 400, 562, 561, 50816], "temperature":
  0.0, "avg_logprob": -0.1696626773247352, "compression_ratio": 1.8064516129032258,
  "no_speech_prob": 0.004847658798098564}, {"id": 184, "seek": 107848, "start": 1087.52,
  "end": 1092.8, "text": " search and they type in terms, you know, you can imagine
  like this, this Venn diagram of like,", "tokens": [50816, 3164, 293, 436, 2010,
  294, 2115, 11, 291, 458, 11, 291, 393, 3811, 411, 341, 11, 341, 691, 1857, 10686,
  295, 411, 11, 51080], "temperature": 0.0, "avg_logprob": -0.1696626773247352, "compression_ratio":
  1.8064516129032258, "no_speech_prob": 0.004847658798098564}, {"id": 185, "seek":
  107848, "start": 1092.8, "end": 1097.04, "text": " well, here''s, here''s all of
  the content over here that you''ve trained on. And then here''s all the", "tokens":
  [51080, 731, 11, 510, 311, 11, 510, 311, 439, 295, 264, 2701, 670, 510, 300, 291,
  600, 8895, 322, 13, 400, 550, 510, 311, 439, 264, 51292], "temperature": 0.0, "avg_logprob":
  -0.1696626773247352, "compression_ratio": 1.8064516129032258, "no_speech_prob":
  0.004847658798098564}, {"id": 186, "seek": 107848, "start": 1097.04, "end": 1101.52,
  "text": " terms that your people, that the users know, right? And you try to like
  bring these closer together", "tokens": [51292, 2115, 300, 428, 561, 11, 300, 264,
  5022, 458, 11, 558, 30, 400, 291, 853, 281, 411, 1565, 613, 4966, 1214, 51516],
  "temperature": 0.0, "avg_logprob": -0.1696626773247352, "compression_ratio": 1.8064516129032258,
  "no_speech_prob": 0.004847658798098564}, {"id": 187, "seek": 110152, "start": 1101.6,
  "end": 1111.84, "text": " somehow, right? If the model was trained on content that
  is like up here, then you''re going to have", "tokens": [50368, 6063, 11, 558, 30,
  759, 264, 2316, 390, 8895, 322, 2701, 300, 307, 411, 493, 510, 11, 550, 291, 434,
  516, 281, 362, 50880], "temperature": 0.0, "avg_logprob": -0.15758652262168354,
  "compression_ratio": 1.6147540983606556, "no_speech_prob": 0.01173362322151661},
  {"id": 188, "seek": 110152, "start": 1111.84, "end": 1116.16, "text": " trouble
  like kind of putting it together. I don''t know if you can do a good job in my hands
  showing", "tokens": [50880, 5253, 411, 733, 295, 3372, 309, 1214, 13, 286, 500,
  380, 458, 498, 291, 393, 360, 257, 665, 1691, 294, 452, 2377, 4099, 51096], "temperature":
  0.0, "avg_logprob": -0.15758652262168354, "compression_ratio": 1.6147540983606556,
  "no_speech_prob": 0.01173362322151661}, {"id": 189, "seek": 110152, "start": 1116.16,
  "end": 1124.8, "text": " this, but no, you''re doing perfect job there. So I think
  that one of the one of the big existing", "tokens": [51096, 341, 11, 457, 572, 11,
  291, 434, 884, 2176, 1691, 456, 13, 407, 286, 519, 300, 472, 295, 264, 472, 295,
  264, 955, 6741, 51528], "temperature": 0.0, "avg_logprob": -0.15758652262168354,
  "compression_ratio": 1.6147540983606556, "no_speech_prob": 0.01173362322151661},
  {"id": 190, "seek": 110152, "start": 1124.8, "end": 1130.56, "text": " problems
  is pre-training still costs like a ridiculous amount of money and is out of the
  reach of", "tokens": [51528, 2740, 307, 659, 12, 17227, 1760, 920, 5497, 411, 257,
  11083, 2372, 295, 1460, 293, 307, 484, 295, 264, 2524, 295, 51816], "temperature":
  0.0, "avg_logprob": -0.15758652262168354, "compression_ratio": 1.6147540983606556,
  "no_speech_prob": 0.01173362322151661}, {"id": 191, "seek": 113056, "start": 1130.56,
  "end": 1139.76, "text": " most teams. Yeah, I''ve read, I''ve read papers, you know,
  one of them was by Microsoft showing like,", "tokens": [50364, 881, 5491, 13, 865,
  11, 286, 600, 1401, 11, 286, 600, 1401, 10577, 11, 291, 458, 11, 472, 295, 552,
  390, 538, 8116, 4099, 411, 11, 50824], "temperature": 0.0, "avg_logprob": -0.11304883858592239,
  "compression_ratio": 1.6563876651982379, "no_speech_prob": 0.0005696497391909361},
  {"id": 192, "seek": 113056, "start": 1139.76, "end": 1144.24, "text": " if you,
  you know, the bird vocabulary is like 30,000 words or something like that. If you
  increase", "tokens": [50824, 498, 291, 11, 291, 458, 11, 264, 5255, 19864, 307,
  411, 2217, 11, 1360, 2283, 420, 746, 411, 300, 13, 759, 291, 3488, 51048], "temperature":
  0.0, "avg_logprob": -0.11304883858592239, "compression_ratio": 1.6563876651982379,
  "no_speech_prob": 0.0005696497391909361}, {"id": 193, "seek": 113056, "start": 1144.24,
  "end": 1154.8, "text": " the vocabulary size to like 100,000 words, then the model
  generalizes much better. And you,", "tokens": [51048, 264, 19864, 2744, 281, 411,
  2319, 11, 1360, 2283, 11, 550, 264, 2316, 2674, 5660, 709, 1101, 13, 400, 291, 11,
  51576], "temperature": 0.0, "avg_logprob": -0.11304883858592239, "compression_ratio":
  1.6563876651982379, "no_speech_prob": 0.0005696497391909361}, {"id": 194, "seek":
  113056, "start": 1154.8, "end": 1157.9199999999998, "text": " of course, you expand
  the content and the domains that are involved in that training.", "tokens": [51576,
  295, 1164, 11, 291, 5268, 264, 2701, 293, 264, 25514, 300, 366, 3288, 294, 300,
  3097, 13, 51732], "temperature": 0.0, "avg_logprob": -0.11304883858592239, "compression_ratio":
  1.6563876651982379, "no_speech_prob": 0.0005696497391909361}, {"id": 195, "seek":
  115792, "start": 1158.4, "end": 1166.3200000000002, "text": " So I think you, I
  think we''re going to see some more of that. The world is still stuck on this 30,000",
  "tokens": [50388, 407, 286, 519, 291, 11, 286, 519, 321, 434, 516, 281, 536, 512,
  544, 295, 300, 13, 440, 1002, 307, 920, 5541, 322, 341, 2217, 11, 1360, 50784],
  "temperature": 0.0, "avg_logprob": -0.16254050835319186, "compression_ratio": 1.58008658008658,
  "no_speech_prob": 0.002149689244106412}, {"id": 196, "seek": 115792, "start": 1166.3200000000002,
  "end": 1173.44, "text": " terms in the pre-trained space of things like onto notes
  because it''s just so expensive,", "tokens": [50784, 2115, 294, 264, 659, 12, 17227,
  2001, 1901, 295, 721, 411, 3911, 5570, 570, 309, 311, 445, 370, 5124, 11, 51140],
  "temperature": 0.0, "avg_logprob": -0.16254050835319186, "compression_ratio": 1.58008658008658,
  "no_speech_prob": 0.002149689244106412}, {"id": 197, "seek": 115792, "start": 1173.44,
  "end": 1178.3200000000002, "text": " it''s train models and Google and Microsoft
  and Facebook and these companies that train models,", "tokens": [51140, 309, 311,
  3847, 5245, 293, 3329, 293, 8116, 293, 4384, 293, 613, 3431, 300, 3847, 5245, 11,
  51384], "temperature": 0.0, "avg_logprob": -0.16254050835319186, "compression_ratio":
  1.58008658008658, "no_speech_prob": 0.002149689244106412}, {"id": 198, "seek": 115792,
  "start": 1178.3200000000002, "end": 1182.96, "text": " they''re not going to bother
  open sourcing those. Maybe they will at some point,", "tokens": [51384, 436, 434,
  406, 516, 281, 8677, 1269, 11006, 2175, 729, 13, 2704, 436, 486, 412, 512, 935,
  11, 51616], "temperature": 0.0, "avg_logprob": -0.16254050835319186, "compression_ratio":
  1.58008658008658, "no_speech_prob": 0.002149689244106412}, {"id": 199, "seek": 118296,
  "start": 1183.04, "end": 1187.8400000000001, "text": " but I think we''re going
  to need to see big companies that are specific in that domain,", "tokens": [50368,
  457, 286, 519, 321, 434, 516, 281, 643, 281, 536, 955, 3431, 300, 366, 2685, 294,
  300, 9274, 11, 50608], "temperature": 0.0, "avg_logprob": -0.1331671679461444, "compression_ratio":
  1.8611111111111112, "no_speech_prob": 0.0076689026318490505}, {"id": 200, "seek":
  118296, "start": 1187.8400000000001, "end": 1192.64, "text": " train those models
  and then open sourcing them. But if you spend millions of dollars to train a model",
  "tokens": [50608, 3847, 729, 5245, 293, 550, 1269, 11006, 2175, 552, 13, 583, 498,
  291, 3496, 6803, 295, 3808, 281, 3847, 257, 2316, 50848], "temperature": 0.0, "avg_logprob":
  -0.1331671679461444, "compression_ratio": 1.8611111111111112, "no_speech_prob":
  0.0076689026318490505}, {"id": 201, "seek": 118296, "start": 1192.64, "end": 1197.76,
  "text": " and you''re a big private company, are you going to open sourcing the
  model weights? Probably not,", "tokens": [50848, 293, 291, 434, 257, 955, 4551,
  2237, 11, 366, 291, 516, 281, 1269, 11006, 2175, 264, 2316, 17443, 30, 9210, 406,
  11, 51104], "temperature": 0.0, "avg_logprob": -0.1331671679461444, "compression_ratio":
  1.8611111111111112, "no_speech_prob": 0.0076689026318490505}, {"id": 202, "seek":
  118296, "start": 1197.76, "end": 1201.92, "text": " you''re going to keep it for
  yourself because that''s huge value, it''s huge value for your product.", "tokens":
  [51104, 291, 434, 516, 281, 1066, 309, 337, 1803, 570, 300, 311, 2603, 2158, 11,
  309, 311, 2603, 2158, 337, 428, 1674, 13, 51312], "temperature": 0.0, "avg_logprob":
  -0.1331671679461444, "compression_ratio": 1.8611111111111112, "no_speech_prob":
  0.0076689026318490505}, {"id": 203, "seek": 118296, "start": 1203.2, "end": 1206.96,
  "text": " I guess you open sourced the idea sort of if you publish, okay, here''s
  the bird model,", "tokens": [51376, 286, 2041, 291, 1269, 11006, 1232, 264, 1558,
  1333, 295, 498, 291, 11374, 11, 1392, 11, 510, 311, 264, 5255, 2316, 11, 51564],
  "temperature": 0.0, "avg_logprob": -0.1331671679461444, "compression_ratio": 1.8611111111111112,
  "no_speech_prob": 0.0076689026318490505}, {"id": 204, "seek": 118296, "start": 1206.96,
  "end": 1210.8, "text": " here''s the mom model or whatever. But then go train it
  yourself.", "tokens": [51564, 510, 311, 264, 1225, 2316, 420, 2035, 13, 583, 550,
  352, 3847, 309, 1803, 13, 51756], "temperature": 0.0, "avg_logprob": -0.1331671679461444,
  "compression_ratio": 1.8611111111111112, "no_speech_prob": 0.0076689026318490505},
  {"id": 205, "seek": 121080, "start": 1210.8, "end": 1215.12, "text": " Yeah, yeah,
  if you have a couple million dollars lying around.", "tokens": [50364, 865, 11,
  1338, 11, 498, 291, 362, 257, 1916, 2459, 3808, 8493, 926, 13, 50580], "temperature":
  0.0, "avg_logprob": -0.2861937673468339, "compression_ratio": 1.525, "no_speech_prob":
  0.014519112184643745}, {"id": 206, "seek": 121080, "start": 1215.12, "end": 1221.6,
  "text": " Yeah, and then I was also talking to in another episode, I mean, Ahmaad,
  who used to work at Google,", "tokens": [50580, 865, 11, 293, 550, 286, 390, 611,
  1417, 281, 294, 1071, 3500, 11, 286, 914, 11, 2438, 1696, 345, 11, 567, 1143, 281,
  589, 412, 3329, 11, 50904], "temperature": 0.0, "avg_logprob": -0.2861937673468339,
  "compression_ratio": 1.525, "no_speech_prob": 0.014519112184643745}, {"id": 207,
  "seek": 121080, "start": 1222.24, "end": 1231.04, "text": " and he said that entire
  teams would be dedicated on a quarterly basis to do the expensive fine-tuning work",
  "tokens": [50936, 293, 415, 848, 300, 2302, 5491, 576, 312, 8374, 322, 257, 38633,
  5143, 281, 360, 264, 5124, 2489, 12, 83, 37726, 589, 51376], "temperature": 0.0,
  "avg_logprob": -0.2861937673468339, "compression_ratio": 1.525, "no_speech_prob":
  0.014519112184643745}, {"id": 208, "seek": 121080, "start": 1231.84, "end": 1237.68,
  "text": " with burrito similar models. So can you imagine that it''s like a team''s
  effort and this people,", "tokens": [51416, 365, 2779, 17492, 2531, 5245, 13, 407,
  393, 291, 3811, 300, 309, 311, 411, 257, 1469, 311, 4630, 293, 341, 561, 11, 51708],
  "temperature": 0.0, "avg_logprob": -0.2861937673468339, "compression_ratio": 1.525,
  "no_speech_prob": 0.014519112184643745}, {"id": 209, "seek": 123768, "start": 1237.68,
  "end": 1243.8400000000001, "text": " some of them invented the model, some of them
  didn''t, but you know, with all the resources that Google", "tokens": [50364, 512,
  295, 552, 14479, 264, 2316, 11, 512, 295, 552, 994, 380, 11, 457, 291, 458, 11,
  365, 439, 264, 3593, 300, 3329, 50672], "temperature": 0.0, "avg_logprob": -0.14056586344307714,
  "compression_ratio": 1.6791666666666667, "no_speech_prob": 0.01326596550643444},
  {"id": 210, "seek": 123768, "start": 1243.8400000000001, "end": 1250.96, "text":
  " has to fine tune them for three months. So I don''t think this is out of reach
  of startups. And I mean,", "tokens": [50672, 575, 281, 2489, 10864, 552, 337, 1045,
  2493, 13, 407, 286, 500, 380, 519, 341, 307, 484, 295, 2524, 295, 28041, 13, 400,
  286, 914, 11, 51028], "temperature": 0.0, "avg_logprob": -0.14056586344307714, "compression_ratio":
  1.6791666666666667, "no_speech_prob": 0.01326596550643444}, {"id": 211, "seek":
  123768, "start": 1250.96, "end": 1254.8, "text": " there are other things that are
  out of reach, like, and this is where you saw the gap with MITI,", "tokens": [51028,
  456, 366, 661, 721, 300, 366, 484, 295, 2524, 11, 411, 11, 293, 341, 307, 689, 291,
  1866, 264, 7417, 365, 13100, 40, 11, 51220], "temperature": 0.0, "avg_logprob":
  -0.14056586344307714, "compression_ratio": 1.6791666666666667, "no_speech_prob":
  0.01326596550643444}, {"id": 212, "seek": 123768, "start": 1254.8, "end": 1263.8400000000001,
  "text": " I want to get closer to the MITI now. So there is, you know, every time
  I install a vector database,", "tokens": [51220, 286, 528, 281, 483, 4966, 281,
  264, 13100, 40, 586, 13, 407, 456, 307, 11, 291, 458, 11, 633, 565, 286, 3625, 257,
  8062, 8149, 11, 51672], "temperature": 0.0, "avg_logprob": -0.14056586344307714,
  "compression_ratio": 1.6791666666666667, "no_speech_prob": 0.01326596550643444},
  {"id": 213, "seek": 126384, "start": 1263.84, "end": 1270.3999999999999, "text":
  " I''m not going to name one. And it says, hey, you know, it will be faster if you
  use GPUs. And I''m like,", "tokens": [50364, 286, 478, 406, 516, 281, 1315, 472,
  13, 400, 309, 1619, 11, 4177, 11, 291, 458, 11, 309, 486, 312, 4663, 498, 291, 764,
  18407, 82, 13, 400, 286, 478, 411, 11, 50692], "temperature": 0.0, "avg_logprob":
  -0.17104445370760832, "compression_ratio": 1.6574074074074074, "no_speech_prob":
  0.004702328238636255}, {"id": 214, "seek": 126384, "start": 1270.3999999999999,
  "end": 1277.28, "text": " okay, I''m a startup. I don''t have GPUs. You know, so
  this is, I think one of the gaps that you saw", "tokens": [50692, 1392, 11, 286,
  478, 257, 18578, 13, 286, 500, 380, 362, 18407, 82, 13, 509, 458, 11, 370, 341,
  307, 11, 286, 519, 472, 295, 264, 15031, 300, 291, 1866, 51036], "temperature":
  0.0, "avg_logprob": -0.17104445370760832, "compression_ratio": 1.6574074074074074,
  "no_speech_prob": 0.004702328238636255}, {"id": 215, "seek": 126384, "start": 1277.28,
  "end": 1282.8799999999999, "text": " with MITI, but are there other gaps that you
  saw that you are addressing with MITI server?", "tokens": [51036, 365, 13100, 40,
  11, 457, 366, 456, 661, 15031, 300, 291, 1866, 300, 291, 366, 14329, 365, 13100,
  40, 7154, 30, 51316], "temperature": 0.0, "avg_logprob": -0.17104445370760832, "compression_ratio":
  1.6574074074074074, "no_speech_prob": 0.004702328238636255}, {"id": 216, "seek":
  126384, "start": 1285.4399999999998, "end": 1292.32, "text": " Yes, so the NLP world
  right now, and the vector world right now,", "tokens": [51444, 1079, 11, 370, 264,
  426, 45196, 1002, 558, 586, 11, 293, 264, 8062, 1002, 558, 586, 11, 51788], "temperature":
  0.0, "avg_logprob": -0.17104445370760832, "compression_ratio": 1.6574074074074074,
  "no_speech_prob": 0.004702328238636255}, {"id": 217, "seek": 129232, "start": 1292.96,
  "end": 1296.96, "text": " they all they talk about is Python, Python, Python, Python,
  everything is in Python.", "tokens": [50396, 436, 439, 436, 751, 466, 307, 15329,
  11, 15329, 11, 15329, 11, 15329, 11, 1203, 307, 294, 15329, 13, 50596], "temperature":
  0.0, "avg_logprob": -0.23446333926656973, "compression_ratio": 1.6682926829268292,
  "no_speech_prob": 0.0007650977931916714}, {"id": 218, "seek": 129232, "start": 1297.9199999999998,
  "end": 1300.8799999999999, "text": " When you get to production, you use something
  else, but it''s Python, Python, Python.", "tokens": [50644, 1133, 291, 483, 281,
  4265, 11, 291, 764, 746, 1646, 11, 457, 309, 311, 15329, 11, 15329, 11, 15329, 13,
  50792], "temperature": 0.0, "avg_logprob": -0.23446333926656973, "compression_ratio":
  1.6682926829268292, "no_speech_prob": 0.0007650977931916714}, {"id": 219, "seek":
  129232, "start": 1304.3999999999999, "end": 1312.24, "text": " So I wanted to, I
  came from a non-Python background. I started with C,", "tokens": [50968, 407, 286,
  1415, 281, 11, 286, 1361, 490, 257, 2107, 12, 47, 88, 11943, 3678, 13, 286, 1409,
  365, 383, 11, 51360], "temperature": 0.0, "avg_logprob": -0.23446333926656973, "compression_ratio":
  1.6682926829268292, "no_speech_prob": 0.0007650977931916714}, {"id": 220, "seek":
  129232, "start": 1313.36, "end": 1320.24, "text": " Pascal when I was really young
  and then my seed programming is terrible, I''m sure. Then I discovered,", "tokens":
  [51416, 41723, 562, 286, 390, 534, 2037, 293, 550, 452, 8871, 9410, 307, 6237, 11,
  286, 478, 988, 13, 1396, 286, 6941, 11, 51760], "temperature": 0.0, "avg_logprob":
  -0.23446333926656973, "compression_ratio": 1.6682926829268292, "no_speech_prob":
  0.0007650977931916714}, {"id": 221, "seek": 132024, "start": 1320.24, "end": 1325.68,
  "text": " you know, intermediate, intermediately compiled languages, Java, C sharp,
  things like that.", "tokens": [50364, 291, 458, 11, 19376, 11, 19376, 356, 36548,
  8650, 11, 10745, 11, 383, 8199, 11, 721, 411, 300, 13, 50636], "temperature": 0.0,
  "avg_logprob": -0.1762496381998062, "compression_ratio": 1.7946768060836502, "no_speech_prob":
  0.002240551169961691}, {"id": 222, "seek": 132024, "start": 1325.68, "end": 1330.88,
  "text": " And that was like early 2000s for me. And I kind of went, I was in the
  Microsoft world,", "tokens": [50636, 400, 300, 390, 411, 2440, 8132, 82, 337, 385,
  13, 400, 286, 733, 295, 1437, 11, 286, 390, 294, 264, 8116, 1002, 11, 50896], "temperature":
  0.0, "avg_logprob": -0.1762496381998062, "compression_ratio": 1.7946768060836502,
  "no_speech_prob": 0.002240551169961691}, {"id": 223, "seek": 132024, "start": 1330.88,
  "end": 1336.48, "text": " so I was doing C sharp for a while. And then I found,
  and all the while I''ve been doing Java script", "tokens": [50896, 370, 286, 390,
  884, 383, 8199, 337, 257, 1339, 13, 400, 550, 286, 1352, 11, 293, 439, 264, 1339,
  286, 600, 668, 884, 10745, 5755, 51176], "temperature": 0.0, "avg_logprob": -0.1762496381998062,
  "compression_ratio": 1.7946768060836502, "no_speech_prob": 0.002240551169961691},
  {"id": 224, "seek": 132024, "start": 1336.48, "end": 1343.92, "text": " because
  of, you know, I was involved in the web, so in the mid 90s, and that''s how I got
  involved", "tokens": [51176, 570, 295, 11, 291, 458, 11, 286, 390, 3288, 294, 264,
  3670, 11, 370, 294, 264, 2062, 4289, 82, 11, 293, 300, 311, 577, 286, 658, 3288,
  51548], "temperature": 0.0, "avg_logprob": -0.1762496381998062, "compression_ratio":
  1.7946768060836502, "no_speech_prob": 0.002240551169961691}, {"id": 225, "seek":
  132024, "start": 1343.92, "end": 1348.56, "text": " with content and content data
  and all this stuff. It''s just all web stuff. And then you got to", "tokens": [51548,
  365, 2701, 293, 2701, 1412, 293, 439, 341, 1507, 13, 467, 311, 445, 439, 3670, 1507,
  13, 400, 550, 291, 658, 281, 51780], "temperature": 0.0, "avg_logprob": -0.1762496381998062,
  "compression_ratio": 1.7946768060836502, "no_speech_prob": 0.002240551169961691},
  {"id": 226, "seek": 134856, "start": 1348.56, "end": 1353.52, "text": " know JavaScript
  if you do anything with the web. So it was like C sharp and JavaScript for me for
  a while.", "tokens": [50364, 458, 15778, 498, 291, 360, 1340, 365, 264, 3670, 13,
  407, 309, 390, 411, 383, 8199, 293, 15778, 337, 385, 337, 257, 1339, 13, 50612],
  "temperature": 0.0, "avg_logprob": -0.23894014444437112, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0007655072840861976}, {"id": 227, "seek": 134856, "start": 1355.12,
  "end": 1360.72, "text": " So I know that there''s a gap. If you go and if you go
  and you go into the JavaScript world,", "tokens": [50692, 407, 286, 458, 300, 456,
  311, 257, 7417, 13, 759, 291, 352, 293, 498, 291, 352, 293, 291, 352, 666, 264,
  15778, 1002, 11, 50972], "temperature": 0.0, "avg_logprob": -0.23894014444437112,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0007655072840861976},
  {"id": 228, "seek": 134856, "start": 1360.72, "end": 1369.9199999999998, "text":
  " the node, or, you know, TypeScript or those things, Dino now, there''s nothing.
  You want to do NLP?", "tokens": [50972, 264, 9984, 11, 420, 11, 291, 458, 11, 15576,
  14237, 420, 729, 721, 11, 413, 2982, 586, 11, 456, 311, 1825, 13, 509, 528, 281,
  360, 426, 45196, 30, 51432], "temperature": 0.0, "avg_logprob": -0.23894014444437112,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0007655072840861976},
  {"id": 229, "seek": 134856, "start": 1369.9199999999998, "end": 1376.96, "text":
  " Learn Python. That''s pretty much the suggestion. Same with C sharp, you know.
  Okay, well, there''s", "tokens": [51432, 17216, 15329, 13, 663, 311, 1238, 709,
  264, 16541, 13, 10635, 365, 383, 8199, 11, 291, 458, 13, 1033, 11, 731, 11, 456,
  311, 51784], "temperature": 0.0, "avg_logprob": -0.23894014444437112, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.0007655072840861976}, {"id": 230, "seek":
  137696, "start": 1376.96, "end": 1382.0, "text": " there''s some libraries out there,
  but they''re clunky. Nobody really, you know, Microsoft probably", "tokens": [50364,
  456, 311, 512, 15148, 484, 456, 11, 457, 436, 434, 596, 25837, 13, 9297, 534, 11,
  291, 458, 11, 8116, 1391, 50616], "temperature": 0.0, "avg_logprob": -0.21946386992931366,
  "compression_ratio": 1.7201365187713311, "no_speech_prob": 0.000817342079244554},
  {"id": 231, "seek": 137696, "start": 1382.0, "end": 1386.56, "text": " uses them,
  right? Because they''re Microsoft and they built C sharp and everybody''s doing
  Microsoft stuff.", "tokens": [50616, 4960, 552, 11, 558, 30, 1436, 436, 434, 8116,
  293, 436, 3094, 383, 8199, 293, 2201, 311, 884, 8116, 1507, 13, 50844], "temperature":
  0.0, "avg_logprob": -0.21946386992931366, "compression_ratio": 1.7201365187713311,
  "no_speech_prob": 0.000817342079244554}, {"id": 232, "seek": 137696, "start": 1386.56,
  "end": 1391.8400000000001, "text": " But, you know, outside of outside of Microsoft,
  like who''s using C sharp for for natural language", "tokens": [50844, 583, 11,
  291, 458, 11, 2380, 295, 2380, 295, 8116, 11, 411, 567, 311, 1228, 383, 8199, 337,
  337, 3303, 2856, 51108], "temperature": 0.0, "avg_logprob": -0.21946386992931366,
  "compression_ratio": 1.7201365187713311, "no_speech_prob": 0.000817342079244554},
  {"id": 233, "seek": 137696, "start": 1391.8400000000001, "end": 1399.44, "text":
  " process to train models? No, but, and to host models, you know, okay, well, to
  do it, you have to", "tokens": [51108, 1399, 281, 3847, 5245, 30, 883, 11, 457,
  11, 293, 281, 3975, 5245, 11, 291, 458, 11, 1392, 11, 731, 11, 281, 360, 309, 11,
  291, 362, 281, 51488], "temperature": 0.0, "avg_logprob": -0.21946386992931366,
  "compression_ratio": 1.7201365187713311, "no_speech_prob": 0.000817342079244554},
  {"id": 234, "seek": 137696, "start": 1399.44, "end": 1405.04, "text": " jump through
  all these hoops. And it''s really hard. So unless you want to like put Python in
  your stack,", "tokens": [51488, 3012, 807, 439, 613, 1106, 3370, 13, 400, 309, 311,
  534, 1152, 13, 407, 5969, 291, 528, 281, 411, 829, 15329, 294, 428, 8630, 11, 51768],
  "temperature": 0.0, "avg_logprob": -0.21946386992931366, "compression_ratio": 1.7201365187713311,
  "no_speech_prob": 0.000817342079244554}, {"id": 235, "seek": 140504, "start": 1405.84,
  "end": 1413.76, "text": " which is basically a non-starter for a lot of teams. A
  lot of teams, they work in languages like", "tokens": [50404, 597, 307, 1936, 257,
  2107, 12, 33969, 337, 257, 688, 295, 5491, 13, 316, 688, 295, 5491, 11, 436, 589,
  294, 8650, 411, 50800], "temperature": 0.0, "avg_logprob": -0.1466675176248922,
  "compression_ratio": 1.462686567164179, "no_speech_prob": 0.0013073710724711418},
  {"id": 236, "seek": 140504, "start": 1413.76, "end": 1423.2, "text": " node, JavaScript,
  C sharp, Java, Ruby, Go. Like there''s so many huge languages out there that just",
  "tokens": [50800, 9984, 11, 15778, 11, 383, 8199, 11, 10745, 11, 19907, 11, 1037,
  13, 1743, 456, 311, 370, 867, 2603, 8650, 484, 456, 300, 445, 51272], "temperature":
  0.0, "avg_logprob": -0.1466675176248922, "compression_ratio": 1.462686567164179,
  "no_speech_prob": 0.0013073710724711418}, {"id": 237, "seek": 140504, "start": 1423.2,
  "end": 1429.36, "text": " can''t touch these models. So I wanted something that
  kind of broke out of this shell, this Python,", "tokens": [51272, 393, 380, 2557,
  613, 5245, 13, 407, 286, 1415, 746, 300, 733, 295, 6902, 484, 295, 341, 8720, 11,
  341, 15329, 11, 51580], "temperature": 0.0, "avg_logprob": -0.1466675176248922,
  "compression_ratio": 1.462686567164179, "no_speech_prob": 0.0013073710724711418},
  {"id": 238, "seek": 142936, "start": 1430.0, "end": 1435.84, "text": " this Python
  like enclosure of like how do you get this stuff into the hands of other people",
  "tokens": [50396, 341, 15329, 411, 34093, 295, 411, 577, 360, 291, 483, 341, 1507,
  666, 264, 2377, 295, 661, 561, 50688], "temperature": 0.0, "avg_logprob": -0.2190812753171337,
  "compression_ratio": 1.7162162162162162, "no_speech_prob": 0.001832067035138607},
  {"id": 239, "seek": 142936, "start": 1435.84, "end": 1441.36, "text": " just want
  to build web applications. They don''t want to go and, you know, go into the Python
  family.", "tokens": [50688, 445, 528, 281, 1322, 3670, 5821, 13, 814, 500, 380,
  528, 281, 352, 293, 11, 291, 458, 11, 352, 666, 264, 15329, 1605, 13, 50964], "temperature":
  0.0, "avg_logprob": -0.2190812753171337, "compression_ratio": 1.7162162162162162,
  "no_speech_prob": 0.001832067035138607}, {"id": 240, "seek": 142936, "start": 1442.7199999999998,
  "end": 1449.28, "text": " So that was that was one of the one of the starting catalysts
  from from Mighty InfraServer.", "tokens": [51032, 407, 300, 390, 300, 390, 472,
  295, 264, 472, 295, 264, 2891, 23868, 82, 490, 490, 45874, 11537, 424, 31859, 331,
  13, 51360], "temperature": 0.0, "avg_logprob": -0.2190812753171337, "compression_ratio":
  1.7162162162162162, "no_speech_prob": 0.001832067035138607}, {"id": 241, "seek":
  142936, "start": 1451.6799999999998, "end": 1458.1599999999999, "text": " I, I there
  are there is one tool that I have to use that is Python because it has to you have
  to", "tokens": [51480, 286, 11, 286, 456, 366, 456, 307, 472, 2290, 300, 286, 362,
  281, 764, 300, 307, 15329, 570, 309, 575, 281, 291, 362, 281, 51804], "temperature":
  0.0, "avg_logprob": -0.2190812753171337, "compression_ratio": 1.7162162162162162,
  "no_speech_prob": 0.001832067035138607}, {"id": 242, "seek": 145816, "start": 1458.16,
  "end": 1463.2, "text": " convert a model and I convert the model to Onyx, which
  is most people know about Onyx if you''re in", "tokens": [50364, 7620, 257, 2316,
  293, 286, 7620, 264, 2316, 281, 1282, 88, 87, 11, 597, 307, 881, 561, 458, 466,
  1282, 88, 87, 498, 291, 434, 294, 50616], "temperature": 0.0, "avg_logprob": -0.22187744568441517,
  "compression_ratio": 1.5879828326180256, "no_speech_prob": 0.0003088583762291819},
  {"id": 243, "seek": 145816, "start": 1463.2, "end": 1469.44, "text": " the NLP world
  by now, which is it''s ONNX, that''s for an open neural network exchange. And",
  "tokens": [50616, 264, 426, 45196, 1002, 538, 586, 11, 597, 307, 309, 311, 422,
  45, 45, 55, 11, 300, 311, 337, 364, 1269, 18161, 3209, 7742, 13, 400, 50928], "temperature":
  0.0, "avg_logprob": -0.22187744568441517, "compression_ratio": 1.5879828326180256,
  "no_speech_prob": 0.0003088583762291819}, {"id": 244, "seek": 145816, "start": 1470.16,
  "end": 1476.96, "text": " is this intermediary format that can be used generically.
  It''s like an open model format.", "tokens": [50964, 307, 341, 15184, 822, 7877,
  300, 393, 312, 1143, 1337, 984, 13, 467, 311, 411, 364, 1269, 2316, 7877, 13, 51304],
  "temperature": 0.0, "avg_logprob": -0.22187744568441517, "compression_ratio": 1.5879828326180256,
  "no_speech_prob": 0.0003088583762291819}, {"id": 245, "seek": 145816, "start": 1478.3200000000002,
  "end": 1484.0, "text": " Now there are runtimes that you can take Onyx and Onyx
  models and run them. So the biggest,", "tokens": [51372, 823, 456, 366, 49435, 1532,
  300, 291, 393, 747, 1282, 88, 87, 293, 1282, 88, 87, 5245, 293, 1190, 552, 13, 407,
  264, 3880, 11, 51656], "temperature": 0.0, "avg_logprob": -0.22187744568441517,
  "compression_ratio": 1.5879828326180256, "no_speech_prob": 0.0003088583762291819},
  {"id": 246, "seek": 148400, "start": 1484.96, "end": 1490.72, "text": " the biggest
  one is Onyx runtime and that''s developed by Microsoft, it''s open source. I see
  licensed", "tokens": [50412, 264, 3880, 472, 307, 1282, 88, 87, 34474, 293, 300,
  311, 4743, 538, 8116, 11, 309, 311, 1269, 4009, 13, 286, 536, 25225, 50700], "temperature":
  0.0, "avg_logprob": -0.1664989249220172, "compression_ratio": 1.6569037656903767,
  "no_speech_prob": 0.0006226053810678422}, {"id": 247, "seek": 148400, "start": 1491.6,
  "end": 1499.2, "text": " and that''s written in C++. But there are bindings for
  other languages and community contributes", "tokens": [50744, 293, 300, 311, 3720,
  294, 383, 25472, 13, 583, 456, 366, 14786, 1109, 337, 661, 8650, 293, 1768, 32035,
  51124], "temperature": 0.0, "avg_logprob": -0.1664989249220172, "compression_ratio":
  1.6569037656903767, "no_speech_prob": 0.0006226053810678422}, {"id": 248, "seek":
  148400, "start": 1499.2, "end": 1504.96, "text": " bindings. So you can use Onyx
  runtime in Python if you want to. You can, and you''ll get like for those", "tokens":
  [51124, 14786, 1109, 13, 407, 291, 393, 764, 1282, 88, 87, 34474, 294, 15329, 498,
  291, 528, 281, 13, 509, 393, 11, 293, 291, 603, 483, 411, 337, 729, 51412], "temperature":
  0.0, "avg_logprob": -0.1664989249220172, "compression_ratio": 1.6569037656903767,
  "no_speech_prob": 0.0006226053810678422}, {"id": 249, "seek": 148400, "start": 1504.96,
  "end": 1510.64, "text": " Python people who want to host models in Python, just
  convert your model to Onyx and host it in a", "tokens": [51412, 15329, 561, 567,
  528, 281, 3975, 5245, 294, 15329, 11, 445, 7620, 428, 2316, 281, 1282, 88, 87, 293,
  3975, 309, 294, 257, 51696], "temperature": 0.0, "avg_logprob": -0.1664989249220172,
  "compression_ratio": 1.6569037656903767, "no_speech_prob": 0.0006226053810678422},
  {"id": 250, "seek": 151064, "start": 1510.64, "end": 1515.2800000000002, "text":
  " Python Onyx runtime. It''ll double the speed of the model inference, like out
  of the box. You don''t", "tokens": [50364, 15329, 1282, 88, 87, 34474, 13, 467,
  603, 3834, 264, 3073, 295, 264, 2316, 38253, 11, 411, 484, 295, 264, 2424, 13, 509,
  500, 380, 50596], "temperature": 0.0, "avg_logprob": -0.21714177861943976, "compression_ratio":
  1.75, "no_speech_prob": 0.0002043155545834452}, {"id": 251, "seek": 151064, "start":
  1515.2800000000002, "end": 1519.1200000000001, "text": " have to do anything. You
  press like a button. You don''t, you clone the repo, you press a button,", "tokens":
  [50596, 362, 281, 360, 1340, 13, 509, 1886, 411, 257, 2960, 13, 509, 500, 380, 11,
  291, 26506, 264, 49040, 11, 291, 1886, 257, 2960, 11, 50788], "temperature": 0.0,
  "avg_logprob": -0.21714177861943976, "compression_ratio": 1.75, "no_speech_prob":
  0.0002043155545834452}, {"id": 252, "seek": 151064, "start": 1519.1200000000001,
  "end": 1527.1200000000001, "text": " then twice, twice as fast. But for others,
  you know, there''s binding for C sharp, there''s bindings for", "tokens": [50788,
  550, 6091, 11, 6091, 382, 2370, 13, 583, 337, 2357, 11, 291, 458, 11, 456, 311,
  17359, 337, 383, 8199, 11, 456, 311, 14786, 1109, 337, 51188], "temperature": 0.0,
  "avg_logprob": -0.21714177861943976, "compression_ratio": 1.75, "no_speech_prob":
  0.0002043155545834452}, {"id": 253, "seek": 151064, "start": 1527.1200000000001,
  "end": 1534.96, "text": " Java, there''s, there might be bindings for Ruby. I haven''t
  looked probably bindings for go. And even", "tokens": [51188, 10745, 11, 456, 311,
  11, 456, 1062, 312, 14786, 1109, 337, 19907, 13, 286, 2378, 380, 2956, 1391, 14786,
  1109, 337, 352, 13, 400, 754, 51580], "temperature": 0.0, "avg_logprob": -0.21714177861943976,
  "compression_ratio": 1.75, "no_speech_prob": 0.0002043155545834452}, {"id": 254,
  "seek": 153496, "start": 1534.96, "end": 1543.6000000000001, "text": " if Microsoft
  doesn''t support them, the community builds them. So you can do this, but there''s
  this", "tokens": [50364, 498, 8116, 1177, 380, 1406, 552, 11, 264, 1768, 15182,
  552, 13, 407, 291, 393, 360, 341, 11, 457, 456, 311, 341, 50796], "temperature":
  0.0, "avg_logprob": -0.1317237115675403, "compression_ratio": 1.8157894736842106,
  "no_speech_prob": 0.0016603866824880242}, {"id": 255, "seek": 153496, "start": 1543.6000000000001,
  "end": 1548.96, "text": " other problem that you have. The other problem is that,
  well, those are just the model weights.", "tokens": [50796, 661, 1154, 300, 291,
  362, 13, 440, 661, 1154, 307, 300, 11, 731, 11, 729, 366, 445, 264, 2316, 17443,
  13, 51064], "temperature": 0.0, "avg_logprob": -0.1317237115675403, "compression_ratio":
  1.8157894736842106, "no_speech_prob": 0.0016603866824880242}, {"id": 256, "seek":
  153496, "start": 1548.96, "end": 1553.2, "text": " And if you''re talking about,
  and hosting the runtime for the model weights, so you put in inputs", "tokens":
  [51064, 400, 498, 291, 434, 1417, 466, 11, 293, 16058, 264, 34474, 337, 264, 2316,
  17443, 11, 370, 291, 829, 294, 15743, 51276], "temperature": 0.0, "avg_logprob":
  -0.1317237115675403, "compression_ratio": 1.8157894736842106, "no_speech_prob":
  0.0016603866824880242}, {"id": 257, "seek": 153496, "start": 1553.2, "end": 1558.72,
  "text": " and you get outputs. But where do you get the inputs from? Well, you have
  to tokenize text,", "tokens": [51276, 293, 291, 483, 23930, 13, 583, 689, 360, 291,
  483, 264, 15743, 490, 30, 1042, 11, 291, 362, 281, 14862, 1125, 2487, 11, 51552],
  "temperature": 0.0, "avg_logprob": -0.1317237115675403, "compression_ratio": 1.8157894736842106,
  "no_speech_prob": 0.0016603866824880242}, {"id": 258, "seek": 153496, "start": 1559.3600000000001,
  "end": 1564.32, "text": " you have to do all the stuff to prepare it to pre-process
  it. And then when you tokenize and you do", "tokens": [51584, 291, 362, 281, 360,
  439, 264, 1507, 281, 5940, 309, 281, 659, 12, 41075, 309, 13, 400, 550, 562, 291,
  14862, 1125, 293, 291, 360, 51832], "temperature": 0.0, "avg_logprob": -0.1317237115675403,
  "compression_ratio": 1.8157894736842106, "no_speech_prob": 0.0016603866824880242},
  {"id": 259, "seek": 156432, "start": 1564.32, "end": 1574.08, "text": " pre-processing,
  then you can pass in those, the tokenized data as inputs. But all the tokenizers",
  "tokens": [50364, 659, 12, 41075, 278, 11, 550, 291, 393, 1320, 294, 729, 11, 264,
  14862, 1602, 1412, 382, 15743, 13, 583, 439, 264, 14862, 22525, 50852], "temperature":
  0.0, "avg_logprob": -0.17863023281097412, "compression_ratio": 1.7339449541284404,
  "no_speech_prob": 0.00027670248528011143}, {"id": 260, "seek": 156432, "start":
  1574.08, "end": 1581.52, "text": " are written in Python. So now you have to, now
  you have that problem. So I actually used Rust", "tokens": [50852, 366, 3720, 294,
  15329, 13, 407, 586, 291, 362, 281, 11, 586, 291, 362, 300, 1154, 13, 407, 286,
  767, 1143, 34952, 51224], "temperature": 0.0, "avg_logprob": -0.17863023281097412,
  "compression_ratio": 1.7339449541284404, "no_speech_prob": 0.00027670248528011143},
  {"id": 261, "seek": 156432, "start": 1581.52, "end": 1588.08, "text": " for mighty
  inference server because hugging face based their tokenizer, their fast tokenizers",
  "tokens": [51224, 337, 21556, 38253, 7154, 570, 41706, 1851, 2361, 641, 14862, 6545,
  11, 641, 2370, 14862, 22525, 51552], "temperature": 0.0, "avg_logprob": -0.17863023281097412,
  "compression_ratio": 1.7339449541284404, "no_speech_prob": 0.00027670248528011143},
  {"id": 262, "seek": 156432, "start": 1588.08, "end": 1591.76, "text": " on Rust,
  they wrote it in Rust, and they offer bindings for Python. So if you, if you install",
  "tokens": [51552, 322, 34952, 11, 436, 4114, 309, 294, 34952, 11, 293, 436, 2626,
  14786, 1109, 337, 15329, 13, 407, 498, 291, 11, 498, 291, 3625, 51736], "temperature":
  0.0, "avg_logprob": -0.17863023281097412, "compression_ratio": 1.7339449541284404,
  "no_speech_prob": 0.00027670248528011143}, {"id": 263, "seek": 159176, "start":
  1591.76, "end": 1598.48, "text": " a fast tokenizer in Python, you''re actually
  using Rust bindings for that. So I wrote a web server", "tokens": [50364, 257, 2370,
  14862, 6545, 294, 15329, 11, 291, 434, 767, 1228, 34952, 14786, 1109, 337, 300,
  13, 407, 286, 4114, 257, 3670, 7154, 50700], "temperature": 0.0, "avg_logprob":
  -0.21274781227111816, "compression_ratio": 1.6260504201680672, "no_speech_prob":
  0.00030918169068172574}, {"id": 264, "seek": 159176, "start": 1598.48, "end": 1606.96,
  "text": " that wraps the Rust tokenizers and on X Run time. And I wrote a whole
  bunch of code for pipeline", "tokens": [50700, 300, 25831, 264, 34952, 14862, 22525,
  293, 322, 1783, 8950, 565, 13, 400, 286, 4114, 257, 1379, 3840, 295, 3089, 337,
  15517, 51124], "temperature": 0.0, "avg_logprob": -0.21274781227111816, "compression_ratio":
  1.6260504201680672, "no_speech_prob": 0.00030918169068172574}, {"id": 265, "seek":
  159176, "start": 1606.96, "end": 1613.36, "text": " specific stuff like question
  answering, sentence transformers, sequence classification, which is", "tokens":
  [51124, 2685, 1507, 411, 1168, 13430, 11, 8174, 4088, 433, 11, 8310, 21538, 11,
  597, 307, 51444], "temperature": 0.0, "avg_logprob": -0.21274781227111816, "compression_ratio":
  1.6260504201680672, "no_speech_prob": 0.00030918169068172574}, {"id": 266, "seek":
  159176, "start": 1613.36, "end": 1621.2, "text": " like sentiment analysis token
  classifications. That''s like, entity recognition. And I''m working", "tokens":
  [51444, 411, 16149, 5215, 14862, 1508, 7833, 13, 663, 311, 411, 11, 13977, 11150,
  13, 400, 286, 478, 1364, 51836], "temperature": 0.0, "avg_logprob": -0.21274781227111816,
  "compression_ratio": 1.6260504201680672, "no_speech_prob": 0.00030918169068172574},
  {"id": 267, "seek": 162120, "start": 1621.3600000000001, "end": 1628.8, "text":
  " on others also, but it''s so much faster, it''s so much faster than Python, like
  it''s not even close.", "tokens": [50372, 322, 2357, 611, 11, 457, 309, 311, 370,
  709, 4663, 11, 309, 311, 370, 709, 4663, 813, 15329, 11, 411, 309, 311, 406, 754,
  1998, 13, 50744], "temperature": 0.0, "avg_logprob": -0.13338863736107237, "compression_ratio":
  1.6609442060085837, "no_speech_prob": 0.0020275639835745096}, {"id": 268, "seek":
  162120, "start": 1631.2, "end": 1636.72, "text": " It''s probably like three or
  four times as fast without any fine tuning of it. And I''ve gone", "tokens": [50864,
  467, 311, 1391, 411, 1045, 420, 1451, 1413, 382, 2370, 1553, 604, 2489, 15164, 295,
  309, 13, 400, 286, 600, 2780, 51140], "temperature": 0.0, "avg_logprob": -0.13338863736107237,
  "compression_ratio": 1.6609442060085837, "no_speech_prob": 0.0020275639835745096},
  {"id": 269, "seek": 162120, "start": 1636.72, "end": 1642.56, "text": " through
  fine tuning. So I haven''t compared it to Python in a long time, but I might be
  like five", "tokens": [51140, 807, 2489, 15164, 13, 407, 286, 2378, 380, 5347, 309,
  281, 15329, 294, 257, 938, 565, 11, 457, 286, 1062, 312, 411, 1732, 51432], "temperature":
  0.0, "avg_logprob": -0.13338863736107237, "compression_ratio": 1.6609442060085837,
  "no_speech_prob": 0.0020275639835745096}, {"id": 270, "seek": 162120, "start": 1642.56,
  "end": 1650.16, "text": " times as fast as Python right now on CPU. You can also
  use GPU if you want. And it''s, you maintain", "tokens": [51432, 1413, 382, 2370,
  382, 15329, 558, 586, 322, 13199, 13, 509, 393, 611, 764, 18407, 498, 291, 528,
  13, 400, 309, 311, 11, 291, 6909, 51812], "temperature": 0.0, "avg_logprob": -0.13338863736107237,
  "compression_ratio": 1.6609442060085837, "no_speech_prob": 0.0020275639835745096},
  {"id": 271, "seek": 165016, "start": 1650.16, "end": 1658.72, "text": " the same,
  the same speed. It''s just as fast. Yeah. Well, it''s just as fast as the, the ratio
  of speed is", "tokens": [50364, 264, 912, 11, 264, 912, 3073, 13, 467, 311, 445,
  382, 2370, 13, 865, 13, 1042, 11, 309, 311, 445, 382, 2370, 382, 264, 11, 264, 8509,
  295, 3073, 307, 50792], "temperature": 0.0, "avg_logprob": -0.16960127848499226,
  "compression_ratio": 1.736842105263158, "no_speech_prob": 0.002098849043250084},
  {"id": 272, "seek": 165016, "start": 1658.72, "end": 1664.0, "text": " like the,
  you know, if you took the model and Python and you put it in a GPU versus you take
  the model", "tokens": [50792, 411, 264, 11, 291, 458, 11, 498, 291, 1890, 264, 2316,
  293, 15329, 293, 291, 829, 309, 294, 257, 18407, 5717, 291, 747, 264, 2316, 51056],
  "temperature": 0.0, "avg_logprob": -0.16960127848499226, "compression_ratio": 1.736842105263158,
  "no_speech_prob": 0.002098849043250084}, {"id": 273, "seek": 165016, "start": 1664.0,
  "end": 1669.2, "text": " and on X Run time, you put it in the GPU, you get it''s
  far faster.", "tokens": [51056, 293, 322, 1783, 8950, 565, 11, 291, 829, 309, 294,
  264, 18407, 11, 291, 483, 309, 311, 1400, 4663, 13, 51316], "temperature": 0.0,
  "avg_logprob": -0.16960127848499226, "compression_ratio": 1.736842105263158, "no_speech_prob":
  0.002098849043250084}, {"id": 274, "seek": 165016, "start": 1670.72, "end": 1675.28,
  "text": " And you say like when you said bindings in other languages, you know,
  like Java C sharp.", "tokens": [51392, 400, 291, 584, 411, 562, 291, 848, 14786,
  1109, 294, 661, 8650, 11, 291, 458, 11, 411, 10745, 383, 8199, 13, 51620], "temperature":
  0.0, "avg_logprob": -0.16960127848499226, "compression_ratio": 1.736842105263158,
  "no_speech_prob": 0.002098849043250084}, {"id": 275, "seek": 167528, "start": 1676.24,
  "end": 1683.28, "text": " So if my stack is in Java, I can take this model and kind
  of plug it in into my Java code.", "tokens": [50412, 407, 498, 452, 8630, 307, 294,
  10745, 11, 286, 393, 747, 341, 2316, 293, 733, 295, 5452, 309, 294, 666, 452, 10745,
  3089, 13, 50764], "temperature": 0.0, "avg_logprob": -0.18871515933598312, "compression_ratio":
  1.6926605504587156, "no_speech_prob": 0.014592043124139309}, {"id": 276, "seek":
  167528, "start": 1684.6399999999999, "end": 1689.84, "text": " You can take a, you
  can take a, let''s take a hugging face model, for example, like just", "tokens":
  [50832, 509, 393, 747, 257, 11, 291, 393, 747, 257, 11, 718, 311, 747, 257, 41706,
  1851, 2316, 11, 337, 1365, 11, 411, 445, 51092], "temperature": 0.0, "avg_logprob":
  -0.18871515933598312, "compression_ratio": 1.6926605504587156, "no_speech_prob":
  0.014592043124139309}, {"id": 277, "seek": 167528, "start": 1691.12, "end": 1695.76,
  "text": " let''s say brick based on case, you know, most people know that one. Brat
  based on case, you can", "tokens": [51156, 718, 311, 584, 16725, 2361, 322, 1389,
  11, 291, 458, 11, 881, 561, 458, 300, 472, 13, 1603, 267, 2361, 322, 1389, 11, 291,
  393, 51388], "temperature": 0.0, "avg_logprob": -0.18871515933598312, "compression_ratio":
  1.6926605504587156, "no_speech_prob": 0.014592043124139309}, {"id": 278, "seek":
  167528, "start": 1695.76, "end": 1700.3999999999999, "text": " export that to Onyx
  with hugging face code in Python. And you have now you have an Onyx model.", "tokens":
  [51388, 10725, 300, 281, 1282, 88, 87, 365, 41706, 1851, 3089, 294, 15329, 13, 400,
  291, 362, 586, 291, 362, 364, 1282, 88, 87, 2316, 13, 51620], "temperature": 0.0,
  "avg_logprob": -0.18871515933598312, "compression_ratio": 1.6926605504587156, "no_speech_prob":
  0.014592043124139309}, {"id": 279, "seek": 170040, "start": 1700.8000000000002,
  "end": 1712.3200000000002, "text": " Now you can, in Java, you can stand up a class
  that wraps the Onyx runtime and you, and you load", "tokens": [50384, 823, 291,
  393, 11, 294, 10745, 11, 291, 393, 1463, 493, 257, 1508, 300, 25831, 264, 1282,
  88, 87, 34474, 293, 291, 11, 293, 291, 3677, 50960], "temperature": 0.0, "avg_logprob":
  -0.1804190947946194, "compression_ratio": 1.8045454545454545, "no_speech_prob":
  0.0014941992703825235}, {"id": 280, "seek": 170040, "start": 1712.3200000000002,
  "end": 1718.5600000000002, "text": " the model into memory with on X run time in
  your class. And then you can create methods around that", "tokens": [50960, 264,
  2316, 666, 4675, 365, 322, 1783, 1190, 565, 294, 428, 1508, 13, 400, 550, 291, 393,
  1884, 7150, 926, 300, 51272], "temperature": 0.0, "avg_logprob": -0.1804190947946194,
  "compression_ratio": 1.8045454545454545, "no_speech_prob": 0.0014941992703825235},
  {"id": 281, "seek": 170040, "start": 1718.5600000000002, "end": 1724.0, "text":
  " class, right? And then you can call, you can call it and you can say, I''m going
  to pass in the inputs", "tokens": [51272, 1508, 11, 558, 30, 400, 550, 291, 393,
  818, 11, 291, 393, 818, 309, 293, 291, 393, 584, 11, 286, 478, 516, 281, 1320, 294,
  264, 15743, 51544], "temperature": 0.0, "avg_logprob": -0.1804190947946194, "compression_ratio":
  1.8045454545454545, "no_speech_prob": 0.0014941992703825235}, {"id": 282, "seek":
  170040, "start": 1724.0, "end": 1728.8000000000002, "text": " and I''m going to
  get out. And that''s all in Java now. Well, with the C++ wrapper for Onyx runtime,",
  "tokens": [51544, 293, 286, 478, 516, 281, 483, 484, 13, 400, 300, 311, 439, 294,
  10745, 586, 13, 1042, 11, 365, 264, 383, 25472, 46906, 337, 1282, 88, 87, 34474,
  11, 51784], "temperature": 0.0, "avg_logprob": -0.1804190947946194, "compression_ratio":
  1.8045454545454545, "no_speech_prob": 0.0014941992703825235}, {"id": 283, "seek":
  172880, "start": 1728.8, "end": 1737.2, "text": " of course, but the connect, but
  to wrap that C++ runtime, there have to be bindings between the", "tokens": [50364,
  295, 1164, 11, 457, 264, 1745, 11, 457, 281, 7019, 300, 383, 25472, 34474, 11, 456,
  362, 281, 312, 14786, 1109, 1296, 264, 50784], "temperature": 0.0, "avg_logprob":
  -0.1769964055317204, "compression_ratio": 1.5828877005347595, "no_speech_prob":
  0.0011279038153588772}, {"id": 284, "seek": 172880, "start": 1737.2, "end": 1744.56,
  "text": " language. So Java has to have some application interface to talk to C++.
  Yeah, which is GNI, right?", "tokens": [50784, 2856, 13, 407, 10745, 575, 281, 362,
  512, 3861, 9226, 281, 751, 281, 383, 25472, 13, 865, 11, 597, 307, 460, 42496, 11,
  558, 30, 51152], "temperature": 0.0, "avg_logprob": -0.1769964055317204, "compression_ratio":
  1.5828877005347595, "no_speech_prob": 0.0011279038153588772}, {"id": 285, "seek":
  172880, "start": 1744.56, "end": 1753.36, "text": " Java native interface, I think.
  Yeah, I think so. Java. Yeah. So that part, like having Java talk to", "tokens":
  [51152, 10745, 8470, 9226, 11, 286, 519, 13, 865, 11, 286, 519, 370, 13, 10745,
  13, 865, 13, 407, 300, 644, 11, 411, 1419, 10745, 751, 281, 51592], "temperature":
  0.0, "avg_logprob": -0.1769964055317204, "compression_ratio": 1.5828877005347595,
  "no_speech_prob": 0.0011279038153588772}, {"id": 286, "seek": 175336, "start": 1753.4399999999998,
  "end": 1758.32, "text": " Onyx runtime is taken care of already. You still have
  to write all the other stuff around it,", "tokens": [50368, 1282, 88, 87, 34474,
  307, 2726, 1127, 295, 1217, 13, 509, 920, 362, 281, 2464, 439, 264, 661, 1507, 926,
  309, 11, 50612], "temperature": 0.0, "avg_logprob": -0.18286997133547123, "compression_ratio":
  1.6050420168067228, "no_speech_prob": 0.0015153585700318217}, {"id": 287, "seek":
  175336, "start": 1758.32, "end": 1763.1999999999998, "text": " like to you to leverage
  it. But that''s, you know, where programmers used to that sort of thing.", "tokens":
  [50612, 411, 281, 291, 281, 13982, 309, 13, 583, 300, 311, 11, 291, 458, 11, 689,
  41504, 1143, 281, 300, 1333, 295, 551, 13, 50856], "temperature": 0.0, "avg_logprob":
  -0.18286997133547123, "compression_ratio": 1.6050420168067228, "no_speech_prob":
  0.0015153585700318217}, {"id": 288, "seek": 175336, "start": 1763.1999999999998,
  "end": 1775.6799999999998, "text": " You know, Java, you can, you can do that. And
  I think, I don''t know if it''s, I don''t know how much", "tokens": [50856, 509,
  458, 11, 10745, 11, 291, 393, 11, 291, 393, 360, 300, 13, 400, 286, 519, 11, 286,
  500, 380, 458, 498, 309, 311, 11, 286, 500, 380, 458, 577, 709, 51480], "temperature":
  0.0, "avg_logprob": -0.18286997133547123, "compression_ratio": 1.6050420168067228,
  "no_speech_prob": 0.0015153585700318217}, {"id": 289, "seek": 175336, "start": 1775.6799999999998,
  "end": 1781.12, "text": " we''ve seen it, but Jeff Zemorek, who works at open source
  connections, I know that is like he", "tokens": [51480, 321, 600, 1612, 309, 11,
  457, 7506, 1176, 443, 418, 74, 11, 567, 1985, 412, 1269, 4009, 9271, 11, 286, 458,
  300, 307, 411, 415, 51752], "temperature": 0.0, "avg_logprob": -0.18286997133547123,
  "compression_ratio": 1.6050420168067228, "no_speech_prob": 0.0015153585700318217},
  {"id": 290, "seek": 178112, "start": 1781.12, "end": 1785.84, "text": " was working
  on a project where he, you know, he could try to load an Onyx runtime in open,",
  "tokens": [50364, 390, 1364, 322, 257, 1716, 689, 415, 11, 291, 458, 11, 415, 727,
  853, 281, 3677, 364, 1282, 88, 87, 34474, 294, 1269, 11, 50600], "temperature":
  0.0, "avg_logprob": -0.23622053703375623, "compression_ratio": 1.575, "no_speech_prob":
  0.001816479256376624}, {"id": 291, "seek": 178112, "start": 1785.84, "end": 1793.04,
  "text": " in open NLP, which is a Java program. So trying to get an Onyx model in
  open NLP. And I think he", "tokens": [50600, 294, 1269, 426, 45196, 11, 597, 307,
  257, 10745, 1461, 13, 407, 1382, 281, 483, 364, 1282, 88, 87, 2316, 294, 1269, 426,
  45196, 13, 400, 286, 519, 415, 50960], "temperature": 0.0, "avg_logprob": -0.23622053703375623,
  "compression_ratio": 1.575, "no_speech_prob": 0.001816479256376624}, {"id": 292,
  "seek": 178112, "start": 1793.04, "end": 1799.04, "text": " succeeded. I haven''t
  seen code for that. Yeah. Yeah. But that''s what I''m exactly. Yeah, that''s,",
  "tokens": [50960, 20263, 13, 286, 2378, 380, 1612, 3089, 337, 300, 13, 865, 13,
  865, 13, 583, 300, 311, 437, 286, 478, 2293, 13, 865, 11, 300, 311, 11, 51260],
  "temperature": 0.0, "avg_logprob": -0.23622053703375623, "compression_ratio": 1.575,
  "no_speech_prob": 0.001816479256376624}, {"id": 293, "seek": 178112, "start": 1799.04,
  "end": 1806.08, "text": " that''s awesome. So I mean, the reason I''m asking is
  because I witnessed this tectonic shift in", "tokens": [51260, 300, 311, 3476, 13,
  407, 286, 914, 11, 264, 1778, 286, 478, 3365, 307, 570, 286, 21519, 341, 535, 349,
  11630, 5513, 294, 51612], "temperature": 0.0, "avg_logprob": -0.23622053703375623,
  "compression_ratio": 1.575, "no_speech_prob": 0.001816479256376624}, {"id": 294,
  "seek": 180608, "start": 1806.24, "end": 1815.36, "text": " in my previous company
  where we had the entire stack in Java. Even though we started with Pearl,", "tokens":
  [50372, 294, 452, 3894, 2237, 689, 321, 632, 264, 2302, 8630, 294, 10745, 13, 2754,
  1673, 321, 1409, 365, 24639, 11, 50828], "temperature": 0.0, "avg_logprob": -0.22057157693449983,
  "compression_ratio": 1.5756302521008403, "no_speech_prob": 0.0024803695268929005},
  {"id": 295, "seek": 180608, "start": 1815.36, "end": 1823.4399999999998, "text":
  " but we had to read right everything into Java, just didn''t scale on Pearl. And,
  yeah, and I mean,", "tokens": [50828, 457, 321, 632, 281, 1401, 558, 1203, 666,
  10745, 11, 445, 994, 380, 4373, 322, 24639, 13, 400, 11, 1338, 11, 293, 286, 914,
  11, 51232], "temperature": 0.0, "avg_logprob": -0.22057157693449983, "compression_ratio":
  1.5756302521008403, "no_speech_prob": 0.0024803695268929005}, {"id": 296, "seek":
  180608, "start": 1823.4399999999998, "end": 1829.4399999999998, "text": " we had
  Apache Solar on one end as the open source search engine also written in Java. And,",
  "tokens": [51232, 321, 632, 46597, 22385, 322, 472, 917, 382, 264, 1269, 4009, 3164,
  2848, 611, 3720, 294, 10745, 13, 400, 11, 51532], "temperature": 0.0, "avg_logprob":
  -0.22057157693449983, "compression_ratio": 1.5756302521008403, "no_speech_prob":
  0.0024803695268929005}, {"id": 297, "seek": 180608, "start": 1829.4399999999998,
  "end": 1835.4399999999998, "text": " you know, when we would customize it, we would
  write plugins in Java and so on. But then,", "tokens": [51532, 291, 458, 11, 562,
  321, 576, 19734, 309, 11, 321, 576, 2464, 33759, 294, 10745, 293, 370, 322, 13,
  583, 550, 11, 51832], "temperature": 0.0, "avg_logprob": -0.22057157693449983, "compression_ratio":
  1.5756302521008403, "no_speech_prob": 0.0024803695268929005}, {"id": 298, "seek":
  183544, "start": 1835.76, "end": 1842.48, "text": " when we wanted to introduce
  AI into the pipeline, of course, everything was in Python. We hired", "tokens":
  [50380, 562, 321, 1415, 281, 5366, 7318, 666, 264, 15517, 11, 295, 1164, 11, 1203,
  390, 294, 15329, 13, 492, 13144, 50716], "temperature": 0.0, "avg_logprob": -0.12215498515537807,
  "compression_ratio": 1.6166666666666667, "no_speech_prob": 0.003057604655623436},
  {"id": 299, "seek": 183544, "start": 1842.48, "end": 1849.2, "text": " people who
  could only do Python, nothing else, fresh grads. And, and now you are stuck with
  this", "tokens": [50716, 561, 567, 727, 787, 360, 15329, 11, 1825, 1646, 11, 4451,
  677, 5834, 13, 400, 11, 293, 586, 291, 366, 5541, 365, 341, 51052], "temperature":
  0.0, "avg_logprob": -0.12215498515537807, "compression_ratio": 1.6166666666666667,
  "no_speech_prob": 0.003057604655623436}, {"id": 300, "seek": 183544, "start": 1849.2,
  "end": 1855.92, "text": " new architecture. Okay, you have Python as one step in
  the pipeline. How do you call it? How do", "tokens": [51052, 777, 9482, 13, 1033,
  11, 291, 362, 15329, 382, 472, 1823, 294, 264, 15517, 13, 1012, 360, 291, 818, 309,
  30, 1012, 360, 51388], "temperature": 0.0, "avg_logprob": -0.12215498515537807,
  "compression_ratio": 1.6166666666666667, "no_speech_prob": 0.003057604655623436},
  {"id": 301, "seek": 183544, "start": 1855.92, "end": 1861.8400000000001, "text":
  " you handle errors? How do you scale this thing? Right? And we were also moving
  to Kubernetes to add", "tokens": [51388, 291, 4813, 13603, 30, 1012, 360, 291, 4373,
  341, 551, 30, 1779, 30, 400, 321, 645, 611, 2684, 281, 23145, 281, 909, 51684],
  "temperature": 0.0, "avg_logprob": -0.12215498515537807, "compression_ratio": 1.6166666666666667,
  "no_speech_prob": 0.003057604655623436}, {"id": 302, "seek": 186184, "start": 1861.84,
  "end": 1871.4399999999998, "text": " to this crazy mix. And, and what we ended up
  doing is that we would have a synchronous processor,", "tokens": [50364, 281, 341,
  3219, 2890, 13, 400, 11, 293, 437, 321, 4590, 493, 884, 307, 300, 321, 576, 362,
  257, 44743, 15321, 11, 50844], "temperature": 0.0, "avg_logprob": -0.13527759240598095,
  "compression_ratio": 1.5378486055776892, "no_speech_prob": 0.004806575831025839},
  {"id": 303, "seek": 186184, "start": 1871.4399999999998, "end": 1878.1599999999999,
  "text": " plugged in in every place where you have Python to abstract Python away
  from Java. Right? So you", "tokens": [50844, 25679, 294, 294, 633, 1081, 689, 291,
  362, 15329, 281, 12649, 15329, 1314, 490, 10745, 13, 1779, 30, 407, 291, 51180],
  "temperature": 0.0, "avg_logprob": -0.13527759240598095, "compression_ratio": 1.5378486055776892,
  "no_speech_prob": 0.004806575831025839}, {"id": 304, "seek": 186184, "start": 1878.1599999999999,
  "end": 1883.28, "text": " would kind of like just say send this message to an SQS
  queue. And on the other end, there is", "tokens": [51180, 576, 733, 295, 411, 445,
  584, 2845, 341, 3636, 281, 364, 318, 48, 50, 18639, 13, 400, 322, 264, 661, 917,
  11, 456, 307, 51436], "temperature": 0.0, "avg_logprob": -0.13527759240598095, "compression_ratio":
  1.5378486055776892, "no_speech_prob": 0.004806575831025839}, {"id": 305, "seek":
  186184, "start": 1883.28, "end": 1889.84, "text": " somebody consuming it. Can you
  imagine how scalable this can be? It works. It works. You can also", "tokens": [51436,
  2618, 19867, 309, 13, 1664, 291, 3811, 577, 38481, 341, 393, 312, 30, 467, 1985,
  13, 467, 1985, 13, 509, 393, 611, 51764], "temperature": 0.0, "avg_logprob": -0.13527759240598095,
  "compression_ratio": 1.5378486055776892, "no_speech_prob": 0.004806575831025839},
  {"id": 306, "seek": 188984, "start": 1889.84, "end": 1896.24, "text": " like scale
  it locally. But as the whole architecture, I don''t think it''s a very kind of smooth",
  "tokens": [50364, 411, 4373, 309, 16143, 13, 583, 382, 264, 1379, 9482, 11, 286,
  500, 380, 519, 309, 311, 257, 588, 733, 295, 5508, 50684], "temperature": 0.0, "avg_logprob":
  -0.17292574177617612, "compression_ratio": 1.5814977973568283, "no_speech_prob":
  0.002885310212150216}, {"id": 307, "seek": 188984, "start": 1896.24, "end": 1902.08,
  "text": " in a way solution, like not to mention that the performance element of
  it is just not taken care of.", "tokens": [50684, 294, 257, 636, 3827, 11, 411,
  406, 281, 2152, 300, 264, 3389, 4478, 295, 309, 307, 445, 406, 2726, 1127, 295,
  13, 50976], "temperature": 0.0, "avg_logprob": -0.17292574177617612, "compression_ratio":
  1.5814977973568283, "no_speech_prob": 0.002885310212150216}, {"id": 308, "seek":
  188984, "start": 1903.9199999999998, "end": 1911.52, "text": " And what you say
  now, essentially, like with ONX binding in Java, we could just train that model",
  "tokens": [51068, 400, 437, 291, 584, 586, 11, 4476, 11, 411, 365, 9299, 55, 17359,
  294, 10745, 11, 321, 727, 445, 3847, 300, 2316, 51448], "temperature": 0.0, "avg_logprob":
  -0.17292574177617612, "compression_ratio": 1.5814977973568283, "no_speech_prob":
  0.002885310212150216}, {"id": 309, "seek": 188984, "start": 1911.52, "end": 1915.1999999999998,
  "text": " and then export it in ONX format and then use it directly in Java.", "tokens":
  [51448, 293, 550, 10725, 309, 294, 9299, 55, 7877, 293, 550, 764, 309, 3838, 294,
  10745, 13, 51632], "temperature": 0.0, "avg_logprob": -0.17292574177617612, "compression_ratio":
  1.5814977973568283, "no_speech_prob": 0.002885310212150216}, {"id": 310, "seek":
  191520, "start": 1916.0800000000002, "end": 1922.64, "text": " You can''t, yes.
  But you still have to get the inputs to the model. So if", "tokens": [50408, 509,
  393, 380, 11, 2086, 13, 583, 291, 920, 362, 281, 483, 264, 15743, 281, 264, 2316,
  13, 407, 498, 50736], "temperature": 0.0, "avg_logprob": -0.15294763565063477, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.011475927196443081}, {"id": 311, "seek":
  191520, "start": 1925.2, "end": 1929.04, "text": " if it''s like an image or something
  like that, it''s usually pretty easy. But if it''s text, then you", "tokens": [50864,
  498, 309, 311, 411, 364, 3256, 420, 746, 411, 300, 11, 309, 311, 2673, 1238, 1858,
  13, 583, 498, 309, 311, 2487, 11, 550, 291, 51056], "temperature": 0.0, "avg_logprob":
  -0.15294763565063477, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.011475927196443081}, {"id": 312, "seek": 191520, "start": 1929.04, "end": 1934.96,
  "text": " have to tokenize first. And you have to use the right tokenizer. And you
  have to do, you have to", "tokens": [51056, 362, 281, 14862, 1125, 700, 13, 400,
  291, 362, 281, 764, 264, 558, 14862, 6545, 13, 400, 291, 362, 281, 360, 11, 291,
  362, 281, 51352], "temperature": 0.0, "avg_logprob": -0.15294763565063477, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.011475927196443081}, {"id": 313, "seek":
  191520, "start": 1934.96, "end": 1939.04, "text": " kind of jump through a bunch
  of hoops to get it to work correctly. So it''s probably", "tokens": [51352, 733,
  295, 3012, 807, 257, 3840, 295, 1106, 3370, 281, 483, 309, 281, 589, 8944, 13, 407,
  309, 311, 1391, 51556], "temperature": 0.0, "avg_logprob": -0.15294763565063477,
  "compression_ratio": 1.6923076923076923, "no_speech_prob": 0.011475927196443081},
  {"id": 314, "seek": 193904, "start": 1939.84, "end": 1945.12, "text": " a month''s
  worth of work to get a tokenizer working in Java the way you needed to work.", "tokens":
  [50404, 257, 1618, 311, 3163, 295, 589, 281, 483, 257, 14862, 6545, 1364, 294, 10745,
  264, 636, 291, 2978, 281, 589, 13, 50668], "temperature": 0.0, "avg_logprob": -0.19555811260057532,
  "compression_ratio": 1.705607476635514, "no_speech_prob": 0.00319071882404387},
  {"id": 315, "seek": 193904, "start": 1945.84, "end": 1950.48, "text": " Yeah. And
  maybe you could, in principle, share this tokenizer between tasks, right? So", "tokens":
  [50704, 865, 13, 400, 1310, 291, 727, 11, 294, 8665, 11, 2073, 341, 14862, 6545,
  1296, 9608, 11, 558, 30, 407, 50936], "temperature": 0.0, "avg_logprob": -0.19555811260057532,
  "compression_ratio": 1.705607476635514, "no_speech_prob": 0.00319071882404387},
  {"id": 316, "seek": 193904, "start": 1950.48, "end": 1957.36, "text": " it''s for
  sentiment or for entity recognition in principle, you could use the same tokenizer.
  Yeah.", "tokens": [50936, 309, 311, 337, 16149, 420, 337, 13977, 11150, 294, 8665,
  11, 291, 727, 764, 264, 912, 14862, 6545, 13, 865, 13, 51280], "temperature": 0.0,
  "avg_logprob": -0.19555811260057532, "compression_ratio": 1.705607476635514, "no_speech_prob":
  0.00319071882404387}, {"id": 317, "seek": 193904, "start": 1958.3999999999999, "end":
  1964.0, "text": " Right. So the tokenizer is, so the tokenizer relies on the vocabulary
  and the configuration,", "tokens": [51332, 1779, 13, 407, 264, 14862, 6545, 307,
  11, 370, 264, 14862, 6545, 30910, 322, 264, 19864, 293, 264, 11694, 11, 51612],
  "temperature": 0.0, "avg_logprob": -0.19555811260057532, "compression_ratio": 1.705607476635514,
  "no_speech_prob": 0.00319071882404387}, {"id": 318, "seek": 196400, "start": 1964.0,
  "end": 1969.6, "text": " which is bound to the model. So the model is dependent
  on these things. So if you have a generalized", "tokens": [50364, 597, 307, 5472,
  281, 264, 2316, 13, 407, 264, 2316, 307, 12334, 322, 613, 721, 13, 407, 498, 291,
  362, 257, 44498, 50644], "temperature": 0.0, "avg_logprob": -0.22368507385253905,
  "compression_ratio": 1.5108695652173914, "no_speech_prob": 0.008656044490635395},
  {"id": 319, "seek": 196400, "start": 1969.6, "end": 1978.4, "text": " way to load
  the vocabulary and the configuration, then yes, you could just take the thing and",
  "tokens": [50644, 636, 281, 3677, 264, 19864, 293, 264, 11694, 11, 550, 2086, 11,
  291, 727, 445, 747, 264, 551, 293, 51084], "temperature": 0.0, "avg_logprob": -0.22368507385253905,
  "compression_ratio": 1.5108695652173914, "no_speech_prob": 0.008656044490635395},
  {"id": 320, "seek": 196400, "start": 1980.8, "end": 1987.28, "text": " your new
  stack. But having said all this with MITY, you took a different, you know,", "tokens":
  [51204, 428, 777, 8630, 13, 583, 1419, 848, 439, 341, 365, 13100, 56, 11, 291, 1890,
  257, 819, 11, 291, 458, 11, 51528], "temperature": 0.0, "avg_logprob": -0.22368507385253905,
  "compression_ratio": 1.5108695652173914, "no_speech_prob": 0.008656044490635395},
  {"id": 321, "seek": 198728, "start": 1987.44, "end": 1994.0, "text": " approach,
  like the philosophy behind MIT, you''ll offer it as a web server, right?", "tokens":
  [50372, 3109, 11, 411, 264, 10675, 2261, 13100, 11, 291, 603, 2626, 309, 382, 257,
  3670, 7154, 11, 558, 30, 50700], "temperature": 0.0, "avg_logprob": -0.16905337688969632,
  "compression_ratio": 1.574468085106383, "no_speech_prob": 0.011271785944700241},
  {"id": 322, "seek": 198728, "start": 1994.0, "end": 1998.96, "text": " Yeah. And
  again, can you tell me more about it? I mean, I''m sure you can open a lot of detail.",
  "tokens": [50700, 865, 13, 400, 797, 11, 393, 291, 980, 385, 544, 466, 309, 30,
  286, 914, 11, 286, 478, 988, 291, 393, 1269, 257, 688, 295, 2607, 13, 50948], "temperature":
  0.0, "avg_logprob": -0.16905337688969632, "compression_ratio": 1.574468085106383,
  "no_speech_prob": 0.011271785944700241}, {"id": 323, "seek": 198728, "start": 1998.96,
  "end": 2009.2, "text": " Yeah, the reason I went that route is because when you,
  when you want to do model inference,", "tokens": [50948, 865, 11, 264, 1778, 286,
  1437, 300, 7955, 307, 570, 562, 291, 11, 562, 291, 528, 281, 360, 2316, 38253, 11,
  51460], "temperature": 0.0, "avg_logprob": -0.16905337688969632, "compression_ratio":
  1.574468085106383, "no_speech_prob": 0.011271785944700241}, {"id": 324, "seek":
  198728, "start": 2010.48, "end": 2016.0, "text": " you want to give it as much compute
  as possible, right? And you kind of want it to be its own thing.", "tokens": [51524,
  291, 528, 281, 976, 309, 382, 709, 14722, 382, 1944, 11, 558, 30, 400, 291, 733,
  295, 528, 309, 281, 312, 1080, 1065, 551, 13, 51800], "temperature": 0.0, "avg_logprob":
  -0.16905337688969632, "compression_ratio": 1.574468085106383, "no_speech_prob":
  0.011271785944700241}, {"id": 325, "seek": 201600, "start": 2016.64, "end": 2022.24,
  "text": " So I went the microservice route. I''m not, I''m not saying microservices
  are the way of the", "tokens": [50396, 407, 286, 1437, 264, 15547, 25006, 7955,
  13, 286, 478, 406, 11, 286, 478, 406, 1566, 15547, 47480, 366, 264, 636, 295, 264,
  50676], "temperature": 0.0, "avg_logprob": -0.13343693846363133, "compression_ratio":
  1.728301886792453, "no_speech_prob": 0.0013234539655968547}, {"id": 326, "seek":
  201600, "start": 2022.24, "end": 2027.28, "text": " future and they''re better than
  model it''s and all this stuff. But the idea of coupling", "tokens": [50676, 2027,
  293, 436, 434, 1101, 813, 2316, 309, 311, 293, 439, 341, 1507, 13, 583, 264, 1558,
  295, 37447, 50928], "temperature": 0.0, "avg_logprob": -0.13343693846363133, "compression_ratio":
  1.728301886792453, "no_speech_prob": 0.0013234539655968547}, {"id": 327, "seek":
  201600, "start": 2027.28, "end": 2033.28, "text": " with this, you know, this model
  inference is part of like your regular application code.", "tokens": [50928, 365,
  341, 11, 291, 458, 11, 341, 2316, 38253, 307, 644, 295, 411, 428, 3890, 3861, 3089,
  13, 51228], "temperature": 0.0, "avg_logprob": -0.13343693846363133, "compression_ratio":
  1.728301886792453, "no_speech_prob": 0.0013234539655968547}, {"id": 328, "seek":
  201600, "start": 2034.4, "end": 2038.4, "text": " Maybe you don''t want to do that,
  you know, you want to have this other service that can,", "tokens": [51284, 2704,
  291, 500, 380, 528, 281, 360, 300, 11, 291, 458, 11, 291, 528, 281, 362, 341, 661,
  2643, 300, 393, 11, 51484], "temperature": 0.0, "avg_logprob": -0.13343693846363133,
  "compression_ratio": 1.728301886792453, "no_speech_prob": 0.0013234539655968547},
  {"id": 329, "seek": 201600, "start": 2039.2, "end": 2045.52, "text": " and this
  is part of like the bigger ML ops question, which is, well, how often should I update
  models?", "tokens": [51524, 293, 341, 307, 644, 295, 411, 264, 3801, 21601, 44663,
  1168, 11, 597, 307, 11, 731, 11, 577, 2049, 820, 286, 5623, 5245, 30, 51840], "temperature":
  0.0, "avg_logprob": -0.13343693846363133, "compression_ratio": 1.728301886792453,
  "no_speech_prob": 0.0013234539655968547}, {"id": 330, "seek": 204552, "start": 2045.52,
  "end": 2052.0, "text": " What are the things that I just know about, you know, drift
  and all these things that are like,", "tokens": [50364, 708, 366, 264, 721, 300,
  286, 445, 458, 466, 11, 291, 458, 11, 19699, 293, 439, 613, 721, 300, 366, 411,
  11, 50688], "temperature": 0.0, "avg_logprob": -0.10393639907096196, "compression_ratio":
  1.7342342342342343, "no_speech_prob": 0.00017055209900718182}, {"id": 331, "seek":
  204552, "start": 2052.0, "end": 2056.4, "text": " what about logging and all this
  stuff? It''s like, well, okay, you need a way to do this. And if you", "tokens":
  [50688, 437, 466, 27991, 293, 439, 341, 1507, 30, 467, 311, 411, 11, 731, 11, 1392,
  11, 291, 643, 257, 636, 281, 360, 341, 13, 400, 498, 291, 50908], "temperature":
  0.0, "avg_logprob": -0.10393639907096196, "compression_ratio": 1.7342342342342343,
  "no_speech_prob": 0.00017055209900718182}, {"id": 332, "seek": 204552, "start":
  2057.04, "end": 2062.08, "text": " embed model inference in your own code, now you''re
  also responsible for all this stuff, right?", "tokens": [50940, 12240, 2316, 38253,
  294, 428, 1065, 3089, 11, 586, 291, 434, 611, 6250, 337, 439, 341, 1507, 11, 558,
  30, 51192], "temperature": 0.0, "avg_logprob": -0.10393639907096196, "compression_ratio":
  1.7342342342342343, "no_speech_prob": 0.00017055209900718182}, {"id": 333, "seek":
  204552, "start": 2063.68, "end": 2070.32, "text": " So as a, as a microservice,
  you can evolve that microservice and say, all right, this thing is", "tokens": [51272,
  407, 382, 257, 11, 382, 257, 15547, 25006, 11, 291, 393, 16693, 300, 15547, 25006,
  293, 584, 11, 439, 558, 11, 341, 551, 307, 51604], "temperature": 0.0, "avg_logprob":
  -0.10393639907096196, "compression_ratio": 1.7342342342342343, "no_speech_prob":
  0.00017055209900718182}, {"id": 334, "seek": 207032, "start": 2070.32, "end": 2077.76,
  "text": " responsible for model inference and that''s it, right? And then all the
  side effects around that of like,", "tokens": [50364, 6250, 337, 2316, 38253, 293,
  300, 311, 309, 11, 558, 30, 400, 550, 439, 264, 1252, 5065, 926, 300, 295, 411,
  11, 50736], "temperature": 0.0, "avg_logprob": -0.1442105953509991, "compression_ratio":
  1.7056277056277056, "no_speech_prob": 0.0006310308817774057}, {"id": 335, "seek":
  207032, "start": 2077.76, "end": 2083.2000000000003, "text": " okay, well, you need
  a new model, but if you have to AB test models, what if you want to do logging,",
  "tokens": [50736, 1392, 11, 731, 11, 291, 643, 257, 777, 2316, 11, 457, 498, 291,
  362, 281, 13838, 1500, 5245, 11, 437, 498, 291, 528, 281, 360, 27991, 11, 51008],
  "temperature": 0.0, "avg_logprob": -0.1442105953509991, "compression_ratio": 1.7056277056277056,
  "no_speech_prob": 0.0006310308817774057}, {"id": 336, "seek": 207032, "start": 2083.2000000000003,
  "end": 2089.84, "text": " what if you want to do all these other things? You can
  evolve that in its own way and it''s in the", "tokens": [51008, 437, 498, 291, 528,
  281, 360, 439, 613, 661, 721, 30, 509, 393, 16693, 300, 294, 1080, 1065, 636, 293,
  309, 311, 294, 264, 51340], "temperature": 0.0, "avg_logprob": -0.1442105953509991,
  "compression_ratio": 1.7056277056277056, "no_speech_prob": 0.0006310308817774057},
  {"id": 337, "seek": 207032, "start": 2089.84, "end": 2096.7200000000003, "text":
  " separation of concerns makes much more sense. So, and then it kind of gets you
  out of the,", "tokens": [51340, 14634, 295, 7389, 1669, 709, 544, 2020, 13, 407,
  11, 293, 550, 309, 733, 295, 2170, 291, 484, 295, 264, 11, 51684], "temperature":
  0.0, "avg_logprob": -0.1442105953509991, "compression_ratio": 1.7056277056277056,
  "no_speech_prob": 0.0006310308817774057}, {"id": 338, "seek": 209672, "start": 2097.12,
  "end": 2103.4399999999996, "text": " it gets you out of the problem of like, okay,
  well, am I going to build a mighty for Ruby? Am I going", "tokens": [50384, 309,
  2170, 291, 484, 295, 264, 1154, 295, 411, 11, 1392, 11, 731, 11, 669, 286, 516,
  281, 1322, 257, 21556, 337, 19907, 30, 2012, 286, 516, 50700], "temperature": 0.0,
  "avg_logprob": -0.1849060196807419, "compression_ratio": 1.8278388278388278, "no_speech_prob":
  0.0056561920791864395}, {"id": 339, "seek": 209672, "start": 2103.4399999999996,
  "end": 2108.0, "text": " to build mighty for node? Am I going to build ready mighty
  for go? Like, I don''t have to do that. I", "tokens": [50700, 281, 1322, 21556,
  337, 9984, 30, 2012, 286, 516, 281, 1322, 1919, 21556, 337, 352, 30, 1743, 11, 286,
  500, 380, 362, 281, 360, 300, 13, 286, 50928], "temperature": 0.0, "avg_logprob":
  -0.1849060196807419, "compression_ratio": 1.8278388278388278, "no_speech_prob":
  0.0056561920791864395}, {"id": 340, "seek": 209672, "start": 2108.0, "end": 2114.56,
  "text": " can just build mighty inference server as a web server or a GRPC, which
  own, you know, it''s on,", "tokens": [50928, 393, 445, 1322, 21556, 38253, 7154,
  382, 257, 3670, 7154, 420, 257, 10903, 12986, 11, 597, 1065, 11, 291, 458, 11, 309,
  311, 322, 11, 51256], "temperature": 0.0, "avg_logprob": -0.1849060196807419, "compression_ratio":
  1.8278388278388278, "no_speech_prob": 0.0056561920791864395}, {"id": 341, "seek":
  209672, "start": 2114.56, "end": 2118.9599999999996, "text": " it''s on the roadmap.
  I don''t know how long that''s going to take, but now you have this thing. And then",
  "tokens": [51256, 309, 311, 322, 264, 35738, 13, 286, 500, 380, 458, 577, 938, 300,
  311, 516, 281, 747, 11, 457, 586, 291, 362, 341, 551, 13, 400, 550, 51476], "temperature":
  0.0, "avg_logprob": -0.1849060196807419, "compression_ratio": 1.8278388278388278,
  "no_speech_prob": 0.0056561920791864395}, {"id": 342, "seek": 209672, "start": 2118.9599999999996,
  "end": 2124.16, "text": " I just have to write client libraries. And the APIs always
  the same. The client libraries for HTTP", "tokens": [51476, 286, 445, 362, 281,
  2464, 6423, 15148, 13, 400, 264, 21445, 1009, 264, 912, 13, 440, 6423, 15148, 337,
  33283, 51736], "temperature": 0.0, "avg_logprob": -0.1849060196807419, "compression_ratio":
  1.8278388278388278, "no_speech_prob": 0.0056561920791864395}, {"id": 343, "seek":
  212416, "start": 2124.24, "end": 2135.2799999999997, "text": " are super easy. So
  yeah. And if you compare this, let''s say we take a database, like VV8 or", "tokens":
  [50368, 366, 1687, 1858, 13, 407, 1338, 13, 400, 498, 291, 6794, 341, 11, 718, 311,
  584, 321, 747, 257, 8149, 11, 411, 691, 53, 23, 420, 50920], "temperature": 0.0,
  "avg_logprob": -0.21464213346823668, "compression_ratio": 1.4739583333333333, "no_speech_prob":
  0.007369358092546463}, {"id": 344, "seek": 212416, "start": 2135.2799999999997,
  "end": 2143.2799999999997, "text": " SBA, they have inference inside them, right?
  So like, if you already bought into that solution,", "tokens": [50920, 318, 9295,
  11, 436, 362, 38253, 1854, 552, 11, 558, 30, 407, 411, 11, 498, 291, 1217, 4243,
  666, 300, 3827, 11, 51320], "temperature": 0.0, "avg_logprob": -0.21464213346823668,
  "compression_ratio": 1.4739583333333333, "no_speech_prob": 0.007369358092546463},
  {"id": 345, "seek": 212416, "start": 2143.2799999999997, "end": 2149.2799999999997,
  "text": " in principle, you could do this. The only caveat I think is that if you
  have your custom model,", "tokens": [51320, 294, 8665, 11, 291, 727, 360, 341, 13,
  440, 787, 43012, 286, 519, 307, 300, 498, 291, 362, 428, 2375, 2316, 11, 51620],
  "temperature": 0.0, "avg_logprob": -0.21464213346823668, "compression_ratio": 1.4739583333333333,
  "no_speech_prob": 0.007369358092546463}, {"id": 346, "seek": 214928, "start": 2149.28,
  "end": 2156.0800000000004, "text": " you''ll have to go an extra mile to actually
  integrate it inside this database, right? And", "tokens": [50364, 291, 603, 362,
  281, 352, 364, 2857, 12620, 281, 767, 13365, 309, 1854, 341, 8149, 11, 558, 30,
  400, 50704], "temperature": 0.0, "avg_logprob": -0.14749718612095095, "compression_ratio":
  1.606837606837607, "no_speech_prob": 0.0033544660545885563}, {"id": 347, "seek":
  214928, "start": 2156.0800000000004, "end": 2162.2400000000002, "text": " at that
  point, with VV8, I think you will have to master go with SBA, you''ll have to master
  the C", "tokens": [50704, 412, 300, 935, 11, 365, 691, 53, 23, 11, 286, 519, 291,
  486, 362, 281, 4505, 352, 365, 318, 9295, 11, 291, 603, 362, 281, 4505, 264, 383,
  51012], "temperature": 0.0, "avg_logprob": -0.14749718612095095, "compression_ratio":
  1.606837606837607, "no_speech_prob": 0.0033544660545885563}, {"id": 348, "seek":
  214928, "start": 2162.2400000000002, "end": 2167.6800000000003, "text": " plus plus
  or Java. I''m not sure. I''m not an expert in that, but there is a podcast with
  Joe", "tokens": [51012, 1804, 1804, 420, 10745, 13, 286, 478, 406, 988, 13, 286,
  478, 406, 364, 5844, 294, 300, 11, 457, 456, 307, 257, 7367, 365, 6807, 51284],
  "temperature": 0.0, "avg_logprob": -0.14749718612095095, "compression_ratio": 1.606837606837607,
  "no_speech_prob": 0.0033544660545885563}, {"id": 349, "seek": 214928, "start": 2167.6800000000003,
  "end": 2175.0400000000004, "text": " Bergum that you can check out. But yes, so
  how would you kind of like on product side, how would", "tokens": [51284, 27511,
  449, 300, 291, 393, 1520, 484, 13, 583, 2086, 11, 370, 577, 576, 291, 733, 295,
  411, 322, 1674, 1252, 11, 577, 576, 51652], "temperature": 0.0, "avg_logprob": -0.14749718612095095,
  "compression_ratio": 1.606837606837607, "no_speech_prob": 0.0033544660545885563},
  {"id": 350, "seek": 217504, "start": 2175.2, "end": 2184.8, "text": " you compare
  mititude that approach? So VESPA uses on X-Rontane. VESPA wraps on X-Rontane. I
  believe", "tokens": [50372, 291, 6794, 2194, 4377, 300, 3109, 30, 407, 691, 2358,
  10297, 4960, 322, 1783, 12, 49, 896, 1929, 13, 691, 2358, 10297, 25831, 322, 1783,
  12, 49, 896, 1929, 13, 286, 1697, 50852], "temperature": 0.0, "avg_logprob": -0.25370802999544545,
  "compression_ratio": 1.6830357142857142, "no_speech_prob": 0.00028813848621211946},
  {"id": 351, "seek": 217504, "start": 2184.8, "end": 2188.72, "text": " it''s on
  X-Rontane. I know they use on X models. I don''t know how to present it on X-Rontane.",
  "tokens": [50852, 309, 311, 322, 1783, 12, 49, 896, 1929, 13, 286, 458, 436, 764,
  322, 1783, 5245, 13, 286, 500, 380, 458, 577, 281, 1974, 309, 322, 1783, 12, 49,
  896, 1929, 13, 51048], "temperature": 0.0, "avg_logprob": -0.25370802999544545,
  "compression_ratio": 1.6830357142857142, "no_speech_prob": 0.00028813848621211946},
  {"id": 352, "seek": 217504, "start": 2190.8, "end": 2197.12, "text": " So you''d
  still have to go through the step of doing that. With VV8, it''s a little bit different.",
  "tokens": [51152, 407, 291, 1116, 920, 362, 281, 352, 807, 264, 1823, 295, 884,
  300, 13, 2022, 691, 53, 23, 11, 309, 311, 257, 707, 857, 819, 13, 51468], "temperature":
  0.0, "avg_logprob": -0.25370802999544545, "compression_ratio": 1.6830357142857142,
  "no_speech_prob": 0.00028813848621211946}, {"id": 353, "seek": 217504, "start":
  2197.12, "end": 2202.32, "text": " With VV8, you have these things called modules.
  And then the modules are typically like", "tokens": [51468, 2022, 691, 53, 23, 11,
  291, 362, 613, 721, 1219, 16679, 13, 400, 550, 264, 16679, 366, 5850, 411, 51728],
  "temperature": 0.0, "avg_logprob": -0.25370802999544545, "compression_ratio": 1.6830357142857142,
  "no_speech_prob": 0.00028813848621211946}, {"id": 354, "seek": 220232, "start":
  2202.96, "end": 2212.0800000000004, "text": " Docker containers with APIs exposed.
  And then there''s logic written in the module code for", "tokens": [50396, 33772,
  17089, 365, 21445, 9495, 13, 400, 550, 456, 311, 9952, 3720, 294, 264, 10088, 3089,
  337, 50852], "temperature": 0.0, "avg_logprob": -0.14255503245762416, "compression_ratio":
  1.5603864734299517, "no_speech_prob": 0.00028645788552239537}, {"id": 355, "seek":
  220232, "start": 2212.0800000000004, "end": 2218.7200000000003, "text": " VV8 that
  will wrap that API. And it''s easier if you just copy and paste a model and then
  change", "tokens": [50852, 691, 53, 23, 300, 486, 7019, 300, 9362, 13, 400, 309,
  311, 3571, 498, 291, 445, 5055, 293, 9163, 257, 2316, 293, 550, 1319, 51184], "temperature":
  0.0, "avg_logprob": -0.14255503245762416, "compression_ratio": 1.5603864734299517,
  "no_speech_prob": 0.00028645788552239537}, {"id": 356, "seek": 220232, "start":
  2218.7200000000003, "end": 2221.84, "text": " stuff to match the API of the thing
  that you have in a Docker container.", "tokens": [51184, 1507, 281, 2995, 264, 9362,
  295, 264, 551, 300, 291, 362, 294, 257, 33772, 10129, 13, 51340], "temperature":
  0.0, "avg_logprob": -0.14255503245762416, "compression_ratio": 1.5603864734299517,
  "no_speech_prob": 0.00028645788552239537}, {"id": 357, "seek": 220232, "start":
  2224.32, "end": 2230.1600000000003, "text": " So it''s not that much work. You still
  have to know go to do it.", "tokens": [51464, 407, 309, 311, 406, 300, 709, 589,
  13, 509, 920, 362, 281, 458, 352, 281, 360, 309, 13, 51756], "temperature": 0.0,
  "avg_logprob": -0.14255503245762416, "compression_ratio": 1.5603864734299517, "no_speech_prob":
  0.00028645788552239537}, {"id": 358, "seek": 223232, "start": 2232.88, "end": 2243.1200000000003,
  "text": " And yeah, I think the other problem that I have with that approach, and
  I''m not saying it''s wrong,", "tokens": [50392, 400, 1338, 11, 286, 519, 264, 661,
  1154, 300, 286, 362, 365, 300, 3109, 11, 293, 286, 478, 406, 1566, 309, 311, 2085,
  11, 50904], "temperature": 0.0, "avg_logprob": -0.19556961832819758, "compression_ratio":
  1.4270833333333333, "no_speech_prob": 0.0015615865122526884}, {"id": 359, "seek":
  223232, "start": 2243.76, "end": 2250.4, "text": " but from my perspective, so if
  you look at the documentation actually for a couple of vector", "tokens": [50936,
  457, 490, 452, 4585, 11, 370, 498, 291, 574, 412, 264, 14333, 767, 337, 257, 1916,
  295, 8062, 51268], "temperature": 0.0, "avg_logprob": -0.19556961832819758, "compression_ratio":
  1.4270833333333333, "no_speech_prob": 0.0015615865122526884}, {"id": 360, "seek":
  223232, "start": 2250.4, "end": 2256.56, "text": " search engines, I''m not sure
  of VESPA, but I think VV8 and maybe another will say,", "tokens": [51268, 3164,
  12982, 11, 286, 478, 406, 988, 295, 691, 2358, 10297, 11, 457, 286, 519, 691, 53,
  23, 293, 1310, 1071, 486, 584, 11, 51576], "temperature": 0.0, "avg_logprob": -0.19556961832819758,
  "compression_ratio": 1.4270833333333333, "no_speech_prob": 0.0015615865122526884},
  {"id": 361, "seek": 225656, "start": 2256.72, "end": 2262.48, "text": " OK, well,
  it''s better to use a GPU for inference and then CPU for the vector search,", "tokens":
  [50372, 2264, 11, 731, 11, 309, 311, 1101, 281, 764, 257, 18407, 337, 38253, 293,
  550, 13199, 337, 264, 8062, 3164, 11, 50660], "temperature": 0.0, "avg_logprob":
  -0.15691626202929151, "compression_ratio": 1.6576576576576576, "no_speech_prob":
  0.0019621665123850107}, {"id": 362, "seek": 225656, "start": 2262.48, "end": 2270.24,
  "text": " right? Because you want to provide as many workers to the search algorithm
  as possible.", "tokens": [50660, 558, 30, 1436, 291, 528, 281, 2893, 382, 867, 5600,
  281, 264, 3164, 9284, 382, 1944, 13, 51048], "temperature": 0.0, "avg_logprob":
  -0.15691626202929151, "compression_ratio": 1.6576576576576576, "no_speech_prob":
  0.0019621665123850107}, {"id": 363, "seek": 225656, "start": 2270.24, "end": 2278.4,
  "text": " And you don''t want the inference, the model inference, and the vector
  search fighting for resources.", "tokens": [51048, 400, 291, 500, 380, 528, 264,
  38253, 11, 264, 2316, 38253, 11, 293, 264, 8062, 3164, 5237, 337, 3593, 13, 51456],
  "temperature": 0.0, "avg_logprob": -0.15691626202929151, "compression_ratio": 1.6576576576576576,
  "no_speech_prob": 0.0019621665123850107}, {"id": 364, "seek": 225656, "start": 2278.96,
  "end": 2284.24, "text": " Because both are very expensive, right? So they say, hey,
  if you have GPU, then all your model", "tokens": [51484, 1436, 1293, 366, 588, 5124,
  11, 558, 30, 407, 436, 584, 11, 4177, 11, 498, 291, 362, 18407, 11, 550, 439, 428,
  2316, 51748], "temperature": 0.0, "avg_logprob": -0.15691626202929151, "compression_ratio":
  1.6576576576576576, "no_speech_prob": 0.0019621665123850107}, {"id": 365, "seek":
  228424, "start": 2284.24, "end": 2289.04, "text": " inferences and GPU and your
  vector search is all CPU and you get this one perfect box and", "tokens": [50364,
  13596, 2667, 293, 18407, 293, 428, 8062, 3164, 307, 439, 13199, 293, 291, 483, 341,
  472, 2176, 2424, 293, 50604], "temperature": 0.0, "avg_logprob": -0.1686912737394634,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.00260981940664351},
  {"id": 366, "seek": 228424, "start": 2289.04, "end": 2296.4799999999996, "text":
  " everything just works. But OK, well, what if you want to scale beyond that? You
  can only send so", "tokens": [50604, 1203, 445, 1985, 13, 583, 2264, 11, 731, 11,
  437, 498, 291, 528, 281, 4373, 4399, 300, 30, 509, 393, 787, 2845, 370, 50976],
  "temperature": 0.0, "avg_logprob": -0.1686912737394634, "compression_ratio": 1.5932203389830508,
  "no_speech_prob": 0.00260981940664351}, {"id": 367, "seek": 228424, "start": 2296.4799999999996,
  "end": 2304.56, "text": " many documents into a GPU at a time. What if I need 12
  machines? Well, now I need 12 machines", "tokens": [50976, 867, 8512, 666, 257,
  18407, 412, 257, 565, 13, 708, 498, 286, 643, 2272, 8379, 30, 1042, 11, 586, 286,
  643, 2272, 8379, 51380], "temperature": 0.0, "avg_logprob": -0.1686912737394634,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.00260981940664351},
  {"id": 368, "seek": 228424, "start": 2304.56, "end": 2312.08, "text": " that are
  all hosting VV8 and they''re all hosting mighty or whatever your inference solution
  is,", "tokens": [51380, 300, 366, 439, 16058, 691, 53, 23, 293, 436, 434, 439, 16058,
  21556, 420, 2035, 428, 38253, 3827, 307, 11, 51756], "temperature": 0.0, "avg_logprob":
  -0.1686912737394634, "compression_ratio": 1.5932203389830508, "no_speech_prob":
  0.00260981940664351}, {"id": 369, "seek": 231208, "start": 2312.08, "end": 2316.7999999999997,
  "text": " all it wants, right? So this goes back to the separation of concerns,",
  "tokens": [50364, 439, 309, 2738, 11, 558, 30, 407, 341, 1709, 646, 281, 264, 14634,
  295, 7389, 11, 50600], "temperature": 0.0, "avg_logprob": -0.13059596186098846,
  "compression_ratio": 1.7213740458015268, "no_speech_prob": 0.003360312432050705},
  {"id": 370, "seek": 231208, "start": 2316.7999999999997, "end": 2321.44, "text":
  " problems. Like, well, what if I have a lot of documents that I need to process?
  And it doesn''t take", "tokens": [50600, 2740, 13, 1743, 11, 731, 11, 437, 498,
  286, 362, 257, 688, 295, 8512, 300, 286, 643, 281, 1399, 30, 400, 309, 1177, 380,
  747, 50832], "temperature": 0.0, "avg_logprob": -0.13059596186098846, "compression_ratio":
  1.7213740458015268, "no_speech_prob": 0.003360312432050705}, {"id": 371, "seek":
  231208, "start": 2321.44, "end": 2326.56, "text": " that long to get them into the
  vector search by the vectors, but processing those documents", "tokens": [50832,
  300, 938, 281, 483, 552, 666, 264, 8062, 3164, 538, 264, 18875, 11, 457, 9007, 729,
  8512, 51088], "temperature": 0.0, "avg_logprob": -0.13059596186098846, "compression_ratio":
  1.7213740458015268, "no_speech_prob": 0.003360312432050705}, {"id": 372, "seek":
  231208, "start": 2326.56, "end": 2332.48, "text": " takes a long time. So I have
  to pre-process. Well, now you''ve kind of got like this situation where", "tokens":
  [51088, 2516, 257, 938, 565, 13, 407, 286, 362, 281, 659, 12, 41075, 13, 1042, 11,
  586, 291, 600, 733, 295, 658, 411, 341, 2590, 689, 51384], "temperature": 0.0, "avg_logprob":
  -0.13059596186098846, "compression_ratio": 1.7213740458015268, "no_speech_prob":
  0.003360312432050705}, {"id": 373, "seek": 231208, "start": 2332.48, "end": 2338.72,
  "text": " you might need another solution to do this batch pre-processing, right?
  In another place.", "tokens": [51384, 291, 1062, 643, 1071, 3827, 281, 360, 341,
  15245, 659, 12, 41075, 278, 11, 558, 30, 682, 1071, 1081, 13, 51696], "temperature":
  0.0, "avg_logprob": -0.13059596186098846, "compression_ratio": 1.7213740458015268,
  "no_speech_prob": 0.003360312432050705}, {"id": 374, "seek": 233872, "start": 2339.3599999999997,
  "end": 2345.3599999999997, "text": " And then you bypass the module when you integrate
  into VV8. You just want to send the", "tokens": [50396, 400, 550, 291, 24996, 264,
  10088, 562, 291, 13365, 666, 691, 53, 23, 13, 509, 445, 528, 281, 2845, 264, 50696],
  "temperature": 0.0, "avg_logprob": -0.19641963640848795, "compression_ratio": 1.7338403041825095,
  "no_speech_prob": 0.005385193973779678}, {"id": 375, "seek": 233872, "start": 2345.3599999999997,
  "end": 2350.3199999999997, "text": " vectors directly to VV8 so you don''t have
  any inference. You send the vector to it. So,", "tokens": [50696, 18875, 3838, 281,
  691, 53, 23, 370, 291, 500, 380, 362, 604, 38253, 13, 509, 2845, 264, 8062, 281,
  309, 13, 407, 11, 50944], "temperature": 0.0, "avg_logprob": -0.19641963640848795,
  "compression_ratio": 1.7338403041825095, "no_speech_prob": 0.005385193973779678},
  {"id": 376, "seek": 233872, "start": 2351.2, "end": 2358.0, "text": " again, it''s
  like this. I''m not saying it''s wrong. I think it''s a great idea because you can
  just", "tokens": [50988, 797, 11, 309, 311, 411, 341, 13, 286, 478, 406, 1566, 309,
  311, 2085, 13, 286, 519, 309, 311, 257, 869, 1558, 570, 291, 393, 445, 51328], "temperature":
  0.0, "avg_logprob": -0.19641963640848795, "compression_ratio": 1.7338403041825095,
  "no_speech_prob": 0.005385193973779678}, {"id": 377, "seek": 233872, "start": 2358.0,
  "end": 2362.64, "text": " install something that will just work, right? You don''t
  have to install like three different things", "tokens": [51328, 3625, 746, 300,
  486, 445, 589, 11, 558, 30, 509, 500, 380, 362, 281, 3625, 411, 1045, 819, 721,
  51560], "temperature": 0.0, "avg_logprob": -0.19641963640848795, "compression_ratio":
  1.7338403041825095, "no_speech_prob": 0.005385193973779678}, {"id": 378, "seek":
  233872, "start": 2362.64, "end": 2368.48, "text": " and try to figure it all out.
  So I think that getting up to speed on that is probably", "tokens": [51560, 293,
  853, 281, 2573, 309, 439, 484, 13, 407, 286, 519, 300, 1242, 493, 281, 3073, 322,
  300, 307, 1391, 51852], "temperature": 0.0, "avg_logprob": -0.19641963640848795,
  "compression_ratio": 1.7338403041825095, "no_speech_prob": 0.005385193973779678},
  {"id": 379, "seek": 236848, "start": 2368.48, "end": 2374.96, "text": " quick. But
  in the long term, like the scalability overall, I think that you now have this coupling",
  "tokens": [50364, 1702, 13, 583, 294, 264, 938, 1433, 11, 411, 264, 15664, 2310,
  4787, 11, 286, 519, 300, 291, 586, 362, 341, 37447, 50688], "temperature": 0.0,
  "avg_logprob": -0.12974992835003396, "compression_ratio": 1.6245614035087719, "no_speech_prob":
  0.0026637595146894455}, {"id": 380, "seek": 236848, "start": 2374.96, "end": 2378.16,
  "text": " and it''s a bit of a challenge. So I don''t know how that gets resolved.",
  "tokens": [50688, 293, 309, 311, 257, 857, 295, 257, 3430, 13, 407, 286, 500, 380,
  458, 577, 300, 2170, 20772, 13, 50848], "temperature": 0.0, "avg_logprob": -0.12974992835003396,
  "compression_ratio": 1.6245614035087719, "no_speech_prob": 0.0026637595146894455},
  {"id": 381, "seek": 236848, "start": 2379.28, "end": 2384.64, "text": " Yeah, that''s
  actually a good point because you reminded me of, I don''t remember precisely what
  we", "tokens": [50904, 865, 11, 300, 311, 767, 257, 665, 935, 570, 291, 15920, 385,
  295, 11, 286, 500, 380, 1604, 13402, 437, 321, 51172], "temperature": 0.0, "avg_logprob":
  -0.12974992835003396, "compression_ratio": 1.6245614035087719, "no_speech_prob":
  0.0026637595146894455}, {"id": 382, "seek": 236848, "start": 2384.64, "end": 2391.12,
  "text": " were sort of balancing between, but like with solar and a Java pipeline
  in front of it. So the", "tokens": [51172, 645, 1333, 295, 22495, 1296, 11, 457,
  411, 365, 7936, 293, 257, 10745, 15517, 294, 1868, 295, 309, 13, 407, 264, 51496],
  "temperature": 0.0, "avg_logprob": -0.12974992835003396, "compression_ratio": 1.6245614035087719,
  "no_speech_prob": 0.0026637595146894455}, {"id": 383, "seek": 236848, "start": 2391.12,
  "end": 2397.6, "text": " pipeline would process documents as they come in, you know,
  chunk them, classify them, run sentiment", "tokens": [51496, 15517, 576, 1399, 8512,
  382, 436, 808, 294, 11, 291, 458, 11, 16635, 552, 11, 33872, 552, 11, 1190, 16149,
  51820], "temperature": 0.0, "avg_logprob": -0.12974992835003396, "compression_ratio":
  1.6245614035087719, "no_speech_prob": 0.0026637595146894455}, {"id": 384, "seek":
  239760, "start": 2397.6, "end": 2404.56, "text": " analysis on them and so on. We
  were thinking, okay, some of these things could be computed inside", "tokens": [50364,
  5215, 322, 552, 293, 370, 322, 13, 492, 645, 1953, 11, 1392, 11, 512, 295, 613,
  721, 727, 312, 40610, 1854, 50712], "temperature": 0.0, "avg_logprob": -0.15172861019770303,
  "compression_ratio": 1.603448275862069, "no_speech_prob": 0.0005646685021929443},
  {"id": 385, "seek": 239760, "start": 2404.56, "end": 2410.72, "text": " solar. Like
  we could write some clever plugin which actually does, I mean, solar has a lot of",
  "tokens": [50712, 7936, 13, 1743, 321, 727, 2464, 512, 13494, 23407, 597, 767, 775,
  11, 286, 914, 11, 7936, 575, 257, 688, 295, 51020], "temperature": 0.0, "avg_logprob":
  -0.15172861019770303, "compression_ratio": 1.603448275862069, "no_speech_prob":
  0.0005646685021929443}, {"id": 386, "seek": 239760, "start": 2410.72, "end": 2415.92,
  "text": " things there, you know, like before it indexes the document, you can run
  like a ton of things.", "tokens": [51020, 721, 456, 11, 291, 458, 11, 411, 949,
  309, 8186, 279, 264, 4166, 11, 291, 393, 1190, 411, 257, 2952, 295, 721, 13, 51280],
  "temperature": 0.0, "avg_logprob": -0.15172861019770303, "compression_ratio": 1.603448275862069,
  "no_speech_prob": 0.0005646685021929443}, {"id": 387, "seek": 239760, "start": 2415.92,
  "end": 2420.08, "text": " I think OpenNLP is one example, right? You could plug
  in and it runs something there.", "tokens": [51280, 286, 519, 7238, 45, 45196, 307,
  472, 1365, 11, 558, 30, 509, 727, 5452, 294, 293, 309, 6676, 746, 456, 13, 51488],
  "temperature": 0.0, "avg_logprob": -0.15172861019770303, "compression_ratio": 1.603448275862069,
  "no_speech_prob": 0.0005646685021929443}, {"id": 388, "seek": 242008, "start": 2420.48,
  "end": 2428.88, "text": " And I remember that my manager, like who was a VP of engineering,
  he came and said, hey,", "tokens": [50384, 400, 286, 1604, 300, 452, 6598, 11, 411,
  567, 390, 257, 35812, 295, 7043, 11, 415, 1361, 293, 848, 11, 4177, 11, 50804],
  "temperature": 0.0, "avg_logprob": -0.14155952297911353, "compression_ratio": 1.5601659751037344,
  "no_speech_prob": 0.011596374213695526}, {"id": 389, "seek": 242008, "start": 2428.88,
  "end": 2434.64, "text": " what if we lose solar? So we computed everything inside
  solar, stored it and lost it. Then what?", "tokens": [50804, 437, 498, 321, 3624,
  7936, 30, 407, 321, 40610, 1203, 1854, 7936, 11, 12187, 309, 293, 2731, 309, 13,
  1396, 437, 30, 51092], "temperature": 0.0, "avg_logprob": -0.14155952297911353,
  "compression_ratio": 1.5601659751037344, "no_speech_prob": 0.011596374213695526},
  {"id": 390, "seek": 242008, "start": 2435.44, "end": 2440.64, "text": " Like now
  you need to bring it up back really quickly and usually what you want to do is probably
  like", "tokens": [51132, 1743, 586, 291, 643, 281, 1565, 309, 493, 646, 534, 2661,
  293, 2673, 437, 291, 528, 281, 360, 307, 1391, 411, 51392], "temperature": 0.0,
  "avg_logprob": -0.14155952297911353, "compression_ratio": 1.5601659751037344, "no_speech_prob":
  0.011596374213695526}, {"id": 391, "seek": 242008, "start": 2440.64, "end": 2446.08,
  "text": " replicate some shard and off you go, right? But if you don''t have that
  data, you need to", "tokens": [51392, 25356, 512, 402, 515, 293, 766, 291, 352,
  11, 558, 30, 583, 498, 291, 500, 380, 362, 300, 1412, 11, 291, 643, 281, 51664],
  "temperature": 0.0, "avg_logprob": -0.14155952297911353, "compression_ratio": 1.5601659751037344,
  "no_speech_prob": 0.011596374213695526}, {"id": 392, "seek": 244608, "start": 2446.08,
  "end": 2451.84, "text": " recompute it now. So you don''t have any intermediate
  storage. Solar is not the storage. Solar is", "tokens": [50364, 48000, 1169, 309,
  586, 13, 407, 291, 500, 380, 362, 604, 19376, 6725, 13, 22385, 307, 406, 264, 6725,
  13, 22385, 307, 50652], "temperature": 0.0, "avg_logprob": -0.1170184378530465,
  "compression_ratio": 1.75, "no_speech_prob": 0.002784757874906063}, {"id": 393,
  "seek": 244608, "start": 2451.84, "end": 2457.68, "text": " the database. And so
  we backtracked and we said, okay, we will compute everything and store it", "tokens":
  [50652, 264, 8149, 13, 400, 370, 321, 646, 19466, 292, 293, 321, 848, 11, 1392,
  11, 321, 486, 14722, 1203, 293, 3531, 309, 50944], "temperature": 0.0, "avg_logprob":
  -0.1170184378530465, "compression_ratio": 1.75, "no_speech_prob": 0.002784757874906063},
  {"id": 394, "seek": 244608, "start": 2457.68, "end": 2464.4, "text": " in S3, you
  know, in file storage. And if in the event of losing solar, we will restore it and",
  "tokens": [50944, 294, 318, 18, 11, 291, 458, 11, 294, 3991, 6725, 13, 400, 498,
  294, 264, 2280, 295, 7027, 7936, 11, 321, 486, 15227, 309, 293, 51280], "temperature":
  0.0, "avg_logprob": -0.1170184378530465, "compression_ratio": 1.75, "no_speech_prob":
  0.002784757874906063}, {"id": 395, "seek": 244608, "start": 2464.4, "end": 2472.3199999999997,
  "text": " reindex everything on the fly. So I mean, that kind of also like, you
  know, resurrected that", "tokens": [51280, 319, 471, 3121, 1203, 322, 264, 3603,
  13, 407, 286, 914, 11, 300, 733, 295, 611, 411, 11, 291, 458, 11, 48825, 300, 51676],
  "temperature": 0.0, "avg_logprob": -0.1170184378530465, "compression_ratio": 1.75,
  "no_speech_prob": 0.002784757874906063}, {"id": 396, "seek": 247232, "start": 2472.56,
  "end": 2478.48, "text": " situation that also be deviated or quadrant to any other
  database. If you lose the fact,", "tokens": [50376, 2590, 300, 611, 312, 31219,
  770, 420, 46856, 281, 604, 661, 8149, 13, 759, 291, 3624, 264, 1186, 11, 50672],
  "temperature": 0.0, "avg_logprob": -0.1890843255179269, "compression_ratio": 1.7889908256880733,
  "no_speech_prob": 0.004681700374931097}, {"id": 397, "seek": 247232, "start": 2478.48,
  "end": 2483.36, "text": " if you lose the database, you lose the vectors. So if
  you have computed them inside the database,", "tokens": [50672, 498, 291, 3624,
  264, 8149, 11, 291, 3624, 264, 18875, 13, 407, 498, 291, 362, 40610, 552, 1854,
  264, 8149, 11, 50916], "temperature": 0.0, "avg_logprob": -0.1890843255179269, "compression_ratio":
  1.7889908256880733, "no_speech_prob": 0.004681700374931097}, {"id": 398, "seek":
  247232, "start": 2483.36, "end": 2488.88, "text": " now bringing it back and then
  turning it on and say, hey, please compute my vectors again, please,", "tokens":
  [50916, 586, 5062, 309, 646, 293, 550, 6246, 309, 322, 293, 584, 11, 4177, 11, 1767,
  14722, 452, 18875, 797, 11, 1767, 11, 51192], "temperature": 0.0, "avg_logprob":
  -0.1890843255179269, "compression_ratio": 1.7889908256880733, "no_speech_prob":
  0.004681700374931097}, {"id": 399, "seek": 247232, "start": 2488.88, "end": 2497.92,
  "text": " please, please, you know, just too much time. You''re exactly right. And
  this is a lesson that I learned.", "tokens": [51192, 1767, 11, 1767, 11, 291, 458,
  11, 445, 886, 709, 565, 13, 509, 434, 2293, 558, 13, 400, 341, 307, 257, 6898, 300,
  286, 3264, 13, 51644], "temperature": 0.0, "avg_logprob": -0.1890843255179269, "compression_ratio":
  1.7889908256880733, "no_speech_prob": 0.004681700374931097}, {"id": 400, "seek":
  249792, "start": 2498.88, "end": 2503.28, "text": " I didn''t learn this lesson
  the hard way, thankfully. But this is just a lesson I learned picking", "tokens":
  [50412, 286, 994, 380, 1466, 341, 6898, 264, 1152, 636, 11, 27352, 13, 583, 341,
  307, 445, 257, 6898, 286, 3264, 8867, 50632], "temperature": 0.0, "avg_logprob":
  -0.13989214536522618, "compression_ratio": 1.7194244604316546, "no_speech_prob":
  0.0031802107114344835}, {"id": 401, "seek": 249792, "start": 2503.28, "end": 2510.32,
  "text": " stuff up when I was at, when I was at Walter''s Clure, which is a huge
  publishing firm. And you have,", "tokens": [50632, 1507, 493, 562, 286, 390, 412,
  11, 562, 286, 390, 412, 21572, 311, 2033, 540, 11, 597, 307, 257, 2603, 17832, 6174,
  13, 400, 291, 362, 11, 50984], "temperature": 0.0, "avg_logprob": -0.13989214536522618,
  "compression_ratio": 1.7194244604316546, "no_speech_prob": 0.0031802107114344835},
  {"id": 402, "seek": 249792, "start": 2510.32, "end": 2514.8, "text": " you have
  your content, which is like editorial content, primary source content. And it''s,",
  "tokens": [50984, 291, 362, 428, 2701, 11, 597, 307, 411, 33412, 2701, 11, 6194,
  4009, 2701, 13, 400, 309, 311, 11, 51208], "temperature": 0.0, "avg_logprob": -0.13989214536522618,
  "compression_ratio": 1.7194244604316546, "no_speech_prob": 0.0031802107114344835},
  {"id": 403, "seek": 249792, "start": 2515.76, "end": 2521.92, "text": " it''s written
  in such a way where it''s it''s pretty raw from a machine perspective, you know.
  And", "tokens": [51256, 309, 311, 3720, 294, 1270, 257, 636, 689, 309, 311, 309,
  311, 1238, 8936, 490, 257, 3479, 4585, 11, 291, 458, 13, 400, 51564], "temperature":
  0.0, "avg_logprob": -0.13989214536522618, "compression_ratio": 1.7194244604316546,
  "no_speech_prob": 0.0031802107114344835}, {"id": 404, "seek": 249792, "start": 2521.92,
  "end": 2526.0, "text": " then it goes through a series of enrichments and transformations.
  So eventually it reaches the", "tokens": [51564, 550, 309, 1709, 807, 257, 2638,
  295, 18849, 1117, 293, 34852, 13, 407, 4728, 309, 14235, 264, 51768], "temperature":
  0.0, "avg_logprob": -0.13989214536522618, "compression_ratio": 1.7194244604316546,
  "no_speech_prob": 0.0031802107114344835}, {"id": 405, "seek": 252600, "start": 2526.0,
  "end": 2531.12, "text": " search engine. But every step along the way, it''s like,
  okay, well, we need to add topics to classify", "tokens": [50364, 3164, 2848, 13,
  583, 633, 1823, 2051, 264, 636, 11, 309, 311, 411, 11, 1392, 11, 731, 11, 321, 643,
  281, 909, 8378, 281, 33872, 50620], "temperature": 0.0, "avg_logprob": -0.1483428147587463,
  "compression_ratio": 1.8661710037174721, "no_speech_prob": 0.0020140265114605427},
  {"id": 406, "seek": 252600, "start": 2531.12, "end": 2535.68, "text": " topics,
  right? So I''m going to add the topics. And then I''m going to save that state that''s
  now on", "tokens": [50620, 8378, 11, 558, 30, 407, 286, 478, 516, 281, 909, 264,
  8378, 13, 400, 550, 286, 478, 516, 281, 3155, 300, 1785, 300, 311, 586, 322, 50848],
  "temperature": 0.0, "avg_logprob": -0.1483428147587463, "compression_ratio": 1.8661710037174721,
  "no_speech_prob": 0.0020140265114605427}, {"id": 407, "seek": 252600, "start": 2535.68,
  "end": 2541.28, "text": " disk somewhere back to, okay, well, now I have to, you
  know, add this other thing, you know, do any", "tokens": [50848, 12355, 4079, 646,
  281, 11, 1392, 11, 731, 11, 586, 286, 362, 281, 11, 291, 458, 11, 909, 341, 661,
  551, 11, 291, 458, 11, 360, 604, 51128], "temperature": 0.0, "avg_logprob": -0.1483428147587463,
  "compression_ratio": 1.8661710037174721, "no_speech_prob": 0.0020140265114605427},
  {"id": 408, "seek": 252600, "start": 2541.28, "end": 2545.68, "text": " recognition
  or something. That''s also saved, right? So you have all these intermediate steps.
  So if", "tokens": [51128, 11150, 420, 746, 13, 663, 311, 611, 6624, 11, 558, 30,
  407, 291, 362, 439, 613, 19376, 4439, 13, 407, 498, 51348], "temperature": 0.0,
  "avg_logprob": -0.1483428147587463, "compression_ratio": 1.8661710037174721, "no_speech_prob":
  0.0020140265114605427}, {"id": 409, "seek": 252600, "start": 2545.68, "end": 2550.32,
  "text": " you lose anything, it''s really easy. You don''t have to rerun the entire,
  you have to rerun the entire", "tokens": [51348, 291, 3624, 1340, 11, 309, 311,
  534, 1858, 13, 509, 500, 380, 362, 281, 43819, 409, 264, 2302, 11, 291, 362, 281,
  43819, 409, 264, 2302, 51580], "temperature": 0.0, "avg_logprob": -0.1483428147587463,
  "compression_ratio": 1.8661710037174721, "no_speech_prob": 0.0020140265114605427},
  {"id": 410, "seek": 255032, "start": 2550.32, "end": 2557.04, "text": " pipeline.
  It takes you months to do that. Not just days, but like literally months to start
  from", "tokens": [50364, 15517, 13, 467, 2516, 291, 2493, 281, 360, 300, 13, 1726,
  445, 1708, 11, 457, 411, 3736, 2493, 281, 722, 490, 50700], "temperature": 0.0,
  "avg_logprob": -0.13068068118495796, "compression_ratio": 1.7956989247311828, "no_speech_prob":
  0.004148334264755249}, {"id": 411, "seek": 255032, "start": 2557.04, "end": 2564.0,
  "text": " scratch with content. So that''s like a disastrous scenario. So this lesson
  that you learn is, okay,", "tokens": [50700, 8459, 365, 2701, 13, 407, 300, 311,
  411, 257, 44502, 9005, 13, 407, 341, 6898, 300, 291, 1466, 307, 11, 1392, 11, 51048],
  "temperature": 0.0, "avg_logprob": -0.13068068118495796, "compression_ratio": 1.7956989247311828,
  "no_speech_prob": 0.004148334264755249}, {"id": 412, "seek": 255032, "start": 2564.0,
  "end": 2567.6800000000003, "text": " well, yeah, you don''t do, you don''t do everything
  all in one place. Because if you lose it, then it''s", "tokens": [51048, 731, 11,
  1338, 11, 291, 500, 380, 360, 11, 291, 500, 380, 360, 1203, 439, 294, 472, 1081,
  13, 1436, 498, 291, 3624, 309, 11, 550, 309, 311, 51232], "temperature": 0.0, "avg_logprob":
  -0.13068068118495796, "compression_ratio": 1.7956989247311828, "no_speech_prob":
  0.004148334264755249}, {"id": 413, "seek": 255032, "start": 2567.6800000000003,
  "end": 2573.76, "text": " all gone. You have to start from scratch. So yeah, separating
  concerns in that way. And then the idea", "tokens": [51232, 439, 2780, 13, 509,
  362, 281, 722, 490, 8459, 13, 407, 1338, 11, 29279, 7389, 294, 300, 636, 13, 400,
  550, 264, 1558, 51536], "temperature": 0.0, "avg_logprob": -0.13068068118495796,
  "compression_ratio": 1.7956989247311828, "no_speech_prob": 0.004148334264755249},
  {"id": 414, "seek": 255032, "start": 2573.76, "end": 2577.92, "text": " of, well,
  you can plug this thing in anywhere along the chain now, you know, you have this,
  you have", "tokens": [51536, 295, 11, 731, 11, 291, 393, 5452, 341, 551, 294, 4992,
  2051, 264, 5021, 586, 11, 291, 458, 11, 291, 362, 341, 11, 291, 362, 51744], "temperature":
  0.0, "avg_logprob": -0.13068068118495796, "compression_ratio": 1.7956989247311828,
  "no_speech_prob": 0.004148334264755249}, {"id": 415, "seek": 257792, "start": 2577.92,
  "end": 2581.6800000000003, "text": " a microservice, you can put it in, you can
  put it anywhere. And then you can, you don''t even have to", "tokens": [50364, 257,
  15547, 25006, 11, 291, 393, 829, 309, 294, 11, 291, 393, 829, 309, 4992, 13, 400,
  550, 291, 393, 11, 291, 500, 380, 754, 362, 281, 50552], "temperature": 0.0, "avg_logprob":
  -0.12371279808782762, "compression_ratio": 1.9673202614379084, "no_speech_prob":
  0.0010272186482325196}, {"id": 416, "seek": 257792, "start": 2581.6800000000003,
  "end": 2586.0, "text": " just take the vectors and then stick them in the search
  engine, right? But what if you want, what if", "tokens": [50552, 445, 747, 264,
  18875, 293, 550, 2897, 552, 294, 264, 3164, 2848, 11, 558, 30, 583, 437, 498, 291,
  528, 11, 437, 498, 50768], "temperature": 0.0, "avg_logprob": -0.12371279808782762,
  "compression_ratio": 1.9673202614379084, "no_speech_prob": 0.0010272186482325196},
  {"id": 417, "seek": 257792, "start": 2586.0, "end": 2590.08, "text": " you need
  the vectors and you want to do something else? What if you have like a recommendations
  platform", "tokens": [50768, 291, 643, 264, 18875, 293, 291, 528, 281, 360, 746,
  1646, 30, 708, 498, 291, 362, 411, 257, 10434, 3663, 50972], "temperature": 0.0,
  "avg_logprob": -0.12371279808782762, "compression_ratio": 1.9673202614379084, "no_speech_prob":
  0.0010272186482325196}, {"id": 418, "seek": 257792, "start": 2590.08, "end": 2593.52,
  "text": " and you have this other system over here and you want to do this other
  stuff? It''s like, well,", "tokens": [50972, 293, 291, 362, 341, 661, 1185, 670,
  510, 293, 291, 528, 281, 360, 341, 661, 1507, 30, 467, 311, 411, 11, 731, 11, 51144],
  "temperature": 0.0, "avg_logprob": -0.12371279808782762, "compression_ratio": 1.9673202614379084,
  "no_speech_prob": 0.0010272186482325196}, {"id": 419, "seek": 257792, "start": 2593.52,
  "end": 2598.0, "text": " now you have to think about routing and all these other
  things. But if you just have an easy way to", "tokens": [51144, 586, 291, 362, 281,
  519, 466, 32722, 293, 439, 613, 661, 721, 13, 583, 498, 291, 445, 362, 364, 1858,
  636, 281, 51368], "temperature": 0.0, "avg_logprob": -0.12371279808782762, "compression_ratio":
  1.9673202614379084, "no_speech_prob": 0.0010272186482325196}, {"id": 420, "seek":
  257792, "start": 2598.0, "end": 2604.16, "text": " get vectors, you know, plug it
  anywhere along the stack, then that''s up to you. You know, there''s no", "tokens":
  [51368, 483, 18875, 11, 291, 458, 11, 5452, 309, 4992, 2051, 264, 8630, 11, 550,
  300, 311, 493, 281, 291, 13, 509, 458, 11, 456, 311, 572, 51676], "temperature":
  0.0, "avg_logprob": -0.12371279808782762, "compression_ratio": 1.9673202614379084,
  "no_speech_prob": 0.0010272186482325196}, {"id": 421, "seek": 260416, "start": 2605.12,
  "end": 2610.3199999999997, "text": " prescribed way of doing things. It''s a Lego.
  You put the Lego wherever you want.", "tokens": [50412, 29099, 636, 295, 884, 721,
  13, 467, 311, 257, 28761, 13, 509, 829, 264, 28761, 8660, 291, 528, 13, 50672],
  "temperature": 0.0, "avg_logprob": -0.21572314026535197, "compression_ratio": 1.5690376569037656,
  "no_speech_prob": 0.0036720873322337866}, {"id": 422, "seek": 260416, "start": 2610.3199999999997,
  "end": 2619.7599999999998, "text": " Yeah, that''s a great point because we also
  implemented like an algorithm, which was it computing", "tokens": [50672, 865, 11,
  300, 311, 257, 869, 935, 570, 321, 611, 12270, 411, 364, 9284, 11, 597, 390, 309,
  15866, 51144], "temperature": 0.0, "avg_logprob": -0.21572314026535197, "compression_ratio":
  1.5690376569037656, "no_speech_prob": 0.0036720873322337866}, {"id": 423, "seek":
  260416, "start": 2619.7599999999998, "end": 2627.04, "text": " some topics, I think.
  And we used fast text and work to back vectors. But we didn''t need the vectors",
  "tokens": [51144, 512, 8378, 11, 286, 519, 13, 400, 321, 1143, 2370, 2487, 293,
  589, 281, 646, 18875, 13, 583, 321, 994, 380, 643, 264, 18875, 51508], "temperature":
  0.0, "avg_logprob": -0.21572314026535197, "compression_ratio": 1.5690376569037656,
  "no_speech_prob": 0.0036720873322337866}, {"id": 424, "seek": 260416, "start": 2627.04,
  "end": 2632.48, "text": " in the end in the downstream system. We just computed
  them, clustered, ran some magic algorithm,", "tokens": [51508, 294, 264, 917, 294,
  264, 30621, 1185, 13, 492, 445, 40610, 552, 11, 596, 38624, 11, 5872, 512, 5585,
  9284, 11, 51780], "temperature": 0.0, "avg_logprob": -0.21572314026535197, "compression_ratio":
  1.5690376569037656, "no_speech_prob": 0.0036720873322337866}, {"id": 425, "seek":
  263248, "start": 2633.12, "end": 2639.52, "text": " you know, produced topics and
  then you store the topics. So you store actual words in some", "tokens": [50396,
  291, 458, 11, 7126, 8378, 293, 550, 291, 3531, 264, 8378, 13, 407, 291, 3531, 3539,
  2283, 294, 512, 50716], "temperature": 0.0, "avg_logprob": -0.2163111822945731,
  "compression_ratio": 1.618421052631579, "no_speech_prob": 0.0015619659097865224},
  {"id": 426, "seek": 263248, "start": 2639.52, "end": 2644.2400000000002, "text":
  " database, so index them in the search engine. So yeah, you''re absolutely right.
  Like, sometimes", "tokens": [50716, 8149, 11, 370, 8186, 552, 294, 264, 3164, 2848,
  13, 407, 1338, 11, 291, 434, 3122, 558, 13, 1743, 11, 2171, 50952], "temperature":
  0.0, "avg_logprob": -0.2163111822945731, "compression_ratio": 1.618421052631579,
  "no_speech_prob": 0.0015619659097865224}, {"id": 427, "seek": 263248, "start": 2644.2400000000002,
  "end": 2652.96, "text": " you don''t need the vectors, but they are still the medium
  to get to your target. So, and so,", "tokens": [50952, 291, 500, 380, 643, 264,
  18875, 11, 457, 436, 366, 920, 264, 6399, 281, 483, 281, 428, 3779, 13, 407, 11,
  293, 370, 11, 51388], "temperature": 0.0, "avg_logprob": -0.2163111822945731, "compression_ratio":
  1.618421052631579, "no_speech_prob": 0.0015619659097865224}, {"id": 428, "seek":
  263248, "start": 2653.68, "end": 2658.64, "text": " but you''ve, I''ve seen the
  blog posts, which will also link, you''ve published on marks.io,", "tokens": [51424,
  457, 291, 600, 11, 286, 600, 1612, 264, 6968, 12300, 11, 597, 486, 611, 2113, 11,
  291, 600, 6572, 322, 10640, 13, 1004, 11, 51672], "temperature": 0.0, "avg_logprob":
  -0.2163111822945731, "compression_ratio": 1.618421052631579, "no_speech_prob": 0.0015619659097865224},
  {"id": 429, "seek": 265864, "start": 2659.2799999999997, "end": 2665.92, "text":
  " so discussing sort of almost like a unit, unit economy of this thing. Like, if
  I have MIT", "tokens": [50396, 370, 10850, 1333, 295, 1920, 411, 257, 4985, 11,
  4985, 5010, 295, 341, 551, 13, 1743, 11, 498, 286, 362, 13100, 50728], "temperature":
  0.0, "avg_logprob": -0.22191854964855107, "compression_ratio": 1.5701357466063348,
  "no_speech_prob": 0.012499794363975525}, {"id": 430, "seek": 265864, "start": 2666.7999999999997,
  "end": 2670.96, "text": " gazillion amount of servers, how it will play out, you
  know, how much", "tokens": [50772, 26232, 11836, 2372, 295, 15909, 11, 577, 309,
  486, 862, 484, 11, 291, 458, 11, 577, 709, 50980], "temperature": 0.0, "avg_logprob":
  -0.22191854964855107, "compression_ratio": 1.5701357466063348, "no_speech_prob":
  0.012499794363975525}, {"id": 431, "seek": 265864, "start": 2672.24, "end": 2677.8399999999997,
  "text": " separation of concern and also resource separation, all these things,
  and how economical it is", "tokens": [51044, 14634, 295, 3136, 293, 611, 7684, 14634,
  11, 439, 613, 721, 11, 293, 577, 42473, 309, 307, 51324], "temperature": 0.0, "avg_logprob":
  -0.22191854964855107, "compression_ratio": 1.5701357466063348, "no_speech_prob":
  0.012499794363975525}, {"id": 432, "seek": 265864, "start": 2678.4, "end": 2684.3199999999997,
  "text": " in the end. Is this something that you are proposing? So let''s say if
  somebody takes MIT and", "tokens": [51352, 294, 264, 917, 13, 1119, 341, 746, 300,
  291, 366, 29939, 30, 407, 718, 311, 584, 498, 2618, 2516, 13100, 293, 51648], "temperature":
  0.0, "avg_logprob": -0.22191854964855107, "compression_ratio": 1.5701357466063348,
  "no_speech_prob": 0.012499794363975525}, {"id": 433, "seek": 268432, "start": 2684.32,
  "end": 2690.2400000000002, "text": " wants to scale it, you know, like all of a
  sudden you get, instead of 10,000 documents, you get", "tokens": [50364, 2738, 281,
  4373, 309, 11, 291, 458, 11, 411, 439, 295, 257, 3990, 291, 483, 11, 2602, 295,
  1266, 11, 1360, 8512, 11, 291, 483, 50660], "temperature": 0.0, "avg_logprob": -0.13023217180941968,
  "compression_ratio": 1.5726141078838174, "no_speech_prob": 0.00242774304933846},
  {"id": 434, "seek": 268432, "start": 2690.2400000000002, "end": 2694.8, "text":
  " 10 million documents to process, right? Because somebody changed somewhere in
  the pipeline,", "tokens": [50660, 1266, 2459, 8512, 281, 1399, 11, 558, 30, 1436,
  2618, 3105, 4079, 294, 264, 15517, 11, 50888], "temperature": 0.0, "avg_logprob":
  -0.13023217180941968, "compression_ratio": 1.5726141078838174, "no_speech_prob":
  0.00242774304933846}, {"id": 435, "seek": 268432, "start": 2694.8, "end": 2700.56,
  "text": " and now we need to rerun the whole thing. So, how would you, what is your
  recommendation also", "tokens": [50888, 293, 586, 321, 643, 281, 43819, 409, 264,
  1379, 551, 13, 407, 11, 577, 576, 291, 11, 437, 307, 428, 11879, 611, 51176], "temperature":
  0.0, "avg_logprob": -0.13023217180941968, "compression_ratio": 1.5726141078838174,
  "no_speech_prob": 0.00242774304933846}, {"id": 436, "seek": 268432, "start": 2700.56,
  "end": 2709.52, "text": " on the economy side? How do you see MIT playing a role
  in making this huge thing more economical?", "tokens": [51176, 322, 264, 5010, 1252,
  30, 1012, 360, 291, 536, 13100, 2433, 257, 3090, 294, 1455, 341, 2603, 551, 544,
  42473, 30, 51624], "temperature": 0.0, "avg_logprob": -0.13023217180941968, "compression_ratio":
  1.5726141078838174, "no_speech_prob": 0.00242774304933846}, {"id": 437, "seek":
  270952, "start": 2709.92, "end": 2721.12, "text": " So, the first thing, the first
  thing that I see is that you can, you can calculate the cost ahead", "tokens": [50384,
  407, 11, 264, 700, 551, 11, 264, 700, 551, 300, 286, 536, 307, 300, 291, 393, 11,
  291, 393, 8873, 264, 2063, 2286, 50944], "temperature": 0.0, "avg_logprob": -0.1829650707733937,
  "compression_ratio": 1.5978260869565217, "no_speech_prob": 0.005748170427978039},
  {"id": 438, "seek": 270952, "start": 2721.12, "end": 2729.28, "text": " of time,
  because it''s absolutely linearly scalable, right? You take, so MIT itself sits
  on one CPU,", "tokens": [50944, 295, 565, 11, 570, 309, 311, 3122, 43586, 38481,
  11, 558, 30, 509, 747, 11, 370, 13100, 2564, 12696, 322, 472, 13199, 11, 51352],
  "temperature": 0.0, "avg_logprob": -0.1829650707733937, "compression_ratio": 1.5978260869565217,
  "no_speech_prob": 0.005748170427978039}, {"id": 439, "seek": 270952, "start": 2730.08,
  "end": 2735.12, "text": " right? It sits on one thread, I''ll even say a thread,
  because these days you have cores and CPUs", "tokens": [51392, 558, 30, 467, 12696,
  322, 472, 7207, 11, 286, 603, 754, 584, 257, 7207, 11, 570, 613, 1708, 291, 362,
  24826, 293, 13199, 82, 51644], "temperature": 0.0, "avg_logprob": -0.1829650707733937,
  "compression_ratio": 1.5978260869565217, "no_speech_prob": 0.005748170427978039},
  {"id": 440, "seek": 273512, "start": 2735.12, "end": 2741.8399999999997, "text":
  " and threads and it gets messed up. You can tell MIT to use multiple threads in
  certain situations", "tokens": [50364, 293, 19314, 293, 309, 2170, 16507, 493, 13,
  509, 393, 980, 13100, 281, 764, 3866, 19314, 294, 1629, 6851, 50700], "temperature":
  0.0, "avg_logprob": -0.19406892557059768, "compression_ratio": 1.7092198581560283,
  "no_speech_prob": 0.0006323584821075201}, {"id": 441, "seek": 273512, "start": 2741.8399999999997,
  "end": 2746.7999999999997, "text": " that you want to, but the example for bash
  processing that I use, which I actually learned from", "tokens": [50700, 300, 291,
  528, 281, 11, 457, 264, 1365, 337, 46183, 9007, 300, 286, 764, 11, 597, 286, 767,
  3264, 490, 50948], "temperature": 0.0, "avg_logprob": -0.19406892557059768, "compression_ratio":
  1.7092198581560283, "no_speech_prob": 0.0006323584821075201}, {"id": 442, "seek":
  273512, "start": 2746.7999999999997, "end": 2754.08, "text": " the VESPITE because
  they wrote an amazing blog post in, I think it was early January, they released
  a", "tokens": [50948, 264, 691, 2358, 47, 3927, 36, 570, 436, 4114, 364, 2243, 6968,
  2183, 294, 11, 286, 519, 309, 390, 2440, 7061, 11, 436, 4736, 257, 51312], "temperature":
  0.0, "avg_logprob": -0.19406892557059768, "compression_ratio": 1.7092198581560283,
  "no_speech_prob": 0.0006323584821075201}, {"id": 443, "seek": 273512, "start": 2754.08,
  "end": 2759.2799999999997, "text": " blog post talking about this exact problem
  of, you know, do you have one process across multiple", "tokens": [51312, 6968,
  2183, 1417, 466, 341, 1900, 1154, 295, 11, 291, 458, 11, 360, 291, 362, 472, 1399,
  2108, 3866, 51572], "temperature": 0.0, "avg_logprob": -0.19406892557059768, "compression_ratio":
  1.7092198581560283, "no_speech_prob": 0.0006323584821075201}, {"id": 444, "seek":
  273512, "start": 2759.2799999999997, "end": 2764.24, "text": " threads? Do you have
  multiple processes? So, if you go with the multiple processes route,", "tokens":
  [51572, 19314, 30, 1144, 291, 362, 3866, 7555, 30, 407, 11, 498, 291, 352, 365,
  264, 3866, 7555, 7955, 11, 51820], "temperature": 0.0, "avg_logprob": -0.19406892557059768,
  "compression_ratio": 1.7092198581560283, "no_speech_prob": 0.0006323584821075201},
  {"id": 445, "seek": 276512, "start": 2765.2799999999997, "end": 2775.52, "text":
  " let''s say I take, I take a bunch of documents and I pass them in and I have some
  level of consistency", "tokens": [50372, 718, 311, 584, 286, 747, 11, 286, 747,
  257, 3840, 295, 8512, 293, 286, 1320, 552, 294, 293, 286, 362, 512, 1496, 295, 14416,
  50884], "temperature": 0.0, "avg_logprob": -0.17621022179013207, "compression_ratio":
  1.751111111111111, "no_speech_prob": 0.0031097624450922012}, {"id": 446, "seek":
  276512, "start": 2775.52, "end": 2782.56, "text": " in the document size, which
  you usually do. Pass them in and it takes you X as long, it takes you", "tokens":
  [50884, 294, 264, 4166, 2744, 11, 597, 291, 2673, 360, 13, 10319, 552, 294, 293,
  309, 2516, 291, 1783, 382, 938, 11, 309, 2516, 291, 51236], "temperature": 0.0,
  "avg_logprob": -0.17621022179013207, "compression_ratio": 1.751111111111111, "no_speech_prob":
  0.0031097624450922012}, {"id": 447, "seek": 276512, "start": 2782.56, "end": 2787.8399999999997,
  "text": " X to get all of your documents, inference, right? So, you have that number
  and you know how long it", "tokens": [51236, 1783, 281, 483, 439, 295, 428, 8512,
  11, 38253, 11, 558, 30, 407, 11, 291, 362, 300, 1230, 293, 291, 458, 577, 938, 309,
  51500], "temperature": 0.0, "avg_logprob": -0.17621022179013207, "compression_ratio":
  1.751111111111111, "no_speech_prob": 0.0031097624450922012}, {"id": 448, "seek":
  276512, "start": 2787.8399999999997, "end": 2794.16, "text": " took and you know
  how much, how much content you processed in terms of bytes. Well, what if I,", "tokens":
  [51500, 1890, 293, 291, 458, 577, 709, 11, 577, 709, 2701, 291, 18846, 294, 2115,
  295, 36088, 13, 1042, 11, 437, 498, 286, 11, 51816], "temperature": 0.0, "avg_logprob":
  -0.17621022179013207, "compression_ratio": 1.751111111111111, "no_speech_prob":
  0.0031097624450922012}, {"id": 449, "seek": 279416, "start": 2794.16, "end": 2800.3999999999996,
  "text": " if I add, if I add another process now and I''m doing this purely paralyzeable,
  so half of my documents", "tokens": [50364, 498, 286, 909, 11, 498, 286, 909, 1071,
  1399, 586, 293, 286, 478, 884, 341, 17491, 32645, 1381, 712, 11, 370, 1922, 295,
  452, 8512, 50676], "temperature": 0.0, "avg_logprob": -0.1267544315979544, "compression_ratio":
  1.6652542372881356, "no_speech_prob": 0.0006732585607096553}, {"id": 450, "seek":
  279416, "start": 2800.3999999999996, "end": 2806.16, "text": " go here, half of
  my documents go there, it''s what I said exactly is linearly scalable. I add a CPU,",
  "tokens": [50676, 352, 510, 11, 1922, 295, 452, 8512, 352, 456, 11, 309, 311, 437,
  286, 848, 2293, 307, 43586, 38481, 13, 286, 909, 257, 13199, 11, 50964], "temperature":
  0.0, "avg_logprob": -0.1267544315979544, "compression_ratio": 1.6652542372881356,
  "no_speech_prob": 0.0006732585607096553}, {"id": 451, "seek": 279416, "start": 2806.7999999999997,
  "end": 2815.7599999999998, "text": " it has the time, right? It has the time that
  it takes to do this. So, if I have a situation where", "tokens": [50996, 309, 575,
  264, 565, 11, 558, 30, 467, 575, 264, 565, 300, 309, 2516, 281, 360, 341, 13, 407,
  11, 498, 286, 362, 257, 2590, 689, 51444], "temperature": 0.0, "avg_logprob": -0.1267544315979544,
  "compression_ratio": 1.6652542372881356, "no_speech_prob": 0.0006732585607096553},
  {"id": 452, "seek": 279416, "start": 2815.7599999999998, "end": 2821.44, "text":
  " I''ve said, okay, I did 10,000 documents, it took me X, now I have to do a million
  documents.", "tokens": [51444, 286, 600, 848, 11, 1392, 11, 286, 630, 1266, 11,
  1360, 8512, 11, 309, 1890, 385, 1783, 11, 586, 286, 362, 281, 360, 257, 2459, 8512,
  13, 51728], "temperature": 0.0, "avg_logprob": -0.1267544315979544, "compression_ratio":
  1.6652542372881356, "no_speech_prob": 0.0006732585607096553}, {"id": 453, "seek":
  282144, "start": 2822.0, "end": 2828.32, "text": " How long do I want it to take?
  You can actually write down the calculation and say, I need,", "tokens": [50392,
  1012, 938, 360, 286, 528, 309, 281, 747, 30, 509, 393, 767, 2464, 760, 264, 17108,
  293, 584, 11, 286, 643, 11, 50708], "temperature": 0.0, "avg_logprob": -0.15547142406501394,
  "compression_ratio": 1.5756302521008403, "no_speech_prob": 0.006124628242105246},
  {"id": 454, "seek": 282144, "start": 2828.32, "end": 2833.2000000000003, "text":
  " I need this exact infrastructure, which is a huge problem right now, a lot of
  people don''t know that.", "tokens": [50708, 286, 643, 341, 1900, 6896, 11, 597,
  307, 257, 2603, 1154, 558, 586, 11, 257, 688, 295, 561, 500, 380, 458, 300, 13,
  50952], "temperature": 0.0, "avg_logprob": -0.15547142406501394, "compression_ratio":
  1.5756302521008403, "no_speech_prob": 0.006124628242105246}, {"id": 455, "seek":
  282144, "start": 2833.2000000000003, "end": 2839.52, "text": " It''s like, okay,
  let''s just add a lot of GPUs and see what happens, you know. You can, you can spend",
  "tokens": [50952, 467, 311, 411, 11, 1392, 11, 718, 311, 445, 909, 257, 688, 295,
  18407, 82, 293, 536, 437, 2314, 11, 291, 458, 13, 509, 393, 11, 291, 393, 3496,
  51268], "temperature": 0.0, "avg_logprob": -0.15547142406501394, "compression_ratio":
  1.5756302521008403, "no_speech_prob": 0.006124628242105246}, {"id": 456, "seek":
  282144, "start": 2839.52, "end": 2845.2000000000003, "text": " the time to go through
  and do that calculation, but it''s not so straightforward.", "tokens": [51268, 264,
  565, 281, 352, 807, 293, 360, 300, 17108, 11, 457, 309, 311, 406, 370, 15325, 13,
  51552], "temperature": 0.0, "avg_logprob": -0.15547142406501394, "compression_ratio":
  1.5756302521008403, "no_speech_prob": 0.006124628242105246}, {"id": 457, "seek":
  284520, "start": 2845.8399999999997, "end": 2854.3999999999996, "text": " And you''d
  have to do it like, you''d have to cost it yourself. I haven''t released it, but
  I want", "tokens": [50396, 400, 291, 1116, 362, 281, 360, 309, 411, 11, 291, 1116,
  362, 281, 2063, 309, 1803, 13, 286, 2378, 380, 4736, 309, 11, 457, 286, 528, 50824],
  "temperature": 0.0, "avg_logprob": -0.1919794630730289, "compression_ratio": 1.5891891891891892,
  "no_speech_prob": 0.031021952629089355}, {"id": 458, "seek": 284520, "start": 2854.3999999999996,
  "end": 2859.2799999999997, "text": " to have a calculator that says, how many bytes
  do you have and, you know, how long do you want to spend?", "tokens": [50824, 281,
  362, 257, 24993, 300, 1619, 11, 577, 867, 36088, 360, 291, 362, 293, 11, 291, 458,
  11, 577, 938, 360, 291, 528, 281, 3496, 30, 51068], "temperature": 0.0, "avg_logprob":
  -0.1919794630730289, "compression_ratio": 1.5891891891891892, "no_speech_prob":
  0.031021952629089355}, {"id": 459, "seek": 284520, "start": 2859.2799999999997,
  "end": 2869.68, "text": " And I can say, well, it''ll cost you this in Amazon or
  whatever. So, that''s, that''s one thing.", "tokens": [51068, 400, 286, 393, 584,
  11, 731, 11, 309, 603, 2063, 291, 341, 294, 6795, 420, 2035, 13, 407, 11, 300, 311,
  11, 300, 311, 472, 551, 13, 51588], "temperature": 0.0, "avg_logprob": -0.1919794630730289,
  "compression_ratio": 1.5891891891891892, "no_speech_prob": 0.031021952629089355},
  {"id": 460, "seek": 286968, "start": 2870.3999999999996, "end": 2877.6, "text":
  " I also want it so, I mentioned GPUs, it''s like, this is, I built it so it works
  on CPU.", "tokens": [50400, 286, 611, 528, 309, 370, 11, 286, 2835, 18407, 82, 11,
  309, 311, 411, 11, 341, 307, 11, 286, 3094, 309, 370, 309, 1985, 322, 13199, 13,
  50760], "temperature": 0.0, "avg_logprob": -0.24736902848729547, "compression_ratio":
  1.6299559471365639, "no_speech_prob": 0.0028566857799887657}, {"id": 461, "seek":
  286968, "start": 2878.56, "end": 2885.2799999999997, "text": " If you are a company
  that''s getting into this stuff and this, this, this idea of the", "tokens": [50808,
  759, 291, 366, 257, 2237, 300, 311, 1242, 666, 341, 1507, 293, 341, 11, 341, 11,
  341, 1558, 295, 264, 51144], "temperature": 0.0, "avg_logprob": -0.24736902848729547,
  "compression_ratio": 1.6299559471365639, "no_speech_prob": 0.0028566857799887657},
  {"id": 462, "seek": 286968, "start": 2885.2799999999997, "end": 2890.8799999999997,
  "text": " unit economy, like, how long does it take to process something? And what''s
  the cost and, you know,", "tokens": [51144, 4985, 5010, 11, 411, 11, 577, 938, 775,
  309, 747, 281, 1399, 746, 30, 400, 437, 311, 264, 2063, 293, 11, 291, 458, 11, 51424],
  "temperature": 0.0, "avg_logprob": -0.24736902848729547, "compression_ratio": 1.6299559471365639,
  "no_speech_prob": 0.0028566857799887657}, {"id": 463, "seek": 286968, "start": 2890.8799999999997,
  "end": 2896.3999999999996, "text": " how do I scale it? But the, the, the, the billion
  documents. If I''m coming into this ecosystem and", "tokens": [51424, 577, 360,
  286, 4373, 309, 30, 583, 264, 11, 264, 11, 264, 11, 264, 5218, 8512, 13, 759, 286,
  478, 1348, 666, 341, 11311, 293, 51700], "temperature": 0.0, "avg_logprob": -0.24736902848729547,
  "compression_ratio": 1.6299559471365639, "no_speech_prob": 0.0028566857799887657},
  {"id": 464, "seek": 289640, "start": 2896.4, "end": 2903.44, "text": " content processing,
  and I''m used to working in Java or, you know, C sharp or something like that.",
  "tokens": [50364, 2701, 9007, 11, 293, 286, 478, 1143, 281, 1364, 294, 10745, 420,
  11, 291, 458, 11, 383, 8199, 420, 746, 411, 300, 13, 50716], "temperature": 0.0,
  "avg_logprob": -0.17613258018149985, "compression_ratio": 1.560483870967742, "no_speech_prob":
  0.0010718363337218761}, {"id": 465, "seek": 289640, "start": 2905.12, "end": 2909.6800000000003,
  "text": " Now you''re telling me I need to buy GPUs, like I have to run GPUs, and
  then I go check the prices,", "tokens": [50800, 823, 291, 434, 3585, 385, 286, 643,
  281, 2256, 18407, 82, 11, 411, 286, 362, 281, 1190, 18407, 82, 11, 293, 550, 286,
  352, 1520, 264, 7901, 11, 51028], "temperature": 0.0, "avg_logprob": -0.17613258018149985,
  "compression_ratio": 1.560483870967742, "no_speech_prob": 0.0010718363337218761},
  {"id": 466, "seek": 289640, "start": 2909.6800000000003, "end": 2914.8, "text":
  " I''m like, well, that''s not how much we spend on infrastructure. That''s not
  in our budget. I''m", "tokens": [51028, 286, 478, 411, 11, 731, 11, 300, 311, 406,
  577, 709, 321, 3496, 322, 6896, 13, 663, 311, 406, 294, 527, 4706, 13, 286, 478,
  51284], "temperature": 0.0, "avg_logprob": -0.17613258018149985, "compression_ratio":
  1.560483870967742, "no_speech_prob": 0.0010718363337218761}, {"id": 467, "seek":
  289640, "start": 2914.8, "end": 2920.8, "text": " sorry to tell you. So maybe we
  can''t even do this. So I wanted to have a way where you could get", "tokens": [51284,
  2597, 281, 980, 291, 13, 407, 1310, 321, 393, 380, 754, 360, 341, 13, 407, 286,
  1415, 281, 362, 257, 636, 689, 291, 727, 483, 51584], "temperature": 0.0, "avg_logprob":
  -0.17613258018149985, "compression_ratio": 1.560483870967742, "no_speech_prob":
  0.0010718363337218761}, {"id": 468, "seek": 292080, "start": 2920.8, "end": 2925.84,
  "text": " around that problem where you could just use CPU and it''s a straightforward
  understanding of the cost", "tokens": [50364, 926, 300, 1154, 689, 291, 727, 445,
  764, 13199, 293, 309, 311, 257, 15325, 3701, 295, 264, 2063, 50616], "temperature":
  0.0, "avg_logprob": -0.2150675045546665, "compression_ratio": 1.615702479338843,
  "no_speech_prob": 0.001631997642107308}, {"id": 469, "seek": 292080, "start": 2927.04,
  "end": 2933.6800000000003, "text": " that you''d have to put in. I haven''t checked
  Amazon, I haven''t checked Amazon prices in a little while,", "tokens": [50676,
  300, 291, 1116, 362, 281, 829, 294, 13, 286, 2378, 380, 10033, 6795, 11, 286, 2378,
  380, 10033, 6795, 7901, 294, 257, 707, 1339, 11, 51008], "temperature": 0.0, "avg_logprob":
  -0.2150675045546665, "compression_ratio": 1.615702479338843, "no_speech_prob": 0.001631997642107308},
  {"id": 470, "seek": 292080, "start": 2933.6800000000003, "end": 2941.52, "text":
  " but I might as well be posted online, which is, which is another cloud platform.
  I just, the pricing", "tokens": [51008, 457, 286, 1062, 382, 731, 312, 9437, 2950,
  11, 597, 307, 11, 597, 307, 1071, 4588, 3663, 13, 286, 445, 11, 264, 17621, 51400],
  "temperature": 0.0, "avg_logprob": -0.2150675045546665, "compression_ratio": 1.615702479338843,
  "no_speech_prob": 0.001631997642107308}, {"id": 471, "seek": 292080, "start": 2941.52,
  "end": 2950.0, "text": " is better and I just, like, they were actually recently
  purchased by a huge content,", "tokens": [51400, 307, 1101, 293, 286, 445, 11, 411,
  11, 436, 645, 767, 3938, 14734, 538, 257, 2603, 2701, 11, 51824], "temperature":
  0.0, "avg_logprob": -0.2150675045546665, "compression_ratio": 1.615702479338843,
  "no_speech_prob": 0.001631997642107308}, {"id": 472, "seek": 295080, "start": 2951.2000000000003,
  "end": 2957.52, "text": " management system, uh, it starts with an, I forget the
  name, whatever. Anyway, I use line-out and", "tokens": [50384, 4592, 1185, 11, 2232,
  11, 309, 3719, 365, 364, 11, 286, 2870, 264, 1315, 11, 2035, 13, 5684, 11, 286,
  764, 1622, 12, 346, 293, 50700], "temperature": 0.0, "avg_logprob": -0.22877515709918478,
  "compression_ratio": 1.5646551724137931, "no_speech_prob": 0.0037144243251532316},
  {"id": 473, "seek": 295080, "start": 2957.52, "end": 2963.6800000000003, "text":
  " it''s, uh, it''s, it''s cheap for CPUs. Like, it''s great, but you want to, you
  want to run a GPU,", "tokens": [50700, 309, 311, 11, 2232, 11, 309, 311, 11, 309,
  311, 7084, 337, 13199, 82, 13, 1743, 11, 309, 311, 869, 11, 457, 291, 528, 281,
  11, 291, 528, 281, 1190, 257, 18407, 11, 51008], "temperature": 0.0, "avg_logprob":
  -0.22877515709918478, "compression_ratio": 1.5646551724137931, "no_speech_prob":
  0.0037144243251532316}, {"id": 474, "seek": 295080, "start": 2963.6800000000003,
  "end": 2970.5600000000004, "text": " it''s like $500 a month or $1,000 a month.
  And that''s a lot of money for one machine,", "tokens": [51008, 309, 311, 411, 1848,
  7526, 257, 1618, 420, 1848, 16, 11, 1360, 257, 1618, 13, 400, 300, 311, 257, 688,
  295, 1460, 337, 472, 3479, 11, 51352], "temperature": 0.0, "avg_logprob": -0.22877515709918478,
  "compression_ratio": 1.5646551724137931, "no_speech_prob": 0.0037144243251532316},
  {"id": 475, "seek": 295080, "start": 2970.5600000000004, "end": 2976.96, "text":
  " and most teams are not willing to spend that. If you want to do fractional, you
  know,", "tokens": [51352, 293, 881, 5491, 366, 406, 4950, 281, 3496, 300, 13, 759,
  291, 528, 281, 360, 17948, 1966, 11, 291, 458, 11, 51672], "temperature": 0.0, "avg_logprob":
  -0.22877515709918478, "compression_ratio": 1.5646551724137931, "no_speech_prob":
  0.0037144243251532316}, {"id": 476, "seek": 297696, "start": 2976.96, "end": 2984.32,
  "text": " on AWS is probably for actionable GPUs, I think, but it''s still expensive.
  And now you''re, now,", "tokens": [50364, 322, 17650, 307, 1391, 337, 45098, 18407,
  82, 11, 286, 519, 11, 457, 309, 311, 920, 5124, 13, 400, 586, 291, 434, 11, 586,
  11, 50732], "temperature": 0.0, "avg_logprob": -0.19726796735797011, "compression_ratio":
  1.5932203389830508, "no_speech_prob": 0.001627921941690147}, {"id": 477, "seek":
  297696, "start": 2985.6, "end": 2989.92, "text": " it''s like this cost that never
  goes away. Like, once you do it, it''s like, well, it''s there,", "tokens": [50796,
  309, 311, 411, 341, 2063, 300, 1128, 1709, 1314, 13, 1743, 11, 1564, 291, 360, 309,
  11, 309, 311, 411, 11, 731, 11, 309, 311, 456, 11, 51012], "temperature": 0.0, "avg_logprob":
  -0.19726796735797011, "compression_ratio": 1.5932203389830508, "no_speech_prob":
  0.001627921941690147}, {"id": 478, "seek": 297696, "start": 2989.92, "end": 2996.8,
  "text": " it''s there for a long time, you know, CPUs are a commodity. Um, GPUs,
  you have to fight with the,", "tokens": [51012, 309, 311, 456, 337, 257, 938, 565,
  11, 291, 458, 11, 13199, 82, 366, 257, 29125, 13, 3301, 11, 18407, 82, 11, 291,
  362, 281, 2092, 365, 264, 11, 51356], "temperature": 0.0, "avg_logprob": -0.19726796735797011,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.001627921941690147},
  {"id": 479, "seek": 297696, "start": 2996.8, "end": 3005.2, "text": " with the cryptocurrency
  crowd for the costs, all this stuff. So, yes, CPUs the way to go.", "tokens": [51356,
  365, 264, 28809, 6919, 337, 264, 5497, 11, 439, 341, 1507, 13, 407, 11, 2086, 11,
  13199, 82, 264, 636, 281, 352, 13, 51776], "temperature": 0.0, "avg_logprob": -0.19726796735797011,
  "compression_ratio": 1.5932203389830508, "no_speech_prob": 0.001627921941690147},
  {"id": 480, "seek": 300520, "start": 3005.4399999999996, "end": 3011.7599999999998,
  "text": " I can imagine that GPUs can be used during the model training or fine
  tuning, but during serving,", "tokens": [50376, 286, 393, 3811, 300, 18407, 82,
  393, 312, 1143, 1830, 264, 2316, 3097, 420, 2489, 15164, 11, 457, 1830, 8148, 11,
  50692], "temperature": 0.0, "avg_logprob": -0.1661984776876059, "compression_ratio":
  1.5, "no_speech_prob": 0.005041016731411219}, {"id": 481, "seek": 300520, "start":
  3011.7599999999998, "end": 3020.0, "text": " that sounds way too expensive. Right.
  Yeah, yeah, that makes a lot of sense. And, um, and so,", "tokens": [50692, 300,
  3263, 636, 886, 5124, 13, 1779, 13, 865, 11, 1338, 11, 300, 1669, 257, 688, 295,
  2020, 13, 400, 11, 1105, 11, 293, 370, 11, 51104], "temperature": 0.0, "avg_logprob":
  -0.1661984776876059, "compression_ratio": 1.5, "no_speech_prob": 0.005041016731411219},
  {"id": 482, "seek": 300520, "start": 3021.04, "end": 3028.08, "text": " now when
  you offer my, how exactly you offer it, it''s, it''s a binary package, right, uh,
  that I can", "tokens": [51156, 586, 562, 291, 2626, 452, 11, 577, 2293, 291, 2626,
  309, 11, 309, 311, 11, 309, 311, 257, 17434, 7372, 11, 558, 11, 2232, 11, 300, 286,
  393, 51508], "temperature": 0.0, "avg_logprob": -0.1661984776876059, "compression_ratio":
  1.5, "no_speech_prob": 0.005041016731411219}, {"id": 483, "seek": 302808, "start":
  3028.08, "end": 3035.44, "text": " install and, and, and basically run on my, on
  my system, and I can decide whether it will be like,", "tokens": [50364, 3625, 293,
  11, 293, 11, 293, 1936, 1190, 322, 452, 11, 322, 452, 1185, 11, 293, 286, 393, 4536,
  1968, 309, 486, 312, 411, 11, 50732], "temperature": 0.0, "avg_logprob": -0.21533725788066913,
  "compression_ratio": 1.5245901639344261, "no_speech_prob": 0.004794891923666}, {"id":
  484, "seek": 302808, "start": 3035.44, "end": 3042.0, "text": " a standalone kind
  of script or it will be a pod in Kubernetes or Docker image and some other", "tokens":
  [50732, 257, 37454, 733, 295, 5755, 420, 309, 486, 312, 257, 2497, 294, 23145, 420,
  33772, 3256, 293, 512, 661, 51060], "temperature": 0.0, "avg_logprob": -0.21533725788066913,
  "compression_ratio": 1.5245901639344261, "no_speech_prob": 0.004794891923666}, {"id":
  485, "seek": 302808, "start": 3043.12, "end": 3051.52, "text": " non Kubernetes.
  Um, so is that right? That''s right. It''s, it''s a very small executable.", "tokens":
  [51116, 2107, 23145, 13, 3301, 11, 370, 307, 300, 558, 30, 663, 311, 558, 13, 467,
  311, 11, 309, 311, 257, 588, 1359, 7568, 712, 13, 51536], "temperature": 0.0, "avg_logprob":
  -0.21533725788066913, "compression_ratio": 1.5245901639344261, "no_speech_prob":
  0.004794891923666}, {"id": 486, "seek": 305152, "start": 3051.52, "end": 3061.28,
  "text": " Um, it''s, it''s so Linux is a first class citizen. Um, Windows is, it''ll
  run on Windows. It''ll run on", "tokens": [50364, 3301, 11, 309, 311, 11, 309, 311,
  370, 18734, 307, 257, 700, 1508, 13326, 13, 3301, 11, 8591, 307, 11, 309, 603, 1190,
  322, 8591, 13, 467, 603, 1190, 322, 50852], "temperature": 0.0, "avg_logprob": -0.16736780014713254,
  "compression_ratio": 1.5983935742971886, "no_speech_prob": 0.003780386410653591},
  {"id": 487, "seek": 305152, "start": 3061.28, "end": 3067.6, "text": " Mac, but
  I''ve heard people running it on Mac M1, but they had to like do a lot of stuff
  to like", "tokens": [50852, 5707, 11, 457, 286, 600, 2198, 561, 2614, 309, 322,
  5707, 376, 16, 11, 457, 436, 632, 281, 411, 360, 257, 688, 295, 1507, 281, 411,
  51168], "temperature": 0.0, "avg_logprob": -0.16736780014713254, "compression_ratio":
  1.5983935742971886, "no_speech_prob": 0.003780386410653591}, {"id": 488, "seek":
  305152, "start": 3067.6, "end": 3072.08, "text": " fix dependencies and it wasn''t
  really working that well. And I think what, what''s it called Rosetta", "tokens":
  [51168, 3191, 36606, 293, 309, 2067, 380, 534, 1364, 300, 731, 13, 400, 286, 519,
  437, 11, 437, 311, 309, 1219, 11144, 16593, 51392], "temperature": 0.0, "avg_logprob":
  -0.16736780014713254, "compression_ratio": 1.5983935742971886, "no_speech_prob":
  0.003780386410653591}, {"id": 489, "seek": 305152, "start": 3072.08, "end": 3078.72,
  "text": " or something? I think it''s still using that like to, to do the X86 like
  bridge, like the translation,", "tokens": [51392, 420, 746, 30, 286, 519, 309, 311,
  920, 1228, 300, 411, 281, 11, 281, 360, 264, 1783, 22193, 411, 7283, 11, 411, 264,
  12853, 11, 51724], "temperature": 0.0, "avg_logprob": -0.16736780014713254, "compression_ratio":
  1.5983935742971886, "no_speech_prob": 0.003780386410653591}, {"id": 490, "seek":
  307872, "start": 3078.72, "end": 3084.7999999999997, "text": " visualization. Um,
  so Mac M1, it''s not, uh, I wouldn''t consider it working. I''ve also seen some",
  "tokens": [50364, 25801, 13, 3301, 11, 370, 5707, 376, 16, 11, 309, 311, 406, 11,
  2232, 11, 286, 2759, 380, 1949, 309, 1364, 13, 286, 600, 611, 1612, 512, 50668],
  "temperature": 0.0, "avg_logprob": -0.15476605491916628, "compression_ratio": 1.696969696969697,
  "no_speech_prob": 0.002198495902121067}, {"id": 491, "seek": 307872, "start": 3084.7999999999997,
  "end": 3089.12, "text": " other problems on, on Mac that I''m trying to resolve.
  It works fine, works on my machine, right,", "tokens": [50668, 661, 2740, 322, 11,
  322, 5707, 300, 286, 478, 1382, 281, 14151, 13, 467, 1985, 2489, 11, 1985, 322,
  452, 3479, 11, 558, 11, 50884], "temperature": 0.0, "avg_logprob": -0.15476605491916628,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.002198495902121067},
  {"id": 492, "seek": 307872, "start": 3089.12, "end": 3092.9599999999996, "text":
  " that, that type of thing, but really it''s meant to be running links. Um, you
  can run it in Docker.", "tokens": [50884, 300, 11, 300, 2010, 295, 551, 11, 457,
  534, 309, 311, 4140, 281, 312, 2614, 6123, 13, 3301, 11, 291, 393, 1190, 309, 294,
  33772, 13, 51076], "temperature": 0.0, "avg_logprob": -0.15476605491916628, "compression_ratio":
  1.696969696969697, "no_speech_prob": 0.002198495902121067}, {"id": 493, "seek":
  307872, "start": 3092.9599999999996, "end": 3097.68, "text": " It''s really easy
  to get started in Docker. Uh, so you can download the executable and run it on your",
  "tokens": [51076, 467, 311, 534, 1858, 281, 483, 1409, 294, 33772, 13, 4019, 11,
  370, 291, 393, 5484, 264, 7568, 712, 293, 1190, 309, 322, 428, 51312], "temperature":
  0.0, "avg_logprob": -0.15476605491916628, "compression_ratio": 1.696969696969697,
  "no_speech_prob": 0.002198495902121067}, {"id": 494, "seek": 307872, "start": 3097.68,
  "end": 3103.52, "text": " Mac, um, or you can just download the Docker and use that,
  which is probably a little bit more straightforward.", "tokens": [51312, 5707, 11,
  1105, 11, 420, 291, 393, 445, 5484, 264, 33772, 293, 764, 300, 11, 597, 307, 1391,
  257, 707, 857, 544, 15325, 13, 51604], "temperature": 0.0, "avg_logprob": -0.15476605491916628,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.002198495902121067},
  {"id": 495, "seek": 310352, "start": 3104.48, "end": 3109.6, "text": " Um, then
  you don''t have to worry about other dependencies. Uh, with Linux, I don''t, if
  you''re running it", "tokens": [50412, 3301, 11, 550, 291, 500, 380, 362, 281, 3292,
  466, 661, 36606, 13, 4019, 11, 365, 18734, 11, 286, 500, 380, 11, 498, 291, 434,
  2614, 309, 50668], "temperature": 0.0, "avg_logprob": -0.1407222897987666, "compression_ratio":
  1.6971830985915493, "no_speech_prob": 0.0024130267556756735}, {"id": 496, "seek":
  310352, "start": 3110.08, "end": 3115.28, "text": " on, uh, on Linux machines, you
  can use the Docker if you''re doing like Kubernetes and that stuff.", "tokens":
  [50692, 322, 11, 2232, 11, 322, 18734, 8379, 11, 291, 393, 764, 264, 33772, 498,
  291, 434, 884, 411, 23145, 293, 300, 1507, 13, 50952], "temperature": 0.0, "avg_logprob":
  -0.1407222897987666, "compression_ratio": 1.6971830985915493, "no_speech_prob":
  0.0024130267556756735}, {"id": 497, "seek": 310352, "start": 3115.28, "end": 3122.4,
  "text": " Great. Run it in Docker. Um, just make sure that you sort out like in
  your pod or whatever,", "tokens": [50952, 3769, 13, 8950, 309, 294, 33772, 13, 3301,
  11, 445, 652, 988, 300, 291, 1333, 484, 411, 294, 428, 2497, 420, 2035, 11, 51308],
  "temperature": 0.0, "avg_logprob": -0.1407222897987666, "compression_ratio": 1.6971830985915493,
  "no_speech_prob": 0.0024130267556756735}, {"id": 498, "seek": 310352, "start": 3122.4,
  "end": 3127.68, "text": " like how much compute you''re actually giving it. Um,
  because model inference doesn''t,", "tokens": [51308, 411, 577, 709, 14722, 291,
  434, 767, 2902, 309, 13, 3301, 11, 570, 2316, 38253, 1177, 380, 11, 51572], "temperature":
  0.0, "avg_logprob": -0.1407222897987666, "compression_ratio": 1.6971830985915493,
  "no_speech_prob": 0.0024130267556756735}, {"id": 499, "seek": 310352, "start": 3127.68,
  "end": 3131.92, "text": " it''s not just a mighty. It''s like all model inference
  is really, really heavy. It''s really expensive.", "tokens": [51572, 309, 311, 406,
  445, 257, 21556, 13, 467, 311, 411, 439, 2316, 38253, 307, 534, 11, 534, 4676, 13,
  467, 311, 534, 5124, 13, 51784], "temperature": 0.0, "avg_logprob": -0.1407222897987666,
  "compression_ratio": 1.6971830985915493, "no_speech_prob": 0.0024130267556756735},
  {"id": 500, "seek": 313192, "start": 3131.92, "end": 3137.2000000000003, "text":
  " It wants a lot of, wants a lot of compute, not so much memory, but compute.",
  "tokens": [50364, 467, 2738, 257, 688, 295, 11, 2738, 257, 688, 295, 14722, 11,
  406, 370, 709, 4675, 11, 457, 14722, 13, 50628], "temperature": 0.0, "avg_logprob":
  -0.1825498100218734, "compression_ratio": 1.6345381526104417, "no_speech_prob":
  0.0004321828600950539}, {"id": 501, "seek": 313192, "start": 3137.76, "end": 3144.08,
  "text": " So just be sure to give it enough, um, to satisfy your needs and do time.
  I haven''t done Kubernetes test myself.", "tokens": [50656, 407, 445, 312, 988,
  281, 976, 309, 1547, 11, 1105, 11, 281, 19319, 428, 2203, 293, 360, 565, 13, 286,
  2378, 380, 1096, 23145, 1500, 2059, 13, 50972], "temperature": 0.0, "avg_logprob":
  -0.1825498100218734, "compression_ratio": 1.6345381526104417, "no_speech_prob":
  0.0004321828600950539}, {"id": 502, "seek": 313192, "start": 3145.2000000000003,
  "end": 3153.76, "text": " Uh, but I like to run, I''m, I''m old school. Like this
  whole Docker thing. Yeah. Okay. I''ll, uh, I''ll make a Docker file.", "tokens":
  [51028, 4019, 11, 457, 286, 411, 281, 1190, 11, 286, 478, 11, 286, 478, 1331, 1395,
  13, 1743, 341, 1379, 33772, 551, 13, 865, 13, 1033, 13, 286, 603, 11, 2232, 11,
  286, 603, 652, 257, 33772, 3991, 13, 51456], "temperature": 0.0, "avg_logprob":
  -0.1825498100218734, "compression_ratio": 1.6345381526104417, "no_speech_prob":
  0.0004321828600950539}, {"id": 503, "seek": 313192, "start": 3153.76, "end": 3158.96,
  "text": " Sure. You can use it in Docker. Um, it''s on the Docker hub. Uh, but I
  like to just install stuff.", "tokens": [51456, 4894, 13, 509, 393, 764, 309, 294,
  33772, 13, 3301, 11, 309, 311, 322, 264, 33772, 11838, 13, 4019, 11, 457, 286, 411,
  281, 445, 3625, 1507, 13, 51716], "temperature": 0.0, "avg_logprob": -0.1825498100218734,
  "compression_ratio": 1.6345381526104417, "no_speech_prob": 0.0004321828600950539},
  {"id": 504, "seek": 315896, "start": 3159.04, "end": 3164.08, "text": " The old
  fashioned way. Uh, in Ubuntu, I just, you know, download the download the thing.",
  "tokens": [50368, 440, 1331, 40646, 636, 13, 4019, 11, 294, 30230, 45605, 11, 286,
  445, 11, 291, 458, 11, 5484, 264, 5484, 264, 551, 13, 50620], "temperature": 0.0,
  "avg_logprob": -0.21900687073216293, "compression_ratio": 1.7983870967741935, "no_speech_prob":
  0.0019972093869000673}, {"id": 505, "seek": 315896, "start": 3164.08, "end": 3171.28,
  "text": " It''s a tarball and you, you know, it''s at the tarball and you''re good
  to go. Uh, and, uh, the way you", "tokens": [50620, 467, 311, 257, 3112, 3129, 293,
  291, 11, 291, 458, 11, 309, 311, 412, 264, 3112, 3129, 293, 291, 434, 665, 281,
  352, 13, 4019, 11, 293, 11, 2232, 11, 264, 636, 291, 50980], "temperature": 0.0,
  "avg_logprob": -0.21900687073216293, "compression_ratio": 1.7983870967741935, "no_speech_prob":
  0.0019972093869000673}, {"id": 506, "seek": 315896, "start": 3171.28, "end": 3176.2400000000002,
  "text": " start it is actually, it''s a, it''s a rest program with a, with a library
  dependency, which is on", "tokens": [50980, 722, 309, 307, 767, 11, 309, 311, 257,
  11, 309, 311, 257, 1472, 1461, 365, 257, 11, 365, 257, 6405, 33621, 11, 597, 307,
  322, 51228], "temperature": 0.0, "avg_logprob": -0.21900687073216293, "compression_ratio":
  1.7983870967741935, "no_speech_prob": 0.0019972093869000673}, {"id": 507, "seek":
  315896, "start": 3176.2400000000002, "end": 3180.56, "text": " extra one time. Um,
  because it''s dynamically linked. It''s not statically linked.", "tokens": [51228,
  2857, 472, 565, 13, 3301, 11, 570, 309, 311, 43492, 9408, 13, 467, 311, 406, 2219,
  984, 9408, 13, 51444], "temperature": 0.0, "avg_logprob": -0.21900687073216293,
  "compression_ratio": 1.7983870967741935, "no_speech_prob": 0.0019972093869000673},
  {"id": 508, "seek": 315896, "start": 3181.76, "end": 3186.08, "text": " But, uh,
  to start it, you can either start one core or you specify the model.", "tokens":
  [51504, 583, 11, 2232, 11, 281, 722, 309, 11, 291, 393, 2139, 722, 472, 4965, 420,
  291, 16500, 264, 2316, 13, 51720], "temperature": 0.0, "avg_logprob": -0.21900687073216293,
  "compression_ratio": 1.7983870967741935, "no_speech_prob": 0.0019972093869000673},
  {"id": 509, "seek": 318608, "start": 3186.72, "end": 3190.64, "text": " Or there''s
  a thing that says it''s called mighty cluster. It''s just a back script, back script.",
  "tokens": [50396, 1610, 456, 311, 257, 551, 300, 1619, 309, 311, 1219, 21556, 13630,
  13, 467, 311, 445, 257, 646, 5755, 11, 646, 5755, 13, 50592], "temperature": 0.0,
  "avg_logprob": -0.2029423787043645, "compression_ratio": 1.6807017543859648, "no_speech_prob":
  0.007068520411849022}, {"id": 510, "seek": 318608, "start": 3190.64, "end": 3195.52,
  "text": " And it''ll look and check how many cores you have on the machine and it''ll
  start a process for", "tokens": [50592, 400, 309, 603, 574, 293, 1520, 577, 867,
  24826, 291, 362, 322, 264, 3479, 293, 309, 603, 722, 257, 1399, 337, 50836], "temperature":
  0.0, "avg_logprob": -0.2029423787043645, "compression_ratio": 1.6807017543859648,
  "no_speech_prob": 0.007068520411849022}, {"id": 511, "seek": 318608, "start": 3195.52,
  "end": 3202.16, "text": " every core that you have. So it does this work. Um, and
  it takes like less than half a second for", "tokens": [50836, 633, 4965, 300, 291,
  362, 13, 407, 309, 775, 341, 589, 13, 3301, 11, 293, 309, 2516, 411, 1570, 813,
  1922, 257, 1150, 337, 51168], "temperature": 0.0, "avg_logprob": -0.2029423787043645,
  "compression_ratio": 1.6807017543859648, "no_speech_prob": 0.007068520411849022},
  {"id": 512, "seek": 318608, "start": 3202.16, "end": 3208.16, "text": " each quarter
  startup. It is, I, I actually put that in on purpose. That''s a limit I put in to
  slow it", "tokens": [51168, 1184, 6555, 18578, 13, 467, 307, 11, 286, 11, 286, 767,
  829, 300, 294, 322, 4334, 13, 663, 311, 257, 4948, 286, 829, 294, 281, 2964, 309,
  51468], "temperature": 0.0, "avg_logprob": -0.2029423787043645, "compression_ratio":
  1.6807017543859648, "no_speech_prob": 0.007068520411849022}, {"id": 513, "seek":
  318608, "start": 3208.16, "end": 3212.4, "text": " down a little bit. So it didn''t
  let go off the rails. Um, but you could probably take that", "tokens": [51468, 760,
  257, 707, 857, 13, 407, 309, 994, 380, 718, 352, 766, 264, 27649, 13, 3301, 11,
  457, 291, 727, 1391, 747, 300, 51680], "temperature": 0.0, "avg_logprob": -0.2029423787043645,
  "compression_ratio": 1.6807017543859648, "no_speech_prob": 0.007068520411849022},
  {"id": 514, "seek": 321240, "start": 3212.4, "end": 3217.6, "text": " limit off.
  You could just go and modify the bash script and, uh, and see how, see how quickly
  it''ll", "tokens": [50364, 4948, 766, 13, 509, 727, 445, 352, 293, 16927, 264, 46183,
  5755, 293, 11, 2232, 11, 293, 536, 577, 11, 536, 577, 2661, 309, 603, 50624], "temperature":
  0.0, "avg_logprob": -0.1596168268506772, "compression_ratio": 1.6266094420600858,
  "no_speech_prob": 0.0004996072966605425}, {"id": 515, "seek": 321240, "start": 3217.6,
  "end": 3224.4, "text": " start up. So I, so that blog post that you mentioned before,
  um, like I rented on 128 cores.", "tokens": [50624, 722, 493, 13, 407, 286, 11,
  370, 300, 6968, 2183, 300, 291, 2835, 949, 11, 1105, 11, 411, 286, 32381, 322, 29810,
  24826, 13, 50964], "temperature": 0.0, "avg_logprob": -0.1596168268506772, "compression_ratio":
  1.6266094420600858, "no_speech_prob": 0.0004996072966605425}, {"id": 516, "seek":
  321240, "start": 3224.4, "end": 3228.7200000000003, "text": " So it would take like,
  I actually took the rails off and let it start up really quickly. Um,", "tokens":
  [50964, 407, 309, 576, 747, 411, 11, 286, 767, 1890, 264, 27649, 766, 293, 718,
  309, 722, 493, 534, 2661, 13, 3301, 11, 51180], "temperature": 0.0, "avg_logprob":
  -0.1596168268506772, "compression_ratio": 1.6266094420600858, "no_speech_prob":
  0.0004996072966605425}, {"id": 517, "seek": 321240, "start": 3229.6, "end": 3237.44,
  "text": " but it can take, it can take a moment to start it up on every single core.
  Uh, and, yeah, you", "tokens": [51224, 457, 309, 393, 747, 11, 309, 393, 747, 257,
  1623, 281, 722, 309, 493, 322, 633, 2167, 4965, 13, 4019, 11, 293, 11, 1338, 11,
  291, 51616], "temperature": 0.0, "avg_logprob": -0.1596168268506772, "compression_ratio":
  1.6266094420600858, "no_speech_prob": 0.0004996072966605425}, {"id": 518, "seek":
  323744, "start": 3237.52, "end": 3241.84, "text": " you could do it in Docker. You
  could do it bare metal. Um, if there''s any people out there using", "tokens": [50368,
  291, 727, 360, 309, 294, 33772, 13, 509, 727, 360, 309, 6949, 5760, 13, 3301, 11,
  498, 456, 311, 604, 561, 484, 456, 1228, 50584], "temperature": 0.0, "avg_logprob":
  -0.16772691286527194, "compression_ratio": 1.6982456140350877, "no_speech_prob":
  0.011370191350579262}, {"id": 519, "seek": 323744, "start": 3241.84, "end": 3246.7200000000003,
  "text": " windows, I''d love to hear from you. Um, I''ve heard some feedback from
  Mac and Linux, but I haven''t", "tokens": [50584, 9309, 11, 286, 1116, 959, 281,
  1568, 490, 291, 13, 3301, 11, 286, 600, 2198, 512, 5824, 490, 5707, 293, 18734,
  11, 457, 286, 2378, 380, 50828], "temperature": 0.0, "avg_logprob": -0.16772691286527194,
  "compression_ratio": 1.6982456140350877, "no_speech_prob": 0.011370191350579262},
  {"id": 520, "seek": 323744, "start": 3246.7200000000003, "end": 3251.36, "text":
  " gotten any windows feedback. So I don''t even know if it''s worth building it
  for windows these days.", "tokens": [50828, 5768, 604, 9309, 5824, 13, 407, 286,
  500, 380, 754, 458, 498, 309, 311, 3163, 2390, 309, 337, 9309, 613, 1708, 13, 51060],
  "temperature": 0.0, "avg_logprob": -0.16772691286527194, "compression_ratio": 1.6982456140350877,
  "no_speech_prob": 0.011370191350579262}, {"id": 521, "seek": 323744, "start": 3251.36,
  "end": 3258.2400000000002, "text": " Maybe not. Yeah, I think it depends. If I don''t
  know what should be this scenario is like you", "tokens": [51060, 2704, 406, 13,
  865, 11, 286, 519, 309, 5946, 13, 759, 286, 500, 380, 458, 437, 820, 312, 341, 9005,
  307, 411, 291, 51404], "temperature": 0.0, "avg_logprob": -0.16772691286527194,
  "compression_ratio": 1.6982456140350877, "no_speech_prob": 0.011370191350579262},
  {"id": 522, "seek": 323744, "start": 3258.2400000000002, "end": 3264.32, "text":
  " are a developer on windows. And for some reason, you don''t go on your server
  side to like you,", "tokens": [51404, 366, 257, 10754, 322, 9309, 13, 400, 337,
  512, 1778, 11, 291, 500, 380, 352, 322, 428, 7154, 1252, 281, 411, 291, 11, 51708],
  "temperature": 0.0, "avg_logprob": -0.16772691286527194, "compression_ratio": 1.6982456140350877,
  "no_speech_prob": 0.011370191350579262}, {"id": 523, "seek": 326432, "start": 3264.4,
  "end": 3268.7200000000003, "text": " we still want to develop everything locally,
  right? So you want to bring up, I saw such guys actually", "tokens": [50368, 321,
  920, 528, 281, 1499, 1203, 16143, 11, 558, 30, 407, 291, 528, 281, 1565, 493, 11,
  286, 1866, 1270, 1074, 767, 50584], "temperature": 0.0, "avg_logprob": -0.1669043712928647,
  "compression_ratio": 1.7035714285714285, "no_speech_prob": 0.006542309653013945},
  {"id": 524, "seek": 326432, "start": 3268.7200000000003, "end": 3275.1200000000003,
  "text": " in my team, they wanted to bring every single server service on their
  laptop. Yeah. And that''s", "tokens": [50584, 294, 452, 1469, 11, 436, 1415, 281,
  1565, 633, 2167, 7154, 2643, 322, 641, 10732, 13, 865, 13, 400, 300, 311, 50904],
  "temperature": 0.0, "avg_logprob": -0.1669043712928647, "compression_ratio": 1.7035714285714285,
  "no_speech_prob": 0.006542309653013945}, {"id": 525, "seek": 326432, "start": 3275.1200000000003,
  "end": 3279.92, "text": " how they developed. They didn''t want to depend on any
  external connection. Right. Even,", "tokens": [50904, 577, 436, 4743, 13, 814, 994,
  380, 528, 281, 5672, 322, 604, 8320, 4984, 13, 1779, 13, 2754, 11, 51144], "temperature":
  0.0, "avg_logprob": -0.1669043712928647, "compression_ratio": 1.7035714285714285,
  "no_speech_prob": 0.006542309653013945}, {"id": 526, "seek": 326432, "start": 3279.92,
  "end": 3285.76, "text": " even Docker is like a pain in windows these days sometimes,
  right? So I know that I know the", "tokens": [51144, 754, 33772, 307, 411, 257,
  1822, 294, 9309, 613, 1708, 2171, 11, 558, 30, 407, 286, 458, 300, 286, 458, 264,
  51436], "temperature": 0.0, "avg_logprob": -0.1669043712928647, "compression_ratio":
  1.7035714285714285, "no_speech_prob": 0.006542309653013945}, {"id": 527, "seek":
  326432, "start": 3285.76, "end": 3291.36, "text": " windows ecosystem, because I
  used to, I used to be in in the 2000s. That''s the, that''s the mindset.", "tokens":
  [51436, 9309, 11311, 11, 570, 286, 1143, 281, 11, 286, 1143, 281, 312, 294, 294,
  264, 8132, 82, 13, 663, 311, 264, 11, 300, 311, 264, 12543, 13, 51716], "temperature":
  0.0, "avg_logprob": -0.1669043712928647, "compression_ratio": 1.7035714285714285,
  "no_speech_prob": 0.006542309653013945}, {"id": 528, "seek": 329136, "start": 3291.36,
  "end": 3294.6400000000003, "text": " It''s like I''m just going to run everything
  natively in windows. Yeah.", "tokens": [50364, 467, 311, 411, 286, 478, 445, 516,
  281, 1190, 1203, 8470, 356, 294, 9309, 13, 865, 13, 50528], "temperature": 0.0,
  "avg_logprob": -0.17491290148566752, "compression_ratio": 1.5728155339805825, "no_speech_prob":
  0.011930027045309544}, {"id": 529, "seek": 329136, "start": 3296.6400000000003,
  "end": 3304.2400000000002, "text": " And like when I tried mighty on on Mac, I think
  it took like some seconds to boot,", "tokens": [50628, 400, 411, 562, 286, 3031,
  21556, 322, 322, 5707, 11, 286, 519, 309, 1890, 411, 512, 3949, 281, 11450, 11,
  51008], "temperature": 0.0, "avg_logprob": -0.17491290148566752, "compression_ratio":
  1.5728155339805825, "no_speech_prob": 0.011930027045309544}, {"id": 530, "seek":
  329136, "start": 3304.2400000000002, "end": 3309.04, "text": " but the moment it
  booted, I was like shooting some queries and like to compute the vectors and", "tokens":
  [51008, 457, 264, 1623, 309, 11450, 292, 11, 286, 390, 411, 5942, 512, 24109, 293,
  411, 281, 14722, 264, 18875, 293, 51248], "temperature": 0.0, "avg_logprob": -0.17491290148566752,
  "compression_ratio": 1.5728155339805825, "no_speech_prob": 0.011930027045309544},
  {"id": 531, "seek": 329136, "start": 3309.04, "end": 3315.1200000000003, "text":
  " it was insanely fast. Is it only on a secret source in this insane fastness?",
  "tokens": [51248, 309, 390, 40965, 2370, 13, 1119, 309, 787, 322, 257, 4054, 4009,
  294, 341, 10838, 2370, 1287, 30, 51552], "temperature": 0.0, "avg_logprob": -0.17491290148566752,
  "compression_ratio": 1.5728155339805825, "no_speech_prob": 0.011930027045309544},
  {"id": 532, "seek": 331512, "start": 3316.08, "end": 3322.4, "text": " I mean, if
  you''re used to running models and Python, it''ll seem insanely fast. A lot of",
  "tokens": [50412, 286, 914, 11, 498, 291, 434, 1143, 281, 2614, 5245, 293, 15329,
  11, 309, 603, 1643, 40965, 2370, 13, 316, 688, 295, 50728], "temperature": 0.0,
  "avg_logprob": -0.24038882785373264, "compression_ratio": 1.569377990430622, "no_speech_prob":
  0.007889417931437492}, {"id": 533, "seek": 331512, "start": 3322.4, "end": 3328.4,
  "text": " it is on. That''s they get most of the credit there. Yes. But there''s
  a lot of other stuff that", "tokens": [50728, 309, 307, 322, 13, 663, 311, 436,
  483, 881, 295, 264, 5397, 456, 13, 1079, 13, 583, 456, 311, 257, 688, 295, 661,
  1507, 300, 51028], "temperature": 0.0, "avg_logprob": -0.24038882785373264, "compression_ratio":
  1.569377990430622, "no_speech_prob": 0.007889417931437492}, {"id": 534, "seek":
  331512, "start": 3328.4, "end": 3334.0, "text": " goes into it, which is like the
  tokenization and the pre processing and the post processing is", "tokens": [51028,
  1709, 666, 309, 11, 597, 307, 411, 264, 14862, 2144, 293, 264, 659, 9007, 293, 264,
  2183, 9007, 307, 51308], "temperature": 0.0, "avg_logprob": -0.24038882785373264,
  "compression_ratio": 1.569377990430622, "no_speech_prob": 0.007889417931437492},
  {"id": 535, "seek": 331512, "start": 3334.0, "end": 3338.7999999999997, "text":
  " just, it''s fast is I''ve been using Rust for it and", "tokens": [51308, 445,
  11, 309, 311, 2370, 307, 286, 600, 668, 1228, 34952, 337, 309, 293, 51548], "temperature":
  0.0, "avg_logprob": -0.24038882785373264, "compression_ratio": 1.569377990430622,
  "no_speech_prob": 0.007889417931437492}, {"id": 536, "seek": 333880, "start": 3339.36,
  "end": 3345.52, "text": " Rust is a, Rust is a really interesting language. It''s
  it''s gotten me back into systems programming.", "tokens": [50392, 34952, 307, 257,
  11, 34952, 307, 257, 534, 1880, 2856, 13, 467, 311, 309, 311, 5768, 385, 646, 666,
  3652, 9410, 13, 50700], "temperature": 0.0, "avg_logprob": -0.17074422367283557,
  "compression_ratio": 1.7463235294117647, "no_speech_prob": 0.004121183417737484},
  {"id": 537, "seek": 333880, "start": 3346.5600000000004, "end": 3350.4, "text":
  " I''m not here to say that like Rust is like the most amazing thing ever. There
  are things I love", "tokens": [50752, 286, 478, 406, 510, 281, 584, 300, 411, 34952,
  307, 411, 264, 881, 2243, 551, 1562, 13, 821, 366, 721, 286, 959, 50944], "temperature":
  0.0, "avg_logprob": -0.17074422367283557, "compression_ratio": 1.7463235294117647,
  "no_speech_prob": 0.004121183417737484}, {"id": 538, "seek": 333880, "start": 3350.4,
  "end": 3355.04, "text": " about it, the things that are like, I don''t know if I
  would do that way, but you''re supposed to", "tokens": [50944, 466, 309, 11, 264,
  721, 300, 366, 411, 11, 286, 500, 380, 458, 498, 286, 576, 360, 300, 636, 11, 457,
  291, 434, 3442, 281, 51176], "temperature": 0.0, "avg_logprob": -0.17074422367283557,
  "compression_ratio": 1.7463235294117647, "no_speech_prob": 0.004121183417737484},
  {"id": 539, "seek": 333880, "start": 3355.04, "end": 3360.48, "text": " do things
  a certain way because the compiler understands that it''ll super optimize it for
  you.", "tokens": [51176, 360, 721, 257, 1629, 636, 570, 264, 31958, 15146, 300,
  309, 603, 1687, 19719, 309, 337, 291, 13, 51448], "temperature": 0.0, "avg_logprob":
  -0.17074422367283557, "compression_ratio": 1.7463235294117647, "no_speech_prob":
  0.004121183417737484}, {"id": 540, "seek": 333880, "start": 3361.04, "end": 3364.8,
  "text": " It''s hard to, it''s hard to wrap your brain around it if you''re if you''re
  from a dynamic", "tokens": [51476, 467, 311, 1152, 281, 11, 309, 311, 1152, 281,
  7019, 428, 3567, 926, 309, 498, 291, 434, 498, 291, 434, 490, 257, 8546, 51664],
  "temperature": 0.0, "avg_logprob": -0.17074422367283557, "compression_ratio": 1.7463235294117647,
  "no_speech_prob": 0.004121183417737484}, {"id": 541, "seek": 336480, "start": 3364.8,
  "end": 3370.96, "text": " really typed language like Python or JavaScript. It''s
  hard to get a handle on node. My my compiled", "tokens": [50364, 534, 33941, 2856,
  411, 15329, 420, 15778, 13, 467, 311, 1152, 281, 483, 257, 4813, 322, 9984, 13,
  1222, 452, 36548, 50672], "temperature": 0.0, "avg_logprob": -0.19009941668549846,
  "compression_ratio": 1.7634408602150538, "no_speech_prob": 0.010129575617611408},
  {"id": 542, "seek": 336480, "start": 3370.96, "end": 3377.1200000000003, "text":
  " background like, you know, typed, typed programming languages compile ahead of
  time. I was used", "tokens": [50672, 3678, 411, 11, 291, 458, 11, 33941, 11, 33941,
  9410, 8650, 31413, 2286, 295, 565, 13, 286, 390, 1143, 50980], "temperature": 0.0,
  "avg_logprob": -0.19009941668549846, "compression_ratio": 1.7634408602150538, "no_speech_prob":
  0.010129575617611408}, {"id": 543, "seek": 336480, "start": 3377.1200000000003,
  "end": 3382.2400000000002, "text": " to that from my previous life. So I was able
  to pick it up again and I read the I read I just read", "tokens": [50980, 281, 300,
  490, 452, 3894, 993, 13, 407, 286, 390, 1075, 281, 1888, 309, 493, 797, 293, 286,
  1401, 264, 286, 1401, 286, 445, 1401, 51236], "temperature": 0.0, "avg_logprob":
  -0.19009941668549846, "compression_ratio": 1.7634408602150538, "no_speech_prob":
  0.010129575617611408}, {"id": 544, "seek": 336480, "start": 3382.2400000000002,
  "end": 3387.04, "text": " the rest book. There''s a free book out there. I actually
  bought the I bought a paperback because", "tokens": [51236, 264, 1472, 1446, 13,
  821, 311, 257, 1737, 1446, 484, 456, 13, 286, 767, 4243, 264, 286, 4243, 257, 3035,
  3207, 570, 51476], "temperature": 0.0, "avg_logprob": -0.19009941668549846, "compression_ratio":
  1.7634408602150538, "no_speech_prob": 0.010129575617611408}, {"id": 545, "seek":
  336480, "start": 3387.04, "end": 3394.1600000000003, "text": " I like paperbacks
  and I like hard covers like actual paper these days. So I was reading it like that.",
  "tokens": [51476, 286, 411, 3035, 17758, 293, 286, 411, 1152, 10538, 411, 3539,
  3035, 613, 1708, 13, 407, 286, 390, 3760, 309, 411, 300, 13, 51832], "temperature":
  0.0, "avg_logprob": -0.19009941668549846, "compression_ratio": 1.7634408602150538,
  "no_speech_prob": 0.010129575617611408}, {"id": 546, "seek": 339480, "start": 3395.6000000000004,
  "end": 3399.28, "text": " And just going through the examples took me a couple weeks
  to get a handle on Rust.", "tokens": [50404, 400, 445, 516, 807, 264, 5110, 1890,
  385, 257, 1916, 3259, 281, 483, 257, 4813, 322, 34952, 13, 50588], "temperature":
  0.0, "avg_logprob": -0.13685197096604568, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.001487237517721951}, {"id": 547, "seek": 339480, "start": 3401.2000000000003,
  "end": 3409.52, "text": " That gets a lot of the credit as well, the Rust language.
  It''s just it optimizes and you know,", "tokens": [50684, 663, 2170, 257, 688, 295,
  264, 5397, 382, 731, 11, 264, 34952, 2856, 13, 467, 311, 445, 309, 5028, 5660, 293,
  291, 458, 11, 51100], "temperature": 0.0, "avg_logprob": -0.13685197096604568, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.001487237517721951}, {"id": 548, "seek":
  339480, "start": 3409.52, "end": 3417.44, "text": " you have to learn this field
  that I''m in now with model inference. It''s like the super niche field of", "tokens":
  [51100, 291, 362, 281, 1466, 341, 2519, 300, 286, 478, 294, 586, 365, 2316, 38253,
  13, 467, 311, 411, 264, 1687, 19956, 2519, 295, 51496], "temperature": 0.0, "avg_logprob":
  -0.13685197096604568, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.001487237517721951}, {"id": 549, "seek": 339480, "start": 3417.44, "end": 3422.32,
  "text": " like you have to understand the hardware and you have to understand the
  machine learning.", "tokens": [51496, 411, 291, 362, 281, 1223, 264, 8837, 293,
  291, 362, 281, 1223, 264, 3479, 2539, 13, 51740], "temperature": 0.0, "avg_logprob":
  -0.13685197096604568, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.001487237517721951}, {"id": 550, "seek": 342232, "start": 3423.04, "end": 3428.7200000000003,
  "text": " And there are those two fields are like so different. There are very few
  people out there that are", "tokens": [50400, 400, 456, 366, 729, 732, 7909, 366,
  411, 370, 819, 13, 821, 366, 588, 1326, 561, 484, 456, 300, 366, 50684], "temperature":
  0.0, "avg_logprob": -0.16213827495333516, "compression_ratio": 1.5125628140703518,
  "no_speech_prob": 0.001896693604066968}, {"id": 551, "seek": 342232, "start": 3429.52,
  "end": 3441.04, "text": " really good in both. So I know that there''s a word vectorization.
  So vectorized on the CPU is like,", "tokens": [50724, 534, 665, 294, 1293, 13, 407,
  286, 458, 300, 456, 311, 257, 1349, 8062, 2144, 13, 407, 8062, 1602, 322, 264, 13199,
  307, 411, 11, 51300], "temperature": 0.0, "avg_logprob": -0.16213827495333516, "compression_ratio":
  1.5125628140703518, "no_speech_prob": 0.001896693604066968}, {"id": 552, "seek":
  342232, "start": 3441.04, "end": 3448.4, "text": " well, if I have to do a calculation
  with eight with a byte and you know, I have a register at 64 bits.", "tokens": [51300,
  731, 11, 498, 286, 362, 281, 360, 257, 17108, 365, 3180, 365, 257, 40846, 293, 291,
  458, 11, 286, 362, 257, 7280, 412, 12145, 9239, 13, 51668], "temperature": 0.0,
  "avg_logprob": -0.16213827495333516, "compression_ratio": 1.5125628140703518, "no_speech_prob":
  0.001896693604066968}, {"id": 553, "seek": 344840, "start": 3449.36, "end": 3456.32,
  "text": " But I have an eight bit byte like, well, I can vectorize and I can do
  eight calculations because it''s", "tokens": [50412, 583, 286, 362, 364, 3180, 857,
  40846, 411, 11, 731, 11, 286, 393, 8062, 1125, 293, 286, 393, 360, 3180, 20448,
  570, 309, 311, 50760], "temperature": 0.0, "avg_logprob": -0.2842003984271355, "compression_ratio":
  1.5905511811023623, "no_speech_prob": 0.0031938592437654734}, {"id": 554, "seek":
  344840, "start": 3456.32, "end": 3464.4, "text": " with SIMD, same instruction multiple
  data. So that so Rust, if you turn on certain compile flags,", "tokens": [50760,
  365, 24738, 35, 11, 912, 10951, 3866, 1412, 13, 407, 300, 370, 34952, 11, 498, 291,
  1261, 322, 1629, 31413, 23265, 11, 51164], "temperature": 0.0, "avg_logprob": -0.2842003984271355,
  "compression_ratio": 1.5905511811023623, "no_speech_prob": 0.0031938592437654734},
  {"id": 555, "seek": 344840, "start": 3464.4, "end": 3469.6, "text": " it''ll do
  that for you automatically. So you get that speed up. So I turn those knobs all
  the way up.", "tokens": [51164, 309, 603, 360, 300, 337, 291, 6772, 13, 407, 291,
  483, 300, 3073, 493, 13, 407, 286, 1261, 729, 46999, 439, 264, 636, 493, 13, 51424],
  "temperature": 0.0, "avg_logprob": -0.2842003984271355, "compression_ratio": 1.5905511811023623,
  "no_speech_prob": 0.0031938592437654734}, {"id": 556, "seek": 344840, "start": 3469.6,
  "end": 3476.88, "text": " I said use all the use AVX1 and 2 if the process supports
  it and most processes do these days if you''re", "tokens": [51424, 286, 848, 764,
  439, 264, 764, 30198, 55, 16, 293, 568, 498, 264, 1399, 9346, 309, 293, 881, 7555,
  360, 613, 1708, 498, 291, 434, 51788], "temperature": 0.0, "avg_logprob": -0.2842003984271355,
  "compression_ratio": 1.5905511811023623, "no_speech_prob": 0.0031938592437654734},
  {"id": 557, "seek": 347688, "start": 3476.88, "end": 3483.76, "text": " on X86.
  ARM has a different set. I haven''t gotten into the ARM world that I have to get
  an M1 Mac and", "tokens": [50364, 322, 1783, 22193, 13, 45209, 575, 257, 819, 992,
  13, 286, 2378, 380, 5768, 666, 264, 45209, 1002, 300, 286, 362, 281, 483, 364, 376,
  16, 5707, 293, 50708], "temperature": 0.0, "avg_logprob": -0.10746487704190341,
  "compression_ratio": 1.6694214876033058, "no_speech_prob": 0.001158062950707972},
  {"id": 558, "seek": 347688, "start": 3483.76, "end": 3490.08, "text": " I''m going
  to start messing around with all that. But if you know that stuff and you know how
  to turn it", "tokens": [50708, 286, 478, 516, 281, 722, 23258, 926, 365, 439, 300,
  13, 583, 498, 291, 458, 300, 1507, 293, 291, 458, 577, 281, 1261, 309, 51024], "temperature":
  0.0, "avg_logprob": -0.10746487704190341, "compression_ratio": 1.6694214876033058,
  "no_speech_prob": 0.001158062950707972}, {"id": 559, "seek": 347688, "start": 3490.08,
  "end": 3496.96, "text": " on, Rust does the rest for you. You kind of have to write
  your code a certain way so that, you know,", "tokens": [51024, 322, 11, 34952, 775,
  264, 1472, 337, 291, 13, 509, 733, 295, 362, 281, 2464, 428, 3089, 257, 1629, 636,
  370, 300, 11, 291, 458, 11, 51368], "temperature": 0.0, "avg_logprob": -0.10746487704190341,
  "compression_ratio": 1.6694214876033058, "no_speech_prob": 0.001158062950707972},
  {"id": 560, "seek": 347688, "start": 3496.96, "end": 3501.12, "text": " Rust will
  do the optimization a certain way. You can''t think like old school. You have to
  kind of", "tokens": [51368, 34952, 486, 360, 264, 19618, 257, 1629, 636, 13, 509,
  393, 380, 519, 411, 1331, 1395, 13, 509, 362, 281, 733, 295, 51576], "temperature":
  0.0, "avg_logprob": -0.10746487704190341, "compression_ratio": 1.6694214876033058,
  "no_speech_prob": 0.001158062950707972}, {"id": 561, "seek": 350112, "start": 3501.12,
  "end": 3507.8399999999997, "text": " think in Rust world a little bit. But doing
  that, now you get all this extra, all this extra speed", "tokens": [50364, 519,
  294, 34952, 1002, 257, 707, 857, 13, 583, 884, 300, 11, 586, 291, 483, 439, 341,
  2857, 11, 439, 341, 2857, 3073, 50700], "temperature": 0.0, "avg_logprob": -0.16897632678349814,
  "compression_ratio": 1.5958333333333334, "no_speech_prob": 0.006385597866028547},
  {"id": 562, "seek": 350112, "start": 3508.64, "end": 3512.64, "text": " from pretty
  much nothing just from writing your code a certain way turning on a couple of compiled",
  "tokens": [50740, 490, 1238, 709, 1825, 445, 490, 3579, 428, 3089, 257, 1629, 636,
  6246, 322, 257, 1916, 295, 36548, 50940], "temperature": 0.0, "avg_logprob": -0.16897632678349814,
  "compression_ratio": 1.5958333333333334, "no_speech_prob": 0.006385597866028547},
  {"id": 563, "seek": 350112, "start": 3512.64, "end": 3518.96, "text": " flags. That''s
  why it was so fast. Yeah, but you still needed to figure all of these out and I",
  "tokens": [50940, 23265, 13, 663, 311, 983, 309, 390, 370, 2370, 13, 865, 11, 457,
  291, 920, 2978, 281, 2573, 439, 295, 613, 484, 293, 286, 51256], "temperature":
  0.0, "avg_logprob": -0.16897632678349814, "compression_ratio": 1.5958333333333334,
  "no_speech_prob": 0.006385597866028547}, {"id": 564, "seek": 350112, "start": 3518.96,
  "end": 3525.6, "text": " remember you were you were saying that you had a bunch
  of weeks, you know, coding on stuff.", "tokens": [51256, 1604, 291, 645, 291, 645,
  1566, 300, 291, 632, 257, 3840, 295, 3259, 11, 291, 458, 11, 17720, 322, 1507, 13,
  51588], "temperature": 0.0, "avg_logprob": -0.16897632678349814, "compression_ratio":
  1.5958333333333334, "no_speech_prob": 0.006385597866028547}, {"id": 565, "seek":
  352560, "start": 3526.56, "end": 3532.24, "text": " Yeah, you get things done because
  I know and many of us probably know here in the audience that", "tokens": [50412,
  865, 11, 291, 483, 721, 1096, 570, 286, 458, 293, 867, 295, 505, 1391, 458, 510,
  294, 264, 4034, 300, 50696], "temperature": 0.0, "avg_logprob": -0.1683180191937615,
  "compression_ratio": 1.583673469387755, "no_speech_prob": 0.053860876709222794},
  {"id": 566, "seek": 352560, "start": 3532.24, "end": 3538.7999999999997, "text":
  " if you are a programmer, you might say, yeah, I can do it. But you cannot actually
  estimate when", "tokens": [50696, 498, 291, 366, 257, 32116, 11, 291, 1062, 584,
  11, 1338, 11, 286, 393, 360, 309, 13, 583, 291, 2644, 767, 12539, 562, 51024], "temperature":
  0.0, "avg_logprob": -0.1683180191937615, "compression_ratio": 1.583673469387755,
  "no_speech_prob": 0.053860876709222794}, {"id": 567, "seek": 352560, "start": 3538.7999999999997,
  "end": 3544.96, "text": " you will be done. So you get into the weeds and like,
  oh my god, it just like UTF or something else", "tokens": [51024, 291, 486, 312,
  1096, 13, 407, 291, 483, 666, 264, 26370, 293, 411, 11, 1954, 452, 3044, 11, 309,
  445, 411, 624, 20527, 420, 746, 1646, 51332], "temperature": 0.0, "avg_logprob":
  -0.1683180191937615, "compression_ratio": 1.583673469387755, "no_speech_prob": 0.053860876709222794},
  {"id": 568, "seek": 352560, "start": 3544.96, "end": 3549.7599999999998, "text":
  " doesn''t work or like, I''m sending a requested fails, whatever, what''s going
  on and you spend so", "tokens": [51332, 1177, 380, 589, 420, 411, 11, 286, 478,
  7750, 257, 16436, 18199, 11, 2035, 11, 437, 311, 516, 322, 293, 291, 3496, 370,
  51572], "temperature": 0.0, "avg_logprob": -0.1683180191937615, "compression_ratio":
  1.583673469387755, "no_speech_prob": 0.053860876709222794}, {"id": 569, "seek":
  354976, "start": 3549.76, "end": 3555.1200000000003, "text": " much time or if you''re
  doing an algorithm, that''s another story. That''s like an internet journey", "tokens":
  [50364, 709, 565, 420, 498, 291, 434, 884, 364, 9284, 11, 300, 311, 1071, 1657,
  13, 663, 311, 411, 364, 4705, 4671, 50632], "temperature": 0.0, "avg_logprob": -0.16823814465449408,
  "compression_ratio": 1.6623931623931625, "no_speech_prob": 0.0027399607934057713},
  {"id": 570, "seek": 354976, "start": 3555.1200000000003, "end": 3562.8, "text":
  " there, like debugging all these states. And I mean, I''m just trying to say that
  even though you", "tokens": [50632, 456, 11, 411, 45592, 439, 613, 4368, 13, 400,
  286, 914, 11, 286, 478, 445, 1382, 281, 584, 300, 754, 1673, 291, 51016], "temperature":
  0.0, "avg_logprob": -0.16823814465449408, "compression_ratio": 1.6623931623931625,
  "no_speech_prob": 0.0027399607934057713}, {"id": 571, "seek": 354976, "start": 3562.8,
  "end": 3570.96, "text": " you make it sound so easy to to master Rust and you know,
  to go through all these maze and make", "tokens": [51016, 291, 652, 309, 1626, 370,
  1858, 281, 281, 4505, 34952, 293, 291, 458, 11, 281, 352, 807, 439, 613, 33032,
  293, 652, 51424], "temperature": 0.0, "avg_logprob": -0.16823814465449408, "compression_ratio":
  1.6623931623931625, "no_speech_prob": 0.0027399607934057713}, {"id": 572, "seek":
  354976, "start": 3570.96, "end": 3578.2400000000002, "text": " it the way compiler
  wants it, it''s still time. It''s a lot of time. It''s skill. And so you master
  it.", "tokens": [51424, 309, 264, 636, 31958, 2738, 309, 11, 309, 311, 920, 565,
  13, 467, 311, 257, 688, 295, 565, 13, 467, 311, 5389, 13, 400, 370, 291, 4505, 309,
  13, 51788], "temperature": 0.0, "avg_logprob": -0.16823814465449408, "compression_ratio":
  1.6623931623931625, "no_speech_prob": 0.0027399607934057713}, {"id": 573, "seek":
  357824, "start": 3578.24, "end": 3584.7999999999997, "text": " And that''s why and
  in the end, you know, the end result was not given. You earned it, right?", "tokens":
  [50364, 400, 300, 311, 983, 293, 294, 264, 917, 11, 291, 458, 11, 264, 917, 1874,
  390, 406, 2212, 13, 509, 12283, 309, 11, 558, 30, 50692], "temperature": 0.0, "avg_logprob":
  -0.17792512785713627, "compression_ratio": 1.706896551724138, "no_speech_prob":
  0.0017735135043039918}, {"id": 574, "seek": 357824, "start": 3585.4399999999996,
  "end": 3592.08, "text": " So why not turn this into the business? So now on the
  business side, I''m thinking, how do you offer", "tokens": [50724, 407, 983, 406,
  1261, 341, 666, 264, 1606, 30, 407, 586, 322, 264, 1606, 1252, 11, 286, 478, 1953,
  11, 577, 360, 291, 2626, 51056], "temperature": 0.0, "avg_logprob": -0.17792512785713627,
  "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0017735135043039918},
  {"id": 575, "seek": 357824, "start": 3592.08, "end": 3599.3599999999997, "text":
  " Rust? Like, so how do you offer excuse me, mighty? So you have you have the the
  binary, you have the", "tokens": [51056, 34952, 30, 1743, 11, 370, 577, 360, 291,
  2626, 8960, 385, 11, 21556, 30, 407, 291, 362, 291, 362, 264, 264, 17434, 11, 291,
  362, 264, 51420], "temperature": 0.0, "avg_logprob": -0.17792512785713627, "compression_ratio":
  1.706896551724138, "no_speech_prob": 0.0017735135043039918}, {"id": 576, "seek":
  357824, "start": 3599.3599999999997, "end": 3605.4399999999996, "text": " like the
  model will be shipped separately somehow outside of binary, right? But what is a
  customer I''m", "tokens": [51420, 411, 264, 2316, 486, 312, 25312, 14759, 6063,
  2380, 295, 17434, 11, 558, 30, 583, 437, 307, 257, 5474, 286, 478, 51724], "temperature":
  0.0, "avg_logprob": -0.17792512785713627, "compression_ratio": 1.706896551724138,
  "no_speech_prob": 0.0017735135043039918}, {"id": 577, "seek": 360544, "start": 3605.44,
  "end": 3612.4, "text": " paying for? And yeah, and also kind of ahead of time, a
  question, can you give a discount code", "tokens": [50364, 6229, 337, 30, 400, 1338,
  11, 293, 611, 733, 295, 2286, 295, 565, 11, 257, 1168, 11, 393, 291, 976, 257, 11635,
  3089, 50712], "temperature": 0.0, "avg_logprob": -0.13891210468537216, "compression_ratio":
  1.5925925925925926, "no_speech_prob": 0.0020615719258785248}, {"id": 578, "seek":
  360544, "start": 3612.4, "end": 3622.2400000000002, "text": " for our audience to
  try it? Oh, that''s a great question. Um, uh, yes. So my business model is,", "tokens":
  [50712, 337, 527, 4034, 281, 853, 309, 30, 876, 11, 300, 311, 257, 869, 1168, 13,
  3301, 11, 2232, 11, 2086, 13, 407, 452, 1606, 2316, 307, 11, 51204], "temperature":
  0.0, "avg_logprob": -0.13891210468537216, "compression_ratio": 1.5925925925925926,
  "no_speech_prob": 0.0020615719258785248}, {"id": 579, "seek": 360544, "start": 3622.96,
  "end": 3627.76, "text": " is again, old school, because I''ve been doing software
  for a long time. So it''s licensed software,", "tokens": [51240, 307, 797, 11, 1331,
  1395, 11, 570, 286, 600, 668, 884, 4722, 337, 257, 938, 565, 13, 407, 309, 311,
  25225, 4722, 11, 51480], "temperature": 0.0, "avg_logprob": -0.13891210468537216,
  "compression_ratio": 1.5925925925925926, "no_speech_prob": 0.0020615719258785248},
  {"id": 580, "seek": 360544, "start": 3627.76, "end": 3632.96, "text": " right? You
  pay, you pay a license, you get to use the software. Um, I''m still trying to figure
  out", "tokens": [51480, 558, 30, 509, 1689, 11, 291, 1689, 257, 10476, 11, 291,
  483, 281, 764, 264, 4722, 13, 3301, 11, 286, 478, 920, 1382, 281, 2573, 484, 51740],
  "temperature": 0.0, "avg_logprob": -0.13891210468537216, "compression_ratio": 1.5925925925925926,
  "no_speech_prob": 0.0020615719258785248}, {"id": 581, "seek": 363296, "start": 3632.96,
  "end": 3638.32, "text": " the exact price point. Um, some people say, some people
  say it''s too cheap, which is interesting,", "tokens": [50364, 264, 1900, 3218,
  935, 13, 3301, 11, 512, 561, 584, 11, 512, 561, 584, 309, 311, 886, 7084, 11, 597,
  307, 1880, 11, 50632], "temperature": 0.0, "avg_logprob": -0.16370959933713186,
  "compression_ratio": 1.7419354838709677, "no_speech_prob": 0.0046398574486374855},
  {"id": 582, "seek": 363296, "start": 3638.32, "end": 3643.6, "text": " because I
  didn''t, I didn''t think so. Um, some people think I say I should charge more money
  for it.", "tokens": [50632, 570, 286, 994, 380, 11, 286, 994, 380, 519, 370, 13,
  3301, 11, 512, 561, 519, 286, 584, 286, 820, 4602, 544, 1460, 337, 309, 13, 50896],
  "temperature": 0.0, "avg_logprob": -0.16370959933713186, "compression_ratio": 1.7419354838709677,
  "no_speech_prob": 0.0046398574486374855}, {"id": 583, "seek": 363296, "start": 3644.0,
  "end": 3650.0, "text": " Uh, it''s $99 a month right now. When this podcast is published
  and after that, it may change.", "tokens": [50916, 4019, 11, 309, 311, 1848, 8494,
  257, 1618, 558, 586, 13, 1133, 341, 7367, 307, 6572, 293, 934, 300, 11, 309, 815,
  1319, 13, 51216], "temperature": 0.0, "avg_logprob": -0.16370959933713186, "compression_ratio":
  1.7419354838709677, "no_speech_prob": 0.0046398574486374855}, {"id": 584, "seek":
  363296, "start": 3650.56, "end": 3655.2, "text": " If you get it, I don''t have,
  it''s a light up to strike. I can go in and create a discount code", "tokens": [51244,
  759, 291, 483, 309, 11, 286, 500, 380, 362, 11, 309, 311, 257, 1442, 493, 281, 9302,
  13, 286, 393, 352, 294, 293, 1884, 257, 11635, 3089, 51476], "temperature": 0.0,
  "avg_logprob": -0.16370959933713186, "compression_ratio": 1.7419354838709677, "no_speech_prob":
  0.0046398574486374855}, {"id": 585, "seek": 363296, "start": 3655.84, "end": 3660.32,
  "text": " for folks. I don''t have a code right now. But if you, if you email me
  and you say I heard about you", "tokens": [51508, 337, 4024, 13, 286, 500, 380,
  362, 257, 3089, 558, 586, 13, 583, 498, 291, 11, 498, 291, 3796, 385, 293, 291,
  584, 286, 2198, 466, 291, 51732], "temperature": 0.0, "avg_logprob": -0.16370959933713186,
  "compression_ratio": 1.7419354838709677, "no_speech_prob": 0.0046398574486374855},
  {"id": 586, "seek": 366032, "start": 3660.4, "end": 3665.28, "text": " on the vector
  podcast, um, follow the link in the description, like follow the link in the notes
  and", "tokens": [50368, 322, 264, 8062, 7367, 11, 1105, 11, 1524, 264, 2113, 294,
  264, 3855, 11, 411, 1524, 264, 2113, 294, 264, 5570, 293, 50612], "temperature":
  0.0, "avg_logprob": -0.15423403845893013, "compression_ratio": 1.6866359447004609,
  "no_speech_prob": 0.0013247025199234486}, {"id": 587, "seek": 366032, "start": 3665.92,
  "end": 3669.6000000000004, "text": " email, we''ll, we''ll set something up, um,
  so you can get a discount.", "tokens": [50644, 3796, 11, 321, 603, 11, 321, 603,
  992, 746, 493, 11, 1105, 11, 370, 291, 393, 483, 257, 11635, 13, 50828], "temperature":
  0.0, "avg_logprob": -0.15423403845893013, "compression_ratio": 1.6866359447004609,
  "no_speech_prob": 0.0013247025199234486}, {"id": 588, "seek": 366032, "start": 3670.96,
  "end": 3677.1200000000003, "text": " Uh, that''s the way it works. But that''s,
  uh, that''s for commercial. So if you''re using it commercially,", "tokens": [50896,
  4019, 11, 300, 311, 264, 636, 309, 1985, 13, 583, 300, 311, 11, 2232, 11, 300, 311,
  337, 6841, 13, 407, 498, 291, 434, 1228, 309, 41751, 11, 51204], "temperature":
  0.0, "avg_logprob": -0.15423403845893013, "compression_ratio": 1.6866359447004609,
  "no_speech_prob": 0.0013247025199234486}, {"id": 589, "seek": 366032, "start": 3677.1200000000003,
  "end": 3683.76, "text": " um, and you''re making money from it, uh, then, you know,
  I, I ask you pay a license, please.", "tokens": [51204, 1105, 11, 293, 291, 434,
  1455, 1460, 490, 309, 11, 2232, 11, 550, 11, 291, 458, 11, 286, 11, 286, 1029, 291,
  1689, 257, 10476, 11, 1767, 13, 51536], "temperature": 0.0, "avg_logprob": -0.15423403845893013,
  "compression_ratio": 1.6866359447004609, "no_speech_prob": 0.0013247025199234486},
  {"id": 590, "seek": 368376, "start": 3683.92, "end": 3691.84, "text": " If you are
  a nonprofit charity, um, or just using it, you''re a student, um, or you just have
  a", "tokens": [50372, 759, 291, 366, 257, 23348, 16863, 11, 1105, 11, 420, 445,
  1228, 309, 11, 291, 434, 257, 3107, 11, 1105, 11, 420, 291, 445, 362, 257, 50768],
  "temperature": 0.0, "avg_logprob": -0.21080346540971237, "compression_ratio": 1.7300884955752212,
  "no_speech_prob": 0.0044619301334023476}, {"id": 591, "seek": 368376, "start": 3691.84,
  "end": 3696.96, "text": " side project, you''re messing around, you just want to
  get some vectors, go and install it, you know,", "tokens": [50768, 1252, 1716, 11,
  291, 434, 23258, 926, 11, 291, 445, 528, 281, 483, 512, 18875, 11, 352, 293, 3625,
  309, 11, 291, 458, 11, 51024], "temperature": 0.0, "avg_logprob": -0.21080346540971237,
  "compression_ratio": 1.7300884955752212, "no_speech_prob": 0.0044619301334023476},
  {"id": 592, "seek": 368376, "start": 3696.96, "end": 3701.1200000000003, "text":
  " don''t worry about it. Um, but if you put it in production and you''re, and you''re
  charging money for", "tokens": [51024, 500, 380, 3292, 466, 309, 13, 3301, 11, 457,
  498, 291, 829, 309, 294, 4265, 293, 291, 434, 11, 293, 291, 434, 11379, 1460, 337,
  51232], "temperature": 0.0, "avg_logprob": -0.21080346540971237, "compression_ratio":
  1.7300884955752212, "no_speech_prob": 0.0044619301334023476}, {"id": 593, "seek":
  368376, "start": 3701.1200000000003, "end": 3707.76, "text": " your product, then
  please, please buy a list. Yeah. Yeah. To have questions, Sign, um, how will", "tokens":
  [51232, 428, 1674, 11, 550, 1767, 11, 1767, 2256, 257, 1329, 13, 865, 13, 865, 13,
  1407, 362, 1651, 11, 13515, 11, 1105, 11, 577, 486, 51564], "temperature": 0.0,
  "avg_logprob": -0.21080346540971237, "compression_ratio": 1.7300884955752212, "no_speech_prob":
  0.0044619301334023476}, {"id": 594, "seek": 370776, "start": 3707.84, "end": 3713.1200000000003,
  "text": " you track who is using it for commercial and who is using it for a hobbyist
  project?", "tokens": [50368, 291, 2837, 567, 307, 1228, 309, 337, 6841, 293, 567,
  307, 1228, 309, 337, 257, 18240, 468, 1716, 30, 50632], "temperature": 0.0, "avg_logprob":
  -0.14765692220150844, "compression_ratio": 1.6380090497737556, "no_speech_prob":
  0.0018436595564708114}, {"id": 595, "seek": 370776, "start": 3713.92, "end": 3722.1600000000003,
  "text": " That''s a great question. And, and I don''t, I don''t track that. Um,
  I''m also, I''m really into", "tokens": [50672, 663, 311, 257, 869, 1168, 13, 400,
  11, 293, 286, 500, 380, 11, 286, 500, 380, 2837, 300, 13, 3301, 11, 286, 478, 611,
  11, 286, 478, 534, 666, 51084], "temperature": 0.0, "avg_logprob": -0.14765692220150844,
  "compression_ratio": 1.6380090497737556, "no_speech_prob": 0.0018436595564708114},
  {"id": 596, "seek": 370776, "start": 3723.2000000000003, "end": 3729.1200000000003,
  "text": " uh, privacy and safety on the web. So I don''t like the idea of like putting
  in a whole bunch of", "tokens": [51136, 2232, 11, 11427, 293, 4514, 322, 264, 3670,
  13, 407, 286, 500, 380, 411, 264, 1558, 295, 411, 3372, 294, 257, 1379, 3840, 295,
  51432], "temperature": 0.0, "avg_logprob": -0.14765692220150844, "compression_ratio":
  1.6380090497737556, "no_speech_prob": 0.0018436595564708114}, {"id": 597, "seek":
  370776, "start": 3729.1200000000003, "end": 3735.0400000000004, "text": " tracking
  into lemon tree. Um, I think that''s a terrible way to run a product these days.",
  "tokens": [51432, 11603, 666, 11356, 4230, 13, 3301, 11, 286, 519, 300, 311, 257,
  6237, 636, 281, 1190, 257, 1674, 613, 1708, 13, 51728], "temperature": 0.0, "avg_logprob":
  -0.14765692220150844, "compression_ratio": 1.6380090497737556, "no_speech_prob":
  0.0018436595564708114}, {"id": 598, "seek": 373504, "start": 3735.04, "end": 3745.84,
  "text": " Um, I, the only thing it does is I, uh, have it ask when it first starts
  up, it just asks the server", "tokens": [50364, 3301, 11, 286, 11, 264, 787, 551,
  309, 775, 307, 286, 11, 2232, 11, 362, 309, 1029, 562, 309, 700, 3719, 493, 11,
  309, 445, 8962, 264, 7154, 50904], "temperature": 0.0, "avg_logprob": -0.13559315347263956,
  "compression_ratio": 1.6569037656903767, "no_speech_prob": 0.0042787641286849976},
  {"id": 599, "seek": 373504, "start": 3745.84, "end": 3751.6, "text": " for what
  the latest version is. And it''ll tell you if there''s a new version. So with that,
  I see,", "tokens": [50904, 337, 437, 264, 6792, 3037, 307, 13, 400, 309, 603, 980,
  291, 498, 456, 311, 257, 777, 3037, 13, 407, 365, 300, 11, 286, 536, 11, 51192],
  "temperature": 0.0, "avg_logprob": -0.13559315347263956, "compression_ratio": 1.6569037656903767,
  "no_speech_prob": 0.0042787641286849976}, {"id": 600, "seek": 373504, "start": 3751.6,
  "end": 3758.72, "text": " I see that, um, okay, the, you know, somebody asked for
  a new version. Uh, and I anonymize all the", "tokens": [51192, 286, 536, 300, 11,
  1105, 11, 1392, 11, 264, 11, 291, 458, 11, 2618, 2351, 337, 257, 777, 3037, 13,
  4019, 11, 293, 286, 37293, 1125, 439, 264, 51548], "temperature": 0.0, "avg_logprob":
  -0.13559315347263956, "compression_ratio": 1.6569037656903767, "no_speech_prob":
  0.0042787641286849976}, {"id": 601, "seek": 373504, "start": 3758.72, "end": 3763.92,
  "text": " IP addresses. So I don''t even know who, like, there''s nothing. There''s
  no user information at all.", "tokens": [51548, 8671, 16862, 13, 407, 286, 500,
  380, 754, 458, 567, 11, 411, 11, 456, 311, 1825, 13, 821, 311, 572, 4195, 1589,
  412, 439, 13, 51808], "temperature": 0.0, "avg_logprob": -0.13559315347263956, "compression_ratio":
  1.6569037656903767, "no_speech_prob": 0.0042787641286849976}, {"id": 602, "seek":
  376392, "start": 3763.92, "end": 3769.92, "text": " So I just use that to kind of
  track, um, how often it starts. And it''s, I, I see like maybe,", "tokens": [50364,
  407, 286, 445, 764, 300, 281, 733, 295, 2837, 11, 1105, 11, 577, 2049, 309, 3719,
  13, 400, 309, 311, 11, 286, 11, 286, 536, 411, 1310, 11, 50664], "temperature":
  0.0, "avg_logprob": -0.13836362806417174, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.00038933835458010435}, {"id": 603, "seek": 376392, "start":
  3771.04, "end": 3780.8, "text": " maybe five downloads a day, um, right now. That''s
  what I do. So if, if you''re running it,", "tokens": [50720, 1310, 1732, 36553,
  257, 786, 11, 1105, 11, 558, 586, 13, 663, 311, 437, 286, 360, 13, 407, 498, 11,
  498, 291, 434, 2614, 309, 11, 51208], "temperature": 0.0, "avg_logprob": -0.13836362806417174,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.00038933835458010435},
  {"id": 604, "seek": 376392, "start": 3780.8, "end": 3787.28, "text": " you''re for
  pirating it, I can''t stop you. Uh, spending my time trying to stop you. Uh, it''s
  not,", "tokens": [51208, 291, 434, 337, 13528, 990, 309, 11, 286, 393, 380, 1590,
  291, 13, 4019, 11, 6434, 452, 565, 1382, 281, 1590, 291, 13, 4019, 11, 309, 311,
  406, 11, 51532], "temperature": 0.0, "avg_logprob": -0.13836362806417174, "compression_ratio":
  1.631578947368421, "no_speech_prob": 0.00038933835458010435}, {"id": 605, "seek":
  376392, "start": 3787.28, "end": 3792.08, "text": " it''s not worth my energy. Yeah.
  And I''d much rather, uh, I''d much rather work with teams who", "tokens": [51532,
  309, 311, 406, 3163, 452, 2281, 13, 865, 13, 400, 286, 1116, 709, 2831, 11, 2232,
  11, 286, 1116, 709, 2831, 589, 365, 5491, 567, 51772], "temperature": 0.0, "avg_logprob":
  -0.13836362806417174, "compression_ratio": 1.631578947368421, "no_speech_prob":
  0.00038933835458010435}, {"id": 606, "seek": 379208, "start": 3792.08, "end": 3796.16,
  "text": " really want to gain something. So if you do buy a license, I''ll work
  with you on setting it up", "tokens": [50364, 534, 528, 281, 6052, 746, 13, 407,
  498, 291, 360, 2256, 257, 10476, 11, 286, 603, 589, 365, 291, 322, 3287, 309, 493,
  50568], "temperature": 0.0, "avg_logprob": -0.10490030914772558, "compression_ratio":
  1.8452830188679246, "no_speech_prob": 0.0010457357857376337}, {"id": 607, "seek":
  379208, "start": 3796.16, "end": 3802.4, "text": " and telling you how to use it
  and working it and working on it with you. Um, it''s not advertised,", "tokens":
  [50568, 293, 3585, 291, 577, 281, 764, 309, 293, 1364, 309, 293, 1364, 322, 309,
  365, 291, 13, 3301, 11, 309, 311, 406, 42310, 11, 50880], "temperature": 0.0, "avg_logprob":
  -0.10490030914772558, "compression_ratio": 1.8452830188679246, "no_speech_prob":
  0.0010457357857376337}, {"id": 608, "seek": 379208, "start": 3802.4, "end": 3809.2,
  "text": " but around model inference itself, I''m happy to, uh, offer services,
  uh, to get your model up and", "tokens": [50880, 457, 926, 2316, 38253, 2564, 11,
  286, 478, 2055, 281, 11, 2232, 11, 2626, 3328, 11, 2232, 11, 281, 483, 428, 2316,
  493, 293, 51220], "temperature": 0.0, "avg_logprob": -0.10490030914772558, "compression_ratio":
  1.8452830188679246, "no_speech_prob": 0.0010457357857376337}, {"id": 609, "seek":
  379208, "start": 3809.2, "end": 3814.3199999999997, "text": " running and making
  sure that it''s running optimally, um, even doing a model conversion with you,",
  "tokens": [51220, 2614, 293, 1455, 988, 300, 309, 311, 2614, 5028, 379, 11, 1105,
  11, 754, 884, 257, 2316, 14298, 365, 291, 11, 51476], "temperature": 0.0, "avg_logprob":
  -0.10490030914772558, "compression_ratio": 1.8452830188679246, "no_speech_prob":
  0.0010457357857376337}, {"id": 610, "seek": 379208, "start": 3814.3199999999997,
  "end": 3821.2, "text": " setting you, setting you up for that stuff. Um, but that''s,
  that''s not advertised. It does say, like,", "tokens": [51476, 3287, 291, 11, 3287,
  291, 493, 337, 300, 1507, 13, 3301, 11, 457, 300, 311, 11, 300, 311, 406, 42310,
  13, 467, 775, 584, 11, 411, 11, 51820], "temperature": 0.0, "avg_logprob": -0.10490030914772558,
  "compression_ratio": 1.8452830188679246, "no_speech_prob": 0.0010457357857376337},
  {"id": 611, "seek": 382120, "start": 3821.6, "end": 3826.08, "text": " I''ll spend
  an hour with you if you buy a subscription to get you set up, but if you need more
  help", "tokens": [50384, 286, 603, 3496, 364, 1773, 365, 291, 498, 291, 2256, 257,
  17231, 281, 483, 291, 992, 493, 11, 457, 498, 291, 643, 544, 854, 50608], "temperature":
  0.0, "avg_logprob": -0.14842058577627507, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.0005218836013227701}, {"id": 612, "seek": 382120, "start": 3826.08,
  "end": 3834.0, "text": " than that, you know, let me know. Uh, now there''s another
  tier, which is like, if you''re Amazon,", "tokens": [50608, 813, 300, 11, 291, 458,
  11, 718, 385, 458, 13, 4019, 11, 586, 456, 311, 1071, 12362, 11, 597, 307, 411,
  11, 498, 291, 434, 6795, 11, 51004], "temperature": 0.0, "avg_logprob": -0.14842058577627507,
  "compression_ratio": 1.608695652173913, "no_speech_prob": 0.0005218836013227701},
  {"id": 613, "seek": 382120, "start": 3834.72, "end": 3839.2, "text": " Amazon would
  never buy my, they have their own world. But if you''re like a cloud provider,",
  "tokens": [51040, 6795, 576, 1128, 2256, 452, 11, 436, 362, 641, 1065, 1002, 13,
  583, 498, 291, 434, 411, 257, 4588, 12398, 11, 51264], "temperature": 0.0, "avg_logprob":
  -0.14842058577627507, "compression_ratio": 1.608695652173913, "no_speech_prob":
  0.0005218836013227701}, {"id": 614, "seek": 382120, "start": 3839.2, "end": 3844.96,
  "text": " or if you want to offer it as an API, that it doesn''t count because it''s,
  it''s per,", "tokens": [51264, 420, 498, 291, 528, 281, 2626, 309, 382, 364, 9362,
  11, 300, 309, 1177, 380, 1207, 570, 309, 311, 11, 309, 311, 680, 11, 51552], "temperature":
  0.0, "avg_logprob": -0.14842058577627507, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.0005218836013227701}, {"id": 615, "seek": 384496, "start": 3845.92,
  "end": 3852.88, "text": " it''s per product that I sell the license for. So if you
  are selling it as a cloud provider,", "tokens": [50412, 309, 311, 680, 1674, 300,
  286, 3607, 264, 10476, 337, 13, 407, 498, 291, 366, 6511, 309, 382, 257, 4588, 12398,
  11, 50760], "temperature": 0.0, "avg_logprob": -0.1285796598954634, "compression_ratio":
  1.5836909871244635, "no_speech_prob": 0.00031709924223832786}, {"id": 616, "seek":
  384496, "start": 3852.88, "end": 3858.4, "text": " or as an API, and you''ve got
  like a thousand clients that are now using my money, well, I,", "tokens": [50760,
  420, 382, 364, 9362, 11, 293, 291, 600, 658, 411, 257, 4714, 6982, 300, 366, 586,
  1228, 452, 1460, 11, 731, 11, 286, 11, 51036], "temperature": 0.0, "avg_logprob":
  -0.1285796598954634, "compression_ratio": 1.5836909871244635, "no_speech_prob":
  0.00031709924223832786}, {"id": 617, "seek": 384496, "start": 3858.4, "end": 3865.84,
  "text": " I actually count all of those clients as a mighty user. So I don''t have
  a price published,", "tokens": [51036, 286, 767, 1207, 439, 295, 729, 6982, 382,
  257, 21556, 4195, 13, 407, 286, 500, 380, 362, 257, 3218, 6572, 11, 51408], "temperature":
  0.0, "avg_logprob": -0.1285796598954634, "compression_ratio": 1.5836909871244635,
  "no_speech_prob": 0.00031709924223832786}, {"id": 618, "seek": 384496, "start":
  3865.84, "end": 3871.28, "text": " but if you have that situation, I''m not going
  to charge you 99 dollars a month for each client.", "tokens": [51408, 457, 498,
  291, 362, 300, 2590, 11, 286, 478, 406, 516, 281, 4602, 291, 11803, 3808, 257, 1618,
  337, 1184, 6423, 13, 51680], "temperature": 0.0, "avg_logprob": -0.1285796598954634,
  "compression_ratio": 1.5836909871244635, "no_speech_prob": 0.00031709924223832786},
  {"id": 619, "seek": 387128, "start": 3871.28, "end": 3876.1600000000003, "text":
  " That''s that, that, you know, if you''re running that type of business, contact
  me and we''ll work,", "tokens": [50364, 663, 311, 300, 11, 300, 11, 291, 458, 11,
  498, 291, 434, 2614, 300, 2010, 295, 1606, 11, 3385, 385, 293, 321, 603, 589, 11,
  50608], "temperature": 0.0, "avg_logprob": -0.1755919683547247, "compression_ratio":
  1.606837606837607, "no_speech_prob": 0.010349803604185581}, {"id": 620, "seek":
  387128, "start": 3876.1600000000003, "end": 3881.6800000000003, "text": " we''ll
  work something out. Yeah, that''s perfect. I mean, sounds like a solid model. I
  mean,", "tokens": [50608, 321, 603, 589, 746, 484, 13, 865, 11, 300, 311, 2176,
  13, 286, 914, 11, 3263, 411, 257, 5100, 2316, 13, 286, 914, 11, 50884], "temperature":
  0.0, "avg_logprob": -0.1755919683547247, "compression_ratio": 1.606837606837607,
  "no_speech_prob": 0.010349803604185581}, {"id": 621, "seek": 387128, "start": 3881.6800000000003,
  "end": 3887.44, "text": " for the start, for sure. And another like favorite question
  I have, and I''ve been asking this question", "tokens": [50884, 337, 264, 722, 11,
  337, 988, 13, 400, 1071, 411, 2954, 1168, 286, 362, 11, 293, 286, 600, 668, 3365,
  341, 1168, 51172], "temperature": 0.0, "avg_logprob": -0.1755919683547247, "compression_ratio":
  1.606837606837607, "no_speech_prob": 0.010349803604185581}, {"id": 622, "seek":
  387128, "start": 3887.44, "end": 3895.6800000000003, "text": " also to open source
  players like VV8, um, and I think quadrant. Um, so basically, um,", "tokens": [51172,
  611, 281, 1269, 4009, 4150, 411, 691, 53, 23, 11, 1105, 11, 293, 286, 519, 46856,
  13, 3301, 11, 370, 1936, 11, 1105, 11, 51584], "temperature": 0.0, "avg_logprob":
  -0.1755919683547247, "compression_ratio": 1.606837606837607, "no_speech_prob": 0.010349803604185581},
  {"id": 623, "seek": 389568, "start": 3896.64, "end": 3903.2, "text": " have you
  thought, you know, one way of kind of building that connection that may yield a
  business", "tokens": [50412, 362, 291, 1194, 11, 291, 458, 11, 472, 636, 295, 733,
  295, 2390, 300, 4984, 300, 815, 11257, 257, 1606, 50740], "temperature": 0.0, "avg_logprob":
  -0.13726764029644906, "compression_ratio": 1.6182572614107884, "no_speech_prob":
  0.002891132840886712}, {"id": 624, "seek": 389568, "start": 3903.2, "end": 3909.3599999999997,
  "text": " case for you is what you just explained, right? So somebody buys a license
  and then you scale with", "tokens": [50740, 1389, 337, 291, 307, 437, 291, 445,
  8825, 11, 558, 30, 407, 2618, 28153, 257, 10476, 293, 550, 291, 4373, 365, 51048],
  "temperature": 0.0, "avg_logprob": -0.13726764029644906, "compression_ratio": 1.6182572614107884,
  "no_speech_prob": 0.002891132840886712}, {"id": 625, "seek": 389568, "start": 3909.3599999999997,
  "end": 3914.64, "text": " them, you explain how to make it better, how to tune it,
  maybe implement some features. Another", "tokens": [51048, 552, 11, 291, 2903, 577,
  281, 652, 309, 1101, 11, 577, 281, 10864, 309, 11, 1310, 4445, 512, 4122, 13, 3996,
  51312], "temperature": 0.0, "avg_logprob": -0.13726764029644906, "compression_ratio":
  1.6182572614107884, "no_speech_prob": 0.002891132840886712}, {"id": 626, "seek":
  389568, "start": 3914.64, "end": 3921.2799999999997, "text": " route is to open
  a Slack channel or Discord, whatever. And, you know, invite users there and then",
  "tokens": [51312, 7955, 307, 281, 1269, 257, 37211, 2269, 420, 32623, 11, 2035,
  13, 400, 11, 291, 458, 11, 7980, 5022, 456, 293, 550, 51644], "temperature": 0.0,
  "avg_logprob": -0.13726764029644906, "compression_ratio": 1.6182572614107884, "no_speech_prob":
  0.002891132840886712}, {"id": 627, "seek": 392128, "start": 3921.28, "end": 3926.0,
  "text": " start talking to them. And maybe you''ll have some open source components
  as well at some point,", "tokens": [50364, 722, 1417, 281, 552, 13, 400, 1310, 291,
  603, 362, 512, 1269, 4009, 6677, 382, 731, 412, 512, 935, 11, 50600], "temperature":
  0.0, "avg_logprob": -0.10573368687783519, "compression_ratio": 1.6198347107438016,
  "no_speech_prob": 0.0014794785529375076}, {"id": 628, "seek": 392128, "start": 3926.0,
  "end": 3931.2000000000003, "text": " you know, I don''t know a tool that helps me
  to convert my model into representation that might", "tokens": [50600, 291, 458,
  11, 286, 500, 380, 458, 257, 2290, 300, 3665, 385, 281, 7620, 452, 2316, 666, 10290,
  300, 1062, 50860], "temperature": 0.0, "avg_logprob": -0.10573368687783519, "compression_ratio":
  1.6198347107438016, "no_speech_prob": 0.0014794785529375076}, {"id": 629, "seek":
  392128, "start": 3931.2000000000003, "end": 3938.8, "text": " you can read. Um,
  have you considered also taking that open source route as one way of building",
  "tokens": [50860, 291, 393, 1401, 13, 3301, 11, 362, 291, 4888, 611, 1940, 300,
  1269, 4009, 7955, 382, 472, 636, 295, 2390, 51240], "temperature": 0.0, "avg_logprob":
  -0.10573368687783519, "compression_ratio": 1.6198347107438016, "no_speech_prob":
  0.0014794785529375076}, {"id": 630, "seek": 392128, "start": 3938.8, "end": 3946.5600000000004,
  "text": " that community of some of which will be your users and paying customers?
  Uh, great question. I don''t have", "tokens": [51240, 300, 1768, 295, 512, 295,
  597, 486, 312, 428, 5022, 293, 6229, 4581, 30, 4019, 11, 869, 1168, 13, 286, 500,
  380, 362, 51628], "temperature": 0.0, "avg_logprob": -0.10573368687783519, "compression_ratio":
  1.6198347107438016, "no_speech_prob": 0.0014794785529375076}, {"id": 631, "seek":
  394656, "start": 3947.2, "end": 3955.2, "text": " a, I don''t have a Slack, I don''t
  have a Slack myself. Um, I''m a member in many other slacks.", "tokens": [50396,
  257, 11, 286, 500, 380, 362, 257, 37211, 11, 286, 500, 380, 362, 257, 37211, 2059,
  13, 3301, 11, 286, 478, 257, 4006, 294, 867, 661, 1061, 7424, 13, 50796], "temperature":
  0.0, "avg_logprob": -0.1792139350821119, "compression_ratio": 1.7454545454545454,
  "no_speech_prob": 0.0023044534027576447}, {"id": 632, "seek": 394656, "start": 3956.08,
  "end": 3962.72, "text": " I could set up a Discord, I''m on Discord, um, mostly
  just for the ML ops community in Discord.", "tokens": [50840, 286, 727, 992, 493,
  257, 32623, 11, 286, 478, 322, 32623, 11, 1105, 11, 5240, 445, 337, 264, 21601,
  44663, 1768, 294, 32623, 13, 51172], "temperature": 0.0, "avg_logprob": -0.1792139350821119,
  "compression_ratio": 1.7454545454545454, "no_speech_prob": 0.0023044534027576447},
  {"id": 633, "seek": 394656, "start": 3963.68, "end": 3968.64, "text": " But I could
  just start like a thread or a channel in that. I don''t know if mighty itself needs
  its", "tokens": [51220, 583, 286, 727, 445, 722, 411, 257, 7207, 420, 257, 2269,
  294, 300, 13, 286, 500, 380, 458, 498, 21556, 2564, 2203, 1080, 51468], "temperature":
  0.0, "avg_logprob": -0.1792139350821119, "compression_ratio": 1.7454545454545454,
  "no_speech_prob": 0.0023044534027576447}, {"id": 634, "seek": 394656, "start": 3968.64,
  "end": 3975.68, "text": " own Slack by itself. Um, I think it''s more of a community.
  It would be part of another community.", "tokens": [51468, 1065, 37211, 538, 2564,
  13, 3301, 11, 286, 519, 309, 311, 544, 295, 257, 1768, 13, 467, 576, 312, 644, 295,
  1071, 1768, 13, 51820], "temperature": 0.0, "avg_logprob": -0.1792139350821119,
  "compression_ratio": 1.7454545454545454, "no_speech_prob": 0.0023044534027576447},
  {"id": 635, "seek": 397656, "start": 3977.2, "end": 3981.44, "text": " One of the,
  one of the annoying things for me is I have to go and join like 12 million slacks",
  "tokens": [50396, 1485, 295, 264, 11, 472, 295, 264, 11304, 721, 337, 385, 307,
  286, 362, 281, 352, 293, 3917, 411, 2272, 2459, 1061, 7424, 50608], "temperature":
  0.0, "avg_logprob": -0.1495165475984899, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.0019218268571421504}, {"id": 636, "seek": 397656, "start": 3981.44,
  "end": 3985.52, "text": " because everybody has their own Slack and it doesn''t
  work with one another. Discord does that", "tokens": [50608, 570, 2201, 575, 641,
  1065, 37211, 293, 309, 1177, 380, 589, 365, 472, 1071, 13, 32623, 775, 300, 50812],
  "temperature": 0.0, "avg_logprob": -0.1495165475984899, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.0019218268571421504}, {"id": 637, "seek": 397656, "start": 3985.52,
  "end": 3991.68, "text": " way better. Slack, we got to have words. Um, you got to
  make it easier. I have like four email", "tokens": [50812, 636, 1101, 13, 37211,
  11, 321, 658, 281, 362, 2283, 13, 3301, 11, 291, 658, 281, 652, 309, 3571, 13, 286,
  362, 411, 1451, 3796, 51120], "temperature": 0.0, "avg_logprob": -0.1495165475984899,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.0019218268571421504},
  {"id": 638, "seek": 397656, "start": 3991.68, "end": 3997.12, "text": " addresses
  or five email addresses across like 12 different slacks right now. I can''t keep
  track of", "tokens": [51120, 16862, 420, 1732, 3796, 16862, 2108, 411, 2272, 819,
  1061, 7424, 558, 586, 13, 286, 393, 380, 1066, 2837, 295, 51392], "temperature":
  0.0, "avg_logprob": -0.1495165475984899, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.0019218268571421504}, {"id": 639, "seek": 397656, "start": 3997.12,
  "end": 4003.04, "text": " them. Um, but in terms of open, of open source, I already
  have a bunch of open source projects. So", "tokens": [51392, 552, 13, 3301, 11,
  457, 294, 2115, 295, 1269, 11, 295, 1269, 4009, 11, 286, 1217, 362, 257, 3840, 295,
  1269, 4009, 4455, 13, 407, 51688], "temperature": 0.0, "avg_logprob": -0.1495165475984899,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.0019218268571421504},
  {"id": 640, "seek": 400304, "start": 4004.0, "end": 4015.84, "text": " uh, there
  is, um, max.io but spelled out, M-A-X-D-O-T-I-O on GitHub. Somebody already took
  max-io.", "tokens": [50412, 2232, 11, 456, 307, 11, 1105, 11, 11469, 13, 1004, 457,
  34388, 484, 11, 376, 12, 32, 12, 55, 12, 35, 12, 46, 12, 51, 12, 40, 12, 46, 322,
  23331, 13, 13463, 1217, 1890, 11469, 12, 1004, 13, 51004], "temperature": 0.0, "avg_logprob":
  -0.22393798828125, "compression_ratio": 1.3923444976076556, "no_speech_prob": 0.0030506616458296776},
  {"id": 641, "seek": 400304, "start": 4015.84, "end": 4024.0, "text": " We can''t
  have dots in GitHub names. Um, that''s fine. You know, names or names. Uh, so there''s
  mighty", "tokens": [51004, 492, 393, 380, 362, 15026, 294, 23331, 5288, 13, 3301,
  11, 300, 311, 2489, 13, 509, 458, 11, 5288, 420, 5288, 13, 4019, 11, 370, 456, 311,
  21556, 51412], "temperature": 0.0, "avg_logprob": -0.22393798828125, "compression_ratio":
  1.3923444976076556, "no_speech_prob": 0.0030506616458296776}, {"id": 642, "seek":
  400304, "start": 4024.0, "end": 4029.04, "text": " convert, which I actually, I''m
  working on updating that because it''s based on, um, optimum,", "tokens": [51412,
  7620, 11, 597, 286, 767, 11, 286, 478, 1364, 322, 25113, 300, 570, 309, 311, 2361,
  322, 11, 1105, 11, 39326, 11, 51664], "temperature": 0.0, "avg_logprob": -0.22393798828125,
  "compression_ratio": 1.3923444976076556, "no_speech_prob": 0.0030506616458296776},
  {"id": 643, "seek": 402904, "start": 4029.04, "end": 4034.8, "text": " which is
  a hugging-face repository that does model conversion. It''s a very light wrapper
  around", "tokens": [50364, 597, 307, 257, 41706, 12, 2868, 25841, 300, 775, 2316,
  14298, 13, 467, 311, 257, 588, 1442, 46906, 926, 50652], "temperature": 0.0, "avg_logprob":
  -0.13433128244736614, "compression_ratio": 1.6081632653061224, "no_speech_prob":
  0.0006002169102430344}, {"id": 644, "seek": 402904, "start": 4035.84, "end": 4044.08,
  "text": " optimum. It basically just converts the model for you, uh, bundles the
  tokenizer and a configuration.", "tokens": [50704, 39326, 13, 467, 1936, 445, 38874,
  264, 2316, 337, 291, 11, 2232, 11, 13882, 904, 264, 14862, 6545, 293, 257, 11694,
  13, 51116], "temperature": 0.0, "avg_logprob": -0.13433128244736614, "compression_ratio":
  1.6081632653061224, "no_speech_prob": 0.0006002169102430344}, {"id": 645, "seek":
  402904, "start": 4044.08, "end": 4049.2799999999997, "text": " That''s it. Uh, it''s
  pretty straightforward. Um, you can do that yourself. You don''t have to use that.",
  "tokens": [51116, 663, 311, 309, 13, 4019, 11, 309, 311, 1238, 15325, 13, 3301,
  11, 291, 393, 360, 300, 1803, 13, 509, 500, 380, 362, 281, 764, 300, 13, 51376],
  "temperature": 0.0, "avg_logprob": -0.13433128244736614, "compression_ratio": 1.6081632653061224,
  "no_speech_prob": 0.0006002169102430344}, {"id": 646, "seek": 402904, "start": 4049.84,
  "end": 4055.92, "text": " So that, but that''s open source. Um, there''s also mighty
  batch, which is a node program, which", "tokens": [51404, 407, 300, 11, 457, 300,
  311, 1269, 4009, 13, 3301, 11, 456, 311, 611, 21556, 15245, 11, 597, 307, 257, 9984,
  1461, 11, 597, 51708], "temperature": 0.0, "avg_logprob": -0.13433128244736614,
  "compression_ratio": 1.6081632653061224, "no_speech_prob": 0.0006002169102430344},
  {"id": 647, "seek": 405592, "start": 4056.7200000000003, "end": 4062.0, "text":
  " is a way to do, uh, concurrent batch processing of documents,", "tokens": [50404,
  307, 257, 636, 281, 360, 11, 2232, 11, 37702, 15245, 9007, 295, 8512, 11, 50668],
  "temperature": 0.0, "avg_logprob": -0.17158190863473075, "compression_ratio": 1.5029239766081872,
  "no_speech_prob": 0.0006857871194370091}, {"id": 648, "seek": 405592, "start": 4062.56,
  "end": 4073.2000000000003, "text": " into vectors, pointing it at a mighty server.
  Um, that''s best described in the blog post that I wrote", "tokens": [50696, 666,
  18875, 11, 12166, 309, 412, 257, 21556, 7154, 13, 3301, 11, 300, 311, 1151, 7619,
  294, 264, 6968, 2183, 300, 286, 4114, 51228], "temperature": 0.0, "avg_logprob":
  -0.17158190863473075, "compression_ratio": 1.5029239766081872, "no_speech_prob":
  0.0006857871194370091}, {"id": 649, "seek": 405592, "start": 4073.2000000000003,
  "end": 4078.64, "text": " and how that works, um, about, you know, the, the blog
  post being, uh, converting the code of", "tokens": [51228, 293, 577, 300, 1985,
  11, 1105, 11, 466, 11, 291, 458, 11, 264, 11, 264, 6968, 2183, 885, 11, 2232, 11,
  29942, 264, 3089, 295, 51500], "temperature": 0.0, "avg_logprob": -0.17158190863473075,
  "compression_ratio": 1.5029239766081872, "no_speech_prob": 0.0006857871194370091},
  {"id": 650, "seek": 407864, "start": 4078.64, "end": 4087.52, "text": " federal
  regulations. Um, that''s on, it''s on the homepage of max.io. And, uh, there''s
  also a bunch of", "tokens": [50364, 6019, 12563, 13, 3301, 11, 300, 311, 322, 11,
  309, 311, 322, 264, 31301, 295, 11469, 13, 1004, 13, 400, 11, 2232, 11, 456, 311,
  611, 257, 3840, 295, 50808], "temperature": 0.0, "avg_logprob": -0.1253059442760875,
  "compression_ratio": 1.625531914893617, "no_speech_prob": 0.00027877523098140955},
  {"id": 651, "seek": 407864, "start": 4087.52, "end": 4092.4, "text": " other open
  source projects that I haven''t talked about yet. So there''s now node mighty, which
  is", "tokens": [50808, 661, 1269, 4009, 4455, 300, 286, 2378, 380, 2825, 466, 1939,
  13, 407, 456, 311, 586, 9984, 21556, 11, 597, 307, 51052], "temperature": 0.0, "avg_logprob":
  -0.1253059442760875, "compression_ratio": 1.625531914893617, "no_speech_prob": 0.00027877523098140955},
  {"id": 652, "seek": 407864, "start": 4092.4, "end": 4098.8, "text": " basically
  just an API client for node that will talk to mighty, um, it does connection pooling.",
  "tokens": [51052, 1936, 445, 364, 9362, 6423, 337, 9984, 300, 486, 751, 281, 21556,
  11, 1105, 11, 309, 775, 4984, 7005, 278, 13, 51372], "temperature": 0.0, "avg_logprob":
  -0.1253059442760875, "compression_ratio": 1.625531914893617, "no_speech_prob": 0.00027877523098140955},
  {"id": 653, "seek": 407864, "start": 4098.8, "end": 4104.639999999999, "text": "
  So if you have like four mighty, four mighty cores running, it''ll talk to all the,
  it''ll", "tokens": [51372, 407, 498, 291, 362, 411, 1451, 21556, 11, 1451, 21556,
  24826, 2614, 11, 309, 603, 751, 281, 439, 264, 11, 309, 603, 51664], "temperature":
  0.0, "avg_logprob": -0.1253059442760875, "compression_ratio": 1.625531914893617,
  "no_speech_prob": 0.00027877523098140955}, {"id": 654, "seek": 410464, "start":
  4104.64, "end": 4109.92, "text": " negotiate which core to use, um, when it makes
  a call. So that''s really easy to use in like an express", "tokens": [50364, 21713,
  597, 4965, 281, 764, 11, 1105, 11, 562, 309, 1669, 257, 818, 13, 407, 300, 311,
  534, 1858, 281, 764, 294, 411, 364, 5109, 50628], "temperature": 0.0, "avg_logprob":
  -0.12416741583082411, "compression_ratio": 1.6040816326530611, "no_speech_prob":
  0.000273947196546942}, {"id": 655, "seek": 410464, "start": 4109.92, "end": 4116.88,
  "text": " server. Um, I also wrote two other node modules while I was at it, uh,
  that aren''t from mighty,", "tokens": [50628, 7154, 13, 3301, 11, 286, 611, 4114,
  732, 661, 9984, 16679, 1339, 286, 390, 412, 309, 11, 2232, 11, 300, 3212, 380, 490,
  21556, 11, 50976], "temperature": 0.0, "avg_logprob": -0.12416741583082411, "compression_ratio":
  1.6040816326530611, "no_speech_prob": 0.000273947196546942}, {"id": 656, "seek":
  410464, "start": 4116.88, "end": 4122.320000000001, "text": " but I wrote node quadrant.
  So now there''s a node client for, for the quadrant vector database.", "tokens":
  [50976, 457, 286, 4114, 9984, 46856, 13, 407, 586, 456, 311, 257, 9984, 6423, 337,
  11, 337, 264, 46856, 8062, 8149, 13, 51248], "temperature": 0.0, "avg_logprob":
  -0.12416741583082411, "compression_ratio": 1.6040816326530611, "no_speech_prob":
  0.000273947196546942}, {"id": 657, "seek": 410464, "start": 4123.12, "end": 4131.68,
  "text": " And I told, uh, uh, I told the guys at quadrant that this exists. I''m
  trying to work on a blog post", "tokens": [51288, 400, 286, 1907, 11, 2232, 11,
  2232, 11, 286, 1907, 264, 1074, 412, 46856, 300, 341, 8198, 13, 286, 478, 1382,
  281, 589, 322, 257, 6968, 2183, 51716], "temperature": 0.0, "avg_logprob": -0.12416741583082411,
  "compression_ratio": 1.6040816326530611, "no_speech_prob": 0.000273947196546942},
  {"id": 658, "seek": 413168, "start": 4131.68, "end": 4136.4800000000005, "text":
  " out of an asset, I guess this is the announcement. Um, but I''ll, I''ll, I''ll
  publish something.", "tokens": [50364, 484, 295, 364, 11999, 11, 286, 2041, 341,
  307, 264, 12847, 13, 3301, 11, 457, 286, 603, 11, 286, 603, 11, 286, 603, 11374,
  746, 13, 50604], "temperature": 0.0, "avg_logprob": -0.1966743999057346, "compression_ratio":
  1.795539033457249, "no_speech_prob": 0.0013255112571641803}, {"id": 659, "seek":
  413168, "start": 4136.4800000000005, "end": 4142.72, "text": " There''s going to
  be a demo. I also wrote node pine cone. So well, it''s pine cone dash I.O. So now",
  "tokens": [50604, 821, 311, 516, 281, 312, 257, 10723, 13, 286, 611, 4114, 9984,
  15113, 19749, 13, 407, 731, 11, 309, 311, 15113, 19749, 8240, 286, 13, 46, 13, 407,
  586, 50916], "temperature": 0.0, "avg_logprob": -0.1966743999057346, "compression_ratio":
  1.795539033457249, "no_speech_prob": 0.0013255112571641803}, {"id": 660, "seek":
  413168, "start": 4142.72, "end": 4149.04, "text": " there''s a node JS integration
  into pine cone. So you can talk to pine cone from, from node from", "tokens": [50916,
  456, 311, 257, 9984, 33063, 10980, 666, 15113, 19749, 13, 407, 291, 393, 751, 281,
  15113, 19749, 490, 11, 490, 9984, 490, 51232], "temperature": 0.0, "avg_logprob":
  -0.1966743999057346, "compression_ratio": 1.795539033457249, "no_speech_prob": 0.0013255112571641803},
  {"id": 661, "seek": 413168, "start": 4149.04, "end": 4153.4400000000005, "text":
  " a kind of express server or something. Um, the guys at pine cone don''t know what
  that I wrote that", "tokens": [51232, 257, 733, 295, 5109, 7154, 420, 746, 13, 3301,
  11, 264, 1074, 412, 15113, 19749, 500, 380, 458, 437, 300, 286, 4114, 300, 51452],
  "temperature": 0.0, "avg_logprob": -0.1966743999057346, "compression_ratio": 1.795539033457249,
  "no_speech_prob": 0.0013255112571641803}, {"id": 662, "seek": 413168, "start": 4153.4400000000005,
  "end": 4160.8, "text": " yet because it wasn''t, I didn''t, I just put it out there.
  It''s on npm. Um, so I gotta, I gotta,", "tokens": [51452, 1939, 570, 309, 2067,
  380, 11, 286, 994, 380, 11, 286, 445, 829, 309, 484, 456, 13, 467, 311, 322, 297,
  14395, 13, 3301, 11, 370, 286, 3428, 11, 286, 3428, 11, 51820], "temperature": 0.0,
  "avg_logprob": -0.1966743999057346, "compression_ratio": 1.795539033457249, "no_speech_prob":
  0.0013255112571641803}, {"id": 663, "seek": 416080, "start": 4160.8, "end": 4164.56,
  "text": " I gotta work that out. And they might want it. If you guys, if you want
  this, you know, I,", "tokens": [50364, 286, 3428, 589, 300, 484, 13, 400, 436, 1062,
  528, 309, 13, 759, 291, 1074, 11, 498, 291, 528, 341, 11, 291, 458, 11, 286, 11,
  50552], "temperature": 0.0, "avg_logprob": -0.14496816387613312, "compression_ratio":
  1.7563636363636363, "no_speech_prob": 0.0006712747272104025}, {"id": 664, "seek":
  416080, "start": 4164.56, "end": 4169.4400000000005, "text": " I just wanted something
  that I could use, but it''s your name. So please take the, take the package", "tokens":
  [50552, 286, 445, 1415, 746, 300, 286, 727, 764, 11, 457, 309, 311, 428, 1315, 13,
  407, 1767, 747, 264, 11, 747, 264, 7372, 50796], "temperature": 0.0, "avg_logprob":
  -0.14496816387613312, "compression_ratio": 1.7563636363636363, "no_speech_prob":
  0.0006712747272104025}, {"id": 665, "seek": 416080, "start": 4169.4400000000005,
  "end": 4174.4800000000005, "text": " from me. If you don''t get upset that I used
  your name. Um, I just wanted a tool that I could use", "tokens": [50796, 490, 385,
  13, 759, 291, 500, 380, 483, 8340, 300, 286, 1143, 428, 1315, 13, 3301, 11, 286,
  445, 1415, 257, 2290, 300, 286, 727, 764, 51048], "temperature": 0.0, "avg_logprob":
  -0.14496816387613312, "compression_ratio": 1.7563636363636363, "no_speech_prob":
  0.0006712747272104025}, {"id": 666, "seek": 416080, "start": 4174.4800000000005,
  "end": 4180.4800000000005, "text": " for my own node JS testing. Um, but then this
  stuff integrates with, with mighty really easily. So", "tokens": [51048, 337, 452,
  1065, 9984, 33063, 4997, 13, 3301, 11, 457, 550, 341, 1507, 3572, 1024, 365, 11,
  365, 21556, 534, 3612, 13, 407, 51348], "temperature": 0.0, "avg_logprob": -0.14496816387613312,
  "compression_ratio": 1.7563636363636363, "no_speech_prob": 0.0006712747272104025},
  {"id": 667, "seek": 416080, "start": 4180.4800000000005, "end": 4184.4800000000005,
  "text": " I have all these node clients now and I''m fricking focusing, focusing
  on JavaScript first. So all", "tokens": [51348, 286, 362, 439, 613, 9984, 6982,
  586, 293, 286, 478, 431, 10401, 8416, 11, 8416, 322, 15778, 700, 13, 407, 439, 51548],
  "temperature": 0.0, "avg_logprob": -0.14496816387613312, "compression_ratio": 1.7563636363636363,
  "no_speech_prob": 0.0006712747272104025}, {"id": 668, "seek": 418448, "start": 4184.48,
  "end": 4189.839999999999, "text": " the stuff is going to be released. It''s already,
  it''s already up there. It''s on npm. It''s on my,", "tokens": [50364, 264, 1507,
  307, 516, 281, 312, 4736, 13, 467, 311, 1217, 11, 309, 311, 1217, 493, 456, 13,
  467, 311, 322, 297, 14395, 13, 467, 311, 322, 452, 11, 50632], "temperature": 0.0,
  "avg_logprob": -0.12790803909301757, "compression_ratio": 1.7048611111111112, "no_speech_prob":
  0.0005388341378420591}, {"id": 669, "seek": 418448, "start": 4189.839999999999,
  "end": 4196.959999999999, "text": " my GitHub. Uh, it''s, it''s free to use. It
  maybe needs a little bit more polish. I haven''t fully", "tokens": [50632, 452,
  23331, 13, 4019, 11, 309, 311, 11, 309, 311, 1737, 281, 764, 13, 467, 1310, 2203,
  257, 707, 857, 544, 20452, 13, 286, 2378, 380, 4498, 50988], "temperature": 0.0,
  "avg_logprob": -0.12790803909301757, "compression_ratio": 1.7048611111111112, "no_speech_prob":
  0.0005388341378420591}, {"id": 670, "seek": 418448, "start": 4196.959999999999,
  "end": 4202.639999999999, "text": " mapped out the APIs. I just mapped out the course
  stuff that I needed to do. So it doesn''t do things", "tokens": [50988, 33318, 484,
  264, 21445, 13, 286, 445, 33318, 484, 264, 1164, 1507, 300, 286, 2978, 281, 360,
  13, 407, 309, 1177, 380, 360, 721, 51272], "temperature": 0.0, "avg_logprob": -0.12790803909301757,
  "compression_ratio": 1.7048611111111112, "no_speech_prob": 0.0005388341378420591},
  {"id": 671, "seek": 418448, "start": 4202.639999999999, "end": 4207.599999999999,
  "text": " like the scroll command, you know, where you can scroll through all the
  points on quadrant. But I", "tokens": [51272, 411, 264, 11369, 5622, 11, 291, 458,
  11, 689, 291, 393, 11369, 807, 439, 264, 2793, 322, 46856, 13, 583, 286, 51520],
  "temperature": 0.0, "avg_logprob": -0.12790803909301757, "compression_ratio": 1.7048611111111112,
  "no_speech_prob": 0.0005388341378420591}, {"id": 672, "seek": 418448, "start": 4207.599999999999,
  "end": 4212.08, "text": " don''t know how much of a use for that is it''s really
  easy to add that. I just didn''t have the time.", "tokens": [51520, 500, 380, 458,
  577, 709, 295, 257, 764, 337, 300, 307, 309, 311, 534, 1858, 281, 909, 300, 13,
  286, 445, 994, 380, 362, 264, 565, 13, 51744], "temperature": 0.0, "avg_logprob":
  -0.12790803909301757, "compression_ratio": 1.7048611111111112, "no_speech_prob":
  0.0005388341378420591}, {"id": 673, "seek": 421208, "start": 4212.64, "end": 4218.64,
  "text": " So yeah, there''s, there''s a bunch of open source work that I''ve been
  doing. Um, I also want to", "tokens": [50392, 407, 1338, 11, 456, 311, 11, 456,
  311, 257, 3840, 295, 1269, 4009, 589, 300, 286, 600, 668, 884, 13, 3301, 11, 286,
  611, 528, 281, 50692], "temperature": 0.0, "avg_logprob": -0.16313892940305313,
  "compression_ratio": 1.7882882882882882, "no_speech_prob": 0.0008735001320019364},
  {"id": 674, "seek": 421208, "start": 4218.64, "end": 4227.84, "text": " mention
  I''m working on starter applications. So I have, I have right now, uh, basically
  it''s like a,", "tokens": [50692, 2152, 286, 478, 1364, 322, 22465, 5821, 13, 407,
  286, 362, 11, 286, 362, 558, 586, 11, 2232, 11, 1936, 309, 311, 411, 257, 11, 51152],
  "temperature": 0.0, "avg_logprob": -0.16313892940305313, "compression_ratio": 1.7882882882882882,
  "no_speech_prob": 0.0008735001320019364}, {"id": 675, "seek": 421208, "start": 4227.84,
  "end": 4235.28, "text": " it''s like a starter app that works with node and node
  mighty and quadrant. Um, and also node mighty", "tokens": [51152, 309, 311, 411,
  257, 22465, 724, 300, 1985, 365, 9984, 293, 9984, 21556, 293, 46856, 13, 3301, 11,
  293, 611, 9984, 21556, 51524], "temperature": 0.0, "avg_logprob": -0.16313892940305313,
  "compression_ratio": 1.7882882882882882, "no_speech_prob": 0.0008735001320019364},
  {"id": 676, "seek": 421208, "start": 4235.28, "end": 4241.28, "text": " and pine
  cone. I have two starter apps that aren''t released yet that I''m working on polishing
  up and,", "tokens": [51524, 293, 15113, 19749, 13, 286, 362, 732, 22465, 7733, 300,
  3212, 380, 4736, 1939, 300, 286, 478, 1364, 322, 47258, 493, 293, 11, 51824], "temperature":
  0.0, "avg_logprob": -0.16313892940305313, "compression_ratio": 1.7882882882882882,
  "no_speech_prob": 0.0008735001320019364}, {"id": 677, "seek": 424128, "start": 4241.28,
  "end": 4246.24, "text": " and getting out there where it''s where it''s really easy
  if you''re a node, if you''re a job script", "tokens": [50364, 293, 1242, 484, 456,
  689, 309, 311, 689, 309, 311, 534, 1858, 498, 291, 434, 257, 9984, 11, 498, 291,
  434, 257, 1691, 5755, 50612], "temperature": 0.0, "avg_logprob": -0.20601383209228516,
  "compression_ratio": 1.6244725738396624, "no_speech_prob": 0.0005491789197549224},
  {"id": 678, "seek": 424128, "start": 4246.24, "end": 4250.96, "text": " person to
  just take documents, convert them into vectors, load them into a vector database,",
  "tokens": [50612, 954, 281, 445, 747, 8512, 11, 7620, 552, 666, 18875, 11, 3677,
  552, 666, 257, 8062, 8149, 11, 50848], "temperature": 0.0, "avg_logprob": -0.20601383209228516,
  "compression_ratio": 1.6244725738396624, "no_speech_prob": 0.0005491789197549224},
  {"id": 679, "seek": 424128, "start": 4251.84, "end": 4260.719999999999, "text":
  " and have a search app running using them. Yeah, that''s fantastic. I mean, so
  much to unpack. And I", "tokens": [50892, 293, 362, 257, 3164, 724, 2614, 1228,
  552, 13, 865, 11, 300, 311, 5456, 13, 286, 914, 11, 370, 709, 281, 26699, 13, 400,
  286, 51336], "temperature": 0.0, "avg_logprob": -0.20601383209228516, "compression_ratio":
  1.6244725738396624, "no_speech_prob": 0.0005491789197549224}, {"id": 680, "seek":
  424128, "start": 4260.719999999999, "end": 4269.5199999999995, "text": " think this
  could be one of the like a we''re witnessing, um, a community written, uh, software
  for", "tokens": [51336, 519, 341, 727, 312, 472, 295, 264, 411, 257, 321, 434, 39233,
  11, 1105, 11, 257, 1768, 3720, 11, 2232, 11, 4722, 337, 51776], "temperature": 0.0,
  "avg_logprob": -0.20601383209228516, "compression_ratio": 1.6244725738396624, "no_speech_prob":
  0.0005491789197549224}, {"id": 681, "seek": 426952, "start": 4269.52, "end": 4275.76,
  "text": " a close software company. I mean, pine cone is a close software company,
  right? And we have an", "tokens": [50364, 257, 1998, 4722, 2237, 13, 286, 914, 11,
  15113, 19749, 307, 257, 1998, 4722, 2237, 11, 558, 30, 400, 321, 362, 364, 50676],
  "temperature": 0.0, "avg_logprob": -0.24457542494972154, "compression_ratio": 1.6375,
  "no_speech_prob": 0.0016823967453092337}, {"id": 682, "seek": 426952, "start": 4275.76,
  "end": 4283.360000000001, "text": " episode with Greg Kogan, who is a chief marketing
  marketing officer with pine cone. Um, we can connect", "tokens": [50676, 3500, 365,
  11490, 591, 21576, 11, 567, 307, 257, 9588, 6370, 6370, 8456, 365, 15113, 19749,
  13, 3301, 11, 321, 393, 1745, 51056], "temperature": 0.0, "avg_logprob": -0.24457542494972154,
  "compression_ratio": 1.6375, "no_speech_prob": 0.0016823967453092337}, {"id": 683,
  "seek": 426952, "start": 4283.360000000001, "end": 4288.96, "text": " you to and
  you can discuss the future. Yeah, I talked to Greg. You know, we''re working on
  some stuff.", "tokens": [51056, 291, 281, 293, 291, 393, 2248, 264, 2027, 13, 865,
  11, 286, 2825, 281, 11490, 13, 509, 458, 11, 321, 434, 1364, 322, 512, 1507, 13,
  51336], "temperature": 0.0, "avg_logprob": -0.24457542494972154, "compression_ratio":
  1.6375, "no_speech_prob": 0.0016823967453092337}, {"id": 684, "seek": 426952, "start":
  4290.320000000001, "end": 4295.92, "text": " But what, what, my question is what
  made you write those connectors? Like, did you think that", "tokens": [51404, 583,
  437, 11, 437, 11, 452, 1168, 307, 437, 1027, 291, 2464, 729, 31865, 30, 1743, 11,
  630, 291, 519, 300, 51684], "temperature": 0.0, "avg_logprob": -0.24457542494972154,
  "compression_ratio": 1.6375, "no_speech_prob": 0.0016823967453092337}, {"id": 685,
  "seek": 429592, "start": 4296.4800000000005, "end": 4302.88, "text": " this would
  also pave the way to using mighty, you know, plugging in mighty in the pipeline?",
  "tokens": [50392, 341, 576, 611, 28870, 264, 636, 281, 1228, 21556, 11, 291, 458,
  11, 42975, 294, 21556, 294, 264, 15517, 30, 50712], "temperature": 0.0, "avg_logprob":
  -0.12615863096366808, "compression_ratio": 1.6973684210526316, "no_speech_prob":
  0.002458206145092845}, {"id": 686, "seek": 429592, "start": 4302.88, "end": 4308.4800000000005,
  "text": " Let''s say if I''m a pine cone user and I can have a node pine cone connector
  at the same time as", "tokens": [50712, 961, 311, 584, 498, 286, 478, 257, 15113,
  19749, 4195, 293, 286, 393, 362, 257, 9984, 15113, 19749, 19127, 412, 264, 912,
  565, 382, 50992], "temperature": 0.0, "avg_logprob": -0.12615863096366808, "compression_ratio":
  1.6973684210526316, "no_speech_prob": 0.002458206145092845}, {"id": 687, "seek":
  429592, "start": 4308.4800000000005, "end": 4314.32, "text": " mighty. I''d say
  half half that, you know, there is, you know, I do want to promote mighty, of course.",
  "tokens": [50992, 21556, 13, 286, 1116, 584, 1922, 1922, 300, 11, 291, 458, 11,
  456, 307, 11, 291, 458, 11, 286, 360, 528, 281, 9773, 21556, 11, 295, 1164, 13,
  51284], "temperature": 0.0, "avg_logprob": -0.12615863096366808, "compression_ratio":
  1.6973684210526316, "no_speech_prob": 0.002458206145092845}, {"id": 688, "seek":
  429592, "start": 4315.12, "end": 4322.56, "text": " But again, I want to bring these
  tools outside of the Python ecosystem. If you look at the vector", "tokens": [51324,
  583, 797, 11, 286, 528, 281, 1565, 613, 3873, 2380, 295, 264, 15329, 11311, 13,
  759, 291, 574, 412, 264, 8062, 51696], "temperature": 0.0, "avg_logprob": -0.12615863096366808,
  "compression_ratio": 1.6973684210526316, "no_speech_prob": 0.002458206145092845},
  {"id": 689, "seek": 432256, "start": 4322.56, "end": 4328.0, "text": " databases
  right now, with it, with the exception of, uh, with VV8, VV8 does a great job of
  having", "tokens": [50364, 22380, 558, 586, 11, 365, 309, 11, 365, 264, 11183, 295,
  11, 2232, 11, 365, 691, 53, 23, 11, 691, 53, 23, 775, 257, 869, 1691, 295, 1419,
  50636], "temperature": 0.0, "avg_logprob": -0.20592634139522428, "compression_ratio":
  1.7610294117647058, "no_speech_prob": 0.0020707380026578903}, {"id": 690, "seek":
  432256, "start": 4328.0, "end": 4334.72, "text": " different clients for different,
  um, different languages and stacks, um, Vespa as well. But both,", "tokens": [50636,
  819, 6982, 337, 819, 11, 1105, 11, 819, 8650, 293, 30792, 11, 1105, 11, 691, 279,
  4306, 382, 731, 13, 583, 1293, 11, 50972], "temperature": 0.0, "avg_logprob": -0.20592634139522428,
  "compression_ratio": 1.7610294117647058, "no_speech_prob": 0.0020707380026578903},
  {"id": 691, "seek": 432256, "start": 4335.4400000000005, "end": 4340.8, "text":
  " both quadrant and pine cone right now, it''s all Python. Well, like, quadrant,
  quadrant is written", "tokens": [51008, 1293, 46856, 293, 15113, 19749, 558, 586,
  11, 309, 311, 439, 15329, 13, 1042, 11, 411, 11, 46856, 11, 46856, 307, 3720, 51276],
  "temperature": 0.0, "avg_logprob": -0.20592634139522428, "compression_ratio": 1.7610294117647058,
  "no_speech_prob": 0.0020707380026578903}, {"id": 692, "seek": 432256, "start": 4340.8,
  "end": 4346.64, "text": " in rust, but their client right now is their, their first
  class client is in Python. Um,", "tokens": [51276, 294, 15259, 11, 457, 641, 6423,
  558, 586, 307, 641, 11, 641, 700, 1508, 6423, 307, 294, 15329, 13, 3301, 11, 51568],
  "temperature": 0.0, "avg_logprob": -0.20592634139522428, "compression_ratio": 1.7610294117647058,
  "no_speech_prob": 0.0020707380026578903}, {"id": 693, "seek": 432256, "start": 4347.360000000001,
  "end": 4352.4800000000005, "text": " which they did that because obviously everybody
  who has to get vectors has to use Python anyway,", "tokens": [51604, 597, 436, 630,
  300, 570, 2745, 2201, 567, 575, 281, 483, 18875, 575, 281, 764, 15329, 4033, 11,
  51860], "temperature": 0.0, "avg_logprob": -0.20592634139522428, "compression_ratio":
  1.7610294117647058, "no_speech_prob": 0.0020707380026578903}, {"id": 694, "seek":
  435248, "start": 4352.48, "end": 4359.919999999999, "text": " uh, or they used to.
  Um, so that''s why they chose Python. At least that''s, that''s what I speculate.",
  "tokens": [50364, 2232, 11, 420, 436, 1143, 281, 13, 3301, 11, 370, 300, 311, 983,
  436, 5111, 15329, 13, 1711, 1935, 300, 311, 11, 300, 311, 437, 286, 40775, 13, 50736],
  "temperature": 0.0, "avg_logprob": -0.13662703335285187, "compression_ratio": 1.8091603053435115,
  "no_speech_prob": 0.00022973115846980363}, {"id": 695, "seek": 435248, "start":
  4360.32, "end": 4366.32, "text": " Um, and pine cone as well, all their examples
  are in notebook form, um, in Jupyter notebook form.", "tokens": [50756, 3301, 11,
  293, 15113, 19749, 382, 731, 11, 439, 641, 5110, 366, 294, 21060, 1254, 11, 1105,
  11, 294, 22125, 88, 391, 21060, 1254, 13, 51056], "temperature": 0.0, "avg_logprob":
  -0.13662703335285187, "compression_ratio": 1.8091603053435115, "no_speech_prob":
  0.00022973115846980363}, {"id": 696, "seek": 435248, "start": 4366.32, "end": 4370.4,
  "text": " You go in and you want to do a somatic search example, that''s a Python
  notebook.", "tokens": [51056, 509, 352, 294, 293, 291, 528, 281, 360, 257, 3307,
  2399, 3164, 1365, 11, 300, 311, 257, 15329, 21060, 13, 51260], "temperature": 0.0,
  "avg_logprob": -0.13662703335285187, "compression_ratio": 1.8091603053435115, "no_speech_prob":
  0.00022973115846980363}, {"id": 697, "seek": 435248, "start": 4371.759999999999,
  "end": 4376.08, "text": " I''m not crazy about Python notebooks. I think Python
  notebooks are good for illustrating like", "tokens": [51328, 286, 478, 406, 3219,
  466, 15329, 43782, 13, 286, 519, 15329, 43782, 366, 665, 337, 8490, 8754, 411, 51544],
  "temperature": 0.0, "avg_logprob": -0.13662703335285187, "compression_ratio": 1.8091603053435115,
  "no_speech_prob": 0.00022973115846980363}, {"id": 698, "seek": 435248, "start":
  4376.08, "end": 4381.759999999999, "text": " ideas and sketches, uh, for papers,
  but it''s really hard for me to look at a Python notebook and say,", "tokens": [51544,
  3487, 293, 34547, 11, 2232, 11, 337, 10577, 11, 457, 309, 311, 534, 1152, 337, 385,
  281, 574, 412, 257, 15329, 21060, 293, 584, 11, 51828], "temperature": 0.0, "avg_logprob":
  -0.13662703335285187, "compression_ratio": 1.8091603053435115, "no_speech_prob":
  0.00022973115846980363}, {"id": 699, "seek": 438176, "start": 4381.76, "end": 4387.52,
  "text": " here''s how I make this into a working application. Um, it doesn''t translate
  well because the,", "tokens": [50364, 510, 311, 577, 286, 652, 341, 666, 257, 1364,
  3861, 13, 3301, 11, 309, 1177, 380, 13799, 731, 570, 264, 11, 50652], "temperature":
  0.0, "avg_logprob": -0.10886617986167349, "compression_ratio": 1.7765567765567765,
  "no_speech_prob": 0.0005089626647531986}, {"id": 700, "seek": 438176, "start": 4387.52,
  "end": 4390.88, "text": " the architecture isn''t there. It''s a bunch of cells
  that you run in order. That''s not how,", "tokens": [50652, 264, 9482, 1943, 380,
  456, 13, 467, 311, 257, 3840, 295, 5438, 300, 291, 1190, 294, 1668, 13, 663, 311,
  406, 577, 11, 50820], "temperature": 0.0, "avg_logprob": -0.10886617986167349, "compression_ratio":
  1.7765567765567765, "no_speech_prob": 0.0005089626647531986}, {"id": 701, "seek":
  438176, "start": 4391.52, "end": 4399.04, "text": " you know, real world applications
  work. So the idea is to just get these tools and get these ideas", "tokens": [50852,
  291, 458, 11, 957, 1002, 5821, 589, 13, 407, 264, 1558, 307, 281, 445, 483, 613,
  3873, 293, 483, 613, 3487, 51228], "temperature": 0.0, "avg_logprob": -0.10886617986167349,
  "compression_ratio": 1.7765567765567765, "no_speech_prob": 0.0005089626647531986},
  {"id": 702, "seek": 438176, "start": 4399.04, "end": 4403.52, "text": " and capabilities
  out into the hands of a lot of other people who want to be able to use this stuff",
  "tokens": [51228, 293, 10862, 484, 666, 264, 2377, 295, 257, 688, 295, 661, 561,
  567, 528, 281, 312, 1075, 281, 764, 341, 1507, 51452], "temperature": 0.0, "avg_logprob":
  -0.10886617986167349, "compression_ratio": 1.7765567765567765, "no_speech_prob":
  0.0005089626647531986}, {"id": 703, "seek": 438176, "start": 4403.52, "end": 4407.84,
  "text": " and are not familiar with Python, they''re not familiar with NLP, but
  they want to be able to use this,", "tokens": [51452, 293, 366, 406, 4963, 365,
  15329, 11, 436, 434, 406, 4963, 365, 426, 45196, 11, 457, 436, 528, 281, 312, 1075,
  281, 764, 341, 11, 51668], "temperature": 0.0, "avg_logprob": -0.10886617986167349,
  "compression_ratio": 1.7765567765567765, "no_speech_prob": 0.0005089626647531986},
  {"id": 704, "seek": 440784, "start": 4407.84, "end": 4413.04, "text": " uh, this
  new technology because they might have a business problem to try to solve.", "tokens":
  [50364, 2232, 11, 341, 777, 2899, 570, 436, 1062, 362, 257, 1606, 1154, 281, 853,
  281, 5039, 13, 50624], "temperature": 0.0, "avg_logprob": -0.18054136899438236,
  "compression_ratio": 1.5378486055776892, "no_speech_prob": 0.008108616806566715},
  {"id": 705, "seek": 440784, "start": 4413.04, "end": 4418.16, "text": " So you''re
  thinking actually about engineers who are day to day productizing their code and
  thinking,", "tokens": [50624, 407, 291, 434, 1953, 767, 466, 11955, 567, 366, 786,
  281, 786, 1674, 3319, 641, 3089, 293, 1953, 11, 50880], "temperature": 0.0, "avg_logprob":
  -0.18054136899438236, "compression_ratio": 1.5378486055776892, "no_speech_prob":
  0.008108616806566715}, {"id": 706, "seek": 440784, "start": 4418.16, "end": 4425.52,
  "text": " okay, yeah, I need a embedding layer, but I don''t care about notebooks.
  I''m not a Pythonista or whatever.", "tokens": [50880, 1392, 11, 1338, 11, 286,
  643, 257, 12240, 3584, 4583, 11, 457, 286, 500, 380, 1127, 466, 43782, 13, 286,
  478, 406, 257, 15329, 5236, 420, 2035, 13, 51248], "temperature": 0.0, "avg_logprob":
  -0.18054136899438236, "compression_ratio": 1.5378486055776892, "no_speech_prob":
  0.008108616806566715}, {"id": 707, "seek": 440784, "start": 4425.52, "end": 4433.28,
  "text": " So, you know, just give me the tool. Exactly. Yeah, that''s fantastic.
  I mean, and by the tools,", "tokens": [51248, 407, 11, 291, 458, 11, 445, 976, 385,
  264, 2290, 13, 7587, 13, 865, 11, 300, 311, 5456, 13, 286, 914, 11, 293, 538, 264,
  3873, 11, 51636], "temperature": 0.0, "avg_logprob": -0.18054136899438236, "compression_ratio":
  1.5378486055776892, "no_speech_prob": 0.008108616806566715}, {"id": 708, "seek":
  443328, "start": 4433.28, "end": 4437.759999999999, "text": " you also like disclose
  something like ahead of time with me that, to me, that, um, you,", "tokens": [50364,
  291, 611, 411, 36146, 746, 411, 2286, 295, 565, 365, 385, 300, 11, 281, 385, 11,
  300, 11, 1105, 11, 291, 11, 50588], "temperature": 0.0, "avg_logprob": -0.13792694755222487,
  "compression_ratio": 1.7692307692307692, "no_speech_prob": 0.00717752892524004},
  {"id": 709, "seek": 443328, "start": 4438.32, "end": 4444.16, "text": " like one
  of the overarching goals for you is to develop as many tools for the vector search",
  "tokens": [50616, 411, 472, 295, 264, 45501, 5493, 337, 291, 307, 281, 1499, 382,
  867, 3873, 337, 264, 8062, 3164, 50908], "temperature": 0.0, "avg_logprob": -0.13792694755222487,
  "compression_ratio": 1.7692307692307692, "no_speech_prob": 0.00717752892524004},
  {"id": 710, "seek": 443328, "start": 4444.16, "end": 4449.84, "text": " community
  as possible. And like some of the tools you mentioned, like go beyond, you know,",
  "tokens": [50908, 1768, 382, 1944, 13, 400, 411, 512, 295, 264, 3873, 291, 2835,
  11, 411, 352, 4399, 11, 291, 458, 11, 51192], "temperature": 0.0, "avg_logprob":
  -0.13792694755222487, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.00717752892524004}, {"id": 711, "seek": 443328, "start": 4449.84, "end": 4455.84,
  "text": " pure engineering components, like connectors, you said, uh, maybe like
  fine tuning a model or", "tokens": [51192, 6075, 7043, 6677, 11, 411, 31865, 11,
  291, 848, 11, 2232, 11, 1310, 411, 2489, 15164, 257, 2316, 420, 51492], "temperature":
  0.0, "avg_logprob": -0.13792694755222487, "compression_ratio": 1.7692307692307692,
  "no_speech_prob": 0.00717752892524004}, {"id": 712, "seek": 443328, "start": 4455.84,
  "end": 4460.719999999999, "text": " something of that sort, which at that point,
  I think you''re stepping, uh, on the ground of, you", "tokens": [51492, 746, 295,
  300, 1333, 11, 597, 412, 300, 935, 11, 286, 519, 291, 434, 16821, 11, 2232, 11,
  322, 264, 2727, 295, 11, 291, 51736], "temperature": 0.0, "avg_logprob": -0.13792694755222487,
  "compression_ratio": 1.7692307692307692, "no_speech_prob": 0.00717752892524004},
  {"id": 713, "seek": 446072, "start": 4460.88, "end": 4467.360000000001, "text":
  " know, other startups like Gina and, um, you know, deep set and so on. Do you feel
  that way or do you", "tokens": [50372, 458, 11, 661, 28041, 411, 34711, 293, 11,
  1105, 11, 291, 458, 11, 2452, 992, 293, 370, 322, 13, 1144, 291, 841, 300, 636,
  420, 360, 291, 50696], "temperature": 0.0, "avg_logprob": -0.13885197146185513,
  "compression_ratio": 1.6260504201680672, "no_speech_prob": 0.0015320490347221494},
  {"id": 714, "seek": 446072, "start": 4467.360000000001, "end": 4471.52, "text":
  " not concern yourself with those and you''re just thinking, okay, what''s missing
  in the field? I''m", "tokens": [50696, 406, 3136, 1803, 365, 729, 293, 291, 434,
  445, 1953, 11, 1392, 11, 437, 311, 5361, 294, 264, 2519, 30, 286, 478, 50904], "temperature":
  0.0, "avg_logprob": -0.13885197146185513, "compression_ratio": 1.6260504201680672,
  "no_speech_prob": 0.0015320490347221494}, {"id": 715, "seek": 446072, "start": 4471.52,
  "end": 4480.56, "text": " going to add it. I''m going to open source it. Yeah, same.
  So, uh, deep set is like, it''s all Python.", "tokens": [50904, 516, 281, 909, 309,
  13, 286, 478, 516, 281, 1269, 4009, 309, 13, 865, 11, 912, 13, 407, 11, 2232, 11,
  2452, 992, 307, 411, 11, 309, 311, 439, 15329, 13, 51356], "temperature": 0.0, "avg_logprob":
  -0.13885197146185513, "compression_ratio": 1.6260504201680672, "no_speech_prob":
  0.0015320490347221494}, {"id": 716, "seek": 446072, "start": 4480.56, "end": 4486.4800000000005,
  "text": " Again, um, Gina, I think is a lot of Python, right? I''m not as familiar
  with Gina. Yeah,", "tokens": [51356, 3764, 11, 1105, 11, 34711, 11, 286, 519, 307,
  257, 688, 295, 15329, 11, 558, 30, 286, 478, 406, 382, 4963, 365, 34711, 13, 865,
  11, 51652], "temperature": 0.0, "avg_logprob": -0.13885197146185513, "compression_ratio":
  1.6260504201680672, "no_speech_prob": 0.0015320490347221494}, {"id": 717, "seek":
  448648, "start": 4486.48, "end": 4494.0, "text": " they are, they''re Python mostly.
  Yeah. It''s, it''s, there''s a huge opportunity, uh, to make", "tokens": [50364,
  436, 366, 11, 436, 434, 15329, 5240, 13, 865, 13, 467, 311, 11, 309, 311, 11, 456,
  311, 257, 2603, 2650, 11, 2232, 11, 281, 652, 50740], "temperature": 0.0, "avg_logprob":
  -0.18279426976254112, "compression_ratio": 1.4404145077720207, "no_speech_prob":
  0.00047038114280439913}, {"id": 718, "seek": 448648, "start": 4494.0, "end": 4507.12,
  "text": " these tools available to non Python, um, stacks. And I don''t, I, before
  I started working in", "tokens": [50740, 613, 3873, 2435, 281, 2107, 15329, 11,
  1105, 11, 30792, 13, 400, 286, 500, 380, 11, 286, 11, 949, 286, 1409, 1364, 294,
  51396], "temperature": 0.0, "avg_logprob": -0.18279426976254112, "compression_ratio":
  1.4404145077720207, "no_speech_prob": 0.00047038114280439913}, {"id": 719, "seek":
  448648, "start": 4507.12, "end": 4512.799999999999, "text": " machine learning,
  I''ve never even considered Python as, as an application framework. You know,",
  "tokens": [51396, 3479, 2539, 11, 286, 600, 1128, 754, 4888, 15329, 382, 11, 382,
  364, 3861, 8388, 13, 509, 458, 11, 51680], "temperature": 0.0, "avg_logprob": -0.18279426976254112,
  "compression_ratio": 1.4404145077720207, "no_speech_prob": 0.00047038114280439913},
  {"id": 720, "seek": 451280, "start": 4512.88, "end": 4519.360000000001, "text":
  " people are using like Django, flash and stuff like that. Um, but for me, it was
  like, uh,", "tokens": [50368, 561, 366, 1228, 411, 33464, 17150, 11, 7319, 293,
  1507, 411, 300, 13, 3301, 11, 457, 337, 385, 11, 309, 390, 411, 11, 2232, 11, 50692],
  "temperature": 0.0, "avg_logprob": -0.1309790228405138, "compression_ratio": 1.763157894736842,
  "no_speech_prob": 0.0004544277908280492}, {"id": 721, "seek": 451280, "start": 4519.360000000001,
  "end": 4523.6, "text": " it''s not that it didn''t take it seriously. I just felt
  it wasn''t, it wasn''t something that", "tokens": [50692, 309, 311, 406, 300, 309,
  994, 380, 747, 309, 6638, 13, 286, 445, 2762, 309, 2067, 380, 11, 309, 2067, 380,
  746, 300, 50904], "temperature": 0.0, "avg_logprob": -0.1309790228405138, "compression_ratio":
  1.763157894736842, "no_speech_prob": 0.0004544277908280492}, {"id": 722, "seek":
  451280, "start": 4524.24, "end": 4530.400000000001, "text": " I would have chosen
  to use aside from, you know, a lot of other, a lot of other stacks. So there", "tokens":
  [50936, 286, 576, 362, 8614, 281, 764, 7359, 490, 11, 291, 458, 11, 257, 688, 295,
  661, 11, 257, 688, 295, 661, 30792, 13, 407, 456, 51244], "temperature": 0.0, "avg_logprob":
  -0.1309790228405138, "compression_ratio": 1.763157894736842, "no_speech_prob": 0.0004544277908280492},
  {"id": 723, "seek": 451280, "start": 4530.400000000001, "end": 4534.88, "text":
  " is so many other teams out there that want to be able to use these things, but
  now they have to,", "tokens": [51244, 307, 370, 867, 661, 5491, 484, 456, 300, 528,
  281, 312, 1075, 281, 764, 613, 721, 11, 457, 586, 436, 362, 281, 11, 51468], "temperature":
  0.0, "avg_logprob": -0.1309790228405138, "compression_ratio": 1.763157894736842,
  "no_speech_prob": 0.0004544277908280492}, {"id": 724, "seek": 451280, "start": 4534.88,
  "end": 4541.52, "text": " oh, Python, Python, Python, it''s nonstop. So we got to
  break out of that somehow. Um, and, uh,", "tokens": [51468, 1954, 11, 15329, 11,
  15329, 11, 15329, 11, 309, 311, 2107, 13559, 13, 407, 321, 658, 281, 1821, 484,
  295, 300, 6063, 13, 3301, 11, 293, 11, 2232, 11, 51800], "temperature": 0.0, "avg_logprob":
  -0.1309790228405138, "compression_ratio": 1.763157894736842, "no_speech_prob": 0.0004544277908280492},
  {"id": 725, "seek": 454152, "start": 4541.52, "end": 4546.0, "text": " I''m starting
  with node because the JavaScript ecosystem is just absolutely enormous. I think",
  "tokens": [50364, 286, 478, 2891, 365, 9984, 570, 264, 15778, 11311, 307, 445, 3122,
  11322, 13, 286, 519, 50588], "temperature": 0.0, "avg_logprob": -0.13762704166797324,
  "compression_ratio": 1.7348484848484849, "no_speech_prob": 0.0015206891112029552},
  {"id": 726, "seek": 454152, "start": 4546.0, "end": 4550.400000000001, "text": "
  people underestimate the size of the JavaScript ecosystem. If you''re in machine
  learning and you''re", "tokens": [50588, 561, 35826, 264, 2744, 295, 264, 15778,
  11311, 13, 759, 291, 434, 294, 3479, 2539, 293, 291, 434, 50808], "temperature":
  0.0, "avg_logprob": -0.13762704166797324, "compression_ratio": 1.7348484848484849,
  "no_speech_prob": 0.0015206891112029552}, {"id": 727, "seek": 454152, "start": 4550.400000000001,
  "end": 4558.160000000001, "text": " listening to this podcast right now, like there,
  there are like maybe a hundred people for every one", "tokens": [50808, 4764, 281,
  341, 7367, 558, 586, 11, 411, 456, 11, 456, 366, 411, 1310, 257, 3262, 561, 337,
  633, 472, 51196], "temperature": 0.0, "avg_logprob": -0.13762704166797324, "compression_ratio":
  1.7348484848484849, "no_speech_prob": 0.0015206891112029552}, {"id": 728, "seek":
  454152, "start": 4558.160000000001, "end": 4566.080000000001, "text": " of you who''s
  using JavaScript in, in, for applications. Like that''s how big it is. Um, so that,
  uh,", "tokens": [51196, 295, 291, 567, 311, 1228, 15778, 294, 11, 294, 11, 337,
  5821, 13, 1743, 300, 311, 577, 955, 309, 307, 13, 3301, 11, 370, 300, 11, 2232,
  11, 51592], "temperature": 0.0, "avg_logprob": -0.13762704166797324, "compression_ratio":
  1.7348484848484849, "no_speech_prob": 0.0015206891112029552}, {"id": 729, "seek":
  454152, "start": 4566.080000000001, "end": 4568.72, "text": " I''m starting there.
  I just know it''s just an enormous community.", "tokens": [51592, 286, 478, 2891,
  456, 13, 286, 445, 458, 309, 311, 445, 364, 11322, 1768, 13, 51724], "temperature":
  0.0, "avg_logprob": -0.13762704166797324, "compression_ratio": 1.7348484848484849,
  "no_speech_prob": 0.0015206891112029552}, {"id": 730, "seek": 456872, "start": 4569.4400000000005,
  "end": 4574.8, "text": " And not only for front end development, you know, we need
  to emphasize this because you also have", "tokens": [50400, 400, 406, 787, 337,
  1868, 917, 3250, 11, 291, 458, 11, 321, 643, 281, 16078, 341, 570, 291, 611, 362,
  50668], "temperature": 0.0, "avg_logprob": -0.19019221296214095, "compression_ratio":
  1.6074380165289257, "no_speech_prob": 0.01118532195687294}, {"id": 731, "seek":
  456872, "start": 4574.8, "end": 4581.12, "text": " server side JavaScript, like
  Node.js and others. And it''s, it''s huge. And a lot of software,", "tokens": [50668,
  7154, 1252, 15778, 11, 411, 38640, 13, 25530, 293, 2357, 13, 400, 309, 311, 11,
  309, 311, 2603, 13, 400, 257, 688, 295, 4722, 11, 50984], "temperature": 0.0, "avg_logprob":
  -0.19019221296214095, "compression_ratio": 1.6074380165289257, "no_speech_prob":
  0.01118532195687294}, {"id": 732, "seek": 456872, "start": 4582.0, "end": 4589.360000000001,
  "text": " which is kind of the, the middleware between your super cool search engine
  or your, your vector database,", "tokens": [51028, 597, 307, 733, 295, 264, 11,
  264, 2808, 3039, 1296, 428, 1687, 1627, 3164, 2848, 420, 428, 11, 428, 8062, 8149,
  11, 51396], "temperature": 0.0, "avg_logprob": -0.19019221296214095, "compression_ratio":
  1.6074380165289257, "no_speech_prob": 0.01118532195687294}, {"id": 733, "seek":
  456872, "start": 4590.0, "end": 4594.96, "text": " and the front end, you have a
  lot of middleware written in node because it''s so much easier.", "tokens": [51428,
  293, 264, 1868, 917, 11, 291, 362, 257, 688, 295, 2808, 3039, 3720, 294, 9984, 570,
  309, 311, 370, 709, 3571, 13, 51676], "temperature": 0.0, "avg_logprob": -0.19019221296214095,
  "compression_ratio": 1.6074380165289257, "no_speech_prob": 0.01118532195687294},
  {"id": 734, "seek": 459496, "start": 4595.68, "end": 4600.24, "text": " Oh, well,
  not easy. I don''t know. Is it easier? But I think it''s just the pervasive, you
  know,", "tokens": [50400, 876, 11, 731, 11, 406, 1858, 13, 286, 500, 380, 458, 13,
  1119, 309, 3571, 30, 583, 286, 519, 309, 311, 445, 264, 680, 39211, 11, 291, 458,
  11, 50628], "temperature": 0.0, "avg_logprob": -0.15575005326952254, "compression_ratio":
  1.6394849785407726, "no_speech_prob": 0.006392363924533129}, {"id": 735, "seek":
  459496, "start": 4600.24, "end": 4606.0, "text": " nature of JavaScript. Yeah, I
  don''t know if I''d say node is easier than Python. I think it''s,", "tokens": [50628,
  3687, 295, 15778, 13, 865, 11, 286, 500, 380, 458, 498, 286, 1116, 584, 9984, 307,
  3571, 813, 15329, 13, 286, 519, 309, 311, 11, 50916], "temperature": 0.0, "avg_logprob":
  -0.15575005326952254, "compression_ratio": 1.6394849785407726, "no_speech_prob":
  0.006392363924533129}, {"id": 736, "seek": 459496, "start": 4606.8, "end": 4611.12,
  "text": " you know, I think they''re similar actually in a lot of ways. The syntax
  is a little bit different,", "tokens": [50956, 291, 458, 11, 286, 519, 436, 434,
  2531, 767, 294, 257, 688, 295, 2098, 13, 440, 28431, 307, 257, 707, 857, 819, 11,
  51172], "temperature": 0.0, "avg_logprob": -0.15575005326952254, "compression_ratio":
  1.6394849785407726, "no_speech_prob": 0.006392363924533129}, {"id": 737, "seek":
  459496, "start": 4611.12, "end": 4620.64, "text": " you know, curly braces versus
  tabs. But, uh, I think that node, we''re, we''re getting away from", "tokens": [51172,
  291, 458, 11, 32066, 41537, 5717, 20743, 13, 583, 11, 2232, 11, 286, 519, 300, 9984,
  11, 321, 434, 11, 321, 434, 1242, 1314, 490, 51648], "temperature": 0.0, "avg_logprob":
  -0.15575005326952254, "compression_ratio": 1.6394849785407726, "no_speech_prob":
  0.006392363924533129}, {"id": 738, "seek": 462064, "start": 4620.64, "end": 4625.76,
  "text": " vectors right now. But node started because the JavaScript was the language
  of the web.", "tokens": [50364, 18875, 558, 586, 13, 583, 9984, 1409, 570, 264,
  15778, 390, 264, 2856, 295, 264, 3670, 13, 50620], "temperature": 0.0, "avg_logprob":
  -0.16725805193878884, "compression_ratio": 1.5896226415094339, "no_speech_prob":
  0.0004629429313354194}, {"id": 739, "seek": 462064, "start": 4626.72, "end": 4632.320000000001,
  "text": " And people didn''t want to learn another language to also write back end
  code.", "tokens": [50668, 400, 561, 994, 380, 528, 281, 1466, 1071, 2856, 281, 611,
  2464, 646, 917, 3089, 13, 50948], "temperature": 0.0, "avg_logprob": -0.16725805193878884,
  "compression_ratio": 1.5896226415094339, "no_speech_prob": 0.0004629429313354194},
  {"id": 740, "seek": 462064, "start": 4634.0, "end": 4639.200000000001, "text": "
  You know, you were using Pearl, right? So a lot of the, there was a lot of time
  where it was like", "tokens": [51032, 509, 458, 11, 291, 645, 1228, 24639, 11, 558,
  30, 407, 257, 688, 295, 264, 11, 456, 390, 257, 688, 295, 565, 689, 309, 390, 411,
  51292], "temperature": 0.0, "avg_logprob": -0.16725805193878884, "compression_ratio":
  1.5896226415094339, "no_speech_prob": 0.0004629429313354194}, {"id": 741, "seek":
  462064, "start": 4639.200000000001, "end": 4643.68, "text": " Pearl, PHP, plus JavaScript,
  right? There was that whole world out there.", "tokens": [51292, 24639, 11, 47298,
  11, 1804, 15778, 11, 558, 30, 821, 390, 300, 1379, 1002, 484, 456, 13, 51516], "temperature":
  0.0, "avg_logprob": -0.16725805193878884, "compression_ratio": 1.5896226415094339,
  "no_speech_prob": 0.0004629429313354194}, {"id": 742, "seek": 464368, "start": 4644.56,
  "end": 4651.280000000001, "text": " Um, so that''s where node came from. It came
  from the web, the web front end. So that''s,", "tokens": [50408, 3301, 11, 370,
  300, 311, 689, 9984, 1361, 490, 13, 467, 1361, 490, 264, 3670, 11, 264, 3670, 1868,
  917, 13, 407, 300, 311, 11, 50744], "temperature": 0.0, "avg_logprob": -0.21919116795620072,
  "compression_ratio": 1.6923076923076923, "no_speech_prob": 0.0033956628758460283},
  {"id": 743, "seek": 464368, "start": 4651.92, "end": 4655.92, "text": " web front
  end is enormous. And they all, and a lot of them just adopted node. And the node
  had", "tokens": [50776, 3670, 1868, 917, 307, 11322, 13, 400, 436, 439, 11, 293,
  257, 688, 295, 552, 445, 12175, 9984, 13, 400, 264, 9984, 632, 50976], "temperature":
  0.0, "avg_logprob": -0.21919116795620072, "compression_ratio": 1.6923076923076923,
  "no_speech_prob": 0.0033956628758460283}, {"id": 744, "seek": 464368, "start": 4655.92,
  "end": 4663.360000000001, "text": " its own hype cycle, like 2010 through 2014 was
  like maybe nodes heyday where it just was like", "tokens": [50976, 1080, 1065, 24144,
  6586, 11, 411, 9657, 807, 8227, 390, 411, 1310, 13891, 4177, 810, 689, 309, 445,
  390, 411, 51348], "temperature": 0.0, "avg_logprob": -0.21919116795620072, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.0033956628758460283}, {"id": 745, "seek":
  464368, "start": 4663.360000000001, "end": 4669.68, "text": " through the roof.
  Everything was node.js. Um, it was going crazy. Now it''s all, now it''s all, uh,",
  "tokens": [51348, 807, 264, 8418, 13, 5471, 390, 9984, 13, 25530, 13, 3301, 11,
  309, 390, 516, 3219, 13, 823, 309, 311, 439, 11, 586, 309, 311, 439, 11, 2232, 11,
  51664], "temperature": 0.0, "avg_logprob": -0.21919116795620072, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.0033956628758460283}, {"id": 746, "seek":
  466968, "start": 4669.68, "end": 4675.4400000000005, "text": " uh, you know, machine
  learning and AI. A lot of people got involved in this, in this world.", "tokens":
  [50364, 2232, 11, 291, 458, 11, 3479, 2539, 293, 7318, 13, 316, 688, 295, 561, 658,
  3288, 294, 341, 11, 294, 341, 1002, 13, 50652], "temperature": 0.0, "avg_logprob":
  -0.16469749296554412, "compression_ratio": 1.60352422907489, "no_speech_prob": 0.003676739986985922},
  {"id": 747, "seek": 466968, "start": 4676.0, "end": 4681.280000000001, "text": "
  But there''s still a huge, a huge section of the world that''s written on top of
  node", "tokens": [50680, 583, 456, 311, 920, 257, 2603, 11, 257, 2603, 3541, 295,
  264, 1002, 300, 311, 3720, 322, 1192, 295, 9984, 50944], "temperature": 0.0, "avg_logprob":
  -0.16469749296554412, "compression_ratio": 1.60352422907489, "no_speech_prob": 0.003676739986985922},
  {"id": 748, "seek": 466968, "start": 4681.84, "end": 4687.4400000000005, "text":
  " from applications that started in, in, you know, the early 2010s. And it evolved
  ever since.", "tokens": [50972, 490, 5821, 300, 1409, 294, 11, 294, 11, 291, 458,
  11, 264, 2440, 9657, 82, 13, 400, 309, 14178, 1562, 1670, 13, 51252], "temperature":
  0.0, "avg_logprob": -0.16469749296554412, "compression_ratio": 1.60352422907489,
  "no_speech_prob": 0.003676739986985922}, {"id": 749, "seek": 466968, "start": 4688.8,
  "end": 4694.4800000000005, "text": " Yeah. But back to tools. Like, so you said
  in the early notes you shared, like you also want to", "tokens": [51320, 865, 13,
  583, 646, 281, 3873, 13, 1743, 11, 370, 291, 848, 294, 264, 2440, 5570, 291, 5507,
  11, 411, 291, 611, 528, 281, 51604], "temperature": 0.0, "avg_logprob": -0.16469749296554412,
  "compression_ratio": 1.60352422907489, "no_speech_prob": 0.003676739986985922},
  {"id": 750, "seek": 469448, "start": 4694.5599999999995, "end": 4700.16, "text":
  " address some of the, uh, problem solved problems like in model fine tuning or
  some other like pipeline", "tokens": [50368, 2985, 512, 295, 264, 11, 2232, 11,
  1154, 13041, 2740, 411, 294, 2316, 2489, 15164, 420, 512, 661, 411, 15517, 50648],
  "temperature": 0.0, "avg_logprob": -0.18292916010296534, "compression_ratio": 1.7509578544061302,
  "no_speech_prob": 0.00938659068197012}, {"id": 751, "seek": 469448, "start": 4700.16,
  "end": 4707.04, "text": " steps that, that may be precede the, uh, the, the embedding
  layer that you have now addressed with", "tokens": [50648, 4439, 300, 11, 300, 815,
  312, 16969, 68, 264, 11, 2232, 11, 264, 11, 264, 12240, 3584, 4583, 300, 291, 362,
  586, 13847, 365, 50992], "temperature": 0.0, "avg_logprob": -0.18292916010296534,
  "compression_ratio": 1.7509578544061302, "no_speech_prob": 0.00938659068197012},
  {"id": 752, "seek": 469448, "start": 4707.04, "end": 4710.08, "text": " MITIS. So
  what are your thoughts there? What, what do you think is missing?", "tokens": [50992,
  13100, 2343, 13, 407, 437, 366, 428, 4598, 456, 30, 708, 11, 437, 360, 291, 519,
  307, 5361, 30, 51144], "temperature": 0.0, "avg_logprob": -0.18292916010296534,
  "compression_ratio": 1.7509578544061302, "no_speech_prob": 0.00938659068197012},
  {"id": 753, "seek": 469448, "start": 4712.16, "end": 4716.4, "text": " I don''t,
  yeah, I don''t know if I''m going to get into actual model tuning. I think that,",
  "tokens": [51248, 286, 500, 380, 11, 1338, 11, 286, 500, 380, 458, 498, 286, 478,
  516, 281, 483, 666, 3539, 2316, 15164, 13, 286, 519, 300, 11, 51460], "temperature":
  0.0, "avg_logprob": -0.18292916010296534, "compression_ratio": 1.7509578544061302,
  "no_speech_prob": 0.00938659068197012}, {"id": 754, "seek": 469448, "start": 4717.839999999999,
  "end": 4722.879999999999, "text": " first of all, I''m not, I''m not as good as,
  I''m not as good training models as other people.", "tokens": [51532, 700, 295,
  439, 11, 286, 478, 406, 11, 286, 478, 406, 382, 665, 382, 11, 286, 478, 406, 382,
  665, 3097, 5245, 382, 661, 561, 13, 51784], "temperature": 0.0, "avg_logprob": -0.18292916010296534,
  "compression_ratio": 1.7509578544061302, "no_speech_prob": 0.00938659068197012},
  {"id": 755, "seek": 472288, "start": 4722.88, "end": 4727.76, "text": " There are
  other people that are suited to train models. But I do think there''s a lot of other",
  "tokens": [50364, 821, 366, 661, 561, 300, 366, 24736, 281, 3847, 5245, 13, 583,
  286, 360, 519, 456, 311, 257, 688, 295, 661, 50608], "temperature": 0.0, "avg_logprob":
  -0.18495378040132068, "compression_ratio": 1.5826446280991735, "no_speech_prob":
  0.00019972323207184672}, {"id": 756, "seek": 472288, "start": 4727.76, "end": 4736.16,
  "text": " information that is lacking in model in the, the ML ops world and vector,
  and vector search.", "tokens": [50608, 1589, 300, 307, 20889, 294, 2316, 294, 264,
  11, 264, 21601, 44663, 1002, 293, 8062, 11, 293, 8062, 3164, 13, 51028], "temperature":
  0.0, "avg_logprob": -0.18495378040132068, "compression_ratio": 1.5826446280991735,
  "no_speech_prob": 0.00019972323207184672}, {"id": 757, "seek": 472288, "start":
  4737.4400000000005, "end": 4742.32, "text": " One of them is just like, well, how
  similar are these things, right? What, what''s the distribution", "tokens": [51092,
  1485, 295, 552, 307, 445, 411, 11, 731, 11, 577, 2531, 366, 613, 721, 11, 558, 30,
  708, 11, 437, 311, 264, 7316, 51336], "temperature": 0.0, "avg_logprob": -0.18495378040132068,
  "compression_ratio": 1.5826446280991735, "no_speech_prob": 0.00019972323207184672},
  {"id": 758, "seek": 472288, "start": 4742.32, "end": 4750.4800000000005, "text":
  " of similarities? Um, I think we, V8 said they, they do support, uh, some of that
  and, uh, Vespas,", "tokens": [51336, 295, 24197, 30, 3301, 11, 286, 519, 321, 11,
  691, 23, 848, 436, 11, 436, 360, 1406, 11, 2232, 11, 512, 295, 300, 293, 11, 2232,
  11, 691, 13361, 296, 11, 51744], "temperature": 0.0, "avg_logprob": -0.18495378040132068,
  "compression_ratio": 1.5826446280991735, "no_speech_prob": 0.00019972323207184672},
  {"id": 759, "seek": 475048, "start": 4750.48, "end": 4757.2, "text": " what''s some
  of that in logging. But, um, I don''t know about Pankoam, uh, I''m pretty sure,
  rust,", "tokens": [50364, 437, 311, 512, 295, 300, 294, 27991, 13, 583, 11, 1105,
  11, 286, 500, 380, 458, 466, 430, 657, 78, 335, 11, 2232, 11, 286, 478, 1238, 988,
  11, 15259, 11, 50700], "temperature": 0.0, "avg_logprob": -0.2034935992697011, "compression_ratio":
  1.6167400881057268, "no_speech_prob": 0.00035570000181905925}, {"id": 760, "seek":
  475048, "start": 4757.2, "end": 4762.959999999999, "text": " uh, I''m sure, pretty
  sure quadrant does not. So it''s like, what do I mean by this? It''s like, if I,",
  "tokens": [50700, 2232, 11, 286, 478, 988, 11, 1238, 988, 46856, 775, 406, 13, 407,
  309, 311, 411, 11, 437, 360, 286, 914, 538, 341, 30, 467, 311, 411, 11, 498, 286,
  11, 50988], "temperature": 0.0, "avg_logprob": -0.2034935992697011, "compression_ratio":
  1.6167400881057268, "no_speech_prob": 0.00035570000181905925}, {"id": 761, "seek":
  475048, "start": 4762.959999999999, "end": 4772.48, "text": " if I, uh, have a vector
  and I get, and I do a query against, um, uh, quadrant, for example,", "tokens":
  [50988, 498, 286, 11, 2232, 11, 362, 257, 8062, 293, 286, 483, 11, 293, 286, 360,
  257, 14581, 1970, 11, 1105, 11, 2232, 11, 46856, 11, 337, 1365, 11, 51464], "temperature":
  0.0, "avg_logprob": -0.2034935992697011, "compression_ratio": 1.6167400881057268,
  "no_speech_prob": 0.00035570000181905925}, {"id": 762, "seek": 475048, "start":
  4772.48, "end": 4776.24, "text": " I get back a list of documents that are nearest
  neighbors and the similarities.", "tokens": [51464, 286, 483, 646, 257, 1329, 295,
  8512, 300, 366, 23831, 12512, 293, 264, 24197, 13, 51652], "temperature": 0.0, "avg_logprob":
  -0.2034935992697011, "compression_ratio": 1.6167400881057268, "no_speech_prob":
  0.00035570000181905925}, {"id": 763, "seek": 477624, "start": 4777.2, "end": 4782.719999999999,
  "text": " Well, where does that fit? Like, if I get it back in the first document
  is like point four or", "tokens": [50412, 1042, 11, 689, 775, 300, 3318, 30, 1743,
  11, 498, 286, 483, 309, 646, 294, 264, 700, 4166, 307, 411, 935, 1451, 420, 50688],
  "temperature": 0.0, "avg_logprob": -0.1438651597204287, "compression_ratio": 1.7470817120622568,
  "no_speech_prob": 0.003709448967128992}, {"id": 764, "seek": 477624, "start": 4782.719999999999,
  "end": 4789.04, "text": " not similar, right? Is that good? Is that bad? Like, what
  are the, what''s, what''s, what''s real,", "tokens": [50688, 406, 2531, 11, 558,
  30, 1119, 300, 665, 30, 1119, 300, 1578, 30, 1743, 11, 437, 366, 264, 11, 437, 311,
  11, 437, 311, 11, 437, 311, 957, 11, 51004], "temperature": 0.0, "avg_logprob":
  -0.1438651597204287, "compression_ratio": 1.7470817120622568, "no_speech_prob":
  0.003709448967128992}, {"id": 765, "seek": 477624, "start": 4789.04, "end": 4793.04,
  "text": " what''s real good similar? Maybe, maybe the best similarities are like
  point eight range.", "tokens": [51004, 437, 311, 957, 665, 2531, 30, 2704, 11, 1310,
  264, 1151, 24197, 366, 411, 935, 3180, 3613, 13, 51204], "temperature": 0.0, "avg_logprob":
  -0.1438651597204287, "compression_ratio": 1.7470817120622568, "no_speech_prob":
  0.003709448967128992}, {"id": 766, "seek": 477624, "start": 4793.599999999999, "end":
  4798.96, "text": " So now I know that, well, in terms of my entire corpus and how
  people usually query,", "tokens": [51232, 407, 586, 286, 458, 300, 11, 731, 11,
  294, 2115, 295, 452, 2302, 1181, 31624, 293, 577, 561, 2673, 14581, 11, 51500],
  "temperature": 0.0, "avg_logprob": -0.1438651597204287, "compression_ratio": 1.7470817120622568,
  "no_speech_prob": 0.003709448967128992}, {"id": 767, "seek": 477624, "start": 4798.96,
  "end": 4804.16, "text": " this result is actually not that great. And there''s a
  lot of questions to be answered", "tokens": [51500, 341, 1874, 307, 767, 406, 300,
  869, 13, 400, 456, 311, 257, 688, 295, 1651, 281, 312, 10103, 51760], "temperature":
  0.0, "avg_logprob": -0.1438651597204287, "compression_ratio": 1.7470817120622568,
  "no_speech_prob": 0.003709448967128992}, {"id": 768, "seek": 480416, "start": 4805.12,
  "end": 4810.08, "text": " around that stuff. And so I think that''s lacking in a
  lot of ways. I don''t know if that''s the right", "tokens": [50412, 926, 300, 1507,
  13, 400, 370, 286, 519, 300, 311, 20889, 294, 257, 688, 295, 2098, 13, 286, 500,
  380, 458, 498, 300, 311, 264, 558, 50660], "temperature": 0.0, "avg_logprob": -0.14286590936615712,
  "compression_ratio": 1.8122605363984674, "no_speech_prob": 0.00830679852515459},
  {"id": 769, "seek": 480416, "start": 4810.08, "end": 4814.5599999999995, "text":
  " fit for Mighty though. I think there''s just external tools that, you know, I''m
  kicking around.", "tokens": [50660, 3318, 337, 45874, 1673, 13, 286, 519, 456, 311,
  445, 8320, 3873, 300, 11, 291, 458, 11, 286, 478, 19137, 926, 13, 50884], "temperature":
  0.0, "avg_logprob": -0.14286590936615712, "compression_ratio": 1.8122605363984674,
  "no_speech_prob": 0.00830679852515459}, {"id": 770, "seek": 480416, "start": 4814.5599999999995,
  "end": 4821.2, "text": " All that stuff would be open source. I''m really interested
  in, in Mighty being, uh, the area of", "tokens": [50884, 1057, 300, 1507, 576, 312,
  1269, 4009, 13, 286, 478, 534, 3102, 294, 11, 294, 45874, 885, 11, 2232, 11, 264,
  1859, 295, 51216], "temperature": 0.0, "avg_logprob": -0.14286590936615712, "compression_ratio":
  1.8122605363984674, "no_speech_prob": 0.00830679852515459}, {"id": 771, "seek":
  480416, "start": 4821.2, "end": 4826.0, "text": " the business and then all the
  other stuff is open source to make things easier for people to use,", "tokens":
  [51216, 264, 1606, 293, 550, 439, 264, 661, 1507, 307, 1269, 4009, 281, 652, 721,
  3571, 337, 561, 281, 764, 11, 51456], "temperature": 0.0, "avg_logprob": -0.14286590936615712,
  "compression_ratio": 1.8122605363984674, "no_speech_prob": 0.00830679852515459},
  {"id": 772, "seek": 480416, "start": 4826.5599999999995, "end": 4834.08, "text":
  " uh, these things. But yeah, there, there''s a lot, there''s a lot of stuff in
  terms of", "tokens": [51484, 2232, 11, 613, 721, 13, 583, 1338, 11, 456, 11, 456,
  311, 257, 688, 11, 456, 311, 257, 688, 295, 1507, 294, 2115, 295, 51860], "temperature":
  0.0, "avg_logprob": -0.14286590936615712, "compression_ratio": 1.8122605363984674,
  "no_speech_prob": 0.00830679852515459}, {"id": 773, "seek": 483408, "start": 4834.08,
  "end": 4841.84, "text": " uh, in the MLObs world, there''s like model drift. It''s
  like, well, I used, you know, if,", "tokens": [50364, 2232, 11, 294, 264, 21601,
  46, 929, 1002, 11, 456, 311, 411, 2316, 19699, 13, 467, 311, 411, 11, 731, 11, 286,
  1143, 11, 291, 458, 11, 498, 11, 50752], "temperature": 0.0, "avg_logprob": -0.175953077233356,
  "compression_ratio": 1.5380434782608696, "no_speech_prob": 0.0010293223895132542},
  {"id": 774, "seek": 483408, "start": 4841.84, "end": 4848.72, "text": " let''s say
  I have like 100, uh, 100 sentences, right? And I vectorized these against, you know,",
  "tokens": [50752, 718, 311, 584, 286, 362, 411, 2319, 11, 2232, 11, 2319, 16579,
  11, 558, 30, 400, 286, 8062, 1602, 613, 1970, 11, 291, 458, 11, 51096], "temperature":
  0.0, "avg_logprob": -0.175953077233356, "compression_ratio": 1.5380434782608696,
  "no_speech_prob": 0.0010293223895132542}, {"id": 775, "seek": 483408, "start": 4848.72,
  "end": 4855.6, "text": " model one dot two dot three, right? And I got back, um,
  I got back a list of, uh, vectors. Now I''ve", "tokens": [51096, 2316, 472, 5893,
  732, 5893, 1045, 11, 558, 30, 400, 286, 658, 646, 11, 1105, 11, 286, 658, 646, 257,
  1329, 295, 11, 2232, 11, 18875, 13, 823, 286, 600, 51440], "temperature": 0.0, "avg_logprob":
  -0.175953077233356, "compression_ratio": 1.5380434782608696, "no_speech_prob": 0.0010293223895132542},
  {"id": 776, "seek": 485560, "start": 4855.68, "end": 4863.76, "text": " upgraded
  my model. I have model one dot three dot eight, right? And now I, now I, uh, run
  my test", "tokens": [50368, 24133, 452, 2316, 13, 286, 362, 2316, 472, 5893, 1045,
  5893, 3180, 11, 558, 30, 400, 586, 286, 11, 586, 286, 11, 2232, 11, 1190, 452, 1500,
  50772], "temperature": 0.0, "avg_logprob": -0.1391047349910146, "compression_ratio":
  1.641350210970464, "no_speech_prob": 0.0005055960500612855}, {"id": 777, "seek":
  485560, "start": 4863.76, "end": 4869.92, "text": " vectors, my test sentences through
  and I get different vectors. Like how, how much has changed?", "tokens": [50772,
  18875, 11, 452, 1500, 16579, 807, 293, 286, 483, 819, 18875, 13, 1743, 577, 11,
  577, 709, 575, 3105, 30, 51080], "temperature": 0.0, "avg_logprob": -0.1391047349910146,
  "compression_ratio": 1.641350210970464, "no_speech_prob": 0.0005055960500612855},
  {"id": 778, "seek": 485560, "start": 4869.92, "end": 4874.08, "text": " What''s
  the difference there? So there''s this whole world around measuring model drift.
  And there''s", "tokens": [51080, 708, 311, 264, 2649, 456, 30, 407, 456, 311, 341,
  1379, 1002, 926, 13389, 2316, 19699, 13, 400, 456, 311, 51288], "temperature": 0.0,
  "avg_logprob": -0.1391047349910146, "compression_ratio": 1.641350210970464, "no_speech_prob":
  0.0005055960500612855}, {"id": 779, "seek": 485560, "start": 4874.08, "end": 4880.72,
  "text": " some, there''s some interesting open source tools on this already. But
  they''re written in Python.", "tokens": [51288, 512, 11, 456, 311, 512, 1880, 1269,
  4009, 3873, 322, 341, 1217, 13, 583, 436, 434, 3720, 294, 15329, 13, 51620], "temperature":
  0.0, "avg_logprob": -0.1391047349910146, "compression_ratio": 1.641350210970464,
  "no_speech_prob": 0.0005055960500612855}, {"id": 780, "seek": 488072, "start": 4881.52,
  "end": 4885.68, "text": " So now you have to use Python to do all this stuff. So
  I''m trying to understand what,", "tokens": [50404, 407, 586, 291, 362, 281, 764,
  15329, 281, 360, 439, 341, 1507, 13, 407, 286, 478, 1382, 281, 1223, 437, 11, 50612],
  "temperature": 0.0, "avg_logprob": -0.16797809190647575, "compression_ratio": 1.6217391304347826,
  "no_speech_prob": 0.0015828986652195454}, {"id": 781, "seek": 488072, "start": 4886.8,
  "end": 4893.84, "text": " what the tools, uh, what tools could be written that are
  not in Python land. Um, that could expose", "tokens": [50668, 437, 264, 3873, 11,
  2232, 11, 437, 3873, 727, 312, 3720, 300, 366, 406, 294, 15329, 2117, 13, 3301,
  11, 300, 727, 19219, 51020], "temperature": 0.0, "avg_logprob": -0.16797809190647575,
  "compression_ratio": 1.6217391304347826, "no_speech_prob": 0.0015828986652195454},
  {"id": 782, "seek": 488072, "start": 4893.84, "end": 4900.56, "text": " these statistics
  and this important information to people who, um, you know, who don''t want to",
  "tokens": [51020, 613, 12523, 293, 341, 1021, 1589, 281, 561, 567, 11, 1105, 11,
  291, 458, 11, 567, 500, 380, 528, 281, 51356], "temperature": 0.0, "avg_logprob":
  -0.16797809190647575, "compression_ratio": 1.6217391304347826, "no_speech_prob":
  0.0015828986652195454}, {"id": 783, "seek": 488072, "start": 4900.56, "end": 4905.360000000001,
  "text": " marry themselves to Python. Yeah, yeah, absolutely. This sounds like you
  touched also on this", "tokens": [51356, 9747, 2969, 281, 15329, 13, 865, 11, 1338,
  11, 3122, 13, 639, 3263, 411, 291, 9828, 611, 322, 341, 51596], "temperature": 0.0,
  "avg_logprob": -0.16797809190647575, "compression_ratio": 1.6217391304347826, "no_speech_prob":
  0.0015828986652195454}, {"id": 784, "seek": 490536, "start": 4905.36, "end": 4912.32,
  "text": " very important topic, which I think, uh, is, is, uh, known as a metric
  learning where, um,", "tokens": [50364, 588, 1021, 4829, 11, 597, 286, 519, 11,
  2232, 11, 307, 11, 307, 11, 2232, 11, 2570, 382, 257, 20678, 2539, 689, 11, 1105,
  11, 50712], "temperature": 0.0, "avg_logprob": -0.14546428862072172, "compression_ratio":
  1.6428571428571428, "no_speech_prob": 0.002350588794797659}, {"id": 785, "seek":
  490536, "start": 4913.12, "end": 4918.0, "text": " like on one hand, you do want
  to know what is the optimal distance and maybe you need to fine tune", "tokens":
  [50752, 411, 322, 472, 1011, 11, 291, 360, 528, 281, 458, 437, 307, 264, 16252,
  4560, 293, 1310, 291, 643, 281, 2489, 10864, 50996], "temperature": 0.0, "avg_logprob":
  -0.14546428862072172, "compression_ratio": 1.6428571428571428, "no_speech_prob":
  0.002350588794797659}, {"id": 786, "seek": 490536, "start": 4918.0, "end": 4923.759999999999,
  "text": " your model or maybe your data is not good fit for this model and so on.
  But you do need the tools.", "tokens": [50996, 428, 2316, 420, 1310, 428, 1412,
  307, 406, 665, 3318, 337, 341, 2316, 293, 370, 322, 13, 583, 291, 360, 643, 264,
  3873, 13, 51284], "temperature": 0.0, "avg_logprob": -0.14546428862072172, "compression_ratio":
  1.6428571428571428, "no_speech_prob": 0.002350588794797659}, {"id": 787, "seek":
  490536, "start": 4923.759999999999, "end": 4931.759999999999, "text": " Maybe it''s
  something like Cupid for, you know, ranking, um, evaluation and tuning. You would
  also have", "tokens": [51284, 2704, 309, 311, 746, 411, 383, 6127, 337, 11, 291,
  458, 11, 17833, 11, 1105, 11, 13344, 293, 15164, 13, 509, 576, 611, 362, 51684],
  "temperature": 0.0, "avg_logprob": -0.14546428862072172, "compression_ratio": 1.6428571428571428,
  "no_speech_prob": 0.002350588794797659}, {"id": 788, "seek": 493176, "start": 4931.76,
  "end": 4937.2, "text": " some tool which is Cupid like maybe even with the UI way.
  You can load this vectors, visualize them", "tokens": [50364, 512, 2290, 597, 307,
  383, 6127, 411, 1310, 754, 365, 264, 15682, 636, 13, 509, 393, 3677, 341, 18875,
  11, 23273, 552, 50636], "temperature": 0.0, "avg_logprob": -0.17643913200923375,
  "compression_ratio": 1.5776892430278884, "no_speech_prob": 0.003824483370408416},
  {"id": 789, "seek": 493176, "start": 4937.2, "end": 4942.08, "text": " and see,
  okay, how do they fit together? What''s missing and so on and then have the stats
  on it,", "tokens": [50636, 293, 536, 11, 1392, 11, 577, 360, 436, 3318, 1214, 30,
  708, 311, 5361, 293, 370, 322, 293, 550, 362, 264, 18152, 322, 309, 11, 50880],
  "temperature": 0.0, "avg_logprob": -0.17643913200923375, "compression_ratio": 1.5776892430278884,
  "no_speech_prob": 0.003824483370408416}, {"id": 790, "seek": 493176, "start": 4942.08,
  "end": 4948.64, "text": " right? So you can actually run the statistics and, um,
  you know, I''m gonna let Eric write that tool.", "tokens": [50880, 558, 30, 407,
  291, 393, 767, 1190, 264, 12523, 293, 11, 1105, 11, 291, 458, 11, 286, 478, 799,
  718, 9336, 2464, 300, 2290, 13, 51208], "temperature": 0.0, "avg_logprob": -0.17643913200923375,
  "compression_ratio": 1.5776892430278884, "no_speech_prob": 0.003824483370408416},
  {"id": 791, "seek": 493176, "start": 4948.64, "end": 4954.8, "text": " I love Cupid.
  Cupid is so great. Eric, go write Cupid for vector search. Yeah, I think, uh, we
  can", "tokens": [51208, 286, 959, 383, 6127, 13, 383, 6127, 307, 370, 869, 13, 9336,
  11, 352, 2464, 383, 6127, 337, 8062, 3164, 13, 865, 11, 286, 519, 11, 2232, 11,
  321, 393, 51516], "temperature": 0.0, "avg_logprob": -0.17643913200923375, "compression_ratio":
  1.5776892430278884, "no_speech_prob": 0.003824483370408416}, {"id": 792, "seek":
  495480, "start": 4954.8, "end": 4962.72, "text": " pair up on that maybe all of
  us contribute, make it open source. Um, but yeah, um, I think this is", "tokens":
  [50364, 6119, 493, 322, 300, 1310, 439, 295, 505, 10586, 11, 652, 309, 1269, 4009,
  13, 3301, 11, 457, 1338, 11, 1105, 11, 286, 519, 341, 307, 50760], "temperature":
  0.0, "avg_logprob": -0.15817988152597465, "compression_ratio": 1.6458333333333333,
  "no_speech_prob": 0.007086475845426321}, {"id": 793, "seek": 495480, "start": 4962.72,
  "end": 4970.16, "text": " one way to look at it, right? Um, and I think quadrant,
  um, developers, they, they push the metric", "tokens": [50760, 472, 636, 281, 574,
  412, 309, 11, 558, 30, 3301, 11, 293, 286, 519, 46856, 11, 1105, 11, 8849, 11, 436,
  11, 436, 2944, 264, 20678, 51132], "temperature": 0.0, "avg_logprob": -0.15817988152597465,
  "compression_ratio": 1.6458333333333333, "no_speech_prob": 0.007086475845426321},
  {"id": 794, "seek": 495480, "start": 4970.16, "end": 4976.320000000001, "text":
  " learning quite heavily forward by the time this podcast is, uh, this episode is
  out. There will be", "tokens": [51132, 2539, 1596, 10950, 2128, 538, 264, 565, 341,
  7367, 307, 11, 2232, 11, 341, 3500, 307, 484, 13, 821, 486, 312, 51440], "temperature":
  0.0, "avg_logprob": -0.15817988152597465, "compression_ratio": 1.6458333333333333,
  "no_speech_prob": 0.007086475845426321}, {"id": 795, "seek": 495480, "start": 4976.320000000001,
  "end": 4984.08, "text": " another episode with a developer from quadrant who is
  actually very big on, on this idea of metric", "tokens": [51440, 1071, 3500, 365,
  257, 10754, 490, 46856, 567, 307, 767, 588, 955, 322, 11, 322, 341, 1558, 295, 20678,
  51828], "temperature": 0.0, "avg_logprob": -0.15817988152597465, "compression_ratio":
  1.6458333333333333, "no_speech_prob": 0.007086475845426321}, {"id": 796, "seek":
  498408, "start": 4984.08, "end": 4990.88, "text": " learning. And, uh, he opens
  sources, of course, everything. And I mean, he offers tools and also like,", "tokens":
  [50364, 2539, 13, 400, 11, 2232, 11, 415, 9870, 7139, 11, 295, 1164, 11, 1203, 13,
  400, 286, 914, 11, 415, 7736, 3873, 293, 611, 411, 11, 50704], "temperature": 0.0,
  "avg_logprob": -0.13319195441479953, "compression_ratio": 1.6178861788617886, "no_speech_prob":
  0.012398069724440575}, {"id": 797, "seek": 498408, "start": 4991.76, "end": 4996.8,
  "text": " papers that you can read and indicate yourself on this space. I think
  this is something that", "tokens": [50748, 10577, 300, 291, 393, 1401, 293, 13330,
  1803, 322, 341, 1901, 13, 286, 519, 341, 307, 746, 300, 51000], "temperature": 0.0,
  "avg_logprob": -0.13319195441479953, "compression_ratio": 1.6178861788617886, "no_speech_prob":
  0.012398069724440575}, {"id": 798, "seek": 498408, "start": 4996.8, "end": 5002.96,
  "text": " barely is scratched at the moment by the community, by, by even the end
  users, you know, they don''t", "tokens": [51000, 10268, 307, 40513, 412, 264, 1623,
  538, 264, 1768, 11, 538, 11, 538, 754, 264, 917, 5022, 11, 291, 458, 11, 436, 500,
  380, 51308], "temperature": 0.0, "avg_logprob": -0.13319195441479953, "compression_ratio":
  1.6178861788617886, "no_speech_prob": 0.012398069724440575}, {"id": 799, "seek":
  498408, "start": 5002.96, "end": 5009.84, "text": " know. Okay, I take clip model.
  I have the images, plug them in together, works fine. I''m done. What if", "tokens":
  [51308, 458, 13, 1033, 11, 286, 747, 7353, 2316, 13, 286, 362, 264, 5267, 11, 5452,
  552, 294, 1214, 11, 1985, 2489, 13, 286, 478, 1096, 13, 708, 498, 51652], "temperature":
  0.0, "avg_logprob": -0.13319195441479953, "compression_ratio": 1.6178861788617886,
  "no_speech_prob": 0.012398069724440575}, {"id": 800, "seek": 500984, "start": 5009.84,
  "end": 5016.0, "text": " it doesn''t work? What if you have some images, you never
  find them for any query, but you do", "tokens": [50364, 309, 1177, 380, 589, 30,
  708, 498, 291, 362, 512, 5267, 11, 291, 1128, 915, 552, 337, 604, 14581, 11, 457,
  291, 360, 50672], "temperature": 0.0, "avg_logprob": -0.11690245027895327, "compression_ratio":
  1.7330960854092528, "no_speech_prob": 0.0021353857591748238}, {"id": 801, "seek":
  500984, "start": 5016.0, "end": 5020.8, "text": " want to find them because it''s
  a name of some product that was recently released and you do want to,", "tokens":
  [50672, 528, 281, 915, 552, 570, 309, 311, 257, 1315, 295, 512, 1674, 300, 390,
  3938, 4736, 293, 291, 360, 528, 281, 11, 50912], "temperature": 0.0, "avg_logprob":
  -0.11690245027895327, "compression_ratio": 1.7330960854092528, "no_speech_prob":
  0.0021353857591748238}, {"id": 802, "seek": 500984, "start": 5020.8, "end": 5027.76,
  "text": " to showcase it, right? And you''re not using keyword search there. It''s
  a name. You''re using, um,", "tokens": [50912, 281, 20388, 309, 11, 558, 30, 400,
  291, 434, 406, 1228, 20428, 3164, 456, 13, 467, 311, 257, 1315, 13, 509, 434, 1228,
  11, 1105, 11, 51260], "temperature": 0.0, "avg_logprob": -0.11690245027895327, "compression_ratio":
  1.7330960854092528, "no_speech_prob": 0.0021353857591748238}, {"id": 803, "seek":
  500984, "start": 5027.76, "end": 5032.8, "text": " vectors to retrieve it, right?
  So it thinks like this. I mean, it''s kind of like, there''s a bunch of", "tokens":
  [51260, 18875, 281, 30254, 309, 11, 558, 30, 407, 309, 7309, 411, 341, 13, 286,
  914, 11, 309, 311, 733, 295, 411, 11, 456, 311, 257, 3840, 295, 51512], "temperature":
  0.0, "avg_logprob": -0.11690245027895327, "compression_ratio": 1.7330960854092528,
  "no_speech_prob": 0.0021353857591748238}, {"id": 804, "seek": 500984, "start": 5032.8,
  "end": 5039.76, "text": " topics there. One, another one favorite that I like is
  the, uh, robustness, right? So if I have", "tokens": [51512, 8378, 456, 13, 1485,
  11, 1071, 472, 2954, 300, 286, 411, 307, 264, 11, 2232, 11, 13956, 1287, 11, 558,
  30, 407, 498, 286, 362, 51860], "temperature": 0.0, "avg_logprob": -0.11690245027895327,
  "compression_ratio": 1.7330960854092528, "no_speech_prob": 0.0021353857591748238},
  {"id": 805, "seek": 503976, "start": 5040.16, "end": 5046.8, "text": " an aircraft,
  I rotated a little bit and all of a sudden I find kittens instead of the aircrafts.",
  "tokens": [50384, 364, 9465, 11, 286, 42146, 257, 707, 857, 293, 439, 295, 257,
  3990, 286, 915, 47363, 2602, 295, 264, 9465, 82, 13, 50716], "temperature": 0.0,
  "avg_logprob": -0.20732696383607155, "compression_ratio": 1.5991902834008098, "no_speech_prob":
  0.005572644528001547}, {"id": 806, "seek": 503976, "start": 5046.8, "end": 5051.76,
  "text": " And this is what Connor Shorten showed yesterday on on on the genometer
  and was amazing. I mean,", "tokens": [50716, 400, 341, 307, 437, 33133, 16881, 268,
  4712, 5186, 322, 322, 322, 264, 1049, 13606, 293, 390, 2243, 13, 286, 914, 11, 50964],
  "temperature": 0.0, "avg_logprob": -0.20732696383607155, "compression_ratio": 1.5991902834008098,
  "no_speech_prob": 0.005572644528001547}, {"id": 807, "seek": 503976, "start": 5051.76,
  "end": 5058.16, "text": " robustness. You just change slightly your input and you
  just, yeah, it doesn''t work. So I think there", "tokens": [50964, 13956, 1287,
  13, 509, 445, 1319, 4748, 428, 4846, 293, 291, 445, 11, 1338, 11, 309, 1177, 380,
  589, 13, 407, 286, 519, 456, 51284], "temperature": 0.0, "avg_logprob": -0.20732696383607155,
  "compression_ratio": 1.5991902834008098, "no_speech_prob": 0.005572644528001547},
  {"id": 808, "seek": 503976, "start": 5058.16, "end": 5064.4800000000005, "text":
  " is a lot of things missing, but like you, like from what I sense in your answer,
  like it feels like", "tokens": [51284, 307, 257, 688, 295, 721, 5361, 11, 457, 411,
  291, 11, 411, 490, 437, 286, 2020, 294, 428, 1867, 11, 411, 309, 3417, 411, 51600],
  "temperature": 0.0, "avg_logprob": -0.20732696383607155, "compression_ratio": 1.5991902834008098,
  "no_speech_prob": 0.005572644528001547}, {"id": 809, "seek": 506448, "start": 5064.48,
  "end": 5070.799999999999, "text": " you do still want to keep your focus on mighty
  and push that as further along as possible, right?", "tokens": [50364, 291, 360,
  920, 528, 281, 1066, 428, 1879, 322, 21556, 293, 2944, 300, 382, 3052, 2051, 382,
  1944, 11, 558, 30, 50680], "temperature": 0.0, "avg_logprob": -0.16498756408691406,
  "compression_ratio": 1.5340314136125655, "no_speech_prob": 0.0002988640044350177},
  {"id": 810, "seek": 506448, "start": 5075.12, "end": 5081.839999999999, "text":
  " Yes. And I want to, what I really want is I, I love that people download and install
  it and use it", "tokens": [50896, 1079, 13, 400, 286, 528, 281, 11, 437, 286, 534,
  528, 307, 286, 11, 286, 959, 300, 561, 5484, 293, 3625, 309, 293, 764, 309, 51232],
  "temperature": 0.0, "avg_logprob": -0.16498756408691406, "compression_ratio": 1.5340314136125655,
  "no_speech_prob": 0.0002988640044350177}, {"id": 811, "seek": 506448, "start": 5081.839999999999,
  "end": 5088.24, "text": " and do whatever they want, uh, to get vectors with my,
  that''s awesome. I''m really trying to find", "tokens": [51232, 293, 360, 2035,
  436, 528, 11, 2232, 11, 281, 483, 18875, 365, 452, 11, 300, 311, 3476, 13, 286,
  478, 534, 1382, 281, 915, 51552], "temperature": 0.0, "avg_logprob": -0.16498756408691406,
  "compression_ratio": 1.5340314136125655, "no_speech_prob": 0.0002988640044350177},
  {"id": 812, "seek": 508824, "start": 5088.24, "end": 5095.76, "text": " partners.
  I''m really trying to find partners who, um, who want to just really make it super
  easy", "tokens": [50364, 4462, 13, 286, 478, 534, 1382, 281, 915, 4462, 567, 11,
  1105, 11, 567, 528, 281, 445, 534, 652, 309, 1687, 1858, 50740], "temperature":
  0.0, "avg_logprob": -0.11893547148931594, "compression_ratio": 1.6132596685082874,
  "no_speech_prob": 0.0005097273970022798}, {"id": 813, "seek": 508824, "start": 5096.719999999999,
  "end": 5104.88, "text": " uh, to do, uh, inference, model inference at scale. Um,
  so for example, I haven''t gotten any", "tokens": [50788, 2232, 11, 281, 360, 11,
  2232, 11, 38253, 11, 2316, 38253, 412, 4373, 13, 3301, 11, 370, 337, 1365, 11, 286,
  2378, 380, 5768, 604, 51196], "temperature": 0.0, "avg_logprob": -0.11893547148931594,
  "compression_ratio": 1.6132596685082874, "no_speech_prob": 0.0005097273970022798},
  {"id": 814, "seek": 508824, "start": 5104.88, "end": 5112.08, "text": " replies.
  I''ve been like spamming, uh, not spamming. I''ve been, uh, emailing and trying
  to get in touch", "tokens": [51196, 42289, 13, 286, 600, 668, 411, 24028, 2810,
  11, 2232, 11, 406, 24028, 2810, 13, 286, 600, 668, 11, 2232, 11, 3796, 278, 293,
  1382, 281, 483, 294, 2557, 51556], "temperature": 0.0, "avg_logprob": -0.11893547148931594,
  "compression_ratio": 1.6132596685082874, "no_speech_prob": 0.0005097273970022798},
  {"id": 815, "seek": 511208, "start": 5112.24, "end": 5118.32, "text": " with like
  cloud cloud providers, right, to say serverless inference. If you could offer serverless",
  "tokens": [50372, 365, 411, 4588, 4588, 11330, 11, 558, 11, 281, 584, 7154, 1832,
  38253, 13, 759, 291, 727, 2626, 7154, 1832, 50676], "temperature": 0.0, "avg_logprob":
  -0.13872390747070312, "compression_ratio": 1.7008547008547008, "no_speech_prob":
  0.000725920544937253}, {"id": 816, "seek": 511208, "start": 5118.32, "end": 5124.72,
  "text": " inference, right, through lambdas or whatever, that''s like so many people
  are asking for that, you know,", "tokens": [50676, 38253, 11, 558, 11, 807, 10097,
  27476, 420, 2035, 11, 300, 311, 411, 370, 867, 561, 366, 3365, 337, 300, 11, 291,
  458, 11, 50996], "temperature": 0.0, "avg_logprob": -0.13872390747070312, "compression_ratio":
  1.7008547008547008, "no_speech_prob": 0.000725920544937253}, {"id": 817, "seek":
  511208, "start": 5125.6, "end": 5132.88, "text": " you can''t do that with Python
  tools these days. Um, you can do it. It''s just going to, it would take", "tokens":
  [51040, 291, 393, 380, 360, 300, 365, 15329, 3873, 613, 1708, 13, 3301, 11, 291,
  393, 360, 309, 13, 467, 311, 445, 516, 281, 11, 309, 576, 747, 51404], "temperature":
  0.0, "avg_logprob": -0.13872390747070312, "compression_ratio": 1.7008547008547008,
  "no_speech_prob": 0.000725920544937253}, {"id": 818, "seek": 511208, "start": 5132.88,
  "end": 5138.48, "text": " forever and it would be really expensive and really slow.
  Um, but there''s such an opportunity", "tokens": [51404, 5680, 293, 309, 576, 312,
  534, 5124, 293, 534, 2964, 13, 3301, 11, 457, 456, 311, 1270, 364, 2650, 51684],
  "temperature": 0.0, "avg_logprob": -0.13872390747070312, "compression_ratio": 1.7008547008547008,
  "no_speech_prob": 0.000725920544937253}, {"id": 819, "seek": 513848, "start": 5139.28,
  "end": 5148.16, "text": " for cloud providers to make it super easy. So you can
  have, you know, you want to get content from,", "tokens": [50404, 337, 4588, 11330,
  281, 652, 309, 1687, 1858, 13, 407, 291, 393, 362, 11, 291, 458, 11, 291, 528, 281,
  483, 2701, 490, 11, 50848], "temperature": 0.0, "avg_logprob": -0.10755076127893784,
  "compression_ratio": 1.6553191489361703, "no_speech_prob": 0.001585534424521029},
  {"id": 820, "seek": 513848, "start": 5148.959999999999, "end": 5154.32, "text":
  " from point A into, uh, into your recommendation engine or your vector database
  or whatever,", "tokens": [50888, 490, 935, 316, 666, 11, 2232, 11, 666, 428, 11879,
  2848, 420, 428, 8062, 8149, 420, 2035, 11, 51156], "temperature": 0.0, "avg_logprob":
  -0.10755076127893784, "compression_ratio": 1.6553191489361703, "no_speech_prob":
  0.001585534424521029}, {"id": 821, "seek": 513848, "start": 5154.32, "end": 5160.5599999999995,
  "text": " you know, do you want to stand up like the big GPU server in the middle
  to get this? No, you don''t", "tokens": [51156, 291, 458, 11, 360, 291, 528, 281,
  1463, 493, 411, 264, 955, 18407, 7154, 294, 264, 2808, 281, 483, 341, 30, 883, 11,
  291, 500, 380, 51468], "temperature": 0.0, "avg_logprob": -0.10755076127893784,
  "compression_ratio": 1.6553191489361703, "no_speech_prob": 0.001585534424521029},
  {"id": 822, "seek": 513848, "start": 5160.5599999999995, "end": 5165.5199999999995,
  "text": " want to do that. Um, if you can avoid it. So how about something that''s
  that serverless and people", "tokens": [51468, 528, 281, 360, 300, 13, 3301, 11,
  498, 291, 393, 5042, 309, 13, 407, 577, 466, 746, 300, 311, 300, 7154, 1832, 293,
  561, 51716], "temperature": 0.0, "avg_logprob": -0.10755076127893784, "compression_ratio":
  1.6553191489361703, "no_speech_prob": 0.001585534424521029}, {"id": 823, "seek":
  516552, "start": 5165.52, "end": 5171.120000000001, "text": " can just run? So I''m
  trying to find partners there. I''m trying to find partners who, uh, who have",
  "tokens": [50364, 393, 445, 1190, 30, 407, 286, 478, 1382, 281, 915, 4462, 456,
  13, 286, 478, 1382, 281, 915, 4462, 567, 11, 2232, 11, 567, 362, 50644], "temperature":
  0.0, "avg_logprob": -0.1581282948338708, "compression_ratio": 1.84375, "no_speech_prob":
  0.0009631191496737301}, {"id": 824, "seek": 516552, "start": 5172.8, "end": 5179.52,
  "text": " search platforms and, um, and other and other platforms or just see this
  as a Lego and their stack", "tokens": [50728, 3164, 9473, 293, 11, 1105, 11, 293,
  661, 293, 661, 9473, 420, 445, 536, 341, 382, 257, 28761, 293, 641, 8630, 51064],
  "temperature": 0.0, "avg_logprob": -0.1581282948338708, "compression_ratio": 1.84375,
  "no_speech_prob": 0.0009631191496737301}, {"id": 825, "seek": 516552, "start": 5180.0,
  "end": 5185.120000000001, "text": " and things that''s going to make it easier and
  they don''t want to, you know, hire a team and spend", "tokens": [51088, 293, 721,
  300, 311, 516, 281, 652, 309, 3571, 293, 436, 500, 380, 528, 281, 11, 291, 458,
  11, 11158, 257, 1469, 293, 3496, 51344], "temperature": 0.0, "avg_logprob": -0.1581282948338708,
  "compression_ratio": 1.84375, "no_speech_prob": 0.0009631191496737301}, {"id": 826,
  "seek": 516552, "start": 5185.120000000001, "end": 5189.84, "text": " months building
  this thing and trying to figure it out. Um, you can do that of course. Go, uh,",
  "tokens": [51344, 2493, 2390, 341, 551, 293, 1382, 281, 2573, 309, 484, 13, 3301,
  11, 291, 393, 360, 300, 295, 1164, 13, 1037, 11, 2232, 11, 51580], "temperature":
  0.0, "avg_logprob": -0.1581282948338708, "compression_ratio": 1.84375, "no_speech_prob":
  0.0009631191496737301}, {"id": 827, "seek": 516552, "start": 5189.84, "end": 5192.4800000000005,
  "text": " go do that, but, you know, you can save yourself a lot of time and pay
  and buy it.", "tokens": [51580, 352, 360, 300, 11, 457, 11, 291, 458, 11, 291, 393,
  3155, 1803, 257, 688, 295, 565, 293, 1689, 293, 2256, 309, 13, 51712], "temperature":
  0.0, "avg_logprob": -0.1581282948338708, "compression_ratio": 1.84375, "no_speech_prob":
  0.0009631191496737301}, {"id": 828, "seek": 519248, "start": 5193.28, "end": 5195.759999999999,
  "text": " Um, by working with stuff that''s already there.", "tokens": [50404, 3301,
  11, 538, 1364, 365, 1507, 300, 311, 1217, 456, 13, 50528], "temperature": 0.0, "avg_logprob":
  -0.24413514368742414, "compression_ratio": 1.5905511811023623, "no_speech_prob":
  0.005984840914607048}, {"id": 829, "seek": 519248, "start": 5197.2, "end": 5200.959999999999,
  "text": " Yeah, that makes sense. I mean, probably companies like the likes of",
  "tokens": [50600, 865, 11, 300, 1669, 2020, 13, 286, 914, 11, 1391, 3431, 411, 264,
  5902, 295, 50788], "temperature": 0.0, "avg_logprob": -0.24413514368742414, "compression_ratio":
  1.5905511811023623, "no_speech_prob": 0.005984840914607048}, {"id": 830, "seek":
  519248, "start": 5200.959999999999, "end": 5208.639999999999, "text": " Algolea
  or, right, exactly, but potentially elastic, you know, because they, both of these,",
  "tokens": [50788, 967, 1571, 306, 64, 420, 11, 558, 11, 2293, 11, 457, 7263, 17115,
  11, 291, 458, 11, 570, 436, 11, 1293, 295, 613, 11, 51172], "temperature": 0.0,
  "avg_logprob": -0.24413514368742414, "compression_ratio": 1.5905511811023623, "no_speech_prob":
  0.005984840914607048}, {"id": 831, "seek": 519248, "start": 5209.44, "end": 5215.28,
  "text": " want to get closer to the neural search even though maybe they were not
  wired up originally to", "tokens": [51212, 528, 281, 483, 4966, 281, 264, 18161,
  3164, 754, 1673, 1310, 436, 645, 406, 27415, 493, 7993, 281, 51504], "temperature":
  0.0, "avg_logprob": -0.24413514368742414, "compression_ratio": 1.5905511811023623,
  "no_speech_prob": 0.005984840914607048}, {"id": 832, "seek": 519248, "start": 5215.28,
  "end": 5221.5199999999995, "text": " be vector search databases, but they do have
  the components like elastic based on Lussin and Algolea", "tokens": [51504, 312,
  8062, 3164, 22380, 11, 457, 436, 360, 362, 264, 6677, 411, 17115, 2361, 322, 441,
  2023, 259, 293, 967, 1571, 306, 64, 51816], "temperature": 0.0, "avg_logprob": -0.24413514368742414,
  "compression_ratio": 1.5905511811023623, "no_speech_prob": 0.005984840914607048},
  {"id": 833, "seek": 522152, "start": 5222.320000000001, "end": 5227.6, "text": "
  probably based also Lussin. I''m not sure, but I''m sure that they''re looking at
  this field. So I mean,", "tokens": [50404, 1391, 2361, 611, 441, 2023, 259, 13,
  286, 478, 406, 988, 11, 457, 286, 478, 988, 300, 436, 434, 1237, 412, 341, 2519,
  13, 407, 286, 914, 11, 50668], "temperature": 0.0, "avg_logprob": -0.19526315391610521,
  "compression_ratio": 1.592, "no_speech_prob": 0.0017663463950157166}, {"id": 834,
  "seek": 522152, "start": 5227.6, "end": 5234.400000000001, "text": " for them and
  now we are getting a little bit into MLOPS and Vision, um, that you also shared
  a little", "tokens": [50668, 337, 552, 293, 586, 321, 366, 1242, 257, 707, 857,
  666, 21601, 46, 6273, 293, 25170, 11, 1105, 11, 300, 291, 611, 5507, 257, 707, 51008],
  "temperature": 0.0, "avg_logprob": -0.19526315391610521, "compression_ratio": 1.592,
  "no_speech_prob": 0.0017663463950157166}, {"id": 835, "seek": 522152, "start": 5234.400000000001,
  "end": 5244.320000000001, "text": " bit ahead of time that, um, might it could be
  one of the components in the MLOPS ecosystem, right?", "tokens": [51008, 857, 2286,
  295, 565, 300, 11, 1105, 11, 1062, 309, 727, 312, 472, 295, 264, 6677, 294, 264,
  21601, 46, 6273, 11311, 11, 558, 30, 51504], "temperature": 0.0, "avg_logprob":
  -0.19526315391610521, "compression_ratio": 1.592, "no_speech_prob": 0.0017663463950157166},
  {"id": 836, "seek": 522152, "start": 5245.76, "end": 5251.120000000001, "text":
  " Yeah, absolutely. Not just a standalone kind of script, which I download and then
  I''m thinking,", "tokens": [51576, 865, 11, 3122, 13, 1726, 445, 257, 37454, 733,
  295, 5755, 11, 597, 286, 5484, 293, 550, 286, 478, 1953, 11, 51844], "temperature":
  0.0, "avg_logprob": -0.19526315391610521, "compression_ratio": 1.592, "no_speech_prob":
  0.0017663463950157166}, {"id": 837, "seek": 525112, "start": 5251.12, "end": 5257.5199999999995,
  "text": " okay, where do I plug it in? Right? I mean, if it was, if it was, are
  you thinking in that direction", "tokens": [50364, 1392, 11, 689, 360, 286, 5452,
  309, 294, 30, 1779, 30, 286, 914, 11, 498, 309, 390, 11, 498, 309, 390, 11, 366,
  291, 1953, 294, 300, 3513, 50684], "temperature": 0.0, "avg_logprob": -0.17146593048459008,
  "compression_ratio": 1.4607843137254901, "no_speech_prob": 0.0010670768097043037},
  {"id": 838, "seek": 525112, "start": 5257.5199999999995, "end": 5265.68, "text":
  " as well yourself? Like, okay, identifying the tools and systems where MIT could
  kind of like play", "tokens": [50684, 382, 731, 1803, 30, 1743, 11, 1392, 11, 16696,
  264, 3873, 293, 3652, 689, 13100, 727, 733, 295, 411, 862, 51092], "temperature":
  0.0, "avg_logprob": -0.17146593048459008, "compression_ratio": 1.4607843137254901,
  "no_speech_prob": 0.0010670768097043037}, {"id": 839, "seek": 525112, "start": 5265.68,
  "end": 5280.24, "text": " a long role of the embedding software? Yeah, absolutely.
  Um, it''s, I have to, if, the other thing I", "tokens": [51092, 257, 938, 3090,
  295, 264, 12240, 3584, 4722, 30, 865, 11, 3122, 13, 3301, 11, 309, 311, 11, 286,
  362, 281, 11, 498, 11, 264, 661, 551, 286, 51820], "temperature": 0.0, "avg_logprob":
  -0.17146593048459008, "compression_ratio": 1.4607843137254901, "no_speech_prob":
  0.0010670768097043037}, {"id": 840, "seek": 528024, "start": 5280.24, "end": 5285.599999999999,
  "text": " want to figure out is, does it make sense as it is right now as a, as
  a web server? Like that for", "tokens": [50364, 528, 281, 2573, 484, 307, 11, 775,
  309, 652, 2020, 382, 309, 307, 558, 586, 382, 257, 11, 382, 257, 3670, 7154, 30,
  1743, 300, 337, 50632], "temperature": 0.0, "avg_logprob": -0.1551298630976044,
  "compression_ratio": 1.6055776892430278, "no_speech_prob": 0.0005562129081226885},
  {"id": 841, "seek": 528024, "start": 5285.599999999999, "end": 5292.08, "text":
  " every case, probably not. There''s probably situations. GRPC was one request,
  um, that I have to figure", "tokens": [50632, 633, 1389, 11, 1391, 406, 13, 821,
  311, 1391, 6851, 13, 10903, 12986, 390, 472, 5308, 11, 1105, 11, 300, 286, 362,
  281, 2573, 50956], "temperature": 0.0, "avg_logprob": -0.1551298630976044, "compression_ratio":
  1.6055776892430278, "no_speech_prob": 0.0005562129081226885}, {"id": 842, "seek":
  528024, "start": 5292.08, "end": 5298.24, "text": " that out. So that makes it a
  little bit easier to, to, um, to bind it to certain application layers.", "tokens":
  [50956, 300, 484, 13, 407, 300, 1669, 309, 257, 707, 857, 3571, 281, 11, 281, 11,
  1105, 11, 281, 14786, 309, 281, 1629, 3861, 7914, 13, 51264], "temperature": 0.0,
  "avg_logprob": -0.1551298630976044, "compression_ratio": 1.6055776892430278, "no_speech_prob":
  0.0005562129081226885}, {"id": 843, "seek": 528024, "start": 5299.36, "end": 5308.96,
  "text": " Uh, but yeah, it''s, it''s meant to be flexible for you sticking a model
  that your model, um, you know,", "tokens": [51320, 4019, 11, 457, 1338, 11, 309,
  311, 11, 309, 311, 4140, 281, 312, 11358, 337, 291, 13465, 257, 2316, 300, 428,
  2316, 11, 1105, 11, 291, 458, 11, 51800], "temperature": 0.0, "avg_logprob": -0.1551298630976044,
  "compression_ratio": 1.6055776892430278, "no_speech_prob": 0.0005562129081226885},
  {"id": 844, "seek": 530896, "start": 5309.84, "end": 5316.8, "text": " and, and
  you, you run it how you want. The, the other thing that I found was that I, I met
  a lot of", "tokens": [50408, 293, 11, 293, 291, 11, 291, 1190, 309, 577, 291, 528,
  13, 440, 11, 264, 661, 551, 300, 286, 1352, 390, 300, 286, 11, 286, 1131, 257, 688,
  295, 50756], "temperature": 0.0, "avg_logprob": -0.18921325798321487, "compression_ratio":
  1.7295373665480427, "no_speech_prob": 0.001124868169426918}, {"id": 845, "seek":
  530896, "start": 5316.8, "end": 5322.0, "text": " people who were like scratching
  their heads saying, like, which model should I use also, right?", "tokens": [50756,
  561, 567, 645, 411, 29699, 641, 8050, 1566, 11, 411, 11, 597, 2316, 820, 286, 764,
  611, 11, 558, 30, 51016], "temperature": 0.0, "avg_logprob": -0.18921325798321487,
  "compression_ratio": 1.7295373665480427, "no_speech_prob": 0.001124868169426918},
  {"id": 846, "seek": 530896, "start": 5322.0, "end": 5326.24, "text": " As my, my
  first model or, or whatever. And I just want to start playing around with this.
  So that''s", "tokens": [51016, 1018, 452, 11, 452, 700, 2316, 420, 11, 420, 2035,
  13, 400, 286, 445, 528, 281, 722, 2433, 926, 365, 341, 13, 407, 300, 311, 51228],
  "temperature": 0.0, "avg_logprob": -0.18921325798321487, "compression_ratio": 1.7295373665480427,
  "no_speech_prob": 0.001124868169426918}, {"id": 847, "seek": 530896, "start": 5326.24,
  "end": 5331.68, "text": " the other thing I did is I, is I have like default models
  that I, that I chose that I know work well", "tokens": [51228, 264, 661, 551, 286,
  630, 307, 286, 11, 307, 286, 362, 411, 7576, 5245, 300, 286, 11, 300, 286, 5111,
  300, 286, 458, 589, 731, 51500], "temperature": 0.0, "avg_logprob": -0.18921325798321487,
  "compression_ratio": 1.7295373665480427, "no_speech_prob": 0.001124868169426918},
  {"id": 848, "seek": 530896, "start": 5331.68, "end": 5337.2, "text": " because,
  you know, especially like Neil''s rumors, he''s amazing and he''s done amazing,
  um,", "tokens": [51500, 570, 11, 291, 458, 11, 2318, 411, 18615, 311, 21201, 11,
  415, 311, 2243, 293, 415, 311, 1096, 2243, 11, 1105, 11, 51776], "temperature":
  0.0, "avg_logprob": -0.18921325798321487, "compression_ratio": 1.7295373665480427,
  "no_speech_prob": 0.001124868169426918}, {"id": 849, "seek": 533720, "start": 5338.16,
  "end": 5344.08, "text": " community development around, around expert and the models
  that he''s trained and the", "tokens": [50412, 1768, 3250, 926, 11, 926, 5844, 293,
  264, 5245, 300, 415, 311, 8895, 293, 264, 50708], "temperature": 0.0, "avg_logprob":
  -0.12591260429320297, "compression_ratio": 1.7732342007434945, "no_speech_prob":
  0.0006102172774262726}, {"id": 850, "seek": 533720, "start": 5344.08, "end": 5348.72,
  "text": " documentation he''s published around why certain models are good and others
  are bad. So other people,", "tokens": [50708, 14333, 415, 311, 6572, 926, 983, 1629,
  5245, 366, 665, 293, 2357, 366, 1578, 13, 407, 661, 561, 11, 50940], "temperature":
  0.0, "avg_logprob": -0.12591260429320297, "compression_ratio": 1.7732342007434945,
  "no_speech_prob": 0.0006102172774262726}, {"id": 851, "seek": 533720, "start": 5348.72,
  "end": 5353.2, "text": " they don''t know of, of, of this stuff. So it''s just like,
  well, you don''t have to go off and learn", "tokens": [50940, 436, 500, 380, 458,
  295, 11, 295, 11, 295, 341, 1507, 13, 407, 309, 311, 445, 411, 11, 731, 11, 291,
  500, 380, 362, 281, 352, 766, 293, 1466, 51164], "temperature": 0.0, "avg_logprob":
  -0.12591260429320297, "compression_ratio": 1.7732342007434945, "no_speech_prob":
  0.0006102172774262726}, {"id": 852, "seek": 533720, "start": 5353.2, "end": 5359.5199999999995,
  "text": " and understand, um, right away, why, why I should choose one model versus
  another. It''s a hard", "tokens": [51164, 293, 1223, 11, 1105, 11, 558, 1314, 11,
  983, 11, 983, 286, 820, 2826, 472, 2316, 5717, 1071, 13, 467, 311, 257, 1152, 51480],
  "temperature": 0.0, "avg_logprob": -0.12591260429320297, "compression_ratio": 1.7732342007434945,
  "no_speech_prob": 0.0006102172774262726}, {"id": 853, "seek": 533720, "start": 5359.5199999999995,
  "end": 5363.84, "text": " decision to make. So there''s some, there''s some defaults
  that I chose. So it''s really easy to get", "tokens": [51480, 3537, 281, 652, 13,
  407, 456, 311, 512, 11, 456, 311, 512, 7576, 82, 300, 286, 5111, 13, 407, 309, 311,
  534, 1858, 281, 483, 51696], "temperature": 0.0, "avg_logprob": -0.12591260429320297,
  "compression_ratio": 1.7732342007434945, "no_speech_prob": 0.0006102172774262726},
  {"id": 854, "seek": 536384, "start": 5363.84, "end": 5368.400000000001, "text":
  " started. So the, so the vectors themselves right off the bat or if you do question
  answering,", "tokens": [50364, 1409, 13, 407, 264, 11, 370, 264, 18875, 2969, 558,
  766, 264, 7362, 420, 498, 291, 360, 1168, 13430, 11, 50592], "temperature": 0.0,
  "avg_logprob": -0.1491843561331431, "compression_ratio": 1.6075949367088607, "no_speech_prob":
  0.0009784846333786845}, {"id": 855, "seek": 536384, "start": 5368.400000000001,
  "end": 5375.28, "text": " it''ll be, it''ll be pretty good. Like for, for regular,
  regular English, not domain specific.", "tokens": [50592, 309, 603, 312, 11, 309,
  603, 312, 1238, 665, 13, 1743, 337, 11, 337, 3890, 11, 3890, 3669, 11, 406, 9274,
  2685, 13, 50936], "temperature": 0.0, "avg_logprob": -0.1491843561331431, "compression_ratio":
  1.6075949367088607, "no_speech_prob": 0.0009784846333786845}, {"id": 856, "seek":
  536384, "start": 5375.28, "end": 5381.28, "text": " You, you still have to do fine
  tuning for most cases. But you''re not going to start fine tuning", "tokens": [50936,
  509, 11, 291, 920, 362, 281, 360, 2489, 15164, 337, 881, 3331, 13, 583, 291, 434,
  406, 516, 281, 722, 2489, 15164, 51236], "temperature": 0.0, "avg_logprob": -0.1491843561331431,
  "compression_ratio": 1.6075949367088607, "no_speech_prob": 0.0009784846333786845},
  {"id": 857, "seek": 536384, "start": 5381.28, "end": 5387.84, "text": " before you
  even know how this thing performs like in the beginning, right? You want to try
  a model", "tokens": [51236, 949, 291, 754, 458, 577, 341, 551, 26213, 411, 294,
  264, 2863, 11, 558, 30, 509, 528, 281, 853, 257, 2316, 51564], "temperature": 0.0,
  "avg_logprob": -0.1491843561331431, "compression_ratio": 1.6075949367088607, "no_speech_prob":
  0.0009784846333786845}, {"id": 858, "seek": 538784, "start": 5387.92, "end": 5395.52,
  "text": " and see what, how close it is. Um, so there''s some starting, starting
  work there. I know Algolia is", "tokens": [50368, 293, 536, 437, 11, 577, 1998,
  309, 307, 13, 3301, 11, 370, 456, 311, 512, 2891, 11, 2891, 589, 456, 13, 286, 458,
  967, 70, 29760, 307, 50748], "temperature": 0.0, "avg_logprob": -0.17935154801708156,
  "compression_ratio": 1.6556016597510372, "no_speech_prob": 0.015115798451006413},
  {"id": 859, "seek": 538784, "start": 5395.52, "end": 5399.52, "text": " getting
  to the vector search stuff. So I don''t know. Maybe they, they, maybe they don''t
  know how to", "tokens": [50748, 1242, 281, 264, 8062, 3164, 1507, 13, 407, 286,
  500, 380, 458, 13, 2704, 436, 11, 436, 11, 1310, 436, 500, 380, 458, 577, 281, 50948],
  "temperature": 0.0, "avg_logprob": -0.17935154801708156, "compression_ratio": 1.6556016597510372,
  "no_speech_prob": 0.015115798451006413}, {"id": 860, "seek": 538784, "start": 5399.52,
  "end": 5405.84, "text": " choose a model. So you guys, you can use my default model
  if you want. It''s just a, yeah, absolutely.", "tokens": [50948, 2826, 257, 2316,
  13, 407, 291, 1074, 11, 291, 393, 764, 452, 7576, 2316, 498, 291, 528, 13, 467,
  311, 445, 257, 11, 1338, 11, 3122, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.17935154801708156, "compression_ratio": 1.6556016597510372, "no_speech_prob":
  0.015115798451006413}, {"id": 861, "seek": 538784, "start": 5405.84, "end": 5412.96,
  "text": " I mean, so far, what I hear from you is that my tea has, uh, the qualities,
  let''s say, it can run", "tokens": [51264, 286, 914, 11, 370, 1400, 11, 437, 286,
  1568, 490, 291, 307, 300, 452, 5817, 575, 11, 2232, 11, 264, 16477, 11, 718, 311,
  584, 11, 309, 393, 1190, 51620], "temperature": 0.0, "avg_logprob": -0.17935154801708156,
  "compression_ratio": 1.6556016597510372, "no_speech_prob": 0.015115798451006413},
  {"id": 862, "seek": 541296, "start": 5412.96, "end": 5419.2, "text": " on pure CPU,
  which is a win on cost. It scales, which is also a win on cost in the long term.",
  "tokens": [50364, 322, 6075, 13199, 11, 597, 307, 257, 1942, 322, 2063, 13, 467,
  17408, 11, 597, 307, 611, 257, 1942, 322, 2063, 294, 264, 938, 1433, 13, 50676],
  "temperature": 0.0, "avg_logprob": -0.1636808552873244, "compression_ratio": 1.654867256637168,
  "no_speech_prob": 0.03533283621072769}, {"id": 863, "seek": 541296, "start": 5419.76,
  "end": 5429.52, "text": " Right. Um, and it also, uh, is insanely fast, which is
  a win on product. It''s a win on, go to", "tokens": [50704, 1779, 13, 3301, 11,
  293, 309, 611, 11, 2232, 11, 307, 40965, 2370, 11, 597, 307, 257, 1942, 322, 1674,
  13, 467, 311, 257, 1942, 322, 11, 352, 281, 51192], "temperature": 0.0, "avg_logprob":
  -0.1636808552873244, "compression_ratio": 1.654867256637168, "no_speech_prob": 0.03533283621072769},
  {"id": 864, "seek": 541296, "start": 5429.52, "end": 5435.52, "text": " market.
  Like I have this document, how quickly it travels through the pipeline and is searchable.",
  "tokens": [51192, 2142, 13, 1743, 286, 362, 341, 4166, 11, 577, 2661, 309, 19863,
  807, 264, 15517, 293, 307, 3164, 712, 13, 51492], "temperature": 0.0, "avg_logprob":
  -0.1636808552873244, "compression_ratio": 1.654867256637168, "no_speech_prob": 0.03533283621072769},
  {"id": 865, "seek": 541296, "start": 5436.56, "end": 5442.16, "text": " Right. So
  I mean, it''s important use case. In some cases, like paramount, you know, like",
  "tokens": [51544, 1779, 13, 407, 286, 914, 11, 309, 311, 1021, 764, 1389, 13, 682,
  512, 3331, 11, 411, 6220, 792, 11, 291, 458, 11, 411, 51824], "temperature": 0.0,
  "avg_logprob": -0.1636808552873244, "compression_ratio": 1.654867256637168, "no_speech_prob":
  0.03533283621072769}, {"id": 866, "seek": 544216, "start": 5442.16, "end": 5448.32,
  "text": " financial space, you know, a document came out. I wanted to be indexed
  right away. Like a second", "tokens": [50364, 4669, 1901, 11, 291, 458, 11, 257,
  4166, 1361, 484, 13, 286, 1415, 281, 312, 8186, 292, 558, 1314, 13, 1743, 257, 1150,
  50672], "temperature": 0.0, "avg_logprob": -0.15753915376752337, "compression_ratio":
  1.563265306122449, "no_speech_prob": 0.006090919487178326}, {"id": 867, "seek":
  544216, "start": 5448.32, "end": 5453.76, "text": " after, I don''t want to wait
  five minutes. It will be way too late for me to make a decision. So,", "tokens":
  [50672, 934, 11, 286, 500, 380, 528, 281, 1699, 1732, 2077, 13, 467, 486, 312, 636,
  886, 3469, 337, 385, 281, 652, 257, 3537, 13, 407, 11, 50944], "temperature": 0.0,
  "avg_logprob": -0.15753915376752337, "compression_ratio": 1.563265306122449, "no_speech_prob":
  0.006090919487178326}, {"id": 868, "seek": 544216, "start": 5454.639999999999, "end":
  5461.36, "text": " I mean, is there something else? Like you, and maybe if you,
  if you could compare now or point", "tokens": [50988, 286, 914, 11, 307, 456, 746,
  1646, 30, 1743, 291, 11, 293, 1310, 498, 291, 11, 498, 291, 727, 6794, 586, 420,
  935, 51324], "temperature": 0.0, "avg_logprob": -0.15753915376752337, "compression_ratio":
  1.563265306122449, "no_speech_prob": 0.006090919487178326}, {"id": 869, "seek":
  544216, "start": 5461.36, "end": 5467.04, "text": " us to the blog post, you know,
  uh, with other vendors like Amazon has in French, uh, you know,", "tokens": [51324,
  505, 281, 264, 6968, 2183, 11, 291, 458, 11, 2232, 11, 365, 661, 22056, 411, 6795,
  575, 294, 5522, 11, 2232, 11, 291, 458, 11, 51608], "temperature": 0.0, "avg_logprob":
  -0.15753915376752337, "compression_ratio": 1.563265306122449, "no_speech_prob":
  0.006090919487178326}, {"id": 870, "seek": 546704, "start": 5467.12, "end": 5475.04,
  "text": " hugging face has infinity, infinity, right? Um, and then, uh, and video,
  I think they also had", "tokens": [50368, 41706, 1851, 575, 13202, 11, 13202, 11,
  558, 30, 3301, 11, 293, 550, 11, 2232, 11, 293, 960, 11, 286, 519, 436, 611, 632,
  50764], "temperature": 0.0, "avg_logprob": -0.1803096889220562, "compression_ratio":
  1.626086956521739, "no_speech_prob": 0.007530526723712683}, {"id": 871, "seek":
  546704, "start": 5475.04, "end": 5480.8, "text": " some layer. I forgot its name,
  but like those are probably fairly expensive. They probably", "tokens": [50764,
  512, 4583, 13, 286, 5298, 1080, 1315, 11, 457, 411, 729, 366, 1391, 6457, 5124,
  13, 814, 1391, 51052], "temperature": 0.0, "avg_logprob": -0.1803096889220562, "compression_ratio":
  1.626086956521739, "no_speech_prob": 0.007530526723712683}, {"id": 872, "seek":
  546704, "start": 5480.8, "end": 5488.64, "text": " are not $90 per piece. So what,
  what, what is your thinking there? So like you, you, I think you", "tokens": [51052,
  366, 406, 1848, 7771, 680, 2522, 13, 407, 437, 11, 437, 11, 437, 307, 428, 1953,
  456, 30, 407, 411, 291, 11, 291, 11, 286, 519, 291, 51444], "temperature": 0.0,
  "avg_logprob": -0.1803096889220562, "compression_ratio": 1.626086956521739, "no_speech_prob":
  0.007530526723712683}, {"id": 873, "seek": 546704, "start": 5488.64, "end": 5494.48,
  "text": " also are vocal in this space or like in that direction that mighty is
  much more economical.", "tokens": [51444, 611, 366, 11657, 294, 341, 1901, 420,
  411, 294, 300, 3513, 300, 21556, 307, 709, 544, 42473, 13, 51736], "temperature":
  0.0, "avg_logprob": -0.1803096889220562, "compression_ratio": 1.626086956521739,
  "no_speech_prob": 0.007530526723712683}, {"id": 874, "seek": 549448, "start": 5494.48,
  "end": 5501.759999999999, "text": " Uh, than these more expensive solutions, but
  they probably offer something else as well, but like,", "tokens": [50364, 4019,
  11, 813, 613, 544, 5124, 6547, 11, 457, 436, 1391, 2626, 746, 1646, 382, 731, 11,
  457, 411, 11, 50728], "temperature": 0.0, "avg_logprob": -0.2381542696811185, "compression_ratio":
  1.6455696202531647, "no_speech_prob": 0.011571727693080902}, {"id": 875, "seek":
  549448, "start": 5501.759999999999, "end": 5510.24, "text": " you have an issue
  for sure. Yeah. Um, I think that, so the interesting thing, if you, if you get",
  "tokens": [50728, 291, 362, 364, 2734, 337, 988, 13, 865, 13, 3301, 11, 286, 519,
  300, 11, 370, 264, 1880, 551, 11, 498, 291, 11, 498, 291, 483, 51152], "temperature":
  0.0, "avg_logprob": -0.2381542696811185, "compression_ratio": 1.6455696202531647,
  "no_speech_prob": 0.011571727693080902}, {"id": 876, "seek": 549448, "start": 5510.24,
  "end": 5515.04, "text": " involved with like, if you, if you get into Amazon, like
  in French, yeah, and all this stuff,", "tokens": [51152, 3288, 365, 411, 11, 498,
  291, 11, 498, 291, 483, 666, 6795, 11, 411, 294, 5522, 11, 1338, 11, 293, 439, 341,
  1507, 11, 51392], "temperature": 0.0, "avg_logprob": -0.2381542696811185, "compression_ratio":
  1.6455696202531647, "no_speech_prob": 0.011571727693080902}, {"id": 877, "seek":
  549448, "start": 5515.679999999999, "end": 5521.04, "text": " they crafted like
  their entire, like they build their own hardware. Um, they have their neural core,",
  "tokens": [51424, 436, 36213, 411, 641, 2302, 11, 411, 436, 1322, 641, 1065, 8837,
  13, 3301, 11, 436, 362, 641, 18161, 4965, 11, 51692], "temperature": 0.0, "avg_logprob":
  -0.2381542696811185, "compression_ratio": 1.6455696202531647, "no_speech_prob":
  0.011571727693080902}, {"id": 878, "seek": 552104, "start": 5522.0, "end": 5529.6,
  "text": " um, that all the stuff is based around. And that''s like, it''s lockin.
  It''s big time lockin, right?", "tokens": [50412, 1105, 11, 300, 439, 264, 1507,
  307, 2361, 926, 13, 400, 300, 311, 411, 11, 309, 311, 4017, 259, 13, 467, 311, 955,
  565, 4017, 259, 11, 558, 30, 50792], "temperature": 0.0, "avg_logprob": -0.19079274868746415,
  "compression_ratio": 1.632034632034632, "no_speech_prob": 0.001660916837863624},
  {"id": 879, "seek": 552104, "start": 5529.6, "end": 5539.28, "text": " Um, uh, this
  is just a web API. You can just use it. I, I think that, um, I, I''ve considered",
  "tokens": [50792, 3301, 11, 2232, 11, 341, 307, 445, 257, 3670, 9362, 13, 509, 393,
  445, 764, 309, 13, 286, 11, 286, 519, 300, 11, 1105, 11, 286, 11, 286, 600, 4888,
  51276], "temperature": 0.0, "avg_logprob": -0.19079274868746415, "compression_ratio":
  1.632034632034632, "no_speech_prob": 0.001660916837863624}, {"id": 880, "seek":
  552104, "start": 5539.28, "end": 5544.8, "text": " also like hosting an API, like,
  uh, hugging face, hugging faces like one of the most amazing", "tokens": [51276,
  611, 411, 16058, 364, 9362, 11, 411, 11, 2232, 11, 41706, 1851, 11, 41706, 8475,
  411, 472, 295, 264, 881, 2243, 51552], "temperature": 0.0, "avg_logprob": -0.19079274868746415,
  "compression_ratio": 1.632034632034632, "no_speech_prob": 0.001660916837863624},
  {"id": 881, "seek": 552104, "start": 5544.8, "end": 5550.0, "text": " software companies
  ever. It''s like, that''s like the real community driven open source stuff.", "tokens":
  [51552, 4722, 3431, 1562, 13, 467, 311, 411, 11, 300, 311, 411, 264, 957, 1768,
  9555, 1269, 4009, 1507, 13, 51812], "temperature": 0.0, "avg_logprob": -0.19079274868746415,
  "compression_ratio": 1.632034632034632, "no_speech_prob": 0.001660916837863624},
  {"id": 882, "seek": 555000, "start": 5550.0, "end": 5554.48, "text": " They do such
  amazing work. So I don''t want to, I don''t want to say anything bad about hugging",
  "tokens": [50364, 814, 360, 1270, 2243, 589, 13, 407, 286, 500, 380, 528, 281, 11,
  286, 500, 380, 528, 281, 584, 1340, 1578, 466, 41706, 50588], "temperature": 0.0,
  "avg_logprob": -0.1598685642458358, "compression_ratio": 1.6973684210526316, "no_speech_prob":
  0.000646044674795121}, {"id": 883, "seek": 555000, "start": 5554.48, "end": 5560.0,
  "text": " face because I really have nothing bad to say at all. Um, but, you know,
  Infinity definitely has", "tokens": [50588, 1851, 570, 286, 534, 362, 1825, 1578,
  281, 584, 412, 439, 13, 3301, 11, 457, 11, 291, 458, 11, 34762, 2138, 575, 50864],
  "temperature": 0.0, "avg_logprob": -0.1598685642458358, "compression_ratio": 1.6973684210526316,
  "no_speech_prob": 0.000646044674795121}, {"id": 884, "seek": 555000, "start": 5560.0,
  "end": 5567.28, "text": " a fit for the market, which is like, you know, if you
  are like Walmart and you need a solution, okay.", "tokens": [50864, 257, 3318, 337,
  264, 2142, 11, 597, 307, 411, 11, 291, 458, 11, 498, 291, 366, 411, 25237, 293,
  291, 643, 257, 3827, 11, 1392, 13, 51228], "temperature": 0.0, "avg_logprob": -0.1598685642458358,
  "compression_ratio": 1.6973684210526316, "no_speech_prob": 0.000646044674795121},
  {"id": 885, "seek": 555000, "start": 5568.88, "end": 5574.8, "text": " Hacking face
  infinity is in your budget. Go pay for it, you know. Um, that''s the type of thing",
  "tokens": [51308, 389, 14134, 1851, 13202, 307, 294, 428, 4706, 13, 1037, 1689,
  337, 309, 11, 291, 458, 13, 3301, 11, 300, 311, 264, 2010, 295, 551, 51604], "temperature":
  0.0, "avg_logprob": -0.1598685642458358, "compression_ratio": 1.6973684210526316,
  "no_speech_prob": 0.000646044674795121}, {"id": 886, "seek": 557480, "start": 5574.88,
  "end": 5582.72, "text": " that Walmart should use. Um, but if, if you are just like,
  if you''re a five person developer team", "tokens": [50368, 300, 25237, 820, 764,
  13, 3301, 11, 457, 498, 11, 498, 291, 366, 445, 411, 11, 498, 291, 434, 257, 1732,
  954, 10754, 1469, 50760], "temperature": 0.0, "avg_logprob": -0.13758040428161622,
  "compression_ratio": 1.6222222222222222, "no_speech_prob": 0.0006148762768134475},
  {"id": 887, "seek": 557480, "start": 5582.72, "end": 5587.4400000000005, "text":
  " or like, even a, if you work at a company that''s like, you know, 300 people,",
  "tokens": [50760, 420, 411, 11, 754, 257, 11, 498, 291, 589, 412, 257, 2237, 300,
  311, 411, 11, 291, 458, 11, 6641, 561, 11, 50996], "temperature": 0.0, "avg_logprob":
  -0.13758040428161622, "compression_ratio": 1.6222222222222222, "no_speech_prob":
  0.0006148762768134475}, {"id": 888, "seek": 557480, "start": 5589.2, "end": 5596.24,
  "text": " infinity is like really, really expensive. Um, so there is a, there is
  a market segmentation there.", "tokens": [51084, 13202, 307, 411, 534, 11, 534,
  5124, 13, 3301, 11, 370, 456, 307, 257, 11, 456, 307, 257, 2142, 9469, 399, 456,
  13, 51436], "temperature": 0.0, "avg_logprob": -0.13758040428161622, "compression_ratio":
  1.6222222222222222, "no_speech_prob": 0.0006148762768134475}, {"id": 889, "seek":
  557480, "start": 5596.24, "end": 5600.72, "text": " There''s a difference between,
  okay, well, how much can you afford and who can you hire and", "tokens": [51436,
  821, 311, 257, 2649, 1296, 11, 1392, 11, 731, 11, 577, 709, 393, 291, 6157, 293,
  567, 393, 291, 11158, 293, 51660], "temperature": 0.0, "avg_logprob": -0.13758040428161622,
  "compression_ratio": 1.6222222222222222, "no_speech_prob": 0.0006148762768134475},
  {"id": 890, "seek": 560072, "start": 5600.88, "end": 5606.56, "text": " what''s
  the level of, um, internal support that you have to put around this thing and how
  does it all fit?", "tokens": [50372, 437, 311, 264, 1496, 295, 11, 1105, 11, 6920,
  1406, 300, 291, 362, 281, 829, 926, 341, 551, 293, 577, 775, 309, 439, 3318, 30,
  50656], "temperature": 0.0, "avg_logprob": -0.16906849173612373, "compression_ratio":
  1.7169117647058822, "no_speech_prob": 0.002512376755475998}, {"id": 891, "seek":
  560072, "start": 5608.320000000001, "end": 5613.12, "text": " The teams that are
  just starting off that need to use something that, that works really fast,", "tokens":
  [50744, 440, 5491, 300, 366, 445, 2891, 766, 300, 643, 281, 764, 746, 300, 11, 300,
  1985, 534, 2370, 11, 50984], "temperature": 0.0, "avg_logprob": -0.16906849173612373,
  "compression_ratio": 1.7169117647058822, "no_speech_prob": 0.002512376755475998},
  {"id": 892, "seek": 560072, "start": 5613.12, "end": 5618.320000000001, "text":
  " easy to use, then that''s, that''s where it might fit. So I don''t think mighty
  can,", "tokens": [50984, 1858, 281, 764, 11, 550, 300, 311, 11, 300, 311, 689, 309,
  1062, 3318, 13, 407, 286, 500, 380, 519, 21556, 393, 11, 51244], "temperature":
  0.0, "avg_logprob": -0.16906849173612373, "compression_ratio": 1.7169117647058822,
  "no_speech_prob": 0.002512376755475998}, {"id": 893, "seek": 560072, "start": 5618.320000000001,
  "end": 5623.92, "text": " competes with infinity because honestly, I, uh, you know,
  hey, Walmart, if you want me as a", "tokens": [51244, 2850, 279, 365, 13202, 570,
  6095, 11, 286, 11, 2232, 11, 291, 458, 11, 4177, 11, 25237, 11, 498, 291, 528, 385,
  382, 257, 51524], "temperature": 0.0, "avg_logprob": -0.16906849173612373, "compression_ratio":
  1.7169117647058822, "no_speech_prob": 0.002512376755475998}, {"id": 894, "seek":
  560072, "start": 5623.92, "end": 5628.400000000001, "text": " customer, if you want,
  if you want to buy mighty, sure, go ahead, you know, let''s talk or you", "tokens":
  [51524, 5474, 11, 498, 291, 528, 11, 498, 291, 528, 281, 2256, 21556, 11, 988, 11,
  352, 2286, 11, 291, 458, 11, 718, 311, 751, 420, 291, 51748], "temperature": 0.0,
  "avg_logprob": -0.16906849173612373, "compression_ratio": 1.7169117647058822, "no_speech_prob":
  0.002512376755475998}, {"id": 895, "seek": 562840, "start": 5628.4, "end": 5632.799999999999,
  "text": " can pay the 99 bucks a month. But, you know, that''s not, that''s not
  one target. I''m trying to", "tokens": [50364, 393, 1689, 264, 11803, 11829, 257,
  1618, 13, 583, 11, 291, 458, 11, 300, 311, 406, 11, 300, 311, 406, 472, 3779, 13,
  286, 478, 1382, 281, 50584], "temperature": 0.0, "avg_logprob": -0.17214930499041523,
  "compression_ratio": 1.5, "no_speech_prob": 0.0036120289005339146}, {"id": 896,
  "seek": 562840, "start": 5632.799999999999, "end": 5639.2, "text": " make it super
  easy for everybody else. Um, somebody high rank recently, uh, connected with me,",
  "tokens": [50584, 652, 309, 1687, 1858, 337, 2201, 1646, 13, 3301, 11, 2618, 1090,
  6181, 3938, 11, 2232, 11, 4582, 365, 385, 11, 50904], "temperature": 0.0, "avg_logprob":
  -0.17214930499041523, "compression_ratio": 1.5, "no_speech_prob": 0.0036120289005339146},
  {"id": 897, "seek": 562840, "start": 5639.2, "end": 5645.2, "text": " a LinkedIn,
  I think some kind of VP of engineering, hey, if you''re looking into embeddings,
  contact max.", "tokens": [50904, 257, 20657, 11, 286, 519, 512, 733, 295, 35812,
  295, 7043, 11, 4177, 11, 498, 291, 434, 1237, 666, 12240, 29432, 11, 3385, 11469,
  13, 51204], "temperature": 0.0, "avg_logprob": -0.17214930499041523, "compression_ratio":
  1.5, "no_speech_prob": 0.0036120289005339146}, {"id": 898, "seek": 562840, "start":
  5648.32, "end": 5656.0, "text": " Really? But like, so we understand, uh, infinity
  a little bit better because I didn''t try this at all.", "tokens": [51360, 4083,
  30, 583, 411, 11, 370, 321, 1223, 11, 2232, 11, 13202, 257, 707, 857, 1101, 570,
  286, 994, 380, 853, 341, 412, 439, 13, 51744], "temperature": 0.0, "avg_logprob":
  -0.17214930499041523, "compression_ratio": 1.5, "no_speech_prob": 0.0036120289005339146},
  {"id": 899, "seek": 565600, "start": 5656.96, "end": 5662.64, "text": " Um, is this
  like some kind of web service that you basically buy subscription for like,", "tokens":
  [50412, 3301, 11, 307, 341, 411, 512, 733, 295, 3670, 2643, 300, 291, 1936, 2256,
  17231, 337, 411, 11, 50696], "temperature": 0.0, "avg_logprob": -0.2154098885958312,
  "compression_ratio": 1.78544061302682, "no_speech_prob": 0.005826977081596851},
  {"id": 900, "seek": 565600, "start": 5662.64, "end": 5667.92, "text": " sauce kind
  of thing? No, it''s like a dark container. I think infinity is a dark container.
  Um,", "tokens": [50696, 4880, 733, 295, 551, 30, 883, 11, 309, 311, 411, 257, 2877,
  10129, 13, 286, 519, 13202, 307, 257, 2877, 10129, 13, 3301, 11, 50960], "temperature":
  0.0, "avg_logprob": -0.2154098885958312, "compression_ratio": 1.78544061302682,
  "no_speech_prob": 0.005826977081596851}, {"id": 901, "seek": 565600, "start": 5669.28,
  "end": 5674.08, "text": " I don''t know, it might be, it might even be written in
  Rust, I''m not sure. Consider tokenizers are", "tokens": [51028, 286, 500, 380,
  458, 11, 309, 1062, 312, 11, 309, 1062, 754, 312, 3720, 294, 34952, 11, 286, 478,
  406, 988, 13, 17416, 14862, 22525, 366, 51268], "temperature": 0.0, "avg_logprob":
  -0.2154098885958312, "compression_ratio": 1.78544061302682, "no_speech_prob": 0.005826977081596851},
  {"id": 902, "seek": 565600, "start": 5674.08, "end": 5678.48, "text": " written
  in Rust, they may have done, I may have done some, infinity came out before mighty,
  so they", "tokens": [51268, 3720, 294, 34952, 11, 436, 815, 362, 1096, 11, 286,
  815, 362, 1096, 512, 11, 13202, 1361, 484, 949, 21556, 11, 370, 436, 51488], "temperature":
  0.0, "avg_logprob": -0.2154098885958312, "compression_ratio": 1.78544061302682,
  "no_speech_prob": 0.005826977081596851}, {"id": 903, "seek": 565600, "start": 5678.48,
  "end": 5683.12, "text": " may have done something. So it''s a perfect competitor
  for, for mighty in that sense.", "tokens": [51488, 815, 362, 1096, 746, 13, 407,
  309, 311, 257, 2176, 27266, 337, 11, 337, 21556, 294, 300, 2020, 13, 51720], "temperature":
  0.0, "avg_logprob": -0.2154098885958312, "compression_ratio": 1.78544061302682,
  "no_speech_prob": 0.005826977081596851}, {"id": 904, "seek": 568312, "start": 5683.12,
  "end": 5689.2, "text": " Um, I mean, I mean, no time pricing, but I mean, the only
  package itself, right? So basically,", "tokens": [50364, 3301, 11, 286, 914, 11,
  286, 914, 11, 572, 565, 17621, 11, 457, 286, 914, 11, 264, 787, 7372, 2564, 11,
  558, 30, 407, 1936, 11, 50668], "temperature": 0.0, "avg_logprob": -0.26638587315877277,
  "compression_ratio": 1.6885964912280702, "no_speech_prob": 0.00759807089343667},
  {"id": 905, "seek": 568312, "start": 5689.2, "end": 5695.28, "text": " it''s like
  Docker Docker anyway. Yeah. And I think, I think, I think my, well, I think infinity",
  "tokens": [50668, 309, 311, 411, 33772, 33772, 4033, 13, 865, 13, 400, 286, 519,
  11, 286, 519, 11, 286, 519, 452, 11, 731, 11, 286, 519, 13202, 50972], "temperature":
  0.0, "avg_logprob": -0.26638587315877277, "compression_ratio": 1.6885964912280702,
  "no_speech_prob": 0.00759807089343667}, {"id": 906, "seek": 568312, "start": 5695.28,
  "end": 5702.88, "text": " encourages GPU like you, they want you to use GPU for
  it. But that''s like, I think infinity fits", "tokens": [50972, 28071, 18407, 411,
  291, 11, 436, 528, 291, 281, 764, 18407, 337, 309, 13, 583, 300, 311, 411, 11, 286,
  519, 13202, 9001, 51352], "temperature": 0.0, "avg_logprob": -0.26638587315877277,
  "compression_ratio": 1.6885964912280702, "no_speech_prob": 0.00759807089343667},
  {"id": 907, "seek": 568312, "start": 5702.88, "end": 5708.4, "text": " well. If
  you have like, you know, a million requests an hour, something like that scale,
  you know?", "tokens": [51352, 731, 13, 759, 291, 362, 411, 11, 291, 458, 11, 257,
  2459, 12475, 364, 1773, 11, 746, 411, 300, 4373, 11, 291, 458, 30, 51628], "temperature":
  0.0, "avg_logprob": -0.26638587315877277, "compression_ratio": 1.6885964912280702,
  "no_speech_prob": 0.00759807089343667}, {"id": 908, "seek": 570840, "start": 5708.4,
  "end": 5716.4, "text": " Yeah. Um, if you have like 20,000 requests a day or a thousand
  requests a day, you know,", "tokens": [50364, 865, 13, 3301, 11, 498, 291, 362,
  411, 945, 11, 1360, 12475, 257, 786, 420, 257, 4714, 12475, 257, 786, 11, 291, 458,
  11, 50764], "temperature": 0.0, "avg_logprob": -0.1739403020555728, "compression_ratio":
  1.7674418604651163, "no_speech_prob": 0.008607376366853714}, {"id": 909, "seek":
  570840, "start": 5716.4, "end": 5722.639999999999, "text": " that, that range, a
  hundred thousand, you know, I think by these perfect for that, you know,", "tokens":
  [50764, 300, 11, 300, 3613, 11, 257, 3262, 4714, 11, 291, 458, 11, 286, 519, 538,
  613, 2176, 337, 300, 11, 291, 458, 11, 51076], "temperature": 0.0, "avg_logprob":
  -0.1739403020555728, "compression_ratio": 1.7674418604651163, "no_speech_prob":
  0.008607376366853714}, {"id": 910, "seek": 570840, "start": 5722.639999999999, "end":
  5728.16, "text": " it''s not, you don''t have to have like this huge scale. It can
  get bigger. You can just, you know,", "tokens": [51076, 309, 311, 406, 11, 291,
  500, 380, 362, 281, 362, 411, 341, 2603, 4373, 13, 467, 393, 483, 3801, 13, 509,
  393, 445, 11, 291, 458, 11, 51352], "temperature": 0.0, "avg_logprob": -0.1739403020555728,
  "compression_ratio": 1.7674418604651163, "no_speech_prob": 0.008607376366853714},
  {"id": 911, "seek": 570840, "start": 5728.16, "end": 5733.12, "text": " spend more
  money on hardware than scale it up as much as you want. You can support, you can
  support,", "tokens": [51352, 3496, 544, 1460, 322, 8837, 813, 4373, 309, 493, 382,
  709, 382, 291, 528, 13, 509, 393, 1406, 11, 291, 393, 1406, 11, 51600], "temperature":
  0.0, "avg_logprob": -0.1739403020555728, "compression_ratio": 1.7674418604651163,
  "no_speech_prob": 0.008607376366853714}, {"id": 912, "seek": 573312, "start": 5733.599999999999,
  "end": 5738.24, "text": " you know, a million requests a day if you want to, you''re
  a 10 million. You just have to put more", "tokens": [50388, 291, 458, 11, 257, 2459,
  12475, 257, 786, 498, 291, 528, 281, 11, 291, 434, 257, 1266, 2459, 13, 509, 445,
  362, 281, 829, 544, 50620], "temperature": 0.0, "avg_logprob": -0.11717043099579988,
  "compression_ratio": 1.6556016597510372, "no_speech_prob": 0.0022550441790372133},
  {"id": 913, "seek": 573312, "start": 5738.24, "end": 5744.24, "text": " hardware
  behind it. So I think I''m just competing in a different market. I don''t think,
  I don''t think", "tokens": [50620, 8837, 2261, 309, 13, 407, 286, 519, 286, 478,
  445, 15439, 294, 257, 819, 2142, 13, 286, 500, 380, 519, 11, 286, 500, 380, 519,
  50920], "temperature": 0.0, "avg_logprob": -0.11717043099579988, "compression_ratio":
  1.6556016597510372, "no_speech_prob": 0.0022550441790372133}, {"id": 914, "seek":
  573312, "start": 5744.24, "end": 5752.08, "text": " infinity and I are targeting
  the same, the same businesses. Yeah. Yeah. And I mean, you do have the", "tokens":
  [50920, 13202, 293, 286, 366, 17918, 264, 912, 11, 264, 912, 6011, 13, 865, 13,
  865, 13, 400, 286, 914, 11, 291, 360, 362, 264, 51312], "temperature": 0.0, "avg_logprob":
  -0.11717043099579988, "compression_ratio": 1.6556016597510372, "no_speech_prob":
  0.0022550441790372133}, {"id": 915, "seek": 573312, "start": 5752.08, "end": 5760.16,
  "text": " edge on the fact that you want to address the community beyond Python.
  So like, I think it''s a big,", "tokens": [51312, 4691, 322, 264, 1186, 300, 291,
  528, 281, 2985, 264, 1768, 4399, 15329, 13, 407, 411, 11, 286, 519, 309, 311, 257,
  955, 11, 51716], "temperature": 0.0, "avg_logprob": -0.11717043099579988, "compression_ratio":
  1.6556016597510372, "no_speech_prob": 0.0022550441790372133}, {"id": 916, "seek":
  576016, "start": 5760.96, "end": 5769.92, "text": " it''s a big message to send.
  Um, and in some ways through you, you channeled this, this feeling that,", "tokens":
  [50404, 309, 311, 257, 955, 3636, 281, 2845, 13, 3301, 11, 293, 294, 512, 2098,
  807, 291, 11, 291, 2269, 292, 341, 11, 341, 2633, 300, 11, 50852], "temperature":
  0.0, "avg_logprob": -0.23092596871512278, "compression_ratio": 1.6596638655462186,
  "no_speech_prob": 0.013590123504400253}, {"id": 917, "seek": 576016, "start": 5769.92,
  "end": 5776.24, "text": " hey, this guy is in Node.js, a job, I probably feel like
  left out from this big thing, but it''s", "tokens": [50852, 4177, 11, 341, 2146,
  307, 294, 38640, 13, 25530, 11, 257, 1691, 11, 286, 1391, 841, 411, 1411, 484, 490,
  341, 955, 551, 11, 457, 309, 311, 51168], "temperature": 0.0, "avg_logprob": -0.23092596871512278,
  "compression_ratio": 1.6596638655462186, "no_speech_prob": 0.013590123504400253},
  {"id": 918, "seek": 576016, "start": 5776.24, "end": 5781.84, "text": " probably
  not true. I mean, I know also there is this deep learning for J and blah, blah,
  blah, but like,", "tokens": [51168, 1391, 406, 2074, 13, 286, 914, 11, 286, 458,
  611, 456, 307, 341, 2452, 2539, 337, 508, 293, 12288, 11, 12288, 11, 12288, 11,
  457, 411, 11, 51448], "temperature": 0.0, "avg_logprob": -0.23092596871512278, "compression_ratio":
  1.6596638655462186, "no_speech_prob": 0.013590123504400253}, {"id": 919, "seek":
  576016, "start": 5781.84, "end": 5787.28, "text": " it''s like an island in the
  ocean, probably comparing it to it. It''s amazing software. It just", "tokens":
  [51448, 309, 311, 411, 364, 6077, 294, 264, 7810, 11, 1391, 15763, 309, 281, 309,
  13, 467, 311, 2243, 4722, 13, 467, 445, 51720], "temperature": 0.0, "avg_logprob":
  -0.23092596871512278, "compression_ratio": 1.6596638655462186, "no_speech_prob":
  0.013590123504400253}, {"id": 920, "seek": 578728, "start": 5787.28, "end": 5794.0,
  "text": " didn''t get the adoption that Python got. Yeah. I remember going through
  these internal pains myself,", "tokens": [50364, 994, 380, 483, 264, 19215, 300,
  15329, 658, 13, 865, 13, 286, 1604, 516, 807, 613, 6920, 29774, 2059, 11, 50700],
  "temperature": 0.0, "avg_logprob": -0.25029105369490806, "compression_ratio": 1.6296296296296295,
  "no_speech_prob": 0.003511376678943634}, {"id": 921, "seek": 578728, "start": 5794.0,
  "end": 5803.04, "text": " right? When I was, when it was like 2015, 2016, and I
  started, and I started getting deep learning", "tokens": [50700, 558, 30, 1133,
  286, 390, 11, 562, 309, 390, 411, 7546, 11, 6549, 11, 293, 286, 1409, 11, 293, 286,
  1409, 1242, 2452, 2539, 51152], "temperature": 0.0, "avg_logprob": -0.25029105369490806,
  "compression_ratio": 1.6296296296296295, "no_speech_prob": 0.003511376678943634},
  {"id": 922, "seek": 578728, "start": 5803.04, "end": 5809.44, "text": " training
  and I took course error courses and rings courses on machine learning and stuff.
  I started", "tokens": [51152, 3097, 293, 286, 1890, 1164, 6713, 7712, 293, 11136,
  7712, 322, 3479, 2539, 293, 1507, 13, 286, 1409, 51472], "temperature": 0.0, "avg_logprob":
  -0.25029105369490806, "compression_ratio": 1.6296296296296295, "no_speech_prob":
  0.003511376678943634}, {"id": 923, "seek": 578728, "start": 5809.44, "end": 5815.599999999999,
  "text": " it off with Octav, which is an open source, uh, is a mathematical or whatever.
  It''s a new Octav,", "tokens": [51472, 309, 766, 365, 6788, 706, 11, 597, 307, 364,
  1269, 4009, 11, 2232, 11, 307, 257, 18894, 420, 2035, 13, 467, 311, 257, 777, 6788,
  706, 11, 51780], "temperature": 0.0, "avg_logprob": -0.25029105369490806, "compression_ratio":
  1.6296296296296295, "no_speech_prob": 0.003511376678943634}, {"id": 924, "seek":
  581560, "start": 5815.6, "end": 5820.4800000000005, "text": " but it''s like, it''s
  its own language, right? So it''s mathematics, um, just just code. But then,", "tokens":
  [50364, 457, 309, 311, 411, 11, 309, 311, 1080, 1065, 2856, 11, 558, 30, 407, 309,
  311, 18666, 11, 1105, 11, 445, 445, 3089, 13, 583, 550, 11, 50608], "temperature":
  0.0, "avg_logprob": -0.1813757832845052, "compression_ratio": 1.8154981549815499,
  "no_speech_prob": 0.0008447906002402306}, {"id": 925, "seek": 581560, "start": 5820.4800000000005,
  "end": 5824.4800000000005, "text": " like the next courses were all Python. And
  I was like, Oh, no, I have to learn Python. I don''t know", "tokens": [50608, 411,
  264, 958, 7712, 645, 439, 15329, 13, 400, 286, 390, 411, 11, 876, 11, 572, 11, 286,
  362, 281, 1466, 15329, 13, 286, 500, 380, 458, 50808], "temperature": 0.0, "avg_logprob":
  -0.1813757832845052, "compression_ratio": 1.8154981549815499, "no_speech_prob":
  0.0008447906002402306}, {"id": 926, "seek": 581560, "start": 5824.4800000000005,
  "end": 5830.08, "text": " Python. I have to know, no, no, no, no, no, no language
  to use this stuff. Okay, fine. I''ll do it.", "tokens": [50808, 15329, 13, 286,
  362, 281, 458, 11, 572, 11, 572, 11, 572, 11, 572, 11, 572, 11, 572, 2856, 281,
  764, 341, 1507, 13, 1033, 11, 2489, 13, 286, 603, 360, 309, 13, 51088], "temperature":
  0.0, "avg_logprob": -0.1813757832845052, "compression_ratio": 1.8154981549815499,
  "no_speech_prob": 0.0008447906002402306}, {"id": 927, "seek": 581560, "start": 5830.08,
  "end": 5834.72, "text": " Right? So I went down that and I learned Python and I
  got pretty good at it. Um, but there''s a lot", "tokens": [51088, 1779, 30, 407,
  286, 1437, 760, 300, 293, 286, 3264, 15329, 293, 286, 658, 1238, 665, 412, 309,
  13, 3301, 11, 457, 456, 311, 257, 688, 51320], "temperature": 0.0, "avg_logprob":
  -0.1813757832845052, "compression_ratio": 1.8154981549815499, "no_speech_prob":
  0.0008447906002402306}, {"id": 928, "seek": 581560, "start": 5834.72, "end": 5838.56,
  "text": " of people who just don''t want to take that step, you know, they want
  to, they want to ship code in", "tokens": [51320, 295, 561, 567, 445, 500, 380,
  528, 281, 747, 300, 1823, 11, 291, 458, 11, 436, 528, 281, 11, 436, 528, 281, 5374,
  3089, 294, 51512], "temperature": 0.0, "avg_logprob": -0.1813757832845052, "compression_ratio":
  1.8154981549815499, "no_speech_prob": 0.0008447906002402306}, {"id": 929, "seek":
  583856, "start": 5838.56, "end": 5845.84, "text": " their, in their stack. So it''s,
  it''s a big ask to say, if you want to use these awesome tools,", "tokens": [50364,
  641, 11, 294, 641, 8630, 13, 407, 309, 311, 11, 309, 311, 257, 955, 1029, 281, 584,
  11, 498, 291, 528, 281, 764, 613, 3476, 3873, 11, 50728], "temperature": 0.0, "avg_logprob":
  -0.15885656782724325, "compression_ratio": 1.6869158878504673, "no_speech_prob":
  0.0017256569117307663}, {"id": 930, "seek": 583856, "start": 5845.84, "end": 5849.120000000001,
  "text": " you got to use, you got to, you got to convert, you got to convert your
  language.", "tokens": [50728, 291, 658, 281, 764, 11, 291, 658, 281, 11, 291, 658,
  281, 7620, 11, 291, 658, 281, 7620, 428, 2856, 13, 50892], "temperature": 0.0, "avg_logprob":
  -0.15885656782724325, "compression_ratio": 1.6869158878504673, "no_speech_prob":
  0.0017256569117307663}, {"id": 931, "seek": 583856, "start": 5850.56, "end": 5858.96,
  "text": " Yeah, yeah, exactly. And if you''re, you know, if you''re not into data
  science or machine learning,", "tokens": [50964, 865, 11, 1338, 11, 2293, 13, 400,
  498, 291, 434, 11, 291, 458, 11, 498, 291, 434, 406, 666, 1412, 3497, 420, 3479,
  2539, 11, 51384], "temperature": 0.0, "avg_logprob": -0.15885656782724325, "compression_ratio":
  1.6869158878504673, "no_speech_prob": 0.0017256569117307663}, {"id": 932, "seek":
  583856, "start": 5859.6, "end": 5866.8, "text": " then why would you enter Python
  at all? Like it has no, no like single winning point,", "tokens": [51416, 550, 983,
  576, 291, 3242, 15329, 412, 439, 30, 1743, 309, 575, 572, 11, 572, 411, 2167, 8224,
  935, 11, 51776], "temperature": 0.0, "avg_logprob": -0.15885656782724325, "compression_ratio":
  1.6869158878504673, "no_speech_prob": 0.0017256569117307663}, {"id": 933, "seek":
  586680, "start": 5867.76, "end": 5875.360000000001, "text": " well, maybe simplicity,
  but hey, is that it? You know, um, and it''s like lose deposition. Of course,",
  "tokens": [50412, 731, 11, 1310, 25632, 11, 457, 4177, 11, 307, 300, 309, 30, 509,
  458, 11, 1105, 11, 293, 309, 311, 411, 3624, 1367, 5830, 13, 2720, 1164, 11, 50792],
  "temperature": 0.0, "avg_logprob": -0.16830779021640993, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.008484384045004845}, {"id": 934, "seek": 586680, "start": 5875.360000000001,
  "end": 5880.0, "text": " you can make it more strict with typing and blah, blah,
  blah, but like still, but like it took me,", "tokens": [50792, 291, 393, 652, 309,
  544, 10910, 365, 18444, 293, 12288, 11, 12288, 11, 12288, 11, 457, 411, 920, 11,
  457, 411, 309, 1890, 385, 11, 51024], "temperature": 0.0, "avg_logprob": -0.16830779021640993,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.008484384045004845},
  {"id": 935, "seek": 586680, "start": 5880.0, "end": 5884.64, "text": " I think it
  took me actually good three years to learn Python properly. Because it''s like,",
  "tokens": [51024, 286, 519, 309, 1890, 385, 767, 665, 1045, 924, 281, 1466, 15329,
  6108, 13, 1436, 309, 311, 411, 11, 51256], "temperature": 0.0, "avg_logprob": -0.16830779021640993,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.008484384045004845},
  {"id": 936, "seek": 586680, "start": 5884.64, "end": 5889.52, "text": " not like,
  okay, oh, I understand how to do the for loop. I understand the indentation and
  blah,", "tokens": [51256, 406, 411, 11, 1392, 11, 1954, 11, 286, 1223, 577, 281,
  360, 264, 337, 6367, 13, 286, 1223, 264, 44494, 399, 293, 12288, 11, 51500], "temperature":
  0.0, "avg_logprob": -0.16830779021640993, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.008484384045004845}, {"id": 937, "seek": 588952, "start": 5889.6,
  "end": 5897.84, "text": " but like to actually master it, right? Like, you know,
  avoid stupid loading of the model multiple times", "tokens": [50368, 457, 411, 281,
  767, 4505, 309, 11, 558, 30, 1743, 11, 291, 458, 11, 5042, 6631, 15114, 295, 264,
  2316, 3866, 1413, 50780], "temperature": 0.0, "avg_logprob": -0.3020557495484869,
  "compression_ratio": 1.4527363184079602, "no_speech_prob": 0.005055190995335579},
  {"id": 938, "seek": 588952, "start": 5897.84, "end": 5907.92, "text": " in G unicorn.
  So, so I think the, all like, sithon, I didn''t enter thyson, the sithon world,",
  "tokens": [50780, 294, 460, 28122, 13, 407, 11, 370, 286, 519, 264, 11, 439, 411,
  11, 262, 355, 266, 11, 286, 994, 380, 3242, 258, 749, 266, 11, 264, 262, 355, 266,
  1002, 11, 51284], "temperature": 0.0, "avg_logprob": -0.3020557495484869, "compression_ratio":
  1.4527363184079602, "no_speech_prob": 0.005055190995335579}, {"id": 939, "seek":
  588952, "start": 5907.92, "end": 5914.240000000001, "text": " likely, but, but even
  just writing normal soft when Python takes a lot of time, productizing it", "tokens":
  [51284, 3700, 11, 457, 11, 457, 754, 445, 3579, 2710, 2787, 562, 15329, 2516, 257,
  688, 295, 565, 11, 1674, 3319, 309, 51600], "temperature": 0.0, "avg_logprob": -0.3020557495484869,
  "compression_ratio": 1.4527363184079602, "no_speech_prob": 0.005055190995335579},
  {"id": 940, "seek": 591424, "start": 5914.24, "end": 5921.04, "text": " takes a
  lot of time. So, so why would you enter it if you are not after the tasty machine
  learning", "tokens": [50364, 2516, 257, 688, 295, 565, 13, 407, 11, 370, 983, 576,
  291, 3242, 309, 498, 291, 366, 406, 934, 264, 11535, 3479, 2539, 50704], "temperature":
  0.0, "avg_logprob": -0.08920461405878481, "compression_ratio": 1.676056338028169,
  "no_speech_prob": 0.003312513465061784}, {"id": 941, "seek": 591424, "start": 5921.04,
  "end": 5926.5599999999995, "text": " and data science? So why would you consider
  even converting your software stack into this?", "tokens": [50704, 293, 1412, 3497,
  30, 407, 983, 576, 291, 1949, 754, 29942, 428, 4722, 8630, 666, 341, 30, 50980],
  "temperature": 0.0, "avg_logprob": -0.08920461405878481, "compression_ratio": 1.676056338028169,
  "no_speech_prob": 0.003312513465061784}, {"id": 942, "seek": 591424, "start": 5927.5199999999995,
  "end": 5931.44, "text": " So it should be the other way around. And I think you''re
  doing a great job there with Mighty,", "tokens": [51028, 407, 309, 820, 312, 264,
  661, 636, 926, 13, 400, 286, 519, 291, 434, 884, 257, 869, 1691, 456, 365, 45874,
  11, 51224], "temperature": 0.0, "avg_logprob": -0.08920461405878481, "compression_ratio":
  1.676056338028169, "no_speech_prob": 0.003312513465061784}, {"id": 943, "seek":
  591424, "start": 5932.16, "end": 5937.28, "text": " basically offered as a service
  offered as maybe in the future as some kind of library or some kind", "tokens":
  [51260, 1936, 8059, 382, 257, 2643, 8059, 382, 1310, 294, 264, 2027, 382, 512, 733,
  295, 6405, 420, 512, 733, 51516], "temperature": 0.0, "avg_logprob": -0.08920461405878481,
  "compression_ratio": 1.676056338028169, "no_speech_prob": 0.003312513465061784},
  {"id": 944, "seek": 591424, "start": 5937.28, "end": 5941.5199999999995, "text":
  " of environment. I mean, Microsoft has been doing a bunch of these things. I don''t
  know if you", "tokens": [51516, 295, 2823, 13, 286, 914, 11, 8116, 575, 668, 884,
  257, 3840, 295, 613, 721, 13, 286, 500, 380, 458, 498, 291, 51728], "temperature":
  0.0, "avg_logprob": -0.08920461405878481, "compression_ratio": 1.676056338028169,
  "no_speech_prob": 0.003312513465061784}, {"id": 945, "seek": 594152, "start": 5941.52,
  "end": 5948.8, "text": " remember the CLR common language runtime. So like, you,
  you, you bring up the, the visual studio and", "tokens": [50364, 1604, 264, 12855,
  49, 2689, 2856, 34474, 13, 407, 411, 11, 291, 11, 291, 11, 291, 1565, 493, 264,
  11, 264, 5056, 6811, 293, 50728], "temperature": 0.0, "avg_logprob": -0.12301448539451316,
  "compression_ratio": 1.5846774193548387, "no_speech_prob": 0.0010254178196191788},
  {"id": 946, "seek": 594152, "start": 5948.8, "end": 5954.8, "text": " you can say,
  okay, my project will be in Pearl compiled and run for Java. I don''t remember.
  It", "tokens": [50728, 291, 393, 584, 11, 1392, 11, 452, 1716, 486, 312, 294, 24639,
  36548, 293, 1190, 337, 10745, 13, 286, 500, 380, 1604, 13, 467, 51028], "temperature":
  0.0, "avg_logprob": -0.12301448539451316, "compression_ratio": 1.5846774193548387,
  "no_speech_prob": 0.0010254178196191788}, {"id": 947, "seek": 594152, "start": 5954.8,
  "end": 5959.6, "text": " was crazy. I was just experimenting with it. And I was
  like, I barely knew any of these languages", "tokens": [51028, 390, 3219, 13, 286,
  390, 445, 29070, 365, 309, 13, 400, 286, 390, 411, 11, 286, 10268, 2586, 604, 295,
  613, 8650, 51268], "temperature": 0.0, "avg_logprob": -0.12301448539451316, "compression_ratio":
  1.5846774193548387, "no_speech_prob": 0.0010254178196191788}, {"id": 948, "seek":
  594152, "start": 5959.6, "end": 5967.52, "text": " as a student, but I was fascinated
  by the idea. It didn''t fly, I think, but it was, it was amazing.", "tokens": [51268,
  382, 257, 3107, 11, 457, 286, 390, 24597, 538, 264, 1558, 13, 467, 994, 380, 3603,
  11, 286, 519, 11, 457, 309, 390, 11, 309, 390, 2243, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.12301448539451316, "compression_ratio": 1.5846774193548387,
  "no_speech_prob": 0.0010254178196191788}, {"id": 949, "seek": 596752, "start": 5968.4800000000005,
  "end": 5978.400000000001, "text": " Yeah, absolutely. And I, you know, I would,
  I did, I did play around with the idea of, well,", "tokens": [50412, 865, 11, 3122,
  13, 400, 286, 11, 291, 458, 11, 286, 576, 11, 286, 630, 11, 286, 630, 862, 926,
  365, 264, 1558, 295, 11, 731, 11, 50908], "temperature": 0.0, "avg_logprob": -0.17765399142428562,
  "compression_ratio": 1.672340425531915, "no_speech_prob": 0.011254729703068733},
  {"id": 950, "seek": 596752, "start": 5978.400000000001, "end": 5982.56, "text":
  " what if you don''t even have to download Mighty, what if I was playing around
  with this idea from the", "tokens": [50908, 437, 498, 291, 500, 380, 754, 362, 281,
  5484, 45874, 11, 437, 498, 286, 390, 2433, 926, 365, 341, 1558, 490, 264, 51116],
  "temperature": 0.0, "avg_logprob": -0.17765399142428562, "compression_ratio": 1.672340425531915,
  "no_speech_prob": 0.011254729703068733}, {"id": 951, "seek": 596752, "start": 5982.56,
  "end": 5988.160000000001, "text": " NPM perspective, like, what if you just installed
  it from NPM command? And I thought, that''s a little", "tokens": [51116, 426, 18819,
  4585, 11, 411, 11, 437, 498, 291, 445, 8899, 309, 490, 426, 18819, 5622, 30, 400,
  286, 1194, 11, 300, 311, 257, 707, 51396], "temperature": 0.0, "avg_logprob": -0.17765399142428562,
  "compression_ratio": 1.672340425531915, "no_speech_prob": 0.011254729703068733},
  {"id": 952, "seek": 596752, "start": 5988.160000000001, "end": 5995.6, "text": "
  bit heavyweight. Do I want to bring in this thing from, you know, I could. I don''t
  know if that''s", "tokens": [51396, 857, 4676, 12329, 13, 1144, 286, 528, 281, 1565,
  294, 341, 551, 490, 11, 291, 458, 11, 286, 727, 13, 286, 500, 380, 458, 498, 300,
  311, 51768], "temperature": 0.0, "avg_logprob": -0.17765399142428562, "compression_ratio":
  1.672340425531915, "no_speech_prob": 0.011254729703068733}, {"id": 953, "seek":
  599560, "start": 5996.400000000001, "end": 6001.360000000001, "text": " if I should
  do that. And I also don''t want to set false expectations to. And maybe this is
  just", "tokens": [50404, 498, 286, 820, 360, 300, 13, 400, 286, 611, 500, 380, 528,
  281, 992, 7908, 9843, 281, 13, 400, 1310, 341, 307, 445, 50652], "temperature":
  0.0, "avg_logprob": -0.1276414017928274, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.002071540569886565}, {"id": 954, "seek": 599560, "start": 6001.360000000001,
  "end": 6006.56, "text": " because I''m not great at marketing, but I don''t want
  to set the expectation of you just do NPM", "tokens": [50652, 570, 286, 478, 406,
  869, 412, 6370, 11, 457, 286, 500, 380, 528, 281, 992, 264, 14334, 295, 291, 445,
  360, 426, 18819, 50912], "temperature": 0.0, "avg_logprob": -0.1276414017928274,
  "compression_ratio": 1.9078947368421053, "no_speech_prob": 0.002071540569886565},
  {"id": 955, "seek": 599560, "start": 6006.56, "end": 6010.96, "text": " install,
  look, Mighty server. And then you have a perfectly running thing because it''s,
  it''s more", "tokens": [50912, 3625, 11, 574, 11, 45874, 7154, 13, 400, 550, 291,
  362, 257, 6239, 2614, 551, 570, 309, 311, 11, 309, 311, 544, 51132], "temperature":
  0.0, "avg_logprob": -0.1276414017928274, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.002071540569886565}, {"id": 956, "seek": 599560, "start": 6010.96,
  "end": 6015.52, "text": " than that. You have to scale it properly. You have to
  give it its own compute. You have to choose", "tokens": [51132, 813, 300, 13, 509,
  362, 281, 4373, 309, 6108, 13, 509, 362, 281, 976, 309, 1080, 1065, 14722, 13, 509,
  362, 281, 2826, 51360], "temperature": 0.0, "avg_logprob": -0.1276414017928274,
  "compression_ratio": 1.9078947368421053, "no_speech_prob": 0.002071540569886565},
  {"id": 957, "seek": 599560, "start": 6015.52, "end": 6019.280000000001, "text":
  " the appropriate model. You have to, you have to do certain things to really get
  the most out of it.", "tokens": [51360, 264, 6854, 2316, 13, 509, 362, 281, 11,
  291, 362, 281, 360, 1629, 721, 281, 534, 483, 264, 881, 484, 295, 309, 13, 51548],
  "temperature": 0.0, "avg_logprob": -0.1276414017928274, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.002071540569886565}, {"id": 958, "seek": 599560, "start": 6020.160000000001,
  "end": 6025.52, "text": " So I don''t want to set false expectations where somebody
  deploys it and, and it''s like, it''s,", "tokens": [51592, 407, 286, 500, 380, 528,
  281, 992, 7908, 9843, 689, 2618, 368, 49522, 309, 293, 11, 293, 309, 311, 411, 11,
  309, 311, 11, 51860], "temperature": 0.0, "avg_logprob": -0.1276414017928274, "compression_ratio":
  1.9078947368421053, "no_speech_prob": 0.002071540569886565}, {"id": 959, "seek":
  602552, "start": 6025.52, "end": 6031.040000000001, "text": " doesn''t work well
  at all because they just did NPM install Mighty server, which doesn''t exist by",
  "tokens": [50364, 1177, 380, 589, 731, 412, 439, 570, 436, 445, 630, 426, 18819,
  3625, 45874, 7154, 11, 597, 1177, 380, 2514, 538, 50640], "temperature": 0.0, "avg_logprob":
  -0.14515689038854884, "compression_ratio": 1.6912280701754385, "no_speech_prob":
  0.0005770266288891435}, {"id": 960, "seek": 602552, "start": 6031.040000000001,
  "end": 6037.6, "text": " the way. Don''t try that. And then it didn''t, and then
  it didn''t work. So I, you know, there is a", "tokens": [50640, 264, 636, 13, 1468,
  380, 853, 300, 13, 400, 550, 309, 994, 380, 11, 293, 550, 309, 994, 380, 589, 13,
  407, 286, 11, 291, 458, 11, 456, 307, 257, 50968], "temperature": 0.0, "avg_logprob":
  -0.14515689038854884, "compression_ratio": 1.6912280701754385, "no_speech_prob":
  0.0005770266288891435}, {"id": 961, "seek": 602552, "start": 6037.6, "end": 6042.080000000001,
  "text": " little bit of knowledge that you do that that you do have to attain. So
  I want to pass, you know,", "tokens": [50968, 707, 857, 295, 3601, 300, 291, 360,
  300, 300, 291, 360, 362, 281, 23766, 13, 407, 286, 528, 281, 1320, 11, 291, 458,
  11, 51192], "temperature": 0.0, "avg_logprob": -0.14515689038854884, "compression_ratio":
  1.6912280701754385, "no_speech_prob": 0.0005770266288891435}, {"id": 962, "seek":
  602552, "start": 6043.4400000000005, "end": 6047.4400000000005, "text": " you do
  have to familiarize yourself with some concepts. That doesn''t mean learning an
  entirely", "tokens": [51260, 291, 360, 362, 281, 4963, 1125, 1803, 365, 512, 10392,
  13, 663, 1177, 380, 914, 2539, 364, 7696, 51460], "temperature": 0.0, "avg_logprob":
  -0.14515689038854884, "compression_ratio": 1.6912280701754385, "no_speech_prob":
  0.0005770266288891435}, {"id": 963, "seek": 602552, "start": 6047.4400000000005,
  "end": 6053.120000000001, "text": " new language and stack. Yeah, it''s more like
  probably like I''m a lobster devil. So somebody can", "tokens": [51460, 777, 2856,
  293, 8630, 13, 865, 11, 309, 311, 544, 411, 1391, 411, 286, 478, 257, 33198, 13297,
  13, 407, 2618, 393, 51744], "temperature": 0.0, "avg_logprob": -0.14515689038854884,
  "compression_ratio": 1.6912280701754385, "no_speech_prob": 0.0005770266288891435},
  {"id": 964, "seek": 605312, "start": 6053.12, "end": 6059.44, "text": " pick it
  up. And I mean, learning that way is much faster than actually, you know, figuring
  out how", "tokens": [50364, 1888, 309, 493, 13, 400, 286, 914, 11, 2539, 300, 636,
  307, 709, 4663, 813, 767, 11, 291, 458, 11, 15213, 484, 577, 50680], "temperature":
  0.0, "avg_logprob": -0.138465409327035, "compression_ratio": 1.5532786885245902,
  "no_speech_prob": 0.005983843468129635}, {"id": 965, "seek": 605312, "start": 6059.44,
  "end": 6064.32, "text": " the how will I plug it into my Java code or C++ code or
  whatever. So yeah, of course.", "tokens": [50680, 264, 577, 486, 286, 5452, 309,
  666, 452, 10745, 3089, 420, 383, 25472, 3089, 420, 2035, 13, 407, 1338, 11, 295,
  1164, 13, 50924], "temperature": 0.0, "avg_logprob": -0.138465409327035, "compression_ratio":
  1.5532786885245902, "no_speech_prob": 0.005983843468129635}, {"id": 966, "seek":
  605312, "start": 6065.84, "end": 6072.64, "text": " I think we, like I''ve really
  enjoyed this conversation, Max, we went deep into all these aspects.", "tokens":
  [51000, 286, 519, 321, 11, 411, 286, 600, 534, 4626, 341, 3761, 11, 7402, 11, 321,
  1437, 2452, 666, 439, 613, 7270, 13, 51340], "temperature": 0.0, "avg_logprob":
  -0.138465409327035, "compression_ratio": 1.5532786885245902, "no_speech_prob": 0.005983843468129635},
  {"id": 967, "seek": 605312, "start": 6072.64, "end": 6078.0, "text": " Maybe not
  we can record another episode, you know, going in another direction. I''m sure there
  is", "tokens": [51340, 2704, 406, 321, 393, 2136, 1071, 3500, 11, 291, 458, 11,
  516, 294, 1071, 3513, 13, 286, 478, 988, 456, 307, 51608], "temperature": 0.0, "avg_logprob":
  -0.138465409327035, "compression_ratio": 1.5532786885245902, "no_speech_prob": 0.005983843468129635},
  {"id": 968, "seek": 607800, "start": 6078.0, "end": 6086.56, "text": " like million,
  million directions to take. But I enjoy asking this question of philosophical why,",
  "tokens": [50364, 411, 2459, 11, 2459, 11095, 281, 747, 13, 583, 286, 2103, 3365,
  341, 1168, 295, 25066, 983, 11, 50792], "temperature": 0.0, "avg_logprob": -0.22510557396467343,
  "compression_ratio": 1.5659574468085107, "no_speech_prob": 0.0058393762446939945},
  {"id": 969, "seek": 607800, "start": 6087.12, "end": 6094.0, "text": " if you can
  still spare a few minutes, like why why why why why I''m fascinated by this", "tokens":
  [50820, 498, 291, 393, 920, 13798, 257, 1326, 2077, 11, 411, 983, 983, 983, 983,
  983, 286, 478, 24597, 538, 341, 51164], "temperature": 0.0, "avg_logprob": -0.22510557396467343,
  "compression_ratio": 1.5659574468085107, "no_speech_prob": 0.0058393762446939945},
  {"id": 970, "seek": 607800, "start": 6094.0, "end": 6101.44, "text": " field of
  vector search. What brought you into it? And I remember I will also make sure to",
  "tokens": [51164, 2519, 295, 8062, 3164, 13, 708, 3038, 291, 666, 309, 30, 400,
  286, 1604, 286, 486, 611, 652, 988, 281, 51536], "temperature": 0.0, "avg_logprob":
  -0.22510557396467343, "compression_ratio": 1.5659574468085107, "no_speech_prob":
  0.0058393762446939945}, {"id": 971, "seek": 607800, "start": 6101.44, "end": 6107.76,
  "text": " mention this that we did form a team with you and you you responded positively
  to my inquiry to", "tokens": [51536, 2152, 341, 300, 321, 630, 1254, 257, 1469,
  365, 291, 293, 291, 291, 15806, 25795, 281, 452, 25736, 281, 51852], "temperature":
  0.0, "avg_logprob": -0.22510557396467343, "compression_ratio": 1.5659574468085107,
  "no_speech_prob": 0.0058393762446939945}, {"id": 972, "seek": 610800, "start": 6108.0,
  "end": 6116.08, "text": " compete in in billion scale and then competition. And
  you basically single handedly, almost driven", "tokens": [50364, 11831, 294, 294,
  5218, 4373, 293, 550, 6211, 13, 400, 291, 1936, 2167, 1011, 13516, 11, 1920, 9555,
  50768], "temperature": 0.0, "avg_logprob": -0.25516940222846135, "compression_ratio":
  1.5737704918032787, "no_speech_prob": 0.0024721981026232243}, {"id": 973, "seek":
  610800, "start": 6116.08, "end": 6122.96, "text": " the idea of body PQ. Of course,
  we also have Alexander, similar who was helping you and all of us", "tokens": [50768,
  264, 1558, 295, 1772, 430, 48, 13, 2720, 1164, 11, 321, 611, 362, 14845, 11, 2531,
  567, 390, 4315, 291, 293, 439, 295, 505, 51112], "temperature": 0.0, "avg_logprob":
  -0.25516940222846135, "compression_ratio": 1.5737704918032787, "no_speech_prob":
  0.0024721981026232243}, {"id": 974, "seek": 610800, "start": 6122.96, "end": 6129.84,
  "text": " been brainstorming with you. But so that was kind of like maybe academic
  fascination with it,", "tokens": [51112, 668, 35245, 278, 365, 291, 13, 583, 370,
  300, 390, 733, 295, 411, 1310, 7778, 7184, 2486, 365, 309, 11, 51456], "temperature":
  0.0, "avg_logprob": -0.25516940222846135, "compression_ratio": 1.5737704918032787,
  "no_speech_prob": 0.0024721981026232243}, {"id": 975, "seek": 610800, "start": 6129.84,
  "end": 6135.84, "text": " right? But other other facets that that keep you going
  also giving your background in search,", "tokens": [51456, 558, 30, 583, 661, 661,
  49752, 300, 300, 1066, 291, 516, 611, 2902, 428, 3678, 294, 3164, 11, 51756], "temperature":
  0.0, "avg_logprob": -0.25516940222846135, "compression_ratio": 1.5737704918032787,
  "no_speech_prob": 0.0024721981026232243}, {"id": 976, "seek": 613584, "start": 6135.84,
  "end": 6145.2, "text": " which was pre vector search. Yeah, I''d say just my endless
  curiosity into things, you know,", "tokens": [50364, 597, 390, 659, 8062, 3164,
  13, 865, 11, 286, 1116, 584, 445, 452, 16144, 18769, 666, 721, 11, 291, 458, 11,
  50832], "temperature": 0.0, "avg_logprob": -0.1450278917948405, "compression_ratio":
  1.7048458149779735, "no_speech_prob": 0.006520905531942844}, {"id": 977, "seek":
  613584, "start": 6145.2, "end": 6150.72, "text": " think a lot of us have that as,
  you know, if you''re listening to this podcast, the audience,", "tokens": [50832,
  519, 257, 688, 295, 505, 362, 300, 382, 11, 291, 458, 11, 498, 291, 434, 4764, 281,
  341, 7367, 11, 264, 4034, 11, 51108], "temperature": 0.0, "avg_logprob": -0.1450278917948405,
  "compression_ratio": 1.7048458149779735, "no_speech_prob": 0.006520905531942844},
  {"id": 978, "seek": 613584, "start": 6150.72, "end": 6155.360000000001, "text":
  " there''s probably a lot of you are very curious about just check technology in
  general and the limitations", "tokens": [51108, 456, 311, 1391, 257, 688, 295, 291,
  366, 588, 6369, 466, 445, 1520, 2899, 294, 2674, 293, 264, 15705, 51340], "temperature":
  0.0, "avg_logprob": -0.1450278917948405, "compression_ratio": 1.7048458149779735,
  "no_speech_prob": 0.006520905531942844}, {"id": 979, "seek": 613584, "start": 6155.360000000001,
  "end": 6161.12, "text": " of technology and what''s positive and getting to that
  new magical thing and trying something for", "tokens": [51340, 295, 2899, 293, 437,
  311, 3353, 293, 1242, 281, 300, 777, 12066, 551, 293, 1382, 746, 337, 51628], "temperature":
  0.0, "avg_logprob": -0.1450278917948405, "compression_ratio": 1.7048458149779735,
  "no_speech_prob": 0.006520905531942844}, {"id": 980, "seek": 616112, "start": 6161.12,
  "end": 6166.64, "text": " the first time and saying, Oh my God, this is incredible.
  I can''t believe this actually worked that I", "tokens": [50364, 264, 700, 565,
  293, 1566, 11, 876, 452, 1265, 11, 341, 307, 4651, 13, 286, 393, 380, 1697, 341,
  767, 2732, 300, 286, 50640], "temperature": 0.0, "avg_logprob": -0.12363483224596296,
  "compression_ratio": 1.640495867768595, "no_speech_prob": 0.0021597477607429028},
  {"id": 981, "seek": 616112, "start": 6166.64, "end": 6176.88, "text": " did this.
  So, so it''s that. I mean, I, you know, I''m in my 40s now. So I''ve gone through
  that cycle a", "tokens": [50640, 630, 341, 13, 407, 11, 370, 309, 311, 300, 13,
  286, 914, 11, 286, 11, 291, 458, 11, 286, 478, 294, 452, 3356, 82, 586, 13, 407,
  286, 600, 2780, 807, 300, 6586, 257, 51152], "temperature": 0.0, "avg_logprob":
  -0.12363483224596296, "compression_ratio": 1.640495867768595, "no_speech_prob":
  0.0021597477607429028}, {"id": 982, "seek": 616112, "start": 6176.88, "end": 6183.2,
  "text": " lot of times where I''ve tried something and it was amazing. I do really
  feel that there''s a lot of", "tokens": [51152, 688, 295, 1413, 689, 286, 600, 3031,
  746, 293, 309, 390, 2243, 13, 286, 360, 534, 841, 300, 456, 311, 257, 688, 295,
  51468], "temperature": 0.0, "avg_logprob": -0.12363483224596296, "compression_ratio":
  1.640495867768595, "no_speech_prob": 0.0021597477607429028}, {"id": 983, "seek":
  616112, "start": 6183.2, "end": 6188.48, "text": " practicality to it though, you
  know, in my wisdom now. I see that yeah, just because something", "tokens": [51468,
  8496, 507, 281, 309, 1673, 11, 291, 458, 11, 294, 452, 10712, 586, 13, 286, 536,
  300, 1338, 11, 445, 570, 746, 51732], "temperature": 0.0, "avg_logprob": -0.12363483224596296,
  "compression_ratio": 1.640495867768595, "no_speech_prob": 0.0021597477607429028},
  {"id": 984, "seek": 618848, "start": 6188.48, "end": 6193.44, "text": " looks cool
  doesn''t mean it''s the best thing in the world and it should be used everywhere.
  So I,", "tokens": [50364, 1542, 1627, 1177, 380, 914, 309, 311, 264, 1151, 551,
  294, 264, 1002, 293, 309, 820, 312, 1143, 5315, 13, 407, 286, 11, 50612], "temperature":
  0.0, "avg_logprob": -0.11597125044146787, "compression_ratio": 1.615702479338843,
  "no_speech_prob": 0.0005102952709421515}, {"id": 985, "seek": 618848, "start": 6193.44,
  "end": 6205.04, "text": " I see the practical, the practical use and need for vector
  search. Whether or not it turns out to be", "tokens": [50612, 286, 536, 264, 8496,
  11, 264, 8496, 764, 293, 643, 337, 8062, 3164, 13, 8503, 420, 406, 309, 4523, 484,
  281, 312, 51192], "temperature": 0.0, "avg_logprob": -0.11597125044146787, "compression_ratio":
  1.615702479338843, "no_speech_prob": 0.0005102952709421515}, {"id": 986, "seek":
  618848, "start": 6205.04, "end": 6211.2, "text": " like the end all be all the search,
  you know, that debate is open, right? But I don''t think it is.", "tokens": [51192,
  411, 264, 917, 439, 312, 439, 264, 3164, 11, 291, 458, 11, 300, 7958, 307, 1269,
  11, 558, 30, 583, 286, 500, 380, 519, 309, 307, 13, 51500], "temperature": 0.0,
  "avg_logprob": -0.11597125044146787, "compression_ratio": 1.615702479338843, "no_speech_prob":
  0.0005102952709421515}, {"id": 987, "seek": 618848, "start": 6211.2, "end": 6217.04,
  "text": " I think it''s just one piece in the puzzle. But it does solve this whole
  class of problems that", "tokens": [51500, 286, 519, 309, 311, 445, 472, 2522, 294,
  264, 12805, 13, 583, 309, 775, 5039, 341, 1379, 1508, 295, 2740, 300, 51792], "temperature":
  0.0, "avg_logprob": -0.11597125044146787, "compression_ratio": 1.615702479338843,
  "no_speech_prob": 0.0005102952709421515}, {"id": 988, "seek": 621704, "start": 6217.04,
  "end": 6223.5199999999995, "text": " were unsolvable before if you go back 10 years.
  When I first started in search, the types of things", "tokens": [50364, 645, 2693,
  401, 17915, 949, 498, 291, 352, 646, 1266, 924, 13, 1133, 286, 700, 1409, 294, 3164,
  11, 264, 3467, 295, 721, 50688], "temperature": 0.0, "avg_logprob": -0.11372274206590283,
  "compression_ratio": 1.8007380073800738, "no_speech_prob": 0.0010112569434568286},
  {"id": 989, "seek": 621704, "start": 6223.5199999999995, "end": 6229.36, "text":
  " that I''m doing right now. And I''ll give you an example and I actually, you know,
  I set this to", "tokens": [50688, 300, 286, 478, 884, 558, 586, 13, 400, 286, 603,
  976, 291, 364, 1365, 293, 286, 767, 11, 291, 458, 11, 286, 992, 341, 281, 50980],
  "temperature": 0.0, "avg_logprob": -0.11372274206590283, "compression_ratio": 1.8007380073800738,
  "no_speech_prob": 0.0010112569434568286}, {"id": 990, "seek": 621704, "start": 6229.36,
  "end": 6234.64, "text": " somebody the other day. It''s like, you know, the first
  time I installed solar, this is even, you", "tokens": [50980, 2618, 264, 661, 786,
  13, 467, 311, 411, 11, 291, 458, 11, 264, 700, 565, 286, 8899, 7936, 11, 341, 307,
  754, 11, 291, 51244], "temperature": 0.0, "avg_logprob": -0.11372274206590283, "compression_ratio":
  1.8007380073800738, "no_speech_prob": 0.0010112569434568286}, {"id": 991, "seek":
  621704, "start": 6234.64, "end": 6238.16, "text": " know, maybe elastic search was
  around at that time, but maybe it was compass search. It wasn''t even", "tokens":
  [51244, 458, 11, 1310, 17115, 3164, 390, 926, 412, 300, 565, 11, 457, 1310, 309,
  390, 10707, 3164, 13, 467, 2067, 380, 754, 51420], "temperature": 0.0, "avg_logprob":
  -0.11372274206590283, "compression_ratio": 1.8007380073800738, "no_speech_prob":
  0.0010112569434568286}, {"id": 992, "seek": 621704, "start": 6238.16, "end": 6243.04,
  "text": " elastic yet. The first time I installed solar and I put in some documents,
  I was like, wow, this", "tokens": [51420, 17115, 1939, 13, 440, 700, 565, 286, 8899,
  7936, 293, 286, 829, 294, 512, 8512, 11, 286, 390, 411, 11, 6076, 11, 341, 51664],
  "temperature": 0.0, "avg_logprob": -0.11372274206590283, "compression_ratio": 1.8007380073800738,
  "no_speech_prob": 0.0010112569434568286}, {"id": 993, "seek": 624304, "start": 6243.04,
  "end": 6248.32, "text": " is amazing. Like I can do a search. This is so much better
  than that crappy index that I was using", "tokens": [50364, 307, 2243, 13, 1743,
  286, 393, 360, 257, 3164, 13, 639, 307, 370, 709, 1101, 813, 300, 36531, 8186, 300,
  286, 390, 1228, 50628], "temperature": 0.0, "avg_logprob": -0.1406606760892001,
  "compression_ratio": 1.7357142857142858, "no_speech_prob": 0.00035309369559399784},
  {"id": 994, "seek": 624304, "start": 6248.32, "end": 6255.44, "text": " on SQL Server.
  So it was just really, it was like that type of amazement. But then you,", "tokens":
  [50628, 322, 19200, 25684, 13, 407, 309, 390, 445, 534, 11, 309, 390, 411, 300,
  2010, 295, 669, 921, 1712, 13, 583, 550, 291, 11, 50984], "temperature": 0.0, "avg_logprob":
  -0.1406606760892001, "compression_ratio": 1.7357142857142858, "no_speech_prob":
  0.00035309369559399784}, {"id": 995, "seek": 624304, "start": 6255.44, "end": 6260.64,
  "text": " you know, you work with it over time, you see the limitations and it''s
  like, oh, this got it out", "tokens": [50984, 291, 458, 11, 291, 589, 365, 309,
  670, 565, 11, 291, 536, 264, 15705, 293, 309, 311, 411, 11, 1954, 11, 341, 658,
  309, 484, 51244], "temperature": 0.0, "avg_logprob": -0.1406606760892001, "compression_ratio":
  1.7357142857142858, "no_speech_prob": 0.00035309369559399784}, {"id": 996, "seek":
  624304, "start": 6260.64, "end": 6265.28, "text": " of these synonyms and all these
  other problems and all this stuff. I''ll say that, you know, when you", "tokens":
  [51244, 295, 613, 5451, 2526, 2592, 293, 439, 613, 661, 2740, 293, 439, 341, 1507,
  13, 286, 603, 584, 300, 11, 291, 458, 11, 562, 291, 51476], "temperature": 0.0,
  "avg_logprob": -0.1406606760892001, "compression_ratio": 1.7357142857142858, "no_speech_prob":
  0.00035309369559399784}, {"id": 997, "seek": 624304, "start": 6265.28, "end": 6270.24,
  "text": " when you first start off in like the relevance of solar, like out of the
  box, you take their example,", "tokens": [51476, 562, 291, 700, 722, 766, 294, 411,
  264, 32684, 295, 7936, 11, 411, 484, 295, 264, 2424, 11, 291, 747, 641, 1365, 11,
  51724], "temperature": 0.0, "avg_logprob": -0.1406606760892001, "compression_ratio":
  1.7357142857142858, "no_speech_prob": 0.00035309369559399784}, {"id": 998, "seek":
  627024, "start": 6271.12, "end": 6278.48, "text": " schema XML and you and you add
  some documents to it and you get back stuff and you''re like, okay,", "tokens":
  [50408, 34078, 43484, 293, 291, 293, 291, 909, 512, 8512, 281, 309, 293, 291, 483,
  646, 1507, 293, 291, 434, 411, 11, 1392, 11, 50776], "temperature": 0.0, "avg_logprob":
  -0.17839252587520715, "compression_ratio": 1.6569037656903767, "no_speech_prob":
  0.0020829071290791035}, {"id": 999, "seek": 627024, "start": 6278.48, "end": 6285.679999999999,
  "text": " this is cool. If you take that feeling and then you once and I''ll just
  use quadrant for an example", "tokens": [50776, 341, 307, 1627, 13, 759, 291, 747,
  300, 2633, 293, 550, 291, 1564, 293, 286, 603, 445, 764, 46856, 337, 364, 1365,
  51136], "temperature": 0.0, "avg_logprob": -0.17839252587520715, "compression_ratio":
  1.6569037656903767, "no_speech_prob": 0.0020829071290791035}, {"id": 1000, "seek":
  627024, "start": 6285.679999999999, "end": 6291.84, "text": " because quadrant is
  in my opinion, like super easy to use, like you just doc or pull quadrant and",
  "tokens": [51136, 570, 46856, 307, 294, 452, 4800, 11, 411, 1687, 1858, 281, 764,
  11, 411, 291, 445, 3211, 420, 2235, 46856, 293, 51444], "temperature": 0.0, "avg_logprob":
  -0.17839252587520715, "compression_ratio": 1.6569037656903767, "no_speech_prob":
  0.0020829071290791035}, {"id": 1001, "seek": 627024, "start": 6291.84, "end": 6298.639999999999,
  "text": " use throw some and stuff in there. Especially now with this node thing.
  So when I did that, the first", "tokens": [51444, 764, 3507, 512, 293, 1507, 294,
  456, 13, 8545, 586, 365, 341, 9984, 551, 13, 407, 562, 286, 630, 300, 11, 264, 700,
  51784], "temperature": 0.0, "avg_logprob": -0.17839252587520715, "compression_ratio":
  1.6569037656903767, "no_speech_prob": 0.0020829071290791035}, {"id": 1002, "seek":
  629864, "start": 6298.64, "end": 6302.8, "text": " time I used quadrant and I wrote
  this node wrapper and I just chucked in a whole bunch of documents,", "tokens":
  [50364, 565, 286, 1143, 46856, 293, 286, 4114, 341, 9984, 46906, 293, 286, 445,
  20870, 292, 294, 257, 1379, 3840, 295, 8512, 11, 50572], "temperature": 0.0, "avg_logprob":
  -0.12379133208724093, "compression_ratio": 1.7906137184115523, "no_speech_prob":
  0.0004194905632175505}, {"id": 1003, "seek": 629864, "start": 6302.8, "end": 6308.4800000000005,
  "text": " I saw that like just the out of the box relevance. And I''m not saying
  this is fine tuned, like this", "tokens": [50572, 286, 1866, 300, 411, 445, 264,
  484, 295, 264, 2424, 32684, 13, 400, 286, 478, 406, 1566, 341, 307, 2489, 10870,
  11, 411, 341, 50856], "temperature": 0.0, "avg_logprob": -0.12379133208724093, "compression_ratio":
  1.7906137184115523, "no_speech_prob": 0.0004194905632175505}, {"id": 1004, "seek":
  629864, "start": 6308.4800000000005, "end": 6314.56, "text": " isn''t something
  production worthy. But just the out of the box relevance, I was like, this is better",
  "tokens": [50856, 1943, 380, 746, 4265, 14829, 13, 583, 445, 264, 484, 295, 264,
  2424, 32684, 11, 286, 390, 411, 11, 341, 307, 1101, 51160], "temperature": 0.0,
  "avg_logprob": -0.12379133208724093, "compression_ratio": 1.7906137184115523, "no_speech_prob":
  0.0004194905632175505}, {"id": 1005, "seek": 629864, "start": 6314.56, "end": 6321.52,
  "text": " and I would spend in my opinion less time worrying about this than I would
  with an inverted index,", "tokens": [51160, 293, 286, 576, 3496, 294, 452, 4800,
  1570, 565, 18788, 466, 341, 813, 286, 576, 365, 364, 38969, 8186, 11, 51508], "temperature":
  0.0, "avg_logprob": -0.12379133208724093, "compression_ratio": 1.7906137184115523,
  "no_speech_prob": 0.0004194905632175505}, {"id": 1006, "seek": 629864, "start":
  6321.52, "end": 6328.240000000001, "text": " you know, just because well, yeah,
  maybe the results aren''t like super precise all the time and", "tokens": [51508,
  291, 458, 11, 445, 570, 731, 11, 1338, 11, 1310, 264, 3542, 3212, 380, 411, 1687,
  13600, 439, 264, 565, 293, 51844], "temperature": 0.0, "avg_logprob": -0.12379133208724093,
  "compression_ratio": 1.7906137184115523, "no_speech_prob": 0.0004194905632175505},
  {"id": 1007, "seek": 632824, "start": 6328.32, "end": 6334.639999999999, "text":
  " things like that. But if I''m on a team and it''s like, I got this search bar
  and I got this content and", "tokens": [50368, 721, 411, 300, 13, 583, 498, 286,
  478, 322, 257, 1469, 293, 309, 311, 411, 11, 286, 658, 341, 3164, 2159, 293, 286,
  658, 341, 2701, 293, 50684], "temperature": 0.0, "avg_logprob": -0.10822598492657697,
  "compression_ratio": 1.92578125, "no_speech_prob": 0.001967298099771142}, {"id":
  1008, "seek": 632824, "start": 6336.48, "end": 6340.88, "text": " I don''t want
  to worry about it, right? I don''t want to worry about it. I just wanted to work.
  I", "tokens": [50776, 286, 500, 380, 528, 281, 3292, 466, 309, 11, 558, 30, 286,
  500, 380, 528, 281, 3292, 466, 309, 13, 286, 445, 1415, 281, 589, 13, 286, 50996],
  "temperature": 0.0, "avg_logprob": -0.10822598492657697, "compression_ratio": 1.92578125,
  "no_speech_prob": 0.001967298099771142}, {"id": 1009, "seek": 632824, "start": 6340.88,
  "end": 6345.2, "text": " wanted to surface stuff that''s like reasonably accurate.
  It doesn''t have to be the best search in the", "tokens": [50996, 1415, 281, 3753,
  1507, 300, 311, 411, 23551, 8559, 13, 467, 1177, 380, 362, 281, 312, 264, 1151,
  3164, 294, 264, 51212], "temperature": 0.0, "avg_logprob": -0.10822598492657697,
  "compression_ratio": 1.92578125, "no_speech_prob": 0.001967298099771142}, {"id":
  1010, "seek": 632824, "start": 6345.2, "end": 6350.88, "text": " world. But it''s
  a cost for me. It''s a cost for me as a team. I don''t make money from search, but",
  "tokens": [51212, 1002, 13, 583, 309, 311, 257, 2063, 337, 385, 13, 467, 311, 257,
  2063, 337, 385, 382, 257, 1469, 13, 286, 500, 380, 652, 1460, 490, 3164, 11, 457,
  51496], "temperature": 0.0, "avg_logprob": -0.10822598492657697, "compression_ratio":
  1.92578125, "no_speech_prob": 0.001967298099771142}, {"id": 1011, "seek": 632824,
  "start": 6350.88, "end": 6355.92, "text": " it''s something I have to support. I
  think vector search offers are really, really good solution", "tokens": [51496,
  309, 311, 746, 286, 362, 281, 1406, 13, 286, 519, 8062, 3164, 7736, 366, 534, 11,
  534, 665, 3827, 51748], "temperature": 0.0, "avg_logprob": -0.10822598492657697,
  "compression_ratio": 1.92578125, "no_speech_prob": 0.001967298099771142}, {"id":
  1012, "seek": 635592, "start": 6356.24, "end": 6364.72, "text": " because it''s
  not like you have to chase that endless bug of this doesn''t even have anything
  to do", "tokens": [50380, 570, 309, 311, 406, 411, 291, 362, 281, 15359, 300, 16144,
  7426, 295, 341, 1177, 380, 754, 362, 1340, 281, 360, 50804], "temperature": 0.0,
  "avg_logprob": -0.1995239512125651, "compression_ratio": 1.597883597883598, "no_speech_prob":
  0.008552688173949718}, {"id": 1013, "seek": 635592, "start": 6364.72, "end": 6374.4800000000005,
  "text": " with my search. I search for, you know, what is the best hiking boot or
  something like that, you know?", "tokens": [50804, 365, 452, 3164, 13, 286, 3164,
  337, 11, 291, 458, 11, 437, 307, 264, 1151, 23784, 11450, 420, 746, 411, 300, 11,
  291, 458, 30, 51292], "temperature": 0.0, "avg_logprob": -0.1995239512125651, "compression_ratio":
  1.597883597883598, "no_speech_prob": 0.008552688173949718}, {"id": 1014, "seek":
  635592, "start": 6374.4800000000005, "end": 6381.2, "text": " And all the documents
  they matched what 10 times, but there''s no semblance of hiking boot or anything",
  "tokens": [51292, 400, 439, 264, 8512, 436, 21447, 437, 1266, 1413, 11, 457, 456,
  311, 572, 20775, 37271, 295, 23784, 11450, 420, 1340, 51628], "temperature": 0.0,
  "avg_logprob": -0.1995239512125651, "compression_ratio": 1.597883597883598, "no_speech_prob":
  0.008552688173949718}, {"id": 1015, "seek": 638120, "start": 6381.28, "end": 6385.5199999999995,
  "text": " in my document. This is terrible. You know, you don''t get anything like
  that in vector search.", "tokens": [50368, 294, 452, 4166, 13, 639, 307, 6237, 13,
  509, 458, 11, 291, 500, 380, 483, 1340, 411, 300, 294, 8062, 3164, 13, 50580], "temperature":
  0.0, "avg_logprob": -0.1636473083496094, "compression_ratio": 1.7404580152671756,
  "no_speech_prob": 0.0034643705002963543}, {"id": 1016, "seek": 638120, "start":
  6386.08, "end": 6391.2, "text": " And that''s, I think, the appeal. You know, when
  you get into like real,", "tokens": [50608, 400, 300, 311, 11, 286, 519, 11, 264,
  13668, 13, 509, 458, 11, 562, 291, 483, 666, 411, 957, 11, 50864], "temperature":
  0.0, "avg_logprob": -0.1636473083496094, "compression_ratio": 1.7404580152671756,
  "no_speech_prob": 0.0034643705002963543}, {"id": 1017, "seek": 638120, "start":
  6392.4, "end": 6398.5599999999995, "text": " real production, like highly tuned
  search, it''s just one piece. But just for the teams that''s like", "tokens": [50924,
  957, 4265, 11, 411, 5405, 10870, 3164, 11, 309, 311, 445, 472, 2522, 13, 583, 445,
  337, 264, 5491, 300, 311, 411, 51232], "temperature": 0.0, "avg_logprob": -0.1636473083496094,
  "compression_ratio": 1.7404580152671756, "no_speech_prob": 0.0034643705002963543},
  {"id": 1018, "seek": 638120, "start": 6398.5599999999995, "end": 6403.36, "text":
  " out of the box, I want to work and I don''t want to deal with it. I think it''s
  a better,", "tokens": [51232, 484, 295, 264, 2424, 11, 286, 528, 281, 589, 293,
  286, 500, 380, 528, 281, 2028, 365, 309, 13, 286, 519, 309, 311, 257, 1101, 11,
  51472], "temperature": 0.0, "avg_logprob": -0.1636473083496094, "compression_ratio":
  1.7404580152671756, "no_speech_prob": 0.0034643705002963543}, {"id": 1019, "seek":
  638120, "start": 6404.16, "end": 6409.5199999999995, "text": " I think it''s a better
  solution than elasticer solar. You end up spending a lot less time and headache.",
  "tokens": [51512, 286, 519, 309, 311, 257, 1101, 3827, 813, 17115, 260, 7936, 13,
  509, 917, 493, 6434, 257, 688, 1570, 565, 293, 23520, 13, 51780], "temperature":
  0.0, "avg_logprob": -0.1636473083496094, "compression_ratio": 1.7404580152671756,
  "no_speech_prob": 0.0034643705002963543}, {"id": 1020, "seek": 640952, "start":
  6410.4800000000005, "end": 6414.4800000000005, "text": " Yeah, that''s amazing.
  That''s that''s so deep. And in what you said,", "tokens": [50412, 865, 11, 300,
  311, 2243, 13, 663, 311, 300, 311, 370, 2452, 13, 400, 294, 437, 291, 848, 11, 50612],
  "temperature": 0.0, "avg_logprob": -0.16556003656280174, "compression_ratio": 1.72,
  "no_speech_prob": 0.009662752971053123}, {"id": 1021, "seek": 640952, "start": 6416.4800000000005,
  "end": 6423.040000000001, "text": " speaks, speaks and sings a practitioner, but
  I think also speaks and sings a dreamer.", "tokens": [50712, 10789, 11, 10789, 293,
  23250, 257, 32125, 11, 457, 286, 519, 611, 10789, 293, 23250, 257, 3055, 260, 13,
  51040], "temperature": 0.0, "avg_logprob": -0.16556003656280174, "compression_ratio":
  1.72, "no_speech_prob": 0.009662752971053123}, {"id": 1022, "seek": 640952, "start":
  6423.68, "end": 6429.68, "text": " I think you dream of better ways of searching
  things, right? And like you went through it", "tokens": [51072, 286, 519, 291, 3055,
  295, 1101, 2098, 295, 10808, 721, 11, 558, 30, 400, 411, 291, 1437, 807, 309, 51372],
  "temperature": 0.0, "avg_logprob": -0.16556003656280174, "compression_ratio": 1.72,
  "no_speech_prob": 0.009662752971053123}, {"id": 1023, "seek": 640952, "start": 6430.56,
  "end": 6438.160000000001, "text": " practically, but also, you know, when you when
  you get so deep into practical elements, you get stuck", "tokens": [51416, 15667,
  11, 457, 611, 11, 291, 458, 11, 562, 291, 562, 291, 483, 370, 2452, 666, 8496, 4959,
  11, 291, 483, 5541, 51796], "temperature": 0.0, "avg_logprob": -0.16556003656280174,
  "compression_ratio": 1.72, "no_speech_prob": 0.009662752971053123}, {"id": 1024,
  "seek": 643816, "start": 6438.24, "end": 6443.28, "text": " into it and you''re
  like, you''re thinking in the in the framework of the given system,", "tokens":
  [50368, 666, 309, 293, 291, 434, 411, 11, 291, 434, 1953, 294, 264, 294, 264, 8388,
  295, 264, 2212, 1185, 11, 50620], "temperature": 0.0, "avg_logprob": -0.13786199903979743,
  "compression_ratio": 1.6622222222222223, "no_speech_prob": 0.0015538427978754044},
  {"id": 1025, "seek": 643816, "start": 6443.28, "end": 6448.96, "text": " of a given
  language even, right? Sometimes the paradigms that you read through the docs and
  you", "tokens": [50620, 295, 257, 2212, 2856, 754, 11, 558, 30, 4803, 264, 13480,
  328, 2592, 300, 291, 1401, 807, 264, 45623, 293, 291, 50904], "temperature": 0.0,
  "avg_logprob": -0.13786199903979743, "compression_ratio": 1.6622222222222223, "no_speech_prob":
  0.0015538427978754044}, {"id": 1026, "seek": 643816, "start": 6448.96, "end": 6455.2,
  "text": " keep thinking about them, it''s hard to unstick yourself from them. And
  I mean, the fact that", "tokens": [50904, 1066, 1953, 466, 552, 11, 309, 311, 1152,
  281, 517, 11881, 1803, 490, 552, 13, 400, 286, 914, 11, 264, 1186, 300, 51216],
  "temperature": 0.0, "avg_logprob": -0.13786199903979743, "compression_ratio": 1.6622222222222223,
  "no_speech_prob": 0.0015538427978754044}, {"id": 1027, "seek": 643816, "start":
  6455.2, "end": 6462.48, "text": " vector search field was born is magical in many
  ways. So I feel like you feel the same. And I mean,", "tokens": [51216, 8062, 3164,
  2519, 390, 4232, 307, 12066, 294, 867, 2098, 13, 407, 286, 841, 411, 291, 841, 264,
  912, 13, 400, 286, 914, 11, 51580], "temperature": 0.0, "avg_logprob": -0.13786199903979743,
  "compression_ratio": 1.6622222222222223, "no_speech_prob": 0.0015538427978754044},
  {"id": 1028, "seek": 646248, "start": 6462.48, "end": 6469.36, "text": " the fact
  that you also ventured with me and others into building a new algorithm for vector
  search", "tokens": [50364, 264, 1186, 300, 291, 611, 6931, 3831, 365, 385, 293,
  2357, 666, 2390, 257, 777, 9284, 337, 8062, 3164, 50708], "temperature": 0.0, "avg_logprob":
  -0.11177883353284611, "compression_ratio": 1.6863636363636363, "no_speech_prob":
  0.0067966715432703495}, {"id": 1029, "seek": 646248, "start": 6469.36, "end": 6476.32,
  "text": " also says that that you wanted to go as deep as implementing an algorithm,
  right? So", "tokens": [50708, 611, 1619, 300, 300, 291, 1415, 281, 352, 382, 2452,
  382, 18114, 364, 9284, 11, 558, 30, 407, 51056], "temperature": 0.0, "avg_logprob":
  -0.11177883353284611, "compression_ratio": 1.6863636363636363, "no_speech_prob":
  0.0067966715432703495}, {"id": 1030, "seek": 646248, "start": 6476.32, "end": 6481.2,
  "text": " which what could be sexier than implementing an algorithm? I mean, I don''t
  know. Of course,", "tokens": [51056, 597, 437, 727, 312, 3260, 811, 813, 18114,
  364, 9284, 30, 286, 914, 11, 286, 500, 380, 458, 13, 2720, 1164, 11, 51300], "temperature":
  0.0, "avg_logprob": -0.11177883353284611, "compression_ratio": 1.6863636363636363,
  "no_speech_prob": 0.0067966715432703495}, {"id": 1031, "seek": 646248, "start":
  6481.2, "end": 6486.48, "text": " all other things are also sexy, but I''m just
  saying that it''s very it''s very complex. It''s very", "tokens": [51300, 439, 661,
  721, 366, 611, 13701, 11, 457, 286, 478, 445, 1566, 300, 309, 311, 588, 309, 311,
  588, 3997, 13, 467, 311, 588, 51564], "temperature": 0.0, "avg_logprob": -0.11177883353284611,
  "compression_ratio": 1.6863636363636363, "no_speech_prob": 0.0067966715432703495},
  {"id": 1032, "seek": 648648, "start": 6487.28, "end": 6495.5199999999995, "text":
  " demanding in intellectually demanding work. So that that''s amazing. Thanks so
  much for this depth.", "tokens": [50404, 19960, 294, 46481, 19960, 589, 13, 407,
  300, 300, 311, 2243, 13, 2561, 370, 709, 337, 341, 7161, 13, 50816], "temperature":
  0.0, "avg_logprob": -0.19223440847089213, "compression_ratio": 1.7657657657657657,
  "no_speech_prob": 0.006982909515500069}, {"id": 1033, "seek": 648648, "start": 6495.5199999999995,
  "end": 6501.839999999999, "text": " And is there something you would like to share
  or announce with, you know, on mighty or maybe on", "tokens": [50816, 400, 307,
  456, 746, 291, 576, 411, 281, 2073, 420, 7478, 365, 11, 291, 458, 11, 322, 21556,
  420, 1310, 322, 51132], "temperature": 0.0, "avg_logprob": -0.19223440847089213,
  "compression_ratio": 1.7657657657657657, "no_speech_prob": 0.006982909515500069},
  {"id": 1034, "seek": 648648, "start": 6501.839999999999, "end": 6506.799999999999,
  "text": " something you''re going to be presenting on Berlin buzzwords, I know as
  well, but is there something", "tokens": [51132, 746, 291, 434, 516, 281, 312, 15578,
  322, 13848, 13036, 13832, 11, 286, 458, 382, 731, 11, 457, 307, 456, 746, 51380],
  "temperature": 0.0, "avg_logprob": -0.19223440847089213, "compression_ratio": 1.7657657657657657,
  "no_speech_prob": 0.006982909515500069}, {"id": 1035, "seek": 648648, "start": 6506.799999999999,
  "end": 6515.12, "text": " that you would like to share? Yeah, so I am presenting
  a Berlin buzzwords. I am putting together", "tokens": [51380, 300, 291, 576, 411,
  281, 2073, 30, 865, 11, 370, 286, 669, 15578, 257, 13848, 13036, 13832, 13, 286,
  669, 3372, 1214, 51796], "temperature": 0.0, "avg_logprob": -0.19223440847089213,
  "compression_ratio": 1.7657657657657657, "no_speech_prob": 0.006982909515500069},
  {"id": 1036, "seek": 651512, "start": 6515.68, "end": 6522.0, "text": " a charity
  event to hack on vector search. And that''s going to be on May 5th. I don''t know
  when this", "tokens": [50392, 257, 16863, 2280, 281, 10339, 322, 8062, 3164, 13,
  400, 300, 311, 516, 281, 312, 322, 1891, 1025, 392, 13, 286, 500, 380, 458, 562,
  341, 50708], "temperature": 0.0, "avg_logprob": -0.13522368344393643, "compression_ratio":
  1.6625, "no_speech_prob": 0.0016674576327204704}, {"id": 1037, "seek": 651512, "start":
  6522.0, "end": 6528.4, "text": " podcast will be published, but on May 5th, I want
  to get and I want it to be it''s just going to be", "tokens": [50708, 7367, 486,
  312, 6572, 11, 457, 322, 1891, 1025, 392, 11, 286, 528, 281, 483, 293, 286, 528,
  309, 281, 312, 309, 311, 445, 516, 281, 312, 51028], "temperature": 0.0, "avg_logprob":
  -0.13522368344393643, "compression_ratio": 1.6625, "no_speech_prob": 0.0016674576327204704},
  {"id": 1038, "seek": 651512, "start": 6528.4, "end": 6535.04, "text": " an all day
  learning session on and I''m not charging money for this. This is like free. I just
  want to", "tokens": [51028, 364, 439, 786, 2539, 5481, 322, 293, 286, 478, 406,
  11379, 1460, 337, 341, 13, 639, 307, 411, 1737, 13, 286, 445, 528, 281, 51360],
  "temperature": 0.0, "avg_logprob": -0.13522368344393643, "compression_ratio": 1.6625,
  "no_speech_prob": 0.0016674576327204704}, {"id": 1039, "seek": 651512, "start":
  6535.599999999999, "end": 6540.72, "text": " show people how to use these tools
  if you''re not in the Python world. If you''re part of the Python", "tokens": [51388,
  855, 561, 577, 281, 764, 613, 3873, 498, 291, 434, 406, 294, 264, 15329, 1002, 13,
  759, 291, 434, 644, 295, 264, 15329, 51644], "temperature": 0.0, "avg_logprob":
  -0.13522368344393643, "compression_ratio": 1.6625, "no_speech_prob": 0.0016674576327204704},
  {"id": 1040, "seek": 654072, "start": 6540.72, "end": 6548.0, "text": " world, you
  want to join amazing. Great. But I want to do an all day like hackathon, where I''ll
  show", "tokens": [50364, 1002, 11, 291, 528, 281, 3917, 2243, 13, 3769, 13, 583,
  286, 528, 281, 360, 364, 439, 786, 411, 10339, 18660, 11, 689, 286, 603, 855, 50728],
  "temperature": 0.0, "avg_logprob": -0.19846921920776367, "compression_ratio": 1.6431535269709543,
  "no_speech_prob": 0.0018031391082331538}, {"id": 1041, "seek": 654072, "start":
  6548.0, "end": 6553.04, "text": " you how to get these things up and running hack
  away at it by the end you''ll have, you know, a working", "tokens": [50728, 291,
  577, 281, 483, 613, 721, 493, 293, 2614, 10339, 1314, 412, 309, 538, 264, 917, 291,
  603, 362, 11, 291, 458, 11, 257, 1364, 50980], "temperature": 0.0, "avg_logprob":
  -0.19846921920776367, "compression_ratio": 1.6431535269709543, "no_speech_prob":
  0.0018031391082331538}, {"id": 1042, "seek": 654072, "start": 6553.04, "end": 6558.72,
  "text": " or working example on your own. And all the money we''re all the time
  we''re going to raise money for", "tokens": [50980, 420, 1364, 1365, 322, 428, 1065,
  13, 400, 439, 264, 1460, 321, 434, 439, 264, 565, 321, 434, 516, 281, 5300, 1460,
  337, 51264], "temperature": 0.0, "avg_logprob": -0.19846921920776367, "compression_ratio":
  1.6431535269709543, "no_speech_prob": 0.0018031391082331538}, {"id": 1043, "seek":
  654072, "start": 6558.72, "end": 6565.12, "text": " charity, specifically around
  refugees and displaced people, you know, because of the horrible", "tokens": [51264,
  16863, 11, 4682, 926, 18301, 293, 33692, 561, 11, 291, 458, 11, 570, 295, 264, 9263,
  51584], "temperature": 0.0, "avg_logprob": -0.19846921920776367, "compression_ratio":
  1.6431535269709543, "no_speech_prob": 0.0018031391082331538}, {"id": 1044, "seek":
  656512, "start": 6565.2, "end": 6572.88, "text": " things that are happening in
  Ukraine and other parts of the world as well. You know, getting", "tokens": [50368,
  721, 300, 366, 2737, 294, 14081, 293, 661, 3166, 295, 264, 1002, 382, 731, 13, 509,
  458, 11, 1242, 50752], "temperature": 0.0, "avg_logprob": -0.1525156878042912, "compression_ratio":
  1.4742268041237114, "no_speech_prob": 0.001272257068194449}, {"id": 1045, "seek":
  656512, "start": 6574.0, "end": 6579.76, "text": " getting some learning happening
  and also raising money for charity seems like a great way to spend", "tokens": [50808,
  1242, 512, 2539, 2737, 293, 611, 11225, 1460, 337, 16863, 2544, 411, 257, 869, 636,
  281, 3496, 51096], "temperature": 0.0, "avg_logprob": -0.1525156878042912, "compression_ratio":
  1.4742268041237114, "no_speech_prob": 0.001272257068194449}, {"id": 1046, "seek":
  656512, "start": 6579.76, "end": 6588.4, "text": " time. So I plan to host that
  on May 5th. It''s probably going to be on Twitch because I want to", "tokens": [51096,
  565, 13, 407, 286, 1393, 281, 3975, 300, 322, 1891, 1025, 392, 13, 467, 311, 1391,
  516, 281, 312, 322, 22222, 570, 286, 528, 281, 51528], "temperature": 0.0, "avg_logprob":
  -0.1525156878042912, "compression_ratio": 1.4742268041237114, "no_speech_prob":
  0.001272257068194449}, {"id": 1047, "seek": 658840, "start": 6589.36, "end": 6594.799999999999,
  "text": " just to be an open drop in drop out format. You can come, you can go.
  It''s not going to be like a", "tokens": [50412, 445, 281, 312, 364, 1269, 3270,
  294, 3270, 484, 7877, 13, 509, 393, 808, 11, 291, 393, 352, 13, 467, 311, 406, 516,
  281, 312, 411, 257, 50684], "temperature": 0.0, "avg_logprob": -0.1657773866428165,
  "compression_ratio": 1.6986301369863013, "no_speech_prob": 0.022870071232318878},
  {"id": 1048, "seek": 658840, "start": 6594.799999999999, "end": 6600.0, "text":
  " controlled zoom where you, you know, it''s like that. It''s going to be on Twitch
  with chat and stuff", "tokens": [50684, 10164, 8863, 689, 291, 11, 291, 458, 11,
  309, 311, 411, 300, 13, 467, 311, 516, 281, 312, 322, 22222, 365, 5081, 293, 1507,
  50944], "temperature": 0.0, "avg_logprob": -0.1657773866428165, "compression_ratio":
  1.6986301369863013, "no_speech_prob": 0.022870071232318878}, {"id": 1049, "seek":
  658840, "start": 6600.0, "end": 6604.32, "text": " like that. So I''m going to get
  it all set up. Details are going to come out shortly. By the time", "tokens": [50944,
  411, 300, 13, 407, 286, 478, 516, 281, 483, 309, 439, 992, 493, 13, 42811, 366,
  516, 281, 808, 484, 13392, 13, 3146, 264, 565, 51160], "temperature": 0.0, "avg_logprob":
  -0.1657773866428165, "compression_ratio": 1.6986301369863013, "no_speech_prob":
  0.022870071232318878}, {"id": 1050, "seek": 658840, "start": 6604.32, "end": 6609.2,
  "text": " this is published, maybe the details will be available already and we''ll
  drop a link. Yeah, awesome.", "tokens": [51160, 341, 307, 6572, 11, 1310, 264, 4365,
  486, 312, 2435, 1217, 293, 321, 603, 3270, 257, 2113, 13, 865, 11, 3476, 13, 51404],
  "temperature": 0.0, "avg_logprob": -0.1657773866428165, "compression_ratio": 1.6986301369863013,
  "no_speech_prob": 0.022870071232318878}, {"id": 1051, "seek": 658840, "start": 6609.2,
  "end": 6617.44, "text": " This sounds amazing that you also keep thinking about
  this sensitive topics or like what''s happening", "tokens": [51404, 639, 3263, 2243,
  300, 291, 611, 1066, 1953, 466, 341, 9477, 8378, 420, 411, 437, 311, 2737, 51816],
  "temperature": 0.0, "avg_logprob": -0.1657773866428165, "compression_ratio": 1.6986301369863013,
  "no_speech_prob": 0.022870071232318878}, {"id": 1052, "seek": 661744, "start": 6618.0,
  "end": 6623.919999999999, "text": " in the world and you are also contributing with
  your skills into a good course here.", "tokens": [50392, 294, 264, 1002, 293, 291,
  366, 611, 19270, 365, 428, 3942, 666, 257, 665, 1164, 510, 13, 50688], "temperature":
  0.0, "avg_logprob": -0.2411188013413373, "compression_ratio": 1.5023474178403755,
  "no_speech_prob": 0.007671094965189695}, {"id": 1053, "seek": 661744, "start": 6624.32,
  "end": 6628.719999999999, "text": " Thanks so much. I will try to publish this podcast
  before May 5th.", "tokens": [50708, 2561, 370, 709, 13, 286, 486, 853, 281, 11374,
  341, 7367, 949, 1891, 1025, 392, 13, 50928], "temperature": 0.0, "avg_logprob":
  -0.2411188013413373, "compression_ratio": 1.5023474178403755, "no_speech_prob":
  0.007671094965189695}, {"id": 1054, "seek": 661744, "start": 6630.5599999999995,
  "end": 6636.24, "text": " So make sure that somebody can join and get chappin, of
  course, we can do the", "tokens": [51020, 407, 652, 988, 300, 2618, 393, 3917, 293,
  483, 417, 1746, 259, 11, 295, 1164, 11, 321, 393, 360, 264, 51304], "temperature":
  0.0, "avg_logprob": -0.2411188013413373, "compression_ratio": 1.5023474178403755,
  "no_speech_prob": 0.007671094965189695}, {"id": 1055, "seek": 661744, "start": 6636.24,
  "end": 6644.4, "text": " the most media, social media push. This is amazing. Thanks
  so much, Max. I''ve enjoyed this", "tokens": [51304, 264, 881, 3021, 11, 2093, 3021,
  2944, 13, 639, 307, 2243, 13, 2561, 370, 709, 11, 7402, 13, 286, 600, 4626, 341,
  51712], "temperature": 0.0, "avg_logprob": -0.2411188013413373, "compression_ratio":
  1.5023474178403755, "no_speech_prob": 0.007671094965189695}, {"id": 1056, "seek":
  664440, "start": 6644.4, "end": 6654.24, "text": " conversation thoroughly. We went
  into depth and with and everything all dimensions. It''s a multi-dimensional", "tokens":
  [50364, 3761, 17987, 13, 492, 1437, 666, 7161, 293, 365, 293, 1203, 439, 12819,
  13, 467, 311, 257, 4825, 12, 18759, 50856], "temperature": 0.0, "avg_logprob": -0.1875454818501192,
  "compression_ratio": 1.5172413793103448, "no_speech_prob": 0.02902468480169773},
  {"id": 1057, "seek": 664440, "start": 6654.24, "end": 6662.0, "text": " conversation.
  So thanks so much and keep it up and I''m curious to hear news about Mighty and
  the", "tokens": [50856, 3761, 13, 407, 3231, 370, 709, 293, 1066, 309, 493, 293,
  286, 478, 6369, 281, 1568, 2583, 466, 45874, 293, 264, 51244], "temperature": 0.0,
  "avg_logprob": -0.1875454818501192, "compression_ratio": 1.5172413793103448, "no_speech_prob":
  0.02902468480169773}, {"id": 1058, "seek": 664440, "start": 6662.0, "end": 6669.12,
  "text": " tooling around it and also looking forward to your building buzzwords
  presentation. Yeah, thank you so", "tokens": [51244, 46593, 926, 309, 293, 611,
  1237, 2128, 281, 428, 2390, 13036, 13832, 5860, 13, 865, 11, 1309, 291, 370, 51600],
  "temperature": 0.0, "avg_logprob": -0.1875454818501192, "compression_ratio": 1.5172413793103448,
  "no_speech_prob": 0.02902468480169773}, {"id": 1059, "seek": 666912, "start": 6669.12,
  "end": 6679.44, "text": " much, Dima. It''s great to chat. Yeah, thank you, Max.
  Cheers. Cheers. Take care. Bye-bye.", "tokens": [50364, 709, 11, 413, 4775, 13,
  467, 311, 869, 281, 5081, 13, 865, 11, 1309, 291, 11, 7402, 13, 13006, 13, 13006,
  13, 3664, 1127, 13, 4621, 12, 6650, 13, 50880], "temperature": 0.0, "avg_logprob":
  -0.31698110699653625, "compression_ratio": 1.0348837209302326, "no_speech_prob":
  0.038853757083415985}]'
---

Hello, vector podcast is here. And today I'm going to be talking to Max Irwin. He's this star in the search engine business in search engine world. He has been doubling also in NLP a lot. I don't know 20 years. It's huge amount of time.
And I mean, he has been consulting in this space, also building products. And now he's focusing on building his new product. And he's the founder of company called max.io, which is also a website. You can go check it out. And he's building a mighty inference server.
And the number of other tools that I'm sure Max will talk about today. Hey, Max, how are you doing? I'm doing great. How are you? I'm great. And thanks so much for joining me today. I'm very happy to be talking to you today. I'm very happy to be talking to you today.
I'm very happy to be talking to you today. I'm very happy to be talking to you today. And I'm learning about my tea and all the things that you're cooking there. But I think as a tradition, could you start with introducing yourself first? Sure. Yeah. Hi. So I'm good to go on my own business.
I'm good to go on my own business. So I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. I'm a doctor. And sometimes I get a lot of things to do with my career.
In fact, when I was a younger, I didn't do so well in my language course. started in 2015-2016 with actual product development around NLP. With search, I've been doing search since about 2010-2011.
Again, it's fuzzy when I actually first started, but I think the first real serious thing I did with search was when I went to take my first solar training course, which was one of the, when Lucid Works still had solar training and they had contractors coming to give training.
So that was, that was in 2012, but I'd been messing around with engines before that. And I started on an engine called DT Search, which was the C++ closed source engine, but you could buy the code for like a thousand dollars a year.
So the company I was working for, MetiRex, we actually bought the code. And I was, I was the newbie with search. I mean, we had guys been working with it for a while. And they'd built a whole platform around DT Search. And then I was starting to show its age. So we started shifting over to solar.
But yeah, since I started that, but well, before that, I did a little bunch of computer programs. So like the 20 years, 22 years-ish stuff that's in my bio, like I've been, I graduated university in the year 2000, and I've been, you know, working professionally software ever since.
But with Search, I, I really got interested in in Search around 2012, is when I really said, wow, this is amazing. This is so much different from what I've been doing before. So that's when I really do have had first into into the problem space in the domain. Yeah.
And some people say that many of us ended up in Search field by accident, as well as actually NLP. I've been talking to one professor here in the University of Helsinki has built machine translation team, very, very strong one. And, and he has built the, the system called Opus.
And, and, and he actually said that he ended up in NLP also by accident because it was just an offer from a professor and he decided to take it and he turned out to be quite good at it, you know.
But he also had another option just to go and work in in Germany, he's from Germany, to work in Germany in some company, database company. And, and, and likely he didn't take that path.
How was it for you? How do you feel about yourself and then ending up in the in the in this space? That's a great question. It's interesting. I feel like ending it up, I, it was definitely somewhat accidental.
I found, I, I had the pleasure of meeting so many people in search through my different positions that I was working with and the varying degrees of expertise.
I found that a lot of people who got involved with machine learning found out about search because TFI, DF and all that stuff is like an algorithm and it's like, oh, there's this whole language problem behind search, so we have to figure out.
And then the search people get involved in machine learning because, oh, this language problem is horrible. How do we solve it with automation and learning? So I, I accidentally stumbled on it because I took, it was a, it was a role that was in like healthcare compliance.
And I was interested in that domain specifically and search just happened to be a really important problem in that space. So that's how I kind of got into the, the technical domain of search.
And it just was so much more fascinating than like the stuff that I was used to with, crud, you know, just create read update delete and just workflow applications, which I'd been doing for, you know, 10 to 12 years at that point. Yeah.
Yeah, I mean, for me, like searching, you know, like, I think I started 2002, 2003 academically, but then it was like seven years past and I still couldn't find a niche or a job for myself because there haven't been then many search companies in Finland actually at that point.
And then I found a company which I joined in 2010, AlfaSense. And it was Apache Solar, you see in everything new, but it was still somehow inviting.
And I think the first time when I, when I've built the backend and I was like, okay, somebody is going to use this, somebody is going to type the queries and we'll try to find information. So I also tried it out and kind of like maybe work, maybe didn't, I wasn't the, the, the user of this system.
I didn't know what to type. So I was just grabbing some phrases from the documents and see, okay, does it find or not, you know? So is this something that also like attracted you like, okay, findability, right? Like discovery or maybe discovery is the next stage, but even the findability itself.
Yeah, I guess search was really my first step towards working with real complex data that wasn't so unstructured, unstructured data, right? You kind of, you kind of reach a limit with structured data at some point of getting stuff into databases, getting it out and things like that.
And you can, you can spend a lifetime in that work. But I felt like I'd been doing it for a while. And with, with search, it was like this, this weird world where it's like all this unknown stuff and you don't know what to do. So it's this unsolved problem.
I felt like databases and things like that were like this solved problem, where search, search wasn't a solved problem and still isn't. Now with the work, if I had been doing the same database work, that's all no code right now. You can just create the same stuff I was doing with no code tools.
You don't even have to be a programmer if you don't want to with the level that we were doing it, you know, in the mid 2000s. So, yeah, now it is. And it's still, it's still unsolved. Even when we start talking, you know, we're going to talk about vectors, of course, but vector search.
But that's still an unsolved problem. It's like another tool, but you still have all these issues that you have to take into account. Yeah. So endless exploration. Yeah, it's like infinite quest in many ways. There is like a limitless amount of tasks to solve.
But then, so somehow in your career, there was a turn that you decided to get closer to this vector search field.
I just wanted to hear your kind of first reaction, like what did you think about it? When did you hear about it? And also, what attracted you?
I'd say the first thing that really attracted me towards vector search was the birth paper that was written in 2018, but I didn't I didn't come across it until 2019.
And Google had written a blog about how they were using it for their for their web search. And you know, you could download some Python and get this stuff to work. But the reason why I was so fascinated by that is because of you know, working in search already six years. No, let's do some math.
So, you know, eight years at that point, I had been stumbling along with the vocabulary problem.
The query term dependence problem, as we call it, where, okay, well, to solve this, you have to create a bunch of synonyms and then you get to a certain level of advancement and then you create a taxonomy and then you know, you created a knowledge graph.
And you know, before before birth, we'd started playing around with word to veck and saying, oh, can you know, can these type of embeddings be used to solve this whack-able problem with synonyms and knowledge graph vocabulary expansion? The answer turned out to be no with word to veck.
It didn't work as well as we'd hoped. It helped with some things, but not, but it harmed with others. So it produced a lot of noise and and you know, maybe we didn't give it a good enough chance, but we saw, okay, we can train this thing pretty quick and we can get this model from our content.
But there's still this problem.
 So when I started to play around with some of the Python tools that were available for for Bert and large language networks, which actually used word to veck as the pre-processing step to get the first to get the first encodings and then with first embeddings and then use those identifiers to go forward.
I really saw something there. I saw actual similarity where I didn't, I just saw kind of co-occurrence with word to veck before. Yeah, these things are, you see them in the same context.
But with actual linguistic similarity, the first time I saw that was with Bert and that's where all the hype came from. And then the next step with Bert is like, okay, I have these vectors.
Now what do I do with them? And then I said, okay, well, I have to use a dot product, right? I have to use a cosine similarity. Okay, let me just do that. And then I say, oh, you can't just do that across every vector. It's impossible. You have to do something else.
And then you go on this learning path, right? So that's where I ended up. And I had actually written a blog post in 2019, you know, about, and I think that post was, you know, widely accepted by community, it's still in the open source connections blog.
And it was really, it was really showing like, hey, this is, this is a change, you know, it's not just Google that's going to be doing this. Like, this is really interesting. And a lot of people agreed and there's, there was like this movement that kind of happened after that.
And a lot of other people were coming to the same conclusions, but there were a lot of challenges. So with vector search and approximate nearest neighbor search, you know, that's, it would, that's just the tool to solve the problem.
It's like, you know, you start with this problem over here, and then you go like 10 steps over here, and finally, you get to vector searching. Okay, this is, this is a potential solution, right? This is the core of the potential solution with all this stuff in the middle.
Yeah, but have you felt that I should read this blog and we'll definitely link it in the show notes. But sometimes when I look at vector search, let's say demos or applications or algorithms, I get a feeling that you might just think, okay, I have a solution. Let me find a problem.
Because it's, it's all semitical. I mean, it's so sexy, right? Do you, do you think this is one of the sort of misconceptions, you know, in this field, or do you think that it's well-past that already? That's a great question. I don't know if, I don't think it's a solution looking for a problem.
I don't think that's true. I think there, it actually does solve some problems. But I do agree that it gets, you know, there's a lot of gray area.
And how do you arrive at that from, I need to find things as a person? You know, and all the things that you have to go through until vector search actually means something that is a solution.
I think there's, there's a lot of people who picked it up and say, okay, we could just use this and it's going to solve, solve these problems.
But it doesn't do that, right? Because search is not just about similarity, you know, you can express a query similarity with a document using TFI DFBM25, you know, the sentence transformer, you know, cosine distance, whatever. But that's only the similarity.
There's also like the, the need that the person has to what they have. So it's, it's a bunch of candidate documents that are similar, but what's the actual document you need? So that's where a lot of other things come into play.
 It's just one piece in a much larger search or recommendations platform, you know, you still have to take on all the other signals and, you know, common now in the, in the more mature platforms is, you know, you have some learning to rank algorithm that takes, you know, me and Vector similarity is one, is one feature in, in a learning to rank model.
Along with, you know, BM25 with the title, BM25 with the body, you know, the number of clicks, the date, all this other stuff. And it's, it's a piece.
But the thing that the piece solves is that query term dependence problem, whereas like I don't have to, in a, in a, sometimes, you know, I don't have to go in and, and craft synonyms by hand, and I don't have this endless task of doing that.
You just, you kind of have all these other tasks that you still have to do, but that one maybe has kept it bay a little bit. Yeah, yeah, absolutely.
 I mean, maybe I can a little bit like, restate my question, or sort of like, clarify what I meant, I guess, when you read, I think when you read the paper, like, birth or similar papers, they also say, hey, we, we ran down this on downstream task, like sentiment analysis, we also did question answering, we did recommendation, all these other things.
And it works great. Which kind of like pushes you to think in the direction that is this a universal language model or approach that I can now take and apply to everywhere, every task.
And the answer is actually no, because, hey, I mean, if you are in healthcare and they trained on news, it's not going to work. So the vocabulary still was not excluded from this journey. So if it's mismatch, it's mismatch.
But the model itself, of course, is a clever piece of, you know, attack, which you can then take and kind of apply fine tune, maybe, or retrain on your data.
So I think that that's, that's one way to look at it, right? It is, but I think that we, we see a huge, still a huge gap in the domain, right? I think there are a lot of organizations that can just make use of retrain models and fine tune them.
But, you know, we, I know that there are still domains that you can't do that. Like, if you go up and you try, you know, something that's fine tuned, like law, right? Law is like its own language. I wouldn't even, like law written in English, I wouldn't even call that English.
I'd call that, you know, legal English, right? Because just the structure, the vocabulary, the grammar, all this stuff is so different than what's in like a Wikipedia article or in the news or something like that, right?
So, when you try to do a fine tuning on a pretrained model that's trained on, you know, let's say like onto notice 5, which is a bunch of collections of like, you know, news, Wikipedia, like general knowledge that most people use.
When you find tune it, there's still a gap. There's, there's something missing, right? Because the original trained model was lacking this context. And that's, that's only for the content also. That's just, that's just the content.
And when people search and they type in terms, you know, you can imagine like this, this Venn diagram of like, well, here's, here's all of the content over here that you've trained on.
And then here's all the terms that your people, that the users know, right? And you try to like bring these closer together somehow, right? If the model was trained on content that is like up here, then you're going to have trouble like kind of putting it together.
I don't know if you can do a good job in my hands showing this, but no, you're doing perfect job there. So I think that one of the one of the big existing problems is pre-training still costs like a ridiculous amount of money and is out of the reach of most teams.
Yeah, I've read, I've read papers, you know, one of them was by Microsoft showing like, if you, you know, the bird vocabulary is like 30,000 words or something like that. If you increase the vocabulary size to like 100,000 words, then the model generalizes much better.
And you, of course, you expand the content and the domains that are involved in that training. So I think you, I think we're going to see some more of that.
The world is still stuck on this 30,000 terms in the pre-trained space of things like onto notes because it's just so expensive, it's train models and Google and Microsoft and Facebook and these companies that train models, they're not going to bother open sourcing those.
Maybe they will at some point, but I think we're going to need to see big companies that are specific in that domain, train those models and then open sourcing them.
But if you spend millions of dollars to train a model and you're a big private company, are you going to open sourcing the model weights? Probably not, you're going to keep it for yourself because that's huge value, it's huge value for your product.
I guess you open sourced the idea sort of if you publish, okay, here's the bird model, here's the mom model or whatever. But then go train it yourself. Yeah, yeah, if you have a couple million dollars lying around.
Yeah, and then I was also talking to in another episode, I mean, Ahmaad, who used to work at Google, and he said that entire teams would be dedicated on a quarterly basis to do the expensive fine-tuning work with burrito similar models.
So can you imagine that it's like a team's effort and this people, some of them invented the model, some of them didn't, but you know, with all the resources that Google has to fine tune them for three months. So I don't think this is out of reach of startups.
And I mean, there are other things that are out of reach, like, and this is where you saw the gap with MITI, I want to get closer to the MITI now. So there is, you know, every time I install a vector database, I'm not going to name one. And it says, hey, you know, it will be faster if you use GPUs.
And I'm like, okay, I'm a startup. I don't have GPUs.
You know, so this is, I think one of the gaps that you saw with MITI, but are there other gaps that you saw that you are addressing with MITI server? Yes, so the NLP world right now, and the vector world right now, they all they talk about is Python, Python, Python, Python, everything is in Python.
When you get to production, you use something else, but it's Python, Python, Python. So I wanted to, I came from a non-Python background. I started with C, Pascal when I was really young and then my seed programming is terrible, I'm sure.
Then I discovered, you know, intermediate, intermediately compiled languages, Java, C sharp, things like that. And that was like early 2000s for me. And I kind of went, I was in the Microsoft world, so I was doing C sharp for a while.
And then I found, and all the while I've been doing Java script because of, you know, I was involved in the web, so in the mid 90s, and that's how I got involved with content and content data and all this stuff. It's just all web stuff.
And then you got to know JavaScript if you do anything with the web. So it was like C sharp and JavaScript for me for a while. So I know that there's a gap. If you go and if you go and you go into the JavaScript world, the node, or, you know, TypeScript or those things, Dino now, there's nothing.
You want to do NLP? Learn Python. That's pretty much the suggestion. Same with C sharp, you know. Okay, well, there's there's some libraries out there, but they're clunky.
Nobody really, you know, Microsoft probably uses them, right? Because they're Microsoft and they built C sharp and everybody's doing Microsoft stuff.
But, you know, outside of outside of Microsoft, like who's using C sharp for for natural language process to train models? No, but, and to host models, you know, okay, well, to do it, you have to jump through all these hoops. And it's really hard.
So unless you want to like put Python in your stack, which is basically a non-starter for a lot of teams. A lot of teams, they work in languages like node, JavaScript, C sharp, Java, Ruby, Go. Like there's so many huge languages out there that just can't touch these models.
So I wanted something that kind of broke out of this shell, this Python, this Python like enclosure of like how do you get this stuff into the hands of other people just want to build web applications. They don't want to go and, you know, go into the Python family.
So that was that was one of the one of the starting catalysts from from Mighty InfraServer.
I, I there are there is one tool that I have to use that is Python because it has to you have to convert a model and I convert the model to Onyx, which is most people know about Onyx if you're in the NLP world by now, which is it's ONNX, that's for an open neural network exchange.
And is this intermediary format that can be used generically. It's like an open model format. Now there are runtimes that you can take Onyx and Onyx models and run them. So the biggest, the biggest one is Onyx runtime and that's developed by Microsoft, it's open source.
I see licensed and that's written in C++. But there are bindings for other languages and community contributes bindings. So you can use Onyx runtime in Python if you want to.
You can, and you'll get like for those Python people who want to host models in Python, just convert your model to Onyx and host it in a Python Onyx runtime. It'll double the speed of the model inference, like out of the box. You don't have to do anything. You press like a button.
You don't, you clone the repo, you press a button, then twice, twice as fast. But for others, you know, there's binding for C sharp, there's bindings for Java, there's, there might be bindings for Ruby. I haven't looked probably bindings for go.
And even if Microsoft doesn't support them, the community builds them. So you can do this, but there's this other problem that you have. The other problem is that, well, those are just the model weights.
And if you're talking about, and hosting the runtime for the model weights, so you put in inputs and you get outputs. But where do you get the inputs from? Well, you have to tokenize text, you have to do all the stuff to prepare it to pre-process it.
And then when you tokenize and you do pre-processing, then you can pass in those, the tokenized data as inputs. But all the tokenizers are written in Python. So now you have to, now you have that problem.
So I actually used Rust for mighty inference server because hugging face based their tokenizer, their fast tokenizers on Rust, they wrote it in Rust, and they offer bindings for Python. So if you, if you install a fast tokenizer in Python, you're actually using Rust bindings for that.
So I wrote a web server that wraps the Rust tokenizers and on X Run time. And I wrote a whole bunch of code for pipeline specific stuff like question answering, sentence transformers, sequence classification, which is like sentiment analysis token classifications. That's like, entity recognition.
And I'm working on others also, but it's so much faster, it's so much faster than Python, like it's not even close. It's probably like three or four times as fast without any fine tuning of it. And I've gone through fine tuning.
So I haven't compared it to Python in a long time, but I might be like five times as fast as Python right now on CPU. You can also use GPU if you want. And it's, you maintain the same, the same speed. It's just as fast. Yeah.
Well, it's just as fast as the, the ratio of speed is like the, you know, if you took the model and Python and you put it in a GPU versus you take the model and on X Run time, you put it in the GPU, you get it's far faster.
And you say like when you said bindings in other languages, you know, like Java C sharp. So if my stack is in Java, I can take this model and kind of plug it in into my Java code.
You can take a, you can take a, let's take a hugging face model, for example, like just let's say brick based on case, you know, most people know that one. Brat based on case, you can export that to Onyx with hugging face code in Python. And you have now you have an Onyx model.
Now you can, in Java, you can stand up a class that wraps the Onyx runtime and you, and you load the model into memory with on X run time in your class.
And then you can create methods around that class, right? And then you can call, you can call it and you can say, I'm going to pass in the inputs and I'm going to get out. And that's all in Java now.
Well, with the C++ wrapper for Onyx runtime, of course, but the connect, but to wrap that C++ runtime, there have to be bindings between the language. So Java has to have some application interface to talk to C++. Yeah, which is GNI, right? Java native interface, I think. Yeah, I think so. Java.
Yeah. So that part, like having Java talk to Onyx runtime is taken care of already. You still have to write all the other stuff around it, like to you to leverage it. But that's, you know, where programmers used to that sort of thing. You know, Java, you can, you can do that.
And I think, I don't know if it's, I don't know how much we've seen it, but Jeff Zemorek, who works at open source connections, I know that is like he was working on a project where he, you know, he could try to load an Onyx runtime in open, in open NLP, which is a Java program.
So trying to get an Onyx model in open NLP. And I think he succeeded. I haven't seen code for that. Yeah. Yeah. But that's what I'm exactly. Yeah, that's, that's awesome.
So I mean, the reason I'm asking is because I witnessed this tectonic shift in in my previous company where we had the entire stack in Java. Even though we started with Pearl, but we had to read right everything into Java, just didn't scale on Pearl.
And, yeah, and I mean, we had Apache Solar on one end as the open source search engine also written in Java. And, you know, when we would customize it, we would write plugins in Java and so on. But then, when we wanted to introduce AI into the pipeline, of course, everything was in Python.
We hired people who could only do Python, nothing else, fresh grads. And, and now you are stuck with this new architecture. Okay, you have Python as one step in the pipeline.
How do you call it? How do you handle errors? How do you scale this thing? Right? And we were also moving to Kubernetes to add to this crazy mix.
And, and what we ended up doing is that we would have a synchronous processor, plugged in in every place where you have Python to abstract Python away from Java. Right? So you would kind of like just say send this message to an SQS queue. And on the other end, there is somebody consuming it.
Can you imagine how scalable this can be? It works. It works. You can also like scale it locally. But as the whole architecture, I don't think it's a very kind of smooth in a way solution, like not to mention that the performance element of it is just not taken care of.
And what you say now, essentially, like with ONX binding in Java, we could just train that model and then export it in ONX format and then use it directly in Java. You can't, yes. But you still have to get the inputs to the model.
So if if it's like an image or something like that, it's usually pretty easy. But if it's text, then you have to tokenize first. And you have to use the right tokenizer. And you have to do, you have to kind of jump through a bunch of hoops to get it to work correctly.
So it's probably a month's worth of work to get a tokenizer working in Java the way you needed to work. Yeah. And maybe you could, in principle, share this tokenizer between tasks, right? So it's for sentiment or for entity recognition in principle, you could use the same tokenizer. Yeah. Right.
So the tokenizer is, so the tokenizer relies on the vocabulary and the configuration, which is bound to the model. So the model is dependent on these things. So if you have a generalized way to load the vocabulary and the configuration, then yes, you could just take the thing and your new stack.
But having said all this with MITY, you took a different, you know, approach, like the philosophy behind MIT, you'll offer it as a web server, right? Yeah. And again, can you tell me more about it? I mean, I'm sure you can open a lot of detail.
Yeah, the reason I went that route is because when you, when you want to do model inference, you want to give it as much compute as possible, right? And you kind of want it to be its own thing. So I went the microservice route.
I'm not, I'm not saying microservices are the way of the future and they're better than model it's and all this stuff. But the idea of coupling with this, you know, this model inference is part of like your regular application code.
Maybe you don't want to do that, you know, you want to have this other service that can, and this is part of like the bigger ML ops question, which is, well, how often should I update models?
What are the things that I just know about, you know, drift and all these things that are like, what about logging and all this stuff? It's like, well, okay, you need a way to do this.
And if you embed model inference in your own code, now you're also responsible for all this stuff, right? So as a, as a microservice, you can evolve that microservice and say, all right, this thing is responsible for model inference and that's it, right?
And then all the side effects around that of like, okay, well, you need a new model, but if you have to AB test models, what if you want to do logging, what if you want to do all these other things? You can evolve that in its own way and it's in the separation of concerns makes much more sense.
So, and then it kind of gets you out of the, it gets you out of the problem of like, okay, well, am I going to build a mighty for Ruby? Am I going to build mighty for node? Am I going to build ready mighty for go? Like, I don't have to do that.
I can just build mighty inference server as a web server or a GRPC, which own, you know, it's on, it's on the roadmap. I don't know how long that's going to take, but now you have this thing. And then I just have to write client libraries. And the APIs always the same.
The client libraries for HTTP are super easy. So yeah. And if you compare this, let's say we take a database, like VV8 or SBA, they have inference inside them, right? So like, if you already bought into that solution, in principle, you could do this.
The only caveat I think is that if you have your custom model, you'll have to go an extra mile to actually integrate it inside this database, right? And at that point, with VV8, I think you will have to master go with SBA, you'll have to master the C plus plus or Java. I'm not sure.
I'm not an expert in that, but there is a podcast with Joe Bergum that you can check out. But yes, so how would you kind of like on product side, how would you compare mititude that approach? So VESPA uses on X-Rontane. VESPA wraps on X-Rontane. I believe it's on X-Rontane.
I know they use on X models. I don't know how to present it on X-Rontane. So you'd still have to go through the step of doing that. With VV8, it's a little bit different. With VV8, you have these things called modules. And then the modules are typically like Docker containers with APIs exposed.
And then there's logic written in the module code for VV8 that will wrap that API. And it's easier if you just copy and paste a model and then change stuff to match the API of the thing that you have in a Docker container. So it's not that much work. You still have to know go to do it.
 And yeah, I think the other problem that I have with that approach, and I'm not saying it's wrong, but from my perspective, so if you look at the documentation actually for a couple of vector search engines, I'm not sure of VESPA, but I think VV8 and maybe another will say, OK, well, it's better to use a GPU for inference and then CPU for the vector search, right?
Because you want to provide as many workers to the search algorithm as possible.
And you don't want the inference, the model inference, and the vector search fighting for resources.
Because both are very expensive, right? So they say, hey, if you have GPU, then all your model inferences and GPU and your vector search is all CPU and you get this one perfect box and everything just works.
But OK, well, what if you want to scale beyond that? You can only send so many documents into a GPU at a time.
What if I need 12 machines? Well, now I need 12 machines that are all hosting VV8 and they're all hosting mighty or whatever your inference solution is, all it wants, right? So this goes back to the separation of concerns, problems.
Like, well, what if I have a lot of documents that I need to process? And it doesn't take that long to get them into the vector search by the vectors, but processing those documents takes a long time. So I have to pre-process.
Well, now you've kind of got like this situation where you might need another solution to do this batch pre-processing, right? In another place. And then you bypass the module when you integrate into VV8. You just want to send the vectors directly to VV8 so you don't have any inference.
You send the vector to it. So, again, it's like this. I'm not saying it's wrong. I think it's a great idea because you can just install something that will just work, right? You don't have to install like three different things and try to figure it all out.
So I think that getting up to speed on that is probably quick. But in the long term, like the scalability overall, I think that you now have this coupling and it's a bit of a challenge. So I don't know how that gets resolved.
Yeah, that's actually a good point because you reminded me of, I don't remember precisely what we were sort of balancing between, but like with solar and a Java pipeline in front of it.
So the pipeline would process documents as they come in, you know, chunk them, classify them, run sentiment analysis on them and so on. We were thinking, okay, some of these things could be computed inside solar.
Like we could write some clever plugin which actually does, I mean, solar has a lot of things there, you know, like before it indexes the document, you can run like a ton of things. I think OpenNLP is one example, right? You could plug in and it runs something there.
And I remember that my manager, like who was a VP of engineering, he came and said, hey, what if we lose solar? So we computed everything inside solar, stored it and lost it.
Then what? Like now you need to bring it up back really quickly and usually what you want to do is probably like replicate some shard and off you go, right? But if you don't have that data, you need to recompute it now. So you don't have any intermediate storage. Solar is not the storage.
Solar is the database. And so we backtracked and we said, okay, we will compute everything and store it in S3, you know, in file storage. And if in the event of losing solar, we will restore it and reindex everything on the fly.
So I mean, that kind of also like, you know, resurrected that situation that also be deviated or quadrant to any other database. If you lose the fact, if you lose the database, you lose the vectors.
So if you have computed them inside the database, now bringing it back and then turning it on and say, hey, please compute my vectors again, please, please, please, you know, just too much time. You're exactly right. And this is a lesson that I learned.
I didn't learn this lesson the hard way, thankfully. But this is just a lesson I learned picking stuff up when I was at, when I was at Walter's Clure, which is a huge publishing firm. And you have, you have your content, which is like editorial content, primary source content.
And it's, it's written in such a way where it's it's pretty raw from a machine perspective, you know. And then it goes through a series of enrichments and transformations. So eventually it reaches the search engine.
But every step along the way, it's like, okay, well, we need to add topics to classify topics, right? So I'm going to add the topics.
And then I'm going to save that state that's now on disk somewhere back to, okay, well, now I have to, you know, add this other thing, you know, do any recognition or something. That's also saved, right? So you have all these intermediate steps. So if you lose anything, it's really easy.
You don't have to rerun the entire, you have to rerun the entire pipeline. It takes you months to do that. Not just days, but like literally months to start from scratch with content. So that's like a disastrous scenario.
So this lesson that you learn is, okay, well, yeah, you don't do, you don't do everything all in one place. Because if you lose it, then it's all gone. You have to start from scratch. So yeah, separating concerns in that way.
And then the idea of, well, you can plug this thing in anywhere along the chain now, you know, you have this, you have a microservice, you can put it in, you can put it anywhere.
And then you can, you don't even have to just take the vectors and then stick them in the search engine, right? But what if you want, what if you need the vectors and you want to do something else?
What if you have like a recommendations platform and you have this other system over here and you want to do this other stuff? It's like, well, now you have to think about routing and all these other things.
But if you just have an easy way to get vectors, you know, plug it anywhere along the stack, then that's up to you. You know, there's no prescribed way of doing things. It's a Lego. You put the Lego wherever you want.
Yeah, that's a great point because we also implemented like an algorithm, which was it computing some topics, I think. And we used fast text and work to back vectors. But we didn't need the vectors in the end in the downstream system.
We just computed them, clustered, ran some magic algorithm, you know, produced topics and then you store the topics. So you store actual words in some database, so index them in the search engine. So yeah, you're absolutely right.
Like, sometimes you don't need the vectors, but they are still the medium to get to your target. So, and so, but you've, I've seen the blog posts, which will also link, you've published on marks.io, so discussing sort of almost like a unit, unit economy of this thing.
Like, if I have MIT gazillion amount of servers, how it will play out, you know, how much separation of concern and also resource separation, all these things, and how economical it is in the end.
Is this something that you are proposing? So let's say if somebody takes MIT and wants to scale it, you know, like all of a sudden you get, instead of 10,000 documents, you get 10 million documents to process, right?
Because somebody changed somewhere in the pipeline, and now we need to rerun the whole thing.
So, how would you, what is your recommendation also on the economy side? How do you see MIT playing a role in making this huge thing more economical?
So, the first thing, the first thing that I see is that you can, you can calculate the cost ahead of time, because it's absolutely linearly scalable, right? You take, so MIT itself sits on one CPU, right?
It sits on one thread, I'll even say a thread, because these days you have cores and CPUs and threads and it gets messed up.
 You can tell MIT to use multiple threads in certain situations that you want to, but the example for bash processing that I use, which I actually learned from the VESPITE because they wrote an amazing blog post in, I think it was early January, they released a blog post talking about this exact problem of, you know, do you have one process across multiple threads?
Do you have multiple processes? So, if you go with the multiple processes route, let's say I take, I take a bunch of documents and I pass them in and I have some level of consistency in the document size, which you usually do.
Pass them in and it takes you X as long, it takes you X to get all of your documents, inference, right? So, you have that number and you know how long it took and you know how much, how much content you processed in terms of bytes.
Well, what if I, if I add, if I add another process now and I'm doing this purely paralyzeable, so half of my documents go here, half of my documents go there, it's what I said exactly is linearly scalable. I add a CPU, it has the time, right? It has the time that it takes to do this.
So, if I have a situation where I've said, okay, I did 10,000 documents, it took me X, now I have to do a million documents.
How long do I want it to take? You can actually write down the calculation and say, I need, I need this exact infrastructure, which is a huge problem right now, a lot of people don't know that. It's like, okay, let's just add a lot of GPUs and see what happens, you know.
You can, you can spend the time to go through and do that calculation, but it's not so straightforward. And you'd have to do it like, you'd have to cost it yourself.
I haven't released it, but I want to have a calculator that says, how many bytes do you have and, you know, how long do you want to spend? And I can say, well, it'll cost you this in Amazon or whatever. So, that's, that's one thing.
I also want it so, I mentioned GPUs, it's like, this is, I built it so it works on CPU.
If you are a company that's getting into this stuff and this, this, this idea of the unit economy, like, how long does it take to process something? And what's the cost and, you know, how do I scale it? But the, the, the, the billion documents.
If I'm coming into this ecosystem and content processing, and I'm used to working in Java or, you know, C sharp or something like that. Now you're telling me I need to buy GPUs, like I have to run GPUs, and then I go check the prices, I'm like, well, that's not how much we spend on infrastructure.
That's not in our budget. I'm sorry to tell you. So maybe we can't even do this. So I wanted to have a way where you could get around that problem where you could just use CPU and it's a straightforward understanding of the cost that you'd have to put in.
I haven't checked Amazon, I haven't checked Amazon prices in a little while, but I might as well be posted online, which is, which is another cloud platform.
I just, the pricing is better and I just, like, they were actually recently purchased by a huge content, management system, uh, it starts with an, I forget the name, whatever. Anyway, I use line-out and it's, uh, it's, it's cheap for CPUs.
Like, it's great, but you want to, you want to run a GPU, it's like $500 a month or $1,000 a month. And that's a lot of money for one machine, and most teams are not willing to spend that.
If you want to do fractional, you know, on AWS is probably for actionable GPUs, I think, but it's still expensive. And now you're, now, it's like this cost that never goes away. Like, once you do it, it's like, well, it's there, it's there for a long time, you know, CPUs are a commodity.
Um, GPUs, you have to fight with the, with the cryptocurrency crowd for the costs, all this stuff. So, yes, CPUs the way to go. I can imagine that GPUs can be used during the model training or fine tuning, but during serving, that sounds way too expensive. Right.
Yeah, yeah, that makes a lot of sense.
 And, um, and so, now when you offer my, how exactly you offer it, it's, it's a binary package, right, uh, that I can install and, and, and basically run on my, on my system, and I can decide whether it will be like, a standalone kind of script or it will be a pod in Kubernetes or Docker image and some other non Kubernetes.
Um, so is that right? That's right. It's, it's a very small executable. Um, it's, it's so Linux is a first class citizen. Um, Windows is, it'll run on Windows.
It'll run on Mac, but I've heard people running it on Mac M1, but they had to like do a lot of stuff to like fix dependencies and it wasn't really working that well.
And I think what, what's it called Rosetta or something? I think it's still using that like to, to do the X86 like bridge, like the translation, visualization. Um, so Mac M1, it's not, uh, I wouldn't consider it working. I've also seen some other problems on, on Mac that I'm trying to resolve.
It works fine, works on my machine, right, that, that type of thing, but really it's meant to be running links. Um, you can run it in Docker. It's really easy to get started in Docker.
Uh, so you can download the executable and run it on your Mac, um, or you can just download the Docker and use that, which is probably a little bit more straightforward. Um, then you don't have to worry about other dependencies.
Uh, with Linux, I don't, if you're running it on, uh, on Linux machines, you can use the Docker if you're doing like Kubernetes and that stuff. Great. Run it in Docker. Um, just make sure that you sort out like in your pod or whatever, like how much compute you're actually giving it.
Um, because model inference doesn't, it's not just a mighty. It's like all model inference is really, really heavy. It's really expensive. It wants a lot of, wants a lot of compute, not so much memory, but compute. So just be sure to give it enough, um, to satisfy your needs and do time.
I haven't done Kubernetes test myself. Uh, but I like to run, I'm, I'm old school. Like this whole Docker thing. Yeah. Okay. I'll, uh, I'll make a Docker file. Sure. You can use it in Docker. Um, it's on the Docker hub. Uh, but I like to just install stuff. The old fashioned way.
Uh, in Ubuntu, I just, you know, download the download the thing. It's a tarball and you, you know, it's at the tarball and you're good to go. Uh, and, uh, the way you start it is actually, it's a, it's a rest program with a, with a library dependency, which is on extra one time.
Um, because it's dynamically linked. It's not statically linked. But, uh, to start it, you can either start one core or you specify the model. Or there's a thing that says it's called mighty cluster. It's just a back script, back script.
And it'll look and check how many cores you have on the machine and it'll start a process for every core that you have. So it does this work. Um, and it takes like less than half a second for each quarter startup. It is, I, I actually put that in on purpose.
That's a limit I put in to slow it down a little bit. So it didn't let go off the rails. Um, but you could probably take that limit off. You could just go and modify the bash script and, uh, and see how, see how quickly it'll start up.
So I, so that blog post that you mentioned before, um, like I rented on 128 cores. So it would take like, I actually took the rails off and let it start up really quickly. Um, but it can take, it can take a moment to start it up on every single core. Uh, and, yeah, you you could do it in Docker.
You could do it bare metal. Um, if there's any people out there using windows, I'd love to hear from you. Um, I've heard some feedback from Mac and Linux, but I haven't gotten any windows feedback. So I don't even know if it's worth building it for windows these days. Maybe not.
Yeah, I think it depends. If I don't know what should be this scenario is like you are a developer on windows.
And for some reason, you don't go on your server side to like you, we still want to develop everything locally, right? So you want to bring up, I saw such guys actually in my team, they wanted to bring every single server service on their laptop. Yeah. And that's how they developed.
They didn't want to depend on any external connection. Right. Even, even Docker is like a pain in windows these days sometimes, right? So I know that I know the windows ecosystem, because I used to, I used to be in in the 2000s. That's the, that's the mindset.
It's like I'm just going to run everything natively in windows. Yeah. And like when I tried mighty on on Mac, I think it took like some seconds to boot, but the moment it booted, I was like shooting some queries and like to compute the vectors and it was insanely fast.
Is it only on a secret source in this insane fastness? I mean, if you're used to running models and Python, it'll seem insanely fast. A lot of it is on. That's they get most of the credit there. Yes.
But there's a lot of other stuff that goes into it, which is like the tokenization and the pre processing and the post processing is just, it's fast is I've been using Rust for it and Rust is a, Rust is a really interesting language. It's it's gotten me back into systems programming.
I'm not here to say that like Rust is like the most amazing thing ever. There are things I love about it, the things that are like, I don't know if I would do that way, but you're supposed to do things a certain way because the compiler understands that it'll super optimize it for you.
It's hard to, it's hard to wrap your brain around it if you're if you're from a dynamic really typed language like Python or JavaScript. It's hard to get a handle on node. My my compiled background like, you know, typed, typed programming languages compile ahead of time.
I was used to that from my previous life. So I was able to pick it up again and I read the I read I just read the rest book. There's a free book out there. I actually bought the I bought a paperback because I like paperbacks and I like hard covers like actual paper these days.
So I was reading it like that. And just going through the examples took me a couple weeks to get a handle on Rust. That gets a lot of the credit as well, the Rust language. It's just it optimizes and you know, you have to learn this field that I'm in now with model inference.
It's like the super niche field of like you have to understand the hardware and you have to understand the machine learning. And there are those two fields are like so different. There are very few people out there that are really good in both. So I know that there's a word vectorization.
So vectorized on the CPU is like, well, if I have to do a calculation with eight with a byte and you know, I have a register at 64 bits. But I have an eight bit byte like, well, I can vectorize and I can do eight calculations because it's with SIMD, same instruction multiple data.
So that so Rust, if you turn on certain compile flags, it'll do that for you automatically. So you get that speed up. So I turn those knobs all the way up. I said use all the use AVX1 and 2 if the process supports it and most processes do these days if you're on X86. ARM has a different set.
I haven't gotten into the ARM world that I have to get an M1 Mac and I'm going to start messing around with all that. But if you know that stuff and you know how to turn it on, Rust does the rest for you.
You kind of have to write your code a certain way so that, you know, Rust will do the optimization a certain way. You can't think like old school. You have to kind of think in Rust world a little bit.
But doing that, now you get all this extra, all this extra speed from pretty much nothing just from writing your code a certain way turning on a couple of compiled flags. That's why it was so fast.
Yeah, but you still needed to figure all of these out and I remember you were you were saying that you had a bunch of weeks, you know, coding on stuff.
Yeah, you get things done because I know and many of us probably know here in the audience that if you are a programmer, you might say, yeah, I can do it. But you cannot actually estimate when you will be done.
So you get into the weeds and like, oh my god, it just like UTF or something else doesn't work or like, I'm sending a requested fails, whatever, what's going on and you spend so much time or if you're doing an algorithm, that's another story.
That's like an internet journey there, like debugging all these states. And I mean, I'm just trying to say that even though you you make it sound so easy to to master Rust and you know, to go through all these maze and make it the way compiler wants it, it's still time. It's a lot of time.
It's skill. And so you master it. And that's why and in the end, you know, the end result was not given.
You earned it, right? So why not turn this into the business? So now on the business side, I'm thinking, how do you offer Rust? Like, so how do you offer excuse me, mighty? So you have you have the the binary, you have the like the model will be shipped separately somehow outside of binary, right?
But what is a customer I'm paying for? And yeah, and also kind of ahead of time, a question, can you give a discount code for our audience to try it? Oh, that's a great question.
Um, uh, yes. So my business model is, is again, old school, because I've been doing software for a long time. So it's licensed software, right? You pay, you pay a license, you get to use the software. Um, I'm still trying to figure out the exact price point.
Um, some people say, some people say it's too cheap, which is interesting, because I didn't, I didn't think so. Um, some people think I say I should charge more money for it. Uh, it's $99 a month right now. When this podcast is published and after that, it may change.
If you get it, I don't have, it's a light up to strike. I can go in and create a discount code for folks. I don't have a code right now.
But if you, if you email me and you say I heard about you on the vector podcast, um, follow the link in the description, like follow the link in the notes and email, we'll, we'll set something up, um, so you can get a discount. Uh, that's the way it works. But that's, uh, that's for commercial.
So if you're using it commercially, um, and you're making money from it, uh, then, you know, I, I ask you pay a license, please.
If you are a nonprofit charity, um, or just using it, you're a student, um, or you just have a side project, you're messing around, you just want to get some vectors, go and install it, you know, don't worry about it.
Um, but if you put it in production and you're, and you're charging money for your product, then please, please buy a list. Yeah. Yeah. To have questions, Sign, um, how will you track who is using it for commercial and who is using it for a hobbyist project? That's a great question.
And, and I don't, I don't track that. Um, I'm also, I'm really into uh, privacy and safety on the web. So I don't like the idea of like putting in a whole bunch of tracking into lemon tree. Um, I think that's a terrible way to run a product these days.
Um, I, the only thing it does is I, uh, have it ask when it first starts up, it just asks the server for what the latest version is. And it'll tell you if there's a new version. So with that, I see, I see that, um, okay, the, you know, somebody asked for a new version.
Uh, and I anonymize all the IP addresses. So I don't even know who, like, there's nothing. There's no user information at all. So I just use that to kind of track, um, how often it starts. And it's, I, I see like maybe, maybe five downloads a day, um, right now. That's what I do.
So if, if you're running it, you're for pirating it, I can't stop you. Uh, spending my time trying to stop you. Uh, it's not, it's not worth my energy. Yeah. And I'd much rather, uh, I'd much rather work with teams who really want to gain something.
So if you do buy a license, I'll work with you on setting it up and telling you how to use it and working it and working on it with you.
Um, it's not advertised, but around model inference itself, I'm happy to, uh, offer services, uh, to get your model up and running and making sure that it's running optimally, um, even doing a model conversion with you, setting you, setting you up for that stuff.
Um, but that's, that's not advertised. It does say, like, I'll spend an hour with you if you buy a subscription to get you set up, but if you need more help than that, you know, let me know.
Uh, now there's another tier, which is like, if you're Amazon, Amazon would never buy my, they have their own world. But if you're like a cloud provider, or if you want to offer it as an API, that it doesn't count because it's, it's per, it's per product that I sell the license for.
So if you are selling it as a cloud provider, or as an API, and you've got like a thousand clients that are now using my money, well, I, I actually count all of those clients as a mighty user.
So I don't have a price published, but if you have that situation, I'm not going to charge you 99 dollars a month for each client. That's that, that, you know, if you're running that type of business, contact me and we'll work, we'll work something out. Yeah, that's perfect.
I mean, sounds like a solid model. I mean, for the start, for sure. And another like favorite question I have, and I've been asking this question also to open source players like VV8, um, and I think quadrant.
Um, so basically, um, have you thought, you know, one way of kind of building that connection that may yield a business case for you is what you just explained, right?
So somebody buys a license and then you scale with them, you explain how to make it better, how to tune it, maybe implement some features.
Another route is to open a Slack channel or Discord, whatever. And, you know, invite users there and then start talking to them.
And maybe you'll have some open source components as well at some point, you know, I don't know a tool that helps me to convert my model into representation that might you can read.
Um, have you considered also taking that open source route as one way of building that community of some of which will be your users and paying customers? Uh, great question. I don't have a, I don't have a Slack, I don't have a Slack myself. Um, I'm a member in many other slacks.
I could set up a Discord, I'm on Discord, um, mostly just for the ML ops community in Discord. But I could just start like a thread or a channel in that. I don't know if mighty itself needs its own Slack by itself. Um, I think it's more of a community. It would be part of another community.
One of the, one of the annoying things for me is I have to go and join like 12 million slacks because everybody has their own Slack and it doesn't work with one another. Discord does that way better. Slack, we got to have words. Um, you got to make it easier.
I have like four email addresses or five email addresses across like 12 different slacks right now. I can't keep track of them. Um, but in terms of open, of open source, I already have a bunch of open source projects. So uh, there is, um, max.io but spelled out, M-A-X-D-O-T-I-O on GitHub.
Somebody already took max-io. We can't have dots in GitHub names. Um, that's fine. You know, names or names. Uh, so there's mighty convert, which I actually, I'm working on updating that because it's based on, um, optimum, which is a hugging-face repository that does model conversion.
It's a very light wrapper around optimum. It basically just converts the model for you, uh, bundles the tokenizer and a configuration. That's it. Uh, it's pretty straightforward. Um, you can do that yourself. You don't have to use that. So that, but that's open source.
Um, there's also mighty batch, which is a node program, which is a way to do, uh, concurrent batch processing of documents, into vectors, pointing it at a mighty server.
Um, that's best described in the blog post that I wrote and how that works, um, about, you know, the, the blog post being, uh, converting the code of federal regulations. Um, that's on, it's on the homepage of max.io.
And, uh, there's also a bunch of other open source projects that I haven't talked about yet. So there's now node mighty, which is basically just an API client for node that will talk to mighty, um, it does connection pooling.
So if you have like four mighty, four mighty cores running, it'll talk to all the, it'll negotiate which core to use, um, when it makes a call. So that's really easy to use in like an express server.
Um, I also wrote two other node modules while I was at it, uh, that aren't from mighty, but I wrote node quadrant. So now there's a node client for, for the quadrant vector database. And I told, uh, uh, I told the guys at quadrant that this exists.
I'm trying to work on a blog post out of an asset, I guess this is the announcement. Um, but I'll, I'll, I'll publish something. There's going to be a demo. I also wrote node pine cone. So well, it's pine cone dash I.O. So now there's a node JS integration into pine cone.
So you can talk to pine cone from, from node from a kind of express server or something. Um, the guys at pine cone don't know what that I wrote that yet because it wasn't, I didn't, I just put it out there. It's on npm. Um, so I gotta, I gotta, I gotta work that out. And they might want it.
If you guys, if you want this, you know, I, I just wanted something that I could use, but it's your name. So please take the, take the package from me. If you don't get upset that I used your name. Um, I just wanted a tool that I could use for my own node JS testing.
Um, but then this stuff integrates with, with mighty really easily. So I have all these node clients now and I'm fricking focusing, focusing on JavaScript first. So all the stuff is going to be released. It's already, it's already up there. It's on npm. It's on my, my GitHub.
Uh, it's, it's free to use. It maybe needs a little bit more polish. I haven't fully mapped out the APIs. I just mapped out the course stuff that I needed to do. So it doesn't do things like the scroll command, you know, where you can scroll through all the points on quadrant.
But I don't know how much of a use for that is it's really easy to add that. I just didn't have the time. So yeah, there's, there's a bunch of open source work that I've been doing. Um, I also want to mention I'm working on starter applications.
So I have, I have right now, uh, basically it's like a, it's like a starter app that works with node and node mighty and quadrant. Um, and also node mighty and pine cone.
 I have two starter apps that aren't released yet that I'm working on polishing up and, and getting out there where it's where it's really easy if you're a node, if you're a job script person to just take documents, convert them into vectors, load them into a vector database, and have a search app running using them.
Yeah, that's fantastic. I mean, so much to unpack. And I think this could be one of the like a we're witnessing, um, a community written, uh, software for a close software company.
I mean, pine cone is a close software company, right? And we have an episode with Greg Kogan, who is a chief marketing marketing officer with pine cone. Um, we can connect you to and you can discuss the future. Yeah, I talked to Greg. You know, we're working on some stuff.
But what, what, my question is what made you write those connectors? Like, did you think that this would also pave the way to using mighty, you know, plugging in mighty in the pipeline? Let's say if I'm a pine cone user and I can have a node pine cone connector at the same time as mighty.
I'd say half half that, you know, there is, you know, I do want to promote mighty, of course. But again, I want to bring these tools outside of the Python ecosystem.
If you look at the vector databases right now, with it, with the exception of, uh, with VV8, VV8 does a great job of having different clients for different, um, different languages and stacks, um, Vespa as well. But both, both quadrant and pine cone right now, it's all Python.
Well, like, quadrant, quadrant is written in rust, but their client right now is their, their first class client is in Python. Um, which they did that because obviously everybody who has to get vectors has to use Python anyway, uh, or they used to. Um, so that's why they chose Python.
At least that's, that's what I speculate. Um, and pine cone as well, all their examples are in notebook form, um, in Jupyter notebook form. You go in and you want to do a somatic search example, that's a Python notebook. I'm not crazy about Python notebooks.
I think Python notebooks are good for illustrating like ideas and sketches, uh, for papers, but it's really hard for me to look at a Python notebook and say, here's how I make this into a working application. Um, it doesn't translate well because the, the architecture isn't there.
It's a bunch of cells that you run in order. That's not how, you know, real world applications work.
 So the idea is to just get these tools and get these ideas and capabilities out into the hands of a lot of other people who want to be able to use this stuff and are not familiar with Python, they're not familiar with NLP, but they want to be able to use this, uh, this new technology because they might have a business problem to try to solve.
So you're thinking actually about engineers who are day to day productizing their code and thinking, okay, yeah, I need a embedding layer, but I don't care about notebooks. I'm not a Pythonista or whatever. So, you know, just give me the tool. Exactly. Yeah, that's fantastic.
I mean, and by the tools, you also like disclose something like ahead of time with me that, to me, that, um, you, like one of the overarching goals for you is to develop as many tools for the vector search community as possible.
 And like some of the tools you mentioned, like go beyond, you know, pure engineering components, like connectors, you said, uh, maybe like fine tuning a model or something of that sort, which at that point, I think you're stepping, uh, on the ground of, you know, other startups like Gina and, um, you know, deep set and so on.
Do you feel that way or do you not concern yourself with those and you're just thinking, okay, what's missing in the field? I'm going to add it. I'm going to open source it. Yeah, same. So, uh, deep set is like, it's all Python.
Again, um, Gina, I think is a lot of Python, right? I'm not as familiar with Gina. Yeah, they are, they're Python mostly. Yeah. It's, it's, there's a huge opportunity, uh, to make these tools available to non Python, um, stacks.
And I don't, I, before I started working in machine learning, I've never even considered Python as, as an application framework. You know, people are using like Django, flash and stuff like that. Um, but for me, it was like, uh, it's not that it didn't take it seriously.
I just felt it wasn't, it wasn't something that I would have chosen to use aside from, you know, a lot of other, a lot of other stacks. So there is so many other teams out there that want to be able to use these things, but now they have to, oh, Python, Python, Python, it's nonstop.
So we got to break out of that somehow. Um, and, uh, I'm starting with node because the JavaScript ecosystem is just absolutely enormous. I think people underestimate the size of the JavaScript ecosystem.
If you're in machine learning and you're listening to this podcast right now, like there, there are like maybe a hundred people for every one of you who's using JavaScript in, in, for applications. Like that's how big it is. Um, so that, uh, I'm starting there.
I just know it's just an enormous community. And not only for front end development, you know, we need to emphasize this because you also have server side JavaScript, like Node.js and others. And it's, it's huge.
And a lot of software, which is kind of the, the middleware between your super cool search engine or your, your vector database, and the front end, you have a lot of middleware written in node because it's so much easier. Oh, well, not easy. I don't know.
Is it easier? But I think it's just the pervasive, you know, nature of JavaScript. Yeah, I don't know if I'd say node is easier than Python. I think it's, you know, I think they're similar actually in a lot of ways. The syntax is a little bit different, you know, curly braces versus tabs.
But, uh, I think that node, we're, we're getting away from vectors right now. But node started because the JavaScript was the language of the web. And people didn't want to learn another language to also write back end code.
You know, you were using Pearl, right? So a lot of the, there was a lot of time where it was like Pearl, PHP, plus JavaScript, right? There was that whole world out there. Um, so that's where node came from. It came from the web, the web front end. So that's, web front end is enormous.
And they all, and a lot of them just adopted node. And the node had its own hype cycle, like 2010 through 2014 was like maybe nodes heyday where it just was like through the roof. Everything was node.js. Um, it was going crazy. Now it's all, now it's all, uh, uh, you know, machine learning and AI.
A lot of people got involved in this, in this world. But there's still a huge, a huge section of the world that's written on top of node from applications that started in, in, you know, the early 2010s. And it evolved ever since. Yeah. But back to tools.
Like, so you said in the early notes you shared, like you also want to address some of the, uh, problem solved problems like in model fine tuning or some other like pipeline steps that, that may be precede the, uh, the, the embedding layer that you have now addressed with MITIS.
So what are your thoughts there? What, what do you think is missing? I don't, yeah, I don't know if I'm going to get into actual model tuning. I think that, first of all, I'm not, I'm not as good as, I'm not as good training models as other people.
There are other people that are suited to train models. But I do think there's a lot of other information that is lacking in model in the, the ML ops world and vector, and vector search.
One of them is just like, well, how similar are these things, right? What, what's the distribution of similarities? Um, I think we, V8 said they, they do support, uh, some of that and, uh, Vespas, what's some of that in logging.
But, um, I don't know about Pankoam, uh, I'm pretty sure, rust, uh, I'm sure, pretty sure quadrant does not.
So it's like, what do I mean by this? It's like, if I, if I, uh, have a vector and I get, and I do a query against, um, uh, quadrant, for example, I get back a list of documents that are nearest neighbors and the similarities.
Well, where does that fit? Like, if I get it back in the first document is like point four or not similar, right? Is that good? Is that bad? Like, what are the, what's, what's, what's real, what's real good similar? Maybe, maybe the best similarities are like point eight range.
So now I know that, well, in terms of my entire corpus and how people usually query, this result is actually not that great. And there's a lot of questions to be answered around that stuff. And so I think that's lacking in a lot of ways. I don't know if that's the right fit for Mighty though.
I think there's just external tools that, you know, I'm kicking around. All that stuff would be open source. I'm really interested in, in Mighty being, uh, the area of the business and then all the other stuff is open source to make things easier for people to use, uh, these things.
But yeah, there, there's a lot, there's a lot of stuff in terms of uh, in the MLObs world, there's like model drift.
It's like, well, I used, you know, if, let's say I have like 100, uh, 100 sentences, right? And I vectorized these against, you know, model one dot two dot three, right? And I got back, um, I got back a list of, uh, vectors. Now I've upgraded my model.
I have model one dot three dot eight, right? And now I, now I, uh, run my test vectors, my test sentences through and I get different vectors. Like how, how much has changed? What's the difference there? So there's this whole world around measuring model drift.
And there's some, there's some interesting open source tools on this already. But they're written in Python. So now you have to use Python to do all this stuff. So I'm trying to understand what, what the tools, uh, what tools could be written that are not in Python land.
Um, that could expose these statistics and this important information to people who, um, you know, who don't want to marry themselves to Python. Yeah, yeah, absolutely.
 This sounds like you touched also on this very important topic, which I think, uh, is, is, uh, known as a metric learning where, um, like on one hand, you do want to know what is the optimal distance and maybe you need to fine tune your model or maybe your data is not good fit for this model and so on.
But you do need the tools. Maybe it's something like Cupid for, you know, ranking, um, evaluation and tuning. You would also have some tool which is Cupid like maybe even with the UI way.
You can load this vectors, visualize them and see, okay, how do they fit together? What's missing and so on and then have the stats on it, right? So you can actually run the statistics and, um, you know, I'm gonna let Eric write that tool. I love Cupid. Cupid is so great.
Eric, go write Cupid for vector search. Yeah, I think, uh, we can pair up on that maybe all of us contribute, make it open source.
Um, but yeah, um, I think this is one way to look at it, right? Um, and I think quadrant, um, developers, they, they push the metric learning quite heavily forward by the time this podcast is, uh, this episode is out.
There will be another episode with a developer from quadrant who is actually very big on, on this idea of metric learning. And, uh, he opens sources, of course, everything. And I mean, he offers tools and also like, papers that you can read and indicate yourself on this space.
I think this is something that barely is scratched at the moment by the community, by, by even the end users, you know, they don't know. Okay, I take clip model. I have the images, plug them in together, works fine. I'm done.
What if it doesn't work? What if you have some images, you never find them for any query, but you do want to find them because it's a name of some product that was recently released and you do want to, to showcase it, right? And you're not using keyword search there. It's a name.
You're using, um, vectors to retrieve it, right? So it thinks like this. I mean, it's kind of like, there's a bunch of topics there.
One, another one favorite that I like is the, uh, robustness, right? So if I have an aircraft, I rotated a little bit and all of a sudden I find kittens instead of the aircrafts. And this is what Connor Shorten showed yesterday on on on the genometer and was amazing. I mean, robustness.
You just change slightly your input and you just, yeah, it doesn't work. So I think there is a lot of things missing, but like you, like from what I sense in your answer, like it feels like you do still want to keep your focus on mighty and push that as further along as possible, right? Yes.
And I want to, what I really want is I, I love that people download and install it and use it and do whatever they want, uh, to get vectors with my, that's awesome. I'm really trying to find partners.
I'm really trying to find partners who, um, who want to just really make it super easy uh, to do, uh, inference, model inference at scale. Um, so for example, I haven't gotten any replies. I've been like spamming, uh, not spamming.
I've been, uh, emailing and trying to get in touch with like cloud cloud providers, right, to say serverless inference.
If you could offer serverless inference, right, through lambdas or whatever, that's like so many people are asking for that, you know, you can't do that with Python tools these days. Um, you can do it. It's just going to, it would take forever and it would be really expensive and really slow.
Um, but there's such an opportunity for cloud providers to make it super easy.
So you can have, you know, you want to get content from, from point A into, uh, into your recommendation engine or your vector database or whatever, you know, do you want to stand up like the big GPU server in the middle to get this? No, you don't want to do that. Um, if you can avoid it.
So how about something that's that serverless and people can just run? So I'm trying to find partners there.
I'm trying to find partners who, uh, who have search platforms and, um, and other and other platforms or just see this as a Lego and their stack and things that's going to make it easier and they don't want to, you know, hire a team and spend months building this thing and trying to figure it out.
Um, you can do that of course. Go, uh, go do that, but, you know, you can save yourself a lot of time and pay and buy it. Um, by working with stuff that's already there. Yeah, that makes sense.
 I mean, probably companies like the likes of Algolea or, right, exactly, but potentially elastic, you know, because they, both of these, want to get closer to the neural search even though maybe they were not wired up originally to be vector search databases, but they do have the components like elastic based on Lussin and Algolea probably based also Lussin.
I'm not sure, but I'm sure that they're looking at this field. So I mean, for them and now we are getting a little bit into MLOPS and Vision, um, that you also shared a little bit ahead of time that, um, might it could be one of the components in the MLOPS ecosystem, right? Yeah, absolutely.
Not just a standalone kind of script, which I download and then I'm thinking, okay, where do I plug it in? Right? I mean, if it was, if it was, are you thinking in that direction as well yourself?
Like, okay, identifying the tools and systems where MIT could kind of like play a long role of the embedding software? Yeah, absolutely.
Um, it's, I have to, if, the other thing I want to figure out is, does it make sense as it is right now as a, as a web server? Like that for every case, probably not. There's probably situations. GRPC was one request, um, that I have to figure that out.
So that makes it a little bit easier to, to, um, to bind it to certain application layers. Uh, but yeah, it's, it's meant to be flexible for you sticking a model that your model, um, you know, and, and you, you run it how you want.
The, the other thing that I found was that I, I met a lot of people who were like scratching their heads saying, like, which model should I use also, right? As my, my first model or, or whatever. And I just want to start playing around with this.
 So that's the other thing I did is I, is I have like default models that I, that I chose that I know work well because, you know, especially like Neil's rumors, he's amazing and he's done amazing, um, community development around, around expert and the models that he's trained and the documentation he's published around why certain models are good and others are bad.
So other people, they don't know of, of, of this stuff. So it's just like, well, you don't have to go off and learn and understand, um, right away, why, why I should choose one model versus another. It's a hard decision to make. So there's some, there's some defaults that I chose.
So it's really easy to get started. So the, so the vectors themselves right off the bat or if you do question answering, it'll be, it'll be pretty good. Like for, for regular, regular English, not domain specific. You, you still have to do fine tuning for most cases.
But you're not going to start fine tuning before you even know how this thing performs like in the beginning, right? You want to try a model and see what, how close it is. Um, so there's some starting, starting work there. I know Algolia is getting to the vector search stuff. So I don't know.
Maybe they, they, maybe they don't know how to choose a model. So you guys, you can use my default model if you want. It's just a, yeah, absolutely. I mean, so far, what I hear from you is that my tea has, uh, the qualities, let's say, it can run on pure CPU, which is a win on cost.
It scales, which is also a win on cost in the long term. Right. Um, and it also, uh, is insanely fast, which is a win on product. It's a win on, go to market. Like I have this document, how quickly it travels through the pipeline and is searchable. Right. So I mean, it's important use case.
In some cases, like paramount, you know, like financial space, you know, a document came out. I wanted to be indexed right away. Like a second after, I don't want to wait five minutes. It will be way too late for me to make a decision.
So, I mean, is there something else? Like you, and maybe if you, if you could compare now or point us to the blog post, you know, uh, with other vendors like Amazon has in French, uh, you know, hugging face has infinity, infinity, right?
Um, and then, uh, and video, I think they also had some layer.
I forgot its name, but like those are probably fairly expensive. They probably are not $90 per piece. So what, what, what is your thinking there? So like you, you, I think you also are vocal in this space or like in that direction that mighty is much more economical.
Uh, than these more expensive solutions, but they probably offer something else as well, but like, you have an issue for sure. Yeah.
Um, I think that, so the interesting thing, if you, if you get involved with like, if you, if you get into Amazon, like in French, yeah, and all this stuff, they crafted like their entire, like they build their own hardware. Um, they have their neural core, um, that all the stuff is based around.
And that's like, it's lockin. It's big time lockin, right? Um, uh, this is just a web API. You can just use it. I, I think that, um, I, I've considered also like hosting an API, like, uh, hugging face, hugging faces like one of the most amazing software companies ever.
It's like, that's like the real community driven open source stuff. They do such amazing work. So I don't want to, I don't want to say anything bad about hugging face because I really have nothing bad to say at all.
Um, but, you know, Infinity definitely has a fit for the market, which is like, you know, if you are like Walmart and you need a solution, okay. Hacking face infinity is in your budget. Go pay for it, you know. Um, that's the type of thing that Walmart should use.
Um, but if, if you are just like, if you're a five person developer team or like, even a, if you work at a company that's like, you know, 300 people, infinity is like really, really expensive. Um, so there is a, there is a market segmentation there.
There's a difference between, okay, well, how much can you afford and who can you hire and what's the level of, um, internal support that you have to put around this thing and how does it all fit?
The teams that are just starting off that need to use something that, that works really fast, easy to use, then that's, that's where it might fit.
So I don't think mighty can, competes with infinity because honestly, I, uh, you know, hey, Walmart, if you want me as a customer, if you want, if you want to buy mighty, sure, go ahead, you know, let's talk or you can pay the 99 bucks a month. But, you know, that's not, that's not one target.
I'm trying to make it super easy for everybody else. Um, somebody high rank recently, uh, connected with me, a LinkedIn, I think some kind of VP of engineering, hey, if you're looking into embeddings, contact max.
Really? But like, so we understand, uh, infinity a little bit better because I didn't try this at all. Um, is this like some kind of web service that you basically buy subscription for like, sauce kind of thing? No, it's like a dark container. I think infinity is a dark container.
Um, I don't know, it might be, it might even be written in Rust, I'm not sure. Consider tokenizers are written in Rust, they may have done, I may have done some, infinity came out before mighty, so they may have done something. So it's a perfect competitor for, for mighty in that sense.
Um, I mean, I mean, no time pricing, but I mean, the only package itself, right? So basically, it's like Docker Docker anyway. Yeah. And I think, I think, I think my, well, I think infinity encourages GPU like you, they want you to use GPU for it. But that's like, I think infinity fits well.
If you have like, you know, a million requests an hour, something like that scale, you know? Yeah.
Um, if you have like 20,000 requests a day or a thousand requests a day, you know, that, that range, a hundred thousand, you know, I think by these perfect for that, you know, it's not, you don't have to have like this huge scale. It can get bigger.
You can just, you know, spend more money on hardware than scale it up as much as you want. You can support, you can support, you know, a million requests a day if you want to, you're a 10 million. You just have to put more hardware behind it. So I think I'm just competing in a different market.
I don't think, I don't think infinity and I are targeting the same, the same businesses. Yeah. Yeah. And I mean, you do have the edge on the fact that you want to address the community beyond Python. So like, I think it's a big, it's a big message to send.
Um, and in some ways through you, you channeled this, this feeling that, hey, this guy is in Node.js, a job, I probably feel like left out from this big thing, but it's probably not true.
I mean, I know also there is this deep learning for J and blah, blah, blah, but like, it's like an island in the ocean, probably comparing it to it. It's amazing software. It just didn't get the adoption that Python got. Yeah.
I remember going through these internal pains myself, right? When I was, when it was like 2015, 2016, and I started, and I started getting deep learning training and I took course error courses and rings courses on machine learning and stuff.
I started it off with Octav, which is an open source, uh, is a mathematical or whatever. It's a new Octav, but it's like, it's its own language, right? So it's mathematics, um, just just code. But then, like the next courses were all Python. And I was like, Oh, no, I have to learn Python.
I don't know Python. I have to know, no, no, no, no, no, no language to use this stuff. Okay, fine. I'll do it. Right? So I went down that and I learned Python and I got pretty good at it.
Um, but there's a lot of people who just don't want to take that step, you know, they want to, they want to ship code in their, in their stack. So it's, it's a big ask to say, if you want to use these awesome tools, you got to use, you got to, you got to convert, you got to convert your language.
Yeah, yeah, exactly. And if you're, you know, if you're not into data science or machine learning, then why would you enter Python at all? Like it has no, no like single winning point, well, maybe simplicity, but hey, is that it? You know, um, and it's like lose deposition.
Of course, you can make it more strict with typing and blah, blah, blah, but like still, but like it took me, I think it took me actually good three years to learn Python properly. Because it's like, not like, okay, oh, I understand how to do the for loop.
I understand the indentation and blah, but like to actually master it, right? Like, you know, avoid stupid loading of the model multiple times in G unicorn.
So, so I think the, all like, sithon, I didn't enter thyson, the sithon world, likely, but, but even just writing normal soft when Python takes a lot of time, productizing it takes a lot of time.
So, so why would you enter it if you are not after the tasty machine learning and data science? So why would you consider even converting your software stack into this? So it should be the other way around.
And I think you're doing a great job there with Mighty, basically offered as a service offered as maybe in the future as some kind of library or some kind of environment. I mean, Microsoft has been doing a bunch of these things. I don't know if you remember the CLR common language runtime.
So like, you, you, you bring up the, the visual studio and you can say, okay, my project will be in Pearl compiled and run for Java. I don't remember. It was crazy. I was just experimenting with it. And I was like, I barely knew any of these languages as a student, but I was fascinated by the idea.
It didn't fly, I think, but it was, it was amazing. Yeah, absolutely.
And I, you know, I would, I did, I did play around with the idea of, well, what if you don't even have to download Mighty, what if I was playing around with this idea from the NPM perspective, like, what if you just installed it from NPM command? And I thought, that's a little bit heavyweight.
Do I want to bring in this thing from, you know, I could. I don't know if that's if I should do that. And I also don't want to set false expectations to.
And maybe this is just because I'm not great at marketing, but I don't want to set the expectation of you just do NPM install, look, Mighty server. And then you have a perfectly running thing because it's, it's more than that. You have to scale it properly. You have to give it its own compute.
You have to choose the appropriate model. You have to, you have to do certain things to really get the most out of it.
So I don't want to set false expectations where somebody deploys it and, and it's like, it's, doesn't work well at all because they just did NPM install Mighty server, which doesn't exist by the way. Don't try that. And then it didn't, and then it didn't work.
So I, you know, there is a little bit of knowledge that you do that that you do have to attain. So I want to pass, you know, you do have to familiarize yourself with some concepts. That doesn't mean learning an entirely new language and stack. Yeah, it's more like probably like I'm a lobster devil.
So somebody can pick it up. And I mean, learning that way is much faster than actually, you know, figuring out how the how will I plug it into my Java code or C++ code or whatever. So yeah, of course. I think we, like I've really enjoyed this conversation, Max, we went deep into all these aspects.
Maybe not we can record another episode, you know, going in another direction. I'm sure there is like million, million directions to take.
But I enjoy asking this question of philosophical why, if you can still spare a few minutes, like why why why why why I'm fascinated by this field of vector search.
What brought you into it? And I remember I will also make sure to mention this that we did form a team with you and you you responded positively to my inquiry to compete in in billion scale and then competition. And you basically single handedly, almost driven the idea of body PQ.
Of course, we also have Alexander, similar who was helping you and all of us been brainstorming with you. But so that was kind of like maybe academic fascination with it, right? But other other facets that that keep you going also giving your background in search, which was pre vector search.
 Yeah, I'd say just my endless curiosity into things, you know, think a lot of us have that as, you know, if you're listening to this podcast, the audience, there's probably a lot of you are very curious about just check technology in general and the limitations of technology and what's positive and getting to that new magical thing and trying something for the first time and saying, Oh my God, this is incredible.
I can't believe this actually worked that I did this. So, so it's that. I mean, I, you know, I'm in my 40s now. So I've gone through that cycle a lot of times where I've tried something and it was amazing. I do really feel that there's a lot of practicality to it though, you know, in my wisdom now.
I see that yeah, just because something looks cool doesn't mean it's the best thing in the world and it should be used everywhere. So I, I see the practical, the practical use and need for vector search.
Whether or not it turns out to be like the end all be all the search, you know, that debate is open, right? But I don't think it is. I think it's just one piece in the puzzle. But it does solve this whole class of problems that were unsolvable before if you go back 10 years.
When I first started in search, the types of things that I'm doing right now. And I'll give you an example and I actually, you know, I set this to somebody the other day.
It's like, you know, the first time I installed solar, this is even, you know, maybe elastic search was around at that time, but maybe it was compass search. It wasn't even elastic yet. The first time I installed solar and I put in some documents, I was like, wow, this is amazing.
Like I can do a search. This is so much better than that crappy index that I was using on SQL Server. So it was just really, it was like that type of amazement.
But then you, you know, you work with it over time, you see the limitations and it's like, oh, this got it out of these synonyms and all these other problems and all this stuff.
I'll say that, you know, when you when you first start off in like the relevance of solar, like out of the box, you take their example, schema XML and you and you add some documents to it and you get back stuff and you're like, okay, this is cool.
If you take that feeling and then you once and I'll just use quadrant for an example because quadrant is in my opinion, like super easy to use, like you just doc or pull quadrant and use throw some and stuff in there. Especially now with this node thing.
So when I did that, the first time I used quadrant and I wrote this node wrapper and I just chucked in a whole bunch of documents, I saw that like just the out of the box relevance. And I'm not saying this is fine tuned, like this isn't something production worthy.
But just the out of the box relevance, I was like, this is better and I would spend in my opinion less time worrying about this than I would with an inverted index, you know, just because well, yeah, maybe the results aren't like super precise all the time and things like that.
But if I'm on a team and it's like, I got this search bar and I got this content and I don't want to worry about it, right? I don't want to worry about it. I just wanted to work. I wanted to surface stuff that's like reasonably accurate. It doesn't have to be the best search in the world.
But it's a cost for me. It's a cost for me as a team. I don't make money from search, but it's something I have to support. I think vector search offers are really, really good solution because it's not like you have to chase that endless bug of this doesn't even have anything to do with my search.
I search for, you know, what is the best hiking boot or something like that, you know? And all the documents they matched what 10 times, but there's no semblance of hiking boot or anything in my document. This is terrible. You know, you don't get anything like that in vector search.
And that's, I think, the appeal. You know, when you get into like real, real production, like highly tuned search, it's just one piece. But just for the teams that's like out of the box, I want to work and I don't want to deal with it.
I think it's a better, I think it's a better solution than elasticer solar. You end up spending a lot less time and headache. Yeah, that's amazing. That's that's so deep. And in what you said, speaks, speaks and sings a practitioner, but I think also speaks and sings a dreamer.
I think you dream of better ways of searching things, right?
And like you went through it practically, but also, you know, when you when you get so deep into practical elements, you get stuck into it and you're like, you're thinking in the in the framework of the given system, of a given language even, right?
Sometimes the paradigms that you read through the docs and you keep thinking about them, it's hard to unstick yourself from them.
And I mean, the fact that vector search field was born is magical in many ways. So I feel like you feel the same.
And I mean, the fact that you also ventured with me and others into building a new algorithm for vector search also says that that you wanted to go as deep as implementing an algorithm, right? So which what could be sexier than implementing an algorithm? I mean, I don't know.
Of course, all other things are also sexy, but I'm just saying that it's very it's very complex. It's very demanding in intellectually demanding work. So that that's amazing. Thanks so much for this depth.
And is there something you would like to share or announce with, you know, on mighty or maybe on something you're going to be presenting on Berlin buzzwords, I know as well, but is there something that you would like to share? Yeah, so I am presenting a Berlin buzzwords.
I am putting together a charity event to hack on vector search. And that's going to be on May 5th. I don't know when this podcast will be published, but on May 5th, I want to get and I want it to be it's just going to be an all day learning session on and I'm not charging money for this.
This is like free. I just want to show people how to use these tools if you're not in the Python world. If you're part of the Python world, you want to join amazing. Great.
But I want to do an all day like hackathon, where I'll show you how to get these things up and running hack away at it by the end you'll have, you know, a working or working example on your own.
And all the money we're all the time we're going to raise money for charity, specifically around refugees and displaced people, you know, because of the horrible things that are happening in Ukraine and other parts of the world as well.
You know, getting getting some learning happening and also raising money for charity seems like a great way to spend time. So I plan to host that on May 5th. It's probably going to be on Twitch because I want to just to be an open drop in drop out format. You can come, you can go.
It's not going to be like a controlled zoom where you, you know, it's like that. It's going to be on Twitch with chat and stuff like that. So I'm going to get it all set up. Details are going to come out shortly.
By the time this is published, maybe the details will be available already and we'll drop a link. Yeah, awesome. This sounds amazing that you also keep thinking about this sensitive topics or like what's happening in the world and you are also contributing with your skills into a good course here.
Thanks so much. I will try to publish this podcast before May 5th. So make sure that somebody can join and get chappin, of course, we can do the the most media, social media push. This is amazing. Thanks so much, Max. I've enjoyed this conversation thoroughly.
We went into depth and with and everything all dimensions. It's a multi-dimensional conversation. So thanks so much and keep it up and I'm curious to hear news about Mighty and the tooling around it and also looking forward to your building buzzwords presentation. Yeah, thank you so much, Dima.
It's great to chat. Yeah, thank you, Max. Cheers. Cheers. Take care. Bye-bye.