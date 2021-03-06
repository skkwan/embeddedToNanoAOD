# Convert MiniAOD Embedded samples to NanoAOD

Convert HiggsToTauTau Embedded MiniAOD samples to NanoAOD, using Condor jobs.

See [list of samples](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingLegacyRun2#Embedded_2018) and [official instructions for NanoAOD conversion](https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauTauEmbeddingSamples2018#NanoAOD_Conversion) (TWiki log-in needed).

## Setup
On an lxplus7 machine:
```
cmsrel 10_6_16
cd CMSSW_10_6_16/src
```
and git clone this repo.

## Converting MiniAOD to NanoAOD

1. (Do only once, each time you change the datasets)
   Get the logical file names to the input MiniAOD samples (edit `logicalFileNames.txt`). This step also makes directories
   with shorter .list files. 
```
cmsenv
voms-proxy-init --voms cms
cd getFilePaths/
cat logicalFileNames.txt   
source getFilePaths.sh
```

2. Make a `.csv` list of datasets like this (Year, name of dataset, path to `.list` logical file names made in previous step) :
`2018,EmbeddingRun2018B-MuTau,getFilePaths/2018/EmbeddingRun2018B-MuTau`	    

3. Edit `condorEmbed.sh` to use the correct template .py script, and edit the `.sub` file so it calls `queue` however many times you want

```
cmsenv
voms-proxy-init --voms cms
cd condor/
source condorEmbed.sh ../embeddedMiniAOD-2017.csv
```

4. Skim the Embedded NanoAOD in the main LUNA framework.

```
# cd to the directory with all the .root files
ls -d $PWD/*.root > /afs/cern.ch/work/s/skkwan/public/hToAA/syncNanoAOD/nanoAODfilepaths/2017/Embedded-Run2017B-Mu
```