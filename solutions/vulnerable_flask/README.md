## Solution

#### Vulnerability

The website is vulnerable to commands injection, as no input checking has been implemented. It is possible to find the *flag.txt* file by injecting *ls* command and navigating over the directories, and later retrieve the contents of it with *cat* command.

#### Correct queries

Correct queries are present in the *Correct_queries* file.

## Conclusion

Remember to implement input checks in every type of application - always assume the user is malicious. If you are unsure how to do that, just use external tools to help you make safe and secure code. Or let others do it for you before you are experienced enough to do it yourself.
