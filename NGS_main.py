import os
import sys
import time
start=time.clock()
LEADING_quality=int(sys.argv[1])
TRAILING_quality=int(sys.argv[2])
MINLEN=int(sys.argv[3])
Maxlength=int(sys.argv[4])
forwardFastq=sys.argv[5]
reverseFastq=sys.argv[6]
mismatch=float(sys.argv[7])
overlap=int(sys.argv[8])
prefix=sys.argv[9]
if len(sys.argv)!=10:
    path=os.getcwd()
    path+='/meger_result'
    path_final=sys.argv[10]
else:
    path=os.getcwd()
    path_final=path+'/final_result'
    path+='/meger_result'
    os.system('mkdir -p %s'%(path_final))
    print('output path is %s'%(path))

flashPath=sys.path[0]
if forwardFastq.find('/') != -1:
    Forward_trim='%s/%s'%(path_final,forwardFastq.split('/')[-1].split('.fq')[0]+'_trim.fq')
else:
    Forward_trim='%s/%s'%(path_final,forwardFastq.split('.fq')[0]+'_trim.fq')
Forward_trim_pair='%s/%s'%(path,Forward_trim.split('/')[-1].split('.fq')[0]+'_pair.fq')

os.system('cat /dev/null > %s'%(Forward_trim))
os.system('%s/flash --max-mismatch-density=%s --max-overlap=%s --allow-outies --output-prefix=%s --output-directory=%s %s %s'%(flashPath,mismatch,overlap,prefix,path,forwardFastq,reverseFastq))
os.system('python %s/NGS_trim_filter.py %s %s %s %s %s/%s.extendedFrags.fastq %s'%(flashPath,LEADING_quality,TRAILING_quality,MINLEN,Maxlength,path,prefix,Forward_trim))
end=time.clock()
print('Running time: %s Minutes'%((end-start)/60))
