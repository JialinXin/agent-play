import json

class QueryBuilder:
    def __init__(self, knowledge_base_path="queries/knowledge_base.json"):
        # Load query templates knowledge base
        with open(knowledge_base_path, "r") as f:
            self.knowledge_base = json.load(f)

    def build_query(self, query_name, **kwargs):
        """
        根据查询名称和传入的字段动态构建查询语句
        query_name: 查询模板的名字（例如 'product_usage' 或 'user_retention'）
        kwargs: 传入的字段值（例如查询的字段，条件等）
        """
        if query_name not in self.knowledge_base:
            raise ValueError(f"Query template '{query_name}' does not exist!")

        # 获取查询模板和字段信息
        query_info = self.knowledge_base[query_name]
        template = query_info["template"]
        fields = kwargs.get("fields", query_info["fields"])
        table = kwargs.get("table", query_info["table"])
        condition = kwargs.get("condition", query_info["default_condition"])
        order_by = kwargs.get("order_by", query_info["default_order_by"])
        limit = kwargs.get("limit", query_info["default_limit"])

        # 动态替换占位符
        query = template.format(
            fields=", ".join(fields),
            table=table,
            condition=condition,
            order_by=order_by,
            limit=limit
        )
        return query
