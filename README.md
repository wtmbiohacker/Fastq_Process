# 脚本说明(本脚本是用来对pair-end二代测序数据进行预处理，第一步对pair-end read进行合并，然后再对合并后的single end read进行trim和过滤)
#脚本需要输入的参数说明
LEADING_quality   read5‘端trim的threshold（一般选择25，前端的base质量值低于25的base会被去掉）
TRAILING_quality  read3’端trim的threshold（一般选择25，尾端的base质量值低于25的base会被去掉）
MINLEN            过滤时read的最短长度（如果read中base的质量很低导致read被trim后的长度太短低于这个threshold值，该read就被丢弃）
Maxlength	        过滤时read的最大长度（）
forwardFastq      pair-end reads的right的fastq file
reverseFastq      pair-end reads的left的fastq file
mismatch          merge时允许的错配的比率。（对pair-end read 进行merge时mismatch占两个read的overlap长度的比率。如果overlap长度为120，允许一个错配则该参数为0.0084）
overlap           merge时pair-end的最大重叠长度值（pair-end read中两个read的重叠区域长度）
prefix            merge时输出文件的名字（存储pair-end read合并后的输出文件的文件名）
path              保存输出文件的文件夹名称（即将最终的结果name.extendedFrags.fastq输出到那个文件中，如果不加这一项，script会自己在当前工作目录下创建一个results文件夹，然后所有的输出文件都会被保存到这个文件夹中。）



没有path这一项的命令：
python ~/Desktop/process_the_raw_data/NGS_main.py 25 25 120 155 r0-C1R1-s0_L1_1.clean.fq r0-C1R1-s0_L1_2.clean.fq 0.02 149 r0-C1R1-s0 
有path这一项的命令
python ~/Desktop/process_the_raw_data/NGS_main.py 25 25 120 155 r0-C1R1-s0_L1_1.clean.fq r0-C1R1-s0_L1_2.clean.fq 0.02 149 r0-C1R1-s0 ~/Desktop/results/

(python ~/Desktop/process_the_raw_data/NGS_main.py LEADING_quality TRAILING_quality MINLEN Maxlength forwardFastq reverseFastq mismatch overlap prefix)
