import pandas as pd


def read_excel_columns_to_json(file_path, sheet_name, column_names):
    """读取 Excel 文件中指定 sheet 下某几列的数据并组成json格式的字典列表"""
    
    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)
    selected_df = df[column_names]
    dict_list = selected_df.to_dict('records')
    
    return dict_list


def compare_answers(str1, str2):
    """计算两个答案的 Jaccard 相似度"""
    
    answer1 = [i.strip() for i in str1.split(",")]
    answer2 = [i.strip() for i in str2.split(",")]

    return len(set(answer1) & set(answer2)) / len(set(answer1) | set(answer2))


if __name__ == '__main__':

    file_name = "research focus_sample.xlsx"
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

                s1 = compare_answers(std["Human"], result["Doubao"])
                score_doubao += s1
                if s1 != 1:
                    doubao.append(std["Index"])

                s2 = compare_answers(std["Human"], result["DeepSeek"])
                score_deepseek += s2
                if s2 != 1:
                    deepseek.append(std["Index"])    
                
                s3 = compare_answers(std["Human"], result["Kimi"])
                score_kimi += s3
                if s3 != 1:
                    kimi.append(std["Index"])

    print(f"total: {total}")
    print(f"doubao: {score_doubao / total * 100:.2f} / {100 - len(doubao) / total * 100:.2f}")
    print(f"deepseek: {score_deepseek / total * 100:.2f} / {100 - len(deepseek) / total * 100:.2f}")
    print(f"kimi: {score_kimi / total * 100:.2f} / {100 - len(kimi) / total * 100:.2f}")
