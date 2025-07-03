import xlrd;

from xlutils.copy import copy;

'''
方法: 实现通过用例文件的路径和sheet名称获取用例中的接口信息并返回
参数: file_url 文件的路径   file_sheet 用例文件的sheet名称
返回值: 接口列表
'''

def read_case_turn_interlist(file_url,file_sheet):

    inter_list = [];

    case_file = xlrd.open_workbook(file_url);

    sheet_file = case_file.sheet_by_name(file_sheet);

    for i in range(1,sheet_file.nrows):

        inter_info = {};

        inter_info["jk_name"] = sheet_file.row(i)[1].value;
        inter_info["jk_url"] = sheet_file.row(i)[3].value;
        inter_info["jk_method"] = sheet_file.row(i)[4].value;
        inter_info["jk_parm"] = sheet_file.row(i)[5].value;
        inter_info["jk_think"] = sheet_file.row(i)[6].value;

        inter_list.append(inter_info);

    return inter_list;

'''
方法: 该放啊是将传入的列表中的信息写入到指定文件中的指定行列中。
参数: 信息列表(两个)     文件路径   sheet名称
返回值: 无
'''

def write_case(text_list,result_list,case_url,sheet_name):

    case_file = xlrd.open_workbook(case_url);

    new_case_file = copy(case_file);

    sheet_file = new_case_file.get_sheet(sheet_name);

    for i in range(len(text_list)):

        sheet_file.write(i+1,7,text_list[i]);

        sheet_file.write(i + 1, 8, result_list[i]);

    new_case_file.save(case_url);