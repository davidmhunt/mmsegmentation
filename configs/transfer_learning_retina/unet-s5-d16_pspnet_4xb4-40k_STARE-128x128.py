_base_ = ["../unet/unet-s5-d16_pspnet_4xb4-40k_stare-128x128.py"]

#specify the dataset root
dataset_root = "/data/transfer_learning_retina/DME"
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