'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
 
Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3 

Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
'''

# Normal Iteration

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            new_email = []
            
            for char in email:
                if char == '+' or char == '@':
                    break
                if char != '.':
                    new_email.append(char)
                    
            domain_name = []
            
            for char in reversed(email):
                domain_name.append(char)
                if char == '@':
                    break
                    
            new_email = ''.join(new_email)
            domain_name = ''.join(domain_name[::-1])
            res.add(new_email+domain_name)
            
        return len(res)

# Using in-built Function

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            name, domain_name = email.split('@')
            new_email = name.split('+')
            new_email = new_email[0].replace('.', '')
            res.add(new_email+'@'+domain_name)
            
        return len(res)