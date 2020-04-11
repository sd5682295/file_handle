import os

from tool.IO_Handle import IO
from tool.tool_base.base import base


class setting(base):
    BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
    input_path = os.path.join(BASE_DIR,"input")
    output_path = os.path.join(BASE_DIR, "output")
    input_type = 'md'
    output_type = "txt"

if __name__ == "__main__":
    # for file_path in base.input_list:
    #     datas = IO.read_file(file_path)
    # dh = dir_handle()
    # files = dh.get_html_iter()
    # [run_md(file).run() for file in files]
    st = setting()
    print(st.input_path)