from boto.mturk.connection import MTurkConnection


# AWSAccessKeyId='AKIAIIECFUFRBXEHXCOA'
# AWSSecretKey='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'
AWSAccessKeyId='AKIAJBT42GOBYK3Q3GLA'
AWSSecretKey='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'


ACCESS_ID = AWSAccessKeyId
SECRET_KEY = AWSSecretKey

# adjust host setting, depending on whether HIT is live (production) or in testing mode (sandbox)
# mode = "sandbox"
# # mode ="production"

# if mode=="production":
#     HOST='mechanicalturk.amazonaws.com'
# else:
#     HOST='mechanicalturk.sandbox.amazonaws.com'

HOST = 'mechanicalturk.sandbox.amazonaws.com'

mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

print mtc.get_account_balance()






