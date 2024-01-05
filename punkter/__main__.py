import os
import re
import subprocess
import config

def symlink(src, dst):
    #check if dst is folder
    if dst.endswith('/'):
        dst = dst[:-1]
    
    if dst.startswith('~'):
        home_dir_src = os.path.expanduser('~')
        dst = home_dir_src+dst[1:]

    #unlink if symlink already exists
    if os.path.islink(dst):
        os.unlink(dst)
    src = os.getcwd()+"/"+src
    print(f"{src} => {dst}")
    os.symlink(src, dst)

def iterate_config_sections(config_sections, target_folder):
    for config in config_sections:
        src = os.getcwd()+"/"+config
        dst = target_folder+config
        symlink(config, dst)

def iterate_custom_section():
    for src, dst in config.custom.items():
        symlink(src, dst)

def import_scripts(dst, config_sections):
    #create scripts folder if it doesn't exist
    if not os.path.isdir(dst):
        os.makedirs(dst)
        #add folder to path
        subprocess.run["bash", "-c", "export PATH=$PATH:"+dst+"/"]
    for script in config_sections:
        dst = dst+"/"+script
        src = "scripts/"+script
        symlink(src, dst)

def add_alias_to_bashrc(aliases):
    home_dir_src = os.path.expanduser('~')
    with open(home_dir_src+"/.bashrc", 'r') as file:
        data = file.read()

    #remove stuff between alias config_sections
    modified_data = re.sub(r'####ALIAS SECTION.*?####END ALIAS SECTION\n', '', data, flags=re.DOTALL)
    alias_section = "####ALIAS SECTION\n#add aliases to punkter config.py file, otherwise it will be removed"
    for alias in aliases:
        alias_section += "\nalias "+alias
    alias_section = alias_section
    alias_section += "\n####END ALIAS SECTION"

    with open(home_dir_src+"/.bashrc", 'w') as file:
        #file.write(modified_data+alias_section)
        print(modified_data+alias_section)

home_dir_src = os.path.expanduser('~/')
config_dir_src = home_dir_src+".config/"


import_scripts(config.scripts_folder, config.scripts)
iterate_config_sections(config.config_dir, config_dir_src)
iterate_custom_section()
#add_alias_to_bashrc(config.aliases)
