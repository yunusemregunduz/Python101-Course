Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> if x > 0 :
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    if x > 0 :
NameError: name 'x' is not defined
>>> if x > 0:
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    if x > 0:
NameError: name 'x' is not defined

>>> x = 0
       if x > 0:
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")
	
SyntaxError: multiple statements found while compiling a single statement
>>> x = 0
       if x > 0:
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")
	
SyntaxError: multiple statements found while compiling a single statement
>>> x = 0:
       if x > 0:
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")
	
SyntaxError: invalid syntax
>>> 
>>> x = 0
>>> if x > 0:
	print("it is positive")
elif x == 0:
	print ("it is zero")
else :
	print (" it is not possitive")

	
it is zero
>>> number = 2.0
>>> if type(number) == int:
	if number > 0:
		print("it is a possitive integer number")
	elif number == 0:
		print("it is zero")
	else:
		print("it is a negative integer number ")
else:
	print("this number is not a int.")

	
this number is not a int.
>>> 
>>> 
>>> 
>>> x = 1
>>> x
1
>>> x ++ 5
6
>>> x
1
>>> 
>>> x += 5
>>> x
6
>>> x ++6
12
>>> x = x+5
>>> x
11
>>> n =5
while n>0:
	print(n)
	n -= 2
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> while n>0:
	print(n)
	n -= 2

	
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    while n>0:
NameError: name 'n' is not defined
>>> n = 28
>>> while n > 0:
	print (n)
	n -= -4

	
28
32
36
40
44
48
52
56
60
64
68
72
76
80
84
88
92
96
100
104
108
112
116
120
124
128
132
136
140
144
148
152
156
160
164
168
172
176
180
184
188
192
196
200
204
208
212
216
220
224
228
232
236
240
244
248
252
256
260
264
268
272
276
280
284
288
292
296
300
304
308
312
316
320
324
328
332
336
340
344
348
352
356
360
364
368
372
376
380
384
388
392
396
400
404
408
412
416
420
424
428
432
436
440
444
448
452
456
460
464
468
472
476
480
484
488
492
496
500
504
508
512
516
520
524
528
532
536
540
544
548
552
556
560
564
568
572
576
580
584
588
592
596
600
604
608
612
616
620
624
628
632
636
640
644
648
652
656
660
664
668
672
676
680
684
688
692
696
700
704
708
712
716
720
724
728
732
736
740
744
748
752
756
760
764
768
772
776
780
784
788
792
796
800
804
808
812
816
820
824
828
832
836
840
844
848
852
856
860
864
868
872
876
880
884
888
892
896
900
904
908
912
916
920
924
928
932
936
940
944
948
952
956
960
964
968
972
976
980
984
988
992
996
1000
1004
1008
1012
1016
1020
1024
1028
1032
1036
1040
1044
1048
1052
1056
1060
1064
1068
1072
1076
1080
1084
1088
1092
1096
1100
1104
1108
1112
1116
1120
1124
1128
1132
1136
1140
1144
1148
1152
1156
1160
1164
1168
1172
1176
1180
1184
1188
1192
1196
1200
1204
1208
1212
1216
1220
1224
1228
1232
1236
1240
1244
1248
1252
1256
1260
1264
1268
1272
1276
1280
1284
1288
1292
1296
1300
1304
1308
1312
1316
1320
1324
1328
1332
1336
1340
1344
1348
1352
1356
1360
1364
1368
1372
1376
1380
1384
1388
1392
1396
1400
1404
1408
1412
1416
1420
1424
1428
1432
1436
1440
1444
1448
1452
1456
1460
1464
1468
1472
1476
1480
1484
1488
1492
1496
1500
1504
1508
1512
1516
1520
1524
1528
1532
1536
1540
1544
1548
1552
1556
1560
1564
1568
1572
1576
1580
1584
1588
1592
1596
1600
1604
1608
1612
1616
1620
1624
1628
1632
1636
1640
1644
1648
1652
1656
1660
1664
1668
1672
1676
1680
1684
1688
1692
1696
1700
1704
1708
1712
1716
1720
1724
1728
1732
1736
1740
1744
1748
1752
1756
1760
1764
1768
1772
1776
1780
1784
1788
1792
1796
1800
1804
1808
1812
1816
1820
1824
1828
1832
1836
1840
1844
1848
1852
1856
1860
1864
1868
1872
1876
1880
1884
1888
1892
1896
1900
1904
1908
1912
1916
1920
1924
1928
1932
1936
1940
1944
1948
1952
1956
1960
1964
1968
1972
1976
1980
1984
1988
1992
1996
2000
2004
2008
2012
2016
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
2120
2124
2128
2132
2136
2140
2144
2148
2152
2156
2160
2164
2168
2172
2176
2180
2184
2188
2192
2196
2200
2204
2208
2212
2216
2220
2224
2228
2232
2236
2240
2244
2248
2252
2256
2260
2264
2268
2272
2276
2280
2284
2288
2292
2296
2300
2304
2308
2312
2316
2320
2324
2328
2332
2336
2340
2344
2348
2352
2356
2360
2364
2368
2372
2376
2380
2384
2388
2392
2396
2400
2404
2408
2412
2416
2420
2424
2428
2432
2436
2440
2444
2448
2452
2456
2460
2464
2468
2472
2476
2480
2484
2488
2492
2496
2500
2504
2508
2512
2516
2520
2524
2528
2532
2536
2540
2544
2548
2552
2556
2560
2564
2568
2572
2576
2580
2584
2588
2592
2596
2600
2604
2608
2612
2616
2620
2624
2628
2632
2636
2640
2644
2648
2652
2656
2660
2664
2668
2672
2676
2680
2684
2688
2692
2696
2700
2704
2708
2712
2716
2720
2724
2728
2732
2736
2740
2744
2748
2752
2756
2760
2764
2768
2772
2776
2780
2784
2788
2792
2796
2800
2804
2808
2812
2816
2820
2824
2828
2832
2836
2840
2844
2848
2852
2856
2860
2864
2868
2872
2876
2880
2884
2888
2892
2896
2900
2904
2908
2912
2916
2920
2924
2928
2932
2936
2940
2944
2948
2952
2956
2960
2964
2968
2972
2976
2980
2984
2988
2992
2996
3000
3004
3008
3012
3016
3020
3024
3028
3032
3036
3040
3044
3048
3052
3056
3060
3064
3068
3072
3076
3080
3084
3088
3092
3096
3100
3104
3108
3112
3116
3120
3124
3128
3132
3136
3140
3144
3148
3152
3156
3160
3164
3168
3172
3176
3180
3184
3188
3192
3196
3200
3204
3208
3212
3216
3220
3224
3228
3232
3236
3240
3244
3248
3252
3256
3260
3264
3268
3272
3276
3280
3284
3288
3292
3296
3300
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    print (n)
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while n > 0:
	print (n)
	n -= 5

	
3300
3295
3290
3285
3280
3275
3270
3265
3260
3255
3250
3245
3240
3235
3230
3225
3220
3215
3210
3205
3200
3195
3190
3185
3180
3175
3170
3165
3160
3155
3150
3145
3140
3135
3130
3125
3120
3115
3110
3105
3100
3095
3090
3085
3080
3075
3070
3065
3060
3055
3050
3045
3040
3035
3030
3025
3020
3015
3010
3005
3000
2995
2990
2985
2980
2975
2970
2965
2960
2955
2950
2945
2940
2935
2930
2925
2920
2915
2910
2905
2900
2895
2890
2885
2880
2875
2870
2865
2860
2855
2850
2845
2840
2835
2830
2825
2820
2815
2810
2805
2800
2795
2790
2785
2780
2775
2770
2765
2760
2755
2750
2745
2740
2735
2730
2725
2720
2715
2710
2705
2700
2695
2690
2685
2680
2675
2670
2665
2660
2655
2650
2645
2640
2635
2630
2625
2620
2615
2610
2605
2600
2595
2590
2585
2580
2575
2570
2565
2560
2555
2550
2545
2540
2535
2530
2525
2520
2515
2510
2505
2500
2495
2490
2485
2480
2475
2470
2465
2460
2455
2450
2445
2440
2435
2430
2425
2420
2415
2410
2405
2400
2395
2390
2385
2380
2375
2370
2365
2360
2355
2350
2345
2340
2335
2330
2325
2320
2315
2310
2305
2300
2295
2290
2285
2280
2275
2270
2265
2260
2255
2250
2245
2240
2235
2230
2225
2220
2215
2210
2205
2200
2195
2190
2185
2180
2175
2170
2165
2160
2155
2150
2145
2140
2135
2130
2125
2120
2115
2110
2105
2100
2095
2090
2085
2080
2075
2070
2065
2060
2055
2050
2045
2040
2035
2030
2025
2020
2015
2010
2005
2000
1995
1990
1985
1980
1975
1970
1965
1960
1955
1950
1945
1940
1935
1930
1925
1920
1915
1910
1905
1900
1895
1890
1885
1880
1875
1870
1865
1860
1855
1850
1845
1840
1835
1830
1825
1820
1815
1810
1805
1800
1795
1790
1785
1780
1775
1770
1765
1760
1755
1750
1745
1740
1735
1730
1725
1720
1715
1710
1705
1700
1695
1690
1685
1680
1675
1670
1665
1660
1655
1650
1645
1640
1635
1630
1625
1620
1615
1610
1605
1600
1595
1590
1585
1580
1575
1570
1565
1560
1555
1550
1545
1540
1535
1530
1525
1520
1515
1510
1505
1500
1495
1490
1485
1480
1475
1470
1465
1460
1455
1450
1445
1440
1435
1430
1425
1420
1415
1410
1405
1400
1395
1390
1385
1380
1375
1370
1365
1360
1355
1350
1345
1340
1335
1330
1325
1320
1315
1310
1305
1300
1295
1290
1285
1280
1275
1270
1265
1260
1255
1250
1245
1240
1235
1230
1225
1220
1215
1210
1205
1200
1195
1190
1185
1180
1175
1170
1165
1160
1155
1150
1145
1140
1135
1130
1125
1120
1115
1110
1105
1100
1095
1090
1085
1080
1075
1070
1065
1060
1055
1050
1045
1040
1035
1030
1025
1020
1015
1010
1005
1000
995
990
985
980
975
970
965
960
955
950
945
940
935
930
925
920
915
910
905
900
895
890
885
880
875
870
865
860
855
850
845
840
835
830
825
820
815
810
805
800
795
790
785
780
775
770
765
760
755
750
745
740
735
730
725
720
715
710
705
700
695
690
685
680
675
670
665
660
655
650
645
640
635
630
625
620
615
610
605
600
595
590
585
580
575
570
565
560
555
550
545
540
535
530
525
520
515
510
505
500
495
490
485
480
475
470
465
460
455
450
445
440
435
430
425
420
415
410
405
400
395
390
385
380
375
370
365
360
355
350
345
340
335
330
325
320
315
310
305
300
295
290
285
280
275
270
265
260
255
250
245
240
235
230
225
220
215
210
205
200
195
190
185
180
175
170
165
160
155
150
145
140
135
130
125
120
115
110
105
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
>>> while n > 0:
	print (n)
	n -= 5

	
>>> # can U explain why it finished the counting when it came to 5 ??
>>> n = 10
>>> while True:
	print(n, end = " ")
	n = n -  1
print("done")
SyntaxError: invalid syntax
>>> while True:
	print(n, end = " ")
	n = n - 1

	
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36 -37 -38 -39 -40 -41 -42 -43 -44 -45 -46 -47 -48 -49 -50 -51 -52 -53 -54 -55 -56 -57 -58 -59 -60 -61 -62 -63 -64 -65 -66 -67 -68 -69 -70 -71 -72 -73 -74 -75 -76 -77 -78 -79 -80 -81 -82 -83 -84 -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95 -96 -97 -98 -99 -100 -101 -102 -103 -104 -105 -106 -107 -108 -109 -110 -111 -112 -113 -114 -115 -116 -117 -118 -119 -120 -121 -122 -123 -124 -125 -126 -127 -128 -129 -130 -131 -132 -133 -134 -135 -136 -137 -138 -139 -140 -141 -142 -143 -144 -145 -146 -147 -148 -149 -150 -151 -152 -153 -154 -155 -156 -157 -158 -159 -160 -161 -162 -163 -164 -165 -166 -167 -168 -169 -170 -171 -172 -173 -174 -175 -176 -177 -178 -179 -180 -181 -182 -183 -184 -185 -186 -187 -188 -189 -190 -191 -192 -193 -194 -195 -196 -197 -198 -199 -200 -201 -202 -203 -204 -205 -206 -207 -208 -209 -210 -211 -212 -213 -214 -215 -216 -217 -218 -219 -220 -221 -222 -223 -224 -225 -226 -227 -228 -229 -230 -231 -232 -233 -234 -235 -236 -237 -238 -239 -240 -241 -242 -243 -244 -245 -246 -247 -248 -249 -250 -251 -252 -253 -254 -255 -256 -257 -258 -259 -260 -261 -262 -263 -264 -265 -266 -267 -268 -269 -270 -271 -272 -273 -274 -275 -276 -277 -278 -279 -280 -281 -282 -283 -284 -285 -286 -287 -288 -289 -290 -291 -292 -293 -294 -295 -296 -297 -298 -299 -300 -301 Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    print(n, end = " ")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line == "done" :
		break
	print(line)

	
>

>while True:
	line = input("hacı sen bu işi biliyon ya :D")
	if line == "done" :
		break
	print(line)
while True:
>	line = input("hacı sen bu işi biliyon ya :D")
>	if line == "done" :
>		break
>	print(line)
>

>

>while True:
	line = input("hacı sen bu işi biliyon ya :D")
	if line == "done" :
		break
	print(line)
while True:
>	line = input("hacı sen bu işi biliyon ya :D")
>	if line == "done" :
>		break
>	print(line)
>

>

>

>
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    line = input(">")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1394, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> while True:
	line = input("hacı sen bu işi biliyon ya :D")
	if line == "done" :
		break
	print(line)

	
hacı sen bu işi biliyon ya :D

hacı sen bu işi biliyon ya :D
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    line = input("hacı sen bu işi biliyon ya :D")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1394, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> # tamam dostum abartma :D
>>> import time
>>> i = 1
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	      i += 1
	      
SyntaxError: invalid syntax
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	i += 1
	      
SyntaxError: invalid syntax
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	i += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	i += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	k += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	2 += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	 i += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	i += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> i = 1
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]"
	i += 1
	      
SyntaxError: invalid syntax
>>> import time
>>> i = 1
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]")
	i += 1
	time.sleep(2)

	
welcome 1 times. To stop press [CTRL+C]
welcome 2 times. To stop press [CTRL+C]
welcome 3 times. To stop press [CTRL+C]
welcome 4 times. To stop press [CTRL+C]
welcome 5 times. To stop press [CTRL+C]
welcome 6 times. To stop press [CTRL+C]
welcome 7 times. To stop press [CTRL+C]
Traceback (most recent call last):
  File "<pyshell#101>", line 4, in <module>
    time.sleep(2)
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]")
	i += 1
	time.sleep(10)

	
welcome 8 times. To stop press [CTRL+C]
welcome 9 times. To stop press [CTRL+C]
Traceback (most recent call last):
  File "<pyshell#103>", line 4, in <module>
    time.sleep(10)
KeyboardInterrupt
>>> while True:
	print("welcome", i, "times. To stop press [CTRL+C]")
	i += 1
	time.sleep(-5)

	
welcome 10 times. To stop press [CTRL+C]
Traceback (most recent call last):
  File "<pyshell#105>", line 4, in <module>
    time.sleep(-5)
ValueError: sleep length must be non-negative
>>> # i just try :D
>>> 
>>> # i just try :D
>>> while True:
	line = input (">><<")
	if line [0] == "#":
		continue
	if line == "done ":
		break

	
>><<
Traceback (most recent call last):
  File "<pyshell#115>", line 3, in <module>
    if line [0] == "#":
IndexError: string index out of range
>>> while True:
	line = input (">><<")
	if line [0] == "#":
		continue
	if line == "done ":
		break
	print(line )

	
>><<
Traceback (most recent call last):
  File "<pyshell#118>", line 3, in <module>
    if line [0] == "#":
IndexError: string index out of range
>>> 
>>> 
>>> while True:
	line = input (">><<")
	if line [5] == "#":
		continue
	if line == "done ":
		break
	print(line )

	
>><<
Traceback (most recent call last):
  File "<pyshell#122>", line 3, in <module>
    if line [5] == "#":
IndexError: string index out of range
>>> 
>>> 
>>> while True:
	line = input (">><<")
	if line [1000000] == "#":
		continue
	if line == "done ":
		break
	print(line )

	
>><<
Traceback (most recent call last):
  File "<pyshell#126>", line 3, in <module>
    if line [1000000] == "#":
IndexError: string index out of range
>>> 
>>> 
>>> # i did not understan how did U get numbers? when did U input number ??
>>> # enes kemal
>>> 
>>> 
>>> while True:
	line = input (">><<")
	if line [1000000] == "#":
		continue
	if line == "done ":
		break
	print(line )

	
>><<#will it print this line ?
Traceback (most recent call last):
  File "<pyshell#134>", line 3, in <module>
    if line [1000000] == "#":
IndexError: string index out of range
>>> 
>>> 
>>> for i in "Python":
	print(i, end = "-")

	
P-y-t-h-o-n-
>>> for i in "Python":
	print(i, end = "55")

	
P55y55t55h55o55n55
>>> for i in "Python":
	print(i)

	
P
y
t
h
o
n
>>> for i in "Python":
	print(i, end = /n)
	
SyntaxError: invalid syntax
>>> 
>>> for i in "Python":
	print(i, /n)
	
SyntaxError: invalid syntax
>>> 
>>> for i in "Python":
	print(i, n)

	
P -301
y -301
t -301
h -301
o -301
n -301
>>> for i in "Python":
	print(i, y)

	
Traceback (most recent call last):
  File "<pyshell#152>", line 2, in <module>
    print(i, y)
NameError: name 'y' is not defined
>>> y= 10
>>> for i in "Python":
	print(i, y)

	
P 10
y 10
t 10
h 10
o 10
n 10
>>> for i in "Python":
	print(i, y, \n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y, \n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y,\n n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y,\n n):
		
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y)

	
P 10
y 10
t 10
h 10
o 10
n 10
>>> for i in "Python":
	print(i, y,\n n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y)

	
P 10
y 10
t 10
h 10
o 10
n 10
>>> for i in "Python":
	print(i, y, n)

	
P 10 -301
y 10 -301
t 10 -301
h 10 -301
o 10 -301
n 10 -301
>>> for i in "Python":
	print(i, y, /n n)
	
SyntaxError: invalid syntax
>>> 
>>> for i in "Python":
	print(i, y, \n n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y, \n n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in "Python":
	print(i, y,  n)

	
P 10 -301
y 10 -301
t 10 -301
h 10 -301
o 10 -301
n 10 -301
>>> type (4)
<class 'int'>
>>> 
>>> type (45454
      654564
      
SyntaxError: invalid syntax
>>> type (45454
      654564)
SyntaxError: invalid syntax
>>> type (45454
654564)
SyntaxError: invalid syntax
>>> type (45454
654564):
	
SyntaxError: invalid syntax
>>> type (454545456445555555555555555555555555555555555555555555555555555555555555555555555555)
<class 'int'>
>>> type (454545)
<class 'int'>
>>> type ( yunus )
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    type ( yunus )
NameError: name 'yunus' is not defined
>>> yunus = 78
>>> type ( yunus )
<class 'int'>
>>> 
