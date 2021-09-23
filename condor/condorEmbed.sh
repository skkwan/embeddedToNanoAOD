#!/bin/bash

# Usage: source condorEmbed.sh [samples.csv] 
# REMAKE : remake the unique .py files

SAMPLES=$1

# Directory in nfs where the *.list and *.py files are held (currently on login05)
# Copied /scripts and /getFilePaths into this directory
# WORKING_AREA="/nfs_scratch/skkwan/embeddedMiniToNano/"

WORKING_AREA="/afs/hep.wisc.edu/home/skkwan/public/embeddedMiniToNano/CMSSW_10_6_16/src/embeddedToNanoAOD"

NFS_AREA="/nfs_scratch/skkwan/embeddedMiniToNano"

cmsenv



#--------------------------------------------------------
# Check that the input .list files exist first!
#--------------------------------------------------------
echo ">>> condorEmbed.sh: Reading from ${SAMPLES}..."
while IFS=, read -r YEAR SAMPLE INPUT_DIR BASE_SCRIPT
do
    echo ">>> condorEmbed.sh: Starting sample ${SAMPLE} and input directory: ${INPUT_DIR}"

    if [[ -d "../${INPUT_DIR}" ]]; then
	echo "   >>> ${INPUT_DIR} exists"
    else
	echo "   >>> condorEmbed.sh: [ERROR]: Input directory ${INPUT_DIR} not found"
    fi
done < ${SAMPLES} 

#--------------------------------------------------------
# Get the voms-proxy-info certificate
#--------------------------------------------------------
export MYPROXYPATH="$(voms-proxy-info -path)"

#export DESTINATION="/afs/hep.wisc.edu/home/skkwan/private/x509up"
export DESTINATION="/nfs_scratch/skkwan/x509up" 

echo ">>> condorEmbed.sh: Found proxy at: ${MYPROXYPATH}, copying to ${DESTINATION}"
cp ${MYPROXYPATH} ${DESTINATION}

#--------------------------------------------------------
# Get the current date and time, needed for output files 
#--------------------------------------------------------                                                              

DATETIME="$(date +"%b-%d-%Y-%Hh%Mm")"

# JOB_DIR: where the .out, .log, .err files will go
# For hep.wisc.edu, this can't be in /afs/ because Condor jobs do not have write access to afs by default
JOB_DIR="/nfs_scratch/skkwan/embeddedMiniToNano"

# Access the .csv list of samples to run over
while IFS=, read -r YEAR SAMPLE INPUT_DIR BASE_SCRIPT
do
    {
	# Declare scratch directory to put each config.py file                                                                                               
	# TEMP_DIR="${CMSSW_BASE}/src/embeddedToNanoAOD/temp/${YEAR}/${SAMPLE}"
	# mkdir -p ${TEMP_DIR}

	# Declare the directory to put the output file in
	OUTDIR="${JOB_DIR}/${YEAR}/${SAMPLE}"
	mkdir -p ${OUTDIR}
	echo ">>> condorEmbed.sh: making ${OUTDIR}"

	# Each INPUT_DIR has a bunch of .list files in it
	FILES="${WORKING_AREA}/${INPUT_DIR}*.list"

	# If we use the 'queue' command in Condor, we don't need to make one .sub file for each unique .py (that would take a long time just to submit)
	# e.g. queue 100 will set $(Process) equal to 0 through 99 in the .sub file
	LISTNAME_AFS="${WORKING_AREA}/${INPUT_DIR}/${SAMPLE}_BATCH_\$(Process).list"
	LISTNAME_NFS="${NFS_AREA}/${INPUT_DIR}/${SAMPLE}_BATCH_\$(Process).list"
	LISTNAME_LOCAL="${SAMPLE}_BATCH_\$(Process).list"

	# Copy the base script to nfs
	BASE_SCRIPT_AFS="${WORKING_AREA}/scripts/${BASE_SCRIPT}"
	BASE_SCRIPT_NFS="${NFS_AREA}/scripts/${BASE_SCRIPT}"
	BASE_SCRIPT_LOCAL="${BASE_SCRIPT}"

	OUTPUTFILE="${SAMPLE}_\$(Process).root"
	MAXEVENTS=-1
	N_TOTAL_INSTANCES=`find ${WORKING_AREA}/${INPUT_DIR}/ -name "Embedding*" | xargs ls -lrt | wc -l`
	NINSTANCES=10
	# NINSTANCES=${N_TOTAL_INSTANCES}
	
	echo ">>> Submitting with max ${MAXEVENTS} events (per input file) (-1: run over all events)..."
	echo ">>> Submitting ${NINSTANCES} .list files, out of ${N_TOTAL_INSTANCES} total .lists..."
	
	# Make a subfile in the temp directory
	subfile=${OUTDIR}/job_${SAMPLE}.sub
	echo ">>> Creating subfile at ${subfile}..."

	# Make sure the /hdfs area is initialized
	HDFSDIR="skkwan/EmbeddedNanoAOD/${YEAR}/${SAMPLE}/"
	mkdir -p /hdfs/store/user/${HDFSDIR}


	cp jobTemplate.sub ${subfile}
	sed -i "s|(CMSSW_BASE)|${CMSSW_BASE}|g" ${subfile}
	sed -i "s|(jobdir)|${OUTDIR}|g" ${subfile}
	sed -i "s|(sampleName)|${SAMPLE}|g" ${subfile}
	
	sed -i "s|(fileToRun_afs)|${BASE_SCRIPT_AFS}|g" ${subfile}
	sed -i "s|(fileToRun_name)|${BASE_SCRIPT_LOCAL}|g" ${subfile}  # we will ship this to the node
	
	sed -i "s|(inputFileList_afs)|${LISTNAME_AFS}|g" ${subfile}
	sed -i "s|(inputFileList_name)|${LISTNAME_LOCAL}|g" ${subfile}  # we will ship this to the node
	
	sed -i "s|(outputFile)|${OUTPUTFILE}|g" ${subfile}
	sed -i "s|(maxEvents)|${MAXEVENTS}|g" ${subfile}

	sed -i "s|(nInstances)|${NINSTANCES}|g" ${subfile}
	sed -i "s|(hdfsDir)|${HDFSDIR}|g" ${subfile}
	cat ${subfile}
	condor_submit ${subfile}
	
    } 
done < ${SAMPLES}
