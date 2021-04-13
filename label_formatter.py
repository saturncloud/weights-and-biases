
import re
import s3fs

##### Load label dataset
s3 = s3fs.S3FileSystem(anon=True)
with s3.open('s3://saturn-public-data/dogs/imagenet1000_clsidx_to_labels.txt') as f:
    imagenetclasses = [line.strip() for line in f.readlines()]
    
##### Format labels to match pretrained Resnet
def replace_label(dataset_label, model_labels):
    label_string = re.search('n[0-9]+-([^/]+)', dataset_label).group(1)
    
    for i in model_labels:
        i = str(i).replace('{', '').replace('}', '')
        model_label_str = re.search('''b["'][0-9]+: ["']([^\/]+)["'],["']''', str(i))
        model_label_idx = re.search('''b["']([0-9]+):''', str(i)).group(1)
        
        if re.search(str(label_string).replace('_', ' '), str(model_label_str).replace('_', ' ')):
            return i, model_label_idx
            break
