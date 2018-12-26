"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        eDict = {} # localname : set([domain])
        for email in emails:
            lname,domain = email.split('@')
            if "+" in lname:
                idx = lname.index("+")
                lname = lname[:idx]
            lname = lname.replace('.','')
            
            if lname in eDict.keys():
                eDict[lname].add(domain)
            else:
                eDict[lname] = set([domain])
        res = 0
        for e in eDict.keys():
            res += len(eDict[e])
        return res
"""
Fast
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmails=set([])
        
        for email in emails:
            local, domain=email.split('@');
            final_local=local.split('+')[0]
            final_local=final_local.replace('.',"");
            final_email=final_local+domain
            if final_email not in uniqueEmails:
                uniqueEmails.add(final_email)
        
        return len(uniqueEmails) 