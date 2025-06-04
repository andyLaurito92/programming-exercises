Notes:

1GB -> 1024 MB
1MB -> 1024 KB
1KB -> 1024 B

Remember that 1024 = 2^10
--------
How many bytes does a GB has? -> 2^30 B -> 2^33 bits

1 Gigabit -> 10^9 bits (1 billion bits)

How many bytes are transfered per second in a Gigabit?

2^34 bits / 10^9 bits/second = 17,179869184 seconds

17 * 5000 = 85000 seconds to transfer to all nodes, because each 
node has a link of 1 Gbit/s

85000 is the total amount of seconds

85000 / (60*24) = 59,02777777778 days is what it takes to do 
linearly in our current infraestructure the deployment of 
release from node 1 to all other nodes


How can we do this faster?

- Transfer from node1 file to node2. Now transfer from node1 to node3
and from node2 to node3, and so on. You are creating a tree.
With this, we downgrade the transfer time from:

W/the above algorithm, you downgrade from log_2(85000) to 16.4 seconds
in total!


But in the above scenario, you still need to work out how to handle
incoming traffics while deploying the release in the node. And the
above only takes into consideration how much time it takes to 
transfer the file. What about the deployment? Does it need some sort
of initial load?


