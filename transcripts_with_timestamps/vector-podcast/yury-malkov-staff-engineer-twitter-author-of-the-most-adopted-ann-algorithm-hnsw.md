---
description: '<p>YouTube: <a target="_blank" rel="noopener noreferrer nofollow" href="https://www.youtube.com/watch?v=gvgD98jWrJM">https://www.youtube.com/watch?v=gvgD98jWrJM</a></p><p>Topics:</p><p>00:00
  Introduction</p><p>01:04 Yury’s background in laser physics, computer vision and
  startups</p><p>05:14 How Yury entered the field of nearest neighbor search and his
  impression of it</p><p>09:03 “Not all Small Worlds are Navigable”</p><p>10:10 Gentle
  introduction into the theory of Small World Navigable Graphs and related concepts</p><p>13:55
  Further clarification on the input constraints for the NN search algorithm design</p><p>15:03
  What did not work in NSW algorithm and how did Yury set up to invent new algorithm
  called HNSW</p><p>24:06 Collaboration with Leo Boytsov on integrating HNSW in nmslib</p><p>26:01
  Differences between HNSW and NSW</p><p>27:55 Does algorithm always converge?</p><p>31:56
  How FAISS’s implementation is different from the original HNSW</p><p>33:13 Could
  Yury predict that his algorithm would be implemented in so many frameworks and vector
  databases in languages like Go and Rust?</p><p>36:51 How our perception of high-dimensional
  spaces change compared to 3D?</p><p>38:30 ANN Benchmarks</p><p>41:33 Feeling proud
  of the invention and publication process during 2,5 years!</p><p>48:10 Yury’s effort
  to maintain HNSW and its GitHub community and the algorithm’s design principles</p><p>53:29
  Dmitry’s ANN algorithm KANNDI, which uses HNSW as a building block</p><p>1:02:16
  Java / Python Virtual Machines, profiling and benchmarking. “Your analysis of performance
  contradicts the profiler”</p><p>1:05:36 What are Yury’s hopes and goals for HNSW
  and role of symbolic filtering in ANN in general</p><p>1:13:05 The future of ANN
  field: search inside a neural network, graph ANN</p><p>1:15:14 Multistage ranking
  with graph based nearest neighbor search</p><p>1:18:18 Do we have the “best” ANN
  algorithm? How ANN algorithms influence each other</p><p>1:21:27 Yury’s plans on
  publishing his ideas</p><p>1:23:42 The intriguing question of Why</p><p>Show notes:</p><p>-
  HNSW library: <a target="_blank" rel="noopener noreferrer nofollow" href="https://github.com/nmslib/hnswlib/">https://github.com/nmslib/hnswlib/</a></p><p>-
  HNSW paper Malkov, Y. A., &amp; Yashunin, D. A. (2018). Efficient and robust approximate
  nearest neighbor search using hierarchical navigable small world graphs. TPAMI,
  42(4), 824-836. (arxiv:1603.09320)</p><p>- NSW paper Malkov, Y., Ponomarenko, A.,
  Logvinov, A., &amp; Krylov, V. (2014). Approximate nearest neighbor algorithm based
  on navigable small world graphs. Information Systems, 45, 61-68.</p><p>- Yury Lifshits’s
  paper: <a target="_blank" rel="noopener noreferrer nofollow" href="https://yury.name/papers/lifshits2009combinatorial.pdf">https://yury.name/papers/lifshits2009combinatorial.pdf</a></p><p>-
  Sergey Brin’s work in nearest neighbour search: GNAT - Geometric Near-neighbour
  Access Tree: [CiteSeerX — Near neighbor search in large metric spaces](<a target="_blank"
  rel="noopener noreferrer nofollow" href="http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.173.8156)">http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.173.8156)</a></p><p>-
  Podcast with Leo Boytsov: <a target="_blank" rel="noopener noreferrer nofollow"
  href="https://rare-technologies.com/rrp-4-leo-boytsov-knn-search/">https://rare-technologies.com/rrp-4-leo-boytsov-knn-search/</a></p><p>-
  FALCONN algorithm: <a target="_blank" rel="noopener noreferrer nofollow" href="https://github.com/falconn-lib/falconn">https://github.com/falconn-lib/falconn</a></p><p>-
  Mentioned navigable small world papers:</p><p>Kleinberg, J. M. (2000). Navigation
  in a small world. Nature, 406(6798), 845-845.;</p><p>Boguna, M., Krioukov, D., &amp;
  Claffy, K. C. (2009). Navigability of complex networks. Nature Physics, 5(1), 74-80.</p><p></p><p></p>'
image_url: https://media.rss.com/vector-podcast/20220131_090127_be85ef047356dd187c4b22fb3a9286be.jpg
pub_date: Mon, 31 Jan 2022 09:41:27 GMT
title: Yury Malkov - Staff Engineer, Twitter - Author of the most adopted ANN algorithm
  HNSW
url: https://rss.com/podcasts/vector-podcast/377082
whisper_segments: '[{"id": 0, "seek": 0, "start": 0.0, "end": 21.44, "text": " Hello,
  vector podcast is here and today we''re going to be talking to the author of H&SW",
  "tokens": [50364, 2425, 11, 8062, 7367, 307, 510, 293, 965, 321, 434, 516, 281,
  312, 1417, 281, 264, 3793, 295, 389, 5, 50, 54, 51436], "temperature": 0.0, "avg_logprob":
  -0.4366465210914612, "compression_ratio": 1.1458333333333333, "no_speech_prob":
  0.09332770109176636}, {"id": 1, "seek": 0, "start": 21.44, "end": 25.44, "text":
  " library and algorithm.", "tokens": [51436, 6405, 293, 9284, 13, 51636], "temperature":
  0.0, "avg_logprob": -0.4366465210914612, "compression_ratio": 1.1458333333333333,
  "no_speech_prob": 0.09332770109176636}, {"id": 2, "seek": 2544, "start": 25.44,
  "end": 32.0, "text": " It''s one of the best algorithms out there, one of the most
  used algorithms in vector search.", "tokens": [50364, 467, 311, 472, 295, 264, 1151,
  14642, 484, 456, 11, 472, 295, 264, 881, 1143, 14642, 294, 8062, 3164, 13, 50692],
  "temperature": 0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 3, "seek": 2544, "start": 32.0, "end":
  34.160000000000004, "text": " And today I''m talking to Yuri Malkov.", "tokens":
  [50692, 400, 965, 286, 478, 1417, 281, 33901, 376, 667, 5179, 13, 50800], "temperature":
  0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 4, "seek": 2544, "start": 34.160000000000004,
  "end": 36.160000000000004, "text": " How are you doing?", "tokens": [50800, 1012,
  366, 291, 884, 30, 50900], "temperature": 0.0, "avg_logprob": -0.4448713302612305,
  "compression_ratio": 1.5817307692307692, "no_speech_prob": 0.04719945415854454},
  {"id": 5, "seek": 2544, "start": 36.160000000000004, "end": 37.160000000000004,
  "text": " Hi.", "tokens": [50900, 2421, 13, 50950], "temperature": 0.0, "avg_logprob":
  -0.4448713302612305, "compression_ratio": 1.5817307692307692, "no_speech_prob":
  0.04719945415854454}, {"id": 6, "seek": 2544, "start": 37.160000000000004, "end":
  38.160000000000004, "text": " Hi.", "tokens": [50950, 2421, 13, 51000], "temperature":
  0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 7, "seek": 2544, "start": 38.160000000000004,
  "end": 39.160000000000004, "text": " Hi.", "tokens": [51000, 2421, 13, 51050], "temperature":
  0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 8, "seek": 2544, "start": 39.160000000000004,
  "end": 44.24, "text": " So yeah, my name is Yuri Malkov.", "tokens": [51050, 407,
  1338, 11, 452, 1315, 307, 33901, 376, 667, 5179, 13, 51304], "temperature": 0.0,
  "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692, "no_speech_prob":
  0.04719945415854454}, {"id": 9, "seek": 2544, "start": 44.24, "end": 46.36, "text":
  " Currently I''m working at Twitter.", "tokens": [51304, 19964, 286, 478, 1364,
  412, 5794, 13, 51410], "temperature": 0.0, "avg_logprob": -0.4448713302612305, "compression_ratio":
  1.5817307692307692, "no_speech_prob": 0.04719945415854454}, {"id": 10, "seek": 2544,
  "start": 46.36, "end": 53.32, "text": " There''s a staff from my engineer and the
  content understanding and research and recommender", "tokens": [51410, 821, 311,
  257, 3525, 490, 452, 11403, 293, 264, 2701, 3701, 293, 2132, 293, 2748, 260, 51758],
  "temperature": 0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 11, "seek": 2544, "start": 53.32,
  "end": 54.32, "text": " systems.", "tokens": [51758, 3652, 13, 51808], "temperature":
  0.0, "avg_logprob": -0.4448713302612305, "compression_ratio": 1.5817307692307692,
  "no_speech_prob": 0.04719945415854454}, {"id": 12, "seek": 5432, "start": 54.56,
  "end": 60.24, "text": " Yeah, please know that during discussion I don''t represent
  like Twitter''s point of view.", "tokens": [50376, 865, 11, 1767, 458, 300, 1830,
  5017, 286, 500, 380, 2906, 411, 5794, 311, 935, 295, 1910, 13, 50660], "temperature":
  0.0, "avg_logprob": -0.3138644748263889, "compression_ratio": 1.53125, "no_speech_prob":
  0.004192720633000135}, {"id": 13, "seek": 5432, "start": 60.24, "end": 63.16, "text":
  " The views are of my own.", "tokens": [50660, 440, 6809, 366, 295, 452, 1065, 13,
  50806], "temperature": 0.0, "avg_logprob": -0.3138644748263889, "compression_ratio":
  1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 14, "seek": 5432, "start":
  63.16, "end": 66.08, "text": " Yeah, so it''s great.", "tokens": [50806, 865, 11,
  370, 309, 311, 869, 13, 50952], "temperature": 0.0, "avg_logprob": -0.3138644748263889,
  "compression_ratio": 1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 15,
  "seek": 5432, "start": 66.08, "end": 69.56, "text": " So yeah, you already began
  introducing yourself.", "tokens": [50952, 407, 1338, 11, 291, 1217, 4283, 15424,
  1803, 13, 51126], "temperature": 0.0, "avg_logprob": -0.3138644748263889, "compression_ratio":
  1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 16, "seek": 5432, "start":
  69.56, "end": 76.03999999999999, "text": " So I was wondering if you could tell
  me a bit about yourself, your background and then", "tokens": [51126, 407, 286,
  390, 6359, 498, 291, 727, 980, 385, 257, 857, 466, 1803, 11, 428, 3678, 293, 550,
  51450], "temperature": 0.0, "avg_logprob": -0.3138644748263889, "compression_ratio":
  1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 17, "seek": 5432, "start":
  76.03999999999999, "end": 80.0, "text": " maybe we can also move into discussing
  the algorithm itself.", "tokens": [51450, 1310, 321, 393, 611, 1286, 666, 10850,
  264, 9284, 2564, 13, 51648], "temperature": 0.0, "avg_logprob": -0.3138644748263889,
  "compression_ratio": 1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 18,
  "seek": 5432, "start": 80.0, "end": 81.64, "text": " Okay, sure.", "tokens": [51648,
  1033, 11, 988, 13, 51730], "temperature": 0.0, "avg_logprob": -0.3138644748263889,
  "compression_ratio": 1.53125, "no_speech_prob": 0.004192720633000135}, {"id": 19,
  "seek": 8164, "start": 82.12, "end": 90.56, "text": " Yeah, so my trajectory of
  moving to ML is quite typical to Russia.", "tokens": [50388, 865, 11, 370, 452,
  21512, 295, 2684, 281, 21601, 307, 1596, 7476, 281, 6797, 13, 50810], "temperature":
  0.0, "avg_logprob": -0.32309078034900485, "compression_ratio": 1.3734177215189873,
  "no_speech_prob": 0.005141934845596552}, {"id": 20, "seek": 8164, "start": 90.56,
  "end": 98.84, "text": " So yeah, I got good physics education in Nizhny Novgorod
  and there I did the PhD in laser", "tokens": [50810, 407, 1338, 11, 286, 658, 665,
  10649, 3309, 294, 426, 590, 71, 1634, 31948, 26465, 378, 293, 456, 286, 630, 264,
  14476, 294, 12530, 51224], "temperature": 0.0, "avg_logprob": -0.32309078034900485,
  "compression_ratio": 1.3734177215189873, "no_speech_prob": 0.005141934845596552},
  {"id": 21, "seek": 8164, "start": 98.84, "end": 101.0, "text": " physics.", "tokens":
  [51224, 10649, 13, 51332], "temperature": 0.0, "avg_logprob": -0.32309078034900485,
  "compression_ratio": 1.3734177215189873, "no_speech_prob": 0.005141934845596552},
  {"id": 22, "seek": 8164, "start": 101.0, "end": 105.56, "text": " So there I was
  doing experiments on teravat lasers.", "tokens": [51332, 407, 456, 286, 390, 884,
  12050, 322, 1796, 706, 267, 37948, 13, 51560], "temperature": 0.0, "avg_logprob":
  -0.32309078034900485, "compression_ratio": 1.3734177215189873, "no_speech_prob":
  0.005141934845596552}, {"id": 23, "seek": 10556, "start": 105.56, "end": 112.56,
  "text": " So that was fun and like that part of physics is like considered to be
  like sexy part,", "tokens": [50364, 407, 300, 390, 1019, 293, 411, 300, 644, 295,
  10649, 307, 411, 4888, 281, 312, 411, 13701, 644, 11, 50714], "temperature": 0.0,
  "avg_logprob": -0.3145904979486575, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.011874135583639145}, {"id": 24, "seek": 10556, "start": 112.56, "end": 116.44,
  "text": " similar to computer vision in machine learning.", "tokens": [50714, 2531,
  281, 3820, 5201, 294, 3479, 2539, 13, 50908], "temperature": 0.0, "avg_logprob":
  -0.3145904979486575, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.011874135583639145}, {"id": 25, "seek": 10556, "start": 116.44, "end": 119.68,
  "text": " And I was lucky to have good supervisors.", "tokens": [50908, 400, 286,
  390, 6356, 281, 362, 665, 42218, 13, 51070], "temperature": 0.0, "avg_logprob":
  -0.3145904979486575, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.011874135583639145}, {"id": 26, "seek": 10556, "start": 119.68, "end": 125.48,
  "text": " So one of my supervisor which was like mostly a supervisor of paper.",
  "tokens": [51070, 407, 472, 295, 452, 24610, 597, 390, 411, 5240, 257, 24610, 295,
  3035, 13, 51360], "temperature": 0.0, "avg_logprob": -0.3145904979486575, "compression_ratio":
  1.6386138613861385, "no_speech_prob": 0.011874135583639145}, {"id": 27, "seek":
  10556, "start": 125.48, "end": 126.80000000000001, "text": " So he helped me.",
  "tokens": [51360, 407, 415, 4254, 385, 13, 51426], "temperature": 0.0, "avg_logprob":
  -0.3145904979486575, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.011874135583639145}, {"id": 28, "seek": 10556, "start": 126.80000000000001, "end":
  129.44, "text": " Is now the head of Russian Academy.", "tokens": [51426, 1119,
  586, 264, 1378, 295, 7220, 11735, 13, 51558], "temperature": 0.0, "avg_logprob":
  -0.3145904979486575, "compression_ratio": 1.6386138613861385, "no_speech_prob":
  0.011874135583639145}, {"id": 29, "seek": 10556, "start": 129.44, "end": 133.2,
  "text": " So yeah, I had good supervisors.", "tokens": [51558, 407, 1338, 11, 286,
  632, 665, 42218, 13, 51746], "temperature": 0.0, "avg_logprob": -0.3145904979486575,
  "compression_ratio": 1.6386138613861385, "no_speech_prob": 0.011874135583639145},
  {"id": 30, "seek": 13320, "start": 134.2, "end": 141.51999999999998, "text": " In
  addition to physics, I was concurrently working part time in a startup that was
  building", "tokens": [50414, 682, 4500, 281, 10649, 11, 286, 390, 37702, 356, 1364,
  644, 565, 294, 257, 18578, 300, 390, 2390, 50780], "temperature": 0.0, "avg_logprob":
  -0.26957862782028486, "compression_ratio": 1.4036144578313252, "no_speech_prob":
  0.003964224364608526}, {"id": 31, "seek": 13320, "start": 141.51999999999998, "end":
  149.64, "text": " distributed scalable search systems based on insights from real
  networks.", "tokens": [50780, 12631, 38481, 3164, 3652, 2361, 322, 14310, 490, 957,
  9590, 13, 51186], "temperature": 0.0, "avg_logprob": -0.26957862782028486, "compression_ratio":
  1.4036144578313252, "no_speech_prob": 0.003964224364608526}, {"id": 32, "seek":
  13320, "start": 149.64, "end": 159.95999999999998, "text": " Yeah, that worked ended
  up in several papers on predecessor of H&W.", "tokens": [51186, 865, 11, 300, 2732,
  4590, 493, 294, 2940, 10577, 322, 34991, 295, 389, 5, 54, 13, 51702], "temperature":
  0.0, "avg_logprob": -0.26957862782028486, "compression_ratio": 1.4036144578313252,
  "no_speech_prob": 0.003964224364608526}, {"id": 33, "seek": 15996, "start": 159.96,
  "end": 169.56, "text": " And the startup, yeah, unfortunately the startup was closed
  before even I got PhD.", "tokens": [50364, 400, 264, 18578, 11, 1338, 11, 7015,
  264, 18578, 390, 5395, 949, 754, 286, 658, 14476, 13, 50844], "temperature": 0.0,
  "avg_logprob": -0.2619208017985026, "compression_ratio": 1.4, "no_speech_prob":
  0.015900060534477234}, {"id": 34, "seek": 15996, "start": 169.56, "end": 181.20000000000002,
  "text": " So yeah, I decided to focus on physics after that, but after I got my
  PhD degree in physics.", "tokens": [50844, 407, 1338, 11, 286, 3047, 281, 1879,
  322, 10649, 934, 300, 11, 457, 934, 286, 658, 452, 14476, 4314, 294, 10649, 13,
  51426], "temperature": 0.0, "avg_logprob": -0.2619208017985026, "compression_ratio":
  1.4, "no_speech_prob": 0.015900060534477234}, {"id": 35, "seek": 18120, "start":
  181.2, "end": 190.51999999999998, "text": " So I, like there was a choice for me
  like what to do next and to proceed with career", "tokens": [50364, 407, 286, 11,
  411, 456, 390, 257, 3922, 337, 385, 411, 437, 281, 360, 958, 293, 281, 8991, 365,
  3988, 50830], "temperature": 0.0, "avg_logprob": -0.31042656341156405, "compression_ratio":
  1.5696969696969696, "no_speech_prob": 0.030610591173171997}, {"id": 36, "seek":
  18120, "start": 190.51999999999998, "end": 191.51999999999998, "text": " and physics.",
  "tokens": [50830, 293, 10649, 13, 50880], "temperature": 0.0, "avg_logprob": -0.31042656341156405,
  "compression_ratio": 1.5696969696969696, "no_speech_prob": 0.030610591173171997},
  {"id": 37, "seek": 18120, "start": 191.51999999999998, "end": 195.04, "text": "
  I had to go abroad, like I didn''t want to go abroad.", "tokens": [50880, 286, 632,
  281, 352, 12637, 11, 411, 286, 994, 380, 528, 281, 352, 12637, 13, 51056], "temperature":
  0.0, "avg_logprob": -0.31042656341156405, "compression_ratio": 1.5696969696969696,
  "no_speech_prob": 0.030610591173171997}, {"id": 38, "seek": 18120, "start": 195.04,
  "end": 197.44, "text": " I want to stay in Nizhny Novgorod.", "tokens": [51056,
  286, 528, 281, 1754, 294, 426, 590, 71, 1634, 31948, 26465, 378, 13, 51176], "temperature":
  0.0, "avg_logprob": -0.31042656341156405, "compression_ratio": 1.5696969696969696,
  "no_speech_prob": 0.030610591173171997}, {"id": 39, "seek": 18120, "start": 197.44,
  "end": 204.83999999999997, "text": " So I decided to just like switch directions
  and to network science there.", "tokens": [51176, 407, 286, 3047, 281, 445, 411,
  3679, 11095, 293, 281, 3209, 3497, 456, 13, 51546], "temperature": 0.0, "avg_logprob":
  -0.31042656341156405, "compression_ratio": 1.5696969696969696, "no_speech_prob":
  0.030610591173171997}, {"id": 40, "seek": 20484, "start": 204.84, "end": 213.0,
  "text": " And then I got a really good grant from the Russian fund.", "tokens":
  [50364, 400, 550, 286, 658, 257, 534, 665, 6386, 490, 264, 7220, 2374, 13, 50772],
  "temperature": 0.0, "avg_logprob": -0.383243845469916, "compression_ratio": 1.4325842696629214,
  "no_speech_prob": 0.01627843640744686}, {"id": 41, "seek": 20484, "start": 213.0,
  "end": 217.52, "text": " Alpha Phi, which now is not present anymore.", "tokens":
  [50772, 20588, 41435, 11, 597, 586, 307, 406, 1974, 3602, 13, 50998], "temperature":
  0.0, "avg_logprob": -0.383243845469916, "compression_ratio": 1.4325842696629214,
  "no_speech_prob": 0.01627843640744686}, {"id": 42, "seek": 20484, "start": 217.52,
  "end": 221.36, "text": " So I could do like research by my own.", "tokens": [50998,
  407, 286, 727, 360, 411, 2132, 538, 452, 1065, 13, 51190], "temperature": 0.0, "avg_logprob":
  -0.383243845469916, "compression_ratio": 1.4325842696629214, "no_speech_prob": 0.01627843640744686},
  {"id": 43, "seek": 20484, "start": 221.36, "end": 224.6, "text": " Like this pretty
  good salary.", "tokens": [51190, 1743, 341, 1238, 665, 15360, 13, 51352], "temperature":
  0.0, "avg_logprob": -0.383243845469916, "compression_ratio": 1.4325842696629214,
  "no_speech_prob": 0.01627843640744686}, {"id": 44, "seek": 20484, "start": 224.6,
  "end": 230.84, "text": " And yeah, I also joined companies, like computer vision
  companies to get to insight", "tokens": [51352, 400, 1338, 11, 286, 611, 6869, 3431,
  11, 411, 3820, 5201, 3431, 281, 483, 281, 11269, 51664], "temperature": 0.0, "avg_logprob":
  -0.383243845469916, "compression_ratio": 1.4325842696629214, "no_speech_prob": 0.01627843640744686},
  {"id": 45, "seek": 23084, "start": 230.84, "end": 236.56, "text": " into why people
  actually use like similarities to your algorithm and machine learning.", "tokens":
  [50364, 666, 983, 561, 767, 764, 411, 24197, 281, 428, 9284, 293, 3479, 2539, 13,
  50650], "temperature": 0.0, "avg_logprob": -0.42778515171360326, "compression_ratio":
  1.5388349514563107, "no_speech_prob": 0.0028358076233416796}, {"id": 46, "seek":
  23084, "start": 236.56, "end": 245.76, "text": " And I worked at an television and
  later anti-club, which is the company that is like doing big", "tokens": [50650,
  400, 286, 2732, 412, 364, 8815, 293, 1780, 6061, 12, 40607, 11, 597, 307, 264, 2237,
  300, 307, 411, 884, 955, 51110], "temperature": 0.0, "avg_logprob": -0.42778515171360326,
  "compression_ratio": 1.5388349514563107, "no_speech_prob": 0.0028358076233416796},
  {"id": 47, "seek": 23084, "start": 245.76, "end": 250.52, "text": " brother for
  Moscow, like Moscow surveillance.", "tokens": [51110, 3708, 337, 18298, 11, 411,
  18298, 18475, 13, 51348], "temperature": 0.0, "avg_logprob": -0.42778515171360326,
  "compression_ratio": 1.5388349514563107, "no_speech_prob": 0.0028358076233416796},
  {"id": 48, "seek": 23084, "start": 250.52, "end": 259.24, "text": " And later I
  joined some some VIS Center in Moscow and I worked with like Victor Limpitsky",
  "tokens": [51348, 400, 1780, 286, 6869, 512, 512, 691, 2343, 5169, 294, 18298, 293,
  286, 2732, 365, 411, 15777, 441, 8814, 1208, 4133, 51784], "temperature": 0.0, "avg_logprob":
  -0.42778515171360326, "compression_ratio": 1.5388349514563107, "no_speech_prob":
  0.0028358076233416796}, {"id": 49, "seek": 25924, "start": 259.24, "end": 270.56,
  "text": " who is one of the well known personas in Russia and in 2019 I moved to
  US and now I", "tokens": [50364, 567, 307, 472, 295, 264, 731, 2570, 12019, 294,
  6797, 293, 294, 6071, 286, 4259, 281, 2546, 293, 586, 286, 50930], "temperature":
  0.0, "avg_logprob": -0.37339091691814486, "compression_ratio": 1.3798882681564246,
  "no_speech_prob": 0.02167615294456482}, {"id": 50, "seek": 25924, "start": 270.56,
  "end": 280.0, "text": " work in Twitter to recommend their systems and content understanding,
  like board models.", "tokens": [50930, 589, 294, 5794, 281, 2748, 641, 3652, 293,
  2701, 3701, 11, 411, 3150, 5245, 13, 51402], "temperature": 0.0, "avg_logprob":
  -0.37339091691814486, "compression_ratio": 1.3798882681564246, "no_speech_prob":
  0.02167615294456482}, {"id": 51, "seek": 25924, "start": 280.0, "end": 281.0, "text":
  " Oh yeah.", "tokens": [51402, 876, 1338, 13, 51452], "temperature": 0.0, "avg_logprob":
  -0.37339091691814486, "compression_ratio": 1.3798882681564246, "no_speech_prob":
  0.02167615294456482}, {"id": 52, "seek": 25924, "start": 281.0, "end": 285.84000000000003,
  "text": " So you probably also use nearest neighbor search in your work or.", "tokens":
  [51452, 407, 291, 1391, 611, 764, 23831, 5987, 3164, 294, 428, 589, 420, 13, 51694],
  "temperature": 0.0, "avg_logprob": -0.37339091691814486, "compression_ratio": 1.3798882681564246,
  "no_speech_prob": 0.02167615294456482}, {"id": 53, "seek": 28584, "start": 286.4,
  "end": 290.52, "text": " Well, I can mention it.", "tokens": [50392, 1042, 11, 286,
  393, 2152, 309, 13, 50598], "temperature": 0.0, "avg_logprob": -0.46531993586842607,
  "compression_ratio": 1.5166666666666666, "no_speech_prob": 0.06107814237475395},
  {"id": 54, "seek": 28584, "start": 290.52, "end": 292.88, "text": " Yeah, well,
  not really.", "tokens": [50598, 865, 11, 731, 11, 406, 534, 13, 50716], "temperature":
  0.0, "avg_logprob": -0.46531993586842607, "compression_ratio": 1.5166666666666666,
  "no_speech_prob": 0.06107814237475395}, {"id": 55, "seek": 28584, "start": 292.88,
  "end": 300.28, "text": " So I''m focused on the so I can work Twitter most of the
  time.", "tokens": [50716, 407, 286, 478, 5178, 322, 264, 370, 286, 393, 589, 5794,
  881, 295, 264, 565, 13, 51086], "temperature": 0.0, "avg_logprob": -0.46531993586842607,
  "compression_ratio": 1.5166666666666666, "no_speech_prob": 0.06107814237475395},
  {"id": 56, "seek": 28584, "start": 300.28, "end": 305.55999999999995, "text": "
  I can have last half a year, I spent on improving search relevance.", "tokens":
  [51086, 286, 393, 362, 1036, 1922, 257, 1064, 11, 286, 4418, 322, 11470, 3164, 32684,
  13, 51350], "temperature": 0.0, "avg_logprob": -0.46531993586842607, "compression_ratio":
  1.5166666666666666, "no_speech_prob": 0.06107814237475395}, {"id": 57, "seek": 28584,
  "start": 305.55999999999995, "end": 308.55999999999995, "text": " So that is mostly
  the ranker.", "tokens": [51350, 407, 300, 307, 5240, 264, 6181, 260, 13, 51500],
  "temperature": 0.0, "avg_logprob": -0.46531993586842607, "compression_ratio": 1.5166666666666666,
  "no_speech_prob": 0.06107814237475395}, {"id": 58, "seek": 28584, "start": 308.55999999999995,
  "end": 313.52, "text": " But that is closely related to the nearest neighbor search.",
  "tokens": [51500, 583, 300, 307, 8185, 4077, 281, 264, 23831, 5987, 3164, 13, 51748],
  "temperature": 0.0, "avg_logprob": -0.46531993586842607, "compression_ratio": 1.5166666666666666,
  "no_speech_prob": 0.06107814237475395}, {"id": 59, "seek": 28584, "start": 313.52,
  "end": 314.52, "text": " Yeah.", "tokens": [51748, 865, 13, 51798], "temperature":
  0.0, "avg_logprob": -0.46531993586842607, "compression_ratio": 1.5166666666666666,
  "no_speech_prob": 0.06107814237475395}, {"id": 60, "seek": 31452, "start": 314.68,
  "end": 319.08, "text": " So you mentioned like basically the background where you''ve
  been in Russia, it was like kind", "tokens": [50372, 407, 291, 2835, 411, 1936,
  264, 3678, 689, 291, 600, 668, 294, 6797, 11, 309, 390, 411, 733, 50592], "temperature":
  0.0, "avg_logprob": -0.20180282990137735, "compression_ratio": 1.6869918699186992,
  "no_speech_prob": 0.0018707547569647431}, {"id": 61, "seek": 31452, "start": 319.08,
  "end": 320.59999999999997, "text": " of related to computer vision.", "tokens":
  [50592, 295, 4077, 281, 3820, 5201, 13, 50668], "temperature": 0.0, "avg_logprob":
  -0.20180282990137735, "compression_ratio": 1.6869918699186992, "no_speech_prob":
  0.0018707547569647431}, {"id": 62, "seek": 31452, "start": 320.59999999999997, "end":
  325.59999999999997, "text": " Of course, you had physics background by education,
  but you also kind of worked in computer vision", "tokens": [50668, 2720, 1164, 11,
  291, 632, 10649, 3678, 538, 3309, 11, 457, 291, 611, 733, 295, 2732, 294, 3820,
  5201, 50918], "temperature": 0.0, "avg_logprob": -0.20180282990137735, "compression_ratio":
  1.6869918699186992, "no_speech_prob": 0.0018707547569647431}, {"id": 63, "seek":
  31452, "start": 325.59999999999997, "end": 326.52, "text": " startups.", "tokens":
  [50918, 28041, 13, 50964], "temperature": 0.0, "avg_logprob": -0.20180282990137735,
  "compression_ratio": 1.6869918699186992, "no_speech_prob": 0.0018707547569647431},
  {"id": 64, "seek": 31452, "start": 326.52, "end": 332.24, "text": " So what was
  your impression of this nearest neighbor search problem and like, how did you think",
  "tokens": [50964, 407, 437, 390, 428, 9995, 295, 341, 23831, 5987, 3164, 1154, 293,
  411, 11, 577, 630, 291, 519, 51250], "temperature": 0.0, "avg_logprob": -0.20180282990137735,
  "compression_ratio": 1.6869918699186992, "no_speech_prob": 0.0018707547569647431},
  {"id": 65, "seek": 31452, "start": 332.24, "end": 338.15999999999997, "text": "
  about it when like, did you read papers to understand like what was done in that
  area?", "tokens": [51250, 466, 309, 562, 411, 11, 630, 291, 1401, 10577, 281, 1223,
  411, 437, 390, 1096, 294, 300, 1859, 30, 51546], "temperature": 0.0, "avg_logprob":
  -0.20180282990137735, "compression_ratio": 1.6869918699186992, "no_speech_prob":
  0.0018707547569647431}, {"id": 66, "seek": 33816, "start": 338.16, "end": 346.44,
  "text": " I think that areas pretty like developed right in in in the papers like
  like NSW itself,", "tokens": [50364, 286, 519, 300, 3179, 1238, 411, 4743, 558,
  294, 294, 294, 264, 10577, 411, 411, 15943, 54, 2564, 11, 50778], "temperature":
  0.0, "avg_logprob": -0.39413238826550934, "compression_ratio": 1.4861878453038675,
  "no_speech_prob": 0.02068152092397213}, {"id": 67, "seek": 33816, "start": 346.44,
  "end": 347.44, "text": " right?", "tokens": [50778, 558, 30, 50828], "temperature":
  0.0, "avg_logprob": -0.39413238826550934, "compression_ratio": 1.4861878453038675,
  "no_speech_prob": 0.02068152092397213}, {"id": 68, "seek": 33816, "start": 347.44,
  "end": 349.44, "text": " Like navigators.", "tokens": [50828, 1743, 7407, 3391,
  13, 50928], "temperature": 0.0, "avg_logprob": -0.39413238826550934, "compression_ratio":
  1.4861878453038675, "no_speech_prob": 0.02068152092397213}, {"id": 69, "seek": 33816,
  "start": 349.44, "end": 358.88, "text": " Well, so like in the startup meta labs,
  I have been working, I think I''ve worked for", "tokens": [50928, 1042, 11, 370,
  411, 294, 264, 18578, 19616, 20339, 11, 286, 362, 668, 1364, 11, 286, 519, 286,
  600, 2732, 337, 51400], "temperature": 0.0, "avg_logprob": -0.39413238826550934,
  "compression_ratio": 1.4861878453038675, "no_speech_prob": 0.02068152092397213},
  {"id": 70, "seek": 33816, "start": 358.88, "end": 361.16, "text": " six or seven
  years.", "tokens": [51400, 2309, 420, 3407, 924, 13, 51514], "temperature": 0.0,
  "avg_logprob": -0.39413238826550934, "compression_ratio": 1.4861878453038675, "no_speech_prob":
  0.02068152092397213}, {"id": 71, "seek": 33816, "start": 361.16, "end": 365.8, "text":
  " So it was quite quite a significant period of time.", "tokens": [51514, 407, 309,
  390, 1596, 1596, 257, 4776, 2896, 295, 565, 13, 51746], "temperature": 0.0, "avg_logprob":
  -0.39413238826550934, "compression_ratio": 1.4861878453038675, "no_speech_prob":
  0.02068152092397213}, {"id": 72, "seek": 36580, "start": 365.8, "end": 370.16, "text":
  " And then we started just like from distributed search.", "tokens": [50364, 400,
  550, 321, 1409, 445, 411, 490, 12631, 3164, 13, 50582], "temperature": 0.0, "avg_logprob":
  -0.24922507459467108, "compression_ratio": 1.6858638743455496, "no_speech_prob":
  0.0018466752953827381}, {"id": 73, "seek": 36580, "start": 370.16, "end": 373.36,
  "text": " So the idea was like we do it from scratch.", "tokens": [50582, 407, 264,
  1558, 390, 411, 321, 360, 309, 490, 8459, 13, 50742], "temperature": 0.0, "avg_logprob":
  -0.24922507459467108, "compression_ratio": 1.6858638743455496, "no_speech_prob":
  0.0018466752953827381}, {"id": 74, "seek": 36580, "start": 373.36, "end": 377.0,
  "text": " So like we don''t care what I''ve been done before.", "tokens": [50742,
  407, 411, 321, 500, 380, 1127, 437, 286, 600, 668, 1096, 949, 13, 50924], "temperature":
  0.0, "avg_logprob": -0.24922507459467108, "compression_ratio": 1.6858638743455496,
  "no_speech_prob": 0.0018466752953827381}, {"id": 75, "seek": 36580, "start": 377.0,
  "end": 378.0, "text": " So we have an idea.", "tokens": [50924, 407, 321, 362, 364,
  1558, 13, 50974], "temperature": 0.0, "avg_logprob": -0.24922507459467108, "compression_ratio":
  1.6858638743455496, "no_speech_prob": 0.0018466752953827381}, {"id": 76, "seek":
  36580, "start": 378.0, "end": 385.08000000000004, "text": " So there are like distributed
  hash tables like port or other stuff and we want to do it,", "tokens": [50974, 407,
  456, 366, 411, 12631, 22019, 8020, 411, 2436, 420, 661, 1507, 293, 321, 528, 281,
  360, 309, 11, 51328], "temperature": 0.0, "avg_logprob": -0.24922507459467108, "compression_ratio":
  1.6858638743455496, "no_speech_prob": 0.0018466752953827381}, {"id": 77, "seek":
  36580, "start": 385.08000000000004, "end": 386.92, "text": " but with similarity
  search.", "tokens": [51328, 457, 365, 32194, 3164, 13, 51420], "temperature": 0.0,
  "avg_logprob": -0.24922507459467108, "compression_ratio": 1.6858638743455496, "no_speech_prob":
  0.0018466752953827381}, {"id": 78, "seek": 36580, "start": 386.92, "end": 391.28000000000003,
  "text": " So that should scale to better base.", "tokens": [51420, 407, 300, 820,
  4373, 281, 1101, 3096, 13, 51638], "temperature": 0.0, "avg_logprob": -0.24922507459467108,
  "compression_ratio": 1.6858638743455496, "no_speech_prob": 0.0018466752953827381},
  {"id": 79, "seek": 39128, "start": 391.28, "end": 396.15999999999997, "text": "
  And there that''s like very different approach from nearest neighbor search.", "tokens":
  [50364, 400, 456, 300, 311, 411, 588, 819, 3109, 490, 23831, 5987, 3164, 13, 50608],
  "temperature": 0.0, "avg_logprob": -0.2146826996200386, "compression_ratio": 1.6919642857142858,
  "no_speech_prob": 0.006103829946368933}, {"id": 80, "seek": 39128, "start": 396.15999999999997,
  "end": 401.88, "text": " And like most of the time we spent like developing this
  algorithm was not even like nearest", "tokens": [50608, 400, 411, 881, 295, 264,
  565, 321, 4418, 411, 6416, 341, 9284, 390, 406, 754, 411, 23831, 50894], "temperature":
  0.0, "avg_logprob": -0.2146826996200386, "compression_ratio": 1.6919642857142858,
  "no_speech_prob": 0.006103829946368933}, {"id": 81, "seek": 39128, "start": 401.88,
  "end": 402.88, "text": " neighbor search.", "tokens": [50894, 5987, 3164, 13, 50944],
  "temperature": 0.0, "avg_logprob": -0.2146826996200386, "compression_ratio": 1.6919642857142858,
  "no_speech_prob": 0.006103829946368933}, {"id": 82, "seek": 39128, "start": 402.88,
  "end": 412.35999999999996, "text": " That was closer to this symbolic filtering,
  but with like arbitrary filters.", "tokens": [50944, 663, 390, 4966, 281, 341, 25755,
  30822, 11, 457, 365, 411, 23211, 15995, 13, 51418], "temperature": 0.0, "avg_logprob":
  -0.2146826996200386, "compression_ratio": 1.6919642857142858, "no_speech_prob":
  0.006103829946368933}, {"id": 83, "seek": 39128, "start": 412.35999999999996, "end":
  418.08, "text": " And only at some point of time, like we had a realization that
  oh, like that is similar", "tokens": [51418, 400, 787, 412, 512, 935, 295, 565,
  11, 411, 321, 632, 257, 25138, 300, 1954, 11, 411, 300, 307, 2531, 51704], "temperature":
  0.0, "avg_logprob": -0.2146826996200386, "compression_ratio": 1.6919642857142858,
  "no_speech_prob": 0.006103829946368933}, {"id": 84, "seek": 39128, "start": 418.08,
  "end": 420.4, "text": " to what people actually need.", "tokens": [51704, 281, 437,
  561, 767, 643, 13, 51820], "temperature": 0.0, "avg_logprob": -0.2146826996200386,
  "compression_ratio": 1.6919642857142858, "no_speech_prob": 0.006103829946368933},
  {"id": 85, "seek": 42040, "start": 420.4, "end": 423.4, "text": " Like there are
  a lot of papers of on nearest neighbor search.", "tokens": [50364, 1743, 456, 366,
  257, 688, 295, 10577, 295, 322, 23831, 5987, 3164, 13, 50514], "temperature": 0.0,
  "avg_logprob": -0.34679229442889875, "compression_ratio": 1.6218487394957983, "no_speech_prob":
  0.008457459509372711}, {"id": 86, "seek": 42040, "start": 423.4, "end": 432.2, "text":
  " So we switch direction and like the most cited publications are on nearest neighbors.",
  "tokens": [50514, 407, 321, 3679, 3513, 293, 411, 264, 881, 30134, 25618, 366, 322,
  23831, 12512, 13, 50954], "temperature": 0.0, "avg_logprob": -0.34679229442889875,
  "compression_ratio": 1.6218487394957983, "no_speech_prob": 0.008457459509372711},
  {"id": 87, "seek": 42040, "start": 432.2, "end": 433.2, "text": " Yeah.", "tokens":
  [50954, 865, 13, 51004], "temperature": 0.0, "avg_logprob": -0.34679229442889875,
  "compression_ratio": 1.6218487394957983, "no_speech_prob": 0.008457459509372711},
  {"id": 88, "seek": 42040, "start": 433.2, "end": 434.2, "text": " Yeah.", "tokens":
  [51004, 865, 13, 51054], "temperature": 0.0, "avg_logprob": -0.34679229442889875,
  "compression_ratio": 1.6218487394957983, "no_speech_prob": 0.008457459509372711},
  {"id": 89, "seek": 42040, "start": 434.2, "end": 437.2, "text": " I don''t remember
  was it on your paper or somebody else''s paper.", "tokens": [51054, 286, 500, 380,
  1604, 390, 309, 322, 428, 3035, 420, 2618, 1646, 311, 3035, 13, 51204], "temperature":
  0.0, "avg_logprob": -0.34679229442889875, "compression_ratio": 1.6218487394957983,
  "no_speech_prob": 0.008457459509372711}, {"id": 90, "seek": 42040, "start": 437.2,
  "end": 442.35999999999996, "text": " I saw a paper of my old friend, you reliefs
  because he actually defended his thesis like", "tokens": [51204, 286, 1866, 257,
  3035, 295, 452, 1331, 1277, 11, 291, 10915, 82, 570, 415, 767, 34135, 702, 22288,
  411, 51462], "temperature": 0.0, "avg_logprob": -0.34679229442889875, "compression_ratio":
  1.6218487394957983, "no_speech_prob": 0.008457459509372711}, {"id": 91, "seek":
  42040, "start": 442.35999999999996, "end": 445.32, "text": " in PG thesis in this
  space.", "tokens": [51462, 294, 40975, 22288, 294, 341, 1901, 13, 51610], "temperature":
  0.0, "avg_logprob": -0.34679229442889875, "compression_ratio": 1.6218487394957983,
  "no_speech_prob": 0.008457459509372711}, {"id": 92, "seek": 42040, "start": 445.32,
  "end": 448.56, "text": " So when he was doing it, I think it was 2009.", "tokens":
  [51610, 407, 562, 415, 390, 884, 309, 11, 286, 519, 309, 390, 11453, 13, 51772],
  "temperature": 0.0, "avg_logprob": -0.34679229442889875, "compression_ratio": 1.6218487394957983,
  "no_speech_prob": 0.008457459509372711}, {"id": 93, "seek": 44856, "start": 448.56,
  "end": 453.64, "text": " I was like, I was considering this like a pure mathematical
  problem without like maybe", "tokens": [50364, 286, 390, 411, 11, 286, 390, 8079,
  341, 411, 257, 6075, 18894, 1154, 1553, 411, 1310, 50618], "temperature": 0.0, "avg_logprob":
  -0.19077334684484146, "compression_ratio": 1.7306273062730628, "no_speech_prob":
  0.0022083779331296682}, {"id": 94, "seek": 44856, "start": 453.64, "end": 455.12,
  "text": " direct application.", "tokens": [50618, 2047, 3861, 13, 50692], "temperature":
  0.0, "avg_logprob": -0.19077334684484146, "compression_ratio": 1.7306273062730628,
  "no_speech_prob": 0.0022083779331296682}, {"id": 95, "seek": 44856, "start": 455.12,
  "end": 458.44, "text": " But then he gave a talk at Google, like you know, Google
  tech talks.", "tokens": [50692, 583, 550, 415, 2729, 257, 751, 412, 3329, 11, 411,
  291, 458, 11, 3329, 7553, 6686, 13, 50858], "temperature": 0.0, "avg_logprob": -0.19077334684484146,
  "compression_ratio": 1.7306273062730628, "no_speech_prob": 0.0022083779331296682},
  {"id": 96, "seek": 44856, "start": 458.44, "end": 463.88, "text": " I don''t know
  if they still exist or not, but like he presented this problem and like they", "tokens":
  [50858, 286, 500, 380, 458, 498, 436, 920, 2514, 420, 406, 11, 457, 411, 415, 8212,
  341, 1154, 293, 411, 436, 51130], "temperature": 0.0, "avg_logprob": -0.19077334684484146,
  "compression_ratio": 1.7306273062730628, "no_speech_prob": 0.0022083779331296682},
  {"id": 97, "seek": 44856, "start": 463.88, "end": 467.32, "text": " did some optimizations
  as well.", "tokens": [51130, 630, 512, 5028, 14455, 382, 731, 13, 51302], "temperature":
  0.0, "avg_logprob": -0.19077334684484146, "compression_ratio": 1.7306273062730628,
  "no_speech_prob": 0.0022083779331296682}, {"id": 98, "seek": 44856, "start": 467.32,
  "end": 470.96, "text": " And then I think I think your paper sites it or maybe someone
  else''s I don''t remember.", "tokens": [51302, 400, 550, 286, 519, 286, 519, 428,
  3035, 7533, 309, 420, 1310, 1580, 1646, 311, 286, 500, 380, 1604, 13, 51484], "temperature":
  0.0, "avg_logprob": -0.19077334684484146, "compression_ratio": 1.7306273062730628,
  "no_speech_prob": 0.0022083779331296682}, {"id": 99, "seek": 44856, "start": 470.96,
  "end": 476.36, "text": " I was like really surprised to see, you know, his work
  also kind of in the same line", "tokens": [51484, 286, 390, 411, 534, 6100, 281,
  536, 11, 291, 458, 11, 702, 589, 611, 733, 295, 294, 264, 912, 1622, 51754], "temperature":
  0.0, "avg_logprob": -0.19077334684484146, "compression_ratio": 1.7306273062730628,
  "no_speech_prob": 0.0022083779331296682}, {"id": 100, "seek": 47636, "start": 476.36,
  "end": 481.36, "text": " of things that now lead to vector search essentially.",
  "tokens": [50364, 295, 721, 300, 586, 1477, 281, 8062, 3164, 4476, 13, 50614], "temperature":
  0.0, "avg_logprob": -0.36263618940188563, "compression_ratio": 1.5544554455445545,
  "no_speech_prob": 0.0341654010117054}, {"id": 101, "seek": 47636, "start": 481.36,
  "end": 487.36, "text": " Well, yeah, I think I saw his work, but it seemed like
  more theory.", "tokens": [50614, 1042, 11, 1338, 11, 286, 519, 286, 1866, 702, 589,
  11, 457, 309, 6576, 411, 544, 5261, 13, 50914], "temperature": 0.0, "avg_logprob":
  -0.36263618940188563, "compression_ratio": 1.5544554455445545, "no_speech_prob":
  0.0341654010117054}, {"id": 102, "seek": 47636, "start": 487.36, "end": 495.36,
  "text": " Like if you look to history like of like graph approaches so like.", "tokens":
  [50914, 1743, 498, 291, 574, 281, 2503, 411, 295, 411, 4295, 11587, 370, 411, 13,
  51314], "temperature": 0.0, "avg_logprob": -0.36263618940188563, "compression_ratio":
  1.5544554455445545, "no_speech_prob": 0.0341654010117054}, {"id": 103, "seek": 47636,
  "start": 495.36, "end": 500.36, "text": " Now it''s mostly like rehashing of old
  stuff.", "tokens": [51314, 823, 309, 311, 5240, 411, 22355, 11077, 295, 1331, 1507,
  13, 51564], "temperature": 0.0, "avg_logprob": -0.36263618940188563, "compression_ratio":
  1.5544554455445545, "no_speech_prob": 0.0341654010117054}, {"id": 104, "seek": 47636,
  "start": 500.36, "end": 505.48, "text": " So definitely new things, but like there
  is so much work done before like Sergey", "tokens": [51564, 407, 2138, 777, 721,
  11, 457, 411, 456, 307, 370, 709, 589, 1096, 949, 411, 49238, 51820], "temperature":
  0.0, "avg_logprob": -0.36263618940188563, "compression_ratio": 1.5544554455445545,
  "no_speech_prob": 0.0341654010117054}, {"id": 105, "seek": 50548, "start": 505.48,
  "end": 511.48, "text": " Brein worked on nearest neighbor search with like GNIT.",
  "tokens": [50364, 7090, 259, 2732, 322, 23831, 5987, 3164, 365, 411, 46411, 3927,
  13, 50664], "temperature": 0.0, "avg_logprob": -0.38368380069732666, "compression_ratio":
  1.4555555555555555, "no_speech_prob": 0.014138257130980492}, {"id": 106, "seek":
  50548, "start": 511.48, "end": 514.48, "text": " So that is also like good work.",
  "tokens": [50664, 407, 300, 307, 611, 411, 665, 589, 13, 50814], "temperature":
  0.0, "avg_logprob": -0.38368380069732666, "compression_ratio": 1.4555555555555555,
  "no_speech_prob": 0.014138257130980492}, {"id": 107, "seek": 50548, "start": 514.48,
  "end": 522.24, "text": " There were there were previous work on graph search, I
  think in 1993, which like aren''t", "tokens": [50814, 821, 645, 456, 645, 3894,
  589, 322, 4295, 3164, 11, 286, 519, 294, 25137, 11, 597, 411, 3212, 380, 51202],
  "temperature": 0.0, "avg_logprob": -0.38368380069732666, "compression_ratio": 1.4555555555555555,
  "no_speech_prob": 0.014138257130980492}, {"id": 108, "seek": 50548, "start": 522.24,
  "end": 527.48, "text": " that much different compared to like current though, like
  they have also problems with", "tokens": [51202, 300, 709, 819, 5347, 281, 411,
  2190, 1673, 11, 411, 436, 362, 611, 2740, 365, 51464], "temperature": 0.0, "avg_logprob":
  -0.38368380069732666, "compression_ratio": 1.4555555555555555, "no_speech_prob":
  0.014138257130980492}, {"id": 109, "seek": 52748, "start": 527.48, "end": 531.48,
  "text": " scalability at that point.", "tokens": [50364, 15664, 2310, 412, 300,
  935, 13, 50564], "temperature": 0.0, "avg_logprob": -0.2575679723767267, "compression_ratio":
  1.4325842696629214, "no_speech_prob": 0.20761214196681976}, {"id": 110, "seek":
  52748, "start": 531.48, "end": 537.48, "text": " So I think yeah, so that was.",
  "tokens": [50564, 407, 286, 519, 1338, 11, 370, 300, 390, 13, 50864], "temperature":
  0.0, "avg_logprob": -0.2575679723767267, "compression_ratio": 1.4325842696629214,
  "no_speech_prob": 0.20761214196681976}, {"id": 111, "seek": 52748, "start": 537.48,
  "end": 543.48, "text": " There is a large number of like previous work in that area.",
  "tokens": [50864, 821, 307, 257, 2416, 1230, 295, 411, 3894, 589, 294, 300, 1859,
  13, 51164], "temperature": 0.0, "avg_logprob": -0.2575679723767267, "compression_ratio":
  1.4325842696629214, "no_speech_prob": 0.20761214196681976}, {"id": 112, "seek":
  52748, "start": 543.48, "end": 549.48, "text": " But you said like you didn''t concern
  yourself with reading too many papers before you started", "tokens": [51164, 583,
  291, 848, 411, 291, 994, 380, 3136, 1803, 365, 3760, 886, 867, 10577, 949, 291,
  1409, 51464], "temperature": 0.0, "avg_logprob": -0.2575679723767267, "compression_ratio":
  1.4325842696629214, "no_speech_prob": 0.20761214196681976}, {"id": 113, "seek":
  52748, "start": 549.48, "end": 551.48, "text": " inventing this new algorithm.",
  "tokens": [51464, 7962, 278, 341, 777, 9284, 13, 51564], "temperature": 0.0, "avg_logprob":
  -0.2575679723767267, "compression_ratio": 1.4325842696629214, "no_speech_prob":
  0.20761214196681976}, {"id": 114, "seek": 52748, "start": 551.48, "end": 552.48,
  "text": " Is that right?", "tokens": [51564, 1119, 300, 558, 30, 51614], "temperature":
  0.0, "avg_logprob": -0.2575679723767267, "compression_ratio": 1.4325842696629214,
  "no_speech_prob": 0.20761214196681976}, {"id": 115, "seek": 55248, "start": 552.48,
  "end": 558.48, "text": " Yeah, sure, sure, we read papers, but they were not really
  relevant.", "tokens": [50364, 865, 11, 988, 11, 988, 11, 321, 1401, 10577, 11, 457,
  436, 645, 406, 534, 7340, 13, 50664], "temperature": 0.0, "avg_logprob": -0.2470530027984291,
  "compression_ratio": 1.721951219512195, "no_speech_prob": 0.027562787756323814},
  {"id": 116, "seek": 55248, "start": 558.48, "end": 563.48, "text": " So we read
  papers on network science.", "tokens": [50664, 407, 321, 1401, 10577, 322, 3209,
  3497, 13, 50914], "temperature": 0.0, "avg_logprob": -0.2470530027984291, "compression_ratio":
  1.721951219512195, "no_speech_prob": 0.027562787756323814}, {"id": 117, "seek":
  55248, "start": 563.48, "end": 569.48, "text": " And so we tried to so there was
  a problem with building like this, no navigable small roles.", "tokens": [50914,
  400, 370, 321, 3031, 281, 370, 456, 390, 257, 1154, 365, 2390, 411, 341, 11, 572,
  7407, 712, 1359, 9604, 13, 51214], "temperature": 0.0, "avg_logprob": -0.2470530027984291,
  "compression_ratio": 1.721951219512195, "no_speech_prob": 0.027562787756323814},
  {"id": 118, "seek": 55248, "start": 569.48, "end": 573.48, "text": " So like not
  every small network is navigable.", "tokens": [51214, 407, 411, 406, 633, 1359,
  3209, 307, 7407, 712, 13, 51414], "temperature": 0.0, "avg_logprob": -0.2470530027984291,
  "compression_ratio": 1.721951219512195, "no_speech_prob": 0.027562787756323814},
  {"id": 119, "seek": 55248, "start": 573.48, "end": 576.48, "text": " Like most models
  are not.", "tokens": [51414, 1743, 881, 5245, 366, 406, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.2470530027984291, "compression_ratio": 1.721951219512195,
  "no_speech_prob": 0.027562787756323814}, {"id": 120, "seek": 55248, "start": 576.48,
  "end": 581.48, "text": " So we wanted to build navigable small and there were also
  didn''t understand like.", "tokens": [51564, 407, 321, 1415, 281, 1322, 7407, 712,
  1359, 293, 456, 645, 611, 994, 380, 1223, 411, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.2470530027984291, "compression_ratio": 1.721951219512195, "no_speech_prob": 0.027562787756323814},
  {"id": 121, "seek": 58148, "start": 581.48, "end": 591.48, "text": " Like what what
  was the criteria like what is like how we could make it and we reinvented like this.",
  "tokens": [50364, 1743, 437, 437, 390, 264, 11101, 411, 437, 307, 411, 577, 321,
  727, 652, 309, 293, 321, 33477, 292, 411, 341, 13, 50864], "temperature": 0.0, "avg_logprob":
  -0.3275919521556181, "compression_ratio": 1.6467391304347827, "no_speech_prob":
  0.0074677495285868645}, {"id": 122, "seek": 58148, "start": 591.48, "end": 602.48,
  "text": " Dillon or graphs inside the company and after like you reinvented like
  you know starting to search and see there are lots of papers who did the same.",
  "tokens": [50864, 413, 30961, 420, 24877, 1854, 264, 2237, 293, 934, 411, 291, 33477,
  292, 411, 291, 458, 2891, 281, 3164, 293, 536, 456, 366, 3195, 295, 10577, 567,
  630, 264, 912, 13, 51414], "temperature": 0.0, "avg_logprob": -0.3275919521556181,
  "compression_ratio": 1.6467391304347827, "no_speech_prob": 0.0074677495285868645},
  {"id": 123, "seek": 58148, "start": 602.48, "end": 603.48, "text": " Right.", "tokens":
  [51414, 1779, 13, 51464], "temperature": 0.0, "avg_logprob": -0.3275919521556181,
  "compression_ratio": 1.6467391304347827, "no_speech_prob": 0.0074677495285868645},
  {"id": 124, "seek": 58148, "start": 603.48, "end": 604.48, "text": " Yeah.", "tokens":
  [51464, 865, 13, 51514], "temperature": 0.0, "avg_logprob": -0.3275919521556181,
  "compression_ratio": 1.6467391304347827, "no_speech_prob": 0.0074677495285868645},
  {"id": 125, "seek": 58148, "start": 604.48, "end": 606.48, "text": " So yeah.",
  "tokens": [51514, 407, 1338, 13, 51614], "temperature": 0.0, "avg_logprob": -0.3275919521556181,
  "compression_ratio": 1.6467391304347827, "no_speech_prob": 0.0074677495285868645},
  {"id": 126, "seek": 58148, "start": 606.48, "end": 608.48, "text": " So we went
  the other way.", "tokens": [51614, 407, 321, 1437, 264, 661, 636, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.3275919521556181, "compression_ratio": 1.6467391304347827,
  "no_speech_prob": 0.0074677495285868645}, {"id": 127, "seek": 58148, "start": 608.48,
  "end": 609.48, "text": " Yeah.", "tokens": [51714, 865, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.3275919521556181, "compression_ratio": 1.6467391304347827,
  "no_speech_prob": 0.0074677495285868645}, {"id": 128, "seek": 60948, "start": 609.48,
  "end": 625.48, "text": " So now that you mentioned this thing like can you actually
  please introduce this concepts at least on high level to our audience like what
  is a small world what is like what white it''s to be navigable kind of a little
  bit like more to the user facing", "tokens": [50364, 407, 586, 300, 291, 2835, 341,
  551, 411, 393, 291, 767, 1767, 5366, 341, 10392, 412, 1935, 322, 1090, 1496, 281,
  527, 4034, 411, 437, 307, 257, 1359, 1002, 437, 307, 411, 437, 2418, 309, 311, 281,
  312, 7407, 712, 733, 295, 257, 707, 857, 411, 544, 281, 264, 4195, 7170, 51164],
  "temperature": 0.0, "avg_logprob": -0.16488108559260292, "compression_ratio": 1.583815028901734,
  "no_speech_prob": 0.011575441807508469}, {"id": 129, "seek": 60948, "start": 625.48,
  "end": 628.48, "text": " level if it''s possible.", "tokens": [51164, 1496, 498,
  309, 311, 1944, 13, 51314], "temperature": 0.0, "avg_logprob": -0.16488108559260292,
  "compression_ratio": 1.583815028901734, "no_speech_prob": 0.011575441807508469},
  {"id": 130, "seek": 62848, "start": 628.48, "end": 633.48, "text": " Well, like
  navigable small world so you have a large network.", "tokens": [50364, 1042, 11,
  411, 7407, 712, 1359, 1002, 370, 291, 362, 257, 2416, 3209, 13, 50614], "temperature":
  0.0, "avg_logprob": -0.1980497802513233, "compression_ratio": 1.6229508196721312,
  "no_speech_prob": 0.03176131099462509}, {"id": 131, "seek": 62848, "start": 633.48,
  "end": 648.48, "text": " And so navigable small world that means you can find paths
  between like arbitrary elements in this network using which is a logarithmic scale.",
  "tokens": [50614, 400, 370, 7407, 712, 1359, 1002, 300, 1355, 291, 393, 915, 14518,
  1296, 411, 23211, 4959, 294, 341, 3209, 1228, 597, 307, 257, 41473, 355, 13195,
  4373, 13, 51364], "temperature": 0.0, "avg_logprob": -0.1980497802513233, "compression_ratio":
  1.6229508196721312, "no_speech_prob": 0.03176131099462509}, {"id": 132, "seek":
  62848, "start": 648.48, "end": 655.48, "text": " So the number of hopes can be done
  with the rhythmic and you can use only local information.", "tokens": [51364, 407,
  264, 1230, 295, 13681, 393, 312, 1096, 365, 264, 46967, 293, 291, 393, 764, 787,
  2654, 1589, 13, 51714], "temperature": 0.0, "avg_logprob": -0.1980497802513233,
  "compression_ratio": 1.6229508196721312, "no_speech_prob": 0.03176131099462509},
  {"id": 133, "seek": 65548, "start": 655.48, "end": 667.48, "text": " And do like
  something like greedy search like greedy searches allow and if you can find like
  the path and the algorithmic steps to your network is navigable.", "tokens": [50364,
  400, 360, 411, 746, 411, 28228, 3164, 411, 28228, 26701, 2089, 293, 498, 291, 393,
  915, 411, 264, 3100, 293, 264, 9284, 299, 4439, 281, 428, 3209, 307, 7407, 712,
  13, 50964], "temperature": 0.0, "avg_logprob": -0.37479050305424905, "compression_ratio":
  1.5629629629629629, "no_speech_prob": 0.032770946621894836}, {"id": 134, "seek":
  65548, "start": 667.48, "end": 673.48, "text": " And that small world part like
  why is it small small.", "tokens": [50964, 400, 300, 1359, 1002, 644, 411, 983,
  307, 309, 1359, 1359, 13, 51264], "temperature": 0.0, "avg_logprob": -0.37479050305424905,
  "compression_ratio": 1.5629629629629629, "no_speech_prob": 0.032770946621894836},
  {"id": 135, "seek": 67348, "start": 673.48, "end": 689.48, "text": " And that''s
  like history how he''s historical reasons so there was like a famous like milligram
  experiment where they they send letters from one person like from random person
  to some target person.", "tokens": [50364, 400, 300, 311, 411, 2503, 577, 415, 311,
  8584, 4112, 370, 456, 390, 411, 257, 4618, 411, 38298, 5120, 689, 436, 436, 2845,
  7825, 490, 472, 954, 411, 490, 4974, 954, 281, 512, 3779, 954, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.3330188536308181, "compression_ratio": 1.7676767676767677,
  "no_speech_prob": 0.05594843998551369}, {"id": 136, "seek": 67348, "start": 689.48,
  "end": 699.48, "text": " That was kind of greedy like greedy search for connections
  very similar to this and that that''s called like small world experiment so like
  a small world.", "tokens": [51164, 663, 390, 733, 295, 28228, 411, 28228, 3164,
  337, 9271, 588, 2531, 281, 341, 293, 300, 300, 311, 1219, 411, 1359, 1002, 5120,
  370, 411, 257, 1359, 1002, 13, 51664], "temperature": 0.0, "avg_logprob": -0.3330188536308181,
  "compression_ratio": 1.7676767676767677, "no_speech_prob": 0.05594843998551369},
  {"id": 137, "seek": 69948, "start": 699.48, "end": 710.48, "text": " And real networks
  like people have like real networks have low diameter like human human connection
  networks.", "tokens": [50364, 400, 957, 9590, 411, 561, 362, 411, 957, 9590, 362,
  2295, 14196, 411, 1952, 1952, 4984, 9590, 13, 50914], "temperature": 0.0, "avg_logprob":
  -0.16736959431269396, "compression_ratio": 1.7075471698113207, "no_speech_prob":
  0.11016340553760529}, {"id": 138, "seek": 69948, "start": 710.48, "end": 718.48,
  "text": " And they are navigable like at least according to milligram experiments
  and like subsequent experiments.", "tokens": [50914, 400, 436, 366, 7407, 712, 411,
  412, 1935, 4650, 281, 38298, 12050, 293, 411, 19962, 12050, 13, 51314], "temperature":
  0.0, "avg_logprob": -0.16736959431269396, "compression_ratio": 1.7075471698113207,
  "no_speech_prob": 0.11016340553760529}, {"id": 139, "seek": 69948, "start": 718.48,
  "end": 728.48, "text": " Is it kind of related in common terms like to six handshakes
  that you need to connect every random person with another random person on the planet.",
  "tokens": [51314, 1119, 309, 733, 295, 4077, 294, 2689, 2115, 411, 281, 2309, 2377,
  71, 3419, 300, 291, 643, 281, 1745, 633, 4974, 954, 365, 1071, 4974, 954, 322, 264,
  5054, 13, 51814], "temperature": 0.0, "avg_logprob": -0.16736959431269396, "compression_ratio":
  1.7075471698113207, "no_speech_prob": 0.11016340553760529}, {"id": 140, "seek":
  72848, "start": 728.48, "end": 737.48, "text": " Yes, yes, so that''s that''s like
  that experiment is pretty sure I think it''s done in the 60s so yeah so.", "tokens":
  [50364, 1079, 11, 2086, 11, 370, 300, 311, 300, 311, 411, 300, 5120, 307, 1238,
  988, 286, 519, 309, 311, 1096, 294, 264, 4060, 82, 370, 1338, 370, 13, 50814], "temperature":
  0.0, "avg_logprob": -0.17175868806384859, "compression_ratio": 1.6909871244635193,
  "no_speech_prob": 0.0020402243826538324}, {"id": 141, "seek": 72848, "start": 737.48,
  "end": 745.48, "text": " And so the navigable part is basically like if we put this
  in the context of search right so.", "tokens": [50814, 400, 370, 264, 7407, 712,
  644, 307, 1936, 411, 498, 321, 829, 341, 294, 264, 4319, 295, 3164, 558, 370, 13,
  51214], "temperature": 0.0, "avg_logprob": -0.17175868806384859, "compression_ratio":
  1.6909871244635193, "no_speech_prob": 0.0020402243826538324}, {"id": 142, "seek":
  72848, "start": 745.48, "end": 756.48, "text": " So let''s say I have local information
  I''m here I would like to travel from here let''s say I''m in Helsinki I would like
  to travel to New York like how do I travel right I need to go to the airport.",
  "tokens": [51214, 407, 718, 311, 584, 286, 362, 2654, 1589, 286, 478, 510, 286,
  576, 411, 281, 3147, 490, 510, 718, 311, 584, 286, 478, 294, 45429, 41917, 286,
  576, 411, 281, 3147, 281, 1873, 3609, 411, 577, 360, 286, 3147, 558, 286, 643, 281,
  352, 281, 264, 10155, 13, 51764], "temperature": 0.0, "avg_logprob": -0.17175868806384859,
  "compression_ratio": 1.6909871244635193, "no_speech_prob": 0.0020402243826538324},
  {"id": 143, "seek": 75648, "start": 756.48, "end": 766.48, "text": " From the airport
  I will travel maybe to some city in Europe from there I will change you know the
  airplane and then fly over to New York.", "tokens": [50364, 3358, 264, 10155, 286,
  486, 3147, 1310, 281, 512, 2307, 294, 3315, 490, 456, 286, 486, 1319, 291, 458,
  264, 17130, 293, 550, 3603, 670, 281, 1873, 3609, 13, 50864], "temperature": 0.0,
  "avg_logprob": -0.10633975015559667, "compression_ratio": 1.5487179487179488, "no_speech_prob":
  0.025776835158467293}, {"id": 144, "seek": 75648, "start": 766.48, "end": 777.48,
  "text": " I''m making it a little bit more complicated there is a direct flight
  to New York from Helsinki but okay maybe that wasn''t right is that analogous to
  navigable part.", "tokens": [50864, 286, 478, 1455, 309, 257, 707, 857, 544, 6179,
  456, 307, 257, 2047, 7018, 281, 1873, 3609, 490, 45429, 41917, 457, 1392, 1310,
  300, 2067, 380, 558, 307, 300, 16660, 563, 281, 7407, 712, 644, 13, 51414], "temperature":
  0.0, "avg_logprob": -0.10633975015559667, "compression_ratio": 1.5487179487179488,
  "no_speech_prob": 0.025776835158467293}, {"id": 145, "seek": 77748, "start": 777.48,
  "end": 792.48, "text": " Yes, yes, so like generally like that you can pinpoint
  that but if you start and finish in like small local airports which usually don''t
  have connections, my magic connection so they connected to hops.", "tokens": [50364,
  1079, 11, 2086, 11, 370, 411, 5101, 411, 300, 291, 393, 40837, 300, 457, 498, 291,
  722, 293, 2413, 294, 411, 1359, 2654, 36561, 597, 2673, 500, 380, 362, 9271, 11,
  452, 5585, 4984, 370, 436, 4582, 281, 47579, 13, 51114], "temperature": 0.0, "avg_logprob":
  -0.24590779472799862, "compression_ratio": 1.7465437788018434, "no_speech_prob":
  0.048686470836400986}, {"id": 146, "seek": 77748, "start": 792.48, "end": 803.48,
  "text": " Yeah, and that is one of the model of navigable small roles so there are
  like Kleinberg''s model which doesn''t have hops so you can also build navigable
  small walls without hops.", "tokens": [51114, 865, 11, 293, 300, 307, 472, 295,
  264, 2316, 295, 7407, 712, 1359, 9604, 370, 456, 366, 411, 33327, 6873, 311, 2316,
  597, 1177, 380, 362, 47579, 370, 291, 393, 611, 1322, 7407, 712, 1359, 7920, 1553,
  47579, 13, 51664], "temperature": 0.0, "avg_logprob": -0.24590779472799862, "compression_ratio":
  1.7465437788018434, "no_speech_prob": 0.048686470836400986}, {"id": 147, "seek":
  80348, "start": 803.48, "end": 832.48, "text": " But they have polylogarifmix coedizian
  so if you want to have polylogarifmix coedizian so maybe I''ll ask you to provide
  some references later so especially for those who want to dig deeper into the smithematics
  like you mentioned these different algorithms like many of them are new to me at
  least so I''m sure to our part of our audience.", "tokens": [50364, 583, 436, 362,
  6754, 4987, 289, 351, 76, 970, 598, 292, 590, 952, 370, 498, 291, 528, 281, 362,
  6754, 4987, 289, 351, 76, 970, 598, 292, 590, 952, 370, 1310, 286, 603, 1029, 291,
  281, 2893, 512, 15400, 1780, 370, 2318, 337, 729, 567, 528, 281, 2528, 7731, 666,
  264, 899, 355, 37541, 411, 291, 2835, 613, 819, 14642, 411, 867, 295, 552, 366,
  777, 281, 385, 412, 1935, 370, 286, 478, 988, 281, 527, 644, 295, 527, 4034, 13,
  51814], "temperature": 0.0, "avg_logprob": -0.3868344475241268, "compression_ratio":
  1.6732673267326732, "no_speech_prob": 0.13643303513526917}, {"id": 148, "seek":
  83248, "start": 832.48, "end": 856.48, "text": " Part of our audience as well and
  I wanted to also ask you like on the context of your invention like what was the
  input so you said like you had a lot of data right from computer vision but like
  was there something else like dimensionality or some other constraint that was kind
  of tough for previous algorithms like a LSH or you know any other.", "tokens": [50364,
  4100, 295, 527, 4034, 382, 731, 293, 286, 1415, 281, 611, 1029, 291, 411, 322, 264,
  4319, 295, 428, 22265, 411, 437, 390, 264, 4846, 370, 291, 848, 411, 291, 632, 257,
  688, 295, 1412, 558, 490, 3820, 5201, 457, 411, 390, 456, 746, 1646, 411, 10139,
  1860, 420, 512, 661, 25534, 300, 390, 733, 295, 4930, 337, 3894, 14642, 411, 257,
  441, 17308, 420, 291, 458, 604, 661, 13, 51564], "temperature": 0.0, "avg_logprob":
  -0.12364180023605759, "compression_ratio": 1.619718309859155, "no_speech_prob":
  0.01772996410727501}, {"id": 149, "seek": 85648, "start": 856.48, "end": 868.48,
  "text": " Well, there LSH didn''t even work so we worked with like three structures
  we have to like how will you do LSH.", "tokens": [50364, 1042, 11, 456, 441, 17308,
  994, 380, 754, 589, 370, 321, 2732, 365, 411, 1045, 9227, 321, 362, 281, 411, 577,
  486, 291, 360, 441, 17308, 13, 50964], "temperature": 0.0, "avg_logprob": -0.35864014779367753,
  "compression_ratio": 1.1595744680851063, "no_speech_prob": 0.16624902188777924},
  {"id": 150, "seek": 86848, "start": 868.48, "end": 893.48, "text": " Yeah, for and
  for LSH so I thought that those are not practical algorithms so even when I spoke
  with people who like were writing a lot of papers on LSH they like expressed doubts
  and whether those algorithms are practical so they are not learnable so they cannot
  take advantage of the data that you have so like that.", "tokens": [50364, 865,
  11, 337, 293, 337, 441, 17308, 370, 286, 1194, 300, 729, 366, 406, 8496, 14642,
  370, 754, 562, 286, 7179, 365, 561, 567, 411, 645, 3579, 257, 688, 295, 10577, 322,
  441, 17308, 436, 411, 12675, 22618, 293, 1968, 729, 14642, 366, 8496, 370, 436,
  366, 406, 1466, 712, 370, 436, 2644, 747, 5002, 295, 264, 1412, 300, 291, 362, 370,
  411, 300, 13, 51614], "temperature": 0.0, "avg_logprob": -0.1623264948527018, "compression_ratio":
  1.6476683937823835, "no_speech_prob": 0.2989859879016876}, {"id": 151, "seek": 89348,
  "start": 894.08, "end": 901.48, "text": " And like what what they told is like they
  see as quantization as just a better version of practical version of LSH.", "tokens":
  [50394, 400, 411, 437, 437, 436, 1907, 307, 411, 436, 536, 382, 4426, 2144, 382,
  445, 257, 1101, 3037, 295, 8496, 3037, 295, 441, 17308, 13, 50764], "temperature":
  0.0, "avg_logprob": -0.14685373163934964, "compression_ratio": 1.5459183673469388,
  "no_speech_prob": 0.020174356177449226}, {"id": 152, "seek": 89348, "start": 903.48,
  "end": 917.48, "text": " Yeah right and so actually I''m really interested like
  how did you set up to invent the algorithm like I can just give you briefly like
  in the recent billion scale vector search challenge.", "tokens": [50864, 865, 558,
  293, 370, 767, 286, 478, 534, 3102, 411, 577, 630, 291, 992, 493, 281, 7962, 264,
  9284, 411, 286, 393, 445, 976, 291, 10515, 411, 294, 264, 5162, 5218, 4373, 8062,
  3164, 3430, 13, 51564], "temperature": 0.0, "avg_logprob": -0.14685373163934964,
  "compression_ratio": 1.5459183673469388, "no_speech_prob": 0.020174356177449226},
  {"id": 153, "seek": 91748, "start": 918.48, "end": 939.48, "text": " We had like
  a small team and one of our team members actually implemented like a small change
  in product quantization layer like basically how you shuffle the dimensions in the
  vector and he achieved like 12% recall increase over the baseline you know the Facebook
  sell algorithm.", "tokens": [50414, 492, 632, 411, 257, 1359, 1469, 293, 472, 295,
  527, 1469, 2679, 767, 12270, 411, 257, 1359, 1319, 294, 1674, 4426, 2144, 4583,
  411, 1936, 577, 291, 39426, 264, 12819, 294, 264, 8062, 293, 415, 11042, 411, 2272,
  4, 9901, 3488, 670, 264, 20518, 291, 458, 264, 4384, 3607, 9284, 13, 51464], "temperature":
  0.0, "avg_logprob": -0.13454842133955522, "compression_ratio": 1.5135135135135136,
  "no_speech_prob": 0.0518990121781826}, {"id": 154, "seek": 93948, "start": 939.48,
  "end": 955.48, "text": " I didn''t like have that much knowledge I''ve read your
  paper I''ve read other papers and so I was just thinking okay if I if I would start
  from first principles how would I solve it like I know nothing about this problem
  right so like how can I solve you know the search in multi-dimensional space.",
  "tokens": [50364, 286, 994, 380, 411, 362, 300, 709, 3601, 286, 600, 1401, 428,
  3035, 286, 600, 1401, 661, 10577, 293, 370, 286, 390, 445, 1953, 1392, 498, 286,
  498, 286, 576, 722, 490, 700, 9156, 577, 576, 286, 5039, 309, 411, 286, 458, 1825,
  466, 341, 1154, 558, 370, 411, 577, 393, 286, 5039, 291, 458, 264, 3164, 294, 4825,
  12, 18759, 1901, 13, 51164], "temperature": 0.0, "avg_logprob": -0.11763519610998766,
  "compression_ratio": 1.707142857142857, "no_speech_prob": 0.005949764046818018},
  {"id": 155, "seek": 93948, "start": 955.48, "end": 967.48, "text": " And so I actually
  implemented a very very simple algorithm using your algorithm as one of the components
  maybe we can talk later about it but like how did you start inventing H&S W.", "tokens":
  [51164, 400, 370, 286, 767, 12270, 257, 588, 588, 2199, 9284, 1228, 428, 9284, 382,
  472, 295, 264, 6677, 1310, 321, 393, 751, 1780, 466, 309, 457, 411, 577, 630, 291,
  722, 7962, 278, 389, 5, 50, 343, 13, 51764], "temperature": 0.0, "avg_logprob":
  -0.11763519610998766, "compression_ratio": 1.707142857142857, "no_speech_prob":
  0.005949764046818018}, {"id": 156, "seek": 96948, "start": 970.48, "end": 987.48,
  "text": " Well H&S W had a pretty assessor so it has like an NSW it''s also called
  MSW or SW graph in different places like depending on where you look so and there
  I just so it had problems.", "tokens": [50414, 1042, 389, 5, 50, 343, 632, 257,
  1238, 5877, 284, 370, 309, 575, 411, 364, 15943, 54, 309, 311, 611, 1219, 7395,
  54, 420, 20346, 4295, 294, 819, 3190, 411, 5413, 322, 689, 291, 574, 370, 293, 456,
  286, 445, 370, 309, 632, 2740, 13, 51264], "temperature": 0.0, "avg_logprob": -0.21885568268445074,
  "compression_ratio": 1.3235294117647058, "no_speech_prob": 0.01921668089926243},
  {"id": 157, "seek": 98748, "start": 988.48, "end": 1005.48, "text": " So it had
  several problems but like for like if you don''t think about distributed setup the
  main problem it had poly algorithmic scalability with a number of elements and that
  killed the performance on low dimensional data.", "tokens": [50414, 407, 309, 632,
  2940, 2740, 457, 411, 337, 411, 498, 291, 500, 380, 519, 466, 12631, 8657, 264,
  2135, 1154, 309, 632, 6754, 9284, 299, 15664, 2310, 365, 257, 1230, 295, 4959, 293,
  300, 4652, 264, 3389, 322, 2295, 18795, 1412, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.22851226640784222, "compression_ratio": 1.457516339869281, "no_speech_prob":
  0.042576249688863754}, {"id": 158, "seek": 100548, "start": 1006.48, "end": 1034.48,
  "text": " So there were like comparison works like one by Leonid Bytes of where
  he evaluated different algorithms and like its performance really like it didn''t
  perform that well on some data set and the loss was by many orders of magnitude
  so it could be like one like 1000 times slower than the best solution and yeah.",
  "tokens": [50414, 407, 456, 645, 411, 9660, 1985, 411, 472, 538, 13244, 327, 3146,
  7269, 295, 689, 415, 25509, 819, 14642, 293, 411, 1080, 3389, 534, 411, 309, 994,
  380, 2042, 300, 731, 322, 512, 1412, 992, 293, 264, 4470, 390, 538, 867, 9470, 295,
  15668, 370, 309, 727, 312, 411, 472, 411, 9714, 1413, 14009, 813, 264, 1151, 3827,
  293, 1338, 13, 51814], "temperature": 0.0, "avg_logprob": -0.21878616626446062,
  "compression_ratio": 1.5422885572139304, "no_speech_prob": 0.06631921976804733},
  {"id": 159, "seek": 103448, "start": 1034.48, "end": 1048.48, "text": " So the work
  on H&S W were targeted at just improving the previous version so it wouldn''t have
  this problem and like ideally would perform the best on all setups.", "tokens":
  [50364, 407, 264, 589, 322, 389, 5, 50, 343, 645, 15045, 412, 445, 11470, 264, 3894,
  3037, 370, 309, 2759, 380, 362, 341, 1154, 293, 411, 22915, 576, 2042, 264, 1151,
  322, 439, 46832, 13, 51064], "temperature": 0.0, "avg_logprob": -0.1654958163990694,
  "compression_ratio": 1.4285714285714286, "no_speech_prob": 0.003002072451636195},
  {"id": 160, "seek": 103448, "start": 1048.48, "end": 1052.48, "text": " So yeah
  and that that that that has been solved.", "tokens": [51064, 407, 1338, 293, 300,
  300, 300, 300, 575, 668, 13041, 13, 51264], "temperature": 0.0, "avg_logprob": -0.1654958163990694,
  "compression_ratio": 1.4285714285714286, "no_speech_prob": 0.003002072451636195},
  {"id": 161, "seek": 105248, "start": 1053.48, "end": 1071.48, "text": " Right but
  like you still needed to add that magical age in front of it so you made it hierarchical
  like what what pushed you in the direction of making it hierarchical and what what
  did you think that it might work or was it like as a result of experimentation that
  it proved to work.", "tokens": [50414, 1779, 457, 411, 291, 920, 2978, 281, 909,
  300, 12066, 3205, 294, 1868, 295, 309, 370, 291, 1027, 309, 35250, 804, 411, 437,
  437, 9152, 291, 294, 264, 3513, 295, 1455, 309, 35250, 804, 293, 437, 437, 630,
  291, 519, 300, 309, 1062, 589, 420, 390, 309, 411, 382, 257, 1874, 295, 37142, 300,
  309, 14617, 281, 589, 13, 51314], "temperature": 0.0, "avg_logprob": -0.1273075890919519,
  "compression_ratio": 1.7005988023952097, "no_speech_prob": 0.042004723101854324},
  {"id": 162, "seek": 107148, "start": 1072.48, "end": 1097.48, "text": " Well yeah
  that that that''s that''s yeah that has many ingredients in it so for for one thing
  when I worked with the startup mirror labs so we had a different problem with distributed
  index that NSW had a pleasant quality that the hubs that are created in the network
  are the first elements.", "tokens": [50414, 1042, 1338, 300, 300, 300, 311, 300,
  311, 1338, 300, 575, 867, 6952, 294, 309, 370, 337, 337, 472, 551, 562, 286, 2732,
  365, 264, 18578, 8013, 20339, 370, 321, 632, 257, 819, 1154, 365, 12631, 8186, 300,
  15943, 54, 632, 257, 16232, 3125, 300, 264, 46870, 300, 366, 2942, 294, 264, 3209,
  366, 264, 700, 4959, 13, 51664], "temperature": 0.0, "avg_logprob": -0.25532833222419987,
  "compression_ratio": 1.6420454545454546, "no_speech_prob": 0.03184979781508446},
  {"id": 163, "seek": 109748, "start": 1098.48, "end": 1121.48, "text": " So and the
  for distributed system you would want to add new nodes to the system and you will
  have much capacity like increase the capacity of the system but because all your
  hubs on in the first notes like in the older notes because they have been created
  before new nodes even existed.", "tokens": [50414, 407, 293, 264, 337, 12631, 1185,
  291, 576, 528, 281, 909, 777, 13891, 281, 264, 1185, 293, 291, 486, 362, 709, 6042,
  411, 3488, 264, 6042, 295, 264, 1185, 457, 570, 439, 428, 46870, 322, 294, 264,
  700, 5570, 411, 294, 264, 4906, 5570, 570, 436, 362, 668, 2942, 949, 777, 13891,
  754, 13135, 13, 51564], "temperature": 0.0, "avg_logprob": -0.2255421169733597,
  "compression_ratio": 1.7228915662650603, "no_speech_prob": 0.015513861551880836},
  {"id": 164, "seek": 112148, "start": 1121.48, "end": 1145.48, "text": " The traffic
  is routed through the same old notes which make it not scalable and we spent quite
  a lot of time on figuring out how to solve it and there at some point I''ve noticed
  that like our NSW approach is pretty similar to skip list in terms of what what
  has been what is being protest as final network.", "tokens": [50364, 440, 6419,
  307, 4020, 292, 807, 264, 912, 1331, 5570, 597, 652, 309, 406, 38481, 293, 321,
  4418, 1596, 257, 688, 295, 565, 322, 15213, 484, 577, 281, 5039, 309, 293, 456,
  412, 512, 935, 286, 600, 5694, 300, 411, 527, 15943, 54, 3109, 307, 1238, 2531,
  281, 10023, 1329, 294, 2115, 295, 437, 437, 575, 668, 437, 307, 885, 11281, 382,
  2572, 3209, 13, 51564], "temperature": 0.0, "avg_logprob": -0.15753530419391135,
  "compression_ratio": 1.5223880597014925, "no_speech_prob": 0.026150261983275414},
  {"id": 165, "seek": 114548, "start": 1145.48, "end": 1168.48, "text": " The idea
  is like if you if you create a skip list for one D and create the NSW for one D
  and then like for skip list you just merge the all all links regardless of player
  you will get a similar network in terms of like degree distribution like distance
  distribution well all major properties.", "tokens": [50364, 440, 1558, 307, 411,
  498, 291, 498, 291, 1884, 257, 10023, 1329, 337, 472, 413, 293, 1884, 264, 15943,
  54, 337, 472, 413, 293, 550, 411, 337, 10023, 1329, 291, 445, 22183, 264, 439, 439,
  6123, 10060, 295, 4256, 291, 486, 483, 257, 2531, 3209, 294, 2115, 295, 411, 4314,
  7316, 411, 4560, 7316, 731, 439, 2563, 7221, 13, 51514], "temperature": 0.0, "avg_logprob":
  -0.16269907875666542, "compression_ratio": 1.7176470588235293, "no_speech_prob":
  0.03380730375647545}, {"id": 166, "seek": 116848, "start": 1168.48, "end": 1193.48,
  "text": " So but skip list doesn''t have this property so you can add new nodes
  and they can have like they can have higher levels and like your traffic will be
  a road through notes in your form like across your distributed system so and that
  thing we knew like from the startup that there is a like equivalence but that was
  only for the problem of distributed search.", "tokens": [50364, 407, 457, 10023,
  1329, 1177, 380, 362, 341, 4707, 370, 291, 393, 909, 777, 13891, 293, 436, 393,
  362, 411, 436, 393, 362, 2946, 4358, 293, 411, 428, 6419, 486, 312, 257, 3060, 807,
  5570, 294, 428, 1254, 411, 2108, 428, 12631, 1185, 370, 293, 300, 551, 321, 2586,
  411, 490, 264, 18578, 300, 456, 307, 257, 411, 9052, 655, 457, 300, 390, 787, 337,
  264, 1154, 295, 12631, 3164, 13, 51614], "temperature": 0.0, "avg_logprob": -0.23071039835611978,
  "compression_ratio": 1.733009708737864, "no_speech_prob": 0.01258369255810976},
  {"id": 167, "seek": 119348, "start": 1193.48, "end": 1220.48, "text": " So it would
  still use the same polylogar if Michael like 3d search algorithm like which doesn''t
  think about like what is that how many links you have on a note so that was shelved
  for that reasons in the startup but then so after ID PhD so like I wanted to publish
  a good paper on network science.", "tokens": [50364, 407, 309, 576, 920, 764, 264,
  912, 6754, 4987, 289, 498, 5116, 411, 805, 67, 3164, 9284, 411, 597, 1177, 380,
  519, 466, 411, 437, 307, 300, 577, 867, 6123, 291, 362, 322, 257, 3637, 370, 300,
  390, 9180, 937, 337, 300, 4112, 294, 264, 18578, 457, 550, 370, 934, 7348, 14476,
  370, 411, 286, 1415, 281, 11374, 257, 665, 3035, 322, 3209, 3497, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.4356955929078918, "compression_ratio": 1.485, "no_speech_prob":
  0.06325482577085495}, {"id": 168, "seek": 122048, "start": 1220.48, "end": 1249.48,
  "text": " And there like it was and I like there is there is a result that we can
  create a new navigable networks which a method which was not known before so I tried
  to publish it in nature so it was rejected like nature physics also rejected that
  it was rejected by editors then in scientific reports was rejected after a review
  and then like it was finally published in plus one.", "tokens": [50414, 400, 456,
  411, 309, 390, 293, 286, 411, 456, 307, 456, 307, 257, 1874, 300, 321, 393, 1884,
  257, 777, 7407, 712, 9590, 597, 257, 3170, 597, 390, 406, 2570, 949, 370, 286, 3031,
  281, 11374, 309, 294, 3687, 370, 309, 390, 15749, 411, 3687, 10649, 611, 15749,
  300, 309, 390, 15749, 538, 31446, 550, 294, 8134, 7122, 390, 15749, 934, 257, 3131,
  293, 550, 411, 309, 390, 2721, 6572, 294, 1804, 472, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.20691304392628856, "compression_ratio": 1.8235294117647058,
  "no_speech_prob": 0.032385438680648804}, {"id": 169, "seek": 125048, "start": 1250.48,
  "end": 1258.48, "text": " And I think like I really like this paper so that was
  like the most surprising result I think I got but yet it''s not really decided.",
  "tokens": [50364, 400, 286, 519, 411, 286, 534, 411, 341, 3035, 370, 300, 390, 411,
  264, 881, 8830, 1874, 286, 519, 286, 658, 457, 1939, 309, 311, 406, 534, 3047, 13,
  50764], "temperature": 0.0, "avg_logprob": -0.19177235727724823, "compression_ratio":
  1.7627118644067796, "no_speech_prob": 0.011710943654179573}, {"id": 170, "seek":
  125048, "start": 1259.48, "end": 1279.48, "text": " And as a byproduct of this I
  did a comparison to other navigable small world methods and so like maybe I have
  maybe like this approach with like the old vision that you can apply like you can
  look at the real world networks and replicate it and like computer system and they
  will be.", "tokens": [50814, 400, 382, 257, 538, 33244, 295, 341, 286, 630, 257,
  9660, 281, 661, 7407, 712, 1359, 1002, 7150, 293, 370, 411, 1310, 286, 362, 1310,
  411, 341, 3109, 365, 411, 264, 1331, 5201, 300, 291, 393, 3079, 411, 291, 393, 574,
  412, 264, 957, 1002, 9590, 293, 25356, 309, 293, 411, 3820, 1185, 293, 436, 486,
  312, 13, 51814], "temperature": 0.0, "avg_logprob": -0.19177235727724823, "compression_ratio":
  1.7627118644067796, "no_speech_prob": 0.011710943654179573}, {"id": 171, "seek":
  128048, "start": 1280.48, "end": 1290.48, "text": " So I replicate that the work
  done like scale free navigable navigable small worlds which are very popular thing
  till the moment all.", "tokens": [50364, 407, 286, 25356, 300, 264, 589, 1096, 411,
  4373, 1737, 7407, 712, 7407, 712, 1359, 13401, 597, 366, 588, 3743, 551, 4288, 264,
  1623, 439, 13, 50864], "temperature": 0.0, "avg_logprob": -0.3321691904312525, "compression_ratio":
  1.740566037735849, "no_speech_prob": 0.12275636196136475}, {"id": 172, "seek": 128048,
  "start": 1291.48, "end": 1309.48, "text": " And so that the performance was really
  was like very bad like extremely bad and the reason for that that if you have a
  scale free network and scale free means you have a power low distribution of degree
  and usually they like there is a.", "tokens": [50914, 400, 370, 300, 264, 3389,
  390, 534, 390, 411, 588, 1578, 411, 4664, 1578, 293, 264, 1778, 337, 300, 300, 498,
  291, 362, 257, 4373, 1737, 3209, 293, 4373, 1737, 1355, 291, 362, 257, 1347, 2295,
  7316, 295, 4314, 293, 2673, 436, 411, 456, 307, 257, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.3321691904312525, "compression_ratio": 1.740566037735849,
  "no_speech_prob": 0.12275636196136475}, {"id": 173, "seek": 131048, "start": 1310.48,
  "end": 1339.48, "text": " coefficient gamma and like the best cases was gamma is
  close to two but gamma close to two means that the scalability with the size of
  the network so the degree scale is almost linearly so when you have a like a greedy
  search for the hub so when it goes through the hub like it to play it''s like a
  huge portion of the network so you have like linear scalability instead of like
  ultra logarithmic so log log again which is.", "tokens": [50364, 17619, 15546, 293,
  411, 264, 1151, 3331, 390, 15546, 307, 1998, 281, 732, 457, 15546, 1998, 281, 732,
  1355, 300, 264, 15664, 2310, 365, 264, 2744, 295, 264, 3209, 370, 264, 4314, 4373,
  307, 1920, 8213, 356, 370, 562, 291, 362, 257, 411, 257, 28228, 3164, 337, 264,
  11838, 370, 562, 309, 1709, 807, 264, 11838, 411, 309, 281, 862, 309, 311, 411,
  257, 2603, 8044, 295, 264, 3209, 370, 291, 362, 411, 8213, 15664, 2310, 2602, 295,
  411, 14808, 41473, 355, 13195, 370, 3565, 3565, 797, 597, 307, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.2759508522607947, "compression_ratio": 1.8923766816143497,
  "no_speech_prob": 0.02611459605395794}, {"id": 174, "seek": 134048, "start": 1340.48,
  "end": 1369.48, "text": " They like the number of hope is log log in but at some
  point you evaluate to like almost every point in your network and you have like
  really bad performance and that like that after that realized what was the problem
  with NSW and like I thought all like we already have a solution for that so because
  keep least doesn''t have this problem and so yeah after that I implemented the prototype
  and it worked.", "tokens": [50364, 814, 411, 264, 1230, 295, 1454, 307, 3565, 3565,
  294, 457, 412, 512, 935, 291, 13059, 281, 411, 1920, 633, 935, 294, 428, 3209, 293,
  291, 362, 411, 534, 1578, 3389, 293, 300, 411, 300, 934, 300, 5334, 437, 390, 264,
  1154, 365, 15943, 54, 293, 411, 286, 1194, 439, 411, 321, 1217, 362, 257, 3827,
  337, 300, 370, 570, 1066, 1935, 1177, 380, 362, 341, 1154, 293, 370, 1338, 934,
  300, 286, 12270, 264, 19475, 293, 309, 2732, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.24544520550463572, "compression_ratio": 1.7046413502109705, "no_speech_prob":
  0.024636508896946907}, {"id": 175, "seek": 137048, "start": 1370.48, "end": 1377.48,
  "text": " Working on the like C++ version and the evaluation.", "tokens": [50364,
  18337, 322, 264, 411, 383, 25472, 3037, 293, 264, 13344, 13, 50714], "temperature":
  0.0, "avg_logprob": -0.27485483033316477, "compression_ratio": 1.5225806451612902,
  "no_speech_prob": 0.0366550087928772}, {"id": 176, "seek": 137048, "start": 1377.48,
  "end": 1392.48, "text": " By the way when when you started implementing your prototype
  was it initially in C++ now it wasn''t in in in in Java and Java because Java is
  your favorite language or what was it Java.", "tokens": [50714, 3146, 264, 636,
  562, 562, 291, 1409, 18114, 428, 19475, 390, 309, 9105, 294, 383, 25472, 586, 309,
  2067, 380, 294, 294, 294, 294, 10745, 293, 10745, 570, 10745, 307, 428, 2954, 2856,
  420, 437, 390, 309, 10745, 13, 51464], "temperature": 0.0, "avg_logprob": -0.27485483033316477,
  "compression_ratio": 1.5225806451612902, "no_speech_prob": 0.0366550087928772},
  {"id": 177, "seek": 139248, "start": 1392.48, "end": 1409.48, "text": " Because
  the distributed system like that was implemented in Java so that was close so like
  it was easier to integrate like if you like maybe you were thinking it''s easier
  to integrate in Java right.", "tokens": [50364, 1436, 264, 12631, 1185, 411, 300,
  390, 12270, 294, 10745, 370, 300, 390, 1998, 370, 411, 309, 390, 3571, 281, 13365,
  411, 498, 291, 411, 1310, 291, 645, 1953, 309, 311, 3571, 281, 13365, 294, 10745,
  558, 13, 51214], "temperature": 0.0, "avg_logprob": -0.2186222748017647, "compression_ratio":
  1.6684491978609626, "no_speech_prob": 0.08544904738664627}, {"id": 178, "seek":
  139248, "start": 1409.48, "end": 1420.48, "text": " Well I just know how to code
  it in Java so I code that several times for NSW and that all Java code was released.",
  "tokens": [51214, 1042, 286, 445, 458, 577, 281, 3089, 309, 294, 10745, 370, 286,
  3089, 300, 2940, 1413, 337, 15943, 54, 293, 300, 439, 10745, 3089, 390, 4736, 13,
  51764], "temperature": 0.0, "avg_logprob": -0.2186222748017647, "compression_ratio":
  1.6684491978609626, "no_speech_prob": 0.08544904738664627}, {"id": 179, "seek":
  142048, "start": 1421.48, "end": 1446.48, "text": " So yeah just code it and then
  like I had to transfer it to C++ to make it efficient and like yeah and so there
  is like Leonid bites off so who who is a maintainer of an MS leap so I have been
  in contact with him for quite a while and yeah so it was implemented in the library.",
  "tokens": [50414, 407, 1338, 445, 3089, 309, 293, 550, 411, 286, 632, 281, 5003,
  309, 281, 383, 25472, 281, 652, 309, 7148, 293, 411, 1338, 293, 370, 456, 307, 411,
  13244, 327, 26030, 766, 370, 567, 567, 307, 257, 6909, 260, 295, 364, 7395, 19438,
  370, 286, 362, 668, 294, 3385, 365, 796, 337, 1596, 257, 1339, 293, 1338, 370, 309,
  390, 12270, 294, 264, 6405, 13, 51664], "temperature": 0.0, "avg_logprob": -0.27116899904997455,
  "compression_ratio": 1.541899441340782, "no_speech_prob": 0.02220718376338482},
  {"id": 180, "seek": 144648, "start": 1446.48, "end": 1456.48, "text": " Did you
  like collaborate with him to to to implement it using the enemy sleep sort of the
  most efficient way or.", "tokens": [50364, 2589, 291, 411, 18338, 365, 796, 281,
  281, 281, 4445, 309, 1228, 264, 5945, 2817, 1333, 295, 264, 881, 7148, 636, 420,
  13, 50864], "temperature": 0.0, "avg_logprob": -0.21896951728396946, "compression_ratio":
  1.5422885572139304, "no_speech_prob": 0.014739437028765678}, {"id": 181, "seek":
  144648, "start": 1456.48, "end": 1474.48, "text": " Well first of all like the ideology
  of the library is very close to like what we have been developing so it''s not only
  focused on like typical distances like L2, Cassian or even like inner product.",
  "tokens": [50864, 1042, 700, 295, 439, 411, 264, 23101, 295, 264, 6405, 307, 588,
  1998, 281, 411, 437, 321, 362, 668, 6416, 370, 309, 311, 406, 787, 5178, 322, 411,
  7476, 22182, 411, 441, 17, 11, 383, 640, 952, 420, 754, 411, 7284, 1674, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.21896951728396946, "compression_ratio": 1.5422885572139304,
  "no_speech_prob": 0.014739437028765678}, {"id": 182, "seek": 147448, "start": 1475.48,
  "end": 1489.48, "text": " So yeah it makes sense to compare on all those distances
  and Leonid also had a paper like in a bench like on all of those so we can just
  implement a new algorithm and run a bench.", "tokens": [50414, 407, 1338, 309, 1669,
  2020, 281, 6794, 322, 439, 729, 22182, 293, 13244, 327, 611, 632, 257, 3035, 411,
  294, 257, 10638, 411, 322, 439, 295, 729, 370, 321, 393, 445, 4445, 257, 777, 9284,
  293, 1190, 257, 10638, 13, 51114], "temperature": 0.0, "avg_logprob": -0.2149033424181816,
  "compression_ratio": 1.703125, "no_speech_prob": 0.016881758347153664}, {"id": 183,
  "seek": 147448, "start": 1489.48, "end": 1502.48, "text": " Right and come so that
  that was like a really good point and it also wasn''t implemented in and benchmark
  so if you add an algorithm so we can like.", "tokens": [51114, 1779, 293, 808, 370,
  300, 300, 390, 411, 257, 534, 665, 935, 293, 309, 611, 2067, 380, 12270, 294, 293,
  18927, 370, 498, 291, 909, 364, 9284, 370, 321, 393, 411, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.2149033424181816, "compression_ratio": 1.703125, "no_speech_prob":
  0.016881758347153664}, {"id": 184, "seek": 150248, "start": 1503.48, "end": 1518.48,
  "text": " Go through all sets of benchmarks yeah yeah yeah so like it was kind of
  easy for you to evaluate where you algorithm stands against other algorithms right
  so like yes right right and so what was the.", "tokens": [50414, 1037, 807, 439,
  6352, 295, 43751, 1338, 1338, 1338, 370, 411, 309, 390, 733, 295, 1858, 337, 291,
  281, 13059, 689, 291, 9284, 7382, 1970, 661, 14642, 558, 370, 411, 2086, 558, 558,
  293, 370, 437, 390, 264, 13, 51164], "temperature": 0.0, "avg_logprob": -0.1774702650127989,
  "compression_ratio": 1.6629213483146068, "no_speech_prob": 0.006451904773712158},
  {"id": 185, "seek": 150248, "start": 1518.48, "end": 1525.48, "text": " And you
  also had a call to write maybe maybe you could introduce him as well like on your
  paper.", "tokens": [51164, 400, 291, 611, 632, 257, 818, 281, 2464, 1310, 1310,
  291, 727, 5366, 796, 382, 731, 411, 322, 428, 3035, 13, 51514], "temperature": 0.0,
  "avg_logprob": -0.1774702650127989, "compression_ratio": 1.6629213483146068, "no_speech_prob":
  0.006451904773712158}, {"id": 186, "seek": 152548, "start": 1525.48, "end": 1530.48,
  "text": " Oh yeah that that is midrida shunyan so.", "tokens": [50364, 876, 1338,
  300, 300, 307, 2062, 81, 2887, 402, 409, 6277, 370, 13, 50614], "temperature": 0.0,
  "avg_logprob": -0.4161293195641559, "compression_ratio": 1.3070175438596492, "no_speech_prob":
  0.04281523451209068}, {"id": 187, "seek": 152548, "start": 1530.48, "end": 1543.48,
  "text": " So that''s that that that was my peer in the like physics lab he also
  got PhD the same year I did so yeah so.", "tokens": [50614, 407, 300, 311, 300,
  300, 300, 390, 452, 15108, 294, 264, 411, 10649, 2715, 415, 611, 658, 14476, 264,
  912, 1064, 286, 630, 370, 1338, 370, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.4161293195641559, "compression_ratio": 1.3070175438596492, "no_speech_prob":
  0.04281523451209068}, {"id": 188, "seek": 154348, "start": 1544.48, "end": 1555.48,
  "text": " Yeah so we decided to team up with that so he helped a lot on he he did
  he did the all evaluation so he integrated it with other code.", "tokens": [50414,
  865, 370, 321, 3047, 281, 1469, 493, 365, 300, 370, 415, 4254, 257, 688, 322, 415,
  415, 630, 415, 630, 264, 439, 13344, 370, 415, 10919, 309, 365, 661, 3089, 13, 50964],
  "temperature": 0.0, "avg_logprob": -0.1683224074694575, "compression_ratio": 1.8125,
  "no_speech_prob": 0.15242688357830048}, {"id": 189, "seek": 154348, "start": 1555.48,
  "end": 1560.48, "text": " And here on the evaluation on the like clusters that we
  had.", "tokens": [50964, 400, 510, 322, 264, 13344, 322, 264, 411, 23313, 300, 321,
  632, 13, 51214], "temperature": 0.0, "avg_logprob": -0.1683224074694575, "compression_ratio":
  1.8125, "no_speech_prob": 0.15242688357830048}, {"id": 190, "seek": 154348, "start":
  1560.48, "end": 1572.48, "text": " Yeah at that point nice so so back to the invention
  like as you''ve been inventing this elbow did you have to make a lot of adjustments
  to the core of the algorithm as you have been evaluating it or was it like.", "tokens":
  [51214, 865, 412, 300, 935, 1481, 370, 370, 646, 281, 264, 22265, 411, 382, 291,
  600, 668, 7962, 278, 341, 18507, 630, 291, 362, 281, 652, 257, 688, 295, 18624,
  281, 264, 4965, 295, 264, 9284, 382, 291, 362, 668, 27479, 309, 420, 390, 309, 411,
  13, 51814], "temperature": 0.0, "avg_logprob": -0.1683224074694575, "compression_ratio":
  1.8125, "no_speech_prob": 0.15242688357830048}, {"id": 191, "seek": 157248, "start":
  1572.48, "end": 1577.48, "text": " You know the first shot and it was it.", "tokens":
  [50364, 509, 458, 264, 700, 3347, 293, 309, 390, 309, 13, 50614], "temperature":
  0.0, "avg_logprob": -0.2782336984361921, "compression_ratio": 1.4705882352941178,
  "no_speech_prob": 0.016889402642846107}, {"id": 192, "seek": 157248, "start": 1577.48,
  "end": 1597.48, "text": " Well not really so there are like two changes compared
  to NSW in the national SW so first one is the idea of layers so that''s all most
  of the problems with like low dimensional data and.", "tokens": [50614, 1042, 406,
  534, 370, 456, 366, 411, 732, 2962, 5347, 281, 15943, 54, 294, 264, 4048, 20346,
  370, 700, 472, 307, 264, 1558, 295, 7914, 370, 300, 311, 439, 881, 295, 264, 2740,
  365, 411, 2295, 18795, 1412, 293, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.2782336984361921, "compression_ratio": 1.4705882352941178, "no_speech_prob":
  0.016889402642846107}, {"id": 193, "seek": 159748, "start": 1597.48, "end": 1620.48,
  "text": " Yeah also improve performance like in most of the tax that like most of
  the distributions even like but maybe not much like high dimensional data but still
  when I ran the whole like suit that was there was a few data set on we should perform
  worse compared to.", "tokens": [50364, 865, 611, 3470, 3389, 411, 294, 881, 295,
  264, 3366, 300, 411, 881, 295, 264, 37870, 754, 411, 457, 1310, 406, 709, 411, 1090,
  18795, 1412, 457, 920, 562, 286, 5872, 264, 1379, 411, 5722, 300, 390, 456, 390,
  257, 1326, 1412, 992, 322, 321, 820, 2042, 5324, 5347, 281, 13, 51514], "temperature":
  0.0, "avg_logprob": -0.24169871590354225, "compression_ratio": 1.6149068322981366,
  "no_speech_prob": 0.02894921787083149}, {"id": 194, "seek": 162048, "start": 1620.48,
  "end": 1636.48, "text": " VP3 so that''s from Leonits you then I thought that wasn''t
  a big deal but like communicated the results with Leonit trying to convince him
  that like we don''t need to have that much algorithms.", "tokens": [50364, 35812,
  18, 370, 300, 311, 490, 13244, 1208, 291, 550, 286, 1194, 300, 2067, 380, 257, 955,
  2028, 457, 411, 34989, 264, 3542, 365, 13244, 270, 1382, 281, 13447, 796, 300, 411,
  321, 500, 380, 643, 281, 362, 300, 709, 14642, 13, 51164], "temperature": 0.0, "avg_logprob":
  -0.277025844739831, "compression_ratio": 1.3642857142857143, "no_speech_prob": 0.09887982904911041},
  {"id": 195, "seek": 163648, "start": 1636.48, "end": 1654.48, "text": " But he was
  not convinced so then we added like an improvement with the heuristic for selecting
  the neighbors which like I personally knew from the work on spatial approximation
  three.", "tokens": [50364, 583, 415, 390, 406, 12561, 370, 550, 321, 3869, 411,
  364, 10444, 365, 264, 415, 374, 3142, 337, 18182, 264, 12512, 597, 411, 286, 5665,
  2586, 490, 264, 589, 322, 23598, 28023, 1045, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.12329130423696417, "compression_ratio": 1.3656716417910448, "no_speech_prob":
  0.07337860763072968}, {"id": 196, "seek": 165448, "start": 1654.48, "end": 1675.48,
  "text": " That made that that made the transition to skip list exact so it made
  an exact so you can build the exact skip list in one day using this heuristic and
  after that so yeah that that that that addition improved the performance yeah.",
  "tokens": [50364, 663, 1027, 300, 300, 1027, 264, 6034, 281, 10023, 1329, 1900,
  370, 309, 1027, 364, 1900, 370, 291, 393, 1322, 264, 1900, 10023, 1329, 294, 472,
  786, 1228, 341, 415, 374, 3142, 293, 934, 300, 370, 1338, 300, 300, 300, 300, 4500,
  9689, 264, 3389, 1338, 13, 51414], "temperature": 0.0, "avg_logprob": -0.3832649530148974,
  "compression_ratio": 1.7164179104477613, "no_speech_prob": 0.10238711535930634},
  {"id": 197, "seek": 167548, "start": 1675.48, "end": 1691.48, "text": " I remember
  please correctly if i''m wrong but like I''ve read your paper actually really really
  closely so I printed it and you know like I was reading with the pencil actually
  making notes so remember like at some point was it so that you agree to them it
  also needs to prove that it will converge.", "tokens": [50364, 286, 1604, 1767,
  8944, 498, 741, 478, 2085, 457, 411, 286, 600, 1401, 428, 3035, 767, 534, 534, 8185,
  370, 286, 13567, 309, 293, 291, 458, 411, 286, 390, 3760, 365, 264, 10985, 767,
  1455, 5570, 370, 1604, 411, 412, 512, 935, 390, 309, 370, 300, 291, 3986, 281, 552,
  309, 611, 2203, 281, 7081, 300, 309, 486, 41881, 13, 51164], "temperature": 0.0,
  "avg_logprob": -0.170175239443779, "compression_ratio": 1.6408839779005524, "no_speech_prob":
  0.3042680323123932}, {"id": 198, "seek": 169148, "start": 1691.48, "end": 1717.48,
  "text": " Or like because you keep resuffling the points in some way right like
  as you build it you use multiple threads like in order to kind of build the actual
  paths between the nodes between layers right so like do you need to kind of still
  somehow make sure that it will converge on all dimensionality so all spaces or was
  it was it not necessary.", "tokens": [50364, 1610, 411, 570, 291, 1066, 725, 1245,
  1688, 264, 2793, 294, 512, 636, 558, 411, 382, 291, 1322, 309, 291, 764, 3866, 19314,
  411, 294, 1668, 281, 733, 295, 1322, 264, 3539, 14518, 1296, 264, 13891, 1296, 7914,
  558, 370, 411, 360, 291, 643, 281, 733, 295, 920, 6063, 652, 988, 300, 309, 486,
  41881, 322, 439, 10139, 1860, 370, 439, 7673, 420, 390, 309, 390, 309, 406, 4818,
  13, 51664], "temperature": 0.0, "avg_logprob": -0.1653478596661542, "compression_ratio":
  1.693069306930693, "no_speech_prob": 0.19410616159439087}, {"id": 199, "seek": 171748,
  "start": 1717.48, "end": 1746.48, "text": " Well so the algorithm is pretty stable
  so the result is like how many threads you can go that is an empirical result so
  I was surprised when I saw it but you know even like for NSW the first algorithm
  even if you start to do like to use I know 40 threads from a single element I can
  found no no no drop in the recall.", "tokens": [50364, 1042, 370, 264, 9284, 307,
  1238, 8351, 370, 264, 1874, 307, 411, 577, 867, 19314, 291, 393, 352, 300, 307,
  364, 31886, 1874, 370, 286, 390, 6100, 562, 286, 1866, 309, 457, 291, 458, 754,
  411, 337, 15943, 54, 264, 700, 9284, 754, 498, 291, 722, 281, 360, 411, 281, 764,
  286, 458, 3356, 19314, 490, 257, 2167, 4478, 286, 393, 1352, 572, 572, 572, 3270,
  294, 264, 9901, 13, 51814], "temperature": 0.0, "avg_logprob": -0.2161735586217932,
  "compression_ratio": 1.601010101010101, "no_speech_prob": 0.08253836631774902},
  {"id": 200, "seek": 174648, "start": 1746.48, "end": 1751.48, "text": " No drop
  in the recall or speed that was a bit surprising.", "tokens": [50364, 883, 3270,
  294, 264, 9901, 420, 3073, 300, 390, 257, 857, 8830, 13, 50614], "temperature":
  0.0, "avg_logprob": -0.16134048330372777, "compression_ratio": 1.5394736842105263,
  "no_speech_prob": 0.002386378822848201}, {"id": 201, "seek": 174648, "start": 1751.48,
  "end": 1755.48, "text": " In terms of stability.", "tokens": [50614, 682, 2115,
  295, 11826, 13, 50814], "temperature": 0.0, "avg_logprob": -0.16134048330372777,
  "compression_ratio": 1.5394736842105263, "no_speech_prob": 0.002386378822848201},
  {"id": 202, "seek": 174648, "start": 1755.48, "end": 1768.48, "text": " So the main
  way to make it stable is just like to avoid avoid exploring so like use use proper
  parameters big enough there are ways to make it stable in.", "tokens": [50814, 407,
  264, 2135, 636, 281, 652, 309, 8351, 307, 445, 411, 281, 5042, 5042, 12736, 370,
  411, 764, 764, 2296, 9834, 955, 1547, 456, 366, 2098, 281, 652, 309, 8351, 294,
  13, 51464], "temperature": 0.0, "avg_logprob": -0.16134048330372777, "compression_ratio":
  1.5394736842105263, "no_speech_prob": 0.002386378822848201}, {"id": 203, "seek":
  176848, "start": 1768.48, "end": 1789.48, "text": " For corruption so when when
  but that that that that is pretty costly so if you bootstrap the graph so if you
  like do iterations like similar to an undecent I think you probably know that I
  can make it stable even if it''s corrupted by a lot.", "tokens": [50364, 1171, 17959,
  370, 562, 562, 457, 300, 300, 300, 300, 307, 1238, 28328, 370, 498, 291, 11450,
  372, 4007, 264, 4295, 370, 498, 291, 411, 360, 36540, 411, 2531, 281, 364, 674,
  3045, 317, 286, 519, 291, 1391, 458, 300, 286, 393, 652, 309, 8351, 754, 498, 309,
  311, 39480, 538, 257, 688, 13, 51414], "temperature": 0.0, "avg_logprob": -0.20094226968699488,
  "compression_ratio": 1.5686274509803921, "no_speech_prob": 0.16928915679454803},
  {"id": 204, "seek": 178948, "start": 1789.48, "end": 1801.48, "text": " So that
  is done only for updates so like when you update your kind of corrupting the graph
  and well in the like a channels WLIP.", "tokens": [50364, 407, 300, 307, 1096, 787,
  337, 9205, 370, 411, 562, 291, 5623, 428, 733, 295, 17366, 278, 264, 4295, 293,
  731, 294, 264, 411, 257, 9235, 343, 43, 9139, 13, 50964], "temperature": 0.0, "avg_logprob":
  -0.24967892198677522, "compression_ratio": 1.6930232558139535, "no_speech_prob":
  0.050628744065761566}, {"id": 205, "seek": 178948, "start": 1801.48, "end": 1817.48,
  "text": " So for updates it wasn''t specifically made to be like very stable but
  for just construction it doesn''t have to be like that''s stable doesn''t have to
  conversion all situation just keep the parameters high enough and it wouldn''t diverge.",
  "tokens": [50964, 407, 337, 9205, 309, 2067, 380, 4682, 1027, 281, 312, 411, 588,
  8351, 457, 337, 445, 6435, 309, 1177, 380, 362, 281, 312, 411, 300, 311, 8351, 1177,
  380, 362, 281, 14298, 439, 2590, 445, 1066, 264, 9834, 1090, 1547, 293, 309, 2759,
  380, 18558, 432, 13, 51764], "temperature": 0.0, "avg_logprob": -0.24967892198677522,
  "compression_ratio": 1.6930232558139535, "no_speech_prob": 0.050628744065761566},
  {"id": 206, "seek": 181748, "start": 1817.48, "end": 1846.48, "text": " Right yeah
  because I remember like and I''m also curious to hear your opinion so then I after
  your paper I started reading other papers for example the Microsoft''s zoom algorithm
  and then later they called it discount and with some modifications so they were
  comparing to etch and SW at larger scale something like billions of nodes billions
  of points in the space right.", "tokens": [50364, 1779, 1338, 570, 286, 1604, 411,
  293, 286, 478, 611, 6369, 281, 1568, 428, 4800, 370, 550, 286, 934, 428, 3035, 286,
  1409, 3760, 661, 10577, 337, 1365, 264, 8116, 311, 8863, 9284, 293, 550, 1780, 436,
  1219, 309, 11635, 293, 365, 512, 26881, 370, 436, 645, 15763, 281, 1030, 339, 293,
  20346, 412, 4833, 4373, 746, 411, 17375, 295, 13891, 17375, 295, 2793, 294, 264,
  1901, 558, 13, 51814], "temperature": 0.0, "avg_logprob": -0.22679744354666095,
  "compression_ratio": 1.608695652173913, "no_speech_prob": 0.003249343251809478},
  {"id": 207, "seek": 184648, "start": 1846.48, "end": 1871.48, "text": " And so they
  they were trying to minimize the cost that that that it will incur because basically
  as you build the H and SW you also use memory quite a bit right so I wanted to hear
  your opinion on that part and then they what they did is that they I don''t know
  if you''re familiar with these papers but what they did is that they offloaded portion
  of the retrieval to to an SSD disk.", "tokens": [50364, 400, 370, 436, 436, 645,
  1382, 281, 17522, 264, 2063, 300, 300, 300, 309, 486, 35774, 570, 1936, 382, 291,
  1322, 264, 389, 293, 20346, 291, 611, 764, 4675, 1596, 257, 857, 558, 370, 286,
  1415, 281, 1568, 428, 4800, 322, 300, 644, 293, 550, 436, 437, 436, 630, 307, 300,
  436, 286, 500, 380, 458, 498, 291, 434, 4963, 365, 613, 10577, 457, 437, 436, 630,
  307, 300, 436, 766, 2907, 292, 8044, 295, 264, 19817, 3337, 281, 281, 364, 30262,
  12355, 13, 51614], "temperature": 0.0, "avg_logprob": -0.15148478204553778, "compression_ratio":
  1.668122270742358, "no_speech_prob": 0.011889033019542694}, {"id": 208, "seek":
  187148, "start": 1871.48, "end": 1884.48, "text": " And so they kind of combined
  your algorithm with like additional layers and then they kind of resolve to full
  precision when they go to SSD disk but they don''t don''t do it in memory.", "tokens":
  [50364, 400, 370, 436, 733, 295, 9354, 428, 9284, 365, 411, 4497, 7914, 293, 550,
  436, 733, 295, 14151, 281, 1577, 18356, 562, 436, 352, 281, 30262, 12355, 457, 436,
  500, 380, 500, 380, 360, 309, 294, 4675, 13, 51014], "temperature": 0.0, "avg_logprob":
  -0.1278900771305479, "compression_ratio": 1.575, "no_speech_prob": 0.08497486263513565},
  {"id": 209, "seek": 187148, "start": 1884.48, "end": 1889.48, "text": " So they
  do use quantization right yeah they use quantization exactly.", "tokens": [51014,
  407, 436, 360, 764, 4426, 2144, 558, 1338, 436, 764, 4426, 2144, 2293, 13, 51264],
  "temperature": 0.0, "avg_logprob": -0.1278900771305479, "compression_ratio": 1.575,
  "no_speech_prob": 0.08497486263513565}, {"id": 210, "seek": 188948, "start": 1890.48,
  "end": 1911.48, "text": " That''s a very popular approach and that makes sense so
  it''s so basically you have a hardware limitation so that you can can store but
  you have a hardware here are here so you have like not so big RAM and like lots
  of SSDs and maybe like if you have distributed system you have access to other nodes.",
  "tokens": [50414, 663, 311, 257, 588, 3743, 3109, 293, 300, 1669, 2020, 370, 309,
  311, 370, 1936, 291, 362, 257, 8837, 27432, 370, 300, 291, 393, 393, 3531, 457,
  291, 362, 257, 8837, 510, 366, 510, 370, 291, 362, 411, 406, 370, 955, 14561, 293,
  411, 3195, 295, 30262, 82, 293, 1310, 411, 498, 291, 362, 12631, 1185, 291, 362,
  2105, 281, 661, 13891, 13, 51464], "temperature": 0.0, "avg_logprob": -0.20697151013274692,
  "compression_ratio": 1.6611111111111112, "no_speech_prob": 0.5008446574211121},
  {"id": 211, "seek": 191148, "start": 1912.48, "end": 1916.48, "text": " So yeah
  that''s a clever use of here are here that makes sense.", "tokens": [50414, 407,
  1338, 300, 311, 257, 13494, 764, 295, 510, 366, 510, 300, 1669, 2020, 13, 50614],
  "temperature": 0.0, "avg_logprob": -0.1383817396968244, "compression_ratio": 1.6388888888888888,
  "no_speech_prob": 0.018013939261436462}, {"id": 212, "seek": 191148, "start": 1916.48,
  "end": 1928.48, "text": " But at the same time like your algorithm was taken into
  using to popular frameworks like files right so like files is not a single algorithm
  like one of them as H and SW and then.", "tokens": [50614, 583, 412, 264, 912, 565,
  411, 428, 9284, 390, 2726, 666, 1228, 281, 3743, 29834, 411, 7098, 558, 370, 411,
  7098, 307, 406, 257, 2167, 9284, 411, 472, 295, 552, 382, 389, 293, 20346, 293,
  550, 13, 51214], "temperature": 0.0, "avg_logprob": -0.1383817396968244, "compression_ratio":
  1.6388888888888888, "no_speech_prob": 0.018013939261436462}, {"id": 213, "seek":
  191148, "start": 1928.48, "end": 1937.48, "text": " Actually don''t know how they
  did it did they take your C++ dependency directly or did they implemented do know.",
  "tokens": [51214, 5135, 500, 380, 458, 577, 436, 630, 309, 630, 436, 747, 428, 383,
  25472, 33621, 3838, 420, 630, 436, 12270, 360, 458, 13, 51664], "temperature": 0.0,
  "avg_logprob": -0.1383817396968244, "compression_ratio": 1.6388888888888888, "no_speech_prob":
  0.018013939261436462}, {"id": 214, "seek": 193748, "start": 1937.48, "end": 1957.48,
  "text": " They very implemented from scratch so like I talked to them once so they
  said they tried different way but like in the end it was like pretty close to the
  like the initial C++ library don''t have some different there is some if something''s
  are implemented differently in fights.", "tokens": [50364, 814, 588, 12270, 490,
  8459, 370, 411, 286, 2825, 281, 552, 1564, 370, 436, 848, 436, 3031, 819, 636, 457,
  411, 294, 264, 917, 309, 390, 411, 1238, 1998, 281, 264, 411, 264, 5883, 383, 25472,
  6405, 500, 380, 362, 512, 819, 456, 307, 512, 498, 746, 311, 366, 12270, 7614, 294,
  14512, 13, 51364], "temperature": 0.0, "avg_logprob": -0.3318731373754041, "compression_ratio":
  1.6104651162790697, "no_speech_prob": 0.020452603697776794}, {"id": 215, "seek":
  195748, "start": 1957.48, "end": 1975.48, "text": " So for instance there is a thread
  pool like in channels WL for keeping track of visited elements so when you have
  a new search if there is like a map like think of a bitmap for which knows which
  notes in the network are visited.", "tokens": [50364, 407, 337, 5197, 456, 307,
  257, 7207, 7005, 411, 294, 9235, 343, 43, 337, 5145, 2837, 295, 11220, 4959, 370,
  562, 291, 362, 257, 777, 3164, 498, 456, 307, 411, 257, 4471, 411, 519, 295, 257,
  857, 24223, 337, 597, 3255, 597, 5570, 294, 264, 3209, 366, 11220, 13, 51264], "temperature":
  0.0, "avg_logprob": -0.2739807884648161, "compression_ratio": 1.52, "no_speech_prob":
  0.032176580280065536}, {"id": 216, "seek": 197548, "start": 1976.48, "end": 1991.48,
  "text": " And the channels WL it''s kept in memory all the time and when you have
  like a new search it will just like peaks from the pool and then face like it creates
  it once per search so there are much searches more more effective.", "tokens": [50414,
  400, 264, 9235, 343, 43, 309, 311, 4305, 294, 4675, 439, 264, 565, 293, 562, 291,
  362, 411, 257, 777, 3164, 309, 486, 445, 411, 26897, 490, 264, 7005, 293, 550, 1851,
  411, 309, 7829, 309, 1564, 680, 3164, 370, 456, 366, 709, 26701, 544, 544, 4942,
  13, 51164], "temperature": 0.0, "avg_logprob": -0.3434600463280311, "compression_ratio":
  1.4966442953020134, "no_speech_prob": 0.0547904446721077}, {"id": 217, "seek": 199148,
  "start": 1992.48, "end": 2017.48, "text": " Yeah yeah yeah by search yeah batch
  search is another feature that sometimes is implemented in vector databases but
  did you like expect that your algorithm would become so widely applicable like do
  you know that it has been re implemented in several languages like for example as
  part of vector database called V ev8 it was implemented in goal.", "tokens": [50414,
  865, 1338, 1338, 538, 3164, 1338, 15245, 3164, 307, 1071, 4111, 300, 2171, 307,
  12270, 294, 8062, 22380, 457, 630, 291, 411, 2066, 300, 428, 9284, 576, 1813, 370,
  13371, 21142, 411, 360, 291, 458, 300, 309, 575, 668, 319, 12270, 294, 2940, 8650,
  411, 337, 1365, 382, 644, 295, 8062, 8149, 1219, 691, 1073, 23, 309, 390, 12270,
  294, 3387, 13, 51664], "temperature": 0.0, "avg_logprob": -0.24775661121715198,
  "compression_ratio": 1.72, "no_speech_prob": 0.04997752234339714}, {"id": 218, "seek":
  201748, "start": 2017.48, "end": 2032.48, "text": " And there is a database called
  quadrant it it''s implemented in rast and of course all of these implementations
  also add like crowd support so they you can actually update right because in reality
  in database you need these features.", "tokens": [50364, 400, 456, 307, 257, 8149,
  1219, 10787, 7541, 309, 309, 311, 12270, 294, 367, 525, 293, 295, 1164, 439, 295,
  613, 4445, 763, 611, 909, 411, 6919, 1406, 370, 436, 291, 393, 767, 5623, 558, 570,
  294, 4103, 294, 8149, 291, 643, 613, 4122, 13, 51114], "temperature": 0.0, "avg_logprob":
  -0.16049987841875124, "compression_ratio": 1.7096774193548387, "no_speech_prob":
  0.008340234868228436}, {"id": 219, "seek": 201748, "start": 2032.48, "end": 2044.48,
  "text": " And then they also added symbolic filtering on top of that so it''s also
  inside your algorithm like did you did you expect such popularity.", "tokens": [51114,
  400, 550, 436, 611, 3869, 25755, 30822, 322, 1192, 295, 300, 370, 309, 311, 611,
  1854, 428, 9284, 411, 630, 291, 630, 291, 2066, 1270, 19301, 13, 51714], "temperature":
  0.0, "avg_logprob": -0.16049987841875124, "compression_ratio": 1.7096774193548387,
  "no_speech_prob": 0.008340234868228436}, {"id": 220, "seek": 204448, "start": 2045.48,
  "end": 2052.48, "text": " No no like I thought that we will publish the algorithm
  and like we will win the benchmarks and we''re clearly seeing.", "tokens": [50414,
  883, 572, 411, 286, 1194, 300, 321, 486, 11374, 264, 9284, 293, 411, 321, 486, 1942,
  264, 43751, 293, 321, 434, 4448, 2577, 13, 50764], "temperature": 0.0, "avg_logprob":
  -0.22544760704040528, "compression_ratio": 1.863849765258216, "no_speech_prob":
  0.028511296957731247}, {"id": 221, "seek": 204448, "start": 2052.48, "end": 2072.48,
  "text": " But though at that time like just before we published the benchmark there
  was a like competitor Falcon which also published the benchmarks of widget better
  but like for Falcon targeted like not like that much and I thought that well Falcon
  was only like for few specific metrics.", "tokens": [50764, 583, 1673, 412, 300,
  565, 411, 445, 949, 321, 6572, 264, 18927, 456, 390, 257, 411, 27266, 31801, 597,
  611, 6572, 264, 43751, 295, 34047, 1101, 457, 411, 337, 31801, 15045, 411, 406,
  411, 300, 709, 293, 286, 1194, 300, 731, 31801, 390, 787, 411, 337, 1326, 2685,
  16367, 13, 51764], "temperature": 0.0, "avg_logprob": -0.22544760704040528, "compression_ratio":
  1.863849765258216, "no_speech_prob": 0.028511296957731247}, {"id": 222, "seek":
  207248, "start": 2072.48, "end": 2096.48, "text": " And yeah actually it also was
  done by like person from the same school which I went so it was in jarrison stain
  so I talked with him a bit and I thought that like we have open source to code so
  we published the paper so like people will quickly just like iterate on top of that
  and like improve.", "tokens": [50364, 400, 1338, 767, 309, 611, 390, 1096, 538,
  411, 954, 490, 264, 912, 1395, 597, 286, 1437, 370, 309, 390, 294, 361, 2284, 2770,
  16441, 370, 286, 2825, 365, 796, 257, 857, 293, 286, 1194, 300, 411, 321, 362, 1269,
  4009, 281, 3089, 370, 321, 6572, 264, 3035, 370, 411, 561, 486, 2661, 445, 411,
  44497, 322, 1192, 295, 300, 293, 411, 3470, 13, 51564], "temperature": 0.0, "avg_logprob":
  -0.30870457256541534, "compression_ratio": 1.560846560846561, "no_speech_prob":
  0.018862580880522728}, {"id": 223, "seek": 209648, "start": 2096.48, "end": 2125.48,
  "text": " But yeah so it took much more time to others to improve upon it compared
  to what I''ve expected and maybe that was due to lack of interest maybe that was
  to some inertia so I don''t know like looking at the how many startups and solutions
  are popping out right now it seems like that like the most of the interest came
  much longer.", "tokens": [50364, 583, 1338, 370, 309, 1890, 709, 544, 565, 281,
  2357, 281, 3470, 3564, 309, 5347, 281, 437, 286, 600, 5176, 293, 1310, 300, 390,
  3462, 281, 5011, 295, 1179, 1310, 300, 390, 281, 512, 37234, 370, 286, 500, 380,
  458, 411, 1237, 412, 264, 577, 867, 28041, 293, 6547, 366, 18374, 484, 558, 586,
  309, 2544, 411, 300, 411, 264, 881, 295, 264, 1179, 1361, 709, 2854, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.1206220653322008, "compression_ratio": 1.604878048780488,
  "no_speech_prob": 0.0800580233335495}, {"id": 224, "seek": 212548, "start": 2125.48,
  "end": 2135.48, "text": " Like much later yeah to like to the point when it was
  released so it was hard to predict it back then.", "tokens": [50364, 1743, 709,
  1780, 1338, 281, 411, 281, 264, 935, 562, 309, 390, 4736, 370, 309, 390, 1152, 281,
  6069, 309, 646, 550, 13, 50864], "temperature": 0.0, "avg_logprob": -0.19256186485290527,
  "compression_ratio": 1.6790697674418604, "no_speech_prob": 0.05155416205525398},
  {"id": 225, "seek": 212548, "start": 2135.48, "end": 2153.48, "text": " Yeah do
  you think that an MS leap has to do something with this success that it kind of
  maybe an MS leap was somewhat visible and then when you edit your algorithm there
  and show that it performs you know those people who followed this library at least
  knew.", "tokens": [50864, 865, 360, 291, 519, 300, 364, 7395, 19438, 575, 281, 360,
  746, 365, 341, 2245, 300, 309, 733, 295, 1310, 364, 7395, 19438, 390, 8344, 8974,
  293, 550, 562, 291, 8129, 428, 9284, 456, 293, 855, 300, 309, 26213, 291, 458, 729,
  561, 567, 6263, 341, 6405, 412, 1935, 2586, 13, 51764], "temperature": 0.0, "avg_logprob":
  -0.19256186485290527, "compression_ratio": 1.6790697674418604, "no_speech_prob":
  0.05155416205525398}, {"id": 226, "seek": 215348, "start": 2153.48, "end": 2156.48,
  "text": " Okay there is a new algorithm.", "tokens": [50364, 1033, 456, 307, 257,
  777, 9284, 13, 50514], "temperature": 0.0, "avg_logprob": -0.29628263517867687,
  "compression_ratio": 1.3488372093023255, "no_speech_prob": 0.01560369785875082},
  {"id": 227, "seek": 215348, "start": 2156.48, "end": 2168.48, "text": " I think
  yeah well that helps so when the MS leap is a good library so it has some audience
  I think the most attention came from and benchmarks.", "tokens": [50514, 286, 519,
  1338, 731, 300, 3665, 370, 562, 264, 7395, 19438, 307, 257, 665, 6405, 370, 309,
  575, 512, 4034, 286, 519, 264, 881, 3202, 1361, 490, 293, 43751, 13, 51114], "temperature":
  0.0, "avg_logprob": -0.29628263517867687, "compression_ratio": 1.3488372093023255,
  "no_speech_prob": 0.01560369785875082}, {"id": 228, "seek": 216848, "start": 2169.48,
  "end": 2180.48, "text": " So because yeah well an eye is like what was I had a lot
  of attention by that point and that benchmark was done by the same person.", "tokens":
  [50414, 407, 570, 1338, 731, 364, 3313, 307, 411, 437, 390, 286, 632, 257, 688,
  295, 3202, 538, 300, 935, 293, 300, 18927, 390, 1096, 538, 264, 912, 954, 13, 50964],
  "temperature": 0.0, "avg_logprob": -0.22842265620376123, "compression_ratio": 1.6264367816091954,
  "no_speech_prob": 0.037044331431388855}, {"id": 229, "seek": 216848, "start": 2180.48,
  "end": 2197.48, "text": " Who did an eye so yeah I think that draw some like traffic
  to the libraries and yeah also I think the idea of algorithm was like understandable
  and so.", "tokens": [50964, 2102, 630, 364, 3313, 370, 1338, 286, 519, 300, 2642,
  512, 411, 6419, 281, 264, 15148, 293, 1338, 611, 286, 519, 264, 1558, 295, 9284,
  390, 411, 25648, 293, 370, 13, 51814], "temperature": 0.0, "avg_logprob": -0.22842265620376123,
  "compression_ratio": 1.6264367816091954, "no_speech_prob": 0.037044331431388855},
  {"id": 230, "seek": 219748, "start": 2198.48, "end": 2207.48, "text": " So that
  also like affects the usage so if you understand something you are more likely to
  use it.", "tokens": [50414, 407, 300, 611, 411, 11807, 264, 14924, 370, 498, 291,
  1223, 746, 291, 366, 544, 3700, 281, 764, 309, 13, 50864], "temperature": 0.0, "avg_logprob":
  -0.2194897292496322, "compression_ratio": 1.5515695067264574, "no_speech_prob":
  0.005177979823201895}, {"id": 231, "seek": 219748, "start": 2207.48, "end": 2226.48,
  "text": " Yeah yeah it''s Eric Bernerson right the Swedish guy as he says the sweet
  who is stuck in New York City yeah I think he implemented a no way originally there
  is also like a presentation by him where he explains not only the annoy algorithm
  but also.", "tokens": [50864, 865, 1338, 309, 311, 9336, 10781, 3953, 558, 264,
  23523, 2146, 382, 415, 1619, 264, 3844, 567, 307, 5541, 294, 1873, 3609, 4392, 1338,
  286, 519, 415, 12270, 257, 572, 636, 7993, 456, 307, 611, 411, 257, 5860, 538, 796,
  689, 415, 13948, 406, 787, 264, 8759, 9284, 457, 611, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.2194897292496322, "compression_ratio": 1.5515695067264574,
  "no_speech_prob": 0.005177979823201895}, {"id": 232, "seek": 222648, "start": 2226.48,
  "end": 2249.48, "text": " So how intuition doesn''t work in multi-dimensional spaces
  anymore like we think that like in three in 3D world where we leave now right like
  the further the point away from you like you can actually see it somehow perceive
  it but like in multi-dimensional space it''s not like that I don''t know what''s
  your view on that by the way.", "tokens": [50364, 407, 577, 24002, 1177, 380, 589,
  294, 4825, 12, 18759, 7673, 3602, 411, 321, 519, 300, 411, 294, 1045, 294, 805,
  35, 1002, 689, 321, 1856, 586, 558, 411, 264, 3052, 264, 935, 1314, 490, 291, 411,
  291, 393, 767, 536, 309, 6063, 20281, 309, 457, 411, 294, 4825, 12, 18759, 1901,
  309, 311, 406, 411, 300, 286, 500, 380, 458, 437, 311, 428, 1910, 322, 300, 538,
  264, 636, 13, 51514], "temperature": 0.0, "avg_logprob": -0.13716737111409505, "compression_ratio":
  1.6417910447761195, "no_speech_prob": 0.010929143987596035}, {"id": 233, "seek":
  224948, "start": 2249.48, "end": 2255.48, "text": " So like does geometry perception
  changes in high dimensional space.", "tokens": [50364, 407, 411, 775, 18426, 12860,
  2962, 294, 1090, 18795, 1901, 13, 50664], "temperature": 0.0, "avg_logprob": -0.19851755717444042,
  "compression_ratio": 1.6576086956521738, "no_speech_prob": 0.011454934254288673},
  {"id": 234, "seek": 224948, "start": 2255.48, "end": 2276.48, "text": " Well yes
  yes so there are like many interpretations of this so people who work with nearest
  neighbor search they know about it so like if you have like if you have like many
  dimensions even small perturbations there they can go like far.", "tokens": [50664,
  1042, 2086, 2086, 370, 456, 366, 411, 867, 37547, 295, 341, 370, 561, 567, 589,
  365, 23831, 5987, 3164, 436, 458, 466, 309, 370, 411, 498, 291, 362, 411, 498, 291,
  362, 411, 867, 12819, 754, 1359, 40468, 763, 456, 436, 393, 352, 411, 1400, 13,
  51714], "temperature": 0.0, "avg_logprob": -0.19851755717444042, "compression_ratio":
  1.6576086956521738, "no_speech_prob": 0.011454934254288673}, {"id": 235, "seek":
  227648, "start": 2276.48, "end": 2297.48, "text": " So you all have like so to find
  nearest neighbor you need to have like a huge cover sphere yeah like when you divide
  divide the space so yeah that makes the problem complicated and that that one of
  the reasons why all the practical methods are approximate.", "tokens": [50364, 407,
  291, 439, 362, 411, 370, 281, 915, 23831, 5987, 291, 643, 281, 362, 411, 257, 2603,
  2060, 16687, 1338, 411, 562, 291, 9845, 9845, 264, 1901, 370, 1338, 300, 1669, 264,
  1154, 6179, 293, 300, 300, 472, 295, 264, 4112, 983, 439, 264, 8496, 7150, 366,
  30874, 13, 51414], "temperature": 0.0, "avg_logprob": -0.17376018020341982, "compression_ratio":
  1.610062893081761, "no_speech_prob": 0.028064627200365067}, {"id": 236, "seek":
  229748, "start": 2298.48, "end": 2320.48, "text": " Right yeah yeah yeah so like
  you do need some approximation in order to find the points and so yeah I mean it
  sounds like so when you when you mentioned and then benchmarks was it you who submitted
  the algorithm for the benchmarks or was it Eric who picked it up and he made it
  kind of available in the end and benchmarks.", "tokens": [50414, 1779, 1338, 1338,
  1338, 370, 411, 291, 360, 643, 512, 28023, 294, 1668, 281, 915, 264, 2793, 293,
  370, 1338, 286, 914, 309, 3263, 411, 370, 562, 291, 562, 291, 2835, 293, 550, 43751,
  390, 309, 291, 567, 14405, 264, 9284, 337, 264, 43751, 420, 390, 309, 9336, 567,
  6183, 309, 493, 293, 415, 1027, 309, 733, 295, 2435, 294, 264, 917, 293, 43751,
  13, 51514], "temperature": 0.0, "avg_logprob": -0.143162008644878, "compression_ratio":
  1.7219251336898396, "no_speech_prob": 0.13415798544883728}, {"id": 237, "seek":
  232048, "start": 2320.48, "end": 2323.48, "text": " No no I did a full request to
  edit.", "tokens": [50364, 883, 572, 286, 630, 257, 1577, 5308, 281, 8129, 13, 50514],
  "temperature": 0.0, "avg_logprob": -0.31843823725634285, "compression_ratio": 1.7826086956521738,
  "no_speech_prob": 0.2328237146139145}, {"id": 238, "seek": 232048, "start": 2323.48,
  "end": 2333.48, "text": " All right so it basically yeah yeah so you pushed it forward
  yourself right so it wasn''t like you just implemented and then you waited for it
  to be discovered so to say.", "tokens": [50514, 1057, 558, 370, 309, 1936, 1338,
  1338, 370, 291, 9152, 309, 2128, 1803, 558, 370, 309, 2067, 380, 411, 291, 445,
  12270, 293, 550, 291, 15240, 337, 309, 281, 312, 6941, 370, 281, 584, 13, 51014],
  "temperature": 0.0, "avg_logprob": -0.31843823725634285, "compression_ratio": 1.7826086956521738,
  "no_speech_prob": 0.2328237146139145}, {"id": 239, "seek": 232048, "start": 2333.48,
  "end": 2349.48, "text": " No yeah definitely so like the one of the like decisions
  to use in the most sleep was that the most sleep was already integrated in an benchmark
  so adding that will be just like adding some code in an benchmark that like pulls
  the algorithm and.", "tokens": [51014, 883, 1338, 2138, 370, 411, 264, 472, 295,
  264, 411, 5327, 281, 764, 294, 264, 881, 2817, 390, 300, 264, 881, 2817, 390, 1217,
  10919, 294, 364, 18927, 370, 5127, 300, 486, 312, 445, 411, 5127, 512, 3089, 294,
  364, 18927, 300, 411, 16982, 264, 9284, 293, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.31843823725634285, "compression_ratio": 1.7826086956521738, "no_speech_prob":
  0.2328237146139145}, {"id": 240, "seek": 234948, "start": 2349.48, "end": 2369.48,
  "text": " And then the tuning of the parameters so that was but that was simple
  to do right yeah and so as you did that like what were the results like of that
  of course an end benchmarks it has a number of parameters right for example like
  even indexing speed.", "tokens": [50364, 400, 550, 264, 15164, 295, 264, 9834, 370,
  300, 390, 457, 300, 390, 2199, 281, 360, 558, 1338, 293, 370, 382, 291, 630, 300,
  411, 437, 645, 264, 3542, 411, 295, 300, 295, 1164, 364, 917, 43751, 309, 575, 257,
  1230, 295, 9834, 558, 337, 1365, 411, 754, 8186, 278, 3073, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.3187592029571533, "compression_ratio": 1.5987261146496816,
  "no_speech_prob": 0.0018335786880925298}, {"id": 241, "seek": 236948, "start": 2369.48,
  "end": 2383.48, "text": " Not only like recall versus QPS trade trade off like was
  there some specific kind of metrics that were hnsw excelled over other algorithms.",
  "tokens": [50364, 1726, 787, 411, 9901, 5717, 1249, 6273, 4923, 4923, 766, 411,
  390, 456, 512, 2685, 733, 295, 16367, 300, 645, 276, 3695, 86, 45817, 292, 670,
  661, 14642, 13, 51064], "temperature": 0.0, "avg_logprob": -0.27355136293353455,
  "compression_ratio": 1.2636363636363637, "no_speech_prob": 0.21543322503566742},
  {"id": 242, "seek": 238348, "start": 2384.48, "end": 2404.48, "text": " Well at
  that point of time there was like no logging of the construction time and memory
  consumption and the like the initial version in the most sleep it had like clear
  focus on the performance like recall to speed ratio.", "tokens": [50414, 1042, 412,
  300, 935, 295, 565, 456, 390, 411, 572, 27991, 295, 264, 6435, 565, 293, 4675, 12126,
  293, 264, 411, 264, 5883, 3037, 294, 264, 881, 2817, 309, 632, 411, 1850, 1879,
  322, 264, 3389, 411, 9901, 281, 3073, 8509, 13, 51414], "temperature": 0.0, "avg_logprob":
  -0.21947410832280698, "compression_ratio": 1.5524475524475525, "no_speech_prob":
  0.0713333711028099}, {"id": 243, "seek": 240448, "start": 2405.48, "end": 2421.48,
  "text": " Yeah and well you know it''s hard to do proper benchmarking so like there
  are a number of scenarios somewhere you have a limit on memory somewhere you have
  a limit on the construction time sometimes like you don''t care about them at all
  you just care about the speed.", "tokens": [50414, 865, 293, 731, 291, 458, 309,
  311, 1152, 281, 360, 2296, 18927, 278, 370, 411, 456, 366, 257, 1230, 295, 15077,
  4079, 291, 362, 257, 4948, 322, 4675, 4079, 291, 362, 257, 4948, 322, 264, 6435,
  565, 2171, 411, 291, 500, 380, 1127, 466, 552, 412, 439, 291, 445, 1127, 466, 264,
  3073, 13, 51214], "temperature": 0.0, "avg_logprob": -0.11550265345080145, "compression_ratio":
  1.705128205128205, "no_speech_prob": 0.04405513033270836}, {"id": 244, "seek": 242148,
  "start": 2421.48, "end": 2442.48, "text": " You can also care about like multi thread
  performance or you can care about like single thread performance like maybe different
  scenarios so it''s pretty hard to go proper benchmarking and the depth like like
  I did a decision to just focus on the recall and don''t think about construction
  and memory.", "tokens": [50364, 509, 393, 611, 1127, 466, 411, 4825, 7207, 3389,
  420, 291, 393, 1127, 466, 411, 2167, 7207, 3389, 411, 1310, 819, 15077, 370, 309,
  311, 1238, 1152, 281, 352, 2296, 18927, 278, 293, 264, 7161, 411, 411, 286, 630,
  257, 3537, 281, 445, 1879, 322, 264, 9901, 293, 500, 380, 519, 466, 6435, 293, 4675,
  13, 51414], "temperature": 0.0, "avg_logprob": -0.2436261018117269, "compression_ratio":
  1.670391061452514, "no_speech_prob": 0.05505936220288277}, {"id": 245, "seek": 244248,
  "start": 2442.48, "end": 2454.48, "text": " Okay I see yeah and so and and basically
  when you when you did that like was hnsw like at the top of the competition at that
  point.", "tokens": [50364, 1033, 286, 536, 1338, 293, 370, 293, 293, 1936, 562,
  291, 562, 291, 630, 300, 411, 390, 276, 3695, 86, 411, 412, 264, 1192, 295, 264,
  6211, 412, 300, 935, 13, 50964], "temperature": 0.0, "avg_logprob": -0.23508886011635385,
  "compression_ratio": 1.7614213197969544, "no_speech_prob": 0.055322013795375824},
  {"id": 246, "seek": 244248, "start": 2454.48, "end": 2471.48, "text": " Yes yes
  it was like a top and on many many benchmarks it was like it was a huge cap compared
  to the next competitor so not so maybe for a globe I think this Falcon there was
  still there there was a like significant.", "tokens": [50964, 1079, 2086, 309, 390,
  411, 257, 1192, 293, 322, 867, 867, 43751, 309, 390, 411, 309, 390, 257, 2603, 1410,
  5347, 281, 264, 958, 27266, 370, 406, 370, 1310, 337, 257, 15371, 286, 519, 341,
  31801, 456, 390, 920, 456, 456, 390, 257, 411, 4776, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.23508886011635385, "compression_ratio": 1.7614213197969544,
  "no_speech_prob": 0.055322013795375824}, {"id": 247, "seek": 247248, "start": 2473.48,
  "end": 2477.48, "text": " Difference yeah but many.", "tokens": [50414, 35940, 5158,
  1338, 457, 867, 13, 50614], "temperature": 0.0, "avg_logprob": -0.28007225556807086,
  "compression_ratio": 1.4076923076923078, "no_speech_prob": 0.010700671002268791},
  {"id": 248, "seek": 247248, "start": 2479.48, "end": 2492.48, "text": " Yeah also
  like at some point after that there was a real release of key graph algorithm so
  which like decreased the difference but it was still on top of it.", "tokens": [50714,
  865, 611, 411, 412, 512, 935, 934, 300, 456, 390, 257, 957, 4374, 295, 2141, 4295,
  9284, 370, 597, 411, 24436, 264, 2649, 457, 309, 390, 920, 322, 1192, 295, 309,
  13, 51364], "temperature": 0.0, "avg_logprob": -0.28007225556807086, "compression_ratio":
  1.4076923076923078, "no_speech_prob": 0.010700671002268791}, {"id": 249, "seek":
  249248, "start": 2492.48, "end": 2502.48, "text": " Yeah so did you did you did
  it make you feel proud at that moment when you saw the big gap and like this is
  your invention for how did you feel about it.", "tokens": [50364, 865, 370, 630,
  291, 630, 291, 630, 309, 652, 291, 841, 4570, 412, 300, 1623, 562, 291, 1866, 264,
  955, 7417, 293, 411, 341, 307, 428, 22265, 337, 577, 630, 291, 841, 466, 309, 13,
  50864], "temperature": 0.0, "avg_logprob": -0.1310565899579953, "compression_ratio":
  1.6701030927835052, "no_speech_prob": 0.07944231480360031}, {"id": 250, "seek":
  249248, "start": 2502.48, "end": 2519.48, "text": " Well that felt nice for sure
  so yeah so we published the paper I think like pop when the paper was finally accepted
  so it''s also felt like really well so I think it took.", "tokens": [50864, 1042,
  300, 2762, 1481, 337, 988, 370, 1338, 370, 321, 6572, 264, 3035, 286, 519, 411,
  1665, 562, 264, 3035, 390, 2721, 9035, 370, 309, 311, 611, 2762, 411, 534, 731,
  370, 286, 519, 309, 1890, 13, 51714], "temperature": 0.0, "avg_logprob": -0.1310565899579953,
  "compression_ratio": 1.6701030927835052, "no_speech_prob": 0.07944231480360031},
  {"id": 251, "seek": 251948, "start": 2519.48, "end": 2524.48, "text": " Like two
  and a half years to publish the paper well.", "tokens": [50364, 1743, 732, 293,
  257, 1922, 924, 281, 11374, 264, 3035, 731, 13, 50614], "temperature": 0.0, "avg_logprob":
  -0.2913198149606083, "compression_ratio": 1.665289256198347, "no_speech_prob": 0.02951093018054962},
  {"id": 252, "seek": 251948, "start": 2524.48, "end": 2535.48, "text": " As they
  say in the US I think every rejection brings you closer to the goal so it sounds
  like you''ve been rejected in multiple like journals that was not that was still
  published.", "tokens": [50614, 1018, 436, 584, 294, 264, 2546, 286, 519, 633, 26044,
  5607, 291, 4966, 281, 264, 3387, 370, 309, 3263, 411, 291, 600, 668, 15749, 294,
  3866, 411, 29621, 300, 390, 406, 300, 390, 920, 6572, 13, 51164], "temperature":
  0.0, "avg_logprob": -0.2913198149606083, "compression_ratio": 1.665289256198347,
  "no_speech_prob": 0.02951093018054962}, {"id": 253, "seek": 251948, "start": 2535.48,
  "end": 2547.48, "text": " Now that was a single journal it''s just like yeah one
  revision took one year so that is that is palm year so transaction of pattern analyzing
  a machine intelligence okay.", "tokens": [51164, 823, 300, 390, 257, 2167, 6708,
  309, 311, 445, 411, 1338, 472, 34218, 1890, 472, 1064, 370, 300, 307, 300, 307,
  17018, 1064, 370, 14425, 295, 5102, 23663, 257, 3479, 7599, 1392, 13, 51764], "temperature":
  0.0, "avg_logprob": -0.2913198149606083, "compression_ratio": 1.665289256198347,
  "no_speech_prob": 0.02951093018054962}, {"id": 254, "seek": 254748, "start": 2548.48,
  "end": 2560.48, "text": " So like we follow the practice and physics and ignore
  ignore the conferences so and we also need the for the grants we need to have journal
  publications not not confidence publication so we sent.", "tokens": [50414, 407,
  411, 321, 1524, 264, 3124, 293, 10649, 293, 11200, 11200, 264, 22032, 370, 293,
  321, 611, 643, 264, 337, 264, 16101, 321, 643, 281, 362, 6708, 25618, 406, 406,
  6687, 19953, 370, 321, 2279, 13, 51014], "temperature": 0.0, "avg_logprob": -0.2794168735372609,
  "compression_ratio": 1.607361963190184, "no_speech_prob": 0.0058587719686329365},
  {"id": 255, "seek": 254748, "start": 2561.48, "end": 2566.48, "text": " To Pamy
  and had few revisions there but each revision took a year.", "tokens": [51064, 1407,
  430, 7804, 293, 632, 1326, 3698, 4252, 456, 457, 1184, 34218, 1890, 257, 1064, 13,
  51314], "temperature": 0.0, "avg_logprob": -0.2794168735372609, "compression_ratio":
  1.607361963190184, "no_speech_prob": 0.0058587719686329365}, {"id": 256, "seek":
  256648, "start": 2566.48, "end": 2576.48, "text": " Wow this is super long why do
  you think it was like that like why why would reviewers be so scrutinizing like
  your submission.", "tokens": [50364, 3153, 341, 307, 1687, 938, 983, 360, 291, 519,
  309, 390, 411, 300, 411, 983, 983, 576, 45837, 312, 370, 28949, 259, 3319, 411,
  428, 23689, 13, 50864], "temperature": 0.0, "avg_logprob": -0.16562448848377576,
  "compression_ratio": 1.483695652173913, "no_speech_prob": 0.19627168774604797},
  {"id": 257, "seek": 256648, "start": 2577.48, "end": 2593.48, "text": " Well I don''t
  know so like I actually talked with the editor so I was very angry after the first
  result so and it seems like just a problem is how.", "tokens": [50914, 1042, 286,
  500, 380, 458, 370, 411, 286, 767, 2825, 365, 264, 9839, 370, 286, 390, 588, 6884,
  934, 264, 700, 1874, 370, 293, 309, 2544, 411, 445, 257, 1154, 307, 577, 13, 51714],
  "temperature": 0.0, "avg_logprob": -0.16562448848377576, "compression_ratio": 1.483695652173913,
  "no_speech_prob": 0.19627168774604797}, {"id": 258, "seek": 259348, "start": 2593.48,
  "end": 2603.48, "text": " So publications in computer science are organized so that''s
  that''s not only that journal there are so many journals which have.", "tokens":
  [50364, 407, 25618, 294, 3820, 3497, 366, 9983, 370, 300, 311, 300, 311, 406, 787,
  300, 6708, 456, 366, 370, 867, 29621, 597, 362, 13, 50864], "temperature": 0.0,
  "avg_logprob": -0.3304427146911621, "compression_ratio": 1.6089385474860336, "no_speech_prob":
  0.08353373408317566}, {"id": 259, "seek": 259348, "start": 2603.48, "end": 2618.48,
  "text": " This problem and like when I looked at the Twitter like when some discussions
  were like oh I got like review invitation for like this like the national journal.",
  "tokens": [50864, 639, 1154, 293, 411, 562, 286, 2956, 412, 264, 5794, 411, 562,
  512, 11088, 645, 411, 1954, 286, 658, 411, 3131, 17890, 337, 411, 341, 411, 264,
  4048, 6708, 13, 51614], "temperature": 0.0, "avg_logprob": -0.3304427146911621,
  "compression_ratio": 1.6089385474860336, "no_speech_prob": 0.08353373408317566},
  {"id": 260, "seek": 261848, "start": 2618.48, "end": 2646.48, "text": " They said
  I have to write review in 10 days oh I never gonna do that so no like no way I''m
  writing a review in 10 days and yeah so in physics it took it sometimes took a few
  weeks to get the review and journal in journal so you send it and thank you for
  the months you can already start like writing to review like what what what takes
  so long yeah and yeah in computer science.", "tokens": [50364, 814, 848, 286, 362,
  281, 2464, 3131, 294, 1266, 1708, 1954, 286, 1128, 799, 360, 300, 370, 572, 411,
  572, 636, 286, 478, 3579, 257, 3131, 294, 1266, 1708, 293, 1338, 370, 294, 10649,
  309, 1890, 309, 2171, 1890, 257, 1326, 3259, 281, 483, 264, 3131, 293, 6708, 294,
  6708, 370, 291, 2845, 309, 293, 1309, 291, 337, 264, 2493, 291, 393, 1217, 722,
  411, 3579, 281, 3131, 411, 437, 437, 437, 2516, 370, 938, 1338, 293, 1338, 294,
  3820, 3497, 13, 51764], "temperature": 0.0, "avg_logprob": -0.21093954041946766,
  "compression_ratio": 1.75, "no_speech_prob": 0.12649580836296082}, {"id": 261, "seek":
  264648, "start": 2646.48, "end": 2664.48, "text": " But journals are very slow conferences
  are also slow there''s several months to get the review and like people saw that
  we are using archive yeah so if there were no archive I think they have already
  they will just.", "tokens": [50364, 583, 29621, 366, 588, 2964, 22032, 366, 611,
  2964, 456, 311, 2940, 2493, 281, 483, 264, 3131, 293, 411, 561, 1866, 300, 321,
  366, 1228, 23507, 1338, 370, 498, 456, 645, 572, 23507, 286, 519, 436, 362, 1217,
  436, 486, 445, 13, 51264], "temperature": 0.0, "avg_logprob": -0.3064603805541992,
  "compression_ratio": 1.4758620689655173, "no_speech_prob": 0.1618216633796692},
  {"id": 262, "seek": 266448, "start": 2664.48, "end": 2688.48, "text": " They will
  create new journals yeah exactly like they should be any monopolies right in that
  sense like maybe go and create your own journal but then the question is when the
  problem is when you a PhD student let''s say you have a chicken act problem right
  so you haven''t proven yourself yet you need a publication to defend your thesis
  right so that''s the trap.", "tokens": [50364, 814, 486, 1884, 777, 29621, 1338,
  2293, 411, 436, 820, 312, 604, 47721, 530, 558, 294, 300, 2020, 411, 1310, 352,
  293, 1884, 428, 1065, 6708, 457, 550, 264, 1168, 307, 562, 264, 1154, 307, 562,
  291, 257, 14476, 3107, 718, 311, 584, 291, 362, 257, 4662, 605, 1154, 558, 370,
  291, 2378, 380, 12785, 1803, 1939, 291, 643, 257, 19953, 281, 8602, 428, 22288,
  558, 370, 300, 311, 264, 11487, 13, 51564], "temperature": 0.0, "avg_logprob": -0.1908327529304906,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.2940293252468109},
  {"id": 263, "seek": 268848, "start": 2688.48, "end": 2717.48, "text": " Well it''s
  also known how how can this all so if like they created like a new conference conferences
  like I think I didn''t remember I see a lot or I see a lot was created not that
  long ago they could have created the journal as well yeah the same people said like
  we don''t want to do conferences like conferences you have a very tight deadline
  that means like if you miss it you''ll wait for another year and that is like not
  not.", "tokens": [50414, 1042, 309, 311, 611, 2570, 577, 577, 393, 341, 439, 370,
  498, 411, 436, 2942, 411, 257, 777, 7586, 22032, 411, 286, 519, 286, 994, 380, 1604,
  286, 536, 257, 688, 420, 286, 536, 257, 688, 390, 2942, 406, 300, 938, 2057, 436,
  727, 362, 2942, 264, 6708, 382, 731, 1338, 264, 912, 561, 848, 411, 321, 500, 380,
  528, 281, 360, 22032, 411, 22032, 291, 362, 257, 588, 4524, 20615, 300, 1355, 411,
  498, 291, 1713, 309, 291, 603, 1699, 337, 1071, 1064, 293, 300, 307, 411, 406, 406,
  13, 51814], "temperature": 0.0, "avg_logprob": -0.20963461855624585, "compression_ratio":
  1.8771929824561404, "no_speech_prob": 0.26836782693862915}, {"id": 264, "seek":
  271848, "start": 2718.48, "end": 2735.48, "text": " Great let''s create a journal
  and now you have a continuous like a spectrum of time when you want to send your
  paper no deadlines there are no deadlines for reviewers yeah you could almost review
  yourself.", "tokens": [50364, 3769, 718, 311, 1884, 257, 6708, 293, 586, 291, 362,
  257, 10957, 411, 257, 11143, 295, 565, 562, 291, 528, 281, 2845, 428, 3035, 572,
  37548, 456, 366, 572, 37548, 337, 45837, 1338, 291, 727, 1920, 3131, 1803, 13, 51214],
  "temperature": 0.0, "avg_logprob": -0.23158929514330487, "compression_ratio": 1.4782608695652173,
  "no_speech_prob": 0.0892980620265007}, {"id": 265, "seek": 273548, "start": 2735.48,
  "end": 2755.48, "text": " Yeah I mean like during the review period on the conference
  you can get like 10 papers at the same time so you have to review them like in a
  batch but if you are working with journals you get a review like from time to time
  yeah like your your load is distributed.", "tokens": [50364, 865, 286, 914, 411,
  1830, 264, 3131, 2896, 322, 264, 7586, 291, 393, 483, 411, 1266, 10577, 412, 264,
  912, 565, 370, 291, 362, 281, 3131, 552, 411, 294, 257, 15245, 457, 498, 291, 366,
  1364, 365, 29621, 291, 483, 257, 3131, 411, 490, 565, 281, 565, 1338, 411, 428,
  428, 3677, 307, 12631, 13, 51364], "temperature": 0.0, "avg_logprob": -0.1861377813048282,
  "compression_ratio": 1.6, "no_speech_prob": 0.33215025067329407}, {"id": 266, "seek":
  275548, "start": 2755.48, "end": 2781.48, "text": " Yeah so by the way what is your
  take like I think new IPS conference they decided this year they decided to hold
  all reviews publicly so essentially anybody can see you know the comments from reviewers
  and there is like a discussion between reviewers and authors and everything is public
  do you think it improves the process somehow or not what''s your take on this.",
  "tokens": [50364, 865, 370, 538, 264, 636, 437, 307, 428, 747, 411, 286, 519, 777,
  50021, 7586, 436, 3047, 341, 1064, 436, 3047, 281, 1797, 439, 10229, 14843, 370,
  4476, 4472, 393, 536, 291, 458, 264, 3053, 490, 45837, 293, 456, 307, 411, 257,
  5017, 1296, 45837, 293, 16552, 293, 1203, 307, 1908, 360, 291, 519, 309, 24771,
  264, 1399, 6063, 420, 406, 437, 311, 428, 747, 322, 341, 13, 51664], "temperature":
  0.0, "avg_logprob": -0.1015020145310296, "compression_ratio": 1.6898148148148149,
  "no_speech_prob": 0.09201295673847198}, {"id": 267, "seek": 278148, "start": 2781.48,
  "end": 2810.48, "text": " Well I think that makes sense so that opens well that
  sets the bar for reviewers higher because if you know that your review will be read
  by some random people you want to make it better and spend more time on reading
  the paper it also helps to understand the review process from outside like for if
  you''re a new reviewer you want to understand how to do proper review you can just
  read reviews by other people.", "tokens": [50414, 1042, 286, 519, 300, 1669, 2020,
  370, 300, 9870, 731, 300, 6352, 264, 2159, 337, 45837, 2946, 570, 498, 291, 458,
  300, 428, 3131, 486, 312, 1401, 538, 512, 4974, 561, 291, 528, 281, 652, 309, 1101,
  293, 3496, 544, 565, 322, 3760, 264, 3035, 309, 611, 3665, 281, 1223, 264, 3131,
  1399, 490, 2380, 411, 337, 498, 291, 434, 257, 777, 3131, 260, 291, 528, 281, 1223,
  577, 281, 360, 2296, 3131, 291, 393, 445, 1401, 10229, 538, 661, 561, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.11340210858513328, "compression_ratio": 1.7869565217391303,
  "no_speech_prob": 0.061579495668411255}, {"id": 268, "seek": 281148, "start": 2811.48,
  "end": 2835.48, "text": " And that is helpful and you can also like if you''re if
  you want to publish a paper you can find similar papers and read the reviews for
  those papers and understand like why they are rejected or accepted so that that
  helps I don''t see like much problem in that that fights against against the corruption
  and some places in science are corrupted so.", "tokens": [50364, 400, 300, 307,
  4961, 293, 291, 393, 611, 411, 498, 291, 434, 498, 291, 528, 281, 11374, 257, 3035,
  291, 393, 915, 2531, 10577, 293, 1401, 264, 10229, 337, 729, 10577, 293, 1223, 411,
  983, 436, 366, 15749, 420, 9035, 370, 300, 300, 3665, 286, 500, 380, 536, 411, 709,
  1154, 294, 300, 300, 14512, 1970, 1970, 264, 17959, 293, 512, 3190, 294, 3497, 366,
  39480, 370, 13, 51564], "temperature": 0.0, "avg_logprob": -0.20947571595509848,
  "compression_ratio": 1.7263681592039801, "no_speech_prob": 0.04055245220661163},
  {"id": 269, "seek": 283548, "start": 2835.48, "end": 2864.48, "text": " Yeah it
  kind of brings transparency at least with the process and also as you mentioned
  someone can learn how to do these things right so I think it''s also useful and
  maybe it prevents situations when the paper is rejected outright because the reviewer
  has some bias against this topic or you know I mean at least transparency is good
  I think yeah.", "tokens": [50414, 865, 309, 733, 295, 5607, 17131, 412, 1935, 365,
  264, 1399, 293, 611, 382, 291, 2835, 1580, 393, 1466, 577, 281, 360, 613, 721, 558,
  370, 286, 519, 309, 311, 611, 4420, 293, 1310, 309, 22367, 6851, 562, 264, 3035,
  307, 15749, 35189, 570, 264, 3131, 260, 575, 512, 12577, 1970, 341, 4829, 420, 291,
  458, 286, 914, 412, 1935, 17131, 307, 665, 286, 519, 1338, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.08758626665387835, "compression_ratio": 1.6186046511627907,
  "no_speech_prob": 0.1423475593328476}, {"id": 270, "seek": 286548, "start": 2866.48,
  "end": 2872.48, "text": " Are you publishing today by the way do you have any publishable
  work do you intend to publish.", "tokens": [50414, 2014, 291, 17832, 965, 538, 264,
  636, 360, 291, 362, 604, 11374, 712, 589, 360, 291, 19759, 281, 11374, 13, 50714],
  "temperature": 0.0, "avg_logprob": -0.2400408699398949, "compression_ratio": 1.6235294117647059,
  "no_speech_prob": 0.032644256949424744}, {"id": 271, "seek": 286548, "start": 2874.48,
  "end": 2888.48, "text": " Not much so I''m working mostly on protection like maybe
  next year I work on something publishable we are last last thing I published that
  wasn''t some song so for on both estimation.", "tokens": [50814, 1726, 709, 370,
  286, 478, 1364, 5240, 322, 6334, 411, 1310, 958, 1064, 286, 589, 322, 746, 11374,
  712, 321, 366, 1036, 1036, 551, 286, 6572, 300, 2067, 380, 512, 2153, 370, 337,
  322, 1293, 35701, 13, 51514], "temperature": 0.0, "avg_logprob": -0.2400408699398949,
  "compression_ratio": 1.6235294117647059, "no_speech_prob": 0.032644256949424744},
  {"id": 272, "seek": 288848, "start": 2889.48, "end": 2914.48, "text": " Yeah but
  like I''ve noticed like you are very active on hnsw github like when I when I posted
  my question and maybe we can discuss that as well if you are kind of curious on
  that kind of you responded really fast and so it means that you still continue to
  allocate chunk of your time to to look at you know issues and pull requests on on
  github.", "tokens": [50414, 865, 457, 411, 286, 600, 5694, 411, 291, 366, 588, 4967,
  322, 276, 3695, 86, 290, 355, 836, 411, 562, 286, 562, 286, 9437, 452, 1168, 293,
  1310, 321, 393, 2248, 300, 382, 731, 498, 291, 366, 733, 295, 6369, 322, 300, 733,
  295, 291, 15806, 534, 2370, 293, 370, 309, 1355, 300, 291, 920, 2354, 281, 35713,
  16635, 295, 428, 565, 281, 281, 574, 412, 291, 458, 2663, 293, 2235, 12475, 322,
  322, 290, 355, 836, 13, 51664], "temperature": 0.0, "avg_logprob": -0.12601515141929068,
  "compression_ratio": 1.6618357487922706, "no_speech_prob": 0.06960642337799072},
  {"id": 273, "seek": 291448, "start": 2914.48, "end": 2943.48, "text": " Yeah so
  like I wish I would have done it better so I miss some some things from there but
  yeah I tried to update this library so I think that well when I designed hnsw so
  there was some design decisions and even if I see like some algorithms outside improve
  upon that I think they are not.", "tokens": [50414, 865, 370, 411, 286, 3172, 286,
  576, 362, 1096, 309, 1101, 370, 286, 1713, 512, 512, 721, 490, 456, 457, 1338, 286,
  3031, 281, 5623, 341, 6405, 370, 286, 519, 300, 731, 562, 286, 4761, 276, 3695,
  86, 370, 456, 390, 512, 1715, 5327, 293, 754, 498, 286, 536, 411, 512, 14642, 2380,
  3470, 3564, 300, 286, 519, 436, 366, 406, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.2035375741811899, "compression_ratio": 1.6235955056179776, "no_speech_prob":
  0.03246492147445679}, {"id": 274, "seek": 294448, "start": 2944.48, "end": 2946.48,
  "text": " Aligned with the design.", "tokens": [50364, 967, 16690, 365, 264, 1715,
  13, 50464], "temperature": 0.0, "avg_logprob": -0.21321464909447563, "compression_ratio":
  1.5251396648044693, "no_speech_prob": 0.0077543724328279495}, {"id": 275, "seek":
  294448, "start": 2946.48, "end": 2956.48, "text": " So and I skip them one of that
  is like hnsw tries to avoid global view of the network so because it''s it''s a
  descendant of.", "tokens": [50464, 407, 293, 286, 10023, 552, 472, 295, 300, 307,
  411, 276, 3695, 86, 9898, 281, 5042, 4338, 1910, 295, 264, 3209, 370, 570, 309,
  311, 309, 311, 257, 16333, 394, 295, 13, 50964], "temperature": 0.0, "avg_logprob":
  -0.21321464909447563, "compression_ratio": 1.5251396648044693, "no_speech_prob":
  0.0077543724328279495}, {"id": 276, "seek": 294448, "start": 2959.48, "end": 2968.48,
  "text": " Distributed algorithms so like it''s like it''s not good strategically
  if you have like a global view well sometimes it helps.", "tokens": [51114, 9840,
  2024, 4866, 14642, 370, 411, 309, 311, 411, 309, 311, 406, 665, 38061, 498, 291,
  362, 411, 257, 4338, 1910, 731, 2171, 309, 3665, 13, 51564], "temperature": 0.0,
  "avg_logprob": -0.21321464909447563, "compression_ratio": 1.5251396648044693, "no_speech_prob":
  0.0077543724328279495}, {"id": 277, "seek": 296848, "start": 2969.48, "end": 2992.48,
  "text": " Like there are papers where you can and that we should make that the pass
  from the entry point of the network to every node is in short so you can make it
  but that is that breaks if you''re doing assertions for instance so like you cannot
  have a global view and dynamic nature at the same time.", "tokens": [50414, 1743,
  456, 366, 10577, 689, 291, 393, 293, 300, 321, 820, 652, 300, 264, 1320, 490, 264,
  8729, 935, 295, 264, 3209, 281, 633, 9984, 307, 294, 2099, 370, 291, 393, 652, 309,
  457, 300, 307, 300, 9857, 498, 291, 434, 884, 19810, 626, 337, 5197, 370, 411, 291,
  2644, 362, 257, 4338, 1910, 293, 8546, 3687, 412, 264, 912, 565, 13, 51564], "temperature":
  0.0, "avg_logprob": -0.17540849338878284, "compression_ratio": 1.5923913043478262,
  "no_speech_prob": 0.027314988896250725}, {"id": 278, "seek": 299248, "start": 2993.48,
  "end": 3018.48, "text": " Yeah so that that''s why I ignore some of the stuff there''s
  also a focus on like custom distances so even though the hnsw lip supports only
  free distances is pretty easy to implement what distances like you want and I believe
  that there will be a shift in like what distances are being used.", "tokens": [50414,
  865, 370, 300, 300, 311, 983, 286, 11200, 512, 295, 264, 1507, 456, 311, 611, 257,
  1879, 322, 411, 2375, 22182, 370, 754, 1673, 264, 276, 3695, 86, 8280, 9346, 787,
  1737, 22182, 307, 1238, 1858, 281, 4445, 437, 22182, 411, 291, 528, 293, 286, 1697,
  300, 456, 486, 312, 257, 5513, 294, 411, 437, 22182, 366, 885, 1143, 13, 51664],
  "temperature": 0.0, "avg_logprob": -0.17219698429107666, "compression_ratio": 1.6111111111111112,
  "no_speech_prob": 0.08882223069667816}, {"id": 279, "seek": 301848, "start": 3018.48,
  "end": 3045.48, "text": " After some time because there are problems with like those
  like those simple distances you mean like a sign cosign dot product this type of
  distances right or yeah yeah it''s more a problem that you want to embed everything
  like you want to embed an entity into a single vector representation so and that
  has limitations like as you probably know that.", "tokens": [50364, 2381, 512, 565,
  570, 456, 366, 2740, 365, 411, 729, 411, 729, 2199, 22182, 291, 914, 411, 257, 1465,
  3792, 788, 5893, 1674, 341, 2010, 295, 22182, 558, 420, 1338, 1338, 309, 311, 544,
  257, 1154, 300, 291, 528, 281, 12240, 1203, 411, 291, 528, 281, 12240, 364, 13977,
  666, 257, 2167, 8062, 10290, 370, 293, 300, 575, 15705, 411, 382, 291, 1391, 458,
  300, 13, 51714], "temperature": 0.0, "avg_logprob": -0.2616024562290737, "compression_ratio":
  1.755, "no_speech_prob": 0.04624165967106819}, {"id": 280, "seek": 304548, "start":
  3045.48, "end": 3074.48, "text": " Like transformers are based on attention and
  there before there was a like a last year with attention for translation and without
  attention of didn''t work well because it like compressed everything to a single
  vector so I believe that in some time there will be at least set distances so where
  your object and query represented as a set of like as a set of which can be shuffled
  and doesn''t change the structure.", "tokens": [50364, 1743, 4088, 433, 366, 2361,
  322, 3202, 293, 456, 949, 456, 390, 257, 411, 257, 1036, 1064, 365, 3202, 337, 12853,
  293, 1553, 3202, 295, 994, 380, 589, 731, 570, 309, 411, 30353, 1203, 281, 257,
  2167, 8062, 370, 286, 1697, 300, 294, 512, 565, 456, 486, 312, 412, 1935, 992, 22182,
  370, 689, 428, 2657, 293, 14581, 10379, 382, 257, 992, 295, 411, 382, 257, 992,
  295, 597, 393, 312, 402, 33974, 293, 1177, 380, 1319, 264, 3877, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.17764822642008463, "compression_ratio": 1.7606837606837606,
  "no_speech_prob": 0.014399350620806217}, {"id": 281, "seek": 307448, "start": 3074.48,
  "end": 3102.48, "text": " So for a user that can be like set of user interests for
  a document that can be a set of like subjects inside the document for the query
  it can be like different parts that you want to have in the query at the same time
  but those parts like might not be ordered and when you embed something you are that
  you make it ordered and like for instance when I played with clip.", "tokens": [50364,
  407, 337, 257, 4195, 300, 393, 312, 411, 992, 295, 4195, 8847, 337, 257, 4166, 300,
  393, 312, 257, 992, 295, 411, 13066, 1854, 264, 4166, 337, 264, 14581, 309, 393,
  312, 411, 819, 3166, 300, 291, 528, 281, 362, 294, 264, 14581, 412, 264, 912, 565,
  457, 729, 3166, 411, 1062, 406, 312, 8866, 293, 562, 291, 12240, 746, 291, 366,
  300, 291, 652, 309, 8866, 293, 411, 337, 5197, 562, 286, 3737, 365, 7353, 13, 51764],
  "temperature": 0.0, "avg_logprob": -0.16185068201135705, "compression_ratio": 1.8592964824120604,
  "no_speech_prob": 0.012826280668377876}, {"id": 282, "seek": 310248, "start": 3102.48,
  "end": 3131.48, "text": " So there is this for so I thought that like it can do
  what''s your which is nice so you can like have an image and like see like what
  are the words are which text is closest but definitely struggles with the notion
  of like what words are there so what is the first word yeah yeah so like geometrically
  or like in different languages it might be even different geometry of words right
  like should you read left to right or right.", "tokens": [50364, 407, 456, 307,
  341, 337, 370, 286, 1194, 300, 411, 309, 393, 360, 437, 311, 428, 597, 307, 1481,
  370, 291, 393, 411, 362, 364, 3256, 293, 411, 536, 411, 437, 366, 264, 2283, 366,
  597, 2487, 307, 13699, 457, 2138, 17592, 365, 264, 10710, 295, 411, 437, 2283, 366,
  456, 370, 437, 307, 264, 700, 1349, 1338, 1338, 370, 411, 12956, 81, 984, 420, 411,
  294, 819, 8650, 309, 1062, 312, 754, 819, 18426, 295, 2283, 558, 411, 820, 291,
  1401, 1411, 281, 558, 420, 558, 13, 51814], "temperature": 0.0, "avg_logprob": -0.3359025389283568,
  "compression_ratio": 1.8484848484848484, "no_speech_prob": 0.0416722372174263},
  {"id": 283, "seek": 313248, "start": 3132.48, "end": 3137.48, "text": " Right to
  left and then like you also need another dimension of language they are guess.",
  "tokens": [50364, 1779, 281, 1411, 293, 550, 411, 291, 611, 643, 1071, 10139, 295,
  2856, 436, 366, 2041, 13, 50614], "temperature": 0.0, "avg_logprob": -0.3035950488354786,
  "compression_ratio": 1.6363636363636365, "no_speech_prob": 0.012068433687090874},
  {"id": 284, "seek": 313248, "start": 3137.48, "end": 3161.48, "text": " Yeah, we
  can represent it as like bag of words maybe ordered bag of words is something encoding
  as all people do now for text but that that I have so I think like an end would
  need to adapt for the situation in the future and keeping the stability to add new
  distances is like is important.", "tokens": [50614, 865, 11, 321, 393, 2906, 309,
  382, 411, 3411, 295, 2283, 1310, 8866, 3411, 295, 2283, 307, 746, 43430, 382, 439,
  561, 360, 586, 337, 2487, 457, 300, 300, 286, 362, 370, 286, 519, 411, 364, 917,
  576, 643, 281, 6231, 337, 264, 2590, 294, 264, 2027, 293, 5145, 264, 11826, 281,
  909, 777, 22182, 307, 411, 307, 1021, 13, 51814], "temperature": 0.0, "avg_logprob":
  -0.3035950488354786, "compression_ratio": 1.6363636363636365, "no_speech_prob":
  0.012068433687090874}, {"id": 285, "seek": 316148, "start": 3161.48, "end": 3173.48,
  "text": " Yeah, so are you are you working on on this personally or are you like
  welcoming pool requests as they say you know to implement different distances.",
  "tokens": [50364, 865, 11, 370, 366, 291, 366, 291, 1364, 322, 322, 341, 5665, 420,
  366, 291, 411, 17378, 7005, 12475, 382, 436, 584, 291, 458, 281, 4445, 819, 22182,
  13, 50964], "temperature": 0.0, "avg_logprob": -0.19610314142136348, "compression_ratio":
  1.6022099447513811, "no_speech_prob": 0.011396877467632294}, {"id": 286, "seek":
  316148, "start": 3173.48, "end": 3184.48, "text": " Well, I''m welcoming pool requests
  for sure because those are very application specific well it''s pretty easy to implement
  like I don''t know.", "tokens": [50964, 1042, 11, 286, 478, 17378, 7005, 12475,
  337, 988, 570, 729, 366, 588, 3861, 2685, 731, 309, 311, 1238, 1858, 281, 4445,
  411, 286, 500, 380, 458, 13, 51514], "temperature": 0.0, "avg_logprob": -0.19610314142136348,
  "compression_ratio": 1.6022099447513811, "no_speech_prob": 0.011396877467632294},
  {"id": 287, "seek": 318448, "start": 3185.48, "end": 3212.48, "text": " Or some
  simple distance so you have like a set a set of distance you just select which are
  the closest out of the set so it would like many many to many somewhat similar I
  think to what colder does so though they can I think go without it but essentially
  you all you''ll need a set to set distance right yeah make sense I was since I mentioned
  it twice already I was wondering like to pick your name.", "tokens": [50414, 1610,
  512, 2199, 4560, 370, 291, 362, 411, 257, 992, 257, 992, 295, 4560, 291, 445, 3048,
  597, 366, 264, 13699, 484, 295, 264, 992, 370, 309, 576, 411, 867, 867, 281, 867,
  8344, 2531, 286, 519, 281, 437, 31020, 775, 370, 1673, 436, 393, 286, 519, 352,
  1553, 309, 457, 4476, 291, 439, 291, 603, 643, 257, 992, 281, 992, 4560, 558, 1338,
  652, 2020, 286, 390, 1670, 286, 2835, 309, 6091, 1217, 286, 390, 6359, 411, 281,
  1888, 428, 1315, 13, 51764], "temperature": 0.0, "avg_logprob": -0.2948715166113843,
  "compression_ratio": 1.7733333333333334, "no_speech_prob": 0.08927077054977417},
  {"id": 288, "seek": 321248, "start": 3212.48, "end": 3241.48, "text": " I was wondering
  like to pick your brain on what I was thinking in this space like an and trust me
  it''s absolutely very simple algorithm that I came up with the only problem is that
  I chose Python as the language and so Python has this little bit weird virtual machine
  kind of how it does the garbage collection and so what I suspect maybe it''s also
  bugging my code but on billion nodes I cannot actually make it conversion reasonable
  memory so I''m going to say.", "tokens": [50364, 286, 390, 6359, 411, 281, 1888,
  428, 3567, 322, 437, 286, 390, 1953, 294, 341, 1901, 411, 364, 293, 3361, 385, 309,
  311, 3122, 588, 2199, 9284, 300, 286, 1361, 493, 365, 264, 787, 1154, 307, 300,
  286, 5111, 15329, 382, 264, 2856, 293, 370, 15329, 575, 341, 707, 857, 3657, 6374,
  3479, 733, 295, 577, 309, 775, 264, 14150, 5765, 293, 370, 437, 286, 9091, 1310,
  309, 311, 611, 7426, 3249, 452, 3089, 457, 322, 5218, 13891, 286, 2644, 767, 652,
  309, 14298, 10585, 4675, 370, 286, 478, 516, 281, 584, 13, 51814], "temperature":
  0.0, "avg_logprob": -0.2782296446180835, "compression_ratio": 1.6824817518248176,
  "no_speech_prob": 0.005664549767971039}, {"id": 289, "seek": 324148, "start": 3241.48,
  "end": 3265.48, "text": " And so it runs out of memory like on 995 million and what
  I did I was really what like I took the input set of points right so the points
  are like 128 dimensions or 200 dimensions.", "tokens": [50364, 400, 370, 309, 6676,
  484, 295, 4675, 411, 322, 1722, 15718, 2459, 293, 437, 286, 630, 286, 390, 534,
  437, 411, 286, 1890, 264, 4846, 992, 295, 2793, 558, 370, 264, 2793, 366, 411, 29810,
  12819, 420, 2331, 12819, 13, 51564], "temperature": 0.0, "avg_logprob": -0.2871645147150213,
  "compression_ratio": 1.3636363636363635, "no_speech_prob": 0.0032338628079742193},
  {"id": 290, "seek": 326548, "start": 3265.48, "end": 3281.48, "text": " Essentially
  I pick a random point the first one not not random the first one and then I on a
  sample of points I compute a median distance right so basically what''s what''s
  the kind of average distance between between all of them in a player wise fashion.",
  "tokens": [50364, 23596, 286, 1888, 257, 4974, 935, 264, 700, 472, 406, 406, 4974,
  264, 700, 472, 293, 550, 286, 322, 257, 6889, 295, 2793, 286, 14722, 257, 26779,
  4560, 558, 370, 1936, 437, 311, 437, 311, 264, 733, 295, 4274, 4560, 1296, 1296,
  439, 295, 552, 294, 257, 4256, 10829, 6700, 13, 51164], "temperature": 0.0, "avg_logprob":
  -0.08790369033813476, "compression_ratio": 1.6217948717948718, "no_speech_prob":
  0.03686128929257393}, {"id": 291, "seek": 328148, "start": 3282.48, "end": 3308.48,
  "text": " And and so then I use that as as a filter to build what I called a sharp
  right so essentially I decided to split the billion points down to controllable
  number of charts let''s say 1000 charts right and so I pick the first point and
  then I say okay which other point is close enough so like within that median distance
  to this point.", "tokens": [50414, 400, 293, 370, 550, 286, 764, 300, 382, 382,
  257, 6608, 281, 1322, 437, 286, 1219, 257, 8199, 558, 370, 4476, 286, 3047, 281,
  7472, 264, 5218, 2793, 760, 281, 45159, 712, 1230, 295, 17767, 718, 311, 584, 9714,
  17767, 558, 293, 370, 286, 1888, 264, 700, 935, 293, 550, 286, 584, 1392, 597, 661,
  935, 307, 1998, 1547, 370, 411, 1951, 300, 26779, 4560, 281, 341, 935, 13, 51714],
  "temperature": 0.0, "avg_logprob": -0.14440786022029511, "compression_ratio": 1.6274509803921569,
  "no_speech_prob": 0.02213110215961933}, {"id": 292, "seek": 330848, "start": 3308.48,
  "end": 3333.48, "text": " And so I joined them together in the chart and as the
  chart reaches 1 million so basically if it''s like 1000 charts each chart roughly
  1 million points that''s a billion points right and then I will close that chart
  and I will run H and as double you on it so that I can actually have that chart
  as a hierarchical navigable small world graph.", "tokens": [50364, 400, 370, 286,
  6869, 552, 1214, 294, 264, 6927, 293, 382, 264, 6927, 14235, 502, 2459, 370, 1936,
  498, 309, 311, 411, 9714, 17767, 1184, 6927, 9810, 502, 2459, 2793, 300, 311, 257,
  5218, 2793, 558, 293, 550, 286, 486, 1998, 300, 6927, 293, 286, 486, 1190, 389,
  293, 382, 3834, 291, 322, 309, 370, 300, 286, 393, 767, 362, 300, 6927, 382, 257,
  35250, 804, 7407, 712, 1359, 1002, 4295, 13, 51614], "temperature": 0.0, "avg_logprob":
  -0.1812357275109542, "compression_ratio": 1.7577319587628866, "no_speech_prob":
  0.04544257000088692}, {"id": 293, "seek": 333348, "start": 3334.48, "end": 3348.48,
  "text": " And and it seems to converge like at least on 10 million it converges
  on 100 million converges it runs out of memory on one billion but I think it''s
  just some weirdness in how I do it in this big loop or overall points.", "tokens":
  [50414, 400, 293, 309, 2544, 281, 41881, 411, 412, 1935, 322, 1266, 2459, 309, 9652,
  2880, 322, 2319, 2459, 9652, 2880, 309, 6676, 484, 295, 4675, 322, 472, 5218, 457,
  286, 519, 309, 311, 445, 512, 3657, 1287, 294, 577, 286, 360, 309, 294, 341, 955,
  6367, 420, 4787, 2793, 13, 51114], "temperature": 0.0, "avg_logprob": -0.14005363429034198,
  "compression_ratio": 1.5208333333333333, "no_speech_prob": 0.019728410989046097},
  {"id": 294, "seek": 334848, "start": 3348.48, "end": 3366.48, "text": " But when
  I reached out to you on on GitHub like my idea was to also access the first layer
  of the graph so that first layer where the query will enter I could use that.",
  "tokens": [50364, 583, 562, 286, 6488, 484, 281, 291, 322, 322, 23331, 411, 452,
  1558, 390, 281, 611, 2105, 264, 700, 4583, 295, 264, 4295, 370, 300, 700, 4583,
  689, 264, 14581, 486, 3242, 286, 727, 764, 300, 13, 51264], "temperature": 0.0,
  "avg_logprob": -0.13900033439077983, "compression_ratio": 1.3770491803278688, "no_speech_prob":
  0.09835981577634811}, {"id": 295, "seek": 336648, "start": 3367.48, "end": 3393.48,
  "text": " And as the sort of entry point across this 1000 charts right so because
  I don''t want to load all 1000 into memory I want to load only sufficient amount
  of entry points so that I can quickly check which chart is closer to my query and
  then go inside that and use it as W what do you think about this idea it''s very
  simple I think.", "tokens": [50414, 400, 382, 264, 1333, 295, 8729, 935, 2108, 341,
  9714, 17767, 558, 370, 570, 286, 500, 380, 528, 281, 3677, 439, 9714, 666, 4675,
  286, 528, 281, 3677, 787, 11563, 2372, 295, 8729, 2793, 370, 300, 286, 393, 2661,
  1520, 597, 6927, 307, 4966, 281, 452, 14581, 293, 550, 352, 1854, 300, 293, 764,
  309, 382, 343, 437, 360, 291, 519, 466, 341, 1558, 309, 311, 588, 2199, 286, 519,
  13, 51714], "temperature": 0.0, "avg_logprob": -0.12703253428141276, "compression_ratio":
  1.6127450980392157, "no_speech_prob": 0.09558729082345963}, {"id": 296, "seek":
  339348, "start": 3394.48, "end": 3411.48, "text": " Yes well that that that makes
  sense so that clustering it seems to be so like you did you have like a cluster
  the points into 1000 clusters and then they select the clusters and.", "tokens":
  [50414, 1079, 731, 300, 300, 300, 1669, 2020, 370, 300, 596, 48673, 309, 2544, 281,
  312, 370, 411, 291, 630, 291, 362, 411, 257, 13630, 264, 2793, 666, 9714, 23313,
  293, 550, 436, 3048, 264, 23313, 293, 13, 51264], "temperature": 0.0, "avg_logprob":
  -0.2219376680327625, "compression_ratio": 1.575221238938053, "no_speech_prob": 0.04425818473100662},
  {"id": 297, "seek": 341148, "start": 3412.48, "end": 3421.48, "text": " Well yeah
  that that makes sense I think like historically there were other papers that suggested
  something similar to.", "tokens": [50414, 1042, 1338, 300, 300, 1669, 2020, 286,
  519, 411, 16180, 456, 645, 661, 10577, 300, 10945, 746, 2531, 281, 13, 50864], "temperature":
  0.0, "avg_logprob": -0.2000776373821756, "compression_ratio": 1.5071428571428571,
  "no_speech_prob": 0.032513830810785294}, {"id": 298, "seek": 341148, "start": 3421.48,
  "end": 3429.48, "text": " And then I think in flam so that was one of the distributors
  strategies that they suggested.", "tokens": [50864, 400, 550, 286, 519, 294, 932,
  335, 370, 300, 390, 472, 295, 264, 4400, 30751, 9029, 300, 436, 10945, 13, 51264],
  "temperature": 0.0, "avg_logprob": -0.2000776373821756, "compression_ratio": 1.5071428571428571,
  "no_speech_prob": 0.032513830810785294}, {"id": 299, "seek": 342948, "start": 3430.48,
  "end": 3451.48, "text": " Yeah well that that that might work out so that though
  that depends on on the scale so and so that also well for production system you
  also want to replicate those notes and so right.", "tokens": [50414, 865, 731, 300,
  300, 300, 1062, 589, 484, 370, 300, 1673, 300, 5946, 322, 322, 264, 4373, 370, 293,
  370, 300, 611, 731, 337, 4265, 1185, 291, 611, 528, 281, 25356, 729, 5570, 293,
  370, 558, 13, 51464], "temperature": 0.0, "avg_logprob": -0.2498370612539896, "compression_ratio":
  1.525, "no_speech_prob": 0.07719220221042633}, {"id": 300, "seek": 345148, "start":
  3452.48, "end": 3476.48, "text": " Okay maybe like let''s come from a different
  way so that you can also start to very small pieces so it might not be needed in
  this case I can want to balance so but on the top layer you can also use like as
  in this Microsoft paper that you mentioned also there are other papers like from
  young so.", "tokens": [50414, 1033, 1310, 411, 718, 311, 808, 490, 257, 819, 636,
  370, 300, 291, 393, 611, 722, 281, 588, 1359, 3755, 370, 309, 1062, 406, 312, 2978,
  294, 341, 1389, 286, 393, 528, 281, 4772, 370, 457, 322, 264, 1192, 4583, 291, 393,
  611, 764, 411, 382, 294, 341, 8116, 3035, 300, 291, 2835, 611, 456, 366, 661, 10577,
  411, 490, 2037, 370, 13, 51614], "temperature": 0.0, "avg_logprob": -0.21727066609396864,
  "compression_ratio": 1.6174863387978142, "no_speech_prob": 0.006955789867788553},
  {"id": 301, "seek": 347648, "start": 3476.48, "end": 3486.48, "text": " So I have
  a paper this those guys so you can use a in you can start into maybe not the short
  you can.", "tokens": [50364, 407, 286, 362, 257, 3035, 341, 729, 1074, 370, 291,
  393, 764, 257, 294, 291, 393, 722, 666, 1310, 406, 264, 2099, 291, 393, 13, 50864],
  "temperature": 0.0, "avg_logprob": -0.5875177712276064, "compression_ratio": 1.216867469879518,
  "no_speech_prob": 0.025405174121260643}, {"id": 302, "seek": 348648, "start": 3486.48,
  "end": 3501.48, "text": " So if you want to divide your data set into like million
  clusters and use like a higher index to decide on which chart you want to select
  it right yes.", "tokens": [50364, 407, 498, 291, 528, 281, 9845, 428, 1412, 992,
  666, 411, 2459, 23313, 293, 764, 411, 257, 2946, 8186, 281, 4536, 322, 597, 6927,
  291, 528, 281, 3048, 309, 558, 2086, 13, 51114], "temperature": 0.0, "avg_logprob":
  -0.37323816006000227, "compression_ratio": 1.532846715328467, "no_speech_prob":
  0.24684560298919678}, {"id": 303, "seek": 348648, "start": 3501.48, "end": 3506.48,
  "text": " So though like if you''re if you''re not talking about like.", "tokens":
  [51114, 407, 1673, 411, 498, 291, 434, 498, 291, 434, 406, 1417, 466, 411, 13, 51364],
  "temperature": 0.0, "avg_logprob": -0.37323816006000227, "compression_ratio": 1.532846715328467,
  "no_speech_prob": 0.24684560298919678}, {"id": 304, "seek": 350648, "start": 3506.48,
  "end": 3511.48, "text": " So it''s not a scale so probably like doesn''t make too
  much sense.", "tokens": [50364, 407, 309, 311, 406, 257, 4373, 370, 1391, 411, 1177,
  380, 652, 886, 709, 2020, 13, 50614], "temperature": 0.0, "avg_logprob": -0.24902000427246093,
  "compression_ratio": 1.6226415094339623, "no_speech_prob": 0.3841511607170105},
  {"id": 305, "seek": 350648, "start": 3511.48, "end": 3534.48, "text": " But yeah
  yeah you can do this yeah I mean I''m still hopeful to kind of keep trying it I
  have another friend who is like on Twitter he actually recorded like a YouTube video
  where he said here here and here you make a mistake like this is why you lose memory
  like you should never allocate objects inside loops you should pre-allocate them
  as NAMPA erase and so on.", "tokens": [50614, 583, 1338, 1338, 291, 393, 360, 341,
  1338, 286, 914, 286, 478, 920, 20531, 281, 733, 295, 1066, 1382, 309, 286, 362,
  1071, 1277, 567, 307, 411, 322, 5794, 415, 767, 8287, 411, 257, 3088, 960, 689,
  415, 848, 510, 510, 293, 510, 291, 652, 257, 6146, 411, 341, 307, 983, 291, 3624,
  4675, 411, 291, 820, 1128, 35713, 6565, 1854, 16121, 291, 820, 659, 12, 336, 42869,
  552, 382, 426, 2865, 10297, 23525, 293, 370, 322, 13, 51764], "temperature": 0.0,
  "avg_logprob": -0.24902000427246093, "compression_ratio": 1.6226415094339623, "no_speech_prob":
  0.3841511607170105}, {"id": 306, "seek": 353448, "start": 3534.48, "end": 3554.48,
  "text": " So with his modifications it still runs out of memory so like I need to
  kind of move forward and I''m still kind of like hopefully I can do it in Python
  but something also tells me maybe I should move to more kind of memory controllable
  language something like rast or C++ I don''t know.", "tokens": [50364, 407, 365,
  702, 26881, 309, 920, 6676, 484, 295, 4675, 370, 411, 286, 643, 281, 733, 295, 1286,
  2128, 293, 286, 478, 920, 733, 295, 411, 4696, 286, 393, 360, 309, 294, 15329, 457,
  746, 611, 5112, 385, 1310, 286, 820, 1286, 281, 544, 733, 295, 4675, 45159, 712,
  2856, 746, 411, 367, 525, 420, 383, 25472, 286, 500, 380, 458, 13, 51364], "temperature":
  0.0, "avg_logprob": -0.1569580598310991, "compression_ratio": 1.5159574468085106,
  "no_speech_prob": 0.33807137608528137}, {"id": 307, "seek": 355448, "start": 3554.48,
  "end": 3583.48, "text": " Well I''m not sure so like so using something like so
  you probably using C++ libraries from Python like NAMPA or torch yeah something
  like that so they should not click memory so those are pretty pretty controllable
  yeah yeah it is definitely my code somewhere in the loop it probably just computes
  too many time like like basically the hottest part of the algorithm like in terms
  of profiling it right is like.", "tokens": [50364, 1042, 286, 478, 406, 988, 370,
  411, 370, 1228, 746, 411, 370, 291, 1391, 1228, 383, 25472, 15148, 490, 15329, 411,
  426, 2865, 10297, 420, 27822, 1338, 746, 411, 300, 370, 436, 820, 406, 2052, 4675,
  370, 729, 366, 1238, 1238, 45159, 712, 1338, 1338, 309, 307, 2138, 452, 3089, 4079,
  294, 264, 6367, 309, 1391, 445, 715, 1819, 886, 867, 565, 411, 411, 1936, 264, 32780,
  644, 295, 264, 9284, 411, 294, 2115, 295, 1740, 4883, 309, 558, 307, 411, 13, 51814],
  "temperature": 0.0, "avg_logprob": -0.14544051192527593, "compression_ratio": 1.6942148760330578,
  "no_speech_prob": 0.044569287449121475}, {"id": 308, "seek": 358348, "start": 3583.48,
  "end": 3605.48, "text": " Like when you can so you pre compute the median distance
  once right and then you use that value all the time so it''s kind of it''s okay
  it''s just an object so it doesn''t allocate much but then as you extract the next
  batch of points so I read the one billion set in one million batches right.", "tokens":
  [50364, 1743, 562, 291, 393, 370, 291, 659, 14722, 264, 26779, 4560, 1564, 558,
  293, 550, 291, 764, 300, 2158, 439, 264, 565, 370, 309, 311, 733, 295, 309, 311,
  1392, 309, 311, 445, 364, 2657, 370, 309, 1177, 380, 35713, 709, 457, 550, 382,
  291, 8947, 264, 958, 15245, 295, 2793, 370, 286, 1401, 264, 472, 5218, 992, 294,
  472, 2459, 15245, 279, 558, 13, 51464], "temperature": 0.0, "avg_logprob": -0.13325601384259653,
  "compression_ratio": 1.6440677966101696, "no_speech_prob": 0.020004967227578163},
  {"id": 309, "seek": 360548, "start": 3606.48, "end": 3625.48, "text": " I sense
  that there could be a loss of memory because like it''s a binary file and so you
  say in NAMPA you say from this file read the next batch right so like you you provide
  the kind of offset and so I sense that maybe there it loses memory maybe not I don''t
  know.", "tokens": [50414, 286, 2020, 300, 456, 727, 312, 257, 4470, 295, 4675, 570,
  411, 309, 311, 257, 17434, 3991, 293, 370, 291, 584, 294, 426, 2865, 10297, 291,
  584, 490, 341, 3991, 1401, 264, 958, 15245, 558, 370, 411, 291, 291, 2893, 264,
  733, 295, 18687, 293, 370, 286, 2020, 300, 1310, 456, 309, 18293, 4675, 1310, 406,
  286, 500, 380, 458, 13, 51364], "temperature": 0.2, "avg_logprob": -0.24742143232743818,
  "compression_ratio": 1.698019801980198, "no_speech_prob": 0.01445314846932888},
  {"id": 310, "seek": 360548, "start": 3626.48, "end": 3634.48, "text": " Because
  I''ve noticed that in files library they use M M M M M M M M M M M M M.", "tokens":
  [51414, 1436, 286, 600, 5694, 300, 294, 7098, 6405, 436, 764, 376, 376, 376, 376,
  376, 376, 376, 376, 376, 376, 376, 376, 376, 13, 51814], "temperature": 0.2, "avg_logprob":
  -0.24742143232743818, "compression_ratio": 1.698019801980198, "no_speech_prob":
  0.01445314846932888}, {"id": 311, "seek": 363448, "start": 3634.48, "end": 3644.48,
  "text": " Yeah, I can also use M M M M. So NAMPA if you read the tenser from NAMPA
  they can also have M M M M M M M options so you can load this M M M M M M M M M
  M M M M M.", "tokens": [50364, 865, 11, 286, 393, 611, 764, 376, 376, 376, 376,
  13, 407, 426, 2865, 10297, 498, 291, 1401, 264, 10688, 260, 490, 426, 2865, 10297,
  436, 393, 611, 362, 376, 376, 376, 376, 376, 376, 376, 3956, 370, 291, 393, 3677,
  341, 376, 376, 376, 376, 376, 376, 376, 376, 376, 376, 376, 376, 376, 376, 13, 50864],
  "temperature": 0.6, "avg_logprob": -0.3152877209233303, "compression_ratio": 1.8118279569892473,
  "no_speech_prob": 0.021768230944871902}, {"id": 312, "seek": 363448, "start": 3645.48,
  "end": 3660.48, "text": " But even if you''re using if you''re reading we are like
  open like open file is like read binary it should not click memory so it should
  it should do read then it''s just like.", "tokens": [50914, 583, 754, 498, 291,
  434, 1228, 498, 291, 434, 3760, 321, 366, 411, 1269, 411, 1269, 3991, 307, 411,
  1401, 17434, 309, 820, 406, 2052, 4675, 370, 309, 820, 309, 820, 360, 1401, 550,
  309, 311, 445, 411, 13, 51664], "temperature": 0.6, "avg_logprob": -0.3152877209233303,
  "compression_ratio": 1.8118279569892473, "no_speech_prob": 0.021768230944871902},
  {"id": 313, "seek": 366048, "start": 3660.48, "end": 3668.1, "text": " Yeah, so
  it must be something super stupid then in my code that kind of like really obvious
  to somebody like you like okay", "tokens": [50364, 865, 11, 370, 309, 1633, 312,
  746, 1687, 6631, 550, 294, 452, 3089, 300, 733, 295, 411, 534, 6322, 281, 2618,
  411, 291, 411, 1392, 50745], "temperature": 0.0, "avg_logprob": -0.2828137919587909,
  "compression_ratio": 1.7114624505928853, "no_speech_prob": 0.2249089628458023},
  {"id": 314, "seek": 366048, "start": 3668.1, "end": 3670.7, "text": " Here is here
  is that point you should not do this", "tokens": [50745, 1692, 307, 510, 307, 300,
  935, 291, 820, 406, 360, 341, 50875], "temperature": 0.0, "avg_logprob": -0.2828137919587909,
  "compression_ratio": 1.7114624505928853, "no_speech_prob": 0.2249089628458023},
  {"id": 315, "seek": 366048, "start": 3670.98, "end": 3674.42, "text": " But like
  for me it''s like I invented this basic idea", "tokens": [50889, 583, 411, 337,
  385, 309, 311, 411, 286, 14479, 341, 3875, 1558, 51061], "temperature": 0.0, "avg_logprob":
  -0.2828137919587909, "compression_ratio": 1.7114624505928853, "no_speech_prob":
  0.2249089628458023}, {"id": 316, "seek": 366048, "start": 3674.76, "end": 3679.86,
  "text": " But then like pushing it maybe like like it works on 10 million and I''m
  okay", "tokens": [51078, 583, 550, 411, 7380, 309, 1310, 411, 411, 309, 1985, 322,
  1266, 2459, 293, 286, 478, 1392, 51333], "temperature": 0.0, "avg_logprob": -0.2828137919587909,
  "compression_ratio": 1.7114624505928853, "no_speech_prob": 0.2249089628458023},
  {"id": 317, "seek": 366048, "start": 3680.02, "end": 3685.44, "text": " But like
  the task was as part of this challenge to do the billion scale right so this is
  like", "tokens": [51341, 583, 411, 264, 5633, 390, 382, 644, 295, 341, 3430, 281,
  360, 264, 5218, 4373, 558, 370, 341, 307, 411, 51612], "temperature": 0.0, "avg_logprob":
  -0.2828137919587909, "compression_ratio": 1.7114624505928853, "no_speech_prob":
  0.2249089628458023}, {"id": 318, "seek": 366048, "start": 3685.96, "end": 3688.46,
  "text": " You crawl you crawl the the mountain", "tokens": [51638, 509, 24767, 291,
  24767, 264, 264, 6937, 51763], "temperature": 0.0, "avg_logprob": -0.2828137919587909,
  "compression_ratio": 1.7114624505928853, "no_speech_prob": 0.2249089628458023},
  {"id": 319, "seek": 368846, "start": 3689.02, "end": 3693.5, "text": " Without the
  top in a way, but yes, there is a top of course. It''s only one billion points",
  "tokens": [50392, 9129, 264, 1192, 294, 257, 636, 11, 457, 2086, 11, 456, 307, 257,
  1192, 295, 1164, 13, 467, 311, 787, 472, 5218, 2793, 50616], "temperature": 0.0,
  "avg_logprob": -0.286625608391718, "compression_ratio": 1.5576923076923077, "no_speech_prob":
  0.0039496049284935}, {"id": 320, "seek": 368846, "start": 3694.38, "end": 3699.7,
  "text": " But yeah, I mean it keeps me quite excited to keep doing it. Of course,
  I already see some", "tokens": [50660, 583, 1338, 11, 286, 914, 309, 5965, 385,
  1596, 2919, 281, 1066, 884, 309, 13, 2720, 1164, 11, 286, 1217, 536, 512, 50926],
  "temperature": 0.0, "avg_logprob": -0.286625608391718, "compression_ratio": 1.5576923076923077,
  "no_speech_prob": 0.0039496049284935}, {"id": 321, "seek": 368846, "start": 3700.42,
  "end": 3702.02, "text": " maybe", "tokens": [50962, 1310, 51042], "temperature":
  0.0, "avg_logprob": -0.286625608391718, "compression_ratio": 1.5576923076923077,
  "no_speech_prob": 0.0039496049284935}, {"id": 322, "seek": 368846, "start": 3702.02,
  "end": 3705.68, "text": " Need for improvements for example. How how do I make updates?",
  "tokens": [51042, 16984, 337, 13797, 337, 1365, 13, 1012, 577, 360, 286, 652, 9205,
  30, 51225], "temperature": 0.0, "avg_logprob": -0.286625608391718, "compression_ratio":
  1.5576923076923077, "no_speech_prob": 0.0039496049284935}, {"id": 323, "seek": 368846,
  "start": 3705.98, "end": 3710.3, "text": " Right, so let''s say a new point comes
  in and I have like 1000 charts predefined", "tokens": [51240, 1779, 11, 370, 718,
  311, 584, 257, 777, 935, 1487, 294, 293, 286, 362, 411, 9714, 17767, 659, 37716,
  51456], "temperature": 0.0, "avg_logprob": -0.286625608391718, "compression_ratio":
  1.5576923076923077, "no_speech_prob": 0.0039496049284935}, {"id": 324, "seek": 368846,
  "start": 3710.66, "end": 3715.84, "text": " So I need to find either an existing
  chart or create a new one at some point", "tokens": [51474, 407, 286, 643, 281,
  915, 2139, 364, 6741, 6927, 420, 1884, 257, 777, 472, 412, 512, 935, 51733], "temperature":
  0.0, "avg_logprob": -0.286625608391718, "compression_ratio": 1.5576923076923077,
  "no_speech_prob": 0.0039496049284935}, {"id": 325, "seek": 371584, "start": 3715.88,
  "end": 3723.8, "text": " So that that part I defer to the future, but like maybe
  I still need to push push harder to just converge it first", "tokens": [50366, 407,
  300, 300, 644, 286, 25704, 281, 264, 2027, 11, 457, 411, 1310, 286, 920, 643, 281,
  2944, 2944, 6081, 281, 445, 41881, 309, 700, 50762], "temperature": 0.0, "avg_logprob":
  -0.2673491564663974, "compression_ratio": 1.6164383561643836, "no_speech_prob":
  0.00398827251046896}, {"id": 326, "seek": 371584, "start": 3725.56, "end": 3733.26,
  "text": " Okay, you can profile for memory so we can like loop some operations in
  the code that you think that can leak and", "tokens": [50850, 1033, 11, 291, 393,
  7964, 337, 4675, 370, 321, 393, 411, 6367, 512, 7705, 294, 264, 3089, 300, 291,
  519, 300, 393, 17143, 293, 51235], "temperature": 0.0, "avg_logprob": -0.2673491564663974,
  "compression_ratio": 1.6164383561643836, "no_speech_prob": 0.00398827251046896},
  {"id": 327, "seek": 371584, "start": 3733.76, "end": 3735.76, "text": " Profile
  the memory for those", "tokens": [51260, 6039, 794, 264, 4675, 337, 729, 51360],
  "temperature": 0.0, "avg_logprob": -0.2673491564663974, "compression_ratio": 1.6164383561643836,
  "no_speech_prob": 0.00398827251046896}, {"id": 328, "seek": 371584, "start": 3735.76,
  "end": 3740.1200000000003, "text": " Yeah, I''ve been doing that like actually I
  also come from the world of Java so in Java it''s like", "tokens": [51360, 865,
  11, 286, 600, 668, 884, 300, 411, 767, 286, 611, 808, 490, 264, 1002, 295, 10745,
  370, 294, 10745, 309, 311, 411, 51578], "temperature": 0.0, "avg_logprob": -0.2673491564663974,
  "compression_ratio": 1.6164383561643836, "no_speech_prob": 0.00398827251046896},
  {"id": 329, "seek": 374012, "start": 3740.7999999999997, "end": 3745.64, "text":
  " Quite straightforward in a way there are also tools in Python when you plug in
  this memory profiler", "tokens": [50398, 20464, 15325, 294, 257, 636, 456, 366,
  611, 3873, 294, 15329, 562, 291, 5452, 294, 341, 4675, 1740, 5441, 50640], "temperature":
  0.0, "avg_logprob": -0.29528640914749316, "compression_ratio": 1.5872340425531914,
  "no_speech_prob": 0.012513574212789536}, {"id": 330, "seek": 374012, "start": 3745.64,
  "end": 3751.0, "text": " It slows down your computations significantly and so you
  have to wait like 10 times more", "tokens": [50640, 467, 35789, 760, 428, 2807,
  763, 10591, 293, 370, 291, 362, 281, 1699, 411, 1266, 1413, 544, 50908], "temperature":
  0.0, "avg_logprob": -0.29528640914749316, "compression_ratio": 1.5872340425531914,
  "no_speech_prob": 0.012513574212789536}, {"id": 331, "seek": 374012, "start": 3754.48,
  "end": 3763.7999999999997, "text": " Yeah, so I''m not a fan of profilers so like
  recently I find I found a video like a talk on YouTube", "tokens": [51082, 865,
  11, 370, 286, 478, 406, 257, 3429, 295, 1740, 388, 433, 370, 411, 3938, 286, 915,
  286, 1352, 257, 960, 411, 257, 751, 322, 3088, 51548], "temperature": 0.0, "avg_logprob":
  -0.29528640914749316, "compression_ratio": 1.5872340425531914, "no_speech_prob":
  0.012513574212789536}, {"id": 332, "seek": 374012, "start": 3763.7999999999997,
  "end": 3769.72, "text": " Which explain like why why we shouldn''t use profilers
  and that was like the profilers", "tokens": [51548, 3013, 2903, 411, 983, 983, 321,
  4659, 380, 764, 1740, 388, 433, 293, 300, 390, 411, 264, 1740, 388, 433, 51844],
  "temperature": 0.0, "avg_logprob": -0.29528640914749316, "compression_ratio": 1.5872340425531914,
  "no_speech_prob": 0.012513574212789536}, {"id": 333, "seek": 377012, "start": 3770.2,
  "end": 3777.2799999999997, "text": " They become obsolete when the code became like
  not multi-freaded, but like with multiple paths", "tokens": [50368, 814, 1813, 46333,
  562, 264, 3089, 3062, 411, 406, 4825, 12, 69, 2538, 292, 11, 457, 411, 365, 3866,
  14518, 50722], "temperature": 0.0, "avg_logprob": -0.496322234471639, "compression_ratio":
  1.6419213973799127, "no_speech_prob": 0.005532990675419569}, {"id": 334, "seek":
  377012, "start": 3777.2799999999997, "end": 3780.7999999999997, "text": " So when
  I''m totally this pension so pension was super scholar", "tokens": [50722, 407,
  562, 286, 478, 3879, 341, 21927, 370, 21927, 390, 1687, 17912, 50898], "temperature":
  0.0, "avg_logprob": -0.496322234471639, "compression_ratio": 1.6419213973799127,
  "no_speech_prob": 0.005532990675419569}, {"id": 335, "seek": 377012, "start": 3781.2799999999997,
  "end": 3786.48, "text": " So your operations are out of order and when you look
  at the profiler results like", "tokens": [50922, 407, 428, 7705, 366, 484, 295,
  1668, 293, 562, 291, 574, 412, 264, 1740, 5441, 3542, 411, 51182], "temperature":
  0.0, "avg_logprob": -0.496322234471639, "compression_ratio": 1.6419213973799127,
  "no_speech_prob": 0.005532990675419569}, {"id": 336, "seek": 377012, "start": 3787.24,
  "end": 3793.56, "text": " I don''t understand them so when I was developing a S&S
  W Libye, I haven''t used profilers", "tokens": [51220, 286, 500, 380, 1223, 552,
  370, 562, 286, 390, 6416, 257, 318, 5, 50, 343, 15834, 1200, 11, 286, 2378, 380,
  1143, 1740, 388, 433, 51536], "temperature": 0.0, "avg_logprob": -0.496322234471639,
  "compression_ratio": 1.6419213973799127, "no_speech_prob": 0.005532990675419569},
  {"id": 337, "seek": 377012, "start": 3793.56, "end": 3797.0, "text": " So I just
  like wrote benches for operations and", "tokens": [51536, 407, 286, 445, 411, 4114,
  3271, 3781, 337, 7705, 293, 51708], "temperature": 0.0, "avg_logprob": -0.496322234471639,
  "compression_ratio": 1.6419213973799127, "no_speech_prob": 0.005532990675419569},
  {"id": 338, "seek": 379700, "start": 3797.64, "end": 3799.64, "text": " And like
  I had like", "tokens": [50396, 400, 411, 286, 632, 411, 50496], "temperature": 0.0,
  "avg_logprob": -0.3821509225027902, "compression_ratio": 1.575, "no_speech_prob":
  0.009380927309393883}, {"id": 339, "seek": 379700, "start": 3800.16, "end": 3804.32,
  "text": " Faceline and trial so they usually work in the same memory", "tokens":
  [50522, 17667, 5440, 293, 7308, 370, 436, 2673, 589, 294, 264, 912, 4675, 50730],
  "temperature": 0.0, "avg_logprob": -0.3821509225027902, "compression_ratio": 1.575,
  "no_speech_prob": 0.009380927309393883}, {"id": 340, "seek": 379700, "start": 3804.6,
  "end": 3809.16, "text": " So the like index is the same, but there are different
  implementations of search and", "tokens": [50744, 407, 264, 411, 8186, 307, 264,
  912, 11, 457, 456, 366, 819, 4445, 763, 295, 3164, 293, 50972], "temperature": 0.0,
  "avg_logprob": -0.3821509225027902, "compression_ratio": 1.575, "no_speech_prob":
  0.009380927309393883}, {"id": 341, "seek": 379700, "start": 3809.84, "end": 3814.8,
  "text": " Like your your speed can depend on memory how you allocate the memory
  and", "tokens": [51006, 1743, 428, 428, 3073, 393, 5672, 322, 4675, 577, 291, 35713,
  264, 4675, 293, 51254], "temperature": 0.0, "avg_logprob": -0.3821509225027902,
  "compression_ratio": 1.575, "no_speech_prob": 0.009380927309393883}, {"id": 342,
  "seek": 379700, "start": 3815.96, "end": 3820.36, "text": " With those benches you
  can measure something like up to 1 or 2% of difference", "tokens": [51312, 2022,
  729, 3271, 3781, 291, 393, 3481, 746, 411, 493, 281, 502, 420, 568, 4, 295, 2649,
  51532], "temperature": 0.0, "avg_logprob": -0.3821509225027902, "compression_ratio":
  1.575, "no_speech_prob": 0.009380927309393883}, {"id": 343, "seek": 382036, "start":
  3820.96, "end": 3829.1200000000003, "text": " And when you like do a lot of benches
  with one or two percent improvement you can get like 20% improvement 50% improvement",
  "tokens": [50394, 400, 562, 291, 411, 360, 257, 688, 295, 3271, 3781, 365, 472,
  420, 732, 3043, 10444, 291, 393, 483, 411, 945, 4, 10444, 2625, 4, 10444, 50802],
  "temperature": 0.0, "avg_logprob": -0.35023237410045804, "compression_ratio": 1.7584541062801933,
  "no_speech_prob": 0.00907359179109335}, {"id": 344, "seek": 382036, "start": 3831.04,
  "end": 3839.44, "text": " Yeah, but like I never used profiles and like I never
  saw like in my life that people use profiles and like get", "tokens": [50898, 865,
  11, 457, 411, 286, 1128, 1143, 23693, 293, 411, 286, 1128, 1866, 411, 294, 452,
  993, 300, 561, 764, 23693, 293, 411, 483, 51318], "temperature": 0.0, "avg_logprob":
  -0.35023237410045804, "compression_ratio": 1.7584541062801933, "no_speech_prob":
  0.00907359179109335}, {"id": 345, "seek": 382036, "start": 3840.1600000000003, "end":
  3843.1600000000003, "text": " really complicated insights from using profiles",
  "tokens": [51354, 534, 6179, 14310, 490, 1228, 23693, 51504], "temperature": 0.0,
  "avg_logprob": -0.35023237410045804, "compression_ratio": 1.7584541062801933, "no_speech_prob":
  0.00907359179109335}, {"id": 346, "seek": 382036, "start": 3843.1600000000003, "end":
  3847.92, "text": " Yeah, I agree like we we did like so we''re building also building
  a search engine", "tokens": [51504, 865, 11, 286, 3986, 411, 321, 321, 630, 411,
  370, 321, 434, 2390, 611, 2390, 257, 3164, 2848, 51742], "temperature": 0.0, "avg_logprob":
  -0.35023237410045804, "compression_ratio": 1.7584541062801933, "no_speech_prob":
  0.00907359179109335}, {"id": 347, "seek": 384792, "start": 3848.4, "end": 3857.76,
  "text": " With like we had like by design we had like billions of documents and
  each document was just a short sentence like a statement from a document real document",
  "tokens": [50388, 2022, 411, 321, 632, 411, 538, 1715, 321, 632, 411, 17375, 295,
  8512, 293, 1184, 4166, 390, 445, 257, 2099, 8174, 411, 257, 5629, 490, 257, 4166,
  957, 4166, 50856], "temperature": 0.0, "avg_logprob": -0.2521374667132342, "compression_ratio":
  1.7876447876447876, "no_speech_prob": 0.008226973004639149}, {"id": 348, "seek":
  384792, "start": 3858.28, "end": 3866.08, "text": " And of course we were running
  out like we were running into all this garbage collector stop the world problems
  and so on and we were running this", "tokens": [50882, 400, 295, 1164, 321, 645,
  2614, 484, 411, 321, 645, 2614, 666, 439, 341, 14150, 23960, 1590, 264, 1002, 2740,
  293, 370, 322, 293, 321, 645, 2614, 341, 51272], "temperature": 0.0, "avg_logprob":
  -0.2521374667132342, "compression_ratio": 1.7876447876447876, "no_speech_prob":
  0.008226973004639149}, {"id": 349, "seek": 384792, "start": 3866.08, "end": 3872.08,
  "text": " Profilers, I think one of them was J rocket and then others and like when
  you see the graphs you''re like, okay", "tokens": [51272, 6039, 388, 433, 11, 286,
  519, 472, 295, 552, 390, 508, 13012, 293, 550, 2357, 293, 411, 562, 291, 536, 264,
  24877, 291, 434, 411, 11, 1392, 51572], "temperature": 0.0, "avg_logprob": -0.2521374667132342,
  "compression_ratio": 1.7876447876447876, "no_speech_prob": 0.008226973004639149},
  {"id": 350, "seek": 384792, "start": 3872.64, "end": 3876.08, "text": " So now I
  know yes it leaks, but what should I do?", "tokens": [51600, 407, 586, 286, 458,
  2086, 309, 28885, 11, 457, 437, 820, 286, 360, 30, 51772], "temperature": 0.0, "avg_logprob":
  -0.2521374667132342, "compression_ratio": 1.7876447876447876, "no_speech_prob":
  0.008226973004639149}, {"id": 351, "seek": 387608, "start": 3876.7999999999997,
  "end": 3880.96, "text": " So or it tells you that your code is using like", "tokens":
  [50400, 407, 420, 309, 5112, 291, 300, 428, 3089, 307, 1228, 411, 50608], "temperature":
  0.0, "avg_logprob": -0.3873465061187744, "compression_ratio": 1.5691489361702127,
  "no_speech_prob": 0.01709228754043579}, {"id": 352, "seek": 387608, "start": 3881.52,
  "end": 3884.7999999999997, "text": " Biterase too much like what can you do other
  than that?", "tokens": [50636, 363, 1681, 651, 886, 709, 411, 437, 393, 291, 360,
  661, 813, 300, 30, 50800], "temperature": 0.0, "avg_logprob": -0.3873465061187744,
  "compression_ratio": 1.5691489361702127, "no_speech_prob": 0.01709228754043579},
  {"id": 353, "seek": 387608, "start": 3887.56, "end": 3893.7999999999997, "text":
  " Yeah, and for performance it''s even worse. So you see that like this model takes
  a lot of time, but", "tokens": [50938, 865, 11, 293, 337, 3389, 309, 311, 754, 5324,
  13, 407, 291, 536, 300, 411, 341, 2316, 2516, 257, 688, 295, 565, 11, 457, 51250],
  "temperature": 0.0, "avg_logprob": -0.3873465061187744, "compression_ratio": 1.5691489361702127,
  "no_speech_prob": 0.01709228754043579}, {"id": 354, "seek": 387608, "start": 3895.68,
  "end": 3902.56, "text": " The in a multi multi threaded world that like it''s not
  for sure. So you may improve it that", "tokens": [51344, 440, 294, 257, 4825, 4825,
  47493, 1002, 300, 411, 309, 311, 406, 337, 988, 13, 407, 291, 815, 3470, 309, 300,
  51688], "temperature": 0.0, "avg_logprob": -0.3873465061187744, "compression_ratio":
  1.5691489361702127, "no_speech_prob": 0.01709228754043579}, {"id": 355, "seek":
  390256, "start": 3903.36, "end": 3910.0, "text": " Like and that happened so quite
  quite quite a few times so people went to me and said like", "tokens": [50404, 1743,
  293, 300, 2011, 370, 1596, 1596, 1596, 257, 1326, 1413, 370, 561, 1437, 281, 385,
  293, 848, 411, 50736], "temperature": 0.0, "avg_logprob": -0.3109179941813151, "compression_ratio":
  1.595, "no_speech_prob": 0.009028066881000996}, {"id": 356, "seek": 390256, "start":
  3911.04, "end": 3914.56, "text": " You''re analysis of performance contradictory",
  "tokens": [50788, 509, 434, 5215, 295, 3389, 49555, 50964], "temperature": 0.0,
  "avg_logprob": -0.3109179941813151, "compression_ratio": 1.595, "no_speech_prob":
  0.009028066881000996}, {"id": 357, "seek": 390256, "start": 3915.84, "end": 3917.84,
  "text": " Profile blocks", "tokens": [51028, 6039, 794, 8474, 51128], "temperature":
  0.0, "avg_logprob": -0.3109179941813151, "compression_ratio": 1.595, "no_speech_prob":
  0.009028066881000996}, {"id": 358, "seek": 390256, "start": 3918.96, "end": 3922.88,
  "text": " And that''s okay, right because you didn''t optimize for the profiler",
  "tokens": [51184, 400, 300, 311, 1392, 11, 558, 570, 291, 994, 380, 19719, 337,
  264, 1740, 5441, 51380], "temperature": 0.0, "avg_logprob": -0.3109179941813151,
  "compression_ratio": 1.595, "no_speech_prob": 0.009028066881000996}, {"id": 359,
  "seek": 390256, "start": 3924.4, "end": 3930.48, "text": " Yeah, because profiler
  cannot like so it cannot say to you what would happen if you change something",
  "tokens": [51456, 865, 11, 570, 1740, 5441, 2644, 411, 370, 309, 2644, 584, 281,
  291, 437, 576, 1051, 498, 291, 1319, 746, 51760], "temperature": 0.0, "avg_logprob":
  -0.3109179941813151, "compression_ratio": 1.595, "no_speech_prob": 0.009028066881000996},
  {"id": 360, "seek": 393048, "start": 3930.88, "end": 3935.44, "text": " Exactly,
  it''s just a snapshot. Yeah, it''s just a snapshot. Yeah, exactly", "tokens": [50384,
  7587, 11, 309, 311, 445, 257, 30163, 13, 865, 11, 309, 311, 445, 257, 30163, 13,
  865, 11, 2293, 50612], "temperature": 0.0, "avg_logprob": -0.32242582241694134,
  "compression_ratio": 1.7136563876651982, "no_speech_prob": 0.004768346436321735},
  {"id": 361, "seek": 393048, "start": 3935.92, "end": 3940.64, "text": " And and
  like coming back to hsw what are you hoping to achieve like", "tokens": [50636,
  400, 293, 411, 1348, 646, 281, 276, 82, 86, 437, 366, 291, 7159, 281, 4584, 411,
  50872], "temperature": 0.0, "avg_logprob": -0.32242582241694134, "compression_ratio":
  1.7136563876651982, "no_speech_prob": 0.004768346436321735}, {"id": 362, "seek":
  393048, "start": 3941.28, "end": 3944.8, "text": " Maybe in some midterm future
  for example like", "tokens": [50904, 2704, 294, 512, 2062, 7039, 2027, 337, 1365,
  411, 51080], "temperature": 0.0, "avg_logprob": -0.32242582241694134, "compression_ratio":
  1.7136563876651982, "no_speech_prob": 0.004768346436321735}, {"id": 363, "seek":
  393048, "start": 3945.92, "end": 3953.12, "text": " Why do you decide at work which
  where the reimplementation as w is when they add symbolic filtering?", "tokens":
  [51136, 1545, 360, 291, 4536, 412, 589, 597, 689, 264, 33433, 781, 19631, 382, 261,
  307, 562, 436, 909, 25755, 30822, 30, 51496], "temperature": 0.0, "avg_logprob":
  -0.32242582241694134, "compression_ratio": 1.7136563876651982, "no_speech_prob":
  0.004768346436321735}, {"id": 364, "seek": 393048, "start": 3953.6, "end": 3959.6,
  "text": " So like what would it take in your original paper in your original algorithm
  to add symbolic filters?", "tokens": [51520, 407, 411, 437, 576, 309, 747, 294,
  428, 3380, 3035, 294, 428, 3380, 9284, 281, 909, 25755, 15995, 30, 51820], "temperature":
  0.0, "avg_logprob": -0.32242582241694134, "compression_ratio": 1.7136563876651982,
  "no_speech_prob": 0.004768346436321735}, {"id": 365, "seek": 395960, "start": 3959.8399999999997,
  "end": 3963.2799999999997, "text": " How does it change the dynamic of that graph
  and search?", "tokens": [50376, 1012, 775, 309, 1319, 264, 8546, 295, 300, 4295,
  293, 3164, 30, 50548], "temperature": 0.0, "avg_logprob": -0.21966276729808135,
  "compression_ratio": 1.7327188940092166, "no_speech_prob": 0.003681499743834138},
  {"id": 366, "seek": 395960, "start": 3964.4, "end": 3973.52, "text": " Uh, well,
  it seems like for me like so I can correlate interest to and then and interest to
  symbolic filtering", "tokens": [50604, 4019, 11, 731, 11, 309, 2544, 411, 337, 385,
  411, 370, 286, 393, 48742, 1179, 281, 293, 550, 293, 1179, 281, 25755, 30822, 51060],
  "temperature": 0.0, "avg_logprob": -0.21966276729808135, "compression_ratio": 1.7327188940092166,
  "no_speech_prob": 0.003681499743834138}, {"id": 367, "seek": 395960, "start": 3973.8399999999997,
  "end": 3982.7999999999997, "text": " So like I think two years ago I haven''t heard
  like people talk about symbolic filtering in an but now like it''s a hot topic",
  "tokens": [51076, 407, 411, 286, 519, 732, 924, 2057, 286, 2378, 380, 2198, 411,
  561, 751, 466, 25755, 30822, 294, 364, 457, 586, 411, 309, 311, 257, 2368, 4829,
  51524], "temperature": 0.0, "avg_logprob": -0.21966276729808135, "compression_ratio":
  1.7327188940092166, "no_speech_prob": 0.003681499743834138}, {"id": 368, "seek":
  395960, "start": 3983.44, "end": 3988.08, "text": " Like from different places people
  want symbolic filtering that is like for targeting", "tokens": [51556, 1743, 490,
  819, 3190, 561, 528, 25755, 30822, 300, 307, 411, 337, 17918, 51788], "temperature":
  0.0, "avg_logprob": -0.21966276729808135, "compression_ratio": 1.7327188940092166,
  "no_speech_prob": 0.003681499743834138}, {"id": 369, "seek": 398808, "start": 3988.72,
  "end": 3994.64, "text": " So like for ads. Yeah, you can you want to have some targeting
  for the audience or some other", "tokens": [50396, 407, 411, 337, 10342, 13, 865,
  11, 291, 393, 291, 528, 281, 362, 512, 17918, 337, 264, 4034, 420, 512, 661, 50692],
  "temperature": 0.0, "avg_logprob": -0.24053382873535156, "compression_ratio": 1.5404040404040404,
  "no_speech_prob": 0.0013806666247546673}, {"id": 370, "seek": 398808, "start": 3995.2,
  "end": 3996.48, "text": " filters and", "tokens": [50720, 15995, 293, 50784], "temperature":
  0.0, "avg_logprob": -0.24053382873535156, "compression_ratio": 1.5404040404040404,
  "no_speech_prob": 0.0013806666247546673}, {"id": 371, "seek": 398808, "start": 3997.68,
  "end": 4001.12, "text": " But I see that as outside of the end and itself", "tokens":
  [50844, 583, 286, 536, 300, 382, 2380, 295, 264, 917, 293, 2564, 51016], "temperature":
  0.0, "avg_logprob": -0.24053382873535156, "compression_ratio": 1.5404040404040404,
  "no_speech_prob": 0.0013806666247546673}, {"id": 372, "seek": 398808, "start": 4001.92,
  "end": 4003.92, "text": " so", "tokens": [51056, 370, 51156], "temperature": 0.0,
  "avg_logprob": -0.24053382873535156, "compression_ratio": 1.5404040404040404, "no_speech_prob":
  0.0013806666247546673}, {"id": 373, "seek": 398808, "start": 4003.92, "end": 4008.08,
  "text": " As I said when working on a startup so our first application was", "tokens":
  [51156, 1018, 286, 848, 562, 1364, 322, 257, 18578, 370, 527, 700, 3861, 390, 51364],
  "temperature": 0.0, "avg_logprob": -0.24053382873535156, "compression_ratio": 1.5404040404040404,
  "no_speech_prob": 0.0013806666247546673}, {"id": 374, "seek": 398808, "start": 4008.96,
  "end": 4014.4, "text": " Doing something like symbolic filtering and there it''s
  easier in some sense because", "tokens": [51408, 18496, 746, 411, 25755, 30822,
  293, 456, 309, 311, 3571, 294, 512, 2020, 570, 51680], "temperature": 0.0, "avg_logprob":
  -0.24053382873535156, "compression_ratio": 1.5404040404040404, "no_speech_prob":
  0.0013806666247546673}, {"id": 375, "seek": 401440, "start": 4014.8, "end": 4021.36,
  "text": " Like as you said there is a problem of this distances and high-dimensional
  space and this problem", "tokens": [50384, 1743, 382, 291, 848, 456, 307, 257, 1154,
  295, 341, 22182, 293, 1090, 12, 18759, 1901, 293, 341, 1154, 50712], "temperature":
  0.0, "avg_logprob": -0.2316982632591611, "compression_ratio": 1.6396396396396395,
  "no_speech_prob": 0.0011786088580265641}, {"id": 376, "seek": 401440, "start": 4021.44,
  "end": 4023.6800000000003, "text": " There is no such problem in symbolic filtering",
  "tokens": [50716, 821, 307, 572, 1270, 1154, 294, 25755, 30822, 50828], "temperature":
  0.0, "avg_logprob": -0.2316982632591611, "compression_ratio": 1.6396396396396395,
  "no_speech_prob": 0.0011786088580265641}, {"id": 377, "seek": 401440, "start": 4024.7200000000003,
  "end": 4030.56, "text": " So symbolic filtering you have a query that have exact
  result and yeah, if you write the SQL query", "tokens": [50880, 407, 25755, 30822,
  291, 362, 257, 14581, 300, 362, 1900, 1874, 293, 1338, 11, 498, 291, 2464, 264,
  19200, 14581, 51172], "temperature": 0.0, "avg_logprob": -0.2316982632591611, "compression_ratio":
  1.6396396396396395, "no_speech_prob": 0.0011786088580265641}, {"id": 378, "seek":
  401440, "start": 4031.12, "end": 4037.92, "text": " So it can be optimized to work
  efficiently and but the iNM does a very different job. It does approximate", "tokens":
  [51200, 407, 309, 393, 312, 26941, 281, 589, 19621, 293, 457, 264, 741, 45, 44,
  775, 257, 588, 819, 1691, 13, 467, 775, 30874, 51540], "temperature": 0.0, "avg_logprob":
  -0.2316982632591611, "compression_ratio": 1.6396396396396395, "no_speech_prob":
  0.0011786088580265641}, {"id": 379, "seek": 401440, "start": 4038.7200000000003,
  "end": 4040.4, "text": " Yeah filtering", "tokens": [51580, 865, 30822, 51664],
  "temperature": 0.0, "avg_logprob": -0.2316982632591611, "compression_ratio": 1.6396396396396395,
  "no_speech_prob": 0.0011786088580265641}, {"id": 380, "seek": 404040, "start": 4040.48,
  "end": 4048.56, "text": " We can kind of mix them together. So if you add like so
  you have a distance and like you add some", "tokens": [50368, 492, 393, 733, 295,
  2890, 552, 1214, 13, 407, 498, 291, 909, 411, 370, 291, 362, 257, 4560, 293, 411,
  291, 909, 512, 50772], "temperature": 0.0, "avg_logprob": -0.16905040171608995,
  "compression_ratio": 1.5913978494623655, "no_speech_prob": 0.001725785550661385},
  {"id": 381, "seek": 404040, "start": 4050.4, "end": 4057.6, "text": " Like prefix
  for that which somehow captures the symbolic filtering and you can build an index
  that also like takes", "tokens": [50864, 1743, 46969, 337, 300, 597, 6063, 27986,
  264, 25755, 30822, 293, 291, 393, 1322, 364, 8186, 300, 611, 411, 2516, 51224],
  "temperature": 0.0, "avg_logprob": -0.16905040171608995, "compression_ratio": 1.5913978494623655,
  "no_speech_prob": 0.001725785550661385}, {"id": 382, "seek": 404040, "start": 4059.36,
  "end": 4064.48, "text": " Takes account and like there are some other people who
  suggested to do that as well", "tokens": [51312, 44347, 2696, 293, 411, 456, 366,
  512, 661, 561, 567, 10945, 281, 360, 300, 382, 731, 51568], "temperature": 0.0,
  "avg_logprob": -0.16905040171608995, "compression_ratio": 1.5913978494623655, "no_speech_prob":
  0.001725785550661385}, {"id": 383, "seek": 406448, "start": 4065.2, "end": 4069.04,
  "text": " But the problem here like and yeah, that can help so during search", "tokens":
  [50400, 583, 264, 1154, 510, 411, 293, 1338, 11, 300, 393, 854, 370, 1830, 3164,
  50592], "temperature": 0.0, "avg_logprob": -0.22255685594346789, "compression_ratio":
  1.7254098360655739, "no_speech_prob": 0.008683813735842705}, {"id": 384, "seek":
  406448, "start": 4069.36, "end": 4078.48, "text": " So if you filter by the symbol
  and like you can easily add filtering so when hnsw does filtering for deletes like
  can be done the same way", "tokens": [50608, 407, 498, 291, 6608, 538, 264, 5986,
  293, 411, 291, 393, 3612, 909, 30822, 370, 562, 276, 3695, 86, 775, 30822, 337,
  1103, 37996, 411, 393, 312, 1096, 264, 912, 636, 51064], "temperature": 0.0, "avg_logprob":
  -0.22255685594346789, "compression_ratio": 1.7254098360655739, "no_speech_prob":
  0.008683813735842705}, {"id": 385, "seek": 406448, "start": 4080.08, "end": 4082.08,
  "text": " Yeah, you can extract", "tokens": [51144, 865, 11, 291, 393, 8947, 51244],
  "temperature": 0.0, "avg_logprob": -0.22255685594346789, "compression_ratio": 1.7254098360655739,
  "no_speech_prob": 0.008683813735842705}, {"id": 386, "seek": 406448, "start": 4082.08,
  "end": 4088.4, "text": " Like only elements that pass the filter and there is some
  like guidance on the graph because you create that wizard", "tokens": [51244, 1743,
  787, 4959, 300, 1320, 264, 6608, 293, 456, 307, 512, 411, 10056, 322, 264, 4295,
  570, 291, 1884, 300, 25807, 51560], "temperature": 0.0, "avg_logprob": -0.22255685594346789,
  "compression_ratio": 1.7254098360655739, "no_speech_prob": 0.008683813735842705},
  {"id": 387, "seek": 406448, "start": 4089.12, "end": 4094.2400000000002, "text":
  " But for me like I don''t know so you have like huge number of possible filters",
  "tokens": [51596, 583, 337, 385, 411, 286, 500, 380, 458, 370, 291, 362, 411, 2603,
  1230, 295, 1944, 15995, 51852], "temperature": 0.0, "avg_logprob": -0.22255685594346789,
  "compression_ratio": 1.7254098360655739, "no_speech_prob": 0.008683813735842705},
  {"id": 388, "seek": 409448, "start": 4094.56, "end": 4101.68, "text": " So what
  will be the metric and how would you balance it with the like approximate network
  that creates a lot of problems", "tokens": [50368, 407, 437, 486, 312, 264, 20678,
  293, 577, 576, 291, 4772, 309, 365, 264, 411, 30874, 3209, 300, 7829, 257, 688,
  295, 2740, 50724], "temperature": 0.0, "avg_logprob": -0.2755220247351605, "compression_ratio":
  1.6440677966101696, "no_speech_prob": 0.0027677782345563173}, {"id": 389, "seek":
  409448, "start": 4102.24, "end": 4104.24, "text": " I think yeah, and I", "tokens":
  [50752, 286, 519, 1338, 11, 293, 286, 50852], "temperature": 0.0, "avg_logprob":
  -0.2755220247351605, "compression_ratio": 1.6440677966101696, "no_speech_prob":
  0.0027677782345563173}, {"id": 390, "seek": 409448, "start": 4104.88, "end": 4110.32,
  "text": " I thought that the best solution would be like to keep this like to some
  extent", "tokens": [50884, 286, 1194, 300, 264, 1151, 3827, 576, 312, 411, 281,
  1066, 341, 411, 281, 512, 8396, 51156], "temperature": 0.0, "avg_logprob": -0.2755220247351605,
  "compression_ratio": 1.6440677966101696, "no_speech_prob": 0.0027677782345563173},
  {"id": 391, "seek": 409448, "start": 4111.52, "end": 4117.36, "text": " But focus
  more on like how do you can chart the index according to those like", "tokens":
  [51216, 583, 1879, 544, 322, 411, 577, 360, 291, 393, 6927, 264, 8186, 4650, 281,
  729, 411, 51508], "temperature": 0.0, "avg_logprob": -0.2755220247351605, "compression_ratio":
  1.6440677966101696, "no_speech_prob": 0.0027677782345563173}, {"id": 392, "seek":
  409448, "start": 4118.96, "end": 4123.28, "text": " Great theory don''t that there
  are sharp. So you can like do SQL queries like for instance", "tokens": [51588,
  3769, 5261, 500, 380, 300, 456, 366, 8199, 13, 407, 291, 393, 411, 360, 19200, 24109,
  411, 337, 5197, 51804], "temperature": 0.0, "avg_logprob": -0.2755220247351605,
  "compression_ratio": 1.6440677966101696, "no_speech_prob": 0.0027677782345563173},
  {"id": 393, "seek": 412328, "start": 4124.08, "end": 4126.0, "text": " Like there
  are some queries that can", "tokens": [50404, 1743, 456, 366, 512, 24109, 300, 393,
  50500], "temperature": 0.0, "avg_logprob": -0.21215457706661014, "compression_ratio":
  1.6604651162790698, "no_speech_prob": 0.004452978726476431}, {"id": 394, "seek":
  412328, "start": 4127.04, "end": 4128.88, "text": " Work well with this filtering",
  "tokens": [50552, 6603, 731, 365, 341, 30822, 50644], "temperature": 0.0, "avg_logprob":
  -0.21215457706661014, "compression_ratio": 1.6604651162790698, "no_speech_prob":
  0.004452978726476431}, {"id": 395, "seek": 412328, "start": 4129.679999999999, "end":
  4135.44, "text": " Like if you''re most of like or like I don''t know 20% of the
  elements pass the symbolic filter", "tokens": [50684, 1743, 498, 291, 434, 881,
  295, 411, 420, 411, 286, 500, 380, 458, 945, 4, 295, 264, 4959, 1320, 264, 25755,
  6608, 50972], "temperature": 0.0, "avg_logprob": -0.21215457706661014, "compression_ratio":
  1.6604651162790698, "no_speech_prob": 0.004452978726476431}, {"id": 396, "seek":
  412328, "start": 4135.84, "end": 4137.84, "text": " So that is fine you can use
  it", "tokens": [50992, 407, 300, 307, 2489, 291, 393, 764, 309, 51092], "temperature":
  0.0, "avg_logprob": -0.21215457706661014, "compression_ratio": 1.6604651162790698,
  "no_speech_prob": 0.004452978726476431}, {"id": 397, "seek": 412328, "start": 4137.92,
  "end": 4145.44, "text": " But maybe there are some queries for which like I know
  only like one of a million passes them and those are in different parts", "tokens":
  [51096, 583, 1310, 456, 366, 512, 24109, 337, 597, 411, 286, 458, 787, 411, 472,
  295, 257, 2459, 11335, 552, 293, 729, 366, 294, 819, 3166, 51472], "temperature":
  0.0, "avg_logprob": -0.21215457706661014, "compression_ratio": 1.6604651162790698,
  "no_speech_prob": 0.004452978726476431}, {"id": 398, "seek": 412328, "start": 4145.84,
  "end": 4147.44, "text": " Yeah exactly space", "tokens": [51492, 865, 2293, 1901,
  51572], "temperature": 0.0, "avg_logprob": -0.21215457706661014, "compression_ratio":
  1.6604651162790698, "no_speech_prob": 0.004452978726476431}, {"id": 399, "seek":
  412328, "start": 4148.16, "end": 4150.08, "text": " So for them you can", "tokens":
  [51608, 407, 337, 552, 291, 393, 51704], "temperature": 0.0, "avg_logprob": -0.21215457706661014,
  "compression_ratio": 1.6604651162790698, "no_speech_prob": 0.004452978726476431},
  {"id": 400, "seek": 415008, "start": 4150.24, "end": 4152.24, "text": " Uh", "tokens":
  [50372, 4019, 50472], "temperature": 0.0, "avg_logprob": -0.28486966623843296, "compression_ratio":
  1.74235807860262, "no_speech_prob": 0.003158317180350423}, {"id": 401, "seek": 415008,
  "start": 4152.24, "end": 4156.88, "text": " See in real time. So you like you search
  and you see that it doesn''t perform well", "tokens": [50472, 3008, 294, 957, 565,
  13, 407, 291, 411, 291, 3164, 293, 291, 536, 300, 309, 1177, 380, 2042, 731, 50704],
  "temperature": 0.0, "avg_logprob": -0.28486966623843296, "compression_ratio": 1.74235807860262,
  "no_speech_prob": 0.003158317180350423}, {"id": 402, "seek": 415008, "start": 4158.08,
  "end": 4160.24, "text": " Uh for those and you can just", "tokens": [50764, 4019,
  337, 729, 293, 291, 393, 445, 50872], "temperature": 0.0, "avg_logprob": -0.28486966623843296,
  "compression_ratio": 1.74235807860262, "no_speech_prob": 0.003158317180350423},
  {"id": 403, "seek": 415008, "start": 4160.88, "end": 4167.36, "text": " Build the
  separate index for them right because you know those are small those are people
  want to find them", "tokens": [50904, 11875, 264, 4994, 8186, 337, 552, 558, 570,
  291, 458, 729, 366, 1359, 729, 366, 561, 528, 281, 915, 552, 51228], "temperature":
  0.0, "avg_logprob": -0.28486966623843296, "compression_ratio": 1.74235807860262,
  "no_speech_prob": 0.003158317180350423}, {"id": 404, "seek": 415008, "start": 4168.24,
  "end": 4174.08, "text": " Uh, maybe there are enough maybe they''re out of a billion,
  but if you have three LN elements, so there''s like a million of them", "tokens":
  [51272, 4019, 11, 1310, 456, 366, 1547, 1310, 436, 434, 484, 295, 257, 5218, 11,
  457, 498, 291, 362, 1045, 441, 45, 4959, 11, 370, 456, 311, 411, 257, 2459, 295,
  552, 51564], "temperature": 0.0, "avg_logprob": -0.28486966623843296, "compression_ratio":
  1.74235807860262, "no_speech_prob": 0.003158317180350423}, {"id": 405, "seek": 415008,
  "start": 4174.64, "end": 4177.28, "text": " So you you you cash them like build
  a cash index", "tokens": [51592, 407, 291, 291, 291, 6388, 552, 411, 1322, 257,
  6388, 8186, 51724], "temperature": 0.0, "avg_logprob": -0.28486966623843296, "compression_ratio":
  1.74235807860262, "no_speech_prob": 0.003158317180350423}, {"id": 406, "seek": 417728,
  "start": 4177.92, "end": 4181.92, "text": " For those on the fly so that is like
  discrete optimization problem", "tokens": [50396, 1171, 729, 322, 264, 3603, 370,
  300, 307, 411, 27706, 19618, 1154, 50596], "temperature": 0.0, "avg_logprob": -0.2454017167238845,
  "compression_ratio": 1.7025862068965518, "no_speech_prob": 0.012665307149291039},
  {"id": 407, "seek": 417728, "start": 4182.5599999999995, "end": 4186.639999999999,
  "text": " And I think that''s a bit outside of the index because index is like",
  "tokens": [50628, 400, 286, 519, 300, 311, 257, 857, 2380, 295, 264, 8186, 570,
  8186, 307, 411, 50832], "temperature": 0.0, "avg_logprob": -0.2454017167238845,
  "compression_ratio": 1.7025862068965518, "no_speech_prob": 0.012665307149291039},
  {"id": 408, "seek": 417728, "start": 4188.16, "end": 4189.84, "text": " Uh", "tokens":
  [50908, 4019, 50992], "temperature": 0.0, "avg_logprob": -0.2454017167238845, "compression_ratio":
  1.7025862068965518, "no_speech_prob": 0.012665307149291039}, {"id": 409, "seek":
  417728, "start": 4189.92, "end": 4192.5599999999995, "text": " Yeah, so it''s focused
  on the different part. Yeah", "tokens": [50996, 865, 11, 370, 309, 311, 5178, 322,
  264, 819, 644, 13, 865, 51128], "temperature": 0.0, "avg_logprob": -0.2454017167238845,
  "compression_ratio": 1.7025862068965518, "no_speech_prob": 0.012665307149291039},
  {"id": 410, "seek": 417728, "start": 4193.44, "end": 4200.24, "text": " Yeah, and
  I really I don''t think that other algorithms like and an algorithms can like somehow
  avoid this problem", "tokens": [51172, 865, 11, 293, 286, 534, 286, 500, 380, 519,
  300, 661, 14642, 411, 293, 364, 14642, 393, 411, 6063, 5042, 341, 1154, 51512],
  "temperature": 0.0, "avg_logprob": -0.2454017167238845, "compression_ratio": 1.7025862068965518,
  "no_speech_prob": 0.012665307149291039}, {"id": 411, "seek": 417728, "start": 4200.96,
  "end": 4205.679999999999, "text": " Yeah exactly. Yeah, I mean it sounds yeah, what
  would you say like you find a stunt correctly", "tokens": [51548, 865, 2293, 13,
  865, 11, 286, 914, 309, 3263, 1338, 11, 437, 576, 291, 584, 411, 291, 915, 257,
  33391, 8944, 51784], "temperature": 0.0, "avg_logprob": -0.2454017167238845, "compression_ratio":
  1.7025862068965518, "no_speech_prob": 0.012665307149291039}, {"id": 412, "seek":
  420568, "start": 4205.76, "end": 4208.320000000001, "text": " Like a little bit
  like a and then contradicts", "tokens": [50368, 1743, 257, 707, 857, 411, 257, 293,
  550, 28900, 82, 50496], "temperature": 0.0, "avg_logprob": -0.24843960541945237,
  "compression_ratio": 1.7046413502109705, "no_speech_prob": 0.004104072693735361},
  {"id": 413, "seek": 420568, "start": 4209.04, "end": 4215.04, "text": " Just kind
  of the nature of symbolic filtering in some sense, but still people do it right
  so for example in VEV8", "tokens": [50532, 1449, 733, 295, 264, 3687, 295, 25755,
  30822, 294, 512, 2020, 11, 457, 920, 561, 360, 309, 558, 370, 337, 1365, 294, 691,
  36, 53, 23, 50832], "temperature": 0.0, "avg_logprob": -0.24843960541945237, "compression_ratio":
  1.7046413502109705, "no_speech_prob": 0.004104072693735361}, {"id": 414, "seek":
  420568, "start": 4215.4400000000005, "end": 4222.08, "text": " And in quadrant they
  did it right so like you and in milbus as well, but it''s funny like in milbus they
  use", "tokens": [50852, 400, 294, 46856, 436, 630, 309, 558, 370, 411, 291, 293,
  294, 1962, 21441, 382, 731, 11, 457, 309, 311, 4074, 411, 294, 1962, 21441, 436,
  764, 51184], "temperature": 0.0, "avg_logprob": -0.24843960541945237, "compression_ratio":
  1.7046413502109705, "no_speech_prob": 0.004104072693735361}, {"id": 415, "seek":
  420568, "start": 4223.360000000001, "end": 4228.88, "text": " Fies and then other
  algorithms, right, but they say we only support you know integer", "tokens": [51248,
  479, 530, 293, 550, 661, 14642, 11, 558, 11, 457, 436, 584, 321, 787, 1406, 291,
  458, 24922, 51524], "temperature": 0.0, "avg_logprob": -0.24843960541945237, "compression_ratio":
  1.7046413502109705, "no_speech_prob": 0.004104072693735361}, {"id": 416, "seek":
  420568, "start": 4229.4400000000005, "end": 4232.240000000001, "text": " Fields,
  but we don''t support for example strings yet", "tokens": [51552, 48190, 11, 457,
  321, 500, 380, 1406, 337, 1365, 13985, 1939, 51692], "temperature": 0.0, "avg_logprob":
  -0.24843960541945237, "compression_ratio": 1.7046413502109705, "no_speech_prob":
  0.004104072693735361}, {"id": 417, "seek": 423224, "start": 4232.32, "end": 4236.32,
  "text": " So we are working on adding strings which means essentially they''re designing
  like", "tokens": [50368, 407, 321, 366, 1364, 322, 5127, 13985, 597, 1355, 4476,
  436, 434, 14685, 411, 50568], "temperature": 0.0, "avg_logprob": -0.2312630773748009,
  "compression_ratio": 1.6434108527131783, "no_speech_prob": 0.0019731600768864155},
  {"id": 418, "seek": 423224, "start": 4237.28, "end": 4240.96, "text": " This graph
  somehow in such a way that okay, it doesn''t support strings yet", "tokens": [50616,
  639, 4295, 6063, 294, 1270, 257, 636, 300, 1392, 11, 309, 1177, 380, 1406, 13985,
  1939, 50800], "temperature": 0.0, "avg_logprob": -0.2312630773748009, "compression_ratio":
  1.6434108527131783, "no_speech_prob": 0.0019731600768864155}, {"id": 419, "seek":
  423224, "start": 4241.679999999999, "end": 4243.679999999999, "text": " Maybe because
  it''s not so easy", "tokens": [50836, 2704, 570, 309, 311, 406, 370, 1858, 50936],
  "temperature": 0.0, "avg_logprob": -0.2312630773748009, "compression_ratio": 1.6434108527131783,
  "no_speech_prob": 0.0019731600768864155}, {"id": 420, "seek": 423224, "start": 4244.0,
  "end": 4246.0, "text": " To to to to to edit right", "tokens": [50952, 1407, 281,
  281, 281, 281, 8129, 558, 51052], "temperature": 0.0, "avg_logprob": -0.2312630773748009,
  "compression_ratio": 1.6434108527131783, "no_speech_prob": 0.0019731600768864155},
  {"id": 421, "seek": 423224, "start": 4246.32, "end": 4252.96, "text": " Well, I
  I''m not sure so that also depends how you measure the performance like if you have
  rare queries", "tokens": [51068, 1042, 11, 286, 286, 478, 406, 988, 370, 300, 611,
  5946, 577, 291, 3481, 264, 3389, 411, 498, 291, 362, 5892, 24109, 51400], "temperature":
  0.0, "avg_logprob": -0.2312630773748009, "compression_ratio": 1.6434108527131783,
  "no_speech_prob": 0.0019731600768864155}, {"id": 422, "seek": 423224, "start": 4253.44,
  "end": 4259.12, "text": " That switch the rich don''t have any result. So like you
  pro like your algorithm doesn''t even work on them", "tokens": [51424, 663, 3679,
  264, 4593, 500, 380, 362, 604, 1874, 13, 407, 411, 291, 447, 411, 428, 9284, 1177,
  380, 754, 589, 322, 552, 51708], "temperature": 0.0, "avg_logprob": -0.2312630773748009,
  "compression_ratio": 1.6434108527131783, "no_speech_prob": 0.0019731600768864155},
  {"id": 423, "seek": 425912, "start": 4259.599999999999, "end": 4266.64, "text":
  " But you either are rare to you measure the like overall recall and you don''t
  see it like any problems", "tokens": [50388, 583, 291, 2139, 366, 5892, 281, 291,
  3481, 264, 411, 4787, 9901, 293, 291, 500, 380, 536, 309, 411, 604, 2740, 50740],
  "temperature": 0.0, "avg_logprob": -0.23749273794668693, "compression_ratio": 1.6273584905660377,
  "no_speech_prob": 0.0017013797769322991}, {"id": 424, "seek": 425912, "start": 4267.5199999999995,
  "end": 4273.599999999999, "text": " So definitely you can build the solution maybe
  like some simple with like filtering during search", "tokens": [50784, 407, 2138,
  291, 393, 1322, 264, 3827, 1310, 411, 512, 2199, 365, 411, 30822, 1830, 3164, 51088],
  "temperature": 0.0, "avg_logprob": -0.23749273794668693, "compression_ratio": 1.6273584905660377,
  "no_speech_prob": 0.0017013797769322991}, {"id": 425, "seek": 425912, "start": 4274.4,
  "end": 4276.24, "text": " but like", "tokens": [51128, 457, 411, 51220], "temperature":
  0.0, "avg_logprob": -0.23749273794668693, "compression_ratio": 1.6273584905660377,
  "no_speech_prob": 0.0017013797769322991}, {"id": 426, "seek": 425912, "start": 4276.24,
  "end": 4281.28, "text": " It sure it will fail on some points and that is suboptimal
  in terms of latency", "tokens": [51220, 467, 988, 309, 486, 3061, 322, 512, 2793,
  293, 300, 307, 1422, 5747, 10650, 294, 2115, 295, 27043, 51472], "temperature":
  0.0, "avg_logprob": -0.23749273794668693, "compression_ratio": 1.6273584905660377,
  "no_speech_prob": 0.0017013797769322991}, {"id": 427, "seek": 425912, "start": 4282.16,
  "end": 4285.28, "text": " Yeah, so if you if you''re talking about existing solution",
  "tokens": [51516, 865, 11, 370, 498, 291, 498, 291, 434, 1417, 466, 6741, 3827,
  51672], "temperature": 0.0, "avg_logprob": -0.23749273794668693, "compression_ratio":
  1.6273584905660377, "no_speech_prob": 0.0017013797769322991}, {"id": 428, "seek":
  428528, "start": 4285.759999999999, "end": 4290.8, "text": " Maybe they have like
  a really good solution, which I just don''t know I looked at few", "tokens": [50388,
  2704, 436, 362, 411, 257, 534, 665, 3827, 11, 597, 286, 445, 500, 380, 458, 286,
  2956, 412, 1326, 50640], "temperature": 0.0, "avg_logprob": -0.22526710264144406,
  "compression_ratio": 1.6150627615062763, "no_speech_prob": 0.004469835199415684},
  {"id": 429, "seek": 428528, "start": 4292.0, "end": 4295.679999999999, "text": "
  Uh, and that was mostly like filtering inside the graph", "tokens": [50700, 4019,
  11, 293, 300, 390, 5240, 411, 30822, 1854, 264, 4295, 50884], "temperature": 0.0,
  "avg_logprob": -0.22526710264144406, "compression_ratio": 1.6150627615062763, "no_speech_prob":
  0.004469835199415684}, {"id": 430, "seek": 428528, "start": 4296.48, "end": 4304.24,
  "text": " So like if you if you if you if you have really rare elements which are
  like distributed across the search space", "tokens": [50924, 407, 411, 498, 291,
  498, 291, 498, 291, 498, 291, 362, 534, 5892, 4959, 597, 366, 411, 12631, 2108,
  264, 3164, 1901, 51312], "temperature": 0.0, "avg_logprob": -0.22526710264144406,
  "compression_ratio": 1.6150627615062763, "no_speech_prob": 0.004469835199415684},
  {"id": 431, "seek": 428528, "start": 4305.5199999999995, "end": 4308.48, "text":
  " Evenly like in different parts. So it will struggle", "tokens": [51376, 2754,
  356, 411, 294, 819, 3166, 13, 407, 309, 486, 7799, 51524], "temperature": 0.0, "avg_logprob":
  -0.22526710264144406, "compression_ratio": 1.6150627615062763, "no_speech_prob":
  0.004469835199415684}, {"id": 432, "seek": 428528, "start": 4309.28, "end": 4313.599999999999,
  "text": " Because you need to just do brute force of the whole to find them. Yeah,
  exactly", "tokens": [51564, 1436, 291, 643, 281, 445, 360, 47909, 3464, 295, 264,
  1379, 281, 915, 552, 13, 865, 11, 2293, 51780], "temperature": 0.0, "avg_logprob":
  -0.22526710264144406, "compression_ratio": 1.6150627615062763, "no_speech_prob":
  0.004469835199415684}, {"id": 433, "seek": 431360, "start": 4313.68, "end": 4318.4800000000005,
  "text": " I mean to me it sounds like computerial explosion like if I add more and
  more symbolic filters", "tokens": [50368, 286, 914, 281, 385, 309, 3263, 411, 3820,
  831, 15673, 411, 498, 286, 909, 544, 293, 544, 25755, 15995, 50608], "temperature":
  0.0, "avg_logprob": -0.19057241760858215, "compression_ratio": 1.7877551020408162,
  "no_speech_prob": 0.0008095403900370002}, {"id": 434, "seek": 431360, "start": 4318.96,
  "end": 4322.72, "text": " Like essentially I''m introducing like new sub spaces
  in my space, right?", "tokens": [50632, 1743, 4476, 286, 478, 15424, 411, 777, 1422,
  7673, 294, 452, 1901, 11, 558, 30, 50820], "temperature": 0.0, "avg_logprob": -0.19057241760858215,
  "compression_ratio": 1.7877551020408162, "no_speech_prob": 0.0008095403900370002},
  {"id": 435, "seek": 431360, "start": 4322.96, "end": 4329.92, "text": " So like
  I need to like push these points somehow closer to each other within that specific
  symbolic filter", "tokens": [50832, 407, 411, 286, 643, 281, 411, 2944, 613, 2793,
  6063, 4966, 281, 1184, 661, 1951, 300, 2685, 25755, 6608, 51180], "temperature":
  0.0, "avg_logprob": -0.19057241760858215, "compression_ratio": 1.7877551020408162,
  "no_speech_prob": 0.0008095403900370002}, {"id": 436, "seek": 431360, "start": 4330.0,
  "end": 4335.68, "text": " But if I add more of them now I have like kind of like
  multi-dimensional space of filters, right?", "tokens": [51184, 583, 498, 286, 909,
  544, 295, 552, 586, 286, 362, 411, 733, 295, 411, 4825, 12, 18759, 1901, 295, 15995,
  11, 558, 30, 51468], "temperature": 0.0, "avg_logprob": -0.19057241760858215, "compression_ratio":
  1.7877551020408162, "no_speech_prob": 0.0008095403900370002}, {"id": 437, "seek":
  431360, "start": 4336.8, "end": 4341.04, "text": " Yeah, and you you have a really
  high dimensional space of filters", "tokens": [51524, 865, 11, 293, 291, 291, 362,
  257, 534, 1090, 18795, 1901, 295, 15995, 51736], "temperature": 0.0, "avg_logprob":
  -0.19057241760858215, "compression_ratio": 1.7877551020408162, "no_speech_prob":
  0.0008095403900370002}, {"id": 438, "seek": 434104, "start": 4341.12, "end": 4343.84,
  "text": " But you don''t really know like the distribution of queries", "tokens":
  [50368, 583, 291, 500, 380, 534, 458, 411, 264, 7316, 295, 24109, 50504], "temperature":
  0.0, "avg_logprob": -0.17489470056740633, "compression_ratio": 1.7183098591549295,
  "no_speech_prob": 0.002023716690018773}, {"id": 439, "seek": 434104, "start": 4344.56,
  "end": 4349.68, "text": " For those filters it should be very different because
  those are user distribution", "tokens": [50540, 1171, 729, 15995, 309, 820, 312,
  588, 819, 570, 729, 366, 4195, 7316, 50796], "temperature": 0.0, "avg_logprob":
  -0.17489470056740633, "compression_ratio": 1.7183098591549295, "no_speech_prob":
  0.002023716690018773}, {"id": 440, "seek": 434104, "start": 4350.4, "end": 4354.08,
  "text": " Yeah, so that also will make the problem more complicated", "tokens":
  [50832, 865, 11, 370, 300, 611, 486, 652, 264, 1154, 544, 6179, 51016], "temperature":
  0.0, "avg_logprob": -0.17489470056740633, "compression_ratio": 1.7183098591549295,
  "no_speech_prob": 0.002023716690018773}, {"id": 441, "seek": 434104, "start": 4354.24,
  "end": 4359.2, "text": " So it still can work if you if the especially if distribution
  is kind of similar", "tokens": [51024, 407, 309, 920, 393, 589, 498, 291, 498, 264,
  2318, 498, 7316, 307, 733, 295, 2531, 51272], "temperature": 0.0, "avg_logprob":
  -0.17489470056740633, "compression_ratio": 1.7183098591549295, "no_speech_prob":
  0.002023716690018773}, {"id": 442, "seek": 434104, "start": 4359.68, "end": 4363.68,
  "text": " So it will work if you crank up the parameters of the graph", "tokens":
  [51296, 407, 309, 486, 589, 498, 291, 21263, 493, 264, 9834, 295, 264, 4295, 51496],
  "temperature": 0.0, "avg_logprob": -0.17489470056740633, "compression_ratio": 1.7183098591549295,
  "no_speech_prob": 0.002023716690018773}, {"id": 443, "seek": 434104, "start": 4364.56,
  "end": 4366.56, "text": " Yeah, use more connections", "tokens": [51540, 865, 11,
  764, 544, 9271, 51640], "temperature": 0.0, "avg_logprob": -0.17489470056740633,
  "compression_ratio": 1.7183098591549295, "no_speech_prob": 0.002023716690018773},
  {"id": 444, "seek": 436656, "start": 4366.64, "end": 4373.200000000001, "text":
  " But so there is a mismatch so during query your distribution may be very different
  and you need to think about it", "tokens": [50368, 583, 370, 456, 307, 257, 23220,
  852, 370, 1830, 14581, 428, 7316, 815, 312, 588, 819, 293, 291, 643, 281, 519, 466,
  309, 50696], "temperature": 0.0, "avg_logprob": -0.20746775540438564, "compression_ratio":
  1.82421875, "no_speech_prob": 0.004831674508750439}, {"id": 445, "seek": 436656,
  "start": 4373.84, "end": 4375.200000000001, "text": " So like", "tokens": [50728,
  407, 411, 50796], "temperature": 0.0, "avg_logprob": -0.20746775540438564, "compression_ratio":
  1.82421875, "no_speech_prob": 0.004831674508750439}, {"id": 446, "seek": 436656,
  "start": 4375.200000000001, "end": 4380.240000000001, "text": " How you balance
  those inside so you have like two types of distance and how you balance them", "tokens":
  [50796, 1012, 291, 4772, 729, 1854, 370, 291, 362, 411, 732, 3467, 295, 4560, 293,
  577, 291, 4772, 552, 51048], "temperature": 0.0, "avg_logprob": -0.20746775540438564,
  "compression_ratio": 1.82421875, "no_speech_prob": 0.004831674508750439}, {"id":
  447, "seek": 436656, "start": 4380.240000000001, "end": 4383.52, "text": " You want
  to balance it so the the query distribution", "tokens": [51048, 509, 528, 281, 4772,
  309, 370, 264, 264, 14581, 7316, 51212], "temperature": 0.0, "avg_logprob": -0.20746775540438564,
  "compression_ratio": 1.82421875, "no_speech_prob": 0.004831674508750439}, {"id":
  448, "seek": 436656, "start": 4384.080000000001, "end": 4385.280000000001, "text":
  " Yeah", "tokens": [51240, 865, 51300], "temperature": 0.0, "avg_logprob": -0.20746775540438564,
  "compression_ratio": 1.82421875, "no_speech_prob": 0.004831674508750439}, {"id":
  449, "seek": 436656, "start": 4385.280000000001, "end": 4391.84, "text": " That''s
  that''s that''s this field like I think this field of vector search doesn''t make
  you excited that you you contributed to it", "tokens": [51300, 663, 311, 300, 311,
  300, 311, 341, 2519, 411, 286, 519, 341, 2519, 295, 8062, 3164, 1177, 380, 652,
  291, 2919, 300, 291, 291, 18434, 281, 309, 51628], "temperature": 0.0, "avg_logprob":
  -0.20746775540438564, "compression_ratio": 1.82421875, "no_speech_prob": 0.004831674508750439},
  {"id": 450, "seek": 436656, "start": 4391.92, "end": 4396.0, "text": " Like how
  do you feel about this field that is emerging right now?", "tokens": [51632, 1743,
  577, 360, 291, 841, 466, 341, 2519, 300, 307, 14989, 558, 586, 30, 51836], "temperature":
  0.0, "avg_logprob": -0.20746775540438564, "compression_ratio": 1.82421875, "no_speech_prob":
  0.004831674508750439}, {"id": 451, "seek": 439656, "start": 4397.200000000001, "end":
  4402.64, "text": " Well, I think it is very important so right now I''m working
  mostly on applications", "tokens": [50396, 1042, 11, 286, 519, 309, 307, 588, 1021,
  370, 558, 586, 286, 478, 1364, 5240, 322, 5821, 50668], "temperature": 0.0, "avg_logprob":
  -0.255834477742513, "compression_ratio": 1.575609756097561, "no_speech_prob": 0.0015009396011009812},
  {"id": 452, "seek": 439656, "start": 4403.52, "end": 4405.52, "text": " how to",
  "tokens": [50712, 577, 281, 50812], "temperature": 0.0, "avg_logprob": -0.255834477742513,
  "compression_ratio": 1.575609756097561, "no_speech_prob": 0.0015009396011009812},
  {"id": 453, "seek": 439656, "start": 4406.400000000001, "end": 4411.04, "text":
  " Like get advantage of this and so there are many applications", "tokens": [50856,
  1743, 483, 5002, 295, 341, 293, 370, 456, 366, 867, 5821, 51088], "temperature":
  0.0, "avg_logprob": -0.255834477742513, "compression_ratio": 1.575609756097561,
  "no_speech_prob": 0.0015009396011009812}, {"id": 454, "seek": 439656, "start": 4412.320000000001,
  "end": 4417.120000000001, "text": " Which cannot be done without efficient search
  like there was a paper for deep mind", "tokens": [51152, 3013, 2644, 312, 1096,
  1553, 7148, 3164, 411, 456, 390, 257, 3035, 337, 2452, 1575, 51392], "temperature":
  0.0, "avg_logprob": -0.255834477742513, "compression_ratio": 1.575609756097561,
  "no_speech_prob": 0.0015009396011009812}, {"id": 455, "seek": 439656, "start": 4417.6,
  "end": 4420.4800000000005, "text": " Like was quite recently where they used search",
  "tokens": [51416, 1743, 390, 1596, 3938, 689, 436, 1143, 3164, 51560], "temperature":
  0.0, "avg_logprob": -0.255834477742513, "compression_ratio": 1.575609756097561,
  "no_speech_prob": 0.0015009396011009812}, {"id": 456, "seek": 439656, "start": 4421.4400000000005,
  "end": 4424.96, "text": " Uh like inside of the network and uh well", "tokens":
  [51608, 4019, 411, 1854, 295, 264, 3209, 293, 2232, 731, 51784], "temperature":
  0.0, "avg_logprob": -0.255834477742513, "compression_ratio": 1.575609756097561,
  "no_speech_prob": 0.0015009396011009812}, {"id": 457, "seek": 442656, "start": 4426.64,
  "end": 4428.64, "text": " That makes a lot of sense", "tokens": [50368, 663, 1669,
  257, 688, 295, 2020, 50468], "temperature": 0.0, "avg_logprob": -0.3023087637765067,
  "compression_ratio": 1.75, "no_speech_prob": 0.0007562597165815532}, {"id": 458,
  "seek": 442656, "start": 4428.64, "end": 4430.400000000001, "text": " And I think",
  "tokens": [50468, 400, 286, 519, 50556], "temperature": 0.0, "avg_logprob": -0.3023087637765067,
  "compression_ratio": 1.75, "no_speech_prob": 0.0007562597165815532}, {"id": 459,
  "seek": 442656, "start": 4431.4400000000005, "end": 4434.8, "text": " Yeah, there
  will be more papers and that there were papers before that paper", "tokens": [50608,
  865, 11, 456, 486, 312, 544, 10577, 293, 300, 456, 645, 10577, 949, 300, 3035, 50776],
  "temperature": 0.0, "avg_logprob": -0.3023087637765067, "compression_ratio": 1.75,
  "no_speech_prob": 0.0007562597165815532}, {"id": 460, "seek": 442656, "start": 4435.76,
  "end": 4442.160000000001, "text": " But there will be more papers that use an M
  inside the inside the big like a huge nal p model", "tokens": [50824, 583, 456,
  486, 312, 544, 10577, 300, 764, 364, 376, 1854, 264, 1854, 264, 955, 411, 257, 2603,
  297, 304, 280, 2316, 51144], "temperature": 0.0, "avg_logprob": -0.3023087637765067,
  "compression_ratio": 1.75, "no_speech_prob": 0.0007562597165815532}, {"id": 461,
  "seek": 442656, "start": 4442.96, "end": 4446.8, "text": " Yeah, yeah, for example
  like this uh learning to hash methods", "tokens": [51184, 865, 11, 1338, 11, 337,
  1365, 411, 341, 2232, 2539, 281, 22019, 7150, 51376], "temperature": 0.0, "avg_logprob":
  -0.3023087637765067, "compression_ratio": 1.75, "no_speech_prob": 0.0007562597165815532},
  {"id": 462, "seek": 442656, "start": 4446.8, "end": 4448.72, "text": " I don''t
  know if you heard about them", "tokens": [51376, 286, 500, 380, 458, 498, 291, 2198,
  466, 552, 51472], "temperature": 0.0, "avg_logprob": -0.3023087637765067, "compression_ratio":
  1.75, "no_speech_prob": 0.0007562597165815532}, {"id": 463, "seek": 442656, "start":
  4448.72, "end": 4451.76, "text": " So like um there are like when I when I tried
  to kind of", "tokens": [51472, 407, 411, 1105, 456, 366, 411, 562, 286, 562, 286,
  3031, 281, 733, 295, 51624], "temperature": 0.0, "avg_logprob": -0.3023087637765067,
  "compression_ratio": 1.75, "no_speech_prob": 0.0007562597165815532}, {"id": 464,
  "seek": 445176, "start": 4452.56, "end": 4457.280000000001, "text": " Put everything
  into their buckets like how many different types of algorithms exist", "tokens":
  [50404, 4935, 1203, 666, 641, 32191, 411, 577, 867, 819, 3467, 295, 14642, 2514,
  50640], "temperature": 0.0, "avg_logprob": -0.21257998303669254, "compression_ratio":
  1.6320754716981132, "no_speech_prob": 0.004206873942166567}, {"id": 465, "seek":
  445176, "start": 4457.76, "end": 4462.88, "text": " Like I didn''t know about learning
  to hash. It seems to be like one of the recent uh developments", "tokens": [50664,
  1743, 286, 994, 380, 458, 466, 2539, 281, 22019, 13, 467, 2544, 281, 312, 411, 472,
  295, 264, 5162, 2232, 20862, 50920], "temperature": 0.0, "avg_logprob": -0.21257998303669254,
  "compression_ratio": 1.6320754716981132, "no_speech_prob": 0.004206873942166567},
  {"id": 466, "seek": 445176, "start": 4464.16, "end": 4467.2, "text": " Are you following
  up on that as well or uh", "tokens": [50984, 2014, 291, 3480, 493, 322, 300, 382,
  731, 420, 2232, 51136], "temperature": 0.0, "avg_logprob": -0.21257998303669254,
  "compression_ratio": 1.6320754716981132, "no_speech_prob": 0.004206873942166567},
  {"id": 467, "seek": 445176, "start": 4467.92, "end": 4476.08, "text": " Well learning
  to hash so like I''m not really following that so learning to hash was before hnsw",
  "tokens": [51172, 1042, 2539, 281, 22019, 370, 411, 286, 478, 406, 534, 3480, 300,
  370, 2539, 281, 22019, 390, 949, 276, 3695, 86, 51580], "temperature": 0.0, "avg_logprob":
  -0.21257998303669254, "compression_ratio": 1.6320754716981132, "no_speech_prob":
  0.004206873942166567}, {"id": 468, "seek": 445176, "start": 4476.8, "end": 4478.8,
  "text": " Okay, there are algorithms", "tokens": [51616, 1033, 11, 456, 366, 14642,
  51716], "temperature": 0.0, "avg_logprob": -0.21257998303669254, "compression_ratio":
  1.6320754716981132, "no_speech_prob": 0.004206873942166567}, {"id": 469, "seek":
  447880, "start": 4478.88, "end": 4485.4400000000005, "text": " And uh when I talked
  with people who did like were specialized on product quantization and review the
  papers", "tokens": [50368, 400, 2232, 562, 286, 2825, 365, 561, 567, 630, 411, 645,
  19813, 322, 1674, 4426, 2144, 293, 3131, 264, 10577, 50696], "temperature": 0.0,
  "avg_logprob": -0.23785109852635583, "compression_ratio": 1.6056338028169015, "no_speech_prob":
  0.0006676787161268294}, {"id": 470, "seek": 447880, "start": 4486.320000000001,
  "end": 4493.84, "text": " Uh, they told me that like learning to hash never reaches
  the performance of like post quantization", "tokens": [50740, 4019, 11, 436, 1907,
  385, 300, 411, 2539, 281, 22019, 1128, 14235, 264, 3389, 295, 411, 2183, 4426, 2144,
  51116], "temperature": 0.0, "avg_logprob": -0.23785109852635583, "compression_ratio":
  1.6056338028169015, "no_speech_prob": 0.0006676787161268294}, {"id": 471, "seek":
  447880, "start": 4494.4800000000005, "end": 4497.28, "text": " Like at least at
  what that was like a few years ago", "tokens": [51148, 1743, 412, 1935, 412, 437,
  300, 390, 411, 257, 1326, 924, 2057, 51288], "temperature": 0.0, "avg_logprob":
  -0.23785109852635583, "compression_ratio": 1.6056338028169015, "no_speech_prob":
  0.0006676787161268294}, {"id": 472, "seek": 447880, "start": 4498.56, "end": 4501.12,
  "text": " Yeah, and uh yeah, maybe like", "tokens": [51352, 865, 11, 293, 2232,
  1338, 11, 1310, 411, 51480], "temperature": 0.0, "avg_logprob": -0.23785109852635583,
  "compression_ratio": 1.6056338028169015, "no_speech_prob": 0.0006676787161268294},
  {"id": 473, "seek": 447880, "start": 4502.72, "end": 4504.72, "text": " Now it''s
  solved", "tokens": [51560, 823, 309, 311, 13041, 51660], "temperature": 0.0, "avg_logprob":
  -0.23785109852635583, "compression_ratio": 1.6056338028169015, "no_speech_prob":
  0.0006676787161268294}, {"id": 474, "seek": 447880, "start": 4505.4400000000005,
  "end": 4508.320000000001, "text": " Uh, but like when I talk about an n", "tokens":
  [51696, 4019, 11, 457, 411, 562, 286, 751, 466, 364, 297, 51840], "temperature":
  0.0, "avg_logprob": -0.23785109852635583, "compression_ratio": 1.6056338028169015,
  "no_speech_prob": 0.0006676787161268294}, {"id": 475, "seek": 450880, "start": 4509.12,
  "end": 4512.08, "text": " Inside the i think about like about graph in it", "tokens":
  [50380, 15123, 264, 741, 519, 466, 411, 466, 4295, 294, 309, 50528], "temperature":
  0.0, "avg_logprob": -0.28593329020908903, "compression_ratio": 1.635, "no_speech_prob":
  0.0005888649611733854}, {"id": 476, "seek": 450880, "start": 4512.88, "end": 4514.4800000000005,
  "text": " So yeah, yeah, and", "tokens": [50568, 407, 1338, 11, 1338, 11, 293, 50648],
  "temperature": 0.0, "avg_logprob": -0.28593329020908903, "compression_ratio": 1.635,
  "no_speech_prob": 0.0005888649611733854}, {"id": 477, "seek": 450880, "start": 4515.52,
  "end": 4517.52, "text": " Yeah, and uh", "tokens": [50700, 865, 11, 293, 2232, 50800],
  "temperature": 0.0, "avg_logprob": -0.28593329020908903, "compression_ratio": 1.635,
  "no_speech_prob": 0.0005888649611733854}, {"id": 478, "seek": 450880, "start": 4517.52,
  "end": 4521.4400000000005, "text": " So one interesting thing also can happen uh
  like with graphs", "tokens": [50800, 407, 472, 1880, 551, 611, 393, 1051, 2232,
  411, 365, 24877, 50996], "temperature": 0.0, "avg_logprob": -0.28593329020908903,
  "compression_ratio": 1.635, "no_speech_prob": 0.0005888649611733854}, {"id": 479,
  "seek": 450880, "start": 4522.08, "end": 4530.0, "text": " So what what like what
  is an additional advantage of graph uh nearest neighbors to your engines is that
  you can change the metric", "tokens": [51028, 407, 437, 437, 411, 437, 307, 364,
  4497, 5002, 295, 4295, 2232, 23831, 12512, 281, 428, 12982, 307, 300, 291, 393,
  1319, 264, 20678, 51424], "temperature": 0.0, "avg_logprob": -0.28593329020908903,
  "compression_ratio": 1.635, "no_speech_prob": 0.0005888649611733854}, {"id": 480,
  "seek": 450880, "start": 4531.52, "end": 4533.52, "text": " Uh, so", "tokens": [51500,
  4019, 11, 370, 51600], "temperature": 0.0, "avg_logprob": -0.28593329020908903,
  "compression_ratio": 1.635, "no_speech_prob": 0.0005888649611733854}, {"id": 481,
  "seek": 450880, "start": 4533.6, "end": 4536.64, "text": " For instance if you are
  doing multi-stage ranking", "tokens": [51604, 1171, 5197, 498, 291, 366, 884, 4825,
  12, 17882, 17833, 51756], "temperature": 0.0, "avg_logprob": -0.28593329020908903,
  "compression_ratio": 1.635, "no_speech_prob": 0.0005888649611733854}, {"id": 482,
  "seek": 453664, "start": 4537.12, "end": 4538.320000000001, "text": " Like the",
  "tokens": [50388, 1743, 264, 50448], "temperature": 0.0, "avg_logprob": -0.3003704522245674,
  "compression_ratio": 1.8436018957345972, "no_speech_prob": 0.001609328668564558},
  {"id": 483, "seek": 453664, "start": 4538.320000000001, "end": 4544.72, "text":
  " You have like and you have multiple candidate sources like for search you have
  something like like like the m25", "tokens": [50448, 509, 362, 411, 293, 291, 362,
  3866, 11532, 7139, 411, 337, 3164, 291, 362, 746, 411, 411, 411, 264, 275, 6074,
  50768], "temperature": 0.0, "avg_logprob": -0.3003704522245674, "compression_ratio":
  1.8436018957345972, "no_speech_prob": 0.001609328668564558}, {"id": 484, "seek":
  453664, "start": 4545.360000000001, "end": 4548.4800000000005, "text": " Also you
  might have embeddings like with similarity search", "tokens": [50800, 2743, 291,
  1062, 362, 12240, 29432, 411, 365, 32194, 3164, 50956], "temperature": 0.0, "avg_logprob":
  -0.3003704522245674, "compression_ratio": 1.8436018957345972, "no_speech_prob":
  0.001609328668564558}, {"id": 485, "seek": 453664, "start": 4550.0, "end": 4554.0,
  "text": " So uh, and those are like three that are separate sources and then ranked",
  "tokens": [51032, 407, 2232, 11, 293, 729, 366, 411, 1045, 300, 366, 4994, 7139,
  293, 550, 20197, 51232], "temperature": 0.0, "avg_logprob": -0.3003704522245674,
  "compression_ratio": 1.8436018957345972, "no_speech_prob": 0.001609328668564558},
  {"id": 486, "seek": 453664, "start": 4554.88, "end": 4560.240000000001, "text":
  " Uh, but essentially like why do you need an n like for the first like from from
  the beginning", "tokens": [51276, 4019, 11, 457, 4476, 411, 983, 360, 291, 643,
  364, 297, 411, 337, 264, 700, 411, 490, 490, 264, 2863, 51544], "temperature": 0.0,
  "avg_logprob": -0.3003704522245674, "compression_ratio": 1.8436018957345972, "no_speech_prob":
  0.001609328668564558}, {"id": 487, "seek": 453664, "start": 4560.96, "end": 4563.360000000001,
  "text": " Uh, you need an n to speed up the ranking", "tokens": [51580, 4019, 11,
  291, 643, 364, 297, 281, 3073, 493, 264, 17833, 51700], "temperature": 0.0, "avg_logprob":
  -0.3003704522245674, "compression_ratio": 1.8436018957345972, "no_speech_prob":
  0.001609328668564558}, {"id": 488, "seek": 456336, "start": 4563.44, "end": 4566.719999999999,
  "text": " So essentially you can rank all the documents using your have a ranker",
  "tokens": [50368, 407, 4476, 291, 393, 6181, 439, 264, 8512, 1228, 428, 362, 257,
  6181, 260, 50532], "temperature": 0.0, "avg_logprob": -0.2939552990895397, "compression_ratio":
  1.7887931034482758, "no_speech_prob": 0.0010237540118396282}, {"id": 489, "seek":
  456336, "start": 4567.36, "end": 4576.32, "text": " Uh, but uh you cannot it''s
  to like to expensive to do so you can add an n and n is basically for vector search
  uh that is you", "tokens": [50564, 4019, 11, 457, 2232, 291, 2644, 309, 311, 281,
  411, 281, 5124, 281, 360, 370, 291, 393, 909, 364, 297, 293, 297, 307, 1936, 337,
  8062, 3164, 2232, 300, 307, 291, 51012], "temperature": 0.0, "avg_logprob": -0.2939552990895397,
  "compression_ratio": 1.7887931034482758, "no_speech_prob": 0.0010237540118396282},
  {"id": 490, "seek": 456336, "start": 4576.4, "end": 4581.28, "text": " Distill everything
  to vectors and you have the same objective and you have like a", "tokens": [51016,
  9840, 373, 1203, 281, 18875, 293, 291, 362, 264, 912, 10024, 293, 291, 362, 411,
  257, 51260], "temperature": 0.0, "avg_logprob": -0.2939552990895397, "compression_ratio":
  1.7887931034482758, "no_speech_prob": 0.0010237540118396282}, {"id": 491, "seek":
  456336, "start": 4582.88, "end": 4584.88, "text": " Like a way to", "tokens": [51340,
  1743, 257, 636, 281, 51440], "temperature": 0.0, "avg_logprob": -0.2939552990895397,
  "compression_ratio": 1.7887931034482758, "no_speech_prob": 0.0010237540118396282},
  {"id": 492, "seek": 456336, "start": 4584.88, "end": 4587.36, "text": " Sparsify
  the interactions", "tokens": [51440, 1738, 685, 2505, 264, 13280, 51564], "temperature":
  0.0, "avg_logprob": -0.2939552990895397, "compression_ratio": 1.7887931034482758,
  "no_speech_prob": 0.0010237540118396282}, {"id": 493, "seek": 456336, "start": 4588.24,
  "end": 4593.28, "text": " Uh, but you can look about the other way so you know you
  have a graph and the graph are just the", "tokens": [51608, 4019, 11, 457, 291,
  393, 574, 466, 264, 661, 636, 370, 291, 458, 291, 362, 257, 4295, 293, 264, 4295,
  366, 445, 264, 51860], "temperature": 0.0, "avg_logprob": -0.2939552990895397, "compression_ratio":
  1.7887931034482758, "no_speech_prob": 0.0010237540118396282}, {"id": 494, "seek":
  459336, "start": 4593.44, "end": 4597.839999999999, "text": " Candidates and you
  have like a low simple metric now you have", "tokens": [50368, 20466, 327, 1024,
  293, 291, 362, 411, 257, 2295, 2199, 20678, 586, 291, 362, 50588], "temperature":
  0.0, "avg_logprob": -0.26624090592939775, "compression_ratio": 1.7783251231527093,
  "no_speech_prob": 0.00101264170370996}, {"id": 495, "seek": 459336, "start": 4598.5599999999995,
  "end": 4604.639999999999, "text": " More complicated metric on this graph and you
  have like a final ranking that also can be searched on this graph", "tokens": [50624,
  5048, 6179, 20678, 322, 341, 4295, 293, 291, 362, 411, 257, 2572, 17833, 300, 611,
  393, 312, 22961, 322, 341, 4295, 50928], "temperature": 0.0, "avg_logprob": -0.26624090592939775,
  "compression_ratio": 1.7783251231527093, "no_speech_prob": 0.00101264170370996},
  {"id": 496, "seek": 459336, "start": 4605.5199999999995, "end": 4607.5199999999995,
  "text": " So that means you don''t supply", "tokens": [50972, 407, 300, 1355, 291,
  500, 380, 5847, 51072], "temperature": 0.0, "avg_logprob": -0.26624090592939775,
  "compression_ratio": 1.7783251231527093, "no_speech_prob": 0.00101264170370996},
  {"id": 497, "seek": 459336, "start": 4608.32, "end": 4612.799999999999, "text":
  " Like a set of candidates to the ranking, but rather you supply interpoints in
  the graphs", "tokens": [51112, 1743, 257, 992, 295, 11255, 281, 264, 17833, 11,
  457, 2831, 291, 5847, 728, 20552, 294, 264, 24877, 51336], "temperature": 0.0, "avg_logprob":
  -0.26624090592939775, "compression_ratio": 1.7783251231527093, "no_speech_prob":
  0.00101264170370996}, {"id": 498, "seek": 459336, "start": 4613.28, "end": 4615.679999999999,
  "text": " So you have a graph which is uh, well", "tokens": [51360, 407, 291, 362,
  257, 4295, 597, 307, 2232, 11, 731, 51480], "temperature": 0.0, "avg_logprob": -0.26624090592939775,
  "compression_ratio": 1.7783251231527093, "no_speech_prob": 0.00101264170370996},
  {"id": 499, "seek": 459336, "start": 4616.639999999999, "end": 4619.2, "text": "
  Which is built a trying to uh", "tokens": [51528, 3013, 307, 3094, 257, 1382, 281,
  2232, 51656], "temperature": 0.0, "avg_logprob": -0.26624090592939775, "compression_ratio":
  1.7783251231527093, "no_speech_prob": 0.00101264170370996}, {"id": 500, "seek":
  461920, "start": 4619.28, "end": 4621.28, "text": " uh", "tokens": [50368, 2232,
  50468], "temperature": 0.0, "avg_logprob": -0.2878838309758826, "compression_ratio":
  1.634517766497462, "no_speech_prob": 0.0012936722487211227}, {"id": 501, "seek":
  461920, "start": 4621.28, "end": 4623.28, "text": " Capture the uh", "tokens": [50468,
  9480, 540, 264, 2232, 50568], "temperature": 0.0, "avg_logprob": -0.2878838309758826,
  "compression_ratio": 1.634517766497462, "no_speech_prob": 0.0012936722487211227},
  {"id": 502, "seek": 461920, "start": 4623.28, "end": 4630.48, "text": " similarity
  for the ranker and uh like when you so instead of filtering like from one stage
  to the next stage", "tokens": [50568, 32194, 337, 264, 6181, 260, 293, 2232, 411,
  562, 291, 370, 2602, 295, 30822, 411, 490, 472, 3233, 281, 264, 958, 3233, 50928],
  "temperature": 0.0, "avg_logprob": -0.2878838309758826, "compression_ratio": 1.634517766497462,
  "no_speech_prob": 0.0012936722487211227}, {"id": 503, "seek": 461920, "start": 4630.639999999999,
  "end": 4639.12, "text": " You can uh just switch the metric in the graph. You had
  light metric, which is like vectors now you have more complicated metrics", "tokens":
  [50936, 509, 393, 2232, 445, 3679, 264, 20678, 294, 264, 4295, 13, 509, 632, 1442,
  20678, 11, 597, 307, 411, 18875, 586, 291, 362, 544, 6179, 16367, 51360], "temperature":
  0.0, "avg_logprob": -0.2878838309758826, "compression_ratio": 1.634517766497462,
  "no_speech_prob": 0.0012936722487211227}, {"id": 504, "seek": 461920, "start": 4639.12,
  "end": 4642.48, "text": " So you hydrate the features of the elements in the graph
  and like", "tokens": [51360, 407, 291, 5796, 4404, 264, 4122, 295, 264, 4959, 294,
  264, 4295, 293, 411, 51528], "temperature": 0.0, "avg_logprob": -0.2878838309758826,
  "compression_ratio": 1.634517766497462, "no_speech_prob": 0.0012936722487211227},
  {"id": 505, "seek": 464248, "start": 4643.28, "end": 4647.44, "text": " Traverse
  and like now you have a really complicated metric", "tokens": [50404, 5403, 4308,
  293, 411, 586, 291, 362, 257, 534, 6179, 20678, 50612], "temperature": 0.0, "avg_logprob":
  -0.27549139022827146, "compression_ratio": 1.6583333333333334, "no_speech_prob":
  0.0034101265482604504}, {"id": 506, "seek": 464248, "start": 4648.08, "end": 4654.639999999999,
  "text": " Which yeah, like you just very heavy, but you still you just have an interpoint
  in the graph. So you explore it and you can", "tokens": [50644, 3013, 1338, 11,
  411, 291, 445, 588, 4676, 11, 457, 291, 920, 291, 445, 362, 364, 728, 6053, 294,
  264, 4295, 13, 407, 291, 6839, 309, 293, 291, 393, 50972], "temperature": 0.0, "avg_logprob":
  -0.27549139022827146, "compression_ratio": 1.6583333333333334, "no_speech_prob":
  0.0034101265482604504}, {"id": 507, "seek": 464248, "start": 4655.44, "end": 4662.16,
  "text": " Uh, well, you can fix some mistakes done by the previous layers. Yeah,
  so it''s not exact filtering. So that''s yeah, that''s another like", "tokens":
  [51012, 4019, 11, 731, 11, 291, 393, 3191, 512, 8038, 1096, 538, 264, 3894, 7914,
  13, 865, 11, 370, 309, 311, 406, 1900, 30822, 13, 407, 300, 311, 1338, 11, 300,
  311, 1071, 411, 51348], "temperature": 0.0, "avg_logprob": -0.27549139022827146,
  "compression_ratio": 1.6583333333333334, "no_speech_prob": 0.0034101265482604504},
  {"id": 508, "seek": 464248, "start": 4663.36, "end": 4665.36, "text": " Maybe unique",
  "tokens": [51408, 2704, 3845, 51508], "temperature": 0.0, "avg_logprob": -0.27549139022827146,
  "compression_ratio": 1.6583333333333334, "no_speech_prob": 0.0034101265482604504},
  {"id": 509, "seek": 464248, "start": 4665.36, "end": 4668.4, "text": " The feature
  of the graph methods. Yeah, sounds quite exciting like", "tokens": [51508, 440,
  4111, 295, 264, 4295, 7150, 13, 865, 11, 3263, 1596, 4670, 411, 51660], "temperature":
  0.0, "avg_logprob": -0.27549139022827146, "compression_ratio": 1.6583333333333334,
  "no_speech_prob": 0.0034101265482604504}, {"id": 510, "seek": 466840, "start": 4668.879999999999,
  "end": 4674.48, "text": " Have you have you thought about publishing this idea or
  like I mean it sounds quite quite unique", "tokens": [50388, 3560, 291, 362, 291,
  1194, 466, 17832, 341, 1558, 420, 411, 286, 914, 309, 3263, 1596, 1596, 3845, 50668],
  "temperature": 0.0, "avg_logprob": -0.2381882115414268, "compression_ratio": 1.6598360655737705,
  "no_speech_prob": 0.001674604951404035}, {"id": 511, "seek": 466840, "start": 4675.839999999999,
  "end": 4679.28, "text": " Well, it doesn''t make sense to publish an idea without
  implementation", "tokens": [50736, 1042, 11, 309, 1177, 380, 652, 2020, 281, 11374,
  364, 1558, 1553, 11420, 50908], "temperature": 0.0, "avg_logprob": -0.2381882115414268,
  "compression_ratio": 1.6598360655737705, "no_speech_prob": 0.001674604951404035},
  {"id": 512, "seek": 466840, "start": 4679.599999999999, "end": 4684.08, "text":
  " Yeah, for sure, but maybe you can influence those who who would like to", "tokens":
  [50924, 865, 11, 337, 988, 11, 457, 1310, 291, 393, 6503, 729, 567, 567, 576, 411,
  281, 51148], "temperature": 0.0, "avg_logprob": -0.2381882115414268, "compression_ratio":
  1.6598360655737705, "no_speech_prob": 0.001674604951404035}, {"id": 513, "seek":
  466840, "start": 4685.44, "end": 4687.28, "text": " Experiment on it", "tokens":
  [51216, 37933, 322, 309, 51308], "temperature": 0.0, "avg_logprob": -0.2381882115414268,
  "compression_ratio": 1.6598360655737705, "no_speech_prob": 0.001674604951404035},
  {"id": 514, "seek": 466840, "start": 4687.28, "end": 4692.96, "text": " At least
  those who will watch this podcast. I think they will listen. They will they will
  probably pick it up", "tokens": [51308, 1711, 1935, 729, 567, 486, 1159, 341, 7367,
  13, 286, 519, 436, 486, 2140, 13, 814, 486, 436, 486, 1391, 1888, 309, 493, 51592],
  "temperature": 0.0, "avg_logprob": -0.2381882115414268, "compression_ratio": 1.6598360655737705,
  "no_speech_prob": 0.001674604951404035}, {"id": 515, "seek": 466840, "start": 4694.0,
  "end": 4696.0, "text": " Yeah, and use graph algorithms for sure", "tokens": [51644,
  865, 11, 293, 764, 4295, 14642, 337, 988, 51744], "temperature": 0.0, "avg_logprob":
  -0.2381882115414268, "compression_ratio": 1.6598360655737705, "no_speech_prob":
  0.001674604951404035}, {"id": 516, "seek": 469600, "start": 4696.0, "end": 4698.0,
  "text": " Like", "tokens": [50364, 1743, 50464], "temperature": 0.0, "avg_logprob":
  -0.28791150381398756, "compression_ratio": 1.6220095693779903, "no_speech_prob":
  0.0030487084295600653}, {"id": 517, "seek": 469600, "start": 4698.0, "end": 4701.68,
  "text": " Yeah, I mean it sounds like all all of the NN algorithms they have", "tokens":
  [50464, 865, 11, 286, 914, 309, 3263, 411, 439, 439, 295, 264, 426, 45, 14642, 436,
  362, 50648], "temperature": 0.0, "avg_logprob": -0.28791150381398756, "compression_ratio":
  1.6220095693779903, "no_speech_prob": 0.0030487084295600653}, {"id": 518, "seek":
  469600, "start": 4702.72, "end": 4707.6, "text": " Like advantages and disadvantages,
  right? So it''s not like the all of them are uniquely", "tokens": [50700, 1743,
  14906, 293, 37431, 11, 558, 30, 407, 309, 311, 406, 411, 264, 439, 295, 552, 366,
  31474, 50944], "temperature": 0.0, "avg_logprob": -0.28791150381398756, "compression_ratio":
  1.6220095693779903, "no_speech_prob": 0.0030487084295600653}, {"id": 519, "seek":
  469600, "start": 4709.12, "end": 4711.12, "text": " Outperforming, you know the
  others", "tokens": [51020, 5925, 26765, 278, 11, 291, 458, 264, 2357, 51120], "temperature":
  0.0, "avg_logprob": -0.28791150381398756, "compression_ratio": 1.6220095693779903,
  "no_speech_prob": 0.0030487084295600653}, {"id": 520, "seek": 469600, "start": 4712.24,
  "end": 4720.0, "text": " Well, there is like a division like if you think about
  like quantization algorithms. So they are kind of orthogonal to", "tokens": [51176,
  1042, 11, 456, 307, 411, 257, 10044, 411, 498, 291, 519, 466, 411, 4426, 2144, 14642,
  13, 407, 436, 366, 733, 295, 41488, 281, 51564], "temperature": 0.0, "avg_logprob":
  -0.28791150381398756, "compression_ratio": 1.6220095693779903, "no_speech_prob":
  0.0030487084295600653}, {"id": 521, "seek": 469600, "start": 4721.04, "end": 4723.04,
  "text": " Graph algorithms. So they", "tokens": [51616, 21884, 14642, 13, 407, 436,
  51716], "temperature": 0.0, "avg_logprob": -0.28791150381398756, "compression_ratio":
  1.6220095693779903, "no_speech_prob": 0.0030487084295600653}, {"id": 522, "seek":
  472304, "start": 4723.44, "end": 4729.68, "text": " They quantize so they can speed
  up a compressed like I''m compressed to save the memory and speed up the computation",
  "tokens": [50384, 814, 4426, 1125, 370, 436, 393, 3073, 493, 257, 30353, 411, 286,
  478, 30353, 281, 3155, 264, 4675, 293, 3073, 493, 264, 24903, 50696], "temperature":
  0.0, "avg_logprob": -0.2789344178869369, "compression_ratio": 1.6923076923076923,
  "no_speech_prob": 0.0017961168196052313}, {"id": 523, "seek": 472304, "start": 4730.72,
  "end": 4735.12, "text": " But like older algorithm they just use something like
  IVF. So", "tokens": [50748, 583, 411, 4906, 9284, 436, 445, 764, 746, 411, 15967,
  37, 13, 407, 50968], "temperature": 0.0, "avg_logprob": -0.2789344178869369, "compression_ratio":
  1.6923076923076923, "no_speech_prob": 0.0017961168196052313}, {"id": 524, "seek":
  472304, "start": 4735.76, "end": 4741.2, "text": " And then like one layer filtering
  and you can use graphs instead of IVF", "tokens": [51000, 400, 550, 411, 472, 4583,
  30822, 293, 291, 393, 764, 24877, 2602, 295, 15967, 37, 51272], "temperature": 0.0,
  "avg_logprob": -0.2789344178869369, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.0017961168196052313}, {"id": 525, "seek": 472304, "start": 4741.68, "end": 4746.32,
  "text": " Right, so we can use graphs and add the quantization and at the Faiz did
  that", "tokens": [51296, 1779, 11, 370, 321, 393, 764, 24877, 293, 909, 264, 4426,
  2144, 293, 412, 264, 12710, 590, 630, 300, 51528], "temperature": 0.0, "avg_logprob":
  -0.2789344178869369, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.0017961168196052313}, {"id": 526, "seek": 472304, "start": 4747.04, "end": 4748.24,
  "text": " before", "tokens": [51564, 949, 51624], "temperature": 0.0, "avg_logprob":
  -0.2789344178869369, "compression_ratio": 1.6923076923076923, "no_speech_prob":
  0.0017961168196052313}, {"id": 527, "seek": 472304, "start": 4748.24, "end": 4750.96,
  "text": " Yeah, I think some others also did that", "tokens": [51624, 865, 11, 286,
  519, 512, 2357, 611, 630, 300, 51760], "temperature": 0.0, "avg_logprob": -0.2789344178869369,
  "compression_ratio": 1.6923076923076923, "no_speech_prob": 0.0017961168196052313},
  {"id": 528, "seek": 475096, "start": 4751.6, "end": 4756.08, "text": " Yeah, and
  the thing and then like vector databases actually offer it as one method like like",
  "tokens": [50396, 865, 11, 293, 264, 551, 293, 550, 411, 8062, 22380, 767, 2626,
  309, 382, 472, 3170, 411, 411, 50620], "temperature": 0.0, "avg_logprob": -0.20382654868950278,
  "compression_ratio": 1.6748251748251748, "no_speech_prob": 0.0015540739987045527},
  {"id": 529, "seek": 475096, "start": 4756.72, "end": 4763.76, "text": " Milvus for
  example like they offer IVF and then you can choose like if you want to do exact
  K&N or if you want to do A&N", "tokens": [50652, 7036, 85, 301, 337, 1365, 411,
  436, 2626, 15967, 37, 293, 550, 291, 393, 2826, 411, 498, 291, 528, 281, 360, 1900,
  591, 5, 45, 420, 498, 291, 528, 281, 360, 316, 5, 45, 51004], "temperature": 0.0,
  "avg_logprob": -0.20382654868950278, "compression_ratio": 1.6748251748251748, "no_speech_prob":
  0.0015540739987045527}, {"id": 530, "seek": 475096, "start": 4764.32, "end": 4766.8,
  "text": " So you can actually configure it in different ways", "tokens": [51032,
  407, 291, 393, 767, 22162, 309, 294, 819, 2098, 51156], "temperature": 0.0, "avg_logprob":
  -0.20382654868950278, "compression_ratio": 1.6748251748251748, "no_speech_prob":
  0.0015540739987045527}, {"id": 531, "seek": 475096, "start": 4768.0, "end": 4770.4,
  "text": " Yeah, I mean just sounds like you''re", "tokens": [51216, 865, 11, 286,
  914, 445, 3263, 411, 291, 434, 51336], "temperature": 0.0, "avg_logprob": -0.20382654868950278,
  "compression_ratio": 1.6748251748251748, "no_speech_prob": 0.0015540739987045527},
  {"id": 532, "seek": 475096, "start": 4771.2, "end": 4777.04, "text": " Without maybe
  realizing much like you are at the core of what''s happening in vector search in
  some sense", "tokens": [51376, 9129, 1310, 16734, 709, 411, 291, 366, 412, 264,
  4965, 295, 437, 311, 2737, 294, 8062, 3164, 294, 512, 2020, 51668], "temperature":
  0.0, "avg_logprob": -0.20382654868950278, "compression_ratio": 1.6748251748251748,
  "no_speech_prob": 0.0015540739987045527}, {"id": 533, "seek": 475096, "start": 4777.52,
  "end": 4780.4, "text": " Of course, there have been other multiple contributions,
  right? But like", "tokens": [51692, 2720, 1164, 11, 456, 362, 668, 661, 3866, 15725,
  11, 558, 30, 583, 411, 51836], "temperature": 0.0, "avg_logprob": -0.20382654868950278,
  "compression_ratio": 1.6748251748251748, "no_speech_prob": 0.0015540739987045527},
  {"id": 534, "seek": 478040, "start": 4780.799999999999, "end": 4785.28, "text":
  " For some reason exactly your algorithm has been picked by many vector databases",
  "tokens": [50384, 1171, 512, 1778, 2293, 428, 9284, 575, 668, 6183, 538, 867, 8062,
  22380, 50608], "temperature": 0.0, "avg_logprob": -0.18953146683542352, "compression_ratio":
  1.6857142857142857, "no_speech_prob": 0.000993597786873579}, {"id": 535, "seek":
  478040, "start": 4785.36, "end": 4788.0, "text": " There are like seven of them.
  So actually wrote a blog about", "tokens": [50612, 821, 366, 411, 3407, 295, 552,
  13, 407, 767, 4114, 257, 6968, 466, 50744], "temperature": 0.0, "avg_logprob": -0.18953146683542352,
  "compression_ratio": 1.6857142857142857, "no_speech_prob": 0.000993597786873579},
  {"id": 536, "seek": 478040, "start": 4788.719999999999, "end": 4793.2, "text": "
  Six of them and then seventh kind of knocked on my door and said can you also add
  at us", "tokens": [50780, 11678, 295, 552, 293, 550, 17875, 733, 295, 16914, 322,
  452, 2853, 293, 848, 393, 291, 611, 909, 412, 505, 51004], "temperature": 0.0, "avg_logprob":
  -0.18953146683542352, "compression_ratio": 1.6857142857142857, "no_speech_prob":
  0.000993597786873579}, {"id": 537, "seek": 478040, "start": 4794.5599999999995,
  "end": 4803.12, "text": " And so when I when I was going through different databases
  like in Java implemented in Java or in in Python or you know in Rust and go", "tokens":
  [51072, 400, 370, 562, 286, 562, 286, 390, 516, 807, 819, 22380, 411, 294, 10745,
  12270, 294, 10745, 420, 294, 294, 15329, 420, 291, 458, 294, 34952, 293, 352, 51500],
  "temperature": 0.0, "avg_logprob": -0.18953146683542352, "compression_ratio": 1.6857142857142857,
  "no_speech_prob": 0.000993597786873579}, {"id": 538, "seek": 478040, "start": 4803.599999999999,
  "end": 4806.4, "text": " All of them picked your algorithm for some reason", "tokens":
  [51524, 1057, 295, 552, 6183, 428, 9284, 337, 512, 1778, 51664], "temperature":
  0.0, "avg_logprob": -0.18953146683542352, "compression_ratio": 1.6857142857142857,
  "no_speech_prob": 0.000993597786873579}, {"id": 539, "seek": 480640, "start": 4807.36,
  "end": 4819.44, "text": " So like maybe it was easier like it''s a combination of
  how easy it is to implement how transparent it is like to understand right and then
  basically it''s stability. So it''s like a combination of things", "tokens": [50412,
  407, 411, 1310, 309, 390, 3571, 411, 309, 311, 257, 6562, 295, 577, 1858, 309, 307,
  281, 4445, 577, 12737, 309, 307, 411, 281, 1223, 558, 293, 550, 1936, 309, 311,
  11826, 13, 407, 309, 311, 411, 257, 6562, 295, 721, 51016], "temperature": 0.0,
  "avg_logprob": -0.1975628266851586, "compression_ratio": 1.7320574162679425, "no_speech_prob":
  0.0028562198858708143}, {"id": 540, "seek": 480640, "start": 4822.24, "end": 4825.679999999999,
  "text": " Yeah, probably like I''m not totally sure", "tokens": [51156, 865, 11,
  1391, 411, 286, 478, 406, 3879, 988, 51328], "temperature": 0.0, "avg_logprob":
  -0.1975628266851586, "compression_ratio": 1.7320574162679425, "no_speech_prob":
  0.0028562198858708143}, {"id": 541, "seek": 480640, "start": 4826.32, "end": 4834.08,
  "text": " So yeah, the initial library also was implemented as a header on the well,
  not the initial so that was a second library", "tokens": [51360, 407, 1338, 11,
  264, 5883, 6405, 611, 390, 12270, 382, 257, 23117, 322, 264, 731, 11, 406, 264,
  5883, 370, 300, 390, 257, 1150, 6405, 51748], "temperature": 0.0, "avg_logprob":
  -0.1975628266851586, "compression_ratio": 1.7320574162679425, "no_speech_prob":
  0.0028562198858708143}, {"id": 542, "seek": 483408, "start": 4834.72, "end": 4840.24,
  "text": " So there there was a problem with HNW lippen implementation and NMS lip",
  "tokens": [50396, 407, 456, 456, 390, 257, 1154, 365, 389, 45, 54, 375, 21278, 11420,
  293, 426, 10288, 8280, 50672], "temperature": 0.0, "avg_logprob": -0.4676639513037671,
  "compression_ratio": 1.6116504854368932, "no_speech_prob": 0.0030006265733391047},
  {"id": 543, "seek": 483408, "start": 4840.8, "end": 4845.04, "text": " So it so
  like the NMS lip format was a bit restrictive", "tokens": [50700, 407, 309, 370,
  411, 264, 426, 10288, 8280, 7877, 390, 257, 857, 43220, 50912], "temperature": 0.0,
  "avg_logprob": -0.4676639513037671, "compression_ratio": 1.6116504854368932, "no_speech_prob":
  0.0030006265733391047}, {"id": 544, "seek": 483408, "start": 4845.68, "end": 4848.48,
  "text": " Like for efficient operation. So it converted it to", "tokens": [50944,
  1743, 337, 7148, 6916, 13, 407, 309, 16424, 309, 281, 51084], "temperature": 0.0,
  "avg_logprob": -0.4676639513037671, "compression_ratio": 1.6116504854368932, "no_speech_prob":
  0.0030006265733391047}, {"id": 545, "seek": 483408, "start": 4849.76, "end": 4853.28,
  "text": " Flat memory format and so that that", "tokens": [51148, 36172, 4675, 7877,
  293, 370, 300, 300, 51324], "temperature": 0.0, "avg_logprob": -0.4676639513037671,
  "compression_ratio": 1.6116504854368932, "no_speech_prob": 0.0030006265733391047},
  {"id": 546, "seek": 483408, "start": 4854.16, "end": 4860.8, "text": " That makes
  made construction slower and memory can sub-share bigger. So was re-implemented
  as I had a wrongly library", "tokens": [51368, 663, 1669, 1027, 6435, 14009, 293,
  4675, 393, 1422, 12, 2716, 543, 3801, 13, 407, 390, 319, 12, 332, 781, 14684, 382,
  286, 632, 257, 2085, 356, 6405, 51700], "temperature": 0.0, "avg_logprob": -0.4676639513037671,
  "compression_ratio": 1.6116504854368932, "no_speech_prob": 0.0030006265733391047},
  {"id": 547, "seek": 486080, "start": 4861.4400000000005, "end": 4864.0, "text":
  " So header on the library was inspired by an I", "tokens": [50396, 407, 23117,
  322, 264, 6405, 390, 7547, 538, 364, 286, 50524], "temperature": 0.0, "avg_logprob":
  -0.2919126465207055, "compression_ratio": 1.6122448979591837, "no_speech_prob":
  0.0021126149222254753}, {"id": 548, "seek": 486080, "start": 4864.56, "end": 4867.12,
  "text": " So like by the success also and I", "tokens": [50552, 407, 411, 538, 264,
  2245, 611, 293, 286, 50680], "temperature": 0.0, "avg_logprob": -0.2919126465207055,
  "compression_ratio": 1.6122448979591837, "no_speech_prob": 0.0021126149222254753},
  {"id": 549, "seek": 486080, "start": 4868.24, "end": 4872.72, "text": " Think that
  also might have contributed because it''s very easy to like integrate it", "tokens":
  [50736, 6557, 300, 611, 1062, 362, 18434, 570, 309, 311, 588, 1858, 281, 411, 13365,
  309, 50960], "temperature": 0.0, "avg_logprob": -0.2919126465207055, "compression_ratio":
  1.6122448979591837, "no_speech_prob": 0.0021126149222254753}, {"id": 550, "seek":
  486080, "start": 4873.52, "end": 4876.8, "text": " So there are a few files it compiles
  in some seconds", "tokens": [51000, 407, 456, 366, 257, 1326, 7098, 309, 715, 4680,
  294, 512, 3949, 51164], "temperature": 0.0, "avg_logprob": -0.2919126465207055,
  "compression_ratio": 1.6122448979591837, "no_speech_prob": 0.0021126149222254753},
  {"id": 551, "seek": 486080, "start": 4878.16, "end": 4879.6, "text": " Yeah, no",
  "tokens": [51232, 865, 11, 572, 51304], "temperature": 0.0, "avg_logprob": -0.2919126465207055,
  "compression_ratio": 1.6122448979591837, "no_speech_prob": 0.0021126149222254753},
  {"id": 552, "seek": 486080, "start": 4879.6, "end": 4881.6, "text": " Maybe maybe
  also that help", "tokens": [51304, 2704, 1310, 611, 300, 854, 51404], "temperature":
  0.0, "avg_logprob": -0.2919126465207055, "compression_ratio": 1.6122448979591837,
  "no_speech_prob": 0.0021126149222254753}, {"id": 553, "seek": 486080, "start": 4881.6,
  "end": 4884.56, "text": " So the library itself is simple and easy to integrate",
  "tokens": [51404, 407, 264, 6405, 2564, 307, 2199, 293, 1858, 281, 13365, 51552],
  "temperature": 0.0, "avg_logprob": -0.2919126465207055, "compression_ratio": 1.6122448979591837,
  "no_speech_prob": 0.0021126149222254753}, {"id": 554, "seek": 486080, "start": 4885.28,
  "end": 4886.96, "text": " Yeah, yeah", "tokens": [51588, 865, 11, 1338, 51672],
  "temperature": 0.0, "avg_logprob": -0.2919126465207055, "compression_ratio": 1.6122448979591837,
  "no_speech_prob": 0.0021126149222254753}, {"id": 555, "seek": 488696, "start": 4887.12,
  "end": 4891.12, "text": " And I mean it must feel kind of cool to have this impact",
  "tokens": [50372, 400, 286, 914, 309, 1633, 841, 733, 295, 1627, 281, 362, 341,
  2712, 50572], "temperature": 0.0, "avg_logprob": -0.20754295587539673, "compression_ratio":
  1.6333333333333333, "no_speech_prob": 0.00152643583714962}, {"id": 556, "seek":
  488696, "start": 4891.52, "end": 4895.12, "text": " But but I also I also hope like
  you you will continue kind of", "tokens": [50592, 583, 457, 286, 611, 286, 611,
  1454, 411, 291, 291, 486, 2354, 733, 295, 50772], "temperature": 0.0, "avg_logprob":
  -0.20754295587539673, "compression_ratio": 1.6333333333333333, "no_speech_prob":
  0.00152643583714962}, {"id": 557, "seek": 488696, "start": 4895.84, "end": 4901.2,
  "text": " Maybe doing some publishable publishable work in some fashion and doesn''t
  need to be a journal", "tokens": [50808, 2704, 884, 512, 11374, 712, 11374, 712,
  589, 294, 512, 6700, 293, 1177, 380, 643, 281, 312, 257, 6708, 51076], "temperature":
  0.0, "avg_logprob": -0.20754295587539673, "compression_ratio": 1.6333333333333333,
  "no_speech_prob": 0.00152643583714962}, {"id": 558, "seek": 488696, "start": 4901.2,
  "end": 4903.84, "text": " Which is rejected five times but something else", "tokens":
  [51076, 3013, 307, 15749, 1732, 1413, 457, 746, 1646, 51208], "temperature": 0.0,
  "avg_logprob": -0.20754295587539673, "compression_ratio": 1.6333333333333333, "no_speech_prob":
  0.00152643583714962}, {"id": 559, "seek": 488696, "start": 4904.56, "end": 4906.72,
  "text": " Is this something that you are planning to do or", "tokens": [51244, 1119,
  341, 746, 300, 291, 366, 5038, 281, 360, 420, 51352], "temperature": 0.0, "avg_logprob":
  -0.20754295587539673, "compression_ratio": 1.6333333333333333, "no_speech_prob":
  0.00152643583714962}, {"id": 560, "seek": 488696, "start": 4909.6, "end": 4915.2,
  "text": " Uh, well that depends so like I cannot talk too much about my work in
  Twitter. So", "tokens": [51496, 4019, 11, 731, 300, 5946, 370, 411, 286, 2644, 751,
  886, 709, 466, 452, 589, 294, 5794, 13, 407, 51776], "temperature": 0.0, "avg_logprob":
  -0.20754295587539673, "compression_ratio": 1.6333333333333333, "no_speech_prob":
  0.00152643583714962}, {"id": 561, "seek": 491696, "start": 4917.52, "end": 4919.52,
  "text": " So", "tokens": [50392, 407, 50492], "temperature": 0.0, "avg_logprob":
  -0.37414201100667316, "compression_ratio": 1.5507246376811594, "no_speech_prob":
  0.0019481817726045847}, {"id": 562, "seek": 491696, "start": 4920.32, "end": 4929.68,
  "text": " Maybe maybe we will publish something so that that depends on how it goes.
  I mean, I''m near even nearest neighbors. Yeah, not not only but yeah", "tokens":
  [50532, 2704, 1310, 321, 486, 11374, 746, 370, 300, 300, 5946, 322, 577, 309, 1709,
  13, 286, 914, 11, 286, 478, 2651, 754, 23831, 12512, 13, 865, 11, 406, 406, 787,
  457, 1338, 51000], "temperature": 0.0, "avg_logprob": -0.37414201100667316, "compression_ratio":
  1.5507246376811594, "no_speech_prob": 0.0019481817726045847}, {"id": 563, "seek":
  491696, "start": 4931.44, "end": 4935.44, "text": " But I it''s hard to predict
  now if it works well", "tokens": [51088, 583, 286, 309, 311, 1152, 281, 6069, 586,
  498, 309, 1985, 731, 51288], "temperature": 0.0, "avg_logprob": -0.37414201100667316,
  "compression_ratio": 1.5507246376811594, "no_speech_prob": 0.0019481817726045847},
  {"id": 564, "seek": 491696, "start": 4936.16, "end": 4943.92, "text": " So that
  then publish yeah, at least the idea that you mentioned like I mean if you if it''s
  outside Twitter for example in hnsw", "tokens": [51324, 407, 300, 550, 11374, 1338,
  11, 412, 1935, 264, 1558, 300, 291, 2835, 411, 286, 914, 498, 291, 498, 309, 311,
  2380, 5794, 337, 1365, 294, 276, 3695, 86, 51712], "temperature": 0.0, "avg_logprob":
  -0.37414201100667316, "compression_ratio": 1.5507246376811594, "no_speech_prob":
  0.0019481817726045847}, {"id": 565, "seek": 494392, "start": 4943.92, "end": 4948.24,
  "text": " Your library like the idea of this multistage ranking sounds quite exciting",
  "tokens": [50364, 2260, 6405, 411, 264, 1558, 295, 341, 2120, 468, 609, 17833, 3263,
  1596, 4670, 50580], "temperature": 0.0, "avg_logprob": -0.34343172429682134, "compression_ratio":
  1.7242990654205608, "no_speech_prob": 0.020026100799441338}, {"id": 566, "seek":
  494392, "start": 4948.96, "end": 4956.4800000000005, "text": " Um, uh, well, I think
  it can be implemented only by the teams who own the rankers and all the whole pipeline",
  "tokens": [50616, 3301, 11, 2232, 11, 731, 11, 286, 519, 309, 393, 312, 12270, 787,
  538, 264, 5491, 567, 1065, 264, 6181, 433, 293, 439, 264, 1379, 15517, 50992], "temperature":
  0.0, "avg_logprob": -0.34343172429682134, "compression_ratio": 1.7242990654205608,
  "no_speech_prob": 0.020026100799441338}, {"id": 567, "seek": 494392, "start": 4956.96,
  "end": 4960.24, "text": " Yes, true. I think it can be implemented as like", "tokens":
  [51016, 1079, 11, 2074, 13, 286, 519, 309, 393, 312, 12270, 382, 411, 51180], "temperature":
  0.0, "avg_logprob": -0.34343172429682134, "compression_ratio": 1.7242990654205608,
  "no_speech_prob": 0.020026100799441338}, {"id": 568, "seek": 494392, "start": 4961.2,
  "end": 4969.28, "text": " As I think you need to hide ha you need to hydrate the
  features and like yeah on the fly and have feature hydration is very specific to",
  "tokens": [51228, 1018, 286, 519, 291, 643, 281, 6479, 324, 291, 643, 281, 5796,
  4404, 264, 4122, 293, 411, 1338, 322, 264, 3603, 293, 362, 4111, 43631, 307, 588,
  2685, 281, 51632], "temperature": 0.0, "avg_logprob": -0.34343172429682134, "compression_ratio":
  1.7242990654205608, "no_speech_prob": 0.020026100799441338}, {"id": 569, "seek":
  496928, "start": 4969.84, "end": 4971.04, "text": " application", "tokens": [50392,
  3861, 50452], "temperature": 0.0, "avg_logprob": -0.22211335834703946, "compression_ratio":
  1.5893719806763285, "no_speech_prob": 0.0044957296922802925}, {"id": 570, "seek":
  496928, "start": 4971.04, "end": 4973.759999999999, "text": " Yeah, but not only
  inside the production environment", "tokens": [50452, 865, 11, 457, 406, 787, 1854,
  264, 4265, 2823, 50588], "temperature": 0.0, "avg_logprob": -0.22211335834703946,
  "compression_ratio": 1.5893719806763285, "no_speech_prob": 0.0044957296922802925},
  {"id": 571, "seek": 496928, "start": 4974.32, "end": 4984.719999999999, "text":
  " Yeah, that makes sense. Yeah, uh, so maybe it will call for creation of data sets
  and kind of this benchmarks if the industry chooses to move in that direction",
  "tokens": [50616, 865, 11, 300, 1669, 2020, 13, 865, 11, 2232, 11, 370, 1310, 309,
  486, 818, 337, 8016, 295, 1412, 6352, 293, 733, 295, 341, 43751, 498, 264, 3518,
  25963, 281, 1286, 294, 300, 3513, 51136], "temperature": 0.0, "avg_logprob": -0.22211335834703946,
  "compression_ratio": 1.5893719806763285, "no_speech_prob": 0.0044957296922802925},
  {"id": 572, "seek": 496928, "start": 4986.16, "end": 4990.5599999999995, "text":
  " Well, like there are some obvious problems with data privacy", "tokens": [51208,
  1042, 11, 411, 456, 366, 512, 6322, 2740, 365, 1412, 11427, 51428], "temperature":
  0.0, "avg_logprob": -0.22211335834703946, "compression_ratio": 1.5893719806763285,
  "no_speech_prob": 0.0044957296922802925}, {"id": 573, "seek": 496928, "start": 4991.44,
  "end": 4994.24, "text": " With that so it''s hard to publish something", "tokens":
  [51472, 2022, 300, 370, 309, 311, 1152, 281, 11374, 746, 51612], "temperature":
  0.0, "avg_logprob": -0.22211335834703946, "compression_ratio": 1.5893719806763285,
  "no_speech_prob": 0.0044957296922802925}, {"id": 574, "seek": 499424, "start": 4994.96,
  "end": 5003.04, "text": " Well, you can think of a toy problem. So like you have
  like you don''t do actual like work with users, but maybe", "tokens": [50400, 1042,
  11, 291, 393, 519, 295, 257, 12058, 1154, 13, 407, 411, 291, 362, 411, 291, 500,
  380, 360, 3539, 411, 589, 365, 5022, 11, 457, 1310, 50804], "temperature": 0.0,
  "avg_logprob": -0.2812381244841076, "compression_ratio": 1.6237113402061856, "no_speech_prob":
  0.0055713895708322525}, {"id": 575, "seek": 499424, "start": 5004.24, "end": 5008.4,
  "text": " We do image to image search and you have like a huge transformer model",
  "tokens": [50864, 492, 360, 3256, 281, 3256, 3164, 293, 291, 362, 411, 257, 2603,
  31782, 2316, 51072], "temperature": 0.0, "avg_logprob": -0.2812381244841076, "compression_ratio":
  1.6237113402061856, "no_speech_prob": 0.0055713895708322525}, {"id": 576, "seek":
  499424, "start": 5009.36, "end": 5012.24, "text": " On top of that or maybe like
  something like marco", "tokens": [51120, 1282, 1192, 295, 300, 420, 1310, 411, 746,
  411, 1849, 1291, 51264], "temperature": 0.0, "avg_logprob": -0.2812381244841076,
  "compression_ratio": 1.6237113402061856, "no_speech_prob": 0.0055713895708322525},
  {"id": 577, "seek": 499424, "start": 5012.719999999999, "end": 5016.88, "text":
  " Emma smart car maybe it can be done with that like experimented", "tokens": [51288,
  17124, 4069, 1032, 1310, 309, 393, 312, 1096, 365, 300, 411, 5120, 292, 51496],
  "temperature": 0.0, "avg_logprob": -0.2812381244841076, "compression_ratio": 1.6237113402061856,
  "no_speech_prob": 0.0055713895708322525}, {"id": 578, "seek": 499424, "start": 5017.76,
  "end": 5019.76, "text": " Hmm, maybe so", "tokens": [51540, 8239, 11, 1310, 370,
  51640], "temperature": 0.0, "avg_logprob": -0.2812381244841076, "compression_ratio":
  1.6237113402061856, "no_speech_prob": 0.0055713895708322525}, {"id": 579, "seek":
  499424, "start": 5020.32, "end": 5021.599999999999, "text": " Yeah", "tokens": [51668,
  865, 51732], "temperature": 0.0, "avg_logprob": -0.2812381244841076, "compression_ratio":
  1.6237113402061856, "no_speech_prob": 0.0055713895708322525}, {"id": 580, "seek":
  502160, "start": 5021.76, "end": 5027.200000000001, "text": " Yeah, I think we weren''t
  really deep today. You really I think it was really really cold cold talking to
  you", "tokens": [50372, 865, 11, 286, 519, 321, 4999, 380, 534, 2452, 965, 13, 509,
  534, 286, 519, 309, 390, 534, 534, 3554, 3554, 1417, 281, 291, 50644], "temperature":
  0.0, "avg_logprob": -0.2723648628492034, "compression_ratio": 1.6556603773584906,
  "no_speech_prob": 0.0013995451154187322}, {"id": 581, "seek": 502160, "start": 5027.4400000000005,
  "end": 5029.6, "text": " I always like to still ask", "tokens": [50656, 286, 1009,
  411, 281, 920, 1029, 50764], "temperature": 0.0, "avg_logprob": -0.2723648628492034,
  "compression_ratio": 1.6556603773584906, "no_speech_prob": 0.0013995451154187322},
  {"id": 582, "seek": 502160, "start": 5030.4800000000005, "end": 5035.6, "text":
  " Kind of this question orthogonal question of why like it''s a little bit more
  philosophical", "tokens": [50808, 9242, 295, 341, 1168, 41488, 1168, 295, 983, 411,
  309, 311, 257, 707, 857, 544, 25066, 51064], "temperature": 0.0, "avg_logprob":
  -0.2723648628492034, "compression_ratio": 1.6556603773584906, "no_speech_prob":
  0.0013995451154187322}, {"id": 583, "seek": 502160, "start": 5035.68, "end": 5037.68,
  "text": " But like if you''re not a verse", "tokens": [51068, 583, 411, 498, 291,
  434, 406, 257, 7996, 51168], "temperature": 0.0, "avg_logprob": -0.2723648628492034,
  "compression_ratio": 1.6556603773584906, "no_speech_prob": 0.0013995451154187322},
  {"id": 584, "seek": 502160, "start": 5038.400000000001, "end": 5040.400000000001,
  "text": " Of philosophy like why", "tokens": [51204, 2720, 10675, 411, 983, 51304],
  "temperature": 0.0, "avg_logprob": -0.2723648628492034, "compression_ratio": 1.6556603773584906,
  "no_speech_prob": 0.0013995451154187322}, {"id": 585, "seek": 502160, "start": 5041.120000000001,
  "end": 5046.72, "text": " Would you say like this field attracted you like in your
  own words?", "tokens": [51340, 6068, 291, 584, 411, 341, 2519, 15912, 291, 411,
  294, 428, 1065, 2283, 30, 51620], "temperature": 0.0, "avg_logprob": -0.2723648628492034,
  "compression_ratio": 1.6556603773584906, "no_speech_prob": 0.0013995451154187322},
  {"id": 586, "seek": 502160, "start": 5048.56, "end": 5050.08, "text": " Uh", "tokens":
  [51712, 4019, 51788], "temperature": 0.0, "avg_logprob": -0.2723648628492034, "compression_ratio":
  1.6556603773584906, "no_speech_prob": 0.0013995451154187322}, {"id": 587, "seek":
  505008, "start": 5050.8, "end": 5053.6, "text": " I didn''t have much choice. It
  just was like I", "tokens": [50400, 286, 994, 380, 362, 709, 3922, 13, 467, 445,
  390, 411, 286, 50540], "temperature": 0.0, "avg_logprob": -0.2576492533964269, "compression_ratio":
  1.658878504672897, "no_speech_prob": 0.0005544802406802773}, {"id": 588, "seek":
  505008, "start": 5054.64, "end": 5057.84, "text": " I got my first job offer and
  that was", "tokens": [50592, 286, 658, 452, 700, 1691, 2626, 293, 300, 390, 50752],
  "temperature": 0.0, "avg_logprob": -0.2576492533964269, "compression_ratio": 1.658878504672897,
  "no_speech_prob": 0.0005544802406802773}, {"id": 589, "seek": 505008, "start": 5059.04,
  "end": 5061.04, "text": " In this field", "tokens": [50812, 682, 341, 2519, 50912],
  "temperature": 0.0, "avg_logprob": -0.2576492533964269, "compression_ratio": 1.658878504672897,
  "no_speech_prob": 0.0005544802406802773}, {"id": 590, "seek": 505008, "start": 5061.76,
  "end": 5070.24, "text": " That''s that''s about scale so like people like scaling
  and like many games when you play on like android or other stuff", "tokens": [50948,
  663, 311, 300, 311, 466, 4373, 370, 411, 561, 411, 21589, 293, 411, 867, 2813, 562,
  291, 862, 322, 411, 36157, 420, 661, 1507, 51372], "temperature": 0.0, "avg_logprob":
  -0.2576492533964269, "compression_ratio": 1.658878504672897, "no_speech_prob": 0.0005544802406802773},
  {"id": 591, "seek": 505008, "start": 5070.24, "end": 5077.84, "text": " They''re
  based on scaling so you do like a little action and there are like huge consequences
  of those actions like destroying something or", "tokens": [51372, 814, 434, 2361,
  322, 21589, 370, 291, 360, 411, 257, 707, 3069, 293, 456, 366, 411, 2603, 10098,
  295, 729, 5909, 411, 19926, 746, 420, 51752], "temperature": 0.0, "avg_logprob":
  -0.2576492533964269, "compression_ratio": 1.658878504672897, "no_speech_prob": 0.0005544802406802773},
  {"id": 592, "seek": 507784, "start": 5078.56, "end": 5080.56, "text": " Like and
  that is scaling and", "tokens": [50400, 1743, 293, 300, 307, 21589, 293, 50500],
  "temperature": 0.0, "avg_logprob": -0.21875047246250537, "compression_ratio": 1.6719367588932805,
  "no_speech_prob": 0.0016594500048086047}, {"id": 593, "seek": 507784, "start": 5081.2,
  "end": 5085.76, "text": " uh, this is just like a pure scale of how how how we scale
  machine learning", "tokens": [50532, 2232, 11, 341, 307, 445, 411, 257, 6075, 4373,
  295, 577, 577, 577, 321, 4373, 3479, 2539, 50760], "temperature": 0.0, "avg_logprob":
  -0.21875047246250537, "compression_ratio": 1.6719367588932805, "no_speech_prob":
  0.0016594500048086047}, {"id": 594, "seek": 507784, "start": 5086.8, "end": 5088.24,
  "text": " Applications", "tokens": [50812, 26519, 763, 50884], "temperature": 0.0,
  "avg_logprob": -0.21875047246250537, "compression_ratio": 1.6719367588932805, "no_speech_prob":
  0.0016594500048086047}, {"id": 595, "seek": 507784, "start": 5088.32, "end": 5093.52,
  "text": " Yeah, so on on one hand it kind of was predefined as you said you found
  the job on the other hand", "tokens": [50888, 865, 11, 370, 322, 322, 472, 1011,
  309, 733, 295, 390, 659, 37716, 382, 291, 848, 291, 1352, 264, 1691, 322, 264, 661,
  1011, 51148], "temperature": 0.0, "avg_logprob": -0.21875047246250537, "compression_ratio":
  1.6719367588932805, "no_speech_prob": 0.0016594500048086047}, {"id": 596, "seek":
  507784, "start": 5094.0, "end": 5099.68, "text": " You still were curious to implement
  that algorithm. So like it wasn''t like somebody said okay", "tokens": [51172, 509,
  920, 645, 6369, 281, 4445, 300, 9284, 13, 407, 411, 309, 2067, 380, 411, 2618, 848,
  1392, 51456], "temperature": 0.0, "avg_logprob": -0.21875047246250537, "compression_ratio":
  1.6719367588932805, "no_speech_prob": 0.0016594500048086047}, {"id": 597, "seek":
  507784, "start": 5099.68, "end": 5105.12, "text": " You have to do it right you
  could also choose a job of like okay. I''m just coding nine to five and then I go
  home", "tokens": [51456, 509, 362, 281, 360, 309, 558, 291, 727, 611, 2826, 257,
  1691, 295, 411, 1392, 13, 286, 478, 445, 17720, 4949, 281, 1732, 293, 550, 286,
  352, 1280, 51728], "temperature": 0.0, "avg_logprob": -0.21875047246250537, "compression_ratio":
  1.6719367588932805, "no_speech_prob": 0.0016594500048086047}, {"id": 598, "seek":
  510512, "start": 5106.08, "end": 5108.88, "text": " But like you still decided to
  implement an algorithm", "tokens": [50412, 583, 411, 291, 920, 3047, 281, 4445,
  364, 9284, 50552], "temperature": 0.0, "avg_logprob": -0.23932915642147973, "compression_ratio":
  1.6132075471698113, "no_speech_prob": 0.003961828537285328}, {"id": 599, "seek":
  510512, "start": 5111.12, "end": 5114.24, "text": " Well, yes, well that that was
  a fun job. So", "tokens": [50664, 1042, 11, 2086, 11, 731, 300, 300, 390, 257, 1019,
  1691, 13, 407, 50820], "temperature": 0.0, "avg_logprob": -0.23932915642147973,
  "compression_ratio": 1.6132075471698113, "no_speech_prob": 0.003961828537285328},
  {"id": 600, "seek": 510512, "start": 5115.5199999999995, "end": 5122.24, "text":
  " Yeah, so like you were not scared by the challenge itself, right? Maybe was it
  like motivating actually", "tokens": [50884, 865, 11, 370, 411, 291, 645, 406, 5338,
  538, 264, 3430, 2564, 11, 558, 30, 2704, 390, 309, 411, 41066, 767, 51220], "temperature":
  0.0, "avg_logprob": -0.23932915642147973, "compression_ratio": 1.6132075471698113,
  "no_speech_prob": 0.003961828537285328}, {"id": 601, "seek": 510512, "start": 5123.68,
  "end": 5128.0, "text": " There was no like that much push like from the like", "tokens":
  [51292, 821, 390, 572, 411, 300, 709, 2944, 411, 490, 264, 411, 51508], "temperature":
  0.0, "avg_logprob": -0.23932915642147973, "compression_ratio": 1.6132075471698113,
  "no_speech_prob": 0.003961828537285328}, {"id": 602, "seek": 510512, "start": 5129.12,
  "end": 5134.4, "text": " From from the company itself. So we could we could do whatever
  we want inside the company", "tokens": [51564, 3358, 490, 264, 2237, 2564, 13, 407,
  321, 727, 321, 727, 360, 2035, 321, 528, 1854, 264, 2237, 51828], "temperature":
  0.0, "avg_logprob": -0.23932915642147973, "compression_ratio": 1.6132075471698113,
  "no_speech_prob": 0.003961828537285328}, {"id": 603, "seek": 513440, "start": 5134.4,
  "end": 5136.4, "text": " So it was very like relaxed", "tokens": [50364, 407, 309,
  390, 588, 411, 14628, 50464], "temperature": 0.0, "avg_logprob": -0.1659189987182617,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.0006032013334333897},
  {"id": 604, "seek": 513440, "start": 5136.799999999999, "end": 5141.2, "text": "
  Yeah, that might be actually a really good background to invent things", "tokens":
  [50484, 865, 11, 300, 1062, 312, 767, 257, 534, 665, 3678, 281, 7962, 721, 50704],
  "temperature": 0.0, "avg_logprob": -0.1659189987182617, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.0006032013334333897}, {"id": 605, "seek": 513440, "start": 5141.679999999999,
  "end": 5146.4, "text": " Don''t you think like if if you if you come to work and
  somebody says no, you cannot do what you want", "tokens": [50728, 1468, 380, 291,
  519, 411, 498, 498, 291, 498, 291, 808, 281, 589, 293, 2618, 1619, 572, 11, 291,
  2644, 360, 437, 291, 528, 50964], "temperature": 0.0, "avg_logprob": -0.1659189987182617,
  "compression_ratio": 1.7142857142857142, "no_speech_prob": 0.0006032013334333897},
  {"id": 606, "seek": 513440, "start": 5146.4, "end": 5150.08, "text": " You should
  do this and it might be kind of too restrictive", "tokens": [50964, 509, 820, 360,
  341, 293, 309, 1062, 312, 733, 295, 886, 43220, 51148], "temperature": 0.0, "avg_logprob":
  -0.1659189987182617, "compression_ratio": 1.7142857142857142, "no_speech_prob":
  0.0006032013334333897}, {"id": 607, "seek": 513440, "start": 5150.5599999999995,
  "end": 5155.759999999999, "text": " But here like they''ve been both challenges
  and also that freedom to solve those challenges", "tokens": [51172, 583, 510, 411,
  436, 600, 668, 1293, 4759, 293, 611, 300, 5645, 281, 5039, 729, 4759, 51432], "temperature":
  0.0, "avg_logprob": -0.1659189987182617, "compression_ratio": 1.7142857142857142,
  "no_speech_prob": 0.0006032013334333897}, {"id": 608, "seek": 513440, "start": 5157.44,
  "end": 5161.5199999999995, "text": " Yeah, there are like two components first of
  all you need to have like", "tokens": [51516, 865, 11, 456, 366, 411, 732, 6677,
  700, 295, 439, 291, 643, 281, 362, 411, 51720], "temperature": 0.0, "avg_logprob":
  -0.1659189987182617, "compression_ratio": 1.7142857142857142, "no_speech_prob":
  0.0006032013334333897}, {"id": 609, "seek": 516152, "start": 5162.160000000001,
  "end": 5169.92, "text": " Freedom and do long long term stuff. So like without worrying
  or like what are you going to ship into production soon?", "tokens": [50396, 22208,
  293, 360, 938, 938, 1433, 1507, 13, 407, 411, 1553, 18788, 420, 411, 437, 366, 291,
  516, 281, 5374, 666, 4265, 2321, 30, 50784], "temperature": 0.0, "avg_logprob":
  -0.24563800927364465, "compression_ratio": 1.7818930041152263, "no_speech_prob":
  0.0029202087316662073}, {"id": 610, "seek": 516152, "start": 5169.92, "end": 5171.68,
  "text": " The second is concentration of talent", "tokens": [50784, 440, 1150, 307,
  9856, 295, 8301, 50872], "temperature": 0.0, "avg_logprob": -0.24563800927364465,
  "compression_ratio": 1.7818930041152263, "no_speech_prob": 0.0029202087316662073},
  {"id": 611, "seek": 516152, "start": 5172.4800000000005, "end": 5176.0, "text":
  " So you have like high concentration of talent so people can", "tokens": [50912,
  407, 291, 362, 411, 1090, 9856, 295, 8301, 370, 561, 393, 51088], "temperature":
  0.0, "avg_logprob": -0.24563800927364465, "compression_ratio": 1.7818930041152263,
  "no_speech_prob": 0.0029202087316662073}, {"id": 612, "seek": 516152, "start": 5177.040000000001,
  "end": 5178.88, "text": " Share ideas", "tokens": [51140, 14945, 3487, 51232], "temperature":
  0.0, "avg_logprob": -0.24563800927364465, "compression_ratio": 1.7818930041152263,
  "no_speech_prob": 0.0029202087316662073}, {"id": 613, "seek": 516152, "start": 5178.88,
  "end": 5183.200000000001, "text": " Yeah, if you have this mix so like there will
  there will be innovations for sure", "tokens": [51232, 865, 11, 498, 291, 362, 341,
  2890, 370, 411, 456, 486, 456, 486, 312, 24283, 337, 988, 51448], "temperature":
  0.0, "avg_logprob": -0.24563800927364465, "compression_ratio": 1.7818930041152263,
  "no_speech_prob": 0.0029202087316662073}, {"id": 614, "seek": 516152, "start": 5183.68,
  "end": 5190.64, "text": " Yeah, it sounds like you had a combination of all three
  components that you mentioned, right? So like talents and also yeah", "tokens":
  [51472, 865, 11, 309, 3263, 411, 291, 632, 257, 6562, 295, 439, 1045, 6677, 300,
  291, 2835, 11, 558, 30, 407, 411, 19933, 293, 611, 1338, 51820], "temperature":
  0.0, "avg_logprob": -0.24563800927364465, "compression_ratio": 1.7818930041152263,
  "no_speech_prob": 0.0029202087316662073}, {"id": 615, "seek": 519064, "start": 5191.52,
  "end": 5194.320000000001, "text": " Yeah, yeah, I also saw that another company
  is like", "tokens": [50408, 865, 11, 1338, 11, 286, 611, 1866, 300, 1071, 2237,
  307, 411, 50548], "temperature": 0.0, "avg_logprob": -0.21239442091721755, "compression_ratio":
  1.7885462555066078, "no_speech_prob": 0.00251026707701385}, {"id": 616, "seek":
  519064, "start": 5194.96, "end": 5201.4400000000005, "text": " Yeah, like in Samsung
  there was already a strong team and there were like lots of innovation. So there
  are a few startups", "tokens": [50580, 865, 11, 411, 294, 13173, 456, 390, 1217,
  257, 2068, 1469, 293, 456, 645, 411, 3195, 295, 8504, 13, 407, 456, 366, 257, 1326,
  28041, 50904], "temperature": 0.0, "avg_logprob": -0.21239442091721755, "compression_ratio":
  1.7885462555066078, "no_speech_prob": 0.00251026707701385}, {"id": 617, "seek":
  519064, "start": 5202.320000000001, "end": 5206.64, "text": " Uh, which came from
  our lab and there was like a really good paper", "tokens": [50948, 4019, 11, 597,
  1361, 490, 527, 2715, 293, 456, 390, 411, 257, 534, 665, 3035, 51164], "temperature":
  0.0, "avg_logprob": -0.21239442091721755, "compression_ratio": 1.7885462555066078,
  "no_speech_prob": 0.00251026707701385}, {"id": 618, "seek": 519064, "start": 5208.0,
  "end": 5212.72, "text": " Yeah, so that that that''s a that''s a recipe for innovation
  for sure", "tokens": [51232, 865, 11, 370, 300, 300, 300, 311, 257, 300, 311, 257,
  6782, 337, 8504, 337, 988, 51468], "temperature": 0.0, "avg_logprob": -0.21239442091721755,
  "compression_ratio": 1.7885462555066078, "no_speech_prob": 0.00251026707701385},
  {"id": 619, "seek": 519064, "start": 5213.52, "end": 5219.280000000001, "text":
  " Yeah, yeah, I''m really happy that it turned out so well to you for you and uh
  your author as well", "tokens": [51508, 865, 11, 1338, 11, 286, 478, 534, 2055,
  300, 309, 3574, 484, 370, 731, 281, 291, 337, 291, 293, 2232, 428, 3793, 382, 731,
  51796], "temperature": 0.0, "avg_logprob": -0.21239442091721755, "compression_ratio":
  1.7885462555066078, "no_speech_prob": 0.00251026707701385}, {"id": 620, "seek":
  521928, "start": 5219.84, "end": 5223.44, "text": " I think he continues to work
  also in the industry at least last time I checked", "tokens": [50392, 286, 519,
  415, 6515, 281, 589, 611, 294, 264, 3518, 412, 1935, 1036, 565, 286, 10033, 50572],
  "temperature": 0.0, "avg_logprob": -0.2183579314838756, "compression_ratio": 1.5961538461538463,
  "no_speech_prob": 0.0023854163009673357}, {"id": 621, "seek": 521928, "start": 5223.92,
  "end": 5226.88, "text": " um, and so I I really hope that", "tokens": [50596, 1105,
  11, 293, 370, 286, 286, 534, 1454, 300, 50744], "temperature": 0.0, "avg_logprob":
  -0.2183579314838756, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.0023854163009673357}, {"id": 622, "seek": 521928, "start": 5227.92, "end": 5233.92,
  "text": " You will get some really cool pull requests on hnsw that will pass your
  criteria", "tokens": [50796, 509, 486, 483, 512, 534, 1627, 2235, 12475, 322, 276,
  3695, 86, 300, 486, 1320, 428, 11101, 51096], "temperature": 0.0, "avg_logprob":
  -0.2183579314838756, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.0023854163009673357}, {"id": 623, "seek": 521928, "start": 5236.08, "end": 5239.44,
  "text": " Well, yeah, most of them pass is just like I", "tokens": [51204, 1042,
  11, 1338, 11, 881, 295, 552, 1320, 307, 445, 411, 286, 51372], "temperature": 0.0,
  "avg_logprob": -0.2183579314838756, "compression_ratio": 1.5961538461538463, "no_speech_prob":
  0.0023854163009673357}, {"id": 624, "seek": 521928, "start": 5240.639999999999,
  "end": 5243.84, "text": " Would love to have more time and I''ll try to allocate
  more time", "tokens": [51432, 6068, 959, 281, 362, 544, 565, 293, 286, 603, 853,
  281, 35713, 544, 565, 51592], "temperature": 0.0, "avg_logprob": -0.2183579314838756,
  "compression_ratio": 1.5961538461538463, "no_speech_prob": 0.0023854163009673357},
  {"id": 625, "seek": 521928, "start": 5244.719999999999, "end": 5246.639999999999,
  "text": " Yeah, looking and checking them", "tokens": [51636, 865, 11, 1237, 293,
  8568, 552, 51732], "temperature": 0.0, "avg_logprob": -0.2183579314838756, "compression_ratio":
  1.5961538461538463, "no_speech_prob": 0.0023854163009673357}, {"id": 626, "seek":
  524664, "start": 5246.64, "end": 5253.360000000001, "text": " Yeah, it''s really
  really great. I really enjoyed talking to you Yuri. Um, thanks so much for allocating
  your time also in this", "tokens": [50364, 865, 11, 309, 311, 534, 534, 869, 13,
  286, 534, 4626, 1417, 281, 291, 33901, 13, 3301, 11, 3231, 370, 709, 337, 12660,
  990, 428, 565, 611, 294, 341, 50700], "temperature": 0.0, "avg_logprob": -0.2931802942511741,
  "compression_ratio": 1.6390243902439023, "no_speech_prob": 0.0014533621724694967},
  {"id": 627, "seek": 524664, "start": 5253.360000000001, "end": 5260.8, "text": "
  Precreasement time um, but yeah, I mean all the best to you in in the future also
  twitter and uh", "tokens": [50700, 6001, 66, 265, 296, 1712, 565, 1105, 11, 457,
  1338, 11, 286, 914, 439, 264, 1151, 281, 291, 294, 294, 264, 2027, 611, 21439, 293,
  2232, 51072], "temperature": 0.0, "avg_logprob": -0.2931802942511741, "compression_ratio":
  1.6390243902439023, "no_speech_prob": 0.0014533621724694967}, {"id": 628, "seek":
  524664, "start": 5261.84, "end": 5268.88, "text": " Hope to see some published work
  at some point, but I don''t know it just uh, I enjoyed reading your paper and and",
  "tokens": [51124, 6483, 281, 536, 512, 6572, 589, 412, 512, 935, 11, 457, 286, 500,
  380, 458, 309, 445, 2232, 11, 286, 4626, 3760, 428, 3035, 293, 293, 51476], "temperature":
  0.0, "avg_logprob": -0.2931802942511741, "compression_ratio": 1.6390243902439023,
  "no_speech_prob": 0.0014533621724694967}, {"id": 629, "seek": 526888, "start": 5269.68,
  "end": 5273.36, "text": " Kind of also then read read your code and it''s kind of
  like", "tokens": [50404, 9242, 295, 611, 550, 1401, 1401, 428, 3089, 293, 309, 311,
  733, 295, 411, 50588], "temperature": 0.0, "avg_logprob": -0.1744119703155203, "compression_ratio":
  1.6782608695652175, "no_speech_prob": 0.002410390181466937}, {"id": 630, "seek":
  526888, "start": 5274.08, "end": 5277.52, "text": " It feels like you''ve put a
  lot of effort there and and", "tokens": [50624, 467, 3417, 411, 291, 600, 829, 257,
  688, 295, 4630, 456, 293, 293, 50796], "temperature": 0.0, "avg_logprob": -0.1744119703155203,
  "compression_ratio": 1.6782608695652175, "no_speech_prob": 0.002410390181466937},
  {"id": 631, "seek": 526888, "start": 5278.56, "end": 5281.76, "text": " It uh, it
  also influences the industry so much today", "tokens": [50848, 467, 2232, 11, 309,
  611, 21222, 264, 3518, 370, 709, 965, 51008], "temperature": 0.0, "avg_logprob":
  -0.1744119703155203, "compression_ratio": 1.6782608695652175, "no_speech_prob":
  0.002410390181466937}, {"id": 632, "seek": 526888, "start": 5282.08, "end": 5286.16,
  "text": " So maybe you are not kind of realizing this every single day, but like",
  "tokens": [51024, 407, 1310, 291, 366, 406, 733, 295, 16734, 341, 633, 2167, 786,
  11, 457, 411, 51228], "temperature": 0.0, "avg_logprob": -0.1744119703155203, "compression_ratio":
  1.6782608695652175, "no_speech_prob": 0.002410390181466937}, {"id": 633, "seek":
  526888, "start": 5286.88, "end": 5294.8, "text": " Yeah, you should know this that
  there are so many databases that use your algorithm as as one of the baseline''s
  in production", "tokens": [51264, 865, 11, 291, 820, 458, 341, 300, 456, 366, 370,
  867, 22380, 300, 764, 428, 9284, 382, 382, 472, 295, 264, 20518, 311, 294, 4265,
  51660], "temperature": 0.0, "avg_logprob": -0.1744119703155203, "compression_ratio":
  1.6782608695652175, "no_speech_prob": 0.002410390181466937}, {"id": 634, "seek":
  526888, "start": 5295.92, "end": 5297.92, "text": " It''s really cool work", "tokens":
  [51716, 467, 311, 534, 1627, 589, 51816], "temperature": 0.0, "avg_logprob": -0.1744119703155203,
  "compression_ratio": 1.6782608695652175, "no_speech_prob": 0.002410390181466937},
  {"id": 635, "seek": 529792, "start": 5298.08, "end": 5300.8, "text": " Yeah, yeah,
  that that that that that was great that", "tokens": [50372, 865, 11, 1338, 11, 300,
  300, 300, 300, 300, 390, 869, 300, 50508], "temperature": 0.0, "avg_logprob": -0.3320886117440683,
  "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 636, "seek": 529792, "start": 5301.68, "end": 5303.68, "text": " There was
  success", "tokens": [50552, 821, 390, 2245, 50652], "temperature": 0.0, "avg_logprob":
  -0.3320886117440683, "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 637, "seek": 529792, "start": 5303.68, "end": 5306.4800000000005, "text":
  " Yeah, maybe one thing like I would note uh", "tokens": [50652, 865, 11, 1310,
  472, 551, 411, 286, 576, 3637, 2232, 50792], "temperature": 0.0, "avg_logprob":
  -0.3320886117440683, "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 638, "seek": 529792, "start": 5307.28, "end": 5312.96, "text": " That the
  idea was the rain cares. So that was partially implemented and there needs work",
  "tokens": [50832, 663, 264, 1558, 390, 264, 4830, 12310, 13, 407, 300, 390, 18886,
  12270, 293, 456, 2203, 589, 51116], "temperature": 0.0, "avg_logprob": -0.3320886117440683,
  "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 639, "seek": 529792, "start": 5313.76, "end": 5316.8, "text": " So he had
  a work on ER maybe you know like", "tokens": [51156, 407, 415, 632, 257, 589, 322,
  14929, 1310, 291, 458, 411, 51308], "temperature": 0.0, "avg_logprob": -0.3320886117440683,
  "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 640, "seek": 529792, "start": 5318.64, "end": 5320.64, "text": " by using
  the", "tokens": [51400, 538, 1228, 264, 51500], "temperature": 0.0, "avg_logprob":
  -0.3320886117440683, "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 641, "seek": 529792, "start": 5320.8, "end": 5323.04, "text": " And then
  as the for the final rain care", "tokens": [51508, 400, 550, 382, 264, 337, 264,
  2572, 4830, 1127, 51620], "temperature": 0.0, "avg_logprob": -0.3320886117440683,
  "compression_ratio": 1.706896551724138, "no_speech_prob": 0.0015692192828282714},
  {"id": 642, "seek": 532304, "start": 5323.92, "end": 5324.96, "text": " So", "tokens":
  [50408, 407, 50460], "temperature": 0.0, "avg_logprob": -0.2514350825342639, "compression_ratio":
  1.6770428015564203, "no_speech_prob": 0.005218378733843565}, {"id": 643, "seek":
  532304, "start": 5324.96, "end": 5330.8, "text": " Yeah, it''s just like so I felt
  that I need to cite this sure I need work for sure", "tokens": [50460, 865, 11,
  309, 311, 445, 411, 370, 286, 2762, 300, 286, 643, 281, 37771, 341, 988, 286, 643,
  589, 337, 988, 50752], "temperature": 0.0, "avg_logprob": -0.2514350825342639, "compression_ratio":
  1.6770428015564203, "no_speech_prob": 0.005218378733843565}, {"id": 644, "seek":
  532304, "start": 5331.6, "end": 5335.04, "text": " I learned this idea like maybe
  not was changing, but from from him", "tokens": [50792, 286, 3264, 341, 1558, 411,
  1310, 406, 390, 4473, 11, 457, 490, 490, 796, 50964], "temperature": 0.0, "avg_logprob":
  -0.2514350825342639, "compression_ratio": 1.6770428015564203, "no_speech_prob":
  0.005218378733843565}, {"id": 645, "seek": 532304, "start": 5335.68, "end": 5342.32,
  "text": " Yeah, yeah, it sounds great. I mean, I''ve also interacted a bit with
  him uh and and it sounds like he''s very knowledgeable guy", "tokens": [50996, 865,
  11, 1338, 11, 309, 3263, 869, 13, 286, 914, 11, 286, 600, 611, 49621, 257, 857,
  365, 796, 2232, 293, 293, 309, 3263, 411, 415, 311, 588, 33800, 2146, 51328], "temperature":
  0.0, "avg_logprob": -0.2514350825342639, "compression_ratio": 1.6770428015564203,
  "no_speech_prob": 0.005218378733843565}, {"id": 646, "seek": 532304, "start": 5342.88,
  "end": 5344.88, "text": " And he has very strong opinions as well", "tokens": [51356,
  400, 415, 575, 588, 2068, 11819, 382, 731, 51456], "temperature": 0.0, "avg_logprob":
  -0.2514350825342639, "compression_ratio": 1.6770428015564203, "no_speech_prob":
  0.005218378733843565}, {"id": 647, "seek": 532304, "start": 5344.96, "end": 5348.24,
  "text": " So maybe we will also talk with him on one of the episodes", "tokens":
  [51460, 407, 1310, 321, 486, 611, 751, 365, 796, 322, 472, 295, 264, 9313, 51624],
  "temperature": 0.0, "avg_logprob": -0.2514350825342639, "compression_ratio": 1.6770428015564203,
  "no_speech_prob": 0.005218378733843565}, {"id": 648, "seek": 532304, "start": 5349.04,
  "end": 5352.8, "text": " Uh, but um, yeah, I''m glad that you guys collaborated",
  "tokens": [51664, 4019, 11, 457, 1105, 11, 1338, 11, 286, 478, 5404, 300, 291, 1074,
  42463, 51852], "temperature": 0.0, "avg_logprob": -0.2514350825342639, "compression_ratio":
  1.6770428015564203, "no_speech_prob": 0.005218378733843565}, {"id": 649, "seek":
  535304, "start": 5353.68, "end": 5357.36, "text": " Yeah, it''s it''s a fantastic
  result for for the industry as well", "tokens": [50396, 865, 11, 309, 311, 309,
  311, 257, 5456, 1874, 337, 337, 264, 3518, 382, 731, 50580], "temperature": 0.0,
  "avg_logprob": -0.22022696464292466, "compression_ratio": 1.8402061855670102, "no_speech_prob":
  0.0010746006155386567}, {"id": 650, "seek": 535304, "start": 5358.48, "end": 5363.44,
  "text": " And and probably for your profiles well not probably but definitely for
  your profiles", "tokens": [50636, 400, 293, 1391, 337, 428, 23693, 731, 406, 1391,
  457, 2138, 337, 428, 23693, 50884], "temperature": 0.0, "avg_logprob": -0.22022696464292466,
  "compression_ratio": 1.8402061855670102, "no_speech_prob": 0.0010746006155386567},
  {"id": 651, "seek": 535304, "start": 5364.64, "end": 5371.92, "text": " So yeah,
  um, thank you so much for your time and um, yeah, I hope you will have a relaxing
  time over the Christmas and", "tokens": [50944, 407, 1338, 11, 1105, 11, 1309, 291,
  370, 709, 337, 428, 565, 293, 1105, 11, 1338, 11, 286, 1454, 291, 486, 362, 257,
  20103, 565, 670, 264, 5272, 293, 51308], "temperature": 0.0, "avg_logprob": -0.22022696464292466,
  "compression_ratio": 1.8402061855670102, "no_speech_prob": 0.0010746006155386567},
  {"id": 652, "seek": 535304, "start": 5372.88, "end": 5374.88, "text": " Happy new
  year as well", "tokens": [51356, 8277, 777, 1064, 382, 731, 51456], "temperature":
  0.0, "avg_logprob": -0.22022696464292466, "compression_ratio": 1.8402061855670102,
  "no_speech_prob": 0.0010746006155386567}, {"id": 653, "seek": 535304, "start": 5375.28,
  "end": 5377.28, "text": " So thank you very much for your time Yuri", "tokens":
  [51476, 407, 1309, 291, 588, 709, 337, 428, 565, 33901, 51576], "temperature": 0.0,
  "avg_logprob": -0.22022696464292466, "compression_ratio": 1.8402061855670102, "no_speech_prob":
  0.0010746006155386567}, {"id": 654, "seek": 535304, "start": 5378.4, "end": 5380.4,
  "text": " Thank you", "tokens": [51632, 1044, 291, 51732], "temperature": 0.0, "avg_logprob":
  -0.22022696464292466, "compression_ratio": 1.8402061855670102, "no_speech_prob":
  0.0010746006155386567}, {"id": 655, "seek": 535304, "start": 5380.4, "end": 5382.4,
  "text": " Yeah, bye bye", "tokens": [51732, 865, 11, 6543, 6543, 51832], "temperature":
  0.0, "avg_logprob": -0.22022696464292466, "compression_ratio": 1.8402061855670102,
  "no_speech_prob": 0.0010746006155386567}, {"id": 656, "seek": 538304, "start": 5383.04,
  "end": 5402.64, "text": " Um", "tokens": [50396, 3301, 51344], "temperature": 1.0,
  "avg_logprob": -3.687346935272217, "compression_ratio": 0.2, "no_speech_prob": 0.313255250453949}]'
---

Hello, vector podcast is here and today we're going to be talking to the author of H&SW library and algorithm. It's one of the best algorithms out there, one of the most used algorithms in vector search. And today I'm talking to Yuri Malkov. How are you doing? Hi. Hi. Hi.
So yeah, my name is Yuri Malkov. Currently I'm working at Twitter. There's a staff from my engineer and the content understanding and research and recommender systems. Yeah, please know that during discussion I don't represent like Twitter's point of view. The views are of my own.
Yeah, so it's great. So yeah, you already began introducing yourself. So I was wondering if you could tell me a bit about yourself, your background and then maybe we can also move into discussing the algorithm itself. Okay, sure. Yeah, so my trajectory of moving to ML is quite typical to Russia.
So yeah, I got good physics education in Nizhny Novgorod and there I did the PhD in laser physics. So there I was doing experiments on teravat lasers. So that was fun and like that part of physics is like considered to be like sexy part, similar to computer vision in machine learning.
And I was lucky to have good supervisors. So one of my supervisor which was like mostly a supervisor of paper. So he helped me. Is now the head of Russian Academy. So yeah, I had good supervisors.
In addition to physics, I was concurrently working part time in a startup that was building distributed scalable search systems based on insights from real networks. Yeah, that worked ended up in several papers on predecessor of H&W.
And the startup, yeah, unfortunately the startup was closed before even I got PhD. So yeah, I decided to focus on physics after that, but after I got my PhD degree in physics. So I, like there was a choice for me like what to do next and to proceed with career and physics.
I had to go abroad, like I didn't want to go abroad. I want to stay in Nizhny Novgorod. So I decided to just like switch directions and to network science there. And then I got a really good grant from the Russian fund. Alpha Phi, which now is not present anymore.
So I could do like research by my own. Like this pretty good salary. And yeah, I also joined companies, like computer vision companies to get to insight into why people actually use like similarities to your algorithm and machine learning.
And I worked at an television and later anti-club, which is the company that is like doing big brother for Moscow, like Moscow surveillance.
And later I joined some some VIS Center in Moscow and I worked with like Victor Limpitsky who is one of the well known personas in Russia and in 2019 I moved to US and now I work in Twitter to recommend their systems and content understanding, like board models. Oh yeah.
So you probably also use nearest neighbor search in your work or. Well, I can mention it. Yeah, well, not really. So I'm focused on the so I can work Twitter most of the time. I can have last half a year, I spent on improving search relevance. So that is mostly the ranker.
But that is closely related to the nearest neighbor search. Yeah. So you mentioned like basically the background where you've been in Russia, it was like kind of related to computer vision. Of course, you had physics background by education, but you also kind of worked in computer vision startups.
So what was your impression of this nearest neighbor search problem and like, how did you think about it when like, did you read papers to understand like what was done in that area? I think that areas pretty like developed right in in in the papers like like NSW itself, right? Like navigators.
Well, so like in the startup meta labs, I have been working, I think I've worked for six or seven years. So it was quite quite a significant period of time. And then we started just like from distributed search. So the idea was like we do it from scratch.
So like we don't care what I've been done before. So we have an idea. So there are like distributed hash tables like port or other stuff and we want to do it, but with similarity search. So that should scale to better base. And there that's like very different approach from nearest neighbor search.
And like most of the time we spent like developing this algorithm was not even like nearest neighbor search. That was closer to this symbolic filtering, but with like arbitrary filters.
And only at some point of time, like we had a realization that oh, like that is similar to what people actually need. Like there are a lot of papers of on nearest neighbor search. So we switch direction and like the most cited publications are on nearest neighbors. Yeah. Yeah.
I don't remember was it on your paper or somebody else's paper. I saw a paper of my old friend, you reliefs because he actually defended his thesis like in PG thesis in this space. So when he was doing it, I think it was 2009.
I was like, I was considering this like a pure mathematical problem without like maybe direct application. But then he gave a talk at Google, like you know, Google tech talks. I don't know if they still exist or not, but like he presented this problem and like they did some optimizations as well.
And then I think I think your paper sites it or maybe someone else's I don't remember. I was like really surprised to see, you know, his work also kind of in the same line of things that now lead to vector search essentially. Well, yeah, I think I saw his work, but it seemed like more theory.
Like if you look to history like of like graph approaches so like. Now it's mostly like rehashing of old stuff. So definitely new things, but like there is so much work done before like Sergey Brein worked on nearest neighbor search with like GNIT. So that is also like good work.
There were there were previous work on graph search, I think in 1993, which like aren't that much different compared to like current though, like they have also problems with scalability at that point. So I think yeah, so that was. There is a large number of like previous work in that area.
But you said like you didn't concern yourself with reading too many papers before you started inventing this new algorithm. Is that right? Yeah, sure, sure, we read papers, but they were not really relevant. So we read papers on network science.
And so we tried to so there was a problem with building like this, no navigable small roles. So like not every small network is navigable. Like most models are not. So we wanted to build navigable small and there were also didn't understand like.
Like what what was the criteria like what is like how we could make it and we reinvented like this. Dillon or graphs inside the company and after like you reinvented like you know starting to search and see there are lots of papers who did the same. Right. Yeah. So yeah. So we went the other way.
Yeah. So now that you mentioned this thing like can you actually please introduce this concepts at least on high level to our audience like what is a small world what is like what white it's to be navigable kind of a little bit like more to the user facing level if it's possible.
Well, like navigable small world so you have a large network. And so navigable small world that means you can find paths between like arbitrary elements in this network using which is a logarithmic scale. So the number of hopes can be done with the rhythmic and you can use only local information.
And do like something like greedy search like greedy searches allow and if you can find like the path and the algorithmic steps to your network is navigable. And that small world part like why is it small small.
And that's like history how he's historical reasons so there was like a famous like milligram experiment where they they send letters from one person like from random person to some target person.
That was kind of greedy like greedy search for connections very similar to this and that that's called like small world experiment so like a small world. And real networks like people have like real networks have low diameter like human human connection networks.
And they are navigable like at least according to milligram experiments and like subsequent experiments. Is it kind of related in common terms like to six handshakes that you need to connect every random person with another random person on the planet.
Yes, yes, so that's that's like that experiment is pretty sure I think it's done in the 60s so yeah so. And so the navigable part is basically like if we put this in the context of search right so.
So let's say I have local information I'm here I would like to travel from here let's say I'm in Helsinki I would like to travel to New York like how do I travel right I need to go to the airport.
From the airport I will travel maybe to some city in Europe from there I will change you know the airplane and then fly over to New York.
I'm making it a little bit more complicated there is a direct flight to New York from Helsinki but okay maybe that wasn't right is that analogous to navigable part.
Yes, yes, so like generally like that you can pinpoint that but if you start and finish in like small local airports which usually don't have connections, my magic connection so they connected to hops.
Yeah, and that is one of the model of navigable small roles so there are like Kleinberg's model which doesn't have hops so you can also build navigable small walls without hops.
 But they have polylogarifmix coedizian so if you want to have polylogarifmix coedizian so maybe I'll ask you to provide some references later so especially for those who want to dig deeper into the smithematics like you mentioned these different algorithms like many of them are new to me at least so I'm sure to our part of our audience.
 Part of our audience as well and I wanted to also ask you like on the context of your invention like what was the input so you said like you had a lot of data right from computer vision but like was there something else like dimensionality or some other constraint that was kind of tough for previous algorithms like a LSH or you know any other.
Well, there LSH didn't even work so we worked with like three structures we have to like how will you do LSH.
 Yeah, for and for LSH so I thought that those are not practical algorithms so even when I spoke with people who like were writing a lot of papers on LSH they like expressed doubts and whether those algorithms are practical so they are not learnable so they cannot take advantage of the data that you have so like that.
And like what what they told is like they see as quantization as just a better version of practical version of LSH.
Yeah right and so actually I'm really interested like how did you set up to invent the algorithm like I can just give you briefly like in the recent billion scale vector search challenge.
We had like a small team and one of our team members actually implemented like a small change in product quantization layer like basically how you shuffle the dimensions in the vector and he achieved like 12% recall increase over the baseline you know the Facebook sell algorithm.
I didn't like have that much knowledge I've read your paper I've read other papers and so I was just thinking okay if I if I would start from first principles how would I solve it like I know nothing about this problem right so like how can I solve you know the search in multi-dimensional space.
And so I actually implemented a very very simple algorithm using your algorithm as one of the components maybe we can talk later about it but like how did you start inventing H&S W.
Well H&S W had a pretty assessor so it has like an NSW it's also called MSW or SW graph in different places like depending on where you look so and there I just so it had problems.
So it had several problems but like for like if you don't think about distributed setup the main problem it had poly algorithmic scalability with a number of elements and that killed the performance on low dimensional data.
 So there were like comparison works like one by Leonid Bytes of where he evaluated different algorithms and like its performance really like it didn't perform that well on some data set and the loss was by many orders of magnitude so it could be like one like 1000 times slower than the best solution and yeah.
So the work on H&S W were targeted at just improving the previous version so it wouldn't have this problem and like ideally would perform the best on all setups. So yeah and that that that that has been solved.
Right but like you still needed to add that magical age in front of it so you made it hierarchical like what what pushed you in the direction of making it hierarchical and what what did you think that it might work or was it like as a result of experimentation that it proved to work.
Well yeah that that that's that's yeah that has many ingredients in it so for for one thing when I worked with the startup mirror labs so we had a different problem with distributed index that NSW had a pleasant quality that the hubs that are created in the network are the first elements.
So and the for distributed system you would want to add new nodes to the system and you will have much capacity like increase the capacity of the system but because all your hubs on in the first notes like in the older notes because they have been created before new nodes even existed.
 The traffic is routed through the same old notes which make it not scalable and we spent quite a lot of time on figuring out how to solve it and there at some point I've noticed that like our NSW approach is pretty similar to skip list in terms of what what has been what is being protest as final network.
The idea is like if you if you create a skip list for one D and create the NSW for one D and then like for skip list you just merge the all all links regardless of player you will get a similar network in terms of like degree distribution like distance distribution well all major properties.
 So but skip list doesn't have this property so you can add new nodes and they can have like they can have higher levels and like your traffic will be a road through notes in your form like across your distributed system so and that thing we knew like from the startup that there is a like equivalence but that was only for the problem of distributed search.
So it would still use the same polylogar if Michael like 3d search algorithm like which doesn't think about like what is that how many links you have on a note so that was shelved for that reasons in the startup but then so after ID PhD so like I wanted to publish a good paper on network science.
 And there like it was and I like there is there is a result that we can create a new navigable networks which a method which was not known before so I tried to publish it in nature so it was rejected like nature physics also rejected that it was rejected by editors then in scientific reports was rejected after a review and then like it was finally published in plus one.
And I think like I really like this paper so that was like the most surprising result I think I got but yet it's not really decided.
And as a byproduct of this I did a comparison to other navigable small world methods and so like maybe I have maybe like this approach with like the old vision that you can apply like you can look at the real world networks and replicate it and like computer system and they will be.
So I replicate that the work done like scale free navigable navigable small worlds which are very popular thing till the moment all.
And so that the performance was really was like very bad like extremely bad and the reason for that that if you have a scale free network and scale free means you have a power low distribution of degree and usually they like there is a.
 coefficient gamma and like the best cases was gamma is close to two but gamma close to two means that the scalability with the size of the network so the degree scale is almost linearly so when you have a like a greedy search for the hub so when it goes through the hub like it to play it's like a huge portion of the network so you have like linear scalability instead of like ultra logarithmic so log log again which is.
 They like the number of hope is log log in but at some point you evaluate to like almost every point in your network and you have like really bad performance and that like that after that realized what was the problem with NSW and like I thought all like we already have a solution for that so because keep least doesn't have this problem and so yeah after that I implemented the prototype and it worked.
Working on the like C++ version and the evaluation. By the way when when you started implementing your prototype was it initially in C++ now it wasn't in in in in Java and Java because Java is your favorite language or what was it Java.
Because the distributed system like that was implemented in Java so that was close so like it was easier to integrate like if you like maybe you were thinking it's easier to integrate in Java right.
Well I just know how to code it in Java so I code that several times for NSW and that all Java code was released.
So yeah just code it and then like I had to transfer it to C++ to make it efficient and like yeah and so there is like Leonid bites off so who who is a maintainer of an MS leap so I have been in contact with him for quite a while and yeah so it was implemented in the library.
Did you like collaborate with him to to to implement it using the enemy sleep sort of the most efficient way or.
Well first of all like the ideology of the library is very close to like what we have been developing so it's not only focused on like typical distances like L2, Cassian or even like inner product.
So yeah it makes sense to compare on all those distances and Leonid also had a paper like in a bench like on all of those so we can just implement a new algorithm and run a bench.
Right and come so that that was like a really good point and it also wasn't implemented in and benchmark so if you add an algorithm so we can like.
Go through all sets of benchmarks yeah yeah yeah so like it was kind of easy for you to evaluate where you algorithm stands against other algorithms right so like yes right right and so what was the. And you also had a call to write maybe maybe you could introduce him as well like on your paper.
Oh yeah that that is midrida shunyan so. So that's that that that was my peer in the like physics lab he also got PhD the same year I did so yeah so. Yeah so we decided to team up with that so he helped a lot on he he did he did the all evaluation so he integrated it with other code.
And here on the evaluation on the like clusters that we had. Yeah at that point nice so so back to the invention like as you've been inventing this elbow did you have to make a lot of adjustments to the core of the algorithm as you have been evaluating it or was it like.
You know the first shot and it was it. Well not really so there are like two changes compared to NSW in the national SW so first one is the idea of layers so that's all most of the problems with like low dimensional data and.
Yeah also improve performance like in most of the tax that like most of the distributions even like but maybe not much like high dimensional data but still when I ran the whole like suit that was there was a few data set on we should perform worse compared to.
VP3 so that's from Leonits you then I thought that wasn't a big deal but like communicated the results with Leonit trying to convince him that like we don't need to have that much algorithms.
But he was not convinced so then we added like an improvement with the heuristic for selecting the neighbors which like I personally knew from the work on spatial approximation three.
That made that that made the transition to skip list exact so it made an exact so you can build the exact skip list in one day using this heuristic and after that so yeah that that that that addition improved the performance yeah.
I remember please correctly if i'm wrong but like I've read your paper actually really really closely so I printed it and you know like I was reading with the pencil actually making notes so remember like at some point was it so that you agree to them it also needs to prove that it will converge.
 Or like because you keep resuffling the points in some way right like as you build it you use multiple threads like in order to kind of build the actual paths between the nodes between layers right so like do you need to kind of still somehow make sure that it will converge on all dimensionality so all spaces or was it was it not necessary.
 Well so the algorithm is pretty stable so the result is like how many threads you can go that is an empirical result so I was surprised when I saw it but you know even like for NSW the first algorithm even if you start to do like to use I know 40 threads from a single element I can found no no no drop in the recall.
No drop in the recall or speed that was a bit surprising. In terms of stability. So the main way to make it stable is just like to avoid avoid exploring so like use use proper parameters big enough there are ways to make it stable in.
For corruption so when when but that that that that is pretty costly so if you bootstrap the graph so if you like do iterations like similar to an undecent I think you probably know that I can make it stable even if it's corrupted by a lot.
So that is done only for updates so like when you update your kind of corrupting the graph and well in the like a channels WLIP.
So for updates it wasn't specifically made to be like very stable but for just construction it doesn't have to be like that's stable doesn't have to conversion all situation just keep the parameters high enough and it wouldn't diverge.
 Right yeah because I remember like and I'm also curious to hear your opinion so then I after your paper I started reading other papers for example the Microsoft's zoom algorithm and then later they called it discount and with some modifications so they were comparing to etch and SW at larger scale something like billions of nodes billions of points in the space right.
 And so they they were trying to minimize the cost that that that it will incur because basically as you build the H and SW you also use memory quite a bit right so I wanted to hear your opinion on that part and then they what they did is that they I don't know if you're familiar with these papers but what they did is that they offloaded portion of the retrieval to to an SSD disk.
And so they kind of combined your algorithm with like additional layers and then they kind of resolve to full precision when they go to SSD disk but they don't don't do it in memory. So they do use quantization right yeah they use quantization exactly.
 That's a very popular approach and that makes sense so it's so basically you have a hardware limitation so that you can can store but you have a hardware here are here so you have like not so big RAM and like lots of SSDs and maybe like if you have distributed system you have access to other nodes.
So yeah that's a clever use of here are here that makes sense. But at the same time like your algorithm was taken into using to popular frameworks like files right so like files is not a single algorithm like one of them as H and SW and then.
Actually don't know how they did it did they take your C++ dependency directly or did they implemented do know.
They very implemented from scratch so like I talked to them once so they said they tried different way but like in the end it was like pretty close to the like the initial C++ library don't have some different there is some if something's are implemented differently in fights.
So for instance there is a thread pool like in channels WL for keeping track of visited elements so when you have a new search if there is like a map like think of a bitmap for which knows which notes in the network are visited.
And the channels WL it's kept in memory all the time and when you have like a new search it will just like peaks from the pool and then face like it creates it once per search so there are much searches more more effective.
 Yeah yeah yeah by search yeah batch search is another feature that sometimes is implemented in vector databases but did you like expect that your algorithm would become so widely applicable like do you know that it has been re implemented in several languages like for example as part of vector database called V ev8 it was implemented in goal.
And there is a database called quadrant it it's implemented in rast and of course all of these implementations also add like crowd support so they you can actually update right because in reality in database you need these features.
And then they also added symbolic filtering on top of that so it's also inside your algorithm like did you did you expect such popularity. No no like I thought that we will publish the algorithm and like we will win the benchmarks and we're clearly seeing.
But though at that time like just before we published the benchmark there was a like competitor Falcon which also published the benchmarks of widget better but like for Falcon targeted like not like that much and I thought that well Falcon was only like for few specific metrics.
And yeah actually it also was done by like person from the same school which I went so it was in jarrison stain so I talked with him a bit and I thought that like we have open source to code so we published the paper so like people will quickly just like iterate on top of that and like improve.
 But yeah so it took much more time to others to improve upon it compared to what I've expected and maybe that was due to lack of interest maybe that was to some inertia so I don't know like looking at the how many startups and solutions are popping out right now it seems like that like the most of the interest came much longer.
Like much later yeah to like to the point when it was released so it was hard to predict it back then.
Yeah do you think that an MS leap has to do something with this success that it kind of maybe an MS leap was somewhat visible and then when you edit your algorithm there and show that it performs you know those people who followed this library at least knew. Okay there is a new algorithm.
I think yeah well that helps so when the MS leap is a good library so it has some audience I think the most attention came from and benchmarks. So because yeah well an eye is like what was I had a lot of attention by that point and that benchmark was done by the same person.
Who did an eye so yeah I think that draw some like traffic to the libraries and yeah also I think the idea of algorithm was like understandable and so. So that also like affects the usage so if you understand something you are more likely to use it.
Yeah yeah it's Eric Bernerson right the Swedish guy as he says the sweet who is stuck in New York City yeah I think he implemented a no way originally there is also like a presentation by him where he explains not only the annoy algorithm but also.
 So how intuition doesn't work in multi-dimensional spaces anymore like we think that like in three in 3D world where we leave now right like the further the point away from you like you can actually see it somehow perceive it but like in multi-dimensional space it's not like that I don't know what's your view on that by the way.
So like does geometry perception changes in high dimensional space.
Well yes yes so there are like many interpretations of this so people who work with nearest neighbor search they know about it so like if you have like if you have like many dimensions even small perturbations there they can go like far.
So you all have like so to find nearest neighbor you need to have like a huge cover sphere yeah like when you divide divide the space so yeah that makes the problem complicated and that that one of the reasons why all the practical methods are approximate.
 Right yeah yeah yeah so like you do need some approximation in order to find the points and so yeah I mean it sounds like so when you when you mentioned and then benchmarks was it you who submitted the algorithm for the benchmarks or was it Eric who picked it up and he made it kind of available in the end and benchmarks.
No no I did a full request to edit. All right so it basically yeah yeah so you pushed it forward yourself right so it wasn't like you just implemented and then you waited for it to be discovered so to say.
No yeah definitely so like the one of the like decisions to use in the most sleep was that the most sleep was already integrated in an benchmark so adding that will be just like adding some code in an benchmark that like pulls the algorithm and.
And then the tuning of the parameters so that was but that was simple to do right yeah and so as you did that like what were the results like of that of course an end benchmarks it has a number of parameters right for example like even indexing speed.
Not only like recall versus QPS trade trade off like was there some specific kind of metrics that were hnsw excelled over other algorithms.
Well at that point of time there was like no logging of the construction time and memory consumption and the like the initial version in the most sleep it had like clear focus on the performance like recall to speed ratio.
Yeah and well you know it's hard to do proper benchmarking so like there are a number of scenarios somewhere you have a limit on memory somewhere you have a limit on the construction time sometimes like you don't care about them at all you just care about the speed.
 You can also care about like multi thread performance or you can care about like single thread performance like maybe different scenarios so it's pretty hard to go proper benchmarking and the depth like like I did a decision to just focus on the recall and don't think about construction and memory.
Okay I see yeah and so and and basically when you when you did that like was hnsw like at the top of the competition at that point.
Yes yes it was like a top and on many many benchmarks it was like it was a huge cap compared to the next competitor so not so maybe for a globe I think this Falcon there was still there there was a like significant. Difference yeah but many.
Yeah also like at some point after that there was a real release of key graph algorithm so which like decreased the difference but it was still on top of it.
Yeah so did you did you did it make you feel proud at that moment when you saw the big gap and like this is your invention for how did you feel about it.
Well that felt nice for sure so yeah so we published the paper I think like pop when the paper was finally accepted so it's also felt like really well so I think it took. Like two and a half years to publish the paper well.
As they say in the US I think every rejection brings you closer to the goal so it sounds like you've been rejected in multiple like journals that was not that was still published.
Now that was a single journal it's just like yeah one revision took one year so that is that is palm year so transaction of pattern analyzing a machine intelligence okay.
So like we follow the practice and physics and ignore ignore the conferences so and we also need the for the grants we need to have journal publications not not confidence publication so we sent. To Pamy and had few revisions there but each revision took a year.
Wow this is super long why do you think it was like that like why why would reviewers be so scrutinizing like your submission. Well I don't know so like I actually talked with the editor so I was very angry after the first result so and it seems like just a problem is how.
So publications in computer science are organized so that's that's not only that journal there are so many journals which have. This problem and like when I looked at the Twitter like when some discussions were like oh I got like review invitation for like this like the national journal.
 They said I have to write review in 10 days oh I never gonna do that so no like no way I'm writing a review in 10 days and yeah so in physics it took it sometimes took a few weeks to get the review and journal in journal so you send it and thank you for the months you can already start like writing to review like what what what takes so long yeah and yeah in computer science.
But journals are very slow conferences are also slow there's several months to get the review and like people saw that we are using archive yeah so if there were no archive I think they have already they will just.
 They will create new journals yeah exactly like they should be any monopolies right in that sense like maybe go and create your own journal but then the question is when the problem is when you a PhD student let's say you have a chicken act problem right so you haven't proven yourself yet you need a publication to defend your thesis right so that's the trap.
 Well it's also known how how can this all so if like they created like a new conference conferences like I think I didn't remember I see a lot or I see a lot was created not that long ago they could have created the journal as well yeah the same people said like we don't want to do conferences like conferences you have a very tight deadline that means like if you miss it you'll wait for another year and that is like not not.
Great let's create a journal and now you have a continuous like a spectrum of time when you want to send your paper no deadlines there are no deadlines for reviewers yeah you could almost review yourself.
Yeah I mean like during the review period on the conference you can get like 10 papers at the same time so you have to review them like in a batch but if you are working with journals you get a review like from time to time yeah like your your load is distributed.
 Yeah so by the way what is your take like I think new IPS conference they decided this year they decided to hold all reviews publicly so essentially anybody can see you know the comments from reviewers and there is like a discussion between reviewers and authors and everything is public do you think it improves the process somehow or not what's your take on this.
 Well I think that makes sense so that opens well that sets the bar for reviewers higher because if you know that your review will be read by some random people you want to make it better and spend more time on reading the paper it also helps to understand the review process from outside like for if you're a new reviewer you want to understand how to do proper review you can just read reviews by other people.
 And that is helpful and you can also like if you're if you want to publish a paper you can find similar papers and read the reviews for those papers and understand like why they are rejected or accepted so that that helps I don't see like much problem in that that fights against against the corruption and some places in science are corrupted so.
 Yeah it kind of brings transparency at least with the process and also as you mentioned someone can learn how to do these things right so I think it's also useful and maybe it prevents situations when the paper is rejected outright because the reviewer has some bias against this topic or you know I mean at least transparency is good I think yeah.
Are you publishing today by the way do you have any publishable work do you intend to publish. Not much so I'm working mostly on protection like maybe next year I work on something publishable we are last last thing I published that wasn't some song so for on both estimation.
 Yeah but like I've noticed like you are very active on hnsw github like when I when I posted my question and maybe we can discuss that as well if you are kind of curious on that kind of you responded really fast and so it means that you still continue to allocate chunk of your time to to look at you know issues and pull requests on on github.
Yeah so like I wish I would have done it better so I miss some some things from there but yeah I tried to update this library so I think that well when I designed hnsw so there was some design decisions and even if I see like some algorithms outside improve upon that I think they are not.
Aligned with the design. So and I skip them one of that is like hnsw tries to avoid global view of the network so because it's it's a descendant of. Distributed algorithms so like it's like it's not good strategically if you have like a global view well sometimes it helps.
Like there are papers where you can and that we should make that the pass from the entry point of the network to every node is in short so you can make it but that is that breaks if you're doing assertions for instance so like you cannot have a global view and dynamic nature at the same time.
Yeah so that that's why I ignore some of the stuff there's also a focus on like custom distances so even though the hnsw lip supports only free distances is pretty easy to implement what distances like you want and I believe that there will be a shift in like what distances are being used.
 After some time because there are problems with like those like those simple distances you mean like a sign cosign dot product this type of distances right or yeah yeah it's more a problem that you want to embed everything like you want to embed an entity into a single vector representation so and that has limitations like as you probably know that.
 Like transformers are based on attention and there before there was a like a last year with attention for translation and without attention of didn't work well because it like compressed everything to a single vector so I believe that in some time there will be at least set distances so where your object and query represented as a set of like as a set of which can be shuffled and doesn't change the structure.
 So for a user that can be like set of user interests for a document that can be a set of like subjects inside the document for the query it can be like different parts that you want to have in the query at the same time but those parts like might not be ordered and when you embed something you are that you make it ordered and like for instance when I played with clip.
 So there is this for so I thought that like it can do what's your which is nice so you can like have an image and like see like what are the words are which text is closest but definitely struggles with the notion of like what words are there so what is the first word yeah yeah so like geometrically or like in different languages it might be even different geometry of words right like should you read left to right or right.
Right to left and then like you also need another dimension of language they are guess.
Yeah, we can represent it as like bag of words maybe ordered bag of words is something encoding as all people do now for text but that that I have so I think like an end would need to adapt for the situation in the future and keeping the stability to add new distances is like is important.
Yeah, so are you are you working on on this personally or are you like welcoming pool requests as they say you know to implement different distances. Well, I'm welcoming pool requests for sure because those are very application specific well it's pretty easy to implement like I don't know.
 Or some simple distance so you have like a set a set of distance you just select which are the closest out of the set so it would like many many to many somewhat similar I think to what colder does so though they can I think go without it but essentially you all you'll need a set to set distance right yeah make sense I was since I mentioned it twice already I was wondering like to pick your name.
 I was wondering like to pick your brain on what I was thinking in this space like an and trust me it's absolutely very simple algorithm that I came up with the only problem is that I chose Python as the language and so Python has this little bit weird virtual machine kind of how it does the garbage collection and so what I suspect maybe it's also bugging my code but on billion nodes I cannot actually make it conversion reasonable memory so I'm going to say.
And so it runs out of memory like on 995 million and what I did I was really what like I took the input set of points right so the points are like 128 dimensions or 200 dimensions.
Essentially I pick a random point the first one not not random the first one and then I on a sample of points I compute a median distance right so basically what's what's the kind of average distance between between all of them in a player wise fashion.
 And and so then I use that as as a filter to build what I called a sharp right so essentially I decided to split the billion points down to controllable number of charts let's say 1000 charts right and so I pick the first point and then I say okay which other point is close enough so like within that median distance to this point.
 And so I joined them together in the chart and as the chart reaches 1 million so basically if it's like 1000 charts each chart roughly 1 million points that's a billion points right and then I will close that chart and I will run H and as double you on it so that I can actually have that chart as a hierarchical navigable small world graph.
And and it seems to converge like at least on 10 million it converges on 100 million converges it runs out of memory on one billion but I think it's just some weirdness in how I do it in this big loop or overall points.
But when I reached out to you on on GitHub like my idea was to also access the first layer of the graph so that first layer where the query will enter I could use that.
 And as the sort of entry point across this 1000 charts right so because I don't want to load all 1000 into memory I want to load only sufficient amount of entry points so that I can quickly check which chart is closer to my query and then go inside that and use it as W what do you think about this idea it's very simple I think.
Yes well that that that makes sense so that clustering it seems to be so like you did you have like a cluster the points into 1000 clusters and then they select the clusters and. Well yeah that that makes sense I think like historically there were other papers that suggested something similar to.
And then I think in flam so that was one of the distributors strategies that they suggested. Yeah well that that that might work out so that though that depends on on the scale so and so that also well for production system you also want to replicate those notes and so right.
Okay maybe like let's come from a different way so that you can also start to very small pieces so it might not be needed in this case I can want to balance so but on the top layer you can also use like as in this Microsoft paper that you mentioned also there are other papers like from young so.
So I have a paper this those guys so you can use a in you can start into maybe not the short you can. So if you want to divide your data set into like million clusters and use like a higher index to decide on which chart you want to select it right yes.
So though like if you're if you're not talking about like. So it's not a scale so probably like doesn't make too much sense.
 But yeah yeah you can do this yeah I mean I'm still hopeful to kind of keep trying it I have another friend who is like on Twitter he actually recorded like a YouTube video where he said here here and here you make a mistake like this is why you lose memory like you should never allocate objects inside loops you should pre-allocate them as NAMPA erase and so on.
So with his modifications it still runs out of memory so like I need to kind of move forward and I'm still kind of like hopefully I can do it in Python but something also tells me maybe I should move to more kind of memory controllable language something like rast or C++ I don't know.
 Well I'm not sure so like so using something like so you probably using C++ libraries from Python like NAMPA or torch yeah something like that so they should not click memory so those are pretty pretty controllable yeah yeah it is definitely my code somewhere in the loop it probably just computes too many time like like basically the hottest part of the algorithm like in terms of profiling it right is like.
Like when you can so you pre compute the median distance once right and then you use that value all the time so it's kind of it's okay it's just an object so it doesn't allocate much but then as you extract the next batch of points so I read the one billion set in one million batches right.
I sense that there could be a loss of memory because like it's a binary file and so you say in NAMPA you say from this file read the next batch right so like you you provide the kind of offset and so I sense that maybe there it loses memory maybe not I don't know.
Because I've noticed that in files library they use M M M M M M M M M M M M M. Yeah, I can also use M M M M. So NAMPA if you read the tenser from NAMPA they can also have M M M M M M M options so you can load this M M M M M M M M M M M M M M.
But even if you're using if you're reading we are like open like open file is like read binary it should not click memory so it should it should do read then it's just like.
 Yeah, so it must be something super stupid then in my code that kind of like really obvious to somebody like you like okay Here is here is that point you should not do this But like for me it's like I invented this basic idea But then like pushing it maybe like like it works on 10 million and I'm okay But like the task was as part of this challenge to do the billion scale right so this is like You crawl you crawl the the mountain Without the top in a way, but yes, there is a top of course.
It's only one billion points But yeah, I mean it keeps me quite excited to keep doing it. Of course, I already see some maybe Need for improvements for example.
How how do I make updates?
 Right, so let's say a new point comes in and I have like 1000 charts predefined So I need to find either an existing chart or create a new one at some point So that that part I defer to the future, but like maybe I still need to push push harder to just converge it first Okay, you can profile for memory so we can like loop some operations in the code that you think that can leak and Profile the memory for those Yeah, I've been doing that like actually I also come from the world of Java so in Java it's like Quite straightforward in a way there are also tools in Python when you plug in this memory profiler It slows down your computations significantly and so you have to wait like 10 times more Yeah, so I'm not a fan of profilers so like recently I find I found a video like a talk on YouTube Which explain like why why we shouldn't use profilers and that was like the profilers They become obsolete when the code became like not multi-freaded, but like with multiple paths So when I'm totally this pension so pension was super scholar So your operations are out of order and when you look at the profiler results like I don't understand them so when I was developing a S&S W Libye, I haven't used profilers So I just like wrote benches for operations and And like I had like Faceline and trial so they usually work in the same memory So the like index is the same, but there are different implementations of search and Like your your speed can depend on memory how you allocate the memory and With those benches you can measure something like up to 1 or 2% of difference And when you like do a lot of benches with one or two percent improvement you can get like 20% improvement 50% improvement Yeah, but like I never used profiles and like I never saw like in my life that people use profiles and like get really complicated insights from using profiles Yeah, I agree like we we did like so we're building also building a search engine With like we had like by design we had like billions of documents and each document was just a short sentence like a statement from a document real document And of course we were running out like we were running into all this garbage collector stop the world problems and so on and we were running this Profilers, I think one of them was J rocket and then others and like when you see the graphs you're like, okay So now I know yes it leaks, but what should I do?
So or it tells you that your code is using like Biterase too much like what can you do other than that? Yeah, and for performance it's even worse.
So you see that like this model takes a lot of time, but The in a multi multi threaded world that like it's not for sure.
 So you may improve it that Like and that happened so quite quite quite a few times so people went to me and said like You're analysis of performance contradictory Profile blocks And that's okay, right because you didn't optimize for the profiler Yeah, because profiler cannot like so it cannot say to you what would happen if you change something Exactly, it's just a snapshot.
Yeah, it's just a snapshot.
Yeah, exactly And and like coming back to hsw what are you hoping to achieve like Maybe in some midterm future for example like Why do you decide at work which where the reimplementation as w is when they add symbolic filtering?
So like what would it take in your original paper in your original algorithm to add symbolic filters? How does it change the dynamic of that graph and search?
 Uh, well, it seems like for me like so I can correlate interest to and then and interest to symbolic filtering So like I think two years ago I haven't heard like people talk about symbolic filtering in an but now like it's a hot topic Like from different places people want symbolic filtering that is like for targeting So like for ads.
 Yeah, you can you want to have some targeting for the audience or some other filters and But I see that as outside of the end and itself so As I said when working on a startup so our first application was Doing something like symbolic filtering and there it's easier in some sense because Like as you said there is a problem of this distances and high-dimensional space and this problem There is no such problem in symbolic filtering So symbolic filtering you have a query that have exact result and yeah, if you write the SQL query So it can be optimized to work efficiently and but the iNM does a very different job.
It does approximate Yeah filtering We can kind of mix them together.
 So if you add like so you have a distance and like you add some Like prefix for that which somehow captures the symbolic filtering and you can build an index that also like takes Takes account and like there are some other people who suggested to do that as well But the problem here like and yeah, that can help so during search So if you filter by the symbol and like you can easily add filtering so when hnsw does filtering for deletes like can be done the same way Yeah, you can extract Like only elements that pass the filter and there is some like guidance on the graph because you create that wizard But for me like I don't know so you have like huge number of possible filters So what will be the metric and how would you balance it with the like approximate network that creates a lot of problems I think yeah, and I I thought that the best solution would be like to keep this like to some extent But focus more on like how do you can chart the index according to those like Great theory don't that there are sharp.
 So you can like do SQL queries like for instance Like there are some queries that can Work well with this filtering Like if you're most of like or like I don't know 20% of the elements pass the symbolic filter So that is fine you can use it But maybe there are some queries for which like I know only like one of a million passes them and those are in different parts Yeah exactly space So for them you can Uh See in real time.
 So you like you search and you see that it doesn't perform well Uh for those and you can just Build the separate index for them right because you know those are small those are people want to find them Uh, maybe there are enough maybe they're out of a billion, but if you have three LN elements, so there's like a million of them So you you you cash them like build a cash index For those on the fly so that is like discrete optimization problem And I think that's a bit outside of the index because index is like Uh Yeah, so it's focused on the different part.
Yeah Yeah, and I really I don't think that other algorithms like and an algorithms can like somehow avoid this problem Yeah exactly.
 Yeah, I mean it sounds yeah, what would you say like you find a stunt correctly Like a little bit like a and then contradicts Just kind of the nature of symbolic filtering in some sense, but still people do it right so for example in VEV8 And in quadrant they did it right so like you and in milbus as well, but it's funny like in milbus they use Fies and then other algorithms, right, but they say we only support you know integer Fields, but we don't support for example strings yet So we are working on adding strings which means essentially they're designing like This graph somehow in such a way that okay, it doesn't support strings yet Maybe because it's not so easy To to to to to edit right Well, I I'm not sure so that also depends how you measure the performance like if you have rare queries That switch the rich don't have any result.
 So like you pro like your algorithm doesn't even work on them But you either are rare to you measure the like overall recall and you don't see it like any problems So definitely you can build the solution maybe like some simple with like filtering during search but like It sure it will fail on some points and that is suboptimal in terms of latency Yeah, so if you if you're talking about existing solution Maybe they have like a really good solution, which I just don't know I looked at few Uh, and that was mostly like filtering inside the graph So like if you if you if you if you have really rare elements which are like distributed across the search space Evenly like in different parts.
So it will struggle Because you need to just do brute force of the whole to find them.
Yeah, exactly I mean to me it sounds like computerial explosion like if I add more and more symbolic filters Like essentially I'm introducing like new sub spaces in my space, right?
So like I need to like push these points somehow closer to each other within that specific symbolic filter But if I add more of them now I have like kind of like multi-dimensional space of filters, right?
 Yeah, and you you have a really high dimensional space of filters But you don't really know like the distribution of queries For those filters it should be very different because those are user distribution Yeah, so that also will make the problem more complicated So it still can work if you if the especially if distribution is kind of similar So it will work if you crank up the parameters of the graph Yeah, use more connections But so there is a mismatch so during query your distribution may be very different and you need to think about it So like How you balance those inside so you have like two types of distance and how you balance them You want to balance it so the the query distribution Yeah That's that's that's this field like I think this field of vector search doesn't make you excited that you you contributed to it Like how do you feel about this field that is emerging right now?
 Well, I think it is very important so right now I'm working mostly on applications how to Like get advantage of this and so there are many applications Which cannot be done without efficient search like there was a paper for deep mind Like was quite recently where they used search Uh like inside of the network and uh well That makes a lot of sense And I think Yeah, there will be more papers and that there were papers before that paper But there will be more papers that use an M inside the inside the big like a huge nal p model Yeah, yeah, for example like this uh learning to hash methods I don't know if you heard about them So like um there are like when I when I tried to kind of Put everything into their buckets like how many different types of algorithms exist Like I didn't know about learning to hash.
 It seems to be like one of the recent uh developments Are you following up on that as well or uh Well learning to hash so like I'm not really following that so learning to hash was before hnsw Okay, there are algorithms And uh when I talked with people who did like were specialized on product quantization and review the papers Uh, they told me that like learning to hash never reaches the performance of like post quantization Like at least at what that was like a few years ago Yeah, and uh yeah, maybe like Now it's solved Uh, but like when I talk about an n Inside the i think about like about graph in it So yeah, yeah, and Yeah, and uh So one interesting thing also can happen uh like with graphs So what what like what is an additional advantage of graph uh nearest neighbors to your engines is that you can change the metric Uh, so For instance if you are doing multi-stage ranking Like the You have like and you have multiple candidate sources like for search you have something like like like the m25 Also you might have embeddings like with similarity search So uh, and those are like three that are separate sources and then ranked Uh, but essentially like why do you need an n like for the first like from from the beginning Uh, you need an n to speed up the ranking So essentially you can rank all the documents using your have a ranker Uh, but uh you cannot it's to like to expensive to do so you can add an n and n is basically for vector search uh that is you Distill everything to vectors and you have the same objective and you have like a Like a way to Sparsify the interactions Uh, but you can look about the other way so you know you have a graph and the graph are just the Candidates and you have like a low simple metric now you have More complicated metric on this graph and you have like a final ranking that also can be searched on this graph So that means you don't supply Like a set of candidates to the ranking, but rather you supply interpoints in the graphs So you have a graph which is uh, well Which is built a trying to uh uh Capture the uh similarity for the ranker and uh like when you so instead of filtering like from one stage to the next stage You can uh just switch the metric in the graph.
 You had light metric, which is like vectors now you have more complicated metrics So you hydrate the features of the elements in the graph and like Traverse and like now you have a really complicated metric Which yeah, like you just very heavy, but you still you just have an interpoint in the graph.
So you explore it and you can Uh, well, you can fix some mistakes done by the previous layers. Yeah, so it's not exact filtering. So that's yeah, that's another like Maybe unique The feature of the graph methods.
 Yeah, sounds quite exciting like Have you have you thought about publishing this idea or like I mean it sounds quite quite unique Well, it doesn't make sense to publish an idea without implementation Yeah, for sure, but maybe you can influence those who who would like to Experiment on it At least those who will watch this podcast.
I think they will listen.
They will they will probably pick it up Yeah, and use graph algorithms for sure Like Yeah, I mean it sounds like all all of the NN algorithms they have Like advantages and disadvantages, right?
So it's not like the all of them are uniquely Outperforming, you know the others Well, there is like a division like if you think about like quantization algorithms.
So they are kind of orthogonal to Graph algorithms. So they They quantize so they can speed up a compressed like I'm compressed to save the memory and speed up the computation But like older algorithm they just use something like IVF.
 So And then like one layer filtering and you can use graphs instead of IVF Right, so we can use graphs and add the quantization and at the Faiz did that before Yeah, I think some others also did that Yeah, and the thing and then like vector databases actually offer it as one method like like Milvus for example like they offer IVF and then you can choose like if you want to do exact K&N or if you want to do A&N So you can actually configure it in different ways Yeah, I mean just sounds like you're Without maybe realizing much like you are at the core of what's happening in vector search in some sense Of course, there have been other multiple contributions, right?
But like For some reason exactly your algorithm has been picked by many vector databases There are like seven of them.
 So actually wrote a blog about Six of them and then seventh kind of knocked on my door and said can you also add at us And so when I when I was going through different databases like in Java implemented in Java or in in Python or you know in Rust and go All of them picked your algorithm for some reason So like maybe it was easier like it's a combination of how easy it is to implement how transparent it is like to understand right and then basically it's stability.
 So it's like a combination of things Yeah, probably like I'm not totally sure So yeah, the initial library also was implemented as a header on the well, not the initial so that was a second library So there there was a problem with HNW lippen implementation and NMS lip So it so like the NMS lip format was a bit restrictive Like for efficient operation.
So it converted it to Flat memory format and so that that That makes made construction slower and memory can sub-share bigger.
 So was re-implemented as I had a wrongly library So header on the library was inspired by an I So like by the success also and I Think that also might have contributed because it's very easy to like integrate it So there are a few files it compiles in some seconds Yeah, no Maybe maybe also that help So the library itself is simple and easy to integrate Yeah, yeah And I mean it must feel kind of cool to have this impact But but I also I also hope like you you will continue kind of Maybe doing some publishable publishable work in some fashion and doesn't need to be a journal Which is rejected five times but something else Is this something that you are planning to do or Uh, well that depends so like I cannot talk too much about my work in Twitter.
So So Maybe maybe we will publish something so that that depends on how it goes. I mean, I'm near even nearest neighbors.
 Yeah, not not only but yeah But I it's hard to predict now if it works well So that then publish yeah, at least the idea that you mentioned like I mean if you if it's outside Twitter for example in hnsw Your library like the idea of this multistage ranking sounds quite exciting Um, uh, well, I think it can be implemented only by the teams who own the rankers and all the whole pipeline Yes, true.
I think it can be implemented as like As I think you need to hide ha you need to hydrate the features and like yeah on the fly and have feature hydration is very specific to application Yeah, but not only inside the production environment Yeah, that makes sense.
Yeah, uh, so maybe it will call for creation of data sets and kind of this benchmarks if the industry chooses to move in that direction Well, like there are some obvious problems with data privacy With that so it's hard to publish something Well, you can think of a toy problem.
 So like you have like you don't do actual like work with users, but maybe We do image to image search and you have like a huge transformer model On top of that or maybe like something like marco Emma smart car maybe it can be done with that like experimented Hmm, maybe so Yeah Yeah, I think we weren't really deep today.
 You really I think it was really really cold cold talking to you I always like to still ask Kind of this question orthogonal question of why like it's a little bit more philosophical But like if you're not a verse Of philosophy like why Would you say like this field attracted you like in your own words?
Uh I didn't have much choice.
 It just was like I I got my first job offer and that was In this field That's that's about scale so like people like scaling and like many games when you play on like android or other stuff They're based on scaling so you do like a little action and there are like huge consequences of those actions like destroying something or Like and that is scaling and uh, this is just like a pure scale of how how how we scale machine learning Applications Yeah, so on on one hand it kind of was predefined as you said you found the job on the other hand You still were curious to implement that algorithm.
So like it wasn't like somebody said okay You have to do it right you could also choose a job of like okay. I'm just coding nine to five and then I go home But like you still decided to implement an algorithm Well, yes, well that that was a fun job.
So Yeah, so like you were not scared by the challenge itself, right? Maybe was it like motivating actually There was no like that much push like from the like From from the company itself.
 So we could we could do whatever we want inside the company So it was very like relaxed Yeah, that might be actually a really good background to invent things Don't you think like if if you if you come to work and somebody says no, you cannot do what you want You should do this and it might be kind of too restrictive But here like they've been both challenges and also that freedom to solve those challenges Yeah, there are like two components first of all you need to have like Freedom and do long long term stuff.
So like without worrying or like what are you going to ship into production soon?
The second is concentration of talent So you have like high concentration of talent so people can Share ideas Yeah, if you have this mix so like there will there will be innovations for sure Yeah, it sounds like you had a combination of all three components that you mentioned, right?
So like talents and also yeah Yeah, yeah, I also saw that another company is like Yeah, like in Samsung there was already a strong team and there were like lots of innovation.
 So there are a few startups Uh, which came from our lab and there was like a really good paper Yeah, so that that that's a that's a recipe for innovation for sure Yeah, yeah, I'm really happy that it turned out so well to you for you and uh your author as well I think he continues to work also in the industry at least last time I checked um, and so I I really hope that You will get some really cool pull requests on hnsw that will pass your criteria Well, yeah, most of them pass is just like I Would love to have more time and I'll try to allocate more time Yeah, looking and checking them Yeah, it's really really great.
I really enjoyed talking to you Yuri.
 Um, thanks so much for allocating your time also in this Precreasement time um, but yeah, I mean all the best to you in in the future also twitter and uh Hope to see some published work at some point, but I don't know it just uh, I enjoyed reading your paper and and Kind of also then read read your code and it's kind of like It feels like you've put a lot of effort there and and It uh, it also influences the industry so much today So maybe you are not kind of realizing this every single day, but like Yeah, you should know this that there are so many databases that use your algorithm as as one of the baseline's in production It's really cool work Yeah, yeah, that that that that that was great that There was success Yeah, maybe one thing like I would note uh That the idea was the rain cares.
 So that was partially implemented and there needs work So he had a work on ER maybe you know like by using the And then as the for the final rain care So Yeah, it's just like so I felt that I need to cite this sure I need work for sure I learned this idea like maybe not was changing, but from from him Yeah, yeah, it sounds great.
 I mean, I've also interacted a bit with him uh and and it sounds like he's very knowledgeable guy And he has very strong opinions as well So maybe we will also talk with him on one of the episodes Uh, but um, yeah, I'm glad that you guys collaborated Yeah, it's it's a fantastic result for for the industry as well And and probably for your profiles well not probably but definitely for your profiles So yeah, um, thank you so much for your time and um, yeah, I hope you will have a relaxing time over the Christmas and Happy new year as well So thank you very much for your time Yuri Thank you Yeah, bye bye Um