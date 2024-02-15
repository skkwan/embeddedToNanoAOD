import os
import yaml

config_file = open("datasetConfig.yml")

config = yaml.safe_load(config_file)

os.system("mkdir -p temp/")

# for era in ["Embed2018", "Embed2017", "Embed2016_HIPM", "Embed2016"]:
for era in ["Embed2018"]:
   for name in config[era]["datasets"]:
      # Make the crab file
      crabCfgName = "temp/crabConfig-test-{}.py".format(name)
      command = "cp {} {}".format(config[era]["template_crab"], crabCfgName)
      print(command)
      os.system(command)

      # Replace the strings in the crab cfg
      with open(crabCfgName, 'r') as file:
      
         # Reading the content of the file
         # using the read() function and storing
         # them in a new variable
         data = file.read()
      
         # Searching and replacing the text
         # using the replace() function
         data = data.replace("REPLACEME_DATASET_NAME", name)
         data = data.replace("REPLACEME_PATH_TO_CMSRUN", config[era]["cmsRun_script"])
         data = data.replace("REPLACEME_DAS_DATASET",  config[era]["datasets"][name])
         data = data.replace("REPLACEME_PRODTAG", config["prodtag"])
  
      # Opening our text file in write only
      # mode to write the replaced content
      with open(crabCfgName, 'w') as file:
      
         # Writing the replaced data in our
         # text file
         file.write(data)

      

      # command = "crab submit -c {}".format(crabCfgName)
      # print(command)
      # os.system(command)
