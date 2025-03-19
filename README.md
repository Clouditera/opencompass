### 1. 工具安装
```bash
conda create --name opencompass python=3.10 -y
conda activate opencompass
pip install -U opencompass
```

### 3. 自定义数据集
```bash
选择题 (mcq)对于选择 (mcq) 类型的数据.jsonl 格式样例如下：
{"question": "165+833+650+615=", "A": "2258", "B": "2263", "C": "2281", "answer": "B"}
{"question": "368+959+918+653+978=", "A": "3876", "B": "3878", "C": "3880", "answer": "A"}
{"question": "776+208+589+882+571+996+515+726=", "A": "5213", "B": "5263", "C": "5383", "answer": "B"}
{"question": "803+862+815+100+409+758+262+169=", "A": "4098", "B": "4128", "C": "4178", "answer": "C"}
问答题 (qa)，对于问答 (qa) 类型的数据，默认的字段如下：
{"question": "752+361+181+933+235+986=", "answer": "3448"}
{"question": "712+165+223+711=", "answer": "1811"}
{"question": "921+975+888+539=", "answer": "3323"}
{"question": "752+321+388+643+568+982+468+397=", "answer": "4519"}
```
### 3. 运行脚本开始评测

```bash
python3 run.py examples/eval_api_secgpt.py --debug
```
