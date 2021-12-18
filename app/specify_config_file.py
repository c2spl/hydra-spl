from omegaconf import OmegaConf, DictConfig
import hydra


@hydra.main(config_path="../config", config_name="specify_config")
def curr_app(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    curr_app()
