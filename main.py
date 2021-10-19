import PyPDF2

form_file   = './files/form.pdf'
input_file  = './files/imput.pdf'
output_file = './files/output.pdf'

class PDFMerge:

    def __init__(self):
        self.f = open(form_file, mode='rb')
        self.i = open(input_file, mode='rb')
        self.o = open(output_file, mode='wb')

        self.PDFMerge(-6.5,-20)

    def PDFMerge(self, i_X, i_Y):
        # 入力ファイル
        input_reader  = PyPDF2.PdfFileReader(self.i)
        input_page    = input_reader.getPage(0)    
        # 下地となるファイル
        form_reader   = PyPDF2.PdfFileReader(self.f)
        # 出力ファイル
        output_writer = PyPDF2.PdfFileWriter()

        for page_num in range(0, form_reader.numPages):

            # 下地ファイルからページ指定してページ取得
            form = form_reader.getPage(page_num)
            p_width  = form.mediaBox.getUpperRight_x()
            p_height = form.mediaBox.getUpperRight_y()
            
            # 下地のページと同じサイズで白紙ページ作成
            p = PyPDF2.pdf.PageObject.createBlankPage(width=p_width,height=p_height)
            # 白紙ページに下地ページを置く
            p.mergePage(form)
            # 入力ページを位置指定して置く
            p.mergeTranslatedPage(input_page,i_X,i_Y)

            # 圧縮して書き出し
            p.compressContentStreams()
            output_writer.addPage(p)
            
        # ファイルへの書き込み
        output_writer.write(self.o)

if __name__ == '__main__':
	pdfmerge = PDFMerge() 