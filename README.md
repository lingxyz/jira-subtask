# jira子任务导入

### 使用步骤
1. 按 `subtask.csv` 格式组织好 csv 文件
2. 在 `config.py` 中修改好配置
3. 确保在python3和pip3中，执行
```py
pip install jira
python jiraCreateSubtaskCSV.py
```

### 已知问题
- [x] csv 中字段不能为空，否则程序会 crash
- [ ] 重新执行脚本，已创建的子任务会重新创建
- [ ] 若bug和task类型的任务，只有一条子任务，仍旧会创建1条，并不会直接指派
