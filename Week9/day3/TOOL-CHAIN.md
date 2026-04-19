# Tool-Calling Agent System (Day 3)

## Overview

This system allows agents to:
- Execute Python code
- Query databases
- Read files

## Architecture

User Query
   ↓
Tool Orchestrator
   ↓
Tool Selection (CODE / DB / FILE)
   ↓
Execution
   ↓
Output

## Tools

### Code Executor
- Executes Python dynamically

### DB Agent
- Runs SQL queries on SQLite

### File Agent
- Reads CSV and TXT files

## Example

User: Analyze sales.csv

Flow:
- Orchestrator → FILE
- File Agent → reads CSV
- Output returned

## Concepts

- Tool calling without APIs
- System-to-tool execution
- Function-based execution