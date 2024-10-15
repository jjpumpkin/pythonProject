# pip install split-folders
import splitfolders
# train/validation/test 폴더로 분할
splitfolders.ratio('./whale', output='split_whale', ratio=(.8,.0,.2))
