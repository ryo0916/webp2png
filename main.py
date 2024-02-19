# まずCUIでWebP→PNG変換器を作る
from PIL import Image
import glob, os
import sys

# 変換先拡張子
IMG_FORMAT = 'png'

# 画像を取得
file = glob.glob('./' + '*.webp')

# 画像名を取得
file = str(file[0])
file_name = os.path.splitext(os.path.basename(file))[0]

# 変換
img = Image.open(file).convert('RGB')

# 保存
img.save('./' + file_name + '.' + IMG_FORMAT, quality = 100)
