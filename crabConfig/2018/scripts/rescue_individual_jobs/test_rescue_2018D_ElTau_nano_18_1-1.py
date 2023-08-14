# Auto generated configuration file
# modified with instructions from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauEmbeddingSamplesUL#NanoAOD_Conversion
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: -s NANO --data --eventcontent NANOAOD --datatier NANOAOD --no_exec --conditions 106X_dataRun2_v37 --era Run2_2018 --filein file:test_18.root --fileout file:test_nano_18.root --python_filename=embedding_nanoAOD_18.py
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
    fileNames = cms.untracked.vstring(

    #   '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018D/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/d587d16e-5f24-4bf1-8458-7b9d94b303e2.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018D/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/994561cf-b98f-4a0c-8fa1-9c8a02b897d6.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018D/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/35acad9b-ab4b-4007-8f4d-4ef46564c05e.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018D/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/35acad9b-ab4b-4007-8f4d-4ef46564c05e.root'
        ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange( (
 "321078:50-321078:50", "321078:5-321078:5", "321078:12-321078:14", "321078:31-321078:31", "321078:49-321078:49", 
    "321005:32-321005:33", "321005:23-321005:23", "321005:51-321005:51", "321005:56-321005:56", "321005:49-321005:49", 
    "321005:52-321005:54", "321005:22-321005:22", "321005:57-321005:57", "321005:30-321005:30", "321005:46-321005:47", 
    "321005:50-321005:50", "321005:48-321005:48", "321005:55-321005:55", "321005:31-321005:31", "321006:121-321006:121", 
    "321006:123-321006:123", "321006:107-321006:107", "321006:119-321006:119", "321006:122-321006:122", "321006:117-321006:118", 
    "321006:120-321006:120", "321006:105-321006:105", "321006:114-321006:114", "321006:106-321006:106", "321006:116-321006:116", 
    "321006:115-321006:115", "321006:124-321006:124", "321006:146-321006:146", "321006:148-321006:148", "321006:152-321006:152", 
    "321006:156-321006:156", "321006:125-321006:125", "321006:128-321006:128", "321006:137-321006:137", "321006:140-321006:140", 
    "321006:154-321006:154", "321006:158-321006:158", "321006:142-321006:142", "321006:161-321006:161", "321006:127-321006:127", 
    "321006:129-321006:130", "321006:139-321006:139", "321006:145-321006:145", "321006:150-321006:150", "321006:131-321006:131", 
    "321006:136-321006:136", "321006:149-321006:149", "321006:133-321006:133", "321006:135-321006:135", "321006:141-321006:141", 
    "321006:153-321006:153", "321006:155-321006:155", "321006:134-321006:134", "321006:144-321006:144", "321006:162-321006:162", 
    "321006:126-321006:126", "321006:132-321006:132", "321006:138-321006:138", "321006:143-321006:143", "321006:147-321006:147", 
    "321006:151-321006:151", "321006:157-321006:157", "321006:159-321006:160", "321007:11-321007:11", "321007:27-321007:28", 
    "321007:37-321007:37", "321007:41-321007:41", "321007:57-321007:58", "321007:66-321007:66", "321007:70-321007:70", 
    "321007:78-321007:78", "321007:85-321007:85", "321007:89-321007:89", "321007:91-321007:92", "321007:97-321007:97", 
    "321007:102-321007:102", "321007:107-321007:107", "321007:116-321007:116", "321007:120-321007:121", "321007:126-321007:126", 
    "321007:145-321007:145", "321007:155-321007:155", "321007:3-321007:4", "321007:6-321007:6", "321007:33-321007:33", 
    "321007:35-321007:35", "321007:39-321007:39", "321007:49-321007:49", "321007:56-321007:56", "321007:63-321007:63", 
    "321007:65-321007:65", "321007:76-321007:76", "321007:80-321007:80", "321007:82-321007:82", "321007:86-321007:86", 
    "321007:113-321007:113", "321007:118-321007:118", "321007:122-321007:122", "321007:125-321007:125", "321007:134-321007:135", 
    "321007:148-321007:148", "321007:160-321007:160", "321007:176-321007:176", "321007:179-321007:179", "321007:2-321007:2", 
    "321007:21-321007:21", "321007:34-321007:34", "321007:40-321007:40", "321007:47-321007:47", "321007:50-321007:51", 
    "321007:61-321007:61", "321007:75-321007:75", "321007:95-321007:95", "321007:103-321007:103", "321007:112-321007:112", 
    "321007:119-321007:119", "321007:150-321007:150", "321007:157-321007:157", "321007:174-321007:174", "321007:10-321007:10", 
    "321007:13-321007:14", "321007:19-321007:19", "321007:25-321007:26", "321007:55-321007:55", "321007:60-321007:60", 
    "321007:73-321007:74", "321007:81-321007:81", "321007:123-321007:123", "321007:127-321007:128", "321007:137-321007:137", 
    "321007:139-321007:139", "321007:147-321007:147", "321007:158-321007:159", "321007:161-321007:161", "321007:5-321007:5", 
    "321007:8-321007:8", "321007:12-321007:12", "321007:15-321007:15", "321007:20-321007:20", "321007:23-321007:24", 
    "321007:36-321007:36", "321007:45-321007:45", "321007:69-321007:69", "321007:72-321007:72", "321007:87-321007:87", 
    "321007:93-321007:94", "321007:96-321007:96", "321007:99-321007:99", "321007:105-321007:105", "321007:109-321007:109", 
    "321007:111-321007:111", "321007:143-321007:143", "321007:154-321007:154", "321007:156-321007:156", "321007:17-321007:18", 
    "321007:29-321007:31", "321007:38-321007:38", "321007:42-321007:42", "321007:46-321007:46", "321007:48-321007:48", 
    "321007:52-321007:54", "321007:71-321007:71", "321007:77-321007:77", "321007:84-321007:84", "321007:101-321007:101", 
    "321007:104-321007:104", "321007:106-321007:106", "321007:124-321007:124", "321007:129-321007:129", "321007:138-321007:138", 
    "321007:141-321007:141", "321007:146-321007:146", "321007:149-321007:149", "321007:175-321007:175", "321007:177-321007:177", 
    "321007:1-321007:1", "321007:9-321007:9", "321007:22-321007:22", "321007:32-321007:32", "321007:62-321007:62", 
    "321007:68-321007:68", "321007:83-321007:83", "321007:88-321007:88", "321007:90-321007:90", "321007:100-321007:100", 
    "321007:108-321007:108", "321007:114-321007:114", "321007:136-321007:136", "321007:142-321007:142", "321007:178-321007:178", 
    "321007:7-321007:7", "321007:16-321007:16", "321007:43-321007:44", "321007:59-321007:59", "321007:64-321007:64", 
    "321007:67-321007:67", "321007:79-321007:79", "321007:98-321007:98", "321007:110-321007:110", "321007:115-321007:115", 
    "321007:117-321007:117", "321007:133-321007:133", "321007:140-321007:140", "321007:144-321007:144", "321007:165-321007:165", 
    "321007:173-321007:173", "321007:180-321007:180", "321007:132-321007:132", "321007:171-321007:171", "321007:183-321007:183", 
    "321007:187-321007:187", "321007:190-321007:190", "321007:197-321007:198", "321007:207-321007:209", "321007:220-321007:220", 
    "321007:228-321007:228", "321007:245-321007:245", "321007:248-321007:248", "321007:255-321007:255", "321007:262-321007:262", 
    "321007:273-321007:273", "321007:279-321007:279", "321007:284-321007:284", "321007:286-321007:286", "321007:301-321007:301", 
    "321007:304-321007:304", "321007:339-321007:339", "321007:347-321007:347", "321007:131-321007:131", "321007:163-321007:164", 
    "321007:169-321007:170", "321007:194-321007:194", "321007:199-321007:199", "321007:203-321007:203", "321007:205-321007:205", 
    "321007:221-321007:221"
))

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
    fileName = cms.untracked.string('file:test_nano_2018D_ElTau_1-1.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v37', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.particleLevelSequence + process.genParticleSequence + process.nanoSequenceCommon + process.nanoSequenceOnlyFullSim + process.muonMC + process.electronMC + process.photonMC + process.tauMC + process.globalTablesMC + process.btagWeightTable + process.genWeightsTable + process.genParticleTables)
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

# add modifications from https://github.com/cms-sw/cmssw/pull/38472 to correctly handle trigger flags in NanoAOD
process.triggerObjectTable.selections[0].qualityBits = cms.string(
                            "filter('*CaloIdLTrackIdLIsoVL*TrackIso*Filter') + " \
                            "2*filter('hltEle*WPTight*TrackIsoFilter*') + " \
                            "4*filter('hltEle*WPLoose*TrackIsoFilter') + " \
                            "8*filter('*OverlapFilter*IsoEle*PFTau*') + " \
                            "16*filter('hltEle*Ele*CaloIdLTrackIdLIsoVL*Filter') + " \
                            "32*filter('hltMu*TrkIsoVVL*Ele*CaloIdLTrackIdLIsoVL*Filter*')  + " \
                            "64*filter('hlt*OverlapFilterIsoEle*PFTau*') + " \
                            "128*filter('hltEle*Ele*Ele*CaloIdLTrackIdLDphiLeg*Filter') + " \
                            "256*max(filter('hltL3fL1Mu*DoubleEG*Filtered*'),filter('hltMu*DiEle*CaloIdLTrackIdLElectronleg*Filter')) + " \
                            "512*max(filter('hltL3fL1DoubleMu*EG*Filter*'),filter('hltDiMu*Ele*CaloIdLTrackIdLElectronleg*Filter')) + " \
                            "1024*min(filter('hltEle32L1DoubleEGWPTightGsfTrackIsoFilter'),filter('hltEGL1SingleEGOrFilter')) + " \
                            "2048*filter('hltEle*CaloIdVTGsfTrkIdTGsfDphiFilter') + " \
                            "4096*path('HLT_Ele*PFJet*') + " \
                            "8192*max(filter('hltEG175HEFilter'),filter('hltEG200HEFilter'))")
process.triggerObjectTable.selections[2].qualityBits = cms.string(
                            "filter('*RelTrkIsoVVLFiltered0p4') + " \
                            "2*filter('hltL3crIso*Filtered0p07') + " \
                            "4*filter('*OverlapFilterIsoMu*PFTau*') + " \
                            "8*max(filter('hltL3crIsoL1*SingleMu*Filtered0p07'),filter('hltL3crIsoL1sMu*Filtered0p07')) + " \
                            "16*filter('hltDiMuon*Filtered*') + " \
                            "32*filter('hltMu*TrkIsoVVL*Ele*CaloIdLTrackIdLIsoVL*Filter*') + " \
                            "64*filter('hlt*OverlapFilterIsoMu*PFTau*') + " \
                            "128*filter('hltL3fL1TripleMu*') + " \
                            "256*max(filter('hltL3fL1DoubleMu*EG*Filtered*'),filter('hltDiMu*Ele*CaloIdLTrackIdLElectronleg*Filter')) + " \
                            "512*max(filter('hltL3fL1Mu*DoubleEG*Filtered*'),filter('hltMu*DiEle*CaloIdLTrackIdLElectronleg*Filter')) + " \
                            "1024*max(filter('hltL3fL1sMu*L3Filtered50*'),filter('hltL3fL1sMu*TkFiltered50*')) + " \
                            "2048*max(filter('hltL3fL1sMu*L3Filtered100*'),filter('hltL3fL1sMu*TkFiltered100*'))")
process.triggerObjectTable.selections[3] = cms.PSet(
            name = cms.string("Tau"),
            id = cms.int32(15),
            sel = cms.string("type(84) && pt > 5 && coll('*Tau*') && ( filter('*LooseChargedIso*') || filter('*MediumChargedIso*') || filter('*DeepTau*') || filter('*TightChargedIso*') || filter('*TightOOSCPhotons*') || filter('hltL2TauIsoFilter') || filter('*OverlapFilterIsoMu*') || filter('*OverlapFilterIsoEle*') || filter('*L1HLTMatched*') || filter('*Dz02*') || filter('*DoublePFTau*') || filter('*SinglePFTau*') || filter('hlt*SelectedPFTau') || filter('*DisplPFTau*') || filter('*Tau*') )"), #All trigger objects from a Tau collection + passing at least one filter
            # sel = cms.string("type(84) && pt > 5 && coll('*Tau*') && filter('*Tau*') "), #All trigger objects from a Tau collection + passing at least one filter
            l1seed = cms.string("type(-100)"),
            l1deltaR = cms.double(0.3),
            l2seed = cms.string("type(84) && coll('hltL2TauJetsL1IsoTauSeeded')"),
            l2deltaR = cms.double(0.3),
            skipObjectsNotPassingQualityBits = cms.bool(True),
            qualityBits = cms.string(
                            "filter('*LooseChargedIso*') + " \
                            "2*filter('*MediumChargedIso*') + " \
                            "4*filter('*TightChargedIso*') + " \
                            "8*filter('*DeepTau*') + " \
                            "16*filter('*TightOOSCPhotons*') + " \
                            "32*filter('*Hps*') + " \
                            "64*filter('hlt*DoublePFTau*TrackPt1*ChargedIsolation*Dz02*') + " \
                            "128*filter('hlt*DoublePFTau*DeepTau*L1HLTMatched') + " \
                            "256*filter('hlt*OverlapFilterIsoEle*WPTightGsf*PFTau') + " \
                            "512*filter('hlt*OverlapFilterIsoMu*PFTau*') + " \
                            "1024*filter('hlt*SelectedPFTau*L1HLTMatched') + " \
                            "2048*filter('hlt*DoublePFTau*TrackPt1*ChargedIso*') + " \
                            "4096*filter('hlt*DoublePFTau*Track*ChargedIso*AgainstMuon') + " \
                            "8192*filter('hltHpsSinglePFTau*HLTMatched') + " \
                            "16384*filter('hltHpsOverlapFilterDeepTauDoublePFTau*PFJet*') + " \
                            "32768*filter('hlt*Double*ChargedIsoDisplPFTau*Dxy*') + " \
                            "65536*filter('*Monitoring') + " \
                            "131072*filter('*Reg') + " \
                            "262144*filter('*L1Seeded') + " \
                            "524288*filter('*1Prong') + " \
                            "1048576*filter('*DoubleL2IsoTau26*') + " \
                            "2097152*filter('*SingleL2IsoTau20*') + " \
                            "4194304*filter('*TauJet*') "),
            # qualityBits = cms.string("5000*filter('*DoubleL2IsoTau26*')"),
            qualityBitsDoc = cms.string("1 = LooseChargedIso, 2 = MediumChargedIso, 4 = TightChargedIso, 8 = DeepTau, 16 = TightID OOSC photons, 32 = HPS, 64 = charged iso di-tau, 128 = deeptau di-tau, 256 = e-tau, 512 = mu-tau, 1024 = single-tau/tau+MET, 2048 = run 2 VBF+ditau, 4096 = run 3 VBF+ditau, 8192 = run 3 double PF jets + ditau, 16384 = di-tau + PFJet, 32768 = Displaced Tau, 65536 = Monitoring, 131072 = regional paths, 262144 = L1 seeded paths, 524288 = 1 prong tau paths, 1048576 = double L2 tau26 (for tau embedding), 2097152 = single L2 tau20 (for tauleg in mu + tau crosstrigger in embedding), 4194304 = tau jet5 (for tauleg in e + tau crosstrigger in embedding)"),
        )
process.triggerObjectTable.selections[4].qualityBits = cms.string(
                "1         * filter('*CrossCleaned*LooseChargedIsoPFTau*') + " \
                "2         * filter('hltBTagCaloCSVp087Triple') + " \
                "4         * filter('hltDoubleCentralJet90') + " \
                "8         * filter('hltDoublePFCentralJetLooseID90') + " \
                "16        * filter('hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet') + " \
                "32        * filter('hltQuadCentralJet30') + " \
                "64        * filter('hltQuadPFCentralJetLooseID30') + " \
                "128       * max(filter('hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF'), filter('hltL1sQuadJetCIorTripleJetVBFIorHTT')) + " \
                "256       * filter('hltQuadCentralJet45') + " \
                "512       * filter('hltQuadPFCentralJetLooseID45') + " \
                "1024      * max(filter('hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet'), filter('hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet')) + " \
                "2048      * max(filter('hltBTagCaloCSVp05Double'), filter('hltBTagCaloDeepCSVp17Double')) + " \
                "4096      * filter('hltPFCentralJetLooseIDQuad30') + " \
                "8192      * filter('hlt1PFCentralJetLooseID75') + " \
                "16384     * filter('hlt2PFCentralJetLooseID60') + " \
                "32768     * filter('hlt3PFCentralJetLooseID45') + " \
                "65536     * filter('hlt4PFCentralJetLooseID40') + " \
                "131072    * max(filter('hltBTagPFCSVp070Triple'), max(filter('hltBTagPFDeepCSVp24Triple'), filter('hltBTagPFDeepCSV4p5Triple')) )+ " \
                "262144    * filter('hltHpsOverlapFilterDeepTauDoublePFTau*PFJet*') + " \
                "524288   * filter('*CrossCleaned*MediumDeepTauDitauWPPFTau*') + " \
                "1048576   * filter('*CrossCleanedUsingDiJetCorrChecker*')"
                )
process.triggerObjectTable.selections[4].qualityBitsDoc = cms.string(
                "Jet bits: bit 0 for VBF cross-cleaned from loose iso PFTau, bit 1 for hltBTagCaloCSVp087Triple, bit 2 for hltDoubleCentralJet90, bit 3 for hltDoublePFCentralJetLooseID90," \
                " bit 4 for hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet, bit 5 for hltQuadCentralJet30, bit 6 for hltQuadPFCentralJetLooseID30," \
                " bit 7 for hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF or hltL1sQuadJetCIorTripleJetVBFIorHTT," \
                " bit 8 for hltQuadCentralJet45, bit 9 for hltQuadPFCentralJetLooseID45," \
                " bit 10  for hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet or hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet" \
                " bit 11 for hltBTagCaloCSVp05Double or hltBTagCaloDeepCSVp17Double, bit 12 for hltPFCentralJetLooseIDQuad30, bit 13 for hlt1PFCentralJetLooseID75," \
                " bit 14 for hlt2PFCentralJetLooseID60, bit 15 for hlt3PFCentralJetLooseID45, bit 16 for hlt4PFCentralJetLooseID40," \
                " bit 17 for hltBTagPFCSVp070Triple or hltBTagPFDeepCSVp24Triple or hltBTagPFDeepCSV4p5Triple,"\
                " bit 18 for Double tau + jet,"\
                " bit 19 for VBF cross-cleaned from medium deeptau PFTau,"+
                " bit 20 for VBF cross-cleaned using dijet correlation checker ")
process.triggerObjectTable.selections.append(
            cms.PSet(
            name = cms.string("BoostedTau"),
            id = cms.int32(1515),
            sel = cms.string("type(85) && pt > 120 && coll('hltAK8PFJetsCorrected') && filter('hltAK8SinglePFJets*SoftDropMass40*ParticleNetTauTau')"),
            l1seed = cms.string("type(-99)"),
            l1deltaR = cms.double(0.3),
            l2seed = cms.string("type(85)  && coll('hltAK8CaloJetsCorrectedIDPassed')"),
            l2deltaR = cms.double(0.3),
            skipObjectsNotPassingQualityBits = cms.bool(True),
            qualityBits = cms.string(
                "filter('hltAK8SinglePFJets*SoftDropMass40*ParticleNetTauTau')"
                ),
            qualityBitsDoc = cms.string("Bit 0 for HLT_AK8PFJetX_SoftDropMass40_PFAK8ParticleNetTauTau0p30")))

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion