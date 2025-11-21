---
description: '<p>Vector Podcast website: <a target="_blank" rel="noopener noreferrer
  nofollow" href="https://vectorpodcast.com">https://vectorpodcast.com</a></p><p></p><p>Haystack
  US 2025: <a target="_blank" rel="noopener noreferrer nofollow" href="https://haystackconf.com/2025/">https://haystackconf.com/2025/</a></p><p></p><p>Federated
  search, Keyword &amp; Neural Search, ML Optimisation, Pros and Cons of Hybrid search</p><p></p><p>It
  is fascinating and funny how things develop, but also turn around. In 2022-23 everyone
  was buzzing about hybrid search. In 2024 the conversation shifted to RAG, RAG, RAG.
  And now we are in 2025 and back to hybrid search - on a different level: finally
  there are strides and contributions towards making hybrid search parameters learnt
  with ML. How cool is that?</p><p></p><p>Design: Saurabh Rai, <a target="_blank"
  rel="noopener noreferrer nofollow" href="https://www.linkedin.com/in/srbhr/">https://www.linkedin.com/in/srbhr/</a></p><p>The
  design of this episode is inspired by a scene in Blade Runner 2049. There''s a clear
  path leading towards where people want to go to, yet they''re searching for something.</p><p></p><p>00:00
  Intro</p><p>00:54 Eric''s intro and Daniel''s background</p><p>02:50 Importance
  of Hybrid search: Daniel''s take</p><p>07:26 Eric''s take</p><p>10:57 Dmitry''s
  take</p><p>11:41 Eric''s predictions</p><p>13:47 Doug''s blog on RRF is not enough</p><p>16:18
  How to not fall short of the blind picking in RRF: score normalization, combinations
  and weights</p><p>25:03 The role of query understanding: feature groups</p><p>35:11
  Lesson 1 from Daniel: Simple models might be all you need</p><p>36:30 Lesson 2:
  query features might be all you need</p><p>38:30 Reasoning capabilities in search</p><p>40:02
  Question from Eric: how is this different from Learning To Rank?</p><p>42:46 Carrying
  the past in Learning To Rank / any rank</p><p>44:21 Demo!</p><p>51:52 How to consume
  this in OpenSearch</p><p>55:15 What''s next</p><p>58:44 Haystack US 2025</p><p></p><p>YouTube:
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://www.youtube.com/watch?v=quY769om1EY">https://www.youtube.com/watch?v=quY769om1EY</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20250321_110308_985bc30944ce48882d237ba24dea55a4.png
pub_date: Fri, 21 Mar 2025 11:33:23 GMT
title: 'Adding ML layer to Search: Hybrid Search Optimizer with Daniel Wrigley and
  Eric Pugh'
url: https://rss.com/podcasts/vector-podcast/1951801
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 19.48, "text": " Hello
  there, Vector Podcast is back.", "tokens": [50364, 2425, 456, 11, 691, 20814, 29972,
  307, 646, 13, 51338], "temperature": 0.0, "avg_logprob": -0.377059421023807, "compression_ratio":
  1.1504424778761062, "no_speech_prob": 0.23972827196121216}, {"id": 1, "seek": 0,
  "start": 19.48, "end": 21.88, "text": " Same season 3.", "tokens": [51338, 10635,
  3196, 805, 13, 51458], "temperature": 0.0, "avg_logprob": -0.377059421023807, "compression_ratio":
  1.1504424778761062, "no_speech_prob": 0.23972827196121216}, {"id": 2, "seek": 0,
  "start": 21.88, "end": 27.0, "text": " I think we are about to wrap it up with few
  final really interesting episodes.", "tokens": [51458, 286, 519, 321, 366, 466,
  281, 7019, 309, 493, 365, 1326, 2572, 534, 1880, 9313, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.377059421023807, "compression_ratio": 1.1504424778761062,
  "no_speech_prob": 0.23972827196121216}, {"id": 3, "seek": 2700, "start": 27.0, "end":
  32.44, "text": " There I have the privilege to talk to the open source crew Eric
  Pugh who you have seen", "tokens": [50364, 821, 286, 362, 264, 12122, 281, 751,
  281, 264, 1269, 4009, 7260, 9336, 430, 1984, 567, 291, 362, 1612, 50636], "temperature":
  0.0, "avg_logprob": -0.4400940972405511, "compression_ratio": 1.495049504950495,
  "no_speech_prob": 0.3294818103313446}, {"id": 4, "seek": 2700, "start": 32.44, "end":
  40.24, "text": " in the one of the previous episodes and you guessed Daniel Riggly
  joining us to discuss", "tokens": [50636, 294, 264, 472, 295, 264, 3894, 9313, 293,
  291, 21852, 8033, 497, 46737, 5549, 505, 281, 2248, 51026], "temperature": 0.0,
  "avg_logprob": -0.4400940972405511, "compression_ratio": 1.495049504950495, "no_speech_prob":
  0.3294818103313446}, {"id": 5, "seek": 2700, "start": 40.24, "end": 46.84, "text":
  " really interesting topic on hybrid search and optimization.", "tokens": [51026,
  534, 1880, 4829, 322, 13051, 3164, 293, 19618, 13, 51356], "temperature": 0.0, "avg_logprob":
  -0.4400940972405511, "compression_ratio": 1.495049504950495, "no_speech_prob": 0.3294818103313446},
  {"id": 6, "seek": 2700, "start": 46.84, "end": 49.2, "text": " Really really excited
  to have you both on the show.", "tokens": [51356, 4083, 534, 2919, 281, 362, 291,
  1293, 322, 264, 855, 13, 51474], "temperature": 0.0, "avg_logprob": -0.4400940972405511,
  "compression_ratio": 1.495049504950495, "no_speech_prob": 0.3294818103313446}, {"id":
  7, "seek": 2700, "start": 49.2, "end": 50.2, "text": " Hello.", "tokens": [51474,
  2425, 13, 51524], "temperature": 0.0, "avg_logprob": -0.4400940972405511, "compression_ratio":
  1.495049504950495, "no_speech_prob": 0.3294818103313446}, {"id": 8, "seek": 2700,
  "start": 50.2, "end": 52.04, "text": " Awesome.", "tokens": [51524, 10391, 13, 51616],
  "temperature": 0.0, "avg_logprob": -0.4400940972405511, "compression_ratio": 1.495049504950495,
  "no_speech_prob": 0.3294818103313446}, {"id": 9, "seek": 5204, "start": 53.04, "end":
  54.04, "text": " Awesome.", "tokens": [50414, 10391, 13, 50464], "temperature":
  0.0, "avg_logprob": -0.2870995751742659, "compression_ratio": 1.6875, "no_speech_prob":
  0.29941433668136597}, {"id": 10, "seek": 5204, "start": 54.04, "end": 58.04, "text":
  " So as a tradition we start with the intros.", "tokens": [50464, 407, 382, 257,
  6994, 321, 722, 365, 264, 560, 2635, 13, 50664], "temperature": 0.0, "avg_logprob":
  -0.2870995751742659, "compression_ratio": 1.6875, "no_speech_prob": 0.29941433668136597},
  {"id": 11, "seek": 5204, "start": 58.04, "end": 63.04, "text": " Eric everyone knows
  but Eric feel free to introduce yourself.", "tokens": [50664, 9336, 1518, 3255,
  457, 9336, 841, 1737, 281, 5366, 1803, 13, 50914], "temperature": 0.0, "avg_logprob":
  -0.2870995751742659, "compression_ratio": 1.6875, "no_speech_prob": 0.29941433668136597},
  {"id": 12, "seek": 5204, "start": 63.04, "end": 65.03999999999999, "text": " I mean
  great to be back to me tree.", "tokens": [50914, 286, 914, 869, 281, 312, 646, 281,
  385, 4230, 13, 51014], "temperature": 0.0, "avg_logprob": -0.2870995751742659, "compression_ratio":
  1.6875, "no_speech_prob": 0.29941433668136597}, {"id": 13, "seek": 5204, "start":
  65.03999999999999, "end": 69.75999999999999, "text": " I actually I''m a little
  late getting here because I realized I was driving to the office", "tokens": [51014,
  286, 767, 286, 478, 257, 707, 3469, 1242, 510, 570, 286, 5334, 286, 390, 4840, 281,
  264, 3398, 51250], "temperature": 0.0, "avg_logprob": -0.2870995751742659, "compression_ratio":
  1.6875, "no_speech_prob": 0.29941433668136597}, {"id": 14, "seek": 5204, "start":
  69.75999999999999, "end": 73.32, "text": " that I forgot my mug that you gave me
  the other year.", "tokens": [51250, 300, 286, 5298, 452, 23610, 300, 291, 2729,
  385, 264, 661, 1064, 13, 51428], "temperature": 0.0, "avg_logprob": -0.2870995751742659,
  "compression_ratio": 1.6875, "no_speech_prob": 0.29941433668136597}, {"id": 15,
  "seek": 5204, "start": 73.32, "end": 76.52, "text": " So I actually called Daniels
  like I''m going to be a little late because I got to go home", "tokens": [51428,
  407, 286, 767, 1219, 8033, 82, 411, 286, 478, 516, 281, 312, 257, 707, 3469, 570,
  286, 658, 281, 352, 1280, 51588], "temperature": 0.0, "avg_logprob": -0.2870995751742659,
  "compression_ratio": 1.6875, "no_speech_prob": 0.29941433668136597}, {"id": 16,
  "seek": 5204, "start": 76.52, "end": 78.8, "text": " and pick up the mug and bring
  it into the office.", "tokens": [51588, 293, 1888, 493, 264, 23610, 293, 1565, 309,
  666, 264, 3398, 13, 51702], "temperature": 0.0, "avg_logprob": -0.2870995751742659,
  "compression_ratio": 1.6875, "no_speech_prob": 0.29941433668136597}, {"id": 17,
  "seek": 7880, "start": 78.8, "end": 82.96, "text": " My wife keeps it and we use
  it when we go hiking but I was like I''m going to bring it into", "tokens": [50364,
  1222, 3836, 5965, 309, 293, 321, 764, 309, 562, 321, 352, 23784, 457, 286, 390,
  411, 286, 478, 516, 281, 1565, 309, 666, 50572], "temperature": 0.0, "avg_logprob":
  -0.26173441863257035, "compression_ratio": 1.713740458015267, "no_speech_prob":
  0.11045863479375839}, {"id": 18, "seek": 7880, "start": 82.96, "end": 88.44, "text":
  " the office and show it off since this is my second podcast to do with you and
  the mug", "tokens": [50572, 264, 3398, 293, 855, 309, 766, 1670, 341, 307, 452,
  1150, 7367, 281, 360, 365, 291, 293, 264, 23610, 50846], "temperature": 0.0, "avg_logprob":
  -0.26173441863257035, "compression_ratio": 1.713740458015267, "no_speech_prob":
  0.11045863479375839}, {"id": 19, "seek": 7880, "start": 88.44, "end": 92.0, "text":
  " that you gave me two years ago three years ago at this point.", "tokens": [50846,
  300, 291, 2729, 385, 732, 924, 2057, 1045, 924, 2057, 412, 341, 935, 13, 51024],
  "temperature": 0.0, "avg_logprob": -0.26173441863257035, "compression_ratio": 1.713740458015267,
  "no_speech_prob": 0.11045863479375839}, {"id": 20, "seek": 7880, "start": 92.0,
  "end": 94.47999999999999, "text": " Yeah probably three years.", "tokens": [51024,
  865, 1391, 1045, 924, 13, 51148], "temperature": 0.0, "avg_logprob": -0.26173441863257035,
  "compression_ratio": 1.713740458015267, "no_speech_prob": 0.11045863479375839},
  {"id": 21, "seek": 7880, "start": 94.47999999999999, "end": 95.84, "text": " Works
  great works great.", "tokens": [51148, 27914, 869, 1985, 869, 13, 51216], "temperature":
  0.0, "avg_logprob": -0.26173441863257035, "compression_ratio": 1.713740458015267,
  "no_speech_prob": 0.11045863479375839}, {"id": 22, "seek": 7880, "start": 95.84,
  "end": 101.12, "text": " So yeah super excited to be back here and you know kind
  of talk about some of the work", "tokens": [51216, 407, 1338, 1687, 2919, 281, 312,
  646, 510, 293, 291, 458, 733, 295, 751, 466, 512, 295, 264, 589, 51480], "temperature":
  0.0, "avg_logprob": -0.26173441863257035, "compression_ratio": 1.713740458015267,
  "no_speech_prob": 0.11045863479375839}, {"id": 23, "seek": 7880, "start": 101.12,
  "end": 103.67999999999999, "text": " that we''ve been doing with the open search
  community.", "tokens": [51480, 300, 321, 600, 668, 884, 365, 264, 1269, 3164, 1768,
  13, 51608], "temperature": 0.0, "avg_logprob": -0.26173441863257035, "compression_ratio":
  1.713740458015267, "no_speech_prob": 0.11045863479375839}, {"id": 24, "seek": 7880,
  "start": 103.67999999999999, "end": 105.28, "text": " So exciting.", "tokens": [51608,
  407, 4670, 13, 51688], "temperature": 0.0, "avg_logprob": -0.26173441863257035,
  "compression_ratio": 1.713740458015267, "no_speech_prob": 0.11045863479375839},
  {"id": 25, "seek": 7880, "start": 105.28, "end": 107.08, "text": " Yes.", "tokens":
  [51688, 1079, 13, 51778], "temperature": 0.0, "avg_logprob": -0.26173441863257035,
  "compression_ratio": 1.713740458015267, "no_speech_prob": 0.11045863479375839},
  {"id": 26, "seek": 10708, "start": 107.08, "end": 109.12, "text": " And Daniel welcome.",
  "tokens": [50364, 400, 8033, 2928, 13, 50466], "temperature": 0.0, "avg_logprob":
  -0.30384905745343466, "compression_ratio": 1.4292682926829268, "no_speech_prob":
  0.029049118980765343}, {"id": 27, "seek": 10708, "start": 109.12, "end": 111.88,
  "text": " Can you say a few words about yourself your background?", "tokens": [50466,
  1664, 291, 584, 257, 1326, 2283, 466, 1803, 428, 3678, 30, 50604], "temperature":
  0.0, "avg_logprob": -0.30384905745343466, "compression_ratio": 1.4292682926829268,
  "no_speech_prob": 0.029049118980765343}, {"id": 28, "seek": 10708, "start": 111.88,
  "end": 114.0, "text": " Absolutely yeah thanks.", "tokens": [50604, 7021, 1338,
  3231, 13, 50710], "temperature": 0.0, "avg_logprob": -0.30384905745343466, "compression_ratio":
  1.4292682926829268, "no_speech_prob": 0.029049118980765343}, {"id": 29, "seek":
  10708, "start": 114.0, "end": 115.0, "text": " It''s great to be here.", "tokens":
  [50710, 467, 311, 869, 281, 312, 510, 13, 50760], "temperature": 0.0, "avg_logprob":
  -0.30384905745343466, "compression_ratio": 1.4292682926829268, "no_speech_prob":
  0.029049118980765343}, {"id": 30, "seek": 10708, "start": 115.0, "end": 119.52,
  "text": " I''m super excited maybe a little nervous but I''m sure it''ll be fun.",
  "tokens": [50760, 286, 478, 1687, 2919, 1310, 257, 707, 6296, 457, 286, 478, 988,
  309, 603, 312, 1019, 13, 50986], "temperature": 0.0, "avg_logprob": -0.30384905745343466,
  "compression_ratio": 1.4292682926829268, "no_speech_prob": 0.029049118980765343},
  {"id": 31, "seek": 10708, "start": 119.52, "end": 123.2, "text": " So I''m Daniel
  I''m with open source connections.", "tokens": [50986, 407, 286, 478, 8033, 286,
  478, 365, 1269, 4009, 9271, 13, 51170], "temperature": 0.0, "avg_logprob": -0.30384905745343466,
  "compression_ratio": 1.4292682926829268, "no_speech_prob": 0.029049118980765343},
  {"id": 32, "seek": 10708, "start": 123.2, "end": 129.48, "text": " I started out
  as a search consultant back in May 2012.", "tokens": [51170, 286, 1409, 484, 382,
  257, 3164, 24676, 646, 294, 1891, 9125, 13, 51484], "temperature": 0.0, "avg_logprob":
  -0.30384905745343466, "compression_ratio": 1.4292682926829268, "no_speech_prob":
  0.029049118980765343}, {"id": 33, "seek": 12948, "start": 129.48, "end": 140.35999999999999,
  "text": " So almost 13 years now and I''m here to share some of our experiences
  that we made in our", "tokens": [50364, 407, 1920, 3705, 924, 586, 293, 286, 478,
  510, 281, 2073, 512, 295, 527, 5235, 300, 321, 1027, 294, 527, 50908], "temperature":
  0.0, "avg_logprob": -0.20429320335388185, "compression_ratio": 1.6462264150943395,
  "no_speech_prob": 0.11860533803701401}, {"id": 34, "seek": 12948, "start": 140.35999999999999,
  "end": 146.6, "text": " most recent project together with the folks of open search
  when it comes to hybrid search", "tokens": [50908, 881, 5162, 1716, 1214, 365, 264,
  4024, 295, 1269, 3164, 562, 309, 1487, 281, 13051, 3164, 51220], "temperature":
  0.0, "avg_logprob": -0.20429320335388185, "compression_ratio": 1.6462264150943395,
  "no_speech_prob": 0.11860533803701401}, {"id": 35, "seek": 12948, "start": 146.6,
  "end": 153.28, "text": " how to optimize hybrid search and also what''s necessary
  to optimize hybrid search namely", "tokens": [51220, 577, 281, 19719, 13051, 3164,
  293, 611, 437, 311, 4818, 281, 19719, 13051, 3164, 20926, 51554], "temperature":
  0.0, "avg_logprob": -0.20429320335388185, "compression_ratio": 1.6462264150943395,
  "no_speech_prob": 0.11860533803701401}, {"id": 36, "seek": 12948, "start": 153.28,
  "end": 158.88, "text": " query sets and judgments but I''m sure we''ll get into
  that in a couple of seconds.", "tokens": [51554, 14581, 6352, 293, 40337, 457, 286,
  478, 988, 321, 603, 483, 666, 300, 294, 257, 1916, 295, 3949, 13, 51834], "temperature":
  0.0, "avg_logprob": -0.20429320335388185, "compression_ratio": 1.6462264150943395,
  "no_speech_prob": 0.11860533803701401}, {"id": 37, "seek": 15888, "start": 158.88,
  "end": 160.28, "text": " Yeah thanks Daniel.", "tokens": [50364, 865, 3231, 8033,
  13, 50434], "temperature": 0.0, "avg_logprob": -0.3505380980822505, "compression_ratio":
  1.5956521739130434, "no_speech_prob": 0.039369069039821625}, {"id": 38, "seek":
  15888, "start": 160.28, "end": 167.35999999999999, "text": " I''m also nervous but
  I also know that you know when I release in the episodes I enjoy them.", "tokens":
  [50434, 286, 478, 611, 6296, 457, 286, 611, 458, 300, 291, 458, 562, 286, 4374,
  294, 264, 9313, 286, 2103, 552, 13, 50788], "temperature": 0.0, "avg_logprob": -0.3505380980822505,
  "compression_ratio": 1.5956521739130434, "no_speech_prob": 0.039369069039821625},
  {"id": 39, "seek": 15888, "start": 167.35999999999999, "end": 169.76, "text": "
  It''s just it''s just fun really.", "tokens": [50788, 467, 311, 445, 309, 311, 445,
  1019, 534, 13, 50908], "temperature": 0.0, "avg_logprob": -0.3505380980822505, "compression_ratio":
  1.5956521739130434, "no_speech_prob": 0.039369069039821625}, {"id": 40, "seek":
  15888, "start": 169.76, "end": 174.12, "text": " So I was thinking like hybrid search
  yeah we did discuss and I think community discusses", "tokens": [50908, 407, 286,
  390, 1953, 411, 13051, 3164, 1338, 321, 630, 2248, 293, 286, 519, 1768, 2248, 279,
  51126], "temperature": 0.0, "avg_logprob": -0.3505380980822505, "compression_ratio":
  1.5956521739130434, "no_speech_prob": 0.039369069039821625}, {"id": 41, "seek":
  15888, "start": 174.12, "end": 176.76, "text": " it at large and various forums.",
  "tokens": [51126, 309, 412, 2416, 293, 3683, 26998, 13, 51258], "temperature": 0.0,
  "avg_logprob": -0.3505380980822505, "compression_ratio": 1.5956521739130434, "no_speech_prob":
  0.039369069039821625}, {"id": 42, "seek": 15888, "start": 176.76, "end": 182.04,
  "text": " Erick also reminded me of the episode with Alessandro Benindetti that
  we just did it really", "tokens": [51258, 3300, 618, 611, 15920, 385, 295, 264,
  3500, 365, 967, 442, 29173, 3964, 471, 12495, 300, 321, 445, 630, 309, 534, 51522],
  "temperature": 0.0, "avg_logprob": -0.3505380980822505, "compression_ratio": 1.5956521739130434,
  "no_speech_prob": 0.039369069039821625}, {"id": 43, "seek": 15888, "start": 182.04,
  "end": 183.04, "text": " was worth.", "tokens": [51522, 390, 3163, 13, 51572], "temperature":
  0.0, "avg_logprob": -0.3505380980822505, "compression_ratio": 1.5956521739130434,
  "no_speech_prob": 0.039369069039821625}, {"id": 44, "seek": 18304, "start": 184.04,
  "end": 190.64, "text": " Yeah I was really just curious maybe step back from that
  topic a little bit and discuss", "tokens": [50414, 865, 286, 390, 534, 445, 6369,
  1310, 1823, 646, 490, 300, 4829, 257, 707, 857, 293, 2248, 50744], "temperature":
  0.0, "avg_logprob": -0.18696778615315754, "compression_ratio": 1.5869565217391304,
  "no_speech_prob": 0.072663314640522}, {"id": 45, "seek": 18304, "start": 190.64,
  "end": 195.23999999999998, "text": " the importance of hybrid search and what is
  it in your own words where do you see value", "tokens": [50744, 264, 7379, 295,
  13051, 3164, 293, 437, 307, 309, 294, 428, 1065, 2283, 689, 360, 291, 536, 2158,
  50974], "temperature": 0.0, "avg_logprob": -0.18696778615315754, "compression_ratio":
  1.5869565217391304, "no_speech_prob": 0.072663314640522}, {"id": 46, "seek": 18304,
  "start": 195.23999999999998, "end": 200.92, "text": " for it compared to how we
  used to do search before.", "tokens": [50974, 337, 309, 5347, 281, 577, 321, 1143,
  281, 360, 3164, 949, 13, 51258], "temperature": 0.0, "avg_logprob": -0.18696778615315754,
  "compression_ratio": 1.5869565217391304, "no_speech_prob": 0.072663314640522}, {"id":
  47, "seek": 18304, "start": 200.92, "end": 203.6, "text": " You want to take it
  Daniel and then I''ll follow up.", "tokens": [51258, 509, 528, 281, 747, 309, 8033,
  293, 550, 286, 603, 1524, 493, 13, 51392], "temperature": 0.0, "avg_logprob": -0.18696778615315754,
  "compression_ratio": 1.5869565217391304, "no_speech_prob": 0.072663314640522}, {"id":
  48, "seek": 18304, "start": 203.6, "end": 211.32, "text": " Sure yeah so I think
  we see hybrid search especially in this project as let''s say the", "tokens": [51392,
  4894, 1338, 370, 286, 519, 321, 536, 13051, 3164, 2318, 294, 341, 1716, 382, 718,
  311, 584, 264, 51778], "temperature": 0.0, "avg_logprob": -0.18696778615315754,
  "compression_ratio": 1.5869565217391304, "no_speech_prob": 0.072663314640522}, {"id":
  49, "seek": 21132, "start": 211.32, "end": 218.4, "text": " process of blending
  traditional keyword search and also let''s say modern search approaches", "tokens":
  [50364, 1399, 295, 23124, 5164, 20428, 3164, 293, 611, 718, 311, 584, 4363, 3164,
  11587, 50718], "temperature": 0.0, "avg_logprob": -0.280281497586158, "compression_ratio":
  1.5730337078651686, "no_speech_prob": 0.0051127891056239605}, {"id": 50, "seek":
  21132, "start": 218.4, "end": 227.56, "text": " based on language more or mostly
  called either vector search or neuro search and I think", "tokens": [50718, 2361,
  322, 2856, 544, 420, 5240, 1219, 2139, 8062, 3164, 420, 16499, 3164, 293, 286, 519,
  51176], "temperature": 0.0, "avg_logprob": -0.280281497586158, "compression_ratio":
  1.5730337078651686, "no_speech_prob": 0.0051127891056239605}, {"id": 51, "seek":
  21132, "start": 227.56, "end": 235.4, "text": " the benefits of it are probably
  you follow it or I guess you can you can group them into", "tokens": [51176, 264,
  5311, 295, 309, 366, 1391, 291, 1524, 309, 420, 286, 2041, 291, 393, 291, 393, 1594,
  552, 666, 51568], "temperature": 0.0, "avg_logprob": -0.280281497586158, "compression_ratio":
  1.5730337078651686, "no_speech_prob": 0.0051127891056239605}, {"id": 52, "seek":
  21132, "start": 235.4, "end": 236.4, "text": " two groups.", "tokens": [51568, 732,
  3935, 13, 51618], "temperature": 0.0, "avg_logprob": -0.280281497586158, "compression_ratio":
  1.5730337078651686, "no_speech_prob": 0.0051127891056239605}, {"id": 53, "seek":
  23640, "start": 236.96, "end": 243.84, "text": " Looking at the end user we always
  want to provide the end users with the most or the", "tokens": [50392, 11053, 412,
  264, 917, 4195, 321, 1009, 528, 281, 2893, 264, 917, 5022, 365, 264, 881, 420, 264,
  50736], "temperature": 0.0, "avg_logprob": -0.18179401397705078, "compression_ratio":
  1.6495327102803738, "no_speech_prob": 0.030946411192417145}, {"id": 54, "seek":
  23640, "start": 243.84, "end": 251.04000000000002, "text": " highest quality results
  right so search result quality is what we strive for and traditional", "tokens":
  [50736, 6343, 3125, 3542, 558, 370, 3164, 1874, 3125, 307, 437, 321, 23829, 337,
  293, 5164, 51096], "temperature": 0.0, "avg_logprob": -0.18179401397705078, "compression_ratio":
  1.6495327102803738, "no_speech_prob": 0.030946411192417145}, {"id": 55, "seek":
  23640, "start": 251.04000000000002, "end": 258.36, "text": " keyword search always
  lacks of let''s say finding related things that may not really contain", "tokens":
  [51096, 20428, 3164, 1009, 31132, 295, 718, 311, 584, 5006, 4077, 721, 300, 815,
  406, 534, 5304, 51462], "temperature": 0.0, "avg_logprob": -0.18179401397705078,
  "compression_ratio": 1.6495327102803738, "no_speech_prob": 0.030946411192417145},
  {"id": 56, "seek": 23640, "start": 258.36, "end": 265.44, "text": " the specific
  words but similar so laptop and notebook is an example that I think we", "tokens":
  [51462, 264, 2685, 2283, 457, 2531, 370, 10732, 293, 21060, 307, 364, 1365, 300,
  286, 519, 321, 51816], "temperature": 0.0, "avg_logprob": -0.18179401397705078,
  "compression_ratio": 1.6495327102803738, "no_speech_prob": 0.030946411192417145},
  {"id": 57, "seek": 26544, "start": 265.44, "end": 273.24, "text": " ran probably
  a million times in demos maybe even more than a million times so if notebook", "tokens":
  [50364, 5872, 1391, 257, 2459, 1413, 294, 33788, 1310, 754, 544, 813, 257, 2459,
  1413, 370, 498, 21060, 50754], "temperature": 0.0, "avg_logprob": -0.1342410099359206,
  "compression_ratio": 1.6515837104072397, "no_speech_prob": 0.004714095965027809},
  {"id": 58, "seek": 26544, "start": 273.24, "end": 278.16, "text": " is not in my
  product description I will not find it when I search for laptop and the other",
  "tokens": [50754, 307, 406, 294, 452, 1674, 3855, 286, 486, 406, 915, 309, 562,
  286, 3164, 337, 10732, 293, 264, 661, 51000], "temperature": 0.0, "avg_logprob":
  -0.1342410099359206, "compression_ratio": 1.6515837104072397, "no_speech_prob":
  0.004714095965027809}, {"id": 59, "seek": 26544, "start": 278.16, "end": 286.6,
  "text": " way around and that''s where let''s say blending the two techniques really
  shine because it enables", "tokens": [51000, 636, 926, 293, 300, 311, 689, 718,
  311, 584, 23124, 264, 732, 7512, 534, 12207, 570, 309, 17077, 51422], "temperature":
  0.0, "avg_logprob": -0.1342410099359206, "compression_ratio": 1.6515837104072397,
  "no_speech_prob": 0.004714095965027809}, {"id": 60, "seek": 26544, "start": 286.6,
  "end": 293.24, "text": " you to not only find where your keywords are in but also
  find related stuff to augment", "tokens": [51422, 291, 281, 406, 787, 915, 689,
  428, 21009, 366, 294, 457, 611, 915, 4077, 1507, 281, 29919, 51754], "temperature":
  0.0, "avg_logprob": -0.1342410099359206, "compression_ratio": 1.6515837104072397,
  "no_speech_prob": 0.004714095965027809}, {"id": 61, "seek": 29324, "start": 293.48,
  "end": 301.64, "text": " the result set and I think that with that with that large
  benefit of course come a lot of", "tokens": [50376, 264, 1874, 992, 293, 286, 519,
  300, 365, 300, 365, 300, 2416, 5121, 295, 1164, 808, 257, 688, 295, 50784], "temperature":
  0.0, "avg_logprob": -0.1804484110029917, "compression_ratio": 1.680473372781065,
  "no_speech_prob": 0.0049310545437037945}, {"id": 62, "seek": 29324, "start": 301.64,
  "end": 309.72, "text": " challenges because it always is let''s say non-tribal how
  to actually blend the traditional techniques", "tokens": [50784, 4759, 570, 309,
  1009, 307, 718, 311, 584, 2107, 12, 83, 2024, 304, 577, 281, 767, 10628, 264, 5164,
  7512, 51188], "temperature": 0.0, "avg_logprob": -0.1804484110029917, "compression_ratio":
  1.680473372781065, "no_speech_prob": 0.0049310545437037945}, {"id": 63, "seek":
  29324, "start": 309.72, "end": 317.08, "text": " and the more modern techniques
  so that''s where the challenge between or the challenge behind", "tokens": [51188,
  293, 264, 544, 4363, 7512, 370, 300, 311, 689, 264, 3430, 1296, 420, 264, 3430,
  2261, 51556], "temperature": 0.0, "avg_logprob": -0.1804484110029917, "compression_ratio":
  1.680473372781065, "no_speech_prob": 0.0049310545437037945}, {"id": 64, "seek":
  31708, "start": 317.15999999999997, "end": 323.47999999999996, "text": " hybrid
  search actually lies. I mentioned two groups for which there are benefits of the
  end user", "tokens": [50368, 13051, 3164, 767, 9134, 13, 286, 2835, 732, 3935, 337,
  597, 456, 366, 5311, 295, 264, 917, 4195, 50684], "temperature": 0.0, "avg_logprob":
  -0.11517394343508949, "compression_ratio": 1.7395348837209301, "no_speech_prob":
  0.007801172323524952}, {"id": 65, "seek": 31708, "start": 323.47999999999996, "end":
  328.44, "text": " we want to provide the end user with the highest quality results
  that''s one group the other", "tokens": [50684, 321, 528, 281, 2893, 264, 917, 4195,
  365, 264, 6343, 3125, 3542, 300, 311, 472, 1594, 264, 661, 50932], "temperature":
  0.0, "avg_logprob": -0.11517394343508949, "compression_ratio": 1.7395348837209301,
  "no_speech_prob": 0.007801172323524952}, {"id": 66, "seek": 31708, "start": 328.44,
  "end": 335.4, "text": " group is of course we as the ones providing search applications
  I mean we somehow need to profit", "tokens": [50932, 1594, 307, 295, 1164, 321,
  382, 264, 2306, 6530, 3164, 5821, 286, 914, 321, 6063, 643, 281, 7475, 51280], "temperature":
  0.0, "avg_logprob": -0.11517394343508949, "compression_ratio": 1.7395348837209301,
  "no_speech_prob": 0.007801172323524952}, {"id": 67, "seek": 31708, "start": 335.4,
  "end": 344.28, "text": " from providing better results and it then is always different
  or yeah different in which", "tokens": [51280, 490, 6530, 1101, 3542, 293, 309,
  550, 307, 1009, 819, 420, 1338, 819, 294, 597, 51724], "temperature": 0.0, "avg_logprob":
  -0.11517394343508949, "compression_ratio": 1.7395348837209301, "no_speech_prob":
  0.007801172323524952}, {"id": 68, "seek": 34428, "start": 344.28, "end": 349.79999999999995,
  "text": " let''s say scenario in which industry we are working so the monosperm
  transparent one is always", "tokens": [50364, 718, 311, 584, 9005, 294, 597, 3518,
  321, 366, 1364, 370, 264, 1108, 329, 610, 76, 12737, 472, 307, 1009, 50640], "temperature":
  0.0, "avg_logprob": -0.18972611701351472, "compression_ratio": 1.7149122807017543,
  "no_speech_prob": 0.0008283494389615953}, {"id": 69, "seek": 34428, "start": 349.79999999999995,
  "end": 357.23999999999995, "text": " e-commerce the easier the end user the consumer
  actually finds stuff in your online shop the easier", "tokens": [50640, 308, 12,
  26926, 264, 3571, 264, 917, 4195, 264, 9711, 767, 10704, 1507, 294, 428, 2950, 3945,
  264, 3571, 51012], "temperature": 0.0, "avg_logprob": -0.18972611701351472, "compression_ratio":
  1.7149122807017543, "no_speech_prob": 0.0008283494389615953}, {"id": 70, "seek":
  34428, "start": 357.23999999999995, "end": 363.23999999999995, "text": " is for
  them to buy stuff if they buy more stuff more easily of course we generate more
  revenue and", "tokens": [51012, 307, 337, 552, 281, 2256, 1507, 498, 436, 2256,
  544, 1507, 544, 3612, 295, 1164, 321, 8460, 544, 9324, 293, 51312], "temperature":
  0.0, "avg_logprob": -0.18972611701351472, "compression_ratio": 1.7149122807017543,
  "no_speech_prob": 0.0008283494389615953}, {"id": 71, "seek": 34428, "start": 363.23999999999995,
  "end": 371.96, "text": " that''s kind of the benefit then that comes with providing
  better search results and the other way", "tokens": [51312, 300, 311, 733, 295,
  264, 5121, 550, 300, 1487, 365, 6530, 1101, 3164, 3542, 293, 264, 661, 636, 51748],
  "temperature": 0.0, "avg_logprob": -0.18972611701351472, "compression_ratio": 1.7149122807017543,
  "no_speech_prob": 0.0008283494389615953}, {"id": 72, "seek": 37196, "start": 371.96,
  "end": 381.32, "text": " is we don''t want to let''s say manually tune systems let''s
  say indefinitely so of course I can", "tokens": [50364, 307, 321, 500, 380, 528,
  281, 718, 311, 584, 16945, 10864, 3652, 718, 311, 584, 24162, 10925, 370, 295, 1164,
  286, 393, 50832], "temperature": 0.0, "avg_logprob": -0.07885779937108357, "compression_ratio":
  1.5567567567567568, "no_speech_prob": 0.0034359849523752928}, {"id": 73, "seek":
  37196, "start": 381.32, "end": 391.4, "text": " go ahead and say laptop is synonymous
  to notebook and PC is maybe broader term of laptop and rules", "tokens": [50832,
  352, 2286, 293, 584, 10732, 307, 5451, 18092, 281, 21060, 293, 6465, 307, 1310,
  13227, 1433, 295, 10732, 293, 4474, 51336], "temperature": 0.0, "avg_logprob": -0.07885779937108357,
  "compression_ratio": 1.5567567567567568, "no_speech_prob": 0.0034359849523752928},
  {"id": 74, "seek": 37196, "start": 391.4, "end": 399.79999999999995, "text": " like
  these but that''s kind of work that is never done if I have a changing catalog that
  I don''t", "tokens": [51336, 411, 613, 457, 300, 311, 733, 295, 589, 300, 307, 1128,
  1096, 498, 286, 362, 257, 4473, 19746, 300, 286, 500, 380, 51756], "temperature":
  0.0, "avg_logprob": -0.07885779937108357, "compression_ratio": 1.5567567567567568,
  "no_speech_prob": 0.0034359849523752928}, {"id": 75, "seek": 39980, "start": 400.44,
  "end": 407.24, "text": " know old products get thrown out of the product catalog
  new products arrive so it''s a never-ending", "tokens": [50396, 458, 1331, 3383,
  483, 11732, 484, 295, 264, 1674, 19746, 777, 3383, 8881, 370, 309, 311, 257, 1128,
  12, 2029, 50736], "temperature": 0.0, "avg_logprob": -0.1322068590106386, "compression_ratio":
  1.6010928961748634, "no_speech_prob": 0.0010116742923855782}, {"id": 76, "seek":
  39980, "start": 407.24, "end": 416.04, "text": " challenge for me and I don''t want
  to let''s say spend my work for us always manually hunting these", "tokens": [50736,
  3430, 337, 385, 293, 286, 500, 380, 528, 281, 718, 311, 584, 3496, 452, 589, 337,
  505, 1009, 16945, 12599, 613, 51176], "temperature": 0.0, "avg_logprob": -0.1322068590106386,
  "compression_ratio": 1.6010928961748634, "no_speech_prob": 0.0010116742923855782},
  {"id": 77, "seek": 39980, "start": 416.04, "end": 422.12, "text": " rules and thinking
  about what made the users mean when they start for something I want something",
  "tokens": [51176, 4474, 293, 1953, 466, 437, 1027, 264, 5022, 914, 562, 436, 722,
  337, 746, 286, 528, 746, 51480], "temperature": 0.0, "avg_logprob": -0.1322068590106386,
  "compression_ratio": 1.6010928961748634, "no_speech_prob": 0.0010116742923855782},
  {"id": 78, "seek": 42212, "start": 423.08, "end": 430.68, "text": " let''s say intelligently
  looking for the right things in my index and that''s what the neural part", "tokens":
  [50412, 718, 311, 584, 5613, 2276, 1237, 337, 264, 558, 721, 294, 452, 8186, 293,
  300, 311, 437, 264, 18161, 644, 50792], "temperature": 0.0, "avg_logprob": -0.19416969541519408,
  "compression_ratio": 1.5833333333333333, "no_speech_prob": 0.0043699066154658794},
  {"id": 79, "seek": 42212, "start": 430.68, "end": 439.32, "text": " of hybrid search
  enables us so I think these are definitely maybe the two groups that benefit", "tokens":
  [50792, 295, 13051, 3164, 17077, 505, 370, 286, 519, 613, 366, 2138, 1310, 264,
  732, 3935, 300, 5121, 51224], "temperature": 0.0, "avg_logprob": -0.19416969541519408,
  "compression_ratio": 1.5833333333333333, "no_speech_prob": 0.0043699066154658794},
  {"id": 80, "seek": 42212, "start": 439.32, "end": 445.72, "text": " and how these
  two groups benefit from my perspective yeah that''s really good intro Ericy water",
  "tokens": [51224, 293, 577, 613, 732, 3935, 5121, 490, 452, 4585, 1338, 300, 311,
  534, 665, 12897, 9336, 88, 1281, 51544], "temperature": 0.0, "avg_logprob": -0.19416969541519408,
  "compression_ratio": 1.5833333333333333, "no_speech_prob": 0.0043699066154658794},
  {"id": 81, "seek": 44572, "start": 445.8, "end": 452.36, "text": " take it yeah
  I think it''s an interesting journey that we''ve been on the last few years and
  I", "tokens": [50368, 747, 309, 1338, 286, 519, 309, 311, 364, 1880, 4671, 300,
  321, 600, 668, 322, 264, 1036, 1326, 924, 293, 286, 50696], "temperature": 0.0,
  "avg_logprob": -0.11472883678617932, "compression_ratio": 1.6753246753246753, "no_speech_prob":
  0.002358798636123538}, {"id": 82, "seek": 44572, "start": 452.36, "end": 459.40000000000003,
  "text": " sort of look at hybrid search as a little bit of a like a course correction
  right so keyword search", "tokens": [50696, 1333, 295, 574, 412, 13051, 3164, 382,
  257, 707, 857, 295, 257, 411, 257, 1164, 19984, 558, 370, 20428, 3164, 51048], "temperature":
  0.0, "avg_logprob": -0.11472883678617932, "compression_ratio": 1.6753246753246753,
  "no_speech_prob": 0.002358798636123538}, {"id": 83, "seek": 44572, "start": 459.40000000000003,
  "end": 465.88000000000005, "text": " been around forever well understood frustrations
  are well known and then vectors came out and all", "tokens": [51048, 668, 926, 5680,
  731, 7320, 7454, 12154, 366, 731, 2570, 293, 550, 18875, 1361, 484, 293, 439, 51372],
  "temperature": 0.0, "avg_logprob": -0.11472883678617932, "compression_ratio": 1.6753246753246753,
  "no_speech_prob": 0.002358798636123538}, {"id": 84, "seek": 44572, "start": 465.88000000000005,
  "end": 471.88000000000005, "text": " these new products these new vector databases
  everybody was really excited about them and we all", "tokens": [51372, 613, 777,
  3383, 613, 777, 8062, 22380, 2201, 390, 534, 2919, 466, 552, 293, 321, 439, 51672],
  "temperature": 0.0, "avg_logprob": -0.11472883678617932, "compression_ratio": 1.6753246753246753,
  "no_speech_prob": 0.002358798636123538}, {"id": 85, "seek": 47188, "start": 471.88,
  "end": 477.64, "text": " said oh okay let''s go use vectors and we leapt on that
  and got really excited built everything", "tokens": [50364, 848, 1954, 1392, 718,
  311, 352, 764, 18875, 293, 321, 476, 2796, 322, 300, 293, 658, 534, 2919, 3094,
  1203, 50652], "temperature": 0.0, "avg_logprob": -0.09517174232296827, "compression_ratio":
  1.7570093457943925, "no_speech_prob": 0.0008602467132732272}, {"id": 86, "seek":
  47188, "start": 477.64, "end": 486.28, "text": " using vectors and I think maybe
  we went too far that way over into vector land and we started after", "tokens":
  [50652, 1228, 18875, 293, 286, 519, 1310, 321, 1437, 886, 1400, 300, 636, 670, 666,
  8062, 2117, 293, 321, 1409, 934, 51084], "temperature": 0.0, "avg_logprob": -0.09517174232296827,
  "compression_ratio": 1.7570093457943925, "no_speech_prob": 0.0008602467132732272},
  {"id": 87, "seek": 47188, "start": 486.28, "end": 492.36, "text": " we started getting
  some experience with vectors we started realizing some of the problems with it",
  "tokens": [51084, 321, 1409, 1242, 512, 1752, 365, 18875, 321, 1409, 16734, 512,
  295, 264, 2740, 365, 309, 51388], "temperature": 0.0, "avg_logprob": -0.09517174232296827,
  "compression_ratio": 1.7570093457943925, "no_speech_prob": 0.0008602467132732272},
  {"id": 88, "seek": 47188, "start": 492.36, "end": 498.44, "text": " right like doesn''t
  matter what you query you''re gonna get some search results right", "tokens": [51388,
  558, 411, 1177, 380, 1871, 437, 291, 14581, 291, 434, 799, 483, 512, 3164, 3542,
  558, 51692], "temperature": 0.0, "avg_logprob": -0.09517174232296827, "compression_ratio":
  1.7570093457943925, "no_speech_prob": 0.0008602467132732272}, {"id": 89, "seek":
  49844, "start": 499.4, "end": 507.48, "text": " sometimes zero search results is
  the right answer right you know interesting challenges around", "tokens": [50412,
  2171, 4018, 3164, 3542, 307, 264, 558, 1867, 558, 291, 458, 1880, 4759, 926, 50816],
  "temperature": 0.0, "avg_logprob": -0.1020694308810764, "compression_ratio": 1.742081447963801,
  "no_speech_prob": 0.001348108984529972}, {"id": 90, "seek": 49844, "start": 508.12,
  "end": 514.04, "text": " you know faceting or pagination or highlighting can be
  weird right so you know I think that there", "tokens": [50848, 291, 458, 1915, 9880,
  420, 11812, 2486, 420, 26551, 393, 312, 3657, 558, 370, 291, 458, 286, 519, 300,
  456, 51144], "temperature": 0.0, "avg_logprob": -0.1020694308810764, "compression_ratio":
  1.742081447963801, "no_speech_prob": 0.001348108984529972}, {"id": 91, "seek": 49844,
  "start": 514.04, "end": 519.08, "text": " are some definite challenges in vectors
  and we all went over that way and I think we''ve seen it", "tokens": [51144, 366,
  512, 25131, 4759, 294, 18875, 293, 321, 439, 1437, 670, 300, 636, 293, 286, 519,
  321, 600, 1612, 309, 51396], "temperature": 0.0, "avg_logprob": -0.1020694308810764,
  "compression_ratio": 1.742081447963801, "no_speech_prob": 0.001348108984529972},
  {"id": 92, "seek": 49844, "start": 519.08, "end": 528.36, "text": " in the last
  two years where all the vector databases were frantically adding keyword like search",
  "tokens": [51396, 294, 264, 1036, 732, 924, 689, 439, 264, 8062, 22380, 645, 431,
  49505, 5127, 20428, 411, 3164, 51860], "temperature": 0.0, "avg_logprob": -0.1020694308810764,
  "compression_ratio": 1.742081447963801, "no_speech_prob": 0.001348108984529972},
  {"id": 93, "seek": 52836, "start": 529.16, "end": 538.44, "text": " and all of the
  keyword search indexes were all frantically adding vectors okay now we have these",
  "tokens": [50404, 293, 439, 295, 264, 20428, 3164, 8186, 279, 645, 439, 431, 49505,
  5127, 18875, 1392, 586, 321, 362, 613, 50868], "temperature": 0.0, "avg_logprob":
  -0.13279681735568577, "compression_ratio": 1.5826771653543308, "no_speech_prob":
  0.0006227812846191227}, {"id": 94, "seek": 52836, "start": 538.44, "end": 547.32,
  "text": " things as like where do we go oh hybrid search right hybrid search and
  you know hybrid search popped out", "tokens": [50868, 721, 382, 411, 689, 360, 321,
  352, 1954, 13051, 3164, 558, 13051, 3164, 293, 291, 458, 13051, 3164, 21545, 484,
  51312], "temperature": 0.0, "avg_logprob": -0.13279681735568577, "compression_ratio":
  1.5826771653543308, "no_speech_prob": 0.0006227812846191227}, {"id": 95, "seek":
  54732, "start": 547.4000000000001, "end": 559.88, "text": " and you know hear me
  out I think hybrid search is just good old federated search from the late 90s",
  "tokens": [50368, 293, 291, 458, 1568, 385, 484, 286, 519, 13051, 3164, 307, 445,
  665, 1331, 38024, 770, 3164, 490, 264, 3469, 4289, 82, 50992], "temperature": 0.0,
  "avg_logprob": -0.10870110470315685, "compression_ratio": 1.5956284153005464, "no_speech_prob":
  0.0003426594485063106}, {"id": 96, "seek": 54732, "start": 559.88, "end": 568.2,
  "text": " and 2000s where you had two search engines with two we send out two queries
  and then you brought", "tokens": [50992, 293, 8132, 82, 689, 291, 632, 732, 3164,
  12982, 365, 732, 321, 2845, 484, 732, 24109, 293, 550, 291, 3038, 51408], "temperature":
  0.0, "avg_logprob": -0.10870110470315685, "compression_ratio": 1.5956284153005464,
  "no_speech_prob": 0.0003426594485063106}, {"id": 97, "seek": 54732, "start": 568.2,
  "end": 574.2, "text": " them back and you''re like how do I merge them together
  and sometimes you do terrible things like", "tokens": [51408, 552, 646, 293, 291,
  434, 411, 577, 360, 286, 22183, 552, 1214, 293, 2171, 291, 360, 6237, 721, 411,
  51708], "temperature": 0.0, "avg_logprob": -0.10870110470315685, "compression_ratio":
  1.5956284153005464, "no_speech_prob": 0.0003426594485063106}, {"id": 98, "seek":
  57420, "start": 574.2, "end": 582.84, "text": " two lists of results right we was
  sometimes we would try to link them up together um it''s the", "tokens": [50364,
  732, 14511, 295, 3542, 558, 321, 390, 2171, 321, 576, 853, 281, 2113, 552, 493,
  1214, 1105, 309, 311, 264, 50796], "temperature": 0.0, "avg_logprob": -0.10777336718088174,
  "compression_ratio": 1.799043062200957, "no_speech_prob": 0.0002078502147924155},
  {"id": 99, "seek": 57420, "start": 582.84, "end": 588.84, "text": " same idea whether
  you''re going to one search engine you''re making a keyword search and a neural",
  "tokens": [50796, 912, 1558, 1968, 291, 434, 516, 281, 472, 3164, 2848, 291, 434,
  1455, 257, 20428, 3164, 293, 257, 18161, 51096], "temperature": 0.0, "avg_logprob":
  -0.10777336718088174, "compression_ratio": 1.799043062200957, "no_speech_prob":
  0.0002078502147924155}, {"id": 100, "seek": 57420, "start": 588.84, "end": 593.6400000000001,
  "text": " search and bring them together or two totally separate see keyword search
  engines you''re still", "tokens": [51096, 3164, 293, 1565, 552, 1214, 420, 732,
  3879, 4994, 536, 20428, 3164, 12982, 291, 434, 920, 51336], "temperature": 0.0,
  "avg_logprob": -0.10777336718088174, "compression_ratio": 1.799043062200957, "no_speech_prob":
  0.0002078502147924155}, {"id": 101, "seek": 57420, "start": 593.6400000000001, "end":
  601.24, "text": " bringing back two lists however I think at least this time around
  how to merge the lists of", "tokens": [51336, 5062, 646, 732, 14511, 4461, 286,
  519, 412, 1935, 341, 565, 926, 577, 281, 22183, 264, 14511, 295, 51716], "temperature":
  0.0, "avg_logprob": -0.10777336718088174, "compression_ratio": 1.799043062200957,
  "no_speech_prob": 0.0002078502147924155}, {"id": 102, "seek": 60124, "start": 601.24,
  "end": 608.6800000000001, "text": " results together seems to be going better than
  when we did it back in federated search right", "tokens": [50364, 3542, 1214, 2544,
  281, 312, 516, 1101, 813, 562, 321, 630, 309, 646, 294, 38024, 770, 3164, 558, 50736],
  "temperature": 0.0, "avg_logprob": -0.07979805022478104, "compression_ratio": 1.5869565217391304,
  "no_speech_prob": 0.0002062526618828997}, {"id": 103, "seek": 60124, "start": 609.4,
  "end": 614.52, "text": " uh and I look forward to talking more about like some of
  the ways that we bring hybrid you know build", "tokens": [50772, 2232, 293, 286,
  574, 2128, 281, 1417, 544, 466, 411, 512, 295, 264, 2098, 300, 321, 1565, 13051,
  291, 458, 1322, 51028], "temperature": 0.0, "avg_logprob": -0.07979805022478104,
  "compression_ratio": 1.5869565217391304, "no_speech_prob": 0.0002062526618828997},
  {"id": 104, "seek": 60124, "start": 614.52, "end": 622.36, "text": " our hybrid
  results set together um part of me really kind of wonders why ranked reciprocal
  fusion", "tokens": [51028, 527, 13051, 3542, 992, 1214, 1105, 644, 295, 385, 534,
  733, 295, 27348, 983, 20197, 46948, 23100, 51420], "temperature": 0.0, "avg_logprob":
  -0.07979805022478104, "compression_ratio": 1.5869565217391304, "no_speech_prob":
  0.0002062526618828997}, {"id": 105, "seek": 62236, "start": 623.32, "end": 631.88,
  "text": " wasn''t a thing the last time I did federated search back in the 2000s
  right like doesn''t seem like", "tokens": [50412, 2067, 380, 257, 551, 264, 1036,
  565, 286, 630, 38024, 770, 3164, 646, 294, 264, 8132, 82, 558, 411, 1177, 380, 1643,
  411, 50840], "temperature": 0.0, "avg_logprob": -0.0960174814860026, "compression_ratio":
  1.598901098901099, "no_speech_prob": 0.0015305147971957922}, {"id": 106, "seek":
  62236, "start": 631.88, "end": 638.2, "text": " that crazy of a concept why didn''t
  we do that right but we didn''t uh so I''m a little more optimistic", "tokens":
  [50840, 300, 3219, 295, 257, 3410, 983, 994, 380, 321, 360, 300, 558, 457, 321,
  994, 380, 2232, 370, 286, 478, 257, 707, 544, 19397, 51156], "temperature": 0.0,
  "avg_logprob": -0.0960174814860026, "compression_ratio": 1.598901098901099, "no_speech_prob":
  0.0015305147971957922}, {"id": 107, "seek": 62236, "start": 638.2, "end": 645.72,
  "text": " about the value of it but um it i think hybrid is a little bit of something
  old coming back", "tokens": [51156, 466, 264, 2158, 295, 309, 457, 1105, 309, 741,
  519, 13051, 307, 257, 707, 857, 295, 746, 1331, 1348, 646, 51532], "temperature":
  0.0, "avg_logprob": -0.0960174814860026, "compression_ratio": 1.598901098901099,
  "no_speech_prob": 0.0015305147971957922}, {"id": 108, "seek": 64572, "start": 645.72,
  "end": 652.9200000000001, "text": " because we''re back to the same problem I literally
  have two search engines two concepts for how to", "tokens": [50364, 570, 321, 434,
  646, 281, 264, 912, 1154, 286, 3736, 362, 732, 3164, 12982, 732, 10392, 337, 577,
  281, 50724], "temperature": 0.0, "avg_logprob": -0.08661473629086516, "compression_ratio":
  1.6008403361344539, "no_speech_prob": 0.0022914668079465628}, {"id": 109, "seek":
  64572, "start": 652.9200000000001, "end": 659.4, "text": " do information retrieval
  and yet I want to blend it into one yeah that''s exciting topic I think", "tokens":
  [50724, 360, 1589, 19817, 3337, 293, 1939, 286, 528, 281, 10628, 309, 666, 472,
  1338, 300, 311, 4670, 4829, 286, 519, 51048], "temperature": 0.0, "avg_logprob":
  -0.08661473629086516, "compression_ratio": 1.6008403361344539, "no_speech_prob":
  0.0022914668079465628}, {"id": 110, "seek": 64572, "start": 660.28, "end": 666.0400000000001,
  "text": " to me a hybrid search opens doors beyond sort of what I think Daniel just
  explained you know", "tokens": [51092, 281, 385, 257, 13051, 3164, 9870, 8077, 4399,
  1333, 295, 437, 286, 519, 8033, 445, 8825, 291, 458, 51380], "temperature": 0.0,
  "avg_logprob": -0.08661473629086516, "compression_ratio": 1.6008403361344539, "no_speech_prob":
  0.0022914668079465628}, {"id": 111, "seek": 64572, "start": 666.0400000000001, "end":
  671.88, "text": " the semantic connection between you know keywords and so on is
  where you go multi-model right", "tokens": [51380, 264, 47982, 4984, 1296, 291,
  458, 21009, 293, 370, 322, 307, 689, 291, 352, 4825, 12, 8014, 338, 558, 51672],
  "temperature": 0.0, "avg_logprob": -0.08661473629086516, "compression_ratio": 1.6008403361344539,
  "no_speech_prob": 0.0022914668079465628}, {"id": 112, "seek": 67188, "start": 671.88,
  "end": 677.24, "text": " of course you need to go there carefully probably but if
  you do miss metadata on a particular you", "tokens": [50364, 295, 1164, 291, 643,
  281, 352, 456, 7500, 1391, 457, 498, 291, 360, 1713, 26603, 322, 257, 1729, 291,
  50632], "temperature": 0.0, "avg_logprob": -0.1272990573536266, "compression_ratio":
  1.7518518518518518, "no_speech_prob": 0.0032136570662260056}, {"id": 113, "seek":
  67188, "start": 677.24, "end": 684.28, "text": " know image on the product you could
  reason about it using the image itself and maybe also video", "tokens": [50632,
  458, 3256, 322, 264, 1674, 291, 727, 1778, 466, 309, 1228, 264, 3256, 2564, 293,
  1310, 611, 960, 50984], "temperature": 0.0, "avg_logprob": -0.1272990573536266,
  "compression_ratio": 1.7518518518518518, "no_speech_prob": 0.0032136570662260056},
  {"id": 114, "seek": 67188, "start": 684.28, "end": 688.6, "text": " because we have
  video alarms as well they''re more expensive of course to run but you know", "tokens":
  [50984, 570, 321, 362, 960, 45039, 382, 731, 436, 434, 544, 5124, 295, 1164, 281,
  1190, 457, 291, 458, 51200], "temperature": 0.0, "avg_logprob": -0.1272990573536266,
  "compression_ratio": 1.7518518518518518, "no_speech_prob": 0.0032136570662260056},
  {"id": 115, "seek": 67188, "start": 688.6, "end": 694.12, "text": " sky''s the limit
  so to say if you want to go there and go um yeah so I think I think in that sense",
  "tokens": [51200, 5443, 311, 264, 4948, 370, 281, 584, 498, 291, 528, 281, 352,
  456, 293, 352, 1105, 1338, 370, 286, 519, 286, 519, 294, 300, 2020, 51476], "temperature":
  0.0, "avg_logprob": -0.1272990573536266, "compression_ratio": 1.7518518518518518,
  "no_speech_prob": 0.0032136570662260056}, {"id": 116, "seek": 67188, "start": 694.12,
  "end": 700.52, "text": " hybrid search uh unlocks many more avenues to explore including
  in e-commerce I think right", "tokens": [51476, 13051, 3164, 2232, 517, 34896, 867,
  544, 43039, 281, 6839, 3009, 294, 308, 12, 26926, 286, 519, 558, 51796], "temperature":
  0.0, "avg_logprob": -0.1272990573536266, "compression_ratio": 1.7518518518518518,
  "no_speech_prob": 0.0032136570662260056}, {"id": 117, "seek": 70052, "start": 701.48,
  "end": 710.36, "text": " yeah yeah yeah I mean I love that we are actually getting
  away from the old just straight up", "tokens": [50412, 1338, 1338, 1338, 286, 914,
  286, 959, 300, 321, 366, 767, 1242, 1314, 490, 264, 1331, 445, 2997, 493, 50856],
  "temperature": 0.0, "avg_logprob": -0.09141743838132083, "compression_ratio": 1.6785714285714286,
  "no_speech_prob": 0.003222076455131173}, {"id": 118, "seek": 70052, "start": 710.36,
  "end": 716.36, "text": " bag of words that was keyword that served us for a long
  time but still was just a very rough", "tokens": [50856, 3411, 295, 2283, 300, 390,
  20428, 300, 7584, 505, 337, 257, 938, 565, 457, 920, 390, 445, 257, 588, 5903, 51156],
  "temperature": 0.0, "avg_logprob": -0.09141743838132083, "compression_ratio": 1.6785714285714286,
  "no_speech_prob": 0.003222076455131173}, {"id": 119, "seek": 70052, "start": 716.36,
  "end": 723.56, "text": " approximation of what people want right I mean BM25 you
  know people say it''s not even the best", "tokens": [51156, 28023, 295, 437, 561,
  528, 558, 286, 914, 15901, 6074, 291, 458, 561, 584, 309, 311, 406, 754, 264, 1151,
  51516], "temperature": 0.0, "avg_logprob": -0.09141743838132083, "compression_ratio":
  1.6785714285714286, "no_speech_prob": 0.003222076455131173}, {"id": 120, "seek":
  70052, "start": 723.56, "end": 729.72, "text": " algorithm it''s just as fast as
  the one that we use uh vectors is sort of this idea of there are", "tokens": [51516,
  9284, 309, 311, 445, 382, 2370, 382, 264, 472, 300, 321, 764, 2232, 18875, 307,
  1333, 295, 341, 1558, 295, 456, 366, 51824], "temperature": 0.0, "avg_logprob":
  -0.09141743838132083, "compression_ratio": 1.6785714285714286, "no_speech_prob":
  0.003222076455131173}, {"id": 121, "seek": 72972, "start": 729.72, "end": 736.6,
  "text": " richer ways of understanding user queries and the content tech and just
  going beyond taxes the", "tokens": [50364, 29021, 2098, 295, 3701, 4195, 24109,
  293, 264, 2701, 7553, 293, 445, 516, 4399, 10041, 264, 50708], "temperature": 0.0,
  "avg_logprob": -0.12392632527784868, "compression_ratio": 1.696969696969697, "no_speech_prob":
  0.0008326139068230987}, {"id": 122, "seek": 72972, "start": 736.6, "end": 741.96,
  "text": " you know it''s absolutely wonderful right lots of different things I mean
  some point we''ll do a vector", "tokens": [50708, 291, 458, 309, 311, 3122, 3715,
  558, 3195, 295, 819, 721, 286, 914, 512, 935, 321, 603, 360, 257, 8062, 50976],
  "temperature": 0.0, "avg_logprob": -0.12392632527784868, "compression_ratio": 1.696969696969697,
  "no_speech_prob": 0.0008326139068230987}, {"id": 123, "seek": 72972, "start": 741.96,
  "end": 751.24, "text": " search on usage patterns right to figure stuff out right
  like it''ll be the the mode will be activity", "tokens": [50976, 3164, 322, 14924,
  8294, 558, 281, 2573, 1507, 484, 558, 411, 309, 603, 312, 264, 264, 4391, 486, 312,
  5191, 51440], "temperature": 0.0, "avg_logprob": -0.12392632527784868, "compression_ratio":
  1.696969696969697, "no_speech_prob": 0.0008326139068230987}, {"id": 124, "seek":
  72972, "start": 751.24, "end": 756.6, "text": " won''t be video or image or something
  it''ll be activity you''d be like oh yeah that''s the person", "tokens": [51440,
  1582, 380, 312, 960, 420, 3256, 420, 746, 309, 603, 312, 5191, 291, 1116, 312, 411,
  1954, 1338, 300, 311, 264, 954, 51708], "temperature": 0.0, "avg_logprob": -0.12392632527784868,
  "compression_ratio": 1.696969696969697, "no_speech_prob": 0.0008326139068230987},
  {"id": 125, "seek": 75660, "start": 756.6, "end": 763.32, "text": " I want to talk
  to they have the same activities as me based on whatever it is that they do right",
  "tokens": [50364, 286, 528, 281, 751, 281, 436, 362, 264, 912, 5354, 382, 385, 2361,
  322, 2035, 309, 307, 300, 436, 360, 558, 50700], "temperature": 0.0, "avg_logprob":
  -0.056114905122397606, "compression_ratio": 1.6277777777777778, "no_speech_prob":
  0.000335940218064934}, {"id": 126, "seek": 75660, "start": 763.32, "end": 771.64,
  "text": " so but those kinds of things definitely are expressed through the vectors
  um I do think that hybrid", "tokens": [50700, 370, 457, 729, 3685, 295, 721, 2138,
  366, 12675, 807, 264, 18875, 1105, 286, 360, 519, 300, 13051, 51116], "temperature":
  0.0, "avg_logprob": -0.056114905122397606, "compression_ratio": 1.6277777777777778,
  "no_speech_prob": 0.000335940218064934}, {"id": 127, "seek": 75660, "start": 771.64,
  "end": 780.2, "text": " is an amazing thing for right now for the next few years
  uh I do think though it''s also a little", "tokens": [51116, 307, 364, 2243, 551,
  337, 558, 586, 337, 264, 958, 1326, 924, 2232, 286, 360, 519, 1673, 309, 311, 611,
  257, 707, 51544], "temperature": 0.0, "avg_logprob": -0.056114905122397606, "compression_ratio":
  1.6277777777777778, "no_speech_prob": 0.000335940218064934}, {"id": 128, "seek":
  78020, "start": 780.2, "end": 789.1600000000001, "text": " bit of a bandaid in the
  sense that we''re still leaning on keyword search for you know various", "tokens":
  [50364, 857, 295, 257, 4116, 17810, 294, 264, 2020, 300, 321, 434, 920, 23390, 322,
  20428, 3164, 337, 291, 458, 3683, 50812], "temperature": 0.0, "avg_logprob": -0.08040446501511794,
  "compression_ratio": 1.5454545454545454, "no_speech_prob": 0.002656811149790883},
  {"id": 129, "seek": 78020, "start": 789.1600000000001, "end": 797.48, "text": "
  use cases and if we were to look 10 years out I think an ideal solution is that
  we''re not doing", "tokens": [50812, 764, 3331, 293, 498, 321, 645, 281, 574, 1266,
  924, 484, 286, 519, 364, 7157, 3827, 307, 300, 321, 434, 406, 884, 51228], "temperature":
  0.0, "avg_logprob": -0.08040446501511794, "compression_ratio": 1.5454545454545454,
  "no_speech_prob": 0.002656811149790883}, {"id": 130, "seek": 78020, "start": 797.48,
  "end": 804.76, "text": " hybrid anymore just have a better approach to search something
  beyond vector plus keyword something", "tokens": [51228, 13051, 3602, 445, 362,
  257, 1101, 3109, 281, 3164, 746, 4399, 8062, 1804, 20428, 746, 51592], "temperature":
  0.0, "avg_logprob": -0.08040446501511794, "compression_ratio": 1.5454545454545454,
  "no_speech_prob": 0.002656811149790883}, {"id": 131, "seek": 80476, "start": 804.76,
  "end": 811.3199999999999, "text": " better that still supports the zero results
  is the right answer you know some of these problems", "tokens": [50364, 1101, 300,
  920, 9346, 264, 4018, 3542, 307, 264, 558, 1867, 291, 458, 512, 295, 613, 2740,
  50692], "temperature": 0.0, "avg_logprob": -0.15298568118702283, "compression_ratio":
  1.7025862068965518, "no_speech_prob": 0.015728961676359177}, {"id": 132, "seek":
  80476, "start": 811.3199999999999, "end": 819.08, "text": " that vector using vectors
  gives us right we would have better better approach and not this slightly", "tokens":
  [50692, 300, 8062, 1228, 18875, 2709, 505, 558, 321, 576, 362, 1101, 1101, 3109,
  293, 406, 341, 4748, 51080], "temperature": 0.0, "avg_logprob": -0.15298568118702283,
  "compression_ratio": 1.7025862068965518, "no_speech_prob": 0.015728961676359177},
  {"id": 133, "seek": 80476, "start": 819.08, "end": 825.4, "text": " band-aid I have
  two different ways of searching and then have to wedge them back together yeah I
  like", "tokens": [51080, 4116, 12, 64, 327, 286, 362, 732, 819, 2098, 295, 10808,
  293, 550, 362, 281, 34530, 552, 646, 1214, 1338, 286, 411, 51396], "temperature":
  0.0, "avg_logprob": -0.15298568118702283, "compression_ratio": 1.7025862068965518,
  "no_speech_prob": 0.015728961676359177}, {"id": 134, "seek": 80476, "start": 825.4,
  "end": 830.84, "text": " for now hybrid''s exciting yeah I like that I like where
  you''re going I wanted to also I wonder if", "tokens": [51396, 337, 586, 13051,
  311, 4670, 1338, 286, 411, 300, 286, 411, 689, 291, 434, 516, 286, 1415, 281, 611,
  286, 2441, 498, 51668], "temperature": 0.0, "avg_logprob": -0.15298568118702283,
  "compression_ratio": 1.7025862068965518, "no_speech_prob": 0.015728961676359177},
  {"id": 135, "seek": 83084, "start": 830.84, "end": 839.48, "text": " you saw that
  blog by Dr. Enbal I will make sure to link it where he talks about uh rrf you know",
  "tokens": [50364, 291, 1866, 300, 6968, 538, 2491, 13, 2193, 2645, 286, 486, 652,
  988, 281, 2113, 309, 689, 415, 6686, 466, 2232, 367, 81, 69, 291, 458, 50796], "temperature":
  0.0, "avg_logprob": -0.1799412688163862, "compression_ratio": 1.4973821989528795,
  "no_speech_prob": 0.00138946867082268}, {"id": 136, "seek": 83084, "start": 839.48,
  "end": 848.2, "text": " reciprocal rank fusion and he shows on a like handcrafted
  example that uh you know if let''s say", "tokens": [50796, 46948, 6181, 23100, 293,
  415, 3110, 322, 257, 411, 1011, 5611, 292, 1365, 300, 2232, 291, 458, 498, 718,
  311, 584, 51232], "temperature": 0.0, "avg_logprob": -0.1799412688163862, "compression_ratio":
  1.4973821989528795, "no_speech_prob": 0.00138946867082268}, {"id": 137, "seek":
  83084, "start": 848.9200000000001, "end": 856.6800000000001, "text": " neural search
  brings relevant result to the top of few results keyword lacks and doesn''t so it",
  "tokens": [51268, 18161, 3164, 5607, 7340, 1874, 281, 264, 1192, 295, 1326, 3542,
  20428, 31132, 293, 1177, 380, 370, 309, 51656], "temperature": 0.0, "avg_logprob":
  -0.1799412688163862, "compression_ratio": 1.4973821989528795, "no_speech_prob":
  0.00138946867082268}, {"id": 138, "seek": 85668, "start": 856.68, "end": 862.52,
  "text": " basically brings noise when you combine the two you will end up having
  kind of half noise half", "tokens": [50364, 1936, 5607, 5658, 562, 291, 10432, 264,
  732, 291, 486, 917, 493, 1419, 733, 295, 1922, 5658, 1922, 50656], "temperature":
  0.0, "avg_logprob": -0.19746763627607744, "compression_ratio": 1.8396226415094339,
  "no_speech_prob": 0.006937813945114613}, {"id": 139, "seek": 85668, "start": 862.52,
  "end": 868.8399999999999, "text": " signal and it will look terrible it will look
  terrible right and where do you stand on this like", "tokens": [50656, 6358, 293,
  309, 486, 574, 6237, 309, 486, 574, 6237, 558, 293, 689, 360, 291, 1463, 322, 341,
  411, 50972], "temperature": 0.0, "avg_logprob": -0.19746763627607744, "compression_ratio":
  1.8396226415094339, "no_speech_prob": 0.006937813945114613}, {"id": 140, "seek":
  85668, "start": 870.12, "end": 878.3599999999999, "text": " only there was a way
  yeah yeah it''s only there was a way of at our understand not just blindly yeah",
  "tokens": [51036, 787, 456, 390, 257, 636, 1338, 1338, 309, 311, 787, 456, 390,
  257, 636, 295, 412, 527, 1223, 406, 445, 47744, 1338, 51448], "temperature": 0.0,
  "avg_logprob": -0.19746763627607744, "compression_ratio": 1.8396226415094339, "no_speech_prob":
  0.006937813945114613}, {"id": 141, "seek": 85668, "start": 878.92, "end": 884.92,
  "text": " you know blindly matching things um and I''ll hand it over to Daniel and
  just a moment I do want to", "tokens": [51476, 291, 458, 47744, 14324, 721, 1105,
  293, 286, 603, 1011, 309, 670, 281, 8033, 293, 445, 257, 1623, 286, 360, 528, 281,
  51776], "temperature": 0.0, "avg_logprob": -0.19746763627607744, "compression_ratio":
  1.8396226415094339, "no_speech_prob": 0.006937813945114613}, {"id": 142, "seek":
  88492, "start": 884.92, "end": 891.4, "text": " call that I really liked uh your
  previous episode with all a Sandra where uh I can''t remember", "tokens": [50364,
  818, 300, 286, 534, 4501, 2232, 428, 3894, 3500, 365, 439, 257, 28184, 689, 2232,
  286, 393, 380, 1604, 50688], "temperature": 0.0, "avg_logprob": -0.14683284542777322,
  "compression_ratio": 1.670995670995671, "no_speech_prob": 0.0005746468668803573},
  {"id": 143, "seek": 88492, "start": 891.4, "end": 896.68, "text": " was you were
  all a Sandra but you kind of I think it was you Demetri said yeah that your engineers",
  "tokens": [50688, 390, 291, 645, 439, 257, 28184, 457, 291, 733, 295, 286, 519,
  309, 390, 291, 4686, 302, 470, 848, 1338, 300, 428, 11955, 50952], "temperature":
  0.0, "avg_logprob": -0.14683284542777322, "compression_ratio": 1.670995670995671,
  "no_speech_prob": 0.0005746468668803573}, {"id": 144, "seek": 88492, "start": 896.68,
  "end": 902.1999999999999, "text": " were looking at hybrid search and they kind
  of looked at it and said when you strip away the fancy", "tokens": [50952, 645,
  1237, 412, 13051, 3164, 293, 436, 733, 295, 2956, 412, 309, 293, 848, 562, 291,
  12828, 1314, 264, 10247, 51228], "temperature": 0.0, "avg_logprob": -0.14683284542777322,
  "compression_ratio": 1.670995670995671, "no_speech_prob": 0.0005746468668803573},
  {"id": 145, "seek": 88492, "start": 902.1999999999999, "end": 909.9599999999999,
  "text": " words like ranked reciprocal fusion for blending things together you''re
  like that''s just round", "tokens": [51228, 2283, 411, 20197, 46948, 23100, 337,
  23124, 721, 1214, 291, 434, 411, 300, 311, 445, 3098, 51616], "temperature": 0.0,
  "avg_logprob": -0.14683284542777322, "compression_ratio": 1.670995670995671, "no_speech_prob":
  0.0005746468668803573}, {"id": 146, "seek": 90996, "start": 909.96, "end": 918.76,
  "text": " Robin right and you know round robin is not necessarily a round blind
  and it''s blind round", "tokens": [50364, 16533, 558, 293, 291, 458, 3098, 3870,
  259, 307, 406, 4725, 257, 3098, 6865, 293, 309, 311, 6865, 3098, 50804], "temperature":
  0.0, "avg_logprob": -0.12723348428914835, "compression_ratio": 1.8398058252427185,
  "no_speech_prob": 0.00046124018263071775}, {"id": 147, "seek": 90996, "start": 918.76,
  "end": 925.64, "text": " Robin right it''s not round robin in in your middle school
  when you had to pick teams for dodgeball", "tokens": [50804, 16533, 558, 309, 311,
  406, 3098, 3870, 259, 294, 294, 428, 2808, 1395, 562, 291, 632, 281, 1888, 5491,
  337, 27238, 3129, 51148], "temperature": 0.0, "avg_logprob": -0.12723348428914835,
  "compression_ratio": 1.8398058252427185, "no_speech_prob": 0.00046124018263071775},
  {"id": 148, "seek": 90996, "start": 926.6, "end": 932.76, "text": " right the people
  picking knew who the best players were so at least you were at least divvying",
  "tokens": [51196, 558, 264, 561, 8867, 2586, 567, 264, 1151, 4150, 645, 370, 412,
  1935, 291, 645, 412, 1935, 3414, 85, 1840, 51504], "temperature": 0.0, "avg_logprob":
  -0.12723348428914835, "compression_ratio": 1.8398058252427185, "no_speech_prob":
  0.00046124018263071775}, {"id": 149, "seek": 90996, "start": 932.76, "end": 939.08,
  "text": " the best choices and at the very end those last two kids you know you
  knew they were the worst", "tokens": [51504, 264, 1151, 7994, 293, 412, 264, 588,
  917, 729, 1036, 732, 2301, 291, 458, 291, 2586, 436, 645, 264, 5855, 51820], "temperature":
  0.0, "avg_logprob": -0.12723348428914835, "compression_ratio": 1.8398058252427185,
  "no_speech_prob": 0.00046124018263071775}, {"id": 150, "seek": 93908, "start": 939.08,
  "end": 945.32, "text": " choices they were the noise in the search results right
  but you were that round robin at least had", "tokens": [50364, 7994, 436, 645, 264,
  5658, 294, 264, 3164, 3542, 558, 457, 291, 645, 300, 3098, 3870, 259, 412, 1935,
  632, 50676], "temperature": 0.0, "avg_logprob": -0.11290172088977903, "compression_ratio":
  1.798165137614679, "no_speech_prob": 0.00011593567614909261}, {"id": 151, "seek":
  93908, "start": 945.32, "end": 953.1600000000001, "text": " the benefit of knowing
  what was good ranked refresh ranked reciprocal fusion has no sense of whether",
  "tokens": [50676, 264, 5121, 295, 5276, 437, 390, 665, 20197, 15134, 20197, 46948,
  23100, 575, 572, 2020, 295, 1968, 51068], "temperature": 0.0, "avg_logprob": -0.11290172088977903,
  "compression_ratio": 1.798165137614679, "no_speech_prob": 0.00011593567614909261},
  {"id": 152, "seek": 93908, "start": 953.1600000000001, "end": 960.2, "text": " the
  those results are good or bad right it is literally blindly picking them in some
  order with no", "tokens": [51068, 264, 729, 3542, 366, 665, 420, 1578, 558, 309,
  307, 3736, 47744, 8867, 552, 294, 512, 1668, 365, 572, 51420], "temperature": 0.0,
  "avg_logprob": -0.11290172088977903, "compression_ratio": 1.798165137614679, "no_speech_prob":
  0.00011593567614909261}, {"id": 153, "seek": 93908, "start": 960.2, "end": 966.2,
  "text": " sense of uh of what that is and as you can imagine blindly picking is
  going to leave lead you", "tokens": [51420, 2020, 295, 2232, 295, 437, 300, 307,
  293, 382, 291, 393, 3811, 47744, 8867, 307, 516, 281, 1856, 1477, 291, 51720], "temperature":
  0.0, "avg_logprob": -0.11290172088977903, "compression_ratio": 1.798165137614679,
  "no_speech_prob": 0.00011593567614909261}, {"id": 154, "seek": 96620, "start": 966.2,
  "end": 973.5600000000001, "text": " be pinched potentially a very weak dodgeball
  team right and yet that''s what we think of a state of the", "tokens": [50364, 312,
  14614, 292, 7263, 257, 588, 5336, 27238, 3129, 1469, 558, 293, 1939, 300, 311, 437,
  321, 519, 295, 257, 1785, 295, 264, 50732], "temperature": 0.0, "avg_logprob": -0.1573984252081977,
  "compression_ratio": 1.6853448275862069, "no_speech_prob": 0.0013409038074314594},
  {"id": 155, "seek": 96620, "start": 973.5600000000001, "end": 980.5200000000001,
  "text": " art yeah so Daniel what should we do in this case is there any solution
  it''s it''s a good segue", "tokens": [50732, 1523, 1338, 370, 8033, 437, 820, 321,
  360, 294, 341, 1389, 307, 456, 604, 3827, 309, 311, 309, 311, 257, 665, 33850, 51080],
  "temperature": 0.0, "avg_logprob": -0.1573984252081977, "compression_ratio": 1.6853448275862069,
  "no_speech_prob": 0.0013409038074314594}, {"id": 156, "seek": 96620, "start": 980.5200000000001,
  "end": 988.12, "text": " into what we actually tried and explored and experimented
  with um so in our most recent work we", "tokens": [51080, 666, 437, 321, 767, 3031,
  293, 24016, 293, 5120, 292, 365, 1105, 370, 294, 527, 881, 5162, 589, 321, 51460],
  "temperature": 0.0, "avg_logprob": -0.1573984252081977, "compression_ratio": 1.6853448275862069,
  "no_speech_prob": 0.0013409038074314594}, {"id": 157, "seek": 96620, "start": 988.84,
  "end": 994.84, "text": " tried to come up with a systematic approach to optimize
  hybrid search specifically in open search", "tokens": [51496, 3031, 281, 808, 493,
  365, 257, 27249, 3109, 281, 19719, 13051, 3164, 4682, 294, 1269, 3164, 51796], "temperature":
  0.0, "avg_logprob": -0.1573984252081977, "compression_ratio": 1.6853448275862069,
  "no_speech_prob": 0.0013409038074314594}, {"id": 158, "seek": 99484, "start": 995.24,
  "end": 1005.8000000000001, "text": " um so in open search actually right now you
  have linear combination techniques at hand so that", "tokens": [50384, 1105, 370,
  294, 1269, 3164, 767, 558, 586, 291, 362, 8213, 6562, 7512, 412, 1011, 370, 300,
  50912], "temperature": 0.0, "avg_logprob": -0.15689779500492285, "compression_ratio":
  1.6932515337423313, "no_speech_prob": 0.0004383990599308163}, {"id": 159, "seek":
  99484, "start": 1005.8000000000001, "end": 1011.5600000000001, "text": " means you
  have two normalization techniques you can choose one the L2 norm the min max norm",
  "tokens": [50912, 1355, 291, 362, 732, 2710, 2144, 7512, 291, 393, 2826, 472, 264,
  441, 17, 2026, 264, 923, 11469, 2026, 51200], "temperature": 0.0, "avg_logprob":
  -0.15689779500492285, "compression_ratio": 1.6932515337423313, "no_speech_prob":
  0.0004383990599308163}, {"id": 160, "seek": 99484, "start": 1011.5600000000001,
  "end": 1018.0400000000001, "text": " um they are basically both there so that you
  can normalize the scores from keyword search", "tokens": [51200, 1105, 436, 366,
  1936, 1293, 456, 370, 300, 291, 393, 2710, 1125, 264, 13444, 490, 20428, 3164, 51524],
  "temperature": 0.0, "avg_logprob": -0.15689779500492285, "compression_ratio": 1.6932515337423313,
  "no_speech_prob": 0.0004383990599308163}, {"id": 161, "seek": 101804, "start": 1018.92,
  "end": 1026.28, "text": " into the let''s say space of vector search so that you
  can compare apples to apples more or less", "tokens": [50408, 666, 264, 718, 311,
  584, 1901, 295, 8062, 3164, 370, 300, 291, 393, 6794, 16814, 281, 16814, 544, 420,
  1570, 50776], "temperature": 0.0, "avg_logprob": -0.15317499464836673, "compression_ratio":
  1.60989010989011, "no_speech_prob": 0.0031713047064840794}, {"id": 162, "seek":
  101804, "start": 1026.28, "end": 1034.44, "text": " here and not apples to oranges
  because as we all know vm25 scores especially if you have if you have", "tokens":
  [50776, 510, 293, 406, 16814, 281, 35474, 570, 382, 321, 439, 458, 371, 76, 6074,
  13444, 2318, 498, 291, 362, 498, 291, 362, 51184], "temperature": 0.0, "avg_logprob":
  -0.15317499464836673, "compression_ratio": 1.60989010989011, "no_speech_prob": 0.0031713047064840794},
  {"id": 163, "seek": 101804, "start": 1034.44, "end": 1042.12, "text": " like wired
  field weights they are unbounded they can be in the dozens the hundreds the thousands",
  "tokens": [51184, 411, 27415, 2519, 17443, 436, 366, 517, 18767, 292, 436, 393,
  312, 294, 264, 18431, 264, 6779, 264, 5383, 51568], "temperature": 0.0, "avg_logprob":
  -0.15317499464836673, "compression_ratio": 1.60989010989011, "no_speech_prob": 0.0031713047064840794},
  {"id": 164, "seek": 104212, "start": 1042.12, "end": 1049.4799999999998, "text":
  " so you don''t really know upfront in what range you are operating and also you
  can''t really compare", "tokens": [50364, 370, 291, 500, 380, 534, 458, 30264, 294,
  437, 3613, 291, 366, 7447, 293, 611, 291, 393, 380, 534, 6794, 50732], "temperature":
  0.0, "avg_logprob": -0.11347551814845351, "compression_ratio": 1.64, "no_speech_prob":
  0.00010527812264626846}, {"id": 165, "seek": 104212, "start": 1049.4799999999998,
  "end": 1055.6399999999999, "text": " the scores from one query to another query
  so that makes it really difficult to combine keyword", "tokens": [50732, 264, 13444,
  490, 472, 14581, 281, 1071, 14581, 370, 300, 1669, 309, 534, 2252, 281, 10432, 20428,
  51040], "temperature": 0.0, "avg_logprob": -0.11347551814845351, "compression_ratio":
  1.64, "no_speech_prob": 0.00010527812264626846}, {"id": 166, "seek": 104212, "start":
  1056.6799999999998, "end": 1065.8, "text": " search scores with any other um let''s
  say search mechanism together with these normalization", "tokens": [51092, 3164,
  13444, 365, 604, 661, 1105, 718, 311, 584, 3164, 7513, 1214, 365, 613, 2710, 2144,
  51548], "temperature": 0.0, "avg_logprob": -0.11347551814845351, "compression_ratio":
  1.64, "no_speech_prob": 0.00010527812264626846}, {"id": 167, "seek": 106580, "start":
  1065.8799999999999, "end": 1072.84, "text": " techniques the L2 norm them in max
  norm you have three combination techniques at hand and that''s", "tokens": [50368,
  7512, 264, 441, 17, 2026, 552, 294, 11469, 2026, 291, 362, 1045, 6562, 7512, 412,
  1011, 293, 300, 311, 50716], "temperature": 0.0, "avg_logprob": -0.16189916928609213,
  "compression_ratio": 1.8293838862559242, "no_speech_prob": 0.0012069582007825375},
  {"id": 168, "seek": 106580, "start": 1072.84, "end": 1078.68, "text": " basically
  just three different means you can apply the arithmetic mean the harmonic mean and
  the", "tokens": [50716, 1936, 445, 1045, 819, 1355, 291, 393, 3079, 264, 42973,
  914, 264, 32270, 914, 293, 264, 51008], "temperature": 0.0, "avg_logprob": -0.16189916928609213,
  "compression_ratio": 1.8293838862559242, "no_speech_prob": 0.0012069582007825375},
  {"id": 169, "seek": 106580, "start": 1078.68, "end": 1086.36, "text": " geometric
  mean so that leaves you with two by three so that''s already six parameter combinations",
  "tokens": [51008, 33246, 914, 370, 300, 5510, 291, 365, 732, 538, 1045, 370, 300,
  311, 1217, 2309, 13075, 21267, 51392], "temperature": 0.0, "avg_logprob": -0.16189916928609213,
  "compression_ratio": 1.8293838862559242, "no_speech_prob": 0.0012069582007825375},
  {"id": 170, "seek": 106580, "start": 1086.36, "end": 1094.9199999999998, "text":
  " that you can try on and then you can define weights um so how um how much neurosurge
  weight how", "tokens": [51392, 300, 291, 393, 853, 322, 293, 550, 291, 393, 6964,
  17443, 1105, 370, 577, 1105, 577, 709, 28813, 374, 432, 3364, 577, 51820], "temperature":
  0.0, "avg_logprob": -0.16189916928609213, "compression_ratio": 1.8293838862559242,
  "no_speech_prob": 0.0012069582007825375}, {"id": 171, "seek": 109492, "start": 1094.92,
  "end": 1101.4, "text": " much keyword search weight do i want to have in my query
  they always add up to one so you can say", "tokens": [50364, 709, 20428, 3164, 3364,
  360, 741, 528, 281, 362, 294, 452, 14581, 436, 1009, 909, 493, 281, 472, 370, 291,
  393, 584, 50688], "temperature": 0.0, "avg_logprob": -0.1726050059000651, "compression_ratio":
  1.5217391304347827, "no_speech_prob": 0.000397005642298609}, {"id": 172, "seek":
  109492, "start": 1101.4, "end": 1110.2, "text": " I want to go with 10% keyword
  90% neural or 50-50 um thinking of let''s say 11 of these", "tokens": [50688, 286,
  528, 281, 352, 365, 1266, 4, 20428, 4289, 4, 18161, 420, 2625, 12, 2803, 1105, 1953,
  295, 718, 311, 584, 2975, 295, 613, 51128], "temperature": 0.0, "avg_logprob": -0.1726050059000651,
  "compression_ratio": 1.5217391304347827, "no_speech_prob": 0.000397005642298609},
  {"id": 173, "seek": 109492, "start": 1111.16, "end": 1118.3600000000001, "text":
  " weights so maybe you start with zero keyword and a hundred percent neural and
  10% 90% and so on", "tokens": [51176, 17443, 370, 1310, 291, 722, 365, 4018, 20428,
  293, 257, 3262, 3043, 18161, 293, 1266, 4, 4289, 4, 293, 370, 322, 51536], "temperature":
  0.0, "avg_logprob": -0.1726050059000651, "compression_ratio": 1.5217391304347827,
  "no_speech_prob": 0.000397005642298609}, {"id": 174, "seek": 111836, "start": 1118.4399999999998,
  "end": 1127.08, "text": " and so forth so that gives you a range of 11 multiplied
  with the six parameter combinations", "tokens": [50368, 293, 370, 5220, 370, 300,
  2709, 291, 257, 3613, 295, 2975, 17207, 365, 264, 2309, 13075, 21267, 50800], "temperature":
  0.0, "avg_logprob": -0.12123590502245672, "compression_ratio": 1.5737704918032787,
  "no_speech_prob": 0.00017715782450977713}, {"id": 175, "seek": 111836, "start":
  1127.08, "end": 1137.6399999999999, "text": " that we already had gives us let''s
  say a solution area to explore of 66 different combinations", "tokens": [50800,
  300, 321, 1217, 632, 2709, 505, 718, 311, 584, 257, 3827, 1859, 281, 6839, 295,
  21126, 819, 21267, 51328], "temperature": 0.0, "avg_logprob": -0.12123590502245672,
  "compression_ratio": 1.5737704918032787, "no_speech_prob": 0.00017715782450977713},
  {"id": 176, "seek": 111836, "start": 1137.6399999999999, "end": 1146.52, "text":
  " which is pretty manageable so we defined optimizing hybrid search as a parameter
  optimization problem", "tokens": [51328, 597, 307, 1238, 38798, 370, 321, 7642,
  40425, 13051, 3164, 382, 257, 13075, 19618, 1154, 51772], "temperature": 0.0, "avg_logprob":
  -0.12123590502245672, "compression_ratio": 1.5737704918032787, "no_speech_prob":
  0.00017715782450977713}, {"id": 177, "seek": 114652, "start": 1147.16, "end": 1152.52,
  "text": " and we picked the most straightforward approach that you can pick and
  we just tried out all", "tokens": [50396, 293, 321, 6183, 264, 881, 15325, 3109,
  300, 291, 393, 1888, 293, 321, 445, 3031, 484, 439, 50664], "temperature": 0.0,
  "avg_logprob": -0.1616206623259045, "compression_ratio": 1.6437768240343347, "no_speech_prob":
  0.001243914826773107}, {"id": 178, "seek": 114652, "start": 1152.52, "end": 1160.6,
  "text": " different combinations and calculated search metrics based on judgments
  and then we just had a", "tokens": [50664, 819, 21267, 293, 15598, 3164, 16367,
  2361, 322, 40337, 293, 550, 321, 445, 632, 257, 51068], "temperature": 0.0, "avg_logprob":
  -0.1616206623259045, "compression_ratio": 1.6437768240343347, "no_speech_prob":
  0.001243914826773107}, {"id": 179, "seek": 114652, "start": 1160.6, "end": 1168.36,
  "text": " look at which one is the best combination um for our experiments we used
  the ESCI data set um so", "tokens": [51068, 574, 412, 597, 472, 307, 264, 1151,
  6562, 1105, 337, 527, 12050, 321, 1143, 264, 12564, 25240, 1412, 992, 1105, 370,
  51456], "temperature": 0.0, "avg_logprob": -0.1616206623259045, "compression_ratio":
  1.6437768240343347, "no_speech_prob": 0.001243914826773107}, {"id": 180, "seek":
  114652, "start": 1168.36, "end": 1175.72, "text": " that was released by amazon
  a couple of i think 18 months ago or something like that as part of our", "tokens":
  [51456, 300, 390, 4736, 538, 47010, 257, 1916, 295, 741, 519, 2443, 2493, 2057,
  420, 746, 411, 300, 382, 644, 295, 527, 51824], "temperature": 0.0, "avg_logprob":
  -0.1616206623259045, "compression_ratio": 1.6437768240343347, "no_speech_prob":
  0.001243914826773107}, {"id": 181, "seek": 117572, "start": 1175.72, "end": 1182.68,
  "text": " taglet competition um this data set comes with queries comes with products
  and most importantly", "tokens": [50364, 6162, 2631, 6211, 1105, 341, 1412, 992,
  1487, 365, 24109, 1487, 365, 3383, 293, 881, 8906, 50712], "temperature": 0.0, "avg_logprob":
  -0.1821271260579427, "compression_ratio": 1.7725118483412323, "no_speech_prob":
  0.0002748727274592966}, {"id": 182, "seek": 117572, "start": 1182.68, "end": 1190.6000000000001,
  "text": " it comes with judgments so we basically have everything that we need to
  really try out different", "tokens": [50712, 309, 1487, 365, 40337, 370, 321, 1936,
  362, 1203, 300, 321, 643, 281, 534, 853, 484, 819, 51108], "temperature": 0.0, "avg_logprob":
  -0.1821271260579427, "compression_ratio": 1.7725118483412323, "no_speech_prob":
  0.0002748727274592966}, {"id": 183, "seek": 117572, "start": 1190.6000000000001,
  "end": 1196.6000000000001, "text": " um parameter combinations see how they work
  what results are retrieved um can calculate a couple", "tokens": [51108, 1105, 13075,
  21267, 536, 577, 436, 589, 437, 3542, 366, 19817, 937, 1105, 393, 8873, 257, 1916,
  51408], "temperature": 0.0, "avg_logprob": -0.1821271260579427, "compression_ratio":
  1.7725118483412323, "no_speech_prob": 0.0002748727274592966}, {"id": 184, "seek":
  117572, "start": 1196.6000000000001, "end": 1202.3600000000001, "text": " of metrics
  compare these and then see which one is the best um parameter combination", "tokens":
  [51408, 295, 16367, 6794, 613, 293, 550, 536, 597, 472, 307, 264, 1151, 1105, 13075,
  6562, 51696], "temperature": 0.0, "avg_logprob": -0.1821271260579427, "compression_ratio":
  1.7725118483412323, "no_speech_prob": 0.0002748727274592966}, {"id": 185, "seek":
  120236, "start": 1203.1599999999999, "end": 1211.1599999999999, "text": " and um
  that''s what we call the global hybrid search optimizer so we try to identify the
  best", "tokens": [50404, 293, 1105, 300, 311, 437, 321, 818, 264, 4338, 13051, 3164,
  5028, 6545, 370, 321, 853, 281, 5876, 264, 1151, 50804], "temperature": 0.0, "avg_logprob":
  -0.08685370742297563, "compression_ratio": 1.5909090909090908, "no_speech_prob":
  0.0012637972831726074}, {"id": 186, "seek": 120236, "start": 1211.1599999999999,
  "end": 1218.28, "text": " parameter combination globally for all the queries that
  we are looking at in a certain defined", "tokens": [50804, 13075, 6562, 18958, 337,
  439, 264, 24109, 300, 321, 366, 1237, 412, 294, 257, 1629, 7642, 51160], "temperature":
  0.0, "avg_logprob": -0.08685370742297563, "compression_ratio": 1.5909090909090908,
  "no_speech_prob": 0.0012637972831726074}, {"id": 187, "seek": 120236, "start": 1219.08,
  "end": 1226.04, "text": " subset of queries so that''s kind of the first step um
  the very very straightforward approach", "tokens": [51200, 25993, 295, 24109, 370,
  300, 311, 733, 295, 264, 700, 1823, 1105, 264, 588, 588, 15325, 3109, 51548], "temperature":
  0.0, "avg_logprob": -0.08685370742297563, "compression_ratio": 1.5909090909090908,
  "no_speech_prob": 0.0012637972831726074}, {"id": 188, "seek": 122604, "start": 1226.2,
  "end": 1232.28, "text": " that we applied that''s not really something um let''s
  say scientifically um so first decated", "tokens": [50372, 300, 321, 6456, 300,
  311, 406, 534, 746, 1105, 718, 311, 584, 39719, 1105, 370, 700, 979, 770, 50676],
  "temperature": 0.0, "avg_logprob": -0.22167723855854551, "compression_ratio": 1.696035242290749,
  "no_speech_prob": 0.0014247347135096788}, {"id": 189, "seek": 122604, "start": 1232.28,
  "end": 1240.36, "text": " there was just a very brute force approach to see um what''s
  in there also learn how results may be", "tokens": [50676, 456, 390, 445, 257, 588,
  47909, 3464, 3109, 281, 536, 1105, 437, 311, 294, 456, 611, 1466, 577, 3542, 815,
  312, 51080], "temperature": 0.0, "avg_logprob": -0.22167723855854551, "compression_ratio":
  1.696035242290749, "no_speech_prob": 0.0014247347135096788}, {"id": 190, "seek":
  122604, "start": 1241.32, "end": 1248.12, "text": " shaped or turn out differently
  when we increase neural search weight or increase the keyword search", "tokens":
  [51128, 13475, 420, 1261, 484, 7614, 562, 321, 3488, 18161, 3164, 3364, 420, 3488,
  264, 20428, 3164, 51468], "temperature": 0.0, "avg_logprob": -0.22167723855854551,
  "compression_ratio": 1.696035242290749, "no_speech_prob": 0.0014247347135096788},
  {"id": 191, "seek": 122604, "start": 1248.12, "end": 1255.32, "text": " weight which
  normalization combination uh technique is usually the one that''s best to retrieve",
  "tokens": [51468, 3364, 597, 2710, 2144, 6562, 2232, 6532, 307, 2673, 264, 472,
  300, 311, 1151, 281, 30254, 51828], "temperature": 0.0, "avg_logprob": -0.22167723855854551,
  "compression_ratio": 1.696035242290749, "no_speech_prob": 0.0014247347135096788},
  {"id": 192, "seek": 125532, "start": 1255.32, "end": 1262.4399999999998, "text":
  " the results and so on and so forth so um we started out with what I call reasonable",
  "tokens": [50364, 264, 3542, 293, 370, 322, 293, 370, 5220, 370, 1105, 321, 1409,
  484, 365, 437, 286, 818, 10585, 50720], "temperature": 0.0, "avg_logprob": -0.20958518981933594,
  "compression_ratio": 1.5393258426966292, "no_speech_prob": 0.000259325752267614},
  {"id": 193, "seek": 125532, "start": 1262.4399999999998, "end": 1269.72, "text":
  " baseline so searching across um I think five or six fields so title category color
  brand", "tokens": [50720, 20518, 370, 10808, 2108, 1105, 286, 519, 1732, 420, 2309,
  7909, 370, 4876, 7719, 2017, 3360, 51084], "temperature": 0.0, "avg_logprob": -0.20958518981933594,
  "compression_ratio": 1.5393258426966292, "no_speech_prob": 0.000259325752267614},
  {"id": 194, "seek": 125532, "start": 1269.72, "end": 1277.8, "text": " and description
  some bullet points so ecommerce data set like pretty basic stuff um and we calculated",
  "tokens": [51084, 293, 3855, 512, 11632, 2793, 370, 308, 26926, 1412, 992, 411,
  1238, 3875, 1507, 1105, 293, 321, 15598, 51488], "temperature": 0.0, "avg_logprob":
  -0.20958518981933594, "compression_ratio": 1.5393258426966292, "no_speech_prob":
  0.000259325752267614}, {"id": 195, "seek": 127780, "start": 1277.8799999999999,
  "end": 1286.52, "text": " our metrics with that baseline so um I would call it uh
  probably not the best baseline you can come", "tokens": [50368, 527, 16367, 365,
  300, 20518, 370, 1105, 286, 576, 818, 309, 2232, 1391, 406, 264, 1151, 20518, 291,
  393, 808, 50800], "temperature": 0.0, "avg_logprob": -0.07955386373731825, "compression_ratio":
  1.9121951219512194, "no_speech_prob": 0.0008101784042082727}, {"id": 196, "seek":
  127780, "start": 1286.52, "end": 1293.32, "text": " up with um but a reasonable
  baseline um you could come up with so we didn''t want to let''s say", "tokens":
  [50800, 493, 365, 1105, 457, 257, 10585, 20518, 1105, 291, 727, 808, 493, 365, 370,
  321, 994, 380, 528, 281, 718, 311, 584, 51140], "temperature": 0.0, "avg_logprob":
  -0.07955386373731825, "compression_ratio": 1.9121951219512194, "no_speech_prob":
  0.0008101784042082727}, {"id": 197, "seek": 127780, "start": 1294.12, "end": 1300.04,
  "text": " just create the weakest baseline because that''s not really difficult
  to let''s say outperform so", "tokens": [51180, 445, 1884, 264, 44001, 20518, 570,
  300, 311, 406, 534, 2252, 281, 718, 311, 584, 484, 26765, 370, 51476], "temperature":
  0.0, "avg_logprob": -0.07955386373731825, "compression_ratio": 1.9121951219512194,
  "no_speech_prob": 0.0008101784042082727}, {"id": 198, "seek": 127780, "start": 1300.04,
  "end": 1306.36, "text": " we wanted to create a reasonable baseline without putting
  let''s say a man here in finding out what the", "tokens": [51476, 321, 1415, 281,
  1884, 257, 10585, 20518, 1553, 3372, 718, 311, 584, 257, 587, 510, 294, 5006, 484,
  437, 264, 51792], "temperature": 0.0, "avg_logprob": -0.07955386373731825, "compression_ratio":
  1.9121951219512194, "no_speech_prob": 0.0008101784042082727}, {"id": 199, "seek":
  130636, "start": 1306.36, "end": 1314.76, "text": " best baseline is um that''s
  called okay right um we got decent results out of that and then", "tokens": [50364,
  1151, 20518, 307, 1105, 300, 311, 1219, 1392, 558, 1105, 321, 658, 8681, 3542, 484,
  295, 300, 293, 550, 50784], "temperature": 0.0, "avg_logprob": -0.13504152095064204,
  "compression_ratio": 1.8110599078341014, "no_speech_prob": 0.0002652165130712092},
  {"id": 200, "seek": 130636, "start": 1314.76, "end": 1321.56, "text": " we ran this
  global hybrid search optimizer and that outperformed the baseline already um across
  the", "tokens": [50784, 321, 5872, 341, 4338, 13051, 3164, 5028, 6545, 293, 300,
  484, 610, 22892, 264, 20518, 1217, 1105, 2108, 264, 51124], "temperature": 0.0,
  "avg_logprob": -0.13504152095064204, "compression_ratio": 1.8110599078341014, "no_speech_prob":
  0.0002652165130712092}, {"id": 201, "seek": 130636, "start": 1321.56, "end": 1328.76,
  "text": " metrics that we had a look at so better in DCG better DCG better precision
  at 10 were um these were", "tokens": [51124, 16367, 300, 321, 632, 257, 574, 412,
  370, 1101, 294, 9114, 38, 1101, 9114, 38, 1101, 18356, 412, 1266, 645, 1105, 613,
  645, 51484], "temperature": 0.0, "avg_logprob": -0.13504152095064204, "compression_ratio":
  1.8110599078341014, "no_speech_prob": 0.0002652165130712092}, {"id": 202, "seek":
  130636, "start": 1328.76, "end": 1335.8, "text": " the three metrics that we had
  a look at and that was nice to see because that already gave us um let''s", "tokens":
  [51484, 264, 1045, 16367, 300, 321, 632, 257, 574, 412, 293, 300, 390, 1481, 281,
  536, 570, 300, 1217, 2729, 505, 1105, 718, 311, 51836], "temperature": 0.0, "avg_logprob":
  -0.13504152095064204, "compression_ratio": 1.8110599078341014, "no_speech_prob":
  0.0002652165130712092}, {"id": 203, "seek": 133580, "start": 1335.8, "end": 1342.2,
  "text": " say assurance in a there is a straightforward approach that everyone can
  use because it''s really", "tokens": [50364, 584, 32189, 294, 257, 456, 307, 257,
  15325, 3109, 300, 1518, 393, 764, 570, 309, 311, 534, 50684], "temperature": 0.0,
  "avg_logprob": -0.12143955732646741, "compression_ratio": 1.8019323671497585, "no_speech_prob":
  0.00033421439002268016}, {"id": 204, "seek": 133580, "start": 1342.2, "end": 1349.48,
  "text": " easily applicable um it gets you good results and it also gives you assurance
  that there is", "tokens": [50684, 3612, 21142, 1105, 309, 2170, 291, 665, 3542,
  293, 309, 611, 2709, 291, 32189, 300, 456, 307, 51048], "temperature": 0.0, "avg_logprob":
  -0.12143955732646741, "compression_ratio": 1.8019323671497585, "no_speech_prob":
  0.00033421439002268016}, {"id": 205, "seek": 133580, "start": 1349.48, "end": 1356.28,
  "text": " something too neural search when switching to it from a keyword based
  um search engine or", "tokens": [51048, 746, 886, 18161, 3164, 562, 16493, 281,
  309, 490, 257, 20428, 2361, 1105, 3164, 2848, 420, 51388], "temperature": 0.0, "avg_logprob":
  -0.12143955732646741, "compression_ratio": 1.8019323671497585, "no_speech_prob":
  0.00033421439002268016}, {"id": 206, "seek": 133580, "start": 1356.28, "end": 1364.9199999999998,
  "text": " search application to a hybrid search um application but um as always
  when you apply something", "tokens": [51388, 3164, 3861, 281, 257, 13051, 3164,
  1105, 3861, 457, 1105, 382, 1009, 562, 291, 3079, 746, 51820], "temperature": 0.0,
  "avg_logprob": -0.12143955732646741, "compression_ratio": 1.8019323671497585, "no_speech_prob":
  0.00033421439002268016}, {"id": 207, "seek": 136492, "start": 1364.92, "end": 1372.28,
  "text": " globally there are winners and there are losers so um some of the queries
  really improve by this", "tokens": [50364, 18958, 456, 366, 17193, 293, 456, 366,
  37713, 370, 1105, 512, 295, 264, 24109, 534, 3470, 538, 341, 50732], "temperature":
  0.0, "avg_logprob": -0.09761110428840883, "compression_ratio": 1.6201117318435754,
  "no_speech_prob": 0.00019892251293640584}, {"id": 208, "seek": 136492, "start":
  1372.28, "end": 1380.52, "text": " hybrid search optimization step the global one
  but others didn''t so we took this one step further", "tokens": [50732, 13051, 3164,
  19618, 1823, 264, 4338, 472, 457, 2357, 994, 380, 370, 321, 1890, 341, 472, 1823,
  3052, 51144], "temperature": 0.0, "avg_logprob": -0.09761110428840883, "compression_ratio":
  1.6201117318435754, "no_speech_prob": 0.00019892251293640584}, {"id": 209, "seek":
  136492, "start": 1380.52, "end": 1390.2, "text": " and thought about how can we
  um really create a process that dynamically per query now predicts", "tokens": [51144,
  293, 1194, 466, 577, 393, 321, 1105, 534, 1884, 257, 1399, 300, 43492, 680, 14581,
  586, 6069, 82, 51628], "temperature": 0.0, "avg_logprob": -0.09761110428840883,
  "compression_ratio": 1.6201117318435754, "no_speech_prob": 0.00019892251293640584},
  {"id": 210, "seek": 139020, "start": 1390.28, "end": 1397.96, "text": " what the
  best parameter set is and that now is also like going in this direction that dark
  mentions", "tokens": [50368, 437, 264, 1151, 13075, 992, 307, 293, 300, 586, 307,
  611, 411, 516, 294, 341, 3513, 300, 2877, 23844, 50752], "temperature": 0.0, "avg_logprob":
  -0.13489577770233155, "compression_ratio": 1.7477064220183487, "no_speech_prob":
  0.0005321715143509209}, {"id": 211, "seek": 139020, "start": 1397.96, "end": 1403.4,
  "text": " in his blog post right so that''s kind of a query understanding approach
  to hybrid search", "tokens": [50752, 294, 702, 6968, 2183, 558, 370, 300, 311, 733,
  295, 257, 14581, 3701, 3109, 281, 13051, 3164, 51024], "temperature": 0.0, "avg_logprob":
  -0.13489577770233155, "compression_ratio": 1.7477064220183487, "no_speech_prob":
  0.0005321715143509209}, {"id": 212, "seek": 139020, "start": 1404.1200000000001,
  "end": 1411.48, "text": " so we''re not just blindly applying one parameter combination
  that we identified on a thousand queries", "tokens": [51060, 370, 321, 434, 406,
  445, 47744, 9275, 472, 13075, 6562, 300, 321, 9234, 322, 257, 4714, 24109, 51428],
  "temperature": 0.0, "avg_logprob": -0.13489577770233155, "compression_ratio": 1.7477064220183487,
  "no_speech_prob": 0.0005321715143509209}, {"id": 213, "seek": 139020, "start": 1411.48,
  "end": 1418.68, "text": " that we explored we are taking one query analyzing this
  one query and then saying based on", "tokens": [51428, 300, 321, 24016, 321, 366,
  1940, 472, 14581, 23663, 341, 472, 14581, 293, 550, 1566, 2361, 322, 51788], "temperature":
  0.0, "avg_logprob": -0.13489577770233155, "compression_ratio": 1.7477064220183487,
  "no_speech_prob": 0.0005321715143509209}, {"id": 214, "seek": 141868, "start": 1419.3200000000002,
  "end": 1425.72, "text": " a variety of experiments that we made what is for this
  individual query the best parameter", "tokens": [50396, 257, 5673, 295, 12050, 300,
  321, 1027, 437, 307, 337, 341, 2609, 14581, 264, 1151, 13075, 50716], "temperature":
  0.0, "avg_logprob": -0.12494560388418344, "compression_ratio": 1.7788461538461537,
  "no_speech_prob": 0.0004352013929747045}, {"id": 215, "seek": 141868, "start": 1425.72,
  "end": 1431.16, "text": " combination that we cannot apply so that we are not really
  globally applying something but", "tokens": [50716, 6562, 300, 321, 2644, 3079,
  370, 300, 321, 366, 406, 534, 18958, 9275, 746, 457, 50988], "temperature": 0.0,
  "avg_logprob": -0.12494560388418344, "compression_ratio": 1.7788461538461537, "no_speech_prob":
  0.0004352013929747045}, {"id": 216, "seek": 141868, "start": 1431.16, "end": 1440.68,
  "text": " individually dynamically per query and um to already maybe yeah give you
  the results um of", "tokens": [50988, 16652, 43492, 680, 14581, 293, 1105, 281,
  1217, 1310, 1338, 976, 291, 264, 3542, 1105, 295, 51464], "temperature": 0.0, "avg_logprob":
  -0.12494560388418344, "compression_ratio": 1.7788461538461537, "no_speech_prob":
  0.0004352013929747045}, {"id": 217, "seek": 141868, "start": 1441.24, "end": 1447.96,
  "text": " what we did and then go into detail how we did it um the dynamic approach
  outperformed the global", "tokens": [51492, 437, 321, 630, 293, 550, 352, 666, 2607,
  577, 321, 630, 309, 1105, 264, 8546, 3109, 484, 610, 22892, 264, 4338, 51828], "temperature":
  0.0, "avg_logprob": -0.12494560388418344, "compression_ratio": 1.7788461538461537,
  "no_speech_prob": 0.0004352013929747045}, {"id": 218, "seek": 144796, "start": 1447.96,
  "end": 1456.76, "text": " approach so we managed to identify a set of features we
  trained a model or multiple models actually", "tokens": [50364, 3109, 370, 321,
  6453, 281, 5876, 257, 992, 295, 4122, 321, 8895, 257, 2316, 420, 3866, 5245, 767,
  50804], "temperature": 0.0, "avg_logprob": -0.130331888794899, "compression_ratio":
  1.6363636363636365, "no_speech_prob": 0.0004946246044710279}, {"id": 219, "seek":
  144796, "start": 1457.8, "end": 1464.52, "text": " and by applying this we were
  able to predict the best neuralness in that case or the best neural", "tokens":
  [50856, 293, 538, 9275, 341, 321, 645, 1075, 281, 6069, 264, 1151, 18161, 1287,
  294, 300, 1389, 420, 264, 1151, 18161, 51192], "temperature": 0.0, "avg_logprob":
  -0.130331888794899, "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0004946246044710279},
  {"id": 220, "seek": 144796, "start": 1464.52, "end": 1471.96, "text": " search weight
  for a given query based on um the results we got off the global hybrid search",
  "tokens": [51192, 3164, 3364, 337, 257, 2212, 14581, 2361, 322, 1105, 264, 3542,
  321, 658, 766, 264, 4338, 13051, 3164, 51564], "temperature": 0.0, "avg_logprob":
  -0.130331888794899, "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0004946246044710279},
  {"id": 221, "seek": 147196, "start": 1472.04, "end": 1479.32, "text": " optimizer
  so we basically recycled all the different search metrics on a per query basis that
  we got", "tokens": [50368, 5028, 6545, 370, 321, 1936, 30674, 439, 264, 819, 3164,
  16367, 322, 257, 680, 14581, 5143, 300, 321, 658, 50732], "temperature": 0.0, "avg_logprob":
  -0.15848018421846277, "compression_ratio": 1.668103448275862, "no_speech_prob":
  0.0003756447113119066}, {"id": 222, "seek": 147196, "start": 1479.88, "end": 1486.3600000000001,
  "text": " did some feature engineering trained models and then used these models
  to predict what is the", "tokens": [50760, 630, 512, 4111, 7043, 8895, 5245, 293,
  550, 1143, 613, 5245, 281, 6069, 437, 307, 264, 51084], "temperature": 0.0, "avg_logprob":
  -0.15848018421846277, "compression_ratio": 1.668103448275862, "no_speech_prob":
  0.0003756447113119066}, {"id": 223, "seek": 147196, "start": 1486.3600000000001,
  "end": 1493.32, "text": " best neural search weight for this query and with this
  dynamic approach we even saw increases", "tokens": [51084, 1151, 18161, 3164, 3364,
  337, 341, 14581, 293, 365, 341, 8546, 3109, 321, 754, 1866, 8637, 51432], "temperature":
  0.0, "avg_logprob": -0.15848018421846277, "compression_ratio": 1.668103448275862,
  "no_speech_prob": 0.0003756447113119066}, {"id": 224, "seek": 147196, "start": 1493.32,
  "end": 1501.48, "text": " up to 10% in one of the metrics of the three that I just
  mentioned DCG and DCG and precision at 10", "tokens": [51432, 493, 281, 1266, 4,
  294, 472, 295, 264, 16367, 295, 264, 1045, 300, 286, 445, 2835, 9114, 38, 293, 9114,
  38, 293, 18356, 412, 1266, 51840], "temperature": 0.0, "avg_logprob": -0.15848018421846277,
  "compression_ratio": 1.668103448275862, "no_speech_prob": 0.0003756447113119066},
  {"id": 225, "seek": 150196, "start": 1502.52, "end": 1507.56, "text": " yeah that''s
  very exciting thanks for for sharing this whole you know end-to-end", "tokens":
  [50392, 1338, 300, 311, 588, 4670, 3231, 337, 337, 5414, 341, 1379, 291, 458, 917,
  12, 1353, 12, 521, 50644], "temperature": 0.0, "avg_logprob": -0.19924222855340867,
  "compression_ratio": 1.6415929203539823, "no_speech_prob": 0.0009391083149239421},
  {"id": 226, "seek": 150196, "start": 1507.56, "end": 1516.76, "text": " picture
  pipeline I''m particularly interested at least at this point in time about the fact
  that", "tokens": [50644, 3036, 15517, 286, 478, 4098, 3102, 412, 1935, 412, 341,
  935, 294, 565, 466, 264, 1186, 300, 51104], "temperature": 0.0, "avg_logprob": -0.19924222855340867,
  "compression_ratio": 1.6415929203539823, "no_speech_prob": 0.0009391083149239421},
  {"id": 227, "seek": 150196, "start": 1516.76, "end": 1523.08, "text": " well first
  of all your dynamic approach outperformed the global one right and that seems to
  be thanks", "tokens": [51104, 731, 700, 295, 439, 428, 8546, 3109, 484, 610, 22892,
  264, 4338, 472, 558, 293, 300, 2544, 281, 312, 3231, 51420], "temperature": 0.0,
  "avg_logprob": -0.19924222855340867, "compression_ratio": 1.6415929203539823, "no_speech_prob":
  0.0009391083149239421}, {"id": 228, "seek": 150196, "start": 1523.08, "end": 1530.68,
  "text": " to that query understanding part right can you talk a bit more about that
  uh and also did you", "tokens": [51420, 281, 300, 14581, 3701, 644, 558, 393, 291,
  751, 257, 857, 544, 466, 300, 2232, 293, 611, 630, 291, 51800], "temperature": 0.0,
  "avg_logprob": -0.19924222855340867, "compression_ratio": 1.6415929203539823, "no_speech_prob":
  0.0009391083149239421}, {"id": 229, "seek": 153068, "start": 1531.64, "end": 1539.4,
  "text": " check those predictions manually for example does it make intuitive sense
  that system picked that''s", "tokens": [50412, 1520, 729, 21264, 16945, 337, 1365,
  775, 309, 652, 21769, 2020, 300, 1185, 6183, 300, 311, 50800], "temperature": 0.0,
  "avg_logprob": -0.16313033633761936, "compression_ratio": 1.6724890829694323, "no_speech_prob":
  0.0011577354744076729}, {"id": 230, "seek": 153068, "start": 1539.4, "end": 1545.16,
  "text": " for that specific query it picked more neuralness I mean is it like is
  it like a natural language", "tokens": [50800, 337, 300, 2685, 14581, 309, 6183,
  544, 18161, 1287, 286, 914, 307, 309, 411, 307, 309, 411, 257, 3303, 2856, 51088],
  "temperature": 0.0, "avg_logprob": -0.16313033633761936, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.0011577354744076729}, {"id": 231, "seek": 153068, "start": 1545.72,
  "end": 1551.16, "text": " question there or like some remnants of it or is there
  some other interesting findings that you", "tokens": [51116, 1168, 456, 420, 411,
  512, 44652, 295, 309, 420, 307, 456, 512, 661, 1880, 16483, 300, 291, 51388], "temperature":
  0.0, "avg_logprob": -0.16313033633761936, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.0011577354744076729}, {"id": 232, "seek": 153068, "start": 1551.16,
  "end": 1559.88, "text": " could share possibly oh yeah so um let''s first maybe
  outline what we did exactly and then", "tokens": [51388, 727, 2073, 6264, 1954,
  1338, 370, 1105, 718, 311, 700, 1310, 16387, 437, 321, 630, 2293, 293, 550, 51824],
  "temperature": 0.0, "avg_logprob": -0.16313033633761936, "compression_ratio": 1.6724890829694323,
  "no_speech_prob": 0.0011577354744076729}, {"id": 233, "seek": 155988, "start": 1560.44,
  "end": 1567.8000000000002, "text": " dive into a couple of observations that we
  made on the way um so we started out by creating", "tokens": [50392, 9192, 666,
  257, 1916, 295, 18163, 300, 321, 1027, 322, 264, 636, 1105, 370, 321, 1409, 484,
  538, 4084, 50760], "temperature": 0.0, "avg_logprob": -0.1355469822883606, "compression_ratio":
  2.0828729281767955, "no_speech_prob": 0.0001732686796458438}, {"id": 234, "seek":
  155988, "start": 1568.8400000000001, "end": 1575.8000000000002, "text": " what we
  call feature groups and then we created features for these feature groups so we
  looked at", "tokens": [50812, 437, 321, 818, 4111, 3935, 293, 550, 321, 2942, 4122,
  337, 613, 4111, 3935, 370, 321, 2956, 412, 51160], "temperature": 0.0, "avg_logprob":
  -0.1355469822883606, "compression_ratio": 2.0828729281767955, "no_speech_prob":
  0.0001732686796458438}, {"id": 235, "seek": 155988, "start": 1575.8000000000002,
  "end": 1582.2, "text": " three different feature groups um one was the query feature
  group the next one was the keyword", "tokens": [51160, 1045, 819, 4111, 3935, 1105,
  472, 390, 264, 14581, 4111, 1594, 264, 958, 472, 390, 264, 20428, 51480], "temperature":
  0.0, "avg_logprob": -0.1355469822883606, "compression_ratio": 2.0828729281767955,
  "no_speech_prob": 0.0001732686796458438}, {"id": 236, "seek": 155988, "start": 1582.2,
  "end": 1589.24, "text": " search result feature group and then the semantics search
  result feature group for the query", "tokens": [51480, 3164, 1874, 4111, 1594, 293,
  550, 264, 4361, 45298, 3164, 1874, 4111, 1594, 337, 264, 14581, 51832], "temperature":
  0.0, "avg_logprob": -0.1355469822883606, "compression_ratio": 2.0828729281767955,
  "no_speech_prob": 0.0001732686796458438}, {"id": 237, "seek": 158924, "start": 1589.32,
  "end": 1597.64, "text": " feature group we had a look at the length of the query
  the number of query terms if the query has", "tokens": [50368, 4111, 1594, 321,
  632, 257, 574, 412, 264, 4641, 295, 264, 14581, 264, 1230, 295, 14581, 2115, 498,
  264, 14581, 575, 50784], "temperature": 0.0, "avg_logprob": -0.07804080934235544,
  "compression_ratio": 1.8389261744966443, "no_speech_prob": 0.00014303417992778122},
  {"id": 238, "seek": 158924, "start": 1597.64, "end": 1605.0, "text": " numbers in
  it and if the query has any special characters in it so we kind of thought of ways",
  "tokens": [50784, 3547, 294, 309, 293, 498, 264, 14581, 575, 604, 2121, 4342, 294,
  309, 370, 321, 733, 295, 1194, 295, 2098, 51152], "temperature": 0.0, "avg_logprob":
  -0.07804080934235544, "compression_ratio": 1.8389261744966443, "no_speech_prob":
  0.00014303417992778122}, {"id": 239, "seek": 158924, "start": 1605.96, "end": 1612.52,
  "text": " figuring out when is the query maybe more specific when it is more when
  is it more", "tokens": [51200, 15213, 484, 562, 307, 264, 14581, 1310, 544, 2685,
  562, 309, 307, 544, 562, 307, 309, 544, 51528], "temperature": 0.0, "avg_logprob":
  -0.07804080934235544, "compression_ratio": 1.8389261744966443, "no_speech_prob":
  0.00014303417992778122}, {"id": 240, "seek": 161252, "start": 1612.52, "end": 1618.68,
  "text": " broad query a narrow query and then we will just come up with rules like
  well a longer", "tokens": [50364, 4152, 14581, 257, 9432, 14581, 293, 550, 321,
  486, 445, 808, 493, 365, 4474, 411, 731, 257, 2854, 50672], "temperature": 0.0,
  "avg_logprob": -0.14232163096583167, "compression_ratio": 1.968586387434555, "no_speech_prob":
  0.0014477790100499988}, {"id": 241, "seek": 161252, "start": 1618.68, "end": 1626.68,
  "text": " query is the more specific it is and maybe if we have more specific queries
  we have less results", "tokens": [50672, 14581, 307, 264, 544, 2685, 309, 307, 293,
  1310, 498, 321, 362, 544, 2685, 24109, 321, 362, 1570, 3542, 51072], "temperature":
  0.0, "avg_logprob": -0.14232163096583167, "compression_ratio": 1.968586387434555,
  "no_speech_prob": 0.0014477790100499988}, {"id": 242, "seek": 161252, "start": 1626.68,
  "end": 1634.2, "text": " that''s where we may want to augment search results with
  neural search results on the other hand", "tokens": [51072, 300, 311, 689, 321,
  815, 528, 281, 29919, 3164, 3542, 365, 18161, 3164, 3542, 322, 264, 661, 1011, 51448],
  "temperature": 0.0, "avg_logprob": -0.14232163096583167, "compression_ratio": 1.968586387434555,
  "no_speech_prob": 0.0014477790100499988}, {"id": 243, "seek": 161252, "start": 1634.2,
  "end": 1639.48, "text": " when we have a very broad query we may have a lot of results
  these are short queries and then we", "tokens": [51448, 562, 321, 362, 257, 588,
  4152, 14581, 321, 815, 362, 257, 688, 295, 3542, 613, 366, 2099, 24109, 293, 550,
  321, 51712], "temperature": 0.0, "avg_logprob": -0.14232163096583167, "compression_ratio":
  1.968586387434555, "no_speech_prob": 0.0014477790100499988}, {"id": 244, "seek":
  163948, "start": 1639.48, "end": 1646.2, "text": " may want to let''s say only use
  organic traditional keyword search results yeah so we just came up with", "tokens":
  [50364, 815, 528, 281, 718, 311, 584, 787, 764, 10220, 5164, 20428, 3164, 3542,
  1338, 370, 321, 445, 1361, 493, 365, 50700], "temperature": 0.0, "avg_logprob":
  -0.11411915296389732, "compression_ratio": 1.819047619047619, "no_speech_prob":
  0.00030637902091257274}, {"id": 245, "seek": 163948, "start": 1646.2, "end": 1654.84,
  "text": " a couple of assumptions on our side and then with these four features
  for the keyword search result", "tokens": [50700, 257, 1916, 295, 17695, 322, 527,
  1252, 293, 550, 365, 613, 1451, 4122, 337, 264, 20428, 3164, 1874, 51132], "temperature":
  0.0, "avg_logprob": -0.11411915296389732, "compression_ratio": 1.819047619047619,
  "no_speech_prob": 0.00030637902091257274}, {"id": 246, "seek": 163948, "start":
  1654.84, "end": 1662.6, "text": " feature group we looked at the number of search
  results the number of hits we got when we", "tokens": [51132, 4111, 1594, 321, 2956,
  412, 264, 1230, 295, 3164, 3542, 264, 1230, 295, 8664, 321, 658, 562, 321, 51520],
  "temperature": 0.0, "avg_logprob": -0.11411915296389732, "compression_ratio": 1.819047619047619,
  "no_speech_prob": 0.00030637902091257274}, {"id": 247, "seek": 163948, "start":
  1663.4, "end": 1669.24, "text": " executed the query with our baseline search configuration
  so the one searching in the six", "tokens": [51560, 17577, 264, 14581, 365, 527,
  20518, 3164, 11694, 370, 264, 472, 10808, 294, 264, 2309, 51852], "temperature":
  0.0, "avg_logprob": -0.11411915296389732, "compression_ratio": 1.819047619047619,
  "no_speech_prob": 0.00030637902091257274}, {"id": 248, "seek": 166924, "start":
  1669.24, "end": 1676.04, "text": " fields and then with something like hey if we
  have zero results then this is maybe a perfect scenario", "tokens": [50364, 7909,
  293, 550, 365, 746, 411, 4177, 498, 321, 362, 4018, 3542, 550, 341, 307, 1310, 257,
  2176, 9005, 50704], "temperature": 0.0, "avg_logprob": -0.11994010894024959, "compression_ratio":
  1.699421965317919, "no_speech_prob": 0.0004973821341991425}, {"id": 249, "seek":
  166924, "start": 1676.04, "end": 1684.92, "text": " for neural search because then
  we want to augment zero results with zero keyword results with what", "tokens":
  [50704, 337, 18161, 3164, 570, 550, 321, 528, 281, 29919, 4018, 3542, 365, 4018,
  20428, 3542, 365, 437, 51148], "temperature": 0.0, "avg_logprob": -0.11994010894024959,
  "compression_ratio": 1.699421965317919, "no_speech_prob": 0.0004973821341991425},
  {"id": 250, "seek": 166924, "start": 1684.92, "end": 1694.6, "text": " comes from
  the vector search application the other two features we had in this group were the",
  "tokens": [51148, 1487, 490, 264, 8062, 3164, 3861, 264, 661, 732, 4122, 321, 632,
  294, 341, 1594, 645, 264, 51632], "temperature": 0.0, "avg_logprob": -0.11994010894024959,
  "compression_ratio": 1.699421965317919, "no_speech_prob": 0.0004973821341991425},
  {"id": 251, "seek": 169460, "start": 1695.48, "end": 1702.4399999999998, "text":
  " the best title score we had in the keyword search result so if we have a strong
  title match maybe", "tokens": [50408, 264, 1151, 4876, 6175, 321, 632, 294, 264,
  20428, 3164, 1874, 370, 498, 321, 362, 257, 2068, 4876, 2995, 1310, 50756], "temperature":
  0.0, "avg_logprob": -0.0765617644950135, "compression_ratio": 1.716763005780347,
  "no_speech_prob": 0.0008155876421369612}, {"id": 252, "seek": 169460, "start": 1702.4399999999998,
  "end": 1711.8, "text": " that''s an indication of we don''t need as much neural
  search and we also have a look at I think the", "tokens": [50756, 300, 311, 364,
  18877, 295, 321, 500, 380, 643, 382, 709, 18161, 3164, 293, 321, 611, 362, 257,
  574, 412, 286, 519, 264, 51224], "temperature": 0.0, "avg_logprob": -0.0765617644950135,
  "compression_ratio": 1.716763005780347, "no_speech_prob": 0.0008155876421369612},
  {"id": 253, "seek": 169460, "start": 1711.8, "end": 1719.56, "text": " average title
  score in the top 10 was was another one so if we have like a high average in the
  title", "tokens": [51224, 4274, 4876, 6175, 294, 264, 1192, 1266, 390, 390, 1071,
  472, 370, 498, 321, 362, 411, 257, 1090, 4274, 294, 264, 4876, 51612], "temperature":
  0.0, "avg_logprob": -0.0765617644950135, "compression_ratio": 1.716763005780347,
  "no_speech_prob": 0.0008155876421369612}, {"id": 254, "seek": 171956, "start": 1719.56,
  "end": 1728.84, "text": " scores that''s maybe a good sign for no augmentation needed
  with neural search results for semantic", "tokens": [50364, 13444, 300, 311, 1310,
  257, 665, 1465, 337, 572, 14501, 19631, 2978, 365, 18161, 3164, 3542, 337, 47982,
  50828], "temperature": 0.0, "avg_logprob": -0.09373751420241136, "compression_ratio":
  1.7218934911242603, "no_speech_prob": 0.0005050160689279437}, {"id": 255, "seek":
  171956, "start": 1728.84, "end": 1738.6, "text": " search it was similar to the
  title score so we had a look at the best title score and the average", "tokens":
  [50828, 3164, 309, 390, 2531, 281, 264, 4876, 6175, 370, 321, 632, 257, 574, 412,
  264, 1151, 4876, 6175, 293, 264, 4274, 51316], "temperature": 0.0, "avg_logprob":
  -0.09373751420241136, "compression_ratio": 1.7218934911242603, "no_speech_prob":
  0.0005050160689279437}, {"id": 256, "seek": 171956, "start": 1739.3999999999999,
  "end": 1746.44, "text": " semantic similarity based on the title that we had indexed
  so by looking at these three groups", "tokens": [51356, 47982, 32194, 2361, 322,
  264, 4876, 300, 321, 632, 8186, 292, 370, 538, 1237, 412, 613, 1045, 3935, 51708],
  "temperature": 0.0, "avg_logprob": -0.09373751420241136, "compression_ratio": 1.7218934911242603,
  "no_speech_prob": 0.0005050160689279437}, {"id": 257, "seek": 174644, "start": 1746.44,
  "end": 1753.48, "text": " we thought of well we now have a representation of the
  query on its own the result set based on keywords", "tokens": [50364, 321, 1194,
  295, 731, 321, 586, 362, 257, 10290, 295, 264, 14581, 322, 1080, 1065, 264, 1874,
  992, 2361, 322, 21009, 50716], "temperature": 0.0, "avg_logprob": -0.0883289048838061,
  "compression_ratio": 1.7972972972972974, "no_speech_prob": 0.0012511537643149495},
  {"id": 258, "seek": 174644, "start": 1753.48, "end": 1760.28, "text": " and then
  the result set based on neural search and that was kind of our starting point and
  then we", "tokens": [50716, 293, 550, 264, 1874, 992, 2361, 322, 18161, 3164, 293,
  300, 390, 733, 295, 527, 2891, 935, 293, 550, 321, 51056], "temperature": 0.0, "avg_logprob":
  -0.0883289048838061, "compression_ratio": 1.7972972972972974, "no_speech_prob":
  0.0012511537643149495}, {"id": 259, "seek": 174644, "start": 1760.28, "end": 1768.1200000000001,
  "text": " did loads of experiments having to do with what''s the best feature combination
  when we train a linear", "tokens": [51056, 630, 12668, 295, 12050, 1419, 281, 360,
  365, 437, 311, 264, 1151, 4111, 6562, 562, 321, 3847, 257, 8213, 51448], "temperature":
  0.0, "avg_logprob": -0.0883289048838061, "compression_ratio": 1.7972972972972974,
  "no_speech_prob": 0.0012511537643149495}, {"id": 260, "seek": 174644, "start": 1768.1200000000001,
  "end": 1775.96, "text": " regression model or a random forest regression model what
  does regularization play for a role", "tokens": [51448, 24590, 2316, 420, 257, 4974,
  6719, 24590, 2316, 437, 775, 3890, 2144, 862, 337, 257, 3090, 51840], "temperature":
  0.0, "avg_logprob": -0.0883289048838061, "compression_ratio": 1.7972972972972974,
  "no_speech_prob": 0.0012511537643149495}, {"id": 261, "seek": 177596, "start": 1776.2,
  "end": 1784.2, "text": " can we optimize the model training aspect with that so
  we really did a lot of iterations with these we", "tokens": [50376, 393, 321, 19719,
  264, 2316, 3097, 4171, 365, 300, 370, 321, 534, 630, 257, 688, 295, 36540, 365,
  613, 321, 50776], "temperature": 0.0, "avg_logprob": -0.14441747376413056, "compression_ratio":
  1.646067415730337, "no_speech_prob": 0.00133566337171942}, {"id": 262, "seek": 177596,
  "start": 1784.2, "end": 1791.0, "text": " also had a look at a large query set and
  versus a smaller query set to see if that also provides", "tokens": [50776, 611,
  632, 257, 574, 412, 257, 2416, 14581, 992, 293, 5717, 257, 4356, 14581, 992, 281,
  536, 498, 300, 611, 6417, 51116], "temperature": 0.0, "avg_logprob": -0.14441747376413056,
  "compression_ratio": 1.646067415730337, "no_speech_prob": 0.00133566337171942},
  {"id": 263, "seek": 177596, "start": 1791.0, "end": 1801.4, "text": " different
  aspects to it if we just randomly sound the 500 yet 500 queries versus 5000 queries",
  "tokens": [51116, 819, 7270, 281, 309, 498, 321, 445, 16979, 1626, 264, 5923, 1939,
  5923, 24109, 5717, 23777, 24109, 51636], "temperature": 0.0, "avg_logprob": -0.14441747376413056,
  "compression_ratio": 1.646067415730337, "no_speech_prob": 0.00133566337171942},
  {"id": 264, "seek": 180140, "start": 1801.5600000000002, "end": 1810.92, "text":
  " so we did a lot of exploration to really pick out and make sure that we are not
  really let''s say", "tokens": [50372, 370, 321, 630, 257, 688, 295, 16197, 281,
  534, 1888, 484, 293, 652, 988, 300, 321, 366, 406, 534, 718, 311, 584, 50840], "temperature":
  0.0, "avg_logprob": -0.17442808431737564, "compression_ratio": 1.7045454545454546,
  "no_speech_prob": 0.0032360912300646305}, {"id": 265, "seek": 180140, "start": 1810.92,
  "end": 1820.1200000000001, "text": " randomly receiving the uplift that we saw but
  actually really making sure that there is something", "tokens": [50840, 16979, 10040,
  264, 45407, 300, 321, 1866, 457, 767, 534, 1455, 988, 300, 456, 307, 746, 51300],
  "temperature": 0.0, "avg_logprob": -0.17442808431737564, "compression_ratio": 1.7045454545454546,
  "no_speech_prob": 0.0032360912300646305}, {"id": 266, "seek": 180140, "start": 1820.1200000000001,
  "end": 1830.2800000000002, "text": " to it and that we can go out in the wild there
  for example on this podcast and share our observations and", "tokens": [51300, 281,
  309, 293, 300, 321, 393, 352, 484, 294, 264, 4868, 456, 337, 1365, 322, 341, 7367,
  293, 2073, 527, 18163, 293, 51808], "temperature": 0.0, "avg_logprob": -0.17442808431737564,
  "compression_ratio": 1.7045454545454546, "no_speech_prob": 0.0032360912300646305},
  {"id": 267, "seek": 183028, "start": 1831.16, "end": 1837.08, "text": " be kind
  of on the safe side that they can be reproduced hopefully in other scenarios as
  well", "tokens": [50408, 312, 733, 295, 322, 264, 3273, 1252, 300, 436, 393, 312,
  11408, 1232, 4696, 294, 661, 15077, 382, 731, 50704], "temperature": 0.0, "avg_logprob":
  -0.12407591848662405, "compression_ratio": 1.6705882352941177, "no_speech_prob":
  0.00036687497049570084}, {"id": 268, "seek": 183028, "start": 1839.72, "end": 1847.3999999999999,
  "text": " so that''s kind of on the let''s say how did we do it here so the features
  feature engineering", "tokens": [50836, 370, 300, 311, 733, 295, 322, 264, 718,
  311, 584, 577, 630, 321, 360, 309, 510, 370, 264, 4122, 4111, 7043, 51220], "temperature":
  0.0, "avg_logprob": -0.12407591848662405, "compression_ratio": 1.6705882352941177,
  "no_speech_prob": 0.00036687497049570084}, {"id": 269, "seek": 183028, "start":
  1847.3999999999999, "end": 1853.48, "text": " how we train our models so we have
  a look at linear regression models and random forest regression", "tokens": [51220,
  577, 321, 3847, 527, 5245, 370, 321, 362, 257, 574, 412, 8213, 24590, 5245, 293,
  4974, 6719, 24590, 51524], "temperature": 0.0, "avg_logprob": -0.12407591848662405,
  "compression_ratio": 1.6705882352941177, "no_speech_prob": 0.00036687497049570084},
  {"id": 270, "seek": 185348, "start": 1854.3600000000001, "end": 1861.24, "text":
  " as a starting point because we thought let''s have a look at simple models first
  and if that works", "tokens": [50408, 382, 257, 2891, 935, 570, 321, 1194, 718,
  311, 362, 257, 574, 412, 2199, 5245, 700, 293, 498, 300, 1985, 50752], "temperature":
  0.0, "avg_logprob": -0.07810977064532998, "compression_ratio": 1.8390243902439025,
  "no_speech_prob": 0.0013448463287204504}, {"id": 271, "seek": 185348, "start": 1861.24,
  "end": 1867.64, "text": " we can still have a look at the more complex ones and
  that''s maybe already the first observation", "tokens": [50752, 321, 393, 920, 362,
  257, 574, 412, 264, 544, 3997, 2306, 293, 300, 311, 1310, 1217, 264, 700, 14816,
  51072], "temperature": 0.0, "avg_logprob": -0.07810977064532998, "compression_ratio":
  1.8390243902439025, "no_speech_prob": 0.0013448463287204504}, {"id": 272, "seek":
  185348, "start": 1867.64, "end": 1875.64, "text": " that I can share so linear regression
  models and the simplest form random forest regression", "tokens": [51072, 300, 286,
  393, 2073, 370, 8213, 24590, 5245, 293, 264, 22811, 1254, 4974, 6719, 24590, 51472],
  "temperature": 0.0, "avg_logprob": -0.07810977064532998, "compression_ratio": 1.8390243902439025,
  "no_speech_prob": 0.0013448463287204504}, {"id": 273, "seek": 185348, "start": 1875.64,
  "end": 1880.76, "text": " slightly more complex form and then this is the last model
  iteration that we did last week", "tokens": [51472, 4748, 544, 3997, 1254, 293,
  550, 341, 307, 264, 1036, 2316, 24784, 300, 321, 630, 1036, 1243, 51728], "temperature":
  0.0, "avg_logprob": -0.07810977064532998, "compression_ratio": 1.8390243902439025,
  "no_speech_prob": 0.0013448463287204504}, {"id": 274, "seek": 188076, "start": 1881.4,
  "end": 1891.72, "text": " we also have a look at gradient boosting methods and interestingly
  they all were almost the same", "tokens": [50396, 321, 611, 362, 257, 574, 412,
  16235, 43117, 7150, 293, 25873, 436, 439, 645, 1920, 264, 912, 50912], "temperature":
  0.0, "avg_logprob": -0.07371518688817177, "compression_ratio": 1.5815217391304348,
  "no_speech_prob": 0.0006007174379192293}, {"id": 275, "seek": 188076, "start": 1891.72,
  "end": 1898.36, "text": " from the model performance perspective so it wasn''t like
  the most complex ones really give you", "tokens": [50912, 490, 264, 2316, 3389,
  4585, 370, 309, 2067, 380, 411, 264, 881, 3997, 2306, 534, 976, 291, 51244], "temperature":
  0.0, "avg_logprob": -0.07371518688817177, "compression_ratio": 1.5815217391304348,
  "no_speech_prob": 0.0006007174379192293}, {"id": 276, "seek": 188076, "start": 1898.36,
  "end": 1906.6, "text": " the best results and that''s kind of a very reassuring
  feeling because we need to calculate a couple", "tokens": [51244, 264, 1151, 3542,
  293, 300, 311, 733, 295, 257, 588, 19486, 1345, 2633, 570, 321, 643, 281, 8873,
  257, 1916, 51656], "temperature": 0.0, "avg_logprob": -0.07371518688817177, "compression_ratio":
  1.5815217391304348, "no_speech_prob": 0.0006007174379192293}, {"id": 277, "seek":
  190660, "start": 1906.76, "end": 1914.9199999999998, "text": " features right per
  query and that adds latency to your query execution and especially in e-commerce",
  "tokens": [50372, 4122, 558, 680, 14581, 293, 300, 10860, 27043, 281, 428, 14581,
  15058, 293, 2318, 294, 308, 12, 26926, 50780], "temperature": 0.0, "avg_logprob":
  -0.13972900027320498, "compression_ratio": 1.5614973262032086, "no_speech_prob":
  0.0022194196935743093}, {"id": 278, "seek": 190660, "start": 1914.9199999999998,
  "end": 1920.76, "text": " where every millisecond basically counts we don''t really
  want to let''s say run multiple queries", "tokens": [50780, 689, 633, 27940, 18882,
  1936, 14893, 321, 500, 380, 534, 528, 281, 718, 311, 584, 1190, 3866, 24109, 51072],
  "temperature": 0.0, "avg_logprob": -0.13972900027320498, "compression_ratio": 1.5614973262032086,
  "no_speech_prob": 0.0022194196935743093}, {"id": 279, "seek": 190660, "start": 1920.76,
  "end": 1929.8, "text": " to calculate our features just to have like 0.3 percent
  performance increase so it really has to", "tokens": [51072, 281, 8873, 527, 4122,
  445, 281, 362, 411, 1958, 13, 18, 3043, 3389, 3488, 370, 309, 534, 575, 281, 51524],
  "temperature": 0.0, "avg_logprob": -0.13972900027320498, "compression_ratio": 1.5614973262032086,
  "no_speech_prob": 0.0022194196935743093}, {"id": 280, "seek": 192980, "start": 1930.44,
  "end": 1937.6399999999999, "text": " be worth the effort so that''s kind of a nice
  observation so we don''t have to go for the most", "tokens": [50396, 312, 3163,
  264, 4630, 370, 300, 311, 733, 295, 257, 1481, 14816, 370, 321, 500, 380, 362, 281,
  352, 337, 264, 881, 50756], "temperature": 0.0, "avg_logprob": -0.15205131342381606,
  "compression_ratio": 1.6771300448430493, "no_speech_prob": 0.0016967261908575892},
  {"id": 281, "seek": 192980, "start": 1937.6399999999999, "end": 1943.6399999999999,
  "text": " complex model architectures we can stick with the simple ones and don''t
  really lose a lot of", "tokens": [50756, 3997, 2316, 6331, 1303, 321, 393, 2897,
  365, 264, 2199, 2306, 293, 500, 380, 534, 3624, 257, 688, 295, 51056], "temperature":
  0.0, "avg_logprob": -0.15205131342381606, "compression_ratio": 1.6771300448430493,
  "no_speech_prob": 0.0016967261908575892}, {"id": 282, "seek": 192980, "start": 1943.6399999999999,
  "end": 1950.68, "text": " performance if any the linear regression model and the
  random forest regression model they actually", "tokens": [51056, 3389, 498, 604,
  264, 8213, 24590, 2316, 293, 264, 4974, 6719, 24590, 2316, 436, 767, 51408], "temperature":
  0.0, "avg_logprob": -0.15205131342381606, "compression_ratio": 1.6771300448430493,
  "no_speech_prob": 0.0016967261908575892}, {"id": 283, "seek": 192980, "start": 1950.68,
  "end": 1959.24, "text": " scored absolutely equally when calculating the search
  metrics so they predicted the NDEG", "tokens": [51408, 18139, 3122, 12309, 562,
  28258, 264, 3164, 16367, 370, 436, 19147, 264, 426, 22296, 38, 51836], "temperature":
  0.0, "avg_logprob": -0.15205131342381606, "compression_ratio": 1.6771300448430493,
  "no_speech_prob": 0.0016967261908575892}, {"id": 284, "seek": 195924, "start": 1959.24,
  "end": 1966.68, "text": " scores slightly different so that''s how we did it we
  predicted NDEG scores by adding neuroness", "tokens": [50364, 13444, 4748, 819,
  370, 300, 311, 577, 321, 630, 309, 321, 19147, 426, 22296, 38, 13444, 538, 5127,
  12087, 266, 442, 50736], "temperature": 0.0, "avg_logprob": -0.16975004217597875,
  "compression_ratio": 1.7710280373831775, "no_speech_prob": 0.0007928272243589163},
  {"id": 285, "seek": 195924, "start": 1966.68, "end": 1973.88, "text": " as a 10th
  feature in that case and by looking at which neuroness scored best and that kind
  of", "tokens": [50736, 382, 257, 1266, 392, 4111, 294, 300, 1389, 293, 538, 1237,
  412, 597, 12087, 266, 442, 18139, 1151, 293, 300, 733, 295, 51096], "temperature":
  0.0, "avg_logprob": -0.16975004217597875, "compression_ratio": 1.7710280373831775,
  "no_speech_prob": 0.0007928272243589163}, {"id": 286, "seek": 195924, "start": 1973.88,
  "end": 1981.96, "text": " the neuroness we went then with for testing efforts afterwards
  so that''s kind of the first interesting", "tokens": [51096, 264, 12087, 266, 442,
  321, 1437, 550, 365, 337, 4997, 6484, 10543, 370, 300, 311, 733, 295, 264, 700,
  1880, 51500], "temperature": 0.0, "avg_logprob": -0.16975004217597875, "compression_ratio":
  1.7710280373831775, "no_speech_prob": 0.0007928272243589163}, {"id": 287, "seek":
  195924, "start": 1981.96, "end": 1989.0, "text": " observation that we made we also
  had a look at different feature groups so what happens", "tokens": [51500, 14816,
  300, 321, 1027, 321, 611, 632, 257, 574, 412, 819, 4111, 3935, 370, 437, 2314, 51852],
  "temperature": 0.0, "avg_logprob": -0.16975004217597875, "compression_ratio": 1.7710280373831775,
  "no_speech_prob": 0.0007928272243589163}, {"id": 288, "seek": 198900, "start": 1989.0,
  "end": 1997.16, "text": " to model performance if we focus only on query features
  or only on keyword search result features", "tokens": [50364, 281, 2316, 3389, 498,
  321, 1879, 787, 322, 14581, 4122, 420, 787, 322, 20428, 3164, 1874, 4122, 50772],
  "temperature": 0.0, "avg_logprob": -0.10760331572147838, "compression_ratio": 1.7439024390243902,
  "no_speech_prob": 0.0002571550430729985}, {"id": 289, "seek": 198900, "start": 1997.16,
  "end": 2004.28, "text": " so training models within one feature group only and not
  taking all features into account", "tokens": [50772, 370, 3097, 5245, 1951, 472,
  4111, 1594, 787, 293, 406, 1940, 439, 4122, 666, 2696, 51128], "temperature": 0.0,
  "avg_logprob": -0.10760331572147838, "compression_ratio": 1.7439024390243902, "no_speech_prob":
  0.0002571550430729985}, {"id": 290, "seek": 198900, "start": 2005.32, "end": 2012.28,
  "text": " the interesting part here was that the combination work best so not always
  the combinations of all", "tokens": [51180, 264, 1880, 644, 510, 390, 300, 264,
  6562, 589, 1151, 370, 406, 1009, 264, 21267, 295, 439, 51528], "temperature": 0.0,
  "avg_logprob": -0.10760331572147838, "compression_ratio": 1.7439024390243902, "no_speech_prob":
  0.0002571550430729985}, {"id": 291, "seek": 201228, "start": 2012.28, "end": 2018.76,
  "text": " in nine features together with the neuroness feature but at least some
  of the key word search", "tokens": [50364, 294, 4949, 4122, 1214, 365, 264, 12087,
  266, 442, 4111, 457, 412, 1935, 512, 295, 264, 2141, 1349, 3164, 50688], "temperature":
  0.0, "avg_logprob": -0.16376498937606812, "compression_ratio": 1.913265306122449,
  "no_speech_prob": 0.000762462499551475}, {"id": 292, "seek": 201228, "start": 2018.76,
  "end": 2024.12, "text": " result features some of the semantics search result features
  and some of the queries features", "tokens": [50688, 1874, 4122, 512, 295, 264,
  4361, 45298, 3164, 1874, 4122, 293, 512, 295, 264, 24109, 4122, 50956], "temperature":
  0.0, "avg_logprob": -0.16376498937606812, "compression_ratio": 1.913265306122449,
  "no_speech_prob": 0.000762462499551475}, {"id": 293, "seek": 201228, "start": 2024.84,
  "end": 2030.2, "text": " so they were best but looking at the query features only
  and these are the simplest ones to", "tokens": [50992, 370, 436, 645, 1151, 457,
  1237, 412, 264, 14581, 4122, 787, 293, 613, 366, 264, 22811, 2306, 281, 51260],
  "temperature": 0.0, "avg_logprob": -0.16376498937606812, "compression_ratio": 1.913265306122449,
  "no_speech_prob": 0.000762462499551475}, {"id": 294, "seek": 201228, "start": 2030.2,
  "end": 2038.12, "text": " calculate they weren''t part of these models from this
  performance aspect so you wouldn''t really", "tokens": [51260, 8873, 436, 4999,
  380, 644, 295, 613, 5245, 490, 341, 3389, 4171, 370, 291, 2759, 380, 534, 51656],
  "temperature": 0.0, "avg_logprob": -0.16376498937606812, "compression_ratio": 1.913265306122449,
  "no_speech_prob": 0.000762462499551475}, {"id": 295, "seek": 203812, "start": 2038.1999999999998,
  "end": 2047.08, "text": " lose a lot if you only shows query features for your predictions
  so that was another nice observation", "tokens": [50368, 3624, 257, 688, 498, 291,
  787, 3110, 14581, 4122, 337, 428, 21264, 370, 300, 390, 1071, 1481, 14816, 50812],
  "temperature": 0.0, "avg_logprob": -0.13134191975449072, "compression_ratio": 1.6793478260869565,
  "no_speech_prob": 0.0008912773337215185}, {"id": 296, "seek": 203812, "start": 2047.08,
  "end": 2055.08, "text": " here that if you went with the highest performance in
  terms of let''s say inference speed and also speed", "tokens": [50812, 510, 300,
  498, 291, 1437, 365, 264, 6343, 3389, 294, 2115, 295, 718, 311, 584, 38253, 3073,
  293, 611, 3073, 51212], "temperature": 0.0, "avg_logprob": -0.13134191975449072,
  "compression_ratio": 1.6793478260869565, "no_speech_prob": 0.0008912773337215185},
  {"id": 297, "seek": 203812, "start": 2055.08, "end": 2063.16, "text": " of calculating
  the features beforehand you don''t lose a lot of search result quality so again
  you don''t", "tokens": [51212, 295, 28258, 264, 4122, 22893, 291, 500, 380, 3624,
  257, 688, 295, 3164, 1874, 3125, 370, 797, 291, 500, 380, 51616], "temperature":
  0.0, "avg_logprob": -0.13134191975449072, "compression_ratio": 1.6793478260869565,
  "no_speech_prob": 0.0008912773337215185}, {"id": 298, "seek": 206316, "start": 2063.24,
  "end": 2069.24, "text": " have to go with the most complex approach to get reasonable
  results out of that which was I think", "tokens": [50368, 362, 281, 352, 365, 264,
  881, 3997, 3109, 281, 483, 10585, 3542, 484, 295, 300, 597, 390, 286, 519, 50668],
  "temperature": 0.0, "avg_logprob": -0.21859038503546463, "compression_ratio": 1.5973451327433628,
  "no_speech_prob": 0.007162398658692837}, {"id": 299, "seek": 206316, "start": 2069.24,
  "end": 2074.92, "text": " the second most important finding at least from my perspective
  because that gives us again", "tokens": [50668, 264, 1150, 881, 1021, 5006, 412,
  1935, 490, 452, 4585, 570, 300, 2709, 505, 797, 50952], "temperature": 0.0, "avg_logprob":
  -0.21859038503546463, "compression_ratio": 1.5973451327433628, "no_speech_prob":
  0.007162398658692837}, {"id": 300, "seek": 206316, "start": 2075.64, "end": 2083.48,
  "text": " the assurance that when putting this into production we don''t assume
  let''s say hundreds of", "tokens": [50988, 264, 32189, 300, 562, 3372, 341, 666,
  4265, 321, 500, 380, 6552, 718, 311, 584, 6779, 295, 51380], "temperature": 0.0,
  "avg_logprob": -0.21859038503546463, "compression_ratio": 1.5973451327433628, "no_speech_prob":
  0.007162398658692837}, {"id": 301, "seek": 206316, "start": 2083.48, "end": 2089.08,
  "text": " milliseconds added to your query latency if you stick to the the simple
  features.", "tokens": [51380, 34184, 3869, 281, 428, 14581, 27043, 498, 291, 2897,
  281, 264, 264, 2199, 4122, 13, 51660], "temperature": 0.0, "avg_logprob": -0.21859038503546463,
  "compression_ratio": 1.5973451327433628, "no_speech_prob": 0.007162398658692837},
  {"id": 302, "seek": 208908, "start": 2089.16, "end": 2093.72, "text": " May it means
  that there''s like room for growth with this technique right we''re not", "tokens":
  [50368, 1891, 309, 1355, 300, 456, 311, 411, 1808, 337, 4599, 365, 341, 6532, 558,
  321, 434, 406, 50596], "temperature": 0.0, "avg_logprob": -0.18722731913995305,
  "compression_ratio": 1.757462686567164, "no_speech_prob": 0.06885755062103271},
  {"id": 303, "seek": 208908, "start": 2093.72, "end": 2099.88, "text": " maxing out
  this technique just to get started we can start out and then as we get more sophisticated",
  "tokens": [50596, 11469, 278, 484, 341, 6532, 445, 281, 483, 1409, 321, 393, 722,
  484, 293, 550, 382, 321, 483, 544, 16950, 50904], "temperature": 0.0, "avg_logprob":
  -0.18722731913995305, "compression_ratio": 1.757462686567164, "no_speech_prob":
  0.06885755062103271}, {"id": 304, "seek": 208908, "start": 2099.88, "end": 2107.56,
  "text": " we have room we have milliseconds to burn to do other cool interesting
  things ask an lllm to", "tokens": [50904, 321, 362, 1808, 321, 362, 34184, 281,
  5064, 281, 360, 661, 1627, 1880, 721, 1029, 364, 287, 285, 76, 281, 51288], "temperature":
  0.0, "avg_logprob": -0.18722731913995305, "compression_ratio": 1.757462686567164,
  "no_speech_prob": 0.06885755062103271}, {"id": 305, "seek": 208908, "start": 2107.56,
  "end": 2112.2799999999997, "text": " characterize the query or something like that
  right we''ve got room for bro but I will also like", "tokens": [51288, 38463, 264,
  14581, 420, 746, 411, 300, 558, 321, 600, 658, 1808, 337, 2006, 457, 286, 486, 611,
  411, 51524], "temperature": 0.0, "avg_logprob": -0.18722731913995305, "compression_ratio":
  1.757462686567164, "no_speech_prob": 0.06885755062103271}, {"id": 306, "seek": 208908,
  "start": 2112.2799999999997, "end": 2118.04, "text": " this lesson and I think it
  kind of resonates with what I''ve seen in doing a mal previously is that", "tokens":
  [51524, 341, 6898, 293, 286, 519, 309, 733, 295, 41051, 365, 437, 286, 600, 1612,
  294, 884, 257, 2806, 8046, 307, 300, 51812], "temperature": 0.0, "avg_logprob":
  -0.18722731913995305, "compression_ratio": 1.757462686567164, "no_speech_prob":
  0.06885755062103271}, {"id": 307, "seek": 211804, "start": 2118.68, "end": 2125.4,
  "text": " start with like simpler solutions and try to kind of maximize ROI you
  know by upgrading to", "tokens": [50396, 722, 365, 411, 18587, 6547, 293, 853, 281,
  733, 295, 19874, 49808, 291, 458, 538, 36249, 281, 50732], "temperature": 0.0, "avg_logprob":
  -0.08514618343777126, "compression_ratio": 1.641025641025641, "no_speech_prob":
  0.008666086941957474}, {"id": 308, "seek": 211804, "start": 2125.4, "end": 2130.6,
  "text": " a more complex one and you need to set some thresholds because like as
  you said Daniel you know just", "tokens": [50732, 257, 544, 3997, 472, 293, 291,
  643, 281, 992, 512, 14678, 82, 570, 411, 382, 291, 848, 8033, 291, 458, 445, 50992],
  "temperature": 0.0, "avg_logprob": -0.08514618343777126, "compression_ratio": 1.641025641025641,
  "no_speech_prob": 0.008666086941957474}, {"id": 309, "seek": 211804, "start": 2130.6,
  "end": 2137.08, "text": " you know adding 0.03 won''t get it right it doesn''t it''s
  not worth because also when you bring", "tokens": [50992, 291, 458, 5127, 1958,
  13, 11592, 1582, 380, 483, 309, 558, 309, 1177, 380, 309, 311, 406, 3163, 570, 611,
  562, 291, 1565, 51316], "temperature": 0.0, "avg_logprob": -0.08514618343777126,
  "compression_ratio": 1.641025641025641, "no_speech_prob": 0.008666086941957474},
  {"id": 310, "seek": 211804, "start": 2137.08, "end": 2142.92, "text": " in neural
  search it means that you need to build that parallel index of things right like
  you need", "tokens": [51316, 294, 18161, 3164, 309, 1355, 300, 291, 643, 281, 1322,
  300, 8952, 8186, 295, 721, 558, 411, 291, 643, 51608], "temperature": 0.0, "avg_logprob":
  -0.08514618343777126, "compression_ratio": 1.641025641025641, "no_speech_prob":
  0.008666086941957474}, {"id": 311, "seek": 214292, "start": 2143.32, "end": 2151.48,
  "text": " you need to compute and maybe GPUs as well and someone will need to pay
  for it and I guess", "tokens": [50384, 291, 643, 281, 14722, 293, 1310, 18407, 82,
  382, 731, 293, 1580, 486, 643, 281, 1689, 337, 309, 293, 286, 2041, 50792], "temperature":
  0.0, "avg_logprob": -0.3127850426567925, "compression_ratio": 1.5217391304347827,
  "no_speech_prob": 0.007821322418749332}, {"id": 312, "seek": 214292, "start": 2151.48,
  "end": 2157.2400000000002, "text": " the passing Daniel we''re doing this project
  I kept asking Daniel I''m like why is re-indexing", "tokens": [50792, 264, 8437,
  8033, 321, 434, 884, 341, 1716, 286, 4305, 3365, 8033, 286, 478, 411, 983, 307,
  319, 12, 471, 3121, 278, 51080], "temperature": 0.0, "avg_logprob": -0.3127850426567925,
  "compression_ratio": 1.5217391304347827, "no_speech_prob": 0.007821322418749332},
  {"id": 313, "seek": 214292, "start": 2157.2400000000002, "end": 2164.44, "text":
  " with embedding so slow like where''s my turbo button like really why is this still
  a problem it''s", "tokens": [51080, 365, 12240, 3584, 370, 2964, 411, 689, 311,
  452, 20902, 2960, 411, 534, 983, 307, 341, 920, 257, 1154, 309, 311, 51440], "temperature":
  0.0, "avg_logprob": -0.3127850426567925, "compression_ratio": 1.5217391304347827,
  "no_speech_prob": 0.007821322418749332}, {"id": 314, "seek": 216444, "start": 2164.44,
  "end": 2173.16, "text": " 2024 almost 2025 why does embeddings take a long time
  yeah I remain a little confused why it''s so like", "tokens": [50364, 45237, 1920,
  39209, 983, 775, 12240, 29432, 747, 257, 938, 565, 1338, 286, 6222, 257, 707, 9019,
  983, 309, 311, 370, 411, 50800], "temperature": 0.0, "avg_logprob": -0.17782463965477882,
  "compression_ratio": 1.5336787564766838, "no_speech_prob": 0.005210345145314932},
  {"id": 315, "seek": 216444, "start": 2174.04, "end": 2181.32, "text": " don''t we
  just turn a knob and make a GPU go faster and then re-index with embeddings is just
  the same", "tokens": [50844, 500, 380, 321, 445, 1261, 257, 26759, 293, 652, 257,
  18407, 352, 4663, 293, 550, 319, 12, 471, 3121, 365, 12240, 29432, 307, 445, 264,
  912, 51208], "temperature": 0.0, "avg_logprob": -0.17782463965477882, "compression_ratio":
  1.5336787564766838, "no_speech_prob": 0.005210345145314932}, {"id": 316, "seek":
  216444, "start": 2181.32, "end": 2190.2000000000003, "text": " speed as re-indexing
  with keywords yeah but but also what Daniel says now but also like the", "tokens":
  [51208, 3073, 382, 319, 12, 471, 3121, 278, 365, 21009, 1338, 457, 457, 611, 437,
  8033, 1619, 586, 457, 611, 411, 264, 51652], "temperature": 0.0, "avg_logprob":
  -0.17782463965477882, "compression_ratio": 1.5336787564766838, "no_speech_prob":
  0.005210345145314932}, {"id": 317, "seek": 219020, "start": 2190.2, "end": 2194.52,
  "text": " fascinating part like one thought crossed my mind as you explained it
  Daniel is that in some", "tokens": [50364, 10343, 644, 411, 472, 1194, 14622, 452,
  1575, 382, 291, 8825, 309, 8033, 307, 300, 294, 512, 50580], "temperature": 0.0,
  "avg_logprob": -0.09886228519937267, "compression_ratio": 1.6986899563318778, "no_speech_prob":
  0.0012310482561588287}, {"id": 318, "seek": 219020, "start": 2194.52, "end": 2200.68,
  "text": " sense you''ve built some sort of like a reasoning engine if I may call
  it that way maybe it''s not", "tokens": [50580, 2020, 291, 600, 3094, 512, 1333,
  295, 411, 257, 21577, 2848, 498, 286, 815, 818, 309, 300, 636, 1310, 309, 311, 406,
  50888], "temperature": 0.0, "avg_logprob": -0.09886228519937267, "compression_ratio":
  1.6986899563318778, "no_speech_prob": 0.0012310482561588287}, {"id": 319, "seek":
  219020, "start": 2200.68, "end": 2206.3599999999997, "text": " fully you know reasoning
  like I don''t know LLM start to do it that way or something but it''s like", "tokens":
  [50888, 4498, 291, 458, 21577, 411, 286, 500, 380, 458, 441, 43, 44, 722, 281, 360,
  309, 300, 636, 420, 746, 457, 309, 311, 411, 51172], "temperature": 0.0, "avg_logprob":
  -0.09886228519937267, "compression_ratio": 1.6986899563318778, "no_speech_prob":
  0.0012310482561588287}, {"id": 320, "seek": 219020, "start": 2207.08, "end": 2212.8399999999997,
  "text": " the engine that looks at the query and examines its features and makes
  some some conclusions and then", "tokens": [51208, 264, 2848, 300, 1542, 412, 264,
  14581, 293, 1139, 1652, 1080, 4122, 293, 1669, 512, 512, 22865, 293, 550, 51496],
  "temperature": 0.0, "avg_logprob": -0.09886228519937267, "compression_ratio": 1.6986899563318778,
  "no_speech_prob": 0.0012310482561588287}, {"id": 321, "seek": 221284, "start": 2212.84,
  "end": 2219.96, "text": " it looks also at the results it''s not like you just you
  just you understood the query you set it", "tokens": [50364, 309, 1542, 611, 412,
  264, 3542, 309, 311, 406, 411, 291, 445, 291, 445, 291, 7320, 264, 14581, 291, 992,
  309, 50720], "temperature": 0.0, "avg_logprob": -0.07936587540999702, "compression_ratio":
  1.7713004484304933, "no_speech_prob": 0.001717950333841145}, {"id": 322, "seek":
  221284, "start": 2219.96, "end": 2225.32, "text": " over to the retriever side and
  then you hope for the best that there will be best results right but in", "tokens":
  [50720, 670, 281, 264, 19817, 331, 1252, 293, 550, 291, 1454, 337, 264, 1151, 300,
  456, 486, 312, 1151, 3542, 558, 457, 294, 50988], "temperature": 0.0, "avg_logprob":
  -0.07936587540999702, "compression_ratio": 1.7713004484304933, "no_speech_prob":
  0.001717950333841145}, {"id": 323, "seek": 221284, "start": 2225.32, "end": 2231.7200000000003,
  "text": " some sense you you basically do this dynamic sort of reasoning on top
  of everything but but the", "tokens": [50988, 512, 2020, 291, 291, 1936, 360, 341,
  8546, 1333, 295, 21577, 322, 1192, 295, 1203, 457, 457, 264, 51308], "temperature":
  0.0, "avg_logprob": -0.07936587540999702, "compression_ratio": 1.7713004484304933,
  "no_speech_prob": 0.001717950333841145}, {"id": 324, "seek": 221284, "start": 2231.7200000000003,
  "end": 2238.44, "text": " lesson there you said and correct me if I''m wrong is
  that just by looking at the query features you", "tokens": [51308, 6898, 456, 291,
  848, 293, 3006, 385, 498, 286, 478, 2085, 307, 300, 445, 538, 1237, 412, 264, 14581,
  4122, 291, 51644], "temperature": 0.0, "avg_logprob": -0.07936587540999702, "compression_ratio":
  1.7713004484304933, "no_speech_prob": 0.001717950333841145}, {"id": 325, "seek":
  223844, "start": 2238.44, "end": 2245.56, "text": " could already achieve good results
  you don''t need to look at the result features yes yes but", "tokens": [50364, 727,
  1217, 4584, 665, 3542, 291, 500, 380, 643, 281, 574, 412, 264, 1874, 4122, 2086,
  2086, 457, 50720], "temperature": 0.0, "avg_logprob": -0.09210114893705948, "compression_ratio":
  1.7252252252252251, "no_speech_prob": 0.001563511323183775}, {"id": 326, "seek":
  223844, "start": 2245.56, "end": 2251.8, "text": " wouldn''t it be nice to look
  at those yeah I do love the idea of looking at both sides right we", "tokens": [50720,
  2759, 380, 309, 312, 1481, 281, 574, 412, 729, 1338, 286, 360, 959, 264, 1558, 295,
  1237, 412, 1293, 4881, 558, 321, 51032], "temperature": 0.0, "avg_logprob": -0.09210114893705948,
  "compression_ratio": 1.7252252252252251, "no_speech_prob": 0.001563511323183775},
  {"id": 327, "seek": 223844, "start": 2251.8, "end": 2258.28, "text": " tend to focus
  on queries because I think that''s the viewpoint of our industry we are very query",
  "tokens": [51032, 3928, 281, 1879, 322, 24109, 570, 286, 519, 300, 311, 264, 35248,
  295, 527, 3518, 321, 366, 588, 14581, 51356], "temperature": 0.0, "avg_logprob":
  -0.09210114893705948, "compression_ratio": 1.7252252252252251, "no_speech_prob":
  0.001563511323183775}, {"id": 328, "seek": 223844, "start": 2258.28, "end": 2263.64,
  "text": " centric in the search world it''s all about the query and what can we
  get out of the query we really", "tokens": [51356, 1489, 1341, 294, 264, 3164, 1002,
  309, 311, 439, 466, 264, 14581, 293, 437, 393, 321, 483, 484, 295, 264, 14581, 321,
  534, 51624], "temperature": 0.0, "avg_logprob": -0.09210114893705948, "compression_ratio":
  1.7252252252252251, "no_speech_prob": 0.001563511323183775}, {"id": 329, "seek":
  226364, "start": 2263.72, "end": 2270.92, "text": " don''t look at the results that
  much except to say are they good or bad and we''re not particularly good", "tokens":
  [50368, 500, 380, 574, 412, 264, 3542, 300, 709, 3993, 281, 584, 366, 436, 665,
  420, 1578, 293, 321, 434, 406, 4098, 665, 50728], "temperature": 0.0, "avg_logprob":
  -0.08737870057423909, "compression_ratio": 1.6353591160220995, "no_speech_prob":
  0.003289616433903575}, {"id": 330, "seek": 226364, "start": 2270.92, "end": 2280.6,
  "text": " about factoring in and what did the user do back into our algorithm and
  yeah I love that this is a", "tokens": [50728, 466, 1186, 3662, 294, 293, 437, 630,
  264, 4195, 360, 646, 666, 527, 9284, 293, 1338, 286, 959, 300, 341, 307, 257, 51212],
  "temperature": 0.0, "avg_logprob": -0.08737870057423909, "compression_ratio": 1.6353591160220995,
  "no_speech_prob": 0.003289616433903575}, {"id": 331, "seek": 226364, "start": 2280.6,
  "end": 2286.7599999999998, "text": " little the dynamic thing that we''re doing
  here I think it''s a pointer to bring in more dynamic", "tokens": [51212, 707, 264,
  8546, 551, 300, 321, 434, 884, 510, 286, 519, 309, 311, 257, 23918, 281, 1565, 294,
  544, 8546, 51520], "temperature": 0.0, "avg_logprob": -0.08737870057423909, "compression_ratio":
  1.6353591160220995, "no_speech_prob": 0.003289616433903575}, {"id": 332, "seek":
  228676, "start": 2287.6400000000003, "end": 2293.96, "text": " aspects to our algorithms
  where they actually can start evolving or changing or being very specific", "tokens":
  [50408, 7270, 281, 527, 14642, 689, 436, 767, 393, 722, 21085, 420, 4473, 420, 885,
  588, 2685, 50724], "temperature": 0.0, "avg_logprob": -0.09651506142538102, "compression_ratio":
  1.6055555555555556, "no_speech_prob": 0.007187430281192064}, {"id": 333, "seek":
  228676, "start": 2293.96, "end": 2303.8, "text": " to very specific query types
  use cases time of year right and today that''s very difficult to do", "tokens":
  [50724, 281, 588, 2685, 14581, 3467, 764, 3331, 565, 295, 1064, 558, 293, 965, 300,
  311, 588, 2252, 281, 360, 51216], "temperature": 0.0, "avg_logprob": -0.09651506142538102,
  "compression_ratio": 1.6055555555555556, "no_speech_prob": 0.007187430281192064},
  {"id": 334, "seek": 228676, "start": 2303.8, "end": 2313.4, "text": " only the most
  sophisticated to teams have sets of algorithms yeah but I also feel like I like",
  "tokens": [51216, 787, 264, 881, 16950, 281, 5491, 362, 6352, 295, 14642, 1338,
  457, 286, 611, 841, 411, 286, 411, 51696], "temperature": 0.0, "avg_logprob": -0.09651506142538102,
  "compression_ratio": 1.6055555555555556, "no_speech_prob": 0.007187430281192064},
  {"id": 335, "seek": 231340, "start": 2313.56, "end": 2319.0, "text": " what you
  said Eric like looking at results you know and reasoning about results and also
  what", "tokens": [50372, 437, 291, 848, 9336, 411, 1237, 412, 3542, 291, 458, 293,
  21577, 466, 3542, 293, 611, 437, 50644], "temperature": 0.0, "avg_logprob": -0.0943937654848452,
  "compression_ratio": 1.892156862745098, "no_speech_prob": 0.0017330568516626954},
  {"id": 336, "seek": 231340, "start": 2319.0, "end": 2325.1600000000003, "text":
  " you understood about the query might lead to much better final representation
  of what you show to", "tokens": [50644, 291, 7320, 466, 264, 14581, 1062, 1477,
  281, 709, 1101, 2572, 10290, 295, 437, 291, 855, 281, 50952], "temperature": 0.0,
  "avg_logprob": -0.0943937654848452, "compression_ratio": 1.892156862745098, "no_speech_prob":
  0.0017330568516626954}, {"id": 337, "seek": 231340, "start": 2325.1600000000003,
  "end": 2332.12, "text": " the user right because there are so many there are so
  many factors also beyond the query and results", "tokens": [50952, 264, 4195, 558,
  570, 456, 366, 370, 867, 456, 366, 370, 867, 6771, 611, 4399, 264, 14581, 293, 3542,
  51300], "temperature": 0.0, "avg_logprob": -0.0943937654848452, "compression_ratio":
  1.892156862745098, "no_speech_prob": 0.0017330568516626954}, {"id": 338, "seek":
  231340, "start": 2332.12, "end": 2338.12, "text": " right like as you said season
  or you know you observed some patterns with the user the recent", "tokens": [51300,
  558, 411, 382, 291, 848, 3196, 420, 291, 458, 291, 13095, 512, 8294, 365, 264, 4195,
  264, 5162, 51600], "temperature": 0.0, "avg_logprob": -0.0943937654848452, "compression_ratio":
  1.892156862745098, "no_speech_prob": 0.0017330568516626954}, {"id": 339, "seek":
  233812, "start": 2338.12, "end": 2345.16, "text": " purchase history and so on and
  so forth yeah I mean it''s very fascinating and also like if I", "tokens": [50364,
  8110, 2503, 293, 370, 322, 293, 370, 5220, 1338, 286, 914, 309, 311, 588, 10343,
  293, 611, 411, 498, 286, 50716], "temperature": 0.0, "avg_logprob": -0.15321807239366614,
  "compression_ratio": 1.6491228070175439, "no_speech_prob": 0.008580013178288937},
  {"id": 340, "seek": 233812, "start": 2345.16, "end": 2350.8399999999997, "text":
  " continue to draw this analogy with lm world you know when you ask lm to to think
  through what it", "tokens": [50716, 2354, 281, 2642, 341, 21663, 365, 287, 76, 1002,
  291, 458, 562, 291, 1029, 287, 76, 281, 281, 519, 807, 437, 309, 51000], "temperature":
  0.0, "avg_logprob": -0.15321807239366614, "compression_ratio": 1.6491228070175439,
  "no_speech_prob": 0.008580013178288937}, {"id": 341, "seek": 233812, "start": 2350.8399999999997,
  "end": 2358.2799999999997, "text": " has done it may correct itself right by just
  looking at what it has produced because lm''s are", "tokens": [51000, 575, 1096,
  309, 815, 3006, 2564, 558, 538, 445, 1237, 412, 437, 309, 575, 7126, 570, 287, 76,
  311, 366, 51372], "temperature": 0.0, "avg_logprob": -0.15321807239366614, "compression_ratio":
  1.6491228070175439, "no_speech_prob": 0.008580013178288937}, {"id": 342, "seek":
  233812, "start": 2358.2799999999997, "end": 2365.96, "text": " as someone said calculators
  for words so if you if you give it itself its own output and ask", "tokens": [51372,
  382, 1580, 848, 4322, 3391, 337, 2283, 370, 498, 291, 498, 291, 976, 309, 2564,
  1080, 1065, 5598, 293, 1029, 51756], "temperature": 0.0, "avg_logprob": -0.15321807239366614,
  "compression_ratio": 1.6491228070175439, "no_speech_prob": 0.008580013178288937},
  {"id": 343, "seek": 236596, "start": 2366.52, "end": 2375.0, "text": " yeah exactly
  yeah like I can''t wait to write a search algorithm that understands what they did",
  "tokens": [50392, 1338, 2293, 1338, 411, 286, 393, 380, 1699, 281, 2464, 257, 3164,
  9284, 300, 15146, 437, 436, 630, 50816], "temperature": 0.0, "avg_logprob": -0.1078964430710365,
  "compression_ratio": 1.7853881278538812, "no_speech_prob": 0.026512479409575462},
  {"id": 344, "seek": 236596, "start": 2375.0, "end": 2380.6, "text": " the last time
  the user didn''t like the results and so when you get a similar query for the same
  user", "tokens": [50816, 264, 1036, 565, 264, 4195, 994, 380, 411, 264, 3542, 293,
  370, 562, 291, 483, 257, 2531, 14581, 337, 264, 912, 4195, 51096], "temperature":
  0.0, "avg_logprob": -0.1078964430710365, "compression_ratio": 1.7853881278538812,
  "no_speech_prob": 0.026512479409575462}, {"id": 345, "seek": 236596, "start": 2380.6,
  "end": 2386.44, "text": " do something new right try something new because whatever
  you were doing before the user didn''t like", "tokens": [51096, 360, 746, 777, 558,
  853, 746, 777, 570, 2035, 291, 645, 884, 949, 264, 4195, 994, 380, 411, 51388],
  "temperature": 0.0, "avg_logprob": -0.1078964430710365, "compression_ratio": 1.7853881278538812,
  "no_speech_prob": 0.026512479409575462}, {"id": 346, "seek": 236596, "start": 2387.2400000000002,
  "end": 2393.64, "text": " yeah joke about if the user hates what you''re giving
  them you might as well just return random", "tokens": [51428, 1338, 7647, 466, 498,
  264, 4195, 23000, 437, 291, 434, 2902, 552, 291, 1062, 382, 731, 445, 2736, 4974,
  51748], "temperature": 0.0, "avg_logprob": -0.1078964430710365, "compression_ratio":
  1.7853881278538812, "no_speech_prob": 0.026512479409575462}, {"id": 347, "seek":
  239364, "start": 2393.64, "end": 2399.64, "text": " docs because that''ll be better
  than whatever you''re doing right now yeah yeah at least you you have a", "tokens":
  [50364, 45623, 570, 300, 603, 312, 1101, 813, 2035, 291, 434, 884, 558, 586, 1338,
  1338, 412, 1935, 291, 291, 362, 257, 50664], "temperature": 0.0, "avg_logprob":
  -0.1216478895867008, "compression_ratio": 1.8246445497630333, "no_speech_prob":
  0.010809781961143017}, {"id": 348, "seek": 239364, "start": 2399.64, "end": 2407.3199999999997,
  "text": " chance there right with the random so what question I sort of have though
  in what we described how is", "tokens": [50664, 2931, 456, 558, 365, 264, 4974,
  370, 437, 1168, 286, 1333, 295, 362, 1673, 294, 437, 321, 7619, 577, 307, 51048],
  "temperature": 0.0, "avg_logprob": -0.1216478895867008, "compression_ratio": 1.8246445497630333,
  "no_speech_prob": 0.010809781961143017}, {"id": 349, "seek": 239364, "start": 2407.3199999999997,
  "end": 2414.12, "text": " it different than learning to rank other than learning
  to rank is about ranking one list", "tokens": [51048, 309, 819, 813, 2539, 281,
  6181, 661, 813, 2539, 281, 6181, 307, 466, 17833, 472, 1329, 51388], "temperature":
  0.0, "avg_logprob": -0.1216478895867008, "compression_ratio": 1.8246445497630333,
  "no_speech_prob": 0.010809781961143017}, {"id": 350, "seek": 239364, "start": 2415.48,
  "end": 2422.8399999999997, "text": " and here we''re ranking two lists is do I just
  conceptually have the role of learning to rank", "tokens": [51456, 293, 510, 321,
  434, 17833, 732, 14511, 307, 360, 286, 445, 3410, 671, 362, 264, 3090, 295, 2539,
  281, 6181, 51824], "temperature": 0.0, "avg_logprob": -0.1216478895867008, "compression_ratio":
  1.8246445497630333, "no_speech_prob": 0.010809781961143017}, {"id": 351, "seek":
  242284, "start": 2422.84, "end": 2430.04, "text": " wrong between what learning
  to rank is and how the dynamic hybrid optimizer was working", "tokens": [50364,
  2085, 1296, 437, 2539, 281, 6181, 307, 293, 577, 264, 8546, 13051, 5028, 6545, 390,
  1364, 50724], "temperature": 0.0, "avg_logprob": -0.08268000474616663, "compression_ratio":
  1.6171428571428572, "no_speech_prob": 0.0007803972694091499}, {"id": 352, "seek":
  242284, "start": 2432.28, "end": 2439.56, "text": " so I mean we are not re-ranking
  results right so that''s what typically learning to rank does but", "tokens": [50836,
  370, 286, 914, 321, 366, 406, 319, 12, 20479, 278, 3542, 558, 370, 300, 311, 437,
  5850, 2539, 281, 6181, 775, 457, 51200], "temperature": 0.0, "avg_logprob": -0.08268000474616663,
  "compression_ratio": 1.6171428571428572, "no_speech_prob": 0.0007803972694091499},
  {"id": 353, "seek": 242284, "start": 2439.56, "end": 2450.28, "text": " what we
  are kind of doing is we are learning when when to let''s say increase the weight
  on keyword", "tokens": [51200, 437, 321, 366, 733, 295, 884, 307, 321, 366, 2539,
  562, 562, 281, 718, 311, 584, 3488, 264, 3364, 322, 20428, 51736], "temperature":
  0.0, "avg_logprob": -0.08268000474616663, "compression_ratio": 1.6171428571428572,
  "no_speech_prob": 0.0007803972694091499}, {"id": 354, "seek": 245028, "start": 2450.28,
  "end": 2457.4, "text": " search results or on your search results right so it''s
  kind of a learn to", "tokens": [50364, 3164, 3542, 420, 322, 428, 3164, 3542, 558,
  370, 309, 311, 733, 295, 257, 1466, 281, 50720], "temperature": 0.0, "avg_logprob":
  -0.19344098944413035, "compression_ratio": 1.7352941176470589, "no_speech_prob":
  0.0023917951621115208}, {"id": 355, "seek": 245028, "start": 2458.6800000000003,
  "end": 2467.0800000000004, "text": " lend learn to blend learn to search the new
  technology or we just done with the learning to", "tokens": [50784, 21774, 1466,
  281, 10628, 1466, 281, 3164, 264, 777, 2899, 420, 321, 445, 1096, 365, 264, 2539,
  281, 51204], "temperature": 0.0, "avg_logprob": -0.19344098944413035, "compression_ratio":
  1.7352941176470589, "no_speech_prob": 0.0023917951621115208}, {"id": 356, "seek":
  245028, "start": 2469.0, "end": 2474.52, "text": " nomenclature right and we like
  optimizer better than learning to blend", "tokens": [51300, 297, 4726, 3474, 1503,
  558, 293, 321, 411, 5028, 6545, 1101, 813, 2539, 281, 10628, 51576], "temperature":
  0.0, "avg_logprob": -0.19344098944413035, "compression_ratio": 1.7352941176470589,
  "no_speech_prob": 0.0023917951621115208}, {"id": 357, "seek": 247452, "start": 2475.16,
  "end": 2484.2, "text": " maybe yeah so I''m not the one who''s most creative in
  coming up with clever names so maybe it''s", "tokens": [50396, 1310, 1338, 370,
  286, 478, 406, 264, 472, 567, 311, 881, 5880, 294, 1348, 493, 365, 13494, 5288,
  370, 1310, 309, 311, 50848], "temperature": 0.0, "avg_logprob": -0.1449633631212958,
  "compression_ratio": 1.7416267942583732, "no_speech_prob": 0.005703783128410578},
  {"id": 358, "seek": 247452, "start": 2484.2, "end": 2492.12, "text": " maybe it''s
  time for not learn to but blah blah blah optimizer and that''s kind of how we",
  "tokens": [50848, 1310, 309, 311, 565, 337, 406, 1466, 281, 457, 12288, 12288, 12288,
  5028, 6545, 293, 300, 311, 733, 295, 577, 321, 51244], "temperature": 0.0, "avg_logprob":
  -0.1449633631212958, "compression_ratio": 1.7416267942583732, "no_speech_prob":
  0.005703783128410578}, {"id": 359, "seek": 247452, "start": 2492.12, "end": 2496.7599999999998,
  "text": " ended up with the hybrid search optimizer right now but I wouldn''t really
  have a good", "tokens": [51244, 4590, 493, 365, 264, 13051, 3164, 5028, 6545, 558,
  586, 457, 286, 2759, 380, 534, 362, 257, 665, 51476], "temperature": 0.0, "avg_logprob":
  -0.1449633631212958, "compression_ratio": 1.7416267942583732, "no_speech_prob":
  0.005703783128410578}, {"id": 360, "seek": 247452, "start": 2497.64, "end": 2503.96,
  "text": " let''s say argument against calling it learning to optimize hybrid search
  or something like that", "tokens": [51520, 718, 311, 584, 6770, 1970, 5141, 309,
  2539, 281, 19719, 13051, 3164, 420, 746, 411, 300, 51836], "temperature": 0.0, "avg_logprob":
  -0.1449633631212958, "compression_ratio": 1.7416267942583732, "no_speech_prob":
  0.005703783128410578}, {"id": 361, "seek": 250396, "start": 2504.36, "end": 2512.2,
  "text": " because that''s kind of what the dynamic approach does right as we gather
  more data more clicks more", "tokens": [50384, 570, 300, 311, 733, 295, 437, 264,
  8546, 3109, 775, 558, 382, 321, 5448, 544, 1412, 544, 18521, 544, 50776], "temperature":
  0.0, "avg_logprob": -0.10012498768893155, "compression_ratio": 1.8483412322274881,
  "no_speech_prob": 0.0012311162427067757}, {"id": 362, "seek": 250396, "start": 2512.2,
  "end": 2518.04, "text": " of that those go into the features right we even use the
  the language of learning to rank right", "tokens": [50776, 295, 300, 729, 352, 666,
  264, 4122, 558, 321, 754, 764, 264, 264, 2856, 295, 2539, 281, 6181, 558, 51068],
  "temperature": 0.0, "avg_logprob": -0.10012498768893155, "compression_ratio": 1.8483412322274881,
  "no_speech_prob": 0.0012311162427067757}, {"id": 363, "seek": 250396, "start": 2518.04,
  "end": 2524.84, "text": " feature engineering right we use that language and we''re
  building a model and you even mention", "tokens": [51068, 4111, 7043, 558, 321,
  764, 300, 2856, 293, 321, 434, 2390, 257, 2316, 293, 291, 754, 2152, 51408], "temperature":
  0.0, "avg_logprob": -0.10012498768893155, "compression_ratio": 1.8483412322274881,
  "no_speech_prob": 0.0012311162427067757}, {"id": 364, "seek": 250396, "start": 2525.4,
  "end": 2532.04, "text": " right linear models in a forest and you know those are
  all the the words that I think of as oh it''s", "tokens": [51436, 558, 8213, 5245,
  294, 257, 6719, 293, 291, 458, 729, 366, 439, 264, 264, 2283, 300, 286, 519, 295,
  382, 1954, 309, 311, 51768], "temperature": 0.0, "avg_logprob": -0.10012498768893155,
  "compression_ratio": 1.8483412322274881, "no_speech_prob": 0.0012311162427067757},
  {"id": 365, "seek": 253204, "start": 2532.04, "end": 2537.64, "text": " learning
  to rank so interesting I think that''s just it''s interesting to see learning to
  rate maybe", "tokens": [50364, 2539, 281, 6181, 370, 1880, 286, 519, 300, 311, 445,
  309, 311, 1880, 281, 536, 2539, 281, 3314, 1310, 50644], "temperature": 0.2, "avg_logprob":
  -0.1863905035931131, "compression_ratio": 1.7557603686635945, "no_speech_prob":
  0.0007230683113448322}, {"id": 366, "seek": 253204, "start": 2537.64, "end": 2544.92,
  "text": " come back in a new way yeah yeah I''m learning to rank still something
  you can apply on top of the", "tokens": [50644, 808, 646, 294, 257, 777, 636, 1338,
  1338, 286, 478, 2539, 281, 6181, 920, 746, 291, 393, 3079, 322, 1192, 295, 264,
  51008], "temperature": 0.2, "avg_logprob": -0.1863905035931131, "compression_ratio":
  1.7557603686635945, "no_speech_prob": 0.0007230683113448322}, {"id": 367, "seek":
  253204, "start": 2544.92, "end": 2553.56, "text": " hybrid search optimizer right
  so it''s not like we have any kind of substitute here so that''s kind", "tokens":
  [51008, 13051, 3164, 5028, 6545, 558, 370, 309, 311, 406, 411, 321, 362, 604, 733,
  295, 15802, 510, 370, 300, 311, 733, 51440], "temperature": 0.2, "avg_logprob":
  -0.1863905035931131, "compression_ratio": 1.7557603686635945, "no_speech_prob":
  0.0007230683113448322}, {"id": 368, "seek": 253204, "start": 2553.56, "end": 2561.08,
  "text": " of still I think a very valuable tool in the mix and that''s just now
  one way to really", "tokens": [51440, 295, 920, 286, 519, 257, 588, 8263, 2290,
  294, 264, 2890, 293, 300, 311, 445, 586, 472, 636, 281, 534, 51816], "temperature":
  0.2, "avg_logprob": -0.1863905035931131, "compression_ratio": 1.7557603686635945,
  "no_speech_prob": 0.0007230683113448322}, {"id": 369, "seek": 256108, "start": 2561.7999999999997,
  "end": 2567.88, "text": " figure out what''s the best way of getting to reasonable
  hybrid search results yeah but I was", "tokens": [50400, 2573, 484, 437, 311, 264,
  1151, 636, 295, 1242, 281, 10585, 13051, 3164, 3542, 1338, 457, 286, 390, 50704],
  "temperature": 0.0, "avg_logprob": -0.1099062442779541, "compression_ratio": 1.722488038277512,
  "no_speech_prob": 0.0013559159124270082}, {"id": 370, "seek": 256108, "start": 2567.88,
  "end": 2571.0, "text": " recently also thinking about this I wonder what''s your
  hunt on that but", "tokens": [50704, 3938, 611, 1953, 466, 341, 286, 2441, 437,
  311, 428, 12454, 322, 300, 457, 50860], "temperature": 0.0, "avg_logprob": -0.1099062442779541,
  "compression_ratio": 1.722488038277512, "no_speech_prob": 0.0013559159124270082},
  {"id": 371, "seek": 256108, "start": 2573.16, "end": 2579.88, "text": " learning
  to rank sort of depends on the training data and you usually collected from the
  past you", "tokens": [50968, 2539, 281, 6181, 1333, 295, 5946, 322, 264, 3097, 1412,
  293, 291, 2673, 11087, 490, 264, 1791, 291, 51304], "temperature": 0.0, "avg_logprob":
  -0.1099062442779541, "compression_ratio": 1.722488038277512, "no_speech_prob": 0.0013559159124270082},
  {"id": 372, "seek": 256108, "start": 2579.88, "end": 2586.2799999999997, "text":
  " don''t collect it from the future right and so as you move into the future and
  patterns change you", "tokens": [51304, 500, 380, 2500, 309, 490, 264, 2027, 558,
  293, 370, 382, 291, 1286, 666, 264, 2027, 293, 8294, 1319, 291, 51624], "temperature":
  0.0, "avg_logprob": -0.1099062442779541, "compression_ratio": 1.722488038277512,
  "no_speech_prob": 0.0013559159124270082}, {"id": 373, "seek": 258628, "start": 2586.28,
  "end": 2593.5600000000004, "text": " carry over that past weight that can actually
  go against the intent of your reasoning engine and", "tokens": [50364, 3985, 670,
  300, 1791, 3364, 300, 393, 767, 352, 1970, 264, 8446, 295, 428, 21577, 2848, 293,
  50728], "temperature": 0.0, "avg_logprob": -0.08094951718352562, "compression_ratio":
  1.7272727272727273, "no_speech_prob": 0.007452432997524738}, {"id": 374, "seek":
  258628, "start": 2593.5600000000004, "end": 2600.36, "text": " and that''s where
  I think that a lot of work needs to go in all of these directions but as you", "tokens":
  [50728, 293, 300, 311, 689, 286, 519, 300, 257, 688, 295, 589, 2203, 281, 352, 294,
  439, 295, 613, 11095, 457, 382, 291, 51068], "temperature": 0.0, "avg_logprob":
  -0.08094951718352562, "compression_ratio": 1.7272727272727273, "no_speech_prob":
  0.007452432997524738}, {"id": 375, "seek": 258628, "start": 2600.36, "end": 2606.2000000000003,
  "text": " optimize your retrieving and your reasoning engine you know your query
  understanding maybe you", "tokens": [51068, 19719, 428, 19817, 798, 293, 428, 21577,
  2848, 291, 458, 428, 14581, 3701, 1310, 291, 51360], "temperature": 0.0, "avg_logprob":
  -0.08094951718352562, "compression_ratio": 1.7272727272727273, "no_speech_prob":
  0.007452432997524738}, {"id": 376, "seek": 258628, "start": 2606.2000000000003,
  "end": 2612.0400000000004, "text": " should dial back the LTR a little bit or maybe
  you need to retrain it right there right then I", "tokens": [51360, 820, 5502, 646,
  264, 441, 25936, 257, 707, 857, 420, 1310, 291, 643, 281, 1533, 7146, 309, 558,
  456, 558, 550, 286, 51652], "temperature": 0.0, "avg_logprob": -0.08094951718352562,
  "compression_ratio": 1.7272727272727273, "no_speech_prob": 0.007452432997524738},
  {"id": 377, "seek": 261204, "start": 2612.04, "end": 2621.4, "text": " don''t know
  or retrain frequently enough so that you don''t lose the invention strengths right
  yeah", "tokens": [50364, 500, 380, 458, 420, 1533, 7146, 10374, 1547, 370, 300,
  291, 500, 380, 3624, 264, 22265, 16986, 558, 1338, 50832], "temperature": 0.0, "avg_logprob":
  -0.1083514844217608, "compression_ratio": 1.6416184971098267, "no_speech_prob":
  0.0012699058279395103}, {"id": 378, "seek": 261204, "start": 2621.64, "end": 2628.2799999999997,
  "text": " I think that''s our challenge in a lot of these things yeah the historical
  approaches versus the", "tokens": [50844, 286, 519, 300, 311, 527, 3430, 294, 257,
  688, 295, 613, 721, 1338, 264, 8584, 11587, 5717, 264, 51176], "temperature": 0.0,
  "avg_logprob": -0.1083514844217608, "compression_ratio": 1.6416184971098267, "no_speech_prob":
  0.0012699058279395103}, {"id": 379, "seek": 261204, "start": 2628.2799999999997,
  "end": 2637.32, "text": " predictive approaches right and you know which ones do
  you go with and how do you discount", "tokens": [51176, 35521, 11587, 558, 293,
  291, 458, 597, 2306, 360, 291, 352, 365, 293, 577, 360, 291, 11635, 51628], "temperature":
  0.0, "avg_logprob": -0.1083514844217608, "compression_ratio": 1.6416184971098267,
  "no_speech_prob": 0.0012699058279395103}, {"id": 380, "seek": 263732, "start": 2637.32,
  "end": 2644.2000000000003, "text": " the historical if you have a bunch of new interesting
  data yeah yeah but I also like the limitations", "tokens": [50364, 264, 8584, 498,
  291, 362, 257, 3840, 295, 777, 1880, 1412, 1338, 1338, 457, 286, 611, 411, 264,
  15705, 50708], "temperature": 0.0, "avg_logprob": -0.09566466779593961, "compression_ratio":
  1.6651982378854626, "no_speech_prob": 0.0058951606042683125}, {"id": 381, "seek":
  263732, "start": 2644.2000000000003, "end": 2652.6800000000003, "text": " of the
  physical world I think from investment books I''ve read one key key takeaway lesson
  is that", "tokens": [50708, 295, 264, 4001, 1002, 286, 519, 490, 6078, 3642, 286,
  600, 1401, 472, 2141, 2141, 30681, 6898, 307, 300, 51132], "temperature": 0.0, "avg_logprob":
  -0.09566466779593961, "compression_ratio": 1.6651982378854626, "no_speech_prob":
  0.0058951606042683125}, {"id": 382, "seek": 263732, "start": 2652.6800000000003,
  "end": 2657.56, "text": " no one can predict the future if someone claims that they
  can do they probably lie", "tokens": [51132, 572, 472, 393, 6069, 264, 2027, 498,
  1580, 9441, 300, 436, 393, 360, 436, 1391, 4544, 51376], "temperature": 0.0, "avg_logprob":
  -0.09566466779593961, "compression_ratio": 1.6651982378854626, "no_speech_prob":
  0.0058951606042683125}, {"id": 383, "seek": 263732, "start": 2659.4, "end": 2665.2400000000002,
  "text": " but but again I guess there is still room for being more dynamic and is
  there something you guys", "tokens": [51468, 457, 457, 797, 286, 2041, 456, 307,
  920, 1808, 337, 885, 544, 8546, 293, 307, 456, 746, 291, 1074, 51760], "temperature":
  0.0, "avg_logprob": -0.09566466779593961, "compression_ratio": 1.6651982378854626,
  "no_speech_prob": 0.0058951606042683125}, {"id": 384, "seek": 266524, "start": 2665.24,
  "end": 2670.12, "text": " want to also show I mean is this something we can look
  at visually or", "tokens": [50364, 528, 281, 611, 855, 286, 914, 307, 341, 746,
  321, 393, 574, 412, 19622, 420, 50608], "temperature": 0.0, "avg_logprob": -0.15950644400811964,
  "compression_ratio": 1.6226415094339623, "no_speech_prob": 0.001306170946918428},
  {"id": 385, "seek": 266524, "start": 2673.24, "end": 2683.56, "text": " well theoretically
  we can no pressure I mean so this small demo here and I''m going to show the", "tokens":
  [50764, 731, 29400, 321, 393, 572, 3321, 286, 914, 370, 341, 1359, 10723, 510, 293,
  286, 478, 516, 281, 855, 264, 51280], "temperature": 0.0, "avg_logprob": -0.15950644400811964,
  "compression_ratio": 1.6226415094339623, "no_speech_prob": 0.001306170946918428},
  {"id": 386, "seek": 266524, "start": 2683.56, "end": 2692.2, "text": " results first
  and then how we get to these results it basically takes in a user query my such",
  "tokens": [51280, 3542, 700, 293, 550, 577, 321, 483, 281, 613, 3542, 309, 1936,
  2516, 294, 257, 4195, 14581, 452, 1270, 51712], "temperature": 0.0, "avg_logprob":
  -0.15950644400811964, "compression_ratio": 1.6226415094339623, "no_speech_prob":
  0.001306170946918428}, {"id": 387, "seek": 269220, "start": 2692.2, "end": 2697.96,
  "text": " application now is this Jupyter Notebook so it''s not the most sophisticated
  search application", "tokens": [50364, 3861, 586, 307, 341, 22125, 88, 391, 11633,
  2939, 370, 309, 311, 406, 264, 881, 16950, 3164, 3861, 50652], "temperature": 0.0,
  "avg_logprob": -0.14665975878315587, "compression_ratio": 1.7409638554216869, "no_speech_prob":
  0.00034268011222593486}, {"id": 388, "seek": 269220, "start": 2698.68, "end": 2706.04,
  "text": " but it calculates the query features then with these query features reaches
  out to the model to", "tokens": [50688, 457, 309, 4322, 1024, 264, 14581, 4122,
  550, 365, 613, 14581, 4122, 14235, 484, 281, 264, 2316, 281, 51056], "temperature":
  0.0, "avg_logprob": -0.14665975878315587, "compression_ratio": 1.7409638554216869,
  "no_speech_prob": 0.00034268011222593486}, {"id": 389, "seek": 269220, "start":
  2706.04, "end": 2716.2, "text": " get the the best neural nest what these search
  features and with that retrieved response the query", "tokens": [51056, 483, 264,
  264, 1151, 18161, 15646, 437, 613, 3164, 4122, 293, 365, 300, 19817, 937, 4134,
  264, 14581, 51564], "temperature": 0.0, "avg_logprob": -0.14665975878315587, "compression_ratio":
  1.7409638554216869, "no_speech_prob": 0.00034268011222593486}, {"id": 390, "seek":
  271620, "start": 2716.2, "end": 2724.52, "text": " is built together and then sent
  to open search so we''re just going to have a look at a couple of", "tokens": [50364,
  307, 3094, 1214, 293, 550, 2279, 281, 1269, 3164, 370, 321, 434, 445, 516, 281,
  362, 257, 574, 412, 257, 1916, 295, 50780], "temperature": 0.0, "avg_logprob": -0.13025188446044922,
  "compression_ratio": 1.5668449197860963, "no_speech_prob": 0.0020670457743108273},
  {"id": 391, "seek": 271620, "start": 2724.52, "end": 2731.48, "text": " examples
  first and then we can have a look at the code so again this is now part of the ESC
  iData", "tokens": [50780, 5110, 700, 293, 550, 321, 393, 362, 257, 574, 412, 264,
  3089, 370, 797, 341, 307, 586, 644, 295, 264, 12564, 34, 741, 35, 3274, 51128],
  "temperature": 0.0, "avg_logprob": -0.13025188446044922, "compression_ratio": 1.5668449197860963,
  "no_speech_prob": 0.0020670457743108273}, {"id": 392, "seek": 271620, "start": 2731.48,
  "end": 2738.68, "text": " set my index has like 20,000 documents in it so it''s
  not large it''s only a subset of the ESC iData", "tokens": [51128, 992, 452, 8186,
  575, 411, 945, 11, 1360, 8512, 294, 309, 370, 309, 311, 406, 2416, 309, 311, 787,
  257, 25993, 295, 264, 12564, 34, 741, 35, 3274, 51488], "temperature": 0.0, "avg_logprob":
  -0.13025188446044922, "compression_ratio": 1.5668449197860963, "no_speech_prob":
  0.0020670457743108273}, {"id": 393, "seek": 273868, "start": 2739.64, "end": 2749.72,
  "text": " and when we send queries now in this case waterproof jacket in this method
  the method first as I", "tokens": [50412, 293, 562, 321, 2845, 24109, 586, 294,
  341, 1389, 27974, 11781, 294, 341, 3170, 264, 3170, 700, 382, 286, 50916], "temperature":
  0.0, "avg_logprob": -0.12327960087702824, "compression_ratio": 1.5806451612903225,
  "no_speech_prob": 0.002759872004389763}, {"id": 394, "seek": 273868, "start": 2749.72,
  "end": 2759.0, "text": " just explained cause out to the model it retrieves the
  neural nest score and then builds the query", "tokens": [50916, 445, 8825, 3082,
  484, 281, 264, 2316, 309, 19817, 977, 264, 18161, 15646, 6175, 293, 550, 15182,
  264, 14581, 51380], "temperature": 0.0, "avg_logprob": -0.12327960087702824, "compression_ratio":
  1.5806451612903225, "no_speech_prob": 0.002759872004389763}, {"id": 395, "seek":
  273868, "start": 2759.0, "end": 2766.3599999999997, "text": " together and then
  we have this HTML display here as you can see there are not images available for",
  "tokens": [51380, 1214, 293, 550, 321, 362, 341, 17995, 4674, 510, 382, 291, 393,
  536, 456, 366, 406, 5267, 2435, 337, 51748], "temperature": 0.0, "avg_logprob":
  -0.12327960087702824, "compression_ratio": 1.5806451612903225, "no_speech_prob":
  0.002759872004389763}, {"id": 396, "seek": 276636, "start": 2766.36, "end": 2773.88,
  "text": " all of the products but what we can see here is that what a weatherproof
  sorry weatherproof jacket", "tokens": [50364, 439, 295, 264, 3383, 457, 437, 321,
  393, 536, 510, 307, 300, 437, 257, 5503, 15690, 2597, 5503, 15690, 11781, 50740],
  "temperature": 0.0, "avg_logprob": -0.19228851318359375, "compression_ratio": 1.4848484848484849,
  "no_speech_prob": 0.0024820754770189524}, {"id": 397, "seek": 276636, "start": 2774.84,
  "end": 2784.84, "text": " it gets a 50-50 search waiting also in this case 50% keyword
  50% neural if we go for weatherproof", "tokens": [50788, 309, 2170, 257, 2625, 12,
  2803, 3164, 3806, 611, 294, 341, 1389, 2625, 4, 20428, 2625, 4, 18161, 498, 321,
  352, 337, 5503, 15690, 51288], "temperature": 0.0, "avg_logprob": -0.19228851318359375,
  "compression_ratio": 1.4848484848484849, "no_speech_prob": 0.0024820754770189524},
  {"id": 398, "seek": 278484, "start": 2784.84, "end": 2796.52, "text": " jacket for
  the women the weights change so now we have 90% neural and only 10% keyword search
  weight", "tokens": [50364, 11781, 337, 264, 2266, 264, 17443, 1319, 370, 586, 321,
  362, 4289, 4, 18161, 293, 787, 1266, 4, 20428, 3164, 3364, 50948], "temperature":
  0.0, "avg_logprob": -0.16628310259650736, "compression_ratio": 1.6032608695652173,
  "no_speech_prob": 0.015731146559119225}, {"id": 399, "seek": 278484, "start": 2797.08,
  "end": 2803.08, "text": " and then oh and that''s because the query became much
  more specific meaning that since we did add", "tokens": [50976, 293, 550, 1954,
  293, 300, 311, 570, 264, 14581, 3062, 709, 544, 2685, 3620, 300, 1670, 321, 630,
  909, 51276], "temperature": 0.0, "avg_logprob": -0.16628310259650736, "compression_ratio":
  1.6032608695652173, "no_speech_prob": 0.015731146559119225}, {"id": 400, "seek":
  278484, "start": 2803.08, "end": 2809.32, "text": " women there we are not expecting
  results for men or for kids right is that exactly so that''s kind", "tokens": [51276,
  2266, 456, 321, 366, 406, 9650, 3542, 337, 1706, 420, 337, 2301, 558, 307, 300,
  2293, 370, 300, 311, 733, 51588], "temperature": 0.0, "avg_logprob": -0.16628310259650736,
  "compression_ratio": 1.6032608695652173, "no_speech_prob": 0.015731146559119225},
  {"id": 401, "seek": 280932, "start": 2809.32, "end": 2815.4, "text": " of what we
  can now infer maybe in what the model picks up here so we have a longer query we
  have a", "tokens": [50364, 295, 437, 321, 393, 586, 13596, 1310, 294, 437, 264,
  2316, 16137, 493, 510, 370, 321, 362, 257, 2854, 14581, 321, 362, 257, 50668], "temperature":
  0.0, "avg_logprob": -0.10824088428331458, "compression_ratio": 1.7873303167420815,
  "no_speech_prob": 0.0033873342908918858}, {"id": 402, "seek": 280932, "start": 2815.4,
  "end": 2821.6400000000003, "text": " more specific query so it''s not really looking
  at the words I''ll say the model but at the features like", "tokens": [50668, 544,
  2685, 14581, 370, 309, 311, 406, 534, 1237, 412, 264, 2283, 286, 603, 584, 264,
  2316, 457, 412, 264, 4122, 411, 50980], "temperature": 0.0, "avg_logprob": -0.10824088428331458,
  "compression_ratio": 1.7873303167420815, "no_speech_prob": 0.0033873342908918858},
  {"id": 403, "seek": 280932, "start": 2821.6400000000003, "end": 2829.0800000000004,
  "text": " query length are there numbers in it are there any special characters
  in it and so on so another one", "tokens": [50980, 14581, 4641, 366, 456, 3547,
  294, 309, 366, 456, 604, 2121, 4342, 294, 309, 293, 370, 322, 370, 1071, 472, 51352],
  "temperature": 0.0, "avg_logprob": -0.10824088428331458, "compression_ratio": 1.7873303167420815,
  "no_speech_prob": 0.0033873342908918858}, {"id": 404, "seek": 280932, "start": 2829.0800000000004,
  "end": 2834.84, "text": " weatherproof jacket black and we also see that maybe results
  that we wouldn''t really expect", "tokens": [51352, 5503, 15690, 11781, 2211, 293,
  321, 611, 536, 300, 1310, 3542, 300, 321, 2759, 380, 534, 2066, 51640], "temperature":
  0.0, "avg_logprob": -0.10824088428331458, "compression_ratio": 1.7873303167420815,
  "no_speech_prob": 0.0033873342908918858}, {"id": 405, "seek": 283484, "start": 2835.0,
  "end": 2841.56, "text": " in the top here but again it''s only a smallish proof
  of concept kind of thing that we are looking at", "tokens": [50372, 294, 264, 1192,
  510, 457, 797, 309, 311, 787, 257, 1359, 742, 8177, 295, 3410, 733, 295, 551, 300,
  321, 366, 1237, 412, 50700], "temperature": 0.0, "avg_logprob": -0.17334971708409927,
  "compression_ratio": 1.6779661016949152, "no_speech_prob": 0.0023127684835344553},
  {"id": 406, "seek": 283484, "start": 2841.56, "end": 2849.1600000000003, "text":
  " here but we can see different queries that are similar from let''s say meanings
  standpoint of you", "tokens": [50700, 510, 457, 321, 393, 536, 819, 24109, 300,
  366, 2531, 490, 718, 311, 584, 28138, 15827, 295, 291, 51080], "temperature": 0.0,
  "avg_logprob": -0.17334971708409927, "compression_ratio": 1.6779661016949152, "no_speech_prob":
  0.0023127684835344553}, {"id": 407, "seek": 283484, "start": 2849.8, "end": 2857.4,
  "text": " they retrieve different weights in that case and that''s kind of the interesting
  thing and we can go", "tokens": [51112, 436, 30254, 819, 17443, 294, 300, 1389,
  293, 300, 311, 733, 295, 264, 1880, 551, 293, 321, 393, 352, 51492], "temperature":
  0.0, "avg_logprob": -0.17334971708409927, "compression_ratio": 1.6779661016949152,
  "no_speech_prob": 0.0023127684835344553}, {"id": 408, "seek": 285740, "start": 2857.48,
  "end": 2868.12, "text": " for something completely different as well um iPhone case
  and we see like nice iPhone cases", "tokens": [50368, 337, 746, 2584, 819, 382,
  731, 1105, 7252, 1389, 293, 321, 536, 411, 1481, 7252, 3331, 50900], "temperature":
  0.0, "avg_logprob": -0.2702459971110026, "compression_ratio": 1.364963503649635,
  "no_speech_prob": 0.0014275498688220978}, {"id": 409, "seek": 285740, "start": 2868.92,
  "end": 2879.56, "text": " throughout the query and that goes with neuro.7 and keyword.3
  and I don''t know what''s iPhone 15", "tokens": [50940, 3710, 264, 14581, 293, 300,
  1709, 365, 16499, 13, 22, 293, 20428, 13, 18, 293, 286, 500, 380, 458, 437, 311,
  7252, 2119, 51472], "temperature": 0.0, "avg_logprob": -0.2702459971110026, "compression_ratio":
  1.364963503649635, "no_speech_prob": 0.0014275498688220978}, {"id": 410, "seek":
  287956, "start": 2880.2799999999997, "end": 2890.84, "text": " roll max a is black
  so that would be a very very very specific query and here again the", "tokens":
  [50400, 3373, 11469, 257, 307, 2211, 370, 300, 576, 312, 257, 588, 588, 588, 2685,
  14581, 293, 510, 797, 264, 50928], "temperature": 0.0, "avg_logprob": -0.23271123824581022,
  "compression_ratio": 1.6645962732919255, "no_speech_prob": 0.0011124081211164594},
  {"id": 411, "seek": 287956, "start": 2890.84, "end": 2897.48, "text": " neural search
  rate increases whereas when we go for a very broad query so that''s maybe one",
  "tokens": [50928, 18161, 3164, 3314, 8637, 9735, 562, 321, 352, 337, 257, 588, 4152,
  14581, 370, 300, 311, 1310, 472, 51260], "temperature": 0.0, "avg_logprob": -0.23271123824581022,
  "compression_ratio": 1.6645962732919255, "no_speech_prob": 0.0011124081211164594},
  {"id": 412, "seek": 287956, "start": 2899.24, "end": 2905.48, "text": " characteristic
  of the model that you that you can almost feel is the more specific we get", "tokens":
  [51348, 16282, 295, 264, 2316, 300, 291, 300, 291, 393, 1920, 841, 307, 264, 544,
  2685, 321, 483, 51660], "temperature": 0.0, "avg_logprob": -0.23271123824581022,
  "compression_ratio": 1.6645962732919255, "no_speech_prob": 0.0011124081211164594},
  {"id": 413, "seek": 290548, "start": 2905.96, "end": 2911.88, "text": " the more
  neural weight it gets but also other features do play a role.", "tokens": [50388,
  264, 544, 18161, 3364, 309, 2170, 457, 611, 661, 4122, 360, 862, 257, 3090, 13,
  50684], "temperature": 0.0, "avg_logprob": -0.1436357810849049, "compression_ratio":
  1.5515151515151515, "no_speech_prob": 0.00042315831524319947}, {"id": 414, "seek":
  290548, "start": 2912.76, "end": 2922.36, "text": " Yeah yeah that''s very interesting
  and that''s how the open search query looks like so let''s say", "tokens": [50728,
  865, 1338, 300, 311, 588, 1880, 293, 300, 311, 577, 264, 1269, 3164, 14581, 1542,
  411, 370, 718, 311, 584, 51208], "temperature": 0.0, "avg_logprob": -0.1436357810849049,
  "compression_ratio": 1.5515151515151515, "no_speech_prob": 0.00042315831524319947},
  {"id": 415, "seek": 290548, "start": 2922.36, "end": 2931.48, "text": " the interesting
  part is that one here so we have a keyword query which is like I explained", "tokens":
  [51208, 264, 1880, 644, 307, 300, 472, 510, 370, 321, 362, 257, 20428, 14581, 597,
  307, 411, 286, 8825, 51664], "temperature": 0.0, "avg_logprob": -0.1436357810849049,
  "compression_ratio": 1.5515151515151515, "no_speech_prob": 0.00042315831524319947},
  {"id": 416, "seek": 293148, "start": 2931.48, "end": 2937.32, "text": " before searching
  in these couple of fields with different field weights a best fields query", "tokens":
  [50364, 949, 10808, 294, 613, 1916, 295, 7909, 365, 819, 2519, 17443, 257, 1151,
  7909, 14581, 50656], "temperature": 0.0, "avg_logprob": -0.17114732265472413, "compression_ratio":
  1.7061611374407584, "no_speech_prob": 0.0001779366284608841}, {"id": 417, "seek":
  293148, "start": 2937.88, "end": 2943.56, "text": " multi match with the end operator
  and then we have a neural query that retrieves the", "tokens": [50684, 4825, 2995,
  365, 264, 917, 12973, 293, 550, 321, 362, 257, 18161, 14581, 300, 19817, 977, 264,
  50968], "temperature": 0.0, "avg_logprob": -0.17114732265472413, "compression_ratio":
  1.7061611374407584, "no_speech_prob": 0.0001779366284608841}, {"id": 418, "seek":
  293148, "start": 2944.68, "end": 2950.84, "text": " A100 based on the title embedding
  that we have and then the hybrid part is actually the", "tokens": [51024, 316, 6879,
  2361, 322, 264, 4876, 12240, 3584, 300, 321, 362, 293, 550, 264, 13051, 644, 307,
  767, 264, 51332], "temperature": 0.0, "avg_logprob": -0.17114732265472413, "compression_ratio":
  1.7061611374407584, "no_speech_prob": 0.0001779366284608841}, {"id": 419, "seek":
  293148, "start": 2950.84, "end": 2958.36, "text": " search pipeline that normalizes
  in this case with the L2 norm and combines the results with the", "tokens": [51332,
  3164, 15517, 300, 2710, 5660, 294, 341, 1389, 365, 264, 441, 17, 2026, 293, 29520,
  264, 3542, 365, 264, 51708], "temperature": 0.0, "avg_logprob": -0.17114732265472413,
  "compression_ratio": 1.7061611374407584, "no_speech_prob": 0.0001779366284608841},
  {"id": 420, "seek": 295836, "start": 2958.36, "end": 2964.76, "text": " arithmetic
  mean based on the keyword search rate and neural search rate and that are here",
  "tokens": [50364, 42973, 914, 2361, 322, 264, 20428, 3164, 3314, 293, 18161, 3164,
  3314, 293, 300, 366, 510, 50684], "temperature": 0.0, "avg_logprob": -0.1950115849894862,
  "compression_ratio": 1.5625, "no_speech_prob": 0.00012403786240611225}, {"id": 421,
  "seek": 295836, "start": 2964.76, "end": 2972.2000000000003, "text": " passed in
  as variables that are another method yeah predicts with model inference in that
  case.", "tokens": [50684, 4678, 294, 382, 9102, 300, 366, 1071, 3170, 1338, 6069,
  82, 365, 2316, 38253, 294, 300, 1389, 13, 51056], "temperature": 0.0, "avg_logprob":
  -0.1950115849894862, "compression_ratio": 1.5625, "no_speech_prob": 0.00012403786240611225},
  {"id": 422, "seek": 295836, "start": 2975.0, "end": 2985.32, "text": " Yeah that''s
  that''s kind of the small but built in Jupyter notebook prototype that we have",
  "tokens": [51196, 865, 300, 311, 300, 311, 733, 295, 264, 1359, 457, 3094, 294,
  22125, 88, 391, 21060, 19475, 300, 321, 362, 51712], "temperature": 0.0, "avg_logprob":
  -0.1950115849894862, "compression_ratio": 1.5625, "no_speech_prob": 0.00012403786240611225},
  {"id": 423, "seek": 298532, "start": 2986.28, "end": 2993.4, "text": " everything
  we built is like Eric just mentioned open source so we have a public repository
  that", "tokens": [50412, 1203, 321, 3094, 307, 411, 9336, 445, 2835, 1269, 4009,
  370, 321, 362, 257, 1908, 25841, 300, 50768], "temperature": 0.0, "avg_logprob":
  -0.1696358228984632, "compression_ratio": 1.6367713004484306, "no_speech_prob":
  0.0016907332465052605}, {"id": 424, "seek": 298532, "start": 2993.4, "end": 2999.7200000000003,
  "text": " contains all but this one notebook actually but everything you need to
  train the models", "tokens": [50768, 8306, 439, 457, 341, 472, 21060, 767, 457,
  1203, 291, 643, 281, 3847, 264, 5245, 51084], "temperature": 0.0, "avg_logprob":
  -0.1696358228984632, "compression_ratio": 1.6367713004484306, "no_speech_prob":
  0.0016907332465052605}, {"id": 425, "seek": 298532, "start": 3000.44, "end": 3007.88,
  "text": " do the feature engineering calculate the search metrics so yeah everything
  you actually need so", "tokens": [51120, 360, 264, 4111, 7043, 8873, 264, 3164,
  16367, 370, 1338, 1203, 291, 767, 643, 370, 51492], "temperature": 0.0, "avg_logprob":
  -0.1696358228984632, "compression_ratio": 1.6367713004484306, "no_speech_prob":
  0.0016907332465052605}, {"id": 426, "seek": 298532, "start": 3007.88, "end": 3014.52,
  "text": " running this with the ESC IDATA set is possible for everyone and if you
  want to apply", "tokens": [51492, 2614, 341, 365, 264, 12564, 34, 7348, 44811, 992,
  307, 1944, 337, 1518, 293, 498, 291, 528, 281, 3079, 51824], "temperature": 0.0,
  "avg_logprob": -0.1696358228984632, "compression_ratio": 1.6367713004484306, "no_speech_prob":
  0.0016907332465052605}, {"id": 427, "seek": 301452, "start": 3014.6, "end": 3020.7599999999998,
  "text": " with your own data that of course is also possible so that''s kind of
  what we are looking at next", "tokens": [50368, 365, 428, 1065, 1412, 300, 295,
  1164, 307, 611, 1944, 370, 300, 311, 733, 295, 437, 321, 366, 1237, 412, 958, 50676],
  "temperature": 0.0, "avg_logprob": -0.11262814203898112, "compression_ratio": 1.6,
  "no_speech_prob": 0.0009003984159789979}, {"id": 428, "seek": 301452, "start": 3020.7599999999998,
  "end": 3030.04, "text": " here so adoption in the industry and also hooking it up
  with the other part of this project which is", "tokens": [50676, 510, 370, 19215,
  294, 264, 3518, 293, 611, 1106, 5953, 309, 493, 365, 264, 661, 644, 295, 341, 1716,
  597, 307, 51140], "temperature": 0.0, "avg_logprob": -0.11262814203898112, "compression_ratio":
  1.6, "no_speech_prob": 0.0009003984159789979}, {"id": 429, "seek": 301452, "start":
  3030.04, "end": 3039.08, "text": " namely the let''s call it the evaluation part
  calculating implicit judgments based on user feedback", "tokens": [51140, 20926,
  264, 718, 311, 818, 309, 264, 13344, 644, 28258, 26947, 40337, 2361, 322, 4195,
  5824, 51592], "temperature": 0.0, "avg_logprob": -0.11262814203898112, "compression_ratio":
  1.6, "no_speech_prob": 0.0009003984159789979}, {"id": 430, "seek": 303908, "start":
  3039.16, "end": 3046.92, "text": " so clicks queries stuff like that so that we
  also enable not only everyone to optimize hybrid", "tokens": [50368, 370, 18521,
  24109, 1507, 411, 300, 370, 300, 321, 611, 9528, 406, 787, 1518, 281, 19719, 13051,
  50756], "temperature": 0.0, "avg_logprob": -0.1788503646850586, "compression_ratio":
  1.5988700564971752, "no_speech_prob": 0.005032109096646309}, {"id": 431, "seek":
  303908, "start": 3046.92, "end": 3053.72, "text": " search but also enable and empower
  everyone to well come up with judgments if you don''t have any", "tokens": [50756,
  3164, 457, 611, 9528, 293, 11071, 1518, 281, 731, 808, 493, 365, 40337, 498, 291,
  500, 380, 362, 604, 51096], "temperature": 0.0, "avg_logprob": -0.1788503646850586,
  "compression_ratio": 1.5988700564971752, "no_speech_prob": 0.005032109096646309},
  {"id": 432, "seek": 303908, "start": 3053.72, "end": 3060.52, "text": " because
  that''s kind of the the basics you need for any query you need. Yeah and that''s
  where", "tokens": [51096, 570, 300, 311, 733, 295, 264, 264, 14688, 291, 643, 337,
  604, 14581, 291, 643, 13, 865, 293, 300, 311, 689, 51436], "temperature": 0.0, "avg_logprob":
  -0.1788503646850586, "compression_ratio": 1.5988700564971752, "no_speech_prob":
  0.005032109096646309}, {"id": 433, "seek": 306052, "start": 3060.6, "end": 3069.96,
  "text": " keep it comes in. Shameless flag. So one of the things we actually have
  a reference implementation", "tokens": [50368, 1066, 309, 1487, 294, 13, 42912,
  4272, 7166, 13, 407, 472, 295, 264, 721, 321, 767, 362, 257, 6408, 11420, 50836],
  "temperature": 0.0, "avg_logprob": -0.1594693258907018, "compression_ratio": 1.7443946188340806,
  "no_speech_prob": 0.0019274278311058879}, {"id": 434, "seek": 306052, "start": 3069.96,
  "end": 3074.6, "text": " you know some of you all may have heard of chorus which
  is reference implementation for e-commerce", "tokens": [50836, 291, 458, 512, 295,
  291, 439, 815, 362, 2198, 295, 22632, 597, 307, 6408, 11420, 337, 308, 12, 26926,
  51068], "temperature": 0.0, "avg_logprob": -0.1594693258907018, "compression_ratio":
  1.7443946188340806, "no_speech_prob": 0.0019274278311058879}, {"id": 435, "seek":
  306052, "start": 3074.6, "end": 3080.84, "text": " search we did it in solar this
  we have an open search version and some of the stuff that you''re", "tokens": [51068,
  3164, 321, 630, 309, 294, 7936, 341, 321, 362, 364, 1269, 3164, 3037, 293, 512,
  295, 264, 1507, 300, 291, 434, 51380], "temperature": 0.0, "avg_logprob": -0.1594693258907018,
  "compression_ratio": 1.7443946188340806, "no_speech_prob": 0.0019274278311058879},
  {"id": 436, "seek": 306052, "start": 3080.84, "end": 3086.84, "text": " seeing is
  sort of bleeding edge hot off the presses but we''re working right now on getting
  that", "tokens": [51380, 2577, 307, 1333, 295, 19312, 4691, 2368, 766, 264, 40892,
  457, 321, 434, 1364, 558, 586, 322, 1242, 300, 51680], "temperature": 0.0, "avg_logprob":
  -0.1594693258907018, "compression_ratio": 1.7443946188340806, "no_speech_prob":
  0.0019274278311058879}, {"id": 437, "seek": 308684, "start": 3086.84, "end": 3093.8,
  "text": " chorus for open search edition updated with some of these scripts and
  notebooks so you can just", "tokens": [50364, 22632, 337, 1269, 3164, 11377, 10588,
  365, 512, 295, 613, 23294, 293, 43782, 370, 291, 393, 445, 50712], "temperature":
  0.0, "avg_logprob": -0.13832103941175672, "compression_ratio": 1.7085201793721974,
  "no_speech_prob": 0.001251386129297316}, {"id": 438, "seek": 308684, "start": 3093.8,
  "end": 3098.6800000000003, "text": " check it out run the quick start and then have
  everything and start playing with it so you don''t", "tokens": [50712, 1520, 309,
  484, 1190, 264, 1702, 722, 293, 550, 362, 1203, 293, 722, 2433, 365, 309, 370, 291,
  500, 380, 50956], "temperature": 0.0, "avg_logprob": -0.13832103941175672, "compression_ratio":
  1.7085201793721974, "no_speech_prob": 0.001251386129297316}, {"id": 439, "seek":
  308684, "start": 3098.6800000000003, "end": 3106.36, "text": " have to build all
  the steps yourself so you can see how all the pieces fit together and so that''s",
  "tokens": [50956, 362, 281, 1322, 439, 264, 4439, 1803, 370, 291, 393, 536, 577,
  439, 264, 3755, 3318, 1214, 293, 370, 300, 311, 51340], "temperature": 0.0, "avg_logprob":
  -0.13832103941175672, "compression_ratio": 1.7085201793721974, "no_speech_prob":
  0.001251386129297316}, {"id": 440, "seek": 308684, "start": 3106.36, "end": 3111.0,
  "text": " available be great if we can add a link in the line or notes for that
  as well to meet you.", "tokens": [51340, 2435, 312, 869, 498, 321, 393, 909, 257,
  2113, 294, 264, 1622, 420, 5570, 337, 300, 382, 731, 281, 1677, 291, 13, 51572],
  "temperature": 0.0, "avg_logprob": -0.13832103941175672, "compression_ratio": 1.7085201793721974,
  "no_speech_prob": 0.001251386129297316}, {"id": 441, "seek": 311100, "start": 3111.08,
  "end": 3116.68, "text": " Yeah let''s do that and just want to also to understand
  this search pipeline and all this you know", "tokens": [50368, 865, 718, 311, 360,
  300, 293, 445, 528, 281, 611, 281, 1223, 341, 3164, 15517, 293, 439, 341, 291, 458,
  50648], "temperature": 0.0, "avg_logprob": -0.1607085197202621, "compression_ratio":
  1.7321428571428572, "no_speech_prob": 0.007830423302948475}, {"id": 442, "seek":
  311100, "start": 3116.68, "end": 3123.0, "text": " mechanics of hybrid search that
  you guys implemented is it like a plugin to open search and what''s", "tokens":
  [50648, 12939, 295, 13051, 3164, 300, 291, 1074, 12270, 307, 309, 411, 257, 23407,
  281, 1269, 3164, 293, 437, 311, 50964], "temperature": 0.0, "avg_logprob": -0.1607085197202621,
  "compression_ratio": 1.7321428571428572, "no_speech_prob": 0.007830423302948475},
  {"id": 443, "seek": 311100, "start": 3123.0, "end": 3129.08, "text": " the plan
  for it right so I guess you spoke to that like let''s let''s give it to as many
  users as", "tokens": [50964, 264, 1393, 337, 309, 558, 370, 286, 2041, 291, 7179,
  281, 300, 411, 718, 311, 718, 311, 976, 309, 281, 382, 867, 5022, 382, 51268], "temperature":
  0.0, "avg_logprob": -0.1607085197202621, "compression_ratio": 1.7321428571428572,
  "no_speech_prob": 0.007830423302948475}, {"id": 444, "seek": 311100, "start": 3129.08,
  "end": 3139.24, "text": " possible what''s your idea there. So hybrid search is
  available in open search so with let''s say", "tokens": [51268, 1944, 437, 311,
  428, 1558, 456, 13, 407, 13051, 3164, 307, 2435, 294, 1269, 3164, 370, 365, 718,
  311, 584, 51776], "temperature": 0.0, "avg_logprob": -0.1607085197202621, "compression_ratio":
  1.7321428571428572, "no_speech_prob": 0.007830423302948475}, {"id": 445, "seek":
  313924, "start": 3140.12, "end": 3147.24, "text": " the the basic share so you can
  create a pipeline and say 70% keyword search weight and 30%", "tokens": [50408,
  264, 264, 3875, 2073, 370, 291, 393, 1884, 257, 15517, 293, 584, 5285, 4, 20428,
  3164, 3364, 293, 2217, 4, 50764], "temperature": 0.0, "avg_logprob": -0.16770266019381008,
  "compression_ratio": 1.5810055865921788, "no_speech_prob": 0.0015157173620536923},
  {"id": 446, "seek": 313924, "start": 3147.24, "end": 3154.8399999999997, "text":
  " neural search weight you can also define these on the fly but we currently have
  the limitation", "tokens": [50764, 18161, 3164, 3364, 291, 393, 611, 6964, 613,
  322, 264, 3603, 457, 321, 4362, 362, 264, 27432, 51144], "temperature": 0.0, "avg_logprob":
  -0.16770266019381008, "compression_ratio": 1.5810055865921788, "no_speech_prob":
  0.0015157173620536923}, {"id": 447, "seek": 313924, "start": 3154.8399999999997,
  "end": 3162.6, "text": " that we although we can hook up the model within a so-called
  ml inference pipeline in open search", "tokens": [51144, 300, 321, 4878, 321, 393,
  6328, 493, 264, 2316, 1951, 257, 370, 12, 11880, 23271, 38253, 15517, 294, 1269,
  3164, 51532], "temperature": 0.0, "avg_logprob": -0.16770266019381008, "compression_ratio":
  1.5810055865921788, "no_speech_prob": 0.0015157173620536923}, {"id": 448, "seek":
  316260, "start": 3163.48, "end": 3173.3199999999997, "text": " this ml inference
  pipeline can as of now not pass the predicted neural and keyword search weights",
  "tokens": [50408, 341, 23271, 38253, 15517, 393, 382, 295, 586, 406, 1320, 264,
  19147, 18161, 293, 20428, 3164, 17443, 50900], "temperature": 0.0, "avg_logprob":
  -0.09703114724928333, "compression_ratio": 1.5846994535519126, "no_speech_prob":
  0.000978419790044427}, {"id": 449, "seek": 316260, "start": 3173.3199999999997,
  "end": 3181.64, "text": " to this pipeline but feature request is already out there
  and I assume that in one of the next", "tokens": [50900, 281, 341, 15517, 457, 4111,
  5308, 307, 1217, 484, 456, 293, 286, 6552, 300, 294, 472, 295, 264, 958, 51316],
  "temperature": 0.0, "avg_logprob": -0.09703114724928333, "compression_ratio": 1.5846994535519126,
  "no_speech_prob": 0.000978419790044427}, {"id": 450, "seek": 316260, "start": 3182.2,
  "end": 3188.6, "text": " open search versions we will have the possibility to not
  only what''s already possible hook up the", "tokens": [51344, 1269, 3164, 9606,
  321, 486, 362, 264, 7959, 281, 406, 787, 437, 311, 1217, 1944, 6328, 493, 264, 51664],
  "temperature": 0.0, "avg_logprob": -0.09703114724928333, "compression_ratio": 1.5846994535519126,
  "no_speech_prob": 0.000978419790044427}, {"id": 451, "seek": 318860, "start": 3188.6,
  "end": 3197.3199999999997, "text": " model within open search so that it from within
  open search you call out to the model to make", "tokens": [50364, 2316, 1951, 1269,
  3164, 370, 300, 309, 490, 1951, 1269, 3164, 291, 818, 484, 281, 264, 2316, 281,
  652, 50800], "temperature": 0.0, "avg_logprob": -0.13806663125248278, "compression_ratio":
  1.7577639751552796, "no_speech_prob": 0.0006006536423228681}, {"id": 452, "seek":
  318860, "start": 3197.3199999999997, "end": 3204.92, "text": " inference you will
  retrieve the predicted neural and keyword search weights and then you can use",
  "tokens": [50800, 38253, 291, 486, 30254, 264, 19147, 18161, 293, 20428, 3164, 17443,
  293, 550, 291, 393, 764, 51180], "temperature": 0.0, "avg_logprob": -0.13806663125248278,
  "compression_ratio": 1.7577639751552796, "no_speech_prob": 0.0006006536423228681},
  {"id": 453, "seek": 318860, "start": 3204.92, "end": 3211.64, "text": " these in
  your search pipeline so there is already an implementation plan out there there
  are", "tokens": [51180, 613, 294, 428, 3164, 15517, 370, 456, 307, 1217, 364, 11420,
  1393, 484, 456, 456, 366, 51516], "temperature": 0.0, "avg_logprob": -0.13806663125248278,
  "compression_ratio": 1.7577639751552796, "no_speech_prob": 0.0006006536423228681},
  {"id": 454, "seek": 321164, "start": 3211.96, "end": 3219.3199999999997, "text":
  " open feature requests and if anyone wants to give these thumbs up to prioritize
  that within the", "tokens": [50380, 1269, 4111, 12475, 293, 498, 2878, 2738, 281,
  976, 613, 8838, 493, 281, 25164, 300, 1951, 264, 50748], "temperature": 0.0, "avg_logprob":
  -0.10399868844569414, "compression_ratio": 1.6551724137931034, "no_speech_prob":
  0.006629263982176781}, {"id": 455, "seek": 321164, "start": 3219.3199999999997,
  "end": 3224.68, "text": " open search community that would of course be greatly
  appreciated and I''m sure we can include", "tokens": [50748, 1269, 3164, 1768, 300,
  576, 295, 1164, 312, 14147, 17169, 293, 286, 478, 988, 321, 393, 4090, 51016], "temperature":
  0.0, "avg_logprob": -0.10399868844569414, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.006629263982176781}, {"id": 456, "seek": 321164, "start": 3224.68,
  "end": 3231.8799999999997, "text": " these GitHub issues as well in the show notes.
  Yeah for sure let''s do that and we will call out", "tokens": [51016, 613, 23331,
  2663, 382, 731, 294, 264, 855, 5570, 13, 865, 337, 988, 718, 311, 360, 300, 293,
  321, 486, 818, 484, 51376], "temperature": 0.0, "avg_logprob": -0.10399868844569414,
  "compression_ratio": 1.6551724137931034, "no_speech_prob": 0.006629263982176781},
  {"id": 457, "seek": 321164, "start": 3231.8799999999997, "end": 3236.6, "text":
  " that''s how to call out to the community please vote if you care I hope there
  will be enough people", "tokens": [51376, 300, 311, 577, 281, 818, 484, 281, 264,
  1768, 1767, 4740, 498, 291, 1127, 286, 1454, 456, 486, 312, 1547, 561, 51612], "temperature":
  0.0, "avg_logprob": -0.10399868844569414, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.006629263982176781}, {"id": 458, "seek": 323660, "start": 3236.68,
  "end": 3245.64, "text": " who care about this. Yeah exactly and then the you said
  everything is open source does that mean", "tokens": [50368, 567, 1127, 466, 341,
  13, 865, 2293, 293, 550, 264, 291, 848, 1203, 307, 1269, 4009, 775, 300, 914, 50816],
  "temperature": 0.0, "avg_logprob": -0.15059559920738483, "compression_ratio": 1.7085201793721974,
  "no_speech_prob": 0.01387438178062439}, {"id": 459, "seek": 323660, "start": 3245.64,
  "end": 3252.68, "text": " that the training scripts the algorithms the choices you
  make you can make there is also open", "tokens": [50816, 300, 264, 3097, 23294,
  264, 14642, 264, 7994, 291, 652, 291, 393, 652, 456, 307, 611, 1269, 51168], "temperature":
  0.0, "avg_logprob": -0.15059559920738483, "compression_ratio": 1.7085201793721974,
  "no_speech_prob": 0.01387438178062439}, {"id": 460, "seek": 323660, "start": 3252.68,
  "end": 3260.04, "text": " source right and we can link to that as well yeah. Yes
  so everything with the I mean we of course", "tokens": [51168, 4009, 558, 293, 321,
  393, 2113, 281, 300, 382, 731, 1338, 13, 1079, 370, 1203, 365, 264, 286, 914, 321,
  295, 1164, 51536], "temperature": 0.0, "avg_logprob": -0.15059559920738483, "compression_ratio":
  1.7085201793721974, "no_speech_prob": 0.01387438178062439}, {"id": 461, "seek":
  323660, "start": 3260.04, "end": 3265.88, "text": " didn''t include all the thousand
  experiments but all the helpers at least that we used to run", "tokens": [51536,
  994, 380, 4090, 439, 264, 4714, 12050, 457, 439, 264, 854, 433, 412, 1935, 300,
  321, 1143, 281, 1190, 51828], "temperature": 0.0, "avg_logprob": -0.15059559920738483,
  "compression_ratio": 1.7085201793721974, "no_speech_prob": 0.01387438178062439},
  {"id": 462, "seek": 326588, "start": 3265.88, "end": 3274.44, "text": " these 1000
  experiments they are all in the repository out there for everyone to have a look
  at and", "tokens": [50364, 613, 9714, 12050, 436, 366, 439, 294, 264, 25841, 484,
  456, 337, 1518, 281, 362, 257, 574, 412, 293, 50792], "temperature": 0.0, "avg_logprob":
  -0.14934514550601735, "compression_ratio": 1.546875, "no_speech_prob": 0.001986442133784294},
  {"id": 463, "seek": 326588, "start": 3274.44, "end": 3280.84, "text": " maybe come
  up with even better ideas than we had so we definitely always love to hear these
  as well.", "tokens": [50792, 1310, 808, 493, 365, 754, 1101, 3487, 813, 321, 632,
  370, 321, 2138, 1009, 959, 281, 1568, 613, 382, 731, 13, 51112], "temperature":
  0.0, "avg_logprob": -0.14934514550601735, "compression_ratio": 1.546875, "no_speech_prob":
  0.001986442133784294}, {"id": 464, "seek": 326588, "start": 3281.48, "end": 3289.4,
  "text": " Wow this is amazing this is a we can true sense you speak up to your name
  open source connections", "tokens": [51144, 3153, 341, 307, 2243, 341, 307, 257,
  321, 393, 2074, 2020, 291, 1710, 493, 281, 428, 1315, 1269, 4009, 9271, 51540],
  "temperature": 0.0, "avg_logprob": -0.14934514550601735, "compression_ratio": 1.546875,
  "no_speech_prob": 0.001986442133784294}, {"id": 465, "seek": 328940, "start": 3289.88,
  "end": 3296.44, "text": " that''s amazing like to me it''s a ton of work that you
  could choose to hide as well right and work", "tokens": [50388, 300, 311, 2243,
  411, 281, 385, 309, 311, 257, 2952, 295, 589, 300, 291, 727, 2826, 281, 6479, 382,
  731, 558, 293, 589, 50716], "temperature": 0.0, "avg_logprob": -0.14937685894709762,
  "compression_ratio": 1.8240740740740742, "no_speech_prob": 0.014770988374948502},
  {"id": 466, "seek": 328940, "start": 3296.44, "end": 3302.6800000000003, "text":
  " only with your clients and and nurture and iron out and everything and make a
  ton of money and", "tokens": [50716, 787, 365, 428, 6982, 293, 293, 41451, 293,
  6497, 484, 293, 1203, 293, 652, 257, 2952, 295, 1460, 293, 51028], "temperature":
  0.0, "avg_logprob": -0.14937685894709762, "compression_ratio": 1.8240740740740742,
  "no_speech_prob": 0.014770988374948502}, {"id": 467, "seek": 328940, "start": 3302.6800000000003,
  "end": 3307.56, "text": " continue on that but you choose to open source because
  you believe in the power of the community as", "tokens": [51028, 2354, 322, 300,
  457, 291, 2826, 281, 1269, 4009, 570, 291, 1697, 294, 264, 1347, 295, 264, 1768,
  382, 51272], "temperature": 0.0, "avg_logprob": -0.14937685894709762, "compression_ratio":
  1.8240740740740742, "no_speech_prob": 0.014770988374948502}, {"id": 468, "seek":
  328940, "start": 3307.56, "end": 3318.6800000000003, "text": " well to enhance it
  that''s amazing well said what''s next you already said a couple of words but what''s",
  "tokens": [51272, 731, 281, 11985, 309, 300, 311, 2243, 731, 848, 437, 311, 958,
  291, 1217, 848, 257, 1916, 295, 2283, 457, 437, 311, 51828], "temperature": 0.0,
  "avg_logprob": -0.14937685894709762, "compression_ratio": 1.8240740740740742, "no_speech_prob":
  0.014770988374948502}, {"id": 469, "seek": 331868, "start": 3318.68, "end": 3325.96,
  "text": " next and also do you want to address our audience what do you expect from
  me I think you know one of", "tokens": [50364, 958, 293, 611, 360, 291, 528, 281,
  2985, 527, 4034, 437, 360, 291, 2066, 490, 385, 286, 519, 291, 458, 472, 295, 50728],
  "temperature": 0.0, "avg_logprob": -0.15480988748957603, "compression_ratio": 1.7345132743362832,
  "no_speech_prob": 0.0003564977669157088}, {"id": 470, "seek": 331868, "start": 3325.96,
  "end": 3332.2, "text": " the things is you know as we''ve gotten into this you know
  we''ve we''ve found some rough spots in", "tokens": [50728, 264, 721, 307, 291,
  458, 382, 321, 600, 5768, 666, 341, 291, 458, 321, 600, 321, 600, 1352, 512, 5903,
  10681, 294, 51040], "temperature": 0.0, "avg_logprob": -0.15480988748957603, "compression_ratio":
  1.7345132743362832, "no_speech_prob": 0.0003564977669157088}, {"id": 471, "seek":
  331868, "start": 3332.2, "end": 3339.16, "text": " open search right open search
  has a strong ML component ML Commons project right but integrating it", "tokens":
  [51040, 1269, 3164, 558, 1269, 3164, 575, 257, 2068, 21601, 6542, 21601, 34894,
  1716, 558, 457, 26889, 309, 51388], "temperature": 0.0, "avg_logprob": -0.15480988748957603,
  "compression_ratio": 1.7345132743362832, "no_speech_prob": 0.0003564977669157088},
  {"id": 472, "seek": 331868, "start": 3339.16, "end": 3344.9199999999996, "text":
  " in sort of new and interesting ways like what Daniel was showing we''re finding
  some rough spots", "tokens": [51388, 294, 1333, 295, 777, 293, 1880, 2098, 411,
  437, 8033, 390, 4099, 321, 434, 5006, 512, 5903, 10681, 51676], "temperature": 0.0,
  "avg_logprob": -0.15480988748957603, "compression_ratio": 1.7345132743362832, "no_speech_prob":
  0.0003564977669157088}, {"id": 473, "seek": 334492, "start": 3345.7200000000003,
  "end": 3353.8, "text": " it is interesting to me it does bring them in the do search
  engines what we call a search engine need", "tokens": [50404, 309, 307, 1880, 281,
  385, 309, 775, 1565, 552, 294, 264, 360, 3164, 12982, 437, 321, 818, 257, 3164,
  2848, 643, 50808], "temperature": 0.0, "avg_logprob": -0.08490586280822754, "compression_ratio":
  1.7757847533632287, "no_speech_prob": 0.0021228506229817867}, {"id": 474, "seek":
  334492, "start": 3353.8, "end": 3360.6800000000003, "text": " to evolve to be more
  of an ML engine as well right I mean it feels to me like search has been", "tokens":
  [50808, 281, 16693, 281, 312, 544, 295, 364, 21601, 2848, 382, 731, 558, 286, 914,
  309, 3417, 281, 385, 411, 3164, 575, 668, 51152], "temperature": 0.0, "avg_logprob":
  -0.08490586280822754, "compression_ratio": 1.7757847533632287, "no_speech_prob":
  0.0021228506229817867}, {"id": 475, "seek": 334492, "start": 3360.6800000000003,
  "end": 3367.64, "text": " revolutionized by machine learning and as we move into
  this direction of more calculating building", "tokens": [51152, 8894, 1602, 538,
  3479, 2539, 293, 382, 321, 1286, 666, 341, 3513, 295, 544, 28258, 2390, 51500],
  "temperature": 0.0, "avg_logprob": -0.08490586280822754, "compression_ratio": 1.7757847533632287,
  "no_speech_prob": 0.0021228506229817867}, {"id": 476, "seek": 334492, "start": 3367.64,
  "end": 3373.96, "text": " models evaluating data on the fly do our search engines
  need to support those use cases and go beyond", "tokens": [51500, 5245, 27479, 1412,
  322, 264, 3603, 360, 527, 3164, 12982, 643, 281, 1406, 729, 764, 3331, 293, 352,
  4399, 51816], "temperature": 0.0, "avg_logprob": -0.08490586280822754, "compression_ratio":
  1.7757847533632287, "no_speech_prob": 0.0021228506229817867}, {"id": 477, "seek":
  337396, "start": 3373.96, "end": 3381.7200000000003, "text": " just the I I get
  a query I get documents I match them up and that''s it right is there another",
  "tokens": [50364, 445, 264, 286, 286, 483, 257, 14581, 286, 483, 8512, 286, 2995,
  552, 493, 293, 300, 311, 309, 558, 307, 456, 1071, 50752], "temperature": 0.0, "avg_logprob":
  -0.11376806323447924, "compression_ratio": 1.6877828054298643, "no_speech_prob":
  0.0004616710648406297}, {"id": 478, "seek": 337396, "start": 3381.7200000000003,
  "end": 3388.52, "text": " layer of computation that we kind of need in the search
  engine versus bolting it on in", "tokens": [50752, 4583, 295, 24903, 300, 321, 733,
  295, 643, 294, 264, 3164, 2848, 5717, 8986, 783, 309, 322, 294, 51092], "temperature":
  0.0, "avg_logprob": -0.11376806323447924, "compression_ratio": 1.6877828054298643,
  "no_speech_prob": 0.0004616710648406297}, {"id": 479, "seek": 337396, "start": 3389.48,
  "end": 3396.04, "text": " some other environment with an ML ops pipeline and all
  the rest um and and I think that''s in the", "tokens": [51140, 512, 661, 2823, 365,
  364, 21601, 44663, 15517, 293, 439, 264, 1472, 1105, 293, 293, 286, 519, 300, 311,
  294, 264, 51468], "temperature": 0.0, "avg_logprob": -0.11376806323447924, "compression_ratio":
  1.6877828054298643, "no_speech_prob": 0.0004616710648406297}, {"id": 480, "seek":
  337396, "start": 3396.04, "end": 3401.48, "text": " interesting you know one place
  where I think open search is a little bit you know is definitely", "tokens": [51468,
  1880, 291, 458, 472, 1081, 689, 286, 519, 1269, 3164, 307, 257, 707, 857, 291, 458,
  307, 2138, 51740], "temperature": 0.0, "avg_logprob": -0.11376806323447924, "compression_ratio":
  1.6877828054298643, "no_speech_prob": 0.0004616710648406297}, {"id": 481, "seek":
  340148, "start": 3402.28, "end": 3406.6, "text": " you know breaking some interesting
  ground is all the machine learning aspects to it", "tokens": [50404, 291, 458, 7697,
  512, 1880, 2727, 307, 439, 264, 3479, 2539, 7270, 281, 309, 50620], "temperature":
  0.0, "avg_logprob": -0.07449235544576273, "compression_ratio": 1.6846846846846846,
  "no_speech_prob": 0.000674513285048306}, {"id": 482, "seek": 340148, "start": 3407.48,
  "end": 3413.88, "text": " but you know data processing and building models and all
  of that needs to maybe be a first class", "tokens": [50664, 457, 291, 458, 1412,
  9007, 293, 2390, 5245, 293, 439, 295, 300, 2203, 281, 1310, 312, 257, 700, 1508,
  50984], "temperature": 0.0, "avg_logprob": -0.07449235544576273, "compression_ratio":
  1.6846846846846846, "no_speech_prob": 0.000674513285048306}, {"id": 483, "seek":
  340148, "start": 3413.88, "end": 3421.56, "text": " citizen of what we consider
  a search engine versus something done by some other system elsewhere", "tokens":
  [50984, 13326, 295, 437, 321, 1949, 257, 3164, 2848, 5717, 746, 1096, 538, 512,
  661, 1185, 14517, 51368], "temperature": 0.0, "avg_logprob": -0.07449235544576273,
  "compression_ratio": 1.6846846846846846, "no_speech_prob": 0.000674513285048306},
  {"id": 484, "seek": 340148, "start": 3421.56, "end": 3427.4, "text": " because that''s
  a lot more complexity and you know raises the barrier to adopting these things so",
  "tokens": [51368, 570, 300, 311, 257, 688, 544, 14024, 293, 291, 458, 19658, 264,
  13357, 281, 32328, 613, 721, 370, 51660], "temperature": 0.0, "avg_logprob": -0.07449235544576273,
  "compression_ratio": 1.6846846846846846, "no_speech_prob": 0.000674513285048306},
  {"id": 485, "seek": 342740, "start": 3427.48, "end": 3434.2000000000003, "text":
  " I look forward to things like a hybrid optimizer just sort of being like what
  you do when you build", "tokens": [50368, 286, 574, 2128, 281, 721, 411, 257, 13051,
  5028, 6545, 445, 1333, 295, 885, 411, 437, 291, 360, 562, 291, 1322, 50704], "temperature":
  0.0, "avg_logprob": -0.09127230976903161, "compression_ratio": 1.7255813953488373,
  "no_speech_prob": 0.0005911454791203141}, {"id": 486, "seek": 342740, "start": 3434.2000000000003,
  "end": 3439.1600000000003, "text": " your search engine of course you turn on the
  hybrid optimizer if it meets your use case and", "tokens": [50704, 428, 3164, 2848,
  295, 1164, 291, 1261, 322, 264, 13051, 5028, 6545, 498, 309, 13961, 428, 764, 1389,
  293, 50952], "temperature": 0.0, "avg_logprob": -0.09127230976903161, "compression_ratio":
  1.7255813953488373, "no_speech_prob": 0.0005911454791203141}, {"id": 487, "seek":
  342740, "start": 3439.1600000000003, "end": 3445.7200000000003, "text": " you have
  the judgments and other features that you need right versus oh a major engineering
  project", "tokens": [50952, 291, 362, 264, 40337, 293, 661, 4122, 300, 291, 643,
  558, 5717, 1954, 257, 2563, 7043, 1716, 51280], "temperature": 0.0, "avg_logprob":
  -0.09127230976903161, "compression_ratio": 1.7255813953488373, "no_speech_prob":
  0.0005911454791203141}, {"id": 488, "seek": 342740, "start": 3445.7200000000003,
  "end": 3452.28, "text": " that we''re going to do this going to take us six months
  so um yeah yeah yeah um", "tokens": [51280, 300, 321, 434, 516, 281, 360, 341, 516,
  281, 747, 505, 2309, 2493, 370, 1105, 1338, 1338, 1338, 1105, 51608], "temperature":
  0.0, "avg_logprob": -0.09127230976903161, "compression_ratio": 1.7255813953488373,
  "no_speech_prob": 0.0005911454791203141}, {"id": 489, "seek": 345228, "start": 3453.2400000000002,
  "end": 3459.48, "text": " um and you know supporting that you know as Dan you highlighted
  the search quality evaluation", "tokens": [50412, 1105, 293, 291, 458, 7231, 300,
  291, 458, 382, 3394, 291, 17173, 264, 3164, 3125, 13344, 50724], "temperature":
  0.0, "avg_logprob": -0.14010675563368685, "compression_ratio": 1.6695278969957081,
  "no_speech_prob": 0.0030809228774160147}, {"id": 490, "seek": 345228, "start": 3459.48,
  "end": 3465.0, "text": " framework that we''re adding to open searches really exciting
  would love to come back to Metri and", "tokens": [50724, 8388, 300, 321, 434, 5127,
  281, 1269, 26701, 534, 4670, 576, 959, 281, 808, 646, 281, 6377, 470, 293, 51000],
  "temperature": 0.0, "avg_logprob": -0.14010675563368685, "compression_ratio": 1.6695278969957081,
  "no_speech_prob": 0.0030809228774160147}, {"id": 491, "seek": 345228, "start": 3465.0,
  "end": 3471.0, "text": " talk all about that on another show yeah let''s do that
  I''m really excited to dive deeper into", "tokens": [51000, 751, 439, 466, 300,
  322, 1071, 855, 1338, 718, 311, 360, 300, 286, 478, 534, 2919, 281, 9192, 7731,
  666, 51300], "temperature": 0.0, "avg_logprob": -0.14010675563368685, "compression_ratio":
  1.6695278969957081, "no_speech_prob": 0.0030809228774160147}, {"id": 492, "seek":
  345228, "start": 3471.0, "end": 3476.36, "text": " evil because I think in so many
  ways you need to start with evil especially if you have a search engine", "tokens":
  [51300, 6724, 570, 286, 519, 294, 370, 867, 2098, 291, 643, 281, 722, 365, 6724,
  2318, 498, 291, 362, 257, 3164, 2848, 51568], "temperature": 0.0, "avg_logprob":
  -0.14010675563368685, "compression_ratio": 1.6695278969957081, "no_speech_prob":
  0.0030809228774160147}, {"id": 493, "seek": 347636, "start": 3476.36, "end": 3482.92,
  "text": " right out there uh to establish that uh you know baseline for yourself
  and then learn and", "tokens": [50364, 558, 484, 456, 2232, 281, 8327, 300, 2232,
  291, 458, 20518, 337, 1803, 293, 550, 1466, 293, 50692], "temperature": 0.0, "avg_logprob":
  -0.15163103739420572, "compression_ratio": 1.7168949771689497, "no_speech_prob":
  0.0086812824010849}, {"id": 494, "seek": 347636, "start": 3482.92, "end": 3489.56,
  "text": " introspect where things uh work or fail yeah make sure some of these models
  don''t go and produce", "tokens": [50692, 560, 28713, 689, 721, 2232, 589, 420,
  3061, 1338, 652, 988, 512, 295, 613, 5245, 500, 380, 352, 293, 5258, 51024], "temperature":
  0.0, "avg_logprob": -0.15163103739420572, "compression_ratio": 1.7168949771689497,
  "no_speech_prob": 0.0086812824010849}, {"id": 495, "seek": 347636, "start": 3489.56,
  "end": 3497.2400000000002, "text": " terrible yeah back shit crazy results right
  we had the risk that you know boosting up on neural", "tokens": [51024, 6237, 1338,
  646, 4611, 3219, 3542, 558, 321, 632, 264, 3148, 300, 291, 458, 43117, 493, 322,
  18161, 51408], "temperature": 0.0, "avg_logprob": -0.15163103739420572, "compression_ratio":
  1.7168949771689497, "no_speech_prob": 0.0086812824010849}, {"id": 496, "seek": 347636,
  "start": 3497.2400000000002, "end": 3502.6, "text": "ness might be terrible right
  we have to understand that and so we need to be much better about", "tokens": [51408,
  1287, 1062, 312, 6237, 558, 321, 362, 281, 1223, 300, 293, 370, 321, 643, 281, 312,
  709, 1101, 466, 51676], "temperature": 0.0, "avg_logprob": -0.15163103739420572,
  "compression_ratio": 1.7168949771689497, "no_speech_prob": 0.0086812824010849},
  {"id": 497, "seek": 350260, "start": 3502.6, "end": 3509.08, "text": " evaluation
  right we can''t take our eye off the ball of speed right query speed does remain",
  "tokens": [50364, 13344, 558, 321, 393, 380, 747, 527, 3313, 766, 264, 2594, 295,
  3073, 558, 14581, 3073, 775, 6222, 50688], "temperature": 0.0, "avg_logprob": -0.20521946957236842,
  "compression_ratio": 1.8436018957345972, "no_speech_prob": 0.0012746984139084816},
  {"id": 498, "seek": 350260, "start": 3509.7999999999997, "end": 3515.72, "text":
  " just sort of top of mind we also really need to be good at evaluation and I think
  for a lot of", "tokens": [50724, 445, 1333, 295, 1192, 295, 1575, 321, 611, 534,
  643, 281, 312, 665, 412, 13344, 293, 286, 519, 337, 257, 688, 295, 51020], "temperature":
  0.0, "avg_logprob": -0.20521946957236842, "compression_ratio": 1.8436018957345972,
  "no_speech_prob": 0.0012746984139084816}, {"id": 499, "seek": 350260, "start": 3515.72,
  "end": 3521.72, "text": " search teams that''s kind of a new thing yes absolutely
  so the pooling and low search agents yeah and", "tokens": [51020, 3164, 5491, 300,
  311, 733, 295, 257, 777, 551, 2086, 3122, 370, 264, 7005, 278, 293, 2295, 3164,
  12554, 1338, 293, 51320], "temperature": 0.0, "avg_logprob": -0.20521946957236842,
  "compression_ratio": 1.8436018957345972, "no_speech_prob": 0.0012746984139084816},
  {"id": 500, "seek": 350260, "start": 3521.72, "end": 3527.24, "text": " we do want
  to do what other thing I want to shout out yeah one other thing I want to shout
  out is that", "tokens": [51320, 321, 360, 528, 281, 360, 437, 661, 551, 286, 528,
  281, 8043, 484, 1338, 472, 661, 551, 286, 528, 281, 8043, 484, 307, 300, 51596],
  "temperature": 0.0, "avg_logprob": -0.20521946957236842, "compression_ratio": 1.8436018957345972,
  "no_speech_prob": 0.0012746984139084816}, {"id": 501, "seek": 352724, "start": 3527.7999999999997,
  "end": 3535.9599999999996, "text": " the next haystack conference uh the saved the
  date last week in April right um last week in April", "tokens": [50392, 264, 958,
  4842, 372, 501, 7586, 2232, 264, 6624, 264, 4002, 1036, 1243, 294, 6929, 558, 1105,
  1036, 1243, 294, 6929, 50800], "temperature": 0.0, "avg_logprob": -0.15075209971224324,
  "compression_ratio": 1.7180616740088106, "no_speech_prob": 0.0024090104270726442},
  {"id": 502, "seek": 352724, "start": 3536.7599999999998, "end": 3543.8799999999997,
  "text": " save the date went out um and we are looking for uh talk reviewers people
  who want to be reviewing", "tokens": [50840, 3155, 264, 4002, 1437, 484, 1105, 293,
  321, 366, 1237, 337, 2232, 751, 45837, 561, 567, 528, 281, 312, 19576, 51196], "temperature":
  0.0, "avg_logprob": -0.15075209971224324, "compression_ratio": 1.7180616740088106,
  "no_speech_prob": 0.0024090104270726442}, {"id": 503, "seek": 352724, "start": 3543.8799999999997,
  "end": 3548.4399999999996, "text": " the talk proposals it''s a double blind process
  we get a couple people from the community so if", "tokens": [51196, 264, 751, 20198,
  309, 311, 257, 3834, 6865, 1399, 321, 483, 257, 1916, 561, 490, 264, 1768, 370,
  498, 51424], "temperature": 0.0, "avg_logprob": -0.15075209971224324, "compression_ratio":
  1.7180616740088106, "no_speech_prob": 0.0024090104270726442}, {"id": 504, "seek":
  352724, "start": 3548.4399999999996, "end": 3555.08, "text": " that''s something
  interested reach out to David Fisher uh he''s running that process uh and call for",
  "tokens": [51424, 300, 311, 746, 3102, 2524, 484, 281, 4389, 26676, 2232, 415, 311,
  2614, 300, 1399, 2232, 293, 818, 337, 51756], "temperature": 0.0, "avg_logprob":
  -0.15075209971224324, "compression_ratio": 1.7180616740088106, "no_speech_prob":
  0.0024090104270726442}, {"id": 505, "seek": 355508, "start": 3555.08, "end": 3562.44,
  "text": " proposals will be out I''m curious if this year haystack in Charlottesville
  might as well just be called", "tokens": [50364, 20198, 486, 312, 484, 286, 478,
  6369, 498, 341, 1064, 4842, 372, 501, 294, 14130, 1521, 279, 8386, 1062, 382, 731,
  445, 312, 1219, 50732], "temperature": 0.0, "avg_logprob": -0.14968310252274616,
  "compression_ratio": 1.652542372881356, "no_speech_prob": 0.0013577057980000973},
  {"id": 506, "seek": 355508, "start": 3562.44, "end": 3571.16, "text": " hybrid stack
  like are we gonna have two days of talking about hybrid uh because R.A.G. rag is",
  "tokens": [50732, 13051, 8630, 411, 366, 321, 799, 362, 732, 1708, 295, 1417, 466,
  13051, 2232, 570, 497, 13, 32, 13, 38, 13, 17539, 307, 51168], "temperature": 0.0,
  "avg_logprob": -0.14968310252274616, "compression_ratio": 1.652542372881356, "no_speech_prob":
  0.0013577057980000973}, {"id": 507, "seek": 355508, "start": 3571.16, "end": 3575.96,
  "text": " rag is you know that''s last year now we''re on to hybrid uh or is there
  going to be something new", "tokens": [51168, 17539, 307, 291, 458, 300, 311, 1036,
  1064, 586, 321, 434, 322, 281, 13051, 2232, 420, 307, 456, 516, 281, 312, 746, 777,
  51408], "temperature": 0.0, "avg_logprob": -0.14968310252274616, "compression_ratio":
  1.652542372881356, "no_speech_prob": 0.0013577057980000973}, {"id": 508, "seek":
  355508, "start": 3575.96, "end": 3580.84, "text": " so it''s going to be interesting
  to see what what what kind of comes out of the community uh for", "tokens": [51408,
  370, 309, 311, 516, 281, 312, 1880, 281, 536, 437, 437, 437, 733, 295, 1487, 484,
  295, 264, 1768, 2232, 337, 51652], "temperature": 0.0, "avg_logprob": -0.14968310252274616,
  "compression_ratio": 1.652542372881356, "no_speech_prob": 0.0013577057980000973},
  {"id": 509, "seek": 358084, "start": 3580.84, "end": 3586.6800000000003, "text":
  " this year''s haystack it''s also very interesting to to see this dynamic or this
  evolution because", "tokens": [50364, 341, 1064, 311, 4842, 372, 501, 309, 311,
  611, 588, 1880, 281, 281, 536, 341, 8546, 420, 341, 9303, 570, 50656], "temperature":
  0.0, "avg_logprob": -0.10982514279229301, "compression_ratio": 1.7717391304347827,
  "no_speech_prob": 0.008731388486921787}, {"id": 510, "seek": 358084, "start": 3586.6800000000003,
  "end": 3592.2000000000003, "text": " I think two or three years ago hybrid search
  was at the top of charts everyone was discussing it", "tokens": [50656, 286, 519,
  732, 420, 1045, 924, 2057, 13051, 3164, 390, 412, 264, 1192, 295, 17767, 1518, 390,
  10850, 309, 50932], "temperature": 0.0, "avg_logprob": -0.10982514279229301, "compression_ratio":
  1.7717391304347827, "no_speech_prob": 0.008731388486921787}, {"id": 511, "seek":
  358084, "start": 3592.2000000000003, "end": 3598.04, "text": " and then rags proceeded
  it and that just tells me that maybe we didn''t dive deep enough into the", "tokens":
  [50932, 293, 550, 367, 12109, 39053, 309, 293, 300, 445, 5112, 385, 300, 1310, 321,
  994, 380, 9192, 2452, 1547, 666, 264, 51224], "temperature": 0.0, "avg_logprob":
  -0.10982514279229301, "compression_ratio": 1.7717391304347827, "no_speech_prob":
  0.008731388486921787}, {"id": 512, "seek": 358084, "start": 3598.04, "end": 3604.36,
  "text": " topic which is let it go it passed and people thought oh that doesn''t
  work we need we need something", "tokens": [51224, 4829, 597, 307, 718, 309, 352,
  309, 4678, 293, 561, 1194, 1954, 300, 1177, 380, 589, 321, 643, 321, 643, 746, 51540],
  "temperature": 0.0, "avg_logprob": -0.10982514279229301, "compression_ratio": 1.7717391304347827,
  "no_speech_prob": 0.008731388486921787}, {"id": 513, "seek": 358084, "start": 3604.36,
  "end": 3610.76, "text": " else and now it''s rag rag rag everywhere but then rag
  also comes with its own you know limitation", "tokens": [51540, 1646, 293, 586,
  309, 311, 17539, 17539, 17539, 5315, 457, 550, 17539, 611, 1487, 365, 1080, 1065,
  291, 458, 27432, 51860], "temperature": 0.0, "avg_logprob": -0.10982514279229301,
  "compression_ratio": 1.7717391304347827, "no_speech_prob": 0.008731388486921787},
  {"id": 514, "seek": 361084, "start": 3611.2400000000002, "end": 3618.92, "text":
  " uh and now we have a new you know evolution level right with hybrid search you
  guys are", "tokens": [50384, 2232, 293, 586, 321, 362, 257, 777, 291, 458, 9303,
  1496, 558, 365, 13051, 3164, 291, 1074, 366, 50768], "temperature": 0.0, "avg_logprob":
  -0.14187672024681455, "compression_ratio": 1.6854460093896713, "no_speech_prob":
  0.0023195648100227118}, {"id": 515, "seek": 361084, "start": 3619.48, "end": 3624.44,
  "text": " optimizing uh that''s amazing I was actually waiting for it I''m happy
  to see it happen", "tokens": [50796, 40425, 2232, 300, 311, 2243, 286, 390, 767,
  3806, 337, 309, 286, 478, 2055, 281, 536, 309, 1051, 51044], "temperature": 0.0,
  "avg_logprob": -0.14187672024681455, "compression_ratio": 1.6854460093896713, "no_speech_prob":
  0.0023195648100227118}, {"id": 516, "seek": 361084, "start": 3625.6400000000003,
  "end": 3630.28, "text": " and thanks for sharing the story let''s come back to the
  evolve when you guys are ready I also", "tokens": [51104, 293, 3231, 337, 5414,
  264, 1657, 718, 311, 808, 646, 281, 264, 16693, 562, 291, 1074, 366, 1919, 286,
  611, 51336], "temperature": 0.0, "avg_logprob": -0.14187672024681455, "compression_ratio":
  1.6854460093896713, "no_speech_prob": 0.0023195648100227118}, {"id": 517, "seek":
  361084, "start": 3630.28, "end": 3636.44, "text": " expect that you will publish
  some blog posts around this topic about this topic so I''ll you", "tokens": [51336,
  2066, 300, 291, 486, 11374, 512, 6968, 12300, 926, 341, 4829, 466, 341, 4829, 370,
  286, 603, 291, 51644], "temperature": 0.0, "avg_logprob": -0.14187672024681455,
  "compression_ratio": 1.6854460093896713, "no_speech_prob": 0.0023195648100227118},
  {"id": 518, "seek": 363644, "start": 3636.44, "end": 3640.68, "text": " know I''ll
  be happy to promote those as well and read them of course and learn", "tokens":
  [50364, 458, 286, 603, 312, 2055, 281, 9773, 729, 382, 731, 293, 1401, 552, 295,
  1164, 293, 1466, 50576], "temperature": 0.0, "avg_logprob": -0.2078845549602898,
  "compression_ratio": 1.6859504132231404, "no_speech_prob": 0.015017562545835972},
  {"id": 519, "seek": 363644, "start": 3642.28, "end": 3647.88, "text": " terrific
  yeah thank you thank you very much thanks for coming to the show today and sharing
  this", "tokens": [50656, 20899, 1338, 1309, 291, 1309, 291, 588, 709, 3231, 337,
  1348, 281, 264, 855, 965, 293, 5414, 341, 50936], "temperature": 0.0, "avg_logprob":
  -0.2078845549602898, "compression_ratio": 1.6859504132231404, "no_speech_prob":
  0.015017562545835972}, {"id": 520, "seek": 363644, "start": 3647.88, "end": 3652.12,
  "text": " story it''s very exciting and also showing the demo I like notebooks because
  they love you", "tokens": [50936, 1657, 309, 311, 588, 4670, 293, 611, 4099, 264,
  10723, 286, 411, 43782, 570, 436, 959, 291, 51148], "temperature": 0.0, "avg_logprob":
  -0.2078845549602898, "compression_ratio": 1.6859504132231404, "no_speech_prob":
  0.015017562545835972}, {"id": 521, "seek": 363644, "start": 3653.16, "end": 3657.8,
  "text": " you know too quickly uh they say things and and have a feel of what''s
  going on", "tokens": [51200, 291, 458, 886, 2661, 2232, 436, 584, 721, 293, 293,
  362, 257, 841, 295, 437, 311, 516, 322, 51432], "temperature": 0.0, "avg_logprob":
  -0.2078845549602898, "compression_ratio": 1.6859504132231404, "no_speech_prob":
  0.015017562545835972}, {"id": 522, "seek": 363644, "start": 3658.68, "end": 3662.28,
  "text": " I''m glad that Eric still uses the cup that we gave him as a gift", "tokens":
  [51476, 286, 478, 5404, 300, 9336, 920, 4960, 264, 4414, 300, 321, 2729, 796, 382,
  257, 5306, 51656], "temperature": 0.0, "avg_logprob": -0.2078845549602898, "compression_ratio":
  1.6859504132231404, "no_speech_prob": 0.015017562545835972}, {"id": 523, "seek":
  366228, "start": 3662.36, "end": 3669.4, "text": " I love it it''s like like you
  really see you really see the gift you gave like coming back and saying", "tokens":
  [50368, 286, 959, 309, 309, 311, 411, 411, 291, 534, 536, 291, 534, 536, 264, 5306,
  291, 2729, 411, 1348, 646, 293, 1566, 50720], "temperature": 0.0, "avg_logprob":
  -0.2811511484781901, "compression_ratio": 1.8245614035087718, "no_speech_prob":
  0.02362840808928013}, {"id": 524, "seek": 366228, "start": 3669.4, "end": 3675.7200000000003,
  "text": " you did this and the person you gave it to is still enjoying that''s amazing",
  "tokens": [50720, 291, 630, 341, 293, 264, 954, 291, 2729, 309, 281, 307, 920, 9929,
  300, 311, 2243, 51036], "temperature": 0.0, "avg_logprob": -0.2811511484781901,
  "compression_ratio": 1.8245614035087718, "no_speech_prob": 0.02362840808928013},
  {"id": 525, "seek": 366228, "start": 3675.7200000000003, "end": 3680.1200000000003,
  "text": " so awesome to meet you thank you very much thank you thank you and Daniel
  on", "tokens": [51036, 370, 3476, 281, 1677, 291, 1309, 291, 588, 709, 1309, 291,
  1309, 291, 293, 8033, 322, 51256], "temperature": 0.0, "avg_logprob": -0.2811511484781901,
  "compression_ratio": 1.8245614035087718, "no_speech_prob": 0.02362840808928013},
  {"id": 526, "seek": 366228, "start": 3680.1200000000003, "end": 3685.0, "text":
  " yeah thanks for having us yeah thank you take care bye bye", "tokens": [51256,
  1338, 3231, 337, 1419, 505, 1338, 1309, 291, 747, 1127, 6543, 6543, 51500], "temperature":
  0.0, "avg_logprob": -0.2811511484781901, "compression_ratio": 1.8245614035087718,
  "no_speech_prob": 0.02362840808928013}]'
---

Hello there, Vector Podcast is back. Same season 3. I think we are about to wrap it up with few final really interesting episodes.
There I have the privilege to talk to the open source crew Eric Pugh who you have seen in the one of the previous episodes and you guessed Daniel Riggly joining us to discuss really interesting topic on hybrid search and optimization. Really really excited to have you both on the show. Hello.
Awesome. Awesome. So as a tradition we start with the intros. Eric everyone knows but Eric feel free to introduce yourself. I mean great to be back to me tree.
I actually I'm a little late getting here because I realized I was driving to the office that I forgot my mug that you gave me the other year. So I actually called Daniels like I'm going to be a little late because I got to go home and pick up the mug and bring it into the office.
My wife keeps it and we use it when we go hiking but I was like I'm going to bring it into the office and show it off since this is my second podcast to do with you and the mug that you gave me two years ago three years ago at this point. Yeah probably three years. Works great works great.
So yeah super excited to be back here and you know kind of talk about some of the work that we've been doing with the open search community. So exciting. Yes. And Daniel welcome. Can you say a few words about yourself your background? Absolutely yeah thanks. It's great to be here.
I'm super excited maybe a little nervous but I'm sure it'll be fun. So I'm Daniel I'm with open source connections. I started out as a search consultant back in May 2012.
 So almost 13 years now and I'm here to share some of our experiences that we made in our most recent project together with the folks of open search when it comes to hybrid search how to optimize hybrid search and also what's necessary to optimize hybrid search namely query sets and judgments but I'm sure we'll get into that in a couple of seconds.
Yeah thanks Daniel. I'm also nervous but I also know that you know when I release in the episodes I enjoy them. It's just it's just fun really. So I was thinking like hybrid search yeah we did discuss and I think community discusses it at large and various forums.
Erick also reminded me of the episode with Alessandro Benindetti that we just did it really was worth.
Yeah I was really just curious maybe step back from that topic a little bit and discuss the importance of hybrid search and what is it in your own words where do you see value for it compared to how we used to do search before. You want to take it Daniel and then I'll follow up.
 Sure yeah so I think we see hybrid search especially in this project as let's say the process of blending traditional keyword search and also let's say modern search approaches based on language more or mostly called either vector search or neuro search and I think the benefits of it are probably you follow it or I guess you can you can group them into two groups.
 Looking at the end user we always want to provide the end users with the most or the highest quality results right so search result quality is what we strive for and traditional keyword search always lacks of let's say finding related things that may not really contain the specific words but similar so laptop and notebook is an example that I think we ran probably a million times in demos maybe even more than a million times so if notebook is not in my product description I will not find it when I search for laptop and the other way around and that's where let's say blending the two techniques really shine because it enables you to not only find where your keywords are in but also find related stuff to augment the result set and I think that with that with that large benefit of course come a lot of challenges because it always is let's say non-tribal how to actually blend the traditional techniques and the more modern techniques so that's where the challenge between or the challenge behind hybrid search actually lies.
 I mentioned two groups for which there are benefits of the end user we want to provide the end user with the highest quality results that's one group the other group is of course we as the ones providing search applications I mean we somehow need to profit from providing better results and it then is always different or yeah different in which let's say scenario in which industry we are working so the monosperm transparent one is always e-commerce the easier the end user the consumer actually finds stuff in your online shop the easier is for them to buy stuff if they buy more stuff more easily of course we generate more revenue and that's kind of the benefit then that comes with providing better search results and the other way is we don't want to let's say manually tune systems let's say indefinitely so of course I can go ahead and say laptop is synonymous to notebook and PC is maybe broader term of laptop and rules like these but that's kind of work that is never done if I have a changing catalog that I don't know old products get thrown out of the product catalog new products arrive so it's a never-ending challenge for me and I don't want to let's say spend my work for us always manually hunting these rules and thinking about what made the users mean when they start for something I want something let's say intelligently looking for the right things in my index and that's what the neural part of hybrid search enables us so I think these are definitely maybe the two groups that benefit and how these two groups benefit from my perspective yeah that's really good intro Ericy water take it yeah I think it's an interesting journey that we've been on the last few years and I sort of look at hybrid search as a little bit of a like a course correction right so keyword search been around forever well understood frustrations are well known and then vectors came out and all these new products these new vector databases everybody was really excited about them and we all said oh okay let's go use vectors and we leapt on that and got really excited built everything using vectors and I think maybe we went too far that way over into vector land and we started after we started getting some experience with vectors we started realizing some of the problems with it right like doesn't matter what you query you're gonna get some search results right sometimes zero search results is the right answer right you know interesting challenges around you know faceting or pagination or highlighting can be weird right so you know I think that there are some definite challenges in vectors and we all went over that way and I think we've seen it in the last two years where all the vector databases were frantically adding keyword like search and all of the keyword search indexes were all frantically adding vectors okay now we have these things as like where do we go oh hybrid search right hybrid search and you know hybrid search popped out and you know hear me out I think hybrid search is just good old federated search from the late 90s and 2000s where you had two search engines with two we send out two queries and then you brought them back and you're like how do I merge them together and sometimes you do terrible things like two lists of results right we was sometimes we would try to link them up together um it's the same idea whether you're going to one search engine you're making a keyword search and a neural search and bring them together or two totally separate see keyword search engines you're still bringing back two lists however I think at least this time around how to merge the lists of results together seems to be going better than when we did it back in federated search right uh and I look forward to talking more about like some of the ways that we bring hybrid you know build our hybrid results set together um part of me really kind of wonders why ranked reciprocal fusion wasn't a thing the last time I did federated search back in the 2000s right like doesn't seem like that crazy of a concept why didn't we do that right but we didn't uh so I'm a little more optimistic about the value of it but um it i think hybrid is a little bit of something old coming back because we're back to the same problem I literally have two search engines two concepts for how to do information retrieval and yet I want to blend it into one yeah that's exciting topic I think to me a hybrid search opens doors beyond sort of what I think Daniel just explained you know the semantic connection between you know keywords and so on is where you go multi-model right of course you need to go there carefully probably but if you do miss metadata on a particular you know image on the product you could reason about it using the image itself and maybe also video because we have video alarms as well they're more expensive of course to run but you know sky's the limit so to say if you want to go there and go um yeah so I think I think in that sense hybrid search uh unlocks many more avenues to explore including in e-commerce I think right yeah yeah yeah I mean I love that we are actually getting away from the old just straight up bag of words that was keyword that served us for a long time but still was just a very rough approximation of what people want right I mean BM25 you know people say it's not even the best algorithm it's just as fast as the one that we use uh vectors is sort of this idea of there are richer ways of understanding user queries and the content tech and just going beyond taxes the you know it's absolutely wonderful right lots of different things I mean some point we'll do a vector search on usage patterns right to figure stuff out right like it'll be the the mode will be activity won't be video or image or something it'll be activity you'd be like oh yeah that's the person I want to talk to they have the same activities as me based on whatever it is that they do right so but those kinds of things definitely are expressed through the vectors um I do think that hybrid is an amazing thing for right now for the next few years uh I do think though it's also a little bit of a bandaid in the sense that we're still leaning on keyword search for you know various use cases and if we were to look 10 years out I think an ideal solution is that we're not doing hybrid anymore just have a better approach to search something beyond vector plus keyword something better that still supports the zero results is the right answer you know some of these problems that vector using vectors gives us right we would have better better approach and not this slightly band-aid I have two different ways of searching and then have to wedge them back together yeah I like for now hybrid's exciting yeah I like that I like where you're going I wanted to also I wonder if you saw that blog by Dr.
 Enbal I will make sure to link it where he talks about uh rrf you know reciprocal rank fusion and he shows on a like handcrafted example that uh you know if let's say neural search brings relevant result to the top of few results keyword lacks and doesn't so it basically brings noise when you combine the two you will end up having kind of half noise half signal and it will look terrible it will look terrible right and where do you stand on this like only there was a way yeah yeah it's only there was a way of at our understand not just blindly yeah you know blindly matching things um and I'll hand it over to Daniel and just a moment I do want to call that I really liked uh your previous episode with all a Sandra where uh I can't remember was you were all a Sandra but you kind of I think it was you Demetri said yeah that your engineers were looking at hybrid search and they kind of looked at it and said when you strip away the fancy words like ranked reciprocal fusion for blending things together you're like that's just round Robin right and you know round robin is not necessarily a round blind and it's blind round Robin right it's not round robin in in your middle school when you had to pick teams for dodgeball right the people picking knew who the best players were so at least you were at least divvying the best choices and at the very end those last two kids you know you knew they were the worst choices they were the noise in the search results right but you were that round robin at least had the benefit of knowing what was good ranked refresh ranked reciprocal fusion has no sense of whether the those results are good or bad right it is literally blindly picking them in some order with no sense of uh of what that is and as you can imagine blindly picking is going to leave lead you be pinched potentially a very weak dodgeball team right and yet that's what we think of a state of the art yeah so Daniel what should we do in this case is there any solution it's it's a good segue into what we actually tried and explored and experimented with um so in our most recent work we tried to come up with a systematic approach to optimize hybrid search specifically in open search um so in open search actually right now you have linear combination techniques at hand so that means you have two normalization techniques you can choose one the L2 norm the min max norm um they are basically both there so that you can normalize the scores from keyword search into the let's say space of vector search so that you can compare apples to apples more or less here and not apples to oranges because as we all know vm25 scores especially if you have if you have like wired field weights they are unbounded they can be in the dozens the hundreds the thousands so you don't really know upfront in what range you are operating and also you can't really compare the scores from one query to another query so that makes it really difficult to combine keyword search scores with any other um let's say search mechanism together with these normalization techniques the L2 norm them in max norm you have three combination techniques at hand and that's basically just three different means you can apply the arithmetic mean the harmonic mean and the geometric mean so that leaves you with two by three so that's already six parameter combinations that you can try on and then you can define weights um so how um how much neurosurge weight how much keyword search weight do i want to have in my query they always add up to one so you can say I want to go with 10% keyword 90% neural or 50-50 um thinking of let's say 11 of these weights so maybe you start with zero keyword and a hundred percent neural and 10% 90% and so on and so forth so that gives you a range of 11 multiplied with the six parameter combinations that we already had gives us let's say a solution area to explore of 66 different combinations which is pretty manageable so we defined optimizing hybrid search as a parameter optimization problem and we picked the most straightforward approach that you can pick and we just tried out all different combinations and calculated search metrics based on judgments and then we just had a look at which one is the best combination um for our experiments we used the ESCI data set um so that was released by amazon a couple of i think 18 months ago or something like that as part of our taglet competition um this data set comes with queries comes with products and most importantly it comes with judgments so we basically have everything that we need to really try out different um parameter combinations see how they work what results are retrieved um can calculate a couple of metrics compare these and then see which one is the best um parameter combination and um that's what we call the global hybrid search optimizer so we try to identify the best parameter combination globally for all the queries that we are looking at in a certain defined subset of queries so that's kind of the first step um the very very straightforward approach that we applied that's not really something um let's say scientifically um so first decated there was just a very brute force approach to see um what's in there also learn how results may be shaped or turn out differently when we increase neural search weight or increase the keyword search weight which normalization combination uh technique is usually the one that's best to retrieve the results and so on and so forth so um we started out with what I call reasonable baseline so searching across um I think five or six fields so title category color brand and description some bullet points so ecommerce data set like pretty basic stuff um and we calculated our metrics with that baseline so um I would call it uh probably not the best baseline you can come up with um but a reasonable baseline um you could come up with so we didn't want to let's say just create the weakest baseline because that's not really difficult to let's say outperform so we wanted to create a reasonable baseline without putting let's say a man here in finding out what the best baseline is um that's called okay right um we got decent results out of that and then we ran this global hybrid search optimizer and that outperformed the baseline already um across the metrics that we had a look at so better in DCG better DCG better precision at 10 were um these were the three metrics that we had a look at and that was nice to see because that already gave us um let's say assurance in a there is a straightforward approach that everyone can use because it's really easily applicable um it gets you good results and it also gives you assurance that there is something too neural search when switching to it from a keyword based um search engine or search application to a hybrid search um application but um as always when you apply something globally there are winners and there are losers so um some of the queries really improve by this hybrid search optimization step the global one but others didn't so we took this one step further and thought about how can we um really create a process that dynamically per query now predicts what the best parameter set is and that now is also like going in this direction that dark mentions in his blog post right so that's kind of a query understanding approach to hybrid search so we're not just blindly applying one parameter combination that we identified on a thousand queries that we explored we are taking one query analyzing this one query and then saying based on a variety of experiments that we made what is for this individual query the best parameter combination that we cannot apply so that we are not really globally applying something but individually dynamically per query and um to already maybe yeah give you the results um of what we did and then go into detail how we did it um the dynamic approach outperformed the global approach so we managed to identify a set of features we trained a model or multiple models actually and by applying this we were able to predict the best neuralness in that case or the best neural search weight for a given query based on um the results we got off the global hybrid search optimizer so we basically recycled all the different search metrics on a per query basis that we got did some feature engineering trained models and then used these models to predict what is the best neural search weight for this query and with this dynamic approach we even saw increases up to 10% in one of the metrics of the three that I just mentioned DCG and DCG and precision at 10 yeah that's very exciting thanks for for sharing this whole you know end-to-end picture pipeline I'm particularly interested at least at this point in time about the fact that well first of all your dynamic approach outperformed the global one right and that seems to be thanks to that query understanding part right can you talk a bit more about that uh and also did you check those predictions manually for example does it make intuitive sense that system picked that's for that specific query it picked more neuralness I mean is it like is it like a natural language question there or like some remnants of it or is there some other interesting findings that you could share possibly oh yeah so um let's first maybe outline what we did exactly and then dive into a couple of observations that we made on the way um so we started out by creating what we call feature groups and then we created features for these feature groups so we looked at three different feature groups um one was the query feature group the next one was the keyword search result feature group and then the semantics search result feature group for the query feature group we had a look at the length of the query the number of query terms if the query has numbers in it and if the query has any special characters in it so we kind of thought of ways figuring out when is the query maybe more specific when it is more when is it more broad query a narrow query and then we will just come up with rules like well a longer query is the more specific it is and maybe if we have more specific queries we have less results that's where we may want to augment search results with neural search results on the other hand when we have a very broad query we may have a lot of results these are short queries and then we may want to let's say only use organic traditional keyword search results yeah so we just came up with a couple of assumptions on our side and then with these four features for the keyword search result feature group we looked at the number of search results the number of hits we got when we executed the query with our baseline search configuration so the one searching in the six fields and then with something like hey if we have zero results then this is maybe a perfect scenario for neural search because then we want to augment zero results with zero keyword results with what comes from the vector search application the other two features we had in this group were the the best title score we had in the keyword search result so if we have a strong title match maybe that's an indication of we don't need as much neural search and we also have a look at I think the average title score in the top 10 was was another one so if we have like a high average in the title scores that's maybe a good sign for no augmentation needed with neural search results for semantic search it was similar to the title score so we had a look at the best title score and the average semantic similarity based on the title that we had indexed so by looking at these three groups we thought of well we now have a representation of the query on its own the result set based on keywords and then the result set based on neural search and that was kind of our starting point and then we did loads of experiments having to do with what's the best feature combination when we train a linear regression model or a random forest regression model what does regularization play for a role can we optimize the model training aspect with that so we really did a lot of iterations with these we also had a look at a large query set and versus a smaller query set to see if that also provides different aspects to it if we just randomly sound the 500 yet 500 queries versus 5000 queries so we did a lot of exploration to really pick out and make sure that we are not really let's say randomly receiving the uplift that we saw but actually really making sure that there is something to it and that we can go out in the wild there for example on this podcast and share our observations and be kind of on the safe side that they can be reproduced hopefully in other scenarios as well so that's kind of on the let's say how did we do it here so the features feature engineering how we train our models so we have a look at linear regression models and random forest regression as a starting point because we thought let's have a look at simple models first and if that works we can still have a look at the more complex ones and that's maybe already the first observation that I can share so linear regression models and the simplest form random forest regression slightly more complex form and then this is the last model iteration that we did last week we also have a look at gradient boosting methods and interestingly they all were almost the same from the model performance perspective so it wasn't like the most complex ones really give you the best results and that's kind of a very reassuring feeling because we need to calculate a couple features right per query and that adds latency to your query execution and especially in e-commerce where every millisecond basically counts we don't really want to let's say run multiple queries to calculate our features just to have like 0.
3 percent performance increase so it really has to be worth the effort so that's kind of a nice observation so we don't have to go for the most complex model architectures we can stick with the simple ones and don't really lose a lot of performance if any the linear regression model and the random forest regression model they actually scored absolutely equally when calculating the search metrics so they predicted the NDEG scores slightly different so that's how we did it we predicted NDEG scores by adding neuroness as a 10th feature in that case and by looking at which neuroness scored best and that kind of the neuroness we went then with for testing efforts afterwards so that's kind of the first interesting observation that we made we also had a look at different feature groups so what happens to model performance if we focus only on query features or only on keyword search result features so training models within one feature group only and not taking all features into account the interesting part here was that the combination work best so not always the combinations of all in nine features together with the neuroness feature but at least some of the key word search result features some of the semantics search result features and some of the queries features so they were best but looking at the query features only and these are the simplest ones to calculate they weren't part of these models from this performance aspect so you wouldn't really lose a lot if you only shows query features for your predictions so that was another nice observation here that if you went with the highest performance in terms of let's say inference speed and also speed of calculating the features beforehand you don't lose a lot of search result quality so again you don't have to go with the most complex approach to get reasonable results out of that which was I think the second most important finding at least from my perspective because that gives us again the assurance that when putting this into production we don't assume let's say hundreds of milliseconds added to your query latency if you stick to the the simple features.
 May it means that there's like room for growth with this technique right we're not maxing out this technique just to get started we can start out and then as we get more sophisticated we have room we have milliseconds to burn to do other cool interesting things ask an lllm to characterize the query or something like that right we've got room for bro but I will also like this lesson and I think it kind of resonates with what I've seen in doing a mal previously is that start with like simpler solutions and try to kind of maximize ROI you know by upgrading to a more complex one and you need to set some thresholds because like as you said Daniel you know just you know adding 0.
03 won't get it right it doesn't it's not worth because also when you bring in neural search it means that you need to build that parallel index of things right like you need you need to compute and maybe GPUs as well and someone will need to pay for it and I guess the passing Daniel we're doing this project I kept asking Daniel I'm like why is re-indexing with embedding so slow like where's my turbo button like really why is this still a problem it's 2024 almost 2025 why does embeddings take a long time yeah I remain a little confused why it's so like don't we just turn a knob and make a GPU go faster and then re-index with embeddings is just the same speed as re-indexing with keywords yeah but but also what Daniel says now but also like the fascinating part like one thought crossed my mind as you explained it Daniel is that in some sense you've built some sort of like a reasoning engine if I may call it that way maybe it's not fully you know reasoning like I don't know LLM start to do it that way or something but it's like the engine that looks at the query and examines its features and makes some some conclusions and then it looks also at the results it's not like you just you just you understood the query you set it over to the retriever side and then you hope for the best that there will be best results right but in some sense you you basically do this dynamic sort of reasoning on top of everything but but the lesson there you said and correct me if I'm wrong is that just by looking at the query features you could already achieve good results you don't need to look at the result features yes yes but wouldn't it be nice to look at those yeah I do love the idea of looking at both sides right we tend to focus on queries because I think that's the viewpoint of our industry we are very query centric in the search world it's all about the query and what can we get out of the query we really don't look at the results that much except to say are they good or bad and we're not particularly good about factoring in and what did the user do back into our algorithm and yeah I love that this is a little the dynamic thing that we're doing here I think it's a pointer to bring in more dynamic aspects to our algorithms where they actually can start evolving or changing or being very specific to very specific query types use cases time of year right and today that's very difficult to do only the most sophisticated to teams have sets of algorithms yeah but I also feel like I like what you said Eric like looking at results you know and reasoning about results and also what you understood about the query might lead to much better final representation of what you show to the user right because there are so many there are so many factors also beyond the query and results right like as you said season or you know you observed some patterns with the user the recent purchase history and so on and so forth yeah I mean it's very fascinating and also like if I continue to draw this analogy with lm world you know when you ask lm to to think through what it has done it may correct itself right by just looking at what it has produced because lm's are as someone said calculators for words so if you if you give it itself its own output and ask yeah exactly yeah like I can't wait to write a search algorithm that understands what they did the last time the user didn't like the results and so when you get a similar query for the same user do something new right try something new because whatever you were doing before the user didn't like yeah joke about if the user hates what you're giving them you might as well just return random docs because that'll be better than whatever you're doing right now yeah yeah at least you you have a chance there right with the random so what question I sort of have though in what we described how is it different than learning to rank other than learning to rank is about ranking one list and here we're ranking two lists is do I just conceptually have the role of learning to rank wrong between what learning to rank is and how the dynamic hybrid optimizer was working so I mean we are not re-ranking results right so that's what typically learning to rank does but what we are kind of doing is we are learning when when to let's say increase the weight on keyword search results or on your search results right so it's kind of a learn to lend learn to blend learn to search the new technology or we just done with the learning to nomenclature right and we like optimizer better than learning to blend maybe yeah so I'm not the one who's most creative in coming up with clever names so maybe it's maybe it's time for not learn to but blah blah blah optimizer and that's kind of how we ended up with the hybrid search optimizer right now but I wouldn't really have a good let's say argument against calling it learning to optimize hybrid search or something like that because that's kind of what the dynamic approach does right as we gather more data more clicks more of that those go into the features right we even use the the language of learning to rank right feature engineering right we use that language and we're building a model and you even mention right linear models in a forest and you know those are all the the words that I think of as oh it's learning to rank so interesting I think that's just it's interesting to see learning to rate maybe come back in a new way yeah yeah I'm learning to rank still something you can apply on top of the hybrid search optimizer right so it's not like we have any kind of substitute here so that's kind of still I think a very valuable tool in the mix and that's just now one way to really figure out what's the best way of getting to reasonable hybrid search results yeah but I was recently also thinking about this I wonder what's your hunt on that but learning to rank sort of depends on the training data and you usually collected from the past you don't collect it from the future right and so as you move into the future and patterns change you carry over that past weight that can actually go against the intent of your reasoning engine and and that's where I think that a lot of work needs to go in all of these directions but as you optimize your retrieving and your reasoning engine you know your query understanding maybe you should dial back the LTR a little bit or maybe you need to retrain it right there right then I don't know or retrain frequently enough so that you don't lose the invention strengths right yeah I think that's our challenge in a lot of these things yeah the historical approaches versus the predictive approaches right and you know which ones do you go with and how do you discount the historical if you have a bunch of new interesting data yeah yeah but I also like the limitations of the physical world I think from investment books I've read one key key takeaway lesson is that no one can predict the future if someone claims that they can do they probably lie but but again I guess there is still room for being more dynamic and is there something you guys want to also show I mean is this something we can look at visually or well theoretically we can no pressure I mean so this small demo here and I'm going to show the results first and then how we get to these results it basically takes in a user query my such application now is this Jupyter Notebook so it's not the most sophisticated search application but it calculates the query features then with these query features reaches out to the model to get the the best neural nest what these search features and with that retrieved response the query is built together and then sent to open search so we're just going to have a look at a couple of examples first and then we can have a look at the code so again this is now part of the ESC iData set my index has like 20,000 documents in it so it's not large it's only a subset of the ESC iData and when we send queries now in this case waterproof jacket in this method the method first as I just explained cause out to the model it retrieves the neural nest score and then builds the query together and then we have this HTML display here as you can see there are not images available for all of the products but what we can see here is that what a weatherproof sorry weatherproof jacket it gets a 50-50 search waiting also in this case 50% keyword 50% neural if we go for weatherproof jacket for the women the weights change so now we have 90% neural and only 10% keyword search weight and then oh and that's because the query became much more specific meaning that since we did add women there we are not expecting results for men or for kids right is that exactly so that's kind of what we can now infer maybe in what the model picks up here so we have a longer query we have a more specific query so it's not really looking at the words I'll say the model but at the features like query length are there numbers in it are there any special characters in it and so on so another one weatherproof jacket black and we also see that maybe results that we wouldn't really expect in the top here but again it's only a smallish proof of concept kind of thing that we are looking at here but we can see different queries that are similar from let's say meanings standpoint of you they retrieve different weights in that case and that's kind of the interesting thing and we can go for something completely different as well um iPhone case and we see like nice iPhone cases throughout the query and that goes with neuro.
7 and keyword.
3 and I don't know what's iPhone 15 roll max a is black so that would be a very very very specific query and here again the neural search rate increases whereas when we go for a very broad query so that's maybe one characteristic of the model that you that you can almost feel is the more specific we get the more neural weight it gets but also other features do play a role.
 Yeah yeah that's very interesting and that's how the open search query looks like so let's say the interesting part is that one here so we have a keyword query which is like I explained before searching in these couple of fields with different field weights a best fields query multi match with the end operator and then we have a neural query that retrieves the A100 based on the title embedding that we have and then the hybrid part is actually the search pipeline that normalizes in this case with the L2 norm and combines the results with the arithmetic mean based on the keyword search rate and neural search rate and that are here passed in as variables that are another method yeah predicts with model inference in that case.
 Yeah that's that's kind of the small but built in Jupyter notebook prototype that we have everything we built is like Eric just mentioned open source so we have a public repository that contains all but this one notebook actually but everything you need to train the models do the feature engineering calculate the search metrics so yeah everything you actually need so running this with the ESC IDATA set is possible for everyone and if you want to apply with your own data that of course is also possible so that's kind of what we are looking at next here so adoption in the industry and also hooking it up with the other part of this project which is namely the let's call it the evaluation part calculating implicit judgments based on user feedback so clicks queries stuff like that so that we also enable not only everyone to optimize hybrid search but also enable and empower everyone to well come up with judgments if you don't have any because that's kind of the the basics you need for any query you need.
Yeah and that's where keep it comes in. Shameless flag.
 So one of the things we actually have a reference implementation you know some of you all may have heard of chorus which is reference implementation for e-commerce search we did it in solar this we have an open search version and some of the stuff that you're seeing is sort of bleeding edge hot off the presses but we're working right now on getting that chorus for open search edition updated with some of these scripts and notebooks so you can just check it out run the quick start and then have everything and start playing with it so you don't have to build all the steps yourself so you can see how all the pieces fit together and so that's available be great if we can add a link in the line or notes for that as well to meet you.
 Yeah let's do that and just want to also to understand this search pipeline and all this you know mechanics of hybrid search that you guys implemented is it like a plugin to open search and what's the plan for it right so I guess you spoke to that like let's let's give it to as many users as possible what's your idea there.
 So hybrid search is available in open search so with let's say the the basic share so you can create a pipeline and say 70% keyword search weight and 30% neural search weight you can also define these on the fly but we currently have the limitation that we although we can hook up the model within a so-called ml inference pipeline in open search this ml inference pipeline can as of now not pass the predicted neural and keyword search weights to this pipeline but feature request is already out there and I assume that in one of the next open search versions we will have the possibility to not only what's already possible hook up the model within open search so that it from within open search you call out to the model to make inference you will retrieve the predicted neural and keyword search weights and then you can use these in your search pipeline so there is already an implementation plan out there there are open feature requests and if anyone wants to give these thumbs up to prioritize that within the open search community that would of course be greatly appreciated and I'm sure we can include these GitHub issues as well in the show notes.
Yeah for sure let's do that and we will call out that's how to call out to the community please vote if you care I hope there will be enough people who care about this.
Yeah exactly and then the you said everything is open source does that mean that the training scripts the algorithms the choices you make you can make there is also open source right and we can link to that as well yeah.
 Yes so everything with the I mean we of course didn't include all the thousand experiments but all the helpers at least that we used to run these 1000 experiments they are all in the repository out there for everyone to have a look at and maybe come up with even better ideas than we had so we definitely always love to hear these as well.
 Wow this is amazing this is a we can true sense you speak up to your name open source connections that's amazing like to me it's a ton of work that you could choose to hide as well right and work only with your clients and and nurture and iron out and everything and make a ton of money and continue on that but you choose to open source because you believe in the power of the community as well to enhance it that's amazing well said what's next you already said a couple of words but what's next and also do you want to address our audience what do you expect from me I think you know one of the things is you know as we've gotten into this you know we've we've found some rough spots in open search right open search has a strong ML component ML Commons project right but integrating it in sort of new and interesting ways like what Daniel was showing we're finding some rough spots it is interesting to me it does bring them in the do search engines what we call a search engine need to evolve to be more of an ML engine as well right I mean it feels to me like search has been revolutionized by machine learning and as we move into this direction of more calculating building models evaluating data on the fly do our search engines need to support those use cases and go beyond just the I I get a query I get documents I match them up and that's it right is there another layer of computation that we kind of need in the search engine versus bolting it on in some other environment with an ML ops pipeline and all the rest um and and I think that's in the interesting you know one place where I think open search is a little bit you know is definitely you know breaking some interesting ground is all the machine learning aspects to it but you know data processing and building models and all of that needs to maybe be a first class citizen of what we consider a search engine versus something done by some other system elsewhere because that's a lot more complexity and you know raises the barrier to adopting these things so I look forward to things like a hybrid optimizer just sort of being like what you do when you build your search engine of course you turn on the hybrid optimizer if it meets your use case and you have the judgments and other features that you need right versus oh a major engineering project that we're going to do this going to take us six months so um yeah yeah yeah um um and you know supporting that you know as Dan you highlighted the search quality evaluation framework that we're adding to open searches really exciting would love to come back to Metri and talk all about that on another show yeah let's do that I'm really excited to dive deeper into evil because I think in so many ways you need to start with evil especially if you have a search engine right out there uh to establish that uh you know baseline for yourself and then learn and introspect where things uh work or fail yeah make sure some of these models don't go and produce terrible yeah back shit crazy results right we had the risk that you know boosting up on neuralness might be terrible right we have to understand that and so we need to be much better about evaluation right we can't take our eye off the ball of speed right query speed does remain just sort of top of mind we also really need to be good at evaluation and I think for a lot of search teams that's kind of a new thing yes absolutely so the pooling and low search agents yeah and we do want to do what other thing I want to shout out yeah one other thing I want to shout out is that the next haystack conference uh the saved the date last week in April right um last week in April save the date went out um and we are looking for uh talk reviewers people who want to be reviewing the talk proposals it's a double blind process we get a couple people from the community so if that's something interested reach out to David Fisher uh he's running that process uh and call for proposals will be out I'm curious if this year haystack in Charlottesville might as well just be called hybrid stack like are we gonna have two days of talking about hybrid uh because R.
A.G.
 rag is rag is you know that's last year now we're on to hybrid uh or is there going to be something new so it's going to be interesting to see what what what kind of comes out of the community uh for this year's haystack it's also very interesting to to see this dynamic or this evolution because I think two or three years ago hybrid search was at the top of charts everyone was discussing it and then rags proceeded it and that just tells me that maybe we didn't dive deep enough into the topic which is let it go it passed and people thought oh that doesn't work we need we need something else and now it's rag rag rag everywhere but then rag also comes with its own you know limitation uh and now we have a new you know evolution level right with hybrid search you guys are optimizing uh that's amazing I was actually waiting for it I'm happy to see it happen and thanks for sharing the story let's come back to the evolve when you guys are ready I also expect that you will publish some blog posts around this topic about this topic so I'll you know I'll be happy to promote those as well and read them of course and learn terrific yeah thank you thank you very much thanks for coming to the show today and sharing this story it's very exciting and also showing the demo I like notebooks because they love you you know too quickly uh they say things and and have a feel of what's going on I'm glad that Eric still uses the cup that we gave him as a gift I love it it's like like you really see you really see the gift you gave like coming back and saying you did this and the person you gave it to is still enjoying that's amazing so awesome to meet you thank you very much thank you thank you and Daniel on yeah thanks for having us yeah thank you take care bye bye