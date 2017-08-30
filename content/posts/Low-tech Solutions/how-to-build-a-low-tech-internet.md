Title: How to Build a Low-tech Internet
Date: 2015-10-26 00:26
Author: Kris De Decker
Category: Low-tech Solutions
Slug: how-to-build-a-low-tech-internet
Status: published


internet access is on the rise in both modern consumer societies and in
the developing world.

In rich countries, however, the focus is on always-on connectivity and
ever higher access speeds. In poor countries, on the other hand,
connectivity is achieved through much more low-tech, often asynchronous
networks.

While the high-tech approach pushes the costs and energy use of the
internet [higher and
higher]({filename}/posts/can-the-internet-run-on-renewable-energy.md),
the low-tech alternatives result in much cheaper and very energy
efficient networks that combine well with renewable power production and
are resistant to disruptions.

If we want the internet to keep working in circumstances where access to
energy is more limited, we can learn important lessons from alternative
network technologies. Best of all, there's no need to wait for
governments or companies to facilitate: we can build our own resilient
communication infrastructure if we cooperate with one another. This is
demonstrated by several community networks in Europe, of which the
largest has more than 35,000 users already.

Picture: A node in the [Scottish Tegola
Network](http://www.tegola.org.uk/hebnet/).

  

More than half of the global population does not have access to the
"worldwide" web. Up to now, the internet is mainly an urban phenomenon,
especially in "developing" countries. Telecommunication companies are
usually reluctant to extend their network outside cities due to a
combination of high infrastructure costs, low population density,
limited ability to pay for services, and an unreliable or non-existent
electricity infrastructure. Even in remote regions of "developed"
countries, internet connectivity isn't always available.

Internet companies such as Facebook and Google regularly make headlines
with plans for connecting these remote regions to the internet. Facebook
tries to achieve this with drones, while Google counts on high-altitude
balloons. There are major technological challenges, but the main
objection to these plans is their commercial character. Obviously,
Google and Facebook want to connect more people to the internet because
that would increase their revenues. Facebook especially receives lots of
criticism because their network promotes their own site in particular,
and blocks most other internet applications. \[1\]

Meanwhile, several research groups and network enthusiasts have
developed and implemented much cheaper alternative network technologies
to solve these issues. Although these low-tech networks have proven
their worth, they have received much less attention. Contrary to the
projects of internet companies, they are set up by small organisations
or by the users themselves. This guarantees an open network that
benefits the users instead of a handful of corporations. At the same
time, these low-tech networks are very energy efficient.

WiFi-based Long Distance Networks

Most low-tech networks are based on WiFi, the same technology that
allows mobile access to the internet in most western households. As we
have seen in the previous article, [sharing these devices could provide
free mobile access across densely populated
cities]({filename}/posts/the-4g-network-thats-already-there.md).
But the technology can be equally useful in sparsely populated areas.
Although the WiFi-standard was developed for short-distance data
communication (with a typical range of about 30 metres), its reach can
be extended through modifications of the Media Access Control (MAC)
layer in the networking protocol, and through the use of range extender
amplifiers and directional antennas. \[2\]

> Although the WiFi-standard was developed for short-distance data
> communication, its reach can be extended to cover distances of more
> than 100 kilometres.

The longest unamplified WiFi link is a 384 km wireless point-to-point
connection between Pico El Águila and Platillón in Venezuela,
established a few years ago. \[3,4\] However, WiFi-based long distance
networks usually consist of a combination of shorter point-to-point
links, each between a few kilometres and one hundred kilometers long at
most. These are combined to create larger, multihop networks.
Point-to-points links, which form the backbone of a long range WiFi
network, are combined with omnidirectional antennas that distribute the
signal to individual households (or public institutions) of a community.


A relay with three point-to-point links and three sectoral antennae.
[Tegola](http://www.tegola.org.uk/howto/network-planning.html).

Long-distance WiFi links require line of sight to make a connection --
in this sense, the technology resembles the [18th century optical
telegraph]({filename}/posts/email-in-the-18.md).
\[5\] If there's no line of sight between two points, a third relay is
required that can see both points, and the signal is sent to the
intermediate relay first. Depending on the terrain and particular
obstacles, more hubs may be necessary. \[6\]

Point-to-point links typically consist of two directional antennas, one
focused on the next node and the other on the previous node in the
network. Nodes can have multiple antennas with one antenna per fixed
point-to-point link to each neighbour. \[7\] This allows mesh routing
protocols that can dynamically select which links to choose for routing
among the available ones. \[8\]

> Long-distance WiFi links require line of sight to make a connection --
> in this sense, the technology resembles the 18th century optical
> telegraph.

Distribution nodes usually consist of a sectoral antenna (a small
version of the things you see on mobile phone masts) or a conventional
WiFi-router, together with a number of receivers in the community. \[6\]
For short distance WiFi-communication, there is no requirement for line
of sight between the transmitter and the receiver. \[9\]

To provide users with access to the worldwide internet, a long range
WiFi network should be connected to the main backbone of the internet
using at least one "backhaul" or "gateway node". This can be a dial-up
or broadband connection (DSL, fibre or satellite). If such a link is not
established, users would still be able to communicate with each other
and view websites set up on local servers, but they would not be able to
access the internet. \[10\]

Advantages of Long Range WiFi


range WiFi offers high bandwidth (up to 54 Mbps) combined with very low
capital costs. Because the WiFi standard enjoys widespread acceptance
and has huge production volumes, off-the-shelf antennas and wireless
cards can be bought for very little money. \[11\] Alternatively,
components can be put together [from discarded
materials](http://roelof.info/projects/%282014%29Pretty_Fly_For_A_Wifi/)
such as old routers, satellite dish antennas and laptops. Protocols like
WiLDNet run on a 266 Mhz processor with only 128 MB memory, so an old
computer will do the trick. \[7\]

The WiFi-nodes are lightweight and don't need expensive towers --
further decreasing capital costs, and minimizing the impact of the
structures to be built. \[7\] More recently, single units that combine
antenna, wireless card and processor have become available. These are
very convenient for installation. To build a relay, one simply connects
such units together with ethernet cables that carry both signal and
power. \[6\] The units can be mounted in towers or slim masts, given
that they offer little windload. \[3\] Examples of suppliers of long
range WiFi components are [Ubiquity](https://www.ubnt.com/),
[Alvarion](http://www.alvarion.com/) and
[MikroTik](http://www.mikrotik.com/), and
[simpleWiFi](https://www.simplewifi.com/).

> Long Range WiFi makes use of unlicensed spectrum and offers high
> bandwidth, low capital costs, easy installation, and low power
> requirements.

Long range WiFi also has low operational costs due to low power
requirements. A typical mast installation consisting of two long
distance links and one or two wireless cards for local distribution
consumes around 30 watts. \[6,12\] In several low-tech networks, nodes
are entirely powered by solar panels and batteries. Another important
advantage of long range WiFi is that it makes use of unlicensed spectrum
(2.4 and 5 GHz), and thus avoids negotiations with telecom operators and
government. This adds to the cost advantage and allows basically anyone
to start a WiFi-based long distance network. \[9\]

Long Range WiFi Networks in Poor Countries

The first long range WiFi networks were set up ten to fifteen years ago.
In poor countries, two main types have been built. The first is aimed at
providing internet access to people in remote villages. An example is
the Akshaya network in India, which covers the entire Kerala State and
is one of the largest wireless networks in the world. The infrastructure
is built around approximately 2,500 "computer access centers", which are
open to the local population&mdash;direct ownership of computers is minimal
in the region. \[13\]

Another example, also in India, are the AirJaldi networks which provide
internet access to approximately 20,000 users in six states, all in
remote regions and on difficult terrain. Most nodes in this network are
solar-powered and the distance between them can range up to 50 km or
more. \[14\] In some African countries, local WiFi-networks distribute
internet access from a satellite gateway. \[15,16\]



A node in the AirJaldi network. Picture: AirJaldi.

A second type of long distance WiFi network in poor countries is aimed
at providing telemedicine to remote communities. In remote regions,
health care is often provided through health posts scarcely equipped and
attended by health technicians who are barely trained. \[17\] Long-range
WiFi networks can connect urban hospitals with these outlying health
posts, allowing doctors to remotely support health technicians using
high-resolution file transfers and real-time communication tools based
on voice and video.

An example is the link between Cabo Pantoja and Iquitos in the Loreto
province in Peru, which was established in 2007. The 450 km network
consists of 17 towers which are 16 to 50 km apart. The line connects 15
medical outposts in remote villages with the main hospital in Iquitos
and is aimed at remote diagnosis of patients. \[17,18\] All equipment is
powered by solar panels. \[18,19\] Other succesful examples of long
range WiFi telemedicine networks have been built in India, Malawi and
Ghana. \[20,21\]

WiFi-Based Community Networks in Europe

The low-tech networks in poor countries are set up by NGO's,
governments, universities or businesses. In contrast, most of the
WiFi-based long distance networks in remote regions of rich countries
are so-called "community networks": the users themselves build, own,
power and maintain the infrastructure. Similar to the shared wireless
approach in cities, reciprocal resource sharing forms the basis of these
networks: participants can set up their own node and connect to the
network (for free), as long as their node also allows traffic of other
members. Each node acts as a WiFi routing device that provides IP
forwarding services and a data link to all users and nodes connected to
it. \[8,22\]

> In a community network, the users themselves build, own, power and
> maintain the infrastructure.

Consequently, with each new user, the network becomes larger. There is
no a-priori overall planning. A community network grows bottom-up,
driven by the needs of its users, as nodes and links are added or
upgraded following demand patterns. The only consideration is to connect
a node from a new participant to an existing one. As a node is powered
on, it discovers it neighbours, attributes itself a unique IP adress,
and then establishes the most appropriate routes to the rest of the
network, taking into account the quality of the links. Community
networks are open to participation to everyone, sometimes according to
an open peering agreement. \[8,9,19,22\]



Wireless links in the Spanish Guifi network.
[Credit](http://iuliinet.github.io/presentazione_ottobre_2014/img/barcellona.jpg).

Despite the lack of reliable statistics, community networks seem to be
rather succesful, and there are several large ones in Europe, such as
[Guifi.net](https://guifi.net/) (Spain), [Athens Wireless Metropolitan
Network](http://www.awmn.gr/content.php?s=ce506a41ab245641d6934638c6f6f107)
(Greece), [FunkFeuer](http://www.funkfeuer.at/) (Austria), and
[Freifunk](http://freifunk.net/en/) (Germany). \[8,22,23,24\] The
Spanish network is the largest WiFi-based long distance network in the
world with more than 50,000 kilometres of links, although a small part
is based on optic fibre links. Most of it is located in the Catalan
Pyrenees, one of the least populated areas in Spain. The network was
initiated in 2004 and now has close to 30,000 nodes, up from 17,000 in
2012. \[8,22\]

Guifi.net provides internet access to individuals, companies,
administrations and universities. In principle, the network is
installed, powered and maintained by its users, although volunteer teams
and even commercial installers are present to help. Some nodes and
backbone upgrades have been succesfully crowdfunded by indirect
beneficiaries of the network. \[8,22\]

Performance of Low-tech Networks

So how about the performance of low-tech networks? What can you do with
them? The available bandwidth per user can vary enormously, depending on
the bandwidth of the gateway node(s) and the number of users, among
other factors. The long-distance WiFi networks aimed at telemedicine in
poor countries have few users and a good backhaul, resulting in high
bandwidth (+ 40 Mbps). This gives them a similar performance to fibre
connections in the developed world. A study of (a small part of) the
Guifi.net community network, which has dozens of gateway nodes and
thousands of users, showed an average throughput of 2 Mbps, which is
comparable to a relatively slow DSL connection. Actual throughput per
user varies from 700 kbps to 8 Mbps. \[25\]

> The available bandwidth per user can vary enormously, depending on the
> bandwidth of the gateway node(s) and the number of users, among other
> factors

However, the low-tech networks that distribute internet access to a
large user base in developing countries can have much more limited
bandwidth per user. For example, a university campus in Kerala (India)
uses a 750 kbps internet connection that is shared across 3,000 faculty
members and students operating from 400 machines, where during peak
hours nearly every machine is being used.

Therefore, the worst-case average bandwidth available per machine is
approximately 1.9 kbps, which is slow even in comparison to a dial-up
connection (56 kbps). And this can be considered a really good
connectivity compared to typical rural settings in poor countries.
\[26\] To make matters worse, such networks often have to deal with an
intermittent power supply.

<div id="photo-xid-6a00e0099229e8883301b8d16a5899970c"
class="photo-wrap photo-xid-6a00e0099229e8883301b8d16a5899970c photo-full">


<div id="caption-xid-6a00e0099229e8883301b8d16a5899970c"
class="photo-caption caption-xid-6a00e0099229e8883301b8d16a5899970c">

A node in the Spanish Guifi community network.

</div>

</div>

Under these circumstances, even the most common internet applications
have poor performance, or don't work at all. The communication model of
the internet is based on a set of network assumptions, called the TCP/IP
protocol suite. These include the existence of a bi-directional
end-to-end path between the source (for example a website's server) and
the destination (the user's computer), short round-trip delays, and low
error rates.

Many low-tech networks in poor countries do not comform to these
assumptions. They are characterized by intermittent connectivity or
"network partitioning"&mdash;the absence of an end-to-end path between
source and destination&mdash;long and variable delays, and high error
rates. \[21,27,28\]

Delay-Tolerant Networks

Nevertheless, even in such conditions, the internet could work perfectly
fine. The technical issues can be solved by moving away from the
always-on model of traditional networks, and instead design networks
based upon asynchronous communication and intermittent connectivity.
These so-called "delay-tolerant networks" (DTNs) have their own
specialized protocols overlayed on top of the lower protocols and do not
utilize TCP. They overcome the problems of intermittent connectivity and
long delays by using store-and-forward message switching.

Information is forwarded from a storage place on one node to a storage
place on another node, along a path that *eventually* reaches its
destination. In contrast to traditional internet routers, which only
store incoming packets for a few milliseconds on memory chips, the nodes
of a delay-tolerant network have persistent storage (such as hard disks)
that can hold information indefinitely. \[27,28\]

> Delay-tolerant networks combine well with renewable energy: solar
> panels or wind turbines could power network nodes only when the sun
> shines or the wind blows, eliminating the need for energy storage.

Delay-tolerant networks don't require an end-to-end path between source
and destination. Data is simply transferred from node to node. If the
next node is unavailable because of long delays or a power outage, the
data is stored on the hard disk until the node becomes available again.
While it might take a long time for data to travel from source to
destination, a delay-tolerant network ensures that it will eventually
arrive.

Delay-tolerant networks further decrease capital costs and energy use,
leading to the most efficient use of scarce resources. They keep working
with an intermittent energy supply and they combine well with renewable
energy sources: solar panels or wind turbines could power network nodes
only when the sun shines or the wind blows, eliminating the need for
energy storage.

Data Mules

Delay-tolerant networking can take surprising forms, especially when
they take advantage of some non-traditional means of communication, such
as "data mules". \[11,29\] In such networks, conventional transportation
technologies&mdash;buses, cars, motorcycles, trains, boats, airplanes --
are used to ferry messages from one location to another in a
store-and-forward manner.

Examples are DakNet and KioskNet, which use buses as data mules.
\[30-34\] In many developing regions, rural bus routes regularly visit
villages and towns that have no network connectivity. By equipping each
vehicle with a computer, a storage device and a mobile WiFi-node on the
one hand, and by installing a stationary WiFi-node in each village on
the other hand, the local transport infrastructure can substitute for a
wireless internet link. \[11\]


AirJaldi.

Outgoing data (such as sent emails or requests for webpages) is stored
on local computers in the village until the bus comes withing range. At
this point, the fixed WiFi-node of the local computer automatically
transmits the data to the mobile WiFi-node of the bus. Later, when the
bus arrives at a hub that is connected to the internet, the outgoing
data is transmitted from the mobile WiFi-node to the gateway node, and
then to the internet. Data sent to the village takes the opposite route.
The bus&mdash;or data&mdash;driver doesn't require any special skills and is
completely oblivious to the data transfers taking place. He or she does
not need to do anything other than come in range of the nodes. \[30,31\]

> In a data mules network, the local transport infrastructure
> substitutes for a wireless internet link.

The use of data mules offers some extra advantages over more
"sophisticated" delay-tolerant networks. A "drive-by" WiFi network
allows for small, low-cost and low-power radio devices to be used, which
don't require line of sight and consequently no towers&mdash;further
lowering capital costs and energy use compared to other low-tech
networks. \[30,31,32\]

The use of short-distance WiFi-links also results in a higher bandwidth
compared to long-distance WiFi-links, which makes data mules better
suited to transfer larger files. On average, 20 MB of data can be moved
in each direction when a bus passes a fixed WiFi-node. \[30,32\] On the
other hand, latency (the time interval between sending and receiving
data) is usually higher than on long-range WiFi-links. A single bus
passing by a village once a day gives a latency of 24 hours.

Delay-Tolerant Software

Obviously, a delay-tolerant network (DTN)&mdash;whatever its form&mdash;also
requires new software: applications that function without a connected
end-to-end networking path. \[11\] Such custom applications are also
useful for synchronous, low bandwidth networks. Email is relatively easy
to adapt to intermittent connectivity, because it's an asynchronous
communication method by itself. A DTN-enabled email client stores
outgoing messages until a connection is available. Although emails may
take longer to reach their destination, the user experience doesn't
really change.



A Freifunk WiFi-node is installed in Berlin, Germany. Picture:[Wikipedia
Commons](https://upload.wikimedia.org/wikipedia/commons/5/51/Freifunk-Initiative_in_Berlin-Kreuzberg.jpg).

Browsing and searching the web requires more adaptations. For example,
most search engines optimize for speed, assuming that a user can quickly
look through the returned links and immediately run a second modified
search if the first result is inadequate. However, in intermittent
networks, multiple rounds of interactive search would be impractical.
\[26,35\] Asynchronous search engines optimize for bandwith rather than
response time. \[26,30,31,35,36\] For example, RuralCafe desynchronizes
the search process by performing many search tasks in an offline manner,
refining the search request based on a database of similar searches. The
actual retrieval of information using the network is only done when
absolutely necessary.

> Many internet applications could be adapted to intermittent networks,
> such as webbrowsing, email, electronic form filling, interaction with
> e-commerce sites, blogsoftware, large file downloads, or social media.

Some DTN-enabled browsers download not only the explicitly requested
webpages but also the pages that are linked to by the requested pages.
\[30\] Others are optimized to return low-bandwidth results, which are
achieved by filtering, analysis, and compression on the server site. A
similar effect can be achieved through the use of a service like
[Loband](http://www.loband.org/loband/), which strips webpages of
images, video, advertisements, social media buttons, and so on, merely
presenting the textual content. \[26\]

Browsing and searching on intermittent networks can also be improved by
local caching (storing already downloaded pages) and prefetching
(downloading pages that might be retrieved in the future). \[206\] Many
other internet applications could also be adapted to intermittent
networks, such as electronic form filling, interaction with e-commerce
sites, blogsoftware, large file downloads, social media, and so on.
\[11,30\] All these applications would remain possible, though at lower
speeds.

Sneakernets

Obviously, real-time applications such as internet telephony, media
streaming, chatting or videoconferencing are impossible to adapt to
intermittent networks, which provide only asynchronous communication.
These applications are also difficult to run on synchronous networks
that have limited bandwidth. Because these are the applications that are
in large part responsible for the growing energy use of the internet,
one could argue that their incompatibility with low-tech networks is
actually a good thing (see the [previous
article]({filename}/posts/can-the-internet-run-on-renewable-energy.md)).

Furthermore, many of these applications could be organized in different
ways. While real-time voice or video conversations won't work, it's
perfectly possible to send and receive voice or video messages. And
while streaming media can't happen, downloading music albums and video
remains possible. Moreover, these files could be "transmitted" by the
most low-tech internet technology available: a sneakernet. In a
sneakernet, digital data is "wirelessly" transmitted using a storage
medium such as a hard disk, a USB-key, a flash card, or a CD or DVD.
Before the arrival of the internet, all computer files were exchanged
via a sneakernet, using tape or floppy disks as a storage medium.



Stuffing a cargo train full of digital storage media would beat any
digital network in terms of speed, cost and energy efficiency. Picture:
Wikipedia Commons.

Just like a data mules network, a sneakernet involves a vehicle, a
messenger on foot, or an animal (such as a [carrier
pigeon]({filename}/posts/sneakernet-beats-internet.md)).
However, in a sneakernet there is no automatic data transfer between the
mobile node (for instance, a vehicle) and the stationary nodes (sender
and recipient). Instead, the data first have to be transferred from the
sender's computer to a portable storage medium. Then, upon arrival, the
data have to be transferred from the portable storage medium to the
receiver's computer. \[30\] A sneakernet thus requires manual
intervention and this makes it less convenient for many internet
applications.

There are exceptions, though. For example, a movie doesn't have to be
transferred to the hard disk of your computer in order to watch it. You
play it straight from a portable hard disk or slide a disc into the
DVD-player. Moreover, a sneakernet also offers an important advantage:
of all low-tech networks, it has the most bandwidth available. This
makes it perfectly suited for the distribution of large files such as
movies or computer games. In fact, when very large files are involved, a
sneakernet even beats the fastest fibre internet connection. At lower
internet speeds, sneakernets can be advantageous for much smaller files.

Technological progress will not lower the advantage of a sneakernet.
Digital storage media evolve at least as fast as internet connections
and they both improve communication in an equal way.

Resilient Networks

While most low-tech networks are aimed at regions where the alternative
is often no internet connection at all, their usefulness for
well-connected areas cannot be overlooked. The internet as we know it in
the industrialized world is a product of an abundant energy supply, a
robust electricity infrastructure, and sustained economic growth. This
"high-tech" internet might offer some fancy advantages over the low-tech
networks, but it cannot survive if these conditions change. This makes
it extremely vulnerable.

> The internet as we know it in the industrialized world is a product of
> an abundant energy supply, a robust electricity infrastructure, and
> sustained economic growth. It cannot survive if these conditions
> change.

Depending on their level of resilience, low-tech networks can remain in
operation when the supply of fossil fuels is interrupted, when the
electricity infrastructure deteriorates, when the economy grinds to a
halt, or if other calamities should hit. Such a low-tech internet would
allow us to surf the web, send and receive e-mails, shop online, share
content, and so on. Meanwhile, data mules and sneakernets could serve to
handle the distribution of large files such as videos. Stuffing a cargo
vessel or a train full of digital storage media would beat any digital
network in terms of speed, cost and energy efficiency. And if such a
transport infrastructure would no longer be available, we could still
rely on messengers on foot, [cargo
bikes]({filename}/posts/modular-cargo-cycles.md)
and [sailing vessels](http://www.lowtechmagazine.com/sailing-ships/).

Such a hybrid system of online and offline applications would remain a
very powerful communication network&mdash;unlike anything we had even in
the late twentieth century. Even if we envision a doom scenario in which
the wider internet infrastructure would disintegrate, isolated low-tech
networks would still be very useful local and regional communication
technologies. Furthermore, they could obtain content from other remote
networks through the exchange of portable storage media. The internet,
it appears, can be as low-tech or high-tech as we can afford it to be.

Kris De Decker (edited by [Jenna
Collett](https://www.linkedin.com/pub/jenna-collett/1a/925/b3))

![](https://www.paypalobjects.com/en_US/i/scr/pixel.gif){width="1"
height="1"}

Sources & Notes:

DIY: [Wireless networking in the developing
world](http://wndw.net/book.html#readBook) (Third Edition) is a free
book about designing, implementing and maintaining low-cost wireless
networks. Available in English, French, and Spanish.

\[1\] [Connecting the unwired world with balloons, satellites, lasers &
drones](http://tech.slashdot.org/story/15/09/03/214256/connecting-the-unwired-world-with-balloons-satellites-lasers-drones),
Slashdot, 2015

\[2\] [A QoS-aware dynamic bandwidth allocation scheme for multi-hop
WiFi-based long distance
networks](http://link.springer.com/article/10.1186%2Fs13638-015-0352-z#/page-1),
Iftekhar Hussain et al., 2015

\[3\] [Long-distance, Low-Cost Wireless Data
Transmission](http://www.ursi.org/files/RSBissues/RSB_339_2011_12.pdf)
(PDF), Ermanno Pietrosemoli, 2011

\[4\] This link could only be established thanks to the height of the
endpoints (4,200 and 1,500 km) and the flatness of the middle ground.
The curvature of the Earth makes longer point-to-point WiFi-links
difficult to achieve because line of sight between two points is
required.

\[5\] Radio waves occupy a volume around the optical line, which must be
unemcumbered from obstacles. This volume is known as the Fresnel
ellipsoid and its size grows with the distance between the two end
points and with the wavelength of the signal, which is in turn inversely
proportional to the frequency. Thus, it is required to leave extra
"elbow room" for the Fresnel zone. \[9\]

\[6\] [A Brief History of the Tegola
Project](http://www.tegola.org.uk/tegola-history.html), Tegola Project,
retrieved October 2015

\[7\] [WiLDNet: Design and Implementation of High Performance WiFi based
Long Distance
Networks](http://tier.cs.berkeley.edu/docs/wireless/wild_multihop.pdf)
(PDF), Rabin Patra et al., 2007

\[8\] [Topology Patterns of a Community Network:
Guifi.net](http://dsg.ac.upc.edu/sites/default/files/1569633605.pdf)
(PDF), Davide Vega et al., 2012

\[9\] [Global Access to the Internet for All, internet
draft](https://trac.tools.ietf.org/group/irtf/trac/wiki/gaia), Internet
Engineering Task Force (IETF), 2015

\[10\] This is what happened to Afghanistan's JLINK network when
[funding for the network's satellite link ran dry in
2012](http://www.wired.com/2012/05/jlink/).

\[11\] [The case for technology in developing
regions](http://www.cs.cmu.edu/~mattkam/lab/publications/Computer2005.pdf)
(PDF), Eric Brewer et al., 2005

\[12\] [Beyond Pilots: Keeping Rural Wireless Networks
Alive](https://www.usenix.org/legacy/event/nsdi08/tech/full_papers/surana/surana.pdf)
(PDF), Sonesh Surana et al., 2008

\[13\] <http://www.akshaya.kerala.gov.in/>

\[14\] <http://main.airjaldi.com/>

\[15\] [VillageCell: Cost Effective Cellular Connectivity in Rural
Areas](http://www.cs.bham.ac.uk/~pejovicv/docs/Anand12ICTD.pdf) (PDF),
Abhinav Anand et al., 2012

\[16\] [Deployment and Extensio of a Converged WiMAX/WiFi Network for
Dwesa Community Area South
Africa](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.452.7357&rep=rep1&type=pdf)
(PDF), N. Ndlovu et al., 2009

\[17\] "[A telemedicine network optimized for long distances in the
Amazonian jungle of
Peru](http://www.ehas.org/wp-content/uploads/2012/01/Extremecomm_sig_ISBN.pdf)"
(PDF), Carlos Rey-Moreno, ExtremeCom '11, September 2011

\[18\] "[Telemedicine networks of EHAS Foundation in Latin
America](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4197650/)", Ignacio
Prieto-Egido et al., in "Frontiers in Public Health", October 15, 2014.

\[19\] "[The design of a wireless solar-powered router for rural
environments isolated from health
facilities](https://eciencia.urjc.es/bitstream/handle/10115/2293/THE%20DESIGN%20OF%20A%20WIRELESS%20SOLAR-POWERED-2008.pdf?sequence=1)"
(PDF), Francisco Javier Simo Reigadas et al., in "IEEE Wireless
Communications", June 2008.

\[20\] [On a long wireless link for rural telemedicine in
Malawi](http://users.ictp.it/~mzennaro/Malawi.pdf) (PDF), M. Zennaro et
al., 2008

\[21\] [A Survey of Delay- and Disruption-Tolerant Networking
Applications](http://www.jie-online.org/index.php/jie/article/view/91),
Artemios G. Voyiatzis, 2012

\[22\] [Supporting Cloud Deployment in the Guifi Community
Network](https://www.sics.se/~amir/files/download/papers/guifi.pdf)
(PDF), Roger Baig et al., 2013

\[23\] [A Case for Research with and on Community
Networks](http://www.sigcomm.org/sites/default/files/ccr/papers/2013/July/2500098-2500108.pdf)
(PDF), Bart Braem et.al, 2013

\[24\] There are smaller networks in Scotland
([Tegola](http://www.tegola.org.uk/)), Slovenia ([wlan
slovenija](https://wlan-si.net/)), Belgium ([Wireless
Antwerpen](http://www.wirelessantwerpen.be/)), and the Netherlands
([Wireless Leiden](https://www.wirelessleiden.nl/)), among others.
Australia has [Melbourne Wireless](http://melbourne.wireless.org.au/).
In Latin America, numerous examples exists, such as [Bogota
Mesh](https://www.facebook.com/BogotaMesh) (Colombia) and [Monte Video
Libre](http://picandocodigo.net/2008/montevideolibre-redes-libres-en-montevideo/)
(Uruguay). Some of these networks are interconnected. This is the case
for the Belgian and Dutch community networks, and for the Slovenian and
Austrian networks. \[8,22,23\]

\[25\] [Proxy performance analysis in a community wireless
network](http://upcommons.upc.edu/handle/2099.1/19710), Pablo Pitarch
Miguel, 2013

\[26\] [RuralCafe: Web Search in the Rural Developing
World](http://www.ambuehler.ethz.ch/CDstore/www2009/proc/docs/p411.pdf)
(PDF), Jay Chen et al., 2009

\[27\] [A Delay-Tolerant Network Architecture for Challenged
Networks](http://www.kevinfall.com/seipage/papers/p27-fall.pdf) (PDF),
Kevin Fall, 2003

\[28\] [Delay- and Disruption-Tolerant Networks (DTNs)&mdash;A Tutorial
(version
2.0)](http://ipnsig.org/wp-content/uploads/2012/07/DTN_Tutorial_v2.04.pdf)
(PDF), Forrest Warthman, 2012

\[29\] [Healthcare Supported by Data Mule Networks in Remote Communities
of the Amazon
Region](http://www.hindawi.com/journals/isrn/2014/730760/), Mauro
Margalho Coutinho et al., 2014

\[30\] [First Mile Solutions' Daknet Takes Rural Communities
Online](http://www.firstmilesolutions.com/documents/FMS_Case_Study.pdf)
(PDF), Carol Chyau and Jean-Francois Raymond, 2005

\[31\] [DakNet: A Road to Universal Broadband
Connectivity](http://courses.media.mit.edu/2003fall/de/DakNet-Case.pdf)
(PDF), Amir Alexander Hasson et al., 2003

\[32\] [DakNet: Architecture and Connectivity in Developing
Nations](http://ijpret.com/publishedarticle/2015/4/IJPRET%20-%20ECN%20115.pdf)
(PDF), Madhuri Bhole, 2015

\[33\] [Delay Tolerant Networks and Their
Applications](http://www.citeulike.org/user/tnhh/article/13517347),
Longxiang Gao et al., 2015

\[34\] [Low-cost communication for rural internet kiosks using
mechanical
backhaul](https://people.csail.mit.edu/matei/papers/2006/mobicom_kiosks.pdf),
A. Seth et al., 2006

\[35\] [Searching the World Wide Web in Low-Connectivity
Communities](http://tek.sourceforge.net/papers/tek-www02.pdf) (PDF),
William Thies et al., 2002

\[36\] [Slow Search: Information Retrieval without Time
Constraints](http://www.cs.cmu.edu/~yubink/hcir2013.pdf) (PDF), Jaime
Teevan, 2013

\[37\] [Potential for Collaborative Caching and Prefetching in
Largely-Disconnected
Villages](http://mrmgroup.cs.princeton.edu/papers/isaacman-winsdr503.pdf)
(PDF), Sibren Isaacman et al., 2008
