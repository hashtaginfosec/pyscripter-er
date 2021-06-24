from pyscripter_utils import CustomIssue
import re
import sys

# Adds custom passive audit checks.
# Requires pyscripter_utils.py to be loaded with Burp.

if not messageIsRequest:

    if callbacks.isInScope(messageInfo.getUrl()):
        response = messageInfo.getResponse()    

        # Checks for verbose headers.
        bad_headers = ('WWW-Authenticate')
        headers = helpers.analyzeResponse(messageInfo.getResponse()).getHeaders()
        for header in headers:

            name = header.split(':')[0]
            if name.lower() in bad_headers.lower():
                
                if 'https://' in messageInfo.getUrl().lower():
                    httpbasic_severity = 'Medium'
                    httpbasic_detail = 'A severity of Medium was given since the application uses HTTPS. '
                elif 'http://' in messageInfo.getUrl().lower():
                    httpbasic_severity = 'High'
                    httpbasic_detail = 'A severity of High was given since the application uses cleartext HTTP. '

                issue = CustomIssue(
                    BasePair=messageInfo,
                    IssueName='HTTP Basic Auth',
                    IssueDetail='The following HTTP response header shows HTTP Basic Auth being used: \n' + header + '</li></ul>. \n' + httpbasic_detail,
                    Severity=httpbasic_severity
                )
                callbacks.addScanIssue(issue)