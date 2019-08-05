import sys
import pdfplumber
import pandas as pd
from tqdm import tqdm

'''
将pdf中的文字和表格分开储存
没用使用os模块，运行前检查保存的目录是否存在
可以直接运行，也可以在终端中运行
终端运行方法
python /xx/pdfread.py '/xx/xx.pdf' './1.txt' './2.csv'
python 代码路径 pdf路径 文本保存路径 表格保存路径
'''


class Pdf(object):
    def __init__(self, pdf_path, txt_path, csv_path):
        self.pdf_path = pdf_path
        self.txt_path = txt_path
        self.csv_path = csv_path

        self.pdf = pdfplumber.open(self.pdf_path)
        self.txt = open(self.txt_path, 'w')
        self.csv = open(self.csv_path, 'w')

    def work(self):
        for page in tqdm(self.pdf.pages):
            table = page.extract_tables()

            for t in table:
                df = pd.DataFrame(t[1:], columns=t[0])
                name = pd.DataFrame([page.page_number])
                name.to_csv(self.csv_path, mode='a', header=0, index=0)
                df.to_csv(self.csv_path, mode='a')

            text = page.extract_text()
            if len(table) > 0:
                self.txt.write('\n见表格%s\n' % page.page_number)
            else:
                self.txt.write(text)

        self.pdf.close()
        self.txt.close()
        self.csv.close()


if __name__ == '__main__':
    try:
        pdf_path = sys.argv[1]
        txt_path = sys.argv[2]
        csv_path = sys.argv[3]
    except:
        pdf_path = input('pdf_path:')
        txt_path = input('txt_path:')
        csv_path = input('csv_path:')

    pdf = Pdf(pdf_path, txt_path, csv_path)
    pdf.work()
