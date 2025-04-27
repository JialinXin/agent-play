import argparse
from workflows.pm_workflow import create_pm_workflow

def main():
    manager = create_pm_workflow()

    parser = argparse.ArgumentParser(description="Input task")
    parser.add_argument('task', type=str, help="User task")
    args = parser.parse_args()

    manager.run_chat(args.task)

if __name__ == "__main__":
    # sample input: python main.py "分析产品最近的使用数据".
    main()