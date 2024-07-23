set config_path="chuteConfig.yml"

call conda activate yolov8
call python calibrate/undistort_videos.py --config_path %config_path%

cd detection
set new_path=../%config_path%
call python track.py --config_path %new_path%

cd ../classification

call python test.py --config_path %new_path%

cd ../segmentation

call python segment.py --config_path %new_path%

cd ..