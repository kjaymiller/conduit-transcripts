---
description: '<p>This lightning session introduces a new idea in vector search - Wormhole
  vectors!</p><p>It has deep roots in physics and allows for transcending spaces of
  any nature: sparse, vector and behaviour (but could theoretically be any N-dimensional
  space).</p><p></p><p>Blog post on Medium: <a target="_blank" rel="noopener noreferrer
  nofollow" href="https://dmitry-kan.medium.com/novel-idea-in-vector-search-wormhole-vectors-6093910593b8">https://dmitry-kan.medium.com/novel-idea-in-vector-search-wormhole-vectors-6093910593b8</a></p><p></p><p>Session
  page on maven: <a target="_blank" rel="noopener noreferrer nofollow" href="https://maven.com/p/8c7de9/beyond-hybrid-search-with-wormhole-vectors?utm_campaign=NzI2NzIx&amp;utm_medium=ll_share_link&amp;utm_source=instructor">https://maven.com/p/8c7de9/beyond-hybrid-search-with-wormhole-vectors?utm_campaign=NzI2NzIx&amp;utm_medium=ll_share_link&amp;utm_source=instructor</a></p><p></p><p>To
  try the managed OpenSearch (multi-cloud, automatic backups, disaster recovery, vector
  search and more), go here: <a target="_blank" rel="noopener noreferrer nofollow"
  href="https://console.aiven.io/signup?utm_source=youtube&amp;utm_medium&amp;&amp;utm_content=vectorpodcast">https://console.aiven.io/signup?utm_source=youtube&amp;utm_medium&amp;&amp;utm_content=vectorpodcast</a></p><p></p><p>Get
  credits to use Aiven''s products (PG, Kafka, Valkey, OpenSearch, ClickHouse): <a
  target="_blank" rel="noopener noreferrer nofollow" href="https://aiven.io/startups">https://aiven.io/startups</a></p><p></p><p>Timecodes:</p><p>00:00
  Intro by Dmitry</p><p>01:48 Trey''s presentation</p><p>03:05 Walk to the AI-Powered
  Search course by Trey and Doug</p><p>07:07 Intro to vector spaces and embeddings</p><p>19:03
  Disjoint vector spaces and the need of hybrid search</p><p>23:11 Different modes
  of search</p><p>24:49 Wormhole vectors</p><p>47:49 Q&amp;A</p><p></p><p>What you''ll
  learn:</p><p></p><p>- What are "Wormhole Vectors"?</p><p>Learn how wormhole vectors
  work &amp; how to use them to traverse between disparate vector spaces for better
  hybrid search.</p><p>- Building a behavioral vector space from click stream data</p><p>Learn
  to generate behavioral embeddings to be integrated with dense/semantic and sparse/lexical
  vector queries.</p><p>- Traverse lexical, semantic, &amp; behavioral vectors spaces</p><p>Jump
  back and forth between multiple dense and sparse vector spaces in the same query</p><p>-
  Advanced hybrid search techniques (beyond fusion algorithms)</p><p>Hybrid search
  is more than mixing lexical + semantic search. See advanced techniques and where
  wormhole vectors fit in.</p><p></p><p>YouTube: <a target="_blank" rel="noopener
  noreferrer nofollow" href="https://www.youtube.com/watch?v=fvDC7nK-_C0">https://www.youtube.com/watch?v=fvDC7nK-_C0</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20251107_051156_724d3e0d493d36eed167f0604822b7e3.png
pub_date: Fri, 07 Nov 2025 05:58:00 GMT
title: Trey Grainger - Wormhole Vectors
url: https://rss.com/podcasts/vector-podcast/2314900
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 9.0, "text": " Alright,
  hello everyone, wherever you are, really, really happy to see all of you online.",
  "tokens": [50364, 2798, 11, 7751, 1518, 11, 8660, 291, 366, 11, 534, 11, 534, 2055,
  281, 536, 439, 295, 291, 2950, 13, 50814], "temperature": 0.0, "avg_logprob": -0.3031943683892908,
  "compression_ratio": 1.4818652849740932, "no_speech_prob": 0.3462936580181122},
  {"id": 1, "seek": 0, "start": 9.0, "end": 15.0, "text": " Welcome to the Beyond
  Hybrid Search with Warm Home Vectors. It''s another idea that", "tokens": [50814,
  4027, 281, 264, 19707, 47088, 17180, 365, 40353, 8719, 691, 557, 830, 13, 467, 311,
  1071, 1558, 300, 51114], "temperature": 0.0, "avg_logprob": -0.3031943683892908,
  "compression_ratio": 1.4818652849740932, "no_speech_prob": 0.3462936580181122},
  {"id": 2, "seek": 0, "start": 15.0, "end": 24.0, "text": " Tray is going to present
  today and we will have a discussion and all of you are welcome to ask questions
  as well.", "tokens": [51114, 1765, 320, 307, 516, 281, 1974, 965, 293, 321, 486,
  362, 257, 5017, 293, 439, 295, 291, 366, 2928, 281, 1029, 1651, 382, 731, 13, 51564],
  "temperature": 0.0, "avg_logprob": -0.3031943683892908, "compression_ratio": 1.4818652849740932,
  "no_speech_prob": 0.3462936580181122}, {"id": 3, "seek": 2400, "start": 24.0, "end":
  31.0, "text": " Yeah, cool. I think we''ll start with that. This is just a quick
  intro from me. I''m Dmitri Khan.", "tokens": [50364, 865, 11, 1627, 13, 286, 519,
  321, 603, 722, 365, 300, 13, 639, 307, 445, 257, 1702, 12897, 490, 385, 13, 286,
  478, 413, 3508, 470, 18136, 13, 50714], "temperature": 0.0, "avg_logprob": -0.18720425092256987,
  "compression_ratio": 1.4427860696517414, "no_speech_prob": 0.31713834404945374},
  {"id": 4, "seek": 2400, "start": 31.0, "end": 40.0, "text": " I, most recently,
  I''m with Ivan. I joined as a product director leading the search domain.", "tokens":
  [50714, 286, 11, 881, 3938, 11, 286, 478, 365, 28893, 13, 286, 6869, 382, 257, 1674,
  5391, 5775, 264, 3164, 9274, 13, 51164], "temperature": 0.0, "avg_logprob": -0.18720425092256987,
  "compression_ratio": 1.4427860696517414, "no_speech_prob": 0.31713834404945374},
  {"id": 5, "seek": 2400, "start": 40.0, "end": 49.0, "text": " We offer managed open
  search so that you don''t have your headaches setting it up and doing some DevOps.",
  "tokens": [51164, 492, 2626, 6453, 1269, 3164, 370, 300, 291, 500, 380, 362, 428,
  35046, 3287, 309, 493, 293, 884, 512, 43051, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.18720425092256987, "compression_ratio": 1.4427860696517414, "no_speech_prob":
  0.31713834404945374}, {"id": 6, "seek": 4900, "start": 49.0, "end": 57.0, "text":
  " And you can choose any cloud whatsoever, really. And then just go and run with
  that.", "tokens": [50364, 400, 291, 393, 2826, 604, 4588, 17076, 11, 534, 13, 400,
  550, 445, 352, 293, 1190, 365, 300, 13, 50764], "temperature": 0.0, "avg_logprob":
  -0.11983788398004347, "compression_ratio": 1.564102564102564, "no_speech_prob":
  0.19468526542186737}, {"id": 7, "seek": 4900, "start": 57.0, "end": 65.0, "text":
  " And I''ll share a couple of links later. I''m also a host of the vector podcast
  that I started, I think, four years ago.", "tokens": [50764, 400, 286, 603, 2073,
  257, 1916, 295, 6123, 1780, 13, 286, 478, 611, 257, 3975, 295, 264, 8062, 7367,
  300, 286, 1409, 11, 286, 519, 11, 1451, 924, 2057, 13, 51164], "temperature": 0.0,
  "avg_logprob": -0.11983788398004347, "compression_ratio": 1.564102564102564, "no_speech_prob":
  0.19468526542186737}, {"id": 8, "seek": 4900, "start": 65.0, "end": 75.0, "text":
  " I already stopped counting. Maybe some of you have heard some of the episodes.
  And yeah, it keeps going on and off, but I''m really excited to continue doing that.",
  "tokens": [51164, 286, 1217, 5936, 13251, 13, 2704, 512, 295, 291, 362, 2198, 512,
  295, 264, 9313, 13, 400, 1338, 11, 309, 5965, 516, 322, 293, 766, 11, 457, 286,
  478, 534, 2919, 281, 2354, 884, 300, 13, 51664], "temperature": 0.0, "avg_logprob":
  -0.11983788398004347, "compression_ratio": 1.564102564102564, "no_speech_prob":
  0.19468526542186737}, {"id": 9, "seek": 7500, "start": 75.0, "end": 84.0, "text":
  " I''ve been in search for, I think, 16 years, maybe 20 years if I include academic
  experience or exposure.", "tokens": [50364, 286, 600, 668, 294, 3164, 337, 11, 286,
  519, 11, 3165, 924, 11, 1310, 945, 924, 498, 286, 4090, 7778, 1752, 420, 10420,
  13, 50814], "temperature": 0.0, "avg_logprob": -0.14241212873316522, "compression_ratio":
  1.4505494505494505, "no_speech_prob": 0.24794630706310272}, {"id": 10, "seek": 7500,
  "start": 84.0, "end": 97.0, "text": " I''ve built search at startups, multinational
  technology giants. I think what was the startup, for example, AlfaSense became,
  I think, a unicorn company by now.", "tokens": [50814, 286, 600, 3094, 3164, 412,
  28041, 11, 45872, 1478, 2899, 31894, 13, 286, 519, 437, 390, 264, 18578, 11, 337,
  1365, 11, 967, 11771, 50, 1288, 3062, 11, 286, 519, 11, 257, 28122, 2237, 538, 586,
  13, 51464], "temperature": 0.0, "avg_logprob": -0.14241212873316522, "compression_ratio":
  1.4505494505494505, "no_speech_prob": 0.24794630706310272}, {"id": 11, "seek": 9700,
  "start": 97.0, "end": 108.0, "text": " Yeah, I''m super excited to partner with
  three AI power search and support from vector podcasts looking forward to the session
  today.", "tokens": [50364, 865, 11, 286, 478, 1687, 2919, 281, 4975, 365, 1045,
  7318, 1347, 3164, 293, 1406, 490, 8062, 24045, 1237, 2128, 281, 264, 5481, 965,
  13, 50914], "temperature": 0.0, "avg_logprob": -0.19855614994349105, "compression_ratio":
  1.5585585585585586, "no_speech_prob": 0.2782234847545624}, {"id": 12, "seek": 9700,
  "start": 108.0, "end": 110.0, "text": " Over to you, Trey.", "tokens": [50914, 4886,
  281, 291, 11, 314, 7950, 13, 51014], "temperature": 0.0, "avg_logprob": -0.19855614994349105,
  "compression_ratio": 1.5585585585585586, "no_speech_prob": 0.2782234847545624},
  {"id": 13, "seek": 9700, "start": 110.0, "end": 112.0, "text": " Awesome. Thanks,
  Dmitri. Appreciate it.", "tokens": [51014, 10391, 13, 2561, 11, 413, 3508, 470,
  13, 37601, 309, 13, 51114], "temperature": 0.0, "avg_logprob": -0.19855614994349105,
  "compression_ratio": 1.5585585585585586, "no_speech_prob": 0.2782234847545624},
  {"id": 14, "seek": 9700, "start": 112.0, "end": 121.0, "text": " I''m really excited
  to have Dmitri Khan more for the conversation part of this. He''s been doing, doing
  the vector podcast and in the space for a long time.", "tokens": [51114, 286, 478,
  534, 2919, 281, 362, 413, 3508, 470, 18136, 544, 337, 264, 3761, 644, 295, 341,
  13, 634, 311, 668, 884, 11, 884, 264, 8062, 7367, 293, 294, 264, 1901, 337, 257,
  938, 565, 13, 51564], "temperature": 0.0, "avg_logprob": -0.19855614994349105, "compression_ratio":
  1.5585585585585586, "no_speech_prob": 0.2782234847545624}, {"id": 15, "seek": 12100,
  "start": 121.0, "end": 135.0, "text": " So I think it''d be useful to help him facilitate,
  get lots of questions and good discussions. So I''m Trey Granger. I''m the lead
  author on the book AI Powered Search along with Doug Turnbull and Max Irwin.", "tokens":
  [50364, 407, 286, 519, 309, 1116, 312, 4420, 281, 854, 796, 20207, 11, 483, 3195,
  295, 1651, 293, 665, 11088, 13, 407, 286, 478, 314, 7950, 2606, 3176, 13, 286, 478,
  264, 1477, 3793, 322, 264, 1446, 7318, 7086, 292, 17180, 2051, 365, 12742, 7956,
  37290, 293, 7402, 9151, 9136, 13, 51064], "temperature": 0.0, "avg_logprob": -0.19658759877651552,
  "compression_ratio": 1.5, "no_speech_prob": 0.32589954137802124}, {"id": 16, "seek":
  12100, "start": 135.0, "end": 142.0, "text": " I''m the founder of Search Colonel
  company that does AI Powered Search consulting, technical advisor, open source connections.",
  "tokens": [51064, 286, 478, 264, 14917, 295, 17180, 28478, 2237, 300, 775, 7318,
  7086, 292, 17180, 23682, 11, 6191, 19161, 11, 1269, 4009, 9271, 13, 51414], "temperature":
  0.0, "avg_logprob": -0.19658759877651552, "compression_ratio": 1.5, "no_speech_prob":
  0.32589954137802124}, {"id": 17, "seek": 14200, "start": 142.0, "end": 156.0, "text":
  " Last year, I''ve been an adjunct professor at from university teaching computer
  science. My background, basically my entire career has been in search, particularly
  the intersection of data science, AI and search.", "tokens": [50364, 5264, 1064,
  11, 286, 600, 668, 364, 614, 10010, 349, 8304, 412, 490, 5454, 4571, 3820, 3497,
  13, 1222, 3678, 11, 1936, 452, 2302, 3988, 575, 668, 294, 3164, 11, 4098, 264, 15236,
  295, 1412, 3497, 11, 7318, 293, 3164, 13, 51064], "temperature": 0.0, "avg_logprob":
  -0.21775614298306978, "compression_ratio": 1.6487455197132617, "no_speech_prob":
  0.5073336362838745}, {"id": 18, "seek": 14200, "start": 156.0, "end": 170.0, "text":
  " My last company, prior to search journal, I was the CTO of pre search, which is
  a decentralized web search engine prior to that. I was the chief algorithms officer
  at Lucidworks, a search company, as well as prior to that, their SVP of engineering.",
  "tokens": [51064, 1222, 1036, 2237, 11, 4059, 281, 3164, 6708, 11, 286, 390, 264,
  383, 15427, 295, 659, 3164, 11, 597, 307, 257, 32870, 3670, 3164, 2848, 4059, 281,
  300, 13, 286, 390, 264, 9588, 14642, 8456, 412, 9593, 327, 18357, 11, 257, 3164,
  2237, 11, 382, 731, 382, 4059, 281, 300, 11, 641, 31910, 47, 295, 7043, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.21775614298306978, "compression_ratio": 1.6487455197132617,
  "no_speech_prob": 0.5073336362838745}, {"id": 19, "seek": 17000, "start": 170.0,
  "end": 181.0, "text": " I also had a search at career builder, prior to that. I
  also a decade ago, solar in action, but AI Powered Search is the focus of what I''m
  doing right now.", "tokens": [50364, 286, 611, 632, 257, 3164, 412, 3988, 27377,
  11, 4059, 281, 300, 13, 286, 611, 257, 10378, 2057, 11, 7936, 294, 3069, 11, 457,
  7318, 7086, 292, 17180, 307, 264, 1879, 295, 437, 286, 478, 884, 558, 586, 13, 50914],
  "temperature": 0.0, "avg_logprob": -0.21004395346039706, "compression_ratio": 1.6053639846743295,
  "no_speech_prob": 0.2600209712982178}, {"id": 20, "seek": 17000, "start": 181.0,
  "end": 197.0, "text": " The books got, you know, quite good reviews from folks.
  If you haven''t checked it out, please check it out. And this lightning lesson is
  one of a series leading up to an AI Powered Search course that Doug Turnbull and
  I are teaching starting two weeks from today.", "tokens": [50914, 440, 3642, 658,
  11, 291, 458, 11, 1596, 665, 10229, 490, 4024, 13, 759, 291, 2378, 380, 10033, 309,
  484, 11, 1767, 1520, 309, 484, 13, 400, 341, 16589, 6898, 307, 472, 295, 257, 2638,
  5775, 493, 281, 364, 7318, 7086, 292, 17180, 1164, 300, 12742, 7956, 37290, 293,
  286, 366, 4571, 2891, 732, 3259, 490, 965, 13, 51714], "temperature": 0.0, "avg_logprob":
  -0.21004395346039706, "compression_ratio": 1.6053639846743295, "no_speech_prob":
  0.2600209712982178}, {"id": 21, "seek": 19700, "start": 197.0, "end": 205.0, "text":
  " I heard of it. It''s kind of themed based upon the book, but we''ll be going into
  a lot of new and emerging techniques that aren''t in the book as well.", "tokens":
  [50364, 286, 2198, 295, 309, 13, 467, 311, 733, 295, 33920, 2361, 3564, 264, 1446,
  11, 457, 321, 603, 312, 516, 666, 257, 688, 295, 777, 293, 14989, 7512, 300, 3212,
  380, 294, 264, 1446, 382, 731, 13, 50764], "temperature": 0.0, "avg_logprob": -0.15663624560739112,
  "compression_ratio": 1.6645569620253164, "no_speech_prob": 0.3834373354911804},
  {"id": 22, "seek": 19700, "start": 205.0, "end": 226.0, "text": " Just to give you
  a sense, I''ll spend like a minute on this, maybe two. If you''re curious, it''s,
  you know, four solid weeks of material, the first week will sort of, you know, do
  a course intro, introduce the search relevance problem, talk about ranking those
  things. We''ll have a guest session from Eric Pugh from open source connections,
  talking about user behavior insights.", "tokens": [50764, 1449, 281, 976, 291, 257,
  2020, 11, 286, 603, 3496, 411, 257, 3456, 322, 341, 11, 1310, 732, 13, 759, 291,
  434, 6369, 11, 309, 311, 11, 291, 458, 11, 1451, 5100, 3259, 295, 2527, 11, 264,
  700, 1243, 486, 1333, 295, 11, 291, 458, 11, 360, 257, 1164, 12897, 11, 5366, 264,
  3164, 32684, 1154, 11, 751, 466, 17833, 729, 721, 13, 492, 603, 362, 257, 8341,
  5481, 490, 9336, 430, 1984, 490, 1269, 4009, 9271, 11, 1417, 466, 4195, 5223, 14310,
  13, 51814], "temperature": 0.0, "avg_logprob": -0.15663624560739112, "compression_ratio":
  1.6645569620253164, "no_speech_prob": 0.3834373354911804}, {"id": 23, "seek": 22600,
  "start": 226.0, "end": 236.0, "text": " For collecting click stream data and how
  to properly collect and process that are an accession will be on signals and reflected
  intelligence models.", "tokens": [50364, 1171, 12510, 2052, 4309, 1412, 293, 577,
  281, 6108, 2500, 293, 1399, 300, 366, 364, 2105, 313, 486, 312, 322, 12354, 293,
  15502, 7599, 5245, 13, 50864], "temperature": 0.0, "avg_logprob": -0.143905967029173,
  "compression_ratio": 1.7889908256880733, "no_speech_prob": 0.009816485457122326},
  {"id": 24, "seek": 22600, "start": 236.0, "end": 253.0, "text": " Everything from
  signals boosting for popularized relevance to learning to rank for generalized relevance
  to collaborative filtering and matrix factorization for personalized relevance to
  knowledge graph learning to learn from user behaviors.", "tokens": [50864, 5471,
  490, 12354, 43117, 337, 3743, 1602, 32684, 281, 2539, 281, 6181, 337, 44498, 32684,
  281, 16555, 30822, 293, 8141, 5952, 2144, 337, 28415, 32684, 281, 3601, 4295, 2539,
  281, 1466, 490, 4195, 15501, 13, 51714], "temperature": 0.0, "avg_logprob": -0.143905967029173,
  "compression_ratio": 1.7889908256880733, "no_speech_prob": 0.009816485457122326},
  {"id": 25, "seek": 25300, "start": 253.0, "end": 267.0, "text": " You know, terms,
  misspelling things like that about your domain. And then every week will have office
  hours where you can bring your hardest questions or we''ve got labs throughout the
  course as well. If you need help with those, we can help.", "tokens": [50364, 509,
  458, 11, 2115, 11, 1713, 494, 2669, 721, 411, 300, 466, 428, 9274, 13, 400, 550,
  633, 1243, 486, 362, 3398, 2496, 689, 291, 393, 1565, 428, 13158, 1651, 420, 321,
  600, 658, 20339, 3710, 264, 1164, 382, 731, 13, 759, 291, 643, 854, 365, 729, 11,
  321, 393, 854, 13, 51064], "temperature": 0.0, "avg_logprob": -0.1717073576790946,
  "compression_ratio": 1.4260355029585798, "no_speech_prob": 0.36015018820762634},
  {"id": 26, "seek": 26700, "start": 267.0, "end": 287.0, "text": " We the next week
  will dive into AI powered query modalities, things like buying coders and crossing
  coders talk about chunking, talk about late interaction models, hybrid search, multimodal
  search, all of those. Again, all of this has code and notebooks associated with
  it will be working through.", "tokens": [50364, 492, 264, 958, 1243, 486, 9192,
  666, 7318, 17786, 14581, 1072, 16110, 11, 721, 411, 6382, 17656, 433, 293, 14712,
  17656, 433, 751, 466, 16635, 278, 11, 751, 466, 3469, 9285, 5245, 11, 13051, 3164,
  11, 32972, 378, 304, 3164, 11, 439, 295, 729, 13, 3764, 11, 439, 295, 341, 575,
  3089, 293, 43782, 6615, 365, 309, 486, 312, 1364, 807, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.15559605396155154, "compression_ratio": 1.5797872340425532,
  "no_speech_prob": 0.6516717672348022}, {"id": 27, "seek": 28700, "start": 287.0,
  "end": 305.0, "text": " We have a guest lecture from Jenny from quadrant who will
  be talking about mixing sparse sentence representations with mini coil and then
  we''ll dive after that into sort of hands on building ranking classifiers or learning
  to rank models.", "tokens": [50364, 492, 362, 257, 8341, 7991, 490, 20580, 490,
  46856, 567, 486, 312, 1417, 466, 11983, 637, 11668, 8174, 33358, 365, 8382, 22225,
  293, 550, 321, 603, 9192, 934, 300, 666, 1333, 295, 2377, 322, 2390, 17833, 1508,
  23463, 420, 2539, 281, 6181, 5245, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.24801528453826904, "compression_ratio": 1.451219512195122, "no_speech_prob":
  0.5208132266998291}, {"id": 28, "seek": 30500, "start": 305.0, "end": 315.0, "text":
  " And what is entailed in that we will of course then have office hours again the
  next week will dive deep into rag talk about rag.", "tokens": [50364, 400, 437,
  307, 948, 24731, 294, 300, 321, 486, 295, 1164, 550, 362, 3398, 2496, 797, 264,
  958, 1243, 486, 9192, 2452, 666, 17539, 751, 466, 17539, 13, 50864], "temperature":
  0.0, "avg_logprob": -0.25813097702829463, "compression_ratio": 1.7728937728937728,
  "no_speech_prob": 0.56816565990448}, {"id": 29, "seek": 30500, "start": 315.0, "end":
  323.0, "text": " You know, sort of naive rag, agentech rag adaptive rag guard rails
  all the sorts of things you need to sort of understand to do to rag well.", "tokens":
  [50864, 509, 458, 11, 1333, 295, 29052, 17539, 11, 623, 1576, 339, 17539, 27912,
  17539, 6290, 27649, 439, 264, 7527, 295, 721, 291, 643, 281, 1333, 295, 1223, 281,
  360, 281, 17539, 731, 13, 51264], "temperature": 0.0, "avg_logprob": -0.25813097702829463,
  "compression_ratio": 1.7728937728937728, "no_speech_prob": 0.56816565990448}, {"id":
  30, "seek": 30500, "start": 323.0, "end": 334.0, "text": " We''ll talk about agentech
  search towards the end of the course talk about interleaving strategies for rag
  will have Max Irwin our co author on a powered search to giving a guest lecture
  session after that will be.", "tokens": [51264, 492, 603, 751, 466, 623, 1576, 339,
  3164, 3030, 264, 917, 295, 264, 1164, 751, 466, 728, 306, 6152, 9029, 337, 17539,
  486, 362, 7402, 9151, 9136, 527, 598, 3793, 322, 257, 17786, 3164, 281, 2902, 257,
  8341, 7991, 5481, 934, 300, 486, 312, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.25813097702829463, "compression_ratio": 1.7728937728937728, "no_speech_prob":
  0.56816565990448}, {"id": 31, "seek": 33400, "start": 334.0, "end": 354.0, "text":
  " Automating learning to rank and with click models and with active learning so
  we''ll be diving into how to deal with biases in your data how to deal with exploration
  versus exploitation looking for results that may maybe don''t show up in your normal
  search patterns and then.", "tokens": [50364, 24619, 990, 2539, 281, 6181, 293,
  365, 2052, 5245, 293, 365, 4967, 2539, 370, 321, 603, 312, 20241, 666, 577, 281,
  2028, 365, 32152, 294, 428, 1412, 577, 281, 2028, 365, 16197, 5717, 33122, 1237,
  337, 3542, 300, 815, 1310, 500, 380, 855, 493, 294, 428, 2710, 3164, 8294, 293,
  550, 13, 51364], "temperature": 0.0, "avg_logprob": -0.14062168768474034, "compression_ratio":
  1.6407185628742516, "no_speech_prob": 0.005514203105121851}, {"id": 32, "seek":
  35400, "start": 354.0, "end": 378.0, "text": " The sort of final two weeks will
  have a guest lecture from john handler from open search and AWS really talking about
  scaling vector search in production with lots of good experience from large scale
  open search clusters and Amazon servers and then we''ll dive into optimizing I search
  for production everything from quantization re ranking strategies semantic caching.",
  "tokens": [50364, 440, 1333, 295, 2572, 732, 3259, 486, 362, 257, 8341, 7991, 490,
  35097, 41967, 490, 1269, 3164, 293, 17650, 534, 1417, 466, 21589, 8062, 3164, 294,
  4265, 365, 3195, 295, 665, 1752, 490, 2416, 4373, 1269, 3164, 23313, 293, 6795,
  15909, 293, 550, 321, 603, 9192, 666, 40425, 286, 3164, 337, 4265, 1203, 490, 4426,
  2144, 319, 17833, 9029, 47982, 269, 2834, 13, 51564], "temperature": 0.0, "avg_logprob":
  -0.1519966552506632, "compression_ratio": 1.6428571428571428, "no_speech_prob":
  0.20361757278442383}, {"id": 33, "seek": 37800, "start": 378.0, "end": 400.0, "text":
  " Running local models and then for our last session will dive deep into AI powered
  query understanding and agentech search focused on really interpreting understanding
  queries leveraging agents as part of that process and so if that''s interesting
  to you there''s a link and a QR code here anyone who attends today is eligible for
  20% off the course.", "tokens": [50364, 28136, 2654, 5245, 293, 550, 337, 527, 1036,
  5481, 486, 9192, 2452, 666, 7318, 17786, 14581, 3701, 293, 623, 1576, 339, 3164,
  5178, 322, 534, 37395, 3701, 24109, 32666, 12554, 382, 644, 295, 300, 1399, 293,
  370, 498, 300, 311, 1880, 281, 291, 456, 311, 257, 2113, 293, 257, 32784, 3089,
  510, 2878, 567, 49837, 965, 307, 14728, 337, 945, 4, 766, 264, 1164, 13, 51464],
  "temperature": 0.0, "avg_logprob": -0.10343417568483214, "compression_ratio": 1.5844748858447488,
  "no_speech_prob": 0.19440768659114838}, {"id": 34, "seek": 40000, "start": 401.0,
  "end": 425.0, "text": " And so definitely check it out if you''ve been considering
  it there''s two weeks left and of course even if you can''t attend all the sessions
  everyone who''s enrolled will have permanent access to all of the recordings all
  the code and all the course materials so you can use these going forward into the
  future if that''s interesting to you so done with that now I''d like to get to our
  topic which is beyond hybrid search with wormhole vectors.", "tokens": [50414, 400,
  370, 2138, 1520, 309, 484, 498, 291, 600, 668, 8079, 309, 456, 311, 732, 3259, 1411,
  293, 295, 1164, 754, 498, 291, 393, 380, 6888, 439, 264, 11081, 1518, 567, 311,
  25896, 486, 362, 10996, 2105, 281, 439, 295, 264, 25162, 439, 264, 3089, 293, 439,
  264, 1164, 5319, 370, 291, 393, 764, 613, 516, 2128, 666, 264, 2027, 498, 300, 311,
  1880, 281, 291, 370, 1096, 365, 300, 586, 286, 1116, 411, 281, 483, 281, 527, 4829,
  597, 307, 4399, 13051, 3164, 365, 23835, 14094, 18875, 13, 51614], "temperature":
  0.0, "avg_logprob": -0.07660269480879589, "compression_ratio": 1.6768060836501901,
  "no_speech_prob": 0.17372703552246094}, {"id": 35, "seek": 42500, "start": 425.0,
  "end": 454.0, "text": " So let me dive straight in and feel free if you have questions
  as Dimitri said post them in the comments Dimitri feel free to interrupt me at any
  point if there''s something worth diving into otherwise i''m just going to keep
  going and kind of focus on conversation at the end so I want to start with some
  basic material on vectors and vector spaces to kind of set our expectations for
  where we''re going with wormhole vectors to start vectors by definition mathematically
  or something that have direction and we''re going to start with the end of the end
  of the session.", "tokens": [50414, 407, 718, 385, 9192, 2997, 294, 293, 841, 1737,
  498, 291, 362, 1651, 382, 20975, 270, 470, 848, 2183, 552, 294, 264, 3053, 20975,
  270, 470, 841, 1737, 281, 12729, 385, 412, 604, 935, 498, 456, 311, 746, 3163, 20241,
  666, 5911, 741, 478, 445, 516, 281, 1066, 516, 293, 733, 295, 1879, 322, 3761, 412,
  264, 917, 370, 286, 528, 281, 722, 365, 512, 3875, 2527, 322, 18875, 293, 8062,
  7673, 281, 733, 295, 992, 527, 9843, 337, 689, 321, 434, 516, 365, 23835, 14094,
  18875, 281, 722, 18875, 538, 7123, 44003, 420, 746, 300, 362, 3513, 293, 321, 434,
  516, 281, 722, 365, 264, 917, 295, 264, 917, 295, 264, 5481, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.3083912123981704, "compression_ratio": 1.89, "no_speech_prob":
  0.12884946167469025}, {"id": 36, "seek": 45500, "start": 455.0, "end": 457.18, "text":
  " And in this video let''s see in situations [\u266amagnitude [\u266amagnitude [\u266amagnitude
  [\u266amagnitude [\u266amagnitude [\u266amagnitude [\u266amagnitude [\u266amagnitude
  [\u266amagnitude [\u266amagnitude [\u266amagnitude [\u266amagnitude [\u266amagnitude
  [\u266amagnitude [\u266amagnitude [\u266amanage [\u266amagnitude [\u266af Mash Fans
  Bake \u0443\u0432\u0438\u0434 then", "tokens": [50364, 400, 294, 341, 960, 718,
  311, 536, 294, 6851, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76, 4535,
  4377, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529,
  76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377,
  44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76, 4535, 4377, 44529, 76,
  4535, 4377, 44529, 76, 4535, 4377, 44529, 1601, 609, 44529, 76, 4535, 4377, 44529,
  69, 42039, 25065, 42597, 21974, 550, 50473], "temperature": 1.0, "avg_logprob":
  -2.9473230931665992, "compression_ratio": 2.16, "no_speech_prob": 0.0055676670745015144},
  {"id": 37, "seek": 45500, "start": 457.18, "end": 458.88, "text": "\u82e5ymab\u0457r
  VPN www.pe devils.comspeaking.habit.com", "tokens": [50473, 13736, 98, 4199, 455,
  8045, 81, 24512, 12520, 13, 494, 1905, 4174, 13, 1112, 14579, 13, 7821, 270, 13,
  1112, 50558], "temperature": 1.0, "avg_logprob": -2.9473230931665992, "compression_ratio":
  2.16, "no_speech_prob": 0.0055676670745015144}, {"id": 38, "seek": 45500, "start":
  458.88, "end": 468.96, "text": " So let''s see how much you could get together.",
  "tokens": [50558, 407, 718, 311, 536, 577, 709, 291, 727, 483, 1214, 13, 51062],
  "temperature": 1.0, "avg_logprob": -2.9473230931665992, "compression_ratio": 2.16,
  "no_speech_prob": 0.0055676670745015144}, {"id": 39, "seek": 45500, "start": 474.0,
  "end": 480.9, "text": " of course GK doctrine is a huge task, a huge task that a
  man develops on who the heck is dominant during the process and setup it in", "tokens":
  [51314, 295, 1164, 460, 42, 23290, 307, 257, 2603, 5633, 11, 257, 2603, 5633, 300,
  257, 587, 25453, 322, 567, 264, 12872, 307, 15657, 1830, 264, 1399, 293, 8657, 309,
  294, 51659], "temperature": 1.0, "avg_logprob": -2.9473230931665992, "compression_ratio":
  2.16, "no_speech_prob": 0.0055676670745015144}, {"id": 40, "seek": 48090, "start":
  480.9, "end": 483.65999999999997, "text": " in vector space and a Hilbert space,",
  "tokens": [50364, 294, 8062, 1901, 293, 257, 19914, 4290, 1901, 11, 50502], "temperature":
  0.0, "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849,
  "no_speech_prob": 0.1460099071264267}, {"id": 41, "seek": 48090, "start": 483.65999999999997,
  "end": 485.9, "text": " but in a semantic vector space,", "tokens": [50502, 457,
  294, 257, 47982, 8062, 1901, 11, 50614], "temperature": 0.0, "avg_logprob": -0.29920297241210936,
  "compression_ratio": 1.7569721115537849, "no_speech_prob": 0.1460099071264267},
  {"id": 42, "seek": 48090, "start": 485.9, "end": 487.94, "text": " into which we
  can map a concept.", "tokens": [50614, 666, 597, 321, 393, 4471, 257, 3410, 13,
  50716], "temperature": 0.0, "avg_logprob": -0.29920297241210936, "compression_ratio":
  1.7569721115537849, "no_speech_prob": 0.1460099071264267}, {"id": 43, "seek": 48090,
  "start": 487.94, "end": 491.29999999999995, "text": " So whereas, vectors have dimensions,",
  "tokens": [50716, 407, 9735, 11, 18875, 362, 12819, 11, 50884], "temperature": 0.0,
  "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849, "no_speech_prob":
  0.1460099071264267}, {"id": 44, "seek": 48090, "start": 491.29999999999995, "end":
  494.58, "text": " and those dimensions sort of go in any direction.", "tokens":
  [50884, 293, 729, 12819, 1333, 295, 352, 294, 604, 3513, 13, 51048], "temperature":
  0.0, "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849,
  "no_speech_prob": 0.1460099071264267}, {"id": 45, "seek": 48090, "start": 494.58,
  "end": 496.14, "text": " When we talk about an embedding,", "tokens": [51048, 1133,
  321, 751, 466, 364, 12240, 3584, 11, 51126], "temperature": 0.0, "avg_logprob":
  -0.29920297241210936, "compression_ratio": 1.7569721115537849, "no_speech_prob":
  0.1460099071264267}, {"id": 46, "seek": 48090, "start": 496.14, "end": 499.17999999999995,
  "text": " an embedding is actually a point in vector space.", "tokens": [51126,
  364, 12240, 3584, 307, 767, 257, 935, 294, 8062, 1901, 13, 51278], "temperature":
  0.0, "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849,
  "no_speech_prob": 0.1460099071264267}, {"id": 47, "seek": 48090, "start": 499.17999999999995,
  "end": 501.06, "text": " So for example, this point right here,", "tokens": [51278,
  407, 337, 1365, 11, 341, 935, 558, 510, 11, 51372], "temperature": 0.0, "avg_logprob":
  -0.29920297241210936, "compression_ratio": 1.7569721115537849, "no_speech_prob":
  0.1460099071264267}, {"id": 48, "seek": 48090, "start": 501.06, "end": 504.38, "text":
  " this series of floats for book or tree or what have you.", "tokens": [51372, 341,
  2638, 295, 37878, 337, 1446, 420, 4230, 420, 437, 362, 291, 13, 51538], "temperature":
  0.0, "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849,
  "no_speech_prob": 0.1460099071264267}, {"id": 49, "seek": 48090, "start": 504.38,
  "end": 506.09999999999997, "text": " You can think of it as a vector", "tokens":
  [51538, 509, 393, 519, 295, 309, 382, 257, 8062, 51624], "temperature": 0.0, "avg_logprob":
  -0.29920297241210936, "compression_ratio": 1.7569721115537849, "no_speech_prob":
  0.1460099071264267}, {"id": 50, "seek": 48090, "start": 506.09999999999997, "end":
  509.85999999999996, "text": " originating from the origin at 0, 0 here,", "tokens":
  [51624, 4957, 990, 490, 264, 4957, 412, 1958, 11, 1958, 510, 11, 51812], "temperature":
  0.0, "avg_logprob": -0.29920297241210936, "compression_ratio": 1.7569721115537849,
  "no_speech_prob": 0.1460099071264267}, {"id": 51, "seek": 50986, "start": 509.86,
  "end": 512.26, "text": " and extending out to that point.", "tokens": [50364, 293,
  24360, 484, 281, 300, 935, 13, 50484], "temperature": 0.0, "avg_logprob": -0.19104307731695935,
  "compression_ratio": 1.695970695970696, "no_speech_prob": 0.00017427001148462296},
  {"id": 52, "seek": 50986, "start": 512.26, "end": 515.34, "text": " But fundamentally,
  we think of an embedding as a coordinate,", "tokens": [50484, 583, 17879, 11, 321,
  519, 295, 364, 12240, 3584, 382, 257, 15670, 11, 50638], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 53, "seek": 50986, "start": 515.34, "end": 518.0600000000001,
  "text": " that is a point in vector space that corresponds", "tokens": [50638, 300,
  307, 257, 935, 294, 8062, 1901, 300, 23249, 50774], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 54, "seek": 50986, "start": 518.0600000000001, "end":
  521.3000000000001, "text": " with some semantic meaning.", "tokens": [50774, 365,
  512, 47982, 3620, 13, 50936], "temperature": 0.0, "avg_logprob": -0.19104307731695935,
  "compression_ratio": 1.695970695970696, "no_speech_prob": 0.00017427001148462296},
  {"id": 55, "seek": 50986, "start": 521.3000000000001, "end": 523.62, "text": " And
  search whenever we''re dealing with embeddings,", "tokens": [50936, 400, 3164, 5699,
  321, 434, 6260, 365, 12240, 29432, 11, 51052], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 56, "seek": 50986, "start": 523.62, "end": 527.58,
  "text": " we often have things like word or phrase embeddings,", "tokens": [51052,
  321, 2049, 362, 721, 411, 1349, 420, 9535, 12240, 29432, 11, 51250], "temperature":
  0.0, "avg_logprob": -0.19104307731695935, "compression_ratio": 1.695970695970696,
  "no_speech_prob": 0.00017427001148462296}, {"id": 57, "seek": 50986, "start": 527.58,
  "end": 529.1800000000001, "text": " where we take an individual word", "tokens":
  [51250, 689, 321, 747, 364, 2609, 1349, 51330], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 58, "seek": 50986, "start": 529.1800000000001, "end":
  531.46, "text": " and leveraging a transformer model typically.", "tokens": [51330,
  293, 32666, 257, 31782, 2316, 5850, 13, 51444], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 59, "seek": 50986, "start": 531.46, "end": 534.9,
  "text": " We will generate that series of floats", "tokens": [51444, 492, 486, 8460,
  300, 2638, 295, 37878, 51616], "temperature": 0.0, "avg_logprob": -0.19104307731695935,
  "compression_ratio": 1.695970695970696, "no_speech_prob": 0.00017427001148462296},
  {"id": 60, "seek": 50986, "start": 534.9, "end": 537.02, "text": " that represents
  the meaning of that word,", "tokens": [51616, 300, 8855, 264, 3620, 295, 300, 1349,
  11, 51722], "temperature": 0.0, "avg_logprob": -0.19104307731695935, "compression_ratio":
  1.695970695970696, "no_speech_prob": 0.00017427001148462296}, {"id": 61, "seek":
  50986, "start": 537.02, "end": 538.54, "text": " given the context around it.",
  "tokens": [51722, 2212, 264, 4319, 926, 309, 13, 51798], "temperature": 0.0, "avg_logprob":
  -0.19104307731695935, "compression_ratio": 1.695970695970696, "no_speech_prob":
  0.00017427001148462296}, {"id": 62, "seek": 53854, "start": 538.54, "end": 540.9399999999999,
  "text": " But we can also have sentence embeddings,", "tokens": [50364, 583, 321,
  393, 611, 362, 8174, 12240, 29432, 11, 50484], "temperature": 0.0, "avg_logprob":
  -0.1349480564432933, "compression_ratio": 1.937269372693727, "no_speech_prob": 0.0001605852594366297},
  {"id": 63, "seek": 53854, "start": 540.9399999999999, "end": 542.8199999999999,
  "text": " where we look at all of the words in the sentence", "tokens": [50484,
  689, 321, 574, 412, 439, 295, 264, 2283, 294, 264, 8174, 50578], "temperature":
  0.0, "avg_logprob": -0.1349480564432933, "compression_ratio": 1.937269372693727,
  "no_speech_prob": 0.0001605852594366297}, {"id": 64, "seek": 53854, "start": 542.8199999999999,
  "end": 544.86, "text": " and their contextual meaning,", "tokens": [50578, 293,
  641, 35526, 3620, 11, 50680], "temperature": 0.0, "avg_logprob": -0.1349480564432933,
  "compression_ratio": 1.937269372693727, "no_speech_prob": 0.0001605852594366297},
  {"id": 65, "seek": 53854, "start": 544.86, "end": 548.18, "text": " and generate
  an embedding that represents", "tokens": [50680, 293, 8460, 364, 12240, 3584, 300,
  8855, 50846], "temperature": 0.0, "avg_logprob": -0.1349480564432933, "compression_ratio":
  1.937269372693727, "no_speech_prob": 0.0001605852594366297}, {"id": 66, "seek":
  53854, "start": 548.18, "end": 549.18, "text": " the meaning of the sentence.",
  "tokens": [50846, 264, 3620, 295, 264, 8174, 13, 50896], "temperature": 0.0, "avg_logprob":
  -0.1349480564432933, "compression_ratio": 1.937269372693727, "no_speech_prob": 0.0001605852594366297},
  {"id": 67, "seek": 53854, "start": 549.18, "end": 550.54, "text": " We can have
  paragraph embeddings", "tokens": [50896, 492, 393, 362, 18865, 12240, 29432, 50964],
  "temperature": 0.0, "avg_logprob": -0.1349480564432933, "compression_ratio": 1.937269372693727,
  "no_speech_prob": 0.0001605852594366297}, {"id": 68, "seek": 53854, "start": 550.54,
  "end": 554.02, "text": " that sort of summarize the core ideas of that paragraph,",
  "tokens": [50964, 300, 1333, 295, 20858, 264, 4965, 3487, 295, 300, 18865, 11, 51138],
  "temperature": 0.0, "avg_logprob": -0.1349480564432933, "compression_ratio": 1.937269372693727,
  "no_speech_prob": 0.0001605852594366297}, {"id": 69, "seek": 53854, "start": 554.02,
  "end": 555.54, "text": " and the same thing with a document.", "tokens": [51138,
  293, 264, 912, 551, 365, 257, 4166, 13, 51214], "temperature": 0.0, "avg_logprob":
  -0.1349480564432933, "compression_ratio": 1.937269372693727, "no_speech_prob": 0.0001605852594366297},
  {"id": 70, "seek": 53854, "start": 555.54, "end": 558.5799999999999, "text": " Often
  in search, we''ll start with just a document embedding,", "tokens": [51214, 20043,
  294, 3164, 11, 321, 603, 722, 365, 445, 257, 4166, 12240, 3584, 11, 51366], "temperature":
  0.0, "avg_logprob": -0.1349480564432933, "compression_ratio": 1.937269372693727,
  "no_speech_prob": 0.0001605852594366297}, {"id": 71, "seek": 53854, "start": 558.5799999999999,
  "end": 561.6999999999999, "text": " and when we take a query, we generate an embedding,",
  "tokens": [51366, 293, 562, 321, 747, 257, 14581, 11, 321, 8460, 364, 12240, 3584,
  11, 51522], "temperature": 0.0, "avg_logprob": -0.1349480564432933, "compression_ratio":
  1.937269372693727, "no_speech_prob": 0.0001605852594366297}, {"id": 72, "seek":
  53854, "start": 561.6999999999999, "end": 563.54, "text": " and we do sort of a
  vector similarity", "tokens": [51522, 293, 321, 360, 1333, 295, 257, 8062, 32194,
  51614], "temperature": 0.0, "avg_logprob": -0.1349480564432933, "compression_ratio":
  1.937269372693727, "no_speech_prob": 0.0001605852594366297}, {"id": 73, "seek":
  53854, "start": 563.54, "end": 567.0999999999999, "text": " between defined related
  documents that match the query.", "tokens": [51614, 1296, 7642, 4077, 8512, 300,
  2995, 264, 14581, 13, 51792], "temperature": 0.0, "avg_logprob": -0.1349480564432933,
  "compression_ratio": 1.937269372693727, "no_speech_prob": 0.0001605852594366297},
  {"id": 74, "seek": 56710, "start": 567.1, "end": 569.26, "text": " But you can chunk
  documents up in any way", "tokens": [50364, 583, 291, 393, 16635, 8512, 493, 294,
  604, 636, 50472], "temperature": 0.0, "avg_logprob": -0.16214718204913753, "compression_ratio":
  1.628691983122363, "no_speech_prob": 9.877497359411791e-05}, {"id": 75, "seek":
  56710, "start": 569.26, "end": 571.74, "text": " and any number of vectors.", "tokens":
  [50472, 293, 604, 1230, 295, 18875, 13, 50596], "temperature": 0.0, "avg_logprob":
  -0.16214718204913753, "compression_ratio": 1.628691983122363, "no_speech_prob":
  9.877497359411791e-05}, {"id": 76, "seek": 56710, "start": 571.74, "end": 575.3000000000001,
  "text": " Conceptually, we typically think of embeddings and vectors", "tokens":
  [50596, 47482, 671, 11, 321, 5850, 519, 295, 12240, 29432, 293, 18875, 50774], "temperature":
  0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 77, "seek": 56710, "start": 575.3000000000001,
  "end": 578.86, "text": " as having a relatively small number of dimensions.", "tokens":
  [50774, 382, 1419, 257, 7226, 1359, 1230, 295, 12819, 13, 50952], "temperature":
  0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 78, "seek": 56710, "start": 578.86,
  "end": 582.5, "text": " We call these dense vectors, where maybe there''s 768",
  "tokens": [50952, 492, 818, 613, 18011, 18875, 11, 689, 1310, 456, 311, 1614, 27102,
  51134], "temperature": 0.0, "avg_logprob": -0.16214718204913753, "compression_ratio":
  1.628691983122363, "no_speech_prob": 9.877497359411791e-05}, {"id": 79, "seek":
  56710, "start": 582.5, "end": 586.1, "text": " or 1024, some number of dimensions.",
  "tokens": [51134, 420, 1266, 7911, 11, 512, 1230, 295, 12819, 13, 51314], "temperature":
  0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 80, "seek": 56710, "start": 586.1,
  "end": 589.9, "text": " And we compress lots of data into a continuous space", "tokens":
  [51314, 400, 321, 14778, 3195, 295, 1412, 666, 257, 10957, 1901, 51504], "temperature":
  0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 81, "seek": 56710, "start": 589.9,
  "end": 590.9, "text": " within those.", "tokens": [51504, 1951, 729, 13, 51554],
  "temperature": 0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 82, "seek": 56710, "start": 590.9,
  "end": 596.7, "text": " However, there''s also the notion of sparse vectors.", "tokens":
  [51554, 2908, 11, 456, 311, 611, 264, 10710, 295, 637, 11668, 18875, 13, 51844],
  "temperature": 0.0, "avg_logprob": -0.16214718204913753, "compression_ratio": 1.628691983122363,
  "no_speech_prob": 9.877497359411791e-05}, {"id": 83, "seek": 59670, "start": 596.7,
  "end": 598.5400000000001, "text": " And the best way to think of a sparse vector",
  "tokens": [50364, 400, 264, 1151, 636, 281, 519, 295, 257, 637, 11668, 8062, 50456],
  "temperature": 0.0, "avg_logprob": -0.1382564211648608, "compression_ratio": 1.7547892720306513,
  "no_speech_prob": 4.4013890146743506e-05}, {"id": 84, "seek": 59670, "start": 598.5400000000001,
  "end": 600.7, "text": " for purposes of our discussion today", "tokens": [50456,
  337, 9932, 295, 527, 5017, 965, 50564], "temperature": 0.0, "avg_logprob": -0.1382564211648608,
  "compression_ratio": 1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05},
  {"id": 85, "seek": 59670, "start": 600.7, "end": 604.46, "text": " is to think of
  lexical search and to think of just,", "tokens": [50564, 307, 281, 519, 295, 476,
  87, 804, 3164, 293, 281, 519, 295, 445, 11, 50752], "temperature": 0.0, "avg_logprob":
  -0.1382564211648608, "compression_ratio": 1.7547892720306513, "no_speech_prob":
  4.4013890146743506e-05}, {"id": 86, "seek": 59670, "start": 604.46, "end": 606.82,
  "text": " when I''m trying to run a search for keywords.", "tokens": [50752, 562,
  286, 478, 1382, 281, 1190, 257, 3164, 337, 21009, 13, 50870], "temperature": 0.0,
  "avg_logprob": -0.1382564211648608, "compression_ratio": 1.7547892720306513, "no_speech_prob":
  4.4013890146743506e-05}, {"id": 87, "seek": 59670, "start": 606.82, "end": 613.1,
  "text": " So imagine you have a 1 million dimensional vector, not 768,", "tokens":
  [50870, 407, 3811, 291, 362, 257, 502, 2459, 18795, 8062, 11, 406, 1614, 27102,
  11, 51184], "temperature": 0.0, "avg_logprob": -0.1382564211648608, "compression_ratio":
  1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05}, {"id": 88, "seek":
  59670, "start": 613.1, "end": 614.74, "text": " but a million dimensions.", "tokens":
  [51184, 457, 257, 2459, 12819, 13, 51266], "temperature": 0.0, "avg_logprob": -0.1382564211648608,
  "compression_ratio": 1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05},
  {"id": 89, "seek": 59670, "start": 614.74, "end": 617.1400000000001, "text": " And
  every single one of those dimensions", "tokens": [51266, 400, 633, 2167, 472, 295,
  729, 12819, 51386], "temperature": 0.0, "avg_logprob": -0.1382564211648608, "compression_ratio":
  1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05}, {"id": 90, "seek":
  59670, "start": 617.1400000000001, "end": 620.74, "text": " corresponds to a term
  in your index,", "tokens": [51386, 23249, 281, 257, 1433, 294, 428, 8186, 11, 51566],
  "temperature": 0.0, "avg_logprob": -0.1382564211648608, "compression_ratio": 1.7547892720306513,
  "no_speech_prob": 4.4013890146743506e-05}, {"id": 91, "seek": 59670, "start": 620.74,
  "end": 622.38, "text": " where you''ve indexed all of your keywords.", "tokens":
  [51566, 689, 291, 600, 8186, 292, 439, 295, 428, 21009, 13, 51648], "temperature":
  0.0, "avg_logprob": -0.1382564211648608, "compression_ratio": 1.7547892720306513,
  "no_speech_prob": 4.4013890146743506e-05}, {"id": 92, "seek": 59670, "start": 622.38,
  "end": 624.26, "text": " And let''s just assume that there''s only a million terms",
  "tokens": [51648, 400, 718, 311, 445, 6552, 300, 456, 311, 787, 257, 2459, 2115,
  51742], "temperature": 0.0, "avg_logprob": -0.1382564211648608, "compression_ratio":
  1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05}, {"id": 93, "seek":
  59670, "start": 624.26, "end": 626.58, "text": " in your index.", "tokens": [51742,
  294, 428, 8186, 13, 51858], "temperature": 0.0, "avg_logprob": -0.1382564211648608,
  "compression_ratio": 1.7547892720306513, "no_speech_prob": 4.4013890146743506e-05},
  {"id": 94, "seek": 62658, "start": 626.58, "end": 630.9000000000001, "text": " If
  I wanted to represent latte as a query,", "tokens": [50364, 759, 286, 1415, 281,
  2906, 37854, 382, 257, 14581, 11, 50580], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 95, "seek": 62658, "start": 630.9000000000001, "end": 631.82, "text": " well,
  let me not do latte.", "tokens": [50580, 731, 11, 718, 385, 406, 360, 37854, 13,
  50626], "temperature": 0.0, "avg_logprob": -0.17519365824185884, "compression_ratio":
  1.7941176470588236, "no_speech_prob": 0.0010118169011548162}, {"id": 96, "seek":
  62658, "start": 631.82, "end": 634.5, "text": " Let me do a donut.", "tokens": [50626,
  961, 385, 360, 257, 33782, 13, 50760], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 97, "seek": 62658, "start": 634.5, "end": 636.7, "text": " If I want to represent
  donut as a query,", "tokens": [50760, 759, 286, 528, 281, 2906, 33782, 382, 257,
  14581, 11, 50870], "temperature": 0.0, "avg_logprob": -0.17519365824185884, "compression_ratio":
  1.7941176470588236, "no_speech_prob": 0.0010118169011548162}, {"id": 98, "seek":
  62658, "start": 636.7, "end": 640.7, "text": " then I can represent that as a vector
  with a million zeros", "tokens": [50870, 550, 286, 393, 2906, 300, 382, 257, 8062,
  365, 257, 2459, 35193, 51070], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 99, "seek": 62658, "start": 640.7, "end": 641.86, "text": " minus 1.", "tokens":
  [51070, 3175, 502, 13, 51128], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 100, "seek": 62658, "start": 641.86, "end": 645.14, "text": " And there''s
  a 1 in the column for donut,", "tokens": [51128, 400, 456, 311, 257, 502, 294, 264,
  7738, 337, 33782, 11, 51292], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 101, "seek": 62658, "start": 645.14, "end": 648.0200000000001, "text": "
  indicating that this is a million dimensional vector", "tokens": [51292, 25604,
  300, 341, 307, 257, 2459, 18795, 8062, 51436], "temperature": 0.0, "avg_logprob":
  -0.17519365824185884, "compression_ratio": 1.7941176470588236, "no_speech_prob":
  0.0010118169011548162}, {"id": 102, "seek": 62658, "start": 648.0200000000001, "end":
  650.9000000000001, "text": " with only one value represented.", "tokens": [51436,
  365, 787, 472, 2158, 10379, 13, 51580], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 103, "seek": 62658, "start": 650.9000000000001, "end": 655.26, "text": "
  And that''s whether the text donut appears", "tokens": [51580, 400, 300, 311, 1968,
  264, 2487, 33782, 7038, 51798], "temperature": 0.0, "avg_logprob": -0.17519365824185884,
  "compression_ratio": 1.7941176470588236, "no_speech_prob": 0.0010118169011548162},
  {"id": 104, "seek": 65526, "start": 655.26, "end": 659.38, "text": " within this
  document or query.", "tokens": [50364, 1951, 341, 4166, 420, 14581, 13, 50570],
  "temperature": 0.0, "avg_logprob": -0.1314561406119925, "compression_ratio": 1.7829787234042553,
  "no_speech_prob": 0.0004816131549887359}, {"id": 105, "seek": 65526, "start": 659.38,
  "end": 663.8199999999999, "text": " And so that''s a sparse vector, where it''s
  sparse", "tokens": [50570, 400, 370, 300, 311, 257, 637, 11668, 8062, 11, 689, 309,
  311, 637, 11668, 50792], "temperature": 0.0, "avg_logprob": -0.1314561406119925,
  "compression_ratio": 1.7829787234042553, "no_speech_prob": 0.0004816131549887359},
  {"id": 106, "seek": 65526, "start": 663.8199999999999, "end": 665.8199999999999,
  "text": " because most of the data is not filled.", "tokens": [50792, 570, 881,
  295, 264, 1412, 307, 406, 6412, 13, 50892], "temperature": 0.0, "avg_logprob": -0.1314561406119925,
  "compression_ratio": 1.7829787234042553, "no_speech_prob": 0.0004816131549887359},
  {"id": 107, "seek": 65526, "start": 665.8199999999999, "end": 669.1, "text": " And
  I have mostly zeros, but there''s some ones.", "tokens": [50892, 400, 286, 362,
  5240, 35193, 11, 457, 456, 311, 512, 2306, 13, 51056], "temperature": 0.0, "avg_logprob":
  -0.1314561406119925, "compression_ratio": 1.7829787234042553, "no_speech_prob":
  0.0004816131549887359}, {"id": 108, "seek": 65526, "start": 669.1, "end": 672.5,
  "text": " And of course, in this case, if I had the search for cheese pizza,", "tokens":
  [51056, 400, 295, 1164, 11, 294, 341, 1389, 11, 498, 286, 632, 264, 3164, 337, 5399,
  8298, 11, 51226], "temperature": 0.0, "avg_logprob": -0.1314561406119925, "compression_ratio":
  1.7829787234042553, "no_speech_prob": 0.0004816131549887359}, {"id": 109, "seek":
  65526, "start": 672.5, "end": 675.18, "text": " that vector would have two ones
  in it, one for cheese", "tokens": [51226, 300, 8062, 576, 362, 732, 2306, 294, 309,
  11, 472, 337, 5399, 51360], "temperature": 0.0, "avg_logprob": -0.1314561406119925,
  "compression_ratio": 1.7829787234042553, "no_speech_prob": 0.0004816131549887359},
  {"id": 110, "seek": 65526, "start": 675.18, "end": 676.42, "text": " and one for
  pizza.", "tokens": [51360, 293, 472, 337, 8298, 13, 51422], "temperature": 0.0,
  "avg_logprob": -0.1314561406119925, "compression_ratio": 1.7829787234042553, "no_speech_prob":
  0.0004816131549887359}, {"id": 111, "seek": 65526, "start": 676.42, "end": 679.8199999999999,
  "text": " So it''s a million dimensional vector with two ones in it.", "tokens":
  [51422, 407, 309, 311, 257, 2459, 18795, 8062, 365, 732, 2306, 294, 309, 13, 51592],
  "temperature": 0.0, "avg_logprob": -0.1314561406119925, "compression_ratio": 1.7829787234042553,
  "no_speech_prob": 0.0004816131549887359}, {"id": 112, "seek": 65526, "start": 679.8199999999999,
  "end": 683.8199999999999, "text": " This is just as valid as a vector, as a dense
  vector,", "tokens": [51592, 639, 307, 445, 382, 7363, 382, 257, 8062, 11, 382, 257,
  18011, 8062, 11, 51792], "temperature": 0.0, "avg_logprob": -0.1314561406119925,
  "compression_ratio": 1.7829787234042553, "no_speech_prob": 0.0004816131549887359},
  {"id": 113, "seek": 68382, "start": 683.82, "end": 686.22, "text": " with only 738
  dimensions.", "tokens": [50364, 365, 787, 1614, 12625, 12819, 13, 50484], "temperature":
  0.0, "avg_logprob": -0.16312205684077632, "compression_ratio": 1.7066115702479339,
  "no_speech_prob": 0.0014139787526801229}, {"id": 114, "seek": 68382, "start": 686.22,
  "end": 689.3000000000001, "text": " But what we typically do, when we start", "tokens":
  [50484, 583, 437, 321, 5850, 360, 11, 562, 321, 722, 50638], "temperature": 0.0,
  "avg_logprob": -0.16312205684077632, "compression_ratio": 1.7066115702479339, "no_speech_prob":
  0.0014139787526801229}, {"id": 115, "seek": 68382, "start": 689.3000000000001, "end":
  693.22, "text": " to move from lexical matching, where we can match on those", "tokens":
  [50638, 281, 1286, 490, 476, 87, 804, 14324, 11, 689, 321, 393, 2995, 322, 729,
  50834], "temperature": 0.0, "avg_logprob": -0.16312205684077632, "compression_ratio":
  1.7066115702479339, "no_speech_prob": 0.0014139787526801229}, {"id": 116, "seek":
  68382, "start": 693.22, "end": 696.46, "text": " yes or no ones or zeros in an inverted
  index,", "tokens": [50834, 2086, 420, 572, 2306, 420, 35193, 294, 364, 38969, 8186,
  11, 50996], "temperature": 0.0, "avg_logprob": -0.16312205684077632, "compression_ratio":
  1.7066115702479339, "no_speech_prob": 0.0014139787526801229}, {"id": 117, "seek":
  68382, "start": 696.46, "end": 699.7, "text": " what we typically do when we move
  to doing semantic search", "tokens": [50996, 437, 321, 5850, 360, 562, 321, 1286,
  281, 884, 47982, 3164, 51158], "temperature": 0.0, "avg_logprob": -0.16312205684077632,
  "compression_ratio": 1.7066115702479339, "no_speech_prob": 0.0014139787526801229},
  {"id": 118, "seek": 68382, "start": 699.7, "end": 702.1400000000001, "text": " is
  we focus on a much smaller number of dimensions.", "tokens": [51158, 307, 321, 1879,
  322, 257, 709, 4356, 1230, 295, 12819, 13, 51280], "temperature": 0.0, "avg_logprob":
  -0.16312205684077632, "compression_ratio": 1.7066115702479339, "no_speech_prob":
  0.0014139787526801229}, {"id": 119, "seek": 68382, "start": 702.1400000000001, "end":
  705.1400000000001, "text": " And so conceptually, as an embedding here,", "tokens":
  [51280, 400, 370, 3410, 671, 11, 382, 364, 12240, 3584, 510, 11, 51430], "temperature":
  0.0, "avg_logprob": -0.16312205684077632, "compression_ratio": 1.7066115702479339,
  "no_speech_prob": 0.0014139787526801229}, {"id": 120, "seek": 68382, "start": 705.1400000000001,
  "end": 708.2600000000001, "text": " what I have is eight dimensions.", "tokens":
  [51430, 437, 286, 362, 307, 3180, 12819, 13, 51586], "temperature": 0.0, "avg_logprob":
  -0.16312205684077632, "compression_ratio": 1.7066115702479339, "no_speech_prob":
  0.0014139787526801229}, {"id": 121, "seek": 68382, "start": 708.2600000000001, "end":
  710.9000000000001, "text": " Each of these items that I showed on the previous slide",
  "tokens": [51586, 6947, 295, 613, 4754, 300, 286, 4712, 322, 264, 3894, 4137, 51718],
  "temperature": 0.0, "avg_logprob": -0.16312205684077632, "compression_ratio": 1.7066115702479339,
  "no_speech_prob": 0.0014139787526801229}, {"id": 122, "seek": 71090, "start": 710.9399999999999,
  "end": 714.62, "text": " has dimensions indicating whether it''s food,", "tokens":
  [50366, 575, 12819, 25604, 1968, 309, 311, 1755, 11, 50550], "temperature": 0.0,
  "avg_logprob": -0.12700746259616533, "compression_ratio": 2.0088105726872247, "no_speech_prob":
  0.01598554477095604}, {"id": 123, "seek": 71090, "start": 714.62, "end": 718.66,
  "text": " whether it''s a drink, how much dairy it has, is it bread,", "tokens":
  [50550, 1968, 309, 311, 257, 2822, 11, 577, 709, 21276, 309, 575, 11, 307, 309,
  5961, 11, 50752], "temperature": 0.0, "avg_logprob": -0.12700746259616533, "compression_ratio":
  2.0088105726872247, "no_speech_prob": 0.01598554477095604}, {"id": 124, "seek":
  71090, "start": 718.66, "end": 721.14, "text": " is it caffeine, sweet, calories,
  healthy, et cetera.", "tokens": [50752, 307, 309, 31261, 11, 3844, 11, 14904, 11,
  4627, 11, 1030, 11458, 13, 50876], "temperature": 0.0, "avg_logprob": -0.12700746259616533,
  "compression_ratio": 2.0088105726872247, "no_speech_prob": 0.01598554477095604},
  {"id": 125, "seek": 71090, "start": 721.14, "end": 724.4599999999999, "text": "
  So you can see apple juice now is not represented as,", "tokens": [50876, 407, 291,
  393, 536, 10606, 8544, 586, 307, 406, 10379, 382, 11, 51042], "temperature": 0.0,
  "avg_logprob": -0.12700746259616533, "compression_ratio": 2.0088105726872247, "no_speech_prob":
  0.01598554477095604}, {"id": 126, "seek": 71090, "start": 724.4599999999999, "end":
  726.42, "text": " it has the word apple and it has the word juice,", "tokens": [51042,
  309, 575, 264, 1349, 10606, 293, 309, 575, 264, 1349, 8544, 11, 51140], "temperature":
  0.0, "avg_logprob": -0.12700746259616533, "compression_ratio": 2.0088105726872247,
  "no_speech_prob": 0.01598554477095604}, {"id": 127, "seek": 71090, "start": 726.42,
  "end": 729.98, "text": " but it''s represented as very much not food,", "tokens":
  [51140, 457, 309, 311, 10379, 382, 588, 709, 406, 1755, 11, 51318], "temperature":
  0.0, "avg_logprob": -0.12700746259616533, "compression_ratio": 2.0088105726872247,
  "no_speech_prob": 0.01598554477095604}, {"id": 128, "seek": 71090, "start": 729.98,
  "end": 733.9399999999999, "text": " very much a drink, no dairy, no bread, no caffeine,",
  "tokens": [51318, 588, 709, 257, 2822, 11, 572, 21276, 11, 572, 5961, 11, 572, 31261,
  11, 51516], "temperature": 0.0, "avg_logprob": -0.12700746259616533, "compression_ratio":
  2.0088105726872247, "no_speech_prob": 0.01598554477095604}, {"id": 129, "seek":
  71090, "start": 733.9399999999999, "end": 736.22, "text": " very high on sweet,
  but not all the way up,", "tokens": [51516, 588, 1090, 322, 3844, 11, 457, 406,
  439, 264, 636, 493, 11, 51630], "temperature": 0.0, "avg_logprob": -0.12700746259616533,
  "compression_ratio": 2.0088105726872247, "no_speech_prob": 0.01598554477095604},
  {"id": 130, "seek": 71090, "start": 736.22, "end": 739.38, "text": " very high on
  calories, but all the way up and in between,", "tokens": [51630, 588, 1090, 322,
  14904, 11, 457, 439, 264, 636, 493, 293, 294, 1296, 11, 51788], "temperature": 0.0,
  "avg_logprob": -0.12700746259616533, "compression_ratio": 2.0088105726872247, "no_speech_prob":
  0.01598554477095604}, {"id": 131, "seek": 73938, "start": 739.38, "end": 743.22,
  "text": " but kind of sort of healthy, but not really.", "tokens": [50364, 457,
  733, 295, 1333, 295, 4627, 11, 457, 406, 534, 13, 50556], "temperature": 0.0, "avg_logprob":
  -0.1634188982156607, "compression_ratio": 1.6804979253112033, "no_speech_prob":
  0.00027289101853966713}, {"id": 132, "seek": 73938, "start": 743.22, "end": 745.46,
  "text": " And then same thing, cheese bread sticks,", "tokens": [50556, 400, 550,
  912, 551, 11, 5399, 5961, 12518, 11, 50668], "temperature": 0.0, "avg_logprob":
  -0.1634188982156607, "compression_ratio": 1.6804979253112033, "no_speech_prob":
  0.00027289101853966713}, {"id": 133, "seek": 73938, "start": 745.46, "end": 748.66,
  "text": " very much food, not a drink, good bit of dairy,", "tokens": [50668, 588,
  709, 1755, 11, 406, 257, 2822, 11, 665, 857, 295, 21276, 11, 50828], "temperature":
  0.0, "avg_logprob": -0.1634188982156607, "compression_ratio": 1.6804979253112033,
  "no_speech_prob": 0.00027289101853966713}, {"id": 134, "seek": 73938, "start": 748.66,
  "end": 751.34, "text": " very much bread, no caffeine, you get the idea.", "tokens":
  [50828, 588, 709, 5961, 11, 572, 31261, 11, 291, 483, 264, 1558, 13, 50962], "temperature":
  0.0, "avg_logprob": -0.1634188982156607, "compression_ratio": 1.6804979253112033,
  "no_speech_prob": 0.00027289101853966713}, {"id": 135, "seek": 73938, "start": 751.34,
  "end": 755.42, "text": " These map in the attributes are the dimensions", "tokens":
  [50962, 1981, 4471, 294, 264, 17212, 366, 264, 12819, 51166], "temperature": 0.0,
  "avg_logprob": -0.1634188982156607, "compression_ratio": 1.6804979253112033, "no_speech_prob":
  0.00027289101853966713}, {"id": 136, "seek": 73938, "start": 755.42, "end": 758.34,
  "text": " of these concepts over here by representing them", "tokens": [51166, 295,
  613, 10392, 670, 510, 538, 13460, 552, 51312], "temperature": 0.0, "avg_logprob":
  -0.1634188982156607, "compression_ratio": 1.6804979253112033, "no_speech_prob":
  0.00027289101853966713}, {"id": 137, "seek": 73938, "start": 758.34, "end": 759.82,
  "text": " in these eight dimensions.", "tokens": [51312, 294, 613, 3180, 12819,
  13, 51386], "temperature": 0.0, "avg_logprob": -0.1634188982156607, "compression_ratio":
  1.6804979253112033, "no_speech_prob": 0.00027289101853966713}, {"id": 138, "seek":
  73938, "start": 759.82, "end": 764.46, "text": " And in search, what we typically
  do is we represent documents", "tokens": [51386, 400, 294, 3164, 11, 437, 321, 5850,
  360, 307, 321, 2906, 8512, 51618], "temperature": 0.0, "avg_logprob": -0.1634188982156607,
  "compression_ratio": 1.6804979253112033, "no_speech_prob": 0.00027289101853966713},
  {"id": 139, "seek": 73938, "start": 764.46, "end": 767.58, "text": " and queries
  leveraging these vectors,", "tokens": [51618, 293, 24109, 32666, 613, 18875, 11,
  51774], "temperature": 0.0, "avg_logprob": -0.1634188982156607, "compression_ratio":
  1.6804979253112033, "no_speech_prob": 0.00027289101853966713}, {"id": 140, "seek":
  76758, "start": 767.58, "end": 771.46, "text": " and then we do some sort of vector
  similarity calculation", "tokens": [50364, 293, 550, 321, 360, 512, 1333, 295, 8062,
  32194, 17108, 50558], "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio":
  1.8464566929133859, "no_speech_prob": 0.00037480180617421865}, {"id": 141, "seek":
  76758, "start": 771.46, "end": 774.5, "text": " in order to say how later similar
  things are.", "tokens": [50558, 294, 1668, 281, 584, 577, 1780, 2531, 721, 366,
  13, 50710], "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio":
  1.8464566929133859, "no_speech_prob": 0.00037480180617421865}, {"id": 142, "seek":
  76758, "start": 774.5, "end": 777.14, "text": " So if I were to, for example, take
  the vector", "tokens": [50710, 407, 498, 286, 645, 281, 11, 337, 1365, 11, 747,
  264, 8062, 50842], "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio":
  1.8464566929133859, "no_speech_prob": 0.00037480180617421865}, {"id": 143, "seek":
  76758, "start": 777.14, "end": 781.1800000000001, "text": " over here for cheese
  pizza, and I were to then do a cosine", "tokens": [50842, 670, 510, 337, 5399, 8298,
  11, 293, 286, 645, 281, 550, 360, 257, 23565, 51044], "temperature": 0.0, "avg_logprob":
  -0.11309589717699134, "compression_ratio": 1.8464566929133859, "no_speech_prob":
  0.00037480180617421865}, {"id": 144, "seek": 76758, "start": 781.1800000000001,
  "end": 784.4200000000001, "text": " similarity between that vector and every other
  vector,", "tokens": [51044, 32194, 1296, 300, 8062, 293, 633, 661, 8062, 11, 51206],
  "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio": 1.8464566929133859,
  "no_speech_prob": 0.00037480180617421865}, {"id": 145, "seek": 76758, "start": 784.4200000000001,
  "end": 788.0600000000001, "text": " I would see that cheese bread sticks have a
  very high", "tokens": [51206, 286, 576, 536, 300, 5399, 5961, 12518, 362, 257, 588,
  1090, 51388], "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio":
  1.8464566929133859, "no_speech_prob": 0.00037480180617421865}, {"id": 146, "seek":
  76758, "start": 788.0600000000001, "end": 790.82, "text": " similarity followed
  by cinnamon bread sticks,", "tokens": [51388, 32194, 6263, 538, 22969, 5961, 12518,
  11, 51526], "temperature": 0.0, "avg_logprob": -0.11309589717699134, "compression_ratio":
  1.8464566929133859, "no_speech_prob": 0.00037480180617421865}, {"id": 147, "seek":
  76758, "start": 790.82, "end": 792.86, "text": " followed by doughnut, all the way
  down to water.", "tokens": [51526, 6263, 538, 7984, 18316, 11, 439, 264, 636, 760,
  281, 1281, 13, 51628], "temperature": 0.0, "avg_logprob": -0.11309589717699134,
  "compression_ratio": 1.8464566929133859, "no_speech_prob": 0.00037480180617421865},
  {"id": 148, "seek": 76758, "start": 792.86, "end": 796.1, "text": " So these are
  essentially ranked based upon cheese pizza,", "tokens": [51628, 407, 613, 366, 4476,
  20197, 2361, 3564, 5399, 8298, 11, 51790], "temperature": 0.0, "avg_logprob": -0.11309589717699134,
  "compression_ratio": 1.8464566929133859, "no_speech_prob": 0.00037480180617421865},
  {"id": 149, "seek": 79610, "start": 796.1, "end": 797.9, "text": " these are the
  cheesiest, breadiest,", "tokens": [50364, 613, 366, 264, 947, 279, 6495, 11, 5961,
  6495, 11, 50454], "temperature": 0.0, "avg_logprob": -0.177269571976696, "compression_ratio":
  1.8473895582329318, "no_speech_prob": 0.00041461861110292375}, {"id": 150, "seek":
  79610, "start": 797.9, "end": 801.38, "text": " unhealthiest, non-drinkiest things
  at the top.", "tokens": [50454, 517, 19225, 6495, 11, 2107, 12, 16753, 475, 6495,
  721, 412, 264, 1192, 13, 50628], "temperature": 0.0, "avg_logprob": -0.177269571976696,
  "compression_ratio": 1.8473895582329318, "no_speech_prob": 0.00041461861110292375},
  {"id": 151, "seek": 79610, "start": 801.38, "end": 805.7, "text": " This is still
  very, very non-drinky,", "tokens": [50628, 639, 307, 920, 588, 11, 588, 2107, 12,
  16753, 22998, 11, 50844], "temperature": 0.0, "avg_logprob": -0.177269571976696,
  "compression_ratio": 1.8473895582329318, "no_speech_prob": 0.00041461861110292375},
  {"id": 152, "seek": 79610, "start": 805.7, "end": 808.22, "text": " not very healthy
  here, ranked all the way down to it.", "tokens": [50844, 406, 588, 4627, 510, 11,
  20197, 439, 264, 636, 760, 281, 309, 13, 50970], "temperature": 0.0, "avg_logprob":
  -0.177269571976696, "compression_ratio": 1.8473895582329318, "no_speech_prob": 0.00041461861110292375},
  {"id": 153, "seek": 79610, "start": 808.22, "end": 810.38, "text": " It''s essentially
  opposite in this vector space,", "tokens": [50970, 467, 311, 4476, 6182, 294, 341,
  8062, 1901, 11, 51078], "temperature": 0.0, "avg_logprob": -0.177269571976696, "compression_ratio":
  1.8473895582329318, "no_speech_prob": 0.00041461861110292375}, {"id": 154, "seek":
  79610, "start": 810.38, "end": 811.74, "text": " which is water, which is all the
  way", "tokens": [51078, 597, 307, 1281, 11, 597, 307, 439, 264, 636, 51146], "temperature":
  0.0, "avg_logprob": -0.177269571976696, "compression_ratio": 1.8473895582329318,
  "no_speech_prob": 0.00041461861110292375}, {"id": 155, "seek": 79610, "start": 811.74,
  "end": 813.1800000000001, "text": " on the other end of the spectrum.", "tokens":
  [51146, 322, 264, 661, 917, 295, 264, 11143, 13, 51218], "temperature": 0.0, "avg_logprob":
  -0.177269571976696, "compression_ratio": 1.8473895582329318, "no_speech_prob": 0.00041461861110292375},
  {"id": 156, "seek": 79610, "start": 813.1800000000001, "end": 815.5400000000001,
  "text": " Same thing with green tea, very similar to water,", "tokens": [51218,
  10635, 551, 365, 3092, 5817, 11, 588, 2531, 281, 1281, 11, 51336], "temperature":
  0.0, "avg_logprob": -0.177269571976696, "compression_ratio": 1.8473895582329318,
  "no_speech_prob": 0.00041461861110292375}, {"id": 157, "seek": 79610, "start": 815.5400000000001,
  "end": 820.86, "text": " cappuccino latte, healthy, no calories drink,", "tokens":
  [51336, 1335, 427, 39407, 2982, 37854, 11, 4627, 11, 572, 14904, 2822, 11, 51602],
  "temperature": 0.0, "avg_logprob": -0.177269571976696, "compression_ratio": 1.8473895582329318,
  "no_speech_prob": 0.00041461861110292375}, {"id": 158, "seek": 79610, "start": 820.86,
  "end": 824.34, "text": " all the way down to a very unhealthy, very not drink.",
  "tokens": [51602, 439, 264, 636, 760, 281, 257, 588, 29147, 11, 588, 406, 2822,
  13, 51776], "temperature": 0.0, "avg_logprob": -0.177269571976696, "compression_ratio":
  1.8473895582329318, "no_speech_prob": 0.00041461861110292375}, {"id": 159, "seek":
  79610, "start": 824.34, "end": 825.14, "text": " You get the idea.", "tokens": [51776,
  509, 483, 264, 1558, 13, 51816], "temperature": 0.0, "avg_logprob": -0.177269571976696,
  "compression_ratio": 1.8473895582329318, "no_speech_prob": 0.00041461861110292375},
  {"id": 160, "seek": 82514, "start": 825.14, "end": 829.02, "text": " So that''s
  essentially in a semantic vector space,", "tokens": [50364, 407, 300, 311, 4476,
  294, 257, 47982, 8062, 1901, 11, 50558], "temperature": 0.0, "avg_logprob": -0.14254786825587606,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.00014917526277713478},
  {"id": 161, "seek": 82514, "start": 829.02, "end": 831.62, "text": " things span
  across these dimensions,", "tokens": [50558, 721, 16174, 2108, 613, 12819, 11, 50688],
  "temperature": 0.0, "avg_logprob": -0.14254786825587606, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.00014917526277713478}, {"id": 162, "seek": 82514, "start": 831.62,
  "end": 834.62, "text": " and they fit at different places along,", "tokens": [50688,
  293, 436, 3318, 412, 819, 3190, 2051, 11, 50838], "temperature": 0.0, "avg_logprob":
  -0.14254786825587606, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.00014917526277713478}, {"id": 163, "seek": 82514, "start": 834.62, "end": 836.54,
  "text": " within the vector space, that corresponds", "tokens": [50838, 1951, 264,
  8062, 1901, 11, 300, 23249, 50934], "temperature": 0.0, "avg_logprob": -0.14254786825587606,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.00014917526277713478},
  {"id": 164, "seek": 82514, "start": 836.54, "end": 839.26, "text": " to the meaning
  of these attributes.", "tokens": [50934, 281, 264, 3620, 295, 613, 17212, 13, 51070],
  "temperature": 0.0, "avg_logprob": -0.14254786825587606, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.00014917526277713478}, {"id": 165, "seek": 82514, "start": 839.26,
  "end": 841.74, "text": " Now, when we deal with transformers,", "tokens": [51070,
  823, 11, 562, 321, 2028, 365, 4088, 433, 11, 51194], "temperature": 0.0, "avg_logprob":
  -0.14254786825587606, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.00014917526277713478}, {"id": 166, "seek": 82514, "start": 841.74, "end": 843.54,
  "text": " which we get from all the LLMs today", "tokens": [51194, 597, 321, 483,
  490, 439, 264, 441, 43, 26386, 965, 51284], "temperature": 0.0, "avg_logprob": -0.14254786825587606,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.00014917526277713478},
  {"id": 167, "seek": 82514, "start": 843.54, "end": 845.98, "text": " that we''re
  leveraging for vector search,", "tokens": [51284, 300, 321, 434, 32666, 337, 8062,
  3164, 11, 51406], "temperature": 0.0, "avg_logprob": -0.14254786825587606, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.00014917526277713478}, {"id": 168, "seek":
  82514, "start": 845.98, "end": 848.62, "text": " these don''t use explicit features,",
  "tokens": [51406, 613, 500, 380, 764, 13691, 4122, 11, 51538], "temperature": 0.0,
  "avg_logprob": -0.14254786825587606, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.00014917526277713478}, {"id": 169, "seek": 82514, "start": 848.62, "end": 851.74,
  "text": " like we have here, food, drink, dairy, bread, et cetera.", "tokens": [51538,
  411, 321, 362, 510, 11, 1755, 11, 2822, 11, 21276, 11, 5961, 11, 1030, 11458, 13,
  51694], "temperature": 0.0, "avg_logprob": -0.14254786825587606, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.00014917526277713478}, {"id": 170, "seek":
  82514, "start": 851.74, "end": 853.22, "text": " They use latent features.", "tokens":
  [51694, 814, 764, 48994, 4122, 13, 51768], "temperature": 0.0, "avg_logprob": -0.14254786825587606,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.00014917526277713478},
  {"id": 171, "seek": 85322, "start": 853.22, "end": 855.46, "text": " And latent
  just means sort of hidden,", "tokens": [50364, 400, 48994, 445, 1355, 1333, 295,
  7633, 11, 50476], "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 4.148954030824825e-05}, {"id": 172, "seek":
  85322, "start": 855.46, "end": 857.1, "text": " or another way to put it is,", "tokens":
  [50476, 420, 1071, 636, 281, 829, 309, 307, 11, 50558], "temperature": 0.0, "avg_logprob":
  -0.12584982094941316, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  4.148954030824825e-05}, {"id": 173, "seek": 85322, "start": 857.1, "end": 859.6600000000001,
  "text": " the dimensions don''t correspond one to one", "tokens": [50558, 264, 12819,
  500, 380, 6805, 472, 281, 472, 50686], "temperature": 0.0, "avg_logprob": -0.12584982094941316,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 4.148954030824825e-05},
  {"id": 174, "seek": 85322, "start": 859.6600000000001, "end": 861.1800000000001,
  "text": " with particular attributes.", "tokens": [50686, 365, 1729, 17212, 13,
  50762], "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 4.148954030824825e-05}, {"id": 175, "seek":
  85322, "start": 861.1800000000001, "end": 864.26, "text": " It''s combinations of
  those dimensions together", "tokens": [50762, 467, 311, 21267, 295, 729, 12819,
  1214, 50916], "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 4.148954030824825e-05}, {"id": 176, "seek":
  85322, "start": 864.26, "end": 865.94, "text": " that they give us our meaning.",
  "tokens": [50916, 300, 436, 976, 505, 527, 3620, 13, 51000], "temperature": 0.0,
  "avg_logprob": -0.12584982094941316, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  4.148954030824825e-05}, {"id": 177, "seek": 85322, "start": 865.94, "end": 870.5,
  "text": " And so to think of that visually,", "tokens": [51000, 400, 370, 281, 519,
  295, 300, 19622, 11, 51228], "temperature": 0.0, "avg_logprob": -0.12584982094941316,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 4.148954030824825e-05},
  {"id": 178, "seek": 85322, "start": 870.5, "end": 872.82, "text": " if I were to
  create an embedding space,", "tokens": [51228, 498, 286, 645, 281, 1884, 364, 12240,
  3584, 1901, 11, 51344], "temperature": 0.0, "avg_logprob": -0.12584982094941316,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 4.148954030824825e-05},
  {"id": 179, "seek": 85322, "start": 872.82, "end": 874.4200000000001, "text": "
  and this is obviously flattened,", "tokens": [51344, 293, 341, 307, 2745, 24183,
  292, 11, 51424], "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 4.148954030824825e-05}, {"id": 180, "seek":
  85322, "start": 874.4200000000001, "end": 876.62, "text": " there could be thousands
  and thousands of dimensions", "tokens": [51424, 456, 727, 312, 5383, 293, 5383,
  295, 12819, 51534], "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 4.148954030824825e-05}, {"id": 181, "seek":
  85322, "start": 876.62, "end": 880.02, "text": " or hundreds, but in this vector
  space,", "tokens": [51534, 420, 6779, 11, 457, 294, 341, 8062, 1901, 11, 51704],
  "temperature": 0.0, "avg_logprob": -0.12584982094941316, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 4.148954030824825e-05}, {"id": 182, "seek": 88002, "start": 880.02,
  "end": 883.5799999999999, "text": " if these are all of the embeddings that I have,",
  "tokens": [50364, 498, 613, 366, 439, 295, 264, 12240, 29432, 300, 286, 362, 11,
  50542], "temperature": 0.0, "avg_logprob": -0.11100775400797526, "compression_ratio":
  1.772563176895307, "no_speech_prob": 0.000533765705768019}, {"id": 183, "seek":
  88002, "start": 883.5799999999999, "end": 887.78, "text": " and I would assert for
  the phrase Darth Vader,", "tokens": [50542, 293, 286, 576, 19810, 337, 264, 9535,
  40696, 36337, 11, 50752], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 184, "seek": 88002, "start": 887.78, "end": 889.66, "text": " turn that into
  an embedding and match it,", "tokens": [50752, 1261, 300, 666, 364, 12240, 3584,
  293, 2995, 309, 11, 50846], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 185, "seek": 88002, "start": 889.66, "end": 891.06, "text": " you''ll see
  that over here on the right,", "tokens": [50846, 291, 603, 536, 300, 670, 510, 322,
  264, 558, 11, 50916], "temperature": 0.0, "avg_logprob": -0.11100775400797526, "compression_ratio":
  1.772563176895307, "no_speech_prob": 0.000533765705768019}, {"id": 186, "seek":
  88002, "start": 891.06, "end": 893.5, "text": " I have a cluster of meaning associated",
  "tokens": [50916, 286, 362, 257, 13630, 295, 3620, 6615, 51038], "temperature":
  0.0, "avg_logprob": -0.11100775400797526, "compression_ratio": 1.772563176895307,
  "no_speech_prob": 0.000533765705768019}, {"id": 187, "seek": 88002, "start": 893.5,
  "end": 895.06, "text": " with the search for Darth Vader.", "tokens": [51038, 365,
  264, 3164, 337, 40696, 36337, 13, 51116], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 188, "seek": 88002, "start": 895.06, "end": 896.98, "text": " Now, there''s
  some other points in various places,", "tokens": [51116, 823, 11, 456, 311, 512,
  661, 2793, 294, 3683, 3190, 11, 51212], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 189, "seek": 88002, "start": 896.98, "end": 900.62, "text": " but if I were
  to look at the items in this cluster,", "tokens": [51212, 457, 498, 286, 645, 281,
  574, 412, 264, 4754, 294, 341, 13630, 11, 51394], "temperature": 0.0, "avg_logprob":
  -0.11100775400797526, "compression_ratio": 1.772563176895307, "no_speech_prob":
  0.000533765705768019}, {"id": 190, "seek": 88002, "start": 900.62, "end": 902.34,
  "text": " I see pictures of Darth Vader,", "tokens": [51394, 286, 536, 5242, 295,
  40696, 36337, 11, 51480], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 191, "seek": 88002, "start": 902.34, "end": 903.74, "text": " which is what
  I would expect,", "tokens": [51480, 597, 307, 437, 286, 576, 2066, 11, 51550], "temperature":
  0.0, "avg_logprob": -0.11100775400797526, "compression_ratio": 1.772563176895307,
  "no_speech_prob": 0.000533765705768019}, {"id": 192, "seek": 88002, "start": 903.74,
  "end": 905.62, "text": " because the meaning of Darth Vader", "tokens": [51550,
  570, 264, 3620, 295, 40696, 36337, 51644], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 193, "seek": 88002, "start": 905.62, "end": 908.42, "text": " is essentially
  in this area of vector space.", "tokens": [51644, 307, 4476, 294, 341, 1859, 295,
  8062, 1901, 13, 51784], "temperature": 0.0, "avg_logprob": -0.11100775400797526,
  "compression_ratio": 1.772563176895307, "no_speech_prob": 0.000533765705768019},
  {"id": 194, "seek": 90842, "start": 908.42, "end": 911.9, "text": " Similarly, if
  I were to search for Puppy,", "tokens": [50364, 13157, 11, 498, 286, 645, 281, 3164,
  337, 13605, 7966, 11, 50538], "temperature": 0.0, "avg_logprob": -0.21191672908449635,
  "compression_ratio": 1.5867768595041323, "no_speech_prob": 0.00018618193280417472},
  {"id": 195, "seek": 90842, "start": 911.9, "end": 914.3399999999999, "text": " then
  this cluster of meaning right here", "tokens": [50538, 550, 341, 13630, 295, 3620,
  558, 510, 50660], "temperature": 0.0, "avg_logprob": -0.21191672908449635, "compression_ratio":
  1.5867768595041323, "no_speech_prob": 0.00018618193280417472}, {"id": 196, "seek":
  90842, "start": 914.3399999999999, "end": 916.06, "text": " corresponds with puppies
  and d,", "tokens": [50660, 23249, 365, 33734, 293, 274, 11, 50746], "temperature":
  0.0, "avg_logprob": -0.21191672908449635, "compression_ratio": 1.5867768595041323,
  "no_speech_prob": 0.00018618193280417472}, {"id": 197, "seek": 90842, "start": 916.06,
  "end": 918.14, "text": " I see pictures of puppies.", "tokens": [50746, 286, 536,
  5242, 295, 33734, 13, 50850], "temperature": 0.0, "avg_logprob": -0.21191672908449635,
  "compression_ratio": 1.5867768595041323, "no_speech_prob": 0.00018618193280417472},
  {"id": 198, "seek": 90842, "start": 918.14, "end": 920.9799999999999, "text": "
  So the interesting question arises,", "tokens": [50850, 407, 264, 1880, 1168, 27388,
  11, 50992], "temperature": 0.0, "avg_logprob": -0.21191672908449635, "compression_ratio":
  1.5867768595041323, "no_speech_prob": 0.00018618193280417472}, {"id": 199, "seek":
  90842, "start": 920.9799999999999, "end": 922.66, "text": " when I ask what happens,",
  "tokens": [50992, 562, 286, 1029, 437, 2314, 11, 51076], "temperature": 0.0, "avg_logprob":
  -0.21191672908449635, "compression_ratio": 1.5867768595041323, "no_speech_prob":
  0.00018618193280417472}, {"id": 200, "seek": 90842, "start": 922.66, "end": 927.54,
  "text": " if I were to find the midpoint between Puppy and Darth Vader", "tokens":
  [51076, 498, 286, 645, 281, 915, 264, 2062, 6053, 1296, 13605, 7966, 293, 40696,
  36337, 51320], "temperature": 0.0, "avg_logprob": -0.21191672908449635, "compression_ratio":
  1.5867768595041323, "no_speech_prob": 0.00018618193280417472}, {"id": 201, "seek":
  90842, "start": 927.54, "end": 929.42, "text": " in this semantic vector space?",
  "tokens": [51320, 294, 341, 47982, 8062, 1901, 30, 51414], "temperature": 0.0, "avg_logprob":
  -0.21191672908449635, "compression_ratio": 1.5867768595041323, "no_speech_prob":
  0.00018618193280417472}, {"id": 202, "seek": 90842, "start": 933.02, "end": 934.18,
  "text": " People have different intuitions", "tokens": [51594, 3432, 362, 819, 16224,
  626, 51652], "temperature": 0.0, "avg_logprob": -0.21191672908449635, "compression_ratio":
  1.5867768595041323, "no_speech_prob": 0.00018618193280417472}, {"id": 203, "seek":
  90842, "start": 934.18, "end": 935.9, "text": " about what actually happens here.",
  "tokens": [51652, 466, 437, 767, 2314, 510, 13, 51738], "temperature": 0.0, "avg_logprob":
  -0.21191672908449635, "compression_ratio": 1.5867768595041323, "no_speech_prob":
  0.00018618193280417472}, {"id": 204, "seek": 90842, "start": 935.9, "end": 936.9399999999999,
  "text": " Some people think it''s,", "tokens": [51738, 2188, 561, 519, 309, 311,
  11, 51790], "temperature": 0.0, "avg_logprob": -0.21191672908449635, "compression_ratio":
  1.5867768595041323, "no_speech_prob": 0.00018618193280417472}, {"id": 205, "seek":
  93694, "start": 936.94, "end": 939.1, "text": " I don''t know what I would find
  in the middle,", "tokens": [50364, 286, 500, 380, 458, 437, 286, 576, 915, 294,
  264, 2808, 11, 50472], "temperature": 0.0, "avg_logprob": -0.12856858352134967,
  "compression_ratio": 2.015810276679842, "no_speech_prob": 0.0029177896212786436},
  {"id": 206, "seek": 93694, "start": 939.1, "end": 942.1800000000001, "text": " but
  the answer is if this vector space is properly constructed,", "tokens": [50472,
  457, 264, 1867, 307, 498, 341, 8062, 1901, 307, 6108, 17083, 11, 50626], "temperature":
  0.0, "avg_logprob": -0.12856858352134967, "compression_ratio": 2.015810276679842,
  "no_speech_prob": 0.0029177896212786436}, {"id": 207, "seek": 93694, "start": 942.1800000000001,
  "end": 944.7800000000001, "text": " so that the semantic meaning is represented,",
  "tokens": [50626, 370, 300, 264, 47982, 3620, 307, 10379, 11, 50756], "temperature":
  0.0, "avg_logprob": -0.12856858352134967, "compression_ratio": 2.015810276679842,
  "no_speech_prob": 0.0029177896212786436}, {"id": 208, "seek": 93694, "start": 944.7800000000001,
  "end": 947.74, "text": " i.e., the further away I get from this point,", "tokens":
  [50756, 741, 13, 68, 7933, 264, 3052, 1314, 286, 483, 490, 341, 935, 11, 50904],
  "temperature": 0.0, "avg_logprob": -0.12856858352134967, "compression_ratio": 2.015810276679842,
  "no_speech_prob": 0.0029177896212786436}, {"id": 209, "seek": 93694, "start": 947.74,
  "end": 949.1400000000001, "text": " the more I get away from dog,", "tokens": [50904,
  264, 544, 286, 483, 1314, 490, 3000, 11, 50974], "temperature": 0.0, "avg_logprob":
  -0.12856858352134967, "compression_ratio": 2.015810276679842, "no_speech_prob":
  0.0029177896212786436}, {"id": 210, "seek": 93694, "start": 949.1400000000001, "end":
  950.6600000000001, "text": " the further away I get from this,", "tokens": [50974,
  264, 3052, 1314, 286, 483, 490, 341, 11, 51050], "temperature": 0.0, "avg_logprob":
  -0.12856858352134967, "compression_ratio": 2.015810276679842, "no_speech_prob":
  0.0029177896212786436}, {"id": 211, "seek": 93694, "start": 950.6600000000001, "end":
  953.62, "text": " the more I get away from Darth Vader and vice versa,", "tokens":
  [51050, 264, 544, 286, 483, 1314, 490, 40696, 36337, 293, 11964, 25650, 11, 51198],
  "temperature": 0.0, "avg_logprob": -0.12856858352134967, "compression_ratio": 2.015810276679842,
  "no_speech_prob": 0.0029177896212786436}, {"id": 212, "seek": 93694, "start": 953.62,
  "end": 955.58, "text": " then what I would expect to find,", "tokens": [51198, 550,
  437, 286, 576, 2066, 281, 915, 11, 51296], "temperature": 0.0, "avg_logprob": -0.12856858352134967,
  "compression_ratio": 2.015810276679842, "no_speech_prob": 0.0029177896212786436},
  {"id": 213, "seek": 93694, "start": 955.58, "end": 958.22, "text": " if I sort of
  average those two,", "tokens": [51296, 498, 286, 1333, 295, 4274, 729, 732, 11,
  51428], "temperature": 0.0, "avg_logprob": -0.12856858352134967, "compression_ratio":
  2.015810276679842, "no_speech_prob": 0.0029177896212786436}, {"id": 214, "seek":
  93694, "start": 958.22, "end": 960.74, "text": " a vector from here and a vector
  from here together,", "tokens": [51428, 257, 8062, 490, 510, 293, 257, 8062, 490,
  510, 1214, 11, 51554], "temperature": 0.0, "avg_logprob": -0.12856858352134967,
  "compression_ratio": 2.015810276679842, "no_speech_prob": 0.0029177896212786436},
  {"id": 215, "seek": 93694, "start": 960.74, "end": 962.94, "text": " is a Puppy
  Darth Vader,", "tokens": [51554, 307, 257, 13605, 7966, 40696, 36337, 11, 51664],
  "temperature": 0.0, "avg_logprob": -0.12856858352134967, "compression_ratio": 2.015810276679842,
  "no_speech_prob": 0.0029177896212786436}, {"id": 216, "seek": 93694, "start": 962.94,
  "end": 965.7800000000001, "text": " a cute Puppy Darth Vader right here in the middle.",
  "tokens": [51664, 257, 4052, 13605, 7966, 40696, 36337, 558, 510, 294, 264, 2808,
  13, 51806], "temperature": 0.0, "avg_logprob": -0.12856858352134967, "compression_ratio":
  2.015810276679842, "no_speech_prob": 0.0029177896212786436}, {"id": 217, "seek":
  96578, "start": 966.74, "end": 968.5, "text": " For some people that makes intuitive
  sense,", "tokens": [50412, 1171, 512, 561, 300, 1669, 21769, 2020, 11, 50500], "temperature":
  0.0, "avg_logprob": -0.1405307400611139, "compression_ratio": 1.693069306930693,
  "no_speech_prob": 0.00044243282172828913}, {"id": 218, "seek": 96578, "start": 968.5,
  "end": 971.86, "text": " but if you think about what a semantic vector space is
  doing,", "tokens": [50500, 457, 498, 291, 519, 466, 437, 257, 47982, 8062, 1901,
  307, 884, 11, 50668], "temperature": 0.0, "avg_logprob": -0.1405307400611139, "compression_ratio":
  1.693069306930693, "no_speech_prob": 0.00044243282172828913}, {"id": 219, "seek":
  96578, "start": 971.86, "end": 975.14, "text": " where it''s representing meaning
  across a continuous spectrum,", "tokens": [50668, 689, 309, 311, 13460, 3620, 2108,
  257, 10957, 11143, 11, 50832], "temperature": 0.0, "avg_logprob": -0.1405307400611139,
  "compression_ratio": 1.693069306930693, "no_speech_prob": 0.00044243282172828913},
  {"id": 220, "seek": 96578, "start": 975.14, "end": 976.38, "text": " you would expect
  to find this,", "tokens": [50832, 291, 576, 2066, 281, 915, 341, 11, 50894], "temperature":
  0.0, "avg_logprob": -0.1405307400611139, "compression_ratio": 1.693069306930693,
  "no_speech_prob": 0.00044243282172828913}, {"id": 221, "seek": 96578, "start": 976.38,
  "end": 978.62, "text": " because I''m essentially finding what the thing is,", "tokens":
  [50894, 570, 286, 478, 4476, 5006, 437, 264, 551, 307, 11, 51006], "temperature":
  0.0, "avg_logprob": -0.1405307400611139, "compression_ratio": 1.693069306930693,
  "no_speech_prob": 0.00044243282172828913}, {"id": 222, "seek": 96578, "start": 978.62,
  "end": 982.4599999999999, "text": " that is the average sort of in between Darth
  Vader and Puppy", "tokens": [51006, 300, 307, 264, 4274, 1333, 295, 294, 1296, 40696,
  36337, 293, 13605, 7966, 51198], "temperature": 0.0, "avg_logprob": -0.1405307400611139,
  "compression_ratio": 1.693069306930693, "no_speech_prob": 0.00044243282172828913},
  {"id": 223, "seek": 96578, "start": 982.4599999999999, "end": 984.62, "text": "
  within the semantic vector space.", "tokens": [51198, 1951, 264, 47982, 8062, 1901,
  13, 51306], "temperature": 0.0, "avg_logprob": -0.1405307400611139, "compression_ratio":
  1.693069306930693, "no_speech_prob": 0.00044243282172828913}, {"id": 224, "seek":
  96578, "start": 984.62, "end": 987.1, "text": " Now there''s all sorts of reasons
  why this could not work,", "tokens": [51306, 823, 456, 311, 439, 7527, 295, 4112,
  983, 341, 727, 406, 589, 11, 51430], "temperature": 0.0, "avg_logprob": -0.1405307400611139,
  "compression_ratio": 1.693069306930693, "no_speech_prob": 0.00044243282172828913},
  {"id": 225, "seek": 96578, "start": 987.1, "end": 989.02, "text": " depending upon
  how you''ve changed your model,", "tokens": [51430, 5413, 3564, 577, 291, 600, 3105,
  428, 2316, 11, 51526], "temperature": 0.0, "avg_logprob": -0.1405307400611139, "compression_ratio":
  1.693069306930693, "no_speech_prob": 0.00044243282172828913}, {"id": 226, "seek":
  96578, "start": 989.02, "end": 994.66, "text": " and if there''s too much data being
  compressed into little space,", "tokens": [51526, 293, 498, 456, 311, 886, 709,
  1412, 885, 30353, 666, 707, 1901, 11, 51808], "temperature": 0.0, "avg_logprob":
  -0.1405307400611139, "compression_ratio": 1.693069306930693, "no_speech_prob": 0.00044243282172828913},
  {"id": 227, "seek": 99466, "start": 994.66, "end": 997.18, "text": " but conceptually
  this works.", "tokens": [50364, 457, 3410, 671, 341, 1985, 13, 50490], "temperature":
  0.0, "avg_logprob": -0.1647048232578995, "compression_ratio": 1.8780487804878048,
  "no_speech_prob": 6.653396121691912e-05}, {"id": 228, "seek": 99466, "start": 998.2199999999999,
  "end": 1001.14, "text": " So similarly, if I were to do an embedding search", "tokens":
  [50542, 407, 14138, 11, 498, 286, 645, 281, 360, 364, 12240, 3584, 3164, 50688],
  "temperature": 0.0, "avg_logprob": -0.1647048232578995, "compression_ratio": 1.8780487804878048,
  "no_speech_prob": 6.653396121691912e-05}, {"id": 229, "seek": 99466, "start": 1001.14,
  "end": 1004.4599999999999, "text": " for superhero flying versus superhero''s flying,",
  "tokens": [50688, 337, 19428, 7137, 5717, 19428, 311, 7137, 11, 50854], "temperature":
  0.0, "avg_logprob": -0.1647048232578995, "compression_ratio": 1.8780487804878048,
  "no_speech_prob": 6.653396121691912e-05}, {"id": 230, "seek": 99466, "start": 1004.4599999999999,
  "end": 1010.4599999999999, "text": " this is very comparable to running a search
  for superhero flying", "tokens": [50854, 341, 307, 588, 25323, 281, 2614, 257, 3164,
  337, 19428, 7137, 51154], "temperature": 0.0, "avg_logprob": -0.1647048232578995,
  "compression_ratio": 1.8780487804878048, "no_speech_prob": 6.653396121691912e-05},
  {"id": 231, "seek": 99466, "start": 1010.4599999999999, "end": 1015.4599999999999,
  "text": " sort of with the idea of a singular hero", "tokens": [51154, 1333, 295,
  365, 264, 1558, 295, 257, 20010, 5316, 51404], "temperature": 0.0, "avg_logprob":
  -0.1647048232578995, "compression_ratio": 1.8780487804878048, "no_speech_prob":
  6.653396121691912e-05}, {"id": 232, "seek": 99466, "start": 1016.3399999999999,
  "end": 1019.66, "text": " and then sort of tracking out the idea of a singular",
  "tokens": [51448, 293, 550, 1333, 295, 11603, 484, 264, 1558, 295, 257, 20010, 51614],
  "temperature": 0.0, "avg_logprob": -0.1647048232578995, "compression_ratio": 1.8780487804878048,
  "no_speech_prob": 6.653396121691912e-05}, {"id": 233, "seek": 99466, "start": 1019.66,
  "end": 1021.54, "text": " and adding in the idea of a plural,", "tokens": [51614,
  293, 5127, 294, 264, 1558, 295, 257, 25377, 11, 51708], "temperature": 0.0, "avg_logprob":
  -0.1647048232578995, "compression_ratio": 1.8780487804878048, "no_speech_prob":
  6.653396121691912e-05}, {"id": 234, "seek": 99466, "start": 1021.54, "end": 1023.06,
  "text": " again, from here to heroes,", "tokens": [51708, 797, 11, 490, 510, 281,
  12332, 11, 51784], "temperature": 0.0, "avg_logprob": -0.1647048232578995, "compression_ratio":
  1.8780487804878048, "no_speech_prob": 6.653396121691912e-05}, {"id": 235, "seek":
  99466, "start": 1023.06, "end": 1024.42, "text": " and then what happens over here
  is,", "tokens": [51784, 293, 550, 437, 2314, 670, 510, 307, 11, 51852], "temperature":
  0.0, "avg_logprob": -0.1647048232578995, "compression_ratio": 1.8780487804878048,
  "no_speech_prob": 6.653396121691912e-05}, {"id": 236, "seek": 102442, "start": 1024.42,
  "end": 1026.74, "text": " this is essentially the same vector,", "tokens": [50364,
  341, 307, 4476, 264, 912, 8062, 11, 50480], "temperature": 0.0, "avg_logprob": -0.15135489391679524,
  "compression_ratio": 1.7159090909090908, "no_speech_prob": 5.813015013700351e-05},
  {"id": 237, "seek": 102442, "start": 1026.74, "end": 1031.74, "text": " but moved
  toward or in the direction of multiple versus singular.", "tokens": [50480, 457,
  4259, 7361, 420, 294, 264, 3513, 295, 3866, 5717, 20010, 13, 50730], "temperature":
  0.0, "avg_logprob": -0.15135489391679524, "compression_ratio": 1.7159090909090908,
  "no_speech_prob": 5.813015013700351e-05}, {"id": 238, "seek": 102442, "start": 1032.74,
  "end": 1034.26, "text": " And so what you see over here, in fact,", "tokens": [50780,
  400, 370, 437, 291, 536, 670, 510, 11, 294, 1186, 11, 50856], "temperature": 0.0,
  "avg_logprob": -0.15135489391679524, "compression_ratio": 1.7159090909090908, "no_speech_prob":
  5.813015013700351e-05}, {"id": 239, "seek": 102442, "start": 1034.26, "end": 1037.3400000000001,
  "text": " is that while some of the images are the same,", "tokens": [50856, 307,
  300, 1339, 512, 295, 264, 5267, 366, 264, 912, 11, 51010], "temperature": 0.0, "avg_logprob":
  -0.15135489391679524, "compression_ratio": 1.7159090909090908, "no_speech_prob":
  5.813015013700351e-05}, {"id": 240, "seek": 102442, "start": 1037.3400000000001,
  "end": 1040.74, "text": " I''ll, in general, I''m seeing more images of superheroes",
  "tokens": [51010, 286, 603, 11, 294, 2674, 11, 286, 478, 2577, 544, 5267, 295, 45417,
  51180], "temperature": 0.0, "avg_logprob": -0.15135489391679524, "compression_ratio":
  1.7159090909090908, "no_speech_prob": 5.813015013700351e-05}, {"id": 241, "seek":
  102442, "start": 1040.74, "end": 1043.5, "text": " that are in groups of multiple
  superheroes.", "tokens": [51180, 300, 366, 294, 3935, 295, 3866, 45417, 13, 51318],
  "temperature": 0.0, "avg_logprob": -0.15135489391679524, "compression_ratio": 1.7159090909090908,
  "no_speech_prob": 5.813015013700351e-05}, {"id": 242, "seek": 102442, "start": 1043.5,
  "end": 1048.3000000000002, "text": " And so to demonstrate this with a very explicit
  concrete example,", "tokens": [51318, 400, 370, 281, 11698, 341, 365, 257, 588,
  13691, 9859, 1365, 11, 51558], "temperature": 0.0, "avg_logprob": -0.15135489391679524,
  "compression_ratio": 1.7159090909090908, "no_speech_prob": 5.813015013700351e-05},
  {"id": 243, "seek": 102442, "start": 1048.3000000000002, "end": 1051.42, "text":
  " if I were to take this, an embedding for this image,", "tokens": [51558, 498,
  286, 645, 281, 747, 341, 11, 364, 12240, 3584, 337, 341, 3256, 11, 51714], "temperature":
  0.0, "avg_logprob": -0.15135489391679524, "compression_ratio": 1.7159090909090908,
  "no_speech_prob": 5.813015013700351e-05}, {"id": 244, "seek": 102442, "start": 1051.42,
  "end": 1053.46, "text": " which is a delorean from back to the future,", "tokens":
  [51714, 597, 307, 257, 1103, 25885, 490, 646, 281, 264, 2027, 11, 51816], "temperature":
  0.0, "avg_logprob": -0.15135489391679524, "compression_ratio": 1.7159090909090908,
  "no_speech_prob": 5.813015013700351e-05}, {"id": 245, "seek": 105346, "start": 1053.54,
  "end": 1055.3400000000001, "text": " and I were to describe it, right?", "tokens":
  [50368, 293, 286, 645, 281, 6786, 309, 11, 558, 30, 50458], "temperature": 0.0,
  "avg_logprob": -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 246, "seek": 105346, "start": 1055.3400000000001,
  "end": 1060.3400000000001, "text": " This is a sporty car with one door on either
  side,", "tokens": [50458, 639, 307, 257, 45804, 1032, 365, 472, 2853, 322, 2139,
  1252, 11, 50708], "temperature": 0.0, "avg_logprob": -0.13120878348916265, "compression_ratio":
  1.7647058823529411, "no_speech_prob": 0.0003347648598719388}, {"id": 247, "seek":
  105346, "start": 1061.3, "end": 1065.82, "text": " and it''s kind of boxy and it''s
  got really cool lighting.", "tokens": [50756, 293, 309, 311, 733, 295, 2424, 88,
  293, 309, 311, 658, 534, 1627, 9577, 13, 50982], "temperature": 0.0, "avg_logprob":
  -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 248, "seek": 105346, "start": 1065.82, "end": 1067.94,
  "text": " And so when I run that search for this embedding", "tokens": [50982, 400,
  370, 562, 286, 1190, 300, 3164, 337, 341, 12240, 3584, 51088], "temperature": 0.0,
  "avg_logprob": -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 249, "seek": 105346, "start": 1067.94, "end": 1070.9,
  "text": " on other images, I find other sporty cars,", "tokens": [51088, 322, 661,
  5267, 11, 286, 915, 661, 45804, 5163, 11, 51236], "temperature": 0.0, "avg_logprob":
  -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 250, "seek": 105346, "start": 1070.9, "end": 1072.54,
  "text": " obviously some delorians in here,", "tokens": [51236, 2745, 512, 1103,
  284, 2567, 294, 510, 11, 51318], "temperature": 0.0, "avg_logprob": -0.13120878348916265,
  "compression_ratio": 1.7647058823529411, "no_speech_prob": 0.0003347648598719388},
  {"id": 251, "seek": 105346, "start": 1072.54, "end": 1076.3, "text": " but also
  just in general sporty cars with a door on either side", "tokens": [51318, 457,
  611, 445, 294, 2674, 45804, 5163, 365, 257, 2853, 322, 2139, 1252, 51506], "temperature":
  0.0, "avg_logprob": -0.13120878348916265, "compression_ratio": 1.7647058823529411,
  "no_speech_prob": 0.0003347648598719388}, {"id": 252, "seek": 105346, "start": 1076.3,
  "end": 1078.38, "text": " and really cool lighting for the most part.", "tokens":
  [51506, 293, 534, 1627, 9577, 337, 264, 881, 644, 13, 51610], "temperature": 0.0,
  "avg_logprob": -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 253, "seek": 105346, "start": 1078.38, "end": 1081.06,
  "text": " However, what if I were to take an embedding", "tokens": [51610, 2908,
  11, 437, 498, 286, 645, 281, 747, 364, 12240, 3584, 51744], "temperature": 0.0,
  "avg_logprob": -0.13120878348916265, "compression_ratio": 1.7647058823529411, "no_speech_prob":
  0.0003347648598719388}, {"id": 254, "seek": 108106, "start": 1081.06, "end": 1085.46,
  "text": " for the query from the last slide superhero,", "tokens": [50364, 337,
  264, 14581, 490, 264, 1036, 4137, 19428, 11, 50584], "temperature": 0.0, "avg_logprob":
  -0.15508970595498123, "compression_ratio": 1.7723880597014925, "no_speech_prob":
  0.004468755330890417}, {"id": 255, "seek": 108106, "start": 1085.46, "end": 1088.4199999999998,
  "text": " and I were to average that or pull it", "tokens": [50584, 293, 286, 645,
  281, 4274, 300, 420, 2235, 309, 50732], "temperature": 0.0, "avg_logprob": -0.15508970595498123,
  "compression_ratio": 1.7723880597014925, "no_speech_prob": 0.004468755330890417},
  {"id": 256, "seek": 108106, "start": 1088.4199999999998, "end": 1090.26, "text":
  " with this image embedding, what would I get?", "tokens": [50732, 365, 341, 3256,
  12240, 3584, 11, 437, 576, 286, 483, 30, 50824], "temperature": 0.0, "avg_logprob":
  -0.15508970595498123, "compression_ratio": 1.7723880597014925, "no_speech_prob":
  0.004468755330890417}, {"id": 257, "seek": 108106, "start": 1090.26, "end": 1092.3,
  "text": " Well, in fact, we have an example of this", "tokens": [50824, 1042, 11,
  294, 1186, 11, 321, 362, 364, 1365, 295, 341, 50926], "temperature": 0.0, "avg_logprob":
  -0.15508970595498123, "compression_ratio": 1.7723880597014925, "no_speech_prob":
  0.004468755330890417}, {"id": 258, "seek": 108106, "start": 1092.3, "end": 1095.86,
  "text": " in the iPad search book when we''re doing multi-modal search.", "tokens":
  [50926, 294, 264, 12945, 3164, 1446, 562, 321, 434, 884, 4825, 12, 8014, 304, 3164,
  13, 51104], "temperature": 0.0, "avg_logprob": -0.15508970595498123, "compression_ratio":
  1.7723880597014925, "no_speech_prob": 0.004468755330890417}, {"id": 259, "seek":
  108106, "start": 1095.86, "end": 1097.7, "text": " If I take an embedding for superhero",
  "tokens": [51104, 759, 286, 747, 364, 12240, 3584, 337, 19428, 51196], "temperature":
  0.0, "avg_logprob": -0.15508970595498123, "compression_ratio": 1.7723880597014925,
  "no_speech_prob": 0.004468755330890417}, {"id": 260, "seek": 108106, "start": 1097.7,
  "end": 1099.34, "text": " and an embedding for this image,", "tokens": [51196, 293,
  364, 12240, 3584, 337, 341, 3256, 11, 51278], "temperature": 0.0, "avg_logprob":
  -0.15508970595498123, "compression_ratio": 1.7723880597014925, "no_speech_prob":
  0.004468755330890417}, {"id": 261, "seek": 108106, "start": 1099.34, "end": 1102.86,
  "text": " what I, in fact, do get is this very first result", "tokens": [51278,
  437, 286, 11, 294, 1186, 11, 360, 483, 307, 341, 588, 700, 1874, 51454], "temperature":
  0.0, "avg_logprob": -0.15508970595498123, "compression_ratio": 1.7723880597014925,
  "no_speech_prob": 0.004468755330890417}, {"id": 262, "seek": 108106, "start": 1102.86,
  "end": 1106.54, "text": " as a sporty car with cool lighting with a superhero on
  top,", "tokens": [51454, 382, 257, 45804, 1032, 365, 1627, 9577, 365, 257, 19428,
  322, 1192, 11, 51638], "temperature": 0.0, "avg_logprob": -0.15508970595498123,
  "compression_ratio": 1.7723880597014925, "no_speech_prob": 0.004468755330890417},
  {"id": 263, "seek": 108106, "start": 1106.54, "end": 1109.22, "text": " because
  that''s what I would expect in this semantic vector space", "tokens": [51638, 570,
  300, 311, 437, 286, 576, 2066, 294, 341, 47982, 8062, 1901, 51772], "temperature":
  0.0, "avg_logprob": -0.15508970595498123, "compression_ratio": 1.7723880597014925,
  "no_speech_prob": 0.004468755330890417}, {"id": 264, "seek": 110922, "start": 1109.22,
  "end": 1112.1000000000001, "text": " to be in between these things.", "tokens":
  [50364, 281, 312, 294, 1296, 613, 721, 13, 50508], "temperature": 0.0, "avg_logprob":
  -0.12945638164397208, "compression_ratio": 1.7445255474452555, "no_speech_prob":
  0.006800663657486439}, {"id": 265, "seek": 110922, "start": 1112.1000000000001,
  "end": 1116.06, "text": " And for these other images, again, sporty cars, single
  door,", "tokens": [50508, 400, 337, 613, 661, 5267, 11, 797, 11, 45804, 5163, 11,
  2167, 2853, 11, 50706], "temperature": 0.0, "avg_logprob": -0.12945638164397208,
  "compression_ratio": 1.7445255474452555, "no_speech_prob": 0.006800663657486439},
  {"id": 266, "seek": 110922, "start": 1116.06, "end": 1119.02, "text": " but notice
  that in all of them, there''s a person,", "tokens": [50706, 457, 3449, 300, 294,
  439, 295, 552, 11, 456, 311, 257, 954, 11, 50854], "temperature": 0.0, "avg_logprob":
  -0.12945638164397208, "compression_ratio": 1.7445255474452555, "no_speech_prob":
  0.006800663657486439}, {"id": 267, "seek": 110922, "start": 1119.02, "end": 1120.78,
  "text": " and it just so happens that that person", "tokens": [50854, 293, 309,
  445, 370, 2314, 300, 300, 954, 50942], "temperature": 0.0, "avg_logprob": -0.12945638164397208,
  "compression_ratio": 1.7445255474452555, "no_speech_prob": 0.006800663657486439},
  {"id": 268, "seek": 110922, "start": 1120.78, "end": 1123.14, "text": " is the protagonist
  of their story.", "tokens": [50942, 307, 264, 24506, 295, 641, 1657, 13, 51060],
  "temperature": 0.0, "avg_logprob": -0.12945638164397208, "compression_ratio": 1.7445255474452555,
  "no_speech_prob": 0.006800663657486439}, {"id": 269, "seek": 110922, "start": 1123.14,
  "end": 1125.66, "text": " So maybe those stories didn''t have actual superheroes,",
  "tokens": [51060, 407, 1310, 729, 3676, 994, 380, 362, 3539, 45417, 11, 51186],
  "temperature": 0.0, "avg_logprob": -0.12945638164397208, "compression_ratio": 1.7445255474452555,
  "no_speech_prob": 0.006800663657486439}, {"id": 270, "seek": 110922, "start": 1125.66,
  "end": 1127.98, "text": " but these are the heroes of those stories.", "tokens":
  [51186, 457, 613, 366, 264, 12332, 295, 729, 3676, 13, 51302], "temperature": 0.0,
  "avg_logprob": -0.12945638164397208, "compression_ratio": 1.7445255474452555, "no_speech_prob":
  0.006800663657486439}, {"id": 271, "seek": 110922, "start": 1127.98, "end": 1130.82,
  "text": " So you get the idea, and I wanted to paint that conceptually", "tokens":
  [51302, 407, 291, 483, 264, 1558, 11, 293, 286, 1415, 281, 4225, 300, 3410, 671,
  51444], "temperature": 0.0, "avg_logprob": -0.12945638164397208, "compression_ratio":
  1.7445255474452555, "no_speech_prob": 0.006800663657486439}, {"id": 272, "seek":
  110922, "start": 1130.82, "end": 1133.7, "text": " just to talk about regions of
  vector space", "tokens": [51444, 445, 281, 751, 466, 10682, 295, 8062, 1901, 51588],
  "temperature": 0.0, "avg_logprob": -0.12945638164397208, "compression_ratio": 1.7445255474452555,
  "no_speech_prob": 0.006800663657486439}, {"id": 273, "seek": 110922, "start": 1133.7,
  "end": 1137.3, "text": " and what they represent and how you can use math on vectors",
  "tokens": [51588, 293, 437, 436, 2906, 293, 577, 291, 393, 764, 5221, 322, 18875,
  51768], "temperature": 0.0, "avg_logprob": -0.12945638164397208, "compression_ratio":
  1.7445255474452555, "no_speech_prob": 0.006800663657486439}, {"id": 274, "seek":
  113730, "start": 1137.3, "end": 1140.74, "text": " to move between them and sort
  of combine concepts", "tokens": [50364, 281, 1286, 1296, 552, 293, 1333, 295, 10432,
  10392, 50536], "temperature": 0.0, "avg_logprob": -0.13015363673971156, "compression_ratio":
  1.688073394495413, "no_speech_prob": 0.00017746536468621343}, {"id": 275, "seek":
  113730, "start": 1140.74, "end": 1142.8999999999999, "text": " and find related
  things.", "tokens": [50536, 293, 915, 4077, 721, 13, 50644], "temperature": 0.0,
  "avg_logprob": -0.13015363673971156, "compression_ratio": 1.688073394495413, "no_speech_prob":
  0.00017746536468621343}, {"id": 276, "seek": 113730, "start": 1143.94, "end": 1148.94,
  "text": " And so one problem, now zooming back out to the topic of today,", "tokens":
  [50696, 400, 370, 472, 1154, 11, 586, 48226, 646, 484, 281, 264, 4829, 295, 965,
  11, 50946], "temperature": 0.0, "avg_logprob": -0.13015363673971156, "compression_ratio":
  1.688073394495413, "no_speech_prob": 0.00017746536468621343}, {"id": 277, "seek":
  113730, "start": 1148.94, "end": 1152.62, "text": " one problem that we commonly
  come across,", "tokens": [50946, 472, 1154, 300, 321, 12719, 808, 2108, 11, 51130],
  "temperature": 0.0, "avg_logprob": -0.13015363673971156, "compression_ratio": 1.688073394495413,
  "no_speech_prob": 0.00017746536468621343}, {"id": 278, "seek": 113730, "start":
  1152.62, "end": 1155.02, "text": " and this is where hybrid search comes into play,",
  "tokens": [51130, 293, 341, 307, 689, 13051, 3164, 1487, 666, 862, 11, 51250], "temperature":
  0.0, "avg_logprob": -0.13015363673971156, "compression_ratio": 1.688073394495413,
  "no_speech_prob": 0.00017746536468621343}, {"id": 279, "seek": 113730, "start":
  1155.02, "end": 1158.3799999999999, "text": " is that we have disjoint vector spaces
  in search", "tokens": [51250, 307, 300, 321, 362, 717, 48613, 8062, 7673, 294, 3164,
  51418], "temperature": 0.0, "avg_logprob": -0.13015363673971156, "compression_ratio":
  1.688073394495413, "no_speech_prob": 0.00017746536468621343}, {"id": 280, "seek":
  113730, "start": 1158.3799999999999, "end": 1161.3, "text": " and that leads to
  disjoint query paradigms.", "tokens": [51418, 293, 300, 6689, 281, 717, 48613, 14581,
  13480, 328, 2592, 13, 51564], "temperature": 0.0, "avg_logprob": -0.13015363673971156,
  "compression_ratio": 1.688073394495413, "no_speech_prob": 0.00017746536468621343},
  {"id": 281, "seek": 113730, "start": 1161.3, "end": 1166.1, "text": " What I mean
  by that is that we have a sparse,", "tokens": [51564, 708, 286, 914, 538, 300, 307,
  300, 321, 362, 257, 637, 11668, 11, 51804], "temperature": 0.0, "avg_logprob": -0.13015363673971156,
  "compression_ratio": 1.688073394495413, "no_speech_prob": 0.00017746536468621343},
  {"id": 282, "seek": 116610, "start": 1166.1, "end": 1170.82, "text": " lexical semantic
  space, which is our inverted index.", "tokens": [50364, 476, 87, 804, 47982, 1901,
  11, 597, 307, 527, 38969, 8186, 13, 50600], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 283, "seek": 116610, "start": 1170.82, "end": 1172.9399999999998, "text":
  " What I showed you earlier with the million dimensions", "tokens": [50600, 708,
  286, 4712, 291, 3071, 365, 264, 2459, 12819, 50706], "temperature": 0.0, "avg_logprob":
  -0.11010892982156868, "compression_ratio": 1.6853932584269662, "no_speech_prob":
  9.287398279411718e-05}, {"id": 284, "seek": 116610, "start": 1172.9399999999998,
  "end": 1175.3799999999999, "text": " and the keywords represent the dimensions,",
  "tokens": [50706, 293, 264, 21009, 2906, 264, 12819, 11, 50828], "temperature":
  0.0, "avg_logprob": -0.11010892982156868, "compression_ratio": 1.6853932584269662,
  "no_speech_prob": 9.287398279411718e-05}, {"id": 285, "seek": 116610, "start": 1175.3799999999999,
  "end": 1176.86, "text": " that is a vector space.", "tokens": [50828, 300, 307,
  257, 8062, 1901, 13, 50902], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 286, "seek": 116610, "start": 1176.86, "end": 1178.2199999999998, "text":
  " It''s just a very sparse one.", "tokens": [50902, 467, 311, 445, 257, 588, 637,
  11668, 472, 13, 50970], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 287, "seek": 116610, "start": 1179.2199999999998, "end": 1181.86, "text":
  " Similarly, we have dense vector spaces", "tokens": [51020, 13157, 11, 321, 362,
  18011, 8062, 7673, 51152], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 288, "seek": 116610, "start": 1181.86, "end": 1184.2199999999998, "text":
  " where most of our embeddings are,", "tokens": [51152, 689, 881, 295, 527, 12240,
  29432, 366, 11, 51270], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 289, "seek": 116610, "start": 1184.2199999999998, "end": 1185.86, "text":
  " that we get out of large language models", "tokens": [51270, 300, 321, 483, 484,
  295, 2416, 2856, 5245, 51352], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 290, "seek": 116610, "start": 1185.86, "end": 1189.34, "text": " where they''re
  compact into a small number of dimensions,", "tokens": [51352, 689, 436, 434, 14679,
  666, 257, 1359, 1230, 295, 12819, 11, 51526], "temperature": 0.0, "avg_logprob":
  -0.11010892982156868, "compression_ratio": 1.6853932584269662, "no_speech_prob":
  9.287398279411718e-05}, {"id": 291, "seek": 116610, "start": 1189.34, "end": 1191.1799999999998,
  "text": " but they''re continuous.", "tokens": [51526, 457, 436, 434, 10957, 13,
  51618], "temperature": 0.0, "avg_logprob": -0.11010892982156868, "compression_ratio":
  1.6853932584269662, "no_speech_prob": 9.287398279411718e-05}, {"id": 292, "seek":
  116610, "start": 1191.1799999999998, "end": 1193.82, "text": " Because we have these
  two different query paradigms,", "tokens": [51618, 1436, 321, 362, 613, 732, 819,
  14581, 13480, 328, 2592, 11, 51750], "temperature": 0.0, "avg_logprob": -0.11010892982156868,
  "compression_ratio": 1.6853932584269662, "no_speech_prob": 9.287398279411718e-05},
  {"id": 293, "seek": 119382, "start": 1193.82, "end": 1198.22, "text": " what often
  happens with vector search is we say,", "tokens": [50364, 437, 2049, 2314, 365,
  8062, 3164, 307, 321, 584, 11, 50584], "temperature": 0.0, "avg_logprob": -0.12971499870563374,
  "compression_ratio": 1.657992565055762, "no_speech_prob": 0.00019350160437170416},
  {"id": 294, "seek": 119382, "start": 1198.22, "end": 1201.3, "text": " hey, I don''t
  know how to combine this dense query", "tokens": [50584, 4177, 11, 286, 500, 380,
  458, 577, 281, 10432, 341, 18011, 14581, 50738], "temperature": 0.0, "avg_logprob":
  -0.12971499870563374, "compression_ratio": 1.657992565055762, "no_speech_prob":
  0.00019350160437170416}, {"id": 295, "seek": 119382, "start": 1201.3, "end": 1204.62,
  "text": " on this embedding with the sparse query with these keywords.", "tokens":
  [50738, 322, 341, 12240, 3584, 365, 264, 637, 11668, 14581, 365, 613, 21009, 13,
  50904], "temperature": 0.0, "avg_logprob": -0.12971499870563374, "compression_ratio":
  1.657992565055762, "no_speech_prob": 0.00019350160437170416}, {"id": 296, "seek":
  119382, "start": 1204.62, "end": 1207.02, "text": " So I''m just going to run them
  as separate searches.", "tokens": [50904, 407, 286, 478, 445, 516, 281, 1190, 552,
  382, 4994, 26701, 13, 51024], "temperature": 0.0, "avg_logprob": -0.12971499870563374,
  "compression_ratio": 1.657992565055762, "no_speech_prob": 0.00019350160437170416},
  {"id": 297, "seek": 119382, "start": 1207.02, "end": 1210.74, "text": " And in fact,
  that''s what most sort of hybrid searches,", "tokens": [51024, 400, 294, 1186, 11,
  300, 311, 437, 881, 1333, 295, 13051, 26701, 11, 51210], "temperature": 0.0, "avg_logprob":
  -0.12971499870563374, "compression_ratio": 1.657992565055762, "no_speech_prob":
  0.00019350160437170416}, {"id": 298, "seek": 119382, "start": 1210.74, "end": 1213.86,
  "text": " hybrid search implementations look like out of the box.", "tokens": [51210,
  13051, 3164, 4445, 763, 574, 411, 484, 295, 264, 2424, 13, 51366], "temperature":
  0.0, "avg_logprob": -0.12971499870563374, "compression_ratio": 1.657992565055762,
  "no_speech_prob": 0.00019350160437170416}, {"id": 299, "seek": 119382, "start":
  1213.86, "end": 1218.62, "text": " So this is an example of RRF or the reciprocal
  rank fusion algorithm", "tokens": [51366, 407, 341, 307, 364, 1365, 295, 497, 49,
  37, 420, 264, 46948, 6181, 23100, 9284, 51604], "temperature": 0.0, "avg_logprob":
  -0.12971499870563374, "compression_ratio": 1.657992565055762, "no_speech_prob":
  0.00019350160437170416}, {"id": 300, "seek": 119382, "start": 1218.62, "end": 1221.9399999999998,
  "text": " where I''m essentially taking a lexical query over here", "tokens": [51604,
  689, 286, 478, 4476, 1940, 257, 476, 87, 804, 14581, 670, 510, 51770], "temperature":
  0.0, "avg_logprob": -0.12971499870563374, "compression_ratio": 1.657992565055762,
  "no_speech_prob": 0.00019350160437170416}, {"id": 301, "seek": 122194, "start":
  1221.94, "end": 1223.46, "text": " for the Hobbit.", "tokens": [50364, 337, 264,
  22966, 5260, 13, 50440], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 302, "seek": 122194, "start": 1223.46, "end": 1225.22, "text": " And I''m
  matching on a bunch of documents.", "tokens": [50440, 400, 286, 478, 14324, 322,
  257, 3840, 295, 8512, 13, 50528], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 303, "seek": 122194, "start": 1225.22, "end": 1227.98, "text": " You''ll
  see each of these has the word Hobbit", "tokens": [50528, 509, 603, 536, 1184, 295,
  613, 575, 264, 1349, 22966, 5260, 50666], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 304, "seek": 122194, "start": 1227.98, "end": 1229.78, "text": " and it''s
  somewhere either in the title", "tokens": [50666, 293, 309, 311, 4079, 2139, 294,
  264, 4876, 50756], "temperature": 0.0, "avg_logprob": -0.1446118462354617, "compression_ratio":
  1.873015873015873, "no_speech_prob": 0.006634780205786228}, {"id": 305, "seek":
  122194, "start": 1229.78, "end": 1231.74, "text": " or maybe in the description.",
  "tokens": [50756, 420, 1310, 294, 264, 3855, 13, 50854], "temperature": 0.0, "avg_logprob":
  -0.1446118462354617, "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 306, "seek": 122194, "start": 1231.74, "end": 1236.66, "text": " But notice
  that while the first four results look pretty good,", "tokens": [50854, 583, 3449,
  300, 1339, 264, 700, 1451, 3542, 574, 1238, 665, 11, 51100], "temperature": 0.0,
  "avg_logprob": -0.1446118462354617, "compression_ratio": 1.873015873015873, "no_speech_prob":
  0.006634780205786228}, {"id": 307, "seek": 122194, "start": 1236.66, "end": 1238.46,
  "text": " the next, these are the only results", "tokens": [51100, 264, 958, 11,
  613, 366, 264, 787, 3542, 51190], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 308, "seek": 122194, "start": 1238.46, "end": 1240.3400000000001, "text":
  " that had the word Hobbit in them.", "tokens": [51190, 300, 632, 264, 1349, 22966,
  5260, 294, 552, 13, 51284], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 309, "seek": 122194, "start": 1240.3400000000001, "end": 1241.98, "text":
  " And then the rest of these results,", "tokens": [51284, 400, 550, 264, 1472, 295,
  613, 3542, 11, 51366], "temperature": 0.0, "avg_logprob": -0.1446118462354617, "compression_ratio":
  1.873015873015873, "no_speech_prob": 0.006634780205786228}, {"id": 310, "seek":
  122194, "start": 1241.98, "end": 1244.26, "text": " the good, the bad, and the ugly.",
  "tokens": [51366, 264, 665, 11, 264, 1578, 11, 293, 264, 12246, 13, 51480], "temperature":
  0.0, "avg_logprob": -0.1446118462354617, "compression_ratio": 1.873015873015873,
  "no_speech_prob": 0.006634780205786228}, {"id": 311, "seek": 122194, "start": 1244.26,
  "end": 1247.8200000000002, "text": " This just happens to match on the word the
  three times.", "tokens": [51480, 639, 445, 2314, 281, 2995, 322, 264, 1349, 264,
  1045, 1413, 13, 51658], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 312, "seek": 122194, "start": 1247.8200000000002, "end": 1250.46, "text":
  " And then this next result happens to match", "tokens": [51658, 400, 550, 341,
  958, 1874, 2314, 281, 2995, 51790], "temperature": 0.0, "avg_logprob": -0.1446118462354617,
  "compression_ratio": 1.873015873015873, "no_speech_prob": 0.006634780205786228},
  {"id": 313, "seek": 125046, "start": 1250.46, "end": 1253.14, "text": " on the Lord
  of the ring.", "tokens": [50364, 322, 264, 3257, 295, 264, 4875, 13, 50498], "temperature":
  0.0, "avg_logprob": -0.14320736057710964, "compression_ratio": 1.7451612903225806,
  "no_speech_prob": 0.0005634360131807625}, {"id": 314, "seek": 125046, "start": 1253.14,
  "end": 1255.3400000000001, "text": " So it''s got the in it three times as well.",
  "tokens": [50498, 407, 309, 311, 658, 264, 294, 309, 1045, 1413, 382, 731, 13, 50608],
  "temperature": 0.0, "avg_logprob": -0.14320736057710964, "compression_ratio": 1.7451612903225806,
  "no_speech_prob": 0.0005634360131807625}, {"id": 315, "seek": 125046, "start": 1255.3400000000001,
  "end": 1257.22, "text": " It happened to give me a good result,", "tokens": [50608,
  467, 2011, 281, 976, 385, 257, 665, 1874, 11, 50702], "temperature": 0.0, "avg_logprob":
  -0.14320736057710964, "compression_ratio": 1.7451612903225806, "no_speech_prob":
  0.0005634360131807625}, {"id": 316, "seek": 125046, "start": 1257.22, "end": 1258.74,
  "text": " but it was purely coincidence", "tokens": [50702, 457, 309, 390, 17491,
  22137, 50778], "temperature": 0.0, "avg_logprob": -0.14320736057710964, "compression_ratio":
  1.7451612903225806, "no_speech_prob": 0.0005634360131807625}, {"id": 317, "seek":
  125046, "start": 1258.74, "end": 1260.78, "text": " because it doesn''t have the
  word Hobbit here.", "tokens": [50778, 570, 309, 1177, 380, 362, 264, 1349, 22966,
  5260, 510, 13, 50880], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 318, "seek": 125046, "start": 1260.78, "end": 1263.06, "text": " And then
  I get the abyss and then the apartment again,", "tokens": [50880, 400, 550, 286,
  483, 264, 410, 31059, 293, 550, 264, 9587, 797, 11, 50994], "temperature": 0.0,
  "avg_logprob": -0.14320736057710964, "compression_ratio": 1.7451612903225806, "no_speech_prob":
  0.0005634360131807625}, {"id": 319, "seek": 125046, "start": 1263.06, "end": 1264.46,
  "text": " only matching on the word the.", "tokens": [50994, 787, 14324, 322, 264,
  1349, 264, 13, 51064], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 320, "seek": 125046, "start": 1264.46, "end": 1266.46, "text": " So the lexical
  search found all the results", "tokens": [51064, 407, 264, 476, 87, 804, 3164, 1352,
  439, 264, 3542, 51164], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 321, "seek": 125046, "start": 1266.46, "end": 1268.1000000000001, "text":
  " that had the word Hobbit in them,", "tokens": [51164, 300, 632, 264, 1349, 22966,
  5260, 294, 552, 11, 51246], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 322, "seek": 125046, "start": 1268.1000000000001, "end": 1269.8600000000001,
  "text": " but it completely missed a whole bunch", "tokens": [51246, 457, 309, 2584,
  6721, 257, 1379, 3840, 51334], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 323, "seek": 125046, "start": 1269.8600000000001, "end": 1271.82, "text":
  " of other potentially relevant results.", "tokens": [51334, 295, 661, 7263, 7340,
  3542, 13, 51432], "temperature": 0.0, "avg_logprob": -0.14320736057710964, "compression_ratio":
  1.7451612903225806, "no_speech_prob": 0.0005634360131807625}, {"id": 324, "seek":
  125046, "start": 1271.82, "end": 1275.22, "text": " Likewise, my vector query over
  here for this embedding", "tokens": [51432, 30269, 11, 452, 8062, 14581, 670, 510,
  337, 341, 12240, 3584, 51602], "temperature": 0.0, "avg_logprob": -0.14320736057710964,
  "compression_ratio": 1.7451612903225806, "no_speech_prob": 0.0005634360131807625},
  {"id": 325, "seek": 125046, "start": 1275.22, "end": 1277.3, "text": " matched the
  Hobbit here.", "tokens": [51602, 21447, 264, 22966, 5260, 510, 13, 51706], "temperature":
  0.0, "avg_logprob": -0.14320736057710964, "compression_ratio": 1.7451612903225806,
  "no_speech_prob": 0.0005634360131807625}, {"id": 326, "seek": 125046, "start": 1277.3,
  "end": 1279.74, "text": " It matched a Harry Potter movie here.", "tokens": [51706,
  467, 21447, 257, 9378, 18115, 3169, 510, 13, 51828], "temperature": 0.0, "avg_logprob":
  -0.14320736057710964, "compression_ratio": 1.7451612903225806, "no_speech_prob":
  0.0005634360131807625}, {"id": 327, "seek": 127974, "start": 1279.74, "end": 1282.74,
  "text": " Similar concepts, similar themes,", "tokens": [50364, 10905, 10392, 11,
  2531, 13544, 11, 50514], "temperature": 0.0, "avg_logprob": -0.18317613670294233,
  "compression_ratio": 1.962962962962963, "no_speech_prob": 0.00045225981739349663},
  {"id": 328, "seek": 127974, "start": 1282.74, "end": 1286.5, "text": " and similar
  kind of visual style.", "tokens": [50514, 293, 2531, 733, 295, 5056, 3758, 13, 50702],
  "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio": 1.962962962962963,
  "no_speech_prob": 0.00045225981739349663}, {"id": 329, "seek": 127974, "start":
  1286.5, "end": 1288.1, "text": " Lord of the rings, Lord of the rings,", "tokens":
  [50702, 3257, 295, 264, 11136, 11, 3257, 295, 264, 11136, 11, 50782], "temperature":
  0.0, "avg_logprob": -0.18317613670294233, "compression_ratio": 1.962962962962963,
  "no_speech_prob": 0.00045225981739349663}, {"id": 330, "seek": 127974, "start":
  1288.1, "end": 1289.46, "text": " Rise of the Guardians, I guess,", "tokens": [50782,
  34482, 295, 264, 45236, 11, 286, 2041, 11, 50850], "temperature": 0.0, "avg_logprob":
  -0.18317613670294233, "compression_ratio": 1.962962962962963, "no_speech_prob":
  0.00045225981739349663}, {"id": 331, "seek": 127974, "start": 1289.46, "end": 1291.02,
  "text": " is maybe kind of conceptually similar", "tokens": [50850, 307, 1310, 733,
  295, 3410, 671, 2531, 50928], "temperature": 0.0, "avg_logprob": -0.18317613670294233,
  "compression_ratio": 1.962962962962963, "no_speech_prob": 0.00045225981739349663},
  {"id": 332, "seek": 127974, "start": 1291.02, "end": 1293.7, "text": " even though
  it''s a cartoon.", "tokens": [50928, 754, 1673, 309, 311, 257, 18569, 13, 51062],
  "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio": 1.962962962962963,
  "no_speech_prob": 0.00045225981739349663}, {"id": 333, "seek": 127974, "start":
  1293.7, "end": 1296.1, "text": " The wailing, I think, just has a visually similar
  style,", "tokens": [51062, 440, 261, 23315, 11, 286, 519, 11, 445, 575, 257, 19622,
  2531, 3758, 11, 51182], "temperature": 0.0, "avg_logprob": -0.18317613670294233,
  "compression_ratio": 1.962962962962963, "no_speech_prob": 0.00045225981739349663},
  {"id": 334, "seek": 127974, "start": 1296.1, "end": 1297.18, "text": " but it''s
  a really bad match.", "tokens": [51182, 457, 309, 311, 257, 534, 1578, 2995, 13,
  51236], "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio":
  1.962962962962963, "no_speech_prob": 0.00045225981739349663}, {"id": 335, "seek":
  127974, "start": 1297.18, "end": 1298.02, "text": " You get the idea.", "tokens":
  [51236, 509, 483, 264, 1558, 13, 51278], "temperature": 0.0, "avg_logprob": -0.18317613670294233,
  "compression_ratio": 1.962962962962963, "no_speech_prob": 0.00045225981739349663},
  {"id": 336, "seek": 127974, "start": 1298.02, "end": 1299.66, "text": " So there''s
  some really good results", "tokens": [51278, 407, 456, 311, 512, 534, 665, 3542,
  51360], "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio":
  1.962962962962963, "no_speech_prob": 0.00045225981739349663}, {"id": 337, "seek":
  127974, "start": 1299.66, "end": 1302.18, "text": " I get from the vector search,",
  "tokens": [51360, 286, 483, 490, 264, 8062, 3164, 11, 51486], "temperature": 0.0,
  "avg_logprob": -0.18317613670294233, "compression_ratio": 1.962962962962963, "no_speech_prob":
  0.00045225981739349663}, {"id": 338, "seek": 127974, "start": 1302.18, "end": 1303.9,
  "text": " some the dense vector search,", "tokens": [51486, 512, 264, 18011, 8062,
  3164, 11, 51572], "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio":
  1.962962962962963, "no_speech_prob": 0.00045225981739349663}, {"id": 339, "seek":
  127974, "start": 1303.9, "end": 1306.22, "text": " some really good results I get
  from this lexical", "tokens": [51572, 512, 534, 665, 3542, 286, 483, 490, 341, 476,
  87, 804, 51688], "temperature": 0.0, "avg_logprob": -0.18317613670294233, "compression_ratio":
  1.962962962962963, "no_speech_prob": 0.00045225981739349663}, {"id": 340, "seek":
  127974, "start": 1306.22, "end": 1308.26, "text": " or sparse vector search.", "tokens":
  [51688, 420, 637, 11668, 8062, 3164, 13, 51790], "temperature": 0.0, "avg_logprob":
  -0.18317613670294233, "compression_ratio": 1.962962962962963, "no_speech_prob":
  0.00045225981739349663}, {"id": 341, "seek": 130826, "start": 1308.26, "end": 1311.78,
  "text": " And then with hybrid search with reciprocal rank fusion,", "tokens": [50364,
  400, 550, 365, 13051, 3164, 365, 46948, 6181, 23100, 11, 50540], "temperature":
  0.0, "avg_logprob": -0.1321264338270526, "compression_ratio": 1.728395061728395,
  "no_speech_prob": 6.19793645455502e-05}, {"id": 342, "seek": 130826, "start": 1311.78,
  "end": 1314.3799999999999, "text": " we can essentially take each of those separate
  sets", "tokens": [50540, 321, 393, 4476, 747, 1184, 295, 729, 4994, 6352, 50670],
  "temperature": 0.0, "avg_logprob": -0.1321264338270526, "compression_ratio": 1.728395061728395,
  "no_speech_prob": 6.19793645455502e-05}, {"id": 343, "seek": 130826, "start": 1314.3799999999999,
  "end": 1316.86, "text": " of results and combine them together", "tokens": [50670,
  295, 3542, 293, 10432, 552, 1214, 50794], "temperature": 0.0, "avg_logprob": -0.1321264338270526,
  "compression_ratio": 1.728395061728395, "no_speech_prob": 6.19793645455502e-05},
  {"id": 344, "seek": 130826, "start": 1316.86, "end": 1320.74, "text": " in a way
  that weights things that both the lexical", "tokens": [50794, 294, 257, 636, 300,
  17443, 721, 300, 1293, 264, 476, 87, 804, 50988], "temperature": 0.0, "avg_logprob":
  -0.1321264338270526, "compression_ratio": 1.728395061728395, "no_speech_prob": 6.19793645455502e-05},
  {"id": 345, "seek": 130826, "start": 1320.74, "end": 1324.62, "text": " and the
  dense search found relevant.", "tokens": [50988, 293, 264, 18011, 3164, 1352, 7340,
  13, 51182], "temperature": 0.0, "avg_logprob": -0.1321264338270526, "compression_ratio":
  1.728395061728395, "no_speech_prob": 6.19793645455502e-05}, {"id": 346, "seek":
  130826, "start": 1324.62, "end": 1325.94, "text": " It moves those to the top",
  "tokens": [51182, 467, 6067, 729, 281, 264, 1192, 51248], "temperature": 0.0, "avg_logprob":
  -0.1321264338270526, "compression_ratio": 1.728395061728395, "no_speech_prob": 6.19793645455502e-05},
  {"id": 347, "seek": 130826, "start": 1325.94, "end": 1329.1, "text": " and then
  kind of gives us better results overall.", "tokens": [51248, 293, 550, 733, 295,
  2709, 505, 1101, 3542, 4787, 13, 51406], "temperature": 0.0, "avg_logprob": -0.1321264338270526,
  "compression_ratio": 1.728395061728395, "no_speech_prob": 6.19793645455502e-05},
  {"id": 348, "seek": 130826, "start": 1329.1, "end": 1333.58, "text": " And you can
  see that I''ve matched most of the results over here.", "tokens": [51406, 400, 291,
  393, 536, 300, 286, 600, 21447, 881, 295, 264, 3542, 670, 510, 13, 51630], "temperature":
  0.0, "avg_logprob": -0.1321264338270526, "compression_ratio": 1.728395061728395,
  "no_speech_prob": 6.19793645455502e-05}, {"id": 349, "seek": 130826, "start": 1333.58,
  "end": 1335.94, "text": " So it''s better than either of the two lexical", "tokens":
  [51630, 407, 309, 311, 1101, 813, 2139, 295, 264, 732, 476, 87, 804, 51748], "temperature":
  0.0, "avg_logprob": -0.1321264338270526, "compression_ratio": 1.728395061728395,
  "no_speech_prob": 6.19793645455502e-05}, {"id": 350, "seek": 133594, "start": 1335.94,
  "end": 1339.38, "text": " or dense vector search mechanisms individually.", "tokens":
  [50364, 420, 18011, 8062, 3164, 15902, 16652, 13, 50536], "temperature": 0.0, "avg_logprob":
  -0.14885834185746463, "compression_ratio": 1.8265682656826567, "no_speech_prob":
  0.001988595351576805}, {"id": 351, "seek": 133594, "start": 1339.38, "end": 1342.38,
  "text": " However, I''m still treating them", "tokens": [50536, 2908, 11, 286, 478,
  920, 15083, 552, 50686], "temperature": 0.0, "avg_logprob": -0.14885834185746463,
  "compression_ratio": 1.8265682656826567, "no_speech_prob": 0.001988595351576805},
  {"id": 352, "seek": 133594, "start": 1342.38, "end": 1344.1000000000001, "text":
  " as entirely separate things.", "tokens": [50686, 382, 7696, 4994, 721, 13, 50772],
  "temperature": 0.0, "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567,
  "no_speech_prob": 0.001988595351576805}, {"id": 353, "seek": 133594, "start": 1344.1000000000001,
  "end": 1345.3400000000001, "text": " I''m doing the lexical search,", "tokens":
  [50772, 286, 478, 884, 264, 476, 87, 804, 3164, 11, 50834], "temperature": 0.0,
  "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567, "no_speech_prob":
  0.001988595351576805}, {"id": 354, "seek": 133594, "start": 1345.3400000000001,
  "end": 1346.54, "text": " I''m doing an embedding search", "tokens": [50834, 286,
  478, 884, 364, 12240, 3584, 3164, 50894], "temperature": 0.0, "avg_logprob": -0.14885834185746463,
  "compression_ratio": 1.8265682656826567, "no_speech_prob": 0.001988595351576805},
  {"id": 355, "seek": 133594, "start": 1346.54, "end": 1349.66, "text": " and then
  I''m combining them together.", "tokens": [50894, 293, 550, 286, 478, 21928, 552,
  1214, 13, 51050], "temperature": 0.0, "avg_logprob": -0.14885834185746463, "compression_ratio":
  1.8265682656826567, "no_speech_prob": 0.001988595351576805}, {"id": 356, "seek":
  133594, "start": 1349.66, "end": 1351.8200000000002, "text": " But in reality, there''s
  lots of ways", "tokens": [51050, 583, 294, 4103, 11, 456, 311, 3195, 295, 2098,
  51158], "temperature": 0.0, "avg_logprob": -0.14885834185746463, "compression_ratio":
  1.8265682656826567, "no_speech_prob": 0.001988595351576805}, {"id": 357, "seek":
  133594, "start": 1351.8200000000002, "end": 1353.66, "text": " to merge these different
  paradigms.", "tokens": [51158, 281, 22183, 613, 819, 13480, 328, 2592, 13, 51250],
  "temperature": 0.0, "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567,
  "no_speech_prob": 0.001988595351576805}, {"id": 358, "seek": 133594, "start": 1353.66,
  "end": 1357.46, "text": " And even beyond just the embeddings I''m getting from
  texts,", "tokens": [51250, 400, 754, 4399, 445, 264, 12240, 29432, 286, 478, 1242,
  490, 15765, 11, 51440], "temperature": 0.0, "avg_logprob": -0.14885834185746463,
  "compression_ratio": 1.8265682656826567, "no_speech_prob": 0.001988595351576805},
  {"id": 359, "seek": 133594, "start": 1357.46, "end": 1359.3, "text": " we can get
  text embeddings.", "tokens": [51440, 321, 393, 483, 2487, 12240, 29432, 13, 51532],
  "temperature": 0.0, "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567,
  "no_speech_prob": 0.001988595351576805}, {"id": 360, "seek": 133594, "start": 1359.3,
  "end": 1361.9, "text": " So for example, we can do a text encoder", "tokens": [51532,
  407, 337, 1365, 11, 321, 393, 360, 257, 2487, 2058, 19866, 51662], "temperature":
  0.0, "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567,
  "no_speech_prob": 0.001988595351576805}, {"id": 361, "seek": 133594, "start": 1361.9,
  "end": 1363.38, "text": " to generate embeddings for that.", "tokens": [51662, 281,
  8460, 12240, 29432, 337, 300, 13, 51736], "temperature": 0.0, "avg_logprob": -0.14885834185746463,
  "compression_ratio": 1.8265682656826567, "no_speech_prob": 0.001988595351576805},
  {"id": 362, "seek": 133594, "start": 1363.38, "end": 1365.8600000000001, "text":
  " We can take images and generate embeddings for that.", "tokens": [51736, 492,
  393, 747, 5267, 293, 8460, 12240, 29432, 337, 300, 13, 51860], "temperature": 0.0,
  "avg_logprob": -0.14885834185746463, "compression_ratio": 1.8265682656826567, "no_speech_prob":
  0.001988595351576805}, {"id": 363, "seek": 136586, "start": 1365.86, "end": 1368.1,
  "text": " We can also take user behaviors", "tokens": [50364, 492, 393, 611, 747,
  4195, 15501, 50476], "temperature": 0.0, "avg_logprob": -0.12627686828863424, "compression_ratio":
  1.7043795620437956, "no_speech_prob": 6.328119343379512e-05}, {"id": 364, "seek":
  136586, "start": 1368.1, "end": 1370.74, "text": " and generate behavioral based
  embeddings", "tokens": [50476, 293, 8460, 19124, 2361, 12240, 29432, 50608], "temperature":
  0.0, "avg_logprob": -0.12627686828863424, "compression_ratio": 1.7043795620437956,
  "no_speech_prob": 6.328119343379512e-05}, {"id": 365, "seek": 136586, "start": 1370.74,
  "end": 1372.1, "text": " and combine those together.", "tokens": [50608, 293, 10432,
  729, 1214, 13, 50676], "temperature": 0.0, "avg_logprob": -0.12627686828863424,
  "compression_ratio": 1.7043795620437956, "no_speech_prob": 6.328119343379512e-05},
  {"id": 366, "seek": 136586, "start": 1372.1, "end": 1375.1399999999999, "text":
  " And there''s different ways to generate new vector spaces.", "tokens": [50676,
  400, 456, 311, 819, 2098, 281, 8460, 777, 8062, 7673, 13, 50828], "temperature":
  0.0, "avg_logprob": -0.12627686828863424, "compression_ratio": 1.7043795620437956,
  "no_speech_prob": 6.328119343379512e-05}, {"id": 367, "seek": 136586, "start": 1375.1399999999999,
  "end": 1376.9399999999998, "text": " You can concatenate these together", "tokens":
  [50828, 509, 393, 1588, 7186, 473, 613, 1214, 50918], "temperature": 0.0, "avg_logprob":
  -0.12627686828863424, "compression_ratio": 1.7043795620437956, "no_speech_prob":
  6.328119343379512e-05}, {"id": 368, "seek": 136586, "start": 1376.9399999999998,
  "end": 1378.9799999999998, "text": " and you can do dimensionality reduction", "tokens":
  [50918, 293, 291, 393, 360, 10139, 1860, 11004, 51020], "temperature": 0.0, "avg_logprob":
  -0.12627686828863424, "compression_ratio": 1.7043795620437956, "no_speech_prob":
  6.328119343379512e-05}, {"id": 369, "seek": 136586, "start": 1378.9799999999998,
  "end": 1380.1399999999999, "text": " or you can stack them.", "tokens": [51020,
  420, 291, 393, 8630, 552, 13, 51078], "temperature": 0.0, "avg_logprob": -0.12627686828863424,
  "compression_ratio": 1.7043795620437956, "no_speech_prob": 6.328119343379512e-05},
  {"id": 370, "seek": 136586, "start": 1380.1399999999999, "end": 1382.02, "text":
  " I''m not gonna get into those today.", "tokens": [51078, 286, 478, 406, 799, 483,
  666, 729, 965, 13, 51172], "temperature": 0.0, "avg_logprob": -0.12627686828863424,
  "compression_ratio": 1.7043795620437956, "no_speech_prob": 6.328119343379512e-05},
  {"id": 371, "seek": 136586, "start": 1382.02, "end": 1385.54, "text": " But the
  reality is we''ve got a lot of tools at our disposal", "tokens": [51172, 583, 264,
  4103, 307, 321, 600, 658, 257, 688, 295, 3873, 412, 527, 26400, 51348], "temperature":
  0.0, "avg_logprob": -0.12627686828863424, "compression_ratio": 1.7043795620437956,
  "no_speech_prob": 6.328119343379512e-05}, {"id": 372, "seek": 136586, "start": 1385.54,
  "end": 1388.26, "text": " to be able to query and get at data", "tokens": [51348,
  281, 312, 1075, 281, 14581, 293, 483, 412, 1412, 51484], "temperature": 0.0, "avg_logprob":
  -0.12627686828863424, "compression_ratio": 1.7043795620437956, "no_speech_prob":
  6.328119343379512e-05}, {"id": 373, "seek": 136586, "start": 1388.26, "end": 1389.9399999999998,
  "text": " and relate it in different ways.", "tokens": [51484, 293, 10961, 309,
  294, 819, 2098, 13, 51568], "temperature": 0.0, "avg_logprob": -0.12627686828863424,
  "compression_ratio": 1.7043795620437956, "no_speech_prob": 6.328119343379512e-05},
  {"id": 374, "seek": 136586, "start": 1389.9399999999998, "end": 1394.1799999999998,
  "text": " In fact, what I described for hybrid searches", "tokens": [51568, 682,
  1186, 11, 437, 286, 7619, 337, 13051, 26701, 51780], "temperature": 0.0, "avg_logprob":
  -0.12627686828863424, "compression_ratio": 1.7043795620437956, "no_speech_prob":
  6.328119343379512e-05}, {"id": 375, "seek": 139418, "start": 1394.26, "end": 1397.02,
  "text": " I can go with RRF is just scratching the surface", "tokens": [50368, 286,
  393, 352, 365, 497, 49, 37, 307, 445, 29699, 264, 3753, 50506], "temperature": 0.0,
  "avg_logprob": -0.2643263006723055, "compression_ratio": 1.5272727272727273, "no_speech_prob":
  0.0011563804000616074}, {"id": 376, "seek": 139418, "start": 1397.02, "end": 1401.1000000000001,
  "text": " for what we can do with combining different paradigms.", "tokens": [50506,
  337, 437, 321, 393, 360, 365, 21928, 819, 13480, 328, 2592, 13, 50710], "temperature":
  0.0, "avg_logprob": -0.2643263006723055, "compression_ratio": 1.5272727272727273,
  "no_speech_prob": 0.0011563804000616074}, {"id": 377, "seek": 139418, "start": 1401.1000000000001,
  "end": 1403.5800000000002, "text": " And so this spectrum here on the left,", "tokens":
  [50710, 400, 370, 341, 11143, 510, 322, 264, 1411, 11, 50834], "temperature": 0.0,
  "avg_logprob": -0.2643263006723055, "compression_ratio": 1.5272727272727273, "no_speech_prob":
  0.0011563804000616074}, {"id": 378, "seek": 139418, "start": 1403.5800000000002,
  "end": 1408.5800000000002, "text": " this is token matching or traditional electrical
  search.", "tokens": [50834, 341, 307, 14862, 14324, 420, 5164, 12147, 3164, 13,
  51084], "temperature": 0.0, "avg_logprob": -0.2643263006723055, "compression_ratio":
  1.5272727272727273, "no_speech_prob": 0.0011563804000616074}, {"id": 379, "seek":
  139418, "start": 1412.14, "end": 1417.14, "text": " And you''ll see that things
  like TF IDF,", "tokens": [51262, 400, 291, 603, 536, 300, 721, 411, 40964, 7348,
  37, 11, 51512], "temperature": 0.0, "avg_logprob": -0.2643263006723055, "compression_ratio":
  1.5272727272727273, "no_speech_prob": 0.0011563804000616074}, {"id": 380, "seek":
  139418, "start": 1417.54, "end": 1420.6200000000001, "text": " will be a matching
  those kinds of things fit over here.", "tokens": [51532, 486, 312, 257, 14324, 729,
  3685, 295, 721, 3318, 670, 510, 13, 51686], "temperature": 0.0, "avg_logprob": -0.2643263006723055,
  "compression_ratio": 1.5272727272727273, "no_speech_prob": 0.0011563804000616074},
  {"id": 381, "seek": 139418, "start": 1420.6200000000001, "end": 1422.74, "text":
  " We''ve also, let me just check the, yeah.", "tokens": [51686, 492, 600, 611, 11,
  718, 385, 445, 1520, 264, 11, 1338, 13, 51792], "temperature": 0.0, "avg_logprob":
  -0.2643263006723055, "compression_ratio": 1.5272727272727273, "no_speech_prob":
  0.0011563804000616074}, {"id": 382, "seek": 142274, "start": 1422.74, "end": 1426.26,
  "text": " Okay, we''ve also got on the opposite of the spectrum", "tokens": [50364,
  1033, 11, 321, 600, 611, 658, 322, 264, 6182, 295, 264, 11143, 50540], "temperature":
  0.0, "avg_logprob": -0.1475802584811374, "compression_ratio": 1.688, "no_speech_prob":
  0.00024897450930438936}, {"id": 383, "seek": 142274, "start": 1426.26, "end": 1427.66,
  "text": " this dense vector search.", "tokens": [50540, 341, 18011, 8062, 3164,
  13, 50610], "temperature": 0.0, "avg_logprob": -0.1475802584811374, "compression_ratio":
  1.688, "no_speech_prob": 0.00024897450930438936}, {"id": 384, "seek": 142274, "start":
  1427.66, "end": 1430.6200000000001, "text": " And of course the RRF would fall in
  here", "tokens": [50610, 400, 295, 1164, 264, 497, 49, 37, 576, 2100, 294, 510,
  50758], "temperature": 0.0, "avg_logprob": -0.1475802584811374, "compression_ratio":
  1.688, "no_speech_prob": 0.00024897450930438936}, {"id": 385, "seek": 142274, "start":
  1430.6200000000001, "end": 1434.3, "text": " in this sort of hybrid sparse retrieval",
  "tokens": [50758, 294, 341, 1333, 295, 13051, 637, 11668, 19817, 3337, 50942], "temperature":
  0.0, "avg_logprob": -0.1475802584811374, "compression_ratio": 1.688, "no_speech_prob":
  0.00024897450930438936}, {"id": 386, "seek": 142274, "start": 1434.3, "end": 1436.46,
  "text": " in dense vector search where we''re running them", "tokens": [50942, 294,
  18011, 8062, 3164, 689, 321, 434, 2614, 552, 51050], "temperature": 0.0, "avg_logprob":
  -0.1475802584811374, "compression_ratio": 1.688, "no_speech_prob": 0.00024897450930438936},
  {"id": 387, "seek": 142274, "start": 1436.46, "end": 1440.34, "text": " independently
  and in parallel and combining the results.", "tokens": [51050, 21761, 293, 294,
  8952, 293, 21928, 264, 3542, 13, 51244], "temperature": 0.0, "avg_logprob": -0.1475802584811374,
  "compression_ratio": 1.688, "no_speech_prob": 0.00024897450930438936}, {"id": 388,
  "seek": 142274, "start": 1440.34, "end": 1443.54, "text": " But there''s also mechanisms
  where we could,", "tokens": [51244, 583, 456, 311, 611, 15902, 689, 321, 727, 11,
  51404], "temperature": 0.0, "avg_logprob": -0.1475802584811374, "compression_ratio":
  1.688, "no_speech_prob": 0.00024897450930438936}, {"id": 389, "seek": 142274, "start":
  1443.54, "end": 1446.06, "text": " for example, run sparse retrieval first", "tokens":
  [51404, 337, 1365, 11, 1190, 637, 11668, 19817, 3337, 700, 51530], "temperature":
  0.0, "avg_logprob": -0.1475802584811374, "compression_ratio": 1.688, "no_speech_prob":
  0.00024897450930438936}, {"id": 390, "seek": 142274, "start": 1446.06, "end": 1449.02,
  "text": " and then re-rank using dense embeddings", "tokens": [51530, 293, 550,
  319, 12, 20479, 1228, 18011, 12240, 29432, 51678], "temperature": 0.0, "avg_logprob":
  -0.1475802584811374, "compression_ratio": 1.688, "no_speech_prob": 0.00024897450930438936},
  {"id": 391, "seek": 142274, "start": 1449.02, "end": 1451.7, "text": " or something
  like with mini coil,", "tokens": [51678, 420, 746, 411, 365, 8382, 22225, 11, 51812],
  "temperature": 0.0, "avg_logprob": -0.1475802584811374, "compression_ratio": 1.688,
  "no_speech_prob": 0.00024897450930438936}, {"id": 392, "seek": 145170, "start":
  1451.7, "end": 1453.78, "text": " which I mentioned Jenny from Quadrant''s", "tokens":
  [50364, 597, 286, 2835, 20580, 490, 29619, 7541, 311, 50468], "temperature": 0.0,
  "avg_logprob": -0.1499513584932835, "compression_ratio": 1.7763578274760383, "no_speech_prob":
  0.00028708824538625777}, {"id": 393, "seek": 145170, "start": 1453.78, "end": 1456.42,
  "text": " going to come talk to us about in the AI powered search course.", "tokens":
  [50468, 516, 281, 808, 751, 281, 505, 466, 294, 264, 7318, 17786, 3164, 1164, 13,
  50600], "temperature": 0.0, "avg_logprob": -0.1499513584932835, "compression_ratio":
  1.7763578274760383, "no_speech_prob": 0.00028708824538625777}, {"id": 394, "seek":
  145170, "start": 1456.42, "end": 1459.3, "text": " You can actually run a sparse
  search", "tokens": [50600, 509, 393, 767, 1190, 257, 637, 11668, 3164, 50744], "temperature":
  0.0, "avg_logprob": -0.1499513584932835, "compression_ratio": 1.7763578274760383,
  "no_speech_prob": 0.00028708824538625777}, {"id": 395, "seek": 145170, "start":
  1459.3, "end": 1462.78, "text": " and have embeddings that are sort of adding additional",
  "tokens": [50744, 293, 362, 12240, 29432, 300, 366, 1333, 295, 5127, 4497, 50918],
  "temperature": 0.0, "avg_logprob": -0.1499513584932835, "compression_ratio": 1.7763578274760383,
  "no_speech_prob": 0.00028708824538625777}, {"id": 396, "seek": 145170, "start":
  1462.78, "end": 1465.5, "text": " semantic data to your electrical queries", "tokens":
  [50918, 47982, 1412, 281, 428, 12147, 24109, 51054], "temperature": 0.0, "avg_logprob":
  -0.1499513584932835, "compression_ratio": 1.7763578274760383, "no_speech_prob":
  0.00028708824538625777}, {"id": 397, "seek": 145170, "start": 1465.5, "end": 1468.46,
  "text": " to be able to better leverage semantics", "tokens": [51054, 281, 312,
  1075, 281, 1101, 13982, 4361, 45298, 51202], "temperature": 0.0, "avg_logprob":
  -0.1499513584932835, "compression_ratio": 1.7763578274760383, "no_speech_prob":
  0.00028708824538625777}, {"id": 398, "seek": 145170, "start": 1468.46, "end": 1469.98,
  "text": " as part of your sparse search.", "tokens": [51202, 382, 644, 295, 428,
  637, 11668, 3164, 13, 51278], "temperature": 0.0, "avg_logprob": -0.1499513584932835,
  "compression_ratio": 1.7763578274760383, "no_speech_prob": 0.00028708824538625777},
  {"id": 399, "seek": 145170, "start": 1469.98, "end": 1471.6200000000001, "text":
  " There''s splay, there''s semantic knowledge graphs,", "tokens": [51278, 821, 311,
  262, 2858, 11, 456, 311, 47982, 3601, 24877, 11, 51360], "temperature": 0.0, "avg_logprob":
  -0.1499513584932835, "compression_ratio": 1.7763578274760383, "no_speech_prob":
  0.00028708824538625777}, {"id": 400, "seek": 145170, "start": 1471.6200000000001,
  "end": 1472.98, "text": " there''s all these different techniques", "tokens": [51360,
  456, 311, 439, 613, 819, 7512, 51428], "temperature": 0.0, "avg_logprob": -0.1499513584932835,
  "compression_ratio": 1.7763578274760383, "no_speech_prob": 0.00028708824538625777},
  {"id": 401, "seek": 145170, "start": 1472.98, "end": 1474.7, "text": " that we can
  use to get better search,", "tokens": [51428, 300, 321, 393, 764, 281, 483, 1101,
  3164, 11, 51514], "temperature": 0.0, "avg_logprob": -0.1499513584932835, "compression_ratio":
  1.7763578274760383, "no_speech_prob": 0.00028708824538625777}, {"id": 402, "seek":
  145170, "start": 1474.7, "end": 1477.38, "text": " whether it''s hybrid search or
  leveraging one of the techniques.", "tokens": [51514, 1968, 309, 311, 13051, 3164,
  420, 32666, 472, 295, 264, 7512, 13, 51648], "temperature": 0.0, "avg_logprob":
  -0.1499513584932835, "compression_ratio": 1.7763578274760383, "no_speech_prob":
  0.00028708824538625777}, {"id": 403, "seek": 145170, "start": 1477.38, "end": 1480.78,
  "text": " But I want to just like mention that there''s lots of ways", "tokens":
  [51648, 583, 286, 528, 281, 445, 411, 2152, 300, 456, 311, 3195, 295, 2098, 51818],
  "temperature": 0.0, "avg_logprob": -0.1499513584932835, "compression_ratio": 1.7763578274760383,
  "no_speech_prob": 0.00028708824538625777}, {"id": 404, "seek": 148078, "start":
  1480.78, "end": 1482.62, "text": " to deal with embeddings and to deal", "tokens":
  [50364, 281, 2028, 365, 12240, 29432, 293, 281, 2028, 50456], "temperature": 0.0,
  "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774, "no_speech_prob":
  0.0002039766841335222}, {"id": 405, "seek": 148078, "start": 1482.62, "end": 1485.66,
  "text": " with sparse and dense vectors to combine them", "tokens": [50456, 365,
  637, 11668, 293, 18011, 18875, 281, 10432, 552, 50608], "temperature": 0.0, "avg_logprob":
  -0.1386562796200023, "compression_ratio": 1.9735849056603774, "no_speech_prob":
  0.0002039766841335222}, {"id": 406, "seek": 148078, "start": 1485.66, "end": 1488.62,
  "text": " to improve query understanding and to improve recall.", "tokens": [50608,
  281, 3470, 14581, 3701, 293, 281, 3470, 9901, 13, 50756], "temperature": 0.0, "avg_logprob":
  -0.1386562796200023, "compression_ratio": 1.9735849056603774, "no_speech_prob":
  0.0002039766841335222}, {"id": 407, "seek": 148078, "start": 1488.62, "end": 1493.3799999999999,
  "text": " And so one of the things that I''m experimenting with", "tokens": [50756,
  400, 370, 472, 295, 264, 721, 300, 286, 478, 29070, 365, 50994], "temperature":
  0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 408, "seek": 148078, "start": 1493.3799999999999,
  "end": 1495.1399999999999, "text": " is sort of like an emerging way to do this",
  "tokens": [50994, 307, 1333, 295, 411, 364, 14989, 636, 281, 360, 341, 51082], "temperature":
  0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 409, "seek": 148078, "start": 1495.1399999999999,
  "end": 1496.98, "text": " is something I''m calling wormhole vectors.", "tokens":
  [51082, 307, 746, 286, 478, 5141, 23835, 14094, 18875, 13, 51174], "temperature":
  0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 410, "seek": 148078, "start": 1496.98,
  "end": 1499.86, "text": " And the idea of wormhole vectors is that I''ve got", "tokens":
  [51174, 400, 264, 1558, 295, 23835, 14094, 18875, 307, 300, 286, 600, 658, 51318],
  "temperature": 0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 411, "seek": 148078, "start": 1499.86,
  "end": 1502.3, "text": " these sort of different vector spaces.", "tokens": [51318,
  613, 1333, 295, 819, 8062, 7673, 13, 51440], "temperature": 0.0, "avg_logprob":
  -0.1386562796200023, "compression_ratio": 1.9735849056603774, "no_speech_prob":
  0.0002039766841335222}, {"id": 412, "seek": 148078, "start": 1502.3, "end": 1504.5,
  "text": " I''ve got my sparse lexical vector space,", "tokens": [51440, 286, 600,
  658, 452, 637, 11668, 476, 87, 804, 8062, 1901, 11, 51550], "temperature": 0.0,
  "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774, "no_speech_prob":
  0.0002039766841335222}, {"id": 413, "seek": 148078, "start": 1504.5, "end": 1505.66,
  "text": " which we talked about.", "tokens": [51550, 597, 321, 2825, 466, 13, 51608],
  "temperature": 0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 414, "seek": 148078, "start": 1505.66,
  "end": 1507.98, "text": " I''ve got my dense semantic vector space.", "tokens":
  [51608, 286, 600, 658, 452, 18011, 47982, 8062, 1901, 13, 51724], "temperature":
  0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 415, "seek": 148078, "start": 1507.98,
  "end": 1510.62, "text": " And then I mentioned we can generate behavioral vector",
  "tokens": [51724, 400, 550, 286, 2835, 321, 393, 8460, 19124, 8062, 51856], "temperature":
  0.0, "avg_logprob": -0.1386562796200023, "compression_ratio": 1.9735849056603774,
  "no_speech_prob": 0.0002039766841335222}, {"id": 416, "seek": 151062, "start": 1510.62,
  "end": 1513.6999999999998, "text": " spaces, which I''ll show in just a little bit.",
  "tokens": [50364, 7673, 11, 597, 286, 603, 855, 294, 445, 257, 707, 857, 13, 50518],
  "temperature": 0.0, "avg_logprob": -0.13930073430982687, "compression_ratio": 1.6730769230769231,
  "no_speech_prob": 0.000653287919703871}, {"id": 417, "seek": 151062, "start": 1513.6999999999998,
  "end": 1517.82, "text": " And so I want to walk through what this technique looks
  like.", "tokens": [50518, 400, 370, 286, 528, 281, 1792, 807, 437, 341, 6532, 1542,
  411, 13, 50724], "temperature": 0.0, "avg_logprob": -0.13930073430982687, "compression_ratio":
  1.6730769230769231, "no_speech_prob": 0.000653287919703871}, {"id": 418, "seek":
  151062, "start": 1517.82, "end": 1521.1799999999998, "text": " And I do want to
  frame this talk as this is sort of like", "tokens": [50724, 400, 286, 360, 528,
  281, 3920, 341, 751, 382, 341, 307, 1333, 295, 411, 50892], "temperature": 0.0,
  "avg_logprob": -0.13930073430982687, "compression_ratio": 1.6730769230769231, "no_speech_prob":
  0.000653287919703871}, {"id": 419, "seek": 151062, "start": 1521.1799999999998,
  "end": 1522.7399999999998, "text": " new and emerging.", "tokens": [50892, 777,
  293, 14989, 13, 50970], "temperature": 0.0, "avg_logprob": -0.13930073430982687,
  "compression_ratio": 1.6730769230769231, "no_speech_prob": 0.000653287919703871},
  {"id": 420, "seek": 151062, "start": 1522.7399999999998, "end": 1526.6999999999998,
  "text": " I''ve got lots of experience doing some of this", "tokens": [50970, 286,
  600, 658, 3195, 295, 1752, 884, 512, 295, 341, 51168], "temperature": 0.0, "avg_logprob":
  -0.13930073430982687, "compression_ratio": 1.6730769230769231, "no_speech_prob":
  0.000653287919703871}, {"id": 421, "seek": 151062, "start": 1526.6999999999998,
  "end": 1527.9799999999998, "text": " across different vector spaces.", "tokens":
  [51168, 2108, 819, 8062, 7673, 13, 51232], "temperature": 0.0, "avg_logprob": -0.13930073430982687,
  "compression_ratio": 1.6730769230769231, "no_speech_prob": 0.000653287919703871},
  {"id": 422, "seek": 151062, "start": 1527.9799999999998, "end": 1531.02, "text":
  " But there''s a lot of things that I so need to iron out", "tokens": [51232, 583,
  456, 311, 257, 688, 295, 721, 300, 286, 370, 643, 281, 6497, 484, 51384], "temperature":
  0.0, "avg_logprob": -0.13930073430982687, "compression_ratio": 1.6730769230769231,
  "no_speech_prob": 0.000653287919703871}, {"id": 423, "seek": 151062, "start": 1531.02,
  "end": 1532.8999999999999, "text": " in terms of best practices for doing this.",
  "tokens": [51384, 294, 2115, 295, 1151, 7525, 337, 884, 341, 13, 51478], "temperature":
  0.0, "avg_logprob": -0.13930073430982687, "compression_ratio": 1.6730769230769231,
  "no_speech_prob": 0.000653287919703871}, {"id": 424, "seek": 151062, "start": 1532.8999999999999,
  "end": 1536.9799999999998, "text": " So treat this as something that''s emerging",
  "tokens": [51478, 407, 2387, 341, 382, 746, 300, 311, 14989, 51682], "temperature":
  0.0, "avg_logprob": -0.13930073430982687, "compression_ratio": 1.6730769230769231,
  "no_speech_prob": 0.000653287919703871}, {"id": 425, "seek": 151062, "start": 1536.9799999999998,
  "end": 1538.1, "text": " and something you can play with.", "tokens": [51682, 293,
  746, 291, 393, 862, 365, 13, 51738], "temperature": 0.0, "avg_logprob": -0.13930073430982687,
  "compression_ratio": 1.6730769230769231, "no_speech_prob": 0.000653287919703871},
  {"id": 426, "seek": 153810, "start": 1538.1, "end": 1541.1, "text": " And I think
  the intuition will be really helpful.", "tokens": [50364, 400, 286, 519, 264, 24002,
  486, 312, 534, 4961, 13, 50514], "temperature": 0.0, "avg_logprob": -0.1733814380787037,
  "compression_ratio": 1.7692307692307692, "no_speech_prob": 0.0001525890693301335},
  {"id": 427, "seek": 153810, "start": 1541.1, "end": 1543.78, "text": " But I''m,
  you know, if in preparation for the course", "tokens": [50514, 583, 286, 478, 11,
  291, 458, 11, 498, 294, 13081, 337, 264, 1164, 50648], "temperature": 0.0, "avg_logprob":
  -0.1733814380787037, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0001525890693301335}, {"id": 428, "seek": 153810, "start": 1543.78, "end": 1545.62,
  "text": " and going forward, I''m going to be doing a lot more", "tokens": [50648,
  293, 516, 2128, 11, 286, 478, 516, 281, 312, 884, 257, 688, 544, 50740], "temperature":
  0.0, "avg_logprob": -0.1733814380787037, "compression_ratio": 1.7692307692307692,
  "no_speech_prob": 0.0001525890693301335}, {"id": 429, "seek": 153810, "start": 1545.62,
  "end": 1547.74, "text": " in terms of concrete examples for this.", "tokens": [50740,
  294, 2115, 295, 9859, 5110, 337, 341, 13, 50846], "temperature": 0.0, "avg_logprob":
  -0.1733814380787037, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0001525890693301335}, {"id": 430, "seek": 153810, "start": 1547.74, "end": 1552.58,
  "text": " And so I don''t want to get into quantum physics or, you know,", "tokens":
  [50846, 400, 370, 286, 500, 380, 528, 281, 483, 666, 13018, 10649, 420, 11, 291,
  458, 11, 51088], "temperature": 0.0, "avg_logprob": -0.1733814380787037, "compression_ratio":
  1.7692307692307692, "no_speech_prob": 0.0001525890693301335}, {"id": 431, "seek":
  153810, "start": 1552.58, "end": 1553.3799999999999, "text": " physics in general.",
  "tokens": [51088, 10649, 294, 2674, 13, 51128], "temperature": 0.0, "avg_logprob":
  -0.1733814380787037, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0001525890693301335}, {"id": 432, "seek": 153810, "start": 1553.3799999999999,
  "end": 1555.5, "text": " But, you know, wormholes, if you''re not familiar,", "tokens":
  [51128, 583, 11, 291, 458, 11, 23835, 37894, 11, 498, 291, 434, 406, 4963, 11, 51234],
  "temperature": 0.0, "avg_logprob": -0.1733814380787037, "compression_ratio": 1.7692307692307692,
  "no_speech_prob": 0.0001525890693301335}, {"id": 433, "seek": 153810, "start": 1555.5,
  "end": 1559.1, "text": " are essentially passages through space time.", "tokens":
  [51234, 366, 4476, 31589, 807, 1901, 565, 13, 51414], "temperature": 0.0, "avg_logprob":
  -0.1733814380787037, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0001525890693301335}, {"id": 434, "seek": 153810, "start": 1559.1, "end": 1562.1799999999998,
  "text": " You can think of it as, you know, the ability to, you know,", "tokens":
  [51414, 509, 393, 519, 295, 309, 382, 11, 291, 458, 11, 264, 3485, 281, 11, 291,
  458, 11, 51568], "temperature": 0.0, "avg_logprob": -0.1733814380787037, "compression_ratio":
  1.7692307692307692, "no_speech_prob": 0.0001525890693301335}, {"id": 435, "seek":
  153810, "start": 1562.1799999999998, "end": 1566.1399999999999, "text": " go from
  one point in space to another point in space", "tokens": [51568, 352, 490, 472,
  935, 294, 1901, 281, 1071, 935, 294, 1901, 51766], "temperature": 0.0, "avg_logprob":
  -0.1733814380787037, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0001525890693301335}, {"id": 436, "seek": 156614, "start": 1566.14, "end": 1568.66,
  "text": " and essentially like hop there instantly.", "tokens": [50364, 293, 4476,
  411, 3818, 456, 13518, 13, 50490], "temperature": 0.0, "avg_logprob": -0.25437104317449755,
  "compression_ratio": 1.5805243445692885, "no_speech_prob": 0.001434129080735147},
  {"id": 437, "seek": 156614, "start": 1568.66, "end": 1570.7800000000002, "text":
  " I could get into Einstein Rosenberg''s", "tokens": [50490, 286, 727, 483, 666,
  23486, 33630, 6873, 311, 50596], "temperature": 0.0, "avg_logprob": -0.25437104317449755,
  "compression_ratio": 1.5805243445692885, "no_speech_prob": 0.001434129080735147},
  {"id": 438, "seek": 156614, "start": 1570.7800000000002, "end": 1572.6200000000001,
  "text": " and all that kind of stuff, but don''t really want to", "tokens": [50596,
  293, 439, 300, 733, 295, 1507, 11, 457, 500, 380, 534, 528, 281, 50688], "temperature":
  0.0, "avg_logprob": -0.25437104317449755, "compression_ratio": 1.5805243445692885,
  "no_speech_prob": 0.001434129080735147}, {"id": 439, "seek": 156614, "start": 1572.6200000000001,
  "end": 1575.5, "text": " for purposes of today.", "tokens": [50688, 337, 9932, 295,
  965, 13, 50832], "temperature": 0.0, "avg_logprob": -0.25437104317449755, "compression_ratio":
  1.5805243445692885, "no_speech_prob": 0.001434129080735147}, {"id": 440, "seek":
  156614, "start": 1575.5, "end": 1579.46, "text": " And what I do want to do though
  is talk about,", "tokens": [50832, 400, 437, 286, 360, 528, 281, 360, 1673, 307,
  751, 466, 11, 51030], "temperature": 0.0, "avg_logprob": -0.25437104317449755, "compression_ratio":
  1.5805243445692885, "no_speech_prob": 0.001434129080735147}, {"id": 441, "seek":
  156614, "start": 1579.46, "end": 1580.9, "text": " oh, give me a second.", "tokens":
  [51030, 1954, 11, 976, 385, 257, 1150, 13, 51102], "temperature": 0.0, "avg_logprob":
  -0.25437104317449755, "compression_ratio": 1.5805243445692885, "no_speech_prob":
  0.001434129080735147}, {"id": 442, "seek": 156614, "start": 1580.9, "end": 1582.8200000000002,
  "text": " Well, I''ll skip over this.", "tokens": [51102, 1042, 11, 286, 603, 10023,
  670, 341, 13, 51198], "temperature": 0.0, "avg_logprob": -0.25437104317449755, "compression_ratio":
  1.5805243445692885, "no_speech_prob": 0.001434129080735147}, {"id": 443, "seek":
  156614, "start": 1582.8200000000002, "end": 1584.66, "text": " We''ll maybe come
  to that in the Q&A", "tokens": [51198, 492, 603, 1310, 808, 281, 300, 294, 264,
  1249, 5, 32, 51290], "temperature": 0.0, "avg_logprob": -0.25437104317449755, "compression_ratio":
  1.5805243445692885, "no_speech_prob": 0.001434129080735147}, {"id": 444, "seek":
  156614, "start": 1584.66, "end": 1589.8600000000001, "text": " if Demetri''s interested
  in talking about this notion", "tokens": [51290, 498, 4686, 302, 470, 311, 3102,
  294, 1417, 466, 341, 10710, 51550], "temperature": 0.0, "avg_logprob": -0.25437104317449755,
  "compression_ratio": 1.5805243445692885, "no_speech_prob": 0.001434129080735147},
  {"id": 445, "seek": 156614, "start": 1589.8600000000001, "end": 1593.6200000000001,
  "text": " of entanglement and how that relates to wormholes.", "tokens": [51550,
  295, 948, 656, 3054, 293, 577, 300, 16155, 281, 23835, 37894, 13, 51738], "temperature":
  0.0, "avg_logprob": -0.25437104317449755, "compression_ratio": 1.5805243445692885,
  "no_speech_prob": 0.001434129080735147}, {"id": 446, "seek": 156614, "start": 1593.6200000000001,
  "end": 1594.9, "text": " It might be interesting later.", "tokens": [51738, 467,
  1062, 312, 1880, 1780, 13, 51802], "temperature": 0.0, "avg_logprob": -0.25437104317449755,
  "compression_ratio": 1.5805243445692885, "no_speech_prob": 0.001434129080735147},
  {"id": 447, "seek": 159490, "start": 1594.9, "end": 1598.3400000000001, "text":
  " But I don''t, this is about search, not about quantum physics", "tokens": [50364,
  583, 286, 500, 380, 11, 341, 307, 466, 3164, 11, 406, 466, 13018, 10649, 50536],
  "temperature": 0.0, "avg_logprob": -0.17942346152612718, "compression_ratio": 1.8705357142857142,
  "no_speech_prob": 0.00015755061758682132}, {"id": 448, "seek": 159490, "start":
  1598.3400000000001, "end": 1599.3400000000001, "text": " and physics in general.",
  "tokens": [50536, 293, 10649, 294, 2674, 13, 50586], "temperature": 0.0, "avg_logprob":
  -0.17942346152612718, "compression_ratio": 1.8705357142857142, "no_speech_prob":
  0.00015755061758682132}, {"id": 449, "seek": 159490, "start": 1599.3400000000001,
  "end": 1603.42, "text": " So this is what it means to generate a wormhole vector",
  "tokens": [50586, 407, 341, 307, 437, 309, 1355, 281, 8460, 257, 23835, 14094, 8062,
  50790], "temperature": 0.0, "avg_logprob": -0.17942346152612718, "compression_ratio":
  1.8705357142857142, "no_speech_prob": 0.00015755061758682132}, {"id": 450, "seek":
  159490, "start": 1603.42, "end": 1604.6200000000001, "text": " bi-practically.",
  "tokens": [50790, 3228, 12, 42559, 984, 13, 50850], "temperature": 0.0, "avg_logprob":
  -0.17942346152612718, "compression_ratio": 1.8705357142857142, "no_speech_prob":
  0.00015755061758682132}, {"id": 451, "seek": 159490, "start": 1604.6200000000001,
  "end": 1609.14, "text": " So if you want to generate a wormhole vector,", "tokens":
  [50850, 407, 498, 291, 528, 281, 8460, 257, 23835, 14094, 8062, 11, 51076], "temperature":
  0.0, "avg_logprob": -0.17942346152612718, "compression_ratio": 1.8705357142857142,
  "no_speech_prob": 0.00015755061758682132}, {"id": 452, "seek": 159490, "start":
  1609.14, "end": 1612.02, "text": " there''s a fundamental base reality", "tokens":
  [51076, 456, 311, 257, 8088, 3096, 4103, 51220], "temperature": 0.0, "avg_logprob":
  -0.17942346152612718, "compression_ratio": 1.8705357142857142, "no_speech_prob":
  0.00015755061758682132}, {"id": 453, "seek": 159490, "start": 1612.02, "end": 1614.3400000000001,
  "text": " of all these vector spaces, meaning if I query", "tokens": [51220, 295,
  439, 613, 8062, 7673, 11, 3620, 498, 286, 14581, 51336], "temperature": 0.0, "avg_logprob":
  -0.17942346152612718, "compression_ratio": 1.8705357142857142, "no_speech_prob":
  0.00015755061758682132}, {"id": 454, "seek": 159490, "start": 1614.3400000000001,
  "end": 1616.74, "text": " with an embedding and a dense vector space,", "tokens":
  [51336, 365, 364, 12240, 3584, 293, 257, 18011, 8062, 1901, 11, 51456], "temperature":
  0.0, "avg_logprob": -0.17942346152612718, "compression_ratio": 1.8705357142857142,
  "no_speech_prob": 0.00015755061758682132}, {"id": 455, "seek": 159490, "start":
  1616.74, "end": 1619.5, "text": " or I query with a lexical query over here,", "tokens":
  [51456, 420, 286, 14581, 365, 257, 476, 87, 804, 14581, 670, 510, 11, 51594], "temperature":
  0.0, "avg_logprob": -0.17942346152612718, "compression_ratio": 1.8705357142857142,
  "no_speech_prob": 0.00015755061758682132}, {"id": 456, "seek": 159490, "start":
  1619.5, "end": 1623.18, "text": " or I query with IDs and user behavior over here,",
  "tokens": [51594, 420, 286, 14581, 365, 48212, 293, 4195, 5223, 670, 510, 11, 51778],
  "temperature": 0.0, "avg_logprob": -0.17942346152612718, "compression_ratio": 1.8705357142857142,
  "no_speech_prob": 0.00015755061758682132}, {"id": 457, "seek": 162318, "start":
  1623.18, "end": 1628.5800000000002, "text": " all of those queries ultimately boil
  down to matching something.", "tokens": [50364, 439, 295, 729, 24109, 6284, 13329,
  760, 281, 14324, 746, 13, 50634], "temperature": 0.0, "avg_logprob": -0.12074902424445519,
  "compression_ratio": 1.7883817427385893, "no_speech_prob": 0.0001317524875048548},
  {"id": 458, "seek": 162318, "start": 1628.5800000000002, "end": 1631.54, "text":
  " And the something that they match is really critical", "tokens": [50634, 400,
  264, 746, 300, 436, 2995, 307, 534, 4924, 50782], "temperature": 0.0, "avg_logprob":
  -0.12074902424445519, "compression_ratio": 1.7883817427385893, "no_speech_prob":
  0.0001317524875048548}, {"id": 459, "seek": 162318, "start": 1631.54, "end": 1634.9,
  "text": " to how we understand queries and how we understand relevance.", "tokens":
  [50782, 281, 577, 321, 1223, 24109, 293, 577, 321, 1223, 32684, 13, 50950], "temperature":
  0.0, "avg_logprob": -0.12074902424445519, "compression_ratio": 1.7883817427385893,
  "no_speech_prob": 0.0001317524875048548}, {"id": 460, "seek": 162318, "start": 1634.9,
  "end": 1637.8200000000002, "text": " And what they boil down to is a document set.",
  "tokens": [50950, 400, 437, 436, 13329, 760, 281, 307, 257, 4166, 992, 13, 51096],
  "temperature": 0.0, "avg_logprob": -0.12074902424445519, "compression_ratio": 1.7883817427385893,
  "no_speech_prob": 0.0001317524875048548}, {"id": 461, "seek": 162318, "start": 1637.8200000000002,
  "end": 1640.5800000000002, "text": " So if you run an embedding search over here,",
  "tokens": [51096, 407, 498, 291, 1190, 364, 12240, 3584, 3164, 670, 510, 11, 51234],
  "temperature": 0.0, "avg_logprob": -0.12074902424445519, "compression_ratio": 1.7883817427385893,
  "no_speech_prob": 0.0001317524875048548}, {"id": 462, "seek": 162318, "start": 1640.5800000000002,
  "end": 1642.98, "text": " you find a point in vector space.", "tokens": [51234,
  291, 915, 257, 935, 294, 8062, 1901, 13, 51354], "temperature": 0.0, "avg_logprob":
  -0.12074902424445519, "compression_ratio": 1.7883817427385893, "no_speech_prob":
  0.0001317524875048548}, {"id": 463, "seek": 162318, "start": 1642.98, "end": 1646.54,
  "text": " And if it''s a dense space, you typically", "tokens": [51354, 400, 498,
  309, 311, 257, 18011, 1901, 11, 291, 5850, 51532], "temperature": 0.0, "avg_logprob":
  -0.12074902424445519, "compression_ratio": 1.7883817427385893, "no_speech_prob":
  0.0001317524875048548}, {"id": 464, "seek": 162318, "start": 1646.54, "end": 1649.26,
  "text": " do an approximate nearest neighbor algorithm,", "tokens": [51532, 360,
  364, 30874, 23831, 5987, 9284, 11, 51668], "temperature": 0.0, "avg_logprob": -0.12074902424445519,
  "compression_ratio": 1.7883817427385893, "no_speech_prob": 0.0001317524875048548},
  {"id": 465, "seek": 162318, "start": 1649.26, "end": 1652.46, "text": " or otherwise
  find the nearest neighbors", "tokens": [51668, 420, 5911, 915, 264, 23831, 12512,
  51828], "temperature": 0.0, "avg_logprob": -0.12074902424445519, "compression_ratio":
  1.7883817427385893, "no_speech_prob": 0.0001317524875048548}, {"id": 466, "seek":
  165246, "start": 1652.46, "end": 1653.94, "text": " to whatever point you''re querying.",
  "tokens": [50364, 281, 2035, 935, 291, 434, 7083, 1840, 13, 50438], "temperature":
  0.0, "avg_logprob": -0.15615109879841177, "compression_ratio": 1.8913857677902621,
  "no_speech_prob": 0.0002027682203333825}, {"id": 467, "seek": 165246, "start": 1653.94,
  "end": 1656.46, "text": " And those are your relevant documents.", "tokens": [50438,
  400, 729, 366, 428, 7340, 8512, 13, 50564], "temperature": 0.0, "avg_logprob": -0.15615109879841177,
  "compression_ratio": 1.8913857677902621, "no_speech_prob": 0.0002027682203333825},
  {"id": 468, "seek": 165246, "start": 1656.46, "end": 1657.98, "text": " Those documents
  form a set.", "tokens": [50564, 3950, 8512, 1254, 257, 992, 13, 50640], "temperature":
  0.0, "avg_logprob": -0.15615109879841177, "compression_ratio": 1.8913857677902621,
  "no_speech_prob": 0.0002027682203333825}, {"id": 469, "seek": 165246, "start": 1657.98,
  "end": 1660.26, "text": " And you can cut off the threshold at any point to say,",
  "tokens": [50640, 400, 291, 393, 1723, 766, 264, 14678, 412, 604, 935, 281, 584,
  11, 50754], "temperature": 0.0, "avg_logprob": -0.15615109879841177, "compression_ratio":
  1.8913857677902621, "no_speech_prob": 0.0002027682203333825}, {"id": 470, "seek":
  165246, "start": 1660.26, "end": 1662.1000000000001, "text": " these are the documents
  that matched.", "tokens": [50754, 613, 366, 264, 8512, 300, 21447, 13, 50846], "temperature":
  0.0, "avg_logprob": -0.15615109879841177, "compression_ratio": 1.8913857677902621,
  "no_speech_prob": 0.0002027682203333825}, {"id": 471, "seek": 165246, "start": 1662.1000000000001,
  "end": 1664.46, "text": " But that set of documents collectively", "tokens": [50846,
  583, 300, 992, 295, 8512, 24341, 50964], "temperature": 0.0, "avg_logprob": -0.15615109879841177,
  "compression_ratio": 1.8913857677902621, "no_speech_prob": 0.0002027682203333825},
  {"id": 472, "seek": 165246, "start": 1664.46, "end": 1667.8600000000001, "text":
  " has some meaning that some relationships within it", "tokens": [50964, 575, 512,
  3620, 300, 512, 6159, 1951, 309, 51134], "temperature": 0.0, "avg_logprob": -0.15615109879841177,
  "compression_ratio": 1.8913857677902621, "no_speech_prob": 0.0002027682203333825},
  {"id": 473, "seek": 165246, "start": 1667.8600000000001, "end": 1670.22, "text":
  " that represent the meaning of that query.", "tokens": [51134, 300, 2906, 264,
  3620, 295, 300, 14581, 13, 51252], "temperature": 0.0, "avg_logprob": -0.15615109879841177,
  "compression_ratio": 1.8913857677902621, "no_speech_prob": 0.0002027682203333825},
  {"id": 474, "seek": 165246, "start": 1670.22, "end": 1673.1000000000001, "text":
  " Likewise, if I do a keyword search,", "tokens": [51252, 30269, 11, 498, 286, 360,
  257, 20428, 3164, 11, 51396], "temperature": 0.0, "avg_logprob": -0.15615109879841177,
  "compression_ratio": 1.8913857677902621, "no_speech_prob": 0.0002027682203333825},
  {"id": 475, "seek": 165246, "start": 1673.1000000000001, "end": 1674.7, "text":
  " I find a document set.", "tokens": [51396, 286, 915, 257, 4166, 992, 13, 51476],
  "temperature": 0.0, "avg_logprob": -0.15615109879841177, "compression_ratio": 1.8913857677902621,
  "no_speech_prob": 0.0002027682203333825}, {"id": 476, "seek": 165246, "start": 1674.7,
  "end": 1677.1000000000001, "text": " And the collection of those documents", "tokens":
  [51476, 400, 264, 5765, 295, 729, 8512, 51596], "temperature": 0.0, "avg_logprob":
  -0.15615109879841177, "compression_ratio": 1.8913857677902621, "no_speech_prob":
  0.0002027682203333825}, {"id": 477, "seek": 165246, "start": 1677.1000000000001,
  "end": 1679.5, "text": " represents the meaning of that query,", "tokens": [51596,
  8855, 264, 3620, 295, 300, 14581, 11, 51716], "temperature": 0.0, "avg_logprob":
  -0.15615109879841177, "compression_ratio": 1.8913857677902621, "no_speech_prob":
  0.0002027682203333825}, {"id": 478, "seek": 165246, "start": 1679.5, "end": 1681.54,
  "text": " at least as we''ve been able to represent it", "tokens": [51716, 412,
  1935, 382, 321, 600, 668, 1075, 281, 2906, 309, 51818], "temperature": 0.0, "avg_logprob":
  -0.15615109879841177, "compression_ratio": 1.8913857677902621, "no_speech_prob":
  0.0002027682203333825}, {"id": 479, "seek": 168154, "start": 1681.54, "end": 1683.62,
  "text": " in that vector space, same thing over here.", "tokens": [50364, 294, 300,
  8062, 1901, 11, 912, 551, 670, 510, 13, 50468], "temperature": 0.0, "avg_logprob":
  -0.19520183231519617, "compression_ratio": 1.8846153846153846, "no_speech_prob":
  2.7283009330858476e-05}, {"id": 480, "seek": 168154, "start": 1683.62, "end": 1685.74,
  "text": " So the idea of a wormhole vector is", "tokens": [50468, 407, 264, 1558,
  295, 257, 23835, 14094, 8062, 307, 50574], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 481, "seek": 168154, "start": 1685.74, "end": 1690.06, "text": " if I want
  to query in one vector space", "tokens": [50574, 498, 286, 528, 281, 14581, 294,
  472, 8062, 1901, 50790], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 482, "seek": 168154, "start": 1690.06, "end": 1693.74, "text": " and find
  a corresponding region in another vector space", "tokens": [50790, 293, 915, 257,
  11760, 4458, 294, 1071, 8062, 1901, 50974], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 483, "seek": 168154, "start": 1693.74, "end": 1698.3799999999999, "text":
  " that shares the same meaning semantically,", "tokens": [50974, 300, 12182, 264,
  912, 3620, 4361, 49505, 11, 51206], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 484, "seek": 168154, "start": 1698.3799999999999, "end": 1700.8999999999999,
  "text": " then what I''ll do is I''ll query in the current vector space,", "tokens":
  [51206, 550, 437, 286, 603, 360, 307, 286, 603, 14581, 294, 264, 2190, 8062, 1901,
  11, 51332], "temperature": 0.0, "avg_logprob": -0.19520183231519617, "compression_ratio":
  1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05}, {"id": 485, "seek":
  168154, "start": 1700.8999999999999, "end": 1702.94, "text": " for example, within
  embedding here.", "tokens": [51332, 337, 1365, 11, 1951, 12240, 3584, 510, 13, 51434],
  "temperature": 0.0, "avg_logprob": -0.19520183231519617, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 2.7283009330858476e-05}, {"id": 486, "seek": 168154, "start":
  1702.94, "end": 1703.8999999999999, "text": " Actually, let me start it here.",
  "tokens": [51434, 5135, 11, 718, 385, 722, 309, 510, 13, 51482], "temperature":
  0.0, "avg_logprob": -0.19520183231519617, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 2.7283009330858476e-05}, {"id": 487, "seek": 168154, "start":
  1703.8999999999999, "end": 1706.5, "text": " I''ll query in the sparse-like-school
  vector space.", "tokens": [51482, 286, 603, 14581, 294, 264, 637, 11668, 12, 4092,
  12, 82, 21856, 8062, 1901, 13, 51612], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 488, "seek": 168154, "start": 1706.5, "end": 1708.7, "text": " I will then
  find a relevant document set.", "tokens": [51612, 286, 486, 550, 915, 257, 7340,
  4166, 992, 13, 51722], "temperature": 0.0, "avg_logprob": -0.19520183231519617,
  "compression_ratio": 1.8846153846153846, "no_speech_prob": 2.7283009330858476e-05},
  {"id": 489, "seek": 168154, "start": 1708.7, "end": 1709.82, "text": " This is what
  search does.", "tokens": [51722, 639, 307, 437, 3164, 775, 13, 51778], "temperature":
  0.0, "avg_logprob": -0.19520183231519617, "compression_ratio": 1.8846153846153846,
  "no_speech_prob": 2.7283009330858476e-05}, {"id": 490, "seek": 168154, "start":
  1709.82, "end": 1711.3799999999999, "text": " It finds a document set.", "tokens":
  [51778, 467, 10704, 257, 4166, 992, 13, 51856], "temperature": 0.0, "avg_logprob":
  -0.19520183231519617, "compression_ratio": 1.8846153846153846, "no_speech_prob":
  2.7283009330858476e-05}, {"id": 491, "seek": 171138, "start": 1711.38, "end": 1713.6200000000001,
  "text": " And then I will derive a wormhole vector", "tokens": [50364, 400, 550,
  286, 486, 28446, 257, 23835, 14094, 8062, 50476], "temperature": 0.0, "avg_logprob":
  -0.15189586836716223, "compression_ratio": 1.897872340425532, "no_speech_prob":
  2.2624504708801396e-05}, {"id": 492, "seek": 171138, "start": 1713.6200000000001,
  "end": 1717.14, "text": " to a corresponding region of another vector space.", "tokens":
  [50476, 281, 257, 11760, 4458, 295, 1071, 8062, 1901, 13, 50652], "temperature":
  0.0, "avg_logprob": -0.15189586836716223, "compression_ratio": 1.897872340425532,
  "no_speech_prob": 2.2624504708801396e-05}, {"id": 493, "seek": 171138, "start":
  1717.14, "end": 1720.5, "text": " So for example, once I found a document set over
  here,", "tokens": [50652, 407, 337, 1365, 11, 1564, 286, 1352, 257, 4166, 992, 670,
  510, 11, 50820], "temperature": 0.0, "avg_logprob": -0.15189586836716223, "compression_ratio":
  1.897872340425532, "no_speech_prob": 2.2624504708801396e-05}, {"id": 494, "seek":
  171138, "start": 1720.5, "end": 1723.8600000000001, "text": " I will use that document
  set to generate,", "tokens": [50820, 286, 486, 764, 300, 4166, 992, 281, 8460, 11,
  50988], "temperature": 0.0, "avg_logprob": -0.15189586836716223, "compression_ratio":
  1.897872340425532, "no_speech_prob": 2.2624504708801396e-05}, {"id": 495, "seek":
  171138, "start": 1723.8600000000001, "end": 1725.3400000000001, "text": " what I''m
  calling a wormhole vector,", "tokens": [50988, 437, 286, 478, 5141, 257, 23835,
  14094, 8062, 11, 51062], "temperature": 0.0, "avg_logprob": -0.15189586836716223,
  "compression_ratio": 1.897872340425532, "no_speech_prob": 2.2624504708801396e-05},
  {"id": 496, "seek": 171138, "start": 1725.3400000000001, "end": 1728.0200000000002,
  "text": " but to generate a vector that will allow me", "tokens": [51062, 457, 281,
  8460, 257, 8062, 300, 486, 2089, 385, 51196], "temperature": 0.0, "avg_logprob":
  -0.15189586836716223, "compression_ratio": 1.897872340425532, "no_speech_prob":
  2.2624504708801396e-05}, {"id": 497, "seek": 171138, "start": 1728.0200000000002,
  "end": 1730.74, "text": " to query in the other vector space or hop or traverse",
  "tokens": [51196, 281, 14581, 294, 264, 661, 8062, 1901, 420, 3818, 420, 45674,
  51332], "temperature": 0.0, "avg_logprob": -0.15189586836716223, "compression_ratio":
  1.897872340425532, "no_speech_prob": 2.2624504708801396e-05}, {"id": 498, "seek":
  171138, "start": 1730.74, "end": 1732.6200000000001, "text": " to the other vector
  space instantly,", "tokens": [51332, 281, 264, 661, 8062, 1901, 13518, 11, 51426],
  "temperature": 0.0, "avg_logprob": -0.15189586836716223, "compression_ratio": 1.897872340425532,
  "no_speech_prob": 2.2624504708801396e-05}, {"id": 499, "seek": 171138, "start":
  1732.6200000000001, "end": 1736.0200000000002, "text": " to a region that shares
  a similar semantic meaning", "tokens": [51426, 281, 257, 4458, 300, 12182, 257,
  2531, 47982, 3620, 51596], "temperature": 0.0, "avg_logprob": -0.15189586836716223,
  "compression_ratio": 1.897872340425532, "no_speech_prob": 2.2624504708801396e-05},
  {"id": 500, "seek": 171138, "start": 1736.0200000000002, "end": 1738.6200000000001,
  "text": " to the region in the Lexical space.", "tokens": [51596, 281, 264, 4458,
  294, 264, 24086, 804, 1901, 13, 51726], "temperature": 0.0, "avg_logprob": -0.15189586836716223,
  "compression_ratio": 1.897872340425532, "no_speech_prob": 2.2624504708801396e-05},
  {"id": 501, "seek": 173862, "start": 1738.62, "end": 1742.58, "text": " Then once
  I''ve found that vector for the other vector space,", "tokens": [50364, 1396, 1564,
  286, 600, 1352, 300, 8062, 337, 264, 661, 8062, 1901, 11, 50562], "temperature":
  0.0, "avg_logprob": -0.15582829814846233, "compression_ratio": 1.8911290322580645,
  "no_speech_prob": 0.00017260682943742722}, {"id": 502, "seek": 173862, "start":
  1742.58, "end": 1744.86, "text": " I will run that query in the other vector space",
  "tokens": [50562, 286, 486, 1190, 300, 14581, 294, 264, 661, 8062, 1901, 50676],
  "temperature": 0.0, "avg_logprob": -0.15582829814846233, "compression_ratio": 1.8911290322580645,
  "no_speech_prob": 0.00017260682943742722}, {"id": 503, "seek": 173862, "start":
  1744.86, "end": 1746.82, "text": " to traverse to that vector space,", "tokens":
  [50676, 281, 45674, 281, 300, 8062, 1901, 11, 50774], "temperature": 0.0, "avg_logprob":
  -0.15582829814846233, "compression_ratio": 1.8911290322580645, "no_speech_prob":
  0.00017260682943742722}, {"id": 504, "seek": 173862, "start": 1746.82, "end": 1748.4599999999998,
  "text": " and then I''ll repeat as needed.", "tokens": [50774, 293, 550, 286, 603,
  7149, 382, 2978, 13, 50856], "temperature": 0.0, "avg_logprob": -0.15582829814846233,
  "compression_ratio": 1.8911290322580645, "no_speech_prob": 0.00017260682943742722},
  {"id": 505, "seek": 173862, "start": 1748.4599999999998, "end": 1750.9799999999998,
  "text": " So I can actually hop back and forth between vector spaces", "tokens":
  [50856, 407, 286, 393, 767, 3818, 646, 293, 5220, 1296, 8062, 7673, 50982], "temperature":
  0.0, "avg_logprob": -0.15582829814846233, "compression_ratio": 1.8911290322580645,
  "no_speech_prob": 0.00017260682943742722}, {"id": 506, "seek": 173862, "start":
  1750.9799999999998, "end": 1753.26, "text": " to find and collect documents,", "tokens":
  [50982, 281, 915, 293, 2500, 8512, 11, 51096], "temperature": 0.0, "avg_logprob":
  -0.15582829814846233, "compression_ratio": 1.8911290322580645, "no_speech_prob":
  0.00017260682943742722}, {"id": 507, "seek": 173862, "start": 1753.26, "end": 1754.9799999999998,
  "text": " to try to better understand them,", "tokens": [51096, 281, 853, 281, 1101,
  1223, 552, 11, 51182], "temperature": 0.0, "avg_logprob": -0.15582829814846233,
  "compression_ratio": 1.8911290322580645, "no_speech_prob": 0.00017260682943742722},
  {"id": 508, "seek": 173862, "start": 1754.9799999999998, "end": 1758.86, "text":
  " and then to use that understanding to take those documents", "tokens": [51182,
  293, 550, 281, 764, 300, 3701, 281, 747, 729, 8512, 51376], "temperature": 0.0,
  "avg_logprob": -0.15582829814846233, "compression_ratio": 1.8911290322580645, "no_speech_prob":
  0.00017260682943742722}, {"id": 509, "seek": 173862, "start": 1758.86, "end": 1761.34,
  "text": " and return them for the full set of search results.", "tokens": [51376,
  293, 2736, 552, 337, 264, 1577, 992, 295, 3164, 3542, 13, 51500], "temperature":
  0.0, "avg_logprob": -0.15582829814846233, "compression_ratio": 1.8911290322580645,
  "no_speech_prob": 0.00017260682943742722}, {"id": 510, "seek": 173862, "start":
  1762.5, "end": 1765.7399999999998, "text": " So I''m gonna actually just show this
  visually for a second.", "tokens": [51558, 407, 286, 478, 799, 767, 445, 855, 341,
  19622, 337, 257, 1150, 13, 51720], "temperature": 0.0, "avg_logprob": -0.15582829814846233,
  "compression_ratio": 1.8911290322580645, "no_speech_prob": 0.00017260682943742722},
  {"id": 511, "seek": 176574, "start": 1766.74, "end": 1769.14, "text": " Let me put
  them up.", "tokens": [50414, 961, 385, 829, 552, 493, 13, 50534], "temperature":
  0.0, "avg_logprob": -0.35301541678513154, "compression_ratio": 1.5568181818181819,
  "no_speech_prob": 0.002192049054428935}, {"id": 512, "seek": 176574, "start": 1773.6200000000001,
  "end": 1776.6200000000001, "text": " Let me click here and restart this demo.",
  "tokens": [50758, 961, 385, 2052, 510, 293, 21022, 341, 10723, 13, 50908], "temperature":
  0.0, "avg_logprob": -0.35301541678513154, "compression_ratio": 1.5568181818181819,
  "no_speech_prob": 0.002192049054428935}, {"id": 513, "seek": 176574, "start": 1779.38,
  "end": 1782.98, "text": " So imagine I have a sparse vector space over here on the
  left.", "tokens": [51046, 407, 3811, 286, 362, 257, 637, 11668, 8062, 1901, 670,
  510, 322, 264, 1411, 13, 51226], "temperature": 0.0, "avg_logprob": -0.35301541678513154,
  "compression_ratio": 1.5568181818181819, "no_speech_prob": 0.002192049054428935},
  {"id": 514, "seek": 176574, "start": 1783.98, "end": 1786.66, "text": " The way
  this works is I send a query in.", "tokens": [51276, 440, 636, 341, 1985, 307, 286,
  2845, 257, 14581, 294, 13, 51410], "temperature": 0.0, "avg_logprob": -0.35301541678513154,
  "compression_ratio": 1.5568181818181819, "no_speech_prob": 0.002192049054428935},
  {"id": 515, "seek": 176574, "start": 1786.66, "end": 1789.98, "text": " This query
  finds a set of relevant documents", "tokens": [51410, 639, 14581, 10704, 257, 992,
  295, 7340, 8512, 51576], "temperature": 0.0, "avg_logprob": -0.35301541678513154,
  "compression_ratio": 1.5568181818181819, "no_speech_prob": 0.002192049054428935},
  {"id": 516, "seek": 176574, "start": 1789.98, "end": 1792.26, "text": " that are
  in this vector space,", "tokens": [51576, 300, 366, 294, 341, 8062, 1901, 11, 51690],
  "temperature": 0.0, "avg_logprob": -0.35301541678513154, "compression_ratio": 1.5568181818181819,
  "no_speech_prob": 0.002192049054428935}, {"id": 517, "seek": 176574, "start": 1792.26,
  "end": 1793.66, "text": " and what''s found those documents,", "tokens": [51690,
  293, 437, 311, 1352, 729, 8512, 11, 51760], "temperature": 0.0, "avg_logprob": -0.35301541678513154,
  "compression_ratio": 1.5568181818181819, "no_speech_prob": 0.002192049054428935},
  {"id": 518, "seek": 179366, "start": 1793.66, "end": 1797.18, "text": " it uses
  them to essentially a wormhole in the pauses", "tokens": [50364, 309, 4960, 552,
  281, 4476, 257, 23835, 14094, 294, 264, 2502, 8355, 50540], "temperature": 0.0,
  "avg_logprob": -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 519, "seek": 179366, "start": 1797.18, "end": 1798.18,
  "text": " for a second.", "tokens": [50540, 337, 257, 1150, 13, 50590], "temperature":
  0.0, "avg_logprob": -0.19951272518076796, "compression_ratio": 1.7517482517482517,
  "no_speech_prob": 9.638664778321981e-05}, {"id": 520, "seek": 179366, "start": 1798.18,
  "end": 1800.1000000000001, "text": " Oh, maybe I can''t.", "tokens": [50590, 876,
  11, 1310, 286, 393, 380, 13, 50686], "temperature": 0.0, "avg_logprob": -0.19951272518076796,
  "compression_ratio": 1.7517482517482517, "no_speech_prob": 9.638664778321981e-05},
  {"id": 521, "seek": 179366, "start": 1800.1000000000001, "end": 1801.5400000000002,
  "text": " Essentially, once I''ve run that query,", "tokens": [50686, 23596, 11,
  1564, 286, 600, 1190, 300, 14581, 11, 50758], "temperature": 0.0, "avg_logprob":
  -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 522, "seek": 179366, "start": 1801.5400000000002,
  "end": 1803.02, "text": " I find the relevant documents,", "tokens": [50758, 286,
  915, 264, 7340, 8512, 11, 50832], "temperature": 0.0, "avg_logprob": -0.19951272518076796,
  "compression_ratio": 1.7517482517482517, "no_speech_prob": 9.638664778321981e-05},
  {"id": 523, "seek": 179366, "start": 1803.02, "end": 1805.3400000000001, "text":
  " which are the things close by in vector space.", "tokens": [50832, 597, 366, 264,
  721, 1998, 538, 294, 8062, 1901, 13, 50948], "temperature": 0.0, "avg_logprob":
  -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 524, "seek": 179366, "start": 1805.3400000000001,
  "end": 1809.02, "text": " I then use that to generate a vector and embedding", "tokens":
  [50948, 286, 550, 764, 300, 281, 8460, 257, 8062, 293, 12240, 3584, 51132], "temperature":
  0.0, "avg_logprob": -0.19951272518076796, "compression_ratio": 1.7517482517482517,
  "no_speech_prob": 9.638664778321981e-05}, {"id": 525, "seek": 179366, "start": 1809.02,
  "end": 1812.0600000000002, "text": " that I''m gonna run a search for over here
  in the dense space.", "tokens": [51132, 300, 286, 478, 799, 1190, 257, 3164, 337,
  670, 510, 294, 264, 18011, 1901, 13, 51284], "temperature": 0.0, "avg_logprob":
  -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 526, "seek": 179366, "start": 1812.0600000000002,
  "end": 1813.5, "text": " And once I run that search,", "tokens": [51284, 400, 1564,
  286, 1190, 300, 3164, 11, 51356], "temperature": 0.0, "avg_logprob": -0.19951272518076796,
  "compression_ratio": 1.7517482517482517, "no_speech_prob": 9.638664778321981e-05},
  {"id": 527, "seek": 179366, "start": 1813.5, "end": 1815.98, "text": " you''ll notice
  that in this example,", "tokens": [51356, 291, 603, 3449, 300, 294, 341, 1365, 11,
  51480], "temperature": 0.0, "avg_logprob": -0.19951272518076796, "compression_ratio":
  1.7517482517482517, "no_speech_prob": 9.638664778321981e-05}, {"id": 528, "seek":
  179366, "start": 1815.98, "end": 1818.42, "text": " it''s not exactly where these
  documents are,", "tokens": [51480, 309, 311, 406, 2293, 689, 613, 8512, 366, 11,
  51602], "temperature": 0.0, "avg_logprob": -0.19951272518076796, "compression_ratio":
  1.7517482517482517, "no_speech_prob": 9.638664778321981e-05}, {"id": 529, "seek":
  179366, "start": 1818.42, "end": 1819.74, "text": " but it''s very nearby,", "tokens":
  [51602, 457, 309, 311, 588, 11184, 11, 51668], "temperature": 0.0, "avg_logprob":
  -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 530, "seek": 179366, "start": 1819.74, "end": 1822.66,
  "text": " meaning the sort of collection of these things together", "tokens": [51668,
  3620, 264, 1333, 295, 5765, 295, 613, 721, 1214, 51814], "temperature": 0.0, "avg_logprob":
  -0.19951272518076796, "compression_ratio": 1.7517482517482517, "no_speech_prob":
  9.638664778321981e-05}, {"id": 531, "seek": 182266, "start": 1822.66, "end": 1826.26,
  "text": " and what''s understood semantically about the relationship,", "tokens":
  [50364, 293, 437, 311, 7320, 4361, 49505, 466, 264, 2480, 11, 50544], "temperature":
  0.0, "avg_logprob": -0.15157008171081543, "compression_ratio": 1.7628458498023716,
  "no_speech_prob": 5.4762684158049524e-05}, {"id": 532, "seek": 182266, "start":
  1826.26, "end": 1829.18, "text": " maps to this point and vector space on the right.",
  "tokens": [50544, 11317, 281, 341, 935, 293, 8062, 1901, 322, 264, 558, 13, 50690],
  "temperature": 0.0, "avg_logprob": -0.15157008171081543, "compression_ratio": 1.7628458498023716,
  "no_speech_prob": 5.4762684158049524e-05}, {"id": 533, "seek": 182266, "start":
  1829.18, "end": 1833.8600000000001, "text": " And then that allows me to then find
  other things surrounding it", "tokens": [50690, 400, 550, 300, 4045, 385, 281, 550,
  915, 661, 721, 11498, 309, 50924], "temperature": 0.0, "avg_logprob": -0.15157008171081543,
  "compression_ratio": 1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05},
  {"id": 534, "seek": 182266, "start": 1833.8600000000001, "end": 1836.66, "text":
  " that represent a similar meaning.", "tokens": [50924, 300, 2906, 257, 2531, 3620,
  13, 51064], "temperature": 0.0, "avg_logprob": -0.15157008171081543, "compression_ratio":
  1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05}, {"id": 535, "seek":
  182266, "start": 1836.66, "end": 1839.26, "text": " And this is just looking at
  two vector spaces,", "tokens": [51064, 400, 341, 307, 445, 1237, 412, 732, 8062,
  7673, 11, 51194], "temperature": 0.0, "avg_logprob": -0.15157008171081543, "compression_ratio":
  1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05}, {"id": 536, "seek":
  182266, "start": 1839.26, "end": 1841.8600000000001, "text": " a sparse vector space
  and a dense vector space", "tokens": [51194, 257, 637, 11668, 8062, 1901, 293, 257,
  18011, 8062, 1901, 51324], "temperature": 0.0, "avg_logprob": -0.15157008171081543,
  "compression_ratio": 1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05},
  {"id": 537, "seek": 182266, "start": 1841.8600000000001, "end": 1844.02, "text":
  " for keywords and then for embeddings.", "tokens": [51324, 337, 21009, 293, 550,
  337, 12240, 29432, 13, 51432], "temperature": 0.0, "avg_logprob": -0.15157008171081543,
  "compression_ratio": 1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05},
  {"id": 538, "seek": 182266, "start": 1844.02, "end": 1845.8600000000001, "text":
  " But as I mentioned, there''s also this notion", "tokens": [51432, 583, 382, 286,
  2835, 11, 456, 311, 611, 341, 10710, 51524], "temperature": 0.0, "avg_logprob":
  -0.15157008171081543, "compression_ratio": 1.7628458498023716, "no_speech_prob":
  5.4762684158049524e-05}, {"id": 539, "seek": 182266, "start": 1845.8600000000001,
  "end": 1847.5800000000002, "text": " of a behavioral vector space.", "tokens": [51524,
  295, 257, 19124, 8062, 1901, 13, 51610], "temperature": 0.0, "avg_logprob": -0.15157008171081543,
  "compression_ratio": 1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05},
  {"id": 540, "seek": 182266, "start": 1847.5800000000002, "end": 1849.02, "text":
  " So the same thing happens here.", "tokens": [51610, 407, 264, 912, 551, 2314,
  510, 13, 51682], "temperature": 0.0, "avg_logprob": -0.15157008171081543, "compression_ratio":
  1.7628458498023716, "no_speech_prob": 5.4762684158049524e-05}, {"id": 541, "seek":
  184902, "start": 1849.1, "end": 1853.26, "text": " I can run a query, find relevant
  documents,", "tokens": [50368, 286, 393, 1190, 257, 14581, 11, 915, 7340, 8512,
  11, 50576], "temperature": 0.0, "avg_logprob": -0.1160381283380289, "compression_ratio":
  1.7328244274809161, "no_speech_prob": 0.0007076597539708018}, {"id": 542, "seek":
  184902, "start": 1853.26, "end": 1855.54, "text": " use those as my wormhole.",
  "tokens": [50576, 764, 729, 382, 452, 23835, 14094, 13, 50690], "temperature": 0.0,
  "avg_logprob": -0.1160381283380289, "compression_ratio": 1.7328244274809161, "no_speech_prob":
  0.0007076597539708018}, {"id": 543, "seek": 184902, "start": 1855.54, "end": 1857.5,
  "text": " And then I generate this wormhole vector", "tokens": [50690, 400, 550,
  286, 8460, 341, 23835, 14094, 8062, 50788], "temperature": 0.0, "avg_logprob": -0.1160381283380289,
  "compression_ratio": 1.7328244274809161, "no_speech_prob": 0.0007076597539708018},
  {"id": 544, "seek": 184902, "start": 1857.5, "end": 1859.94, "text": " to hop through
  the wormhole to the other side", "tokens": [50788, 281, 3818, 807, 264, 23835, 14094,
  281, 264, 661, 1252, 50910], "temperature": 0.0, "avg_logprob": -0.1160381283380289,
  "compression_ratio": 1.7328244274809161, "no_speech_prob": 0.0007076597539708018},
  {"id": 545, "seek": 184902, "start": 1859.94, "end": 1862.66, "text": " to find
  the region corresponding to that meaning", "tokens": [50910, 281, 915, 264, 4458,
  11760, 281, 300, 3620, 51046], "temperature": 0.0, "avg_logprob": -0.1160381283380289,
  "compression_ratio": 1.7328244274809161, "no_speech_prob": 0.0007076597539708018},
  {"id": 546, "seek": 184902, "start": 1862.66, "end": 1864.9, "text": " in either
  of these other vector spaces.", "tokens": [51046, 294, 2139, 295, 613, 661, 8062,
  7673, 13, 51158], "temperature": 0.0, "avg_logprob": -0.1160381283380289, "compression_ratio":
  1.7328244274809161, "no_speech_prob": 0.0007076597539708018}, {"id": 547, "seek":
  184902, "start": 1864.9, "end": 1868.82, "text": " So in this case, if I''ve done
  major expectation,", "tokens": [51158, 407, 294, 341, 1389, 11, 498, 286, 600, 1096,
  2563, 14334, 11, 51354], "temperature": 0.0, "avg_logprob": -0.1160381283380289,
  "compression_ratio": 1.7328244274809161, "no_speech_prob": 0.0007076597539708018},
  {"id": 548, "seek": 184902, "start": 1868.82, "end": 1870.74, "text": " which is
  like the process you go through", "tokens": [51354, 597, 307, 411, 264, 1399, 291,
  352, 807, 51450], "temperature": 0.0, "avg_logprob": -0.1160381283380289, "compression_ratio":
  1.7328244274809161, "no_speech_prob": 0.0007076597539708018}, {"id": 549, "seek":
  184902, "start": 1870.74, "end": 1873.3799999999999, "text": " when you''re doing
  collaborative filtering for recommendations,", "tokens": [51450, 562, 291, 434,
  884, 16555, 30822, 337, 10434, 11, 51582], "temperature": 0.0, "avg_logprob": -0.1160381283380289,
  "compression_ratio": 1.7328244274809161, "no_speech_prob": 0.0007076597539708018},
  {"id": 550, "seek": 184902, "start": 1873.3799999999999, "end": 1877.34, "text":
  " then I would hop to the corresponding region over here.", "tokens": [51582, 550,
  286, 576, 3818, 281, 264, 11760, 4458, 670, 510, 13, 51780], "temperature": 0.0,
  "avg_logprob": -0.1160381283380289, "compression_ratio": 1.7328244274809161, "no_speech_prob":
  0.0007076597539708018}, {"id": 551, "seek": 187734, "start": 1877.34, "end": 1881.86,
  "text": " So that''s the general idea, just kind of visually describing it.", "tokens":
  [50364, 407, 300, 311, 264, 2674, 1558, 11, 445, 733, 295, 19622, 16141, 309, 13,
  50590], "temperature": 0.2, "avg_logprob": -0.5212716052406713, "compression_ratio":
  1.4437869822485208, "no_speech_prob": 6.683952960884199e-05}, {"id": 552, "seek":
  187734, "start": 1881.86, "end": 1885.5, "text": " And hop like over here.", "tokens":
  [50590, 400, 3818, 411, 670, 510, 13, 50772], "temperature": 0.2, "avg_logprob":
  -0.5212716052406713, "compression_ratio": 1.4437869822485208, "no_speech_prob":
  6.683952960884199e-05}, {"id": 553, "seek": 187734, "start": 1885.5, "end": 1888.34,
  "text": " I can just one second.", "tokens": [50772, 286, 393, 445, 472, 1150, 13,
  50914], "temperature": 0.2, "avg_logprob": -0.5212716052406713, "compression_ratio":
  1.4437869822485208, "no_speech_prob": 6.683952960884199e-05}, {"id": 554, "seek":
  187734, "start": 1888.34, "end": 1890.26, "text": " I can be one second.", "tokens":
  [50914, 286, 393, 312, 472, 1150, 13, 51010], "temperature": 0.2, "avg_logprob":
  -0.5212716052406713, "compression_ratio": 1.4437869822485208, "no_speech_prob":
  6.683952960884199e-05}, {"id": 555, "seek": 187734, "start": 1890.26, "end": 1891.74,
  "text": " Come on, slides up.", "tokens": [51010, 2492, 322, 11, 9788, 493, 13,
  51084], "temperature": 0.2, "avg_logprob": -0.5212716052406713, "compression_ratio":
  1.4437869822485208, "no_speech_prob": 6.683952960884199e-05}, {"id": 556, "seek":
  187734, "start": 1900.54, "end": 1901.06, "text": " All right.", "tokens": [51524,
  1057, 558, 13, 51550], "temperature": 0.2, "avg_logprob": -0.5212716052406713, "compression_ratio":
  1.4437869822485208, "no_speech_prob": 6.683952960884199e-05}, {"id": 557, "seek":
  187734, "start": 1903.98, "end": 1905.22, "text": " And then the next question is,
  how", "tokens": [51696, 400, 550, 264, 958, 1168, 307, 11, 577, 51758], "temperature":
  0.2, "avg_logprob": -0.5212716052406713, "compression_ratio": 1.4437869822485208,
  "no_speech_prob": 6.683952960884199e-05}, {"id": 558, "seek": 187734, "start": 1905.22,
  "end": 1907.3, "text": " do we actually create these wormhole vectors?", "tokens":
  [51758, 360, 321, 767, 1884, 613, 23835, 14094, 18875, 30, 51862], "temperature":
  0.2, "avg_logprob": -0.5212716052406713, "compression_ratio": 1.4437869822485208,
  "no_speech_prob": 6.683952960884199e-05}, {"id": 559, "seek": 190730, "start": 1907.46,
  "end": 1909.22, "text": " So to meet you, if there''s any questions,", "tokens":
  [50372, 407, 281, 1677, 291, 11, 498, 456, 311, 604, 1651, 11, 50460], "temperature":
  0.0, "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391,
  "no_speech_prob": 0.00018061262380797416}, {"id": 560, "seek": 190730, "start":
  1909.22, "end": 1910.46, "text": " feel free to interrupt me at any point.", "tokens":
  [50460, 841, 1737, 281, 12729, 385, 412, 604, 935, 13, 50522], "temperature": 0.0,
  "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391, "no_speech_prob":
  0.00018061262380797416}, {"id": 561, "seek": 190730, "start": 1910.46, "end": 1912.7,
  "text": " But I''ll keep going otherwise.", "tokens": [50522, 583, 286, 603, 1066,
  516, 5911, 13, 50634], "temperature": 0.0, "avg_logprob": -0.23760106922250934,
  "compression_ratio": 1.5751072961373391, "no_speech_prob": 0.00018061262380797416},
  {"id": 562, "seek": 190730, "start": 1912.7, "end": 1914.86, "text": " I think we
  have a couple of questions,", "tokens": [50634, 286, 519, 321, 362, 257, 1916, 295,
  1651, 11, 50742], "temperature": 0.0, "avg_logprob": -0.23760106922250934, "compression_ratio":
  1.5751072961373391, "no_speech_prob": 0.00018061262380797416}, {"id": 563, "seek":
  190730, "start": 1914.86, "end": 1916.78, "text": " but we''ll defer at the end.",
  "tokens": [50742, 457, 321, 603, 25704, 412, 264, 917, 13, 50838], "temperature":
  0.0, "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391,
  "no_speech_prob": 0.00018061262380797416}, {"id": 564, "seek": 190730, "start":
  1916.78, "end": 1917.62, "text": " Sounds good.", "tokens": [50838, 14576, 665,
  13, 50880], "temperature": 0.0, "avg_logprob": -0.23760106922250934, "compression_ratio":
  1.5751072961373391, "no_speech_prob": 0.00018061262380797416}, {"id": 565, "seek":
  190730, "start": 1917.62, "end": 1918.26, "text": " All right.", "tokens": [50880,
  1057, 558, 13, 50912], "temperature": 0.0, "avg_logprob": -0.23760106922250934,
  "compression_ratio": 1.5751072961373391, "no_speech_prob": 0.00018061262380797416},
  {"id": 566, "seek": 190730, "start": 1918.26, "end": 1921.62, "text": " So the question
  now is, how do we create a wormhole vector?", "tokens": [50912, 407, 264, 1168,
  586, 307, 11, 577, 360, 321, 1884, 257, 23835, 14094, 8062, 30, 51080], "temperature":
  0.0, "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391,
  "no_speech_prob": 0.00018061262380797416}, {"id": 567, "seek": 190730, "start":
  1921.62, "end": 1927.3799999999999, "text": " And there''s essentially two types
  that I''m going to focus on right now.", "tokens": [51080, 400, 456, 311, 4476,
  732, 3467, 300, 286, 478, 516, 281, 1879, 322, 558, 586, 13, 51368], "temperature":
  0.0, "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391,
  "no_speech_prob": 0.00018061262380797416}, {"id": 568, "seek": 190730, "start":
  1927.3799999999999, "end": 1933.7, "text": " One is the, sorry, I lost this.", "tokens":
  [51368, 1485, 307, 264, 11, 2597, 11, 286, 2731, 341, 13, 51684], "temperature":
  0.0, "avg_logprob": -0.23760106922250934, "compression_ratio": 1.5751072961373391,
  "no_speech_prob": 0.00018061262380797416}, {"id": 569, "seek": 193370, "start":
  1933.7, "end": 1934.98, "text": " OK.", "tokens": [50364, 2264, 13, 50428], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 570, "seek": 193370, "start": 1934.98,
  "end": 1941.74, "text": " The first is if I''m trying to go to a dense vector space
  within bedding.", "tokens": [50428, 440, 700, 307, 498, 286, 478, 1382, 281, 352,
  281, 257, 18011, 8062, 1901, 1951, 2901, 3584, 13, 50766], "temperature": 0.0, "avg_logprob":
  -0.2036243237947163, "compression_ratio": 1.682608695652174, "no_speech_prob": 0.002920187311246991},
  {"id": 571, "seek": 193370, "start": 1941.74, "end": 1942.66, "text": " So this
  is very easy.", "tokens": [50766, 407, 341, 307, 588, 1858, 13, 50812], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 572, "seek": 193370, "start": 1942.66,
  "end": 1948.22, "text": " All I have to do is pull the vectors or average the vectors
  of the top end documents.", "tokens": [50812, 1057, 286, 362, 281, 360, 307, 2235,
  264, 18875, 420, 4274, 264, 18875, 295, 264, 1192, 917, 8512, 13, 51090], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 573, "seek": 193370, "start": 1948.22,
  "end": 1950.78, "text": " So imagine I run a keyword search.", "tokens": [51090,
  407, 3811, 286, 1190, 257, 20428, 3164, 13, 51218], "temperature": 0.0, "avg_logprob":
  -0.2036243237947163, "compression_ratio": 1.682608695652174, "no_speech_prob": 0.002920187311246991},
  {"id": 574, "seek": 193370, "start": 1950.78, "end": 1952.3, "text": " I find a
  set of documents.", "tokens": [51218, 286, 915, 257, 992, 295, 8512, 13, 51294],
  "temperature": 0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 575, "seek": 193370, "start": 1952.3,
  "end": 1953.8600000000001, "text": " I rank those.", "tokens": [51294, 286, 6181,
  729, 13, 51372], "temperature": 0.0, "avg_logprob": -0.2036243237947163, "compression_ratio":
  1.682608695652174, "no_speech_prob": 0.002920187311246991}, {"id": 576, "seek":
  193370, "start": 1953.8600000000001, "end": 1956.8600000000001, "text": " And then
  I don''t necessarily need to take the entire document set.", "tokens": [51372, 400,
  550, 286, 500, 380, 4725, 643, 281, 747, 264, 2302, 4166, 992, 13, 51522], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 577, "seek": 193370, "start": 1956.8600000000001,
  "end": 1957.78, "text": " I could.", "tokens": [51522, 286, 727, 13, 51568], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 578, "seek": 193370, "start": 1957.78,
  "end": 1959.66, "text": " But if I wanted to just take the top end documents", "tokens":
  [51568, 583, 498, 286, 1415, 281, 445, 747, 264, 1192, 917, 8512, 51662], "temperature":
  0.0, "avg_logprob": -0.2036243237947163, "compression_ratio": 1.682608695652174,
  "no_speech_prob": 0.002920187311246991}, {"id": 579, "seek": 195966, "start": 1959.66,
  "end": 1963.1000000000001, "text": " to get a more sort of semantically relevant,",
  "tokens": [50364, 281, 483, 257, 544, 1333, 295, 4361, 49505, 7340, 11, 50536],
  "temperature": 0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 580, "seek": 195966, "start": 1963.1000000000001,
  "end": 1967.5800000000002, "text": " or just let''s just say relevant set corresponding
  to that keyword query,", "tokens": [50536, 420, 445, 718, 311, 445, 584, 7340, 992,
  11760, 281, 300, 20428, 14581, 11, 50760], "temperature": 0.0, "avg_logprob": -0.15439103395884274,
  "compression_ratio": 1.7346938775510203, "no_speech_prob": 0.0010433149291202426},
  {"id": 581, "seek": 195966, "start": 1967.5800000000002, "end": 1972.14, "text":
  " then I generate a new embedding in the dense space", "tokens": [50760, 550, 286,
  8460, 257, 777, 12240, 3584, 294, 264, 18011, 1901, 50988], "temperature": 0.0,
  "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203, "no_speech_prob":
  0.0010433149291202426}, {"id": 582, "seek": 195966, "start": 1972.14, "end": 1974.6200000000001,
  "text": " that is just an average of those.", "tokens": [50988, 300, 307, 445, 364,
  4274, 295, 729, 13, 51112], "temperature": 0.0, "avg_logprob": -0.15439103395884274,
  "compression_ratio": 1.7346938775510203, "no_speech_prob": 0.0010433149291202426},
  {"id": 583, "seek": 195966, "start": 1974.6200000000001, "end": 1977.1000000000001,
  "text": " If you go back to the Darth Vader example from earlier,", "tokens": [51112,
  759, 291, 352, 646, 281, 264, 40696, 36337, 1365, 490, 3071, 11, 51236], "temperature":
  0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 584, "seek": 195966, "start": 1977.1000000000001,
  "end": 1978.98, "text": " where the puppy Darth Vader is in the middle,", "tokens":
  [51236, 689, 264, 18196, 40696, 36337, 307, 294, 264, 2808, 11, 51330], "temperature":
  0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 585, "seek": 195966, "start": 1978.98,
  "end": 1983.1000000000001, "text": " it was sort of a combination of the meaning
  of Darth Vader and a meaning of puppy.", "tokens": [51330, 309, 390, 1333, 295,
  257, 6562, 295, 264, 3620, 295, 40696, 36337, 293, 257, 3620, 295, 18196, 13, 51536],
  "temperature": 0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 586, "seek": 195966, "start": 1983.1000000000001,
  "end": 1985.1000000000001, "text": " Think of this as taking a bunch of documents",
  "tokens": [51536, 6557, 295, 341, 382, 1940, 257, 3840, 295, 8512, 51636], "temperature":
  0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 587, "seek": 195966, "start": 1985.1000000000001,
  "end": 1986.5400000000002, "text": " that each have their own meaning.", "tokens":
  [51636, 300, 1184, 362, 641, 1065, 3620, 13, 51708], "temperature": 0.0, "avg_logprob":
  -0.15439103395884274, "compression_ratio": 1.7346938775510203, "no_speech_prob":
  0.0010433149291202426}, {"id": 588, "seek": 195966, "start": 1986.5400000000002,
  "end": 1989.5, "text": " And when I pull them together, I''m creating", "tokens":
  [51708, 400, 562, 286, 2235, 552, 1214, 11, 286, 478, 4084, 51856], "temperature":
  0.0, "avg_logprob": -0.15439103395884274, "compression_ratio": 1.7346938775510203,
  "no_speech_prob": 0.0010433149291202426}, {"id": 589, "seek": 198950, "start": 1989.5,
  "end": 1992.34, "text": " an embedding that has the average of the meaning.", "tokens":
  [50364, 364, 12240, 3584, 300, 575, 264, 4274, 295, 264, 3620, 13, 50506], "temperature":
  0.0, "avg_logprob": -0.13117500967230677, "compression_ratio": 1.8130081300813008,
  "no_speech_prob": 8.349609561264515e-05}, {"id": 590, "seek": 198950, "start": 1992.34,
  "end": 1998.34, "text": " And if I assume my documents that I queried on the lexical
  side,", "tokens": [50506, 400, 498, 286, 6552, 452, 8512, 300, 286, 7083, 1091,
  322, 264, 476, 87, 804, 1252, 11, 50806], "temperature": 0.0, "avg_logprob": -0.13117500967230677,
  "compression_ratio": 1.8130081300813008, "no_speech_prob": 8.349609561264515e-05},
  {"id": 591, "seek": 198950, "start": 1998.34, "end": 2001.14, "text": " have some
  sense of a shared meaning within them.", "tokens": [50806, 362, 512, 2020, 295,
  257, 5507, 3620, 1951, 552, 13, 50946], "temperature": 0.0, "avg_logprob": -0.13117500967230677,
  "compression_ratio": 1.8130081300813008, "no_speech_prob": 8.349609561264515e-05},
  {"id": 592, "seek": 198950, "start": 2001.14, "end": 2002.86, "text": " And I take
  the top documents from that,", "tokens": [50946, 400, 286, 747, 264, 1192, 8512,
  490, 300, 11, 51032], "temperature": 0.0, "avg_logprob": -0.13117500967230677, "compression_ratio":
  1.8130081300813008, "no_speech_prob": 8.349609561264515e-05}, {"id": 593, "seek":
  198950, "start": 2002.86, "end": 2005.7, "text": " then that shared meaning I can
  hop over to the dense space,", "tokens": [51032, 550, 300, 5507, 3620, 286, 393,
  3818, 670, 281, 264, 18011, 1901, 11, 51174], "temperature": 0.0, "avg_logprob":
  -0.13117500967230677, "compression_ratio": 1.8130081300813008, "no_speech_prob":
  8.349609561264515e-05}, {"id": 594, "seek": 198950, "start": 2005.7, "end": 2008.58,
  "text": " find and then find other things that have similar meaning,", "tokens":
  [51174, 915, 293, 550, 915, 661, 721, 300, 362, 2531, 3620, 11, 51318], "temperature":
  0.0, "avg_logprob": -0.13117500967230677, "compression_ratio": 1.8130081300813008,
  "no_speech_prob": 8.349609561264515e-05}, {"id": 595, "seek": 198950, "start": 2008.58,
  "end": 2010.98, "text": " even if they don''t match the keywords.", "tokens": [51318,
  754, 498, 436, 500, 380, 2995, 264, 21009, 13, 51438], "temperature": 0.0, "avg_logprob":
  -0.13117500967230677, "compression_ratio": 1.8130081300813008, "no_speech_prob":
  8.349609561264515e-05}, {"id": 596, "seek": 198950, "start": 2010.98, "end": 2014.66,
  "text": " Likewise, I can go the other direction if I''m in my embedding space,",
  "tokens": [51438, 30269, 11, 286, 393, 352, 264, 661, 3513, 498, 286, 478, 294,
  452, 12240, 3584, 1901, 11, 51622], "temperature": 0.0, "avg_logprob": -0.13117500967230677,
  "compression_ratio": 1.8130081300813008, "no_speech_prob": 8.349609561264515e-05},
  {"id": 597, "seek": 198950, "start": 2014.66, "end": 2016.42, "text": " my dense
  space.", "tokens": [51622, 452, 18011, 1901, 13, 51710], "temperature": 0.0, "avg_logprob":
  -0.13117500967230677, "compression_ratio": 1.8130081300813008, "no_speech_prob":
  8.349609561264515e-05}, {"id": 598, "seek": 201642, "start": 2016.42, "end": 2021.94,
  "text": " I can run a search, find the top in most related embeddings", "tokens":
  [50364, 286, 393, 1190, 257, 3164, 11, 915, 264, 1192, 294, 881, 4077, 12240, 29432,
  50640], "temperature": 0.0, "avg_logprob": -0.17304037619328153, "compression_ratio":
  1.6123778501628665, "no_speech_prob": 0.00032095983624458313}, {"id": 599, "seek":
  201642, "start": 2021.94, "end": 2024.46, "text": " by cosine similar to what have
  you.", "tokens": [50640, 538, 23565, 2531, 281, 437, 362, 291, 13, 50766], "temperature":
  0.0, "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665,
  "no_speech_prob": 0.00032095983624458313}, {"id": 600, "seek": 201642, "start":
  2024.46, "end": 2027.54, "text": " And then conceptually, it seems more difficult",
  "tokens": [50766, 400, 550, 3410, 671, 11, 309, 2544, 544, 2252, 50920], "temperature":
  0.0, "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665,
  "no_speech_prob": 0.00032095983624458313}, {"id": 601, "seek": 201642, "start":
  2027.54, "end": 2030.3400000000001, "text": " to then hop over to the sparse space.",
  "tokens": [50920, 281, 550, 3818, 670, 281, 264, 637, 11668, 1901, 13, 51060], "temperature":
  0.0, "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665,
  "no_speech_prob": 0.00032095983624458313}, {"id": 602, "seek": 201642, "start":
  2030.3400000000001, "end": 2032.0600000000002, "text": " How do you generate a sparse
  vector?", "tokens": [51060, 1012, 360, 291, 8460, 257, 637, 11668, 8062, 30, 51146],
  "temperature": 0.0, "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665,
  "no_speech_prob": 0.00032095983624458313}, {"id": 603, "seek": 201642, "start":
  2032.0600000000002, "end": 2034.78, "text": " But there''s a technique called semi-technology
  graphs,", "tokens": [51146, 583, 456, 311, 257, 6532, 1219, 12909, 12, 29113, 1793,
  24877, 11, 51282], "temperature": 0.0, "avg_logprob": -0.17304037619328153, "compression_ratio":
  1.6123778501628665, "no_speech_prob": 0.00032095983624458313}, {"id": 604, "seek":
  201642, "start": 2034.78, "end": 2037.78, "text": " which I''ll kind of walk you
  through, which allows you to do this.", "tokens": [51282, 597, 286, 603, 733, 295,
  1792, 291, 807, 11, 597, 4045, 291, 281, 360, 341, 13, 51432], "temperature": 0.0,
  "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665, "no_speech_prob":
  0.00032095983624458313}, {"id": 605, "seek": 201642, "start": 2037.78, "end": 2041.98,
  "text": " So zooming back out, I mentioned pulling the vectors of the K-NN documents.",
  "tokens": [51432, 407, 48226, 646, 484, 11, 286, 2835, 8407, 264, 18875, 295, 264,
  591, 12, 45, 45, 8512, 13, 51642], "temperature": 0.0, "avg_logprob": -0.17304037619328153,
  "compression_ratio": 1.6123778501628665, "no_speech_prob": 0.00032095983624458313},
  {"id": 606, "seek": 201642, "start": 2041.98, "end": 2044.46, "text": " All you
  need to do, again, I query an electrical space,", "tokens": [51642, 1057, 291, 643,
  281, 360, 11, 797, 11, 286, 14581, 364, 12147, 1901, 11, 51766], "temperature":
  0.0, "avg_logprob": -0.17304037619328153, "compression_ratio": 1.6123778501628665,
  "no_speech_prob": 0.00032095983624458313}, {"id": 607, "seek": 201642, "start":
  2044.46, "end": 2045.9, "text": " get the top K documents,", "tokens": [51766, 483,
  264, 1192, 591, 8512, 11, 51838], "temperature": 0.0, "avg_logprob": -0.17304037619328153,
  "compression_ratio": 1.6123778501628665, "no_speech_prob": 0.00032095983624458313},
  {"id": 608, "seek": 204590, "start": 2045.9, "end": 2048.46, "text": " get the embeddings
  of those documents and average them together.", "tokens": [50364, 483, 264, 12240,
  29432, 295, 729, 8512, 293, 4274, 552, 1214, 13, 50492], "temperature": 0.0, "avg_logprob":
  -0.16094406007781742, "compression_ratio": 1.7570422535211268, "no_speech_prob":
  4.3208525312365964e-05}, {"id": 609, "seek": 204590, "start": 2048.46, "end": 2053.7000000000003,
  "text": " This is the simple way to do that, just using NumPy.", "tokens": [50492,
  639, 307, 264, 2199, 636, 281, 360, 300, 11, 445, 1228, 22592, 47, 88, 13, 50754],
  "temperature": 0.0, "avg_logprob": -0.16094406007781742, "compression_ratio": 1.7570422535211268,
  "no_speech_prob": 4.3208525312365964e-05}, {"id": 610, "seek": 204590, "start":
  2053.7000000000003, "end": 2055.1800000000003, "text": " For the semantics knowledge
  graph approach,", "tokens": [50754, 1171, 264, 4361, 45298, 3601, 4295, 3109, 11,
  50828], "temperature": 0.0, "avg_logprob": -0.16094406007781742, "compression_ratio":
  1.7570422535211268, "no_speech_prob": 4.3208525312365964e-05}, {"id": 611, "seek":
  204590, "start": 2055.1800000000003, "end": 2058.1800000000003, "text": " same thing
  I get the top K documents in the current vector space.", "tokens": [50828, 912,
  551, 286, 483, 264, 1192, 591, 8512, 294, 264, 2190, 8062, 1901, 13, 50978], "temperature":
  0.0, "avg_logprob": -0.16094406007781742, "compression_ratio": 1.7570422535211268,
  "no_speech_prob": 4.3208525312365964e-05}, {"id": 612, "seek": 204590, "start":
  2058.1800000000003, "end": 2061.1, "text": " And then I do a semantics knowledge
  graph traversal", "tokens": [50978, 400, 550, 286, 360, 257, 4361, 45298, 3601,
  4295, 23149, 304, 51124], "temperature": 0.0, "avg_logprob": -0.16094406007781742,
  "compression_ratio": 1.7570422535211268, "no_speech_prob": 4.3208525312365964e-05},
  {"id": 613, "seek": 204590, "start": 2061.1, "end": 2063.94, "text": " to derive
  a sparse lexical query", "tokens": [51124, 281, 28446, 257, 637, 11668, 476, 87,
  804, 14581, 51266], "temperature": 0.0, "avg_logprob": -0.16094406007781742, "compression_ratio":
  1.7570422535211268, "no_speech_prob": 4.3208525312365964e-05}, {"id": 614, "seek":
  204590, "start": 2063.94, "end": 2066.94, "text": " that best represents those documents.",
  "tokens": [51266, 300, 1151, 8855, 729, 8512, 13, 51416], "temperature": 0.0, "avg_logprob":
  -0.16094406007781742, "compression_ratio": 1.7570422535211268, "no_speech_prob":
  4.3208525312365964e-05}, {"id": 615, "seek": 204590, "start": 2066.94, "end": 2069.14,
  "text": " So functionally, if you think of language,", "tokens": [51416, 407, 2445,
  379, 11, 498, 291, 519, 295, 2856, 11, 51526], "temperature": 0.0, "avg_logprob":
  -0.16094406007781742, "compression_ratio": 1.7570422535211268, "no_speech_prob":
  4.3208525312365964e-05}, {"id": 616, "seek": 204590, "start": 2069.14, "end": 2071.14,
  "text": " I just talk about semantics knowledge graphs for a second", "tokens":
  [51526, 286, 445, 751, 466, 4361, 45298, 3601, 24877, 337, 257, 1150, 51626], "temperature":
  0.0, "avg_logprob": -0.16094406007781742, "compression_ratio": 1.7570422535211268,
  "no_speech_prob": 4.3208525312365964e-05}, {"id": 617, "seek": 204590, "start":
  2071.14, "end": 2074.06, "text": " and show you the structure of natural language.",
  "tokens": [51626, 293, 855, 291, 264, 3877, 295, 3303, 2856, 13, 51772], "temperature":
  0.0, "avg_logprob": -0.16094406007781742, "compression_ratio": 1.7570422535211268,
  "no_speech_prob": 4.3208525312365964e-05}, {"id": 618, "seek": 207406, "start":
  2074.06, "end": 2076.54, "text": " You could think of it as a graph of relationships.",
  "tokens": [50364, 509, 727, 519, 295, 309, 382, 257, 4295, 295, 6159, 13, 50488],
  "temperature": 0.0, "avg_logprob": -0.16026883885480356, "compression_ratio": 1.9652509652509653,
  "no_speech_prob": 0.0006026344490237534}, {"id": 619, "seek": 207406, "start": 2076.54,
  "end": 2080.58, "text": " We''ve got prefixes and suffixes and those mapped to terms,",
  "tokens": [50488, 492, 600, 658, 18417, 36005, 293, 3889, 36005, 293, 729, 33318,
  281, 2115, 11, 50690], "temperature": 0.0, "avg_logprob": -0.16026883885480356,
  "compression_ratio": 1.9652509652509653, "no_speech_prob": 0.0006026344490237534},
  {"id": 620, "seek": 207406, "start": 2080.58, "end": 2083.1, "text": " those mapped
  to term sequences and documents.", "tokens": [50690, 729, 33318, 281, 1433, 22978,
  293, 8512, 13, 50816], "temperature": 0.0, "avg_logprob": -0.16026883885480356,
  "compression_ratio": 1.9652509652509653, "no_speech_prob": 0.0006026344490237534},
  {"id": 621, "seek": 207406, "start": 2083.1, "end": 2086.34, "text": " But once
  you get documents and we''ve got these terms across documents,", "tokens": [50816,
  583, 1564, 291, 483, 8512, 293, 321, 600, 658, 613, 2115, 2108, 8512, 11, 50978],
  "temperature": 0.0, "avg_logprob": -0.16026883885480356, "compression_ratio": 1.9652509652509653,
  "no_speech_prob": 0.0006026344490237534}, {"id": 622, "seek": 207406, "start": 2086.34,
  "end": 2089.5, "text": " you can just think of this as a giant graph of relationships.",
  "tokens": [50978, 291, 393, 445, 519, 295, 341, 382, 257, 7410, 4295, 295, 6159,
  13, 51136], "temperature": 0.0, "avg_logprob": -0.16026883885480356, "compression_ratio":
  1.9652509652509653, "no_speech_prob": 0.0006026344490237534}, {"id": 623, "seek":
  207406, "start": 2089.5, "end": 2092.34, "text": " And so I can take individual
  words.", "tokens": [51136, 400, 370, 286, 393, 747, 2609, 2283, 13, 51278], "temperature":
  0.0, "avg_logprob": -0.16026883885480356, "compression_ratio": 1.9652509652509653,
  "no_speech_prob": 0.0006026344490237534}, {"id": 624, "seek": 207406, "start": 2092.34,
  "end": 2096.2599999999998, "text": " In this case, Trey, he, he, they all refer
  to the same entity.", "tokens": [51278, 682, 341, 1389, 11, 314, 7950, 11, 415,
  11, 415, 11, 436, 439, 2864, 281, 264, 912, 13977, 13, 51474], "temperature": 0.0,
  "avg_logprob": -0.16026883885480356, "compression_ratio": 1.9652509652509653, "no_speech_prob":
  0.0006026344490237534}, {"id": 625, "seek": 207406, "start": 2096.2599999999998,
  "end": 2097.38, "text": " I can take other things.", "tokens": [51474, 286, 393,
  747, 661, 721, 13, 51530], "temperature": 0.0, "avg_logprob": -0.16026883885480356,
  "compression_ratio": 1.9652509652509653, "no_speech_prob": 0.0006026344490237534},
  {"id": 626, "seek": 207406, "start": 2097.38, "end": 2101.38, "text": " And if I
  think of this as a graph, then in fact,", "tokens": [51530, 400, 498, 286, 519,
  295, 341, 382, 257, 4295, 11, 550, 294, 1186, 11, 51730], "temperature": 0.0, "avg_logprob":
  -0.16026883885480356, "compression_ratio": 1.9652509652509653, "no_speech_prob":
  0.0006026344490237534}, {"id": 627, "seek": 207406, "start": 2101.38, "end": 2103.9,
  "text": " you can leverage your inverted index as a graph", "tokens": [51730, 291,
  393, 13982, 428, 38969, 8186, 382, 257, 4295, 51856], "temperature": 0.0, "avg_logprob":
  -0.16026883885480356, "compression_ratio": 1.9652509652509653, "no_speech_prob":
  0.0006026344490237534}, {"id": 628, "seek": 210390, "start": 2103.9, "end": 2106.98,
  "text": " and you can traverse it to find these relationships.", "tokens": [50364,
  293, 291, 393, 45674, 309, 281, 915, 613, 6159, 13, 50518], "temperature": 0.0,
  "avg_logprob": -0.18201105613408125, "compression_ratio": 1.7575757575757576, "no_speech_prob":
  4.3960564653389156e-05}, {"id": 629, "seek": 210390, "start": 2106.98, "end": 2108.94,
  "text": " And so, and a typical search engine.", "tokens": [50518, 400, 370, 11,
  293, 257, 7476, 3164, 2848, 13, 50616], "temperature": 0.0, "avg_logprob": -0.18201105613408125,
  "compression_ratio": 1.7575757575757576, "no_speech_prob": 4.3960564653389156e-05},
  {"id": 630, "seek": 210390, "start": 2108.94, "end": 2111.62, "text": " So like
  any of the Lucy and engines, for example,", "tokens": [50616, 407, 411, 604, 295,
  264, 22698, 293, 12982, 11, 337, 1365, 11, 50750], "temperature": 0.0, "avg_logprob":
  -0.18201105613408125, "compression_ratio": 1.7575757575757576, "no_speech_prob":
  4.3960564653389156e-05}, {"id": 631, "seek": 210390, "start": 2111.62, "end": 2114.34,
  "text": " you have an inverted index,", "tokens": [50750, 291, 362, 364, 38969,
  8186, 11, 50886], "temperature": 0.0, "avg_logprob": -0.18201105613408125, "compression_ratio":
  1.7575757575757576, "no_speech_prob": 4.3960564653389156e-05}, {"id": 632, "seek":
  210390, "start": 2114.34, "end": 2117.54, "text": " which is something that maps
  terms to sets of documents.", "tokens": [50886, 597, 307, 746, 300, 11317, 2115,
  281, 6352, 295, 8512, 13, 51046], "temperature": 0.0, "avg_logprob": -0.18201105613408125,
  "compression_ratio": 1.7575757575757576, "no_speech_prob": 4.3960564653389156e-05},
  {"id": 633, "seek": 210390, "start": 2117.54, "end": 2119.86, "text": " And then
  you''ve got usually a forward index", "tokens": [51046, 400, 550, 291, 600, 658,
  2673, 257, 2128, 8186, 51162], "temperature": 0.0, "avg_logprob": -0.18201105613408125,
  "compression_ratio": 1.7575757575757576, "no_speech_prob": 4.3960564653389156e-05},
  {"id": 634, "seek": 210390, "start": 2119.86, "end": 2124.86, "text": " and open
  search, elastic search, solar, any Lucy and engine.", "tokens": [51162, 293, 1269,
  3164, 11, 17115, 3164, 11, 7936, 11, 604, 22698, 293, 2848, 13, 51412], "temperature":
  0.0, "avg_logprob": -0.18201105613408125, "compression_ratio": 1.7575757575757576,
  "no_speech_prob": 4.3960564653389156e-05}, {"id": 635, "seek": 210390, "start":
  2124.86, "end": 2127.2200000000003, "text": " This is going to be your doc values.",
  "tokens": [51412, 639, 307, 516, 281, 312, 428, 3211, 4190, 13, 51530], "temperature":
  0.0, "avg_logprob": -0.18201105613408125, "compression_ratio": 1.7575757575757576,
  "no_speech_prob": 4.3960564653389156e-05}, {"id": 636, "seek": 210390, "start":
  2127.2200000000003, "end": 2130.34, "text": " But essentially, I can take any term
  and map it to a set of documents.", "tokens": [51530, 583, 4476, 11, 286, 393, 747,
  604, 1433, 293, 4471, 309, 281, 257, 992, 295, 8512, 13, 51686], "temperature":
  0.0, "avg_logprob": -0.18201105613408125, "compression_ratio": 1.7575757575757576,
  "no_speech_prob": 4.3960564653389156e-05}, {"id": 637, "seek": 210390, "start":
  2130.34, "end": 2132.46, "text": " So if I can take any term,", "tokens": [51686,
  407, 498, 286, 393, 747, 604, 1433, 11, 51792], "temperature": 0.0, "avg_logprob":
  -0.18201105613408125, "compression_ratio": 1.7575757575757576, "no_speech_prob":
  4.3960564653389156e-05}, {"id": 638, "seek": 213246, "start": 2132.46, "end": 2134.7400000000002,
  "text": " I''m sorry, any document map it to a set of terms.", "tokens": [50364,
  286, 478, 2597, 11, 604, 4166, 4471, 309, 281, 257, 992, 295, 2115, 13, 50478],
  "temperature": 0.0, "avg_logprob": -0.14726111725086474, "compression_ratio": 2.017167381974249,
  "no_speech_prob": 0.00017674015543889254}, {"id": 639, "seek": 213246, "start":
  2134.7400000000002, "end": 2138.2200000000003, "text": " So if I can take any term
  and map it to a document set,", "tokens": [50478, 407, 498, 286, 393, 747, 604,
  1433, 293, 4471, 309, 281, 257, 4166, 992, 11, 50652], "temperature": 0.0, "avg_logprob":
  -0.14726111725086474, "compression_ratio": 2.017167381974249, "no_speech_prob":
  0.00017674015543889254}, {"id": 640, "seek": 213246, "start": 2138.2200000000003,
  "end": 2141.38, "text": " and I can take any document and map it to a set of terms,",
  "tokens": [50652, 293, 286, 393, 747, 604, 4166, 293, 4471, 309, 281, 257, 992,
  295, 2115, 11, 50810], "temperature": 0.0, "avg_logprob": -0.14726111725086474,
  "compression_ratio": 2.017167381974249, "no_speech_prob": 0.00017674015543889254},
  {"id": 641, "seek": 213246, "start": 2141.38, "end": 2144.38, "text": " then that''s
  a graph and I can traverse back and forth across this.", "tokens": [50810, 550,
  300, 311, 257, 4295, 293, 286, 393, 45674, 646, 293, 5220, 2108, 341, 13, 50960],
  "temperature": 0.0, "avg_logprob": -0.14726111725086474, "compression_ratio": 2.017167381974249,
  "no_speech_prob": 0.00017674015543889254}, {"id": 642, "seek": 213246, "start":
  2144.38, "end": 2150.66, "text": " So for example, if I have the skill of Java and
  the skill field,", "tokens": [50960, 407, 337, 1365, 11, 498, 286, 362, 264, 5389,
  295, 10745, 293, 264, 5389, 2519, 11, 51274], "temperature": 0.0, "avg_logprob":
  -0.14726111725086474, "compression_ratio": 2.017167381974249, "no_speech_prob":
  0.00017674015543889254}, {"id": 643, "seek": 213246, "start": 2150.66, "end": 2154.1,
  "text": " and I''ve got a set of documents that has the keyword Java,", "tokens":
  [51274, 293, 286, 600, 658, 257, 992, 295, 8512, 300, 575, 264, 20428, 10745, 11,
  51446], "temperature": 0.0, "avg_logprob": -0.14726111725086474, "compression_ratio":
  2.017167381974249, "no_speech_prob": 0.00017674015543889254}, {"id": 644, "seek":
  213246, "start": 2154.1, "end": 2159.7400000000002, "text": " you can think of this
  set of documents as representing the keyword Java.", "tokens": [51446, 291, 393,
  519, 295, 341, 992, 295, 8512, 382, 13460, 264, 20428, 10745, 13, 51728], "temperature":
  0.0, "avg_logprob": -0.14726111725086474, "compression_ratio": 2.017167381974249,
  "no_speech_prob": 0.00017674015543889254}, {"id": 645, "seek": 213246, "start":
  2159.7400000000002, "end": 2161.98, "text": " And then similarly, there''s sort
  of a link", "tokens": [51728, 400, 550, 14138, 11, 456, 311, 1333, 295, 257, 2113,
  51840], "temperature": 0.0, "avg_logprob": -0.14726111725086474, "compression_ratio":
  2.017167381974249, "no_speech_prob": 0.00017674015543889254}, {"id": 646, "seek":
  216198, "start": 2161.98, "end": 2162.82, "text": " to other documents.", "tokens":
  [50364, 281, 661, 8512, 13, 50406], "temperature": 0.0, "avg_logprob": -0.16245371765560573,
  "compression_ratio": 1.9816176470588236, "no_speech_prob": 0.0005235624266788363},
  {"id": 647, "seek": 216198, "start": 2162.82, "end": 2165.18, "text": " You''ll
  notice that there''s no documents that link", "tokens": [50406, 509, 603, 3449,
  300, 456, 311, 572, 8512, 300, 2113, 50524], "temperature": 0.0, "avg_logprob":
  -0.16245371765560573, "compression_ratio": 1.9816176470588236, "no_speech_prob":
  0.0005235624266788363}, {"id": 648, "seek": 216198, "start": 2165.18, "end": 2168.14,
  "text": " both the skill of Java and the skill of hibernate.", "tokens": [50524,
  1293, 264, 5389, 295, 10745, 293, 264, 5389, 295, 4879, 26848, 473, 13, 50672],
  "temperature": 0.0, "avg_logprob": -0.16245371765560573, "compression_ratio": 1.9816176470588236,
  "no_speech_prob": 0.0005235624266788363}, {"id": 649, "seek": 216198, "start": 2168.14,
  "end": 2170.14, "text": " And so in a set theory view, it looks like this.", "tokens":
  [50672, 400, 370, 294, 257, 992, 5261, 1910, 11, 309, 1542, 411, 341, 13, 50772],
  "temperature": 0.0, "avg_logprob": -0.16245371765560573, "compression_ratio": 1.9816176470588236,
  "no_speech_prob": 0.0005235624266788363}, {"id": 650, "seek": 216198, "start": 2170.14,
  "end": 2172.7400000000002, "text": " Notice that this set doesn''t intersect with
  these.", "tokens": [50772, 13428, 300, 341, 992, 1177, 380, 27815, 365, 613, 13,
  50902], "temperature": 0.0, "avg_logprob": -0.16245371765560573, "compression_ratio":
  1.9816176470588236, "no_speech_prob": 0.0005235624266788363}, {"id": 651, "seek":
  216198, "start": 2172.7400000000002, "end": 2176.14, "text": " And from a graph
  theory view, the same underlying indexes", "tokens": [50902, 400, 490, 257, 4295,
  5261, 1910, 11, 264, 912, 14217, 8186, 279, 51072], "temperature": 0.0, "avg_logprob":
  -0.16245371765560573, "compression_ratio": 1.9816176470588236, "no_speech_prob":
  0.0005235624266788363}, {"id": 652, "seek": 216198, "start": 2176.14, "end": 2179.86,
  "text": " look like this where I have a graph where I''ve got the skill of Java",
  "tokens": [51072, 574, 411, 341, 689, 286, 362, 257, 4295, 689, 286, 600, 658, 264,
  5389, 295, 10745, 51258], "temperature": 0.0, "avg_logprob": -0.16245371765560573,
  "compression_ratio": 1.9816176470588236, "no_speech_prob": 0.0005235624266788363},
  {"id": 653, "seek": 216198, "start": 2179.86, "end": 2182.7400000000002, "text":
  " with a has related skill edge to the skill of Scala", "tokens": [51258, 365, 257,
  575, 4077, 5389, 4691, 281, 264, 5389, 295, 2747, 5159, 51402], "temperature": 0.0,
  "avg_logprob": -0.16245371765560573, "compression_ratio": 1.9816176470588236, "no_speech_prob":
  0.0005235624266788363}, {"id": 654, "seek": 216198, "start": 2182.7400000000002,
  "end": 2184.02, "text": " and the skill of hibernate.", "tokens": [51402, 293, 264,
  5389, 295, 4879, 26848, 473, 13, 51466], "temperature": 0.0, "avg_logprob": -0.16245371765560573,
  "compression_ratio": 1.9816176470588236, "no_speech_prob": 0.0005235624266788363},
  {"id": 655, "seek": 216198, "start": 2184.02, "end": 2187.06, "text": " And then
  oncology is completely disconnected from the graph.", "tokens": [51466, 400, 550,
  40592, 1793, 307, 2584, 29426, 490, 264, 4295, 13, 51618], "temperature": 0.0, "avg_logprob":
  -0.16245371765560573, "compression_ratio": 1.9816176470588236, "no_speech_prob":
  0.0005235624266788363}, {"id": 656, "seek": 216198, "start": 2187.06, "end": 2189.86,
  "text": " And all I''m doing is leveraging my inverted index,", "tokens": [51618,
  400, 439, 286, 478, 884, 307, 32666, 452, 38969, 8186, 11, 51758], "temperature":
  0.0, "avg_logprob": -0.16245371765560573, "compression_ratio": 1.9816176470588236,
  "no_speech_prob": 0.0005235624266788363}, {"id": 657, "seek": 218986, "start": 2189.86,
  "end": 2196.3, "text": " my sparse representation to traverse across these relationships.",
  "tokens": [50364, 452, 637, 11668, 10290, 281, 45674, 2108, 613, 6159, 13, 50686],
  "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio": 1.8244897959183672,
  "no_speech_prob": 0.001203685300424695}, {"id": 658, "seek": 218986, "start": 2196.3,
  "end": 2199.02, "text": " This is very useful for things like disambiguation,",
  "tokens": [50686, 639, 307, 588, 4420, 337, 721, 411, 717, 2173, 328, 16073, 11,
  50822], "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio":
  1.8244897959183672, "no_speech_prob": 0.001203685300424695}, {"id": 659, "seek":
  218986, "start": 2199.02, "end": 2200.98, "text": " where I can take a keyword like
  server.", "tokens": [50822, 689, 286, 393, 747, 257, 20428, 411, 7154, 13, 50920],
  "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio": 1.8244897959183672,
  "no_speech_prob": 0.001203685300424695}, {"id": 660, "seek": 218986, "start": 2200.98,
  "end": 2203.58, "text": " I can traverse through documents to find", "tokens": [50920,
  286, 393, 45674, 807, 8512, 281, 915, 51050], "temperature": 0.0, "avg_logprob":
  -0.157505534519659, "compression_ratio": 1.8244897959183672, "no_speech_prob": 0.001203685300424695},
  {"id": 661, "seek": 218986, "start": 2203.58, "end": 2206.2200000000003, "text":
  " what are the top semantically related categories,", "tokens": [51050, 437, 366,
  264, 1192, 4361, 49505, 4077, 10479, 11, 51182], "temperature": 0.0, "avg_logprob":
  -0.157505534519659, "compression_ratio": 1.8244897959183672, "no_speech_prob": 0.001203685300424695},
  {"id": 662, "seek": 218986, "start": 2206.2200000000003, "end": 2207.98, "text":
  " for example, DevOps and Travel.", "tokens": [51182, 337, 1365, 11, 43051, 293,
  20610, 13, 51270], "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio":
  1.8244897959183672, "no_speech_prob": 0.001203685300424695}, {"id": 663, "seek":
  218986, "start": 2207.98, "end": 2209.6600000000003, "text": " And then within each
  of those categories,", "tokens": [51270, 400, 550, 1951, 1184, 295, 729, 10479,
  11, 51354], "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio":
  1.8244897959183672, "no_speech_prob": 0.001203685300424695}, {"id": 664, "seek":
  218986, "start": 2209.6600000000003, "end": 2211.94, "text": " I can traverse to
  other keywords and find", "tokens": [51354, 286, 393, 45674, 281, 661, 21009, 293,
  915, 51468], "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio":
  1.8244897959183672, "no_speech_prob": 0.001203685300424695}, {"id": 665, "seek":
  218986, "start": 2211.94, "end": 2214.1400000000003, "text": " which are the most
  semantically related keywords", "tokens": [51468, 597, 366, 264, 881, 4361, 49505,
  4077, 21009, 51578], "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio":
  1.8244897959183672, "no_speech_prob": 0.001203685300424695}, {"id": 666, "seek":
  218986, "start": 2214.1400000000003, "end": 2216.3, "text": " to server and the
  DevOps category.", "tokens": [51578, 281, 7154, 293, 264, 43051, 7719, 13, 51686],
  "temperature": 0.0, "avg_logprob": -0.157505534519659, "compression_ratio": 1.8244897959183672,
  "no_speech_prob": 0.001203685300424695}, {"id": 667, "seek": 221630, "start": 2216.3,
  "end": 2218.82, "text": " For example, I get terms like Docker,", "tokens": [50364,
  1171, 1365, 11, 286, 483, 2115, 411, 33772, 11, 50490], "temperature": 0.0, "avg_logprob":
  -0.1971553455699574, "compression_ratio": 1.5691056910569106, "no_speech_prob":
  0.000775289663579315}, {"id": 668, "seek": 221630, "start": 2218.82, "end": 2221.82,
  "text": " Ingenx, Jenkins, Git, Words and Travel,", "tokens": [50490, 682, 1766,
  87, 11, 41273, 11, 16939, 11, 32857, 293, 20610, 11, 50640], "temperature": 0.0,
  "avg_logprob": -0.1971553455699574, "compression_ratio": 1.5691056910569106, "no_speech_prob":
  0.000775289663579315}, {"id": 669, "seek": 221630, "start": 2221.82, "end": 2224.2200000000003,
  "text": " I get things like tip, restaurant,", "tokens": [50640, 286, 483, 721,
  411, 4125, 11, 6383, 11, 50760], "temperature": 0.0, "avg_logprob": -0.1971553455699574,
  "compression_ratio": 1.5691056910569106, "no_speech_prob": 0.000775289663579315},
  {"id": 670, "seek": 221630, "start": 2224.2200000000003, "end": 2226.5800000000004,
  "text": " bill, wages, things like that.", "tokens": [50760, 2961, 11, 20097, 11,
  721, 411, 300, 13, 50878], "temperature": 0.0, "avg_logprob": -0.1971553455699574,
  "compression_ratio": 1.5691056910569106, "no_speech_prob": 0.000775289663579315},
  {"id": 671, "seek": 221630, "start": 2226.5800000000004, "end": 2229.9, "text":
  " And so all of this just leverages an inverted index.", "tokens": [50878, 400,
  370, 439, 295, 341, 445, 12451, 1660, 364, 38969, 8186, 13, 51044], "temperature":
  0.0, "avg_logprob": -0.1971553455699574, "compression_ratio": 1.5691056910569106,
  "no_speech_prob": 0.000775289663579315}, {"id": 672, "seek": 221630, "start": 2229.9,
  "end": 2232.78, "text": " There''s no embeddings whatsoever.", "tokens": [51044,
  821, 311, 572, 12240, 29432, 17076, 13, 51188], "temperature": 0.0, "avg_logprob":
  -0.1971553455699574, "compression_ratio": 1.5691056910569106, "no_speech_prob":
  0.000775289663579315}, {"id": 673, "seek": 221630, "start": 2232.78, "end": 2237.9,
  "text": " This is all just leveraging the sparse semantic space.", "tokens": [51188,
  639, 307, 439, 445, 32666, 264, 637, 11668, 47982, 1901, 13, 51444], "temperature":
  0.0, "avg_logprob": -0.1971553455699574, "compression_ratio": 1.5691056910569106,
  "no_speech_prob": 0.000775289663579315}, {"id": 674, "seek": 221630, "start": 2237.9,
  "end": 2240.26, "text": " But why this matters for modeling a tent", "tokens": [51444,
  583, 983, 341, 7001, 337, 15983, 257, 7054, 51562], "temperature": 0.0, "avg_logprob":
  -0.1971553455699574, "compression_ratio": 1.5691056910569106, "no_speech_prob":
  0.000775289663579315}, {"id": 675, "seek": 221630, "start": 2240.26, "end": 2244.6200000000003,
  "text": " is if I have a query like barbecue near haystack over here,", "tokens":
  [51562, 307, 498, 286, 362, 257, 14581, 411, 21877, 2651, 4842, 372, 501, 670, 510,
  11, 51780], "temperature": 0.0, "avg_logprob": -0.1971553455699574, "compression_ratio":
  1.5691056910569106, "no_speech_prob": 0.000775289663579315}, {"id": 676, "seek":
  224462, "start": 2245.58, "end": 2250.1, "text": " I can generate a sparse vector
  representing the meaning", "tokens": [50412, 286, 393, 8460, 257, 637, 11668, 8062,
  13460, 264, 3620, 50638], "temperature": 0.0, "avg_logprob": -0.154041166305542,
  "compression_ratio": 1.7110091743119267, "no_speech_prob": 0.0029200271237641573},
  {"id": 677, "seek": 224462, "start": 2250.1, "end": 2252.9, "text": " of barbecue
  by looking at the index", "tokens": [50638, 295, 21877, 538, 1237, 412, 264, 8186,
  50778], "temperature": 0.0, "avg_logprob": -0.154041166305542, "compression_ratio":
  1.7110091743119267, "no_speech_prob": 0.0029200271237641573}, {"id": 678, "seek":
  224462, "start": 2252.9, "end": 2254.02, "text": " and seeing what''s related to
  it.", "tokens": [50778, 293, 2577, 437, 311, 4077, 281, 309, 13, 50834], "temperature":
  0.0, "avg_logprob": -0.154041166305542, "compression_ratio": 1.7110091743119267,
  "no_speech_prob": 0.0029200271237641573}, {"id": 679, "seek": 224462, "start": 2254.02,
  "end": 2256.7, "text": " So in this context, what I''m able to find", "tokens":
  [50834, 407, 294, 341, 4319, 11, 437, 286, 478, 1075, 281, 915, 50968], "temperature":
  0.0, "avg_logprob": -0.154041166305542, "compression_ratio": 1.7110091743119267,
  "no_speech_prob": 0.0029200271237641573}, {"id": 680, "seek": 224462, "start": 2256.7,
  "end": 2260.2999999999997, "text": " is that barbecue is related to things like
  ribs", "tokens": [50968, 307, 300, 21877, 307, 4077, 281, 721, 411, 21400, 51148],
  "temperature": 0.0, "avg_logprob": -0.154041166305542, "compression_ratio": 1.7110091743119267,
  "no_speech_prob": 0.0029200271237641573}, {"id": 681, "seek": 224462, "start": 2260.2999999999997,
  "end": 2264.14, "text": " and brisket and pork and the category of restaurant.",
  "tokens": [51148, 293, 738, 271, 5758, 293, 10208, 293, 264, 7719, 295, 6383, 13,
  51340], "temperature": 0.0, "avg_logprob": -0.154041166305542, "compression_ratio":
  1.7110091743119267, "no_speech_prob": 0.0029200271237641573}, {"id": 682, "seek":
  224462, "start": 2264.14, "end": 2269.14, "text": " IE, I can generate a sparse
  lexical vector like this,", "tokens": [51340, 286, 36, 11, 286, 393, 8460, 257,
  637, 11668, 476, 87, 804, 8062, 411, 341, 11, 51590], "temperature": 0.0, "avg_logprob":
  -0.154041166305542, "compression_ratio": 1.7110091743119267, "no_speech_prob": 0.0029200271237641573},
  {"id": 683, "seek": 224462, "start": 2269.66, "end": 2273.8199999999997, "text":
  " purely from the things that are semantically nearby", "tokens": [51616, 17491,
  490, 264, 721, 300, 366, 4361, 49505, 11184, 51824], "temperature": 0.0, "avg_logprob":
  -0.154041166305542, "compression_ratio": 1.7110091743119267, "no_speech_prob": 0.0029200271237641573},
  {"id": 684, "seek": 227382, "start": 2273.82, "end": 2276.86, "text": " in my sparse
  vector space to barbecue.", "tokens": [50364, 294, 452, 637, 11668, 8062, 1901,
  281, 21877, 13, 50516], "temperature": 0.0, "avg_logprob": -0.11250356038411459,
  "compression_ratio": 1.7067669172932332, "no_speech_prob": 0.00020677690918091685},
  {"id": 685, "seek": 227382, "start": 2276.86, "end": 2279.1800000000003, "text":
  " But also, if you look at the query over on the right,", "tokens": [50516, 583,
  611, 11, 498, 291, 574, 412, 264, 14581, 670, 322, 264, 558, 11, 50632], "temperature":
  0.0, "avg_logprob": -0.11250356038411459, "compression_ratio": 1.7067669172932332,
  "no_speech_prob": 0.00020677690918091685}, {"id": 686, "seek": 227382, "start":
  2279.1800000000003, "end": 2281.7000000000003, "text": " barbecue grill, what I''m
  able to do", "tokens": [50632, 21877, 16492, 11, 437, 286, 478, 1075, 281, 360,
  50758], "temperature": 0.0, "avg_logprob": -0.11250356038411459, "compression_ratio":
  1.7067669172932332, "no_speech_prob": 0.00020677690918091685}, {"id": 687, "seek":
  227382, "start": 2281.7000000000003, "end": 2286.26, "text": " is generate a sparse
  vector that is barbecue or grill", "tokens": [50758, 307, 8460, 257, 637, 11668,
  8062, 300, 307, 21877, 420, 16492, 50986], "temperature": 0.0, "avg_logprob": -0.11250356038411459,
  "compression_ratio": 1.7067669172932332, "no_speech_prob": 0.00020677690918091685},
  {"id": 688, "seek": 227382, "start": 2286.26, "end": 2288.2200000000003, "text":
  " or propane or charcoal.", "tokens": [50986, 420, 2365, 1929, 420, 30625, 13, 51084],
  "temperature": 0.0, "avg_logprob": -0.11250356038411459, "compression_ratio": 1.7067669172932332,
  "no_speech_prob": 0.00020677690918091685}, {"id": 689, "seek": 227382, "start":
  2288.2200000000003, "end": 2290.3, "text": " Notice that this vector is now different",
  "tokens": [51084, 13428, 300, 341, 8062, 307, 586, 819, 51188], "temperature": 0.0,
  "avg_logprob": -0.11250356038411459, "compression_ratio": 1.7067669172932332, "no_speech_prob":
  0.00020677690918091685}, {"id": 690, "seek": 227382, "start": 2290.3, "end": 2293.2200000000003,
  "text": " because it''s contextualized based upon grill being", "tokens": [51188,
  570, 309, 311, 35526, 1602, 2361, 3564, 16492, 885, 51334], "temperature": 0.0,
  "avg_logprob": -0.11250356038411459, "compression_ratio": 1.7067669172932332, "no_speech_prob":
  0.00020677690918091685}, {"id": 691, "seek": 227382, "start": 2293.2200000000003,
  "end": 2294.06, "text": " in this query.", "tokens": [51334, 294, 341, 14581, 13,
  51376], "temperature": 0.0, "avg_logprob": -0.11250356038411459, "compression_ratio":
  1.7067669172932332, "no_speech_prob": 0.00020677690918091685}, {"id": 692, "seek":
  227382, "start": 2294.06, "end": 2297.94, "text": " So now my query becomes a category
  about to our appliance", "tokens": [51376, 407, 586, 452, 14581, 3643, 257, 7719,
  466, 281, 527, 45646, 51570], "temperature": 0.0, "avg_logprob": -0.11250356038411459,
  "compression_ratio": 1.7067669172932332, "no_speech_prob": 0.00020677690918091685},
  {"id": 693, "seek": 227382, "start": 2297.94, "end": 2299.38, "text": " and then
  this is the list of words", "tokens": [51570, 293, 550, 341, 307, 264, 1329, 295,
  2283, 51642], "temperature": 0.0, "avg_logprob": -0.11250356038411459, "compression_ratio":
  1.7067669172932332, "no_speech_prob": 0.00020677690918091685}, {"id": 694, "seek":
  227382, "start": 2299.38, "end": 2301.9, "text": " that better represents the meaning
  of barbecue.", "tokens": [51642, 300, 1101, 8855, 264, 3620, 295, 21877, 13, 51768],
  "temperature": 0.0, "avg_logprob": -0.11250356038411459, "compression_ratio": 1.7067669172932332,
  "no_speech_prob": 0.00020677690918091685}, {"id": 695, "seek": 230190, "start":
  2301.9, "end": 2305.3, "text": " Again, no embeddings, no transformer models,",
  "tokens": [50364, 3764, 11, 572, 12240, 29432, 11, 572, 31782, 5245, 11, 50534],
  "temperature": 0.0, "avg_logprob": -0.16834406088326723, "compression_ratio": 1.658273381294964,
  "no_speech_prob": 0.00031480571487918496}, {"id": 696, "seek": 230190, "start":
  2305.3, "end": 2306.54, "text": " no LLMs involved here.", "tokens": [50534, 572,
  441, 43, 26386, 3288, 510, 13, 50596], "temperature": 0.0, "avg_logprob": -0.16834406088326723,
  "compression_ratio": 1.658273381294964, "no_speech_prob": 0.00031480571487918496},
  {"id": 697, "seek": 230190, "start": 2306.54, "end": 2309.46, "text": " This is
  purely leveraging my sparse lexical space", "tokens": [50596, 639, 307, 17491, 32666,
  452, 637, 11668, 476, 87, 804, 1901, 50742], "temperature": 0.0, "avg_logprob":
  -0.16834406088326723, "compression_ratio": 1.658273381294964, "no_speech_prob":
  0.00031480571487918496}, {"id": 698, "seek": 230190, "start": 2309.46, "end": 2311.46,
  "text": " in the semantics within it.", "tokens": [50742, 294, 264, 4361, 45298,
  1951, 309, 13, 50842], "temperature": 0.0, "avg_logprob": -0.16834406088326723,
  "compression_ratio": 1.658273381294964, "no_speech_prob": 0.00031480571487918496},
  {"id": 699, "seek": 230190, "start": 2311.46, "end": 2313.7000000000003, "text":
  " And so this is some example source code", "tokens": [50842, 400, 370, 341, 307,
  512, 1365, 4009, 3089, 50954], "temperature": 0.0, "avg_logprob": -0.16834406088326723,
  "compression_ratio": 1.658273381294964, "no_speech_prob": 0.00031480571487918496},
  {"id": 700, "seek": 230190, "start": 2313.7000000000003, "end": 2314.94, "text":
  " from the AI Power Search book", "tokens": [50954, 490, 264, 7318, 7086, 17180,
  1446, 51016], "temperature": 0.0, "avg_logprob": -0.16834406088326723, "compression_ratio":
  1.658273381294964, "no_speech_prob": 0.00031480571487918496}, {"id": 701, "seek":
  230190, "start": 2314.94, "end": 2317.98, "text": " for traversing semantic knowledge
  graphs.", "tokens": [51016, 337, 23149, 278, 47982, 3601, 24877, 13, 51168], "temperature":
  0.0, "avg_logprob": -0.16834406088326723, "compression_ratio": 1.658273381294964,
  "no_speech_prob": 0.00031480571487918496}, {"id": 702, "seek": 230190, "start":
  2317.98, "end": 2321.3, "text": " But the idea here with the wormhole vectors",
  "tokens": [51168, 583, 264, 1558, 510, 365, 264, 23835, 14094, 18875, 51334], "temperature":
  0.0, "avg_logprob": -0.16834406088326723, "compression_ratio": 1.658273381294964,
  "no_speech_prob": 0.00031480571487918496}, {"id": 703, "seek": 230190, "start":
  2321.3, "end": 2323.82, "text": " is that I can take a query in any vector space.",
  "tokens": [51334, 307, 300, 286, 393, 747, 257, 14581, 294, 604, 8062, 1901, 13,
  51460], "temperature": 0.0, "avg_logprob": -0.16834406088326723, "compression_ratio":
  1.658273381294964, "no_speech_prob": 0.00031480571487918496}, {"id": 704, "seek":
  230190, "start": 2323.82, "end": 2326.02, "text": " So for example, if I take a
  lexical query here,", "tokens": [51460, 407, 337, 1365, 11, 498, 286, 747, 257,
  476, 87, 804, 14581, 510, 11, 51570], "temperature": 0.0, "avg_logprob": -0.16834406088326723,
  "compression_ratio": 1.658273381294964, "no_speech_prob": 0.00031480571487918496},
  {"id": 705, "seek": 230190, "start": 2327.9, "end": 2331.62, "text": " I can easily
  take a lasagna or drive through it, what have you.", "tokens": [51664, 286, 393,
  3612, 747, 257, 2439, 35697, 420, 3332, 807, 309, 11, 437, 362, 291, 13, 51850],
  "temperature": 0.0, "avg_logprob": -0.16834406088326723, "compression_ratio": 1.658273381294964,
  "no_speech_prob": 0.00031480571487918496}, {"id": 706, "seek": 233162, "start":
  2331.62, "end": 2334.7799999999997, "text": " And I can generate these representations
  over here", "tokens": [50364, 400, 286, 393, 8460, 613, 33358, 670, 510, 50522],
  "temperature": 0.0, "avg_logprob": -0.27583667719475574, "compression_ratio": 1.7725321888412018,
  "no_speech_prob": 0.00028894373099319637}, {"id": 707, "seek": 233162, "start":
  2334.7799999999997, "end": 2338.98, "text": " by taking a lasagna, finding a dockset
  that matches that keyword,", "tokens": [50522, 538, 1940, 257, 2439, 35697, 11,
  5006, 257, 360, 2761, 302, 300, 10676, 300, 20428, 11, 50732], "temperature": 0.0,
  "avg_logprob": -0.27583667719475574, "compression_ratio": 1.7725321888412018, "no_speech_prob":
  0.00028894373099319637}, {"id": 708, "seek": 233162, "start": 2338.98, "end": 2342.1,
  "text": " and then from that dockset, finding these other relationships,", "tokens":
  [50732, 293, 550, 490, 300, 360, 2761, 302, 11, 5006, 613, 661, 6159, 11, 50888],
  "temperature": 0.0, "avg_logprob": -0.27583667719475574, "compression_ratio": 1.7725321888412018,
  "no_speech_prob": 0.00028894373099319637}, {"id": 709, "seek": 233162, "start":
  2342.1, "end": 2346.94, "text": " for example, lasagna can be described as Italian",
  "tokens": [50888, 337, 1365, 11, 2439, 35697, 393, 312, 7619, 382, 10003, 51130],
  "temperature": 0.0, "avg_logprob": -0.27583667719475574, "compression_ratio": 1.7725321888412018,
  "no_speech_prob": 0.00028894373099319637}, {"id": 710, "seek": 233162, "start":
  2346.94, "end": 2350.1, "text": " with keywords like lasagna, Alfredo pasta and
  Italian.", "tokens": [51130, 365, 21009, 411, 2439, 35697, 11, 28327, 78, 13296,
  293, 10003, 13, 51288], "temperature": 0.0, "avg_logprob": -0.27583667719475574,
  "compression_ratio": 1.7725321888412018, "no_speech_prob": 0.00028894373099319637},
  {"id": 711, "seek": 233162, "start": 2351.22, "end": 2354.14, "text": " And then
  Korean barbecue can be represented as category", "tokens": [51344, 400, 550, 6933,
  21877, 393, 312, 10379, 382, 7719, 51490], "temperature": 0.0, "avg_logprob": -0.27583667719475574,
  "compression_ratio": 1.7725321888412018, "no_speech_prob": 0.00028894373099319637},
  {"id": 712, "seek": 233162, "start": 2354.14, "end": 2357.54, "text": " of Korean
  with terms like Korean,", "tokens": [51490, 295, 6933, 365, 2115, 411, 6933, 11,
  51660], "temperature": 0.0, "avg_logprob": -0.27583667719475574, "compression_ratio":
  1.7725321888412018, "no_speech_prob": 0.00028894373099319637}, {"id": 713, "seek":
  233162, "start": 2357.54, "end": 2360.42, "text": " Bonchon, Saruwan, et cetera,
  fast food,", "tokens": [51660, 7368, 339, 266, 11, 6894, 84, 7916, 11, 1030, 11458,
  11, 2370, 1755, 11, 51804], "temperature": 0.0, "avg_logprob": -0.27583667719475574,
  "compression_ratio": 1.7725321888412018, "no_speech_prob": 0.00028894373099319637},
  {"id": 714, "seek": 236042, "start": 2360.42, "end": 2362.1800000000003, "text":
  " gets things like McDonald''s in window.", "tokens": [50364, 2170, 721, 411, 16889,
  311, 294, 4910, 13, 50452], "temperature": 0.0, "avg_logprob": -0.12369064952051917,
  "compression_ratio": 1.7932330827067668, "no_speech_prob": 0.0006806566379964352},
  {"id": 715, "seek": 236042, "start": 2362.1800000000003, "end": 2363.98, "text":
  " So this is purely leveraging,", "tokens": [50452, 407, 341, 307, 17491, 32666,
  11, 50542], "temperature": 0.0, "avg_logprob": -0.12369064952051917, "compression_ratio":
  1.7932330827067668, "no_speech_prob": 0.0006806566379964352}, {"id": 716, "seek":
  236042, "start": 2363.98, "end": 2365.34, "text": " and I''ve been doing this for
  years,", "tokens": [50542, 293, 286, 600, 668, 884, 341, 337, 924, 11, 50610], "temperature":
  0.0, "avg_logprob": -0.12369064952051917, "compression_ratio": 1.7932330827067668,
  "no_speech_prob": 0.0006806566379964352}, {"id": 717, "seek": 236042, "start": 2365.34,
  "end": 2367.34, "text": " and it works very, very well.", "tokens": [50610, 293,
  309, 1985, 588, 11, 588, 731, 13, 50710], "temperature": 0.0, "avg_logprob": -0.12369064952051917,
  "compression_ratio": 1.7932330827067668, "no_speech_prob": 0.0006806566379964352},
  {"id": 718, "seek": 236042, "start": 2367.34, "end": 2369.9, "text": " But this
  is purely leveraging the inverted index", "tokens": [50710, 583, 341, 307, 17491,
  32666, 264, 38969, 8186, 50838], "temperature": 0.0, "avg_logprob": -0.12369064952051917,
  "compression_ratio": 1.7932330827067668, "no_speech_prob": 0.0006806566379964352},
  {"id": 719, "seek": 236042, "start": 2369.9, "end": 2371.3, "text": " in this document
  set.", "tokens": [50838, 294, 341, 4166, 992, 13, 50908], "temperature": 0.0, "avg_logprob":
  -0.12369064952051917, "compression_ratio": 1.7932330827067668, "no_speech_prob":
  0.0006806566379964352}, {"id": 720, "seek": 236042, "start": 2371.3, "end": 2373.1800000000003,
  "text": " But the idea with the wormhole vectors", "tokens": [50908, 583, 264, 1558,
  365, 264, 23835, 14094, 18875, 51002], "temperature": 0.0, "avg_logprob": -0.12369064952051917,
  "compression_ratio": 1.7932330827067668, "no_speech_prob": 0.0006806566379964352},
  {"id": 721, "seek": 236042, "start": 2373.1800000000003, "end": 2377.5, "text":
  " is not just to stay within a single vector space,", "tokens": [51002, 307, 406,
  445, 281, 1754, 1951, 257, 2167, 8062, 1901, 11, 51218], "temperature": 0.0, "avg_logprob":
  -0.12369064952051917, "compression_ratio": 1.7932330827067668, "no_speech_prob":
  0.0006806566379964352}, {"id": 722, "seek": 236042, "start": 2377.5, "end": 2379.14,
  "text": " but to be able to go across vector spaces.", "tokens": [51218, 457, 281,
  312, 1075, 281, 352, 2108, 8062, 7673, 13, 51300], "temperature": 0.0, "avg_logprob":
  -0.12369064952051917, "compression_ratio": 1.7932330827067668, "no_speech_prob":
  0.0006806566379964352}, {"id": 723, "seek": 236042, "start": 2379.14, "end": 2383.2200000000003,
  "text": " So similarly, I should be able to take an embedding", "tokens": [51300,
  407, 14138, 11, 286, 820, 312, 1075, 281, 747, 364, 12240, 3584, 51504], "temperature":
  0.0, "avg_logprob": -0.12369064952051917, "compression_ratio": 1.7932330827067668,
  "no_speech_prob": 0.0006806566379964352}, {"id": 724, "seek": 236042, "start": 2383.2200000000003,
  "end": 2386.9, "text": " that finds a region in semantic vector space", "tokens":
  [51504, 300, 10704, 257, 4458, 294, 47982, 8062, 1901, 51688], "temperature": 0.0,
  "avg_logprob": -0.12369064952051917, "compression_ratio": 1.7932330827067668, "no_speech_prob":
  0.0006806566379964352}, {"id": 725, "seek": 236042, "start": 2386.9, "end": 2389.62,
  "text": " and a dense space, find the nearby things,", "tokens": [51688, 293, 257,
  18011, 1901, 11, 915, 264, 11184, 721, 11, 51824], "temperature": 0.0, "avg_logprob":
  -0.12369064952051917, "compression_ratio": 1.7932330827067668, "no_speech_prob":
  0.0006806566379964352}, {"id": 726, "seek": 238962, "start": 2389.62, "end": 2392.02,
  "text": " which ultimately just translate to a dockset.", "tokens": [50364, 597,
  6284, 445, 13799, 281, 257, 360, 2761, 302, 13, 50484], "temperature": 0.0, "avg_logprob":
  -0.12167274212015086, "compression_ratio": 1.7849829351535835, "no_speech_prob":
  8.210516534745693e-05}, {"id": 727, "seek": 238962, "start": 2392.02, "end": 2394.7,
  "text": " And then from that dockset, I can use the same technique", "tokens": [50484,
  400, 550, 490, 300, 360, 2761, 302, 11, 286, 393, 764, 264, 912, 6532, 50618], "temperature":
  0.0, "avg_logprob": -0.12167274212015086, "compression_ratio": 1.7849829351535835,
  "no_speech_prob": 8.210516534745693e-05}, {"id": 728, "seek": 238962, "start": 2394.7,
  "end": 2396.7799999999997, "text": " to say what are the things that are related",
  "tokens": [50618, 281, 584, 437, 366, 264, 721, 300, 366, 4077, 50722], "temperature":
  0.0, "avg_logprob": -0.12167274212015086, "compression_ratio": 1.7849829351535835,
  "no_speech_prob": 8.210516534745693e-05}, {"id": 729, "seek": 238962, "start": 2396.7799999999997,
  "end": 2399.14, "text": " within these documents and generate", "tokens": [50722,
  1951, 613, 8512, 293, 8460, 50840], "temperature": 0.0, "avg_logprob": -0.12167274212015086,
  "compression_ratio": 1.7849829351535835, "no_speech_prob": 8.210516534745693e-05},
  {"id": 730, "seek": 238962, "start": 2399.14, "end": 2401.7, "text": " the similar
  kinds of outputs over here?", "tokens": [50840, 264, 2531, 3685, 295, 23930, 670,
  510, 30, 50968], "temperature": 0.0, "avg_logprob": -0.12167274212015086, "compression_ratio":
  1.7849829351535835, "no_speech_prob": 8.210516534745693e-05}, {"id": 731, "seek":
  238962, "start": 2401.7, "end": 2404.7, "text": " You can also think of this, if
  taking away", "tokens": [50968, 509, 393, 611, 519, 295, 341, 11, 498, 1940, 1314,
  51118], "temperature": 0.0, "avg_logprob": -0.12167274212015086, "compression_ratio":
  1.7849829351535835, "no_speech_prob": 8.210516534745693e-05}, {"id": 732, "seek":
  238962, "start": 2404.7, "end": 2407.22, "text": " all the wormhole vector terminology,",
  "tokens": [51118, 439, 264, 23835, 14094, 8062, 27575, 11, 51244], "temperature":
  0.0, "avg_logprob": -0.12167274212015086, "compression_ratio": 1.7849829351535835,
  "no_speech_prob": 8.210516534745693e-05}, {"id": 733, "seek": 238962, "start": 2407.22,
  "end": 2408.94, "text": " you can think of this as just a way to make", "tokens":
  [51244, 291, 393, 519, 295, 341, 382, 445, 257, 636, 281, 652, 51330], "temperature":
  0.0, "avg_logprob": -0.12167274212015086, "compression_ratio": 1.7849829351535835,
  "no_speech_prob": 8.210516534745693e-05}, {"id": 734, "seek": 238962, "start": 2408.94,
  "end": 2410.98, "text": " your embeddings more explainable.", "tokens": [51330,
  428, 12240, 29432, 544, 2903, 712, 13, 51432], "temperature": 0.0, "avg_logprob":
  -0.12167274212015086, "compression_ratio": 1.7849829351535835, "no_speech_prob":
  8.210516534745693e-05}, {"id": 735, "seek": 238962, "start": 2410.98, "end": 2413.66,
  "text": " I''ve got an embedding, I go to a dense vector space,", "tokens": [51432,
  286, 600, 658, 364, 12240, 3584, 11, 286, 352, 281, 257, 18011, 8062, 1901, 11,
  51566], "temperature": 0.0, "avg_logprob": -0.12167274212015086, "compression_ratio":
  1.7849829351535835, "no_speech_prob": 8.210516534745693e-05}, {"id": 736, "seek":
  238962, "start": 2413.66, "end": 2416.02, "text": " I find documents, and then from
  that set of documents,", "tokens": [51566, 286, 915, 8512, 11, 293, 550, 490, 300,
  992, 295, 8512, 11, 51684], "temperature": 0.0, "avg_logprob": -0.12167274212015086,
  "compression_ratio": 1.7849829351535835, "no_speech_prob": 8.210516534745693e-05},
  {"id": 737, "seek": 238962, "start": 2416.02, "end": 2418.14, "text": " I''m now
  deriving a lexical vector,", "tokens": [51684, 286, 478, 586, 1163, 2123, 257, 476,
  87, 804, 8062, 11, 51790], "temperature": 0.0, "avg_logprob": -0.12167274212015086,
  "compression_ratio": 1.7849829351535835, "no_speech_prob": 8.210516534745693e-05},
  {"id": 738, "seek": 241814, "start": 2418.14, "end": 2421.58, "text": " which is
  readable that''s describing what''s happening there.", "tokens": [50364, 597, 307,
  49857, 300, 311, 16141, 437, 311, 2737, 456, 13, 50536], "temperature": 0.0, "avg_logprob":
  -0.13206357404220204, "compression_ratio": 1.6751824817518248, "no_speech_prob":
  0.0001020477429847233}, {"id": 739, "seek": 241814, "start": 2421.58, "end": 2422.7799999999997,
  "text": " And of course, I can then turn around", "tokens": [50536, 400, 295, 1164,
  11, 286, 393, 550, 1261, 926, 50596], "temperature": 0.0, "avg_logprob": -0.13206357404220204,
  "compression_ratio": 1.6751824817518248, "no_speech_prob": 0.0001020477429847233},
  {"id": 740, "seek": 241814, "start": 2422.7799999999997, "end": 2425.66, "text":
  " and take that and query in my sparse space", "tokens": [50596, 293, 747, 300,
  293, 14581, 294, 452, 637, 11668, 1901, 50740], "temperature": 0.0, "avg_logprob":
  -0.13206357404220204, "compression_ratio": 1.6751824817518248, "no_speech_prob":
  0.0001020477429847233}, {"id": 741, "seek": 241814, "start": 2425.66, "end": 2428.2999999999997,
  "text": " to match other things that have the terms,", "tokens": [50740, 281, 2995,
  661, 721, 300, 362, 264, 2115, 11, 50872], "temperature": 0.0, "avg_logprob": -0.13206357404220204,
  "compression_ratio": 1.6751824817518248, "no_speech_prob": 0.0001020477429847233},
  {"id": 742, "seek": 241814, "start": 2428.2999999999997, "end": 2429.8599999999997,
  "text": " but maybe didn''t match in the dense space.", "tokens": [50872, 457, 1310,
  994, 380, 2995, 294, 264, 18011, 1901, 13, 50950], "temperature": 0.0, "avg_logprob":
  -0.13206357404220204, "compression_ratio": 1.6751824817518248, "no_speech_prob":
  0.0001020477429847233}, {"id": 743, "seek": 241814, "start": 2429.8599999999997,
  "end": 2431.7, "text": " So that''s the general idea.", "tokens": [50950, 407, 300,
  311, 264, 2674, 1558, 13, 51042], "temperature": 0.0, "avg_logprob": -0.13206357404220204,
  "compression_ratio": 1.6751824817518248, "no_speech_prob": 0.0001020477429847233},
  {"id": 744, "seek": 241814, "start": 2432.8199999999997, "end": 2437.9, "text":
  " There''s one last thing I wanted to cover briefly,", "tokens": [51098, 821, 311,
  472, 1036, 551, 286, 1415, 281, 2060, 10515, 11, 51352], "temperature": 0.0, "avg_logprob":
  -0.13206357404220204, "compression_ratio": 1.6751824817518248, "no_speech_prob":
  0.0001020477429847233}, {"id": 745, "seek": 241814, "start": 2437.9, "end": 2440.62,
  "text": " which is this notion of behavioral embedding spaces,", "tokens": [51352,
  597, 307, 341, 10710, 295, 19124, 12240, 3584, 7673, 11, 51488], "temperature":
  0.0, "avg_logprob": -0.13206357404220204, "compression_ratio": 1.6751824817518248,
  "no_speech_prob": 0.0001020477429847233}, {"id": 746, "seek": 241814, "start": 2440.62,
  "end": 2442.66, "text": " because I''ve mentioned it multiple times.", "tokens":
  [51488, 570, 286, 600, 2835, 309, 3866, 1413, 13, 51590], "temperature": 0.0, "avg_logprob":
  -0.13206357404220204, "compression_ratio": 1.6751824817518248, "no_speech_prob":
  0.0001020477429847233}, {"id": 747, "seek": 241814, "start": 2442.66, "end": 2446.22,
  "text": " And I have a feeling a lot of people aren''t super familiar.", "tokens":
  [51590, 400, 286, 362, 257, 2633, 257, 688, 295, 561, 3212, 380, 1687, 4963, 13,
  51768], "temperature": 0.0, "avg_logprob": -0.13206357404220204, "compression_ratio":
  1.6751824817518248, "no_speech_prob": 0.0001020477429847233}, {"id": 748, "seek":
  244622, "start": 2446.2999999999997, "end": 2450.14, "text": " And so let me click
  here.", "tokens": [50368, 400, 370, 718, 385, 2052, 510, 13, 50560], "temperature":
  0.0, "avg_logprob": -0.12966444553473058, "compression_ratio": 1.6072727272727272,
  "no_speech_prob": 0.0005561095895245671}, {"id": 749, "seek": 244622, "start": 2450.14,
  "end": 2451.98, "text": " The general idea, and I''ll be very quick through this,",
  "tokens": [50560, 440, 2674, 1558, 11, 293, 286, 603, 312, 588, 1702, 807, 341,
  11, 50652], "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0005561095895245671}, {"id": 750, "seek":
  244622, "start": 2451.98, "end": 2453.8199999999997, "text": " we''ll spend more
  time in the AI Power Search course", "tokens": [50652, 321, 603, 3496, 544, 565,
  294, 264, 7318, 7086, 17180, 1164, 50744], "temperature": 0.0, "avg_logprob": -0.12966444553473058,
  "compression_ratio": 1.6072727272727272, "no_speech_prob": 0.0005561095895245671},
  {"id": 751, "seek": 244622, "start": 2453.8199999999997, "end": 2457.7799999999997,
  "text": " diving into all of this, but the very high level intuition", "tokens":
  [50744, 20241, 666, 439, 295, 341, 11, 457, 264, 588, 1090, 1496, 24002, 50942],
  "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio": 1.6072727272727272,
  "no_speech_prob": 0.0005561095895245671}, {"id": 752, "seek": 244622, "start": 2457.7799999999997,
  "end": 2461.2999999999997, "text": " is that when users interact with your documents,
  right?", "tokens": [50942, 307, 300, 562, 5022, 4648, 365, 428, 8512, 11, 558, 30,
  51118], "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0005561095895245671}, {"id": 753, "seek":
  244622, "start": 2461.2999999999997, "end": 2463.74, "text": " They run queries,
  they click on things,", "tokens": [51118, 814, 1190, 24109, 11, 436, 2052, 322,
  721, 11, 51240], "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0005561095895245671}, {"id": 754, "seek":
  244622, "start": 2463.74, "end": 2466.2999999999997, "text": " they like them, add
  to cart purchase,", "tokens": [51240, 436, 411, 552, 11, 909, 281, 5467, 8110, 11,
  51368], "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0005561095895245671}, {"id": 755, "seek":
  244622, "start": 2466.2999999999997, "end": 2468.3799999999997, "text": " those
  are user behavioral signals.", "tokens": [51368, 729, 366, 4195, 19124, 12354, 13,
  51472], "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0005561095895245671}, {"id": 756, "seek":
  244622, "start": 2468.3799999999997, "end": 2470.98, "text": " And if you''ve got
  a sufficient amount of traffic,", "tokens": [51472, 400, 498, 291, 600, 658, 257,
  11563, 2372, 295, 6419, 11, 51602], "temperature": 0.0, "avg_logprob": -0.12966444553473058,
  "compression_ratio": 1.6072727272727272, "no_speech_prob": 0.0005561095895245671},
  {"id": 757, "seek": 244622, "start": 2470.98, "end": 2472.58, "text": " you want
  to be collecting those", "tokens": [51602, 291, 528, 281, 312, 12510, 729, 51682],
  "temperature": 0.0, "avg_logprob": -0.12966444553473058, "compression_ratio": 1.6072727272727272,
  "no_speech_prob": 0.0005561095895245671}, {"id": 758, "seek": 247258, "start": 2472.58,
  "end": 2477.42, "text": " and leveraging them to build reflected intelligence algorithms.",
  "tokens": [50364, 293, 32666, 552, 281, 1322, 15502, 7599, 14642, 13, 50606], "temperature":
  0.0, "avg_logprob": -0.1764691925048828, "compression_ratio": 1.828358208955224,
  "no_speech_prob": 0.000283190980553627}, {"id": 759, "seek": 247258, "start": 2477.42,
  "end": 2479.62, "text": " So one of the types I mentioned", "tokens": [50606, 407,
  472, 295, 264, 3467, 286, 2835, 50716], "temperature": 0.0, "avg_logprob": -0.1764691925048828,
  "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 760, "seek": 247258, "start": 2479.62, "end": 2482.8199999999997, "text":
  " several earlier signals boosting, collaborative filtering,", "tokens": [50716,
  2940, 3071, 12354, 43117, 11, 16555, 30822, 11, 50876], "temperature": 0.0, "avg_logprob":
  -0.1764691925048828, "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 761, "seek": 247258, "start": 2482.8199999999997, "end": 2484.9, "text":
  " and matrix factorization, learning to rank,", "tokens": [50876, 293, 8141, 5952,
  2144, 11, 2539, 281, 6181, 11, 50980], "temperature": 0.0, "avg_logprob": -0.1764691925048828,
  "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 762, "seek": 247258, "start": 2484.9, "end": 2486.66, "text": " and knowledge
  graph learning,", "tokens": [50980, 293, 3601, 4295, 2539, 11, 51068], "temperature":
  0.0, "avg_logprob": -0.1764691925048828, "compression_ratio": 1.828358208955224,
  "no_speech_prob": 0.000283190980553627}, {"id": 763, "seek": 247258, "start": 2486.66,
  "end": 2489.18, "text": " but specifically on collaborative filtering,", "tokens":
  [51068, 457, 4682, 322, 16555, 30822, 11, 51194], "temperature": 0.0, "avg_logprob":
  -0.1764691925048828, "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 764, "seek": 247258, "start": 2489.18, "end": 2492.38, "text": " which is
  mostly focused on personalized search,", "tokens": [51194, 597, 307, 5240, 5178,
  322, 28415, 3164, 11, 51354], "temperature": 0.0, "avg_logprob": -0.1764691925048828,
  "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 765, "seek": 247258, "start": 2492.38, "end": 2493.7799999999997, "text":
  " or understanding user behavior", "tokens": [51354, 420, 3701, 4195, 5223, 51424],
  "temperature": 0.0, "avg_logprob": -0.1764691925048828, "compression_ratio": 1.828358208955224,
  "no_speech_prob": 0.000283190980553627}, {"id": 766, "seek": 247258, "start": 2493.7799999999997,
  "end": 2496.34, "text": " to generate better personalized results.", "tokens": [51424,
  281, 8460, 1101, 28415, 3542, 13, 51552], "temperature": 0.0, "avg_logprob": -0.1764691925048828,
  "compression_ratio": 1.828358208955224, "no_speech_prob": 0.000283190980553627},
  {"id": 767, "seek": 247258, "start": 2496.34, "end": 2498.7, "text": " We typically
  leverage collaborative filtering,", "tokens": [51552, 492, 5850, 13982, 16555, 30822,
  11, 51670], "temperature": 0.0, "avg_logprob": -0.1764691925048828, "compression_ratio":
  1.828358208955224, "no_speech_prob": 0.000283190980553627}, {"id": 768, "seek":
  247258, "start": 2498.7, "end": 2500.86, "text": " which is now algorithm for doing
  recommendations.", "tokens": [51670, 597, 307, 586, 9284, 337, 884, 10434, 13, 51778],
  "temperature": 0.0, "avg_logprob": -0.1764691925048828, "compression_ratio": 1.828358208955224,
  "no_speech_prob": 0.000283190980553627}, {"id": 769, "seek": 250086, "start": 2500.86,
  "end": 2502.98, "text": " So I start with a particular item,", "tokens": [50364,
  407, 286, 722, 365, 257, 1729, 3174, 11, 50470], "temperature": 0.0, "avg_logprob":
  -0.17474715492942117, "compression_ratio": 1.7568627450980392, "no_speech_prob":
  0.0001063140225596726}, {"id": 770, "seek": 250086, "start": 2502.98, "end": 2506.3,
  "text": " or particular user, and I recommend other items", "tokens": [50470, 420,
  1729, 4195, 11, 293, 286, 2748, 661, 4754, 50636], "temperature": 0.0, "avg_logprob":
  -0.17474715492942117, "compression_ratio": 1.7568627450980392, "no_speech_prob":
  0.0001063140225596726}, {"id": 771, "seek": 250086, "start": 2506.3, "end": 2508.46,
  "text": " based upon that item or user.", "tokens": [50636, 2361, 3564, 300, 3174,
  420, 4195, 13, 50744], "temperature": 0.0, "avg_logprob": -0.17474715492942117,
  "compression_ratio": 1.7568627450980392, "no_speech_prob": 0.0001063140225596726},
  {"id": 772, "seek": 250086, "start": 2508.46, "end": 2510.3, "text": " So this is
  what that typically looks like, right?", "tokens": [50744, 407, 341, 307, 437, 300,
  5850, 1542, 411, 11, 558, 30, 50836], "temperature": 0.0, "avg_logprob": -0.17474715492942117,
  "compression_ratio": 1.7568627450980392, "no_speech_prob": 0.0001063140225596726},
  {"id": 773, "seek": 250086, "start": 2510.3, "end": 2513.46, "text": " Somebody
  runs searches or purchases things like Apple", "tokens": [50836, 13463, 6676, 26701,
  420, 26762, 721, 411, 6373, 50994], "temperature": 0.0, "avg_logprob": -0.17474715492942117,
  "compression_ratio": 1.7568627450980392, "no_speech_prob": 0.0001063140225596726},
  {"id": 774, "seek": 250086, "start": 2513.46, "end": 2516.7000000000003, "text":
  " and MacBook, and then these are the items they interact with,", "tokens": [50994,
  293, 31737, 11, 293, 550, 613, 366, 264, 4754, 436, 4648, 365, 11, 51156], "temperature":
  0.0, "avg_logprob": -0.17474715492942117, "compression_ratio": 1.7568627450980392,
  "no_speech_prob": 0.0001063140225596726}, {"id": 775, "seek": 250086, "start": 2516.7000000000003,
  "end": 2519.82, "text": " iPads and MacBook Airs, things like that.", "tokens":
  [51156, 5180, 5834, 293, 31737, 5774, 82, 11, 721, 411, 300, 13, 51312], "temperature":
  0.0, "avg_logprob": -0.17474715492942117, "compression_ratio": 1.7568627450980392,
  "no_speech_prob": 0.0001063140225596726}, {"id": 776, "seek": 250086, "start": 2519.82,
  "end": 2521.7400000000002, "text": " And then for that user, we can generate", "tokens":
  [51312, 400, 550, 337, 300, 4195, 11, 321, 393, 8460, 51408], "temperature": 0.0,
  "avg_logprob": -0.17474715492942117, "compression_ratio": 1.7568627450980392, "no_speech_prob":
  0.0001063140225596726}, {"id": 777, "seek": 250086, "start": 2521.7400000000002,
  "end": 2524.78, "text": " this list of recommendations based upon running", "tokens":
  [51408, 341, 1329, 295, 10434, 2361, 3564, 2614, 51560], "temperature": 0.0, "avg_logprob":
  -0.17474715492942117, "compression_ratio": 1.7568627450980392, "no_speech_prob":
  0.0001063140225596726}, {"id": 778, "seek": 250086, "start": 2524.78, "end": 2527.78,
  "text": " this collaborative filtering algorithm.", "tokens": [51560, 341, 16555,
  30822, 9284, 13, 51710], "temperature": 0.0, "avg_logprob": -0.17474715492942117,
  "compression_ratio": 1.7568627450980392, "no_speech_prob": 0.0001063140225596726},
  {"id": 779, "seek": 252778, "start": 2527.78, "end": 2532.5, "text": " In this case,
  I want to briefly mention again,", "tokens": [50364, 682, 341, 1389, 11, 286, 528,
  281, 10515, 2152, 797, 11, 50600], "temperature": 0.0, "avg_logprob": -0.1571255260043674,
  "compression_ratio": 1.8680851063829786, "no_speech_prob": 0.0008366529946215451},
  {"id": 780, "seek": 252778, "start": 2532.5, "end": 2535.78, "text": " that with
  typical content based embeddings,", "tokens": [50600, 300, 365, 7476, 2701, 2361,
  12240, 29432, 11, 50764], "temperature": 0.0, "avg_logprob": -0.1571255260043674,
  "compression_ratio": 1.8680851063829786, "no_speech_prob": 0.0008366529946215451},
  {"id": 781, "seek": 252778, "start": 2535.78, "end": 2538.26, "text": " I mentioned
  latent features earlier.", "tokens": [50764, 286, 2835, 48994, 4122, 3071, 13, 50888],
  "temperature": 0.0, "avg_logprob": -0.1571255260043674, "compression_ratio": 1.8680851063829786,
  "no_speech_prob": 0.0008366529946215451}, {"id": 782, "seek": 252778, "start": 2538.26,
  "end": 2540.46, "text": " Typically you have items,", "tokens": [50888, 23129, 291,
  362, 4754, 11, 50998], "temperature": 0.0, "avg_logprob": -0.1571255260043674, "compression_ratio":
  1.8680851063829786, "no_speech_prob": 0.0008366529946215451}, {"id": 783, "seek":
  252778, "start": 2540.46, "end": 2544.7000000000003, "text": " and there''s these
  densely packed dimensions", "tokens": [50998, 293, 456, 311, 613, 24505, 736, 13265,
  12819, 51210], "temperature": 0.0, "avg_logprob": -0.1571255260043674, "compression_ratio":
  1.8680851063829786, "no_speech_prob": 0.0008366529946215451}, {"id": 784, "seek":
  252778, "start": 2544.7000000000003, "end": 2547.5, "text": " that represents different
  features.", "tokens": [51210, 300, 8855, 819, 4122, 13, 51350], "temperature": 0.0,
  "avg_logprob": -0.1571255260043674, "compression_ratio": 1.8680851063829786, "no_speech_prob":
  0.0008366529946215451}, {"id": 785, "seek": 252778, "start": 2547.5, "end": 2550.34,
  "text": " Collectively, this particular feature", "tokens": [51350, 31896, 3413,
  11, 341, 1729, 4111, 51492], "temperature": 0.0, "avg_logprob": -0.1571255260043674,
  "compression_ratio": 1.8680851063829786, "no_speech_prob": 0.0008366529946215451},
  {"id": 786, "seek": 252778, "start": 2550.34, "end": 2552.5, "text": " might have
  a strong correlation with size,", "tokens": [51492, 1062, 362, 257, 2068, 20009,
  365, 2744, 11, 51600], "temperature": 0.0, "avg_logprob": -0.1571255260043674, "compression_ratio":
  1.8680851063829786, "no_speech_prob": 0.0008366529946215451}, {"id": 787, "seek":
  252778, "start": 2552.5, "end": 2554.5800000000004, "text": " this one I have a
  strong correlation with color,", "tokens": [51600, 341, 472, 286, 362, 257, 2068,
  20009, 365, 2017, 11, 51704], "temperature": 0.0, "avg_logprob": -0.1571255260043674,
  "compression_ratio": 1.8680851063829786, "no_speech_prob": 0.0008366529946215451},
  {"id": 788, "seek": 252778, "start": 2554.5800000000004, "end": 2556.1400000000003,
  "text": " this one I have a strong correlation with,", "tokens": [51704, 341, 472,
  286, 362, 257, 2068, 20009, 365, 11, 51782], "temperature": 0.0, "avg_logprob":
  -0.1571255260043674, "compression_ratio": 1.8680851063829786, "no_speech_prob":
  0.0008366529946215451}, {"id": 789, "seek": 252778, "start": 2556.1400000000003,
  "end": 2557.7400000000002, "text": " is this kind of like a computer.", "tokens":
  [51782, 307, 341, 733, 295, 411, 257, 3820, 13, 51862], "temperature": 0.0, "avg_logprob":
  -0.1571255260043674, "compression_ratio": 1.8680851063829786, "no_speech_prob":
  0.0008366529946215451}, {"id": 790, "seek": 255774, "start": 2557.74, "end": 2562.18,
  "text": " But those meanings spread across many different", "tokens": [50364, 583,
  729, 28138, 3974, 2108, 867, 819, 50586], "temperature": 0.0, "avg_logprob": -0.1256363902773176,
  "compression_ratio": 1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 791,
  "seek": 255774, "start": 2562.18, "end": 2564.2999999999997, "text": " of these
  dimensions.", "tokens": [50586, 295, 613, 12819, 13, 50692], "temperature": 0.0,
  "avg_logprob": -0.1256363902773176, "compression_ratio": 1.96875, "no_speech_prob":
  8.213351247832179e-05}, {"id": 792, "seek": 255774, "start": 2564.2999999999997,
  "end": 2567.2599999999998, "text": " Similarly, whenever we''re doing collaborative
  filtering,", "tokens": [50692, 13157, 11, 5699, 321, 434, 884, 16555, 30822, 11,
  50840], "temperature": 0.0, "avg_logprob": -0.1256363902773176, "compression_ratio":
  1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 793, "seek": 255774, "start":
  2567.2599999999998, "end": 2571.06, "text": " these also rely on latent features
  or latent dimensions.", "tokens": [50840, 613, 611, 10687, 322, 48994, 4122, 420,
  48994, 12819, 13, 51030], "temperature": 0.0, "avg_logprob": -0.1256363902773176,
  "compression_ratio": 1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 794,
  "seek": 255774, "start": 2571.06, "end": 2574.4599999999996, "text": " So for example,
  if I have a bunch of users,", "tokens": [51030, 407, 337, 1365, 11, 498, 286, 362,
  257, 3840, 295, 5022, 11, 51200], "temperature": 0.0, "avg_logprob": -0.1256363902773176,
  "compression_ratio": 1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 795,
  "seek": 255774, "start": 2574.4599999999996, "end": 2577.18, "text": " my first
  user likes these three movies,", "tokens": [51200, 452, 700, 4195, 5902, 613, 1045,
  6233, 11, 51336], "temperature": 0.0, "avg_logprob": -0.1256363902773176, "compression_ratio":
  1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 796, "seek": 255774, "start":
  2577.18, "end": 2579.58, "text": " my next user likes these three movies,", "tokens":
  [51336, 452, 958, 4195, 5902, 613, 1045, 6233, 11, 51456], "temperature": 0.0, "avg_logprob":
  -0.1256363902773176, "compression_ratio": 1.96875, "no_speech_prob": 8.213351247832179e-05},
  {"id": 797, "seek": 255774, "start": 2579.58, "end": 2581.3399999999997, "text":
  " my third user likes these three,", "tokens": [51456, 452, 2636, 4195, 5902, 613,
  1045, 11, 51544], "temperature": 0.0, "avg_logprob": -0.1256363902773176, "compression_ratio":
  1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 798, "seek": 255774, "start":
  2581.3399999999997, "end": 2582.8999999999996, "text": " my next user likes these
  three,", "tokens": [51544, 452, 958, 4195, 5902, 613, 1045, 11, 51622], "temperature":
  0.0, "avg_logprob": -0.1256363902773176, "compression_ratio": 1.96875, "no_speech_prob":
  8.213351247832179e-05}, {"id": 799, "seek": 255774, "start": 2582.8999999999996,
  "end": 2585.06, "text": " and my last user likes these three.", "tokens": [51622,
  293, 452, 1036, 4195, 5902, 613, 1045, 13, 51730], "temperature": 0.0, "avg_logprob":
  -0.1256363902773176, "compression_ratio": 1.96875, "no_speech_prob": 8.213351247832179e-05},
  {"id": 800, "seek": 255774, "start": 2585.06, "end": 2586.8199999999997, "text":
  " You can kind of visually see here,", "tokens": [51730, 509, 393, 733, 295, 19622,
  536, 510, 11, 51818], "temperature": 0.0, "avg_logprob": -0.1256363902773176, "compression_ratio":
  1.96875, "no_speech_prob": 8.213351247832179e-05}, {"id": 801, "seek": 258682, "start":
  2586.82, "end": 2589.6600000000003, "text": " these are some similarity here,",
  "tokens": [50364, 613, 366, 512, 32194, 510, 11, 50506], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 802, "seek": 258682, "start": 2589.6600000000003, "end":
  2591.1000000000004, "text": " there''s some similarity here,", "tokens": [50506,
  456, 311, 512, 32194, 510, 11, 50578], "temperature": 0.0, "avg_logprob": -0.16618667431731723,
  "compression_ratio": 1.8274647887323943, "no_speech_prob": 0.00411580502986908},
  {"id": 803, "seek": 258682, "start": 2591.1000000000004, "end": 2593.38, "text":
  " your brain''s probably picking out what it is.", "tokens": [50578, 428, 3567,
  311, 1391, 8867, 484, 437, 309, 307, 13, 50692], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 804, "seek": 258682, "start": 2593.38, "end": 2596.46,
  "text": " But if I were to map these conceptually,", "tokens": [50692, 583, 498,
  286, 645, 281, 4471, 613, 3410, 671, 11, 50846], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 805, "seek": 258682, "start": 2596.46, "end": 2599.34,
  "text": " I would say that users one, two, and three", "tokens": [50846, 286, 576,
  584, 300, 5022, 472, 11, 732, 11, 293, 1045, 50990], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 806, "seek": 258682, "start": 2599.34, "end": 2601.46,
  "text": " tended to like movies that were about superheroes", "tokens": [50990,
  34732, 281, 411, 6233, 300, 645, 466, 45417, 51096], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 807, "seek": 258682, "start": 2601.46, "end": 2604.46,
  "text": " made by Marvel Studios and occasionally Warner Brothers,", "tokens": [51096,
  1027, 538, 13837, 23005, 293, 16895, 31769, 19886, 11, 51246], "temperature": 0.0,
  "avg_logprob": -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 808, "seek": 258682, "start": 2604.46, "end": 2605.5800000000004,
  "text": " they''re all action movies,", "tokens": [51246, 436, 434, 439, 3069, 6233,
  11, 51302], "temperature": 0.0, "avg_logprob": -0.16618667431731723, "compression_ratio":
  1.8274647887323943, "no_speech_prob": 0.00411580502986908}, {"id": 809, "seek":
  258682, "start": 2605.5800000000004, "end": 2607.54, "text": " and they''re not
  suitable for small children.", "tokens": [51302, 293, 436, 434, 406, 12873, 337,
  1359, 2227, 13, 51400], "temperature": 0.0, "avg_logprob": -0.16618667431731723,
  "compression_ratio": 1.8274647887323943, "no_speech_prob": 0.00411580502986908},
  {"id": 810, "seek": 258682, "start": 2607.54, "end": 2609.02, "text": " Whereas
  users four and five,", "tokens": [51400, 13813, 5022, 1451, 293, 1732, 11, 51474],
  "temperature": 0.0, "avg_logprob": -0.16618667431731723, "compression_ratio": 1.8274647887323943,
  "no_speech_prob": 0.00411580502986908}, {"id": 811, "seek": 258682, "start": 2609.02,
  "end": 2611.2200000000003, "text": " all liked animated movies,", "tokens": [51474,
  439, 4501, 18947, 6233, 11, 51584], "temperature": 0.0, "avg_logprob": -0.16618667431731723,
  "compression_ratio": 1.8274647887323943, "no_speech_prob": 0.00411580502986908},
  {"id": 812, "seek": 258682, "start": 2611.2200000000003, "end": 2612.94, "text":
  " all of them were suitable for small children,", "tokens": [51584, 439, 295, 552,
  645, 12873, 337, 1359, 2227, 11, 51670], "temperature": 0.0, "avg_logprob": -0.16618667431731723,
  "compression_ratio": 1.8274647887323943, "no_speech_prob": 0.00411580502986908},
  {"id": 813, "seek": 258682, "start": 2612.94, "end": 2615.1400000000003, "text":
  " and all of them were made by Disney and Pixar.", "tokens": [51670, 293, 439, 295,
  552, 645, 1027, 538, 8653, 293, 46695, 13, 51780], "temperature": 0.0, "avg_logprob":
  -0.16618667431731723, "compression_ratio": 1.8274647887323943, "no_speech_prob":
  0.00411580502986908}, {"id": 814, "seek": 261514, "start": 2616.1, "end": 2617.9,
  "text": " A collaborative filtering algorithm", "tokens": [50412, 316, 16555, 30822,
  9284, 50502], "temperature": 0.0, "avg_logprob": -0.15696475575271163, "compression_ratio":
  1.7020408163265306, "no_speech_prob": 0.001121428911574185}, {"id": 815, "seek":
  261514, "start": 2618.74, "end": 2621.3799999999997, "text": " sort of discovers
  these relationships", "tokens": [50544, 1333, 295, 44522, 613, 6159, 50676], "temperature":
  0.0, "avg_logprob": -0.15696475575271163, "compression_ratio": 1.7020408163265306,
  "no_speech_prob": 0.001121428911574185}, {"id": 816, "seek": 261514, "start": 2621.3799999999997,
  "end": 2623.54, "text": " and recommends based upon them", "tokens": [50676, 293,
  34556, 2361, 3564, 552, 50784], "temperature": 0.0, "avg_logprob": -0.15696475575271163,
  "compression_ratio": 1.7020408163265306, "no_speech_prob": 0.001121428911574185},
  {"id": 817, "seek": 261514, "start": 2623.54, "end": 2626.62, "text": " because
  they exist in the underlying documents,", "tokens": [50784, 570, 436, 2514, 294,
  264, 14217, 8512, 11, 50938], "temperature": 0.0, "avg_logprob": -0.15696475575271163,
  "compression_ratio": 1.7020408163265306, "no_speech_prob": 0.001121428911574185},
  {"id": 818, "seek": 261514, "start": 2626.62, "end": 2630.1, "text": " even though
  we don''t have them modeled out explicitly.", "tokens": [50938, 754, 1673, 321,
  500, 380, 362, 552, 37140, 484, 20803, 13, 51112], "temperature": 0.0, "avg_logprob":
  -0.15696475575271163, "compression_ratio": 1.7020408163265306, "no_speech_prob":
  0.001121428911574185}, {"id": 819, "seek": 261514, "start": 2630.1, "end": 2632.2999999999997,
  "text": " And the way this works with collaborative filtering", "tokens": [51112,
  400, 264, 636, 341, 1985, 365, 16555, 30822, 51222], "temperature": 0.0, "avg_logprob":
  -0.15696475575271163, "compression_ratio": 1.7020408163265306, "no_speech_prob":
  0.001121428911574185}, {"id": 820, "seek": 261514, "start": 2632.2999999999997,
  "end": 2634.8199999999997, "text": " is we do matrix factorization.", "tokens":
  [51222, 307, 321, 360, 8141, 5952, 2144, 13, 51348], "temperature": 0.0, "avg_logprob":
  -0.15696475575271163, "compression_ratio": 1.7020408163265306, "no_speech_prob":
  0.001121428911574185}, {"id": 821, "seek": 261514, "start": 2634.8199999999997,
  "end": 2638.18, "text": " So we start with a user item matrix,", "tokens": [51348,
  407, 321, 722, 365, 257, 4195, 3174, 8141, 11, 51516], "temperature": 0.0, "avg_logprob":
  -0.15696475575271163, "compression_ratio": 1.7020408163265306, "no_speech_prob":
  0.001121428911574185}, {"id": 822, "seek": 261514, "start": 2638.18, "end": 2639.62,
  "text": " where here''s my list of users,", "tokens": [51516, 689, 510, 311, 452,
  1329, 295, 5022, 11, 51588], "temperature": 0.0, "avg_logprob": -0.15696475575271163,
  "compression_ratio": 1.7020408163265306, "no_speech_prob": 0.001121428911574185},
  {"id": 823, "seek": 261514, "start": 2639.62, "end": 2640.62, "text": " and here''s
  my items,", "tokens": [51588, 293, 510, 311, 452, 4754, 11, 51638], "temperature":
  0.0, "avg_logprob": -0.15696475575271163, "compression_ratio": 1.7020408163265306,
  "no_speech_prob": 0.001121428911574185}, {"id": 824, "seek": 261514, "start": 2640.62,
  "end": 2643.3799999999997, "text": " and then these are sort of the amount", "tokens":
  [51638, 293, 550, 613, 366, 1333, 295, 264, 2372, 51776], "temperature": 0.0, "avg_logprob":
  -0.15696475575271163, "compression_ratio": 1.7020408163265306, "no_speech_prob":
  0.001121428911574185}, {"id": 825, "seek": 264338, "start": 2643.5, "end": 2645.2200000000003,
  "text": " to which they like those items.", "tokens": [50370, 281, 597, 436, 411,
  729, 4754, 13, 50456], "temperature": 0.0, "avg_logprob": -0.15000835748819205,
  "compression_ratio": 1.7330827067669172, "no_speech_prob": 0.0006736969808116555},
  {"id": 826, "seek": 264338, "start": 2645.2200000000003, "end": 2648.62, "text":
  " We can derive this based upon just their querian click patterns.", "tokens": [50456,
  492, 393, 28446, 341, 2361, 3564, 445, 641, 7083, 952, 2052, 8294, 13, 50626], "temperature":
  0.0, "avg_logprob": -0.15000835748819205, "compression_ratio": 1.7330827067669172,
  "no_speech_prob": 0.0006736969808116555}, {"id": 827, "seek": 264338, "start": 2650.26,
  "end": 2652.42, "text": " The intermediate step for collaborative filtering", "tokens":
  [50708, 440, 19376, 1823, 337, 16555, 30822, 50816], "temperature": 0.0, "avg_logprob":
  -0.15000835748819205, "compression_ratio": 1.7330827067669172, "no_speech_prob":
  0.0006736969808116555}, {"id": 828, "seek": 264338, "start": 2652.42, "end": 2654.1800000000003,
  "text": " is matrix factorization,", "tokens": [50816, 307, 8141, 5952, 2144, 11,
  50904], "temperature": 0.0, "avg_logprob": -0.15000835748819205, "compression_ratio":
  1.7330827067669172, "no_speech_prob": 0.0006736969808116555}, {"id": 829, "seek":
  264338, "start": 2654.1800000000003, "end": 2658.58, "text": " which is taking this
  underlying user item interaction matrix", "tokens": [50904, 597, 307, 1940, 341,
  14217, 4195, 3174, 9285, 8141, 51124], "temperature": 0.0, "avg_logprob": -0.15000835748819205,
  "compression_ratio": 1.7330827067669172, "no_speech_prob": 0.0006736969808116555},
  {"id": 830, "seek": 264338, "start": 2658.58, "end": 2661.38, "text": " and trying
  to break it into two different matrices.", "tokens": [51124, 293, 1382, 281, 1821,
  309, 666, 732, 819, 32284, 13, 51264], "temperature": 0.0, "avg_logprob": -0.15000835748819205,
  "compression_ratio": 1.7330827067669172, "no_speech_prob": 0.0006736969808116555},
  {"id": 831, "seek": 264338, "start": 2661.38, "end": 2664.9, "text": " This user
  feature matrix and this item feature matrix.", "tokens": [51264, 639, 4195, 4111,
  8141, 293, 341, 3174, 4111, 8141, 13, 51440], "temperature": 0.0, "avg_logprob":
  -0.15000835748819205, "compression_ratio": 1.7330827067669172, "no_speech_prob":
  0.0006736969808116555}, {"id": 832, "seek": 264338, "start": 2664.9, "end": 2669.1800000000003,
  "text": " And the idea is that if I can generate a set of latent values", "tokens":
  [51440, 400, 264, 1558, 307, 300, 498, 286, 393, 8460, 257, 992, 295, 48994, 4190,
  51654], "temperature": 0.0, "avg_logprob": -0.15000835748819205, "compression_ratio":
  1.7330827067669172, "no_speech_prob": 0.0006736969808116555}, {"id": 833, "seek":
  264338, "start": 2669.1800000000003, "end": 2671.98, "text": " associated with this
  user across some number of dimensions,", "tokens": [51654, 6615, 365, 341, 4195,
  2108, 512, 1230, 295, 12819, 11, 51794], "temperature": 0.0, "avg_logprob": -0.15000835748819205,
  "compression_ratio": 1.7330827067669172, "no_speech_prob": 0.0006736969808116555},
  {"id": 834, "seek": 267198, "start": 2671.98, "end": 2673.7400000000002, "text":
  " I''m only showing three here visually,", "tokens": [50364, 286, 478, 787, 4099,
  1045, 510, 19622, 11, 50452], "temperature": 0.0, "avg_logprob": -0.10863017234481684,
  "compression_ratio": 1.7865612648221343, "no_speech_prob": 0.0004396222939249128},
  {"id": 835, "seek": 267198, "start": 2673.7400000000002, "end": 2676.7400000000002,
  "text": " because it''s a PowerPoint slide, but there''ll be more.", "tokens": [50452,
  570, 309, 311, 257, 25584, 4137, 11, 457, 456, 603, 312, 544, 13, 50602], "temperature":
  0.0, "avg_logprob": -0.10863017234481684, "compression_ratio": 1.7865612648221343,
  "no_speech_prob": 0.0004396222939249128}, {"id": 836, "seek": 267198, "start": 2676.7400000000002,
  "end": 2680.14, "text": " And if I have the same latent dimensions", "tokens": [50602,
  400, 498, 286, 362, 264, 912, 48994, 12819, 50772], "temperature": 0.0, "avg_logprob":
  -0.10863017234481684, "compression_ratio": 1.7865612648221343, "no_speech_prob":
  0.0004396222939249128}, {"id": 837, "seek": 267198, "start": 2680.14, "end": 2681.7400000000002,
  "text": " over here for the items,", "tokens": [50772, 670, 510, 337, 264, 4754,
  11, 50852], "temperature": 0.0, "avg_logprob": -0.10863017234481684, "compression_ratio":
  1.7865612648221343, "no_speech_prob": 0.0004396222939249128}, {"id": 838, "seek":
  267198, "start": 2681.7400000000002, "end": 2683.98, "text": " when I multiply a
  particular user", "tokens": [50852, 562, 286, 12972, 257, 1729, 4195, 50964], "temperature":
  0.0, "avg_logprob": -0.10863017234481684, "compression_ratio": 1.7865612648221343,
  "no_speech_prob": 0.0004396222939249128}, {"id": 839, "seek": 267198, "start": 2683.98,
  "end": 2688.98, "text": " and their particular values associated", "tokens": [50964,
  293, 641, 1729, 4190, 6615, 51214], "temperature": 0.0, "avg_logprob": -0.10863017234481684,
  "compression_ratio": 1.7865612648221343, "no_speech_prob": 0.0004396222939249128},
  {"id": 840, "seek": 267198, "start": 2688.98, "end": 2691.7, "text": " with these
  latent dimensions with the movie,", "tokens": [51214, 365, 613, 48994, 12819, 365,
  264, 3169, 11, 51350], "temperature": 0.0, "avg_logprob": -0.10863017234481684,
  "compression_ratio": 1.7865612648221343, "no_speech_prob": 0.0004396222939249128},
  {"id": 841, "seek": 267198, "start": 2691.7, "end": 2694.42, "text": " then I''m
  pulling apart how much of this belongs to the movie", "tokens": [51350, 550, 286,
  478, 8407, 4936, 577, 709, 295, 341, 12953, 281, 264, 3169, 51486], "temperature":
  0.0, "avg_logprob": -0.10863017234481684, "compression_ratio": 1.7865612648221343,
  "no_speech_prob": 0.0004396222939249128}, {"id": 842, "seek": 267198, "start": 2694.42,
  "end": 2695.86, "text": " and how much of this belongs to the user", "tokens": [51486,
  293, 577, 709, 295, 341, 12953, 281, 264, 4195, 51558], "temperature": 0.0, "avg_logprob":
  -0.10863017234481684, "compression_ratio": 1.7865612648221343, "no_speech_prob":
  0.0004396222939249128}, {"id": 843, "seek": 267198, "start": 2695.86, "end": 2697.34,
  "text": " in terms of an interest.", "tokens": [51558, 294, 2115, 295, 364, 1179,
  13, 51632], "temperature": 0.0, "avg_logprob": -0.10863017234481684, "compression_ratio":
  1.7865612648221343, "no_speech_prob": 0.0004396222939249128}, {"id": 844, "seek":
  267198, "start": 2697.34, "end": 2699.34, "text": " But at the end of the day, these
  are embeddings.", "tokens": [51632, 583, 412, 264, 917, 295, 264, 786, 11, 613,
  366, 12240, 29432, 13, 51732], "temperature": 0.0, "avg_logprob": -0.10863017234481684,
  "compression_ratio": 1.7865612648221343, "no_speech_prob": 0.0004396222939249128},
  {"id": 845, "seek": 269934, "start": 2699.34, "end": 2702.78, "text": " This is
  a user embedding and this is an item embedding.", "tokens": [50364, 639, 307, 257,
  4195, 12240, 3584, 293, 341, 307, 364, 3174, 12240, 3584, 13, 50536], "temperature":
  0.0, "avg_logprob": -0.11654238547048261, "compression_ratio": 1.8694029850746268,
  "no_speech_prob": 0.00016376233543269336}, {"id": 846, "seek": 269934, "start":
  2702.78, "end": 2704.7000000000003, "text": " What that means is that,", "tokens":
  [50536, 708, 300, 1355, 307, 300, 11, 50632], "temperature": 0.0, "avg_logprob":
  -0.11654238547048261, "compression_ratio": 1.8694029850746268, "no_speech_prob":
  0.00016376233543269336}, {"id": 847, "seek": 269934, "start": 2704.7000000000003,
  "end": 2707.6600000000003, "text": " and this is just how it works to do collaborative
  filtering", "tokens": [50632, 293, 341, 307, 445, 577, 309, 1985, 281, 360, 16555,
  30822, 50780], "temperature": 0.0, "avg_logprob": -0.11654238547048261, "compression_ratio":
  1.8694029850746268, "no_speech_prob": 0.00016376233543269336}, {"id": 848, "seek":
  269934, "start": 2707.6600000000003, "end": 2710.46, "text": " and actually generate
  recommendations for particular items,", "tokens": [50780, 293, 767, 8460, 10434,
  337, 1729, 4754, 11, 50920], "temperature": 0.0, "avg_logprob": -0.11654238547048261,
  "compression_ratio": 1.8694029850746268, "no_speech_prob": 0.00016376233543269336},
  {"id": 849, "seek": 269934, "start": 2710.46, "end": 2712.2200000000003, "text":
  " not particularly useful for today.", "tokens": [50920, 406, 4098, 4420, 337, 965,
  13, 51008], "temperature": 0.0, "avg_logprob": -0.11654238547048261, "compression_ratio":
  1.8694029850746268, "no_speech_prob": 0.00016376233543269336}, {"id": 850, "seek":
  269934, "start": 2712.2200000000003, "end": 2716.58, "text": " But what I can do
  is I can generate these latent embeddings", "tokens": [51008, 583, 437, 286, 393,
  360, 307, 286, 393, 8460, 613, 48994, 12240, 29432, 51226], "temperature": 0.0,
  "avg_logprob": -0.11654238547048261, "compression_ratio": 1.8694029850746268, "no_speech_prob":
  0.00016376233543269336}, {"id": 851, "seek": 269934, "start": 2716.58, "end": 2718.3,
  "text": " and these essentially allow me to create", "tokens": [51226, 293, 613,
  4476, 2089, 385, 281, 1884, 51312], "temperature": 0.0, "avg_logprob": -0.11654238547048261,
  "compression_ratio": 1.8694029850746268, "no_speech_prob": 0.00016376233543269336},
  {"id": 852, "seek": 269934, "start": 2718.3, "end": 2721.9, "text": " a behavioral
  embedding space for my items.", "tokens": [51312, 257, 19124, 12240, 3584, 1901,
  337, 452, 4754, 13, 51492], "temperature": 0.0, "avg_logprob": -0.11654238547048261,
  "compression_ratio": 1.8694029850746268, "no_speech_prob": 0.00016376233543269336},
  {"id": 853, "seek": 269934, "start": 2721.9, "end": 2723.06, "text": " So once I''ve
  done that,", "tokens": [51492, 407, 1564, 286, 600, 1096, 300, 11, 51550], "temperature":
  0.0, "avg_logprob": -0.11654238547048261, "compression_ratio": 1.8694029850746268,
  "no_speech_prob": 0.00016376233543269336}, {"id": 854, "seek": 269934, "start":
  2723.06, "end": 2725.7000000000003, "text": " I can add these behavioral embeddings
  onto documents", "tokens": [51550, 286, 393, 909, 613, 19124, 12240, 29432, 3911,
  8512, 51682], "temperature": 0.0, "avg_logprob": -0.11654238547048261, "compression_ratio":
  1.8694029850746268, "no_speech_prob": 0.00016376233543269336}, {"id": 855, "seek":
  269934, "start": 2725.7000000000003, "end": 2728.94, "text": " just like I do with
  content-based embeddings", "tokens": [51682, 445, 411, 286, 360, 365, 2701, 12,
  6032, 12240, 29432, 51844], "temperature": 0.0, "avg_logprob": -0.11654238547048261,
  "compression_ratio": 1.8694029850746268, "no_speech_prob": 0.00016376233543269336},
  {"id": 856, "seek": 272894, "start": 2728.94, "end": 2731.38, "text": " or whether
  it''s images or text or what have you,", "tokens": [50364, 420, 1968, 309, 311,
  5267, 420, 2487, 420, 437, 362, 291, 11, 50486], "temperature": 0.0, "avg_logprob":
  -0.20460670535303965, "compression_ratio": 1.5326460481099657, "no_speech_prob":
  6.502851465484127e-05}, {"id": 857, "seek": 272894, "start": 2731.38, "end": 2735.62,
  "text": " and then leverage those as a behavioral space.", "tokens": [50486, 293,
  550, 13982, 729, 382, 257, 19124, 1901, 13, 50698], "temperature": 0.0, "avg_logprob":
  -0.20460670535303965, "compression_ratio": 1.5326460481099657, "no_speech_prob":
  6.502851465484127e-05}, {"id": 858, "seek": 272894, "start": 2735.62, "end": 2738.62,
  "text": " So we do this commonly with personalized search,", "tokens": [50698, 407,
  321, 360, 341, 12719, 365, 28415, 3164, 11, 50848], "temperature": 0.0, "avg_logprob":
  -0.20460670535303965, "compression_ratio": 1.5326460481099657, "no_speech_prob":
  6.502851465484127e-05}, {"id": 859, "seek": 272894, "start": 2738.62, "end": 2740.7000000000003,
  "text": " for example, we''ll go through this in the course.", "tokens": [50848,
  337, 1365, 11, 321, 603, 352, 807, 341, 294, 264, 1164, 13, 50952], "temperature":
  0.0, "avg_logprob": -0.20460670535303965, "compression_ratio": 1.5326460481099657,
  "no_speech_prob": 6.502851465484127e-05}, {"id": 860, "seek": 272894, "start": 2740.7000000000003,
  "end": 2743.86, "text": " But if I have a person who previously searched", "tokens":
  [50952, 583, 498, 286, 362, 257, 954, 567, 8046, 22961, 51110], "temperature": 0.0,
  "avg_logprob": -0.20460670535303965, "compression_ratio": 1.5326460481099657, "no_speech_prob":
  6.502851465484127e-05}, {"id": 861, "seek": 272894, "start": 2743.86, "end": 2747.54,
  "text": " for Hello Kitty Plus toy, GE Electric Razor,", "tokens": [51110, 337,
  2425, 36393, 7721, 12058, 11, 18003, 24677, 29051, 284, 11, 51294], "temperature":
  0.0, "avg_logprob": -0.20460670535303965, "compression_ratio": 1.5326460481099657,
  "no_speech_prob": 6.502851465484127e-05}, {"id": 862, "seek": 272894, "start": 2747.54,
  "end": 2749.26, "text": " GE Bright White Lightbulbs,", "tokens": [51294, 18003,
  24271, 5552, 8279, 12176, 929, 11, 51380], "temperature": 0.0, "avg_logprob": -0.20460670535303965,
  "compression_ratio": 1.5326460481099657, "no_speech_prob": 6.502851465484127e-05},
  {"id": 863, "seek": 272894, "start": 2749.26, "end": 2751.82, "text": " Samsung
  Stainless Steel refrigerator,", "tokens": [51380, 13173, 745, 491, 1832, 26038,
  19655, 11, 51508], "temperature": 0.0, "avg_logprob": -0.20460670535303965, "compression_ratio":
  1.5326460481099657, "no_speech_prob": 6.502851465484127e-05}, {"id": 864, "seek":
  272894, "start": 2751.82, "end": 2753.86, "text": " I can take a normal query,",
  "tokens": [51508, 286, 393, 747, 257, 2710, 14581, 11, 51610], "temperature": 0.0,
  "avg_logprob": -0.20460670535303965, "compression_ratio": 1.5326460481099657, "no_speech_prob":
  6.502851465484127e-05}, {"id": 865, "seek": 272894, "start": 2753.86, "end": 2755.38,
  "text": " keyword query for microwave,", "tokens": [51610, 20428, 14581, 337, 19025,
  11, 51686], "temperature": 0.0, "avg_logprob": -0.20460670535303965, "compression_ratio":
  1.5326460481099657, "no_speech_prob": 6.502851465484127e-05}, {"id": 866, "seek":
  272894, "start": 2755.38, "end": 2757.38, "text": " which just returns random microwaves.",
  "tokens": [51686, 597, 445, 11247, 4974, 17177, 5423, 13, 51786], "temperature":
  0.0, "avg_logprob": -0.20460670535303965, "compression_ratio": 1.5326460481099657,
  "no_speech_prob": 6.502851465484127e-05}, {"id": 867, "seek": 275738, "start": 2758.34,
  "end": 2763.06, "text": " If I use these vectors improperly with no guardrails,",
  "tokens": [50412, 759, 286, 764, 613, 18875, 40651, 356, 365, 572, 6290, 424, 4174,
  11, 50648], "temperature": 0.0, "avg_logprob": -0.15857930481433868, "compression_ratio":
  1.723021582733813, "no_speech_prob": 0.002244642935693264}, {"id": 868, "seek":
  275738, "start": 2763.06, "end": 2766.1800000000003, "text": " I might do things
  like blur the lines between categories.", "tokens": [50648, 286, 1062, 360, 721,
  411, 14257, 264, 3876, 1296, 10479, 13, 50804], "temperature": 0.0, "avg_logprob":
  -0.15857930481433868, "compression_ratio": 1.723021582733813, "no_speech_prob":
  0.002244642935693264}, {"id": 869, "seek": 275738, "start": 2766.1800000000003,
  "end": 2768.46, "text": " Most people, if they''ve searched for a Samsung Stainless",
  "tokens": [50804, 4534, 561, 11, 498, 436, 600, 22961, 337, 257, 13173, 745, 491,
  1832, 50918], "temperature": 0.0, "avg_logprob": -0.15857930481433868, "compression_ratio":
  1.723021582733813, "no_speech_prob": 0.002244642935693264}, {"id": 870, "seek":
  275738, "start": 2768.46, "end": 2769.86, "text": " Steel refrigerator,", "tokens":
  [50918, 26038, 19655, 11, 50988], "temperature": 0.0, "avg_logprob": -0.15857930481433868,
  "compression_ratio": 1.723021582733813, "no_speech_prob": 0.002244642935693264},
  {"id": 871, "seek": 275738, "start": 2769.86, "end": 2773.34, "text": " the best
  result here would be a Samsung Stainless Steel microwave.", "tokens": [50988, 264,
  1151, 1874, 510, 576, 312, 257, 13173, 745, 491, 1832, 26038, 19025, 13, 51162],
  "temperature": 0.0, "avg_logprob": -0.15857930481433868, "compression_ratio": 1.723021582733813,
  "no_speech_prob": 0.002244642935693264}, {"id": 872, "seek": 275738, "start": 2773.34,
  "end": 2774.9, "text": " But if you do this wrong,", "tokens": [51162, 583, 498,
  291, 360, 341, 2085, 11, 51240], "temperature": 0.0, "avg_logprob": -0.15857930481433868,
  "compression_ratio": 1.723021582733813, "no_speech_prob": 0.002244642935693264},
  {"id": 873, "seek": 275738, "start": 2774.9, "end": 2776.7400000000002, "text":
  " the sort of naive approach is,", "tokens": [51240, 264, 1333, 295, 29052, 3109,
  307, 11, 51332], "temperature": 0.0, "avg_logprob": -0.15857930481433868, "compression_ratio":
  1.723021582733813, "no_speech_prob": 0.002244642935693264}, {"id": 874, "seek":
  275738, "start": 2776.7400000000002, "end": 2778.42, "text": " I might end up with
  a Hello Kitty microwave", "tokens": [51332, 286, 1062, 917, 493, 365, 257, 2425,
  36393, 19025, 51416], "temperature": 0.0, "avg_logprob": -0.15857930481433868, "compression_ratio":
  1.723021582733813, "no_speech_prob": 0.002244642935693264}, {"id": 875, "seek":
  275738, "start": 2778.42, "end": 2782.7000000000003, "text": " or a Panasonic microwave,
  or not Panasonic,", "tokens": [51416, 420, 257, 7557, 39460, 19025, 11, 420, 406,
  7557, 39460, 11, 51630], "temperature": 0.0, "avg_logprob": -0.15857930481433868,
  "compression_ratio": 1.723021582733813, "no_speech_prob": 0.002244642935693264},
  {"id": 876, "seek": 275738, "start": 2782.7000000000003, "end": 2784.2200000000003,
  "text": " but I might end up with things", "tokens": [51630, 457, 286, 1062, 917,
  493, 365, 721, 51706], "temperature": 0.0, "avg_logprob": -0.15857930481433868,
  "compression_ratio": 1.723021582733813, "no_speech_prob": 0.002244642935693264},
  {"id": 877, "seek": 275738, "start": 2784.2200000000003, "end": 2786.5, "text":
  " that don''t exactly match all of the preferences", "tokens": [51706, 300, 500,
  380, 2293, 2995, 439, 295, 264, 21910, 51820], "temperature": 0.0, "avg_logprob":
  -0.15857930481433868, "compression_ratio": 1.723021582733813, "no_speech_prob":
  0.002244642935693264}, {"id": 878, "seek": 278650, "start": 2786.78, "end": 2789.06,
  "text": " of the category, again, for another day.", "tokens": [50378, 295, 264,
  7719, 11, 797, 11, 337, 1071, 786, 13, 50492], "temperature": 0.0, "avg_logprob":
  -0.15876143833376327, "compression_ratio": 1.62109375, "no_speech_prob": 0.00041343827615492046},
  {"id": 879, "seek": 278650, "start": 2789.06, "end": 2791.62, "text": " But this
  is how a behavioral vector space would typically", "tokens": [50492, 583, 341, 307,
  577, 257, 19124, 8062, 1901, 576, 5850, 50620], "temperature": 0.0, "avg_logprob":
  -0.15876143833376327, "compression_ratio": 1.62109375, "no_speech_prob": 0.00041343827615492046},
  {"id": 880, "seek": 278650, "start": 2791.62, "end": 2793.3, "text": " be used.",
  "tokens": [50620, 312, 1143, 13, 50704], "temperature": 0.0, "avg_logprob": -0.15876143833376327,
  "compression_ratio": 1.62109375, "no_speech_prob": 0.00041343827615492046}, {"id":
  881, "seek": 278650, "start": 2793.3, "end": 2796.42, "text": " But ultimately,
  there''s a lot of tips and tricks", "tokens": [50704, 583, 6284, 11, 456, 311, 257,
  688, 295, 6082, 293, 11733, 50860], "temperature": 0.0, "avg_logprob": -0.15876143833376327,
  "compression_ratio": 1.62109375, "no_speech_prob": 0.00041343827615492046}, {"id":
  882, "seek": 278650, "start": 2796.42, "end": 2798.74, "text": " you can use to
  do AI-powered search", "tokens": [50860, 291, 393, 764, 281, 360, 7318, 12, 27178,
  3164, 50976], "temperature": 0.0, "avg_logprob": -0.15876143833376327, "compression_ratio":
  1.62109375, "no_speech_prob": 0.00041343827615492046}, {"id": 883, "seek": 278650,
  "start": 2798.74, "end": 2801.66, "text": " to combine all of these different techniques",
  "tokens": [50976, 281, 10432, 439, 295, 613, 819, 7512, 51122], "temperature": 0.0,
  "avg_logprob": -0.15876143833376327, "compression_ratio": 1.62109375, "no_speech_prob":
  0.00041343827615492046}, {"id": 884, "seek": 278650, "start": 2801.66, "end": 2803.82,
  "text": " that you might use to run searches", "tokens": [51122, 300, 291, 1062,
  764, 281, 1190, 26701, 51230], "temperature": 0.0, "avg_logprob": -0.15876143833376327,
  "compression_ratio": 1.62109375, "no_speech_prob": 0.00041343827615492046}, {"id":
  885, "seek": 278650, "start": 2803.82, "end": 2806.3, "text": " and to query understanding
  of relevance", "tokens": [51230, 293, 281, 14581, 3701, 295, 32684, 51354], "temperature":
  0.0, "avg_logprob": -0.15876143833376327, "compression_ratio": 1.62109375, "no_speech_prob":
  0.00041343827615492046}, {"id": 886, "seek": 278650, "start": 2806.3, "end": 2809.3,
  "text": " and sort of integrate wormhole vectors in various places.", "tokens":
  [51354, 293, 1333, 295, 13365, 23835, 14094, 18875, 294, 3683, 3190, 13, 51504],
  "temperature": 0.0, "avg_logprob": -0.15876143833376327, "compression_ratio": 1.62109375,
  "no_speech_prob": 0.00041343827615492046}, {"id": 887, "seek": 278650, "start":
  2809.3, "end": 2812.3, "text": " So there''s lots of different query paradigms",
  "tokens": [51504, 407, 456, 311, 3195, 295, 819, 14581, 13480, 328, 2592, 51654],
  "temperature": 0.0, "avg_logprob": -0.15876143833376327, "compression_ratio": 1.62109375,
  "no_speech_prob": 0.00041343827615492046}, {"id": 888, "seek": 281230, "start":
  2812.3, "end": 2816.6200000000003, "text": " to experiment with, to merge using
  wormhole vectors.", "tokens": [50364, 281, 5120, 365, 11, 281, 22183, 1228, 23835,
  14094, 18875, 13, 50580], "temperature": 0.0, "avg_logprob": -0.13896166376706934,
  "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143}, {"id": 889,
  "seek": 281230, "start": 2816.6200000000003, "end": 2818.78, "text": " But that''s
  the general idea.", "tokens": [50580, 583, 300, 311, 264, 2674, 1558, 13, 50688],
  "temperature": 0.0, "avg_logprob": -0.13896166376706934, "compression_ratio": 1.75,
  "no_speech_prob": 0.0018121888861060143}, {"id": 890, "seek": 281230, "start": 2818.78,
  "end": 2820.26, "text": " I wanted to kind of introduce today", "tokens": [50688,
  286, 1415, 281, 733, 295, 5366, 965, 50762], "temperature": 0.0, "avg_logprob":
  -0.13896166376706934, "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143},
  {"id": 891, "seek": 281230, "start": 2820.26, "end": 2823.1800000000003, "text":
  " to get the discussion going about going", "tokens": [50762, 281, 483, 264, 5017,
  516, 466, 516, 50908], "temperature": 0.0, "avg_logprob": -0.13896166376706934,
  "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143}, {"id": 892,
  "seek": 281230, "start": 2823.1800000000003, "end": 2825.3, "text": " from thinking
  of these vector spaces", "tokens": [50908, 490, 1953, 295, 613, 8062, 7673, 51014],
  "temperature": 0.0, "avg_logprob": -0.13896166376706934, "compression_ratio": 1.75,
  "no_speech_prob": 0.0018121888861060143}, {"id": 893, "seek": 281230, "start": 2825.3,
  "end": 2827.1400000000003, "text": " as entirely sort of orthogonal,", "tokens":
  [51014, 382, 7696, 1333, 295, 41488, 11, 51106], "temperature": 0.0, "avg_logprob":
  -0.13896166376706934, "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143},
  {"id": 894, "seek": 281230, "start": 2827.1400000000003, "end": 2828.7000000000003,
  "text": " where I have to query them separately,", "tokens": [51106, 689, 286, 362,
  281, 14581, 552, 14759, 11, 51184], "temperature": 0.0, "avg_logprob": -0.13896166376706934,
  "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143}, {"id": 895,
  "seek": 281230, "start": 2828.7000000000003, "end": 2830.9, "text": " or maybe I
  could even query them in the same query,", "tokens": [51184, 420, 1310, 286, 727,
  754, 14581, 552, 294, 264, 912, 14581, 11, 51294], "temperature": 0.0, "avg_logprob":
  -0.13896166376706934, "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143},
  {"id": 896, "seek": 281230, "start": 2830.9, "end": 2833.0600000000004, "text":
  " but I''m filtering on them separately,", "tokens": [51294, 457, 286, 478, 30822,
  322, 552, 14759, 11, 51402], "temperature": 0.0, "avg_logprob": -0.13896166376706934,
  "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143}, {"id": 897,
  "seek": 281230, "start": 2833.0600000000004, "end": 2836.46, "text": " to trying
  to actually pull out the semantic understanding", "tokens": [51402, 281, 1382, 281,
  767, 2235, 484, 264, 47982, 3701, 51572], "temperature": 0.0, "avg_logprob": -0.13896166376706934,
  "compression_ratio": 1.75, "no_speech_prob": 0.0018121888861060143}, {"id": 898,
  "seek": 281230, "start": 2836.46, "end": 2840.78, "text": " from one vector space
  and use that to craft a sort of wormhole", "tokens": [51572, 490, 472, 8062, 1901,
  293, 764, 300, 281, 8448, 257, 1333, 295, 23835, 14094, 51788], "temperature": 0.0,
  "avg_logprob": -0.13896166376706934, "compression_ratio": 1.75, "no_speech_prob":
  0.0018121888861060143}, {"id": 899, "seek": 284078, "start": 2840.78, "end": 2842.98,
  "text": " or hopping off point to another vector space", "tokens": [50364, 420,
  47199, 766, 935, 281, 1071, 8062, 1901, 50474], "temperature": 0.0, "avg_logprob":
  -0.19012510272818553, "compression_ratio": 1.6539682539682539, "no_speech_prob":
  0.0009992808336392045}, {"id": 900, "seek": 284078, "start": 2842.98, "end": 2845.3,
  "text": " to sort of continue to explore leveraging", "tokens": [50474, 281, 1333,
  295, 2354, 281, 6839, 32666, 50590], "temperature": 0.0, "avg_logprob": -0.19012510272818553,
  "compression_ratio": 1.6539682539682539, "no_speech_prob": 0.0009992808336392045},
  {"id": 901, "seek": 284078, "start": 2845.3, "end": 2846.6200000000003, "text":
  " a different query paradigm.", "tokens": [50590, 257, 819, 14581, 24709, 13, 50656],
  "temperature": 0.0, "avg_logprob": -0.19012510272818553, "compression_ratio": 1.6539682539682539,
  "no_speech_prob": 0.0009992808336392045}, {"id": 902, "seek": 284078, "start": 2846.6200000000003,
  "end": 2850.98, "text": " So that''s pretty much it for the talk for today.", "tokens":
  [50656, 407, 300, 311, 1238, 709, 309, 337, 264, 751, 337, 965, 13, 50874], "temperature":
  0.0, "avg_logprob": -0.19012510272818553, "compression_ratio": 1.6539682539682539,
  "no_speech_prob": 0.0009992808336392045}, {"id": 903, "seek": 284078, "start": 2850.98,
  "end": 2854.5400000000004, "text": " Dima, Dmitry, I don''t know if you want to
  start", "tokens": [50874, 413, 4775, 11, 413, 3508, 627, 11, 286, 500, 380, 458,
  498, 291, 528, 281, 722, 51052], "temperature": 0.0, "avg_logprob": -0.19012510272818553,
  "compression_ratio": 1.6539682539682539, "no_speech_prob": 0.0009992808336392045},
  {"id": 904, "seek": 284078, "start": 2854.5400000000004, "end": 2856.2200000000003,
  "text": " to dive in some questions.", "tokens": [51052, 281, 9192, 294, 512, 1651,
  13, 51136], "temperature": 0.0, "avg_logprob": -0.19012510272818553, "compression_ratio":
  1.6539682539682539, "no_speech_prob": 0.0009992808336392045}, {"id": 905, "seek":
  284078, "start": 2856.2200000000003, "end": 2858.9, "text": " I know some people
  will have to hop off at the top of the hour", "tokens": [51136, 286, 458, 512, 561,
  486, 362, 281, 3818, 766, 412, 264, 1192, 295, 264, 1773, 51270], "temperature":
  0.0, "avg_logprob": -0.19012510272818553, "compression_ratio": 1.6539682539682539,
  "no_speech_prob": 0.0009992808336392045}, {"id": 906, "seek": 284078, "start": 2858.9,
  "end": 2860.3, "text": " because this is scheduled for an hour,", "tokens": [51270,
  570, 341, 307, 15678, 337, 364, 1773, 11, 51340], "temperature": 0.0, "avg_logprob":
  -0.19012510272818553, "compression_ratio": 1.6539682539682539, "no_speech_prob":
  0.0009992808336392045}, {"id": 907, "seek": 284078, "start": 2860.3, "end": 2862.5,
  "text": " but I''m also happy to just kind of keep going", "tokens": [51340, 457,
  286, 478, 611, 2055, 281, 445, 733, 295, 1066, 516, 51450], "temperature": 0.0,
  "avg_logprob": -0.19012510272818553, "compression_ratio": 1.6539682539682539, "no_speech_prob":
  0.0009992808336392045}, {"id": 908, "seek": 284078, "start": 2862.5, "end": 2864.78,
  "text": " with questions a little bit after", "tokens": [51450, 365, 1651, 257,
  707, 857, 934, 51564], "temperature": 0.0, "avg_logprob": -0.19012510272818553,
  "compression_ratio": 1.6539682539682539, "no_speech_prob": 0.0009992808336392045},
  {"id": 909, "seek": 284078, "start": 2864.78, "end": 2866.78, "text": " if it makes
  sense and people can drop off when they want.", "tokens": [51564, 498, 309, 1669,
  2020, 293, 561, 393, 3270, 766, 562, 436, 528, 13, 51664], "temperature": 0.0, "avg_logprob":
  -0.19012510272818553, "compression_ratio": 1.6539682539682539, "no_speech_prob":
  0.0009992808336392045}, {"id": 910, "seek": 284078, "start": 2866.78, "end": 2869.26,
  "text": " But let''s maybe dive into some discussion.", "tokens": [51664, 583, 718,
  311, 1310, 9192, 666, 512, 5017, 13, 51788], "temperature": 0.0, "avg_logprob":
  -0.19012510272818553, "compression_ratio": 1.6539682539682539, "no_speech_prob":
  0.0009992808336392045}, {"id": 911, "seek": 286926, "start": 2869.26, "end": 2870.94,
  "text": " Yeah, we have a bunch of questions.", "tokens": [50364, 865, 11, 321,
  362, 257, 3840, 295, 1651, 13, 50448], "temperature": 0.0, "avg_logprob": -0.26576798050491895,
  "compression_ratio": 1.6063829787234043, "no_speech_prob": 0.009843863546848297},
  {"id": 912, "seek": 286926, "start": 2870.94, "end": 2872.26, "text": " Thanks,
  Tray, a bunch.", "tokens": [50448, 2561, 11, 1765, 320, 11, 257, 3840, 13, 50514],
  "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 913, "seek": 286926, "start": 2872.26,
  "end": 2873.94, "text": " This is fantastic topic.", "tokens": [50514, 639, 307,
  5456, 4829, 13, 50598], "temperature": 0.0, "avg_logprob": -0.26576798050491895,
  "compression_ratio": 1.6063829787234043, "no_speech_prob": 0.009843863546848297},
  {"id": 914, "seek": 286926, "start": 2873.94, "end": 2876.86, "text": " I just recently
  traveled to Texas from Finland", "tokens": [50598, 286, 445, 3938, 16147, 281, 7885,
  490, 24869, 50744], "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio":
  1.6063829787234043, "no_speech_prob": 0.009843863546848297}, {"id": 915, "seek":
  286926, "start": 2876.86, "end": 2878.7000000000003, "text": " and it took me like
  12 hours.", "tokens": [50744, 293, 309, 1890, 385, 411, 2272, 2496, 13, 50836],
  "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 916, "seek": 286926, "start": 2878.7000000000003,
  "end": 2881.78, "text": " I wish there was a wormhole jump through points", "tokens":
  [50836, 286, 3172, 456, 390, 257, 23835, 14094, 3012, 807, 2793, 50990], "temperature":
  0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 917, "seek": 286926, "start": 2881.78,
  "end": 2884.2200000000003, "text": " so I could just end up there much quicker.",
  "tokens": [50990, 370, 286, 727, 445, 917, 493, 456, 709, 16255, 13, 51112], "temperature":
  0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 918, "seek": 286926, "start": 2884.2200000000003,
  "end": 2885.46, "text": " There''d be all of them.", "tokens": [51112, 821, 1116,
  312, 439, 295, 552, 13, 51174], "temperature": 0.0, "avg_logprob": -0.26576798050491895,
  "compression_ratio": 1.6063829787234043, "no_speech_prob": 0.009843863546848297},
  {"id": 919, "seek": 286926, "start": 2885.46, "end": 2887.5800000000004, "text":
  " We have so many questions, man.", "tokens": [51174, 492, 362, 370, 867, 1651,
  11, 587, 13, 51280], "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio":
  1.6063829787234043, "no_speech_prob": 0.009843863546848297}, {"id": 920, "seek":
  286926, "start": 2888.5800000000004, "end": 2892.5400000000004, "text": " So I''ll
  defer my questions off and I''ll just jump.", "tokens": [51330, 407, 286, 603, 25704,
  452, 1651, 766, 293, 286, 603, 445, 3012, 13, 51528], "temperature": 0.0, "avg_logprob":
  -0.26576798050491895, "compression_ratio": 1.6063829787234043, "no_speech_prob":
  0.009843863546848297}, {"id": 921, "seek": 286926, "start": 2892.5400000000004,
  "end": 2895.6200000000003, "text": " There is one logistic question from Ardune.",
  "tokens": [51528, 821, 307, 472, 3565, 3142, 1168, 490, 1587, 67, 2613, 13, 51682],
  "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 922, "seek": 286926, "start": 2895.6200000000003,
  "end": 2898.5, "text": " I hope I pronounced you name correctly, I''m sorry.", "tokens":
  [51682, 286, 1454, 286, 23155, 291, 1315, 8944, 11, 286, 478, 2597, 13, 51826],
  "temperature": 0.0, "avg_logprob": -0.26576798050491895, "compression_ratio": 1.6063829787234043,
  "no_speech_prob": 0.009843863546848297}, {"id": 923, "seek": 289850, "start": 2898.5,
  "end": 2901.3, "text": " How''s the course different from the AI Powered Search
  book?", "tokens": [50364, 1012, 311, 264, 1164, 819, 490, 264, 7318, 7086, 292,
  17180, 1446, 30, 50504], "temperature": 0.0, "avg_logprob": -0.23608602134926807,
  "compression_ratio": 1.5289256198347108, "no_speech_prob": 0.03237403929233551},
  {"id": 924, "seek": 289850, "start": 2901.3, "end": 2905.86, "text": " And then
  later is this topic wormhole vectors", "tokens": [50504, 400, 550, 1780, 307, 341,
  4829, 23835, 14094, 18875, 50732], "temperature": 0.0, "avg_logprob": -0.23608602134926807,
  "compression_ratio": 1.5289256198347108, "no_speech_prob": 0.03237403929233551},
  {"id": 925, "seek": 289850, "start": 2905.86, "end": 2908.22, "text": " covered
  in the book?", "tokens": [50732, 5343, 294, 264, 1446, 30, 50850], "temperature":
  0.0, "avg_logprob": -0.23608602134926807, "compression_ratio": 1.5289256198347108,
  "no_speech_prob": 0.03237403929233551}, {"id": 926, "seek": 289850, "start": 2908.22,
  "end": 2909.06, "text": " Awesome.", "tokens": [50850, 10391, 13, 50892], "temperature":
  0.0, "avg_logprob": -0.23608602134926807, "compression_ratio": 1.5289256198347108,
  "no_speech_prob": 0.03237403929233551}, {"id": 927, "seek": 289850, "start": 2909.06,
  "end": 2913.42, "text": " OK, so I would say there''s materialized.", "tokens":
  [50892, 2264, 11, 370, 286, 576, 584, 456, 311, 2527, 1602, 13, 51110], "temperature":
  0.0, "avg_logprob": -0.23608602134926807, "compression_ratio": 1.5289256198347108,
  "no_speech_prob": 0.03237403929233551}, {"id": 928, "seek": 289850, "start": 2913.42,
  "end": 2918.54, "text": " There''s probably like about a 40% overlap.", "tokens":
  [51110, 821, 311, 1391, 411, 466, 257, 3356, 4, 19959, 13, 51366], "temperature":
  0.0, "avg_logprob": -0.23608602134926807, "compression_ratio": 1.5289256198347108,
  "no_speech_prob": 0.03237403929233551}, {"id": 929, "seek": 289850, "start": 2918.54,
  "end": 2921.26, "text": " The book is a good solid foundation", "tokens": [51366,
  440, 1446, 307, 257, 665, 5100, 7030, 51502], "temperature": 0.0, "avg_logprob":
  -0.23608602134926807, "compression_ratio": 1.5289256198347108, "no_speech_prob":
  0.03237403929233551}, {"id": 930, "seek": 289850, "start": 2921.26, "end": 2923.06,
  "text": " for how to think about AI Powered Search.", "tokens": [51502, 337, 577,
  281, 519, 466, 7318, 7086, 292, 17180, 13, 51592], "temperature": 0.0, "avg_logprob":
  -0.23608602134926807, "compression_ratio": 1.5289256198347108, "no_speech_prob":
  0.03237403929233551}, {"id": 931, "seek": 289850, "start": 2923.06, "end": 2925.34,
  "text": " Obviously we go through all the mental models", "tokens": [51592, 7580,
  321, 352, 807, 439, 264, 4973, 5245, 51706], "temperature": 0.0, "avg_logprob":
  -0.23608602134926807, "compression_ratio": 1.5289256198347108, "no_speech_prob":
  0.03237403929233551}, {"id": 932, "seek": 289850, "start": 2925.34, "end": 2926.62,
  "text": " and lots of code examples.", "tokens": [51706, 293, 3195, 295, 3089, 5110,
  13, 51770], "temperature": 0.0, "avg_logprob": -0.23608602134926807, "compression_ratio":
  1.5289256198347108, "no_speech_prob": 0.03237403929233551}, {"id": 933, "seek":
  292662, "start": 2926.62, "end": 2929.06, "text": " So a lot of the labs and a lot
  of the code", "tokens": [50364, 407, 257, 688, 295, 264, 20339, 293, 257, 688, 295,
  264, 3089, 50486], "temperature": 0.0, "avg_logprob": -0.1772294725690569, "compression_ratio":
  2.0368852459016393, "no_speech_prob": 0.0012175999581813812}, {"id": 934, "seek":
  292662, "start": 2929.06, "end": 2931.02, "text": " for the course will come from
  the book.", "tokens": [50486, 337, 264, 1164, 486, 808, 490, 264, 1446, 13, 50584],
  "temperature": 0.0, "avg_logprob": -0.1772294725690569, "compression_ratio": 2.0368852459016393,
  "no_speech_prob": 0.0012175999581813812}, {"id": 935, "seek": 292662, "start": 2931.02,
  "end": 2935.18, "text": " However, there''s a lot of new topics and things", "tokens":
  [50584, 2908, 11, 456, 311, 257, 688, 295, 777, 8378, 293, 721, 50792], "temperature":
  0.0, "avg_logprob": -0.1772294725690569, "compression_ratio": 2.0368852459016393,
  "no_speech_prob": 0.0012175999581813812}, {"id": 936, "seek": 292662, "start": 2935.18,
  "end": 2937.9, "text": " that we just like, we couldn''t write a thousand page book.",
  "tokens": [50792, 300, 321, 445, 411, 11, 321, 2809, 380, 2464, 257, 4714, 3028,
  1446, 13, 50928], "temperature": 0.0, "avg_logprob": -0.1772294725690569, "compression_ratio":
  2.0368852459016393, "no_speech_prob": 0.0012175999581813812}, {"id": 937, "seek":
  292662, "start": 2937.9, "end": 2939.66, "text": " And so there''s a lot of things
  we just couldn''t get to", "tokens": [50928, 400, 370, 456, 311, 257, 688, 295,
  721, 321, 445, 2809, 380, 483, 281, 51016], "temperature": 0.0, "avg_logprob": -0.1772294725690569,
  "compression_ratio": 2.0368852459016393, "no_speech_prob": 0.0012175999581813812},
  {"id": 938, "seek": 292662, "start": 2939.66, "end": 2942.02, "text": " because
  we had to start from the beginning and frame it.", "tokens": [51016, 570, 321, 632,
  281, 722, 490, 264, 2863, 293, 3920, 309, 13, 51134], "temperature": 0.0, "avg_logprob":
  -0.1772294725690569, "compression_ratio": 2.0368852459016393, "no_speech_prob":
  0.0012175999581813812}, {"id": 939, "seek": 292662, "start": 2942.02, "end": 2946.94,
  "text": " So things like late interaction models, things like", "tokens": [51134,
  407, 721, 411, 3469, 9285, 5245, 11, 721, 411, 51380], "temperature": 0.0, "avg_logprob":
  -0.1772294725690569, "compression_ratio": 2.0368852459016393, "no_speech_prob":
  0.0012175999581813812}, {"id": 940, "seek": 292662, "start": 2946.94, "end": 2950.06,
  "text": " a gentick search that aren''t in the book,", "tokens": [51380, 257, 16108,
  618, 3164, 300, 3212, 380, 294, 264, 1446, 11, 51536], "temperature": 0.0, "avg_logprob":
  -0.1772294725690569, "compression_ratio": 2.0368852459016393, "no_speech_prob":
  0.0012175999581813812}, {"id": 941, "seek": 292662, "start": 2950.06, "end": 2951.58,
  "text": " like late interaction models are referenced,", "tokens": [51536, 411,
  3469, 9285, 5245, 366, 32734, 11, 51612], "temperature": 0.0, "avg_logprob": -0.1772294725690569,
  "compression_ratio": 2.0368852459016393, "no_speech_prob": 0.0012175999581813812},
  {"id": 942, "seek": 292662, "start": 2951.58, "end": 2955.02, "text": " but we just
  couldn''t get into depth that are more modern", "tokens": [51612, 457, 321, 445,
  2809, 380, 483, 666, 7161, 300, 366, 544, 4363, 51784], "temperature": 0.0, "avg_logprob":
  -0.1772294725690569, "compression_ratio": 2.0368852459016393, "no_speech_prob":
  0.0012175999581813812}, {"id": 943, "seek": 295502, "start": 2955.02, "end": 2958.14,
  "text": " and interesting ways to solve problems.", "tokens": [50364, 293, 1880,
  2098, 281, 5039, 2740, 13, 50520], "temperature": 0.0, "avg_logprob": -0.17497139236553996,
  "compression_ratio": 1.8979591836734695, "no_speech_prob": 0.008172878064215183},
  {"id": 944, "seek": 295502, "start": 2958.14, "end": 2960.46, "text": " Things like
  mini coil, which I mentioned,", "tokens": [50520, 9514, 411, 8382, 22225, 11, 597,
  286, 2835, 11, 50636], "temperature": 0.0, "avg_logprob": -0.17497139236553996,
  "compression_ratio": 1.8979591836734695, "no_speech_prob": 0.008172878064215183},
  {"id": 945, "seek": 295502, "start": 2960.46, "end": 2963.2599999999998, "text":
  " those things will be in the course and unique to the course", "tokens": [50636,
  729, 721, 486, 312, 294, 264, 1164, 293, 3845, 281, 264, 1164, 50776], "temperature":
  0.0, "avg_logprob": -0.17497139236553996, "compression_ratio": 1.8979591836734695,
  "no_speech_prob": 0.008172878064215183}, {"id": 946, "seek": 295502, "start": 2963.2599999999998,
  "end": 2966.34, "text": " and will have guest speakers who are experts in those
  things.", "tokens": [50776, 293, 486, 362, 8341, 9518, 567, 366, 8572, 294, 729,
  721, 13, 50930], "temperature": 0.0, "avg_logprob": -0.17497139236553996, "compression_ratio":
  1.8979591836734695, "no_speech_prob": 0.008172878064215183}, {"id": 947, "seek":
  295502, "start": 2966.34, "end": 2970.7, "text": " So I would say the course doesn''t
  expect you to have read the book", "tokens": [50930, 407, 286, 576, 584, 264, 1164,
  1177, 380, 2066, 291, 281, 362, 1401, 264, 1446, 51148], "temperature": 0.0, "avg_logprob":
  -0.17497139236553996, "compression_ratio": 1.8979591836734695, "no_speech_prob":
  0.008172878064215183}, {"id": 948, "seek": 295502, "start": 2970.7, "end": 2972.3,
  "text": " or to understand the fundamentals in the book.", "tokens": [51148, 420,
  281, 1223, 264, 29505, 294, 264, 1446, 13, 51228], "temperature": 0.0, "avg_logprob":
  -0.17497139236553996, "compression_ratio": 1.8979591836734695, "no_speech_prob":
  0.008172878064215183}, {"id": 949, "seek": 295502, "start": 2972.3, "end": 2975.74,
  "text": " We''ll cover those, but we won''t cover everything in the book.", "tokens":
  [51228, 492, 603, 2060, 729, 11, 457, 321, 1582, 380, 2060, 1203, 294, 264, 1446,
  13, 51400], "temperature": 0.0, "avg_logprob": -0.17497139236553996, "compression_ratio":
  1.8979591836734695, "no_speech_prob": 0.008172878064215183}, {"id": 950, "seek":
  295502, "start": 2975.74, "end": 2977.1, "text": " And we''ll also cover a lot of
  things", "tokens": [51400, 400, 321, 603, 611, 2060, 257, 688, 295, 721, 51468],
  "temperature": 0.0, "avg_logprob": -0.17497139236553996, "compression_ratio": 1.8979591836734695,
  "no_speech_prob": 0.008172878064215183}, {"id": 951, "seek": 295502, "start": 2977.1,
  "end": 2979.38, "text": " that aren''t in the book and go in deeper depth.", "tokens":
  [51468, 300, 3212, 380, 294, 264, 1446, 293, 352, 294, 7731, 7161, 13, 51582], "temperature":
  0.0, "avg_logprob": -0.17497139236553996, "compression_ratio": 1.8979591836734695,
  "no_speech_prob": 0.008172878064215183}, {"id": 952, "seek": 295502, "start": 2979.38,
  "end": 2981.86, "text": " And so I would say, if you''ve read the book,", "tokens":
  [51582, 400, 370, 286, 576, 584, 11, 498, 291, 600, 1401, 264, 1446, 11, 51706],
  "temperature": 0.0, "avg_logprob": -0.17497139236553996, "compression_ratio": 1.8979591836734695,
  "no_speech_prob": 0.008172878064215183}, {"id": 953, "seek": 295502, "start": 2981.86,
  "end": 2984.58, "text": " the course is still going to be really valuable.", "tokens":
  [51706, 264, 1164, 307, 920, 516, 281, 312, 534, 8263, 13, 51842], "temperature":
  0.0, "avg_logprob": -0.17497139236553996, "compression_ratio": 1.8979591836734695,
  "no_speech_prob": 0.008172878064215183}, {"id": 954, "seek": 298458, "start": 2984.58,
  "end": 2986.38, "text": " And even if you can''t make all the sessions,", "tokens":
  [50364, 400, 754, 498, 291, 393, 380, 652, 439, 264, 11081, 11, 50454], "temperature":
  0.0, "avg_logprob": -0.20999315750500389, "compression_ratio": 1.76, "no_speech_prob":
  0.0011745034717023373}, {"id": 955, "seek": 298458, "start": 2986.38, "end": 2992.54,
  "text": " again, the videos and all the materials available for you forever.", "tokens":
  [50454, 797, 11, 264, 2145, 293, 439, 264, 5319, 2435, 337, 291, 5680, 13, 50762],
  "temperature": 0.0, "avg_logprob": -0.20999315750500389, "compression_ratio": 1.76,
  "no_speech_prob": 0.0011745034717023373}, {"id": 956, "seek": 298458, "start": 2992.54,
  "end": 2996.5, "text": " So you don''t have to have read the book to take the course,",
  "tokens": [50762, 407, 291, 500, 380, 362, 281, 362, 1401, 264, 1446, 281, 747,
  264, 1164, 11, 50960], "temperature": 0.0, "avg_logprob": -0.20999315750500389,
  "compression_ratio": 1.76, "no_speech_prob": 0.0011745034717023373}, {"id": 957,
  "seek": 298458, "start": 2996.5, "end": 2998.22, "text": " but if you have read
  the book, the course", "tokens": [50960, 457, 498, 291, 362, 1401, 264, 1446, 11,
  264, 1164, 51046], "temperature": 0.0, "avg_logprob": -0.20999315750500389, "compression_ratio":
  1.76, "no_speech_prob": 0.0011745034717023373}, {"id": 958, "seek": 298458, "start":
  2998.22, "end": 3000.06, "text": " is still going to be massively useful.", "tokens":
  [51046, 307, 920, 516, 281, 312, 29379, 4420, 13, 51138], "temperature": 0.0, "avg_logprob":
  -0.20999315750500389, "compression_ratio": 1.76, "no_speech_prob": 0.0011745034717023373},
  {"id": 959, "seek": 298458, "start": 3000.06, "end": 3001.7, "text": " Yeah, so
  to implement each other.", "tokens": [51138, 865, 11, 370, 281, 4445, 1184, 661,
  13, 51220], "temperature": 0.0, "avg_logprob": -0.20999315750500389, "compression_ratio":
  1.76, "no_speech_prob": 0.0011745034717023373}, {"id": 960, "seek": 298458, "start":
  3001.7, "end": 3005.94, "text": " And by the way, I own the book and it''s amazing
  read in silency.", "tokens": [51220, 400, 538, 264, 636, 11, 286, 1065, 264, 1446,
  293, 309, 311, 2243, 1401, 294, 3425, 3020, 13, 51432], "temperature": 0.0, "avg_logprob":
  -0.20999315750500389, "compression_ratio": 1.76, "no_speech_prob": 0.0011745034717023373},
  {"id": 961, "seek": 298458, "start": 3005.94, "end": 3008.62, "text": " And then
  the course is a different way of engaging", "tokens": [51432, 400, 550, 264, 1164,
  307, 257, 819, 636, 295, 11268, 51566], "temperature": 0.0, "avg_logprob": -0.20999315750500389,
  "compression_ratio": 1.76, "no_speech_prob": 0.0011745034717023373}, {"id": 962,
  "seek": 298458, "start": 3008.62, "end": 3012.62, "text": " with the material like
  a dynamic way.", "tokens": [51566, 365, 264, 2527, 411, 257, 8546, 636, 13, 51766],
  "temperature": 0.0, "avg_logprob": -0.20999315750500389, "compression_ratio": 1.76,
  "no_speech_prob": 0.0011745034717023373}, {"id": 963, "seek": 301262, "start": 3012.62,
  "end": 3014.1, "text": " Well, I didn''t answer the last part, which", "tokens":
  [50364, 1042, 11, 286, 994, 380, 1867, 264, 1036, 644, 11, 597, 50438], "temperature":
  0.0, "avg_logprob": -0.20913433661827674, "compression_ratio": 1.674496644295302,
  "no_speech_prob": 0.0022750417701900005}, {"id": 964, "seek": 301262, "start": 3014.1,
  "end": 3016.46, "text": " is, will wormhole vectors be covered?", "tokens": [50438,
  307, 11, 486, 23835, 14094, 18875, 312, 5343, 30, 50556], "temperature": 0.0, "avg_logprob":
  -0.20913433661827674, "compression_ratio": 1.674496644295302, "no_speech_prob":
  0.0022750417701900005}, {"id": 965, "seek": 301262, "start": 3016.46, "end": 3019.54,
  "text": " They will definitely be covered more", "tokens": [50556, 814, 486, 2138,
  312, 5343, 544, 50710], "temperature": 0.0, "avg_logprob": -0.20913433661827674,
  "compression_ratio": 1.674496644295302, "no_speech_prob": 0.0022750417701900005},
  {"id": 966, "seek": 301262, "start": 3019.54, "end": 3023.42, "text": " so as the
  techniques and strategies for how", "tokens": [50710, 370, 382, 264, 7512, 293,
  9029, 337, 577, 50904], "temperature": 0.0, "avg_logprob": -0.20913433661827674,
  "compression_ratio": 1.674496644295302, "no_speech_prob": 0.0022750417701900005},
  {"id": 967, "seek": 301262, "start": 3023.42, "end": 3025.18, "text": " to hop back
  and forth between.", "tokens": [50904, 281, 3818, 646, 293, 5220, 1296, 13, 50992],
  "temperature": 0.0, "avg_logprob": -0.20913433661827674, "compression_ratio": 1.674496644295302,
  "no_speech_prob": 0.0022750417701900005}, {"id": 968, "seek": 301262, "start": 3025.18,
  "end": 3028.18, "text": " So some of it''s actually in the book, the semantic knowledge",
  "tokens": [50992, 407, 512, 295, 309, 311, 767, 294, 264, 1446, 11, 264, 47982,
  3601, 51142], "temperature": 0.0, "avg_logprob": -0.20913433661827674, "compression_ratio":
  1.674496644295302, "no_speech_prob": 0.0022750417701900005}, {"id": 969, "seek":
  301262, "start": 3028.18, "end": 3029.7799999999997, "text": " graph stuff is already
  in the book.", "tokens": [51142, 4295, 1507, 307, 1217, 294, 264, 1446, 13, 51222],
  "temperature": 0.0, "avg_logprob": -0.20913433661827674, "compression_ratio": 1.674496644295302,
  "no_speech_prob": 0.0022750417701900005}, {"id": 970, "seek": 301262, "start": 3029.7799999999997,
  "end": 3034.2999999999997, "text": " But the, yeah, we''ll definitely talk about
  wormhole vectors", "tokens": [51222, 583, 264, 11, 1338, 11, 321, 603, 2138, 751,
  466, 23835, 14094, 18875, 51448], "temperature": 0.0, "avg_logprob": -0.20913433661827674,
  "compression_ratio": 1.674496644295302, "no_speech_prob": 0.0022750417701900005},
  {"id": 971, "seek": 301262, "start": 3034.2999999999997, "end": 3036.38, "text":
  " explicitly and have some more specific examples", "tokens": [51448, 20803, 293,
  362, 512, 544, 2685, 5110, 51552], "temperature": 0.0, "avg_logprob": -0.20913433661827674,
  "compression_ratio": 1.674496644295302, "no_speech_prob": 0.0022750417701900005},
  {"id": 972, "seek": 301262, "start": 3036.38, "end": 3037.62, "text": " people can
  play with.", "tokens": [51552, 561, 393, 862, 365, 13, 51614], "temperature": 0.0,
  "avg_logprob": -0.20913433661827674, "compression_ratio": 1.674496644295302, "no_speech_prob":
  0.0022750417701900005}, {"id": 973, "seek": 301262, "start": 3037.62, "end": 3039.1,
  "text": " Yeah, awesome.", "tokens": [51614, 865, 11, 3476, 13, 51688], "temperature":
  0.0, "avg_logprob": -0.20913433661827674, "compression_ratio": 1.674496644295302,
  "no_speech_prob": 0.0022750417701900005}, {"id": 974, "seek": 301262, "start": 3039.1,
  "end": 3042.38, "text": " And I do want to mention this is like experimental and
  emerging.", "tokens": [51688, 400, 286, 360, 528, 281, 2152, 341, 307, 411, 17069,
  293, 14989, 13, 51852], "temperature": 0.0, "avg_logprob": -0.20913433661827674,
  "compression_ratio": 1.674496644295302, "no_speech_prob": 0.0022750417701900005},
  {"id": 975, "seek": 304238, "start": 3042.38, "end": 3046.2200000000003, "text":
  " And there''s some things that I glossed over today", "tokens": [50364, 400, 456,
  311, 512, 721, 300, 286, 19574, 292, 670, 965, 50556], "temperature": 0.0, "avg_logprob":
  -0.23646517412378154, "compression_ratio": 1.6282051282051282, "no_speech_prob":
  0.00036594553967006505}, {"id": 976, "seek": 304238, "start": 3046.2200000000003,
  "end": 3050.2200000000003, "text": " in terms of hopping to a particular point",
  "tokens": [50556, 294, 2115, 295, 47199, 281, 257, 1729, 935, 50756], "temperature":
  0.0, "avg_logprob": -0.23646517412378154, "compression_ratio": 1.6282051282051282,
  "no_speech_prob": 0.00036594553967006505}, {"id": 977, "seek": 304238, "start":
  3050.2200000000003, "end": 3053.54, "text": " versus trying to hop to a region and
  have more of a shape", "tokens": [50756, 5717, 1382, 281, 3818, 281, 257, 4458,
  293, 362, 544, 295, 257, 3909, 50922], "temperature": 0.0, "avg_logprob": -0.23646517412378154,
  "compression_ratio": 1.6282051282051282, "no_speech_prob": 0.00036594553967006505},
  {"id": 978, "seek": 304238, "start": 3053.54, "end": 3055.34, "text": " that we
  could chat about as well.", "tokens": [50922, 300, 321, 727, 5081, 466, 382, 731,
  13, 51012], "temperature": 0.0, "avg_logprob": -0.23646517412378154, "compression_ratio":
  1.6282051282051282, "no_speech_prob": 0.00036594553967006505}, {"id": 979, "seek":
  304238, "start": 3055.34, "end": 3060.54, "text": " But yeah, there''s still some
  things", "tokens": [51012, 583, 1338, 11, 456, 311, 920, 512, 721, 51272], "temperature":
  0.0, "avg_logprob": -0.23646517412378154, "compression_ratio": 1.6282051282051282,
  "no_speech_prob": 0.00036594553967006505}, {"id": 980, "seek": 304238, "start":
  3060.54, "end": 3063.5, "text": " I''m doing to kind of better understand it fine
  to know.", "tokens": [51272, 286, 478, 884, 281, 733, 295, 1101, 1223, 309, 2489,
  281, 458, 13, 51420], "temperature": 0.0, "avg_logprob": -0.23646517412378154, "compression_ratio":
  1.6282051282051282, "no_speech_prob": 0.00036594553967006505}, {"id": 981, "seek":
  304238, "start": 3063.5, "end": 3065.34, "text": " Yeah, awesome.", "tokens": [51420,
  865, 11, 3476, 13, 51512], "temperature": 0.0, "avg_logprob": -0.23646517412378154,
  "compression_ratio": 1.6282051282051282, "no_speech_prob": 0.00036594553967006505},
  {"id": 982, "seek": 304238, "start": 3065.34, "end": 3066.42, "text": " I''m trying
  to speed up.", "tokens": [51512, 286, 478, 1382, 281, 3073, 493, 13, 51566], "temperature":
  0.0, "avg_logprob": -0.23646517412378154, "compression_ratio": 1.6282051282051282,
  "no_speech_prob": 0.00036594553967006505}, {"id": 983, "seek": 304238, "start":
  3066.42, "end": 3069.26, "text": " But there''s a question from Claudiu.", "tokens":
  [51566, 583, 456, 311, 257, 1168, 490, 24858, 5951, 13, 51708], "temperature": 0.0,
  "avg_logprob": -0.23646517412378154, "compression_ratio": 1.6282051282051282, "no_speech_prob":
  0.00036594553967006505}, {"id": 984, "seek": 304238, "start": 3069.26, "end": 3070.62,
  "text": " What are the latent features?", "tokens": [51708, 708, 366, 264, 48994,
  4122, 30, 51776], "temperature": 0.0, "avg_logprob": -0.23646517412378154, "compression_ratio":
  1.6282051282051282, "no_speech_prob": 0.00036594553967006505}, {"id": 985, "seek":
  307062, "start": 3070.62, "end": 3074.7799999999997, "text": " And basically where
  you switched from sort of explicit feature", "tokens": [50364, 400, 1936, 689, 291,
  16858, 490, 1333, 295, 13691, 4111, 50572], "temperature": 0.0, "avg_logprob": -0.23717843569242036,
  "compression_ratio": 1.646341463414634, "no_speech_prob": 0.005522354505956173},
  {"id": 986, "seek": 307062, "start": 3074.7799999999997, "end": 3077.18, "text":
  " metrics to like latent features.", "tokens": [50572, 16367, 281, 411, 48994, 4122,
  13, 50692], "temperature": 0.0, "avg_logprob": -0.23717843569242036, "compression_ratio":
  1.646341463414634, "no_speech_prob": 0.005522354505956173}, {"id": 987, "seek":
  307062, "start": 3077.18, "end": 3078.66, "text": " Maybe I can take it quickly.",
  "tokens": [50692, 2704, 286, 393, 747, 309, 2661, 13, 50766], "temperature": 0.0,
  "avg_logprob": -0.23717843569242036, "compression_ratio": 1.646341463414634, "no_speech_prob":
  0.005522354505956173}, {"id": 988, "seek": 307062, "start": 3078.66, "end": 3080.94,
  "text": " It''s basically in an LLAM.", "tokens": [50766, 467, 311, 1936, 294, 364,
  441, 43, 2865, 13, 50880], "temperature": 0.0, "avg_logprob": -0.23717843569242036,
  "compression_ratio": 1.646341463414634, "no_speech_prob": 0.005522354505956173},
  {"id": 989, "seek": 307062, "start": 3080.94, "end": 3083.22, "text": " So if you
  deal with an encoder model,", "tokens": [50880, 407, 498, 291, 2028, 365, 364, 2058,
  19866, 2316, 11, 50994], "temperature": 0.0, "avg_logprob": -0.23717843569242036,
  "compression_ratio": 1.646341463414634, "no_speech_prob": 0.005522354505956173},
  {"id": 990, "seek": 307062, "start": 3083.22, "end": 3086.54, "text": " where you
  generate embeddings, basically", "tokens": [50994, 689, 291, 8460, 12240, 29432,
  11, 1936, 51160], "temperature": 0.0, "avg_logprob": -0.23717843569242036, "compression_ratio":
  1.646341463414634, "no_speech_prob": 0.005522354505956173}, {"id": 991, "seek":
  307062, "start": 3086.54, "end": 3088.3399999999997, "text": " these are like internal
  representations", "tokens": [51160, 613, 366, 411, 6920, 33358, 51250], "temperature":
  0.0, "avg_logprob": -0.23717843569242036, "compression_ratio": 1.646341463414634,
  "no_speech_prob": 0.005522354505956173}, {"id": 992, "seek": 307062, "start": 3088.3399999999997,
  "end": 3089.58, "text": " that the model learns.", "tokens": [51250, 300, 264, 2316,
  27152, 13, 51312], "temperature": 0.0, "avg_logprob": -0.23717843569242036, "compression_ratio":
  1.646341463414634, "no_speech_prob": 0.005522354505956173}, {"id": 993, "seek":
  307062, "start": 3089.58, "end": 3091.1, "text": " And they''re like compressed.",
  "tokens": [51312, 400, 436, 434, 411, 30353, 13, 51388], "temperature": 0.0, "avg_logprob":
  -0.23717843569242036, "compression_ratio": 1.646341463414634, "no_speech_prob":
  0.005522354505956173}, {"id": 994, "seek": 307062, "start": 3091.1, "end": 3094.8599999999997,
  "text": " They''re like abstract way of dealing with patterns", "tokens": [51388,
  814, 434, 411, 12649, 636, 295, 6260, 365, 8294, 51576], "temperature": 0.0, "avg_logprob":
  -0.23717843569242036, "compression_ratio": 1.646341463414634, "no_speech_prob":
  0.005522354505956173}, {"id": 995, "seek": 307062, "start": 3094.8599999999997,
  "end": 3097.42, "text": " or relationships and your data.", "tokens": [51576, 420,
  6159, 293, 428, 1412, 13, 51704], "temperature": 0.0, "avg_logprob": -0.23717843569242036,
  "compression_ratio": 1.646341463414634, "no_speech_prob": 0.005522354505956173},
  {"id": 996, "seek": 309742, "start": 3097.42, "end": 3100.7400000000002, "text":
  " It''s not exactly directly that black and white,", "tokens": [50364, 467, 311,
  406, 2293, 3838, 300, 2211, 293, 2418, 11, 50530], "temperature": 0.0, "avg_logprob":
  -0.2316513421400538, "compression_ratio": 1.578512396694215, "no_speech_prob": 0.00023609970230609179},
  {"id": 997, "seek": 309742, "start": 3100.7400000000002, "end": 3104.02, "text":
  " but the thing is that on the conceptual level,", "tokens": [50530, 457, 264, 551,
  307, 300, 322, 264, 24106, 1496, 11, 50694], "temperature": 0.0, "avg_logprob":
  -0.2316513421400538, "compression_ratio": 1.578512396694215, "no_speech_prob": 0.00023609970230609179},
  {"id": 998, "seek": 309742, "start": 3104.02, "end": 3108.14, "text": " these are
  like internal weights that the model learns.", "tokens": [50694, 613, 366, 411,
  6920, 17443, 300, 264, 2316, 27152, 13, 50900], "temperature": 0.0, "avg_logprob":
  -0.2316513421400538, "compression_ratio": 1.578512396694215, "no_speech_prob": 0.00023609970230609179},
  {"id": 999, "seek": 309742, "start": 3108.14, "end": 3111.2200000000003, "text":
  " Then there is a question from Julian, very concrete one.", "tokens": [50900, 1396,
  456, 307, 257, 1168, 490, 25151, 11, 588, 9859, 472, 13, 51054], "temperature":
  0.0, "avg_logprob": -0.2316513421400538, "compression_ratio": 1.578512396694215,
  "no_speech_prob": 0.00023609970230609179}, {"id": 1000, "seek": 309742, "start":
  3111.2200000000003, "end": 3113.78, "text": " Can you give an great example of how",
  "tokens": [51054, 1664, 291, 976, 364, 869, 1365, 295, 577, 51182], "temperature":
  0.0, "avg_logprob": -0.2316513421400538, "compression_ratio": 1.578512396694215,
  "no_speech_prob": 0.00023609970230609179}, {"id": 1001, "seek": 309742, "start":
  3113.78, "end": 3119.54, "text": " to compute the wormhole vector from sparse to
  dense space?", "tokens": [51182, 281, 14722, 264, 23835, 14094, 8062, 490, 637,
  11668, 281, 18011, 1901, 30, 51470], "temperature": 0.0, "avg_logprob": -0.2316513421400538,
  "compression_ratio": 1.578512396694215, "no_speech_prob": 0.00023609970230609179},
  {"id": 1002, "seek": 309742, "start": 3119.54, "end": 3121.46, "text": " Yeah, so
  I had a slide.", "tokens": [51470, 865, 11, 370, 286, 632, 257, 4137, 13, 51566],
  "temperature": 0.0, "avg_logprob": -0.2316513421400538, "compression_ratio": 1.578512396694215,
  "no_speech_prob": 0.00023609970230609179}, {"id": 1003, "seek": 309742, "start":
  3121.46, "end": 3127.06, "text": " It''s sparse to dense is the easy one, which
  is, let me,", "tokens": [51566, 467, 311, 637, 11668, 281, 18011, 307, 264, 1858,
  472, 11, 597, 307, 11, 718, 385, 11, 51846], "temperature": 0.0, "avg_logprob":
  -0.2316513421400538, "compression_ratio": 1.578512396694215, "no_speech_prob": 0.00023609970230609179},
  {"id": 1004, "seek": 312706, "start": 3127.06, "end": 3128.2999999999997, "text":
  " let me go back to the slide.", "tokens": [50364, 718, 385, 352, 646, 281, 264,
  4137, 13, 50426], "temperature": 0.0, "avg_logprob": -0.222856482680963, "compression_ratio":
  1.5944700460829493, "no_speech_prob": 0.0004166789003647864}, {"id": 1005, "seek":
  312706, "start": 3131.1, "end": 3133.7, "text": " One second almost there.", "tokens":
  [50566, 1485, 1150, 1920, 456, 13, 50696], "temperature": 0.0, "avg_logprob": -0.222856482680963,
  "compression_ratio": 1.5944700460829493, "no_speech_prob": 0.0004166789003647864},
  {"id": 1006, "seek": 312706, "start": 3136.66, "end": 3138.38, "text": " Here we
  go.", "tokens": [50844, 1692, 321, 352, 13, 50930], "temperature": 0.0, "avg_logprob":
  -0.222856482680963, "compression_ratio": 1.5944700460829493, "no_speech_prob": 0.0004166789003647864},
  {"id": 1007, "seek": 312706, "start": 3138.38, "end": 3143.38, "text": " So to go
  from sparse to dense, think of it this way.", "tokens": [50930, 407, 281, 352, 490,
  637, 11668, 281, 18011, 11, 519, 295, 309, 341, 636, 13, 51180], "temperature":
  0.0, "avg_logprob": -0.222856482680963, "compression_ratio": 1.5944700460829493,
  "no_speech_prob": 0.0004166789003647864}, {"id": 1008, "seek": 312706, "start":
  3143.38, "end": 3145.7799999999997, "text": " You''ve got a bunch of documents in
  your index,", "tokens": [51180, 509, 600, 658, 257, 3840, 295, 8512, 294, 428, 8186,
  11, 51300], "temperature": 0.0, "avg_logprob": -0.222856482680963, "compression_ratio":
  1.5944700460829493, "no_speech_prob": 0.0004166789003647864}, {"id": 1009, "seek":
  312706, "start": 3145.7799999999997, "end": 3148.14, "text": " and you generate
  embeddings for those documents.", "tokens": [51300, 293, 291, 8460, 12240, 29432,
  337, 729, 8512, 13, 51418], "temperature": 0.0, "avg_logprob": -0.222856482680963,
  "compression_ratio": 1.5944700460829493, "no_speech_prob": 0.0004166789003647864},
  {"id": 1010, "seek": 312706, "start": 3148.14, "end": 3151.34, "text": " That''s
  how your dense space is constructed, right?", "tokens": [51418, 663, 311, 577, 428,
  18011, 1901, 307, 17083, 11, 558, 30, 51578], "temperature": 0.0, "avg_logprob":
  -0.222856482680963, "compression_ratio": 1.5944700460829493, "no_speech_prob": 0.0004166789003647864},
  {"id": 1011, "seek": 312706, "start": 3151.34, "end": 3153.2999999999997, "text":
  " Those embeddings on the documents,", "tokens": [51578, 3950, 12240, 29432, 322,
  264, 8512, 11, 51676], "temperature": 0.0, "avg_logprob": -0.222856482680963, "compression_ratio":
  1.5944700460829493, "no_speech_prob": 0.0004166789003647864}, {"id": 1012, "seek":
  312706, "start": 3153.2999999999997, "end": 3155.94, "text": " if you query for
  the documents using keywords", "tokens": [51676, 498, 291, 14581, 337, 264, 8512,
  1228, 21009, 51808], "temperature": 0.0, "avg_logprob": -0.222856482680963, "compression_ratio":
  1.5944700460829493, "no_speech_prob": 0.0004166789003647864}, {"id": 1013, "seek":
  315594, "start": 3155.94, "end": 3158.58, "text": " in your sparse space, then you''re
  still", "tokens": [50364, 294, 428, 637, 11668, 1901, 11, 550, 291, 434, 920, 50496],
  "temperature": 0.0, "avg_logprob": -0.16652173844594803, "compression_ratio": 1.8171641791044777,
  "no_speech_prob": 0.0008758945623412728}, {"id": 1014, "seek": 315594, "start":
  3158.58, "end": 3159.86, "text": " matching that set of documents,", "tokens": [50496,
  14324, 300, 992, 295, 8512, 11, 50560], "temperature": 0.0, "avg_logprob": -0.16652173844594803,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.0008758945623412728},
  {"id": 1015, "seek": 315594, "start": 3159.86, "end": 3162.3, "text": " and all
  of those documents have the embeddings on them.", "tokens": [50560, 293, 439, 295,
  729, 8512, 362, 264, 12240, 29432, 322, 552, 13, 50682], "temperature": 0.0, "avg_logprob":
  -0.16652173844594803, "compression_ratio": 1.8171641791044777, "no_speech_prob":
  0.0008758945623412728}, {"id": 1016, "seek": 315594, "start": 3162.3, "end": 3165.54,
  "text": " So all you do is run a keyword search on your documents,", "tokens": [50682,
  407, 439, 291, 360, 307, 1190, 257, 20428, 3164, 322, 428, 8512, 11, 50844], "temperature":
  0.0, "avg_logprob": -0.16652173844594803, "compression_ratio": 1.8171641791044777,
  "no_speech_prob": 0.0008758945623412728}, {"id": 1017, "seek": 315594, "start":
  3165.54, "end": 3168.18, "text": " take the top end documents are the most relevant,
  right?", "tokens": [50844, 747, 264, 1192, 917, 8512, 366, 264, 881, 7340, 11, 558,
  30, 50976], "temperature": 0.0, "avg_logprob": -0.16652173844594803, "compression_ratio":
  1.8171641791044777, "no_speech_prob": 0.0008758945623412728}, {"id": 1018, "seek":
  315594, "start": 3168.18, "end": 3172.7400000000002, "text": " They hopefully semantically
  represent the concept the best.", "tokens": [50976, 814, 4696, 4361, 49505, 2906,
  264, 3410, 264, 1151, 13, 51204], "temperature": 0.0, "avg_logprob": -0.16652173844594803,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.0008758945623412728},
  {"id": 1019, "seek": 315594, "start": 3172.7400000000002, "end": 3175.26, "text":
  " And then you take those embeddings off of them,", "tokens": [51204, 400, 550,
  291, 747, 729, 12240, 29432, 766, 295, 552, 11, 51330], "temperature": 0.0, "avg_logprob":
  -0.16652173844594803, "compression_ratio": 1.8171641791044777, "no_speech_prob":
  0.0008758945623412728}, {"id": 1020, "seek": 315594, "start": 3175.26, "end": 3177.02,
  "text": " and you literally abverse them together.", "tokens": [51330, 293, 291,
  3736, 410, 4308, 552, 1214, 13, 51418], "temperature": 0.0, "avg_logprob": -0.16652173844594803,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.0008758945623412728},
  {"id": 1021, "seek": 315594, "start": 3177.02, "end": 3180.78, "text": " The code
  for that is on the screen right here,", "tokens": [51418, 440, 3089, 337, 300, 307,
  322, 264, 2568, 558, 510, 11, 51606], "temperature": 0.0, "avg_logprob": -0.16652173844594803,
  "compression_ratio": 1.8171641791044777, "no_speech_prob": 0.0008758945623412728},
  {"id": 1022, "seek": 315594, "start": 3180.78, "end": 3183.7000000000003, "text":
  " and that you just generate this pooled embedding.", "tokens": [51606, 293, 300,
  291, 445, 8460, 341, 7005, 292, 12240, 3584, 13, 51752], "temperature": 0.0, "avg_logprob":
  -0.16652173844594803, "compression_ratio": 1.8171641791044777, "no_speech_prob":
  0.0008758945623412728}, {"id": 1023, "seek": 318370, "start": 3183.7, "end": 3186.14,
  "text": " It''s that notion of Darth Vader versus Puppy,", "tokens": [50364, 467,
  311, 300, 10710, 295, 40696, 36337, 5717, 13605, 7966, 11, 50486], "temperature":
  0.0, "avg_logprob": -0.1876959707222733, "compression_ratio": 1.8772563176895307,
  "no_speech_prob": 0.0005989124183543026}, {"id": 1024, "seek": 318370, "start":
  3186.14, "end": 3188.5, "text": " and finding the Puppy Darth Vader in the middle,
  right?", "tokens": [50486, 293, 5006, 264, 13605, 7966, 40696, 36337, 294, 264,
  2808, 11, 558, 30, 50604], "temperature": 0.0, "avg_logprob": -0.1876959707222733,
  "compression_ratio": 1.8772563176895307, "no_speech_prob": 0.0005989124183543026},
  {"id": 1025, "seek": 318370, "start": 3188.5, "end": 3190.8599999999997, "text":
  " If someone were to run a keyword search,", "tokens": [50604, 759, 1580, 645, 281,
  1190, 257, 20428, 3164, 11, 50722], "temperature": 0.0, "avg_logprob": -0.1876959707222733,
  "compression_ratio": 1.8772563176895307, "no_speech_prob": 0.0005989124183543026},
  {"id": 1026, "seek": 318370, "start": 3190.8599999999997, "end": 3193.3399999999997,
  "text": " and it''s sort of, it''s easy to think of this", "tokens": [50722, 293,
  309, 311, 1333, 295, 11, 309, 311, 1858, 281, 519, 295, 341, 50846], "temperature":
  0.0, "avg_logprob": -0.1876959707222733, "compression_ratio": 1.8772563176895307,
  "no_speech_prob": 0.0005989124183543026}, {"id": 1027, "seek": 318370, "start":
  3193.3399999999997, "end": 3195.8999999999996, "text": " with a single keyword,
  but let''s go back to my,", "tokens": [50846, 365, 257, 2167, 20428, 11, 457, 718,
  311, 352, 646, 281, 452, 11, 50974], "temperature": 0.0, "avg_logprob": -0.1876959707222733,
  "compression_ratio": 1.8772563176895307, "no_speech_prob": 0.0005989124183543026},
  {"id": 1028, "seek": 318370, "start": 3199.18, "end": 3200.8599999999997, "text":
  " let''s go back to cheese pizza, right?", "tokens": [51138, 718, 311, 352, 646,
  281, 5399, 8298, 11, 558, 30, 51222], "temperature": 0.0, "avg_logprob": -0.1876959707222733,
  "compression_ratio": 1.8772563176895307, "no_speech_prob": 0.0005989124183543026},
  {"id": 1029, "seek": 318370, "start": 3200.8599999999997, "end": 3203.8199999999997,
  "text": " Like if I search for pizza, I''m gonna match a bunch of pizzas.", "tokens":
  [51222, 1743, 498, 286, 3164, 337, 8298, 11, 286, 478, 799, 2995, 257, 3840, 295,
  44037, 13, 51370], "temperature": 0.0, "avg_logprob": -0.1876959707222733, "compression_ratio":
  1.8772563176895307, "no_speech_prob": 0.0005989124183543026}, {"id": 1030, "seek":
  318370, "start": 3203.8199999999997, "end": 3205.7, "text": " If I search for, maybe
  cheese pizza is back", "tokens": [51370, 759, 286, 3164, 337, 11, 1310, 5399, 8298,
  307, 646, 51464], "temperature": 0.0, "avg_logprob": -0.1876959707222733, "compression_ratio":
  1.8772563176895307, "no_speech_prob": 0.0005989124183543026}, {"id": 1031, "seek":
  318370, "start": 3205.7, "end": 3209.3799999999997, "text": " as all pizza has cheese,
  let''s do cinnamon bread sticks, right?", "tokens": [51464, 382, 439, 8298, 575,
  5399, 11, 718, 311, 360, 22969, 5961, 12518, 11, 558, 30, 51648], "temperature":
  0.0, "avg_logprob": -0.1876959707222733, "compression_ratio": 1.8772563176895307,
  "no_speech_prob": 0.0005989124183543026}, {"id": 1032, "seek": 318370, "start":
  3209.3799999999997, "end": 3212.02, "text": " If I search for bread, I''m gonna
  find bread.", "tokens": [51648, 759, 286, 3164, 337, 5961, 11, 286, 478, 799, 915,
  5961, 13, 51780], "temperature": 0.0, "avg_logprob": -0.1876959707222733, "compression_ratio":
  1.8772563176895307, "no_speech_prob": 0.0005989124183543026}, {"id": 1033, "seek":
  318370, "start": 3212.02, "end": 3213.1, "text": " Documents have the word bread.",
  "tokens": [51780, 16024, 4697, 362, 264, 1349, 5961, 13, 51834], "temperature":
  0.0, "avg_logprob": -0.1876959707222733, "compression_ratio": 1.8772563176895307,
  "no_speech_prob": 0.0005989124183543026}, {"id": 1034, "seek": 321310, "start":
  3213.1, "end": 3215.46, "text": " If I search for cinnamon, I find documents with
  cinnamon.", "tokens": [50364, 759, 286, 3164, 337, 22969, 11, 286, 915, 8512, 365,
  22969, 13, 50482], "temperature": 0.0, "avg_logprob": -0.11311496628655328, "compression_ratio":
  2.1294117647058823, "no_speech_prob": 0.0004339195729698986}, {"id": 1035, "seek":
  321310, "start": 3215.46, "end": 3217.7799999999997, "text": " If I search for sticks,
  I find documents with sticks.", "tokens": [50482, 759, 286, 3164, 337, 12518, 11,
  286, 915, 8512, 365, 12518, 13, 50598], "temperature": 0.0, "avg_logprob": -0.11311496628655328,
  "compression_ratio": 2.1294117647058823, "no_speech_prob": 0.0004339195729698986},
  {"id": 1036, "seek": 321310, "start": 3217.7799999999997, "end": 3220.42, "text":
  " Sticks by itself isn''t really what I''m looking for,", "tokens": [50598, 745,
  7663, 538, 2564, 1943, 380, 534, 437, 286, 478, 1237, 337, 11, 50730], "temperature":
  0.0, "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823,
  "no_speech_prob": 0.0004339195729698986}, {"id": 1037, "seek": 321310, "start":
  3220.42, "end": 3222.9, "text": " but if I do cinnamon bread sticks,", "tokens":
  [50730, 457, 498, 286, 360, 22969, 5961, 12518, 11, 50854], "temperature": 0.0,
  "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823, "no_speech_prob":
  0.0004339195729698986}, {"id": 1038, "seek": 321310, "start": 3222.9, "end": 3224.42,
  "text": " then I''m finding all of the documents", "tokens": [50854, 550, 286, 478,
  5006, 439, 295, 264, 8512, 50930], "temperature": 0.0, "avg_logprob": -0.11311496628655328,
  "compression_ratio": 2.1294117647058823, "no_speech_prob": 0.0004339195729698986},
  {"id": 1039, "seek": 321310, "start": 3224.42, "end": 3226.54, "text": " that have
  those terms together,", "tokens": [50930, 300, 362, 729, 2115, 1214, 11, 51036],
  "temperature": 0.0, "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823,
  "no_speech_prob": 0.0004339195729698986}, {"id": 1040, "seek": 321310, "start":
  3226.54, "end": 3229.8199999999997, "text": " which likely are cinnamon bread sticks,",
  "tokens": [51036, 597, 3700, 366, 22969, 5961, 12518, 11, 51200], "temperature":
  0.0, "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823,
  "no_speech_prob": 0.0004339195729698986}, {"id": 1041, "seek": 321310, "start":
  3229.8199999999997, "end": 3231.54, "text": " or have the notion of cinnamon bread
  sticks,", "tokens": [51200, 420, 362, 264, 10710, 295, 22969, 5961, 12518, 11, 51286],
  "temperature": 0.0, "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823,
  "no_speech_prob": 0.0004339195729698986}, {"id": 1042, "seek": 321310, "start":
  3231.54, "end": 3233.74, "text": " or talking about cinnamon bread sticks.", "tokens":
  [51286, 420, 1417, 466, 22969, 5961, 12518, 13, 51396], "temperature": 0.0, "avg_logprob":
  -0.11311496628655328, "compression_ratio": 2.1294117647058823, "no_speech_prob":
  0.0004339195729698986}, {"id": 1043, "seek": 321310, "start": 3233.74, "end": 3235.5,
  "text": " So if I take all of those documents,", "tokens": [51396, 407, 498, 286,
  747, 439, 295, 729, 8512, 11, 51484], "temperature": 0.0, "avg_logprob": -0.11311496628655328,
  "compression_ratio": 2.1294117647058823, "no_speech_prob": 0.0004339195729698986},
  {"id": 1044, "seek": 321310, "start": 3235.5, "end": 3238.46, "text": " the most
  relevant ones, and I generate,", "tokens": [51484, 264, 881, 7340, 2306, 11, 293,
  286, 8460, 11, 51632], "temperature": 0.0, "avg_logprob": -0.11311496628655328,
  "compression_ratio": 2.1294117647058823, "no_speech_prob": 0.0004339195729698986},
  {"id": 1045, "seek": 321310, "start": 3238.46, "end": 3239.86, "text": " and I average
  their embeddings together,", "tokens": [51632, 293, 286, 4274, 641, 12240, 29432,
  1214, 11, 51702], "temperature": 0.0, "avg_logprob": -0.11311496628655328, "compression_ratio":
  2.1294117647058823, "no_speech_prob": 0.0004339195729698986}, {"id": 1046, "seek":
  321310, "start": 3239.86, "end": 3242.7799999999997, "text": " and go over to the
  dense space,", "tokens": [51702, 293, 352, 670, 281, 264, 18011, 1901, 11, 51848],
  "temperature": 0.0, "avg_logprob": -0.11311496628655328, "compression_ratio": 2.1294117647058823,
  "no_speech_prob": 0.0004339195729698986}, {"id": 1047, "seek": 324278, "start":
  3242.78, "end": 3247.42, "text": " where I land should be where the concept of cinnamon
  bread sticks is,", "tokens": [50364, 689, 286, 2117, 820, 312, 689, 264, 3410, 295,
  22969, 5961, 12518, 307, 11, 50596], "temperature": 0.0, "avg_logprob": -0.22591648931088654,
  "compression_ratio": 1.7508650519031141, "no_speech_prob": 0.0006612985162064433},
  {"id": 1048, "seek": 324278, "start": 3247.42, "end": 3252.26, "text": " and things
  nearby, which may not have the word cinnamon bread or sticks in them,", "tokens":
  [50596, 293, 721, 11184, 11, 597, 815, 406, 362, 264, 1349, 22969, 5961, 420, 12518,
  294, 552, 11, 50838], "temperature": 0.0, "avg_logprob": -0.22591648931088654, "compression_ratio":
  1.7508650519031141, "no_speech_prob": 0.0006612985162064433}, {"id": 1049, "seek":
  324278, "start": 3252.26, "end": 3252.98, "text": " should come back.", "tokens":
  [50838, 820, 808, 646, 13, 50874], "temperature": 0.0, "avg_logprob": -0.22591648931088654,
  "compression_ratio": 1.7508650519031141, "no_speech_prob": 0.0006612985162064433},
  {"id": 1050, "seek": 324278, "start": 3252.98, "end": 3255.78, "text": " I might
  get certain kinds of doughnuts,", "tokens": [50874, 286, 1062, 483, 1629, 3685,
  295, 7984, 29251, 11, 51014], "temperature": 0.0, "avg_logprob": -0.22591648931088654,
  "compression_ratio": 1.7508650519031141, "no_speech_prob": 0.0006612985162064433},
  {"id": 1051, "seek": 324278, "start": 3255.78, "end": 3258.5800000000004, "text":
  " and certain kind, I might get like a churro or something like that.", "tokens":
  [51014, 293, 1629, 733, 11, 286, 1062, 483, 411, 257, 417, 374, 340, 420, 746, 411,
  300, 13, 51154], "temperature": 0.0, "avg_logprob": -0.22591648931088654, "compression_ratio":
  1.7508650519031141, "no_speech_prob": 0.0006612985162064433}, {"id": 1052, "seek":
  324278, "start": 3258.5800000000004, "end": 3259.86, "text": " So that''s how it
  works.", "tokens": [51154, 407, 300, 311, 577, 309, 1985, 13, 51218], "temperature":
  0.0, "avg_logprob": -0.22591648931088654, "compression_ratio": 1.7508650519031141,
  "no_speech_prob": 0.0006612985162064433}, {"id": 1053, "seek": 324278, "start":
  3259.86, "end": 3261.2200000000003, "text": " But this is the math here.", "tokens":
  [51218, 583, 341, 307, 264, 5221, 510, 13, 51286], "temperature": 0.0, "avg_logprob":
  -0.22591648931088654, "compression_ratio": 1.7508650519031141, "no_speech_prob":
  0.0006612985162064433}, {"id": 1054, "seek": 324278, "start": 3261.2200000000003,
  "end": 3264.1000000000004, "text": " That''s actually the easiest way to go from
  sparse to dense.", "tokens": [51286, 663, 311, 767, 264, 12889, 636, 281, 352, 490,
  637, 11668, 281, 18011, 13, 51430], "temperature": 0.0, "avg_logprob": -0.22591648931088654,
  "compression_ratio": 1.7508650519031141, "no_speech_prob": 0.0006612985162064433},
  {"id": 1055, "seek": 324278, "start": 3264.1000000000004, "end": 3267.46, "text":
  " The dense to sparse requires a semantic knowledge graph or similar.", "tokens":
  [51430, 440, 18011, 281, 637, 11668, 7029, 257, 47982, 3601, 4295, 420, 2531, 13,
  51598], "temperature": 0.0, "avg_logprob": -0.22591648931088654, "compression_ratio":
  1.7508650519031141, "no_speech_prob": 0.0006612985162064433}, {"id": 1056, "seek":
  324278, "start": 3268.42, "end": 3269.26, "text": " Awesome.", "tokens": [51646,
  10391, 13, 51688], "temperature": 0.0, "avg_logprob": -0.22591648931088654, "compression_ratio":
  1.7508650519031141, "no_speech_prob": 0.0006612985162064433}, {"id": 1057, "seek":
  324278, "start": 3269.26, "end": 3271.26, "text": " I hope this answers your question,
  Julen.", "tokens": [51688, 286, 1454, 341, 6338, 428, 1168, 11, 7174, 268, 13, 51788],
  "temperature": 0.0, "avg_logprob": -0.22591648931088654, "compression_ratio": 1.7508650519031141,
  "no_speech_prob": 0.0006612985162064433}, {"id": 1058, "seek": 327126, "start":
  3271.26, "end": 3276.46, "text": " I would not feel free to unmute and ask full
  of questions.", "tokens": [50364, 286, 576, 406, 841, 1737, 281, 41445, 293, 1029,
  1577, 295, 1651, 13, 50624], "temperature": 0.0, "avg_logprob": -0.3246119659725982,
  "compression_ratio": 1.5957446808510638, "no_speech_prob": 0.0066570378839969635},
  {"id": 1059, "seek": 327126, "start": 3276.46, "end": 3280.5, "text": " Otherwise,
  I''ll jump to the next one from Ursula.", "tokens": [50624, 10328, 11, 286, 603,
  3012, 281, 264, 958, 472, 490, 41303, 3780, 13, 50826], "temperature": 0.0, "avg_logprob":
  -0.3246119659725982, "compression_ratio": 1.5957446808510638, "no_speech_prob":
  0.0066570378839969635}, {"id": 1060, "seek": 327126, "start": 3280.5, "end": 3283.5800000000004,
  "text": " Do we build the inverted index and the forward index", "tokens": [50826,
  1144, 321, 1322, 264, 38969, 8186, 293, 264, 2128, 8186, 50980], "temperature":
  0.0, "avg_logprob": -0.3246119659725982, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.0066570378839969635}, {"id": 1061, "seek": 327126, "start":
  3283.5800000000004, "end": 3287.38, "text": " to build the knowledge graph using
  just some document chunks?", "tokens": [50980, 281, 1322, 264, 3601, 4295, 1228,
  445, 512, 4166, 24004, 30, 51170], "temperature": 0.0, "avg_logprob": -0.3246119659725982,
  "compression_ratio": 1.5957446808510638, "no_speech_prob": 0.0066570378839969635},
  {"id": 1062, "seek": 327126, "start": 3287.38, "end": 3290.42, "text": " Or do we
  need a much bigger document base to make it work?", "tokens": [51170, 1610, 360,
  321, 643, 257, 709, 3801, 4166, 3096, 281, 652, 309, 589, 30, 51322], "temperature":
  0.0, "avg_logprob": -0.3246119659725982, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.0066570378839969635}, {"id": 1063, "seek": 327126, "start":
  3291.6600000000003, "end": 3292.6200000000003, "text": " It''s a good question.",
  "tokens": [51384, 467, 311, 257, 665, 1168, 13, 51432], "temperature": 0.0, "avg_logprob":
  -0.3246119659725982, "compression_ratio": 1.5957446808510638, "no_speech_prob":
  0.0066570378839969635}, {"id": 1064, "seek": 327126, "start": 3292.6200000000003,
  "end": 3293.6600000000003, "text": " Mm-hmm.", "tokens": [51432, 8266, 12, 10250,
  13, 51484], "temperature": 0.0, "avg_logprob": -0.3246119659725982, "compression_ratio":
  1.5957446808510638, "no_speech_prob": 0.0066570378839969635}, {"id": 1065, "seek":
  327126, "start": 3293.6600000000003, "end": 3301.1400000000003, "text": " So the
  best way for semantic knowledge graph to work the best,", "tokens": [51484, 407,
  264, 1151, 636, 337, 47982, 3601, 4295, 281, 589, 264, 1151, 11, 51858], "temperature":
  0.0, "avg_logprob": -0.3246119659725982, "compression_ratio": 1.5957446808510638,
  "no_speech_prob": 0.0066570378839969635}, {"id": 1066, "seek": 330126, "start":
  3301.26, "end": 3307.1400000000003, "text": " you need to have overlaps of terms
  that across documents.", "tokens": [50364, 291, 643, 281, 362, 15986, 2382, 295,
  2115, 300, 2108, 8512, 13, 50658], "temperature": 0.0, "avg_logprob": -0.26547984073036596,
  "compression_ratio": 1.585, "no_speech_prob": 0.0027499250136315823}, {"id": 1067,
  "seek": 330126, "start": 3307.1400000000003, "end": 3311.5400000000004, "text":
  " Meaning, if I take something like stack exchange,", "tokens": [50658, 19948, 11,
  498, 286, 747, 746, 411, 8630, 7742, 11, 50878], "temperature": 0.0, "avg_logprob":
  -0.26547984073036596, "compression_ratio": 1.585, "no_speech_prob": 0.0027499250136315823},
  {"id": 1068, "seek": 330126, "start": 3311.5400000000004, "end": 3315.46, "text":
  " where there''s a bunch of topics being talked about,", "tokens": [50878, 689,
  456, 311, 257, 3840, 295, 8378, 885, 2825, 466, 11, 51074], "temperature": 0.0,
  "avg_logprob": -0.26547984073036596, "compression_ratio": 1.585, "no_speech_prob":
  0.0027499250136315823}, {"id": 1069, "seek": 330126, "start": 3315.46, "end": 3320.1400000000003,
  "text": " you''ll have lots of people who use the same words together and the same
  documents.", "tokens": [51074, 291, 603, 362, 3195, 295, 561, 567, 764, 264, 912,
  2283, 1214, 293, 264, 912, 8512, 13, 51308], "temperature": 0.0, "avg_logprob":
  -0.26547984073036596, "compression_ratio": 1.585, "no_speech_prob": 0.0027499250136315823},
  {"id": 1070, "seek": 330126, "start": 3320.1400000000003, "end": 3326.7400000000002,
  "text": " When that happens, you can easily find sets of terms that overlap commonly",
  "tokens": [51308, 1133, 300, 2314, 11, 291, 393, 3612, 915, 6352, 295, 2115, 300,
  19959, 12719, 51638], "temperature": 0.0, "avg_logprob": -0.26547984073036596, "compression_ratio":
  1.585, "no_speech_prob": 0.0027499250136315823}, {"id": 1071, "seek": 332674, "start":
  3326.74, "end": 3331.2599999999998, "text": " and use the semantic knowledge graph
  to generate semantic understanding", "tokens": [50364, 293, 764, 264, 47982, 3601,
  4295, 281, 8460, 47982, 3701, 50590], "temperature": 0.0, "avg_logprob": -0.21526068084093988,
  "compression_ratio": 1.6872586872586872, "no_speech_prob": 0.003010509768500924},
  {"id": 1072, "seek": 332674, "start": 3331.2599999999998, "end": 3333.8599999999997,
  "text": " and relationships based upon those co-occurrences.", "tokens": [50590,
  293, 6159, 2361, 3564, 729, 598, 12, 905, 14112, 38983, 13, 50720], "temperature":
  0.0, "avg_logprob": -0.21526068084093988, "compression_ratio": 1.6872586872586872,
  "no_speech_prob": 0.003010509768500924}, {"id": 1073, "seek": 332674, "start": 3333.8599999999997,
  "end": 3337.02, "text": " All the math for that''s in the AI powered search book,",
  "tokens": [50720, 1057, 264, 5221, 337, 300, 311, 294, 264, 7318, 17786, 3164, 1446,
  11, 50878], "temperature": 0.0, "avg_logprob": -0.21526068084093988, "compression_ratio":
  1.6872586872586872, "no_speech_prob": 0.003010509768500924}, {"id": 1074, "seek":
  332674, "start": 3337.02, "end": 3341.4599999999996, "text": " but that''s when
  it works the best.", "tokens": [50878, 457, 300, 311, 562, 309, 1985, 264, 1151,
  13, 51100], "temperature": 0.0, "avg_logprob": -0.21526068084093988, "compression_ratio":
  1.6872586872586872, "no_speech_prob": 0.003010509768500924}, {"id": 1075, "seek":
  332674, "start": 3341.4599999999996, "end": 3345.22, "text": " Something like Wikipedia
  is actually even though it''s commonly used", "tokens": [51100, 6595, 411, 28999,
  307, 767, 754, 1673, 309, 311, 12719, 1143, 51288], "temperature": 0.0, "avg_logprob":
  -0.21526068084093988, "compression_ratio": 1.6872586872586872, "no_speech_prob":
  0.003010509768500924}, {"id": 1076, "seek": 332674, "start": 3345.22, "end": 3348.4599999999996,
  "text": " for every data science project.", "tokens": [51288, 337, 633, 1412, 3497,
  1716, 13, 51450], "temperature": 0.0, "avg_logprob": -0.21526068084093988, "compression_ratio":
  1.6872586872586872, "no_speech_prob": 0.003010509768500924}, {"id": 1077, "seek":
  332674, "start": 3348.4599999999996, "end": 3350.62, "text": " It''s actually really
  bad for semantic knowledge graphs", "tokens": [51450, 467, 311, 767, 534, 1578,
  337, 47982, 3601, 24877, 51558], "temperature": 0.0, "avg_logprob": -0.21526068084093988,
  "compression_ratio": 1.6872586872586872, "no_speech_prob": 0.003010509768500924},
  {"id": 1078, "seek": 332674, "start": 3350.62, "end": 3355.74, "text": " because
  every Wikipedia document tends to be about a particular topic", "tokens": [51558,
  570, 633, 28999, 4166, 12258, 281, 312, 466, 257, 1729, 4829, 51814], "temperature":
  0.0, "avg_logprob": -0.21526068084093988, "compression_ratio": 1.6872586872586872,
  "no_speech_prob": 0.003010509768500924}, {"id": 1079, "seek": 335574, "start": 3355.74,
  "end": 3358.62, "text": " and other than common terminology,", "tokens": [50364,
  293, 661, 813, 2689, 27575, 11, 50508], "temperature": 0.0, "avg_logprob": -0.1441986051380125,
  "compression_ratio": 1.803088803088803, "no_speech_prob": 0.0001800281897885725},
  {"id": 1080, "seek": 335574, "start": 3358.62, "end": 3361.4199999999996, "text":
  " you tend to not have a lot of overlap across documents", "tokens": [50508, 291,
  3928, 281, 406, 362, 257, 688, 295, 19959, 2108, 8512, 50648], "temperature": 0.0,
  "avg_logprob": -0.1441986051380125, "compression_ratio": 1.803088803088803, "no_speech_prob":
  0.0001800281897885725}, {"id": 1081, "seek": 335574, "start": 3361.4199999999996,
  "end": 3362.9799999999996, "text": " because they''re all focused on one idea.",
  "tokens": [50648, 570, 436, 434, 439, 5178, 322, 472, 1558, 13, 50726], "temperature":
  0.0, "avg_logprob": -0.1441986051380125, "compression_ratio": 1.803088803088803,
  "no_speech_prob": 0.0001800281897885725}, {"id": 1082, "seek": 335574, "start":
  3362.9799999999996, "end": 3366.4599999999996, "text": " So for semantic knowledge
  graph to work well,", "tokens": [50726, 407, 337, 47982, 3601, 4295, 281, 589, 731,
  11, 50900], "temperature": 0.0, "avg_logprob": -0.1441986051380125, "compression_ratio":
  1.803088803088803, "no_speech_prob": 0.0001800281897885725}, {"id": 1083, "seek":
  335574, "start": 3366.4599999999996, "end": 3370.2999999999997, "text": " you typically
  are going to want to have overlap across your documents.", "tokens": [50900, 291,
  5850, 366, 516, 281, 528, 281, 362, 19959, 2108, 428, 8512, 13, 51092], "temperature":
  0.0, "avg_logprob": -0.1441986051380125, "compression_ratio": 1.803088803088803,
  "no_speech_prob": 0.0001800281897885725}, {"id": 1084, "seek": 335574, "start":
  3370.2999999999997, "end": 3375.2599999999998, "text": " What that means is that
  if you chunk your document so small", "tokens": [51092, 708, 300, 1355, 307, 300,
  498, 291, 16635, 428, 4166, 370, 1359, 51340], "temperature": 0.0, "avg_logprob":
  -0.1441986051380125, "compression_ratio": 1.803088803088803, "no_speech_prob": 0.0001800281897885725},
  {"id": 1085, "seek": 335574, "start": 3375.2599999999998, "end": 3379.54, "text":
  " that you only have a couple of words or sentences or something like that,", "tokens":
  [51340, 300, 291, 787, 362, 257, 1916, 295, 2283, 420, 16579, 420, 746, 411, 300,
  11, 51554], "temperature": 0.0, "avg_logprob": -0.1441986051380125, "compression_ratio":
  1.803088803088803, "no_speech_prob": 0.0001800281897885725}, {"id": 1086, "seek":
  335574, "start": 3379.54, "end": 3381.7, "text": " you lose a lot of that context.",
  "tokens": [51554, 291, 3624, 257, 688, 295, 300, 4319, 13, 51662], "temperature":
  0.0, "avg_logprob": -0.1441986051380125, "compression_ratio": 1.803088803088803,
  "no_speech_prob": 0.0001800281897885725}, {"id": 1087, "seek": 335574, "start":
  3381.7, "end": 3383.9799999999996, "text": " I mean, in general, when you chunk,
  you lose context.", "tokens": [51662, 286, 914, 11, 294, 2674, 11, 562, 291, 16635,
  11, 291, 3624, 4319, 13, 51776], "temperature": 0.0, "avg_logprob": -0.1441986051380125,
  "compression_ratio": 1.803088803088803, "no_speech_prob": 0.0001800281897885725},
  {"id": 1088, "seek": 338398, "start": 3383.98, "end": 3387.26, "text": " That''s
  the problem with chunking, with most forms of chunking.", "tokens": [50364, 663,
  311, 264, 1154, 365, 16635, 278, 11, 365, 881, 6422, 295, 16635, 278, 13, 50528],
  "temperature": 0.0, "avg_logprob": -0.16659028412865812, "compression_ratio": 1.673913043478261,
  "no_speech_prob": 0.004153615795075893}, {"id": 1089, "seek": 338398, "start": 3387.26,
  "end": 3389.98, "text": " And so you have to be careful not to chunk too much,",
  "tokens": [50528, 400, 370, 291, 362, 281, 312, 5026, 406, 281, 16635, 886, 709,
  11, 50664], "temperature": 0.0, "avg_logprob": -0.16659028412865812, "compression_ratio":
  1.673913043478261, "no_speech_prob": 0.004153615795075893}, {"id": 1090, "seek":
  338398, "start": 3389.98, "end": 3394.9, "text": " but the end verse is also true
  if you only have 100 documents", "tokens": [50664, 457, 264, 917, 7996, 307, 611,
  2074, 498, 291, 787, 362, 2319, 8512, 50910], "temperature": 0.0, "avg_logprob":
  -0.16659028412865812, "compression_ratio": 1.673913043478261, "no_speech_prob":
  0.004153615795075893}, {"id": 1091, "seek": 338398, "start": 3394.9, "end": 3397.7,
  "text": " and every single one of them is 1,000 pages long,", "tokens": [50910,
  293, 633, 2167, 472, 295, 552, 307, 502, 11, 1360, 7183, 938, 11, 51050], "temperature":
  0.0, "avg_logprob": -0.16659028412865812, "compression_ratio": 1.673913043478261,
  "no_speech_prob": 0.004153615795075893}, {"id": 1092, "seek": 338398, "start": 3397.7,
  "end": 3399.26, "text": " well, there''s way too much overlap", "tokens": [51050,
  731, 11, 456, 311, 636, 886, 709, 19959, 51128], "temperature": 0.0, "avg_logprob":
  -0.16659028412865812, "compression_ratio": 1.673913043478261, "no_speech_prob":
  0.004153615795075893}, {"id": 1093, "seek": 338398, "start": 3399.26, "end": 3400.78,
  "text": " and everything is related at that point.", "tokens": [51128, 293, 1203,
  307, 4077, 412, 300, 935, 13, 51204], "temperature": 0.0, "avg_logprob": -0.16659028412865812,
  "compression_ratio": 1.673913043478261, "no_speech_prob": 0.004153615795075893},
  {"id": 1094, "seek": 338398, "start": 3400.78, "end": 3405.02, "text": " So I would
  say it''s no different than just how you would typically", "tokens": [51204, 407,
  286, 576, 584, 309, 311, 572, 819, 813, 445, 577, 291, 576, 5850, 51416], "temperature":
  0.0, "avg_logprob": -0.16659028412865812, "compression_ratio": 1.673913043478261,
  "no_speech_prob": 0.004153615795075893}, {"id": 1095, "seek": 338398, "start": 3405.02,
  "end": 3407.66, "text": " segment your documents for any search problem.", "tokens":
  [51416, 9469, 428, 8512, 337, 604, 3164, 1154, 13, 51548], "temperature": 0.0, "avg_logprob":
  -0.16659028412865812, "compression_ratio": 1.673913043478261, "no_speech_prob":
  0.004153615795075893}, {"id": 1096, "seek": 338398, "start": 3407.66, "end": 3411.38,
  "text": " You need to be granular enough to be useful,", "tokens": [51548, 509,
  643, 281, 312, 39962, 1547, 281, 312, 4420, 11, 51734], "temperature": 0.0, "avg_logprob":
  -0.16659028412865812, "compression_ratio": 1.673913043478261, "no_speech_prob":
  0.004153615795075893}, {"id": 1097, "seek": 341138, "start": 3411.46, "end": 3416.38,
  "text": " but not broad enough to be too general.", "tokens": [50368, 457, 406,
  4152, 1547, 281, 312, 886, 2674, 13, 50614], "temperature": 0.0, "avg_logprob":
  -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1098, "seek": 341138, "start": 3416.38, "end": 3417.54,
  "text": " Yeah, awesome.", "tokens": [50614, 865, 11, 3476, 13, 50672], "temperature":
  0.0, "avg_logprob": -0.25470991868239184, "compression_ratio": 1.6840148698884758,
  "no_speech_prob": 0.014531845226883888}, {"id": 1099, "seek": 341138, "start": 3417.54,
  "end": 3419.9, "text": " And now the logistical question from Arun,", "tokens":
  [50672, 400, 586, 264, 3565, 42686, 1168, 490, 1587, 409, 11, 50790], "temperature":
  0.0, "avg_logprob": -0.25470991868239184, "compression_ratio": 1.6840148698884758,
  "no_speech_prob": 0.014531845226883888}, {"id": 1100, "seek": 341138, "start": 3419.9,
  "end": 3422.46, "text": " whether we will share slides.", "tokens": [50790, 1968,
  321, 486, 2073, 9788, 13, 50918], "temperature": 0.0, "avg_logprob": -0.25470991868239184,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.014531845226883888},
  {"id": 1101, "seek": 341138, "start": 3422.46, "end": 3423.62, "text": " Yes, absolutely.",
  "tokens": [50918, 1079, 11, 3122, 13, 50976], "temperature": 0.0, "avg_logprob":
  -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1102, "seek": 341138, "start": 3423.62, "end": 3426.7400000000002,
  "text": " Yeah, the video for this, everybody who signed up", "tokens": [50976,
  865, 11, 264, 960, 337, 341, 11, 2201, 567, 8175, 493, 51132], "temperature": 0.0,
  "avg_logprob": -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1103, "seek": 341138, "start": 3426.7400000000002,
  "end": 3428.78, "text": " will get in probably like 48 hours,", "tokens": [51132,
  486, 483, 294, 1391, 411, 11174, 2496, 11, 51234], "temperature": 0.0, "avg_logprob":
  -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1104, "seek": 341138, "start": 3428.78, "end": 3430.3,
  "text": " you''ll get emailed a copy of the video,", "tokens": [51234, 291, 603,
  483, 3796, 292, 257, 5055, 295, 264, 960, 11, 51310], "temperature": 0.0, "avg_logprob":
  -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1105, "seek": 341138, "start": 3430.3, "end": 3431.3,
  "text": " so you can refer back to it.", "tokens": [51310, 370, 291, 393, 2864,
  646, 281, 309, 13, 51360], "temperature": 0.0, "avg_logprob": -0.25470991868239184,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.014531845226883888},
  {"id": 1106, "seek": 341138, "start": 3431.3, "end": 3435.54, "text": " And I''ll
  also send an email with the slides probably shortly thereafter.", "tokens": [51360,
  400, 286, 603, 611, 2845, 364, 3796, 365, 264, 9788, 1391, 13392, 38729, 13, 51572],
  "temperature": 0.0, "avg_logprob": -0.25470991868239184, "compression_ratio": 1.6840148698884758,
  "no_speech_prob": 0.014531845226883888}, {"id": 1107, "seek": 341138, "start": 3435.54,
  "end": 3439.54, "text": " Yeah, and I plan to publish this in the vector podcast
  as well.", "tokens": [51572, 865, 11, 293, 286, 1393, 281, 11374, 341, 294, 264,
  8062, 7367, 382, 731, 13, 51772], "temperature": 0.0, "avg_logprob": -0.25470991868239184,
  "compression_ratio": 1.6840148698884758, "no_speech_prob": 0.014531845226883888},
  {"id": 1108, "seek": 341138, "start": 3439.54, "end": 3440.82, "text": " Yes, absolutely.",
  "tokens": [51772, 1079, 11, 3122, 13, 51836], "temperature": 0.0, "avg_logprob":
  -0.25470991868239184, "compression_ratio": 1.6840148698884758, "no_speech_prob":
  0.014531845226883888}, {"id": 1109, "seek": 344082, "start": 3440.82, "end": 3443.34,
  "text": " I''ll follow up later.", "tokens": [50364, 286, 603, 1524, 493, 1780,
  13, 50490], "temperature": 0.0, "avg_logprob": -0.23563863314115086, "compression_ratio":
  1.7216117216117217, "no_speech_prob": 0.03407295420765877}, {"id": 1110, "seek":
  344082, "start": 3443.34, "end": 3445.5, "text": " The next question is really cool
  from Cloud.", "tokens": [50490, 440, 958, 1168, 307, 534, 1627, 490, 8061, 13, 50598],
  "temperature": 0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1111, "seek": 344082, "start": 3445.5,
  "end": 3450.34, "text": " You''re creating a wormhole vector that will move us from
  embedding space", "tokens": [50598, 509, 434, 4084, 257, 23835, 14094, 8062, 300,
  486, 1286, 505, 490, 12240, 3584, 1901, 50840], "temperature": 0.0, "avg_logprob":
  -0.23563863314115086, "compression_ratio": 1.7216117216117217, "no_speech_prob":
  0.03407295420765877}, {"id": 1112, "seek": 344082, "start": 3450.34, "end": 3452.06,
  "text": " to sparse vector.", "tokens": [50840, 281, 637, 11668, 8062, 13, 50926],
  "temperature": 0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1113, "seek": 344082, "start": 3452.06,
  "end": 3454.5, "text": " I understand the methodology, but the way back now,", "tokens":
  [50926, 286, 1223, 264, 24850, 11, 457, 264, 636, 646, 586, 11, 51048], "temperature":
  0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1114, "seek": 344082, "start": 3454.5,
  "end": 3457.38, "text": " how do we aggregate a set of sparse vectors", "tokens":
  [51048, 577, 360, 321, 26118, 257, 992, 295, 637, 11668, 18875, 51192], "temperature":
  0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1115, "seek": 344082, "start": 3457.38,
  "end": 3460.78, "text": " that represent documents in a way that will allow us to
  move us", "tokens": [51192, 300, 2906, 8512, 294, 257, 636, 300, 486, 2089, 505,
  281, 1286, 505, 51362], "temperature": 0.0, "avg_logprob": -0.23563863314115086,
  "compression_ratio": 1.7216117216117217, "no_speech_prob": 0.03407295420765877},
  {"id": 1116, "seek": 344082, "start": 3460.78, "end": 3461.86, "text": " to the
  embedding space?", "tokens": [51362, 281, 264, 12240, 3584, 1901, 30, 51416], "temperature":
  0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1117, "seek": 344082, "start": 3461.86,
  "end": 3464.94, "text": " In other words, from the sparse, like you showed the tray,",
  "tokens": [51416, 682, 661, 2283, 11, 490, 264, 637, 11668, 11, 411, 291, 4712,
  264, 16027, 11, 51570], "temperature": 0.0, "avg_logprob": -0.23563863314115086,
  "compression_ratio": 1.7216117216117217, "no_speech_prob": 0.03407295420765877},
  {"id": 1118, "seek": 344082, "start": 3464.94, "end": 3467.06, "text": " we have
  millions of dimensions, right?", "tokens": [51570, 321, 362, 6803, 295, 12819, 11,
  558, 30, 51676], "temperature": 0.0, "avg_logprob": -0.23563863314115086, "compression_ratio":
  1.7216117216117217, "no_speech_prob": 0.03407295420765877}, {"id": 1119, "seek":
  344082, "start": 3467.06, "end": 3469.98, "text": " How do we compact that, right?",
  "tokens": [51676, 1012, 360, 321, 14679, 300, 11, 558, 30, 51822], "temperature":
  0.0, "avg_logprob": -0.23563863314115086, "compression_ratio": 1.7216117216117217,
  "no_speech_prob": 0.03407295420765877}, {"id": 1120, "seek": 346998, "start": 3469.98,
  "end": 3472.9, "text": " And don''t lose anything and don''t introduce any noise",
  "tokens": [50364, 400, 500, 380, 3624, 1340, 293, 500, 380, 5366, 604, 5658, 50510],
  "temperature": 0.0, "avg_logprob": -0.18355014181544638, "compression_ratio": 1.653386454183267,
  "no_speech_prob": 0.00017973485228139907}, {"id": 1121, "seek": 346998, "start":
  3472.9, "end": 3475.54, "text": " when we''re not way to the dense space?", "tokens":
  [50510, 562, 321, 434, 406, 636, 281, 264, 18011, 1901, 30, 50642], "temperature":
  0.0, "avg_logprob": -0.18355014181544638, "compression_ratio": 1.653386454183267,
  "no_speech_prob": 0.00017973485228139907}, {"id": 1122, "seek": 346998, "start":
  3475.54, "end": 3477.42, "text": " Yeah, so it''s a really great question.", "tokens":
  [50642, 865, 11, 370, 309, 311, 257, 534, 869, 1168, 13, 50736], "temperature":
  0.0, "avg_logprob": -0.18355014181544638, "compression_ratio": 1.653386454183267,
  "no_speech_prob": 0.00017973485228139907}, {"id": 1123, "seek": 346998, "start":
  3477.42, "end": 3479.5, "text": " I answered it technically in terms of pulling,",
  "tokens": [50736, 286, 10103, 309, 12120, 294, 2115, 295, 8407, 11, 50840], "temperature":
  0.0, "avg_logprob": -0.18355014181544638, "compression_ratio": 1.653386454183267,
  "no_speech_prob": 0.00017973485228139907}, {"id": 1124, "seek": 346998, "start":
  3479.5, "end": 3482.06, "text": " but let me add some color to it in terms of techniques.",
  "tokens": [50840, 457, 718, 385, 909, 512, 2017, 281, 309, 294, 2115, 295, 7512,
  13, 50968], "temperature": 0.0, "avg_logprob": -0.18355014181544638, "compression_ratio":
  1.653386454183267, "no_speech_prob": 0.00017973485228139907}, {"id": 1125, "seek":
  346998, "start": 3482.06, "end": 3484.06, "text": " So the...", "tokens": [50968,
  407, 264, 485, 51068], "temperature": 0.0, "avg_logprob": -0.18355014181544638,
  "compression_ratio": 1.653386454183267, "no_speech_prob": 0.00017973485228139907},
  {"id": 1126, "seek": 346998, "start": 3486.02, "end": 3486.98, "text": " There''s
  a couple of things here.", "tokens": [51166, 821, 311, 257, 1916, 295, 721, 510,
  13, 51214], "temperature": 0.0, "avg_logprob": -0.18355014181544638, "compression_ratio":
  1.653386454183267, "no_speech_prob": 0.00017973485228139907}, {"id": 1127, "seek":
  346998, "start": 3486.98, "end": 3491.54, "text": " One, whenever you''re querying
  in an inverted index,", "tokens": [51214, 1485, 11, 5699, 291, 434, 7083, 1840,
  294, 364, 38969, 8186, 11, 51442], "temperature": 0.0, "avg_logprob": -0.18355014181544638,
  "compression_ratio": 1.653386454183267, "no_speech_prob": 0.00017973485228139907},
  {"id": 1128, "seek": 346998, "start": 3491.54, "end": 3495.66, "text": " there''s
  typically a kind of Boolean matching phase,", "tokens": [51442, 456, 311, 5850,
  257, 733, 295, 23351, 28499, 14324, 5574, 11, 51648], "temperature": 0.0, "avg_logprob":
  -0.18355014181544638, "compression_ratio": 1.653386454183267, "no_speech_prob":
  0.00017973485228139907}, {"id": 1129, "seek": 346998, "start": 3495.66, "end": 3497.22,
  "text": " and then there''s a ranking phase,", "tokens": [51648, 293, 550, 456,
  311, 257, 17833, 5574, 11, 51726], "temperature": 0.0, "avg_logprob": -0.18355014181544638,
  "compression_ratio": 1.653386454183267, "no_speech_prob": 0.00017973485228139907},
  {"id": 1130, "seek": 349722, "start": 3497.22, "end": 3500.54, "text": " meaning
  if you had 10 million documents in your index,", "tokens": [50364, 3620, 498, 291,
  632, 1266, 2459, 8512, 294, 428, 8186, 11, 50530], "temperature": 0.0, "avg_logprob":
  -0.17541495103102464, "compression_ratio": 1.8815331010452963, "no_speech_prob":
  0.004542068112641573}, {"id": 1131, "seek": 349722, "start": 3500.54, "end": 3503.9399999999996,
  "text": " you''re not gonna return a ranked list of 10 million documents.", "tokens":
  [50530, 291, 434, 406, 799, 2736, 257, 20197, 1329, 295, 1266, 2459, 8512, 13, 50700],
  "temperature": 0.0, "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963,
  "no_speech_prob": 0.004542068112641573}, {"id": 1132, "seek": 349722, "start": 3503.9399999999996,
  "end": 3505.3799999999997, "text": " You''re gonna probably return the documents",
  "tokens": [50700, 509, 434, 799, 1391, 2736, 264, 8512, 50772], "temperature": 0.0,
  "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963, "no_speech_prob":
  0.004542068112641573}, {"id": 1133, "seek": 349722, "start": 3505.3799999999997,
  "end": 3507.8999999999996, "text": " that have the specific keywords you search
  for,", "tokens": [50772, 300, 362, 264, 2685, 21009, 291, 3164, 337, 11, 50898],
  "temperature": 0.0, "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963,
  "no_speech_prob": 0.004542068112641573}, {"id": 1134, "seek": 349722, "start": 3507.8999999999996,
  "end": 3510.14, "text": " which is gonna be a much smaller document set.", "tokens":
  [50898, 597, 307, 799, 312, 257, 709, 4356, 4166, 992, 13, 51010], "temperature":
  0.0, "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963,
  "no_speech_prob": 0.004542068112641573}, {"id": 1135, "seek": 349722, "start": 3511.18,
  "end": 3512.02, "text": " And so that''s...", "tokens": [51062, 400, 370, 300, 311,
  485, 51104], "temperature": 0.0, "avg_logprob": -0.17541495103102464, "compression_ratio":
  1.8815331010452963, "no_speech_prob": 0.004542068112641573}, {"id": 1136, "seek":
  349722, "start": 3512.02, "end": 3513.54, "text": " And you can do the same thing
  on the dense side", "tokens": [51104, 400, 291, 393, 360, 264, 912, 551, 322, 264,
  18011, 1252, 51180], "temperature": 0.0, "avg_logprob": -0.17541495103102464, "compression_ratio":
  1.8815331010452963, "no_speech_prob": 0.004542068112641573}, {"id": 1137, "seek":
  349722, "start": 3513.54, "end": 3516.8999999999996, "text": " with cutoffs on cosine
  similarity or something like that.", "tokens": [51180, 365, 1723, 19231, 322, 23565,
  32194, 420, 746, 411, 300, 13, 51348], "temperature": 0.0, "avg_logprob": -0.17541495103102464,
  "compression_ratio": 1.8815331010452963, "no_speech_prob": 0.004542068112641573},
  {"id": 1138, "seek": 349722, "start": 3516.8999999999996, "end": 3521.8999999999996,
  "text": " But, the step one is you start with a condensed document set", "tokens":
  [51348, 583, 11, 264, 1823, 472, 307, 291, 722, 365, 257, 36398, 4166, 992, 51598],
  "temperature": 0.0, "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963,
  "no_speech_prob": 0.004542068112641573}, {"id": 1139, "seek": 349722, "start": 3522.18,
  "end": 3524.18, "text": " that should represent generally the meaning", "tokens":
  [51612, 300, 820, 2906, 5101, 264, 3620, 51712], "temperature": 0.0, "avg_logprob":
  -0.17541495103102464, "compression_ratio": 1.8815331010452963, "no_speech_prob":
  0.004542068112641573}, {"id": 1140, "seek": 349722, "start": 3524.18, "end": 3526.9399999999996,
  "text": " of what you searched for using the keywords you searched", "tokens": [51712,
  295, 437, 291, 22961, 337, 1228, 264, 21009, 291, 22961, 51850], "temperature":
  0.0, "avg_logprob": -0.17541495103102464, "compression_ratio": 1.8815331010452963,
  "no_speech_prob": 0.004542068112641573}, {"id": 1141, "seek": 352694, "start": 3526.98,
  "end": 3528.42, "text": " from the lexical side.", "tokens": [50366, 490, 264, 476,
  87, 804, 1252, 13, 50438], "temperature": 0.0, "avg_logprob": -0.14011366536298137,
  "compression_ratio": 1.7424242424242424, "no_speech_prob": 0.0026540064718574286},
  {"id": 1142, "seek": 352694, "start": 3528.42, "end": 3532.26, "text": " However,
  because the idea of a wormhole vector", "tokens": [50438, 2908, 11, 570, 264, 1558,
  295, 257, 23835, 14094, 8062, 50630], "temperature": 0.0, "avg_logprob": -0.14011366536298137,
  "compression_ratio": 1.7424242424242424, "no_speech_prob": 0.0026540064718574286},
  {"id": 1143, "seek": 352694, "start": 3532.26, "end": 3536.14, "text": " is to find
  the best corresponding region", "tokens": [50630, 307, 281, 915, 264, 1151, 11760,
  4458, 50824], "temperature": 0.0, "avg_logprob": -0.14011366536298137, "compression_ratio":
  1.7424242424242424, "no_speech_prob": 0.0026540064718574286}, {"id": 1144, "seek":
  352694, "start": 3536.14, "end": 3538.54, "text": " in the other semantic space,",
  "tokens": [50824, 294, 264, 661, 47982, 1901, 11, 50944], "temperature": 0.0, "avg_logprob":
  -0.14011366536298137, "compression_ratio": 1.7424242424242424, "no_speech_prob":
  0.0026540064718574286}, {"id": 1145, "seek": 352694, "start": 3538.54, "end": 3541.94,
  "text": " it can often be useful to not take that entire document set,", "tokens":
  [50944, 309, 393, 2049, 312, 4420, 281, 406, 747, 300, 2302, 4166, 992, 11, 51114],
  "temperature": 0.0, "avg_logprob": -0.14011366536298137, "compression_ratio": 1.7424242424242424,
  "no_speech_prob": 0.0026540064718574286}, {"id": 1146, "seek": 352694, "start":
  3541.94, "end": 3543.26, "text": " either matching the query,", "tokens": [51114,
  2139, 14324, 264, 14581, 11, 51180], "temperature": 0.0, "avg_logprob": -0.14011366536298137,
  "compression_ratio": 1.7424242424242424, "no_speech_prob": 0.0026540064718574286},
  {"id": 1147, "seek": 352694, "start": 3543.26, "end": 3545.78, "text": " but if
  you feel confident about your ranking,", "tokens": [51180, 457, 498, 291, 841, 6679,
  466, 428, 17833, 11, 51306], "temperature": 0.0, "avg_logprob": -0.14011366536298137,
  "compression_ratio": 1.7424242424242424, "no_speech_prob": 0.0026540064718574286},
  {"id": 1148, "seek": 352694, "start": 3545.78, "end": 3547.5, "text": " then you
  can take the top end document.", "tokens": [51306, 550, 291, 393, 747, 264, 1192,
  917, 4166, 13, 51392], "temperature": 0.0, "avg_logprob": -0.14011366536298137,
  "compression_ratio": 1.7424242424242424, "no_speech_prob": 0.0026540064718574286},
  {"id": 1149, "seek": 352694, "start": 3547.5, "end": 3549.78, "text": " So maybe
  you match 10,000,", "tokens": [51392, 407, 1310, 291, 2995, 1266, 11, 1360, 11,
  51506], "temperature": 0.0, "avg_logprob": -0.14011366536298137, "compression_ratio":
  1.7424242424242424, "no_speech_prob": 0.0026540064718574286}, {"id": 1150, "seek":
  352694, "start": 3549.78, "end": 3551.1, "text": " and maybe you only take the top
  hundred", "tokens": [51506, 293, 1310, 291, 787, 747, 264, 1192, 3262, 51572], "temperature":
  0.0, "avg_logprob": -0.14011366536298137, "compression_ratio": 1.7424242424242424,
  "no_speech_prob": 0.0026540064718574286}, {"id": 1151, "seek": 352694, "start":
  3551.1, "end": 3552.62, "text": " and say, hey, from the top hundred,", "tokens":
  [51572, 293, 584, 11, 4177, 11, 490, 264, 1192, 3262, 11, 51648], "temperature":
  0.0, "avg_logprob": -0.14011366536298137, "compression_ratio": 1.7424242424242424,
  "no_speech_prob": 0.0026540064718574286}, {"id": 1152, "seek": 352694, "start":
  3552.62, "end": 3554.86, "text": " if you know your relevance ranking is good,",
  "tokens": [51648, 498, 291, 458, 428, 32684, 17833, 307, 665, 11, 51760], "temperature":
  0.0, "avg_logprob": -0.14011366536298137, "compression_ratio": 1.7424242424242424,
  "no_speech_prob": 0.0026540064718574286}, {"id": 1153, "seek": 355486, "start":
  3554.86, "end": 3558.1400000000003, "text": " then you''re gonna use that to generate
  a more precise wormhole", "tokens": [50364, 550, 291, 434, 799, 764, 300, 281, 8460,
  257, 544, 13600, 23835, 14094, 50528], "temperature": 0.0, "avg_logprob": -0.13648429630309578,
  "compression_ratio": 1.8841698841698842, "no_speech_prob": 0.00020072469487786293},
  {"id": 1154, "seek": 355486, "start": 3558.1400000000003, "end": 3560.54, "text":
  " vector to the meaning of those top documents", "tokens": [50528, 8062, 281, 264,
  3620, 295, 729, 1192, 8512, 50648], "temperature": 0.0, "avg_logprob": -0.13648429630309578,
  "compression_ratio": 1.8841698841698842, "no_speech_prob": 0.00020072469487786293},
  {"id": 1155, "seek": 355486, "start": 3560.54, "end": 3562.02, "text": " over to
  the dense space.", "tokens": [50648, 670, 281, 264, 18011, 1901, 13, 50722], "temperature":
  0.0, "avg_logprob": -0.13648429630309578, "compression_ratio": 1.8841698841698842,
  "no_speech_prob": 0.00020072469487786293}, {"id": 1156, "seek": 355486, "start":
  3562.02, "end": 3566.02, "text": " So, whether you go with the full matching document
  set,", "tokens": [50722, 407, 11, 1968, 291, 352, 365, 264, 1577, 14324, 4166, 992,
  11, 50922], "temperature": 0.0, "avg_logprob": -0.13648429630309578, "compression_ratio":
  1.8841698841698842, "no_speech_prob": 0.00020072469487786293}, {"id": 1157, "seek":
  355486, "start": 3566.02, "end": 3568.02, "text": " or you go with the top end,",
  "tokens": [50922, 420, 291, 352, 365, 264, 1192, 917, 11, 51022], "temperature":
  0.0, "avg_logprob": -0.13648429630309578, "compression_ratio": 1.8841698841698842,
  "no_speech_prob": 0.00020072469487786293}, {"id": 1158, "seek": 355486, "start":
  3568.02, "end": 3570.1, "text": " that''s really a just practical matter", "tokens":
  [51022, 300, 311, 534, 257, 445, 8496, 1871, 51126], "temperature": 0.0, "avg_logprob":
  -0.13648429630309578, "compression_ratio": 1.8841698841698842, "no_speech_prob":
  0.00020072469487786293}, {"id": 1159, "seek": 355486, "start": 3570.1, "end": 3572.2200000000003,
  "text": " of how confident you are on the ranking.", "tokens": [51126, 295, 577,
  6679, 291, 366, 322, 264, 17833, 13, 51232], "temperature": 0.0, "avg_logprob":
  -0.13648429630309578, "compression_ratio": 1.8841698841698842, "no_speech_prob":
  0.00020072469487786293}, {"id": 1160, "seek": 355486, "start": 3572.2200000000003,
  "end": 3574.78, "text": " If you''re really confident in your relevance,", "tokens":
  [51232, 759, 291, 434, 534, 6679, 294, 428, 32684, 11, 51360], "temperature": 0.0,
  "avg_logprob": -0.13648429630309578, "compression_ratio": 1.8841698841698842, "no_speech_prob":
  0.00020072469487786293}, {"id": 1161, "seek": 355486, "start": 3574.78, "end": 3576.6200000000003,
  "text": " you should go with the more relevant documents.", "tokens": [51360, 291,
  820, 352, 365, 264, 544, 7340, 8512, 13, 51452], "temperature": 0.0, "avg_logprob":
  -0.13648429630309578, "compression_ratio": 1.8841698841698842, "no_speech_prob":
  0.00020072469487786293}, {"id": 1162, "seek": 355486, "start": 3576.6200000000003,
  "end": 3578.6600000000003, "text": " And if you''re not, just take the whole document
  set", "tokens": [51452, 400, 498, 291, 434, 406, 11, 445, 747, 264, 1379, 4166,
  992, 51554], "temperature": 0.0, "avg_logprob": -0.13648429630309578, "compression_ratio":
  1.8841698841698842, "no_speech_prob": 0.00020072469487786293}, {"id": 1163, "seek":
  355486, "start": 3578.6600000000003, "end": 3581.78, "text": " and it should sort
  of average out the meaning.", "tokens": [51554, 293, 309, 820, 1333, 295, 4274,
  484, 264, 3620, 13, 51710], "temperature": 0.0, "avg_logprob": -0.13648429630309578,
  "compression_ratio": 1.8841698841698842, "no_speech_prob": 0.00020072469487786293},
  {"id": 1164, "seek": 358178, "start": 3582.78, "end": 3585.26, "text": " One other
  thing that we didn''t really get into", "tokens": [50414, 1485, 661, 551, 300, 321,
  994, 380, 534, 483, 666, 50538], "temperature": 0.0, "avg_logprob": -0.27242630499380605,
  "compression_ratio": 1.3409090909090908, "no_speech_prob": 0.0033424245193600655},
  {"id": 1165, "seek": 358178, "start": 3585.26, "end": 3589.2200000000003, "text":
  " is that the strategy, the technique I was showing", "tokens": [50538, 307, 300,
  264, 5206, 11, 264, 6532, 286, 390, 4099, 50736], "temperature": 0.0, "avg_logprob":
  -0.27242630499380605, "compression_ratio": 1.3409090909090908, "no_speech_prob":
  0.0033424245193600655}, {"id": 1166, "seek": 358178, "start": 3589.2200000000003,
  "end": 3594.2200000000003, "text": " if I, let me jump back to the final slide one
  second.", "tokens": [50736, 498, 286, 11, 718, 385, 3012, 646, 281, 264, 2572, 4137,
  472, 1150, 13, 50986], "temperature": 0.0, "avg_logprob": -0.27242630499380605,
  "compression_ratio": 1.3409090909090908, "no_speech_prob": 0.0033424245193600655},
  {"id": 1167, "seek": 358178, "start": 3600.0600000000004, "end": 3601.78, "text":
  " If I jump back to...", "tokens": [51278, 759, 286, 3012, 646, 281, 485, 51364],
  "temperature": 0.0, "avg_logprob": -0.27242630499380605, "compression_ratio": 1.3409090909090908,
  "no_speech_prob": 0.0033424245193600655}, {"id": 1168, "seek": 358178, "start":
  3606.7400000000002, "end": 3607.5800000000004, "text": " Here.", "tokens": [51612,
  1692, 13, 51654], "temperature": 0.0, "avg_logprob": -0.27242630499380605, "compression_ratio":
  1.3409090909090908, "no_speech_prob": 0.0033424245193600655}, {"id": 1169, "seek":
  360758, "start": 3608.58, "end": 3611.8199999999997, "text": " So the technique
  that I''m showing,", "tokens": [50414, 407, 264, 6532, 300, 286, 478, 4099, 11,
  50576], "temperature": 0.0, "avg_logprob": -0.15337547011997388, "compression_ratio":
  1.6227272727272728, "no_speech_prob": 0.0016515774186700583}, {"id": 1170, "seek":
  360758, "start": 3611.8199999999997, "end": 3614.1, "text": " where I get my document
  set,", "tokens": [50576, 689, 286, 483, 452, 4166, 992, 11, 50690], "temperature":
  0.0, "avg_logprob": -0.15337547011997388, "compression_ratio": 1.6227272727272728,
  "no_speech_prob": 0.0016515774186700583}, {"id": 1171, "seek": 360758, "start":
  3614.1, "end": 3615.98, "text": " pull my embeddings together,", "tokens": [50690,
  2235, 452, 12240, 29432, 1214, 11, 50784], "temperature": 0.0, "avg_logprob": -0.15337547011997388,
  "compression_ratio": 1.6227272727272728, "no_speech_prob": 0.0016515774186700583},
  {"id": 1172, "seek": 360758, "start": 3615.98, "end": 3619.7, "text": " that ultimately
  gives me a single embedding,", "tokens": [50784, 300, 6284, 2709, 385, 257, 2167,
  12240, 3584, 11, 50970], "temperature": 0.0, "avg_logprob": -0.15337547011997388,
  "compression_ratio": 1.6227272727272728, "no_speech_prob": 0.0016515774186700583},
  {"id": 1173, "seek": 360758, "start": 3619.7, "end": 3623.58, "text": " which is
  a single point over here in my dense vector space.", "tokens": [50970, 597, 307,
  257, 2167, 935, 670, 510, 294, 452, 18011, 8062, 1901, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.15337547011997388, "compression_ratio": 1.6227272727272728,
  "no_speech_prob": 0.0016515774186700583}, {"id": 1174, "seek": 360758, "start":
  3623.58, "end": 3627.8199999999997, "text": " The reality is that different queries
  have different specificity.", "tokens": [51164, 440, 4103, 307, 300, 819, 24109,
  362, 819, 2685, 507, 13, 51376], "temperature": 0.0, "avg_logprob": -0.15337547011997388,
  "compression_ratio": 1.6227272727272728, "no_speech_prob": 0.0016515774186700583},
  {"id": 1175, "seek": 360758, "start": 3627.8199999999997, "end": 3630.62, "text":
  " So imagine this is like a job search engine.", "tokens": [51376, 407, 3811, 341,
  307, 411, 257, 1691, 3164, 2848, 13, 51516], "temperature": 0.0, "avg_logprob":
  -0.15337547011997388, "compression_ratio": 1.6227272727272728, "no_speech_prob":
  0.0016515774186700583}, {"id": 1176, "seek": 360758, "start": 3630.62, "end": 3635.62,
  "text": " If I run a search for senior AI search engineer,", "tokens": [51516, 759,
  286, 1190, 257, 3164, 337, 7965, 7318, 3164, 11403, 11, 51766], "temperature": 0.0,
  "avg_logprob": -0.15337547011997388, "compression_ratio": 1.6227272727272728, "no_speech_prob":
  0.0016515774186700583}, {"id": 1177, "seek": 363758, "start": 3638.58, "end": 3642.22,
  "text": " a late interaction, culverts,", "tokens": [50414, 257, 3469, 9285, 11,
  11021, 36999, 11, 50596], "temperature": 0.0, "avg_logprob": -0.1882278849777666,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0019133547320961952},
  {"id": 1178, "seek": 363758, "start": 3644.9, "end": 3647.7799999999997, "text":
  " signals boosting and collaborative filter.", "tokens": [50730, 12354, 43117, 293,
  16555, 6608, 13, 50874], "temperature": 0.0, "avg_logprob": -0.1882278849777666,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0019133547320961952},
  {"id": 1179, "seek": 363758, "start": 3647.7799999999997, "end": 3650.74, "text":
  " If I run that search, that''s a very specific search.", "tokens": [50874, 759,
  286, 1190, 300, 3164, 11, 300, 311, 257, 588, 2685, 3164, 13, 51022], "temperature":
  0.0, "avg_logprob": -0.1882278849777666, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0019133547320961952}, {"id": 1180, "seek": 363758, "start":
  3650.74, "end": 3653.22, "text": " Frankly, it probably doesn''t match anybody,",
  "tokens": [51022, 41344, 11, 309, 1391, 1177, 380, 2995, 4472, 11, 51146], "temperature":
  0.0, "avg_logprob": -0.1882278849777666, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0019133547320961952}, {"id": 1181, "seek": 363758, "start":
  3653.22, "end": 3654.94, "text": " but if I ran that search,", "tokens": [51146,
  457, 498, 286, 5872, 300, 3164, 11, 51232], "temperature": 0.0, "avg_logprob": -0.1882278849777666,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0019133547320961952},
  {"id": 1182, "seek": 363758, "start": 3654.94, "end": 3656.62, "text": " it would
  be a very small number of documents.", "tokens": [51232, 309, 576, 312, 257, 588,
  1359, 1230, 295, 8512, 13, 51316], "temperature": 0.0, "avg_logprob": -0.1882278849777666,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0019133547320961952},
  {"id": 1183, "seek": 363758, "start": 3656.62, "end": 3657.66, "text": " It''s very
  specific.", "tokens": [51316, 467, 311, 588, 2685, 13, 51368], "temperature": 0.0,
  "avg_logprob": -0.1882278849777666, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.0019133547320961952}, {"id": 1184, "seek": 363758, "start": 3657.66, "end": 3661.46,
  "text": " However, and so in that case, having a point kind of makes sense.", "tokens":
  [51368, 2908, 11, 293, 370, 294, 300, 1389, 11, 1419, 257, 935, 733, 295, 1669,
  2020, 13, 51558], "temperature": 0.0, "avg_logprob": -0.1882278849777666, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.0019133547320961952}, {"id": 1185, "seek":
  363758, "start": 3661.46, "end": 3663.86, "text": " However, if I ran a search for
  sales,", "tokens": [51558, 2908, 11, 498, 286, 5872, 257, 3164, 337, 5763, 11, 51678],
  "temperature": 0.0, "avg_logprob": -0.1882278849777666, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0019133547320961952}, {"id": 1186, "seek": 366386, "start":
  3664.86, "end": 3668.86, "text": " that''s like a third of all jobs.", "tokens":
  [50414, 300, 311, 411, 257, 2636, 295, 439, 4782, 13, 50614], "temperature": 0.0,
  "avg_logprob": -0.16494624382626694, "compression_ratio": 1.8185654008438819, "no_speech_prob":
  0.001431996002793312}, {"id": 1187, "seek": 366386, "start": 3668.86, "end": 3671.5,
  "text": " And for me to take the notion of sales,", "tokens": [50614, 400, 337,
  385, 281, 747, 264, 10710, 295, 5763, 11, 50746], "temperature": 0.0, "avg_logprob":
  -0.16494624382626694, "compression_ratio": 1.8185654008438819, "no_speech_prob":
  0.001431996002793312}, {"id": 1188, "seek": 366386, "start": 3671.5, "end": 3674.94,
  "text": " which is probably a giant region in this vector space", "tokens": [50746,
  597, 307, 1391, 257, 7410, 4458, 294, 341, 8062, 1901, 50918], "temperature": 0.0,
  "avg_logprob": -0.16494624382626694, "compression_ratio": 1.8185654008438819, "no_speech_prob":
  0.001431996002793312}, {"id": 1189, "seek": 366386, "start": 3674.94, "end": 3676.7000000000003,
  "text": " with lots of nuance inside of it,", "tokens": [50918, 365, 3195, 295,
  42625, 1854, 295, 309, 11, 51006], "temperature": 0.0, "avg_logprob": -0.16494624382626694,
  "compression_ratio": 1.8185654008438819, "no_speech_prob": 0.001431996002793312},
  {"id": 1190, "seek": 366386, "start": 3676.7000000000003, "end": 3680.58, "text":
  " and to then turn that into just a point in the other vector space,", "tokens":
  [51006, 293, 281, 550, 1261, 300, 666, 445, 257, 935, 294, 264, 661, 8062, 1901,
  11, 51200], "temperature": 0.0, "avg_logprob": -0.16494624382626694, "compression_ratio":
  1.8185654008438819, "no_speech_prob": 0.001431996002793312}, {"id": 1191, "seek":
  366386, "start": 3680.58, "end": 3682.7400000000002, "text": " it''s probably not
  gonna work out super well", "tokens": [51200, 309, 311, 1391, 406, 799, 589, 484,
  1687, 731, 51308], "temperature": 0.0, "avg_logprob": -0.16494624382626694, "compression_ratio":
  1.8185654008438819, "no_speech_prob": 0.001431996002793312}, {"id": 1192, "seek":
  366386, "start": 3682.7400000000002, "end": 3683.78, "text": " because there''s
  probably,", "tokens": [51308, 570, 456, 311, 1391, 11, 51360], "temperature": 0.0,
  "avg_logprob": -0.16494624382626694, "compression_ratio": 1.8185654008438819, "no_speech_prob":
  0.001431996002793312}, {"id": 1193, "seek": 366386, "start": 3683.78, "end": 3687.34,
  "text": " sales is probably distributed across that other vector space", "tokens":
  [51360, 5763, 307, 1391, 12631, 2108, 300, 661, 8062, 1901, 51538], "temperature":
  0.0, "avg_logprob": -0.16494624382626694, "compression_ratio": 1.8185654008438819,
  "no_speech_prob": 0.001431996002793312}, {"id": 1194, "seek": 366386, "start": 3687.34,
  "end": 3689.1800000000003, "text": " in a much larger region.", "tokens": [51538,
  294, 257, 709, 4833, 4458, 13, 51630], "temperature": 0.0, "avg_logprob": -0.16494624382626694,
  "compression_ratio": 1.8185654008438819, "no_speech_prob": 0.001431996002793312},
  {"id": 1195, "seek": 366386, "start": 3689.1800000000003, "end": 3693.7400000000002,
  "text": " And so there''s this notion of query specificity", "tokens": [51630, 400,
  370, 456, 311, 341, 10710, 295, 14581, 2685, 507, 51858], "temperature": 0.0, "avg_logprob":
  -0.16494624382626694, "compression_ratio": 1.8185654008438819, "no_speech_prob":
  0.001431996002793312}, {"id": 1196, "seek": 369374, "start": 3693.7799999999997,
  "end": 3695.58, "text": " which is also really useful.", "tokens": [50366, 597,
  307, 611, 534, 4420, 13, 50456], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1197, "seek": 369374, "start": 3695.58, "end": 3698.8199999999997, "text":
  " So I would actually argue that the better way to do this technique", "tokens":
  [50456, 407, 286, 576, 767, 9695, 300, 264, 1101, 636, 281, 360, 341, 6532, 50618],
  "temperature": 0.0, "avg_logprob": -0.14200683653823973, "compression_ratio": 1.7671755725190839,
  "no_speech_prob": 9.53077687881887e-05}, {"id": 1198, "seek": 369374, "start": 3698.8199999999997,
  "end": 3701.54, "text": " is as part of your initial query", "tokens": [50618, 307,
  382, 644, 295, 428, 5883, 14581, 50754], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1199, "seek": 369374, "start": 3701.54, "end": 3704.22, "text": " when you''re
  sort of finding the set of documents.", "tokens": [50754, 562, 291, 434, 1333, 295,
  5006, 264, 992, 295, 8512, 13, 50888], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1200, "seek": 369374, "start": 3704.22, "end": 3706.74, "text": " If you
  can look, for example, at the embeddings", "tokens": [50888, 759, 291, 393, 574,
  11, 337, 1365, 11, 412, 264, 12240, 29432, 51014], "temperature": 0.0, "avg_logprob":
  -0.14200683653823973, "compression_ratio": 1.7671755725190839, "no_speech_prob":
  9.53077687881887e-05}, {"id": 1201, "seek": 369374, "start": 3706.74, "end": 3708.74,
  "text": " and do just like a co-sign similarity", "tokens": [51014, 293, 360, 445,
  411, 257, 598, 12, 82, 788, 32194, 51114], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1202, "seek": 369374, "start": 3708.74, "end": 3710.7, "text": " across the
  embeddings that you''re pulling,", "tokens": [51114, 2108, 264, 12240, 29432, 300,
  291, 434, 8407, 11, 51212], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1203, "seek": 369374, "start": 3710.7, "end": 3715.8599999999997, "text":
  " you can go from a bunch of embeddings", "tokens": [51212, 291, 393, 352, 490,
  257, 3840, 295, 12240, 29432, 51470], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1204, "seek": 369374, "start": 3715.8599999999997, "end": 3717.62, "text":
  " that are just pulled together into a point", "tokens": [51470, 300, 366, 445,
  7373, 1214, 666, 257, 935, 51558], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1205, "seek": 369374, "start": 3717.62, "end": 3720.4599999999996, "text":
  " to actually saying, what is the relative size", "tokens": [51558, 281, 767, 1566,
  11, 437, 307, 264, 4972, 2744, 51700], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1206, "seek": 369374, "start": 3720.4599999999996, "end": 3722.66, "text":
  " of the range of the co-signs", "tokens": [51700, 295, 264, 3613, 295, 264, 598,
  12, 82, 42636, 51810], "temperature": 0.0, "avg_logprob": -0.14200683653823973,
  "compression_ratio": 1.7671755725190839, "no_speech_prob": 9.53077687881887e-05},
  {"id": 1207, "seek": 372266, "start": 3722.66, "end": 3724.5, "text": " within these
  embeddings?", "tokens": [50364, 1951, 613, 12240, 29432, 30, 50456], "temperature":
  0.0, "avg_logprob": -0.10577959265590699, "compression_ratio": 1.702290076335878,
  "no_speech_prob": 0.00023765789228491485}, {"id": 1208, "seek": 372266, "start":
  3724.5, "end": 3726.3799999999997, "text": " And if it''s a very large range,",
  "tokens": [50456, 400, 498, 309, 311, 257, 588, 2416, 3613, 11, 50550], "temperature":
  0.0, "avg_logprob": -0.10577959265590699, "compression_ratio": 1.702290076335878,
  "no_speech_prob": 0.00023765789228491485}, {"id": 1209, "seek": 372266, "start":
  3726.3799999999997, "end": 3729.02, "text": " I understand that this is not a very
  specific query,", "tokens": [50550, 286, 1223, 300, 341, 307, 406, 257, 588, 2685,
  14581, 11, 50682], "temperature": 0.0, "avg_logprob": -0.10577959265590699, "compression_ratio":
  1.702290076335878, "no_speech_prob": 0.00023765789228491485}, {"id": 1210, "seek":
  372266, "start": 3729.02, "end": 3730.22, "text": " it''s a broad query.", "tokens":
  [50682, 309, 311, 257, 4152, 14581, 13, 50742], "temperature": 0.0, "avg_logprob":
  -0.10577959265590699, "compression_ratio": 1.702290076335878, "no_speech_prob":
  0.00023765789228491485}, {"id": 1211, "seek": 372266, "start": 3730.22, "end": 3734.62,
  "text": " Therefore, when I go query in the dense space,", "tokens": [50742, 7504,
  11, 562, 286, 352, 14581, 294, 264, 18011, 1901, 11, 50962], "temperature": 0.0,
  "avg_logprob": -0.10577959265590699, "compression_ratio": 1.702290076335878, "no_speech_prob":
  0.00023765789228491485}, {"id": 1212, "seek": 372266, "start": 3734.62, "end": 3737.66,
  "text": " I need to draw a larger radius", "tokens": [50962, 286, 643, 281, 2642,
  257, 4833, 15845, 51114], "temperature": 0.0, "avg_logprob": -0.10577959265590699,
  "compression_ratio": 1.702290076335878, "no_speech_prob": 0.00023765789228491485},
  {"id": 1213, "seek": 372266, "start": 3737.66, "end": 3741.1, "text": " or a larger
  kind of shape around what I''m searching for.", "tokens": [51114, 420, 257, 4833,
  733, 295, 3909, 926, 437, 286, 478, 10808, 337, 13, 51286], "temperature": 0.0,
  "avg_logprob": -0.10577959265590699, "compression_ratio": 1.702290076335878, "no_speech_prob":
  0.00023765789228491485}, {"id": 1214, "seek": 372266, "start": 3741.1, "end": 3743.46,
  "text": " So ideally, you''re actually searching for a shape", "tokens": [51286,
  407, 22915, 11, 291, 434, 767, 10808, 337, 257, 3909, 51404], "temperature": 0.0,
  "avg_logprob": -0.10577959265590699, "compression_ratio": 1.702290076335878, "no_speech_prob":
  0.00023765789228491485}, {"id": 1215, "seek": 372266, "start": 3743.46, "end": 3744.8599999999997,
  "text": " at not just a point,", "tokens": [51404, 412, 406, 445, 257, 935, 11,
  51474], "temperature": 0.0, "avg_logprob": -0.10577959265590699, "compression_ratio":
  1.702290076335878, "no_speech_prob": 0.00023765789228491485}, {"id": 1216, "seek":
  372266, "start": 3744.8599999999997, "end": 3748.42, "text": " but literally every
  vector search implementation I''ve seen", "tokens": [51474, 457, 3736, 633, 8062,
  3164, 11420, 286, 600, 1612, 51652], "temperature": 0.0, "avg_logprob": -0.10577959265590699,
  "compression_ratio": 1.702290076335878, "no_speech_prob": 0.00023765789228491485},
  {"id": 1217, "seek": 372266, "start": 3748.42, "end": 3751.7, "text": " at any company
  is searching on embeddings as points", "tokens": [51652, 412, 604, 2237, 307, 10808,
  322, 12240, 29432, 382, 2793, 51816], "temperature": 0.0, "avg_logprob": -0.10577959265590699,
  "compression_ratio": 1.702290076335878, "no_speech_prob": 0.00023765789228491485},
  {"id": 1218, "seek": 375170, "start": 3751.7, "end": 3753.54, "text": " and just
  looking for the nearest things,", "tokens": [50364, 293, 445, 1237, 337, 264, 23831,
  721, 11, 50456], "temperature": 0.0, "avg_logprob": -0.20429954194186026, "compression_ratio":
  1.5807692307692307, "no_speech_prob": 0.0001122245448641479}, {"id": 1219, "seek":
  375170, "start": 3753.54, "end": 3754.7, "text": " not searching on shapes.", "tokens":
  [50456, 406, 10808, 322, 10854, 13, 50514], "temperature": 0.0, "avg_logprob": -0.20429954194186026,
  "compression_ratio": 1.5807692307692307, "no_speech_prob": 0.0001122245448641479},
  {"id": 1220, "seek": 375170, "start": 3754.7, "end": 3757.8999999999996, "text":
  " And so we don''t even really have the query patterns", "tokens": [50514, 400,
  370, 321, 500, 380, 754, 534, 362, 264, 14581, 8294, 50674], "temperature": 0.0,
  "avg_logprob": -0.20429954194186026, "compression_ratio": 1.5807692307692307, "no_speech_prob":
  0.0001122245448641479}, {"id": 1221, "seek": 375170, "start": 3757.8999999999996,
  "end": 3761.74, "text": " and paradigms in place today to do that kind of a query.",
  "tokens": [50674, 293, 13480, 328, 2592, 294, 1081, 965, 281, 360, 300, 733, 295,
  257, 14581, 13, 50866], "temperature": 0.0, "avg_logprob": -0.20429954194186026,
  "compression_ratio": 1.5807692307692307, "no_speech_prob": 0.0001122245448641479},
  {"id": 1222, "seek": 375170, "start": 3761.74, "end": 3763.62, "text": " But I think
  that would be a further improvement", "tokens": [50866, 583, 286, 519, 300, 576,
  312, 257, 3052, 10444, 50960], "temperature": 0.0, "avg_logprob": -0.20429954194186026,
  "compression_ratio": 1.5807692307692307, "no_speech_prob": 0.0001122245448641479},
  {"id": 1223, "seek": 375170, "start": 3763.62, "end": 3764.8999999999996, "text":
  " on the paradigm here.", "tokens": [50960, 322, 264, 24709, 510, 13, 51024], "temperature":
  0.0, "avg_logprob": -0.20429954194186026, "compression_ratio": 1.5807692307692307,
  "no_speech_prob": 0.0001122245448641479}, {"id": 1224, "seek": 375170, "start":
  3765.9399999999996, "end": 3767.74, "text": " Awesome.", "tokens": [51076, 10391,
  13, 51166], "temperature": 0.0, "avg_logprob": -0.20429954194186026, "compression_ratio":
  1.5807692307692307, "no_speech_prob": 0.0001122245448641479}, {"id": 1225, "seek":
  375170, "start": 3767.74, "end": 3769.66, "text": " Yeah, Tim Allison says thank
  you.", "tokens": [51166, 865, 11, 7172, 32638, 1619, 1309, 291, 13, 51262], "temperature":
  0.0, "avg_logprob": -0.20429954194186026, "compression_ratio": 1.5807692307692307,
  "no_speech_prob": 0.0001122245448641479}, {"id": 1226, "seek": 375170, "start":
  3769.66, "end": 3771.14, "text": " Thanks, Tim.", "tokens": [51262, 2561, 11, 7172,
  13, 51336], "temperature": 0.0, "avg_logprob": -0.20429954194186026, "compression_ratio":
  1.5807692307692307, "no_speech_prob": 0.0001122245448641479}, {"id": 1227, "seek":
  375170, "start": 3771.14, "end": 3772.54, "text": " The next question is from Julian.",
  "tokens": [51336, 440, 958, 1168, 307, 490, 25151, 13, 51406], "temperature": 0.0,
  "avg_logprob": -0.20429954194186026, "compression_ratio": 1.5807692307692307, "no_speech_prob":
  0.0001122245448641479}, {"id": 1228, "seek": 375170, "start": 3772.54, "end": 3774.98,
  "text": " Can you recommend any papers or other material", "tokens": [51406, 1664,
  291, 2748, 604, 10577, 420, 661, 2527, 51528], "temperature": 0.0, "avg_logprob":
  -0.20429954194186026, "compression_ratio": 1.5807692307692307, "no_speech_prob":
  0.0001122245448641479}, {"id": 1229, "seek": 375170, "start": 3774.98, "end": 3776.98,
  "text": " to explore the topic further?", "tokens": [51528, 281, 6839, 264, 4829,
  3052, 30, 51628], "temperature": 0.0, "avg_logprob": -0.20429954194186026, "compression_ratio":
  1.5807692307692307, "no_speech_prob": 0.0001122245448641479}, {"id": 1230, "seek":
  377698, "start": 3777.26, "end": 3780.7400000000002, "text": " So not really.",
  "tokens": [50378, 407, 406, 534, 13, 50552], "temperature": 0.0, "avg_logprob":
  -0.2884144943751646, "compression_ratio": 1.5648148148148149, "no_speech_prob":
  0.00744219496846199}, {"id": 1231, "seek": 377698, "start": 3780.7400000000002,
  "end": 3787.54, "text": " So the one whole vector thing is something I kind of came
  up with.", "tokens": [50552, 407, 264, 472, 1379, 8062, 551, 307, 746, 286, 733,
  295, 1361, 493, 365, 13, 50892], "temperature": 0.0, "avg_logprob": -0.2884144943751646,
  "compression_ratio": 1.5648148148148149, "no_speech_prob": 0.00744219496846199},
  {"id": 1232, "seek": 377698, "start": 3787.54, "end": 3790.1, "text": " I will say,
  well, two things.", "tokens": [50892, 286, 486, 584, 11, 731, 11, 732, 721, 13,
  51020], "temperature": 0.0, "avg_logprob": -0.2884144943751646, "compression_ratio":
  1.5648148148148149, "no_speech_prob": 0.00744219496846199}, {"id": 1233, "seek":
  377698, "start": 3790.1, "end": 3792.94, "text": " One, semantic knowledge graphs.",
  "tokens": [51020, 1485, 11, 47982, 3601, 24877, 13, 51162], "temperature": 0.0,
  "avg_logprob": -0.2884144943751646, "compression_ratio": 1.5648148148148149, "no_speech_prob":
  0.00744219496846199}, {"id": 1234, "seek": 377698, "start": 3792.94, "end": 3796.02,
  "text": " I actually was the lead author on the original semantic knowledge", "tokens":
  [51162, 286, 767, 390, 264, 1477, 3793, 322, 264, 3380, 47982, 3601, 51316], "temperature":
  0.0, "avg_logprob": -0.2884144943751646, "compression_ratio": 1.5648148148148149,
  "no_speech_prob": 0.00744219496846199}, {"id": 1235, "seek": 377698, "start": 3796.02,
  "end": 3800.18, "text": " graph paper back in like, I don''t know, 2016 or whatever
  was published.", "tokens": [51316, 4295, 3035, 646, 294, 411, 11, 286, 500, 380,
  458, 11, 6549, 420, 2035, 390, 6572, 13, 51524], "temperature": 0.0, "avg_logprob":
  -0.2884144943751646, "compression_ratio": 1.5648148148148149, "no_speech_prob":
  0.00744219496846199}, {"id": 1236, "seek": 377698, "start": 3800.18, "end": 3806.62,
  "text": " So this notion of being able to jump between spaces back", "tokens": [51524,
  407, 341, 10710, 295, 885, 1075, 281, 3012, 1296, 7673, 646, 51846], "temperature":
  0.0, "avg_logprob": -0.2884144943751646, "compression_ratio": 1.5648148148148149,
  "no_speech_prob": 0.00744219496846199}, {"id": 1237, "seek": 380662, "start": 3806.62,
  "end": 3809.98, "text": " to a sparse space, you could look at that paper", "tokens":
  [50364, 281, 257, 637, 11668, 1901, 11, 291, 727, 574, 412, 300, 3035, 50532], "temperature":
  0.0, "avg_logprob": -0.21112240971745672, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.0006073295371606946}, {"id": 1238, "seek": 380662, "start":
  3809.98, "end": 3811.54, "text": " if you want an actual research paper.", "tokens":
  [50532, 498, 291, 528, 364, 3539, 2132, 3035, 13, 50610], "temperature": 0.0, "avg_logprob":
  -0.21112240971745672, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.0006073295371606946}, {"id": 1239, "seek": 380662, "start": 3811.54, "end": 3813.06,
  "text": " I''ve also given lots of talks about it.", "tokens": [50610, 286, 600,
  611, 2212, 3195, 295, 6686, 466, 309, 13, 50686], "temperature": 0.0, "avg_logprob":
  -0.21112240971745672, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.0006073295371606946}, {"id": 1240, "seek": 380662, "start": 3813.06, "end": 3814.3399999999997,
  "text": " It''s in the AI powered search book.", "tokens": [50686, 467, 311, 294,
  264, 7318, 17786, 3164, 1446, 13, 50750], "temperature": 0.0, "avg_logprob": -0.21112240971745672,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0006073295371606946},
  {"id": 1241, "seek": 380662, "start": 3814.3399999999997, "end": 3816.14, "text":
  " It''ll be in the course.", "tokens": [50750, 467, 603, 312, 294, 264, 1164, 13,
  50840], "temperature": 0.0, "avg_logprob": -0.21112240971745672, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 0.0006073295371606946}, {"id": 1242, "seek":
  380662, "start": 3816.14, "end": 3820.46, "text": " However, the notion of taking,
  running a query", "tokens": [50840, 2908, 11, 264, 10710, 295, 1940, 11, 2614, 257,
  14581, 51056], "temperature": 0.0, "avg_logprob": -0.21112240971745672, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 0.0006073295371606946}, {"id": 1243, "seek":
  380662, "start": 3820.46, "end": 3825.74, "text": " and pulling vectors together
  and even the notion of query", "tokens": [51056, 293, 8407, 18875, 1214, 293, 754,
  264, 10710, 295, 14581, 51320], "temperature": 0.0, "avg_logprob": -0.21112240971745672,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0006073295371606946},
  {"id": 1244, "seek": 380662, "start": 3825.74, "end": 3828.9, "text": " specificity
  that co-science similarity thing.", "tokens": [51320, 2685, 507, 300, 598, 12, 82,
  6699, 32194, 551, 13, 51478], "temperature": 0.0, "avg_logprob": -0.21112240971745672,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0006073295371606946},
  {"id": 1245, "seek": 380662, "start": 3828.9, "end": 3833.06, "text": " If you look
  at Daniel Tukolang, he actually did a lightning", "tokens": [51478, 759, 291, 574,
  412, 8033, 314, 2034, 401, 656, 11, 415, 767, 630, 257, 16589, 51686], "temperature":
  0.0, "avg_logprob": -0.21112240971745672, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.0006073295371606946}, {"id": 1246, "seek": 383306, "start":
  3833.06, "end": 3838.06, "text": " talk with us a week or two ago on query understanding.",
  "tokens": [50364, 751, 365, 505, 257, 1243, 420, 732, 2057, 322, 14581, 3701, 13,
  50614], "temperature": 0.0, "avg_logprob": -0.11625098345572488, "compression_ratio":
  1.9367088607594938, "no_speech_prob": 0.00895062554627657}, {"id": 1247, "seek":
  383306, "start": 3838.06, "end": 3840.82, "text": " He actually talks about this
  notion of a bag of documents", "tokens": [50614, 634, 767, 6686, 466, 341, 10710,
  295, 257, 3411, 295, 8512, 50752], "temperature": 0.0, "avg_logprob": -0.11625098345572488,
  "compression_ratio": 1.9367088607594938, "no_speech_prob": 0.00895062554627657},
  {"id": 1248, "seek": 383306, "start": 3840.82, "end": 3842.18, "text": " to represent
  a query.", "tokens": [50752, 281, 2906, 257, 14581, 13, 50820], "temperature": 0.0,
  "avg_logprob": -0.11625098345572488, "compression_ratio": 1.9367088607594938, "no_speech_prob":
  0.00895062554627657}, {"id": 1249, "seek": 383306, "start": 3842.18, "end": 3844.66,
  "text": " It''s functionally the exact same thing.", "tokens": [50820, 467, 311,
  2445, 379, 264, 1900, 912, 551, 13, 50944], "temperature": 0.0, "avg_logprob": -0.11625098345572488,
  "compression_ratio": 1.9367088607594938, "no_speech_prob": 0.00895062554627657},
  {"id": 1250, "seek": 383306, "start": 3844.66, "end": 3848.58, "text": " So if I
  run a query and think of the query''s meaning", "tokens": [50944, 407, 498, 286,
  1190, 257, 14581, 293, 519, 295, 264, 14581, 311, 3620, 51140], "temperature": 0.0,
  "avg_logprob": -0.11625098345572488, "compression_ratio": 1.9367088607594938, "no_speech_prob":
  0.00895062554627657}, {"id": 1251, "seek": 383306, "start": 3848.58, "end": 3852.58,
  "text": " as being represented by the set of documents that match that query,",
  "tokens": [51140, 382, 885, 10379, 538, 264, 992, 295, 8512, 300, 2995, 300, 14581,
  11, 51340], "temperature": 0.0, "avg_logprob": -0.11625098345572488, "compression_ratio":
  1.9367088607594938, "no_speech_prob": 0.00895062554627657}, {"id": 1252, "seek":
  383306, "start": 3852.58, "end": 3855.94, "text": " then to take that set of documents
  that holds that meaning", "tokens": [51340, 550, 281, 747, 300, 992, 295, 8512,
  300, 9190, 300, 3620, 51508], "temperature": 0.0, "avg_logprob": -0.11625098345572488,
  "compression_ratio": 1.9367088607594938, "no_speech_prob": 0.00895062554627657},
  {"id": 1253, "seek": 383306, "start": 3855.94, "end": 3859.86, "text": " and pull
  the embeddings to create an average embedding", "tokens": [51508, 293, 2235, 264,
  12240, 29432, 281, 1884, 364, 4274, 12240, 3584, 51704], "temperature": 0.0, "avg_logprob":
  -0.11625098345572488, "compression_ratio": 1.9367088607594938, "no_speech_prob":
  0.00895062554627657}, {"id": 1254, "seek": 383306, "start": 3859.86, "end": 3862.7,
  "text": " that represents that meaning and embedding space,", "tokens": [51704,
  300, 8855, 300, 3620, 293, 12240, 3584, 1901, 11, 51846], "temperature": 0.0, "avg_logprob":
  -0.11625098345572488, "compression_ratio": 1.9367088607594938, "no_speech_prob":
  0.00895062554627657}, {"id": 1255, "seek": 386270, "start": 3862.7, "end": 3865.18,
  "text": " it''s functionally the same thing that Daniel describes", "tokens": [50364,
  309, 311, 2445, 379, 264, 912, 551, 300, 8033, 15626, 50488], "temperature": 0.0,
  "avg_logprob": -0.20744129919236706, "compression_ratio": 1.6217228464419475, "no_speech_prob":
  0.0002090014168061316}, {"id": 1256, "seek": 386270, "start": 3865.18, "end": 3867.4199999999996,
  "text": " when he talks about bags of documents.", "tokens": [50488, 562, 415, 6686,
  466, 10405, 295, 8512, 13, 50600], "temperature": 0.0, "avg_logprob": -0.20744129919236706,
  "compression_ratio": 1.6217228464419475, "no_speech_prob": 0.0002090014168061316},
  {"id": 1257, "seek": 386270, "start": 3867.4199999999996, "end": 3869.8199999999997,
  "text": " So I would say look at Daniel''s work,", "tokens": [50600, 407, 286, 576,
  584, 574, 412, 8033, 311, 589, 11, 50720], "temperature": 0.0, "avg_logprob": -0.20744129919236706,
  "compression_ratio": 1.6217228464419475, "no_speech_prob": 0.0002090014168061316},
  {"id": 1258, "seek": 386270, "start": 3869.8199999999997, "end": 3874.1, "text":
  " look at the lightning talk he gave a week or two ago with us.", "tokens": [50720,
  574, 412, 264, 16589, 751, 415, 2729, 257, 1243, 420, 732, 2057, 365, 505, 13, 50934],
  "temperature": 0.0, "avg_logprob": -0.20744129919236706, "compression_ratio": 1.6217228464419475,
  "no_speech_prob": 0.0002090014168061316}, {"id": 1259, "seek": 386270, "start":
  3874.1, "end": 3876.58, "text": " And those are some good resources.", "tokens":
  [50934, 400, 729, 366, 512, 665, 3593, 13, 51058], "temperature": 0.0, "avg_logprob":
  -0.20744129919236706, "compression_ratio": 1.6217228464419475, "no_speech_prob":
  0.0002090014168061316}, {"id": 1260, "seek": 386270, "start": 3876.58, "end": 3879.58,
  "text": " And of course, the book and the course.", "tokens": [51058, 400, 295,
  1164, 11, 264, 1446, 293, 264, 1164, 13, 51208], "temperature": 0.0, "avg_logprob":
  -0.20744129919236706, "compression_ratio": 1.6217228464419475, "no_speech_prob":
  0.0002090014168061316}, {"id": 1261, "seek": 386270, "start": 3879.58, "end": 3880.74,
  "text": " Yeah, awesome.", "tokens": [51208, 865, 11, 3476, 13, 51266], "temperature":
  0.0, "avg_logprob": -0.20744129919236706, "compression_ratio": 1.6217228464419475,
  "no_speech_prob": 0.0002090014168061316}, {"id": 1262, "seek": 386270, "start":
  3880.74, "end": 3883.54, "text": " Maybe at some point of paper as well, right?",
  "tokens": [51266, 2704, 412, 512, 935, 295, 3035, 382, 731, 11, 558, 30, 51406],
  "temperature": 0.0, "avg_logprob": -0.20744129919236706, "compression_ratio": 1.6217228464419475,
  "no_speech_prob": 0.0002090014168061316}, {"id": 1263, "seek": 386270, "start":
  3883.54, "end": 3885.1, "text": " Yeah, it''s definitely possible.", "tokens": [51406,
  865, 11, 309, 311, 2138, 1944, 13, 51484], "temperature": 0.0, "avg_logprob": -0.20744129919236706,
  "compression_ratio": 1.6217228464419475, "no_speech_prob": 0.0002090014168061316},
  {"id": 1264, "seek": 386270, "start": 3885.1, "end": 3888.1, "text": " I need lots
  of good.", "tokens": [51484, 286, 643, 3195, 295, 665, 13, 51634], "temperature":
  0.0, "avg_logprob": -0.20744129919236706, "compression_ratio": 1.6217228464419475,
  "no_speech_prob": 0.0002090014168061316}, {"id": 1265, "seek": 386270, "start":
  3888.1, "end": 3891.8599999999997, "text": " I need evals on how this actually does
  in practice.", "tokens": [51634, 286, 643, 1073, 1124, 322, 577, 341, 767, 775,
  294, 3124, 13, 51822], "temperature": 0.0, "avg_logprob": -0.20744129919236706,
  "compression_ratio": 1.6217228464419475, "no_speech_prob": 0.0002090014168061316},
  {"id": 1266, "seek": 389186, "start": 3891.86, "end": 3893.06, "text": " Yeah, absolutely.",
  "tokens": [50364, 865, 11, 3122, 13, 50424], "temperature": 0.0, "avg_logprob":
  -0.2862801752170595, "compression_ratio": 1.6326530612244898, "no_speech_prob":
  0.0007126876735128462}, {"id": 1267, "seek": 389186, "start": 3893.06, "end": 3894.26,
  "text": " Are you not the same question?", "tokens": [50424, 2014, 291, 406, 264,
  912, 1168, 30, 50484], "temperature": 0.0, "avg_logprob": -0.2862801752170595, "compression_ratio":
  1.6326530612244898, "no_speech_prob": 0.0007126876735128462}, {"id": 1268, "seek":
  389186, "start": 3894.26, "end": 3895.34, "text": " I''ll skip that.", "tokens":
  [50484, 286, 603, 10023, 300, 13, 50538], "temperature": 0.0, "avg_logprob": -0.2862801752170595,
  "compression_ratio": 1.6326530612244898, "no_speech_prob": 0.0007126876735128462},
  {"id": 1269, "seek": 389186, "start": 3895.34, "end": 3898.9, "text": " Mustafa
  is asking for a knife phone query cases.", "tokens": [50538, 37229, 307, 3365, 337,
  257, 7976, 2593, 14581, 3331, 13, 50716], "temperature": 0.0, "avg_logprob": -0.2862801752170595,
  "compression_ratio": 1.6326530612244898, "no_speech_prob": 0.0007126876735128462},
  {"id": 1270, "seek": 389186, "start": 3898.9, "end": 3901.54, "text": " So charges
  may also appear.", "tokens": [50716, 407, 12235, 815, 611, 4204, 13, 50848], "temperature":
  0.0, "avg_logprob": -0.2862801752170595, "compression_ratio": 1.6326530612244898,
  "no_speech_prob": 0.0007126876735128462}, {"id": 1271, "seek": 389186, "start":
  3901.54, "end": 3903.6200000000003, "text": " Would be correct to take the average.",
  "tokens": [50848, 6068, 312, 3006, 281, 747, 264, 4274, 13, 50952], "temperature":
  0.0, "avg_logprob": -0.2862801752170595, "compression_ratio": 1.6326530612244898,
  "no_speech_prob": 0.0007126876735128462}, {"id": 1272, "seek": 389186, "start":
  3903.6200000000003, "end": 3906.7000000000003, "text": " Would it be correct to
  take the average of them?", "tokens": [50952, 6068, 309, 312, 3006, 281, 747, 264,
  4274, 295, 552, 30, 51106], "temperature": 0.0, "avg_logprob": -0.2862801752170595,
  "compression_ratio": 1.6326530612244898, "no_speech_prob": 0.0007126876735128462},
  {"id": 1273, "seek": 389186, "start": 3906.7000000000003, "end": 3907.38, "text":
  " So good question.", "tokens": [51106, 407, 665, 1168, 13, 51140], "temperature":
  0.0, "avg_logprob": -0.2862801752170595, "compression_ratio": 1.6326530612244898,
  "no_speech_prob": 0.0007126876735128462}, {"id": 1274, "seek": 389186, "start":
  3907.38, "end": 3910.58, "text": " So yeah, if you, so,", "tokens": [51140, 407,
  1338, 11, 498, 291, 11, 370, 11, 51300], "temperature": 0.0, "avg_logprob": -0.2862801752170595,
  "compression_ratio": 1.6326530612244898, "no_speech_prob": 0.0007126876735128462},
  {"id": 1275, "seek": 389186, "start": 3911.7000000000003, "end": 3914.3, "text":
  " Lexical queries work really well.", "tokens": [51356, 24086, 804, 24109, 589,
  534, 731, 13, 51486], "temperature": 0.0, "avg_logprob": -0.2862801752170595, "compression_ratio":
  1.6326530612244898, "no_speech_prob": 0.0007126876735128462}, {"id": 1276, "seek":
  389186, "start": 3914.3, "end": 3917.1800000000003, "text": " When you''ve got particular
  terms you''re looking for,", "tokens": [51486, 1133, 291, 600, 658, 1729, 2115,
  291, 434, 1237, 337, 11, 51630], "temperature": 0.0, "avg_logprob": -0.2862801752170595,
  "compression_ratio": 1.6326530612244898, "no_speech_prob": 0.0007126876735128462},
  {"id": 1277, "seek": 389186, "start": 3917.1800000000003, "end": 3920.1, "text":
  " whether it''s an ID or whether it''s a keyword,", "tokens": [51630, 1968, 309,
  311, 364, 7348, 420, 1968, 309, 311, 257, 20428, 11, 51776], "temperature": 0.0,
  "avg_logprob": -0.2862801752170595, "compression_ratio": 1.6326530612244898, "no_speech_prob":
  0.0007126876735128462}, {"id": 1278, "seek": 392010, "start": 3920.1, "end": 3922.62,
  "text": " they don''t work as well with like semantic meaning.", "tokens": [50364,
  436, 500, 380, 589, 382, 731, 365, 411, 47982, 3620, 13, 50490], "temperature":
  0.0, "avg_logprob": -0.15670201315808652, "compression_ratio": 1.6769759450171822,
  "no_speech_prob": 0.0007207689923234284}, {"id": 1279, "seek": 392010, "start":
  3922.62, "end": 3925.7, "text": " Whereas in a dent space, obviously you query on
  meaning,", "tokens": [50490, 13813, 294, 257, 7059, 1901, 11, 2745, 291, 14581,
  322, 3620, 11, 50644], "temperature": 0.0, "avg_logprob": -0.15670201315808652,
  "compression_ratio": 1.6769759450171822, "no_speech_prob": 0.0007207689923234284},
  {"id": 1280, "seek": 392010, "start": 3925.7, "end": 3928.62, "text": " but if you
  try to search for a product ID in a dent space,", "tokens": [50644, 457, 498, 291,
  853, 281, 3164, 337, 257, 1674, 7348, 294, 257, 7059, 1901, 11, 50790], "temperature":
  0.0, "avg_logprob": -0.15670201315808652, "compression_ratio": 1.6769759450171822,
  "no_speech_prob": 0.0007207689923234284}, {"id": 1281, "seek": 392010, "start":
  3928.62, "end": 3930.7, "text": " unless you''ve fine-tuned it for that,", "tokens":
  [50790, 5969, 291, 600, 2489, 12, 83, 43703, 309, 337, 300, 11, 50894], "temperature":
  0.0, "avg_logprob": -0.15670201315808652, "compression_ratio": 1.6769759450171822,
  "no_speech_prob": 0.0007207689923234284}, {"id": 1282, "seek": 392010, "start":
  3930.7, "end": 3933.18, "text": " it''s gonna do an awful job.", "tokens": [50894,
  309, 311, 799, 360, 364, 11232, 1691, 13, 51018], "temperature": 0.0, "avg_logprob":
  -0.15670201315808652, "compression_ratio": 1.6769759450171822, "no_speech_prob":
  0.0007207689923234284}, {"id": 1283, "seek": 392010, "start": 3933.18, "end": 3935.98,
  "text": " And so, in the case of like searching for iPhone", "tokens": [51018, 400,
  370, 11, 294, 264, 1389, 295, 411, 10808, 337, 7252, 51158], "temperature": 0.0,
  "avg_logprob": -0.15670201315808652, "compression_ratio": 1.6769759450171822, "no_speech_prob":
  0.0007207689923234284}, {"id": 1284, "seek": 392010, "start": 3935.98, "end": 3938.18,
  "text": " and getting iPhone cases,", "tokens": [51158, 293, 1242, 7252, 3331, 11,
  51268], "temperature": 0.0, "avg_logprob": -0.15670201315808652, "compression_ratio":
  1.6769759450171822, "no_speech_prob": 0.0007207689923234284}, {"id": 1285, "seek":
  392010, "start": 3938.18, "end": 3940.94, "text": " this somewhat gets back to what
  I said earlier about,", "tokens": [51268, 341, 8344, 2170, 646, 281, 437, 286, 848,
  3071, 466, 11, 51406], "temperature": 0.0, "avg_logprob": -0.15670201315808652,
  "compression_ratio": 1.6769759450171822, "no_speech_prob": 0.0007207689923234284},
  {"id": 1286, "seek": 392010, "start": 3940.94, "end": 3943.98, "text": " ideally,
  if you take the top end documents", "tokens": [51406, 22915, 11, 498, 291, 747,
  264, 1192, 917, 8512, 51558], "temperature": 0.0, "avg_logprob": -0.15670201315808652,
  "compression_ratio": 1.6769759450171822, "no_speech_prob": 0.0007207689923234284},
  {"id": 1287, "seek": 392010, "start": 3943.98, "end": 3946.9, "text": " that are
  the most relevant and you limit to that,", "tokens": [51558, 300, 366, 264, 881,
  7340, 293, 291, 4948, 281, 300, 11, 51704], "temperature": 0.0, "avg_logprob": -0.15670201315808652,
  "compression_ratio": 1.6769759450171822, "no_speech_prob": 0.0007207689923234284},
  {"id": 1288, "seek": 392010, "start": 3946.9, "end": 3948.46, "text": " like if
  you''re ranking algorithm", "tokens": [51704, 411, 498, 291, 434, 17833, 9284, 51782],
  "temperature": 0.0, "avg_logprob": -0.15670201315808652, "compression_ratio": 1.6769759450171822,
  "no_speech_prob": 0.0007207689923234284}, {"id": 1289, "seek": 394846, "start":
  3948.46, "end": 3950.78, "text": " can already sort of understand that when someone
  searches", "tokens": [50364, 393, 1217, 1333, 295, 1223, 300, 562, 1580, 26701,
  50480], "temperature": 0.0, "avg_logprob": -0.2072736805882947, "compression_ratio":
  1.8132780082987552, "no_speech_prob": 0.0004132489557377994}, {"id": 1290, "seek":
  394846, "start": 3950.78, "end": 3955.78, "text": " for iPhone that they mean an
  actual iPhone versus a case,", "tokens": [50480, 337, 7252, 300, 436, 914, 364,
  3539, 7252, 5717, 257, 1389, 11, 50730], "temperature": 0.0, "avg_logprob": -0.2072736805882947,
  "compression_ratio": 1.8132780082987552, "no_speech_prob": 0.0004132489557377994},
  {"id": 1291, "seek": 394846, "start": 3955.78, "end": 3958.14, "text": " that''s
  a better way to go", "tokens": [50730, 300, 311, 257, 1101, 636, 281, 352, 50848],
  "temperature": 0.0, "avg_logprob": -0.2072736805882947, "compression_ratio": 1.8132780082987552,
  "no_speech_prob": 0.0004132489557377994}, {"id": 1292, "seek": 394846, "start":
  3958.14, "end": 3960.5, "text": " versus just anything that matches the term.",
  "tokens": [50848, 5717, 445, 1340, 300, 10676, 264, 1433, 13, 50966], "temperature":
  0.0, "avg_logprob": -0.2072736805882947, "compression_ratio": 1.8132780082987552,
  "no_speech_prob": 0.0004132489557377994}, {"id": 1293, "seek": 394846, "start":
  3960.5, "end": 3961.7, "text": " That being said,", "tokens": [50966, 663, 885,
  848, 11, 51026], "temperature": 0.0, "avg_logprob": -0.2072736805882947, "compression_ratio":
  1.8132780082987552, "no_speech_prob": 0.0004132489557377994}, {"id": 1294, "seek":
  394846, "start": 3963.34, "end": 3967.66, "text": " what you can do is you can,
  for example, in that case,", "tokens": [51108, 437, 291, 393, 360, 307, 291, 393,
  11, 337, 1365, 11, 294, 300, 1389, 11, 51324], "temperature": 0.0, "avg_logprob":
  -0.2072736805882947, "compression_ratio": 1.8132780082987552, "no_speech_prob":
  0.0004132489557377994}, {"id": 1295, "seek": 394846, "start": 3967.66, "end": 3970.9,
  "text": " search for iPhone, find the iPhone cases,", "tokens": [51324, 3164, 337,
  7252, 11, 915, 264, 7252, 3331, 11, 51486], "temperature": 0.0, "avg_logprob": -0.2072736805882947,
  "compression_ratio": 1.8132780082987552, "no_speech_prob": 0.0004132489557377994},
  {"id": 1296, "seek": 394846, "start": 3970.9, "end": 3972.94, "text": " along with
  iPhone, get that average vector,", "tokens": [51486, 2051, 365, 7252, 11, 483, 300,
  4274, 8062, 11, 51588], "temperature": 0.0, "avg_logprob": -0.2072736805882947,
  "compression_ratio": 1.8132780082987552, "no_speech_prob": 0.0004132489557377994},
  {"id": 1297, "seek": 394846, "start": 3972.94, "end": 3974.82, "text": " and then
  there''s still this region of,", "tokens": [51588, 293, 550, 456, 311, 920, 341,
  4458, 295, 11, 51682], "temperature": 0.0, "avg_logprob": -0.2072736805882947, "compression_ratio":
  1.8132780082987552, "no_speech_prob": 0.0004132489557377994}, {"id": 1298, "seek":
  394846, "start": 3974.82, "end": 3975.78, "text": " along certain dimensions,",
  "tokens": [51682, 2051, 1629, 12819, 11, 51730], "temperature": 0.0, "avg_logprob":
  -0.2072736805882947, "compression_ratio": 1.8132780082987552, "no_speech_prob":
  0.0004132489557377994}, {"id": 1299, "seek": 394846, "start": 3975.78, "end": 3977.34,
  "text": " it''s associated with iPhone.", "tokens": [51730, 309, 311, 6615, 365,
  7252, 13, 51808], "temperature": 0.0, "avg_logprob": -0.2072736805882947, "compression_ratio":
  1.8132780082987552, "no_speech_prob": 0.0004132489557377994}, {"id": 1300, "seek":
  397734, "start": 3977.34, "end": 3979.7000000000003, "text": " If you hopped over
  to the behavioral embedding space,", "tokens": [50364, 759, 291, 3818, 3452, 670,
  281, 264, 19124, 12240, 3584, 1901, 11, 50482], "temperature": 0.0, "avg_logprob":
  -0.14208681528804867, "compression_ratio": 1.7731958762886597, "no_speech_prob":
  8.853290637489408e-05}, {"id": 1301, "seek": 397734, "start": 3979.7000000000003,
  "end": 3981.06, "text": " what you''re gonna find is that,", "tokens": [50482, 437,
  291, 434, 799, 915, 307, 300, 11, 50550], "temperature": 0.0, "avg_logprob": -0.14208681528804867,
  "compression_ratio": 1.7731958762886597, "no_speech_prob": 8.853290637489408e-05},
  {"id": 1302, "seek": 397734, "start": 3981.06, "end": 3985.7400000000002, "text":
  " hey, these cases are very highly correlated to these items,", "tokens": [50550,
  4177, 11, 613, 3331, 366, 588, 5405, 38574, 281, 613, 4754, 11, 50784], "temperature":
  0.0, "avg_logprob": -0.14208681528804867, "compression_ratio": 1.7731958762886597,
  "no_speech_prob": 8.853290637489408e-05}, {"id": 1303, "seek": 397734, "start":
  3985.7400000000002, "end": 3988.42, "text": " the iPhones that actually correspond
  to those cases,", "tokens": [50784, 264, 43793, 300, 767, 6805, 281, 729, 3331,
  11, 50918], "temperature": 0.0, "avg_logprob": -0.14208681528804867, "compression_ratio":
  1.7731958762886597, "no_speech_prob": 8.853290637489408e-05}, {"id": 1304, "seek":
  397734, "start": 3988.42, "end": 3989.98, "text": " so that might be a case where
  you would want to hop", "tokens": [50918, 370, 300, 1062, 312, 257, 1389, 689, 291,
  576, 528, 281, 3818, 50996], "temperature": 0.0, "avg_logprob": -0.14208681528804867,
  "compression_ratio": 1.7731958762886597, "no_speech_prob": 8.853290637489408e-05},
  {"id": 1305, "seek": 397734, "start": 3989.98, "end": 3992.94, "text": " to the
  behavioral space and leverage what''s there.", "tokens": [50996, 281, 264, 19124,
  1901, 293, 13982, 437, 311, 456, 13, 51144], "temperature": 0.0, "avg_logprob":
  -0.14208681528804867, "compression_ratio": 1.7731958762886597, "no_speech_prob":
  8.853290637489408e-05}, {"id": 1306, "seek": 397734, "start": 3992.94, "end": 3994.7000000000003,
  "text": " There''s also just a note,", "tokens": [51144, 821, 311, 611, 445, 257,
  3637, 11, 51232], "temperature": 0.0, "avg_logprob": -0.14208681528804867, "compression_ratio":
  1.7731958762886597, "no_speech_prob": 8.853290637489408e-05}, {"id": 1307, "seek":
  397734, "start": 3994.7000000000003, "end": 3996.78, "text": " we''ve talked about
  taking entire queries", "tokens": [51232, 321, 600, 2825, 466, 1940, 2302, 24109,
  51336], "temperature": 0.0, "avg_logprob": -0.14208681528804867, "compression_ratio":
  1.7731958762886597, "no_speech_prob": 8.853290637489408e-05}, {"id": 1308, "seek":
  397734, "start": 3996.78, "end": 3999.02, "text": " and hopping from between spaces,",
  "tokens": [51336, 293, 47199, 490, 1296, 7673, 11, 51448], "temperature": 0.0, "avg_logprob":
  -0.14208681528804867, "compression_ratio": 1.7731958762886597, "no_speech_prob":
  8.853290637489408e-05}, {"id": 1309, "seek": 397734, "start": 3999.02, "end": 4002.9,
  "text": " but there''s also a line of thinking and practice here", "tokens": [51448,
  457, 456, 311, 611, 257, 1622, 295, 1953, 293, 3124, 510, 51642], "temperature":
  0.0, "avg_logprob": -0.14208681528804867, "compression_ratio": 1.7731958762886597,
  "no_speech_prob": 8.853290637489408e-05}, {"id": 1310, "seek": 397734, "start":
  4002.9, "end": 4005.82, "text": " around using this for query understanding,", "tokens":
  [51642, 926, 1228, 341, 337, 14581, 3701, 11, 51788], "temperature": 0.0, "avg_logprob":
  -0.14208681528804867, "compression_ratio": 1.7731958762886597, "no_speech_prob":
  8.853290637489408e-05}, {"id": 1311, "seek": 397734, "start": 4005.82, "end": 4007.1000000000004,
  "text": " not just ranking,", "tokens": [51788, 406, 445, 17833, 11, 51852], "temperature":
  0.0, "avg_logprob": -0.14208681528804867, "compression_ratio": 1.7731958762886597,
  "no_speech_prob": 8.853290637489408e-05}, {"id": 1312, "seek": 400710, "start":
  4007.1, "end": 4008.98, "text": " and so you could, for example,", "tokens": [50364,
  293, 370, 291, 727, 11, 337, 1365, 11, 50458], "temperature": 0.0, "avg_logprob":
  -0.17946782243361167, "compression_ratio": 1.7349397590361446, "no_speech_prob":
  1.633443207538221e-05}, {"id": 1313, "seek": 400710, "start": 4008.98, "end": 4011.86,
  "text": " split the query into individual keywords.", "tokens": [50458, 7472, 264,
  14581, 666, 2609, 21009, 13, 50602], "temperature": 0.0, "avg_logprob": -0.17946782243361167,
  "compression_ratio": 1.7349397590361446, "no_speech_prob": 1.633443207538221e-05},
  {"id": 1314, "seek": 400710, "start": 4011.86, "end": 4015.22, "text": " iPhone,
  like just the word iPhone,", "tokens": [50602, 7252, 11, 411, 445, 264, 1349, 7252,
  11, 50770], "temperature": 0.0, "avg_logprob": -0.17946782243361167, "compression_ratio":
  1.7349397590361446, "no_speech_prob": 1.633443207538221e-05}, {"id": 1315, "seek":
  400710, "start": 4015.22, "end": 4017.06, "text": " and you could also search on
  the dense space,", "tokens": [50770, 293, 291, 727, 611, 3164, 322, 264, 18011,
  1901, 11, 50862], "temperature": 0.0, "avg_logprob": -0.17946782243361167, "compression_ratio":
  1.7349397590361446, "no_speech_prob": 1.633443207538221e-05}, {"id": 1316, "seek":
  400710, "start": 4017.06, "end": 4019.3399999999997, "text": " and you could try
  to take the individual pieces", "tokens": [50862, 293, 291, 727, 853, 281, 747,
  264, 2609, 3755, 50976], "temperature": 0.0, "avg_logprob": -0.17946782243361167,
  "compression_ratio": 1.7349397590361446, "no_speech_prob": 1.633443207538221e-05},
  {"id": 1317, "seek": 400710, "start": 4019.3399999999997, "end": 4020.94, "text":
  " and find things related to them,", "tokens": [50976, 293, 915, 721, 4077, 281,
  552, 11, 51056], "temperature": 0.0, "avg_logprob": -0.17946782243361167, "compression_ratio":
  1.7349397590361446, "no_speech_prob": 1.633443207538221e-05}, {"id": 1318, "seek":
  400710, "start": 4020.94, "end": 4023.1, "text": " and then leverage that for query
  understanding", "tokens": [51056, 293, 550, 13982, 300, 337, 14581, 3701, 51164],
  "temperature": 0.0, "avg_logprob": -0.17946782243361167, "compression_ratio": 1.7349397590361446,
  "no_speech_prob": 1.633443207538221e-05}, {"id": 1319, "seek": 400710, "start":
  4023.1, "end": 4024.54, "text": " to hop back and forth between spaces.", "tokens":
  [51164, 281, 3818, 646, 293, 5220, 1296, 7673, 13, 51236], "temperature": 0.0, "avg_logprob":
  -0.17946782243361167, "compression_ratio": 1.7349397590361446, "no_speech_prob":
  1.633443207538221e-05}, {"id": 1320, "seek": 400710, "start": 4024.54, "end": 4028.14,
  "text": " So the answer is you still have", "tokens": [51236, 407, 264, 1867, 307,
  291, 920, 362, 51416], "temperature": 0.0, "avg_logprob": -0.17946782243361167,
  "compression_ratio": 1.7349397590361446, "no_speech_prob": 1.633443207538221e-05},
  {"id": 1321, "seek": 400710, "start": 4028.14, "end": 4031.46, "text": " the fundamental
  limitations of each space,", "tokens": [51416, 264, 8088, 15705, 295, 1184, 1901,
  11, 51582], "temperature": 0.0, "avg_logprob": -0.17946782243361167, "compression_ratio":
  1.7349397590361446, "no_speech_prob": 1.633443207538221e-05}, {"id": 1322, "seek":
  400710, "start": 4031.46, "end": 4034.46, "text": " but imagine if somebody searched
  for,", "tokens": [51582, 457, 3811, 498, 2618, 22961, 337, 11, 51732], "temperature":
  0.0, "avg_logprob": -0.17946782243361167, "compression_ratio": 1.7349397590361446,
  "no_speech_prob": 1.633443207538221e-05}, {"id": 1323, "seek": 403446, "start":
  4034.46, "end": 4039.26, "text": " I want a phone that''s really good at blah, blah,
  blah,", "tokens": [50364, 286, 528, 257, 2593, 300, 311, 534, 665, 412, 12288, 11,
  12288, 11, 12288, 11, 50604], "temperature": 0.0, "avg_logprob": -0.20818191919571313,
  "compression_ratio": 1.7264957264957266, "no_speech_prob": 0.00017591615323908627},
  {"id": 1324, "seek": 403446, "start": 4039.26, "end": 4044.26, "text": " that''s
  made by Apple with product ID X, right?", "tokens": [50604, 300, 311, 1027, 538,
  6373, 365, 1674, 7348, 1783, 11, 558, 30, 50854], "temperature": 0.0, "avg_logprob":
  -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1325, "seek": 403446, "start": 4044.98, "end": 4046.86,
  "text": " You can imagine trying to search for that,", "tokens": [50890, 509, 393,
  3811, 1382, 281, 3164, 337, 300, 11, 50984], "temperature": 0.0, "avg_logprob":
  -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1326, "seek": 403446, "start": 4046.86, "end": 4048.7,
  "text": " like an oratory on the,", "tokens": [50984, 411, 364, 420, 4745, 322,
  264, 11, 51076], "temperature": 0.0, "avg_logprob": -0.20818191919571313, "compression_ratio":
  1.7264957264957266, "no_speech_prob": 0.00017591615323908627}, {"id": 1327, "seek":
  403446, "start": 4048.7, "end": 4051.7400000000002, "text": " on the lexical side,",
  "tokens": [51076, 322, 264, 476, 87, 804, 1252, 11, 51228], "temperature": 0.0,
  "avg_logprob": -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1328, "seek": 403446, "start": 4051.7400000000002,
  "end": 4053.06, "text": " and you''ll actually match that ID", "tokens": [51228,
  293, 291, 603, 767, 2995, 300, 7348, 51294], "temperature": 0.0, "avg_logprob":
  -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1329, "seek": 403446, "start": 4053.06, "end": 4055.14,
  "text": " and probably have it come up at the very top,", "tokens": [51294, 293,
  1391, 362, 309, 808, 493, 412, 264, 588, 1192, 11, 51398], "temperature": 0.0, "avg_logprob":
  -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1330, "seek": 403446, "start": 4055.14, "end": 4058.2200000000003,
  "text": " and then you can imagine searching for that embedding", "tokens": [51398,
  293, 550, 291, 393, 3811, 10808, 337, 300, 12240, 3584, 51552], "temperature": 0.0,
  "avg_logprob": -0.20818191919571313, "compression_ratio": 1.7264957264957266, "no_speech_prob":
  0.00017591615323908627}, {"id": 1331, "seek": 403446, "start": 4058.2200000000003,
  "end": 4061.3, "text": " on the dense space,", "tokens": [51552, 322, 264, 18011,
  1901, 11, 51706], "temperature": 0.0, "avg_logprob": -0.20818191919571313, "compression_ratio":
  1.7264957264957266, "no_speech_prob": 0.00017591615323908627}, {"id": 1332, "seek":
  403446, "start": 4061.3, "end": 4064.18, "text": " and you can imagine for each
  of those hopping back and forth", "tokens": [51706, 293, 291, 393, 3811, 337, 1184,
  295, 729, 47199, 646, 293, 5220, 51850], "temperature": 0.0, "avg_logprob": -0.20818191919571313,
  "compression_ratio": 1.7264957264957266, "no_speech_prob": 0.00017591615323908627},
  {"id": 1333, "seek": 406418, "start": 4064.22, "end": 4066.14, "text": " and trying
  to see what documents are there a couple of times.", "tokens": [50366, 293, 1382,
  281, 536, 437, 8512, 366, 456, 257, 1916, 295, 1413, 13, 50462], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1334, "seek": 406418, "start":
  4066.14, "end": 4067.8599999999997, "text": " So there''s, look,", "tokens": [50462,
  407, 456, 311, 11, 574, 11, 50548], "temperature": 0.0, "avg_logprob": -0.15023418596595717,
  "compression_ratio": 1.796116504854369, "no_speech_prob": 0.00033023249125108123},
  {"id": 1335, "seek": 406418, "start": 4068.98, "end": 4069.8199999999997, "text":
  " sure to answer,", "tokens": [50604, 988, 281, 1867, 11, 50646], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1336, "seek": 406418, "start":
  4069.8199999999997, "end": 4071.22, "text": " there''s a lot of different ways",
  "tokens": [50646, 456, 311, 257, 688, 295, 819, 2098, 50716], "temperature": 0.0,
  "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369, "no_speech_prob":
  0.00033023249125108123}, {"id": 1337, "seek": 406418, "start": 4071.22, "end": 4072.7,
  "text": " that you could leverage this technique", "tokens": [50716, 300, 291, 727,
  13982, 341, 6532, 50790], "temperature": 0.0, "avg_logprob": -0.15023418596595717,
  "compression_ratio": 1.796116504854369, "no_speech_prob": 0.00033023249125108123},
  {"id": 1338, "seek": 406418, "start": 4072.7, "end": 4074.7799999999997, "text":
  " to be hopping back and forth.", "tokens": [50790, 281, 312, 47199, 646, 293, 5220,
  13, 50894], "temperature": 0.0, "avg_logprob": -0.15023418596595717, "compression_ratio":
  1.796116504854369, "no_speech_prob": 0.00033023249125108123}, {"id": 1339, "seek":
  406418, "start": 4074.7799999999997, "end": 4076.7, "text": " I''m not gonna claim
  now that I''ve thought through", "tokens": [50894, 286, 478, 406, 799, 3932, 586,
  300, 286, 600, 1194, 807, 50990], "temperature": 0.0, "avg_logprob": -0.15023418596595717,
  "compression_ratio": 1.796116504854369, "no_speech_prob": 0.00033023249125108123},
  {"id": 1340, "seek": 406418, "start": 4076.7, "end": 4077.58, "text": " every single
  one of them,", "tokens": [50990, 633, 2167, 472, 295, 552, 11, 51034], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1341, "seek": 406418, "start":
  4077.58, "end": 4079.1, "text": " and there''s lots of ways to do it,", "tokens":
  [51034, 293, 456, 311, 3195, 295, 2098, 281, 360, 309, 11, 51110], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1342, "seek": 406418, "start":
  4079.1, "end": 4082.2999999999997, "text": " but I think as an introduction to the
  topic,", "tokens": [51110, 457, 286, 519, 382, 364, 9339, 281, 264, 4829, 11, 51270],
  "temperature": 0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1343, "seek": 406418, "start":
  4082.2999999999997, "end": 4085.3799999999997, "text": " and as a tool that you
  can add to your tool belt,", "tokens": [51270, 293, 382, 257, 2290, 300, 291, 393,
  909, 281, 428, 2290, 10750, 11, 51424], "temperature": 0.0, "avg_logprob": -0.15023418596595717,
  "compression_ratio": 1.796116504854369, "no_speech_prob": 0.00033023249125108123},
  {"id": 1344, "seek": 406418, "start": 4085.3799999999997, "end": 4088.54, "text":
  " to be able to get explainability", "tokens": [51424, 281, 312, 1075, 281, 483,
  2903, 2310, 51582], "temperature": 0.0, "avg_logprob": -0.15023418596595717, "compression_ratio":
  1.796116504854369, "no_speech_prob": 0.00033023249125108123}, {"id": 1345, "seek":
  406418, "start": 4088.54, "end": 4089.62, "text": " and another vector space,",
  "tokens": [51582, 293, 1071, 8062, 1901, 11, 51636], "temperature": 0.0, "avg_logprob":
  -0.15023418596595717, "compression_ratio": 1.796116504854369, "no_speech_prob":
  0.00033023249125108123}, {"id": 1346, "seek": 406418, "start": 4089.62, "end": 4091.4199999999996,
  "text": " based upon what you found in the first vector space,", "tokens": [51636,
  2361, 3564, 437, 291, 1352, 294, 264, 700, 8062, 1901, 11, 51726], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1347, "seek": 406418, "start":
  4091.4199999999996, "end": 4094.02, "text": " I think this is a really cool technique,",
  "tokens": [51726, 286, 519, 341, 307, 257, 534, 1627, 6532, 11, 51856], "temperature":
  0.0, "avg_logprob": -0.15023418596595717, "compression_ratio": 1.796116504854369,
  "no_speech_prob": 0.00033023249125108123}, {"id": 1348, "seek": 409402, "start":
  4094.02, "end": 4096.78, "text": " and I just wanted to kind of present it and get
  feedback", "tokens": [50364, 293, 286, 445, 1415, 281, 733, 295, 1974, 309, 293,
  483, 5824, 50502], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1349, "seek":
  409402, "start": 4096.78, "end": 4098.94, "text": " and enjoy this discussion.",
  "tokens": [50502, 293, 2103, 341, 5017, 13, 50610], "temperature": 0.0, "avg_logprob":
  -0.16125579044736665, "compression_ratio": 1.6866666666666668, "no_speech_prob":
  0.0008274210849776864}, {"id": 1350, "seek": 409402, "start": 4098.94, "end": 4099.94,
  "text": " Yeah, thanks, Trey.", "tokens": [50610, 865, 11, 3231, 11, 314, 7950,
  13, 50660], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1351, "seek":
  409402, "start": 4099.94, "end": 4100.94, "text": " We''re quite over time,", "tokens":
  [50660, 492, 434, 1596, 670, 565, 11, 50710], "temperature": 0.0, "avg_logprob":
  -0.16125579044736665, "compression_ratio": 1.6866666666666668, "no_speech_prob":
  0.0008274210849776864}, {"id": 1352, "seek": 409402, "start": 4100.94, "end": 4102.7,
  "text": " thanks everyone for staying on,", "tokens": [50710, 3231, 1518, 337, 7939,
  322, 11, 50798], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1353, "seek":
  409402, "start": 4102.7, "end": 4104.54, "text": " and hopefully if you can still
  stay on,", "tokens": [50798, 293, 4696, 498, 291, 393, 920, 1754, 322, 11, 50890],
  "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio": 1.6866666666666668,
  "no_speech_prob": 0.0008274210849776864}, {"id": 1354, "seek": 409402, "start":
  4104.54, "end": 4106.62, "text": " we can get to the bottom of the list.", "tokens":
  [50890, 321, 393, 483, 281, 264, 2767, 295, 264, 1329, 13, 50994], "temperature":
  0.0, "avg_logprob": -0.16125579044736665, "compression_ratio": 1.6866666666666668,
  "no_speech_prob": 0.0008274210849776864}, {"id": 1355, "seek": 409402, "start":
  4108.1, "end": 4110.14, "text": " Yeah, and by the way, to your answer, Trey,",
  "tokens": [51068, 865, 11, 293, 538, 264, 636, 11, 281, 428, 1867, 11, 314, 7950,
  11, 51170], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1356, "seek":
  409402, "start": 4110.14, "end": 4112.14, "text": " I think somewhere there is probably
  a notion", "tokens": [51170, 286, 519, 4079, 456, 307, 1391, 257, 10710, 51270],
  "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio": 1.6866666666666668,
  "no_speech_prob": 0.0008274210849776864}, {"id": 1357, "seek": 409402, "start":
  4112.14, "end": 4114.62, "text": " of search result diversity as well, right?",
  "tokens": [51270, 295, 3164, 1874, 8811, 382, 731, 11, 558, 30, 51394], "temperature":
  0.0, "avg_logprob": -0.16125579044736665, "compression_ratio": 1.6866666666666668,
  "no_speech_prob": 0.0008274210849776864}, {"id": 1358, "seek": 409402, "start":
  4114.62, "end": 4116.7, "text": " So even if the user types iPhone,", "tokens":
  [51394, 407, 754, 498, 264, 4195, 3467, 7252, 11, 51498], "temperature": 0.0, "avg_logprob":
  -0.16125579044736665, "compression_ratio": 1.6866666666666668, "no_speech_prob":
  0.0008274210849776864}, {"id": 1359, "seek": 409402, "start": 4116.7, "end": 4117.9,
  "text": " they only mean the phone,", "tokens": [51498, 436, 787, 914, 264, 2593,
  11, 51558], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1360, "seek":
  409402, "start": 4117.9, "end": 4119.94, "text": " but they actually may mean something
  else, right?", "tokens": [51558, 457, 436, 767, 815, 914, 746, 1646, 11, 558, 30,
  51660], "temperature": 0.0, "avg_logprob": -0.16125579044736665, "compression_ratio":
  1.6866666666666668, "no_speech_prob": 0.0008274210849776864}, {"id": 1361, "seek":
  409402, "start": 4119.94, "end": 4121.86, "text": " So showing diverse results,",
  "tokens": [51660, 407, 4099, 9521, 3542, 11, 51756], "temperature": 0.0, "avg_logprob":
  -0.16125579044736665, "compression_ratio": 1.6866666666666668, "no_speech_prob":
  0.0008274210849776864}, {"id": 1362, "seek": 412186, "start": 4121.86, "end": 4124.94,
  "text": " and then traversing to the other side", "tokens": [50364, 293, 550, 23149,
  278, 281, 264, 661, 1252, 50518], "temperature": 0.0, "avg_logprob": -0.26635313034057617,
  "compression_ratio": 1.6473029045643153, "no_speech_prob": 0.0009137650486081839},
  {"id": 1363, "seek": 412186, "start": 4124.94, "end": 4127.82, "text": " with those
  diverse results could also make sense.", "tokens": [50518, 365, 729, 9521, 3542,
  727, 611, 652, 2020, 13, 50662], "temperature": 0.0, "avg_logprob": -0.26635313034057617,
  "compression_ratio": 1.6473029045643153, "no_speech_prob": 0.0009137650486081839},
  {"id": 1364, "seek": 412186, "start": 4129.099999999999, "end": 4130.259999999999,
  "text": " Absolutely.", "tokens": [50726, 7021, 13, 50784], "temperature": 0.0,
  "avg_logprob": -0.26635313034057617, "compression_ratio": 1.6473029045643153, "no_speech_prob":
  0.0009137650486081839}, {"id": 1365, "seek": 412186, "start": 4130.259999999999,
  "end": 4132.099999999999, "text": " Then Arjun is asking,", "tokens": [50784, 1396,
  1587, 10010, 307, 3365, 11, 50876], "temperature": 0.0, "avg_logprob": -0.26635313034057617,
  "compression_ratio": 1.6473029045643153, "no_speech_prob": 0.0009137650486081839},
  {"id": 1366, "seek": 412186, "start": 4132.099999999999, "end": 4133.66, "text":
  " is there, if I summarize the question,", "tokens": [50876, 307, 456, 11, 498,
  286, 20858, 264, 1168, 11, 50954], "temperature": 0.0, "avg_logprob": -0.26635313034057617,
  "compression_ratio": 1.6473029045643153, "no_speech_prob": 0.0009137650486081839},
  {"id": 1367, "seek": 412186, "start": 4133.66, "end": 4137.179999999999, "text":
  " is there a cheaper way than using semantic knowledge graph?", "tokens": [50954,
  307, 456, 257, 12284, 636, 813, 1228, 47982, 3601, 4295, 30, 51130], "temperature":
  0.0, "avg_logprob": -0.26635313034057617, "compression_ratio": 1.6473029045643153,
  "no_speech_prob": 0.0009137650486081839}, {"id": 1368, "seek": 412186, "start":
  4137.179999999999, "end": 4141.78, "text": " Maybe the fear is that the graph approach",
  "tokens": [51130, 2704, 264, 4240, 307, 300, 264, 4295, 3109, 51360], "temperature":
  0.0, "avg_logprob": -0.26635313034057617, "compression_ratio": 1.6473029045643153,
  "no_speech_prob": 0.0009137650486081839}, {"id": 1369, "seek": 412186, "start":
  4141.78, "end": 4146.42, "text": " is computation-expensive, is there some cheap
  way to...", "tokens": [51360, 307, 24903, 12, 27409, 11, 307, 456, 512, 7084, 636,
  281, 485, 51592], "temperature": 0.0, "avg_logprob": -0.26635313034057617, "compression_ratio":
  1.6473029045643153, "no_speech_prob": 0.0009137650486081839}, {"id": 1370, "seek":
  412186, "start": 4146.42, "end": 4148.78, "text": " It''s less computationally expensive
  than running", "tokens": [51592, 467, 311, 1570, 24903, 379, 5124, 813, 2614, 51710],
  "temperature": 0.0, "avg_logprob": -0.26635313034057617, "compression_ratio": 1.6473029045643153,
  "no_speech_prob": 0.0009137650486081839}, {"id": 1371, "seek": 412186, "start":
  4149.78, "end": 4151.299999999999, "text": " an embedding model typically.", "tokens":
  [51760, 364, 12240, 3584, 2316, 5850, 13, 51836], "temperature": 0.0, "avg_logprob":
  -0.26635313034057617, "compression_ratio": 1.6473029045643153, "no_speech_prob":
  0.0009137650486081839}, {"id": 1372, "seek": 415186, "start": 4152.299999999999,
  "end": 4154.78, "text": " But it just depends.", "tokens": [50386, 583, 309, 445,
  5946, 13, 50510], "temperature": 0.0, "avg_logprob": -0.2665522921401843, "compression_ratio":
  1.5850622406639003, "no_speech_prob": 0.00047733221435919404}, {"id": 1373, "seek":
  415186, "start": 4155.7, "end": 4157.259999999999, "text": " Yeah, I mean, there''s
  other techniques.", "tokens": [50556, 865, 11, 286, 914, 11, 456, 311, 661, 7512,
  13, 50634], "temperature": 0.0, "avg_logprob": -0.2665522921401843, "compression_ratio":
  1.5850622406639003, "no_speech_prob": 0.00047733221435919404}, {"id": 1374, "seek":
  415186, "start": 4157.259999999999, "end": 4158.86, "text": " Like if you have a
  fine-tuned,", "tokens": [50634, 1743, 498, 291, 362, 257, 2489, 12, 83, 43703, 11,
  50714], "temperature": 0.0, "avg_logprob": -0.2665522921401843, "compression_ratio":
  1.5850622406639003, "no_speech_prob": 0.00047733221435919404}, {"id": 1375, "seek":
  415186, "start": 4158.86, "end": 4161.0199999999995, "text": " blade model, for
  example,", "tokens": [50714, 10959, 2316, 11, 337, 1365, 11, 50822], "temperature":
  0.0, "avg_logprob": -0.2665522921401843, "compression_ratio": 1.5850622406639003,
  "no_speech_prob": 0.00047733221435919404}, {"id": 1376, "seek": 415186, "start":
  4161.0199999999995, "end": 4163.78, "text": " it can give you very comparable kind
  of", "tokens": [50822, 309, 393, 976, 291, 588, 25323, 733, 295, 50960], "temperature":
  0.0, "avg_logprob": -0.2665522921401843, "compression_ratio": 1.5850622406639003,
  "no_speech_prob": 0.00047733221435919404}, {"id": 1377, "seek": 415186, "start":
  4164.82, "end": 4167.78, "text": " semantic understanding on the sparse side.",
  "tokens": [51012, 47982, 3701, 322, 264, 637, 11668, 1252, 13, 51160], "temperature":
  0.0, "avg_logprob": -0.2665522921401843, "compression_ratio": 1.5850622406639003,
  "no_speech_prob": 0.00047733221435919404}, {"id": 1378, "seek": 415186, "start":
  4167.78, "end": 4169.5, "text": " The problem with that is you have to fine-tune
  it", "tokens": [51160, 440, 1154, 365, 300, 307, 291, 362, 281, 2489, 12, 83, 2613,
  309, 51246], "temperature": 0.0, "avg_logprob": -0.2665522921401843, "compression_ratio":
  1.5850622406639003, "no_speech_prob": 0.00047733221435919404}, {"id": 1379, "seek":
  415186, "start": 4169.5, "end": 4170.58, "text": " to your data,", "tokens": [51246,
  281, 428, 1412, 11, 51300], "temperature": 0.0, "avg_logprob": -0.2665522921401843,
  "compression_ratio": 1.5850622406639003, "no_speech_prob": 0.00047733221435919404},
  {"id": 1380, "seek": 415186, "start": 4170.58, "end": 4173.82, "text": " and also
  one of the benefits of the semantic knowledge graph", "tokens": [51300, 293, 611,
  472, 295, 264, 5311, 295, 264, 47982, 3601, 4295, 51462], "temperature": 0.0, "avg_logprob":
  -0.2665522921401843, "compression_ratio": 1.5850622406639003, "no_speech_prob":
  0.00047733221435919404}, {"id": 1381, "seek": 415186, "start": 4173.82, "end": 4176.7,
  "text": " is that if you,", "tokens": [51462, 307, 300, 498, 291, 11, 51606], "temperature":
  0.0, "avg_logprob": -0.2665522921401843, "compression_ratio": 1.5850622406639003,
  "no_speech_prob": 0.00047733221435919404}, {"id": 1382, "seek": 415186, "start":
  4176.7, "end": 4179.0199999999995, "text": " I''m just gonna quickly jump to the
  slide", "tokens": [51606, 286, 478, 445, 799, 2661, 3012, 281, 264, 4137, 51722],
  "temperature": 0.0, "avg_logprob": -0.2665522921401843, "compression_ratio": 1.5850622406639003,
  "no_speech_prob": 0.00047733221435919404}, {"id": 1383, "seek": 417902, "start":
  4179.02, "end": 4181.5, "text": " and show you this one.", "tokens": [50364, 293,
  855, 291, 341, 472, 13, 50488], "temperature": 0.0, "avg_logprob": -0.14282368324898384,
  "compression_ratio": 1.6437246963562753, "no_speech_prob": 0.008077533915638924},
  {"id": 1384, "seek": 417902, "start": 4183.540000000001, "end": 4185.860000000001,
  "text": " Let me do the one that''s got keywords, here we go.", "tokens": [50590,
  961, 385, 360, 264, 472, 300, 311, 658, 21009, 11, 510, 321, 352, 13, 50706], "temperature":
  0.0, "avg_logprob": -0.14282368324898384, "compression_ratio": 1.6437246963562753,
  "no_speech_prob": 0.008077533915638924}, {"id": 1385, "seek": 417902, "start": 4186.9800000000005,
  "end": 4188.700000000001, "text": " Share here.", "tokens": [50762, 14945, 510,
  13, 50848], "temperature": 0.0, "avg_logprob": -0.14282368324898384, "compression_ratio":
  1.6437246963562753, "no_speech_prob": 0.008077533915638924}, {"id": 1386, "seek":
  417902, "start": 4188.700000000001, "end": 4190.26, "text": " With the semantic
  knowledge graph approach,", "tokens": [50848, 2022, 264, 47982, 3601, 4295, 3109,
  11, 50926], "temperature": 0.0, "avg_logprob": -0.14282368324898384, "compression_ratio":
  1.6437246963562753, "no_speech_prob": 0.008077533915638924}, {"id": 1387, "seek":
  417902, "start": 4190.26, "end": 4192.9400000000005, "text": " you have the ability
  to not just represent", "tokens": [50926, 291, 362, 264, 3485, 281, 406, 445, 2906,
  51060], "temperature": 0.0, "avg_logprob": -0.14282368324898384, "compression_ratio":
  1.6437246963562753, "no_speech_prob": 0.008077533915638924}, {"id": 1388, "seek":
  417902, "start": 4192.9400000000005, "end": 4197.26, "text": " the query with a
  bunch of terms with values,", "tokens": [51060, 264, 14581, 365, 257, 3840, 295,
  2115, 365, 4190, 11, 51276], "temperature": 0.0, "avg_logprob": -0.14282368324898384,
  "compression_ratio": 1.6437246963562753, "no_speech_prob": 0.008077533915638924},
  {"id": 1389, "seek": 417902, "start": 4197.26, "end": 4199.22, "text": " but you
  can actually use any field.", "tokens": [51276, 457, 291, 393, 767, 764, 604, 2519,
  13, 51374], "temperature": 0.0, "avg_logprob": -0.14282368324898384, "compression_ratio":
  1.6437246963562753, "no_speech_prob": 0.008077533915638924}, {"id": 1390, "seek":
  417902, "start": 4199.22, "end": 4201.9400000000005, "text": " So it''s really useful
  to be able to describe it", "tokens": [51374, 407, 309, 311, 534, 4420, 281, 312,
  1075, 281, 6786, 309, 51510], "temperature": 0.0, "avg_logprob": -0.14282368324898384,
  "compression_ratio": 1.6437246963562753, "no_speech_prob": 0.008077533915638924},
  {"id": 1391, "seek": 417902, "start": 4201.9400000000005, "end": 4204.700000000001,
  "text": " with a category of Korean and a bunch of terms here,", "tokens": [51510,
  365, 257, 7719, 295, 6933, 293, 257, 3840, 295, 2115, 510, 11, 51648], "temperature":
  0.0, "avg_logprob": -0.14282368324898384, "compression_ratio": 1.6437246963562753,
  "no_speech_prob": 0.008077533915638924}, {"id": 1392, "seek": 417902, "start": 4204.700000000001,
  "end": 4207.780000000001, "text": " and maybe you''ve got other fields on your documents",
  "tokens": [51648, 293, 1310, 291, 600, 658, 661, 7909, 322, 428, 8512, 51802], "temperature":
  0.0, "avg_logprob": -0.14282368324898384, "compression_ratio": 1.6437246963562753,
  "no_speech_prob": 0.008077533915638924}, {"id": 1393, "seek": 420778, "start": 4207.78,
  "end": 4210.46, "text": " that are really useful for describing the document,",
  "tokens": [50364, 300, 366, 534, 4420, 337, 16141, 264, 4166, 11, 50498], "temperature":
  0.0, "avg_logprob": -0.2193455269666222, "compression_ratio": 1.6413793103448275,
  "no_speech_prob": 0.002246849937364459}, {"id": 1394, "seek": 420778, "start": 4210.46,
  "end": 4212.3, "text": " a taxonomy of some sort.", "tokens": [50498, 257, 3366,
  23423, 295, 512, 1333, 13, 50590], "temperature": 0.0, "avg_logprob": -0.2193455269666222,
  "compression_ratio": 1.6413793103448275, "no_speech_prob": 0.002246849937364459},
  {"id": 1395, "seek": 420778, "start": 4212.3, "end": 4214.86, "text": " The semantic
  knowledge graph gives you a lot richer ability", "tokens": [50590, 440, 47982, 3601,
  4295, 2709, 291, 257, 688, 29021, 3485, 50718], "temperature": 0.0, "avg_logprob":
  -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1396, "seek": 420778, "start": 4214.86, "end": 4219.0599999999995,
  "text": " to turn the set of documents into a fully expressive query.", "tokens":
  [50718, 281, 1261, 264, 992, 295, 8512, 666, 257, 4498, 40189, 14581, 13, 50928],
  "temperature": 0.0, "avg_logprob": -0.2193455269666222, "compression_ratio": 1.6413793103448275,
  "no_speech_prob": 0.002246849937364459}, {"id": 1397, "seek": 420778, "start": 4219.0599999999995,
  "end": 4220.86, "text": " So yeah, there''s other techniques.", "tokens": [50928,
  407, 1338, 11, 456, 311, 661, 7512, 13, 51018], "temperature": 0.0, "avg_logprob":
  -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1398, "seek": 420778, "start": 4220.86, "end": 4222.98,
  "text": " You could look at displayed things like that,", "tokens": [51018, 509,
  727, 574, 412, 16372, 721, 411, 300, 11, 51124], "temperature": 0.0, "avg_logprob":
  -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1399, "seek": 420778, "start": 4222.98, "end": 4226.66,
  "text": " but nothing that''s nearly as expressive.", "tokens": [51124, 457, 1825,
  300, 311, 6217, 382, 40189, 13, 51308], "temperature": 0.0, "avg_logprob": -0.2193455269666222,
  "compression_ratio": 1.6413793103448275, "no_speech_prob": 0.002246849937364459},
  {"id": 1400, "seek": 420778, "start": 4226.66, "end": 4227.94, "text": " Yeah, and
  these are the concepts", "tokens": [51308, 865, 11, 293, 613, 366, 264, 10392, 51372],
  "temperature": 0.0, "avg_logprob": -0.2193455269666222, "compression_ratio": 1.6413793103448275,
  "no_speech_prob": 0.002246849937364459}, {"id": 1401, "seek": 420778, "start": 4227.94,
  "end": 4229.42, "text": " you''re gonna covering the course, right?", "tokens":
  [51372, 291, 434, 799, 10322, 264, 1164, 11, 558, 30, 51446], "temperature": 0.0,
  "avg_logprob": -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1402, "seek": 420778, "start": 4229.42, "end": 4231.86,
  "text": " Yeah, we''ll cover it all in the course.", "tokens": [51446, 865, 11,
  321, 603, 2060, 309, 439, 294, 264, 1164, 13, 51568], "temperature": 0.0, "avg_logprob":
  -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1403, "seek": 420778, "start": 4231.86, "end": 4234.38,
  "text": " For those who are interested to learn more.", "tokens": [51568, 1171,
  729, 567, 366, 3102, 281, 1466, 544, 13, 51694], "temperature": 0.0, "avg_logprob":
  -0.2193455269666222, "compression_ratio": 1.6413793103448275, "no_speech_prob":
  0.002246849937364459}, {"id": 1404, "seek": 423438, "start": 4235.22, "end": 4238.74,
  "text": " Sorry, not trying to make this talk just a big promo", "tokens": [50406,
  4919, 11, 406, 1382, 281, 652, 341, 751, 445, 257, 955, 26750, 50582], "temperature":
  0.0, "avg_logprob": -0.34484953629343135, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.03527650237083435}, {"id": 1405, "seek": 423438, "start": 4238.74,
  "end": 4240.82, "text": " for the course, but this is a really,", "tokens": [50582,
  337, 264, 1164, 11, 457, 341, 307, 257, 534, 11, 50686], "temperature": 0.0, "avg_logprob":
  -0.34484953629343135, "compression_ratio": 1.626923076923077, "no_speech_prob":
  0.03527650237083435}, {"id": 1406, "seek": 423438, "start": 4240.82, "end": 4243.34,
  "text": " wormhole vectors by themselves are a really interesting topic,", "tokens":
  [50686, 23835, 14094, 18875, 538, 2969, 366, 257, 534, 1880, 4829, 11, 50812], "temperature":
  0.0, "avg_logprob": -0.34484953629343135, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.03527650237083435}, {"id": 1407, "seek": 423438, "start": 4243.34,
  "end": 4247.34, "text": " but yeah, obviously I would love if you would join us",
  "tokens": [50812, 457, 1338, 11, 2745, 286, 576, 959, 498, 291, 576, 3917, 505,
  51012], "temperature": 0.0, "avg_logprob": -0.34484953629343135, "compression_ratio":
  1.626923076923077, "no_speech_prob": 0.03527650237083435}, {"id": 1408, "seek":
  423438, "start": 4247.34, "end": 4249.22, "text": " in the course, it''ll be fun.",
  "tokens": [51012, 294, 264, 1164, 11, 309, 603, 312, 1019, 13, 51106], "temperature":
  0.0, "avg_logprob": -0.34484953629343135, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.03527650237083435}, {"id": 1409, "seek": 423438, "start": 4250.1,
  "end": 4253.14, "text": " Debo Brata is asking, what do you think", "tokens": [51150,
  1346, 1763, 1603, 3274, 307, 3365, 11, 437, 360, 291, 519, 51302], "temperature":
  0.0, "avg_logprob": -0.34484953629343135, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.03527650237083435}, {"id": 1410, "seek": 423438, "start": 4253.14,
  "end": 4255.74, "text": " about some of the reputable search sites,", "tokens":
  [51302, 466, 512, 295, 264, 1085, 32148, 3164, 7533, 11, 51432], "temperature":
  0.0, "avg_logprob": -0.34484953629343135, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.03527650237083435}, {"id": 1411, "seek": 423438, "start": 4255.74,
  "end": 4259.900000000001, "text": " like in Deden, LinkedIn, where searching for
  a male engineer", "tokens": [51432, 411, 294, 413, 6876, 11, 20657, 11, 689, 10808,
  337, 257, 7133, 11403, 51640], "temperature": 0.0, "avg_logprob": -0.34484953629343135,
  "compression_ratio": 1.626923076923077, "no_speech_prob": 0.03527650237083435},
  {"id": 1412, "seek": 423438, "start": 4259.900000000001, "end": 4262.34, "text":
  " will bring your results like data engineers", "tokens": [51640, 486, 1565, 428,
  3542, 411, 1412, 11955, 51762], "temperature": 0.0, "avg_logprob": -0.34484953629343135,
  "compression_ratio": 1.626923076923077, "no_speech_prob": 0.03527650237083435},
  {"id": 1413, "seek": 426234, "start": 4262.34, "end": 4265.82, "text": " and whatever
  unrelated stuff, not directly related stuff.", "tokens": [50364, 293, 2035, 38967,
  1507, 11, 406, 3838, 4077, 1507, 13, 50538], "temperature": 0.0, "avg_logprob":
  -0.2616902542114258, "compression_ratio": 1.7251184834123223, "no_speech_prob":
  0.0058535500429570675}, {"id": 1414, "seek": 426234, "start": 4265.82, "end": 4269.58,
  "text": " And so the question is why search documents", "tokens": [50538, 400, 370,
  264, 1168, 307, 983, 3164, 8512, 50726], "temperature": 0.0, "avg_logprob": -0.2616902542114258,
  "compression_ratio": 1.7251184834123223, "no_speech_prob": 0.0058535500429570675},
  {"id": 1415, "seek": 426234, "start": 4269.58, "end": 4271.9400000000005, "text":
  " not based on the entire user query, right?", "tokens": [50726, 406, 2361, 322,
  264, 2302, 4195, 14581, 11, 558, 30, 50844], "temperature": 0.0, "avg_logprob":
  -0.2616902542114258, "compression_ratio": 1.7251184834123223, "no_speech_prob":
  0.0058535500429570675}, {"id": 1416, "seek": 426234, "start": 4271.9400000000005,
  "end": 4272.900000000001, "text": " Only part of it.", "tokens": [50844, 5686, 644,
  295, 309, 13, 50892], "temperature": 0.0, "avg_logprob": -0.2616902542114258, "compression_ratio":
  1.7251184834123223, "no_speech_prob": 0.0058535500429570675}, {"id": 1417, "seek":
  426234, "start": 4277.58, "end": 4280.14, "text": " Sorry, I''m trying to understand
  the question", "tokens": [51126, 4919, 11, 286, 478, 1382, 281, 1223, 264, 1168,
  51254], "temperature": 0.0, "avg_logprob": -0.2616902542114258, "compression_ratio":
  1.7251184834123223, "no_speech_prob": 0.0058535500429570675}, {"id": 1418, "seek":
  426234, "start": 4280.14, "end": 4281.9800000000005, "text": " in relation to the
  wormhole vector topic.", "tokens": [51254, 294, 9721, 281, 264, 23835, 14094, 8062,
  4829, 13, 51346], "temperature": 0.0, "avg_logprob": -0.2616902542114258, "compression_ratio":
  1.7251184834123223, "no_speech_prob": 0.0058535500429570675}, {"id": 1419, "seek":
  426234, "start": 4283.58, "end": 4287.58, "text": " Yeah, I think it''s more, I
  think it''s less directly related.", "tokens": [51426, 865, 11, 286, 519, 309, 311,
  544, 11, 286, 519, 309, 311, 1570, 3838, 4077, 13, 51626], "temperature": 0.0, "avg_logprob":
  -0.2616902542114258, "compression_ratio": 1.7251184834123223, "no_speech_prob":
  0.0058535500429570675}, {"id": 1420, "seek": 426234, "start": 4287.58, "end": 4292.14,
  "text": " I think it''s more airing on the side of why data bias.", "tokens": [51626,
  286, 519, 309, 311, 544, 257, 5057, 322, 264, 1252, 295, 983, 1412, 12577, 13, 51854],
  "temperature": 0.0, "avg_logprob": -0.2616902542114258, "compression_ratio": 1.7251184834123223,
  "no_speech_prob": 0.0058535500429570675}, {"id": 1421, "seek": 429214, "start":
  4292.14, "end": 4296.700000000001, "text": " Why does reputable search sites do
  not sort of", "tokens": [50364, 1545, 775, 1085, 32148, 3164, 7533, 360, 406, 1333,
  295, 50592], "temperature": 0.0, "avg_logprob": -0.1610468796321324, "compression_ratio":
  1.6544715447154472, "no_speech_prob": 0.0005980291753076017}, {"id": 1422, "seek":
  429214, "start": 4296.700000000001, "end": 4301.06, "text": " utilize the semantic
  search, you know, one to one in a way?", "tokens": [50592, 16117, 264, 47982, 3164,
  11, 291, 458, 11, 472, 281, 472, 294, 257, 636, 30, 50810], "temperature": 0.0,
  "avg_logprob": -0.1610468796321324, "compression_ratio": 1.6544715447154472, "no_speech_prob":
  0.0005980291753076017}, {"id": 1423, "seek": 429214, "start": 4301.06, "end": 4301.900000000001,
  "text": " Yeah, I got you.", "tokens": [50810, 865, 11, 286, 658, 291, 13, 50852],
  "temperature": 0.0, "avg_logprob": -0.1610468796321324, "compression_ratio": 1.6544715447154472,
  "no_speech_prob": 0.0005980291753076017}, {"id": 1424, "seek": 429214, "start":
  4301.900000000001, "end": 4306.900000000001, "text": " I mean, the reality is that
  most AI-powered search algorithms,", "tokens": [50852, 286, 914, 11, 264, 4103,
  307, 300, 881, 7318, 12, 27178, 3164, 14642, 11, 51102], "temperature": 0.0, "avg_logprob":
  -0.1610468796321324, "compression_ratio": 1.6544715447154472, "no_speech_prob":
  0.0005980291753076017}, {"id": 1425, "seek": 429214, "start": 4308.5, "end": 4312.58,
  "text": " really all of them are used data and the data is biased, right?", "tokens":
  [51182, 534, 439, 295, 552, 366, 1143, 1412, 293, 264, 1412, 307, 28035, 11, 558,
  30, 51386], "temperature": 0.0, "avg_logprob": -0.1610468796321324, "compression_ratio":
  1.6544715447154472, "no_speech_prob": 0.0005980291753076017}, {"id": 1426, "seek":
  429214, "start": 4312.58, "end": 4315.06, "text": " So like the reality is in the
  world,", "tokens": [51386, 407, 411, 264, 4103, 307, 294, 264, 1002, 11, 51510],
  "temperature": 0.0, "avg_logprob": -0.1610468796321324, "compression_ratio": 1.6544715447154472,
  "no_speech_prob": 0.0005980291753076017}, {"id": 1427, "seek": 429214, "start":
  4315.06, "end": 4317.14, "text": " if you look at data engineering jobs,", "tokens":
  [51510, 498, 291, 574, 412, 1412, 7043, 4782, 11, 51614], "temperature": 0.0, "avg_logprob":
  -0.1610468796321324, "compression_ratio": 1.6544715447154472, "no_speech_prob":
  0.0005980291753076017}, {"id": 1428, "seek": 429214, "start": 4317.14, "end": 4320.04,
  "text": " they are more statistically skewed towards males", "tokens": [51614, 436,
  366, 544, 36478, 8756, 26896, 3030, 20776, 51759], "temperature": 0.0, "avg_logprob":
  -0.1610468796321324, "compression_ratio": 1.6544715447154472, "no_speech_prob":
  0.0005980291753076017}, {"id": 1429, "seek": 429214, "start": 4320.04, "end": 4321.26,
  "text": " being in those jobs and females.", "tokens": [51759, 885, 294, 729, 4782,
  293, 21529, 13, 51820], "temperature": 0.0, "avg_logprob": -0.1610468796321324,
  "compression_ratio": 1.6544715447154472, "no_speech_prob": 0.0005980291753076017},
  {"id": 1430, "seek": 432126, "start": 4321.26, "end": 4324.9800000000005, "text":
  " That doesn''t mean anything in terms of who can do the job", "tokens": [50364,
  663, 1177, 380, 914, 1340, 294, 2115, 295, 567, 393, 360, 264, 1691, 50550], "temperature":
  0.0, "avg_logprob": -0.13937093189784458, "compression_ratio": 1.740072202166065,
  "no_speech_prob": 0.0018295740010216832}, {"id": 1431, "seek": 432126, "start":
  4324.9800000000005, "end": 4325.820000000001, "text": " or who can''t.", "tokens":
  [50550, 420, 567, 393, 380, 13, 50592], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1432, "seek": 432126, "start": 4325.820000000001, "end": 4327.9400000000005,
  "text": " It''s just a reality that, you know,", "tokens": [50592, 467, 311, 445,
  257, 4103, 300, 11, 291, 458, 11, 50698], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1433, "seek": 432126, "start": 4327.9400000000005, "end": 4330.58, "text":
  " there tend to be more males in engineering", "tokens": [50698, 456, 3928, 281,
  312, 544, 20776, 294, 7043, 50830], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1434, "seek": 432126, "start": 4330.58, "end": 4332.42, "text": " and therefore
  the data is reflecting that.", "tokens": [50830, 293, 4412, 264, 1412, 307, 23543,
  300, 13, 50922], "temperature": 0.0, "avg_logprob": -0.13937093189784458, "compression_ratio":
  1.740072202166065, "no_speech_prob": 0.0018295740010216832}, {"id": 1435, "seek":
  432126, "start": 4332.42, "end": 4335.18, "text": " It would be nice to be able
  to take those biases out", "tokens": [50922, 467, 576, 312, 1481, 281, 312, 1075,
  281, 747, 729, 32152, 484, 51060], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1436, "seek": 432126, "start": 4335.18, "end": 4337.58, "text": " and in
  fact, there''s ways you can do that,", "tokens": [51060, 293, 294, 1186, 11, 456,
  311, 2098, 291, 393, 360, 300, 11, 51180], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1437, "seek": 432126, "start": 4337.58, "end": 4339.26, "text": " but they''re
  extra work.", "tokens": [51180, 457, 436, 434, 2857, 589, 13, 51264], "temperature":
  0.0, "avg_logprob": -0.13937093189784458, "compression_ratio": 1.740072202166065,
  "no_speech_prob": 0.0018295740010216832}, {"id": 1438, "seek": 432126, "start":
  4339.26, "end": 4341.22, "text": " And so the out of the box algorithms", "tokens":
  [51264, 400, 370, 264, 484, 295, 264, 2424, 14642, 51362], "temperature": 0.0, "avg_logprob":
  -0.13937093189784458, "compression_ratio": 1.740072202166065, "no_speech_prob":
  0.0018295740010216832}, {"id": 1439, "seek": 432126, "start": 4341.22, "end": 4343.74,
  "text": " that are typically employed don''t necessarily", "tokens": [51362, 300,
  366, 5850, 20115, 500, 380, 4725, 51488], "temperature": 0.0, "avg_logprob": -0.13937093189784458,
  "compression_ratio": 1.740072202166065, "no_speech_prob": 0.0018295740010216832},
  {"id": 1440, "seek": 432126, "start": 4343.74, "end": 4346.02, "text": " try to
  tackle those biases.", "tokens": [51488, 853, 281, 14896, 729, 32152, 13, 51602],
  "temperature": 0.0, "avg_logprob": -0.13937093189784458, "compression_ratio": 1.740072202166065,
  "no_speech_prob": 0.0018295740010216832}, {"id": 1441, "seek": 432126, "start":
  4346.02, "end": 4349.34, "text": " So yeah, I think it''s, I think it''s valiant
  to, you know,", "tokens": [51602, 407, 1338, 11, 286, 519, 309, 311, 11, 286, 519,
  309, 311, 1323, 5798, 281, 11, 291, 458, 11, 51768], "temperature": 0.0, "avg_logprob":
  -0.13937093189784458, "compression_ratio": 1.740072202166065, "no_speech_prob":
  0.0018295740010216832}, {"id": 1442, "seek": 434934, "start": 4349.34, "end": 4351.58,
  "text": " try to, especially when you''re dealing with things", "tokens": [50364,
  853, 281, 11, 2318, 562, 291, 434, 6260, 365, 721, 50476], "temperature": 0.0, "avg_logprob":
  -0.20804228502161362, "compression_ratio": 1.6989247311827957, "no_speech_prob":
  0.008751551620662212}, {"id": 1443, "seek": 434934, "start": 4351.58, "end": 4354.860000000001,
  "text": " like people''s livelihoods and, you know, careers", "tokens": [50476,
  411, 561, 311, 34343, 82, 293, 11, 291, 458, 11, 16409, 50640], "temperature": 0.0,
  "avg_logprob": -0.20804228502161362, "compression_ratio": 1.6989247311827957, "no_speech_prob":
  0.008751551620662212}, {"id": 1444, "seek": 434934, "start": 4354.860000000001,
  "end": 4356.66, "text": " and things like that, I think it''s,", "tokens": [50640,
  293, 721, 411, 300, 11, 286, 519, 309, 311, 11, 50730], "temperature": 0.0, "avg_logprob":
  -0.20804228502161362, "compression_ratio": 1.6989247311827957, "no_speech_prob":
  0.008751551620662212}, {"id": 1445, "seek": 434934, "start": 4356.66, "end": 4360.06,
  "text": " it''s a great exercise and something they should focus on,", "tokens":
  [50730, 309, 311, 257, 869, 5380, 293, 746, 436, 820, 1879, 322, 11, 50900], "temperature":
  0.0, "avg_logprob": -0.20804228502161362, "compression_ratio": 1.6989247311827957,
  "no_speech_prob": 0.008751551620662212}, {"id": 1446, "seek": 434934, "start": 4360.06,
  "end": 4362.22, "text": " but it''s like, unfortunately,", "tokens": [50900, 457,
  309, 311, 411, 11, 7015, 11, 51008], "temperature": 0.0, "avg_logprob": -0.20804228502161362,
  "compression_ratio": 1.6989247311827957, "no_speech_prob": 0.008751551620662212},
  {"id": 1447, "seek": 434934, "start": 4362.22, "end": 4364.3, "text": " kind of
  a reality of the underlying data", "tokens": [51008, 733, 295, 257, 4103, 295, 264,
  14217, 1412, 51112], "temperature": 0.0, "avg_logprob": -0.20804228502161362, "compression_ratio":
  1.6989247311827957, "no_speech_prob": 0.008751551620662212}, {"id": 1448, "seek":
  434934, "start": 4364.3, "end": 4366.58, "text": " that''s being bubbled up, I think.",
  "tokens": [51112, 300, 311, 885, 13045, 1493, 493, 11, 286, 519, 13, 51226], "temperature":
  0.0, "avg_logprob": -0.20804228502161362, "compression_ratio": 1.6989247311827957,
  "no_speech_prob": 0.008751551620662212}, {"id": 1449, "seek": 434934, "start": 4366.58,
  "end": 4367.42, "text": " Yeah.", "tokens": [51226, 865, 13, 51268], "temperature":
  0.0, "avg_logprob": -0.20804228502161362, "compression_ratio": 1.6989247311827957,
  "no_speech_prob": 0.008751551620662212}, {"id": 1450, "seek": 434934, "start": 4367.42,
  "end": 4368.46, "text": " My take is that I-", "tokens": [51268, 1222, 747, 307,
  300, 286, 12, 51320], "temperature": 0.0, "avg_logprob": -0.20804228502161362, "compression_ratio":
  1.6989247311827957, "no_speech_prob": 0.008751551620662212}, {"id": 1451, "seek":
  434934, "start": 4368.46, "end": 4370.02, "text": " The data is biased.", "tokens":
  [51320, 440, 1412, 307, 28035, 13, 51398], "temperature": 0.0, "avg_logprob": -0.20804228502161362,
  "compression_ratio": 1.6989247311827957, "no_speech_prob": 0.008751551620662212},
  {"id": 1452, "seek": 434934, "start": 4370.02, "end": 4371.02, "text": " Yeah, I
  agree.", "tokens": [51398, 865, 11, 286, 3986, 13, 51448], "temperature": 0.0, "avg_logprob":
  -0.20804228502161362, "compression_ratio": 1.6989247311827957, "no_speech_prob":
  0.008751551620662212}, {"id": 1453, "seek": 434934, "start": 4371.02, "end": 4374.18,
  "text": " I''ve been one job search engine like a couple companies ago", "tokens":
  [51448, 286, 600, 668, 472, 1691, 3164, 2848, 411, 257, 1916, 3431, 2057, 51606],
  "temperature": 0.0, "avg_logprob": -0.20804228502161362, "compression_ratio": 1.6989247311827957,
  "no_speech_prob": 0.008751551620662212}, {"id": 1454, "seek": 434934, "start": 4374.18,
  "end": 4377.860000000001, "text": " and my take is that probably these companies
  are trying", "tokens": [51606, 293, 452, 747, 307, 300, 1391, 613, 3431, 366, 1382,
  51790], "temperature": 0.0, "avg_logprob": -0.20804228502161362, "compression_ratio":
  1.6989247311827957, "no_speech_prob": 0.008751551620662212}, {"id": 1455, "seek":
  437786, "start": 4377.86, "end": 4382.86, "text": " to avoid, you know, these traps
  when your super,", "tokens": [50364, 281, 5042, 11, 291, 458, 11, 613, 24173, 562,
  428, 1687, 11, 50614], "temperature": 0.0, "avg_logprob": -0.19890231530643204,
  "compression_ratio": 1.5860655737704918, "no_speech_prob": 0.006218739319592714},
  {"id": 1456, "seek": 437786, "start": 4382.86, "end": 4386.42, "text": " super precise
  query will either lead to nothing", "tokens": [50614, 1687, 13600, 14581, 486, 2139,
  1477, 281, 1825, 50792], "temperature": 0.0, "avg_logprob": -0.19890231530643204,
  "compression_ratio": 1.5860655737704918, "no_speech_prob": 0.006218739319592714},
  {"id": 1457, "seek": 437786, "start": 4386.42, "end": 4388.78, "text": " or lead
  to just a couple of jobs on the screen", "tokens": [50792, 420, 1477, 281, 445,
  257, 1916, 295, 4782, 322, 264, 2568, 50910], "temperature": 0.0, "avg_logprob":
  -0.19890231530643204, "compression_ratio": 1.5860655737704918, "no_speech_prob":
  0.006218739319592714}, {"id": 1458, "seek": 437786, "start": 4388.78, "end": 4391.86,
  "text": " because their business is to show you as many jobs as possible", "tokens":
  [50910, 570, 641, 1606, 307, 281, 855, 291, 382, 867, 4782, 382, 1944, 51064], "temperature":
  0.0, "avg_logprob": -0.19890231530643204, "compression_ratio": 1.5860655737704918,
  "no_speech_prob": 0.006218739319592714}, {"id": 1459, "seek": 437786, "start": 4391.86,
  "end": 4393.94, "text": " so that they can monetize that.", "tokens": [51064, 370,
  300, 436, 393, 15556, 1125, 300, 13, 51168], "temperature": 0.0, "avg_logprob":
  -0.19890231530643204, "compression_ratio": 1.5860655737704918, "no_speech_prob":
  0.006218739319592714}, {"id": 1460, "seek": 437786, "start": 4393.94, "end": 4397.0599999999995,
  "text": " So it''s all about maybe like business element as well.", "tokens": [51168,
  407, 309, 311, 439, 466, 1310, 411, 1606, 4478, 382, 731, 13, 51324], "temperature":
  0.0, "avg_logprob": -0.19890231530643204, "compression_ratio": 1.5860655737704918,
  "no_speech_prob": 0.006218739319592714}, {"id": 1461, "seek": 437786, "start": 4397.0599999999995,
  "end": 4401.0199999999995, "text": " But I''m sure there are other technical aspects
  of this,", "tokens": [51324, 583, 286, 478, 988, 456, 366, 661, 6191, 7270, 295,
  341, 11, 51522], "temperature": 0.0, "avg_logprob": -0.19890231530643204, "compression_ratio":
  1.5860655737704918, "no_speech_prob": 0.006218739319592714}, {"id": 1462, "seek":
  437786, "start": 4401.0199999999995, "end": 4403.179999999999, "text": " which we
  should note disregard.", "tokens": [51522, 597, 321, 820, 3637, 44493, 13, 51630],
  "temperature": 0.0, "avg_logprob": -0.19890231530643204, "compression_ratio": 1.5860655737704918,
  "no_speech_prob": 0.006218739319592714}, {"id": 1463, "seek": 437786, "start": 4404.66,
  "end": 4405.5, "text": " Sure.", "tokens": [51704, 4894, 13, 51746], "temperature":
  0.0, "avg_logprob": -0.19890231530643204, "compression_ratio": 1.5860655737704918,
  "no_speech_prob": 0.006218739319592714}, {"id": 1464, "seek": 440550, "start": 4406.46,
  "end": 4409.1, "text": " The next question is from Arjun.", "tokens": [50412, 440,
  958, 1168, 307, 490, 1587, 10010, 13, 50544], "temperature": 0.0, "avg_logprob":
  -0.3238900320870536, "compression_ratio": 1.7053571428571428, "no_speech_prob":
  0.000620715320110321}, {"id": 1465, "seek": 440550, "start": 4409.1, "end": 4412.02,
  "text": " And you experience how much do the following results differ?", "tokens":
  [50544, 400, 291, 1752, 577, 709, 360, 264, 3480, 3542, 743, 30, 50690], "temperature":
  0.0, "avg_logprob": -0.3238900320870536, "compression_ratio": 1.7053571428571428,
  "no_speech_prob": 0.000620715320110321}, {"id": 1466, "seek": 440550, "start": 4412.02,
  "end": 4416.42, "text": " First, query against dense vector space directly.", "tokens":
  [50690, 2386, 11, 14581, 1970, 18011, 8062, 1901, 3838, 13, 50910], "temperature":
  0.0, "avg_logprob": -0.3238900320870536, "compression_ratio": 1.7053571428571428,
  "no_speech_prob": 0.000620715320110321}, {"id": 1467, "seek": 440550, "start": 4416.42,
  "end": 4420.1, "text": " And the second query in sparse vector space", "tokens":
  [50910, 400, 264, 1150, 14581, 294, 637, 11668, 8062, 1901, 51094], "temperature":
  0.0, "avg_logprob": -0.3238900320870536, "compression_ratio": 1.7053571428571428,
  "no_speech_prob": 0.000620715320110321}, {"id": 1468, "seek": 440550, "start": 4420.1,
  "end": 4422.02, "text": " and wormhole to dense vector space", "tokens": [51094,
  293, 23835, 14094, 281, 18011, 8062, 1901, 51190], "temperature": 0.0, "avg_logprob":
  -0.3238900320870536, "compression_ratio": 1.7053571428571428, "no_speech_prob":
  0.000620715320110321}, {"id": 1469, "seek": 440550, "start": 4422.02, "end": 4423.78,
  "text": " and finally get the docs that are similar", "tokens": [51190, 293, 2721,
  483, 264, 45623, 300, 366, 2531, 51278], "temperature": 0.0, "avg_logprob": -0.3238900320870536,
  "compression_ratio": 1.7053571428571428, "no_speech_prob": 0.000620715320110321},
  {"id": 1470, "seek": 440550, "start": 4423.78, "end": 4426.66, "text": " to the
  wormhole vector average vector.", "tokens": [51278, 281, 264, 23835, 14094, 8062,
  4274, 8062, 13, 51422], "temperature": 0.0, "avg_logprob": -0.3238900320870536,
  "compression_ratio": 1.7053571428571428, "no_speech_prob": 0.000620715320110321},
  {"id": 1471, "seek": 440550, "start": 4428.5, "end": 4430.3, "text": " So what''s
  the question?", "tokens": [51514, 407, 437, 311, 264, 1168, 30, 51604], "temperature":
  0.0, "avg_logprob": -0.3238900320870536, "compression_ratio": 1.7053571428571428,
  "no_speech_prob": 0.000620715320110321}, {"id": 1472, "seek": 440550, "start": 4430.3,
  "end": 4431.06, "text": " That''s the answer.", "tokens": [51604, 663, 311, 264,
  1867, 13, 51642], "temperature": 0.0, "avg_logprob": -0.3238900320870536, "compression_ratio":
  1.7053571428571428, "no_speech_prob": 0.000620715320110321}, {"id": 1473, "seek":
  440550, "start": 4431.06, "end": 4433.78, "text": " I mean, at the end of the day,
  the,", "tokens": [51642, 286, 914, 11, 412, 264, 917, 295, 264, 786, 11, 264, 11,
  51778], "temperature": 0.0, "avg_logprob": -0.3238900320870536, "compression_ratio":
  1.7053571428571428, "no_speech_prob": 0.000620715320110321}, {"id": 1474, "seek":
  443378, "start": 4433.78, "end": 4437.74, "text": " if you have a query that you
  run against your lexical space", "tokens": [50364, 498, 291, 362, 257, 14581, 300,
  291, 1190, 1970, 428, 476, 87, 804, 1901, 50562], "temperature": 0.0, "avg_logprob":
  -0.15940138670775267, "compression_ratio": 1.8608695652173912, "no_speech_prob":
  3.71196074411273e-05}, {"id": 1475, "seek": 443378, "start": 4437.74, "end": 4442.74,
  "text": " that matches mostly documents that are related to the query", "tokens":
  [50562, 300, 10676, 5240, 8512, 300, 366, 4077, 281, 264, 14581, 50812], "temperature":
  0.0, "avg_logprob": -0.15940138670775267, "compression_ratio": 1.8608695652173912,
  "no_speech_prob": 3.71196074411273e-05}, {"id": 1476, "seek": 443378, "start": 4443.259999999999,
  "end": 4446.74, "text": " and then you hop over to the dense space,", "tokens":
  [50838, 293, 550, 291, 3818, 670, 281, 264, 18011, 1901, 11, 51012], "temperature":
  0.0, "avg_logprob": -0.15940138670775267, "compression_ratio": 1.8608695652173912,
  "no_speech_prob": 3.71196074411273e-05}, {"id": 1477, "seek": 443378, "start": 4446.74,
  "end": 4448.86, "text": " you''re typically gonna get a lot of overlap", "tokens":
  [51012, 291, 434, 5850, 799, 483, 257, 688, 295, 19959, 51118], "temperature": 0.0,
  "avg_logprob": -0.15940138670775267, "compression_ratio": 1.8608695652173912, "no_speech_prob":
  3.71196074411273e-05}, {"id": 1478, "seek": 443378, "start": 4448.86, "end": 4451.82,
  "text": " because the lexical space semantics", "tokens": [51118, 570, 264, 476,
  87, 804, 1901, 4361, 45298, 51266], "temperature": 0.0, "avg_logprob": -0.15940138670775267,
  "compression_ratio": 1.8608695652173912, "no_speech_prob": 3.71196074411273e-05},
  {"id": 1479, "seek": 443378, "start": 4451.82, "end": 4454.46, "text": " are going
  to be very similar to the dense vector space", "tokens": [51266, 366, 516, 281,
  312, 588, 2531, 281, 264, 18011, 8062, 1901, 51398], "temperature": 0.0, "avg_logprob":
  -0.15940138670775267, "compression_ratio": 1.8608695652173912, "no_speech_prob":
  3.71196074411273e-05}, {"id": 1480, "seek": 443378, "start": 4454.46, "end": 4456.78,
  "text": " semantics in terms of like the underlying meaning.", "tokens": [51398,
  4361, 45298, 294, 2115, 295, 411, 264, 14217, 3620, 13, 51514], "temperature": 0.0,
  "avg_logprob": -0.15940138670775267, "compression_ratio": 1.8608695652173912, "no_speech_prob":
  3.71196074411273e-05}, {"id": 1481, "seek": 443378, "start": 4458.139999999999,
  "end": 4460.74, "text": " If you were to take the lexical space", "tokens": [51582,
  759, 291, 645, 281, 747, 264, 476, 87, 804, 1901, 51712], "temperature": 0.0, "avg_logprob":
  -0.15940138670775267, "compression_ratio": 1.8608695652173912, "no_speech_prob":
  3.71196074411273e-05}, {"id": 1482, "seek": 443378, "start": 4460.74, "end": 4463.099999999999,
  "text": " and I should mention, you can actually use", "tokens": [51712, 293, 286,
  820, 2152, 11, 291, 393, 767, 764, 51830], "temperature": 0.0, "avg_logprob": -0.15940138670775267,
  "compression_ratio": 1.8608695652173912, "no_speech_prob": 3.71196074411273e-05},
  {"id": 1483, "seek": 446310, "start": 4463.1, "end": 4465.38, "text": " the wormhole
  vector in the same vector space.", "tokens": [50364, 264, 23835, 14094, 8062, 294,
  264, 912, 8062, 1901, 13, 50478], "temperature": 0.0, "avg_logprob": -0.15093188815646702,
  "compression_ratio": 1.783882783882784, "no_speech_prob": 0.00045594366383738816},
  {"id": 1484, "seek": 446310, "start": 4465.38, "end": 4468.860000000001, "text":
  " I kind of showed that with like taking a query like lasagna", "tokens": [50478,
  286, 733, 295, 4712, 300, 365, 411, 1940, 257, 14581, 411, 2439, 35697, 50652],
  "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio": 1.783882783882784,
  "no_speech_prob": 0.00045594366383738816}, {"id": 1485, "seek": 446310, "start":
  4468.860000000001, "end": 4473.3, "text": " and then rewriting it with a more expanded
  out lexical query", "tokens": [50652, 293, 550, 319, 19868, 309, 365, 257, 544,
  14342, 484, 476, 87, 804, 14581, 50874], "temperature": 0.0, "avg_logprob": -0.15093188815646702,
  "compression_ratio": 1.783882783882784, "no_speech_prob": 0.00045594366383738816},
  {"id": 1486, "seek": 446310, "start": 4473.3, "end": 4474.820000000001, "text":
  " with a category of Italian.", "tokens": [50874, 365, 257, 7719, 295, 10003, 13,
  50950], "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio":
  1.783882783882784, "no_speech_prob": 0.00045594366383738816}, {"id": 1487, "seek":
  446310, "start": 4474.820000000001, "end": 4476.9400000000005, "text": " And so
  you don''t have to actually jump", "tokens": [50950, 400, 370, 291, 500, 380, 362,
  281, 767, 3012, 51056], "temperature": 0.0, "avg_logprob": -0.15093188815646702,
  "compression_ratio": 1.783882783882784, "no_speech_prob": 0.00045594366383738816},
  {"id": 1488, "seek": 446310, "start": 4476.9400000000005, "end": 4478.14, "text":
  " between different vector spaces.", "tokens": [51056, 1296, 819, 8062, 7673, 13,
  51116], "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio":
  1.783882783882784, "no_speech_prob": 0.00045594366383738816}, {"id": 1489, "seek":
  446310, "start": 4478.14, "end": 4480.5, "text": " You can even jump within the
  same vector space.", "tokens": [51116, 509, 393, 754, 3012, 1951, 264, 912, 8062,
  1901, 13, 51234], "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio":
  1.783882783882784, "no_speech_prob": 0.00045594366383738816}, {"id": 1490, "seek":
  446310, "start": 4480.5, "end": 4484.620000000001, "text": " And I think that in
  this context,", "tokens": [51234, 400, 286, 519, 300, 294, 341, 4319, 11, 51440],
  "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio": 1.783882783882784,
  "no_speech_prob": 0.00045594366383738816}, {"id": 1491, "seek": 446310, "start":
  4484.620000000001, "end": 4488.22, "text": " the more similar, the meaning of the
  underlying set", "tokens": [51440, 264, 544, 2531, 11, 264, 3620, 295, 264, 14217,
  992, 51620], "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio":
  1.783882783882784, "no_speech_prob": 0.00045594366383738816}, {"id": 1492, "seek":
  446310, "start": 4488.22, "end": 4490.3, "text": " of documents is matching each
  query,", "tokens": [51620, 295, 8512, 307, 14324, 1184, 14581, 11, 51724], "temperature":
  0.0, "avg_logprob": -0.15093188815646702, "compression_ratio": 1.783882783882784,
  "no_speech_prob": 0.00045594366383738816}, {"id": 1493, "seek": 446310, "start":
  4490.3, "end": 4492.46, "text": " the more interesting you''re gonna be able to
  find", "tokens": [51724, 264, 544, 1880, 291, 434, 799, 312, 1075, 281, 915, 51832],
  "temperature": 0.0, "avg_logprob": -0.15093188815646702, "compression_ratio": 1.783882783882784,
  "no_speech_prob": 0.00045594366383738816}, {"id": 1494, "seek": 449246, "start":
  4492.5, "end": 4495.18, "text": " missing links in the other vector space.", "tokens":
  [50366, 5361, 6123, 294, 264, 661, 8062, 1901, 13, 50500], "temperature": 0.0, "avg_logprob":
  -0.20068416595458985, "compression_ratio": 1.725868725868726, "no_speech_prob":
  0.00027209712425246835}, {"id": 1495, "seek": 449246, "start": 4495.18, "end": 4496.86,
  "text": " If you have very orthogonal queries,", "tokens": [50500, 759, 291, 362,
  588, 41488, 24109, 11, 50584], "temperature": 0.0, "avg_logprob": -0.20068416595458985,
  "compression_ratio": 1.725868725868726, "no_speech_prob": 0.00027209712425246835},
  {"id": 1496, "seek": 449246, "start": 4496.86, "end": 4500.82, "text": " like you
  can imagine on the lexical side searching for", "tokens": [50584, 411, 291, 393,
  3811, 322, 264, 476, 87, 804, 1252, 10808, 337, 50782], "temperature": 0.0, "avg_logprob":
  -0.20068416595458985, "compression_ratio": 1.725868725868726, "no_speech_prob":
  0.00027209712425246835}, {"id": 1497, "seek": 449246, "start": 4500.82, "end": 4505.82,
  "text": " orange juice and Nintendo switch, right?", "tokens": [50782, 7671, 8544,
  293, 11578, 3679, 11, 558, 30, 51032], "temperature": 0.0, "avg_logprob": -0.20068416595458985,
  "compression_ratio": 1.725868725868726, "no_speech_prob": 0.00027209712425246835},
  {"id": 1498, "seek": 449246, "start": 4505.82, "end": 4507.58, "text": " Or you''ll
  get nothing for that,", "tokens": [51032, 1610, 291, 603, 483, 1825, 337, 300, 11,
  51120], "temperature": 0.0, "avg_logprob": -0.20068416595458985, "compression_ratio":
  1.725868725868726, "no_speech_prob": 0.00027209712425246835}, {"id": 1499, "seek":
  449246, "start": 4507.58, "end": 4509.06, "text": " but orange juice or Nintendo
  switch.", "tokens": [51120, 457, 7671, 8544, 420, 11578, 3679, 13, 51194], "temperature":
  0.0, "avg_logprob": -0.20068416595458985, "compression_ratio": 1.725868725868726,
  "no_speech_prob": 0.00027209712425246835}, {"id": 1500, "seek": 449246, "start":
  4509.06, "end": 4511.82, "text": " Well, you basically end up with a document set",
  "tokens": [51194, 1042, 11, 291, 1936, 917, 493, 365, 257, 4166, 992, 51332], "temperature":
  0.0, "avg_logprob": -0.20068416595458985, "compression_ratio": 1.725868725868726,
  "no_speech_prob": 0.00027209712425246835}, {"id": 1501, "seek": 449246, "start":
  4511.82, "end": 4514.38, "text": " that is really two separate document sets, right?",
  "tokens": [51332, 300, 307, 534, 732, 4994, 4166, 6352, 11, 558, 30, 51460], "temperature":
  0.0, "avg_logprob": -0.20068416595458985, "compression_ratio": 1.725868725868726,
  "no_speech_prob": 0.00027209712425246835}, {"id": 1502, "seek": 449246, "start":
  4514.38, "end": 4516.46, "text": " It''s like there''s not a lot of overlap", "tokens":
  [51460, 467, 311, 411, 456, 311, 406, 257, 688, 295, 19959, 51564], "temperature":
  0.0, "avg_logprob": -0.20068416595458985, "compression_ratio": 1.725868725868726,
  "no_speech_prob": 0.00027209712425246835}, {"id": 1503, "seek": 449246, "start":
  4516.46, "end": 4518.14, "text": " and if you hop over to the dense space", "tokens":
  [51564, 293, 498, 291, 3818, 670, 281, 264, 18011, 1901, 51648], "temperature":
  0.0, "avg_logprob": -0.20068416595458985, "compression_ratio": 1.725868725868726,
  "no_speech_prob": 0.00027209712425246835}, {"id": 1504, "seek": 449246, "start":
  4518.14, "end": 4520.3, "text": " and get the average of those,", "tokens": [51648,
  293, 483, 264, 4274, 295, 729, 11, 51756], "temperature": 0.0, "avg_logprob": -0.20068416595458985,
  "compression_ratio": 1.725868725868726, "no_speech_prob": 0.00027209712425246835},
  {"id": 1505, "seek": 452030, "start": 4521.26, "end": 4523.66, "text": " there''s
  still gonna be things that are like", "tokens": [50412, 456, 311, 920, 799, 312,
  721, 300, 366, 411, 50532], "temperature": 0.0, "avg_logprob": -0.13911766383958898,
  "compression_ratio": 1.7453874538745386, "no_speech_prob": 0.004013934638351202},
  {"id": 1506, "seek": 452030, "start": 4523.66, "end": 4526.820000000001, "text":
  " probably close to Nintendo switch", "tokens": [50532, 1391, 1998, 281, 11578,
  3679, 50690], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1507, "seek":
  452030, "start": 4526.820000000001, "end": 4529.860000000001, "text": " and probably
  close to orange, but the more different", "tokens": [50690, 293, 1391, 1998, 281,
  7671, 11, 457, 264, 544, 819, 50842], "temperature": 0.0, "avg_logprob": -0.13911766383958898,
  "compression_ratio": 1.7453874538745386, "no_speech_prob": 0.004013934638351202},
  {"id": 1508, "seek": 452030, "start": 4529.860000000001, "end": 4532.46, "text":
  " those things are, you might get some weird stuff in between.", "tokens": [50842,
  729, 721, 366, 11, 291, 1062, 483, 512, 3657, 1507, 294, 1296, 13, 50972], "temperature":
  0.0, "avg_logprob": -0.13911766383958898, "compression_ratio": 1.7453874538745386,
  "no_speech_prob": 0.004013934638351202}, {"id": 1509, "seek": 452030, "start": 4532.46,
  "end": 4535.900000000001, "text": " Because you''re now looking across two different
  places,", "tokens": [50972, 1436, 291, 434, 586, 1237, 2108, 732, 819, 3190, 11,
  51144], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1510, "seek":
  452030, "start": 4535.900000000001, "end": 4539.02, "text": " any Nintendo switch
  stuff that''s orange", "tokens": [51144, 604, 11578, 3679, 1507, 300, 311, 7671,
  51300], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1511, "seek":
  452030, "start": 4539.02, "end": 4540.860000000001, "text": " or related to juice
  or something might show up,", "tokens": [51300, 420, 4077, 281, 8544, 420, 746,
  1062, 855, 493, 11, 51392], "temperature": 0.0, "avg_logprob": -0.13911766383958898,
  "compression_ratio": 1.7453874538745386, "no_speech_prob": 0.004013934638351202},
  {"id": 1512, "seek": 452030, "start": 4540.860000000001, "end": 4542.62, "text":
  " but it''s gonna be weird.", "tokens": [51392, 457, 309, 311, 799, 312, 3657, 13,
  51480], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1513, "seek":
  452030, "start": 4542.62, "end": 4545.7, "text": " And so this isn''t like a magical
  silver bullet", "tokens": [51480, 400, 370, 341, 1943, 380, 411, 257, 12066, 8753,
  11632, 51634], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1514, "seek":
  452030, "start": 4545.7, "end": 4547.38, "text": " that solves every query understanding",
  "tokens": [51634, 300, 39890, 633, 14581, 3701, 51718], "temperature": 0.0, "avg_logprob":
  -0.13911766383958898, "compression_ratio": 1.7453874538745386, "no_speech_prob":
  0.004013934638351202}, {"id": 1515, "seek": 452030, "start": 4547.38, "end": 4548.62,
  "text": " or every relevance problem.", "tokens": [51718, 420, 633, 32684, 1154,
  13, 51780], "temperature": 0.0, "avg_logprob": -0.13911766383958898, "compression_ratio":
  1.7453874538745386, "no_speech_prob": 0.004013934638351202}, {"id": 1516, "seek":
  454862, "start": 4548.62, "end": 4550.86, "text": " It''s just another tool in our
  toolkit", "tokens": [50364, 467, 311, 445, 1071, 2290, 294, 527, 40167, 50476],
  "temperature": 0.0, "avg_logprob": -0.26807504736858867, "compression_ratio": 1.6869918699186992,
  "no_speech_prob": 0.00042176118586212397}, {"id": 1517, "seek": 454862, "start":
  4550.86, "end": 4553.94, "text": " to be able to better reason about the underlying
  documents", "tokens": [50476, 281, 312, 1075, 281, 1101, 1778, 466, 264, 14217,
  8512, 50630], "temperature": 0.0, "avg_logprob": -0.26807504736858867, "compression_ratio":
  1.6869918699186992, "no_speech_prob": 0.00042176118586212397}, {"id": 1518, "seek":
  454862, "start": 4553.94, "end": 4556.5, "text": " and queries and to explain queries",
  "tokens": [50630, 293, 24109, 293, 281, 2903, 24109, 50758], "temperature": 0.0,
  "avg_logprob": -0.26807504736858867, "compression_ratio": 1.6869918699186992, "no_speech_prob":
  0.00042176118586212397}, {"id": 1519, "seek": 454862, "start": 4556.5, "end": 4560.14,
  "text": " in another modality, if you will, another query modality.", "tokens":
  [50758, 294, 1071, 1072, 1860, 11, 498, 291, 486, 11, 1071, 14581, 1072, 1860, 13,
  50940], "temperature": 0.0, "avg_logprob": -0.26807504736858867, "compression_ratio":
  1.6869918699186992, "no_speech_prob": 0.00042176118586212397}, {"id": 1520, "seek":
  454862, "start": 4560.14, "end": 4562.0199999999995, "text": " Yeah, in other words,
  what your searching for", "tokens": [50940, 865, 11, 294, 661, 2283, 11, 437, 428,
  10808, 337, 51034], "temperature": 0.0, "avg_logprob": -0.26807504736858867, "compression_ratio":
  1.6869918699186992, "no_speech_prob": 0.00042176118586212397}, {"id": 1521, "seek":
  454862, "start": 4562.0199999999995, "end": 4564.18, "text": " should still kind
  of make sense.", "tokens": [51034, 820, 920, 733, 295, 652, 2020, 13, 51142], "temperature":
  0.0, "avg_logprob": -0.26807504736858867, "compression_ratio": 1.6869918699186992,
  "no_speech_prob": 0.00042176118586212397}, {"id": 1522, "seek": 454862, "start":
  4564.18, "end": 4565.0199999999995, "text": " Yeah, yeah.", "tokens": [51142, 865,
  11, 1338, 13, 51184], "temperature": 0.0, "avg_logprob": -0.26807504736858867, "compression_ratio":
  1.6869918699186992, "no_speech_prob": 0.00042176118586212397}, {"id": 1523, "seek":
  454862, "start": 4565.0199999999995, "end": 4568.94, "text": " So if it does, it
  probably will return some useful results.", "tokens": [51184, 407, 498, 309, 775,
  11, 309, 1391, 486, 2736, 512, 4420, 3542, 13, 51380], "temperature": 0.0, "avg_logprob":
  -0.26807504736858867, "compression_ratio": 1.6869918699186992, "no_speech_prob":
  0.00042176118586212397}, {"id": 1524, "seek": 454862, "start": 4569.78, "end": 4572.62,
  "text": " Tips say, thank you, thank you, tips.", "tokens": [51422, 36887, 584,
  11, 1309, 291, 11, 1309, 291, 11, 6082, 13, 51564], "temperature": 0.0, "avg_logprob":
  -0.26807504736858867, "compression_ratio": 1.6869918699186992, "no_speech_prob":
  0.00042176118586212397}, {"id": 1525, "seek": 454862, "start": 4572.62, "end": 4577.62,
  "text": " Rustem says, you know, the impact of", "tokens": [51564, 34952, 443, 1619,
  11, 291, 458, 11, 264, 2712, 295, 51814], "temperature": 0.0, "avg_logprob": -0.26807504736858867,
  "compression_ratio": 1.6869918699186992, "no_speech_prob": 0.00042176118586212397},
  {"id": 1526, "seek": 457762, "start": 4577.62, "end": 4580.0199999999995, "text":
  " documents'' segmentation, so basically,", "tokens": [50364, 8512, 6, 9469, 399,
  11, 370, 1936, 11, 50484], "temperature": 0.0, "avg_logprob": -0.24571891959386927,
  "compression_ratio": 1.782442748091603, "no_speech_prob": 0.00192662060726434},
  {"id": 1527, "seek": 457762, "start": 4580.0199999999995, "end": 4582.5, "text":
  " what are the suggestions to improve that", "tokens": [50484, 437, 366, 264, 13396,
  281, 3470, 300, 50608], "temperature": 0.0, "avg_logprob": -0.24571891959386927,
  "compression_ratio": 1.782442748091603, "no_speech_prob": 0.00192662060726434},
  {"id": 1528, "seek": 457762, "start": 4582.5, "end": 4586.42, "text": " so that
  wormhole vectors would be useful?", "tokens": [50608, 370, 300, 23835, 14094, 18875,
  576, 312, 4420, 30, 50804], "temperature": 0.0, "avg_logprob": -0.24571891959386927,
  "compression_ratio": 1.782442748091603, "no_speech_prob": 0.00192662060726434},
  {"id": 1529, "seek": 457762, "start": 4586.42, "end": 4587.26, "text": " Yeah, I
  think-", "tokens": [50804, 865, 11, 286, 519, 12, 50846], "temperature": 0.0, "avg_logprob":
  -0.24571891959386927, "compression_ratio": 1.782442748091603, "no_speech_prob":
  0.00192662060726434}, {"id": 1530, "seek": 457762, "start": 4587.26, "end": 4588.42,
  "text": " Especially for much documents.", "tokens": [50846, 8545, 337, 709, 8512,
  13, 50904], "temperature": 0.0, "avg_logprob": -0.24571891959386927, "compression_ratio":
  1.782442748091603, "no_speech_prob": 0.00192662060726434}, {"id": 1531, "seek":
  457762, "start": 4588.42, "end": 4590.82, "text": " Yeah, I mean, I think it''s
  common sense,", "tokens": [50904, 865, 11, 286, 914, 11, 286, 519, 309, 311, 2689,
  2020, 11, 51024], "temperature": 0.0, "avg_logprob": -0.24571891959386927, "compression_ratio":
  1.782442748091603, "no_speech_prob": 0.00192662060726434}, {"id": 1532, "seek":
  457762, "start": 4590.82, "end": 4593.0199999999995, "text": " like the same way
  that you would chunk documents", "tokens": [51024, 411, 264, 912, 636, 300, 291,
  576, 16635, 8512, 51134], "temperature": 0.0, "avg_logprob": -0.24571891959386927,
  "compression_ratio": 1.782442748091603, "no_speech_prob": 0.00192662060726434},
  {"id": 1533, "seek": 457762, "start": 4593.0199999999995, "end": 4595.98, "text":
  " for doing RAAG, you know, I happen to think of,", "tokens": [51134, 337, 884,
  497, 5265, 38, 11, 291, 458, 11, 286, 1051, 281, 519, 295, 11, 51282], "temperature":
  0.0, "avg_logprob": -0.24571891959386927, "compression_ratio": 1.782442748091603,
  "no_speech_prob": 0.00192662060726434}, {"id": 1534, "seek": 457762, "start": 4595.98,
  "end": 4599.34, "text": " you know, if the documents are too big,", "tokens": [51282,
  291, 458, 11, 498, 264, 8512, 366, 886, 955, 11, 51450], "temperature": 0.0, "avg_logprob":
  -0.24571891959386927, "compression_ratio": 1.782442748091603, "no_speech_prob":
  0.00192662060726434}, {"id": 1535, "seek": 457762, "start": 4599.34, "end": 4602.58,
  "text": " then there''s too much loss of specificity", "tokens": [51450, 550, 456,
  311, 886, 709, 4470, 295, 2685, 507, 51612], "temperature": 0.0, "avg_logprob":
  -0.24571891959386927, "compression_ratio": 1.782442748091603, "no_speech_prob":
  0.00192662060726434}, {"id": 1536, "seek": 457762, "start": 4602.58, "end": 4605.0199999999995,
  "text": " and too much context being blurred together.", "tokens": [51612, 293,
  886, 709, 4319, 885, 43525, 1214, 13, 51734], "temperature": 0.0, "avg_logprob":
  -0.24571891959386927, "compression_ratio": 1.782442748091603, "no_speech_prob":
  0.00192662060726434}, {"id": 1537, "seek": 457762, "start": 4605.0199999999995,
  "end": 4606.54, "text": " And if the documents are too tiny,", "tokens": [51734,
  400, 498, 264, 8512, 366, 886, 5870, 11, 51810], "temperature": 0.0, "avg_logprob":
  -0.24571891959386927, "compression_ratio": 1.782442748091603, "no_speech_prob":
  0.00192662060726434}, {"id": 1538, "seek": 460654, "start": 4606.54, "end": 4608.5,
  "text": " then you''re losing context,", "tokens": [50364, 550, 291, 434, 7027,
  4319, 11, 50462], "temperature": 0.0, "avg_logprob": -0.2600862979888916, "compression_ratio":
  1.626923076923077, "no_speech_prob": 0.0003269418375566602}, {"id": 1539, "seek":
  460654, "start": 4608.5, "end": 4610.82, "text": " and they''re too specific and
  not enough overlap.", "tokens": [50462, 293, 436, 434, 886, 2685, 293, 406, 1547,
  19959, 13, 50578], "temperature": 0.0, "avg_logprob": -0.2600862979888916, "compression_ratio":
  1.626923076923077, "no_speech_prob": 0.0003269418375566602}, {"id": 1540, "seek":
  460654, "start": 4610.82, "end": 4614.38, "text": " So I think, you know, typical,
  like whatever your domain is,", "tokens": [50578, 407, 286, 519, 11, 291, 458, 11,
  7476, 11, 411, 2035, 428, 9274, 307, 11, 50756], "temperature": 0.0, "avg_logprob":
  -0.2600862979888916, "compression_ratio": 1.626923076923077, "no_speech_prob": 0.0003269418375566602},
  {"id": 1541, "seek": 460654, "start": 4614.38, "end": 4617.78, "text": " you know,
  I mean, if you''ve got giant PDFs that are books,", "tokens": [50756, 291, 458,
  11, 286, 914, 11, 498, 291, 600, 658, 7410, 17752, 82, 300, 366, 3642, 11, 50926],
  "temperature": 0.0, "avg_logprob": -0.2600862979888916, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.0003269418375566602}, {"id": 1542, "seek": 460654, "start":
  4617.78, "end": 4620.86, "text": " maybe break into the chapters or possibly even
  sections", "tokens": [50926, 1310, 1821, 666, 264, 20013, 420, 6264, 754, 10863,
  51080], "temperature": 0.0, "avg_logprob": -0.2600862979888916, "compression_ratio":
  1.626923076923077, "no_speech_prob": 0.0003269418375566602}, {"id": 1543, "seek":
  460654, "start": 4620.86, "end": 4622.5, "text": " of chapters of the large sections,",
  "tokens": [51080, 295, 20013, 295, 264, 2416, 10863, 11, 51162], "temperature":
  0.0, "avg_logprob": -0.2600862979888916, "compression_ratio": 1.626923076923077,
  "no_speech_prob": 0.0003269418375566602}, {"id": 1544, "seek": 460654, "start":
  4623.38, "end": 4625.86, "text": " but yeah, just like use common sense.", "tokens":
  [51206, 457, 1338, 11, 445, 411, 764, 2689, 2020, 13, 51330], "temperature": 0.0,
  "avg_logprob": -0.2600862979888916, "compression_ratio": 1.626923076923077, "no_speech_prob":
  0.0003269418375566602}, {"id": 1545, "seek": 460654, "start": 4625.86, "end": 4629.34,
  "text": " What''s a reasonable size document that represents", "tokens": [51330,
  708, 311, 257, 10585, 2744, 4166, 300, 8855, 51504], "temperature": 0.0, "avg_logprob":
  -0.2600862979888916, "compression_ratio": 1.626923076923077, "no_speech_prob": 0.0003269418375566602},
  {"id": 1546, "seek": 460654, "start": 4629.34, "end": 4632.62, "text": " the meaning
  of something that is, like sort of,", "tokens": [51504, 264, 3620, 295, 746, 300,
  307, 11, 411, 1333, 295, 11, 51668], "temperature": 0.0, "avg_logprob": -0.2600862979888916,
  "compression_ratio": 1.626923076923077, "no_speech_prob": 0.0003269418375566602},
  {"id": 1547, "seek": 463262, "start": 4633.62, "end": 4638.22, "text": " it''s called
  integral, like a whole thing, a whole concept.", "tokens": [50414, 309, 311, 1219,
  11573, 11, 411, 257, 1379, 551, 11, 257, 1379, 3410, 13, 50644], "temperature":
  0.0, "avg_logprob": -0.3731326410325907, "compression_ratio": 1.5525291828793775,
  "no_speech_prob": 0.007267951965332031}, {"id": 1548, "seek": 463262, "start": 4639.0199999999995,
  "end": 4640.0199999999995, "text": " Yeah, yeah.", "tokens": [50684, 865, 11, 1338,
  13, 50734], "temperature": 0.0, "avg_logprob": -0.3731326410325907, "compression_ratio":
  1.5525291828793775, "no_speech_prob": 0.007267951965332031}, {"id": 1549, "seek":
  463262, "start": 4641.62, "end": 4644.54, "text": " It depends on the domain, but
  I would just say,", "tokens": [50814, 467, 5946, 322, 264, 9274, 11, 457, 286, 576,
  445, 584, 11, 50960], "temperature": 0.0, "avg_logprob": -0.3731326410325907, "compression_ratio":
  1.5525291828793775, "no_speech_prob": 0.007267951965332031}, {"id": 1550, "seek":
  463262, "start": 4644.54, "end": 4646.46, "text": " you know, your common sense
  is probably going to take you", "tokens": [50960, 291, 458, 11, 428, 2689, 2020,
  307, 1391, 516, 281, 747, 291, 51056], "temperature": 0.0, "avg_logprob": -0.3731326410325907,
  "compression_ratio": 1.5525291828793775, "no_speech_prob": 0.007267951965332031},
  {"id": 1551, "seek": 463262, "start": 4646.46, "end": 4647.46, "text": " far on
  that one.", "tokens": [51056, 1400, 322, 300, 472, 13, 51106], "temperature": 0.0,
  "avg_logprob": -0.3731326410325907, "compression_ratio": 1.5525291828793775, "no_speech_prob":
  0.007267951965332031}, {"id": 1552, "seek": 463262, "start": 4647.46, "end": 4649.54,
  "text": " Yeah, and like for long documents that are like", "tokens": [51106, 865,
  11, 293, 411, 337, 938, 8512, 300, 366, 411, 51210], "temperature": 0.0, "avg_logprob":
  -0.3731326410325907, "compression_ratio": 1.5525291828793775, "no_speech_prob":
  0.007267951965332031}, {"id": 1553, "seek": 463262, "start": 4649.54, "end": 4652.099999999999,
  "text": " at 1,000 pages for sure you want to do that.", "tokens": [51210, 412,
  502, 11, 1360, 7183, 337, 988, 291, 528, 281, 360, 300, 13, 51338], "temperature":
  0.0, "avg_logprob": -0.3731326410325907, "compression_ratio": 1.5525291828793775,
  "no_speech_prob": 0.007267951965332031}, {"id": 1554, "seek": 463262, "start": 4652.74,
  "end": 4655.34, "text": " And maybe the last question is from Arjun.", "tokens":
  [51370, 400, 1310, 264, 1036, 1168, 307, 490, 1587, 10010, 13, 51500], "temperature":
  0.0, "avg_logprob": -0.3731326410325907, "compression_ratio": 1.5525291828793775,
  "no_speech_prob": 0.007267951965332031}, {"id": 1555, "seek": 463262, "start": 4656.5,
  "end": 4659.0199999999995, "text": " Can this idea of wormhole vectors give us",
  "tokens": [51558, 1664, 341, 1558, 295, 23835, 14094, 18875, 976, 505, 51684], "temperature":
  0.0, "avg_logprob": -0.3731326410325907, "compression_ratio": 1.5525291828793775,
  "no_speech_prob": 0.007267951965332031}, {"id": 1556, "seek": 463262, "start": 4659.0199999999995,
  "end": 4660.82, "text": " more serendipitous results?", "tokens": [51684, 544, 816,
  521, 647, 39831, 3542, 30, 51774], "temperature": 0.0, "avg_logprob": -0.3731326410325907,
  "compression_ratio": 1.5525291828793775, "no_speech_prob": 0.007267951965332031},
  {"id": 1557, "seek": 466082, "start": 4661.66, "end": 4662.94, "text": " Give us
  more what?", "tokens": [50406, 5303, 505, 544, 437, 30, 50470], "temperature": 0.0,
  "avg_logprob": -0.29548610051472984, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.0021705341059714556}, {"id": 1558, "seek": 466082, "start": 4662.94, "end": 4664.94,
  "text": " Serendipitous results.", "tokens": [50470, 4210, 521, 647, 39831, 3542,
  13, 50570], "temperature": 0.0, "avg_logprob": -0.29548610051472984, "compression_ratio":
  1.6553030303030303, "no_speech_prob": 0.0021705341059714556}, {"id": 1559, "seek":
  466082, "start": 4664.94, "end": 4667.299999999999, "text": " Yeah, absolutely.",
  "tokens": [50570, 865, 11, 3122, 13, 50688], "temperature": 0.0, "avg_logprob":
  -0.29548610051472984, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.0021705341059714556}, {"id": 1560, "seek": 466082, "start": 4667.299999999999,
  "end": 4670.94, "text": " So yeah, think of just the behavioral space, right?",
  "tokens": [50688, 407, 1338, 11, 519, 295, 445, 264, 19124, 1901, 11, 558, 30, 50870],
  "temperature": 0.0, "avg_logprob": -0.29548610051472984, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.0021705341059714556}, {"id": 1561, "seek": 466082, "start":
  4670.94, "end": 4673.46, "text": " If I run a query, a keyword query,", "tokens":
  [50870, 759, 286, 1190, 257, 14581, 11, 257, 20428, 14581, 11, 50996], "temperature":
  0.0, "avg_logprob": -0.29548610051472984, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.0021705341059714556}, {"id": 1562, "seek": 466082, "start":
  4673.46, "end": 4677.54, "text": " and then I want to find other things that are
  related to this", "tokens": [50996, 293, 550, 286, 528, 281, 915, 661, 721, 300,
  366, 4077, 281, 341, 51200], "temperature": 0.0, "avg_logprob": -0.29548610051472984,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.0021705341059714556},
  {"id": 1563, "seek": 466082, "start": 4677.54, "end": 4680.74, "text": " that don''t
  match the terms and maybe don''t even match the meaning,", "tokens": [51200, 300,
  500, 380, 2995, 264, 2115, 293, 1310, 500, 380, 754, 2995, 264, 3620, 11, 51360],
  "temperature": 0.0, "avg_logprob": -0.29548610051472984, "compression_ratio": 1.6553030303030303,
  "no_speech_prob": 0.0021705341059714556}, {"id": 1564, "seek": 466082, "start":
  4680.74, "end": 4684.299999999999, "text": " but like user behavior has said that
  these things I should suggest.", "tokens": [51360, 457, 411, 4195, 5223, 575, 848,
  300, 613, 721, 286, 820, 3402, 13, 51538], "temperature": 0.0, "avg_logprob": -0.29548610051472984,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.0021705341059714556},
  {"id": 1565, "seek": 466082, "start": 4684.299999999999, "end": 4686.98, "text":
  " I''m basically infusing recommendations then.", "tokens": [51538, 286, 478, 1936,
  1536, 7981, 10434, 550, 13, 51672], "temperature": 0.0, "avg_logprob": -0.29548610051472984,
  "compression_ratio": 1.6553030303030303, "no_speech_prob": 0.0021705341059714556},
  {"id": 1566, "seek": 466082, "start": 4686.98, "end": 4689.7, "text": " If I help
  over to the cement to the dense space,", "tokens": [51672, 759, 286, 854, 670, 281,
  264, 19729, 281, 264, 18011, 1901, 11, 51808], "temperature": 0.0, "avg_logprob":
  -0.29548610051472984, "compression_ratio": 1.6553030303030303, "no_speech_prob":
  0.0021705341059714556}, {"id": 1567, "seek": 468970, "start": 4690.54, "end": 4694.7,
  "text": " then I take my keywords and I''m finding other things that share meaning,",
  "tokens": [50406, 550, 286, 747, 452, 21009, 293, 286, 478, 5006, 661, 721, 300,
  2073, 3620, 11, 50614], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1568, "seek": 468970, "start": 4694.7, "end": 4697.099999999999, "text":
  " but don''t necessarily have that keyword.", "tokens": [50614, 457, 500, 380, 4725,
  362, 300, 20428, 13, 50734], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1569, "seek": 468970, "start": 4697.099999999999, "end": 4700.66, "text":
  " I''m starting with dense and I hop over to the electrical side.", "tokens": [50734,
  286, 478, 2891, 365, 18011, 293, 286, 3818, 670, 281, 264, 12147, 1252, 13, 50912],
  "temperature": 0.0, "avg_logprob": -0.17417796741832386, "compression_ratio": 1.7755102040816326,
  "no_speech_prob": 0.002898290054872632}, {"id": 1570, "seek": 468970, "start": 4700.66,
  "end": 4704.099999999999, "text": " I''m making sure that I''m finding things with
  that meaning,", "tokens": [50912, 286, 478, 1455, 988, 300, 286, 478, 5006, 721,
  365, 300, 3620, 11, 51084], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1571, "seek": 468970, "start": 4704.099999999999, "end": 4709.74, "text":
  " but I''m adding in keywords that were completely ignored by the dense space.",
  "tokens": [51084, 457, 286, 478, 5127, 294, 21009, 300, 645, 2584, 19735, 538, 264,
  18011, 1901, 13, 51366], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1572, "seek": 468970, "start": 4709.74, "end": 4711.74, "text": " That was
  not necessarily a serendipitous.", "tokens": [51366, 663, 390, 406, 4725, 257, 816,
  521, 647, 39831, 13, 51466], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1573, "seek": 468970, "start": 4711.74, "end": 4716.54, "text": " That''s
  just like fixing problems, but I would say going from lexical to semantic.", "tokens":
  [51466, 663, 311, 445, 411, 19442, 2740, 11, 457, 286, 576, 584, 516, 490, 476,
  87, 804, 281, 47982, 13, 51706], "temperature": 0.0, "avg_logprob": -0.17417796741832386,
  "compression_ratio": 1.7755102040816326, "no_speech_prob": 0.002898290054872632},
  {"id": 1574, "seek": 471654, "start": 4716.54, "end": 4720.74, "text": " More so
  we''ll get you things that were dismissed.", "tokens": [50364, 5048, 370, 321, 603,
  483, 291, 721, 300, 645, 29970, 13, 50574], "temperature": 0.0, "avg_logprob": -0.22747069464789496,
  "compression_ratio": 1.6981818181818182, "no_speech_prob": 0.0048144799657166},
  {"id": 1575, "seek": 471654, "start": 4720.74, "end": 4722.26, "text": " But yeah,
  for actual serendipitous,", "tokens": [50574, 583, 1338, 11, 337, 3539, 816, 521,
  647, 39831, 11, 50650], "temperature": 0.0, "avg_logprob": -0.22747069464789496,
  "compression_ratio": 1.6981818181818182, "no_speech_prob": 0.0048144799657166},
  {"id": 1576, "seek": 471654, "start": 4722.26, "end": 4726.5, "text": " the behavioral
  space is probably going to give you a lot more magic there.", "tokens": [50650,
  264, 19124, 1901, 307, 1391, 516, 281, 976, 291, 257, 688, 544, 5585, 456, 13, 50862],
  "temperature": 0.0, "avg_logprob": -0.22747069464789496, "compression_ratio": 1.6981818181818182,
  "no_speech_prob": 0.0048144799657166}, {"id": 1577, "seek": 471654, "start": 4726.5,
  "end": 4727.42, "text": " All right, awesome.", "tokens": [50862, 1057, 558, 11,
  3476, 13, 50908], "temperature": 0.0, "avg_logprob": -0.22747069464789496, "compression_ratio":
  1.6981818181818182, "no_speech_prob": 0.0048144799657166}, {"id": 1578, "seek":
  471654, "start": 4727.42, "end": 4728.3, "text": " I think it''s a wrap.", "tokens":
  [50908, 286, 519, 309, 311, 257, 7019, 13, 50952], "temperature": 0.0, "avg_logprob":
  -0.22747069464789496, "compression_ratio": 1.6981818181818182, "no_speech_prob":
  0.0048144799657166}, {"id": 1579, "seek": 471654, "start": 4728.3, "end": 4729.86,
  "text": " Thanks so much, everyone.", "tokens": [50952, 2561, 370, 709, 11, 1518,
  13, 51030], "temperature": 0.0, "avg_logprob": -0.22747069464789496, "compression_ratio":
  1.6981818181818182, "no_speech_prob": 0.0048144799657166}, {"id": 1580, "seek":
  471654, "start": 4729.86, "end": 4733.58, "text": " Trey, thank you so much for
  the presentation, for the idea,", "tokens": [51030, 314, 7950, 11, 1309, 291, 370,
  709, 337, 264, 5860, 11, 337, 264, 1558, 11, 51216], "temperature": 0.0, "avg_logprob":
  -0.22747069464789496, "compression_ratio": 1.6981818181818182, "no_speech_prob":
  0.0048144799657166}, {"id": 1581, "seek": 471654, "start": 4733.58, "end": 4737.7,
  "text": " and for pounding at the questions with such an immense speed.", "tokens":
  [51216, 293, 337, 40034, 412, 264, 1651, 365, 1270, 364, 22920, 3073, 13, 51422],
  "temperature": 0.0, "avg_logprob": -0.22747069464789496, "compression_ratio": 1.6981818181818182,
  "no_speech_prob": 0.0048144799657166}, {"id": 1582, "seek": 471654, "start": 4737.7,
  "end": 4740.42, "text": " Thank you all for time.", "tokens": [51422, 1044, 291,
  439, 337, 565, 13, 51558], "temperature": 0.0, "avg_logprob": -0.22747069464789496,
  "compression_ratio": 1.6981818181818182, "no_speech_prob": 0.0048144799657166},
  {"id": 1583, "seek": 471654, "start": 4740.42, "end": 4741.9, "text": " This was
  awesome.", "tokens": [51558, 639, 390, 3476, 13, 51632], "temperature": 0.0, "avg_logprob":
  -0.22747069464789496, "compression_ratio": 1.6981818181818182, "no_speech_prob":
  0.0048144799657166}, {"id": 1584, "seek": 471654, "start": 4741.9, "end": 4742.74,
  "text": " Awesome.", "tokens": [51632, 10391, 13, 51674], "temperature": 0.0, "avg_logprob":
  -0.22747069464789496, "compression_ratio": 1.6981818181818182, "no_speech_prob":
  0.0048144799657166}, {"id": 1585, "seek": 471654, "start": 4742.74, "end": 4745.06,
  "text": " Thanks to me to really appreciate you coming on.", "tokens": [51674, 2561,
  281, 385, 281, 534, 4449, 291, 1348, 322, 13, 51790], "temperature": 0.0, "avg_logprob":
  -0.22747069464789496, "compression_ratio": 1.6981818181818182, "no_speech_prob":
  0.0048144799657166}, {"id": 1586, "seek": 471654, "start": 4745.06, "end": 4745.78,
  "text": " This was awesome.", "tokens": [51790, 639, 390, 3476, 13, 51826], "temperature":
  0.0, "avg_logprob": -0.22747069464789496, "compression_ratio": 1.6981818181818182,
  "no_speech_prob": 0.0048144799657166}, {"id": 1587, "seek": 474578, "start": 4745.78,
  "end": 4748.42, "text": " Thanks to everybody for joining.", "tokens": [50364, 2561,
  281, 2201, 337, 5549, 13, 50496], "temperature": 0.0, "avg_logprob": -0.2834304675721286,
  "compression_ratio": 1.3983739837398375, "no_speech_prob": 0.009870157577097416},
  {"id": 1588, "seek": 474578, "start": 4748.42, "end": 4751.42, "text": " And yeah,
  the video and slides and everything will be coming out to you.", "tokens": [50496,
  400, 1338, 11, 264, 960, 293, 9788, 293, 1203, 486, 312, 1348, 484, 281, 291, 13,
  50646], "temperature": 0.0, "avg_logprob": -0.2834304675721286, "compression_ratio":
  1.3983739837398375, "no_speech_prob": 0.009870157577097416}, {"id": 1589, "seek":
  474578, "start": 4751.42, "end": 4753.0199999999995, "text": " And I hope to see
  you soon.", "tokens": [50646, 400, 286, 1454, 281, 536, 291, 2321, 13, 50726], "temperature":
  0.0, "avg_logprob": -0.2834304675721286, "compression_ratio": 1.3983739837398375,
  "no_speech_prob": 0.009870157577097416}, {"id": 1590, "seek": 474578, "start": 4753.0199999999995,
  "end": 4754.219999999999, "text": " Thank you.", "tokens": [50726, 1044, 291, 13,
  50786], "temperature": 0.0, "avg_logprob": -0.2834304675721286, "compression_ratio":
  1.3983739837398375, "no_speech_prob": 0.009870157577097416}, {"id": 1591, "seek":
  474578, "start": 4754.219999999999, "end": 4755.0599999999995, "text": " See you
  soon.", "tokens": [50786, 3008, 291, 2321, 13, 50828], "temperature": 0.0, "avg_logprob":
  -0.2834304675721286, "compression_ratio": 1.3983739837398375, "no_speech_prob":
  0.009870157577097416}, {"id": 1592, "seek": 474578, "start": 4755.0599999999995,
  "end": 4755.62, "text": " Bye bye.", "tokens": [50828, 4621, 6543, 13, 50856], "temperature":
  0.0, "avg_logprob": -0.2834304675721286, "compression_ratio": 1.3983739837398375,
  "no_speech_prob": 0.009870157577097416}, {"id": 1593, "seek": 474578, "start": 4755.62,
  "end": 4756.62, "text": " Bye.", "tokens": [50856, 4621, 13, 50906], "temperature":
  0.0, "avg_logprob": -0.2834304675721286, "compression_ratio": 1.3983739837398375,
  "no_speech_prob": 0.009870157577097416}]'
---

Alright, hello everyone, wherever you are, really, really happy to see all of you online. Welcome to the Beyond Hybrid Search with Warm Home Vectors. It's another idea that Tray is going to present today and we will have a discussion and all of you are welcome to ask questions as well. Yeah, cool.
I think we'll start with that. This is just a quick intro from me. I'm Dmitri Khan. I, most recently, I'm with Ivan. I joined as a product director leading the search domain. We offer managed open search so that you don't have your headaches setting it up and doing some DevOps.
And you can choose any cloud whatsoever, really. And then just go and run with that. And I'll share a couple of links later. I'm also a host of the vector podcast that I started, I think, four years ago. I already stopped counting. Maybe some of you have heard some of the episodes.
And yeah, it keeps going on and off, but I'm really excited to continue doing that. I've been in search for, I think, 16 years, maybe 20 years if I include academic experience or exposure. I've built search at startups, multinational technology giants.
I think what was the startup, for example, AlfaSense became, I think, a unicorn company by now. Yeah, I'm super excited to partner with three AI power search and support from vector podcasts looking forward to the session today. Over to you, Trey. Awesome. Thanks, Dmitri. Appreciate it.
I'm really excited to have Dmitri Khan more for the conversation part of this. He's been doing, doing the vector podcast and in the space for a long time. So I think it'd be useful to help him facilitate, get lots of questions and good discussions. So I'm Trey Granger.
I'm the lead author on the book AI Powered Search along with Doug Turnbull and Max Irwin. I'm the founder of Search Colonel company that does AI Powered Search consulting, technical advisor, open source connections.
Last year, I've been an adjunct professor at from university teaching computer science. My background, basically my entire career has been in search, particularly the intersection of data science, AI and search.
My last company, prior to search journal, I was the CTO of pre search, which is a decentralized web search engine prior to that. I was the chief algorithms officer at Lucidworks, a search company, as well as prior to that, their SVP of engineering.
I also had a search at career builder, prior to that. I also a decade ago, solar in action, but AI Powered Search is the focus of what I'm doing right now. The books got, you know, quite good reviews from folks. If you haven't checked it out, please check it out.
And this lightning lesson is one of a series leading up to an AI Powered Search course that Doug Turnbull and I are teaching starting two weeks from today. I heard of it.
It's kind of themed based upon the book, but we'll be going into a lot of new and emerging techniques that aren't in the book as well. Just to give you a sense, I'll spend like a minute on this, maybe two.
If you're curious, it's, you know, four solid weeks of material, the first week will sort of, you know, do a course intro, introduce the search relevance problem, talk about ranking those things.
We'll have a guest session from Eric Pugh from open source connections, talking about user behavior insights. For collecting click stream data and how to properly collect and process that are an accession will be on signals and reflected intelligence models.
Everything from signals boosting for popularized relevance to learning to rank for generalized relevance to collaborative filtering and matrix factorization for personalized relevance to knowledge graph learning to learn from user behaviors.
You know, terms, misspelling things like that about your domain. And then every week will have office hours where you can bring your hardest questions or we've got labs throughout the course as well. If you need help with those, we can help.
We the next week will dive into AI powered query modalities, things like buying coders and crossing coders talk about chunking, talk about late interaction models, hybrid search, multimodal search, all of those. Again, all of this has code and notebooks associated with it will be working through.
We have a guest lecture from Jenny from quadrant who will be talking about mixing sparse sentence representations with mini coil and then we'll dive after that into sort of hands on building ranking classifiers or learning to rank models.
And what is entailed in that we will of course then have office hours again the next week will dive deep into rag talk about rag. You know, sort of naive rag, agentech rag adaptive rag guard rails all the sorts of things you need to sort of understand to do to rag well.
We'll talk about agentech search towards the end of the course talk about interleaving strategies for rag will have Max Irwin our co author on a powered search to giving a guest lecture session after that will be.
Automating learning to rank and with click models and with active learning so we'll be diving into how to deal with biases in your data how to deal with exploration versus exploitation looking for results that may maybe don't show up in your normal search patterns and then.
 The sort of final two weeks will have a guest lecture from john handler from open search and AWS really talking about scaling vector search in production with lots of good experience from large scale open search clusters and Amazon servers and then we'll dive into optimizing I search for production everything from quantization re ranking strategies semantic caching.
 Running local models and then for our last session will dive deep into AI powered query understanding and agentech search focused on really interpreting understanding queries leveraging agents as part of that process and so if that's interesting to you there's a link and a QR code here anyone who attends today is eligible for 20% off the course.
 And so definitely check it out if you've been considering it there's two weeks left and of course even if you can't attend all the sessions everyone who's enrolled will have permanent access to all of the recordings all the code and all the course materials so you can use these going forward into the future if that's interesting to you so done with that now I'd like to get to our topic which is beyond hybrid search with wormhole vectors.
 So let me dive straight in and feel free if you have questions as Dimitri said post them in the comments Dimitri feel free to interrupt me at any point if there's something worth diving into otherwise i'm just going to keep going and kind of focus on conversation at the end so I want to start with some basic material on vectors and vector spaces to kind of set our expectations for where we're going with wormhole vectors to start vectors by definition mathematically or something that have direction and we're going to start with the end of the end of the session.
And in this video let's see in situations [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪magnitude [♪manage [♪magnitude [♪f Mash Fans Bake увид then若ymabїr VPN www.pe devils.
comspeaking.habit.com So let's see how much you could get together.
of course GK doctrine is a huge task, a huge task that a man develops on who the heck is dominant during the process and setup it in in vector space and a Hilbert space, but in a semantic vector space, into which we can map a concept.
So whereas, vectors have dimensions, and those dimensions sort of go in any direction. When we talk about an embedding, an embedding is actually a point in vector space. So for example, this point right here, this series of floats for book or tree or what have you.
You can think of it as a vector originating from the origin at 0, 0 here, and extending out to that point. But fundamentally, we think of an embedding as a coordinate, that is a point in vector space that corresponds with some semantic meaning.
And search whenever we're dealing with embeddings, we often have things like word or phrase embeddings, where we take an individual word and leveraging a transformer model typically. We will generate that series of floats that represents the meaning of that word, given the context around it.
But we can also have sentence embeddings, where we look at all of the words in the sentence and their contextual meaning, and generate an embedding that represents the meaning of the sentence.
We can have paragraph embeddings that sort of summarize the core ideas of that paragraph, and the same thing with a document.
Often in search, we'll start with just a document embedding, and when we take a query, we generate an embedding, and we do sort of a vector similarity between defined related documents that match the query. But you can chunk documents up in any way and any number of vectors.
Conceptually, we typically think of embeddings and vectors as having a relatively small number of dimensions. We call these dense vectors, where maybe there's 768 or 1024, some number of dimensions. And we compress lots of data into a continuous space within those.
However, there's also the notion of sparse vectors. And the best way to think of a sparse vector for purposes of our discussion today is to think of lexical search and to think of just, when I'm trying to run a search for keywords.
So imagine you have a 1 million dimensional vector, not 768, but a million dimensions. And every single one of those dimensions corresponds to a term in your index, where you've indexed all of your keywords. And let's just assume that there's only a million terms in your index.
If I wanted to represent latte as a query, well, let me not do latte. Let me do a donut. If I want to represent donut as a query, then I can represent that as a vector with a million zeros minus 1.
And there's a 1 in the column for donut, indicating that this is a million dimensional vector with only one value represented. And that's whether the text donut appears within this document or query. And so that's a sparse vector, where it's sparse because most of the data is not filled.
And I have mostly zeros, but there's some ones. And of course, in this case, if I had the search for cheese pizza, that vector would have two ones in it, one for cheese and one for pizza. So it's a million dimensional vector with two ones in it.
This is just as valid as a vector, as a dense vector, with only 738 dimensions.
But what we typically do, when we start to move from lexical matching, where we can match on those yes or no ones or zeros in an inverted index, what we typically do when we move to doing semantic search is we focus on a much smaller number of dimensions.
And so conceptually, as an embedding here, what I have is eight dimensions. Each of these items that I showed on the previous slide has dimensions indicating whether it's food, whether it's a drink, how much dairy it has, is it bread, is it caffeine, sweet, calories, healthy, et cetera.
 So you can see apple juice now is not represented as, it has the word apple and it has the word juice, but it's represented as very much not food, very much a drink, no dairy, no bread, no caffeine, very high on sweet, but not all the way up, very high on calories, but all the way up and in between, but kind of sort of healthy, but not really.
And then same thing, cheese bread sticks, very much food, not a drink, good bit of dairy, very much bread, no caffeine, you get the idea. These map in the attributes are the dimensions of these concepts over here by representing them in these eight dimensions.
And in search, what we typically do is we represent documents and queries leveraging these vectors, and then we do some sort of vector similarity calculation in order to say how later similar things are.
 So if I were to, for example, take the vector over here for cheese pizza, and I were to then do a cosine similarity between that vector and every other vector, I would see that cheese bread sticks have a very high similarity followed by cinnamon bread sticks, followed by doughnut, all the way down to water.
So these are essentially ranked based upon cheese pizza, these are the cheesiest, breadiest, unhealthiest, non-drinkiest things at the top. This is still very, very non-drinky, not very healthy here, ranked all the way down to it.
It's essentially opposite in this vector space, which is water, which is all the way on the other end of the spectrum. Same thing with green tea, very similar to water, cappuccino latte, healthy, no calories drink, all the way down to a very unhealthy, very not drink. You get the idea.
So that's essentially in a semantic vector space, things span across these dimensions, and they fit at different places along, within the vector space, that corresponds to the meaning of these attributes.
Now, when we deal with transformers, which we get from all the LLMs today that we're leveraging for vector search, these don't use explicit features, like we have here, food, drink, dairy, bread, et cetera. They use latent features.
And latent just means sort of hidden, or another way to put it is, the dimensions don't correspond one to one with particular attributes. It's combinations of those dimensions together that they give us our meaning.
 And so to think of that visually, if I were to create an embedding space, and this is obviously flattened, there could be thousands and thousands of dimensions or hundreds, but in this vector space, if these are all of the embeddings that I have, and I would assert for the phrase Darth Vader, turn that into an embedding and match it, you'll see that over here on the right, I have a cluster of meaning associated with the search for Darth Vader.
Now, there's some other points in various places, but if I were to look at the items in this cluster, I see pictures of Darth Vader, which is what I would expect, because the meaning of Darth Vader is essentially in this area of vector space.
Similarly, if I were to search for Puppy, then this cluster of meaning right here corresponds with puppies and d, I see pictures of puppies.
So the interesting question arises, when I ask what happens, if I were to find the midpoint between Puppy and Darth Vader in this semantic vector space? People have different intuitions about what actually happens here.
Some people think it's, I don't know what I would find in the middle, but the answer is if this vector space is properly constructed, so that the semantic meaning is represented, i.e.
, the further away I get from this point, the more I get away from dog, the further away I get from this, the more I get away from Darth Vader and vice versa, then what I would expect to find, if I sort of average those two, a vector from here and a vector from here together, is a Puppy Darth Vader, a cute Puppy Darth Vader right here in the middle.
 For some people that makes intuitive sense, but if you think about what a semantic vector space is doing, where it's representing meaning across a continuous spectrum, you would expect to find this, because I'm essentially finding what the thing is, that is the average sort of in between Darth Vader and Puppy within the semantic vector space.
Now there's all sorts of reasons why this could not work, depending upon how you've changed your model, and if there's too much data being compressed into little space, but conceptually this works.
 So similarly, if I were to do an embedding search for superhero flying versus superhero's flying, this is very comparable to running a search for superhero flying sort of with the idea of a singular hero and then sort of tracking out the idea of a singular and adding in the idea of a plural, again, from here to heroes, and then what happens over here is, this is essentially the same vector, but moved toward or in the direction of multiple versus singular.
And so what you see over here, in fact, is that while some of the images are the same, I'll, in general, I'm seeing more images of superheroes that are in groups of multiple superheroes.
And so to demonstrate this with a very explicit concrete example, if I were to take this, an embedding for this image, which is a delorean from back to the future, and I were to describe it, right?
This is a sporty car with one door on either side, and it's kind of boxy and it's got really cool lighting.
And so when I run that search for this embedding on other images, I find other sporty cars, obviously some delorians in here, but also just in general sporty cars with a door on either side and really cool lighting for the most part.
However, what if I were to take an embedding for the query from the last slide superhero, and I were to average that or pull it with this image embedding, what would I get? Well, in fact, we have an example of this in the iPad search book when we're doing multi-modal search.
If I take an embedding for superhero and an embedding for this image, what I, in fact, do get is this very first result as a sporty car with cool lighting with a superhero on top, because that's what I would expect in this semantic vector space to be in between these things.
And for these other images, again, sporty cars, single door, but notice that in all of them, there's a person, and it just so happens that that person is the protagonist of their story. So maybe those stories didn't have actual superheroes, but these are the heroes of those stories.
So you get the idea, and I wanted to paint that conceptually just to talk about regions of vector space and what they represent and how you can use math on vectors to move between them and sort of combine concepts and find related things.
And so one problem, now zooming back out to the topic of today, one problem that we commonly come across, and this is where hybrid search comes into play, is that we have disjoint vector spaces in search and that leads to disjoint query paradigms.
What I mean by that is that we have a sparse, lexical semantic space, which is our inverted index. What I showed you earlier with the million dimensions and the keywords represent the dimensions, that is a vector space. It's just a very sparse one.
Similarly, we have dense vector spaces where most of our embeddings are, that we get out of large language models where they're compact into a small number of dimensions, but they're continuous.
Because we have these two different query paradigms, what often happens with vector search is we say, hey, I don't know how to combine this dense query on this embedding with the sparse query with these keywords. So I'm just going to run them as separate searches.
And in fact, that's what most sort of hybrid searches, hybrid search implementations look like out of the box. So this is an example of RRF or the reciprocal rank fusion algorithm where I'm essentially taking a lexical query over here for the Hobbit. And I'm matching on a bunch of documents.
You'll see each of these has the word Hobbit and it's somewhere either in the title or maybe in the description. But notice that while the first four results look pretty good, the next, these are the only results that had the word Hobbit in them.
And then the rest of these results, the good, the bad, and the ugly. This just happens to match on the word the three times. And then this next result happens to match on the Lord of the ring. So it's got the in it three times as well.
It happened to give me a good result, but it was purely coincidence because it doesn't have the word Hobbit here. And then I get the abyss and then the apartment again, only matching on the word the.
So the lexical search found all the results that had the word Hobbit in them, but it completely missed a whole bunch of other potentially relevant results. Likewise, my vector query over here for this embedding matched the Hobbit here. It matched a Harry Potter movie here.
Similar concepts, similar themes, and similar kind of visual style. Lord of the rings, Lord of the rings, Rise of the Guardians, I guess, is maybe kind of conceptually similar even though it's a cartoon. The wailing, I think, just has a visually similar style, but it's a really bad match.
You get the idea. So there's some really good results I get from the vector search, some the dense vector search, some really good results I get from this lexical or sparse vector search.
And then with hybrid search with reciprocal rank fusion, we can essentially take each of those separate sets of results and combine them together in a way that weights things that both the lexical and the dense search found relevant.
It moves those to the top and then kind of gives us better results overall. And you can see that I've matched most of the results over here. So it's better than either of the two lexical or dense vector search mechanisms individually. However, I'm still treating them as entirely separate things.
I'm doing the lexical search, I'm doing an embedding search and then I'm combining them together. But in reality, there's lots of ways to merge these different paradigms. And even beyond just the embeddings I'm getting from texts, we can get text embeddings.
So for example, we can do a text encoder to generate embeddings for that. We can take images and generate embeddings for that. We can also take user behaviors and generate behavioral based embeddings and combine those together. And there's different ways to generate new vector spaces.
You can concatenate these together and you can do dimensionality reduction or you can stack them. I'm not gonna get into those today. But the reality is we've got a lot of tools at our disposal to be able to query and get at data and relate it in different ways.
In fact, what I described for hybrid searches I can go with RRF is just scratching the surface for what we can do with combining different paradigms. And so this spectrum here on the left, this is token matching or traditional electrical search.
And you'll see that things like TF IDF, will be a matching those kinds of things fit over here. We've also, let me just check the, yeah. Okay, we've also got on the opposite of the spectrum this dense vector search.
And of course the RRF would fall in here in this sort of hybrid sparse retrieval in dense vector search where we're running them independently and in parallel and combining the results.
But there's also mechanisms where we could, for example, run sparse retrieval first and then re-rank using dense embeddings or something like with mini coil, which I mentioned Jenny from Quadrant's going to come talk to us about in the AI powered search course.
You can actually run a sparse search and have embeddings that are sort of adding additional semantic data to your electrical queries to be able to better leverage semantics as part of your sparse search.
There's splay, there's semantic knowledge graphs, there's all these different techniques that we can use to get better search, whether it's hybrid search or leveraging one of the techniques.
But I want to just like mention that there's lots of ways to deal with embeddings and to deal with sparse and dense vectors to combine them to improve query understanding and to improve recall.
And so one of the things that I'm experimenting with is sort of like an emerging way to do this is something I'm calling wormhole vectors. And the idea of wormhole vectors is that I've got these sort of different vector spaces. I've got my sparse lexical vector space, which we talked about.
I've got my dense semantic vector space. And then I mentioned we can generate behavioral vector spaces, which I'll show in just a little bit. And so I want to walk through what this technique looks like. And I do want to frame this talk as this is sort of like new and emerging.
I've got lots of experience doing some of this across different vector spaces. But there's a lot of things that I so need to iron out in terms of best practices for doing this. So treat this as something that's emerging and something you can play with.
And I think the intuition will be really helpful. But I'm, you know, if in preparation for the course and going forward, I'm going to be doing a lot more in terms of concrete examples for this. And so I don't want to get into quantum physics or, you know, physics in general.
But, you know, wormholes, if you're not familiar, are essentially passages through space time. You can think of it as, you know, the ability to, you know, go from one point in space to another point in space and essentially like hop there instantly.
I could get into Einstein Rosenberg's and all that kind of stuff, but don't really want to for purposes of today. And what I do want to do though is talk about, oh, give me a second. Well, I'll skip over this.
We'll maybe come to that in the Q&A if Demetri's interested in talking about this notion of entanglement and how that relates to wormholes. It might be interesting later. But I don't, this is about search, not about quantum physics and physics in general.
So this is what it means to generate a wormhole vector bi-practically.
 So if you want to generate a wormhole vector, there's a fundamental base reality of all these vector spaces, meaning if I query with an embedding and a dense vector space, or I query with a lexical query over here, or I query with IDs and user behavior over here, all of those queries ultimately boil down to matching something.
And the something that they match is really critical to how we understand queries and how we understand relevance. And what they boil down to is a document set. So if you run an embedding search over here, you find a point in vector space.
And if it's a dense space, you typically do an approximate nearest neighbor algorithm, or otherwise find the nearest neighbors to whatever point you're querying. And those are your relevant documents. Those documents form a set.
And you can cut off the threshold at any point to say, these are the documents that matched. But that set of documents collectively has some meaning that some relationships within it that represent the meaning of that query. Likewise, if I do a keyword search, I find a document set.
And the collection of those documents represents the meaning of that query, at least as we've been able to represent it in that vector space, same thing over here.
So the idea of a wormhole vector is if I want to query in one vector space and find a corresponding region in another vector space that shares the same meaning semantically, then what I'll do is I'll query in the current vector space, for example, within embedding here.
Actually, let me start it here. I'll query in the sparse-like-school vector space. I will then find a relevant document set. This is what search does. It finds a document set. And then I will derive a wormhole vector to a corresponding region of another vector space.
 So for example, once I found a document set over here, I will use that document set to generate, what I'm calling a wormhole vector, but to generate a vector that will allow me to query in the other vector space or hop or traverse to the other vector space instantly, to a region that shares a similar semantic meaning to the region in the Lexical space.
Then once I've found that vector for the other vector space, I will run that query in the other vector space to traverse to that vector space, and then I'll repeat as needed.
So I can actually hop back and forth between vector spaces to find and collect documents, to try to better understand them, and then to use that understanding to take those documents and return them for the full set of search results. So I'm gonna actually just show this visually for a second.
Let me put them up. Let me click here and restart this demo. So imagine I have a sparse vector space over here on the left. The way this works is I send a query in.
This query finds a set of relevant documents that are in this vector space, and what's found those documents, it uses them to essentially a wormhole in the pauses for a second. Oh, maybe I can't.
Essentially, once I've run that query, I find the relevant documents, which are the things close by in vector space. I then use that to generate a vector and embedding that I'm gonna run a search for over here in the dense space.
And once I run that search, you'll notice that in this example, it's not exactly where these documents are, but it's very nearby, meaning the sort of collection of these things together and what's understood semantically about the relationship, maps to this point and vector space on the right.
And then that allows me to then find other things surrounding it that represent a similar meaning. And this is just looking at two vector spaces, a sparse vector space and a dense vector space for keywords and then for embeddings.
But as I mentioned, there's also this notion of a behavioral vector space. So the same thing happens here. I can run a query, find relevant documents, use those as my wormhole.
And then I generate this wormhole vector to hop through the wormhole to the other side to find the region corresponding to that meaning in either of these other vector spaces.
So in this case, if I've done major expectation, which is like the process you go through when you're doing collaborative filtering for recommendations, then I would hop to the corresponding region over here. So that's the general idea, just kind of visually describing it. And hop like over here.
I can just one second. I can be one second. Come on, slides up. All right. And then the next question is, how do we actually create these wormhole vectors? So to meet you, if there's any questions, feel free to interrupt me at any point. But I'll keep going otherwise.
I think we have a couple of questions, but we'll defer at the end. Sounds good. All right. So the question now is, how do we create a wormhole vector? And there's essentially two types that I'm going to focus on right now. One is the, sorry, I lost this. OK.
The first is if I'm trying to go to a dense vector space within bedding. So this is very easy. All I have to do is pull the vectors or average the vectors of the top end documents. So imagine I run a keyword search. I find a set of documents. I rank those.
And then I don't necessarily need to take the entire document set. I could.
But if I wanted to just take the top end documents to get a more sort of semantically relevant, or just let's just say relevant set corresponding to that keyword query, then I generate a new embedding in the dense space that is just an average of those.
If you go back to the Darth Vader example from earlier, where the puppy Darth Vader is in the middle, it was sort of a combination of the meaning of Darth Vader and a meaning of puppy. Think of this as taking a bunch of documents that each have their own meaning.
And when I pull them together, I'm creating an embedding that has the average of the meaning. And if I assume my documents that I queried on the lexical side, have some sense of a shared meaning within them.
And I take the top documents from that, then that shared meaning I can hop over to the dense space, find and then find other things that have similar meaning, even if they don't match the keywords. Likewise, I can go the other direction if I'm in my embedding space, my dense space.
I can run a search, find the top in most related embeddings by cosine similar to what have you. And then conceptually, it seems more difficult to then hop over to the sparse space.
How do you generate a sparse vector? But there's a technique called semi-technology graphs, which I'll kind of walk you through, which allows you to do this. So zooming back out, I mentioned pulling the vectors of the K-NN documents.
All you need to do, again, I query an electrical space, get the top K documents, get the embeddings of those documents and average them together. This is the simple way to do that, just using NumPy.
For the semantics knowledge graph approach, same thing I get the top K documents in the current vector space. And then I do a semantics knowledge graph traversal to derive a sparse lexical query that best represents those documents.
So functionally, if you think of language, I just talk about semantics knowledge graphs for a second and show you the structure of natural language. You could think of it as a graph of relationships.
We've got prefixes and suffixes and those mapped to terms, those mapped to term sequences and documents. But once you get documents and we've got these terms across documents, you can just think of this as a giant graph of relationships. And so I can take individual words.
In this case, Trey, he, he, they all refer to the same entity. I can take other things. And if I think of this as a graph, then in fact, you can leverage your inverted index as a graph and you can traverse it to find these relationships. And so, and a typical search engine.
So like any of the Lucy and engines, for example, you have an inverted index, which is something that maps terms to sets of documents. And then you've got usually a forward index and open search, elastic search, solar, any Lucy and engine. This is going to be your doc values.
But essentially, I can take any term and map it to a set of documents. So if I can take any term, I'm sorry, any document map it to a set of terms.
So if I can take any term and map it to a document set, and I can take any document and map it to a set of terms, then that's a graph and I can traverse back and forth across this.
So for example, if I have the skill of Java and the skill field, and I've got a set of documents that has the keyword Java, you can think of this set of documents as representing the keyword Java. And then similarly, there's sort of a link to other documents.
You'll notice that there's no documents that link both the skill of Java and the skill of hibernate. And so in a set theory view, it looks like this. Notice that this set doesn't intersect with these.
And from a graph theory view, the same underlying indexes look like this where I have a graph where I've got the skill of Java with a has related skill edge to the skill of Scala and the skill of hibernate. And then oncology is completely disconnected from the graph.
And all I'm doing is leveraging my inverted index, my sparse representation to traverse across these relationships. This is very useful for things like disambiguation, where I can take a keyword like server.
I can traverse through documents to find what are the top semantically related categories, for example, DevOps and Travel. And then within each of those categories, I can traverse to other keywords and find which are the most semantically related keywords to server and the DevOps category.
For example, I get terms like Docker, Ingenx, Jenkins, Git, Words and Travel, I get things like tip, restaurant, bill, wages, things like that. And so all of this just leverages an inverted index. There's no embeddings whatsoever. This is all just leveraging the sparse semantic space.
But why this matters for modeling a tent is if I have a query like barbecue near haystack over here, I can generate a sparse vector representing the meaning of barbecue by looking at the index and seeing what's related to it.
So in this context, what I'm able to find is that barbecue is related to things like ribs and brisket and pork and the category of restaurant. IE, I can generate a sparse lexical vector like this, purely from the things that are semantically nearby in my sparse vector space to barbecue.
But also, if you look at the query over on the right, barbecue grill, what I'm able to do is generate a sparse vector that is barbecue or grill or propane or charcoal. Notice that this vector is now different because it's contextualized based upon grill being in this query.
So now my query becomes a category about to our appliance and then this is the list of words that better represents the meaning of barbecue. Again, no embeddings, no transformer models, no LLMs involved here. This is purely leveraging my sparse lexical space in the semantics within it.
And so this is some example source code from the AI Power Search book for traversing semantic knowledge graphs. But the idea here with the wormhole vectors is that I can take a query in any vector space.
So for example, if I take a lexical query here, I can easily take a lasagna or drive through it, what have you.
And I can generate these representations over here by taking a lasagna, finding a dockset that matches that keyword, and then from that dockset, finding these other relationships, for example, lasagna can be described as Italian with keywords like lasagna, Alfredo pasta and Italian.
And then Korean barbecue can be represented as category of Korean with terms like Korean, Bonchon, Saruwan, et cetera, fast food, gets things like McDonald's in window. So this is purely leveraging, and I've been doing this for years, and it works very, very well.
But this is purely leveraging the inverted index in this document set. But the idea with the wormhole vectors is not just to stay within a single vector space, but to be able to go across vector spaces.
So similarly, I should be able to take an embedding that finds a region in semantic vector space and a dense space, find the nearby things, which ultimately just translate to a dockset.
And then from that dockset, I can use the same technique to say what are the things that are related within these documents and generate the similar kinds of outputs over here?
You can also think of this, if taking away all the wormhole vector terminology, you can think of this as just a way to make your embeddings more explainable.
I've got an embedding, I go to a dense vector space, I find documents, and then from that set of documents, I'm now deriving a lexical vector, which is readable that's describing what's happening there.
And of course, I can then turn around and take that and query in my sparse space to match other things that have the terms, but maybe didn't match in the dense space. So that's the general idea.
There's one last thing I wanted to cover briefly, which is this notion of behavioral embedding spaces, because I've mentioned it multiple times. And I have a feeling a lot of people aren't super familiar. And so let me click here.
The general idea, and I'll be very quick through this, we'll spend more time in the AI Power Search course diving into all of this, but the very high level intuition is that when users interact with your documents, right?
They run queries, they click on things, they like them, add to cart purchase, those are user behavioral signals.
And if you've got a sufficient amount of traffic, you want to be collecting those and leveraging them to build reflected intelligence algorithms.
 So one of the types I mentioned several earlier signals boosting, collaborative filtering, and matrix factorization, learning to rank, and knowledge graph learning, but specifically on collaborative filtering, which is mostly focused on personalized search, or understanding user behavior to generate better personalized results.
We typically leverage collaborative filtering, which is now algorithm for doing recommendations. So I start with a particular item, or particular user, and I recommend other items based upon that item or user.
So this is what that typically looks like, right? Somebody runs searches or purchases things like Apple and MacBook, and then these are the items they interact with, iPads and MacBook Airs, things like that.
And then for that user, we can generate this list of recommendations based upon running this collaborative filtering algorithm. In this case, I want to briefly mention again, that with typical content based embeddings, I mentioned latent features earlier.
Typically you have items, and there's these densely packed dimensions that represents different features.
Collectively, this particular feature might have a strong correlation with size, this one I have a strong correlation with color, this one I have a strong correlation with, is this kind of like a computer. But those meanings spread across many different of these dimensions.
Similarly, whenever we're doing collaborative filtering, these also rely on latent features or latent dimensions.
So for example, if I have a bunch of users, my first user likes these three movies, my next user likes these three movies, my third user likes these three, my next user likes these three, and my last user likes these three.
You can kind of visually see here, these are some similarity here, there's some similarity here, your brain's probably picking out what it is.
But if I were to map these conceptually, I would say that users one, two, and three tended to like movies that were about superheroes made by Marvel Studios and occasionally Warner Brothers, they're all action movies, and they're not suitable for small children.
Whereas users four and five, all liked animated movies, all of them were suitable for small children, and all of them were made by Disney and Pixar.
A collaborative filtering algorithm sort of discovers these relationships and recommends based upon them because they exist in the underlying documents, even though we don't have them modeled out explicitly. And the way this works with collaborative filtering is we do matrix factorization.
So we start with a user item matrix, where here's my list of users, and here's my items, and then these are sort of the amount to which they like those items. We can derive this based upon just their querian click patterns.
The intermediate step for collaborative filtering is matrix factorization, which is taking this underlying user item interaction matrix and trying to break it into two different matrices. This user feature matrix and this item feature matrix.
And the idea is that if I can generate a set of latent values associated with this user across some number of dimensions, I'm only showing three here visually, because it's a PowerPoint slide, but there'll be more.
 And if I have the same latent dimensions over here for the items, when I multiply a particular user and their particular values associated with these latent dimensions with the movie, then I'm pulling apart how much of this belongs to the movie and how much of this belongs to the user in terms of an interest.
But at the end of the day, these are embeddings. This is a user embedding and this is an item embedding. What that means is that, and this is just how it works to do collaborative filtering and actually generate recommendations for particular items, not particularly useful for today.
But what I can do is I can generate these latent embeddings and these essentially allow me to create a behavioral embedding space for my items.
So once I've done that, I can add these behavioral embeddings onto documents just like I do with content-based embeddings or whether it's images or text or what have you, and then leverage those as a behavioral space.
So we do this commonly with personalized search, for example, we'll go through this in the course.
But if I have a person who previously searched for Hello Kitty Plus toy, GE Electric Razor, GE Bright White Lightbulbs, Samsung Stainless Steel refrigerator, I can take a normal query, keyword query for microwave, which just returns random microwaves.
If I use these vectors improperly with no guardrails, I might do things like blur the lines between categories. Most people, if they've searched for a Samsung Stainless Steel refrigerator, the best result here would be a Samsung Stainless Steel microwave.
But if you do this wrong, the sort of naive approach is, I might end up with a Hello Kitty microwave or a Panasonic microwave, or not Panasonic, but I might end up with things that don't exactly match all of the preferences of the category, again, for another day.
But this is how a behavioral vector space would typically be used.
But ultimately, there's a lot of tips and tricks you can use to do AI-powered search to combine all of these different techniques that you might use to run searches and to query understanding of relevance and sort of integrate wormhole vectors in various places.
So there's lots of different query paradigms to experiment with, to merge using wormhole vectors. But that's the general idea.
 I wanted to kind of introduce today to get the discussion going about going from thinking of these vector spaces as entirely sort of orthogonal, where I have to query them separately, or maybe I could even query them in the same query, but I'm filtering on them separately, to trying to actually pull out the semantic understanding from one vector space and use that to craft a sort of wormhole or hopping off point to another vector space to sort of continue to explore leveraging a different query paradigm.
So that's pretty much it for the talk for today. Dima, Dmitry, I don't know if you want to start to dive in some questions.
I know some people will have to hop off at the top of the hour because this is scheduled for an hour, but I'm also happy to just kind of keep going with questions a little bit after if it makes sense and people can drop off when they want. But let's maybe dive into some discussion.
Yeah, we have a bunch of questions. Thanks, Tray, a bunch. This is fantastic topic. I just recently traveled to Texas from Finland and it took me like 12 hours. I wish there was a wormhole jump through points so I could just end up there much quicker. There'd be all of them.
We have so many questions, man. So I'll defer my questions off and I'll just jump. There is one logistic question from Ardune. I hope I pronounced you name correctly, I'm sorry.
How's the course different from the AI Powered Search book? And then later is this topic wormhole vectors covered in the book? Awesome. OK, so I would say there's materialized. There's probably like about a 40% overlap. The book is a good solid foundation for how to think about AI Powered Search.
Obviously we go through all the mental models and lots of code examples. So a lot of the labs and a lot of the code for the course will come from the book. However, there's a lot of new topics and things that we just like, we couldn't write a thousand page book.
And so there's a lot of things we just couldn't get to because we had to start from the beginning and frame it.
So things like late interaction models, things like a gentick search that aren't in the book, like late interaction models are referenced, but we just couldn't get into depth that are more modern and interesting ways to solve problems.
Things like mini coil, which I mentioned, those things will be in the course and unique to the course and will have guest speakers who are experts in those things. So I would say the course doesn't expect you to have read the book or to understand the fundamentals in the book.
We'll cover those, but we won't cover everything in the book. And we'll also cover a lot of things that aren't in the book and go in deeper depth. And so I would say, if you've read the book, the course is still going to be really valuable.
And even if you can't make all the sessions, again, the videos and all the materials available for you forever. So you don't have to have read the book to take the course, but if you have read the book, the course is still going to be massively useful. Yeah, so to implement each other.
And by the way, I own the book and it's amazing read in silency. And then the course is a different way of engaging with the material like a dynamic way.
Well, I didn't answer the last part, which is, will wormhole vectors be covered? They will definitely be covered more so as the techniques and strategies for how to hop back and forth between. So some of it's actually in the book, the semantic knowledge graph stuff is already in the book.
But the, yeah, we'll definitely talk about wormhole vectors explicitly and have some more specific examples people can play with. Yeah, awesome. And I do want to mention this is like experimental and emerging.
And there's some things that I glossed over today in terms of hopping to a particular point versus trying to hop to a region and have more of a shape that we could chat about as well. But yeah, there's still some things I'm doing to kind of better understand it fine to know. Yeah, awesome.
I'm trying to speed up. But there's a question from Claudiu. What are the latent features? And basically where you switched from sort of explicit feature metrics to like latent features. Maybe I can take it quickly. It's basically in an LLAM.
So if you deal with an encoder model, where you generate embeddings, basically these are like internal representations that the model learns. And they're like compressed. They're like abstract way of dealing with patterns or relationships and your data.
It's not exactly directly that black and white, but the thing is that on the conceptual level, these are like internal weights that the model learns. Then there is a question from Julian, very concrete one.
Can you give an great example of how to compute the wormhole vector from sparse to dense space? Yeah, so I had a slide. It's sparse to dense is the easy one, which is, let me, let me go back to the slide. One second almost there. Here we go. So to go from sparse to dense, think of it this way.
You've got a bunch of documents in your index, and you generate embeddings for those documents.
That's how your dense space is constructed, right? Those embeddings on the documents, if you query for the documents using keywords in your sparse space, then you're still matching that set of documents, and all of those documents have the embeddings on them.
So all you do is run a keyword search on your documents, take the top end documents are the most relevant, right? They hopefully semantically represent the concept the best. And then you take those embeddings off of them, and you literally abverse them together.
The code for that is on the screen right here, and that you just generate this pooled embedding.
It's that notion of Darth Vader versus Puppy, and finding the Puppy Darth Vader in the middle, right? If someone were to run a keyword search, and it's sort of, it's easy to think of this with a single keyword, but let's go back to my, let's go back to cheese pizza, right?
Like if I search for pizza, I'm gonna match a bunch of pizzas.
If I search for, maybe cheese pizza is back as all pizza has cheese, let's do cinnamon bread sticks, right? If I search for bread, I'm gonna find bread. Documents have the word bread. If I search for cinnamon, I find documents with cinnamon. If I search for sticks, I find documents with sticks.
Sticks by itself isn't really what I'm looking for, but if I do cinnamon bread sticks, then I'm finding all of the documents that have those terms together, which likely are cinnamon bread sticks, or have the notion of cinnamon bread sticks, or talking about cinnamon bread sticks.
 So if I take all of those documents, the most relevant ones, and I generate, and I average their embeddings together, and go over to the dense space, where I land should be where the concept of cinnamon bread sticks is, and things nearby, which may not have the word cinnamon bread or sticks in them, should come back.
I might get certain kinds of doughnuts, and certain kind, I might get like a churro or something like that. So that's how it works. But this is the math here. That's actually the easiest way to go from sparse to dense. The dense to sparse requires a semantic knowledge graph or similar. Awesome.
I hope this answers your question, Julen. I would not feel free to unmute and ask full of questions. Otherwise, I'll jump to the next one from Ursula.
Do we build the inverted index and the forward index to build the knowledge graph using just some document chunks? Or do we need a much bigger document base to make it work? It's a good question. Mm-hmm.
So the best way for semantic knowledge graph to work the best, you need to have overlaps of terms that across documents.
Meaning, if I take something like stack exchange, where there's a bunch of topics being talked about, you'll have lots of people who use the same words together and the same documents.
When that happens, you can easily find sets of terms that overlap commonly and use the semantic knowledge graph to generate semantic understanding and relationships based upon those co-occurrences. All the math for that's in the AI powered search book, but that's when it works the best.
Something like Wikipedia is actually even though it's commonly used for every data science project.
It's actually really bad for semantic knowledge graphs because every Wikipedia document tends to be about a particular topic and other than common terminology, you tend to not have a lot of overlap across documents because they're all focused on one idea.
So for semantic knowledge graph to work well, you typically are going to want to have overlap across your documents. What that means is that if you chunk your document so small that you only have a couple of words or sentences or something like that, you lose a lot of that context.
I mean, in general, when you chunk, you lose context. That's the problem with chunking, with most forms of chunking.
And so you have to be careful not to chunk too much, but the end verse is also true if you only have 100 documents and every single one of them is 1,000 pages long, well, there's way too much overlap and everything is related at that point.
So I would say it's no different than just how you would typically segment your documents for any search problem. You need to be granular enough to be useful, but not broad enough to be too general. Yeah, awesome. And now the logistical question from Arun, whether we will share slides.
Yes, absolutely. Yeah, the video for this, everybody who signed up will get in probably like 48 hours, you'll get emailed a copy of the video, so you can refer back to it. And I'll also send an email with the slides probably shortly thereafter.
Yeah, and I plan to publish this in the vector podcast as well. Yes, absolutely. I'll follow up later. The next question is really cool from Cloud. You're creating a wormhole vector that will move us from embedding space to sparse vector.
I understand the methodology, but the way back now, how do we aggregate a set of sparse vectors that represent documents in a way that will allow us to move us to the embedding space? In other words, from the sparse, like you showed the tray, we have millions of dimensions, right?
How do we compact that, right? And don't lose anything and don't introduce any noise when we're not way to the dense space? Yeah, so it's a really great question.
I answered it technically in terms of pulling, but let me add some color to it in terms of techniques. So the... There's a couple of things here.
One, whenever you're querying in an inverted index, there's typically a kind of Boolean matching phase, and then there's a ranking phase, meaning if you had 10 million documents in your index, you're not gonna return a ranked list of 10 million documents.
You're gonna probably return the documents that have the specific keywords you search for, which is gonna be a much smaller document set. And so that's... And you can do the same thing on the dense side with cutoffs on cosine similarity or something like that.
But, the step one is you start with a condensed document set that should represent generally the meaning of what you searched for using the keywords you searched from the lexical side.
However, because the idea of a wormhole vector is to find the best corresponding region in the other semantic space, it can often be useful to not take that entire document set, either matching the query, but if you feel confident about your ranking, then you can take the top end document.
So maybe you match 10,000, and maybe you only take the top hundred and say, hey, from the top hundred, if you know your relevance ranking is good, then you're gonna use that to generate a more precise wormhole vector to the meaning of those top documents over to the dense space.
So, whether you go with the full matching document set, or you go with the top end, that's really a just practical matter of how confident you are on the ranking. If you're really confident in your relevance, you should go with the more relevant documents.
And if you're not, just take the whole document set and it should sort of average out the meaning. One other thing that we didn't really get into is that the strategy, the technique I was showing if I, let me jump back to the final slide one second. If I jump back to... Here.
So the technique that I'm showing, where I get my document set, pull my embeddings together, that ultimately gives me a single embedding, which is a single point over here in my dense vector space. The reality is that different queries have different specificity.
So imagine this is like a job search engine. If I run a search for senior AI search engineer, a late interaction, culverts, signals boosting and collaborative filter. If I run that search, that's a very specific search.
Frankly, it probably doesn't match anybody, but if I ran that search, it would be a very small number of documents. It's very specific. However, and so in that case, having a point kind of makes sense. However, if I ran a search for sales, that's like a third of all jobs.
 And for me to take the notion of sales, which is probably a giant region in this vector space with lots of nuance inside of it, and to then turn that into just a point in the other vector space, it's probably not gonna work out super well because there's probably, sales is probably distributed across that other vector space in a much larger region.
And so there's this notion of query specificity which is also really useful. So I would actually argue that the better way to do this technique is as part of your initial query when you're sort of finding the set of documents.
 If you can look, for example, at the embeddings and do just like a co-sign similarity across the embeddings that you're pulling, you can go from a bunch of embeddings that are just pulled together into a point to actually saying, what is the relative size of the range of the co-signs within these embeddings?
And if it's a very large range, I understand that this is not a very specific query, it's a broad query.
Therefore, when I go query in the dense space, I need to draw a larger radius or a larger kind of shape around what I'm searching for.
So ideally, you're actually searching for a shape at not just a point, but literally every vector search implementation I've seen at any company is searching on embeddings as points and just looking for the nearest things, not searching on shapes.
And so we don't even really have the query patterns and paradigms in place today to do that kind of a query. But I think that would be a further improvement on the paradigm here. Awesome. Yeah, Tim Allison says thank you. Thanks, Tim. The next question is from Julian.
Can you recommend any papers or other material to explore the topic further? So not really. So the one whole vector thing is something I kind of came up with. I will say, well, two things. One, semantic knowledge graphs.
I actually was the lead author on the original semantic knowledge graph paper back in like, I don't know, 2016 or whatever was published. So this notion of being able to jump between spaces back to a sparse space, you could look at that paper if you want an actual research paper.
I've also given lots of talks about it. It's in the AI powered search book. It'll be in the course. However, the notion of taking, running a query and pulling vectors together and even the notion of query specificity that co-science similarity thing.
If you look at Daniel Tukolang, he actually did a lightning talk with us a week or two ago on query understanding. He actually talks about this notion of a bag of documents to represent a query. It's functionally the exact same thing.
 So if I run a query and think of the query's meaning as being represented by the set of documents that match that query, then to take that set of documents that holds that meaning and pull the embeddings to create an average embedding that represents that meaning and embedding space, it's functionally the same thing that Daniel describes when he talks about bags of documents.
So I would say look at Daniel's work, look at the lightning talk he gave a week or two ago with us. And those are some good resources. And of course, the book and the course. Yeah, awesome. Maybe at some point of paper as well, right? Yeah, it's definitely possible. I need lots of good.
I need evals on how this actually does in practice. Yeah, absolutely. Are you not the same question? I'll skip that. Mustafa is asking for a knife phone query cases. So charges may also appear. Would be correct to take the average. Would it be correct to take the average of them? So good question.
So yeah, if you, so, Lexical queries work really well. When you've got particular terms you're looking for, whether it's an ID or whether it's a keyword, they don't work as well with like semantic meaning.
Whereas in a dent space, obviously you query on meaning, but if you try to search for a product ID in a dent space, unless you've fine-tuned it for that, it's gonna do an awful job.
 And so, in the case of like searching for iPhone and getting iPhone cases, this somewhat gets back to what I said earlier about, ideally, if you take the top end documents that are the most relevant and you limit to that, like if you're ranking algorithm can already sort of understand that when someone searches for iPhone that they mean an actual iPhone versus a case, that's a better way to go versus just anything that matches the term.
That being said, what you can do is you can, for example, in that case, search for iPhone, find the iPhone cases, along with iPhone, get that average vector, and then there's still this region of, along certain dimensions, it's associated with iPhone.
 If you hopped over to the behavioral embedding space, what you're gonna find is that, hey, these cases are very highly correlated to these items, the iPhones that actually correspond to those cases, so that might be a case where you would want to hop to the behavioral space and leverage what's there.
There's also just a note, we've talked about taking entire queries and hopping from between spaces, but there's also a line of thinking and practice here around using this for query understanding, not just ranking, and so you could, for example, split the query into individual keywords.
iPhone, like just the word iPhone, and you could also search on the dense space, and you could try to take the individual pieces and find things related to them, and then leverage that for query understanding to hop back and forth between spaces.
So the answer is you still have the fundamental limitations of each space, but imagine if somebody searched for, I want a phone that's really good at blah, blah, blah, that's made by Apple with product ID X, right?
 You can imagine trying to search for that, like an oratory on the, on the lexical side, and you'll actually match that ID and probably have it come up at the very top, and then you can imagine searching for that embedding on the dense space, and you can imagine for each of those hopping back and forth and trying to see what documents are there a couple of times.
So there's, look, sure to answer, there's a lot of different ways that you could leverage this technique to be hopping back and forth.
 I'm not gonna claim now that I've thought through every single one of them, and there's lots of ways to do it, but I think as an introduction to the topic, and as a tool that you can add to your tool belt, to be able to get explainability and another vector space, based upon what you found in the first vector space, I think this is a really cool technique, and I just wanted to kind of present it and get feedback and enjoy this discussion.
Yeah, thanks, Trey. We're quite over time, thanks everyone for staying on, and hopefully if you can still stay on, we can get to the bottom of the list.
Yeah, and by the way, to your answer, Trey, I think somewhere there is probably a notion of search result diversity as well, right? So even if the user types iPhone, they only mean the phone, but they actually may mean something else, right?
So showing diverse results, and then traversing to the other side with those diverse results could also make sense.
Absolutely. Then Arjun is asking, is there, if I summarize the question, is there a cheaper way than using semantic knowledge graph? Maybe the fear is that the graph approach is computation-expensive, is there some cheap way to...
It's less computationally expensive than running an embedding model typically. But it just depends. Yeah, I mean, there's other techniques. Like if you have a fine-tuned, blade model, for example, it can give you very comparable kind of semantic understanding on the sparse side.
The problem with that is you have to fine-tune it to your data, and also one of the benefits of the semantic knowledge graph is that if you, I'm just gonna quickly jump to the slide and show you this one. Let me do the one that's got keywords, here we go. Share here.
With the semantic knowledge graph approach, you have the ability to not just represent the query with a bunch of terms with values, but you can actually use any field.
So it's really useful to be able to describe it with a category of Korean and a bunch of terms here, and maybe you've got other fields on your documents that are really useful for describing the document, a taxonomy of some sort.
The semantic knowledge graph gives you a lot richer ability to turn the set of documents into a fully expressive query. So yeah, there's other techniques. You could look at displayed things like that, but nothing that's nearly as expressive.
Yeah, and these are the concepts you're gonna covering the course, right? Yeah, we'll cover it all in the course. For those who are interested to learn more.
Sorry, not trying to make this talk just a big promo for the course, but this is a really, wormhole vectors by themselves are a really interesting topic, but yeah, obviously I would love if you would join us in the course, it'll be fun.
Debo Brata is asking, what do you think about some of the reputable search sites, like in Deden, LinkedIn, where searching for a male engineer will bring your results like data engineers and whatever unrelated stuff, not directly related stuff.
And so the question is why search documents not based on the entire user query, right? Only part of it. Sorry, I'm trying to understand the question in relation to the wormhole vector topic. Yeah, I think it's more, I think it's less directly related.
I think it's more airing on the side of why data bias. Why does reputable search sites do not sort of utilize the semantic search, you know, one to one in a way? Yeah, I got you.
I mean, the reality is that most AI-powered search algorithms, really all of them are used data and the data is biased, right? So like the reality is in the world, if you look at data engineering jobs, they are more statistically skewed towards males being in those jobs and females.
That doesn't mean anything in terms of who can do the job or who can't. It's just a reality that, you know, there tend to be more males in engineering and therefore the data is reflecting that.
It would be nice to be able to take those biases out and in fact, there's ways you can do that, but they're extra work. And so the out of the box algorithms that are typically employed don't necessarily try to tackle those biases.
 So yeah, I think it's, I think it's valiant to, you know, try to, especially when you're dealing with things like people's livelihoods and, you know, careers and things like that, I think it's, it's a great exercise and something they should focus on, but it's like, unfortunately, kind of a reality of the underlying data that's being bubbled up, I think.
Yeah. My take is that I- The data is biased. Yeah, I agree.
 I've been one job search engine like a couple companies ago and my take is that probably these companies are trying to avoid, you know, these traps when your super, super precise query will either lead to nothing or lead to just a couple of jobs on the screen because their business is to show you as many jobs as possible so that they can monetize that.
So it's all about maybe like business element as well. But I'm sure there are other technical aspects of this, which we should note disregard. Sure. The next question is from Arjun. And you experience how much do the following results differ? First, query against dense vector space directly.
And the second query in sparse vector space and wormhole to dense vector space and finally get the docs that are similar to the wormhole vector average vector. So what's the question? That's the answer.
 I mean, at the end of the day, the, if you have a query that you run against your lexical space that matches mostly documents that are related to the query and then you hop over to the dense space, you're typically gonna get a lot of overlap because the lexical space semantics are going to be very similar to the dense vector space semantics in terms of like the underlying meaning.
If you were to take the lexical space and I should mention, you can actually use the wormhole vector in the same vector space. I kind of showed that with like taking a query like lasagna and then rewriting it with a more expanded out lexical query with a category of Italian.
And so you don't have to actually jump between different vector spaces. You can even jump within the same vector space.
And I think that in this context, the more similar, the meaning of the underlying set of documents is matching each query, the more interesting you're gonna be able to find missing links in the other vector space.
If you have very orthogonal queries, like you can imagine on the lexical side searching for orange juice and Nintendo switch, right? Or you'll get nothing for that, but orange juice or Nintendo switch.
Well, you basically end up with a document set that is really two separate document sets, right?
 It's like there's not a lot of overlap and if you hop over to the dense space and get the average of those, there's still gonna be things that are like probably close to Nintendo switch and probably close to orange, but the more different those things are, you might get some weird stuff in between.
Because you're now looking across two different places, any Nintendo switch stuff that's orange or related to juice or something might show up, but it's gonna be weird. And so this isn't like a magical silver bullet that solves every query understanding or every relevance problem.
It's just another tool in our toolkit to be able to better reason about the underlying documents and queries and to explain queries in another modality, if you will, another query modality. Yeah, in other words, what your searching for should still kind of make sense. Yeah, yeah.
So if it does, it probably will return some useful results. Tips say, thank you, thank you, tips.
Rustem says, you know, the impact of documents' segmentation, so basically, what are the suggestions to improve that so that wormhole vectors would be useful? Yeah, I think- Especially for much documents.
Yeah, I mean, I think it's common sense, like the same way that you would chunk documents for doing RAAG, you know, I happen to think of, you know, if the documents are too big, then there's too much loss of specificity and too much context being blurred together.
And if the documents are too tiny, then you're losing context, and they're too specific and not enough overlap.
So I think, you know, typical, like whatever your domain is, you know, I mean, if you've got giant PDFs that are books, maybe break into the chapters or possibly even sections of chapters of the large sections, but yeah, just like use common sense.
What's a reasonable size document that represents the meaning of something that is, like sort of, it's called integral, like a whole thing, a whole concept. Yeah, yeah. It depends on the domain, but I would just say, you know, your common sense is probably going to take you far on that one.
Yeah, and like for long documents that are like at 1,000 pages for sure you want to do that. And maybe the last question is from Arjun. Can this idea of wormhole vectors give us more serendipitous results? Give us more what? Serendipitous results. Yeah, absolutely.
So yeah, think of just the behavioral space, right? If I run a query, a keyword query, and then I want to find other things that are related to this that don't match the terms and maybe don't even match the meaning, but like user behavior has said that these things I should suggest.
I'm basically infusing recommendations then. If I help over to the cement to the dense space, then I take my keywords and I'm finding other things that share meaning, but don't necessarily have that keyword. I'm starting with dense and I hop over to the electrical side.
I'm making sure that I'm finding things with that meaning, but I'm adding in keywords that were completely ignored by the dense space. That was not necessarily a serendipitous. That's just like fixing problems, but I would say going from lexical to semantic.
More so we'll get you things that were dismissed. But yeah, for actual serendipitous, the behavioral space is probably going to give you a lot more magic there. All right, awesome. I think it's a wrap. Thanks so much, everyone.
Trey, thank you so much for the presentation, for the idea, and for pounding at the questions with such an immense speed. Thank you all for time. This was awesome. Awesome. Thanks to me to really appreciate you coming on. This was awesome. Thanks to everybody for joining.
And yeah, the video and slides and everything will be coming out to you. And I hope to see you soon. Thank you. See you soon. Bye bye. Bye.