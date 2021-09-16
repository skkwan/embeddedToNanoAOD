# Usage: After getting voms-proxy-init certificate: source runCondorEmbed.sh
# ALSO:  - Check condorEmbed.sh has the desired number of events per file to run over,
#          and queues the appropriate number of files per dataset
# E.g. Start with a few events per file and one file per dataset to make sure things
# are running smoothly.

# source condorEmbed.sh ../embeddedMiniAOD-2018A.csv 

# Try all four data eras

source condorEmbed.sh ../embeddedMiniAOD-2018A.csv
