from omegaconf import DictConfig, OmegaConf
import hydra


@hydra.main(config_path=None)
def curr_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    curr_app()
