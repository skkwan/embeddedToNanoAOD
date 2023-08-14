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

    #'/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018A/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/408d598c-12f0-49b3-b056-754b783816f4.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018A/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/0c687e2a-58dd-4f69-a480-80f4656cb0b5.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018A/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/b0594417-daa3-4db7-a290-03a3ff203884.root', 
    '/store/group/rucio/pog_tau_group/ul_embedding/large_miniAOD_v2/ElTauFinalState/EmbeddingRun2018A/MINIAOD/inputDoubleMu_106X_ULegacy_miniAOD-v1/0000/b0594417-daa3-4db7-a290-03a3ff203884.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange( (
        "315252:38-315252:38", "315252:41-315252:41", "315252:39-315252:39", "315252:43-315252:44", "315252:36-315252:37", 
    "315252:40-315252:40", "315252:42-315252:42", "315257:29-315257:29", "315257:38-315257:38", "315257:40-315257:41", 
    "315257:53-315257:53", "315257:57-315257:57", "315257:59-315257:59", "315257:61-315257:61", "315257:64-315257:64", 
    "315257:73-315257:73", "315257:7-315257:7", "315257:11-315257:11", "315257:28-315257:28", "315257:46-315257:46", 
    "315257:48-315257:48", "315257:62-315257:62", "315257:66-315257:66", "315257:68-315257:68", "315257:87-315257:87", 
    "315257:90-315257:90", "315257:3-315257:3", "315257:15-315257:15", "315257:20-315257:20", "315257:24-315257:24", 
    "315257:34-315257:34", "315257:45-315257:45", "315257:50-315257:51", "315257:56-315257:56", "315257:58-315257:58", 
    "315257:65-315257:65", "315257:74-315257:74", "315257:76-315257:77", "315257:2-315257:2", "315257:4-315257:4", 
    "315257:10-315257:10", "315257:12-315257:12", "315257:55-315257:55", "315257:63-315257:63", "315257:72-315257:72", 
    "315257:75-315257:75", "315257:82-315257:82", "315257:9-315257:9", "315257:14-315257:14", "315257:22-315257:23", 
    "315257:26-315257:26", "315257:42-315257:42", "315257:67-315257:67", "315257:69-315257:69", "315257:78-315257:79", 
    "315257:85-315257:86", "315257:91-315257:91", "315257:5-315257:6", "315257:16-315257:16", "315257:18-315257:19", 
    "315257:30-315257:30", "315257:37-315257:37", "315257:47-315257:47", "315257:52-315257:52", "315257:60-315257:60", 
    "315257:89-315257:89", "315257:17-315257:17", "315257:25-315257:25", "315257:27-315257:27", "315257:32-315257:33", 
    "315257:36-315257:36", "315257:39-315257:39", "315257:43-315257:44", "315257:70-315257:71", "315257:80-315257:81", 
    "315257:84-315257:84", "315257:1-315257:1", "315257:8-315257:8", "315257:13-315257:13", "315257:21-315257:21", 
    "315257:31-315257:31", "315257:35-315257:35", "315257:49-315257:49", "315257:54-315257:54", "315257:83-315257:83", 
    "315257:88-315257:88", "315257:92-315257:92", "315258:1-315258:1", "315259:124-315259:124", "315259:128-315259:128", 
    "315259:130-315259:130", "315259:135-315259:135", "315259:148-315259:148", "315259:151-315259:151", "315259:158-315259:158", 
    "315259:161-315259:163", "315259:165-315259:165", "315259:2-315259:2", "315259:10-315259:10", "315259:36-315259:37", 
    "315259:66-315259:67", "315259:106-315259:106", "315259:119-315259:119", "315259:133-315259:133", "315259:137-315259:137", 
    "315259:139-315259:139", "315259:141-315259:141", "315259:145-315259:145", "315259:147-315259:147", "315259:149-315259:150", 
    "315259:159-315259:159", "315259:177-315259:177", "315259:179-315259:179", "315259:181-315259:181", "315259:11-315259:11", 
    "315259:14-315259:14", "315259:23-315259:23", "315259:26-315259:26", "315259:34-315259:34", "315259:62-315259:62", 
    "315259:72-315259:72", "315259:76-315259:77", "315259:85-315259:86", "315259:108-315259:108", "315259:116-315259:116", 
    "315259:129-315259:129", "315259:153-315259:153", "315259:164-315259:164", "315259:175-315259:175", "315259:180-315259:180", 
    "315259:183-315259:183", "315259:4-315259:6", "315259:16-315259:16", "315259:47-315259:47", "315259:50-315259:50", 
    "315259:59-315259:59", "315259:71-315259:71", "315259:92-315259:92", "315259:96-315259:97", "315259:99-315259:99", 
    "315259:102-315259:102", "315259:118-315259:118", "315259:123-315259:123", "315259:127-315259:127", "315259:131-315259:131", 
    "315259:136-315259:136", "315259:138-315259:138", "315259:168-315259:168", "315259:174-315259:174", "315259:178-315259:178", 
    "315259:1-315259:1", "315259:3-315259:3", "315259:19-315259:19", "315259:42-315259:42", "315259:53-315259:56", 
    "315259:60-315259:60", "315259:65-315259:65", "315259:81-315259:81", "315259:87-315259:88", "315259:101-315259:101", 
    "315259:105-315259:105", "315259:121-315259:122", "315259:126-315259:126", "315259:142-315259:142", "315259:144-315259:144", 
    "315259:154-315259:154", "315259:156-315259:156", "315259:169-315259:169", "315259:15-315259:15", "315259:39-315259:39", 
    "315259:41-315259:41", "315259:49-315259:49", "315259:51-315259:51", "315259:61-315259:61", "315259:63-315259:63", 
    "315259:69-315259:69", "315259:74-315259:74", "315259:89-315259:90", "315259:103-315259:103", "315259:111-315259:111", 
    "315259:125-315259:125", "315259:134-315259:134", "315259:140-315259:140", "315259:155-315259:155", "315259:157-315259:157", 
    "315259:160-315259:160", "315259:170-315259:170", "315259:176-315259:176", "315259:182-315259:182", "315259:8-315259:9", 
    "315259:12-315259:12", "315259:18-315259:18", "315259:20-315259:21", "315259:29-315259:29", "315259:31-315259:31", 
    "315259:33-315259:33", "315259:35-315259:35", "315259:43-315259:43", "315259:45-315259:45", "315259:70-315259:70", 
    "315259:78-315259:78", "315259:80-315259:80", "315259:84-315259:84", "315259:91-315259:91", "315259:94-315259:94", 
    "315259:98-315259:98", "315259:100-315259:100", "315259:104-315259:104", "315259:107-315259:107", "315259:109-315259:110", 
    "315259:113-315259:113", "315259:115-315259:115", "315259:117-315259:117", "315259:132-315259:132", "315259:143-315259:143", 
    "315259:146-315259:146", "315259:152-315259:152", "315259:166-315259:166", "315259:172-315259:173", "315259:7-315259:7", 
    "315259:17-315259:17", "315259:22-315259:22", "315259:27-315259:27", "315259:40-315259:40", "315259:44-315259:44", 
    "315259:64-315259:64", "315259:75-315259:75", "315259:112-315259:112", "315259:114-315259:114", "315259:120-315259:120", 
    "315259:167-315259:167", "315259:171-315259:171", "315259:13-315259:13", "315259:24-315259:25", "315259:28-315259:28", 
    "315259:30-315259:30", "315259:32-315259:32", "315259:38-315259:38", "315259:46-315259:46", "315259:48-315259:48", 
    "315259:52-315259:52", "315259:57-315259:58", "315259:68-315259:68", "315259:73-315259:73", "315259:79-315259:79", 
    "315259:82-315259:83", "315259:93-315259:93", "315259:95-315259:95", "315264:3-315264:3", "315264:6-315264:6", 
    "315264:28-315264:28", "315264:31-315264:31", "315264:33-315264:34", "315264:128-315264:128", "315264:173-315264:173", 
    "315264:176-315264:176", "315264:191-315264:192", "315264:197-315264:197", "315264:214-315264:214", "315264:242-315264:242", 
    "315264:253-315264:253", "315264:257-315264:257", "315264:4-315264:4", "315264:9-315264:9", "315264:17-315264:17", 
    "315264:22-315264:22", "315264:25-315264:25", "315264:27-315264:27", "315264:56-315264:56", "315264:126-315264:126", 
    "315264:168-315264:168", "315264:193-315264:193", "315264:202-315264:202", "315264:208-315264:208", "315264:216-315264:216", 
    "315264:219-315264:220", "315264:222-315264:222", "315264:228-315264:228", "315264:244-315264:244", "315264:255-315264:255", 
    "315264:258-315264:258", "315264:5-315264:5", "315264:26-315264:26", "315264:32-315264:32", "315264:41-315264:41", 
    "315264:54-315264:54", "315264:169-315264:169", "315264:171-315264:171", "315264:196-315264:196", "315264:199-315264:199", 
    "315264:201-315264:201", "315264:205-315264:205", "315264:227-315264:227", "315264:233-315264:234", "315264:247-315264:248", 
    "315264:252-315264:252", "315264:1-315264:1", "315264:11-315264:11", "315264:20-315264:20", "315264:37-315264:37", 
    "315264:42-315264:42", "315264:44-315264:44", "315264:127-315264:127", "315264:178-315264:178", "315264:189-315264:190", 
    "315264:204-315264:204", "315264:209-315264:209", "315264:211-315264:211", "315264:224-315264:224", "315264:230-315264:230", 
    "315264:235-315264:236", "315264:249-315264:249", "315264:254-315264:254", "315264:256-315264:256", "315264:23-315264:23", 
    "315264:36-315264:36", "315264:125-315264:125", "315264:194-315264:194", "315264:215-315264:215", "315264:218-315264:218", 
    "315264:240-315264:241", "315264:246-315264:246", "315264:251-315264:251", "315264:7-315264:7", "315264:13-315264:13", 
    "315264:16-315264:16", "315264:18-315264:19", "315264:24-315264:24", "315264:35-315264:35", "315264:40-315264:40", 
    "315264:172-315264:172", "315264:203-315264:203", "315264:210-315264:210", "315264:212-315264:212", "315264:221-315264:221", 
    "315264:226-315264:226", "315264:229-315264:229", "315264:232-315264:232", "315264:237-315264:237", "315264:239-315264:239", 
    "315264:250-315264:250", "315264:2-315264:2", "315264:10-315264:10", "315264:14-315264:15", "315264:29-315264:29", 
    "315264:38-315264:38", "315264:167-315264:167", "315264:175-315264:175", "315264:187-315264:188", "315264:195-315264:195", 
    "315264:206-315264:206", "315264:213-315264:213", "315264:217-315264:217", "315264:223-315264:223", "315264:238-315264:238", 
    "315264:8-315264:8", "315264:12-315264:12", "315264:21-315264:21", "315264:30-315264:30", "315264:39-315264:39", 
    "315264:43-315264:43", "315264:55-315264:55", "315264:170-315264:170", "315264:174-315264:174", "315264:177-315264:177", 
    "315264:198-315264:198", "315264:200-315264:200", "315264:207-315264:207", "315264:225-315264:225", "315264:231-315264:231", 
    "315264:243-315264:243", "315264:245-315264:245", "315264:259-315264:259", "315264:65-315264:65", "315264:71-315264:71", 
    "315264:78-315264:78", "315264:82-315264:82", "315264:91-315264:91", "315264:93-315264:93", "315264:103-315264:103", 
    "315264:113-315264:113", "315264:115-315264:115", "315264:121-315264:121", "315264:130-315264:130", "315264:136-315264:136", 
    "315264:140-315264:140", "315264:147-315264:147", "315264:153-315264:153", "315264:159-315264:159", "315264:166-315264:166", 
    "315264:184-315264:184", "315264:45-315264:45", "315264:47-315264:47", "315264:62-315264:62", "315264:68-315264:68", 
    "315264:80-315264:80", "315264:90-315264:90", "315264:94-315264:94", "315264:102-315264:102", "315264:106-315264:106", 
    "315264:129-315264:129", "315264:134-315264:135", "315264:142-315264:142", "315264:158-315264:158", "315264:160-315264:160", 
    "315264:162-315264:162", "315264:66-315264:66", "315264:84-315264:84", "315264:108-315264:108", "315264:110-315264:110", 
    "315264:124-315264:124", "315264:149-315264:149", "315264:183-315264:183", "315264:59-315264:59", "315264:61-315264:61", 
    "315264:76-315264:77", "315264:79-315264:79", "315264:85-315264:85", "315264:92-315264:92", "315264:99-315264:99", 
    "315264:101-315264:101", "315264:112-315264:112", "315264:120-315264:120", "315264:122-315264:122", "315264:154-315264:154", 
    "315264:181-315264:181", "315264:185-315264:185", "315264:69-315264:69", "315264:81-315264:81", "315264:83-315264:83", 
    "315264:100-315264:100", "315264:107-315264:107", "315264:111-315264:111", "315264:116-315264:116", "315264:138-315264:138", 
    "315264:144-315264:145", "315264:148-315264:148", "315264:165-315264:165", "315264:182-315264:182", "315264:46-315264:46", 
    "315264:64-315264:64", "315264:67-315264:67", "315264:72-315264:72", "315264:88-315264:88", "315264:104-315264:104", 
    "315264:118-315264:118", "315264:123-315264:123", "315264:133-315264:133", "315264:141-315264:141", "315264:151-315264:151", 
    "315264:155-315264:156", "315264:161-315264:161", "315264:163-315264:163", "315264:60-315264:60", "315264:70-315264:70", 
    "315264:86-315264:87", "315264:97-315264:98", "315264:109-315264:109", "315264:114-315264:114", "315264:117-315264:117", 
    "315264:119-315264:119", "315264:143-315264:143", "315264:146-315264:146", "315264:150-315264:150", "315264:152-315264:152", 
    "315264:157-315264:157", "315264:164-315264:164", "315264:186-315264:186", "315264:63-315264:63", "315264:73-315264:75", 
    "315264:89-315264:89", "315264:95-315264:96", "315264:105-315264:105", "315264:131-315264:132", "315264:137-315264:137", 
    "315264:139-315264:139", "315264:179-315264:180", "315267:19-315267:20", "315267:23-315267:23", "315267:27-315267:27", 
    "315267:46-315267:46", "315267:60-315267:62", "315267:66-315267:66", "315267:71-315267:71", "315267:73-315267:73", 
    "315267:79-315267:79", "315267:92-315267:92", "315267:95-315267:95", "315267:107-315267:107", "315267:1-315267:1", 
    "315267:12-315267:12", "315267:18-315267:18", "315267:29-315267:30", "315267:36-315267:36", "315267:50-315267:50", 
    "315267:52-315267:52", "315267:54-315267:54", "315267:56-315267:56", "315267:64-315267:64", "315267:72-315267:72", 
    "315267:84-315267:84", "315267:2-315267:2", "315267:8-315267:8", "315267:16-315267:16", "315267:31-315267:31", 
    "315267:58-315267:58", "315267:83-315267:83", "315267:96-315267:96", "315267:109-315267:110", "315267:11-315267:11", 
    "315267:33-315267:33", "315267:35-315267:35", "315267:49-315267:49", "315267:51-315267:51", "315267:55-315267:55", 
    "315267:63-315267:63", "315267:77-315267:77", "315267:82-315267:82", "315267:85-315267:85", "315267:94-315267:94", 
    "315267:6-315267:6", "315267:13-315267:13", "315267:25-315267:25", "315267:34-315267:34", "315267:37-315267:40", 
    "315267:76-315267:76", "315267:81-315267:81", "315267:106-315267:106", "315267:3-315267:3", "315267:9-315267:9", 
    "315267:15-315267:15", "315267:26-315267:26", "315267:48-315267:48", "315267:59-315267:59", "315267:74-315267:74", 
    "315267:97-315267:97", "315267:7-315267:7", "315267:21-315267:21", "315267:24-315267:24", "315267:32-315267:32", 
    "315267:57-315267:57", "315267:65-315267:65", "315267:67-315267:67", "315267:69-315267:70", "315267:91-315267:91", 
    "315267:93-315267:93", "315267:4-315267:5", "315267:10-315267:10", "315267:14-315267:14", "315267:17-315267:17", 
    "315267:22-315267:22", "315267:28-315267:28", "315267:47-315267:47", "315267:53-315267:53", "315267:68-315267:68", 
    "315267:75-315267:75", "315267:78-315267:78", "315267:80-315267:80", "315267:108-315267:108", "315267:225-315267:225", 
    "315267:227-315267:228", "315267:172-315267:172", "315267:176-315267:176", "315267:221-315267:221", "315267:224-315267:224", 
    "315267:241-315267:241", "315267:229-315267:232", "315267:238-315267:238", "315267:220-315267:220", "315267:239-315267:239", 
    "315267:173-315267:173", "315267:236-315267:236", "315267:235-315267:235", "315267:174-315267:175", "315267:218-315267:219", 
    "315267:226-315267:226", "315267:234-315267:234", "315267:237-315267:237", "315267:222-315267:223", "315267:233-315267:233", 
    "315267:240-315267:240", "315265:29-315265:29", "315265:27-315265:28", "315265:26-315265:26", "315270:26-315270:26", 
    "315270:44-315270:44", "315270:55-315270:55", "315270:69-315270:69", "315270:71-315270:71", "315270:106-315270:106", 
    "315270:263-315270:263", "315270:292-315270:292", "315270:295-315270:295", "315270:297-315270:297", "315270:304-315270:304", 
    "315270:317-315270:317", "315270:322-315270:322", "315270:326-315270:326", "315270:338-315270:338", "315270:346-315270:346", 
    "315270:375-315270:376", "315270:379-315270:379"

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
    fileName = cms.untracked.string('file:test_nano_2018A_ElTau_1-1.root'),
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
