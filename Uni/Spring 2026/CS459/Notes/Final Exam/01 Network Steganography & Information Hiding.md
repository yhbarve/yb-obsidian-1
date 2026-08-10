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
- **Timing attack:** Propagating covert information by crafting delays between certain events. For example, modifying the usual inter-packet delay by introducing losses by skipping sequence numbers
- We may also have **hybrids of storage and timing**. For example, replace encrypted packet contents with covered data and use delays for signalling the receiver about specific packets.
## Covert Channels at the Application Level
- **DNS Tunneling**
	- DNS tunneling is based on encoding the data of other programs and protocols in DNS queries and responses.
- **Games:**
	- We can create covert channels by encoding information in games' virtual worlds, which are shared by multiple users.
## Detecting or Preventing Network Covert Channels
- A warden inspects or manipulates traffic to detect and break covert channels.
- Storage channels can be detected by **analyzing transmitted data for anomalies** and **normalizing data in header fields.**
- Timing channels can be detected or prevented by **analyzing packet timing for inconsistencies** and **shaping the traffic** (constant rate of transmission).
- - -
# File Formats
- A file format is a standard way that information is encoded for storage in a computer file.
- There are two broad file format families:
	- Text files: Essential to determine the text encoding scheme and structure
	- Binary files: Essential to determine the file format
## Text Files
- Text files can have some structure on their own.
- Examples: HTML, XML, JSON
- Some of the elements in text files may be used to store covert data as part of a covert storage channel.
## Binary Files
- In binary files, bytes represent custom data.
- Binary file formats may include multiple types of data in the same file, such as image, video, and audio data.
- This data can be interpreted by supporting programs but will show up as garbled text in a text editor.
- To inspect a file's raw bytes, we can use a hex editor to read file contents. We can also use the file utility to match a file's signature.
- When in doubt, look for **magic numbers**. These are numerical or text values used to identify a file or protocol.
- An adversary may be able to use magic numbers to make sense of what's being transmitted in a network channel.
- - -
# Traffic Obfuscation
- Timing and content anomalies may be an effective way to detect covert channels. But there are better ways to hide the existence of covert data transmissions.
- **Traffic obfuscation** hides the characteristics of a covert data transmission by shaping the look of data exchanges.
- Some techniques for traffic obfuscation include:
	- **Randomized Traffic**
		- The idea is to evade inspection by generating traffic that does not conform to any known protocol specification.
		- Randomize packet sizes, timings, and contents.
		- Examples: Shadowsocks, V2Ray, OutlineVPN
		- A potential issue is that it "looks-like-nothing" might be a signature in itself.
		- This may not work if wardens have protocol allow lists in place.
		- And it can still be detected via cryptographic flaws and entropy tests.
	- **Mimic Traffic**
		- The idea is to hide a protocol's execution by mimicking another innocuous protocol's characteristics.
		- Leverage steganography or encrypted carrier protocols
		- Mimic how an encrypted cover protocol sends its traffic.
		- Some issues include the difficulty to build a perfect imitation.
		- Now it is believed to be a fundamentally flawed approach.
	- **Tunnel Traffic**
		- The idea is to piggy back covert data on the execution of a protocol.
		- Send covert data as the protocol's application messages help avoid mimicking issues.
		- Still needs to ensure the cover protocol does not generate weird traffic patterns.
		- Eg: Meek & Decoy Routing (HTTPS), Dolphin (Cellphones), SWEET & Camoufler (Email)
		- Often times, there is a disconnect between the usage patterns of the cover protocol and the covert protocol. Covert data embedding mechanisms may slow down the cover activity, leading to noticeable changes in traffic patterns.
- Covered channels allow for the surreptitious transfer of information, both within processes of a given machine or across machines.
- Network covert channels are increasingly hard to detect but can also be used for commendable purposes.
- - -
