# LLM-Assisted Literature Triage and Data Extraction for FTS

提供“Unveiling a Century of Fischer-Tropsch Synthesis through Large-Language-Model-Assisted Literature Triaging and Data Extraction”一文中使用到的数据和代码（自2026年10月16日后不再更新）

Data and codes for "Unveiling a Century of Fischer-Tropsch Synthesis through Large-Language-Model-Assisted Literature Triaging and Data Extraction" (no more update after October 16, 2026)

***

## literature corpus/FTS literature.xlsx

该文件中包含了2025年9月23日从Web of Science导出的以“Fischer-Tropsch”为主题的12467篇“Article”类型文献的信息。其它文件中提及的文献序号均于该文件中的序号一致。

This file contains information on 12,467 "Article"-type publications on the topic of "Fischer-Tropsch," exported from Web of Science on September 23, 2025. The literature indexes mentioned in the other files are all consistent with those in this file.

## sample results

该文件夹中的xlsx文件包含了样本文献的文献编号、人工标注的结果和大语言模型的运行结果。该文件夹中的py文件包含了大语言模型性能评价的具体计算流程。

The XLSX file in this folder contains the indexes of the sample literature，human annotation，and LLM judgment. The PY file in this folder contains the detailed procedure for the evaluation of LLM performance.

## final results

## prompt_template.json
- JSON格式的提示词模板.
- Prompt template in JSON format.

## token_check.py
- 统计文献转化为markdown格式后的token数。
- Count the number of tokens after converting the literature to markdown format.

## batch_task.py
- 将提示词转化为火山引擎平台的批量任务格式。
- Convert prompts to the batch task format of Volcengine.

## batch_result.py
- 将火山引擎平台的批量任务结果转化为Excel格式。
- Convert the batch task results from Volcengine to Excel format..
