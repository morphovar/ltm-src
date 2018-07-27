Title: Ditch the batteries: Off-grid compressed air energy storage
Date: 2018-05-16
Category: Low-tech Solutions
Tags: energy storage, compressed air, off-the-grid
Slug: ditch-the-batteries-off-the-grid-compressed-air-energy-storage
Summary: Compressed air energy storage is the sustainable and resilient alternative to chemical batteries, with much longer life expectancy, lower life cycle costs, technical simplicity, and low maintenance.
Status: published

![DIY compressed air energy storage](/images/DIY-compressed-air-energy-storage.png)

Going off-grid? Think twice before you invest in a battery system. Compressed air energy storage is the sustainable and resilient alternative to batteries, with much longer life expectancy, lower life cycle costs, technical simplicity, and low maintenance. Designing a compressed air energy storage system that combines high efficiency with small storage size is not self-explanatory, but a growing number of researchers show that it can be done.

Compressed Air Energy Storage (CAES) is usually regarded as a form of large-scale energy storage, comparable to a pumped hydropower plant. Such a CAES plant compresses air and stores it in an underground cavern, recovering the energy by expanding (or decompressing) the air through a turbine, which runs a generator.

Unfortunately, large-scale CAES plants are very energy inefficient. Compressing and decompressing air introduces energy losses, resulting in an electric-to-electric efficiency of only 40-52%, compared to 70-85% for pumped hydropower plants, and 70-90% for chemical batteries.

The low efficiency is mainly since air heats up during compression. This waste heat, which holds a large share of the energy input, is dumped into the atmosphere. A related problem is that air cools down when it is decompressed, lowering electricity production and possibly freezing the water vapour in the air. To avoid this, large-scale CAES plants heat the air prior to expansion using natural gas fuel, which further deteriorates the system efficiency and makes renewable energy storage dependent on fossil fuels.

## Why Small-scale CAES?

In the previous article, we outlined several ideas – [inspired by historical systems](/2018/05/history-and-future-of-the-compressed-air-economy.html) – that could improve the efficiency of large-scale CAES plants. In this article, we focus on the small but growing number of engineers and researchers who think that the future is not in large-scale compressed air energy storage, but rather in small-scale or micro systems, using man-made, aboveground storage vessels instead of underground reservoirs. Such systems could be off-the-grid or grid-connected, either operating by themselves or alongside a battery system.

The main reason to investigate decentralised compressed air energy storage is the simple fact that such a system could be installed anywhere, just like chemical batteries. Large-scale CAES, on the other hand, is dependent on a suitable underground geology. Although there are more potential sites for large-scale CAES plants than for large-scale pumped hydropower plants, finding appropriate storage caverns is not as easy as was previously assumed.[^1][^2][^3]

![set up small scale compressed air energy storage system](/images/set-up-small-scale-compressed-air-energy-storage-system.png)
Experimental set-up of small-scale compressed air energy storage system. Source: [^27]

Compared to chemical batteries, micro-CAES systems have some interesting advantages. Most importantly, a distributed network of compressed air energy storage systems would be much more sustainable and environmentally friendly. Over their lifetimes, [chemical batteries store only two to ten times the energy needed to manufacture them](/2015/05/sustainability-off-grid-solar-power.html). [^4] Small-scale CAES systems do much better than that, mainly because of their much longer lifespan.

> Compared to chemical batteries, a distributed network of compressed air energy storage systems would be much more sustainable and environmentally friendly

Furthermore, they do not require rare or toxic materials, and the hardware is easily recyclable. In addition, decentralised compressed air energy storage doesn’t need high-tech production lines and can be manufactured, installed and maintained by local business, unlike an energy storage system based on chemical batteries. Finally, micro-CAES has no self-discharge, is tolerant of a wider range of environments, and promises to be cheaper than chemical batteries. [^5]

![sustainability of different energy storage technologies](/images/sustainability-of-different-energy-storage-technologies.png)

Although the initial investment cost is estimated to be higher than that of a battery system (around $10,000 for a typical residential set-up), and although above-ground storage increases the costs in comparison to underground storage (the storage vessel is good for roughly half of the investment cost), a compressed air energy storage system offers an almost infinite number of charge and discharge cycles. Batteries, on the other hand, need to be replaced every few years, which makes them more expensive in the long run. [^5][^6]

## Challenge: Limiting Storage Size

However, decentralised CAES also faces important challenges. The first is the system efficiency, which is a problem in large- and small-scale systems alike, and the second is the size of the storage vessel, which is especially problematic for small-scale CAES systems.

Both issues make small-scale CAES systems unpractical. Sufficient space for a large storage vessel is not always available, while a low storage efficiency requires a larger solar PV or wind power plant to make up for that loss, raising the costs and lowering the sustainability of the system.

To make matters worse, system efficiency and storage size are inversely related: improving one factor is often at the expense of the other. Increasing the air pressure minimizes the storage size but decreases the system efficiency, while using a lower pressure makes the system more energy efficient but results in a larger storage size. Some examples help illustrate the problem.

![compressed air tanks](/images/compressed-air-tanks.jpg)
Compressed air energy storage tanks. [Source](http://www.screwtypeaircompressors.com/sale-8108163-vertical-compressed-air-tank-natural-gas-tank-2000l-air-receiver-tank.html).

A simulation for a stand-alone CAES aimed at unpowered rural areas, and which is connected to a solar PV system and used for lighting only, operates at a relatively low air pressure of 8 bar and obtains a round-trip efficiency of 60% -- comparable to the efficiency of lead-acid batteries. [^7]

However, to store 360 Wh of potential electrical energy, the system requires a storage reservoir of 18 m3, the size of a small room measuring 3x3x2 metres. The authors note that “although the tank size appears very large, it still makes sense for applications in rural areas”.

> System efficiency and storage size are inversely related: improving one factor is often at the expense of the other.

Such a system may indeed be beneficial in this context, especially because it has a much longer lifespan than chemical batteries. However, a similar configuration in an urban context with high energy use is obviously problematic. In another study, it was calculated that it would take a 65 m3 air storage tank to store 3 kWh of energy. This corresponds to a 13 metre long pressure vessel with a diameter of 2.5 metres, shown below. [^8]

![air receiver](/images/air-receiver.png)

Furthermore, average household electricity use per day in industrialised countries is much higher still. For example, in the UK it’s slightly below 13 kWh per day, in the US and Canada it’s more than 30 kWh. In the latter case, ten such air pressure tanks would be required to store one day of electricity use.

Small-scale CAES systems with high pressures give the opposite results. For example, a configuration modelled for a typical household electrical use in Europe (6,400 kWh per year) operates at a pressure of 200 bar (almost 4 times higher than the pressure in large-scale CAES plants) and achieves a storage volume of only 0.55 m3, which is comparable to batteries. However, the electric-to-electric efficiency of this set-up is only 11-17%, depending on the size of the solar PV system. [^9]

## Two Strategies to Make Micro CAES work

These examples seem to suggest that compressed air energy storage makes no sense as a small-scale energy storage system, [even with a reduction in energy demand](/2018/01/how-much-energy-do-we-need.html). However, perhaps surprisingly to many, this is not the case.

Small-scale CAES systems cannot follow the same approach as large-scale CAES systems, which increase storage capacity and overall efficiency by using multi-stage compression with intercooling and multi-stage expansion with reheating. This method involves additional components and increases the complexity and cost, which is impractical for small-scale systems.

![modular compressed air energy storage](/images/modular-compressed-air-energy-storage.jpg)

The same goes for “adiabatic” processes (AA-CAES), which aim to use the heat of compression to reheat the expanding air, and which are the main research focus for large-scale CAES. For a micro-CAES system, it’s very important to simplify the structure as much as possible. [^5][^10]

This leaves us with two low-tech strategies that can be followed to achieve similar storage capacity and energy efficiency as lead-acid batteries. First, we can design low pressure systems which minimize the temperature differences during compression and expansion. Second, we can design high pressure systems in which the heat and cold from compression and expansion are used for household applications.

## Small-scale, High Pressure

Small-scale compressed air energy storage systems with high air pressures turn the inefficiency of compression and expansion into an advantage. While large-scale AA-CAES aims to recover the heat of compression with the aim of maximizing electricity production, these small-scale systems take advantage of the temperature differences to allow trigeneration of electrical, heating and cooling power. The dissipated heat of compression is used for residential heating and hot water production, while the cold expanding air is used for space cooling and refrigeration. Chemical batteries can’t do this.

> Small-scale, high pressure systems use the dissipated heat of compression for residential heating and hot water production, while the cold expanding air is used for space cooling and refrigeration.

In these systems, the electric-to-electric efficiency is very low. However, there are now several efficiencies to define, because the system also supplies heat and cold. [^10][^11] Furthermore, this approach can make several electrical appliances unnecessary, such as the refrigerator, the air-conditioning, and the electric boiler for space and water heating. Since the use of these appliances is often responsible for roughly half of the electricity use in an average household, a small-scale CAES system with high pressure has lower electricity demand overall.

![air compressor](/images/air-compressor.jpg)
A typical air compressor. [Source](https://www.thomasnet.com/articles/machinery-tools-supplies/Air-Compressors).

High pressure systems easily solve the issue of storage size. As we have seen, a higher air pressure can greatly reduce the size of a compressed air storage vessel, but only at the expense of increased waste heat. In a small-scale system that takes advantage of temperature differences to provide heating and cooling, this is advantageous. Therefore, high pressure systems are ideal for small-scale residential buildings, where storage space is limited and where there is a large demand for heat and cold as well as electricity. The only disadvantages are that high pressure systems require stronger and more expensive storage tanks, and that extra space is required for heat exchangers.

![experimental setup of a micro caes system](/images/Experimental-set-up-of-a-micro-CAES-system.jpg)
Experimental set-up of a micro CAES system. Source: [^30]

Several research groups have designed, modeled and built small-scale combined heat-and-power CAES units which provide heating and cooling as well as electricity. The high pressure system with a storage volume of only 0.55 m3 that we mentioned earlier, is an example of this type of system. [^9] As noted, its electrical efficiency is only 11-17%, but the system also produces sufficient heat to produce 270 litres of hot water per day. If this thermal source of energy is also taken into account, the “exergetic” efficiency of the whole system is close to 70%. Similar "exergy" efficiencies can be found in other studies, with systems operating at pressures between 50 and 200 bar. [^11][^21]

Heat and cold from compression and expansion can be distributed to heating or cooling devices by means of water or air. The setup of an air cycle heating and cooling system is very similar to a CAES system, except for the storage vessel. Air cycle heating and cooling has many advantages, including high reliability, ease of maintenance, and the use of a natural refrigerant, which is environmentally benign. [^11]

## Small-scale, Low Pressure

The second strategy to achieve higher efficiencies and lower storage volumes is exactly the opposite from the first. Instead of compressing air to a high pressure and taking advantage of the heat and cold from compression and expansion, a second class of small-scale CAES systems is based on low pressures and “near-isothermal” compression and expansion.

Below air pressures of roughly 10 bar, the compression and expansion of air exhibit insignificant temperature changes (“near-isothermal”), and the efficiency of the energy storage system can be close to 100%. There is no waste heat and consequently there is no need to reheat the air upon expansion. 

![hiscox three stage compressor](/images/hiscox-three-stage-compressor.png)

Isothermal compression requires the least amount of energy to compress a given amount of air to a given pressure. However, reaching an isothermal process is far from reality. To start with, it only works with small and/or slowly cycling compressors and expanders. Unfortunately, typical industrial compressors are not made for maximum efficiency but for maximum power and thus work under fast-cycling, non-isothermal conditions. The same goes for most industrial expanders. [^22][^24]

> Below air pressures of 10 bar, compression and expansion of air exhibit insignificant temperature changes and the efficiency can be close to 100%.

The use of industrial compressors and expanders explains in large part why the low pressure CAES systems mentioned at the beginning of this article have such large storage vessels. Both systems are based on devices which are operated outside of their optimal or rated conditions. [^25] Because inefficiencies multiply during energy conversions, even relatively small differences in the efficiency of compressors and expanders can have large effects. For example, a variation in device efficiency from 60% to 80% results in a system efficiency from 36% to 64%, respectively.

## New Types of Compressors and Expanders

Because the performance of a compressor and an expander significantly impact the overall efficiency of a small-scale CAES system, several researchers have built their own compressors and expanders, which are especially aimed at energy storage. For example, one team designed, built and examined a single-stage, low power isothermal compressor that uses a liquid piston. [^22] It operates at a very low compression rate (between 10-60 rpm), which correspond to the output of solar PV panels, and limits temperature fluctuation during compression and expansion to 2 degrees Celsius.

The low-cost device has minimum moving parts and obtains efficiencies of 60-70% at 3 to 7 bar pressure. [^22] This is a very high efficiency for such a simple device, considering that a sophisticated three-stage centrifugal compressor, used in large-scale CAES systems or in industrial settings, is roughly 70% efficient. Furthermore, the researchers state that the efficiency is limited by the off-the-shelf motor that they use to power their compressor. Indeed, another research team achieved 83% efficiency. [^26]

![scroll compressor](/images/scroll-compressor.jpg)
A scroll compressor. Source: [^30]

Another novelty is the use of scroll compressors, which are the types of compressors that are now used in refrigerators, air-conditioning systems, and heat pumps. Both fluid piston and scroll compressors have a high area-to-volume ratio, which minimizes heat production, and can easily handle two-phase flow, which means that they can also be used as expanders. They are also lighter and less noisy than typical reciprocating compressors. [^24]

## Varying Air Pressure

Although compressors and expanders are the most important determinants of system efficiency in small-scale CAES systems, they are not the only ones. For example, in every compressed air energy storage system, additional efficiency loss is caused by the fact that during expansion the storage reservoir is depleted and therefore the pressure drops. Meanwhile, the input pressure for the expander is required to vary only in a minimal range to assure high efficiency.

![air pressure gauge](/images/air-pressure-gauge.png)

This is usually solved in two ways, although neither is really satisfactory. First, air can be stored in a tank with surplus pressure, after which it is throttled down to the required expander input pressure. However, this method – which is used in large-scale CAES – requires additional energy use and thus introduces inefficiency. Second, the expander can operate at variable conditions, but in this case efficiency will drop along with the pressure while the storage is emptied.

> During expansion the storage reservoir is depleted and therefore the pressure drops.

With these problems in mind, a team of researchers combined a small-scale CAES with a small-scale pumped hydropower plant, resulting in a system that maintains a steady pressure during the complete discharge of the storage reservoir. It consists of two compressed air tanks that are connected by a pipe attached to their lower portions: each of these have separate spaces for air (below) and water storage (above). The configuration maintains a head of water by means of a pump, which consumes 15% of the generated power. However, in spite of this extra energy use, the researchers managed to increase both the efficiency and the energy density of the system. [^11]

## Off-the-Grid Power Storage

To give an idea of what a combination of the right components can achieve, let’s have a look at a last research project. [^27] It concerns a system that is based on a highly efficient, custom-made compressor/expander, which is directly coupled to a DC motor/generator. Apart from its efficient components, this CAES project also introduces an innovative system configuration. It doesn’t use one large air storage tank, but several smaller ones, which are interconnected and computer-controlled.

The setup consists of the compression/expansion unit coupled to three small (7L) cylinders, previously used as air extinguishers, and operates at low pressure (max 5 bar). The storage vessels are connected via PVC pipework and brass fittings. To control the air-flow, three computer-controlled air valves are installed at the inlet of each cylinder. The system can be extended by adding more pressure vessels. [^27]

![small scale caes setup](/images/small-scale-CAES-setup.png)

A modular configuration results in a higher system efficiency and energy density for mainly two reasons. First, it helps more effective heat transfer to take place, because every air tank acts as an additional heat exchanger. Second, it allows better control over the discharge rate of the storage reservoir. The cylinders can be discharged either in unison to satisfy a demand for high power density (more power at the cost of a shorter discharge time), or they can be discharged sequentially to satisfy a demand for high energy density (longer discharge time at the cost of maximum power).

> By discharging modular storage cylinders sequentially, the discharge time can be greatly increased, making the system comparable to lead-acid batteries in terms of energy density. 

By discharging the cylinders sequentially, the discharge time can be greatly increased, making the system comparable to lead-acid batteries in terms of energy density. Based on their experimental set-up, the researchers calculated the efficiencies for different starting pressures and numbers of cylinders. They found that 57 interconnected cylinders of 10 litre each, operating at 5 bar, could fulfill the job of four 24V batteries for 20 consecutive hours, all while having a surprisingly small footprint of just 0.6 m3. 

Interestingly, the storage capacity is 410 Wh, which is comparable to the 360 Wh rural system noted earlier, which requires an 18 m3 storage vessel – that’s thirty times larger than the modular storage system.

![computer controlled air valves](/images/computer-controlled-air-valves.jpg)
Computer-controlled air valves. [Source](http://www.jaksa.si/compressed-air-solenoid-valves.html).

The electric-to-electric efficiency for the 3-cylinder set-up reached a peak of 85% at 3 bar pressure, while the estimated efficiency for the 57-cylinder set-up is 75%. These are values comparable to lithium-ion batteries, but adding more storage vessels or operating at higher pressures introduces larger losses due to compression, heat, friction and fittings. [^27][^29]

Nevertheless, when I e-mailed Abdul Alami, the main author of the study, thinking that the results sounded too good to be true, he told me that the figures were actually overly conservative: “We stuck to low pressures to achieve near-isothermal compression and to ensure safe operation. Operating at pressures higher than 10 bar would create serious thermal losses, but a pressure of 7-8 bar may be beneficial in terms of energy and power density, though maybe not in terms of efficiency.”

## Build it Yourself?

In conclusion, small-scale compressed air energy storage could be a promising alternative to batteries, but the research is still in its early stages – the first study on small-scale CAES was published in 2010 – and new ideas will continue to shed light on how best to develop the technology. At the moment, there are no commercial products available, and setting up your own system can be quite intimidating if you are new to pneumatics. Simply getting hold of the right components and fittings is a headache, as these come in a bewildering variety and are only sold to industries.

However, if you’re patient and not too unhandy, and if you are determined to use a more sustainable energy storage system, it is perfectly possible to build your own CAES system. As the examples in this article have shown, it’s just a bit harder to build a good one.

Kris De Decker

There's more ideas for small-scale CAES systems in the previous article: [History and Future of the Compressed Air Economy](/2018/05/history-and-future-of-the-compressed-air-economy.html).

## References & Notes:

[^1]: Luo, Xing, et al. "Overview of current development in electrical energy storage technologies and the application potential in power system operation." Applied Energy 137 (2015): 511-536. https://www.sciencedirect.com/science/article/pii/S0306261914010290

[^2]: Laijun, C. H. E. N., et al. "Review and prospect of compressed air energy storage system." Journal of Modern Power Systems and Clean Energy 4.4 (2016): 529-541. https://link.springer.com/article/10.1007/s40565-016-0240-5

[^3]: There is increasing competition for potential CAES geologic units, as many are also well suited to the storage of natural gas or sequestered carbon. Furthermore, cavern storage imposes harsh requirements on the geographical conditions. For example, the originally planned Iowa CAES project in the US was terminated due to its porous sandstone condition. [^2]

[^4]: Barnhart, Charles J., and Sally M. Benson. "On the importance of reducing the energetic and material demands of electrical energy storage." Energy & Environmental Science 6.4 (2013): 1083-1092. https://gcep.stanford.edu/pdfs/EES_reducingdemandsonenergystorage.pdf

[^5]: Petrov, Miroslav P., Reza Arghandeh, and Robert Broadwater. "Concept and application of distributed compressed air energy storage systems integrated in utility networks." ASME 2013 Power Conference. American Society of Mechanical Engineers, 2013. http://eddism.com/wp-content/uploads/2014/10/Paper-EDD-Concept-and-Application-of-Distributed-Compressed-Air-Energy-Storage-Systems-Integrated-in-Utility-Networks-July-2013.pdf

[^6]: Tallini, Alessandro, Andrea Vallati, and Luca Cedola. "Applications of micro-CAES systems: energy and economic analysis." Energy Procedia 82 (2015): 797-804.

[^7]: Setiawan, A., et al. "Sizing compressed-air energy storage tanks for solar home systems." Computational Intelligence and Virtual Environments for Measurement Systems and Applications (CIVEMSA), 2015 IEEE International Conference on. IEEE, 2015. https://www.researchgate.net/profile/Ardyono_Priyadi/publication/274898992_Sizing_Compressed-Air_Energy_Storage_Tanks_for_Solar_Home_Systems/links/5670e2c408ae2b1f87acf927.pdf

[^8]: Herriman, Kayne. "Small compressed air energy storage systems." (2013). https://eprints.usq.edu.au/24651/1/Herriman_2013.pdf

[^9]: Manfrida, Giampaolo, and Riccardo Secchi. "Performance prediction of a small-size adiabatic compressed air energy storage system." International Journal of Thermodynamics 18.2 (2015): 111-119. http://dergipark.ulakbim.gov.tr/eoguijt/article/download/5000071710/5000113411

[^10]: Kim, Y. M., and Daniel Favrat. "Energy and exergy analysis of a micro-compressed air energy storage and air cycle heating and cooling system." Energy 35.1 (2010): 213-220.

[^11]: Kim, Young Min. "Novel concepts of compressed air energy storage and thermo-electric energy storage." (2012). https://infoscience.epfl.ch/record/181540/files/EPFL_TH5525.pdf

[^12]: Inder, Shane D., and Mehrdad Khamooshi. "Energy Efficiency Analysis of Discharge Modes of an Adiabatic Compressed Air Energy Storage System." World Academy of Science, Engineering and Technology, International Journal of Electrical, Computer, Energetic, Electronic and Communication Engineering 11.12 (2017): 1101-1109. 

[^13]: Vollaro, Roberto De Lieto, et al. "Energy and thermodynamical study of a small innovative compressed air energy storage system (micro-CAES)." Energy Procedia 82 (2015): 645-651.

[^14]: Li, Yongliang, et al. "A trigeneration system based on compressed air and thermal energy storage." Applied Energy 99 (2012): 316-323. https://www.sciencedirect.com/science/article/pii/S0306261912003479 

[^15]: Facci, Andrea L., et al. "Trigenerative micro compressed air energy storage: Concept and thermodynamic assessment." Applied energy 158 (2015): 243-254. https://www.sciencedirect.com/science/article/pii/S0306261915009526 

[^16]: Mohammadi, Amin, et al. "Exergy analysis of a Combined Cooling, Heating and Power system integrated with wind turbine and compressed air energy storage system." Energy Conversion and Management 131 (2017): 69-78. https://www.sciencedirect.com/science/article/pii/S0306261915009526 

[^17]: Yao, Erren, et al. "Thermo-economic optimization of a combined cooling, heating and power system based on small-scale compressed air energy storage." Energy Conversion and Management 118 (2016): 377-386. https://www.sciencedirect.com/science/article/pii/S0196890416302229 

[^18]: Liu, Jin-Long, and Jian-Hua Wang. "Thermodynamic analysis of a novel tri-generation system based on compressed air energy storage and pneumatic motor." Energy 91 (2015): 420-429. https://www.sciencedirect.com/science/article/pii/S0360544215011317 

[^19]: Lv, Song, et al. "Modelling and analysis of a novel compressed air energy storage system for trigeneration based on electrical energy peak load shifting." Energy Conversion and Management 135 (2017): 394-401. https://www.sciencedirect.com/science/article/pii/S0196890416311839 

[^20]: Besharat, M. O. H. S. E. N., SANDRA C. Martins, and HELENA M. Ramos. "Evaluation of Energy Recovery in Compressed Air Energy Storage (CAES) Systems." 3rd IAHR Europe Congress. Book of Proceedings, Portugal. 2014. https://www.researchgate.net/profile/Mohsen_Besharat2/publication/270896130_Evaluation_of_Energy_Recovery_in_Compressed_Air_Energy_Storage_CAES_Systems/links/58a1fce0a6fdccf5e97109b2/Evaluation-of-Energy-Recovery-in-Compressed-Air-Energy-Storage-CAES-Systems.pdf 

[^21]: Minutillo, M., A. Lubrano Lavadera, and E. Jannelli. "Assessment of design and operating parameters for a small compressed air energy storage system integrated with a stand-alone renewable power plant." Journal of Energy Storage 4 (2015): 135-144. https://www.sciencedirect.com/science/article/pii/S2352152X15300207 

[^22]: Villela, Dominique, et al. "Compressed-air energy storage systems for stand-alone off-grid photovoltaic modules." Photovoltaic Specialists Conference (PVSC), 2010 35th IEEE. IEEE, 2010. https://pdfs.semanticscholar.org/9f1d/4273f8deb4a0a18c86eb4056e2fd378f8f3f.pdf

[^23]: Paloheimo, H., and M. Omidiora. "A feasibility study on Compressed Air Energy Storage system for portable electrical and electronic devices." Clean Electrical Power, 2009 International Conference on. IEEE, 2009. https://www.researchgate.net/profile/Michael_Omidiora/publication/224581292_A_Feasibility_Study_on_Compressed_Air_Energy_Storage_System_for_Portable_Electrical_and_Electronic_Devices/links/5640d5d308aebaaea1f6ad44.pdf 

[^24]: Prinsen, Thomas H. Design and analysis of a solar-powered compressed air energy storage system. Naval Postgraduate School Monterey United States, 2016. https://scholar.google.com/scholar?cluster=5783353621699682542&hl=nl&as_sdt=2005&sciodt=0,5

[^25]: The small-scale system aimed at urban environments, which has a storage reservoir of 18 metres long, is based on a compressor that “had been in service for 30 years on building sites to run various air tools and had little maintenance done”. [^8] This is detrimental to system efficiency, because a compressor that is not maintained well easily wastes as much as 30% of its potential output through air leaks, increased friction, or dirty air filters. This small-scale system also used a highly inefficient expander. All together, this explains why it combines a very large storage volume with a very low electric-to-electric efficiency (less than 5%).

[^26]: Van de Ven, James D., and Perry Y. Li. "Liquid piston gas compression." Applied Energy 86.10 (2009): 2183-2191. https://experts.umn.edu/en/publications/liquid-piston-gas-compression

[^27]: Alami, Abdul Hai, et al. "Low pressure, modular compressed air energy storage (CAES) system for wind energy storage applications." Renewable Energy 106 (2017): 201-211.

[^28]: Alami, Abdul Hai. "Experimental assessment of compressed air energy storage (CAES) system and buoyancy work energy storage (BWES) as cellular wind energy storage options." Journal of Energy Storage 1 (2015): 38-43.

[^29]: Abdul Alami, e-mail conversation.

[^30]: Sun, Hao, Xing Luo, and Jihong Wang. "Feasibility study of a hybrid wind turbine system–Integration with compressed air energy storage." Applied Energy 137 (2015): 617 -628. https://www.sciencedirect.com/science/article/pii/S0306261914006680 
