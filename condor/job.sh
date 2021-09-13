#!/bin/bash

#-----------------------------------------------
# This is the bash script called by job.sub
# References:
#  https://www.hep.wisc.edu/cms/comp/faq.html#how-can-i-copy-files
#  https://tier2.hep.caltech.edu/?page_id=141
#----------------------------------------------- 

export X509_USER_PROXY=$1
voms-proxy-info -all
voms-proxy-info -all -file $1

export jobdir=$2
export sampleName=$3
export fileToRun=$4    # the cmsRun driver .py file
export inputFileList=$5   # path to list of input files (/path/myList.list where myList.list contains
                       # 'root://xrootd.[...]'
export outputFile=$6   # output file path (parsed in cmsRun .py file)
export maxEvents=$7    # max events to process (parsed in cmsRun .py file)
export hdfsDir=$8      # E.g. If this is set to skkwan/, output file is copied to /hdfs/store/user/skkwan/

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
echo "System software: `cat /etc/redhat-release`" #Operating System on that node
source /cvmfs/cms.cern.ch/cmsset_default.sh 
scramv1 project CMSSW CMSSW_10_6_16 # cmsrel is an alias not on the workers
ls -alrth
cd CMSSW_10_6_16/src/
eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
echo $CMSSW_BASE "is the CMSSW we created on the local worker node"
pwd

### cmsRun mycode.py $1 $2
# cmsRun tempJOB_EmbeddingRun2018A-MuTau_BATCH_1.py inputFiles='root://cms-xrd-global.cern.ch//store/user/jbechtel/gc_storage/MuTau_data_2018ABC_CMSSW1020/TauEmbedding_MuTau_data_2018ABC_CMSSW1020_Run2018A/20/merged_19.root' outputFile='myTest.root' maxEvents=5
inputFiles=$(cat $inputFileList)

echo "job.sh: Inputfilelist is $inputFileList, running with input files ${inputFiles} and output file name ${outputFile}..." 
cmsRun ${fileToRun} inputFiles=$inputFiles outputFile=$outputFile maxEvents=$maxEvents


echo "Attempting to gfal-copy $outputFile :..." 
eval `scram unsetenv -sh`
pwd
ls

# Copying *.root is a little sloppy but we can do this because each job only produces
# one output file.
# Gets copied to /hdfs/store/user/skkwan/[..]
gfal-copy -p *.root davs://cmsxrootd.hep.wisc.edu:1094/store/user/$hdfsDir

echo "End of attempt to gfal-copy $outputFile "
