import os
import sys
from Bio import SeqIO
import gzip
import pickle
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import fileinput
import time
start=time.clock()
LEADING_quality=int(sys.argv[1])
TRAILING_quality=int(sys.argv[2])
MINLEN=int(sys.argv[3])
length=int(sys.argv[4])
input_forward=open(sys.argv[5],"r")
output=sys.argv[6]




def reads_filter(inputFile,LEADING_quality,TRAILING_quality,minilength,maxlength,writefile):
    good_reads=[]
    good_readsLst=[]
    n=0
    count=0
    n_length=0
    w=open(writefile,'a')
    for rec in SeqIO.parse(inputFile, "fastq"):
        
        n+=1
        end=0
        start=0
        qualityLst=rec.letter_annotations["phred_quality"]
        length=len(qualityLst)
        if len(rec.seq)>maxlength:
            n_length+=1
            continue
        for i in range(len(qualityLst)):
            if int(qualityLst[i])<LEADING_quality:
                continue
            else:
                start=i
                break
        for i in range(len(qualityLst)):
            if int(qualityLst[length-i-1])<TRAILING_quality:
                continue
            else:
                end=length-1-i
                break
        rec=rec[start:end]
        readQuality=rec.letter_annotations["phred_quality"]
        Q30Number=len(filter(lambda x: x>=30 , rec.letter_annotations["phred_quality"]))
        Q20Number=len(filter(lambda x: x>=20 , rec.letter_annotations["phred_quality"]))
        Q10Number=len(filter(lambda x: x<10 , rec.letter_annotations["phred_quality"]))
        Seqlength=len(rec.letter_annotations["phred_quality"])
        if Q30Number>0.6*Seqlength and Q20Number>0.85*Seqlength and Q10Number<1 and Seqlength>minilength:
           SeqIO.write(rec,w, "fastq")
           count+=1 
    w.close()
    print('The length filter is %s'%(n_length))
    return n,count




forwardNumber,count1=reads_filter(input_forward,LEADING_quality,TRAILING_quality,MINLEN,length,output)
end=time.clock()
print('Running time: %s Minutes'%((end-start)/60))
print("Input forward :%s,filtered  %s " %(forwardNumber,int(forwardNumber)-count1))
