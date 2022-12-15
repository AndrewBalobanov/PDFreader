# -*- coding: utf-8 -*-
def main_prg(path):
    import aux_func as af
    import classes as cl
    outpath = path + '\\Project summary.xlsx'

    dir_list = af.dir_list(path)
    if len(dir_list) != 0:
        frame_list = af.create_frame_list(dir_list)

        #########################################################
        main_frame = cl.Prj_sum(frame_list)
        crop_frame = cl.Page_calc(frame_list)

        #########################################################
        list_to_write = []
        list_to_write.append(main_frame)
        list_to_write.append(crop_frame)

        dict_to_write = af.frame_list_to_sict(list_to_write)

        #########################################################
        af.write(outpath, dict_to_write)

        #########################################################
        doc_list = af.doc_list(main_frame.out['Имя файла'])
        af.merger(path=outpath, doclist=doc_list)
        return True
    else:
        return False