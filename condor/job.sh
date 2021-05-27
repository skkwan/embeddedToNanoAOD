#!/bin/bash

#-----------------------------------------------
# This is the bash script called by job.sub
#----------------------------------------------- 

export X509_USER_PROXY=$1
voms-proxy-info -all
voms-proxy-info -all -file $1

export jobdir=$2
export jobname=$3
export fileToRun=$4

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

cmsRun ${fileToRun}
