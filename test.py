#!/usr/bin/env python3
"""
GitHub 操作实验 - 完整功能版
演示 GitHub 仓库操作和 Python 编程
"""

import math
from datetime import datetime


class GitHubStudent:
    """GitHub 学习者类"""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.completed_tasks = []

    def complete_task(self, task_name):
        """完成任务"""
        self.completed_tasks.append({
            'task': task_name,
            'completed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"✅ 完成任务: {task_name}")

    def show_progress(self):
        """显示学习进度"""
        print(f"\n👨‍🎓 学生: {self.name}")
        print(f"🎯 学号: {self.student_id}")
        print(f"📊 完成任务数: {len(self.completed_tasks)}")

        for task in self.completed_tasks:
            print(f"   - {task['task']} (完成于 {task['completed_at']})")


class MathOperations:
    """数学运算工具类"""

    @staticmethod
    def basic_operations(a, b):
        """基础四则运算"""
        operations = {
            '加法': a + b,
            '减法': a - b,
            '乘法': a * b,
            '除法': f"{a / b:.2f}" if b != 0 else "无穷大"
        }
        return operations

    @staticmethod
    def advanced_operations(x):
        """高级数学运算"""
        return {
            '平方': x ** 2,
            '平方根': f"{math.sqrt(x):.2f}",
            '对数': f"{math.log(x):.2f}",
            '正弦': f"{math.sin(x):.4f}"
        }


def demonstrate_github_operations():
    """演示 GitHub 操作流程"""
    print("🚀 GitHub 代码云平台操作流程")
    steps = [
        "1. 创建 GitHub 账号",
        "2. 创建 Repository",
        "3. 编写 README.md",
        "4. 提交代码文件",
        "5. Fork 其他仓库",
        "6. Star 感兴趣的项目",
        "7. 修改和更新代码"
    ]

    for step in steps:
        print(f"   {step}")


def generate_project_stats():
    """生成项目统计信息"""
    current_time = datetime.now()
    project_start = datetime(2024, 1, 1)
    days_running = (current_time - project_start).days

    stats = {
        '项目运行天数': days_running,
        '创建日期': project_start.strftime("%Y-%m-%d"),
        '当前版本': 'v1.0.0',
        '文件数量': 2,
        '代码行数': '约 100 行'
    }

    return stats


def main():
    """主函数 - 演示所有功能"""
    print("=" * 60)
    print("🌟 GitHub 代码云平台实验 - 完整演示")
    print("=" * 60)

    # 1. 创建学生实例
    student = GitHubStudent("GitHub学习者", "2024001")

    # 2. 演示 GitHub 操作流程
    demonstrate_github_operations()

    # 3. 完成任务
    tasks = [
        "创建 GitHub 账号",
        "建立代码仓库",
        "编写 Markdown 文档",
        "提交 Python 代码",
        "Fork 其他项目",
        "Star 优质仓库"
    ]

    for task in tasks:
        student.complete_task(task)

    # 4. 显示学习进度
    student.show_progress()

    print("\n" + "=" * 40)
    print("🧮 数学运算演示")
    print("=" * 40)

    # 5. 数学运算演示
    math_ops = MathOperations()

    # 基础运算
    basic_results = math_ops.basic_operations(25, 4)
    print("基础运算 (25 和 4):")
    for op, result in basic_results.items():
        print(f"   {op}: {result}")

    # 高级运算
    advanced_results = math_ops.advanced_operations(16)
    print("\n高级运算 (16):")
    for op, result in advanced_results.items():
        print(f"   {op}: {result}")

    print("\n" + "=" * 40)
    print("📈 项目统计信息")
    print("=" * 40)

    # 6. 项目统计
    stats = generate_project_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")

    # 7. 斐波那契数列演示
    def fibonacci_demo(n=8):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    fib_sequence = fibonacci_demo()
    print(f"\n🔢 斐波那契数列 (前8个): {fib_sequence}")

    print("\n" + "=" * 60)
    print("🎉 实验完成！已掌握 GitHub 基础操作")
    print("📚 继续探索更多 GitHub 高级功能吧！")
    print("=" * 60)


if __name__ == "__main__":
    main()