from WMCore.Configuration import Configuration 
config = Configuration()

config.section_("General")
config.General.requestName = 'REPLACEME_DATASET_NAME'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'REPLACEME_PATH_TO_CMSRUN'

config.section_("Data")
config.Data.inputDataset = 'REPLACEME_DAS_DATASET'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'Automatic'

config.Data.outLFNDirBase    = '/store/user/skkwan/embeddedNanoUL/REPLACEME_DATASET_NAME'
config.Data.publication = True
config.Data.outputDatasetTag = 'REPLACEME_DATASET_NAME_REPLACEME_PRODTAG'

config.section_("Site")
config.Site.storageSite = 'T2_US_Wisconsin'
