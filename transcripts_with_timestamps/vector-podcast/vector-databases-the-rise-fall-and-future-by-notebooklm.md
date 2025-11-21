---
description: '<p><a target="_blank" rel="noopener noreferrer nofollow" href="https://www.vectorpodcast.com/">https://www.vectorpodcast.com/</a></p><p>I
  had fun interacting with NotebookLM - mostly for self-educational purposes. I think
  this tool can help by bringing an additional perspective over a textual content.
  It ties to what RAG (Retrieval Augmented Generation) can do to content generation
  in another modality. In this case, text is used to augment the generation of a podcast
  episode.</p><p>This episode is based on my blog post: <a target="_blank" rel="noopener
  noreferrer nofollow" href="https://dmitry-kan.medium.com/the-rise-fall-and-future-of-vector-databases-how-to-pick-the-one-that-lasts-6b9fbb43bbbe">https://dmitry-kan.medium.com/the-rise-fall-and-future-of-vector-databases-how-to-pick-the-one-that-lasts-6b9fbb43bbbe</a></p><p></p><p>Time
  codes:</p><p>00:00 Intro to the topic</p><p>1:11 Dmitry''s knowledge in the space</p><p>1:54
  Unpacking the Rise &amp; Fall idea</p><p>3:14 How attention got back to Vector DBs
  for a bit</p><p>4:18 Getting practical: Dmitry''s guide for choosing the right Vector
  Database</p><p>4:39 FAISS</p><p>5:34 What if you need fine-grained keyword search?
  Look at Apache Lucene-based engines</p><p>6:41 Exception to the rule: Late-interaction
  models</p><p>8:30 Latency and QPS: GSI APU, Vespa, Hyperspace</p><p>9:28 Strategic
  approach</p><p>9:55 Cloud solutions: CosmosDB, Vertex AI, Pinecone, Weaviate Cloud</p><p>10:14
  Community voice: pgvector</p><p>10:48 Picture of the fascinating future of the field</p><p>12:23
  Question to the audience</p><p>12:44 Taking a step back: key points</p><p>13:45
  Don''t get caught up in trendy shiny new tech</p><p></p><p>YouTube: <a target="_blank"
  rel="noopener noreferrer nofollow" href="https://www.youtube.com/watch?v=403rxbWZK9Y">https://www.youtube.com/watch?v=403rxbWZK9Y</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20250302_080303_04f8b5f2665529faa9d13569b97a18c9.png
pub_date: Sun, 02 Mar 2025 08:27:58 GMT
title: 'Vector Databases: The Rise, Fall and Future - by NotebookLM'
url: https://rss.com/podcasts/vector-podcast/1922013
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 1.24, "text": " Welcome
  back everybody.", "tokens": [50364, 4027, 646, 2201, 13, 50426], "temperature":
  0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 1, "seek": 0, "start": 1.24, "end":
  5.72, "text": " Today, we''re gonna be diving into the world", "tokens": [50426,
  2692, 11, 321, 434, 799, 312, 20241, 666, 264, 1002, 50650], "temperature": 0.0,
  "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095, "no_speech_prob":
  0.01761999912559986}, {"id": 2, "seek": 0, "start": 5.72, "end": 7.2, "text": "
  of vector databases.", "tokens": [50650, 295, 8062, 22380, 13, 50724], "temperature":
  0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 3, "seek": 0, "start": 7.2, "end":
  8.44, "text": " Ooh, fun.", "tokens": [50724, 7951, 11, 1019, 13, 50786], "temperature":
  0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 4, "seek": 0, "start": 8.44, "end":
  10.8, "text": " They''re rise, they''re potential fall,", "tokens": [50786, 814,
  434, 6272, 11, 436, 434, 3995, 2100, 11, 50904], "temperature": 0.0, "avg_logprob":
  -0.2856946832993451, "compression_ratio": 1.4946996466431095, "no_speech_prob":
  0.01761999912559986}, {"id": 5, "seek": 0, "start": 10.8, "end": 12.08, "text":
  " and with the future holds.", "tokens": [50904, 293, 365, 264, 2027, 9190, 13,
  50968], "temperature": 0.0, "avg_logprob": -0.2856946832993451, "compression_ratio":
  1.4946996466431095, "no_speech_prob": 0.01761999912559986}, {"id": 6, "seek": 0,
  "start": 12.08, "end": 12.92, "text": " Okay.", "tokens": [50968, 1033, 13, 51010],
  "temperature": 0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 7, "seek": 0, "start": 12.92, "end":
  14.68, "text": " You know, you sent us this fascinating medium article", "tokens":
  [51010, 509, 458, 11, 291, 2279, 505, 341, 10343, 6399, 7222, 51098], "temperature":
  0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 8, "seek": 0, "start": 14.68, "end":
  16.240000000000002, "text": " to kind of guide our exploration.", "tokens": [51098,
  281, 733, 295, 5934, 527, 16197, 13, 51176], "temperature": 0.0, "avg_logprob":
  -0.2856946832993451, "compression_ratio": 1.4946996466431095, "no_speech_prob":
  0.01761999912559986}, {"id": 9, "seek": 0, "start": 16.240000000000002, "end": 17.080000000000002,
  "text": " Ooh.", "tokens": [51176, 7951, 13, 51218], "temperature": 0.0, "avg_logprob":
  -0.2856946832993451, "compression_ratio": 1.4946996466431095, "no_speech_prob":
  0.01761999912559986}, {"id": 10, "seek": 0, "start": 17.080000000000002, "end":
  21.64, "text": " Called The Rise, Fall, and Future of Vector Databases.", "tokens":
  [51218, 45001, 440, 34482, 11, 7465, 11, 293, 20805, 295, 691, 20814, 40461, 1957,
  13, 51446], "temperature": 0.0, "avg_logprob": -0.2856946832993451, "compression_ratio":
  1.4946996466431095, "no_speech_prob": 0.01761999912559986}, {"id": 11, "seek": 0,
  "start": 21.64, "end": 24.36, "text": " How to pick the one that lasts by Dimitri
  Can.", "tokens": [51446, 1012, 281, 1888, 264, 472, 300, 20669, 538, 20975, 270,
  470, 1664, 13, 51582], "temperature": 0.0, "avg_logprob": -0.2856946832993451, "compression_ratio":
  1.4946996466431095, "no_speech_prob": 0.01761999912559986}, {"id": 12, "seek": 0,
  "start": 24.36, "end": 25.52, "text": " Yeah, I saw that one.", "tokens": [51582,
  865, 11, 286, 1866, 300, 472, 13, 51640], "temperature": 0.0, "avg_logprob": -0.2856946832993451,
  "compression_ratio": 1.4946996466431095, "no_speech_prob": 0.01761999912559986},
  {"id": 13, "seek": 0, "start": 25.52, "end": 27.92, "text": " Published January
  6th, 2025.", "tokens": [51640, 21808, 4173, 7061, 1386, 392, 11, 39209, 13, 51760],
  "temperature": 0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 14, "seek": 0, "start": 27.92, "end":
  28.84, "text": " Mm-hmm.", "tokens": [51760, 8266, 12, 10250, 13, 51806], "temperature":
  0.0, "avg_logprob": -0.2856946832993451, "compression_ratio": 1.4946996466431095,
  "no_speech_prob": 0.01761999912559986}, {"id": 15, "seek": 2884, "start": 28.84,
  "end": 33.32, "text": " So guess the term vector database might actually be", "tokens":
  [50364, 407, 2041, 264, 1433, 8062, 8149, 1062, 767, 312, 50588], "temperature":
  0.0, "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127,
  "no_speech_prob": 0.0015298514626920223}, {"id": 16, "seek": 2884, "start": 33.32,
  "end": 34.16, "text": " on its way out.", "tokens": [50588, 322, 1080, 636, 484,
  13, 50630], "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio":
  1.6265822784810127, "no_speech_prob": 0.0015298514626920223}, {"id": 17, "seek":
  2884, "start": 34.16, "end": 35.16, "text": " Really?", "tokens": [50630, 4083,
  30, 50680], "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio":
  1.6265822784810127, "no_speech_prob": 0.0015298514626920223}, {"id": 18, "seek":
  2884, "start": 35.16, "end": 37.76, "text": " And your choice of database could
  hinge on", "tokens": [50680, 400, 428, 3922, 295, 8149, 727, 28822, 322, 50810],
  "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127,
  "no_speech_prob": 0.0015298514626920223}, {"id": 19, "seek": 2884, "start": 37.76,
  "end": 40.4, "text": " needing things like faceted search.", "tokens": [50810, 18006,
  721, 411, 1915, 10993, 3164, 13, 50942], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 20, "seek": 2884, "start": 40.4, "end": 41.24, "text": " Oh, wow.", "tokens":
  [50942, 876, 11, 6076, 13, 50984], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 21, "seek": 2884, "start": 41.24, "end": 44.08, "text": " Or even those super
  cool late interaction models.", "tokens": [50984, 1610, 754, 729, 1687, 1627, 3469,
  9285, 5245, 13, 51126], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 22, "seek": 2884, "start": 44.08, "end": 45.239999999999995, "text": " Huh,
  interesting.", "tokens": [51126, 8063, 11, 1880, 13, 51184], "temperature": 0.0,
  "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127, "no_speech_prob":
  0.0015298514626920223}, {"id": 23, "seek": 2884, "start": 45.239999999999995, "end":
  45.84, "text": " And treat.", "tokens": [51184, 400, 2387, 13, 51214], "temperature":
  0.0, "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127,
  "no_speech_prob": 0.0015298514626920223}, {"id": 24, "seek": 2884, "start": 45.84,
  "end": 46.68, "text": " I know I am.", "tokens": [51214, 286, 458, 286, 669, 13,
  51256], "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio":
  1.6265822784810127, "no_speech_prob": 0.0015298514626920223}, {"id": 25, "seek":
  2884, "start": 46.68, "end": 47.44, "text": " Let''s break it all down.", "tokens":
  [51256, 961, 311, 1821, 309, 439, 760, 13, 51294], "temperature": 0.0, "avg_logprob":
  -0.21132066788211945, "compression_ratio": 1.6265822784810127, "no_speech_prob":
  0.0015298514626920223}, {"id": 26, "seek": 2884, "start": 47.44, "end": 48.28, "text":
  " Okay, let''s do it.", "tokens": [51294, 1033, 11, 718, 311, 360, 309, 13, 51336],
  "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127,
  "no_speech_prob": 0.0015298514626920223}, {"id": 27, "seek": 2884, "start": 48.28,
  "end": 49.4, "text": " So it''s gonna be good.", "tokens": [51336, 407, 309, 311,
  799, 312, 665, 13, 51392], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 28, "seek": 2884, "start": 49.4, "end": 51.28, "text": " What I thought was
  so interesting about this article", "tokens": [51392, 708, 286, 1194, 390, 370,
  1880, 466, 341, 7222, 51486], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 29, "seek": 2884, "start": 51.28, "end": 54.120000000000005, "text": " is
  how it really blends like the technical side", "tokens": [51486, 307, 577, 309,
  534, 37619, 411, 264, 6191, 1252, 51628], "temperature": 0.0, "avg_logprob": -0.21132066788211945,
  "compression_ratio": 1.6265822784810127, "no_speech_prob": 0.0015298514626920223},
  {"id": 30, "seek": 2884, "start": 54.120000000000005, "end": 55.8, "text": " with
  the broader AI landscape.", "tokens": [51628, 365, 264, 13227, 7318, 9661, 13, 51712],
  "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio": 1.6265822784810127,
  "no_speech_prob": 0.0015298514626920223}, {"id": 31, "seek": 2884, "start": 55.8,
  "end": 56.92, "text": " Yeah, you''re right.", "tokens": [51712, 865, 11, 291, 434,
  558, 13, 51768], "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio":
  1.6265822784810127, "no_speech_prob": 0.0015298514626920223}, {"id": 32, "seek":
  2884, "start": 56.92, "end": 58.36, "text": " It''s not just about the nuts and
  bolts.", "tokens": [51768, 467, 311, 406, 445, 466, 264, 10483, 293, 18127, 13,
  51840], "temperature": 0.0, "avg_logprob": -0.21132066788211945, "compression_ratio":
  1.6265822784810127, "no_speech_prob": 0.0015298514626920223}, {"id": 33, "seek":
  5836, "start": 58.36, "end": 60.519999999999996, "text": " It''s about how perceptions
  and adoption", "tokens": [50364, 467, 311, 466, 577, 35258, 293, 19215, 50472],
  "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 34, "seek": 5836, "start": 60.519999999999996,
  "end": 64.08, "text": " of vector databases are shifting within the AI world.",
  "tokens": [50472, 295, 8062, 22380, 366, 17573, 1951, 264, 7318, 1002, 13, 50650],
  "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 35, "seek": 5836, "start": 64.08,
  "end": 64.92, "text": " Absolutely.", "tokens": [50650, 7021, 13, 50692], "temperature":
  0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 36, "seek": 5836, "start": 64.92,
  "end": 66.8, "text": " Like this is not just a technical deep dive.", "tokens":
  [50692, 1743, 341, 307, 406, 445, 257, 6191, 2452, 9192, 13, 50786], "temperature":
  0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 37, "seek": 5836, "start": 66.8,
  "end": 67.8, "text": " Right.", "tokens": [50786, 1779, 13, 50836], "temperature":
  0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 38, "seek": 5836, "start": 67.8,
  "end": 69.84, "text": " This is about how people are thinking about these things.",
  "tokens": [50836, 639, 307, 466, 577, 561, 366, 1953, 466, 613, 721, 13, 50938],
  "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 39, "seek": 5836, "start": 69.84,
  "end": 70.36, "text": " Yeah.", "tokens": [50938, 865, 13, 50964], "temperature":
  0.0, "avg_logprob": -0.20929038885867957, "compression_ratio": 1.6266666666666667,
  "no_speech_prob": 0.00015660123608540744}, {"id": 40, "seek": 5836, "start": 70.36,
  "end": 71.36, "text": " And using them.", "tokens": [50964, 400, 1228, 552, 13,
  51014], "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio":
  1.6266666666666667, "no_speech_prob": 0.00015660123608540744}, {"id": 41, "seek":
  5836, "start": 71.36, "end": 72.36, "text": " Totally.", "tokens": [51014, 22837,
  13, 51064], "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio":
  1.6266666666666667, "no_speech_prob": 0.00015660123608540744}, {"id": 42, "seek":
  5836, "start": 72.36, "end": 74.72, "text": " And Dimitri brings this really unique
  perspective", "tokens": [51064, 400, 20975, 270, 470, 5607, 341, 534, 3845, 4585,
  51182], "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio":
  1.6266666666666667, "no_speech_prob": 0.00015660123608540744}, {"id": 43, "seek":
  5836, "start": 74.72, "end": 75.72, "text": " He does.", "tokens": [51182, 634,
  775, 13, 51232], "temperature": 0.0, "avg_logprob": -0.20929038885867957, "compression_ratio":
  1.6266666666666667, "no_speech_prob": 0.00015660123608540744}, {"id": 44, "seek":
  5836, "start": 75.72, "end": 76.96000000000001, "text": " to this whole conversation.",
  "tokens": [51232, 281, 341, 1379, 3761, 13, 51294], "temperature": 0.0, "avg_logprob":
  -0.20929038885867957, "compression_ratio": 1.6266666666666667, "no_speech_prob":
  0.00015660123608540744}, {"id": 45, "seek": 5836, "start": 76.96000000000001, "end":
  78.52, "text": " Because he was like deeply involved", "tokens": [51294, 1436, 415,
  390, 411, 8760, 3288, 51372], "temperature": 0.0, "avg_logprob": -0.20929038885867957,
  "compression_ratio": 1.6266666666666667, "no_speech_prob": 0.00015660123608540744},
  {"id": 46, "seek": 5836, "start": 78.52, "end": 81.0, "text": " in this emerging
  market just a few years back.", "tokens": [51372, 294, 341, 14989, 2142, 445, 257,
  1326, 924, 646, 13, 51496], "temperature": 0.0, "avg_logprob": -0.20929038885867957,
  "compression_ratio": 1.6266666666666667, "no_speech_prob": 0.00015660123608540744},
  {"id": 47, "seek": 5836, "start": 81.0, "end": 82.12, "text": " Oh, really?", "tokens":
  [51496, 876, 11, 534, 30, 51552], "temperature": 0.0, "avg_logprob": -0.20929038885867957,
  "compression_ratio": 1.6266666666666667, "no_speech_prob": 0.00015660123608540744},
  {"id": 48, "seek": 5836, "start": 82.12, "end": 87.4, "text": " He was even advising
  VCs on which vector database companies", "tokens": [51552, 634, 390, 754, 35598,
  691, 33290, 322, 597, 8062, 8149, 3431, 51816], "temperature": 0.0, "avg_logprob":
  -0.20929038885867957, "compression_ratio": 1.6266666666666667, "no_speech_prob":
  0.00015660123608540744}, {"id": 49, "seek": 8740, "start": 87.4, "end": 88.4, "text":
  " to back.", "tokens": [50364, 281, 646, 13, 50414], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 50, "seek": 8740, "start": 88.4, "end": 89.4, "text":
  " Wow.", "tokens": [50414, 3153, 13, 50464], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 51, "seek": 8740, "start": 89.4, "end": 90.4, "text":
  " So he''s like an insider.", "tokens": [50464, 407, 415, 311, 411, 364, 40990,
  13, 50514], "temperature": 0.0, "avg_logprob": -0.23036939559444305, "compression_ratio":
  1.694267515923567, "no_speech_prob": 0.0057039810344576836}, {"id": 52, "seek":
  8740, "start": 90.4, "end": 91.4, "text": " Yeah, he''s got the inside scoop.",
  "tokens": [50514, 865, 11, 415, 311, 658, 264, 1854, 19555, 13, 50564], "temperature":
  0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 53, "seek": 8740, "start": 91.4,
  "end": 94.48, "text": " So he really saw this whole thing unfold firsthand.", "tokens":
  [50564, 407, 415, 534, 1866, 341, 1379, 551, 17980, 38599, 13, 50718], "temperature":
  0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 54, "seek": 8740, "start": 94.48,
  "end": 95.72, "text": " He was there from the beginning.", "tokens": [50718, 634,
  390, 456, 490, 264, 2863, 13, 50780], "temperature": 0.0, "avg_logprob": -0.23036939559444305,
  "compression_ratio": 1.694267515923567, "no_speech_prob": 0.0057039810344576836},
  {"id": 55, "seek": 8740, "start": 95.72, "end": 97.12, "text": " Wow, that''s amazing.",
  "tokens": [50780, 3153, 11, 300, 311, 2243, 13, 50850], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 56, "seek": 8740, "start": 97.12, "end": 99.68, "text":
  " And it''s interesting because just a few years ago,", "tokens": [50850, 400, 309,
  311, 1880, 570, 445, 257, 1326, 924, 2057, 11, 50978], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 57, "seek": 8740, "start": 99.68, "end": 102.88000000000001,
  "text": " vector databases were like the hot topic.", "tokens": [50978, 8062, 22380,
  645, 411, 264, 2368, 4829, 13, 51138], "temperature": 0.0, "avg_logprob": -0.23036939559444305,
  "compression_ratio": 1.694267515923567, "no_speech_prob": 0.0057039810344576836},
  {"id": 58, "seek": 8740, "start": 102.88000000000001, "end": 104.2, "text": " They
  were everywhere, right?", "tokens": [51138, 814, 645, 5315, 11, 558, 30, 51204],
  "temperature": 0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 59, "seek": 8740, "start": 104.2,
  "end": 105.36000000000001, "text": " Everybody was talking about it.", "tokens":
  [51204, 7646, 390, 1417, 466, 309, 13, 51262], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 60, "seek": 8740, "start": 105.36000000000001, "end":
  107.4, "text": " Like they were the key to unlocking", "tokens": [51262, 1743, 436,
  645, 264, 2141, 281, 49620, 51364], "temperature": 0.0, "avg_logprob": -0.23036939559444305,
  "compression_ratio": 1.694267515923567, "no_speech_prob": 0.0057039810344576836},
  {"id": 61, "seek": 8740, "start": 107.4, "end": 110.44, "text": " all these powerful
  AI applications.", "tokens": [51364, 439, 613, 4005, 7318, 5821, 13, 51516], "temperature":
  0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 62, "seek": 8740, "start": 110.44,
  "end": 112.36000000000001, "text": " Like this was gonna change everything.", "tokens":
  [51516, 1743, 341, 390, 799, 1319, 1203, 13, 51612], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 63, "seek": 8740, "start": 112.36000000000001, "end":
  113.36000000000001, "text": " Everyone was so excited.", "tokens": [51612, 5198,
  390, 370, 2919, 13, 51662], "temperature": 0.0, "avg_logprob": -0.23036939559444305,
  "compression_ratio": 1.694267515923567, "no_speech_prob": 0.0057039810344576836},
  {"id": 64, "seek": 8740, "start": 113.36000000000001, "end": 114.36000000000001,
  "text": " Yeah.", "tokens": [51662, 865, 13, 51712], "temperature": 0.0, "avg_logprob":
  -0.23036939559444305, "compression_ratio": 1.694267515923567, "no_speech_prob":
  0.0057039810344576836}, {"id": 65, "seek": 8740, "start": 114.36000000000001, "end":
  116.48, "text": " Okay, so let''s unpack this whole rise and fall idea.", "tokens":
  [51712, 1033, 11, 370, 718, 311, 26699, 341, 1379, 6272, 293, 2100, 1558, 13, 51818],
  "temperature": 0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 66, "seek": 8740, "start": 116.48,
  "end": 117.32000000000001, "text": " Okay.", "tokens": [51818, 1033, 13, 51860],
  "temperature": 0.0, "avg_logprob": -0.23036939559444305, "compression_ratio": 1.694267515923567,
  "no_speech_prob": 0.0057039810344576836}, {"id": 67, "seek": 11732, "start": 117.32,
  "end": 118.96, "text": " So Dimitri noticed something interesting.", "tokens": [50364,
  407, 20975, 270, 470, 5694, 746, 1880, 13, 50446], "temperature": 0.0, "avg_logprob":
  -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801},
  {"id": 68, "seek": 11732, "start": 118.96, "end": 119.96, "text": " What''s up?",
  "tokens": [50446, 708, 311, 493, 30, 50496], "temperature": 0.0, "avg_logprob":
  -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801},
  {"id": 69, "seek": 11732, "start": 119.96, "end": 123.32, "text": " Fewer people
  were reading his early articles", "tokens": [50496, 33468, 260, 561, 645, 3760,
  702, 2440, 11290, 50664], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 70,
  "seek": 11732, "start": 123.32, "end": 125.08, "text": " about vector databases.",
  "tokens": [50664, 466, 8062, 22380, 13, 50752], "temperature": 0.0, "avg_logprob":
  -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801},
  {"id": 71, "seek": 11732, "start": 125.08, "end": 126.08, "text": " Oh, really?",
  "tokens": [50752, 876, 11, 534, 30, 50802], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 72,
  "seek": 11732, "start": 126.08, "end": 127.08, "text": " Huh?", "tokens": [50802,
  8063, 30, 50852], "temperature": 0.0, "avg_logprob": -0.20658189392089843, "compression_ratio":
  1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 73, "seek": 11732, "start":
  127.08, "end": 128.07999999999998, "text": " I wonder why.", "tokens": [50852, 286,
  2441, 983, 13, 50902], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 74,
  "seek": 11732, "start": 128.07999999999998, "end": 129.07999999999998, "text": "
  What do you make of that?", "tokens": [50902, 708, 360, 291, 652, 295, 300, 30,
  50952], "temperature": 0.0, "avg_logprob": -0.20658189392089843, "compression_ratio":
  1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 75, "seek": 11732, "start":
  129.07999999999998, "end": 132.51999999999998, "text": " Well, you know, it kind
  of hints at a potential shift", "tokens": [50952, 1042, 11, 291, 458, 11, 309, 733,
  295, 27271, 412, 257, 3995, 5513, 51124], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 76,
  "seek": 11732, "start": 132.51999999999998, "end": 133.51999999999998, "text": "
  in the industry.", "tokens": [51124, 294, 264, 3518, 13, 51174], "temperature":
  0.0, "avg_logprob": -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob":
  0.0007272476796060801}, {"id": 77, "seek": 11732, "start": 133.51999999999998, "end":
  134.51999999999998, "text": " Okay.", "tokens": [51174, 1033, 13, 51224], "temperature":
  0.0, "avg_logprob": -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob":
  0.0007272476796060801}, {"id": 78, "seek": 11732, "start": 134.51999999999998, "end":
  138.4, "text": " Instead of being seen as these like standalone solutions,", "tokens":
  [51224, 7156, 295, 885, 1612, 382, 613, 411, 37454, 6547, 11, 51418], "temperature":
  0.0, "avg_logprob": -0.20658189392089843, "compression_ratio": 1.55, "no_speech_prob":
  0.0007272476796060801}, {"id": 79, "seek": 11732, "start": 138.4, "end": 140.68,
  "text": " it seems like vector search technology", "tokens": [51418, 309, 2544,
  411, 8062, 3164, 2899, 51532], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 80,
  "seek": 11732, "start": 140.68, "end": 144.35999999999999, "text": " is kind of
  merging with other AI advancements,", "tokens": [51532, 307, 733, 295, 44559, 365,
  661, 7318, 7295, 1117, 11, 51716], "temperature": 0.0, "avg_logprob": -0.20658189392089843,
  "compression_ratio": 1.55, "no_speech_prob": 0.0007272476796060801}, {"id": 81,
  "seek": 11732, "start": 144.35999999999999, "end": 146.32, "text": " becoming part
  of a bigger picture.", "tokens": [51716, 5617, 644, 295, 257, 3801, 3036, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.20658189392089843, "compression_ratio": 1.55,
  "no_speech_prob": 0.0007272476796060801}, {"id": 82, "seek": 14632, "start": 146.32,
  "end": 147.32, "text": " Like what?", "tokens": [50364, 1743, 437, 30, 50414], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 83, "seek": 14632, "start": 147.32,
  "end": 150.44, "text": " Think LLM, small time modal search.", "tokens": [50414,
  6557, 441, 43, 44, 11, 1359, 565, 39745, 3164, 13, 50570], "temperature": 0.0, "avg_logprob":
  -0.1910396853819588, "compression_ratio": 1.6547231270358307, "no_speech_prob":
  0.0006415004609152675}, {"id": 84, "seek": 14632, "start": 150.44, "end": 152.0,
  "text": " They''re all getting more integrated.", "tokens": [50570, 814, 434, 439,
  1242, 544, 10919, 13, 50648], "temperature": 0.0, "avg_logprob": -0.1910396853819588,
  "compression_ratio": 1.6547231270358307, "no_speech_prob": 0.0006415004609152675},
  {"id": 85, "seek": 14632, "start": 152.0, "end": 154.35999999999999, "text": " Okay,
  so it''s not that vector databases", "tokens": [50648, 1033, 11, 370, 309, 311,
  406, 300, 8062, 22380, 50766], "temperature": 0.0, "avg_logprob": -0.1910396853819588,
  "compression_ratio": 1.6547231270358307, "no_speech_prob": 0.0006415004609152675},
  {"id": 86, "seek": 14632, "start": 154.35999999999999, "end": 155.6, "text": " are
  like vanishing.", "tokens": [50766, 366, 411, 3161, 3807, 13, 50828], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 87, "seek": 14632, "start": 155.6,
  "end": 156.44, "text": " Right.", "tokens": [50828, 1779, 13, 50870], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 88, "seek": 14632, "start": 156.44,
  "end": 157.44, "text": " They''re evolving.", "tokens": [50870, 814, 434, 21085,
  13, 50920], "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio":
  1.6547231270358307, "no_speech_prob": 0.0006415004609152675}, {"id": 89, "seek":
  14632, "start": 157.44, "end": 158.44, "text": " Exactly.", "tokens": [50920, 7587,
  13, 50970], "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio":
  1.6547231270358307, "no_speech_prob": 0.0006415004609152675}, {"id": 90, "seek":
  14632, "start": 158.44, "end": 159.72, "text": " I''m blending into more comprehensive
  solutions.", "tokens": [50970, 286, 478, 23124, 666, 544, 13914, 6547, 13, 51034],
  "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 91, "seek": 14632, "start": 159.72,
  "end": 160.72, "text": " That''s it.", "tokens": [51034, 663, 311, 309, 13, 51084],
  "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 92, "seek": 14632, "start": 160.72,
  "end": 161.72, "text": " Okay, I got it.", "tokens": [51084, 1033, 11, 286, 658,
  309, 13, 51134], "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio":
  1.6547231270358307, "no_speech_prob": 0.0006415004609152675}, {"id": 93, "seek":
  14632, "start": 161.72, "end": 163.48, "text": " The technology itself is still
  crucial.", "tokens": [51134, 440, 2899, 2564, 307, 920, 11462, 13, 51222], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 94, "seek": 14632, "start": 163.48,
  "end": 166.64, "text": " But how we think about it and use it is evolving.", "tokens":
  [51222, 583, 577, 321, 519, 466, 309, 293, 764, 309, 307, 21085, 13, 51380], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 95, "seek": 14632, "start": 166.64,
  "end": 167.64, "text": " Okay.", "tokens": [51380, 1033, 13, 51430], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 96, "seek": 14632, "start": 167.64,
  "end": 170.04, "text": " Like, you know, you have your traditional databases, right?",
  "tokens": [51430, 1743, 11, 291, 458, 11, 291, 362, 428, 5164, 22380, 11, 558, 30,
  51550], "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio":
  1.6547231270358307, "no_speech_prob": 0.0006415004609152675}, {"id": 97, "seek":
  14632, "start": 170.04, "end": 172.4, "text": " Like your SQL and no SQL types.",
  "tokens": [51550, 1743, 428, 19200, 293, 572, 19200, 3467, 13, 51668], "temperature":
  0.0, "avg_logprob": -0.1910396853819588, "compression_ratio": 1.6547231270358307,
  "no_speech_prob": 0.0006415004609152675}, {"id": 98, "seek": 14632, "start": 172.4,
  "end": 176.04, "text": " Well, a lot of them have integrated vector search capabilities
  now.", "tokens": [51668, 1042, 11, 257, 688, 295, 552, 362, 10919, 8062, 3164, 10862,
  586, 13, 51850], "temperature": 0.0, "avg_logprob": -0.1910396853819588, "compression_ratio":
  1.6547231270358307, "no_speech_prob": 0.0006415004609152675}, {"id": 99, "seek":
  17604, "start": 176.04, "end": 177.28, "text": " Oh, wow.", "tokens": [50364, 876,
  11, 6076, 13, 50426], "temperature": 0.0, "avg_logprob": -0.18342658148871527, "compression_ratio":
  1.7788161993769471, "no_speech_prob": 0.001304388279095292}, {"id": 100, "seek":
  17604, "start": 177.28, "end": 179.95999999999998, "text": " So the data type itself
  is becoming normalized", "tokens": [50426, 407, 264, 1412, 2010, 2564, 307, 5617,
  48704, 50560], "temperature": 0.0, "avg_logprob": -0.18342658148871527, "compression_ratio":
  1.7788161993769471, "no_speech_prob": 0.001304388279095292}, {"id": 101, "seek":
  17604, "start": 179.95999999999998, "end": 181.6, "text": " within these existing
  systems.", "tokens": [50560, 1951, 613, 6741, 3652, 13, 50642], "temperature": 0.0,
  "avg_logprob": -0.18342658148871527, "compression_ratio": 1.7788161993769471, "no_speech_prob":
  0.001304388279095292}, {"id": 102, "seek": 17604, "start": 181.6, "end": 182.6,
  "text": " Okay.", "tokens": [50642, 1033, 13, 50692], "temperature": 0.0, "avg_logprob":
  -0.18342658148871527, "compression_ratio": 1.7788161993769471, "no_speech_prob":
  0.001304388279095292}, {"id": 103, "seek": 17604, "start": 182.6, "end": 183.6,
  "text": " I see.", "tokens": [50692, 286, 536, 13, 50742], "temperature": 0.0, "avg_logprob":
  -0.18342658148871527, "compression_ratio": 1.7788161993769471, "no_speech_prob":
  0.001304388279095292}, {"id": 104, "seek": 17604, "start": 183.6, "end": 184.6,
  "text": " So it''s becoming more commonplace.", "tokens": [50742, 407, 309, 311,
  5617, 544, 2689, 6742, 13, 50792], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 105, "seek": 17604, "start": 184.6, "end": 185.6, "text": " Yeah.", "tokens":
  [50792, 865, 13, 50842], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 106, "seek": 17604, "start": 185.6, "end": 186.6, "text": " Exactly.", "tokens":
  [50842, 7587, 13, 50892], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 107, "seek": 17604, "start": 186.6, "end": 187.6, "text": " It''s not this
  like niche thing anymore.", "tokens": [50892, 467, 311, 406, 341, 411, 19956, 551,
  3602, 13, 50942], "temperature": 0.0, "avg_logprob": -0.18342658148871527, "compression_ratio":
  1.7788161993769471, "no_speech_prob": 0.001304388279095292}, {"id": 108, "seek":
  17604, "start": 187.6, "end": 188.6, "text": " Right.", "tokens": [50942, 1779,
  13, 50992], "temperature": 0.0, "avg_logprob": -0.18342658148871527, "compression_ratio":
  1.7788161993769471, "no_speech_prob": 0.001304388279095292}, {"id": 109, "seek":
  17604, "start": 188.6, "end": 189.6, "text": " It''s just part of the toolkit.",
  "tokens": [50992, 467, 311, 445, 644, 295, 264, 40167, 13, 51042], "temperature":
  0.0, "avg_logprob": -0.18342658148871527, "compression_ratio": 1.7788161993769471,
  "no_speech_prob": 0.001304388279095292}, {"id": 110, "seek": 17604, "start": 189.6,
  "end": 191.23999999999998, "text": " It''s becoming part of the fabric of how we
  work with data.", "tokens": [51042, 467, 311, 5617, 644, 295, 264, 7253, 295, 577,
  321, 589, 365, 1412, 13, 51124], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 111, "seek": 17604, "start": 191.23999999999998, "end": 193.12, "text": "
  I like that fabric of how we work with data.", "tokens": [51124, 286, 411, 300,
  7253, 295, 577, 321, 589, 365, 1412, 13, 51218], "temperature": 0.0, "avg_logprob":
  -0.18342658148871527, "compression_ratio": 1.7788161993769471, "no_speech_prob":
  0.001304388279095292}, {"id": 112, "seek": 17604, "start": 193.12, "end": 194.28,
  "text": " It''s a good way to put it right.", "tokens": [51218, 467, 311, 257, 665,
  636, 281, 829, 309, 558, 13, 51276], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 113, "seek": 17604, "start": 194.28, "end": 195.92, "text": " But here''s
  where things get really interesting.", "tokens": [51276, 583, 510, 311, 689, 721,
  483, 534, 1880, 13, 51358], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 114, "seek": 17604, "start": 195.92, "end": 196.92, "text": " Okay.", "tokens":
  [51358, 1033, 13, 51408], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 115, "seek": 17604, "start": 196.92, "end": 197.92, "text": " Tell me.",
  "tokens": [51408, 5115, 385, 13, 51458], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 116, "seek": 17604, "start": 197.92, "end": 202.12, "text": " Dimitri saw
  this resurgence in views for those older articles.", "tokens": [51458, 20975, 270,
  470, 1866, 341, 725, 44607, 294, 6809, 337, 729, 4906, 11290, 13, 51668], "temperature":
  0.0, "avg_logprob": -0.18342658148871527, "compression_ratio": 1.7788161993769471,
  "no_speech_prob": 0.001304388279095292}, {"id": 117, "seek": 17604, "start": 202.12,
  "end": 203.76, "text": " Oh, so people are coming back to them.", "tokens": [51668,
  876, 11, 370, 561, 366, 1348, 646, 281, 552, 13, 51750], "temperature": 0.0, "avg_logprob":
  -0.18342658148871527, "compression_ratio": 1.7788161993769471, "no_speech_prob":
  0.001304388279095292}, {"id": 118, "seek": 17604, "start": 203.76, "end": 205.32,
  "text": " They''re coming back and guess what?", "tokens": [51750, 814, 434, 1348,
  646, 293, 2041, 437, 30, 51828], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 119, "seek": 17604, "start": 205.32, "end": 206.0, "text": " What?", "tokens":
  [51828, 708, 30, 51862], "temperature": 0.0, "avg_logprob": -0.18342658148871527,
  "compression_ratio": 1.7788161993769471, "no_speech_prob": 0.001304388279095292},
  {"id": 120, "seek": 20600, "start": 206.0, "end": 211.24, "text": " We''ve been
  right when major funding announcements hit for some vector database startups back
  in", "tokens": [50364, 492, 600, 668, 558, 562, 2563, 6137, 23785, 2045, 337, 512,
  8062, 8149, 28041, 646, 294, 50626], "temperature": 0.0, "avg_logprob": -0.34150967355501854,
  "compression_ratio": 1.5121951219512195, "no_speech_prob": 0.003568369895219803},
  {"id": 121, "seek": 20600, "start": 211.24, "end": 212.24, "text": " April 2023.",
  "tokens": [50626, 6929, 44377, 13, 50676], "temperature": 0.0, "avg_logprob": -0.34150967355501854,
  "compression_ratio": 1.5121951219512195, "no_speech_prob": 0.003568369895219803},
  {"id": 122, "seek": 20600, "start": 212.24, "end": 213.24, "text": " Oh, interesting.",
  "tokens": [50676, 876, 11, 1880, 13, 50726], "temperature": 0.0, "avg_logprob":
  -0.34150967355501854, "compression_ratio": 1.5121951219512195, "no_speech_prob":
  0.003568369895219803}, {"id": 123, "seek": 20600, "start": 213.24, "end": 215.8,
  "text": " Like, big money was flowing back into this space.", "tokens": [50726,
  1743, 11, 955, 1460, 390, 13974, 646, 666, 341, 1901, 13, 50854], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 124, "seek": 20600, "start": 215.8,
  "end": 216.8, "text": " Yeah.", "tokens": [50854, 865, 13, 50904], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 125, "seek": 20600, "start": 216.8,
  "end": 218.64, "text": " Like, pine cones, $100 million series B.", "tokens": [50904,
  1743, 11, 15113, 40548, 11, 1848, 6879, 2459, 2638, 363, 13, 50996], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 126, "seek": 20600, "start": 218.64,
  "end": 219.64, "text": " Yeah.", "tokens": [50996, 865, 13, 51046], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 127, "seek": 20600, "start": 219.64,
  "end": 220.64, "text": " Pine cone was huge.", "tokens": [51046, 33531, 19749, 390,
  2603, 13, 51096], "temperature": 0.0, "avg_logprob": -0.34150967355501854, "compression_ratio":
  1.5121951219512195, "no_speech_prob": 0.003568369895219803}, {"id": 128, "seek":
  20600, "start": 220.64, "end": 222.72, "text": " Weve 8 securing $50 million.",
  "tokens": [51096, 492, 303, 1649, 33640, 1848, 2803, 2459, 13, 51200], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 129, "seek": 20600, "start": 222.72,
  "end": 223.72, "text": " Huh.", "tokens": [51200, 8063, 13, 51250], "temperature":
  0.0, "avg_logprob": -0.34150967355501854, "compression_ratio": 1.5121951219512195,
  "no_speech_prob": 0.003568369895219803}, {"id": 130, "seek": 20600, "start": 223.72,
  "end": 227.48, "text": " And QDran getting $7.5 million in seed funding.", "tokens":
  [51250, 400, 1249, 35, 4257, 1242, 1848, 22, 13, 20, 2459, 294, 8871, 6137, 13,
  51438], "temperature": 0.0, "avg_logprob": -0.34150967355501854, "compression_ratio":
  1.5121951219512195, "no_speech_prob": 0.003568369895219803}, {"id": 131, "seek":
  20600, "start": 227.48, "end": 228.48, "text": " Yeah.", "tokens": [51438, 865,
  13, 51488], "temperature": 0.0, "avg_logprob": -0.34150967355501854, "compression_ratio":
  1.5121951219512195, "no_speech_prob": 0.003568369895219803}, {"id": 132, "seek":
  20600, "start": 228.48, "end": 229.8, "text": " Those were big headlines.", "tokens":
  [51488, 3950, 645, 955, 23867, 13, 51554], "temperature": 0.0, "avg_logprob": -0.34150967355501854,
  "compression_ratio": 1.5121951219512195, "no_speech_prob": 0.003568369895219803},
  {"id": 133, "seek": 20600, "start": 229.8, "end": 230.8, "text": " They were.",
  "tokens": [51554, 814, 645, 13, 51604], "temperature": 0.0, "avg_logprob": -0.34150967355501854,
  "compression_ratio": 1.5121951219512195, "no_speech_prob": 0.003568369895219803},
  {"id": 134, "seek": 23080, "start": 230.8, "end": 237.16000000000003, "text": "
  It really highlights how much media coverage and industry buzz can influence how
  we perceive", "tokens": [50364, 467, 534, 14254, 577, 709, 3021, 9645, 293, 3518,
  13036, 393, 6503, 577, 321, 20281, 50682], "temperature": 0.0, "avg_logprob": -0.21253193600077025,
  "compression_ratio": 1.6869009584664536, "no_speech_prob": 0.20910020172595978},
  {"id": 135, "seek": 23080, "start": 237.16000000000003, "end": 238.56, "text": "
  technology trends.", "tokens": [50682, 2899, 13892, 13, 50752], "temperature": 0.0,
  "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536, "no_speech_prob":
  0.20910020172595978}, {"id": 136, "seek": 23080, "start": 238.56, "end": 239.56,
  "text": " Codally.", "tokens": [50752, 383, 378, 379, 13, 50802], "temperature":
  0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 137, "seek": 23080, "start": 239.56,
  "end": 241.28, "text": " It''s like a self-fulfilling prophecy almost.", "tokens":
  [50802, 467, 311, 411, 257, 2698, 12, 906, 69, 7345, 23945, 1920, 13, 50888], "temperature":
  0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 138, "seek": 23080, "start": 241.28,
  "end": 242.28, "text": " Yeah.", "tokens": [50888, 865, 13, 50938], "temperature":
  0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 139, "seek": 23080, "start": 242.28,
  "end": 246.36, "text": " And it makes you think like how much of what we perceive
  is like the next big thing is", "tokens": [50938, 400, 309, 1669, 291, 519, 411,
  577, 709, 295, 437, 321, 20281, 307, 411, 264, 958, 955, 551, 307, 51142], "temperature":
  0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 140, "seek": 23080, "start": 246.36,
  "end": 250.60000000000002, "text": " actually driven by, you know, the hype, the
  hype, the funding, the media attention.", "tokens": [51142, 767, 9555, 538, 11,
  291, 458, 11, 264, 24144, 11, 264, 24144, 11, 264, 6137, 11, 264, 3021, 3202, 13,
  51354], "temperature": 0.0, "avg_logprob": -0.21253193600077025, "compression_ratio":
  1.6869009584664536, "no_speech_prob": 0.20910020172595978}, {"id": 141, "seek":
  23080, "start": 250.60000000000002, "end": 251.60000000000002, "text": " Yeah.",
  "tokens": [51354, 865, 13, 51404], "temperature": 0.0, "avg_logprob": -0.21253193600077025,
  "compression_ratio": 1.6869009584664536, "no_speech_prob": 0.20910020172595978},
  {"id": 142, "seek": 23080, "start": 251.60000000000002, "end": 252.60000000000002,
  "text": " It''s fascinating.", "tokens": [51404, 467, 311, 10343, 13, 51454], "temperature":
  0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 143, "seek": 23080, "start": 252.60000000000002,
  "end": 256.40000000000003, "text": " So clearly, there''s still a ton of innovation
  and investment happening in the vector database", "tokens": [51454, 407, 4448, 11,
  456, 311, 920, 257, 2952, 295, 8504, 293, 6078, 2737, 294, 264, 8062, 8149, 51644],
  "temperature": 0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 144, "seek": 23080, "start": 256.40000000000003,
  "end": 257.40000000000003, "text": " space.", "tokens": [51644, 1901, 13, 51694],
  "temperature": 0.0, "avg_logprob": -0.21253193600077025, "compression_ratio": 1.6869009584664536,
  "no_speech_prob": 0.20910020172595978}, {"id": 145, "seek": 23080, "start": 257.40000000000003,
  "end": 258.40000000000003, "text": " Be sure.", "tokens": [51694, 879, 988, 13,
  51744], "temperature": 0.0, "avg_logprob": -0.21253193600077025, "compression_ratio":
  1.6869009584664536, "no_speech_prob": 0.20910020172595978}, {"id": 146, "seek":
  23080, "start": 258.40000000000003, "end": 260.56, "text": " But let''s get practical
  for our listener out there.", "tokens": [51744, 583, 718, 311, 483, 8496, 337, 527,
  31569, 484, 456, 13, 51852], "temperature": 0.0, "avg_logprob": -0.21253193600077025,
  "compression_ratio": 1.6869009584664536, "no_speech_prob": 0.20910020172595978},
  {"id": 147, "seek": 26056, "start": 260.56, "end": 261.96, "text": " Let''s give
  him some actionable advice.", "tokens": [50364, 961, 311, 976, 796, 512, 45098,
  5192, 13, 50434], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 148, "seek":
  26056, "start": 261.96, "end": 266.48, "text": " The real gem in this article is
  Demetri''s guide for choosing the right vector database.", "tokens": [50434, 440,
  957, 7173, 294, 341, 7222, 307, 4686, 302, 470, 311, 5934, 337, 10875, 264, 558,
  8062, 8149, 13, 50660], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 149, "seek": 26056, "start": 266.48, "end": 267.48, "text": " Right.", "tokens":
  [50660, 1779, 13, 50710], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 150, "seek": 26056, "start": 267.48, "end": 269.2, "text": " Because there''s
  no one size fits all solution.", "tokens": [50710, 1436, 456, 311, 572, 472, 2744,
  9001, 439, 3827, 13, 50796], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 151, "seek": 26056, "start": 269.2, "end": 270.2, "text": " Exactly.", "tokens":
  [50796, 7587, 13, 50846], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 152, "seek": 26056, "start": 270.2, "end": 271.44, "text": " It really depends
  on your specific needs.", "tokens": [50846, 467, 534, 5946, 322, 428, 2685, 2203,
  13, 50908], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 153, "seek":
  26056, "start": 271.44, "end": 274.84000000000003, "text": " It''s like having a
  roadmap for navigating this complex landscape.", "tokens": [50908, 467, 311, 411,
  1419, 257, 35738, 337, 32054, 341, 3997, 9661, 13, 51078], "temperature": 0.0, "avg_logprob":
  -0.2596795290511176, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.01484401524066925}, {"id": 154, "seek": 26056, "start": 274.84000000000003, "end":
  276.48, "text": " Totally a roadmap.", "tokens": [51078, 22837, 257, 35738, 13,
  51160], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 155, "seek":
  26056, "start": 276.48, "end": 278.6, "text": " So where does he suggest starting?",
  "tokens": [51160, 407, 689, 775, 415, 3402, 2891, 30, 51266], "temperature": 0.0,
  "avg_logprob": -0.2596795290511176, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.01484401524066925}, {"id": 156, "seek": 26056, "start": 278.6, "end": 279.6, "text":
  " Okay.", "tokens": [51266, 1033, 13, 51316], "temperature": 0.0, "avg_logprob":
  -0.2596795290511176, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.01484401524066925}, {"id": 157, "seek": 26056, "start": 279.6, "end": 280.6, "text":
  " I''m ready.", "tokens": [51316, 286, 478, 1919, 13, 51366], "temperature": 0.0,
  "avg_logprob": -0.2596795290511176, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.01484401524066925}, {"id": 158, "seek": 26056, "start": 280.6, "end": 283.4, "text":
  " His secret weapon is, FAYS.", "tokens": [51366, 2812, 4054, 7463, 307, 11, 479,
  4299, 50, 13, 51506], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 159, "seek":
  26056, "start": 283.4, "end": 284.4, "text": " Okay.", "tokens": [51506, 1033, 13,
  51556], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 160, "seek":
  26056, "start": 284.4, "end": 287.16, "text": " No, it''s not technically a full-fledged
  database.", "tokens": [51556, 883, 11, 309, 311, 406, 12120, 257, 1577, 12, 69,
  1493, 3004, 8149, 13, 51694], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 161, "seek": 26056, "start": 287.16, "end": 288.16, "text": " Right.", "tokens":
  [51694, 1779, 13, 51744], "temperature": 0.0, "avg_logprob": -0.2596795290511176,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.01484401524066925},
  {"id": 162, "seek": 26056, "start": 288.16, "end": 289.16, "text": " It''s more
  of a powerful library.", "tokens": [51744, 467, 311, 544, 295, 257, 4005, 6405,
  13, 51794], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 163, "seek":
  26056, "start": 289.16, "end": 290.16, "text": " Okay.", "tokens": [51794, 1033,
  13, 51844], "temperature": 0.0, "avg_logprob": -0.2596795290511176, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.01484401524066925}, {"id": 164, "seek":
  29016, "start": 290.16, "end": 294.40000000000003, "text": " So the kicker, it can
  handle massive data sets.", "tokens": [50364, 407, 264, 4437, 260, 11, 309, 393,
  4813, 5994, 1412, 6352, 13, 50576], "temperature": 0.0, "avg_logprob": -0.2221156081108198,
  "compression_ratio": 1.6058394160583942, "no_speech_prob": 0.07253293693065643},
  {"id": 165, "seek": 29016, "start": 294.40000000000003, "end": 295.40000000000003,
  "text": " Okay.", "tokens": [50576, 1033, 13, 50626], "temperature": 0.0, "avg_logprob":
  -0.2221156081108198, "compression_ratio": 1.6058394160583942, "no_speech_prob":
  0.07253293693065643}, {"id": 166, "seek": 29016, "start": 295.40000000000003, "end":
  297.04, "text": " We''re talking over a billion vectors.", "tokens": [50626, 492,
  434, 1417, 670, 257, 5218, 18875, 13, 50708], "temperature": 0.0, "avg_logprob":
  -0.2221156081108198, "compression_ratio": 1.6058394160583942, "no_speech_prob":
  0.07253293693065643}, {"id": 167, "seek": 29016, "start": 297.04, "end": 298.04,
  "text": " Wow.", "tokens": [50708, 3153, 13, 50758], "temperature": 0.0, "avg_logprob":
  -0.2221156081108198, "compression_ratio": 1.6058394160583942, "no_speech_prob":
  0.07253293693065643}, {"id": 168, "seek": 29016, "start": 298.04, "end": 299.04,
  "text": " That''s a lot.", "tokens": [50758, 663, 311, 257, 688, 13, 50808], "temperature":
  0.0, "avg_logprob": -0.2221156081108198, "compression_ratio": 1.6058394160583942,
  "no_speech_prob": 0.07253293693065643}, {"id": 169, "seek": 29016, "start": 299.04,
  "end": 300.04, "text": " So it can scale.", "tokens": [50808, 407, 309, 393, 4373,
  13, 50858], "temperature": 0.0, "avg_logprob": -0.2221156081108198, "compression_ratio":
  1.6058394160583942, "no_speech_prob": 0.07253293693065643}, {"id": 170, "seek":
  29016, "start": 300.04, "end": 301.32000000000005, "text": " We can handle the big
  stuff.", "tokens": [50858, 492, 393, 4813, 264, 955, 1507, 13, 50922], "temperature":
  0.0, "avg_logprob": -0.2221156081108198, "compression_ratio": 1.6058394160583942,
  "no_speech_prob": 0.07253293693065643}, {"id": 171, "seek": 29016, "start": 301.32000000000005,
  "end": 305.16, "text": " And the beauty of FAYS is its simplicity and scalability.",
  "tokens": [50922, 400, 264, 6643, 295, 479, 4299, 50, 307, 1080, 25632, 293, 15664,
  2310, 13, 51114], "temperature": 0.0, "avg_logprob": -0.2221156081108198, "compression_ratio":
  1.6058394160583942, "no_speech_prob": 0.07253293693065643}, {"id": 172, "seek":
  29016, "start": 305.16, "end": 309.84000000000003, "text": " So it''s perfect for,
  it''s perfect for initial exploration and prototyping.", "tokens": [51114, 407,
  309, 311, 2176, 337, 11, 309, 311, 2176, 337, 5883, 16197, 293, 46219, 3381, 13,
  51348], "temperature": 0.0, "avg_logprob": -0.2221156081108198, "compression_ratio":
  1.6058394160583942, "no_speech_prob": 0.07253293693065643}, {"id": 173, "seek":
  29016, "start": 309.84000000000003, "end": 311.92, "text": " You can just get in
  there and start playing around.", "tokens": [51348, 509, 393, 445, 483, 294, 456,
  293, 722, 2433, 926, 13, 51452], "temperature": 0.0, "avg_logprob": -0.2221156081108198,
  "compression_ratio": 1.6058394160583942, "no_speech_prob": 0.07253293693065643},
  {"id": 174, "seek": 29016, "start": 311.92, "end": 312.92, "text": " Exactly.",
  "tokens": [51452, 7587, 13, 51502], "temperature": 0.0, "avg_logprob": -0.2221156081108198,
  "compression_ratio": 1.6058394160583942, "no_speech_prob": 0.07253293693065643},
  {"id": 175, "seek": 29016, "start": 312.92, "end": 313.92, "text": " Yeah.", "tokens":
  [51502, 865, 13, 51552], "temperature": 0.0, "avg_logprob": -0.2221156081108198,
  "compression_ratio": 1.6058394160583942, "no_speech_prob": 0.07253293693065643},
  {"id": 176, "seek": 29016, "start": 313.92, "end": 315.96000000000004, "text": "
  But of course, uh oh, there''s always a butt.", "tokens": [51552, 583, 295, 1164,
  11, 2232, 1954, 11, 456, 311, 1009, 257, 6660, 13, 51654], "temperature": 0.0, "avg_logprob":
  -0.2221156081108198, "compression_ratio": 1.6058394160583942, "no_speech_prob":
  0.07253293693065643}, {"id": 177, "seek": 29016, "start": 315.96000000000004, "end":
  316.96000000000004, "text": " There''s a trade-off.", "tokens": [51654, 821, 311,
  257, 4923, 12, 4506, 13, 51704], "temperature": 0.0, "avg_logprob": -0.2221156081108198,
  "compression_ratio": 1.6058394160583942, "no_speech_prob": 0.07253293693065643},
  {"id": 178, "seek": 29016, "start": 316.96000000000004, "end": 317.96000000000004,
  "text": " Okay.", "tokens": [51704, 1033, 13, 51754], "temperature": 0.0, "avg_logprob":
  -0.2221156081108198, "compression_ratio": 1.6058394160583942, "no_speech_prob":
  0.07253293693065643}, {"id": 179, "seek": 29016, "start": 317.96000000000004, "end":
  318.96000000000004, "text": " What is it?", "tokens": [51754, 708, 307, 309, 30,
  51804], "temperature": 0.0, "avg_logprob": -0.2221156081108198, "compression_ratio":
  1.6058394160583942, "no_speech_prob": 0.07253293693065643}, {"id": 180, "seek":
  31896, "start": 318.96, "end": 321.12, "text": " Built-in filtering capabilities.",
  "tokens": [50364, 49822, 12, 259, 30822, 10862, 13, 50472], "temperature": 0.0,
  "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564, "no_speech_prob":
  0.07089832425117493}, {"id": 181, "seek": 31896, "start": 321.12, "end": 324.28,
  "text": " Uh, so you can''t really do that fine-grained search.", "tokens": [50472,
  4019, 11, 370, 291, 393, 380, 534, 360, 300, 2489, 12, 20735, 2001, 3164, 13, 50630],
  "temperature": 0.0, "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564,
  "no_speech_prob": 0.07089832425117493}, {"id": 182, "seek": 31896, "start": 324.28,
  "end": 325.28, "text": " Right.", "tokens": [50630, 1779, 13, 50680], "temperature":
  0.0, "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564,
  "no_speech_prob": 0.07089832425117493}, {"id": 183, "seek": 31896, "start": 325.28,
  "end": 326.47999999999996, "text": " Like with keywords and stuff.", "tokens": [50680,
  1743, 365, 21009, 293, 1507, 13, 50740], "temperature": 0.0, "avg_logprob": -0.2789870491863167,
  "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 184, "seek": 31896, "start": 326.47999999999996, "end": 328.52, "text": "
  Which might mean getting creative with workarounds?", "tokens": [50740, 3013, 1062,
  914, 1242, 5880, 365, 589, 289, 4432, 30, 50842], "temperature": 0.0, "avg_logprob":
  -0.2789870491863167, "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 185, "seek": 31896, "start": 328.52, "end": 329.52, "text": " Okay.", "tokens":
  [50842, 1033, 13, 50892], "temperature": 0.0, "avg_logprob": -0.2789870491863167,
  "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 186, "seek": 31896, "start": 329.52, "end": 330.52, "text": " So you''ve
  got to be a little clever.", "tokens": [50892, 407, 291, 600, 658, 281, 312, 257,
  707, 13494, 13, 50942], "temperature": 0.0, "avg_logprob": -0.2789870491863167,
  "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 187, "seek": 31896, "start": 330.52, "end": 331.52, "text": " A little bit.",
  "tokens": [50942, 316, 707, 857, 13, 50992], "temperature": 0.0, "avg_logprob":
  -0.2789870491863167, "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 188, "seek": 31896, "start": 331.52, "end": 334.52, "text": " If you want
  to use FAYS, I.S. for certain things.", "tokens": [50992, 759, 291, 528, 281, 764,
  479, 4299, 50, 11, 286, 13, 50, 13, 337, 1629, 721, 13, 51142], "temperature": 0.0,
  "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564, "no_speech_prob":
  0.07089832425117493}, {"id": 189, "seek": 31896, "start": 334.52, "end": 335.52,
  "text": " Yeah.", "tokens": [51142, 865, 13, 51192], "temperature": 0.0, "avg_logprob":
  -0.2789870491863167, "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 190, "seek": 31896, "start": 335.52, "end": 337.56, "text": " So if you need
  that fine-grained controlled keyword search.", "tokens": [51192, 407, 498, 291,
  643, 300, 2489, 12, 20735, 2001, 10164, 20428, 3164, 13, 51294], "temperature":
  0.0, "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564,
  "no_speech_prob": 0.07089832425117493}, {"id": 191, "seek": 31896, "start": 337.56,
  "end": 338.56, "text": " Yeah.", "tokens": [51294, 865, 13, 51344], "temperature":
  0.0, "avg_logprob": -0.2789870491863167, "compression_ratio": 1.564102564102564,
  "no_speech_prob": 0.07089832425117493}, {"id": 192, "seek": 31896, "start": 338.56,
  "end": 343.4, "text": " Along with your vector search, what does Demetri recommend?",
  "tokens": [51344, 17457, 365, 428, 8062, 3164, 11, 437, 775, 4686, 302, 470, 2748,
  30, 51586], "temperature": 0.0, "avg_logprob": -0.2789870491863167, "compression_ratio":
  1.564102564102564, "no_speech_prob": 0.07089832425117493}, {"id": 193, "seek": 31896,
  "start": 343.4, "end": 345.0, "text": " I''m all ears.", "tokens": [51586, 286,
  478, 439, 8798, 13, 51666], "temperature": 0.0, "avg_logprob": -0.2789870491863167,
  "compression_ratio": 1.564102564102564, "no_speech_prob": 0.07089832425117493},
  {"id": 194, "seek": 34500, "start": 345.0, "end": 349.28, "text": " He suggests
  looking at databases built on top of Lucene.", "tokens": [50364, 634, 13409, 1237,
  412, 22380, 3094, 322, 1192, 295, 9593, 1450, 13, 50578], "temperature": 0.0, "avg_logprob":
  -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 195, "seek": 34500, "start": 349.28, "end": 350.28,
  "text": " Lucene.", "tokens": [50578, 9593, 1450, 13, 50628], "temperature": 0.0,
  "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 196, "seek": 34500, "start": 350.28, "end": 354.68,
  "text": " Options like open search, elastic search, and a patchy solar.", "tokens":
  [50628, 42934, 411, 1269, 3164, 11, 17115, 3164, 11, 293, 257, 9972, 88, 7936, 13,
  50848], "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio":
  1.6933797909407666, "no_speech_prob": 0.3848007917404175}, {"id": 197, "seek": 34500,
  "start": 354.68, "end": 355.68, "text": " Got it.", "tokens": [50848, 5803, 309,
  13, 50898], "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio":
  1.6933797909407666, "no_speech_prob": 0.3848007917404175}, {"id": 198, "seek": 34500,
  "start": 355.68, "end": 359.12, "text": " So these are all built on this like solid
  foundation of Lucene technology.", "tokens": [50898, 407, 613, 366, 439, 3094, 322,
  341, 411, 5100, 7030, 295, 9593, 1450, 2899, 13, 51070], "temperature": 0.0, "avg_logprob":
  -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 199, "seek": 34500, "start": 359.12, "end": 360.12,
  "text": " Yeah.", "tokens": [51070, 865, 13, 51120], "temperature": 0.0, "avg_logprob":
  -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 200, "seek": 34500, "start": 360.12, "end": 361.12,
  "text": " Lucene''s been around for a while, right?", "tokens": [51120, 9593, 1450,
  311, 668, 926, 337, 257, 1339, 11, 558, 30, 51170], "temperature": 0.0, "avg_logprob":
  -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 201, "seek": 34500, "start": 361.12, "end": 363.56,
  "text": " It''s a mature technology with a proven track record.", "tokens": [51170,
  467, 311, 257, 14442, 2899, 365, 257, 12785, 2837, 2136, 13, 51292], "temperature":
  0.0, "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666,
  "no_speech_prob": 0.3848007917404175}, {"id": 202, "seek": 34500, "start": 363.56,
  "end": 364.56, "text": " Yeah.", "tokens": [51292, 865, 13, 51342], "temperature":
  0.0, "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666,
  "no_speech_prob": 0.3848007917404175}, {"id": 203, "seek": 34500, "start": 364.56,
  "end": 365.56, "text": " So it''s reliable.", "tokens": [51342, 407, 309, 311, 12924,
  13, 51392], "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio":
  1.6933797909407666, "no_speech_prob": 0.3848007917404175}, {"id": 204, "seek": 34500,
  "start": 365.56, "end": 366.56, "text": " Reliable.", "tokens": [51392, 8738, 9364,
  13, 51442], "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio":
  1.6933797909407666, "no_speech_prob": 0.3848007917404175}, {"id": 205, "seek": 34500,
  "start": 366.56, "end": 367.56, "text": " Yeah.", "tokens": [51442, 865, 13, 51492],
  "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666,
  "no_speech_prob": 0.3848007917404175}, {"id": 206, "seek": 34500, "start": 367.56,
  "end": 368.56, "text": " And it provides that robust keyword search.", "tokens":
  [51492, 400, 309, 6417, 300, 13956, 20428, 3164, 13, 51542], "temperature": 0.0,
  "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 207, "seek": 34500, "start": 368.56, "end": 369.56,
  "text": " Okay.", "tokens": [51542, 1033, 13, 51592], "temperature": 0.0, "avg_logprob":
  -0.1796564694108634, "compression_ratio": 1.6933797909407666, "no_speech_prob":
  0.3848007917404175}, {"id": 208, "seek": 34500, "start": 369.56, "end": 371.72,
  "text": " You mentioned plus multilingual support.", "tokens": [51592, 509, 2835,
  1804, 2120, 38219, 1406, 13, 51700], "temperature": 0.0, "avg_logprob": -0.1796564694108634,
  "compression_ratio": 1.6933797909407666, "no_speech_prob": 0.3848007917404175},
  {"id": 209, "seek": 34500, "start": 371.72, "end": 373.12, "text": " That''s important
  these days.", "tokens": [51700, 663, 311, 1021, 613, 1708, 13, 51770], "temperature":
  0.0, "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666,
  "no_speech_prob": 0.3848007917404175}, {"id": 210, "seek": 34500, "start": 373.12,
  "end": 374.12, "text": " Super important.", "tokens": [51770, 4548, 1021, 13, 51820],
  "temperature": 0.0, "avg_logprob": -0.1796564694108634, "compression_ratio": 1.6933797909407666,
  "no_speech_prob": 0.3848007917404175}, {"id": 211, "seek": 37412, "start": 374.12,
  "end": 376.72, "text": " And it performs incredibly well.", "tokens": [50364, 400,
  309, 26213, 6252, 731, 13, 50494], "temperature": 0.0, "avg_logprob": -0.2774854426761325,
  "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 212, "seek": 37412, "start": 376.72, "end": 378.56, "text": " So it''s fast
  and efficient.", "tokens": [50494, 407, 309, 311, 2370, 293, 7148, 13, 50586], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 213, "seek": 37412, "start": 378.56,
  "end": 379.56, "text": " Nice.", "tokens": [50586, 5490, 13, 50636], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 214, "seek": 37412, "start": 379.56,
  "end": 382.64, "text": " This makes it particularly well suited for e-commerce.",
  "tokens": [50636, 639, 1669, 309, 4098, 731, 24736, 337, 308, 12, 26926, 13, 50790],
  "temperature": 0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 215, "seek": 37412, "start": 382.64,
  "end": 384.44, "text": " Oh, interesting why e-commerce?", "tokens": [50790, 876,
  11, 1880, 983, 308, 12, 26926, 30, 50880], "temperature": 0.0, "avg_logprob": -0.2774854426761325,
  "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 216, "seek": 37412, "start": 384.44, "end": 391.36, "text": " Where features
  like faceting, which allows users to refine their search by specific attributes.",
  "tokens": [50880, 2305, 4122, 411, 1915, 9880, 11, 597, 4045, 5022, 281, 33906,
  641, 3164, 538, 2685, 17212, 13, 51226], "temperature": 0.0, "avg_logprob": -0.2774854426761325,
  "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 217, "seek": 37412, "start": 391.36, "end": 392.36, "text": " Oh, I see.",
  "tokens": [51226, 876, 11, 286, 536, 13, 51276], "temperature": 0.0, "avg_logprob":
  -0.2774854426761325, "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 218, "seek": 37412, "start": 392.36, "end": 394.44, "text": " So like filtering
  by brands.", "tokens": [51276, 407, 411, 30822, 538, 11324, 13, 51380], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 219, "seek": 37412, "start": 394.44,
  "end": 395.44, "text": " Yeah.", "tokens": [51380, 865, 13, 51430], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 220, "seek": 37412, "start": 395.44,
  "end": 396.44, "text": " Like filtering by brand.", "tokens": [51430, 1743, 30822,
  538, 3360, 13, 51480], "temperature": 0.0, "avg_logprob": -0.2774854426761325, "compression_ratio":
  1.693103448275862, "no_speech_prob": 0.31069931387901306}, {"id": 221, "seek": 37412,
  "start": 396.44, "end": 397.44, "text": " Price range.", "tokens": [51480, 25803,
  3613, 13, 51530], "temperature": 0.0, "avg_logprob": -0.2774854426761325, "compression_ratio":
  1.693103448275862, "no_speech_prob": 0.31069931387901306}, {"id": 222, "seek": 37412,
  "start": 397.44, "end": 398.44, "text": " Price range size.", "tokens": [51530,
  25803, 3613, 2744, 13, 51580], "temperature": 0.0, "avg_logprob": -0.2774854426761325,
  "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 223, "seek": 37412, "start": 398.44, "end": 399.68, "text": " All those things
  are essential.", "tokens": [51580, 1057, 729, 721, 366, 7115, 13, 51642], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 224, "seek": 37412, "start": 399.68,
  "end": 401.16, "text": " Makes sense for e-commerce.", "tokens": [51642, 25245,
  2020, 337, 308, 12, 26926, 13, 51716], "temperature": 0.0, "avg_logprob": -0.2774854426761325,
  "compression_ratio": 1.693103448275862, "no_speech_prob": 0.31069931387901306},
  {"id": 225, "seek": 37412, "start": 401.16, "end": 402.56, "text": " He did mention
  one exception though, right?", "tokens": [51716, 634, 630, 2152, 472, 11183, 1673,
  11, 558, 30, 51786], "temperature": 0.0, "avg_logprob": -0.2774854426761325, "compression_ratio":
  1.693103448275862, "no_speech_prob": 0.31069931387901306}, {"id": 226, "seek": 37412,
  "start": 402.56, "end": 403.56, "text": " Though there''s always an exception.",
  "tokens": [51786, 10404, 456, 311, 1009, 364, 11183, 13, 51836], "temperature":
  0.0, "avg_logprob": -0.2774854426761325, "compression_ratio": 1.693103448275862,
  "no_speech_prob": 0.31069931387901306}, {"id": 227, "seek": 40356, "start": 404.56,
  "end": 405.56, "text": " What is it?", "tokens": [50414, 708, 307, 309, 30, 50464],
  "temperature": 0.0, "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6,
  "no_speech_prob": 0.002844778122380376}, {"id": 228, "seek": 40356, "start": 405.56,
  "end": 408.28000000000003, "text": " Cudrant, even though it''s not built on Lucene.",
  "tokens": [50464, 383, 532, 7541, 11, 754, 1673, 309, 311, 406, 3094, 322, 9593,
  1450, 13, 50600], "temperature": 0.0, "avg_logprob": -0.21318682352701823, "compression_ratio":
  1.6, "no_speech_prob": 0.002844778122380376}, {"id": 229, "seek": 40356, "start":
  408.28000000000003, "end": 409.28000000000003, "text": " Oh, okay.", "tokens": [50600,
  876, 11, 1392, 13, 50650], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 230, "seek":
  40356, "start": 409.28000000000003, "end": 411.6, "text": " Includes fascinating
  capabilities.", "tokens": [50650, 7779, 1471, 279, 10343, 10862, 13, 50766], "temperature":
  0.0, "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6, "no_speech_prob":
  0.002844778122380376}, {"id": 231, "seek": 40356, "start": 411.6, "end": 412.6,
  "text": " Interesting.", "tokens": [50766, 14711, 13, 50816], "temperature": 0.0,
  "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6, "no_speech_prob":
  0.002844778122380376}, {"id": 232, "seek": 40356, "start": 412.6, "end": 414.4,
  "text": " So it''s kind of a hybrid approach.", "tokens": [50816, 407, 309, 311,
  733, 295, 257, 13051, 3109, 13, 50906], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 233, "seek":
  40356, "start": 414.4, "end": 416.48, "text": " Making it a contender in those scenarios
  too.", "tokens": [50906, 14595, 309, 257, 660, 3216, 294, 729, 15077, 886, 13, 51010],
  "temperature": 0.0, "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6,
  "no_speech_prob": 0.002844778122380376}, {"id": 234, "seek": 40356, "start": 416.48,
  "end": 418.4, "text": " So Cudrant''s kind of a wild card.", "tokens": [51010, 407,
  383, 532, 7541, 311, 733, 295, 257, 4868, 2920, 13, 51106], "temperature": 0.0,
  "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6, "no_speech_prob":
  0.002844778122380376}, {"id": 235, "seek": 40356, "start": 418.4, "end": 419.4,
  "text": " A little bit.", "tokens": [51106, 316, 707, 857, 13, 51156], "temperature":
  0.0, "avg_logprob": -0.21318682352701823, "compression_ratio": 1.6, "no_speech_prob":
  0.002844778122380376}, {"id": 236, "seek": 40356, "start": 419.4, "end": 420.4,
  "text": " Yeah.", "tokens": [51156, 865, 13, 51206], "temperature": 0.0, "avg_logprob":
  -0.21318682352701823, "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376},
  {"id": 237, "seek": 40356, "start": 420.4, "end": 421.72, "text": " It''s got its
  own unique set of features.", "tokens": [51206, 467, 311, 658, 1080, 1065, 3845,
  992, 295, 4122, 13, 51272], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 238, "seek":
  40356, "start": 421.72, "end": 424.8, "text": " And it shows the importance of going
  beyond general categories.", "tokens": [51272, 400, 309, 3110, 264, 7379, 295, 516,
  4399, 2674, 10479, 13, 51426], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 239, "seek":
  40356, "start": 424.8, "end": 425.8, "text": " Yeah.", "tokens": [51426, 865, 13,
  51476], "temperature": 0.0, "avg_logprob": -0.21318682352701823, "compression_ratio":
  1.6, "no_speech_prob": 0.002844778122380376}, {"id": 240, "seek": 40356, "start":
  425.8, "end": 429.64, "text": " And really digging into the specific features each
  database offers.", "tokens": [51476, 400, 534, 17343, 666, 264, 2685, 4122, 1184,
  8149, 7736, 13, 51668], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 241, "seek":
  40356, "start": 429.64, "end": 430.64, "text": " Absolutely.", "tokens": [51668,
  7021, 13, 51718], "temperature": 0.0, "avg_logprob": -0.21318682352701823, "compression_ratio":
  1.6, "no_speech_prob": 0.002844778122380376}, {"id": 242, "seek": 40356, "start":
  430.64, "end": 433.12, "text": " You can''t just like assume that because it''s
  in one category.", "tokens": [51718, 509, 393, 380, 445, 411, 6552, 300, 570, 309,
  311, 294, 472, 7719, 13, 51842], "temperature": 0.0, "avg_logprob": -0.21318682352701823,
  "compression_ratio": 1.6, "no_speech_prob": 0.002844778122380376}, {"id": 243, "seek":
  43312, "start": 433.12, "end": 434.12, "text": " Right.", "tokens": [50364, 1779,
  13, 50414], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 244, "seek": 43312,
  "start": 434.12, "end": 435.12, "text": " It''s got all the features you need.",
  "tokens": [50414, 467, 311, 658, 439, 264, 4122, 291, 643, 13, 50464], "temperature":
  0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 245, "seek": 43312, "start": 435.12,
  "end": 436.12, "text": " You got to do your research.", "tokens": [50464, 509, 658,
  281, 360, 428, 2132, 13, 50514], "temperature": 0.0, "avg_logprob": -0.1812015919203169,
  "compression_ratio": 1.7701863354037266, "no_speech_prob": 0.1291946917772293},
  {"id": 246, "seek": 43312, "start": 436.12, "end": 437.44, "text": " You got to
  look under the hood.", "tokens": [50514, 509, 658, 281, 574, 833, 264, 13376, 13,
  50580], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 247, "seek": 43312,
  "start": 437.44, "end": 438.44, "text": " Exactly.", "tokens": [50580, 7587, 13,
  50630], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 248, "seek": 43312,
  "start": 438.44, "end": 441.64, "text": " Now what if you need something more advanced?",
  "tokens": [50630, 823, 437, 498, 291, 643, 746, 544, 7339, 30, 50790], "temperature":
  0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 249, "seek": 43312, "start": 441.64,
  "end": 442.64, "text": " Okay.", "tokens": [50790, 1033, 13, 50840], "temperature":
  0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 250, "seek": 43312, "start": 442.64,
  "end": 443.64, "text": " Like what?", "tokens": [50840, 1743, 437, 30, 50890], "temperature":
  0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 251, "seek": 43312, "start": 443.64,
  "end": 444.96, "text": " Like support for those late interaction models.", "tokens":
  [50890, 1743, 1406, 337, 729, 3469, 9285, 5245, 13, 50956], "temperature": 0.0,
  "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266, "no_speech_prob":
  0.1291946917772293}, {"id": 252, "seek": 43312, "start": 444.96, "end": 446.16,
  "text": " Late interaction models, huh?", "tokens": [50956, 31220, 9285, 5245, 11,
  7020, 30, 51016], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 253, "seek": 43312,
  "start": 446.16, "end": 447.16, "text": " Yeah.", "tokens": [51016, 865, 13, 51066],
  "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 254, "seek": 43312, "start": 447.16,
  "end": 448.16, "text": " If you heard of these.", "tokens": [51066, 759, 291, 2198,
  295, 613, 13, 51116], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 255, "seek": 43312,
  "start": 448.16, "end": 449.64, "text": " I''ve heard the term, but I''m not really
  sure what they were.", "tokens": [51116, 286, 600, 2198, 264, 1433, 11, 457, 286,
  478, 406, 534, 988, 437, 436, 645, 13, 51190], "temperature": 0.0, "avg_logprob":
  -0.1812015919203169, "compression_ratio": 1.7701863354037266, "no_speech_prob":
  0.1291946917772293}, {"id": 256, "seek": 43312, "start": 449.64, "end": 450.64,
  "text": " Okay.", "tokens": [51190, 1033, 13, 51240], "temperature": 0.0, "avg_logprob":
  -0.1812015919203169, "compression_ratio": 1.7701863354037266, "no_speech_prob":
  0.1291946917772293}, {"id": 257, "seek": 43312, "start": 450.64, "end": 454.28000000000003,
  "text": " So imagine you''re searching for the perfect pair of red shoes.", "tokens":
  [51240, 407, 3811, 291, 434, 10808, 337, 264, 2176, 6119, 295, 2182, 6654, 13, 51422],
  "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 258, "seek": 43312, "start": 454.28000000000003,
  "end": 455.28000000000003, "text": " Okay.", "tokens": [51422, 1033, 13, 51472],
  "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio": 1.7701863354037266,
  "no_speech_prob": 0.1291946917772293}, {"id": 259, "seek": 43312, "start": 455.28000000000003,
  "end": 456.28000000000003, "text": " I like shoes.", "tokens": [51472, 286, 411,
  6654, 13, 51522], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 260, "seek": 43312,
  "start": 456.28000000000003, "end": 458.84000000000003, "text": " But only after
  you''ve seen a picture of the outfit you want them to match.", "tokens": [51522,
  583, 787, 934, 291, 600, 1612, 257, 3036, 295, 264, 11263, 291, 528, 552, 281, 2995,
  13, 51650], "temperature": 0.0, "avg_logprob": -0.1812015919203169, "compression_ratio":
  1.7701863354037266, "no_speech_prob": 0.1291946917772293}, {"id": 261, "seek": 43312,
  "start": 458.84000000000003, "end": 459.84000000000003, "text": " Oh, I see.", "tokens":
  [51650, 876, 11, 286, 536, 13, 51700], "temperature": 0.0, "avg_logprob": -0.1812015919203169,
  "compression_ratio": 1.7701863354037266, "no_speech_prob": 0.1291946917772293},
  {"id": 262, "seek": 43312, "start": 459.84000000000003, "end": 461.68, "text": "
  So like the context of the search changes.", "tokens": [51700, 407, 411, 264, 4319,
  295, 264, 3164, 2962, 13, 51792], "temperature": 0.0, "avg_logprob": -0.1812015919203169,
  "compression_ratio": 1.7701863354037266, "no_speech_prob": 0.1291946917772293},
  {"id": 263, "seek": 43312, "start": 461.68, "end": 462.68, "text": " Exactly.",
  "tokens": [51792, 7587, 13, 51842], "temperature": 0.0, "avg_logprob": -0.1812015919203169,
  "compression_ratio": 1.7701863354037266, "no_speech_prob": 0.1291946917772293},
  {"id": 264, "seek": 46268, "start": 462.72, "end": 464.16, "text": " And then you
  see something you see later on.", "tokens": [50366, 400, 550, 291, 536, 746, 291,
  536, 1780, 322, 13, 50438], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 265, "seek": 46268, "start": 464.16, "end": 465.96, "text": " That''s where
  late interaction models come in.", "tokens": [50438, 663, 311, 689, 3469, 9285,
  5245, 808, 294, 13, 50528], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 266, "seek": 46268, "start": 465.96, "end": 466.96, "text": " Okay.", "tokens":
  [50528, 1033, 13, 50578], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 267, "seek": 46268, "start": 466.96, "end": 471.16, "text": " Allowing you
  to refine your search based on context that''s only available later in the", "tokens":
  [50578, 1057, 9637, 291, 281, 33906, 428, 3164, 2361, 322, 4319, 300, 311, 787,
  2435, 1780, 294, 264, 50788], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 268, "seek": 46268, "start": 471.16, "end": 472.16, "text": " process.",
  "tokens": [50788, 1399, 13, 50838], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 269, "seek": 46268, "start": 472.16, "end": 474.6, "text": " So it''s like
  a more dynamic way of searching.", "tokens": [50838, 407, 309, 311, 411, 257, 544,
  8546, 636, 295, 10808, 13, 50960], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 270, "seek": 46268, "start": 474.6, "end": 476.0, "text": " It is a more
  dynamic way of searching.", "tokens": [50960, 467, 307, 257, 544, 8546, 636, 295,
  10808, 13, 51030], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 271, "seek":
  46268, "start": 476.0, "end": 477.0, "text": " Interesting.", "tokens": [51030,
  14711, 13, 51080], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 272, "seek":
  46268, "start": 477.0, "end": 479.36, "text": " And it requires a different level
  of database support.", "tokens": [51080, 400, 309, 7029, 257, 819, 1496, 295, 8149,
  1406, 13, 51198], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 273, "seek":
  46268, "start": 479.36, "end": 480.36, "text": " I bet.", "tokens": [51198, 286,
  778, 13, 51248], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 274, "seek":
  46268, "start": 480.36, "end": 485.4, "text": " And Dmitry points to QDrent or Vespa
  as potential solutions.", "tokens": [51248, 400, 413, 3508, 627, 2793, 281, 1249,
  35, 1753, 420, 691, 279, 4306, 382, 3995, 6547, 13, 51500], "temperature": 0.0,
  "avg_logprob": -0.24896220288245507, "compression_ratio": 1.7896440129449838, "no_speech_prob":
  0.057629648596048355}, {"id": 275, "seek": 46268, "start": 485.4, "end": 486.4,
  "text": " Okay.", "tokens": [51500, 1033, 13, 51550], "temperature": 0.0, "avg_logprob":
  -0.24896220288245507, "compression_ratio": 1.7896440129449838, "no_speech_prob":
  0.057629648596048355}, {"id": 276, "seek": 46268, "start": 486.4, "end": 488.6,
  "text": " So they can handle those late interactions.", "tokens": [51550, 407, 436,
  393, 4813, 729, 3469, 13280, 13, 51660], "temperature": 0.0, "avg_logprob": -0.24896220288245507,
  "compression_ratio": 1.7896440129449838, "no_speech_prob": 0.057629648596048355},
  {"id": 277, "seek": 46268, "start": 488.6, "end": 490.72, "text": " Because they
  offer that support natively.", "tokens": [51660, 1436, 436, 2626, 300, 1406, 8470,
  356, 13, 51766], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 278, "seek":
  46268, "start": 490.72, "end": 492.24, "text": " So you don''t have to hack it together
  yourself.", "tokens": [51766, 407, 291, 500, 380, 362, 281, 10339, 309, 1214, 1803,
  13, 51842], "temperature": 0.0, "avg_logprob": -0.24896220288245507, "compression_ratio":
  1.7896440129449838, "no_speech_prob": 0.057629648596048355}, {"id": 279, "seek":
  49224, "start": 492.28000000000003, "end": 493.28000000000003, "text": " Exactly.",
  "tokens": [50366, 7587, 13, 50416], "temperature": 0.0, "avg_logprob": -0.19433695475260418,
  "compression_ratio": 1.5472312703583062, "no_speech_prob": 0.002053606091067195},
  {"id": 280, "seek": 49224, "start": 493.28000000000003, "end": 494.28000000000003,
  "text": " That''s good to know.", "tokens": [50416, 663, 311, 665, 281, 458, 13,
  50466], "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio":
  1.5472312703583062, "no_speech_prob": 0.002053606091067195}, {"id": 281, "seek":
  49224, "start": 494.28000000000003, "end": 500.32, "text": " So choosing a database
  that can handle those complexities is critical for performance and", "tokens": [50466,
  407, 10875, 257, 8149, 300, 393, 4813, 729, 48705, 307, 4924, 337, 3389, 293, 50768],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 282, "seek": 49224, "start": 500.32,
  "end": 501.32, "text": " efficiency.", "tokens": [50768, 10493, 13, 50818], "temperature":
  0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 283, "seek": 49224, "start": 501.32,
  "end": 503.72, "text": " You don''t want your search to be slow and clunky.", "tokens":
  [50818, 509, 500, 380, 528, 428, 3164, 281, 312, 2964, 293, 596, 25837, 13, 50938],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 284, "seek": 49224, "start": 503.72,
  "end": 505.92, "text": " Especially if you''re dealing with a lot of data.", "tokens":
  [50938, 8545, 498, 291, 434, 6260, 365, 257, 688, 295, 1412, 13, 51048], "temperature":
  0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 285, "seek": 49224, "start": 505.92,
  "end": 506.92, "text": " Right.", "tokens": [51048, 1779, 13, 51098], "temperature":
  0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 286, "seek": 49224, "start": 506.92,
  "end": 508.72, "text": " Or if you need those results in real time.", "tokens":
  [51098, 1610, 498, 291, 643, 729, 3542, 294, 957, 565, 13, 51188], "temperature":
  0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 287, "seek": 49224, "start": 508.72,
  "end": 509.92, "text": " But it doesn''t stop there.", "tokens": [51188, 583, 309,
  1177, 380, 1590, 456, 13, 51248], "temperature": 0.0, "avg_logprob": -0.19433695475260418,
  "compression_ratio": 1.5472312703583062, "no_speech_prob": 0.002053606091067195},
  {"id": 288, "seek": 49224, "start": 509.92, "end": 510.92, "text": " There''s more.",
  "tokens": [51248, 821, 311, 544, 13, 51298], "temperature": 0.0, "avg_logprob":
  -0.19433695475260418, "compression_ratio": 1.5472312703583062, "no_speech_prob":
  0.002053606091067195}, {"id": 289, "seek": 49224, "start": 510.92, "end": 513.5600000000001,
  "text": " The next step into Dmitry''s roadmap is super important.", "tokens": [51298,
  440, 958, 1823, 666, 413, 3508, 627, 311, 35738, 307, 1687, 1021, 13, 51430], "temperature":
  0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 290, "seek": 49224, "start": 513.5600000000001,
  "end": 514.5600000000001, "text": " Okay.", "tokens": [51430, 1033, 13, 51480],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 291, "seek": 49224, "start": 514.5600000000001,
  "end": 515.5600000000001, "text": " Hit me.", "tokens": [51480, 9217, 385, 13, 51530],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 292, "seek": 49224, "start": 515.5600000000001,
  "end": 516.5600000000001, "text": " Considering latency.", "tokens": [51530, 33854,
  27043, 13, 51580], "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio":
  1.5472312703583062, "no_speech_prob": 0.002053606091067195}, {"id": 293, "seek":
  49224, "start": 516.5600000000001, "end": 517.5600000000001, "text": " Latency,
  okay.", "tokens": [51580, 7354, 3020, 11, 1392, 13, 51630], "temperature": 0.0,
  "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062, "no_speech_prob":
  0.002053606091067195}, {"id": 294, "seek": 49224, "start": 517.5600000000001, "end":
  518.5600000000001, "text": " And those query per second abans?", "tokens": [51630,
  400, 729, 14581, 680, 1150, 410, 599, 30, 51680], "temperature": 0.0, "avg_logprob":
  -0.19433695475260418, "compression_ratio": 1.5472312703583062, "no_speech_prob":
  0.002053606091067195}, {"id": 295, "seek": 49224, "start": 518.5600000000001, "end":
  519.5600000000001, "text": " Oh, yes.", "tokens": [51680, 876, 11, 2086, 13, 51730],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 296, "seek": 49224, "start": 519.5600000000001,
  "end": 520.5600000000001, "text": " QPS.", "tokens": [51730, 1249, 6273, 13, 51780],
  "temperature": 0.0, "avg_logprob": -0.19433695475260418, "compression_ratio": 1.5472312703583062,
  "no_speech_prob": 0.002053606091067195}, {"id": 297, "seek": 52056, "start": 520.64,
  "end": 522.4799999999999, "text": " Can make or break your application?", "tokens":
  [50368, 1664, 652, 420, 1821, 428, 3861, 30, 50460], "temperature": 0.0, "avg_logprob":
  -0.1773903483436221, "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 298, "seek": 52056, "start": 522.4799999999999, "end": 523.3199999999999,
  "text": " You''re telling me.", "tokens": [50460, 509, 434, 3585, 385, 13, 50502],
  "temperature": 0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 299, "seek": 52056, "start": 523.3199999999999,
  "end": 524.8, "text": " If your database is slow.", "tokens": [50502, 759, 428,
  8149, 307, 2964, 13, 50576], "temperature": 0.0, "avg_logprob": -0.1773903483436221,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 300, "seek": 52056, "start": 524.8, "end": 525.8, "text": " Yeah.", "tokens":
  [50576, 865, 13, 50626], "temperature": 0.0, "avg_logprob": -0.1773903483436221,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 301, "seek": 52056, "start": 525.8, "end": 527.4799999999999, "text": " Or
  it can''t handle the volume of queries.", "tokens": [50626, 1610, 309, 393, 380,
  4813, 264, 5523, 295, 24109, 13, 50710], "temperature": 0.0, "avg_logprob": -0.1773903483436221,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 302, "seek": 52056, "start": 527.4799999999999, "end": 529.16, "text": "
  It''s going to be a bad experience for the user.", "tokens": [50710, 467, 311, 516,
  281, 312, 257, 1578, 1752, 337, 264, 4195, 13, 50794], "temperature": 0.0, "avg_logprob":
  -0.1773903483436221, "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 303, "seek": 52056, "start": 529.16, "end": 530.16, "text": " It''s going
  to be a disaster.", "tokens": [50794, 467, 311, 516, 281, 312, 257, 11293, 13, 50844],
  "temperature": 0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 304, "seek": 52056, "start": 530.16,
  "end": 532.0, "text": " So you''ve got to think about those things up front.", "tokens":
  [50844, 407, 291, 600, 658, 281, 519, 466, 729, 721, 493, 1868, 13, 50936], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 305, "seek": 52056, "start": 532.0,
  "end": 533.0, "text": " Absolutely.", "tokens": [50936, 7021, 13, 50986], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 306, "seek": 52056, "start": 533.0,
  "end": 535.3199999999999, "text": " And choose a database that can handle the load.",
  "tokens": [50986, 400, 2826, 257, 8149, 300, 393, 4813, 264, 3677, 13, 51102], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 307, "seek": 52056, "start": 535.3199999999999,
  "end": 537.5999999999999, "text": " If high performance is the name of the game.",
  "tokens": [51102, 759, 1090, 3389, 307, 264, 1315, 295, 264, 1216, 13, 51216], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 308, "seek": 52056, "start": 537.5999999999999,
  "end": 538.5999999999999, "text": " Yeah.", "tokens": [51216, 865, 13, 51266], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 309, "seek": 52056, "start": 538.5999999999999,
  "end": 544.4, "text": " You''ll want to explore solutions like GSI, APU, Vespa,
  or hyperspace.", "tokens": [51266, 509, 603, 528, 281, 6839, 6547, 411, 460, 20262,
  11, 5372, 52, 11, 691, 279, 4306, 11, 420, 7420, 433, 17940, 13, 51556], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 310, "seek": 52056, "start": 544.4,
  "end": 545.4, "text": " Got it.", "tokens": [51556, 5803, 309, 13, 51606], "temperature":
  0.0, "avg_logprob": -0.1773903483436221, "compression_ratio": 1.631578947368421,
  "no_speech_prob": 0.02104545198380947}, {"id": 311, "seek": 52056, "start": 545.4,
  "end": 548.2399999999999, "text": " In fact, Dmitry even shared an anecdote about
  a CTO.", "tokens": [51606, 682, 1186, 11, 413, 3508, 627, 754, 5507, 364, 49845,
  466, 257, 383, 15427, 13, 51748], "temperature": 0.0, "avg_logprob": -0.1773903483436221,
  "compression_ratio": 1.631578947368421, "no_speech_prob": 0.02104545198380947},
  {"id": 312, "seek": 52056, "start": 548.2399999999999, "end": 549.88, "text": "
  Oh, I love a good anecdote.", "tokens": [51748, 876, 11, 286, 959, 257, 665, 49845,
  13, 51830], "temperature": 0.0, "avg_logprob": -0.1773903483436221, "compression_ratio":
  1.631578947368421, "no_speech_prob": 0.02104545198380947}, {"id": 313, "seek": 54988,
  "start": 549.88, "end": 555.8, "text": " You''ll confess that no open source vector
  database could handle their extreme workload.", "tokens": [50364, 509, 603, 19367,
  300, 572, 1269, 4009, 8062, 8149, 727, 4813, 641, 8084, 20139, 13, 50660], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 314, "seek": 54988, "start": 555.8,
  "end": 556.8, "text": " Wow.", "tokens": [50660, 3153, 13, 50710], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 315, "seek": 54988, "start": 556.8,
  "end": 558.48, "text": " So they had to go with a commercial solution.", "tokens":
  [50710, 407, 436, 632, 281, 352, 365, 257, 6841, 3827, 13, 50794], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 316, "seek": 54988, "start": 558.48,
  "end": 559.68, "text": " They''d find something else.", "tokens": [50794, 814, 1116,
  915, 746, 1646, 13, 50854], "temperature": 0.0, "avg_logprob": -0.23072041810013866,
  "compression_ratio": 1.612794612794613, "no_speech_prob": 0.07140126824378967},
  {"id": 317, "seek": 54988, "start": 559.68, "end": 560.68, "text": " That''s interesting.",
  "tokens": [50854, 663, 311, 1880, 13, 50904], "temperature": 0.0, "avg_logprob":
  -0.23072041810013866, "compression_ratio": 1.612794612794613, "no_speech_prob":
  0.07140126824378967}, {"id": 318, "seek": 54988, "start": 560.68, "end": 562.48,
  "text": " Choosing wisely is essential.", "tokens": [50904, 12366, 6110, 37632,
  307, 7115, 13, 50994], "temperature": 0.0, "avg_logprob": -0.23072041810013866,
  "compression_ratio": 1.612794612794613, "no_speech_prob": 0.07140126824378967},
  {"id": 319, "seek": 54988, "start": 562.48, "end": 564.64, "text": " You can''t
  just pick the first one you see.", "tokens": [50994, 509, 393, 380, 445, 1888, 264,
  700, 472, 291, 536, 13, 51102], "temperature": 0.0, "avg_logprob": -0.23072041810013866,
  "compression_ratio": 1.612794612794613, "no_speech_prob": 0.07140126824378967},
  {"id": 320, "seek": 54988, "start": 564.64, "end": 565.64, "text": " No.", "tokens":
  [51102, 883, 13, 51152], "temperature": 0.0, "avg_logprob": -0.23072041810013866,
  "compression_ratio": 1.612794612794613, "no_speech_prob": 0.07140126824378967},
  {"id": 321, "seek": 54988, "start": 565.64, "end": 566.64, "text": " You got to
  your homework.", "tokens": [51152, 509, 658, 281, 428, 14578, 13, 51202], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 322, "seek": 54988, "start": 566.64,
  "end": 568.12, "text": " And think about your long term needs.", "tokens": [51202,
  400, 519, 466, 428, 938, 1433, 2203, 13, 51276], "temperature": 0.0, "avg_logprob":
  -0.23072041810013866, "compression_ratio": 1.612794612794613, "no_speech_prob":
  0.07140126824378967}, {"id": 323, "seek": 54988, "start": 568.12, "end": 571.84,
  "text": " So the takeaway here is you need to think strategically.", "tokens": [51276,
  407, 264, 30681, 510, 307, 291, 643, 281, 519, 38061, 13, 51462], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 324, "seek": 54988, "start": 571.84,
  "end": 572.84, "text": " Yep.", "tokens": [51462, 7010, 13, 51512], "temperature":
  0.0, "avg_logprob": -0.23072041810013866, "compression_ratio": 1.612794612794613,
  "no_speech_prob": 0.07140126824378967}, {"id": 325, "seek": 54988, "start": 572.84,
  "end": 578.12, "text": " Do you invest the engineering time to set up and maintain
  an open source database?", "tokens": [51512, 1144, 291, 1963, 264, 7043, 565, 281,
  992, 493, 293, 6909, 364, 1269, 4009, 8149, 30, 51776], "temperature": 0.0, "avg_logprob":
  -0.23072041810013866, "compression_ratio": 1.612794612794613, "no_speech_prob":
  0.07140126824378967}, {"id": 326, "seek": 54988, "start": 578.12, "end": 579.12,
  "text": " Right.", "tokens": [51776, 1779, 13, 51826], "temperature": 0.0, "avg_logprob":
  -0.23072041810013866, "compression_ratio": 1.612794612794613, "no_speech_prob":
  0.07140126824378967}, {"id": 327, "seek": 57912, "start": 579.12, "end": 584.24,
  "text": " Or do you go with the convenience and potentially higher costs of a cloud
  solution?", "tokens": [50364, 1610, 360, 291, 352, 365, 264, 19283, 293, 7263, 2946,
  5497, 295, 257, 4588, 3827, 30, 50620], "temperature": 0.0, "avg_logprob": -0.22903351022415802,
  "compression_ratio": 1.586466165413534, "no_speech_prob": 0.0004534748732112348},
  {"id": 328, "seek": 57912, "start": 584.24, "end": 585.24, "text": " Right.", "tokens":
  [50620, 1779, 13, 50670], "temperature": 0.0, "avg_logprob": -0.22903351022415802,
  "compression_ratio": 1.586466165413534, "no_speech_prob": 0.0004534748732112348},
  {"id": 329, "seek": 57912, "start": 585.24, "end": 586.24, "text": " It''s a classic
  trade off.", "tokens": [50670, 467, 311, 257, 7230, 4923, 766, 13, 50720], "temperature":
  0.0, "avg_logprob": -0.22903351022415802, "compression_ratio": 1.586466165413534,
  "no_speech_prob": 0.0004534748732112348}, {"id": 330, "seek": 57912, "start": 586.24,
  "end": 587.24, "text": " There''s no right or wrong answer.", "tokens": [50720,
  821, 311, 572, 558, 420, 2085, 1867, 13, 50770], "temperature": 0.0, "avg_logprob":
  -0.22903351022415802, "compression_ratio": 1.586466165413534, "no_speech_prob":
  0.0004534748732112348}, {"id": 331, "seek": 57912, "start": 587.24, "end": 588.24,
  "text": " It depends on your situation.", "tokens": [50770, 467, 5946, 322, 428,
  2590, 13, 50820], "temperature": 0.0, "avg_logprob": -0.22903351022415802, "compression_ratio":
  1.586466165413534, "no_speech_prob": 0.0004534748732112348}, {"id": 332, "seek":
  57912, "start": 588.24, "end": 592.84, "text": " It''s all about finding the balance
  that works best for your specific situation.", "tokens": [50820, 467, 311, 439,
  466, 5006, 264, 4772, 300, 1985, 1151, 337, 428, 2685, 2590, 13, 51050], "temperature":
  0.0, "avg_logprob": -0.22903351022415802, "compression_ratio": 1.586466165413534,
  "no_speech_prob": 0.0004534748732112348}, {"id": 333, "seek": 57912, "start": 592.84,
  "end": 594.32, "text": " Absolutely.", "tokens": [51050, 7021, 13, 51124], "temperature":
  0.0, "avg_logprob": -0.22903351022415802, "compression_ratio": 1.586466165413534,
  "no_speech_prob": 0.0004534748732112348}, {"id": 334, "seek": 57912, "start": 594.32,
  "end": 599.5600000000001, "text": " And there are a lot of great cloud and API based
  options out there.", "tokens": [51124, 400, 456, 366, 257, 688, 295, 869, 4588,
  293, 9362, 2361, 3956, 484, 456, 13, 51386], "temperature": 0.0, "avg_logprob":
  -0.22903351022415802, "compression_ratio": 1.586466165413534, "no_speech_prob":
  0.0004534748732112348}, {"id": 335, "seek": 57912, "start": 599.5600000000001, "end":
  600.5600000000001, "text": " Like what?", "tokens": [51386, 1743, 437, 30, 51436],
  "temperature": 0.0, "avg_logprob": -0.22903351022415802, "compression_ratio": 1.586466165413534,
  "no_speech_prob": 0.0004534748732112348}, {"id": 336, "seek": 57912, "start": 600.5600000000001,
  "end": 607.76, "text": " Like Cosmos DB, Vertex AI, Pine Cone Cloud, Weeveate Cloud,
  and other.", "tokens": [51436, 1743, 15855, 3415, 26754, 11, 21044, 3121, 7318,
  11, 33531, 383, 546, 8061, 11, 492, 68, 303, 473, 8061, 11, 293, 661, 13, 51796],
  "temperature": 0.0, "avg_logprob": -0.22903351022415802, "compression_ratio": 1.586466165413534,
  "no_speech_prob": 0.0004534748732112348}, {"id": 337, "seek": 60776, "start": 607.76,
  "end": 609.4399999999999, "text": " But there''s no shortage of options.", "tokens":
  [50364, 583, 456, 311, 572, 24708, 295, 3956, 13, 50448], "temperature": 0.0, "avg_logprob":
  -0.21822113037109375, "compression_ratio": 1.6396103896103895, "no_speech_prob":
  0.23578330874443054}, {"id": 338, "seek": 60776, "start": 609.4399999999999, "end":
  610.68, "text": " There''s a lot to choose from.", "tokens": [50448, 821, 311, 257,
  688, 281, 2826, 490, 13, 50510], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 339, "seek": 60776, "start": 610.68, "end": 612.0, "text": " It''s a good
  problem to have, right?", "tokens": [50510, 467, 311, 257, 665, 1154, 281, 362,
  11, 558, 30, 50576], "temperature": 0.0, "avg_logprob": -0.21822113037109375, "compression_ratio":
  1.6396103896103895, "no_speech_prob": 0.23578330874443054}, {"id": 340, "seek":
  60776, "start": 612.0, "end": 613.2, "text": " It is a good problem to have.", "tokens":
  [50576, 467, 307, 257, 665, 1154, 281, 362, 13, 50636], "temperature": 0.0, "avg_logprob":
  -0.21822113037109375, "compression_ratio": 1.6396103896103895, "no_speech_prob":
  0.23578330874443054}, {"id": 341, "seek": 60776, "start": 613.2, "end": 615.4, "text":
  " Better than having no options at all.", "tokens": [50636, 15753, 813, 1419, 572,
  3956, 412, 439, 13, 50746], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 342, "seek": 60776, "start": 615.4, "end": 617.24, "text": " And we love
  hearing from our community.", "tokens": [50746, 400, 321, 959, 4763, 490, 527, 1768,
  13, 50838], "temperature": 0.0, "avg_logprob": -0.21822113037109375, "compression_ratio":
  1.6396103896103895, "no_speech_prob": 0.23578330874443054}, {"id": 343, "seek":
  60776, "start": 617.24, "end": 619.48, "text": " Oh yes, our listeners are the best.",
  "tokens": [50838, 876, 2086, 11, 527, 23274, 366, 264, 1151, 13, 50950], "temperature":
  0.0, "avg_logprob": -0.21822113037109375, "compression_ratio": 1.6396103896103895,
  "no_speech_prob": 0.23578330874443054}, {"id": 344, "seek": 60776, "start": 619.48,
  "end": 624.4399999999999, "text": " One reader, Matt Collins, suggested exploring
  extensions like PG Vector.", "tokens": [50950, 1485, 15149, 11, 7397, 27973, 11,
  10945, 12736, 25129, 411, 40975, 691, 20814, 13, 51198], "temperature": 0.0, "avg_logprob":
  -0.21822113037109375, "compression_ratio": 1.6396103896103895, "no_speech_prob":
  0.23578330874443054}, {"id": 345, "seek": 60776, "start": 624.4399999999999, "end":
  625.4399999999999, "text": " Did you vector?", "tokens": [51198, 2589, 291, 8062,
  30, 51248], "temperature": 0.0, "avg_logprob": -0.21822113037109375, "compression_ratio":
  1.6396103896103895, "no_speech_prob": 0.23578330874443054}, {"id": 346, "seek":
  60776, "start": 625.4399999999999, "end": 626.4399999999999, "text": " Okay.", "tokens":
  [51248, 1033, 13, 51298], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 347, "seek": 60776, "start": 626.4399999999999, "end": 628.3199999999999,
  "text": " Which adds vector search to Postgresql.", "tokens": [51298, 3013, 10860,
  8062, 3164, 281, 10223, 45189, 80, 75, 13, 51392], "temperature": 0.0, "avg_logprob":
  -0.21822113037109375, "compression_ratio": 1.6396103896103895, "no_speech_prob":
  0.23578330874443054}, {"id": 348, "seek": 60776, "start": 628.3199999999999, "end":
  632.12, "text": " Oh, so you can just add it onto your existing Postgres database.",
  "tokens": [51392, 876, 11, 370, 291, 393, 445, 909, 309, 3911, 428, 6741, 10223,
  45189, 8149, 13, 51582], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 349, "seek": 60776, "start": 632.12, "end": 633.12, "text": " Exactly.",
  "tokens": [51582, 7587, 13, 51632], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 350, "seek": 60776, "start": 633.12, "end": 634.12, "text": " That''s pretty
  cool.", "tokens": [51632, 663, 311, 1238, 1627, 13, 51682], "temperature": 0.0,
  "avg_logprob": -0.21822113037109375, "compression_ratio": 1.6396103896103895, "no_speech_prob":
  0.23578330874443054}, {"id": 351, "seek": 60776, "start": 634.12, "end": 635.12,
  "text": " It''s a really clever solution.", "tokens": [51682, 467, 311, 257, 534,
  13494, 3827, 13, 51732], "temperature": 0.0, "avg_logprob": -0.21822113037109375,
  "compression_ratio": 1.6396103896103895, "no_speech_prob": 0.23578330874443054},
  {"id": 352, "seek": 63512, "start": 635.12, "end": 637.88, "text": " You have to
  rip and replace your whole infrastructure.", "tokens": [50364, 509, 362, 281, 12782,
  293, 7406, 428, 1379, 6896, 13, 50502], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 353, "seek": 63512, "start": 637.88, "end": 642.88, "text": " And it speaks
  to the constantly evolving nature of the vector database landscape.", "tokens":
  [50502, 400, 309, 10789, 281, 264, 6460, 21085, 3687, 295, 264, 8062, 8149, 9661,
  13, 50752], "temperature": 0.0, "avg_logprob": -0.2464251072286702, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.5175851583480835}, {"id": 354, "seek": 63512,
  "start": 642.88, "end": 643.96, "text": " It''s a fast moving field.", "tokens":
  [50752, 467, 311, 257, 2370, 2684, 2519, 13, 50806], "temperature": 0.0, "avg_logprob":
  -0.2464251072286702, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.5175851583480835}, {"id": 355, "seek": 63512, "start": 643.96, "end": 645.68,
  "text": " There''s always something new happening.", "tokens": [50806, 821, 311,
  1009, 746, 777, 2737, 13, 50892], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 356, "seek": 63512, "start": 645.68, "end": 647.92, "text": " You''ve been
  in new solutions emerging.", "tokens": [50892, 509, 600, 668, 294, 777, 6547, 14989,
  13, 51004], "temperature": 0.0, "avg_logprob": -0.2464251072286702, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.5175851583480835}, {"id": 357, "seek": 63512,
  "start": 647.92, "end": 648.92, "text": " Speaking of evolution.", "tokens": [51004,
  13069, 295, 9303, 13, 51054], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 358, "seek": 63512, "start": 648.92, "end": 650.52, "text": " Oh, this is
  where it gets really interesting.", "tokens": [51054, 876, 11, 341, 307, 689, 309,
  2170, 534, 1880, 13, 51134], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 359, "seek": 63512, "start": 650.52, "end": 652.76, "text": " Dimitri paints
  a fascinating picture of the future.", "tokens": [51134, 20975, 270, 470, 28076,
  257, 10343, 3036, 295, 264, 2027, 13, 51246], "temperature": 0.0, "avg_logprob":
  -0.2464251072286702, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.5175851583480835}, {"id": 360, "seek": 63512, "start": 652.76, "end": 654.44,
  "text": " I can''t wait to hear this.", "tokens": [51246, 286, 393, 380, 1699, 281,
  1568, 341, 13, 51330], "temperature": 0.0, "avg_logprob": -0.2464251072286702, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.5175851583480835}, {"id": 361, "seek": 63512,
  "start": 654.44, "end": 658.5600000000001, "text": " He believes the future lies
  in what he calls neural search frameworks.", "tokens": [51330, 634, 12307, 264,
  2027, 9134, 294, 437, 415, 5498, 18161, 3164, 29834, 13, 51536], "temperature":
  0.0, "avg_logprob": -0.2464251072286702, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.5175851583480835}, {"id": 362, "seek": 63512, "start": 658.5600000000001,
  "end": 659.72, "text": " Oh, wow.", "tokens": [51536, 876, 11, 6076, 13, 51594],
  "temperature": 0.0, "avg_logprob": -0.2464251072286702, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.5175851583480835}, {"id": 363, "seek": 63512, "start": 659.72,
  "end": 664.08, "text": " These frameworks could revolutionize how we build AI-powered
  applications.", "tokens": [51594, 1981, 29834, 727, 8894, 1125, 577, 321, 1322,
  7318, 12, 27178, 5821, 13, 51812], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 364, "seek": 63512, "start": 664.08, "end": 665.08, "text": " Okay.", "tokens":
  [51812, 1033, 13, 51862], "temperature": 0.0, "avg_logprob": -0.2464251072286702,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.5175851583480835},
  {"id": 365, "seek": 66508, "start": 665.08, "end": 669.24, "text": " And then we
  have a system that streamlines the entire process from data modeling and embedding",
  "tokens": [50364, 400, 550, 321, 362, 257, 1185, 300, 4309, 11045, 264, 2302, 1399,
  490, 1412, 15983, 293, 12240, 3584, 50572], "temperature": 0.0, "avg_logprob": -0.25581640355727253,
  "compression_ratio": 1.67595818815331, "no_speech_prob": 0.0053773801773786545},
  {"id": 366, "seek": 66508, "start": 669.24, "end": 672.72, "text": " selection to
  evaluation and scaling.", "tokens": [50572, 9450, 281, 13344, 293, 21589, 13, 50746],
  "temperature": 0.0, "avg_logprob": -0.25581640355727253, "compression_ratio": 1.67595818815331,
  "no_speech_prob": 0.0053773801773786545}, {"id": 367, "seek": 66508, "start": 672.72,
  "end": 676.76, "text": " So instead of wrestling with the complexities of choosing
  and integrating all the different", "tokens": [50746, 407, 2602, 295, 19274, 365,
  264, 48705, 295, 10875, 293, 26889, 439, 264, 819, 50948], "temperature": 0.0, "avg_logprob":
  -0.25581640355727253, "compression_ratio": 1.67595818815331, "no_speech_prob": 0.0053773801773786545},
  {"id": 368, "seek": 66508, "start": 676.76, "end": 682.6800000000001, "text": "
  components, it would be like having an intelligent assistant guiding you through
  building a search", "tokens": [50948, 6677, 11, 309, 576, 312, 411, 1419, 364, 13232,
  10994, 25061, 291, 807, 2390, 257, 3164, 51244], "temperature": 0.0, "avg_logprob":
  -0.25581640355727253, "compression_ratio": 1.67595818815331, "no_speech_prob": 0.0053773801773786545},
  {"id": 369, "seek": 66508, "start": 682.6800000000001, "end": 686.5600000000001,
  "text": " application no matter what database technology you''re using.", "tokens":
  [51244, 3861, 572, 1871, 437, 8149, 2899, 291, 434, 1228, 13, 51438], "temperature":
  0.0, "avg_logprob": -0.25581640355727253, "compression_ratio": 1.67595818815331,
  "no_speech_prob": 0.0053773801773786545}, {"id": 370, "seek": 66508, "start": 686.5600000000001,
  "end": 687.5600000000001, "text": " Exactly.", "tokens": [51438, 7587, 13, 51488],
  "temperature": 0.0, "avg_logprob": -0.25581640355727253, "compression_ratio": 1.67595818815331,
  "no_speech_prob": 0.0053773801773786545}, {"id": 371, "seek": 66508, "start": 687.5600000000001,
  "end": 691.1600000000001, "text": " And this vision ties in nicely with the concept
  of compound AI systems.", "tokens": [51488, 400, 341, 5201, 14039, 294, 9594, 365,
  264, 3410, 295, 14154, 7318, 3652, 13, 51668], "temperature": 0.0, "avg_logprob":
  -0.25581640355727253, "compression_ratio": 1.67595818815331, "no_speech_prob": 0.0053773801773786545},
  {"id": 372, "seek": 66508, "start": 691.1600000000001, "end": 692.1600000000001,
  "text": " Oh, interesting.", "tokens": [51668, 876, 11, 1880, 13, 51718], "temperature":
  0.0, "avg_logprob": -0.25581640355727253, "compression_ratio": 1.67595818815331,
  "no_speech_prob": 0.0053773801773786545}, {"id": 373, "seek": 69216, "start": 692.16,
  "end": 698.28, "text": " So where LLMs vector databases and other AI components
  work together like a well coordinated", "tokens": [50364, 407, 689, 441, 43, 26386,
  8062, 22380, 293, 661, 7318, 6677, 589, 1214, 411, 257, 731, 29591, 50670], "temperature":
  0.0, "avg_logprob": -0.1728930188040448, "compression_ratio": 1.671280276816609,
  "no_speech_prob": 0.10033581405878067}, {"id": 374, "seek": 69216, "start": 698.28,
  "end": 699.28, "text": " orchestra.", "tokens": [50670, 25280, 13, 50720], "temperature":
  0.0, "avg_logprob": -0.1728930188040448, "compression_ratio": 1.671280276816609,
  "no_speech_prob": 0.10033581405878067}, {"id": 375, "seek": 69216, "start": 699.28,
  "end": 703.48, "text": " So instead of focusing on the individual instruments, you''re
  conducting the entire symphony.", "tokens": [50720, 407, 2602, 295, 8416, 322, 264,
  2609, 12190, 11, 291, 434, 21749, 264, 2302, 6697, 28616, 13, 50930], "temperature":
  0.0, "avg_logprob": -0.1728930188040448, "compression_ratio": 1.671280276816609,
  "no_speech_prob": 0.10033581405878067}, {"id": 376, "seek": 69216, "start": 703.48,
  "end": 704.48, "text": " Precisely.", "tokens": [50930, 48746, 736, 13, 50980],
  "temperature": 0.0, "avg_logprob": -0.1728930188040448, "compression_ratio": 1.671280276816609,
  "no_speech_prob": 0.10033581405878067}, {"id": 377, "seek": 69216, "start": 704.48,
  "end": 705.9599999999999, "text": " I love that analogy.", "tokens": [50980, 286,
  959, 300, 21663, 13, 51054], "temperature": 0.0, "avg_logprob": -0.1728930188040448,
  "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 378, "seek": 69216, "start": 705.9599999999999, "end": 709.8, "text": " Users
  can then focus on the task they''re trying to solve, rather than the technical nuts",
  "tokens": [51054, 47092, 393, 550, 1879, 322, 264, 5633, 436, 434, 1382, 281, 5039,
  11, 2831, 813, 264, 6191, 10483, 51246], "temperature": 0.0, "avg_logprob": -0.1728930188040448,
  "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 379, "seek": 69216, "start": 709.8, "end": 710.8, "text": " and bolts.",
  "tokens": [51246, 293, 18127, 13, 51296], "temperature": 0.0, "avg_logprob": -0.1728930188040448,
  "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 380, "seek": 69216, "start": 710.8, "end": 715.0799999999999, "text": " So
  it''s about abstracting away the complexity and empowering users to focus on the
  bigger", "tokens": [51296, 407, 309, 311, 466, 12649, 278, 1314, 264, 14024, 293,
  28261, 5022, 281, 1879, 322, 264, 3801, 51510], "temperature": 0.0, "avg_logprob":
  -0.1728930188040448, "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 381, "seek": 69216, "start": 715.0799999999999, "end": 716.0799999999999,
  "text": " picture.", "tokens": [51510, 3036, 13, 51560], "temperature": 0.0, "avg_logprob":
  -0.1728930188040448, "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 382, "seek": 69216, "start": 716.0799999999999, "end": 719.0, "text": " It''s
  about making AI more accessible and user friendly.", "tokens": [51560, 467, 311,
  466, 1455, 7318, 544, 9515, 293, 4195, 9208, 13, 51706], "temperature": 0.0, "avg_logprob":
  -0.1728930188040448, "compression_ratio": 1.671280276816609, "no_speech_prob": 0.10033581405878067},
  {"id": 383, "seek": 71900, "start": 719.0, "end": 722.24, "text": " It''s fascinating
  how this all connects to those funding announcements we talked about", "tokens":
  [50364, 467, 311, 10343, 577, 341, 439, 16967, 281, 729, 6137, 23785, 321, 2825,
  466, 50526], "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio":
  1.6269592476489028, "no_speech_prob": 0.005485461559146643}, {"id": 384, "seek":
  71900, "start": 722.24, "end": 723.24, "text": " earlier.", "tokens": [50526, 3071,
  13, 50576], "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio":
  1.6269592476489028, "no_speech_prob": 0.005485461559146643}, {"id": 385, "seek":
  71900, "start": 723.24, "end": 724.24, "text": " Right.", "tokens": [50576, 1779,
  13, 50626], "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio":
  1.6269592476489028, "no_speech_prob": 0.005485461559146643}, {"id": 386, "seek":
  71900, "start": 724.24, "end": 730.4, "text": " It seems like the industry might
  be moving towards a more unified approach to AI solutions.", "tokens": [50626, 467,
  2544, 411, 264, 3518, 1062, 312, 2684, 3030, 257, 544, 26787, 3109, 281, 7318, 6547,
  13, 50934], "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio":
  1.6269592476489028, "no_speech_prob": 0.005485461559146643}, {"id": 387, "seek":
  71900, "start": 730.4, "end": 732.16, "text": " That''s a keen observation.", "tokens":
  [50934, 663, 311, 257, 20297, 14816, 13, 51022], "temperature": 0.0, "avg_logprob":
  -0.1810559630393982, "compression_ratio": 1.6269592476489028, "no_speech_prob":
  0.005485461559146643}, {"id": 388, "seek": 71900, "start": 732.16, "end": 735.32,
  "text": " While individual components like vector databases are still important.",
  "tokens": [51022, 3987, 2609, 6677, 411, 8062, 22380, 366, 920, 1021, 13, 51180],
  "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio": 1.6269592476489028,
  "no_speech_prob": 0.005485461559146643}, {"id": 389, "seek": 71900, "start": 735.32,
  "end": 736.32, "text": " For sure.", "tokens": [51180, 1171, 988, 13, 51230], "temperature":
  0.0, "avg_logprob": -0.1810559630393982, "compression_ratio": 1.6269592476489028,
  "no_speech_prob": 0.005485461559146643}, {"id": 390, "seek": 71900, "start": 736.32,
  "end": 740.56, "text": " The future might be about how these pieces fit into a larger
  ecosystem.", "tokens": [51230, 440, 2027, 1062, 312, 466, 577, 613, 3755, 3318,
  666, 257, 4833, 11311, 13, 51442], "temperature": 0.0, "avg_logprob": -0.1810559630393982,
  "compression_ratio": 1.6269592476489028, "no_speech_prob": 0.005485461559146643},
  {"id": 391, "seek": 71900, "start": 740.56, "end": 743.16, "text": " Yeah, it''s
  all about the big picture.", "tokens": [51442, 865, 11, 309, 311, 439, 466, 264,
  955, 3036, 13, 51572], "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio":
  1.6269592476489028, "no_speech_prob": 0.005485461559146643}, {"id": 392, "seek":
  71900, "start": 743.16, "end": 745.8, "text": " This brings us to an interesting
  question for you, the listener.", "tokens": [51572, 639, 5607, 505, 281, 364, 1880,
  1168, 337, 291, 11, 264, 31569, 13, 51704], "temperature": 0.0, "avg_logprob": -0.1810559630393982,
  "compression_ratio": 1.6269592476489028, "no_speech_prob": 0.005485461559146643},
  {"id": 393, "seek": 71900, "start": 745.8, "end": 746.8, "text": " Oh, yes.", "tokens":
  [51704, 876, 11, 2086, 13, 51754], "temperature": 0.0, "avg_logprob": -0.1810559630393982,
  "compression_ratio": 1.6269592476489028, "no_speech_prob": 0.005485461559146643},
  {"id": 394, "seek": 71900, "start": 746.8, "end": 748.56, "text": " Let''s get our
  listeners involved.", "tokens": [51754, 961, 311, 483, 527, 23274, 3288, 13, 51842],
  "temperature": 0.0, "avg_logprob": -0.1810559630393982, "compression_ratio": 1.6269592476489028,
  "no_speech_prob": 0.005485461559146643}, {"id": 395, "seek": 74856, "start": 748.56,
  "end": 753.92, "text": " Do you see neural search frameworks as a complete paradigm
  shift?", "tokens": [50364, 1144, 291, 536, 18161, 3164, 29834, 382, 257, 3566, 24709,
  5513, 30, 50632], "temperature": 0.0, "avg_logprob": -0.199441650390625, "compression_ratio":
  1.5654952076677315, "no_speech_prob": 0.0009701931849122047}, {"id": 396, "seek":
  74856, "start": 753.92, "end": 759.28, "text": " Or will specialized vector databases
  continue to have a distinct role to play?", "tokens": [50632, 1610, 486, 19813,
  8062, 22380, 2354, 281, 362, 257, 10644, 3090, 281, 862, 30, 50900], "temperature":
  0.0, "avg_logprob": -0.199441650390625, "compression_ratio": 1.5654952076677315,
  "no_speech_prob": 0.0009701931849122047}, {"id": 397, "seek": 74856, "start": 759.28,
  "end": 760.8, "text": " It''s tough question.", "tokens": [50900, 467, 311, 4930,
  1168, 13, 50976], "temperature": 0.0, "avg_logprob": -0.199441650390625, "compression_ratio":
  1.5654952076677315, "no_speech_prob": 0.0009701931849122047}, {"id": 398, "seek":
  74856, "start": 760.8, "end": 762.0, "text": " It''s something to think about.",
  "tokens": [50976, 467, 311, 746, 281, 519, 466, 13, 51036], "temperature": 0.0,
  "avg_logprob": -0.199441650390625, "compression_ratio": 1.5654952076677315, "no_speech_prob":
  0.0009701931849122047}, {"id": 399, "seek": 74856, "start": 762.0, "end": 763.4799999999999,
  "text": " Let us know your thoughts in the comments.", "tokens": [51036, 961, 505,
  458, 428, 4598, 294, 264, 3053, 13, 51110], "temperature": 0.0, "avg_logprob": -0.199441650390625,
  "compression_ratio": 1.5654952076677315, "no_speech_prob": 0.0009701931849122047},
  {"id": 400, "seek": 74856, "start": 763.4799999999999, "end": 765.0, "text": " We''d
  love to hear from you.", "tokens": [51110, 492, 1116, 959, 281, 1568, 490, 291,
  13, 51186], "temperature": 0.0, "avg_logprob": -0.199441650390625, "compression_ratio":
  1.5654952076677315, "no_speech_prob": 0.0009701931849122047}, {"id": 401, "seek":
  74856, "start": 765.0, "end": 770.3599999999999, "text": " But before we get too
  caught up in the future, let''s take a step back and revisit one of Dmitry''s",
  "tokens": [51186, 583, 949, 321, 483, 886, 5415, 493, 294, 264, 2027, 11, 718, 311,
  747, 257, 1823, 646, 293, 32676, 472, 295, 413, 3508, 627, 311, 51454], "temperature":
  0.0, "avg_logprob": -0.199441650390625, "compression_ratio": 1.5654952076677315,
  "no_speech_prob": 0.0009701931849122047}, {"id": 402, "seek": 74856, "start": 770.3599999999999,
  "end": 776.04, "text": " key points about the impact of media coverage on perceptions
  of technology trends.", "tokens": [51454, 2141, 2793, 466, 264, 2712, 295, 3021,
  9645, 322, 35258, 295, 2899, 13892, 13, 51738], "temperature": 0.0, "avg_logprob":
  -0.199441650390625, "compression_ratio": 1.5654952076677315, "no_speech_prob": 0.0009701931849122047},
  {"id": 403, "seek": 74856, "start": 776.04, "end": 777.04, "text": " Right.", "tokens":
  [51738, 1779, 13, 51788], "temperature": 0.0, "avg_logprob": -0.199441650390625,
  "compression_ratio": 1.5654952076677315, "no_speech_prob": 0.0009701931849122047},
  {"id": 404, "seek": 74856, "start": 777.04, "end": 777.9599999999999, "text": "
  That was a really important point.", "tokens": [51788, 663, 390, 257, 534, 1021,
  935, 13, 51834], "temperature": 0.0, "avg_logprob": -0.199441650390625, "compression_ratio":
  1.5654952076677315, "no_speech_prob": 0.0009701931849122047}, {"id": 405, "seek":
  77796, "start": 777.96, "end": 782.52, "text": " It''s a crucial reminder to be
  discerning consumers of information, especially in a field", "tokens": [50364, 467,
  311, 257, 11462, 13548, 281, 312, 717, 1776, 773, 11883, 295, 1589, 11, 2318, 294,
  257, 2519, 50592], "temperature": 0.0, "avg_logprob": -0.15416003382483193, "compression_ratio":
  1.634441087613293, "no_speech_prob": 0.007103354204446077}, {"id": 406, "seek":
  77796, "start": 782.52, "end": 786.4000000000001, "text": " as dynamic as AI, where
  innovation is constant.", "tokens": [50592, 382, 8546, 382, 7318, 11, 689, 8504,
  307, 5754, 13, 50786], "temperature": 0.0, "avg_logprob": -0.15416003382483193,
  "compression_ratio": 1.634441087613293, "no_speech_prob": 0.007103354204446077},
  {"id": 407, "seek": 77796, "start": 786.4000000000001, "end": 790.0400000000001,
  "text": " What might seem like a decline could actually be a natural evolution.",
  "tokens": [50786, 708, 1062, 1643, 411, 257, 15635, 727, 767, 312, 257, 3303, 9303,
  13, 50968], "temperature": 0.0, "avg_logprob": -0.15416003382483193, "compression_ratio":
  1.634441087613293, "no_speech_prob": 0.007103354204446077}, {"id": 408, "seek":
  77796, "start": 790.0400000000001, "end": 791.0400000000001, "text": " Interesting.",
  "tokens": [50968, 14711, 13, 51018], "temperature": 0.0, "avg_logprob": -0.15416003382483193,
  "compression_ratio": 1.634441087613293, "no_speech_prob": 0.007103354204446077},
  {"id": 409, "seek": 77796, "start": 791.0400000000001, "end": 794.72, "text": "
  As a technology matures and finds its place within a larger ecosystem.", "tokens":
  [51018, 1018, 257, 2899, 275, 3377, 293, 10704, 1080, 1081, 1951, 257, 4833, 11311,
  13, 51202], "temperature": 0.0, "avg_logprob": -0.15416003382483193, "compression_ratio":
  1.634441087613293, "no_speech_prob": 0.007103354204446077}, {"id": 410, "seek":
  77796, "start": 794.72, "end": 795.72, "text": " Right.", "tokens": [51202, 1779,
  13, 51252], "temperature": 0.0, "avg_logprob": -0.15416003382483193, "compression_ratio":
  1.634441087613293, "no_speech_prob": 0.007103354204446077}, {"id": 411, "seek":
  77796, "start": 795.72, "end": 798.0400000000001, "text": " Like a caterpillar transforming
  into a butterfly.", "tokens": [51252, 1743, 257, 44982, 30635, 27210, 666, 257,
  22140, 13, 51368], "temperature": 0.0, "avg_logprob": -0.15416003382483193, "compression_ratio":
  1.634441087613293, "no_speech_prob": 0.007103354204446077}, {"id": 412, "seek":
  77796, "start": 798.0400000000001, "end": 799.0400000000001, "text": " That''s a
  wonderful analogy.", "tokens": [51368, 663, 311, 257, 3715, 21663, 13, 51418], "temperature":
  0.0, "avg_logprob": -0.15416003382483193, "compression_ratio": 1.634441087613293,
  "no_speech_prob": 0.007103354204446077}, {"id": 413, "seek": 77796, "start": 799.0400000000001,
  "end": 802.8000000000001, "text": " It''s still the same creature, just in a more
  advanced and beautiful form.", "tokens": [51418, 467, 311, 920, 264, 912, 12797,
  11, 445, 294, 257, 544, 7339, 293, 2238, 1254, 13, 51606], "temperature": 0.0, "avg_logprob":
  -0.15416003382483193, "compression_ratio": 1.634441087613293, "no_speech_prob":
  0.007103354204446077}, {"id": 414, "seek": 77796, "start": 802.8000000000001, "end":
  807.36, "text": " It underscores the importance of staying curious, continuing to
  explore, and never assuming", "tokens": [51606, 467, 16692, 66, 2706, 264, 7379,
  295, 7939, 6369, 11, 9289, 281, 6839, 11, 293, 1128, 11926, 51834], "temperature":
  0.0, "avg_logprob": -0.15416003382483193, "compression_ratio": 1.634441087613293,
  "no_speech_prob": 0.007103354204446077}, {"id": 415, "seek": 80736, "start": 807.36,
  "end": 810.72, "text": " that any technology is truly dead.", "tokens": [50364,
  300, 604, 2899, 307, 4908, 3116, 13, 50532], "temperature": 0.0, "avg_logprob":
  -0.19437014447511547, "compression_ratio": 1.608695652173913, "no_speech_prob":
  0.06758448481559753}, {"id": 416, "seek": 80736, "start": 810.72, "end": 813.32,
  "text": " Because it might just be evolving into something even better.", "tokens":
  [50532, 1436, 309, 1062, 445, 312, 21085, 666, 746, 754, 1101, 13, 50662], "temperature":
  0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 417, "seek": 80736, "start": 813.32,
  "end": 816.92, "text": " Who knows what exciting developments await us in the world
  of vector databases?", "tokens": [50662, 2102, 3255, 437, 4670, 20862, 19670, 505,
  294, 264, 1002, 295, 8062, 22380, 30, 50842], "temperature": 0.0, "avg_logprob":
  -0.19437014447511547, "compression_ratio": 1.608695652173913, "no_speech_prob":
  0.06758448481559753}, {"id": 418, "seek": 80736, "start": 816.92, "end": 818.96,
  "text": " I''m definitely eager to see what the future holds.", "tokens": [50842,
  286, 478, 2138, 18259, 281, 536, 437, 264, 2027, 9190, 13, 50944], "temperature":
  0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 419, "seek": 80736, "start": 818.96,
  "end": 819.96, "text": " E2.", "tokens": [50944, 462, 17, 13, 50994], "temperature":
  0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 420, "seek": 80736, "start": 819.96,
  "end": 822.5600000000001, "text": " This deep dive has given me a whole new perspective.",
  "tokens": [50994, 639, 2452, 9192, 575, 2212, 385, 257, 1379, 777, 4585, 13, 51124],
  "temperature": 0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 421, "seek": 80736, "start": 822.5600000000001,
  "end": 825.04, "text": " I''m sure it has for our listeners as well.", "tokens":
  [51124, 286, 478, 988, 309, 575, 337, 527, 23274, 382, 731, 13, 51248], "temperature":
  0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 422, "seek": 80736, "start": 825.04,
  "end": 830.32, "text": " You know, as we''re discussing this, it strikes me that
  Dmitry''s journey with vector databases", "tokens": [51248, 509, 458, 11, 382, 321,
  434, 10850, 341, 11, 309, 16750, 385, 300, 413, 3508, 627, 311, 4671, 365, 8062,
  22380, 51512], "temperature": 0.0, "avg_logprob": -0.19437014447511547, "compression_ratio":
  1.608695652173913, "no_speech_prob": 0.06758448481559753}, {"id": 423, "seek": 80736,
  "start": 830.32, "end": 833.32, "text": " mirrors a broader trend in the tech world.",
  "tokens": [51512, 24238, 257, 13227, 6028, 294, 264, 7553, 1002, 13, 51662], "temperature":
  0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 424, "seek": 80736, "start": 833.32,
  "end": 834.52, "text": " Oh, how so?", "tokens": [51662, 876, 11, 577, 370, 30,
  51722], "temperature": 0.0, "avg_logprob": -0.19437014447511547, "compression_ratio":
  1.608695652173913, "no_speech_prob": 0.06758448481559753}, {"id": 425, "seek": 80736,
  "start": 834.52, "end": 836.16, "text": " We often get caught up in the hype cycle.",
  "tokens": [51722, 492, 2049, 483, 5415, 493, 294, 264, 24144, 6586, 13, 51804],
  "temperature": 0.0, "avg_logprob": -0.19437014447511547, "compression_ratio": 1.608695652173913,
  "no_speech_prob": 0.06758448481559753}, {"id": 426, "seek": 83616, "start": 836.16,
  "end": 837.88, "text": " Oh, yeah, for sure.", "tokens": [50364, 876, 11, 1338,
  11, 337, 988, 13, 50450], "temperature": 0.0, "avg_logprob": -0.19287610521503523,
  "compression_ratio": 1.5320754716981133, "no_speech_prob": 0.01279979757964611},
  {"id": 427, "seek": 83616, "start": 837.88, "end": 844.3199999999999, "text": "
  But true innovation often emerges when technologies evolve and integrate in unexpected
  ways.", "tokens": [50450, 583, 2074, 8504, 2049, 38965, 562, 7943, 16693, 293, 13365,
  294, 13106, 2098, 13, 50772], "temperature": 0.0, "avg_logprob": -0.19287610521503523,
  "compression_ratio": 1.5320754716981133, "no_speech_prob": 0.01279979757964611},
  {"id": 428, "seek": 83616, "start": 844.3199999999999, "end": 849.0799999999999,
  "text": " It''s like that saying the whole is greater than the sum of its parts.",
  "tokens": [50772, 467, 311, 411, 300, 1566, 264, 1379, 307, 5044, 813, 264, 2408,
  295, 1080, 3166, 13, 51010], "temperature": 0.0, "avg_logprob": -0.19287610521503523,
  "compression_ratio": 1.5320754716981133, "no_speech_prob": 0.01279979757964611},
  {"id": 429, "seek": 83616, "start": 849.0799999999999, "end": 851.3199999999999,
  "text": " And that brings us to another crucial point from the article.", "tokens":
  [51010, 400, 300, 5607, 505, 281, 1071, 11462, 935, 490, 264, 7222, 13, 51122],
  "temperature": 0.0, "avg_logprob": -0.19287610521503523, "compression_ratio": 1.5320754716981133,
  "no_speech_prob": 0.01279979757964611}, {"id": 430, "seek": 83616, "start": 851.3199999999999,
  "end": 852.3199999999999, "text": " Okay.", "tokens": [51122, 1033, 13, 51172],
  "temperature": 0.0, "avg_logprob": -0.19287610521503523, "compression_ratio": 1.5320754716981133,
  "no_speech_prob": 0.01279979757964611}, {"id": 431, "seek": 83616, "start": 852.3199999999999,
  "end": 854.92, "text": " One that I think holds immense value for our listeners
  today.", "tokens": [51172, 1485, 300, 286, 519, 9190, 22920, 2158, 337, 527, 23274,
  965, 13, 51302], "temperature": 0.0, "avg_logprob": -0.19287610521503523, "compression_ratio":
  1.5320754716981133, "no_speech_prob": 0.01279979757964611}, {"id": 432, "seek":
  83616, "start": 854.92, "end": 856.24, "text": " I''m all ears.", "tokens": [51302,
  286, 478, 439, 8798, 13, 51368], "temperature": 0.0, "avg_logprob": -0.19287610521503523,
  "compression_ratio": 1.5320754716981133, "no_speech_prob": 0.01279979757964611},
  {"id": 433, "seek": 83616, "start": 856.24, "end": 860.9599999999999, "text": "
  Remember how Dmitry emphasized that it''s not just about the vectors themselves.",
  "tokens": [51368, 5459, 577, 413, 3508, 627, 34068, 300, 309, 311, 406, 445, 466,
  264, 18875, 2969, 13, 51604], "temperature": 0.0, "avg_logprob": -0.19287610521503523,
  "compression_ratio": 1.5320754716981133, "no_speech_prob": 0.01279979757964611},
  {"id": 434, "seek": 86096, "start": 860.96, "end": 866.32, "text": " It''s about
  understanding the nuances of data pre-processing model selection and bedding", "tokens":
  [50364, 467, 311, 466, 3701, 264, 38775, 295, 1412, 659, 12, 41075, 278, 2316, 9450,
  293, 2901, 3584, 50632], "temperature": 0.0, "avg_logprob": -0.20812978329865828,
  "compression_ratio": 1.5774647887323943, "no_speech_prob": 0.08708859235048294},
  {"id": 435, "seek": 86096, "start": 866.32, "end": 867.48, "text": " techniques.",
  "tokens": [50632, 7512, 13, 50690], "temperature": 0.0, "avg_logprob": -0.20812978329865828,
  "compression_ratio": 1.5774647887323943, "no_speech_prob": 0.08708859235048294},
  {"id": 436, "seek": 86096, "start": 867.48, "end": 873.08, "text": " And even knowing
  when to switch back to traditional keyword search for certain tasks.", "tokens":
  [50690, 400, 754, 5276, 562, 281, 3679, 646, 281, 5164, 20428, 3164, 337, 1629,
  9608, 13, 50970], "temperature": 0.0, "avg_logprob": -0.20812978329865828, "compression_ratio":
  1.5774647887323943, "no_speech_prob": 0.08708859235048294}, {"id": 437, "seek":
  86096, "start": 873.08, "end": 875.76, "text": " Yeah, sometimes the old ways are
  still the best.", "tokens": [50970, 865, 11, 2171, 264, 1331, 2098, 366, 920, 264,
  1151, 13, 51104], "temperature": 0.0, "avg_logprob": -0.20812978329865828, "compression_ratio":
  1.5774647887323943, "no_speech_prob": 0.08708859235048294}, {"id": 438, "seek":
  86096, "start": 875.76, "end": 882.2, "text": " He''s advocating for a more holistic
  approach where vector databases are seen as one tool", "tokens": [51104, 634, 311,
  32050, 337, 257, 544, 30334, 3109, 689, 8062, 22380, 366, 1612, 382, 472, 2290,
  51426], "temperature": 0.0, "avg_logprob": -0.20812978329865828, "compression_ratio":
  1.5774647887323943, "no_speech_prob": 0.08708859235048294}, {"id": 439, "seek":
  86096, "start": 882.2, "end": 884.2800000000001, "text": " among many in the AI
  toolbox.", "tokens": [51426, 3654, 867, 294, 264, 7318, 44593, 13, 51530], "temperature":
  0.0, "avg_logprob": -0.20812978329865828, "compression_ratio": 1.5774647887323943,
  "no_speech_prob": 0.08708859235048294}, {"id": 440, "seek": 86096, "start": 884.2800000000001,
  "end": 885.76, "text": " So it''s not a silver bullet.", "tokens": [51530, 407,
  309, 311, 406, 257, 8753, 11632, 13, 51604], "temperature": 0.0, "avg_logprob":
  -0.20812978329865828, "compression_ratio": 1.5774647887323943, "no_speech_prob":
  0.08708859235048294}, {"id": 441, "seek": 86096, "start": 885.76, "end": 886.9200000000001,
  "text": " It''s not a magic solution.", "tokens": [51604, 467, 311, 406, 257, 5585,
  3827, 13, 51662], "temperature": 0.0, "avg_logprob": -0.20812978329865828, "compression_ratio":
  1.5774647887323943, "no_speech_prob": 0.08708859235048294}, {"id": 442, "seek":
  86096, "start": 886.9200000000001, "end": 888.76, "text": " It''s one piece of the
  puzzle.", "tokens": [51662, 467, 311, 472, 2522, 295, 264, 12805, 13, 51754], "temperature":
  0.0, "avg_logprob": -0.20812978329865828, "compression_ratio": 1.5774647887323943,
  "no_speech_prob": 0.08708859235048294}, {"id": 443, "seek": 86096, "start": 888.76,
  "end": 889.76, "text": " Exactly.", "tokens": [51754, 7587, 13, 51804], "temperature":
  0.0, "avg_logprob": -0.20812978329865828, "compression_ratio": 1.5774647887323943,
  "no_speech_prob": 0.08708859235048294}, {"id": 444, "seek": 88976, "start": 889.76,
  "end": 895.0, "text": " There is a deeper understanding of the underlying principles,
  not just blindly applying the latest", "tokens": [50364, 821, 307, 257, 7731, 3701,
  295, 264, 14217, 9156, 11, 406, 445, 47744, 9275, 264, 6792, 50626], "temperature":
  0.0, "avg_logprob": -0.20254910376764113, "compression_ratio": 1.6214511041009463,
  "no_speech_prob": 0.17467549443244934}, {"id": 445, "seek": 88976, "start": 895.0,
  "end": 896.0, "text": " trendy technology.", "tokens": [50626, 38596, 2899, 13,
  50676], "temperature": 0.0, "avg_logprob": -0.20254910376764113, "compression_ratio":
  1.6214511041009463, "no_speech_prob": 0.17467549443244934}, {"id": 446, "seek":
  88976, "start": 896.0, "end": 897.0, "text": " Right.", "tokens": [50676, 1779,
  13, 50726], "temperature": 0.0, "avg_logprob": -0.20254910376764113, "compression_ratio":
  1.6214511041009463, "no_speech_prob": 0.17467549443244934}, {"id": 447, "seek":
  88976, "start": 897.0, "end": 901.76, "text": " It''s about making informed choices
  based on a thorough analysis of your specific needs and", "tokens": [50726, 467,
  311, 466, 1455, 11740, 7994, 2361, 322, 257, 12934, 5215, 295, 428, 2685, 2203,
  293, 50964], "temperature": 0.0, "avg_logprob": -0.20254910376764113, "compression_ratio":
  1.6214511041009463, "no_speech_prob": 0.17467549443244934}, {"id": 448, "seek":
  88976, "start": 901.76, "end": 902.76, "text": " constraints.", "tokens": [50964,
  18491, 13, 51014], "temperature": 0.0, "avg_logprob": -0.20254910376764113, "compression_ratio":
  1.6214511041009463, "no_speech_prob": 0.17467549443244934}, {"id": 449, "seek":
  88976, "start": 902.76, "end": 904.3199999999999, "text": " So don''t just jump
  on the bandwagon.", "tokens": [51014, 407, 500, 380, 445, 3012, 322, 264, 4116,
  86, 6709, 13, 51092], "temperature": 0.0, "avg_logprob": -0.20254910376764113, "compression_ratio":
  1.6214511041009463, "no_speech_prob": 0.17467549443244934}, {"id": 450, "seek":
  88976, "start": 904.3199999999999, "end": 906.88, "text": " Do your research and
  figure out what''s right for you.", "tokens": [51092, 1144, 428, 2132, 293, 2573,
  484, 437, 311, 558, 337, 291, 13, 51220], "temperature": 0.0, "avg_logprob": -0.20254910376764113,
  "compression_ratio": 1.6214511041009463, "no_speech_prob": 0.17467549443244934},
  {"id": 451, "seek": 88976, "start": 906.88, "end": 912.24, "text": " So for those
  of you out there exploring AI solutions, don''t get fixated on buzzwords.", "tokens":
  [51220, 407, 337, 729, 295, 291, 484, 456, 12736, 7318, 6547, 11, 500, 380, 483,
  3191, 770, 322, 13036, 13832, 13, 51488], "temperature": 0.0, "avg_logprob": -0.20254910376764113,
  "compression_ratio": 1.6214511041009463, "no_speech_prob": 0.17467549443244934},
  {"id": 452, "seek": 88976, "start": 912.24, "end": 915.64, "text": " Take the time
  to really grasp the fundamentals.", "tokens": [51488, 3664, 264, 565, 281, 534,
  21743, 264, 29505, 13, 51658], "temperature": 0.0, "avg_logprob": -0.20254910376764113,
  "compression_ratio": 1.6214511041009463, "no_speech_prob": 0.17467549443244934},
  {"id": 453, "seek": 88976, "start": 915.64, "end": 917.4399999999999, "text": "
  Understand the basics.", "tokens": [51658, 26093, 264, 14688, 13, 51748], "temperature":
  0.0, "avg_logprob": -0.20254910376764113, "compression_ratio": 1.6214511041009463,
  "no_speech_prob": 0.17467549443244934}, {"id": 454, "seek": 88976, "start": 917.4399999999999,
  "end": 918.56, "text": " Experiment with different approaches.", "tokens": [51748,
  37933, 365, 819, 11587, 13, 51804], "temperature": 0.0, "avg_logprob": -0.20254910376764113,
  "compression_ratio": 1.6214511041009463, "no_speech_prob": 0.17467549443244934},
  {"id": 455, "seek": 91856, "start": 918.56, "end": 920.16, "text": " Stay around
  with different tools.", "tokens": [50364, 8691, 926, 365, 819, 3873, 13, 50444],
  "temperature": 0.0, "avg_logprob": -0.2009817433153462, "compression_ratio": 1.5674740484429066,
  "no_speech_prob": 0.10541005432605743}, {"id": 456, "seek": 91856, "start": 920.16,
  "end": 922.8, "text": " And don''t be afraid to challenge assumptions.", "tokens":
  [50444, 400, 500, 380, 312, 4638, 281, 3430, 17695, 13, 50576], "temperature": 0.0,
  "avg_logprob": -0.2009817433153462, "compression_ratio": 1.5674740484429066, "no_speech_prob":
  0.10541005432605743}, {"id": 457, "seek": 91856, "start": 922.8, "end": 923.8, "text":
  " Question everything.", "tokens": [50576, 14464, 1203, 13, 50626], "temperature":
  0.0, "avg_logprob": -0.2009817433153462, "compression_ratio": 1.5674740484429066,
  "no_speech_prob": 0.10541005432605743}, {"id": 458, "seek": 91856, "start": 923.8,
  "end": 926.5999999999999, "text": " And remember, the AI landscape is constantly
  evolving.", "tokens": [50626, 400, 1604, 11, 264, 7318, 9661, 307, 6460, 21085,
  13, 50766], "temperature": 0.0, "avg_logprob": -0.2009817433153462, "compression_ratio":
  1.5674740484429066, "no_speech_prob": 0.10541005432605743}, {"id": 459, "seek":
  91856, "start": 926.5999999999999, "end": 930.68, "text": " What works best today
  might be superseded by something even more powerful and efficient", "tokens": [50766,
  708, 1985, 1151, 965, 1062, 312, 37906, 37679, 538, 746, 754, 544, 4005, 293, 7148,
  50970], "temperature": 0.0, "avg_logprob": -0.2009817433153462, "compression_ratio":
  1.5674740484429066, "no_speech_prob": 0.10541005432605743}, {"id": 460, "seek":
  91856, "start": 930.68, "end": 932.16, "text": " tomorrow.", "tokens": [50970, 4153,
  13, 51044], "temperature": 0.0, "avg_logprob": -0.2009817433153462, "compression_ratio":
  1.5674740484429066, "no_speech_prob": 0.10541005432605743}, {"id": 461, "seek":
  91856, "start": 932.16, "end": 933.16, "text": " So stay curious.", "tokens": [51044,
  407, 1754, 6369, 13, 51094], "temperature": 0.0, "avg_logprob": -0.2009817433153462,
  "compression_ratio": 1.5674740484429066, "no_speech_prob": 0.10541005432605743},
  {"id": 462, "seek": 91856, "start": 933.16, "end": 934.16, "text": " They engage.",
  "tokens": [51094, 814, 4683, 13, 51144], "temperature": 0.0, "avg_logprob": -0.2009817433153462,
  "compression_ratio": 1.5674740484429066, "no_speech_prob": 0.10541005432605743},
  {"id": 463, "seek": 91856, "start": 934.16, "end": 935.16, "text": " And keep learning.",
  "tokens": [51144, 400, 1066, 2539, 13, 51194], "temperature": 0.0, "avg_logprob":
  -0.2009817433153462, "compression_ratio": 1.5674740484429066, "no_speech_prob":
  0.10541005432605743}, {"id": 464, "seek": 91856, "start": 935.16, "end": 937.52,
  "text": " Couldn''t have said it better myself.", "tokens": [51194, 35800, 380,
  362, 848, 309, 1101, 2059, 13, 51312], "temperature": 0.0, "avg_logprob": -0.2009817433153462,
  "compression_ratio": 1.5674740484429066, "no_speech_prob": 0.10541005432605743},
  {"id": 465, "seek": 91856, "start": 937.52, "end": 943.88, "text": " Well folks,
  that brings us to the end of our deep dive into the world of vector databases.",
  "tokens": [51312, 1042, 4024, 11, 300, 5607, 505, 281, 264, 917, 295, 527, 2452,
  9192, 666, 264, 1002, 295, 8062, 22380, 13, 51630], "temperature": 0.0, "avg_logprob":
  -0.2009817433153462, "compression_ratio": 1.5674740484429066, "no_speech_prob":
  0.10541005432605743}, {"id": 466, "seek": 91856, "start": 943.88, "end": 945.52,
  "text": " It''s been a wild ride.", "tokens": [51630, 467, 311, 668, 257, 4868,
  5077, 13, 51712], "temperature": 0.0, "avg_logprob": -0.2009817433153462, "compression_ratio":
  1.5674740484429066, "no_speech_prob": 0.10541005432605743}, {"id": 467, "seek":
  94552, "start": 945.52, "end": 951.52, "text": " We''ve explored their rise, their
  potential fall, and the exciting possibilities of neural", "tokens": [50364, 492,
  600, 24016, 641, 6272, 11, 641, 3995, 2100, 11, 293, 264, 4670, 12178, 295, 18161,
  50664], "temperature": 0.0, "avg_logprob": -0.15887847439996128, "compression_ratio":
  1.627986348122867, "no_speech_prob": 0.04780411720275879}, {"id": 468, "seek": 94552,
  "start": 951.52, "end": 952.76, "text": " search frameworks.", "tokens": [50664,
  3164, 29834, 13, 50726], "temperature": 0.0, "avg_logprob": -0.15887847439996128,
  "compression_ratio": 1.627986348122867, "no_speech_prob": 0.04780411720275879},
  {"id": 469, "seek": 94552, "start": 952.76, "end": 954.4, "text": " We''ve covered
  a lot of ground.", "tokens": [50726, 492, 600, 5343, 257, 688, 295, 2727, 13, 50808],
  "temperature": 0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 470, "seek": 94552, "start": 954.4,
  "end": 959.0799999999999, "text": " We''ve also learned some valuable lessons about
  navigating the hype cycle and making informed", "tokens": [50808, 492, 600, 611,
  3264, 512, 8263, 8820, 466, 32054, 264, 24144, 6586, 293, 1455, 11740, 51042], "temperature":
  0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 471, "seek": 94552, "start": 959.0799999999999,
  "end": 962.24, "text": " decisions in a rapidly changing technological landscape.",
  "tokens": [51042, 5327, 294, 257, 12910, 4473, 18439, 9661, 13, 51200], "temperature":
  0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 472, "seek": 94552, "start": 962.24,
  "end": 963.8, "text": " It''s been a fascinating journey.", "tokens": [51200, 467,
  311, 668, 257, 10343, 4671, 13, 51278], "temperature": 0.0, "avg_logprob": -0.15887847439996128,
  "compression_ratio": 1.627986348122867, "no_speech_prob": 0.04780411720275879},
  {"id": 473, "seek": 94552, "start": 963.8, "end": 964.8, "text": " Absolutely.",
  "tokens": [51278, 7021, 13, 51328], "temperature": 0.0, "avg_logprob": -0.15887847439996128,
  "compression_ratio": 1.627986348122867, "no_speech_prob": 0.04780411720275879},
  {"id": 474, "seek": 94552, "start": 964.8, "end": 966.96, "text": " And we hope
  you''ve enjoyed it as much as we have.", "tokens": [51328, 400, 321, 1454, 291,
  600, 4626, 309, 382, 709, 382, 321, 362, 13, 51436], "temperature": 0.0, "avg_logprob":
  -0.15887847439996128, "compression_ratio": 1.627986348122867, "no_speech_prob":
  0.04780411720275879}, {"id": 475, "seek": 94552, "start": 966.96, "end": 967.96,
  "text": " Until next time.", "tokens": [51436, 9088, 958, 565, 13, 51486], "temperature":
  0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 476, "seek": 94552, "start": 967.96,
  "end": 969.16, "text": " Keep exploring.", "tokens": [51486, 5527, 12736, 13, 51546],
  "temperature": 0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 477, "seek": 94552, "start": 969.16,
  "end": 970.24, "text": " Keep questioning.", "tokens": [51546, 5527, 21257, 13,
  51600], "temperature": 0.0, "avg_logprob": -0.15887847439996128, "compression_ratio":
  1.627986348122867, "no_speech_prob": 0.04780411720275879}, {"id": 478, "seek": 94552,
  "start": 970.24, "end": 972.76, "text": " And keep that thirst for knowledge alive.",
  "tokens": [51600, 400, 1066, 300, 34846, 337, 3601, 5465, 13, 51726], "temperature":
  0.0, "avg_logprob": -0.15887847439996128, "compression_ratio": 1.627986348122867,
  "no_speech_prob": 0.04780411720275879}, {"id": 479, "seek": 97276, "start": 972.76,
  "end": 977.2, "text": " It''s funny actually while we''re focused on all this cutting
  edge tech, Dimitri actually", "tokens": [50364, 467, 311, 4074, 767, 1339, 321,
  434, 5178, 322, 439, 341, 6492, 4691, 7553, 11, 20975, 270, 470, 767, 50586], "temperature":
  0.0, "avg_logprob": -0.18286917550223214, "compression_ratio": 1.6242603550295858,
  "no_speech_prob": 0.31692713499069214}, {"id": 480, "seek": 97276, "start": 977.2,
  "end": 979.64, "text": " kind of throws it back to basics in the article a little
  bit.", "tokens": [50586, 733, 295, 19251, 309, 646, 281, 14688, 294, 264, 7222,
  257, 707, 857, 13, 50708], "temperature": 0.0, "avg_logprob": -0.18286917550223214,
  "compression_ratio": 1.6242603550295858, "no_speech_prob": 0.31692713499069214},
  {"id": 481, "seek": 97276, "start": 979.64, "end": 981.16, "text": " Oh yeah, I
  remember that part.", "tokens": [50708, 876, 1338, 11, 286, 1604, 300, 644, 13,
  50784], "temperature": 0.0, "avg_logprob": -0.18286917550223214, "compression_ratio":
  1.6242603550295858, "no_speech_prob": 0.31692713499069214}, {"id": 482, "seek":
  97276, "start": 981.16, "end": 985.68, "text": " He recounts this conversation he
  had with the chief data scientist at a major bank.", "tokens": [50784, 634, 43997,
  82, 341, 3761, 415, 632, 365, 264, 9588, 1412, 12662, 412, 257, 2563, 3765, 13,
  51010], "temperature": 0.0, "avg_logprob": -0.18286917550223214, "compression_ratio":
  1.6242603550295858, "no_speech_prob": 0.31692713499069214}, {"id": 483, "seek":
  97276, "start": 985.68, "end": 990.04, "text": " That was a good one, which I thought
  was so interesting because it really emphasizes", "tokens": [51010, 663, 390, 257,
  665, 472, 11, 597, 286, 1194, 390, 370, 1880, 570, 309, 534, 48856, 51228], "temperature":
  0.0, "avg_logprob": -0.18286917550223214, "compression_ratio": 1.6242603550295858,
  "no_speech_prob": 0.31692713499069214}, {"id": 484, "seek": 97276, "start": 990.04,
  "end": 995.4399999999999, "text": " how even with all these advancements, sometimes
  the simplest solution is the best one.", "tokens": [51228, 577, 754, 365, 439, 613,
  7295, 1117, 11, 2171, 264, 22811, 3827, 307, 264, 1151, 472, 13, 51498], "temperature":
  0.0, "avg_logprob": -0.18286917550223214, "compression_ratio": 1.6242603550295858,
  "no_speech_prob": 0.31692713499069214}, {"id": 485, "seek": 97276, "start": 995.4399999999999,
  "end": 997.68, "text": " You don''t always need the fanciest tools.", "tokens":
  [51498, 509, 500, 380, 1009, 643, 264, 3429, 537, 377, 3873, 13, 51610], "temperature":
  0.0, "avg_logprob": -0.18286917550223214, "compression_ratio": 1.6242603550295858,
  "no_speech_prob": 0.31692713499069214}, {"id": 486, "seek": 97276, "start": 997.68,
  "end": 998.68, "text": " Right.", "tokens": [51610, 1779, 13, 51660], "temperature":
  0.0, "avg_logprob": -0.18286917550223214, "compression_ratio": 1.6242603550295858,
  "no_speech_prob": 0.31692713499069214}, {"id": 487, "seek": 97276, "start": 998.68,
  "end": 1001.08, "text": " Sometimes it''s about using the right tool for the job.",
  "tokens": [51660, 4803, 309, 311, 466, 1228, 264, 558, 2290, 337, 264, 1691, 13,
  51780], "temperature": 0.0, "avg_logprob": -0.18286917550223214, "compression_ratio":
  1.6242603550295858, "no_speech_prob": 0.31692713499069214}, {"id": 488, "seek":
  97276, "start": 1001.08, "end": 1002.08, "text": " Exactly.", "tokens": [51780,
  7587, 13, 51830], "temperature": 0.0, "avg_logprob": -0.18286917550223214, "compression_ratio":
  1.6242603550295858, "no_speech_prob": 0.31692713499069214}, {"id": 489, "seek":
  100208, "start": 1002.08, "end": 1006.1600000000001, "text": " This bank had poured
  resources into building this complex vector search system.", "tokens": [50364, 639,
  3765, 632, 23270, 3593, 666, 2390, 341, 3997, 8062, 3164, 1185, 13, 50568], "temperature":
  0.0, "avg_logprob": -0.19838447868824005, "compression_ratio": 1.5377049180327869,
  "no_speech_prob": 0.11691146343946457}, {"id": 490, "seek": 100208, "start": 1006.1600000000001,
  "end": 1007.1600000000001, "text": " Okay.", "tokens": [50568, 1033, 13, 50618],
  "temperature": 0.0, "avg_logprob": -0.19838447868824005, "compression_ratio": 1.5377049180327869,
  "no_speech_prob": 0.11691146343946457}, {"id": 491, "seek": 100208, "start": 1007.1600000000001,
  "end": 1008.1600000000001, "text": " But guess what?", "tokens": [50618, 583, 2041,
  437, 30, 50668], "temperature": 0.0, "avg_logprob": -0.19838447868824005, "compression_ratio":
  1.5377049180327869, "no_speech_prob": 0.11691146343946457}, {"id": 492, "seek":
  100208, "start": 1008.1600000000001, "end": 1009.1600000000001, "text": " What?",
  "tokens": [50668, 708, 30, 50718], "temperature": 0.0, "avg_logprob": -0.19838447868824005,
  "compression_ratio": 1.5377049180327869, "no_speech_prob": 0.11691146343946457},
  {"id": 493, "seek": 100208, "start": 1009.1600000000001, "end": 1012.0, "text":
  " They ended up getting better results with good old fashioned keyword search.",
  "tokens": [50718, 814, 4590, 493, 1242, 1101, 3542, 365, 665, 1331, 40646, 20428,
  3164, 13, 50860], "temperature": 0.0, "avg_logprob": -0.19838447868824005, "compression_ratio":
  1.5377049180327869, "no_speech_prob": 0.11691146343946457}, {"id": 494, "seek":
  100208, "start": 1012.0, "end": 1013.0, "text": " Really?", "tokens": [50860, 4083,
  30, 50910], "temperature": 0.0, "avg_logprob": -0.19838447868824005, "compression_ratio":
  1.5377049180327869, "no_speech_prob": 0.11691146343946457}, {"id": 495, "seek":
  100208, "start": 1013.0, "end": 1015.0, "text": " For some very specific tasks.",
  "tokens": [50910, 1171, 512, 588, 2685, 9608, 13, 51010], "temperature": 0.0, "avg_logprob":
  -0.19838447868824005, "compression_ratio": 1.5377049180327869, "no_speech_prob":
  0.11691146343946457}, {"id": 496, "seek": 100208, "start": 1015.0, "end": 1016.0,
  "text": " Huh.", "tokens": [51010, 8063, 13, 51060], "temperature": 0.0, "avg_logprob":
  -0.19838447868824005, "compression_ratio": 1.5377049180327869, "no_speech_prob":
  0.11691146343946457}, {"id": 497, "seek": 100208, "start": 1016.0, "end": 1018.76,
  "text": " So even the big bangs are going back to basics sometimes.", "tokens":
  [51060, 407, 754, 264, 955, 32802, 366, 516, 646, 281, 14688, 2171, 13, 51198],
  "temperature": 0.0, "avg_logprob": -0.19838447868824005, "compression_ratio": 1.5377049180327869,
  "no_speech_prob": 0.11691146343946457}, {"id": 498, "seek": 100208, "start": 1018.76,
  "end": 1019.76, "text": " Sometimes it makes more sense.", "tokens": [51198, 4803,
  309, 1669, 544, 2020, 13, 51248], "temperature": 0.0, "avg_logprob": -0.19838447868824005,
  "compression_ratio": 1.5377049180327869, "no_speech_prob": 0.11691146343946457},
  {"id": 499, "seek": 100208, "start": 1019.76, "end": 1020.76, "text": " Yeah.",
  "tokens": [51248, 865, 13, 51298], "temperature": 0.0, "avg_logprob": -0.19838447868824005,
  "compression_ratio": 1.5377049180327869, "no_speech_prob": 0.11691146343946457},
  {"id": 500, "seek": 100208, "start": 1020.76, "end": 1025.08, "text": " It''s a
  powerful reminder that we shouldn''t dismiss those tried and true methods.", "tokens":
  [51298, 467, 311, 257, 4005, 13548, 300, 321, 4659, 380, 16974, 729, 3031, 293,
  2074, 7150, 13, 51514], "temperature": 0.0, "avg_logprob": -0.19838447868824005,
  "compression_ratio": 1.5377049180327869, "no_speech_prob": 0.11691146343946457},
  {"id": 501, "seek": 100208, "start": 1025.08, "end": 1027.32, "text": " Like don''t
  throw out the baby with the bathwater.", "tokens": [51514, 1743, 500, 380, 3507,
  484, 264, 3186, 365, 264, 6079, 8002, 13, 51626], "temperature": 0.0, "avg_logprob":
  -0.19838447868824005, "compression_ratio": 1.5377049180327869, "no_speech_prob":
  0.11691146343946457}, {"id": 502, "seek": 100208, "start": 1027.32, "end": 1028.32,
  "text": " Right.", "tokens": [51626, 1779, 13, 51676], "temperature": 0.0, "avg_logprob":
  -0.19838447868824005, "compression_ratio": 1.5377049180327869, "no_speech_prob":
  0.11691146343946457}, {"id": 503, "seek": 100208, "start": 1028.32, "end": 1029.32,
  "text": " Exactly.", "tokens": [51676, 7587, 13, 51726], "temperature": 0.0, "avg_logprob":
  -0.19838447868824005, "compression_ratio": 1.5377049180327869, "no_speech_prob":
  0.11691146343946457}, {"id": 504, "seek": 102932, "start": 1029.32, "end": 1033.8,
  "text": " The tools when used strategically can outperform the flashiest new tech.",
  "tokens": [50364, 440, 3873, 562, 1143, 38061, 393, 484, 26765, 264, 7319, 6495,
  777, 7553, 13, 50588], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 505,
  "seek": 102932, "start": 1033.8, "end": 1036.48, "text": " It''s all about choosing
  the right tool for the job.", "tokens": [50588, 467, 311, 439, 466, 10875, 264,
  558, 2290, 337, 264, 1691, 13, 50722], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 506,
  "seek": 102932, "start": 1036.48, "end": 1039.1599999999999, "text": " It''s like
  trying to use a chainsaw to cut a piece of paper.", "tokens": [50722, 467, 311,
  411, 1382, 281, 764, 257, 12626, 1607, 281, 1723, 257, 2522, 295, 3035, 13, 50856],
  "temperature": 0.0, "avg_logprob": -0.20490973525577122, "compression_ratio": 1.609375,
  "no_speech_prob": 0.5447851419448853}, {"id": 507, "seek": 102932, "start": 1039.1599999999999,
  "end": 1040.1599999999999, "text": " Oof.", "tokens": [50856, 422, 2670, 13, 50906],
  "temperature": 0.0, "avg_logprob": -0.20490973525577122, "compression_ratio": 1.609375,
  "no_speech_prob": 0.5447851419448853}, {"id": 508, "seek": 102932, "start": 1040.1599999999999,
  "end": 1041.76, "text": " Yeah, that wouldn''t end well.", "tokens": [50906, 865,
  11, 300, 2759, 380, 917, 731, 13, 50986], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 509,
  "seek": 102932, "start": 1041.76, "end": 1044.32, "text": " Sometimes a simple pair
  of scissors does the job better.", "tokens": [50986, 4803, 257, 2199, 6119, 295,
  16066, 775, 264, 1691, 1101, 13, 51114], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 510,
  "seek": 102932, "start": 1044.32, "end": 1045.96, "text": " Much better.", "tokens":
  [51114, 12313, 1101, 13, 51196], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 511,
  "seek": 102932, "start": 1045.96, "end": 1049.6399999999999, "text": " And that
  brings us back to Dimitri''s vision of neural search frameworks.", "tokens": [51196,
  400, 300, 5607, 505, 646, 281, 20975, 270, 470, 311, 5201, 295, 18161, 3164, 29834,
  13, 51380], "temperature": 0.0, "avg_logprob": -0.20490973525577122, "compression_ratio":
  1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 512, "seek": 102932, "start":
  1049.6399999999999, "end": 1050.6399999999999, "text": " Okay.", "tokens": [51380,
  1033, 13, 51430], "temperature": 0.0, "avg_logprob": -0.20490973525577122, "compression_ratio":
  1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 513, "seek": 102932, "start":
  1050.6399999999999, "end": 1051.6399999999999, "text": " If they become a reality.",
  "tokens": [51430, 759, 436, 1813, 257, 4103, 13, 51480], "temperature": 0.0, "avg_logprob":
  -0.20490973525577122, "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853},
  {"id": 514, "seek": 102932, "start": 1051.6399999999999, "end": 1052.6399999999999,
  "text": " Yeah.", "tokens": [51480, 865, 13, 51530], "temperature": 0.0, "avg_logprob":
  -0.20490973525577122, "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853},
  {"id": 515, "seek": 102932, "start": 1052.6399999999999, "end": 1054.6, "text":
  " Could they simplify these choices for us?", "tokens": [51530, 7497, 436, 20460,
  613, 7994, 337, 505, 30, 51628], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 516,
  "seek": 102932, "start": 1054.6, "end": 1055.6, "text": " Interesting question.",
  "tokens": [51628, 14711, 1168, 13, 51678], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 517,
  "seek": 102932, "start": 1055.6, "end": 1058.48, "text": " Would they be able to
  determine the best approach?", "tokens": [51678, 6068, 436, 312, 1075, 281, 6997,
  264, 1151, 3109, 30, 51822], "temperature": 0.0, "avg_logprob": -0.20490973525577122,
  "compression_ratio": 1.609375, "no_speech_prob": 0.5447851419448853}, {"id": 518,
  "seek": 105848, "start": 1058.48, "end": 1064.16, "text": " Like whether it''s vector
  search, keyword search or a hybrid based on the task at hand.", "tokens": [50364,
  1743, 1968, 309, 311, 8062, 3164, 11, 20428, 3164, 420, 257, 13051, 2361, 322, 264,
  5633, 412, 1011, 13, 50648], "temperature": 0.0, "avg_logprob": -0.1728199818095223,
  "compression_ratio": 1.632867132867133, "no_speech_prob": 0.004857513587921858},
  {"id": 519, "seek": 105848, "start": 1064.16, "end": 1065.16, "text": " That''s
  the dream.", "tokens": [50648, 663, 311, 264, 3055, 13, 50698], "temperature": 0.0,
  "avg_logprob": -0.1728199818095223, "compression_ratio": 1.632867132867133, "no_speech_prob":
  0.004857513587921858}, {"id": 520, "seek": 105848, "start": 1065.16, "end": 1066.16,
  "text": " How be amazed?", "tokens": [50698, 1012, 312, 20507, 30, 50748], "temperature":
  0.0, "avg_logprob": -0.1728199818095223, "compression_ratio": 1.632867132867133,
  "no_speech_prob": 0.004857513587921858}, {"id": 521, "seek": 105848, "start": 1066.16,
  "end": 1070.76, "text": " It would be like having this AI assistant that just knows
  the best way to search for anything.", "tokens": [50748, 467, 576, 312, 411, 1419,
  341, 7318, 10994, 300, 445, 3255, 264, 1151, 636, 281, 3164, 337, 1340, 13, 50978],
  "temperature": 0.0, "avg_logprob": -0.1728199818095223, "compression_ratio": 1.632867132867133,
  "no_speech_prob": 0.004857513587921858}, {"id": 522, "seek": 105848, "start": 1070.76,
  "end": 1072.2, "text": " That''s a fantastic question.", "tokens": [50978, 663,
  311, 257, 5456, 1168, 13, 51050], "temperature": 0.0, "avg_logprob": -0.1728199818095223,
  "compression_ratio": 1.632867132867133, "no_speech_prob": 0.004857513587921858},
  {"id": 523, "seek": 105848, "start": 1072.2, "end": 1077.2, "text": " It really
  gets to the heart of what these frameworks could potentially offer.", "tokens":
  [51050, 467, 534, 2170, 281, 264, 1917, 295, 437, 613, 29834, 727, 7263, 2626, 13,
  51300], "temperature": 0.0, "avg_logprob": -0.1728199818095223, "compression_ratio":
  1.632867132867133, "no_speech_prob": 0.004857513587921858}, {"id": 524, "seek":
  105848, "start": 1077.2, "end": 1080.92, "text": " Like a more intelligent and adaptable
  approach to search.", "tokens": [51300, 1743, 257, 544, 13232, 293, 6231, 712, 3109,
  281, 3164, 13, 51486], "temperature": 0.0, "avg_logprob": -0.1728199818095223, "compression_ratio":
  1.632867132867133, "no_speech_prob": 0.004857513587921858}, {"id": 525, "seek":
  105848, "start": 1080.92, "end": 1083.2, "text": " So instead of us having to figure
  it all out.", "tokens": [51486, 407, 2602, 295, 505, 1419, 281, 2573, 309, 439,
  484, 13, 51600], "temperature": 0.0, "avg_logprob": -0.1728199818095223, "compression_ratio":
  1.632867132867133, "no_speech_prob": 0.004857513587921858}, {"id": 526, "seek":
  105848, "start": 1083.2, "end": 1084.2, "text": " Yeah.", "tokens": [51600, 865,
  13, 51650], "temperature": 0.0, "avg_logprob": -0.1728199818095223, "compression_ratio":
  1.632867132867133, "no_speech_prob": 0.004857513587921858}, {"id": 527, "seek":
  105848, "start": 1084.2, "end": 1085.96, "text": " The system would just do it for
  us.", "tokens": [51650, 440, 1185, 576, 445, 360, 309, 337, 505, 13, 51738], "temperature":
  0.0, "avg_logprob": -0.1728199818095223, "compression_ratio": 1.632867132867133,
  "no_speech_prob": 0.004857513587921858}, {"id": 528, "seek": 108596, "start": 1085.96,
  "end": 1092.04, "text": " A vision of system that not only combines different AI
  components, but also understands", "tokens": [50364, 316, 5201, 295, 1185, 300,
  406, 787, 29520, 819, 7318, 6677, 11, 457, 611, 15146, 50668], "temperature": 0.0,
  "avg_logprob": -0.20408561494615343, "compression_ratio": 1.5614035087719298, "no_speech_prob":
  0.13744895160198212}, {"id": 529, "seek": 108596, "start": 1092.04, "end": 1096.16,
  "text": " which tool is best suited for each specific task.", "tokens": [50668,
  597, 2290, 307, 1151, 24736, 337, 1184, 2685, 5633, 13, 50874], "temperature": 0.0,
  "avg_logprob": -0.20408561494615343, "compression_ratio": 1.5614035087719298, "no_speech_prob":
  0.13744895160198212}, {"id": 530, "seek": 108596, "start": 1096.16, "end": 1097.56,
  "text": " That would be a game changer.", "tokens": [50874, 663, 576, 312, 257,
  1216, 22822, 13, 50944], "temperature": 0.0, "avg_logprob": -0.20408561494615343,
  "compression_ratio": 1.5614035087719298, "no_speech_prob": 0.13744895160198212},
  {"id": 531, "seek": 108596, "start": 1097.56, "end": 1101.88, "text": " It would
  free us from getting bogged down in the technical details and allow us to focus",
  "tokens": [50944, 467, 576, 1737, 505, 490, 1242, 26132, 3004, 760, 294, 264, 6191,
  4365, 293, 2089, 505, 281, 1879, 51160], "temperature": 0.0, "avg_logprob": -0.20408561494615343,
  "compression_ratio": 1.5614035087719298, "no_speech_prob": 0.13744895160198212},
  {"id": 532, "seek": 108596, "start": 1101.88, "end": 1103.8400000000001, "text":
  " on solving real world problems.", "tokens": [51160, 322, 12606, 957, 1002, 2740,
  13, 51258], "temperature": 0.0, "avg_logprob": -0.20408561494615343, "compression_ratio":
  1.5614035087719298, "no_speech_prob": 0.13744895160198212}, {"id": 533, "seek":
  108596, "start": 1103.8400000000001, "end": 1106.68, "text": " It''s all about making
  AI work for us.", "tokens": [51258, 467, 311, 439, 466, 1455, 7318, 589, 337, 505,
  13, 51400], "temperature": 0.0, "avg_logprob": -0.20408561494615343, "compression_ratio":
  1.5614035087719298, "no_speech_prob": 0.13744895160198212}, {"id": 534, "seek":
  108596, "start": 1106.68, "end": 1108.16, "text": " Not the other way around.",
  "tokens": [51400, 1726, 264, 661, 636, 926, 13, 51474], "temperature": 0.0, "avg_logprob":
  -0.20408561494615343, "compression_ratio": 1.5614035087719298, "no_speech_prob":
  0.13744895160198212}, {"id": 535, "seek": 108596, "start": 1108.16, "end": 1109.3600000000001,
  "text": " Exactly.", "tokens": [51474, 7587, 13, 51534], "temperature": 0.0, "avg_logprob":
  -0.20408561494615343, "compression_ratio": 1.5614035087719298, "no_speech_prob":
  0.13744895160198212}, {"id": 536, "seek": 108596, "start": 1109.3600000000001, "end":
  1114.24, "text": " And it highlights the importance of staying flexible and open
  to new possibilities.", "tokens": [51534, 400, 309, 14254, 264, 7379, 295, 7939,
  11358, 293, 1269, 281, 777, 12178, 13, 51778], "temperature": 0.0, "avg_logprob":
  -0.20408561494615343, "compression_ratio": 1.5614035087719298, "no_speech_prob":
  0.13744895160198212}, {"id": 537, "seek": 111424, "start": 1114.24, "end": 1120.6,
  "text": " As the AI landscape continues to evolve, we need to be willing to adapt
  and embrace", "tokens": [50364, 1018, 264, 7318, 9661, 6515, 281, 16693, 11, 321,
  643, 281, 312, 4950, 281, 6231, 293, 14038, 50682], "temperature": 0.0, "avg_logprob":
  -0.18256014869326637, "compression_ratio": 1.550387596899225, "no_speech_prob":
  0.008506925776600838}, {"id": 538, "seek": 111424, "start": 1120.6, "end": 1121.6,
  "text": " new approaches.", "tokens": [50682, 777, 11587, 13, 50732], "temperature":
  0.0, "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225,
  "no_speech_prob": 0.008506925776600838}, {"id": 539, "seek": 111424, "start": 1121.6,
  "end": 1124.16, "text": " Even if the challenger existing assumptions.", "tokens":
  [50732, 2754, 498, 264, 2076, 10210, 6741, 17695, 13, 50860], "temperature": 0.0,
  "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225, "no_speech_prob":
  0.008506925776600838}, {"id": 540, "seek": 111424, "start": 1124.16, "end": 1125.16,
  "text": " Challenge the status quo.", "tokens": [50860, 17517, 264, 6558, 28425,
  13, 50910], "temperature": 0.0, "avg_logprob": -0.18256014869326637, "compression_ratio":
  1.550387596899225, "no_speech_prob": 0.008506925776600838}, {"id": 541, "seek":
  111424, "start": 1125.16, "end": 1126.16, "text": " Right.", "tokens": [50910, 1779,
  13, 50960], "temperature": 0.0, "avg_logprob": -0.18256014869326637, "compression_ratio":
  1.550387596899225, "no_speech_prob": 0.008506925776600838}, {"id": 542, "seek":
  111424, "start": 1126.16, "end": 1129.2, "text": " Well said, well, this deep dive
  has been a whirlwind of information.", "tokens": [50960, 1042, 848, 11, 731, 11,
  341, 2452, 9192, 575, 668, 257, 35706, 12199, 295, 1589, 13, 51112], "temperature":
  0.0, "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225,
  "no_speech_prob": 0.008506925776600838}, {"id": 543, "seek": 111424, "start": 1129.2,
  "end": 1130.2, "text": " It has.", "tokens": [51112, 467, 575, 13, 51162], "temperature":
  0.0, "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225,
  "no_speech_prob": 0.008506925776600838}, {"id": 544, "seek": 111424, "start": 1130.2,
  "end": 1136.8, "text": " But I think the biggest takeaway for me is that the world
  of vector databases and AI in general", "tokens": [51162, 583, 286, 519, 264, 3880,
  30681, 337, 385, 307, 300, 264, 1002, 295, 8062, 22380, 293, 7318, 294, 2674, 51492],
  "temperature": 0.0, "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225,
  "no_speech_prob": 0.008506925776600838}, {"id": 545, "seek": 111424, "start": 1136.8,
  "end": 1139.24, "text": " is anything but static.", "tokens": [51492, 307, 1340,
  457, 13437, 13, 51614], "temperature": 0.0, "avg_logprob": -0.18256014869326637,
  "compression_ratio": 1.550387596899225, "no_speech_prob": 0.008506925776600838},
  {"id": 546, "seek": 111424, "start": 1139.24, "end": 1140.52, "text": " It''s constantly
  changing.", "tokens": [51614, 467, 311, 6460, 4473, 13, 51678], "temperature": 0.0,
  "avg_logprob": -0.18256014869326637, "compression_ratio": 1.550387596899225, "no_speech_prob":
  0.008506925776600838}, {"id": 547, "seek": 114052, "start": 1140.52, "end": 1145.12,
  "text": " It''s a constantly evolving landscape full of exciting possibilities and
  unexpected twists", "tokens": [50364, 467, 311, 257, 6460, 21085, 9661, 1577, 295,
  4670, 12178, 293, 13106, 35290, 50594], "temperature": 0.0, "avg_logprob": -0.16215332576206754,
  "compression_ratio": 1.6586102719033233, "no_speech_prob": 0.10723783075809479},
  {"id": 548, "seek": 114052, "start": 1145.12, "end": 1146.12, "text": " in turn.",
  "tokens": [50594, 294, 1261, 13, 50644], "temperature": 0.0, "avg_logprob": -0.16215332576206754,
  "compression_ratio": 1.6586102719033233, "no_speech_prob": 0.10723783075809479},
  {"id": 549, "seek": 114052, "start": 1146.12, "end": 1147.28, "text": " You never
  know what''s going to come next.", "tokens": [50644, 509, 1128, 458, 437, 311, 516,
  281, 808, 958, 13, 50702], "temperature": 0.0, "avg_logprob": -0.16215332576206754,
  "compression_ratio": 1.6586102719033233, "no_speech_prob": 0.10723783075809479},
  {"id": 550, "seek": 114052, "start": 1147.28, "end": 1148.76, "text": " And that''s
  what makes it so exciting.", "tokens": [50702, 400, 300, 311, 437, 1669, 309, 370,
  4670, 13, 50776], "temperature": 0.0, "avg_logprob": -0.16215332576206754, "compression_ratio":
  1.6586102719033233, "no_speech_prob": 0.10723783075809479}, {"id": 551, "seek":
  114052, "start": 1148.76, "end": 1149.76, "text": " I completely agree.", "tokens":
  [50776, 286, 2584, 3986, 13, 50826], "temperature": 0.0, "avg_logprob": -0.16215332576206754,
  "compression_ratio": 1.6586102719033233, "no_speech_prob": 0.10723783075809479},
  {"id": 552, "seek": 114052, "start": 1149.76, "end": 1152.8799999999999, "text":
  " And it''s a landscape that requires us to stay curious.", "tokens": [50826, 400,
  309, 311, 257, 9661, 300, 7029, 505, 281, 1754, 6369, 13, 50982], "temperature":
  0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 553, "seek": 114052, "start": 1152.8799999999999,
  "end": 1153.8799999999999, "text": " Keep learning.", "tokens": [50982, 5527, 2539,
  13, 51032], "temperature": 0.0, "avg_logprob": -0.16215332576206754, "compression_ratio":
  1.6586102719033233, "no_speech_prob": 0.10723783075809479}, {"id": 554, "seek":
  114052, "start": 1153.8799999999999, "end": 1155.76, "text": " And never stop asking
  questions.", "tokens": [51032, 400, 1128, 1590, 3365, 1651, 13, 51126], "temperature":
  0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 555, "seek": 114052, "start": 1155.76,
  "end": 1159.28, "text": " And on that note, we''d love to hear from you, our listeners.",
  "tokens": [51126, 400, 322, 300, 3637, 11, 321, 1116, 959, 281, 1568, 490, 291,
  11, 527, 23274, 13, 51302], "temperature": 0.0, "avg_logprob": -0.16215332576206754,
  "compression_ratio": 1.6586102719033233, "no_speech_prob": 0.10723783075809479},
  {"id": 556, "seek": 114052, "start": 1159.28, "end": 1161.16, "text": " Yes, please
  share your thoughts.", "tokens": [51302, 1079, 11, 1767, 2073, 428, 4598, 13, 51396],
  "temperature": 0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 557, "seek": 114052, "start": 1161.16,
  "end": 1163.56, "text": " What are your thoughts on the future of vector databases?",
  "tokens": [51396, 708, 366, 428, 4598, 322, 264, 2027, 295, 8062, 22380, 30, 51516],
  "temperature": 0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 558, "seek": 114052, "start": 1163.56,
  "end": 1164.56, "text": " Hmm.", "tokens": [51516, 8239, 13, 51566], "temperature":
  0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 559, "seek": 114052, "start": 1164.56,
  "end": 1169.04, "text": " Do you think neural search frameworks will revolutionize
  the way we build AI applications?", "tokens": [51566, 1144, 291, 519, 18161, 3164,
  29834, 486, 8894, 1125, 264, 636, 321, 1322, 7318, 5821, 30, 51790], "temperature":
  0.0, "avg_logprob": -0.16215332576206754, "compression_ratio": 1.6586102719033233,
  "no_speech_prob": 0.10723783075809479}, {"id": 560, "seek": 116904, "start": 1169.04,
  "end": 1171.04, "text": " That''s the big question.", "tokens": [50364, 663, 311,
  264, 955, 1168, 13, 50464], "temperature": 0.0, "avg_logprob": -0.16757558254485436,
  "compression_ratio": 1.6036866359447004, "no_speech_prob": 0.25533971190452576},
  {"id": 561, "seek": 116904, "start": 1171.04, "end": 1173.24, "text": " Share your
  insights, your predictions, and your questions.", "tokens": [50464, 14945, 428,
  14310, 11, 428, 21264, 11, 293, 428, 1651, 13, 50574], "temperature": 0.0, "avg_logprob":
  -0.16757558254485436, "compression_ratio": 1.6036866359447004, "no_speech_prob":
  0.25533971190452576}, {"id": 562, "seek": 116904, "start": 1173.24, "end": 1174.24,
  "text": " We''re all ears.", "tokens": [50574, 492, 434, 439, 8798, 13, 50624],
  "temperature": 0.0, "avg_logprob": -0.16757558254485436, "compression_ratio": 1.6036866359447004,
  "no_speech_prob": 0.25533971190452576}, {"id": 563, "seek": 116904, "start": 1174.24,
  "end": 1176.32, "text": " We''re always eager to continue the conversation.", "tokens":
  [50624, 492, 434, 1009, 18259, 281, 2354, 264, 3761, 13, 50728], "temperature":
  0.0, "avg_logprob": -0.16757558254485436, "compression_ratio": 1.6036866359447004,
  "no_speech_prob": 0.25533971190452576}, {"id": 564, "seek": 116904, "start": 1176.32,
  "end": 1180.6, "text": " Until next time, keep exploring, keep innovating, and keep
  diving deep into the fascinating", "tokens": [50728, 9088, 958, 565, 11, 1066, 12736,
  11, 1066, 5083, 990, 11, 293, 1066, 20241, 2452, 666, 264, 10343, 50942], "temperature":
  0.0, "avg_logprob": -0.16757558254485436, "compression_ratio": 1.6036866359447004,
  "no_speech_prob": 0.25533971190452576}, {"id": 565, "seek": 116904, "start": 1180.6,
  "end": 1182.68, "text": " world of AI.", "tokens": [50942, 1002, 295, 7318, 13,
  51046], "temperature": 0.0, "avg_logprob": -0.16757558254485436, "compression_ratio":
  1.6036866359447004, "no_speech_prob": 0.25533971190452576}, {"id": 566, "seek":
  116904, "start": 1182.68, "end": 1184.8, "text": " That''s a wrap on this deep dive,
  folks.", "tokens": [51046, 663, 311, 257, 7019, 322, 341, 2452, 9192, 11, 4024,
  13, 51152], "temperature": 0.0, "avg_logprob": -0.16757558254485436, "compression_ratio":
  1.6036866359447004, "no_speech_prob": 0.25533971190452576}, {"id": 567, "seek":
  116904, "start": 1184.8, "end": 1186.84, "text": " We hope you''ve enjoyed the journey
  as much as we have.", "tokens": [51152, 492, 1454, 291, 600, 4626, 264, 4671, 382,
  709, 382, 321, 362, 13, 51254], "temperature": 0.0, "avg_logprob": -0.16757558254485436,
  "compression_ratio": 1.6036866359447004, "no_speech_prob": 0.25533971190452576}]'
---

Welcome back everybody. Today, we're gonna be diving into the world of vector databases. Ooh, fun. They're rise, they're potential fall, and with the future holds. Okay. You know, you sent us this fascinating medium article to kind of guide our exploration. Ooh.
Called The Rise, Fall, and Future of Vector Databases. How to pick the one that lasts by Dimitri Can. Yeah, I saw that one. Published January 6th, 2025. Mm-hmm. So guess the term vector database might actually be on its way out.
Really? And your choice of database could hinge on needing things like faceted search. Oh, wow. Or even those super cool late interaction models. Huh, interesting. And treat. I know I am. Let's break it all down. Okay, let's do it. So it's gonna be good.
What I thought was so interesting about this article is how it really blends like the technical side with the broader AI landscape. Yeah, you're right. It's not just about the nuts and bolts. It's about how perceptions and adoption of vector databases are shifting within the AI world. Absolutely.
Like this is not just a technical deep dive. Right. This is about how people are thinking about these things. Yeah. And using them. Totally. And Dimitri brings this really unique perspective He does. to this whole conversation.
Because he was like deeply involved in this emerging market just a few years back. Oh, really? He was even advising VCs on which vector database companies to back. Wow. So he's like an insider. Yeah, he's got the inside scoop. So he really saw this whole thing unfold firsthand.
He was there from the beginning. Wow, that's amazing. And it's interesting because just a few years ago, vector databases were like the hot topic. They were everywhere, right? Everybody was talking about it. Like they were the key to unlocking all these powerful AI applications.
Like this was gonna change everything. Everyone was so excited. Yeah. Okay, so let's unpack this whole rise and fall idea. Okay. So Dimitri noticed something interesting. What's up? Fewer people were reading his early articles about vector databases. Oh, really? Huh? I wonder why.
What do you make of that? Well, you know, it kind of hints at a potential shift in the industry. Okay. Instead of being seen as these like standalone solutions, it seems like vector search technology is kind of merging with other AI advancements, becoming part of a bigger picture.
Like what? Think LLM, small time modal search. They're all getting more integrated. Okay, so it's not that vector databases are like vanishing. Right. They're evolving. Exactly. I'm blending into more comprehensive solutions. That's it. Okay, I got it. The technology itself is still crucial.
But how we think about it and use it is evolving. Okay. Like, you know, you have your traditional databases, right? Like your SQL and no SQL types. Well, a lot of them have integrated vector search capabilities now. Oh, wow.
So the data type itself is becoming normalized within these existing systems. Okay. I see. So it's becoming more commonplace. Yeah. Exactly. It's not this like niche thing anymore. Right. It's just part of the toolkit. It's becoming part of the fabric of how we work with data.
I like that fabric of how we work with data. It's a good way to put it right. But here's where things get really interesting. Okay. Tell me. Dimitri saw this resurgence in views for those older articles. Oh, so people are coming back to them.
They're coming back and guess what? What? We've been right when major funding announcements hit for some vector database startups back in April 2023. Oh, interesting. Like, big money was flowing back into this space. Yeah. Like, pine cones, $100 million series B. Yeah. Pine cone was huge.
Weve 8 securing $50 million. Huh. And QDran getting $7.5 million in seed funding. Yeah. Those were big headlines. They were. It really highlights how much media coverage and industry buzz can influence how we perceive technology trends. Codally. It's like a self-fulfilling prophecy almost. Yeah.
And it makes you think like how much of what we perceive is like the next big thing is actually driven by, you know, the hype, the hype, the funding, the media attention. Yeah. It's fascinating. So clearly, there's still a ton of innovation and investment happening in the vector database space.
Be sure. But let's get practical for our listener out there. Let's give him some actionable advice. The real gem in this article is Demetri's guide for choosing the right vector database. Right. Because there's no one size fits all solution. Exactly. It really depends on your specific needs.
It's like having a roadmap for navigating this complex landscape. Totally a roadmap. So where does he suggest starting? Okay. I'm ready. His secret weapon is, FAYS. Okay. No, it's not technically a full-fledged database. Right. It's more of a powerful library. Okay.
So the kicker, it can handle massive data sets. Okay. We're talking over a billion vectors. Wow. That's a lot. So it can scale. We can handle the big stuff. And the beauty of FAYS is its simplicity and scalability. So it's perfect for, it's perfect for initial exploration and prototyping.
You can just get in there and start playing around. Exactly. Yeah. But of course, uh oh, there's always a butt. There's a trade-off. Okay. What is it? Built-in filtering capabilities. Uh, so you can't really do that fine-grained search. Right. Like with keywords and stuff.
Which might mean getting creative with workarounds? Okay. So you've got to be a little clever. A little bit. If you want to use FAYS, I.S. for certain things. Yeah. So if you need that fine-grained controlled keyword search. Yeah.
Along with your vector search, what does Demetri recommend? I'm all ears. He suggests looking at databases built on top of Lucene. Lucene. Options like open search, elastic search, and a patchy solar. Got it. So these are all built on this like solid foundation of Lucene technology. Yeah.
Lucene's been around for a while, right? It's a mature technology with a proven track record. Yeah. So it's reliable. Reliable. Yeah. And it provides that robust keyword search. Okay. You mentioned plus multilingual support. That's important these days. Super important.
And it performs incredibly well. So it's fast and efficient. Nice. This makes it particularly well suited for e-commerce. Oh, interesting why e-commerce? Where features like faceting, which allows users to refine their search by specific attributes. Oh, I see. So like filtering by brands. Yeah.
Like filtering by brand. Price range. Price range size. All those things are essential. Makes sense for e-commerce. He did mention one exception though, right? Though there's always an exception. What is it? Cudrant, even though it's not built on Lucene. Oh, okay. Includes fascinating capabilities.
Interesting. So it's kind of a hybrid approach. Making it a contender in those scenarios too. So Cudrant's kind of a wild card. A little bit. Yeah. It's got its own unique set of features. And it shows the importance of going beyond general categories. Yeah.
And really digging into the specific features each database offers. Absolutely. You can't just like assume that because it's in one category. Right. It's got all the features you need. You got to do your research. You got to look under the hood. Exactly.
Now what if you need something more advanced? Okay. Like what? Like support for those late interaction models. Late interaction models, huh? Yeah. If you heard of these. I've heard the term, but I'm not really sure what they were. Okay. So imagine you're searching for the perfect pair of red shoes.
Okay. I like shoes. But only after you've seen a picture of the outfit you want them to match. Oh, I see. So like the context of the search changes. Exactly. And then you see something you see later on. That's where late interaction models come in. Okay.
Allowing you to refine your search based on context that's only available later in the process. So it's like a more dynamic way of searching. It is a more dynamic way of searching. Interesting. And it requires a different level of database support. I bet.
And Dmitry points to QDrent or Vespa as potential solutions. Okay. So they can handle those late interactions. Because they offer that support natively. So you don't have to hack it together yourself. Exactly. That's good to know.
So choosing a database that can handle those complexities is critical for performance and efficiency. You don't want your search to be slow and clunky. Especially if you're dealing with a lot of data. Right. Or if you need those results in real time. But it doesn't stop there. There's more.
The next step into Dmitry's roadmap is super important. Okay. Hit me. Considering latency. Latency, okay. And those query per second abans? Oh, yes. QPS. Can make or break your application? You're telling me. If your database is slow. Yeah. Or it can't handle the volume of queries.
It's going to be a bad experience for the user. It's going to be a disaster. So you've got to think about those things up front. Absolutely. And choose a database that can handle the load. If high performance is the name of the game. Yeah.
You'll want to explore solutions like GSI, APU, Vespa, or hyperspace. Got it. In fact, Dmitry even shared an anecdote about a CTO. Oh, I love a good anecdote. You'll confess that no open source vector database could handle their extreme workload. Wow. So they had to go with a commercial solution.
They'd find something else. That's interesting. Choosing wisely is essential. You can't just pick the first one you see. No. You got to your homework. And think about your long term needs. So the takeaway here is you need to think strategically. Yep.
Do you invest the engineering time to set up and maintain an open source database? Right. Or do you go with the convenience and potentially higher costs of a cloud solution? Right. It's a classic trade off. There's no right or wrong answer. It depends on your situation.
It's all about finding the balance that works best for your specific situation. Absolutely. And there are a lot of great cloud and API based options out there. Like what? Like Cosmos DB, Vertex AI, Pine Cone Cloud, Weeveate Cloud, and other. But there's no shortage of options.
There's a lot to choose from. It's a good problem to have, right? It is a good problem to have. Better than having no options at all. And we love hearing from our community. Oh yes, our listeners are the best. One reader, Matt Collins, suggested exploring extensions like PG Vector.
Did you vector? Okay. Which adds vector search to Postgresql. Oh, so you can just add it onto your existing Postgres database. Exactly. That's pretty cool. It's a really clever solution. You have to rip and replace your whole infrastructure.
And it speaks to the constantly evolving nature of the vector database landscape. It's a fast moving field. There's always something new happening. You've been in new solutions emerging. Speaking of evolution. Oh, this is where it gets really interesting.
Dimitri paints a fascinating picture of the future. I can't wait to hear this. He believes the future lies in what he calls neural search frameworks. Oh, wow. These frameworks could revolutionize how we build AI-powered applications. Okay.
And then we have a system that streamlines the entire process from data modeling and embedding selection to evaluation and scaling.
So instead of wrestling with the complexities of choosing and integrating all the different components, it would be like having an intelligent assistant guiding you through building a search application no matter what database technology you're using. Exactly.
And this vision ties in nicely with the concept of compound AI systems. Oh, interesting. So where LLMs vector databases and other AI components work together like a well coordinated orchestra. So instead of focusing on the individual instruments, you're conducting the entire symphony. Precisely.
I love that analogy. Users can then focus on the task they're trying to solve, rather than the technical nuts and bolts. So it's about abstracting away the complexity and empowering users to focus on the bigger picture. It's about making AI more accessible and user friendly.
It's fascinating how this all connects to those funding announcements we talked about earlier. Right. It seems like the industry might be moving towards a more unified approach to AI solutions. That's a keen observation. While individual components like vector databases are still important.
For sure. The future might be about how these pieces fit into a larger ecosystem. Yeah, it's all about the big picture. This brings us to an interesting question for you, the listener. Oh, yes. Let's get our listeners involved.
Do you see neural search frameworks as a complete paradigm shift? Or will specialized vector databases continue to have a distinct role to play? It's tough question. It's something to think about. Let us know your thoughts in the comments. We'd love to hear from you.
But before we get too caught up in the future, let's take a step back and revisit one of Dmitry's key points about the impact of media coverage on perceptions of technology trends. Right. That was a really important point.
It's a crucial reminder to be discerning consumers of information, especially in a field as dynamic as AI, where innovation is constant. What might seem like a decline could actually be a natural evolution. Interesting. As a technology matures and finds its place within a larger ecosystem. Right.
Like a caterpillar transforming into a butterfly. That's a wonderful analogy. It's still the same creature, just in a more advanced and beautiful form. It underscores the importance of staying curious, continuing to explore, and never assuming that any technology is truly dead.
Because it might just be evolving into something even better. Who knows what exciting developments await us in the world of vector databases? I'm definitely eager to see what the future holds. E2. This deep dive has given me a whole new perspective. I'm sure it has for our listeners as well.
You know, as we're discussing this, it strikes me that Dmitry's journey with vector databases mirrors a broader trend in the tech world. Oh, how so? We often get caught up in the hype cycle. Oh, yeah, for sure.
But true innovation often emerges when technologies evolve and integrate in unexpected ways. It's like that saying the whole is greater than the sum of its parts. And that brings us to another crucial point from the article. Okay. One that I think holds immense value for our listeners today.
I'm all ears. Remember how Dmitry emphasized that it's not just about the vectors themselves. It's about understanding the nuances of data pre-processing model selection and bedding techniques. And even knowing when to switch back to traditional keyword search for certain tasks.
Yeah, sometimes the old ways are still the best. He's advocating for a more holistic approach where vector databases are seen as one tool among many in the AI toolbox. So it's not a silver bullet. It's not a magic solution. It's one piece of the puzzle. Exactly.
There is a deeper understanding of the underlying principles, not just blindly applying the latest trendy technology. Right. It's about making informed choices based on a thorough analysis of your specific needs and constraints. So don't just jump on the bandwagon.
Do your research and figure out what's right for you. So for those of you out there exploring AI solutions, don't get fixated on buzzwords. Take the time to really grasp the fundamentals. Understand the basics. Experiment with different approaches. Stay around with different tools.
And don't be afraid to challenge assumptions. Question everything. And remember, the AI landscape is constantly evolving. What works best today might be superseded by something even more powerful and efficient tomorrow. So stay curious. They engage. And keep learning.
Couldn't have said it better myself. Well folks, that brings us to the end of our deep dive into the world of vector databases. It's been a wild ride. We've explored their rise, their potential fall, and the exciting possibilities of neural search frameworks. We've covered a lot of ground.
We've also learned some valuable lessons about navigating the hype cycle and making informed decisions in a rapidly changing technological landscape. It's been a fascinating journey. Absolutely. And we hope you've enjoyed it as much as we have. Until next time. Keep exploring. Keep questioning.
And keep that thirst for knowledge alive. It's funny actually while we're focused on all this cutting edge tech, Dimitri actually kind of throws it back to basics in the article a little bit. Oh yeah, I remember that part.
He recounts this conversation he had with the chief data scientist at a major bank. That was a good one, which I thought was so interesting because it really emphasizes how even with all these advancements, sometimes the simplest solution is the best one. You don't always need the fanciest tools.
Right. Sometimes it's about using the right tool for the job. Exactly. This bank had poured resources into building this complex vector search system. Okay. But guess what? What? They ended up getting better results with good old fashioned keyword search. Really? For some very specific tasks. Huh.
So even the big bangs are going back to basics sometimes. Sometimes it makes more sense. Yeah. It's a powerful reminder that we shouldn't dismiss those tried and true methods. Like don't throw out the baby with the bathwater. Right. Exactly.
The tools when used strategically can outperform the flashiest new tech. It's all about choosing the right tool for the job. It's like trying to use a chainsaw to cut a piece of paper. Oof. Yeah, that wouldn't end well. Sometimes a simple pair of scissors does the job better. Much better.
And that brings us back to Dimitri's vision of neural search frameworks. Okay. If they become a reality. Yeah. Could they simplify these choices for us? Interesting question.
Would they be able to determine the best approach? Like whether it's vector search, keyword search or a hybrid based on the task at hand. That's the dream. How be amazed? It would be like having this AI assistant that just knows the best way to search for anything. That's a fantastic question.
It really gets to the heart of what these frameworks could potentially offer. Like a more intelligent and adaptable approach to search. So instead of us having to figure it all out. Yeah. The system would just do it for us.
A vision of system that not only combines different AI components, but also understands which tool is best suited for each specific task. That would be a game changer. It would free us from getting bogged down in the technical details and allow us to focus on solving real world problems.
It's all about making AI work for us. Not the other way around. Exactly. And it highlights the importance of staying flexible and open to new possibilities. As the AI landscape continues to evolve, we need to be willing to adapt and embrace new approaches.
Even if the challenger existing assumptions. Challenge the status quo. Right. Well said, well, this deep dive has been a whirlwind of information. It has. But I think the biggest takeaway for me is that the world of vector databases and AI in general is anything but static.
It's constantly changing. It's a constantly evolving landscape full of exciting possibilities and unexpected twists in turn. You never know what's going to come next. And that's what makes it so exciting. I completely agree. And it's a landscape that requires us to stay curious. Keep learning.
And never stop asking questions. And on that note, we'd love to hear from you, our listeners. Yes, please share your thoughts. What are your thoughts on the future of vector databases? Hmm.
Do you think neural search frameworks will revolutionize the way we build AI applications? That's the big question. Share your insights, your predictions, and your questions. We're all ears. We're always eager to continue the conversation.
Until next time, keep exploring, keep innovating, and keep diving deep into the fascinating world of AI. That's a wrap on this deep dive, folks. We hope you've enjoyed the journey as much as we have.