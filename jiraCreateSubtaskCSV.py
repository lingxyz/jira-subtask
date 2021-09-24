# !/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
from jira import JIRA

from config import nameTransferId
from config import CSV_FILE_PATH
from config import sFileName
from config import JIRA_SERVER
from config import JIRA_USER
from config import JIRA_PWD
from config import PROJECT

print(nameTransferId)

totalCardJSON = "["

#无视哪次迭代，只识别故事编号
# jira工具
class JiraTool:
  # 初始化方法
  def __init__(self):
    self.server = JIRA_SERVER
    self.basic_auth = (JIRA_USER, JIRA_PWD)
    self.jiraClinet = None

  # 读取CSV文件
  def read(self):
    with open(sFileName, newline='', encoding='UTF-8') as csvfile:
      rows = csv.reader(csvfile)
      next(rows)
      for row in rows:
        issue = row
        # 调用jira接口
        self.sendJiraCreateAPI(issue)

  # 登陆
  def login(self):
    self.jiraClinet = JIRA(server=self.server, basic_auth=self.basic_auth)
    if self.jiraClinet is not None:
      return True
    else:
      return False

  # 调用jira接口
  def sendJiraCreateAPI(self, issue):
    project = PROJECT
    #fixVersion = FIX_VERSION
    components = "开发"
    parentKey = issue[0]
    subTaskSummary = issue[1]
    userId = issue[2]
    storyPoint = issue[3]
    descriptioin = issue[1]
    label = issue[5]
    startDate = [6]
    endDate = [7]

    if len(issue) > 6:
      startDate = issue[6]
      endDate = issue[7]
      # 转化时间格式
      if "/" in startDate or "/" in endDate:
        startDate = startDate.replace("/", "-")
        endDate = endDate.replace("/", "-")
    # 姓名转工号
    userId = nameTransferId[userId]
    print(userId)

    # 入参字段
    fields = {
      "project": {"key": project},
      #"fixVersions": [{"name": fixVersion}],
      "parent": {"key": parentKey},
      "labels": [label],
      "assignee": {"name": userId},
      "summary": subTaskSummary,
      "description": descriptioin,
      "issuetype": {"id": "10302", "name": "子任务"},
      "customfield_10006": float(storyPoint),
      "customfield_10607": startDate,
      "customfield_10609": endDate
    }

    if self.jiraClinet is None:
      self.login
    print(issue)
    create_issue = self.jiraClinet.create_issue(fields)
    print(create_issue)


# 主方法启动
# if __name__ == '__main__':
#     jiraTool = JiraTool()
#     jiraTool.login()
#     jiraTool.read()

# 启动
jiraTool = JiraTool()
jiraTool.login()
jiraTool.read()
