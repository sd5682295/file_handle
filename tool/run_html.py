# from lxml import html

# from demo2.tool.qa import qa
from setting import setting
from tool.IO_Handle import IO
from tool.dir_handle import dir_handle
from tool.qa import qa


class run_md(setting):
    def __init__(self, ihtml):
        self.html = ihtml
        dh = dir_handle()
        self.file_name = self.html.split('/')[-1].replace('.'+self.input_type, '')

    def run(self):
        datas = IO.read_file(path=self.html, my_filter="=>")

        my_qa = qa()
        data_str = my_qa.data_handle(datas, self.file_name)

        IO.out_put('{}\{}.{}'.format(self.output_path,self.file_name,self.output_type), data_str)

if __name__ == "__main__":

    rh = run_md('../md/Django 如何处理一个请求.md')
    rh.run()