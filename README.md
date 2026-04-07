# LLM-Assisted Literature Triage and Data Extraction for FTS
提供“Unveiling a Century of Fischer-Tropsch Synthesis through Large-Language-Model-Assisted Literature Triaging and Data Extraction”一文中使用到的文献信息和代码（自2026年4月7日后不再更新）

Literature information and codes for "Unveiling a Century of Fischer-Tropsch Synthesis through Large-Language-Model-Assisted Literature Triaging and Data Extraction" (no more update after 7th, April, 2026)
***
## FTS litearture.xlsx
- 2025年9月23日从Web of Science导出的以“Fischer-Tropsch”为主题的12467篇“Article”类型文献。
- 12,467 publications with the topic of "Fischer-Tropsch" and the document type of "Article", exported from Web of Science on 23rd, September, 2025.
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
