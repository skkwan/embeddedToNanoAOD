# Convert MiniAOD Embedded samples to NanoAOD: Ultralegacy

Convert HiggsToTauTau Embedded MiniAOD samples to NanoAOD, using CRAB jobs. Reference: https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauEmbeddingSamplesUL#NanoAOD_Conversion



## Setup
(For me: on `login.hep.wisc.edu`:)
```
cmsrel CMSSW_10_6_30
git clone --branch ultralegacy --single-branch git@github.com:skkwan/embeddedToNanoAOD.git
```

## CRAB for producing NanoAOD from MiniAOD
For CRAB, all you need is to submit from the main directory:
```
# First change 'skkwan' in the crabConfig file's outLFNDirBase
cmsenv
crab submit -c crabConfig-2018A.py
```
In this case, the `.py` called in the job is `scripts/nanoProd_18abc_NANO_CRAB.py`.

