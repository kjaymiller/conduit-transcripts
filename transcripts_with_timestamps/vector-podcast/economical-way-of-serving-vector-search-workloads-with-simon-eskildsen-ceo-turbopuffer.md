---
description: '<p>Turbopuffer search engine supports such products as Cursor, Notion,
  Linear, Superhuman and Readwise.</p><p></p><p>This episode on YouTube: <a target="_blank"
  rel="noopener noreferrer nofollow" href="https://youtu.be/I8Ztqajighg">https://youtu.be/I8Ztqajighg</a></p><p>Medium:
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://dmitry-kan.medium.com/vector-podcast-simon-eskildsen-turbopuffer-69e456da8df3">https://dmitry-kan.medium.com/vector-podcast-simon-eskildsen-turbopuffer-69e456da8df3</a></p><p>Dev:
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://dev.to/vectorpodcast/vector-podcast-simon-eskildsen-turbopuffer-cfa">https://dev.to/vectorpodcast/vector-podcast-simon-eskildsen-turbopuffer-cfa</a></p><p></p><p>If
  you are on Lucene / OpenSearch stack, you can go managed by signing up here: <a
  target="_blank" rel="noopener noreferrer nofollow" href="https://console.aiven.io/signup?utm_source=youtube&amp;utm_medium=&amp;&amp;utm_content=vectorpodcast">https://console.aiven.io/signup?utm_source=youtube&amp;utm_medium=&amp;&amp;utm_content=vectorpodcast</a></p><p></p><p>Time
  codes:</p><p>00:00 Intro</p><p>00:15 Napkin Problem 4: Throughput of Redis</p><p>01:35
  Episode intro</p><p>02:45 Simon''s background, including implementation of Turbopuffer</p><p>09:23
  How Cursor became an early client</p><p>11:25 How to test pre-launch</p><p>14:38
  Why a new vector DB deserves to exist?</p><p>20:39 Latency aspect</p><p>26:27 Implementation
  language for Turbopuffer</p><p>28:11 Impact of LLM coding tools on programmer craft</p><p>30:02
  Engineer 2 CEO transition</p><p>35:10 Architecture of Turbopuffer</p><p>43:25 Disk
  vs S3 latency, NVMe disks, DRAM</p><p>48:27 Multitenancy</p><p>50:29 Recall@N benchmarking</p><p>59:38
  filtered ANN and Big-ANN Benchmarks</p><p>1:00:54 What users care about more (than
  Recall@N benchmarking)</p><p>1:01:28 Spicy question about benchmarking in competition</p><p>1:06:01
  Interesting challenges ahead to tackle</p><p>1:10:13 Simon''s announcement</p><p></p><p>Show
  notes:</p><p>- Turbopuffer in Cursor: <a target="_blank" rel="noopener noreferrer
  nofollow" href="https://www.youtube.com/watch?v=oFfVt3S51T4&amp;t=5223s">https://www.youtube.com/watch?v=oFfVt3S51T4&amp;t=5223s</a></p><p>transcript:
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://lexfridman.com/cursor-team-transcript">https://lexfridman.com/cursor-team-transcript</a></p><p>-
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://turbopuffer.com/">https://turbopuffer.com/</a></p><p>-
  Napkin Math: <a target="_blank" rel="noopener noreferrer nofollow" href="https://sirupsen.com/napkin">https://sirupsen.com/napkin</a></p><p>-
  Follow Simon on X: <a target="_blank" rel="noopener noreferrer nofollow" href="https://x.com/Sirupsen">https://x.com/Sirupsen</a></p><p>-
  Not All Vector Databases Are Made Equal: <a target="_blank" rel="noopener noreferrer
  nofollow" href="https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696/">https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696/</a></p>'
image_url: https://media.rss.com/vector-podcast/ep_cover_20250919_060954_7832a7c20742f9493a19a27a0c5d8947.png
pub_date: Fri, 19 Sep 2025 06:09:39 GMT
title: Economical way of serving vector search workloads with Simon Eskildsen, CEO
  Turbopuffer
url: https://rss.com/podcasts/vector-podcast/2222846
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 16.28, "text": " Now,
  let''s get started.", "tokens": [50364, 823, 11, 718, 311, 483, 1409, 13, 51178],
  "temperature": 0.0, "avg_logprob": -0.8359620445653012, "compression_ratio": 1.1228070175438596,
  "no_speech_prob": 0.049298979341983795}, {"id": 1, "seek": 0, "start": 16.28, "end":
  18.28, "text": " MAPKIN Problem 4", "tokens": [51178, 376, 4715, 42, 1464, 11676,
  1017, 51278], "temperature": 0.0, "avg_logprob": -0.8359620445653012, "compression_ratio":
  1.1228070175438596, "no_speech_prob": 0.049298979341983795}, {"id": 2, "seek": 0,
  "start": 18.28, "end": 24.44, "text": " Today, as you are preparing your organic,
  high mountain type needs along in the kitchen", "tokens": [51278, 2692, 11, 382,
  291, 366, 10075, 428, 10220, 11, 1090, 6937, 2010, 2203, 2051, 294, 264, 6525, 51586],
  "temperature": 0.0, "avg_logprob": -0.8359620445653012, "compression_ratio": 1.1228070175438596,
  "no_speech_prob": 0.049298979341983795}, {"id": 3, "seek": 2444, "start": 24.44,
  "end": 25.560000000000002, "text": " net.", "tokens": [50364, 2533, 13, 50420],
  "temperature": 0.0, "avg_logprob": -0.21295687916514638, "compression_ratio": 1.5560344827586208,
  "no_speech_prob": 0.08836518973112106}, {"id": 4, "seek": 2444, "start": 25.560000000000002,
  "end": 30.64, "text": " One of your lovely co-workers mentioned that they were looking
  at adding more radices because", "tokens": [50420, 1485, 295, 428, 7496, 598, 12,
  37101, 2835, 300, 436, 645, 1237, 412, 5127, 544, 2843, 1473, 570, 50674], "temperature":
  0.0, "avg_logprob": -0.21295687916514638, "compression_ratio": 1.5560344827586208,
  "no_speech_prob": 0.08836518973112106}, {"id": 5, "seek": 2444, "start": 30.64,
  "end": 37.08, "text": " it was maxing out at 10,000 commands per second, which they
  were trending aggressively towards.", "tokens": [50674, 309, 390, 11469, 278, 484,
  412, 1266, 11, 1360, 16901, 680, 1150, 11, 597, 436, 645, 28692, 32024, 3030, 13,
  50996], "temperature": 0.0, "avg_logprob": -0.21295687916514638, "compression_ratio":
  1.5560344827586208, "no_speech_prob": 0.08836518973112106}, {"id": 6, "seek": 2444,
  "start": 37.08, "end": 39.08, "text": " You asked them how they were using it.",
  "tokens": [50996, 509, 2351, 552, 577, 436, 645, 1228, 309, 13, 51096], "temperature":
  0.0, "avg_logprob": -0.21295687916514638, "compression_ratio": 1.5560344827586208,
  "no_speech_prob": 0.08836518973112106}, {"id": 7, "seek": 2444, "start": 39.08,
  "end": 42.96, "text": " Were they writing some obscure order and command?", "tokens":
  [51096, 12448, 436, 3579, 512, 34443, 1668, 293, 5622, 30, 51290], "temperature":
  0.0, "avg_logprob": -0.21295687916514638, "compression_ratio": 1.5560344827586208,
  "no_speech_prob": 0.08836518973112106}, {"id": 8, "seek": 2444, "start": 42.96,
  "end": 50.6, "text": " They would BPF probes to determine that it was all get key
  and set key value.", "tokens": [51290, 814, 576, 40533, 37, 1239, 279, 281, 6997,
  300, 309, 390, 439, 483, 2141, 293, 992, 2141, 2158, 13, 51672], "temperature":
  0.0, "avg_logprob": -0.21295687916514638, "compression_ratio": 1.5560344827586208,
  "no_speech_prob": 0.08836518973112106}, {"id": 9, "seek": 5060, "start": 50.6, "end":
  55.760000000000005, "text": " They also confirmed all the values were about less
  than 64 bytes.", "tokens": [50364, 814, 611, 11341, 439, 264, 4190, 645, 466, 1570,
  813, 12145, 36088, 13, 50622], "temperature": 0.0, "avg_logprob": -0.26877395552818223,
  "compression_ratio": 1.5158730158730158, "no_speech_prob": 0.002365718362852931},
  {"id": 10, "seek": 5060, "start": 55.760000000000005, "end": 60.96, "text": " For
  those unfamiliar with radices, it''s single threaded in memory key value store written",
  "tokens": [50622, 1171, 729, 29415, 365, 2843, 1473, 11, 309, 311, 2167, 47493,
  294, 4675, 2141, 2158, 3531, 3720, 50882], "temperature": 0.0, "avg_logprob": -0.26877395552818223,
  "compression_ratio": 1.5158730158730158, "no_speech_prob": 0.002365718362852931},
  {"id": 11, "seek": 5060, "start": 60.96, "end": 61.96, "text": " in C.", "tokens":
  [50882, 294, 383, 13, 50932], "temperature": 0.0, "avg_logprob": -0.26877395552818223,
  "compression_ratio": 1.5158730158730158, "no_speech_prob": 0.002365718362852931},
  {"id": 12, "seek": 5060, "start": 61.96, "end": 66.8, "text": " And faced, after
  this encounter, you walk to the window.", "tokens": [50932, 400, 11446, 11, 934,
  341, 8593, 11, 291, 1792, 281, 264, 4910, 13, 51174], "temperature": 0.0, "avg_logprob":
  -0.26877395552818223, "compression_ratio": 1.5158730158730158, "no_speech_prob":
  0.002365718362852931}, {"id": 13, "seek": 5060, "start": 66.8, "end": 70.72, "text":
  " You look out and see if your high mountain type needs along.", "tokens": [51174,
  509, 574, 484, 293, 536, 498, 428, 1090, 6937, 2010, 2203, 2051, 13, 51370], "temperature":
  0.0, "avg_logprob": -0.26877395552818223, "compression_ratio": 1.5158730158730158,
  "no_speech_prob": 0.002365718362852931}, {"id": 14, "seek": 5060, "start": 70.72,
  "end": 76.48, "text": " As you stare at yet another condominium building being built,
  it hits you.", "tokens": [51370, 1018, 291, 22432, 412, 1939, 1071, 2224, 6981,
  2197, 2390, 885, 3094, 11, 309, 8664, 291, 13, 51658], "temperature": 0.0, "avg_logprob":
  -0.26877395552818223, "compression_ratio": 1.5158730158730158, "no_speech_prob":
  0.002365718362852931}, {"id": 15, "seek": 5060, "start": 76.48, "end": 79.48, "text":
  " 10,000 commands per second.", "tokens": [51658, 1266, 11, 1360, 16901, 680, 1150,
  13, 51808], "temperature": 0.0, "avg_logprob": -0.26877395552818223, "compression_ratio":
  1.5158730158730158, "no_speech_prob": 0.002365718362852931}, {"id": 16, "seek":
  7948, "start": 79.48, "end": 80.48, "text": " 10,000.", "tokens": [50364, 1266,
  11, 1360, 13, 50414], "temperature": 0.0, "avg_logprob": -0.4315867216690727, "compression_ratio":
  1.3822222222222222, "no_speech_prob": 0.1362903118133545}, {"id": 17, "seek": 7948,
  "start": 80.48, "end": 83.72, "text": " Isn''t that a bit low?", "tokens": [50414,
  6998, 380, 300, 257, 857, 2295, 30, 50576], "temperature": 0.0, "avg_logprob": -0.4315867216690727,
  "compression_ratio": 1.3822222222222222, "no_speech_prob": 0.1362903118133545},
  {"id": 18, "seek": 7948, "start": 83.72, "end": 90.44, "text": " Shouldn''t something
  that''s fundamentally just doing random memory reads and writes over", "tokens":
  [50576, 34170, 380, 746, 300, 311, 17879, 445, 884, 4974, 4675, 15700, 293, 13657,
  670, 50912], "temperature": 0.0, "avg_logprob": -0.4315867216690727, "compression_ratio":
  1.3822222222222222, "no_speech_prob": 0.1362903118133545}, {"id": 19, "seek": 7948,
  "start": 90.44, "end": 95.04, "text": " an established TCP session be able to do
  more?", "tokens": [50912, 364, 7545, 48965, 5481, 312, 1075, 281, 360, 544, 30,
  51142], "temperature": 0.0, "avg_logprob": -0.4315867216690727, "compression_ratio":
  1.3822222222222222, "no_speech_prob": 0.1362903118133545}, {"id": 20, "seek": 7948,
  "start": 95.04, "end": 96.04, "text": " Hello there.", "tokens": [51142, 2425, 456,
  13, 51192], "temperature": 0.0, "avg_logprob": -0.4315867216690727, "compression_ratio":
  1.3822222222222222, "no_speech_prob": 0.1362903118133545}, {"id": 21, "seek": 7948,
  "start": 96.04, "end": 98.08000000000001, "text": " Vector podcast is back.", "tokens":
  [51192, 691, 20814, 7367, 307, 646, 13, 51294], "temperature": 0.0, "avg_logprob":
  -0.4315867216690727, "compression_ratio": 1.3822222222222222, "no_speech_prob":
  0.1362903118133545}, {"id": 22, "seek": 7948, "start": 98.08000000000001, "end":
  100.04, "text": " Season 4.", "tokens": [51294, 16465, 1017, 13, 51392], "temperature":
  0.0, "avg_logprob": -0.4315867216690727, "compression_ratio": 1.3822222222222222,
  "no_speech_prob": 0.1362903118133545}, {"id": 23, "seek": 7948, "start": 100.04,
  "end": 105.96000000000001, "text": " And we are kicking off with an exciting topic
  and guest assignment, Eskulls and CEO of", "tokens": [51392, 400, 321, 366, 19137,
  766, 365, 364, 4670, 4829, 293, 8341, 15187, 11, 2313, 74, 858, 82, 293, 9282, 295,
  51688], "temperature": 0.0, "avg_logprob": -0.4315867216690727, "compression_ratio":
  1.3822222222222222, "no_speech_prob": 0.1362903118133545}, {"id": 24, "seek": 7948,
  "start": 105.96000000000001, "end": 106.96000000000001, "text": " TurboPuffer.",
  "tokens": [51688, 35848, 47, 1245, 260, 13, 51738], "temperature": 0.0, "avg_logprob":
  -0.4315867216690727, "compression_ratio": 1.3822222222222222, "no_speech_prob":
  0.1362903118133545}, {"id": 25, "seek": 10696, "start": 107.36, "end": 113.19999999999999,
  "text": " I''ve been watching you guys from almost from the start, just following
  each other on", "tokens": [50384, 286, 600, 668, 1976, 291, 1074, 490, 1920, 490,
  264, 722, 11, 445, 3480, 1184, 661, 322, 50676], "temperature": 0.0, "avg_logprob":
  -0.3795521384791324, "compression_ratio": 1.612, "no_speech_prob": 0.6404481530189514},
  {"id": 26, "seek": 10696, "start": 113.19999999999999, "end": 115.75999999999999,
  "text": " Twitter, like virtual friends.", "tokens": [50676, 5794, 11, 411, 6374,
  1855, 13, 50804], "temperature": 0.0, "avg_logprob": -0.3795521384791324, "compression_ratio":
  1.612, "no_speech_prob": 0.6404481530189514}, {"id": 27, "seek": 10696, "start":
  115.75999999999999, "end": 119.63999999999999, "text": " And it''s funny that before
  this episode, you''re the CEO of the company and this for this", "tokens": [50804,
  400, 309, 311, 4074, 300, 949, 341, 3500, 11, 291, 434, 264, 9282, 295, 264, 2237,
  293, 341, 337, 341, 50998], "temperature": 0.0, "avg_logprob": -0.3795521384791324,
  "compression_ratio": 1.612, "no_speech_prob": 0.6404481530189514}, {"id": 28, "seek":
  10696, "start": 119.63999999999999, "end": 125.56, "text": " episode, you try to
  sell TurboPuffer to me and say, hey, why don''t you use it?", "tokens": [50998,
  3500, 11, 291, 853, 281, 3607, 35848, 47, 1245, 260, 281, 385, 293, 584, 11, 4177,
  11, 983, 500, 380, 291, 764, 309, 30, 51294], "temperature": 0.0, "avg_logprob":
  -0.3795521384791324, "compression_ratio": 1.612, "no_speech_prob": 0.6404481530189514},
  {"id": 29, "seek": 10696, "start": 125.56, "end": 128.35999999999999, "text": "
  Did you make a compound tom should pass?", "tokens": [51294, 2589, 291, 652, 257,
  14154, 2916, 820, 1320, 30, 51434], "temperature": 0.0, "avg_logprob": -0.3795521384791324,
  "compression_ratio": 1.612, "no_speech_prob": 0.6404481530189514}, {"id": 30, "seek":
  10696, "start": 128.35999999999999, "end": 132.2, "text": " Yeah, should pass, for
  sure.", "tokens": [51434, 865, 11, 820, 1320, 11, 337, 988, 13, 51626], "temperature":
  0.0, "avg_logprob": -0.3795521384791324, "compression_ratio": 1.612, "no_speech_prob":
  0.6404481530189514}, {"id": 31, "seek": 10696, "start": 132.2, "end": 134.68, "text":
  " But tell me, hey, welcome, first of all, welcome.", "tokens": [51626, 583, 980,
  385, 11, 4177, 11, 2928, 11, 700, 295, 439, 11, 2928, 13, 51750], "temperature":
  0.0, "avg_logprob": -0.3795521384791324, "compression_ratio": 1.612, "no_speech_prob":
  0.6404481530189514}, {"id": 32, "seek": 13468, "start": 134.68, "end": 139.48000000000002,
  "text": " And thank you very much for having with me.", "tokens": [50364, 400, 1309,
  291, 588, 709, 337, 1419, 365, 385, 13, 50604], "temperature": 0.0, "avg_logprob":
  -0.29737889188007244, "compression_ratio": 1.5413533834586466, "no_speech_prob":
  0.3278094530105591}, {"id": 33, "seek": 13468, "start": 139.48000000000002, "end":
  142.36, "text": " It''s a tradition to usually start with the background.", "tokens":
  [50604, 467, 311, 257, 6994, 281, 2673, 722, 365, 264, 3678, 13, 50748], "temperature":
  0.0, "avg_logprob": -0.29737889188007244, "compression_ratio": 1.5413533834586466,
  "no_speech_prob": 0.3278094530105591}, {"id": 34, "seek": 13468, "start": 142.36,
  "end": 146.08, "text": " If you could speak in your own words about yourself, your
  journey.", "tokens": [50748, 759, 291, 727, 1710, 294, 428, 1065, 2283, 466, 1803,
  11, 428, 4671, 13, 50934], "temperature": 0.0, "avg_logprob": -0.29737889188007244,
  "compression_ratio": 1.5413533834586466, "no_speech_prob": 0.3278094530105591},
  {"id": 35, "seek": 13468, "start": 146.08, "end": 152.96, "text": " I know that
  you''ve worked at Shopify at some point, also scaling databases, I guess, right?",
  "tokens": [50934, 286, 458, 300, 291, 600, 2732, 412, 43991, 412, 512, 935, 11,
  611, 21589, 22380, 11, 286, 2041, 11, 558, 30, 51278], "temperature": 0.0, "avg_logprob":
  -0.29737889188007244, "compression_ratio": 1.5413533834586466, "no_speech_prob":
  0.3278094530105591}, {"id": 36, "seek": 13468, "start": 152.96, "end": 156.4, "text":
  " But I''ve also been following your napkin math newsletter.", "tokens": [51278,
  583, 286, 600, 611, 668, 3480, 428, 9296, 5843, 5221, 26469, 13, 51450], "temperature":
  0.0, "avg_logprob": -0.29737889188007244, "compression_ratio": 1.5413533834586466,
  "no_speech_prob": 0.3278094530105591}, {"id": 37, "seek": 13468, "start": 156.4,
  "end": 164.28, "text": " I was reading maybe I''ll quote some text today from there,
  just to amuse an exciting audience.", "tokens": [51450, 286, 390, 3760, 1310, 286,
  603, 6513, 512, 2487, 965, 490, 456, 11, 445, 281, 669, 438, 364, 4670, 4034, 13,
  51844], "temperature": 0.0, "avg_logprob": -0.29737889188007244, "compression_ratio":
  1.5413533834586466, "no_speech_prob": 0.3278094530105591}, {"id": 38, "seek": 16428,
  "start": 164.28, "end": 166.28, "text": " But tell me about yourself.", "tokens":
  [50364, 583, 980, 385, 466, 1803, 13, 50464], "temperature": 0.0, "avg_logprob":
  -0.2525026213448003, "compression_ratio": 1.5968992248062015, "no_speech_prob":
  0.15724892914295197}, {"id": 39, "seek": 16428, "start": 166.28, "end": 172.76,
  "text": " Yeah, I can give a very brief overview and if we can dig into anything,
  if there''s anything", "tokens": [50464, 865, 11, 286, 393, 976, 257, 588, 5353,
  12492, 293, 498, 321, 393, 2528, 666, 1340, 11, 498, 456, 311, 1340, 50788], "temperature":
  0.0, "avg_logprob": -0.2525026213448003, "compression_ratio": 1.5968992248062015,
  "no_speech_prob": 0.15724892914295197}, {"id": 40, "seek": 16428, "start": 172.76,
  "end": 174.36, "text": " that stands out.", "tokens": [50788, 300, 7382, 484, 13,
  50868], "temperature": 0.0, "avg_logprob": -0.2525026213448003, "compression_ratio":
  1.5968992248062015, "no_speech_prob": 0.15724892914295197}, {"id": 41, "seek": 16428,
  "start": 174.36, "end": 178.52, "text": " I started programming when I was a teenager.",
  "tokens": [50868, 286, 1409, 9410, 562, 286, 390, 257, 21440, 13, 51076], "temperature":
  0.0, "avg_logprob": -0.2525026213448003, "compression_ratio": 1.5968992248062015,
  "no_speech_prob": 0.15724892914295197}, {"id": 42, "seek": 16428, "start": 178.52,
  "end": 181.04, "text": " Similar to you, English is not my first language.", "tokens":
  [51076, 10905, 281, 291, 11, 3669, 307, 406, 452, 700, 2856, 13, 51202], "temperature":
  0.0, "avg_logprob": -0.2525026213448003, "compression_ratio": 1.5968992248062015,
  "no_speech_prob": 0.15724892914295197}, {"id": 43, "seek": 16428, "start": 181.04,
  "end": 187.64, "text": " So at some point, I exhausted the Danish web and then like
  divulged into video game addiction", "tokens": [51202, 407, 412, 512, 935, 11, 286,
  17992, 264, 36944, 3670, 293, 550, 411, 47291, 3004, 666, 960, 1216, 16835, 51532],
  "temperature": 0.0, "avg_logprob": -0.2525026213448003, "compression_ratio": 1.5968992248062015,
  "no_speech_prob": 0.15724892914295197}, {"id": 44, "seek": 16428, "start": 187.64,
  "end": 192.08, "text": " for three years as a teenager to learn enough English to
  sort of, you know, get my own", "tokens": [51532, 337, 1045, 924, 382, 257, 21440,
  281, 1466, 1547, 3669, 281, 1333, 295, 11, 291, 458, 11, 483, 452, 1065, 51754],
  "temperature": 0.0, "avg_logprob": -0.2525026213448003, "compression_ratio": 1.5968992248062015,
  "no_speech_prob": 0.15724892914295197}, {"id": 45, "seek": 19208, "start": 192.08,
  "end": 195.64000000000001, "text": " chat CBT moment and take off point.", "tokens":
  [50364, 5081, 18745, 51, 1623, 293, 747, 766, 935, 13, 50542], "temperature": 0.0,
  "avg_logprob": -0.1670213400148878, "compression_ratio": 1.7490196078431373, "no_speech_prob":
  0.03435908257961273}, {"id": 46, "seek": 19208, "start": 195.64000000000001, "end":
  200.24, "text": " And then I spent a lot of time in high school being not very good
  at competitive programming,", "tokens": [50542, 400, 550, 286, 4418, 257, 688, 295,
  565, 294, 1090, 1395, 885, 406, 588, 665, 412, 10043, 9410, 11, 50772], "temperature":
  0.0, "avg_logprob": -0.1670213400148878, "compression_ratio": 1.7490196078431373,
  "no_speech_prob": 0.03435908257961273}, {"id": 47, "seek": 19208, "start": 200.24,
  "end": 204.08, "text": " but good enough to qualify for the small country of Denmark.",
  "tokens": [50772, 457, 665, 1547, 281, 20276, 337, 264, 1359, 1941, 295, 28065,
  13, 50964], "temperature": 0.0, "avg_logprob": -0.1670213400148878, "compression_ratio":
  1.7490196078431373, "no_speech_prob": 0.03435908257961273}, {"id": 48, "seek": 19208,
  "start": 204.08, "end": 210.96, "text": " And then I spent almost a decade working
  at Shopify doing mainly infrastructure work.", "tokens": [50964, 400, 550, 286,
  4418, 1920, 257, 10378, 1364, 412, 43991, 884, 8704, 6896, 589, 13, 51308], "temperature":
  0.0, "avg_logprob": -0.1670213400148878, "compression_ratio": 1.7490196078431373,
  "no_speech_prob": 0.03435908257961273}, {"id": 49, "seek": 19208, "start": 210.96,
  "end": 216.36, "text": " So when I joined infrastructure Shopify and the infrastructure
  team, we were doing, I mean,", "tokens": [51308, 407, 562, 286, 6869, 6896, 43991,
  293, 264, 6896, 1469, 11, 321, 645, 884, 11, 286, 914, 11, 51578], "temperature":
  0.0, "avg_logprob": -0.1670213400148878, "compression_ratio": 1.7490196078431373,
  "no_speech_prob": 0.03435908257961273}, {"id": 50, "seek": 19208, "start": 216.36,
  "end": 221.4, "text": " it was not even an infrastructure team like DevOps was just
  becoming a thing.", "tokens": [51578, 309, 390, 406, 754, 364, 6896, 1469, 411,
  43051, 390, 445, 5617, 257, 551, 13, 51830], "temperature": 0.0, "avg_logprob":
  -0.1670213400148878, "compression_ratio": 1.7490196078431373, "no_speech_prob":
  0.03435908257961273}, {"id": 51, "seek": 22140, "start": 221.4, "end": 224.76000000000002,
  "text": " And we were driving just a couple hundred requests per second.", "tokens":
  [50364, 400, 321, 645, 4840, 445, 257, 1916, 3262, 12475, 680, 1150, 13, 50532],
  "temperature": 0.0, "avg_logprob": -0.16867480644812952, "compression_ratio": 1.7157190635451505,
  "no_speech_prob": 0.021443955600261688}, {"id": 52, "seek": 22140, "start": 224.76000000000002,
  "end": 228.24, "text": " And by the time I left, we saw peaks of more than a million.",
  "tokens": [50532, 400, 538, 264, 565, 286, 1411, 11, 321, 1866, 26897, 295, 544,
  813, 257, 2459, 13, 50706], "temperature": 0.0, "avg_logprob": -0.16867480644812952,
  "compression_ratio": 1.7157190635451505, "no_speech_prob": 0.021443955600261688},
  {"id": 53, "seek": 22140, "start": 228.24, "end": 233.44, "text": " And I more or
  less worked on all of the stateful systems that power that because they generally",
  "tokens": [50706, 400, 286, 544, 420, 1570, 2732, 322, 439, 295, 264, 1785, 906,
  3652, 300, 1347, 300, 570, 436, 5101, 50966], "temperature": 0.0, "avg_logprob":
  -0.16867480644812952, "compression_ratio": 1.7157190635451505, "no_speech_prob":
  0.021443955600261688}, {"id": 54, "seek": 22140, "start": 233.44, "end": 238.48000000000002,
  "text": " tend to be the bottleneck just playing whack-a-mole every single year
  for every Black Friday", "tokens": [50966, 3928, 281, 312, 264, 44641, 547, 445,
  2433, 42877, 12, 64, 12, 3280, 306, 633, 2167, 1064, 337, 633, 4076, 6984, 51218],
  "temperature": 0.0, "avg_logprob": -0.16867480644812952, "compression_ratio": 1.7157190635451505,
  "no_speech_prob": 0.021443955600261688}, {"id": 55, "seek": 22140, "start": 238.48000000000002,
  "end": 239.88, "text": " for many years.", "tokens": [51218, 337, 867, 924, 13,
  51288], "temperature": 0.0, "avg_logprob": -0.16867480644812952, "compression_ratio":
  1.7157190635451505, "no_speech_prob": 0.021443955600261688}, {"id": 56, "seek":
  22140, "start": 239.88, "end": 243.96, "text": " And I spent the majority of those
  years on one of the last resort pages for Shopify as", "tokens": [51288, 400, 286,
  4418, 264, 6286, 295, 729, 924, 322, 472, 295, 264, 1036, 19606, 7183, 337, 43991,
  382, 51492], "temperature": 0.0, "avg_logprob": -0.16867480644812952, "compression_ratio":
  1.7157190635451505, "no_speech_prob": 0.021443955600261688}, {"id": 57, "seek":
  22140, "start": 243.96, "end": 244.96, "text": " well.", "tokens": [51492, 731,
  13, 51542], "temperature": 0.0, "avg_logprob": -0.16867480644812952, "compression_ratio":
  1.7157190635451505, "no_speech_prob": 0.021443955600261688}, {"id": 58, "seek":
  22140, "start": 244.96, "end": 250.6, "text": " One of those pages were the pages
  are very scary in the middle of the night and where a lot", "tokens": [51542, 1485,
  295, 729, 7183, 645, 264, 7183, 366, 588, 6958, 294, 264, 2808, 295, 264, 1818,
  293, 689, 257, 688, 51824], "temperature": 0.0, "avg_logprob": -0.16867480644812952,
  "compression_ratio": 1.7157190635451505, "no_speech_prob": 0.021443955600261688},
  {"id": 59, "seek": 25060, "start": 250.6, "end": 253.16, "text": " of GME of course
  runs through Shopify.", "tokens": [50364, 295, 460, 15454, 295, 1164, 6676, 807,
  43991, 13, 50492], "temperature": 0.0, "avg_logprob": -0.1950820474063649, "compression_ratio":
  1.4890829694323144, "no_speech_prob": 0.00859132967889309}, {"id": 60, "seek": 25060,
  "start": 253.16, "end": 257.2, "text": " So very high responsibility on that.",
  "tokens": [50492, 407, 588, 1090, 6357, 322, 300, 13, 50694], "temperature": 0.0,
  "avg_logprob": -0.1950820474063649, "compression_ratio": 1.4890829694323144, "no_speech_prob":
  0.00859132967889309}, {"id": 61, "seek": 25060, "start": 257.2, "end": 263.44, "text":
  " I left in 2021 and kind of jumped around at my friends'' companies helping them
  with various", "tokens": [50694, 286, 1411, 294, 7201, 293, 733, 295, 13864, 926,
  412, 452, 1855, 6, 3431, 4315, 552, 365, 3683, 51006], "temperature": 0.0, "avg_logprob":
  -0.1950820474063649, "compression_ratio": 1.4890829694323144, "no_speech_prob":
  0.00859132967889309}, {"id": 62, "seek": 25060, "start": 263.44, "end": 264.44,
  "text": " things.", "tokens": [51006, 721, 13, 51056], "temperature": 0.0, "avg_logprob":
  -0.1950820474063649, "compression_ratio": 1.4890829694323144, "no_speech_prob":
  0.00859132967889309}, {"id": 63, "seek": 25060, "start": 264.44, "end": 267.08,
  "text": " And I spent almost my entire career at one company.", "tokens": [51056,
  400, 286, 4418, 1920, 452, 2302, 3988, 412, 472, 2237, 13, 51188], "temperature":
  0.0, "avg_logprob": -0.1950820474063649, "compression_ratio": 1.4890829694323144,
  "no_speech_prob": 0.00859132967889309}, {"id": 64, "seek": 25060, "start": 267.08,
  "end": 273.04, "text": " So I wanted to dabble and just go and basically help my
  friends with any infrastructure challenges", "tokens": [51188, 407, 286, 1415, 281,
  28964, 638, 293, 445, 352, 293, 1936, 854, 452, 1855, 365, 604, 6896, 4759, 51486],
  "temperature": 0.0, "avg_logprob": -0.1950820474063649, "compression_ratio": 1.4890829694323144,
  "no_speech_prob": 0.00859132967889309}, {"id": 65, "seek": 25060, "start": 273.04,
  "end": 274.44, "text": " that they had.", "tokens": [51486, 300, 436, 632, 13, 51556],
  "temperature": 0.0, "avg_logprob": -0.1950820474063649, "compression_ratio": 1.4890829694323144,
  "no_speech_prob": 0.00859132967889309}, {"id": 66, "seek": 27444, "start": 274.44,
  "end": 282.24, "text": " And in 2023 when Chatschy BT launched and the APIs launched,
  I was working with my friends", "tokens": [50364, 400, 294, 44377, 562, 761, 1720,
  28629, 31144, 8730, 293, 264, 21445, 8730, 11, 286, 390, 1364, 365, 452, 1855, 50754],
  "temperature": 0.0, "avg_logprob": -0.3703589038314106, "compression_ratio": 1.5278810408921932,
  "no_speech_prob": 0.03991719335317612}, {"id": 67, "seek": 27444, "start": 282.24,
  "end": 284.2, "text": " at this company called Readwise.", "tokens": [50754, 412,
  341, 2237, 1219, 17604, 3711, 13, 50852], "temperature": 0.0, "avg_logprob": -0.3703589038314106,
  "compression_ratio": 1.5278810408921932, "no_speech_prob": 0.03991719335317612},
  {"id": 68, "seek": 27444, "start": 284.2, "end": 291.0, "text": " They have a product
  similar to a pocket and others for reading articles later from", "tokens": [50852,
  814, 362, 257, 1674, 2531, 281, 257, 8963, 293, 2357, 337, 3760, 11290, 1780, 490,
  51192], "temperature": 0.0, "avg_logprob": -0.3703589038314106, "compression_ratio":
  1.5278810408921932, "no_speech_prob": 0.03991719335317612}, {"id": 69, "seek": 27444,
  "start": 291.0, "end": 292.92, "text": " an Amal product.", "tokens": [51192, 364,
  2012, 304, 1674, 13, 51288], "temperature": 0.0, "avg_logprob": -0.3703589038314106,
  "compression_ratio": 1.5278810408921932, "no_speech_prob": 0.03991719335317612},
  {"id": 70, "seek": 27444, "start": 292.92, "end": 297.48, "text": " And they asked
  me to build a recommendation feature for articles.", "tokens": [51288, 400, 436,
  2351, 385, 281, 1322, 257, 11879, 4111, 337, 11290, 13, 51516], "temperature": 0.0,
  "avg_logprob": -0.3703589038314106, "compression_ratio": 1.5278810408921932, "no_speech_prob":
  0.03991719335317612}, {"id": 71, "seek": 27444, "start": 297.48, "end": 299.48,
  "text": " And I was like, well, it''s perfect, right?", "tokens": [51516, 400, 286,
  390, 411, 11, 731, 11, 309, 311, 2176, 11, 558, 30, 51616], "temperature": 0.0,
  "avg_logprob": -0.3703589038314106, "compression_ratio": 1.5278810408921932, "no_speech_prob":
  0.03991719335317612}, {"id": 72, "seek": 27444, "start": 299.48, "end": 304.0, "text":
  " LLMs or embedding models are basically just LLMs with their heads chopped off.",
  "tokens": [51616, 441, 43, 26386, 420, 12240, 3584, 5245, 366, 1936, 445, 441, 43,
  26386, 365, 641, 8050, 16497, 766, 13, 51842], "temperature": 0.0, "avg_logprob":
  -0.3703589038314106, "compression_ratio": 1.5278810408921932, "no_speech_prob":
  0.03991719335317612}, {"id": 73, "seek": 30400, "start": 304.0, "end": 306.32, "text":
  " And they''re trained on exactly this data.", "tokens": [50364, 400, 436, 434,
  8895, 322, 2293, 341, 1412, 13, 50480], "temperature": 0.0, "avg_logprob": -0.19370662355885923,
  "compression_ratio": 1.607843137254902, "no_speech_prob": 0.014127611182630062},
  {"id": 74, "seek": 30400, "start": 306.32, "end": 311.96, "text": " So we built
  something and it actually worked pretty well for just recommending articles.", "tokens":
  [50480, 407, 321, 3094, 746, 293, 309, 767, 2732, 1238, 731, 337, 445, 30559, 11290,
  13, 50762], "temperature": 0.0, "avg_logprob": -0.19370662355885923, "compression_ratio":
  1.607843137254902, "no_speech_prob": 0.014127611182630062}, {"id": 75, "seek": 30400,
  "start": 311.96, "end": 317.24, "text": " But then I ran the back of the envelope
  math on what it would cost to do this for the", "tokens": [50762, 583, 550, 286,
  5872, 264, 646, 295, 264, 19989, 5221, 322, 437, 309, 576, 2063, 281, 360, 341,
  337, 264, 51026], "temperature": 0.0, "avg_logprob": -0.19370662355885923, "compression_ratio":
  1.607843137254902, "no_speech_prob": 0.014127611182630062}, {"id": 76, "seek": 30400,
  "start": 317.24, "end": 320.04, "text": " entire article catalog, right?", "tokens":
  [51026, 2302, 7222, 19746, 11, 558, 30, 51166], "temperature": 0.0, "avg_logprob":
  -0.19370662355885923, "compression_ratio": 1.607843137254902, "no_speech_prob":
  0.014127611182630062}, {"id": 77, "seek": 30400, "start": 320.04, "end": 322.64,
  "text": " It had hundreds of millions of articles.", "tokens": [51166, 467, 632,
  6779, 295, 6803, 295, 11290, 13, 51296], "temperature": 0.0, "avg_logprob": -0.19370662355885923,
  "compression_ratio": 1.607843137254902, "no_speech_prob": 0.014127611182630062},
  {"id": 78, "seek": 30400, "start": 322.64, "end": 327.4, "text": " And it would
  have cost more than 30 grand a month to do.", "tokens": [51296, 400, 309, 576, 362,
  2063, 544, 813, 2217, 2697, 257, 1618, 281, 360, 13, 51534], "temperature": 0.0,
  "avg_logprob": -0.19370662355885923, "compression_ratio": 1.607843137254902, "no_speech_prob":
  0.014127611182630062}, {"id": 79, "seek": 30400, "start": 327.4, "end": 330.56,
  "text": " And for a large company that''s not a big deal for an experiment.", "tokens":
  [51534, 400, 337, 257, 2416, 2237, 300, 311, 406, 257, 955, 2028, 337, 364, 5120,
  13, 51692], "temperature": 0.0, "avg_logprob": -0.19370662355885923, "compression_ratio":
  1.607843137254902, "no_speech_prob": 0.014127611182630062}, {"id": 80, "seek": 33056,
  "start": 330.56, "end": 334.92, "text": " But this was a company that was spending
  three grand a month on a Postgres instance that", "tokens": [50364, 583, 341, 390,
  257, 2237, 300, 390, 6434, 1045, 2697, 257, 1618, 322, 257, 10223, 45189, 5197,
  300, 50582], "temperature": 0.0, "avg_logprob": -0.198042883389238, "compression_ratio":
  1.7835051546391754, "no_speech_prob": 0.14610272645950317}, {"id": 81, "seek": 33056,
  "start": 334.92, "end": 337.96, "text": " prior to working on this, I tuned.", "tokens":
  [50582, 4059, 281, 1364, 322, 341, 11, 286, 10870, 13, 50734], "temperature": 0.0,
  "avg_logprob": -0.198042883389238, "compression_ratio": 1.7835051546391754, "no_speech_prob":
  0.14610272645950317}, {"id": 82, "seek": 33056, "start": 337.96, "end": 344.88,
  "text": " And spending 10 times that on just recommendations and possibly search
  was just untenable.", "tokens": [50734, 400, 6434, 1266, 1413, 300, 322, 445, 10434,
  293, 6264, 3164, 390, 445, 25693, 712, 13, 51080], "temperature": 0.0, "avg_logprob":
  -0.198042883389238, "compression_ratio": 1.7835051546391754, "no_speech_prob": 0.14610272645950317},
  {"id": 83, "seek": 33056, "start": 344.88, "end": 345.88, "text": " So it sort of
  lost it.", "tokens": [51080, 407, 309, 1333, 295, 2731, 309, 13, 51130], "temperature":
  0.0, "avg_logprob": -0.198042883389238, "compression_ratio": 1.7835051546391754,
  "no_speech_prob": 0.14610272645950317}, {"id": 84, "seek": 33056, "start": 345.88,
  "end": 348.96, "text": " It was lost in its track.", "tokens": [51130, 467, 390,
  2731, 294, 1080, 2837, 13, 51284], "temperature": 0.0, "avg_logprob": -0.198042883389238,
  "compression_ratio": 1.7835051546391754, "no_speech_prob": 0.14610272645950317},
  {"id": 85, "seek": 33056, "start": 348.96, "end": 350.64, "text": " And it was a
  bit sad.", "tokens": [51284, 400, 309, 390, 257, 857, 4227, 13, 51368], "temperature":
  0.0, "avg_logprob": -0.198042883389238, "compression_ratio": 1.7835051546391754,
  "no_speech_prob": 0.14610272645950317}, {"id": 86, "seek": 33056, "start": 350.64,
  "end": 353.8, "text": " And it''s sort of ended up in that bucket that a lot of
  companies have of like, okay,", "tokens": [51368, 400, 309, 311, 1333, 295, 4590,
  493, 294, 300, 13058, 300, 257, 688, 295, 3431, 362, 295, 411, 11, 1392, 11, 51526],
  "temperature": 0.0, "avg_logprob": -0.198042883389238, "compression_ratio": 1.7835051546391754,
  "no_speech_prob": 0.14610272645950317}, {"id": 87, "seek": 33056, "start": 353.8,
  "end": 357.28, "text": " we''re going to work on this when it becomes cheaper and
  then we''ll ship this feature.", "tokens": [51526, 321, 434, 516, 281, 589, 322,
  341, 562, 309, 3643, 12284, 293, 550, 321, 603, 5374, 341, 4111, 13, 51700], "temperature":
  0.0, "avg_logprob": -0.198042883389238, "compression_ratio": 1.7835051546391754,
  "no_speech_prob": 0.14610272645950317}, {"id": 88, "seek": 33056, "start": 357.28,
  "end": 359.56, "text": " But it was a bit sad because I was excited about this feature.",
  "tokens": [51700, 583, 309, 390, 257, 857, 4227, 570, 286, 390, 2919, 466, 341,
  4111, 13, 51814], "temperature": 0.0, "avg_logprob": -0.198042883389238, "compression_ratio":
  1.7835051546391754, "no_speech_prob": 0.14610272645950317}, {"id": 89, "seek": 35956,
  "start": 359.56, "end": 362.92, "text": " It''s a user of the product as well.",
  "tokens": [50364, 467, 311, 257, 4195, 295, 264, 1674, 382, 731, 13, 50532], "temperature":
  0.0, "avg_logprob": -0.2509641408920288, "compression_ratio": 1.4444444444444444,
  "no_speech_prob": 0.0010196856455877423}, {"id": 90, "seek": 35956, "start": 362.92,
  "end": 365.88, "text": " And I could not stop thinking about that.", "tokens": [50532,
  400, 286, 727, 406, 1590, 1953, 466, 300, 13, 50680], "temperature": 0.0, "avg_logprob":
  -0.2509641408920288, "compression_ratio": 1.4444444444444444, "no_speech_prob":
  0.0010196856455877423}, {"id": 91, "seek": 35956, "start": 365.88, "end": 367.92,
  "text": " Why was it so expensive?", "tokens": [50680, 1545, 390, 309, 370, 5124,
  30, 50782], "temperature": 0.0, "avg_logprob": -0.2509641408920288, "compression_ratio":
  1.4444444444444444, "no_speech_prob": 0.0010196856455877423}, {"id": 92, "seek":
  35956, "start": 367.92, "end": 374.56, "text": " And the vector databases at the
  time were storing everything in memory.", "tokens": [50782, 400, 264, 8062, 22380,
  412, 264, 565, 645, 26085, 1203, 294, 4675, 13, 51114], "temperature": 0.0, "avg_logprob":
  -0.2509641408920288, "compression_ratio": 1.4444444444444444, "no_speech_prob":
  0.0010196856455877423}, {"id": 93, "seek": 35956, "start": 374.56, "end": 381.8,
  "text": " And DRAM on a cloud cost somewhere between two to five dollars per gigabyte.",
  "tokens": [51114, 400, 12118, 2865, 322, 257, 4588, 2063, 4079, 1296, 732, 281,
  1732, 3808, 680, 8741, 34529, 13, 51476], "temperature": 0.0, "avg_logprob": -0.2509641408920288,
  "compression_ratio": 1.4444444444444444, "no_speech_prob": 0.0010196856455877423},
  {"id": 94, "seek": 35956, "start": 381.8, "end": 384.08, "text": " And this just
  economics of this didn''t line up.", "tokens": [51476, 400, 341, 445, 14564, 295,
  341, 994, 380, 1622, 493, 13, 51590], "temperature": 0.0, "avg_logprob": -0.2509641408920288,
  "compression_ratio": 1.4444444444444444, "no_speech_prob": 0.0010196856455877423},
  {"id": 95, "seek": 38408, "start": 384.08, "end": 389.64, "text": " It wasn''t that
  this vector database was doing anything, you know, malicious in their pricing.",
  "tokens": [50364, 467, 2067, 380, 300, 341, 8062, 8149, 390, 884, 1340, 11, 291,
  458, 11, 33496, 294, 641, 17621, 13, 50642], "temperature": 0.0, "avg_logprob":
  -0.2799035898844401, "compression_ratio": 1.7491961414790997, "no_speech_prob":
  0.008905366063117981}, {"id": 96, "seek": 38408, "start": 389.64, "end": 392.84,
  "text": " They''re just trying to earn them on its margin on memory pricing.", "tokens":
  [50642, 814, 434, 445, 1382, 281, 6012, 552, 322, 1080, 10270, 322, 4675, 17621,
  13, 50802], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 97, "seek":
  38408, "start": 392.84, "end": 397.08, "text": " But memory pricing was just too
  high and it stopped its feature and it''s tracks.", "tokens": [50802, 583, 4675,
  17621, 390, 445, 886, 1090, 293, 309, 5936, 1080, 4111, 293, 309, 311, 10218, 13,
  51014], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 98, "seek":
  38408, "start": 397.08, "end": 400.84, "text": " And what I couldn''t stop thinking
  about is, why can''t we do all of this on top of", "tokens": [51014, 400, 437, 286,
  2809, 380, 1590, 1953, 466, 307, 11, 983, 393, 380, 321, 360, 439, 295, 341, 322,
  1192, 295, 51202], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 99, "seek":
  38408, "start": 400.84, "end": 402.08, "text": " Obick storage, right?", "tokens":
  [51202, 4075, 618, 6725, 11, 558, 30, 51264], "temperature": 0.0, "avg_logprob":
  -0.2799035898844401, "compression_ratio": 1.7491961414790997, "no_speech_prob":
  0.008905366063117981}, {"id": 100, "seek": 38408, "start": 402.08, "end": 403.64,
  "text": " Like we just put it on an Obick storage.", "tokens": [51264, 1743, 321,
  445, 829, 309, 322, 364, 4075, 618, 6725, 13, 51342], "temperature": 0.0, "avg_logprob":
  -0.2799035898844401, "compression_ratio": 1.7491961414790997, "no_speech_prob":
  0.008905366063117981}, {"id": 101, "seek": 38408, "start": 403.64, "end": 404.64,
  "text": " That''s the source of truth.", "tokens": [51342, 663, 311, 264, 4009,
  295, 3494, 13, 51392], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 102, "seek":
  38408, "start": 404.64, "end": 408.52, "text": " And then we actually need to some
  piece of data and we put it in memory or even on this", "tokens": [51392, 400, 550,
  321, 767, 643, 281, 512, 2522, 295, 1412, 293, 321, 829, 309, 294, 4675, 420, 754,
  322, 341, 51586], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 103, "seek":
  38408, "start": 408.52, "end": 410.12, "text": " if we can.", "tokens": [51586,
  498, 321, 393, 13, 51666], "temperature": 0.0, "avg_logprob": -0.2799035898844401,
  "compression_ratio": 1.7491961414790997, "no_speech_prob": 0.008905366063117981},
  {"id": 104, "seek": 38408, "start": 410.12, "end": 411.12, "text": " And I did it
  to Mac and Nathan.", "tokens": [51666, 400, 286, 630, 309, 281, 5707, 293, 20634,
  13, 51716], "temperature": 0.0, "avg_logprob": -0.2799035898844401, "compression_ratio":
  1.7491961414790997, "no_speech_prob": 0.008905366063117981}, {"id": 105, "seek":
  41112, "start": 411.12, "end": 416.04, "text": " And I was like, I think that''s
  about a hundred times cheaper.", "tokens": [50364, 400, 286, 390, 411, 11, 286,
  519, 300, 311, 466, 257, 3262, 1413, 12284, 13, 50610], "temperature": 0.0, "avg_logprob":
  -0.21510773691637763, "compression_ratio": 1.6277372262773722, "no_speech_prob":
  0.3561461269855499}, {"id": 106, "seek": 41112, "start": 416.04, "end": 418.44,
  "text": " And of course, that would have been no brainer for read wise.", "tokens":
  [50610, 400, 295, 1164, 11, 300, 576, 362, 668, 572, 3567, 260, 337, 1401, 10829,
  13, 50730], "temperature": 0.0, "avg_logprob": -0.21510773691637763, "compression_ratio":
  1.6277372262773722, "no_speech_prob": 0.3561461269855499}, {"id": 107, "seek": 41112,
  "start": 418.44, "end": 421.68, "text": " We would have just bought it and started
  using it and tried it out, right?", "tokens": [50730, 492, 576, 362, 445, 4243,
  309, 293, 1409, 1228, 309, 293, 3031, 309, 484, 11, 558, 30, 50892], "temperature":
  0.0, "avg_logprob": -0.21510773691637763, "compression_ratio": 1.6277372262773722,
  "no_speech_prob": 0.3561461269855499}, {"id": 108, "seek": 41112, "start": 421.68,
  "end": 425.76, "text": " And maybe put way more data in and maybe worked our way
  up to that 30 grand a month bill.", "tokens": [50892, 400, 1310, 829, 636, 544,
  1412, 294, 293, 1310, 2732, 527, 636, 493, 281, 300, 2217, 2697, 257, 1618, 2961,
  13, 51096], "temperature": 0.0, "avg_logprob": -0.21510773691637763, "compression_ratio":
  1.6277372262773722, "no_speech_prob": 0.3561461269855499}, {"id": 109, "seek": 41112,
  "start": 425.76, "end": 428.8, "text": " But with a different workload.", "tokens":
  [51096, 583, 365, 257, 819, 20139, 13, 51248], "temperature": 0.0, "avg_logprob":
  -0.21510773691637763, "compression_ratio": 1.6277372262773722, "no_speech_prob":
  0.3561461269855499}, {"id": 110, "seek": 41112, "start": 428.8, "end": 431.44, "text":
  " And so yeah, I couldn''t stop thinking about it.", "tokens": [51248, 400, 370,
  1338, 11, 286, 2809, 380, 1590, 1953, 466, 309, 13, 51380], "temperature": 0.0,
  "avg_logprob": -0.21510773691637763, "compression_ratio": 1.6277372262773722, "no_speech_prob":
  0.3561461269855499}, {"id": 111, "seek": 41112, "start": 431.44, "end": 436.48,
  "text": " And then eventually started writing the first version over the summer
  of 2023.", "tokens": [51380, 400, 550, 4728, 1409, 3579, 264, 700, 3037, 670, 264,
  4266, 295, 44377, 13, 51632], "temperature": 0.0, "avg_logprob": -0.21510773691637763,
  "compression_ratio": 1.6277372262773722, "no_speech_prob": 0.3561461269855499},
  {"id": 112, "seek": 43648, "start": 436.48, "end": 441.92, "text": " Just me alone
  in the wills of Canada and then launched it in October of 2023, which is", "tokens":
  [50364, 1449, 385, 3312, 294, 264, 486, 82, 295, 6309, 293, 550, 8730, 309, 294,
  7617, 295, 44377, 11, 597, 307, 50636], "temperature": 0.0, "avg_logprob": -0.2465718778452479,
  "compression_ratio": 1.707070707070707, "no_speech_prob": 0.40480300784111023},
  {"id": 113, "seek": 43648, "start": 441.92, "end": 442.92, "text": " probably where
  you saw it.", "tokens": [50636, 1391, 689, 291, 1866, 309, 13, 50686], "temperature":
  0.0, "avg_logprob": -0.2465718778452479, "compression_ratio": 1.707070707070707,
  "no_speech_prob": 0.40480300784111023}, {"id": 114, "seek": 43648, "start": 442.92,
  "end": 444.20000000000005, "text": " I didn''t really tell anyone about it.", "tokens":
  [50686, 286, 994, 380, 534, 980, 2878, 466, 309, 13, 50750], "temperature": 0.0,
  "avg_logprob": -0.2465718778452479, "compression_ratio": 1.707070707070707, "no_speech_prob":
  0.40480300784111023}, {"id": 115, "seek": 43648, "start": 444.20000000000005, "end":
  447.6, "text": " I was just I was just hacking away.", "tokens": [50750, 286, 390,
  445, 286, 390, 445, 31422, 1314, 13, 50920], "temperature": 0.0, "avg_logprob":
  -0.2465718778452479, "compression_ratio": 1.707070707070707, "no_speech_prob": 0.40480300784111023},
  {"id": 116, "seek": 43648, "start": 447.6, "end": 452.04, "text": " Launched it
  did a lot of our deal over that summer insights that some of them still are", "tokens":
  [50920, 28119, 292, 309, 630, 257, 688, 295, 527, 2028, 670, 300, 4266, 14310, 300,
  512, 295, 552, 920, 366, 51142], "temperature": 0.0, "avg_logprob": -0.2465718778452479,
  "compression_ratio": 1.707070707070707, "no_speech_prob": 0.40480300784111023},
  {"id": 117, "seek": 43648, "start": 452.04, "end": 455.96000000000004, "text": "
  in the product and a lot of them we''ve since faced out.", "tokens": [51142, 294,
  264, 1674, 293, 257, 688, 295, 552, 321, 600, 1670, 11446, 484, 13, 51338], "temperature":
  0.0, "avg_logprob": -0.2465718778452479, "compression_ratio": 1.707070707070707,
  "no_speech_prob": 0.40480300784111023}, {"id": 118, "seek": 43648, "start": 455.96000000000004,
  "end": 459.16, "text": " But the most important thing was that it launched.", "tokens":
  [51338, 583, 264, 881, 1021, 551, 390, 300, 309, 8730, 13, 51498], "temperature":
  0.0, "avg_logprob": -0.2465718778452479, "compression_ratio": 1.707070707070707,
  "no_speech_prob": 0.40480300784111023}, {"id": 119, "seek": 43648, "start": 459.16,
  "end": 462.32, "text": " And the first version of trouble puffer didn''t have I
  was just looking at the website the", "tokens": [51498, 400, 264, 700, 3037, 295,
  5253, 19613, 260, 994, 380, 362, 286, 390, 445, 1237, 412, 264, 3144, 264, 51656],
  "temperature": 0.0, "avg_logprob": -0.2465718778452479, "compression_ratio": 1.707070707070707,
  "no_speech_prob": 0.40480300784111023}, {"id": 120, "seek": 43648, "start": 462.32,
  "end": 464.32, "text": " other day for an unrelated reason.", "tokens": [51656,
  661, 786, 337, 364, 38967, 1778, 13, 51756], "temperature": 0.0, "avg_logprob":
  -0.2465718778452479, "compression_ratio": 1.707070707070707, "no_speech_prob": 0.40480300784111023},
  {"id": 121, "seek": 46432, "start": 464.32, "end": 466.76, "text": " It didn''t
  have mutable indexes.", "tokens": [50364, 467, 994, 380, 362, 5839, 712, 8186, 279,
  13, 50486], "temperature": 0.0, "avg_logprob": -0.2450800963810512, "compression_ratio":
  1.6883116883116882, "no_speech_prob": 0.12119867652654648}, {"id": 122, "seek":
  46432, "start": 466.76, "end": 472.36, "text": " So you just wrote to it and then
  you called an index endpoint and then you''re logged in like that''s it.", "tokens":
  [50486, 407, 291, 445, 4114, 281, 309, 293, 550, 291, 1219, 364, 8186, 35795, 293,
  550, 291, 434, 27231, 294, 411, 300, 311, 309, 13, 50766], "temperature": 0.0, "avg_logprob":
  -0.2450800963810512, "compression_ratio": 1.6883116883116882, "no_speech_prob":
  0.12119867652654648}, {"id": 123, "seek": 46432, "start": 472.36, "end": 475.96,
  "text": " And it didn''t have any SDKs.", "tokens": [50766, 400, 309, 994, 380,
  362, 604, 37135, 82, 13, 50946], "temperature": 0.0, "avg_logprob": -0.2450800963810512,
  "compression_ratio": 1.6883116883116882, "no_speech_prob": 0.12119867652654648},
  {"id": 124, "seek": 46432, "start": 475.96, "end": 479.96, "text": " It was just
  a big pure HTML website.", "tokens": [50946, 467, 390, 445, 257, 955, 6075, 17995,
  3144, 13, 51146], "temperature": 0.0, "avg_logprob": -0.2450800963810512, "compression_ratio":
  1.6883116883116882, "no_speech_prob": 0.12119867652654648}, {"id": 125, "seek":
  46432, "start": 479.96, "end": 489.2, "text": " But it was enough to ship it and
  it caught the attention at the time of the cursor team back in 2023.", "tokens":
  [51146, 583, 309, 390, 1547, 281, 5374, 309, 293, 309, 5415, 264, 3202, 412, 264,
  565, 295, 264, 28169, 1469, 646, 294, 44377, 13, 51608], "temperature": 0.0, "avg_logprob":
  -0.2450800963810512, "compression_ratio": 1.6883116883116882, "no_speech_prob":
  0.12119867652654648}, {"id": 126, "seek": 46432, "start": 489.2, "end": 492.12,
  "text": " And of course, this was this was this was early on for cursor.", "tokens":
  [51608, 400, 295, 1164, 11, 341, 390, 341, 390, 341, 390, 2440, 322, 337, 28169,
  13, 51754], "temperature": 0.0, "avg_logprob": -0.2450800963810512, "compression_ratio":
  1.6883116883116882, "no_speech_prob": 0.12119867652654648}, {"id": 127, "seek":
  46432, "start": 492.12, "end": 493.6, "text": " It was early on for us.", "tokens":
  [51754, 467, 390, 2440, 322, 337, 505, 13, 51828], "temperature": 0.0, "avg_logprob":
  -0.2450800963810512, "compression_ratio": 1.6883116883116882, "no_speech_prob":
  0.12119867652654648}, {"id": 128, "seek": 49360, "start": 493.6, "end": 499.96000000000004,
  "text": " And they are they''re a vector database built did not line up with their
  per user economics and", "tokens": [50364, 400, 436, 366, 436, 434, 257, 8062, 8149,
  3094, 630, 406, 1622, 493, 365, 641, 680, 4195, 14564, 293, 50682], "temperature":
  0.0, "avg_logprob": -0.22223109692598866, "compression_ratio": 1.7666666666666666,
  "no_speech_prob": 0.0013188893208280206}, {"id": 129, "seek": 49360, "start": 499.96000000000004,
  "end": 503.52000000000004, "text": " how they wanted to use rag in their in cursor.",
  "tokens": [50682, 577, 436, 1415, 281, 764, 17539, 294, 641, 294, 28169, 13, 50860],
  "temperature": 0.0, "avg_logprob": -0.22223109692598866, "compression_ratio": 1.7666666666666666,
  "no_speech_prob": 0.0013188893208280206}, {"id": 130, "seek": 49360, "start": 503.52000000000004,
  "end": 506.20000000000005, "text": " And so they they wanted to try to work together.",
  "tokens": [50860, 400, 370, 436, 436, 1415, 281, 853, 281, 589, 1214, 13, 50994],
  "temperature": 0.0, "avg_logprob": -0.22223109692598866, "compression_ratio": 1.7666666666666666,
  "no_speech_prob": 0.0013188893208280206}, {"id": 131, "seek": 49360, "start": 506.20000000000005,
  "end": 511.28000000000003, "text": " And we exchanged a bunch of emails of bullet
  points and it was very clear that they thought that this", "tokens": [50994, 400,
  321, 38378, 257, 3840, 295, 12524, 295, 11632, 2793, 293, 309, 390, 588, 1850, 300,
  436, 1194, 300, 341, 51248], "temperature": 0.0, "avg_logprob": -0.22223109692598866,
  "compression_ratio": 1.7666666666666666, "no_speech_prob": 0.0013188893208280206},
  {"id": 132, "seek": 49360, "start": 511.28000000000003, "end": 515.96, "text": "
  architecture was exactly now knowing the team are now they were just sat down at
  the dining table,", "tokens": [51248, 9482, 390, 2293, 586, 5276, 264, 1469, 366,
  586, 436, 645, 445, 3227, 760, 412, 264, 17874, 3199, 11, 51482], "temperature":
  0.0, "avg_logprob": -0.22223109692598866, "compression_ratio": 1.7666666666666666,
  "no_speech_prob": 0.0013188893208280206}, {"id": 133, "seek": 49360, "start": 515.96,
  "end": 521.24, "text": " done to napkin math over there and then thought why hasn''t
  anyone built it like this.", "tokens": [51482, 1096, 281, 9296, 5843, 5221, 670,
  456, 293, 550, 1194, 983, 6132, 380, 2878, 3094, 309, 411, 341, 13, 51746], "temperature":
  0.0, "avg_logprob": -0.22223109692598866, "compression_ratio": 1.7666666666666666,
  "no_speech_prob": 0.0013188893208280206}, {"id": 134, "seek": 52124, "start": 521.24,
  "end": 525.96, "text": " And so we worked we worked I went to San Francisco and
  spent some time with them and", "tokens": [50364, 400, 370, 321, 2732, 321, 2732,
  286, 1437, 281, 5271, 12279, 293, 4418, 512, 565, 365, 552, 293, 50600], "temperature":
  0.0, "avg_logprob": -0.2926841042258523, "compression_ratio": 1.6735395189003437,
  "no_speech_prob": 0.021179985255002975}, {"id": 135, "seek": 52124, "start": 525.96,
  "end": 531.84, "text": " came up with a bunch of features that they would need and
  called the best engineer that I knew would", "tokens": [50600, 1361, 493, 365, 257,
  3840, 295, 4122, 300, 436, 576, 643, 293, 1219, 264, 1151, 11403, 300, 286, 2586,
  576, 50894], "temperature": 0.0, "avg_logprob": -0.2926841042258523, "compression_ratio":
  1.6735395189003437, "no_speech_prob": 0.021179985255002975}, {"id": 136, "seek":
  52124, "start": 531.84, "end": 538.64, "text": " Shopify my co founder Justin and
  asked if they''d come on board because I think I think maybe there''s something
  here.", "tokens": [50894, 43991, 452, 598, 14917, 11320, 293, 2351, 498, 436, 1116,
  808, 322, 3150, 570, 286, 519, 286, 519, 1310, 456, 311, 746, 510, 13, 51234], "temperature":
  0.0, "avg_logprob": -0.2926841042258523, "compression_ratio": 1.6735395189003437,
  "no_speech_prob": 0.021179985255002975}, {"id": 137, "seek": 52124, "start": 538.64,
  "end": 544.76, "text": " And yeah, we launched it cursor cursor moved over and their
  bill was reduced by 95% and", "tokens": [51234, 400, 1338, 11, 321, 8730, 309, 28169,
  28169, 4259, 670, 293, 641, 2961, 390, 9212, 538, 13420, 4, 293, 51540], "temperature":
  0.0, "avg_logprob": -0.2926841042258523, "compression_ratio": 1.6735395189003437,
  "no_speech_prob": 0.021179985255002975}, {"id": 138, "seek": 52124, "start": 544.76,
  "end": 549.52, "text": " of course the additional storage architect today were on
  before didn''t make sense for the cursor", "tokens": [51540, 295, 1164, 264, 4497,
  6725, 6331, 965, 645, 322, 949, 994, 380, 652, 2020, 337, 264, 28169, 51778], "temperature":
  0.0, "avg_logprob": -0.2926841042258523, "compression_ratio": 1.6735395189003437,
  "no_speech_prob": 0.021179985255002975}, {"id": 139, "seek": 54952, "start": 549.52,
  "end": 553.6, "text": " economics but our storage architecture really did because
  you put all the all the code based", "tokens": [50364, 14564, 457, 527, 6725, 9482,
  534, 630, 570, 291, 829, 439, 264, 439, 264, 3089, 2361, 50568], "temperature":
  0.0, "avg_logprob": -0.23744130568070845, "compression_ratio": 1.6451612903225807,
  "no_speech_prob": 0.04909742623567581}, {"id": 140, "seek": 54952, "start": 553.6,
  "end": 558.72, "text": " embeddings on s3 and then the ones that are actively being
  used we can use in grammar or have in", "tokens": [50568, 12240, 29432, 322, 262,
  18, 293, 550, 264, 2306, 300, 366, 13022, 885, 1143, 321, 393, 764, 294, 22317,
  420, 362, 294, 50824], "temperature": 0.0, "avg_logprob": -0.23744130568070845,
  "compression_ratio": 1.6451612903225807, "no_speech_prob": 0.04909742623567581},
  {"id": 141, "seek": 54952, "start": 558.72, "end": 563.0799999999999, "text": "
  disk. I''ll stop there but that would be what led up to to this moment.", "tokens":
  [50824, 12355, 13, 286, 603, 1590, 456, 457, 300, 576, 312, 437, 4684, 493, 281,
  281, 341, 1623, 13, 51042], "temperature": 0.0, "avg_logprob": -0.23744130568070845,
  "compression_ratio": 1.6451612903225807, "no_speech_prob": 0.04909742623567581},
  {"id": 142, "seek": 54952, "start": 563.0799999999999, "end": 569.4399999999999,
  "text": " Oh, that''s amazing journey. A lot to ask of course a lot of questions
  but just on that cursor thing", "tokens": [51042, 876, 11, 300, 311, 2243, 4671,
  13, 316, 688, 281, 1029, 295, 1164, 257, 688, 295, 1651, 457, 445, 322, 300, 28169,
  551, 51360], "temperature": 0.0, "avg_logprob": -0.23744130568070845, "compression_ratio":
  1.6451612903225807, "no_speech_prob": 0.04909742623567581}, {"id": 143, "seek":
  54952, "start": 569.4399999999999, "end": 574.76, "text": " as I told you before
  we started recording you know I knew about you launching this working on this",
  "tokens": [51360, 382, 286, 1907, 291, 949, 321, 1409, 6613, 291, 458, 286, 2586,
  466, 291, 18354, 341, 1364, 322, 341, 51626], "temperature": 0.0, "avg_logprob":
  -0.23744130568070845, "compression_ratio": 1.6451612903225807, "no_speech_prob":
  0.04909742623567581}, {"id": 144, "seek": 57476, "start": 574.76, "end": 581.56,
  "text": " and then I''ve released it to the Lex Friedman podcast episode with the
  cursor team and they didn''t", "tokens": [50364, 293, 550, 286, 600, 4736, 309,
  281, 264, 24086, 17605, 1601, 7367, 3500, 365, 264, 28169, 1469, 293, 436, 994,
  380, 50704], "temperature": 0.0, "avg_logprob": -0.20765840337517555, "compression_ratio":
  1.7292576419213974, "no_speech_prob": 0.010459833778440952}, {"id": 145, "seek":
  57476, "start": 581.56, "end": 587.4, "text": " mention turbo pop for sort of like
  in passing but you know I think that also probably created a lot", "tokens": [50704,
  2152, 20902, 1665, 337, 1333, 295, 411, 294, 8437, 457, 291, 458, 286, 519, 300,
  611, 1391, 2942, 257, 688, 50996], "temperature": 0.0, "avg_logprob": -0.20765840337517555,
  "compression_ratio": 1.7292576419213974, "no_speech_prob": 0.010459833778440952},
  {"id": 146, "seek": 57476, "start": 587.4, "end": 594.28, "text": " of attention
  to you guys but I''m just curious like how did you get together how did you know
  cursor", "tokens": [50996, 295, 3202, 281, 291, 1074, 457, 286, 478, 445, 6369,
  411, 577, 630, 291, 483, 1214, 577, 630, 291, 458, 28169, 51340], "temperature":
  0.0, "avg_logprob": -0.20765840337517555, "compression_ratio": 1.7292576419213974,
  "no_speech_prob": 0.010459833778440952}, {"id": 147, "seek": 57476, "start": 594.28,
  "end": 601.4, "text": " team somehow someone on the cursor team that you could like
  partner early on and essentially help", "tokens": [51340, 1469, 6063, 1580, 322,
  264, 28169, 1469, 300, 291, 727, 411, 4975, 2440, 322, 293, 4476, 854, 51696], "temperature":
  0.0, "avg_logprob": -0.20765840337517555, "compression_ratio": 1.7292576419213974,
  "no_speech_prob": 0.010459833778440952}, {"id": 148, "seek": 60140, "start": 602.04,
  "end": 606.76, "text": " they kind of like helped you to pioneer it right in some
  sense becoming the first client", "tokens": [50396, 436, 733, 295, 411, 4254, 291,
  281, 37668, 309, 558, 294, 512, 2020, 5617, 264, 700, 6423, 50632], "temperature":
  0.0, "avg_logprob": -0.12334865707534927, "compression_ratio": 1.7786259541984732,
  "no_speech_prob": 0.007828392088413239}, {"id": 149, "seek": 60140, "start": 607.48,
  "end": 614.92, "text": " or maybe future client right how did you approach them.
  They did I mean they were a design", "tokens": [50668, 420, 1310, 2027, 6423, 558,
  577, 630, 291, 3109, 552, 13, 814, 630, 286, 914, 436, 645, 257, 1715, 51040], "temperature":
  0.0, "avg_logprob": -0.12334865707534927, "compression_ratio": 1.7786259541984732,
  "no_speech_prob": 0.007828392088413239}, {"id": 150, "seek": 60140, "start": 614.92,
  "end": 619.72, "text": " partner in every sense of the word right we had a slack
  channel and I feel like they treated us", "tokens": [51040, 4975, 294, 633, 2020,
  295, 264, 1349, 558, 321, 632, 257, 29767, 2269, 293, 286, 841, 411, 436, 8668,
  505, 51280], "temperature": 0.0, "avg_logprob": -0.12334865707534927, "compression_ratio":
  1.7786259541984732, "no_speech_prob": 0.007828392088413239}, {"id": 151, "seek":
  60140, "start": 619.72, "end": 625.48, "text": " as part of their team and we treated
  them as part of our team. They came inbound they sent an", "tokens": [51280, 382,
  644, 295, 641, 1469, 293, 321, 8668, 552, 382, 644, 295, 527, 1469, 13, 814, 1361,
  294, 18767, 436, 2279, 364, 51568], "temperature": 0.0, "avg_logprob": -0.12334865707534927,
  "compression_ratio": 1.7786259541984732, "no_speech_prob": 0.007828392088413239},
  {"id": 152, "seek": 60140, "start": 625.48, "end": 630.36, "text": " email based
  on the website and they said hey we would need mutable indexes and glob and a couple",
  "tokens": [51568, 3796, 2361, 322, 264, 3144, 293, 436, 848, 4177, 321, 576, 643,
  5839, 712, 8186, 279, 293, 16125, 293, 257, 1916, 51812], "temperature": 0.0, "avg_logprob":
  -0.12334865707534927, "compression_ratio": 1.7786259541984732, "no_speech_prob":
  0.007828392088413239}, {"id": 153, "seek": 63036, "start": 630.36, "end": 635.96,
  "text": " of other things so it''s like well that''s a very reasonable request right
  and I think they had", "tokens": [50364, 295, 661, 721, 370, 309, 311, 411, 731,
  300, 311, 257, 588, 10585, 5308, 558, 293, 286, 519, 436, 632, 50644], "temperature":
  0.0, "avg_logprob": -0.17964347349394352, "compression_ratio": 1.8571428571428572,
  "no_speech_prob": 0.0007849333342164755}, {"id": 154, "seek": 63036, "start": 635.96,
  "end": 641.88, "text": " the conviction that this was the right architecture and
  like if we could prove in their trust and", "tokens": [50644, 264, 24837, 300, 341,
  390, 264, 558, 9482, 293, 411, 498, 321, 727, 7081, 294, 641, 3361, 293, 50940],
  "temperature": 0.0, "avg_logprob": -0.17964347349394352, "compression_ratio": 1.8571428571428572,
  "no_speech_prob": 0.0007849333342164755}, {"id": 155, "seek": 63036, "start": 641.88,
  "end": 647.64, "text": " then be able to be in a good place so it was really just
  a it was just an oneness conversation", "tokens": [50940, 550, 312, 1075, 281, 312,
  294, 257, 665, 1081, 370, 309, 390, 534, 445, 257, 309, 390, 445, 364, 322, 15264,
  3761, 51228], "temperature": 0.0, "avg_logprob": -0.17964347349394352, "compression_ratio":
  1.8571428571428572, "no_speech_prob": 0.0007849333342164755}, {"id": 156, "seek":
  63036, "start": 648.44, "end": 653.8000000000001, "text": " just the way that the
  website is today a very honest description of what are the trade-offs", "tokens":
  [51268, 445, 264, 636, 300, 264, 3144, 307, 965, 257, 588, 3245, 3855, 295, 437,
  366, 264, 4923, 12, 19231, 51536], "temperature": 0.0, "avg_logprob": -0.17964347349394352,
  "compression_ratio": 1.8571428571428572, "no_speech_prob": 0.0007849333342164755},
  {"id": 157, "seek": 63036, "start": 653.8000000000001, "end": 659.4, "text": " what
  can it do what can it not do what is the latency profile what are the guarantees
  and", "tokens": [51536, 437, 393, 309, 360, 437, 393, 309, 406, 360, 437, 307, 264,
  27043, 7964, 437, 366, 264, 32567, 293, 51816], "temperature": 0.0, "avg_logprob":
  -0.17964347349394352, "compression_ratio": 1.8571428571428572, "no_speech_prob":
  0.0007849333342164755}, {"id": 158, "seek": 66036, "start": 660.36, "end": 665.5600000000001,
  "text": " that''s exactly the kind of bullet point discussion that we engaged in
  over email before I met the", "tokens": [50364, 300, 311, 2293, 264, 733, 295, 11632,
  935, 5017, 300, 321, 8237, 294, 670, 3796, 949, 286, 1131, 264, 50624], "temperature":
  0.0, "avg_logprob": -0.16736915876280586, "compression_ratio": 1.7611940298507462,
  "no_speech_prob": 0.001114301267080009}, {"id": 159, "seek": 66036, "start": 665.5600000000001,
  "end": 673.96, "text": " team in person yeah and they of course they were a small
  team at the time right it was and they", "tokens": [50624, 1469, 294, 954, 1338,
  293, 436, 295, 1164, 436, 645, 257, 1359, 1469, 412, 264, 565, 558, 309, 390, 293,
  436, 51044], "temperature": 0.0, "avg_logprob": -0.16736915876280586, "compression_ratio":
  1.7611940298507462, "no_speech_prob": 0.001114301267080009}, {"id": 160, "seek":
  66036, "start": 673.96, "end": 678.52, "text": " needed help with the with with
  parts of their infrastructure and working very very closely with", "tokens": [51044,
  2978, 854, 365, 264, 365, 365, 3166, 295, 641, 6896, 293, 1364, 588, 588, 8185,
  365, 51272], "temperature": 0.0, "avg_logprob": -0.16736915876280586, "compression_ratio":
  1.7611940298507462, "no_speech_prob": 0.001114301267080009}, {"id": 161, "seek":
  66036, "start": 678.52, "end": 683.8000000000001, "text": " teams that they could
  trust with the right economics and the right the right reliability.", "tokens":
  [51272, 5491, 300, 436, 727, 3361, 365, 264, 558, 14564, 293, 264, 558, 264, 558,
  24550, 13, 51536], "temperature": 0.0, "avg_logprob": -0.16736915876280586, "compression_ratio":
  1.7611940298507462, "no_speech_prob": 0.001114301267080009}, {"id": 162, "seek":
  66036, "start": 684.52, "end": 689.72, "text": " Yeah for sure but I guess that
  honesty which I also value a lot you know and in my work as I", "tokens": [51572,
  865, 337, 988, 457, 286, 2041, 300, 26839, 597, 286, 611, 2158, 257, 688, 291, 458,
  293, 294, 452, 589, 382, 286, 51832], "temperature": 0.0, "avg_logprob": -0.16736915876280586,
  "compression_ratio": 1.7611940298507462, "no_speech_prob": 0.001114301267080009},
  {"id": 163, "seek": 68972, "start": 689.72, "end": 696.52, "text": " became a product
  manager you know three years ago and I think it applies to any discipline be honest",
  "tokens": [50364, 3062, 257, 1674, 6598, 291, 458, 1045, 924, 2057, 293, 286, 519,
  309, 13165, 281, 604, 13635, 312, 3245, 50704], "temperature": 0.0, "avg_logprob":
  -0.08318492571512857, "compression_ratio": 1.7612612612612613, "no_speech_prob":
  0.0016630529426038265}, {"id": 164, "seek": 68972, "start": 696.52, "end": 701.88,
  "text": " but but you know like that honesty probably lies on the fact that you
  you''ve done your napkin", "tokens": [50704, 457, 457, 291, 458, 411, 300, 26839,
  1391, 9134, 322, 264, 1186, 300, 291, 291, 600, 1096, 428, 9296, 5843, 50972], "temperature":
  0.0, "avg_logprob": -0.08318492571512857, "compression_ratio": 1.7612612612612613,
  "no_speech_prob": 0.0016630529426038265}, {"id": 165, "seek": 68972, "start": 701.88,
  "end": 709.24, "text": " math and you knew where this will scale where how this
  can go right how did you go about doing that", "tokens": [50972, 5221, 293, 291,
  2586, 689, 341, 486, 4373, 689, 577, 341, 393, 352, 558, 577, 630, 291, 352, 466,
  884, 300, 51340], "temperature": 0.0, "avg_logprob": -0.08318492571512857, "compression_ratio":
  1.7612612612612613, "no_speech_prob": 0.0016630529426038265}, {"id": 166, "seek":
  68972, "start": 709.24, "end": 714.44, "text": " pre-launch right before having
  any client is that the company of your friends that helped you to", "tokens": [51340,
  659, 12, 875, 1680, 558, 949, 1419, 604, 6423, 307, 300, 264, 2237, 295, 428, 1855,
  300, 4254, 291, 281, 51600], "temperature": 0.0, "avg_logprob": -0.08318492571512857,
  "compression_ratio": 1.7612612612612613, "no_speech_prob": 0.0016630529426038265},
  {"id": 167, "seek": 71444, "start": 714.44, "end": 720.12, "text": " kind of like
  figure out the economics and sort of the the throughput and all of these rigorous",
  "tokens": [50364, 733, 295, 411, 2573, 484, 264, 14564, 293, 1333, 295, 264, 264,
  44629, 293, 439, 295, 613, 29882, 50648], "temperature": 0.0, "avg_logprob": -0.11937861496143126,
  "compression_ratio": 1.6521739130434783, "no_speech_prob": 0.0033078561536967754},
  {"id": 168, "seek": 71444, "start": 720.12, "end": 726.7600000000001, "text": "
  questions that you ask you know as problem statements on napkin math. I think that
  should almost", "tokens": [50648, 1651, 300, 291, 1029, 291, 458, 382, 1154, 12363,
  322, 9296, 5843, 5221, 13, 286, 519, 300, 820, 1920, 50980], "temperature": 0.0,
  "avg_logprob": -0.11937861496143126, "compression_ratio": 1.6521739130434783, "no_speech_prob":
  0.0033078561536967754}, {"id": 169, "seek": 71444, "start": 726.7600000000001, "end":
  734.2, "text": " bring up the internet archive version of it the the first version
  of TurboPuffer I had not", "tokens": [50980, 1565, 493, 264, 4705, 23507, 3037,
  295, 309, 264, 264, 700, 3037, 295, 35848, 47, 1245, 260, 286, 632, 406, 51352],
  "temperature": 0.0, "avg_logprob": -0.11937861496143126, "compression_ratio": 1.6521739130434783,
  "no_speech_prob": 0.0033078561536967754}, {"id": 170, "seek": 71444, "start": 734.2,
  "end": 742.6, "text": " thought about the business at all I didn''t have any launch
  playbook I had I had one of course all", "tokens": [51352, 1194, 466, 264, 1606,
  412, 439, 286, 994, 380, 362, 604, 4025, 862, 2939, 286, 632, 286, 632, 472, 295,
  1164, 439, 51772], "temperature": 0.0, "avg_logprob": -0.11937861496143126, "compression_ratio":
  1.6521739130434783, "no_speech_prob": 0.0033078561536967754}, {"id": 171, "seek":
  74260, "start": 742.6, "end": 746.84, "text": " the economics of what it would cost
  me to operate and spend a decent amount of time on the pricing", "tokens": [50364,
  264, 14564, 295, 437, 309, 576, 2063, 385, 281, 9651, 293, 3496, 257, 8681, 2372,
  295, 565, 322, 264, 17621, 50576], "temperature": 0.0, "avg_logprob": -0.11853224951941688,
  "compression_ratio": 1.7610294117647058, "no_speech_prob": 0.00045000307727605104},
  {"id": 172, "seek": 74260, "start": 746.84, "end": 751.88, "text": " because that
  felt like an important thing to spend time on at the time but there was really not",
  "tokens": [50576, 570, 300, 2762, 411, 364, 1021, 551, 281, 3496, 565, 322, 412,
  264, 565, 457, 456, 390, 534, 406, 50828], "temperature": 0.0, "avg_logprob": -0.11853224951941688,
  "compression_ratio": 1.7610294117647058, "no_speech_prob": 0.00045000307727605104},
  {"id": 173, "seek": 74260, "start": 751.88, "end": 757.88, "text": " much more than
  that of course the the Readwise team was very interested but at the time I could",
  "tokens": [50828, 709, 544, 813, 300, 295, 1164, 264, 264, 17604, 3711, 1469, 390,
  588, 3102, 457, 412, 264, 565, 286, 727, 51128], "temperature": 0.0, "avg_logprob":
  -0.11853224951941688, "compression_ratio": 1.7610294117647058, "no_speech_prob":
  0.00045000307727605104}, {"id": 174, "seek": 74260, "start": 757.88, "end": 762.6800000000001,
  "text": " barely do a you know I could just do around 10 million factors which is
  not enough for their use", "tokens": [51128, 10268, 360, 257, 291, 458, 286, 727,
  445, 360, 926, 1266, 2459, 6771, 597, 307, 406, 1547, 337, 641, 764, 51368], "temperature":
  0.0, "avg_logprob": -0.11853224951941688, "compression_ratio": 1.7610294117647058,
  "no_speech_prob": 0.00045000307727605104}, {"id": 175, "seek": 74260, "start": 762.6800000000001,
  "end": 771.08, "text": " case. I can screen share the website with you right here
  of what it looked like at the time", "tokens": [51368, 1389, 13, 286, 393, 2568,
  2073, 264, 3144, 365, 291, 558, 510, 295, 437, 309, 2956, 411, 412, 264, 565, 51788],
  "temperature": 0.0, "avg_logprob": -0.11853224951941688, "compression_ratio": 1.7610294117647058,
  "no_speech_prob": 0.00045000307727605104}, {"id": 176, "seek": 77108, "start": 771.72,
  "end": 777.64, "text": " and then we can get for the for the for the listening audience
  we can get your reaction", "tokens": [50396, 293, 550, 321, 393, 483, 337, 264,
  337, 264, 337, 264, 4764, 4034, 321, 393, 483, 428, 5480, 50692], "temperature":
  0.0, "avg_logprob": -0.12443925716258862, "compression_ratio": 1.8565891472868217,
  "no_speech_prob": 0.017964662984013557}, {"id": 177, "seek": 77108, "start": 777.64,
  "end": 782.44, "text": " but it was it was very simple I wouldn''t I wouldn''t put
  in any sophistication and it was honestly", "tokens": [50692, 457, 309, 390, 309,
  390, 588, 2199, 286, 2759, 380, 286, 2759, 380, 829, 294, 604, 15572, 399, 293,
  309, 390, 6095, 50932], "temperature": 0.0, "avg_logprob": -0.12443925716258862,
  "compression_ratio": 1.8565891472868217, "no_speech_prob": 0.017964662984013557},
  {"id": 178, "seek": 77108, "start": 782.44, "end": 787.48, "text": " I was exhausted
  I''ve been working on this like completely alone not telling anyone about it no",
  "tokens": [50932, 286, 390, 17992, 286, 600, 668, 1364, 322, 341, 411, 2584, 3312,
  406, 3585, 2878, 466, 309, 572, 51184], "temperature": 0.0, "avg_logprob": -0.12443925716258862,
  "compression_ratio": 1.8565891472868217, "no_speech_prob": 0.017964662984013557},
  {"id": 179, "seek": 77108, "start": 787.48, "end": 794.12, "text": " interested
  customers for like four months extremely focused like every single day and I couldn''t
  like", "tokens": [51184, 3102, 4581, 337, 411, 1451, 2493, 4664, 5178, 411, 633,
  2167, 786, 293, 286, 2809, 380, 411, 51516], "temperature": 0.0, "avg_logprob":
  -0.12443925716258862, "compression_ratio": 1.8565891472868217, "no_speech_prob":
  0.017964662984013557}, {"id": 180, "seek": 77108, "start": 794.12, "end": 798.2800000000001,
  "text": " you ask my wife she would say I was very distracted and she''s just like
  well how are you working", "tokens": [51516, 291, 1029, 452, 3836, 750, 576, 584,
  286, 390, 588, 21658, 293, 750, 311, 445, 411, 731, 577, 366, 291, 1364, 51724],
  "temperature": 0.0, "avg_logprob": -0.12443925716258862, "compression_ratio": 1.8565891472868217,
  "no_speech_prob": 0.017964662984013557}, {"id": 181, "seek": 79828, "start": 798.36,
  "end": 802.1999999999999, "text": " so hard on this like there''s no one on the
  team you don''t have any customer line up and I''m just like", "tokens": [50368,
  370, 1152, 322, 341, 411, 456, 311, 572, 472, 322, 264, 1469, 291, 500, 380, 362,
  604, 5474, 1622, 493, 293, 286, 478, 445, 411, 50560], "temperature": 0.0, "avg_logprob":
  -0.17285533029525008, "compression_ratio": 1.8901960784313725, "no_speech_prob":
  0.011518293991684914}, {"id": 182, "seek": 79828, "start": 802.76, "end": 810.04,
  "text": " someone has to do this and I I just launched it and I launched it I mean
  now I feel some", "tokens": [50588, 1580, 575, 281, 360, 341, 293, 286, 286, 445,
  8730, 309, 293, 286, 8730, 309, 286, 914, 586, 286, 841, 512, 50952], "temperature":
  0.0, "avg_logprob": -0.17285533029525008, "compression_ratio": 1.8901960784313725,
  "no_speech_prob": 0.011518293991684914}, {"id": 183, "seek": 79828, "start": 810.04,
  "end": 814.6, "text": " verising would be did launch it just couldn''t do that launch
  it was pretty slow I spent a bunch", "tokens": [50952, 1306, 3436, 576, 312, 630,
  4025, 309, 445, 2809, 380, 360, 300, 4025, 309, 390, 1238, 2964, 286, 4418, 257,
  3840, 51180], "temperature": 0.0, "avg_logprob": -0.17285533029525008, "compression_ratio":
  1.8901960784313725, "no_speech_prob": 0.011518293991684914}, {"id": 184, "seek":
  79828, "start": 814.6, "end": 819.9599999999999, "text": " of time actually trying
  to make it work in wasm and on the edge but it was too hard to make it fast", "tokens":
  [51180, 295, 565, 767, 1382, 281, 652, 309, 589, 294, 390, 76, 293, 322, 264, 4691,
  457, 309, 390, 886, 1152, 281, 652, 309, 2370, 51448], "temperature": 0.0, "avg_logprob":
  -0.17285533029525008, "compression_ratio": 1.8901960784313725, "no_speech_prob":
  0.011518293991684914}, {"id": 185, "seek": 79828, "start": 820.8399999999999, "end":
  825.56, "text": " and a bunch of other false starch like that on different types
  of a and end indexing structures", "tokens": [51492, 293, 257, 3840, 295, 661, 7908,
  24748, 411, 300, 322, 819, 3467, 295, 257, 293, 917, 8186, 278, 9227, 51728], "temperature":
  0.0, "avg_logprob": -0.17285533029525008, "compression_ratio": 1.8901960784313725,
  "no_speech_prob": 0.011518293991684914}, {"id": 186, "seek": 82556, "start": 825.56,
  "end": 830.1199999999999, "text": " we could talk about that as well and would be
  settled on but there was no real sophistication", "tokens": [50364, 321, 727, 751,
  466, 300, 382, 731, 293, 576, 312, 14819, 322, 457, 456, 390, 572, 957, 15572, 399,
  50592], "temperature": 0.0, "avg_logprob": -0.1474095086256663, "compression_ratio":
  1.737327188940092, "no_speech_prob": 0.019443301483988762}, {"id": 187, "seek":
  82556, "start": 830.1199999999999, "end": 834.92, "text": " in the go to market
  it was really just here it is here''s the outcome math here''s what it does", "tokens":
  [50592, 294, 264, 352, 281, 2142, 309, 390, 534, 445, 510, 309, 307, 510, 311, 264,
  9700, 5221, 510, 311, 437, 309, 775, 50832], "temperature": 0.0, "avg_logprob":
  -0.1474095086256663, "compression_ratio": 1.737327188940092, "no_speech_prob": 0.019443301483988762},
  {"id": 188, "seek": 82556, "start": 836.04, "end": 841.16, "text": " let''s see
  how the world takes it but I think when when when you sit on a well you didn''t
  sit on", "tokens": [50888, 718, 311, 536, 577, 264, 1002, 2516, 309, 457, 286, 519,
  562, 562, 562, 291, 1394, 322, 257, 731, 291, 994, 380, 1394, 322, 51144], "temperature":
  0.0, "avg_logprob": -0.1474095086256663, "compression_ratio": 1.737327188940092,
  "no_speech_prob": 0.019443301483988762}, {"id": 189, "seek": 82556, "start": 841.16,
  "end": 849.16, "text": " it yet but you had a cool like technology ID and mind right
  you knew you know it may play out", "tokens": [51144, 309, 1939, 457, 291, 632,
  257, 1627, 411, 2899, 7348, 293, 1575, 558, 291, 2586, 291, 458, 309, 815, 862,
  484, 51544], "temperature": 0.0, "avg_logprob": -0.1474095086256663, "compression_ratio":
  1.737327188940092, "no_speech_prob": 0.019443301483988762}, {"id": 190, "seek":
  84916, "start": 849.64, "end": 856.92, "text": " but also of course it required
  a lot of hard work like you said but after that after you see it fly", "tokens":
  [50388, 457, 611, 295, 1164, 309, 4739, 257, 688, 295, 1152, 589, 411, 291, 848,
  457, 934, 300, 934, 291, 536, 309, 3603, 50752], "temperature": 0.0, "avg_logprob":
  -0.13029775757720505, "compression_ratio": 1.6420454545454546, "no_speech_prob":
  0.007909717969596386}, {"id": 191, "seek": 84916, "start": 856.92, "end": 864.36,
  "text": " like on some small scale or whatever scale I think that brings you like
  that excitement to bring", "tokens": [50752, 411, 322, 512, 1359, 4373, 420, 2035,
  4373, 286, 519, 300, 5607, 291, 411, 300, 14755, 281, 1565, 51124], "temperature":
  0.0, "avg_logprob": -0.13029775757720505, "compression_ratio": 1.6420454545454546,
  "no_speech_prob": 0.007909717969596386}, {"id": 192, "seek": 84916, "start": 864.36,
  "end": 871.3199999999999, "text": " it to the world right so yeah I see you''re
  sharing the screen of the of the web archive page", "tokens": [51124, 309, 281,
  264, 1002, 558, 370, 1338, 286, 536, 291, 434, 5414, 264, 2568, 295, 264, 295, 264,
  3670, 23507, 3028, 51472], "temperature": 0.0, "avg_logprob": -0.13029775757720505,
  "compression_ratio": 1.6420454545454546, "no_speech_prob": 0.007909717969596386},
  {"id": 193, "seek": 87132, "start": 871.88, "end": 880.84, "text": " yeah that''s
  it very simple yeah yeah that''s awesome but yeah that''s actually a good segue
  to", "tokens": [50392, 1338, 300, 311, 309, 588, 2199, 1338, 1338, 300, 311, 3476,
  457, 1338, 300, 311, 767, 257, 665, 33850, 281, 50840], "temperature": 0.0, "avg_logprob":
  -0.16622103506059788, "compression_ratio": 1.7177914110429449, "no_speech_prob":
  0.014284927397966385}, {"id": 194, "seek": 87132, "start": 881.88, "end": 887.72,
  "text": " you know you probably know I''ve been at the emergence of the field of
  vector database field", "tokens": [50892, 291, 458, 291, 1391, 458, 286, 600, 668,
  412, 264, 36211, 295, 264, 2519, 295, 8062, 8149, 2519, 51184], "temperature": 0.0,
  "avg_logprob": -0.16622103506059788, "compression_ratio": 1.7177914110429449, "no_speech_prob":
  0.014284927397966385}, {"id": 195, "seek": 87132, "start": 888.5200000000001, "end":
  895.72, "text": " I''ve been I think I was the first probably to write just a simple
  block post with like you know", "tokens": [51224, 286, 600, 668, 286, 519, 286,
  390, 264, 700, 1391, 281, 2464, 445, 257, 2199, 3461, 2183, 365, 411, 291, 458,
  51584], "temperature": 0.0, "avg_logprob": -0.16622103506059788, "compression_ratio":
  1.7177914110429449, "no_speech_prob": 0.014284927397966385}, {"id": 196, "seek":
  89572, "start": 895.8000000000001, "end": 901.64, "text": " these crump snippets
  of what each vector database did and how they stand out and so on", "tokens": [50368,
  613, 941, 1420, 35623, 1385, 295, 437, 1184, 8062, 8149, 630, 293, 577, 436, 1463,
  484, 293, 370, 322, 50660], "temperature": 0.0, "avg_logprob": -0.12697281376008066,
  "compression_ratio": 1.8173076923076923, "no_speech_prob": 0.005139813758432865},
  {"id": 197, "seek": 89572, "start": 901.64, "end": 908.84, "text": " turbo buffer
  wasn''t there because turbo buffer was still in your mind I think but but the segue",
  "tokens": [50660, 20902, 21762, 2067, 380, 456, 570, 20902, 21762, 390, 920, 294,
  428, 1575, 286, 519, 457, 457, 264, 33850, 51020], "temperature": 0.0, "avg_logprob":
  -0.12697281376008066, "compression_ratio": 1.8173076923076923, "no_speech_prob":
  0.005139813758432865}, {"id": 198, "seek": 89572, "start": 908.84, "end": 918.12,
  "text": " here is I don''t have it covered in that block post but in your mind why
  were you not happy with", "tokens": [51020, 510, 307, 286, 500, 380, 362, 309, 5343,
  294, 300, 3461, 2183, 457, 294, 428, 1575, 983, 645, 291, 406, 2055, 365, 51484],
  "temperature": 0.0, "avg_logprob": -0.12697281376008066, "compression_ratio": 1.8173076923076923,
  "no_speech_prob": 0.005139813758432865}, {"id": 199, "seek": 89572, "start": 918.12,
  "end": 923.5600000000001, "text": " the vector date is like at large did you try
  all of them did you try some of them why did you think", "tokens": [51484, 264,
  8062, 4002, 307, 411, 412, 2416, 630, 291, 853, 439, 295, 552, 630, 291, 853, 512,
  295, 552, 983, 630, 291, 519, 51756], "temperature": 0.0, "avg_logprob": -0.12697281376008066,
  "compression_ratio": 1.8173076923076923, "no_speech_prob": 0.005139813758432865},
  {"id": 200, "seek": 92356, "start": 923.56, "end": 931.4, "text": " that a new vector
  database deserves to exist yeah I think I think it really just came back to the",
  "tokens": [50364, 300, 257, 777, 8062, 8149, 17037, 281, 2514, 1338, 286, 519, 286,
  519, 309, 534, 445, 1361, 646, 281, 264, 50756], "temperature": 0.0, "avg_logprob":
  -0.11996966801332624, "compression_ratio": 1.7354260089686098, "no_speech_prob":
  0.0017117963870987296}, {"id": 201, "seek": 92356, "start": 931.4, "end": 937.16,
  "text": " read wise example right there''s I there''s they look like great products
  I really like the API of", "tokens": [50756, 1401, 10829, 1365, 558, 456, 311, 286,
  456, 311, 436, 574, 411, 869, 3383, 286, 534, 411, 264, 9362, 295, 51044], "temperature":
  0.0, "avg_logprob": -0.11996966801332624, "compression_ratio": 1.7354260089686098,
  "no_speech_prob": 0.0017117963870987296}, {"id": 202, "seek": 92356, "start": 937.16,
  "end": 941.64, "text": " many of them they had lots of features that have taken
  me a long time to build that even features", "tokens": [51044, 867, 295, 552, 436,
  632, 3195, 295, 4122, 300, 362, 2726, 385, 257, 938, 565, 281, 1322, 300, 754, 4122,
  51268], "temperature": 0.0, "avg_logprob": -0.11996966801332624, "compression_ratio":
  1.7354260089686098, "no_speech_prob": 0.0017117963870987296}, {"id": 203, "seek":
  92356, "start": 941.64, "end": 945.8, "text": " that we don''t have today although
  we have a lot of features today compared to when we launched", "tokens": [51268,
  300, 321, 500, 380, 362, 965, 4878, 321, 362, 257, 688, 295, 4122, 965, 5347, 281,
  562, 321, 8730, 51476], "temperature": 0.0, "avg_logprob": -0.11996966801332624,
  "compression_ratio": 1.7354260089686098, "no_speech_prob": 0.0017117963870987296},
  {"id": 204, "seek": 94580, "start": 946.76, "end": 955.3199999999999, "text": "
  it came out of the cost piece that it felt that there was a lot of latent demand
  built up in", "tokens": [50412, 309, 1361, 484, 295, 264, 2063, 2522, 300, 309,
  2762, 300, 456, 390, 257, 688, 295, 48994, 4733, 3094, 493, 294, 50840], "temperature":
  0.0, "avg_logprob": -0.11499584804881703, "compression_ratio": 1.6711111111111112,
  "no_speech_prob": 0.019973021000623703}, {"id": 205, "seek": 94580, "start": 955.3199999999999,
  "end": 958.52, "text": " the market of people who wanted to use these things but
  it just didn''t make sense with the", "tokens": [50840, 264, 2142, 295, 561, 567,
  1415, 281, 764, 613, 721, 457, 309, 445, 994, 380, 652, 2020, 365, 264, 51000],
  "temperature": 0.0, "avg_logprob": -0.11499584804881703, "compression_ratio": 1.6711111111111112,
  "no_speech_prob": 0.019973021000623703}, {"id": 206, "seek": 94580, "start": 958.52,
  "end": 963.7199999999999, "text": " economics it''s very difficult to earn a return
  on search I mean I remember the search clusters", "tokens": [51000, 14564, 309,
  311, 588, 2252, 281, 6012, 257, 2736, 322, 3164, 286, 914, 286, 1604, 264, 3164,
  23313, 51260], "temperature": 0.0, "avg_logprob": -0.11499584804881703, "compression_ratio":
  1.6711111111111112, "no_speech_prob": 0.019973021000623703}, {"id": 207, "seek":
  94580, "start": 963.7199999999999, "end": 971.56, "text": " that Shopify were very
  expensive but ecommerce is a lot about search and so it was okay right but", "tokens":
  [51260, 300, 43991, 645, 588, 5124, 457, 308, 26926, 307, 257, 688, 466, 3164, 293,
  370, 309, 390, 1392, 558, 457, 51652], "temperature": 0.0, "avg_logprob": -0.11499584804881703,
  "compression_ratio": 1.6711111111111112, "no_speech_prob": 0.019973021000623703},
  {"id": 208, "seek": 97156, "start": 971.56, "end": 977.3199999999999, "text": "
  for a lot of companies search is a an important feature but is not the feature right
  and so the", "tokens": [50364, 337, 257, 688, 295, 3431, 3164, 307, 257, 364, 1021,
  4111, 457, 307, 406, 264, 4111, 558, 293, 370, 264, 50652], "temperature": 0.0,
  "avg_logprob": -0.10414466182742499, "compression_ratio": 1.8700787401574803, "no_speech_prob":
  0.00027143603074364364}, {"id": 209, "seek": 97156, "start": 977.3199999999999,
  "end": 982.04, "text": " per user economics just have to make sense it''s not that
  everyone just wants it in the cheapest", "tokens": [50652, 680, 4195, 14564, 445,
  362, 281, 652, 2020, 309, 311, 406, 300, 1518, 445, 2738, 309, 294, 264, 29167,
  50888], "temperature": 0.0, "avg_logprob": -0.10414466182742499, "compression_ratio":
  1.8700787401574803, "no_speech_prob": 0.00027143603074364364}, {"id": 210, "seek":
  97156, "start": 982.04, "end": 987.56, "text": " possible way is that if you invest
  in infrastructure you have to get a return on that investment", "tokens": [50888,
  1944, 636, 307, 300, 498, 291, 1963, 294, 6896, 291, 362, 281, 483, 257, 2736, 322,
  300, 6078, 51164], "temperature": 0.0, "avg_logprob": -0.10414466182742499, "compression_ratio":
  1.8700787401574803, "no_speech_prob": 0.00027143603074364364}, {"id": 211, "seek":
  97156, "start": 988.04, "end": 992.1199999999999, "text": " and it felt that I knew
  that I''d read wise they could get a return on that investment but it", "tokens":
  [51188, 293, 309, 2762, 300, 286, 2586, 300, 286, 1116, 1401, 10829, 436, 727, 483,
  257, 2736, 322, 300, 6078, 457, 309, 51392], "temperature": 0.0, "avg_logprob":
  -0.10414466182742499, "compression_ratio": 1.8700787401574803, "no_speech_prob":
  0.00027143603074364364}, {"id": 212, "seek": 97156, "start": 992.1199999999999,
  "end": 996.1999999999999, "text": " wasn''t on 30 grand a month it was maybe close
  at a 3 grand or 5 grand a month that they would", "tokens": [51392, 2067, 380, 322,
  2217, 2697, 257, 1618, 309, 390, 1310, 1998, 412, 257, 805, 2697, 420, 1025, 2697,
  257, 1618, 300, 436, 576, 51596], "temperature": 0.0, "avg_logprob": -0.10414466182742499,
  "compression_ratio": 1.8700787401574803, "no_speech_prob": 0.00027143603074364364},
  {"id": 213, "seek": 99620, "start": 996.76, "end": 1000.6800000000001, "text": "
  feel that they could earn a return on that feature and gender conversion engagement
  and whatever", "tokens": [50392, 841, 300, 436, 727, 6012, 257, 2736, 322, 300,
  4111, 293, 7898, 14298, 8742, 293, 2035, 50588], "temperature": 0.0, "avg_logprob":
  -0.17379162528298117, "compression_ratio": 1.9015748031496063, "no_speech_prob":
  0.01238193828612566}, {"id": 214, "seek": 99620, "start": 1001.88, "end": 1008.0400000000001,
  "text": " so it was really about the storage architecture and I think that when
  I think about databases now", "tokens": [50648, 370, 309, 390, 534, 466, 264, 6725,
  9482, 293, 286, 519, 300, 562, 286, 519, 466, 22380, 586, 50956], "temperature":
  0.0, "avg_logprob": -0.17379162528298117, "compression_ratio": 1.9015748031496063,
  "no_speech_prob": 0.01238193828612566}, {"id": 215, "seek": 99620, "start": 1008.0400000000001,
  "end": 1012.9200000000001, "text": " this was not as coherent to me at the time
  at the time I was driven by the Nipkin Math Naptkin Math", "tokens": [50956, 341,
  390, 406, 382, 36239, 281, 385, 412, 264, 565, 412, 264, 565, 286, 390, 9555, 538,
  264, 426, 647, 5843, 15776, 426, 2796, 5843, 15776, 51200], "temperature": 0.0,
  "avg_logprob": -0.17379162528298117, "compression_ratio": 1.9015748031496063, "no_speech_prob":
  0.01238193828612566}, {"id": 216, "seek": 99620, "start": 1012.9200000000001, "end":
  1018.0400000000001, "text": " not the not the market nothing else it was based on
  one qualitative experience and an Naptkin", "tokens": [51200, 406, 264, 406, 264,
  2142, 1825, 1646, 309, 390, 2361, 322, 472, 31312, 1752, 293, 364, 426, 2796, 5843,
  51456], "temperature": 0.0, "avg_logprob": -0.17379162528298117, "compression_ratio":
  1.9015748031496063, "no_speech_prob": 0.01238193828612566}, {"id": 217, "seek":
  99620, "start": 1018.0400000000001, "end": 1023.0, "text": " Math there was nothing
  else in it and speak about it in a more sophisticated way now being you", "tokens":
  [51456, 15776, 456, 390, 1825, 1646, 294, 309, 293, 1710, 466, 309, 294, 257, 544,
  16950, 636, 586, 885, 291, 51704], "temperature": 0.0, "avg_logprob": -0.17379162528298117,
  "compression_ratio": 1.9015748031496063, "no_speech_prob": 0.01238193828612566},
  {"id": 218, "seek": 102300, "start": 1023.16, "end": 1028.68, "text": " know having
  learned a lot about go-to-market sense but the that those were that''s really all
  that", "tokens": [50372, 458, 1419, 3264, 257, 688, 466, 352, 12, 1353, 12, 16414,
  2020, 457, 264, 300, 729, 645, 300, 311, 534, 439, 300, 50648], "temperature": 0.0,
  "avg_logprob": -0.1142035456537043, "compression_ratio": 1.8458498023715415, "no_speech_prob":
  0.006433083210140467}, {"id": 219, "seek": 102300, "start": 1028.68, "end": 1032.68,
  "text": " was at the time it was an insight on those two things the best ideas right
  are", "tokens": [50648, 390, 412, 264, 565, 309, 390, 364, 11269, 322, 729, 732,
  721, 264, 1151, 3487, 558, 366, 50848], "temperature": 0.0, "avg_logprob": -0.1142035456537043,
  "compression_ratio": 1.8458498023715415, "no_speech_prob": 0.006433083210140467},
  {"id": 220, "seek": 102300, "start": 1034.92, "end": 1039.48, "text": " simultaneous
  inventions right someone else would have done it six months later probably other
  people", "tokens": [50960, 46218, 43748, 558, 1580, 1646, 576, 362, 1096, 309, 2309,
  2493, 1780, 1391, 661, 561, 51188], "temperature": 0.0, "avg_logprob": -0.1142035456537043,
  "compression_ratio": 1.8458498023715415, "no_speech_prob": 0.006433083210140467},
  {"id": 221, "seek": 102300, "start": 1039.48, "end": 1044.12, "text": " were doing
  it at the time that launched a later right we were the first to launch with this",
  "tokens": [51188, 645, 884, 309, 412, 264, 565, 300, 8730, 257, 1780, 558, 321,
  645, 264, 700, 281, 4025, 365, 341, 51420], "temperature": 0.0, "avg_logprob": -0.1142035456537043,
  "compression_ratio": 1.8458498023715415, "no_speech_prob": 0.006433083210140467},
  {"id": 222, "seek": 102300, "start": 1044.12, "end": 1049.72, "text": " particular
  architecture but it was out there for the grappling right the idea was in the air
  like", "tokens": [51420, 1729, 9482, 457, 309, 390, 484, 456, 337, 264, 50086, 558,
  264, 1558, 390, 294, 264, 1988, 411, 51700], "temperature": 0.0, "avg_logprob":
  -0.1142035456537043, "compression_ratio": 1.8458498023715415, "no_speech_prob":
  0.006433083210140467}, {"id": 223, "seek": 104972, "start": 1049.72, "end": 1056.52,
  "text": " s3 had the the dpites now finally so the way that I think about this to
  really boil this down is that", "tokens": [50364, 262, 18, 632, 264, 264, 274, 79,
  3324, 586, 2721, 370, 264, 636, 300, 286, 519, 466, 341, 281, 534, 13329, 341, 760,
  307, 300, 50704], "temperature": 0.0, "avg_logprob": -0.1946304722836143, "compression_ratio":
  1.7767857142857142, "no_speech_prob": 0.0029727707151323557}, {"id": 224, "seek":
  104972, "start": 1057.08, "end": 1065.88, "text": " if you want to create a generational
  database company I think you need two things you need a new", "tokens": [50732,
  498, 291, 528, 281, 1884, 257, 48320, 8149, 2237, 286, 519, 291, 643, 732, 721,
  291, 643, 257, 777, 51172], "temperature": 0.0, "avg_logprob": -0.1946304722836143,
  "compression_ratio": 1.7767857142857142, "no_speech_prob": 0.0029727707151323557},
  {"id": 225, "seek": 104972, "start": 1065.88, "end": 1073.08, "text": " workload
  the new workload here is that we have almost every company on earth sits on their
  treasure", "tokens": [51172, 20139, 264, 777, 20139, 510, 307, 300, 321, 362, 1920,
  633, 2237, 322, 4120, 12696, 322, 641, 12985, 51532], "temperature": 0.0, "avg_logprob":
  -0.1946304722836143, "compression_ratio": 1.7767857142857142, "no_speech_prob":
  0.0029727707151323557}, {"id": 226, "seek": 104972, "start": 1073.08, "end": 1078.76,
  "text": " troll of data and they want to connect that to LLAMs especially all the
  unstructured data that it''s", "tokens": [51532, 20680, 295, 1412, 293, 436, 528,
  281, 1745, 300, 281, 441, 43, 2865, 82, 2318, 439, 264, 18799, 46847, 1412, 300,
  309, 311, 51816], "temperature": 0.0, "avg_logprob": -0.1946304722836143, "compression_ratio":
  1.7767857142857142, "no_speech_prob": 0.0029727707151323557}, {"id": 227, "seek":
  107876, "start": 1078.76, "end": 1085.32, "text": " always been very difficult to
  do we did this for structured data into 2010s the new workload was", "tokens": [50364,
  1009, 668, 588, 2252, 281, 360, 321, 630, 341, 337, 18519, 1412, 666, 9657, 82,
  264, 777, 20139, 390, 50692], "temperature": 0.0, "avg_logprob": -0.05884032828785549,
  "compression_ratio": 1.904382470119522, "no_speech_prob": 0.0002787653647828847},
  {"id": 228, "seek": 107876, "start": 1085.32, "end": 1091.4, "text": " that we wanted
  to do analytics on billions tens of billions trillions of rows of structured data",
  "tokens": [50692, 300, 321, 1415, 281, 360, 15370, 322, 17375, 10688, 295, 17375,
  504, 46279, 295, 13241, 295, 18519, 1412, 50996], "temperature": 0.0, "avg_logprob":
  -0.05884032828785549, "compression_ratio": 1.904382470119522, "no_speech_prob":
  0.0002787653647828847}, {"id": 229, "seek": 107876, "start": 1091.4, "end": 1096.76,
  "text": " but now with LLAMs we''re entering into that with the unstructured data
  that''s the first thing we", "tokens": [50996, 457, 586, 365, 441, 43, 2865, 82,
  321, 434, 11104, 666, 300, 365, 264, 18799, 46847, 1412, 300, 311, 264, 700, 551,
  321, 51264], "temperature": 0.0, "avg_logprob": -0.05884032828785549, "compression_ratio":
  1.904382470119522, "no_speech_prob": 0.0002787653647828847}, {"id": 230, "seek":
  107876, "start": 1096.76, "end": 1101.56, "text": " needed new workload because
  that''s when people go out shopping for a new database the second thing", "tokens":
  [51264, 2978, 777, 20139, 570, 300, 311, 562, 561, 352, 484, 8688, 337, 257, 777,
  8149, 264, 1150, 551, 51504], "temperature": 0.0, "avg_logprob": -0.05884032828785549,
  "compression_ratio": 1.904382470119522, "no_speech_prob": 0.0002787653647828847},
  {"id": 231, "seek": 107876, "start": 1101.56, "end": 1106.92, "text": " that you
  need is a new storage architecture if you don''t have a new storage architecture",
  "tokens": [51504, 300, 291, 643, 307, 257, 777, 6725, 9482, 498, 291, 500, 380,
  362, 257, 777, 6725, 9482, 51772], "temperature": 0.0, "avg_logprob": -0.05884032828785549,
  "compression_ratio": 1.904382470119522, "no_speech_prob": 0.0002787653647828847},
  {"id": 232, "seek": 110692, "start": 1107.72, "end": 1114.76, "text": " that is
  fundamentally a better tradeoff for the particular workload then there''s no reason
  why", "tokens": [50404, 300, 307, 17879, 257, 1101, 4923, 4506, 337, 264, 1729,
  20139, 550, 456, 311, 572, 1778, 983, 50756], "temperature": 0.0, "avg_logprob":
  -0.1266285281315028, "compression_ratio": 1.6782006920415224, "no_speech_prob":
  0.0055726319551467896}, {"id": 233, "seek": 110692, "start": 1114.76, "end": 1120.6000000000001,
  "text": " tacking on a secondary index to your relational database to your OLAB
  to your existing search engine", "tokens": [50756, 9426, 278, 322, 257, 11396, 8186,
  281, 428, 38444, 8149, 281, 428, 39191, 13868, 281, 428, 6741, 3164, 2848, 51048],
  "temperature": 0.0, "avg_logprob": -0.1266285281315028, "compression_ratio": 1.6782006920415224,
  "no_speech_prob": 0.0055726319551467896}, {"id": 234, "seek": 110692, "start": 1121.5600000000002,
  "end": 1125.48, "text": " they would eat it I would have made that decision in the
  shoes that Shopify right it''s like well", "tokens": [51096, 436, 576, 1862, 309,
  286, 576, 362, 1027, 300, 3537, 294, 264, 6654, 300, 43991, 558, 309, 311, 411,
  731, 51292], "temperature": 0.0, "avg_logprob": -0.1266285281315028, "compression_ratio":
  1.6782006920415224, "no_speech_prob": 0.0055726319551467896}, {"id": 235, "seek":
  110692, "start": 1126.1200000000001, "end": 1131.24, "text": " this database like
  has a really good vector index but it doesn''t bring anything new in terms of",
  "tokens": [51324, 341, 8149, 411, 575, 257, 534, 665, 8062, 8186, 457, 309, 1177,
  380, 1565, 1340, 777, 294, 2115, 295, 51580], "temperature": 0.0, "avg_logprob":
  -0.1266285281315028, "compression_ratio": 1.6782006920415224, "no_speech_prob":
  0.0055726319551467896}, {"id": 236, "seek": 110692, "start": 1131.24, "end": 1136.3600000000001,
  "text": " the storage architecture so we''re just going to invest in the mySQL extension
  right it''s what we", "tokens": [51580, 264, 6725, 9482, 370, 321, 434, 445, 516,
  281, 1963, 294, 264, 452, 39934, 10320, 558, 309, 311, 437, 321, 51836], "temperature":
  0.0, "avg_logprob": -0.1266285281315028, "compression_ratio": 1.6782006920415224,
  "no_speech_prob": 0.0055726319551467896}, {"id": 237, "seek": 113636, "start": 1136.36,
  "end": 1144.04, "text": " really want to Shopify or the uh Lucine Lucine workload
  right these are great databases they''ve stood", "tokens": [50364, 534, 528, 281,
  43991, 420, 264, 2232, 9593, 533, 9593, 533, 20139, 558, 613, 366, 869, 22380, 436,
  600, 9371, 50748], "temperature": 0.0, "avg_logprob": -0.17347704922711407, "compression_ratio":
  1.7580071174377223, "no_speech_prob": 0.0009361585252918303}, {"id": 238, "seek":
  113636, "start": 1144.04, "end": 1148.6799999999998, "text": " the test of time
  and when you''re on call you become very conservative in what you adopt for new",
  "tokens": [50748, 264, 1500, 295, 565, 293, 562, 291, 434, 322, 818, 291, 1813,
  588, 13780, 294, 437, 291, 6878, 337, 777, 50980], "temperature": 0.0, "avg_logprob":
  -0.17347704922711407, "compression_ratio": 1.7580071174377223, "no_speech_prob":
  0.0009361585252918303}, {"id": 239, "seek": 113636, "start": 1148.6799999999998,
  "end": 1154.28, "text": " workloads but you cannot ignore a new storage architecture
  that is an order of magnitude cheaper", "tokens": [50980, 32452, 457, 291, 2644,
  11200, 257, 777, 6725, 9482, 300, 307, 364, 1668, 295, 15668, 12284, 51260], "temperature":
  0.0, "avg_logprob": -0.17347704922711407, "compression_ratio": 1.7580071174377223,
  "no_speech_prob": 0.0009361585252918303}, {"id": 240, "seek": 113636, "start": 1154.28,
  "end": 1160.9199999999998, "text": " than the previous one when you store a gigabyte
  of data in a traditional storage engine you have to", "tokens": [51260, 813, 264,
  3894, 472, 562, 291, 3531, 257, 8741, 34529, 295, 1412, 294, 257, 5164, 6725, 2848,
  291, 362, 281, 51592], "temperature": 0.0, "avg_logprob": -0.17347704922711407,
  "compression_ratio": 1.7580071174377223, "no_speech_prob": 0.0009361585252918303},
  {"id": 241, "seek": 113636, "start": 1160.9199999999998, "end": 1165.8799999999999,
  "text": " replicate that to three disks maybe two if you have a little bit or if
  you have more risk tolerance", "tokens": [51592, 25356, 300, 281, 1045, 41617, 1310,
  732, 498, 291, 362, 257, 707, 857, 420, 498, 291, 362, 544, 3148, 23368, 51840],
  "temperature": 0.0, "avg_logprob": -0.17347704922711407, "compression_ratio": 1.7580071174377223,
  "no_speech_prob": 0.0009361585252918303}, {"id": 242, "seek": 116588, "start": 1165.88,
  "end": 1172.3600000000001, "text": " but likely three a gigabyte of disk with from
  the cloud vendors cost about 10 cents you run it at 50%", "tokens": [50364, 457,
  3700, 1045, 257, 8741, 34529, 295, 12355, 365, 490, 264, 4588, 22056, 2063, 466,
  1266, 14941, 291, 1190, 309, 412, 2625, 4, 50688], "temperature": 0.0, "avg_logprob":
  -0.13840070743005253, "compression_ratio": 1.7654867256637168, "no_speech_prob":
  0.0005042491247877479}, {"id": 243, "seek": 116588, "start": 1172.3600000000001,
  "end": 1178.5200000000002, "text": " utilization otherwise it''s too scary to be
  on call 20 cents per gigabyte times three for all the", "tokens": [50688, 37074,
  5911, 309, 311, 886, 6958, 281, 312, 322, 818, 945, 14941, 680, 8741, 34529, 1413,
  1045, 337, 439, 264, 50996], "temperature": 0.0, "avg_logprob": -0.13840070743005253,
  "compression_ratio": 1.7654867256637168, "no_speech_prob": 0.0005042491247877479},
  {"id": 244, "seek": 116588, "start": 1178.5200000000002, "end": 1186.0400000000002,
  "text": " replicas 60 cents per gigabyte obi storage is two cents per gigabyte right
  so it''s it''s it''s 30 times", "tokens": [50996, 3248, 9150, 4060, 14941, 680,
  8741, 34529, 1111, 72, 6725, 307, 732, 14941, 680, 8741, 34529, 558, 370, 309, 311,
  309, 311, 309, 311, 2217, 1413, 51372], "temperature": 0.0, "avg_logprob": -0.13840070743005253,
  "compression_ratio": 1.7654867256637168, "no_speech_prob": 0.0005042491247877479},
  {"id": 245, "seek": 116588, "start": 1186.0400000000002, "end": 1191.96, "text":
  " cheaper if it''s all cold now by the time you have some of it in SSD and you have
  it in memory then", "tokens": [51372, 12284, 498, 309, 311, 439, 3554, 586, 538,
  264, 565, 291, 362, 512, 295, 309, 294, 30262, 293, 291, 362, 309, 294, 4675, 550,
  51668], "temperature": 0.0, "avg_logprob": -0.13840070743005253, "compression_ratio":
  1.7654867256637168, "no_speech_prob": 0.0005042491247877479}, {"id": 246, "seek":
  119196, "start": 1191.96, "end": 1197.96, "text": " the blended cost ends up being
  different but it tracks the actual value to the customer even if you", "tokens":
  [50364, 264, 27048, 2063, 5314, 493, 885, 819, 457, 309, 10218, 264, 3539, 2158,
  281, 264, 5474, 754, 498, 291, 50664], "temperature": 0.0, "avg_logprob": -0.1048102719443185,
  "compression_ratio": 1.855513307984791, "no_speech_prob": 0.0005112163489684463},
  {"id": 247, "seek": 119196, "start": 1197.96, "end": 1202.92, "text": " have all
  of that in disk well you only need one copy right and that disk you can run it at
  100%", "tokens": [50664, 362, 439, 295, 300, 294, 12355, 731, 291, 787, 643, 472,
  5055, 558, 293, 300, 12355, 291, 393, 1190, 309, 412, 2319, 4, 50912], "temperature":
  0.0, "avg_logprob": -0.1048102719443185, "compression_ratio": 1.855513307984791,
  "no_speech_prob": 0.0005112163489684463}, {"id": 248, "seek": 119196, "start": 1202.92,
  "end": 1207.72, "text": " utilization meaning the blended cost is now 12 cents per
  gigabyte right so the 10 cents 100%", "tokens": [50912, 37074, 3620, 264, 27048,
  2063, 307, 586, 2272, 14941, 680, 8741, 34529, 558, 370, 264, 1266, 14941, 2319,
  4, 51152], "temperature": 0.0, "avg_logprob": -0.1048102719443185, "compression_ratio":
  1.855513307984791, "no_speech_prob": 0.0005112163489684463}, {"id": 249, "seek":
  119196, "start": 1207.72, "end": 1213.32, "text": " utilization plus the two cents
  per gigabyte for obi storage so now you have the ingredients of a", "tokens": [51152,
  37074, 1804, 264, 732, 14941, 680, 8741, 34529, 337, 1111, 72, 6725, 370, 586, 291,
  362, 264, 6952, 295, 257, 51432], "temperature": 0.0, "avg_logprob": -0.1048102719443185,
  "compression_ratio": 1.855513307984791, "no_speech_prob": 0.0005112163489684463},
  {"id": 250, "seek": 119196, "start": 1213.32, "end": 1219.0, "text": " new actual
  database you have a new workload right which is which makes means that people are
  out there", "tokens": [51432, 777, 3539, 8149, 291, 362, 257, 777, 20139, 558, 597,
  307, 597, 1669, 1355, 300, 561, 366, 484, 456, 51716], "temperature": 0.0, "avg_logprob":
  -0.1048102719443185, "compression_ratio": 1.855513307984791, "no_speech_prob": 0.0005112163489684463},
  {"id": 251, "seek": 121900, "start": 1219.0, "end": 1223.64, "text": " trying to
  look for ways to connect their data to LLMs and then you have the second ingredient
  which", "tokens": [50364, 1382, 281, 574, 337, 2098, 281, 1745, 641, 1412, 281,
  441, 43, 26386, 293, 550, 291, 362, 264, 1150, 14751, 597, 50596], "temperature":
  0.0, "avg_logprob": -0.13403476987566268, "compression_ratio": 1.7491166077738516,
  "no_speech_prob": 0.00047771018580533564}, {"id": 252, "seek": 121900, "start":
  1223.64, "end": 1229.08, "text": " is a new storage architecture that allows them
  to do it in order of magnitude easier and cheaper", "tokens": [50596, 307, 257,
  777, 6725, 9482, 300, 4045, 552, 281, 360, 309, 294, 1668, 295, 15668, 3571, 293,
  12284, 50868], "temperature": 0.0, "avg_logprob": -0.13403476987566268, "compression_ratio":
  1.7491166077738516, "no_speech_prob": 0.00047771018580533564}, {"id": 253, "seek":
  121900, "start": 1229.08, "end": 1234.36, "text": " than what they can do when they''re
  existing architectures and this matters because vectors are so big", "tokens": [50868,
  813, 437, 436, 393, 360, 562, 436, 434, 6741, 6331, 1303, 293, 341, 7001, 570, 18875,
  366, 370, 955, 51132], "temperature": 0.0, "avg_logprob": -0.13403476987566268,
  "compression_ratio": 1.7491166077738516, "no_speech_prob": 0.00047771018580533564},
  {"id": 254, "seek": 121900, "start": 1234.36, "end": 1240.28, "text": " right a
  kilobyte of text easily turns into tens of kilobytes of vector data yeah yeah it''s
  absolutely", "tokens": [51132, 558, 257, 5128, 13944, 975, 295, 2487, 3612, 4523,
  666, 10688, 295, 5128, 996, 43673, 295, 8062, 1412, 1338, 1338, 309, 311, 3122,
  51428], "temperature": 0.0, "avg_logprob": -0.13403476987566268, "compression_ratio":
  1.7491166077738516, "no_speech_prob": 0.00047771018580533564}, {"id": 255, "seek":
  121900, "start": 1240.28, "end": 1248.12, "text": " true one other thing that I
  kept keep hearing or kept hearing about you know whether or not to", "tokens": [51428,
  2074, 472, 661, 551, 300, 286, 4305, 1066, 4763, 420, 4305, 4763, 466, 291, 458,
  1968, 420, 406, 281, 51820], "temperature": 0.0, "avg_logprob": -0.13403476987566268,
  "compression_ratio": 1.7491166077738516, "no_speech_prob": 0.00047771018580533564},
  {"id": 256, "seek": 124812, "start": 1248.12, "end": 1254.9199999999998, "text":
  " introduce a vector search in the mix for some really heavy workloads is that it
  will bring", "tokens": [50364, 5366, 257, 8062, 3164, 294, 264, 2890, 337, 512,
  534, 4676, 32452, 307, 300, 309, 486, 1565, 50704], "temperature": 0.0, "avg_logprob":
  -0.12134440926944508, "compression_ratio": 1.6888888888888889, "no_speech_prob":
  0.0005005528219044209}, {"id": 257, "seek": 124812, "start": 1255.9599999999998,
  "end": 1261.08, "text": " certain latency on top that we cannot tolerate right for
  example if you run a hybrid search", "tokens": [50756, 1629, 27043, 322, 1192, 300,
  321, 2644, 25773, 558, 337, 1365, 498, 291, 1190, 257, 13051, 3164, 51012], "temperature":
  0.0, "avg_logprob": -0.12134440926944508, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.0005005528219044209}, {"id": 258, "seek": 124812, "start": 1261.08,
  "end": 1267.08, "text": " like you guys have implemented as well you know one of
  these will be slowest and therefore you", "tokens": [51012, 411, 291, 1074, 362,
  12270, 382, 731, 291, 458, 472, 295, 613, 486, 312, 2964, 377, 293, 4412, 291, 51312],
  "temperature": 0.0, "avg_logprob": -0.12134440926944508, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.0005005528219044209}, {"id": 259, "seek": 124812, "start": 1267.08,
  "end": 1272.84, "text": " will have to wait for that slowest component and so if
  it adds I don''t know a few hundred milliseconds", "tokens": [51312, 486, 362, 281,
  1699, 337, 300, 2964, 377, 6542, 293, 370, 498, 309, 10860, 286, 500, 380, 458,
  257, 1326, 3262, 34184, 51600], "temperature": 0.0, "avg_logprob": -0.12134440926944508,
  "compression_ratio": 1.6888888888888889, "no_speech_prob": 0.0005005528219044209},
  {"id": 260, "seek": 127284, "start": 1272.84, "end": 1277.3999999999999, "text":
  " on top of your original you know retrieval mechanism then it''s going to be an
  off-line", "tokens": [50364, 322, 1192, 295, 428, 3380, 291, 458, 19817, 3337, 7513,
  550, 309, 311, 516, 281, 312, 364, 766, 12, 1889, 50592], "temperature": 0.0, "avg_logprob":
  -0.12013372533461626, "compression_ratio": 1.6818181818181819, "no_speech_prob":
  0.001628653146326542}, {"id": 261, "seek": 127284, "start": 1278.1999999999998,
  "end": 1283.08, "text": " what''s your take on that have you thought obviously you
  have thought about that what''s the", "tokens": [50632, 437, 311, 428, 747, 322,
  300, 362, 291, 1194, 2745, 291, 362, 1194, 466, 300, 437, 311, 264, 50876], "temperature":
  0.0, "avg_logprob": -0.12013372533461626, "compression_ratio": 1.6818181818181819,
  "no_speech_prob": 0.001628653146326542}, {"id": 262, "seek": 127284, "start": 1283.08,
  "end": 1291.8799999999999, "text": " edge that turbo buffer brings in this space
  over maybe pure databases yeah I think I think there''s", "tokens": [50876, 4691,
  300, 20902, 21762, 5607, 294, 341, 1901, 670, 1310, 6075, 22380, 1338, 286, 519,
  286, 519, 456, 311, 51316], "temperature": 0.0, "avg_logprob": -0.12013372533461626,
  "compression_ratio": 1.6818181818181819, "no_speech_prob": 0.001628653146326542},
  {"id": 263, "seek": 127284, "start": 1291.8799999999999, "end": 1298.52, "text":
  " we see two types of ways that people adopt vector databases or turbo buffer we
  don''t consider", "tokens": [51316, 321, 536, 732, 3467, 295, 2098, 300, 561, 6878,
  8062, 22380, 420, 20902, 21762, 321, 500, 380, 1949, 51648], "temperature": 0.0,
  "avg_logprob": -0.12013372533461626, "compression_ratio": 1.6818181818181819, "no_speech_prob":
  0.001628653146326542}, {"id": 264, "seek": 129852, "start": 1299.48, "end": 1304.84,
  "text": " turbo buffer a pure play vector database we consider it a search engine
  we actually consider it", "tokens": [50412, 20902, 21762, 257, 6075, 862, 8062,
  8149, 321, 1949, 309, 257, 3164, 2848, 321, 767, 1949, 309, 50680], "temperature":
  0.0, "avg_logprob": -0.14007179825394242, "compression_ratio": 1.8803088803088803,
  "no_speech_prob": 0.002767975674942136}, {"id": 265, "seek": 129852, "start": 1304.84,
  "end": 1311.56, "text": " a full database because there''s a full generic LSM underneath
  all of that and we consider that the", "tokens": [50680, 257, 1577, 8149, 570, 456,
  311, 257, 1577, 19577, 441, 26693, 7223, 439, 295, 300, 293, 321, 1949, 300, 264,
  51016], "temperature": 0.0, "avg_logprob": -0.14007179825394242, "compression_ratio":
  1.8803088803088803, "no_speech_prob": 0.002767975674942136}, {"id": 266, "seek":
  129852, "start": 1311.56, "end": 1316.12, "text": " actual acid of turbo puffer
  is an LSM that''s obnox storage native and doesn''t rely on any state", "tokens":
  [51016, 3539, 8258, 295, 20902, 19613, 260, 307, 364, 441, 26693, 300, 311, 1111,
  29129, 6725, 8470, 293, 1177, 380, 10687, 322, 604, 1785, 51244], "temperature":
  0.0, "avg_logprob": -0.14007179825394242, "compression_ratio": 1.8803088803088803,
  "no_speech_prob": 0.002767975674942136}, {"id": 267, "seek": 129852, "start": 1317.08,
  "end": 1321.32, "text": " we just think that the vector index and the search engine
  index is what the market needed the most", "tokens": [51292, 321, 445, 519, 300,
  264, 8062, 8186, 293, 264, 3164, 2848, 8186, 307, 437, 264, 2142, 2978, 264, 881,
  51504], "temperature": 0.0, "avg_logprob": -0.14007179825394242, "compression_ratio":
  1.8803088803088803, "no_speech_prob": 0.002767975674942136}, {"id": 268, "seek":
  129852, "start": 1321.32, "end": 1327.72, "text": " so let''s speak about latency
  there''s no real fundamental latency trade off with this architecture", "tokens":
  [51504, 370, 718, 311, 1710, 466, 27043, 456, 311, 572, 957, 8088, 27043, 4923,
  766, 365, 341, 9482, 51824], "temperature": 0.0, "avg_logprob": -0.14007179825394242,
  "compression_ratio": 1.8803088803088803, "no_speech_prob": 0.002767975674942136},
  {"id": 269, "seek": 132772, "start": 1327.72, "end": 1332.84, "text": " the only
  thing is that once in a while you will hit that cold query but the entire databases",
  "tokens": [50364, 264, 787, 551, 307, 300, 1564, 294, 257, 1339, 291, 486, 2045,
  300, 3554, 14581, 457, 264, 2302, 22380, 50620], "temperature": 0.0, "avg_logprob":
  -0.1923782876197328, "compression_ratio": 1.737556561085973, "no_speech_prob": 0.0024514971300959587},
  {"id": 270, "seek": 132772, "start": 1332.84, "end": 1339.56, "text": " optimize
  the round minimizing the amount of round trips that you do to SS3 S3 you can max
  out a", "tokens": [50620, 19719, 264, 3098, 46608, 264, 2372, 295, 3098, 16051,
  300, 291, 360, 281, 12238, 18, 318, 18, 291, 393, 11469, 484, 257, 50956], "temperature":
  0.0, "avg_logprob": -0.1923782876197328, "compression_ratio": 1.737556561085973,
  "no_speech_prob": 0.0024514971300959587}, {"id": 271, "seek": 132772, "start": 1340.84,
  "end": 1346.3600000000001, "text": " a network card right so you can get on a gcp
  or AWS box you can get 50 to 100 gigabytes per second", "tokens": [51020, 257, 3209,
  2920, 558, 370, 291, 393, 483, 322, 257, 290, 66, 79, 420, 17650, 2424, 291, 393,
  483, 2625, 281, 2319, 42741, 680, 1150, 51296], "temperature": 0.0, "avg_logprob":
  -0.1923782876197328, "compression_ratio": 1.737556561085973, "no_speech_prob": 0.0024514971300959587},
  {"id": 272, "seek": 132772, "start": 1346.3600000000001, "end": 1352.68, "text":
  " of network bandwidth you give it per second of network bandwidth so this is similar
  to this band", "tokens": [51296, 295, 3209, 23647, 291, 976, 309, 680, 1150, 295,
  3209, 23647, 370, 341, 307, 2531, 281, 341, 4116, 51612], "temperature": 0.0, "avg_logprob":
  -0.1923782876197328, "compression_ratio": 1.737556561085973, "no_speech_prob": 0.0024514971300959587},
  {"id": 273, "seek": 135268, "start": 1353.16, "end": 1357.72, "text": " with the
  latency actually even better in the clouds often than disks even with SSDs even
  with N and", "tokens": [50388, 365, 264, 27043, 767, 754, 1101, 294, 264, 12193,
  2049, 813, 41617, 754, 365, 30262, 82, 754, 365, 426, 293, 50616], "temperature":
  0.0, "avg_logprob": -0.1461756910596575, "compression_ratio": 1.7706093189964158,
  "no_speech_prob": 0.0058416565880179405}, {"id": 274, "seek": 135268, "start": 1357.72,
  "end": 1365.3200000000002, "text": " NVME SSD so the network is phenomenal you can
  drive you know say you can drive all of that data you", "tokens": [50616, 46512,
  15454, 30262, 370, 264, 3209, 307, 17778, 291, 393, 3332, 291, 458, 584, 291, 393,
  3332, 439, 295, 300, 1412, 291, 50996], "temperature": 0.0, "avg_logprob": -0.1461756910596575,
  "compression_ratio": 1.7706093189964158, "no_speech_prob": 0.0058416565880179405},
  {"id": 275, "seek": 135268, "start": 1365.3200000000002, "end": 1371.16, "text":
  " can drive gigabytes of data per second in a single round trip so you can get great
  throughput but", "tokens": [50996, 393, 3332, 42741, 295, 1412, 680, 1150, 294,
  257, 2167, 3098, 4931, 370, 291, 393, 483, 869, 44629, 457, 51288], "temperature":
  0.0, "avg_logprob": -0.1461756910596575, "compression_ratio": 1.7706093189964158,
  "no_speech_prob": 0.0058416565880179405}, {"id": 276, "seek": 135268, "start": 1371.16,
  "end": 1376.76, "text": " the latency is high the p90 might be around 200 milliseconds
  to s3 for every round trip someone", "tokens": [51288, 264, 27043, 307, 1090, 264,
  280, 7771, 1062, 312, 926, 2331, 34184, 281, 262, 18, 337, 633, 3098, 4931, 1580,
  51568], "temperature": 0.0, "avg_logprob": -0.1461756910596575, "compression_ratio":
  1.7706093189964158, "no_speech_prob": 0.0058416565880179405}, {"id": 277, "seek":
  135268, "start": 1376.76, "end": 1381.48, "text": " regardless of how much data
  that you transfer assuming you''re saturating the box we''ve decide almost", "tokens":
  [51568, 10060, 295, 577, 709, 1412, 300, 291, 5003, 11926, 291, 434, 21160, 990,
  264, 2424, 321, 600, 4536, 1920, 51804], "temperature": 0.0, "avg_logprob": -0.1461756910596575,
  "compression_ratio": 1.7706093189964158, "no_speech_prob": 0.0058416565880179405},
  {"id": 278, "seek": 138148, "start": 1381.48, "end": 1385.8, "text": " everything
  interval buffer around minimizing the number of round trips to 3 to 4 that doesn''t",
  "tokens": [50364, 1203, 15035, 21762, 926, 46608, 264, 1230, 295, 3098, 16051, 281,
  805, 281, 1017, 300, 1177, 380, 50580], "temperature": 0.0, "avg_logprob": -0.12679274755579825,
  "compression_ratio": 1.8224299065420562, "no_speech_prob": 0.002645058324560523},
  {"id": 279, "seek": 138148, "start": 1385.8, "end": 1390.2, "text": " just help
  for s3 it also helps for modern disk which the same thing you can drive enormous",
  "tokens": [50580, 445, 854, 337, 262, 18, 309, 611, 3665, 337, 4363, 12355, 597,
  264, 912, 551, 291, 393, 3332, 11322, 50800], "temperature": 0.0, "avg_logprob":
  -0.12679274755579825, "compression_ratio": 1.8224299065420562, "no_speech_prob":
  0.002645058324560523}, {"id": 280, "seek": 138148, "start": 1390.2, "end": 1394.6,
  "text": " amounts of bandwidth but the round trip time is is long right it''s like
  a hundreds of microseconds", "tokens": [50800, 11663, 295, 23647, 457, 264, 3098,
  4931, 565, 307, 307, 938, 558, 309, 311, 411, 257, 6779, 295, 3123, 37841, 28750,
  51020], "temperature": 0.0, "avg_logprob": -0.12679274755579825, "compression_ratio":
  1.8224299065420562, "no_speech_prob": 0.002645058324560523}, {"id": 281, "seek":
  138148, "start": 1394.6, "end": 1401.16, "text": " versus hundreds of milliseconds
  but still still substantial compared to dm so the latency tradeoff", "tokens": [51020,
  5717, 6779, 295, 34184, 457, 920, 920, 16726, 5347, 281, 274, 76, 370, 264, 27043,
  4923, 4506, 51348], "temperature": 0.0, "avg_logprob": -0.12679274755579825, "compression_ratio":
  1.8224299065420562, "no_speech_prob": 0.002645058324560523}, {"id": 282, "seek":
  138148, "start": 1401.16, "end": 1405.48, "text": " is not a fundamental tradeoff
  with this architecture by the time that it makes it into the memory", "tokens":
  [51348, 307, 406, 257, 8088, 4923, 4506, 365, 341, 9482, 538, 264, 565, 300, 309,
  1669, 309, 666, 264, 4675, 51564], "temperature": 0.0, "avg_logprob": -0.12679274755579825,
  "compression_ratio": 1.8224299065420562, "no_speech_prob": 0.002645058324560523},
  {"id": 283, "seek": 138148, "start": 1405.48, "end": 1410.68, "text": " cache it''s
  just as fast as everyone else we have found that people don''t care if it''s like
  a millisecond", "tokens": [51564, 19459, 309, 311, 445, 382, 2370, 382, 1518, 1646,
  321, 362, 1352, 300, 561, 500, 380, 1127, 498, 309, 311, 411, 257, 27940, 18882,
  51824], "temperature": 0.0, "avg_logprob": -0.12679274755579825, "compression_ratio":
  1.8224299065420562, "no_speech_prob": 0.002645058324560523}, {"id": 284, "seek":
  141068, "start": 1410.68, "end": 1416.3600000000001, "text": " or five milliseconds
  as long as it''s reliably less than around 50 milliseconds they''re good right",
  "tokens": [50364, 420, 1732, 34184, 382, 938, 382, 309, 311, 49927, 1570, 813, 926,
  2625, 34184, 436, 434, 665, 558, 50648], "temperature": 0.0, "avg_logprob": -0.09769366264343261,
  "compression_ratio": 1.7954545454545454, "no_speech_prob": 0.0017712030094116926},
  {"id": 285, "seek": 141068, "start": 1417.0, "end": 1421.96, "text": " and I think
  that a lot of the traditional storage architectures especially because of the",
  "tokens": [50680, 293, 286, 519, 300, 257, 688, 295, 264, 5164, 6725, 6331, 1303,
  2318, 570, 295, 264, 50928], "temperature": 0.0, "avg_logprob": -0.09769366264343261,
  "compression_ratio": 1.7954545454545454, "no_speech_prob": 0.0017712030094116926},
  {"id": 286, "seek": 141068, "start": 1421.96, "end": 1426.44, "text": " sharding
  structure with multiple nodes you''re already in a worse position than going to
  two systems", "tokens": [50928, 402, 515, 278, 3877, 365, 3866, 13891, 291, 434,
  1217, 294, 257, 5324, 2535, 813, 516, 281, 732, 3652, 51152], "temperature": 0.0,
  "avg_logprob": -0.09769366264343261, "compression_ratio": 1.7954545454545454, "no_speech_prob":
  0.0017712030094116926}, {"id": 287, "seek": 141068, "start": 1426.44, "end": 1431.5600000000002,
  "text": " where if you write a query on some of the traditional search engine generally
  you touch", "tokens": [51152, 689, 498, 291, 2464, 257, 14581, 322, 512, 295, 264,
  5164, 3164, 2848, 5101, 291, 2557, 51408], "temperature": 0.0, "avg_logprob": -0.09769366264343261,
  "compression_ratio": 1.7954545454545454, "no_speech_prob": 0.0017712030094116926},
  {"id": 288, "seek": 141068, "start": 1431.5600000000002, "end": 1437.64, "text":
  " five ten maybe more nodes depending on depending on this because the shard size
  is very very small", "tokens": [51408, 1732, 2064, 1310, 544, 13891, 5413, 322,
  5413, 322, 341, 570, 264, 402, 515, 2744, 307, 588, 588, 1359, 51712], "temperature":
  0.0, "avg_logprob": -0.09769366264343261, "compression_ratio": 1.7954545454545454,
  "no_speech_prob": 0.0017712030094116926}, {"id": 289, "seek": 143764, "start": 1437.64,
  "end": 1443.16, "text": " you go into more depth on that so you already have this
  problem what we see is that there''s two", "tokens": [50364, 291, 352, 666, 544,
  7161, 322, 300, 370, 291, 1217, 362, 341, 1154, 437, 321, 536, 307, 300, 456, 311,
  732, 50640], "temperature": 0.0, "avg_logprob": -0.10004511419332253, "compression_ratio":
  1.753787878787879, "no_speech_prob": 0.003484809072688222}, {"id": 290, "seek":
  143764, "start": 1443.16, "end": 1449.0800000000002, "text": " types of ways that
  people adopt it so the first one is you have an existing lexical search engine",
  "tokens": [50640, 3467, 295, 2098, 300, 561, 6878, 309, 370, 264, 700, 472, 307,
  291, 362, 364, 6741, 476, 87, 804, 3164, 2848, 50936], "temperature": 0.0, "avg_logprob":
  -0.10004511419332253, "compression_ratio": 1.753787878787879, "no_speech_prob":
  0.003484809072688222}, {"id": 291, "seek": 143764, "start": 1450.68, "end": 1455.3200000000002,
  "text": " you are having a hard time running it because of the traditional like
  very stateful", "tokens": [51016, 291, 366, 1419, 257, 1152, 565, 2614, 309, 570,
  295, 264, 5164, 411, 588, 1785, 906, 51248], "temperature": 0.0, "avg_logprob":
  -0.10004511419332253, "compression_ratio": 1.753787878787879, "no_speech_prob":
  0.003484809072688222}, {"id": 292, "seek": 143764, "start": 1455.3200000000002,
  "end": 1462.76, "text": " architecture and they''re reputed for just being difficult
  to run and you''re like already a", "tokens": [51248, 9482, 293, 436, 434, 1085,
  4866, 337, 445, 885, 2252, 281, 1190, 293, 291, 434, 411, 1217, 257, 51620], "temperature":
  0.0, "avg_logprob": -0.10004511419332253, "compression_ratio": 1.753787878787879,
  "no_speech_prob": 0.003484809072688222}, {"id": 293, "seek": 143764, "start": 1462.76,
  "end": 1467.24, "text": " little bit add your threshold for the amount of money
  that you''re spending on this cluster and", "tokens": [51620, 707, 857, 909, 428,
  14678, 337, 264, 2372, 295, 1460, 300, 291, 434, 6434, 322, 341, 13630, 293, 51844],
  "temperature": 0.0, "avg_logprob": -0.10004511419332253, "compression_ratio": 1.753787878787879,
  "no_speech_prob": 0.003484809072688222}, {"id": 294, "seek": 146724, "start": 1467.32,
  "end": 1472.1200000000001, "text": " if you put the vector data in it''s often 10
  to 20 times larger than the text data it is just", "tokens": [50368, 498, 291, 829,
  264, 8062, 1412, 294, 309, 311, 2049, 1266, 281, 945, 1413, 4833, 813, 264, 2487,
  1412, 309, 307, 445, 50608], "temperature": 0.0, "avg_logprob": -0.10057676365945191,
  "compression_ratio": 1.7806691449814127, "no_speech_prob": 0.0046919300220906734},
  {"id": 295, "seek": 146724, "start": 1473.16, "end": 1477.96, "text": " it''s a
  project that stops in its tracks similar to the read wise case that I mentioned
  before", "tokens": [50660, 309, 311, 257, 1716, 300, 10094, 294, 1080, 10218, 2531,
  281, 264, 1401, 10829, 1389, 300, 286, 2835, 949, 50900], "temperature": 0.0, "avg_logprob":
  -0.10057676365945191, "compression_ratio": 1.7806691449814127, "no_speech_prob":
  0.0046919300220906734}, {"id": 296, "seek": 146724, "start": 1477.96, "end": 1482.2,
  "text": " so for those players we often see that they have something that''s really
  well tuned for the lexical", "tokens": [50900, 370, 337, 729, 4150, 321, 2049, 536,
  300, 436, 362, 746, 300, 311, 534, 731, 10870, 337, 264, 476, 87, 804, 51112], "temperature":
  0.0, "avg_logprob": -0.10057676365945191, "compression_ratio": 1.7806691449814127,
  "no_speech_prob": 0.0046919300220906734}, {"id": 297, "seek": 146724, "start": 1482.2,
  "end": 1488.6, "text": " and they adopt a vector store and then they do two queries
  in parallel the vector store should not", "tokens": [51112, 293, 436, 6878, 257,
  8062, 3531, 293, 550, 436, 360, 732, 24109, 294, 8952, 264, 8062, 3531, 820, 406,
  51432], "temperature": 0.0, "avg_logprob": -0.10057676365945191, "compression_ratio":
  1.7806691449814127, "no_speech_prob": 0.0046919300220906734}, {"id": 298, "seek":
  146724, "start": 1488.6, "end": 1493.08, "text": " be slower than the lexical right
  so these are just two futures that you merge together in use", "tokens": [51432,
  312, 14009, 813, 264, 476, 87, 804, 558, 370, 613, 366, 445, 732, 26071, 300, 291,
  22183, 1214, 294, 764, 51656], "temperature": 0.0, "avg_logprob": -0.10057676365945191,
  "compression_ratio": 1.7806691449814127, "no_speech_prob": 0.0046919300220906734},
  {"id": 299, "seek": 149308, "start": 1493.96, "end": 1498.4399999999998, "text":
  " and in general we see that our customers are actually quite happy to move some
  of the ranking", "tokens": [50408, 293, 294, 2674, 321, 536, 300, 527, 4581, 366,
  767, 1596, 2055, 281, 1286, 512, 295, 264, 17833, 50632], "temperature": 0.0, "avg_logprob":
  -0.12755109582628524, "compression_ratio": 1.7859778597785978, "no_speech_prob":
  0.019476044923067093}, {"id": 300, "seek": 149308, "start": 1498.4399999999998,
  "end": 1505.08, "text": " and the final like second stage ranking out of the search
  engine and into a search.py instead of", "tokens": [50632, 293, 264, 2572, 411,
  1150, 3233, 17833, 484, 295, 264, 3164, 2848, 293, 666, 257, 3164, 13, 8200, 2602,
  295, 50964], "temperature": 0.0, "avg_logprob": -0.12755109582628524, "compression_ratio":
  1.7859778597785978, "no_speech_prob": 0.019476044923067093}, {"id": 301, "seek":
  149308, "start": 1505.08, "end": 1510.9199999999998, "text": " a big search.json
  which can be very difficult to maintain many of these companies express a lot",
  "tokens": [50964, 257, 955, 3164, 13, 73, 3015, 597, 393, 312, 588, 2252, 281, 6909,
  867, 295, 613, 3431, 5109, 257, 688, 51256], "temperature": 0.0, "avg_logprob":
  -0.12755109582628524, "compression_ratio": 1.7859778597785978, "no_speech_prob":
  0.019476044923067093}, {"id": 302, "seek": 149308, "start": 1510.9199999999998,
  "end": 1516.04, "text": " of desire to move more and more of their lexical work
  also onto turbo buffer and we have a full", "tokens": [51256, 295, 7516, 281, 1286,
  544, 293, 544, 295, 641, 476, 87, 804, 589, 611, 3911, 20902, 21762, 293, 321, 362,
  257, 1577, 51512], "temperature": 0.0, "avg_logprob": -0.12755109582628524, "compression_ratio":
  1.7859778597785978, "no_speech_prob": 0.019476044923067093}, {"id": 303, "seek":
  149308, "start": 1516.04, "end": 1520.9199999999998, "text": " tech search engine
  we don''t have every feature of blue scene yet but we''re working very very actively",
  "tokens": [51512, 7553, 3164, 2848, 321, 500, 380, 362, 633, 4111, 295, 3344, 4145,
  1939, 457, 321, 434, 1364, 588, 588, 13022, 51756], "temperature": 0.0, "avg_logprob":
  -0.12755109582628524, "compression_ratio": 1.7859778597785978, "no_speech_prob":
  0.019476044923067093}, {"id": 304, "seek": 152092, "start": 1521.0, "end": 1527.72,
  "text": " on bringing this up what we also see is that a lot of our customers don''t
  need all of the features", "tokens": [50368, 322, 5062, 341, 493, 437, 321, 611,
  536, 307, 300, 257, 688, 295, 527, 4581, 500, 380, 643, 439, 295, 264, 4122, 50704],
  "temperature": 0.0, "avg_logprob": -0.14197952872828434, "compression_ratio": 1.7035398230088497,
  "no_speech_prob": 0.0048061395063996315}, {"id": 305, "seek": 152092, "start": 1527.72,
  "end": 1535.8000000000002, "text": " of blue scene anymore because the vectors are
  so good that a lot of the you know Ph.D. level", "tokens": [50704, 295, 3344, 4145,
  3602, 570, 264, 18875, 366, 370, 665, 300, 257, 688, 295, 264, 291, 458, 2623, 13,
  35, 13, 1496, 51108], "temperature": 0.0, "avg_logprob": -0.14197952872828434, "compression_ratio":
  1.7035398230088497, "no_speech_prob": 0.0048061395063996315}, {"id": 306, "seek":
  152092, "start": 1535.8000000000002, "end": 1541.0800000000002, "text": " efforts
  we did before to turn strings into things is not as much of an issue anymore and
  really", "tokens": [51108, 6484, 321, 630, 949, 281, 1261, 13985, 666, 721, 307,
  406, 382, 709, 295, 364, 2734, 3602, 293, 534, 51372], "temperature": 0.0, "avg_logprob":
  -0.14197952872828434, "compression_ratio": 1.7035398230088497, "no_speech_prob":
  0.0048061395063996315}, {"id": 307, "seek": 152092, "start": 1541.0800000000002,
  "end": 1546.92, "text": " what we use strings for more is that when you search for
  DM you get the metri right like like for", "tokens": [51372, 437, 321, 764, 13985,
  337, 544, 307, 300, 562, 291, 3164, 337, 15322, 291, 483, 264, 1131, 470, 558, 411,
  411, 337, 51664], "temperature": 0.0, "avg_logprob": -0.14197952872828434, "compression_ratio":
  1.7035398230088497, "no_speech_prob": 0.0048061395063996315}, {"id": 308, "seek":
  154692, "start": 1546.92, "end": 1551.88, "text": " a prefix match whereas an embedding
  model might think that that''s a direct message those kinds", "tokens": [50364,
  257, 46969, 2995, 9735, 364, 12240, 3584, 2316, 1062, 519, 300, 300, 311, 257, 2047,
  3636, 729, 3685, 50612], "temperature": 0.0, "avg_logprob": -0.13636361568345937,
  "compression_ratio": 1.8964143426294822, "no_speech_prob": 0.013296348042786121},
  {"id": 309, "seek": 154692, "start": 1551.88, "end": 1556.52, "text": " of things
  are important and we still need string matching for that lots of applications needed",
  "tokens": [50612, 295, 721, 366, 1021, 293, 321, 920, 643, 6798, 14324, 337, 300,
  3195, 295, 5821, 2978, 50844], "temperature": 0.0, "avg_logprob": -0.13636361568345937,
  "compression_ratio": 1.8964143426294822, "no_speech_prob": 0.013296348042786121},
  {"id": 310, "seek": 154692, "start": 1557.3200000000002, "end": 1562.92, "text":
  " but there''s a lot of things that we do in leucine with synonyms with stemming
  with all these kinds", "tokens": [50884, 457, 456, 311, 257, 688, 295, 721, 300,
  321, 360, 294, 476, 1311, 533, 365, 5451, 2526, 2592, 365, 12312, 2810, 365, 439,
  613, 3685, 51164], "temperature": 0.0, "avg_logprob": -0.13636361568345937, "compression_ratio":
  1.8964143426294822, "no_speech_prob": 0.013296348042786121}, {"id": 311, "seek":
  154692, "start": 1562.92, "end": 1568.44, "text": " of things the team models are
  frankly just a lot better at so we find that this is an adoption", "tokens": [51164,
  295, 721, 264, 1469, 5245, 366, 11939, 445, 257, 688, 1101, 412, 370, 321, 915,
  300, 341, 307, 364, 19215, 51440], "temperature": 0.0, "avg_logprob": -0.13636361568345937,
  "compression_ratio": 1.8964143426294822, "no_speech_prob": 0.013296348042786121},
  {"id": 312, "seek": 154692, "start": 1568.44, "end": 1572.76, "text": " curve that
  is there a lot of the newer companies just start with embedding models and simple",
  "tokens": [51440, 7605, 300, 307, 456, 257, 688, 295, 264, 17628, 3431, 445, 722,
  365, 12240, 3584, 5245, 293, 2199, 51656], "temperature": 0.0, "avg_logprob": -0.13636361568345937,
  "compression_ratio": 1.8964143426294822, "no_speech_prob": 0.013296348042786121},
  {"id": 313, "seek": 157276, "start": 1572.76, "end": 1577.08, "text": " full-text
  search and and they get it up and running on turbo puffer and they like that they
  just", "tokens": [50364, 1577, 12, 25111, 3164, 293, 293, 436, 483, 309, 493, 293,
  2614, 322, 20902, 19613, 260, 293, 436, 411, 300, 436, 445, 50580], "temperature":
  0.0, "avg_logprob": -0.15564343107848608, "compression_ratio": 1.8953488372093024,
  "no_speech_prob": 0.02435794100165367}, {"id": 314, "seek": 157276, "start": 1577.08,
  "end": 1581.48, "text": " pay for what they need they don''t think about it and
  they could pump a petabyte of data and if", "tokens": [50580, 1689, 337, 437, 436,
  643, 436, 500, 380, 519, 466, 309, 293, 436, 727, 5889, 257, 3817, 34529, 295, 1412,
  293, 498, 50800], "temperature": 0.0, "avg_logprob": -0.15564343107848608, "compression_ratio":
  1.8953488372093024, "no_speech_prob": 0.02435794100165367}, {"id": 315, "seek":
  157276, "start": 1581.48, "end": 1586.2, "text": " they want it and it would be
  extremely competitive on pricing and they don''t have to think about it", "tokens":
  [50800, 436, 528, 309, 293, 309, 576, 312, 4664, 10043, 322, 17621, 293, 436, 500,
  380, 362, 281, 519, 466, 309, 51036], "temperature": 0.0, "avg_logprob": -0.15564343107848608,
  "compression_ratio": 1.8953488372093024, "no_speech_prob": 0.02435794100165367},
  {"id": 316, "seek": 157276, "start": 1586.2, "end": 1591.32, "text": " oh that''s
  awesome that''s awesome actually I forgot to mention I forgot to ask you which language",
  "tokens": [51036, 1954, 300, 311, 3476, 300, 311, 3476, 767, 286, 5298, 281, 2152,
  286, 5298, 281, 1029, 291, 597, 2856, 51292], "temperature": 0.0, "avg_logprob":
  -0.15564343107848608, "compression_ratio": 1.8953488372093024, "no_speech_prob":
  0.02435794100165367}, {"id": 317, "seek": 157276, "start": 1591.32, "end": 1599.72,
  "text": " did you choose to implement to revolver on yeah we we um well it was just
  me at the time but I chose", "tokens": [51292, 630, 291, 2826, 281, 4445, 281, 16908,
  331, 322, 1338, 321, 321, 1105, 731, 309, 390, 445, 385, 412, 264, 565, 457, 286,
  5111, 51712], "temperature": 0.0, "avg_logprob": -0.15564343107848608, "compression_ratio":
  1.8953488372093024, "no_speech_prob": 0.02435794100165367}, {"id": 318, "seek":
  159972, "start": 1599.8, "end": 1607.08, "text": " I chose Rust and I think I spent
  the majority of my career writing Ruby at Shopify and", "tokens": [50368, 286, 5111,
  34952, 293, 286, 519, 286, 4418, 264, 6286, 295, 452, 3988, 3579, 19907, 412, 43991,
  293, 50732], "temperature": 0.0, "avg_logprob": -0.1917729320296322, "compression_ratio":
  1.655813953488372, "no_speech_prob": 0.0014194503892213106}, {"id": 319, "seek":
  159972, "start": 1608.1200000000001, "end": 1613.8, "text": " and then a lot of
  go as well for some of the infrastructure components and then mainly debugging",
  "tokens": [50784, 293, 550, 257, 688, 295, 352, 382, 731, 337, 512, 295, 264, 6896,
  6677, 293, 550, 8704, 45592, 51068], "temperature": 0.0, "avg_logprob": -0.1917729320296322,
  "compression_ratio": 1.655813953488372, "no_speech_prob": 0.0014194503892213106},
  {"id": 320, "seek": 159972, "start": 1613.8, "end": 1618.6000000000001, "text":
  " C which all the databases that we were using were we''re doing and reading C",
  "tokens": [51068, 383, 597, 439, 264, 22380, 300, 321, 645, 1228, 645, 321, 434,
  884, 293, 3760, 383, 51308], "temperature": 0.0, "avg_logprob": -0.1917729320296322,
  "compression_ratio": 1.655813953488372, "no_speech_prob": 0.0014194503892213106},
  {"id": 321, "seek": 159972, "start": 1620.2, "end": 1628.04, "text": " I I really
  like go and I like go alongside Ruby at Shopify because go was one of those things
  as", "tokens": [51388, 286, 286, 534, 411, 352, 293, 286, 411, 352, 12385, 19907,
  412, 43991, 570, 352, 390, 472, 295, 729, 721, 382, 51780], "temperature": 0.0,
  "avg_logprob": -0.1917729320296322, "compression_ratio": 1.655813953488372, "no_speech_prob":
  0.0014194503892213106}, {"id": 322, "seek": 162804, "start": 1628.6, "end": 1632.92,
  "text": " when leading teams I didn''t have to worry about whether someone knew
  go or not because the adoption", "tokens": [50392, 562, 5775, 5491, 286, 994, 380,
  362, 281, 3292, 466, 1968, 1580, 2586, 352, 420, 406, 570, 264, 19215, 50608], "temperature":
  0.0, "avg_logprob": -0.10201243240467824, "compression_ratio": 2.0034364261168385,
  "no_speech_prob": 0.0026609969791024923}, {"id": 323, "seek": 162804, "start": 1632.92,
  "end": 1639.8, "text": " to learn it is two weeks um the adoption to learn Rust
  and being proficient in it is months right", "tokens": [50608, 281, 1466, 309, 307,
  732, 3259, 1105, 264, 19215, 281, 1466, 34952, 293, 885, 1740, 24549, 294, 309,
  307, 2493, 558, 50952], "temperature": 0.0, "avg_logprob": -0.10201243240467824,
  "compression_ratio": 2.0034364261168385, "no_speech_prob": 0.0026609969791024923},
  {"id": 324, "seek": 162804, "start": 1639.8, "end": 1643.56, "text": " and somehow
  that''s written Rust for two years it''s a lot more productive than someone who''s",
  "tokens": [50952, 293, 6063, 300, 311, 3720, 34952, 337, 732, 924, 309, 311, 257,
  688, 544, 13304, 813, 1580, 567, 311, 51140], "temperature": 0.0, "avg_logprob":
  -0.10201243240467824, "compression_ratio": 2.0034364261168385, "no_speech_prob":
  0.0026609969791024923}, {"id": 325, "seek": 162804, "start": 1643.56, "end": 1648.28,
  "text": " written it for two months in the language um and that''s just not the
  case for go like someone who''s", "tokens": [51140, 3720, 309, 337, 732, 2493, 294,
  264, 2856, 1105, 293, 300, 311, 445, 406, 264, 1389, 337, 352, 411, 1580, 567, 311,
  51376], "temperature": 0.0, "avg_logprob": -0.10201243240467824, "compression_ratio":
  2.0034364261168385, "no_speech_prob": 0.0026609969791024923}, {"id": 326, "seek":
  162804, "start": 1648.28, "end": 1651.72, "text": " spent two years in it is just
  not that much more productive and so and I think that''s an amazing", "tokens":
  [51376, 4418, 732, 924, 294, 309, 307, 445, 406, 300, 709, 544, 13304, 293, 370,
  293, 286, 519, 300, 311, 364, 2243, 51548], "temperature": 0.0, "avg_logprob": -0.10201243240467824,
  "compression_ratio": 2.0034364261168385, "no_speech_prob": 0.0026609969791024923},
  {"id": 327, "seek": 162804, "start": 1651.72, "end": 1656.92, "text": " feature
  of the language but from from my own point of view and from the napkin web math
  point of", "tokens": [51548, 4111, 295, 264, 2856, 457, 490, 490, 452, 1065, 935,
  295, 1910, 293, 490, 264, 9296, 5843, 3670, 5221, 935, 295, 51808], "temperature":
  0.0, "avg_logprob": -0.10201243240467824, "compression_ratio": 2.0034364261168385,
  "no_speech_prob": 0.0026609969791024923}, {"id": 328, "seek": 165692, "start": 1657.16,
  "end": 1663.24, "text": " you I just I was always so hungry having been in time
  inside of runtimes in the Ruby MRI runtime", "tokens": [50376, 291, 286, 445, 286,
  390, 1009, 370, 8067, 1419, 668, 294, 565, 1854, 295, 49435, 1532, 294, 264, 19907,
  32812, 34474, 50680], "temperature": 0.0, "avg_logprob": -0.12749700457136207, "compression_ratio":
  1.8795180722891567, "no_speech_prob": 0.0036210031248629093}, {"id": 329, "seek":
  165692, "start": 1663.24, "end": 1668.04, "text": " and then inside of the go runtime
  I was just hungry to just get directly connected to", "tokens": [50680, 293, 550,
  1854, 295, 264, 352, 34474, 286, 390, 445, 8067, 281, 445, 483, 3838, 4582, 281,
  50920], "temperature": 0.0, "avg_logprob": -0.12749700457136207, "compression_ratio":
  1.8795180722891567, "no_speech_prob": 0.0036210031248629093}, {"id": 330, "seek":
  165692, "start": 1669.0, "end": 1673.8000000000002, "text": " the metal of the machine
  and so and for a database in particular that was very important right", "tokens":
  [50968, 264, 5760, 295, 264, 3479, 293, 370, 293, 337, 257, 8149, 294, 1729, 300,
  390, 588, 1021, 558, 51208], "temperature": 0.0, "avg_logprob": -0.12749700457136207,
  "compression_ratio": 1.8795180722891567, "no_speech_prob": 0.0036210031248629093},
  {"id": 331, "seek": 165692, "start": 1673.8000000000002, "end": 1679.16, "text":
  " we need to vectorize everything we need full control over that and I think that
  I think that", "tokens": [51208, 321, 643, 281, 8062, 1125, 1203, 321, 643, 1577,
  1969, 670, 300, 293, 286, 519, 300, 286, 519, 300, 51476], "temperature": 0.0, "avg_logprob":
  -0.12749700457136207, "compression_ratio": 1.8795180722891567, "no_speech_prob":
  0.0036210031248629093}, {"id": 332, "seek": 165692, "start": 1679.16, "end": 1684.44,
  "text": " that full control as remarkable now as Go is which would I think it would
  be would have been okay", "tokens": [51476, 300, 1577, 1969, 382, 12802, 586, 382,
  1037, 307, 597, 576, 286, 519, 309, 576, 312, 576, 362, 668, 1392, 51740], "temperature":
  0.0, "avg_logprob": -0.12749700457136207, "compression_ratio": 1.8795180722891567,
  "no_speech_prob": 0.0036210031248629093}, {"id": 333, "seek": 168444, "start": 1685.4,
  "end": 1691.24, "text": " that raw access to the machine has been has is needed
  for for writing something like TurboPover.", "tokens": [50412, 300, 8936, 2105,
  281, 264, 3479, 575, 668, 575, 307, 2978, 337, 337, 3579, 746, 411, 35848, 47, 3570,
  13, 50704], "temperature": 0.0, "avg_logprob": -0.22287628449589372, "compression_ratio":
  1.6018099547511313, "no_speech_prob": 0.006159712094813585}, {"id": 334, "seek":
  168444, "start": 1691.24, "end": 1697.24, "text": " Yeah for sure I still remember
  coding the times when I was learning and coded", "tokens": [50704, 865, 337, 988,
  286, 920, 1604, 17720, 264, 1413, 562, 286, 390, 2539, 293, 34874, 51004], "temperature":
  0.0, "avg_logprob": -0.22287628449589372, "compression_ratio": 1.6018099547511313,
  "no_speech_prob": 0.006159712094813585}, {"id": 335, "seek": 168444, "start": 1697.96,
  "end": 1704.52, "text": " industrially in CNC++ like you like you really need it
  to be very very careful but in return", "tokens": [51040, 49005, 379, 294, 48714,
  25472, 411, 291, 411, 291, 534, 643, 309, 281, 312, 588, 588, 5026, 457, 294, 2736,
  51368], "temperature": 0.0, "avg_logprob": -0.22287628449589372, "compression_ratio":
  1.6018099547511313, "no_speech_prob": 0.006159712094813585}, {"id": 336, "seek":
  168444, "start": 1704.52, "end": 1709.8, "text": " you can get a lot of like performance
  gains you know and some of your ideas really fly", "tokens": [51368, 291, 393, 483,
  257, 688, 295, 411, 3389, 16823, 291, 458, 293, 512, 295, 428, 3487, 534, 3603,
  51632], "temperature": 0.0, "avg_logprob": -0.22287628449589372, "compression_ratio":
  1.6018099547511313, "no_speech_prob": 0.006159712094813585}, {"id": 337, "seek":
  170980, "start": 1710.68, "end": 1715.8799999999999, "text": " but yeah today I
  guess I''m coding more in Python or should I even say that I called in Python when
  I", "tokens": [50408, 457, 1338, 965, 286, 2041, 286, 478, 17720, 544, 294, 15329,
  420, 820, 286, 754, 584, 300, 286, 1219, 294, 15329, 562, 286, 50668], "temperature":
  0.0, "avg_logprob": -0.11883871606055726, "compression_ratio": 1.7017543859649122,
  "no_speech_prob": 0.013183152303099632}, {"id": 338, "seek": 170980, "start": 1715.8799999999999,
  "end": 1724.36, "text": " use cursor more and more which is by the way scary you
  know the the that feeling when some some", "tokens": [50668, 764, 28169, 544, 293,
  544, 597, 307, 538, 264, 636, 6958, 291, 458, 264, 264, 300, 2633, 562, 512, 512,
  51092], "temperature": 0.0, "avg_logprob": -0.11883871606055726, "compression_ratio":
  1.7017543859649122, "no_speech_prob": 0.013183152303099632}, {"id": 339, "seek":
  170980, "start": 1724.36, "end": 1729.3999999999999, "text": " other entity writes
  code and you are just reading it right it''s it''s a little bit scary and I''m",
  "tokens": [51092, 661, 13977, 13657, 3089, 293, 291, 366, 445, 3760, 309, 558, 309,
  311, 309, 311, 257, 707, 857, 6958, 293, 286, 478, 51344], "temperature": 0.0, "avg_logprob":
  -0.11883871606055726, "compression_ratio": 1.7017543859649122, "no_speech_prob":
  0.013183152303099632}, {"id": 340, "seek": 170980, "start": 1729.3999999999999,
  "end": 1736.44, "text": " still grappling with it but the amount of productivity
  that I get is enormous and it''s like you", "tokens": [51344, 920, 50086, 365, 309,
  457, 264, 2372, 295, 15604, 300, 286, 483, 307, 11322, 293, 309, 311, 411, 291,
  51696], "temperature": 0.0, "avg_logprob": -0.11883871606055726, "compression_ratio":
  1.7017543859649122, "no_speech_prob": 0.013183152303099632}, {"id": 341, "seek":
  173644, "start": 1736.52, "end": 1741.24, "text": " know I can shoot daily like
  features and just see them being used that''s amazing.", "tokens": [50368, 458,
  286, 393, 3076, 5212, 411, 4122, 293, 445, 536, 552, 885, 1143, 300, 311, 2243,
  13, 50604], "temperature": 0.0, "avg_logprob": -0.16198551982914636, "compression_ratio":
  1.6525096525096525, "no_speech_prob": 0.0007687908946536481}, {"id": 342, "seek":
  173644, "start": 1742.44, "end": 1748.92, "text": " I think what I love about it
  is that I still love to sit there and write the", "tokens": [50664, 286, 519, 437,
  286, 959, 466, 309, 307, 300, 286, 920, 959, 281, 1394, 456, 293, 2464, 264, 50988],
  "temperature": 0.0, "avg_logprob": -0.16198551982914636, "compression_ratio": 1.6525096525096525,
  "no_speech_prob": 0.0007687908946536481}, {"id": 343, "seek": 173644, "start": 1748.92,
  "end": 1755.4, "text": " additional code by hand you know maybe at some point we
  will we will we will mark TurboPover as", "tokens": [50988, 4497, 3089, 538, 1011,
  291, 458, 1310, 412, 512, 935, 321, 486, 321, 486, 321, 486, 1491, 35848, 47, 3570,
  382, 51312], "temperature": 0.0, "avg_logprob": -0.16198551982914636, "compression_ratio":
  1.6525096525096525, "no_speech_prob": 0.0007687908946536481}, {"id": 344, "seek":
  173644, "start": 1755.4, "end": 1760.6000000000001, "text": " an a seasonally written
  database because we don''t use a ton of AI for the very key parts", "tokens": [51312,
  364, 257, 3196, 379, 3720, 8149, 570, 321, 500, 380, 764, 257, 2952, 295, 7318,
  337, 264, 588, 2141, 3166, 51572], "temperature": 0.0, "avg_logprob": -0.16198551982914636,
  "compression_ratio": 1.6525096525096525, "no_speech_prob": 0.0007687908946536481},
  {"id": 345, "seek": 173644, "start": 1761.24, "end": 1766.28, "text": " because
  I mean we''re at the edge of what the LLMs could know but I think that for me",
  "tokens": [51604, 570, 286, 914, 321, 434, 412, 264, 4691, 295, 437, 264, 441, 43,
  26386, 727, 458, 457, 286, 519, 300, 337, 385, 51856], "temperature": 0.0, "avg_logprob":
  -0.16198551982914636, "compression_ratio": 1.6525096525096525, "no_speech_prob":
  0.0007687908946536481}, {"id": 346, "seek": 176644, "start": 1766.44, "end": 1771.24,
  "text": " in a position where I''m in and out of meetings all day these days but
  I can actually get a lot", "tokens": [50364, 294, 257, 2535, 689, 286, 478, 294,
  293, 484, 295, 8410, 439, 786, 613, 1708, 457, 286, 393, 767, 483, 257, 688, 50604],
  "temperature": 0.0, "avg_logprob": -0.12191998617989676, "compression_ratio": 1.865814696485623,
  "no_speech_prob": 0.006656951736658812}, {"id": 347, "seek": 176644, "start": 1771.24,
  "end": 1775.64, "text": " done in a 30 minute window when I have something that''s
  prompting and writing the tests right and", "tokens": [50604, 1096, 294, 257, 2217,
  3456, 4910, 562, 286, 362, 746, 300, 311, 12391, 278, 293, 3579, 264, 6921, 558,
  293, 50824], "temperature": 0.0, "avg_logprob": -0.12191998617989676, "compression_ratio":
  1.865814696485623, "no_speech_prob": 0.006656951736658812}, {"id": 348, "seek":
  176644, "start": 1775.64, "end": 1779.64, "text": " you follow it off at the beginning
  of the meeting you check in and they''re like you know 15 30 minutes", "tokens":
  [50824, 291, 1524, 309, 766, 412, 264, 2863, 295, 264, 3440, 291, 1520, 294, 293,
  436, 434, 411, 291, 458, 2119, 2217, 2077, 51024], "temperature": 0.0, "avg_logprob":
  -0.12191998617989676, "compression_ratio": 1.865814696485623, "no_speech_prob":
  0.006656951736658812}, {"id": 349, "seek": 176644, "start": 1779.64, "end": 1785.24,
  "text": " you have in between blocks and this allows me to actually contribute a
  lot more code than I was", "tokens": [51024, 291, 362, 294, 1296, 8474, 293, 341,
  4045, 385, 281, 767, 10586, 257, 688, 544, 3089, 813, 286, 390, 51304], "temperature":
  0.0, "avg_logprob": -0.12191998617989676, "compression_ratio": 1.865814696485623,
  "no_speech_prob": 0.006656951736658812}, {"id": 350, "seek": 176644, "start": 1785.24,
  "end": 1790.92, "text": " otherwise going to be able to not into the core engine
  you know I don''t get led led into led into", "tokens": [51304, 5911, 516, 281,
  312, 1075, 281, 406, 666, 264, 4965, 2848, 291, 458, 286, 500, 380, 483, 4684, 4684,
  666, 4684, 666, 51588], "temperature": 0.0, "avg_logprob": -0.12191998617989676,
  "compression_ratio": 1.865814696485623, "no_speech_prob": 0.006656951736658812},
  {"id": 351, "seek": 176644, "start": 1790.92, "end": 1795.3200000000002, "text":
  " a lot of that anymore because I don''t have the the time and focus that it takes
  to fully think", "tokens": [51588, 257, 688, 295, 300, 3602, 570, 286, 500, 380,
  362, 264, 264, 565, 293, 1879, 300, 309, 2516, 281, 4498, 519, 51808], "temperature":
  0.0, "avg_logprob": -0.12191998617989676, "compression_ratio": 1.865814696485623,
  "no_speech_prob": 0.006656951736658812}, {"id": 352, "seek": 179532, "start": 1795.32,
  "end": 1800.12, "text": " something through there but for the website the API to
  initial features all of that it''s just", "tokens": [50364, 746, 807, 456, 457,
  337, 264, 3144, 264, 9362, 281, 5883, 4122, 439, 295, 300, 309, 311, 445, 50604],
  "temperature": 0.0, "avg_logprob": -0.11372512994810592, "compression_ratio": 1.602510460251046,
  "no_speech_prob": 0.0034170181024819613}, {"id": 353, "seek": 179532, "start": 1800.12,
  "end": 1808.04, "text": " been wonderful yeah that''s amazing I also wanted to go
  a bit on the tangent like you essentially", "tokens": [50604, 668, 3715, 1338, 300,
  311, 2243, 286, 611, 1415, 281, 352, 257, 857, 322, 264, 27747, 411, 291, 4476,
  51000], "temperature": 0.0, "avg_logprob": -0.11372512994810592, "compression_ratio":
  1.602510460251046, "no_speech_prob": 0.0034170181024819613}, {"id": 354, "seek":
  179532, "start": 1808.04, "end": 1815.72, "text": " you''ve been you could say mathematician
  engineer but you took a leap towards becoming a CEO right", "tokens": [51000, 291,
  600, 668, 291, 727, 584, 48281, 11403, 457, 291, 1890, 257, 19438, 3030, 5617, 257,
  9282, 558, 51384], "temperature": 0.0, "avg_logprob": -0.11372512994810592, "compression_ratio":
  1.602510460251046, "no_speech_prob": 0.0034170181024819613}, {"id": 355, "seek":
  179532, "start": 1815.72, "end": 1823.0, "text": " and I think you know as you said
  you go to meetings you do lots of you know probably sales and", "tokens": [51384,
  293, 286, 519, 291, 458, 382, 291, 848, 291, 352, 281, 8410, 291, 360, 3195, 295,
  291, 458, 1391, 5763, 293, 51748], "temperature": 0.0, "avg_logprob": -0.11372512994810592,
  "compression_ratio": 1.602510460251046, "no_speech_prob": 0.0034170181024819613},
  {"id": 356, "seek": 182300, "start": 1823.0, "end": 1829.72, "text": " and and and
  product and all of that stuff was it a natural transition for you like what what
  have", "tokens": [50364, 293, 293, 293, 1674, 293, 439, 295, 300, 1507, 390, 309,
  257, 3303, 6034, 337, 291, 411, 437, 437, 362, 50700], "temperature": 0.0, "avg_logprob":
  -0.13952407836914063, "compression_ratio": 1.8309859154929577, "no_speech_prob":
  0.0015195596497505903}, {"id": 357, "seek": 182300, "start": 1829.72, "end": 1837.08,
  "text": " you learned in this in this journey and what what maybe do you miss from
  from your previous career", "tokens": [50700, 291, 3264, 294, 341, 294, 341, 4671,
  293, 437, 437, 1310, 360, 291, 1713, 490, 490, 428, 3894, 3988, 51068], "temperature":
  0.0, "avg_logprob": -0.13952407836914063, "compression_ratio": 1.8309859154929577,
  "no_speech_prob": 0.0015195596497505903}, {"id": 358, "seek": 182300, "start": 1837.08,
  "end": 1843.96, "text": " when you when you were like you know hands on and sit
  down and write a bunch of code I think I", "tokens": [51068, 562, 291, 562, 291,
  645, 411, 291, 458, 2377, 322, 293, 1394, 760, 293, 2464, 257, 3840, 295, 3089,
  286, 519, 286, 51412], "temperature": 0.0, "avg_logprob": -0.13952407836914063,
  "compression_ratio": 1.8309859154929577, "no_speech_prob": 0.0015195596497505903},
  {"id": 359, "seek": 182300, "start": 1843.96, "end": 1848.68, "text": " have a I
  have a couple of angles to answer the question not necessarily a directing answer
  I think", "tokens": [51412, 362, 257, 286, 362, 257, 1916, 295, 14708, 281, 1867,
  264, 1168, 406, 4725, 257, 26979, 1867, 286, 519, 51648], "temperature": 0.0, "avg_logprob":
  -0.13952407836914063, "compression_ratio": 1.8309859154929577, "no_speech_prob":
  0.0015195596497505903}, {"id": 360, "seek": 184868, "start": 1848.76, "end": 1857.3200000000002,
  "text": " one one angle is that fundamentally I''m like a growth junkie for better
  or worse and I think that", "tokens": [50368, 472, 472, 5802, 307, 300, 17879, 286,
  478, 411, 257, 4599, 19109, 414, 337, 1101, 420, 5324, 293, 286, 519, 300, 50796],
  "temperature": 0.0, "avg_logprob": -0.08798768104763206, "compression_ratio": 1.8953488372093024,
  "no_speech_prob": 0.00229034130461514}, {"id": 361, "seek": 184868, "start": 1857.3200000000002,
  "end": 1862.8400000000001, "text": " entrepreneurship is the ultimate path for a
  growth junkie it was never really something that I", "tokens": [50796, 26582, 307,
  264, 9705, 3100, 337, 257, 4599, 19109, 414, 309, 390, 1128, 534, 746, 300, 286,
  51072], "temperature": 0.0, "avg_logprob": -0.08798768104763206, "compression_ratio":
  1.8953488372093024, "no_speech_prob": 0.00229034130461514}, {"id": 362, "seek":
  184868, "start": 1862.8400000000001, "end": 1867.96, "text": " assumed that I was
  going to do I''ve never before even when I was working on the project it''s never",
  "tokens": [51072, 15895, 300, 286, 390, 516, 281, 360, 286, 600, 1128, 949, 754,
  562, 286, 390, 1364, 322, 264, 1716, 309, 311, 1128, 51328], "temperature": 0.0,
  "avg_logprob": -0.08798768104763206, "compression_ratio": 1.8953488372093024, "no_speech_prob":
  0.00229034130461514}, {"id": 363, "seek": 184868, "start": 1867.96, "end": 1872.3600000000001,
  "text": " about becoming a founder it''s just about creating the database right
  and at some point becoming the", "tokens": [51328, 466, 5617, 257, 14917, 309, 311,
  445, 466, 4084, 264, 8149, 558, 293, 412, 512, 935, 5617, 264, 51548], "temperature":
  0.0, "avg_logprob": -0.08798768104763206, "compression_ratio": 1.8953488372093024,
  "no_speech_prob": 0.00229034130461514}, {"id": 364, "seek": 184868, "start": 1872.3600000000001,
  "end": 1876.68, "text": " founder of the company becomes a means to an end of creating
  the database and getting it into the", "tokens": [51548, 14917, 295, 264, 2237,
  3643, 257, 1355, 281, 364, 917, 295, 4084, 264, 8149, 293, 1242, 309, 666, 264,
  51764], "temperature": 0.0, "avg_logprob": -0.08798768104763206, "compression_ratio":
  1.8953488372093024, "no_speech_prob": 0.00229034130461514}, {"id": 365, "seek":
  187668, "start": 1876.76, "end": 1882.8400000000001, "text": " hands of our users
  and making sure they have a great time that''s always what like that''s what", "tokens":
  [50368, 2377, 295, 527, 5022, 293, 1455, 988, 436, 362, 257, 869, 565, 300, 311,
  1009, 437, 411, 300, 311, 437, 50672], "temperature": 0.0, "avg_logprob": -0.09643647545262386,
  "compression_ratio": 1.90234375, "no_speech_prob": 0.0005882293917238712}, {"id":
  366, "seek": 187668, "start": 1882.8400000000001, "end": 1887.8, "text": " drove
  me right was the read why I should have this right our customers should have this
  this you", "tokens": [50672, 13226, 385, 558, 390, 264, 1401, 983, 286, 820, 362,
  341, 558, 527, 4581, 820, 362, 341, 341, 291, 50920], "temperature": 0.0, "avg_logprob":
  -0.09643647545262386, "compression_ratio": 1.90234375, "no_speech_prob": 0.0005882293917238712},
  {"id": 367, "seek": 187668, "start": 1887.8, "end": 1893.5600000000002, "text":
  " have a great experience and that''s always what''s driven me and to me the the
  founder and all of the", "tokens": [50920, 362, 257, 869, 1752, 293, 300, 311, 1009,
  437, 311, 9555, 385, 293, 281, 385, 264, 264, 14917, 293, 439, 295, 264, 51208],
  "temperature": 0.0, "avg_logprob": -0.09643647545262386, "compression_ratio": 1.90234375,
  "no_speech_prob": 0.0005882293917238712}, {"id": 368, "seek": 187668, "start": 1893.5600000000002,
  "end": 1899.0800000000002, "text": " other things have been a mean towards an end
  there I think that one of the things that is maybe both", "tokens": [51208, 661,
  721, 362, 668, 257, 914, 3030, 364, 917, 456, 286, 519, 300, 472, 295, 264, 721,
  300, 307, 1310, 1293, 51484], "temperature": 0.0, "avg_logprob": -0.09643647545262386,
  "compression_ratio": 1.90234375, "no_speech_prob": 0.0005882293917238712}, {"id":
  369, "seek": 187668, "start": 1899.0800000000002, "end": 1903.64, "text": " a controversial
  but also feels like a true statement is that at some point I feel a bit numb to",
  "tokens": [51484, 257, 17323, 457, 611, 3417, 411, 257, 2074, 5629, 307, 300, 412,
  512, 935, 286, 841, 257, 857, 32200, 281, 51712], "temperature": 0.0, "avg_logprob":
  -0.09643647545262386, "compression_ratio": 1.90234375, "no_speech_prob": 0.0005882293917238712},
  {"id": 370, "seek": 190364, "start": 1903.64, "end": 1909.16, "text": " what work
  that I enjoy and what I don''t enjoy anymore because what I enjoy the most is making",
  "tokens": [50364, 437, 589, 300, 286, 2103, 293, 437, 286, 500, 380, 2103, 3602,
  570, 437, 286, 2103, 264, 881, 307, 1455, 50640], "temperature": 0.0, "avg_logprob":
  -0.07741976213884784, "compression_ratio": 1.8779527559055118, "no_speech_prob":
  0.005077640060335398}, {"id": 371, "seek": 190364, "start": 1909.16, "end": 1914.3600000000001,
  "text": " this company successful and making the database successful for our customers
  that''s what I care", "tokens": [50640, 341, 2237, 4406, 293, 1455, 264, 8149, 4406,
  337, 527, 4581, 300, 311, 437, 286, 1127, 50900], "temperature": 0.0, "avg_logprob":
  -0.07741976213884784, "compression_ratio": 1.8779527559055118, "no_speech_prob":
  0.005077640060335398}, {"id": 372, "seek": 190364, "start": 1914.3600000000001,
  "end": 1922.1200000000001, "text": " the most about and I''m yeah I honestly I love
  sales I love marketing I love the engineering I love", "tokens": [50900, 264, 881,
  466, 293, 286, 478, 1338, 286, 6095, 286, 959, 5763, 286, 959, 6370, 286, 959, 264,
  7043, 286, 959, 51288], "temperature": 0.0, "avg_logprob": -0.07741976213884784,
  "compression_ratio": 1.8779527559055118, "no_speech_prob": 0.005077640060335398},
  {"id": 373, "seek": 190364, "start": 1922.1200000000001, "end": 1928.2800000000002,
  "text": " hiring people for the team I love all of these things but it''s not a
  simplistic answer to oh I''ve", "tokens": [51288, 15335, 561, 337, 264, 1469, 286,
  959, 439, 295, 613, 721, 457, 309, 311, 406, 257, 44199, 1867, 281, 1954, 286, 600,
  51596], "temperature": 0.0, "avg_logprob": -0.07741976213884784, "compression_ratio":
  1.8779527559055118, "no_speech_prob": 0.005077640060335398}, {"id": 374, "seek":
  190364, "start": 1928.2800000000002, "end": 1933.0800000000002, "text": " been coding
  my whole life I think it''s more that that is my idle activity if there is that",
  "tokens": [51596, 668, 17720, 452, 1379, 993, 286, 519, 309, 311, 544, 300, 300,
  307, 452, 30650, 5191, 498, 456, 307, 300, 51836], "temperature": 0.0, "avg_logprob":
  -0.07741976213884784, "compression_ratio": 1.8779527559055118, "no_speech_prob":
  0.005077640060335398}, {"id": 375, "seek": 193308, "start": 1933.08, "end": 1937.48,
  "text": " one to two hour and there''s nothing urgent on then I''m going to go spend
  some time in the code", "tokens": [50364, 472, 281, 732, 1773, 293, 456, 311, 1825,
  19022, 322, 550, 286, 478, 516, 281, 352, 3496, 512, 565, 294, 264, 3089, 50584],
  "temperature": 0.0, "avg_logprob": -0.15626467952021847, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.0075340173207223415}, {"id": 376, "seek": 193308, "start": 1937.48,
  "end": 1942.76, "text": " it''s like oh how did how did Nathan implement this new
  this new query planning of query plan", "tokens": [50584, 309, 311, 411, 1954, 577,
  630, 577, 630, 20634, 4445, 341, 777, 341, 777, 14581, 5038, 295, 14581, 1393, 50848],
  "temperature": 0.0, "avg_logprob": -0.15626467952021847, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.0075340173207223415}, {"id": 377, "seek": 193308, "start": 1942.76,
  "end": 1948.28, "text": " or heuristic that is a natural that''s where my idle activity
  and I always like to also an", "tokens": [50848, 420, 415, 374, 3142, 300, 307,
  257, 3303, 300, 311, 689, 452, 30650, 5191, 293, 286, 1009, 411, 281, 611, 364,
  51124], "temperature": 0.0, "avg_logprob": -0.15626467952021847, "compression_ratio":
  1.9078947368421053, "no_speech_prob": 0.0075340173207223415}, {"id": 378, "seek":
  193308, "start": 1948.28, "end": 1952.28, "text": " interviewing people try to understand
  especially if they''re in a more hybrid world what''s your idle", "tokens": [51124,
  26524, 561, 853, 281, 1223, 2318, 498, 436, 434, 294, 257, 544, 13051, 1002, 437,
  311, 428, 30650, 51324], "temperature": 0.0, "avg_logprob": -0.15626467952021847,
  "compression_ratio": 1.9078947368421053, "no_speech_prob": 0.0075340173207223415},
  {"id": 379, "seek": 193308, "start": 1952.28, "end": 1956.52, "text": " activity
  what''s the thing did you do when you have one to two hours and nothing else comes
  up do you", "tokens": [51324, 5191, 437, 311, 264, 551, 630, 291, 360, 562, 291,
  362, 472, 281, 732, 2496, 293, 1825, 1646, 1487, 493, 360, 291, 51536], "temperature":
  0.0, "avg_logprob": -0.15626467952021847, "compression_ratio": 1.9078947368421053,
  "no_speech_prob": 0.0075340173207223415}, {"id": 380, "seek": 193308, "start": 1956.52,
  "end": 1961.8799999999999, "text": " gravitate towards the code do you start looking
  at just start writing an article do you start playing", "tokens": [51536, 7427,
  8086, 3030, 264, 3089, 360, 291, 722, 1237, 412, 445, 722, 3579, 364, 7222, 360,
  291, 722, 2433, 51804], "temperature": 0.0, "avg_logprob": -0.15626467952021847,
  "compression_ratio": 1.9078947368421053, "no_speech_prob": 0.0075340173207223415},
  {"id": 381, "seek": 196188, "start": 1961.88, "end": 1966.2800000000002, "text":
  " with the product what is that idle activity and it is code for me that''s what
  everything is grounded", "tokens": [50364, 365, 264, 1674, 437, 307, 300, 30650,
  5191, 293, 309, 307, 3089, 337, 385, 300, 311, 437, 1203, 307, 23535, 50584], "temperature":
  0.0, "avg_logprob": -0.11034653981526693, "compression_ratio": 1.9416342412451362,
  "no_speech_prob": 0.006499853450804949}, {"id": 382, "seek": 196188, "start": 1966.2800000000002,
  "end": 1973.96, "text": " in and I think it I think it has a deep influence on how
  I can how I can lead the company but I don''t", "tokens": [50584, 294, 293, 286,
  519, 309, 286, 519, 309, 575, 257, 2452, 6503, 322, 577, 286, 393, 577, 286, 393,
  1477, 264, 2237, 457, 286, 500, 380, 50968], "temperature": 0.0, "avg_logprob":
  -0.11034653981526693, "compression_ratio": 1.9416342412451362, "no_speech_prob":
  0.006499853450804949}, {"id": 383, "seek": 196188, "start": 1973.96, "end": 1981.0800000000002,
  "text": " think it''s been I think I often think about something that tell them
  said you know the author of", "tokens": [50968, 519, 309, 311, 668, 286, 519, 286,
  2049, 519, 466, 746, 300, 980, 552, 848, 291, 458, 264, 3793, 295, 51324], "temperature":
  0.0, "avg_logprob": -0.11034653981526693, "compression_ratio": 1.9416342412451362,
  "no_speech_prob": 0.006499853450804949}, {"id": 384, "seek": 196188, "start": 1981.0800000000002,
  "end": 1986.6000000000001, "text": " anti fragile and a bunch of other books is
  that you the best authors of books are not the ones that", "tokens": [51324, 6061,
  23847, 293, 257, 3840, 295, 661, 3642, 307, 300, 291, 264, 1151, 16552, 295, 3642,
  366, 406, 264, 2306, 300, 51600], "temperature": 0.0, "avg_logprob": -0.11034653981526693,
  "compression_ratio": 1.9416342412451362, "no_speech_prob": 0.006499853450804949},
  {"id": 385, "seek": 196188, "start": 1986.6000000000001, "end": 1990.7600000000002,
  "text": " sit down and like you know read a bunch of papers then write a page then
  read another paper write a", "tokens": [51600, 1394, 760, 293, 411, 291, 458, 1401,
  257, 3840, 295, 10577, 550, 2464, 257, 3028, 550, 1401, 1071, 3035, 2464, 257, 51808],
  "temperature": 0.0, "avg_logprob": -0.11034653981526693, "compression_ratio": 1.9416342412451362,
  "no_speech_prob": 0.006499853450804949}, {"id": 386, "seek": 199076, "start": 1990.76,
  "end": 1995.64, "text": " page the best books are written by people who just you
  know go to the cabin sit down write 500", "tokens": [50364, 3028, 264, 1151, 3642,
  366, 3720, 538, 561, 567, 445, 291, 458, 352, 281, 264, 9401, 1394, 760, 2464, 5923,
  50608], "temperature": 0.0, "avg_logprob": -0.08123855931418282, "compression_ratio":
  1.7794117647058822, "no_speech_prob": 0.0060724420472979546}, {"id": 387, "seek":
  199076, "start": 1995.64, "end": 2000.44, "text": " pages and and hit publish of
  course that''s not what actually happens but if you read it to let books", "tokens":
  [50608, 7183, 293, 293, 2045, 11374, 295, 1164, 300, 311, 406, 437, 767, 2314, 457,
  498, 291, 1401, 309, 281, 718, 3642, 50848], "temperature": 0.0, "avg_logprob":
  -0.08123855931418282, "compression_ratio": 1.7794117647058822, "no_speech_prob":
  0.0060724420472979546}, {"id": 388, "seek": 199076, "start": 2000.44, "end": 2004.92,
  "text": " it''s probably pretty close to what actually happened and he just has
  the citations in his head", "tokens": [50848, 309, 311, 1391, 1238, 1998, 281, 437,
  767, 2011, 293, 415, 445, 575, 264, 4814, 763, 294, 702, 1378, 51072], "temperature":
  0.0, "avg_logprob": -0.08123855931418282, "compression_ratio": 1.7794117647058822,
  "no_speech_prob": 0.0060724420472979546}, {"id": 389, "seek": 199076, "start": 2005.56,
  "end": 2011.8799999999999, "text": " and I think about that often when building
  this company that it has felt like I''ve worked or this", "tokens": [51104, 293,
  286, 519, 466, 300, 2049, 562, 2390, 341, 2237, 300, 309, 575, 2762, 411, 286, 600,
  2732, 420, 341, 51420], "temperature": 0.0, "avg_logprob": -0.08123855931418282,
  "compression_ratio": 1.7794117647058822, "no_speech_prob": 0.0060724420472979546},
  {"id": 390, "seek": 199076, "start": 2011.8799999999999, "end": 2017.08, "text":
  " my whole life without knowing for it and I feel every every morning that I wake
  up that this is", "tokens": [51420, 452, 1379, 993, 1553, 5276, 337, 309, 293, 286,
  841, 633, 633, 2446, 300, 286, 6634, 493, 300, 341, 307, 51680], "temperature":
  0.0, "avg_logprob": -0.08123855931418282, "compression_ratio": 1.7794117647058822,
  "no_speech_prob": 0.0060724420472979546}, {"id": 391, "seek": 201708, "start": 2017.08,
  "end": 2023.24, "text": " exactly what it has led up to so it''s very naturally
  even if it wasn''t go onto itself that it", "tokens": [50364, 2293, 437, 309, 575,
  4684, 493, 281, 370, 309, 311, 588, 8195, 754, 498, 309, 2067, 380, 352, 3911, 2564,
  300, 309, 50672], "temperature": 0.0, "avg_logprob": -0.11179924011230469, "compression_ratio":
  1.6302521008403361, "no_speech_prob": 0.010730314999818802}, {"id": 392, "seek":
  201708, "start": 2023.24, "end": 2029.8, "text": " makes sense with the experience
  I''ve had to do exactly this and I tremendously enjoy it but it''s", "tokens": [50672,
  1669, 2020, 365, 264, 1752, 286, 600, 632, 281, 360, 2293, 341, 293, 286, 27985,
  2103, 309, 457, 309, 311, 51000], "temperature": 0.0, "avg_logprob": -0.11179924011230469,
  "compression_ratio": 1.6302521008403361, "no_speech_prob": 0.010730314999818802},
  {"id": 393, "seek": 201708, "start": 2029.8, "end": 2035.96, "text": " not a simplistic
  answer to do I miss coding no I want to make this company incredibly successful",
  "tokens": [51000, 406, 257, 44199, 1867, 281, 360, 286, 1713, 17720, 572, 286, 528,
  281, 652, 341, 2237, 6252, 4406, 51308], "temperature": 0.0, "avg_logprob": -0.11179924011230469,
  "compression_ratio": 1.6302521008403361, "no_speech_prob": 0.010730314999818802},
  {"id": 394, "seek": 201708, "start": 2036.76, "end": 2042.36, "text": " but sometimes
  I will do it as a recreational activity yeah I mean definitely like when I look
  at you", "tokens": [51348, 457, 2171, 286, 486, 360, 309, 382, 257, 37554, 5191,
  1338, 286, 914, 2138, 411, 562, 286, 574, 412, 291, 51628], "temperature": 0.0,
  "avg_logprob": -0.11179924011230469, "compression_ratio": 1.6302521008403361, "no_speech_prob":
  0.010730314999818802}, {"id": 395, "seek": 204236, "start": 2043.32, "end": 2048.6,
  "text": " like on twitter for example you come across as a very technical person
  and you are for sure right", "tokens": [50412, 411, 322, 21439, 337, 1365, 291,
  808, 2108, 382, 257, 588, 6191, 954, 293, 291, 366, 337, 988, 558, 50676], "temperature":
  0.0, "avg_logprob": -0.09982621042351973, "compression_ratio": 1.7268722466960353,
  "no_speech_prob": 0.013405069708824158}, {"id": 396, "seek": 204236, "start": 2048.6,
  "end": 2053.88, "text": " even though you know that to grow your business you need
  to do a lot of other activities but at the same", "tokens": [50676, 754, 1673, 291,
  458, 300, 281, 1852, 428, 1606, 291, 643, 281, 360, 257, 688, 295, 661, 5354, 457,
  412, 264, 912, 50940], "temperature": 0.0, "avg_logprob": -0.09982621042351973,
  "compression_ratio": 1.7268722466960353, "no_speech_prob": 0.013405069708824158},
  {"id": 397, "seek": 204236, "start": 2053.88, "end": 2060.68, "text": " time I mean
  yeah I don''t mean to ask it in a way that hey you regret now that you do sales
  you", "tokens": [50940, 565, 286, 914, 1338, 286, 500, 380, 914, 281, 1029, 309,
  294, 257, 636, 300, 4177, 291, 10879, 586, 300, 291, 360, 5763, 291, 51280], "temperature":
  0.0, "avg_logprob": -0.09982621042351973, "compression_ratio": 1.7268722466960353,
  "no_speech_prob": 0.013405069708824158}, {"id": 398, "seek": 204236, "start": 2060.68,
  "end": 2067.7999999999997, "text": " regret not doing more coding which which is
  not true you still do that and I think that all of", "tokens": [51280, 10879, 406,
  884, 544, 17720, 597, 597, 307, 406, 2074, 291, 920, 360, 300, 293, 286, 519, 300,
  439, 295, 51636], "temperature": 0.0, "avg_logprob": -0.09982621042351973, "compression_ratio":
  1.7268722466960353, "no_speech_prob": 0.013405069708824158}, {"id": 399, "seek":
  206780, "start": 2067.88, "end": 2073.32, "text": " all of the engineers will become
  better engineers if they learn the mastery of actually presenting", "tokens": [50368,
  439, 295, 264, 11955, 486, 1813, 1101, 11955, 498, 436, 1466, 264, 37951, 295, 767,
  15578, 50640], "temperature": 0.0, "avg_logprob": -0.06293760437563241, "compression_ratio":
  1.8046511627906976, "no_speech_prob": 0.008376692421734333}, {"id": 400, "seek":
  206780, "start": 2073.32, "end": 2079.96, "text": " what they do right and then
  they will not need a middle layer or someone else who will go and talk", "tokens":
  [50640, 437, 436, 360, 558, 293, 550, 436, 486, 406, 643, 257, 2808, 4583, 420,
  1580, 1646, 567, 486, 352, 293, 751, 50972], "temperature": 0.0, "avg_logprob":
  -0.06293760437563241, "compression_ratio": 1.8046511627906976, "no_speech_prob":
  0.008376692421734333}, {"id": 401, "seek": 206780, "start": 2079.96, "end": 2086.2000000000003,
  "text": " to that product manager or whoever else needs to talk to right so they
  can actually represent", "tokens": [50972, 281, 300, 1674, 6598, 420, 11387, 1646,
  2203, 281, 751, 281, 558, 370, 436, 393, 767, 2906, 51284], "temperature": 0.0,
  "avg_logprob": -0.06293760437563241, "compression_ratio": 1.8046511627906976, "no_speech_prob":
  0.008376692421734333}, {"id": 402, "seek": 206780, "start": 2086.2000000000003,
  "end": 2094.28, "text": " themselves but also I also love how you put it really
  eloquently that what is your idle activity", "tokens": [51284, 2969, 457, 611, 286,
  611, 959, 577, 291, 829, 309, 534, 38682, 47519, 300, 437, 307, 428, 30650, 5191,
  51688], "temperature": 0.0, "avg_logprob": -0.06293760437563241, "compression_ratio":
  1.8046511627906976, "no_speech_prob": 0.008376692421734333}, {"id": 403, "seek":
  209428, "start": 2094.28, "end": 2099.48, "text": " right what do you what''s your
  affinity what you gravitate to and I actually can it resonates a lot", "tokens":
  [50364, 558, 437, 360, 291, 437, 311, 428, 39703, 437, 291, 7427, 8086, 281, 293,
  286, 767, 393, 309, 41051, 257, 688, 50624], "temperature": 0.0, "avg_logprob":
  -0.11267517708443306, "compression_ratio": 1.749090909090909, "no_speech_prob":
  0.005634230561554432}, {"id": 404, "seek": 209428, "start": 2099.48, "end": 2104.84,
  "text": " with me because my idle activity that I''m really nervous that I do nothing
  especially on vacations", "tokens": [50624, 365, 385, 570, 452, 30650, 5191, 300,
  286, 478, 534, 6296, 300, 286, 360, 1825, 2318, 322, 2842, 763, 50892], "temperature":
  0.0, "avg_logprob": -0.11267517708443306, "compression_ratio": 1.749090909090909,
  "no_speech_prob": 0.005634230561554432}, {"id": 405, "seek": 209428, "start": 2104.84,
  "end": 2111.0800000000004, "text": " I start coding you know I just go and just
  okay let''s just let''s just hypothesize about something", "tokens": [50892, 286,
  722, 17720, 291, 458, 286, 445, 352, 293, 445, 1392, 718, 311, 445, 718, 311, 445,
  14276, 1125, 466, 746, 51204], "temperature": 0.0, "avg_logprob": -0.11267517708443306,
  "compression_ratio": 1.749090909090909, "no_speech_prob": 0.005634230561554432},
  {"id": 406, "seek": 209428, "start": 2111.0800000000004, "end": 2116.52, "text":
  " but let''s let''s dial back for for the into the architecture like when I look
  at the architecture", "tokens": [51204, 457, 718, 311, 718, 311, 5502, 646, 337,
  337, 264, 666, 264, 9482, 411, 562, 286, 574, 412, 264, 9482, 51476], "temperature":
  0.0, "avg_logprob": -0.11267517708443306, "compression_ratio": 1.749090909090909,
  "no_speech_prob": 0.005634230561554432}, {"id": 407, "seek": 209428, "start": 2116.52,
  "end": 2123.96, "text": " page of turbo buffer it''s very simple it''s like client
  connecting over you know TCP to a", "tokens": [51476, 3028, 295, 20902, 21762, 309,
  311, 588, 2199, 309, 311, 411, 6423, 11015, 670, 291, 458, 48965, 281, 257, 51848],
  "temperature": 0.0, "avg_logprob": -0.11267517708443306, "compression_ratio": 1.749090909090909,
  "no_speech_prob": 0.005634230561554432}, {"id": 408, "seek": 212428, "start": 2124.52,
  "end": 2131.0800000000004, "text": " database instance and it has just two components
  they are memory or SSD cache and the object storage", "tokens": [50376, 8149, 5197,
  293, 309, 575, 445, 732, 6677, 436, 366, 4675, 420, 30262, 19459, 293, 264, 2657,
  6725, 50704], "temperature": 0.0, "avg_logprob": -0.11734734025112419, "compression_ratio":
  1.7692307692307692, "no_speech_prob": 0.0049712578766047955}, {"id": 409, "seek":
  212428, "start": 2131.8, "end": 2137.8, "text": " tell me a bit more so I think
  our listeners and I mostly know what object storage is but tell me a", "tokens":
  [50740, 980, 385, 257, 857, 544, 370, 286, 519, 527, 23274, 293, 286, 5240, 458,
  437, 2657, 6725, 307, 457, 980, 385, 257, 51040], "temperature": 0.0, "avg_logprob":
  -0.11734734025112419, "compression_ratio": 1.7692307692307692, "no_speech_prob":
  0.0049712578766047955}, {"id": 410, "seek": 212428, "start": 2137.8, "end": 2143.8,
  "text": " bit more about that memory component like what algorithm design went into
  that maybe trade-offs and", "tokens": [51040, 857, 544, 466, 300, 4675, 6542, 411,
  437, 9284, 1715, 1437, 666, 300, 1310, 4923, 12, 19231, 293, 51340], "temperature":
  0.0, "avg_logprob": -0.11734734025112419, "compression_ratio": 1.7692307692307692,
  "no_speech_prob": 0.0049712578766047955}, {"id": 411, "seek": 212428, "start": 2144.36,
  "end": 2149.7200000000003, "text": " you know how frequently you need to do the
  round trips to the object storage versus when we", "tokens": [51368, 291, 458, 577,
  10374, 291, 643, 281, 360, 264, 3098, 16051, 281, 264, 2657, 6725, 5717, 562, 321,
  51636], "temperature": 0.0, "avg_logprob": -0.11734734025112419, "compression_ratio":
  1.7692307692307692, "no_speech_prob": 0.0049712578766047955}, {"id": 412, "seek":
  214972, "start": 2149.72, "end": 2155.3199999999997, "text": " actually don''t do
  that yeah I think it would be easiest to do this by speaking about the lifetime",
  "tokens": [50364, 767, 500, 380, 360, 300, 1338, 286, 519, 309, 576, 312, 12889,
  281, 360, 341, 538, 4124, 466, 264, 11364, 50644], "temperature": 0.0, "avg_logprob":
  -0.13326539491352282, "compression_ratio": 1.72, "no_speech_prob": 0.0014006359269842505},
  {"id": 413, "seek": 214972, "start": 2155.3199999999997, "end": 2163.56, "text":
  " of a request as the cache worms so we we''ll actually start with the right path
  and when when you do", "tokens": [50644, 295, 257, 5308, 382, 264, 19459, 28271,
  370, 321, 321, 603, 767, 722, 365, 264, 558, 3100, 293, 562, 562, 291, 360, 51056],
  "temperature": 0.0, "avg_logprob": -0.13326539491352282, "compression_ratio": 1.72,
  "no_speech_prob": 0.0014006359269842505}, {"id": 414, "seek": 214972, "start": 2163.56,
  "end": 2169.3199999999997, "text": " a right into turbo buffer it''s as simple as
  you can imagine it I mean at this point we''ve", "tokens": [51056, 257, 558, 666,
  20902, 21762, 309, 311, 382, 2199, 382, 291, 393, 3811, 309, 286, 914, 412, 341,
  935, 321, 600, 51344], "temperature": 0.0, "avg_logprob": -0.13326539491352282,
  "compression_ratio": 1.72, "no_speech_prob": 0.0014006359269842505}, {"id": 415,
  "seek": 214972, "start": 2169.3199999999997, "end": 2175.08, "text": " optimized
  parts of it that it''s not this simple but this is the the best way to explain it
  when you", "tokens": [51344, 26941, 3166, 295, 309, 300, 309, 311, 406, 341, 2199,
  457, 341, 307, 264, 264, 1151, 636, 281, 2903, 309, 562, 291, 51632], "temperature":
  0.0, "avg_logprob": -0.13326539491352282, "compression_ratio": 1.72, "no_speech_prob":
  0.0014006359269842505}, {"id": 416, "seek": 217508, "start": 2175.56, "end": 2182.36,
  "text": " when you do a right to turbo buffer that right basically goes into a file
  in a directory called the", "tokens": [50388, 562, 291, 360, 257, 558, 281, 20902,
  21762, 300, 558, 1936, 1709, 666, 257, 3991, 294, 257, 21120, 1219, 264, 50728],
  "temperature": 0.0, "avg_logprob": -0.10825415580503402, "compression_ratio": 1.8660287081339713,
  "no_speech_prob": 0.0017396729672327638}, {"id": 417, "seek": 217508, "start": 2182.36,
  "end": 2189.08, "text": " right ahead log so when you write to a namespace you can
  imagine that on s3 it''s like slash namespace", "tokens": [50728, 558, 2286, 3565,
  370, 562, 291, 2464, 281, 257, 5288, 17940, 291, 393, 3811, 300, 322, 262, 18, 309,
  311, 411, 17330, 5288, 17940, 51064], "temperature": 0.0, "avg_logprob": -0.10825415580503402,
  "compression_ratio": 1.8660287081339713, "no_speech_prob": 0.0017396729672327638},
  {"id": 418, "seek": 217508, "start": 2189.08, "end": 2194.12, "text": " slash you
  know right ahead log the right ahead log is basically just a sequence of all the
  rights", "tokens": [51064, 17330, 291, 458, 558, 2286, 3565, 264, 558, 2286, 3565,
  307, 1936, 445, 257, 8310, 295, 439, 264, 4601, 51316], "temperature": 0.0, "avg_logprob":
  -0.10825415580503402, "compression_ratio": 1.8660287081339713, "no_speech_prob":
  0.0017396729672327638}, {"id": 419, "seek": 217508, "start": 2194.12, "end": 2199.72,
  "text": " in order the raw rights so you do your right and it might be okay I''m
  inserting a document", "tokens": [51316, 294, 1668, 264, 8936, 4601, 370, 291, 360,
  428, 558, 293, 309, 1062, 312, 1392, 286, 478, 46567, 257, 4166, 51596], "temperature":
  0.0, "avg_logprob": -0.10825415580503402, "compression_ratio": 1.8660287081339713,
  "no_speech_prob": 0.0017396729672327638}, {"id": 420, "seek": 219972, "start": 2199.8799999999997,
  "end": 2205.3999999999996, "text": " with text the metri and one with text Simon
  and those are the two documents you can in the simplest", "tokens": [50372, 365,
  2487, 264, 1131, 470, 293, 472, 365, 2487, 13193, 293, 729, 366, 264, 732, 8512,
  291, 393, 294, 264, 22811, 50648], "temperature": 0.0, "avg_logprob": -0.12305951551957564,
  "compression_ratio": 1.853846153846154, "no_speech_prob": 0.0010597704676911235},
  {"id": 421, "seek": 219972, "start": 2205.3999999999996, "end": 2211.3199999999997,
  "text": " way you can imagine that this file is called zero job JSON and the next
  one is called one dot JSON", "tokens": [50648, 636, 291, 393, 3811, 300, 341, 3991,
  307, 1219, 4018, 1691, 31828, 293, 264, 958, 472, 307, 1219, 472, 5893, 31828, 50944],
  "temperature": 0.0, "avg_logprob": -0.12305951551957564, "compression_ratio": 1.853846153846154,
  "no_speech_prob": 0.0010597704676911235}, {"id": 422, "seek": 219972, "start": 2211.3199999999997,
  "end": 2216.3599999999997, "text": " three dot JSON that''s a database right that''s
  just the right ahead log and if you want to satisfy a", "tokens": [50944, 1045,
  5893, 31828, 300, 311, 257, 8149, 558, 300, 311, 445, 264, 558, 2286, 3565, 293,
  498, 291, 528, 281, 19319, 257, 51196], "temperature": 0.0, "avg_logprob": -0.12305951551957564,
  "compression_ratio": 1.853846153846154, "no_speech_prob": 0.0010597704676911235},
  {"id": 423, "seek": 219972, "start": 2216.3599999999997, "end": 2222.6, "text":
  " query you just scan through all the JSON documents and you satisfy the query that''s
  actually", "tokens": [51196, 14581, 291, 445, 11049, 807, 439, 264, 31828, 8512,
  293, 291, 19319, 264, 14581, 300, 311, 767, 51508], "temperature": 0.0, "avg_logprob":
  -0.12305951551957564, "compression_ratio": 1.853846153846154, "no_speech_prob":
  0.0010597704676911235}, {"id": 424, "seek": 219972, "start": 2222.6, "end": 2228.12,
  "text": " respectable database and it''s not even that far from the first version
  of turbo buffer but", "tokens": [51508, 44279, 8149, 293, 309, 311, 406, 754, 300,
  1400, 490, 264, 700, 3037, 295, 20902, 21762, 457, 51784], "temperature": 0.0, "avg_logprob":
  -0.12305951551957564, "compression_ratio": 1.853846153846154, "no_speech_prob":
  0.0010597704676911235}, {"id": 425, "seek": 222812, "start": 2229.08, "end": 2235.08,
  "text": " of course you have to index that data as well so basically as you can
  imagine once many", "tokens": [50412, 295, 1164, 291, 362, 281, 8186, 300, 1412,
  382, 731, 370, 1936, 382, 291, 393, 3811, 1564, 867, 50712], "temperature": 0.0,
  "avg_logprob": -0.13026620066443154, "compression_ratio": 1.86, "no_speech_prob":
  0.0007774747209623456}, {"id": 426, "seek": 222812, "start": 2235.08, "end": 2241.16,
  "text": " megabytes of data come in asynchronously an indexing node will pick it
  up and put it into the", "tokens": [50712, 10816, 24538, 295, 1412, 808, 294, 42642,
  5098, 364, 8186, 278, 9984, 486, 1888, 309, 493, 293, 829, 309, 666, 264, 51016],
  "temperature": 0.0, "avg_logprob": -0.13026620066443154, "compression_ratio": 1.86,
  "no_speech_prob": 0.0007774747209623456}, {"id": 427, "seek": 222812, "start": 2241.16,
  "end": 2247.24, "text": " inverted index for full text search put it into an a and
  an index for vector search and put it", "tokens": [51016, 38969, 8186, 337, 1577,
  2487, 3164, 829, 309, 666, 364, 257, 293, 364, 8186, 337, 8062, 3164, 293, 829,
  309, 51320], "temperature": 0.0, "avg_logprob": -0.13026620066443154, "compression_ratio":
  1.86, "no_speech_prob": 0.0007774747209623456}, {"id": 428, "seek": 222812, "start":
  2247.24, "end": 2254.3599999999997, "text": " into a attribute or filtering index
  for other attributes and there will be other indexing types", "tokens": [51320,
  666, 257, 19667, 420, 30822, 8186, 337, 661, 17212, 293, 456, 486, 312, 661, 8186,
  278, 3467, 51676], "temperature": 0.0, "avg_logprob": -0.13026620066443154, "compression_ratio":
  1.86, "no_speech_prob": 0.0007774747209623456}, {"id": 429, "seek": 225436, "start":
  2254.36, "end": 2259.7200000000003, "text": " in the future when when that happens
  it will put it into slash namespace slash index and just", "tokens": [50364, 294,
  264, 2027, 562, 562, 300, 2314, 309, 486, 829, 309, 666, 17330, 5288, 17940, 17330,
  8186, 293, 445, 50632], "temperature": 0.0, "avg_logprob": -0.12587163255021377,
  "compression_ratio": 1.9291338582677164, "no_speech_prob": 0.0021439732518047094},
  {"id": 430, "seek": 225436, "start": 2259.7200000000003, "end": 2265.2400000000002,
  "text": " start putting files in there right and then the query layer can then consult
  those files right instead", "tokens": [50632, 722, 3372, 7098, 294, 456, 558, 293,
  550, 264, 14581, 4583, 393, 550, 7189, 729, 7098, 558, 2602, 50908], "temperature":
  0.0, "avg_logprob": -0.12587163255021377, "compression_ratio": 1.9291338582677164,
  "no_speech_prob": 0.0021439732518047094}, {"id": 431, "seek": 225436, "start": 2265.2400000000002,
  "end": 2269.6400000000003, "text": " of scanning through every single document to
  find a metri you can just plop in and look at the", "tokens": [50908, 295, 27019,
  807, 633, 2167, 4166, 281, 915, 257, 1131, 470, 291, 393, 445, 499, 404, 294, 293,
  574, 412, 264, 51128], "temperature": 0.0, "avg_logprob": -0.12587163255021377,
  "compression_ratio": 1.9291338582677164, "no_speech_prob": 0.0021439732518047094},
  {"id": 432, "seek": 225436, "start": 2269.6400000000003, "end": 2275.7200000000003,
  "text": " metri in the inverted index find the document and return it that''s how
  right works when a right", "tokens": [51128, 1131, 470, 294, 264, 38969, 8186, 915,
  264, 4166, 293, 2736, 309, 300, 311, 577, 558, 1985, 562, 257, 558, 51432], "temperature":
  0.0, "avg_logprob": -0.12587163255021377, "compression_ratio": 1.9291338582677164,
  "no_speech_prob": 0.0021439732518047094}, {"id": 433, "seek": 225436, "start": 2275.7200000000003,
  "end": 2282.1200000000003, "text": " happens it will go through one of the query
  nodes and the right will be also written into the into the", "tokens": [51432, 2314,
  309, 486, 352, 807, 472, 295, 264, 14581, 13891, 293, 264, 558, 486, 312, 611, 3720,
  666, 264, 666, 264, 51752], "temperature": 0.0, "avg_logprob": -0.12587163255021377,
  "compression_ratio": 1.9291338582677164, "no_speech_prob": 0.0021439732518047094},
  {"id": 434, "seek": 228212, "start": 2282.2, "end": 2291.88, "text": " cache right
  so both the memory cache and the disk cache and when so when you do a query you
  will go", "tokens": [50368, 19459, 558, 370, 1293, 264, 4675, 19459, 293, 264, 12355,
  19459, 293, 562, 370, 562, 291, 360, 257, 14581, 291, 486, 352, 50852], "temperature":
  0.0, "avg_logprob": -0.15899950458157447, "compression_ratio": 1.976284584980237,
  "no_speech_prob": 0.0017899831291288137}, {"id": 435, "seek": 228212, "start": 2291.88,
  "end": 2295.56, "text": " to that same query node right there''s a consistent hashing
  so if there''s three it''s sort of like the", "tokens": [50852, 281, 300, 912, 14581,
  9984, 558, 456, 311, 257, 8398, 575, 571, 370, 498, 456, 311, 1045, 309, 311, 1333,
  295, 411, 264, 51036], "temperature": 0.0, "avg_logprob": -0.15899950458157447,
  "compression_ratio": 1.976284584980237, "no_speech_prob": 0.0017899831291288137},
  {"id": 436, "seek": 228212, "start": 2295.56, "end": 2300.3599999999997, "text":
  " same namespace will end up on node one all the time if it hashes that I know when
  you''ve satisfied", "tokens": [51036, 912, 5288, 17940, 486, 917, 493, 322, 9984,
  472, 439, 264, 565, 498, 309, 575, 8076, 300, 286, 458, 562, 291, 600, 11239, 51276],
  "temperature": 0.0, "avg_logprob": -0.15899950458157447, "compression_ratio": 1.976284584980237,
  "no_speech_prob": 0.0017899831291288137}, {"id": 437, "seek": 228212, "start": 2300.3599999999997,
  "end": 2305.48, "text": " when you when you do a query it will first take the cat
  check the caches if you just did the right well", "tokens": [51276, 562, 291, 562,
  291, 360, 257, 14581, 309, 486, 700, 747, 264, 3857, 1520, 264, 269, 13272, 498,
  291, 445, 630, 264, 558, 731, 51532], "temperature": 0.0, "avg_logprob": -0.15899950458157447,
  "compression_ratio": 1.976284584980237, "no_speech_prob": 0.0017899831291288137},
  {"id": 438, "seek": 228212, "start": 2306.12, "end": 2309.72, "text": " it''s already
  there because we just wrote all the rights into the cache to have this you know
  the", "tokens": [51564, 309, 311, 1217, 456, 570, 321, 445, 4114, 439, 264, 4601,
  666, 264, 19459, 281, 362, 341, 291, 458, 264, 51744], "temperature": 0.0, "avg_logprob":
  -0.15899950458157447, "compression_ratio": 1.976284584980237, "no_speech_prob":
  0.0017899831291288137}, {"id": 439, "seek": 230972, "start": 2309.72, "end": 2316.4399999999996,
  "text": " right through cache and and we will satisfy the query mainly from the
  cache if for whatever reason", "tokens": [50364, 558, 807, 19459, 293, 293, 321,
  486, 19319, 264, 14581, 8704, 490, 264, 19459, 498, 337, 2035, 1778, 50700], "temperature":
  0.0, "avg_logprob": -0.15967163153454267, "compression_ratio": 1.8671875, "no_speech_prob":
  0.0002784858806990087}, {"id": 440, "seek": 230972, "start": 2316.4399999999996,
  "end": 2320.68, "text": " this namespace is not maybe you did the right a month
  ago and so it''s following that", "tokens": [50700, 341, 5288, 17940, 307, 406,
  1310, 291, 630, 264, 558, 257, 1618, 2057, 293, 370, 309, 311, 3480, 300, 50912],
  "temperature": 0.0, "avg_logprob": -0.15967163153454267, "compression_ratio": 1.8671875,
  "no_speech_prob": 0.0002784858806990087}, {"id": 441, "seek": 230972, "start": 2320.68,
  "end": 2324.8399999999997, "text": " a cache and you do the read well then we''ll
  read through cache by going directly to opix storage", "tokens": [50912, 257, 19459,
  293, 291, 360, 264, 1401, 731, 550, 321, 603, 1401, 807, 19459, 538, 516, 3838,
  281, 999, 970, 6725, 51120], "temperature": 0.0, "avg_logprob": -0.15967163153454267,
  "compression_ratio": 1.8671875, "no_speech_prob": 0.0002784858806990087}, {"id":
  442, "seek": 230972, "start": 2324.8399999999997, "end": 2329.08, "text": " with
  its few round trips as possible to get the data to satisfy the query both from the
  index and", "tokens": [51120, 365, 1080, 1326, 3098, 16051, 382, 1944, 281, 483,
  264, 1412, 281, 19319, 264, 14581, 1293, 490, 264, 8186, 293, 51332], "temperature":
  0.0, "avg_logprob": -0.15967163153454267, "compression_ratio": 1.8671875, "no_speech_prob":
  0.0002784858806990087}, {"id": 443, "seek": 230972, "start": 2329.08, "end": 2335.16,
  "text": " from the wall will do range reads directly on s3 right the old like hcp
  range header to get exactly", "tokens": [51332, 490, 264, 2929, 486, 360, 3613,
  15700, 3838, 322, 262, 18, 558, 264, 1331, 411, 276, 66, 79, 3613, 23117, 281, 483,
  2293, 51636], "temperature": 0.0, "avg_logprob": -0.15967163153454267, "compression_ratio":
  1.8671875, "no_speech_prob": 0.0002784858806990087}, {"id": 444, "seek": 233516,
  "start": 2335.16, "end": 2341.3999999999996, "text": " the bytes we need to satisfy
  the query and then start hydrating the cache on the on the query node", "tokens":
  [50364, 264, 36088, 321, 643, 281, 19319, 264, 14581, 293, 550, 722, 5796, 8754,
  264, 19459, 322, 264, 322, 264, 14581, 9984, 50676], "temperature": 0.0, "avg_logprob":
  -0.13676319803510392, "compression_ratio": 1.9019607843137254, "no_speech_prob":
  0.0013332271482795477}, {"id": 445, "seek": 233516, "start": 2341.3999999999996,
  "end": 2345.96, "text": " so the subsequent queries get faster and faster and we
  can do that a gigabyte per second we can", "tokens": [50676, 370, 264, 19962, 24109,
  483, 4663, 293, 4663, 293, 321, 393, 360, 300, 257, 8741, 34529, 680, 1150, 321,
  393, 50904], "temperature": 0.0, "avg_logprob": -0.13676319803510392, "compression_ratio":
  1.9019607843137254, "no_speech_prob": 0.0013332271482795477}, {"id": 446, "seek":
  233516, "start": 2345.96, "end": 2352.3599999999997, "text": " hydrate the cache
  even for very very very large namespaces so that''s the general architecture of",
  "tokens": [50904, 5796, 4404, 264, 19459, 754, 337, 588, 588, 588, 2416, 5288, 79,
  2116, 370, 300, 311, 264, 2674, 9482, 295, 51224], "temperature": 0.0, "avg_logprob":
  -0.13676319803510392, "compression_ratio": 1.9019607843137254, "no_speech_prob":
  0.0013332271482795477}, {"id": 447, "seek": 233516, "start": 2352.3599999999997,
  "end": 2356.8399999999997, "text": " turbo puffer on a completely cold query it
  takes hundreds of milliseconds and on a warm query it", "tokens": [51224, 20902,
  19613, 260, 322, 257, 2584, 3554, 14581, 309, 2516, 6779, 295, 34184, 293, 322,
  257, 4561, 14581, 309, 51448], "temperature": 0.0, "avg_logprob": -0.13676319803510392,
  "compression_ratio": 1.9019607843137254, "no_speech_prob": 0.0013332271482795477},
  {"id": 448, "seek": 233516, "start": 2356.8399999999997, "end": 2362.92, "text":
  " can take as little as 10 milliseconds to to satisfy the query the the last detail
  I''ll point out", "tokens": [51448, 393, 747, 382, 707, 382, 1266, 34184, 281, 281,
  19319, 264, 14581, 264, 264, 1036, 2607, 286, 603, 935, 484, 51752], "temperature":
  0.0, "avg_logprob": -0.13676319803510392, "compression_ratio": 1.9019607843137254,
  "no_speech_prob": 0.0013332271482795477}, {"id": 449, "seek": 236292, "start": 2363.56,
  "end": 2368.6800000000003, "text": " and then we can go into a particular aspect
  of this is that turbo puffer has chosen to do consistent", "tokens": [50396, 293,
  550, 321, 393, 352, 666, 257, 1729, 4171, 295, 341, 307, 300, 20902, 19613, 260,
  575, 8614, 281, 360, 8398, 50652], "temperature": 0.0, "avg_logprob": -0.13058957513773217,
  "compression_ratio": 1.7343173431734318, "no_speech_prob": 0.005654902197420597},
  {"id": 450, "seek": 236292, "start": 2368.6800000000003, "end": 2373.7200000000003,
  "text": " reads by default this is an unusual choice for search engines we''ve seen
  doesn''t do this", "tokens": [50652, 15700, 538, 7576, 341, 307, 364, 10901, 3922,
  337, 3164, 12982, 321, 600, 1612, 1177, 380, 360, 341, 50904], "temperature": 0.0,
  "avg_logprob": -0.13058957513773217, "compression_ratio": 1.7343173431734318, "no_speech_prob":
  0.005654902197420597}, {"id": 451, "seek": 236292, "start": 2373.7200000000003,
  "end": 2377.16, "text": " unless you turn it on explicitly I think they''ve done
  more work now for real time indexing", "tokens": [50904, 5969, 291, 1261, 309, 322,
  20803, 286, 519, 436, 600, 1096, 544, 589, 586, 337, 957, 565, 8186, 278, 51076],
  "temperature": 0.0, "avg_logprob": -0.13058957513773217, "compression_ratio": 1.7343173431734318,
  "no_speech_prob": 0.005654902197420597}, {"id": 452, "seek": 236292, "start": 2377.96,
  "end": 2382.12, "text": " which to me is the gold standard which is why I keep referring
  back to it''s phenomenal piece of", "tokens": [51116, 597, 281, 385, 307, 264, 3821,
  3832, 597, 307, 983, 286, 1066, 13761, 646, 281, 309, 311, 17778, 2522, 295, 51324],
  "temperature": 0.0, "avg_logprob": -0.13058957513773217, "compression_ratio": 1.7343173431734318,
  "no_speech_prob": 0.005654902197420597}, {"id": 453, "seek": 236292, "start": 2382.12,
  "end": 2387.8, "text": " software and turbo power requests consistent reads by default
  meaning that if you do it right", "tokens": [51324, 4722, 293, 20902, 1347, 12475,
  8398, 15700, 538, 7576, 3620, 300, 498, 291, 360, 309, 558, 51608], "temperature":
  0.0, "avg_logprob": -0.13058957513773217, "compression_ratio": 1.7343173431734318,
  "no_speech_prob": 0.005654902197420597}, {"id": 454, "seek": 238780, "start": 2387.8,
  "end": 2393.96, "text": " and then you read immediately afterwards that right will
  be visible and in order to satisfy that", "tokens": [50364, 293, 550, 291, 1401,
  4258, 10543, 300, 558, 486, 312, 8974, 293, 294, 1668, 281, 19319, 300, 50672],
  "temperature": 0.0, "avg_logprob": -0.12860016744644914, "compression_ratio": 1.830827067669173,
  "no_speech_prob": 0.001849163556471467}, {"id": 455, "seek": 238780, "start": 2393.96,
  "end": 2398.92, "text": " we can''t just rely on the cache on that node being out
  of date that node could have died it could have", "tokens": [50672, 321, 393, 380,
  445, 10687, 322, 264, 19459, 322, 300, 9984, 885, 484, 295, 4002, 300, 9984, 727,
  362, 4539, 309, 727, 362, 50920], "temperature": 0.0, "avg_logprob": -0.12860016744644914,
  "compression_ratio": 1.830827067669173, "no_speech_prob": 0.001849163556471467},
  {"id": 456, "seek": 238780, "start": 2398.92, "end": 2405.88, "text": " you know
  the hashed ring could have moved because we scaled up so every single um query we
  go to", "tokens": [50920, 291, 458, 264, 22019, 292, 4875, 727, 362, 4259, 570,
  321, 36039, 493, 370, 633, 2167, 1105, 14581, 321, 352, 281, 51268], "temperature":
  0.0, "avg_logprob": -0.12860016744644914, "compression_ratio": 1.830827067669173,
  "no_speech_prob": 0.001849163556471467}, {"id": 457, "seek": 238780, "start": 2405.88,
  "end": 2411.7200000000003, "text": " op storage and see what is the latest entry
  in the wall and do we have that entry right is it at", "tokens": [51268, 999, 6725,
  293, 536, 437, 307, 264, 6792, 8729, 294, 264, 2929, 293, 360, 321, 362, 300, 8729,
  558, 307, 309, 412, 51560], "temperature": 0.0, "avg_logprob": -0.12860016744644914,
  "compression_ratio": 1.830827067669173, "no_speech_prob": 0.001849163556471467},
  {"id": 458, "seek": 238780, "start": 2411.7200000000003, "end": 2416.52, "text":
  " 3.json or is that 5.json and do I have that so we have a little pointer file that
  we can look", "tokens": [51560, 805, 13, 73, 3015, 420, 307, 300, 1025, 13, 73,
  3015, 293, 360, 286, 362, 300, 370, 321, 362, 257, 707, 23918, 3991, 300, 321, 393,
  574, 51800], "temperature": 0.0, "avg_logprob": -0.12860016744644914, "compression_ratio":
  1.830827067669173, "no_speech_prob": 0.001849163556471467}, {"id": 459, "seek":
  241652, "start": 2416.52, "end": 2422.6, "text": " and we can download and look
  at right and that round trip is basically our p50 like our spans", "tokens": [50364,
  293, 321, 393, 5484, 293, 574, 412, 558, 293, 300, 3098, 4931, 307, 1936, 527, 280,
  2803, 411, 527, 44086, 50668], "temperature": 0.0, "avg_logprob": -0.18321394264151197,
  "compression_ratio": 1.7985074626865671, "no_speech_prob": 0.004216221161186695},
  {"id": 460, "seek": 241652, "start": 2422.6, "end": 2427.96, "text": " are basically
  you know often like one to two milliseconds of actual search and then on gcs about",
  "tokens": [50668, 366, 1936, 291, 458, 2049, 411, 472, 281, 732, 34184, 295, 3539,
  3164, 293, 550, 322, 290, 14368, 466, 50936], "temperature": 0.0, "avg_logprob":
  -0.18321394264151197, "compression_ratio": 1.7985074626865671, "no_speech_prob":
  0.004216221161186695}, {"id": 461, "seek": 241652, "start": 2427.96, "end": 2435.72,
  "text": " depending on the region 12 to 16 milliseconds waiting for that consistency
  check on s3 the small", "tokens": [50936, 5413, 322, 264, 4458, 2272, 281, 3165,
  34184, 3806, 337, 300, 14416, 1520, 322, 262, 18, 264, 1359, 51324], "temperature":
  0.0, "avg_logprob": -0.18321394264151197, "compression_ratio": 1.7985074626865671,
  "no_speech_prob": 0.004216221161186695}, {"id": 462, "seek": 241652, "start": 2435.72,
  "end": 2440.28, "text": " obnoxiously it''s a little bit better so it''s eight milliseconds
  but you can turn this off and", "tokens": [51324, 1111, 29129, 8994, 309, 311, 257,
  707, 857, 1101, 370, 309, 311, 3180, 34184, 457, 291, 393, 1261, 341, 766, 293,
  51552], "temperature": 0.0, "avg_logprob": -0.18321394264151197, "compression_ratio":
  1.7985074626865671, "no_speech_prob": 0.004216221161186695}, {"id": 463, "seek":
  241652, "start": 2440.28, "end": 2445.4, "text": " you will still get up to you
  you can get eventual consistency that''s very normal for these databases", "tokens":
  [51552, 291, 486, 920, 483, 493, 281, 291, 291, 393, 483, 33160, 14416, 300, 311,
  588, 2710, 337, 613, 22380, 51808], "temperature": 0.0, "avg_logprob": -0.18321394264151197,
  "compression_ratio": 1.7985074626865671, "no_speech_prob": 0.004216221161186695},
  {"id": 464, "seek": 244540, "start": 2445.56, "end": 2449.7200000000003, "text":
  " like could be up to one minute out of date and then you can see often less than
  a millisecond", "tokens": [50372, 411, 727, 312, 493, 281, 472, 3456, 484, 295,
  4002, 293, 550, 291, 393, 536, 2049, 1570, 813, 257, 27940, 18882, 50580], "temperature":
  0.0, "avg_logprob": -0.16819244750002596, "compression_ratio": 1.7788018433179724,
  "no_speech_prob": 0.001846386818215251}, {"id": 465, "seek": 244540, "start": 2449.7200000000003,
  "end": 2454.6800000000003, "text": " or a millisecond latency to a turbo buffer
  by turning off that check but we find that this is a very", "tokens": [50580, 420,
  257, 27940, 18882, 27043, 281, 257, 20902, 21762, 538, 6246, 766, 300, 1520, 457,
  321, 915, 300, 341, 307, 257, 588, 50828], "temperature": 0.0, "avg_logprob": -0.16819244750002596,
  "compression_ratio": 1.7788018433179724, "no_speech_prob": 0.001846386818215251},
  {"id": 466, "seek": 244540, "start": 2454.6800000000003, "end": 2460.6, "text":
  " safe default and I think that database should ship with very safe and unsurprising
  defaults", "tokens": [50828, 3273, 7576, 293, 286, 519, 300, 8149, 820, 5374, 365,
  588, 3273, 293, 2693, 374, 26203, 7576, 82, 51124], "temperature": 0.0, "avg_logprob":
  -0.16819244750002596, "compression_ratio": 1.7788018433179724, "no_speech_prob":
  0.001846386818215251}, {"id": 467, "seek": 244540, "start": 2461.08, "end": 2469.56,
  "text": " yeah for sure for sure um so in that cache but you also have the you also
  have the let''s focus only", "tokens": [51148, 1338, 337, 988, 337, 988, 1105, 370,
  294, 300, 19459, 457, 291, 611, 362, 264, 291, 611, 362, 264, 718, 311, 1879, 787,
  51572], "temperature": 0.0, "avg_logprob": -0.16819244750002596, "compression_ratio":
  1.7788018433179724, "no_speech_prob": 0.001846386818215251}, {"id": 468, "seek":
  246956, "start": 2469.72, "end": 2476.04, "text": " back to search part for now
  you also have the a and n index is that also stored on s3 and then", "tokens": [50372,
  646, 281, 3164, 644, 337, 586, 291, 611, 362, 264, 257, 293, 297, 8186, 307, 300,
  611, 12187, 322, 262, 18, 293, 550, 50688], "temperature": 0.0, "avg_logprob": -0.16967498554902918,
  "compression_ratio": 1.746606334841629, "no_speech_prob": 0.00039154410478658974},
  {"id": 469, "seek": 246956, "start": 2476.6, "end": 2481.88, "text": " is it do
  you also keep kind of like a replica of it in memory to to quick access and how
  do you", "tokens": [50716, 307, 309, 360, 291, 611, 1066, 733, 295, 411, 257, 35456,
  295, 309, 294, 4675, 281, 281, 1702, 2105, 293, 577, 360, 291, 50980], "temperature":
  0.0, "avg_logprob": -0.16967498554902918, "compression_ratio": 1.746606334841629,
  "no_speech_prob": 0.00039154410478658974}, {"id": 470, "seek": 246956, "start":
  2481.88, "end": 2489.16, "text": " sort of it''s true how do you sort of synchronize
  the two both the right-ahead log and the index are", "tokens": [50980, 1333, 295,
  309, 311, 2074, 577, 360, 291, 1333, 295, 19331, 1125, 264, 732, 1293, 264, 558,
  12, 545, 2056, 3565, 293, 264, 8186, 366, 51344], "temperature": 0.0, "avg_logprob":
  -0.16967498554902918, "compression_ratio": 1.746606334841629, "no_speech_prob":
  0.00039154410478658974}, {"id": 471, "seek": 246956, "start": 2490.36, "end": 2497.32,
  "text": " everything is stored on s3 if you killed all of the compute nodes of turbo
  buffer in all of our", "tokens": [51404, 1203, 307, 12187, 322, 262, 18, 498, 291,
  4652, 439, 295, 264, 14722, 13891, 295, 20902, 21762, 294, 439, 295, 527, 51752],
  "temperature": 0.0, "avg_logprob": -0.16967498554902918, "compression_ratio": 1.746606334841629,
  "no_speech_prob": 0.00039154410478658974}, {"id": 472, "seek": 249732, "start":
  2497.32, "end": 2502.92, "text": " clusters we would not lose any data there is
  no data on the compute notes that matter it''s", "tokens": [50364, 23313, 321, 576,
  406, 3624, 604, 1412, 456, 307, 572, 1412, 322, 264, 14722, 5570, 300, 1871, 309,
  311, 50644], "temperature": 0.0, "avg_logprob": -0.08279361222919665, "compression_ratio":
  1.8202247191011236, "no_speech_prob": 0.0046958220191299915}, {"id": 473, "seek":
  249732, "start": 2502.92, "end": 2507.4, "text": " only transient caching but we
  cache everything yeah if you''re accessing the index will cache the", "tokens":
  [50644, 787, 41998, 269, 2834, 457, 321, 19459, 1203, 1338, 498, 291, 434, 26440,
  264, 8186, 486, 19459, 264, 50868], "temperature": 0.0, "avg_logprob": -0.08279361222919665,
  "compression_ratio": 1.8202247191011236, "no_speech_prob": 0.0046958220191299915},
  {"id": 474, "seek": 249732, "start": 2507.4, "end": 2512.36, "text": " index if
  you''re just accessing the right-ahead log files because it''s so small or there''s
  parts of", "tokens": [50868, 8186, 498, 291, 434, 445, 26440, 264, 558, 12, 545,
  2056, 3565, 7098, 570, 309, 311, 370, 1359, 420, 456, 311, 3166, 295, 51116], "temperature":
  0.0, "avg_logprob": -0.08279361222919665, "compression_ratio": 1.8202247191011236,
  "no_speech_prob": 0.0046958220191299915}, {"id": 475, "seek": 249732, "start": 2512.36,
  "end": 2516.76, "text": " the data that hasn''t been indexed then and that''s also
  on s3 and goes into the same cache with", "tokens": [51116, 264, 1412, 300, 6132,
  380, 668, 8186, 292, 550, 293, 300, 311, 611, 322, 262, 18, 293, 1709, 666, 264,
  912, 19459, 365, 51336], "temperature": 0.0, "avg_logprob": -0.08279361222919665,
  "compression_ratio": 1.8202247191011236, "no_speech_prob": 0.0046958220191299915},
  {"id": 476, "seek": 249732, "start": 2516.76, "end": 2521.7200000000003, "text":
  " everything else right prioritized by the workloads to try to get the best performance
  possible yeah it''s", "tokens": [51336, 1203, 1646, 558, 14846, 1602, 538, 264,
  32452, 281, 853, 281, 483, 264, 1151, 3389, 1944, 1338, 309, 311, 51584], "temperature":
  0.0, "avg_logprob": -0.08279361222919665, "compression_ratio": 1.8202247191011236,
  "no_speech_prob": 0.0046958220191299915}, {"id": 477, "seek": 252172, "start": 2521.72,
  "end": 2529.08, "text": " quite smart so effectively you like I remember like at
  some previous companies when I was running", "tokens": [50364, 1596, 4069, 370,
  8659, 291, 411, 286, 1604, 411, 412, 512, 3894, 3431, 562, 286, 390, 2614, 50732],
  "temperature": 0.0, "avg_logprob": -0.11721773897663931, "compression_ratio": 1.636734693877551,
  "no_speech_prob": 0.002499124500900507}, {"id": 478, "seek": 252172, "start": 2529.08,
  "end": 2534.52, "text": " Apache Solar one of the problems was always that all of
  these charts are super cold because they''re", "tokens": [50732, 46597, 22385, 472,
  295, 264, 2740, 390, 1009, 300, 439, 295, 613, 17767, 366, 1687, 3554, 570, 436,
  434, 51004], "temperature": 0.0, "avg_logprob": -0.11721773897663931, "compression_ratio":
  1.636734693877551, "no_speech_prob": 0.002499124500900507}, {"id": 479, "seek":
  252172, "start": 2534.52, "end": 2541.72, "text": " never used right we still pay
  for them but then when the query hits you incur so much latency that''s", "tokens":
  [51004, 1128, 1143, 558, 321, 920, 1689, 337, 552, 457, 550, 562, 264, 14581, 8664,
  291, 35774, 370, 709, 27043, 300, 311, 51364], "temperature": 0.0, "avg_logprob":
  -0.11721773897663931, "compression_ratio": 1.636734693877551, "no_speech_prob":
  0.002499124500900507}, {"id": 480, "seek": 252172, "start": 2541.72, "end": 2549.48,
  "text": " super painful and so I was always coming up with these ideas what if I
  run some you know post indexing", "tokens": [51364, 1687, 11697, 293, 370, 286,
  390, 1009, 1348, 493, 365, 613, 3487, 437, 498, 286, 1190, 512, 291, 458, 2183,
  8186, 278, 51752], "temperature": 0.0, "avg_logprob": -0.11721773897663931, "compression_ratio":
  1.636734693877551, "no_speech_prob": 0.002499124500900507}, {"id": 481, "seek":
  254948, "start": 2549.48, "end": 2553.96, "text": " warm-up script that will go
  and shoot a bunch of queries to all of the charts just to keep them", "tokens":
  [50364, 4561, 12, 1010, 5755, 300, 486, 352, 293, 3076, 257, 3840, 295, 24109, 281,
  439, 295, 264, 17767, 445, 281, 1066, 552, 50588], "temperature": 0.0, "avg_logprob":
  -0.11731377468314222, "compression_ratio": 1.6, "no_speech_prob": 0.0033323941752314568},
  {"id": 482, "seek": 254948, "start": 2554.6, "end": 2562.68, "text": " you know
  up and running and and warm or just cat all the indices on Linux into memory we''ve",
  "tokens": [50620, 291, 458, 493, 293, 2614, 293, 293, 4561, 420, 445, 3857, 439,
  264, 43840, 322, 18734, 666, 4675, 321, 600, 51024], "temperature": 0.0, "avg_logprob":
  -0.11731377468314222, "compression_ratio": 1.6, "no_speech_prob": 0.0033323941752314568},
  {"id": 483, "seek": 254948, "start": 2562.68, "end": 2569.0, "text": " done that
  too that was like 10 years ago or so that was very strange feeling like why do I
  need to", "tokens": [51024, 1096, 300, 886, 300, 390, 411, 1266, 924, 2057, 420,
  370, 300, 390, 588, 5861, 2633, 411, 983, 360, 286, 643, 281, 51340], "temperature":
  0.0, "avg_logprob": -0.11731377468314222, "compression_ratio": 1.6, "no_speech_prob":
  0.0033323941752314568}, {"id": 484, "seek": 254948, "start": 2569.0, "end": 2576.04,
  "text": " mess with that level of detail it never actually paid off I think what
  pays off is a most", "tokens": [51340, 2082, 365, 300, 1496, 295, 2607, 309, 1128,
  767, 4835, 766, 286, 519, 437, 10604, 766, 307, 257, 881, 51692], "temperature":
  0.0, "avg_logprob": -0.11731377468314222, "compression_ratio": 1.6, "no_speech_prob":
  0.0033323941752314568}, {"id": 485, "seek": 257604, "start": 2576.44, "end": 2581.96,
  "text": " smart way to organize your index and how you read data backwards like
  essentially when you", "tokens": [50384, 4069, 636, 281, 13859, 428, 8186, 293,
  577, 291, 1401, 1412, 12204, 411, 4476, 562, 291, 50660], "temperature": 0.0, "avg_logprob":
  -0.12161791324615479, "compression_ratio": 1.6798245614035088, "no_speech_prob":
  0.0021350958850234747}, {"id": 486, "seek": 257604, "start": 2581.96, "end": 2589.24,
  "text": " users really only need fresh data first like on Twitter for example everyone
  is really after the", "tokens": [50660, 5022, 534, 787, 643, 4451, 1412, 700, 411,
  322, 5794, 337, 1365, 1518, 307, 534, 934, 264, 51024], "temperature": 0.0, "avg_logprob":
  -0.12161791324615479, "compression_ratio": 1.6798245614035088, "no_speech_prob":
  0.0021350958850234747}, {"id": 487, "seek": 257604, "start": 2589.24, "end": 2596.04,
  "text": " recent tweets and not some archive and that was very similar case for
  us but it''s very interesting", "tokens": [51024, 5162, 25671, 293, 406, 512, 23507,
  293, 300, 390, 588, 2531, 1389, 337, 505, 457, 309, 311, 588, 1880, 51364], "temperature":
  0.0, "avg_logprob": -0.12161791324615479, "compression_ratio": 1.6798245614035088,
  "no_speech_prob": 0.0021350958850234747}, {"id": 488, "seek": 257604, "start": 2596.04,
  "end": 2603.8, "text": " like you go into so much detail there to to make the database
  effectively like a living organism", "tokens": [51364, 411, 291, 352, 666, 370,
  709, 2607, 456, 281, 281, 652, 264, 8149, 8659, 411, 257, 2647, 24128, 51752], "temperature":
  0.0, "avg_logprob": -0.12161791324615479, "compression_ratio": 1.6798245614035088,
  "no_speech_prob": 0.0021350958850234747}, {"id": 489, "seek": 260380, "start": 2604.28,
  "end": 2610.44, "text": " adjusting to the usage but you also you also have multi-tenancy
  right so meaning that the same", "tokens": [50388, 23559, 281, 264, 14924, 457,
  291, 611, 291, 611, 362, 4825, 12, 1147, 6717, 558, 370, 3620, 300, 264, 912, 50696],
  "temperature": 0.0, "avg_logprob": -0.1595682236085455, "compression_ratio": 1.7464788732394365,
  "no_speech_prob": 0.004518670961260796}, {"id": 490, "seek": 260380, "start": 2611.2400000000002,
  "end": 2619.48, "text": " the same turbo buffer deployed across the data centers
  is going to be used by multiple companies", "tokens": [50736, 264, 912, 20902, 21762,
  17826, 2108, 264, 1412, 10898, 307, 516, 281, 312, 1143, 538, 3866, 3431, 51148],
  "temperature": 0.0, "avg_logprob": -0.1595682236085455, "compression_ratio": 1.7464788732394365,
  "no_speech_prob": 0.004518670961260796}, {"id": 491, "seek": 260380, "start": 2619.48,
  "end": 2625.0, "text": " at the same time unless they demand an isolation how do
  you think about that when they", "tokens": [51148, 412, 264, 912, 565, 5969, 436,
  4733, 364, 16001, 577, 360, 291, 519, 466, 300, 562, 436, 51424], "temperature":
  0.0, "avg_logprob": -0.1595682236085455, "compression_ratio": 1.7464788732394365,
  "no_speech_prob": 0.004518670961260796}, {"id": 492, "seek": 260380, "start": 2625.6400000000003,
  "end": 2631.96, "text": " use the same effectively in the same instance compute
  and index I''d love to go into the solar", "tokens": [51456, 764, 264, 912, 8659,
  294, 264, 912, 5197, 14722, 293, 8186, 286, 1116, 959, 281, 352, 666, 264, 7936,
  51772], "temperature": 0.0, "avg_logprob": -0.1595682236085455, "compression_ratio":
  1.7464788732394365, "no_speech_prob": 0.004518670961260796}, {"id": 493, "seek":
  263196, "start": 2631.96, "end": 2638.12, "text": " example for just one second
  before we go into multi-tenancy how slow were those queries because", "tokens":
  [50364, 1365, 337, 445, 472, 1150, 949, 321, 352, 666, 4825, 12, 1147, 6717, 577,
  2964, 645, 729, 24109, 570, 50672], "temperature": 0.0, "avg_logprob": -0.13707547268625034,
  "compression_ratio": 1.749090909090909, "no_speech_prob": 0.003875292604789138},
  {"id": 494, "seek": 263196, "start": 2638.12, "end": 2643.48, "text": " when you
  say it cold you mean that it''s not in memory when I say cold I mean that it''s
  on S3", "tokens": [50672, 562, 291, 584, 309, 3554, 291, 914, 300, 309, 311, 406,
  294, 4675, 562, 286, 584, 3554, 286, 914, 300, 309, 311, 322, 318, 18, 50940], "temperature":
  0.0, "avg_logprob": -0.13707547268625034, "compression_ratio": 1.749090909090909,
  "no_speech_prob": 0.003875292604789138}, {"id": 495, "seek": 263196, "start": 2643.48,
  "end": 2647.56, "text": " what kind of latency were you seeing that you had to do
  this work on it was very slow first of all", "tokens": [50940, 437, 733, 295, 27043,
  645, 291, 2577, 300, 291, 632, 281, 360, 341, 589, 322, 309, 390, 588, 2964, 700,
  295, 439, 51144], "temperature": 0.0, "avg_logprob": -0.13707547268625034, "compression_ratio":
  1.749090909090909, "no_speech_prob": 0.003875292604789138}, {"id": 496, "seek":
  263196, "start": 2648.68, "end": 2655.48, "text": " the it has to do also with the
  domain specificity you know the the queries were Boolean and very long", "tokens":
  [51200, 264, 309, 575, 281, 360, 611, 365, 264, 9274, 2685, 507, 291, 458, 264,
  264, 24109, 645, 23351, 28499, 293, 588, 938, 51540], "temperature": 0.0, "avg_logprob":
  -0.13707547268625034, "compression_ratio": 1.749090909090909, "no_speech_prob":
  0.003875292604789138}, {"id": 497, "seek": 263196, "start": 2655.48, "end": 2661.2400000000002,
  "text": " and so they they would take sometimes just a query itself would take a
  minute to execute on", "tokens": [51540, 293, 370, 436, 436, 576, 747, 2171, 445,
  257, 14581, 2564, 576, 747, 257, 3456, 281, 14483, 322, 51828], "temperature": 0.0,
  "avg_logprob": -0.13707547268625034, "compression_ratio": 1.749090909090909, "no_speech_prob":
  0.003875292604789138}, {"id": 498, "seek": 266124, "start": 2661.24, "end": 2668.4399999999996,
  "text": " now like a regional index design and that was like just super crazy right
  but it was also very", "tokens": [50364, 586, 411, 257, 10964, 8186, 1715, 293,
  300, 390, 411, 445, 1687, 3219, 558, 457, 309, 390, 611, 588, 50724], "temperature":
  0.0, "avg_logprob": -0.09166621600880343, "compression_ratio": 1.7625570776255708,
  "no_speech_prob": 0.0006432479713112116}, {"id": 499, "seek": 266124, "start": 2668.4399999999996,
  "end": 2674.4399999999996, "text": " accurate because it was like sentence level
  search and then I had to design a new system new", "tokens": [50724, 8559, 570,
  309, 390, 411, 8174, 1496, 3164, 293, 550, 286, 632, 281, 1715, 257, 777, 1185,
  777, 51024], "temperature": 0.0, "avg_logprob": -0.09166621600880343, "compression_ratio":
  1.7625570776255708, "no_speech_prob": 0.0006432479713112116}, {"id": 500, "seek":
  266124, "start": 2674.4399999999996, "end": 2682.04, "text": " architecture where
  we could retain the accuracy of that engine but not have to spend so much money",
  "tokens": [51024, 9482, 689, 321, 727, 18340, 264, 14170, 295, 300, 2848, 457, 406,
  362, 281, 3496, 370, 709, 1460, 51404], "temperature": 0.0, "avg_logprob": -0.09166621600880343,
  "compression_ratio": 1.7625570776255708, "no_speech_prob": 0.0006432479713112116},
  {"id": 501, "seek": 266124, "start": 2682.04, "end": 2688.9199999999996, "text":
  " on on on indexing individual sentences so we indexed one complete document right
  so I had to change", "tokens": [51404, 322, 322, 322, 8186, 278, 2609, 16579, 370,
  321, 8186, 292, 472, 3566, 4166, 558, 370, 286, 632, 281, 1319, 51748], "temperature":
  0.0, "avg_logprob": -0.09166621600880343, "compression_ratio": 1.7625570776255708,
  "no_speech_prob": 0.0006432479713112116}, {"id": 502, "seek": 268892, "start": 2688.92,
  "end": 2695.8, "text": " the algorithms slightly and so it went to sub-second it
  was still I think it''s still slow right but", "tokens": [50364, 264, 14642, 4748,
  293, 370, 309, 1437, 281, 1422, 12, 27375, 309, 390, 920, 286, 519, 309, 311, 920,
  2964, 558, 457, 50708], "temperature": 0.0, "avg_logprob": -0.17029610500540784,
  "compression_ratio": 1.7094017094017093, "no_speech_prob": 0.0012950095115229487},
  {"id": 503, "seek": 268892, "start": 2695.8, "end": 2702.12, "text": " it was much
  faster and and users started like like we could scale the company effectively after
  that", "tokens": [50708, 309, 390, 709, 4663, 293, 293, 5022, 1409, 411, 411, 321,
  727, 4373, 264, 2237, 8659, 934, 300, 51024], "temperature": 0.0, "avg_logprob":
  -0.17029610500540784, "compression_ratio": 1.7094017094017093, "no_speech_prob":
  0.0012950095115229487}, {"id": 504, "seek": 268892, "start": 2702.12, "end": 2710.12,
  "text": " right with one minute and 75% of infrastructure costs were like you know
  shaving off so but that''s", "tokens": [51024, 558, 365, 472, 3456, 293, 9562, 4,
  295, 6896, 5497, 645, 411, 291, 458, 36481, 766, 370, 457, 300, 311, 51424], "temperature":
  0.0, "avg_logprob": -0.17029610500540784, "compression_ratio": 1.7094017094017093,
  "no_speech_prob": 0.0012950095115229487}, {"id": 505, "seek": 268892, "start": 2710.92,
  "end": 2717.16, "text": " that''s that was part of the Lucine you know munging with
  the algorithm and changing how it scans the", "tokens": [51464, 300, 311, 300, 390,
  644, 295, 264, 9593, 533, 291, 458, 275, 1063, 278, 365, 264, 9284, 293, 4473, 577,
  309, 35116, 264, 51776], "temperature": 0.0, "avg_logprob": -0.17029610500540784,
  "compression_ratio": 1.7094017094017093, "no_speech_prob": 0.0012950095115229487},
  {"id": 506, "seek": 271716, "start": 2717.16, "end": 2723.96, "text": " document
  it had nothing to do with the level that you go into you know with turbo buffer
  you know like", "tokens": [50364, 4166, 309, 632, 1825, 281, 360, 365, 264, 1496,
  300, 291, 352, 666, 291, 458, 365, 20902, 21762, 291, 458, 411, 50704], "temperature":
  0.0, "avg_logprob": -0.2030700376664085, "compression_ratio": 1.819905213270142,
  "no_speech_prob": 0.001501852530054748}, {"id": 507, "seek": 271716, "start": 2725.16,
  "end": 2731.8799999999997, "text": " effectively controlling the whole the whole
  process there got it yeah I think the the point", "tokens": [50764, 8659, 14905,
  264, 1379, 264, 1379, 1399, 456, 658, 309, 1338, 286, 519, 264, 264, 935, 51100],
  "temperature": 0.0, "avg_logprob": -0.2030700376664085, "compression_ratio": 1.819905213270142,
  "no_speech_prob": 0.001501852530054748}, {"id": 508, "seek": 271716, "start": 2731.8799999999997,
  "end": 2738.52, "text": " I the the point there is that I think we do see that some
  customers are concerned with with", "tokens": [51100, 286, 264, 264, 935, 456, 307,
  300, 286, 519, 321, 360, 536, 300, 512, 4581, 366, 5922, 365, 365, 51432], "temperature":
  0.0, "avg_logprob": -0.2030700376664085, "compression_ratio": 1.819905213270142,
  "no_speech_prob": 0.001501852530054748}, {"id": 509, "seek": 271716, "start": 2738.52,
  "end": 2743.56, "text": " this cash because they''ve gone bit and by basically the
  the way that I would think about it is in", "tokens": [51432, 341, 6388, 570, 436,
  600, 2780, 857, 293, 538, 1936, 264, 264, 636, 300, 286, 576, 519, 466, 309, 307,
  294, 51684], "temperature": 0.0, "avg_logprob": -0.2030700376664085, "compression_ratio":
  1.819905213270142, "no_speech_prob": 0.001501852530054748}, {"id": 510, "seek":
  274356, "start": 2743.64, "end": 2747.96, "text": " in some of the traditional engines
  the way that they do IO if something is on disk it feels like", "tokens": [50368,
  294, 512, 295, 264, 5164, 12982, 264, 636, 300, 436, 360, 39839, 498, 746, 307,
  322, 12355, 309, 3417, 411, 50584], "temperature": 0.0, "avg_logprob": -0.09234489500522614,
  "compression_ratio": 1.9108527131782946, "no_speech_prob": 0.003323836950585246},
  {"id": 511, "seek": 274356, "start": 2747.96, "end": 2752.92, "text": " it''s bad
  like if it''s on disk it''s slow and it really has to be in memory and so you sort
  of have", "tokens": [50584, 309, 311, 1578, 411, 498, 309, 311, 322, 12355, 309,
  311, 2964, 293, 309, 534, 575, 281, 312, 294, 4675, 293, 370, 291, 1333, 295, 362,
  50832], "temperature": 0.0, "avg_logprob": -0.09234489500522614, "compression_ratio":
  1.9108527131782946, "no_speech_prob": 0.003323836950585246}, {"id": 512, "seek":
  274356, "start": 2752.92, "end": 2757.24, "text": " you know the pufferfish is either
  you know the pufferfish is sort of because when it''s fully inflated", "tokens":
  [50832, 291, 458, 264, 19613, 260, 11608, 307, 2139, 291, 458, 264, 19613, 260,
  11608, 307, 1333, 295, 570, 562, 309, 311, 4498, 9922, 770, 51048], "temperature":
  0.0, "avg_logprob": -0.09234489500522614, "compression_ratio": 1.9108527131782946,
  "no_speech_prob": 0.003323836950585246}, {"id": 513, "seek": 274356, "start": 2757.24,
  "end": 2762.6, "text": " it''s a DRAM right it''s a deflated it''s in s3 well it
  only had two settings right either it''s in", "tokens": [51048, 309, 311, 257, 12118,
  2865, 558, 309, 311, 257, 1060, 38539, 309, 311, 294, 262, 18, 731, 309, 787, 632,
  732, 6257, 558, 2139, 309, 311, 294, 51316], "temperature": 0.0, "avg_logprob":
  -0.09234489500522614, "compression_ratio": 1.9108527131782946, "no_speech_prob":
  0.003323836950585246}, {"id": 514, "seek": 274356, "start": 2762.6, "end": 2767.56,
  "text": " disk which is quite slow and frankly in some of the traditional storage
  engine I''ve seen the latency", "tokens": [51316, 12355, 597, 307, 1596, 2964, 293,
  11939, 294, 512, 295, 264, 5164, 6725, 2848, 286, 600, 1612, 264, 27043, 51564],
  "temperature": 0.0, "avg_logprob": -0.09234489500522614, "compression_ratio": 1.9108527131782946,
  "no_speech_prob": 0.003323836950585246}, {"id": 515, "seek": 276756, "start": 2767.56,
  "end": 2774.2, "text": " on disk being similar to our latency on s3 yeah and so
  then you have to load it into DRAM and what", "tokens": [50364, 322, 12355, 885,
  2531, 281, 527, 27043, 322, 262, 18, 1338, 293, 370, 550, 291, 362, 281, 3677, 309,
  666, 12118, 2865, 293, 437, 50696], "temperature": 0.0, "avg_logprob": -0.12839167045824457,
  "compression_ratio": 1.6666666666666667, "no_speech_prob": 0.0045700110495090485},
  {"id": 516, "seek": 276756, "start": 2774.2, "end": 2778.44, "text": " a lot of
  these traditional databases they have to do a full copy into DRAM they can''t just
  like zero", "tokens": [50696, 257, 688, 295, 613, 5164, 22380, 436, 362, 281, 360,
  257, 1577, 5055, 666, 12118, 2865, 436, 393, 380, 445, 411, 4018, 50908], "temperature":
  0.0, "avg_logprob": -0.12839167045824457, "compression_ratio": 1.6666666666666667,
  "no_speech_prob": 0.0045700110495090485}, {"id": 517, "seek": 276756, "start": 2778.44,
  "end": 2784.44, "text": " copy off of disk and in the disk are also quite slow these
  old network disks right the NVME disks", "tokens": [50908, 5055, 766, 295, 12355,
  293, 294, 264, 12355, 366, 611, 1596, 2964, 613, 1331, 3209, 41617, 558, 264, 46512,
  15454, 41617, 51208], "temperature": 0.0, "avg_logprob": -0.12839167045824457, "compression_ratio":
  1.6666666666666667, "no_speech_prob": 0.0045700110495090485}, {"id": 518, "seek":
  276756, "start": 2784.44, "end": 2793.32, "text": " are so fast right they are they
  can drive bandwidth that''s within you know a very low multiple of DRAM", "tokens":
  [51208, 366, 370, 2370, 558, 436, 366, 436, 393, 3332, 23647, 300, 311, 1951, 291,
  458, 257, 588, 2295, 3866, 295, 12118, 2865, 51652], "temperature": 0.0, "avg_logprob":
  -0.12839167045824457, "compression_ratio": 1.6666666666666667, "no_speech_prob":
  0.0045700110495090485}, {"id": 519, "seek": 279332, "start": 2793.32, "end": 2799.8,
  "text": " right tens of gigabytes per second but their cost is almost and two orders
  of magnitude lower", "tokens": [50364, 558, 10688, 295, 42741, 680, 1150, 457, 641,
  2063, 307, 1920, 293, 732, 9470, 295, 15668, 3126, 50688], "temperature": 0.0, "avg_logprob":
  -0.12304900727182064, "compression_ratio": 1.7178571428571427, "no_speech_prob":
  0.011262807995080948}, {"id": 520, "seek": 279332, "start": 2799.8, "end": 2804.6000000000004,
  "text": " so this completely changes the economics but you you can''t take advantage
  of these very easily you", "tokens": [50688, 370, 341, 2584, 2962, 264, 14564, 457,
  291, 291, 393, 380, 747, 5002, 295, 613, 588, 3612, 291, 50928], "temperature":
  0.0, "avg_logprob": -0.12304900727182064, "compression_ratio": 1.7178571428571427,
  "no_speech_prob": 0.011262807995080948}, {"id": 521, "seek": 279332, "start": 2804.6000000000004,
  "end": 2809.88, "text": " can''t just put as some software on it and just it''s
  going to be like 10 times faster than an original", "tokens": [50928, 393, 380,
  445, 829, 382, 512, 4722, 322, 309, 293, 445, 309, 311, 516, 281, 312, 411, 1266,
  1413, 4663, 813, 364, 3380, 51192], "temperature": 0.0, "avg_logprob": -0.12304900727182064,
  "compression_ratio": 1.7178571428571427, "no_speech_prob": 0.011262807995080948},
  {"id": 522, "seek": 279332, "start": 2809.88, "end": 2814.84, "text": " disk even
  if it''s fundamentally capable of it because what we found for example is that we",
  "tokens": [51192, 12355, 754, 498, 309, 311, 17879, 8189, 295, 309, 570, 437, 321,
  1352, 337, 1365, 307, 300, 321, 51440], "temperature": 0.0, "avg_logprob": -0.12304900727182064,
  "compression_ratio": 1.7178571428571427, "no_speech_prob": 0.011262807995080948},
  {"id": 523, "seek": 279332, "start": 2814.84, "end": 2819.2400000000002, "text":
  " had to remove the Linux page cache because the Linux page cache cannot keep up
  with these disks", "tokens": [51440, 632, 281, 4159, 264, 18734, 3028, 19459, 570,
  264, 18734, 3028, 19459, 2644, 1066, 493, 365, 613, 41617, 51660], "temperature":
  0.0, "avg_logprob": -0.12304900727182064, "compression_ratio": 1.7178571428571427,
  "no_speech_prob": 0.011262807995080948}, {"id": 524, "seek": 281924, "start": 2819.24,
  "end": 2823.0, "text": " so you have to do direct dial but when you do direct dial
  you don''t get coalescing you don''t get", "tokens": [50364, 370, 291, 362, 281,
  360, 2047, 5502, 457, 562, 291, 360, 2047, 5502, 291, 500, 380, 483, 598, 4229,
  2175, 291, 500, 380, 483, 50552], "temperature": 0.0, "avg_logprob": -0.1318685926240066,
  "compression_ratio": 1.8682170542635659, "no_speech_prob": 0.009973360225558281},
  {"id": 525, "seek": 281924, "start": 2823.0, "end": 2826.7599999999998, "text":
  " all these other things now you have to write your own IO driver right and so you
  just", "tokens": [50552, 439, 613, 661, 721, 586, 291, 362, 281, 2464, 428, 1065,
  39839, 6787, 558, 293, 370, 291, 445, 50740], "temperature": 0.0, "avg_logprob":
  -0.1318685926240066, "compression_ratio": 1.8682170542635659, "no_speech_prob":
  0.009973360225558281}, {"id": 526, "seek": 281924, "start": 2828.2799999999997,
  "end": 2833.0, "text": " databases have not been built to take advantage of it because
  they''re also like they''re not built", "tokens": [50816, 22380, 362, 406, 668,
  3094, 281, 747, 5002, 295, 309, 570, 436, 434, 611, 411, 436, 434, 406, 3094, 51052],
  "temperature": 0.0, "avg_logprob": -0.1318685926240066, "compression_ratio": 1.8682170542635659,
  "no_speech_prob": 0.009973360225558281}, {"id": 527, "seek": 281924, "start": 2833.0,
  "end": 2838.9199999999996, "text": " to try to do an IO depth like basically so
  many outside standing IO requests they can they can drive", "tokens": [51052, 281,
  853, 281, 360, 364, 39839, 7161, 411, 1936, 370, 867, 2380, 4877, 39839, 12475,
  436, 393, 436, 393, 3332, 51348], "temperature": 0.0, "avg_logprob": -0.1318685926240066,
  "compression_ratio": 1.8682170542635659, "no_speech_prob": 0.009973360225558281},
  {"id": 528, "seek": 281924, "start": 2838.9199999999996, "end": 2844.04, "text":
  " there''s a lot of throughput so there''s just a lot of barriers of entry there
  so what we find is that", "tokens": [51348, 456, 311, 257, 688, 295, 44629, 370,
  456, 311, 445, 257, 688, 295, 13565, 295, 8729, 456, 370, 437, 321, 915, 307, 300,
  51604], "temperature": 0.0, "avg_logprob": -0.1318685926240066, "compression_ratio":
  1.8682170542635659, "no_speech_prob": 0.009973360225558281}, {"id": 529, "seek":
  284404, "start": 2844.12, "end": 2849.0, "text": " when again speaking in generic
  terms here of like you know millions of vectors query that once", "tokens": [50368,
  562, 797, 4124, 294, 19577, 2115, 510, 295, 411, 291, 458, 6803, 295, 18875, 14581,
  300, 1564, 50612], "temperature": 0.0, "avg_logprob": -0.14663542362681606, "compression_ratio":
  1.8308823529411764, "no_speech_prob": 0.005453239660710096}, {"id": 530, "seek":
  284404, "start": 2849.64, "end": 2855.48, "text": " when something is in disk it''s
  maybe high tens of milliseconds mid you know 50 70 milliseconds when", "tokens":
  [50644, 562, 746, 307, 294, 12355, 309, 311, 1310, 1090, 10688, 295, 34184, 2062,
  291, 458, 2625, 5285, 34184, 562, 50936], "temperature": 0.0, "avg_logprob": -0.14663542362681606,
  "compression_ratio": 1.8308823529411764, "no_speech_prob": 0.005453239660710096},
  {"id": 531, "seek": 284404, "start": 2855.48, "end": 2860.84, "text": " it''s fully
  on disk maybe lower depending on the query the machinality whatever and when it''s
  in memory", "tokens": [50936, 309, 311, 4498, 322, 12355, 1310, 3126, 5413, 322,
  264, 14581, 264, 2246, 259, 1860, 2035, 293, 562, 309, 311, 294, 4675, 51204], "temperature":
  0.0, "avg_logprob": -0.14663542362681606, "compression_ratio": 1.8308823529411764,
  "no_speech_prob": 0.005453239660710096}, {"id": 532, "seek": 284404, "start": 2860.84,
  "end": 2865.24, "text": " it''s closer to 10 to 20 milliseconds right so it''s like
  these are not this is not bad like the user", "tokens": [51204, 309, 311, 4966,
  281, 1266, 281, 945, 34184, 558, 370, 309, 311, 411, 613, 366, 406, 341, 307, 406,
  1578, 411, 264, 4195, 51424], "temperature": 0.0, "avg_logprob": -0.14663542362681606,
  "compression_ratio": 1.8308823529411764, "no_speech_prob": 0.005453239660710096},
  {"id": 533, "seek": 284404, "start": 2865.24, "end": 2870.52, "text": " is barely
  going to notice it and but of course you''re going to get more throughput that way
  and then", "tokens": [51424, 307, 10268, 516, 281, 3449, 309, 293, 457, 295, 1164,
  291, 434, 516, 281, 483, 544, 44629, 300, 636, 293, 550, 51688], "temperature":
  0.0, "avg_logprob": -0.14663542362681606, "compression_ratio": 1.8308823529411764,
  "no_speech_prob": 0.005453239660710096}, {"id": 534, "seek": 287052, "start": 2870.52,
  "end": 2874.52, "text": " means it''s on s3 it''s maybe more like five to six hundred
  milliseconds it''s sort of user would", "tokens": [50364, 1355, 309, 311, 322, 262,
  18, 309, 311, 1310, 544, 411, 1732, 281, 2309, 3262, 34184, 309, 311, 1333, 295,
  4195, 576, 50564], "temperature": 0.0, "avg_logprob": -0.1387880037156798, "compression_ratio":
  1.8317757009345794, "no_speech_prob": 0.0010188273154199123}, {"id": 535, "seek":
  287052, "start": 2874.52, "end": 2880.36, "text": " notice but a lot of our customers
  like notion for example when you open the q and a dialog and", "tokens": [50564,
  3449, 457, 257, 688, 295, 527, 4581, 411, 10710, 337, 1365, 562, 291, 1269, 264,
  9505, 293, 257, 19308, 293, 50856], "temperature": 0.0, "avg_logprob": -0.1387880037156798,
  "compression_ratio": 1.8317757009345794, "no_speech_prob": 0.0010188273154199123},
  {"id": 536, "seek": 287052, "start": 2880.36, "end": 2885.24, "text": " these different
  dialogues that will query turbo puffer they will send a request to tell turbo puffer",
  "tokens": [50856, 613, 819, 45551, 300, 486, 14581, 20902, 19613, 260, 436, 486,
  2845, 257, 5308, 281, 980, 20902, 19613, 260, 51100], "temperature": 0.0, "avg_logprob":
  -0.1387880037156798, "compression_ratio": 1.8317757009345794, "no_speech_prob":
  0.0010188273154199123}, {"id": 537, "seek": 287052, "start": 2885.24, "end": 2889.72,
  "text": " hey can you start warming up the cash here in a way that makes sense and
  by cash we just mean putting", "tokens": [51100, 4177, 393, 291, 722, 17983, 493,
  264, 6388, 510, 294, 257, 636, 300, 1669, 2020, 293, 538, 6388, 321, 445, 914, 3372,
  51324], "temperature": 0.0, "avg_logprob": -0.1387880037156798, "compression_ratio":
  1.8317757009345794, "no_speech_prob": 0.0010188273154199123}, {"id": 538, "seek":
  287052, "start": 2889.72, "end": 2894.28, "text": " it into disk and starting with
  sort of the upper layers of the an index and other things to reduce", "tokens":
  [51324, 309, 666, 12355, 293, 2891, 365, 1333, 295, 264, 6597, 7914, 295, 264, 364,
  8186, 293, 661, 721, 281, 5407, 51552], "temperature": 0.0, "avg_logprob": -0.1387880037156798,
  "compression_ratio": 1.8317757009345794, "no_speech_prob": 0.0010188273154199123},
  {"id": 539, "seek": 287052, "start": 2894.28, "end": 2899.48, "text": " the time
  as much as possible so there''s a lot of things that can be done here that are very
  very", "tokens": [51552, 264, 565, 382, 709, 382, 1944, 370, 456, 311, 257, 688,
  295, 721, 300, 393, 312, 1096, 510, 300, 366, 588, 588, 51812], "temperature": 0.0,
  "avg_logprob": -0.1387880037156798, "compression_ratio": 1.8317757009345794, "no_speech_prob":
  0.0010188273154199123}, {"id": 540, "seek": 289948, "start": 2899.48, "end": 2907.8,
  "text": " simple that means that the there''s there''s there''s barely a trade-off
  yeah but we let''s go", "tokens": [50364, 2199, 300, 1355, 300, 264, 456, 311, 456,
  311, 456, 311, 10268, 257, 4923, 12, 4506, 1338, 457, 321, 718, 311, 352, 50780],
  "temperature": 0.0, "avg_logprob": -0.17048031268733563, "compression_ratio": 1.933673469387755,
  "no_speech_prob": 0.0011517814127728343}, {"id": 541, "seek": 289948, "start": 2907.8,
  "end": 2913.2400000000002, "text": " back into multi-tenancy unless you had a follow
  up let''s do that yeah let''s do that like how do you", "tokens": [50780, 646, 666,
  4825, 12, 1147, 6717, 5969, 291, 632, 257, 1524, 493, 718, 311, 360, 300, 1338,
  718, 311, 360, 300, 411, 577, 360, 291, 51052], "temperature": 0.0, "avg_logprob":
  -0.17048031268733563, "compression_ratio": 1.933673469387755, "no_speech_prob":
  0.0011517814127728343}, {"id": 542, "seek": 289948, "start": 2913.2400000000002,
  "end": 2918.92, "text": " use a multi-tenancy part so so turbo puffer can run in
  three different ways it can run yeah", "tokens": [51052, 764, 257, 4825, 12, 1147,
  6717, 644, 370, 370, 20902, 19613, 260, 393, 1190, 294, 1045, 819, 2098, 309, 393,
  1190, 1338, 51336], "temperature": 0.0, "avg_logprob": -0.17048031268733563, "compression_ratio":
  1.933673469387755, "no_speech_prob": 0.0011517814127728343}, {"id": 543, "seek":
  289948, "start": 2918.92, "end": 2924.76, "text": " multi-tenancy clusters that''s
  what I mean that''s what cursor does that''s what that''s what linear", "tokens":
  [51336, 4825, 12, 1147, 6717, 23313, 300, 311, 437, 286, 914, 300, 311, 437, 28169,
  775, 300, 311, 437, 300, 311, 437, 8213, 51628], "temperature": 0.0, "avg_logprob":
  -0.17048031268733563, "compression_ratio": 1.933673469387755, "no_speech_prob":
  0.0011517814127728343}, {"id": 544, "seek": 292476, "start": 2924.76, "end": 2932.5200000000004,
  "text": " does and many of our customers so in multi-tenancy you share you share
  the compute we can do this", "tokens": [50364, 775, 293, 867, 295, 527, 4581, 370,
  294, 4825, 12, 1147, 6717, 291, 2073, 291, 2073, 264, 14722, 321, 393, 360, 341,
  50752], "temperature": 0.0, "avg_logprob": -0.1391412570912351, "compression_ratio":
  1.8173076923076923, "no_speech_prob": 0.0017693896079435945}, {"id": 545, "seek":
  292476, "start": 2932.5200000000004, "end": 2936.76, "text": " so cheaply right
  because we can share the caching can share the we can share all of this", "tokens":
  [50752, 370, 7084, 356, 558, 570, 321, 393, 2073, 264, 269, 2834, 393, 2073, 264,
  321, 393, 2073, 439, 295, 341, 50964], "temperature": 0.0, "avg_logprob": -0.1391412570912351,
  "compression_ratio": 1.8173076923076923, "no_speech_prob": 0.0017693896079435945},
  {"id": 546, "seek": 292476, "start": 2936.76, "end": 2942.76, "text": " infrastructure
  it''s very easy for us to run this way so that''s the default mode the cash is of",
  "tokens": [50964, 6896, 309, 311, 588, 1858, 337, 505, 281, 1190, 341, 636, 370,
  300, 311, 264, 7576, 4391, 264, 6388, 307, 295, 51264], "temperature": 0.0, "avg_logprob":
  -0.1391412570912351, "compression_ratio": 1.8173076923076923, "no_speech_prob":
  0.0017693896079435945}, {"id": 547, "seek": 292476, "start": 2942.76, "end": 2950.2000000000003,
  "text": " course segregated off in in in in in in different ways but is also like
  shared in ways where you", "tokens": [51264, 1164, 47370, 766, 294, 294, 294, 294,
  294, 294, 819, 2098, 457, 307, 611, 411, 5507, 294, 2098, 689, 291, 51636], "temperature":
  0.0, "avg_logprob": -0.1391412570912351, "compression_ratio": 1.8173076923076923,
  "no_speech_prob": 0.0017693896079435945}, {"id": 548, "seek": 295020, "start": 2950.2,
  "end": 2957.16, "text": " have a big burst the traffic rate you get more of the
  cash than others so that''s what we so it''s", "tokens": [50364, 362, 257, 955,
  12712, 264, 6419, 3314, 291, 483, 544, 295, 264, 6388, 813, 2357, 370, 300, 311,
  437, 321, 370, 309, 311, 50712], "temperature": 0.0, "avg_logprob": -0.07950835704803466,
  "compression_ratio": 1.7333333333333334, "no_speech_prob": 0.0007069749990478158},
  {"id": 549, "seek": 295020, "start": 2957.16, "end": 2961.3999999999996, "text":
  " a very great way of running multi-tenancy the other thing we do for multi-tenancy
  to keep it very", "tokens": [50712, 257, 588, 869, 636, 295, 2614, 4825, 12, 1147,
  6717, 264, 661, 551, 321, 360, 337, 4825, 12, 1147, 6717, 281, 1066, 309, 588, 50924],
  "temperature": 0.0, "avg_logprob": -0.07950835704803466, "compression_ratio": 1.7333333333333334,
  "no_speech_prob": 0.0007069749990478158}, {"id": 550, "seek": 295020, "start": 2961.3999999999996,
  "end": 2967.24, "text": " secure is that because all the data at rest is in the
  bucket you can pass an encryption key to", "tokens": [50924, 7144, 307, 300, 570,
  439, 264, 1412, 412, 1472, 307, 294, 264, 13058, 291, 393, 1320, 364, 29575, 2141,
  281, 51216], "temperature": 0.0, "avg_logprob": -0.07950835704803466, "compression_ratio":
  1.7333333333333334, "no_speech_prob": 0.0007069749990478158}, {"id": 551, "seek":
  295020, "start": 2967.24, "end": 2973.7999999999997, "text": " turbo puffer that
  we don''t have access to unless it''s audit logged on your side where we can encrypt",
  "tokens": [51216, 20902, 19613, 260, 300, 321, 500, 380, 362, 2105, 281, 5969, 309,
  311, 17748, 27231, 322, 428, 1252, 689, 321, 393, 17972, 662, 51544], "temperature":
  0.0, "avg_logprob": -0.07950835704803466, "compression_ratio": 1.7333333333333334,
  "no_speech_prob": 0.0007069749990478158}, {"id": 552, "seek": 297380, "start": 2973.8,
  "end": 2980.76, "text": " and decrypt the object which is logically and from a security
  point standpoint equivalent to you", "tokens": [50364, 293, 979, 627, 662, 264,
  2657, 597, 307, 38887, 293, 490, 257, 3825, 935, 15827, 10344, 281, 291, 50712],
  "temperature": 0.0, "avg_logprob": -0.08792360988231974, "compression_ratio": 1.825925925925926,
  "no_speech_prob": 0.0037865922786295414}, {"id": 553, "seek": 297380, "start": 2980.76,
  "end": 2987.0800000000004, "text": " having all the data in your bucket so this
  is a very nice primitive that for example linear it takes", "tokens": [50712, 1419,
  439, 264, 1412, 294, 428, 13058, 370, 341, 307, 257, 588, 1481, 28540, 300, 337,
  1365, 8213, 309, 2516, 51028], "temperature": 0.0, "avg_logprob": -0.08792360988231974,
  "compression_ratio": 1.825925925925926, "no_speech_prob": 0.0037865922786295414},
  {"id": 554, "seek": 297380, "start": 2987.0800000000004, "end": 2991.32, "text":
  " advantage of because they have full control over their data they can see when
  turbo puffer is", "tokens": [51028, 5002, 295, 570, 436, 362, 1577, 1969, 670, 641,
  1412, 436, 393, 536, 562, 20902, 19613, 260, 307, 51240], "temperature": 0.0, "avg_logprob":
  -0.08792360988231974, "compression_ratio": 1.825925925925926, "no_speech_prob":
  0.0037865922786295414}, {"id": 555, "seek": 297380, "start": 2991.32, "end": 2996.76,
  "text": " accessing it they can shut it down at any point in time and they can even
  pass that on to any other", "tokens": [51240, 26440, 309, 436, 393, 5309, 309, 760,
  412, 604, 935, 294, 565, 293, 436, 393, 754, 1320, 300, 322, 281, 604, 661, 51512],
  "temperature": 0.0, "avg_logprob": -0.08792360988231974, "compression_ratio": 1.825925925925926,
  "no_speech_prob": 0.0037865922786295414}, {"id": 556, "seek": 297380, "start": 2996.76,
  "end": 3002.6000000000004, "text": " customers where turbo puffer can encrypt data
  for linear customers on behalf of the customer with the", "tokens": [51512, 4581,
  689, 20902, 19613, 260, 393, 17972, 662, 1412, 337, 8213, 4581, 322, 9490, 295,
  264, 5474, 365, 264, 51804], "temperature": 0.0, "avg_logprob": -0.08792360988231974,
  "compression_ratio": 1.825925925925926, "no_speech_prob": 0.0037865922786295414},
  {"id": 557, "seek": 300260, "start": 3002.6, "end": 3008.6, "text": " customer''s
  key it this is like really really I think groundbreaking and underrated in this",
  "tokens": [50364, 5474, 311, 2141, 309, 341, 307, 411, 534, 534, 286, 519, 42491,
  293, 833, 5468, 294, 341, 50664], "temperature": 0.0, "avg_logprob": -0.1583266558947864,
  "compression_ratio": 1.7183098591549295, "no_speech_prob": 0.0015153922140598297},
  {"id": 558, "seek": 300260, "start": 3008.6, "end": 3012.68, "text": " architecture
  you can of course do single tenancy with turbo puffer as well with the computers
  only", "tokens": [50664, 9482, 291, 393, 295, 1164, 360, 2167, 2064, 6717, 365,
  20902, 19613, 260, 382, 731, 365, 264, 10807, 787, 50868], "temperature": 0.0, "avg_logprob":
  -0.1583266558947864, "compression_ratio": 1.7183098591549295, "no_speech_prob":
  0.0015153922140598297}, {"id": 559, "seek": 300260, "start": 3012.68, "end": 3017.56,
  "text": " for you you can do b y o c where we run to recover inside of your cloud
  in a way that''s like very", "tokens": [50868, 337, 291, 291, 393, 360, 272, 288,
  277, 269, 689, 321, 1190, 281, 8114, 1854, 295, 428, 4588, 294, 257, 636, 300, 311,
  411, 588, 51112], "temperature": 0.0, "avg_logprob": -0.1583266558947864, "compression_ratio":
  1.7183098591549295, "no_speech_prob": 0.0015153922140598297}, {"id": 560, "seek":
  300260, "start": 3017.56, "end": 3023.48, "text": " compliant we can never see customer
  data but we find it in multi-tenancy with the encryption which", "tokens": [51112,
  36248, 321, 393, 1128, 536, 5474, 1412, 457, 321, 915, 309, 294, 4825, 12, 1147,
  6717, 365, 264, 29575, 597, 51408], "temperature": 0.0, "avg_logprob": -0.1583266558947864,
  "compression_ratio": 1.7183098591549295, "no_speech_prob": 0.0015153922140598297},
  {"id": 561, "seek": 300260, "start": 3023.48, "end": 3028.2799999999997, "text":
  " can be done per namespities satisfies the security requirements of even some of
  the biggest companies", "tokens": [51408, 393, 312, 1096, 680, 5288, 79, 1088, 44271,
  264, 3825, 7728, 295, 754, 512, 295, 264, 3880, 3431, 51648], "temperature": 0.0,
  "avg_logprob": -0.1583266558947864, "compression_ratio": 1.7183098591549295, "no_speech_prob":
  0.0015153922140598297}, {"id": 562, "seek": 302828, "start": 3028.28, "end": 3034.76,
  "text": " in the world yeah that sounds awesome I also wanted to pick one topic
  which usually used to I", "tokens": [50364, 294, 264, 1002, 1338, 300, 3263, 3476,
  286, 611, 1415, 281, 1888, 472, 4829, 597, 2673, 1143, 281, 286, 50688], "temperature":
  0.0, "avg_logprob": -0.16269441654807643, "compression_ratio": 1.5815217391304348,
  "no_speech_prob": 0.01626240462064743}, {"id": 563, "seek": 302828, "start": 3034.76,
  "end": 3042.2000000000003, "text": " don''t know if any more I don''t see that as
  much pick up a lot of flame discussions what is your", "tokens": [50688, 500, 380,
  458, 498, 604, 544, 286, 500, 380, 536, 300, 382, 709, 1888, 493, 257, 688, 295,
  13287, 11088, 437, 307, 428, 51060], "temperature": 0.0, "avg_logprob": -0.16269441654807643,
  "compression_ratio": 1.5815217391304348, "no_speech_prob": 0.01626240462064743},
  {"id": 564, "seek": 302828, "start": 3042.2000000000003, "end": 3051.4, "text":
  " recall at n and when I go to the docs of turbo puffer it says recall at n is 100%
  recall at 10 excuse", "tokens": [51060, 9901, 412, 297, 293, 562, 286, 352, 281,
  264, 45623, 295, 20902, 19613, 260, 309, 1619, 9901, 412, 297, 307, 2319, 4, 9901,
  412, 1266, 8960, 51520], "temperature": 0.0, "avg_logprob": -0.16269441654807643,
  "compression_ratio": 1.5815217391304348, "no_speech_prob": 0.01626240462064743},
  {"id": 565, "seek": 305140, "start": 3051.56, "end": 3059.7200000000003, "text":
  " me but vector search bar so does that not 100% we said 9200 right no I think it
  says what wait wait wait", "tokens": [50372, 385, 457, 8062, 3164, 2159, 370, 775,
  300, 406, 2319, 4, 321, 848, 1722, 7629, 558, 572, 286, 519, 309, 1619, 437, 1699,
  1699, 1699, 50780], "temperature": 0.0, "avg_logprob": -0.17847001211983818, "compression_ratio":
  1.747787610619469, "no_speech_prob": 0.03225192800164223}, {"id": 566, "seek": 305140,
  "start": 3060.36, "end": 3067.88, "text": " I''ll need to what was the page where
  you do that oh here the limits oh I see observed in production", "tokens": [50812,
  286, 603, 643, 281, 437, 390, 264, 3028, 689, 291, 360, 300, 1954, 510, 264, 10406,
  1954, 286, 536, 13095, 294, 4265, 51188], "temperature": 0.0, "avg_logprob": -0.17847001211983818,
  "compression_ratio": 1.747787610619469, "no_speech_prob": 0.03225192800164223},
  {"id": 567, "seek": 305140, "start": 3067.88, "end": 3072.36, "text": " yeah it
  should say up to 100% that''s a bug in the docs that I shipped last night I''m gonna
  I''m", "tokens": [51188, 1338, 309, 820, 584, 493, 281, 2319, 4, 300, 311, 257,
  7426, 294, 264, 45623, 300, 286, 25312, 1036, 1818, 286, 478, 799, 286, 478, 51412],
  "temperature": 0.0, "avg_logprob": -0.17847001211983818, "compression_ratio": 1.747787610619469,
  "no_speech_prob": 0.03225192800164223}, {"id": 568, "seek": 305140, "start": 3072.36,
  "end": 3078.6800000000003, "text": " gonna fix that after this awesome but what
  it says in the in the limits is 90 to 100% but let''s", "tokens": [51412, 799, 3191,
  300, 934, 341, 3476, 457, 437, 309, 1619, 294, 264, 294, 264, 10406, 307, 4289,
  281, 2319, 4, 457, 718, 311, 51728], "temperature": 0.0, "avg_logprob": -0.17847001211983818,
  "compression_ratio": 1.747787610619469, "no_speech_prob": 0.03225192800164223},
  {"id": 569, "seek": 307868, "start": 3078.68, "end": 3085.48, "text": " talk about
  recall I''d love to get into recall so I think recall is incredibly important it''s
  the", "tokens": [50364, 751, 466, 9901, 286, 1116, 959, 281, 483, 666, 9901, 370,
  286, 519, 9901, 307, 6252, 1021, 309, 311, 264, 50704], "temperature": 0.0, "avg_logprob":
  -0.11043286727646649, "compression_ratio": 2.0625, "no_speech_prob": 0.0017049049492925406},
  {"id": 570, "seek": 307868, "start": 3085.48, "end": 3090.2799999999997, "text":
  " equivalent of your database you have to trust your database to do it in the same
  way that you have", "tokens": [50704, 10344, 295, 428, 8149, 291, 362, 281, 3361,
  428, 8149, 281, 360, 309, 294, 264, 912, 636, 300, 291, 362, 50944], "temperature":
  0.0, "avg_logprob": -0.11043286727646649, "compression_ratio": 2.0625, "no_speech_prob":
  0.0017049049492925406}, {"id": 571, "seek": 307868, "start": 3090.2799999999997,
  "end": 3095.3199999999997, "text": " to trust your database do f sync and you have
  to trust your database that when we say that hey we", "tokens": [50944, 281, 3361,
  428, 8149, 360, 283, 20271, 293, 291, 362, 281, 3361, 428, 8149, 300, 562, 321,
  584, 300, 4177, 321, 51196], "temperature": 0.0, "avg_logprob": -0.11043286727646649,
  "compression_ratio": 2.0625, "no_speech_prob": 0.0017049049492925406}, {"id": 572,
  "seek": 307868, "start": 3095.3199999999997, "end": 3101.8799999999997, "text":
  " don''t return a success to you unless it''s committed to s3 you have to trust
  that recall is similar right", "tokens": [51196, 500, 380, 2736, 257, 2245, 281,
  291, 5969, 309, 311, 7784, 281, 262, 18, 291, 362, 281, 3361, 300, 9901, 307, 2531,
  558, 51524], "temperature": 0.0, "avg_logprob": -0.11043286727646649, "compression_ratio":
  2.0625, "no_speech_prob": 0.0017049049492925406}, {"id": 573, "seek": 307868, "start":
  3101.8799999999997, "end": 3108.04, "text": " if you are working on search and you''re
  working on connecting data to llem''s then you don''t want", "tokens": [51524, 498,
  291, 366, 1364, 322, 3164, 293, 291, 434, 1364, 322, 11015, 1412, 281, 287, 10386,
  311, 550, 291, 500, 380, 528, 51832], "temperature": 0.0, "avg_logprob": -0.11043286727646649,
  "compression_ratio": 2.0625, "no_speech_prob": 0.0017049049492925406}, {"id": 574,
  "seek": 310804, "start": 3108.04, "end": 3113.8, "text": " to worry in your e-vails
  on whether your vector database is giving you low recall it''s actually a very",
  "tokens": [50364, 281, 3292, 294, 428, 308, 12, 85, 6227, 322, 1968, 428, 8062,
  8149, 307, 2902, 291, 2295, 9901, 309, 311, 767, 257, 588, 50652], "temperature":
  0.0, "avg_logprob": -0.10244310819185697, "compression_ratio": 1.8009259259259258,
  "no_speech_prob": 0.0007448425167240202}, {"id": 575, "seek": 310804, "start": 3113.8,
  "end": 3117.96, "text": " sophisticated problem to evaluate whether this is the
  cause so you have to trust your vendor", "tokens": [50652, 16950, 1154, 281, 13059,
  1968, 341, 307, 264, 3082, 370, 291, 362, 281, 3361, 428, 24321, 50860], "temperature":
  0.0, "avg_logprob": -0.10244310819185697, "compression_ratio": 1.8009259259259258,
  "no_speech_prob": 0.0007448425167240202}, {"id": 576, "seek": 310804, "start": 3119.48,
  "end": 3125.88, "text": " this is an underrated problem and I love that you''re
  asking about it and very few people ask about", "tokens": [50936, 341, 307, 364,
  833, 5468, 1154, 293, 286, 959, 300, 291, 434, 3365, 466, 309, 293, 588, 1326, 561,
  1029, 466, 51256], "temperature": 0.0, "avg_logprob": -0.10244310819185697, "compression_ratio":
  1.8009259259259258, "no_speech_prob": 0.0007448425167240202}, {"id": 577, "seek":
  310804, "start": 3125.88, "end": 3130.68, "text": " it unless they''re quite sophisticated
  so let''s go into it let''s go into a long answer here for", "tokens": [51256, 309,
  5969, 436, 434, 1596, 16950, 370, 718, 311, 352, 666, 309, 718, 311, 352, 666, 257,
  938, 1867, 510, 337, 51496], "temperature": 0.0, "avg_logprob": -0.10244310819185697,
  "compression_ratio": 1.8009259259259258, "no_speech_prob": 0.0007448425167240202},
  {"id": 578, "seek": 313068, "start": 3130.8399999999997, "end": 3137.72, "text":
  " your audience because I think this is paramount most databases that have a vector
  index are", "tokens": [50372, 428, 4034, 570, 286, 519, 341, 307, 6220, 792, 881,
  22380, 300, 362, 257, 8062, 8186, 366, 50716], "temperature": 0.0, "avg_logprob":
  -0.14194954958829012, "compression_ratio": 1.686832740213523, "no_speech_prob":
  0.00752654392272234}, {"id": 579, "seek": 313068, "start": 3139.08, "end": 3145.3999999999996,
  "text": " trained on or not trained on but they''re benchmarked against for these
  different A&N open", "tokens": [50784, 8895, 322, 420, 406, 8895, 322, 457, 436,
  434, 18927, 292, 1970, 337, 613, 819, 316, 5, 45, 1269, 51100], "temperature": 0.0,
  "avg_logprob": -0.14194954958829012, "compression_ratio": 1.686832740213523, "no_speech_prob":
  0.00752654392272234}, {"id": 580, "seek": 313068, "start": 3145.3999999999996, "end":
  3150.68, "text": " source projects so there''s sift and others problem with these
  data is that they do not represent what", "tokens": [51100, 4009, 4455, 370, 456,
  311, 262, 2008, 293, 2357, 1154, 365, 613, 1412, 307, 300, 436, 360, 406, 2906,
  437, 51364], "temperature": 0.0, "avg_logprob": -0.14194954958829012, "compression_ratio":
  1.686832740213523, "no_speech_prob": 0.00752654392272234}, {"id": 581, "seek": 313068,
  "start": 3150.68, "end": 3155.24, "text": " we''ve seen in the real world a lot
  of them are very low dimensionality like when we do benchmarking", "tokens": [51364,
  321, 600, 1612, 294, 264, 957, 1002, 257, 688, 295, 552, 366, 588, 2295, 10139,
  1860, 411, 562, 321, 360, 18927, 278, 51592], "temperature": 0.0, "avg_logprob":
  -0.14194954958829012, "compression_ratio": 1.686832740213523, "no_speech_prob":
  0.00752654392272234}, {"id": 582, "seek": 313068, "start": 3155.24, "end": 3159.3199999999997,
  "text": " on a billion that we''re working on right now the biggest data sets we
  can find are like 64", "tokens": [51592, 322, 257, 5218, 300, 321, 434, 1364, 322,
  558, 586, 264, 3880, 1412, 6352, 321, 393, 915, 366, 411, 12145, 51796], "temperature":
  0.0, "avg_logprob": -0.14194954958829012, "compression_ratio": 1.686832740213523,
  "no_speech_prob": 0.00752654392272234}, {"id": 583, "seek": 315932, "start": 3159.32,
  "end": 3164.28, "text": " dimensions this is not what people are doing in production
  they''re doing at least 512 often", "tokens": [50364, 12819, 341, 307, 406, 437,
  561, 366, 884, 294, 4265, 436, 434, 884, 412, 1935, 1025, 4762, 2049, 50612], "temperature":
  0.0, "avg_logprob": -0.1559716510772705, "compression_ratio": 1.83206106870229,
  "no_speech_prob": 0.0037499640602618456}, {"id": 584, "seek": 315932, "start": 3165.32,
  "end": 3170.92, "text": " generally I''d say the average is around 768 dimensions
  these are not representative data sets", "tokens": [50664, 5101, 286, 1116, 584,
  264, 4274, 307, 926, 24733, 23, 12819, 613, 366, 406, 12424, 1412, 6352, 50944],
  "temperature": 0.0, "avg_logprob": -0.1559716510772705, "compression_ratio": 1.83206106870229,
  "no_speech_prob": 0.0037499640602618456}, {"id": 585, "seek": 315932, "start": 3170.92,
  "end": 3175.1600000000003, "text": " and the distributions in the academic benchmarks
  are also completely different for what we see in", "tokens": [50944, 293, 264, 37870,
  294, 264, 7778, 43751, 366, 611, 2584, 819, 337, 437, 321, 536, 294, 51156], "temperature":
  0.0, "avg_logprob": -0.1559716510772705, "compression_ratio": 1.83206106870229,
  "no_speech_prob": 0.0037499640602618456}, {"id": 586, "seek": 315932, "start": 3175.1600000000003,
  "end": 3181.56, "text": " real data sets right in real data sets we see millions
  of copy of duplicates right we see filtering", "tokens": [51156, 957, 1412, 6352,
  558, 294, 957, 1412, 6352, 321, 536, 6803, 295, 5055, 295, 17154, 1024, 558, 321,
  536, 30822, 51476], "temperature": 0.0, "avg_logprob": -0.1559716510772705, "compression_ratio":
  1.83206106870229, "no_speech_prob": 0.0037499640602618456}, {"id": 587, "seek":
  315932, "start": 3181.56, "end": 3186.52, "text": " all these chaotic environments
  that do not present themselves in the academic thench works so if", "tokens": [51476,
  439, 613, 27013, 12388, 300, 360, 406, 1974, 2969, 294, 264, 7778, 550, 339, 1985,
  370, 498, 51724], "temperature": 0.0, "avg_logprob": -0.1559716510772705, "compression_ratio":
  1.83206106870229, "no_speech_prob": 0.0037499640602618456}, {"id": 588, "seek":
  318652, "start": 3187.16, "end": 3192.28, "text": " if you''re using a vector index
  that''s only been tested on academic benchmarks it''s it''s I mean", "tokens": [50396,
  498, 291, 434, 1228, 257, 8062, 8186, 300, 311, 787, 668, 8246, 322, 7778, 43751,
  309, 311, 309, 311, 286, 914, 50652], "temperature": 0.0, "avg_logprob": -0.22574036862669872,
  "compression_ratio": 1.9146341463414633, "no_speech_prob": 0.006672090385109186},
  {"id": 589, "seek": 318652, "start": 3192.28, "end": 3196.04, "text": " it''s like
  the LLMs right it''s like you don''t you don''t really trust it just based on",
  "tokens": [50652, 309, 311, 411, 264, 441, 43, 26386, 558, 309, 311, 411, 291, 500,
  380, 291, 500, 380, 534, 3361, 309, 445, 2361, 322, 50840], "temperature": 0.0,
  "avg_logprob": -0.22574036862669872, "compression_ratio": 1.9146341463414633, "no_speech_prob":
  0.006672090385109186}, {"id": 590, "seek": 318652, "start": 3196.04, "end": 3201.32,
  "text": " discording it''s sort of you it''s all the vibes right it''s all the qualitative
  thing right outside", "tokens": [50840, 32989, 278, 309, 311, 1333, 295, 291, 309,
  311, 439, 264, 27636, 558, 309, 311, 439, 264, 31312, 551, 558, 2380, 51104], "temperature":
  0.0, "avg_logprob": -0.22574036862669872, "compression_ratio": 1.9146341463414633,
  "no_speech_prob": 0.006672090385109186}, {"id": 591, "seek": 318652, "start": 3201.32,
  "end": 3205.0, "text": " the benchmark was that everyone was dreaming on them that
  it will work for your domain right like", "tokens": [51104, 264, 18927, 390, 300,
  1518, 390, 21475, 322, 552, 300, 309, 486, 589, 337, 428, 9274, 558, 411, 51288],
  "temperature": 0.0, "avg_logprob": -0.22574036862669872, "compression_ratio": 1.9146341463414633,
  "no_speech_prob": 0.006672090385109186}, {"id": 592, "seek": 318652, "start": 3205.0,
  "end": 3211.56, "text": " the LLM that''s right like early on very very early on
  in in in interval puffer''s history in the", "tokens": [51288, 264, 441, 43, 44,
  300, 311, 558, 411, 2440, 322, 588, 588, 2440, 322, 294, 294, 294, 15035, 19613,
  260, 311, 2503, 294, 264, 51616], "temperature": 0.0, "avg_logprob": -0.22574036862669872,
  "compression_ratio": 1.9146341463414633, "no_speech_prob": 0.006672090385109186},
  {"id": 593, "seek": 321156, "start": 3211.56, "end": 3216.84, "text": " first month
  I was mainly iterating against the SIFT data set right just like 128 dimensional",
  "tokens": [50364, 700, 1618, 286, 390, 8704, 17138, 990, 1970, 264, 318, 12775,
  51, 1412, 992, 558, 445, 411, 29810, 18795, 50628], "temperature": 0.0, "avg_logprob":
  -0.17388935226330654, "compression_ratio": 1.8158730158730159, "no_speech_prob":
  0.0015733742620795965}, {"id": 594, "seek": 321156, "start": 3216.84, "end": 3219.88,
  "text": " data set I didn''t know anything about an end at the time so it''s like
  okay this is pretty good", "tokens": [50628, 1412, 992, 286, 994, 380, 458, 1340,
  466, 364, 917, 412, 264, 565, 370, 309, 311, 411, 1392, 341, 307, 1238, 665, 50780],
  "temperature": 0.0, "avg_logprob": -0.17388935226330654, "compression_ratio": 1.8158730158730159,
  "no_speech_prob": 0.0015733742620795965}, {"id": 595, "seek": 321156, "start": 3219.88,
  "end": 3224.6, "text": " we can tune some risks on this and then I can do go wider
  but I have the feedback loop and the", "tokens": [50780, 321, 393, 10864, 512, 10888,
  322, 341, 293, 550, 286, 393, 360, 352, 11842, 457, 286, 362, 264, 5824, 6367, 293,
  264, 51016], "temperature": 0.0, "avg_logprob": -0.17388935226330654, "compression_ratio":
  1.8158730158730159, "no_speech_prob": 0.0015733742620795965}, {"id": 596, "seek":
  321156, "start": 3224.6, "end": 3229.7999999999997, "text": " observation I had
  at the time was that I found that one I so I got something that worked really",
  "tokens": [51016, 14816, 286, 632, 412, 264, 565, 390, 300, 286, 1352, 300, 472,
  286, 370, 286, 658, 746, 300, 2732, 534, 51276], "temperature": 0.0, "avg_logprob":
  -0.17388935226330654, "compression_ratio": 1.8158730158730159, "no_speech_prob":
  0.0015733742620795965}, {"id": 597, "seek": 321156, "start": 3229.7999999999997,
  "end": 3234.52, "text": " well great heristics on SIFT and then when I went it on
  the other data sets it just completely", "tokens": [51276, 731, 869, 720, 6006,
  322, 318, 12775, 51, 293, 550, 562, 286, 1437, 309, 322, 264, 661, 1412, 6352, 309,
  445, 2584, 51512], "temperature": 0.0, "avg_logprob": -0.17388935226330654, "compression_ratio":
  1.8158730158730159, "no_speech_prob": 0.0015733742620795965}, {"id": 598, "seek":
  321156, "start": 3234.52, "end": 3239.64, "text": " did not work well or generalized
  to the other data sets and I think that taught me an early lesson", "tokens": [51512,
  630, 406, 589, 731, 420, 44498, 281, 264, 661, 1412, 6352, 293, 286, 519, 300, 5928,
  385, 364, 2440, 6898, 51768], "temperature": 0.0, "avg_logprob": -0.17388935226330654,
  "compression_ratio": 1.8158730158730159, "no_speech_prob": 0.0015733742620795965},
  {"id": 599, "seek": 323964, "start": 3239.72, "end": 3246.04, "text": " that the
  these academic data sets are just not enough and the only way to know what your
  recall is", "tokens": [50368, 300, 264, 613, 7778, 1412, 6352, 366, 445, 406, 1547,
  293, 264, 787, 636, 281, 458, 437, 428, 9901, 307, 50684], "temperature": 0.0, "avg_logprob":
  -0.12590561699621455, "compression_ratio": 1.610655737704918, "no_speech_prob":
  0.002041584113612771}, {"id": 600, "seek": 323964, "start": 3246.04, "end": 3253.4,
  "text": " going to be is to measure it in production this is what TurboPuffer does
  for a percentage of queries", "tokens": [50684, 516, 281, 312, 307, 281, 3481, 309,
  294, 4265, 341, 307, 437, 35848, 47, 1245, 260, 775, 337, 257, 9668, 295, 24109,
  51052], "temperature": 0.0, "avg_logprob": -0.12590561699621455, "compression_ratio":
  1.610655737704918, "no_speech_prob": 0.002041584113612771}, {"id": 601, "seek":
  323964, "start": 3253.4, "end": 3259.16, "text": " it depends on the number of queries
  that you do but let''s say around 1% of queries TurboPuffer will", "tokens": [51052,
  309, 5946, 322, 264, 1230, 295, 24109, 300, 291, 360, 457, 718, 311, 584, 926, 502,
  4, 295, 24109, 35848, 47, 1245, 260, 486, 51340], "temperature": 0.0, "avg_logprob":
  -0.12590561699621455, "compression_ratio": 1.610655737704918, "no_speech_prob":
  0.002041584113612771}, {"id": 602, "seek": 323964, "start": 3259.16, "end": 3266.04,
  "text": " run an exhaustive search against the A&N index on a separate worker fleet
  we will then emit a", "tokens": [51340, 1190, 364, 14687, 488, 3164, 1970, 264,
  316, 5, 45, 8186, 322, 257, 4994, 11346, 19396, 321, 486, 550, 32084, 257, 51684],
  "temperature": 0.0, "avg_logprob": -0.12590561699621455, "compression_ratio": 1.610655737704918,
  "no_speech_prob": 0.002041584113612771}, {"id": 603, "seek": 326604, "start": 3266.04,
  "end": 3272.2799999999997, "text": " metric to data dog that is the recall number
  right for this query right like which is basically", "tokens": [50364, 20678, 281,
  1412, 3000, 300, 307, 264, 9901, 1230, 558, 337, 341, 14581, 558, 411, 597, 307,
  1936, 50676], "temperature": 0.0, "avg_logprob": -0.16261936289019288, "compression_ratio":
  1.8814229249011858, "no_speech_prob": 0.004885130096226931}, {"id": 604, "seek":
  326604, "start": 3272.2799999999997, "end": 3276.44, "text": " okay this is the
  top 10 we know is accurate and this is the you know heristic A&N index", "tokens":
  [50676, 1392, 341, 307, 264, 1192, 1266, 321, 458, 307, 8559, 293, 341, 307, 264,
  291, 458, 720, 3142, 316, 5, 45, 8186, 50884], "temperature": 0.0, "avg_logprob":
  -0.16261936289019288, "compression_ratio": 1.8814229249011858, "no_speech_prob":
  0.004885130096226931}, {"id": 605, "seek": 326604, "start": 3276.44, "end": 3281.48,
  "text": " is what''s the overlap and we will average that over time I have a graph
  in data dog that shows all", "tokens": [50884, 307, 437, 311, 264, 19959, 293, 321,
  486, 4274, 300, 670, 565, 286, 362, 257, 4295, 294, 1412, 3000, 300, 3110, 439,
  51136], "temperature": 0.0, "avg_logprob": -0.16261936289019288, "compression_ratio":
  1.8814229249011858, "no_speech_prob": 0.004885130096226931}, {"id": 606, "seek":
  326604, "start": 3281.48, "end": 3287.24, "text": " the different organizations
  that have more than 100 queries in the in the past in the past hour", "tokens":
  [51136, 264, 819, 6150, 300, 362, 544, 813, 2319, 24109, 294, 264, 294, 264, 1791,
  294, 264, 1791, 1773, 51424], "temperature": 0.0, "avg_logprob": -0.16261936289019288,
  "compression_ratio": 1.8814229249011858, "no_speech_prob": 0.004885130096226931},
  {"id": 607, "seek": 326604, "start": 3287.24, "end": 3291.56, "text": " or whatever
  and then we have the recall for all of them we have the recall at what they asked
  for", "tokens": [51424, 420, 2035, 293, 550, 321, 362, 264, 9901, 337, 439, 295,
  552, 321, 362, 264, 9901, 412, 437, 436, 2351, 337, 51640], "temperature": 0.0,
  "avg_logprob": -0.16261936289019288, "compression_ratio": 1.8814229249011858, "no_speech_prob":
  0.004885130096226931}, {"id": 608, "seek": 329156, "start": 3291.56, "end": 3297.16,
  "text": " to recall a 10 the p10 recall the p90 recall and we try to our best to
  make sure that this is", "tokens": [50364, 281, 9901, 257, 1266, 264, 280, 3279,
  9901, 264, 280, 7771, 9901, 293, 321, 853, 281, 527, 1151, 281, 652, 988, 300, 341,
  307, 50644], "temperature": 0.0, "avg_logprob": -0.11797353956434461, "compression_ratio":
  1.7419354838709677, "no_speech_prob": 0.0036414596252143383}, {"id": 609, "seek":
  329156, "start": 3297.16, "end": 3305.4, "text": " green at all times and we consider
  green anything above 90% is generally quite good it well 90%", "tokens": [50644,
  3092, 412, 439, 1413, 293, 321, 1949, 3092, 1340, 3673, 4289, 4, 307, 5101, 1596,
  665, 309, 731, 4289, 4, 51056], "temperature": 0.0, "avg_logprob": -0.11797353956434461,
  "compression_ratio": 1.7419354838709677, "no_speech_prob": 0.0036414596252143383},
  {"id": 610, "seek": 329156, "start": 3305.4, "end": 3311.32, "text": " is is quite
  good for some queries but for simple queries often it''s closer to 100% many of
  our", "tokens": [51056, 307, 307, 1596, 665, 337, 512, 24109, 457, 337, 2199, 24109,
  2049, 309, 311, 4966, 281, 2319, 4, 867, 295, 527, 51352], "temperature": 0.0, "avg_logprob":
  -0.11797353956434461, "compression_ratio": 1.7419354838709677, "no_speech_prob":
  0.0036414596252143383}, {"id": 611, "seek": 329156, "start": 3311.32, "end": 3318.68,
  "text": " customers have have 99.5% recall so this is the only way that we know
  to do this and it''s fun", "tokens": [51352, 4581, 362, 362, 11803, 13, 20, 4, 9901,
  370, 341, 307, 264, 787, 636, 300, 321, 458, 281, 360, 341, 293, 309, 311, 1019,
  51720], "temperature": 0.0, "avg_logprob": -0.11797353956434461, "compression_ratio":
  1.7419354838709677, "no_speech_prob": 0.0036414596252143383}, {"id": 612, "seek":
  331868, "start": 3318.68, "end": 3324.12, "text": " you ask this question today
  because last night I was I was hacking on putting this into the dashboard", "tokens":
  [50364, 291, 1029, 341, 1168, 965, 570, 1036, 1818, 286, 390, 286, 390, 31422, 322,
  3372, 341, 666, 264, 18342, 50636], "temperature": 0.0, "avg_logprob": -0.08967226522940176,
  "compression_ratio": 1.807511737089202, "no_speech_prob": 0.006659318692982197},
  {"id": 613, "seek": 331868, "start": 3324.12, "end": 3329.64, "text": " so literally
  putting the recall that we observe from this from this monitoring system into the",
  "tokens": [50636, 370, 3736, 3372, 264, 9901, 300, 321, 11441, 490, 341, 490, 341,
  11028, 1185, 666, 264, 50912], "temperature": 0.0, "avg_logprob": -0.08967226522940176,
  "compression_ratio": 1.807511737089202, "no_speech_prob": 0.006659318692982197},
  {"id": 614, "seek": 331868, "start": 3329.64, "end": 3335.56, "text": " dashboard
  of the user because we think it''s that important and it''s very difficult to get
  right", "tokens": [50912, 18342, 295, 264, 4195, 570, 321, 519, 309, 311, 300, 1021,
  293, 309, 311, 588, 2252, 281, 483, 558, 51208], "temperature": 0.0, "avg_logprob":
  -0.08967226522940176, "compression_ratio": 1.807511737089202, "no_speech_prob":
  0.006659318692982197}, {"id": 615, "seek": 331868, "start": 3335.56, "end": 3340.9199999999996,
  "text": " we have spent thousands of engineering hours to make sure that the recall
  is high now recall", "tokens": [51208, 321, 362, 4418, 5383, 295, 7043, 2496, 281,
  652, 988, 300, 264, 9901, 307, 1090, 586, 9901, 51476], "temperature": 0.0, "avg_logprob":
  -0.08967226522940176, "compression_ratio": 1.807511737089202, "no_speech_prob":
  0.006659318692982197}, {"id": 616, "seek": 334092, "start": 3340.92, "end": 3349.88,
  "text": " on academic benchmarks easy recall on raw ann search is especially on
  academic benchmarks very easy", "tokens": [50364, 322, 7778, 43751, 1858, 9901,
  322, 8936, 364, 77, 3164, 307, 2318, 322, 7778, 43751, 588, 1858, 50812], "temperature":
  0.0, "avg_logprob": -0.2057559225294325, "compression_ratio": 1.6470588235294117,
  "no_speech_prob": 0.004156796727329493}, {"id": 617, "seek": 334092, "start": 3351.96,
  "end": 3357.56, "text": " raw recall on production data sets I''d say medium to
  medium hard", "tokens": [50916, 8936, 9901, 322, 4265, 1412, 6352, 286, 1116, 584,
  6399, 281, 6399, 1152, 51196], "temperature": 0.0, "avg_logprob": -0.2057559225294325,
  "compression_ratio": 1.6470588235294117, "no_speech_prob": 0.004156796727329493},
  {"id": 618, "seek": 334092, "start": 3359.2400000000002, "end": 3366.6, "text":
  " high recall on ann queries with filters with mixed selectivity and incremental
  indexing", "tokens": [51280, 1090, 9901, 322, 364, 77, 24109, 365, 15995, 365, 7467,
  3048, 4253, 293, 35759, 8186, 278, 51648], "temperature": 0.0, "avg_logprob": -0.2057559225294325,
  "compression_ratio": 1.6470588235294117, "no_speech_prob": 0.004156796727329493},
  {"id": 619, "seek": 336660, "start": 3366.6, "end": 3372.2, "text": " absolute hard
  mode this is what the like you just slap a secondary vector index onto an existing",
  "tokens": [50364, 8236, 1152, 4391, 341, 307, 437, 264, 411, 291, 445, 21075, 257,
  11396, 8062, 8186, 3911, 364, 6741, 50644], "temperature": 0.0, "avg_logprob": -0.09728489098725496,
  "compression_ratio": 1.8371212121212122, "no_speech_prob": 0.003582586534321308},
  {"id": 620, "seek": 336660, "start": 3372.2, "end": 3377.3199999999997, "text":
  " database this is what they can''t do they can''t sustain them like a thousand
  writes per second", "tokens": [50644, 8149, 341, 307, 437, 436, 393, 380, 360, 436,
  393, 380, 6769, 552, 411, 257, 4714, 13657, 680, 1150, 50900], "temperature": 0.0,
  "avg_logprob": -0.09728489098725496, "compression_ratio": 1.8371212121212122, "no_speech_prob":
  0.003582586534321308}, {"id": 621, "seek": 336660, "start": 3377.3199999999997,
  "end": 3382.8399999999997, "text": " with high recall in the face of very difficult
  filter queries so let''s talk about filters recall", "tokens": [50900, 365, 1090,
  9901, 294, 264, 1851, 295, 588, 2252, 6608, 24109, 370, 718, 311, 751, 466, 15995,
  9901, 51176], "temperature": 0.0, "avg_logprob": -0.09728489098725496, "compression_ratio":
  1.8371212121212122, "no_speech_prob": 0.003582586534321308}, {"id": 622, "seek":
  336660, "start": 3382.8399999999997, "end": 3388.7599999999998, "text": " for a
  second there is barely any academic data sets on this yet it''s all the production
  workloads", "tokens": [51176, 337, 257, 1150, 456, 307, 10268, 604, 7778, 1412,
  6352, 322, 341, 1939, 309, 311, 439, 264, 4265, 32452, 51472], "temperature": 0.0,
  "avg_logprob": -0.09728489098725496, "compression_ratio": 1.8371212121212122, "no_speech_prob":
  0.003582586534321308}, {"id": 623, "seek": 336660, "start": 3389.48, "end": 3395.0,
  "text": " what a filtered in an index means is that let''s say that for example
  you have you have an ecommerce", "tokens": [51508, 437, 257, 37111, 294, 364, 8186,
  1355, 307, 300, 718, 311, 584, 300, 337, 1365, 291, 362, 291, 362, 364, 308, 26926,
  51784], "temperature": 0.0, "avg_logprob": -0.09728489098725496, "compression_ratio":
  1.8371212121212122, "no_speech_prob": 0.003582586534321308}, {"id": 624, "seek":
  339500, "start": 3395.72, "end": 3404.44, "text": " and you''re searching for you''re
  searching for I don''t know yellow right and you want to only get", "tokens": [50400,
  293, 291, 434, 10808, 337, 291, 434, 10808, 337, 286, 500, 380, 458, 5566, 558,
  293, 291, 528, 281, 787, 483, 50836], "temperature": 0.0, "avg_logprob": -0.14860212802886963,
  "compression_ratio": 1.6844444444444444, "no_speech_prob": 0.005369552411139011},
  {"id": 625, "seek": 339500, "start": 3404.44, "end": 3410.04, "text": " things that
  ship to Canada that cuts the clusters in different weird ways that might end up
  with", "tokens": [50836, 721, 300, 5374, 281, 6309, 300, 9992, 264, 23313, 294,
  819, 3657, 2098, 300, 1062, 917, 493, 365, 51116], "temperature": 0.0, "avg_logprob":
  -0.14860212802886963, "compression_ratio": 1.6844444444444444, "no_speech_prob":
  0.005369552411139011}, {"id": 626, "seek": 339500, "start": 3410.04, "end": 3416.28,
  "text": " a selectivity of 50% and so if you just visit the the closest whatever
  vectors with some", "tokens": [51116, 257, 3048, 4253, 295, 2625, 4, 293, 370, 498,
  291, 445, 3441, 264, 264, 13699, 2035, 18875, 365, 512, 51428], "temperature": 0.0,
  "avg_logprob": -0.14860212802886963, "compression_ratio": 1.6844444444444444, "no_speech_prob":
  0.005369552411139011}, {"id": 627, "seek": 339500, "start": 3416.28, "end": 3420.76,
  "text": " horrific you have you''re not going to get the true ann because you actually
  have to search maybe", "tokens": [51428, 29248, 291, 362, 291, 434, 406, 516, 281,
  483, 264, 2074, 364, 77, 570, 291, 767, 362, 281, 3164, 1310, 51652], "temperature":
  0.0, "avg_logprob": -0.14860212802886963, "compression_ratio": 1.6844444444444444,
  "no_speech_prob": 0.005369552411139011}, {"id": 628, "seek": 342076, "start": 3420.76,
  "end": 3425.7200000000003, "text": " twice as many maybe three times as many vectors
  to get the right recall the query planner the", "tokens": [50364, 6091, 382, 867,
  1310, 1045, 1413, 382, 867, 18875, 281, 483, 264, 558, 9901, 264, 14581, 31268,
  264, 50612], "temperature": 0.0, "avg_logprob": -0.08776487244500054, "compression_ratio":
  1.9362549800796813, "no_speech_prob": 0.0009666657424531877}, {"id": 629, "seek":
  342076, "start": 3425.7200000000003, "end": 3430.36, "text": " thing in the database
  that decides where to go on disk and figure out the data and aggregate it", "tokens":
  [50612, 551, 294, 264, 8149, 300, 14898, 689, 281, 352, 322, 12355, 293, 2573, 484,
  264, 1412, 293, 26118, 309, 50844], "temperature": 0.0, "avg_logprob": -0.08776487244500054,
  "compression_ratio": 1.9362549800796813, "no_speech_prob": 0.0009666657424531877},
  {"id": 630, "seek": 342076, "start": 3430.36, "end": 3435.7200000000003, "text":
  " altogether and return into the user needs to be aware of the selectivity of the
  filter and plan", "tokens": [50844, 19051, 293, 2736, 666, 264, 4195, 2203, 281,
  312, 3650, 295, 264, 3048, 4253, 295, 264, 6608, 293, 1393, 51112], "temperature":
  0.0, "avg_logprob": -0.08776487244500054, "compression_ratio": 1.9362549800796813,
  "no_speech_prob": 0.0009666657424531877}, {"id": 631, "seek": 342076, "start": 3435.7200000000003,
  "end": 3441.7200000000003, "text": " that into the ann index again if a database
  is not really serious about their vector offering they''re", "tokens": [51112, 300,
  666, 264, 364, 77, 8186, 797, 498, 257, 8149, 307, 406, 534, 3156, 466, 641, 8062,
  8745, 436, 434, 51412], "temperature": 0.0, "avg_logprob": -0.08776487244500054,
  "compression_ratio": 1.9362549800796813, "no_speech_prob": 0.0009666657424531877},
  {"id": 632, "seek": 342076, "start": 3441.7200000000003, "end": 3445.5600000000004,
  "text": " not doing this they''re not measuring in a production they''re not they''re
  not willing to show their", "tokens": [51412, 406, 884, 341, 436, 434, 406, 13389,
  294, 257, 4265, 436, 434, 406, 436, 434, 406, 4950, 281, 855, 641, 51604], "temperature":
  0.0, "avg_logprob": -0.08776487244500054, "compression_ratio": 1.9362549800796813,
  "no_speech_prob": 0.0009666657424531877}, {"id": 633, "seek": 344556, "start": 3445.56,
  "end": 3452.2, "text": " users and they''re not they don''t have a full infrastructure
  in place to measure the recall so", "tokens": [50364, 5022, 293, 436, 434, 406,
  436, 500, 380, 362, 257, 1577, 6896, 294, 1081, 281, 3481, 264, 9901, 370, 50696],
  "temperature": 0.0, "avg_logprob": -0.16591591902182135, "compression_ratio": 1.7117647058823529,
  "no_speech_prob": 0.0002247083029942587}, {"id": 634, "seek": 344556, "start": 3452.2,
  "end": 3460.04, "text": " I''d say we take this extremely seriously and we don''t
  want our users to have to get to get to", "tokens": [50696, 286, 1116, 584, 321,
  747, 341, 4664, 6638, 293, 321, 500, 380, 528, 527, 5022, 281, 362, 281, 483, 281,
  483, 281, 51088], "temperature": 0.0, "avg_logprob": -0.16591591902182135, "compression_ratio":
  1.7117647058823529, "no_speech_prob": 0.0002247083029942587}, {"id": 635, "seek":
  344556, "start": 3460.04, "end": 3468.92, "text": " guest this and it''s a it''s
  sometimes a thankless job because because many many many many emails that we", "tokens":
  [51088, 8341, 341, 293, 309, 311, 257, 309, 311, 2171, 257, 1309, 1832, 1691, 570,
  570, 867, 867, 867, 867, 12524, 300, 321, 51532], "temperature": 0.0, "avg_logprob":
  -0.16591591902182135, "compression_ratio": 1.7117647058823529, "no_speech_prob":
  0.0002247083029942587}, {"id": 636, "seek": 346892, "start": 3468.92, "end": 3476.12,
  "text": " see against some of the other vector indexes have very low recall and
  and how are users supposed", "tokens": [50364, 536, 1970, 512, 295, 264, 661, 8062,
  8186, 279, 362, 588, 2295, 9901, 293, 293, 577, 366, 5022, 3442, 50724], "temperature":
  0.0, "avg_logprob": -0.11930939886305067, "compression_ratio": 1.8910505836575875,
  "no_speech_prob": 0.0047335028648376465}, {"id": 637, "seek": 346892, "start": 3476.12,
  "end": 3481.2400000000002, "text": " to know because running these running these
  tests is extremely difficult it is and it''s like it''s", "tokens": [50724, 281,
  458, 570, 2614, 613, 2614, 613, 6921, 307, 4664, 2252, 309, 307, 293, 309, 311,
  411, 309, 311, 50980], "temperature": 0.0, "avg_logprob": -0.11930939886305067,
  "compression_ratio": 1.8910505836575875, "no_speech_prob": 0.0047335028648376465},
  {"id": 638, "seek": 346892, "start": 3481.2400000000002, "end": 3485.96, "text":
  " as you said like you need to trust there right trust your vendor and it''s basically
  like the like", "tokens": [50980, 382, 291, 848, 411, 291, 643, 281, 3361, 456,
  558, 3361, 428, 24321, 293, 309, 311, 1936, 411, 264, 411, 51216], "temperature":
  0.0, "avg_logprob": -0.11930939886305067, "compression_ratio": 1.8910505836575875,
  "no_speech_prob": 0.0047335028648376465}, {"id": 639, "seek": 346892, "start": 3485.96,
  "end": 3491.7200000000003, "text": " in some documentation pages you say the floor
  or like the bottom line right like the needs of each", "tokens": [51216, 294, 512,
  14333, 7183, 291, 584, 264, 4123, 420, 411, 264, 2767, 1622, 558, 411, 264, 2203,
  295, 1184, 51504], "temperature": 0.0, "avg_logprob": -0.11930939886305067, "compression_ratio":
  1.8910505836575875, "no_speech_prob": 0.0047335028648376465}, {"id": 640, "seek":
  346892, "start": 3492.76, "end": 3497.7200000000003, "text": " it just doesn''t
  make sense right if the quality isn''t there then why are you even running this",
  "tokens": [51556, 309, 445, 1177, 380, 652, 2020, 558, 498, 264, 3125, 1943, 380,
  456, 550, 983, 366, 291, 754, 2614, 341, 51804], "temperature": 0.0, "avg_logprob":
  -0.11930939886305067, "compression_ratio": 1.8910505836575875, "no_speech_prob":
  0.0047335028648376465}, {"id": 641, "seek": 349892, "start": 3499.4, "end": 3503.32,
  "text": " it''s a difference between you know finding that product with those constraints",
  "tokens": [50388, 309, 311, 257, 2649, 1296, 291, 458, 5006, 300, 1674, 365, 729,
  18491, 50584], "temperature": 0.0, "avg_logprob": -0.1803402232232495, "compression_ratio":
  1.7572463768115942, "no_speech_prob": 0.003517464967444539}, {"id": 642, "seek":
  349892, "start": 3504.12, "end": 3509.8, "text": " when it exists and actually not
  finding it right therefore not buying it and so on and so on and so forth", "tokens":
  [50624, 562, 309, 8198, 293, 767, 406, 5006, 309, 558, 4412, 406, 6382, 309, 293,
  370, 322, 293, 370, 322, 293, 370, 5220, 50908], "temperature": 0.0, "avg_logprob":
  -0.1803402232232495, "compression_ratio": 1.7572463768115942, "no_speech_prob":
  0.003517464967444539}, {"id": 643, "seek": 349892, "start": 3510.6, "end": 3517.4,
  "text": " it''s right and I think yeah I you can never guarantee a recall you can
  observe what you are trying to", "tokens": [50948, 309, 311, 558, 293, 286, 519,
  1338, 286, 291, 393, 1128, 10815, 257, 9901, 291, 393, 11441, 437, 291, 366, 1382,
  281, 51288], "temperature": 0.0, "avg_logprob": -0.1803402232232495, "compression_ratio":
  1.7572463768115942, "no_speech_prob": 0.003517464967444539}, {"id": 644, "seek":
  349892, "start": 3517.4, "end": 3523.7200000000003, "text": " make it be here on
  every data set but if you send a billion completely random vectors with 3000", "tokens":
  [51288, 652, 309, 312, 510, 322, 633, 1412, 992, 457, 498, 291, 2845, 257, 5218,
  2584, 4974, 18875, 365, 20984, 51604], "temperature": 0.0, "avg_logprob": -0.1803402232232495,
  "compression_ratio": 1.7572463768115942, "no_speech_prob": 0.003517464967444539},
  {"id": 645, "seek": 349892, "start": 3523.7200000000003, "end": 3528.76, "text":
  " dimensions and try to query them in turbo buffer with query vectors and there
  is no natural clustering", "tokens": [51604, 12819, 293, 853, 281, 14581, 552, 294,
  20902, 21762, 365, 14581, 18875, 293, 456, 307, 572, 3303, 596, 48673, 51856], "temperature":
  0.0, "avg_logprob": -0.1803402232232495, "compression_ratio": 1.7572463768115942,
  "no_speech_prob": 0.003517464967444539}, {"id": 646, "seek": 352876, "start": 3528.76,
  "end": 3533.88, "text": " because they''re random vectors you''re not going to get
  100% recall when you send that with a 10%", "tokens": [50364, 570, 436, 434, 4974,
  18875, 291, 434, 406, 516, 281, 483, 2319, 4, 9901, 562, 291, 2845, 300, 365, 257,
  1266, 4, 50620], "temperature": 0.0, "avg_logprob": -0.10300642147398832, "compression_ratio":
  1.7048611111111112, "no_speech_prob": 0.0007871618145145476}, {"id": 647, "seek":
  352876, "start": 3533.88, "end": 3539.48, "text": " selectivity filters that just
  like completely breaks every heuristic that''s made right but all", "tokens": [50620,
  3048, 4253, 15995, 300, 445, 411, 2584, 9857, 633, 415, 374, 3142, 300, 311, 1027,
  558, 457, 439, 50900], "temperature": 0.0, "avg_logprob": -0.10300642147398832,
  "compression_ratio": 1.7048611111111112, "no_speech_prob": 0.0007871618145145476},
  {"id": 648, "seek": 352876, "start": 3539.48, "end": 3544.36, "text": " data in
  production real data that people want to search has some natural clustering to it
  so that''s", "tokens": [50900, 1412, 294, 4265, 957, 1412, 300, 561, 528, 281, 3164,
  575, 512, 3303, 596, 48673, 281, 309, 370, 300, 311, 51144], "temperature": 0.0,
  "avg_logprob": -0.10300642147398832, "compression_ratio": 1.7048611111111112, "no_speech_prob":
  0.0007871618145145476}, {"id": 649, "seek": 352876, "start": 3544.36, "end": 3549.48,
  "text": " not a real benchmark that you can evaluate recall on right and so we always
  take this seriously and", "tokens": [51144, 406, 257, 957, 18927, 300, 291, 393,
  13059, 9901, 322, 558, 293, 370, 321, 1009, 747, 341, 6638, 293, 51400], "temperature":
  0.0, "avg_logprob": -0.10300642147398832, "compression_ratio": 1.7048611111111112,
  "no_speech_prob": 0.0007871618145145476}, {"id": 650, "seek": 352876, "start": 3549.48,
  "end": 3554.2000000000003, "text": " the in the in the in POCs and with the monitoring
  we do we''re looking at these numbers all the time", "tokens": [51400, 264, 294,
  264, 294, 264, 294, 22299, 33290, 293, 365, 264, 11028, 321, 360, 321, 434, 1237,
  412, 613, 3547, 439, 264, 565, 51636], "temperature": 0.0, "avg_logprob": -0.10300642147398832,
  "compression_ratio": 1.7048611111111112, "no_speech_prob": 0.0007871618145145476},
  {"id": 651, "seek": 355420, "start": 3554.2799999999997, "end": 3559.3199999999997,
  "text": " but there are like absolute edge cases that can be very very difficult
  and what you have to do too", "tokens": [50368, 457, 456, 366, 411, 8236, 4691,
  3331, 300, 393, 312, 588, 588, 2252, 293, 437, 291, 362, 281, 360, 886, 50620],
  "temperature": 0.0, "avg_logprob": -0.0928897714256344, "compression_ratio": 2.0701107011070112,
  "no_speech_prob": 0.0029162555001676083}, {"id": 652, "seek": 355420, "start": 3559.3199999999997,
  "end": 3564.3599999999997, "text": " as a database vendor is like it''s a tug is
  a tug of war between we''re going to look at more data to", "tokens": [50620, 382,
  257, 8149, 24321, 307, 411, 309, 311, 257, 33543, 307, 257, 33543, 295, 1516, 1296,
  321, 434, 516, 281, 574, 412, 544, 1412, 281, 50872], "temperature": 0.0, "avg_logprob":
  -0.0928897714256344, "compression_ratio": 2.0701107011070112, "no_speech_prob":
  0.0029162555001676083}, {"id": 653, "seek": 355420, "start": 3564.3599999999997,
  "end": 3569.48, "text": " try to get high recall and we''re going to try to improve
  the clustering of the data so that we", "tokens": [50872, 853, 281, 483, 1090, 9901,
  293, 321, 434, 516, 281, 853, 281, 3470, 264, 596, 48673, 295, 264, 1412, 370, 300,
  321, 51128], "temperature": 0.0, "avg_logprob": -0.0928897714256344, "compression_ratio":
  2.0701107011070112, "no_speech_prob": 0.0029162555001676083}, {"id": 654, "seek":
  355420, "start": 3569.48, "end": 3573.72, "text": " have to search less data and
  so you''re always trying to improve the clustering and you''re always", "tokens":
  [51128, 362, 281, 3164, 1570, 1412, 293, 370, 291, 434, 1009, 1382, 281, 3470, 264,
  596, 48673, 293, 291, 434, 1009, 51340], "temperature": 0.0, "avg_logprob": -0.0928897714256344,
  "compression_ratio": 2.0701107011070112, "no_speech_prob": 0.0029162555001676083},
  {"id": 655, "seek": 355420, "start": 3573.72, "end": 3577.3999999999996, "text":
  " trying to improve the performance of the database so we can look at more data
  to get high recall", "tokens": [51340, 1382, 281, 3470, 264, 3389, 295, 264, 8149,
  370, 321, 393, 574, 412, 544, 1412, 281, 483, 1090, 9901, 51524], "temperature":
  0.0, "avg_logprob": -0.0928897714256344, "compression_ratio": 2.0701107011070112,
  "no_speech_prob": 0.0029162555001676083}, {"id": 656, "seek": 355420, "start": 3578.04,
  "end": 3583.0, "text": " yeah for sure I know that you mentioned about filters you
  know challenges", "tokens": [51556, 1338, 337, 988, 286, 458, 300, 291, 2835, 466,
  15995, 291, 458, 4759, 51804], "temperature": 0.0, "avg_logprob": -0.0928897714256344,
  "compression_ratio": 2.0701107011070112, "no_speech_prob": 0.0029162555001676083},
  {"id": 657, "seek": 358300, "start": 3583.08, "end": 3587.8, "text": " vegan and
  I don''t know if you aware of those the reason an end-end benchmarks right but there
  is", "tokens": [50368, 12824, 293, 286, 500, 380, 458, 498, 291, 3650, 295, 729,
  264, 1778, 364, 917, 12, 521, 43751, 558, 457, 456, 307, 50604], "temperature":
  0.0, "avg_logprob": -0.20629585872996936, "compression_ratio": 1.8195121951219513,
  "no_speech_prob": 0.003529760055243969}, {"id": 658, "seek": 358300, "start": 3587.8,
  "end": 3595.4, "text": " also a big end-end benchmarks that they happen to pleasure
  to participate in they have one of the", "tokens": [50604, 611, 257, 955, 917, 12,
  521, 43751, 300, 436, 1051, 281, 6834, 281, 8197, 294, 436, 362, 472, 295, 264,
  50984], "temperature": 0.0, "avg_logprob": -0.20629585872996936, "compression_ratio":
  1.8195121951219513, "no_speech_prob": 0.003529760055243969}, {"id": 659, "seek":
  358300, "start": 3595.4, "end": 3602.6, "text": " datasets one of the tasks they
  have is the filtered search I have not participated in that one", "tokens": [50984,
  42856, 472, 295, 264, 9608, 436, 362, 307, 264, 37111, 3164, 286, 362, 406, 17978,
  294, 300, 472, 51344], "temperature": 0.0, "avg_logprob": -0.20629585872996936,
  "compression_ratio": 1.8195121951219513, "no_speech_prob": 0.003529760055243969},
  {"id": 660, "seek": 358300, "start": 3602.6, "end": 3607.0, "text": " but again
  as you said it''s kind of like academic but some of the datasets are quite", "tokens":
  [51344, 457, 797, 382, 291, 848, 309, 311, 733, 295, 411, 7778, 457, 512, 295, 264,
  42856, 366, 1596, 51564], "temperature": 0.0, "avg_logprob": -0.20629585872996936,
  "compression_ratio": 1.8195121951219513, "no_speech_prob": 0.003529760055243969},
  {"id": 661, "seek": 360700, "start": 3607.0, "end": 3612.2, "text": " logical like
  beaten points dimensions and not that huge it''s like that''s the thing there are",
  "tokens": [50364, 14978, 411, 17909, 2793, 12819, 293, 406, 300, 2603, 309, 311,
  411, 300, 311, 264, 551, 456, 366, 50624], "temperature": 0.0, "avg_logprob": -0.22292493932387408,
  "compression_ratio": 1.8522167487684729, "no_speech_prob": 0.013297075405716896},
  {"id": 662, "seek": 360700, "start": 3612.2, "end": 3618.04, "text": " 156 yeah
  it''s not like yeah there are hundreds of 200 dimensions these are not real data
  sets", "tokens": [50624, 2119, 21, 1338, 309, 311, 406, 411, 1338, 456, 366, 6779,
  295, 2331, 12819, 613, 366, 406, 957, 1412, 6352, 50916], "temperature": 0.0, "avg_logprob":
  -0.22292493932387408, "compression_ratio": 1.8522167487684729, "no_speech_prob":
  0.013297075405716896}, {"id": 663, "seek": 360700, "start": 3618.68, "end": 3625.48,
  "text": " like no there are real data sets but they are real data sets from the
  past generation of vectors", "tokens": [50948, 411, 572, 456, 366, 957, 1412, 6352,
  457, 436, 366, 957, 1412, 6352, 490, 264, 1791, 5125, 295, 18875, 51288], "temperature":
  0.0, "avg_logprob": -0.22292493932387408, "compression_ratio": 1.8522167487684729,
  "no_speech_prob": 0.013297075405716896}, {"id": 664, "seek": 360700, "start": 3625.48,
  "end": 3633.08, "text": " right the the pre the pre current modern embedding error
  right which are just scores so much", "tokens": [51288, 558, 264, 264, 659, 264,
  659, 2190, 4363, 12240, 3584, 6713, 558, 597, 366, 445, 13444, 370, 709, 51668],
  "temperature": 0.0, "avg_logprob": -0.22292493932387408, "compression_ratio": 1.8522167487684729,
  "no_speech_prob": 0.013297075405716896}, {"id": 665, "seek": 363308, "start": 3633.08,
  "end": 3637.48, "text": " higher than these so we just don''t see people use these
  yeah yeah exactly it''s still fun to", "tokens": [50364, 2946, 813, 613, 370, 321,
  445, 500, 380, 536, 561, 764, 613, 1338, 1338, 2293, 309, 311, 920, 1019, 281, 50584],
  "temperature": 0.0, "avg_logprob": -0.13589160225608132, "compression_ratio": 1.8587786259541985,
  "no_speech_prob": 0.007158421445637941}, {"id": 666, "seek": 363308, "start": 3637.48,
  "end": 3642.04, "text": " participate in this benchmark by the way because the data
  is there and you know the some of the", "tokens": [50584, 8197, 294, 341, 18927,
  538, 264, 636, 570, 264, 1412, 307, 456, 293, 291, 458, 264, 512, 295, 264, 50812],
  "temperature": 0.0, "avg_logprob": -0.13589160225608132, "compression_ratio": 1.8587786259541985,
  "no_speech_prob": 0.007158421445637941}, {"id": 667, "seek": 363308, "start": 3642.04,
  "end": 3648.2, "text": " guarantees that you need to hit really high you know like
  thousands of tens of thousands of queries", "tokens": [50812, 32567, 300, 291, 643,
  281, 2045, 534, 1090, 291, 458, 411, 5383, 295, 10688, 295, 5383, 295, 24109, 51120],
  "temperature": 0.0, "avg_logprob": -0.13589160225608132, "compression_ratio": 1.8587786259541985,
  "no_speech_prob": 0.007158421445637941}, {"id": 668, "seek": 363308, "start": 3648.2,
  "end": 3655.88, "text": " per second so if you can create a toy index that works
  just a proud moment I guess that''s right", "tokens": [51120, 680, 1150, 370, 498,
  291, 393, 1884, 257, 12058, 8186, 300, 1985, 445, 257, 4570, 1623, 286, 2041, 300,
  311, 558, 51504], "temperature": 0.0, "avg_logprob": -0.13589160225608132, "compression_ratio":
  1.8587786259541985, "no_speech_prob": 0.007158421445637941}, {"id": 669, "seek":
  363308, "start": 3656.12, "end": 3662.04, "text": " but I would say that people
  don''t care about these bench like now people care about the benchmarks like", "tokens":
  [51516, 457, 286, 576, 584, 300, 561, 500, 380, 1127, 466, 613, 10638, 411, 586,
  561, 1127, 466, 264, 43751, 411, 51812], "temperature": 0.0, "avg_logprob": -0.13589160225608132,
  "compression_ratio": 1.8587786259541985, "no_speech_prob": 0.007158421445637941},
  {"id": 670, "seek": 366204, "start": 3662.04, "end": 3666.36, "text": " their fun
  competitions but I think it can ruin your company if all you''re trying to do is
  maximize", "tokens": [50364, 641, 1019, 26185, 457, 286, 519, 309, 393, 15514, 428,
  2237, 498, 439, 291, 434, 1382, 281, 360, 307, 19874, 50580], "temperature": 0.0,
  "avg_logprob": -0.1265374664077185, "compression_ratio": 1.751497005988024, "no_speech_prob":
  0.0005586735205724835}, {"id": 671, "seek": 366204, "start": 3666.36, "end": 3671.64,
  "text": " these benchmarks because how many companies on in the world are trying
  to do 10,000 QPS on a billion", "tokens": [50580, 613, 43751, 570, 577, 867, 3431,
  322, 294, 264, 1002, 366, 1382, 281, 360, 1266, 11, 1360, 1249, 6273, 322, 257,
  5218, 50844], "temperature": 0.0, "avg_logprob": -0.1265374664077185, "compression_ratio":
  1.751497005988024, "no_speech_prob": 0.0005586735205724835}, {"id": 672, "seek":
  366204, "start": 3671.64, "end": 3676.6, "text": " vectors right not that many but
  there''s a lot of companies that have a billion vectors lying around", "tokens":
  [50844, 18875, 558, 406, 300, 867, 457, 456, 311, 257, 688, 295, 3431, 300, 362,
  257, 5218, 18875, 8493, 926, 51092], "temperature": 0.0, "avg_logprob": -0.1265374664077185,
  "compression_ratio": 1.751497005988024, "no_speech_prob": 0.0005586735205724835},
  {"id": 673, "seek": 366204, "start": 3676.6, "end": 3680.44, "text": " that they
  want to search and they just don''t want the pricing to be offensive right we''re",
  "tokens": [51092, 300, 436, 528, 281, 3164, 293, 436, 445, 500, 380, 528, 264, 17621,
  281, 312, 15710, 558, 321, 434, 51284], "temperature": 0.0, "avg_logprob": -0.1265374664077185,
  "compression_ratio": 1.751497005988024, "no_speech_prob": 0.0005586735205724835},
  {"id": 674, "seek": 366204, "start": 3680.44, "end": 3683.56, "text": " a turbo
  buffer can you do this depending on the dimensionality for like a thousand dollars
  in", "tokens": [51284, 257, 20902, 21762, 393, 291, 360, 341, 5413, 322, 264, 10139,
  1860, 337, 411, 257, 4714, 3808, 294, 51440], "temperature": 0.0, "avg_logprob":
  -0.1265374664077185, "compression_ratio": 1.751497005988024, "no_speech_prob": 0.0005586735205724835},
  {"id": 675, "seek": 366204, "start": 3683.56, "end": 3690.92, "text": " month that''s
  what people really seem to care about yeah sure maybe if I ask you like a spicy
  question", "tokens": [51440, 1618, 300, 311, 437, 561, 534, 1643, 281, 1127, 466,
  1338, 988, 1310, 498, 286, 1029, 291, 411, 257, 9127, 1168, 51808], "temperature":
  0.0, "avg_logprob": -0.1265374664077185, "compression_ratio": 1.751497005988024,
  "no_speech_prob": 0.0005586735205724835}, {"id": 676, "seek": 369092, "start": 3690.92,
  "end": 3698.12, "text": " if I may why do you think some of the vector database
  players like in Dalgium cells into that game", "tokens": [50364, 498, 286, 815,
  983, 360, 291, 519, 512, 295, 264, 8062, 8149, 4150, 411, 294, 17357, 70, 2197,
  5438, 666, 300, 1216, 50724], "temperature": 0.0, "avg_logprob": -0.14926262335343796,
  "compression_ratio": 1.7660550458715596, "no_speech_prob": 0.004764711018651724},
  {"id": 677, "seek": 369092, "start": 3698.12, "end": 3703.2400000000002, "text":
  " of showing the benchmark and telling we are the best and then you know someone
  else cuts them over", "tokens": [50724, 295, 4099, 264, 18927, 293, 3585, 321, 366,
  264, 1151, 293, 550, 291, 458, 1580, 1646, 9992, 552, 670, 50980], "temperature":
  0.0, "avg_logprob": -0.14926262335343796, "compression_ratio": 1.7660550458715596,
  "no_speech_prob": 0.004764711018651724}, {"id": 678, "seek": 369092, "start": 3703.2400000000002,
  "end": 3708.44, "text": " and says no you made a mistake in the benchmark why do
  you think this is happening like like", "tokens": [50980, 293, 1619, 572, 291, 1027,
  257, 6146, 294, 264, 18927, 983, 360, 291, 519, 341, 307, 2737, 411, 411, 51240],
  "temperature": 0.0, "avg_logprob": -0.14926262335343796, "compression_ratio": 1.7660550458715596,
  "no_speech_prob": 0.004764711018651724}, {"id": 679, "seek": 369092, "start": 3708.44,
  "end": 3717.0, "text": " publicly if you''re comfortable talking about this yeah
  we we don''t we don''t publish benchmarks", "tokens": [51240, 14843, 498, 291, 434,
  4619, 1417, 466, 341, 1338, 321, 321, 500, 380, 321, 500, 380, 11374, 43751, 51668],
  "temperature": 0.0, "avg_logprob": -0.14926262335343796, "compression_ratio": 1.7660550458715596,
  "no_speech_prob": 0.004764711018651724}, {"id": 680, "seek": 371700, "start": 3717.0,
  "end": 3723.16, "text": " against anyone else in in fact it''s it''s it''s usually
  against the terms of service to do that", "tokens": [50364, 1970, 2878, 1646, 294,
  294, 1186, 309, 311, 309, 311, 309, 311, 2673, 1970, 264, 2115, 295, 2643, 281,
  360, 300, 50672], "temperature": 0.0, "avg_logprob": -0.11893197342201516, "compression_ratio":
  1.8537549407114624, "no_speech_prob": 0.015068494714796543}, {"id": 681, "seek":
  371700, "start": 3723.16, "end": 3727.96, "text": " for almost every vendor including
  the big vendors like the hyper scalers probably shouldn''t be", "tokens": [50672,
  337, 1920, 633, 24321, 3009, 264, 955, 22056, 411, 264, 9848, 15664, 433, 1391,
  4659, 380, 312, 50912], "temperature": 0.0, "avg_logprob": -0.11893197342201516,
  "compression_ratio": 1.8537549407114624, "no_speech_prob": 0.015068494714796543},
  {"id": 682, "seek": 371700, "start": 3728.76, "end": 3732.84, "text": " it probably
  should be prohibited for the hyper scalers for like any competitive reasons or",
  "tokens": [50952, 309, 1391, 820, 312, 32069, 337, 264, 9848, 15664, 433, 337, 411,
  604, 10043, 4112, 420, 51156], "temperature": 0.0, "avg_logprob": -0.11893197342201516,
  "compression_ratio": 1.8537549407114624, "no_speech_prob": 0.015068494714796543},
  {"id": 683, "seek": 371700, "start": 3732.84, "end": 3737.8, "text": " but anyway
  for the peers I think it''s it''s like a low blow because everyone can sort of p-hack",
  "tokens": [51156, 457, 4033, 337, 264, 16739, 286, 519, 309, 311, 309, 311, 411,
  257, 2295, 6327, 570, 1518, 393, 1333, 295, 280, 12, 71, 501, 51404], "temperature":
  0.0, "avg_logprob": -0.11893197342201516, "compression_ratio": 1.8537549407114624,
  "no_speech_prob": 0.015068494714796543}, {"id": 684, "seek": 371700, "start": 3737.8,
  "end": 3742.12, "text": " their way to something where they they go better and becomes
  like month throwing and it''s very", "tokens": [51404, 641, 636, 281, 746, 689,
  436, 436, 352, 1101, 293, 3643, 411, 1618, 10238, 293, 309, 311, 588, 51620], "temperature":
  0.0, "avg_logprob": -0.11893197342201516, "compression_ratio": 1.8537549407114624,
  "no_speech_prob": 0.015068494714796543}, {"id": 685, "seek": 374212, "start": 3742.12,
  "end": 3747.96, "text": " distracting activity um we benchmark ourselves in ways
  that we find that our customers are actually", "tokens": [50364, 36689, 5191, 1105,
  321, 18927, 4175, 294, 2098, 300, 321, 915, 300, 527, 4581, 366, 767, 50656], "temperature":
  0.0, "avg_logprob": -0.10454317375465676, "compression_ratio": 1.8104089219330854,
  "no_speech_prob": 0.0021337273065000772}, {"id": 686, "seek": 374212, "start": 3747.96,
  "end": 3752.04, "text": " using the database so we''re not doing it at 10,000 qps
  because it''s just not what we see to a single", "tokens": [50656, 1228, 264, 8149,
  370, 321, 434, 406, 884, 309, 412, 1266, 11, 1360, 9505, 1878, 570, 309, 311, 445,
  406, 437, 321, 536, 281, 257, 2167, 50860], "temperature": 0.0, "avg_logprob": -0.10454317375465676,
  "compression_ratio": 1.8104089219330854, "no_speech_prob": 0.0021337273065000772},
  {"id": 687, "seek": 374212, "start": 3752.04, "end": 3758.52, "text": " namespace
  um so we benchmark against ourselves we benchmark against first principles and we''re
  always", "tokens": [50860, 5288, 17940, 1105, 370, 321, 18927, 1970, 4175, 321,
  18927, 1970, 700, 9156, 293, 321, 434, 1009, 51184], "temperature": 0.0, "avg_logprob":
  -0.10454317375465676, "compression_ratio": 1.8104089219330854, "no_speech_prob":
  0.0021337273065000772}, {"id": 688, "seek": 374212, "start": 3758.52, "end": 3762.3599999999997,
  "text": " considering what is the gap between what turbo puffer does and first principles
  there''s", "tokens": [51184, 8079, 437, 307, 264, 7417, 1296, 437, 20902, 19613,
  260, 775, 293, 700, 9156, 456, 311, 51376], "temperature": 0.0, "avg_logprob": -0.10454317375465676,
  "compression_ratio": 1.8104089219330854, "no_speech_prob": 0.0021337273065000772},
  {"id": 689, "seek": 374212, "start": 3763.96, "end": 3767.7999999999997, "text":
  " that''s what I''ve learned that''s why I do napkin math is because the fundamental
  thing you should", "tokens": [51456, 300, 311, 437, 286, 600, 3264, 300, 311, 983,
  286, 360, 9296, 5843, 5221, 307, 570, 264, 8088, 551, 291, 820, 51648], "temperature":
  0.0, "avg_logprob": -0.10454317375465676, "compression_ratio": 1.8104089219330854,
  "no_speech_prob": 0.0021337273065000772}, {"id": 690, "seek": 376780, "start": 3767.8,
  "end": 3773.5600000000004, "text": " be benchmarking against our first principles
  there''s a gap between what the DRAM or disband with it", "tokens": [50364, 312,
  18927, 278, 1970, 527, 700, 9156, 456, 311, 257, 7417, 1296, 437, 264, 12118, 2865,
  420, 717, 4235, 365, 309, 50652], "temperature": 0.0, "avg_logprob": -0.10652859729269276,
  "compression_ratio": 1.8014440433212997, "no_speech_prob": 0.0008137811091728508},
  {"id": 691, "seek": 376780, "start": 3773.5600000000004, "end": 3779.48, "text":
  " is multiplied by how much if it you need and your database is not doing that well
  then you either", "tokens": [50652, 307, 17207, 538, 577, 709, 498, 309, 291, 643,
  293, 428, 8149, 307, 406, 884, 300, 731, 550, 291, 2139, 50948], "temperature":
  0.0, "avg_logprob": -0.10652859729269276, "compression_ratio": 1.8014440433212997,
  "no_speech_prob": 0.0008137811091728508}, {"id": 692, "seek": 376780, "start": 3779.48,
  "end": 3784.92, "text": " have a gap and you''re understanding or you have a you''ve
  found room for improvement that''s what matters", "tokens": [50948, 362, 257, 7417,
  293, 291, 434, 3701, 420, 291, 362, 257, 291, 600, 1352, 1808, 337, 10444, 300,
  311, 437, 7001, 51220], "temperature": 0.0, "avg_logprob": -0.10652859729269276,
  "compression_ratio": 1.8014440433212997, "no_speech_prob": 0.0008137811091728508},
  {"id": 693, "seek": 376780, "start": 3784.92, "end": 3788.84, "text": " and of course
  it also matters what other people are doing but what matters the most is what your",
  "tokens": [51220, 293, 295, 1164, 309, 611, 7001, 437, 661, 561, 366, 884, 457,
  437, 7001, 264, 881, 307, 437, 428, 51416], "temperature": 0.0, "avg_logprob": -0.10652859729269276,
  "compression_ratio": 1.8014440433212997, "no_speech_prob": 0.0008137811091728508},
  {"id": 694, "seek": 376780, "start": 3788.84, "end": 3794.04, "text": " customers
  are trying to do and they''ll they''ll pull you in that direction so we think that
  this is a", "tokens": [51416, 4581, 366, 1382, 281, 360, 293, 436, 603, 436, 603,
  2235, 291, 294, 300, 3513, 370, 321, 519, 300, 341, 307, 257, 51676], "temperature":
  0.0, "avg_logprob": -0.10652859729269276, "compression_ratio": 1.8014440433212997,
  "no_speech_prob": 0.0008137811091728508}, {"id": 695, "seek": 379404, "start": 3794.04,
  "end": 3798.52, "text": " this easily becomes one of these metrics where you know
  if you give people a metric they''ll optimize for", "tokens": [50364, 341, 3612,
  3643, 472, 295, 613, 16367, 689, 291, 458, 498, 291, 976, 561, 257, 20678, 436,
  603, 19719, 337, 50588], "temperature": 0.0, "avg_logprob": -0.09159499406814575,
  "compression_ratio": 1.9528619528619529, "no_speech_prob": 0.0017855166224762797},
  {"id": 696, "seek": 379404, "start": 3798.52, "end": 3803.88, "text": " it um and
  benchmarks of how many qps you can do at some number recall it''s just not what
  people", "tokens": [50588, 309, 1105, 293, 43751, 295, 577, 867, 9505, 1878, 291,
  393, 360, 412, 512, 1230, 9901, 309, 311, 445, 406, 437, 561, 50856], "temperature":
  0.0, "avg_logprob": -0.09159499406814575, "compression_ratio": 1.9528619528619529,
  "no_speech_prob": 0.0017855166224762797}, {"id": 697, "seek": 379404, "start": 3803.88,
  "end": 3808.44, "text": " care about um they care about it working they care about
  enormous ride throughput they care about", "tokens": [50856, 1127, 466, 1105, 436,
  1127, 466, 309, 1364, 436, 1127, 466, 11322, 5077, 44629, 436, 1127, 466, 51084],
  "temperature": 0.0, "avg_logprob": -0.09159499406814575, "compression_ratio": 1.9528619528619529,
  "no_speech_prob": 0.0017855166224762797}, {"id": 698, "seek": 379404, "start": 3808.44,
  "end": 3813.4, "text": " costs they care about other things necessarily that are
  much harder to put in such a benchmark um", "tokens": [51084, 5497, 436, 1127, 466,
  661, 721, 4725, 300, 366, 709, 6081, 281, 829, 294, 1270, 257, 18927, 1105, 51332],
  "temperature": 0.0, "avg_logprob": -0.09159499406814575, "compression_ratio": 1.9528619528619529,
  "no_speech_prob": 0.0017855166224762797}, {"id": 699, "seek": 379404, "start": 3813.4,
  "end": 3817.56, "text": " I think benchmarks are important like we need to give
  people a sense of what they should expect", "tokens": [51332, 286, 519, 43751, 366,
  1021, 411, 321, 643, 281, 976, 561, 257, 2020, 295, 437, 436, 820, 2066, 51540],
  "temperature": 0.0, "avg_logprob": -0.09159499406814575, "compression_ratio": 1.9528619528619529,
  "no_speech_prob": 0.0017855166224762797}, {"id": 700, "seek": 379404, "start": 3817.56,
  "end": 3822.04, "text": " and they should hold us truth at that and what I would
  love to have is like more absurd", "tokens": [51540, 293, 436, 820, 1797, 505, 3494,
  412, 300, 293, 437, 286, 576, 959, 281, 362, 307, 411, 544, 19774, 51764], "temperature":
  0.0, "avg_logprob": -0.09159499406814575, "compression_ratio": 1.9528619528619529,
  "no_speech_prob": 0.0017855166224762797}, {"id": 701, "seek": 382204, "start": 3822.04,
  "end": 3825.96, "text": " ability in the turbo puffer product of like what kind
  of like performance are you seeing um", "tokens": [50364, 3485, 294, 264, 20902,
  19613, 260, 1674, 295, 411, 437, 733, 295, 411, 3389, 366, 291, 2577, 1105, 50560],
  "temperature": 0.0, "avg_logprob": -0.18909495452354694, "compression_ratio": 1.8884615384615384,
  "no_speech_prob": 0.03186819702386856}, {"id": 702, "seek": 382204, "start": 3825.96,
  "end": 3831.16, "text": " we''re working on you know explaining um our exposing
  query plans from turbo puffer right so you can see", "tokens": [50560, 321, 434,
  1364, 322, 291, 458, 13468, 1105, 527, 33178, 14581, 5482, 490, 20902, 19613, 260,
  558, 370, 291, 393, 536, 50820], "temperature": 0.0, "avg_logprob": -0.18909495452354694,
  "compression_ratio": 1.8884615384615384, "no_speech_prob": 0.03186819702386856},
  {"id": 703, "seek": 382204, "start": 3831.16, "end": 3837.64, "text": " um well
  what''s what''s causing the indexing uh sorry what''s causing the the query latency
  to be what it is", "tokens": [50820, 1105, 731, 437, 311, 437, 311, 9853, 264, 8186,
  278, 2232, 2597, 437, 311, 9853, 264, 264, 14581, 27043, 281, 312, 437, 309, 307,
  51144], "temperature": 0.0, "avg_logprob": -0.18909495452354694, "compression_ratio":
  1.8884615384615384, "no_speech_prob": 0.03186819702386856}, {"id": 704, "seek":
  382204, "start": 3837.64, "end": 3842.2, "text": " so yeah I don''t think the mud
  throwing is great um I think that at some point someone''s going to", "tokens":
  [51144, 370, 1338, 286, 500, 380, 519, 264, 8933, 10238, 307, 869, 1105, 286, 519,
  300, 412, 512, 935, 1580, 311, 516, 281, 51372], "temperature": 0.0, "avg_logprob":
  -0.18909495452354694, "compression_ratio": 1.8884615384615384, "no_speech_prob":
  0.03186819702386856}, {"id": 705, "seek": 382204, "start": 3842.2, "end": 3847.72,
  "text": " publish a benchmark with turbo puffer and um and and again something else
  and and then we''ll", "tokens": [51372, 11374, 257, 18927, 365, 20902, 19613, 260,
  293, 1105, 293, 293, 797, 746, 1646, 293, 293, 550, 321, 603, 51648], "temperature":
  0.0, "avg_logprob": -0.18909495452354694, "compression_ratio": 1.8884615384615384,
  "no_speech_prob": 0.03186819702386856}, {"id": 706, "seek": 384772, "start": 3847.7999999999997,
  "end": 3852.7599999999998, "text": " have to deal with that as it comes right um
  by um but it''s certainly not an activity that we plan", "tokens": [50368, 362,
  281, 2028, 365, 300, 382, 309, 1487, 558, 1105, 538, 1105, 457, 309, 311, 3297,
  406, 364, 5191, 300, 321, 1393, 50616], "temperature": 0.0, "avg_logprob": -0.1483280616894103,
  "compression_ratio": 1.7234042553191489, "no_speech_prob": 0.007801888510584831},
  {"id": 707, "seek": 384772, "start": 3852.7599999999998, "end": 3858.2, "text":
  " to engage in yeah I love your answer because it also resonates with me like in
  a different dimension", "tokens": [50616, 281, 4683, 294, 1338, 286, 959, 428, 1867,
  570, 309, 611, 41051, 365, 385, 411, 294, 257, 819, 10139, 50888], "temperature":
  0.0, "avg_logprob": -0.1483280616894103, "compression_ratio": 1.7234042553191489,
  "no_speech_prob": 0.007801888510584831}, {"id": 708, "seek": 384772, "start": 3858.2,
  "end": 3863.72, "text": " you know I found myself in a situation when at some point
  in the past when um we''ve been copy", "tokens": [50888, 291, 458, 286, 1352, 2059,
  294, 257, 2590, 562, 412, 512, 935, 294, 264, 1791, 562, 1105, 321, 600, 668, 5055,
  51164], "temperature": 0.0, "avg_logprob": -0.1483280616894103, "compression_ratio":
  1.7234042553191489, "no_speech_prob": 0.007801888510584831}, {"id": 709, "seek":
  384772, "start": 3864.7599999999998, "end": 3869.08, "text": " copycatted I can''t
  be say in that way so there was a company that really literally copied the whole",
  "tokens": [51216, 5055, 66, 32509, 286, 393, 380, 312, 584, 294, 300, 636, 370,
  456, 390, 257, 2237, 300, 534, 3736, 25365, 264, 1379, 51432], "temperature": 0.0,
  "avg_logprob": -0.1483280616894103, "compression_ratio": 1.7234042553191489, "no_speech_prob":
  0.007801888510584831}, {"id": 710, "seek": 384772, "start": 3869.08, "end": 3874.52,
  "text": " interface and it like how how the product looks and we felt threatened
  but what they couldn''t", "tokens": [51432, 9226, 293, 309, 411, 577, 577, 264,
  1674, 1542, 293, 321, 2762, 18268, 457, 437, 436, 2809, 380, 51704], "temperature":
  0.0, "avg_logprob": -0.1483280616894103, "compression_ratio": 1.7234042553191489,
  "no_speech_prob": 0.007801888510584831}, {"id": 711, "seek": 387452, "start": 3874.52,
  "end": 3880.36, "text": " copy is essentially the internal IP right all the algorithms
  everything where we''ve spent hard", "tokens": [50364, 5055, 307, 4476, 264, 6920,
  8671, 558, 439, 264, 14642, 1203, 689, 321, 600, 4418, 1152, 50656], "temperature":
  0.0, "avg_logprob": -0.1465372870950138, "compression_ratio": 1.7105263157894737,
  "no_speech_prob": 0.0010933134471997619}, {"id": 712, "seek": 387452, "start": 3881.0,
  "end": 3887.96, "text": " hard uh working time on you know they couldn''t copy that
  and and effectively that doesn''t fly", "tokens": [50688, 1152, 2232, 1364, 565,
  322, 291, 458, 436, 2809, 380, 5055, 300, 293, 293, 8659, 300, 1177, 380, 3603,
  51036], "temperature": 0.0, "avg_logprob": -0.1465372870950138, "compression_ratio":
  1.7105263157894737, "no_speech_prob": 0.0010933134471997619}, {"id": 713, "seek":
  387452, "start": 3887.96, "end": 3893.96, "text": " by itself right so so basically
  what I''m trying to say is that you know even though it felt threatening", "tokens":
  [51036, 538, 2564, 558, 370, 370, 1936, 437, 286, 478, 1382, 281, 584, 307, 300,
  291, 458, 754, 1673, 309, 2762, 20768, 51336], "temperature": 0.0, "avg_logprob":
  -0.1465372870950138, "compression_ratio": 1.7105263157894737, "no_speech_prob":
  0.0010933134471997619}, {"id": 714, "seek": 387452, "start": 3894.6, "end": 3901.56,
  "text": " still thinking about what you need to solve right by the laws of physics
  you really need to focus", "tokens": [51368, 920, 1953, 466, 437, 291, 643, 281,
  5039, 558, 538, 264, 6064, 295, 10649, 291, 534, 643, 281, 1879, 51716], "temperature":
  0.0, "avg_logprob": -0.1465372870950138, "compression_ratio": 1.7105263157894737,
  "no_speech_prob": 0.0010933134471997619}, {"id": 715, "seek": 390156, "start": 3901.56,
  "end": 3906.44, "text": " just on that and if you solve that you become the leader
  of the market and that''s what happened", "tokens": [50364, 445, 322, 300, 293,
  498, 291, 5039, 300, 291, 1813, 264, 5263, 295, 264, 2142, 293, 300, 311, 437, 2011,
  50608], "temperature": 0.0, "avg_logprob": -0.12110464572906494, "compression_ratio":
  1.9606299212598426, "no_speech_prob": 0.010753949172794819}, {"id": 716, "seek":
  390156, "start": 3906.44, "end": 3912.6, "text": " to the company actually it the
  story was that it actually acquired this copycat right and that''s it", "tokens":
  [50608, 281, 264, 2237, 767, 309, 264, 1657, 390, 300, 309, 767, 17554, 341, 5055,
  18035, 558, 293, 300, 311, 309, 50916], "temperature": 0.0, "avg_logprob": -0.12110464572906494,
  "compression_ratio": 1.9606299212598426, "no_speech_prob": 0.010753949172794819},
  {"id": 717, "seek": 390156, "start": 3913.16, "end": 3917.4, "text": " uh I mean
  it doesn''t mean that''s the bad thing bad outcome for either of them but what I''m
  trying to", "tokens": [50944, 2232, 286, 914, 309, 1177, 380, 914, 300, 311, 264,
  1578, 551, 1578, 9700, 337, 2139, 295, 552, 457, 437, 286, 478, 1382, 281, 51156],
  "temperature": 0.0, "avg_logprob": -0.12110464572906494, "compression_ratio": 1.9606299212598426,
  "no_speech_prob": 0.010753949172794819}, {"id": 718, "seek": 390156, "start": 3917.4,
  "end": 3922.52, "text": " say is that just focus on that on that thing that you''re
  trying to solve and don''t try to indulge", "tokens": [51156, 584, 307, 300, 445,
  1879, 322, 300, 322, 300, 551, 300, 291, 434, 1382, 281, 5039, 293, 500, 380, 853,
  281, 28626, 432, 51412], "temperature": 0.0, "avg_logprob": -0.12110464572906494,
  "compression_ratio": 1.9606299212598426, "no_speech_prob": 0.010753949172794819},
  {"id": 719, "seek": 390156, "start": 3922.52, "end": 3929.24, "text": " into these
  you know games of like you said you know not throwing and stuff I like that really
  well said", "tokens": [51412, 666, 613, 291, 458, 2813, 295, 411, 291, 848, 291,
  458, 406, 10238, 293, 1507, 286, 411, 300, 534, 731, 848, 51748], "temperature":
  0.0, "avg_logprob": -0.12110464572906494, "compression_ratio": 1.9606299212598426,
  "no_speech_prob": 0.010753949172794819}, {"id": 720, "seek": 392924, "start": 3929.24,
  "end": 3936.2, "text": " yeah that''s I think I think so we focus on on customer
  studies we focus on we focus on on", "tokens": [50364, 1338, 300, 311, 286, 519,
  286, 519, 370, 321, 1879, 322, 322, 5474, 5313, 321, 1879, 322, 321, 1879, 322,
  322, 50712], "temperature": 0.0, "avg_logprob": -0.1164558905142325, "compression_ratio":
  2.0837004405286343, "no_speech_prob": 0.0023051046300679445}, {"id": 721, "seek":
  392924, "start": 3936.2, "end": 3941.7999999999997, "text": " first principles we
  focus on benchmarking and we focus on on what are customers telling you", "tokens":
  [50712, 700, 9156, 321, 1879, 322, 18927, 278, 293, 321, 1879, 322, 322, 437, 366,
  4581, 3585, 291, 50992], "temperature": 0.0, "avg_logprob": -0.1164558905142325,
  "compression_ratio": 2.0837004405286343, "no_speech_prob": 0.0023051046300679445},
  {"id": 722, "seek": 392924, "start": 3941.7999999999997, "end": 3947.16, "text":
  " telling us that they need and I think that um I think those are the right things
  to focus on for our", "tokens": [50992, 3585, 505, 300, 436, 643, 293, 286, 519,
  300, 1105, 286, 519, 729, 366, 264, 558, 721, 281, 1879, 322, 337, 527, 51260],
  "temperature": 0.0, "avg_logprob": -0.1164558905142325, "compression_ratio": 2.0837004405286343,
  "no_speech_prob": 0.0023051046300679445}, {"id": 723, "seek": 392924, "start": 3947.16,
  "end": 3953.08, "text": " company for sure and and and just looking at the clientele
  right the the ones that you shared", "tokens": [51260, 2237, 337, 988, 293, 293,
  293, 445, 1237, 412, 264, 6423, 16884, 558, 264, 264, 2306, 300, 291, 5507, 51556],
  "temperature": 0.0, "avg_logprob": -0.1164558905142325, "compression_ratio": 2.0837004405286343,
  "no_speech_prob": 0.0023051046300679445}, {"id": 724, "seek": 392924, "start": 3953.08,
  "end": 3958.04, "text": " just just knowing those names cursor and and notion that
  everyone is pretty much using every day", "tokens": [51556, 445, 445, 5276, 729,
  5288, 28169, 293, 293, 10710, 300, 1518, 307, 1238, 709, 1228, 633, 786, 51804],
  "temperature": 0.0, "avg_logprob": -0.1164558905142325, "compression_ratio": 2.0837004405286343,
  "no_speech_prob": 0.0023051046300679445}, {"id": 725, "seek": 395804, "start": 3958.04,
  "end": 3963.8, "text": " that''s like a testament to what you''ve done um I also
  wanted to ask you before we close I wanted to", "tokens": [50364, 300, 311, 411,
  257, 35499, 281, 437, 291, 600, 1096, 1105, 286, 611, 1415, 281, 1029, 291, 949,
  321, 1998, 286, 1415, 281, 50652], "temperature": 0.0, "avg_logprob": -0.14637079546528478,
  "compression_ratio": 1.695067264573991, "no_speech_prob": 0.0015682813245803118},
  {"id": 726, "seek": 395804, "start": 3963.8, "end": 3971.4, "text": " ask you about
  what are the maybe technical or business or some other challenges that you see",
  "tokens": [50652, 1029, 291, 466, 437, 366, 264, 1310, 6191, 420, 1606, 420, 512,
  661, 4759, 300, 291, 536, 51032], "temperature": 0.0, "avg_logprob": -0.14637079546528478,
  "compression_ratio": 1.695067264573991, "no_speech_prob": 0.0015682813245803118},
  {"id": 727, "seek": 395804, "start": 3971.4, "end": 3975.48, "text": " ahead of
  yourself or maybe that''s what already is happening and you see that it''s important",
  "tokens": [51032, 2286, 295, 1803, 420, 1310, 300, 311, 437, 1217, 307, 2737, 293,
  291, 536, 300, 309, 311, 1021, 51236], "temperature": 0.0, "avg_logprob": -0.14637079546528478,
  "compression_ratio": 1.695067264573991, "no_speech_prob": 0.0015682813245803118},
  {"id": 728, "seek": 395804, "start": 3976.36, "end": 3984.7599999999998, "text":
  " especially in this space of LLAMS where LLAMS can bring value um what is it it
  feels like you", "tokens": [51280, 2318, 294, 341, 1901, 295, 441, 43, 2865, 50,
  689, 441, 43, 2865, 50, 393, 1565, 2158, 1105, 437, 307, 309, 309, 3417, 411, 291,
  51700], "temperature": 0.0, "avg_logprob": -0.14637079546528478, "compression_ratio":
  1.695067264573991, "no_speech_prob": 0.0015682813245803118}, {"id": 729, "seek":
  398476, "start": 3985.0, "end": 3990.6000000000004, "text": " you have wildly successful
  as a business and as a technology but is there something that you see", "tokens":
  [50376, 291, 362, 4868, 356, 4406, 382, 257, 1606, 293, 382, 257, 2899, 457, 307,
  456, 746, 300, 291, 536, 50656], "temperature": 0.0, "avg_logprob": -0.18548973216566927,
  "compression_ratio": 1.5545454545454545, "no_speech_prob": 0.002473148750141263},
  {"id": 730, "seek": 398476, "start": 3991.1600000000003, "end": 3994.84, "text":
  " is still unsolved and and is ahead of you and worth solving", "tokens": [50684,
  307, 920, 2693, 29110, 293, 293, 307, 2286, 295, 291, 293, 3163, 12606, 50868],
  "temperature": 0.0, "avg_logprob": -0.18548973216566927, "compression_ratio": 1.5545454545454545,
  "no_speech_prob": 0.002473148750141263}, {"id": 731, "seek": 398476, "start": 3999.88,
  "end": 4006.2000000000003, "text": " I''ll go back to a you know I spent a long
  time at Shopify and so part of growing up at that", "tokens": [51120, 286, 603,
  352, 646, 281, 257, 291, 458, 286, 4418, 257, 938, 565, 412, 43991, 293, 370, 644,
  295, 4194, 493, 412, 300, 51436], "temperature": 0.0, "avg_logprob": -0.18548973216566927,
  "compression_ratio": 1.5545454545454545, "no_speech_prob": 0.002473148750141263},
  {"id": 732, "seek": 398476, "start": 4006.2000000000003, "end": 4011.1600000000003,
  "text": " company from when I was very young was being taught a bit in the school
  of Toby Lukay the CEO", "tokens": [51436, 2237, 490, 562, 286, 390, 588, 2037, 390,
  885, 5928, 257, 857, 294, 264, 1395, 295, 40223, 34992, 320, 264, 9282, 51684],
  "temperature": 0.0, "avg_logprob": -0.18548973216566927, "compression_ratio": 1.5545454545454545,
  "no_speech_prob": 0.002473148750141263}, {"id": 733, "seek": 401116, "start": 4011.24,
  "end": 4018.2, "text": " and something that he often said is that you know you about
  himself is like you have to grow to keep", "tokens": [50368, 293, 746, 300, 415,
  2049, 848, 307, 300, 291, 458, 291, 466, 3647, 307, 411, 291, 362, 281, 1852, 281,
  1066, 50716], "temperature": 0.0, "avg_logprob": -0.11925489344495407, "compression_ratio":
  1.6933333333333334, "no_speech_prob": 0.0027155608404427767}, {"id": 734, "seek":
  401116, "start": 4018.2, "end": 4024.68, "text": " up with the business and that''s
  that''s what it is for me as well right I um first had to grow as an", "tokens":
  [50716, 493, 365, 264, 1606, 293, 300, 311, 300, 311, 437, 309, 307, 337, 385, 382,
  731, 558, 286, 1105, 700, 632, 281, 1852, 382, 364, 51040], "temperature": 0.0,
  "avg_logprob": -0.11925489344495407, "compression_ratio": 1.6933333333333334, "no_speech_prob":
  0.0027155608404427767}, {"id": 735, "seek": 401116, "start": 4024.68, "end": 4030.04,
  "text": " engineer to put out the first version um then I had to build an engineering
  team to take it much", "tokens": [51040, 11403, 281, 829, 484, 264, 700, 3037, 1105,
  550, 286, 632, 281, 1322, 364, 7043, 1469, 281, 747, 309, 709, 51308], "temperature":
  0.0, "avg_logprob": -0.11925489344495407, "compression_ratio": 1.6933333333333334,
  "no_speech_prob": 0.0027155608404427767}, {"id": 736, "seek": 401116, "start": 4030.04,
  "end": 4035.56, "text": " further than I ever could alone and I think we have and
  just an absolutely like 99%", "tokens": [51308, 3052, 813, 286, 1562, 727, 3312,
  293, 286, 519, 321, 362, 293, 445, 364, 3122, 411, 11803, 4, 51584], "temperature":
  0.0, "avg_logprob": -0.11925489344495407, "compression_ratio": 1.6933333333333334,
  "no_speech_prob": 0.0027155608404427767}, {"id": 737, "seek": 403556, "start": 4035.56,
  "end": 4042.12, "text": " college engineering team now then I turned my focus to
  sales and learning that and now I turn", "tokens": [50364, 3859, 7043, 1469, 586,
  550, 286, 3574, 452, 1879, 281, 5763, 293, 2539, 300, 293, 586, 286, 1261, 50692],
  "temperature": 0.0, "avg_logprob": -0.12436038835913735, "compression_ratio": 2.0,
  "no_speech_prob": 0.0060279155150055885}, {"id": 738, "seek": 403556, "start": 4042.68,
  "end": 4047.32, "text": " now I have to turn it towards marketing towards legal
  towards all these different things to build", "tokens": [50720, 586, 286, 362, 281,
  1261, 309, 3030, 6370, 3030, 5089, 3030, 439, 613, 819, 721, 281, 1322, 50952],
  "temperature": 0.0, "avg_logprob": -0.12436038835913735, "compression_ratio": 2.0,
  "no_speech_prob": 0.0060279155150055885}, {"id": 739, "seek": 403556, "start": 4047.32,
  "end": 4053.72, "text": " the company I we spoke a little bit about this about this
  before um about I think that one of the", "tokens": [50952, 264, 2237, 286, 321,
  7179, 257, 707, 857, 466, 341, 466, 341, 949, 1105, 466, 286, 519, 300, 472, 295,
  264, 51272], "temperature": 0.0, "avg_logprob": -0.12436038835913735, "compression_ratio":
  2.0, "no_speech_prob": 0.0060279155150055885}, {"id": 740, "seek": 403556, "start":
  4053.72, "end": 4058.84, "text": " beliefs that we have is just the town density
  of the team and I don''t think there''s a lot of I", "tokens": [51272, 13585, 300,
  321, 362, 307, 445, 264, 3954, 10305, 295, 264, 1469, 293, 286, 500, 380, 519, 456,
  311, 257, 688, 295, 286, 51528], "temperature": 0.0, "avg_logprob": -0.12436038835913735,
  "compression_ratio": 2.0, "no_speech_prob": 0.0060279155150055885}, {"id": 741,
  "seek": 403556, "start": 4058.84, "end": 4063.72, "text": " think that a lot of
  people talk a lot about the town density and I think that there is um now a", "tokens":
  [51528, 519, 300, 257, 688, 295, 561, 751, 257, 688, 466, 264, 3954, 10305, 293,
  286, 519, 300, 456, 307, 1105, 586, 257, 51772], "temperature": 0.0, "avg_logprob":
  -0.12436038835913735, "compression_ratio": 2.0, "no_speech_prob": 0.0060279155150055885},
  {"id": 742, "seek": 406372, "start": 4063.72, "end": 4068.9199999999996, "text":
  " generation of companies that''s really trying to do it um I think that um the
  tools that we now", "tokens": [50364, 5125, 295, 3431, 300, 311, 534, 1382, 281,
  360, 309, 1105, 286, 519, 300, 1105, 264, 3873, 300, 321, 586, 50624], "temperature":
  0.0, "avg_logprob": -0.06795200434598056, "compression_ratio": 1.755656108597285,
  "no_speech_prob": 0.0014239277224987745}, {"id": 743, "seek": 406372, "start": 4068.9199999999996,
  "end": 4076.2, "text": " have available to us and especially the kind of tool that
  we work on every day um the floor for", "tokens": [50624, 362, 2435, 281, 505, 293,
  2318, 264, 733, 295, 2290, 300, 321, 589, 322, 633, 786, 1105, 264, 4123, 337, 50988],
  "temperature": 0.0, "avg_logprob": -0.06795200434598056, "compression_ratio": 1.755656108597285,
  "no_speech_prob": 0.0014239277224987745}, {"id": 744, "seek": 406372, "start": 4076.2,
  "end": 4082.4399999999996, "text": " productivity has been raised but the ceiling
  has been raised far more and so what really matters to", "tokens": [50988, 15604,
  575, 668, 6005, 457, 264, 13655, 575, 668, 6005, 1400, 544, 293, 370, 437, 534,
  7001, 281, 51300], "temperature": 0.0, "avg_logprob": -0.06795200434598056, "compression_ratio":
  1.755656108597285, "no_speech_prob": 0.0014239277224987745}, {"id": 745, "seek":
  406372, "start": 4082.4399999999996, "end": 4088.4399999999996, "text": " us is
  having a team of individuals that where everyone is is a player right we see these
  teams as", "tokens": [51300, 505, 307, 1419, 257, 1469, 295, 5346, 300, 689, 1518,
  307, 307, 257, 4256, 558, 321, 536, 613, 5491, 382, 51600], "temperature": 0.0,
  "avg_logprob": -0.06795200434598056, "compression_ratio": 1.755656108597285, "no_speech_prob":
  0.0014239277224987745}, {"id": 746, "seek": 408844, "start": 4088.44, "end": 4094.04,
  "text": " a symbol of almost more like sports teams today um then how companies
  were originally uh originally", "tokens": [50364, 257, 5986, 295, 1920, 544, 411,
  6573, 5491, 965, 1105, 550, 577, 3431, 645, 7993, 2232, 7993, 50644], "temperature":
  0.0, "avg_logprob": -0.09398909538022933, "compression_ratio": 1.8211009174311927,
  "no_speech_prob": 0.0013162157265469432}, {"id": 747, "seek": 408844, "start": 4094.04,
  "end": 4101.4, "text": " built um and I think that we we hold that as a as a strong
  belief in how we we um we are building", "tokens": [50644, 3094, 1105, 293, 286,
  519, 300, 321, 321, 1797, 300, 382, 257, 382, 257, 2068, 7107, 294, 577, 321, 321,
  1105, 321, 366, 2390, 51012], "temperature": 0.0, "avg_logprob": -0.09398909538022933,
  "compression_ratio": 1.8211009174311927, "no_speech_prob": 0.0013162157265469432},
  {"id": 748, "seek": 408844, "start": 4101.4, "end": 4107.08, "text": " the company
  but it demands a lot from everyone to work in this way but it''s very fun um and
  I think", "tokens": [51012, 264, 2237, 457, 309, 15107, 257, 688, 490, 1518, 281,
  589, 294, 341, 636, 457, 309, 311, 588, 1019, 1105, 293, 286, 519, 51296], "temperature":
  0.0, "avg_logprob": -0.09398909538022933, "compression_ratio": 1.8211009174311927,
  "no_speech_prob": 0.0013162157265469432}, {"id": 749, "seek": 408844, "start": 4107.08,
  "end": 4112.84, "text": " that the the growth that that embodies on everyone including
  myself is important and I have to keep", "tokens": [51296, 300, 264, 264, 4599,
  300, 300, 4605, 6087, 322, 1518, 3009, 2059, 307, 1021, 293, 286, 362, 281, 1066,
  51584], "temperature": 0.0, "avg_logprob": -0.09398909538022933, "compression_ratio":
  1.8211009174311927, "no_speech_prob": 0.0013162157265469432}, {"id": 750, "seek":
  411284, "start": 4112.84, "end": 4118.4400000000005, "text": " up with that I have
  to keep up with the demand of of of how our customers and our team internally",
  "tokens": [50364, 493, 365, 300, 286, 362, 281, 1066, 493, 365, 264, 4733, 295,
  295, 295, 577, 527, 4581, 293, 527, 1469, 19501, 50644], "temperature": 0.0, "avg_logprob":
  -0.0971376895904541, "compression_ratio": 1.7644444444444445, "no_speech_prob":
  0.004712470807135105}, {"id": 751, "seek": 411284, "start": 4119.24, "end": 4124.360000000001,
  "text": " and everything grows and that''s that''s the biggest challenge is just
  the amount of new that has to", "tokens": [50684, 293, 1203, 13156, 293, 300, 311,
  300, 311, 264, 3880, 3430, 307, 445, 264, 2372, 295, 777, 300, 575, 281, 50940],
  "temperature": 0.0, "avg_logprob": -0.0971376895904541, "compression_ratio": 1.7644444444444445,
  "no_speech_prob": 0.004712470807135105}, {"id": 752, "seek": 411284, "start": 4124.360000000001,
  "end": 4130.52, "text": " be learned um so that we can become a successful company
  which is is important for me for our customers", "tokens": [50940, 312, 3264, 1105,
  370, 300, 321, 393, 1813, 257, 4406, 2237, 597, 307, 307, 1021, 337, 385, 337, 527,
  4581, 51248], "temperature": 0.0, "avg_logprob": -0.0971376895904541, "compression_ratio":
  1.7644444444444445, "no_speech_prob": 0.004712470807135105}, {"id": 753, "seek":
  411284, "start": 4130.52, "end": 4135.4800000000005, "text": " and for everyone
  who''s chosen to come along for the ride and join the company. Oh that''s awesome",
  "tokens": [51248, 293, 337, 1518, 567, 311, 8614, 281, 808, 2051, 337, 264, 5077,
  293, 3917, 264, 2237, 13, 876, 300, 311, 3476, 51496], "temperature": 0.0, "avg_logprob":
  -0.0971376895904541, "compression_ratio": 1.7644444444444445, "no_speech_prob":
  0.004712470807135105}, {"id": 754, "seek": 413548, "start": 4135.48, "end": 4143.16,
  "text": " yeah this field changes so quickly um it it felt much slower when I was
  coding myself you know", "tokens": [50364, 1338, 341, 2519, 2962, 370, 2661, 1105,
  309, 309, 2762, 709, 14009, 562, 286, 390, 17720, 2059, 291, 458, 50748], "temperature":
  0.0, "avg_logprob": -0.12982624901665582, "compression_ratio": 1.6122448979591837,
  "no_speech_prob": 0.010721574537456036}, {"id": 755, "seek": 413548, "start": 4143.16,
  "end": 4149.32, "text": " Java you seen all that stuff you you had like solar elastic
  search that''s it for like long time", "tokens": [50748, 10745, 291, 1612, 439,
  300, 1507, 291, 291, 632, 411, 7936, 17115, 3164, 300, 311, 309, 337, 411, 938,
  565, 51056], "temperature": 0.0, "avg_logprob": -0.12982624901665582, "compression_ratio":
  1.6122448979591837, "no_speech_prob": 0.010721574537456036}, {"id": 756, "seek":
  413548, "start": 4149.32, "end": 4156.44, "text": " and then a lot of new engines
  popped up especially when vector search appeared on the scene but now with", "tokens":
  [51056, 293, 550, 257, 688, 295, 777, 12982, 21545, 493, 2318, 562, 8062, 3164,
  8516, 322, 264, 4145, 457, 586, 365, 51412], "temperature": 0.0, "avg_logprob":
  -0.12982624901665582, "compression_ratio": 1.6122448979591837, "no_speech_prob":
  0.010721574537456036}, {"id": 757, "seek": 413548, "start": 4156.44, "end": 4162.36,
  "text": " the LEM advancements and all of that it just feels so crazy so yeah it''s
  very interesting challenge", "tokens": [51412, 264, 441, 6683, 7295, 1117, 293,
  439, 295, 300, 309, 445, 3417, 370, 3219, 370, 1338, 309, 311, 588, 1880, 3430,
  51708], "temperature": 0.0, "avg_logprob": -0.12982624901665582, "compression_ratio":
  1.6122448979591837, "no_speech_prob": 0.010721574537456036}, {"id": 758, "seek":
  416236, "start": 4162.36, "end": 4170.04, "text": " for sure you know personally
  and business wise and and team wise and yeah and and keeping balance", "tokens":
  [50364, 337, 988, 291, 458, 5665, 293, 1606, 10829, 293, 293, 1469, 10829, 293,
  1338, 293, 293, 5145, 4772, 50748], "temperature": 0.0, "avg_logprob": -0.14645883930263234,
  "compression_ratio": 1.6333333333333333, "no_speech_prob": 0.0028533500153571367},
  {"id": 759, "seek": 416236, "start": 4170.04, "end": 4177.08, "text": " is another
  one. I think the pace of the pace that we see everyone running at now in the successful",
  "tokens": [50748, 307, 1071, 472, 13, 286, 519, 264, 11638, 295, 264, 11638, 300,
  321, 536, 1518, 2614, 412, 586, 294, 264, 4406, 51100], "temperature": 0.0, "avg_logprob":
  -0.14645883930263234, "compression_ratio": 1.6333333333333333, "no_speech_prob":
  0.0028533500153571367}, {"id": 760, "seek": 416236, "start": 4177.08, "end": 4185.639999999999,
  "text": " companies is beyond anything that I''ve seen before um it reminds me of
  of just the the the months", "tokens": [51100, 3431, 307, 4399, 1340, 300, 286,
  600, 1612, 949, 1105, 309, 12025, 385, 295, 295, 445, 264, 264, 264, 2493, 51528],
  "temperature": 0.0, "avg_logprob": -0.14645883930263234, "compression_ratio": 1.6333333333333333,
  "no_speech_prob": 0.0028533500153571367}, {"id": 761, "seek": 418564, "start": 4185.64,
  "end": 4193.88, "text": " leading up to black friday at Shopify but it''s all the
  time and I love it I''m addicted to that pace", "tokens": [50364, 5775, 493, 281,
  2211, 431, 4708, 412, 43991, 457, 309, 311, 439, 264, 565, 293, 286, 959, 309, 286,
  478, 24629, 281, 300, 11638, 50776], "temperature": 0.0, "avg_logprob": -0.09048097783868964,
  "compression_ratio": 1.6995708154506437, "no_speech_prob": 0.012471274472773075},
  {"id": 762, "seek": 418564, "start": 4193.88, "end": 4199.8, "text": " and I think
  that we have created a team of people who seek intensity and that''s exactly what
  we", "tokens": [50776, 293, 286, 519, 300, 321, 362, 2942, 257, 1469, 295, 561,
  567, 8075, 13749, 293, 300, 311, 2293, 437, 321, 51072], "temperature": 0.0, "avg_logprob":
  -0.09048097783868964, "compression_ratio": 1.6995708154506437, "no_speech_prob":
  0.012471274472773075}, {"id": 763, "seek": 418564, "start": 4199.8, "end": 4204.68,
  "text": " think that we need to create the right product at a pace that makes sense
  for also our customers", "tokens": [51072, 519, 300, 321, 643, 281, 1884, 264, 558,
  1674, 412, 257, 11638, 300, 1669, 2020, 337, 611, 527, 4581, 51316], "temperature":
  0.0, "avg_logprob": -0.09048097783868964, "compression_ratio": 1.6995708154506437,
  "no_speech_prob": 0.012471274472773075}, {"id": 764, "seek": 418564, "start": 4204.68,
  "end": 4209.320000000001, "text": " so the day are never bottled next on us and
  that is what keeps me up at night. Oh that''s awesome that''s", "tokens": [51316,
  370, 264, 786, 366, 1128, 2274, 1493, 958, 322, 505, 293, 300, 307, 437, 5965, 385,
  493, 412, 1818, 13, 876, 300, 311, 3476, 300, 311, 51548], "temperature": 0.0, "avg_logprob":
  -0.09048097783868964, "compression_ratio": 1.6995708154506437, "no_speech_prob":
  0.012471274472773075}, {"id": 765, "seek": 420932, "start": 4210.2, "end": 4217.719999999999,
  "text": " great cause. We usually end with some sort of announcement anything you
  want to say to the audience", "tokens": [50408, 869, 3082, 13, 492, 2673, 917, 365,
  512, 1333, 295, 12847, 1340, 291, 528, 281, 584, 281, 264, 4034, 50784], "temperature":
  0.0, "avg_logprob": -0.17218775159857247, "compression_ratio": 1.7022222222222223,
  "no_speech_prob": 0.005553343333303928}, {"id": 766, "seek": 420932, "start": 4217.719999999999,
  "end": 4222.36, "text": " especially now that you said that you want to go deeper
  into marketing it beats your chance", "tokens": [50784, 2318, 586, 300, 291, 848,
  300, 291, 528, 281, 352, 7731, 666, 6370, 309, 16447, 428, 2931, 51016], "temperature":
  0.0, "avg_logprob": -0.17218775159857247, "compression_ratio": 1.7022222222222223,
  "no_speech_prob": 0.005553343333303928}, {"id": 767, "seek": 420932, "start": 4224.12,
  "end": 4231.16, "text": " anything that you want to share all call for. I think
  that we we we we''ve refrained from doing any", "tokens": [51104, 1340, 300, 291,
  528, 281, 2073, 439, 818, 337, 13, 286, 519, 300, 321, 321, 321, 321, 600, 1895,
  31774, 490, 884, 604, 51456], "temperature": 0.0, "avg_logprob": -0.17218775159857247,
  "compression_ratio": 1.7022222222222223, "no_speech_prob": 0.005553343333303928},
  {"id": 768, "seek": 420932, "start": 4231.16, "end": 4237.16, "text": " large releases
  and we try to just ship as rapidly as we possibly can if I look at the change",
  "tokens": [51456, 2416, 16952, 293, 321, 853, 281, 445, 5374, 382, 12910, 382, 321,
  6264, 393, 498, 286, 574, 412, 264, 1319, 51756], "temperature": 0.0, "avg_logprob":
  -0.17218775159857247, "compression_ratio": 1.7022222222222223, "no_speech_prob":
  0.005553343333303928}, {"id": 769, "seek": 423716, "start": 4237.16, "end": 4242.36,
  "text": " log this month it''s um I mean we we launched to we launched the region
  the Singapore Canada", "tokens": [50364, 3565, 341, 1618, 309, 311, 1105, 286, 914,
  321, 321, 8730, 281, 321, 8730, 264, 4458, 264, 14491, 6309, 50624], "temperature":
  0.0, "avg_logprob": -0.1832933177118716, "compression_ratio": 1.7491039426523298,
  "no_speech_prob": 0.06415931135416031}, {"id": 770, "seek": 423716, "start": 4242.36,
  "end": 4249.24, "text": " we''ve added the float tight uh we''ve we''ve recently
  added clients for Java Go Ruby um one of the things", "tokens": [50624, 321, 600,
  3869, 264, 15706, 4524, 2232, 321, 600, 321, 600, 3938, 3869, 6982, 337, 10745,
  1037, 19907, 1105, 472, 295, 264, 721, 50968], "temperature": 0.0, "avg_logprob":
  -0.1832933177118716, "compression_ratio": 1.7491039426523298, "no_speech_prob":
  0.06415931135416031}, {"id": 771, "seek": 423716, "start": 4249.24, "end": 4255.08,
  "text": " that I think is is really exciting is our conditional rights and this
  is where turbo puffer is", "tokens": [50968, 300, 286, 519, 307, 307, 534, 4670,
  307, 527, 27708, 4601, 293, 341, 307, 689, 20902, 19613, 260, 307, 51260], "temperature":
  0.0, "avg_logprob": -0.1832933177118716, "compression_ratio": 1.7491039426523298,
  "no_speech_prob": 0.06415931135416031}, {"id": 772, "seek": 423716, "start": 4255.08,
  "end": 4261.4, "text": " not just a bunch of files on s3 it''s not even just a search
  engine it could do conditional rights", "tokens": [51260, 406, 445, 257, 3840, 295,
  7098, 322, 262, 18, 309, 311, 406, 754, 445, 257, 3164, 2848, 309, 727, 360, 27708,
  4601, 51576], "temperature": 0.0, "avg_logprob": -0.1832933177118716, "compression_ratio":
  1.7491039426523298, "no_speech_prob": 0.06415931135416031}, {"id": 773, "seek":
  423716, "start": 4261.4, "end": 4266.92, "text": " where you can say hey I only
  want to replace this document if it''s newer than the old version right", "tokens":
  [51576, 689, 291, 393, 584, 4177, 286, 787, 528, 281, 7406, 341, 4166, 498, 309,
  311, 17628, 813, 264, 1331, 3037, 558, 51852], "temperature": 0.0, "avg_logprob":
  -0.1832933177118716, "compression_ratio": 1.7491039426523298, "no_speech_prob":
  0.06415931135416031}, {"id": 774, "seek": 426716, "start": 4267.8, "end": 4272.599999999999,
  "text": " these are real database features and things like patch right where you
  do a partial update but we", "tokens": [50396, 613, 366, 957, 8149, 4122, 293, 721,
  411, 9972, 558, 689, 291, 360, 257, 14641, 5623, 457, 321, 50636], "temperature":
  0.0, "avg_logprob": -0.13236265346921725, "compression_ratio": 1.8164794007490637,
  "no_speech_prob": 0.005810700356960297}, {"id": 775, "seek": 426716, "start": 4272.599999999999,
  "end": 4278.5199999999995, "text": " don''t we we just we just launched and then
  we put it on put it on x and we move on um so I don''t", "tokens": [50636, 500,
  380, 321, 321, 445, 321, 445, 8730, 293, 550, 321, 829, 309, 322, 829, 309, 322,
  2031, 293, 321, 1286, 322, 1105, 370, 286, 500, 380, 50932], "temperature": 0.0,
  "avg_logprob": -0.13236265346921725, "compression_ratio": 1.8164794007490637, "no_speech_prob":
  0.005810700356960297}, {"id": 776, "seek": 426716, "start": 4278.5199999999995,
  "end": 4282.5199999999995, "text": " have any big announcement we went GA a couple
  a couple months ago it would have luck to have done that", "tokens": [50932, 362,
  604, 955, 12847, 321, 1437, 22841, 257, 1916, 257, 1916, 2493, 2057, 309, 576, 362,
  3668, 281, 362, 1096, 300, 51132], "temperature": 0.0, "avg_logprob": -0.13236265346921725,
  "compression_ratio": 1.8164794007490637, "no_speech_prob": 0.005810700356960297},
  {"id": 777, "seek": 426716, "start": 4282.5199999999995, "end": 4288.04, "text":
  " but we just tried to ship an announcement just get it out there as soon as possible
  move on", "tokens": [51132, 457, 321, 445, 3031, 281, 5374, 364, 12847, 445, 483,
  309, 484, 456, 382, 2321, 382, 1944, 1286, 322, 51408], "temperature": 0.0, "avg_logprob":
  -0.13236265346921725, "compression_ratio": 1.8164794007490637, "no_speech_prob":
  0.005810700356960297}, {"id": 778, "seek": 426716, "start": 4288.04, "end": 4292.68,
  "text": " and ship the next thing. Yeah congratulations on Jay on your original
  launch but on Jay I think", "tokens": [51408, 293, 5374, 264, 958, 551, 13, 865,
  13568, 322, 11146, 322, 428, 3380, 4025, 457, 322, 11146, 286, 519, 51640], "temperature":
  0.0, "avg_logprob": -0.13236265346921725, "compression_ratio": 1.8164794007490637,
  "no_speech_prob": 0.005810700356960297}, {"id": 779, "seek": 429268, "start": 4292.68,
  "end": 4299.240000000001, "text": " it''s a big milestone as well and as you said
  you''re probably not as sort of transactional anymore", "tokens": [50364, 309, 311,
  257, 955, 28048, 382, 731, 293, 382, 291, 848, 291, 434, 1391, 406, 382, 1333, 295,
  46688, 1966, 3602, 50692], "temperature": 0.0, "avg_logprob": -0.0870864137690118,
  "compression_ratio": 1.6352459016393444, "no_speech_prob": 0.010361993685364723},
  {"id": 780, "seek": 429268, "start": 4299.240000000001, "end": 4304.4400000000005,
  "text": " you just keep shipping and you follow what the customers need and but
  sometimes some of these things", "tokens": [50692, 291, 445, 1066, 14122, 293, 291,
  1524, 437, 264, 4581, 643, 293, 457, 2171, 512, 295, 613, 721, 50952], "temperature":
  0.0, "avg_logprob": -0.0870864137690118, "compression_ratio": 1.6352459016393444,
  "no_speech_prob": 0.010361993685364723}, {"id": 781, "seek": 429268, "start": 4304.4400000000005,
  "end": 4310.6, "text": " may go and notice unless you know people follow exactly
  what you do and so in that sense I feel like", "tokens": [50952, 815, 352, 293,
  3449, 5969, 291, 458, 561, 1524, 2293, 437, 291, 360, 293, 370, 294, 300, 2020,
  286, 841, 411, 51260], "temperature": 0.0, "avg_logprob": -0.0870864137690118, "compression_ratio":
  1.6352459016393444, "no_speech_prob": 0.010361993685364723}, {"id": 782, "seek":
  429268, "start": 4310.6, "end": 4317.8, "text": " there is a room or stage for saying
  hey guys go go use it it''s GA right run your benchmark. I think", "tokens": [51260,
  456, 307, 257, 1808, 420, 3233, 337, 1566, 4177, 1074, 352, 352, 764, 309, 309,
  311, 22841, 558, 1190, 428, 18927, 13, 286, 519, 51620], "temperature": 0.0, "avg_logprob":
  -0.0870864137690118, "compression_ratio": 1.6352459016393444, "no_speech_prob":
  0.010361993685364723}, {"id": 783, "seek": 431780, "start": 4318.76, "end": 4323.320000000001,
  "text": " now do they think about it been more I think one announcement might be
  that early and", "tokens": [50412, 586, 360, 436, 519, 466, 309, 668, 544, 286,
  519, 472, 12847, 1062, 312, 300, 2440, 293, 50640], "temperature": 0.0, "avg_logprob":
  -0.14729079746064686, "compression_ratio": 1.7804878048780488, "no_speech_prob":
  0.0030768937431275845}, {"id": 784, "seek": 431780, "start": 4323.320000000001,
  "end": 4328.6, "text": " unintervaled puffer''s history we were very focused on
  doing many namespaces that were small", "tokens": [50640, 517, 5106, 3337, 292,
  19613, 260, 311, 2503, 321, 645, 588, 5178, 322, 884, 867, 5288, 79, 2116, 300,
  645, 1359, 50904], "temperature": 0.0, "avg_logprob": -0.14729079746064686, "compression_ratio":
  1.7804878048780488, "no_speech_prob": 0.0030768937431275845}, {"id": 785, "seek":
  431780, "start": 4329.16, "end": 4335.96, "text": " but we are getting very good
  at large namespaces now and we have customers that are searching", "tokens": [50932,
  457, 321, 366, 1242, 588, 665, 412, 2416, 5288, 79, 2116, 586, 293, 321, 362, 4581,
  300, 366, 10808, 51272], "temperature": 0.0, "avg_logprob": -0.14729079746064686,
  "compression_ratio": 1.7804878048780488, "no_speech_prob": 0.0030768937431275845},
  {"id": 786, "seek": 431780, "start": 4335.96, "end": 4343.72, "text": " billions
  of vectors at once and we have customers that want to search hundreds of billions
  of", "tokens": [51272, 17375, 295, 18875, 412, 1564, 293, 321, 362, 4581, 300, 528,
  281, 3164, 6779, 295, 17375, 295, 51660], "temperature": 0.0, "avg_logprob": -0.14729079746064686,
  "compression_ratio": 1.7804878048780488, "no_speech_prob": 0.0030768937431275845},
  {"id": 787, "seek": 434372, "start": 4343.72, "end": 4350.4400000000005, "text":
  " vectors all at once and we are working with them on that and this is not particularly
  scary anymore", "tokens": [50364, 18875, 439, 412, 1564, 293, 321, 366, 1364, 365,
  552, 322, 300, 293, 341, 307, 406, 4098, 6958, 3602, 50700], "temperature": 0.0,
  "avg_logprob": -0.1229084079915827, "compression_ratio": 1.706140350877193, "no_speech_prob":
  0.0020374376326799393}, {"id": 788, "seek": 434372, "start": 4350.4400000000005,
  "end": 4355.8, "text": " you know exactly what we need to get there so if you have
  use cases of that caliber you may have", "tokens": [50700, 291, 458, 2293, 437,
  321, 643, 281, 483, 456, 370, 498, 291, 362, 764, 3331, 295, 300, 41946, 291, 815,
  362, 50968], "temperature": 0.0, "avg_logprob": -0.1229084079915827, "compression_ratio":
  1.706140350877193, "no_speech_prob": 0.0020374376326799393}, {"id": 789, "seek":
  434372, "start": 4355.8, "end": 4361.400000000001, "text": " passed by turbo puffer
  before but we''re getting ready and we are ready for hundreds of million", "tokens":
  [50968, 4678, 538, 20902, 19613, 260, 949, 457, 321, 434, 1242, 1919, 293, 321,
  366, 1919, 337, 6779, 295, 2459, 51248], "temperature": 0.0, "avg_logprob": -0.1229084079915827,
  "compression_ratio": 1.706140350877193, "no_speech_prob": 0.0020374376326799393},
  {"id": 790, "seek": 434372, "start": 4362.2, "end": 4368.4400000000005, "text":
  " and billions at once the only limitation there is the is really just the size
  of a single machine", "tokens": [51288, 293, 17375, 412, 1564, 264, 787, 27432,
  456, 307, 264, 307, 534, 445, 264, 2744, 295, 257, 2167, 3479, 51600], "temperature":
  0.0, "avg_logprob": -0.1229084079915827, "compression_ratio": 1.706140350877193,
  "no_speech_prob": 0.0020374376326799393}, {"id": 791, "seek": 436844, "start": 4368.5199999999995,
  "end": 4373.799999999999, "text": " and then we shard over them but I think back
  to the sharding we had before you need to make every", "tokens": [50368, 293, 550,
  321, 402, 515, 670, 552, 457, 286, 519, 646, 281, 264, 402, 515, 278, 321, 632,
  949, 291, 643, 281, 652, 633, 50632], "temperature": 0.0, "avg_logprob": -0.16148722672662816,
  "compression_ratio": 1.7608695652173914, "no_speech_prob": 0.007752406410872936},
  {"id": 792, "seek": 436844, "start": 4373.799999999999, "end": 4377.96, "text":
  " shard as large as possible to get the best economics and the best performance
  and that''s been one", "tokens": [50632, 402, 515, 382, 2416, 382, 1944, 281, 483,
  264, 1151, 14564, 293, 264, 1151, 3389, 293, 300, 311, 668, 472, 50840], "temperature":
  0.0, "avg_logprob": -0.16148722672662816, "compression_ratio": 1.7608695652173914,
  "no_speech_prob": 0.007752406410872936}, {"id": 793, "seek": 436844, "start": 4377.96,
  "end": 4382.44, "text": " of the issues with some of the traditional story tangents.
  Yeah for sure. Yeah I really enjoyed", "tokens": [50840, 295, 264, 2663, 365, 512,
  295, 264, 5164, 1657, 10266, 791, 13, 865, 337, 988, 13, 865, 286, 534, 4626, 51064],
  "temperature": 0.0, "avg_logprob": -0.16148722672662816, "compression_ratio": 1.7608695652173914,
  "no_speech_prob": 0.007752406410872936}, {"id": 794, "seek": 436844, "start": 4382.44,
  "end": 4387.16, "text": " the convo I know we could have gone and so many topics
  like I really wanted to ask you also about", "tokens": [51064, 264, 416, 3080, 286,
  458, 321, 727, 362, 2780, 293, 370, 867, 8378, 411, 286, 534, 1415, 281, 1029, 291,
  611, 466, 51300], "temperature": 0.0, "avg_logprob": -0.16148722672662816, "compression_ratio":
  1.7608695652173914, "no_speech_prob": 0.007752406410872936}, {"id": 795, "seek":
  436844, "start": 4387.16, "end": 4395.24, "text": " an an algorithms and stuff but
  I also I feel like we could talk more later as well you know down", "tokens": [51300,
  364, 364, 14642, 293, 1507, 457, 286, 611, 286, 841, 411, 321, 727, 751, 544, 1780,
  382, 731, 291, 458, 760, 51704], "temperature": 0.0, "avg_logprob": -0.16148722672662816,
  "compression_ratio": 1.7608695652173914, "no_speech_prob": 0.007752406410872936},
  {"id": 796, "seek": 439524, "start": 4395.24, "end": 4400.679999999999, "text":
  " the road as you guys are progressing hopefully you''ll be open to that but I''ve
  learned a ton and", "tokens": [50364, 264, 3060, 382, 291, 1074, 366, 36305, 4696,
  291, 603, 312, 1269, 281, 300, 457, 286, 600, 3264, 257, 2952, 293, 50636], "temperature":
  0.0, "avg_logprob": -0.13507414999462308, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.004269792232662439}, {"id": 797, "seek": 439524, "start": 4400.679999999999,
  "end": 4407.32, "text": " it''s very interesting designed that you have and and
  the whole journey of you pushing for four", "tokens": [50636, 309, 311, 588, 1880,
  4761, 300, 291, 362, 293, 293, 264, 1379, 4671, 295, 291, 7380, 337, 1451, 50968],
  "temperature": 0.0, "avg_logprob": -0.13507414999462308, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.004269792232662439}, {"id": 798, "seek": 439524, "start": 4407.32,
  "end": 4413.88, "text": " months you know and interrupted I hope you now regain
  some of the balance back to your life", "tokens": [50968, 2493, 291, 458, 293, 30329,
  286, 1454, 291, 586, 35336, 512, 295, 264, 4772, 646, 281, 428, 993, 51296], "temperature":
  0.0, "avg_logprob": -0.13507414999462308, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.004269792232662439}, {"id": 799, "seek": 439524, "start": 4414.599999999999,
  "end": 4419.8, "text": " now that you have the team supporting you but I really
  enjoyed this conversation Simon thank you", "tokens": [51332, 586, 300, 291, 362,
  264, 1469, 7231, 291, 457, 286, 534, 4626, 341, 3761, 13193, 1309, 291, 51592],
  "temperature": 0.0, "avg_logprob": -0.13507414999462308, "compression_ratio": 1.6888888888888889,
  "no_speech_prob": 0.004269792232662439}, {"id": 800, "seek": 441980, "start": 4419.8,
  "end": 4429.8, "text": " so much for your time thank you Dimitri", "tokens": [50364,
  370, 709, 337, 428, 565, 1309, 291, 20975, 270, 470, 50864], "temperature": 0.0,
  "avg_logprob": -0.48959115835336536, "compression_ratio": 0.8863636363636364, "no_speech_prob":
  0.09183885902166367}]'
---

Now, let's get started. MAPKIN Problem 4 Today, as you are preparing your organic, high mountain type needs along in the kitchen net.
One of your lovely co-workers mentioned that they were looking at adding more radices because it was maxing out at 10,000 commands per second, which they were trending aggressively towards. You asked them how they were using it.
Were they writing some obscure order and command? They would BPF probes to determine that it was all get key and set key value. They also confirmed all the values were about less than 64 bytes. For those unfamiliar with radices, it's single threaded in memory key value store written in C.
And faced, after this encounter, you walk to the window. You look out and see if your high mountain type needs along. As you stare at yet another condominium building being built, it hits you. 10,000 commands per second. 10,000.
Isn't that a bit low? Shouldn't something that's fundamentally just doing random memory reads and writes over an established TCP session be able to do more? Hello there. Vector podcast is back. Season 4.
And we are kicking off with an exciting topic and guest assignment, Eskulls and CEO of TurboPuffer. I've been watching you guys from almost from the start, just following each other on Twitter, like virtual friends.
And it's funny that before this episode, you're the CEO of the company and this for this episode, you try to sell TurboPuffer to me and say, hey, why don't you use it? Did you make a compound tom should pass? Yeah, should pass, for sure. But tell me, hey, welcome, first of all, welcome.
And thank you very much for having with me. It's a tradition to usually start with the background. If you could speak in your own words about yourself, your journey.
I know that you've worked at Shopify at some point, also scaling databases, I guess, right? But I've also been following your napkin math newsletter. I was reading maybe I'll quote some text today from there, just to amuse an exciting audience. But tell me about yourself.
Yeah, I can give a very brief overview and if we can dig into anything, if there's anything that stands out. I started programming when I was a teenager. Similar to you, English is not my first language.
So at some point, I exhausted the Danish web and then like divulged into video game addiction for three years as a teenager to learn enough English to sort of, you know, get my own chat CBT moment and take off point.
And then I spent a lot of time in high school being not very good at competitive programming, but good enough to qualify for the small country of Denmark. And then I spent almost a decade working at Shopify doing mainly infrastructure work.
So when I joined infrastructure Shopify and the infrastructure team, we were doing, I mean, it was not even an infrastructure team like DevOps was just becoming a thing. And we were driving just a couple hundred requests per second. And by the time I left, we saw peaks of more than a million.
And I more or less worked on all of the stateful systems that power that because they generally tend to be the bottleneck just playing whack-a-mole every single year for every Black Friday for many years. And I spent the majority of those years on one of the last resort pages for Shopify as well.
One of those pages were the pages are very scary in the middle of the night and where a lot of GME of course runs through Shopify. So very high responsibility on that. I left in 2021 and kind of jumped around at my friends' companies helping them with various things.
And I spent almost my entire career at one company. So I wanted to dabble and just go and basically help my friends with any infrastructure challenges that they had. And in 2023 when Chatschy BT launched and the APIs launched, I was working with my friends at this company called Readwise.
They have a product similar to a pocket and others for reading articles later from an Amal product. And they asked me to build a recommendation feature for articles. And I was like, well, it's perfect, right? LLMs or embedding models are basically just LLMs with their heads chopped off.
And they're trained on exactly this data. So we built something and it actually worked pretty well for just recommending articles. But then I ran the back of the envelope math on what it would cost to do this for the entire article catalog, right? It had hundreds of millions of articles.
And it would have cost more than 30 grand a month to do. And for a large company that's not a big deal for an experiment. But this was a company that was spending three grand a month on a Postgres instance that prior to working on this, I tuned.
And spending 10 times that on just recommendations and possibly search was just untenable. So it sort of lost it. It was lost in its track. And it was a bit sad.
And it's sort of ended up in that bucket that a lot of companies have of like, okay, we're going to work on this when it becomes cheaper and then we'll ship this feature. But it was a bit sad because I was excited about this feature. It's a user of the product as well.
And I could not stop thinking about that. Why was it so expensive? And the vector databases at the time were storing everything in memory. And DRAM on a cloud cost somewhere between two to five dollars per gigabyte. And this just economics of this didn't line up.
It wasn't that this vector database was doing anything, you know, malicious in their pricing. They're just trying to earn them on its margin on memory pricing. But memory pricing was just too high and it stopped its feature and it's tracks.
And what I couldn't stop thinking about is, why can't we do all of this on top of Obick storage, right? Like we just put it on an Obick storage. That's the source of truth. And then we actually need to some piece of data and we put it in memory or even on this if we can.
And I did it to Mac and Nathan. And I was like, I think that's about a hundred times cheaper. And of course, that would have been no brainer for read wise.
We would have just bought it and started using it and tried it out, right? And maybe put way more data in and maybe worked our way up to that 30 grand a month bill. But with a different workload. And so yeah, I couldn't stop thinking about it.
And then eventually started writing the first version over the summer of 2023. Just me alone in the wills of Canada and then launched it in October of 2023, which is probably where you saw it. I didn't really tell anyone about it. I was just I was just hacking away.
Launched it did a lot of our deal over that summer insights that some of them still are in the product and a lot of them we've since faced out. But the most important thing was that it launched.
And the first version of trouble puffer didn't have I was just looking at the website the other day for an unrelated reason. It didn't have mutable indexes. So you just wrote to it and then you called an index endpoint and then you're logged in like that's it. And it didn't have any SDKs.
It was just a big pure HTML website. But it was enough to ship it and it caught the attention at the time of the cursor team back in 2023. And of course, this was this was this was early on for cursor. It was early on for us.
And they are they're a vector database built did not line up with their per user economics and how they wanted to use rag in their in cursor. And so they they wanted to try to work together.
And we exchanged a bunch of emails of bullet points and it was very clear that they thought that this architecture was exactly now knowing the team are now they were just sat down at the dining table, done to napkin math over there and then thought why hasn't anyone built it like this.
 And so we worked we worked I went to San Francisco and spent some time with them and came up with a bunch of features that they would need and called the best engineer that I knew would Shopify my co founder Justin and asked if they'd come on board because I think I think maybe there's something here.
 And yeah, we launched it cursor cursor moved over and their bill was reduced by 95% and of course the additional storage architect today were on before didn't make sense for the cursor economics but our storage architecture really did because you put all the all the code based embeddings on s3 and then the ones that are actively being used we can use in grammar or have in disk.
I'll stop there but that would be what led up to to this moment. Oh, that's amazing journey.
 A lot to ask of course a lot of questions but just on that cursor thing as I told you before we started recording you know I knew about you launching this working on this and then I've released it to the Lex Friedman podcast episode with the cursor team and they didn't mention turbo pop for sort of like in passing but you know I think that also probably created a lot of attention to you guys but I'm just curious like how did you get together how did you know cursor team somehow someone on the cursor team that you could like partner early on and essentially help they kind of like helped you to pioneer it right in some sense becoming the first client or maybe future client right how did you approach them.
They did I mean they were a design partner in every sense of the word right we had a slack channel and I feel like they treated us as part of their team and we treated them as part of our team.
 They came inbound they sent an email based on the website and they said hey we would need mutable indexes and glob and a couple of other things so it's like well that's a very reasonable request right and I think they had the conviction that this was the right architecture and like if we could prove in their trust and then be able to be in a good place so it was really just a it was just an oneness conversation just the way that the website is today a very honest description of what are the trade-offs what can it do what can it not do what is the latency profile what are the guarantees and that's exactly the kind of bullet point discussion that we engaged in over email before I met the team in person yeah and they of course they were a small team at the time right it was and they needed help with the with with parts of their infrastructure and working very very closely with teams that they could trust with the right economics and the right the right reliability.
 Yeah for sure but I guess that honesty which I also value a lot you know and in my work as I became a product manager you know three years ago and I think it applies to any discipline be honest but but you know like that honesty probably lies on the fact that you you've done your napkin math and you knew where this will scale where how this can go right how did you go about doing that pre-launch right before having any client is that the company of your friends that helped you to kind of like figure out the economics and sort of the the throughput and all of these rigorous questions that you ask you know as problem statements on napkin math.
 I think that should almost bring up the internet archive version of it the the first version of TurboPuffer I had not thought about the business at all I didn't have any launch playbook I had I had one of course all the economics of what it would cost me to operate and spend a decent amount of time on the pricing because that felt like an important thing to spend time on at the time but there was really not much more than that of course the the Readwise team was very interested but at the time I could barely do a you know I could just do around 10 million factors which is not enough for their use case.
 I can screen share the website with you right here of what it looked like at the time and then we can get for the for the for the listening audience we can get your reaction but it was it was very simple I wouldn't I wouldn't put in any sophistication and it was honestly I was exhausted I've been working on this like completely alone not telling anyone about it no interested customers for like four months extremely focused like every single day and I couldn't like you ask my wife she would say I was very distracted and she's just like well how are you working so hard on this like there's no one on the team you don't have any customer line up and I'm just like someone has to do this and I I just launched it and I launched it I mean now I feel some verising would be did launch it just couldn't do that launch it was pretty slow I spent a bunch of time actually trying to make it work in wasm and on the edge but it was too hard to make it fast and a bunch of other false starch like that on different types of a and end indexing structures we could talk about that as well and would be settled on but there was no real sophistication in the go to market it was really just here it is here's the outcome math here's what it does let's see how the world takes it but I think when when when you sit on a well you didn't sit on it yet but you had a cool like technology ID and mind right you knew you know it may play out but also of course it required a lot of hard work like you said but after that after you see it fly like on some small scale or whatever scale I think that brings you like that excitement to bring it to the world right so yeah I see you're sharing the screen of the of the web archive page yeah that's it very simple yeah yeah that's awesome but yeah that's actually a good segue to you know you probably know I've been at the emergence of the field of vector database field I've been I think I was the first probably to write just a simple block post with like you know these crump snippets of what each vector database did and how they stand out and so on turbo buffer wasn't there because turbo buffer was still in your mind I think but but the segue here is I don't have it covered in that block post but in your mind why were you not happy with the vector date is like at large did you try all of them did you try some of them why did you think that a new vector database deserves to exist yeah I think I think it really just came back to the read wise example right there's I there's they look like great products I really like the API of many of them they had lots of features that have taken me a long time to build that even features that we don't have today although we have a lot of features today compared to when we launched it came out of the cost piece that it felt that there was a lot of latent demand built up in the market of people who wanted to use these things but it just didn't make sense with the economics it's very difficult to earn a return on search I mean I remember the search clusters that Shopify were very expensive but ecommerce is a lot about search and so it was okay right but for a lot of companies search is a an important feature but is not the feature right and so the per user economics just have to make sense it's not that everyone just wants it in the cheapest possible way is that if you invest in infrastructure you have to get a return on that investment and it felt that I knew that I'd read wise they could get a return on that investment but it wasn't on 30 grand a month it was maybe close at a 3 grand or 5 grand a month that they would feel that they could earn a return on that feature and gender conversion engagement and whatever so it was really about the storage architecture and I think that when I think about databases now this was not as coherent to me at the time at the time I was driven by the Nipkin Math Naptkin Math not the not the market nothing else it was based on one qualitative experience and an Naptkin Math there was nothing else in it and speak about it in a more sophisticated way now being you know having learned a lot about go-to-market sense but the that those were that's really all that was at the time it was an insight on those two things the best ideas right are simultaneous inventions right someone else would have done it six months later probably other people were doing it at the time that launched a later right we were the first to launch with this particular architecture but it was out there for the grappling right the idea was in the air like s3 had the the dpites now finally so the way that I think about this to really boil this down is that if you want to create a generational database company I think you need two things you need a new workload the new workload here is that we have almost every company on earth sits on their treasure troll of data and they want to connect that to LLAMs especially all the unstructured data that it's always been very difficult to do we did this for structured data into 2010s the new workload was that we wanted to do analytics on billions tens of billions trillions of rows of structured data but now with LLAMs we're entering into that with the unstructured data that's the first thing we needed new workload because that's when people go out shopping for a new database the second thing that you need is a new storage architecture if you don't have a new storage architecture that is fundamentally a better tradeoff for the particular workload then there's no reason why tacking on a secondary index to your relational database to your OLAB to your existing search engine they would eat it I would have made that decision in the shoes that Shopify right it's like well this database like has a really good vector index but it doesn't bring anything new in terms of the storage architecture so we're just going to invest in the mySQL extension right it's what we really want to Shopify or the uh Lucine Lucine workload right these are great databases they've stood the test of time and when you're on call you become very conservative in what you adopt for new workloads but you cannot ignore a new storage architecture that is an order of magnitude cheaper than the previous one when you store a gigabyte of data in a traditional storage engine you have to replicate that to three disks maybe two if you have a little bit or if you have more risk tolerance but likely three a gigabyte of disk with from the cloud vendors cost about 10 cents you run it at 50% utilization otherwise it's too scary to be on call 20 cents per gigabyte times three for all the replicas 60 cents per gigabyte obi storage is two cents per gigabyte right so it's it's it's 30 times cheaper if it's all cold now by the time you have some of it in SSD and you have it in memory then the blended cost ends up being different but it tracks the actual value to the customer even if you have all of that in disk well you only need one copy right and that disk you can run it at 100% utilization meaning the blended cost is now 12 cents per gigabyte right so the 10 cents 100% utilization plus the two cents per gigabyte for obi storage so now you have the ingredients of a new actual database you have a new workload right which is which makes means that people are out there trying to look for ways to connect their data to LLMs and then you have the second ingredient which is a new storage architecture that allows them to do it in order of magnitude easier and cheaper than what they can do when they're existing architectures and this matters because vectors are so big right a kilobyte of text easily turns into tens of kilobytes of vector data yeah yeah it's absolutely true one other thing that I kept keep hearing or kept hearing about you know whether or not to introduce a vector search in the mix for some really heavy workloads is that it will bring certain latency on top that we cannot tolerate right for example if you run a hybrid search like you guys have implemented as well you know one of these will be slowest and therefore you will have to wait for that slowest component and so if it adds I don't know a few hundred milliseconds on top of your original you know retrieval mechanism then it's going to be an off-line what's your take on that have you thought obviously you have thought about that what's the edge that turbo buffer brings in this space over maybe pure databases yeah I think I think there's we see two types of ways that people adopt vector databases or turbo buffer we don't consider turbo buffer a pure play vector database we consider it a search engine we actually consider it a full database because there's a full generic LSM underneath all of that and we consider that the actual acid of turbo puffer is an LSM that's obnox storage native and doesn't rely on any state we just think that the vector index and the search engine index is what the market needed the most so let's speak about latency there's no real fundamental latency trade off with this architecture the only thing is that once in a while you will hit that cold query but the entire databases optimize the round minimizing the amount of round trips that you do to SS3 S3 you can max out a a network card right so you can get on a gcp or AWS box you can get 50 to 100 gigabytes per second of network bandwidth you give it per second of network bandwidth so this is similar to this band with the latency actually even better in the clouds often than disks even with SSDs even with N and NVME SSD so the network is phenomenal you can drive you know say you can drive all of that data you can drive gigabytes of data per second in a single round trip so you can get great throughput but the latency is high the p90 might be around 200 milliseconds to s3 for every round trip someone regardless of how much data that you transfer assuming you're saturating the box we've decide almost everything interval buffer around minimizing the number of round trips to 3 to 4 that doesn't just help for s3 it also helps for modern disk which the same thing you can drive enormous amounts of bandwidth but the round trip time is is long right it's like a hundreds of microseconds versus hundreds of milliseconds but still still substantial compared to dm so the latency tradeoff is not a fundamental tradeoff with this architecture by the time that it makes it into the memory cache it's just as fast as everyone else we have found that people don't care if it's like a millisecond or five milliseconds as long as it's reliably less than around 50 milliseconds they're good right and I think that a lot of the traditional storage architectures especially because of the sharding structure with multiple nodes you're already in a worse position than going to two systems where if you write a query on some of the traditional search engine generally you touch five ten maybe more nodes depending on depending on this because the shard size is very very small you go into more depth on that so you already have this problem what we see is that there's two types of ways that people adopt it so the first one is you have an existing lexical search engine you are having a hard time running it because of the traditional like very stateful architecture and they're reputed for just being difficult to run and you're like already a little bit add your threshold for the amount of money that you're spending on this cluster and if you put the vector data in it's often 10 to 20 times larger than the text data it is just it's a project that stops in its tracks similar to the read wise case that I mentioned before so for those players we often see that they have something that's really well tuned for the lexical and they adopt a vector store and then they do two queries in parallel the vector store should not be slower than the lexical right so these are just two futures that you merge together in use and in general we see that our customers are actually quite happy to move some of the ranking and the final like second stage ranking out of the search engine and into a search.
py instead of a big search.
json which can be very difficult to maintain many of these companies express a lot of desire to move more and more of their lexical work also onto turbo buffer and we have a full tech search engine we don't have every feature of blue scene yet but we're working very very actively on bringing this up what we also see is that a lot of our customers don't need all of the features of blue scene anymore because the vectors are so good that a lot of the you know Ph.
D.
 level efforts we did before to turn strings into things is not as much of an issue anymore and really what we use strings for more is that when you search for DM you get the metri right like like for a prefix match whereas an embedding model might think that that's a direct message those kinds of things are important and we still need string matching for that lots of applications needed but there's a lot of things that we do in leucine with synonyms with stemming with all these kinds of things the team models are frankly just a lot better at so we find that this is an adoption curve that is there a lot of the newer companies just start with embedding models and simple full-text search and and they get it up and running on turbo puffer and they like that they just pay for what they need they don't think about it and they could pump a petabyte of data and if they want it and it would be extremely competitive on pricing and they don't have to think about it oh that's awesome that's awesome actually I forgot to mention I forgot to ask you which language did you choose to implement to revolver on yeah we we um well it was just me at the time but I chose I chose Rust and I think I spent the majority of my career writing Ruby at Shopify and and then a lot of go as well for some of the infrastructure components and then mainly debugging C which all the databases that we were using were we're doing and reading C I I really like go and I like go alongside Ruby at Shopify because go was one of those things as when leading teams I didn't have to worry about whether someone knew go or not because the adoption to learn it is two weeks um the adoption to learn Rust and being proficient in it is months right and somehow that's written Rust for two years it's a lot more productive than someone who's written it for two months in the language um and that's just not the case for go like someone who's spent two years in it is just not that much more productive and so and I think that's an amazing feature of the language but from from my own point of view and from the napkin web math point of you I just I was always so hungry having been in time inside of runtimes in the Ruby MRI runtime and then inside of the go runtime I was just hungry to just get directly connected to the metal of the machine and so and for a database in particular that was very important right we need to vectorize everything we need full control over that and I think that I think that that full control as remarkable now as Go is which would I think it would be would have been okay that raw access to the machine has been has is needed for for writing something like TurboPover.
 Yeah for sure I still remember coding the times when I was learning and coded industrially in CNC++ like you like you really need it to be very very careful but in return you can get a lot of like performance gains you know and some of your ideas really fly but yeah today I guess I'm coding more in Python or should I even say that I called in Python when I use cursor more and more which is by the way scary you know the the that feeling when some some other entity writes code and you are just reading it right it's it's a little bit scary and I'm still grappling with it but the amount of productivity that I get is enormous and it's like you know I can shoot daily like features and just see them being used that's amazing.
 I think what I love about it is that I still love to sit there and write the additional code by hand you know maybe at some point we will we will we will mark TurboPover as an a seasonally written database because we don't use a ton of AI for the very key parts because I mean we're at the edge of what the LLMs could know but I think that for me in a position where I'm in and out of meetings all day these days but I can actually get a lot done in a 30 minute window when I have something that's prompting and writing the tests right and you follow it off at the beginning of the meeting you check in and they're like you know 15 30 minutes you have in between blocks and this allows me to actually contribute a lot more code than I was otherwise going to be able to not into the core engine you know I don't get led led into led into a lot of that anymore because I don't have the the time and focus that it takes to fully think something through there but for the website the API to initial features all of that it's just been wonderful yeah that's amazing I also wanted to go a bit on the tangent like you essentially you've been you could say mathematician engineer but you took a leap towards becoming a CEO right and I think you know as you said you go to meetings you do lots of you know probably sales and and and and product and all of that stuff was it a natural transition for you like what what have you learned in this in this journey and what what maybe do you miss from from your previous career when you when you were like you know hands on and sit down and write a bunch of code I think I have a I have a couple of angles to answer the question not necessarily a directing answer I think one one angle is that fundamentally I'm like a growth junkie for better or worse and I think that entrepreneurship is the ultimate path for a growth junkie it was never really something that I assumed that I was going to do I've never before even when I was working on the project it's never about becoming a founder it's just about creating the database right and at some point becoming the founder of the company becomes a means to an end of creating the database and getting it into the hands of our users and making sure they have a great time that's always what like that's what drove me right was the read why I should have this right our customers should have this this you have a great experience and that's always what's driven me and to me the the founder and all of the other things have been a mean towards an end there I think that one of the things that is maybe both a controversial but also feels like a true statement is that at some point I feel a bit numb to what work that I enjoy and what I don't enjoy anymore because what I enjoy the most is making this company successful and making the database successful for our customers that's what I care the most about and I'm yeah I honestly I love sales I love marketing I love the engineering I love hiring people for the team I love all of these things but it's not a simplistic answer to oh I've been coding my whole life I think it's more that that is my idle activity if there is that one to two hour and there's nothing urgent on then I'm going to go spend some time in the code it's like oh how did how did Nathan implement this new this new query planning of query plan or heuristic that is a natural that's where my idle activity and I always like to also an interviewing people try to understand especially if they're in a more hybrid world what's your idle activity what's the thing did you do when you have one to two hours and nothing else comes up do you gravitate towards the code do you start looking at just start writing an article do you start playing with the product what is that idle activity and it is code for me that's what everything is grounded in and I think it I think it has a deep influence on how I can how I can lead the company but I don't think it's been I think I often think about something that tell them said you know the author of anti fragile and a bunch of other books is that you the best authors of books are not the ones that sit down and like you know read a bunch of papers then write a page then read another paper write a page the best books are written by people who just you know go to the cabin sit down write 500 pages and and hit publish of course that's not what actually happens but if you read it to let books it's probably pretty close to what actually happened and he just has the citations in his head and I think about that often when building this company that it has felt like I've worked or this my whole life without knowing for it and I feel every every morning that I wake up that this is exactly what it has led up to so it's very naturally even if it wasn't go onto itself that it makes sense with the experience I've had to do exactly this and I tremendously enjoy it but it's not a simplistic answer to do I miss coding no I want to make this company incredibly successful but sometimes I will do it as a recreational activity yeah I mean definitely like when I look at you like on twitter for example you come across as a very technical person and you are for sure right even though you know that to grow your business you need to do a lot of other activities but at the same time I mean yeah I don't mean to ask it in a way that hey you regret now that you do sales you regret not doing more coding which which is not true you still do that and I think that all of all of the engineers will become better engineers if they learn the mastery of actually presenting what they do right and then they will not need a middle layer or someone else who will go and talk to that product manager or whoever else needs to talk to right so they can actually represent themselves but also I also love how you put it really eloquently that what is your idle activity right what do you what's your affinity what you gravitate to and I actually can it resonates a lot with me because my idle activity that I'm really nervous that I do nothing especially on vacations I start coding you know I just go and just okay let's just let's just hypothesize about something but let's let's dial back for for the into the architecture like when I look at the architecture page of turbo buffer it's very simple it's like client connecting over you know TCP to a database instance and it has just two components they are memory or SSD cache and the object storage tell me a bit more so I think our listeners and I mostly know what object storage is but tell me a bit more about that memory component like what algorithm design went into that maybe trade-offs and you know how frequently you need to do the round trips to the object storage versus when we actually don't do that yeah I think it would be easiest to do this by speaking about the lifetime of a request as the cache worms so we we'll actually start with the right path and when when you do a right into turbo buffer it's as simple as you can imagine it I mean at this point we've optimized parts of it that it's not this simple but this is the the best way to explain it when you when you do a right to turbo buffer that right basically goes into a file in a directory called the right ahead log so when you write to a namespace you can imagine that on s3 it's like slash namespace slash you know right ahead log the right ahead log is basically just a sequence of all the rights in order the raw rights so you do your right and it might be okay I'm inserting a document with text the metri and one with text Simon and those are the two documents you can in the simplest way you can imagine that this file is called zero job JSON and the next one is called one dot JSON three dot JSON that's a database right that's just the right ahead log and if you want to satisfy a query you just scan through all the JSON documents and you satisfy the query that's actually respectable database and it's not even that far from the first version of turbo buffer but of course you have to index that data as well so basically as you can imagine once many megabytes of data come in asynchronously an indexing node will pick it up and put it into the inverted index for full text search put it into an a and an index for vector search and put it into a attribute or filtering index for other attributes and there will be other indexing types in the future when when that happens it will put it into slash namespace slash index and just start putting files in there right and then the query layer can then consult those files right instead of scanning through every single document to find a metri you can just plop in and look at the metri in the inverted index find the document and return it that's how right works when a right happens it will go through one of the query nodes and the right will be also written into the into the cache right so both the memory cache and the disk cache and when so when you do a query you will go to that same query node right there's a consistent hashing so if there's three it's sort of like the same namespace will end up on node one all the time if it hashes that I know when you've satisfied when you when you do a query it will first take the cat check the caches if you just did the right well it's already there because we just wrote all the rights into the cache to have this you know the right through cache and and we will satisfy the query mainly from the cache if for whatever reason this namespace is not maybe you did the right a month ago and so it's following that a cache and you do the read well then we'll read through cache by going directly to opix storage with its few round trips as possible to get the data to satisfy the query both from the index and from the wall will do range reads directly on s3 right the old like hcp range header to get exactly the bytes we need to satisfy the query and then start hydrating the cache on the on the query node so the subsequent queries get faster and faster and we can do that a gigabyte per second we can hydrate the cache even for very very very large namespaces so that's the general architecture of turbo puffer on a completely cold query it takes hundreds of milliseconds and on a warm query it can take as little as 10 milliseconds to to satisfy the query the the last detail I'll point out and then we can go into a particular aspect of this is that turbo puffer has chosen to do consistent reads by default this is an unusual choice for search engines we've seen doesn't do this unless you turn it on explicitly I think they've done more work now for real time indexing which to me is the gold standard which is why I keep referring back to it's phenomenal piece of software and turbo power requests consistent reads by default meaning that if you do it right and then you read immediately afterwards that right will be visible and in order to satisfy that we can't just rely on the cache on that node being out of date that node could have died it could have you know the hashed ring could have moved because we scaled up so every single um query we go to op storage and see what is the latest entry in the wall and do we have that entry right is it at 3.
json or is that 5.
json and do I have that so we have a little pointer file that we can look and we can download and look at right and that round trip is basically our p50 like our spans are basically you know often like one to two milliseconds of actual search and then on gcs about depending on the region 12 to 16 milliseconds waiting for that consistency check on s3 the small obnoxiously it's a little bit better so it's eight milliseconds but you can turn this off and you will still get up to you you can get eventual consistency that's very normal for these databases like could be up to one minute out of date and then you can see often less than a millisecond or a millisecond latency to a turbo buffer by turning off that check but we find that this is a very safe default and I think that database should ship with very safe and unsurprising defaults yeah for sure for sure um so in that cache but you also have the you also have the let's focus only back to search part for now you also have the a and n index is that also stored on s3 and then is it do you also keep kind of like a replica of it in memory to to quick access and how do you sort of it's true how do you sort of synchronize the two both the right-ahead log and the index are everything is stored on s3 if you killed all of the compute nodes of turbo buffer in all of our clusters we would not lose any data there is no data on the compute notes that matter it's only transient caching but we cache everything yeah if you're accessing the index will cache the index if you're just accessing the right-ahead log files because it's so small or there's parts of the data that hasn't been indexed then and that's also on s3 and goes into the same cache with everything else right prioritized by the workloads to try to get the best performance possible yeah it's quite smart so effectively you like I remember like at some previous companies when I was running Apache Solar one of the problems was always that all of these charts are super cold because they're never used right we still pay for them but then when the query hits you incur so much latency that's super painful and so I was always coming up with these ideas what if I run some you know post indexing warm-up script that will go and shoot a bunch of queries to all of the charts just to keep them you know up and running and and warm or just cat all the indices on Linux into memory we've done that too that was like 10 years ago or so that was very strange feeling like why do I need to mess with that level of detail it never actually paid off I think what pays off is a most smart way to organize your index and how you read data backwards like essentially when you users really only need fresh data first like on Twitter for example everyone is really after the recent tweets and not some archive and that was very similar case for us but it's very interesting like you go into so much detail there to to make the database effectively like a living organism adjusting to the usage but you also you also have multi-tenancy right so meaning that the same the same turbo buffer deployed across the data centers is going to be used by multiple companies at the same time unless they demand an isolation how do you think about that when they use the same effectively in the same instance compute and index I'd love to go into the solar example for just one second before we go into multi-tenancy how slow were those queries because when you say it cold you mean that it's not in memory when I say cold I mean that it's on S3 what kind of latency were you seeing that you had to do this work on it was very slow first of all the it has to do also with the domain specificity you know the the queries were Boolean and very long and so they they would take sometimes just a query itself would take a minute to execute on now like a regional index design and that was like just super crazy right but it was also very accurate because it was like sentence level search and then I had to design a new system new architecture where we could retain the accuracy of that engine but not have to spend so much money on on on indexing individual sentences so we indexed one complete document right so I had to change the algorithms slightly and so it went to sub-second it was still I think it's still slow right but it was much faster and and users started like like we could scale the company effectively after that right with one minute and 75% of infrastructure costs were like you know shaving off so but that's that's that was part of the Lucine you know munging with the algorithm and changing how it scans the document it had nothing to do with the level that you go into you know with turbo buffer you know like effectively controlling the whole the whole process there got it yeah I think the the point I the the point there is that I think we do see that some customers are concerned with with this cash because they've gone bit and by basically the the way that I would think about it is in in some of the traditional engines the way that they do IO if something is on disk it feels like it's bad like if it's on disk it's slow and it really has to be in memory and so you sort of have you know the pufferfish is either you know the pufferfish is sort of because when it's fully inflated it's a DRAM right it's a deflated it's in s3 well it only had two settings right either it's in disk which is quite slow and frankly in some of the traditional storage engine I've seen the latency on disk being similar to our latency on s3 yeah and so then you have to load it into DRAM and what a lot of these traditional databases they have to do a full copy into DRAM they can't just like zero copy off of disk and in the disk are also quite slow these old network disks right the NVME disks are so fast right they are they can drive bandwidth that's within you know a very low multiple of DRAM right tens of gigabytes per second but their cost is almost and two orders of magnitude lower so this completely changes the economics but you you can't take advantage of these very easily you can't just put as some software on it and just it's going to be like 10 times faster than an original disk even if it's fundamentally capable of it because what we found for example is that we had to remove the Linux page cache because the Linux page cache cannot keep up with these disks so you have to do direct dial but when you do direct dial you don't get coalescing you don't get all these other things now you have to write your own IO driver right and so you just databases have not been built to take advantage of it because they're also like they're not built to try to do an IO depth like basically so many outside standing IO requests they can they can drive there's a lot of throughput so there's just a lot of barriers of entry there so what we find is that when again speaking in generic terms here of like you know millions of vectors query that once when something is in disk it's maybe high tens of milliseconds mid you know 50 70 milliseconds when it's fully on disk maybe lower depending on the query the machinality whatever and when it's in memory it's closer to 10 to 20 milliseconds right so it's like these are not this is not bad like the user is barely going to notice it and but of course you're going to get more throughput that way and then means it's on s3 it's maybe more like five to six hundred milliseconds it's sort of user would notice but a lot of our customers like notion for example when you open the q and a dialog and these different dialogues that will query turbo puffer they will send a request to tell turbo puffer hey can you start warming up the cash here in a way that makes sense and by cash we just mean putting it into disk and starting with sort of the upper layers of the an index and other things to reduce the time as much as possible so there's a lot of things that can be done here that are very very simple that means that the there's there's there's barely a trade-off yeah but we let's go back into multi-tenancy unless you had a follow up let's do that yeah let's do that like how do you use a multi-tenancy part so so turbo puffer can run in three different ways it can run yeah multi-tenancy clusters that's what I mean that's what cursor does that's what that's what linear does and many of our customers so in multi-tenancy you share you share the compute we can do this so cheaply right because we can share the caching can share the we can share all of this infrastructure it's very easy for us to run this way so that's the default mode the cash is of course segregated off in in in in in in different ways but is also like shared in ways where you have a big burst the traffic rate you get more of the cash than others so that's what we so it's a very great way of running multi-tenancy the other thing we do for multi-tenancy to keep it very secure is that because all the data at rest is in the bucket you can pass an encryption key to turbo puffer that we don't have access to unless it's audit logged on your side where we can encrypt and decrypt the object which is logically and from a security point standpoint equivalent to you having all the data in your bucket so this is a very nice primitive that for example linear it takes advantage of because they have full control over their data they can see when turbo puffer is accessing it they can shut it down at any point in time and they can even pass that on to any other customers where turbo puffer can encrypt data for linear customers on behalf of the customer with the customer's key it this is like really really I think groundbreaking and underrated in this architecture you can of course do single tenancy with turbo puffer as well with the computers only for you you can do b y o c where we run to recover inside of your cloud in a way that's like very compliant we can never see customer data but we find it in multi-tenancy with the encryption which can be done per namespities satisfies the security requirements of even some of the biggest companies in the world yeah that sounds awesome I also wanted to pick one topic which usually used to I don't know if any more I don't see that as much pick up a lot of flame discussions what is your recall at n and when I go to the docs of turbo puffer it says recall at n is 100% recall at 10 excuse me but vector search bar so does that not 100% we said 9200 right no I think it says what wait wait wait I'll need to what was the page where you do that oh here the limits oh I see observed in production yeah it should say up to 100% that's a bug in the docs that I shipped last night I'm gonna I'm gonna fix that after this awesome but what it says in the in the limits is 90 to 100% but let's talk about recall I'd love to get into recall so I think recall is incredibly important it's the equivalent of your database you have to trust your database to do it in the same way that you have to trust your database do f sync and you have to trust your database that when we say that hey we don't return a success to you unless it's committed to s3 you have to trust that recall is similar right if you are working on search and you're working on connecting data to llem's then you don't want to worry in your e-vails on whether your vector database is giving you low recall it's actually a very sophisticated problem to evaluate whether this is the cause so you have to trust your vendor this is an underrated problem and I love that you're asking about it and very few people ask about it unless they're quite sophisticated so let's go into it let's go into a long answer here for your audience because I think this is paramount most databases that have a vector index are trained on or not trained on but they're benchmarked against for these different A&N open source projects so there's sift and others problem with these data is that they do not represent what we've seen in the real world a lot of them are very low dimensionality like when we do benchmarking on a billion that we're working on right now the biggest data sets we can find are like 64 dimensions this is not what people are doing in production they're doing at least 512 often generally I'd say the average is around 768 dimensions these are not representative data sets and the distributions in the academic benchmarks are also completely different for what we see in real data sets right in real data sets we see millions of copy of duplicates right we see filtering all these chaotic environments that do not present themselves in the academic thench works so if if you're using a vector index that's only been tested on academic benchmarks it's it's I mean it's like the LLMs right it's like you don't you don't really trust it just based on discording it's sort of you it's all the vibes right it's all the qualitative thing right outside the benchmark was that everyone was dreaming on them that it will work for your domain right like the LLM that's right like early on very very early on in in in interval puffer's history in the first month I was mainly iterating against the SIFT data set right just like 128 dimensional data set I didn't know anything about an end at the time so it's like okay this is pretty good we can tune some risks on this and then I can do go wider but I have the feedback loop and the observation I had at the time was that I found that one I so I got something that worked really well great heristics on SIFT and then when I went it on the other data sets it just completely did not work well or generalized to the other data sets and I think that taught me an early lesson that the these academic data sets are just not enough and the only way to know what your recall is going to be is to measure it in production this is what TurboPuffer does for a percentage of queries it depends on the number of queries that you do but let's say around 1% of queries TurboPuffer will run an exhaustive search against the A&N index on a separate worker fleet we will then emit a metric to data dog that is the recall number right for this query right like which is basically okay this is the top 10 we know is accurate and this is the you know heristic A&N index is what's the overlap and we will average that over time I have a graph in data dog that shows all the different organizations that have more than 100 queries in the in the past in the past hour or whatever and then we have the recall for all of them we have the recall at what they asked for to recall a 10 the p10 recall the p90 recall and we try to our best to make sure that this is green at all times and we consider green anything above 90% is generally quite good it well 90% is is quite good for some queries but for simple queries often it's closer to 100% many of our customers have have 99.
5% recall so this is the only way that we know to do this and it's fun you ask this question today because last night I was I was hacking on putting this into the dashboard so literally putting the recall that we observe from this from this monitoring system into the dashboard of the user because we think it's that important and it's very difficult to get right we have spent thousands of engineering hours to make sure that the recall is high now recall on academic benchmarks easy recall on raw ann search is especially on academic benchmarks very easy raw recall on production data sets I'd say medium to medium hard high recall on ann queries with filters with mixed selectivity and incremental indexing absolute hard mode this is what the like you just slap a secondary vector index onto an existing database this is what they can't do they can't sustain them like a thousand writes per second with high recall in the face of very difficult filter queries so let's talk about filters recall for a second there is barely any academic data sets on this yet it's all the production workloads what a filtered in an index means is that let's say that for example you have you have an ecommerce and you're searching for you're searching for I don't know yellow right and you want to only get things that ship to Canada that cuts the clusters in different weird ways that might end up with a selectivity of 50% and so if you just visit the the closest whatever vectors with some horrific you have you're not going to get the true ann because you actually have to search maybe twice as many maybe three times as many vectors to get the right recall the query planner the thing in the database that decides where to go on disk and figure out the data and aggregate it altogether and return into the user needs to be aware of the selectivity of the filter and plan that into the ann index again if a database is not really serious about their vector offering they're not doing this they're not measuring in a production they're not they're not willing to show their users and they're not they don't have a full infrastructure in place to measure the recall so I'd say we take this extremely seriously and we don't want our users to have to get to get to guest this and it's a it's sometimes a thankless job because because many many many many emails that we see against some of the other vector indexes have very low recall and and how are users supposed to know because running these running these tests is extremely difficult it is and it's like it's as you said like you need to trust there right trust your vendor and it's basically like the like in some documentation pages you say the floor or like the bottom line right like the needs of each it just doesn't make sense right if the quality isn't there then why are you even running this it's a difference between you know finding that product with those constraints when it exists and actually not finding it right therefore not buying it and so on and so on and so forth it's right and I think yeah I you can never guarantee a recall you can observe what you are trying to make it be here on every data set but if you send a billion completely random vectors with 3000 dimensions and try to query them in turbo buffer with query vectors and there is no natural clustering because they're random vectors you're not going to get 100% recall when you send that with a 10% selectivity filters that just like completely breaks every heuristic that's made right but all data in production real data that people want to search has some natural clustering to it so that's not a real benchmark that you can evaluate recall on right and so we always take this seriously and the in the in the in POCs and with the monitoring we do we're looking at these numbers all the time but there are like absolute edge cases that can be very very difficult and what you have to do too as a database vendor is like it's a tug is a tug of war between we're going to look at more data to try to get high recall and we're going to try to improve the clustering of the data so that we have to search less data and so you're always trying to improve the clustering and you're always trying to improve the performance of the database so we can look at more data to get high recall yeah for sure I know that you mentioned about filters you know challenges vegan and I don't know if you aware of those the reason an end-end benchmarks right but there is also a big end-end benchmarks that they happen to pleasure to participate in they have one of the datasets one of the tasks they have is the filtered search I have not participated in that one but again as you said it's kind of like academic but some of the datasets are quite logical like beaten points dimensions and not that huge it's like that's the thing there are 156 yeah it's not like yeah there are hundreds of 200 dimensions these are not real data sets like no there are real data sets but they are real data sets from the past generation of vectors right the the pre the pre current modern embedding error right which are just scores so much higher than these so we just don't see people use these yeah yeah exactly it's still fun to participate in this benchmark by the way because the data is there and you know the some of the guarantees that you need to hit really high you know like thousands of tens of thousands of queries per second so if you can create a toy index that works just a proud moment I guess that's right but I would say that people don't care about these bench like now people care about the benchmarks like their fun competitions but I think it can ruin your company if all you're trying to do is maximize these benchmarks because how many companies on in the world are trying to do 10,000 QPS on a billion vectors right not that many but there's a lot of companies that have a billion vectors lying around that they want to search and they just don't want the pricing to be offensive right we're a turbo buffer can you do this depending on the dimensionality for like a thousand dollars in month that's what people really seem to care about yeah sure maybe if I ask you like a spicy question if I may why do you think some of the vector database players like in Dalgium cells into that game of showing the benchmark and telling we are the best and then you know someone else cuts them over and says no you made a mistake in the benchmark why do you think this is happening like like publicly if you're comfortable talking about this yeah we we don't we don't publish benchmarks against anyone else in in fact it's it's it's usually against the terms of service to do that for almost every vendor including the big vendors like the hyper scalers probably shouldn't be it probably should be prohibited for the hyper scalers for like any competitive reasons or but anyway for the peers I think it's it's like a low blow because everyone can sort of p-hack their way to something where they they go better and becomes like month throwing and it's very distracting activity um we benchmark ourselves in ways that we find that our customers are actually using the database so we're not doing it at 10,000 qps because it's just not what we see to a single namespace um so we benchmark against ourselves we benchmark against first principles and we're always considering what is the gap between what turbo puffer does and first principles there's that's what I've learned that's why I do napkin math is because the fundamental thing you should be benchmarking against our first principles there's a gap between what the DRAM or disband with it is multiplied by how much if it you need and your database is not doing that well then you either have a gap and you're understanding or you have a you've found room for improvement that's what matters and of course it also matters what other people are doing but what matters the most is what your customers are trying to do and they'll they'll pull you in that direction so we think that this is a this easily becomes one of these metrics where you know if you give people a metric they'll optimize for it um and benchmarks of how many qps you can do at some number recall it's just not what people care about um they care about it working they care about enormous ride throughput they care about costs they care about other things necessarily that are much harder to put in such a benchmark um I think benchmarks are important like we need to give people a sense of what they should expect and they should hold us truth at that and what I would love to have is like more absurd ability in the turbo puffer product of like what kind of like performance are you seeing um we're working on you know explaining um our exposing query plans from turbo puffer right so you can see um well what's what's causing the indexing uh sorry what's causing the the query latency to be what it is so yeah I don't think the mud throwing is great um I think that at some point someone's going to publish a benchmark with turbo puffer and um and and again something else and and then we'll have to deal with that as it comes right um by um but it's certainly not an activity that we plan to engage in yeah I love your answer because it also resonates with me like in a different dimension you know I found myself in a situation when at some point in the past when um we've been copy copycatted I can't be say in that way so there was a company that really literally copied the whole interface and it like how how the product looks and we felt threatened but what they couldn't copy is essentially the internal IP right all the algorithms everything where we've spent hard hard uh working time on you know they couldn't copy that and and effectively that doesn't fly by itself right so so basically what I'm trying to say is that you know even though it felt threatening still thinking about what you need to solve right by the laws of physics you really need to focus just on that and if you solve that you become the leader of the market and that's what happened to the company actually it the story was that it actually acquired this copycat right and that's it uh I mean it doesn't mean that's the bad thing bad outcome for either of them but what I'm trying to say is that just focus on that on that thing that you're trying to solve and don't try to indulge into these you know games of like you said you know not throwing and stuff I like that really well said yeah that's I think I think so we focus on on customer studies we focus on we focus on on first principles we focus on benchmarking and we focus on on what are customers telling you telling us that they need and I think that um I think those are the right things to focus on for our company for sure and and and just looking at the clientele right the the ones that you shared just just knowing those names cursor and and notion that everyone is pretty much using every day that's like a testament to what you've done um I also wanted to ask you before we close I wanted to ask you about what are the maybe technical or business or some other challenges that you see ahead of yourself or maybe that's what already is happening and you see that it's important especially in this space of LLAMS where LLAMS can bring value um what is it it feels like you you have wildly successful as a business and as a technology but is there something that you see is still unsolved and and is ahead of you and worth solving I'll go back to a you know I spent a long time at Shopify and so part of growing up at that company from when I was very young was being taught a bit in the school of Toby Lukay the CEO and something that he often said is that you know you about himself is like you have to grow to keep up with the business and that's that's what it is for me as well right I um first had to grow as an engineer to put out the first version um then I had to build an engineering team to take it much further than I ever could alone and I think we have and just an absolutely like 99% college engineering team now then I turned my focus to sales and learning that and now I turn now I have to turn it towards marketing towards legal towards all these different things to build the company I we spoke a little bit about this about this before um about I think that one of the beliefs that we have is just the town density of the team and I don't think there's a lot of I think that a lot of people talk a lot about the town density and I think that there is um now a generation of companies that's really trying to do it um I think that um the tools that we now have available to us and especially the kind of tool that we work on every day um the floor for productivity has been raised but the ceiling has been raised far more and so what really matters to us is having a team of individuals that where everyone is is a player right we see these teams as a symbol of almost more like sports teams today um then how companies were originally uh originally built um and I think that we we hold that as a as a strong belief in how we we um we are building the company but it demands a lot from everyone to work in this way but it's very fun um and I think that the the growth that that embodies on everyone including myself is important and I have to keep up with that I have to keep up with the demand of of of how our customers and our team internally and everything grows and that's that's the biggest challenge is just the amount of new that has to be learned um so that we can become a successful company which is is important for me for our customers and for everyone who's chosen to come along for the ride and join the company.
 Oh that's awesome yeah this field changes so quickly um it it felt much slower when I was coding myself you know Java you seen all that stuff you you had like solar elastic search that's it for like long time and then a lot of new engines popped up especially when vector search appeared on the scene but now with the LEM advancements and all of that it just feels so crazy so yeah it's very interesting challenge for sure you know personally and business wise and and team wise and yeah and and keeping balance is another one.
 I think the pace of the pace that we see everyone running at now in the successful companies is beyond anything that I've seen before um it reminds me of of just the the the months leading up to black friday at Shopify but it's all the time and I love it I'm addicted to that pace and I think that we have created a team of people who seek intensity and that's exactly what we think that we need to create the right product at a pace that makes sense for also our customers so the day are never bottled next on us and that is what keeps me up at night.
Oh that's awesome that's great cause. We usually end with some sort of announcement anything you want to say to the audience especially now that you said that you want to go deeper into marketing it beats your chance anything that you want to share all call for.
 I think that we we we we've refrained from doing any large releases and we try to just ship as rapidly as we possibly can if I look at the change log this month it's um I mean we we launched to we launched the region the Singapore Canada we've added the float tight uh we've we've recently added clients for Java Go Ruby um one of the things that I think is is really exciting is our conditional rights and this is where turbo puffer is not just a bunch of files on s3 it's not even just a search engine it could do conditional rights where you can say hey I only want to replace this document if it's newer than the old version right these are real database features and things like patch right where you do a partial update but we don't we we just we just launched and then we put it on put it on x and we move on um so I don't have any big announcement we went GA a couple a couple months ago it would have luck to have done that but we just tried to ship an announcement just get it out there as soon as possible move on and ship the next thing.
 Yeah congratulations on Jay on your original launch but on Jay I think it's a big milestone as well and as you said you're probably not as sort of transactional anymore you just keep shipping and you follow what the customers need and but sometimes some of these things may go and notice unless you know people follow exactly what you do and so in that sense I feel like there is a room or stage for saying hey guys go go use it it's GA right run your benchmark.
 I think now do they think about it been more I think one announcement might be that early and unintervaled puffer's history we were very focused on doing many namespaces that were small but we are getting very good at large namespaces now and we have customers that are searching billions of vectors at once and we have customers that want to search hundreds of billions of vectors all at once and we are working with them on that and this is not particularly scary anymore you know exactly what we need to get there so if you have use cases of that caliber you may have passed by turbo puffer before but we're getting ready and we are ready for hundreds of million and billions at once the only limitation there is the is really just the size of a single machine and then we shard over them but I think back to the sharding we had before you need to make every shard as large as possible to get the best economics and the best performance and that's been one of the issues with some of the traditional story tangents.
Yeah for sure.
 Yeah I really enjoyed the convo I know we could have gone and so many topics like I really wanted to ask you also about an an algorithms and stuff but I also I feel like we could talk more later as well you know down the road as you guys are progressing hopefully you'll be open to that but I've learned a ton and it's very interesting designed that you have and and the whole journey of you pushing for four months you know and interrupted I hope you now regain some of the balance back to your life now that you have the team supporting you but I really enjoyed this conversation Simon thank you so much for your time thank you Dimitri