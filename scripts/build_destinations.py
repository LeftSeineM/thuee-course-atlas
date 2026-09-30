"""Build the editorial research/industry layer. Course records stay in catalog.json."""
from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
institutes=[
 ('circuits','电路与系统研究所','从器件与电路走向计算系统','官网列出电子系统设计自动化、模拟与混合信号电路、智能传感、高能效硬件计算等方向。'),
 ('wireless','通信研究所','让信息可靠、高效地跨越距离','官网介绍无线通信、通信网络、数字信号处理与终端、通信SoC等研究方向。'),
 ('vision','信息认知与智能系统研究所','让机器看懂、听懂并理解信息','官网研究涉及跨媒体认知、多模态智能体、图像与语音处理，以及智慧医疗等领域。'),
 ('rf','微波与天线研究所','理解、控制与测量电磁波','官网研究涉及电磁理论、微波电路、天线、电波传播、电磁计算与测量等领域。'),
 ('photonics','信息光电子研究所','用光产生、传输和处理信息','官网介绍集成光电器件、微纳光电材料、光通信与网络、微波光子学等方向。'),
 ('systems','信息系统研究所','从观测中提取位置、目标与环境信息','官网研究涉及导航定位、探测感知、网络协同及显微图像处理等领域。')]
institutes=[dict(id=i,name=n,subtitle=s,fact=f,source=i+'-research') for i,n,s,f in institutes]

# Question/method/project/metrics are explanatory examples, not advertised lab projects.
text='''eda|circuits|电子系统设计自动化|怎样让电路仿真更快，又不失去可信度？|数值求解、稀疏矩阵、性能分析；在同一误差条件下比较运行时间。|program,algorithm,linear,circuit,ic|用小规模电阻网络组装方程，对比稠密与稀疏求解。|时间、内存、残差；说明规模变大后哪一步成为瓶颈。|数值分析、优化、EDA工具与电路建模。|chips
mixed|circuits|模拟与混合信号电路|在有限功耗下，怎样把模拟信号更准确地转换成数字？|电路建模、频谱分析、噪声预算，结合仿真与测量。|circuit,signal,analogcourse,solid,circuitlab|模拟量化位数和采样抖动，比较同一正弦信号的输出频谱。|信噪失真比、带宽与功耗假设；不要只报一个最佳数值。|半导体器件、反馈稳定性、SPICE与芯片测试。|chips,instruments
smart-sensor|circuits|智能传感芯片与系统|电池供电的传感节点怎样长期工作并保留有效信息？|采样策略、低功耗调度、校准与嵌入式数据处理。|circuit,digital,program,statsignal,build|用同一段温度或振动数据，比较固定采样和事件触发采样。|采样次数、信息误差、能耗估算与异常漏报情况。|低功耗硬件、传感器接口、时钟与误差预算。|instruments,robotics
efficient-compute|circuits|高能效硬件计算|同一个算法怎样通过改变硬件组织减少访存和能耗？|算子分解、数据流设计、软硬件协同与性能剖析。|digital,digitalsystem,architecture,algorithm,ic|为小型矩阵乘法比较两种分块与数据复用方式。|访存量、执行时间、资源占用；验证数值结果一致。|计算机体系架构、并行计算、硬件描述语言与测量方法。|chips,software
wireless-link|wireless|无线通信与系统|多径和噪声存在时，接收机怎样恢复正确的信息？|信道建模、调制检测、同步估计和蒙特卡洛仿真。|signal,probability,network,commsignal,commsystem|在BPSK基线上加入简化多径，比较均衡前后的误码率。|误码率曲线、算法开销、不同信道下的失效条件。|数字通信、估计理论、具体标准和可复现实验。|connectivity
network-resource|wireless|通信网络与资源分配|多个用户共享有限带宽时，怎样兼顾吞吐、公平和时延？|排队建模、调度算法、网络仿真与约束优化。|network,infonetwork,probability,algorithm,os|模拟两个不同流量用户，对比轮询和按队列长度调度。|平均与尾部时延、吞吐、公平性；记录负载条件。|优化方法、网络协议、分布式系统与网络实验。|connectivity,software
coding-detection|wireless|编码与通信信号处理|用多少冗余，才能在噪声中更可靠地传送信息？|纠错编码、检测估计、复杂度与性能边界分析。|coding,probability,signal,dsp,commsignal|实现简单纠错码，与未编码链路在统一能量口径下比较。|误码率、编码率、解码开销；写清比较是否公平。|信息论、数字通信、矩阵计算与概率推导。|connectivity,chips
comm-soc|wireless|通信SoC与终端实现|通信算法搬到真实芯片后，怎样保持实时性和精度？|定点化、流水线、软硬划分、仿真与验证。|digital,dsp,dspsystem,architecture,commproject|把一个浮点滤波器改成定点实现，扫描位宽。|数值误差、运算量、存储占用与处理时延。|定点数值分析、HDL、嵌入式开发与接口协议。|chips,connectivity
multimodal|vision|跨媒体认知与表示学习|图像和文字描述不完全一致时，机器怎样建立对应关系？|特征表示、对比学习、检索评估与消融实验。|cognition,algorithm,linear,probability,image|用公开的图文特征做检索基线，检查错误匹配的类型。|Recall@K、错误样例、不同数据划分下的变化。|机器学习、优化、数据处理与模型评估；避免训练测试泄漏。|software
speech-vision|vision|语音、图像与信号理解|环境变化后，识别方法为什么失效，怎样验证改进？|信号预处理、表征学习、鲁棒性测试与误差分析。|signal,dsp,speech,image,cognition|对同一批样本逐步加入噪声或亮度变化，测试基线。|准确率随扰动变化的曲线、失败类型与运行时间。|机器学习、音视频数据格式与严格的对照实验。|software,robotics
medical-imaging|vision|计算成像与智慧医工|观测不完整或噪声较大时，怎样恢复更可信的图像？|逆问题、正则化、计算成像与不确定性分析。|linear,signal,image,probability,cognition|对公开非临床示例图像做模糊与重建，对比两种正则强度。|重建误差、细节损失、噪声敏感性；结果不用于诊断。|成像物理、优化、领域知识与数据伦理规范。|instruments,software
embodied|vision|多模态智能体与机器人|图像和其他传感器给出不同线索时，机器人怎样融合判断？|多模态感知、传感器融合、嵌入式实现和场景测试。|cognition,image,probability,program,robotproject|在离线数据中人为移除一种传感信息，比较融合前后结果。|任务成功率、延迟、缺失输入时的退化幅度。|机器人学、几何、控制、实时系统与传感器标定。|robotics
em-theory|rf|电磁理论与传播|材料和边界改变后，波的反射与传播会怎样变化？|场方程、边界条件、解析近似与数值计算。|field,complex,physics,waves,linear|计算不同介质界面的反射，比较入射角与材料参数影响。|反射、透射与能量守恒；说明理想模型忽略了什么。|电磁理论、数值方法、材料参数和建模验证。|connectivity,photonics
rf-circuits|rf|微波与射频电路|高频前端怎样同时满足带宽、噪声与线性度要求？|射频网络分析、匹配设计、器件模型与测量校准。|field,waves,commcircuit,rf,microwavedesign|仿真一个匹配网络，观察中心频率变化对反射的影响。|反射系数、工作带宽、容差敏感性。|射频器件、网络分析仪、版图与电磁联合仿真。|connectivity,chips
antenna-array|rf|天线与阵列|有限尺寸的天线怎样形成需要的覆盖与波束？|辐射建模、阵列综合、参数扫描与方向图测量。|field,antenna,waves,linear,fieldlab|用阵列因子模型改变阵元间距和加权，比较方向图。|主瓣宽度、副瓣、栅瓣；区分理想阵列与实际天线。|全波仿真、互耦、天线测试与制造容差。|connectivity,instruments
em-imaging|rf|电磁计算、测量与成像|怎样从有限的电磁测量反推物体或环境特征？|数值电磁、反问题、测量校准与成像算法。|field,linear,image,statsignal,fieldlab|用简单二维散射模型比较不同采样数量下的重建。|误差、分辨率、对噪声和模型偏差的敏感性。|数值求解、反问题、测量系统与实验设计。|instruments
photon-device|photonics|集成光电子器件|怎样在芯片上高效地产生、调制或探测光？|器件物理、光电耦合建模、参数扫描与测试。|solid,quantum,field,opto,optolab|给简化光探测器建立响应与噪声模型，改变带宽参数。|响应度、带宽、噪声；明确模型与真实器件的差距。|半导体物理、光波导、工艺与光电测试。|photonics,chips
nano-photonics|photonics|微纳光电材料与结构|结构缩小到微纳尺度后，光与材料怎样相互作用？|电磁仿真、材料模型、谱学与微纳结构分析。|quantum,solid,field,complex,opto|用简化谐振模型扫描几何参数对共振谱的影响。|共振位置、线宽、参数敏感性；说明采用的近似。|微纳光学、材料物理、数值电磁与加工知识。|photonics
optical-network|photonics|光通信系统与网络|怎样在更高容量下控制传输失真、误码与系统开销？|调制接收、数字均衡、光链路建模和网络分析。|opticalcomm,dsp,network,probability,opto|在简化带限链路中对比均衡前后的信号质量。|误码、带宽、处理开销与链路假设。|光纤通信、数字接收、光学实验与系统建模。|photonics,connectivity
microwave-photonics|photonics|微波光子学|能否利用光的传输与处理能力来处理宽带微波信号？|光电调制、延时与滤波、跨域链路分析。|waves,opto,signal,rf,opticalcomm|仿真多抽头延时滤波，观察延时对频率响应的影响。|频响、带宽、可调范围与器件误差影响。|微波与光学交叉基础、调制器、光电链路与实验测量。|photonics,connectivity
navigation|systems|导航与定位|卫星信号受限时，怎样融合多个观测估计位置？|参数估计、滤波、几何约束与多源融合。|probability,statsignal,linear,signal,program|生成带噪测距数据，用最小二乘定位并加入一个异常观测。|位置误差、异常敏感性、不同几何布局下的结果。|估计理论、GNSS/惯导基础、坐标系与标定。|robotics,instruments
radar-sensing|systems|探测、感知与雷达成像|杂波和噪声中，怎样判断目标存在并估计其状态？|检测估计、时频分析、成像与统计建模。|signal,dsp,statsignal,probability,field|对合成回波做距离分析，比较两个检测阈值。|检测率、虚警率与距离分辨能力；明确仿真范围。|雷达原理、阵列处理、测量与真实数据验证。|instruments,robotics
cooperative|systems|网络协同与多智能体|多台设备通信受限时，怎样协同定位或共享信息？|图模型、资源分配、分布式估计与协同感知。|algorithm,network,infonetwork,probability,robotproject|模拟多个节点共享有噪观测，逐步减少通信次数。|估计误差、通信量、掉线后的鲁棒性。|图优化、分布式系统、控制与协同决策基础。|robotics,connectivity
scientific-image|systems|显微图像与三维重建|多个有噪二维观测怎样支持三维结构恢复？|图像对齐、逆问题、统计估计与重建算法。|image,linear,statsignal,signal,probability|在合成投影数据上比较不同角度数量下的重建。|重建误差、缺失角度伪影与噪声敏感性。|成像物理、数值优化、三维几何与领域知识。|instruments,software'''
topics=[]
for line in text.splitlines():
 i,org,title,q,m,c,p,ev,g,ind=line.split('|')
 topics.append(dict(id=i,institute=org,title=title,question=q,methods=m,courses=c.split(','),project=p,evidence=ev,gap=g,industries=ind.split(','),source=org+'-research'))

sectors=[
 ('software','互联网、AI与软件系统','音视频、推荐检索、云与数据服务','火山引擎、阿里云等公开产品可作为业务入口。','audio,recommend,rtc','audio,recommend,rtc','把算法变成稳定、可迭代的服务，需要模型、数据、系统与客户端协作。'),
 ('chips','芯片与半导体设计','数字芯片、模拟混合信号与验证','NVIDIA岗位样本、TI模拟电路资源提供不同侧面的工作参照。','chip,analog','chip,analog','规格、架构、设计、验证、实现和测试互相衔接；芯片行业不只有一种“芯片工程师”。'),
 ('connectivity','通信与网络设备','无线联接、射频前端、网络传输','海思联接产品与实时音视频文档提供业务实例。','wifi,rtc','wireless,rtc','算法负责链路方法，硬件实现收发，协议和系统团队共同保证端到端性能。'),
 ('photonics','光电与光通信','光电器件、光模块、光传输设备','华为相干光通信技术文章提供系统层面的公开例子。','optics','optics','从光电器件到收发模块，再到传输系统，每一层面对的性能和制造约束不同。'),
 ('robotics','机器人与智能设备','感知定位、嵌入式、系统集成','大疆公开感知接口和英飞凌雷达应用展示传感数据如何进入智能设备。','robot,radar','robot,radar','感知、定位、控制和嵌入式实现共同工作；会训练一个模型不等于完成整机。'),
 ('instruments','传感、仪器与测量','信号采集、传感算法、测量系统','TI信号链资源与英飞凌雷达存在感知方案提供产品实例。','analog,radar','analog,radar','从读出微弱信号到建立可信测量，既需要硬件和算法，也需要校准与验证。')]
sectors=[dict(id=i,name=n,business=b,companies=c,cases=ca.split(','),sources=s.split(','),chain=ch) for i,n,b,c,ca,s,ch in sectors]

rolesText='''audio-algorithm|software|音频 / 视觉算法|把观测变成可理解的信息|建立基线、准备数据、优化算法并检查噪声和场景变化下的效果。|可复现实验、效果与延迟报告、可调用的推理模块。|signal,probability,dsp,speech,image,cognition|Python/C++、机器学习、数据处理、音视频评估。|audio|为降噪方法做统一测试集、基线和失败样例分析。|speech-vision,multimodal
recommend-engineer|software|推荐 / 搜索算法|把数据变成可评估的排序|处理特征、搭建召回与排序、分析冷启动，并检查离线与实际效果差异。|数据切分说明、检索排序基线、指标与偏差分析。|algorithm,probability,linear,cognition,program|机器学习、优化、数据库、实验设计与工程实现。|recommend|做一个公开评分数据上的检索推荐基线，并按时间验证。|multimodal,network-resource
software-system|software|后端 / 音视频系统|让方法持续、稳定地运行|设计接口与数据流，处理并发、资源占用、日志和性能问题。|可运行服务、接口文档、性能测试与故障定位记录。|program,algorithm,os,network,infonetwork|Linux、数据库、并发、网络协议、版本管理与测试。|rtc,recommend|为一个媒体或检索演示加入日志、错误处理与负载测试。|network-resource,efficient-compute
rtl-design|chips|数字IC / RTL设计|把规格写成硬件逻辑|拆分模块、设计状态机和数据通路，检查接口与时序约束。|RTL、模块说明、仿真与资源/时序结果。|digital,digitalsystem,architecture,ic,program|Verilog/SystemVerilog、综合、静态时序和接口协议。|chip|设计带背压接口的FIFO，说明复位与满空边界。|efficient-compute,comm-soc
verification|chips|芯片验证|用证据说明设计符合规格|制定测试计划、构造边界场景、建立测试平台并分析覆盖与失败。|可重复测试、波形、错误报告和覆盖记录。|digital,program,algorithm,architecture,digitallab|SystemVerilog、验证方法、脚本与调试；工具要求随团队变化。|chip|给FIFO主动注入错误，再用自动化测试捕获并定位。|eda,comm-soc
analog-design|chips|模拟 / 混合信号电路|在物理约束中获得电路性能|分析噪声、增益、带宽和稳定性，进行仿真、容差分析与测试。|电路设计、仿真扫描、误差预算与测量对照。|circuit,analogcourse,solid,signal,ic|器件物理、SPICE、版图寄生、PVT分析与仪器操作。|analog|为一个前端方案比较带宽、噪声与功耗的取舍。|mixed,photon-device
baseband|connectivity|通信 / 基带算法|让接收机恢复正确的信息|建立链路模型，开发同步、检测、均衡或编码模块，并分析复杂度。|链路仿真、误码曲线、算法说明与实现基线。|signal,probability,network,commsignal,coding|数字通信、具体标准、C/C++、定点实现与系统实验。|wifi|对一个多径链路写清假设并比较两个接收方案。|wireless-link,coding-detection
rf-engineer|connectivity|射频 / 天线研发|让收发信号走出电路板|做匹配、天线或射频链路设计，分析布局、环境和器件偏差。|仿真模型、方向图/网络参数、测试与校准记录。|field,antenna,rf,waves,microwavedesign|全波仿真、射频测量、版图与系统指标分解。|wifi,radar|比较天线模型在不同边界条件下的性能变化。|antenna-array,rf-circuits
protocol-test|connectivity|协议 / 网络系统与测试|保证端到端链路可用|分析网络协议和日志，设计拥塞、丢包与互操作场景并定位瓶颈。|测试计划、抓包分析、吞吐与尾延迟报告。|network,infonetwork,os,program,probability|协议栈、网络工具、自动化测试与性能分析。|rtc,wifi|给一个传输演示加上丢包与带宽变化，追踪卡顿原因。|network-resource,cooperative
opto-device|photonics|光电器件研发|理解并优化光电转换|建模器件响应，分析材料和结构参数，设计测量与性能对比。|器件模型、响应曲线、参数扫描与实验说明。|solid,quantum,field,opto,optolab|半导体与光学、数值仿真、工艺与测量知识。|optics|比较两种简化探测器参数下的响应和噪声。|photon-device,nano-photonics
optical-dsp|photonics|光通信算法 / 系统|补偿链路失真并评估传输性能|建立传输与接收模型，评估均衡和调制方案，比较处理代价。|链路模型、误码与开销报告、可复现接收算法。|opticalcomm,dsp,signal,probability,network|光纤通信、相干接收、数字通信与实验分析。|optics|给带宽受限的链路加入均衡，并说明收益与代价。|optical-network,microwave-photonics
optical-test|photonics|光模块 / 系统测试|证明产品在规定条件下工作|分解指标、组织测试、记录温度与接口条件，分析一致性问题。|自动化测试、链路预算、误差与异常定位记录。|opto,optolab,opticalcomm,physicslab,program|光学仪器、自动化、接口与可靠性测试基础。|optics|做一份光链路测试矩阵，列出条件、指标与判定方式。|optical-network,photon-device
perception|robotics|视觉感知 / 定位融合|从不完美观测估计环境和位置|处理图像和多源数据，进行标定、对齐、跟踪与误差分析。|算法基线、标定文件、轨迹误差与失败场景报告。|image,probability,linear,statsignal,cognition|几何、机器人学、C++、优化与传感器标定。|robot|在离线数据中比较单传感器与融合估计。|navigation,embodied
embedded|robotics|嵌入式 / 固件开发|让算法与传感器实时协作|组织采集、通信和任务调度，处理接口、内存与异常。|固件、接口说明、时序与资源测试。|program,digital,os,dspsystem,build|C/C++、MCU、RTOS、总线协议与硬件调试。|robot,radar|实现带时间戳的采集与处理流水线，测试丢帧和超时。|comm-soc,smart-sensor
integration|robotics|机器人系统集成 / 测试|把各模块变成可靠的整机功能|明确模块接口，复现实地问题，分析定位、感知与执行之间的影响。|接口与场景测试、误差定位、回归报告。|robotproject,program,network,probability,build|控制与机器人基础、日志分析、测试工程和跨团队协作。|robot|用仿真或录制数据建立一个可重复的系统失败场景。|embodied,cooperative
sensor-front|instruments|传感器 / 采集硬件|准确读出微弱信号|设计放大与滤波，选择采样与接口方案，分析噪声和饱和。|原理图、信号链预算、频响与噪声测量。|circuit,analogcourse,signal,circuitlab,physicslab|器件手册、SPICE、PCB与仪器测量。|analog|为一个传感器等效输入设计采集前端并扫描输入范围。|mixed,smart-sensor
sensor-algorithm|instruments|雷达 / 传感算法|从回波和时间序列中检测变化|处理回波、估计特征、设置阈值并分析误报漏报。|信号处理流程、检测曲线、场景分层结果。|signal,dsp,statsignal,probability,field|雷达或传感原理、统计评估、嵌入式实现与真实数据。|radar|在合成数据中扫描阈值并报告检测率和虚警率。|radar-sensing,em-imaging
application|instruments|应用 / 测试工程|把器件能力转成可用方案|理解用户场景、搭建参考方案、排查接口和测量误差，形成技术说明。|演示系统、应用说明、测试记录与问题复现步骤。|build,circuitlab,program,signal,physicslab|器件选型、仪器操作、技术表达、实验设计与调试。|analog,radar|为一个传感方案写出接线、参数、复现步骤和失败边界。|smart-sensor,em-imaging'''
roles=[]
for line in rolesText.splitlines():
 i,sector,n,p,t,o,c,g,ca,project,ts=line.split('|')
 roles.append(dict(id=i,sector=sector,name=n,purpose=p,tasks=t,output=o,courses=c.split(','),gap=g,cases=ca.split(','),project=project,topics=ts.split(',')))
teachers=[
 dict(id='wangyu',name='汪玉',window='circuits',areas='智能芯片、高能效电路与系统',topics=['efficient-compute'],email='yu-wang@mail.tsinghua.edu.cn',url='https://collegeai.tsinghua.edu.cn/rydw.htm',sourceTitle='清华人工智能学院 · 兼聘PI公开介绍',extra='https://www.ee.tsinghua.edu.cn/info/1076/3899.htm'),
 dict(id='dailinglong',name='戴凌龙',window='wireless',areas='无线通信传输、大规模MIMO、智能超表面',topics=['wireless-link','coding-detection'],email='daill@tsinghua.edu.cn',url='https://oa.ee.tsinghua.edu.cn/dailinglong/',sourceTitle='教师个人主页'),
 dict(id='fanglu',name='方璐',window='vision',areas='计算成像、视觉智能与光电计算',topics=['medical-imaging'],email='fanglu@tsinghua.edu.cn',url='https://web.ee.tsinghua.edu.cn/fanglu/zh_CN/zhym/2610/list/index.htm',sourceTitle='教师主页 · 公开邮箱',extra='https://www.ee.tsinghua.edu.cn/info/1051/1297.htm'),
 dict(id='yangfan',name='杨帆',window='rf',areas='天线理论与测量、电磁材料、数值电磁',topics=['antenna-array','em-theory','em-imaging'],email='',url='https://web.ee.tsinghua.edu.cn/yangfan/zh_CN/index.htm',sourceTitle='教师个人主页'),
 dict(id='huangyidong',name='黄翊东',window='photonics',areas='微纳光电子器件与系统、智能感知',topics=['photon-device','nano-photonics'],email='yidonghuang@tsinghua.edu.cn',url='https://nano-oelab.ee.tsinghua.edu.cn/Home/jsxx/jsxx_1.html?id=49&lang=zh',sourceTitle='微纳光子学实验室 · 教师介绍',extra='https://web.ee.tsinghua.edu.cn/huangyidong/zh_CN/zsxx/1789/content/1163.htm'),
 dict(id='shenyuan',name='沈渊',window='systems',areas='网络定位与导航、多智能体、统计推断与成像',topics=['navigation','cooperative','scientific-image'],email='shenyuan_ee@tsinghua.edu.cn',url='https://oa.ee.tsinghua.edu.cn/~shenyuan/index.html',sourceTitle='教师个人主页')
]
data=dict(updated='2026-10-01',institutes=institutes,topics=topics,sectors=sectors,roles=roles,teachers=teachers,
 boundary='研究所名称及方向依据官网；问题、方法、指标、学习路线和岗位拆解为编辑解释。机构间主题交叉，企业也会开展科研；两条入口按探索目标区分，不代表互斥的人生道路。')
base=json.loads((P/'catalog.json').read_text(encoding='utf-8'))
cids={c['id'] for c in base['courses']};sids={s['id'] for s in base['sources']};tids={t['id'] for t in topics};caseids={c['id'] for c in base['cases']}
for item in topics+roles: assert set(item['courses'])<=cids,item['id']
for r in roles: assert set(r['topics'])<=tids and set(r['cases'])<=caseids,r['id']
for x in institutes: assert x['source'] in sids
for t in teachers: assert set(t['topics'])<=tids
orgids={x['id'] for x in institutes};sectorids={x['id'] for x in sectors}
for t in topics: assert t['institute'] in orgids and set(t['industries'])<=sectorids
for s in sectors: assert set(s['sources'])<=sids and set(s['cases'])<=caseids
for r in roles: assert r['sector'] in sectorids
for t in teachers: assert t['window'] in orgids and t['url'].startswith('https://')
for collection in [topics,roles,institutes,sectors,teachers]: assert len({x['id'] for x in collection})==len(collection)
assert len([c for c in base['courses'] if c['group']=='core'])==10
assert len(topics)==24 and len(roles)==18
(P/'destinations.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(P/'destinations-data.js').write_text('window.DESTINATIONS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f'{len(institutes)} institutes / {len(topics)} topics / {len(sectors)} sectors / {len(roles)} roles')
