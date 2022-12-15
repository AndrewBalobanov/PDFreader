# -*- coding: utf-8 -*-

class PDFscan():
    def __init__(self, path):
        self.path = path
        self.page_list = []

    # сканирует файл на входе и преобразует его в список словарей
    def watch(self):
        import PyPDF2
        import PaperSize
        import pathlib
        with open(self.path, 'rb') as pdf_file:
            from collections import namedtuple

            Dimensions = namedtuple("Dimensions", ["width", "height"])
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            for num_page in range(pdf_reader.getNumPages()):

                box = pdf_reader.getPage(num_page)
                base_width = float(box.mediaBox.getWidth()) * 0.3527
                base_height = float(box.mediaBox.getHeight()) * 0.3527

                tolerance = 0.3

                width = int(base_width + (tolerance if base_width > 0 else -tolerance))
                height = int(base_height + (tolerance if base_height > 0 else -tolerance))

                size = Dimensions(width, height)

                if size in PaperSize.size_dict.keys():
                    params = PaperSize.size_dict[size]
                    new_page = {'Имя файла': pathlib.Path(self.path).stem, 'Номер листа': num_page + 1,
                                'Формат': params.size, 'Ориентация': params.orientation}
                    self.page_list.append(new_page)

    # преобразует список словарей в dataframe
    def base_frame(self):
        import pandas as pd
        df = pd.DataFrame(self.page_list)
        return df

    # записывает полученный dataframe в excel
    def write(self, frame):
        frame.to_excel("output.xlsx")

    # запускает алгоритм
    def action(self):
        self.watch()
        self.base_frame()
        self.write(self.base_frame())


class Prj_sum():
    def __init__(self, frame_list, name='Summary'):
        self.frame_list = frame_list
        self.name = name
        self.out = self.prj_summary()

    def prj_summary(self):
        import pandas as pd
        main_frame = pd.concat(self.frame_list)
        main_frame.reset_index(drop=True, inplace=True)
        main_frame.index += 1
        main_frame.insert(0, "№", main_frame.index)
        return main_frame


class Page_calc():
    def __init__(self, frame_list, name='Page size calc'):
        self.frame_list = frame_list
        self.name = name
        self.out = self.page_size_calc()

    def page_size_calc(self):
        import pandas as pd
        import aux_func as af

        for frame in self.frame_list:
            frame.drop(columns=['Ориентация'], axis=1, inplace=True)
            frame.drop(columns=['Номер листа'], axis=1, inplace=True)
            frame.reset_index(drop=True, inplace=True)
            frame.index += 1

        dict_list = []
        for frame_num in range(len(self.frame_list)):
            filename = self.frame_list[frame_num].loc[1, 'Имя файла']
            formats_list = []

            for format in self.frame_list[frame_num]['Формат']:
                formats_list.append(format)

            crop_formats_list = list(af.doc_list(formats_list))

            new_dictionary = {}
            new_dictionary['Имя файла'] = filename

            for i in range(len(crop_formats_list)):
                count = formats_list.count(crop_formats_list[i])
                new_dictionary[crop_formats_list[i]] = count

            dict_list.append(new_dictionary)

        crop_frame = pd.DataFrame(dict_list)
        crop_frame.reset_index(drop=True, inplace=True)
        crop_frame.index += 1
        crop_frame.insert(0, '№', crop_frame.index)

        col_list = list(crop_frame)
        col_list.remove('№')
        col_list.remove('Имя файла')
        crop_frame['Количество листов'] = crop_frame[col_list].sum(axis=1)

        col_list.append('Количество листов')
        crop_frame.loc['Total', :] = crop_frame[col_list].sum(axis=0)

        return crop_frame
