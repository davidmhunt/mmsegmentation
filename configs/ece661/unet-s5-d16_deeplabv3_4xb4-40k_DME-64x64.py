_base_ = ["../unet/unet-s5-d16_deeplabv3_4xb4-40k_drive-64x64.py"]

#specify the dataset root
dataset_root = "/data/david/DME"
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