# Definitions
- **Steganography** is the art and science of communicating in a way that hides the existence of a message.
- Steganography takes one piece of information and hides it within another.
- **Cryptography** protects the contents of a message, whereas **steganography** conceals the existence of the message entirely.
- We are studying steganography to be able to transfer sensitive or unauthorized information through a channel that is not supposed to transmit that information.
	- Corporate espionage
	- Government or military activities
	- Criminal Activities
	- Censorship circumvention
- - -
# Covert Channels
- A **covert channel** is a path for the illegal flow of information between subjects within a system, utilizing system resources that were not designed to be used for inter-subject communication.
- Covered channels have various types across several dimensions.
	- Local vs Remote
		- Local covert channels leverage a machine's shared resources like CPU, RAM, and disk.
		- Remote covert channels leverage transmission mechanisms, typically the network.
	- Storage vs Timing
		- **Storage Channel:** The sending process alters a particular data item, and the receiving process detects and interprets the value of the altered data to receive information covertly.
			- **The Action:** The sender wants to transmit a binary "1," so they place a red folder on the top shelf. To transmit a "0," they leave the shelf empty.
			- **The Mechanism:** The sender alters a shared data item (the shelf state), and the receiver reads that exact item to decode the message without sending a single network packet.
			- To use a covert storage channel:
				- Both sender and receiver must have access to the same attribute of a shared object.
				- The sender must be able to modify the attribute. And the receiver must be able to view that attribute.
				- A mechanism must be in place for initiating the sender and receiver processes, and there must be a way to sequence their accesses to the shared resource.
		- **Timing Channel:** The sending process modulates the amount of time required for the receiving process to perform a task or detect a change in an attribute, and the receiving process interprets this delay or lack of delay as information.
			- **The Action:** Instead of sending data through a file or memory address, the sender controls response latency. If they want to send a "1," they make a server request take 500 milliseconds. If they want to send a "0," they respond instantly.
			- **The Mechanism:** The receiver doesn't look at _what_ data changed, but _how long_ it took to get the response, using a stopwatch to translate the delays into bits.
			- To use a covert timing channel:
				- Both sender and receiver must have access to some attribute of a shared object.
				- Both sender and receiver have access to a timer reference, like a real-time clock or a timer.
				- The sender must be able to control the timing of the detection of a change in the attribute of the receiver.
	- Noisy vs Noiseless
- Two important characteristics to note:
	1. Bandwidth: How many bits per second can be transmitted through the covert channel?
	2. Noise: Is the information transmitted through the cover channel distorted in any way?
- It is typically infeasible to eliminate every potential covert channel in a computer system. But we can:
	- Eliminate them by modifying the system implementation.
	- Reduce their bandwidth by introducing noise into the channel.
	- Monitor for usage patterns that indicate someone is trying to exploit a covert channel.
- - -
# Network Information Hiding
- A network covert channel can be created by using:
	- Storage: packet header manipulations
	- Timing: timing between packets
- Steganographic methods are also used to create a network covert channel.
- In a network covert channel, covert data is hidden in covert network transmissions. The cover medium is called a **carrier**.
## Covert Storage Channels on TCP/IP
- TCP/IP packets have headers that provide extra information.
- Headers have different fields that are optional or disregarded in usual transmissions.
- These fields can be used for hiding information.
	- IP Identification
	- Offset
	- Options
	- TCP checksum
	- TCP sequence numbers
- Common detection approaches include:
	- OpenBSD toggles the most significant bit of the IP ID every 3 minutes, so the most significant bit can be examined to check if it matches this pattern.
	- Within a rekey interval, the open BSD IP ID is non-repeating.
- Several constraints make steganography through TCP/IP packets easily detectable.
