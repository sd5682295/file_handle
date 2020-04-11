from setting import setting
from tool.tool_base.dir_handle_base import dir_tool

class dir_handle(dir_tool, setting):
    def __init__(self):
        pass

    def get_file_typle(self):
        return self.input_type

    def get_html_iter(self):
        return self.__get_html_iter()

    def create_input_output(self):
        return self.__create_input_output()

    def __get_html_iter(self):
        return self.get_file_list("{}".format(self.input_path), self.input_type)

    def __create_input_output(self):
        self.create_dir(self.input_path)
        self.create_dir(self.output_path)



if __name__ == "__main__":
    dh = dir_handle()
    print(dh.watch_data(dh.get_html_iter()))
