import os
import yaml

def load_config(path="config/default.yaml"):
  with open(path, "r") as f:
    cfg = yaml.safe_load(f)

  base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  cfg["paths"]["data_dir"] = os.path.join(base, cfg["paths"]["data_dir"])
  cfg["paths"]["sentiment_model_path"] = os.path.join(base, cfg["paths"]["data_dir"],
                                                      cfg["paths"]["sentiment_model_file"])

  return cfg
