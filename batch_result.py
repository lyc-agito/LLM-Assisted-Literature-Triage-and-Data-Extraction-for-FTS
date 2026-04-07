import json
import pandas as pd


def batch_convert(batch_result_path):
    """export batch task results"""

    o_batch_results = []
    with open(batch_result_path, encoding='utf-8') as f:
        for line in f:
            if line.strip(): 
                o_batch_results.append(json.loads(line))
    batch_results = sorted(o_batch_results, key=lambda x: x["custom_id"])
        
    processed_results = []

    for batch_result in batch_results:
            
        index_id = batch_result["custom_id"]
        response = batch_result["response"]

        if response:
            reasoning_answer = response["body"]["choices"][0]["message"]["reasoning_content"]
            answer = response["body"]["choices"][0]["message"]["content"]
        else:
            reasoning_answer = "Error"
            answer = batch_result["error"]["message"]
            
        processed_results.append({"Index": index_id, "Reasoning Answer": reasoning_answer, "Answer": answer})
    
    return processed_results


if __name__ == "__main__":

    batch_result_path = "doubao.jsonl"
    batch_results = batch_convert(batch_result_path)

    doc_name = "your_result_name"
    df = pd.DataFrame(batch_results)
    df.to_excel(f'{doc_name}.xlsx', index=False, engine='openpyxl')
