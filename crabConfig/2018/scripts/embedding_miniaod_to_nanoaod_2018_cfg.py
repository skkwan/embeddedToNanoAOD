# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: -s NANO --data --eventcontent NANOAOD --datatier NANOAOD --no_exec --conditions 106X_dataRun2_v37 --era Run2_2018 --filein file:input_miniaod_file.root --fileout file:output_nanoaod_file.root --python_filename=embedding_miniaod_to_nanoaod_cfg.py

import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('NANO',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/MuTauFinalState/EmbeddingRun2018A/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/0217e7d7-7eec-498b-9eea-e8129fc89f2c.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('-s nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:output_nanoaod_file.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v37', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(
    process.particleLevelSequence
    + process.genParticleSequence
    + process.nanoSequenceCommon
    + process.nanoSequenceOnlyFullSim
    + process.muonMC
    + process.electronMC
    + process.photonMC
    + process.tauMC
    + process.globalTablesMC
    + process.btagWeightTable
    + process.genWeightsTable
    + process.genParticleTables
)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeData 

#call to customisation function nanoAOD_customizeData imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeData(process)

# End of customisation functions

# Customisation from command line
process.unpackedPatTrigger.triggerResults = cms.InputTag("TriggerResults::SIMembeddingHLT")
process.NANOAODoutput.outputCommands.append("keep edmTriggerResults_*_*_SIMembeddingHLT")
process.NANOAODoutput.outputCommands.append("keep edmTriggerResults_*_*_MERGE")
process.NANOAODoutput.outputCommands.remove("keep edmTriggerResults_*_*_*")
process.genParticles2HepMC.genEventInfo = cms.InputTag("generator", "", "SIMembeddingpreHLT")
process.patJetsReapplyJECPuppi.jetSource = cms.InputTag("slimmedJetsPuppi", "", "MERGE")
process.patJetCorrFactorsReapplyJECPuppi.src = cms.InputTag("slimmedJetsPuppi", "", "MERGE")
process.puppiMetTable.src = cms.InputTag("slimmedMETsPuppi", "", "RERUNPUPPI")
process.rawPuppiMetTable.src = cms.InputTag("slimmedMETsPuppi", "", "RERUNPUPPI")
process.slimmedMETsPuppi.t01Variation = cms.InputTag("slimmedMETsPuppi", "", "RERUNPUPPI")
process.metrawCaloPuppi.metSource = cms.InputTag("slimmedMETsPuppi", "", "RERUNPUPPI")
process.pfMetPuppi.metSource = cms.InputTag("slimmedMETsPuppi", "", "RERUNPUPPI")

process.triggerObjectTable.selections[0].qualityBits = cms.string(
    "filter('*CaloIdLTrackIdLIsoVL*TrackIso*Filter') + " \
    "2*filter('hltEle*WPTight*TrackIsoFilter*') + " \
    "4*filter('hltEle*WPLoose*TrackIsoFilter') + " \
    "8*filter('*OverlapFilter*IsoEle*PFTau*') + " \
    "16*filter('hltEle*Ele*CaloIdLTrackIdLIsoVL*Filter') + " \
    "32*filter('hltMu*TrkIsoVVL*Ele*CaloIdLTrackIdLIsoVL*Filter*') + " \
    "64*filter('hltOverlapFilterIsoEle*PFTau*') + " \
    "128*filter('hltEle*Ele*Ele*CaloIdLTrackIdLDphiLeg*Filter') + " \
    "256*max(filter('hltL3fL1Mu*DoubleEG*Filtered*'),filter('hltMu*DiEle*CaloIdLTrackIdLElectronleg*Filter')) + " \
    "512*max(filter('hltL3fL1DoubleMu*EG*Filter*'),filter('hltDiMu*Ele*CaloIdLTrackIdLElectronleg*Filter')) + " \
    "1024*min(filter('hltEle32L1DoubleEGWPTightGsfTrackIsoFilter'),filter('hltEGL1SingleEGOrFilter')) + " \
    "2048*filter('hltEle*CaloIdVTGsfTrkIdTGsfDphiFilter') + " \
    "4096*path('HLT_Ele*PFJet*') + " \
    "8192*max(filter('hltEG175HEFilter'),filter('hltEG200HEFilter')) + " \
    "16384*filter('hltEle27WPTightGsfTrackIsoFilter') + " \
    "32768*filter('hltEle32WPTightGsfTrackIsoFilter') + " \
    "65536*filter('hltEle32L1DoubleEGWPTightGsfTrackIsoFilter') + " \
    "131072*filter('hltEGL1SingleEGOrFilter') + " \
    "262144*filter('hltEle35noerWPTightGsfTrackIsoFilter') + " \
    "524288*filter('hltEle24erWPTightGsfTrackIsoFilterForTau')"
)

process.triggerObjectTable.selections[2].qualityBits = cms.string(
    "filter('*RelTrkIsoVVLFiltered0p4') + " \
    "2*filter('hltL3crIso*Filtered0p07') + " \
    "4*filter('*OverlapFilterIsoMu*PFTau*') + " \
    "8*max(filter('hltL3crIsoL1*SingleMu*Filtered0p07'),filter('hltL3crIsoL1sMu*Filtered0p07')) + " \
    "16*filter('hltDiMuon*Filtered*') + " \
    "32*filter('hltMu*TrkIsoVVL*Ele*CaloIdLTrackIdLIsoVL*Filter*') + " \
    "64*filter('hltOverlapFilterIsoMu*PFTau*') + " \
    "128*filter('hltL3fL1TripleMu*') + " \
    "256*max(filter('hltL3fL1DoubleMu*EG*Filtered*'),filter('hltDiMu*Ele*CaloIdLTrackIdLElectronleg*Filter')) + " \
    "512*max(filter('hltL3fL1Mu*DoubleEG*Filtered*'),filter('hltMu*DiEle*CaloIdLTrackIdLElectronleg*Filter')) + " \
    "1024*max(filter('hltL3fL1sMu*L3Filtered50*'),filter('hltL3fL1sMu*TkFiltered50*')) + " \
    "2048*max(filter('hltL3fL1sMu*L3Filtered100*'),filter('hltL3fL1sMu*TkFiltered100*')) + " \
    "4096*filter('hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07') + " \
    "8192*filter('hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07') + " \
    "16384*filter('hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07') + " \
    "32768*filter('hltL3crIsoBigORMu18erTauXXer2p1L1f0L2f10QL3f20QL3trkIsoFiltered0p07')"
)

process.triggerObjectTable.selections[3].sel = cms.string(
    "( type(84) || type(-100) ) && (pt > 5) && coll('*Tau*') && " \
    "( filter('*LooseChargedIso*') || filter('*MediumChargedIso*') || " \
    "filter('*TightChargedIso*') || filter('*TightOOSCPhotons*') || " \
    "filter('hltL2TauIsoFilter') || filter('*OverlapFilterIsoMu*') || " \
    "filter('*OverlapFilterIsoEle*') || filter('*L1HLTMatched*') || " \
    "filter('*Dz02*') || filter('*DoublePFTau*') || " \
    "filter('*SinglePFTau*') || filter('hlt*SelectedPFTau') || " \
    "filter('*DisplPFTau*') || filter('*Tau*') )"
)

process.triggerObjectTable.selections[3].qualityBits = cms.string(
    "filter('*LooseChargedIso*') + " \
    "2*filter('*MediumChargedIso*') + " \
    "4*filter('*TightChargedIso*') + " \
    "8*filter('*TightOOSCPhotons*') + " \
    "16*filter('*Hps*') + " \
    "32*filter('hltSelectedPFTau*MediumChargedIsolationL1HLTMatched*') + " \
    "64*filter('hltDoublePFTau*TrackPt1*ChargedIsolation*Dz02Reg') + " \
    "128*filter('hltOverlapFilterIsoEle*PFTau*') + " \
    "256*filter('hltOverlapFilterIsoMu*PFTau*') + " \
    "512*filter('hltDoublePFTau*TrackPt1*ChargedIsolation*') + " \
    "1024*filter('hltL1sBigORLooseIsoEGXXerIsoTauYYerdRMin0p3') + " \
    "2048*filter('hltL1sMu18erTau24erIorMu20erTau24er') + " \
    "4096*filter('hltL1sBigORMu18erTauXXer2p1') + " \
    "8192*filter('hltDoubleL2IsoTau26eta2p2')"
)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


