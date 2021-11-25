import urllib.request
import sys
#please pass one of the below key
#key = ['ami-id', 'ami-launch-index', 'ami-manifest-path', 'block-device-mapping/ami', 'events/maintenance/history', 'hibernation/configured', 'hostname', 'iam/info', 'identity-credentials/ec2/info', 'instance-action', 'instance-life-cycle', 'instance-type', 'local-hostname', 'local-ipv4', 'mac', 'metrics/vhostmd', 'network/interfaces/macs/', 'placement/availability-zone', 'placement/availability-zone-id', 'profile', 'public-hostname', 'public-ipv4', 'public-keys/', 'reservation-id', 'security-groups', 'instance-id']
input_key = sys.argv[1]
try:
  url = 'http://169.254.169.254/latest/meta-data/' + input_key
  print ("Queried URL is " + url)
  data = urllib.request.urlopen(url).read().decode()
  print ("Output is: " + data)
except Exception as e:
  if e.__class__.__name__ == 'HTTPError':
    print ("entered key is invalid, please pass valid key")
  else:
    raise e

