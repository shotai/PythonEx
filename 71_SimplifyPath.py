class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        curr = '/'
        for p in paths:
            if p=='..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '':
                        curr = '/'
            elif p !='.' and p !='':
                curr += '/'+p if curr != '/' else p
        return curr
