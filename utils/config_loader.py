#it is going to load the configs
import yaml
import os

def load_config(config_path: str = "config/config.yaml") -> dict:
    # Get the absolute path of the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, config_path)
    
    with open(full_path, "r") as file:
        config = yaml.safe_load(file)
    print(config)
    return config

if __name__ == "__main__":
    load_config()
