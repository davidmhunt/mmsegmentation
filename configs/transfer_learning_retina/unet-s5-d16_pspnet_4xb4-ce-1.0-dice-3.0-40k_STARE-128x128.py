_base_ = ["../unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py"]

#specify the dataset root
dataset_root = "/home/david/Downloads/transfer_learning_retina/STARE"
train_dataloader = dict(
    dataset = dict(
        dataset = dict(
            data_root = dataset_root
        )
    )
)

val_dataloader = dict(
    dataset = dict(
        data_root = dataset_root
    )
)

test_dataloader = dict(
    dataset = dict(
        data_root = dataset_root
    )
)