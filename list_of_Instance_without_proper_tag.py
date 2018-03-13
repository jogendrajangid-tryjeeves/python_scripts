import boto3
import pprint
Check_tag1='Product'
Check_tag2='Name'
Check_tag3='Environment'

ec2=boto3.client('ec2')

#Check instance without proper tag
Instance_without_tags = { "data": []}
Instances_data = ec2.describe_instances()
for inst_list in Instances_data['Reservations']:
	tag_keys = {'tags':[]}
	for value in inst_list['Instances']:
		for prams in value['Tags']:
			tag_keys['tags'].append(prams['Key'])
	 	if ( Check_tag1 and Check_tag2 and Check_tag3 ) not in tag_keys['tags']:
	 		Instance_without_tags['data'].append(value['InstanceId'])

print(len(Instance_without_tags['data']),"Instances without Proper tags")
pprint.pprint(Instance_without_tags['data'])