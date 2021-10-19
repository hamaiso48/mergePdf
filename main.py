import PyPDF2

FILE_PATH = './files/template.pdf'
CONFIDENTIAL_FILE_PATH = './files/abst.pdf'
OUTPUT_FILE_PATH = './files/executive_order_merged.pdf'


class PDFMerge:
    def __init__(self):
        self.f  = open(FILE_PATH, mode='rb')
        self.cf = open(CONFIDENTIAL_FILE_PATH, mode='rb')
        self.of = open(OUTPUT_FILE_PATH, mode='wb')

        self.PDFMerge()

    def PDFMerge(self):
        # マージするConfidential
        conf_reader = PyPDF2.PdfFileReader(self.cf)
        conf_page = conf_reader.getPage(0)    
        # マージ対象のファイル
        reader = PyPDF2.PdfFileReader(self.f)    
        writer = PyPDF2.PdfFileWriter()    
        for page_num in range(0, reader.numPages):
            obj = reader.getPage(page_num)
            obj.mergePage(conf_page)
            
            writer.addPage(obj)
            
        # ファイルへの書き込み
        writer.write(self.of)

if __name__ == '__main__':
	pdfmerge = PDFMerge() 