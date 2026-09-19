# 鸿蒙知识 AI 对话助手

## 项目简介
基于 Python + Flask 搭建的 AI 对话应用，调用智谱大模型 API，实现鸿蒙技术知识的智能问答。支持多轮对话、快捷问题、对话清空等功能。

## 技术栈
- 后端：Python 3 + Flask
- AI 接口：智谱 AI 大模型 API（GLM-4-Flash）
- 前端：HTML + CSS + JavaScript
- 通信：RESTful API + JSON

## 功能
- 多轮对话：支持上下文记忆，连续问答
- 鸿蒙知识问答：预设系统提示词，专门回答 OpenHarmony / HarmonyOS 技术问题
- 快捷问题：页面内置 4 个鸿蒙相关高频问题，一键提问
- 对话清空：一键重置对话历史
- 响应式界面：美观的聊天气泡界面

## 运行方式
1. 安装依赖：`pip install flask requests`
2. 在 app.py 中填入智谱 AI API Key
3. 运行：`python app.py`
4. 浏览器访问：`http://127.0.0.1:5001`

## 项目结构
