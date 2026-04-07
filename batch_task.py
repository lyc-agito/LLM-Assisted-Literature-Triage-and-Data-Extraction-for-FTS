import os
import json


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


def batch_infos(id, prompt):
    """convert prompts to the batch task format of Volcengine"""

    jsonl_volc = {
        "custom_id": str(id),
        "body": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "thinking": {"type": "enabled"}
        }
    }

    return jsonl_volc


def prompt_from_json(json_file_path, attach_file_path=None):
    """integrate markdown texts into prompt"""

    prompt_full = ""

    with open(json_file_path, "r", encoding="utf-8") as f:
        prompt_json = json.load(f)
    
    tag_mapping = {
        "Task": "task",
        "Definition": "definition",
        "Instruction": "instruction",
        "Output Format": "output format"
    }
    
    for key, tag in tag_mapping.items():
        content = prompt_json.get(key)
        if content:
            prompt_full += f"<{tag}>\n{content}\n</{tag}>\n"
    
    if attach_file_path:
        with open(attach_file_path, 'r', encoding='utf-8') as f:
            attach_file = f.read()
        prompt_full += f"<attachment>\n{attach_file}\n</attachment>\n"
    
    return prompt_full


if __name__ == '__main__':

    prompt_path = "your_prompt_path"
    literature_folder_path = "your_literature_folder_path"
    batch_task_name = "your_batch_task_name"

    with open(f'{batch_task_name}.jsonl', 'w', encoding='utf-8') as f:

        for i, literature_path in enumerate(find_files(literature_folder_path)):
            batch_task = batch_infos(i + 1, prompt_from_json(prompt_path, literature_path))                        
            f.write(json.dumps(batch_task, ensure_ascii=False) + '\n')
