import pandas as pd
import numpy as np


def read_excel_columns_to_json(file_path, sheet_name, column_names):
    """读取 Excel 文件中指定 sheet 下某几列的数据并组成json格式的字典列表"""
    
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    selected_df = df[column_names]
    dict_list = selected_df.to_dict('records')
    
    return dict_list


def update_cf(cf, answer, std):
    """更新混淆矩阵"""

    i = 0 if std == "YES" else 1
    j = 0 if answer == "YES" else 1
    
    cf[i][j] += 1

    return cf


def acc_cf(cf):
    """计算混淆矩阵的准确率"""

    return (cf[0][0] + cf[1][1]) / (cf[0][0] + cf[0][1] + cf[1][0] + cf[1][1])


def f1_cf(cf):
    """计算混淆矩阵的F1值"""

    precision = cf[0][0] / (cf[0][0] + cf[1][0])
    recall = cf[0][0] / (cf[0][0] + cf[0][1])

    return 2 * precision * recall / (precision + recall)


if __name__ == '__main__':
    
    stds = read_excel_columns_to_json("relevance_sample.xlsx", "held-out subset", ["Index", "Human"])
    results = read_excel_columns_to_json("relevance_sample.xlsx", "held-out subset", ["Index", "Doubao", "DeepSeek", "Kimi"])

    total = 0
    deepseek, doubao, kimi = np.zeros((2, 2)), np.zeros((2, 2)), np.zeros((2, 2))
    deepseek_errors, doubao_errors, kimi_errors = [], [], []

    for std in stds:
        for result in results:

            if std["Index"] == result["Index"]:

                total += 1

                doubao = update_cf(doubao, result["Doubao"], std["Human"])
                deepseek = update_cf(deepseek, result["DeepSeek"], std["Human"])           
                kimi = update_cf(kimi, result["Kimi"], std["Human"])

                if result["Doubao"] != std["Human"]:
                    doubao_errors.append(std["Index"])
                if result["DeepSeek"] != std["Human"]:
                    deepseek_errors.append(std["Index"])
                if result["Kimi"] != std["Human"]:
                    kimi_errors.append(std["Index"])
    
    print(f"# total: {total}")
    print(f"# doubao:\naccuracy: {acc_cf(doubao) * 100:.2f}%\nf1: {f1_cf(doubao) * 100:.2f}%")
    print(f"# deepseek:\naccuracy: {acc_cf(deepseek) * 100:.2f}%\nf1: {f1_cf(deepseek) * 100:.2f}%")
    print(f"# kimi:\naccuracy: {acc_cf(kimi) * 100:.2f}%\nf1: {f1_cf(kimi) * 100:.2f}%")
