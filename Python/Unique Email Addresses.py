class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        exist_dict = {}
        count = 0
        for email in emails:
            local, domain = email.split('@')
            
            # remove dots
            local = ''.join(local.split('.'))
            # remove plus
            if '+' in local:
                local = local[:local.find('+')]
            
            refined_email = local + '@' + domain
            if refined_email not in exist_dict:
                exist_dict[refined_email] = True
                count += 1
        return count