import pandas as pd
from decimal import Decimal, ROUND_HALF_UP


def read_excel_columns_to_json(file_path, sheet_name, column_names):
    """读取 Excel 文件中指定 sheet 下某几列的数据并组成json格式的字典列表"""
    
    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)
    selected_df = df[column_names]
    dict_list = selected_df.to_dict('records')
    
    return dict_list


def get_decimal_places(num):
    """获取小数位数"""

    s = str(num).lstrip('-')
    if '.' not in s:
        return 0
    return len(s.split('.')[1])


def compare_float_strings(i1, i2):
    """比较两个浮点数字符串是否相等"""

    str1, str2 = str(i1), str(i2)

    if str1 == str2:
        return True

    if str1 == "N/A" or str2 == "N/A":
        return str1 == str2
    
    num1, num2 = Decimal(str1), Decimal(str2)       
    decimal_places1, decimal_places2 = get_decimal_places(num1), get_decimal_places(num2)
 
    if decimal_places1 == decimal_places2:
        return num1 == num2

    if decimal_places1 > decimal_places2:
        # 构造合法的精度模板
        precision_template = Decimal('1') if decimal_places2 == 0 else Decimal('0.' + '0' * (decimal_places2 - 1) + '1')
        rounded_num1 = num1.quantize(precision_template, rounding=ROUND_HALF_UP)
        return rounded_num1 == num2
    else:
        # 构造合法的精度模板
        precision_template = Decimal('1') if decimal_places1 == 0 else Decimal('0.' + '0' * (decimal_places1 - 1) + '1')
        rounded_num2 = num2.quantize(precision_template, rounding=ROUND_HALF_UP)
        return num1 == rounded_num2


if __name__ == '__main__':

    file_name = "pressure_sample.xlsx"
    sheet_name = "held-out subset"
    
    stds = read_excel_columns_to_json(file_name, sheet_name, ["Index", "Human"])
    results = read_excel_columns_to_json(file_name, sheet_name, ["Index", "Doubao", "DeepSeek", "Kimi"])

    deepseek, doubao, kimi = [], [], []
    score_deepseek, score_doubao, score_kimi = 0, 0, 0
    total = 0

    for std in stds:
        for result in results:

            if std["Index"] == result["Index"]:

                total += 1

                s1 = compare_float_strings(std["Human"], result["Doubao"])
                score_doubao += s1
                if s1 != 1:
                    doubao.append(std["Index"])

                s2 = compare_float_strings(std["Human"], result["DeepSeek"])
                score_deepseek += s2
                if s2 != 1:
                    deepseek.append(std["Index"])    
                
                s3 = compare_float_strings(std["Human"], result["Kimi"])
                score_kimi += s3
                if s3 != 1:
                    kimi.append(std["Index"])
    
    print(f"Total: {total}")
    print(f"doubao: {score_doubao / total * 100:.2f}% / {100 - len(doubao) / total * 100:.2f}")
    print(f"deepseek: {score_deepseek / total * 100:.2f}% / {100 - len(deepseek) / total * 100:.2f}")
    print(f"kimi: {score_kimi / total * 100:.2f}% / {100 - len(kimi) / total * 100:.2f}\n")
