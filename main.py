# Tkinter
import tkinter as tk
root = tk.Tk()
root.title('webp2png')
root.geometry('200x100')

# 変換と保存
def convert():
    img = Image.open(file).convert('RGB')
    img.save('./' + file_name + '.' + IMG_FORMAT, quality = 100)

# まずCUIでWebP→PNG変換器を作る
from PIL import Image
import glob, os

# 変換先拡張子
IMG_FORMAT = 'png'

# 画像を取得
file = glob.glob('./' + '*.webp')

# 画像名を取得
file = str(file[0])
file_name = os.path.splitext(os.path.basename(file))[0]

# 画像名を表示
file_label = tk.Label(root, text=file_name)
file_label.place(x=20, y=20)

# 変換ボタン
button = tk.Button(root, text='convert', command=convert)
button.pack()
button.place(x=60, y=60)
root.mainloop()