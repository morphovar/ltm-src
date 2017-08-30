Title: The 4G Mobile Internet That's Already There
Date: 2015-10-25 15:03
Author: Kris De Decker
Category: Low-tech Solutions
Slug: the-4g-mobile-internet-thats-already-there
Status: published



These days, so many households have a WiFi-router installed that sharing
the signal of these devices could provide free mobile internet access
across densely populated cities.

Image: WiFi-routers (green & red) and cell towers (blue) in London,
2014-15. Source: [Wigle](https://wigle.net/).

Telecom operators are deploying 4G-networks at a rapid rate. These
mobile networks provide mobile internet access for smartphones at a
"speed" that is comparable to that of a WiFi-connection. However,
wireless internet access through 4G is expensive&mdash;you need a paid
subscription&mdash;and it's energy-intensive: [4G access consumes twenty
times more energy than making a connection through
WiFi]({filename}/posts/can-the-internet-run-on-renewable-energy.md).
\[1\] But do we really need those mobile networks?

At home, few of us access the internet through a cable these days. In
industrialized countries, WiFi-routers now provide a wireless connection
throughout the house. In cities, many thousands of these are deployed.
Because the range of a WiFi-router can be 30 metres or more, the signal
often reaches the street. Sharing the resources of these WiFi routers
could make 4G (and 3G) mobile networks redundant, at least in densely
populated areas.





Images: WiFi-routers in and around San Francisco, USA, 2014-15. The
images are made by "wardrivers": people that drive through streets to
record the location of wireless networks and then upload the data to
maps. The colour differences indicate the density of nodes or, in the
more detailed maps, the quality of the access points (green is high, red
is low). Blue dots represent cell towers. Source:
[Wigle](https://wigle.net/).

Research in French and British cities has revealed that downtown and
residential neighbourhoods have more than enough access points and
bandwidth available to make free and ubiquitous WiFi-access a reality,
without the need for extra infrastructure. \[2,3\] Add to this that most
broadband connections remain unexploited for much of the day and one can
begin to see the logic of an open network. \[4\]

Shared Wireless

Nowadays, most in-house WiFi-networks are locked down with a password to
protect privacy and security, and to prevent others from slowing down
the home network. But while these issues are of real concern, they could
be solved without denying access to freeloaders. It's perfectly possible
to create two separate networks on a WiFi-router: a network for private
use and a network for public use. The router can wall off one connection
from the other, preventing snooping and security risks. The router can
also priotize the network's owner's traffic over others, assuring
minimum download and upload speeds.

This so-called "shared-wireless" approach is not new. Some companies
(most notably FON) develop and sell routers with a dual access function.
People that buy such a router (FON often works together with internet
providers), gain access to all the routers associated to the community.
However, there's not really a need for a commercial company to organize
such a service. For example, the Electronic Frontier Foundation (EFF)
designed open-source firmware called *Open Wireless Router*, which
performs exactly the same function. \[5,6\]



An approach that's not economically driven would bring a lot of
benefits. First of all, we would be able to connect to any WiFi-router,
not only to those from our own internet service provider. \[2\] This
results in multiple access points, which makes shared-wireless a viable
alternative to mobile networks. Secondly, it would be a free service. By
sharing a small part of the bandwidth of our home router, we gain free
access to mobile internet whenever we step out of the door. Last but not
least, a community approach would stimulate innovation to get the best
out of the available resources.

A Surplus of Bandwidth

A 2014 experimental set-up of a shared-wireless network in a British
city found that broadband users on fibre contracts have so much spare
capacity available that it's not necessary to limit the bandwidth of
freeloaders. \[7\] However, those with DSL connections don't have this
spare capacity, especially not when it concerns upload speeds. In this
case, it's required to give sharers priority over freeloaders, and limit
the bandwidth of the public network. This could make it hard for
freeloaders to use bandwidth-intensive applications such as video
streaming. \[7\]

You could argue that this is a good thing, because it's precisely these
bandwidth-hungry applications that push the power usage of the internet
[higher and
higher]({filename}/posts/can-the-internet-run-on-renewable-energy.md).
There's also ample opportunity for technical improvements. For example,
it could be so arranged that the availability of public bandwidth varies
depending on the activities of the owner. Thus, a DSL connection could
be completely available to passers-by while the owner of the connection
is at work or on holidays, for instance. \[8\]



WiFi-routers in Brussels, Belgium, 2014-15. Blue dots are cell towers.
Source: [Wigle](https://wigle.net/).

Home WiFi routers could also be equipped with storage capabilities,
which increases connectivity opportunities for mobile internet users.
The stored packages can be forwarded to another home router in range, or
relayed to a mobile user that may find another connectivity point.
Research has shown that this approach&mdash;using only 30 MB of storage per
home router&mdash;significantly inproves the service quality for mobile
users \[4,9\] Another idea is WiFi-Direct, which connects two
WiFi-enabled devices without the need for a WiFi-router&mdash;similar to
Bluetooth but much faster and with a wider range. \[10\]

The range of a WiFi-router can also be increased in a spectacular way
through protocol changes and the use of antennas, which is especially
interesting for remote regions. That's the topic of [the next
post]({filename}/posts/how-to-build-a-low-tech-internet.md).

Kris De Decker (edited by [Jenna
Collett](https://www.linkedin.com/pub/jenna-collett/1a/925/b3))

Sources:

\[1\] "[A close examination of performance and power characteristics of
4G LTE
networks](http://www.cs.columbia.edu/%7Elierranli/coms6998-7Spring2014/papers/rrclte_mobisys2012.pdf)"
(PDF), Junxian Huang, June 2012. See also: "[Emerging trends in
electricity consumption for consumer
ICT](http://vmserver14.nuigalway.ie/xmlui/handle/10379/3563)", Peter
Corcoran, 2013 and "[Energy consumption in mobile phones: a measurement
study and implications for network
applications](http://ciir-publications.cs.umass.edu/getpdf.php?id=904)"
(PDF), Niranjan Balasubramanian, 2009. For an in-depth review of the
internet's growing energy use, see our previous article: "[Why we need a
speed limit for the
internet]({filename}/posts/can-the-internet-run-on-renewable-energy.md)".

\[2\] [Global Access to the Internet for All, internet
draft](https://trac.tools.ietf.org/group/irtf/trac/wiki/gaia), Internet
Engineering Task Force (IETF), 2015

\[3\] "[An evaluation of IEEE 802.11 community networks
deployments](https://hal.archives-ouvertes.fr/hal-00609307/document)",
German Castignani, Lucien Loiseau, Nicolas Montavont, International
Conference on Information Networking, 2011

\[4\] "[Storage-enabled access points for improved mobile performance:
an evaluation
study](http://www.ee.ucl.ac.uk/%7Euceeips/storage-APs-wwic11-ipsaras.pdf)",
E. Koutsogiannis, 2011

\[5\] [Why we need an open wireless
movement](https://www.eff.org/deeplinks/2011/04/open-wireless-movement),
EFF, 2011

\[6\] [New open-source router firmware opens your wi-fi network to
strangers](http://arstechnica.com/tech-policy/2014/06/new-router-firmware-safely-opens-your-wi-fi-network-to-strangers/),
Ars Technica, 2014

\[7\] "[A feasibility study of an in-the-wild experimental public access
WiFi network](http://www.cl.cam.ac.uk/%7Eas2330/docs/dev12.pdf)", Arjuna
Sathiaseelan, 2014

\[8\] "[Virtual Public
Networks](http://www.cl.cam.ac.uk/%7Eas2330/docs/vpun.pdf)", Arjuna
Sathiaseelan, 2014

\[9\] "[A survey of Delay- and Disruption-Tolerant Networking
Applications](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.463.6280)",
Artemios G. Voyiatzis, 2012

\[10\] "[WiFi
Direct](http://www.wi-fi.org/discover-wi-fi/wi-fi-direct)", WiFi
Alliance.

[How to Make Everything Ourselves: Open Modular
Hardware]({filename}/posts/how-to-make-everything-ourselves-open-modular-hardware.md)



Reverting to traditional handicrafts is one way to sabotage the
throwaway society. In this article, we discuss another possibility: the
design of modular consumer products, whose parts and components could be
re-used for the design of other products.

Initiatives like OpenStructures, Grid Beam, and Contraptor combine the
modularity of systems like LEGO, Meccano and Erector with the
collaborative power of digital success stories like Wikipedia, Linux or
WordPress.

An economy based on the concept of re-use would not only bring important
advantages in terms of sustainability, but would also save consumers
money, speed up innovation, and take manufacturing out of the hands of
multinationals. [Read more: How to make everything ourselves: open
modular
hardware]({filename}/posts/how-to-make-everything-ourselves-open-modular-hardware.md).
