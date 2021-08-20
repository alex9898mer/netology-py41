from re import search
from typing import List, Dict, Union
import os


class FilesModule:
    _output_file_name: str = "output.txt"

    def __init__(self, data_dir_path: str, file_names: List[str]):
        self._files_info: Dict[str, Dict[str, Union[List[str], int]]] = {}
        self._output_file_location: str = f"{data_dir_path}/output"
        self._prepare_output()
        self._parse_files(data_dir_path, file_names)

    def _prepare_output(self) -> None:
        """
            Method to check for output folder and create it if not exist
        :return:
        """
        try:
            os.mkdir(self._output_file_location)
        except FileExistsError:
            pass

    def _parse_files(self, data_dir: str, file_names: List[str]):
        """
            Method to parse input list of file name and assemble files info dictionary
        :param data_dir: Root directory with data files
        :param file_names: List of filenames to look for
        :return:
        """
        for file in file_names:
            with open(
                file=f"{data_dir}/{file}", mode="r", encoding="utf-8"
            ) as input_file:
                file_name: str = search(
                    r"([^/|\\])((\w)|(\w*\D*))(\.)(\w{2,5}$)", input_file.name
                ).group()
                file_content: List[str] = input_file.readlines()
                self._files_info.update(
                    {
                        file_name: {
                            "content": file_content,
                            "line_count": file_content.__len__(),
                        }
                    }
                )

    def _sorted_files(self, sorting_key: str) -> List[str]:
        """
            Method to sort files info dictionary by specified key
        :param sorting_key: key by which sorting will be made
        :return: List of sorted root keys
        """
        return sorted(
            self._files_info,
            key=lambda file_name: self._files_info[file_name][sorting_key],
        )

    def write_output_file(self) -> None:
        """
            Method to write output file with needed data from parsed files
        :return:
        """
        with open(
            file=f"{self._output_file_location}/{self._output_file_name}",
            mode="w",
            encoding="utf-8",
        ) as output_file:
            for file_name in self._sorted_files("line_count"):
                output_file.write(
                    f"{file_name}\n"
                    f"{self._files_info[file_name]['line_count']}\n"
                    f"{''.join(self._files_info[file_name]['content'])}\n"
                )
            print(f"Файл создан по данному пути [ {output_file.name} ]")

    def read_output_file_content(self):
        """
            Method to read assembled output file to the console
        :return:
        """
        with open(
            file=f"{self._output_file_location}/{self._output_file_name}",
            mode="r",
            encoding="utf-8",
        ) as output_file:
            print(
                f"Содержимое файла:\n{'-' * 60}\n" f"{''.join(output_file.readlines())}"
            )
