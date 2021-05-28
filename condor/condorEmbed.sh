#!/bin/bash

# Usage: source condorEmbed.sh [samples.csv] [optional argument: REMAKE]
# REMAKE : remake the unique .py files

SAMPLES=$1
REMAKE=$2

cmsenv

#--------------------------------------------------------
# Check that the input .list files exist first!
#--------------------------------------------------------
echo ">>> condorEmbed.sh: Reading from ${SAMPLES}..."
while IFS=, read -r YEAR SAMPLE INPUT_DIR
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
echo ">>> condorEmbed.sh: Found proxy at: ${MYPROXYPATH}, copying to /afs/cern.ch/user/s/skkwan/private/x509up_file"

cp ${MYPROXYPATH} /afs/cern.ch/user/s/skkwan/private/x509up_file

#--------------------------------------------------------
# Get the current date and time, needed for output files 
#--------------------------------------------------------                                                              

DATETIME="$(date +"%b-%d-%Y-%Hh%Mm")"

EOS_DIR="/eos/user/s/skkwan/embeddedNanoAOD" 
WORKING_DIR="${CMSSW_BASE}/src/embeddedToNanoAOD"
JOB_DIR="/afs/cern.ch/work/s/skkwan/private/condor_embed"


# BASE SCRIPT: change for year 2017 2018 etc. 
BASE_SCRIPT="../scripts/nanoProd_17_NANO.py"

# Access the .csv list of samples to run over
while IFS=, read -r YEAR SAMPLE INPUT_DIR
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
	FILES="../${INPUT_DIR}*.list"

	if [[ "$REMAKE" == *"REMAKE"* ]]; then
	    # For each .list file, make a unique .py
	    for f in $FILES
	    do
		# echo ${f}
		# Get the file name with extension (merged_10.root, for example)
		STEM=$(basename "${f}" ".${f##*.}")
		# echo ${STEM}
		
		# We will append the lines in this .txt file to the example config.py
		TEMPLATE=$(cat "../scripts/suffixForNanoProdPython.txt")
		
		# Declare output NanoAOD n-tuple file path and name
		OUT_PATH="file:${OUTDIR}/${STEM}_NANO.root"
		# echo ${OUT_PATH}
		
		# Replace INPUT.ROOT and OUTPUT.ROOT in the template with our files
		list=$(cat ${f})
		TEMPLATE2="${TEMPLATE/\'INPUT.ROOT\'/$list}"
		TEMPLATE3="${TEMPLATE2/OUTPUT.ROOT/${OUT_PATH}}"
		
		# Declare the unique Python script, create it
		SINGLE_PYTHON="${OUTDIR}/tempJOB_${STEM}.py"
		# echo ${SINGLE_PYTHON}
		cp ${BASE_SCRIPT} ${SINGLE_PYTHON}
		echo "${TEMPLATE3}" >> ${SINGLE_PYTHON}
		
		# Now there is a unique .py that can be run standalone, in temp/, for example tempJOB_EmbeddingRun2017E-MuTau_BATCH_62.py
	    done
	fi
	
	# If we use the 'queue' command in Condor, we don't need to make one .sub file for each unique .py (that would take a long time just to submit)
	# e.g. queue 100 will set $(Process) equal to 0 through 99 in the .sub file
	PYNAME="tempJOB_${SAMPLE}_BATCH_\$(Process).py"
	NINSTANCES=`ls ${OUTDIR}/tempJOB_*.py | wc -l`
	# NINSTANCES=2
	
	# Make a subfile in the temp directory
	subfile=${OUTDIR}/job_${SAMPLE}.sub
	echo "Creating subfile at ${subfile}"

	cp jobTemplate.sub ${subfile}
	sed -i "s|(CMSSW_BASE)|${CMSSW_BASE}|g" ${subfile}
	sed -i "s|(jobdir)|${OUTDIR}|g" ${subfile}
	sed -i "s|(sampleName)|${SAMPLE}|g" ${subfile}
	sed -i "s|(fileToRun)|${OUTDIR}/${PYNAME}|g" ${subfile}
	sed -i "s|(nInstances)|${NINSTANCES}|g" ${subfile}
	condor_submit ${subfile}

    } 
done < ${SAMPLES}
