"""Select an item from a config group with +GROUP=OPTION"""

from omegaconf import DictConfig, OmegaConf
import hydra


@hydra.main(config_path="../config")
def curr_app(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    curr_app()
