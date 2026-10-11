import pandas as pd


def read_excel_columns_to_json(file_path, sheet_name, column_names):
    """读取 Excel 文件中指定 sheet 下某几列的数据并组成json格式的字典列表"""
    
    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)
    selected_df = df[column_names]
    dict_list = selected_df.to_dict('records')
    
    return dict_list


if __name__ == '__main__':

    file_name = "catalyst_sample.xlsx"
    sheet_name = "annotation"
    column_name = "Annotation"

    stds = read_excel_columns_to_json(file_name, sheet_name, ["Index", column_name])

    sorted_results = []
    for std in stds:
        results = sorted([cate.strip() for cate in std[column_name].split(",")])
        sorted_results.append(",".join(results))

    for sorted_result in sorted_results:
        print(sorted_result)
