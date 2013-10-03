sickle_team8
============


Aim
============
Our goal is to allow the user to cut not only based on when the mean value of a window falls below a threshold, but also when the standard deviation or variance of the quality scores in a window exceeds some threshold.

The first step we propose to accomplish, is produce a table that the user can use as a guide to set his/hers threshold values:

|WindowPosition|MeanQuality|SDQuality|
| ------------ | --------- | ------- |
|1|35|2.57|
|2|37|2.89|
|3|38|3.00|
...
|15|20|10.00|
|16|15|11.22|

How to use
=============
python parse_fastq.py [fastq file] [window size] [offset]

Output should be a summary file called fastq_summary_stats.csv which contains a comma separated table with window position, mean quality score and standard deviation
