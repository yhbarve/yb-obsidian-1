# A simple definition
- A backend is a computer connected to the Internet and which accepts and receives data.
- This computer is running somewhere in the world and can be reached by clients through the internet by making requests through HTTP, gRPC, or any other protocol.
- It is also called a server because it provides some service or some data in response to the request that it receives.
# A detailed look
- Let's assume that we have a backend server running on an AWS EC2 instance.
- Let's take a look at what happens when we make a request through the browser for data from the server:
	- Assume that the url for the server is `https://backend-demo.yb.com`.
	- When we make a request through the browser for the above URL, our request first goes to a DNS server that points the URL to AWS.
	- Inside AWS, our request first reaches a firewall, which forwards it to the appropriate EC2 instance.
	- An EC2 instance is basically a computer which runs the backend server. From the computer's perspective, it's running on its localhost. It's very similar to how we run our backend servers locally on a localhost port.
	- Once the reaches the EC2 instance, it is passed to Nginx.
	- Nginx essentially converts that request into a local host URL and runs the local host URL on the computer, which results in the actual data, which is then passed all the way back to the user.