from mmengine.config import read_base
from opencompass.summarizers import MultiroundSummarizer

from opencompass.models import OpenAI
from opencompass.partitioners import NaivePartitioner
from opencompass.runners.local_api import LocalAPIRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from opencompass.configs.datasets.demo.demo_gsm8k_chat_gen import \
        gsm8k_datasets
    from opencompass.configs.datasets.ceval.ceval_gen import \
        ceval_datasets
    from opencompass.configs.datasets.demo.demo_math_chat_gen import \
        math_datasets
    from opencompass.configs.models.openai.gpt_4o_2024_05_13 import \
        models as gpt4

datasets = [

 # {"path": "data/clouditera/test/qa/filtered_eval_qa.jsonl", "data_type": "qa", "infer_method": "gen"},
  #    *gsm8k_datasets,
   *ceval_datasets,

]

models = [
    dict(
        # abbr='SecGPT',

        type=OpenAI,
        path='SecGPT',
        key='test',  # please give you key
        # generation_kwargs={
        #     'enable_search': False,
        # },
        query_per_second=1,
        max_out_len=2048,
        max_seq_len=2048,
        batch_size=16
    ),
]

infer = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(
        type=LocalAPIRunner,
        max_num_workers=1,
        concurrent_users=1,
        task=dict(type=OpenICLInferTask)),
)

work_dir = 'outputs/api_SecGPT/'
# summarizer = dict(
#     type=MultiroundSummarizer
# )
