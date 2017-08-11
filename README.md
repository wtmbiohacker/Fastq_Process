# 说明
LEADING_quality   read5‘端trim的threshold
TRAILING_quality  read3’端trim的threshold
MINLEN            过滤时read的最短长度
Maxlength	  过滤时read的最大长度
forwardFastq      pair-end reads的right的fastq file
reverseFastq      pair-end reads的left的fastq file
mismatch          merge时允许的错配的比率。
overlap           merge时pair-end的最大重叠长度
prefix            merge时输出文件的名字
path              输出文件的路径（如果不加这一项，script会自己在当前工作目录下创建一个results文件夹，然后所有的输出文件都会被输出到这个文件夹中。）
没有path这一项的命令：
python ~/Desktop/process_the_raw_data/NGS_main.py 25 25 120 155 r0-C1R1-s0_L1_1.clean.fq r0-C1R1-s0_L1_2.clean.fq 0.02 149 r0-C1R1-s0 
有path这一项的命令
python ~/Desktop/process_the_raw_data/NGS_main.py 25 25 120 155 r0-C1R1-s0_L1_1.clean.fq r0-C1R1-s0_L1_2.clean.fq 0.02 149 r0-C1R1-s0 ~/Desktop/results/

(python ~/Desktop/process_the_raw_data/NGS_main.py LEADING_quality TRAILING_quality MINLEN Maxlength forwardFastq reverseFastq mismatch overlap prefix)
