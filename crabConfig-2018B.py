from WMCore.Configuration import Configuration 
config = Configuration()

config.section_("General")
config.General.requestName = 'EmbeddingRun2018B_MuTauFinalState-inputDoubleMu'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'scripts/nanoProd_18abc_NANO_CRAB.py'

config.section_("Data")
config.Data.inputDataset = '/EmbeddingRun2018B/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER'	
config.Data.inputDBS = 'phys03'	
config.Data.splitting = 'FileBased'
# config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_10_6_16_102X_EmbeddingRun2018B_MuTauFinalState-inputDoubleMu'	

config.section_("Site")
config.Site.storageSite = 'T2_US_Wisconsin'
