import boto3
import pprint

region='us-east-1'

Check_sqs_tag1='Product'
Check_sqs_tag2='Environment'

sqs=boto3.client('sqs', region_name=region)

#check sqs
sqs_without_tags ={'data':[]}
sqs_list = sqs.list_queues()
for sqs_url in sqs_list['QueueUrls']:
	queue_tag = {'tags':[]}
	responce = sqs.list_queue_tags(QueueUrl=sqs_url)
	if 'Tags' in responce:
		if (Check_sqs_tag1 and Check_sqs_tag2) not in responce['Tags']:
			sqs_without_tags['data'].append(sqs_url)
	else:
		sqs_without_tags['data'].append(sqs_url)

print(len(sqs_without_tags['data']),"SQS without Proper tags")
pprint.pprint(sqs_without_tags['data'])
