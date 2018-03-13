import boto3
import pprint

tagkey='Product'
tagvalue='Test'

#Gloal variable
volumes_without_tags = { "data": []}
instance_without_tags = { "data": []}
volumes_not_atteched = { "data": []}

ec2 = boto3.client('ec2')
describe_volumes = ec2.describe_volumes()

#Get List of Instances by filter
Instances_data = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+tagkey,
                'Values': [tagvalue]
            }
        ]
    )

print("--------List of instance selected--------------")
for a in Instances_data['Reservations']:
		pprint.pprint(a['Instances'][0]['InstanceId'])
		pprint.pprint(a['Instances'][0]['Tags'])
print("---------------------------------")

ec3 = boto3.resource('ec2')
#List of Volume without tag
for value in Instances_data['Reservations']:
	instance_tags = value['Instances'][0]['Tags']
	if value['Instances'][0]['BlockDeviceMappings']:
		#List of volume atteched to instance
		for vol in value['Instances'][0]['BlockDeviceMappings']:
			volume_id = vol['Ebs']['VolumeId']
			for check_vol in ec2.describe_volumes(
				Filters=[
					{
						'Name': 'volume-id', 'Values': [volume_id]
				}])['Volumes']:
				if 'Tags' not in check_vol and check_vol['Attachments'][0]['State'] == 'attached':
					volumes_id = ec3.Volume(volume_id)
					print("Creating tag for", value['Instances'][0]['InstanceId'] ,"And volume ",volumes_id)
					for t in instance_tags:
						if 'aws' not in t['Key']:
							tag_created = volumes_id.create_tags(
								Tags=[{
									'Key':t['Key'],
									'Value': t['Value']
									},]
							)
							print("Created tag ",tag_created)
