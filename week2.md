# Week 2

## Denial of Service Attacks

An attack on availablitiy by hindering or blocking the provision of a service. Exhausts critical resource of a service, CPU, memory, bandwidth, disc space.

DDoS have increased in size (intensity) over the years. from a few hundred mbps in 2002 to 600 gbps in 2015 (BBC). Although the intensity and severity varies a lot, most attacks last for 30 minutes or less.  Sometimes DDoS can be used as a diversion while another more severe attack is going on somewhere else.

### Resources to attack

- Network bandwidth
  - Related to the capacity of the network links connectinga server to the wider internet
  - Usually, the connection to ones ISP. since this link usually has lower capacity than the links the ISPs links.
- System resources
  - Usually aims to overload or even crash the network handling software. Rather than simply consuming bandwidth.
  - Might aim any temporary buffers to hold arriving packets or tables of open connections, etc.
    - eks. SYN spoofing.
  - Might use packets whose structure trigger a bug in the system which causes a crash which will require a reboot to make the comm system work again.
    - poison packet: ex: ping of death, teardrop
- Application resources
  - such as a web server.
  - **Cyberslam**: using complex requests to a DB to consume significant resources and thereby limit nr of valid requests.
  - Else target the actual server. So it can't be used until reboot.

### Classic DoS attack

A flooding attack on an organisation. If the adversary has access to a higher capacity network connection they can easily overwhelm a lower-cap network. As simple as flooding w *pings*. Pings can have different sizes and different response rate: request max size 65507 byte and fast response:

    ping -f -s 65507

However, the source of the ping attack is clearly identified, as the source address in the ICMP echo request packets. This has another disadvantage (for the attacker): the victim can respond to the attacker and deflect the incoming messages. Therefore the attacker MUST use a falsified or spoofed!

### Source address spoofing

Just means a *forged* source address.

Often done by using the *raw socket interface* on many OS', who's purpose was originally for network protocol testing and whatnot.

Since TCP/IP where developed in a "generally cooperative environment" (and by people who had the priviledge of not needing privacy and protection) the protcols have no built in measure to safegaurd against false addresses.

#### egress filtering

It is possible to filter incoming packets to ensure that the source addresses are at least valid (doesn't check whether the packet actually originated from there). However, this happens at the point where a orginisations network connects to the wider network, at routers or gateways. However, usually boundary routers are located after the resouces being targeted.

Usually the ISP do this w outgoing traffic by ensuring that the source of all packets match their senders (the ISP knows this about it's customers). "Regrettably", not all ISPs follow these standards.

Backscatter traffic.

### SYN spoofing

Attacks the ability of a network server to respond to TCP connections by overflowing the tables used to manage such connections.

Done by sending loads of SYN connection requests w forges source adresses. The system sends an ACK as reply.
If a system receives an ACK that they did not expect (that is if they happen to be one of the spoofed addresses), they return a RST (reset). However if the target is too busy to do anthing about it.

## Flooding attacks

Common flooding attacks use ICMP, UDP or TPC SYN packet types, although it is also possible w other IP packet types.

### ICMP flood

Ping flood using ICMP echo requests. Often allowed through since network admins traditionally used the for diagnostic reasons. Recently many networks don't let them through firewalls. Attackers therefor use other types of ICMP packets since filtering them would be detrimental for correctly functioning TCP/IP.

### UDP flood

Directed at some port number and thereby a potential service on the target system.

### TCP SYN flood

Basically the SYN spoof mentioned above, however here the goal is the sheer volume of data/requests.

Defence: By selective drop or random drop, when the system would overflow. The dropped connection would most likely be an attacker.

#### RST spoofing

Sequence numbers are sent in cleartext which allows eavesdropping or tampering. by changing the RST bit to drop the connection to another system. This way the system will keep sending packets to the server or system wo knowing that the server is not receiving them.

## DDoS

The prev attacks are limited by the rate at which they generate data and requests, therefore..... use multiple systems.

### Zombie apocalypse

Zombies: PCS or workstation computer which have had attack malware installed and can be controlled by an attacker to generate DoS requests.

Botnet: the collective noun for zombies.

Ususally there is a control hierarchy st the attacker doesn't control each zombie individually. Instead some systems act as controllers or handlers for the other systems.

### Tribe Flood Network

TFN is an early and well known DDoS tool.
Did not spoof, simply relied on a large nr of compromised systems and a layered command structure to hide the path to the attacker.

### Newer tools

use Internet Relay Chat (IRC) or HTTP servers etc. Is used for Command-and-Control (C&C)

## Application based bandwidth attacks

A strategy to perform a DoS attack is to force the target to execute resource consuming operations that are disproportionate to the attack method.

### SIP flood

Voice over IP telephony is widely deployed all over the internet (is this what is used in skype and whatnot???) it uses a Session Initiation Protocol to establish the call setup. SIP uses syntax similar to HTTP. SIP INVITE is used to establish media session. Uses a proxy server to get the DNS of the recipient. A SIP flood floods the proxy server with INVITE requests from spoofed addresses. Making the system unusable for ligitimate calls.

### HTTP based attacks

#### HTTP flood

bombard web servers with HTTP requests. ex. a request to download large files which requires the server to read something from disk.

#### Slowloris

Attack a webserver by using up threads by posting incomplete requests.
Different than other HTTP attacks since it uses legitimate HTTP traffic rather than bug-inducing "bad" HTTP requests.

Counter measures:

- limiting the rate of incoming connections from a particular host
- varying the timeout on connections as a function of the number of connections
- delayed binding
  - Delayed binding is performed by load balancing software
  - ensures that your Web server or proxy will never see any of the incomplete requests.

### Reflector and amplifier attacks

Don't use compromised systems but systems that run normally. This is done by sending systems packets where the source address has been spoofed to be the address of the system which is the actual target. This way when the system(s) send a reply it is sent to the actual target.

#### Reflection

As described above. Ideally the attacker sends packets to an intermediary that responds with a greater volume of packet data.

Common UDP services are typically used sa. the echo service (which can't amplify data) or DNS, SNMP, ISAKMP (which all can).

##### DNS

Can be used by 1 attacker sending DNS queries (each w size 60 byte), each reply will be sent to the target and each response is bigger (maybe 512 byte) than the original request size.

##### TCP SYN

Can also be done w TCP SYN packets. Note: this differs from a SYN spoofing:

> The goal is to flood the network link to the target, not to exhaust its network handling resources. Indeed, the attacker would usually take care to limit the volume of traffic to any particular intermediary to ensure that it is not overwhelmed by, or even notices, this traffic.

#### Amplification attack

Same as reflection but uses intermediaries that respond w multiple packets for each original packets. ICMP echo attacks are a good example (see lecture note.)

### Defence against DoS attacks

- Attack prevention and preemption (before)
  - deny service to attackers wo. affecting ligit clients
- Attack detection and filtering (during)
  - Minimize impact
  - look for suspicious behaviour
- Attack source traceback and id (during & after)
  - to prevent future attacks pos. persue legal actions
  - doesn't help against the ongoing attack
- Attack reaction (after)

---

## Notes from the lecture

### Dolev-Yao

Owning the cable that the data is running through (basically)

### Security of the physical layer

**Confidentiality**: The data can be intercepted..
**Integrity**: The data can be intercepted and tampered with before sending it forward
**Availability**: You could simply cut the cable *snip snip*

### Security of the Data-link layer

Media Access Control (MAC) can be changed easily.
Checksums are also possible to avoid.. checksums are 32-bit
they are not cryptographic in design, they are build
switches.

**Confidentiality**: MAC flooding: by flooding the switch w fake MAC addresses you flood the port table and the switch is forced to send the conf message to all ports and thereby the attacker
**Integrity**: defeating the checksum is not too difficult.
**Availability**: change the checksum so everything is dropped on arrival,

### Security in the network layer

Hosts are identified by IP addresses. Unreliable delivery, may introduce packet dump and out for order msgs.

IP operations:

- next-hop routing
- BGP (connects autonomous systems)
- Address resolution protocol ARP
  - ARP cache poisoning aka. arp spoofing
    - redirecting packets to attacker by spoofing ip????
- DHCP (dynamic host configuration protocol)
  - router assigns IPs
  - DHCP starvation (using up all IP addresses)
    - this is a type of local DoS attack
- MTU (maximum transfer unit) fragmentation
  - IP fragmentation attacks
  - Teardrop attack: send the same fragments multiple times (or overlapping fragment) which will crash the memory buffer.
  - Rose attack: just sending the first and last fragments of a large amount of data
    - "Hello I would like to reserve a ton of data so i can send you something"
- IP spoofing
  - blind (the attacker can't see any responses)

### Security in the application layer

DNS, FTP etc.

## **In conclusion nothing is secure**

- slashdot effect: ligitimate flooding of a website. Example slashdot was a newssite that often linked to smaller sites (who couldn't take as much traffic)
  - also known as *slash crowd*, *flash event*
- Syn cookies
- CAPTCHA: to ensure there is a human behind the machine.

### Firewalls

Not useful but oh well...

Selectively block some connections or filter packets based on contents (src/trg IP, src/trg flags, interfaces etc). Default for a firewall should be to discard all connections and only white-list the things you actually want (Fail safe default principle).

#### Characteristics

- All traffic going in/out must pass through
  - by physically blocking access to local network except. via the firewall.
- Only authorised traffic may pass as defined by local policy
  - Based on:
    - IP address and protocol values
    - application protocol (application level gateway)
    - user identity
    - network activity
- firewall must be immune to penetration

limitation:

- protect against attacks that bypass the firewall.
  - Internal systems w wired or mobile broadband capability to connect to an ISP. An internal LAN may have direct connections to peer organizations that bypass the firewall.
- may not protect fully against internal threats
  - disgruntled employees
  - employee who unwittingly cooperates with an external attacker.
- improperly secured wireless LAN
  - may be accessed from outside the organization.
  - internal firewall that separates portions of an enterprise network cannot guard against wireless communications between local systems on different sides of the internal firewall.
- A laptop, PDA, or portable storage device may be used and infected outside the corporate network, then attached and used internally.

#### Types of firewalls

**Packet Filtering Firewall**: applies a set of rules to each in-/out-going packet. Based og src/dst IP, src/dst transport-level address, IP fields, Interface. Pros: simplicity, transparency to users, speediness.

**Stateful inspection firewall**: see 318

**Application-Level Gateway**: see 319

**Circuit-Level Gateway**: see 319

### Basing

Firewalls can be based on a stand alone maching running a common OS, or can be implemented as a softwrare module in a router or LAN switch or server.

#### Bastion host

A system identified as a critial stong point of the networks security. Platform for application level or circuit level gateways.

- Uses secure OS
- only has what services are deamed essential.
  - could by proxy applications for DNS, FTP, HTTP, SMTP
  - only the essential subset of the applications normal command set
- requires additional authentication to access these proxy services
- each proxy maintains detailed logs
  - traffic
  - each connecttion
    - duration of each connection
- stays within the economy of mechanisms
- each proxy is independant of the others, minimising system wide failure
- should perform no disk access other than the initial onfig.
  - makes installing trojan sniffers difficult

#### Host based firewalls

Software module used to secure a single host. FIltering rules can be tailored for user. Independant of topology (both internal and external attacks must pass through the firewall). Easier to add on new servers w their own firewall wo altering anything else in the network.

#### Network device firewall

In devices sa routers switches...

#### virtual firewall

Same as all above but virtual

#### personal firewall

Software module on personal computer. Less complex

### DMZ

Demilitarized zone is sandwiched between an external and internal firewall. The external provides a measure of access control and protection for the dmz and the rest of the enterprise network. The internal firewall adds more stingent protection, it provides two-way protection between the enterprise network and DMZ. The servers and workstations are protected from attacks launched via the DMZ systems (worms, and other nasties). It also protects the DMZ systems from internal attacks.

### Virtual Private Networks

Consists of a set of computers that interconnect by means of relatively unsecure network, but uses encryption and special protocols to provide security.

### Distributed firewalls

involves a stand alone firewall devices working together w host based firewalls under admin control. Security monitoring is important, i guess because a lot of things are going on simultainously.

### Other firewall stuff

Host-resident: includes personal firewall software and software on servers, both physical and virtual.

Screening router: single router between external and internal networks. typically for small buisness or personal use.

Single bastion inline: between and internal and external router. small/med organisation.

Single bastion T: same but w third network interface to dmz

double b inline: dmz is between to bastions.

double b T: a mix?
