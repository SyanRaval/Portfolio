BOT_NAME = "nursing_jobs"
SPIDER_MODULES = ["nursing_jobs.spiders"]
NEWSPIDER_MODULE = "nursing_jobs.spiders"
ITEM_PIPELINES = {"nursing_jobs.pipelines.NursingJobsPipeline": 300}
