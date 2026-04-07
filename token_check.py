import os
import tiktoken
import pandas as pd


def find_files(directory_path, extension='.md'):
    """get the paths of all txt files under the folder"""

    file_infos = []

    if not os.path.exists(directory_path):
        return file_infos

    for file_name in os.listdir(directory_path):

        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            if os.path.splitext(file_name)[1].lower() == extension:
                file_infos.append(file_path)

    return file_infos


def token_counter(text, model = "gpt-4"):
    """count the number of tokens in the txt file"""

    try:
        encoding = tiktoken.encoding_for_model(model)
    except:
        encoding = tiktoken.get_encoding("cl100k_base")
        
    tokens = encoding.encode(text)
    return len(tokens)


if __name__ == "__main__":
    
    md_fold = "your_md_folder_path"
    files = find_files(md_fold)
    token_checks = []

    for file in files:

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        tokens = token_counter(text)
        token_checks.append({
            'index': os.path.splitext(os.path.basename(file))[0],
            'tokens': tokens
        })

    doc_name = "your_result_name"
    df = pd.DataFrame(token_checks)
    df.to_excel(f'{doc_name}.xlsx', index=False, engine='openpyxl')
