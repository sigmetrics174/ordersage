# SSH Configurations
#workers = ["hostname1","hostname2"]
user = "user"
keyfile = "/home/user/.ssh/key"
port_num = 22

# Experiemnts Repo
repo = "<URL for experiment repo>"

# Filepaths and commands
init_script_call = "cd <name of the repo> && bash initialize.sh"
experiment_script_call = "cd <name of the repo> && python3 <experiment script>"
results_dir = "~/<name of the repo>/results"
results_file = "results.txt"

# Options
n_runs = 10
verbose = True
reboot = True
seed = None
