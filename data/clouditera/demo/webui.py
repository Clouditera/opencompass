from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('AI-ModelScope/synthetic_text_to_sql')
for sample in ds["test"]:
    print(sample)
#print(ds.data)