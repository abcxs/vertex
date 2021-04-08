_base_ = './polyrnn_r50_fpn_1x_building_edge.py'
model = dict(
    roi_head=dict(
        polygon_head=dict(
            polyrnn_head=dict(
                max_time_step=10))),
    # model training and testing settings
    train_cfg=dict(
        rcnn=dict(max_polygon_len=10)))