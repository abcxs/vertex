_base_ = './tf_faster_rcnn_r50_fpn_1x_building.py'

model = dict(
    neck=[
        dict(
            type='TFFPN',
            in_channels=[256, 512, 1024, 2048],
            out_channels=256,
            num_outs=4),
        dict(
            type='DFPN',
            in_channels=256,
            num_levels=4,
            refine_type='non_local')
    ])

img_norm_cfg = dict(
    mean=[0,], std=[255,], to_rgb=False)
train_pipeline = [
    dict(type='LoadTifFromFile', extra='ms'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 512), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadTifFromFile', extra='ms'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 512),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    train=dict(
        pipeline=train_pipeline),
    val=dict(
        pipeline=test_pipeline),
    test=dict(
        pipeline=test_pipeline))
