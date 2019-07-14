#脚本说明(本脚本是用来对pair-end二代测序数据进行预处理，第一步对pair-end read进行合并，然后再对合并后的single end read进行trim和过滤)


######
#脚本需要输入的参数说明
######
1.LEADING_quality   read5‘端trim的threshold (一般选择25，前端的base质量值低于25的base会被去掉)
2.TRAILING_quality  read3’端trim的threshold (一般选择25，尾端的base质量值低于25的base会被去掉)

3.MINLEN            过滤时read的最短长度 (如果read中base的质量很低导致read被trim后的长度太短低于这个threshold值，该read就被丢弃)
                    Generally, (length of PCR product) - 1~2 bp
                    
4.Maxlength	        过滤时read的最大长度, same as above
                    Generally, 2N (NGS setting, e.g. 150 bp) - (length of PCR product) + 1~2 bp

5.forwardFastq      pair-end reads的right的fastq file
6.reverseFastq      pair-end reads的left的fastq file

7.mismatch          merge时允许的错配的比率 (对pair-end read 进行merge时mismatch占两个read的overlap长度的比率。如果overlap长度为120，允许一个错配则该参数为0.0084)

8.overlap           merge时pair-end的最大重叠长度值 (pair-end read中两个read的重叠区域长度)
                    Generally, (length of PCR product) + 1~2 bp

9.prefix            merge时输出文件的名字 (存储pair-end read合并后的输出文件的文件名)


######
#输出文件说明
######
本脚本会产生两个文件夹meger_result和final_result。meger_result文件夹是存储中间merge输出结果的，final_result文件夹使用来保存最终的过滤结果的。


######
#脚本命令使用说明
######
一.本脚本的使用方法：

python ~/Desktop/process_the_raw_data/NGS_main.py LEADING_quality TRAILING_quality MINLEN Maxlength forwardFastq reverseFastq mismatch overlap prefix

二.本脚本的应用案例
1.命令输入
python ~/Desktop/process_the_raw_data/NGS_main.py 25 25 120 155 r0-C1R1-s0_L1_1.clean.fq r0-C1R1-s0_L1_2.clean.fq 0.02 149 r0-C1R1-s0 
2.输出文件说明
该命令最终会产生两个文件夹meger_result和final_result。meger_result文件中包含了r0-C1R1-s0_L1_1.clean.fq和r0-C1R1-s0_L1_2.clean.fq合并的r0-C1R1-s0.extendedFrags.fastq文件、未合并的文件以及一些统计文件，final_result文件夹包含最终的过滤文件r0-C1R1-s0_L1_1.clean.fq_trim.fastq文件。
