from WMCore.Configuration import Configuration 
config = Configuration()

config.section_("General")
config.General.requestName = 'EmbeddingRun2018A_MuTauFinalState'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'scripts/embedding_nanoAOD_18.py'

config.section_("Data")
config.Data.inputDataset = '/EmbeddingRun2018A/MuTauFinalState-inputDoubleMu_106X_ULegacy_miniAOD-v1/USER'
config.Data.inputDBS = 'phys03'	
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 3000

config.Data.outLFNDirBase    = '/store/user/skkwan/EmbeddedNanoProduction'
config.Data.publication = True
config.Data.outputDatasetTag = '106X_UL18_MiniAODv1_NanoAODv9'

config.section_("Site")
config.Site.storageSite = 'T2_US_Wisconsin'
