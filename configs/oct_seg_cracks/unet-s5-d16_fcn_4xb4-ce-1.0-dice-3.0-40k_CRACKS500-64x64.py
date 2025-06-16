_base_ = ["../unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py"]

#specify the dataset root
dataset_root = "/home/david/Downloads/CrackDataset/generated_dataset"
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