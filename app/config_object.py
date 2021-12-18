from omegaconf import OmegaConf, DictConfig
import hydra


@hydra.main(config_path="../config", config_name="config_object")
def curr_app(cfg: DictConfig):
    # config value
    assert cfg.node.loompa == 10
    assert cfg["node"]["loompa"] == 10

    # config var
    assert cfg.node.zippity == 10
    assert cfg.node.do == "oompa 10"

    # config not
    try:
        assert cfg.node.waldo is None
    except Exception as e:
        print(e.msg)


if __name__ == "__main__":
    curr_app()
