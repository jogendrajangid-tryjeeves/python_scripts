import boto3
import pprint

region='us-east-1'

Check_tag1='Product'
Check_tag2='Name'
Check_tag3='Environment'

ec2=boto3.client('ec2', region_name=region)

#Check volume without proper tag
Volume_without_tags = { "data": []}
Volume_data = ec2.describe_volumes()
for vol_list in Volume_data['Volumes']:
	tag_keys = {'tags':[]}
	if 'Tags' in vol_list:
		for prams in vol_list['Tags']:
			tag_keys['tags'].append(prams['Key'])
	 	if ( Check_tag1 and Check_tag2 and Check_tag3 ) not in tag_keys['tags']:
	 			Volume_without_tags['data'].append(vol_list['VolumeId'])
	else:
	 	Volume_without_tags['data'].append(vol_list['VolumeId'])

print(len(Volume_without_tags['data']),"Volumes without Proper tags")
pprint.pprint(Volume_without_tags['data'])