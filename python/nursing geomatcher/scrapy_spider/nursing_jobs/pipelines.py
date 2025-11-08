class NursingJobsPipeline:
    def process_item(self, item, spider):
        # Basic cleaning
        for field in item.fields:
            if item.get(field):
                item[field] = item[field].strip()
        return item
