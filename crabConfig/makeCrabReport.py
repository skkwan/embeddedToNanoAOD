import os
import yaml

config_file = open("datasetConfig.yml")

config = yaml.safe_load(config_file)

os.system("rm report_2016.txt")

#for era in ["Embed2018", "Embed2017", "Embed2016_HIPM", "Embed2016"]:
for era in ["Embed2016_HIPM", "Embed2016"]:
   for name in config[era]["datasets"]:
      # Report
      command = "echo '>>> {}' | tee -a report.txt".format(name, name)
      os.system(command)
      command = "crab status -d crab_projects/crab_{} | tee -a report_2016.txt".format(name)
      print(command)
      os.system(command)
