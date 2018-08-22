# SecurityPi

A security-learning platform designed for Rasppberry PI. Includes a server with challenges as well as instructions on modyfing standard Raspbian image to create the desired system. Created during the internship at Newcastle University, supervised by the security sector.

## Connecting to the server

The server is ran on PI's boot. Connecting to it requires ip address and port. The port is always **50000**, and the ip address is the PI's ip address. Example software that can be used to connect to it is *netcat* (command *nc ip port*) or *PuTTY*.

## Solving the challenges

Each challenge description can be found on the repo, within the corresponding folder. To learn more about available commands send *!help* command to the server. It will list all correctly loaded tasks that are available on the server. Each challenge should (but doesn't have to) provide additional description of the commands, that can be retrieved by sending *!command help* command to the server, where *!command* is the command you would like to learn more about.
