import json

metadata_urls = [0] * 100
pdf_urls = [0] * 100

with open('urls.sh', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            filepath = parts[2]
            fileurl = parts[3]

            filename = filepath.split('/')[-1]
            fileurl = fileurl[1:-1]
            filetype = filename.split('_')[0]
            if filetype == 'metadata':
                fileshard = filename.split('_')[1].split('.')[0]
                metadata_urls[int(fileshard)] = fileurl
            else:
                fileshard = filename.split('_')[2].split('.')[0]
                pdf_urls[int(fileshard)] = fileurl

data_urls_list = []
for m_url, p_url in zip(metadata_urls, pdf_urls):
    data_urls_list.append({
        'metadata': m_url,
        'pdf_parses': p_url,
    })

with open('urls.json', 'w') as f:
    json.dump(data_urls_list, f)
