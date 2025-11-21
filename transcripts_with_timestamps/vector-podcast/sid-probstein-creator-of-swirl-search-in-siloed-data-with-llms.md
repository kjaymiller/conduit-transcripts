---
description: '<p>Topics:</p><p>00:00 Intro</p><p>00:22 Quick demo of SWIRL on the
  summary transcript of this episode</p><p>01:29 Sid’s background</p><p>08:50 Enterprise
  vs Federated search</p><p>17:48 How vector search covers for missing folksonomy
  in enterprise data</p><p>26:07 Relevancy from vector search standpoint</p><p>31:58
  How ChatGPT improves programmer’s productivity</p><p>32:57 Demo!</p><p>45:23 Google
  PSE</p><p>53:10 Ideal user of  SWIRL</p><p>57:22 Where SWIRL sits architecturally</p><p>1:01:46
  How to evolve SWIRL with domain expertise</p><p>1:04:59 Reasons to go open source</p><p>1:10:54
  How SWIRL and Sid interact with ChatGPT</p><p>1:23:22 The magical question of WHY</p><p>1:27:58
  Sid’s announcements to the community</p><p>YouTube version: <a href="https://www.youtube.com/watch?v=vhQ5LM5pK_Y">https://www.youtube.com/watch?v=vhQ5LM5pK_Y</a></p><p>Design
  by Saurabh Rai: <a href="https://twitter.com/_srbhr_">https://twitter.com/_srbhr_</a>
  Check out his Resume Matcher project: <a href="https://www.resumematcher.fyi/">https://www.resumematcher.fyi/</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20230722_050704_2b439b236c5d93de6718cfecda81d779.jpg
pub_date: Sat, 22 Jul 2023 05:03:26 GMT
title: Sid Probstein - Creator of SWIRL - Search in siloed data with LLMs
url: https://rss.com/podcasts/vector-podcast/1047952
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 28.72, "text": " In
  this episode, you will learn about Swirl, MetaSearch Engine with large language
  models", "tokens": [50364, 682, 341, 3500, 11, 291, 486, 1466, 466, 3926, 1648,
  11, 6377, 64, 10637, 1178, 7659, 365, 2416, 2856, 5245, 51800], "temperature": 0.0,
  "avg_logprob": -0.3252786000569661, "compression_ratio": 1.0229885057471264, "no_speech_prob":
  0.08927268534898758}, {"id": 1, "seek": 2872, "start": 28.72, "end": 36.16, "text":
  " for your silo data. Here you can see how it works for the summary transcript of
  this episode", "tokens": [50364, 337, 428, 3425, 78, 1412, 13, 1692, 291, 393, 536,
  577, 309, 1985, 337, 264, 12691, 24444, 295, 341, 3500, 50736], "temperature": 0.0,
  "avg_logprob": -0.33554888346109046, "compression_ratio": 1.4162679425837321, "no_speech_prob":
  0.19984905421733856}, {"id": 2, "seek": 2872, "start": 36.16, "end": 40.16, "text":
  " created with the tool called ClearWord.", "tokens": [50736, 2942, 365, 264, 2290,
  1219, 14993, 54, 765, 13, 50936], "temperature": 0.0, "avg_logprob": -0.33554888346109046,
  "compression_ratio": 1.4162679425837321, "no_speech_prob": 0.19984905421733856},
  {"id": 3, "seek": 2872, "start": 40.16, "end": 46.08, "text": " Hello there, Vector
  Podcast Season 2, and today I''m super excited to be talking to", "tokens": [50936,
  2425, 456, 11, 691, 20814, 29972, 16465, 568, 11, 293, 965, 286, 478, 1687, 2919,
  281, 312, 1417, 281, 51232], "temperature": 0.0, "avg_logprob": -0.33554888346109046,
  "compression_ratio": 1.4162679425837321, "no_speech_prob": 0.19984905421733856},
  {"id": 4, "seek": 2872, "start": 46.08, "end": 53.44, "text": " CIPROP STING, the
  creator of Swirl Search. It''s a federated VectorSearch Engine.", "tokens": [51232,
  383, 9139, 7142, 47, 4904, 3017, 11, 264, 14181, 295, 3926, 1648, 17180, 13, 467,
  311, 257, 38024, 770, 691, 20814, 10637, 1178, 7659, 13, 51600], "temperature":
  0.0, "avg_logprob": -0.33554888346109046, "compression_ratio": 1.4162679425837321,
  "no_speech_prob": 0.19984905421733856}, {"id": 5, "seek": 5344, "start": 53.44,
  "end": 58.72, "text": " If I''m correct, but I would not hear more from CIT himself.
  Hello, CIT, how are you?", "tokens": [50364, 759, 286, 478, 3006, 11, 457, 286,
  576, 406, 1568, 544, 490, 383, 3927, 3647, 13, 2425, 11, 383, 3927, 11, 577, 366,
  291, 30, 50628], "temperature": 0.0, "avg_logprob": -0.2250738236510638, "compression_ratio":
  1.5427350427350428, "no_speech_prob": 0.04136265814304352}, {"id": 6, "seek": 5344,
  "start": 59.36, "end": 62.879999999999995, "text": " I''m doing great. It''s really
  great to be here. Thank you so much for inviting me.", "tokens": [50660, 286, 478,
  884, 869, 13, 467, 311, 534, 869, 281, 312, 510, 13, 1044, 291, 370, 709, 337, 18202,
  385, 13, 50836], "temperature": 0.0, "avg_logprob": -0.2250738236510638, "compression_ratio":
  1.5427350427350428, "no_speech_prob": 0.04136265814304352}, {"id": 7, "seek": 5344,
  "start": 62.879999999999995, "end": 71.36, "text": " Yeah, thanks for joining. I''m
  sure you are very busy building Swirl, and I''m really curious to", "tokens": [50836,
  865, 11, 3231, 337, 5549, 13, 286, 478, 988, 291, 366, 588, 5856, 2390, 3926, 1648,
  11, 293, 286, 478, 534, 6369, 281, 51260], "temperature": 0.0, "avg_logprob": -0.2250738236510638,
  "compression_ratio": 1.5427350427350428, "no_speech_prob": 0.04136265814304352},
  {"id": 8, "seek": 5344, "start": 71.36, "end": 77.92, "text": " learn more about
  it. I missed all the discussion, you know, how chat GPT is going to change things.",
  "tokens": [51260, 1466, 544, 466, 309, 13, 286, 6721, 439, 264, 5017, 11, 291, 458,
  11, 577, 5081, 26039, 51, 307, 516, 281, 1319, 721, 13, 51588], "temperature": 0.0,
  "avg_logprob": -0.2250738236510638, "compression_ratio": 1.5427350427350428, "no_speech_prob":
  0.04136265814304352}, {"id": 9, "seek": 7792, "start": 78.48, "end": 85.6, "text":
  " You know, is it going to conquer us or whatnot? But yeah, I mean, I''m really
  interested to hear", "tokens": [50392, 509, 458, 11, 307, 309, 516, 281, 24136,
  505, 420, 25882, 30, 583, 1338, 11, 286, 914, 11, 286, 478, 534, 3102, 281, 1568,
  50748], "temperature": 0.0, "avg_logprob": -0.15245074272155762, "compression_ratio":
  1.616326530612245, "no_speech_prob": 0.17178726196289062}, {"id": 10, "seek": 7792,
  "start": 85.6, "end": 91.76, "text": " how you guys are doing, how you guys are
  building this. And traditionally, we start with your background", "tokens": [50748,
  577, 291, 1074, 366, 884, 11, 577, 291, 1074, 366, 2390, 341, 13, 400, 19067, 11,
  321, 722, 365, 428, 3678, 51056], "temperature": 0.0, "avg_logprob": -0.15245074272155762,
  "compression_ratio": 1.616326530612245, "no_speech_prob": 0.17178726196289062},
  {"id": 11, "seek": 7792, "start": 91.76, "end": 98.64, "text": " because we really
  want to know how you got here. Absolutely, no. And it''s been an interesting", "tokens":
  [51056, 570, 321, 534, 528, 281, 458, 577, 291, 658, 510, 13, 7021, 11, 572, 13,
  400, 309, 311, 668, 364, 1880, 51400], "temperature": 0.0, "avg_logprob": -0.15245074272155762,
  "compression_ratio": 1.616326530612245, "no_speech_prob": 0.17178726196289062},
  {"id": 12, "seek": 7792, "start": 98.64, "end": 105.76, "text": " journey. Swirl
  actually is my, the 12th venture I''ve been lucky enough to work on. I started actually",
  "tokens": [51400, 4671, 13, 3926, 1648, 767, 307, 452, 11, 264, 2272, 392, 18474,
  286, 600, 668, 6356, 1547, 281, 589, 322, 13, 286, 1409, 767, 51756], "temperature":
  0.0, "avg_logprob": -0.15245074272155762, "compression_ratio": 1.616326530612245,
  "no_speech_prob": 0.17178726196289062}, {"id": 13, "seek": 10576, "start": 105.76,
  "end": 113.76, "text": " at a free email company called FreeMarkMail. You might
  remember Juno, our vastly more successful", "tokens": [50364, 412, 257, 1737, 3796,
  2237, 1219, 11551, 15168, 44, 864, 13, 509, 1062, 1604, 8492, 78, 11, 527, 41426,
  544, 4406, 50764], "temperature": 0.0, "avg_logprob": -0.16761928285871233, "compression_ratio":
  1.45, "no_speech_prob": 0.009068218991160393}, {"id": 14, "seek": 10576, "start":
  113.76, "end": 120.4, "text": " competitor. It was a great, great lesson in marketing
  and customer acquisition. But long story short,", "tokens": [50764, 27266, 13, 467,
  390, 257, 869, 11, 869, 6898, 294, 6370, 293, 5474, 21668, 13, 583, 938, 1657, 2099,
  11, 51096], "temperature": 0.0, "avg_logprob": -0.16761928285871233, "compression_ratio":
  1.45, "no_speech_prob": 0.009068218991160393}, {"id": 15, "seek": 10576, "start":
  120.4, "end": 128.08, "text": " you know, my dad was an MIT professor, and he suggested,
  or he was interested in computers,", "tokens": [51096, 291, 458, 11, 452, 3546,
  390, 364, 13100, 8304, 11, 293, 415, 10945, 11, 420, 415, 390, 3102, 294, 10807,
  11, 51480], "temperature": 0.0, "avg_logprob": -0.16761928285871233, "compression_ratio":
  1.45, "no_speech_prob": 0.009068218991160393}, {"id": 16, "seek": 12808, "start":
  128.16000000000003, "end": 138.16000000000003, "text": " and somewhere around, it
  was too long ago, but I was about 12 and I picked up a TRS 80 with 16K of RAM,",
  "tokens": [50368, 293, 4079, 926, 11, 309, 390, 886, 938, 2057, 11, 457, 286, 390,
  466, 2272, 293, 286, 6183, 493, 257, 15176, 50, 4688, 365, 3165, 42, 295, 14561,
  11, 50868], "temperature": 0.0, "avg_logprob": -0.18698006798239314, "compression_ratio":
  1.434782608695652, "no_speech_prob": 0.007260477636009455}, {"id": 17, "seek": 12808,
  "start": 138.16000000000003, "end": 144.64000000000001, "text": " I think, in a
  cassette tape for storage. And we went to a couple of, actually, we went to two",
  "tokens": [50868, 286, 519, 11, 294, 257, 40514, 7314, 337, 6725, 13, 400, 321,
  1437, 281, 257, 1916, 295, 11, 767, 11, 321, 1437, 281, 732, 51192], "temperature":
  0.0, "avg_logprob": -0.18698006798239314, "compression_ratio": 1.434782608695652,
  "no_speech_prob": 0.007260477636009455}, {"id": 18, "seek": 12808, "start": 144.64000000000001,
  "end": 149.76000000000002, "text": " classes together, and then he didn''t want
  to do it anymore, but I stayed with it. And I have always", "tokens": [51192, 5359,
  1214, 11, 293, 550, 415, 994, 380, 528, 281, 360, 309, 3602, 11, 457, 286, 9181,
  365, 309, 13, 400, 286, 362, 1009, 51448], "temperature": 0.0, "avg_logprob": -0.18698006798239314,
  "compression_ratio": 1.434782608695652, "no_speech_prob": 0.007260477636009455},
  {"id": 19, "seek": 14976, "start": 149.76, "end": 159.67999999999998, "text": "
  loved getting that computer to do things that we wanted to do. And so I guess ever
  since then,", "tokens": [50364, 4333, 1242, 300, 3820, 281, 360, 721, 300, 321,
  1415, 281, 360, 13, 400, 370, 286, 2041, 1562, 1670, 550, 11, 50860], "temperature":
  0.0, "avg_logprob": -0.1794012466279587, "compression_ratio": 1.58130081300813,
  "no_speech_prob": 0.0018941774033010006}, {"id": 20, "seek": 14976, "start": 159.67999999999998,
  "end": 165.04, "text": " I followed the tech path, so I was lucky enough to do my
  undergrad at MIT. I actually have an MBA,", "tokens": [50860, 286, 6263, 264, 7553,
  3100, 11, 370, 286, 390, 6356, 1547, 281, 360, 452, 14295, 412, 13100, 13, 286,
  767, 362, 364, 26674, 11, 51128], "temperature": 0.0, "avg_logprob": -0.1794012466279587,
  "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0018941774033010006},
  {"id": 21, "seek": 14976, "start": 165.04, "end": 173.12, "text": " though, I''m
  one of those MBA CTOs. And mostly I''ve worked building software and leading teams
  to", "tokens": [51128, 1673, 11, 286, 478, 472, 295, 729, 26674, 383, 15427, 82,
  13, 400, 5240, 286, 600, 2732, 2390, 4722, 293, 5775, 5491, 281, 51532], "temperature":
  0.0, "avg_logprob": -0.1794012466279587, "compression_ratio": 1.58130081300813,
  "no_speech_prob": 0.0018941774033010006}, {"id": 22, "seek": 14976, "start": 173.12,
  "end": 178.56, "text": " build products and services. So some of them have been
  a TIVIO, which is now actually service now,", "tokens": [51532, 1322, 3383, 293,
  3328, 13, 407, 512, 295, 552, 362, 668, 257, 314, 10375, 15167, 11, 597, 307, 586,
  767, 2643, 586, 11, 51804], "temperature": 0.0, "avg_logprob": -0.1794012466279587,
  "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0018941774033010006},
  {"id": 23, "seek": 17856, "start": 179.36, "end": 182.4, "text": " which is obviously
  one of the unicorns out there. They really", "tokens": [50404, 597, 307, 2745, 472,
  295, 264, 28122, 82, 484, 456, 13, 814, 534, 50556], "temperature": 0.0, "avg_logprob":
  -0.22655503890093634, "compression_ratio": 1.6072727272727272, "no_speech_prob":
  0.0016472884453833103}, {"id": 24, "seek": 17856, "start": 183.04, "end": 190.0,
  "text": " totally disrupted the knowledge base and help desk space. And it''s an
  incredible application", "tokens": [50588, 3879, 42271, 264, 3601, 3096, 293, 854,
  10026, 1901, 13, 400, 309, 311, 364, 4651, 3861, 50936], "temperature": 0.0, "avg_logprob":
  -0.22655503890093634, "compression_ratio": 1.6072727272727272, "no_speech_prob":
  0.0016472884453833103}, {"id": 25, "seek": 17856, "start": 190.0, "end": 196.88,
  "text": " of interesting core technology at the beginning, when things were whiteboardy.
  I''ve worked in a", "tokens": [50936, 295, 1880, 4965, 2899, 412, 264, 2863, 11,
  562, 721, 645, 2418, 3787, 88, 13, 286, 600, 2732, 294, 257, 51280], "temperature":
  0.0, "avg_logprob": -0.22655503890093634, "compression_ratio": 1.6072727272727272,
  "no_speech_prob": 0.0016472884453833103}, {"id": 26, "seek": 17856, "start": 196.88,
  "end": 201.68, "text": " couple of other search companies, and with some other search
  companies, I was lucky to spend a", "tokens": [51280, 1916, 295, 661, 3164, 3431,
  11, 293, 365, 512, 661, 3164, 3431, 11, 286, 390, 6356, 281, 3496, 257, 51520],
  "temperature": 0.0, "avg_logprob": -0.22655503890093634, "compression_ratio": 1.6072727272727272,
  "no_speech_prob": 0.0016472884453833103}, {"id": 27, "seek": 17856, "start": 201.68,
  "end": 207.12, "text": " little time with Mercedes Arabian over at BA Insight, which
  was a very cool and also Jeff Fried,", "tokens": [51520, 707, 565, 365, 22899, 8625,
  952, 670, 412, 21050, 9442, 397, 11, 597, 390, 257, 588, 1627, 293, 611, 7506, 17605,
  11, 51792], "temperature": 0.0, "avg_logprob": -0.22655503890093634, "compression_ratio":
  1.6072727272727272, "no_speech_prob": 0.0016472884453833103}, {"id": 28, "seek":
  20712, "start": 207.12, "end": 212.08, "text": " very cool company. And since I
  know those guys back from fast, another company that I worked at,", "tokens": [50364,
  588, 1627, 2237, 13, 400, 1670, 286, 458, 729, 1074, 646, 490, 2370, 11, 1071, 2237,
  300, 286, 2732, 412, 11, 50612], "temperature": 0.0, "avg_logprob": -0.24365767117204337,
  "compression_ratio": 1.5637860082304527, "no_speech_prob": 0.0026222297456115484},
  {"id": 29, "seek": 20712, "start": 212.08, "end": 219.68, "text": " now Microsoft,
  fast was one of the early players in enterprise search that had an excellent product",
  "tokens": [50612, 586, 8116, 11, 2370, 390, 472, 295, 264, 2440, 4150, 294, 14132,
  3164, 300, 632, 364, 7103, 1674, 50992], "temperature": 0.0, "avg_logprob": -0.24365767117204337,
  "compression_ratio": 1.5637860082304527, "no_speech_prob": 0.0026222297456115484},
  {"id": 30, "seek": 20712, "start": 219.68, "end": 225.36, "text": " that scaled
  and right as Google was sort of becoming a household name and just intermediate",
  "tokens": [50992, 300, 36039, 293, 558, 382, 3329, 390, 1333, 295, 5617, 257, 9888,
  1315, 293, 445, 19376, 51276], "temperature": 0.0, "avg_logprob": -0.24365767117204337,
  "compression_ratio": 1.5637860082304527, "no_speech_prob": 0.0026222297456115484},
  {"id": 31, "seek": 20712, "start": 225.36, "end": 233.44, "text": " everybody. We
  had the tool to build the catalog, the e-catalog, that mostly for publishers,",
  "tokens": [51276, 2201, 13, 492, 632, 264, 2290, 281, 1322, 264, 19746, 11, 264,
  308, 12, 18035, 44434, 11, 300, 5240, 337, 30421, 11, 51680], "temperature": 0.0,
  "avg_logprob": -0.24365767117204337, "compression_ratio": 1.5637860082304527, "no_speech_prob":
  0.0026222297456115484}, {"id": 32, "seek": 23344, "start": 233.44, "end": 237.92,
  "text": " and but then it really spread out and started to affect intranets. And
  it was truly there that I", "tokens": [50364, 293, 457, 550, 309, 534, 3974, 484,
  293, 1409, 281, 3345, 560, 4257, 1385, 13, 400, 309, 390, 4908, 456, 300, 286, 50588],
  "temperature": 0.0, "avg_logprob": -0.192283743518894, "compression_ratio": 1.582236842105263,
  "no_speech_prob": 0.01615281216800213}, {"id": 33, "seek": 23344, "start": 237.92,
  "end": 245.35999999999999, "text": " saw the power of search and how it could change
  almost everything from the business perspective.", "tokens": [50588, 1866, 264,
  1347, 295, 3164, 293, 577, 309, 727, 1319, 1920, 1203, 490, 264, 1606, 4585, 13,
  50960], "temperature": 0.0, "avg_logprob": -0.192283743518894, "compression_ratio":
  1.582236842105263, "no_speech_prob": 0.01615281216800213}, {"id": 34, "seek": 23344,
  "start": 245.92, "end": 250.8, "text": " You know, business intelligence and reporting
  and all of these systems that have been around for", "tokens": [50988, 509, 458,
  11, 1606, 7599, 293, 10031, 293, 439, 295, 613, 3652, 300, 362, 668, 926, 337, 51232],
  "temperature": 0.0, "avg_logprob": -0.192283743518894, "compression_ratio": 1.582236842105263,
  "no_speech_prob": 0.01615281216800213}, {"id": 35, "seek": 23344, "start": 250.8,
  "end": 257.04, "text": " 70, 80 years, they''re what we settle for. But everybody,
  you know, from Brin and Page on,", "tokens": [51232, 5285, 11, 4688, 924, 11, 436,
  434, 437, 321, 11852, 337, 13, 583, 2201, 11, 291, 458, 11, 490, 1603, 259, 293,
  21217, 322, 11, 51544], "temperature": 0.0, "avg_logprob": -0.192283743518894, "compression_ratio":
  1.582236842105263, "no_speech_prob": 0.01615281216800213}, {"id": 36, "seek": 23344,
  "start": 257.04, "end": 263.04, "text": " right, and way before that, we''re all
  inspired by that Star Trek computer. Why can''t we just ask it,", "tokens": [51544,
  558, 11, 293, 636, 949, 300, 11, 321, 434, 439, 7547, 538, 300, 5705, 25845, 3820,
  13, 1545, 393, 380, 321, 445, 1029, 309, 11, 51844], "temperature": 0.0, "avg_logprob":
  -0.192283743518894, "compression_ratio": 1.582236842105263, "no_speech_prob": 0.01615281216800213},
  {"id": 37, "seek": 26304, "start": 263.04, "end": 267.68, "text": " you know, it
  seems like it''s not that hard. And now of course, not to give away the lead, right?",
  "tokens": [50364, 291, 458, 11, 309, 2544, 411, 309, 311, 406, 300, 1152, 13, 400,
  586, 295, 1164, 11, 406, 281, 976, 1314, 264, 1477, 11, 558, 30, 50596], "temperature":
  0.0, "avg_logprob": -0.11837277292203502, "compression_ratio": 1.6928571428571428,
  "no_speech_prob": 0.0009549632668495178}, {"id": 38, "seek": 26304, "start": 267.68,
  "end": 272.32, "text": " But there''s definitely something doing that and it''s
  been a long time coming. But that is not", "tokens": [50596, 583, 456, 311, 2138,
  746, 884, 300, 293, 309, 311, 668, 257, 938, 565, 1348, 13, 583, 300, 307, 406,
  50828], "temperature": 0.0, "avg_logprob": -0.11837277292203502, "compression_ratio":
  1.6928571428571428, "no_speech_prob": 0.0009549632668495178}, {"id": 39, "seek":
  26304, "start": 273.04, "end": 280.08000000000004, "text": " structured data. Well,
  let''s not argue about the semantics, but it''s not what people refer to", "tokens":
  [50864, 18519, 1412, 13, 1042, 11, 718, 311, 406, 9695, 466, 264, 4361, 45298, 11,
  457, 309, 311, 406, 437, 561, 2864, 281, 51216], "temperature": 0.0, "avg_logprob":
  -0.11837277292203502, "compression_ratio": 1.6928571428571428, "no_speech_prob":
  0.0009549632668495178}, {"id": 40, "seek": 26304, "start": 280.08000000000004, "end":
  284.08000000000004, "text": " as structured. It''s not database data metrics and
  KPIs and sales numbers and things like that.", "tokens": [51216, 382, 18519, 13,
  467, 311, 406, 8149, 1412, 16367, 293, 41371, 6802, 293, 5763, 3547, 293, 721, 411,
  300, 13, 51416], "temperature": 0.0, "avg_logprob": -0.11837277292203502, "compression_ratio":
  1.6928571428571428, "no_speech_prob": 0.0009549632668495178}, {"id": 41, "seek":
  26304, "start": 285.28000000000003, "end": 290.08000000000004, "text": " I think
  that it was really at fast and also at Northern Light Technology, which is still
  going", "tokens": [51476, 286, 519, 300, 309, 390, 534, 412, 2370, 293, 611, 412,
  14335, 8279, 15037, 11, 597, 307, 920, 516, 51716], "temperature": 0.0, "avg_logprob":
  -0.11837277292203502, "compression_ratio": 1.6928571428571428, "no_speech_prob":
  0.0009549632668495178}, {"id": 42, "seek": 29008, "start": 290.08, "end": 294.0,
  "text": " strong, by the way, with some fantastic indexing search. And now they''re
  doing question answering.", "tokens": [50364, 2068, 11, 538, 264, 636, 11, 365,
  512, 5456, 8186, 278, 3164, 13, 400, 586, 436, 434, 884, 1168, 13430, 13, 50560],
  "temperature": 0.0, "avg_logprob": -0.14486512116023473, "compression_ratio": 1.6785714285714286,
  "no_speech_prob": 0.002761778188869357}, {"id": 43, "seek": 29008, "start": 295.28,
  "end": 299.91999999999996, "text": " First place I really touched search, right,
  was at Northern Light. It''s the human interface. And", "tokens": [50624, 2386,
  1081, 286, 534, 9828, 3164, 11, 558, 11, 390, 412, 14335, 8279, 13, 467, 311, 264,
  1952, 9226, 13, 400, 50856], "temperature": 0.0, "avg_logprob": -0.14486512116023473,
  "compression_ratio": 1.6785714285714286, "no_speech_prob": 0.002761778188869357},
  {"id": 44, "seek": 29008, "start": 300.64, "end": 306.15999999999997, "text": "
  we feel like it should be coming along faster. And now the text after many years
  of indexing", "tokens": [50892, 321, 841, 411, 309, 820, 312, 1348, 2051, 4663,
  13, 400, 586, 264, 2487, 934, 867, 924, 295, 8186, 278, 51168], "temperature": 0.0,
  "avg_logprob": -0.14486512116023473, "compression_ratio": 1.6785714285714286, "no_speech_prob":
  0.002761778188869357}, {"id": 45, "seek": 29008, "start": 306.15999999999997, "end":
  311.84, "text": " and vector search, right? And the advances driven by Google so
  much, right? Transformer architectures", "tokens": [51168, 293, 8062, 3164, 11,
  558, 30, 400, 264, 25297, 9555, 538, 3329, 370, 709, 11, 558, 30, 27938, 260, 6331,
  1303, 51452], "temperature": 0.0, "avg_logprob": -0.14486512116023473, "compression_ratio":
  1.6785714285714286, "no_speech_prob": 0.002761778188869357}, {"id": 46, "seek":
  29008, "start": 311.84, "end": 317.52, "text": " and vectors. And that has all come
  together into a pretty amazing place. And so", "tokens": [51452, 293, 18875, 13,
  400, 300, 575, 439, 808, 1214, 666, 257, 1238, 2243, 1081, 13, 400, 370, 51736],
  "temperature": 0.0, "avg_logprob": -0.14486512116023473, "compression_ratio": 1.6785714285714286,
  "no_speech_prob": 0.002761778188869357}, {"id": 47, "seek": 31752, "start": 318.47999999999996,
  "end": 324.79999999999995, "text": " long story short, that background led me to
  create swirl because I noticed a couple things.", "tokens": [50412, 938, 1657, 2099,
  11, 300, 3678, 4684, 385, 281, 1884, 30310, 570, 286, 5694, 257, 1916, 721, 13,
  50728], "temperature": 0.0, "avg_logprob": -0.2211082758528463, "compression_ratio":
  1.69377990430622, "no_speech_prob": 0.0010598271619528532}, {"id": 48, "seek": 31752,
  "start": 326.0, "end": 331.03999999999996, "text": " It really came down to three
  things. One is that there''s, there are silos, super silos,", "tokens": [50788,
  467, 534, 1361, 760, 281, 1045, 721, 13, 1485, 307, 300, 456, 311, 11, 456, 366,
  48893, 11, 1687, 48893, 11, 51040], "temperature": 0.0, "avg_logprob": -0.2211082758528463,
  "compression_ratio": 1.69377990430622, "no_speech_prob": 0.0010598271619528532},
  {"id": 49, "seek": 31752, "start": 331.03999999999996, "end": 336.79999999999995,
  "text": " like service now. Service now really did get a lot of the knowledge bases
  and a lot of those,", "tokens": [51040, 411, 2643, 586, 13, 9561, 586, 534, 630,
  483, 257, 688, 295, 264, 3601, 17949, 293, 257, 688, 295, 729, 11, 51328], "temperature":
  0.0, "avg_logprob": -0.2211082758528463, "compression_ratio": 1.69377990430622,
  "no_speech_prob": 0.0010598271619528532}, {"id": 50, "seek": 31752, "start": 337.52,
  "end": 341.52, "text": " a lot of the help desk, you know, the tickets base with
  the streams and tickets.", "tokens": [51364, 257, 688, 295, 264, 854, 10026, 11,
  291, 458, 11, 264, 12628, 3096, 365, 264, 15842, 293, 12628, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.2211082758528463, "compression_ratio": 1.69377990430622,
  "no_speech_prob": 0.0010598271619528532}, {"id": 51, "seek": 34152, "start": 342.32,
  "end": 348.71999999999997, "text": " M365 kind of won the files race at least right
  along with email. And I guess they''ve done very well.", "tokens": [50404, 376,
  11309, 20, 733, 295, 1582, 264, 7098, 4569, 412, 1935, 558, 2051, 365, 3796, 13,
  400, 286, 2041, 436, 600, 1096, 588, 731, 13, 50724], "temperature": 0.0, "avg_logprob":
  -0.16326441083635604, "compression_ratio": 1.5671140939597314, "no_speech_prob":
  0.004269641358405352}, {"id": 52, "seek": 34152, "start": 349.59999999999997, "end":
  354.08, "text": " Obviously, very impressive performance to build teams to the large
  community that it has developed.", "tokens": [50768, 7580, 11, 588, 8992, 3389,
  281, 1322, 5491, 281, 264, 2416, 1768, 300, 309, 575, 4743, 13, 50992], "temperature":
  0.0, "avg_logprob": -0.16326441083635604, "compression_ratio": 1.5671140939597314,
  "no_speech_prob": 0.004269641358405352}, {"id": 53, "seek": 34152, "start": 354.64,
  "end": 359.12, "text": " So, and then there are others, right? There''s certainly
  Salesforce, a great example of where most", "tokens": [51020, 407, 11, 293, 550,
  456, 366, 2357, 11, 558, 30, 821, 311, 3297, 40398, 11, 257, 869, 1365, 295, 689,
  881, 51244], "temperature": 0.0, "avg_logprob": -0.16326441083635604, "compression_ratio":
  1.5671140939597314, "no_speech_prob": 0.004269641358405352}, {"id": 54, "seek":
  34152, "start": 359.12, "end": 364.71999999999997, "text": " of the CRM data now
  lives. Snowflakes, another one, you can''t really get a copy of these. I mean,",
  "tokens": [51244, 295, 264, 14123, 44, 1412, 586, 2909, 13, 14827, 3423, 3419, 11,
  1071, 472, 11, 291, 393, 380, 534, 483, 257, 5055, 295, 613, 13, 286, 914, 11, 51524],
  "temperature": 0.0, "avg_logprob": -0.16326441083635604, "compression_ratio": 1.5671140939597314,
  "no_speech_prob": 0.004269641358405352}, {"id": 55, "seek": 34152, "start": 364.71999999999997,
  "end": 367.84, "text": " moving the data out from Snowflake is relatively easy,
  but the others,", "tokens": [51524, 2684, 264, 1412, 484, 490, 14827, 3423, 619,
  307, 7226, 1858, 11, 457, 264, 2357, 11, 51680], "temperature": 0.0, "avg_logprob":
  -0.16326441083635604, "compression_ratio": 1.5671140939597314, "no_speech_prob":
  0.004269641358405352}, {"id": 56, "seek": 36784, "start": 368.23999999999995, "end":
  374.64, "text": " there''s a complicated API there. Salesforce has thousands of
  tables. So, you can''t really get", "tokens": [50384, 456, 311, 257, 6179, 9362,
  456, 13, 40398, 575, 5383, 295, 8020, 13, 407, 11, 291, 393, 380, 534, 483, 50704],
  "temperature": 0.0, "avg_logprob": -0.1893357907311391, "compression_ratio": 1.6895306859205776,
  "no_speech_prob": 0.006047777831554413}, {"id": 57, "seek": 36784, "start": 374.64,
  "end": 380.0, "text": " that data anymore, but yet it has some of the most important
  ideas, concepts, and knowledge in your", "tokens": [50704, 300, 1412, 3602, 11,
  457, 1939, 309, 575, 512, 295, 264, 881, 1021, 3487, 11, 10392, 11, 293, 3601, 294,
  428, 50972], "temperature": 0.0, "avg_logprob": -0.1893357907311391, "compression_ratio":
  1.6895306859205776, "no_speech_prob": 0.006047777831554413}, {"id": 58, "seek":
  36784, "start": 380.0, "end": 385.91999999999996, "text": " entire company. So,
  that''s when I realized something that had been tried before. MetaSearch,", "tokens":
  [50972, 2302, 2237, 13, 407, 11, 300, 311, 562, 286, 5334, 746, 300, 632, 668, 3031,
  949, 13, 6377, 64, 10637, 1178, 11, 51268], "temperature": 0.0, "avg_logprob": -0.1893357907311391,
  "compression_ratio": 1.6895306859205776, "no_speech_prob": 0.006047777831554413},
  {"id": 59, "seek": 36784, "start": 385.91999999999996, "end": 389.76, "text": "
  right, or federated search. I think MetaSearch is clear up because now sometimes
  people say", "tokens": [51268, 558, 11, 420, 38024, 770, 3164, 13, 286, 519, 6377,
  64, 10637, 1178, 307, 1850, 493, 570, 586, 2171, 561, 584, 51460], "temperature":
  0.0, "avg_logprob": -0.1893357907311391, "compression_ratio": 1.6895306859205776,
  "no_speech_prob": 0.006047777831554413}, {"id": 60, "seek": 36784, "start": 390.47999999999996,
  "end": 397.59999999999997, "text": " federated search is about e-commerce federation.
  The MetaSearch was hard to do because of", "tokens": [51496, 38024, 770, 3164, 307,
  466, 308, 12, 26926, 4636, 5053, 13, 440, 6377, 64, 10637, 1178, 390, 1152, 281,
  360, 570, 295, 51852], "temperature": 0.0, "avg_logprob": -0.1893357907311391, "compression_ratio":
  1.6895306859205776, "no_speech_prob": 0.006047777831554413}, {"id": 61, "seek":
  39760, "start": 397.6, "end": 402.08000000000004, "text": " connectivity, right?
  Like it could take you months to just get somebody to change a network", "tokens":
  [50364, 21095, 11, 558, 30, 1743, 309, 727, 747, 291, 2493, 281, 445, 483, 2618,
  281, 1319, 257, 3209, 50588], "temperature": 0.0, "avg_logprob": -0.16252016813858697,
  "compression_ratio": 1.5766666666666667, "no_speech_prob": 0.000260751461610198},
  {"id": 62, "seek": 39760, "start": 402.08000000000004, "end": 406.56, "text": "
  thing or to put a VPN in place or either change permissions. That was expensive
  in large enterprise.", "tokens": [50588, 551, 420, 281, 829, 257, 24512, 294, 1081,
  420, 2139, 1319, 32723, 13, 663, 390, 5124, 294, 2416, 14132, 13, 50812], "temperature":
  0.0, "avg_logprob": -0.16252016813858697, "compression_ratio": 1.5766666666666667,
  "no_speech_prob": 0.000260751461610198}, {"id": 63, "seek": 39760, "start": 407.12,
  "end": 411.6, "text": " But now, especially with public services, pretty much everything
  has an API. The perimeter", "tokens": [50840, 583, 586, 11, 2318, 365, 1908, 3328,
  11, 1238, 709, 1203, 575, 364, 9362, 13, 440, 32404, 51064], "temperature": 0.0,
  "avg_logprob": -0.16252016813858697, "compression_ratio": 1.5766666666666667, "no_speech_prob":
  0.000260751461610198}, {"id": 64, "seek": 39760, "start": 411.6, "end": 416.40000000000003,
  "text": " doesn''t exist the way I used to. And so, you can query everything. So,
  that left the problem", "tokens": [51064, 1177, 380, 2514, 264, 636, 286, 1143,
  281, 13, 400, 370, 11, 291, 393, 14581, 1203, 13, 407, 11, 300, 1411, 264, 1154,
  51304], "temperature": 0.0, "avg_logprob": -0.16252016813858697, "compression_ratio":
  1.5766666666666667, "no_speech_prob": 0.000260751461610198}, {"id": 65, "seek":
  39760, "start": 416.40000000000003, "end": 421.76000000000005, "text": " of can
  you make sense of things? And that''s of course, what we''re here about, right,
  is vectors.", "tokens": [51304, 295, 393, 291, 652, 2020, 295, 721, 30, 400, 300,
  311, 295, 1164, 11, 437, 321, 434, 510, 466, 11, 558, 11, 307, 18875, 13, 51572],
  "temperature": 0.0, "avg_logprob": -0.16252016813858697, "compression_ratio": 1.5766666666666667,
  "no_speech_prob": 0.000260751461610198}, {"id": 66, "seek": 42176, "start": 421.92,
  "end": 428.08, "text": " The power of vector search and vector similarity, specifically,
  right, self-cosign vector", "tokens": [50372, 440, 1347, 295, 8062, 3164, 293, 8062,
  32194, 11, 4682, 11, 558, 11, 2698, 12, 6877, 788, 8062, 50680], "temperature":
  0.0, "avg_logprob": -0.20515808377947126, "compression_ratio": 1.7045454545454546,
  "no_speech_prob": 0.058903735131025314}, {"id": 67, "seek": 42176, "start": 428.08,
  "end": 432.88, "text": " similarity that we use in Swirl to make sense of completely
  disparate and very, very,", "tokens": [50680, 32194, 300, 321, 764, 294, 3926, 1648,
  281, 652, 2020, 295, 2584, 14548, 473, 293, 588, 11, 588, 11, 50920], "temperature":
  0.0, "avg_logprob": -0.20515808377947126, "compression_ratio": 1.7045454545454546,
  "no_speech_prob": 0.058903735131025314}, {"id": 68, "seek": 42176, "start": 434.0,
  "end": 438.08, "text": " very incompatible results, if you will. And it''s shocking
  how well it works.", "tokens": [50976, 588, 40393, 267, 964, 3542, 11, 498, 291,
  486, 13, 400, 309, 311, 18776, 577, 731, 309, 1985, 13, 51180], "temperature": 0.0,
  "avg_logprob": -0.20515808377947126, "compression_ratio": 1.7045454545454546, "no_speech_prob":
  0.058903735131025314}, {"id": 69, "seek": 42176, "start": 438.71999999999997, "end":
  442.4, "text": " That that''s when I saw it work, I said there''s more to this than
  I thought it now. It seems", "tokens": [51212, 663, 300, 311, 562, 286, 1866, 309,
  589, 11, 286, 848, 456, 311, 544, 281, 341, 813, 286, 1194, 309, 586, 13, 467, 2544,
  51396], "temperature": 0.0, "avg_logprob": -0.20515808377947126, "compression_ratio":
  1.7045454545454546, "no_speech_prob": 0.058903735131025314}, {"id": 70, "seek":
  42176, "start": 442.4, "end": 446.08, "text": " I''m not the only one. So, but anyway,
  that''s a little bit of the story in my background. I hope", "tokens": [51396, 286,
  478, 406, 264, 787, 472, 13, 407, 11, 457, 4033, 11, 300, 311, 257, 707, 857, 295,
  264, 1657, 294, 452, 3678, 13, 286, 1454, 51580], "temperature": 0.0, "avg_logprob":
  -0.20515808377947126, "compression_ratio": 1.7045454545454546, "no_speech_prob":
  0.058903735131025314}, {"id": 71, "seek": 42176, "start": 446.08, "end": 450.4,
  "text": " that that made some sense. Yeah, it''s very solid background. You reminded
  me of one,", "tokens": [51580, 300, 300, 1027, 512, 2020, 13, 865, 11, 309, 311,
  588, 5100, 3678, 13, 509, 15920, 385, 295, 472, 11, 51796], "temperature": 0.0,
  "avg_logprob": -0.20515808377947126, "compression_ratio": 1.7045454545454546, "no_speech_prob":
  0.058903735131025314}, {"id": 72, "seek": 45040, "start": 450.96, "end": 455.67999999999995,
  "text": " I don''t remember the name of that computer, but like didn''t have the
  display the way we have today,", "tokens": [50392, 286, 500, 380, 1604, 264, 1315,
  295, 300, 3820, 11, 457, 411, 994, 380, 362, 264, 4674, 264, 636, 321, 362, 965,
  11, 50628], "temperature": 0.0, "avg_logprob": -0.19299275324894832, "compression_ratio":
  1.6506849315068493, "no_speech_prob": 0.05183985456824303}, {"id": 73, "seek": 45040,
  "start": 455.67999999999995, "end": 461.2, "text": " right? It just had the keyboard.
  And then it had the cassette. And so, my friend and I were", "tokens": [50628, 558,
  30, 467, 445, 632, 264, 10186, 13, 400, 550, 309, 632, 264, 40514, 13, 400, 370,
  11, 452, 1277, 293, 286, 645, 50904], "temperature": 0.0, "avg_logprob": -0.19299275324894832,
  "compression_ratio": 1.6506849315068493, "no_speech_prob": 0.05183985456824303},
  {"id": 74, "seek": 45040, "start": 461.2, "end": 467.12, "text": " sitting there
  for several minutes to boot it. And then there was some game like Mario or whatever.",
  "tokens": [50904, 3798, 456, 337, 2940, 2077, 281, 11450, 309, 13, 400, 550, 456,
  390, 512, 1216, 411, 9343, 420, 2035, 13, 51200], "temperature": 0.0, "avg_logprob":
  -0.19299275324894832, "compression_ratio": 1.6506849315068493, "no_speech_prob":
  0.05183985456824303}, {"id": 75, "seek": 45040, "start": 468.56, "end": 474.88,
  "text": " That was on the cool Apple twos. I was always envious of the Apple two,
  you know, kids. Because", "tokens": [51272, 663, 390, 322, 264, 1627, 6373, 683,
  329, 13, 286, 390, 1009, 465, 1502, 295, 264, 6373, 732, 11, 291, 458, 11, 2301,
  13, 1436, 51588], "temperature": 0.0, "avg_logprob": -0.19299275324894832, "compression_ratio":
  1.6506849315068493, "no_speech_prob": 0.05183985456824303}, {"id": 76, "seek": 45040,
  "start": 474.88, "end": 479.76, "text": " you''re right, on the TRS-80, we only
  had block graphics. It was hilarious. But it didn''t move a", "tokens": [51588,
  291, 434, 558, 11, 322, 264, 15176, 50, 12, 4702, 11, 321, 787, 632, 3461, 11837,
  13, 467, 390, 19796, 13, 583, 309, 994, 380, 1286, 257, 51832], "temperature": 0.0,
  "avg_logprob": -0.19299275324894832, "compression_ratio": 1.6506849315068493, "no_speech_prob":
  0.05183985456824303}, {"id": 77, "seek": 47976, "start": 479.76, "end": 484.8, "text":
  " little bit faster in a way. Like you get to wait a long time for Apple upgrades.
  But I remember", "tokens": [50364, 707, 857, 4663, 294, 257, 636, 13, 1743, 291,
  483, 281, 1699, 257, 938, 565, 337, 6373, 24868, 13, 583, 286, 1604, 50616], "temperature":
  0.0, "avg_logprob": -0.1847791515412878, "compression_ratio": 1.595890410958904,
  "no_speech_prob": 0.0028061617631465197}, {"id": 78, "seek": 47976, "start": 485.92,
  "end": 491.28, "text": " the TRS-80, there was an incredible ecosystem of things
  you could add to it. So, memory. And then", "tokens": [50672, 264, 15176, 50, 12,
  4702, 11, 456, 390, 364, 4651, 11311, 295, 721, 291, 727, 909, 281, 309, 13, 407,
  11, 4675, 13, 400, 550, 50940], "temperature": 0.0, "avg_logprob": -0.1847791515412878,
  "compression_ratio": 1.595890410958904, "no_speech_prob": 0.0028061617631465197},
  {"id": 79, "seek": 47976, "start": 491.28, "end": 495.68, "text": " there was a
  company called Percom that put out disk drives. Wow, a disk drive. That was a game",
  "tokens": [50940, 456, 390, 257, 2237, 1219, 3026, 1112, 300, 829, 484, 12355, 11754,
  13, 3153, 11, 257, 12355, 3332, 13, 663, 390, 257, 1216, 51160], "temperature":
  0.0, "avg_logprob": -0.1847791515412878, "compression_ratio": 1.595890410958904,
  "no_speech_prob": 0.0028061617631465197}, {"id": 80, "seek": 47976, "start": 495.68,
  "end": 500.64, "text": " changer if you played with a cassette recorder. Although,
  who didn''t love switching your parents''", "tokens": [51160, 22822, 498, 291, 3737,
  365, 257, 40514, 37744, 13, 5780, 11, 567, 994, 380, 959, 16493, 428, 3152, 6, 51408],
  "temperature": 0.0, "avg_logprob": -0.1847791515412878, "compression_ratio": 1.595890410958904,
  "no_speech_prob": 0.0028061617631465197}, {"id": 81, "seek": 47976, "start": 500.64,
  "end": 503.59999999999997, "text": " cassettes with the with the data tape so they''d
  put it on in the car and we go,", "tokens": [51408, 21943, 16049, 365, 264, 365,
  264, 1412, 7314, 370, 436, 1116, 829, 309, 322, 294, 264, 1032, 293, 321, 352, 11,
  51556], "temperature": 0.0, "avg_logprob": -0.1847791515412878, "compression_ratio":
  1.595890410958904, "no_speech_prob": 0.0028061617631465197}, {"id": 82, "seek":
  50360, "start": 503.6, "end": 509.44, "text": " okay, are they going to stop and
  turn that off? It was a hilarious prank. A great way to get", "tokens": [50364,
  1392, 11, 366, 436, 516, 281, 1590, 293, 1261, 300, 766, 30, 467, 390, 257, 19796,
  19794, 13, 316, 869, 636, 281, 483, 50656], "temperature": 0.0, "avg_logprob": -0.2387035157945421,
  "compression_ratio": 1.6529209621993126, "no_speech_prob": 0.010534117929637432},
  {"id": 83, "seek": 50360, "start": 509.44, "end": 516.0, "text": " some sound. But
  disk drives then gave, right? First, there were the five in a quarter or actually",
  "tokens": [50656, 512, 1626, 13, 583, 12355, 11754, 550, 2729, 11, 558, 30, 2386,
  11, 456, 645, 264, 1732, 294, 257, 6555, 420, 767, 50984], "temperature": 0.0, "avg_logprob":
  -0.2387035157945421, "compression_ratio": 1.6529209621993126, "no_speech_prob":
  0.010534117929637432}, {"id": 84, "seek": 50360, "start": 516.0, "end": 519.9200000000001,
  "text": " eight inch, then five in a quarter. And then finally, they''ve got to
  the cassette. I was at that", "tokens": [50984, 3180, 7227, 11, 550, 1732, 294,
  257, 6555, 13, 400, 550, 2721, 11, 436, 600, 658, 281, 264, 40514, 13, 286, 390,
  412, 300, 51180], "temperature": 0.0, "avg_logprob": -0.2387035157945421, "compression_ratio":
  1.6529209621993126, "no_speech_prob": 0.010534117929637432}, {"id": 85, "seek":
  50360, "start": 519.9200000000001, "end": 526.4, "text": " point, it was sort of
  replaced, right? Then the IBM PC showed up. And that was a bit of a game", "tokens":
  [51180, 935, 11, 309, 390, 1333, 295, 10772, 11, 558, 30, 1396, 264, 23487, 6465,
  4712, 493, 13, 400, 300, 390, 257, 857, 295, 257, 1216, 51504], "temperature": 0.0,
  "avg_logprob": -0.2387035157945421, "compression_ratio": 1.6529209621993126, "no_speech_prob":
  0.010534117929637432}, {"id": 86, "seek": 50360, "start": 526.4, "end": 533.0400000000001,
  "text": " changer. But the Apple always had better graphics. Yeah, absolutely. I
  just wanted to come back to", "tokens": [51504, 22822, 13, 583, 264, 6373, 1009,
  632, 1101, 11837, 13, 865, 11, 3122, 13, 286, 445, 1415, 281, 808, 646, 281, 51836],
  "temperature": 0.0, "avg_logprob": -0.2387035157945421, "compression_ratio": 1.6529209621993126,
  "no_speech_prob": 0.010534117929637432}, {"id": 87, "seek": 53360, "start": 533.6,
  "end": 538.32, "text": " what you just said about federated search and enterprise
  search. I think I remember hearing about", "tokens": [50364, 437, 291, 445, 848,
  466, 38024, 770, 3164, 293, 14132, 3164, 13, 286, 519, 286, 1604, 4763, 466, 50600],
  "temperature": 0.0, "avg_logprob": -0.12487641334533692, "compression_ratio": 1.592,
  "no_speech_prob": 0.047529760748147964}, {"id": 88, "seek": 53360, "start": 538.32,
  "end": 544.88, "text": " enterprise search was it like 15, 16, 17 years ago, I don''t
  remember in the university when one of", "tokens": [50600, 14132, 3164, 390, 309,
  411, 2119, 11, 3165, 11, 3282, 924, 2057, 11, 286, 500, 380, 1604, 294, 264, 5454,
  562, 472, 295, 50928], "temperature": 0.0, "avg_logprob": -0.12487641334533692,
  "compression_ratio": 1.592, "no_speech_prob": 0.047529760748147964}, {"id": 89,
  "seek": 53360, "start": 544.88, "end": 551.0400000000001, "text": " my supervisors
  was focusing on it and he was saying, this is the next big thing. And once it''s
  figured", "tokens": [50928, 452, 42218, 390, 8416, 322, 309, 293, 415, 390, 1566,
  11, 341, 307, 264, 958, 955, 551, 13, 400, 1564, 309, 311, 8932, 51236], "temperature":
  0.0, "avg_logprob": -0.12487641334533692, "compression_ratio": 1.592, "no_speech_prob":
  0.047529760748147964}, {"id": 90, "seek": 53360, "start": 551.0400000000001, "end":
  561.0400000000001, "text": " out, you know, we will be rich. But somehow it didn''t
  happen. And then later in my career, I heard", "tokens": [51236, 484, 11, 291, 458,
  11, 321, 486, 312, 4593, 13, 583, 6063, 309, 994, 380, 1051, 13, 400, 550, 1780,
  294, 452, 3988, 11, 286, 2198, 51736], "temperature": 0.0, "avg_logprob": -0.12487641334533692,
  "compression_ratio": 1.592, "no_speech_prob": 0.047529760748147964}, {"id": 91,
  "seek": 56104, "start": 561.52, "end": 569.52, "text": " term federated search in
  connection to, okay, we have our own search engine, we have clients data,", "tokens":
  [50388, 1433, 38024, 770, 3164, 294, 4984, 281, 11, 1392, 11, 321, 362, 527, 1065,
  3164, 2848, 11, 321, 362, 6982, 1412, 11, 50788], "temperature": 0.0, "avg_logprob":
  -0.172983447710673, "compression_ratio": 1.579591836734694, "no_speech_prob": 0.013129369355738163},
  {"id": 92, "seek": 56104, "start": 570.0799999999999, "end": 575.68, "text": " can
  we combine the two without needing them to upload their data to our servers? Because
  in some", "tokens": [50816, 393, 321, 10432, 264, 732, 1553, 18006, 552, 281, 6580,
  641, 1412, 281, 527, 15909, 30, 1436, 294, 512, 51096], "temperature": 0.0, "avg_logprob":
  -0.172983447710673, "compression_ratio": 1.579591836734694, "no_speech_prob": 0.013129369355738163},
  {"id": 93, "seek": 56104, "start": 575.68, "end": 581.5999999999999, "text": " cases,
  they wouldn''t trust us, you know, securing it''s enough and so on. So forest. And
  then we", "tokens": [51096, 3331, 11, 436, 2759, 380, 3361, 505, 11, 291, 458, 11,
  33640, 309, 311, 1547, 293, 370, 322, 13, 407, 6719, 13, 400, 550, 321, 51392],
  "temperature": 0.0, "avg_logprob": -0.172983447710673, "compression_ratio": 1.579591836734694,
  "no_speech_prob": 0.013129369355738163}, {"id": 94, "seek": 56104, "start": 581.5999999999999,
  "end": 588.7199999999999, "text": " were confronted with the fact that maybe it
  will incur quite a bit of latency. And also even in", "tokens": [51392, 645, 31257,
  365, 264, 1186, 300, 1310, 309, 486, 35774, 1596, 257, 857, 295, 27043, 13, 400,
  611, 754, 294, 51748], "temperature": 0.0, "avg_logprob": -0.172983447710673, "compression_ratio":
  1.579591836734694, "no_speech_prob": 0.013129369355738163}, {"id": 95, "seek": 58872,
  "start": 588.72, "end": 594.5600000000001, "text": " the first place, how we would
  build this. But you know, like before we even get there, how do you", "tokens":
  [50364, 264, 700, 1081, 11, 577, 321, 576, 1322, 341, 13, 583, 291, 458, 11, 411,
  949, 321, 754, 483, 456, 11, 577, 360, 291, 50656], "temperature": 0.0, "avg_logprob":
  -0.15520266200719254, "compression_ratio": 1.670995670995671, "no_speech_prob":
  0.000723956385627389}, {"id": 96, "seek": 58872, "start": 595.36, "end": 603.2,
  "text": " relate enterprise search versus federated search? So, so I think they''re,
  they''re different in", "tokens": [50696, 10961, 14132, 3164, 5717, 38024, 770,
  3164, 30, 407, 11, 370, 286, 519, 436, 434, 11, 436, 434, 819, 294, 51088], "temperature":
  0.0, "avg_logprob": -0.15520266200719254, "compression_ratio": 1.670995670995671,
  "no_speech_prob": 0.000723956385627389}, {"id": 97, "seek": 58872, "start": 603.2,
  "end": 608.64, "text": " that enterprise search is about a realm. Right. Enterprise
  search means usually not public sources.", "tokens": [51088, 300, 14132, 3164, 307,
  466, 257, 15355, 13, 1779, 13, 26696, 3164, 1355, 2673, 406, 1908, 7139, 13, 51360],
  "temperature": 0.0, "avg_logprob": -0.15520266200719254, "compression_ratio": 1.670995670995671,
  "no_speech_prob": 0.000723956385627389}, {"id": 98, "seek": 58872, "start": 609.6800000000001,
  "end": 615.0400000000001, "text": " And I think it''s important to differentiate
  the problems of the large enterprise and even the", "tokens": [51412, 400, 286,
  519, 309, 311, 1021, 281, 23203, 264, 2740, 295, 264, 2416, 14132, 293, 754, 264,
  51680], "temperature": 0.0, "avg_logprob": -0.15520266200719254, "compression_ratio":
  1.670995670995671, "no_speech_prob": 0.000723956385627389}, {"id": 99, "seek": 61504,
  "start": 615.04, "end": 620.48, "text": " medium enterprise are not the same as
  the sort of small, small and medium enterprise enterprise.", "tokens": [50364, 6399,
  14132, 366, 406, 264, 912, 382, 264, 1333, 295, 1359, 11, 1359, 293, 6399, 14132,
  14132, 13, 50636], "temperature": 0.0, "avg_logprob": -0.1115419864654541, "compression_ratio":
  1.7179487179487178, "no_speech_prob": 0.0004416282754391432}, {"id": 100, "seek":
  61504, "start": 621.28, "end": 624.88, "text": " Maybe that''s not a great dividing
  line. But definitely the large enterprise has a very different", "tokens": [50676,
  2704, 300, 311, 406, 257, 869, 26764, 1622, 13, 583, 2138, 264, 2416, 14132, 575,
  257, 588, 819, 50856], "temperature": 0.0, "avg_logprob": -0.1115419864654541, "compression_ratio":
  1.7179487179487178, "no_speech_prob": 0.0004416282754391432}, {"id": 101, "seek":
  61504, "start": 624.88, "end": 628.7199999999999, "text": " set of problems. It''s
  so much more about, you know, global distribution and languages and", "tokens":
  [50856, 992, 295, 2740, 13, 467, 311, 370, 709, 544, 466, 11, 291, 458, 11, 4338,
  7316, 293, 8650, 293, 51048], "temperature": 0.0, "avg_logprob": -0.1115419864654541,
  "compression_ratio": 1.7179487179487178, "no_speech_prob": 0.0004416282754391432},
  {"id": 102, "seek": 61504, "start": 628.7199999999999, "end": 635.36, "text": "
  regulation. If you''re a, you know, small company like like swirl ink, we have five
  people,", "tokens": [51048, 15062, 13, 759, 291, 434, 257, 11, 291, 458, 11, 1359,
  2237, 411, 411, 30310, 11276, 11, 321, 362, 1732, 561, 11, 51380], "temperature":
  0.0, "avg_logprob": -0.1115419864654541, "compression_ratio": 1.7179487179487178,
  "no_speech_prob": 0.0004416282754391432}, {"id": 103, "seek": 61504, "start": 635.36,
  "end": 640.24, "text": " we can work off of almost anything. I mean, and we don''t
  have the silo problem because we just", "tokens": [51380, 321, 393, 589, 766, 295,
  1920, 1340, 13, 286, 914, 11, 293, 321, 500, 380, 362, 264, 3425, 78, 1154, 570,
  321, 445, 51624], "temperature": 0.0, "avg_logprob": -0.1115419864654541, "compression_ratio":
  1.7179487179487178, "no_speech_prob": 0.0004416282754391432}, {"id": 104, "seek":
  64024, "start": 640.32, "end": 644.96, "text": " have picked, you know, we have
  four. But it''s interesting. We do still have the silo problem,", "tokens": [50368,
  362, 6183, 11, 291, 458, 11, 321, 362, 1451, 13, 583, 309, 311, 1880, 13, 492, 360,
  920, 362, 264, 3425, 78, 1154, 11, 50600], "temperature": 0.0, "avg_logprob": -0.11713124884933722,
  "compression_ratio": 1.6354515050167224, "no_speech_prob": 0.0015854957746341825},
  {"id": 105, "seek": 64024, "start": 644.96, "end": 649.36, "text": " right. And
  as I''m going to show you, just when we were trying to find the steering document
  for this", "tokens": [50600, 558, 13, 400, 382, 286, 478, 516, 281, 855, 291, 11,
  445, 562, 321, 645, 1382, 281, 915, 264, 14823, 4166, 337, 341, 50820], "temperature":
  0.0, "avg_logprob": -0.11713124884933722, "compression_ratio": 1.6354515050167224,
  "no_speech_prob": 0.0015854957746341825}, {"id": 106, "seek": 64024, "start": 649.36,
  "end": 654.0, "text": " discussion, I realized I was hunting around which silo did
  I put it in instead of just going to", "tokens": [50820, 5017, 11, 286, 5334, 286,
  390, 12599, 926, 597, 3425, 78, 630, 286, 829, 309, 294, 2602, 295, 445, 516, 281,
  51052], "temperature": 0.0, "avg_logprob": -0.11713124884933722, "compression_ratio":
  1.6354515050167224, "no_speech_prob": 0.0015854957746341825}, {"id": 107, "seek":
  64024, "start": 654.0, "end": 660.72, "text": " search. So it''s funny that we''ve
  trained ourselves to work that way. That I think it''s a reflection", "tokens":
  [51052, 3164, 13, 407, 309, 311, 4074, 300, 321, 600, 8895, 4175, 281, 589, 300,
  636, 13, 663, 286, 519, 309, 311, 257, 12914, 51388], "temperature": 0.0, "avg_logprob":
  -0.11713124884933722, "compression_ratio": 1.6354515050167224, "no_speech_prob":
  0.0015854957746341825}, {"id": 108, "seek": 64024, "start": 660.72, "end": 667.28,
  "text": " of the reality that in the large enterprise, it''s exactly what you said
  entitlements are extremely", "tokens": [51388, 295, 264, 4103, 300, 294, 264, 2416,
  14132, 11, 309, 311, 2293, 437, 291, 848, 14789, 17988, 366, 4664, 51716], "temperature":
  0.0, "avg_logprob": -0.11713124884933722, "compression_ratio": 1.6354515050167224,
  "no_speech_prob": 0.0015854957746341825}, {"id": 109, "seek": 66728, "start": 667.28,
  "end": 674.0799999999999, "text": " important. You''re talking about crown jewel
  data like PL product data or customer feedback.", "tokens": [50364, 1021, 13, 509,
  434, 1417, 466, 11841, 16010, 1412, 411, 6999, 1674, 1412, 420, 5474, 5824, 13,
  50704], "temperature": 0.0, "avg_logprob": -0.13779831840878443, "compression_ratio":
  1.6297577854671281, "no_speech_prob": 0.0014001547824591398}, {"id": 110, "seek":
  66728, "start": 674.0799999999999, "end": 680.24, "text": " CRM data is much less
  sensitive in some ways. Also data that you might purchase, it''s very common", "tokens":
  [50704, 14123, 44, 1412, 307, 709, 1570, 9477, 294, 512, 2098, 13, 2743, 1412, 300,
  291, 1062, 8110, 11, 309, 311, 588, 2689, 51012], "temperature": 0.0, "avg_logprob":
  -0.13779831840878443, "compression_ratio": 1.6297577854671281, "no_speech_prob":
  0.0014001547824591398}, {"id": 111, "seek": 66728, "start": 680.24, "end": 685.52,
  "text": " for companies to build and or purchase data sets and assemble them or
  assemble derivative sets.", "tokens": [51012, 337, 3431, 281, 1322, 293, 420, 8110,
  1412, 6352, 293, 22364, 552, 420, 22364, 13760, 6352, 13, 51276], "temperature":
  0.0, "avg_logprob": -0.13779831840878443, "compression_ratio": 1.6297577854671281,
  "no_speech_prob": 0.0014001547824591398}, {"id": 112, "seek": 66728, "start": 685.52,
  "end": 691.28, "text": " These would be incredibly valuable for lots of uses. The
  simplest one, right, usually as sales", "tokens": [51276, 1981, 576, 312, 6252,
  8263, 337, 3195, 295, 4960, 13, 440, 22811, 472, 11, 558, 11, 2673, 382, 5763, 51564],
  "temperature": 0.0, "avg_logprob": -0.13779831840878443, "compression_ratio": 1.6297577854671281,
  "no_speech_prob": 0.0014001547824591398}, {"id": 113, "seek": 66728, "start": 691.28,
  "end": 695.6, "text": " or the most obvious one is help sales, help partners sell
  more at the knowledge companies,", "tokens": [51564, 420, 264, 881, 6322, 472, 307,
  854, 5763, 11, 854, 4462, 3607, 544, 412, 264, 3601, 3431, 11, 51780], "temperature":
  0.0, "avg_logprob": -0.13779831840878443, "compression_ratio": 1.6297577854671281,
  "no_speech_prob": 0.0014001547824591398}, {"id": 114, "seek": 69560, "start": 695.6,
  "end": 700.16, "text": " help the sales people better understand their customers
  or industries. And there''s a massive", "tokens": [50364, 854, 264, 5763, 561, 1101,
  1223, 641, 4581, 420, 13284, 13, 400, 456, 311, 257, 5994, 50592], "temperature":
  0.0, "avg_logprob": -0.09958425842889465, "compression_ratio": 1.675, "no_speech_prob":
  0.000511071237269789}, {"id": 115, "seek": 69560, "start": 700.16, "end": 707.52,
  "text": " amount of information overload. So the problems are different. They''re
  acute. They''re willing to spend", "tokens": [50592, 2372, 295, 1589, 28777, 13,
  407, 264, 2740, 366, 819, 13, 814, 434, 24390, 13, 814, 434, 4950, 281, 3496, 50960],
  "temperature": 0.0, "avg_logprob": -0.09958425842889465, "compression_ratio": 1.675,
  "no_speech_prob": 0.000511071237269789}, {"id": 116, "seek": 69560, "start": 707.52,
  "end": 712.5600000000001, "text": " significant money, right, and invest in really
  creating a better world. I think now,", "tokens": [50960, 4776, 1460, 11, 558, 11,
  293, 1963, 294, 534, 4084, 257, 1101, 1002, 13, 286, 519, 586, 11, 51212], "temperature":
  0.0, "avg_logprob": -0.09958425842889465, "compression_ratio": 1.675, "no_speech_prob":
  0.000511071237269789}, {"id": 117, "seek": 69560, "start": 714.4, "end": 718.0,
  "text": " maybe one of the most important trends is people are not so interested
  in more search boxes.", "tokens": [51304, 1310, 472, 295, 264, 881, 1021, 13892,
  307, 561, 366, 406, 370, 3102, 294, 544, 3164, 9002, 13, 51484], "temperature":
  0.0, "avg_logprob": -0.09958425842889465, "compression_ratio": 1.675, "no_speech_prob":
  0.000511071237269789}, {"id": 118, "seek": 69560, "start": 718.72, "end": 724.32,
  "text": " They want to build proactive systems that bring people the information
  that they need. And this", "tokens": [51520, 814, 528, 281, 1322, 28028, 3652, 300,
  1565, 561, 264, 1589, 300, 436, 643, 13, 400, 341, 51800], "temperature": 0.0, "avg_logprob":
  -0.09958425842889465, "compression_ratio": 1.675, "no_speech_prob": 0.000511071237269789},
  {"id": 119, "seek": 72432, "start": 724.32, "end": 728.8000000000001, "text": "
  has been a long time thing in sales with things like LinkedIn Navigator, right?
  A lot of the", "tokens": [50364, 575, 668, 257, 938, 565, 551, 294, 5763, 365, 721,
  411, 20657, 9219, 28895, 11, 558, 30, 316, 688, 295, 264, 50588], "temperature":
  0.0, "avg_logprob": -0.13354564596105506, "compression_ratio": 1.6982456140350877,
  "no_speech_prob": 0.0004095844051335007}, {"id": 120, "seek": 72432, "start": 728.8000000000001,
  "end": 733.44, "text": " public data gets harvested and brought to you. But think
  about all of that incredibly rich,", "tokens": [50588, 1908, 1412, 2170, 40994,
  293, 3038, 281, 291, 13, 583, 519, 466, 439, 295, 300, 6252, 4593, 11, 50820], "temperature":
  0.0, "avg_logprob": -0.13354564596105506, "compression_ratio": 1.6982456140350877,
  "no_speech_prob": 0.0004095844051335007}, {"id": 121, "seek": 72432, "start": 733.44,
  "end": 739.6800000000001, "text": " valuable internal data and needing to bring
  that and how hard it is to bring that to people inside", "tokens": [50820, 8263,
  6920, 1412, 293, 18006, 281, 1565, 300, 293, 577, 1152, 309, 307, 281, 1565, 300,
  281, 561, 1854, 51132], "temperature": 0.0, "avg_logprob": -0.13354564596105506,
  "compression_ratio": 1.6982456140350877, "no_speech_prob": 0.0004095844051335007},
  {"id": 122, "seek": 72432, "start": 739.6800000000001, "end": 745.44, "text": "
  the enterprise because of those entitlement lines. So federated or meta search is
  a technical", "tokens": [51132, 264, 14132, 570, 295, 729, 14789, 3054, 3876, 13,
  407, 38024, 770, 420, 19616, 3164, 307, 257, 6191, 51420], "temperature": 0.0, "avg_logprob":
  -0.13354564596105506, "compression_ratio": 1.6982456140350877, "no_speech_prob":
  0.0004095844051335007}, {"id": 123, "seek": 72432, "start": 745.44, "end": 751.6,
  "text": " approach, which says rather than an in traditional enterprise search,
  traditionally, the tool is indexing.", "tokens": [51420, 3109, 11, 597, 1619, 2831,
  813, 364, 294, 5164, 14132, 3164, 11, 19067, 11, 264, 2290, 307, 8186, 278, 13,
  51728], "temperature": 0.0, "avg_logprob": -0.13354564596105506, "compression_ratio":
  1.6982456140350877, "no_speech_prob": 0.0004095844051335007}, {"id": 124, "seek":
  75160, "start": 751.84, "end": 759.6, "text": " So you take the data from all the
  sources that you need to query, which usually,", "tokens": [50376, 407, 291, 747,
  264, 1412, 490, 439, 264, 7139, 300, 291, 643, 281, 14581, 11, 597, 2673, 11, 50764],
  "temperature": 0.0, "avg_logprob": -0.15041414896647134, "compression_ratio": 1.6470588235294117,
  "no_speech_prob": 0.0007877394673414528}, {"id": 125, "seek": 75160, "start": 760.24,
  "end": 764.96, "text": " since that''s hundreds, if not thousands, inside the large
  enterprise, usually start with a few.", "tokens": [50796, 1670, 300, 311, 6779,
  11, 498, 406, 5383, 11, 1854, 264, 2416, 14132, 11, 2673, 722, 365, 257, 1326, 13,
  51032], "temperature": 0.0, "avg_logprob": -0.15041414896647134, "compression_ratio":
  1.6470588235294117, "no_speech_prob": 0.0007877394673414528}, {"id": 126, "seek":
  75160, "start": 766.24, "end": 771.44, "text": " And you extract the data, meaning
  you pull it all out, then you have to remodel it because", "tokens": [51096, 400,
  291, 8947, 264, 1412, 11, 3620, 291, 2235, 309, 439, 484, 11, 550, 291, 362, 281,
  890, 41147, 309, 570, 51356], "temperature": 0.0, "avg_logprob": -0.15041414896647134,
  "compression_ratio": 1.6470588235294117, "no_speech_prob": 0.0007877394673414528},
  {"id": 127, "seek": 75160, "start": 772.08, "end": 775.76, "text": " you could leave
  it sort of as is, but the odds are high that won''t help with search. You need to",
  "tokens": [51388, 291, 727, 1856, 309, 1333, 295, 382, 307, 11, 457, 264, 17439,
  366, 1090, 300, 1582, 380, 854, 365, 3164, 13, 509, 643, 281, 51572], "temperature":
  0.0, "avg_logprob": -0.15041414896647134, "compression_ratio": 1.6470588235294117,
  "no_speech_prob": 0.0007877394673414528}, {"id": 128, "seek": 77576, "start": 776.48,
  "end": 783.36, "text": " make at least some of the fields, things like title and
  body line up. So you map those things over", "tokens": [50400, 652, 412, 1935, 512,
  295, 264, 7909, 11, 721, 411, 4876, 293, 1772, 1622, 493, 13, 407, 291, 4471, 729,
  721, 670, 50744], "temperature": 0.0, "avg_logprob": -0.1474829021253084, "compression_ratio":
  1.6583333333333334, "no_speech_prob": 0.0015358083182945848}, {"id": 129, "seek":
  77576, "start": 783.36, "end": 788.8, "text": " and you have to make sure that the
  set of entitlements, meaning whose author I see stuff, all of that from", "tokens":
  [50744, 293, 291, 362, 281, 652, 988, 300, 264, 992, 295, 14789, 17988, 11, 3620,
  6104, 3793, 286, 536, 1507, 11, 439, 295, 300, 490, 51016], "temperature": 0.0,
  "avg_logprob": -0.1474829021253084, "compression_ratio": 1.6583333333333334, "no_speech_prob":
  0.0015358083182945848}, {"id": 130, "seek": 77576, "start": 788.8, "end": 794.08,
  "text": " all the silos has to be aggregated and correctly rationalized and put
  together, then you index it.", "tokens": [51016, 439, 264, 48893, 575, 281, 312,
  16743, 770, 293, 8944, 15090, 1602, 293, 829, 1214, 11, 550, 291, 8186, 309, 13,
  51280], "temperature": 0.0, "avg_logprob": -0.1474829021253084, "compression_ratio":
  1.6583333333333334, "no_speech_prob": 0.0015358083182945848}, {"id": 131, "seek":
  77576, "start": 794.96, "end": 800.56, "text": " Indexing is a technical process
  like creating a structure like the back of most books or most", "tokens": [51324,
  33552, 278, 307, 257, 6191, 1399, 411, 4084, 257, 3877, 411, 264, 646, 295, 881,
  3642, 420, 881, 51604], "temperature": 0.0, "avg_logprob": -0.1474829021253084,
  "compression_ratio": 1.6583333333333334, "no_speech_prob": 0.0015358083182945848},
  {"id": 132, "seek": 80056, "start": 800.56, "end": 805.28, "text": " long books,
  a list of words with basically page numbers, but in this case, they''re slightly
  more", "tokens": [50364, 938, 3642, 11, 257, 1329, 295, 2283, 365, 1936, 3028, 3547,
  11, 457, 294, 341, 1389, 11, 436, 434, 4748, 544, 50600], "temperature": 0.0, "avg_logprob":
  -0.11037262364437705, "compression_ratio": 1.58, "no_speech_prob": 0.0005225735949352384},
  {"id": 133, "seek": 80056, "start": 805.28, "end": 809.68, "text": " complex. They
  might identify the documents in the field and the exact token that it occurs in.",
  "tokens": [50600, 3997, 13, 814, 1062, 5876, 264, 8512, 294, 264, 2519, 293, 264,
  1900, 14862, 300, 309, 11843, 294, 13, 50820], "temperature": 0.0, "avg_logprob":
  -0.11037262364437705, "compression_ratio": 1.58, "no_speech_prob": 0.0005225735949352384},
  {"id": 134, "seek": 80056, "start": 809.68, "end": 818.56, "text": " So you have
  this kind of data structure. And you just have to keep it up to date anytime anything
  changes.", "tokens": [50820, 407, 291, 362, 341, 733, 295, 1412, 3877, 13, 400,
  291, 445, 362, 281, 1066, 309, 493, 281, 4002, 13038, 1340, 2962, 13, 51264], "temperature":
  0.0, "avg_logprob": -0.11037262364437705, "compression_ratio": 1.58, "no_speech_prob":
  0.0005225735949352384}, {"id": 135, "seek": 80056, "start": 820.0799999999999, "end":
  825.76, "text": " So it''s really hard. I have been very lucky to work in search
  and fast was a phenomenal indexing", "tokens": [51340, 407, 309, 311, 534, 1152,
  13, 286, 362, 668, 588, 6356, 281, 589, 294, 3164, 293, 2370, 390, 257, 17778, 8186,
  278, 51624], "temperature": 0.0, "avg_logprob": -0.11037262364437705, "compression_ratio":
  1.58, "no_speech_prob": 0.0005225735949352384}, {"id": 136, "seek": 82576, "start":
  825.76, "end": 832.64, "text": " company and it innovated in indexing beyond the
  pale. I really incredible stuff. So fast was one", "tokens": [50364, 2237, 293,
  309, 5083, 770, 294, 8186, 278, 4399, 264, 19546, 13, 286, 534, 4651, 1507, 13,
  407, 2370, 390, 472, 50708], "temperature": 0.0, "avg_logprob": -0.195271746802876,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.00911737885326147},
  {"id": 137, "seek": 82576, "start": 832.64, "end": 838.88, "text": " of the first
  companies to do updateable indices. You could actually update it. Then a lot of
  the stuff", "tokens": [50708, 295, 264, 700, 3431, 281, 360, 5623, 712, 43840, 13,
  509, 727, 767, 5623, 309, 13, 1396, 257, 688, 295, 264, 1507, 51020], "temperature":
  0.0, "avg_logprob": -0.195271746802876, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.00911737885326147}, {"id": 138, "seek": 82576, "start": 838.88,
  "end": 845.12, "text": " that they did is advanced vector. We did it fast, but you
  know, me a tiny bit, right? Whatever the", "tokens": [51020, 300, 436, 630, 307,
  7339, 8062, 13, 492, 630, 309, 2370, 11, 457, 291, 458, 11, 385, 257, 5870, 857,
  11, 558, 30, 8541, 264, 51332], "temperature": 0.0, "avg_logprob": -0.195271746802876,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.00911737885326147},
  {"id": 139, "seek": 82576, "start": 845.12, "end": 850.0, "text": " nuggets were,
  but they went on. They went so far with engine development at fast. And now it''s
  by", "tokens": [51332, 42663, 645, 11, 457, 436, 1437, 322, 13, 814, 1437, 370,
  1400, 365, 2848, 3250, 412, 2370, 13, 400, 586, 309, 311, 538, 51576], "temperature":
  0.0, "avg_logprob": -0.195271746802876, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.00911737885326147}, {"id": 140, "seek": 82576, "start": 850.0,
  "end": 854.08, "text": " the way available through the Vespa project, right? If
  you go to Vespa.de, all that stuff is available,", "tokens": [51576, 264, 636, 2435,
  807, 264, 691, 279, 4306, 1716, 11, 558, 30, 759, 291, 352, 281, 691, 279, 4306,
  13, 1479, 11, 439, 300, 1507, 307, 2435, 11, 51780], "temperature": 0.0, "avg_logprob":
  -0.195271746802876, "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.00911737885326147},
  {"id": 141, "seek": 85408, "start": 854.08, "end": 860.64, "text": " open source
  to. Yeah, we have an episode with Vespa. You probably would joke. Yes.", "tokens":
  [50364, 1269, 4009, 281, 13, 865, 11, 321, 362, 364, 3500, 365, 691, 279, 4306,
  13, 509, 1391, 576, 7647, 13, 1079, 13, 50692], "temperature": 0.0, "avg_logprob":
  -0.23930153891304942, "compression_ratio": 1.6366906474820144, "no_speech_prob":
  0.0016994241159409285}, {"id": 142, "seek": 85408, "start": 862.32, "end": 869.2,
  "text": " He''s my hero on on Twitter. So incredible advances at fast and frankly
  at a", "tokens": [50776, 634, 311, 452, 5316, 322, 322, 5794, 13, 407, 4651, 25297,
  412, 2370, 293, 11939, 412, 257, 51120], "temperature": 0.0, "avg_logprob": -0.23930153891304942,
  "compression_ratio": 1.6366906474820144, "no_speech_prob": 0.0016994241159409285},
  {"id": 143, "seek": 85408, "start": 869.2, "end": 873.5200000000001, "text": " TVO,
  you know, there were a bunch of patents filed. Some very smart people worked on
  that problem", "tokens": [51120, 3558, 46, 11, 291, 458, 11, 456, 645, 257, 3840,
  295, 38142, 18789, 13, 2188, 588, 4069, 561, 2732, 322, 300, 1154, 51336], "temperature":
  0.0, "avg_logprob": -0.23930153891304942, "compression_ratio": 1.6366906474820144,
  "no_speech_prob": 0.0016994241159409285}, {"id": 144, "seek": 85408, "start": 873.5200000000001,
  "end": 879.0400000000001, "text": " and came up with incredible ways to interlink
  data by combining graph and and a traditional inverted", "tokens": [51336, 293,
  1361, 493, 365, 4651, 2098, 281, 728, 22473, 1412, 538, 21928, 4295, 293, 293, 257,
  5164, 38969, 51612], "temperature": 0.0, "avg_logprob": -0.23930153891304942, "compression_ratio":
  1.6366906474820144, "no_speech_prob": 0.0016994241159409285}, {"id": 145, "seek":
  85408, "start": 879.0400000000001, "end": 883.2, "text": " index and doing things
  like then adding that to machine learning and doing things like predicting", "tokens":
  [51612, 8186, 293, 884, 721, 411, 550, 5127, 300, 281, 3479, 2539, 293, 884, 721,
  411, 32884, 51820], "temperature": 0.0, "avg_logprob": -0.23930153891304942, "compression_ratio":
  1.6366906474820144, "no_speech_prob": 0.0016994241159409285}, {"id": 146, "seek":
  88320, "start": 883.44, "end": 891.36, "text": " the answer to a service ticket.
  So there''s no end of indexing. It''s just hard. That''s all.", "tokens": [50376,
  264, 1867, 281, 257, 2643, 10550, 13, 407, 456, 311, 572, 917, 295, 8186, 278, 13,
  467, 311, 445, 1152, 13, 663, 311, 439, 13, 50772], "temperature": 0.0, "avg_logprob":
  -0.1300945281982422, "compression_ratio": 1.5508474576271187, "no_speech_prob":
  0.0007845716900192201}, {"id": 147, "seek": 88320, "start": 892.0, "end": 896.08,
  "text": " It''s just hard. And especially when you want to combine silos. And so
  over the years,", "tokens": [50804, 467, 311, 445, 1152, 13, 400, 2318, 562, 291,
  528, 281, 10432, 48893, 13, 400, 370, 670, 264, 924, 11, 51008], "temperature":
  0.0, "avg_logprob": -0.1300945281982422, "compression_ratio": 1.5508474576271187,
  "no_speech_prob": 0.0007845716900192201}, {"id": 148, "seek": 88320, "start": 896.08,
  "end": 900.88, "text": " I''ve bumped into people who have had the multi silo problem
  in grade numbers. There is one", "tokens": [51008, 286, 600, 42696, 666, 561, 567,
  362, 632, 264, 4825, 3425, 78, 1154, 294, 7204, 3547, 13, 821, 307, 472, 51248],
  "temperature": 0.0, "avg_logprob": -0.1300945281982422, "compression_ratio": 1.5508474576271187,
  "no_speech_prob": 0.0007845716900192201}, {"id": 149, "seek": 88320, "start": 900.88,
  "end": 908.0, "text": " consulting company that has more than 500 silos, separate
  installations of elastic, literally from", "tokens": [51248, 23682, 2237, 300, 575,
  544, 813, 5923, 48893, 11, 4994, 41932, 295, 17115, 11, 3736, 490, 51604], "temperature":
  0.0, "avg_logprob": -0.1300945281982422, "compression_ratio": 1.5508474576271187,
  "no_speech_prob": 0.0007845716900192201}, {"id": 150, "seek": 90800, "start": 908.0,
  "end": 912.56, "text": " version two to version eight or whatever they''re on now,
  right? Because that was a standard.", "tokens": [50364, 3037, 732, 281, 3037, 3180,
  420, 2035, 436, 434, 322, 586, 11, 558, 30, 1436, 300, 390, 257, 3832, 13, 50592],
  "temperature": 0.0, "avg_logprob": -0.13735894899110537, "compression_ratio": 1.6537102473498233,
  "no_speech_prob": 0.004973128903657198}, {"id": 151, "seek": 90800, "start": 912.56,
  "end": 917.36, "text": " And when they got a JSON data set or a database or they
  bought something or they did a hackathon", "tokens": [50592, 400, 562, 436, 658,
  257, 31828, 1412, 992, 420, 257, 8149, 420, 436, 4243, 746, 420, 436, 630, 257,
  10339, 18660, 50832], "temperature": 0.0, "avg_logprob": -0.13735894899110537, "compression_ratio":
  1.6537102473498233, "no_speech_prob": 0.004973128903657198}, {"id": 152, "seek":
  90800, "start": 918.0, "end": 923.12, "text": " invariably, the documents ended
  up in some elastic with some security on it. And now", "tokens": [50864, 33270,
  1188, 11, 264, 8512, 4590, 493, 294, 512, 17115, 365, 512, 3825, 322, 309, 13, 400,
  586, 51120], "temperature": 0.0, "avg_logprob": -0.13735894899110537, "compression_ratio":
  1.6537102473498233, "no_speech_prob": 0.004973128903657198}, {"id": 153, "seek":
  90800, "start": 923.92, "end": 930.56, "text": " the some of the variation right
  in partner and case team performance is attributed internally", "tokens": [51160,
  264, 512, 295, 264, 12990, 558, 294, 4975, 293, 1389, 1469, 3389, 307, 30976, 19501,
  51492], "temperature": 0.0, "avg_logprob": -0.13735894899110537, "compression_ratio":
  1.6537102473498233, "no_speech_prob": 0.004973128903657198}, {"id": 154, "seek":
  90800, "start": 930.56, "end": 936.72, "text": " through surveys to who knows where
  to get the data. If you know, oh, I know to talk to this person,", "tokens": [51492,
  807, 22711, 281, 567, 3255, 689, 281, 483, 264, 1412, 13, 759, 291, 458, 11, 1954,
  11, 286, 458, 281, 751, 281, 341, 954, 11, 51800], "temperature": 0.0, "avg_logprob":
  -0.13735894899110537, "compression_ratio": 1.6537102473498233, "no_speech_prob":
  0.004973128903657198}, {"id": 155, "seek": 93672, "start": 937.28, "end": 942.72,
  "text": " they will have the key to unlock this particular thing that I can then
  use to say, hey, look what", "tokens": [50392, 436, 486, 362, 264, 2141, 281, 11634,
  341, 1729, 551, 300, 286, 393, 550, 764, 281, 584, 11, 4177, 11, 574, 437, 50664],
  "temperature": 0.0, "avg_logprob": -0.1374705660659655, "compression_ratio": 1.725,
  "no_speech_prob": 7.81923154136166e-05}, {"id": 156, "seek": 93672, "start": 942.72,
  "end": 946.64, "text": " we did this incredible work we did in your industry before
  or look at this incredible work we did", "tokens": [50664, 321, 630, 341, 4651,
  589, 321, 630, 294, 428, 3518, 949, 420, 574, 412, 341, 4651, 589, 321, 630, 50860],
  "temperature": 0.0, "avg_logprob": -0.1374705660659655, "compression_ratio": 1.725,
  "no_speech_prob": 7.81923154136166e-05}, {"id": 157, "seek": 93672, "start": 946.64,
  "end": 952.48, "text": " for you in the past, right? A new partner might not know
  that. They''ve done five engagements that", "tokens": [50860, 337, 291, 294, 264,
  1791, 11, 558, 30, 316, 777, 4975, 1062, 406, 458, 300, 13, 814, 600, 1096, 1732,
  44978, 300, 51152], "temperature": 0.0, "avg_logprob": -0.1374705660659655, "compression_ratio":
  1.725, "no_speech_prob": 7.81923154136166e-05}, {"id": 158, "seek": 93672, "start":
  952.48, "end": 960.32, "text": " were very similar. So it''s that kind of and I
  think the word is systematic. People want to be", "tokens": [51152, 645, 588, 2531,
  13, 407, 309, 311, 300, 733, 295, 293, 286, 519, 264, 1349, 307, 27249, 13, 3432,
  528, 281, 312, 51544], "temperature": 0.0, "avg_logprob": -0.1374705660659655, "compression_ratio":
  1.725, "no_speech_prob": 7.81923154136166e-05}, {"id": 159, "seek": 93672, "start":
  960.32, "end": 965.2, "text": " very much more systematic now because everyone is
  too busy and there''s information overload. So", "tokens": [51544, 588, 709, 544,
  27249, 586, 570, 1518, 307, 886, 5856, 293, 456, 311, 1589, 28777, 13, 407, 51788],
  "temperature": 0.0, "avg_logprob": -0.1374705660659655, "compression_ratio": 1.725,
  "no_speech_prob": 7.81923154136166e-05}, {"id": 160, "seek": 96672, "start": 967.44,
  "end": 974.88, "text": " that''s really the to break those lines down. My view is
  enterprise search now really desperately,", "tokens": [50400, 300, 311, 534, 264,
  281, 1821, 729, 3876, 760, 13, 1222, 1910, 307, 14132, 3164, 586, 534, 23726, 11,
  50772], "temperature": 0.0, "avg_logprob": -0.1684650130893873, "compression_ratio":
  1.7136563876651982, "no_speech_prob": 0.003799359081313014}, {"id": 161, "seek":
  96672, "start": 975.44, "end": 981.6800000000001, "text": " desperately critically
  requires meta search. It''s the only choice you cannot you''re downloading,", "tokens":
  [50800, 23726, 22797, 7029, 19616, 3164, 13, 467, 311, 264, 787, 3922, 291, 2644,
  291, 434, 32529, 11, 51112], "temperature": 0.0, "avg_logprob": -0.1684650130893873,
  "compression_ratio": 1.7136563876651982, "no_speech_prob": 0.003799359081313014},
  {"id": 162, "seek": 96672, "start": 982.48, "end": 987.9200000000001, "text": "
  you know, pulling out all of the data, even if you were to desire that. It''s very
  hard to do.", "tokens": [51152, 291, 458, 11, 8407, 484, 439, 295, 264, 1412, 11,
  754, 498, 291, 645, 281, 7516, 300, 13, 467, 311, 588, 1152, 281, 360, 13, 51424],
  "temperature": 0.0, "avg_logprob": -0.1684650130893873, "compression_ratio": 1.7136563876651982,
  "no_speech_prob": 0.003799359081313014}, {"id": 163, "seek": 96672, "start": 989.2,
  "end": 993.12, "text": " Now you''re because you have to basically the old way would
  be to pull all the data out of everything", "tokens": [51488, 823, 291, 434, 570,
  291, 362, 281, 1936, 264, 1331, 636, 576, 312, 281, 2235, 439, 264, 1412, 484, 295,
  1203, 51684], "temperature": 0.0, "avg_logprob": -0.1684650130893873, "compression_ratio":
  1.7136563876651982, "no_speech_prob": 0.003799359081313014}, {"id": 164, "seek":
  99312, "start": 993.12, "end": 1000.8, "text": " and sort of filter it down. Why
  not search it? Yeah, our search is to say it''s out there now.", "tokens": [50364,
  293, 1333, 295, 6608, 309, 760, 13, 1545, 406, 3164, 309, 30, 865, 11, 527, 3164,
  307, 281, 584, 309, 311, 484, 456, 586, 13, 50748], "temperature": 0.0, "avg_logprob":
  -0.166215530549637, "compression_ratio": 1.6125, "no_speech_prob": 0.002496548928320408},
  {"id": 165, "seek": 99312, "start": 1000.8, "end": 1006.16, "text": " The vendors
  are doing incredible things. I mean, service now from where it was years ago to
  where", "tokens": [50748, 440, 22056, 366, 884, 4651, 721, 13, 286, 914, 11, 2643,
  586, 490, 689, 309, 390, 924, 2057, 281, 689, 51016], "temperature": 0.0, "avg_logprob":
  -0.166215530549637, "compression_ratio": 1.6125, "no_speech_prob": 0.002496548928320408},
  {"id": 166, "seek": 99312, "start": 1006.16, "end": 1011.28, "text": " it is today.
  It''s incredible. There''s an amazing team of people working away on that and that''s",
  "tokens": [51016, 309, 307, 965, 13, 467, 311, 4651, 13, 821, 311, 364, 2243, 1469,
  295, 561, 1364, 1314, 322, 300, 293, 300, 311, 51272], "temperature": 0.0, "avg_logprob":
  -0.166215530549637, "compression_ratio": 1.6125, "no_speech_prob": 0.002496548928320408},
  {"id": 167, "seek": 99312, "start": 1011.28, "end": 1017.52, "text": " true of most
  applications now. Somebody''s working on search. It has a nice high quality API.
  So let", "tokens": [51272, 2074, 295, 881, 5821, 586, 13, 13463, 311, 1364, 322,
  3164, 13, 467, 575, 257, 1481, 1090, 3125, 9362, 13, 407, 718, 51584], "temperature":
  0.0, "avg_logprob": -0.166215530549637, "compression_ratio": 1.6125, "no_speech_prob":
  0.002496548928320408}, {"id": 168, "seek": 101752, "start": 1017.68, "end": 1023.68,
  "text": " them do their thing. Let them master it. But search and the other thing,
  the interesting that makes", "tokens": [50372, 552, 360, 641, 551, 13, 961, 552,
  4505, 309, 13, 583, 3164, 293, 264, 661, 551, 11, 264, 1880, 300, 1669, 50672],
  "temperature": 0.0, "avg_logprob": -0.13225844928196498, "compression_ratio": 1.8202247191011236,
  "no_speech_prob": 0.003028707578778267}, {"id": 169, "seek": 101752, "start": 1023.68,
  "end": 1028.08, "text": " meta search particularly powerful for the enterprise is
  you''re always searching on behalf of something.", "tokens": [50672, 19616, 3164,
  4098, 4005, 337, 264, 14132, 307, 291, 434, 1009, 10808, 322, 9490, 295, 746, 13,
  50892], "temperature": 0.0, "avg_logprob": -0.13225844928196498, "compression_ratio":
  1.8202247191011236, "no_speech_prob": 0.003028707578778267}, {"id": 170, "seek":
  101752, "start": 1028.08, "end": 1034.32, "text": " Right. And that avoids something
  that avoids it. It goes with the flow. It goes with the grain", "tokens": [50892,
  1779, 13, 400, 300, 3641, 3742, 746, 300, 3641, 3742, 309, 13, 467, 1709, 365, 264,
  3095, 13, 467, 1709, 365, 264, 12837, 51204], "temperature": 0.0, "avg_logprob":
  -0.13225844928196498, "compression_ratio": 1.8202247191011236, "no_speech_prob":
  0.003028707578778267}, {"id": 171, "seek": 101752, "start": 1035.28, "end": 1038.96,
  "text": " of the enterprise architecture. You''re supposed to query on behalf of
  something and if you do,", "tokens": [51252, 295, 264, 14132, 9482, 13, 509, 434,
  3442, 281, 14581, 322, 9490, 295, 746, 293, 498, 291, 360, 11, 51436], "temperature":
  0.0, "avg_logprob": -0.13225844928196498, "compression_ratio": 1.8202247191011236,
  "no_speech_prob": 0.003028707578778267}, {"id": 172, "seek": 101752, "start": 1038.96,
  "end": 1042.8799999999999, "text": " in theory, the app can just maintain the context.
  It only gets tricky when you start saying,", "tokens": [51436, 294, 5261, 11, 264,
  724, 393, 445, 6909, 264, 4319, 13, 467, 787, 2170, 12414, 562, 291, 722, 1566,
  11, 51632], "temperature": 0.0, "avg_logprob": -0.13225844928196498, "compression_ratio":
  1.8202247191011236, "no_speech_prob": 0.003028707578778267}, {"id": 173, "seek":
  104288, "start": 1042.88, "end": 1047.68, "text": " oh, I want to combine these
  five together. At the data level, when you do it at the user level,", "tokens":
  [50364, 1954, 11, 286, 528, 281, 10432, 613, 1732, 1214, 13, 1711, 264, 1412, 1496,
  11, 562, 291, 360, 309, 412, 264, 4195, 1496, 11, 50604], "temperature": 0.0, "avg_logprob":
  -0.1771651127541712, "compression_ratio": 1.7749077490774907, "no_speech_prob":
  0.0022522613871842623}, {"id": 174, "seek": 104288, "start": 1047.68, "end": 1051.8400000000001,
  "text": " that''s fine. Either the user was authorized to see all three or they
  weren''t or they were able", "tokens": [50604, 300, 311, 2489, 13, 13746, 264, 4195,
  390, 28312, 281, 536, 439, 1045, 420, 436, 4999, 380, 420, 436, 645, 1075, 50812],
  "temperature": 0.0, "avg_logprob": -0.1771651127541712, "compression_ratio": 1.7749077490774907,
  "no_speech_prob": 0.0022522613871842623}, {"id": 175, "seek": 104288, "start": 1051.8400000000001,
  "end": 1057.5200000000002, "text": " to see a portion of it or they weren''t. That''s
  the way things work in the enterprise. So that''s", "tokens": [50812, 281, 536,
  257, 8044, 295, 309, 420, 436, 4999, 380, 13, 663, 311, 264, 636, 721, 589, 294,
  264, 14132, 13, 407, 300, 311, 51096], "temperature": 0.0, "avg_logprob": -0.1771651127541712,
  "compression_ratio": 1.7749077490774907, "no_speech_prob": 0.0022522613871842623},
  {"id": 176, "seek": 104288, "start": 1058.8000000000002, "end": 1063.8400000000001,
  "text": " that''s the subtle difference, right? To delineate them. Yeah. And why
  the potentials there is that", "tokens": [51160, 300, 311, 264, 13743, 2649, 11,
  558, 30, 1407, 1103, 533, 473, 552, 13, 865, 13, 400, 983, 264, 3995, 82, 456, 307,
  300, 51412], "temperature": 0.0, "avg_logprob": -0.1771651127541712, "compression_ratio":
  1.7749077490774907, "no_speech_prob": 0.0022522613871842623}, {"id": 177, "seek":
  104288, "start": 1063.8400000000001, "end": 1070.16, "text": " indexing is costly.
  And yet, on the. Yeah. And you described it really eloquently in a way that", "tokens":
  [51412, 8186, 278, 307, 28328, 13, 400, 1939, 11, 322, 264, 13, 865, 13, 400, 291,
  7619, 309, 534, 38682, 47519, 294, 257, 636, 300, 51728], "temperature": 0.0, "avg_logprob":
  -0.1771651127541712, "compression_ratio": 1.7749077490774907, "no_speech_prob":
  0.0022522613871842623}, {"id": 178, "seek": 107016, "start": 1071.0400000000002,
  "end": 1078.16, "text": " to some extent by implementing meta search, you wouldn''t
  need to solve indexing issues. You", "tokens": [50408, 281, 512, 8396, 538, 18114,
  19616, 3164, 11, 291, 2759, 380, 643, 281, 5039, 8186, 278, 2663, 13, 509, 50764],
  "temperature": 0.0, "avg_logprob": -0.15108410353513108, "compression_ratio": 1.6814159292035398,
  "no_speech_prob": 0.001609696657396853}, {"id": 179, "seek": 107016, "start": 1078.16,
  "end": 1084.72, "text": " wouldn''t need to solve entitlement issues, right? You
  kind of like use the existing proxies.", "tokens": [50764, 2759, 380, 643, 281,
  5039, 14789, 3054, 2663, 11, 558, 30, 509, 733, 295, 411, 764, 264, 6741, 447, 87,
  530, 13, 51092], "temperature": 0.0, "avg_logprob": -0.15108410353513108, "compression_ratio":
  1.6814159292035398, "no_speech_prob": 0.001609696657396853}, {"id": 180, "seek":
  107016, "start": 1085.28, "end": 1093.1200000000001, "text": " But there is one
  remaining bit that I''m really curious about. So if you look at, let''s say what
  Google", "tokens": [51120, 583, 456, 307, 472, 8877, 857, 300, 286, 478, 534, 6369,
  466, 13, 407, 498, 291, 574, 412, 11, 718, 311, 584, 437, 3329, 51512], "temperature":
  0.0, "avg_logprob": -0.15108410353513108, "compression_ratio": 1.6814159292035398,
  "no_speech_prob": 0.001609696657396853}, {"id": 181, "seek": 107016, "start": 1093.1200000000001,
  "end": 1099.92, "text": " did to the web search is that they looked at what you
  could call a proxonym effect. So other", "tokens": [51512, 630, 281, 264, 3670,
  3164, 307, 300, 436, 2956, 412, 437, 291, 727, 818, 257, 447, 87, 12732, 1802, 13,
  407, 661, 51852], "temperature": 0.0, "avg_logprob": -0.15108410353513108, "compression_ratio":
  1.6814159292035398, "no_speech_prob": 0.001609696657396853}, {"id": 182, "seek":
  109992, "start": 1099.92, "end": 1106.88, "text": " people created pages linked
  to more important pages, hubs, and then you invent the algorithm,", "tokens": [50364,
  561, 2942, 7183, 9408, 281, 544, 1021, 7183, 11, 46870, 11, 293, 550, 291, 7962,
  264, 9284, 11, 50712], "temperature": 0.0, "avg_logprob": -0.18699480978290686,
  "compression_ratio": 1.6278026905829597, "no_speech_prob": 0.00293486169539392},
  {"id": 183, "seek": 109992, "start": 1107.52, "end": 1113.44, "text": " create it
  to you. But you still kind of like rely on what others did in a way, right?", "tokens":
  [50744, 1884, 309, 281, 291, 13, 583, 291, 920, 733, 295, 411, 10687, 322, 437,
  2357, 630, 294, 257, 636, 11, 558, 30, 51040], "temperature": 0.0, "avg_logprob":
  -0.18699480978290686, "compression_ratio": 1.6278026905829597, "no_speech_prob":
  0.00293486169539392}, {"id": 184, "seek": 109992, "start": 1114.3200000000002, "end":
  1119.6000000000001, "text": " And so now you have the page rank algorithm, how you
  how you rank the documents and all of a", "tokens": [51084, 400, 370, 586, 291,
  362, 264, 3028, 6181, 9284, 11, 577, 291, 577, 291, 6181, 264, 8512, 293, 439, 295,
  257, 51348], "temperature": 0.0, "avg_logprob": -0.18699480978290686, "compression_ratio":
  1.6278026905829597, "no_speech_prob": 0.00293486169539392}, {"id": 185, "seek":
  109992, "start": 1119.6000000000001, "end": 1124.5600000000002, "text": " sudden,
  this is the breakthrough and this looks a lot more relevant. In enterprise search,",
  "tokens": [51348, 3990, 11, 341, 307, 264, 22397, 293, 341, 1542, 257, 688, 544,
  7340, 13, 682, 14132, 3164, 11, 51596], "temperature": 0.0, "avg_logprob": -0.18699480978290686,
  "compression_ratio": 1.6278026905829597, "no_speech_prob": 0.00293486169539392},
  {"id": 186, "seek": 112456, "start": 1125.2, "end": 1129.84, "text": " you don''t
  necessarily have this. Okay, you do have documents that are being created, created,",
  "tokens": [50396, 291, 500, 380, 4725, 362, 341, 13, 1033, 11, 291, 360, 362, 8512,
  300, 366, 885, 2942, 11, 2942, 11, 50628], "temperature": 0.0, "avg_logprob": -0.16532469267892366,
  "compression_ratio": 1.603305785123967, "no_speech_prob": 0.04346649348735809},
  {"id": 187, "seek": 112456, "start": 1129.84, "end": 1136.0, "text": " and so forth.
  But then as you said, there is a lot of silos, right? And so things get created.",
  "tokens": [50628, 293, 370, 5220, 13, 583, 550, 382, 291, 848, 11, 456, 307, 257,
  688, 295, 48893, 11, 558, 30, 400, 370, 721, 483, 2942, 13, 50936], "temperature":
  0.0, "avg_logprob": -0.16532469267892366, "compression_ratio": 1.603305785123967,
  "no_speech_prob": 0.04346649348735809}, {"id": 188, "seek": 112456, "start": 1136.0,
  "end": 1141.36, "text": " There is no single place where you can say, what happened?
  What did I miss? What do you have on this", "tokens": [50936, 821, 307, 572, 2167,
  1081, 689, 291, 393, 584, 11, 437, 2011, 30, 708, 630, 286, 1713, 30, 708, 360,
  291, 362, 322, 341, 51204], "temperature": 0.0, "avg_logprob": -0.16532469267892366,
  "compression_ratio": 1.603305785123967, "no_speech_prob": 0.04346649348735809},
  {"id": 189, "seek": 112456, "start": 1141.36, "end": 1150.56, "text": " topic and
  so forth? Just today in the morning, I was browsing through Office 365. They have
  like a", "tokens": [51204, 4829, 293, 370, 5220, 30, 1449, 965, 294, 264, 2446,
  11, 286, 390, 38602, 807, 8935, 22046, 13, 814, 362, 411, 257, 51664], "temperature":
  0.0, "avg_logprob": -0.16532469267892366, "compression_ratio": 1.603305785123967,
  "no_speech_prob": 0.04346649348735809}, {"id": 190, "seek": 115056, "start": 1150.56,
  "end": 1157.28, "text": " single page, which shows me all the documents that either
  I interacted with or someone interacted", "tokens": [50364, 2167, 3028, 11, 597,
  3110, 385, 439, 264, 8512, 300, 2139, 286, 49621, 365, 420, 1580, 49621, 50700],
  "temperature": 0.0, "avg_logprob": -0.13872027146188837, "compression_ratio": 1.7232142857142858,
  "no_speech_prob": 0.021721016615629196}, {"id": 191, "seek": 115056, "start": 1157.28,
  "end": 1163.28, "text": " with and I am part of that group. And I can search there.
  That was helpful actually. That''s all the", "tokens": [50700, 365, 293, 286, 669,
  644, 295, 300, 1594, 13, 400, 286, 393, 3164, 456, 13, 663, 390, 4961, 767, 13,
  663, 311, 439, 264, 51000], "temperature": 0.0, "avg_logprob": -0.13872027146188837,
  "compression_ratio": 1.7232142857142858, "no_speech_prob": 0.021721016615629196},
  {"id": 192, "seek": 115056, "start": 1163.28, "end": 1171.84, "text": " lot of save
  the lot of time. But again, it doesn''t have confidence. It doesn''t have Salesforce.
  It", "tokens": [51000, 688, 295, 3155, 264, 688, 295, 565, 13, 583, 797, 11, 309,
  1177, 380, 362, 6687, 13, 467, 1177, 380, 362, 40398, 13, 467, 51428], "temperature":
  0.0, "avg_logprob": -0.13872027146188837, "compression_ratio": 1.7232142857142858,
  "no_speech_prob": 0.021721016615629196}, {"id": 193, "seek": 115056, "start": 1171.84,
  "end": 1179.28, "text": " doesn''t have a bunch of other places where it would go.
  So I guess one missing component,", "tokens": [51428, 1177, 380, 362, 257, 3840,
  295, 661, 3190, 689, 309, 576, 352, 13, 407, 286, 2041, 472, 5361, 6542, 11, 51800],
  "temperature": 0.0, "avg_logprob": -0.13872027146188837, "compression_ratio": 1.7232142857142858,
  "no_speech_prob": 0.021721016615629196}, {"id": 194, "seek": 117928, "start": 1179.28,
  "end": 1186.16, "text": " still in enterprise search was how would you rank these
  documents, right? Because you don''t have", "tokens": [50364, 920, 294, 14132, 3164,
  390, 577, 576, 291, 6181, 613, 8512, 11, 558, 30, 1436, 291, 500, 380, 362, 50708],
  "temperature": 0.0, "avg_logprob": -0.17276717341223427, "compression_ratio": 1.5330396475770924,
  "no_speech_prob": 0.0022269641049206257}, {"id": 195, "seek": 117928, "start": 1186.16,
  "end": 1192.8, "text": " a lot of signals. You simply have the documents themselves.
  And so would you say that", "tokens": [50708, 257, 688, 295, 12354, 13, 509, 2935,
  362, 264, 8512, 2969, 13, 400, 370, 576, 291, 584, 300, 51040], "temperature": 0.0,
  "avg_logprob": -0.17276717341223427, "compression_ratio": 1.5330396475770924, "no_speech_prob":
  0.0022269641049206257}, {"id": 196, "seek": 117928, "start": 1192.8, "end": 1199.12,
  "text": " vector search now opens up this horizon for us? It helps solve this problem.",
  "tokens": [51040, 8062, 3164, 586, 9870, 493, 341, 18046, 337, 505, 30, 467, 3665,
  5039, 341, 1154, 13, 51356], "temperature": 0.0, "avg_logprob": -0.17276717341223427,
  "compression_ratio": 1.5330396475770924, "no_speech_prob": 0.0022269641049206257},
  {"id": 197, "seek": 117928, "start": 1200.16, "end": 1207.84, "text": " Absolutely.
  And I think if we untangle it a little bit, it gets back to Google. In fact,", "tokens":
  [51408, 7021, 13, 400, 286, 519, 498, 321, 1701, 7846, 309, 257, 707, 857, 11, 309,
  2170, 646, 281, 3329, 13, 682, 1186, 11, 51792], "temperature": 0.0, "avg_logprob":
  -0.17276717341223427, "compression_ratio": 1.5330396475770924, "no_speech_prob":
  0.0022269641049206257}, {"id": 198, "seek": 120784, "start": 1207.84, "end": 1212.9599999999998,
  "text": " it goes right back to Google. Google had the challenge of make they had
  the biggest", "tokens": [50364, 309, 1709, 558, 646, 281, 3329, 13, 3329, 632, 264,
  3430, 295, 652, 436, 632, 264, 3880, 50620], "temperature": 0.0, "avg_logprob":
  -0.14617651542731092, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.0018704732647165656}, {"id": 199, "seek": 120784, "start": 1213.9199999999998,
  "end": 1222.32, "text": " data set in history. The web incredibly interlinked. And
  they did the absolute best job of", "tokens": [50668, 1412, 992, 294, 2503, 13,
  440, 3670, 6252, 728, 22473, 292, 13, 400, 436, 630, 264, 8236, 1151, 1691, 295,
  51088], "temperature": 0.0, "avg_logprob": -0.14617651542731092, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.0018704732647165656}, {"id": 200, "seek":
  120784, "start": 1222.32, "end": 1227.52, "text": " figuring out how to model that
  structure. You weren''t searching every web page every time you", "tokens": [51088,
  15213, 484, 577, 281, 2316, 300, 3877, 13, 509, 4999, 380, 10808, 633, 3670, 3028,
  633, 565, 291, 51348], "temperature": 0.0, "avg_logprob": -0.14617651542731092,
  "compression_ratio": 1.6923076923076923, "no_speech_prob": 0.0018704732647165656},
  {"id": 201, "seek": 120784, "start": 1227.52, "end": 1232.72, "text": " searched.
  You were searching a structure that in fact is a large language model. Right? That''s",
  "tokens": [51348, 22961, 13, 509, 645, 10808, 257, 3877, 300, 294, 1186, 307, 257,
  2416, 2856, 2316, 13, 1779, 30, 663, 311, 51608], "temperature": 0.0, "avg_logprob":
  -0.14617651542731092, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.0018704732647165656}, {"id": 202, "seek": 120784, "start": 1232.72, "end": 1237.52,
  "text": " what they built. They were the one they pioneered it. But it was the very
  first one. Or no, that''s", "tokens": [51608, 437, 436, 3094, 13, 814, 645, 264,
  472, 436, 19761, 4073, 309, 13, 583, 309, 390, 264, 588, 700, 472, 13, 1610, 572,
  11, 300, 311, 51848], "temperature": 0.0, "avg_logprob": -0.14617651542731092, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.0018704732647165656}, {"id": 203, "seek":
  123752, "start": 1237.52, "end": 1242.48, "text": " probably not true at all. Burr
  was an early one that got popular. I don''t want to make, I have no", "tokens":
  [50364, 1391, 406, 2074, 412, 439, 13, 7031, 81, 390, 364, 2440, 472, 300, 658,
  3743, 13, 286, 500, 380, 528, 281, 652, 11, 286, 362, 572, 50612], "temperature":
  0.0, "avg_logprob": -0.10617377758026122, "compression_ratio": 1.7056737588652482,
  "no_speech_prob": 0.0009625177481211722}, {"id": 204, "seek": 123752, "start": 1242.48,
  "end": 1247.28, "text": " idea. Right? What came first? But Burr was certainly the
  one that was the game changer. It was very", "tokens": [50612, 1558, 13, 1779, 30,
  708, 1361, 700, 30, 583, 7031, 81, 390, 3297, 264, 472, 300, 390, 264, 1216, 22822,
  13, 467, 390, 588, 50852], "temperature": 0.0, "avg_logprob": -0.10617377758026122,
  "compression_ratio": 1.7056737588652482, "no_speech_prob": 0.0009625177481211722},
  {"id": 205, "seek": 123752, "start": 1247.28, "end": 1254.56, "text": " recognized.
  That''s where the real popularization of transformer models I think came from. And
  it''s", "tokens": [50852, 9823, 13, 663, 311, 689, 264, 957, 3743, 2144, 295, 31782,
  5245, 286, 519, 1361, 490, 13, 400, 309, 311, 51216], "temperature": 0.0, "avg_logprob":
  -0.10617377758026122, "compression_ratio": 1.7056737588652482, "no_speech_prob":
  0.0009625177481211722}, {"id": 206, "seek": 123752, "start": 1254.56, "end": 1259.68,
  "text": " that structure. What is that structure? It''s a structure that can evaluate
  results almost", "tokens": [51216, 300, 3877, 13, 708, 307, 300, 3877, 30, 467,
  311, 257, 3877, 300, 393, 13059, 3542, 1920, 51472], "temperature": 0.0, "avg_logprob":
  -0.10617377758026122, "compression_ratio": 1.7056737588652482, "no_speech_prob":
  0.0009625177481211722}, {"id": 207, "seek": 123752, "start": 1259.68, "end": 1267.04,
  "text": " independent of the results themselves. You don''t have to look at every
  web page. And so that''s", "tokens": [51472, 6695, 295, 264, 3542, 2969, 13, 509,
  500, 380, 362, 281, 574, 412, 633, 3670, 3028, 13, 400, 370, 300, 311, 51840], "temperature":
  0.0, "avg_logprob": -0.10617377758026122, "compression_ratio": 1.7056737588652482,
  "no_speech_prob": 0.0009625177481211722}, {"id": 208, "seek": 126704, "start": 1267.04,
  "end": 1271.68, "text": " the key. In fact, you''re absolutely right. I think there
  have been many attempts to do meta", "tokens": [50364, 264, 2141, 13, 682, 1186,
  11, 291, 434, 3122, 558, 13, 286, 519, 456, 362, 668, 867, 15257, 281, 360, 19616,
  50596], "temperature": 0.0, "avg_logprob": -0.13549367119284236, "compression_ratio":
  1.6464285714285714, "no_speech_prob": 0.003937163390219212}, {"id": 209, "seek":
  126704, "start": 1271.68, "end": 1276.1599999999999, "text": " search and federated
  search even against APIs. But you then end up with just all the results.", "tokens":
  [50596, 3164, 293, 38024, 770, 3164, 754, 1970, 21445, 13, 583, 291, 550, 917, 493,
  365, 445, 439, 264, 3542, 13, 50820], "temperature": 0.0, "avg_logprob": -0.13549367119284236,
  "compression_ratio": 1.6464285714285714, "no_speech_prob": 0.003937163390219212},
  {"id": 210, "seek": 126704, "start": 1277.04, "end": 1280.24, "text": " Tiled or
  whatever it is, but it''s just all the results. And that doesn''t help with", "tokens":
  [50864, 314, 7292, 420, 2035, 309, 307, 11, 457, 309, 311, 445, 439, 264, 3542,
  13, 400, 300, 1177, 380, 854, 365, 51024], "temperature": 0.0, "avg_logprob": -0.13549367119284236,
  "compression_ratio": 1.6464285714285714, "no_speech_prob": 0.003937163390219212},
  {"id": 211, "seek": 126704, "start": 1280.24, "end": 1285.92, "text": " information
  overload. It also doesn''t really get to the potential. So the key is, and what''s",
  "tokens": [51024, 1589, 28777, 13, 467, 611, 1177, 380, 534, 483, 281, 264, 3995,
  13, 407, 264, 2141, 307, 11, 293, 437, 311, 51308], "temperature": 0.0, "avg_logprob":
  -0.13549367119284236, "compression_ratio": 1.6464285714285714, "no_speech_prob":
  0.003937163390219212}, {"id": 212, "seek": 126704, "start": 1285.92, "end": 1292.56,
  "text": " world uses, we use a large language model. There''s more to it, right?
  There''s a relevancy algorithm", "tokens": [51308, 1002, 4960, 11, 321, 764, 257,
  2416, 2856, 2316, 13, 821, 311, 544, 281, 309, 11, 558, 30, 821, 311, 257, 25916,
  6717, 9284, 51640], "temperature": 0.0, "avg_logprob": -0.13549367119284236, "compression_ratio":
  1.6464285714285714, "no_speech_prob": 0.003937163390219212}, {"id": 213, "seek":
  129256, "start": 1292.56, "end": 1296.3999999999999, "text": " around it. There''s
  a similarity pipeline around it, right? But at the end of the day,", "tokens": [50364,
  926, 309, 13, 821, 311, 257, 32194, 15517, 926, 309, 11, 558, 30, 583, 412, 264,
  917, 295, 264, 786, 11, 50556], "temperature": 0.0, "avg_logprob": -0.10684136421449723,
  "compression_ratio": 1.5822784810126582, "no_speech_prob": 0.0030361844692379236},
  {"id": 214, "seek": 129256, "start": 1297.04, "end": 1303.76, "text": " there''s
  a large model that evaluates data as vectors with real numbers. And it allows you
  to do", "tokens": [50588, 456, 311, 257, 2416, 2316, 300, 6133, 1024, 1412, 382,
  18875, 365, 957, 3547, 13, 400, 309, 4045, 291, 281, 360, 50924], "temperature":
  0.0, "avg_logprob": -0.10684136421449723, "compression_ratio": 1.5822784810126582,
  "no_speech_prob": 0.0030361844692379236}, {"id": 215, "seek": 129256, "start": 1303.76,
  "end": 1310.48, "text": " incredible comparisons. And the thing that, as I put this
  together, I wrote it nights and weekends", "tokens": [50924, 4651, 33157, 13, 400,
  264, 551, 300, 11, 382, 286, 829, 341, 1214, 11, 286, 4114, 309, 13249, 293, 23595,
  51260], "temperature": 0.0, "avg_logprob": -0.10684136421449723, "compression_ratio":
  1.5822784810126582, "no_speech_prob": 0.0030361844692379236}, {"id": 216, "seek":
  129256, "start": 1311.76, "end": 1318.72, "text": " starting last year. And when
  I started to get results from it, I was shocked because I did not", "tokens": [51324,
  2891, 1036, 1064, 13, 400, 562, 286, 1409, 281, 483, 3542, 490, 309, 11, 286, 390,
  12763, 570, 286, 630, 406, 51672], "temperature": 0.0, "avg_logprob": -0.10684136421449723,
  "compression_ratio": 1.5822784810126582, "no_speech_prob": 0.0030361844692379236},
  {"id": 217, "seek": 131872, "start": 1318.72, "end": 1326.4, "text": " expect it
  to go to be as good as it came out. The thing about relevancy, right? It''s, oh,
  man,", "tokens": [50364, 2066, 309, 281, 352, 281, 312, 382, 665, 382, 309, 1361,
  484, 13, 440, 551, 466, 25916, 6717, 11, 558, 30, 467, 311, 11, 1954, 11, 587, 11,
  50748], "temperature": 0.0, "avg_logprob": -0.14171066904455665, "compression_ratio":
  1.6605839416058394, "no_speech_prob": 0.003876862581819296}, {"id": 218, "seek":
  131872, "start": 1326.4, "end": 1331.2, "text": " we can always say we can, we''ll
  identify it when we see it. But building tests around it", "tokens": [50748, 321,
  393, 1009, 584, 321, 393, 11, 321, 603, 5876, 309, 562, 321, 536, 309, 13, 583,
  2390, 6921, 926, 309, 50988], "temperature": 0.0, "avg_logprob": -0.14171066904455665,
  "compression_ratio": 1.6605839416058394, "no_speech_prob": 0.003876862581819296},
  {"id": 219, "seek": 131872, "start": 1331.2, "end": 1336.88, "text": " is very difficult.
  You come out with gold standards. And I love all the tooling. There''s so much",
  "tokens": [50988, 307, 588, 2252, 13, 509, 808, 484, 365, 3821, 7787, 13, 400, 286,
  959, 439, 264, 46593, 13, 821, 311, 370, 709, 51272], "temperature": 0.0, "avg_logprob":
  -0.14171066904455665, "compression_ratio": 1.6605839416058394, "no_speech_prob":
  0.003876862581819296}, {"id": 220, "seek": 131872, "start": 1336.88, "end": 1340.64,
  "text": " good tooling around it. But at the end of the day, it all depends, fundamentally,
  on really", "tokens": [51272, 665, 46593, 926, 309, 13, 583, 412, 264, 917, 295,
  264, 786, 11, 309, 439, 5946, 11, 17879, 11, 322, 534, 51460], "temperature": 0.0,
  "avg_logprob": -0.14171066904455665, "compression_ratio": 1.6605839416058394, "no_speech_prob":
  0.003876862581819296}, {"id": 221, "seek": 131872, "start": 1341.3600000000001,
  "end": 1347.28, "text": " some set of finite labeled outcomes, right? That''s what
  it is. I found another way", "tokens": [51496, 512, 992, 295, 19362, 21335, 10070,
  11, 558, 30, 663, 311, 437, 309, 307, 13, 286, 1352, 1071, 636, 51792], "temperature":
  0.0, "avg_logprob": -0.14171066904455665, "compression_ratio": 1.6605839416058394,
  "no_speech_prob": 0.003876862581819296}, {"id": 222, "seek": 134728, "start": 1347.44,
  "end": 1354.0, "text": " to measure the relevancy without doing that. And the way
  to do that is how far to the right", "tokens": [50372, 281, 3481, 264, 25916, 6717,
  1553, 884, 300, 13, 400, 264, 636, 281, 360, 300, 307, 577, 1400, 281, 264, 558,
  50700], "temperature": 0.0, "avg_logprob": -0.19455844099803637, "compression_ratio":
  1.7393364928909953, "no_speech_prob": 0.0018015250097960234}, {"id": 223, "seek":
  134728, "start": 1354.56, "end": 1362.08, "text": " are the term hits. And in, when
  you''re using swirl, it favors because of the large language,", "tokens": [50728,
  366, 264, 1433, 8664, 13, 400, 294, 11, 562, 291, 434, 1228, 30310, 11, 309, 40554,
  570, 295, 264, 2416, 2856, 11, 51104], "temperature": 0.0, "avg_logprob": -0.19455844099803637,
  "compression_ratio": 1.7393364928909953, "no_speech_prob": 0.0018015250097960234},
  {"id": 224, "seek": 134728, "start": 1362.08, "end": 1370.6399999999999, "text":
  " the mall we used, it favors hits that are to the left, beginning of the sentence.
  It views", "tokens": [51104, 264, 16026, 321, 1143, 11, 309, 40554, 8664, 300, 366,
  281, 264, 1411, 11, 2863, 295, 264, 8174, 13, 467, 6809, 51532], "temperature":
  0.0, "avg_logprob": -0.19455844099803637, "compression_ratio": 1.7393364928909953,
  "no_speech_prob": 0.0018015250097960234}, {"id": 225, "seek": 134728, "start": 1370.6399999999999,
  "end": 1375.76, "text": " aboutness as being at the beginning of the sentence. It''s
  extremely good at discriminating,", "tokens": [51532, 466, 1287, 382, 885, 412,
  264, 2863, 295, 264, 8174, 13, 467, 311, 4664, 665, 412, 20828, 990, 11, 51788],
  "temperature": 0.0, "avg_logprob": -0.19455844099803637, "compression_ratio": 1.7393364928909953,
  "no_speech_prob": 0.0018015250097960234}, {"id": 226, "seek": 137576, "start": 1375.76,
  "end": 1383.52, "text": " again, identifying hits that are in passing. So I think
  we can all agree. Relovancy, I''ve always", "tokens": [50364, 797, 11, 16696, 8664,
  300, 366, 294, 8437, 13, 407, 286, 519, 321, 393, 439, 3986, 13, 8738, 5179, 6717,
  11, 286, 600, 1009, 50752], "temperature": 0.0, "avg_logprob": -0.24532432556152345,
  "compression_ratio": 1.6485355648535565, "no_speech_prob": 0.0020069556776434183},
  {"id": 227, "seek": 137576, "start": 1383.52, "end": 1389.2, "text": " viewed relevancy
  as a bit of a stepped function. The absolute top is exactly what I searched for",
  "tokens": [50752, 19174, 25916, 6717, 382, 257, 857, 295, 257, 15251, 2445, 13,
  440, 8236, 1192, 307, 2293, 437, 286, 22961, 337, 51036], "temperature": 0.0, "avg_logprob":
  -0.24532432556152345, "compression_ratio": 1.6485355648535565, "no_speech_prob":
  0.0020069556776434183}, {"id": 228, "seek": 137576, "start": 1389.52, "end": 1393.6,
  "text": " in the entire field of the title and the body, right? At the end of the,
  the hits at the beginning", "tokens": [51052, 294, 264, 2302, 2519, 295, 264, 4876,
  293, 264, 1772, 11, 558, 30, 1711, 264, 917, 295, 264, 11, 264, 8664, 412, 264,
  2863, 51256], "temperature": 0.0, "avg_logprob": -0.24532432556152345, "compression_ratio":
  1.6485355648535565, "no_speech_prob": 0.0020069556776434183}, {"id": 229, "seek":
  137576, "start": 1393.6, "end": 1398.24, "text": " of the body, we can probably
  agree that''s got to be a good hit, the degree there''s a title in a body.", "tokens":
  [51256, 295, 264, 1772, 11, 321, 393, 1391, 3986, 300, 311, 658, 281, 312, 257,
  665, 2045, 11, 264, 4314, 456, 311, 257, 4876, 294, 257, 1772, 13, 51488], "temperature":
  0.0, "avg_logprob": -0.24532432556152345, "compression_ratio": 1.6485355648535565,
  "no_speech_prob": 0.0020069556776434183}, {"id": 230, "seek": 139824, "start": 1398.48,
  "end": 1407.2, "text": " And then we all fear the terrible mention, right? The enemy
  of relevancy is one mention of New", "tokens": [50376, 400, 550, 321, 439, 4240,
  264, 6237, 2152, 11, 558, 30, 440, 5945, 295, 25916, 6717, 307, 472, 2152, 295,
  1873, 50812], "temperature": 0.0, "avg_logprob": -0.13642728446733834, "compression_ratio":
  1.7356828193832599, "no_speech_prob": 0.008744871243834496}, {"id": 231, "seek":
  139824, "start": 1407.2, "end": 1411.6, "text": " York at the very end, right? It''s
  like they''re in the list of cities that absolutely have nothing to do", "tokens":
  [50812, 3609, 412, 264, 588, 917, 11, 558, 30, 467, 311, 411, 436, 434, 294, 264,
  1329, 295, 6486, 300, 3122, 362, 1825, 281, 360, 51032], "temperature": 0.0, "avg_logprob":
  -0.13642728446733834, "compression_ratio": 1.7356828193832599, "no_speech_prob":
  0.008744871243834496}, {"id": 232, "seek": 139824, "start": 1411.6, "end": 1418.48,
  "text": " with the big apple. And that''s what I found is that the relevancy function,
  the lower you are in", "tokens": [51032, 365, 264, 955, 10606, 13, 400, 300, 311,
  437, 286, 1352, 307, 300, 264, 25916, 6717, 2445, 11, 264, 3126, 291, 366, 294,
  51376], "temperature": 0.0, "avg_logprob": -0.13642728446733834, "compression_ratio":
  1.7356828193832599, "no_speech_prob": 0.008744871243834496}, {"id": 233, "seek":
  139824, "start": 1418.48, "end": 1423.52, "text": " the result list, the more to
  the right your search terms are. And the relevancy is what, the other", "tokens":
  [51376, 264, 1874, 1329, 11, 264, 544, 281, 264, 558, 428, 3164, 2115, 366, 13,
  400, 264, 25916, 6717, 307, 437, 11, 264, 661, 51628], "temperature": 0.0, "avg_logprob":
  -0.13642728446733834, "compression_ratio": 1.7356828193832599, "no_speech_prob":
  0.008744871243834496}, {"id": 234, "seek": 142352, "start": 1423.52, "end": 1428.48,
  "text": " thing about meta searches is you don''t have the documents. I believe
  that an evidence-based approach", "tokens": [50364, 551, 466, 19616, 26701, 307,
  291, 500, 380, 362, 264, 8512, 13, 286, 1697, 300, 364, 4467, 12, 6032, 3109, 50612],
  "temperature": 0.0, "avg_logprob": -0.17577994497198807, "compression_ratio": 1.625531914893617,
  "no_speech_prob": 0.0018853303045034409}, {"id": 235, "seek": 142352, "start": 1428.48,
  "end": 1437.28, "text": " is critical. Did the silo return the search terms that
  you, the user put in, are they visible in", "tokens": [50612, 307, 4924, 13, 2589,
  264, 3425, 78, 2736, 264, 3164, 2115, 300, 291, 11, 264, 4195, 829, 294, 11, 366,
  436, 8974, 294, 51052], "temperature": 0.0, "avg_logprob": -0.17577994497198807,
  "compression_ratio": 1.625531914893617, "no_speech_prob": 0.0018853303045034409},
  {"id": 236, "seek": 142352, "start": 1437.28, "end": 1442.0, "text": " the results?
  If they''re not visible, then there''s a question. So that''s the other piece of
  it is we do", "tokens": [51052, 264, 3542, 30, 759, 436, 434, 406, 8974, 11, 550,
  456, 311, 257, 1168, 13, 407, 300, 311, 264, 661, 2522, 295, 309, 307, 321, 360,
  51288], "temperature": 0.0, "avg_logprob": -0.17577994497198807, "compression_ratio":
  1.625531914893617, "no_speech_prob": 0.0018853303045034409}, {"id": 237, "seek":
  142352, "start": 1442.0, "end": 1448.24, "text": " use an evident space metric combined
  with similarity to say to rank and it works.", "tokens": [51288, 764, 364, 16371,
  1901, 20678, 9354, 365, 32194, 281, 584, 281, 6181, 293, 309, 1985, 13, 51600],
  "temperature": 0.0, "avg_logprob": -0.17577994497198807, "compression_ratio": 1.625531914893617,
  "no_speech_prob": 0.0018853303045034409}, {"id": 238, "seek": 144824, "start": 1449.2,
  "end": 1456.4, "text": " And now, so that said, here''s all the stuff that I just
  left out. You have to normalize the query,", "tokens": [50412, 400, 586, 11, 370,
  300, 848, 11, 510, 311, 439, 264, 1507, 300, 286, 445, 1411, 484, 13, 509, 362,
  281, 2710, 1125, 264, 14581, 11, 50772], "temperature": 0.0, "avg_logprob": -0.1387463088082795,
  "compression_ratio": 1.6334661354581674, "no_speech_prob": 0.012598407454788685},
  {"id": 239, "seek": 144824, "start": 1457.36, "end": 1461.36, "text": " especially
  if you interpret the query and rewrite it. One of the most important things about
  meta searches", "tokens": [50820, 2318, 498, 291, 7302, 264, 14581, 293, 28132,
  309, 13, 1485, 295, 264, 881, 1021, 721, 466, 19616, 26701, 51020], "temperature":
  0.0, "avg_logprob": -0.1387463088082795, "compression_ratio": 1.6334661354581674,
  "no_speech_prob": 0.012598407454788685}, {"id": 240, "seek": 144824, "start": 1461.36,
  "end": 1468.8, "text": " you can''t send the same query to every endpoint. Not all
  endpoints are equal. Some endpoints, for example,", "tokens": [51020, 291, 393,
  380, 2845, 264, 912, 14581, 281, 633, 35795, 13, 1726, 439, 917, 20552, 366, 2681,
  13, 2188, 917, 20552, 11, 337, 1365, 11, 51392], "temperature": 0.0, "avg_logprob":
  -0.1387463088082795, "compression_ratio": 1.6334661354581674, "no_speech_prob":
  0.012598407454788685}, {"id": 241, "seek": 144824, "start": 1468.8, "end": 1474.24,
  "text": " might be a database that''s really able to target one field at a time
  effectively. So for example,", "tokens": [51392, 1062, 312, 257, 8149, 300, 311,
  534, 1075, 281, 3779, 472, 2519, 412, 257, 565, 8659, 13, 407, 337, 1365, 11, 51664],
  "temperature": 0.0, "avg_logprob": -0.1387463088082795, "compression_ratio": 1.6334661354581674,
  "no_speech_prob": 0.012598407454788685}, {"id": 242, "seek": 147424, "start": 1474.24,
  "end": 1479.36, "text": " they might be a repository that knows about companies.
  So if your search is electric vehicle Tesla,", "tokens": [50364, 436, 1062, 312,
  257, 25841, 300, 3255, 466, 3431, 13, 407, 498, 428, 3164, 307, 5210, 5864, 13666,
  11, 50620], "temperature": 0.0, "avg_logprob": -0.16039108211158687, "compression_ratio":
  1.857677902621723, "no_speech_prob": 0.0033554621040821075}, {"id": 243, "seek":
  147424, "start": 1479.36, "end": 1484.24, "text": " don''t send electric vehicle
  in, just send Tesla. So we provide a way to mark that. So we''re all", "tokens":
  [50620, 500, 380, 2845, 5210, 5864, 294, 11, 445, 2845, 13666, 13, 407, 321, 2893,
  257, 636, 281, 1491, 300, 13, 407, 321, 434, 439, 50864], "temperature": 0.0, "avg_logprob":
  -0.16039108211158687, "compression_ratio": 1.857677902621723, "no_speech_prob":
  0.0033554621040821075}, {"id": 244, "seek": 147424, "start": 1484.24, "end": 1489.2,
  "text": " has the ability to tag each search provider with what it knows about.
  So you''d write that electric", "tokens": [50864, 575, 264, 3485, 281, 6162, 1184,
  3164, 12398, 365, 437, 309, 3255, 466, 13, 407, 291, 1116, 2464, 300, 5210, 51112],
  "temperature": 0.0, "avg_logprob": -0.16039108211158687, "compression_ratio": 1.857677902621723,
  "no_speech_prob": 0.0033554621040821075}, {"id": 245, "seek": 147424, "start": 1489.2,
  "end": 1497.84, "text": " vehicle company colon Tesla. Tesla goes just to the company
  silos, the query. Everybody else drops the", "tokens": [51112, 5864, 2237, 8255,
  13666, 13, 13666, 1709, 445, 281, 264, 2237, 48893, 11, 264, 14581, 13, 7646, 1646,
  11438, 264, 51544], "temperature": 0.0, "avg_logprob": -0.16039108211158687, "compression_ratio":
  1.857677902621723, "no_speech_prob": 0.0033554621040821075}, {"id": 246, "seek":
  147424, "start": 1497.84, "end": 1502.16, "text": " tag. So Google gets electric
  vehicle Tesla, which of course, it doesn''t have a magnificent job on.", "tokens":
  [51544, 6162, 13, 407, 3329, 2170, 5210, 5864, 13666, 11, 597, 295, 1164, 11, 309,
  1177, 380, 362, 257, 23690, 1691, 322, 13, 51760], "temperature": 0.0, "avg_logprob":
  -0.16039108211158687, "compression_ratio": 1.857677902621723, "no_speech_prob":
  0.0033554621040821075}, {"id": 247, "seek": 150216, "start": 1502.16, "end": 1506.88,
  "text": " So then you have to normalize the query when you''re scoring, as well
  as you have to normalize each", "tokens": [50364, 407, 550, 291, 362, 281, 2710,
  1125, 264, 14581, 562, 291, 434, 22358, 11, 382, 731, 382, 291, 362, 281, 2710,
  1125, 1184, 50600], "temperature": 0.0, "avg_logprob": -0.12436229926495512, "compression_ratio":
  1.7167235494880546, "no_speech_prob": 0.0015101874014362693}, {"id": 248, "seek":
  150216, "start": 1506.88, "end": 1513.2, "text": " field, right, as normal. Freshness
  is certainly an interesting thing. I found the model also works best if", "tokens":
  [50600, 2519, 11, 558, 11, 382, 2710, 13, 22843, 1287, 307, 3297, 364, 1880, 551,
  13, 286, 1352, 264, 2316, 611, 1985, 1151, 498, 50916], "temperature": 0.0, "avg_logprob":
  -0.12436229926495512, "compression_ratio": 1.7167235494880546, "no_speech_prob":
  0.0015101874014362693}, {"id": 249, "seek": 150216, "start": 1513.2, "end": 1520.0800000000002,
  "text": " we add a boost based on the top topness of the results. So if a repository
  gave it rank number one,", "tokens": [50916, 321, 909, 257, 9194, 2361, 322, 264,
  1192, 1192, 1287, 295, 264, 3542, 13, 407, 498, 257, 25841, 2729, 309, 6181, 1230,
  472, 11, 51260], "temperature": 0.0, "avg_logprob": -0.12436229926495512, "compression_ratio":
  1.7167235494880546, "no_speech_prob": 0.0015101874014362693}, {"id": 250, "seek":
  150216, "start": 1520.0800000000002, "end": 1524.88, "text": " we should probably
  at least factor that in a little bit. And then of course, there''s things like",
  "tokens": [51260, 321, 820, 1391, 412, 1935, 5952, 300, 294, 257, 707, 857, 13,
  400, 550, 295, 1164, 11, 456, 311, 721, 411, 51500], "temperature": 0.0, "avg_logprob":
  -0.12436229926495512, "compression_ratio": 1.7167235494880546, "no_speech_prob":
  0.0015101874014362693}, {"id": 251, "seek": 150216, "start": 1524.88, "end": 1530.48,
  "text": " number of hits. And vector similarity is ultimately used, right? We aggregate
  vector similarities to", "tokens": [51500, 1230, 295, 8664, 13, 400, 8062, 32194,
  307, 6284, 1143, 11, 558, 30, 492, 26118, 8062, 24197, 281, 51780], "temperature":
  0.0, "avg_logprob": -0.12436229926495512, "compression_ratio": 1.7167235494880546,
  "no_speech_prob": 0.0015101874014362693}, {"id": 252, "seek": 153048, "start": 1530.48,
  "end": 1536.48, "text": " reflect the evidence level. And then the strength of it,
  right, is captured in the similarity. So a lot", "tokens": [50364, 5031, 264, 4467,
  1496, 13, 400, 550, 264, 3800, 295, 309, 11, 558, 11, 307, 11828, 294, 264, 32194,
  13, 407, 257, 688, 50664], "temperature": 0.0, "avg_logprob": -0.11056848091654259,
  "compression_ratio": 1.610655737704918, "no_speech_prob": 0.002110518282279372},
  {"id": 253, "seek": 153048, "start": 1536.48, "end": 1543.44, "text": " went into
  it. It''s probably the most awful module in our in our repo, but somebody smarter
  will", "tokens": [50664, 1437, 666, 309, 13, 467, 311, 1391, 264, 881, 11232, 10088,
  294, 527, 294, 527, 49040, 11, 457, 2618, 20294, 486, 51012], "temperature": 0.0,
  "avg_logprob": -0.11056848091654259, "compression_ratio": 1.610655737704918, "no_speech_prob":
  0.002110518282279372}, {"id": 254, "seek": 153048, "start": 1543.44, "end": 1549.04,
  "text": " rewrite it soon, but it works. And that''s the important thing. And that
  is why I''m here today,", "tokens": [51012, 28132, 309, 2321, 11, 457, 309, 1985,
  13, 400, 300, 311, 264, 1021, 551, 13, 400, 300, 307, 983, 286, 478, 510, 965, 11,
  51292], "temperature": 0.0, "avg_logprob": -0.11056848091654259, "compression_ratio":
  1.610655737704918, "no_speech_prob": 0.002110518282279372}, {"id": 255, "seek":
  153048, "start": 1549.84, "end": 1555.6, "text": " right? I have exited other ventures
  because I believe in this so much. And I put together a little", "tokens": [51332,
  558, 30, 286, 362, 454, 1226, 661, 6931, 1303, 570, 286, 1697, 294, 341, 370, 709,
  13, 400, 286, 829, 1214, 257, 707, 51620], "temperature": 0.0, "avg_logprob": -0.11056848091654259,
  "compression_ratio": 1.610655737704918, "no_speech_prob": 0.002110518282279372},
  {"id": 256, "seek": 155560, "start": 1556.56, "end": 1561.76, "text": " company
  that is here to support it. It''s 100% open source under Apache 2.0. Get it or grab
  the", "tokens": [50412, 2237, 300, 307, 510, 281, 1406, 309, 13, 467, 311, 2319,
  4, 1269, 4009, 833, 46597, 568, 13, 15, 13, 3240, 309, 420, 4444, 264, 50672], "temperature":
  0.0, "avg_logprob": -0.1441481304168701, "compression_ratio": 1.5261044176706828,
  "no_speech_prob": 0.056096650660037994}, {"id": 257, "seek": 155560, "start": 1561.76,
  "end": 1569.04, "text": " darker and you can make it run in two lines. And you''ll
  see. Yeah, that sounds so fantastic. And I''m", "tokens": [50672, 12741, 293, 291,
  393, 652, 309, 1190, 294, 732, 3876, 13, 400, 291, 603, 536, 13, 865, 11, 300, 3263,
  370, 5456, 13, 400, 286, 478, 51036], "temperature": 0.0, "avg_logprob": -0.1441481304168701,
  "compression_ratio": 1.5261044176706828, "no_speech_prob": 0.056096650660037994},
  {"id": 258, "seek": 155560, "start": 1569.04, "end": 1574.8799999999999, "text":
  " sure our listeners will take a look, especially because it''s open source. It''s
  much easier to", "tokens": [51036, 988, 527, 23274, 486, 747, 257, 574, 11, 2318,
  570, 309, 311, 1269, 4009, 13, 467, 311, 709, 3571, 281, 51328], "temperature":
  0.0, "avg_logprob": -0.1441481304168701, "compression_ratio": 1.5261044176706828,
  "no_speech_prob": 0.056096650660037994}, {"id": 259, "seek": 155560, "start": 1575.6,
  "end": 1583.4399999999998, "text": " you know, start hacking over the weekend or
  something. I also wanted to ask you before you", "tokens": [51364, 291, 458, 11,
  722, 31422, 670, 264, 6711, 420, 746, 13, 286, 611, 1415, 281, 1029, 291, 949, 291,
  51756], "temperature": 0.0, "avg_logprob": -0.1441481304168701, "compression_ratio":
  1.5261044176706828, "no_speech_prob": 0.056096650660037994}, {"id": 260, "seek":
  158344, "start": 1583.92, "end": 1588.96, "text": " show us some demos. I think
  this will be really, really interesting and change in format of the", "tokens":
  [50388, 855, 505, 512, 33788, 13, 286, 519, 341, 486, 312, 534, 11, 534, 1880, 293,
  1319, 294, 7877, 295, 264, 50640], "temperature": 0.0, "avg_logprob": -0.15100580646145728,
  "compression_ratio": 1.6398305084745763, "no_speech_prob": 0.003923231270164251},
  {"id": 261, "seek": 158344, "start": 1588.96, "end": 1598.96, "text": " podcast
  to some extent. You mentioned the similarity aspect of vector search, right? And
  so probably", "tokens": [50640, 7367, 281, 512, 8396, 13, 509, 2835, 264, 32194,
  4171, 295, 8062, 3164, 11, 558, 30, 400, 370, 1391, 51140], "temperature": 0.0,
  "avg_logprob": -0.15100580646145728, "compression_ratio": 1.6398305084745763, "no_speech_prob":
  0.003923231270164251}, {"id": 262, "seek": 158344, "start": 1598.96, "end": 1604.88,
  "text": " it also exists in keyword search to some extent, but there, as you said,
  we trained ourselves to", "tokens": [51140, 309, 611, 8198, 294, 20428, 3164, 281,
  512, 8396, 11, 457, 456, 11, 382, 291, 848, 11, 321, 8895, 4175, 281, 51436], "temperature":
  0.0, "avg_logprob": -0.15100580646145728, "compression_ratio": 1.6398305084745763,
  "no_speech_prob": 0.003923231270164251}, {"id": 263, "seek": 158344, "start": 1604.88,
  "end": 1610.88, "text": " look at what we see. And if we see how a keyword, we kind
  of trusted this more. Although this", "tokens": [51436, 574, 412, 437, 321, 536,
  13, 400, 498, 321, 536, 577, 257, 20428, 11, 321, 733, 295, 16034, 341, 544, 13,
  5780, 341, 51736], "temperature": 0.0, "avg_logprob": -0.15100580646145728, "compression_ratio":
  1.6398305084745763, "no_speech_prob": 0.003923231270164251}, {"id": 264, "seek":
  161088, "start": 1610.88, "end": 1617.44, "text": " probably varies per case, but
  in similarity search and vector search, this similarity is a", "tokens": [50364,
  1391, 21716, 680, 1389, 11, 457, 294, 32194, 3164, 293, 8062, 3164, 11, 341, 32194,
  307, 257, 50692], "temperature": 0.0, "avg_logprob": -0.13356580016433553, "compression_ratio":
  1.759433962264151, "no_speech_prob": 0.006972862407565117}, {"id": 265, "seek":
  161088, "start": 1617.44, "end": 1623.92, "text": " play, right? So like, if you
  cannot find a top result, or even like a middle relevant result,", "tokens": [50692,
  862, 11, 558, 30, 407, 411, 11, 498, 291, 2644, 915, 257, 1192, 1874, 11, 420, 754,
  411, 257, 2808, 7340, 1874, 11, 51016], "temperature": 0.0, "avg_logprob": -0.13356580016433553,
  "compression_ratio": 1.759433962264151, "no_speech_prob": 0.006972862407565117},
  {"id": 266, "seek": 161088, "start": 1623.92, "end": 1630.0800000000002, "text":
  " you only find like very distant ones. How do you detect this and how do you deal
  with this?", "tokens": [51016, 291, 787, 915, 411, 588, 17275, 2306, 13, 1012, 360,
  291, 5531, 341, 293, 577, 360, 291, 2028, 365, 341, 30, 51324], "temperature": 0.0,
  "avg_logprob": -0.13356580016433553, "compression_ratio": 1.759433962264151, "no_speech_prob":
  0.006972862407565117}, {"id": 267, "seek": 161088, "start": 1632.0, "end": 1636.88,
  "text": " So the similarity will be poor and there''ll be no evidence. So the score
  will be low and it will", "tokens": [51420, 407, 264, 32194, 486, 312, 4716, 293,
  456, 603, 312, 572, 4467, 13, 407, 264, 6175, 486, 312, 2295, 293, 309, 486, 51664],
  "temperature": 0.0, "avg_logprob": -0.13356580016433553, "compression_ratio": 1.759433962264151,
  "no_speech_prob": 0.006972862407565117}, {"id": 268, "seek": 163688, "start": 1636.88,
  "end": 1642.16, "text": " be end up dropped to the back of the result list. That''s
  the key. Now, there are a bunch of reasons", "tokens": [50364, 312, 917, 493, 8119,
  281, 264, 646, 295, 264, 1874, 1329, 13, 663, 311, 264, 2141, 13, 823, 11, 456,
  366, 257, 3840, 295, 4112, 50628], "temperature": 0.0, "avg_logprob": -0.13867864770404362,
  "compression_ratio": 1.6551724137931034, "no_speech_prob": 0.005918482784181833},
  {"id": 269, "seek": 163688, "start": 1642.16, "end": 1647.7600000000002, "text":
  " that can happen though. One of those reasons could be that perhaps we do not understand
  the domain,", "tokens": [50628, 300, 393, 1051, 1673, 13, 1485, 295, 729, 4112,
  727, 312, 300, 4317, 321, 360, 406, 1223, 264, 9274, 11, 50908], "temperature":
  0.0, "avg_logprob": -0.13867864770404362, "compression_ratio": 1.6551724137931034,
  "no_speech_prob": 0.005918482784181833}, {"id": 270, "seek": 163688, "start": 1647.7600000000002,
  "end": 1654.48, "text": " as well as the silo does. And one thing, one example of
  that is perhaps we''re dealing with", "tokens": [50908, 382, 731, 382, 264, 3425,
  78, 775, 13, 400, 472, 551, 11, 472, 1365, 295, 300, 307, 4317, 321, 434, 6260,
  365, 51244], "temperature": 0.0, "avg_logprob": -0.13867864770404362, "compression_ratio":
  1.6551724137931034, "no_speech_prob": 0.005918482784181833}, {"id": 271, "seek":
  163688, "start": 1654.48, "end": 1659.44, "text": " transformations of entities,
  very often dictionary based, or sometimes it''s more subtle,", "tokens": [51244,
  34852, 295, 16667, 11, 588, 2049, 25890, 2361, 11, 420, 2171, 309, 311, 544, 13743,
  11, 51492], "temperature": 0.0, "avg_logprob": -0.13867864770404362, "compression_ratio":
  1.6551724137931034, "no_speech_prob": 0.005918482784181833}, {"id": 272, "seek":
  163688, "start": 1660.24, "end": 1666.0, "text": " but one of the things we learned
  very quickly is QueryGee is an open, an amazing open source package", "tokens":
  [51532, 457, 472, 295, 264, 721, 321, 3264, 588, 2661, 307, 2326, 2109, 38, 1653,
  307, 364, 1269, 11, 364, 2243, 1269, 4009, 7372, 51820], "temperature": 0.0, "avg_logprob":
  -0.13867864770404362, "compression_ratio": 1.6551724137931034, "no_speech_prob":
  0.005918482784181833}, {"id": 273, "seek": 166600, "start": 1666.0, "end": 1671.6,
  "text": " that''s used with Elastic Solar, an open source, an open search, I should
  say. And it rewrites", "tokens": [50364, 300, 311, 1143, 365, 2699, 2750, 22385,
  11, 364, 1269, 4009, 11, 364, 1269, 3164, 11, 286, 820, 584, 13, 400, 309, 319,
  86, 30931, 50644], "temperature": 0.0, "avg_logprob": -0.10958928267161051, "compression_ratio":
  1.6714801444043321, "no_speech_prob": 0.0011835844488814473}, {"id": 274, "seek":
  166600, "start": 1671.6, "end": 1675.12, "text": " queries. It''s kind of the standard
  for it. It''s very common to find it. It''s really amazing.", "tokens": [50644,
  24109, 13, 467, 311, 733, 295, 264, 3832, 337, 309, 13, 467, 311, 588, 2689, 281,
  915, 309, 13, 467, 311, 534, 2243, 13, 50820], "temperature": 0.0, "avg_logprob":
  -0.10958928267161051, "compression_ratio": 1.6714801444043321, "no_speech_prob":
  0.0011835844488814473}, {"id": 275, "seek": 166600, "start": 1675.84, "end": 1681.04,
  "text": " So here, the idea is that the silo knows something that we don''t. So
  we actually have an", "tokens": [50856, 407, 510, 11, 264, 1558, 307, 300, 264,
  3425, 78, 3255, 746, 300, 321, 500, 380, 13, 407, 321, 767, 362, 364, 51116], "temperature":
  0.0, "avg_logprob": -0.10958928267161051, "compression_ratio": 1.6714801444043321,
  "no_speech_prob": 0.0011835844488814473}, {"id": 276, "seek": 166600, "start": 1681.04,
  "end": 1686.88, "text": " integration now where we listen to the feedback that comes
  from each engine. So if they report,", "tokens": [51116, 10980, 586, 689, 321, 2140,
  281, 264, 5824, 300, 1487, 490, 1184, 2848, 13, 407, 498, 436, 2275, 11, 51408],
  "temperature": 0.0, "avg_logprob": -0.10958928267161051, "compression_ratio": 1.6714801444043321,
  "no_speech_prob": 0.0011835844488814473}, {"id": 277, "seek": 166600, "start": 1686.88,
  "end": 1692.08, "text": " for example, if they highlight hits, we check the similarity.
  The similarity is high enough", "tokens": [51408, 337, 1365, 11, 498, 436, 5078,
  8664, 11, 321, 1520, 264, 32194, 13, 440, 32194, 307, 1090, 1547, 51668], "temperature":
  0.0, "avg_logprob": -0.10958928267161051, "compression_ratio": 1.6714801444043321,
  "no_speech_prob": 0.0011835844488814473}, {"id": 278, "seek": 169208, "start": 1692.1599999999999,
  "end": 1698.32, "text": " and we''ll honor that. And that''s another idea, where
  we want each of those silos to,", "tokens": [50368, 293, 321, 603, 5968, 300, 13,
  400, 300, 311, 1071, 1558, 11, 689, 321, 528, 1184, 295, 729, 48893, 281, 11, 50676],
  "temperature": 0.0, "avg_logprob": -0.20130513984466267, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.0036669510882347822}, {"id": 279, "seek": 169208, "start": 1698.32,
  "end": 1702.3999999999999, "text": " we want to honor their feedback. Now, we''re
  not today, but in the future,", "tokens": [50676, 321, 528, 281, 5968, 641, 5824,
  13, 823, 11, 321, 434, 406, 965, 11, 457, 294, 264, 2027, 11, 50880], "temperature":
  0.0, "avg_logprob": -0.20130513984466267, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.0036669510882347822}, {"id": 280, "seek": 169208, "start": 1703.4399999999998,
  "end": 1708.56, "text": " why not requery based on expanding our vocabulary around
  the search? Those are all things", "tokens": [50932, 983, 406, 319, 358, 2109, 2361,
  322, 14702, 527, 19864, 926, 264, 3164, 30, 3950, 366, 439, 721, 51188], "temperature":
  0.0, "avg_logprob": -0.20130513984466267, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.0036669510882347822}, {"id": 281, "seek": 169208, "start": 1708.56,
  "end": 1711.28, "text": " that can be done. And by the way, we''d love to get a
  pull request if someone wants to do that.", "tokens": [51188, 300, 393, 312, 1096,
  13, 400, 538, 264, 636, 11, 321, 1116, 959, 281, 483, 257, 2235, 5308, 498, 1580,
  2738, 281, 360, 300, 13, 51324], "temperature": 0.0, "avg_logprob": -0.20130513984466267,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.0036669510882347822},
  {"id": 282, "seek": 169208, "start": 1713.12, "end": 1718.32, "text": " That honestly
  is kind of the key to the whole thing.", "tokens": [51416, 663, 6095, 307, 733,
  295, 264, 2141, 281, 264, 1379, 551, 13, 51676], "temperature": 0.0, "avg_logprob":
  -0.20130513984466267, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.0036669510882347822}, {"id": 283, "seek": 171832, "start": 1719.28, "end": 1725.04,
  "text": " Yeah. So you kind of like learn to innovate. Anyway, you have multiple
  voter problems,", "tokens": [50412, 865, 13, 407, 291, 733, 295, 411, 1466, 281,
  33444, 13, 5684, 11, 291, 362, 3866, 21722, 2740, 11, 50700], "temperature": 0.0,
  "avg_logprob": -0.21927140740787282, "compression_ratio": 1.547486033519553, "no_speech_prob":
  0.02564738504588604}, {"id": 284, "seek": 171832, "start": 1725.6799999999998, "end":
  1733.6799999999998, "text": " but you also want to really hear the signal, hear
  out the signal from every of the voter,", "tokens": [50732, 457, 291, 611, 528,
  281, 534, 1568, 264, 6358, 11, 1568, 484, 264, 6358, 490, 633, 295, 264, 21722,
  11, 51132], "temperature": 0.0, "avg_logprob": -0.21927140740787282, "compression_ratio":
  1.547486033519553, "no_speech_prob": 0.02564738504588604}, {"id": 285, "seek": 171832,
  "start": 1733.6799999999998, "end": 1743.76, "text": " and sort of like make sure
  that you roll this up to the best formula, right? The best representation", "tokens":
  [51132, 293, 1333, 295, 411, 652, 988, 300, 291, 3373, 341, 493, 281, 264, 1151,
  8513, 11, 558, 30, 440, 1151, 10290, 51636], "temperature": 0.0, "avg_logprob":
  -0.21927140740787282, "compression_ratio": 1.547486033519553, "no_speech_prob":
  0.02564738504588604}, {"id": 286, "seek": 174376, "start": 1743.84, "end": 1750.0,
  "text": " of this signal to the user. That''s right. Absolutely. And then you can
  label some of those", "tokens": [50368, 295, 341, 6358, 281, 264, 4195, 13, 663,
  311, 558, 13, 7021, 13, 400, 550, 291, 393, 7645, 512, 295, 729, 50676], "temperature":
  0.0, "avg_logprob": -0.20709907059120922, "compression_ratio": 1.7065217391304348,
  "no_speech_prob": 0.004691182170063257}, {"id": 287, "seek": 174376, "start": 1750.0,
  "end": 1754.08, "text": " sounds because you''re right. Some of them are getting
  really smart. Just some examples. I''ll", "tokens": [50676, 3263, 570, 291, 434,
  558, 13, 2188, 295, 552, 366, 1242, 534, 4069, 13, 1449, 512, 5110, 13, 286, 603,
  50880], "temperature": 0.0, "avg_logprob": -0.20709907059120922, "compression_ratio":
  1.7065217391304348, "no_speech_prob": 0.004691182170063257}, {"id": 288, "seek":
  174376, "start": 1754.08, "end": 1760.48, "text": " throw out some Vectara. Amazing,
  amazing, incredible vector database. That''s probably an inadequate", "tokens":
  [50880, 3507, 484, 512, 691, 557, 2419, 13, 14165, 11, 2243, 11, 4651, 8062, 8149,
  13, 663, 311, 1391, 364, 42107, 51200], "temperature": 0.0, "avg_logprob": -0.20709907059120922,
  "compression_ratio": 1.7065217391304348, "no_speech_prob": 0.004691182170063257},
  {"id": 289, "seek": 174376, "start": 1760.48, "end": 1767.2, "text": " description,
  but it answers questions on your documents. There''s a revolution in Vector,", "tokens":
  [51200, 3855, 11, 457, 309, 6338, 1651, 322, 428, 8512, 13, 821, 311, 257, 8894,
  294, 691, 557, 284, 11, 51536], "temperature": 0.0, "avg_logprob": -0.20709907059120922,
  "compression_ratio": 1.7065217391304348, "no_speech_prob": 0.004691182170063257},
  {"id": 290, "seek": 174376, "start": 1768.24, "end": 1772.72, "text": " in Vector
  search. Some people are focused very much on performance, right? Some people are
  focused", "tokens": [51588, 294, 691, 557, 284, 3164, 13, 2188, 561, 366, 5178,
  588, 709, 322, 3389, 11, 558, 30, 2188, 561, 366, 5178, 51812], "temperature": 0.0,
  "avg_logprob": -0.20709907059120922, "compression_ratio": 1.7065217391304348, "no_speech_prob":
  0.004691182170063257}, {"id": 291, "seek": 177272, "start": 1772.72, "end": 1777.44,
  "text": " on knowledge. Some people are focused on exporting Vectors. So I think
  the enterprise, especially", "tokens": [50364, 322, 3601, 13, 2188, 561, 366, 5178,
  322, 44686, 691, 557, 830, 13, 407, 286, 519, 264, 14132, 11, 2318, 50600], "temperature":
  0.0, "avg_logprob": -0.15711737101056936, "compression_ratio": 1.7098976109215016,
  "no_speech_prob": 0.0005176396225579083}, {"id": 292, "seek": 177272, "start": 1777.44,
  "end": 1783.44, "text": " large enterprise, already has dozens of indexing tools
  and engines and others. And there will be many", "tokens": [50600, 2416, 14132,
  11, 1217, 575, 18431, 295, 8186, 278, 3873, 293, 12982, 293, 2357, 13, 400, 456,
  486, 312, 867, 50900], "temperature": 0.0, "avg_logprob": -0.15711737101056936,
  "compression_ratio": 1.7098976109215016, "no_speech_prob": 0.0005176396225579083},
  {"id": 293, "seek": 177272, "start": 1783.44, "end": 1787.92, "text": " of these
  too, special case, right? There''ll be some that are incredible at customer service.",
  "tokens": [50900, 295, 613, 886, 11, 2121, 1389, 11, 558, 30, 821, 603, 312, 512,
  300, 366, 4651, 412, 5474, 2643, 13, 51124], "temperature": 0.0, "avg_logprob":
  -0.15711737101056936, "compression_ratio": 1.7098976109215016, "no_speech_prob":
  0.0005176396225579083}, {"id": 294, "seek": 177272, "start": 1787.92, "end": 1794.64,
  "text": " And some will be incredible at exception handling. Some will be incredible
  at perhaps sales pre-qualification.", "tokens": [51124, 400, 512, 486, 312, 4651,
  412, 11183, 13175, 13, 2188, 486, 312, 4651, 412, 4317, 5763, 659, 12, 22345, 3774,
  13, 51460], "temperature": 0.0, "avg_logprob": -0.15711737101056936, "compression_ratio":
  1.7098976109215016, "no_speech_prob": 0.0005176396225579083}, {"id": 295, "seek":
  177272, "start": 1794.64, "end": 1800.16, "text": " You know, I just sort of learned
  from the past examples. Watson was going to diagnose everything,", "tokens": [51460,
  509, 458, 11, 286, 445, 1333, 295, 3264, 490, 264, 1791, 5110, 13, 25640, 390, 516,
  281, 36238, 1203, 11, 51736], "temperature": 0.0, "avg_logprob": -0.15711737101056936,
  "compression_ratio": 1.7098976109215016, "no_speech_prob": 0.0005176396225579083},
  {"id": 296, "seek": 180016, "start": 1800.16, "end": 1803.92, "text": " right? And
  I think what it ultimately did well was pre-approval authorizations.", "tokens":
  [50364, 558, 30, 400, 286, 519, 437, 309, 6284, 630, 731, 390, 659, 12, 35821, 3337,
  3793, 14455, 13, 50552], "temperature": 0.0, "avg_logprob": -0.12786371477188602,
  "compression_ratio": 1.6402877697841727, "no_speech_prob": 0.004836043808609247},
  {"id": 297, "seek": 180016, "start": 1805.3600000000001, "end": 1810.3200000000002,
  "text": " So, but over time, I think it''s clearly these will all become more automated.
  And so then,", "tokens": [50624, 407, 11, 457, 670, 565, 11, 286, 519, 309, 311,
  4448, 613, 486, 439, 1813, 544, 18473, 13, 400, 370, 550, 11, 50872], "temperature":
  0.0, "avg_logprob": -0.12786371477188602, "compression_ratio": 1.6402877697841727,
  "no_speech_prob": 0.004836043808609247}, {"id": 298, "seek": 180016, "start": 1810.3200000000002,
  "end": 1814.3200000000002, "text": " but you still need a way, if you''re trying
  to figure out what''s new across these salads,", "tokens": [50872, 457, 291, 920,
  643, 257, 636, 11, 498, 291, 434, 1382, 281, 2573, 484, 437, 311, 777, 2108, 613,
  48025, 11, 51072], "temperature": 0.0, "avg_logprob": -0.12786371477188602, "compression_ratio":
  1.6402877697841727, "no_speech_prob": 0.004836043808609247}, {"id": 299, "seek":
  180016, "start": 1814.3200000000002, "end": 1818.96, "text": " you still need a
  way to query them all. And so this world''s happy. We have an integration with chat",
  "tokens": [51072, 291, 920, 643, 257, 636, 281, 14581, 552, 439, 13, 400, 370, 341,
  1002, 311, 2055, 13, 492, 362, 364, 10980, 365, 5081, 51304], "temperature": 0.0,
  "avg_logprob": -0.12786371477188602, "compression_ratio": 1.6402877697841727, "no_speech_prob":
  0.004836043808609247}, {"id": 300, "seek": 180016, "start": 1818.96, "end": 1825.8400000000001,
  "text": " GPT. You can query chat GPT. In fact, by default, we query it if you put
  your key in every time.", "tokens": [51304, 26039, 51, 13, 509, 393, 14581, 5081,
  26039, 51, 13, 682, 1186, 11, 538, 7576, 11, 321, 14581, 309, 498, 291, 829, 428,
  2141, 294, 633, 565, 13, 51648], "temperature": 0.0, "avg_logprob": -0.12786371477188602,
  "compression_ratio": 1.6402877697841727, "no_speech_prob": 0.004836043808609247},
  {"id": 301, "seek": 182584, "start": 1825.9199999999998, "end": 1830.72, "text":
  " So you and we rewrite the query. If the query is a question, we just pass it right
  along. If it''s not,", "tokens": [50368, 407, 291, 293, 321, 28132, 264, 14581,
  13, 759, 264, 14581, 307, 257, 1168, 11, 321, 445, 1320, 309, 558, 2051, 13, 759,
  309, 311, 406, 11, 50608], "temperature": 0.0, "avg_logprob": -0.158424617737297,
  "compression_ratio": 1.7366412213740459, "no_speech_prob": 0.002280054846778512},
  {"id": 302, "seek": 182584, "start": 1830.72, "end": 1834.1599999999999, "text":
  " we ask rewrite it using a prompt to something like tell me about", "tokens": [50608,
  321, 1029, 28132, 309, 1228, 257, 12391, 281, 746, 411, 980, 385, 466, 50780], "temperature":
  0.0, "avg_logprob": -0.158424617737297, "compression_ratio": 1.7366412213740459,
  "no_speech_prob": 0.002280054846778512}, {"id": 303, "seek": 182584, "start": 1835.6,
  "end": 1840.3999999999999, "text": " thing. So you get a summary, right, which we
  pop up for, I think we also have a query processor.", "tokens": [50852, 551, 13,
  407, 291, 483, 257, 12691, 11, 558, 11, 597, 321, 1665, 493, 337, 11, 286, 519,
  321, 611, 362, 257, 14581, 15321, 13, 51092], "temperature": 0.0, "avg_logprob":
  -0.158424617737297, "compression_ratio": 1.7366412213740459, "no_speech_prob": 0.002280054846778512},
  {"id": 304, "seek": 182584, "start": 1841.04, "end": 1845.84, "text": " So you can
  have a chat GPT change the user''s query. Like you could say rewrite this to a Boolean,",
  "tokens": [51124, 407, 291, 393, 362, 257, 5081, 26039, 51, 1319, 264, 4195, 311,
  14581, 13, 1743, 291, 727, 584, 28132, 341, 281, 257, 23351, 28499, 11, 51364],
  "temperature": 0.0, "avg_logprob": -0.158424617737297, "compression_ratio": 1.7366412213740459,
  "no_speech_prob": 0.002280054846778512}, {"id": 305, "seek": 182584, "start": 1845.84,
  "end": 1851.12, "text": " or rewrite this why not to a vector. But in the end, right,
  it''s going to do that on its own", "tokens": [51364, 420, 28132, 341, 983, 406,
  281, 257, 8062, 13, 583, 294, 264, 917, 11, 558, 11, 309, 311, 516, 281, 360, 300,
  322, 1080, 1065, 51628], "temperature": 0.0, "avg_logprob": -0.158424617737297,
  "compression_ratio": 1.7366412213740459, "no_speech_prob": 0.002280054846778512},
  {"id": 306, "seek": 185112, "start": 1851.1999999999998, "end": 1857.4399999999998,
  "text": " on the back side of things. So when you''re trying to solve problems in
  the enterprise, the key is", "tokens": [50368, 322, 264, 646, 1252, 295, 721, 13,
  407, 562, 291, 434, 1382, 281, 5039, 2740, 294, 264, 14132, 11, 264, 2141, 307,
  50680], "temperature": 0.0, "avg_logprob": -0.10358491758020913, "compression_ratio":
  1.7686832740213523, "no_speech_prob": 0.005133743863552809}, {"id": 307, "seek":
  185112, "start": 1857.4399999999998, "end": 1863.52, "text": " you need an interface
  to write to. And it would be nice not to have to write code to connect to", "tokens":
  [50680, 291, 643, 364, 9226, 281, 2464, 281, 13, 400, 309, 576, 312, 1481, 406,
  281, 362, 281, 2464, 3089, 281, 1745, 281, 50984], "temperature": 0.0, "avg_logprob":
  -0.10358491758020913, "compression_ratio": 1.7686832740213523, "no_speech_prob":
  0.005133743863552809}, {"id": 308, "seek": 185112, "start": 1863.52, "end": 1868.3999999999999,
  "text": " all these things, getting back to your question about architecture. And
  so those are the key abstractions", "tokens": [50984, 439, 613, 721, 11, 1242, 646,
  281, 428, 1168, 466, 9482, 13, 400, 370, 729, 366, 264, 2141, 12649, 626, 51228],
  "temperature": 0.0, "avg_logprob": -0.10358491758020913, "compression_ratio": 1.7686832740213523,
  "no_speech_prob": 0.005133743863552809}, {"id": 309, "seek": 185112, "start": 1868.3999999999999,
  "end": 1872.7199999999998, "text": " in Swirl. Swirl, you don''t have to write code
  to connect to an endpoint that we already have a", "tokens": [51228, 294, 3926,
  1648, 13, 3926, 1648, 11, 291, 500, 380, 362, 281, 2464, 3089, 281, 1745, 281, 364,
  35795, 300, 321, 1217, 362, 257, 51444], "temperature": 0.0, "avg_logprob": -0.10358491758020913,
  "compression_ratio": 1.7686832740213523, "no_speech_prob": 0.005133743863552809},
  {"id": 310, "seek": 185112, "start": 1872.7199999999998, "end": 1877.6799999999998,
  "text": " connector to. You just write a search provider. All you need to know is
  JSON path and maybe be able to", "tokens": [51444, 19127, 281, 13, 509, 445, 2464,
  257, 3164, 12398, 13, 1057, 291, 643, 281, 458, 307, 31828, 3100, 293, 1310, 312,
  1075, 281, 51692], "temperature": 0.0, "avg_logprob": -0.10358491758020913, "compression_ratio":
  1.7686832740213523, "no_speech_prob": 0.005133743863552809}, {"id": 311, "seek":
  187768, "start": 1877.68, "end": 1882.0800000000002, "text": " read a little developer
  API dog. Right. And then that you''ll pretty much be able to get the search", "tokens":
  [50364, 1401, 257, 707, 10754, 9362, 3000, 13, 1779, 13, 400, 550, 300, 291, 603,
  1238, 709, 312, 1075, 281, 483, 264, 3164, 50584], "temperature": 0.0, "avg_logprob":
  -0.1342258297029089, "compression_ratio": 1.6609589041095891, "no_speech_prob":
  0.00152679649181664}, {"id": 312, "seek": 187768, "start": 1882.0800000000002, "end":
  1887.8400000000001, "text": " provider. If you need to write a connector. And of
  course, here''s the punch line. Well, I think", "tokens": [50584, 12398, 13, 759,
  291, 643, 281, 2464, 257, 19127, 13, 400, 295, 1164, 11, 510, 311, 264, 8135, 1622,
  13, 1042, 11, 286, 519, 50872], "temperature": 0.0, "avg_logprob": -0.1342258297029089,
  "compression_ratio": 1.6609589041095891, "no_speech_prob": 0.00152679649181664},
  {"id": 313, "seek": 187768, "start": 1887.8400000000001, "end": 1892.88, "text":
  " it will probably take you a couple hours, depending on your skill at Python. But
  on average,", "tokens": [50872, 309, 486, 1391, 747, 291, 257, 1916, 2496, 11, 5413,
  322, 428, 5389, 412, 15329, 13, 583, 322, 4274, 11, 51124], "temperature": 0.0,
  "avg_logprob": -0.1342258297029089, "compression_ratio": 1.6609589041095891, "no_speech_prob":
  0.00152679649181664}, {"id": 314, "seek": 187768, "start": 1892.88, "end": 1898.0,
  "text": " it shouldn''t take more than two hours because I can give you a prompt.
  And we can teach chat GPT", "tokens": [51124, 309, 4659, 380, 747, 544, 813, 732,
  2496, 570, 286, 393, 976, 291, 257, 12391, 13, 400, 321, 393, 2924, 5081, 26039,
  51, 51380], "temperature": 0.0, "avg_logprob": -0.1342258297029089, "compression_ratio":
  1.6609589041095891, "no_speech_prob": 0.00152679649181664}, {"id": 315, "seek":
  187768, "start": 1898.0, "end": 1903.04, "text": " about the connector class. You
  should be able to get that done in a couple hours just fixing up what", "tokens":
  [51380, 466, 264, 19127, 1508, 13, 509, 820, 312, 1075, 281, 483, 300, 1096, 294,
  257, 1916, 2496, 445, 19442, 493, 437, 51632], "temperature": 0.0, "avg_logprob":
  -0.1342258297029089, "compression_ratio": 1.6609589041095891, "no_speech_prob":
  0.00152679649181664}, {"id": 316, "seek": 190304, "start": 1903.04, "end": 1909.76,
  "text": " it does. I found that about 70% of the time, it will produce a workable
  connector. Just", "tokens": [50364, 309, 775, 13, 286, 1352, 300, 466, 5285, 4,
  295, 264, 565, 11, 309, 486, 5258, 257, 589, 712, 19127, 13, 1449, 50700], "temperature":
  0.0, "avg_logprob": -0.16571494280281712, "compression_ratio": 1.6418439716312057,
  "no_speech_prob": 0.002055591205134988}, {"id": 317, "seek": 190304, "start": 1909.76,
  "end": 1914.6399999999999, "text": " fast. The right prompt, right? Teach it how
  to teach it our connector class. And give it the", "tokens": [50700, 2370, 13, 440,
  558, 12391, 11, 558, 30, 26816, 309, 577, 281, 2924, 309, 527, 19127, 1508, 13,
  400, 976, 309, 264, 50944], "temperature": 0.0, "avg_logprob": -0.16571494280281712,
  "compression_ratio": 1.6418439716312057, "no_speech_prob": 0.002055591205134988},
  {"id": 318, "seek": 190304, "start": 1914.6399999999999, "end": 1919.6, "text":
  " right prompt and bang, you have sort of almost working codes. Yeah, I think this
  is the best part", "tokens": [50944, 558, 12391, 293, 8550, 11, 291, 362, 1333,
  295, 1920, 1364, 14211, 13, 865, 11, 286, 519, 341, 307, 264, 1151, 644, 51192],
  "temperature": 0.0, "avg_logprob": -0.16571494280281712, "compression_ratio": 1.6418439716312057,
  "no_speech_prob": 0.002055591205134988}, {"id": 319, "seek": 190304, "start": 1919.6,
  "end": 1926.1599999999999, "text": " of interfaces like chat GPT systems like chat
  GPT is that you can outsource this mundane work", "tokens": [51192, 295, 28416,
  411, 5081, 26039, 51, 3652, 411, 5081, 26039, 51, 307, 300, 291, 393, 14758, 2948,
  341, 43497, 589, 51520], "temperature": 0.0, "avg_logprob": -0.16571494280281712,
  "compression_ratio": 1.6418439716312057, "no_speech_prob": 0.002055591205134988},
  {"id": 320, "seek": 190304, "start": 1926.1599999999999, "end": 1932.72, "text":
  " and really focus on the actual thing. I was actually born away myself. And to
  some extent,", "tokens": [51520, 293, 534, 1879, 322, 264, 3539, 551, 13, 286, 390,
  767, 4232, 1314, 2059, 13, 400, 281, 512, 8396, 11, 51848], "temperature": 0.0,
  "avg_logprob": -0.16571494280281712, "compression_ratio": 1.6418439716312057, "no_speech_prob":
  0.002055591205134988}, {"id": 321, "seek": 193272, "start": 1932.72, "end": 1938.72,
  "text": " scared you weeks ago when I was just saying, Hey, can you create a Python
  code which we''ll talk to", "tokens": [50364, 5338, 291, 3259, 2057, 562, 286, 390,
  445, 1566, 11, 1911, 11, 393, 291, 1884, 257, 15329, 3089, 597, 321, 603, 751, 281,
  50664], "temperature": 0.0, "avg_logprob": -0.23262975592362253, "compression_ratio":
  1.5120967741935485, "no_speech_prob": 0.0064412672072649}, {"id": 322, "seek": 193272,
  "start": 1939.44, "end": 1945.76, "text": " TomTom search API map search API. And
  it did create it. It just asked me to insert like a", "tokens": [50700, 5041, 23442,
  3164, 9362, 4471, 3164, 9362, 13, 400, 309, 630, 1884, 309, 13, 467, 445, 2351,
  385, 281, 8969, 411, 257, 51016], "temperature": 0.0, "avg_logprob": -0.23262975592362253,
  "compression_ratio": 1.5120967741935485, "no_speech_prob": 0.0064412672072649},
  {"id": 323, "seek": 193272, "start": 1946.88, "end": 1952.48, "text": " token. So
  I just subscribe developer token. But I was really blown away. Like I would have",
  "tokens": [51072, 14862, 13, 407, 286, 445, 3022, 10754, 14862, 13, 583, 286, 390,
  534, 16479, 1314, 13, 1743, 286, 576, 362, 51352], "temperature": 0.0, "avg_logprob":
  -0.23262975592362253, "compression_ratio": 1.5120967741935485, "no_speech_prob":
  0.0064412672072649}, {"id": 324, "seek": 193272, "start": 1952.48, "end": 1958.16,
  "text": " spent probably like several half a days here and there figuring things
  out, right? If it wasn''t", "tokens": [51352, 4418, 1391, 411, 2940, 1922, 257,
  1708, 510, 293, 456, 15213, 721, 484, 11, 558, 30, 759, 309, 2067, 380, 51636],
  "temperature": 0.0, "avg_logprob": -0.23262975592362253, "compression_ratio": 1.5120967741935485,
  "no_speech_prob": 0.0064412672072649}, {"id": 325, "seek": 195816, "start": 1958.16,
  "end": 1966.48, "text": " TomTom or some other API. But yeah, I think this is amazing.
  And I think, well, I believe that you", "tokens": [50364, 5041, 23442, 420, 512,
  661, 9362, 13, 583, 1338, 11, 286, 519, 341, 307, 2243, 13, 400, 286, 519, 11, 731,
  11, 286, 1697, 300, 291, 50780], "temperature": 0.0, "avg_logprob": -0.14554504344337865,
  "compression_ratio": 1.5076923076923077, "no_speech_prob": 0.005329399835318327},
  {"id": 326, "seek": 195816, "start": 1966.48, "end": 1972.96, "text": " guys are
  documenting a lot. But if you if you haven''t yet, which just explained within documents,",
  "tokens": [50780, 1074, 366, 42360, 257, 688, 13, 583, 498, 291, 498, 291, 2378,
  380, 1939, 11, 597, 445, 8825, 1951, 8512, 11, 51104], "temperature": 0.0, "avg_logprob":
  -0.14554504344337865, "compression_ratio": 1.5076923076923077, "no_speech_prob":
  0.005329399835318327}, {"id": 327, "seek": 195816, "start": 1972.96, "end": 1981.44,
  "text": " I think that could save a lot of time for developers. But I was wondering
  maybe you would like to", "tokens": [51104, 286, 519, 300, 727, 3155, 257, 688,
  295, 565, 337, 8849, 13, 583, 286, 390, 6359, 1310, 291, 576, 411, 281, 51528],
  "temperature": 0.0, "avg_logprob": -0.14554504344337865, "compression_ratio": 1.5076923076923077,
  "no_speech_prob": 0.005329399835318327}, {"id": 328, "seek": 198144, "start": 1981.44,
  "end": 1988.96, "text": " show us a demo of swirl and then we''ll dig deeper into
  that. Absolutely. So let me share my screen.", "tokens": [50364, 855, 505, 257,
  10723, 295, 30310, 293, 550, 321, 603, 2528, 7731, 666, 300, 13, 7021, 13, 407,
  718, 385, 2073, 452, 2568, 13, 50740], "temperature": 0.0, "avg_logprob": -0.15176015286832242,
  "compression_ratio": 1.510989010989011, "no_speech_prob": 0.006961983162909746},
  {"id": 329, "seek": 198144, "start": 1990.0800000000002, "end": 1999.1200000000001,
  "text": " So hopefully you can see my screen. Yes. So this is swirl. Actually, I''ll
  start here.", "tokens": [50796, 407, 4696, 291, 393, 536, 452, 2568, 13, 1079, 13,
  407, 341, 307, 30310, 13, 5135, 11, 286, 603, 722, 510, 13, 51248], "temperature":
  0.0, "avg_logprob": -0.15176015286832242, "compression_ratio": 1.510989010989011,
  "no_speech_prob": 0.006961983162909746}, {"id": 330, "seek": 198144, "start": 2000.24,
  "end": 2008.64, "text": " This is the swirl repo. Everything you need to get started
  is here. The readme describes,", "tokens": [51304, 639, 307, 264, 30310, 49040,
  13, 5471, 291, 643, 281, 483, 1409, 307, 510, 13, 440, 1401, 1398, 15626, 11, 51724],
  "temperature": 0.0, "avg_logprob": -0.15176015286832242, "compression_ratio": 1.510989010989011,
  "no_speech_prob": 0.006961983162909746}, {"id": 331, "seek": 200864, "start": 2009.44,
  "end": 2014.16, "text": " pretty much the two commands you need to run to get swirl
  running if you have Docker.", "tokens": [50404, 1238, 709, 264, 732, 16901, 291,
  643, 281, 1190, 281, 483, 30310, 2614, 498, 291, 362, 33772, 13, 50640], "temperature":
  0.0, "avg_logprob": -0.13183361291885376, "compression_ratio": 1.6232394366197183,
  "no_speech_prob": 0.01708962209522724}, {"id": 332, "seek": 200864, "start": 2014.16,
  "end": 2019.76, "text": " There are more detailed instructions if you want to download.
  Everything that you''ll see here runs,", "tokens": [50640, 821, 366, 544, 9942,
  9415, 498, 291, 528, 281, 5484, 13, 5471, 300, 291, 603, 536, 510, 6676, 11, 50920],
  "temperature": 0.0, "avg_logprob": -0.13183361291885376, "compression_ratio": 1.6232394366197183,
  "no_speech_prob": 0.01708962209522724}, {"id": 333, "seek": 200864, "start": 2020.64,
  "end": 2026.48, "text": " we have automated tests against everything. We have a
  whole CICD environment. And support,", "tokens": [50964, 321, 362, 18473, 6921,
  1970, 1203, 13, 492, 362, 257, 1379, 383, 2532, 35, 2823, 13, 400, 1406, 11, 51256],
  "temperature": 0.0, "avg_logprob": -0.13183361291885376, "compression_ratio": 1.6232394366197183,
  "no_speech_prob": 0.01708962209522724}, {"id": 334, "seek": 200864, "start": 2026.48,
  "end": 2030.4, "text": " I just want to be clear, is free. Please just join our
  Slack channel and we''re happy to help", "tokens": [51256, 286, 445, 528, 281, 312,
  1850, 11, 307, 1737, 13, 2555, 445, 3917, 527, 37211, 2269, 293, 321, 434, 2055,
  281, 854, 51452], "temperature": 0.0, "avg_logprob": -0.13183361291885376, "compression_ratio":
  1.6232394366197183, "no_speech_prob": 0.01708962209522724}, {"id": 335, "seek":
  200864, "start": 2031.2800000000002, "end": 2038.5600000000002, "text": " anytime,
  anywhere. Now, when you get swirl installed locally, as I have it, you''ll get this",
  "tokens": [51496, 13038, 11, 4992, 13, 823, 11, 562, 291, 483, 30310, 8899, 16143,
  11, 382, 286, 362, 309, 11, 291, 603, 483, 341, 51860], "temperature": 0.0, "avg_logprob":
  -0.13183361291885376, "compression_ratio": 1.6232394366197183, "no_speech_prob":
  0.01708962209522724}, {"id": 336, "seek": 203856, "start": 2038.56, "end": 2045.44,
  "text": " nice homepage. But ultimately, what most people want to see is the UI.
  So this is Spyglass. It''s an", "tokens": [50364, 1481, 31301, 13, 583, 6284, 11,
  437, 881, 561, 528, 281, 536, 307, 264, 15682, 13, 407, 341, 307, 35854, 28851,
  13, 467, 311, 364, 50708], "temperature": 0.0, "avg_logprob": -0.16613170888164255,
  "compression_ratio": 1.5856573705179282, "no_speech_prob": 0.000386636151233688},
  {"id": 337, "seek": 203856, "start": 2045.44, "end": 2053.2799999999997, "text":
  " open source UI produced by a sister company, KMW, actually long time friend Kevin
  Waters. And he''s", "tokens": [50708, 1269, 4009, 15682, 7126, 538, 257, 4892, 2237,
  11, 591, 44, 54, 11, 767, 938, 565, 1277, 9954, 46743, 13, 400, 415, 311, 51100],
  "temperature": 0.0, "avg_logprob": -0.16613170888164255, "compression_ratio": 1.5856573705179282,
  "no_speech_prob": 0.000386636151233688}, {"id": 338, "seek": 203856, "start": 2053.2799999999997,
  "end": 2060.64, "text": " a long time committer and a contributor to the open source
  community as well. So Spyglass is a great", "tokens": [51100, 257, 938, 565, 800,
  3904, 293, 257, 42859, 281, 264, 1269, 4009, 1768, 382, 731, 13, 407, 35854, 28851,
  307, 257, 869, 51468], "temperature": 0.0, "avg_logprob": -0.16613170888164255,
  "compression_ratio": 1.5856573705179282, "no_speech_prob": 0.000386636151233688},
  {"id": 339, "seek": 203856, "start": 2060.64, "end": 2065.84, "text": " starting
  point for building user interfaces. It has a lot of the key building blocks. And
  so here,", "tokens": [51468, 2891, 935, 337, 2390, 4195, 28416, 13, 467, 575, 257,
  688, 295, 264, 2141, 2390, 8474, 13, 400, 370, 510, 11, 51728], "temperature": 0.0,
  "avg_logprob": -0.16613170888164255, "compression_ratio": 1.5856573705179282, "no_speech_prob":
  0.000386636151233688}, {"id": 340, "seek": 206584, "start": 2065.92, "end": 2074.1600000000003,
  "text": " yesterday, I was thinking about how we wrote a document. You sent me a
  document to use. And", "tokens": [50368, 5186, 11, 286, 390, 1953, 466, 577, 321,
  4114, 257, 4166, 13, 509, 2279, 385, 257, 4166, 281, 764, 13, 400, 50780], "temperature":
  0.0, "avg_logprob": -0.16641987363497415, "compression_ratio": 1.6120689655172413,
  "no_speech_prob": 0.00249667395837605}, {"id": 341, "seek": 206584, "start": 2075.44,
  "end": 2080.48, "text": " I admit today, I was seeing you''re going, where is that
  document? And I actually said,", "tokens": [50844, 286, 9796, 965, 11, 286, 390,
  2577, 291, 434, 516, 11, 689, 307, 300, 4166, 30, 400, 286, 767, 848, 11, 51096],
  "temperature": 0.0, "avg_logprob": -0.16641987363497415, "compression_ratio": 1.6120689655172413,
  "no_speech_prob": 0.00249667395837605}, {"id": 342, "seek": 206584, "start": 2080.48,
  "end": 2085.84, "text": " okay, it''s in Microsoft Outlook and I found it. But I
  forgot that I could search because one of", "tokens": [51096, 1392, 11, 309, 311,
  294, 8116, 5925, 12747, 293, 286, 1352, 309, 13, 583, 286, 5298, 300, 286, 727,
  3164, 570, 472, 295, 51364], "temperature": 0.0, "avg_logprob": -0.16641987363497415,
  "compression_ratio": 1.6120689655172413, "no_speech_prob": 0.00249667395837605},
  {"id": 343, "seek": 206584, "start": 2085.84, "end": 2090.08, "text": " the great
  things about that''s coming out in swirl version two, which is going to drop next
  month in", "tokens": [51364, 264, 869, 721, 466, 300, 311, 1348, 484, 294, 30310,
  3037, 732, 11, 597, 307, 516, 281, 3270, 958, 1618, 294, 51576], "temperature":
  0.0, "avg_logprob": -0.16641987363497415, "compression_ratio": 1.6120689655172413,
  "no_speech_prob": 0.00249667395837605}, {"id": 344, "seek": 209008, "start": 2090.56,
  "end": 2098.72, "text": " May is we have full M365 support. So you can do the OAuth
  two dance. And I''ve actually searched through", "tokens": [50388, 1891, 307, 321,
  362, 1577, 376, 11309, 20, 1406, 13, 407, 291, 393, 360, 264, 48424, 2910, 732,
  4489, 13, 400, 286, 600, 767, 22961, 807, 50796], "temperature": 0.0, "avg_logprob":
  -0.14870882969276578, "compression_ratio": 1.6244897959183673, "no_speech_prob":
  0.0049230908043682575}, {"id": 345, "seek": 209008, "start": 2098.72, "end": 2104.7999999999997,
  "text": " my M365. And here''s my acceptance of your your meeting, actually, some
  other references to it. And", "tokens": [50796, 452, 376, 11309, 20, 13, 400, 510,
  311, 452, 20351, 295, 428, 428, 3440, 11, 767, 11, 512, 661, 15400, 281, 309, 13,
  400, 51100], "temperature": 0.0, "avg_logprob": -0.14870882969276578, "compression_ratio":
  1.6244897959183673, "no_speech_prob": 0.0049230908043682575}, {"id": 346, "seek":
  209008, "start": 2104.7999999999997, "end": 2109.7599999999998, "text": " then here,
  document number four, document shared with you, vector podcast. So if I had searched,",
  "tokens": [51100, 550, 510, 11, 4166, 1230, 1451, 11, 4166, 5507, 365, 291, 11,
  8062, 7367, 13, 407, 498, 286, 632, 22961, 11, 51348], "temperature": 0.0, "avg_logprob":
  -0.14870882969276578, "compression_ratio": 1.6244897959183673, "no_speech_prob":
  0.0049230908043682575}, {"id": 347, "seek": 209008, "start": 2109.7599999999998,
  "end": 2114.16, "text": " it would have been the fourth hit above the fold. And
  I actually haven''t done the relevancy tuning", "tokens": [51348, 309, 576, 362,
  668, 264, 6409, 2045, 3673, 264, 4860, 13, 400, 286, 767, 2378, 380, 1096, 264,
  25916, 6717, 15164, 51568], "temperature": 0.0, "avg_logprob": -0.14870882969276578,
  "compression_ratio": 1.6244897959183673, "no_speech_prob": 0.0049230908043682575},
  {"id": 348, "seek": 211416, "start": 2114.3999999999996, "end": 2121.44, "text":
  " on email or one drive yet. So it worked well enough to come up. But what I think
  you can see again", "tokens": [50376, 322, 3796, 420, 472, 3332, 1939, 13, 407,
  309, 2732, 731, 1547, 281, 808, 493, 13, 583, 437, 286, 519, 291, 393, 536, 797,
  50728], "temperature": 0.0, "avg_logprob": -0.1231204754597432, "compression_ratio":
  1.529100529100529, "no_speech_prob": 0.0007240819395519793}, {"id": 349, "seek":
  211416, "start": 2122.48, "end": 2131.7599999999998, "text": " is the matches are
  early in the document. It favors them. First of all, of course, it likes both",
  "tokens": [50780, 307, 264, 10676, 366, 2440, 294, 264, 4166, 13, 467, 40554, 552,
  13, 2386, 295, 439, 11, 295, 1164, 11, 309, 5902, 1293, 51244], "temperature": 0.0,
  "avg_logprob": -0.1231204754597432, "compression_ratio": 1.529100529100529, "no_speech_prob":
  0.0007240819395519793}, {"id": 350, "seek": 211416, "start": 2131.7599999999998,
  "end": 2138.8799999999997, "text": " terms together, but it favors them without
  with some exceptions. It favors the term that''s to", "tokens": [51244, 2115, 1214,
  11, 457, 309, 40554, 552, 1553, 365, 512, 22847, 13, 467, 40554, 264, 1433, 300,
  311, 281, 51600], "temperature": 0.0, "avg_logprob": -0.1231204754597432, "compression_ratio":
  1.529100529100529, "no_speech_prob": 0.0007240819395519793}, {"id": 351, "seek":
  213888, "start": 2138.96, "end": 2142.8, "text": " the left. And so you can see
  there were a lot of results, but only a few really ranked.", "tokens": [50368, 264,
  1411, 13, 400, 370, 291, 393, 536, 456, 645, 257, 688, 295, 3542, 11, 457, 787,
  257, 1326, 534, 20197, 13, 50560], "temperature": 0.0, "avg_logprob": -0.12193725420081097,
  "compression_ratio": 1.5899581589958158, "no_speech_prob": 0.0023759170435369015},
  {"id": 352, "seek": 213888, "start": 2144.2400000000002, "end": 2149.28, "text":
  " Yeah, hi. And that''s the key, right? I scan it. I''m pretty much done now. And
  I can say,", "tokens": [50632, 865, 11, 4879, 13, 400, 300, 311, 264, 2141, 11,
  558, 30, 286, 11049, 309, 13, 286, 478, 1238, 709, 1096, 586, 13, 400, 286, 393,
  584, 11, 50884], "temperature": 0.0, "avg_logprob": -0.12193725420081097, "compression_ratio":
  1.5899581589958158, "no_speech_prob": 0.0023759170435369015}, {"id": 353, "seek":
  213888, "start": 2149.28, "end": 2153.28, "text": " you know, I probably want to
  go look in my email or my one drive. That''s more than likely where it is.", "tokens":
  [50884, 291, 458, 11, 286, 1391, 528, 281, 352, 574, 294, 452, 3796, 420, 452, 472,
  3332, 13, 663, 311, 544, 813, 3700, 689, 309, 307, 13, 51084], "temperature": 0.0,
  "avg_logprob": -0.12193725420081097, "compression_ratio": 1.5899581589958158, "no_speech_prob":
  0.0023759170435369015}, {"id": 354, "seek": 213888, "start": 2153.84, "end": 2161.84,
  "text": " And I can go and do that, you know, very simply. Right, there we go. Now
  I have in the top three. So", "tokens": [51112, 400, 286, 393, 352, 293, 360, 300,
  11, 291, 458, 11, 588, 2935, 13, 1779, 11, 456, 321, 352, 13, 823, 286, 362, 294,
  264, 1192, 1045, 13, 407, 51512], "temperature": 0.0, "avg_logprob": -0.12193725420081097,
  "compression_ratio": 1.5899581589958158, "no_speech_prob": 0.0023759170435369015},
  {"id": 355, "seek": 216184, "start": 2162.0, "end": 2169.92, "text": " the power
  of meta search though is more than just that. I will just let''s do that.", "tokens":
  [50372, 264, 1347, 295, 19616, 3164, 1673, 307, 544, 813, 445, 300, 13, 286, 486,
  445, 718, 311, 360, 300, 13, 50768], "temperature": 0.0, "avg_logprob": -0.317051751273019,
  "compression_ratio": 1.4821428571428572, "no_speech_prob": 0.00201908266171813},
  {"id": 356, "seek": 216184, "start": 2169.92, "end": 2177.36, "text": " Is it like
  a Django app or? Yes. Yeah. Yeah. So the stack is the stack is", "tokens": [50768,
  1119, 309, 411, 257, 33464, 17150, 724, 420, 30, 1079, 13, 865, 13, 865, 13, 407,
  264, 8630, 307, 264, 8630, 307, 51140], "temperature": 0.0, "avg_logprob": -0.317051751273019,
  "compression_ratio": 1.4821428571428572, "no_speech_prob": 0.00201908266171813},
  {"id": 357, "seek": 216184, "start": 2179.1200000000003, "end": 2186.0, "text":
  " rabbit Django Python celery, although we''re not using too much celery and SQLite
  or Postgres", "tokens": [51228, 19509, 33464, 17150, 15329, 37643, 11, 4878, 321,
  434, 406, 1228, 886, 709, 37643, 293, 19200, 642, 420, 10223, 45189, 51572], "temperature":
  0.0, "avg_logprob": -0.317051751273019, "compression_ratio": 1.4821428571428572,
  "no_speech_prob": 0.00201908266171813}, {"id": 358, "seek": 218600, "start": 2186.88,
  "end": 2193.04, "text": " with a lot of packages. We use NLTK, Spacey, Jason Path,
  some others.", "tokens": [50408, 365, 257, 688, 295, 17401, 13, 492, 764, 426, 43,
  51, 42, 11, 8705, 88, 11, 11181, 21914, 11, 512, 2357, 13, 50716], "temperature":
  0.0, "avg_logprob": -0.2485576919887377, "compression_ratio": 1.4889867841409692,
  "no_speech_prob": 0.0026296114083379507}, {"id": 359, "seek": 218600, "start": 2200.64,
  "end": 2205.12, "text": " So now, so here I am running my electric vehicle company,
  Colin Tesla.", "tokens": [51096, 407, 586, 11, 370, 510, 286, 669, 2614, 452, 5210,
  5864, 2237, 11, 29253, 13666, 13, 51320], "temperature": 0.0, "avg_logprob": -0.2485576919887377,
  "compression_ratio": 1.4889867841409692, "no_speech_prob": 0.0026296114083379507},
  {"id": 360, "seek": 218600, "start": 2206.0, "end": 2209.84, "text": " This is an
  earlier version of the software. So you''re going to see some, there''s one bug
  here,", "tokens": [51364, 639, 307, 364, 3071, 3037, 295, 264, 4722, 13, 407, 291,
  434, 516, 281, 536, 512, 11, 456, 311, 472, 7426, 510, 11, 51556], "temperature":
  0.0, "avg_logprob": -0.2485576919887377, "compression_ratio": 1.4889867841409692,
  "no_speech_prob": 0.0026296114083379507}, {"id": 361, "seek": 218600, "start": 2209.84,
  "end": 2214.96, "text": " which is you''ll see the emphasis tags instead of having
  them render, just because I reloaded the older", "tokens": [51556, 597, 307, 291,
  603, 536, 264, 16271, 18632, 2602, 295, 1419, 552, 15529, 11, 445, 570, 286, 25628,
  292, 264, 4906, 51812], "temperature": 0.0, "avg_logprob": -0.2485576919887377,
  "compression_ratio": 1.4889867841409692, "no_speech_prob": 0.0026296114083379507},
  {"id": 362, "seek": 221496, "start": 2214.96, "end": 2223.36, "text": " version.
  But here we can see a lot more sources than just, just, you know, enterprise sources.",
  "tokens": [50364, 3037, 13, 583, 510, 321, 393, 536, 257, 688, 544, 7139, 813, 445,
  11, 445, 11, 291, 458, 11, 14132, 7139, 13, 50784], "temperature": 0.0, "avg_logprob":
  -0.1451706832714295, "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0006754028145223856},
  {"id": 363, "seek": 221496, "start": 2223.36, "end": 2229.2, "text": " And particular,
  one of the things that the swirl adaptive query processor does is it rewrites",
  "tokens": [50784, 400, 1729, 11, 472, 295, 264, 721, 300, 264, 30310, 27912, 14581,
  15321, 775, 307, 309, 319, 86, 30931, 51076], "temperature": 0.0, "avg_logprob":
  -0.1451706832714295, "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0006754028145223856},
  {"id": 364, "seek": 221496, "start": 2229.2, "end": 2237.04, "text": " this query.
  Most repositories will get the search electric vehicle Tesla with the company tag
  removed.", "tokens": [51076, 341, 14581, 13, 4534, 22283, 2083, 486, 483, 264, 3164,
  5210, 5864, 13666, 365, 264, 2237, 6162, 7261, 13, 51468], "temperature": 0.0, "avg_logprob":
  -0.1451706832714295, "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0006754028145223856},
  {"id": 365, "seek": 221496, "start": 2237.04, "end": 2243.52, "text": " However,
  the company funding database in BigQuery, which I just fixed, will actually only
  get the", "tokens": [51468, 2908, 11, 264, 2237, 6137, 8149, 294, 43422, 11, 597,
  286, 445, 6806, 11, 486, 767, 787, 483, 264, 51792], "temperature": 0.0, "avg_logprob":
  -0.1451706832714295, "compression_ratio": 1.58130081300813, "no_speech_prob": 0.0006754028145223856},
  {"id": 366, "seek": 224352, "start": 2243.52, "end": 2249.92, "text": " query Tesla.
  So if we now look at the results, you know, we''ll see fairly traditional high quality",
  "tokens": [50364, 14581, 13666, 13, 407, 498, 321, 586, 574, 412, 264, 3542, 11,
  291, 458, 11, 321, 603, 536, 6457, 5164, 1090, 3125, 50684], "temperature": 0.0,
  "avg_logprob": -0.09529762268066407, "compression_ratio": 1.5502008032128514, "no_speech_prob":
  0.0003635244211181998}, {"id": 367, "seek": 224352, "start": 2249.92, "end": 2256.96,
  "text": " content here about electric vehicles with Tesla favored early on. So for
  example, it loves this", "tokens": [50684, 2701, 510, 466, 5210, 8948, 365, 13666,
  44420, 2440, 322, 13, 407, 337, 1365, 11, 309, 6752, 341, 51036], "temperature":
  0.0, "avg_logprob": -0.09529762268066407, "compression_ratio": 1.5502008032128514,
  "no_speech_prob": 0.0003635244211181998}, {"id": 368, "seek": 224352, "start": 2256.96,
  "end": 2262.8, "text": " hit with Tesla right at the beginning of the body. Most
  of these, I think are pretty good hits.", "tokens": [51036, 2045, 365, 13666, 558,
  412, 264, 2863, 295, 264, 1772, 13, 4534, 295, 613, 11, 286, 519, 366, 1238, 665,
  8664, 13, 51328], "temperature": 0.0, "avg_logprob": -0.09529762268066407, "compression_ratio":
  1.5502008032128514, "no_speech_prob": 0.0003635244211181998}, {"id": 369, "seek":
  224352, "start": 2262.8, "end": 2268.16, "text": " And here, here''s a database
  hit. This is from BigQuery. It''s a company funding record. So Tesla", "tokens":
  [51328, 400, 510, 11, 510, 311, 257, 8149, 2045, 13, 639, 307, 490, 43422, 13, 467,
  311, 257, 2237, 6137, 2136, 13, 407, 13666, 51596], "temperature": 0.0, "avg_logprob":
  -0.09529762268066407, "compression_ratio": 1.5502008032128514, "no_speech_prob":
  0.0003635244211181998}, {"id": 370, "seek": 226816, "start": 2268.16, "end": 2276.64,
  "text": " Motors raised a large series C back in 2006. This is an old database of
  funding records from Kaggle.", "tokens": [50364, 40118, 6005, 257, 2416, 2638, 383,
  646, 294, 14062, 13, 639, 307, 364, 1331, 8149, 295, 6137, 7724, 490, 48751, 22631,
  13, 50788], "temperature": 0.0, "avg_logprob": -0.14827345477210152, "compression_ratio":
  1.4333333333333333, "no_speech_prob": 0.018362978473305702}, {"id": 371, "seek":
  226816, "start": 2277.44, "end": 2284.7999999999997, "text": " Now, a couple of
  things I want to point out on the fly swirl allows you to turn a database record
  into", "tokens": [50828, 823, 11, 257, 1916, 295, 721, 286, 528, 281, 935, 484,
  322, 264, 3603, 30310, 4045, 291, 281, 1261, 257, 8149, 2136, 666, 51196], "temperature":
  0.0, "avg_logprob": -0.14827345477210152, "compression_ratio": 1.4333333333333333,
  "no_speech_prob": 0.018362978473305702}, {"id": 372, "seek": 226816, "start": 2284.7999999999997,
  "end": 2292.48, "text": " a sort of pseudo document. You can actually just write
  this as a Python expression and use braces", "tokens": [51196, 257, 1333, 295, 35899,
  4166, 13, 509, 393, 767, 445, 2464, 341, 382, 257, 15329, 6114, 293, 764, 41537,
  51580], "temperature": 0.0, "avg_logprob": -0.14827345477210152, "compression_ratio":
  1.4333333333333333, "no_speech_prob": 0.018362978473305702}, {"id": 373, "seek":
  229248, "start": 2292.48, "end": 2299.44, "text": " to refer to the fields. And
  I''ll show that in a second. In addition, though, swirl has a fixed", "tokens":
  [50364, 281, 2864, 281, 264, 7909, 13, 400, 286, 603, 855, 300, 294, 257, 1150,
  13, 682, 4500, 11, 1673, 11, 30310, 575, 257, 6806, 50712], "temperature": 0.0,
  "avg_logprob": -0.1593510945638021, "compression_ratio": 1.7035714285714285, "no_speech_prob":
  0.0703338086605072}, {"id": 374, "seek": 229248, "start": 2299.44, "end": 2305.68,
  "text": " schema URL title, body date published date retrieved and author, but it
  also has a payload field.", "tokens": [50712, 34078, 12905, 4876, 11, 1772, 4002,
  6572, 4002, 19817, 937, 293, 3793, 11, 457, 309, 611, 575, 257, 30918, 2519, 13,
  51024], "temperature": 0.0, "avg_logprob": -0.1593510945638021, "compression_ratio":
  1.7035714285714285, "no_speech_prob": 0.0703338086605072}, {"id": 375, "seek": 229248,
  "start": 2305.68, "end": 2310.72, "text": " The payload field can hold anything.
  And by default, anything that you don''t specify for mapping", "tokens": [51024,
  440, 30918, 2519, 393, 1797, 1340, 13, 400, 538, 7576, 11, 1340, 300, 291, 500,
  380, 16500, 337, 18350, 51276], "temperature": 0.0, "avg_logprob": -0.1593510945638021,
  "compression_ratio": 1.7035714285714285, "no_speech_prob": 0.0703338086605072},
  {"id": 376, "seek": 229248, "start": 2310.72, "end": 2314.96, "text": " goes into
  the payload. You can also say, please don''t put anything in the payload. So here,",
  "tokens": [51276, 1709, 666, 264, 30918, 13, 509, 393, 611, 584, 11, 1767, 500,
  380, 829, 1340, 294, 264, 30918, 13, 407, 510, 11, 51488], "temperature": 0.0, "avg_logprob":
  -0.1593510945638021, "compression_ratio": 1.7035714285714285, "no_speech_prob":
  0.0703338086605072}, {"id": 377, "seek": 229248, "start": 2314.96, "end": 2320.4,
  "text": " the fields are also repeated, right? As data items so that if I want,
  did I could extract those", "tokens": [51488, 264, 7909, 366, 611, 10477, 11, 558,
  30, 1018, 1412, 4754, 370, 300, 498, 286, 528, 11, 630, 286, 727, 8947, 729, 51760],
  "temperature": 0.0, "avg_logprob": -0.1593510945638021, "compression_ratio": 1.7035714285714285,
  "no_speech_prob": 0.0703338086605072}, {"id": 378, "seek": 232040, "start": 2320.4,
  "end": 2325.76, "text": " individually? And the idea here is you have a normalized
  record that reflects the sort of", "tokens": [50364, 16652, 30, 400, 264, 1558,
  510, 307, 291, 362, 257, 48704, 2136, 300, 18926, 264, 1333, 295, 50632], "temperature":
  0.0, "avg_logprob": -0.12956732717053643, "compression_ratio": 1.6305084745762712,
  "no_speech_prob": 0.003615084569901228}, {"id": 379, "seek": 232040, "start": 2325.76,
  "end": 2330.56, "text": " top relevancy items. So you know whether or not you should
  go deeper. And then the payload will", "tokens": [50632, 1192, 25916, 6717, 4754,
  13, 407, 291, 458, 1968, 420, 406, 291, 820, 352, 7731, 13, 400, 550, 264, 30918,
  486, 50872], "temperature": 0.0, "avg_logprob": -0.12956732717053643, "compression_ratio":
  1.6305084745762712, "no_speech_prob": 0.003615084569901228}, {"id": 380, "seek":
  232040, "start": 2330.56, "end": 2335.36, "text": " have anything extra that you
  might need to make that decision. So for example, if we look a little", "tokens":
  [50872, 362, 1340, 2857, 300, 291, 1062, 643, 281, 652, 300, 3537, 13, 407, 337,
  1365, 11, 498, 321, 574, 257, 707, 51112], "temperature": 0.0, "avg_logprob": -0.12956732717053643,
  "compression_ratio": 1.6305084745762712, "no_speech_prob": 0.003615084569901228},
  {"id": 381, "seek": 232040, "start": 2335.36, "end": 2341.92, "text": " further
  down, here''s a result from NLresearch.com. Northern Light, the same company I started
  while", "tokens": [51112, 3052, 760, 11, 510, 311, 257, 1874, 490, 426, 43, 49838,
  1178, 13, 1112, 13, 14335, 8279, 11, 264, 912, 2237, 286, 1409, 1339, 51440], "temperature":
  0.0, "avg_logprob": -0.12956732717053643, "compression_ratio": 1.6305084745762712,
  "no_speech_prob": 0.003615084569901228}, {"id": 382, "seek": 232040, "start": 2341.92,
  "end": 2346.08, "text": " working on search, or I learned a lot about search at
  was really the first company I worked for.", "tokens": [51440, 1364, 322, 3164,
  11, 420, 286, 3264, 257, 688, 466, 3164, 412, 390, 534, 264, 700, 2237, 286, 2732,
  337, 13, 51648], "temperature": 0.0, "avg_logprob": -0.12956732717053643, "compression_ratio":
  1.6305084745762712, "no_speech_prob": 0.003615084569901228}, {"id": 383, "seek":
  234608, "start": 2346.08, "end": 2351.92, "text": " Still going strong. One of the
  things they do is extract super high quality news from the web.", "tokens": [50364,
  8291, 516, 2068, 13, 1485, 295, 264, 721, 436, 360, 307, 8947, 1687, 1090, 3125,
  2583, 490, 264, 3670, 13, 50656], "temperature": 0.0, "avg_logprob": -0.12547557374351045,
  "compression_ratio": 1.6793103448275861, "no_speech_prob": 0.0012360269902274013},
  {"id": 384, "seek": 234608, "start": 2351.92, "end": 2357.36, "text": " And they
  field it and they classify it and can really do rich searching. So here is an article",
  "tokens": [50656, 400, 436, 2519, 309, 293, 436, 33872, 309, 293, 393, 534, 360,
  4593, 10808, 13, 407, 510, 307, 364, 7222, 50928], "temperature": 0.0, "avg_logprob":
  -0.12547557374351045, "compression_ratio": 1.6793103448275861, "no_speech_prob":
  0.0012360269902274013}, {"id": 385, "seek": 234608, "start": 2357.36, "end": 2363.2,
  "text": " that they pulled together about, you know, basically it''s not so much
  about the electric vehicle market.", "tokens": [50928, 300, 436, 7373, 1214, 466,
  11, 291, 458, 11, 1936, 309, 311, 406, 370, 709, 466, 264, 5210, 5864, 2142, 13,
  51220], "temperature": 0.0, "avg_logprob": -0.12547557374351045, "compression_ratio":
  1.6793103448275861, "no_speech_prob": 0.0012360269902274013}, {"id": 386, "seek":
  234608, "start": 2363.2, "end": 2366.4, "text": " It''s about Tesla. So it ranked
  a little bit lower. In this case, there were some other ones that", "tokens": [51220,
  467, 311, 466, 13666, 13, 407, 309, 20197, 257, 707, 857, 3126, 13, 682, 341, 1389,
  11, 456, 645, 512, 661, 2306, 300, 51380], "temperature": 0.0, "avg_logprob": -0.12547557374351045,
  "compression_ratio": 1.6793103448275861, "no_speech_prob": 0.0012360269902274013},
  {"id": 387, "seek": 234608, "start": 2366.4, "end": 2371.12, "text": " ranked higher.
  They have some nice data that we like to capture and put in the payload as well.",
  "tokens": [51380, 20197, 2946, 13, 814, 362, 512, 1481, 1412, 300, 321, 411, 281,
  7983, 293, 829, 294, 264, 30918, 382, 731, 13, 51616], "temperature": 0.0, "avg_logprob":
  -0.12547557374351045, "compression_ratio": 1.6793103448275861, "no_speech_prob":
  0.0012360269902274013}, {"id": 388, "seek": 237112, "start": 2371.68, "end": 2378.64,
  "text": " So this really is the core of swirl. And you say it has things like facets.
  For example,", "tokens": [50392, 407, 341, 534, 307, 264, 4965, 295, 30310, 13,
  400, 291, 584, 309, 575, 721, 411, 49752, 13, 1171, 1365, 11, 50740], "temperature":
  0.0, "avg_logprob": -0.2449361589219835, "compression_ratio": 1.5480769230769231,
  "no_speech_prob": 0.00207709101960063}, {"id": 389, "seek": 237112, "start": 2378.64,
  "end": 2386.16, "text": " we use U-track internally to track issues. So if I want
  to, you know, just switch to those,", "tokens": [50740, 321, 764, 624, 12, 19466,
  19501, 281, 2837, 2663, 13, 407, 498, 286, 528, 281, 11, 291, 458, 11, 445, 3679,
  281, 729, 11, 51116], "temperature": 0.0, "avg_logprob": -0.2449361589219835, "compression_ratio":
  1.5480769230769231, "no_speech_prob": 0.00207709101960063}, {"id": 390, "seek":
  237112, "start": 2386.16, "end": 2394.3199999999997, "text": " it''ll bring just
  those up. Oh, looks like I pooped on that one. Another thing you can do when you''re",
  "tokens": [51116, 309, 603, 1565, 445, 729, 493, 13, 876, 11, 1542, 411, 286, 17153,
  292, 322, 300, 472, 13, 3996, 551, 291, 393, 360, 562, 291, 434, 51524], "temperature":
  0.0, "avg_logprob": -0.2449361589219835, "compression_ratio": 1.5480769230769231,
  "no_speech_prob": 0.00207709101960063}, {"id": 391, "seek": 237112, "start": 2394.3199999999997,
  "end": 2398.08, "text": " running, oops, looks like just a second.", "tokens": [51524,
  2614, 11, 34166, 11, 1542, 411, 445, 257, 1150, 13, 51712], "temperature": 0.0,
  "avg_logprob": -0.2449361589219835, "compression_ratio": 1.5480769230769231, "no_speech_prob":
  0.00207709101960063}, {"id": 392, "seek": 240112, "start": 2401.3599999999997, "end":
  2413.2, "text": " Another thing you can do, we have the concept of mixers. Not for
  drinks, but for results.", "tokens": [50376, 3996, 551, 291, 393, 360, 11, 321,
  362, 264, 3410, 295, 2890, 433, 13, 1726, 337, 12142, 11, 457, 337, 3542, 13, 50968],
  "temperature": 0.0, "avg_logprob": -0.16944787940200495, "compression_ratio": 1.6403508771929824,
  "no_speech_prob": 0.0036291347350925207}, {"id": 393, "seek": 240112, "start": 2413.7599999999998,
  "end": 2418.64, "text": " You can mix the results up by default. We do it by relevancy,
  but you can specify different", "tokens": [50996, 509, 393, 2890, 264, 3542, 493,
  538, 7576, 13, 492, 360, 309, 538, 25916, 6717, 11, 457, 291, 393, 16500, 819, 51240],
  "temperature": 0.0, "avg_logprob": -0.16944787940200495, "compression_ratio": 1.6403508771929824,
  "no_speech_prob": 0.0036291347350925207}, {"id": 394, "seek": 240112, "start": 2418.64,
  "end": 2424.64, "text": " mixers. For example, the date mixer will focus on it.
  Well, date sorted and it hides anything", "tokens": [51240, 2890, 433, 13, 1171,
  1365, 11, 264, 4002, 24063, 486, 1879, 322, 309, 13, 1042, 11, 4002, 25462, 293,
  309, 35953, 1340, 51540], "temperature": 0.0, "avg_logprob": -0.16944787940200495,
  "compression_ratio": 1.6403508771929824, "no_speech_prob": 0.0036291347350925207},
  {"id": 395, "seek": 240112, "start": 2424.64, "end": 2429.68, "text": " that doesn''t
  have a date published. The round robin mixer, on the other hand, still sort of honors",
  "tokens": [51540, 300, 1177, 380, 362, 257, 4002, 6572, 13, 440, 3098, 3870, 259,
  24063, 11, 322, 264, 661, 1011, 11, 920, 1333, 295, 26884, 51792], "temperature":
  0.0, "avg_logprob": -0.16944787940200495, "compression_ratio": 1.6403508771929824,
  "no_speech_prob": 0.0036291347350925207}, {"id": 396, "seek": 242968, "start": 2429.68,
  "end": 2436.56, "text": " relevancy, but it just takes one from each result. So
  you get a cross section of the results.", "tokens": [50364, 25916, 6717, 11, 457,
  309, 445, 2516, 472, 490, 1184, 1874, 13, 407, 291, 483, 257, 3278, 3541, 295, 264,
  3542, 13, 50708], "temperature": 0.0, "avg_logprob": -0.08485564407037229, "compression_ratio":
  1.740909090909091, "no_speech_prob": 0.003491308307275176}, {"id": 397, "seek":
  242968, "start": 2436.56, "end": 2442.3199999999997, "text": " So here, for example,
  you know, just looking at the top five, one result, the best result from", "tokens":
  [50708, 407, 510, 11, 337, 1365, 11, 291, 458, 11, 445, 1237, 412, 264, 1192, 1732,
  11, 472, 1874, 11, 264, 1151, 1874, 490, 50996], "temperature": 0.0, "avg_logprob":
  -0.08485564407037229, "compression_ratio": 1.740909090909091, "no_speech_prob":
  0.003491308307275176}, {"id": 398, "seek": 242968, "start": 2442.3199999999997,
  "end": 2448.3999999999996, "text": " each silo right here at the top. And of course,
  here I''m arguing a little bit about the relevancy", "tokens": [50996, 1184, 3425,
  78, 558, 510, 412, 264, 1192, 13, 400, 295, 1164, 11, 510, 286, 478, 19697, 257,
  707, 857, 466, 264, 25916, 6717, 51300], "temperature": 0.0, "avg_logprob": -0.08485564407037229,
  "compression_ratio": 1.740909090909091, "no_speech_prob": 0.003491308307275176},
  {"id": 399, "seek": 242968, "start": 2448.3999999999996, "end": 2452.16, "text":
  " of this right in one of our support tickets. So you see everything kind of just
  brought together", "tokens": [51300, 295, 341, 558, 294, 472, 295, 527, 1406, 12628,
  13, 407, 291, 536, 1203, 733, 295, 445, 3038, 1214, 51488], "temperature": 0.0,
  "avg_logprob": -0.08485564407037229, "compression_ratio": 1.740909090909091, "no_speech_prob":
  0.003491308307275176}, {"id": 400, "seek": 245216, "start": 2452.24, "end": 2454.72,
  "text": " for me and I can decide which things I might like to do.", "tokens": [50368,
  337, 385, 293, 286, 393, 4536, 597, 721, 286, 1062, 411, 281, 360, 13, 50492], "temperature":
  0.0, "avg_logprob": -0.1923727035522461, "compression_ratio": 1.715481171548117,
  "no_speech_prob": 0.15056148171424866}, {"id": 401, "seek": 245216, "start": 2457.2,
  "end": 2463.2799999999997, "text": " Yeah, maybe it could, I mean, I''m just commenting
  as we go, but maybe visually it could also show", "tokens": [50616, 865, 11, 1310,
  309, 727, 11, 286, 914, 11, 286, 478, 445, 29590, 382, 321, 352, 11, 457, 1310,
  19622, 309, 727, 611, 855, 50920], "temperature": 0.0, "avg_logprob": -0.1923727035522461,
  "compression_ratio": 1.715481171548117, "no_speech_prob": 0.15056148171424866},
  {"id": 402, "seek": 245216, "start": 2463.2799999999997, "end": 2467.3599999999997,
  "text": " where this comes from, right? Because you do have on the left the sources.",
  "tokens": [50920, 689, 341, 1487, 490, 11, 558, 30, 1436, 291, 360, 362, 322, 264,
  1411, 264, 7139, 13, 51124], "temperature": 0.0, "avg_logprob": -0.1923727035522461,
  "compression_ratio": 1.715481171548117, "no_speech_prob": 0.15056148171424866},
  {"id": 403, "seek": 245216, "start": 2467.92, "end": 2472.3999999999996, "text":
  " Yes. So could actually say this comes from here, this comes from there. But again,",
  "tokens": [51152, 1079, 13, 407, 727, 767, 584, 341, 1487, 490, 510, 11, 341, 1487,
  490, 456, 13, 583, 797, 11, 51376], "temperature": 0.0, "avg_logprob": -0.1923727035522461,
  "compression_ratio": 1.715481171548117, "no_speech_prob": 0.15056148171424866},
  {"id": 404, "seek": 245216, "start": 2472.3999999999996, "end": 2477.2, "text":
  " the combined view is also excellent. It''s just if you needed to know, right?
  If you need to know,", "tokens": [51376, 264, 9354, 1910, 307, 611, 7103, 13, 467,
  311, 445, 498, 291, 2978, 281, 458, 11, 558, 30, 759, 291, 643, 281, 458, 11, 51616],
  "temperature": 0.0, "avg_logprob": -0.1923727035522461, "compression_ratio": 1.715481171548117,
  "no_speech_prob": 0.15056148171424866}, {"id": 405, "seek": 247720, "start": 2477.2,
  "end": 2484.24, "text": " where did I get this from, right? That''s right. So we
  do, we do, we keep the source in the result", "tokens": [50364, 689, 630, 286, 483,
  341, 490, 11, 558, 30, 663, 311, 558, 13, 407, 321, 360, 11, 321, 360, 11, 321,
  1066, 264, 4009, 294, 264, 1874, 50716], "temperature": 0.0, "avg_logprob": -0.14283222016834077,
  "compression_ratio": 1.6493506493506493, "no_speech_prob": 0.008677611127495766},
  {"id": 406, "seek": 247720, "start": 2484.24, "end": 2489.4399999999996, "text":
  " here, along with whoever the source tells us the author is. However, in the in
  this version,", "tokens": [50716, 510, 11, 2051, 365, 11387, 264, 4009, 5112, 505,
  264, 3793, 307, 13, 2908, 11, 294, 264, 294, 341, 3037, 11, 50976], "temperature":
  0.0, "avg_logprob": -0.14283222016834077, "compression_ratio": 1.6493506493506493,
  "no_speech_prob": 0.008677611127495766}, {"id": 407, "seek": 247720, "start": 2489.4399999999996,
  "end": 2494.72, "text": " we didn''t get to it. We like to report the original rank.
  So you should see IT news and I''ll", "tokens": [50976, 321, 994, 380, 483, 281,
  309, 13, 492, 411, 281, 2275, 264, 3380, 6181, 13, 407, 291, 820, 536, 6783, 2583,
  293, 286, 603, 51240], "temperature": 0.0, "avg_logprob": -0.14283222016834077,
  "compression_ratio": 1.6493506493506493, "no_speech_prob": 0.008677611127495766},
  {"id": 408, "seek": 247720, "start": 2494.72, "end": 2500.72, "text": " research
  one here. It''s the number one result in the two point O version. Actually, there''s
  a new", "tokens": [51240, 2132, 472, 510, 13, 467, 311, 264, 1230, 472, 1874, 294,
  264, 732, 935, 422, 3037, 13, 5135, 11, 456, 311, 257, 777, 51540], "temperature":
  0.0, "avg_logprob": -0.14283222016834077, "compression_ratio": 1.6493506493506493,
  "no_speech_prob": 0.008677611127495766}, {"id": 409, "seek": 250072, "start": 2500.72,
  "end": 2506.3999999999996, "text": " version that''s coming out. I think we''re
  going to just do a bug fix on this. The latest version 10.1,", "tokens": [50364,
  3037, 300, 311, 1348, 484, 13, 286, 519, 321, 434, 516, 281, 445, 360, 257, 7426,
  3191, 322, 341, 13, 440, 6792, 3037, 1266, 13, 16, 11, 50648], "temperature": 0.0,
  "avg_logprob": -0.127621134375311, "compression_ratio": 1.6772334293948126, "no_speech_prob":
  0.015672797337174416}, {"id": 410, "seek": 250072, "start": 2507.12, "end": 2510.8799999999997,
  "text": " which is in the repo now, fixes that in a couple other issues. So if you
  just get the newest,", "tokens": [50684, 597, 307, 294, 264, 49040, 586, 11, 32539,
  300, 294, 257, 1916, 661, 2663, 13, 407, 498, 291, 445, 483, 264, 17569, 11, 50872],
  "temperature": 0.0, "avg_logprob": -0.127621134375311, "compression_ratio": 1.6772334293948126,
  "no_speech_prob": 0.015672797337174416}, {"id": 411, "seek": 250072, "start": 2510.8799999999997,
  "end": 2515.2, "text": " you''ll be good. In two point O that we have a little bit
  of a new treatment for this. I think", "tokens": [50872, 291, 603, 312, 665, 13,
  682, 732, 935, 422, 300, 321, 362, 257, 707, 857, 295, 257, 777, 5032, 337, 341,
  13, 286, 519, 51088], "temperature": 0.0, "avg_logprob": -0.127621134375311, "compression_ratio":
  1.6772334293948126, "no_speech_prob": 0.015672797337174416}, {"id": 412, "seek":
  250072, "start": 2515.2, "end": 2520.0, "text": " you''ll like a lot better. But
  before I jump to that, you asked me a really important question.", "tokens": [51088,
  291, 603, 411, 257, 688, 1101, 13, 583, 949, 286, 3012, 281, 300, 11, 291, 2351,
  385, 257, 534, 1021, 1168, 13, 51328], "temperature": 0.0, "avg_logprob": -0.127621134375311,
  "compression_ratio": 1.6772334293948126, "no_speech_prob": 0.015672797337174416},
  {"id": 413, "seek": 250072, "start": 2520.0, "end": 2525.7599999999998, "text":
  " Right? So how this is great, this UI will evolve. It''s here so that you can show
  the power, right?", "tokens": [51328, 1779, 30, 407, 577, 341, 307, 869, 11, 341,
  15682, 486, 16693, 13, 467, 311, 510, 370, 300, 291, 393, 855, 264, 1347, 11, 558,
  30, 51616], "temperature": 0.0, "avg_logprob": -0.127621134375311, "compression_ratio":
  1.6772334293948126, "no_speech_prob": 0.015672797337174416}, {"id": 414, "seek":
  250072, "start": 2525.7599999999998, "end": 2530.16, "text": " And we ship it integrated.
  But from a developer perspective, none of this is super helpful, right?", "tokens":
  [51616, 400, 321, 5374, 309, 10919, 13, 583, 490, 257, 10754, 4585, 11, 6022, 295,
  341, 307, 1687, 4961, 11, 558, 30, 51836], "temperature": 0.0, "avg_logprob": -0.127621134375311,
  "compression_ratio": 1.6772334293948126, "no_speech_prob": 0.015672797337174416},
  {"id": 415, "seek": 253016, "start": 2530.16, "end": 2534.96, "text": " How do I
  integrate this with an existing UI? So that''s what I really wanted to show you
  next. So", "tokens": [50364, 1012, 360, 286, 13365, 341, 365, 364, 6741, 15682,
  30, 407, 300, 311, 437, 286, 534, 1415, 281, 855, 291, 958, 13, 407, 50604], "temperature":
  0.0, "avg_logprob": -0.10717669866418325, "compression_ratio": 1.6088709677419355,
  "no_speech_prob": 0.0006971502443775535}, {"id": 416, "seek": 253016, "start": 2535.92,
  "end": 2543.6, "text": " first, how do we connect to something? The answer is a
  search provider definition. So this definition", "tokens": [50652, 700, 11, 577,
  360, 321, 1745, 281, 746, 30, 440, 1867, 307, 257, 3164, 12398, 7123, 13, 407, 341,
  7123, 51036], "temperature": 0.0, "avg_logprob": -0.10717669866418325, "compression_ratio":
  1.6088709677419355, "no_speech_prob": 0.0006971502443775535}, {"id": 417, "seek":
  253016, "start": 2543.6, "end": 2550.3999999999996, "text": " right here, this text
  record, mostly JSON, but mostly just strings. This configures are out of the", "tokens":
  [51036, 558, 510, 11, 341, 2487, 2136, 11, 5240, 31828, 11, 457, 5240, 445, 13985,
  13, 639, 6662, 1303, 366, 484, 295, 264, 51376], "temperature": 0.0, "avg_logprob":
  -0.10717669866418325, "compression_ratio": 1.6088709677419355, "no_speech_prob":
  0.0006971502443775535}, {"id": 418, "seek": 253016, "start": 2550.3999999999996,
  "end": 2557.7599999999998, "text": " box request get connector to query a search
  provider, to query in particular this Google programmable", "tokens": [51376, 2424,
  5308, 483, 19127, 281, 14581, 257, 3164, 12398, 11, 281, 14581, 294, 1729, 341,
  3329, 37648, 712, 51744], "temperature": 0.0, "avg_logprob": -0.10717669866418325,
  "compression_ratio": 1.6088709677419355, "no_speech_prob": 0.0006971502443775535},
  {"id": 419, "seek": 255776, "start": 2557.76, "end": 2561.92, "text": " search engine
  that I put together. And actually, we ship with three of them preset and please
  feel", "tokens": [50364, 3164, 2848, 300, 286, 829, 1214, 13, 400, 767, 11, 321,
  5374, 365, 1045, 295, 552, 32081, 293, 1767, 841, 50572], "temperature": 0.0, "avg_logprob":
  -0.12575600147247315, "compression_ratio": 1.591503267973856, "no_speech_prob":
  0.005927330814301968}, {"id": 420, "seek": 255776, "start": 2561.92, "end": 2568.32,
  "text": " free to share our keys. We''re happy we want to make sure that something
  is working for everybody,", "tokens": [50572, 1737, 281, 2073, 527, 9317, 13, 492,
  434, 2055, 321, 528, 281, 652, 988, 300, 746, 307, 1364, 337, 2201, 11, 50892],
  "temperature": 0.0, "avg_logprob": -0.12575600147247315, "compression_ratio": 1.591503267973856,
  "no_speech_prob": 0.005927330814301968}, {"id": 421, "seek": 255776, "start": 2568.32,
  "end": 2575.2000000000003, "text": " right? Out of the box. So further in this,
  are the things you''d expect? You can configure this with", "tokens": [50892, 558,
  30, 5925, 295, 264, 2424, 13, 407, 3052, 294, 341, 11, 366, 264, 721, 291, 1116,
  2066, 30, 509, 393, 22162, 341, 365, 51236], "temperature": 0.0, "avg_logprob":
  -0.12575600147247315, "compression_ratio": 1.591503267973856, "no_speech_prob":
  0.005927330814301968}, {"id": 422, "seek": 255776, "start": 2575.2000000000003,
  "end": 2581.44, "text": " by providing a URL. You can construct the URL by pulling
  in fields from the query mappings.", "tokens": [51236, 538, 6530, 257, 12905, 13,
  509, 393, 7690, 264, 12905, 538, 8407, 294, 7909, 490, 264, 14581, 463, 28968, 13,
  51548], "temperature": 0.0, "avg_logprob": -0.12575600147247315, "compression_ratio":
  1.591503267973856, "no_speech_prob": 0.005927330814301968}, {"id": 423, "seek":
  255776, "start": 2581.44, "end": 2586.1600000000003, "text": " So the only thing
  that ever really changes in a Google PSC is the CX code. Everything else you can",
  "tokens": [51548, 407, 264, 787, 551, 300, 1562, 534, 2962, 294, 257, 3329, 8168,
  34, 307, 264, 383, 55, 3089, 13, 5471, 1646, 291, 393, 51784], "temperature": 0.0,
  "avg_logprob": -0.12575600147247315, "compression_ratio": 1.591503267973856, "no_speech_prob":
  0.005927330814301968}, {"id": 424, "seek": 258616, "start": 2586.16, "end": 2592.16,
  "text": " just copy and paste. You can put dozens of them in. Also here are some
  of the important system", "tokens": [50364, 445, 5055, 293, 9163, 13, 509, 393,
  829, 18431, 295, 552, 294, 13, 2743, 510, 366, 512, 295, 264, 1021, 1185, 50664],
  "temperature": 0.0, "avg_logprob": -0.13341502256171647, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.00013744051102548838}, {"id": 425, "seek": 258616, "start":
  2592.16, "end": 2599.52, "text": " things that help the system work, help us process
  this. So we have four different processing", "tokens": [50664, 721, 300, 854, 264,
  1185, 589, 11, 854, 505, 1399, 341, 13, 407, 321, 362, 1451, 819, 9007, 51032],
  "temperature": 0.0, "avg_logprob": -0.13341502256171647, "compression_ratio": 1.6363636363636365,
  "no_speech_prob": 0.00013744051102548838}, {"id": 426, "seek": 258616, "start":
  2599.52, "end": 2605.2, "text": " pipelines built into Swirl. One is a prequery
  that runs before Federation. And then there''s a", "tokens": [51032, 40168, 3094,
  666, 3926, 1648, 13, 1485, 307, 257, 659, 358, 2109, 300, 6676, 949, 27237, 13,
  400, 550, 456, 311, 257, 51316], "temperature": 0.0, "avg_logprob": -0.13341502256171647,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.00013744051102548838},
  {"id": 427, "seek": 258616, "start": 2606.3199999999997, "end": 2610.96, "text":
  " query processing pipeline that runs for each connector or actually actually say
  search provider,", "tokens": [51372, 14581, 9007, 15517, 300, 6676, 337, 1184, 19127,
  420, 767, 767, 584, 3164, 12398, 11, 51604], "temperature": 0.0, "avg_logprob":
  -0.13341502256171647, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.00013744051102548838}, {"id": 428, "seek": 261096, "start": 2610.96, "end": 2617.04,
  "text": " which is an instance, a configured instance of a connector. Then each
  of those also has a", "tokens": [50364, 597, 307, 364, 5197, 11, 257, 30538, 5197,
  295, 257, 19127, 13, 1396, 1184, 295, 729, 611, 575, 257, 50668], "temperature":
  0.0, "avg_logprob": -0.09814239216742114, "compression_ratio": 1.7418181818181817,
  "no_speech_prob": 0.0004108204448129982}, {"id": 429, "seek": 261096, "start": 2617.04,
  "end": 2621.84, "text": " result processing pipeline, which transforms the results
  from the source into our normalized", "tokens": [50668, 1874, 9007, 15517, 11, 597,
  35592, 264, 3542, 490, 264, 4009, 666, 527, 48704, 50908], "temperature": 0.0, "avg_logprob":
  -0.09814239216742114, "compression_ratio": 1.7418181818181817, "no_speech_prob":
  0.0004108204448129982}, {"id": 430, "seek": 261096, "start": 2621.84, "end": 2626.16,
  "text": " format. And then there''s a post result processing that does things like
  relevancy ranking where you", "tokens": [50908, 7877, 13, 400, 550, 456, 311, 257,
  2183, 1874, 9007, 300, 775, 721, 411, 25916, 6717, 17833, 689, 291, 51124], "temperature":
  0.0, "avg_logprob": -0.09814239216742114, "compression_ratio": 1.7418181818181817,
  "no_speech_prob": 0.0004108204448129982}, {"id": 431, "seek": 261096, "start": 2626.16,
  "end": 2631.44, "text": " want all of the data. And they''re all different. By the
  way, there''s an object model behind Swirl. So", "tokens": [51124, 528, 439, 295,
  264, 1412, 13, 400, 436, 434, 439, 819, 13, 3146, 264, 636, 11, 456, 311, 364, 2657,
  2316, 2261, 3926, 1648, 13, 407, 51388], "temperature": 0.0, "avg_logprob": -0.09814239216742114,
  "compression_ratio": 1.7418181818181817, "no_speech_prob": 0.0004108204448129982},
  {"id": 432, "seek": 261096, "start": 2631.44, "end": 2636.08, "text": " grading
  these things is really simple. There are different base classes for those and they
  set", "tokens": [51388, 35540, 613, 721, 307, 534, 2199, 13, 821, 366, 819, 3096,
  5359, 337, 729, 293, 436, 992, 51620], "temperature": 0.0, "avg_logprob": -0.09814239216742114,
  "compression_ratio": 1.7418181818181817, "no_speech_prob": 0.0004108204448129982},
  {"id": 433, "seek": 263608, "start": 2636.16, "end": 2641.92, "text": " you up with
  everything you need. So essentially you come in, you have a Python model or I should
  say", "tokens": [50368, 291, 493, 365, 1203, 291, 643, 13, 407, 4476, 291, 808,
  294, 11, 291, 362, 257, 15329, 2316, 420, 286, 820, 584, 50656], "temperature":
  0.0, "avg_logprob": -0.12926271646329673, "compression_ratio": 1.5515873015873016,
  "no_speech_prob": 0.002594432793557644}, {"id": 434, "seek": 263608, "start": 2641.92,
  "end": 2645.92, "text": " a Django model object to operate on. All you have to do
  is change it and exit and you''re done.", "tokens": [50656, 257, 33464, 17150, 2316,
  2657, 281, 9651, 322, 13, 1057, 291, 362, 281, 360, 307, 1319, 309, 293, 11043,
  293, 291, 434, 1096, 13, 50856], "temperature": 0.0, "avg_logprob": -0.12926271646329673,
  "compression_ratio": 1.5515873015873016, "no_speech_prob": 0.002594432793557644},
  {"id": 435, "seek": 263608, "start": 2646.48, "end": 2654.3199999999997, "text":
  " Simple, simple. Also, we map out the different query capabilities of each provider
  in the query", "tokens": [50884, 21532, 11, 2199, 13, 2743, 11, 321, 4471, 484,
  264, 819, 14581, 10862, 295, 1184, 12398, 294, 264, 14581, 51276], "temperature":
  0.0, "avg_logprob": -0.12926271646329673, "compression_ratio": 1.5515873015873016,
  "no_speech_prob": 0.002594432793557644}, {"id": 436, "seek": 263608, "start": 2654.3199999999997,
  "end": 2660.56, "text": " mappings. So how do you tell a given endpoint to sort
  by date? This is how you add this to the URL.", "tokens": [51276, 463, 28968, 13,
  407, 577, 360, 291, 980, 257, 2212, 35795, 281, 1333, 538, 4002, 30, 639, 307, 577,
  291, 909, 341, 281, 264, 12905, 13, 51588], "temperature": 0.0, "avg_logprob": -0.12926271646329673,
  "compression_ratio": 1.5515873015873016, "no_speech_prob": 0.002594432793557644},
  {"id": 437, "seek": 266056, "start": 2660.56, "end": 2668.32, "text": " How do you
  page the results? This is how. Result index is a Swirl capability where we can provide
  you", "tokens": [50364, 1012, 360, 291, 3028, 264, 3542, 30, 639, 307, 577, 13,
  5015, 723, 8186, 307, 257, 3926, 1648, 13759, 689, 321, 393, 2893, 291, 50752],
  "temperature": 0.0, "avg_logprob": -0.16142276417125356, "compression_ratio": 1.7841409691629957,
  "no_speech_prob": 0.0010711950017139316}, {"id": 438, "seek": 266056, "start": 2668.32,
  "end": 2674.48, "text": " with the index number. You can also use result page. So
  the count or the page that you want. And here''s", "tokens": [50752, 365, 264, 8186,
  1230, 13, 509, 393, 611, 764, 1874, 3028, 13, 407, 264, 1207, 420, 264, 3028, 300,
  291, 528, 13, 400, 510, 311, 51060], "temperature": 0.0, "avg_logprob": -0.16142276417125356,
  "compression_ratio": 1.7841409691629957, "no_speech_prob": 0.0010711950017139316},
  {"id": 439, "seek": 266056, "start": 2674.48, "end": 2680.88, "text": " an important
  one too, the not character. So do the silo support not as a term. This one doesn''t.",
  "tokens": [51060, 364, 1021, 472, 886, 11, 264, 406, 2517, 13, 407, 360, 264, 3425,
  78, 1406, 406, 382, 257, 1433, 13, 639, 472, 1177, 380, 13, 51380], "temperature":
  0.0, "avg_logprob": -0.16142276417125356, "compression_ratio": 1.7841409691629957,
  "no_speech_prob": 0.0010711950017139316}, {"id": 440, "seek": 266056, "start": 2681.44,
  "end": 2687.92, "text": " It does not support not as a term. But it supports the
  not character. So as an example, now if I go to", "tokens": [51408, 467, 775, 406,
  1406, 406, 382, 257, 1433, 13, 583, 309, 9346, 264, 406, 2517, 13, 407, 382, 364,
  1365, 11, 586, 498, 286, 352, 281, 51732], "temperature": 0.0, "avg_logprob": -0.16142276417125356,
  "compression_ratio": 1.7841409691629957, "no_speech_prob": 0.0010711950017139316},
  {"id": 441, "seek": 268792, "start": 2687.92, "end": 2692.2400000000002, "text":
  " the search object, I can run a search. I''ll run it for knowledge management.",
  "tokens": [50364, 264, 3164, 2657, 11, 286, 393, 1190, 257, 3164, 13, 286, 603,
  1190, 309, 337, 3601, 4592, 13, 50580], "temperature": 0.0, "avg_logprob": -0.20566890003916982,
  "compression_ratio": 1.5137614678899083, "no_speech_prob": 0.001280047930777073},
  {"id": 442, "seek": 268792, "start": 2695.92, "end": 2699.44, "text": " So actually,
  I''ll just let that one run for a second.", "tokens": [50764, 407, 767, 11, 286,
  603, 445, 718, 300, 472, 1190, 337, 257, 1150, 13, 50940], "temperature": 0.0, "avg_logprob":
  -0.20566890003916982, "compression_ratio": 1.5137614678899083, "no_speech_prob":
  0.001280047930777073}, {"id": 443, "seek": 268792, "start": 2703.36, "end": 2709.6800000000003,
  "text": " There we go. I got my chat. I have the wrong chat GPT API key. But that''s
  okay. Everybody knows", "tokens": [51136, 821, 321, 352, 13, 286, 658, 452, 5081,
  13, 286, 362, 264, 2085, 5081, 26039, 51, 9362, 2141, 13, 583, 300, 311, 1392, 13,
  7646, 3255, 51452], "temperature": 0.0, "avg_logprob": -0.20566890003916982, "compression_ratio":
  1.5137614678899083, "no_speech_prob": 0.001280047930777073}, {"id": 444, "seek":
  268792, "start": 2709.6800000000003, "end": 2716.4, "text": " what we would say
  about this stuff. So actually the query I really want to do is Elon Musk not Twitter.",
  "tokens": [51452, 437, 321, 576, 584, 466, 341, 1507, 13, 407, 767, 264, 14581,
  286, 534, 528, 281, 360, 307, 28498, 26019, 406, 5794, 13, 51788], "temperature":
  0.0, "avg_logprob": -0.20566890003916982, "compression_ratio": 1.5137614678899083,
  "no_speech_prob": 0.001280047930777073}, {"id": 445, "seek": 271640, "start": 2716.48,
  "end": 2722.08, "text": " So perfectly legitimate query, right? What''s going on
  in Elon Musk''s world that''s not related to Twitter?", "tokens": [50368, 407, 6239,
  17956, 14581, 11, 558, 30, 708, 311, 516, 322, 294, 28498, 26019, 311, 1002, 300,
  311, 406, 4077, 281, 5794, 30, 50648], "temperature": 0.0, "avg_logprob": -0.2309645784312281,
  "compression_ratio": 1.5875912408759123, "no_speech_prob": 0.0017051455797627568},
  {"id": 446, "seek": 271640, "start": 2722.4, "end": 2728.96, "text": " Now here''s
  the thing. Google PSC will not understand that query. Everybody says what Google
  doesn''t understand,", "tokens": [50664, 823, 510, 311, 264, 551, 13, 3329, 8168,
  34, 486, 406, 1223, 300, 14581, 13, 7646, 1619, 437, 3329, 1177, 380, 1223, 11,
  50992], "temperature": 0.0, "avg_logprob": -0.2309645784312281, "compression_ratio":
  1.5875912408759123, "no_speech_prob": 0.0017051455797627568}, {"id": 447, "seek":
  271640, "start": 2728.96, "end": 2734.48, "text": " not no web Google does, but
  Google programmable search engine does not honor or not. And in fact,", "tokens":
  [50992, 406, 572, 3670, 3329, 775, 11, 457, 3329, 37648, 712, 3164, 2848, 775, 406,
  5968, 420, 406, 13, 400, 294, 1186, 11, 51268], "temperature": 0.0, "avg_logprob":
  -0.2309645784312281, "compression_ratio": 1.5875912408759123, "no_speech_prob":
  0.0017051455797627568}, {"id": 448, "seek": 271640, "start": 2734.48, "end": 2736.96,
  "text": " just to prove it, PSC.google.com.", "tokens": [51268, 445, 281, 7081,
  309, 11, 8168, 34, 13, 1571, 3127, 13, 1112, 13, 51392], "temperature": 0.0, "avg_logprob":
  -0.2309645784312281, "compression_ratio": 1.5875912408759123, "no_speech_prob":
  0.0017051455797627568}, {"id": 449, "seek": 271640, "start": 2739.12, "end": 2744.56,
  "text": " By the way, before I talk to you, I didn''t know of this system existence
  myself, PSC.", "tokens": [51500, 3146, 264, 636, 11, 949, 286, 751, 281, 291, 11,
  286, 994, 380, 458, 295, 341, 1185, 9123, 2059, 11, 8168, 34, 13, 51772], "temperature":
  0.0, "avg_logprob": -0.2309645784312281, "compression_ratio": 1.5875912408759123,
  "no_speech_prob": 0.0017051455797627568}, {"id": 450, "seek": 274456, "start": 2745.44,
  "end": 2750.56, "text": " Oh my gosh. For web slicing up the web, it is incredible.
  I mean, it takes two seconds to build it,", "tokens": [50408, 876, 452, 6502, 13,
  1171, 3670, 46586, 493, 264, 3670, 11, 309, 307, 4651, 13, 286, 914, 11, 309, 2516,
  732, 3949, 281, 1322, 309, 11, 50664], "temperature": 0.0, "avg_logprob": -0.14057522349887425,
  "compression_ratio": 1.5296442687747036, "no_speech_prob": 0.003534645540639758},
  {"id": 451, "seek": 274456, "start": 2750.56, "end": 2756.96, "text": " right? So
  and you just give it examples. So here''s the thing. You can go, here''s the public
  URL for", "tokens": [50664, 558, 30, 407, 293, 291, 445, 976, 309, 5110, 13, 407,
  510, 311, 264, 551, 13, 509, 393, 352, 11, 510, 311, 264, 1908, 12905, 337, 50984],
  "temperature": 0.0, "avg_logprob": -0.14057522349887425, "compression_ratio": 1.5296442687747036,
  "no_speech_prob": 0.003534645540639758}, {"id": 452, "seek": 274456, "start": 2756.96,
  "end": 2761.92, "text": " one of the programmable search engines I put in and I''ll
  do the same exact query. Elon Musk.", "tokens": [50984, 472, 295, 264, 37648, 712,
  3164, 12982, 286, 829, 294, 293, 286, 603, 360, 264, 912, 1900, 14581, 13, 28498,
  26019, 13, 51232], "temperature": 0.0, "avg_logprob": -0.14057522349887425, "compression_ratio":
  1.5296442687747036, "no_speech_prob": 0.003534645540639758}, {"id": 453, "seek":
  274456, "start": 2764.88, "end": 2772.24, "text": " Okay, so the very first result
  has Twitter in it, right? It''s right there. In fact, the second", "tokens": [51380,
  1033, 11, 370, 264, 588, 700, 1874, 575, 5794, 294, 309, 11, 558, 30, 467, 311,
  558, 456, 13, 682, 1186, 11, 264, 1150, 51748], "temperature": 0.0, "avg_logprob":
  -0.14057522349887425, "compression_ratio": 1.5296442687747036, "no_speech_prob":
  0.003534645540639758}, {"id": 454, "seek": 277224, "start": 2772.24, "end": 2776.9599999999996,
  "text": " result also has Twitter. Google programmable search engine is not going
  through the full Google", "tokens": [50364, 1874, 611, 575, 5794, 13, 3329, 37648,
  712, 3164, 2848, 307, 406, 516, 807, 264, 1577, 3329, 50600], "temperature": 0.0,
  "avg_logprob": -0.13128133920522836, "compression_ratio": 1.651639344262295, "no_speech_prob":
  0.0016597436042502522}, {"id": 455, "seek": 277224, "start": 2776.9599999999996,
  "end": 2784.8799999999997, "text": " parser. And it does not honor the not. However,
  if I say this, it works perfectly. The plus-minus syntax", "tokens": [50600, 21156,
  260, 13, 400, 309, 775, 406, 5968, 264, 406, 13, 2908, 11, 498, 286, 584, 341, 11,
  309, 1985, 6239, 13, 440, 1804, 12, 2367, 301, 28431, 50996], "temperature": 0.0,
  "avg_logprob": -0.13128133920522836, "compression_ratio": 1.651639344262295, "no_speech_prob":
  0.0016597436042502522}, {"id": 456, "seek": 277224, "start": 2784.8799999999997,
  "end": 2793.8399999999997, "text": " works. Okay. So now when we look at this definition,
  it says the not character for Google PSC is minus.", "tokens": [50996, 1985, 13,
  1033, 13, 407, 586, 562, 321, 574, 412, 341, 7123, 11, 309, 1619, 264, 406, 2517,
  337, 3329, 8168, 34, 307, 3175, 13, 51444], "temperature": 0.0, "avg_logprob": -0.13128133920522836,
  "compression_ratio": 1.651639344262295, "no_speech_prob": 0.0016597436042502522},
  {"id": 457, "seek": 277224, "start": 2794.56, "end": 2799.04, "text": " So now if
  we look at the search I ran, let''s look at the search object. It''s another object
  inside", "tokens": [51480, 407, 586, 498, 321, 574, 412, 264, 3164, 286, 5872, 11,
  718, 311, 574, 412, 264, 3164, 2657, 13, 467, 311, 1071, 2657, 1854, 51704], "temperature":
  0.0, "avg_logprob": -0.13128133920522836, "compression_ratio": 1.651639344262295,
  "no_speech_prob": 0.0016597436042502522}, {"id": 458, "seek": 279904, "start": 2799.04,
  "end": 2804.08, "text": " a swirl. Why is there a search object? Because in MetaSearch,
  it takes a few seconds to get the", "tokens": [50364, 257, 30310, 13, 1545, 307,
  456, 257, 3164, 2657, 30, 1436, 294, 6377, 64, 10637, 1178, 11, 309, 2516, 257,
  1326, 3949, 281, 483, 264, 50616], "temperature": 0.0, "avg_logprob": -0.14475833303560087,
  "compression_ratio": 1.7318840579710144, "no_speech_prob": 0.02041260525584221},
  {"id": 459, "seek": 279904, "start": 2804.08, "end": 2810.08, "text": " results
  from everything. And you may want to look at that data over and over again. In fact,
  one of", "tokens": [50616, 3542, 490, 1203, 13, 400, 291, 815, 528, 281, 574, 412,
  300, 1412, 670, 293, 670, 797, 13, 682, 1186, 11, 472, 295, 50916], "temperature":
  0.0, "avg_logprob": -0.14475833303560087, "compression_ratio": 1.7318840579710144,
  "no_speech_prob": 0.02041260525584221}, {"id": 460, "seek": 279904, "start": 2810.08,
  "end": 2813.92, "text": " the cool things you can do is swirl is you can set the
  subscribe function, swirl well, then", "tokens": [50916, 264, 1627, 721, 291, 393,
  360, 307, 30310, 307, 291, 393, 992, 264, 3022, 2445, 11, 30310, 731, 11, 550, 51108],
  "temperature": 0.0, "avg_logprob": -0.14475833303560087, "compression_ratio": 1.7318840579710144,
  "no_speech_prob": 0.02041260525584221}, {"id": 461, "seek": 279904, "start": 2813.92,
  "end": 2818.56, "text": " recheck for new results every so often and update and
  mark them new and you can even get an update", "tokens": [51108, 319, 15723, 337,
  777, 3542, 633, 370, 2049, 293, 5623, 293, 1491, 552, 777, 293, 291, 393, 754, 483,
  364, 5623, 51340], "temperature": 0.0, "avg_logprob": -0.14475833303560087, "compression_ratio":
  1.7318840579710144, "no_speech_prob": 0.02041260525584221}, {"id": 462, "seek":
  279904, "start": 2818.56, "end": 2822.48, "text": " things like that, right? So
  alert mode if you will or subscribe mode as we like to call it.", "tokens": [51340,
  721, 411, 300, 11, 558, 30, 407, 9615, 4391, 498, 291, 486, 420, 3022, 4391, 382,
  321, 411, 281, 818, 309, 13, 51536], "temperature": 0.0, "avg_logprob": -0.14475833303560087,
  "compression_ratio": 1.7318840579710144, "no_speech_prob": 0.02041260525584221},
  {"id": 463, "seek": 282248, "start": 2823.36, "end": 2830.2400000000002, "text":
  " So let''s take a look at the search object. What this object contains for starters,
  a block of messages", "tokens": [50408, 407, 718, 311, 747, 257, 574, 412, 264,
  3164, 2657, 13, 708, 341, 2657, 8306, 337, 35131, 11, 257, 3461, 295, 7897, 50752],
  "temperature": 0.0, "avg_logprob": -0.0993785759837357, "compression_ratio": 1.5833333333333333,
  "no_speech_prob": 0.0053709992207586765}, {"id": 464, "seek": 282248, "start": 2830.2400000000002,
  "end": 2836.16, "text": " that explain exactly what was done to the query. And here
  you can see the adaptive query processor", "tokens": [50752, 300, 2903, 2293, 437,
  390, 1096, 281, 264, 14581, 13, 400, 510, 291, 393, 536, 264, 27912, 14581, 15321,
  51048], "temperature": 0.0, "avg_logprob": -0.0993785759837357, "compression_ratio":
  1.5833333333333333, "no_speech_prob": 0.0053709992207586765}, {"id": 465, "seek":
  282248, "start": 2836.16, "end": 2843.12, "text": " rewrote the queries for Google
  PSC from Elon Musk not Twitter to Elon Musk minus Twitter. So this", "tokens": [51048,
  319, 7449, 1370, 264, 24109, 337, 3329, 8168, 34, 490, 28498, 26019, 406, 5794,
  281, 28498, 26019, 3175, 5794, 13, 407, 341, 51396], "temperature": 0.0, "avg_logprob":
  -0.0993785759837357, "compression_ratio": 1.5833333333333333, "no_speech_prob":
  0.0053709992207586765}, {"id": 466, "seek": 282248, "start": 2843.12, "end": 2847.6,
  "text": " way we guarantee you''re going to get the right result, not a bad result.
  Oh, and also our relevancy", "tokens": [51396, 636, 321, 10815, 291, 434, 516, 281,
  483, 264, 558, 1874, 11, 406, 257, 1578, 1874, 13, 876, 11, 293, 611, 527, 25916,
  6717, 51620], "temperature": 0.0, "avg_logprob": -0.0993785759837357, "compression_ratio":
  1.5833333333333333, "no_speech_prob": 0.0053709992207586765}, {"id": 467, "seek":
  284760, "start": 2847.6, "end": 2852.4, "text": " model checks. If you have a nodded
  term in your query and it finds it in relevancy, we drop it", "tokens": [50364,
  2316, 13834, 13, 759, 291, 362, 257, 15224, 9207, 1433, 294, 428, 14581, 293, 309,
  10704, 309, 294, 25916, 6717, 11, 321, 3270, 309, 50604], "temperature": 0.0, "avg_logprob":
  -0.13176261054144967, "compression_ratio": 1.606060606060606, "no_speech_prob":
  0.011119586415588856}, {"id": 468, "seek": 284760, "start": 2852.4, "end": 2856.48,
  "text": " to the bottom and say we actually put a special flag on it. We say this
  was a bad result.", "tokens": [50604, 281, 264, 2767, 293, 584, 321, 767, 829, 257,
  2121, 7166, 322, 309, 13, 492, 584, 341, 390, 257, 1578, 1874, 13, 50808], "temperature":
  0.0, "avg_logprob": -0.13176261054144967, "compression_ratio": 1.606060606060606,
  "no_speech_prob": 0.011119586415588856}, {"id": 469, "seek": 284760, "start": 2858.4,
  "end": 2863.2799999999997, "text": " Most of the others though, frankly, just either
  didn''t know they don''t handle not. You track", "tokens": [50904, 4534, 295, 264,
  2357, 1673, 11, 11939, 11, 445, 2139, 994, 380, 458, 436, 500, 380, 4813, 406, 13,
  509, 2837, 51148], "temperature": 0.0, "avg_logprob": -0.13176261054144967, "compression_ratio":
  1.606060606060606, "no_speech_prob": 0.011119586415588856}, {"id": 470, "seek":
  284760, "start": 2863.2799999999997, "end": 2867.92, "text": " doesn''t handle a
  knot at all. So we removed it completely and just say, go and give us what you''ve",
  "tokens": [51148, 1177, 380, 4813, 257, 16966, 412, 439, 13, 407, 321, 7261, 309,
  2584, 293, 445, 584, 11, 352, 293, 976, 505, 437, 291, 600, 51380], "temperature":
  0.0, "avg_logprob": -0.13176261054144967, "compression_ratio": 1.606060606060606,
  "no_speech_prob": 0.011119586415588856}, {"id": 471, "seek": 284760, "start": 2867.92,
  "end": 2873.2, "text": " got for that. And for others, we probably would have left
  them. Looking at the results, there''s also", "tokens": [51380, 658, 337, 300, 13,
  400, 337, 2357, 11, 321, 1391, 576, 362, 1411, 552, 13, 11053, 412, 264, 3542, 11,
  456, 311, 611, 51644], "temperature": 0.0, "avg_logprob": -0.13176261054144967,
  "compression_ratio": 1.606060606060606, "no_speech_prob": 0.011119586415588856},
  {"id": 472, "seek": 287320, "start": 2873.2, "end": 2878.0, "text": " an info block.
  This is all JSON. So it''s straightforward for developer using Python. It''s", "tokens":
  [50364, 364, 13614, 3461, 13, 639, 307, 439, 31828, 13, 407, 309, 311, 15325, 337,
  10754, 1228, 15329, 13, 467, 311, 50604], "temperature": 0.0, "avg_logprob": -0.12787823019356565,
  "compression_ratio": 1.6262626262626263, "no_speech_prob": 0.0014749389374628663},
  {"id": 473, "seek": 287320, "start": 2878.0, "end": 2883.7599999999998, "text":
  " little lists and dictionaries. There''s a result that describes what each of the
  different sources", "tokens": [50604, 707, 14511, 293, 22352, 4889, 13, 821, 311,
  257, 1874, 300, 15626, 437, 1184, 295, 264, 819, 7139, 50892], "temperature": 0.0,
  "avg_logprob": -0.12787823019356565, "compression_ratio": 1.6262626262626263, "no_speech_prob":
  0.0014749389374628663}, {"id": 474, "seek": 287320, "start": 2883.7599999999998,
  "end": 2889.68, "text": " gave back. Easy to parse if you want to build that. You
  have a filter URL so you can construct your own", "tokens": [50892, 2729, 646, 13,
  16002, 281, 48377, 498, 291, 528, 281, 1322, 300, 13, 509, 362, 257, 6608, 12905,
  370, 291, 393, 7690, 428, 1065, 51188], "temperature": 0.0, "avg_logprob": -0.12787823019356565,
  "compression_ratio": 1.6262626262626263, "no_speech_prob": 0.0014749389374628663},
  {"id": 475, "seek": 287320, "start": 2889.68, "end": 2895.8399999999997, "text":
  " facet display and to jump to any given provider. We actually give you the query
  that we ran. So if", "tokens": [51188, 1915, 302, 4674, 293, 281, 3012, 281, 604,
  2212, 12398, 13, 492, 767, 976, 291, 264, 14581, 300, 321, 5872, 13, 407, 498, 51496],
  "temperature": 0.0, "avg_logprob": -0.12787823019356565, "compression_ratio": 1.6262626262626263,
  "no_speech_prob": 0.0014749389374628663}, {"id": 476, "seek": 287320, "start": 2895.8399999999997,
  "end": 2899.68, "text": " you want to check the results, assuming you have the right
  credentials, there''s the results.", "tokens": [51496, 291, 528, 281, 1520, 264,
  3542, 11, 11926, 291, 362, 264, 558, 27404, 11, 456, 311, 264, 3542, 13, 51688],
  "temperature": 0.0, "avg_logprob": -0.12787823019356565, "compression_ratio": 1.6262626262626263,
  "no_speech_prob": 0.0014749389374628663}, {"id": 477, "seek": 289968, "start": 2899.68,
  "end": 2904.96, "text": " So I can actually go look at and modify my JSON. And then
  as you would expect, there''s a summary", "tokens": [50364, 407, 286, 393, 767,
  352, 574, 412, 293, 16927, 452, 31828, 13, 400, 550, 382, 291, 576, 2066, 11, 456,
  311, 257, 12691, 50628], "temperature": 0.0, "avg_logprob": -0.149194670505211,
  "compression_ratio": 1.6482758620689655, "no_speech_prob": 0.002980087650939822},
  {"id": 478, "seek": 289968, "start": 2904.96, "end": 2912.56, "text": " of what
  was found. So here''s what we actually searched. The overall query, if you want
  to rerun", "tokens": [50628, 295, 437, 390, 1352, 13, 407, 510, 311, 437, 321, 767,
  22961, 13, 440, 4787, 14581, 11, 498, 291, 528, 281, 43819, 409, 51008], "temperature":
  0.0, "avg_logprob": -0.149194670505211, "compression_ratio": 1.6482758620689655,
  "no_speech_prob": 0.002980087650939822}, {"id": 479, "seek": 289968, "start": 2912.56,
  "end": 2916.48, "text": " or update a query or rescore it, you can do that right
  from the result list. So those links are", "tokens": [51008, 420, 5623, 257, 14581,
  420, 9610, 418, 309, 11, 291, 393, 360, 300, 558, 490, 264, 1874, 1329, 13, 407,
  729, 6123, 366, 51204], "temperature": 0.0, "avg_logprob": -0.149194670505211, "compression_ratio":
  1.6482758620689655, "no_speech_prob": 0.002980087650939822}, {"id": 480, "seek":
  289968, "start": 2916.48, "end": 2922.64, "text": " available. We summarize the
  federation results and the time. Give you the next page of results,", "tokens":
  [51204, 2435, 13, 492, 20858, 264, 4636, 5053, 3542, 293, 264, 565, 13, 5303, 291,
  264, 958, 3028, 295, 3542, 11, 51512], "temperature": 0.0, "avg_logprob": -0.149194670505211,
  "compression_ratio": 1.6482758620689655, "no_speech_prob": 0.002980087650939822},
  {"id": 481, "seek": 289968, "start": 2922.64, "end": 2926.48, "text": " everything
  stored in swirl. So you can page through. By the way, you can also set a retention",
  "tokens": [51512, 1203, 12187, 294, 30310, 13, 407, 291, 393, 3028, 807, 13, 3146,
  264, 636, 11, 291, 393, 611, 992, 257, 22871, 51704], "temperature": 0.0, "avg_logprob":
  -0.149194670505211, "compression_ratio": 1.6482758620689655, "no_speech_prob": 0.002980087650939822},
  {"id": 482, "seek": 292648, "start": 2927.2, "end": 2931.6, "text": " or exploration
  factor if you want. So results will simply disappear for secure applications. You",
  "tokens": [50400, 420, 16197, 5952, 498, 291, 528, 13, 407, 3542, 486, 2935, 11596,
  337, 7144, 5821, 13, 509, 50620], "temperature": 0.0, "avg_logprob": -0.14801109786582203,
  "compression_ratio": 1.72992700729927, "no_speech_prob": 0.008976401761174202},
  {"id": 483, "seek": 292648, "start": 2931.6, "end": 2937.52, "text": " can even
  do it. So there''s no storage at all. And then the results. So from a developer
  perspective,", "tokens": [50620, 393, 754, 360, 309, 13, 407, 456, 311, 572, 6725,
  412, 439, 13, 400, 550, 264, 3542, 13, 407, 490, 257, 10754, 4585, 11, 50916], "temperature":
  0.0, "avg_logprob": -0.14801109786582203, "compression_ratio": 1.72992700729927,
  "no_speech_prob": 0.008976401761174202}, {"id": 484, "seek": 292648, "start": 2938.16,
  "end": 2943.44, "text": " literally, I''m going to extract the results dictionary
  or sorry, the results list from this", "tokens": [50948, 3736, 11, 286, 478, 516,
  281, 8947, 264, 3542, 25890, 420, 2597, 11, 264, 3542, 1329, 490, 341, 51212], "temperature":
  0.0, "avg_logprob": -0.14801109786582203, "compression_ratio": 1.72992700729927,
  "no_speech_prob": 0.008976401761174202}, {"id": 485, "seek": 292648, "start": 2943.44,
  "end": 2948.0, "text": " structure that I get back when I call it. And I''m going
  to iterate on that and each thing''s", "tokens": [51212, 3877, 300, 286, 483, 646,
  562, 286, 818, 309, 13, 400, 286, 478, 516, 281, 44497, 322, 300, 293, 1184, 551,
  311, 51440], "temperature": 0.0, "avg_logprob": -0.14801109786582203, "compression_ratio":
  1.72992700729927, "no_speech_prob": 0.008976401761174202}, {"id": 486, "seek": 292648,
  "start": 2948.0, "end": 2953.12, "text": " a dictionary. It''s a flat dictionary
  with as the things you would expect pretty much, right?", "tokens": [51440, 257,
  25890, 13, 467, 311, 257, 4962, 25890, 365, 382, 264, 721, 291, 576, 2066, 1238,
  709, 11, 558, 30, 51696], "temperature": 0.0, "avg_logprob": -0.14801109786582203,
  "compression_ratio": 1.72992700729927, "no_speech_prob": 0.008976401761174202},
  {"id": 487, "seek": 295312, "start": 2953.12, "end": 2960.08, "text": " Title URL,
  body, date published date retrieved and author. Everything else is meta information.",
  "tokens": [50364, 26768, 12905, 11, 1772, 11, 4002, 6572, 4002, 19817, 937, 293,
  3793, 13, 5471, 1646, 307, 19616, 1589, 13, 50712], "temperature": 0.0, "avg_logprob":
  -0.16446457879017976, "compression_ratio": 1.586092715231788, "no_speech_prob":
  0.002359856851398945}, {"id": 488, "seek": 295312, "start": 2960.08, "end": 2966.3199999999997,
  "text": " So what what search provider responded, what the rank was, our scores
  a score. There''s various", "tokens": [50712, 407, 437, 437, 3164, 12398, 15806,
  11, 437, 264, 6181, 390, 11, 527, 13444, 257, 6175, 13, 821, 311, 3683, 51024],
  "temperature": 0.0, "avg_logprob": -0.16446457879017976, "compression_ratio": 1.586092715231788,
  "no_speech_prob": 0.002359856851398945}, {"id": 489, "seek": 295312, "start": 2966.3199999999997,
  "end": 2970.96, "text": " techniques to turn that into a probability or a confidence
  level if you would like. We may do", "tokens": [51024, 7512, 281, 1261, 300, 666,
  257, 8482, 420, 257, 6687, 1496, 498, 291, 576, 411, 13, 492, 815, 360, 51256],
  "temperature": 0.0, "avg_logprob": -0.16446457879017976, "compression_ratio": 1.586092715231788,
  "no_speech_prob": 0.002359856851398945}, {"id": 490, "seek": 295312, "start": 2970.96,
  "end": 2975.6, "text": " that in the future. I think it''s if people wanted it,
  we''d love to hear about it. I think for now,", "tokens": [51256, 300, 294, 264,
  2027, 13, 286, 519, 309, 311, 498, 561, 1415, 309, 11, 321, 1116, 959, 281, 1568,
  466, 309, 13, 286, 519, 337, 586, 11, 51488], "temperature": 0.0, "avg_logprob":
  -0.16446457879017976, "compression_ratio": 1.586092715231788, "no_speech_prob":
  0.002359856851398945}, {"id": 491, "seek": 295312, "start": 2975.6, "end": 2981.6,
  "text": " though, people seem to be very happy just with rank. Most importantly,
  and really, this is what", "tokens": [51488, 1673, 11, 561, 1643, 281, 312, 588,
  2055, 445, 365, 6181, 13, 4534, 8906, 11, 293, 534, 11, 341, 307, 437, 51788], "temperature":
  0.0, "avg_logprob": -0.16446457879017976, "compression_ratio": 1.586092715231788,
  "no_speech_prob": 0.002359856851398945}, {"id": 492, "seek": 298160, "start": 2981.6,
  "end": 2988.0, "text": " swirls ultimate value is, we explain exactly why the result
  matched and why it scored as it did.", "tokens": [50364, 30310, 82, 9705, 2158,
  307, 11, 321, 2903, 2293, 983, 264, 1874, 21447, 293, 983, 309, 18139, 382, 309,
  630, 13, 50684], "temperature": 0.0, "avg_logprob": -0.169556786032284, "compression_ratio":
  1.6483050847457628, "no_speech_prob": 0.0012338421074673533}, {"id": 493, "seek":
  298160, "start": 2988.48, "end": 2993.2, "text": " So for example, we in this case,
  of course, there are no stems for a name, but we do as basically", "tokens": [50708,
  407, 337, 1365, 11, 321, 294, 341, 1389, 11, 295, 1164, 11, 456, 366, 572, 27600,
  337, 257, 1315, 11, 457, 321, 360, 382, 1936, 50944], "temperature": 0.0, "avg_logprob":
  -0.169556786032284, "compression_ratio": 1.6483050847457628, "no_speech_prob": 0.0012338421074673533},
  {"id": 494, "seek": 298160, "start": 2993.2, "end": 3000.3199999999997, "text":
  " we use nltk, we stem to maximize recall. Then you''ll see the actual extracted
  hits, the actual", "tokens": [50944, 321, 764, 297, 2282, 74, 11, 321, 12312, 281,
  19874, 9901, 13, 1396, 291, 603, 536, 264, 3539, 34086, 8664, 11, 264, 3539, 51300],
  "temperature": 0.0, "avg_logprob": -0.169556786032284, "compression_ratio": 1.6483050847457628,
  "no_speech_prob": 0.0012338421074673533}, {"id": 495, "seek": 298160, "start": 3000.3199999999997,
  "end": 3005.12, "text": " hit, not the lower case tokenized version, right? So we
  extract the actual hit. And then we produce", "tokens": [51300, 2045, 11, 406, 264,
  3126, 1389, 14862, 1602, 3037, 11, 558, 30, 407, 321, 8947, 264, 3539, 2045, 13,
  400, 550, 321, 5258, 51540], "temperature": 0.0, "avg_logprob": -0.169556786032284,
  "compression_ratio": 1.6483050847457628, "no_speech_prob": 0.0012338421074673533},
  {"id": 496, "seek": 300512, "start": 3005.12, "end": 3013.52, "text": " the score,
  which is this is the cosine similarity between the query and the text around it
  in the result.", "tokens": [50364, 264, 6175, 11, 597, 307, 341, 307, 264, 23565,
  32194, 1296, 264, 14581, 293, 264, 2487, 926, 309, 294, 264, 1874, 13, 50784], "temperature":
  0.0, "avg_logprob": -0.1206219372925935, "compression_ratio": 1.8066914498141264,
  "no_speech_prob": 0.0025992179289460182}, {"id": 497, "seek": 300512, "start": 3014.08,
  "end": 3019.04, "text": " So we kind of sentence tokenize the result that we get
  and then we''re basically looking", "tokens": [50812, 407, 321, 733, 295, 8174,
  14862, 1125, 264, 1874, 300, 321, 483, 293, 550, 321, 434, 1936, 1237, 51060], "temperature":
  0.0, "avg_logprob": -0.1206219372925935, "compression_ratio": 1.8066914498141264,
  "no_speech_prob": 0.0025992179289460182}, {"id": 498, "seek": 300512, "start": 3019.04,
  "end": 3024.64, "text": " to try and stay within that sentence and see how relevant
  it is. And ultimately, we also adjust", "tokens": [51060, 281, 853, 293, 1754, 1951,
  300, 8174, 293, 536, 577, 7340, 309, 307, 13, 400, 6284, 11, 321, 611, 4369, 51340],
  "temperature": 0.0, "avg_logprob": -0.1206219372925935, "compression_ratio": 1.8066914498141264,
  "no_speech_prob": 0.0025992179289460182}, {"id": 499, "seek": 300512, "start": 3024.64,
  "end": 3028.48, "text": " since we are sending different queries to different systems
  and of course, different systems have", "tokens": [51340, 1670, 321, 366, 7750,
  819, 24109, 281, 819, 3652, 293, 295, 1164, 11, 819, 3652, 362, 51532], "temperature":
  0.0, "avg_logprob": -0.1206219372925935, "compression_ratio": 1.8066914498141264,
  "no_speech_prob": 0.0025992179289460182}, {"id": 500, "seek": 300512, "start": 3028.48,
  "end": 3032.7999999999997, "text": " different result links on average. We do adjustments
  for both of those. We also give you the exact", "tokens": [51532, 819, 1874, 6123,
  322, 4274, 13, 492, 360, 18624, 337, 1293, 295, 729, 13, 492, 611, 976, 291, 264,
  1900, 51748], "temperature": 0.0, "avg_logprob": -0.1206219372925935, "compression_ratio":
  1.8066914498141264, "no_speech_prob": 0.0025992179289460182}, {"id": 501, "seek":
  303280, "start": 3032.8, "end": 3041.52, "text": " token locations for everything
  that''s hit and ready to rank from there. Wow. So much is done behind", "tokens":
  [50364, 14862, 9253, 337, 1203, 300, 311, 2045, 293, 1919, 281, 6181, 490, 456,
  13, 3153, 13, 407, 709, 307, 1096, 2261, 50800], "temperature": 0.0, "avg_logprob":
  -0.1566390722570285, "compression_ratio": 1.580110497237569, "no_speech_prob": 0.007770642172545195},
  {"id": 502, "seek": 303280, "start": 3041.52, "end": 3050.4, "text": " the scenes
  here. And so much is simplified on the other side, on the outer side. That''s amazing.",
  "tokens": [50800, 264, 8026, 510, 13, 400, 370, 709, 307, 26335, 322, 264, 661,
  1252, 11, 322, 264, 10847, 1252, 13, 663, 311, 2243, 13, 51244], "temperature":
  0.0, "avg_logprob": -0.1566390722570285, "compression_ratio": 1.580110497237569,
  "no_speech_prob": 0.007770642172545195}, {"id": 503, "seek": 303280, "start": 3051.6800000000003,
  "end": 3057.76, "text": " And how many systems do you support or which systems do
  you support out of the box today?", "tokens": [51308, 400, 577, 867, 3652, 360,
  291, 1406, 420, 597, 3652, 360, 291, 1406, 484, 295, 264, 2424, 965, 30, 51612],
  "temperature": 0.0, "avg_logprob": -0.1566390722570285, "compression_ratio": 1.580110497237569,
  "no_speech_prob": 0.007770642172545195}, {"id": 504, "seek": 305776, "start": 3058.6400000000003,
  "end": 3063.44, "text": " So I''m happy to say we have connectors to all of the
  major open source search engines, including solar,", "tokens": [50408, 407, 286,
  478, 2055, 281, 584, 321, 362, 31865, 281, 439, 295, 264, 2563, 1269, 4009, 3164,
  12982, 11, 3009, 7936, 11, 50648], "temperature": 0.0, "avg_logprob": -0.1943179902576265,
  "compression_ratio": 1.6, "no_speech_prob": 0.010007666423916817}, {"id": 505, "seek":
  305776, "start": 3063.92, "end": 3071.1200000000003, "text": " AWS open search or
  open search.org, I should say, an elastic search. We also support the main", "tokens":
  [50672, 17650, 1269, 3164, 420, 1269, 3164, 13, 4646, 11, 286, 820, 584, 11, 364,
  17115, 3164, 13, 492, 611, 1406, 264, 2135, 51032], "temperature": 0.0, "avg_logprob":
  -0.1943179902576265, "compression_ratio": 1.6, "no_speech_prob": 0.010007666423916817},
  {"id": 506, "seek": 305776, "start": 3071.1200000000003, "end": 3077.92, "text":
  " open databases, Postgres, SQLite, also some of the more traditional cloud ones,
  Google BigQuery, for", "tokens": [51032, 1269, 22380, 11, 10223, 45189, 11, 19200,
  642, 11, 611, 512, 295, 264, 544, 5164, 4588, 2306, 11, 3329, 43422, 11, 337, 51372],
  "temperature": 0.0, "avg_logprob": -0.1943179902576265, "compression_ratio": 1.6,
  "no_speech_prob": 0.010007666423916817}, {"id": 507, "seek": 305776, "start": 3077.92,
  "end": 3085.5200000000004, "text": " example. And we are in the process of adding,
  as I mentioned, M365. We also have, as of the last one,", "tokens": [51372, 1365,
  13, 400, 321, 366, 294, 264, 1399, 295, 5127, 11, 382, 286, 2835, 11, 376, 11309,
  20, 13, 492, 611, 362, 11, 382, 295, 264, 1036, 472, 11, 51752], "temperature":
  0.0, "avg_logprob": -0.1943179902576265, "compression_ratio": 1.6, "no_speech_prob":
  0.010007666423916817}, {"id": 508, "seek": 308552, "start": 3085.52, "end": 3091.04,
  "text": " you can connect to Atlassian using our request get. You can connect to
  UTRAC. So many of the", "tokens": [50364, 291, 393, 1745, 281, 11000, 640, 952,
  1228, 527, 5308, 483, 13, 509, 393, 1745, 281, 624, 51, 3750, 34, 13, 407, 867,
  295, 264, 50640], "temperature": 0.0, "avg_logprob": -0.1748656382602928, "compression_ratio":
  1.625, "no_speech_prob": 0.011157287284731865}, {"id": 509, "seek": 308552, "start":
  3091.6, "end": 3096.0, "text": " sophisticated repositories, you can actually just
  use the request get connector to talk to them.", "tokens": [50668, 16950, 22283,
  2083, 11, 291, 393, 767, 445, 764, 264, 5308, 483, 19127, 281, 751, 281, 552, 13,
  50888], "temperature": 0.0, "avg_logprob": -0.1748656382602928, "compression_ratio":
  1.625, "no_speech_prob": 0.011157287284731865}, {"id": 510, "seek": 308552, "start":
  3096.8, "end": 3101.92, "text": " And M365 and Slack are coming in our next release,
  which is next month.", "tokens": [50928, 400, 376, 11309, 20, 293, 37211, 366, 1348,
  294, 527, 958, 4374, 11, 597, 307, 958, 1618, 13, 51184], "temperature": 0.0, "avg_logprob":
  -0.1748656382602928, "compression_ratio": 1.625, "no_speech_prob": 0.011157287284731865},
  {"id": 511, "seek": 308552, "start": 3102.96, "end": 3109.28, "text": " Well, I
  think especially Slack or any like messenger that also has this kind of APIs that",
  "tokens": [51236, 1042, 11, 286, 519, 2318, 37211, 420, 604, 411, 26599, 300, 611,
  575, 341, 733, 295, 21445, 300, 51552], "temperature": 0.0, "avg_logprob": -0.1748656382602928,
  "compression_ratio": 1.625, "no_speech_prob": 0.011157287284731865}, {"id": 512,
  "seek": 308552, "start": 3109.28, "end": 3114.64, "text": " can utilize, I think
  that''s going to be like a big thing in my opinion, because so much is", "tokens":
  [51552, 393, 16117, 11, 286, 519, 300, 311, 516, 281, 312, 411, 257, 955, 551, 294,
  452, 4800, 11, 570, 370, 709, 307, 51820], "temperature": 0.0, "avg_logprob": -0.1748656382602928,
  "compression_ratio": 1.625, "no_speech_prob": 0.011157287284731865}, {"id": 513,
  "seek": 311464, "start": 3114.64, "end": 3120.96, "text": " happening in Slack or
  similar platforms. You know, so much knowledge is kind of written there in", "tokens":
  [50364, 2737, 294, 37211, 420, 2531, 9473, 13, 509, 458, 11, 370, 709, 3601, 307,
  733, 295, 3720, 456, 294, 50680], "temperature": 0.0, "avg_logprob": -0.16908105936917392,
  "compression_ratio": 1.48828125, "no_speech_prob": 0.0022082871291786432}, {"id":
  514, "seek": 311464, "start": 3120.96, "end": 3125.7599999999998, "text": " public
  channel. So you''re in your own direct messages, right? It''s possible to access
  them.", "tokens": [50680, 1908, 2269, 13, 407, 291, 434, 294, 428, 1065, 2047, 7897,
  11, 558, 30, 467, 311, 1944, 281, 2105, 552, 13, 50920], "temperature": 0.0, "avg_logprob":
  -0.16908105936917392, "compression_ratio": 1.48828125, "no_speech_prob": 0.0022082871291786432},
  {"id": 515, "seek": 311464, "start": 3126.64, "end": 3133.2, "text": " Then I think
  that this is amazing. We even support Microsoft Teams in the next release, full",
  "tokens": [50964, 1396, 286, 519, 300, 341, 307, 2243, 13, 492, 754, 1406, 8116,
  24702, 294, 264, 958, 4374, 11, 1577, 51292], "temperature": 0.0, "avg_logprob":
  -0.16908105936917392, "compression_ratio": 1.48828125, "no_speech_prob": 0.0022082871291786432},
  {"id": 516, "seek": 311464, "start": 3133.2, "end": 3138.64, "text": " search of
  messages, also all the shared objects, depending on configuration. And if you''re
  familiar", "tokens": [51292, 3164, 295, 7897, 11, 611, 439, 264, 5507, 6565, 11,
  5413, 322, 11694, 13, 400, 498, 291, 434, 4963, 51564], "temperature": 0.0, "avg_logprob":
  -0.16908105936917392, "compression_ratio": 1.48828125, "no_speech_prob": 0.0022082871291786432},
  {"id": 517, "seek": 313864, "start": 3139.12, "end": 3147.92, "text": " with the
  M365 OpenID connect, the infrastructure and sort of that ecosystem, it''s entirely
  under", "tokens": [50388, 365, 264, 376, 11309, 20, 7238, 2777, 1745, 11, 264, 6896,
  293, 1333, 295, 300, 11311, 11, 309, 311, 7696, 833, 50828], "temperature": 0.0,
  "avg_logprob": -0.1988883399963379, "compression_ratio": 1.5039370078740157, "no_speech_prob":
  0.0131960054859519}, {"id": 518, "seek": 313864, "start": 3147.92, "end": 3153.68,
  "text": " the deployers control. Swirl is just software. I mean, we have a hosted
  platform which you get", "tokens": [50828, 264, 7274, 433, 1969, 13, 3926, 1648,
  307, 445, 4722, 13, 286, 914, 11, 321, 362, 257, 19204, 3663, 597, 291, 483, 51116],
  "temperature": 0.0, "avg_logprob": -0.1988883399963379, "compression_ratio": 1.5039370078740157,
  "no_speech_prob": 0.0131960054859519}, {"id": 519, "seek": 313864, "start": 3153.68,
  "end": 3159.44, "text": " connected to, but the permissioning, all of that is actually
  done on the on the owner''s side. And", "tokens": [51116, 4582, 281, 11, 457, 264,
  11226, 278, 11, 439, 295, 300, 307, 767, 1096, 322, 264, 322, 264, 7289, 311, 1252,
  13, 400, 51404], "temperature": 0.0, "avg_logprob": -0.1988883399963379, "compression_ratio":
  1.5039370078740157, "no_speech_prob": 0.0131960054859519}, {"id": 520, "seek": 313864,
  "start": 3159.44, "end": 3166.24, "text": " you can turn it off in one second for
  any reason you''re uncomfortable. But Swirl 2.0, again,", "tokens": [51404, 291,
  393, 1261, 309, 766, 294, 472, 1150, 337, 604, 1778, 291, 434, 10532, 13, 583, 3926,
  1648, 568, 13, 15, 11, 797, 11, 51744], "temperature": 0.0, "avg_logprob": -0.1988883399963379,
  "compression_ratio": 1.5039370078740157, "no_speech_prob": 0.0131960054859519},
  {"id": 521, "seek": 316624, "start": 3166.24, "end": 3172.8799999999997, "text":
  " we''ll be coming out next month, has all of the OAuth and OIDC capabilities so
  that you''re really", "tokens": [50364, 321, 603, 312, 1348, 484, 958, 1618, 11,
  575, 439, 295, 264, 48424, 2910, 293, 422, 2777, 34, 10862, 370, 300, 291, 434,
  534, 50696], "temperature": 0.0, "avg_logprob": -0.18983150565105936, "compression_ratio":
  1.4980237154150198, "no_speech_prob": 0.005239561200141907}, {"id": 522, "seek":
  316624, "start": 3172.8799999999997, "end": 3177.9199999999996, "text": " just connecting
  your Microsoft account, searching through that stuff. And there''s no other user",
  "tokens": [50696, 445, 11015, 428, 8116, 2696, 11, 10808, 807, 300, 1507, 13, 400,
  456, 311, 572, 661, 4195, 50948], "temperature": 0.0, "avg_logprob": -0.18983150565105936,
  "compression_ratio": 1.4980237154150198, "no_speech_prob": 0.005239561200141907},
  {"id": 523, "seek": 316624, "start": 3177.9199999999996, "end": 3184.72, "text":
  " interfaces or IDs or anything like that. It''s all seamless. And again, I''ll
  completely", "tokens": [50948, 28416, 420, 48212, 420, 1340, 411, 300, 13, 467,
  311, 439, 28677, 13, 400, 797, 11, 286, 603, 2584, 51288], "temperature": 0.0, "avg_logprob":
  -0.18983150565105936, "compression_ratio": 1.4980237154150198, "no_speech_prob":
  0.005239561200141907}, {"id": 524, "seek": 316624, "start": 3185.6, "end": 3192.3999999999996,
  "text": " controlled by the deploy inside that M36510 and owner. Yeah, fantastic.
  Is there something else you", "tokens": [51332, 10164, 538, 264, 7274, 1854, 300,
  376, 11309, 20, 3279, 293, 7289, 13, 865, 11, 5456, 13, 1119, 456, 746, 1646, 291,
  51672], "temperature": 0.0, "avg_logprob": -0.18983150565105936, "compression_ratio":
  1.4980237154150198, "no_speech_prob": 0.005239561200141907}, {"id": 525, "seek":
  319240, "start": 3192.4, "end": 3199.28, "text": " want to show on this demo? Or
  we want to go back to our audio mode video and audio for those", "tokens": [50364,
  528, 281, 855, 322, 341, 10723, 30, 1610, 321, 528, 281, 352, 646, 281, 527, 6278,
  4391, 960, 293, 6278, 337, 729, 50708], "temperature": 0.0, "avg_logprob": -0.13696183368658563,
  "compression_ratio": 1.710914454277286, "no_speech_prob": 0.025341203436255455},
  {"id": 526, "seek": 319240, "start": 3199.28, "end": 3203.6800000000003, "text":
  " who are listening only. All right. I hope that was more than enough. You know,
  there''s a ton to", "tokens": [50708, 567, 366, 4764, 787, 13, 1057, 558, 13, 286,
  1454, 300, 390, 544, 813, 1547, 13, 509, 458, 11, 456, 311, 257, 2952, 281, 50928],
  "temperature": 0.0, "avg_logprob": -0.13696183368658563, "compression_ratio": 1.710914454277286,
  "no_speech_prob": 0.025341203436255455}, {"id": 527, "seek": 319240, "start": 3203.6800000000003,
  "end": 3207.6, "text": " show. I just want to give a little flavor for it. And in
  particular, you know, we''re really focused", "tokens": [50928, 855, 13, 286, 445,
  528, 281, 976, 257, 707, 6813, 337, 309, 13, 400, 294, 1729, 11, 291, 458, 11, 321,
  434, 534, 5178, 51124], "temperature": 0.0, "avg_logprob": -0.13696183368658563,
  "compression_ratio": 1.710914454277286, "no_speech_prob": 0.025341203436255455},
  {"id": 528, "seek": 319240, "start": 3207.6, "end": 3212.8, "text": " on making
  this easy for developers. That''s the current audience. I think there''s lots more
  we can do", "tokens": [51124, 322, 1455, 341, 1858, 337, 8849, 13, 663, 311, 264,
  2190, 4034, 13, 286, 519, 456, 311, 3195, 544, 321, 393, 360, 51384], "temperature":
  0.0, "avg_logprob": -0.13696183368658563, "compression_ratio": 1.710914454277286,
  "no_speech_prob": 0.025341203436255455}, {"id": 529, "seek": 319240, "start": 3212.8,
  "end": 3217.04, "text": " in the future. But if you want to add a bunch of sources
  or solve a multi-silver search problem,", "tokens": [51384, 294, 264, 2027, 13,
  583, 498, 291, 528, 281, 909, 257, 3840, 295, 7139, 420, 5039, 257, 4825, 12, 30605,
  331, 3164, 1154, 11, 51596], "temperature": 0.0, "avg_logprob": -0.13696183368658563,
  "compression_ratio": 1.710914454277286, "no_speech_prob": 0.025341203436255455},
  {"id": 530, "seek": 319240, "start": 3217.04, "end": 3222.32, "text": " that''s
  what Swirls intended to do. That''s a... It''s amazing. It''s amazing. And how do
  you see", "tokens": [51596, 300, 311, 437, 3926, 1648, 82, 10226, 281, 360, 13,
  663, 311, 257, 485, 467, 311, 2243, 13, 467, 311, 2243, 13, 400, 577, 360, 291,
  536, 51860], "temperature": 0.0, "avg_logprob": -0.13696183368658563, "compression_ratio":
  1.710914454277286, "no_speech_prob": 0.025341203436255455}, {"id": 531, "seek":
  322232, "start": 3223.04, "end": 3229.76, "text": " the clientele? Like, what is
  the ideal client for this system? How do you want to interact with", "tokens": [50400,
  264, 6423, 16884, 30, 1743, 11, 437, 307, 264, 7157, 6423, 337, 341, 1185, 30, 1012,
  360, 291, 528, 281, 4648, 365, 50736], "temperature": 0.0, "avg_logprob": -0.16753488540649414,
  "compression_ratio": 1.572, "no_speech_prob": 0.003833875060081482}, {"id": 532,
  "seek": 322232, "start": 3229.76, "end": 3236.1600000000003, "text": " these clients?
  And how do you see... Or maybe you''ll already experience this, you know, first
  steps to", "tokens": [50736, 613, 6982, 30, 400, 577, 360, 291, 536, 485, 1610,
  1310, 291, 603, 1217, 1752, 341, 11, 291, 458, 11, 700, 4439, 281, 51056], "temperature":
  0.0, "avg_logprob": -0.16753488540649414, "compression_ratio": 1.572, "no_speech_prob":
  0.003833875060081482}, {"id": 533, "seek": 322232, "start": 3237.04, "end": 3245.28,
  "text": " succeeding on this path? So I honestly, people who are using it today
  are doing three things with it.", "tokens": [51100, 47912, 322, 341, 3100, 30, 407,
  286, 6095, 11, 561, 567, 366, 1228, 309, 965, 366, 884, 1045, 721, 365, 309, 13,
  51512], "temperature": 0.0, "avg_logprob": -0.16753488540649414, "compression_ratio":
  1.572, "no_speech_prob": 0.003833875060081482}, {"id": 534, "seek": 322232, "start":
  3245.28, "end": 3250.6400000000003, "text": " And I''m super curious, right, as
  to which ones of these will evolve. I think the most basic,", "tokens": [51512,
  400, 286, 478, 1687, 6369, 11, 558, 11, 382, 281, 597, 2306, 295, 613, 486, 16693,
  13, 286, 519, 264, 881, 3875, 11, 51780], "temperature": 0.0, "avg_logprob": -0.16753488540649414,
  "compression_ratio": 1.572, "no_speech_prob": 0.003833875060081482}, {"id": 535,
  "seek": 325064, "start": 3250.64, "end": 3254.0, "text": " you know, or interesting
  use case, right, or the sort of like the most obvious use case", "tokens": [50364,
  291, 458, 11, 420, 1880, 764, 1389, 11, 558, 11, 420, 264, 1333, 295, 411, 264,
  881, 6322, 764, 1389, 50532], "temperature": 0.0, "avg_logprob": -0.10049458452173181,
  "compression_ratio": 1.7725856697819315, "no_speech_prob": 0.0027524952311068773},
  {"id": 536, "seek": 325064, "start": 3254.64, "end": 3259.44, "text": " is one search
  box to rule them all, apart from the Lord of the Rings reference. But honestly,",
  "tokens": [50564, 307, 472, 3164, 2424, 281, 4978, 552, 439, 11, 4936, 490, 264,
  3257, 295, 264, 38543, 6408, 13, 583, 6095, 11, 50804], "temperature": 0.0, "avg_logprob":
  -0.10049458452173181, "compression_ratio": 1.7725856697819315, "no_speech_prob":
  0.0027524952311068773}, {"id": 537, "seek": 325064, "start": 3259.44, "end": 3264.3199999999997,
  "text": " that''s been so hard. If you''ve done a lot of enterprise search projects,
  normally, you know,", "tokens": [50804, 300, 311, 668, 370, 1152, 13, 759, 291,
  600, 1096, 257, 688, 295, 14132, 3164, 4455, 11, 5646, 11, 291, 458, 11, 51048],
  "temperature": 0.0, "avg_logprob": -0.10049458452173181, "compression_ratio": 1.7725856697819315,
  "no_speech_prob": 0.0027524952311068773}, {"id": 538, "seek": 325064, "start": 3264.3199999999997,
  "end": 3268.96, "text": " for the initial scope, and it''s expensive, and it takes
  about a year or whatever, you know,", "tokens": [51048, 337, 264, 5883, 11923, 11,
  293, 309, 311, 5124, 11, 293, 309, 2516, 466, 257, 1064, 420, 2035, 11, 291, 458,
  11, 51280], "temperature": 0.0, "avg_logprob": -0.10049458452173181, "compression_ratio":
  1.7725856697819315, "no_speech_prob": 0.0027524952311068773}, {"id": 539, "seek":
  325064, "start": 3268.96, "end": 3273.8399999999997, "text": " you get a couple
  silos in place, and things are good, and people like it. But adding silos over time",
  "tokens": [51280, 291, 483, 257, 1916, 48893, 294, 1081, 11, 293, 721, 366, 665,
  11, 293, 561, 411, 309, 13, 583, 5127, 48893, 670, 565, 51524], "temperature": 0.0,
  "avg_logprob": -0.10049458452173181, "compression_ratio": 1.7725856697819315, "no_speech_prob":
  0.0027524952311068773}, {"id": 540, "seek": 325064, "start": 3273.8399999999997,
  "end": 3279.6, "text": " is super costly, and it''s hard, and this is the way to
  do it. You have a great existing search index,", "tokens": [51524, 307, 1687, 28328,
  11, 293, 309, 311, 1152, 11, 293, 341, 307, 264, 636, 281, 360, 309, 13, 509, 362,
  257, 869, 6741, 3164, 8186, 11, 51812], "temperature": 0.0, "avg_logprob": -0.10049458452173181,
  "compression_ratio": 1.7725856697819315, "no_speech_prob": 0.0027524952311068773},
  {"id": 541, "seek": 327960, "start": 3279.6, "end": 3286.48, "text": " you have
  a search UI, awesome. Connect the search index to Swirl, and connect your UI to
  Swirl.", "tokens": [50364, 291, 362, 257, 3164, 15682, 11, 3476, 13, 11653, 264,
  3164, 8186, 281, 3926, 1648, 11, 293, 1745, 428, 15682, 281, 3926, 1648, 13, 50708],
  "temperature": 0.0, "avg_logprob": -0.10534522268507215, "compression_ratio": 1.6,
  "no_speech_prob": 0.002256683073937893}, {"id": 542, "seek": 327960, "start": 3286.48,
  "end": 3291.44, "text": " Now you can add a whole bunch of other sources and get
  great ranking, and you don''t have to change", "tokens": [50708, 823, 291, 393,
  909, 257, 1379, 3840, 295, 661, 7139, 293, 483, 869, 17833, 11, 293, 291, 500, 380,
  362, 281, 1319, 50956], "temperature": 0.0, "avg_logprob": -0.10534522268507215,
  "compression_ratio": 1.6, "no_speech_prob": 0.002256683073937893}, {"id": 543, "seek":
  327960, "start": 3291.44, "end": 3297.68, "text": " the UI necessarily. For the
  most part, every search UI has URL, title, and body, and maybe a date.", "tokens":
  [50956, 264, 15682, 4725, 13, 1171, 264, 881, 644, 11, 633, 3164, 15682, 575, 12905,
  11, 4876, 11, 293, 1772, 11, 293, 1310, 257, 4002, 13, 51268], "temperature": 0.0,
  "avg_logprob": -0.10534522268507215, "compression_ratio": 1.6, "no_speech_prob":
  0.002256683073937893}, {"id": 544, "seek": 327960, "start": 3297.68, "end": 3302.72,
  "text": " Okay, so if, for starters, you can just take those. And if you have more,
  right, if you want to do", "tokens": [51268, 1033, 11, 370, 498, 11, 337, 35131,
  11, 291, 393, 445, 747, 729, 13, 400, 498, 291, 362, 544, 11, 558, 11, 498, 291,
  528, 281, 360, 51520], "temperature": 0.0, "avg_logprob": -0.10534522268507215,
  "compression_ratio": 1.6, "no_speech_prob": 0.002256683073937893}, {"id": 545, "seek":
  330272, "start": 3302.72, "end": 3308.64, "text": " a source facet, that''s cool.
  From there, I think, you know, people with Python, right, Django,", "tokens": [50364,
  257, 4009, 1915, 302, 11, 300, 311, 1627, 13, 3358, 456, 11, 286, 519, 11, 291,
  458, 11, 561, 365, 15329, 11, 558, 11, 33464, 17150, 11, 50660], "temperature":
  0.0, "avg_logprob": -0.14359905101634837, "compression_ratio": 1.697594501718213,
  "no_speech_prob": 0.006232177373021841}, {"id": 546, "seek": 330272, "start": 3309.68,
  "end": 3313.6, "text": " experience, and who want to take this and tailor it, we''d
  love to help, we''d love to hear what you''re", "tokens": [50712, 1752, 11, 293,
  567, 528, 281, 747, 341, 293, 33068, 309, 11, 321, 1116, 959, 281, 854, 11, 321,
  1116, 959, 281, 1568, 437, 291, 434, 50908], "temperature": 0.0, "avg_logprob":
  -0.14359905101634837, "compression_ratio": 1.697594501718213, "no_speech_prob":
  0.006232177373021841}, {"id": 547, "seek": 330272, "start": 3313.6, "end": 3318.9599999999996,
  "text": " doing. Again, please, the Slack supports all free, just join up the community
  and get in there,", "tokens": [50908, 884, 13, 3764, 11, 1767, 11, 264, 37211, 9346,
  439, 1737, 11, 445, 3917, 493, 264, 1768, 293, 483, 294, 456, 11, 51176], "temperature":
  0.0, "avg_logprob": -0.14359905101634837, "compression_ratio": 1.697594501718213,
  "no_speech_prob": 0.006232177373021841}, {"id": 548, "seek": 330272, "start": 3318.9599999999996,
  "end": 3323.52, "text": " and tell us what''s going on, or ask. And I think there''s
  lots of other people who are working with", "tokens": [51176, 293, 980, 505, 437,
  311, 516, 322, 11, 420, 1029, 13, 400, 286, 519, 456, 311, 3195, 295, 661, 561,
  567, 366, 1364, 365, 51404], "temperature": 0.0, "avg_logprob": -0.14359905101634837,
  "compression_ratio": 1.697594501718213, "no_speech_prob": 0.006232177373021841},
  {"id": 549, "seek": 330272, "start": 3323.52, "end": 3329.4399999999996, "text":
  " it too, who are started to, you know, answer questions and things like that. The
  second thing, though,", "tokens": [51404, 309, 886, 11, 567, 366, 1409, 281, 11,
  291, 458, 11, 1867, 1651, 293, 721, 411, 300, 13, 440, 1150, 551, 11, 1673, 11,
  51700], "temperature": 0.0, "avg_logprob": -0.14359905101634837, "compression_ratio":
  1.697594501718213, "no_speech_prob": 0.006232177373021841}, {"id": 550, "seek":
  332944, "start": 3329.92, "end": 3334.32, "text": " there are definitely use cases
  where people really want to monitor multiple sources,", "tokens": [50388, 456, 366,
  2138, 764, 3331, 689, 561, 534, 528, 281, 6002, 3866, 7139, 11, 50608], "temperature":
  0.0, "avg_logprob": -0.12125456919435595, "compression_ratio": 1.6421052631578947,
  "no_speech_prob": 0.0020573094952851534}, {"id": 551, "seek": 332944, "start": 3334.32,
  "end": 3339.36, "text": " and push notifications out, like, to Slack, and to teams,
  and things like that. That''s a very different", "tokens": [50608, 293, 2944, 13426,
  484, 11, 411, 11, 281, 37211, 11, 293, 281, 5491, 11, 293, 721, 411, 300, 13, 663,
  311, 257, 588, 819, 50860], "temperature": 0.0, "avg_logprob": -0.12125456919435595,
  "compression_ratio": 1.6421052631578947, "no_speech_prob": 0.0020573094952851534},
  {"id": 552, "seek": 332944, "start": 3339.36, "end": 3345.04, "text": " model. I
  don''t know if that''s for everybody, but I think it''s, in a way, that''s the future.",
  "tokens": [50860, 2316, 13, 286, 500, 380, 458, 498, 300, 311, 337, 2201, 11, 457,
  286, 519, 309, 311, 11, 294, 257, 636, 11, 300, 311, 264, 2027, 13, 51144], "temperature":
  0.0, "avg_logprob": -0.12125456919435595, "compression_ratio": 1.6421052631578947,
  "no_speech_prob": 0.0020573094952851534}, {"id": 553, "seek": 332944, "start": 3346.16,
  "end": 3350.4, "text": " Right, we shouldn''t have to ask when going to a search
  box takes time, and then I still have to parse it.", "tokens": [51200, 1779, 11,
  321, 4659, 380, 362, 281, 1029, 562, 516, 281, 257, 3164, 2424, 2516, 565, 11, 293,
  550, 286, 920, 362, 281, 48377, 309, 13, 51412], "temperature": 0.0, "avg_logprob":
  -0.12125456919435595, "compression_ratio": 1.6421052631578947, "no_speech_prob":
  0.0020573094952851534}, {"id": 554, "seek": 332944, "start": 3351.44, "end": 3356.0,
  "text": " Depending on what you know, Swirl doesn''t do any profiling or anything
  like that,", "tokens": [51464, 22539, 322, 437, 291, 458, 11, 3926, 1648, 1177,
  380, 360, 604, 1740, 4883, 420, 1340, 411, 300, 11, 51692], "temperature": 0.0,
  "avg_logprob": -0.12125456919435595, "compression_ratio": 1.6421052631578947, "no_speech_prob":
  0.0020573094952851534}, {"id": 555, "seek": 335600, "start": 3356.0, "end": 3360.4,
  "text": " depending on what you know, you''re the builder of search apps, right,
  or inside apps.", "tokens": [50364, 5413, 322, 437, 291, 458, 11, 291, 434, 264,
  27377, 295, 3164, 7733, 11, 558, 11, 420, 1854, 7733, 13, 50584], "temperature":
  0.0, "avg_logprob": -0.13668978460903825, "compression_ratio": 1.7746913580246915,
  "no_speech_prob": 0.0021033899392932653}, {"id": 556, "seek": 335600, "start": 3361.6,
  "end": 3366.16, "text": " You should be able to target them, but the barrier is
  usually not what we know about the user,", "tokens": [50644, 509, 820, 312, 1075,
  281, 3779, 552, 11, 457, 264, 13357, 307, 2673, 406, 437, 321, 458, 466, 264, 4195,
  11, 50872], "temperature": 0.0, "avg_logprob": -0.13668978460903825, "compression_ratio":
  1.7746913580246915, "no_speech_prob": 0.0021033899392932653}, {"id": 557, "seek":
  335600, "start": 3366.16, "end": 3371.04, "text": " right? Since they''re an employee,
  we might have skill knowledge about them, right? We probably have", "tokens": [50872,
  558, 30, 4162, 436, 434, 364, 10738, 11, 321, 1062, 362, 5389, 3601, 466, 552, 11,
  558, 30, 492, 1391, 362, 51116], "temperature": 0.0, "avg_logprob": -0.13668978460903825,
  "compression_ratio": 1.7746913580246915, "no_speech_prob": 0.0021033899392932653},
  {"id": 558, "seek": 335600, "start": 3371.04, "end": 3376.32, "text": " access in
  theory to some other information about their job function and department and who
  they", "tokens": [51116, 2105, 294, 5261, 281, 512, 661, 1589, 466, 641, 1691, 2445,
  293, 5882, 293, 567, 436, 51380], "temperature": 0.0, "avg_logprob": -0.13668978460903825,
  "compression_ratio": 1.7746913580246915, "no_speech_prob": 0.0021033899392932653},
  {"id": 559, "seek": 335600, "start": 3376.32, "end": 3381.12, "text": " talk to.
  So it shouldn''t be that hard, but the problem isn''t knowing that stuff. The problem
  is", "tokens": [51380, 751, 281, 13, 407, 309, 4659, 380, 312, 300, 1152, 11, 457,
  264, 1154, 1943, 380, 5276, 300, 1507, 13, 440, 1154, 307, 51620], "temperature":
  0.0, "avg_logprob": -0.13668978460903825, "compression_ratio": 1.7746913580246915,
  "no_speech_prob": 0.0021033899392932653}, {"id": 560, "seek": 335600, "start": 3381.12,
  "end": 3385.44, "text": " saying, okay, well, how do I get content, right? How do
  I get that out? So again, hook it up to Swirl.", "tokens": [51620, 1566, 11, 1392,
  11, 731, 11, 577, 360, 286, 483, 2701, 11, 558, 30, 1012, 360, 286, 483, 300, 484,
  30, 407, 797, 11, 6328, 309, 493, 281, 3926, 1648, 13, 51836], "temperature": 0.0,
  "avg_logprob": -0.13668978460903825, "compression_ratio": 1.7746913580246915, "no_speech_prob":
  0.0021033899392932653}, {"id": 561, "seek": 338600, "start": 3386.24, "end": 3391.92,
  "text": " Build a watch list, which can be essentially a group of queries or set
  of search objects with", "tokens": [50376, 11875, 257, 1159, 1329, 11, 597, 393,
  312, 4476, 257, 1594, 295, 24109, 420, 992, 295, 3164, 6565, 365, 50660], "temperature":
  0.0, "avg_logprob": -0.11151714492262456, "compression_ratio": 1.7321428571428572,
  "no_speech_prob": 0.0031236843205988407}, {"id": 562, "seek": 338600, "start": 3391.92,
  "end": 3397.12, "text": " the subscribe function turned on, you know, for a bunch
  of topics, push that data out to the people", "tokens": [50660, 264, 3022, 2445,
  3574, 322, 11, 291, 458, 11, 337, 257, 3840, 295, 8378, 11, 2944, 300, 1412, 484,
  281, 264, 561, 50920], "temperature": 0.0, "avg_logprob": -0.11151714492262456,
  "compression_ratio": 1.7321428571428572, "no_speech_prob": 0.0031236843205988407},
  {"id": 563, "seek": 338600, "start": 3397.12, "end": 3401.6, "text": " who need
  to know, create groups, use service accounts to search as opposed to using individual",
  "tokens": [50920, 567, 643, 281, 458, 11, 1884, 3935, 11, 764, 2643, 9402, 281,
  3164, 382, 8851, 281, 1228, 2609, 51144], "temperature": 0.0, "avg_logprob": -0.11151714492262456,
  "compression_ratio": 1.7321428571428572, "no_speech_prob": 0.0031236843205988407},
  {"id": 564, "seek": 338600, "start": 3401.6, "end": 3407.84, "text": " users, right?
  Targeting individual users, not super valuable for proactive delivery, but on a
  group", "tokens": [51144, 5022, 11, 558, 30, 24586, 278, 2609, 5022, 11, 406, 1687,
  8263, 337, 28028, 8982, 11, 457, 322, 257, 1594, 51456], "temperature": 0.0, "avg_logprob":
  -0.11151714492262456, "compression_ratio": 1.7321428571428572, "no_speech_prob":
  0.0031236843205988407}, {"id": 565, "seek": 338600, "start": 3407.84, "end": 3414.72,
  "text": " basis, very valuable. So tell, right, create an industry feed that, you
  know, if you really know", "tokens": [51456, 5143, 11, 588, 8263, 13, 407, 980,
  11, 558, 11, 1884, 364, 3518, 3154, 300, 11, 291, 458, 11, 498, 291, 534, 458, 51800],
  "temperature": 0.0, "avg_logprob": -0.11151714492262456, "compression_ratio": 1.7321428571428572,
  "no_speech_prob": 0.0031236843205988407}, {"id": 566, "seek": 341472, "start": 3414.72,
  "end": 3420.3999999999996, "text": " where to get the best industry data, why not
  make that systematic? Why not make that data available", "tokens": [50364, 689,
  281, 483, 264, 1151, 3518, 1412, 11, 983, 406, 652, 300, 27249, 30, 1545, 406, 652,
  300, 1412, 2435, 50648], "temperature": 0.0, "avg_logprob": -0.1317386465557551,
  "compression_ratio": 1.7298245614035088, "no_speech_prob": 0.0063559189438819885},
  {"id": 567, "seek": 341472, "start": 3420.3999999999996, "end": 3424.08, "text":
  " to everybody who''s out there trying to talk to those folks through whatever,
  through their mobile?", "tokens": [50648, 281, 2201, 567, 311, 484, 456, 1382, 281,
  751, 281, 729, 4024, 807, 2035, 11, 807, 641, 6013, 30, 50832], "temperature": 0.0,
  "avg_logprob": -0.1317386465557551, "compression_ratio": 1.7298245614035088, "no_speech_prob":
  0.0063559189438819885}, {"id": 568, "seek": 341472, "start": 3424.7999999999997,
  "end": 3428.3999999999996, "text": " And this is a thing like trying to do end-to-end
  enterprise search is super hard. You got to", "tokens": [50868, 400, 341, 307, 257,
  551, 411, 1382, 281, 360, 917, 12, 1353, 12, 521, 14132, 3164, 307, 1687, 1152,
  13, 509, 658, 281, 51048], "temperature": 0.0, "avg_logprob": -0.1317386465557551,
  "compression_ratio": 1.7298245614035088, "no_speech_prob": 0.0063559189438819885},
  {"id": 569, "seek": 341472, "start": 3428.3999999999996, "end": 3432.64, "text":
  " get people to adopt your solution. Why would what do you want my mobile app for?
  You probably already", "tokens": [51048, 483, 561, 281, 6878, 428, 3827, 13, 1545,
  576, 437, 360, 291, 528, 452, 6013, 724, 337, 30, 509, 1391, 1217, 51260], "temperature":
  0.0, "avg_logprob": -0.1317386465557551, "compression_ratio": 1.7298245614035088,
  "no_speech_prob": 0.0063559189438819885}, {"id": 570, "seek": 341472, "start": 3432.64,
  "end": 3437.8399999999997, "text": " have a cool one. You might already have five.
  So it''s all about just putting that data out there so", "tokens": [51260, 362,
  257, 1627, 472, 13, 509, 1062, 1217, 362, 1732, 13, 407, 309, 311, 439, 466, 445,
  3372, 300, 1412, 484, 456, 370, 51520], "temperature": 0.0, "avg_logprob": -0.1317386465557551,
  "compression_ratio": 1.7298245614035088, "no_speech_prob": 0.0063559189438819885},
  {"id": 571, "seek": 343784, "start": 3437.84, "end": 3443.92, "text": " people can
  keep building fast. That''s it. Yeah, this is amazing. I mean, you", "tokens": [50364,
  561, 393, 1066, 2390, 2370, 13, 663, 311, 309, 13, 865, 11, 341, 307, 2243, 13,
  286, 914, 11, 291, 50668], "temperature": 0.0, "avg_logprob": -0.1939904530843099,
  "compression_ratio": 1.6904761904761905, "no_speech_prob": 0.0061910031363368034},
  {"id": 572, "seek": 343784, "start": 3445.04, "end": 3451.28, "text": " you simplified
  a lot in how you presented, you simplified a lot and you solved so many", "tokens":
  [50724, 291, 26335, 257, 688, 294, 577, 291, 8212, 11, 291, 26335, 257, 688, 293,
  291, 13041, 370, 867, 51036], "temperature": 0.0, "avg_logprob": -0.1939904530843099,
  "compression_ratio": 1.6904761904761905, "no_speech_prob": 0.0061910031363368034},
  {"id": 573, "seek": 343784, "start": 3452.56, "end": 3459.04, "text": " edge case,
  like not edge case, but like this really challenging things that are like showstoppers",
  "tokens": [51100, 4691, 1389, 11, 411, 406, 4691, 1389, 11, 457, 411, 341, 534,
  7595, 721, 300, 366, 411, 855, 13559, 21819, 51424], "temperature": 0.0, "avg_logprob":
  -0.1939904530843099, "compression_ratio": 1.6904761904761905, "no_speech_prob":
  0.0061910031363368034}, {"id": 574, "seek": 343784, "start": 3459.04, "end": 3463.84,
  "text": " sometimes, you know, like, okay, I have this existing search demo app
  or something, you know,", "tokens": [51424, 2171, 11, 291, 458, 11, 411, 11, 1392,
  11, 286, 362, 341, 6741, 3164, 10723, 724, 420, 746, 11, 291, 458, 11, 51664], "temperature":
  0.0, "avg_logprob": -0.1939904530843099, "compression_ratio": 1.6904761904761905,
  "no_speech_prob": 0.0061910031363368034}, {"id": 575, "seek": 346384, "start": 3463.84,
  "end": 3471.6000000000004, "text": " it''s used within my department. I just want
  to add one data source. Now, what do I do, right?", "tokens": [50364, 309, 311,
  1143, 1951, 452, 5882, 13, 286, 445, 528, 281, 909, 472, 1412, 4009, 13, 823, 11,
  437, 360, 286, 360, 11, 558, 30, 50752], "temperature": 0.0, "avg_logprob": -0.15803291247441217,
  "compression_ratio": 1.6394849785407726, "no_speech_prob": 0.00521750608459115},
  {"id": 576, "seek": 346384, "start": 3471.6000000000004, "end": 3476.4, "text":
  " Do I really need to change my UI? Do I really need to rewrite the back end and
  things like that?", "tokens": [50752, 1144, 286, 534, 643, 281, 1319, 452, 15682,
  30, 1144, 286, 534, 643, 281, 28132, 264, 646, 917, 293, 721, 411, 300, 30, 50992],
  "temperature": 0.0, "avg_logprob": -0.15803291247441217, "compression_ratio": 1.6394849785407726,
  "no_speech_prob": 0.00521750608459115}, {"id": 577, "seek": 346384, "start": 3476.4,
  "end": 3484.96, "text": " And so I could actually, when I introduce swirl, will
  it actually precede every search back end", "tokens": [50992, 400, 370, 286, 727,
  767, 11, 562, 286, 5366, 30310, 11, 486, 309, 767, 16969, 68, 633, 3164, 646, 917,
  51420], "temperature": 0.0, "avg_logprob": -0.15803291247441217, "compression_ratio":
  1.6394849785407726, "no_speech_prob": 0.00521750608459115}, {"id": 578, "seek":
  346384, "start": 3484.96, "end": 3493.28, "text": " call between UI and the search
  back end? That''s how I do it now. And like, we''re setting it up.", "tokens": [51420,
  818, 1296, 15682, 293, 264, 3164, 646, 917, 30, 663, 311, 577, 286, 360, 309, 586,
  13, 400, 411, 11, 321, 434, 3287, 309, 493, 13, 51836], "temperature": 0.0, "avg_logprob":
  -0.15803291247441217, "compression_ratio": 1.6394849785407726, "no_speech_prob":
  0.00521750608459115}, {"id": 579, "seek": 349328, "start": 3493.28, "end": 3499.92,
  "text": " We use it internally and that''s the way to do it rather than querying
  an index,", "tokens": [50364, 492, 764, 309, 19501, 293, 300, 311, 264, 636, 281,
  360, 309, 2831, 813, 7083, 1840, 364, 8186, 11, 50696], "temperature": 0.0, "avg_logprob":
  -0.18405945833064308, "compression_ratio": 1.6774193548387097, "no_speech_prob":
  0.0009623169898986816}, {"id": 580, "seek": 349328, "start": 3500.6400000000003,
  "end": 3505.36, "text": " you know, and then create just queries world and have
  it query all of those things. And what you", "tokens": [50732, 291, 458, 11, 293,
  550, 1884, 445, 24109, 1002, 293, 362, 309, 14581, 439, 295, 729, 721, 13, 400,
  437, 291, 50968], "temperature": 0.0, "avg_logprob": -0.18405945833064308, "compression_ratio":
  1.6774193548387097, "no_speech_prob": 0.0009623169898986816}, {"id": 581, "seek":
  349328, "start": 3505.36, "end": 3511.2000000000003, "text": " get is the best results
  from across all sources. Now, that''s no substitute though, right, from going",
  "tokens": [50968, 483, 307, 264, 1151, 3542, 490, 2108, 439, 7139, 13, 823, 11,
  300, 311, 572, 15802, 1673, 11, 558, 11, 490, 516, 51260], "temperature": 0.0, "avg_logprob":
  -0.18405945833064308, "compression_ratio": 1.6774193548387097, "no_speech_prob":
  0.0009623169898986816}, {"id": 582, "seek": 349328, "start": 3511.2000000000003,
  "end": 3515.6800000000003, "text": " into the silo. Sometimes you need to go into
  the silo. They have in addition to a great search API", "tokens": [51260, 666, 264,
  3425, 78, 13, 4803, 291, 643, 281, 352, 666, 264, 3425, 78, 13, 814, 362, 294, 4500,
  281, 257, 869, 3164, 9362, 51484], "temperature": 0.0, "avg_logprob": -0.18405945833064308,
  "compression_ratio": 1.6774193548387097, "no_speech_prob": 0.0009623169898986816},
  {"id": 583, "seek": 349328, "start": 3516.2400000000002, "end": 3521.76, "text":
  " and a lot of business logic right on their side, like query synums. There''s a
  lot more. You", "tokens": [51512, 293, 257, 688, 295, 1606, 9952, 558, 322, 641,
  1252, 11, 411, 14581, 5451, 8099, 13, 821, 311, 257, 688, 544, 13, 509, 51788],
  "temperature": 0.0, "avg_logprob": -0.18405945833064308, "compression_ratio": 1.6774193548387097,
  "no_speech_prob": 0.0009623169898986816}, {"id": 584, "seek": 352176, "start": 3521.76,
  "end": 3527.36, "text": " probably want to view the object in their environment
  versus in swirl, we can create a copy of it or", "tokens": [50364, 1391, 528, 281,
  1910, 264, 2657, 294, 641, 2823, 5717, 294, 30310, 11, 321, 393, 1884, 257, 5055,
  295, 309, 420, 50644], "temperature": 0.0, "avg_logprob": -0.13036083406017673,
  "compression_ratio": 1.6744186046511629, "no_speech_prob": 0.0013863056665286422},
  {"id": 585, "seek": 352176, "start": 3527.36, "end": 3532.48, "text": " whatever,
  like everybody else does. We don''t. If somebody wants to do preview, you know,
  there are so", "tokens": [50644, 2035, 11, 411, 2201, 1646, 775, 13, 492, 500, 380,
  13, 759, 2618, 2738, 281, 360, 14281, 11, 291, 458, 11, 456, 366, 370, 50900], "temperature":
  0.0, "avg_logprob": -0.13036083406017673, "compression_ratio": 1.6744186046511629,
  "no_speech_prob": 0.0013863056665286422}, {"id": 586, "seek": 352176, "start": 3532.48,
  "end": 3538.0, "text": " many technologies to do that, but why? Instead, take, I
  think the best thing to do is after the user has", "tokens": [50900, 867, 7943,
  281, 360, 300, 11, 457, 983, 30, 7156, 11, 747, 11, 286, 519, 264, 1151, 551, 281,
  360, 307, 934, 264, 4195, 575, 51176], "temperature": 0.0, "avg_logprob": -0.13036083406017673,
  "compression_ratio": 1.6744186046511629, "no_speech_prob": 0.0013863056665286422},
  {"id": 587, "seek": 352176, "start": 3538.0, "end": 3543.2000000000003, "text":
  " scanned the shallow results that swirl gives you immediately two, two, three seconds,
  that''s nothing", "tokens": [51176, 45089, 264, 20488, 3542, 300, 30310, 2709, 291,
  4258, 732, 11, 732, 11, 1045, 3949, 11, 300, 311, 1825, 51436], "temperature": 0.0,
  "avg_logprob": -0.13036083406017673, "compression_ratio": 1.6744186046511629, "no_speech_prob":
  0.0013863056665286422}, {"id": 588, "seek": 352176, "start": 3543.2000000000003,
  "end": 3547.5200000000004, "text": " compared to the time it takes to go to each
  silo. After you''ve done three silos, you''re already", "tokens": [51436, 5347,
  281, 264, 565, 309, 2516, 281, 352, 281, 1184, 3425, 78, 13, 2381, 291, 600, 1096,
  1045, 48893, 11, 291, 434, 1217, 51652], "temperature": 0.0, "avg_logprob": -0.13036083406017673,
  "compression_ratio": 1.6744186046511629, "no_speech_prob": 0.0013863056665286422},
  {"id": 589, "seek": 354752, "start": 3547.52, "end": 3552.32, "text": " way saving,
  right? But then say, okay, look, it''s obvious to me that the best results here
  are maybe", "tokens": [50364, 636, 6816, 11, 558, 30, 583, 550, 584, 11, 1392, 11,
  574, 11, 309, 311, 6322, 281, 385, 300, 264, 1151, 3542, 510, 366, 1310, 50604],
  "temperature": 0.0, "avg_logprob": -0.15086651611328125, "compression_ratio": 1.62,
  "no_speech_prob": 0.005448661744594574}, {"id": 590, "seek": 354752, "start": 3552.32,
  "end": 3557.36, "text": " in one drive in this folder or maybe it''s in this team''s
  chat or these teams chats. So now click,", "tokens": [50604, 294, 472, 3332, 294,
  341, 10820, 420, 1310, 309, 311, 294, 341, 1469, 311, 5081, 420, 613, 5491, 38057,
  13, 407, 586, 2052, 11, 50856], "temperature": 0.0, "avg_logprob": -0.15086651611328125,
  "compression_ratio": 1.62, "no_speech_prob": 0.005448661744594574}, {"id": 591,
  "seek": 354752, "start": 3557.84, "end": 3561.6, "text": " go into that environment
  and hopefully you can then, right, traverse the data and get what you", "tokens":
  [50880, 352, 666, 300, 2823, 293, 4696, 291, 393, 550, 11, 558, 11, 45674, 264,
  1412, 293, 483, 437, 291, 51068], "temperature": 0.0, "avg_logprob": -0.15086651611328125,
  "compression_ratio": 1.62, "no_speech_prob": 0.005448661744594574}, {"id": 592,
  "seek": 354752, "start": 3561.6, "end": 3569.2, "text": " actually need. And down
  the road, when those repositories are serving up answers, right? We have", "tokens":
  [51068, 767, 643, 13, 400, 760, 264, 3060, 11, 562, 729, 22283, 2083, 366, 8148,
  493, 6338, 11, 558, 30, 492, 362, 51448], "temperature": 0.0, "avg_logprob": -0.15086651611328125,
  "compression_ratio": 1.62, "no_speech_prob": 0.005448661744594574}, {"id": 593,
  "seek": 354752, "start": 3569.2, "end": 3575.04, "text": " mentioned chat, GPT much,
  but I assume you''ve seen the Microsoft co-pilot demo. How long before", "tokens":
  [51448, 2835, 5081, 11, 26039, 51, 709, 11, 457, 286, 6552, 291, 600, 1612, 264,
  8116, 598, 12, 79, 31516, 10723, 13, 1012, 938, 949, 51740], "temperature": 0.0,
  "avg_logprob": -0.15086651611328125, "compression_ratio": 1.62, "no_speech_prob":
  0.005448661744594574}, {"id": 594, "seek": 357504, "start": 3575.04, "end": 3578.72,
  "text": " that''s pushing the data back, as opposed to you asking for it, right?
  It''s saying, oh, here''s", "tokens": [50364, 300, 311, 7380, 264, 1412, 646, 11,
  382, 8851, 281, 291, 3365, 337, 309, 11, 558, 30, 467, 311, 1566, 11, 1954, 11,
  510, 311, 50548], "temperature": 0.0, "avg_logprob": -0.11402137162255459, "compression_ratio":
  1.6909722222222223, "no_speech_prob": 0.003813371295109391}, {"id": 595, "seek":
  357504, "start": 3578.72, "end": 3584.16, "text": " the summary you need today.
  If you knew what to tell it, it could probably do that for you. So I", "tokens":
  [50548, 264, 12691, 291, 643, 965, 13, 759, 291, 2586, 437, 281, 980, 309, 11, 309,
  727, 1391, 360, 300, 337, 291, 13, 407, 286, 50820], "temperature": 0.0, "avg_logprob":
  -0.11402137162255459, "compression_ratio": 1.6909722222222223, "no_speech_prob":
  0.003813371295109391}, {"id": 596, "seek": 357504, "start": 3584.16, "end": 3589.84,
  "text": " think that''s the new landscape. The much more important thing than the
  one search box to rule them all", "tokens": [50820, 519, 300, 311, 264, 777, 9661,
  13, 440, 709, 544, 1021, 551, 813, 264, 472, 3164, 2424, 281, 4978, 552, 439, 51104],
  "temperature": 0.0, "avg_logprob": -0.11402137162255459, "compression_ratio": 1.6909722222222223,
  "no_speech_prob": 0.003813371295109391}, {"id": 597, "seek": 357504, "start": 3589.84,
  "end": 3594.72, "text": " is to use the power of meta-search to connect systems
  together and deliver information to the stuff", "tokens": [51104, 307, 281, 764,
  264, 1347, 295, 19616, 12, 405, 1178, 281, 1745, 3652, 1214, 293, 4239, 1589, 281,
  264, 1507, 51348], "temperature": 0.0, "avg_logprob": -0.11402137162255459, "compression_ratio":
  1.6909722222222223, "no_speech_prob": 0.003813371295109391}, {"id": 598, "seek":
  357504, "start": 3594.72, "end": 3601.2, "text": " you have already, to the workflows
  that work and make value already. Whether that''s Slack or,", "tokens": [51348,
  291, 362, 1217, 11, 281, 264, 43461, 300, 589, 293, 652, 2158, 1217, 13, 8503, 300,
  311, 37211, 420, 11, 51672], "temperature": 0.0, "avg_logprob": -0.11402137162255459,
  "compression_ratio": 1.6909722222222223, "no_speech_prob": 0.003813371295109391},
  {"id": 599, "seek": 360120, "start": 3602.0, "end": 3608.64, "text": " a newsletter
  or a notification to a Salesforce queue, that''s the what you should do. The world",
  "tokens": [50404, 257, 26469, 420, 257, 11554, 281, 257, 40398, 18639, 11, 300,
  311, 264, 437, 291, 820, 360, 13, 440, 1002, 50736], "temperature": 0.0, "avg_logprob":
  -0.20692779620488486, "compression_ratio": 1.6302521008403361, "no_speech_prob":
  0.010704675689339638}, {"id": 600, "seek": 360120, "start": 3608.64, "end": 3616.24,
  "text": " doesn''t need another search you are. Yeah, especially like today, I saw
  a message on Slack for one", "tokens": [50736, 1177, 380, 643, 1071, 3164, 291,
  366, 13, 865, 11, 2318, 411, 965, 11, 286, 1866, 257, 3636, 322, 37211, 337, 472,
  51116], "temperature": 0.0, "avg_logprob": -0.20692779620488486, "compression_ratio":
  1.6302521008403361, "no_speech_prob": 0.010704675689339638}, {"id": 601, "seek":
  360120, "start": 3616.24, "end": 3624.08, "text": " of the senior managers saying,
  hey, what''s the password to this thing? And I can imagine that", "tokens": [51116,
  295, 264, 7965, 14084, 1566, 11, 4177, 11, 437, 311, 264, 11524, 281, 341, 551,
  30, 400, 286, 393, 3811, 300, 51508], "temperature": 0.0, "avg_logprob": -0.20692779620488486,
  "compression_ratio": 1.6302521008403361, "no_speech_prob": 0.010704675689339638},
  {"id": 602, "seek": 360120, "start": 3624.08, "end": 3630.64, "text": " in the business
  schedules, you know, they don''t have access, they don''t have the password right
  now,", "tokens": [51508, 294, 264, 1606, 28078, 11, 291, 458, 11, 436, 500, 380,
  362, 2105, 11, 436, 500, 380, 362, 264, 11524, 558, 586, 11, 51836], "temperature":
  0.0, "avg_logprob": -0.20692779620488486, "compression_ratio": 1.6302521008403361,
  "no_speech_prob": 0.010704675689339638}, {"id": 603, "seek": 363064, "start": 3630.64,
  "end": 3635.3599999999997, "text": " they will switch to another topic, but maybe
  this topic was still important and maybe even one", "tokens": [50364, 436, 486,
  3679, 281, 1071, 4829, 11, 457, 1310, 341, 4829, 390, 920, 1021, 293, 1310, 754,
  472, 50600], "temperature": 0.0, "avg_logprob": -0.09891825850291919, "compression_ratio":
  1.676595744680851, "no_speech_prob": 0.0022112398874014616}, {"id": 604, "seek":
  363064, "start": 3635.3599999999997, "end": 3642.08, "text": " important, but they
  just don''t want to wait. And what you say is that in principle, they could have",
  "tokens": [50600, 1021, 11, 457, 436, 445, 500, 380, 528, 281, 1699, 13, 400, 437,
  291, 584, 307, 300, 294, 8665, 11, 436, 727, 362, 50936], "temperature": 0.0, "avg_logprob":
  -0.09891825850291919, "compression_ratio": 1.676595744680851, "no_speech_prob":
  0.0022112398874014616}, {"id": 605, "seek": 363064, "start": 3642.08, "end": 3654.0,
  "text": " configured it once and access it as many times as they need. Exactly.
  Exactly. And it''s not uncommon in", "tokens": [50936, 30538, 309, 1564, 293, 2105,
  309, 382, 867, 1413, 382, 436, 643, 13, 7587, 13, 7587, 13, 400, 309, 311, 406,
  29289, 294, 51532], "temperature": 0.0, "avg_logprob": -0.09891825850291919, "compression_ratio":
  1.676595744680851, "no_speech_prob": 0.0022112398874014616}, {"id": 606, "seek":
  363064, "start": 3654.0, "end": 3659.7599999999998, "text": " the world of, you
  know, consulting, strategic consulting, tech strategy, that the most powerful",
  "tokens": [51532, 264, 1002, 295, 11, 291, 458, 11, 23682, 11, 10924, 23682, 11,
  7553, 5206, 11, 300, 264, 881, 4005, 51820], "temperature": 0.0, "avg_logprob":
  -0.09891825850291919, "compression_ratio": 1.676595744680851, "no_speech_prob":
  0.0022112398874014616}, {"id": 607, "seek": 365976, "start": 3659.76, "end": 3666.6400000000003,
  "text": " people are analysts and admins because, you know, partners are very busy,
  right, talking to and", "tokens": [50364, 561, 366, 31388, 293, 5910, 1292, 570,
  11, 291, 458, 11, 4462, 366, 588, 5856, 11, 558, 11, 1417, 281, 293, 50708], "temperature":
  0.0, "avg_logprob": -0.12218938271204631, "compression_ratio": 1.5617529880478087,
  "no_speech_prob": 0.0026510958559811115}, {"id": 608, "seek": 365976, "start": 3666.6400000000003,
  "end": 3673.0400000000004, "text": " solving client problems and finding new ones.
  So they rely on those folks to have access to all the", "tokens": [50708, 12606,
  6423, 2740, 293, 5006, 777, 2306, 13, 407, 436, 10687, 322, 729, 4024, 281, 362,
  2105, 281, 439, 264, 51028], "temperature": 0.0, "avg_logprob": -0.12218938271204631,
  "compression_ratio": 1.5617529880478087, "no_speech_prob": 0.0026510958559811115},
  {"id": 609, "seek": 365976, "start": 3673.0400000000004, "end": 3679.5200000000004,
  "text": " systems and to go scour them. And of course, that''s a waste, right? Probably
  nobody loves scouring", "tokens": [51028, 3652, 293, 281, 352, 795, 396, 552, 13,
  400, 295, 1164, 11, 300, 311, 257, 5964, 11, 558, 30, 9210, 5079, 6752, 795, 40510,
  51352], "temperature": 0.0, "avg_logprob": -0.12218938271204631, "compression_ratio":
  1.5617529880478087, "no_speech_prob": 0.0026510958559811115}, {"id": 610, "seek":
  365976, "start": 3679.5200000000004, "end": 3686.96, "text": " those silos, but
  even more, we cannot be 100% systematic all the time. But with technologies like",
  "tokens": [51352, 729, 48893, 11, 457, 754, 544, 11, 321, 2644, 312, 2319, 4, 27249,
  439, 264, 565, 13, 583, 365, 7943, 411, 51724], "temperature": 0.0, "avg_logprob":
  -0.12218938271204631, "compression_ratio": 1.5617529880478087, "no_speech_prob":
  0.0026510958559811115}, {"id": 611, "seek": 368696, "start": 3686.96, "end": 3691.68,
  "text": " meta-search and push technologies and there''s a million things you could
  use and there''s a million", "tokens": [50364, 19616, 12, 405, 1178, 293, 2944,
  7943, 293, 456, 311, 257, 2459, 721, 291, 727, 764, 293, 456, 311, 257, 2459, 50600],
  "temperature": 0.0, "avg_logprob": -0.1458443986608627, "compression_ratio": 1.6909871244635193,
  "no_speech_prob": 0.003051463281735778}, {"id": 612, "seek": 368696, "start": 3691.68,
  "end": 3698.96, "text": " ways to deliver those things, the opportunity is really
  there to let those people work on something", "tokens": [50600, 2098, 281, 4239,
  729, 721, 11, 264, 2650, 307, 534, 456, 281, 718, 729, 561, 589, 322, 746, 50964],
  "temperature": 0.0, "avg_logprob": -0.1458443986608627, "compression_ratio": 1.6909871244635193,
  "no_speech_prob": 0.003051463281735778}, {"id": 613, "seek": 368696, "start": 3698.96,
  "end": 3703.84, "text": " else, right, to create value in other ways and not just
  be scouring it for everything that''s relevant,", "tokens": [50964, 1646, 11, 558,
  11, 281, 1884, 2158, 294, 661, 2098, 293, 406, 445, 312, 795, 40510, 309, 337, 1203,
  300, 311, 7340, 11, 51208], "temperature": 0.0, "avg_logprob": -0.1458443986608627,
  "compression_ratio": 1.6909871244635193, "no_speech_prob": 0.003051463281735778},
  {"id": 614, "seek": 368696, "start": 3703.84, "end": 3711.44, "text": " for every,
  you know, give the best chance. Yeah, absolutely. And how do you view the problem",
  "tokens": [51208, 337, 633, 11, 291, 458, 11, 976, 264, 1151, 2931, 13, 865, 11,
  3122, 13, 400, 577, 360, 291, 1910, 264, 1154, 51588], "temperature": 0.0, "avg_logprob":
  -0.1458443986608627, "compression_ratio": 1.6909871244635193, "no_speech_prob":
  0.003051463281735778}, {"id": 615, "seek": 371144, "start": 3712.2400000000002,
  "end": 3718.48, "text": " of, or do you think it''s a problem at all, of evolving
  such a search engine, you know, like,", "tokens": [50404, 295, 11, 420, 360, 291,
  519, 309, 311, 257, 1154, 412, 439, 11, 295, 21085, 1270, 257, 3164, 2848, 11, 291,
  458, 11, 411, 11, 50716], "temperature": 0.0, "avg_logprob": -0.20866667506206465,
  "compression_ratio": 1.5509259259259258, "no_speech_prob": 0.009355876594781876},
  {"id": 616, "seek": 371144, "start": 3719.36, "end": 3727.04, "text": " if, if I
  have the main experts who could actually label results for me for these queries,",
  "tokens": [50760, 498, 11, 498, 286, 362, 264, 2135, 8572, 567, 727, 767, 7645,
  3542, 337, 385, 337, 613, 24109, 11, 51144], "temperature": 0.0, "avg_logprob":
  -0.20866667506206465, "compression_ratio": 1.5509259259259258, "no_speech_prob":
  0.009355876594781876}, {"id": 617, "seek": 371144, "start": 3727.84, "end": 3732.56,
  "text": " could I somehow integrate this into the process with swirl?", "tokens":
  [51184, 727, 286, 6063, 13365, 341, 666, 264, 1399, 365, 30310, 30, 51420], "temperature":
  0.0, "avg_logprob": -0.20866667506206465, "compression_ratio": 1.5509259259259258,
  "no_speech_prob": 0.009355876594781876}, {"id": 618, "seek": 371144, "start": 3733.6,
  "end": 3740.32, "text": " Absolutely. So that brings me actually nice lead into
  the third use case that the people are", "tokens": [51472, 7021, 13, 407, 300, 5607,
  385, 767, 1481, 1477, 666, 264, 2636, 764, 1389, 300, 264, 561, 366, 51808], "temperature":
  0.0, "avg_logprob": -0.20866667506206465, "compression_ratio": 1.5509259259259258,
  "no_speech_prob": 0.009355876594781876}, {"id": 619, "seek": 374032, "start": 3740.32,
  "end": 3746.48, "text": " starting to look at with swirl. So exactly what you said,
  maybe I''m trying to build the chat GPT", "tokens": [50364, 2891, 281, 574, 412,
  365, 30310, 13, 407, 2293, 437, 291, 848, 11, 1310, 286, 478, 1382, 281, 1322, 264,
  5081, 26039, 51, 50672], "temperature": 0.0, "avg_logprob": -0.12266995587686855,
  "compression_ratio": 1.6838487972508591, "no_speech_prob": 0.00021481956355273724},
  {"id": 620, "seek": 374032, "start": 3746.48, "end": 3750.96, "text": " of my business,
  okay, maybe it doesn''t even have to be that, maybe it has to be something,", "tokens":
  [50672, 295, 452, 1606, 11, 1392, 11, 1310, 309, 1177, 380, 754, 362, 281, 312,
  300, 11, 1310, 309, 575, 281, 312, 746, 11, 50896], "temperature": 0.0, "avg_logprob":
  -0.12266995587686855, "compression_ratio": 1.6838487972508591, "no_speech_prob":
  0.00021481956355273724}, {"id": 621, "seek": 374032, "start": 3750.96, "end": 3757.28,
  "text": " even a simpler version. How would I automate handling of an exception
  when processing a mortgage,", "tokens": [50896, 754, 257, 18587, 3037, 13, 1012,
  576, 286, 31605, 13175, 295, 364, 11183, 562, 9007, 257, 20236, 11, 51212], "temperature":
  0.0, "avg_logprob": -0.12266995587686855, "compression_ratio": 1.6838487972508591,
  "no_speech_prob": 0.00021481956355273724}, {"id": 622, "seek": 374032, "start":
  3757.28, "end": 3762.88, "text": " as an example? How could I automate that? That''s
  really hard. That is probably not a rules-based system.", "tokens": [51212, 382,
  364, 1365, 30, 1012, 727, 286, 31605, 300, 30, 663, 311, 534, 1152, 13, 663, 307,
  1391, 406, 257, 4474, 12, 6032, 1185, 13, 51492], "temperature": 0.0, "avg_logprob":
  -0.12266995587686855, "compression_ratio": 1.6838487972508591, "no_speech_prob":
  0.00021481956355273724}, {"id": 623, "seek": 374032, "start": 3763.84, "end": 3768.8,
  "text": " But it''s exactly what you said. I need labels, right? So you''re going
  to have your humans go scour,", "tokens": [51540, 583, 309, 311, 2293, 437, 291,
  848, 13, 286, 643, 16949, 11, 558, 30, 407, 291, 434, 516, 281, 362, 428, 6255,
  352, 795, 396, 11, 51788], "temperature": 0.0, "avg_logprob": -0.12266995587686855,
  "compression_ratio": 1.6838487972508591, "no_speech_prob": 0.00021481956355273724},
  {"id": 624, "seek": 376880, "start": 3769.6000000000004, "end": 3774.8, "text":
  " whatever, the various locations slack and teams and various products. And hopefully
  they find", "tokens": [50404, 2035, 11, 264, 3683, 9253, 29767, 293, 5491, 293,
  3683, 3383, 13, 400, 4696, 436, 915, 50664], "temperature": 0.0, "avg_logprob":
  -0.14234038073607166, "compression_ratio": 1.634453781512605, "no_speech_prob":
  0.0040127853862941265}, {"id": 625, "seek": 376880, "start": 3774.8, "end": 3780.6400000000003,
  "text": " them and they label them. Why not use MetaSearch for that? So if you can
  MetaSearch those things and use", "tokens": [50664, 552, 293, 436, 7645, 552, 13,
  1545, 406, 764, 6377, 64, 10637, 1178, 337, 300, 30, 407, 498, 291, 393, 6377, 64,
  10637, 1178, 729, 721, 293, 764, 50956], "temperature": 0.0, "avg_logprob": -0.14234038073607166,
  "compression_ratio": 1.634453781512605, "no_speech_prob": 0.0040127853862941265},
  {"id": 626, "seek": 376880, "start": 3780.6400000000003, "end": 3786.96, "text":
  " the language model, right, to basically say, I''m going to label anything over
  a certain score", "tokens": [50956, 264, 2856, 2316, 11, 558, 11, 281, 1936, 584,
  11, 286, 478, 516, 281, 7645, 1340, 670, 257, 1629, 6175, 51272], "temperature":
  0.0, "avg_logprob": -0.14234038073607166, "compression_ratio": 1.634453781512605,
  "no_speech_prob": 0.0040127853862941265}, {"id": 627, "seek": 376880, "start": 3787.6800000000003,
  "end": 3792.6400000000003, "text": " as being about this thing, then I give it a
  bunch of labels, let it hit, get a bunch of targets,", "tokens": [51308, 382, 885,
  466, 341, 551, 11, 550, 286, 976, 309, 257, 3840, 295, 16949, 11, 718, 309, 2045,
  11, 483, 257, 3840, 295, 12911, 11, 51556], "temperature": 0.0, "avg_logprob": -0.14234038073607166,
  "compression_ratio": 1.634453781512605, "no_speech_prob": 0.0040127853862941265},
  {"id": 628, "seek": 379264, "start": 3792.64, "end": 3797.68, "text": " let it go,
  find those things, hold the documents, because you will need the documents.", "tokens":
  [50364, 718, 309, 352, 11, 915, 729, 721, 11, 1797, 264, 8512, 11, 570, 291, 486,
  643, 264, 8512, 13, 50616], "temperature": 0.0, "avg_logprob": -0.14220977056594122,
  "compression_ratio": 1.829875518672199, "no_speech_prob": 0.0009466343908570707},
  {"id": 629, "seek": 379264, "start": 3798.56, "end": 3804.3199999999997, "text":
  " The difficulty of pulling documents compared to searching documents in M365 is
  one permission.", "tokens": [50660, 440, 10360, 295, 8407, 8512, 5347, 281, 10808,
  8512, 294, 376, 11309, 20, 307, 472, 11226, 13, 50948], "temperature": 0.0, "avg_logprob":
  -0.14220977056594122, "compression_ratio": 1.829875518672199, "no_speech_prob":
  0.0009466343908570707}, {"id": 630, "seek": 379264, "start": 3805.52, "end": 3810.3199999999997,
  "text": " So we are today, right, if you install swirl against M365, against your
  tenant,", "tokens": [51008, 407, 321, 366, 965, 11, 558, 11, 498, 291, 3625, 30310,
  1970, 376, 11309, 20, 11, 1970, 428, 31000, 11, 51248], "temperature": 0.0, "avg_logprob":
  -0.14220977056594122, "compression_ratio": 1.829875518672199, "no_speech_prob":
  0.0009466343908570707}, {"id": 631, "seek": 379264, "start": 3810.3199999999997,
  "end": 3816.3199999999997, "text": " you are granting permission for swirl on behalf
  of some user, right, to search through the one", "tokens": [51248, 291, 366, 50204,
  11226, 337, 30310, 322, 9490, 295, 512, 4195, 11, 558, 11, 281, 3164, 807, 264,
  472, 51548], "temperature": 0.0, "avg_logprob": -0.14220977056594122, "compression_ratio":
  1.829875518672199, "no_speech_prob": 0.0009466343908570707}, {"id": 632, "seek":
  379264, "start": 3816.3199999999997, "end": 3822.3199999999997, "text": " drive
  files. So you could also give a permission to fetch those files. So use swirl,",
  "tokens": [51548, 3332, 7098, 13, 407, 291, 727, 611, 976, 257, 11226, 281, 23673,
  729, 7098, 13, 407, 764, 30310, 11, 51848], "temperature": 0.0, "avg_logprob": -0.14220977056594122,
  "compression_ratio": 1.829875518672199, "no_speech_prob": 0.0009466343908570707},
  {"id": 633, "seek": 382264, "start": 3822.7999999999997, "end": 3828.7999999999997,
  "text": " to find the documents that are about the exception handling across silos,
  label the ones that are", "tokens": [50372, 281, 915, 264, 8512, 300, 366, 466,
  264, 11183, 13175, 2108, 48893, 11, 7645, 264, 2306, 300, 366, 50672], "temperature":
  0.0, "avg_logprob": -0.1558786372548526, "compression_ratio": 1.625514403292181,
  "no_speech_prob": 0.00024645490339025855}, {"id": 634, "seek": 382264, "start":
  3828.7999999999997, "end": 3834.64, "text": " above a certain threshold. Perhaps
  you could display those in a UI and let the, let the analyst check", "tokens": [50672,
  3673, 257, 1629, 14678, 13, 10517, 291, 727, 4674, 729, 294, 257, 15682, 293, 718,
  264, 11, 718, 264, 19085, 1520, 50964], "temperature": 0.0, "avg_logprob": -0.1558786372548526,
  "compression_ratio": 1.625514403292181, "no_speech_prob": 0.00024645490339025855},
  {"id": 635, "seek": 382264, "start": 3834.64, "end": 3840.16, "text": " the labels,
  you could use a cool tool like Prodigy as an example, right, from explosion, the
  same", "tokens": [50964, 264, 16949, 11, 291, 727, 764, 257, 1627, 2290, 411, 1705,
  25259, 88, 382, 364, 1365, 11, 558, 11, 490, 15673, 11, 264, 912, 51240], "temperature":
  0.0, "avg_logprob": -0.1558786372548526, "compression_ratio": 1.625514403292181,
  "no_speech_prob": 0.00024645490339025855}, {"id": 636, "seek": 382264, "start":
  3840.16, "end": 3848.4, "text": " folks who make spacey, which is what we use in
  in swirl. And I think from there you would say you", "tokens": [51240, 4024, 567,
  652, 1901, 88, 11, 597, 307, 437, 321, 764, 294, 294, 30310, 13, 400, 286, 519,
  490, 456, 291, 576, 584, 291, 51652], "temperature": 0.0, "avg_logprob": -0.1558786372548526,
  "compression_ratio": 1.625514403292181, "no_speech_prob": 0.00024645490339025855},
  {"id": 637, "seek": 384840, "start": 3848.7200000000003, "end": 3853.04, "text":
  " if you trusted the labels, if the labels were good enough, you could actually
  do your first run,", "tokens": [50380, 498, 291, 16034, 264, 16949, 11, 498, 264,
  16949, 645, 665, 1547, 11, 291, 727, 767, 360, 428, 700, 1190, 11, 50596], "temperature":
  0.0, "avg_logprob": -0.17304945373535155, "compression_ratio": 1.745644599303136,
  "no_speech_prob": 0.0018037580884993076}, {"id": 638, "seek": 384840, "start": 3853.04,
  "end": 3859.6, "text": " right, take 25 or 40% or whatever your preferred number
  of the labeled results out, build the machine", "tokens": [50596, 558, 11, 747,
  3552, 420, 3356, 4, 420, 2035, 428, 16494, 1230, 295, 264, 21335, 3542, 484, 11,
  1322, 264, 3479, 50924], "temperature": 0.0, "avg_logprob": -0.17304945373535155,
  "compression_ratio": 1.745644599303136, "no_speech_prob": 0.0018037580884993076},
  {"id": 639, "seek": 384840, "start": 3859.6, "end": 3865.2000000000003, "text":
  " learning model with the rest, and then test with the, you know, with the holdout
  set, do the, you know,", "tokens": [50924, 2539, 2316, 365, 264, 1472, 11, 293,
  550, 1500, 365, 264, 11, 291, 458, 11, 365, 264, 1797, 346, 992, 11, 360, 264, 11,
  291, 458, 11, 51204], "temperature": 0.0, "avg_logprob": -0.17304945373535155, "compression_ratio":
  1.745644599303136, "no_speech_prob": 0.0018037580884993076}, {"id": 640, "seek":
  384840, "start": 3865.2000000000003, "end": 3870.88, "text": " if it''s bad, build
  a confusion matrix, etc, etc. There you go. And at least now you''re reviewing and",
  "tokens": [51204, 498, 309, 311, 1578, 11, 1322, 257, 15075, 8141, 11, 5183, 11,
  5183, 13, 821, 291, 352, 13, 400, 412, 1935, 586, 291, 434, 19576, 293, 51488],
  "temperature": 0.0, "avg_logprob": -0.17304945373535155, "compression_ratio": 1.745644599303136,
  "no_speech_prob": 0.0018037580884993076}, {"id": 641, "seek": 384840, "start": 3870.88,
  "end": 3874.96, "text": " refining and adjusting the threshold as opposed to going
  and starting with hand labeling of data.", "tokens": [51488, 1895, 1760, 293, 23559,
  264, 14678, 382, 8851, 281, 516, 293, 2891, 365, 1011, 40244, 295, 1412, 13, 51692],
  "temperature": 0.0, "avg_logprob": -0.17304945373535155, "compression_ratio": 1.745644599303136,
  "no_speech_prob": 0.0018037580884993076}, {"id": 642, "seek": 387496, "start": 3875.92,
  "end": 3880.32, "text": " Yeah. Yeah. That''s, that''s a great application for meta
  search and language models.", "tokens": [50412, 865, 13, 865, 13, 663, 311, 11,
  300, 311, 257, 869, 3861, 337, 19616, 3164, 293, 2856, 5245, 13, 50632], "temperature":
  0.0, "avg_logprob": -0.2142306926638581, "compression_ratio": 1.6575342465753424,
  "no_speech_prob": 0.025662627071142197}, {"id": 643, "seek": 387496, "start": 3880.32,
  "end": 3885.28, "text": " Exactly. And you explain basically kind of like in the,
  in the most straightforward way, you know,", "tokens": [50632, 7587, 13, 400, 291,
  2903, 1936, 733, 295, 411, 294, 264, 11, 294, 264, 881, 15325, 636, 11, 291, 458,
  11, 50880], "temperature": 0.0, "avg_logprob": -0.2142306926638581, "compression_ratio":
  1.6575342465753424, "no_speech_prob": 0.025662627071142197}, {"id": 644, "seek":
  387496, "start": 3885.28, "end": 3891.04, "text": " in a machine learning, out of
  machine learning model training testing validation, right,", "tokens": [50880, 294,
  257, 3479, 2539, 11, 484, 295, 3479, 2539, 2316, 3097, 4997, 24071, 11, 558, 11,
  51168], "temperature": 0.0, "avg_logprob": -0.2142306926638581, "compression_ratio":
  1.6575342465753424, "no_speech_prob": 0.025662627071142197}, {"id": 645, "seek":
  387496, "start": 3892.0, "end": 3899.28, "text": " which doesn''t escape in the
  search world doesn''t escape from this. I think this is amazing.", "tokens": [51216,
  597, 1177, 380, 7615, 294, 264, 3164, 1002, 1177, 380, 7615, 490, 341, 13, 286,
  519, 341, 307, 2243, 13, 51580], "temperature": 0.0, "avg_logprob": -0.2142306926638581,
  "compression_ratio": 1.6575342465753424, "no_speech_prob": 0.025662627071142197},
  {"id": 646, "seek": 389928, "start": 3900.2400000000002, "end": 3910.2400000000002,
  "text": " You chose as the model for your product, open source. You have some thoughts
  on this. I really like", "tokens": [50412, 509, 5111, 382, 264, 2316, 337, 428,
  1674, 11, 1269, 4009, 13, 509, 362, 512, 4598, 322, 341, 13, 286, 534, 411, 50912],
  "temperature": 0.0, "avg_logprob": -0.16929204647357649, "compression_ratio": 1.4545454545454546,
  "no_speech_prob": 0.03539002314209938}, {"id": 647, "seek": 389928, "start": 3910.2400000000002,
  "end": 3916.5600000000004, "text": " this question when I asked this to, I think
  I asked it to Bob Van Lloyd from VV8 as well.", "tokens": [50912, 341, 1168, 562,
  286, 2351, 341, 281, 11, 286, 519, 286, 2351, 309, 281, 6085, 8979, 31401, 490,
  691, 53, 23, 382, 731, 13, 51228], "temperature": 0.0, "avg_logprob": -0.16929204647357649,
  "compression_ratio": 1.4545454545454546, "no_speech_prob": 0.03539002314209938},
  {"id": 648, "seek": 389928, "start": 3917.2000000000003, "end": 3923.52, "text":
  " You know, why did you guys, you know, looking at your competition, let''s say
  Pinecon didn''t choose", "tokens": [51260, 509, 458, 11, 983, 630, 291, 1074, 11,
  291, 458, 11, 1237, 412, 428, 6211, 11, 718, 311, 584, 33531, 1671, 994, 380, 2826,
  51576], "temperature": 0.0, "avg_logprob": -0.16929204647357649, "compression_ratio":
  1.4545454545454546, "no_speech_prob": 0.03539002314209938}, {"id": 649, "seek":
  392352, "start": 3923.52, "end": 3929.04, "text": " open source for some reasons
  that are valid for them, but you guys did. And so did you,", "tokens": [50364, 1269,
  4009, 337, 512, 4112, 300, 366, 7363, 337, 552, 11, 457, 291, 1074, 630, 13, 400,
  370, 630, 291, 11, 50640], "temperature": 0.0, "avg_logprob": -0.17529916763305664,
  "compression_ratio": 1.6194690265486726, "no_speech_prob": 0.014030051417648792},
  {"id": 650, "seek": 392352, "start": 3930.48, "end": 3939.52, "text": " what makes
  you believe in this model work better? Because in some sense, it does require a
  lot of", "tokens": [50712, 437, 1669, 291, 1697, 294, 341, 2316, 589, 1101, 30,
  1436, 294, 512, 2020, 11, 309, 775, 3651, 257, 688, 295, 51164], "temperature":
  0.0, "avg_logprob": -0.17529916763305664, "compression_ratio": 1.6194690265486726,
  "no_speech_prob": 0.014030051417648792}, {"id": 651, "seek": 392352, "start": 3939.52,
  "end": 3944.4, "text": " like public facing work, right? You need to explain, you
  need to document, you need to", "tokens": [51164, 411, 1908, 7170, 589, 11, 558,
  30, 509, 643, 281, 2903, 11, 291, 643, 281, 4166, 11, 291, 643, 281, 51408], "temperature":
  0.0, "avg_logprob": -0.17529916763305664, "compression_ratio": 1.6194690265486726,
  "no_speech_prob": 0.014030051417648792}, {"id": 652, "seek": 392352, "start": 3945.04,
  "end": 3951.2, "text": " review pull requests with all the goodies that come with
  this, of course, right? But there is", "tokens": [51440, 3131, 2235, 12475, 365,
  439, 264, 44072, 300, 808, 365, 341, 11, 295, 1164, 11, 558, 30, 583, 456, 307,
  51748], "temperature": 0.0, "avg_logprob": -0.17529916763305664, "compression_ratio":
  1.6194690265486726, "no_speech_prob": 0.014030051417648792}, {"id": 653, "seek":
  395120, "start": 3951.3599999999997, "end": 3958.3199999999997, "text": " an extra
  work involved, but you definitely get some benefits. What is your thinking here?",
  "tokens": [50372, 364, 2857, 589, 3288, 11, 457, 291, 2138, 483, 512, 5311, 13,
  708, 307, 428, 1953, 510, 30, 50720], "temperature": 0.0, "avg_logprob": -0.12645489519292658,
  "compression_ratio": 1.524390243902439, "no_speech_prob": 0.003641559509560466},
  {"id": 654, "seek": 395120, "start": 3960.56, "end": 3967.52, "text": " The truth
  is I''ve been an open source person forever. I just believe in it, whether it was,",
  "tokens": [50832, 440, 3494, 307, 286, 600, 668, 364, 1269, 4009, 954, 5680, 13,
  286, 445, 1697, 294, 309, 11, 1968, 309, 390, 11, 51180], "temperature": 0.0, "avg_logprob":
  -0.12645489519292658, "compression_ratio": 1.524390243902439, "no_speech_prob":
  0.003641559509560466}, {"id": 655, "seek": 395120, "start": 3968.3199999999997,
  "end": 3973.7599999999998, "text": " Jeff Hammerbacker''s amazing comment about
  how it''s too bad that everyone''s spending their time", "tokens": [51220, 7506,
  33722, 3207, 260, 311, 2243, 2871, 466, 577, 309, 311, 886, 1578, 300, 1518, 311,
  6434, 641, 565, 51492], "temperature": 0.0, "avg_logprob": -0.12645489519292658,
  "compression_ratio": 1.524390243902439, "no_speech_prob": 0.003641559509560466},
  {"id": 656, "seek": 395120, "start": 3973.7599999999998, "end": 3979.7599999999998,
  "text": " on clicks, right? And he believes that the data science approach benefits
  hugely from open source.", "tokens": [51492, 322, 18521, 11, 558, 30, 400, 415,
  12307, 300, 264, 1412, 3497, 3109, 5311, 27417, 490, 1269, 4009, 13, 51792], "temperature":
  0.0, "avg_logprob": -0.12645489519292658, "compression_ratio": 1.524390243902439,
  "no_speech_prob": 0.003641559509560466}, {"id": 657, "seek": 397976, "start": 3979.76,
  "end": 3986.8, "text": " That''s so true. Joseph Jackson, the notable VC, right,
  has written so much about its open source", "tokens": [50364, 663, 311, 370, 2074,
  13, 11170, 10647, 11, 264, 22556, 41922, 11, 558, 11, 575, 3720, 370, 709, 466,
  1080, 1269, 4009, 50716], "temperature": 0.0, "avg_logprob": -0.1254420757293701,
  "compression_ratio": 1.589430894308943, "no_speech_prob": 0.0014395508915185928},
  {"id": 658, "seek": 397976, "start": 3986.8, "end": 3991.84, "text": " software
  that''s really eating the world. It''s eating at a considerably higher rate. And
  the reason", "tokens": [50716, 4722, 300, 311, 534, 3936, 264, 1002, 13, 467, 311,
  3936, 412, 257, 31308, 2946, 3314, 13, 400, 264, 1778, 50968], "temperature": 0.0,
  "avg_logprob": -0.1254420757293701, "compression_ratio": 1.589430894308943, "no_speech_prob":
  0.0014395508915185928}, {"id": 659, "seek": 397976, "start": 3991.84, "end": 3998.8,
  "text": " I think is it''s a few things. One is trust. One is trust. You know, during
  the pandemic, I think the", "tokens": [50968, 286, 519, 307, 309, 311, 257, 1326,
  721, 13, 1485, 307, 3361, 13, 1485, 307, 3361, 13, 509, 458, 11, 1830, 264, 5388,
  11, 286, 519, 264, 51316], "temperature": 0.0, "avg_logprob": -0.1254420757293701,
  "compression_ratio": 1.589430894308943, "no_speech_prob": 0.0014395508915185928},
  {"id": 660, "seek": 397976, "start": 3998.8, "end": 4005.44, "text": " large enterprise
  saw a lot of promising young ventures just not make it. And if you bet on one",
  "tokens": [51316, 2416, 14132, 1866, 257, 688, 295, 20257, 2037, 6931, 1303, 445,
  406, 652, 309, 13, 400, 498, 291, 778, 322, 472, 51648], "temperature": 0.0, "avg_logprob":
  -0.1254420757293701, "compression_ratio": 1.589430894308943, "no_speech_prob": 0.0014395508915185928},
  {"id": 661, "seek": 400544, "start": 4005.44, "end": 4009.92, "text": " of those
  technologies, you probably didn''t get the technology. Or maybe you did, right?
  I don''t", "tokens": [50364, 295, 729, 7943, 11, 291, 1391, 994, 380, 483, 264,
  2899, 13, 1610, 1310, 291, 630, 11, 558, 30, 286, 500, 380, 50588], "temperature":
  0.0, "avg_logprob": -0.10269281243075844, "compression_ratio": 1.7359154929577465,
  "no_speech_prob": 0.0021498538553714752}, {"id": 662, "seek": 400544, "start": 4009.92,
  "end": 4014.88, "text": " know, but there was a certain amount of risk involved
  in that. And open source does, although people,", "tokens": [50588, 458, 11, 457,
  456, 390, 257, 1629, 2372, 295, 3148, 3288, 294, 300, 13, 400, 1269, 4009, 775,
  11, 4878, 561, 11, 50836], "temperature": 0.0, "avg_logprob": -0.10269281243075844,
  "compression_ratio": 1.7359154929577465, "no_speech_prob": 0.0021498538553714752},
  {"id": 663, "seek": 400544, "start": 4014.88, "end": 4019.28, "text": " I don''t
  think want to take the code and run with it, they want to know that they could,
  if they had", "tokens": [50836, 286, 500, 380, 519, 528, 281, 747, 264, 3089, 293,
  1190, 365, 309, 11, 436, 528, 281, 458, 300, 436, 727, 11, 498, 436, 632, 51056],
  "temperature": 0.0, "avg_logprob": -0.10269281243075844, "compression_ratio": 1.7359154929577465,
  "no_speech_prob": 0.0021498538553714752}, {"id": 664, "seek": 400544, "start": 4019.28,
  "end": 4025.68, "text": " to. The second thing though, the trust is much deeper
  when you have a commercial company that supports", "tokens": [51056, 281, 13, 440,
  1150, 551, 1673, 11, 264, 3361, 307, 709, 7731, 562, 291, 362, 257, 6841, 2237,
  300, 9346, 51376], "temperature": 0.0, "avg_logprob": -0.10269281243075844, "compression_ratio":
  1.7359154929577465, "no_speech_prob": 0.0021498538553714752}, {"id": 665, "seek":
  400544, "start": 4025.68, "end": 4031.44, "text": " open source, the so-called commercial
  open source model, because it does require that public", "tokens": [51376, 1269,
  4009, 11, 264, 370, 12, 11880, 6841, 1269, 4009, 2316, 11, 570, 309, 775, 3651,
  300, 1908, 51664], "temperature": 0.0, "avg_logprob": -0.10269281243075844, "compression_ratio":
  1.7359154929577465, "no_speech_prob": 0.0021498538553714752}, {"id": 666, "seek":
  403144, "start": 4031.44, "end": 4037.04, "text": " investment, that public discipline.
  We''re all about people using it. There''s no sales.", "tokens": [50364, 6078, 11,
  300, 1908, 13635, 13, 492, 434, 439, 466, 561, 1228, 309, 13, 821, 311, 572, 5763,
  13, 50644], "temperature": 0.0, "avg_logprob": -0.11111964175575657, "compression_ratio":
  1.5862068965517242, "no_speech_prob": 0.0028009426314383745}, {"id": 667, "seek":
  403144, "start": 4037.6, "end": 4042.96, "text": " Nobody has that title. We''re
  here to make people successful using it. And I''m not sure,", "tokens": [50672,
  9297, 575, 300, 4876, 13, 492, 434, 510, 281, 652, 561, 4406, 1228, 309, 13, 400,
  286, 478, 406, 988, 11, 50940], "temperature": 0.0, "avg_logprob": -0.11111964175575657,
  "compression_ratio": 1.5862068965517242, "no_speech_prob": 0.0028009426314383745},
  {"id": 668, "seek": 403144, "start": 4043.76, "end": 4047.36, "text": " to be honest
  with you, how all the different ways it''s going to evolve, but we want to evolve",
  "tokens": [50980, 281, 312, 3245, 365, 291, 11, 577, 439, 264, 819, 2098, 309, 311,
  516, 281, 16693, 11, 457, 321, 528, 281, 16693, 51160], "temperature": 0.0, "avg_logprob":
  -0.11111964175575657, "compression_ratio": 1.5862068965517242, "no_speech_prob":
  0.0028009426314383745}, {"id": 669, "seek": 403144, "start": 4048.32, "end": 4055.52,
  "text": " in line with what the actual community needs. You know, I think you start
  with a kernel of an idea,", "tokens": [51208, 294, 1622, 365, 437, 264, 3539, 1768,
  2203, 13, 509, 458, 11, 286, 519, 291, 722, 365, 257, 28256, 295, 364, 1558, 11,
  51568], "temperature": 0.0, "avg_logprob": -0.11111964175575657, "compression_ratio":
  1.5862068965517242, "no_speech_prob": 0.0028009426314383745}, {"id": 670, "seek":
  405552, "start": 4055.6, "end": 4061.28, "text": " and I''ve worked in search enough
  to have that. But beyond that, it''s a collective thing.", "tokens": [50368, 293,
  286, 600, 2732, 294, 3164, 1547, 281, 362, 300, 13, 583, 4399, 300, 11, 309, 311,
  257, 12590, 551, 13, 50652], "temperature": 0.0, "avg_logprob": -0.1342171819586503,
  "compression_ratio": 1.625, "no_speech_prob": 0.01445038802921772}, {"id": 671,
  "seek": 405552, "start": 4062.48, "end": 4067.44, "text": " I love the way Vespa,
  as an example, is so open to look at how well it''s evolving in the", "tokens":
  [50712, 286, 959, 264, 636, 691, 279, 4306, 11, 382, 364, 1365, 11, 307, 370, 1269,
  281, 574, 412, 577, 731, 309, 311, 21085, 294, 264, 50960], "temperature": 0.0,
  "avg_logprob": -0.1342171819586503, "compression_ratio": 1.625, "no_speech_prob":
  0.01445038802921772}, {"id": 672, "seek": 405552, "start": 4068.0, "end": 4074.48,
  "text": " place that the community that needs it. I think there''s a similar community.
  And what is out there", "tokens": [50988, 1081, 300, 264, 1768, 300, 2203, 309,
  13, 286, 519, 456, 311, 257, 2531, 1768, 13, 400, 437, 307, 484, 456, 51312], "temperature":
  0.0, "avg_logprob": -0.1342171819586503, "compression_ratio": 1.625, "no_speech_prob":
  0.01445038802921772}, {"id": 673, "seek": 405552, "start": 4074.48, "end": 4080.88,
  "text": " for them are a bunch of potentially some good and some unknown vendors,
  some interesting open source", "tokens": [51312, 337, 552, 366, 257, 3840, 295,
  7263, 512, 665, 293, 512, 9841, 22056, 11, 512, 1880, 1269, 4009, 51632], "temperature":
  0.0, "avg_logprob": -0.1342171819586503, "compression_ratio": 1.625, "no_speech_prob":
  0.01445038802921772}, {"id": 674, "seek": 408088, "start": 4080.96, "end": 4085.36,
  "text": " products, some of which might take a lot of work together. And maybe their
  stories about", "tokens": [50368, 3383, 11, 512, 295, 597, 1062, 747, 257, 688,
  295, 589, 1214, 13, 400, 1310, 641, 3676, 466, 50588], "temperature": 0.0, "avg_logprob":
  -0.17879707122517524, "compression_ratio": 1.627177700348432, "no_speech_prob":
  0.006980721838772297}, {"id": 675, "seek": 408088, "start": 4086.2400000000002,
  "end": 4089.84, "text": " super hot projects where there''s one committee, and they
  go on vacation for two months and", "tokens": [50632, 1687, 2368, 4455, 689, 456,
  311, 472, 7482, 11, 293, 436, 352, 322, 12830, 337, 732, 2493, 293, 50812], "temperature":
  0.0, "avg_logprob": -0.17879707122517524, "compression_ratio": 1.627177700348432,
  "no_speech_prob": 0.006980721838772297}, {"id": 676, "seek": 408088, "start": 4089.84,
  "end": 4095.28, "text": " everything falls apart, where they lose interest after
  two years, and they leave with 2000 tickets.", "tokens": [50812, 1203, 8804, 4936,
  11, 689, 436, 3624, 1179, 934, 732, 924, 11, 293, 436, 1856, 365, 8132, 12628, 13,
  51084], "temperature": 0.0, "avg_logprob": -0.17879707122517524, "compression_ratio":
  1.627177700348432, "no_speech_prob": 0.006980721838772297}, {"id": 677, "seek":
  408088, "start": 4095.28, "end": 4100.4800000000005, "text": " It''s good to know
  that there''s a little commercial entity. But ultimately, aren''t the greatest",
  "tokens": [51084, 467, 311, 665, 281, 458, 300, 456, 311, 257, 707, 6841, 13977,
  13, 583, 6284, 11, 3212, 380, 264, 6636, 51344], "temperature": 0.0, "avg_logprob":
  -0.17879707122517524, "compression_ratio": 1.627177700348432, "no_speech_prob":
  0.006980721838772297}, {"id": 678, "seek": 408088, "start": 4100.4800000000005,
  "end": 4106.4800000000005, "text": " innovations coming from open source, open AI?
  Most of the pieces out there, that''s why there", "tokens": [51344, 24283, 1348,
  490, 1269, 4009, 11, 1269, 7318, 30, 4534, 295, 264, 3755, 484, 456, 11, 300, 311,
  983, 456, 51644], "temperature": 0.0, "avg_logprob": -0.17879707122517524, "compression_ratio":
  1.627177700348432, "no_speech_prob": 0.006980721838772297}, {"id": 679, "seek":
  410648, "start": 4106.48, "end": 4110.959999999999, "text": " have been so many
  replications. And that''s the last piece of it. It''s provable. You know,", "tokens":
  [50364, 362, 668, 370, 867, 3248, 24847, 13, 400, 300, 311, 264, 1036, 2522, 295,
  309, 13, 467, 311, 1439, 712, 13, 509, 458, 11, 50588], "temperature": 0.0, "avg_logprob":
  -0.18282179246869004, "compression_ratio": 1.6, "no_speech_prob": 0.005276723299175501},
  {"id": 680, "seek": 410648, "start": 4111.759999999999, "end": 4115.759999999999,
  "text": " you can take my word for it. You can look at all the charts and stuff.
  But with two", "tokens": [50628, 291, 393, 747, 452, 1349, 337, 309, 13, 509, 393,
  574, 412, 439, 264, 17767, 293, 1507, 13, 583, 365, 732, 50828], "temperature":
  0.0, "avg_logprob": -0.18282179246869004, "compression_ratio": 1.6, "no_speech_prob":
  0.005276723299175501}, {"id": 681, "seek": 410648, "start": 4116.5599999999995,
  "end": 4120.879999999999, "text": " commands, if you have Docker running, you can
  get swirl going, and you can see for yourself.", "tokens": [50868, 16901, 11, 498,
  291, 362, 33772, 2614, 11, 291, 393, 483, 30310, 516, 11, 293, 291, 393, 536, 337,
  1803, 13, 51084], "temperature": 0.0, "avg_logprob": -0.18282179246869004, "compression_ratio":
  1.6, "no_speech_prob": 0.005276723299175501}, {"id": 682, "seek": 410648, "start":
  4122.0, "end": 4126.0, "text": " Yeah. If it doesn''t do something, well, help us
  make it better. Sorry, go ahead.", "tokens": [51140, 865, 13, 759, 309, 1177, 380,
  360, 746, 11, 731, 11, 854, 505, 652, 309, 1101, 13, 4919, 11, 352, 2286, 13, 51340],
  "temperature": 0.0, "avg_logprob": -0.18282179246869004, "compression_ratio": 1.6,
  "no_speech_prob": 0.005276723299175501}, {"id": 683, "seek": 410648, "start": 4126.0,
  "end": 4130.08, "text": " Exactly. Exactly. No, I mean, that exactly proves it because",
  "tokens": [51340, 7587, 13, 7587, 13, 883, 11, 286, 914, 11, 300, 2293, 25019, 309,
  570, 51544], "temperature": 0.0, "avg_logprob": -0.18282179246869004, "compression_ratio":
  1.6, "no_speech_prob": 0.005276723299175501}, {"id": 684, "seek": 413008, "start":
  4130.5599999999995, "end": 4138.64, "text": " however magical the software is, if
  you are the engineer, you really want to like, you know,", "tokens": [50388, 4461,
  12066, 264, 4722, 307, 11, 498, 291, 366, 264, 11403, 11, 291, 534, 528, 281, 411,
  11, 291, 458, 11, 50792], "temperature": 0.0, "avg_logprob": -0.1522594041462186,
  "compression_ratio": 1.554945054945055, "no_speech_prob": 0.04024715721607208},
  {"id": 685, "seek": 413008, "start": 4138.64, "end": 4146.24, "text": " open the
  engine and see what''s going on there. How can I modify this? How can I plug this
  in?", "tokens": [50792, 1269, 264, 2848, 293, 536, 437, 311, 516, 322, 456, 13,
  1012, 393, 286, 16927, 341, 30, 1012, 393, 286, 5452, 341, 294, 30, 51172], "temperature":
  0.0, "avg_logprob": -0.1522594041462186, "compression_ratio": 1.554945054945055,
  "no_speech_prob": 0.04024715721607208}, {"id": 686, "seek": 413008, "start": 4147.2,
  "end": 4155.2, "text": " Because if it''s not open, I guess, well, maybe someone
  will blame me and say, no, this is wrong.", "tokens": [51220, 1436, 498, 309, 311,
  406, 1269, 11, 286, 2041, 11, 731, 11, 1310, 1580, 486, 10127, 385, 293, 584, 11,
  572, 11, 341, 307, 2085, 13, 51620], "temperature": 0.0, "avg_logprob": -0.1522594041462186,
  "compression_ratio": 1.554945054945055, "no_speech_prob": 0.04024715721607208},
  {"id": 687, "seek": 415520, "start": 4155.28, "end": 4160.4, "text": " But you know,
  if it''s like an API that I need to pay for, what''s the path for me to get", "tokens":
  [50368, 583, 291, 458, 11, 498, 309, 311, 411, 364, 9362, 300, 286, 643, 281, 1689,
  337, 11, 437, 311, 264, 3100, 337, 385, 281, 483, 50624], "temperature": 0.0, "avg_logprob":
  -0.13435068997469815, "compression_ratio": 1.6443661971830985, "no_speech_prob":
  0.0394461527466774}, {"id": 688, "seek": 415520, "start": 4160.639999999999, "end":
  4165.44, "text": " into hacking? Should I buy it on my own credit card? Or should
  I call my manager and say, hey,", "tokens": [50636, 666, 31422, 30, 6454, 286, 2256,
  309, 322, 452, 1065, 5397, 2920, 30, 1610, 820, 286, 818, 452, 6598, 293, 584, 11,
  4177, 11, 50876], "temperature": 0.0, "avg_logprob": -0.13435068997469815, "compression_ratio":
  1.6443661971830985, "no_speech_prob": 0.0394461527466774}, {"id": 689, "seek": 415520,
  "start": 4165.44, "end": 4170.4, "text": " can you, well, and usually what happens
  if you look at Pinecon, for example, they will have,", "tokens": [50876, 393, 291,
  11, 731, 11, 293, 2673, 437, 2314, 498, 291, 574, 412, 33531, 1671, 11, 337, 1365,
  11, 436, 486, 362, 11, 51124], "temperature": 0.0, "avg_logprob": -0.13435068997469815,
  "compression_ratio": 1.6443661971830985, "no_speech_prob": 0.0394461527466774},
  {"id": 690, "seek": 415520, "start": 4170.4, "end": 4176.4, "text": " they will
  allocate like a free tier, right? And so you can kind of hack with free tier. If
  you run", "tokens": [51124, 436, 486, 35713, 411, 257, 1737, 12362, 11, 558, 30,
  400, 370, 291, 393, 733, 295, 10339, 365, 1737, 12362, 13, 759, 291, 1190, 51424],
  "temperature": 0.0, "avg_logprob": -0.13435068997469815, "compression_ratio": 1.6443661971830985,
  "no_speech_prob": 0.0394461527466774}, {"id": 691, "seek": 415520, "start": 4176.4,
  "end": 4182.48, "text": " out, then you''ll call your manager, I guess. Right. And
  nothing wrong with that too. I mean,", "tokens": [51424, 484, 11, 550, 291, 603,
  818, 428, 6598, 11, 286, 2041, 13, 1779, 13, 400, 1825, 2085, 365, 300, 886, 13,
  286, 914, 11, 51728], "temperature": 0.0, "avg_logprob": -0.13435068997469815, "compression_ratio":
  1.6443661971830985, "no_speech_prob": 0.0394461527466774}, {"id": 692, "seek": 418248,
  "start": 4182.48, "end": 4186.959999999999, "text": " but I think that that''s just
  a facilitation of the try and buy process. It''s still a commercial", "tokens":
  [50364, 457, 286, 519, 300, 300, 311, 445, 257, 10217, 4614, 295, 264, 853, 293,
  2256, 1399, 13, 467, 311, 920, 257, 6841, 50588], "temperature": 0.0, "avg_logprob":
  -0.12968287392268105, "compression_ratio": 1.66, "no_speech_prob": 0.0054180677980184555},
  {"id": 693, "seek": 418248, "start": 4186.959999999999, "end": 4193.36, "text":
  " company. You can''t know for sure. Right. And honestly, that works for many companies.
  There''s no one", "tokens": [50588, 2237, 13, 509, 393, 380, 458, 337, 988, 13,
  1779, 13, 400, 6095, 11, 300, 1985, 337, 867, 3431, 13, 821, 311, 572, 472, 50908],
  "temperature": 0.0, "avg_logprob": -0.12968287392268105, "compression_ratio": 1.66,
  "no_speech_prob": 0.0054180677980184555}, {"id": 694, "seek": 418248, "start": 4193.36,
  "end": 4199.12, "text": " size fits all. My point is this. I think for solving complex,
  the kinds of complex multi-silow problems", "tokens": [50908, 2744, 9001, 439, 13,
  1222, 935, 307, 341, 13, 286, 519, 337, 12606, 3997, 11, 264, 3685, 295, 3997, 4825,
  12, 30605, 305, 2740, 51196], "temperature": 0.0, "avg_logprob": -0.12968287392268105,
  "compression_ratio": 1.66, "no_speech_prob": 0.0054180677980184555}, {"id": 695,
  "seek": 418248, "start": 4199.12, "end": 4202.879999999999, "text": " in the large
  enterprise where where I have been very lucky to work before and where I think,
  at", "tokens": [51196, 294, 264, 2416, 14132, 689, 689, 286, 362, 668, 588, 6356,
  281, 589, 949, 293, 689, 286, 519, 11, 412, 51384], "temperature": 0.0, "avg_logprob":
  -0.12968287392268105, "compression_ratio": 1.66, "no_speech_prob": 0.0054180677980184555},
  {"id": 696, "seek": 418248, "start": 4202.879999999999, "end": 4206.799999999999,
  "text": " least to some degree, I hear about the problems, right? Even if I don''t
  understand them. I hear about", "tokens": [51384, 1935, 281, 512, 4314, 11, 286,
  1568, 466, 264, 2740, 11, 558, 30, 2754, 498, 286, 500, 380, 1223, 552, 13, 286,
  1568, 466, 51580], "temperature": 0.0, "avg_logprob": -0.12968287392268105, "compression_ratio":
  1.66, "no_speech_prob": 0.0054180677980184555}, {"id": 697, "seek": 420680, "start":
  4206.96, "end": 4214.320000000001, "text": " the problems. Open source is the winning
  model because it is so tailorable. You know, no one has the", "tokens": [50372,
  264, 2740, 13, 7238, 4009, 307, 264, 8224, 2316, 570, 309, 307, 370, 6838, 284,
  712, 13, 509, 458, 11, 572, 472, 575, 264, 50740], "temperature": 0.0, "avg_logprob":
  -0.11268501897012034, "compression_ratio": 1.7560975609756098, "no_speech_prob":
  0.005842366721481085}, {"id": 698, "seek": 420680, "start": 4214.320000000001, "end":
  4218.4800000000005, "text": " same thing. Everybody has seven of everything, I think,
  in the large enterprise. And then there''s", "tokens": [50740, 912, 551, 13, 7646,
  575, 3407, 295, 1203, 11, 286, 519, 11, 294, 264, 2416, 14132, 13, 400, 550, 456,
  311, 50948], "temperature": 0.0, "avg_logprob": -0.11268501897012034, "compression_ratio":
  1.7560975609756098, "no_speech_prob": 0.005842366721481085}, {"id": 699, "seek":
  420680, "start": 4218.4800000000005, "end": 4223.28, "text": " regulation and compliance
  regulatory systems, all that stuff. Those things are the ones, those are", "tokens":
  [50948, 15062, 293, 15882, 18260, 3652, 11, 439, 300, 1507, 13, 3950, 721, 366,
  264, 2306, 11, 729, 366, 51188], "temperature": 0.0, "avg_logprob": -0.11268501897012034,
  "compression_ratio": 1.7560975609756098, "no_speech_prob": 0.005842366721481085},
  {"id": 700, "seek": 420680, "start": 4223.28, "end": 4228.4800000000005, "text":
  " the actual barriers. So open source is most adoptable in that regard. And then
  I think as long as there''s", "tokens": [51188, 264, 3539, 13565, 13, 407, 1269,
  4009, 307, 881, 6878, 712, 294, 300, 3843, 13, 400, 550, 286, 519, 382, 938, 382,
  456, 311, 51448], "temperature": 0.0, "avg_logprob": -0.11268501897012034, "compression_ratio":
  1.7560975609756098, "no_speech_prob": 0.005842366721481085}, {"id": 701, "seek":
  420680, "start": 4228.4800000000005, "end": 4233.360000000001, "text": " someone
  who, you know, as long as there''s some option to say, well, they''re not disappearing,
  right?", "tokens": [51448, 1580, 567, 11, 291, 458, 11, 382, 938, 382, 456, 311,
  512, 3614, 281, 584, 11, 731, 11, 436, 434, 406, 34900, 11, 558, 30, 51692], "temperature":
  0.0, "avg_logprob": -0.11268501897012034, "compression_ratio": 1.7560975609756098,
  "no_speech_prob": 0.005842366721481085}, {"id": 702, "seek": 423336, "start": 4233.36,
  "end": 4237.44, "text": " They''re not. There''s still someone to help us who really
  knows how this thing works.", "tokens": [50364, 814, 434, 406, 13, 821, 311, 920,
  1580, 281, 854, 505, 567, 534, 3255, 577, 341, 551, 1985, 13, 50568], "temperature":
  0.0, "avg_logprob": -0.25137206597056816, "compression_ratio": 1.5680272108843538,
  "no_speech_prob": 0.009913946501910686}, {"id": 703, "seek": 423336, "start": 4238.0,
  "end": 4245.2, "text": " It''s, it''s safe and tailorable. And that''s what''s really
  driving so much of the growth,", "tokens": [50596, 467, 311, 11, 309, 311, 3273,
  293, 6838, 284, 712, 13, 400, 300, 311, 437, 311, 534, 4840, 370, 709, 295, 264,
  4599, 11, 50956], "temperature": 0.0, "avg_logprob": -0.25137206597056816, "compression_ratio":
  1.5680272108843538, "no_speech_prob": 0.009913946501910686}, {"id": 704, "seek":
  423336, "start": 4245.759999999999, "end": 4251.92, "text": " the incredible growth
  in the software. Again, chat GPT, right? Paper, wood methods, not. It''s", "tokens":
  [50984, 264, 4651, 4599, 294, 264, 4722, 13, 3764, 11, 5081, 26039, 51, 11, 558,
  30, 24990, 11, 4576, 7150, 11, 406, 13, 467, 311, 51292], "temperature": 0.0, "avg_logprob":
  -0.25137206597056816, "compression_ratio": 1.5680272108843538, "no_speech_prob":
  0.009913946501910686}, {"id": 705, "seek": 423336, "start": 4251.92, "end": 4256.48,
  "text": " being commercialized, but that''s no surprise. Yeah, I mean, it wouldn''t
  probably exist if, like,", "tokens": [51292, 885, 6841, 1602, 11, 457, 300, 311,
  572, 6365, 13, 865, 11, 286, 914, 11, 309, 2759, 380, 1391, 2514, 498, 11, 411,
  11, 51520], "temperature": 0.0, "avg_logprob": -0.25137206597056816, "compression_ratio":
  1.5680272108843538, "no_speech_prob": 0.009913946501910686}, {"id": 706, "seek":
  423336, "start": 4256.48, "end": 4263.12, "text": " just yesterday I was hacking
  something for going to bed. And it was super slow because I think it", "tokens":
  [51520, 445, 5186, 286, 390, 31422, 746, 337, 516, 281, 2901, 13, 400, 309, 390,
  1687, 2964, 570, 286, 519, 309, 51852], "temperature": 0.0, "avg_logprob": -0.25137206597056816,
  "compression_ratio": 1.5680272108843538, "no_speech_prob": 0.009913946501910686},
  {"id": 707, "seek": 426312, "start": 4263.12, "end": 4268.8, "text": " was US daytime.
  Everyone was probably hacking there as well. But I was fine with that. It was typing",
  "tokens": [50364, 390, 2546, 31908, 13, 5198, 390, 1391, 31422, 456, 382, 731, 13,
  583, 286, 390, 2489, 365, 300, 13, 467, 390, 18444, 50648], "temperature": 0.0,
  "avg_logprob": -0.13506454278614896, "compression_ratio": 1.6416382252559727, "no_speech_prob":
  0.0028039070311933756}, {"id": 708, "seek": 426312, "start": 4268.8, "end": 4275.04,
  "text": " slowly, giving me some code snippets. But could it have given me this
  code snippets if they were not", "tokens": [50648, 5692, 11, 2902, 385, 512, 3089,
  35623, 1385, 13, 583, 727, 309, 362, 2212, 385, 341, 3089, 35623, 1385, 498, 436,
  645, 406, 50960], "temperature": 0.0, "avg_logprob": -0.13506454278614896, "compression_ratio":
  1.6416382252559727, "no_speech_prob": 0.0028039070311933756}, {"id": 709, "seek":
  426312, "start": 4275.04, "end": 4280.0, "text": " online, if they were not like
  on GitHub or somewhere else, right? So I think it''s kind of", "tokens": [50960,
  2950, 11, 498, 436, 645, 406, 411, 322, 23331, 420, 4079, 1646, 11, 558, 30, 407,
  286, 519, 309, 311, 733, 295, 51208], "temperature": 0.0, "avg_logprob": -0.13506454278614896,
  "compression_ratio": 1.6416382252559727, "no_speech_prob": 0.0028039070311933756},
  {"id": 710, "seek": 426312, "start": 4280.0, "end": 4285.44, "text": " extending
  on the shoulders of giants again. Totally. I completely agree with you. And it''s",
  "tokens": [51208, 24360, 322, 264, 10245, 295, 31894, 797, 13, 22837, 13, 286, 2584,
  3986, 365, 291, 13, 400, 309, 311, 51480], "temperature": 0.0, "avg_logprob": -0.13506454278614896,
  "compression_ratio": 1.6416382252559727, "no_speech_prob": 0.0028039070311933756},
  {"id": 711, "seek": 426312, "start": 4285.44, "end": 4290.96, "text": " extremely
  limited. Look, it was trained at least partly the noncode part, right? It was on
  Reddit.", "tokens": [51480, 4664, 5567, 13, 2053, 11, 309, 390, 8895, 412, 1935,
  17031, 264, 2107, 22332, 644, 11, 558, 30, 467, 390, 322, 32210, 13, 51756], "temperature":
  0.0, "avg_logprob": -0.13506454278614896, "compression_ratio": 1.6416382252559727,
  "no_speech_prob": 0.0028039070311933756}, {"id": 712, "seek": 429096, "start": 4291.6,
  "end": 4297.12, "text": " It reads like Reddit. It has a little bit of a know it,
  Ollie, you know, and it gives the sort of", "tokens": [50396, 467, 15700, 411, 32210,
  13, 467, 575, 257, 707, 857, 295, 257, 458, 309, 11, 35089, 11, 291, 458, 11, 293,
  309, 2709, 264, 1333, 295, 50672], "temperature": 0.0, "avg_logprob": -0.14392166137695311,
  "compression_ratio": 1.6821428571428572, "no_speech_prob": 0.00977780856192112},
  {"id": 713, "seek": 429096, "start": 4297.12, "end": 4303.76, "text": " like consensus
  answer. Now, that''s great for code as long as the consensus data is modern, current,",
  "tokens": [50672, 411, 19115, 1867, 13, 823, 11, 300, 311, 869, 337, 3089, 382,
  938, 382, 264, 19115, 1412, 307, 4363, 11, 2190, 11, 51004], "temperature": 0.0,
  "avg_logprob": -0.14392166137695311, "compression_ratio": 1.6821428571428572, "no_speech_prob":
  0.00977780856192112}, {"id": 714, "seek": 429096, "start": 4303.76, "end": 4309.2,
  "text": " and available. So it''s never going to teach you, it probably won''t teach
  you that much about enterprise", "tokens": [51004, 293, 2435, 13, 407, 309, 311,
  1128, 516, 281, 2924, 291, 11, 309, 1391, 1582, 380, 2924, 291, 300, 709, 466, 14132,
  51276], "temperature": 0.0, "avg_logprob": -0.14392166137695311, "compression_ratio":
  1.6821428571428572, "no_speech_prob": 0.00977780856192112}, {"id": 715, "seek":
  429096, "start": 4309.2, "end": 4312.96, "text": " integration patterns and enterprise
  workloads. But it''ll teach you a lot about open source.", "tokens": [51276, 10980,
  8294, 293, 14132, 32452, 13, 583, 309, 603, 2924, 291, 257, 688, 466, 1269, 4009,
  13, 51464], "temperature": 0.0, "avg_logprob": -0.14392166137695311, "compression_ratio":
  1.6821428571428572, "no_speech_prob": 0.00977780856192112}, {"id": 716, "seek":
  429096, "start": 4314.4800000000005, "end": 4317.68, "text": " I write with it,
  I try to write with it almost every day. And I can say this,", "tokens": [51540,
  286, 2464, 365, 309, 11, 286, 853, 281, 2464, 365, 309, 1920, 633, 786, 13, 400,
  286, 393, 584, 341, 11, 51700], "temperature": 0.0, "avg_logprob": -0.14392166137695311,
  "compression_ratio": 1.6821428571428572, "no_speech_prob": 0.00977780856192112},
  {"id": 717, "seek": 431768, "start": 4318.64, "end": 4325.200000000001, "text":
  " it''s very good at filling in a class function. If you teach it a class, it''s
  very good at that.", "tokens": [50412, 309, 311, 588, 665, 412, 10623, 294, 257,
  1508, 2445, 13, 759, 291, 2924, 309, 257, 1508, 11, 309, 311, 588, 665, 412, 300,
  13, 50740], "temperature": 0.0, "avg_logprob": -0.09471610260009766, "compression_ratio":
  1.8108108108108107, "no_speech_prob": 0.007828890345990658}, {"id": 718, "seek":
  431768, "start": 4325.200000000001, "end": 4329.6, "text": " That seems to be, and
  that''s really, I think, commodity work, right? How to connect to X?", "tokens":
  [50740, 663, 2544, 281, 312, 11, 293, 300, 311, 534, 11, 286, 519, 11, 29125, 589,
  11, 558, 30, 1012, 281, 1745, 281, 1783, 30, 50960], "temperature": 0.0, "avg_logprob":
  -0.09471610260009766, "compression_ratio": 1.8108108108108107, "no_speech_prob":
  0.007828890345990658}, {"id": 719, "seek": 431768, "start": 4330.64, "end": 4335.4400000000005,
  "text": " It''s very, very disruptive there. It''s also potentially disruptive to
  a lot of natural language", "tokens": [51012, 467, 311, 588, 11, 588, 37865, 456,
  13, 467, 311, 611, 7263, 37865, 281, 257, 688, 295, 3303, 2856, 51252], "temperature":
  0.0, "avg_logprob": -0.09471610260009766, "compression_ratio": 1.8108108108108107,
  "no_speech_prob": 0.007828890345990658}, {"id": 720, "seek": 431768, "start": 4335.4400000000005,
  "end": 4340.96, "text": " tasks. I think that''s the way it is because it is at
  the end of the day a giant natural language", "tokens": [51252, 9608, 13, 286, 519,
  300, 311, 264, 636, 309, 307, 570, 309, 307, 412, 264, 917, 295, 264, 786, 257,
  7410, 3303, 2856, 51528], "temperature": 0.0, "avg_logprob": -0.09471610260009766,
  "compression_ratio": 1.8108108108108107, "no_speech_prob": 0.007828890345990658},
  {"id": 721, "seek": 431768, "start": 4340.96, "end": 4346.320000000001, "text":
  " model, right? So it''s not surprising. It can do things like translation. It''s
  very good at", "tokens": [51528, 2316, 11, 558, 30, 407, 309, 311, 406, 8830, 13,
  467, 393, 360, 721, 411, 12853, 13, 467, 311, 588, 665, 412, 51796], "temperature":
  0.0, "avg_logprob": -0.09471610260009766, "compression_ratio": 1.8108108108108107,
  "no_speech_prob": 0.007828890345990658}, {"id": 722, "seek": 434632, "start": 4346.32,
  "end": 4351.2, "text": " rewriting a query to make it broader. It knows how to rewrite
  a query to make it Boolean. Those", "tokens": [50364, 319, 19868, 257, 14581, 281,
  652, 309, 13227, 13, 467, 3255, 577, 281, 28132, 257, 14581, 281, 652, 309, 23351,
  28499, 13, 3950, 50608], "temperature": 0.0, "avg_logprob": -0.15012995923151734,
  "compression_ratio": 1.6619718309859155, "no_speech_prob": 0.002547267824411392},
  {"id": 723, "seek": 434632, "start": 4351.2, "end": 4356.5599999999995, "text":
  " are never going to change. But getting the data to it. Again, if you want to build
  the chat GPT", "tokens": [50608, 366, 1128, 516, 281, 1319, 13, 583, 1242, 264,
  1412, 281, 309, 13, 3764, 11, 498, 291, 528, 281, 1322, 264, 5081, 26039, 51, 50876],
  "temperature": 0.0, "avg_logprob": -0.15012995923151734, "compression_ratio": 1.6619718309859155,
  "no_speech_prob": 0.002547267824411392}, {"id": 724, "seek": 434632, "start": 4356.5599999999995,
  "end": 4362.0, "text": " of mortgage exception handling, you''re going to need to
  pull a lot of internal data, label it carefully.", "tokens": [50876, 295, 20236,
  11183, 13175, 11, 291, 434, 516, 281, 643, 281, 2235, 257, 688, 295, 6920, 1412,
  11, 7645, 309, 7500, 13, 51148], "temperature": 0.0, "avg_logprob": -0.15012995923151734,
  "compression_ratio": 1.6619718309859155, "no_speech_prob": 0.002547267824411392},
  {"id": 725, "seek": 434632, "start": 4362.96, "end": 4368.16, "text": " That''s
  that, and that, and you might discover you don''t have enough. That could also be
  the case.", "tokens": [51196, 663, 311, 300, 11, 293, 300, 11, 293, 291, 1062, 4411,
  291, 500, 380, 362, 1547, 13, 663, 727, 611, 312, 264, 1389, 13, 51456], "temperature":
  0.0, "avg_logprob": -0.15012995923151734, "compression_ratio": 1.6619718309859155,
  "no_speech_prob": 0.002547267824411392}, {"id": 726, "seek": 434632, "start": 4368.16,
  "end": 4372.32, "text": " There''s a whole synthetic data market that''s ready to
  solve that problem. So,", "tokens": [51456, 821, 311, 257, 1379, 23420, 1412, 2142,
  300, 311, 1919, 281, 5039, 300, 1154, 13, 407, 11, 51664], "temperature": 0.0, "avg_logprob":
  -0.15012995923151734, "compression_ratio": 1.6619718309859155, "no_speech_prob":
  0.002547267824411392}, {"id": 727, "seek": 437232, "start": 4373.28, "end": 4377.04,
  "text": " but in a larger surprise, I think it''s much more of the other problem.
  We can''t get to it. We know", "tokens": [50412, 457, 294, 257, 4833, 6365, 11,
  286, 519, 309, 311, 709, 544, 295, 264, 661, 1154, 13, 492, 393, 380, 483, 281,
  309, 13, 492, 458, 50600], "temperature": 0.0, "avg_logprob": -0.19560877482096353,
  "compression_ratio": 1.5387596899224807, "no_speech_prob": 0.009804571978747845},
  {"id": 728, "seek": 437232, "start": 4377.04, "end": 4384.5599999999995, "text":
  " it''s there. On that front, have you actually considered implementing a chat GPT
  plugin so that I can go", "tokens": [50600, 309, 311, 456, 13, 1282, 300, 1868,
  11, 362, 291, 767, 4888, 18114, 257, 5081, 26039, 51, 23407, 370, 300, 286, 393,
  352, 50976], "temperature": 0.0, "avg_logprob": -0.19560877482096353, "compression_ratio":
  1.5387596899224807, "no_speech_prob": 0.009804571978747845}, {"id": 729, "seek":
  437232, "start": 4384.5599999999995, "end": 4391.04, "text": " as a user configure
  things at my tokens? And now, boom, I can search my internal data lakes.", "tokens":
  [50976, 382, 257, 4195, 22162, 721, 412, 452, 22667, 30, 400, 586, 11, 9351, 11,
  286, 393, 3164, 452, 6920, 1412, 25595, 13, 51300], "temperature": 0.0, "avg_logprob":
  -0.19560877482096353, "compression_ratio": 1.5387596899224807, "no_speech_prob":
  0.009804571978747845}, {"id": 730, "seek": 437232, "start": 4391.92, "end": 4397.84,
  "text": " So we have, we are integrated with chat GPT. There''s a connector so you
  can query it. We, by default,", "tokens": [51344, 407, 321, 362, 11, 321, 366, 10919,
  365, 5081, 26039, 51, 13, 821, 311, 257, 19127, 370, 291, 393, 14581, 309, 13, 492,
  11, 538, 7576, 11, 51640], "temperature": 0.0, "avg_logprob": -0.19560877482096353,
  "compression_ratio": 1.5387596899224807, "no_speech_prob": 0.009804571978747845},
  {"id": 731, "seek": 439784, "start": 4397.84, "end": 4401.84, "text": " send every
  query to it. We also have a query processor, and we will soon have a result", "tokens":
  [50364, 2845, 633, 14581, 281, 309, 13, 492, 611, 362, 257, 14581, 15321, 11, 293,
  321, 486, 2321, 362, 257, 1874, 50564], "temperature": 0.0, "avg_logprob": -0.12579126594480405,
  "compression_ratio": 1.7132616487455197, "no_speech_prob": 0.006975292693823576},
  {"id": 732, "seek": 439784, "start": 4401.84, "end": 4406.8, "text": " processor
  that will summarize your results for you. But frankly, I think several people have
  already", "tokens": [50564, 15321, 300, 486, 20858, 428, 3542, 337, 291, 13, 583,
  11939, 11, 286, 519, 2940, 561, 362, 1217, 50812], "temperature": 0.0, "avg_logprob":
  -0.12579126594480405, "compression_ratio": 1.7132616487455197, "no_speech_prob":
  0.006975292693823576}, {"id": 733, "seek": 439784, "start": 4406.8, "end": 4412.16,
  "text": " done stuff like that. So you just copy and paste the links. You can probably
  get that. I think that''s", "tokens": [50812, 1096, 1507, 411, 300, 13, 407, 291,
  445, 5055, 293, 9163, 264, 6123, 13, 509, 393, 1391, 483, 300, 13, 286, 519, 300,
  311, 51080], "temperature": 0.0, "avg_logprob": -0.12579126594480405, "compression_ratio":
  1.7132616487455197, "no_speech_prob": 0.006975292693823576}, {"id": 734, "seek":
  439784, "start": 4413.68, "end": 4417.6, "text": " that''s really an essential piece
  of it. Now, to query, like generate queries from chat GPT,", "tokens": [51156, 300,
  311, 534, 364, 7115, 2522, 295, 309, 13, 823, 11, 281, 14581, 11, 411, 8460, 24109,
  490, 5081, 26039, 51, 11, 51352], "temperature": 0.0, "avg_logprob": -0.12579126594480405,
  "compression_ratio": 1.7132616487455197, "no_speech_prob": 0.006975292693823576},
  {"id": 735, "seek": 439784, "start": 4417.6, "end": 4422.56, "text": " I think that''s
  easy to do. Right. Someone can do that. But this is my point. There will be other",
  "tokens": [51352, 286, 519, 300, 311, 1858, 281, 360, 13, 1779, 13, 8734, 393, 360,
  300, 13, 583, 341, 307, 452, 935, 13, 821, 486, 312, 661, 51600], "temperature":
  0.0, "avg_logprob": -0.12579126594480405, "compression_ratio": 1.7132616487455197,
  "no_speech_prob": 0.006975292693823576}, {"id": 736, "seek": 442256, "start": 4423.120000000001,
  "end": 4428.240000000001, "text": " GPs. We refer to chat GPT as a question answer,
  right? Or questions. If you say question, Colin,", "tokens": [50392, 460, 23043,
  13, 492, 2864, 281, 5081, 26039, 51, 382, 257, 1168, 1867, 11, 558, 30, 1610, 1651,
  13, 759, 291, 584, 1168, 11, 29253, 11, 50648], "temperature": 0.0, "avg_logprob":
  -0.17330613683481685, "compression_ratio": 1.7014388489208634, "no_speech_prob":
  0.008556035347282887}, {"id": 737, "seek": 442256, "start": 4428.240000000001, "end":
  4433.280000000001, "text": " put your question in. We''ll send it to chat GPT. I
  am sure people are looking at the amazing", "tokens": [50648, 829, 428, 1168, 294,
  13, 492, 603, 2845, 309, 281, 5081, 26039, 51, 13, 286, 669, 988, 561, 366, 1237,
  412, 264, 2243, 50900], "temperature": 0.0, "avg_logprob": -0.17330613683481685,
  "compression_ratio": 1.7014388489208634, "no_speech_prob": 0.008556035347282887},
  {"id": 738, "seek": 442256, "start": 4433.280000000001, "end": 4438.96, "text":
  " platforms you''ve just mentioned, right? All of them. Those are going to end up
  deployed in different", "tokens": [50900, 9473, 291, 600, 445, 2835, 11, 558, 30,
  1057, 295, 552, 13, 3950, 366, 516, 281, 917, 493, 17826, 294, 819, 51184], "temperature":
  0.0, "avg_logprob": -0.17330613683481685, "compression_ratio": 1.7014388489208634,
  "no_speech_prob": 0.008556035347282887}, {"id": 739, "seek": 442256, "start": 4438.96,
  "end": 4446.96, "text": " parts of the enterprise, answering questions, summarizing,
  extracting, predicting, prescribing.", "tokens": [51184, 3166, 295, 264, 14132,
  11, 13430, 1651, 11, 14611, 3319, 11, 49844, 11, 32884, 11, 1183, 39541, 13, 51584],
  "temperature": 0.0, "avg_logprob": -0.17330613683481685, "compression_ratio": 1.7014388489208634,
  "no_speech_prob": 0.008556035347282887}, {"id": 740, "seek": 442256, "start": 4446.96,
  "end": 4450.4800000000005, "text": " There will be all those things out there. And
  the key will be, how do you get at them?", "tokens": [51584, 821, 486, 312, 439,
  729, 721, 484, 456, 13, 400, 264, 2141, 486, 312, 11, 577, 360, 291, 483, 412, 552,
  30, 51760], "temperature": 0.0, "avg_logprob": -0.17330613683481685, "compression_ratio":
  1.7014388489208634, "no_speech_prob": 0.008556035347282887}, {"id": 741, "seek":
  445048, "start": 4451.44, "end": 4455.44, "text": " Yeah. It''s still the problem.
  Right. Just because you have something that will comment on the", "tokens": [50412,
  865, 13, 467, 311, 920, 264, 1154, 13, 1779, 13, 1449, 570, 291, 362, 746, 300,
  486, 2871, 322, 264, 50612], "temperature": 0.0, "avg_logprob": -0.1542581266111082,
  "compression_ratio": 1.6512455516014235, "no_speech_prob": 0.010725785978138447},
  {"id": 742, "seek": 445048, "start": 4455.44, "end": 4461.679999999999, "text":
  " financial implications of a federal rule change, for example, right? Doesn''t
  mean anyone''s going to", "tokens": [50612, 4669, 16602, 295, 257, 6019, 4978, 1319,
  11, 337, 1365, 11, 558, 30, 12955, 380, 914, 2878, 311, 516, 281, 50924], "temperature":
  0.0, "avg_logprob": -0.1542581266111082, "compression_ratio": 1.6512455516014235,
  "no_speech_prob": 0.010725785978138447}, {"id": 743, "seek": 445048, "start": 4461.679999999999,
  "end": 4467.839999999999, "text": " go look at it. So, but if you made sure that
  every day or whatever it is or every that we were", "tokens": [50924, 352, 574,
  412, 309, 13, 407, 11, 457, 498, 291, 1027, 988, 300, 633, 786, 420, 2035, 309,
  307, 420, 633, 300, 321, 645, 51232], "temperature": 0.0, "avg_logprob": -0.1542581266111082,
  "compression_ratio": 1.6512455516014235, "no_speech_prob": 0.010725785978138447},
  {"id": 744, "seek": 445048, "start": 4467.839999999999, "end": 4472.48, "text":
  " checking for new temporal updates from that and those were being pushed out to
  the people who", "tokens": [51232, 8568, 337, 777, 30881, 9205, 490, 300, 293, 729,
  645, 885, 9152, 484, 281, 264, 561, 567, 51464], "temperature": 0.0, "avg_logprob":
  -0.1542581266111082, "compression_ratio": 1.6512455516014235, "no_speech_prob":
  0.010725785978138447}, {"id": 745, "seek": 445048, "start": 4472.48, "end": 4475.919999999999,
  "text": " needed to know that and read it, especially if you could check that they
  read it.", "tokens": [51464, 2978, 281, 458, 300, 293, 1401, 309, 11, 2318, 498,
  291, 727, 1520, 300, 436, 1401, 309, 13, 51636], "temperature": 0.0, "avg_logprob":
  -0.1542581266111082, "compression_ratio": 1.6512455516014235, "no_speech_prob":
  0.010725785978138447}, {"id": 746, "seek": 447592, "start": 4476.4, "end": 4483.28,
  "text": " If you could imagine doing something like pushing information to analysts
  or somebody who''s", "tokens": [50388, 759, 291, 727, 3811, 884, 746, 411, 7380,
  1589, 281, 31388, 420, 2618, 567, 311, 50732], "temperature": 0.0, "avg_logprob":
  -0.12917191529076946, "compression_ratio": 1.7364864864864864, "no_speech_prob":
  0.006023196037858725}, {"id": 747, "seek": 447592, "start": 4483.28, "end": 4486.96,
  "text": " taking action on it and then tracking to see who read it and then watching
  their performance,", "tokens": [50732, 1940, 3069, 322, 309, 293, 550, 11603, 281,
  536, 567, 1401, 309, 293, 550, 1976, 641, 3389, 11, 50916], "temperature": 0.0,
  "avg_logprob": -0.12917191529076946, "compression_ratio": 1.7364864864864864, "no_speech_prob":
  0.006023196037858725}, {"id": 748, "seek": 447592, "start": 4487.92, "end": 4490.96,
  "text": " I am sure that that will be a thing in the financial services world.",
  "tokens": [50964, 286, 669, 988, 300, 300, 486, 312, 257, 551, 294, 264, 4669, 3328,
  1002, 13, 51116], "temperature": 0.0, "avg_logprob": -0.12917191529076946, "compression_ratio":
  1.7364864864864864, "no_speech_prob": 0.006023196037858725}, {"id": 749, "seek":
  447592, "start": 4492.0, "end": 4496.32, "text": " You know, it''s a tough world.
  There''s very used to a high level of governance, if you will,", "tokens": [51168,
  509, 458, 11, 309, 311, 257, 4930, 1002, 13, 821, 311, 588, 1143, 281, 257, 1090,
  1496, 295, 17449, 11, 498, 291, 486, 11, 51384], "temperature": 0.0, "avg_logprob":
  -0.12917191529076946, "compression_ratio": 1.7364864864864864, "no_speech_prob":
  0.006023196037858725}, {"id": 750, "seek": 447592, "start": 4496.32, "end": 4500.64,
  "text": " but I think that that''s the kind of system that will ultimately produce
  the automation", "tokens": [51384, 457, 286, 519, 300, 300, 311, 264, 733, 295,
  1185, 300, 486, 6284, 5258, 264, 17769, 51600], "temperature": 0.0, "avg_logprob":
  -0.12917191529076946, "compression_ratio": 1.7364864864864864, "no_speech_prob":
  0.006023196037858725}, {"id": 751, "seek": 447592, "start": 4501.36, "end": 4505.36,
  "text": " where the chat GPT will be able to solve the mortgage exception. So, on
  its own,", "tokens": [51636, 689, 264, 5081, 26039, 51, 486, 312, 1075, 281, 5039,
  264, 20236, 11183, 13, 407, 11, 322, 1080, 1065, 11, 51836], "temperature": 0.0,
  "avg_logprob": -0.12917191529076946, "compression_ratio": 1.7364864864864864, "no_speech_prob":
  0.006023196037858725}, {"id": 752, "seek": 450592, "start": 4505.92, "end": 4509.04,
  "text": " 90% of the time, right? 10% of the time engaging a human.", "tokens":
  [50364, 4289, 4, 295, 264, 565, 11, 558, 30, 1266, 4, 295, 264, 565, 11268, 257,
  1952, 13, 50520], "temperature": 0.0, "avg_logprob": -0.15538631690727486, "compression_ratio":
  1.5023041474654377, "no_speech_prob": 0.002235033782199025}, {"id": 753, "seek":
  450592, "start": 4510.56, "end": 4518.0, "text": " Yes. That''s somewhat scary,
  but I think it could also be liberating if done well. And I think", "tokens": [50596,
  1079, 13, 663, 311, 8344, 6958, 11, 457, 286, 519, 309, 727, 611, 312, 6774, 990,
  498, 1096, 731, 13, 400, 286, 519, 50968], "temperature": 0.0, "avg_logprob": -0.15538631690727486,
  "compression_ratio": 1.5023041474654377, "no_speech_prob": 0.002235033782199025},
  {"id": 754, "seek": 450592, "start": 4518.0, "end": 4523.4400000000005, "text":
  " there is a big discussion on this topic going on. How do we collectively as a
  humanity,", "tokens": [50968, 456, 307, 257, 955, 5017, 322, 341, 4829, 516, 322,
  13, 1012, 360, 321, 24341, 382, 257, 10243, 11, 51240], "temperature": 0.0, "avg_logprob":
  -0.15538631690727486, "compression_ratio": 1.5023041474654377, "no_speech_prob":
  0.002235033782199025}, {"id": 755, "seek": 450592, "start": 4524.0, "end": 4530.4,
  "text": " you know, make sure that this tech doesn''t host us, right? Doesn''t just
  kick us out of", "tokens": [51268, 291, 458, 11, 652, 988, 300, 341, 7553, 1177,
  380, 3975, 505, 11, 558, 30, 12955, 380, 445, 4437, 505, 484, 295, 51588], "temperature":
  0.0, "avg_logprob": -0.15538631690727486, "compression_ratio": 1.5023041474654377,
  "no_speech_prob": 0.002235033782199025}, {"id": 756, "seek": 453040, "start": 4531.04,
  "end": 4540.0, "text": " our professions or, you know, we still have a way to, I
  mean, even just going back to yesterday''s", "tokens": [50396, 527, 38129, 420,
  11, 291, 458, 11, 321, 920, 362, 257, 636, 281, 11, 286, 914, 11, 754, 445, 516,
  646, 281, 5186, 311, 50844], "temperature": 0.0, "avg_logprob": -0.13544075375511533,
  "compression_ratio": 1.6016260162601625, "no_speech_prob": 0.02668783999979496},
  {"id": 757, "seek": 453040, "start": 4540.0, "end": 4545.2, "text": " example, I
  was going really in circles. I was just drawing some pins on the map using chat
  GPT.", "tokens": [50844, 1365, 11, 286, 390, 516, 534, 294, 13040, 13, 286, 390,
  445, 6316, 512, 16392, 322, 264, 4471, 1228, 5081, 26039, 51, 13, 51104], "temperature":
  0.0, "avg_logprob": -0.13544075375511533, "compression_ratio": 1.6016260162601625,
  "no_speech_prob": 0.02668783999979496}, {"id": 758, "seek": 453040, "start": 4545.2,
  "end": 4551.2, "text": " And it couldn''t get exactly the crux of what I was asking.
  And so I went to the kitchen. I thought,", "tokens": [51104, 400, 309, 2809, 380,
  483, 2293, 264, 5140, 87, 295, 437, 286, 390, 3365, 13, 400, 370, 286, 1437, 281,
  264, 6525, 13, 286, 1194, 11, 51404], "temperature": 0.0, "avg_logprob": -0.13544075375511533,
  "compression_ratio": 1.6016260162601625, "no_speech_prob": 0.02668783999979496},
  {"id": 759, "seek": 453040, "start": 4551.2, "end": 4556.48, "text": " just for
  two minutes and I thought, okay, I can just break down my code in two parts without
  telling", "tokens": [51404, 445, 337, 732, 2077, 293, 286, 1194, 11, 1392, 11, 286,
  393, 445, 1821, 760, 452, 3089, 294, 732, 3166, 1553, 3585, 51668], "temperature":
  0.0, "avg_logprob": -0.13544075375511533, "compression_ratio": 1.6016260162601625,
  "no_speech_prob": 0.02668783999979496}, {"id": 760, "seek": 455648, "start": 4556.48,
  "end": 4561.44, "text": " chat GPT what I''m doing and just run everything in my
  ID and boom, I''m done because I was", "tokens": [50364, 5081, 26039, 51, 437, 286,
  478, 884, 293, 445, 1190, 1203, 294, 452, 7348, 293, 9351, 11, 286, 478, 1096, 570,
  286, 390, 50612], "temperature": 0.0, "avg_logprob": -0.1262016607367474, "compression_ratio":
  1.5446808510638297, "no_speech_prob": 0.024406125769019127}, {"id": 761, "seek":
  455648, "start": 4561.44, "end": 4568.799999999999, "text": " reasonably going in
  circles. And maybe it''s just me unable to, you know, engineer better prompt,",
  "tokens": [50612, 23551, 516, 294, 13040, 13, 400, 1310, 309, 311, 445, 385, 11299,
  281, 11, 291, 458, 11, 11403, 1101, 12391, 11, 50980], "temperature": 0.0, "avg_logprob":
  -0.1262016607367474, "compression_ratio": 1.5446808510638297, "no_speech_prob":
  0.024406125769019127}, {"id": 762, "seek": 455648, "start": 4568.799999999999, "end":
  4575.12, "text": " so engineer better questions. Or maybe chat GPT does have limitations
  as well. You never know.", "tokens": [50980, 370, 11403, 1101, 1651, 13, 1610, 1310,
  5081, 26039, 51, 775, 362, 15705, 382, 731, 13, 509, 1128, 458, 13, 51296], "temperature":
  0.0, "avg_logprob": -0.1262016607367474, "compression_ratio": 1.5446808510638297,
  "no_speech_prob": 0.024406125769019127}, {"id": 763, "seek": 455648, "start": 4575.839999999999,
  "end": 4581.599999999999, "text": " But it did help me probably like 90% of the
  work was done using that interaction.", "tokens": [51332, 583, 309, 630, 854, 385,
  1391, 411, 4289, 4, 295, 264, 589, 390, 1096, 1228, 300, 9285, 13, 51620], "temperature":
  0.0, "avg_logprob": -0.1262016607367474, "compression_ratio": 1.5446808510638297,
  "no_speech_prob": 0.024406125769019127}, {"id": 764, "seek": 458160, "start": 4582.400000000001,
  "end": 4587.360000000001, "text": " Like I would have spent several half a days
  as they call them or whatever evenings,", "tokens": [50404, 1743, 286, 576, 362,
  4418, 2940, 1922, 257, 1708, 382, 436, 818, 552, 420, 2035, 42835, 11, 50652], "temperature":
  0.0, "avg_logprob": -0.20467409369063705, "compression_ratio": 1.4757281553398058,
  "no_speech_prob": 0.020998766645789146}, {"id": 765, "seek": 458160, "start": 4587.360000000001,
  "end": 4592.64, "text": " figuring out all these things. Like what library should
  they use to connect to open source", "tokens": [50652, 15213, 484, 439, 613, 721,
  13, 1743, 437, 6405, 820, 436, 764, 281, 1745, 281, 1269, 4009, 50916], "temperature":
  0.0, "avg_logprob": -0.20467409369063705, "compression_ratio": 1.4757281553398058,
  "no_speech_prob": 0.020998766645789146}, {"id": 766, "seek": 458160, "start": 4595.04,
  "end": 4598.72, "text": " map or whatever. You know, how do I drop pins?", "tokens":
  [51036, 4471, 420, 2035, 13, 509, 458, 11, 577, 360, 286, 3270, 16392, 30, 51220],
  "temperature": 0.0, "avg_logprob": -0.20467409369063705, "compression_ratio": 1.4757281553398058,
  "no_speech_prob": 0.020998766645789146}, {"id": 767, "seek": 458160, "start": 4600.240000000001,
  "end": 4607.280000000001, "text": " Absolutely. The chat GPT is the perfect replacement
  for the more senior developer,", "tokens": [51296, 7021, 13, 440, 5081, 26039, 51,
  307, 264, 2176, 14419, 337, 264, 544, 7965, 10754, 11, 51648], "temperature": 0.0,
  "avg_logprob": -0.20467409369063705, "compression_ratio": 1.4757281553398058, "no_speech_prob":
  0.020998766645789146}, {"id": 768, "seek": 460728, "start": 4607.28, "end": 4611.759999999999,
  "text": " who will answer your texts right or your Slack, sorry Dave, my name''s
  mine.", "tokens": [50364, 567, 486, 1867, 428, 15765, 558, 420, 428, 37211, 11,
  2597, 11017, 11, 452, 1315, 311, 3892, 13, 50588], "temperature": 0.0, "avg_logprob":
  -0.2849465647051411, "compression_ratio": 1.6498194945848375, "no_speech_prob":
  0.004442207049578428}, {"id": 769, "seek": 460728, "start": 4612.639999999999, "end":
  4617.2, "text": " You know, like that used to do work until you''re blocked and
  then you go find somebody and say,", "tokens": [50632, 509, 458, 11, 411, 300, 1143,
  281, 360, 589, 1826, 291, 434, 15470, 293, 550, 291, 352, 915, 2618, 293, 584, 11,
  50860], "temperature": 0.0, "avg_logprob": -0.2849465647051411, "compression_ratio":
  1.6498194945848375, "no_speech_prob": 0.004442207049578428}, {"id": 770, "seek":
  460728, "start": 4617.2, "end": 4623.44, "text": " okay, so I can''t figure this
  out. This was pre-internet, right? Now, for a long time, we had stack trace or",
  "tokens": [50860, 1392, 11, 370, 286, 393, 380, 2573, 341, 484, 13, 639, 390, 659,
  12, 259, 2231, 302, 11, 558, 30, 823, 11, 337, 257, 938, 565, 11, 321, 632, 8630,
  13508, 420, 51172], "temperature": 0.0, "avg_logprob": -0.2849465647051411, "compression_ratio":
  1.6498194945848375, "no_speech_prob": 0.004442207049578428}, {"id": 771, "seek":
  460728, "start": 4626.16, "end": 4630.5599999999995, "text": " the other thing that
  chat GPT has completely revised. Yeah, stack overflow.", "tokens": [51308, 264,
  661, 551, 300, 5081, 26039, 51, 575, 2584, 35228, 13, 865, 11, 8630, 37772, 13,
  51528], "temperature": 0.0, "avg_logprob": -0.2849465647051411, "compression_ratio":
  1.6498194945848375, "no_speech_prob": 0.004442207049578428}, {"id": 772, "seek":
  460728, "start": 4631.28, "end": 4636.32, "text": " Stack overflow. Right. Exactly.
  Now it is we have stack overflow. For a while, we had stack overflow.", "tokens":
  [51564, 37649, 37772, 13, 1779, 13, 7587, 13, 823, 309, 307, 321, 362, 8630, 37772,
  13, 1171, 257, 1339, 11, 321, 632, 8630, 37772, 13, 51816], "temperature": 0.0,
  "avg_logprob": -0.2849465647051411, "compression_ratio": 1.6498194945848375, "no_speech_prob":
  0.004442207049578428}, {"id": 773, "seek": 463632, "start": 4636.32, "end": 4640.16,
  "text": " And then now chat GPT, it''s funny. I forgot the name because I use chat
  GPT instead.", "tokens": [50364, 400, 550, 586, 5081, 26039, 51, 11, 309, 311, 4074,
  13, 286, 5298, 264, 1315, 570, 286, 764, 5081, 26039, 51, 2602, 13, 50556], "temperature":
  0.0, "avg_logprob": -0.14326433371041566, "compression_ratio": 1.6114864864864864,
  "no_speech_prob": 0.0007970345322974026}, {"id": 774, "seek": 463632, "start": 4640.16,
  "end": 4646.4, "text": " I haven''t Googled for a code thing in so long. I can''t
  even replace your habit, right? Your memory", "tokens": [50556, 286, 2378, 380,
  45005, 1493, 337, 257, 3089, 551, 294, 370, 938, 13, 286, 393, 380, 754, 7406, 428,
  7164, 11, 558, 30, 2260, 4675, 50868], "temperature": 0.0, "avg_logprob": -0.14326433371041566,
  "compression_ratio": 1.6114864864864864, "no_speech_prob": 0.0007970345322974026},
  {"id": 775, "seek": 463632, "start": 4646.4, "end": 4651.12, "text": " and habit
  in some sense. Yeah. Well, you know, we all get good at evaluating those, right?",
  "tokens": [50868, 293, 7164, 294, 512, 2020, 13, 865, 13, 1042, 11, 291, 458, 11,
  321, 439, 483, 665, 412, 27479, 729, 11, 558, 30, 51104], "temperature": 0.0, "avg_logprob":
  -0.14326433371041566, "compression_ratio": 1.6114864864864864, "no_speech_prob":
  0.0007970345322974026}, {"id": 776, "seek": 463632, "start": 4651.12, "end": 4655.679999999999,
  "text": " The stack overflow articles like, okay, so when''s it from? How many upvotes
  does it have? Is there a", "tokens": [51104, 440, 8630, 37772, 11290, 411, 11, 1392,
  11, 370, 562, 311, 309, 490, 30, 1012, 867, 493, 85, 17251, 775, 309, 362, 30, 1119,
  456, 257, 51332], "temperature": 0.0, "avg_logprob": -0.14326433371041566, "compression_ratio":
  1.6114864864864864, "no_speech_prob": 0.0007970345322974026}, {"id": 777, "seek":
  463632, "start": 4655.679999999999, "end": 4661.04, "text": " good response? Does
  it have the green check mark? Chat GPT is pretty much bringing you back the green",
  "tokens": [51332, 665, 4134, 30, 4402, 309, 362, 264, 3092, 1520, 1491, 30, 27503,
  26039, 51, 307, 1238, 709, 5062, 291, 646, 264, 3092, 51600], "temperature": 0.0,
  "avg_logprob": -0.14326433371041566, "compression_ratio": 1.6114864864864864, "no_speech_prob":
  0.0007970345322974026}, {"id": 778, "seek": 466104, "start": 4661.04, "end": 4666.96,
  "text": " check mark answer. So there''s no point anymore. That''s what it''s good
  at. I totally review.", "tokens": [50364, 1520, 1491, 1867, 13, 407, 456, 311, 572,
  935, 3602, 13, 663, 311, 437, 309, 311, 665, 412, 13, 286, 3879, 3131, 13, 50660],
  "temperature": 0.0, "avg_logprob": -0.15141577287153765, "compression_ratio": 1.6109215017064846,
  "no_speech_prob": 0.007223762106150389}, {"id": 779, "seek": 466104, "start": 4666.96,
  "end": 4671.92, "text": " It''s funny. You mentioned this because exactly same thought
  across my mind when I was interacting", "tokens": [50660, 467, 311, 4074, 13, 509,
  2835, 341, 570, 2293, 912, 1194, 2108, 452, 1575, 562, 286, 390, 18017, 50908],
  "temperature": 0.0, "avg_logprob": -0.15141577287153765, "compression_ratio": 1.6109215017064846,
  "no_speech_prob": 0.007223762106150389}, {"id": 780, "seek": 466104, "start": 4671.92,
  "end": 4678.8, "text": " with chat GPT. So that was like relating to my experience
  with stack overflow, doing some small", "tokens": [50908, 365, 5081, 26039, 51,
  13, 407, 300, 390, 411, 23968, 281, 452, 1752, 365, 8630, 37772, 11, 884, 512, 1359,
  51252], "temperature": 0.0, "avg_logprob": -0.15141577287153765, "compression_ratio":
  1.6109215017064846, "no_speech_prob": 0.007223762106150389}, {"id": 781, "seek":
  466104, "start": 4678.8, "end": 4684.48, "text": " Android application. And I''ve
  ran into the issue which was described in like something like 20", "tokens": [51252,
  8853, 3861, 13, 400, 286, 600, 5872, 666, 264, 2734, 597, 390, 7619, 294, 411, 746,
  411, 945, 51536], "temperature": 0.0, "avg_logprob": -0.15141577287153765, "compression_ratio":
  1.6109215017064846, "no_speech_prob": 0.007223762106150389}, {"id": 782, "seek":
  466104, "start": 4684.48, "end": 4690.24, "text": " questions and answers on exactly
  same topic. And everyone had a green, you know, check mark", "tokens": [51536, 1651,
  293, 6338, 322, 2293, 912, 4829, 13, 400, 1518, 632, 257, 3092, 11, 291, 458, 11,
  1520, 1491, 51824], "temperature": 0.0, "avg_logprob": -0.15141577287153765, "compression_ratio":
  1.6109215017064846, "no_speech_prob": 0.007223762106150389}, {"id": 783, "seek":
  469024, "start": 4690.24, "end": 4697.2, "text": " upvotes, but nothing worked.
  And in the end, I found just one of them that worked. And you know,", "tokens":
  [50364, 493, 85, 17251, 11, 457, 1825, 2732, 13, 400, 294, 264, 917, 11, 286, 1352,
  445, 472, 295, 552, 300, 2732, 13, 400, 291, 458, 11, 50712], "temperature": 0.0,
  "avg_logprob": -0.12891268957228888, "compression_ratio": 1.673913043478261, "no_speech_prob":
  0.0066907997243106365}, {"id": 784, "seek": 469024, "start": 4697.2, "end": 4703.76,
  "text": " that was like the process in a way like iterative, repetitive, and also
  in some sense for", "tokens": [50712, 300, 390, 411, 264, 1399, 294, 257, 636, 411,
  17138, 1166, 11, 29404, 11, 293, 611, 294, 512, 2020, 337, 51040], "temperature":
  0.0, "avg_logprob": -0.12891268957228888, "compression_ratio": 1.673913043478261,
  "no_speech_prob": 0.0066907997243106365}, {"id": 785, "seek": 469024, "start": 4703.76,
  "end": 4709.04, "text": " trading, but then in the end, when you achieve it, you
  know, it''s fine. You achieve what you want.", "tokens": [51040, 9529, 11, 457,
  550, 294, 264, 917, 11, 562, 291, 4584, 309, 11, 291, 458, 11, 309, 311, 2489, 13,
  509, 4584, 437, 291, 528, 13, 51304], "temperature": 0.0, "avg_logprob": -0.12891268957228888,
  "compression_ratio": 1.673913043478261, "no_speech_prob": 0.0066907997243106365},
  {"id": 786, "seek": 469024, "start": 4709.04, "end": 4714.24, "text": " With chat
  GPT is somewhat similar, but the experience is different. I don''t need to type
  that much.", "tokens": [51304, 2022, 5081, 26039, 51, 307, 8344, 2531, 11, 457,
  264, 1752, 307, 819, 13, 286, 500, 380, 643, 281, 2010, 300, 709, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.12891268957228888, "compression_ratio": 1.673913043478261,
  "no_speech_prob": 0.0066907997243106365}, {"id": 787, "seek": 471424, "start": 4714.24,
  "end": 4721.12, "text": " I mean, I don''t need to type something into Google then
  go to Stackflow, you know, read this thing,", "tokens": [50364, 286, 914, 11, 286,
  500, 380, 643, 281, 2010, 746, 666, 3329, 550, 352, 281, 37649, 10565, 11, 291,
  458, 11, 1401, 341, 551, 11, 50708], "temperature": 0.0, "avg_logprob": -0.18470687095565025,
  "compression_ratio": 1.6192468619246863, "no_speech_prob": 0.016192669048905373},
  {"id": 788, "seek": 471424, "start": 4721.12, "end": 4727.599999999999, "text":
  " comprehend it, and then apply it. With chat GPT, all of this is condensed. It''s
  like all of", "tokens": [50708, 38183, 309, 11, 293, 550, 3079, 309, 13, 2022, 5081,
  26039, 51, 11, 439, 295, 341, 307, 36398, 13, 467, 311, 411, 439, 295, 51032], "temperature":
  0.0, "avg_logprob": -0.18470687095565025, "compression_ratio": 1.6192468619246863,
  "no_speech_prob": 0.016192669048905373}, {"id": 789, "seek": 471424, "start": 4727.599999999999,
  "end": 4733.04, "text": " these steps just condensed and meet just literally typing
  what I want and getting something on the screen.", "tokens": [51032, 613, 4439,
  445, 36398, 293, 1677, 445, 3736, 18444, 437, 286, 528, 293, 1242, 746, 322, 264,
  2568, 13, 51304], "temperature": 0.0, "avg_logprob": -0.18470687095565025, "compression_ratio":
  1.6192468619246863, "no_speech_prob": 0.016192669048905373}, {"id": 790, "seek":
  471424, "start": 4733.5199999999995, "end": 4741.599999999999, "text": " Right.
  This part by itself is amazing. It is hard to predict where how far that will go.",
  "tokens": [51328, 1779, 13, 639, 644, 538, 2564, 307, 2243, 13, 467, 307, 1152,
  281, 6069, 689, 577, 1400, 300, 486, 352, 13, 51732], "temperature": 0.0, "avg_logprob":
  -0.18470687095565025, "compression_ratio": 1.6192468619246863, "no_speech_prob":
  0.016192669048905373}, {"id": 791, "seek": 474160, "start": 4741.68, "end": 4749.120000000001,
  "text": " But I think that one thing is very clear. The M365 silo is probably the
  most important one going", "tokens": [50368, 583, 286, 519, 300, 472, 551, 307,
  588, 1850, 13, 440, 376, 11309, 20, 3425, 78, 307, 1391, 264, 881, 1021, 472, 516,
  50740], "temperature": 0.0, "avg_logprob": -0.1410447359085083, "compression_ratio":
  1.640495867768595, "no_speech_prob": 0.004218554589897394}, {"id": 792, "seek":
  474160, "start": 4749.120000000001, "end": 4755.92, "text": " forward because it''s
  going to kind of automatically be taking the knowledge, which is very present in",
  "tokens": [50740, 2128, 570, 309, 311, 516, 281, 733, 295, 6772, 312, 1940, 264,
  3601, 11, 597, 307, 588, 1974, 294, 51080], "temperature": 0.0, "avg_logprob": -0.1410447359085083,
  "compression_ratio": 1.640495867768595, "no_speech_prob": 0.004218554589897394},
  {"id": 793, "seek": 474160, "start": 4755.92, "end": 4760.64, "text": " outlook,
  right? Maybe not so much encounter, but in your email is a lot of knowledge there
  in teams.", "tokens": [51080, 26650, 11, 558, 30, 2704, 406, 370, 709, 8593, 11,
  457, 294, 428, 3796, 307, 257, 688, 295, 3601, 456, 294, 5491, 13, 51316], "temperature":
  0.0, "avg_logprob": -0.1410447359085083, "compression_ratio": 1.640495867768595,
  "no_speech_prob": 0.004218554589897394}, {"id": 794, "seek": 474160, "start": 4760.64,
  "end": 4765.360000000001, "text": " There''s a lot of knowledge there. Documents,
  probably a decent amount there too, although I think", "tokens": [51316, 821, 311,
  257, 688, 295, 3601, 456, 13, 16024, 4697, 11, 1391, 257, 8681, 2372, 456, 886,
  11, 4878, 286, 519, 51552], "temperature": 0.0, "avg_logprob": -0.1410447359085083,
  "compression_ratio": 1.640495867768595, "no_speech_prob": 0.004218554589897394},
  {"id": 795, "seek": 476536, "start": 4765.36, "end": 4771.12, "text": " that tends
  to be more scattered. But effectively, right? Chat GPT was trained from Reddit,",
  "tokens": [50364, 300, 12258, 281, 312, 544, 21986, 13, 583, 8659, 11, 558, 30,
  27503, 26039, 51, 390, 8895, 490, 32210, 11, 50652], "temperature": 0.0, "avg_logprob":
  -0.09605575644451639, "compression_ratio": 1.5495867768595042, "no_speech_prob":
  0.0017753250431269407}, {"id": 796, "seek": 476536, "start": 4771.12, "end": 4779.28,
  "text": " which is chat. Teams is chat. Outlook is sort of chat. So there''s no
  doubt that maybe those early", "tokens": [50652, 597, 307, 5081, 13, 24702, 307,
  5081, 13, 5925, 12747, 307, 1333, 295, 5081, 13, 407, 456, 311, 572, 6385, 300,
  1310, 729, 2440, 51060], "temperature": 0.0, "avg_logprob": -0.09605575644451639,
  "compression_ratio": 1.5495867768595042, "no_speech_prob": 0.0017753250431269407},
  {"id": 797, "seek": 476536, "start": 4779.28, "end": 4785.5199999999995, "text":
  " interactions will come through that channel. But I do think that exactly as you
  said early on,", "tokens": [51060, 13280, 486, 808, 807, 300, 2269, 13, 583, 286,
  360, 519, 300, 2293, 382, 291, 848, 2440, 322, 11, 51372], "temperature": 0.0, "avg_logprob":
  -0.09605575644451639, "compression_ratio": 1.5495867768595042, "no_speech_prob":
  0.0017753250431269407}, {"id": 798, "seek": 476536, "start": 4785.5199999999995,
  "end": 4790.719999999999, "text": " Microsoft is never going to make it easy to
  talk to anybody else. They still come from that", "tokens": [51372, 8116, 307, 1128,
  516, 281, 652, 309, 1858, 281, 751, 281, 4472, 1646, 13, 814, 920, 808, 490, 300,
  51632], "temperature": 0.0, "avg_logprob": -0.09605575644451639, "compression_ratio":
  1.5495867768595042, "no_speech_prob": 0.0017753250431269407}, {"id": 799, "seek":
  479072, "start": 4790.8, "end": 4797.04, "text": " position of silo dominance or
  whatever it is. They don''t like to work with Salesforce.", "tokens": [50368, 2535,
  295, 3425, 78, 34987, 420, 2035, 309, 307, 13, 814, 500, 380, 411, 281, 589, 365,
  40398, 13, 50680], "temperature": 0.0, "avg_logprob": -0.15088270043814053, "compression_ratio":
  1.6293103448275863, "no_speech_prob": 0.005442452616989613}, {"id": 800, "seek":
  479072, "start": 4797.04, "end": 4803.280000000001, "text": " Salesforce doesn''t
  like to work with them. Nobody likes to use the non-great product in someone", "tokens":
  [50680, 40398, 1177, 380, 411, 281, 589, 365, 552, 13, 9297, 5902, 281, 764, 264,
  2107, 12, 40753, 1674, 294, 1580, 50992], "temperature": 0.0, "avg_logprob": -0.15088270043814053,
  "compression_ratio": 1.6293103448275863, "no_speech_prob": 0.005442452616989613},
  {"id": 801, "seek": 479072, "start": 4803.280000000001, "end": 4811.4400000000005,
  "text": " else''s stack just because we''re trying to consolidate. So that''s why
  it persists. And that is very real", "tokens": [50992, 1646, 311, 8630, 445, 570,
  321, 434, 1382, 281, 49521, 13, 407, 300, 311, 983, 309, 868, 1751, 13, 400, 300,
  307, 588, 957, 51400], "temperature": 0.0, "avg_logprob": -0.15088270043814053,
  "compression_ratio": 1.6293103448275863, "no_speech_prob": 0.005442452616989613},
  {"id": 802, "seek": 479072, "start": 4811.4400000000005, "end": 4817.6, "text":
  " and exacerbates the problem, the walls between the silos, and then throw in all
  the others.", "tokens": [51400, 293, 38819, 1024, 264, 1154, 11, 264, 7920, 1296,
  264, 48893, 11, 293, 550, 3507, 294, 439, 264, 2357, 13, 51708], "temperature":
  0.0, "avg_logprob": -0.15088270043814053, "compression_ratio": 1.6293103448275863,
  "no_speech_prob": 0.005442452616989613}, {"id": 803, "seek": 481760, "start": 4818.08,
  "end": 4824.160000000001, "text": " After you get the basic whatever, big five,
  then you have all the elastics and open searches and", "tokens": [50388, 2381, 291,
  483, 264, 3875, 2035, 11, 955, 1732, 11, 550, 291, 362, 439, 264, 806, 21598, 293,
  1269, 26701, 293, 50692], "temperature": 0.0, "avg_logprob": -0.32651522424485946,
  "compression_ratio": 1.5051546391752577, "no_speech_prob": 0.014431041665375233},
  {"id": 804, "seek": 481760, "start": 4824.160000000001, "end": 4834.96, "text":
  " solars and postgres and to say nothing of the applications. So one group is using
  swirl to look", "tokens": [50692, 1404, 685, 293, 2183, 45189, 293, 281, 584, 1825,
  295, 264, 5821, 13, 407, 472, 1594, 307, 1228, 30310, 281, 574, 51232], "temperature":
  0.0, "avg_logprob": -0.32651522424485946, "compression_ratio": 1.5051546391752577,
  "no_speech_prob": 0.014431041665375233}, {"id": 805, "seek": 481760, "start": 4834.96,
  "end": 4840.96, "text": " at five different ticket systems. They''re all just ticket.
  You track is one from JetBrains and then", "tokens": [51232, 412, 1732, 819, 10550,
  3652, 13, 814, 434, 439, 445, 10550, 13, 509, 2837, 307, 472, 490, 28730, 45606,
  1292, 293, 550, 51532], "temperature": 0.0, "avg_logprob": -0.32651522424485946,
  "compression_ratio": 1.5051546391752577, "no_speech_prob": 0.014431041665375233},
  {"id": 806, "seek": 484096, "start": 4841.52, "end": 4849.36, "text": " you''re
  on the, there''s some others. Okay, that''s a really interesting problem. The cost
  to migrate", "tokens": [50392, 291, 434, 322, 264, 11, 456, 311, 512, 2357, 13,
  1033, 11, 300, 311, 257, 534, 1880, 1154, 13, 440, 2063, 281, 31821, 50784], "temperature":
  0.0, "avg_logprob": -0.2110749880472819, "compression_ratio": 1.617117117117117,
  "no_speech_prob": 0.02523277886211872}, {"id": 807, "seek": 484096, "start": 4849.36,
  "end": 4853.2, "text": " all that stuff would be just, it''s not even, I don''t
  think it''s necessarily that much money.", "tokens": [50784, 439, 300, 1507, 576,
  312, 445, 11, 309, 311, 406, 754, 11, 286, 500, 380, 519, 309, 311, 4725, 300, 709,
  1460, 13, 50976], "temperature": 0.0, "avg_logprob": -0.2110749880472819, "compression_ratio":
  1.617117117117117, "no_speech_prob": 0.02523277886211872}, {"id": 808, "seek": 484096,
  "start": 4853.2, "end": 4858.88, "text": " It''s just a massive amount of pain.
  If you could figure out how to do it, probably some transfer", "tokens": [50976,
  467, 311, 445, 257, 5994, 2372, 295, 1822, 13, 759, 291, 727, 2573, 484, 577, 281,
  360, 309, 11, 1391, 512, 5003, 51260], "temperature": 0.0, "avg_logprob": -0.2110749880472819,
  "compression_ratio": 1.617117117117117, "no_speech_prob": 0.02523277886211872},
  {"id": 809, "seek": 484096, "start": 4858.88, "end": 4863.04, "text": " much, it''s
  not that much money, but it is a tremendous amount of work.", "tokens": [51260,
  709, 11, 309, 311, 406, 300, 709, 1460, 11, 457, 309, 307, 257, 10048, 2372, 295,
  589, 13, 51468], "temperature": 0.0, "avg_logprob": -0.2110749880472819, "compression_ratio":
  1.617117117117117, "no_speech_prob": 0.02523277886211872}, {"id": 810, "seek": 486304,
  "start": 4863.6, "end": 4872.08, "text": " Yes, I think you probably don''t realize
  yourself yet, but from the way you explain this,", "tokens": [50392, 1079, 11, 286,
  519, 291, 1391, 500, 380, 4325, 1803, 1939, 11, 457, 490, 264, 636, 291, 2903, 341,
  11, 50816], "temperature": 0.0, "avg_logprob": -0.16856873736662023, "compression_ratio":
  1.4615384615384615, "no_speech_prob": 0.07404676079750061}, {"id": 811, "seek":
  486304, "start": 4872.08, "end": 4878.24, "text": " it feels like you''ve invented
  JetGPT for the search part. I mean, in some sense,", "tokens": [50816, 309, 3417,
  411, 291, 600, 14479, 28730, 38, 47, 51, 337, 264, 3164, 644, 13, 286, 914, 11,
  294, 512, 2020, 11, 51124], "temperature": 0.0, "avg_logprob": -0.16856873736662023,
  "compression_ratio": 1.4615384615384615, "no_speech_prob": 0.07404676079750061},
  {"id": 812, "seek": 486304, "start": 4879.04, "end": 4887.76, "text": " like simplifying
  things, not actually, as you said, not requesting anyone to physically reinvent",
  "tokens": [51164, 411, 6883, 5489, 721, 11, 406, 767, 11, 382, 291, 848, 11, 406,
  31937, 2878, 281, 9762, 33477, 51600], "temperature": 0.0, "avg_logprob": -0.16856873736662023,
  "compression_ratio": 1.4615384615384615, "no_speech_prob": 0.07404676079750061},
  {"id": 813, "seek": 488776, "start": 4887.84, "end": 4893.68, "text": " things like
  move data here and there, which can take years, sometimes like dozens of years,",
  "tokens": [50368, 721, 411, 1286, 1412, 510, 293, 456, 11, 597, 393, 747, 924, 11,
  2171, 411, 18431, 295, 924, 11, 50660], "temperature": 0.0, "avg_logprob": -0.12154824393136161,
  "compression_ratio": 1.6891891891891893, "no_speech_prob": 0.10080519318580627},
  {"id": 814, "seek": 488776, "start": 4893.68, "end": 4902.24, "text": " people simply
  don''t do this. And also access to the data, like today, I only remember a fraction",
  "tokens": [50660, 561, 2935, 500, 380, 360, 341, 13, 400, 611, 2105, 281, 264, 1412,
  11, 411, 965, 11, 286, 787, 1604, 257, 14135, 51088], "temperature": 0.0, "avg_logprob":
  -0.12154824393136161, "compression_ratio": 1.6891891891891893, "no_speech_prob":
  0.10080519318580627}, {"id": 815, "seek": 488776, "start": 4902.24, "end": 4907.2,
  "text": " of things that I did. I literally forget things that I''ve done yesterday.
  I might sometimes", "tokens": [51088, 295, 721, 300, 286, 630, 13, 286, 3736, 2870,
  721, 300, 286, 600, 1096, 5186, 13, 286, 1062, 2171, 51336], "temperature": 0.0,
  "avg_logprob": -0.12154824393136161, "compression_ratio": 1.6891891891891893, "no_speech_prob":
  0.10080519318580627}, {"id": 816, "seek": 488776, "start": 4907.2, "end": 4913.2,
  "text": " reflect and I remember something a week ago or so, but it''s still, it''s
  because of information", "tokens": [51336, 5031, 293, 286, 1604, 746, 257, 1243,
  2057, 420, 370, 11, 457, 309, 311, 920, 11, 309, 311, 570, 295, 1589, 51636], "temperature":
  0.0, "avg_logprob": -0.12154824393136161, "compression_ratio": 1.6891891891891893,
  "no_speech_prob": 0.10080519318580627}, {"id": 817, "seek": 491320, "start": 4913.2,
  "end": 4919.2, "text": " overload, and I need to make decisions, I need to scramble
  something together quickly", "tokens": [50364, 28777, 11, 293, 286, 643, 281, 652,
  5327, 11, 286, 643, 281, 795, 48382, 746, 1214, 2661, 50664], "temperature": 0.0,
  "avg_logprob": -0.18316137635862673, "compression_ratio": 1.5566037735849056, "no_speech_prob":
  0.017945485189557076}, {"id": 818, "seek": 491320, "start": 4919.92, "end": 4926.24,
  "text": " on a conference page, how much knowledge do I have myself? And if I had
  that magical", "tokens": [50700, 322, 257, 7586, 3028, 11, 577, 709, 3601, 360,
  286, 362, 2059, 30, 400, 498, 286, 632, 300, 12066, 51016], "temperature": 0.0,
  "avg_logprob": -0.18316137635862673, "compression_ratio": 1.5566037735849056, "no_speech_prob":
  0.017945485189557076}, {"id": 819, "seek": 491320, "start": 4927.2, "end": 4932.24,
  "text": " search bar where I could have typed something and just get the support
  material,", "tokens": [51064, 3164, 2159, 689, 286, 727, 362, 33941, 746, 293, 445,
  483, 264, 1406, 2527, 11, 51316], "temperature": 0.0, "avg_logprob": -0.18316137635862673,
  "compression_ratio": 1.5566037735849056, "no_speech_prob": 0.017945485189557076},
  {"id": 820, "seek": 491320, "start": 4933.599999999999, "end": 4937.679999999999,
  "text": " not to go all over the place, essentially doing what search engines should
  do,", "tokens": [51384, 406, 281, 352, 439, 670, 264, 1081, 11, 4476, 884, 437,
  3164, 12982, 820, 360, 11, 51588], "temperature": 0.0, "avg_logprob": -0.18316137635862673,
  "compression_ratio": 1.5566037735849056, "no_speech_prob": 0.017945485189557076},
  {"id": 821, "seek": 493768, "start": 4938.56, "end": 4943.6, "text": " just go and
  check what happened where and when and by whom?", "tokens": [50408, 445, 352, 293,
  1520, 437, 2011, 689, 293, 562, 293, 538, 7101, 30, 50660], "temperature": 0.0,
  "avg_logprob": -0.17529078892299108, "compression_ratio": 1.606425702811245, "no_speech_prob":
  0.005362936295568943}, {"id": 822, "seek": 493768, "start": 4945.04, "end": 4950.4800000000005,
  "text": " Exactly. Exactly. There''s so much amazing work and time and", "tokens":
  [50732, 7587, 13, 7587, 13, 821, 311, 370, 709, 2243, 589, 293, 565, 293, 51004],
  "temperature": 0.0, "avg_logprob": -0.17529078892299108, "compression_ratio": 1.606425702811245,
  "no_speech_prob": 0.005362936295568943}, {"id": 823, "seek": 493768, "start": 4951.280000000001,
  "end": 4954.88, "text": " genius that''s gone into some of these apps. I mean, who
  doesn''t love them? Like they''re,", "tokens": [51044, 14017, 300, 311, 2780, 666,
  512, 295, 613, 7733, 13, 286, 914, 11, 567, 1177, 380, 959, 552, 30, 1743, 436,
  434, 11, 51224], "temperature": 0.0, "avg_logprob": -0.17529078892299108, "compression_ratio":
  1.606425702811245, "no_speech_prob": 0.005362936295568943}, {"id": 824, "seek":
  493768, "start": 4955.4400000000005, "end": 4961.04, "text": " you know, they all
  have incredible capabilities and they''re evolved, they''re growing all the time.",
  "tokens": [51252, 291, 458, 11, 436, 439, 362, 4651, 10862, 293, 436, 434, 14178,
  11, 436, 434, 4194, 439, 264, 565, 13, 51532], "temperature": 0.0, "avg_logprob":
  -0.17529078892299108, "compression_ratio": 1.606425702811245, "no_speech_prob":
  0.005362936295568943}, {"id": 825, "seek": 493768, "start": 4962.16, "end": 4966.400000000001,
  "text": " In a way, right, the idea that you would take data out to try to make
  sense of it is absurd.", "tokens": [51588, 682, 257, 636, 11, 558, 11, 264, 1558,
  300, 291, 576, 747, 1412, 484, 281, 853, 281, 652, 2020, 295, 309, 307, 19774, 13,
  51800], "temperature": 0.0, "avg_logprob": -0.17529078892299108, "compression_ratio":
  1.606425702811245, "no_speech_prob": 0.005362936295568943}, {"id": 826, "seek":
  496640, "start": 4967.04, "end": 4973.2, "text": " It really is. Think of Salesforce
  as 2,000 plus tables just to make the application work,", "tokens": [50396, 467,
  534, 307, 13, 6557, 295, 40398, 382, 568, 11, 1360, 1804, 8020, 445, 281, 652, 264,
  3861, 589, 11, 50704], "temperature": 0.0, "avg_logprob": -0.1639777981505102, "compression_ratio":
  1.5791666666666666, "no_speech_prob": 0.007999851368367672}, {"id": 827, "seek":
  496640, "start": 4973.2, "end": 4979.599999999999, "text": " you''re going to extract
  that? No, you''re going to query it. And that''s the key, right? And so", "tokens":
  [50704, 291, 434, 516, 281, 8947, 300, 30, 883, 11, 291, 434, 516, 281, 14581, 309,
  13, 400, 300, 311, 264, 2141, 11, 558, 30, 400, 370, 51024], "temperature": 0.0,
  "avg_logprob": -0.1639777981505102, "compression_ratio": 1.5791666666666666, "no_speech_prob":
  0.007999851368367672}, {"id": 828, "seek": 496640, "start": 4979.599999999999, "end":
  4984.96, "text": " we''re focused on making the querying easy and understandable
  simplicity. You know, I''ve worked on", "tokens": [51024, 321, 434, 5178, 322, 1455,
  264, 7083, 1840, 1858, 293, 25648, 25632, 13, 509, 458, 11, 286, 600, 2732, 322,
  51292], "temperature": 0.0, "avg_logprob": -0.1639777981505102, "compression_ratio":
  1.5791666666666666, "no_speech_prob": 0.007999851368367672}, {"id": 829, "seek":
  496640, "start": 4984.96, "end": 4989.92, "text": " some amazing products that were
  not simple. And I''m sorry for some of them, right? Not being that", "tokens": [51292,
  512, 2243, 3383, 300, 645, 406, 2199, 13, 400, 286, 478, 2597, 337, 512, 295, 552,
  11, 558, 30, 1726, 885, 300, 51540], "temperature": 0.0, "avg_logprob": -0.1639777981505102,
  "compression_ratio": 1.5791666666666666, "no_speech_prob": 0.007999851368367672},
  {"id": 830, "seek": 498992, "start": 4989.92, "end": 4997.2, "text": " simple, but
  at the end of the day, I think today in the enterprise, it''s got to get easier.",
  "tokens": [50364, 2199, 11, 457, 412, 264, 917, 295, 264, 786, 11, 286, 519, 965,
  294, 264, 14132, 11, 309, 311, 658, 281, 483, 3571, 13, 50728], "temperature": 0.0,
  "avg_logprob": -0.1337649167239011, "compression_ratio": 1.6604651162790698, "no_speech_prob":
  0.010883676819503307}, {"id": 831, "seek": 498992, "start": 4997.2, "end": 5001.84,
  "text": " And there''s got to be alternatives to indexing. And so thus the simplicity.",
  "tokens": [50728, 400, 456, 311, 658, 281, 312, 20478, 281, 8186, 278, 13, 400,
  370, 8807, 264, 25632, 13, 50960], "temperature": 0.0, "avg_logprob": -0.1337649167239011,
  "compression_ratio": 1.6604651162790698, "no_speech_prob": 0.010883676819503307},
  {"id": 832, "seek": 498992, "start": 5002.64, "end": 5008.8, "text": " Amazing.
  Here comes my favorite question. As we get closer to the end of this amazing podcast",
  "tokens": [51000, 14165, 13, 1692, 1487, 452, 2954, 1168, 13, 1018, 321, 483, 4966,
  281, 264, 917, 295, 341, 2243, 7367, 51308], "temperature": 0.0, "avg_logprob":
  -0.1337649167239011, "compression_ratio": 1.6604651162790698, "no_speech_prob":
  0.010883676819503307}, {"id": 833, "seek": 498992, "start": 5008.8, "end": 5017.36,
  "text": " episode, the question of why you''ve done a lot in software engineering,
  you''ve done quite a lot", "tokens": [51308, 3500, 11, 264, 1168, 295, 983, 291,
  600, 1096, 257, 688, 294, 4722, 7043, 11, 291, 600, 1096, 1596, 257, 688, 51736],
  "temperature": 0.0, "avg_logprob": -0.1337649167239011, "compression_ratio": 1.6604651162790698,
  "no_speech_prob": 0.010883676819503307}, {"id": 834, "seek": 501736, "start": 5017.36,
  "end": 5023.679999999999, "text": " in search. You mentioned on all this companies,
  you know, like fast, which, you know,", "tokens": [50364, 294, 3164, 13, 509, 2835,
  322, 439, 341, 3431, 11, 291, 458, 11, 411, 2370, 11, 597, 11, 291, 458, 11, 50680],
  "temperature": 0.0, "avg_logprob": -0.22209063212076824, "compression_ratio": 1.4806629834254144,
  "no_speech_prob": 0.0016709007322788239}, {"id": 835, "seek": 501736, "start": 5023.679999999999,
  "end": 5030.08, "text": " product became like Vespa and so on. You''re building
  swirl. Why? Like what keeps you", "tokens": [50680, 1674, 3062, 411, 691, 279, 4306,
  293, 370, 322, 13, 509, 434, 2390, 30310, 13, 1545, 30, 1743, 437, 5965, 291, 51000],
  "temperature": 0.0, "avg_logprob": -0.22209063212076824, "compression_ratio": 1.4806629834254144,
  "no_speech_prob": 0.0016709007322788239}, {"id": 836, "seek": 501736, "start": 5031.2,
  "end": 5040.4, "text": " motivated to do this? And as amazing as it is, like you''re
  doing a lot of things. And also in the", "tokens": [51056, 14515, 281, 360, 341,
  30, 400, 382, 2243, 382, 309, 307, 11, 411, 291, 434, 884, 257, 688, 295, 721, 13,
  400, 611, 294, 264, 51516], "temperature": 0.0, "avg_logprob": -0.22209063212076824,
  "compression_ratio": 1.4806629834254144, "no_speech_prob": 0.0016709007322788239},
  {"id": 837, "seek": 504040, "start": 5040.4, "end": 5050.16, "text": " open, what
  motivates you to stay in this topic of search? You know, whether or not it''s been",
  "tokens": [50364, 1269, 11, 437, 42569, 291, 281, 1754, 294, 341, 4829, 295, 3164,
  30, 509, 458, 11, 1968, 420, 406, 309, 311, 668, 50852], "temperature": 0.0, "avg_logprob":
  -0.1261233507200729, "compression_ratio": 1.5183673469387755, "no_speech_prob":
  0.0040545351803302765}, {"id": 838, "seek": 504040, "start": 5050.16, "end": 5056.0,
  "text": " searched, data integration has been the thing that I''ve always liked.
  I started my career at", "tokens": [50852, 22961, 11, 1412, 10980, 575, 668, 264,
  551, 300, 286, 600, 1009, 4501, 13, 286, 1409, 452, 3988, 412, 51144], "temperature":
  0.0, "avg_logprob": -0.1261233507200729, "compression_ratio": 1.5183673469387755,
  "no_speech_prob": 0.0040545351803302765}, {"id": 839, "seek": 504040, "start": 5056.0,
  "end": 5061.679999999999, "text": " John Hancock financial services working in marketing,
  doing customer segmentation. Interesting", "tokens": [51144, 2619, 7820, 29779,
  4669, 3328, 1364, 294, 6370, 11, 884, 5474, 9469, 399, 13, 14711, 51428], "temperature":
  0.0, "avg_logprob": -0.1261233507200729, "compression_ratio": 1.5183673469387755,
  "no_speech_prob": 0.0040545351803302765}, {"id": 840, "seek": 504040, "start": 5061.679999999999,
  "end": 5069.679999999999, "text": " stuff. But really, the problem the company couldn''t
  solve was how to view, well, completely", "tokens": [51428, 1507, 13, 583, 534,
  11, 264, 1154, 264, 2237, 2809, 380, 5039, 390, 577, 281, 1910, 11, 731, 11, 2584,
  51828], "temperature": 0.0, "avg_logprob": -0.1261233507200729, "compression_ratio":
  1.5183673469387755, "no_speech_prob": 0.0040545351803302765}, {"id": 841, "seek":
  506968, "start": 5069.68, "end": 5078.240000000001, "text": " separate product lines
  in one way. They had no idea, right? 110-year-old company had no idea", "tokens":
  [50364, 4994, 1674, 3876, 294, 472, 636, 13, 814, 632, 572, 1558, 11, 558, 30, 20154,
  12, 5294, 12, 2641, 2237, 632, 572, 1558, 50792], "temperature": 0.0, "avg_logprob":
  -0.12974620902019998, "compression_ratio": 1.5685483870967742, "no_speech_prob":
  0.004880491644144058}, {"id": 842, "seek": 506968, "start": 5078.240000000001, "end":
  5084.0, "text": " that it had a Pareto actually was somewhat worse. Like 10% or
  15% of the customers were producing", "tokens": [50792, 300, 309, 632, 257, 31189,
  1353, 767, 390, 8344, 5324, 13, 1743, 1266, 4, 420, 2119, 4, 295, 264, 4581, 645,
  10501, 51080], "temperature": 0.0, "avg_logprob": -0.12974620902019998, "compression_ratio":
  1.5685483870967742, "no_speech_prob": 0.004880491644144058}, {"id": 843, "seek":
  506968, "start": 5084.0, "end": 5089.52, "text": " 80% of the premiums. Everybody
  got treated equally. It was like a very old school business that", "tokens": [51080,
  4688, 4, 295, 264, 12049, 82, 13, 7646, 658, 8668, 12309, 13, 467, 390, 411, 257,
  588, 1331, 1395, 1606, 300, 51356], "temperature": 0.0, "avg_logprob": -0.12974620902019998,
  "compression_ratio": 1.5685483870967742, "no_speech_prob": 0.004880491644144058},
  {"id": 844, "seek": 506968, "start": 5089.52, "end": 5094.96, "text": " was all
  about customers without really understanding customers. And it was still massively
  successful.", "tokens": [51356, 390, 439, 466, 4581, 1553, 534, 3701, 4581, 13,
  400, 309, 390, 920, 29379, 4406, 13, 51628], "temperature": 0.0, "avg_logprob":
  -0.12974620902019998, "compression_ratio": 1.5685483870967742, "no_speech_prob":
  0.004880491644144058}, {"id": 845, "seek": 509496, "start": 5095.28, "end": 5100.32,
  "text": " So that''s not an act. They were one of the biggest users of technology.
  Also, Hancock had the", "tokens": [50380, 407, 300, 311, 406, 364, 605, 13, 814,
  645, 472, 295, 264, 3880, 5022, 295, 2899, 13, 2743, 11, 7820, 29779, 632, 264,
  50632], "temperature": 0.0, "avg_logprob": -0.16405684668738563, "compression_ratio":
  1.7075812274368232, "no_speech_prob": 0.025208672508597374}, {"id": 846, "seek":
  509496, "start": 5100.32, "end": 5108.16, "text": " largest IBM mainframe, I think,
  in the Northeast for many years. But the silo problem was the problem", "tokens":
  [50632, 6443, 23487, 2135, 17265, 11, 286, 519, 11, 294, 264, 42150, 337, 867, 924,
  13, 583, 264, 3425, 78, 1154, 390, 264, 1154, 51024], "temperature": 0.0, "avg_logprob":
  -0.16405684668738563, "compression_ratio": 1.7075812274368232, "no_speech_prob":
  0.025208672508597374}, {"id": 847, "seek": 509496, "start": 5108.64, "end": 5113.76,
  "text": " that we had to solve to actually take the company to the level that it
  could compete with direct", "tokens": [51048, 300, 321, 632, 281, 5039, 281, 767,
  747, 264, 2237, 281, 264, 1496, 300, 309, 727, 11831, 365, 2047, 51304], "temperature":
  0.0, "avg_logprob": -0.16405684668738563, "compression_ratio": 1.7075812274368232,
  "no_speech_prob": 0.025208672508597374}, {"id": 848, "seek": 509496, "start": 5113.76,
  "end": 5118.0, "text": " mail companies because direct mail companies had a lower
  cost basis and they knew the customer.", "tokens": [51304, 10071, 3431, 570, 2047,
  10071, 3431, 632, 257, 3126, 2063, 5143, 293, 436, 2586, 264, 5474, 13, 51516],
  "temperature": 0.0, "avg_logprob": -0.16405684668738563, "compression_ratio": 1.7075812274368232,
  "no_speech_prob": 0.025208672508597374}, {"id": 849, "seek": 509496, "start": 5119.04,
  "end": 5124.0, "text": " And that project quite honestly is the pattern that I have
  seen over and over again,", "tokens": [51568, 400, 300, 1716, 1596, 6095, 307, 264,
  5102, 300, 286, 362, 1612, 670, 293, 670, 797, 11, 51816], "temperature": 0.0, "avg_logprob":
  -0.16405684668738563, "compression_ratio": 1.7075812274368232, "no_speech_prob":
  0.025208672508597374}, {"id": 850, "seek": 512400, "start": 5124.0, "end": 5129.04,
  "text": " regardless of what venture search has been one of them. But I was really
  lucky to work on mortgage", "tokens": [50364, 10060, 295, 437, 18474, 3164, 575,
  668, 472, 295, 552, 13, 583, 286, 390, 534, 6356, 281, 589, 322, 20236, 50616],
  "temperature": 0.0, "avg_logprob": -0.1379446045965211, "compression_ratio": 1.6452702702702702,
  "no_speech_prob": 0.0015558414161205292}, {"id": 851, "seek": 512400, "start": 5129.04,
  "end": 5136.64, "text": " processing too. So a company called AI Foundry was actually
  backed by Kodak Alaris, which was the", "tokens": [50616, 9007, 886, 13, 407, 257,
  2237, 1219, 7318, 8207, 627, 390, 767, 20391, 538, 591, 378, 514, 967, 27489, 11,
  597, 390, 264, 50996], "temperature": 0.0, "avg_logprob": -0.1379446045965211, "compression_ratio":
  1.6452702702702702, "no_speech_prob": 0.0015558414161205292}, {"id": 852, "seek":
  512400, "start": 5136.64, "end": 5141.52, "text": " world leader in scanning at
  the time, right? Said, we need to come up with something to do.", "tokens": [50996,
  1002, 5263, 294, 27019, 412, 264, 565, 11, 558, 30, 26490, 11, 321, 643, 281, 808,
  493, 365, 746, 281, 360, 13, 51240], "temperature": 0.0, "avg_logprob": -0.1379446045965211,
  "compression_ratio": 1.6452702702702702, "no_speech_prob": 0.0015558414161205292},
  {"id": 853, "seek": 512400, "start": 5141.52, "end": 5145.52, "text": " We need
  to do something interesting with this scanning technology. And we''d like to apply
  it in a", "tokens": [51240, 492, 643, 281, 360, 746, 1880, 365, 341, 27019, 2899,
  13, 400, 321, 1116, 411, 281, 3079, 309, 294, 257, 51440], "temperature": 0.0, "avg_logprob":
  -0.1379446045965211, "compression_ratio": 1.6452702702702702, "no_speech_prob":
  0.0015558414161205292}, {"id": 854, "seek": 512400, "start": 5145.52, "end": 5150.24,
  "text": " market other than consumer photos or things like that. Try to find a new
  market. And mortgage turned", "tokens": [51440, 2142, 661, 813, 9711, 5787, 420,
  721, 411, 300, 13, 6526, 281, 915, 257, 777, 2142, 13, 400, 20236, 3574, 51676],
  "temperature": 0.0, "avg_logprob": -0.1379446045965211, "compression_ratio": 1.6452702702702702,
  "no_speech_prob": 0.0015558414161205292}, {"id": 855, "seek": 515024, "start": 5150.24,
  "end": 5154.5599999999995, "text": " out to be hot because if you''ve done a mortgage,
  right, if you''ve taken a mortgage, you have this", "tokens": [50364, 484, 281,
  312, 2368, 570, 498, 291, 600, 1096, 257, 20236, 11, 558, 11, 498, 291, 600, 2726,
  257, 20236, 11, 291, 362, 341, 50580], "temperature": 0.0, "avg_logprob": -0.14849209104265484,
  "compression_ratio": 1.7283582089552239, "no_speech_prob": 0.014303239062428474},
  {"id": 856, "seek": 515024, "start": 5154.5599999999995, "end": 5158.24, "text":
  " ugly moment of sending them a bunch of documents and then you just have to wait.
  And then sometimes", "tokens": [50580, 12246, 1623, 295, 7750, 552, 257, 3840, 295,
  8512, 293, 550, 291, 445, 362, 281, 1699, 13, 400, 550, 2171, 50764], "temperature":
  0.0, "avg_logprob": -0.14849209104265484, "compression_ratio": 1.7283582089552239,
  "no_speech_prob": 0.014303239062428474}, {"id": 857, "seek": 515024, "start": 5158.24,
  "end": 5162.719999999999, "text": " they''re like, Oh, I need to do this one again.
  I believe there''s research that showed that something", "tokens": [50764, 436,
  434, 411, 11, 876, 11, 286, 643, 281, 360, 341, 472, 797, 13, 286, 1697, 456, 311,
  2132, 300, 4712, 300, 746, 50988], "temperature": 0.0, "avg_logprob": -0.14849209104265484,
  "compression_ratio": 1.7283582089552239, "no_speech_prob": 0.014303239062428474},
  {"id": 858, "seek": 515024, "start": 5162.719999999999, "end": 5167.92, "text":
  " like one third of the applicants drop out every two or three days after, you know,
  you haven''t", "tokens": [50988, 411, 472, 2636, 295, 264, 28767, 3270, 484, 633,
  732, 420, 1045, 1708, 934, 11, 291, 458, 11, 291, 2378, 380, 51248], "temperature":
  0.0, "avg_logprob": -0.14849209104265484, "compression_ratio": 1.7283582089552239,
  "no_speech_prob": 0.014303239062428474}, {"id": 859, "seek": 515024, "start": 5167.92,
  "end": 5170.8, "text": " got back to them with their documents. They just want that
  all clear, like you''re good.", "tokens": [51248, 658, 646, 281, 552, 365, 641,
  8512, 13, 814, 445, 528, 300, 439, 1850, 11, 411, 291, 434, 665, 13, 51392], "temperature":
  0.0, "avg_logprob": -0.14849209104265484, "compression_ratio": 1.7283582089552239,
  "no_speech_prob": 0.014303239062428474}, {"id": 860, "seek": 515024, "start": 5171.679999999999,
  "end": 5177.28, "text": " So AI Foundry used pretty interesting OCR''s, zone technology,
  classification, text classification", "tokens": [51436, 407, 7318, 8207, 627, 1143,
  1238, 1880, 422, 18547, 311, 11, 6668, 2899, 11, 21538, 11, 2487, 21538, 51716],
  "temperature": 0.0, "avg_logprob": -0.14849209104265484, "compression_ratio": 1.7283582089552239,
  "no_speech_prob": 0.014303239062428474}, {"id": 861, "seek": 517728, "start": 5177.36,
  "end": 5182.8, "text": " to turn the mortgage app into data, not 100% with the state
  of the art before was", "tokens": [50368, 281, 1261, 264, 20236, 724, 666, 1412,
  11, 406, 2319, 4, 365, 264, 1785, 295, 264, 1523, 949, 390, 50640], "temperature":
  0.0, "avg_logprob": -0.22198511872972762, "compression_ratio": 1.6472727272727272,
  "no_speech_prob": 0.006602272856980562}, {"id": 862, "seek": 517728, "start": 5182.8,
  "end": 5186.8, "text": " keying it, manually keying it, and then someone would manually
  review it. So we switched it to review.", "tokens": [50640, 803, 1840, 309, 11,
  16945, 803, 1840, 309, 11, 293, 550, 1580, 576, 16945, 3131, 309, 13, 407, 321,
  16858, 309, 281, 3131, 13, 50840], "temperature": 0.0, "avg_logprob": -0.22198511872972762,
  "compression_ratio": 1.6472727272727272, "no_speech_prob": 0.006602272856980562},
  {"id": 863, "seek": 517728, "start": 5187.5199999999995, "end": 5193.36, "text":
  " Company was successful. It was a silo problem again. You could think of the different",
  "tokens": [50876, 13918, 390, 4406, 13, 467, 390, 257, 3425, 78, 1154, 797, 13,
  509, 727, 519, 295, 264, 819, 51168], "temperature": 0.0, "avg_logprob": -0.22198511872972762,
  "compression_ratio": 1.6472727272727272, "no_speech_prob": 0.006602272856980562},
  {"id": 864, "seek": 517728, "start": 5194.24, "end": 5199.12, "text": " types, right,
  of articles as being fundamentally silos and understanding them was hard,", "tokens":
  [51212, 3467, 11, 558, 11, 295, 11290, 382, 885, 17879, 48893, 293, 3701, 552, 390,
  1152, 11, 51456], "temperature": 0.0, "avg_logprob": -0.22198511872972762, "compression_ratio":
  1.6472727272727272, "no_speech_prob": 0.006602272856980562}, {"id": 865, "seek":
  517728, "start": 5199.12, "end": 5203.04, "text": " and we do a lot of modeling
  and it worked. It worked great, right? Gaulous bought the company.", "tokens": [51456,
  293, 321, 360, 257, 688, 295, 15983, 293, 309, 2732, 13, 467, 2732, 869, 11, 558,
  30, 10384, 6893, 4243, 264, 2237, 13, 51652], "temperature": 0.0, "avg_logprob":
  -0.22198511872972762, "compression_ratio": 1.6472727272727272, "no_speech_prob":
  0.006602272856980562}, {"id": 866, "seek": 520304, "start": 5203.76, "end": 5210.24,
  "text": " That''s just another example. Did the same thing in an IoT company, most
  recently, where we''re", "tokens": [50400, 663, 311, 445, 1071, 1365, 13, 2589,
  264, 912, 551, 294, 364, 30112, 2237, 11, 881, 3938, 11, 689, 321, 434, 50724],
  "temperature": 0.0, "avg_logprob": -0.15992421117322198, "compression_ratio": 1.6079734219269104,
  "no_speech_prob": 0.0012512467801570892}, {"id": 867, "seek": 520304, "start": 5210.24,
  "end": 5214.88, "text": " basically taking sensor data from healthcare settings,
  marrying it up with other data, like", "tokens": [50724, 1936, 1940, 10200, 1412,
  490, 8884, 6257, 11, 36376, 309, 493, 365, 661, 1412, 11, 411, 50956], "temperature":
  0.0, "avg_logprob": -0.15992421117322198, "compression_ratio": 1.6079734219269104,
  "no_speech_prob": 0.0012512467801570892}, {"id": 868, "seek": 520304, "start": 5214.88,
  "end": 5220.24, "text": " their EHR data and trying to predict, you know, likelihood
  of various conditions. So it''s always", "tokens": [50956, 641, 39416, 49, 1412,
  293, 1382, 281, 6069, 11, 291, 458, 11, 22119, 295, 3683, 4487, 13, 407, 309, 311,
  1009, 51224], "temperature": 0.0, "avg_logprob": -0.15992421117322198, "compression_ratio":
  1.6079734219269104, "no_speech_prob": 0.0012512467801570892}, {"id": 869, "seek":
  520304, "start": 5220.24, "end": 5224.8, "text": " the silo problem. And frankly,
  every single one of these ventures would have benefited from something", "tokens":
  [51224, 264, 3425, 78, 1154, 13, 400, 11939, 11, 633, 2167, 472, 295, 613, 6931,
  1303, 576, 362, 33605, 490, 746, 51452], "temperature": 0.0, "avg_logprob": -0.15992421117322198,
  "compression_ratio": 1.6079734219269104, "no_speech_prob": 0.0012512467801570892},
  {"id": 870, "seek": 520304, "start": 5224.8, "end": 5230.08, "text": " like swirl.
  So that''s why I did it. It''s because to be honest with you, I think the data problem
  is", "tokens": [51452, 411, 30310, 13, 407, 300, 311, 983, 286, 630, 309, 13, 467,
  311, 570, 281, 312, 3245, 365, 291, 11, 286, 519, 264, 1412, 1154, 307, 51716],
  "temperature": 0.0, "avg_logprob": -0.15992421117322198, "compression_ratio": 1.6079734219269104,
  "no_speech_prob": 0.0012512467801570892}, {"id": 871, "seek": 523008, "start": 5230.16,
  "end": 5236.32, "text": " huge. I''m passionate about it. And I think it''s important
  to solve it because frankly, some of the", "tokens": [50368, 2603, 13, 286, 478,
  11410, 466, 309, 13, 400, 286, 519, 309, 311, 1021, 281, 5039, 309, 570, 11939,
  11, 512, 295, 264, 50676], "temperature": 0.0, "avg_logprob": -0.12234523684479469,
  "compression_ratio": 1.6464646464646464, "no_speech_prob": 0.015091207809746265},
  {"id": 872, "seek": 523008, "start": 5236.32, "end": 5240.72, "text": " service
  problems, right, that we all suffer when we''re out in the field dealing with large
  companies", "tokens": [50676, 2643, 2740, 11, 558, 11, 300, 321, 439, 9753, 562,
  321, 434, 484, 294, 264, 2519, 6260, 365, 2416, 3431, 50896], "temperature": 0.0,
  "avg_logprob": -0.12234523684479469, "compression_ratio": 1.6464646464646464, "no_speech_prob":
  0.015091207809746265}, {"id": 873, "seek": 523008, "start": 5240.72, "end": 5244.96,
  "text": " because they just don''t have the data. They''re not just trying to be
  mean or be clueless, right?", "tokens": [50896, 570, 436, 445, 500, 380, 362, 264,
  1412, 13, 814, 434, 406, 445, 1382, 281, 312, 914, 420, 312, 596, 3483, 442, 11,
  558, 30, 51108], "temperature": 0.0, "avg_logprob": -0.12234523684479469, "compression_ratio":
  1.6464646464646464, "no_speech_prob": 0.015091207809746265}, {"id": 874, "seek":
  523008, "start": 5244.96, "end": 5249.68, "text": " Sometimes it''s like, it''s
  a hard problem to solve. We expect a lot now. As an engineer, right?", "tokens":
  [51108, 4803, 309, 311, 411, 11, 309, 311, 257, 1152, 1154, 281, 5039, 13, 492,
  2066, 257, 688, 586, 13, 1018, 364, 11403, 11, 558, 30, 51344], "temperature": 0.0,
  "avg_logprob": -0.12234523684479469, "compression_ratio": 1.6464646464646464, "no_speech_prob":
  0.015091207809746265}, {"id": 875, "seek": 523008, "start": 5249.68, "end": 5255.28,
  "text": " I''m expecting chat GPT level response is pretty soon. And yet, what we
  have is Siri, who like can", "tokens": [51344, 286, 478, 9650, 5081, 26039, 51,
  1496, 4134, 307, 1238, 2321, 13, 400, 1939, 11, 437, 321, 362, 307, 33682, 11, 567,
  411, 393, 51624], "temperature": 0.0, "avg_logprob": -0.12234523684479469, "compression_ratio":
  1.6464646464646464, "no_speech_prob": 0.015091207809746265}, {"id": 876, "seek":
  525528, "start": 5255.28, "end": 5260.8, "text": " barely figure out to turn off
  the alarm, you know, what it''s going to. So there are going to be some", "tokens":
  [50364, 10268, 2573, 484, 281, 1261, 766, 264, 14183, 11, 291, 458, 11, 437, 309,
  311, 516, 281, 13, 407, 456, 366, 516, 281, 312, 512, 50640], "temperature": 0.0,
  "avg_logprob": -0.2271327105435458, "compression_ratio": 1.5633802816901408, "no_speech_prob":
  0.004162776283919811}, {"id": 877, "seek": 525528, "start": 5260.8, "end": 5267.12,
  "text": " bumps. There''s going to be some sudden pulls and pushes. But I think
  the important thing is that", "tokens": [50640, 27719, 13, 821, 311, 516, 281, 312,
  512, 3990, 16982, 293, 21020, 13, 583, 286, 519, 264, 1021, 551, 307, 300, 50956],
  "temperature": 0.0, "avg_logprob": -0.2271327105435458, "compression_ratio": 1.5633802816901408,
  "no_speech_prob": 0.004162776283919811}, {"id": 878, "seek": 525528, "start": 5268.0,
  "end": 5271.28, "text": " why you ask me why do it open because prove it.", "tokens":
  [51000, 983, 291, 1029, 385, 983, 360, 309, 1269, 570, 7081, 309, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.2271327105435458, "compression_ratio": 1.5633802816901408,
  "no_speech_prob": 0.004162776283919811}, {"id": 879, "seek": 525528, "start": 5273.92,
  "end": 5283.36, "text": " Awesome. Yeah, this is an amazing answer. So data is literally
  king and the one who has", "tokens": [51296, 10391, 13, 865, 11, 341, 307, 364,
  2243, 1867, 13, 407, 1412, 307, 3736, 4867, 293, 264, 472, 567, 575, 51768], "temperature":
  0.0, "avg_logprob": -0.2271327105435458, "compression_ratio": 1.5633802816901408,
  "no_speech_prob": 0.004162776283919811}, {"id": 880, "seek": 528336, "start": 5284.32,
  "end": 5289.44, "text": " universal access to data, wins, right? In so many senses
  of this word.", "tokens": [50412, 11455, 2105, 281, 1412, 11, 10641, 11, 558, 30,
  682, 370, 867, 17057, 295, 341, 1349, 13, 50668], "temperature": 0.0, "avg_logprob":
  -0.15400277953786948, "compression_ratio": 1.5493562231759657, "no_speech_prob":
  0.030450498685240746}, {"id": 881, "seek": 528336, "start": 5290.719999999999, "end":
  5296.88, "text": " This is so great. This is so good. Chatting to you, Sid, I''ve
  learned a lot. I was wondering if", "tokens": [50732, 639, 307, 370, 869, 13, 639,
  307, 370, 665, 13, 27503, 783, 281, 291, 11, 19797, 11, 286, 600, 3264, 257, 688,
  13, 286, 390, 6359, 498, 51040], "temperature": 0.0, "avg_logprob": -0.15400277953786948,
  "compression_ratio": 1.5493562231759657, "no_speech_prob": 0.030450498685240746},
  {"id": 882, "seek": 528336, "start": 5296.88, "end": 5302.719999999999, "text":
  " there''s something you would like to announce. Something is cooking. Or you simply
  want to invite", "tokens": [51040, 456, 311, 746, 291, 576, 411, 281, 7478, 13,
  6595, 307, 6361, 13, 1610, 291, 2935, 528, 281, 7980, 51332], "temperature": 0.0,
  "avg_logprob": -0.15400277953786948, "compression_ratio": 1.5493562231759657, "no_speech_prob":
  0.030450498685240746}, {"id": 883, "seek": 528336, "start": 5302.719999999999, "end":
  5309.2, "text": " developers to a tutorial and to send a pull request. Well, I would
  love to do that. First of all,", "tokens": [51332, 8849, 281, 257, 7073, 293, 281,
  2845, 257, 2235, 5308, 13, 1042, 11, 286, 576, 959, 281, 360, 300, 13, 2386, 295,
  439, 11, 51656], "temperature": 0.0, "avg_logprob": -0.15400277953786948, "compression_ratio":
  1.5493562231759657, "no_speech_prob": 0.030450498685240746}, {"id": 884, "seek":
  530920, "start": 5309.2, "end": 5316.16, "text": " we have webinars every couple
  of weeks. Please come if you''re interested. Just, it''s a,", "tokens": [50364,
  321, 362, 26065, 633, 1916, 295, 3259, 13, 2555, 808, 498, 291, 434, 3102, 13, 1449,
  11, 309, 311, 257, 11, 50712], "temperature": 0.0, "avg_logprob": -0.23585526645183563,
  "compression_ratio": 1.6283783783783783, "no_speech_prob": 0.01513128262013197},
  {"id": 885, "seek": 530920, "start": 5316.16, "end": 5323.2, "text": " you just
  need to put an email address at the edge of the red form. We are also totally available",
  "tokens": [50712, 291, 445, 643, 281, 829, 364, 3796, 2985, 412, 264, 4691, 295,
  264, 2182, 1254, 13, 492, 366, 611, 3879, 2435, 51064], "temperature": 0.0, "avg_logprob":
  -0.23585526645183563, "compression_ratio": 1.6283783783783783, "no_speech_prob":
  0.01513128262013197}, {"id": 886, "seek": 530920, "start": 5323.2, "end": 5328.16,
  "text": " on Slack. There''s, you know, totally, we don''t have sales. It''s free.
  Just connect up. You''ll talk", "tokens": [51064, 322, 37211, 13, 821, 311, 11,
  291, 458, 11, 3879, 11, 321, 500, 380, 362, 5763, 13, 467, 311, 1737, 13, 1449,
  1745, 493, 13, 509, 603, 751, 51312], "temperature": 0.0, "avg_logprob": -0.23585526645183563,
  "compression_ratio": 1.6283783783783783, "no_speech_prob": 0.01513128262013197},
  {"id": 887, "seek": 530920, "start": 5328.16, "end": 5333.36, "text": " to support
  or customer success. I guess is the more, more appropriate term these days. But
  they''re", "tokens": [51312, 281, 1406, 420, 5474, 2245, 13, 286, 2041, 307, 264,
  544, 11, 544, 6854, 1433, 613, 1708, 13, 583, 436, 434, 51572], "temperature": 0.0,
  "avg_logprob": -0.23585526645183563, "compression_ratio": 1.6283783783783783, "no_speech_prob":
  0.01513128262013197}, {"id": 888, "seek": 530920, "start": 5333.36, "end": 5337.12,
  "text": " here. We''re here to help. That includes me and everybody else on the
  team. There''s only five of us.", "tokens": [51572, 510, 13, 492, 434, 510, 281,
  854, 13, 663, 5974, 385, 293, 2201, 1646, 322, 264, 1469, 13, 821, 311, 787, 1732,
  295, 505, 13, 51760], "temperature": 0.0, "avg_logprob": -0.23585526645183563, "compression_ratio":
  1.6283783783783783, "no_speech_prob": 0.01513128262013197}, {"id": 889, "seek":
  533712, "start": 5338.08, "end": 5343.76, "text": " But we''re all here to help.
  We would love to hear what you want to do this world, what you''re", "tokens": [50412,
  583, 321, 434, 439, 510, 281, 854, 13, 492, 576, 959, 281, 1568, 437, 291, 528,
  281, 360, 341, 1002, 11, 437, 291, 434, 50696], "temperature": 0.0, "avg_logprob":
  -0.1151013780933942, "compression_ratio": 1.6958041958041958, "no_speech_prob":
  0.0313730388879776}, {"id": 890, "seek": 533712, "start": 5343.76, "end": 5347.68,
  "text": " doing this world. We are here to write, if you need help with a search
  provider, we''ll write it", "tokens": [50696, 884, 341, 1002, 13, 492, 366, 510,
  281, 2464, 11, 498, 291, 643, 854, 365, 257, 3164, 12398, 11, 321, 603, 2464, 309,
  50892], "temperature": 0.0, "avg_logprob": -0.1151013780933942, "compression_ratio":
  1.6958041958041958, "no_speech_prob": 0.0313730388879776}, {"id": 891, "seek": 533712,
  "start": 5347.68, "end": 5354.08, "text": " for you or help you help you get it
  working. What I can say for sure is this. Next month, version 2.0", "tokens": [50892,
  337, 291, 420, 854, 291, 854, 291, 483, 309, 1364, 13, 708, 286, 393, 584, 337,
  988, 307, 341, 13, 3087, 1618, 11, 3037, 568, 13, 15, 51212], "temperature": 0.0,
  "avg_logprob": -0.1151013780933942, "compression_ratio": 1.6958041958041958, "no_speech_prob":
  0.0313730388879776}, {"id": 892, "seek": 533712, "start": 5354.08, "end": 5359.68,
  "text": " will drop. It will be something you can one click try and it will have
  the M365 integration that I", "tokens": [51212, 486, 3270, 13, 467, 486, 312, 746,
  291, 393, 472, 2052, 853, 293, 309, 486, 362, 264, 376, 11309, 20, 10980, 300, 286,
  51492], "temperature": 0.0, "avg_logprob": -0.1151013780933942, "compression_ratio":
  1.6958041958041958, "no_speech_prob": 0.0313730388879776}, {"id": 893, "seek": 533712,
  "start": 5359.68, "end": 5364.4, "text": " talked about. So the full ability to
  deploy it to your tenant in our hosted version or just to", "tokens": [51492, 2825,
  466, 13, 407, 264, 1577, 3485, 281, 7274, 309, 281, 428, 31000, 294, 527, 19204,
  3037, 420, 445, 281, 51728], "temperature": 0.0, "avg_logprob": -0.1151013780933942,
  "compression_ratio": 1.6958041958041958, "no_speech_prob": 0.0313730388879776},
  {"id": 894, "seek": 536440, "start": 5364.4, "end": 5370.5599999999995, "text":
  " take the Docker, run with it, hook that up so it will support OAuth 2 and OIDC.
  Many, many more features", "tokens": [50364, 747, 264, 33772, 11, 1190, 365, 309,
  11, 6328, 300, 493, 370, 309, 486, 1406, 48424, 2910, 568, 293, 422, 2777, 34, 13,
  5126, 11, 867, 544, 4122, 50672], "temperature": 0.0, "avg_logprob": -0.17458599585073967,
  "compression_ratio": 1.5134099616858236, "no_speech_prob": 0.003458797698840499},
  {"id": 895, "seek": 536440, "start": 5370.5599999999995, "end": 5374.799999999999,
  "text": " will be elaborating on the things you can do with it over the next couple
  of months, particularly in", "tokens": [50672, 486, 312, 16298, 990, 322, 264, 721,
  291, 393, 360, 365, 309, 670, 264, 958, 1916, 295, 2493, 11, 4098, 294, 50884],
  "temperature": 0.0, "avg_logprob": -0.17458599585073967, "compression_ratio": 1.5134099616858236,
  "no_speech_prob": 0.003458797698840499}, {"id": 896, "seek": 536440, "start": 5374.799999999999,
  "end": 5383.839999999999, "text": " May. And I just really would beg people to try
  it and tell us what you think. That''s my ask.", "tokens": [50884, 1891, 13, 400,
  286, 445, 534, 576, 4612, 561, 281, 853, 309, 293, 980, 505, 437, 291, 519, 13,
  663, 311, 452, 1029, 13, 51336], "temperature": 0.0, "avg_logprob": -0.17458599585073967,
  "compression_ratio": 1.5134099616858236, "no_speech_prob": 0.003458797698840499},
  {"id": 897, "seek": 536440, "start": 5383.839999999999, "end": 5390.16, "text":
  " So if, and if anybody can, if you want to work on it, you know, we''re always
  delighted to accept", "tokens": [51336, 407, 498, 11, 293, 498, 4472, 393, 11, 498,
  291, 528, 281, 589, 322, 309, 11, 291, 458, 11, 321, 434, 1009, 18783, 281, 3241,
  51652], "temperature": 0.0, "avg_logprob": -0.17458599585073967, "compression_ratio":
  1.5134099616858236, "no_speech_prob": 0.003458797698840499}, {"id": 898, "seek":
  539016, "start": 5391.12, "end": 5396.48, "text": " and even guide anybody as to
  where to start. Right. So that''s where we are. We''re very young", "tokens": [50412,
  293, 754, 5934, 4472, 382, 281, 689, 281, 722, 13, 1779, 13, 407, 300, 311, 689,
  321, 366, 13, 492, 434, 588, 2037, 50680], "temperature": 0.0, "avg_logprob": -0.19176543386358963,
  "compression_ratio": 1.602510460251046, "no_speech_prob": 0.03748473897576332},
  {"id": 899, "seek": 539016, "start": 5396.48, "end": 5402.96, "text": " and we''re
  trying to figure this out. And energetic and knowledgeable. And I think we will
  link", "tokens": [50680, 293, 321, 434, 1382, 281, 2573, 341, 484, 13, 400, 24935,
  293, 33800, 13, 400, 286, 519, 321, 486, 2113, 51004], "temperature": 0.0, "avg_logprob":
  -0.19176543386358963, "compression_ratio": 1.602510460251046, "no_speech_prob":
  0.03748473897576332}, {"id": 900, "seek": 539016, "start": 5402.96, "end": 5408.72,
  "text": " everything you mentioned, of course, in the episode show notes so everyone
  can click it their will.", "tokens": [51004, 1203, 291, 2835, 11, 295, 1164, 11,
  294, 264, 3500, 855, 5570, 370, 1518, 393, 2052, 309, 641, 486, 13, 51292], "temperature":
  0.0, "avg_logprob": -0.19176543386358963, "compression_ratio": 1.602510460251046,
  "no_speech_prob": 0.03748473897576332}, {"id": 901, "seek": 539016, "start": 5408.72,
  "end": 5416.96, "text": " And you know, follow and learn from you as I did today.
  And I really want to allocate time also", "tokens": [51292, 400, 291, 458, 11, 1524,
  293, 1466, 490, 291, 382, 286, 630, 965, 13, 400, 286, 534, 528, 281, 35713, 565,
  611, 51704], "temperature": 0.0, "avg_logprob": -0.19176543386358963, "compression_ratio":
  1.602510460251046, "no_speech_prob": 0.03748473897576332}, {"id": 902, "seek": 541696,
  "start": 5417.36, "end": 5421.28, "text": " to participate in one of your webinars
  with them. I''m pretty sure I will learn more.", "tokens": [50384, 281, 8197, 294,
  472, 295, 428, 26065, 365, 552, 13, 286, 478, 1238, 988, 286, 486, 1466, 544, 13,
  50580], "temperature": 0.0, "avg_logprob": -0.20890057881673177, "compression_ratio":
  1.6774193548387097, "no_speech_prob": 0.013585628010332584}, {"id": 903, "seek":
  541696, "start": 5422.32, "end": 5427.2, "text": " That would be great. We are definitely
  bringing in folks. We had again, KMW, which makes", "tokens": [50632, 663, 576,
  312, 869, 13, 492, 366, 2138, 5062, 294, 4024, 13, 492, 632, 797, 11, 591, 44, 54,
  11, 597, 1669, 50876], "temperature": 0.0, "avg_logprob": -0.20890057881673177,
  "compression_ratio": 1.6774193548387097, "no_speech_prob": 0.013585628010332584},
  {"id": 904, "seek": 541696, "start": 5427.2, "end": 5432.56, "text": " Spyglass
  the open source project. We had the author of Quarge came, came previously Renee.
  It was", "tokens": [50876, 35854, 28851, 264, 1269, 4009, 1716, 13, 492, 632, 264,
  3793, 295, 2326, 289, 432, 1361, 11, 1361, 8046, 47790, 13, 467, 390, 51144], "temperature":
  0.0, "avg_logprob": -0.20890057881673177, "compression_ratio": 1.6774193548387097,
  "no_speech_prob": 0.013585628010332584}, {"id": 905, "seek": 541696, "start": 5432.56,
  "end": 5436.64, "text": " great fun. We hope to have him on again, because I think
  we could learn. I''m actually listening for", "tokens": [51144, 869, 1019, 13, 492,
  1454, 281, 362, 796, 322, 797, 11, 570, 286, 519, 321, 727, 1466, 13, 286, 478,
  767, 4764, 337, 51348], "temperature": 0.0, "avg_logprob": -0.20890057881673177,
  "compression_ratio": 1.6774193548387097, "no_speech_prob": 0.013585628010332584},
  {"id": 906, "seek": 541696, "start": 5436.64, "end": 5442.0, "text": " our talk
  about the things they''re doing. So and many others. So absolutely, we''d love to
  have you on.", "tokens": [51348, 527, 751, 466, 264, 721, 436, 434, 884, 13, 407,
  293, 867, 2357, 13, 407, 3122, 11, 321, 1116, 959, 281, 362, 291, 322, 13, 51616],
  "temperature": 0.0, "avg_logprob": -0.20890057881673177, "compression_ratio": 1.6774193548387097,
  "no_speech_prob": 0.013585628010332584}, {"id": 907, "seek": 541696, "start": 5442.0,
  "end": 5446.16, "text": " And if you know anybody who wants to talk about the stuff
  too, please, I''d love to have them on as", "tokens": [51616, 400, 498, 291, 458,
  4472, 567, 2738, 281, 751, 466, 264, 1507, 886, 11, 1767, 11, 286, 1116, 959, 281,
  362, 552, 322, 382, 51824], "temperature": 0.0, "avg_logprob": -0.20890057881673177,
  "compression_ratio": 1.6774193548387097, "no_speech_prob": 0.013585628010332584},
  {"id": 908, "seek": 544616, "start": 5446.16, "end": 5454.96, "text": " well. Fantastic.
  Thanks for pushing the envelope of search. Keep pushing. I wish you all the success",
  "tokens": [50364, 731, 13, 21320, 13, 2561, 337, 7380, 264, 19989, 295, 3164, 13,
  5527, 7380, 13, 286, 3172, 291, 439, 264, 2245, 50804], "temperature": 0.0, "avg_logprob":
  -0.16196058234389948, "compression_ratio": 1.625514403292181, "no_speech_prob":
  0.02095511183142662}, {"id": 909, "seek": 544616, "start": 5454.96, "end": 5462.88,
  "text": " that you can get and beyond. And I hope we can chat more down the line
  down the road as you got,", "tokens": [50804, 300, 291, 393, 483, 293, 4399, 13,
  400, 286, 1454, 321, 393, 5081, 544, 760, 264, 1622, 760, 264, 3060, 382, 291, 658,
  11, 51200], "temperature": 0.0, "avg_logprob": -0.16196058234389948, "compression_ratio":
  1.625514403292181, "no_speech_prob": 0.02095511183142662}, {"id": 910, "seek": 544616,
  "start": 5462.88, "end": 5469.599999999999, "text": " as you guys grow and I''m
  pretty sure you will. Thank you so much for the confidence we will love to", "tokens":
  [51200, 382, 291, 1074, 1852, 293, 286, 478, 1238, 988, 291, 486, 13, 1044, 291,
  370, 709, 337, 264, 6687, 321, 486, 959, 281, 51536], "temperature": 0.0, "avg_logprob":
  -0.16196058234389948, "compression_ratio": 1.625514403292181, "no_speech_prob":
  0.02095511183142662}, {"id": 911, "seek": 544616, "start": 5469.599999999999, "end":
  5474.639999999999, "text": " share updates in future, especially I''ll be very psyched
  to show you some of the machine learning", "tokens": [51536, 2073, 9205, 294, 2027,
  11, 2318, 286, 603, 312, 588, 4681, 292, 281, 855, 291, 512, 295, 264, 3479, 2539,
  51788], "temperature": 0.0, "avg_logprob": -0.16196058234389948, "compression_ratio":
  1.625514403292181, "no_speech_prob": 0.02095511183142662}, {"id": 912, "seek": 547464,
  "start": 5474.64, "end": 5479.4400000000005, "text": " stuff we''re talking about
  as a case, we definitely want to build that as a use case and make it", "tokens":
  [50364, 1507, 321, 434, 1417, 466, 382, 257, 1389, 11, 321, 2138, 528, 281, 1322,
  300, 382, 257, 764, 1389, 293, 652, 309, 50604], "temperature": 0.0, "avg_logprob":
  -0.18566633760929108, "compression_ratio": 1.6655052264808363, "no_speech_prob":
  0.04799362272024155}, {"id": 913, "seek": 547464, "start": 5479.4400000000005, "end":
  5484.8, "text": " one click easy to do that. So yeah, let''s keep it touch. I love
  to too. I mean, I''m a huge fan of", "tokens": [50604, 472, 2052, 1858, 281, 360,
  300, 13, 407, 1338, 11, 718, 311, 1066, 309, 2557, 13, 286, 959, 281, 886, 13, 286,
  914, 11, 286, 478, 257, 2603, 3429, 295, 50872], "temperature": 0.0, "avg_logprob":
  -0.18566633760929108, "compression_ratio": 1.6655052264808363, "no_speech_prob":
  0.04799362272024155}, {"id": 914, "seek": 547464, "start": 5484.8, "end": 5491.84,
  "text": " the podcast. Obviously, I''ve listened to the Vespa cast several times
  and I think please keep", "tokens": [50872, 264, 7367, 13, 7580, 11, 286, 600, 13207,
  281, 264, 691, 279, 4306, 4193, 2940, 1413, 293, 286, 519, 1767, 1066, 51224], "temperature":
  0.0, "avg_logprob": -0.18566633760929108, "compression_ratio": 1.6655052264808363,
  "no_speech_prob": 0.04799362272024155}, {"id": 915, "seek": 547464, "start": 5491.84,
  "end": 5495.52, "text": " it up. It''s awesome. There''s not enough people focused
  on this incredible area of technology.", "tokens": [51224, 309, 493, 13, 467, 311,
  3476, 13, 821, 311, 406, 1547, 561, 5178, 322, 341, 4651, 1859, 295, 2899, 13, 51408],
  "temperature": 0.0, "avg_logprob": -0.18566633760929108, "compression_ratio": 1.6655052264808363,
  "no_speech_prob": 0.04799362272024155}, {"id": 916, "seek": 547464, "start": 5497.200000000001,
  "end": 5500.96, "text": " We''re talking about stuff. I think it''s going to become
  more common, but it''s still a little bit", "tokens": [51492, 492, 434, 1417, 466,
  1507, 13, 286, 519, 309, 311, 516, 281, 1813, 544, 2689, 11, 457, 309, 311, 920,
  257, 707, 857, 51680], "temperature": 0.0, "avg_logprob": -0.18566633760929108,
  "compression_ratio": 1.6655052264808363, "no_speech_prob": 0.04799362272024155},
  {"id": 917, "seek": 550096, "start": 5500.96, "end": 5507.28, "text": " unknown.
  Yeah, appreciate your kind words. It''s thanks to you, makers. Thank you so much,",
  "tokens": [50364, 9841, 13, 865, 11, 4449, 428, 733, 2283, 13, 467, 311, 3231, 281,
  291, 11, 19323, 13, 1044, 291, 370, 709, 11, 50680], "temperature": 0.0, "avg_logprob":
  -0.23133602509131798, "compression_ratio": 1.072289156626506, "no_speech_prob":
  0.03108839876949787}, {"id": 918, "seek": 550728, "start": 5507.28, "end": 5511.599999999999,
  "text": " say it for your time. Really enjoyed it. Thank you very much. Bye bye.",
  "tokens": [50364, 584, 309, 337, 428, 565, 13, 4083, 4626, 309, 13, 1044, 291, 588,
  709, 13, 4621, 6543, 13, 50580], "temperature": 0.0, "avg_logprob": -0.4556102752685547,
  "compression_ratio": 0.958904109589041, "no_speech_prob": 0.17116160690784454}]'
---

In this episode, you will learn about Swirl, MetaSearch Engine with large language models for your silo data. Here you can see how it works for the summary transcript of this episode created with the tool called ClearWord.
Hello there, Vector Podcast Season 2, and today I'm super excited to be talking to CIPROP STING, the creator of Swirl Search. It's a federated VectorSearch Engine. If I'm correct, but I would not hear more from CIT himself. Hello, CIT, how are you? I'm doing great. It's really great to be here.
Thank you so much for inviting me. Yeah, thanks for joining. I'm sure you are very busy building Swirl, and I'm really curious to learn more about it. I missed all the discussion, you know, how chat GPT is going to change things.
You know, is it going to conquer us or whatnot? But yeah, I mean, I'm really interested to hear how you guys are doing, how you guys are building this. And traditionally, we start with your background because we really want to know how you got here. Absolutely, no.
And it's been an interesting journey. Swirl actually is my, the 12th venture I've been lucky enough to work on. I started actually at a free email company called FreeMarkMail. You might remember Juno, our vastly more successful competitor.
It was a great, great lesson in marketing and customer acquisition.
But long story short, you know, my dad was an MIT professor, and he suggested, or he was interested in computers, and somewhere around, it was too long ago, but I was about 12 and I picked up a TRS 80 with 16K of RAM, I think, in a cassette tape for storage.
And we went to a couple of, actually, we went to two classes together, and then he didn't want to do it anymore, but I stayed with it. And I have always loved getting that computer to do things that we wanted to do.
And so I guess ever since then, I followed the tech path, so I was lucky enough to do my undergrad at MIT. I actually have an MBA, though, I'm one of those MBA CTOs. And mostly I've worked building software and leading teams to build products and services.
So some of them have been a TIVIO, which is now actually service now, which is obviously one of the unicorns out there. They really totally disrupted the knowledge base and help desk space.
And it's an incredible application of interesting core technology at the beginning, when things were whiteboardy.
I've worked in a couple of other search companies, and with some other search companies, I was lucky to spend a little time with Mercedes Arabian over at BA Insight, which was a very cool and also Jeff Fried, very cool company.
And since I know those guys back from fast, another company that I worked at, now Microsoft, fast was one of the early players in enterprise search that had an excellent product that scaled and right as Google was sort of becoming a household name and just intermediate everybody.
We had the tool to build the catalog, the e-catalog, that mostly for publishers, and but then it really spread out and started to affect intranets. And it was truly there that I saw the power of search and how it could change almost everything from the business perspective.
You know, business intelligence and reporting and all of these systems that have been around for 70, 80 years, they're what we settle for. But everybody, you know, from Brin and Page on, right, and way before that, we're all inspired by that Star Trek computer.
Why can't we just ask it, you know, it seems like it's not that hard. And now of course, not to give away the lead, right? But there's definitely something doing that and it's been a long time coming. But that is not structured data.
Well, let's not argue about the semantics, but it's not what people refer to as structured. It's not database data metrics and KPIs and sales numbers and things like that.
I think that it was really at fast and also at Northern Light Technology, which is still going strong, by the way, with some fantastic indexing search. And now they're doing question answering. First place I really touched search, right, was at Northern Light. It's the human interface.
And we feel like it should be coming along faster. And now the text after many years of indexing and vector search, right? And the advances driven by Google so much, right? Transformer architectures and vectors. And that has all come together into a pretty amazing place.
And so long story short, that background led me to create swirl because I noticed a couple things. It really came down to three things. One is that there's, there are silos, super silos, like service now.
Service now really did get a lot of the knowledge bases and a lot of those, a lot of the help desk, you know, the tickets base with the streams and tickets. M365 kind of won the files race at least right along with email. And I guess they've done very well.
Obviously, very impressive performance to build teams to the large community that it has developed. So, and then there are others, right? There's certainly Salesforce, a great example of where most of the CRM data now lives. Snowflakes, another one, you can't really get a copy of these.
I mean, moving the data out from Snowflake is relatively easy, but the others, there's a complicated API there. Salesforce has thousands of tables. So, you can't really get that data anymore, but yet it has some of the most important ideas, concepts, and knowledge in your entire company.
So, that's when I realized something that had been tried before. MetaSearch, right, or federated search. I think MetaSearch is clear up because now sometimes people say federated search is about e-commerce federation.
The MetaSearch was hard to do because of connectivity, right? Like it could take you months to just get somebody to change a network thing or to put a VPN in place or either change permissions. That was expensive in large enterprise.
But now, especially with public services, pretty much everything has an API. The perimeter doesn't exist the way I used to. And so, you can query everything. So, that left the problem of can you make sense of things? And that's of course, what we're here about, right, is vectors.
The power of vector search and vector similarity, specifically, right, self-cosign vector similarity that we use in Swirl to make sense of completely disparate and very, very, very incompatible results, if you will. And it's shocking how well it works.
That that's when I saw it work, I said there's more to this than I thought it now. It seems I'm not the only one. So, but anyway, that's a little bit of the story in my background. I hope that that made some sense. Yeah, it's very solid background.
You reminded me of one, I don't remember the name of that computer, but like didn't have the display the way we have today, right? It just had the keyboard. And then it had the cassette. And so, my friend and I were sitting there for several minutes to boot it.
And then there was some game like Mario or whatever. That was on the cool Apple twos. I was always envious of the Apple two, you know, kids. Because you're right, on the TRS-80, we only had block graphics. It was hilarious. But it didn't move a little bit faster in a way.
Like you get to wait a long time for Apple upgrades. But I remember the TRS-80, there was an incredible ecosystem of things you could add to it. So, memory. And then there was a company called Percom that put out disk drives. Wow, a disk drive.
That was a game changer if you played with a cassette recorder. Although, who didn't love switching your parents' cassettes with the with the data tape so they'd put it on in the car and we go, okay, are they going to stop and turn that off? It was a hilarious prank. A great way to get some sound.
But disk drives then gave, right? First, there were the five in a quarter or actually eight inch, then five in a quarter. And then finally, they've got to the cassette. I was at that point, it was sort of replaced, right? Then the IBM PC showed up. And that was a bit of a game changer.
But the Apple always had better graphics. Yeah, absolutely. I just wanted to come back to what you just said about federated search and enterprise search.
I think I remember hearing about enterprise search was it like 15, 16, 17 years ago, I don't remember in the university when one of my supervisors was focusing on it and he was saying, this is the next big thing. And once it's figured out, you know, we will be rich. But somehow it didn't happen.
And then later in my career, I heard term federated search in connection to, okay, we have our own search engine, we have clients data, can we combine the two without needing them to upload their data to our servers?
Because in some cases, they wouldn't trust us, you know, securing it's enough and so on.
So forest. And then we were confronted with the fact that maybe it will incur quite a bit of latency. And also even in the first place, how we would build this.
But you know, like before we even get there, how do you relate enterprise search versus federated search? So, so I think they're, they're different in that enterprise search is about a realm. Right. Enterprise search means usually not public sources.
And I think it's important to differentiate the problems of the large enterprise and even the medium enterprise are not the same as the sort of small, small and medium enterprise enterprise. Maybe that's not a great dividing line.
But definitely the large enterprise has a very different set of problems. It's so much more about, you know, global distribution and languages and regulation. If you're a, you know, small company like like swirl ink, we have five people, we can work off of almost anything.
I mean, and we don't have the silo problem because we just have picked, you know, we have four. But it's interesting. We do still have the silo problem, right.
And as I'm going to show you, just when we were trying to find the steering document for this discussion, I realized I was hunting around which silo did I put it in instead of just going to search. So it's funny that we've trained ourselves to work that way.
That I think it's a reflection of the reality that in the large enterprise, it's exactly what you said entitlements are extremely important. You're talking about crown jewel data like PL product data or customer feedback. CRM data is much less sensitive in some ways.
Also data that you might purchase, it's very common for companies to build and or purchase data sets and assemble them or assemble derivative sets. These would be incredibly valuable for lots of uses.
The simplest one, right, usually as sales or the most obvious one is help sales, help partners sell more at the knowledge companies, help the sales people better understand their customers or industries. And there's a massive amount of information overload. So the problems are different.
They're acute. They're willing to spend significant money, right, and invest in really creating a better world. I think now, maybe one of the most important trends is people are not so interested in more search boxes.
They want to build proactive systems that bring people the information that they need. And this has been a long time thing in sales with things like LinkedIn Navigator, right? A lot of the public data gets harvested and brought to you.
But think about all of that incredibly rich, valuable internal data and needing to bring that and how hard it is to bring that to people inside the enterprise because of those entitlement lines.
So federated or meta search is a technical approach, which says rather than an in traditional enterprise search, traditionally, the tool is indexing.
So you take the data from all the sources that you need to query, which usually, since that's hundreds, if not thousands, inside the large enterprise, usually start with a few.
And you extract the data, meaning you pull it all out, then you have to remodel it because you could leave it sort of as is, but the odds are high that won't help with search. You need to make at least some of the fields, things like title and body line up.
So you map those things over and you have to make sure that the set of entitlements, meaning whose author I see stuff, all of that from all the silos has to be aggregated and correctly rationalized and put together, then you index it.
Indexing is a technical process like creating a structure like the back of most books or most long books, a list of words with basically page numbers, but in this case, they're slightly more complex. They might identify the documents in the field and the exact token that it occurs in.
So you have this kind of data structure. And you just have to keep it up to date anytime anything changes. So it's really hard. I have been very lucky to work in search and fast was a phenomenal indexing company and it innovated in indexing beyond the pale. I really incredible stuff.
So fast was one of the first companies to do updateable indices. You could actually update it. Then a lot of the stuff that they did is advanced vector. We did it fast, but you know, me a tiny bit, right? Whatever the nuggets were, but they went on. They went so far with engine development at fast.
And now it's by the way available through the Vespa project, right? If you go to Vespa.de, all that stuff is available, open source to. Yeah, we have an episode with Vespa. You probably would joke. Yes. He's my hero on on Twitter.
So incredible advances at fast and frankly at a TVO, you know, there were a bunch of patents filed.
Some very smart people worked on that problem and came up with incredible ways to interlink data by combining graph and and a traditional inverted index and doing things like then adding that to machine learning and doing things like predicting the answer to a service ticket.
So there's no end of indexing. It's just hard. That's all. It's just hard. And especially when you want to combine silos. And so over the years, I've bumped into people who have had the multi silo problem in grade numbers.
There is one consulting company that has more than 500 silos, separate installations of elastic, literally from version two to version eight or whatever they're on now, right? Because that was a standard.
And when they got a JSON data set or a database or they bought something or they did a hackathon invariably, the documents ended up in some elastic with some security on it.
And now the some of the variation right in partner and case team performance is attributed internally through surveys to who knows where to get the data.
If you know, oh, I know to talk to this person, they will have the key to unlock this particular thing that I can then use to say, hey, look what we did this incredible work we did in your industry before or look at this incredible work we did for you in the past, right?
A new partner might not know that.
They've done five engagements that were very similar. So it's that kind of and I think the word is systematic. People want to be very much more systematic now because everyone is too busy and there's information overload. So that's really the to break those lines down.
My view is enterprise search now really desperately, desperately critically requires meta search. It's the only choice you cannot you're downloading, you know, pulling out all of the data, even if you were to desire that. It's very hard to do.
Now you're because you have to basically the old way would be to pull all the data out of everything and sort of filter it down. Why not search it? Yeah, our search is to say it's out there now. The vendors are doing incredible things.
I mean, service now from where it was years ago to where it is today. It's incredible. There's an amazing team of people working away on that and that's true of most applications now. Somebody's working on search. It has a nice high quality API. So let them do their thing. Let them master it.
But search and the other thing, the interesting that makes meta search particularly powerful for the enterprise is you're always searching on behalf of something. Right. And that avoids something that avoids it. It goes with the flow. It goes with the grain of the enterprise architecture.
You're supposed to query on behalf of something and if you do, in theory, the app can just maintain the context. It only gets tricky when you start saying, oh, I want to combine these five together. At the data level, when you do it at the user level, that's fine.
Either the user was authorized to see all three or they weren't or they were able to see a portion of it or they weren't. That's the way things work in the enterprise. So that's that's the subtle difference, right? To delineate them. Yeah. And why the potentials there is that indexing is costly.
And yet, on the. Yeah. And you described it really eloquently in a way that to some extent by implementing meta search, you wouldn't need to solve indexing issues. You wouldn't need to solve entitlement issues, right? You kind of like use the existing proxies.
But there is one remaining bit that I'm really curious about. So if you look at, let's say what Google did to the web search is that they looked at what you could call a proxonym effect.
So other people created pages linked to more important pages, hubs, and then you invent the algorithm, create it to you.
But you still kind of like rely on what others did in a way, right? And so now you have the page rank algorithm, how you how you rank the documents and all of a sudden, this is the breakthrough and this looks a lot more relevant. In enterprise search, you don't necessarily have this.
Okay, you do have documents that are being created, created, and so forth. But then as you said, there is a lot of silos, right? And so things get created.
There is no single place where you can say, what happened? What did I miss? What do you have on this topic and so forth? Just today in the morning, I was browsing through Office 365.
They have like a single page, which shows me all the documents that either I interacted with or someone interacted with and I am part of that group. And I can search there. That was helpful actually. That's all the lot of save the lot of time. But again, it doesn't have confidence.
It doesn't have Salesforce. It doesn't have a bunch of other places where it would go. So I guess one missing component, still in enterprise search was how would you rank these documents, right? Because you don't have a lot of signals. You simply have the documents themselves.
And so would you say that vector search now opens up this horizon for us? It helps solve this problem. Absolutely. And I think if we untangle it a little bit, it gets back to Google. In fact, it goes right back to Google. Google had the challenge of make they had the biggest data set in history.
The web incredibly interlinked. And they did the absolute best job of figuring out how to model that structure. You weren't searching every web page every time you searched. You were searching a structure that in fact is a large language model. Right? That's what they built.
They were the one they pioneered it. But it was the very first one. Or no, that's probably not true at all. Burr was an early one that got popular. I don't want to make, I have no idea. Right? What came first? But Burr was certainly the one that was the game changer. It was very recognized.
That's where the real popularization of transformer models I think came from. And it's that structure. What is that structure? It's a structure that can evaluate results almost independent of the results themselves. You don't have to look at every web page. And so that's the key.
In fact, you're absolutely right. I think there have been many attempts to do meta search and federated search even against APIs. But you then end up with just all the results. Tiled or whatever it is, but it's just all the results. And that doesn't help with information overload.
It also doesn't really get to the potential. So the key is, and what's world uses, we use a large language model. There's more to it, right? There's a relevancy algorithm around it.
There's a similarity pipeline around it, right? But at the end of the day, there's a large model that evaluates data as vectors with real numbers. And it allows you to do incredible comparisons. And the thing that, as I put this together, I wrote it nights and weekends starting last year.
And when I started to get results from it, I was shocked because I did not expect it to go to be as good as it came out. The thing about relevancy, right? It's, oh, man, we can always say we can, we'll identify it when we see it. But building tests around it is very difficult.
You come out with gold standards. And I love all the tooling. There's so much good tooling around it. But at the end of the day, it all depends, fundamentally, on really some set of finite labeled outcomes, right? That's what it is. I found another way to measure the relevancy without doing that.
And the way to do that is how far to the right are the term hits. And in, when you're using swirl, it favors because of the large language, the mall we used, it favors hits that are to the left, beginning of the sentence. It views aboutness as being at the beginning of the sentence.
It's extremely good at discriminating, again, identifying hits that are in passing. So I think we can all agree. Relovancy, I've always viewed relevancy as a bit of a stepped function.
The absolute top is exactly what I searched for in the entire field of the title and the body, right? At the end of the, the hits at the beginning of the body, we can probably agree that's got to be a good hit, the degree there's a title in a body.
And then we all fear the terrible mention, right? The enemy of relevancy is one mention of New York at the very end, right? It's like they're in the list of cities that absolutely have nothing to do with the big apple.
And that's what I found is that the relevancy function, the lower you are in the result list, the more to the right your search terms are. And the relevancy is what, the other thing about meta searches is you don't have the documents. I believe that an evidence-based approach is critical.
Did the silo return the search terms that you, the user put in, are they visible in the results? If they're not visible, then there's a question. So that's the other piece of it is we do use an evident space metric combined with similarity to say to rank and it works.
And now, so that said, here's all the stuff that I just left out. You have to normalize the query, especially if you interpret the query and rewrite it. One of the most important things about meta searches you can't send the same query to every endpoint. Not all endpoints are equal.
Some endpoints, for example, might be a database that's really able to target one field at a time effectively. So for example, they might be a repository that knows about companies. So if your search is electric vehicle Tesla, don't send electric vehicle in, just send Tesla.
So we provide a way to mark that. So we're all has the ability to tag each search provider with what it knows about. So you'd write that electric vehicle company colon Tesla. Tesla goes just to the company silos, the query. Everybody else drops the tag.
So Google gets electric vehicle Tesla, which of course, it doesn't have a magnificent job on. So then you have to normalize the query when you're scoring, as well as you have to normalize each field, right, as normal. Freshness is certainly an interesting thing.
I found the model also works best if we add a boost based on the top topness of the results. So if a repository gave it rank number one, we should probably at least factor that in a little bit. And then of course, there's things like number of hits.
And vector similarity is ultimately used, right? We aggregate vector similarities to reflect the evidence level. And then the strength of it, right, is captured in the similarity. So a lot went into it.
It's probably the most awful module in our in our repo, but somebody smarter will rewrite it soon, but it works. And that's the important thing. And that is why I'm here today, right? I have exited other ventures because I believe in this so much.
And I put together a little company that is here to support it. It's 100% open source under Apache 2.0. Get it or grab the darker and you can make it run in two lines. And you'll see. Yeah, that sounds so fantastic. And I'm sure our listeners will take a look, especially because it's open source.
It's much easier to you know, start hacking over the weekend or something. I also wanted to ask you before you show us some demos. I think this will be really, really interesting and change in format of the podcast to some extent.
You mentioned the similarity aspect of vector search, right? And so probably it also exists in keyword search to some extent, but there, as you said, we trained ourselves to look at what we see. And if we see how a keyword, we kind of trusted this more.
Although this probably varies per case, but in similarity search and vector search, this similarity is a play, right? So like, if you cannot find a top result, or even like a middle relevant result, you only find like very distant ones.
How do you detect this and how do you deal with this? So the similarity will be poor and there'll be no evidence. So the score will be low and it will be end up dropped to the back of the result list. That's the key. Now, there are a bunch of reasons that can happen though.
One of those reasons could be that perhaps we do not understand the domain, as well as the silo does.
 And one thing, one example of that is perhaps we're dealing with transformations of entities, very often dictionary based, or sometimes it's more subtle, but one of the things we learned very quickly is QueryGee is an open, an amazing open source package that's used with Elastic Solar, an open source, an open search, I should say.
And it rewrites queries. It's kind of the standard for it. It's very common to find it. It's really amazing. So here, the idea is that the silo knows something that we don't. So we actually have an integration now where we listen to the feedback that comes from each engine.
So if they report, for example, if they highlight hits, we check the similarity. The similarity is high enough and we'll honor that. And that's another idea, where we want each of those silos to, we want to honor their feedback.
Now, we're not today, but in the future, why not requery based on expanding our vocabulary around the search? Those are all things that can be done. And by the way, we'd love to get a pull request if someone wants to do that. That honestly is kind of the key to the whole thing. Yeah.
So you kind of like learn to innovate. Anyway, you have multiple voter problems, but you also want to really hear the signal, hear out the signal from every of the voter, and sort of like make sure that you roll this up to the best formula, right? The best representation of this signal to the user.
That's right. Absolutely. And then you can label some of those sounds because you're right. Some of them are getting really smart. Just some examples. I'll throw out some Vectara. Amazing, amazing, incredible vector database.
That's probably an inadequate description, but it answers questions on your documents. There's a revolution in Vector, in Vector search. Some people are focused very much on performance, right? Some people are focused on knowledge. Some people are focused on exporting Vectors.
So I think the enterprise, especially large enterprise, already has dozens of indexing tools and engines and others. And there will be many of these too, special case, right? There'll be some that are incredible at customer service. And some will be incredible at exception handling.
Some will be incredible at perhaps sales pre-qualification. You know, I just sort of learned from the past examples. Watson was going to diagnose everything, right? And I think what it ultimately did well was pre-approval authorizations.
So, but over time, I think it's clearly these will all become more automated. And so then, but you still need a way, if you're trying to figure out what's new across these salads, you still need a way to query them all. And so this world's happy. We have an integration with chat GPT.
You can query chat GPT. In fact, by default, we query it if you put your key in every time. So you and we rewrite the query. If the query is a question, we just pass it right along. If it's not, we ask rewrite it using a prompt to something like tell me about thing.
So you get a summary, right, which we pop up for, I think we also have a query processor. So you can have a chat GPT change the user's query. Like you could say rewrite this to a Boolean, or rewrite this why not to a vector.
But in the end, right, it's going to do that on its own on the back side of things. So when you're trying to solve problems in the enterprise, the key is you need an interface to write to.
And it would be nice not to have to write code to connect to all these things, getting back to your question about architecture. And so those are the key abstractions in Swirl. Swirl, you don't have to write code to connect to an endpoint that we already have a connector to.
You just write a search provider. All you need to know is JSON path and maybe be able to read a little developer API dog. Right. And then that you'll pretty much be able to get the search provider. If you need to write a connector. And of course, here's the punch line.
Well, I think it will probably take you a couple hours, depending on your skill at Python. But on average, it shouldn't take more than two hours because I can give you a prompt. And we can teach chat GPT about the connector class.
You should be able to get that done in a couple hours just fixing up what it does. I found that about 70% of the time, it will produce a workable connector. Just fast. The right prompt, right? Teach it how to teach it our connector class.
And give it the right prompt and bang, you have sort of almost working codes. Yeah, I think this is the best part of interfaces like chat GPT systems like chat GPT is that you can outsource this mundane work and really focus on the actual thing. I was actually born away myself.
And to some extent, scared you weeks ago when I was just saying, Hey, can you create a Python code which we'll talk to TomTom search API map search API. And it did create it. It just asked me to insert like a token. So I just subscribe developer token. But I was really blown away.
Like I would have spent probably like several half a days here and there figuring things out, right? If it wasn't TomTom or some other API. But yeah, I think this is amazing. And I think, well, I believe that you guys are documenting a lot.
But if you if you haven't yet, which just explained within documents, I think that could save a lot of time for developers. But I was wondering maybe you would like to show us a demo of swirl and then we'll dig deeper into that. Absolutely. So let me share my screen.
So hopefully you can see my screen. Yes. So this is swirl. Actually, I'll start here. This is the swirl repo. Everything you need to get started is here. The readme describes, pretty much the two commands you need to run to get swirl running if you have Docker.
There are more detailed instructions if you want to download. Everything that you'll see here runs, we have automated tests against everything. We have a whole CICD environment. And support, I just want to be clear, is free.
Please just join our Slack channel and we're happy to help anytime, anywhere. Now, when you get swirl installed locally, as I have it, you'll get this nice homepage. But ultimately, what most people want to see is the UI. So this is Spyglass.
It's an open source UI produced by a sister company, KMW, actually long time friend Kevin Waters. And he's a long time committer and a contributor to the open source community as well. So Spyglass is a great starting point for building user interfaces. It has a lot of the key building blocks.
And so here, yesterday, I was thinking about how we wrote a document. You sent me a document to use. And I admit today, I was seeing you're going, where is that document? And I actually said, okay, it's in Microsoft Outlook and I found it.
But I forgot that I could search because one of the great things about that's coming out in swirl version two, which is going to drop next month in May is we have full M365 support. So you can do the OAuth two dance. And I've actually searched through my M365.
And here's my acceptance of your your meeting, actually, some other references to it. And then here, document number four, document shared with you, vector podcast. So if I had searched, it would have been the fourth hit above the fold.
And I actually haven't done the relevancy tuning on email or one drive yet. So it worked well enough to come up. But what I think you can see again is the matches are early in the document. It favors them.
First of all, of course, it likes both terms together, but it favors them without with some exceptions. It favors the term that's to the left. And so you can see there were a lot of results, but only a few really ranked. Yeah, hi. And that's the key, right? I scan it. I'm pretty much done now.
And I can say, you know, I probably want to go look in my email or my one drive. That's more than likely where it is. And I can go and do that, you know, very simply. Right, there we go. Now I have in the top three. So the power of meta search though is more than just that.
I will just let's do that. Is it like a Django app or? Yes. Yeah. Yeah. So the stack is the stack is rabbit Django Python celery, although we're not using too much celery and SQLite or Postgres with a lot of packages. We use NLTK, Spacey, Jason Path, some others.
So now, so here I am running my electric vehicle company, Colin Tesla. This is an earlier version of the software. So you're going to see some, there's one bug here, which is you'll see the emphasis tags instead of having them render, just because I reloaded the older version.
But here we can see a lot more sources than just, just, you know, enterprise sources. And particular, one of the things that the swirl adaptive query processor does is it rewrites this query. Most repositories will get the search electric vehicle Tesla with the company tag removed.
However, the company funding database in BigQuery, which I just fixed, will actually only get the query Tesla. So if we now look at the results, you know, we'll see fairly traditional high quality content here about electric vehicles with Tesla favored early on.
So for example, it loves this hit with Tesla right at the beginning of the body. Most of these, I think are pretty good hits. And here, here's a database hit. This is from BigQuery. It's a company funding record. So Tesla Motors raised a large series C back in 2006.
This is an old database of funding records from Kaggle. Now, a couple of things I want to point out on the fly swirl allows you to turn a database record into a sort of pseudo document. You can actually just write this as a Python expression and use braces to refer to the fields.
And I'll show that in a second. In addition, though, swirl has a fixed schema URL title, body date published date retrieved and author, but it also has a payload field. The payload field can hold anything. And by default, anything that you don't specify for mapping goes into the payload.
You can also say, please don't put anything in the payload. So here, the fields are also repeated, right? As data items so that if I want, did I could extract those individually? And the idea here is you have a normalized record that reflects the sort of top relevancy items.
So you know whether or not you should go deeper. And then the payload will have anything extra that you might need to make that decision. So for example, if we look a little further down, here's a result from NLresearch.com.
Northern Light, the same company I started while working on search, or I learned a lot about search at was really the first company I worked for. Still going strong. One of the things they do is extract super high quality news from the web.
And they field it and they classify it and can really do rich searching. So here is an article that they pulled together about, you know, basically it's not so much about the electric vehicle market. It's about Tesla. So it ranked a little bit lower.
In this case, there were some other ones that ranked higher. They have some nice data that we like to capture and put in the payload as well. So this really is the core of swirl. And you say it has things like facets. For example, we use U-track internally to track issues.
So if I want to, you know, just switch to those, it'll bring just those up. Oh, looks like I pooped on that one. Another thing you can do when you're running, oops, looks like just a second. Another thing you can do, we have the concept of mixers. Not for drinks, but for results.
You can mix the results up by default. We do it by relevancy, but you can specify different mixers. For example, the date mixer will focus on it. Well, date sorted and it hides anything that doesn't have a date published.
The round robin mixer, on the other hand, still sort of honors relevancy, but it just takes one from each result. So you get a cross section of the results. So here, for example, you know, just looking at the top five, one result, the best result from each silo right here at the top.
And of course, here I'm arguing a little bit about the relevancy of this right in one of our support tickets. So you see everything kind of just brought together for me and I can decide which things I might like to do.
Yeah, maybe it could, I mean, I'm just commenting as we go, but maybe visually it could also show where this comes from, right? Because you do have on the left the sources. Yes. So could actually say this comes from here, this comes from there. But again, the combined view is also excellent.
It's just if you needed to know, right? If you need to know, where did I get this from, right? That's right. So we do, we do, we keep the source in the result here, along with whoever the source tells us the author is. However, in the in this version, we didn't get to it.
We like to report the original rank. So you should see IT news and I'll research one here. It's the number one result in the two point O version. Actually, there's a new version that's coming out. I think we're going to just do a bug fix on this. The latest version 10.
1, which is in the repo now, fixes that in a couple other issues. So if you just get the newest, you'll be good. In two point O that we have a little bit of a new treatment for this. I think you'll like a lot better. But before I jump to that, you asked me a really important question.
Right? So how this is great, this UI will evolve. It's here so that you can show the power, right? And we ship it integrated. But from a developer perspective, none of this is super helpful, right? How do I integrate this with an existing UI? So that's what I really wanted to show you next.
So first, how do we connect to something? The answer is a search provider definition. So this definition right here, this text record, mostly JSON, but mostly just strings.
This configures are out of the box request get connector to query a search provider, to query in particular this Google programmable search engine that I put together. And actually, we ship with three of them preset and please feel free to share our keys.
We're happy we want to make sure that something is working for everybody, right? Out of the box. So further in this, are the things you'd expect? You can configure this with by providing a URL. You can construct the URL by pulling in fields from the query mappings.
So the only thing that ever really changes in a Google PSC is the CX code. Everything else you can just copy and paste. You can put dozens of them in. Also here are some of the important system things that help the system work, help us process this.
So we have four different processing pipelines built into Swirl. One is a prequery that runs before Federation. And then there's a query processing pipeline that runs for each connector or actually actually say search provider, which is an instance, a configured instance of a connector.
Then each of those also has a result processing pipeline, which transforms the results from the source into our normalized format. And then there's a post result processing that does things like relevancy ranking where you want all of the data. And they're all different.
By the way, there's an object model behind Swirl. So grading these things is really simple. There are different base classes for those and they set you up with everything you need. So essentially you come in, you have a Python model or I should say a Django model object to operate on.
All you have to do is change it and exit and you're done. Simple, simple. Also, we map out the different query capabilities of each provider in the query mappings. So how do you tell a given endpoint to sort by date? This is how you add this to the URL. How do you page the results? This is how.
Result index is a Swirl capability where we can provide you with the index number. You can also use result page. So the count or the page that you want. And here's an important one too, the not character. So do the silo support not as a term. This one doesn't. It does not support not as a term.
But it supports the not character. So as an example, now if I go to the search object, I can run a search. I'll run it for knowledge management. So actually, I'll just let that one run for a second. There we go. I got my chat. I have the wrong chat GPT API key. But that's okay.
Everybody knows what we would say about this stuff. So actually the query I really want to do is Elon Musk not Twitter. So perfectly legitimate query, right? What's going on in Elon Musk's world that's not related to Twitter? Now here's the thing. Google PSC will not understand that query.
Everybody says what Google doesn't understand, not no web Google does, but Google programmable search engine does not honor or not. And in fact, just to prove it, PSC.google.com. By the way, before I talk to you, I didn't know of this system existence myself, PSC. Oh my gosh.
For web slicing up the web, it is incredible. I mean, it takes two seconds to build it, right? So and you just give it examples. So here's the thing. You can go, here's the public URL for one of the programmable search engines I put in and I'll do the same exact query. Elon Musk.
Okay, so the very first result has Twitter in it, right? It's right there. In fact, the second result also has Twitter. Google programmable search engine is not going through the full Google parser. And it does not honor the not. However, if I say this, it works perfectly.
The plus-minus syntax works. Okay. So now when we look at this definition, it says the not character for Google PSC is minus. So now if we look at the search I ran, let's look at the search object. It's another object inside a swirl.
Why is there a search object? Because in MetaSearch, it takes a few seconds to get the results from everything. And you may want to look at that data over and over again.
In fact, one of the cool things you can do is swirl is you can set the subscribe function, swirl well, then recheck for new results every so often and update and mark them new and you can even get an update things like that, right? So alert mode if you will or subscribe mode as we like to call it.
So let's take a look at the search object. What this object contains for starters, a block of messages that explain exactly what was done to the query. And here you can see the adaptive query processor rewrote the queries for Google PSC from Elon Musk not Twitter to Elon Musk minus Twitter.
So this way we guarantee you're going to get the right result, not a bad result. Oh, and also our relevancy model checks. If you have a nodded term in your query and it finds it in relevancy, we drop it to the bottom and say we actually put a special flag on it. We say this was a bad result.
Most of the others though, frankly, just either didn't know they don't handle not. You track doesn't handle a knot at all. So we removed it completely and just say, go and give us what you've got for that. And for others, we probably would have left them.
Looking at the results, there's also an info block. This is all JSON. So it's straightforward for developer using Python. It's little lists and dictionaries. There's a result that describes what each of the different sources gave back. Easy to parse if you want to build that.
You have a filter URL so you can construct your own facet display and to jump to any given provider. We actually give you the query that we ran. So if you want to check the results, assuming you have the right credentials, there's the results. So I can actually go look at and modify my JSON.
And then as you would expect, there's a summary of what was found. So here's what we actually searched. The overall query, if you want to rerun or update a query or rescore it, you can do that right from the result list. So those links are available.
We summarize the federation results and the time. Give you the next page of results, everything stored in swirl. So you can page through. By the way, you can also set a retention or exploration factor if you want. So results will simply disappear for secure applications. You can even do it.
So there's no storage at all. And then the results. So from a developer perspective, literally, I'm going to extract the results dictionary or sorry, the results list from this structure that I get back when I call it. And I'm going to iterate on that and each thing's a dictionary.
It's a flat dictionary with as the things you would expect pretty much, right? Title URL, body, date published date retrieved and author. Everything else is meta information. So what what search provider responded, what the rank was, our scores a score.
There's various techniques to turn that into a probability or a confidence level if you would like. We may do that in the future. I think it's if people wanted it, we'd love to hear about it. I think for now, though, people seem to be very happy just with rank.
Most importantly, and really, this is what swirls ultimate value is, we explain exactly why the result matched and why it scored as it did. So for example, we in this case, of course, there are no stems for a name, but we do as basically we use nltk, we stem to maximize recall.
Then you'll see the actual extracted hits, the actual hit, not the lower case tokenized version, right? So we extract the actual hit. And then we produce the score, which is this is the cosine similarity between the query and the text around it in the result.
So we kind of sentence tokenize the result that we get and then we're basically looking to try and stay within that sentence and see how relevant it is.
And ultimately, we also adjust since we are sending different queries to different systems and of course, different systems have different result links on average. We do adjustments for both of those. We also give you the exact token locations for everything that's hit and ready to rank from there.
Wow. So much is done behind the scenes here. And so much is simplified on the other side, on the outer side. That's amazing.
And how many systems do you support or which systems do you support out of the box today? So I'm happy to say we have connectors to all of the major open source search engines, including solar, AWS open search or open search.org, I should say, an elastic search.
We also support the main open databases, Postgres, SQLite, also some of the more traditional cloud ones, Google BigQuery, for example. And we are in the process of adding, as I mentioned, M365. We also have, as of the last one, you can connect to Atlassian using our request get.
You can connect to UTRAC. So many of the sophisticated repositories, you can actually just use the request get connector to talk to them. And M365 and Slack are coming in our next release, which is next month.
Well, I think especially Slack or any like messenger that also has this kind of APIs that can utilize, I think that's going to be like a big thing in my opinion, because so much is happening in Slack or similar platforms. You know, so much knowledge is kind of written there in public channel.
So you're in your own direct messages, right? It's possible to access them. Then I think that this is amazing. We even support Microsoft Teams in the next release, full search of messages, also all the shared objects, depending on configuration.
And if you're familiar with the M365 OpenID connect, the infrastructure and sort of that ecosystem, it's entirely under the deployers control. Swirl is just software.
I mean, we have a hosted platform which you get connected to, but the permissioning, all of that is actually done on the on the owner's side. And you can turn it off in one second for any reason you're uncomfortable. But Swirl 2.
0, again, we'll be coming out next month, has all of the OAuth and OIDC capabilities so that you're really just connecting your Microsoft account, searching through that stuff. And there's no other user interfaces or IDs or anything like that. It's all seamless.
And again, I'll completely controlled by the deploy inside that M36510 and owner. Yeah, fantastic. Is there something else you want to show on this demo? Or we want to go back to our audio mode video and audio for those who are listening only. All right. I hope that was more than enough.
You know, there's a ton to show. I just want to give a little flavor for it. And in particular, you know, we're really focused on making this easy for developers. That's the current audience. I think there's lots more we can do in the future.
But if you want to add a bunch of sources or solve a multi-silver search problem, that's what Swirls intended to do. That's a... It's amazing. It's amazing.
And how do you see the clientele? Like, what is the ideal client for this system? How do you want to interact with these clients? And how do you see...
Or maybe you'll already experience this, you know, first steps to succeeding on this path? So I honestly, people who are using it today are doing three things with it. And I'm super curious, right, as to which ones of these will evolve.
I think the most basic, you know, or interesting use case, right, or the sort of like the most obvious use case is one search box to rule them all, apart from the Lord of the Rings reference. But honestly, that's been so hard.
If you've done a lot of enterprise search projects, normally, you know, for the initial scope, and it's expensive, and it takes about a year or whatever, you know, you get a couple silos in place, and things are good, and people like it.
But adding silos over time is super costly, and it's hard, and this is the way to do it. You have a great existing search index, you have a search UI, awesome. Connect the search index to Swirl, and connect your UI to Swirl.
Now you can add a whole bunch of other sources and get great ranking, and you don't have to change the UI necessarily. For the most part, every search UI has URL, title, and body, and maybe a date. Okay, so if, for starters, you can just take those.
And if you have more, right, if you want to do a source facet, that's cool. From there, I think, you know, people with Python, right, Django, experience, and who want to take this and tailor it, we'd love to help, we'd love to hear what you're doing.
Again, please, the Slack supports all free, just join up the community and get in there, and tell us what's going on, or ask. And I think there's lots of other people who are working with it too, who are started to, you know, answer questions and things like that.
The second thing, though, there are definitely use cases where people really want to monitor multiple sources, and push notifications out, like, to Slack, and to teams, and things like that. That's a very different model.
I don't know if that's for everybody, but I think it's, in a way, that's the future. Right, we shouldn't have to ask when going to a search box takes time, and then I still have to parse it.
Depending on what you know, Swirl doesn't do any profiling or anything like that, depending on what you know, you're the builder of search apps, right, or inside apps.
You should be able to target them, but the barrier is usually not what we know about the user, right? Since they're an employee, we might have skill knowledge about them, right? We probably have access in theory to some other information about their job function and department and who they talk to.
So it shouldn't be that hard, but the problem isn't knowing that stuff. The problem is saying, okay, well, how do I get content, right? How do I get that out? So again, hook it up to Swirl.
 Build a watch list, which can be essentially a group of queries or set of search objects with the subscribe function turned on, you know, for a bunch of topics, push that data out to the people who need to know, create groups, use service accounts to search as opposed to using individual users, right?
Targeting individual users, not super valuable for proactive delivery, but on a group basis, very valuable.
So tell, right, create an industry feed that, you know, if you really know where to get the best industry data, why not make that systematic? Why not make that data available to everybody who's out there trying to talk to those folks through whatever, through their mobile?
And this is a thing like trying to do end-to-end enterprise search is super hard.
You got to get people to adopt your solution. Why would what do you want my mobile app for? You probably already have a cool one. You might already have five. So it's all about just putting that data out there so people can keep building fast. That's it. Yeah, this is amazing.
 I mean, you you simplified a lot in how you presented, you simplified a lot and you solved so many edge case, like not edge case, but like this really challenging things that are like showstoppers sometimes, you know, like, okay, I have this existing search demo app or something, you know, it's used within my department.
I just want to add one data source.
Now, what do I do, right? Do I really need to change my UI? Do I really need to rewrite the back end and things like that? And so I could actually, when I introduce swirl, will it actually precede every search back end call between UI and the search back end? That's how I do it now.
And like, we're setting it up. We use it internally and that's the way to do it rather than querying an index, you know, and then create just queries world and have it query all of those things. And what you get is the best results from across all sources.
Now, that's no substitute though, right, from going into the silo. Sometimes you need to go into the silo. They have in addition to a great search API and a lot of business logic right on their side, like query synums. There's a lot more.
You probably want to view the object in their environment versus in swirl, we can create a copy of it or whatever, like everybody else does. We don't.
If somebody wants to do preview, you know, there are so many technologies to do that, but why?
Instead, take, I think the best thing to do is after the user has scanned the shallow results that swirl gives you immediately two, two, three seconds, that's nothing compared to the time it takes to go to each silo.
After you've done three silos, you're already way saving, right? But then say, okay, look, it's obvious to me that the best results here are maybe in one drive in this folder or maybe it's in this team's chat or these teams chats.
So now click, go into that environment and hopefully you can then, right, traverse the data and get what you actually need. And down the road, when those repositories are serving up answers, right? We have mentioned chat, GPT much, but I assume you've seen the Microsoft co-pilot demo.
How long before that's pushing the data back, as opposed to you asking for it, right? It's saying, oh, here's the summary you need today. If you knew what to tell it, it could probably do that for you. So I think that's the new landscape.
The much more important thing than the one search box to rule them all is to use the power of meta-search to connect systems together and deliver information to the stuff you have already, to the workflows that work and make value already.
Whether that's Slack or, a newsletter or a notification to a Salesforce queue, that's the what you should do. The world doesn't need another search you are.
Yeah, especially like today, I saw a message on Slack for one of the senior managers saying, hey, what's the password to this thing?
And I can imagine that in the business schedules, you know, they don't have access, they don't have the password right now, they will switch to another topic, but maybe this topic was still important and maybe even one important, but they just don't want to wait.
And what you say is that in principle, they could have configured it once and access it as many times as they need. Exactly. Exactly.
And it's not uncommon in the world of, you know, consulting, strategic consulting, tech strategy, that the most powerful people are analysts and admins because, you know, partners are very busy, right, talking to and solving client problems and finding new ones.
So they rely on those folks to have access to all the systems and to go scour them. And of course, that's a waste, right? Probably nobody loves scouring those silos, but even more, we cannot be 100% systematic all the time.
 But with technologies like meta-search and push technologies and there's a million things you could use and there's a million ways to deliver those things, the opportunity is really there to let those people work on something else, right, to create value in other ways and not just be scouring it for everything that's relevant, for every, you know, give the best chance.
Yeah, absolutely.
And how do you view the problem of, or do you think it's a problem at all, of evolving such a search engine, you know, like, if, if I have the main experts who could actually label results for me for these queries, could I somehow integrate this into the process with swirl? Absolutely.
So that brings me actually nice lead into the third use case that the people are starting to look at with swirl. So exactly what you said, maybe I'm trying to build the chat GPT of my business, okay, maybe it doesn't even have to be that, maybe it has to be something, even a simpler version.
How would I automate handling of an exception when processing a mortgage, as an example? How could I automate that? That's really hard. That is probably not a rules-based system. But it's exactly what you said.
I need labels, right? So you're going to have your humans go scour, whatever, the various locations slack and teams and various products. And hopefully they find them and they label them.
Why not use MetaSearch for that?
 So if you can MetaSearch those things and use the language model, right, to basically say, I'm going to label anything over a certain score as being about this thing, then I give it a bunch of labels, let it hit, get a bunch of targets, let it go, find those things, hold the documents, because you will need the documents.
The difficulty of pulling documents compared to searching documents in M365 is one permission. So we are today, right, if you install swirl against M365, against your tenant, you are granting permission for swirl on behalf of some user, right, to search through the one drive files.
So you could also give a permission to fetch those files. So use swirl, to find the documents that are about the exception handling across silos, label the ones that are above a certain threshold.
Perhaps you could display those in a UI and let the, let the analyst check the labels, you could use a cool tool like Prodigy as an example, right, from explosion, the same folks who make spacey, which is what we use in in swirl.
 And I think from there you would say you if you trusted the labels, if the labels were good enough, you could actually do your first run, right, take 25 or 40% or whatever your preferred number of the labeled results out, build the machine learning model with the rest, and then test with the, you know, with the holdout set, do the, you know, if it's bad, build a confusion matrix, etc, etc.
There you go. And at least now you're reviewing and refining and adjusting the threshold as opposed to going and starting with hand labeling of data. Yeah. Yeah. That's, that's a great application for meta search and language models. Exactly.
And you explain basically kind of like in the, in the most straightforward way, you know, in a machine learning, out of machine learning model training testing validation, right, which doesn't escape in the search world doesn't escape from this. I think this is amazing.
You chose as the model for your product, open source. You have some thoughts on this. I really like this question when I asked this to, I think I asked it to Bob Van Lloyd from VV8 as well.
You know, why did you guys, you know, looking at your competition, let's say Pinecon didn't choose open source for some reasons that are valid for them, but you guys did.
And so did you, what makes you believe in this model work better? Because in some sense, it does require a lot of like public facing work, right? You need to explain, you need to document, you need to review pull requests with all the goodies that come with this, of course, right?
But there is an extra work involved, but you definitely get some benefits.
What is your thinking here? The truth is I've been an open source person forever.
I just believe in it, whether it was, Jeff Hammerbacker's amazing comment about how it's too bad that everyone's spending their time on clicks, right? And he believes that the data science approach benefits hugely from open source. That's so true.
Joseph Jackson, the notable VC, right, has written so much about its open source software that's really eating the world. It's eating at a considerably higher rate. And the reason I think is it's a few things. One is trust. One is trust.
You know, during the pandemic, I think the large enterprise saw a lot of promising young ventures just not make it. And if you bet on one of those technologies, you probably didn't get the technology. Or maybe you did, right? I don't know, but there was a certain amount of risk involved in that.
And open source does, although people, I don't think want to take the code and run with it, they want to know that they could, if they had to.
The second thing though, the trust is much deeper when you have a commercial company that supports open source, the so-called commercial open source model, because it does require that public investment, that public discipline. We're all about people using it. There's no sales.
Nobody has that title. We're here to make people successful using it. And I'm not sure, to be honest with you, how all the different ways it's going to evolve, but we want to evolve in line with what the actual community needs.
You know, I think you start with a kernel of an idea, and I've worked in search enough to have that. But beyond that, it's a collective thing. I love the way Vespa, as an example, is so open to look at how well it's evolving in the place that the community that needs it.
I think there's a similar community. And what is out there for them are a bunch of potentially some good and some unknown vendors, some interesting open source products, some of which might take a lot of work together.
And maybe their stories about super hot projects where there's one committee, and they go on vacation for two months and everything falls apart, where they lose interest after two years, and they leave with 2000 tickets. It's good to know that there's a little commercial entity.
But ultimately, aren't the greatest innovations coming from open source, open AI? Most of the pieces out there, that's why there have been so many replications. And that's the last piece of it. It's provable. You know, you can take my word for it. You can look at all the charts and stuff.
But with two commands, if you have Docker running, you can get swirl going, and you can see for yourself. Yeah. If it doesn't do something, well, help us make it better. Sorry, go ahead. Exactly. Exactly.
No, I mean, that exactly proves it because however magical the software is, if you are the engineer, you really want to like, you know, open the engine and see what's going on there.
How can I modify this? How can I plug this in? Because if it's not open, I guess, well, maybe someone will blame me and say, no, this is wrong.
But you know, if it's like an API that I need to pay for, what's the path for me to get into hacking? Should I buy it on my own credit card?
Or should I call my manager and say, hey, can you, well, and usually what happens if you look at Pinecon, for example, they will have, they will allocate like a free tier, right? And so you can kind of hack with free tier.
If you run out, then you'll call your manager, I guess. Right. And nothing wrong with that too. I mean, but I think that that's just a facilitation of the try and buy process. It's still a commercial company. You can't know for sure. Right. And honestly, that works for many companies.
There's no one size fits all. My point is this.
I think for solving complex, the kinds of complex multi-silow problems in the large enterprise where where I have been very lucky to work before and where I think, at least to some degree, I hear about the problems, right? Even if I don't understand them. I hear about the problems.
Open source is the winning model because it is so tailorable. You know, no one has the same thing. Everybody has seven of everything, I think, in the large enterprise. And then there's regulation and compliance regulatory systems, all that stuff.
Those things are the ones, those are the actual barriers. So open source is most adoptable in that regard. And then I think as long as there's someone who, you know, as long as there's some option to say, well, they're not disappearing, right? They're not.
There's still someone to help us who really knows how this thing works. It's, it's safe and tailorable. And that's what's really driving so much of the growth, the incredible growth in the software. Again, chat GPT, right? Paper, wood methods, not. It's being commercialized, but that's no surprise.
Yeah, I mean, it wouldn't probably exist if, like, just yesterday I was hacking something for going to bed. And it was super slow because I think it was US daytime. Everyone was probably hacking there as well. But I was fine with that. It was typing slowly, giving me some code snippets.
But could it have given me this code snippets if they were not online, if they were not like on GitHub or somewhere else, right? So I think it's kind of extending on the shoulders of giants again. Totally. I completely agree with you. And it's extremely limited.
Look, it was trained at least partly the noncode part, right? It was on Reddit. It reads like Reddit. It has a little bit of a know it, Ollie, you know, and it gives the sort of like consensus answer. Now, that's great for code as long as the consensus data is modern, current, and available.
So it's never going to teach you, it probably won't teach you that much about enterprise integration patterns and enterprise workloads. But it'll teach you a lot about open source. I write with it, I try to write with it almost every day.
And I can say this, it's very good at filling in a class function. If you teach it a class, it's very good at that. That seems to be, and that's really, I think, commodity work, right? How to connect to X? It's very, very disruptive there.
It's also potentially disruptive to a lot of natural language tasks. I think that's the way it is because it is at the end of the day a giant natural language model, right? So it's not surprising. It can do things like translation. It's very good at rewriting a query to make it broader.
It knows how to rewrite a query to make it Boolean. Those are never going to change. But getting the data to it. Again, if you want to build the chat GPT of mortgage exception handling, you're going to need to pull a lot of internal data, label it carefully.
That's that, and that, and you might discover you don't have enough. That could also be the case. There's a whole synthetic data market that's ready to solve that problem. So, but in a larger surprise, I think it's much more of the other problem. We can't get to it. We know it's there.
On that front, have you actually considered implementing a chat GPT plugin so that I can go as a user configure things at my tokens? And now, boom, I can search my internal data lakes. So we have, we are integrated with chat GPT. There's a connector so you can query it.
We, by default, send every query to it. We also have a query processor, and we will soon have a result processor that will summarize your results for you. But frankly, I think several people have already done stuff like that. So you just copy and paste the links. You can probably get that.
I think that's that's really an essential piece of it. Now, to query, like generate queries from chat GPT, I think that's easy to do. Right. Someone can do that. But this is my point. There will be other GPs. We refer to chat GPT as a question answer, right? Or questions.
If you say question, Colin, put your question in. We'll send it to chat GPT. I am sure people are looking at the amazing platforms you've just mentioned, right? All of them.
Those are going to end up deployed in different parts of the enterprise, answering questions, summarizing, extracting, predicting, prescribing. There will be all those things out there. And the key will be, how do you get at them? Yeah. It's still the problem. Right.
Just because you have something that will comment on the financial implications of a federal rule change, for example, right? Doesn't mean anyone's going to go look at it.
So, but if you made sure that every day or whatever it is or every that we were checking for new temporal updates from that and those were being pushed out to the people who needed to know that and read it, especially if you could check that they read it.
If you could imagine doing something like pushing information to analysts or somebody who's taking action on it and then tracking to see who read it and then watching their performance, I am sure that that will be a thing in the financial services world. You know, it's a tough world.
There's very used to a high level of governance, if you will, but I think that that's the kind of system that will ultimately produce the automation where the chat GPT will be able to solve the mortgage exception. So, on its own, 90% of the time, right? 10% of the time engaging a human. Yes.
That's somewhat scary, but I think it could also be liberating if done well. And I think there is a big discussion on this topic going on.
How do we collectively as a humanity, you know, make sure that this tech doesn't host us, right? Doesn't just kick us out of our professions or, you know, we still have a way to, I mean, even just going back to yesterday's example, I was going really in circles.
I was just drawing some pins on the map using chat GPT. And it couldn't get exactly the crux of what I was asking. And so I went to the kitchen.
I thought, just for two minutes and I thought, okay, I can just break down my code in two parts without telling chat GPT what I'm doing and just run everything in my ID and boom, I'm done because I was reasonably going in circles.
And maybe it's just me unable to, you know, engineer better prompt, so engineer better questions. Or maybe chat GPT does have limitations as well. You never know. But it did help me probably like 90% of the work was done using that interaction.
Like I would have spent several half a days as they call them or whatever evenings, figuring out all these things. Like what library should they use to connect to open source map or whatever. You know, how do I drop pins? Absolutely.
The chat GPT is the perfect replacement for the more senior developer, who will answer your texts right or your Slack, sorry Dave, my name's mine. You know, like that used to do work until you're blocked and then you go find somebody and say, okay, so I can't figure this out.
This was pre-internet, right? Now, for a long time, we had stack trace or the other thing that chat GPT has completely revised. Yeah, stack overflow. Stack overflow. Right. Exactly. Now it is we have stack overflow. For a while, we had stack overflow. And then now chat GPT, it's funny.
I forgot the name because I use chat GPT instead. I haven't Googled for a code thing in so long. I can't even replace your habit, right? Your memory and habit in some sense. Yeah.
Well, you know, we all get good at evaluating those, right? The stack overflow articles like, okay, so when's it from? How many upvotes does it have? Is there a good response? Does it have the green check mark? Chat GPT is pretty much bringing you back the green check mark answer.
So there's no point anymore. That's what it's good at. I totally review. It's funny. You mentioned this because exactly same thought across my mind when I was interacting with chat GPT. So that was like relating to my experience with stack overflow, doing some small Android application.
And I've ran into the issue which was described in like something like 20 questions and answers on exactly same topic. And everyone had a green, you know, check mark upvotes, but nothing worked. And in the end, I found just one of them that worked.
And you know, that was like the process in a way like iterative, repetitive, and also in some sense for trading, but then in the end, when you achieve it, you know, it's fine. You achieve what you want. With chat GPT is somewhat similar, but the experience is different.
I don't need to type that much. I mean, I don't need to type something into Google then go to Stackflow, you know, read this thing, comprehend it, and then apply it. With chat GPT, all of this is condensed.
It's like all of these steps just condensed and meet just literally typing what I want and getting something on the screen. Right. This part by itself is amazing. It is hard to predict where how far that will go. But I think that one thing is very clear.
The M365 silo is probably the most important one going forward because it's going to kind of automatically be taking the knowledge, which is very present in outlook, right? Maybe not so much encounter, but in your email is a lot of knowledge there in teams. There's a lot of knowledge there.
Documents, probably a decent amount there too, although I think that tends to be more scattered. But effectively, right? Chat GPT was trained from Reddit, which is chat. Teams is chat. Outlook is sort of chat. So there's no doubt that maybe those early interactions will come through that channel.
But I do think that exactly as you said early on, Microsoft is never going to make it easy to talk to anybody else. They still come from that position of silo dominance or whatever it is. They don't like to work with Salesforce. Salesforce doesn't like to work with them.
Nobody likes to use the non-great product in someone else's stack just because we're trying to consolidate. So that's why it persists. And that is very real and exacerbates the problem, the walls between the silos, and then throw in all the others.
After you get the basic whatever, big five, then you have all the elastics and open searches and solars and postgres and to say nothing of the applications. So one group is using swirl to look at five different ticket systems. They're all just ticket.
You track is one from JetBrains and then you're on the, there's some others. Okay, that's a really interesting problem. The cost to migrate all that stuff would be just, it's not even, I don't think it's necessarily that much money. It's just a massive amount of pain.
If you could figure out how to do it, probably some transfer much, it's not that much money, but it is a tremendous amount of work. Yes, I think you probably don't realize yourself yet, but from the way you explain this, it feels like you've invented JetGPT for the search part.
I mean, in some sense, like simplifying things, not actually, as you said, not requesting anyone to physically reinvent things like move data here and there, which can take years, sometimes like dozens of years, people simply don't do this.
And also access to the data, like today, I only remember a fraction of things that I did. I literally forget things that I've done yesterday.
I might sometimes reflect and I remember something a week ago or so, but it's still, it's because of information overload, and I need to make decisions, I need to scramble something together quickly on a conference page, how much knowledge do I have myself?
And if I had that magical search bar where I could have typed something and just get the support material, not to go all over the place, essentially doing what search engines should do, just go and check what happened where and when and by whom? Exactly.
Exactly. There's so much amazing work and time and genius that's gone into some of these apps. I mean, who doesn't love them? Like they're, you know, they all have incredible capabilities and they're evolved, they're growing all the time.
In a way, right, the idea that you would take data out to try to make sense of it is absurd. It really is. Think of Salesforce as 2,000 plus tables just to make the application work, you're going to extract that? No, you're going to query it.
And that's the key, right? And so we're focused on making the querying easy and understandable simplicity. You know, I've worked on some amazing products that were not simple.
And I'm sorry for some of them, right? Not being that simple, but at the end of the day, I think today in the enterprise, it's got to get easier. And there's got to be alternatives to indexing. And so thus the simplicity. Amazing. Here comes my favorite question.
As we get closer to the end of this amazing podcast episode, the question of why you've done a lot in software engineering, you've done quite a lot in search. You mentioned on all this companies, you know, like fast, which, you know, product became like Vespa and so on. You're building swirl.
Why? Like what keeps you motivated to do this? And as amazing as it is, like you're doing a lot of things. And also in the open, what motivates you to stay in this topic of search? You know, whether or not it's been searched, data integration has been the thing that I've always liked.
I started my career at John Hancock financial services working in marketing, doing customer segmentation. Interesting stuff. But really, the problem the company couldn't solve was how to view, well, completely separate product lines in one way.
They had no idea, right? 110-year-old company had no idea that it had a Pareto actually was somewhat worse. Like 10% or 15% of the customers were producing 80% of the premiums. Everybody got treated equally.
It was like a very old school business that was all about customers without really understanding customers. And it was still massively successful. So that's not an act. They were one of the biggest users of technology.
Also, Hancock had the largest IBM mainframe, I think, in the Northeast for many years.
But the silo problem was the problem that we had to solve to actually take the company to the level that it could compete with direct mail companies because direct mail companies had a lower cost basis and they knew the customer.
And that project quite honestly is the pattern that I have seen over and over again, regardless of what venture search has been one of them. But I was really lucky to work on mortgage processing too.
So a company called AI Foundry was actually backed by Kodak Alaris, which was the world leader in scanning at the time, right? Said, we need to come up with something to do. We need to do something interesting with this scanning technology.
And we'd like to apply it in a market other than consumer photos or things like that. Try to find a new market.
And mortgage turned out to be hot because if you've done a mortgage, right, if you've taken a mortgage, you have this ugly moment of sending them a bunch of documents and then you just have to wait. And then sometimes they're like, Oh, I need to do this one again.
I believe there's research that showed that something like one third of the applicants drop out every two or three days after, you know, you haven't got back to them with their documents. They just want that all clear, like you're good.
So AI Foundry used pretty interesting OCR's, zone technology, classification, text classification to turn the mortgage app into data, not 100% with the state of the art before was keying it, manually keying it, and then someone would manually review it. So we switched it to review.
Company was successful. It was a silo problem again. You could think of the different types, right, of articles as being fundamentally silos and understanding them was hard, and we do a lot of modeling and it worked. It worked great, right? Gaulous bought the company. That's just another example.
Did the same thing in an IoT company, most recently, where we're basically taking sensor data from healthcare settings, marrying it up with other data, like their EHR data and trying to predict, you know, likelihood of various conditions. So it's always the silo problem.
And frankly, every single one of these ventures would have benefited from something like swirl. So that's why I did it. It's because to be honest with you, I think the data problem is huge. I'm passionate about it.
And I think it's important to solve it because frankly, some of the service problems, right, that we all suffer when we're out in the field dealing with large companies because they just don't have the data.
They're not just trying to be mean or be clueless, right? Sometimes it's like, it's a hard problem to solve. We expect a lot now. As an engineer, right? I'm expecting chat GPT level response is pretty soon.
And yet, what we have is Siri, who like can barely figure out to turn off the alarm, you know, what it's going to. So there are going to be some bumps. There's going to be some sudden pulls and pushes. But I think the important thing is that why you ask me why do it open because prove it. Awesome.
Yeah, this is an amazing answer. So data is literally king and the one who has universal access to data, wins, right? In so many senses of this word. This is so great. This is so good. Chatting to you, Sid, I've learned a lot. I was wondering if there's something you would like to announce.
Something is cooking. Or you simply want to invite developers to a tutorial and to send a pull request. Well, I would love to do that. First of all, we have webinars every couple of weeks. Please come if you're interested.
Just, it's a, you just need to put an email address at the edge of the red form. We are also totally available on Slack. There's, you know, totally, we don't have sales. It's free. Just connect up. You'll talk to support or customer success. I guess is the more, more appropriate term these days.
But they're here. We're here to help. That includes me and everybody else on the team. There's only five of us. But we're all here to help. We would love to hear what you want to do this world, what you're doing this world.
We are here to write, if you need help with a search provider, we'll write it for you or help you help you get it working. What I can say for sure is this. Next month, version 2.0 will drop. It will be something you can one click try and it will have the M365 integration that I talked about.
So the full ability to deploy it to your tenant in our hosted version or just to take the Docker, run with it, hook that up so it will support OAuth 2 and OIDC. Many, many more features will be elaborating on the things you can do with it over the next couple of months, particularly in May.
And I just really would beg people to try it and tell us what you think. That's my ask. So if, and if anybody can, if you want to work on it, you know, we're always delighted to accept and even guide anybody as to where to start. Right. So that's where we are.
We're very young and we're trying to figure this out. And energetic and knowledgeable. And I think we will link everything you mentioned, of course, in the episode show notes so everyone can click it their will. And you know, follow and learn from you as I did today.
And I really want to allocate time also to participate in one of your webinars with them. I'm pretty sure I will learn more. That would be great. We are definitely bringing in folks. We had again, KMW, which makes Spyglass the open source project.
We had the author of Quarge came, came previously Renee. It was great fun. We hope to have him on again, because I think we could learn. I'm actually listening for our talk about the things they're doing. So and many others. So absolutely, we'd love to have you on.
And if you know anybody who wants to talk about the stuff too, please, I'd love to have them on as well. Fantastic. Thanks for pushing the envelope of search. Keep pushing. I wish you all the success that you can get and beyond.
And I hope we can chat more down the line down the road as you got, as you guys grow and I'm pretty sure you will.
Thank you so much for the confidence we will love to share updates in future, especially I'll be very psyched to show you some of the machine learning stuff we're talking about as a case, we definitely want to build that as a use case and make it one click easy to do that.
So yeah, let's keep it touch. I love to too. I mean, I'm a huge fan of the podcast. Obviously, I've listened to the Vespa cast several times and I think please keep it up. It's awesome. There's not enough people focused on this incredible area of technology. We're talking about stuff.
I think it's going to become more common, but it's still a little bit unknown. Yeah, appreciate your kind words. It's thanks to you, makers. Thank you so much, say it for your time. Really enjoyed it. Thank you very much. Bye bye.