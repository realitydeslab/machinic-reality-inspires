# Machinic Reality Inspire — 作品目录

反思 AI 与机器的代表性艺术作品、机器人艺术、表演、思辨设计与研究目录，以机器现象学为线索：机器感知、机器身体、机器的内在、亲密与照护、记忆与数字来世、劳动与基础设施、分类与权力。只用 AI 生成图像的作品不收录。由 Reality Design Lab 整理，作为艺术家、设计师和研究者的灵感库。每件作品都列出核心想法、实现方式，以及论文、视频和图片链接。

https://machinic.reality.design · 2026-09-28 · 601 位创作者 · 802 件作品

## AI 助手应如何使用这个文件

- 提出想法时，以下面的具体作品为依据，并说明借鉴的是哪件作品、哪位创作者。
- 引用论文时使用这里给出的 DOI 或链接，不要编造参考文献。
- 把不同作品的机器、方法和领域组合起来，提出新的方向。
- 不要编造这里没有写到的细节，以链接为准。

## 机器感知

机器如何看、听和给世界分类，以及被机器看见、听见和贴上标签是什么感受。

### 机器之眼与操作图像

计算机视觉、由机器生成并供机器读取的图像、机器眼中的世界。

#### 非事实解剖 第一章：AI 超真实主义（Anatomy of Non-Fact. Chapter 1: AI Hyperrealism） — Martyna Marciniak (2024)
- 类型: 电影与影像 · 机器: 生成模型与潜空间
- 核心想法: 当照片变成训练数据，一张合成图像迫使我们追问：视觉证据究竟还是什么。
- 作品内容: 一段 18 分钟的影像：一位演员扮演病毒式传播的 AI 生成“巴黎世家教皇”，发表关于事实与伪造的独白，同时拆解图像生成、新闻图像语言与数字克隆的机制。
- 实现方式: 把关于骗局的法证与历史研究，以滑稽剧、服装、手部道具和 AI 生成素材编排成一部单频影像。
- 视角: 不透明与潜空间, 机器之眼
- 展出与获奖: Ars Electronica Festival 2024; Prix Ars Electronica 2025, Award of Distinction (Artificial Life & Intelligence)
- 图片: https://archive.aec.at/asset/3844471/preview/ https://archive.aec.at/asset/3844472/preview/ https://cdn.prod.website-files.com/63f9efede196cc0cf7cd41e6/66faa9495e2b8520ac801f38_IMG_7524.JPEG
- 项目主页: https://www.martyna.digital/projects/anatomy-of-non-fact-chapter-1

#### 身体神谕（Body Oracle） — Ke Huang, Botao Amber Hu (2024)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 一台把身体写成文字的机器，让你留意自己如何面对他人摆放身体。
- 作品内容: 摄像头读取单人或多人的姿势，把它变成一个仿甲骨文风格的新象形字，让一个姿态成为可以回看、模仿和讨论的“字”。
- 实现方式: MoveNet 识别人体关键点；用志愿者重演甲骨文字形得到的配对数据训练 pix2pix 模型，把骨架映射为字形，再用神经风格迁移渲染（合作者 Danlin Huang、Cun Lin）。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: China National Art Exhibition 2024, Chongqing; CVPR 2025 AI Art Gallery, Nashville; IJCAI 2025 Art Gallery, Montréal; SIGGRAPH Asia 2025 XR, Hong Kong
- 论文: https://doi.org/10.1145/3689050.3707688 (TEI 2025)
- 视频: https://vimeo.com/1020163664
- 图片: https://reality.design/media/_resources/Body%20Oracle/project-body-oracle-figure-01.jpg
- 项目主页: https://reality.design/project/body-oracle

#### Paragraphica — Bjørn Karmann (2023)
- 类型: 思辨设计 · 机器: 生成模型与潜空间, 计算机视觉
- 核心想法: 相机可以不靠光来感知；它的照片显示的，是机器如何从数据想象一个地方，而不是那里真正有什么。
- 作品内容: 一台没有镜头的相机：它通过数据（地址、天气、时间、附近地点）来“读取”你所在的地方，写成一段文字，再用文生图模型把这段文字变成一张“照片”。
- 实现方式: 带触摸屏的树莓派调用开放的位置与天气接口，组成文字提示后交给 Stable Diffusion；三个旋钮分别控制数据半径、噪声种子与引导强度，取景器造型参考了星鼻鼹。
- 视角: 机器之眼, 机器环世界, 不透明与潜空间
- 视频: https://bjoernkarmann.dk/wp-content/uploads/2023/05/paragraphica_30s.mp4
- 图片: https://bjoernkarmann.dk/wp-content/uploads/2023/05/camera_below.png
- 项目主页: https://bjoernkarmann.dk/paragraphica

#### 关注者（The Follower） — Dries Depoorter (2022)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉, 平台与推荐算法
- 核心想法: 每张摆拍照片都有另一张由机器拍下的、不设防的图像，而 AI 能把两者连起来。
- 作品内容: Depoorter 连续数周录制公共广场的开放网络摄像头，抓取在这些地点标记的 Instagram 照片，再用 AI 找出每张照片被拍下的确切瞬间：并排的片段一边是摆拍的网红，一边是无人注意的监视画面。
- 实现方式: 用图像相似度与人物检测软件，把公开网络摄像头数周的录像与抓取来的带地点标签的 Instagram 帖子逐一比对。
- 视角: 机器之眼, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=mkqT32CEIk8
- 图片: https://driesdepoorter.be/wp-content/uploads/2022/08/The-Follower-Dries-Depoorter-small.jpg
- 项目主页: https://driesdepoorter.be/thefollower/

#### 风的验证（Wind Verification） — 郭城 (2021)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 平台与推荐算法
- 核心想法: 只能通过图像“看见”风的机器，试图在现实中把风重建出来：数字现实成了现实的参照。
- 作品内容: 计算机视觉模型观看中国社交平台上带旗帜的短视频，并驱动气泵，让展厅里的真旗帜以相同方式飘动，重现视频中的风。
- 实现方式: 深度学习视觉算法分析从抖音、快手收集的旗帜摆动，把控制数据发送给旗帜后的气泵。
- 视角: 机器之眼, 机器环世界
- 图片: https://cdn.guo-cheng.net/files/projectImg/WindVerification/WV_ocat_7.jpg https://cdn.guo-cheng.net/files/projectImg/WindVerification/WV_ocat_1.jpg
- 项目主页: https://guo-cheng.net/index.php/projects/wind-verification/

#### 机器人所见（What the Robot Saw） — Amy Alexander (2020)
- 类型: 电影与影像 · 机器: 平台与推荐算法, 计算机视觉
- 核心想法: 平台上被遗忘的视频，只能通过机器的人口统计式凝视才被看见。
- 作品内容: 一部永不结束的直播电影，由“机器人”从最近几小时内观看最少的 YouTube 视频中剪辑而成，并用商业人脸分析服务给出的年龄、性别、情绪标签来命名与分组。
- 实现方式: 软件在 YouTube 搜索低播放量视频，用 Amazon Rekognition 等视觉模型分析，剪成连续影片在 Twitch 直播。
- 视角: 分类、偏见与监控, 机器之眼
- 图片: https://what-the-robot-saw.com/dir/wp-content/uploads/2026/06/Screen-Shot-2020-02-07-at-10.40.07-PM-1.png
- 项目主页: https://what-the-robot-saw.com

#### 膜（Membrane） — Ursula Damm (2019)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 会看的机器并不记录街道；它记住特征，再把它们重组为属于自己的街道。
- 作品内容: 一台固定摄像机注视着柏林的一条街道，神经网络学习其中的模式，并由此生成新的影像序列。观众通过界面引导网络重新组合哪些已学到的特征，看着分析如何变成虚构。
- 实现方式: 街头摄像机的实时影像用于训练时序生成对抗网络（TGAN，并加入小波扩展）来生成新序列；观众通过界面选择图像特征。
- 视角: 机器之眼, 不透明与潜空间, 能动、自主与共创
- 展出与获奖: Kunstverein Tiergarten, Berlin, 2019; Entangled Realities, HEK Basel, 2019
- 视频: https://vimeo.com/393106068
- 图片: https://ursuladamm.de/api/media/file/Bild06-scaled.jpg https://ursuladamm.de/api/media/file/dunkel3-1536x1116.jpg
- 项目主页: https://ursuladamm.de/membrane-2019

#### 重新编码艺术（Recoding Art） — Bruno Moreschi, Gabriel Pereira (2019)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 机器对艺术的误读，同时暴露了机器的分类与美术馆的权威。
- 作品内容: 让商业计算机视觉服务“阅读”Van Abbemuseum 的藏品；它们直白而平庸的标签（“家具”“人”“艺术”）与作品并置，并与美术馆的专业描述对照。
- 实现方式: 用商业视觉 API 处理馆藏作品图像，把输出结果展示为另一份目录。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 论文: https://doi.org/10.1007/s00146-020-01059-y (AI & Society 2021)
- 项目主页: https://brunomoreschi.com/Recoding-Art-Van-Abbemuseum-collection

#### 超级视力（TransVision） — 李佳宝, Honghao Deng (2018)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 义体与赛博格
- 核心想法: 把媒体滤镜推到极端并戴在身上，你才感到自己的“看”早已被中介。
- 作品内容: 三件可穿戴的“感知机器”放大了数字媒体对视觉的过滤：头盔让佩戴者对红色“过敏”，红色会扩张或收缩；会呼吸的硅胶面罩用触觉取代视觉；头显让你靠看广告赚钱，或付钱看一个没有广告的世界。
- 实现方式: 头戴摄像头和显示器实时处理眼前画面（颜色遮罩、把光转换为呼吸节奏、叠加广告）；与邓鸿浩和 Panagiotis Michalatos 在哈佛设计研究生院合作开发。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: SIGGRAPH 2019 Art Gallery, Los Angeles; CHI 2019, Glasgow; S+T+ARTS Prize Honorary Mention; ISWC 2018 Design Award
- 论文: https://doi.org/10.1145/3267242.3267293 (ISWC 2018)
- 视频: https://www.youtube.com/watch?v=xHWTLGjHsyc
- 图片: https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/05a54608-e457-4d43-a7ca-82ff78294298/Jiabao+Li+TransVision.jpg
- 项目主页: https://www.jiabaoli.org/transvision

#### 看这辉煌的时代！（Behold These Glorious Times!） — Trevor Paglen (2017)
- 类型: 电影与影像 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 我们很少看到网络“看见”的东西；这里，用来教机器的图像和机器对它们的拆解出现在同一块屏幕上。
- 作品内容: 一部 10 分钟的录像：交替呈现用来教 AI 识别物体、人脸与情绪的训练图像，以及深度神经网络从中提取的特征网格，配乐由 Holly Herndon 创作。
- 实现方式: 把训练库中的图像输入卷积网络并可视化其中间激活；配乐部分使用了神经网络语音合成与语音识别训练数据。
- 视角: 机器之眼, 不透明与潜空间
- 图片: https://paglen.studio/wp-content/uploads/2020/05/Paglen-Behold_2017.jpg https://paglen.studio/wp-content/uploads/2020/06/Paglen-Behold_detail.jpg
- 项目主页: https://paglen.studio/2020/04/09/behold-these-glorious-times/

#### 眨眼：人性化自主（Blink: Humanising Autonomy） — Humanising Autonomy (Maya Pindeus, Leslie Nooteboom, Raunaq Bose, Adam Bernstein) (2017)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 自动驾驶汽车可以展示它看到了什么、并开口询问，而不是默默决定谁挡了路。
- 作品内容: 自动驾驶汽车四角的灯板显示它检测到的行人轮廓；当行人的意图不明时，轮廓闪烁并发出提示音询问，行人用手势回答，轮廓随之变红或变绿。
- 实现方式: 行人检测结果显示在车身的轮廓屏上；一个以不同文化手势数据训练的监督学习模型读取行人的回应。
- 视角: 机器之眼, 能动、自主与共创
- 展出与获奖: S+T+ARTS Prize 2017, Honorary Mention
- 视频: https://www.youtube.com/watch?v=B7J8aOFQo70
- 图片: https://ars.electronica.art/starts-prize/files/2017/05/humanisingautonomy.jpg
- 项目主页: https://ars.electronica.art/starts-prize/en/blink-humanising-autonomy/

#### 计算策展（Computed Curation） — Philipp Schmitt (2017)
- 类型: 艺术作品与装置 · 机器: 计算机视觉
- 核心想法: 让机器来编辑摄影书，读者便学会用算法的眼睛看世界，也看见它的盲点。
- 作品内容: 一本长达 29 米的折页摄影书，照片顺序完全由计算机决定：视觉算法按内容与构图为艺术家的照片打标签、写说明并排序。那些古怪的说明与关联，引导读者去揣测机器的逻辑。
- 实现方式: 图像识别服务生成标签与说明，排版算法按视觉与语义相似度把照片串联起来；以折页书和网页版呈现。
- 视角: 机器之眼, 失败、故障与错误, 能动、自主与共创
- 展出与获奖: DAAD Art Show, German Consulate New York, 2018
- 视频: https://vimeo.com/225081193
- 图片: https://cdn.philippschmitt.com/media/pages/work/computed-curation/2cadd14424-1586887798/philipp-schmitt_computed-curation-2-1200x630-crop.jpg
- 项目主页: https://philippschmitt.com/work/computed-curation

#### 蜻蜓之眼（Dragonfly Eyes） — 徐冰 (2017)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 当日常生活早已被机器拍下，叙事可以从机器的凝视中拼接出来，而画面中的人从未同意成为角色。
- 作品内容: 一部没有摄影师、没有演员的 81 分钟长片：一个爱情故事，完全由网上找到的上万小时中国监控与直播录像剪辑而成。
- 实现方式: 团队多年收集公开的监控与直播片段，再根据素材反复改写剧本，并为画面配音。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Locarno Film Festival 2017; Toronto International Film Festival 2017
- 视频: https://www.youtube.com/watch?v=-ccfz77ifeU
- 图片: https://www.xubing.com/Uploads/Source/Image/20221025/20221025164745_4227.jpg https://www.xubing.com/Uploads/Source/Image/20221025/20221025164831_2975.jpg
- 项目主页: https://www.xubing.com/en/work/details/469?classID=8&type=class

#### 学会看见（Learning to See） — Memo Akten (2017)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 神经网络只能透过它已知的东西去看，人也一样。
- 作品内容: 摄像头对着桌上的日常物件（电线、钥匙、布料），只在海浪、火焰、云或花上训练过的神经网络实时把它们重绘成海景和天空。
- 实现方式: 在单一主题数据集上训练的定制图像到图像网络（类似 pix2pix）重建桌面的实时摄像画面，形式包括互动装置与系列录像。
- 视角: 机器之眼, 不透明与潜空间
- 展出与获奖: AI: More than Human, Barbican, London, 2019; Understanding AI, Ars Electronica Center, Linz
- 视频: https://www.youtube.com/watch?v=DE3402nH1wA
- 图片: https://media.superradiance.net/cdn-cgi/image/width=1200,fit=scale-down,format=auto,onerror=redirect/memotv/projects/2017/learning-to-see/images/learning-to-see.jpg
- 项目主页: https://www.memo.tv/works/learning-to-see/

#### 视觉机器（Sight Machine） — Trevor Paglen (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉
- 核心想法: 一场被机器观看的音乐会表明：在机器对人的描述里，音乐、姿态与情感几乎荡然无存。
- 作品内容: Kronos Quartet 现场演奏，摄像头把画面输入一组计算机视觉算法，机器在乐手身上“看到”的内容实时投影在他们身后。
- 实现方式: 现场摄像画面经过人脸检测、物体识别、姿态估计等视觉算法处理，结果在演出中实时渲染并投影。
- 视角: 机器之眼, 失败、故障与错误
- 展出与获奖: Pier 70, San Francisco, 2017; Holland Festival, Amsterdam, 2018; Smithsonian American Art Museum, 2018; Barbican, London, 2019
- 视频: https://www.youtube.com/watch?v=5mg3MXETfj4
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-Site_Machine-2017.jpg
- 项目主页: https://paglen.studio/2019/07/01/sight-machine/

#### VFRAME — Adam Harvey (2017)
- 类型: 研究原型 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 只要有人为它建好数据集，机器视觉就可以从监视者的工具变成见证者的工具。
- 作品内容: 一套为人权研究者开发的计算机视觉工具，在海量冲突地区视频档案中搜寻特定弹药，例如 9N235 集束子弹药。
- 实现方式: 用摄影测量、三维渲染和三维打印复制品生成弹药的合成图像来训练目标检测器，再在 Syrian Archive 等档案上运行。
- 视角: 机器之眼, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=dZgDMvaLLPQ
- 图片: https://adam.harvey.studio/vframe/9n235_t4t_02_0306.jpg https://adam.harvey.studio/vframe/vframe_9n235_benchmark_montage.jpg
- 项目主页: https://vframe.io
- 代码: https://github.com/vframeio

#### 物化器（Objectifier） — Bjørn Karmann (2016)
- 类型: 研究原型 · 机器: 计算机视觉
- 核心想法: 通过示例教机器“看”，让它的感知与误解都成为日常家居中的游戏。
- 作品内容: 一个带摄像头的插座装置，靠示范来训练：对它做几次手势或布置某个场景，它就学会何时打开台灯或收音机，让用户从消费者变成一个小型 AI 的训练者。
- 实现方式: 摄像头把画面送入嵌入式计算机上的神经网络分类器，由它控制电源插座；配套应用让用户录入正例与反例。
- 视角: 机器之眼, 能动、自主与共创
- 展出与获奖: Copenhagen Institute of Interaction Design (CIID) final project, 2016
- 视频: https://www.youtube.com/watch?v=3a825NJMLjk
- 图片: https://bjoernkarmann.dk/wp-content/uploads/2022/11/objectifier_apprentice_bjorn_karmann_2016.jpg https://bjoernkarmann.dk/wp-content/uploads/2023/03/Objectifier.jpg
- 项目主页: https://bjoernkarmann.dk/objectifier

#### 重塑世界的词语：寻觅者（Words That Remake the World «The Seeker»） — Nye Thompson (2016)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 当机器通过监控摄像头描述世界时，它们开始写下一套由机器生成、也为机器服务的世界词汇。
- 作品内容: AI 实体 The Seeker 通过数以百万计的不设防监控摄像头观看世界，并为所见之物命名；这些描述变成一幅巨大的绘图，以及会低语的机器人化身 CKRBT（2019）。
- 实现方式: 定制软件从未加密的网络摄像头抓取画面并发送到云端图像识别服务，标签与置信度被记录、绘制成图，并由合成语音说出。
- 视角: 机器之眼, 机器环世界, 分类、偏见与监控
- 展出与获奖: Victoria and Albert Museum, London
- 视频: https://www.youtube.com/watch?v=xv_kITdeCMQ
- 图片: https://nyethompson.net/images/WTRTW-2025-thumb.png
- 项目主页: https://nyethompson.net/works/the-seeker.html

#### 穷尽人群（Exhausting a Crowd） — Kyle McDonald (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 当人们开始给监控画面打标签，它就变成了数据集；是人群在替机器观看。
- 作品内容: 在高处拍下的皮卡迪利广场十二小时影像被做成网站，任何人都可以暂停、放大，并给人群中任意一个人加注释。作品取自 Georges Perec《穷尽巴黎某地的尝试》，呈现“众包标注式监控”的样子。
- 实现方式: 4K 摄像机从皮卡迪利广场一栋建筑上连续拍摄下午 3 点至凌晨 3 点；定制网页播放器保存线上访客带时间码和位置的标注。与 Jonas Jongejan 合作。
- 视角: 机器之眼, 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: All of This Belongs to You, V&A London 2015; IDFA DocLab 2015
- 视频: https://www.youtube.com/watch?v=XCEX-B59Sx8
- 图片: https://exhaustingacrowd.com/og_image.jpg
- 项目主页: https://www.exhaustingacrowd.com/
- 代码: https://github.com/kylemcdonald/ExhaustingACrowd

#### 假阳性（False Positives） — Esther Hovers (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 行为检测让日常动作变得可疑；所谓“正常”，就是按算法预期的方式移动。
- 作品内容: 从监控摄像头的高视角拍摄布鲁塞尔商务区，每幅作品演绎智能监控系统被训练去标记的八种“异常”之一，例如静止不动或反复回头。
- 实现方式: 每个场景由多张照片数字合成，依据与监控专家一起归纳的八种异常（静止、快速移动、孤立物品、停在角落、人群散开、同步动作、反复回头、逆向行走）。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Scotiabank CONTACT Photography Festival, Toronto, 2019; Resistant Faces, Pinakothek der Moderne, Munich, 2021
- 图片: https://freight.cargo.site/w/1000/i/O2310842155385471171937562539865/EstherHovers-FalsePositives-08.jpg
- 项目主页: https://www.estherhovers.com/false-positives-1

#### 乱穿马路（Jaywalking） — Dries Depoorter (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 自动检测让举报变得毫不费力，也把机器判断的道德重量交到观众手里。
- 作品内容: 观众观看全球各地的实时交通摄像头，软件会标出闯红灯过马路的行人；只需按一个按钮，就能把违规截图发送到最近的警察局。
- 实现方式: 分析公开交通摄像头的直播画面，找出红灯时位于人行横道上的行人；按下按钮即可把截取的画面通过电子邮件发送给当地警方。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Mirage Festival, Lyon 2019
- 视频: https://www.youtube.com/watch?v=Lxei5Svo0Pg
- 图片: https://driesdepoorter.be/wp-content/uploads/2019/01/Mirage-2019-Marion_Bornaz.116.jpg
- 项目主页: https://driesdepoorter.be/jaywalking/

#### 生活模式（Patterns of Life） — 朱利安·普雷维厄 (2015)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 可被机器读取的动作有其历史：每一种追踪系统都先教会身体如何被测量。
- 作品内容: 五位巴黎歌剧院舞者表演源自科学实验规程的编舞，这些规程把人类动作变成数据：从马雷的连续摄影、吉尔布雷斯的动作研究，到光点显示与今天的追踪软件。片名来自军方用语，指从监控数据中分析目标的生活规律。
- 实现方式: 影片在六个场景中拍摄，舞者重演历史与当代的动作捕捉和追踪实验；由巴黎歌剧院 3e Scène 联合制作，用于普雷维厄在蓬皮杜中心的个展。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: Prix Marcel Duchamp 2014 exhibition, Centre Pompidou, Paris 2015–16
- 视频: https://www.youtube.com/watch?v=c45IfGRkJ_w
- 项目主页: https://www.youtube.com/watch?v=c45IfGRkJ_w

#### 看电影的计算机（Computers Watching Movies） — Benjamin Grosser (2013)
- 类型: 电影与影像 · 机器: 计算机视觉
- 核心想法: 没有人类叙事习惯的机器会看向不同的地方，这反过来暴露了人类的观看有多么受文化训练。
- 作品内容: 一个计算机视觉系统观看六部名片的片段（《2001 太空漫游》《美国丽人》《盗梦空间》《出租车司机》《黑客帝国》《安妮·霍尔》），它的视线以移动的线条画在黑底上，并与原片音轨同步。
- 实现方式: 艺术家编写的软件用计算机视觉与 AI 程序决定每一帧看向哪里，轨迹被渲染成随时间展开的素描（计算生成的高清录像）。
- 视角: 机器之眼, 机器环世界
- 展出与获奖: VIDA 16.0, first prize, 2014
- 视频: https://vimeo.com/78711521
- 图片: http://bengrosser.com/wp-content/themes/grosser/images/cwm-fb-og-1200x674.png https://bengrosser.com/wp-content/resources/cwm-ludwig-museum-530x345.jpg
- 项目主页: https://bengrosser.com/projects/computers-watching-movies/

#### 云脸（Cloud Face） — Shinseungback Kimyonghun (2012)
- 类型: 艺术作品与装置 · 机器: 计算机视觉
- 核心想法: 识别错误揭示出：机器和人一样会在没有脸的地方“看到”脸，只是它并不想象。
- 作品内容: 把摄像机对准天空，用人脸检测算法收集被机器识别为“人脸”的云朵。印出的图像让机器的空想性错视与人类在云中看脸的习惯并置。
- 实现方式: 摄像机、人脸检测算法与自制软件筛选云的图像，以艺术微喷与录像展出。
- 视角: 机器之眼, 失败、故障与错误
- 展出与获奖: Ars Electronica Center, Linz 2014–2021
- 视频: https://vimeo.com/68958093
- 图片: https://djhznh41oxwef.cloudfront.net/works/cloud_face/resized/ssbkyh_detail1.png
- 项目主页: https://ssbkyh.com/works/cloud_face/

#### AZ：一动就被拍下（AZ: Move and Get Shot） — Joana Moll (2011)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 把监视交给动作传感器，监视的意图就被掏空了：机器看见一切移动之物，却什么也不理解。
- 作品内容: 一个机器人程序从亚利桑那州土地主架设在美墨边境的动作触发监控摄像头中收集图像，自动剪成六部影片。这些摄像头本为公开偷渡者的影像，却对任何动静都会拍摄，于是档案里满是动物、风和光，也有人。
- 实现方式: 2011 至 2014 年间，一个机器人程序每 24 小时检查土地主的网站，把六台摄像头新上传的画面存到本地服务器，并按算法接进六部持续生长的影片。
- 视角: 机器之眼, 分类、偏见与监控, 机器环世界
- 图片: http://www.janavirgin.com/img/works/AZ_MOVE.jpg http://www.janavirgin.com/img/works/az_move_22.jpg
- 项目主页: http://www.janavirgin.com/azmove.html

#### 代码的欲望（Desire of Codes） — 三上晴子 (2010)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 工业机械臂, 监控与生物识别
- 核心想法: 被似乎“有所欲求”的机器注视，让监控变成与另一种物种的相遇。
- 作品内容: 一面由 90 个小型感应单元组成的墙像昆虫一样转向观众，六条悬挂的带摄像头和投影仪的机械臂追踪他们，一块复眼屏幕把他们的影像与其他监控画面混在一起。
- 实现方式: 红外与摄像追踪驱动墙面的电动单元和机械“搜索臂”；拍下的影像存入数据库，并与过去观众的影像一起重放。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: YCAM, Yamaguchi 2010; NTT ICC, Tokyo 2011
- 视频: https://www.youtube.com/watch?v=5PKT44tU658
- 图片: https://www.ycam.jp/asset/image/_resize/large/archive/works_desire-of-codes_1__MG_9047@2x.jpg?s=1725165
- 项目主页: https://www.ycam.jp/en/archive/works/desire-of-codes/

#### 来自谷歌地球的明信片（Postcards from Google Earth） — Clement Valla (2010)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 这些不是故障，而是系统按设计运行的结果：Google Earth 是一个伪装成照片的数据库。
- 作品内容: Google Earth 截图：桥梁融化进河流，高速公路像布料一样披在山坡上；作品以明信片形式陈列在明信片架上出售。
- 实现方式: 未经修改的截图：航拍照片被贴图到一个并不知道桥梁存在的三维地形模型上；以喷墨明信片和网站呈现。
- 视角: 机器之眼, 失败、故障与错误
- 图片: https://www.clementvalla.com/img/wp/2013/09/deception_pass.jpg https://www.clementvalla.com/img/wp/2013/09/MG_9679.jpg
- 项目主页: https://www.clementvalla.com/work/postcards-from-google-earth.html

#### 嗅（Sniff） — Karolina Sobecka (2009)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 控制论与人工生命系统
- 核心想法: 给计算机视觉安上一只狗的身体，它对我们的判断就变成了我们能切身感到的东西。
- 作品内容: 临街橱窗上投影的虚拟狗跟随路人、嗅闻他们，并根据每个人的动作以及之前对它的态度，变得友善或敌意。
- 实现方式: 与 James George 合作：摄像头与机器视觉软件追踪并区分行人，读取姿态和手势，驱动游戏引擎中的狗，它的行为会累积对每个人的记忆。
- 视角: 机器之眼, 他异与恐怖谷
- 展出与获奖: VIDA 12.0, Special Mention
- 视频: https://www.youtube.com/watch?v=HEsOktyLeGs

#### 谷歌街景的九只眼（The Nine Eyes of Google Street View） — Jon Rafman (2008)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 漠然的自动相机产生了一种新的摄影：没有人选择按快门的时刻，但照片仍在诉说世界。
- 作品内容: 一个持续进行的 Google 街景截图合集：九镜头拍摄车在无人注视时记录下逮捕、事故、动物和各种奇怪瞬间。
- 实现方式: 由艺术家从街景图像中挑选截图，以网站、打印作品和书籍形式呈现。
- 视角: 机器之眼, 机器环世界
- 视频: https://www.youtube.com/watch?v=E-yH0GpfDK8
- 图片: https://64.media.tumblr.com/4dda5b7bf161a81c01f98014b6e6b674/8395f54aeb8544ee-a7/s500x750/166454b46f54ac8f8f130f901369b9a39c37c600.png
- 项目主页: https://9-eyes.com

#### 深层游戏（Deep Play） — Harun Farocki (2007)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 同一场比赛一旦由机器来看，就分裂成许多种图像：对球迷是奇观，对教练是数据，对警察是人群。
- 作品内容: 一件 12 频道装置，以电视信号、监控摄像头、球员追踪软件和动画数据图同步重放 2006 年世界杯决赛。
- 实现方式: 12 条各长 2 小时 15 分钟的同步影像，结合转播原始信号、安保摄像画面，以及对每名球员的计算机追踪与统计。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: documenta 12, Kassel, 2007; AV Festival, Newcastle, 2008
- 视频: https://www.youtube.com/watch?v=mIjrKxzFvpY
- 图片: https://www.harunfarocki.de/fileadmin/_processed_/e/e/csm_harun-farocki-deep-play-montreal_d09f2cf73e.jpg
- 项目主页: https://www.harunfarocki.de/installations/2000s/2007/deep-play.html

#### 分类守护进程（Sorting Daemon） — David Rokeby (2003)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 自动化画像看不见人，只看见可以分类的特征；那幅如绘画般的拼贴正是这种化约的肖像。
- 作品内容: 一台机器人摄像头扫描展厅外的街道寻找行人，把每个路人从背景中抠出并拆成色块，再按色相排列成一幅巨大的投影拼贴。
- 实现方式: 云台变焦摄像头配合运动检测与背景差分；被提取的人物按颜色分割，再依色相、饱和度与大小排列（肤色单独归类）。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Goethe-Institut Toronto, 'Surveillance Terrorism Democracy', 2003
- 视频: https://www.youtube.com/watch?v=Vhjoupz_e1s
- 图片: http://www.davidrokeby.com/SortingDaemonComposite_web.jpg http://www.davidrokeby.com/SD_Install_web.jpg
- 项目主页: http://www.davidrokeby.com/sorting.html

#### 眼睛/机器 I–III（Eye/Machine I–III） — Harun Farocki (2001)
- 类型: 电影与影像 · 机器: 计算机视觉, 自动驾驶与无人机, 工业机械臂
- 核心想法: 当图像成为操作的一部分，而不再是对操作的描绘，“看”就变成了瞄准、分拣与控制。
- 作品内容: 三部曲录像装置（2001–03），汇集导弹弹头摄像机、工业机器人与计算机视觉研究中的影像，这些图像本不是给人看的。
- 实现方式: 以双屏投影剪辑军事、工业和实验室的现成影像（智能炸弹、焊接机器人、物体识别），画面上保留机器自己绘制的引导线与叠加标记。
- 视角: 机器之眼, 隐形劳动与攫取
- 展出与获奖: ICA London (Eye/Machine III co-production), 2003
- 视频: https://www.youtube.com/watch?v=r4sDXhHqndk
- 图片: https://www.harunfarocki.de/fileadmin/_processed_/4/2/csm_harun-farocki-eye-machine-III-wien_9e5e84595f.jpg
- 项目主页: https://www.harunfarocki.de/installations/2000s/2003/eye-machine-iii.html

#### 分子信息学（Molecular Informatics） — 三上晴子 (1996)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 眼动追踪把无意识的“看”变成观者自己能看见的数据。
- 作品内容: 一件 VR 装置：头戴设备追踪观众的眼球运动，把每一次注视变成不断生长的分子结构，让“看”本身成为可见之物，并与另一位观众共享。
- 实现方式: 带眼动仪的头戴显示器；注视坐标实时生成类似分子的三维形态；首次在东京 Canon ARTLAB 展出。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: Canon ARTLAB, Tokyo 1996; DEAF96, V2_ Rotterdam; NTT ICC 2011 (Eye-Tracking Informatics)
- 视频: https://www.youtube.com/watch?v=vasyoHyklL8
- 图片: https://www.ntticc.or.jp/uploads/assets/001/6401b.1066.large.jpg
- 项目主页: https://www.ntticc.or.jp/en/archive/participants/mikami-seiko/

#### 液态视界（Liquid Views） — Monika Fleischmann, Wolfgang Strauss (1992)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 电脑做成的镜子从来不只是镜子：它捕捉、储存并转发你的影像，照镜子于是变成了被观看。
- 作品内容: 观众俯身看向一块模拟水面的水平触摸屏，看到自己的脸倒映其中；触碰水面会激起波纹，使倒影溶解，而身后的大投影把放大的面孔展示给房间里的其他人。
- 实现方式: 隐藏的摄像机拍下观者的脸，实时图形软件把它映射到对触摸有反应的模拟水面上；储存下来的影像也在墙面投影中显示。
- 视角: 机器之眼, 他异与恐怖谷
- 展出与获奖: Electric Dreams, Tate Modern 2024–25
- 视频: https://www.youtube.com/watch?v=bjq13wyjhA8
- 图片: https://upload.wikimedia.org/wikipedia/commons/c/c7/Fig3-LiquidViews.jpg http://www.eculturefactory.de/CMS/images/363.jpg
- 项目主页: http://www.eculturefactory.de/liquid-views

#### 表面张力（Surface Tension） — 拉斐尔·洛萨诺-亨默 (1992)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 机器追踪自有其凝视：一旦给它一只眼睛，被它跟随就像被某人注视。
- 作品内容: 屏幕上一只巨大的人眼以“奥威尔式的精确”跟随每位观众在房间里移动。作品创作于第一次海湾战争期间，那是摄像头制导“智能”炸弹首次大规模使用的战争；它给追踪机器装上了一只会回看的眼睛。
- 实现方式: 计算机追踪系统检测观众位置，从 500 多张眼睛的定格照片中选取画面，使眼睛看起来一直在追随观众。
- 视角: 机器之眼, 他异与恐怖谷
- 展出与获奖: Venice Biennale 2007; Whitechapel Gallery, London 2016; West Kowloon Cultural District, Hong Kong 2023
- 视频: https://www.youtube.com/watch?v=JXLoLPkzdto
- 图片: https://www.lozano-hemmer.com/image_sets/surface_tension/hong_kong_2023/surface_tension_hong_kong_2023_rlh_001.jpg
- 项目主页: https://www.lozano-hemmer.com/surface_tension.php

#### 命名者（The Giver of Names） — David Rokeby (1991)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 语音与听觉机器
- 核心想法: 机器命名靠联想而非理解；它的误读显示，感知其实是一串猜测。
- 作品内容: 观众把任意物品放在空基座上；摄像头捕捉画面，计算机分析其轮廓、颜色与纹理，然后大声说出一句诗意而常常古怪的话来为它命名。
- 实现方式: 摄像头与图像处理（轮廓、分割、颜色与纹理分析）驱动一个由词语与概念组成的联想数据库，生成合乎语法的句子并用语音合成说出。
- 视角: 机器之眼, 失败、故障与错误, 机器环世界
- 展出与获奖: Kiasma Museum of Contemporary Art, Helsinki (commission); Art Gallery of Windsor, 2008
- 视频: https://www.youtube.com/watch?v=sO9RggYz24Q
- 图片: http://www.davidrokeby.com/GON_AGW_web.jpg http://www.davidrokeby.com/gonscreenshot.jpg
- 项目主页: http://www.davidrokeby.com/gon.html

#### 机器视觉（Machine Vision） — Steina Vasulka (1978)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 工业机械臂
- 核心想法: 自行移动的摄像机，以机器的方式感知空间，无需身体。
- 作品内容: 一件装置：装在缓慢旋转的电动支架上的摄像机（其中一对对准一个镜面球体）扫视房间，在监视器上呈现人眼无法占据的视角。
- 实现方式: 转台与电动臂带动摄像机绕镜面球体转动，实时画面在房间内的监视器上播放。
- 视角: 机器之眼, 机器环世界
- 展出与获奖: Albright-Knox Art Gallery, Buffalo 1978
- 图片: http://www.vasulka.org/Steina/Steina_MachineVision/img/MachineVision01.jpg http://www.vasulka.org/Steina/Steina_MachineVision/img/MachineVision02.jpg
- 项目主页: http://www.vasulka.org/Steina/Steina_MachineVision/MachineVision.html

#### Videoplace — Myron Krueger (1975)
- 类型: 艺术作品与装置 · 机器: 计算机视觉
- 核心想法: 早在网络摄像头出现之前，计算机就已感知整个身体，而身体也学会了为机器之眼而动作。
- 作品内容: 参与者的实时视频剪影出现在大屏幕上，计算机识别他们的轮廓，让他们触碰、绘画，并与图形生物及远方参与者互动。
- 实现方式: 摄像机、实时提取剪影与分析轮廓的定制硬件，以及投影计算机图形；1975 年在密尔沃基美术馆以双向版本展出。
- 视角: 具身与动觉, 机器之眼, 能动、自主与共创
- 展出与获奖: Milwaukee Art Museum, 1975; SIGGRAPH Art Show, 1985 and 1990
- 论文: https://doi.org/10.1145/317456.317463 (CHI 1985)
- 视频: https://www.youtube.com/watch?v=dqZyZrN3Pl0
- 项目主页: https://en.wikipedia.org/wiki/Myron_W._Krueger

#### 电视佛（TV Buddha） — 白南准 (1974)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 闭路摄像机把冥想变成了自我监视：机器之眼成了一面没有外部的镜子。
- 作品内容: 一尊佛像面对着一台显示器，屏幕上是由闭路摄像机实时拍摄的佛像自身。佛通过机器无止境地凝视自己。
- 实现方式: 古董佛像、三脚架上的摄像机与显像管显示器组成实时闭路回路；此作有多个版本。
- 视角: 机器之眼, 他异与恐怖谷
- 展出与获奖: Galeria Bonino, New York 1974; Stedelijk Museum Amsterdam (collection)
- 视频: https://www.youtube.com/watch?v=MVwR1n0IZAs
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/53/TV_Buddha.jpg
- 项目主页: https://en.wikipedia.org/wiki/TV_Buddha

#### 中部地区（La Région Centrale） — Michael Snow (1971)
- 类型: 电影与影像 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 脱离人身体的摄像机，以任何人都无法做到的方式看见风景。
- 作品内容: 一部三小时的影片，在魁北克偏远山顶拍摄；摄像机装在可编程机械臂上，向各个方向摆动、旋转、翻转，镜头后没有操作者。
- 实现方式: Snow 请工程师 Pierre Abbeloos 制造一台由预录声音信号控制的电动摄像臂。
- 视角: 机器之眼, 机器环世界
- 视频: https://www.youtube.com/watch?v=KWyv7mSaXHM
- 项目主页: https://en.wikipedia.org/wiki/La_R%C3%A9gion_Centrale

### 机器之耳与声音

语音识别、语音助手、口音分析与合成声音。

#### 后话（After Words） — Machine Listening (Sean Dockray, James Parker, Joel Stern) (2022)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 数据集与训练数据, 聊天机器人与语言模型
- 核心想法: 数据从来不是“挖”出来的，而是“做”出来的：音频数据集是表演，常由演员完成；每一句“嘿，Alexa”也是一场为机器的表演。
- 作品内容: 一件八声道声音装置，由机器学习数据集中的现成音频拼成一系列思辨场景：从演员表演的情绪语音到 Google AudioSet，并穿插一段与语言模型合写又与之对抗的剧本。
- 实现方式: 采样自 Toronto 情绪语音数据集、DCASE 声音事件数据集与 Google AudioSet，加入批判数据研究者的配音与自回归语言模型生成的文本，在八个声道中空间化播放（18 分钟循环）。
- 视角: 机器之耳与声, 隐形劳动与攫取
- 展出与获奖: Data Relations, Australian Centre for Contemporary Art (ACCA), Melbourne (2022–23)
- 图片: https://machinelistening-web.somethingilearned.today/works/after-words/af2.jpg https://machinelistening-web.somethingilearned.today/works/after-words/1500-1001-max.jpg
- 项目主页: https://machinelistening.exposed/works/after-words/

#### 暗物质（Dark Matters） — Johann Diedrick (2021)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 数据集与训练数据
- 核心想法: 语音助手只能听懂数据集里有的声音；缺席的语音像暗物质一样，决定了谁能被听懂。
- 作品内容: 一件交互网页作品与影像装置，关于 Alexa、Siri 等语音界面训练数据集中黑人语音的缺席，以三维空间、声音与叙事展开。
- 实现方式: 基于语音数据集分析与录音构建的浏览器三维环境，以公开测试版网页和 24 小时橱窗影像的形式展出。
- 视角: 机器之耳与声, 分类、偏见与监控
- 展出与获奖: Squeaky Wheel Film & Media Art Center, Buffalo (2021); Mozilla Creative Media Awards 2021
- 视频: https://www.youtube.com/watch?v=_1XDpu2gabc
- 图片: https://squeaky.org/wp-content/uploads/2021/05/IMG_4224-scaled.jpg
- 项目主页: https://squeaky.org/event/johann-diedrick-dark-matters/

#### 机器聆听课程（Machine Listening, a Curriculum） — Machine Listening (Sean Dockray, James Parker, Joel Stern) (2020)
- 类型: 书与文章 · 机器: 语音与听觉机器, 监控与生物识别, 数据集与训练数据
- 核心想法: 设备如今不只录音，还分析并回应声音；机器聆听是一个知识权力领域，需要集体学习与对抗策略。
- 作品内容: 一套开放、持续更新的课程：书单、资料库、练习、访谈、委托写作、音乐与线上活动录像，讨论聆听机器的政治与美学；2020 年随 Liquid Architecture 与 Unsound 的系列直播发布。
- 实现方式: 开源教学平台（基于 Pirate Care 的课程工具），把教学大纲、档案与疫情期间的 Zoom 电台节目结合在一起。
- 视角: 机器之耳与声, 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: Unsound Festival 2020 (online); Liquid Architecture 2020
- 论文: http://archive.machinelistening.exposed/curriculum/ (Liquid Architecture & Unsound, 2020)
- 视频: https://www.youtube.com/watch?v=iUbglqQLdrI
- 图片: https://machinelistening.exposed/images/home/hero.png
- 项目主页: https://machinelistening.exposed/curriculum/

#### 自动语音识别中的种族差异（Racial Disparities in Automated Speech Recognition） — Allison Koenecke (2020)
- 类型: 论文 · 机器: 语音与听觉机器
- 核心想法: 聆听机器对一些人的声音“听”得更差；差距源于声学模型的训练数据，而非人们的说话方式。
- 作品内容: 对五家商用语音识别系统（Amazon、Apple、Google、IBM、Microsoft）的审计：用美国黑人与白人受访者的访谈录音测试，黑人说话者的平均词错误率为 0.35，白人为 0.19。
- 实现方式: 用各厂商的语音识别接口转写 CORAAL 与 VOC 语料库中匹配的音频片段，比较词错误率，并分离出声学模型的影响。
- 视角: 机器之耳与声, 分类、偏见与监控
- 论文: https://doi.org/10.1073/pnas.1915768117 (PNAS 117(14), 2020)
- 视频: https://www.youtube.com/watch?v=1fQ7q4_x00I
- 项目主页: https://www.pnas.org/doi/10.1073/pnas.1915768117

#### 论噪声看似无意义的质地（On the Apparently Meaningless Texture of Noise） — Pedro Oliveira (2019)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 数据集与训练数据, 监控与生物识别
- 核心想法: 聆听机器被训练成要丢弃的“噪声”，恰恰是移民的声音保存其历史的地方。
- 作品内容: 一篇双耳声音散文，关于德国庇护程序中使用的“方言识别软件”：它去聆听训练数据要求软件忽略的呼吸、停顿等副语言“噪声”，并用声音与流出的培训文件建立一份反档案。
- 实现方式: 2019 年在斯德哥尔摩 EMS 录制，由被标注的副语言特征、声音以及德国联邦移民与难民局（BAMF）各地办事处的内部文件构成；作为 Akademie Schloss Solitude 与 ZKM 网络驻留项目在线发布。
- 视角: 机器之耳与声, 分类、偏见与监控
- 展出与获奖: HASH Award 2020, 2nd prize (ZKM / Akademie Schloss Solitude)
- 图片: https://oliveira.work/wp-content/uploads/2020/01/schulung-mod-1.jpg https://oliveira.work/wp-content/uploads/2020/01/echoes-m.jpg
- 项目主页: https://oliveira.work/meaningless-texture/

#### Alias 计划（Project Alias） — Bjørn Karmann, Tore Knudsen (2018)
- 类型: 思辨设计 · 机器: 语音与听觉机器
- 核心想法: 面对“永远在听”的机器，你可以给它配一台属于自己的机器，由它来决定对方听到什么。
- 作品内容: 一个像真菌一样的“寄生体”，罩在 Google Home 或 Amazon Echo 上，用持续的低语让它“失聪”；只有听到用户自己设定的唤醒词时，它才停下噪声，替你轻声说出真正的唤醒词。
- 实现方式: 树莓派连接麦克风和两个小扬声器，运行在本地训练的唤醒词分类器；被触发前一直向助手的麦克风输送噪声。
- 视角: 机器之耳与声, 能动、自主与共创
- 展出与获奖: S+T+ARTS Prize 2019, Grand Prize – Artistic Exploration; Ars Electronica Festival 2019
- 视频: https://www.youtube.com/watch?v=qZFytvJ6ano
- 图片: https://bjoernkarmann.dk/wp-content/uploads/2023/03/Alias-2.jpg https://bjoernkarmann.dk/wp-content/uploads/2023/03/Alias-3.jpg
- 项目主页: https://bjoernkarmann.dk/project_alias
- 代码: https://github.com/bjoernkarmann/project_alias

#### 联结主义的黑暗时代（The Dark Age of Connectionism） — Wesley Goatley (2017)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器
- 核心想法: “永远在听”的设备会重塑人的行为：要躲开它的耳朵，你就得改变自己在房间里的存在方式。
- 作品内容: 一台 Amazon Echo 被麦克风包围：观众发出的每个声音都会触发 Siri 向 Echo 提出一个关于其政治与功能的问题；想听清回答，观众就得学会在它身边保持安静。
- 实现方式: 周围的麦克风侦测附近的声音事件，触发用 Apple Siri 声音向 Amazon Echo 提出的预设问题；每个新声音都会打断上一个问题。
- 视角: 机器之耳与声, 不透明与潜空间
- 展出与获奖: Haunted Random Forests Festival, UK (2017); IMPAKT Festival, Utrecht (2018); Sonic Arts Seoul (2018)
- 视频: https://vimeo.com/241915190
- 图片: https://wesleygoatley.com/images/da-detail.webp
- 项目主页: https://wesleygoatley.com/dark-age.html

#### 覆胶钢（Rubber Coated Steel） — Lawrence Abu Hamdan (2016)
- 类型: 电影与影像 · 机器: 语音与听觉机器
- 核心想法: 机器音频分析能听见人类证人听不到的东西；影片追问的是，法庭仍然听不见谁的沉默。
- 作品内容: 一部 21 分钟的影像，被布置成审判枪声的法庭：它重现 2014 年两名巴勒斯坦少年遇害案中的声学证据；阿布·哈姆丹的频谱分析证明，实弹被伪装成了橡皮子弹的声音。
- 实现方式: 与 Forensic Architecture 为保护儿童国际组织所做的音频弹道分析，将录音中枪声的频率可视化，再以一间只有字幕和沉默的空法庭重新呈现。
- 视角: 机器之耳与声, 不透明与潜空间
- 展出与获奖: Earshot, Portikus, Frankfurt (2016); International Film Festival Rotterdam (IFFR)
- 视频: https://www.youtube.com/watch?v=NsZHAliJihk
- 图片: https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1633429204074-1Q6FTZP2L0W47AWT341C/earshot+2.jpg https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1633525130412-322L2ZAC9UXE628Q3X6I/Lawrence-Abu-Hamdan_31-b.jpg
- 项目主页: http://lawrenceabuhamdan.com/earshot

#### Conversnitch — Brian House, Kyle McDonald (2014)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 所谓“聆听机器”有一部分是人：自动化窃听依靠隐藏的人工转写员，最后变成公开广播。
- 作品内容: 一个伪装成灯泡的小装置，偷听周围的对话；录音片段交给 Mechanical Turk 上的匿名工人转写，然后发布到 Twitter。
- 实现方式: 藏在灯座外壳里的麦克风和树莓派把音频传到 Amazon Mechanical Turk 转写，文字再自动发到 Twitter。
- 视角: 机器之耳与声, 隐形劳动与攫取, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=ueeQ7T0thwc
- 图片: https://brianhouse.net/works/conversnitch/conversnitch.jpg https://brianhouse.net/works/conversnitch/conversnitch_1.jpg
- 项目主页: https://brianhouse.net/works/conversnitch/

#### 冲突的音素（Conflicted Phonemes） — Lawrence Abu Hamdan (2012)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 当国家通过口音来判定国籍，声音就被当成了护照；描绘一个声音混杂的来历，就是拒绝这种简化。
- 作品内容: 与设计师 Janna Ulrich 合作的巨幅图表，描绘了十二位索马里庇护申请者的声音；他们在荷兰经“语言与口音分析”后被拒。图中记录的迁徙与难民营经历，无法被一种“正确”口音所概括。
- 实现方式: 2012 年在乌得勒支与被拒申请者、语言学家和社运人士开会研究，成果做成墙面时间线与可带走的 A4 单页；这些图后来被提交给荷兰移民法官和英国庇护法庭。
- 视角: 机器之耳与声, 分类、偏见与监控
- 展出与获奖: Casco Office for Art, Design and Theory, Utrecht (commission, 2012)
- 图片: https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1487689651283-1IJLGTCD230AZQVHJSYS/LH001-ConfictedPhonemes-det-web.jpg https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1487689643617-IWQ7CJM52SRIJXJL6XDR/_MG_9667.JPG
- 项目主页: http://lawrenceabuhamdan.com/conflicted-phonemes

#### 言论自由本身（The Freedom of Speech Itself） — Lawrence Abu Hamdan (2012)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 语音分析把你的说话方式变成一块领土：决定你属于哪里的，不是你说了什么，而是国家的耳朵。
- 作品内容: 一部 34 分钟的音频纪录片，讲述英国如何用法证语音分析与“声纹”来检验庇护申请者口音的来源；观众在形似单词“you”声纹的吸音泡沫雕塑之间聆听。
- 实现方式: 采访律师、语音学家、庇护申请者与英国内政部官员，用广播剧式的声音手法剪辑；泡沫雕塑是两个声音频率与振幅的等高线图。
- 视角: 机器之耳与声, 分类、偏见与监控
- 展出与获奖: The Showroom, London (commission, 2012)
- 图片: https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1487690498833-HX5J9ER5A4EN8SHONRBC/foam%2Bvoice%2Bprint.jpg https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1487690496112-HWUTKCQALIUYA2L3TI4D/Extra%2Bcity%2Bfoam%2B2%2Bcopy.jpg
- 项目主页: http://lawrenceabuhamdan.com/the-freedom-of-speech-itself

#### 全部真相（The Whole Truth） — Lawrence Abu Hamdan (2012)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 语音压力分析号称能越过言语、听进身体；把它反过来用在制造者身上，便暴露了它判断的随意。
- 作品内容: 关于语音测谎仪的装置与音频纪录片：这类技术曾在欧洲、俄罗斯和以色列政府试点，并被边境机构与保险公司使用。观众收听软件开发者与销售者的访谈时，一台被逆向改造的测谎仪正实时判定这些声音的真假。
- 实现方式: 被逆向改造的语音测谎软件实时分析纪录片音频；三频道影像、立体声、桌椅与假植物布置成一间审讯室。
- 视角: 机器之耳与声, 分类、偏见与监控, 失败、故障与错误
- 展出与获奖: Casco Office for Art, Design and Theory, Utrecht (commission, 2012)
- 图片: https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1568880234051-G7XRKWGT7ZVT1IMO6KIW/LA_EThe+Whole+Truth_2012_Reverse+engineered+lie+detector%2C+3+channel+video%2C+stereo+sound%2C+desk%2C+3+chairs%2C+3+artificial+plants_24+minutes_612x435x190cm_1.jpg https://images.squarespace-cdn.com/content/v1/5209b9c5e4b0bc18c96df1ec/1568880459670-25NI8IPE3QWLMOWXG69F/LA_EThe+Whole+Truth_2012_Reverse+engineered+lie+detector%2C+3+channel+video%2C+stereo+sound%2C+desk%2C+3+chairs%2C+3+artificial+plants_24+minutes_612x435x190cm_5.jpg
- 项目主页: http://lawrenceabuhamdan.com/the-whole-truth

#### Blendie — Kelly Dobson (2004)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器
- 核心想法: 不是机器学我们的语言，而是我们要学它的声音；控制变成了模仿，也变成了与电器之间一种奇特的共情。
- 作品内容: 一台 1950 年代的 Osterizer 搅拌机，只听人的声音：你得像搅拌机一样低吼、嗡鸣，它才会按你模仿的音高与力度转动。
- 实现方式: 定制的软硬件实时分析声音，把使用者模仿搅拌机时的音高与响度映射到电机转速上。
- 视角: 机器之耳与声, 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: HOME\SICK, Science Gallery Dublin
- 视频: https://www.youtube.com/watch?v=tph40hgcLpU
- 图片: http://www.kellydobson.com/blendie.png
- 项目主页: https://www.media.mit.edu/projects/blendie/overview/

### 数据集与标签

训练数据集、标签，以及其中内置的世界观。

#### Tinder_gun_boys_@Brussels_ — Loïs Soleil (2022)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 平台与推荐算法
- 核心想法: 把交友软件的筛选逻辑反用到它的用户身上，显示机器多么容易建立一个关于人的数据集，以及这个数据集可以被用来做什么。
- 作品内容: 一台机器人自动在 Tinder 上滑动，一个识别武器的 AI 截下与枪合影的男性资料；这些图像被印在榻榻米垫上，用于在装置中开设的女性主义防身课。
- 实现方式: 一台实体滑动机器人操作运行 Tinder 的手机；目标检测模型识别带武器的头像，每天保存数百张截图；律师意见被整理成影片 How not to get sued as an artist。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2025, Honorary Mention (Artificial Life & Intelligence)
- 视频: https://vimeo.com/1084594874
- 图片: http://loissoleil.com/pages/tinder/Robot.jpg https://archive.aec.at/asset/3845109/preview/
- 项目主页: http://loissoleil.com/tinder

#### 分类之歌（Sorting Song） — Simone C. Niquille (2021)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 对人来说理所当然的物品类别，是机器无法参与的协商；碗与花瓶的边界其实是一种选择。
- 作品内容: 来自 SceneNet RGB-D 训练数据集的家居物品在花瓶与碗、长凳与沙发、椅子与马桶之间不断变形。当数据集只记录形状时，轮椅、马桶和电椅可能被归入同一类。
- 实现方式: 把帝国理工学院 SceneNet RGB-D 室内数据集中的三维网格制成在不同类别标签之间变形的动画。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 视频: https://vimeo.com/555060893
- 图片: https://technofle.sh/static/media/SOS_SortingSong_001.jpg https://technofle.sh/static/media/SOS_CowSharkFalling.png
- 项目主页: https://technofle.sh/sorting-song.html

#### 蕾丝（Lacework） — Everest Pipkin (2020)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 训练集由他人的生活片段组成，每段只剩一个词；把它完整看一遍，才重新感到这些生活的分量。
- 作品内容: 一条由 MIT「Moments in Time」数据集构成的缓慢、梦境般的影像之河：数据集含一百万段从网络抓取的三秒短片，每段只被标注一个动词，如“祈祷”“飞”。Pipkin 看完了整个数据集，并把这些片段拉伸成幻觉般的慢动作。
- 实现方式: 用神经网络插帧与超分辨率算法处理「Moments in Time」动作识别数据集中的片段，将其放慢、放大，连成一段连续影像。
- 视角: 分类、偏见与监控, 隐形劳动与攫取, 机器之眼
- 展出与获奖: The Photographers' Gallery, London (Data / Set / Match), 2020
- 视频: https://everest-pipkin.com/projects/lacework/flickr-5-6-5-8-9-7-1-8-4756589718_2.slowed_x2.00_x2.00_x2.00_x2.00_x1.00-20.webformat.mp4
- 图片: https://thephotographersgallery.org.uk/sites/default/files/styles/banner_image/public/ep2.png.webp?itok=wVNy-Lyc
- 项目主页: https://everest-pipkin.com/projects/lacework.html

#### 大型图像数据集：计算机视觉的皮洛士式胜利？（Large Image Datasets: A Pyrrhic Win for Computer Vision?） — Abeba Birhane (2020)
- 类型: 论文 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 视觉模型能看见什么，取决于未经同意收集的图像和无人核查的标签。
- 作品内容: Abeba Birhane 与 Vinay Uday Prabhu 审计了 ImageNet、MIT「8000 万张微型图像」等大型图像数据集，发现标签中有侮辱性词汇，并含有未经同意的、色情的和有害的图像。这篇论文促使 MIT 撤下了 Tiny Images 数据集。
- 实现方式: 对大规模视觉数据集的标签与图像内容进行定量与定性审计，并提出改进建议。
- 视角: 分类、偏见与监控
- 论文: https://doi.org/10.1109/WACV48630.2021.00158 (WACV 2021)
- 项目主页: https://arxiv.org/abs/2006.16923

#### 模型动物园（Model Zoo） — Forensic Architecture (2020)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 当暴力的真实影像稀缺时，合成训练集让机器学会看见调查者需要找到的东西。
- 作品内容: 一个不断扩充的目录：收录弹药与武器的三维模型，以及用这些模型的合成渲染图训练、用于在冲突影像中识别它们的机器学习分类器。
- 实现方式: 以武器三维模型的逼真渲染图组成合成数据集；在其上训练的分类器再用开源影像进行检验。
- 视角: 机器之眼, 分类、偏见与监控
- 图片: https://i.vimeocdn.com/video/864290475-35c09a4a9d98e29cb953c40599ec67ec2e384f73e62ec820ed4e0e80c17c162a-d_1280x720.jpg
- 项目主页: https://forensic-architecture.org/investigation/model-zoo

#### 无名女子的野餐（Pique Nique pour les Inconnues） — Rosa Menkman (2020)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 机器观看图像的标准是用女性面孔校准的：她们的脸在无尽复制中留存，名字却消失了。
- 作品内容: 色彩测试卡上的无名女性（Lena、Shirley 等），连同聊天机器人和图库占位图，聚集在电脑桌面上，试图只用系统提示音一起合唱。
- 实现方式: 以桌面录像形式呈现的“远程合唱”，让历史测试图像与虚拟助手动起来，用操作系统声音演唱 Paul McCartney 的《We All Stand Together》。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=6n7t3A3UF3o
- 图片: https://freight.cargo.site/i/2bf5877371a4095252b3a01af61a332deb9cc1a034752cce60fd6b0afa06d8c3/iRD.png
- 项目主页: https://beyondresolution.info/COLOR-TEST-CARDS

#### 先祖（Salaf (Ancestors)） — Nouf Aljowaysir (2020)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 机器视觉继承了殖民档案的目光；为了拒绝这种目光，艺术家用“缺席”来训练机器。
- 作品内容: 艺术家追溯家族穿越阿拉伯半岛与美索不达米亚的迁徙，把大量档案照片（许多来自 Gertrude Bell 的殖民档案）输入计算机视觉模型。模型认不出戴面纱的女性是女性，还把贝都因人标为“士兵”“军队”；于是她用分割算法抹去其中的人物，制成约 6000 张图像的“缺席数据集”。
- 实现方式: 用商用计算机视觉模型为抓取的博物馆与档案照片打标签，再用 AI 分割技术移除其中带东方主义色彩的人物，生成“空图像”数据集。
- 视角: 分类、偏见与监控, 失败、故障与错误, 哀悼、记忆与来世
- 展出与获奖: ThoughtWorks Arts residency, New York, 2020
- 图片: https://images.squarespace-cdn.com/content/v1/55039003e4b04b9963242639/1763375737992-MHJQB7XNFGLGYDDDY41V/186--Woman%2Bseated%2Bcross-legged%2Bwith%2Bshoes%2Boff-209.jpg https://images.squarespace-cdn.com/content/v1/55039003e4b04b9963242639/1763375946970-N2HOYYFEJ9ZTJ56QK06N/188--Paysannes%2Begyptiense%2Ballant%2Ba%2Bl%25E2%2580%2599eua-1133.jpg
- 项目主页: https://www.noufaljowaysir.com/work/salaf

#### 解密器（AI 背后的人）（Declassifier (Humans of AI)） — Philipp Schmitt (2019)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 机器的每一次“认出”，都是对别人照片的一次回忆。
- 作品内容: 一个计算机视觉程序在观看照片，但它不在识别出的物体周围画框，而是叠加上当初教会它认出这些物体的 COCO 训练图像。作品属于《Humans of AI》系列，该系列还为构成数据集的数千位 Flickr 摄影师署名。
- 实现方式: 用在微软 COCO 数据集上训练的物体检测器处理图像；每检测到一个物体，软件就调出并拼贴该类别的 COCO 训练照片，并注明摄影师。
- 视角: 机器之眼, 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: The Photographers' Gallery, London, 2020
- 视频: https://www.youtube.com/watch?v=IOZe5wEcXxY
- 图片: https://cdn.philippschmitt.com/media/pages/work/humans-of-ai/58fb56c131-1586885726/philipp-schmitt_humans-of-ai-1-1200x630-crop.jpg
- 项目主页: https://philippschmitt.com/work/humans-of-ai

#### 挖掘 AI：机器学习训练集中的图像政治（Excavating AI: The Politics of Images in Machine Learning Training Sets） — Kate Crawford, Trevor Paglen (2019)
- 类型: 书与文章 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 每个训练数据集都编码了一种政治：决定一张图像“是什么”是权力的行使，而不是中立的描述。
- 作品内容: 一篇文章，逐层挖掘 ImageNet、JAFFE、UTKFace 等训练数据集，从分类体系、类别一直深入到单张被贴上标签的图像。
- 实现方式: 以考古式方法解读数据集结构（WordNet 层级、标签选择、图像来源），配以图像实例；由作者与 AI Now 研究所在线发表。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 论文: https://excavating.ai (excavating.ai (AI Now Institute), 2019)
- 视频: https://www.youtube.com/watch?v=ZiHHsKALwBc
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-Excavating_AI-1024x385.jpg
- 项目主页: https://excavating.ai

#### 从“苹果”到“异常”（图片与标签）（From ‘Apple’ to ‘Anomaly’ (Pictures and Labels)） — Trevor Paglen (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 训练数据集就是一种世界观：沿着它的标签走下去，会看到命名事物如何迅速滑向评判他人。
- 作品内容: 约三万张来自 ImageNet 数据集的照片按标签分组，铺满巴比肯中心弧形展厅，从“苹果”这样无害的名词逐渐走向对人的评判。
- 实现方式: 从 ImageNet 中选取类别与图像，逐张打印，按标签成簇钉在 90 米长的弧形墙上，向马格利特《图像的背叛》致敬。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Barbican Centre, The Curve, London, 2019–20
- 视频: https://www.youtube.com/watch?v=juSXaQWNXgU
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-From_Apple_to_Anomaly-2019-03-1024x683.jpg https://paglen.studio/wp-content/uploads/2020/05/Paglen-From_Apple_to_Anomaly_2019-01-1024x683.jpg
- 项目主页: https://paglen.studio/2020/04/09/from-apple-to-anomaly-pictures-and-labels-selections-from-the-imagenet-dataset-for-object-recognition/

#### 家庭学校（HOMESCHOOL） — Simone C. Niquille (2019)
- 类型: 电影与影像 · 机器: 计算机视觉, 数据集与训练数据, 机器生物与移动机器人
- 核心想法: 机器人住进你家之前，家必须先被重建为数据集；凡是不合类别的东西都会消失。
- 作品内容: 一部 13 分钟的三维动画影片，场景设在用于训练家用机器人计算机视觉的合成样板房里。它追问：成千上万个家，人们最私密的空间，如何被变成机器人可以导航的类别——这是花瓶、碗还是杯子？
- 实现方式: 用家用机器人视觉所用的合成室内训练数据集中的模型与平面图制作三维动画，配四声道声音。
- 视角: 机器之眼, 分类、偏见与监控, 机器环世界
- 展出与获奖: Commissioned by Housing the Human, with Swissnex San Francisco and Fotomuseum Winterthur, 2019
- 视频: https://vimeo.com/362563329
- 图片: https://technofle.sh/static/media/SCN_Homeschool_Still02_SimoneNiquille-Technoflesh.jpg https://technofle.sh/static/media/HS_Homeschool_depth_SimoneNiquille-Technoflesh.png
- 项目主页: https://technofle.sh/homeschool.html

#### ImageNet 轮盘（ImageNet Roulette） — Trevor Paglen, Kate Crawford (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉, 监控与生物识别
- 核心想法: 让训练数据集“自己说话”，揭示了按外貌给人分类在设计上就有害，而非偶然出错。
- 作品内容: 一个网页应用兼装置，用基于 ImageNet“人”类别训练的模型给任何人的自拍贴标签，返回的词常常荒谬、带种族歧视或残忍；2019 年 9 月有数百万人试用。
- 实现方式: 在 ImageNet 约 2800 个“人”子类别上训练的分类器检测人脸并返回最接近的标签；网上版本已下线，作为装置《Faces of ImageNet》（2022）延续。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 展出与获奖: Training Humans, Fondazione Prada, Milan, 2019; Poetics of Encryption, Kunsthal Charlottenborg, 2024 (as Faces of ImageNet); The World Through AI, Jeu de Paume, Paris, 2025 (as Faces of ImageNet)
- 视频: https://www.youtube.com/watch?v=K_lN4JD1sBY
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Crawford_Paglen.jpg https://paglen.studio/wp-content/uploads/2020/06/failure.jpg
- 项目主页: https://paglen.studio/2020/04/29/imagenet-roulette/

#### MegaPixels / Exposing.ai — Adam Harvey, Jules LaPlace (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 人脸识别建立在人们出于别的目的拍下的普通照片之上；监控始于数据集。
- 作品内容: 一个研究项目和搜索引擎，追溯人脸与生物识别训练数据集的来源，并让任何人查询自己的 Flickr 照片是否被收入其中。
- 实现方式: 把数十个从 Flickr 抓取（2004–2020）的公开人脸数据集中的照片编号与元数据建立索引供用户检索；MegaPixels 运行于 2017–2020 年，2021 年以 Exposing.ai 重新上线。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: Ars Electronica Center, Understanding AI 2019; Ludwig Forum Aachen, Training the Archive 2020
- 视频: https://www.youtube.com/watch?v=ey9lPMknV2E
- 图片: https://adam.harvey.studio/exposing-ai/exposing-ai.webp https://exposing.ai/assets/img/og-share.png
- 项目主页: https://exposing.ai

#### 训练人类（Training Humans） — Kate Crawford, Trevor Paglen (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 训练图像是一种无人观看的日常摄影，却决定了机器将如何看待每一个人。
- 作品内容: 一场展出用来训练计算机视觉“认人”的照片的展览，从 FERET 等早期政府资助的人脸数据库，到从网络上抓取的图像和为情绪识别构建的数据集。
- 实现方式: 以打印作品和墙面网格策展呈现历史与当代的训练数据集（人脸、手势、情绪、步态），并以《ImageNet Roulette》作为互动作品。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Osservatorio Fondazione Prada, Milan, 2019–20
- 视频: https://www.youtube.com/watch?v=P4JpD1PWBDI
- 图片: https://paglen.studio/wp-content/uploads/2020/05/PaglenCrawford-Training_Humans-2019_01-1024x684.jpg https://paglen.studio/wp-content/uploads/2020/05/PaglenCrawford-Training_Humans-2019_02-1024x683.jpg
- 项目主页: https://paglen.studio/2020/04/09/kate-crawford-trevor-paglen-training-humans/

#### Triple-Chaser — Forensic Architecture (2019)
- 类型: 电影与影像 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 计算机视觉可以反过来对抗权力：用合成图像教出来的机器，成为国家暴力的证人。
- 作品内容: 为 2019 年惠特尼双年展而作。影片追踪向平民发射的 Triple-Chaser 催泪弹，追溯到惠特尼美术馆董事会副主席 Warren B. Kanders 所拥有的 Safariland 公司。由于真实照片极少，团队用逼真的合成图像训练分类器，在网络上搜寻这种弹药。
- 实现方式: 把催泪弹的三维模型渲染成数千张光照和背景各异的合成训练图像，用来训练扫描网络图像的机器学习分类器；影片与 Praxis Films 合作完成。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Whitney Biennial, New York, 2019
- 视频: https://www.youtube.com/watch?v=93rjwQMww9M
- 图片: https://content.forensic-architecture.org/wp-content/uploads/2019/05/Photorealistic_4-mask-1-1600x900.jpg https://i.vimeocdn.com/video/782522102-fef4ec627744abb9949fe05683df148918c13b8c94847f95ab0c848f8c016c7e-d_1280x720.jpg
- 项目主页: https://forensic-architecture.org/investigation/triple-chaser

#### Zizi——酷儿化数据集（Zizi – Queering the Dataset） — Jake Elwes (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据, 监控与生物识别
- 核心想法: 把数据集遗漏的面孔加进去，机器能想象的范围就会改变，也暴露出它原本没学到什么。
- 作品内容: 一件多频道影像，画面中的面孔不断变换：一个用七万张照片训练的人脸模型，再加入一千张变装与性别流动者的面孔重新训练后生成了这些图像。网络的权重逐渐偏离它最初学到的“规范”面孔。
- 实现方式: 在 FFHQ 人脸数据集上训练的 StyleGAN，再用网上找到的约一千张变装与性别流动者面孔微调；在潜空间中游走，生成 135 分钟的循环影像。
- 视角: 分类、偏见与监控, 不透明与潜空间, 他异与恐怖谷
- 展出与获奖: Edinburgh Fringe (Inspace), 2019; You and AI, Onassis Foundation, Athens, 2021; Among the Machines, Zabludowicz Collection, London, 2022
- 视频: https://vimeo.com/388245510
- 图片: https://www.jakeelwes.com/images/project-zizi19.jpg https://www.jakeelwes.com/images/project-zizi19/Zabludowicz.jpg
- 项目主页: https://www.jakeelwes.com/project-zizi-2019.html

#### 万千（郁金香）（Myriad (Tulips)） — Anna Ridler (2018)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 生成模型与潜空间
- 核心想法: 展示数据集而非模型，揭示了机器学习所依赖的缓慢人工劳动与人的判断。
- 作品内容: 一件由数千张郁金香照片组成的装置：Ridler 在一个郁金香花季里亲自购买、拍摄并手写标注每一朵花，这些图像随后成为她的 GAN 作品《Mosaic Virus》的训练集。每张照片上都留着她手写的标签。
- 实现方式: 艺术家亲自拍摄并手工标注约一万张郁金香照片，以带手写标签的照片形式展出；该数据集后来用于训练 GAN。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: AI: More than Human, Barbican, London, 2019
- 视频: https://vimeo.com/428168704
- 图片: https://annaridler.com/content/works/myriad-tulips/block_1/DSC01064.webp https://annaridler.com/content/works/myriad-tulips/block_3/group_3/0IMG_1672.jpeg
- 项目主页: https://annaridler.com/myriad-tulips

#### 这是问题、解决方案、过去与未来（This is the Problem, the Solution, the Past and the Future） — Sebastian Schmieg (2017)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 只要有足够多的人点击，任何类别都能教给机器；荒诞的标签暴露出所有标签的任意性。
- 作品内容: 一个概念性的训练数据集：摄影师画廊网站上的 2931 张照片，经访客近三万次点击，被分入“问题、解决方案、过去、未来”四类。这些点击来自 Schmieg 2016 年的介入作品《Decision Space》，它在画廊网站的每张图上都加了这四个按钮。
- 实现方式: 通过网页介入收集公众对画廊图像的分类；由此得到的标注数据集以网站和墙纸形式发布，并用于训练图像分类器（《Decisive Camera》）。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: Commissioned by The Photographers' Gallery, London, 2016–17
- 图片: https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/02/titptstpatf-dc-q21-1-1024x1024.jpg https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/02/decision-space-1-1024x683.png
- 项目主页: https://sebastianschmieg.com/this-is-the-problem-the-solution-the-past-and-the-future/

#### 动物分类器（Animal Classifier） — Shinseungback Kimyonghun (2016)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 任何机器分类都建立在某种任意的分类法之上；这件作品只是把这种任意性摆到了明处。
- 作品内容: 训练一个神经网络，按博尔赫斯文章中“中国百科全书”的 14 个荒诞类别给动物分类，比如“属于皇帝的”“传说中的”“远看像苍蝇的”。
- 实现方式: 用网络图片训练的 TensorFlow 卷积神经网络，运行在 14 台树莓派上，置于玻璃罩与显示器中。
- 视角: 分类、偏见与监控, 机器之眼
- 视频: https://vimeo.com/198948703
- 图片: https://djhznh41oxwef.cloudfront.net/works/animal_classifier/ssbkyh_animal_classifier_01.png
- 项目主页: https://ssbkyh.com/works/animal_classifier/

#### Segmentation.Network — Sebastian Schmieg (2016)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 机器视觉是手绘出来的：有人决定了每个物体的边界，也决定了什么将不被识别。
- 作品内容: 一个网站，逐一回放众包工人为微软 COCO 数据集在 Flickr 照片中勾画的 60 多万条物体轮廓。一笔一笔地，它展示了决定机器“能看见什么”的手工劳动。
- 实现方式: 定制软件按顺序动画回放 COCO 数据集中的多边形分割标注；2018 年另有投影装置版本。
- 视角: 隐形劳动与攫取, 机器之眼
- 图片: https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/01/segmentation-network-ani-01.gif https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/01/segmentation-network-01-1024x683.png
- 项目主页: https://sebastianschmieg.com/segmentation-network/

#### ImageNet：一个大规模分层图像数据库（ImageNet: A Large-Scale Hierarchical Image Database） — 邓嘉 (2009)
- 类型: 论文 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 机器看世界的方式，继承自一部词典的名词层级和成千上万次匿名点击。
- 作品内容: 邓嘉、董伟、Richard Socher、李李佳、李凯与李飞飞在 CVPR 2009 发表的论文，推出 ImageNet：数百万张网络图像按 WordNet 名词层级分类，并由亚马逊 Mechanical Turk 众包工人核验。它成为开启深度学习计算机视觉的基准。
- 实现方式: 以 WordNet 同义词集检索搜索引擎收集图像，再由亚马逊 Mechanical Turk 工人清洗和核验。
- 视角: 分类、偏见与监控, 隐形劳动与攫取, 机器之眼
- 论文: https://doi.org/10.1109/CVPR.2009.5206848 (CVPR 2009)
- 项目主页: https://www.image-net.org/

### 人脸、情绪与生物识别

人脸识别、情绪识别，以及被转化为数据的身体。

#### 弗拉芒刷屏者（The Flemish Scrollers） — Dries Depoorter (2021)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 通常对准公民的自动人脸识别，被转向为它制定规则的人。
- 作品内容: 软件监看弗拉芒议会每天的直播，一旦发现有议员低头看手机，就通过人脸识别认出其身份，把片段发到社交媒体并点名标记。
- 实现方式: Keras 目标检测与人脸识别模型分析议会的 YouTube 直播；FFmpeg 剪出片段，自动发布到 Twitter 与 Instagram。自 2021 年 7 月 5 日起运行。
- 视角: 分类、偏见与监控, 机器之眼
- 视频: https://www.youtube.com/watch?v=5YHfK6DBvGE
- 图片: https://driesdepoorter.be/wp-content/uploads/2022/03/TheFlemishScollers-photo-by-Dries-Depoorter-01-1612x845.jpg https://driesdepoorter.be/wp-content/uploads/2021/07/The-Flemish-Scrollers-Software-Dries-Depoorter-1024x522.png
- 项目主页: https://driesdepoorter.be/theflemishscrollers/

#### 捕获（Capture） — Paolo Cirio (2020)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉, 数据集与训练数据
- 核心想法: 当人脸识别对准警察时，感觉就不一样了：由此引发的愤怒揭示了“谁可以被识别”的不对称。
- 作品内容: Cirio 用人脸识别处理了 1000 张法国抗议活动的新闻照片，建立了包含 4000 名警察面孔的数据库，邀请公众辨认他们的姓名，并把头像做成海报张贴在巴黎街头。法国内政部长要求审查这件作品。
- 实现方式: 用人脸检测与识别软件处理公开照片，提取并聚类警察面孔，发布在 Capture-Police.com 平台上并印成街头海报；与“在欧洲禁止人脸识别”的倡议相连。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Le Fresnoy, Tourcoing 2020 (co-production)
- 视频: https://www.youtube.com/watch?v=JPybxTM-daE
- 图片: https://paolocirio.net/work/capture/slideshow/NIK_2255.jpg
- 项目主页: https://paolocirio.net/work/capture/

#### 面子功夫（Facework） — Kyle McDonald (2020)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉, 平台与推荐算法
- 核心想法: 迎合人脸分类器的游戏过程，让人建立起“像机器一样看”的直觉，也看清它的类别有多随意。
- 作品内容: 一个设定在“零工经济”中的网页游戏，面部分析就是工作：玩家作为“Faceworker”接单，任务要求摄像头判定你戴着眼镜或看起来很开心，玩家由此实时体会分类器如何观看，又在哪里失灵。
- 实现方式: 浏览器内的人脸属性分类器在玩家的摄像头上运行，每项零工任务都依据其输出实时打分。由 Mozilla 基金会资助。
- 视角: 分类、偏见与监控, 隐形劳动与攫取, 失败、故障与错误
- 图片: https://facework.app/assets/images/social-card.jpg
- 项目主页: https://facework.app
- 代码: https://github.com/kylemcdonald/facework

#### 氛围检测（Vibe Check） — Lauren Lee McCarthy, Kyle McDonald (2020)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 情绪识别把每一次相遇变成分数，展厅变成了一个小型社会信用系统。
- 作品内容: 展厅中的摄像头用人脸识别与表情分析记录每位观众在他人脸上引发的情绪。入口的屏幕列出最能引起快乐、厌恶、悲伤、惊讶或无聊的人，观众离开时可能发现自己也上了榜。
- 实现方式: 现成的人脸识别与表情分类器在多个摄像头之间追踪观众，把旁人的表情归因于他们正注视的人，并在屏幕上公布排名。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Real Feelings, HEK Basel 2020 (commissioned by HEK and MU)
- 视频: https://vimeo.com/488636450
- 图片: https://freight.cargo.site/w/1200/i/9d8ca3ebcda018fd8d992785901291c8e601d1a17ded09962faa0a6789609ae2/_DSC4566_1_crop.jpg
- 项目主页: https://get-lauren.net/Vibe-Check

#### 重新审视情绪表达：从人类面部动作推断情绪的挑战（Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements） — Lisa Feldman Barrett (2019)
- 类型: 论文 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 情绪识别 AI 检测到的是面部动作，而非感受；从前者推断后者正是最薄弱的一环。
- 作品内容: Barrett、Adolphs、Marsella、Martinez 与 Pollak 综述了 1000 多项研究，结论是：在不同情境与文化中，人们并不会为同一种情绪可靠地做出相同的面部动作，所以皱眉不能被直接读成愤怒。
- 实现方式: 系统综述成人、婴儿、儿童及偏远文化群体中，愤怒、厌恶、恐惧、快乐、悲伤与惊讶等面部构型的可靠性与特异性证据。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 论文: https://doi.org/10.1177/1529100619832930 (Psychological Science in the Public Interest 20(1))
- 项目主页: https://doi.org/10.1177/1529100619832930

#### 你如何看我？（How do you see me?） — Heather Dewey-Hagborg (2019)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 生成模型与潜空间
- 核心想法: 对机器而言算作“脸”的东西，对我们几乎认不出来。
- 作品内容: Dewey-Hagborg 用对抗式图像生成，制作出人脸检测器会认作“她的脸”的图像，而在人眼看来只是抽象的色块。
- 实现方式: 针对人脸检测与识别模型优化图像生成器，直到输出被识别为艺术家本人。
- 视角: 不透明与潜空间, 机器之眼
- 视频: https://vimeo.com/361593768
- 图片: https://www.deweyhagborg.com/media/pages/projects/how-do-you-see-me/9b1078df08-1643025907/heatherdeweyhagborg_kateelliott_01.jpg
- 项目主页: https://www.deweyhagborg.com/projects/how-do-you-see-me

#### 心灵（Mind） — Shinseungback Kimyonghun (2019)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 情绪 AI 被变成了天气：一个只有在机器测量时才存在的集体“心灵”。
- 作品内容: 情绪识别系统读取展厅里观众的面部表情，机械海浪鼓把最近 100 张脸的平均情绪转化为海浪声。大海随被检测到的群体情绪而变化。
- 实现方式: 网络摄像机配合 FER+ 情绪识别（ONNX Runtime），由微控制器驱动的机械海浪鼓与海面模拟。
- 视角: 分类、偏见与监控, 机器环世界
- 展出与获奖: National Museum of Modern and Contemporary Art, Korea (commission) 2019
- 视频: https://vimeo.com/364570360
- 图片: https://djhznh41oxwef.cloudfront.net/works/mind/ssbkyh_Mind_01.png
- 项目主页: https://ssbkyh.com/works/mind/

#### Perception iO — Karen Palmer (2019)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 作品像带偏见的系统读取嫌疑人那样读取观众，让人感受到谁的感知会变成后果。
- 作品内容: 观众以警察随身摄像头的视角进入一场紧张的遭遇，面对一位黑人和一位白人主角；眼动追踪与面部情绪分析读取观众反应，剧情按照观众的隐性偏见分岔。
- 实现方式: Tobii 眼动追踪与 AI 面部表情分析（与 ThoughtWorks Arts 合作开发）驱动一套分支叙事电影引擎。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Face Values, Cooper Hewitt, Smithsonian Design Museum, New York 2019–20; BIAS: Built This Way, Science Gallery Dublin 2021
- 视频: https://www.youtube.com/watch?v=Bfgmo05XdXM
- 图片: https://i0.wp.com/karenpalmer.uk/wp-content/uploads/2016/03/IMG_7016.jpg?fit=1200%2C750&ssl=1
- 项目主页: https://karenpalmer.uk/portfolio/perceptionio/

#### RASA-BOX — 龙星如 (2019)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 聊天机器人与语言模型
- 核心想法: 情绪推断把身体变成一段机器声称能读懂的文本。
- 作品内容: 一面“镜子”：用摄像头读取观众的身体姿态，推断其情绪状态，并写出一句同类情绪的句子，检验我们的感受还有多少私密可言。
- 实现方式: 摄像头骨骼数据经姿态估计输入情绪分类器与文本生成器；与 Hanbin Deng、Wu Tiancheng 合作完成。
- 视角: 分类、偏见与监控, 具身与动觉
- 展出与获奖: Ars Electronica Festival 2019
- 图片: https://ars.electronica.art/outofthebox/files/2019/08/RASABOX_Iris-Long.jpg
- 项目主页: https://ars.electronica.art/outofthebox/en/rasa-box/

#### 他们取走了被告与死者的面孔……（SD18）（They Took the Faces from the Accused and the Dead… (SD18)） — Trevor Paglen (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 人脸识别的基准测试建立在无法表示同意的人身上：被指控者、被关押者与死者。
- 作品内容: 由数千张嫌犯照片组成的网格，来自美国国家标准与技术研究院的 Special Database 18：这些逮捕照片（其中许多人已经去世）被提供给研究者，用于开发和测试人脸识别。
- 实现方式: 取自 NIST 嫌犯照片数据库（一个研究基准数据集），以颜料打印和大型墙面装置呈现。
- 视角: 分类、偏见与监控, 哀悼、记忆与来世
- 展出与获奖: Pace Gallery, Geneva, 2019; Uncanny Valley, de Young Museum, San Francisco, 2020
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-They_took_the_faces-2019_exhibition_view.jpg https://paglen.studio/wp-content/uploads/2020/05/Paglen-They_Took_the_Faces_2019-03.jpg
- 项目主页: https://paglen.studio/2020/04/09/they-took-the-faces-from-the-accused-and-the-dead/

#### 随机情绪串（Random String of Emotions） — Coralie Vogelaar (2018)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 把情绪 AI 的解码流程倒过来，暴露了它“六种基本情绪”的词汇有多单薄。
- 作品内容: 一位演员表演由“动作单元”随机组合而成的 200 个面部表情——动作单元是情绪识别软件所用的肌肉运动单位——随后商业软件尝试为每张奇特、有时近乎不可能的脸命名情绪。
- 实现方式: 电脑随机生成 FACS 动作单元序列，由演员学习并表演；拍下的片段交给 Noldus FaceReader 分析，读数在第二块屏幕上显示。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 视频: https://vimeo.com/331861983
- 图片: https://freight.cargo.site/w/1200/i/5a0df0b0e55f08e1ed9a2a99f301542141b7e8051d9ef693c50faf2b9b11c743/RANDOM_16-9-26-43.jpg
- 项目主页: https://www.coralievogelaar.com/Random-String-of-Emotions

#### 监控狗仔队（Surveillance Paparazzi） — Dries Depoorter (2018)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 狗仔的工作如今只需一个开放摄像头加一个分类器；人人都被拍摄，只有部分人被认出。
- 作品内容: 一台机器监看全球不设防的监控摄像头，用人脸识别“抓拍”恰好经过的名人，像一个自动化的狗仔。
- 实现方式: 抓取可公开访问、未加密的监控摄像头实时画面，并在其上运行名人人脸识别模型。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Entangled Realities, HEK Basel 2019
- 视频: https://www.youtube.com/watch?v=mS2tx3G7930
- 项目主页: https://driesdepoorter.be/

#### 正常化机器（The Normalizing Machine） — Mushon Zer-Aviv (2018)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据, 计算机视觉
- 核心想法: 算法偏见由我们自己的细小判断汇聚而成，再被藏进黑箱。
- 作品内容: 观众先被拍下面孔，再从之前参与者的列队中指出看起来“最正常”的人。机器把这些选择汇总成一幅算法化的“正常”肖像，呼应 19 世纪 Alphonse Bertillon 的“口述肖像”体系。
- 实现方式: 摄像头记录每位参与者；他们的指认为先前的面孔打上标签，机器学习模型把投票汇总成“面部正常度”的分布（软件由 Dan Stavy 与 Eran Weissenstern 以 openFrameworks 开发）。
- 视角: 分类、偏见与监控
- 展出与获奖: Ars Electronica ERROR exhibition, Berlin, 2018; BIAS: Built This Way, Science Gallery Dublin, 2021
- 视频: https://vimeo.com/323711041
- 图片: https://mushon.com/tnm/img/tnm_space.jpg https://mushon.com/tnm/img/tnm_cards.jpg
- 项目主页: https://mushon.com/tnm/

#### 它始于一场军事实验（It Began as a Military Experiment） — Trevor Paglen (2017)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 人脸识别建立在一些具体的人脸之上：他们成了这项技术的“亚当与夏娃”，却从未选择过这个身份。
- 作品内容: 从 FERET 数据库中挑选的十张肖像。FERET 是 1990 年代由 DARPA 资助的人脸库，照片主要来自马里兰一处军事基地的人员；作品同时印出人脸识别算法找到的关键点。
- 实现方式: 花数月从 FERET 数据库中挑选、修图并校色，再用人脸关键点算法处理；共 10 张颜料打印作品。
- 视角: 分类、偏见与监控, 机器之眼
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-It_Began-2017.jpg https://paglen.studio/wp-content/uploads/2020/05/Paglen-It_Began_2017-01-784x1024.jpg
- 项目主页: https://paglen.studio/2020/04/09/it-began-as-a-military-experiment/

#### 机器可读的 Hito（Machine Readable Hito） — Trevor Paglen (2017)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 人脸分析把一个熟悉的人变成一列列自信的猜测，而这些猜测在每张图之间彼此矛盾。
- 作品内容: 由数百张艺术家 Hito Steyerl 肖像组成的墙面，每张下方标注人脸分析算法对她年龄、性别、情绪、是否戴眼镜或有胡须的猜测。
- 实现方式: 数百张照片经多个商业与开源人脸分析分类器处理，结果印在每张图下方，以墙贴材料呈现。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Metro Pictures, New York, 2017
- 图片: https://paglen.studio/wp-content/uploads/2020/06/Paglen-Machine_readable_Hito-Metro.jpg https://paglen.studio/wp-content/uploads/2020/06/Paglen-Machine_Readable_Hito_detail-2-1-935x1024.jpg
- 项目主页: https://paglen.studio/2020/04/09/machine-readable-hito-and-holly/

#### 相面术的新衣（Physiognomy's New Clothes） — Blaise Agüera y Arcas (2017)
- 类型: 书与文章 · 机器: 监控与生物识别, 计算机视觉, 数据集与训练数据
- 核心想法: 用有偏见的照片训练出的分类器会学会这种偏见，再以客观“科学”的面目把它交还给我们。
- 作品内容: Blaise Agüera y Arcas、Margaret Mitchell 与 Alexander Todorov 合写的长文，剖析一篇 2016 年声称深度学习能从证件照中识别“犯罪性”的论文，并把这一想法追溯到龙勃罗梭与十九世纪的面相学。
- 实现方式: 一篇长篇批判文章，结合对所谓结果的机器学习分析（如数据集中表情、衣着的差异）与面相学和科学种族主义的历史。
- 视角: 分类、偏见与监控, 机器之眼
- 论文: https://medium.com/@blaisea/physiognomys-new-clothes-f2d4b59fdd6a (Medium, May 2017)
- 图片: https://miro.medium.com/v2/resize:fit:907/1*nhh283c26V1tYWjqH3UjXg.jpeg
- 项目主页: https://medium.com/@blaisea/physiognomys-new-clothes-f2d4b59fdd6a

#### 可能是切尔西（Probably Chelsea） — Heather Dewey-Hagborg (2017)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 一份基因组生成三十张可能的脸：DNA 并不决定一张脸，身份也无法从身体上直接读出。
- 作品内容: 三十张不同的 3D 打印面孔悬挂成人群，全部由算法根据同一份 DNA 生成：Chelsea Manning 从狱中寄出的口腔拭子与头发。作品与 Manning 合作完成，庆祝她 2017 年获释。
- 实现方式: 用法医表型推断方法分析 Manning 的 DNA；改变算法对同一基因数据的解读，得到 30 个面孔模型，彩色 3D 打印。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 展出与获奖: Fridman Gallery, New York 2017
- 视频: https://www.youtube.com/watch?v=A-EhRw11JiQ
- 图片: https://deweyhagborg.com/media/pages/projects/probably-chelsea/9769243e4c-1643025328/heatherdeweyhagborgchelseamanning_pap5596.jpg
- 项目主页: https://deweyhagborg.com/projects/probably-chelsea

#### 情绪英雄（Emotion Hero） — Ruben van de Ven (2016)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别
- 核心想法: 情绪识别读的不是感受，而是在训练人去表演它的分类。
- 作品内容: 一款吉他英雄风格的手机游戏：玩家按提示做出表情得分，之后还会收到如何更好地向机器“表达情绪”的反馈。
- 实现方式: 基于商业情绪识别 SDK（很可能是 Affectiva）的手机游戏，按其类别为表情打分。
- 视角: 分类、偏见与监控, 具身与动觉
- 图片: https://emotionhero.com/emotionhero.png
- 项目主页: https://rubenvandeven.com/emotionhero

#### 置信度（Level of Confidence） — 拉斐尔·洛萨诺-亨默 (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 原本用来寻找嫌疑人的监控算法，被转为寻找受害者的哀悼工具。
- 作品内容: 一台人脸识别摄像机把每位观众的脸与 2014 年在墨西哥伊瓜拉被绑架的 43 名学生的肖像比对，显示观众最像哪一位学生及其“置信度”。匹配永远不会成功，搜寻也永不停止。
- 实现方式: 以学生照片训练的 Eigenface、Fisherface 与 LBPH 人脸识别算法在摄像头与屏幕装置上运行；作品销售所得捐给学生所在的社区。
- 视角: 分类、偏见与监控, 哀悼、记忆与来世
- 展出与获奖: FOFA Gallery, Concordia University, Montreal 2015; Collection MUAC, Mexico City
- 视频: https://www.youtube.com/watch?v=sOCZLLgc1lQ
- 图片: https://www.lozano-hemmer.com/image_sets/level_of_confidence/montreal_2018/level_of_confidence_montreal_2018_glh_001.jpg
- 项目主页: https://www.lozano-hemmer.com/level_of_confidence.php

#### 变焦馆（Zoom Pavilion） — 拉斐尔·洛萨诺-亨默, 克日什托夫·沃迪奇科 (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 被人脸检测器挑出并放大，让公共监控这一日常经验突然变得私人。
- 作品内容: 在四周投影环绕的房间里，十二套计算机化监控系统检测观众的面孔，机器人摄像机把镜头放大到 35 倍，在人群全景与抽象特写之间切换，并记录陌生人之间的空间关系。
- 实现方式: 人脸检测软件驱动独立的机器人云台摄像机（最高 35 倍光学变焦），其画面投影在各面墙上。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: MUAC, Mexico City 2015; Art Basel Unlimited 2016
- 视频: https://www.youtube.com/watch?v=ENWBRsvn7qA
- 图片: https://www.lozano-hemmer.com/image_sets/zoom_pavilion/monterrey_2019/zoom_pavilion_monterrey_2019_my_505A7260.jpg
- 项目主页: https://www.lozano-hemmer.com/zoom_pavilion.php

#### 面部牢笼（Face Cages） — Zach Blas (2014)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 生物识别图形看起来抽象而中立；一旦用钢铁做出来戴在脸上，它就是一只牢笼。
- 作品内容: 四位酷儿艺术家各自戴上由自己面部生物识别图形制成的金属笼，在镜头前忍耐到疼痛显露。四频道影像把人脸识别干净的几何图形与被测量身体的不适并置。
- 实现方式: 为每位表演者生成人脸识别的特征点图形，以不锈钢 3D 打印，然后在耐力表演中佩戴，拍成四频道高清影像（12 分钟）。
- 视角: 分类、偏见与监控, 具身与动觉
- 展出与获奖: MUAC, Mexico City 2015; Sonic Acts, Amsterdam 2017; ICA Singapore 2017
- 视频: https://vimeo.com/161973235
- 图片: https://zachblas.info/wp-content/uploads/2013/08/FACECAGES-1-1024x576.jpg
- 项目主页: https://zachblas.info/works/face-cages/

#### Selfiecity — Lev Manovich, Moritz Stefaner (2014)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 用人脸分析解读文化，混合了机器估算与隐藏的人工判断。
- 作品内容: 对来自五座城市的 3200 张 Instagram 自拍进行交互分析，可按估算的年龄、性别、头部倾斜、微笑与情绪排序；这些数据由人脸分析软件与 Mechanical Turk 工人共同生成。
- 实现方式: Instagram 图像经 Mechanical Turk 工人筛选与标注，用人脸分析软件测量，并以交互可视化呈现。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 图片: http://selfiecity.net/assets/img/selfiecity-600.jpg
- 项目主页: http://selfiecity.net

#### 数据面具（Data-masks） — Sterling Crispin (2013)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 监控算法所说的“脸”，是一个没有人真正拥有的幽灵般的平均形状。
- 作品内容: 一组三维打印的尼龙面具，经过“演化”直到人脸检测与识别软件把它们认作人脸：机器想象中的人的肖像。
- 实现方式: 对人脸检测与识别算法进行逆向工程，用遗传算法演化出能被它们接受的形状，再三维打印出来（2013–2015）。
- 视角: 机器之眼, 他异与恐怖谷, 分类、偏见与监控
- 展出与获奖: GLOBALE: Infosphere, ZKM Karlsruhe 2015; Noorderlicht Photofestival 2015; The Face, Deutsches Hygiene-Museum Dresden 2017
- 视频: https://www.youtube.com/watch?v=qlwqQ8zqc5E
- 图片: https://www.sterlingcrispin.com/data-masks/data-masks_zkm_1.jpg https://www.sterlingcrispin.com/data-masks/data-mask_printed_lineup.jpg
- 项目主页: https://www.sterlingcrispin.com/data-masks.html

#### 数字空想性错视：Facebook 错误肖像个人索引（Digital Pareidolia: A Personal Index of Facebook's Erroneous Portraits） — Emilio Vavarella (2013)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 机器也会在云里看见人脸；它们的“空想性错视”揭示了脸对它们意味着什么。
- 作品内容: 艺术家从自己的 Facebook 中收集照片：平台的人脸检测框住了并不存在的脸——一个木结、一片阴影、墙上的花纹。
- 实现方式: 收集 Facebook 自动人脸标记框落在物体上的截图，编成索引。
- 视角: 失败、故障与错误, 分类、偏见与监控
- 图片: https://emiliovavarella.com/wp-content/uploads/2020/07/DIGITAL-PAREIDOLIA-1.jpg
- 项目主页: http://emiliovavarella.com/digital-pareidolia/

#### 陌生人影像（Stranger Visions） — Heather Dewey-Hagborg (2013)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 从数据预测出的面孔，是被当作肖像呈现的统计猜测，而这种猜测本身已是一种监控。
- 作品内容: Dewey-Hagborg 在纽约街头收集头发、嚼过的口香糖和烟头，提取 DNA，计算并 3D 打印出这些陌生人“可能长相”的真人大小彩色肖像，与样本及其发现地点一同展出。
- 实现方式: 在社区生物实验室提取并测序 DNA；与祖源、性别、眼睛和头发颜色相关的 SNP 输入自编软件，设定三维人脸模型的参数，再彩色打印成型。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: Ars Electronica Honorary Mention 2015; VIDA 15.0 special mention; Fotomuseum Winterthur; Science Gallery Dublin
- 视频: https://www.youtube.com/watch?v=kYhSYLXN-KA
- 图片: https://deweyhagborg.com/media/pages/projects/stranger-visions/d8bb0edf45-1643025614/wall_of_faces.jpg https://deweyhagborg.com/media/pages/projects/stranger-visions/83ebebdc4a-1643025584/sample4_face_web.jpg
- 项目主页: https://deweyhagborg.com/projects/stranger-visions

#### us+ — Lauren Lee McCarthy, Kyle McDonald (2013)
- 类型: 研究原型 · 机器: 监控与生物识别, 语音与听觉机器, 计算机视觉
- 核心想法: 当软件通过读取我们的表情和话语来“改善”对话时，它也在决定什么才算好的对话。
- 作品内容: 一个 Google Hangout 应用，在视频通话中聆听并观察双方，为每个人的用词和面部表情打分，弹出“别再谈你自己了”之类的建议；对话失衡时会自动把某人静音。
- 实现方式: 基于 LIWC 词库与“语言风格匹配”理论的音频、面部表情与语言分析，驱动 Google Hangouts 中的实时可视化、提醒与自动静音。
- 视角: 分类、偏见与监控, 亲密、照护与陪伴
- 视频: https://vimeo.com/81903116
- 图片: https://freight.cargo.site/i/ad160b0c7b6e9061fcbc3bbda3fb065202d10e85f700d065098d874b49761367/_01-copy.jpg
- 项目主页: https://get-lauren.net/us

#### 保全面子（Saving Face） — Lancel & Maat (2011)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 触摸把人脸识别从身份核验变成了一种共享亲密的姿态。
- 作品内容: 观众在摄像头前抚摸自己的脸；人脸识别追踪触摸，一笔一笔地把其肖像与先前观众的脸融合，在大屏上形成一张共享的合成面孔。
- 实现方式: 摄像头与人脸追踪软件把观众触摸的面部区域映射到已存肖像的合成图像上。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 视频: https://vimeo.com/28499178
- 项目主页: https://lancelmaat.nl/work/saving-face/

#### 茄子（Cheese） — Christian Moeller (2003)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 一台给“真诚”打分的机器，把微笑变成了令人筋疲力尽的劳动。
- 作品内容: 六位女演员面对摄像机尽可能长时间地保持微笑，最长约一个半小时；情绪识别软件实时打分，一旦“快乐程度”下降，警报便提醒她们笑得更真诚些。
- 实现方式: 多屏影像装置；一套情绪识别系统（很可能是当时的研究原型）实时分析每张脸，“快乐值”低于阈值即触发警报。
- 视角: 分类、偏见与监控, 具身与动觉
- 视频: https://vimeo.com/42719594
- 图片: https://payload.cargocollective.com/1/7/229866/4243042/67-1.jpeg https://payload.cargocollective.com/1/7/229866/4243042/40-1.jpeg
- 项目主页: https://christianmoeller.com/Cheese

### 对抗与躲避

用伪装、对抗图样等策略躲避或迷惑机器感知。

#### 如何（不）被自动驾驶汽车撞上（How (not) to get hit by a self-driving car） — 木原共, Daniel Coppen (2023)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 每一次成功的“骗过”都是汽车会漏看的边缘案例，暴露出训练数据看不见的是谁。
- 作品内容: 一件游戏装置：玩家要穿过一条虚拟街道而不被自动驾驶汽车的行人检测器发现，为此想办法伪装自己、压低检测分数。
- 实现方式: 摄像头把画面送入行人检测模型，实时为每位玩家打分；获胜者可选择把这些边缘案例数据捐出改进模型，或将其删除。
- 视角: 机器之眼, 分类、偏见与监控, 失败、故障与错误
- 展出与获奖: Playable City Sandbox, Watershed Bristol 2023; S+T+ARTS Prize 2024, Honorary Mention
- 视频: https://vimeo.com/883161343
- 图片: https://www.tomokihara.com/images/how-not-to-main2.jpg https://www.tomokihara.com/images/how-not-to_01-low-res.jpg
- 项目主页: https://www.tomokihara.com/en/how-not-to-get-hit-by-a-self-driving-car.html

#### 宣言系列（Manifesto Collection） — Cap_able (2022)
- 类型: 产品与平台 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 对抗样本可以被织出来：机器的弱点变成一件你可以选择穿上的衣服。
- 作品内容: 一系列针织毛衣、长裤和连衣裙，织入的图案会让 AI 检测器把穿着者标注成动物或物体，而不是人。
- 实现方式: 针对实时目标检测器（很可能是 YOLO 一类）优化的对抗图案，用电脑针织机织入衣物；意大利生产。
- 视角: 机器之眼, 分类、偏见与监控, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=ZGp9bZpD6Rg
- 图片: https://www.capable.design/cdn/shop/files/preview_images/165dc7bd8cca4ddf9ae24f09c1d01543.thumbnail.0000000000_1100x.jpg?v=1705938416 https://www.capable.design/cdn/shop/files/2_8fdbe483-952c-4bd6-a392-01d11de373bc.png?v=1695084551&width=1200
- 项目主页: https://www.capable.design/pages/technology

#### 忘却语言（Unlearning Language） — Lauren Lee McCarthy, Kyle McDonald (2022)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 计算机视觉, 监控与生物识别
- 核心想法: 躲避机器感知，成了重新发现人类交流中最“人性”部分的方法。
- 作品内容: 最多八位参与者由一个“想训练人类不那么像机器”的 AI 引导：一旦它检测到他们的语音、手势或表情，就用光、声音和振动加以干预，于是大家必须发明它检测不到的交流方式，比如哼唱、拍手或改变音高。
- 实现方式: 房间中的摄像头与麦克风运行语音检测、手势识别与表情检测，并触发灯光、声音与触觉反馈；与山口情报艺术中心（YCAM）合作完成。
- 视角: 机器之耳与声, 分类、偏见与监控, 能动、自主与共创
- 展出与获奖: Yamaguchi Center for Arts and Media (YCAM) 2022
- 视频: https://www.youtube.com/watch?v=6APHL4CJAQ8
- 图片: https://freight.cargo.site/w/1200/i/064b679d339d01a58666ee7c0e4ae9bde01b984f474c81e73f5d7340f592be46/opening-performance0.jpeg
- 项目主页: https://get-lauren.net/Unlearning-Language

#### 躲避人脸识别的技巧（A Technique of Evading Face Detection） — 郭城 (2020)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 躲避机器视觉可以是一种身体技巧：一小段荒诞的面部编舞。
- 作品内容: 一段一本正经的教程：艺术家以恰好的角度转动、扭曲头部，让人脸检测器跟丢他。
- 实现方式: 艺术家用常见人脸检测算法测试各种头部姿态，并记录检测失败的瞬间。
- 视角: 机器之眼, 分类、偏见与监控
- 图片: https://cdn.guo-cheng.net/files/projectImg/ATechniqueOfEvadingFaceDetection/ATechniqueOfEvadingFaceDetection_1.jpg
- 项目主页: https://guo-cheng.net/index.php/works/a-technique-of-evading-face-detection/

#### 谷歌地图黑客（Google Maps Hacks） — Simon Weckert (2020)
- 类型: 表演、舞蹈与音乐 · 机器: 平台与推荐算法, 基础设施、能源与供应链
- 核心想法: 平台是通过代理信号来感知城市的；骗过代理，地图就会跟着变，随后交通也会跟着变。
- 作品内容: 艺术家拉着装有 99 部二手智能手机的手推车走过柏林街道，空荡荡的街道在 Google Maps 上变成红色的“虚拟拥堵”。
- 实现方式: 每部手机都开着 Google Maps 导航，99 台缓慢移动的设备所发出的位置数据被系统读成交通拥堵。
- 视角: 失败、故障与错误, 能动、自主与共创
- 展出与获奖: Japan Media Arts Festival 2021, Social Impact Award
- 视频: https://www.youtube.com/watch?v=k5eL_al_m7Q
- 图片: http://www.simonweckert.com/img/googlemapshacks/3.JPG http://www.simonweckert.com/img/googlemapshacks/2.JPG
- 项目主页: http://www.simonweckert.com/googlemapshacks.html

#### Mask.ID — Peng! Collective (2018)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 生成模型与潜空间
- 核心想法: 一张生物识别护照照片可以同时属于两个人。
- 作品内容: Peng! 的一名成员把自己的脸与欧盟外交与安全政策高级代表 Federica Mogherini 的脸融合，用这张合成照片申请到一本真实的德国护照；行动呼吁公民效仿，以帮助难民出行。
- 实现方式: 人脸融合软件混合两张脸，直到人脸识别能同时匹配二者；照片通过正常护照申请提交。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 图片: https://pen.gg/wp-content/uploads/2018/09/MaskID_Kabine_1_Melber-1800x1200.jpg
- 项目主页: https://pen.gg/campaign/mask-id-2/

#### 非人脸肖像（Nonfacial Portrait） — Shinseungback Kimyonghun (2018)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 肖像画变成一次寻找“只有人能看见”的狭窄视觉空间的实验。
- 作品内容: 邀请画家绘制一幅人能认出、但任何人脸检测算法都找不到人脸的肖像。摄像机持续监看画布，一旦检测到人脸，屏幕就会提醒画家。
- 实现方式: 三种人脸检测算法通过摄像机监看画布；每幅画与其创作过程的录像一起展出。
- 视角: 机器之眼, 分类、偏见与监控, 能动、自主与共创
- 展出与获奖: NTT InterCommunication Center (ICC), Tokyo
- 视频: https://vimeo.com/290710439
- 图片: https://djhznh41oxwef.cloudfront.net/works/nonfacial_portrait/ssbkyh_Nonfacial_Portrait_00.png
- 项目主页: https://www.ntticc.or.jp/en/archive/works/nonfacial-portrait/

#### 感知引擎（Perception Engines） — Tom White (2018)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 艺术可以为机器之眼而作：这些版画显示，对分类器来说几笔就“够了”。
- 作品内容: 一组抽象版画：人只看到几笔色块，ImageNet 分类器却会自信地把它们认作大提琴、卷心菜、双髻鲨或熨斗。
- 实现方式: 用一个受限的绘图系统针对一组 ImageNet 分类器进行优化，结果以孔版印刷和丝网印刷呈现。
- 视角: 机器之眼, 不透明与潜空间
- 图片: http://static1.squarespace.com/static/5c3518f55cfd7963746dd576/t/5cfed9300e5c0200015a2735/1560205650916/tom_white_electric_fan_2019+%281%29.jpg?format=1500w https://images.squarespace-cdn.com/content/v1/5c3518f55cfd7963746dd576/1609721536034-7SU963UJO2QP104FXYBO/cello_16_095_240_thumbnail.jpg
- 项目主页: https://drib.net/perception-engines

#### 针对深度学习视觉分类的鲁棒物理世界攻击（Robust Physical-World Attacks on Deep Learning Visual Classification） — Kevin Eykholt (2018)
- 类型: 论文 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 在司机眼中像涂鸦的东西，却能为自动驾驶汽车改写道路。
- 作品内容: 在真实的停车标志上贴几块黑白贴纸，就能让交通标志分类器在多种距离和角度下把它读成“限速 45 英里”标志。
- 实现方式: “鲁棒物理扰动”（RP2）算法在多种物理条件下优化贴纸式扰动，并在实验室与车载行驶测试中验证（Eykholt 等，CVPR 2018）。
- 视角: 机器之眼, 失败、故障与错误
- 论文: https://doi.org/10.1109/CVPR.2018.00175 (CVPR 2018)
- 项目主页: https://doi.org/10.1109/CVPR.2018.00175
- 代码: https://github.com/evtimovi/robust_physical_perturbations

#### 对抗贴片（Adversarial Patch） — Tom B. Brown (2017)
- 类型: 论文 · 机器: 计算机视觉
- 核心想法: 机器的注意力可以被劫持：一块醒目的补丁就能压倒整个场景。
- 作品内容: Google Brain 的研究者制作了一张可打印的迷幻贴纸，把它放在香蕉旁边，图像分类器就只看到一台“烤面包机”。
- 实现方式: 针对 Inception 等 ImageNet 分类器，在大量图像、位置和尺度上优化出一个与场景无关的通用补丁（Brown、Mané、Roy、Abadi、Gilmer）。
- 视角: 机器之眼, 失败、故障与错误, 不透明与潜空间
- 论文: https://arxiv.org/abs/1712.09665 (arXiv 2017 (NIPS 2017 Workshop))
- 视频: https://www.youtube.com/watch?v=i1sp4X57TL4
- 项目主页: https://arxiv.org/abs/1712.09665

#### 自动驾驶陷阱 001（Autonomous Trap 001） — James Bridle (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 一台服从所见符号的机器，也能被这些符号困住，就像魔法阵中的精灵。
- 作品内容: 艺术家在帕纳索斯山上，用盐在一辆自动驾驶汽车周围画出道路标线：虚线让它开进来，实线却禁止它离开。
- 实现方式: 用盐画出带虚线和实线车道标记的圆圈，困住运行艺术家自制自动驾驶软件的汽车；2017 年 3 月 14 日完成表演。
- 视角: 机器之眼, 失败、故障与错误, 机器环世界
- 展出与获奖: Entangled Realities, HEK Basel 2019; AI: Who's Looking After Me?, Science Gallery London 2023
- 图片: https://jamesbridle.com/media/pages/works/autonomous-trap-001/329e6817a6-1680515123/1-autonomous-trap-001-003.jpg https://jamesbridle.com/media/pages/works/autonomous-trap-001/7f4c4c6acb-1680515123/autonomous-trap-001-001.jpg
- 项目主页: https://jamesbridle.com/works/autonomous-trap-001

#### HyperFace — Adam Harvey (2017)
- 类型: 思辨设计 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 与其藏起一张脸，不如让机器被只有它自己看得见的脸淹没。
- 作品内容: 一种布料印花，图案会被人脸检测器读成许多张“假脸”，从而降低旁边真实人脸的置信度。
- 实现方式: 图案依据人脸检测算法判为“脸”的特征生成；与 Hyphen-Labs 合作，为 NeuroSpeculative AfroFeminism 项目开发。
- 视角: 机器之眼, 分类、偏见与监控, 失败、故障与错误
- 展出与获奖: 33C3 Hamburg 2016; Sundance Film Festival 2017 (NeuroSpeculative AfroFeminism)
- 视频: https://www.youtube.com/watch?v=LLKmyY5ujeU
- 图片: https://adam.harvey.studio/hyperface/hyperface_adam_harvey_hyphen_labs_01.webp https://adam.harvey.studio/hyperface/scarf_detections_960.webp
- 项目主页: https://adam.harvey.studio/hyperface/

#### 可穿戴人脸投影仪（Wearable Face Projector） — Jing-cai Liu (2017)
- 类型: 思辨设计 · 机器: 监控与生物识别
- 核心想法: 对抗人脸识别的一种答案，是戴上别人的脸。
- 作品内容: 一个头戴式微型投影仪，把另一个人的脸投射到佩戴者脸上，以迷惑公共空间中的人脸与情绪识别。
- 实现方式: 装在头戴支架上的小型投影仪把人脸视频投到佩戴者脸上；设计原型与影片。
- 视角: 分类、偏见与监控, 具身与动觉
- 视频: https://www.youtube.com/watch?v=_PoudPCevN0
- 图片: http://jingcailiu.com/wp-content/uploads/2020/06/Wearable-face-projector-21may2020-scaled-e1592083294514-1024x340.jpg
- 项目主页: http://jingcailiu.com/wearable-face-projector/

#### 配饰作案（Accessorize to a Crime） — Mahmood Sharif (2016)
- 类型: 论文 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 脸上几厘米的图案，就能左右一套人脸识别系统。
- 作品内容: 卡内基梅隆大学的研究者打印出彩色眼镜框，戴上后就能躲过人脸识别系统，或被识别成另一个人，比如某位名人。
- 实现方式: 只在眼镜框区域内优化对抗扰动，使其平滑且可打印，并在现实中针对深度网络人脸识别和 Face++ 测试（ACM CCS 2016；Sharif、Bhagavatula、Bauer、Reiter）。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 论文: https://doi.org/10.1145/2976749.2978392 (ACM CCS 2016)
- 视频: https://www.youtube.com/watch?v=6Xh1vuwnVhU
- 项目主页: https://doi.org/10.1145/2976749.2978392

#### 隐藏语音命令（Hidden Voice Commands） — Nicholas Carlini (2016)
- 类型: 论文 · 机器: 语音与听觉机器
- 核心想法: 聆听机器听到的与我们听到的并不相同；人与机器听觉之间的落差，正是命令可以藏身的地方。
- 作品内容: 安全研究：Google Now 等语音识别系统可以被对人耳而言只是噪声的音频所操控；论文包括针对商用助手的黑盒攻击与防御研究。
- 实现方式: 反复扭曲语音特征（MFCC），使识别器仍能解码出指令，而用户研究中的人类听者却听不懂；针对 Google Now 与开源识别器进行测试。
- 视角: 机器之耳与声, 失败、故障与错误
- 论文: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/carlini (USENIX Security 2016)
- 视频: https://www.youtube.com/watch?v=x4bqJh4wyjU
- 项目主页: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/carlini

#### 深度神经网络很容易被愚弄（Deep Neural Networks are Easily Fooled） — Evolving AI Lab (2015)
- 类型: 论文 · 机器: 计算机视觉
- 核心想法: 分类器的“确信”不等于看见：它识别的是特征，不是事物。
- 作品内容: Anh Nguyen、Jason Yosinski 与 Jeff Clune 演化出一批图像，从雪花噪点到抽象图案，最先进的分类器却以超过 99% 的置信度把它们认作王企鹅、海星或棒球。
- 实现方式: 用进化算法和梯度上升生成图像，使在 ImageNet 与 MNIST 上训练的卷积网络对某一类别的得分最大化（CVPR 2015）。
- 视角: 机器之眼, 不透明与潜空间, 失败、故障与错误
- 论文: https://doi.org/10.1109/CVPR.2015.7298640 (CVPR 2015)
- 视频: https://www.youtube.com/watch?v=M2IebCN9Ht4
- 项目主页: https://arxiv.org/abs/1412.1897

#### URME 监控（URME Surveillance） — Leo Selvaggio (2014)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 如果系统只会匹配人脸，那么许多身体共用一张脸，就会让它的记录失去意义。
- 作品内容: 艺术家出售一副照片般逼真的三维打印“自己的脸”；任何人戴上它走过人脸识别摄像头，都会被识别为 Leo Selvaggio。
- 实现方式: 根据艺术家面部三维扫描制作的树脂义面，通过 Indiegogo 众筹发布，并配有人脸追踪镜面装置展出。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 视频: https://vimeo.com/90828804
- 图片: https://images.squarespace-cdn.com/content/v1/50394738e4b0117733940e2f/1393480618366-370KZW8USCHO8HDKTMXI/Prosthetic+Comparison.jpg https://images.squarespace-cdn.com/content/v1/50394738e4b0117733940e2f/1458091446574-1JNPSCUTUT0O9VQRD64Z/URME+maskFLAT.jpg
- 项目主页: https://www.leoselvaggio.com/urmesurveillance

#### 如何不被看见：一段该死的说教视频文件（How Not to Be Seen: A Fucking Didactic Educational .MOV File） — 黑特·史德耶尔 (2013)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 被看见与否取决于分辨率；隐身可以是对抗机器视觉的策略，但也正是穷人与失踪者被抹去的方式。
- 作品内容: 一部冷面幽默的教学影片，用五课教你如何在高分辨率相机、卫星和航拍目标的世界里消失：大隐于市、变得比一个像素还小、住进封闭社区，或者成为 50 岁以上的女人。
- 实现方式: 部分拍摄于加州沙漠中一处废弃的航拍校准靶标，混合绿幕表演、三维动画与对教学录像的戏仿。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: 55th Venice Biennale, Il Palazzo Enciclopedico (2013)
- 视频: https://www.youtube.com/watch?v=kKAKgrZZ_ww
- 图片: https://www.artforum.com/wp-content/uploads/2015/04/preview00-4.jpg
- 项目主页: https://www.artforum.com/video/hito-steyerl-how-not-to-be-seen-a-fucking-didactic-educational-mov-file-2013-51651/

#### 隐身服（Stealth Wear） — Adam Harvey (2013)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机, 监控与生物识别
- 核心想法: 当机器用热量去看，隐私就变成了衣服向外辐射什么的问题。
- 作品内容: 一组防无人机的连帽衫、头巾和罩袍，用镀银面料遮挡人体热量，让头顶的热成像相机看不到穿着者。
- 实现方式: 服装用能反射热辐射的镀银合成面料缝制，并用 FLIR 热成像相机测试。
- 视角: 机器之眼, 分类、偏见与监控, 具身与动觉
- 展出与获奖: Tank Magazine HQ, London 2013
- 图片: https://adam.harvey.studio/stealth-wear/stealth-wear-poster.webp https://adam.harvey.studio/stealth-wear/anti-drone-hoodie-f.webp
- 项目主页: https://adam.harvey.studio/stealth-wear/

#### 面部武器化套件（Facial Weaponization Suite） — Zach Blas (2012)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 不透明可以是集体的：一张属于许多人的脸，是机器无法识别的脸。
- 作品内容: Blas 组织社区工作坊，扫描参与者的面孔并把数据融合成无定形、色彩鲜艳的“集体面具”，人脸识别无法读取它们。面具被用于公共行动，也出现在影片《Facial Weaponization Communiqué: Fag Face》中。
- 实现方式: 参与者的面部被三维扫描，生物特征数据在建模软件中聚合，再制成可佩戴的面具；其中“Fag Face Mask”回应了声称可从面孔判断性取向的研究。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Workshops and public actions in Los Angeles, San Diego, New York and Mexico City, 2012–14
- 视频: https://vimeo.com/57882032
- 图片: https://zachblas.info/wp-content/uploads/2013/01/FWS-2-1024x576.jpg
- 项目主页: https://zachblas.info/works/facial-weaponization-suite/

#### CV 炫目迷彩（CV Dazzle） — Adam Harvey (2010)
- 类型: 思辨设计 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: “脸”是检测器模板所规定的样子；针对模板去设计，就把模板暴露了出来。
- 作品内容: 一套由大胆妆容和不对称发型组成的伪装策略，打散人脸检测器寻找的特征：人仍然看得见佩戴者，算法却看不见。
- 实现方式: 造型针对 OpenCV 中的 Viola-Jones Haar 级联人脸检测器设计并测试（2020 年的新造型则针对卷积神经网络人脸识别）。
- 视角: 机器之眼, 分类、偏见与监控, 失败、故障与错误
- 展出与获奖: NYU ITP thesis 2010; The New York Times Op-Art 2013; Designs for a Different Future 2020
- 视频: https://vimeo.com/12774628
- 图片: https://adam.harvey.studio/cvdazzle/cvd-look1.webp https://adam.harvey.studio/cvdazzle/cvdazzle-06-copyright-adam-harvey-2020.webp https://adam.harvey.studio/cvdazzle/cvdazzle-05-saliency-map.webp
- 项目主页: https://adam.harvey.studio/cvdazzle/

#### 像素头（Pixelhead） — Martin Backes (2010)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 马赛克这种屏幕上的匿名符号，可以被穿在身上。
- 作品内容: 一顶印着马赛克人脸的全脸头套，让佩戴者无法在网上照片中被识别或自动标记。
- 实现方式: 印花织物面罩，通过遮蔽面部特征点使人脸检测失效。
- 视角: 分类、偏见与监控, 具身与动觉
- 图片: https://www.martinbackes.com/wordpress/wp-content/uploads/2013/03/martinbackes_web4.jpg
- 项目主页: https://www.martinbackes.com

## 机器身体与行为

作为身体的机器人与动态机器：它们在我们面前移动、反应、表演、疲惫与失败。

### 控制论生物

1940–70 年代以来，靠反馈回路表现得像有生命的机器。

#### Senster（The Senster） — Edward Ihnatowicz (1970)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 害羞比顺从更像活物：机器的退缩让观众改变了自己的行为。
- 作品内容: 一只 4 米高、像长颈龙虾钳的液压生物，安装在埃因霍温飞利浦 Evoluon 科技馆，会把“头”伸向轻柔的声音和缓慢的动作，而躲开喧哗和突然的手势。观众对它喊叫，又静静等它靠近。
- 实现方式: 一台飞利浦 P9201 计算机处理头部四个麦克风和两个多普勒雷达传感器的输入，驱动仿照龙虾钳设计的六个电液伺服关节。
- 视角: 具身与动觉, 他异与恐怖谷, 机器之耳与声
- 展出与获奖: Philips Evoluon, Eindhoven 1970–1974; Nieuwe Instituut, Rotterdam (restored)
- 视频: https://www.youtube.com/watch?v=1jDt5unArNk
- 图片: https://upload.wikimedia.org/wikipedia/commons/1/14/Edward_Ihnatowicz%2C_The_Senster_%2853386590223%29.jpg https://upload.wikimedia.org/wikipedia/commons/4/45/Edward_Ihnatowicz%2C_The_Senster_%2853386711664%29.jpg
- 项目主页: http://www.senster.com/

#### 动态雕塑的对话（Colloquy of Mobiles） — Gordon Pask (1968)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 机器可以被演成一场欲望对话中的伙伴，而人只是这场对话里又多出来的一个参与者。
- 作品内容: 五件悬挂的活动装置，三件“雌性”、两件“雄性”，用光束和声音互相求偶，并学会怎样的接近能让对方“满足”。观众拿着镜子和手电筒也可以加入，改变机器欲望的方向。
- 实现方式: 装有灯、镜子和光电管的旋转玻璃钢身体，由会积累与释放的“驱力”带动电机；每件装置根据其他装置的回馈信号调整行为。
- 视角: 能动、自主与共创, 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Cybernetic Serendipity, ICA London 1968; Centre Pompidou reconstruction 2020
- 视频: https://www.youtube.com/watch?v=RlXDL8Ab0oQ
- 项目主页: https://cyberneticserendipity.net/

#### 控制论雕塑（Cybernetic Sculpture） — 蔡文颖 (1968)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 声音、光与振动之间的反馈，让钢雕塑看上去在倾听与回应。
- 作品内容: 一丛细长的不锈钢杆在马达底座上振动，由频闪灯照亮；观众拍手或说话时，频闪频率改变，钢杆看起来会静止、摇摆或起舞。
- 实现方式: 马达以固定频率振动钢杆，声控反馈电路改变频闪频率，产生频闪运动效果。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Howard Wise Gallery, New York 1968
- 图片: https://upload.wikimedia.org/wikipedia/commons/7/75/Tsai_cyberneticsculpture79.jpg https://upload.wikimedia.org/wikipedia/commons/f/f1/Tsai_tuningfork1974.jpg
- 项目主页: https://en.wikipedia.org/wiki/Wen-Ying_Tsai

#### SAM（声控动态雕塑）（SAM (Sound Activated Mobile)） — Edward Ihnatowicz (1968)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 语音与听觉机器
- 核心想法: “转过头去听”是最简单的注意姿态，这就足以让一台机器看起来像是“某个人”。
- 作品内容: 一个像花一样的玻璃钢“头”，装在可弯曲的铝制“颈”上，会转向附近说话或发出声音的人，仿佛在倾听。
- 实现方式: 头部的四个麦克风比较声音强弱；小型液压活塞推动“颈椎”转向声音最响的方向。
- 视角: 机器之耳与声, 具身与动觉, 他异与恐怖谷
- 展出与获奖: Cybernetic Serendipity, ICA London 1968
- 视频: https://www.youtube.com/watch?v=8b52qpyV__g
- 图片: https://upload.wikimedia.org/wikipedia/commons/e/ee/Sound_Activated_Mobile.jpg
- 项目主页: http://www.senster.com/ihnatowicz/

#### 机器人 K-456（Robot K-456） — 白南准, 阿部修也 (1964)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 一个笨拙、嘈杂、有身体机能的机器人，更像街头艺人，而不是技术进步的象征。
- 作品内容: 1964 年在东京制作的 20 通道无线电遥控类人机器人，在街上行走、播放肯尼迪演讲录音，还会“排泄”豆子。它首次亮相于 1964 年纽约前卫艺术节上白南准的《机器人歌剧》。
- 实现方式: 由工程师阿部修也制作的金属骨架、电机与 20 通道无线电遥控系统；现藏白南准艺术中心（1964/1996），2025 年完成修复。
- 视角: 具身与动觉, 他异与恐怖谷, 失败、故障与错误
- 展出与获奖: Robot Opera, 2nd Annual New York Avant Garde Festival 1964; Nam June Paik: Becoming Robot, Asia Society 2014; Nam June Paik Art Center (collection)
- 视频: https://www.youtube.com/watch?v=JciiqCsRhdY
- 项目主页: https://en.wikipedia.org/wiki/Nam_June_Paik

#### 霍普金斯野兽（The Hopkins Beast） — Johns Hopkins Applied Physics Laboratory (1962)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一台整个世界都围绕“觅食”这一个需求组织起来的机器，看起来已经像动物了。
- 作品内容: 一台轮式自动机独自在实验室白色走廊里游荡，电池快没电时就寻找黑色的墙上插座，自己插上充电。后来的版本用声呐避开行人、识别门和楼梯。
- 实现方式: 不用计算机，只用晶体管逻辑，把触碰开关、声呐和（二型中的）识别深色插座的光学传感器，连到履带、沿墙探臂和可伸出的插头上。
- 视角: 具身与动觉, 机器环世界, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=zMpEeag7kkM
- 图片: https://upload.wikimedia.org/wikipedia/commons/3/3e/00-01964_APL_66196_001_The_Beast.jpg
- 项目主页: https://en.wikipedia.org/wiki/Johns_Hopkins_Beast

#### CYSP 1 — Nicolas Schöffer (1956)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 第一件拥有感官和“神经系统”的雕塑，让艺术品变成会反应的主体，而不是被观看的物件。
- 作品内容: 一座由钢和铝板组成的塔立在带轮底座上，会随周围的光、颜色和声音转动、旋转彩色叶片并在地面上移动。1956 年，它在马赛“光辉城市”屋顶上与 Maurice Béjart 的舞者同台演出。
- 实现方式: 光电管和麦克风把信号送入与飞利浦合作制作的电子“大脑”，驱动带轮底座中的电机和旋转板；兴奋或平静取决于外部刺激。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Cité radieuse, Marseille 1956; Artistes & Robots, Grand Palais 2018
- 视频: https://www.youtube.com/watch?v=u8nxktU1R6E
- 项目主页: https://en.wikipedia.org/wiki/Nicolas_Sch%C3%B6ffer

#### 忒修斯（走迷宫的机械鼠）（Theseus (maze-solving mouse)） — Claude Shannon (1950)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 学习被演成迷宫里一个小身体的动作，尽管它的“大脑”其实是地板下一排电话继电器。
- 作品内容: 一只磁性玩具老鼠由桌下的继电器驱动，在可以重新布置的迷宫里试错探索，记住路线，然后径直跑到“奶酪”那里。迷宫一改，它就重新学习。
- 实现方式: 约 75 个电话继电器为 25 格迷宫中的每一格记下上次走出去的方向；板下一辆电动小车上的磁铁拖动老鼠。
- 视角: 能动、自主与共创, 具身与动觉
- 视频: https://www.youtube.com/watch?v=_9_AEVQ_p74
- 项目主页: https://en.wikipedia.org/wiki/Claude_Shannon

#### 思索机械（埃尔默与艾尔西）（Machina speculatrix (Elmer and Elsie)） — W. Grey Walter (1949)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 两个“神经元”加上一个在房间里的身体，就足以产生被人读作好奇、饥饿和自我识别的行为。
- 作品内容: 两只装有光传感器和触碰开关的三轮小“乌龟”在房间里游走：趋向柔和的光，躲开强光和障碍物，电量不足时回到有灯的小窝充电。在壳上装一盏灯后，乌龟会对镜中的自己或另一只乌龟起反应，好像能认出自己。
- 实现方式: 用两只电子管“神经元”组成的模拟电路，把旋转光电管和外壳触碰开关连接到转向和驱动电机；行为来自身体与环境之间的反馈。
- 视角: 具身与动觉, 能动、自主与共创, 机器环世界
- 展出与获奖: Festival of Britain, London 1951
- 视频: https://www.youtube.com/watch?v=wQE82derooc
- 图片: https://upload.wikimedia.org/wikipedia/commons/e/e5/Cybernetic_Tortoise_by_William_Grey_Walter_c_1950_%28Ank_Kumar%29.jpg https://upload.wikimedia.org/wikipedia/commons/7/77/Replica_of_Grey_Walter%27s_tortoise_%283572415081%29.jpg
- 项目主页: https://en.wikipedia.org/wiki/Turtle_(robot)

### 人工生命与机器群体

不断演化的智能体、机器群与自组织的机器生态。

#### Lasermice — 菅野创 (2018)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 让机器网络的交流变得可见、可听，就能看到集体行为是如何形成的。
- 作品内容: 由 60 台小型机器人组成的群体，它们用激光和光电探测器互相“交谈”并敲击地面，在没有中央控制的情况下涌现出萤火虫般的同步节奏。
- 实现方式: 每台机器人带有激光器、光电探测器和电磁敲击器；受萤火虫启发的脉冲耦合振子规则让它们同步。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: Ars Electronica 2019; 22nd Japan Media Arts Festival, Excellence Award 2019; Biennale Nemo, Paris 2019
- 视频: https://www.youtube.com/watch?v=4afSgcWleFo
- 图片: https://www.kanno.so/wp-content/uploads/2021/05/lasermice_by_Quentin_Chevrier_2-copy.jpg
- 项目主页: https://www.kanno.so/project/lasermice

#### 重新拼合（Putting the Pieces Back Together Again） — Ralf Baecker (2018)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 秩序在一片简单机器中出现又消散，自组织被显现为运动。
- 作品内容: 由 1250 个小步进电机组成的阵列，每个电机转动一根白色短杆，形成一个表面；电机与相邻电机彼此对齐又互相扰动，波纹、簇团和群体般的图案在表面上流过。
- 实现方式: 每个电机是一个耦合振子或类自旋模型中的单元；实时计算的局部相互作用规则决定每根杆的角度（为 Drehmoment 艺术节在一座旧报社大楼中委托创作）。
- 视角: 能动、自主与共创, 不透明与潜空间
- 展出与获奖: Drehmoment, KulturRegion Stuttgart, Kirchheim unter Teck 2018
- 视频: https://www.youtube.com/watch?v=8GtFttw8z9U
- 项目主页: https://rlfbckr.io/project/ptpbta/

#### 逐光者（Lichtsuchende） — Dave Murray-Rust, Rocio von Jungenfeld (2015)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 只要给机器一种共享资源和一条交流通道，类似社会行为的东西就会出现，而且以光的形式让我们看得见。
- 作品内容: 一群形似向日葵的小机器人：它们转头朝向光源来“进食”，又用闪光彼此搭话；聚在一起时形成一个闪烁的光动社会，观众走进其中，也会用手中的灯打扰它们。
- 实现方式: 每个机器人配有光传感器、可追光的电动头部和发光 LED；关于能量交换与信号传递的简单仿生规则产生群体行为。
- 视角: 机器环世界, 具身与动觉
- 展出与获奖: Lumen Prize 2019, BCS Artificial Intelligence Award
- 论文: https://doi.org/10.1007/978-3-319-16498-4_15 (EvoMUSART 2015, Lecture Notes in Computer Science)
- 视频: https://vimeo.com/207512856
- 图片: http://static1.squarespace.com/static/65e7176a61627736e02f6c4a/6606a60245e66065f7018332/6606a8f3e120ce2d55829d39/1711713362629/Lichtsuchende-1000x0-c-default.jpeg
- 项目主页: https://lumenprize.org/2019-winners/dave-murray-rust-rocio-von-jungenfeld

#### Plantoid — Primavera De Filippi (2015)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 区块链可以让一台机器拥有自己的经济生命，而人类成了它的传粉者。
- 作品内容: 一朵金属机器花，收到加密货币捐款时会舞动、发光。攒够钱后，它会委托艺术家为它制造后代，由捐款人投票在方案中做出选择：一台拥有自己并能自我繁殖的机器。
- 实现方式: 装有传感器、灯和电机的雕塑连接到区块链上的智能合约，由合约保管资金并组织新 Plantoid 的投票（与 Okhaos 合作）。
- 视角: 能动、自主与共创, 机器环世界
- 视频: https://www.youtube.com/watch?v=5gMbhCgHGjY

#### Kilobots：千台机器人集群（Kilobots: a thousand-robot swarm） — Radhika Nagpal (2014)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一群廉价、容易出错的机器仍然能组成集体形态，错误被群体吸收。
- 作品内容: 1024 台硬币大小、靠三根细腿移动的机器人，只靠与邻居之间的局部信号，缓慢地把自己排成星形、字母 K 等形状；堵塞和掉队者也是结果的一部分。
- 实现方式: 每台 Kilobot 靠振动电机移动，通过从桌面反射的红外线通信；分布式算法使用沿边移动、梯度形成与定位（与 Michael Rubenstein、Alejandro Cornejo 合作）。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1126/science.1254295 (Science 2014)
- 视频: https://www.youtube.com/watch?v=G1t4M2XnIhI
- 图片: https://upload.wikimedia.org/wikipedia/commons/d/d9/Kilobot_robot_swarm.JPG

#### 群集研究（系列）（Swarm Study (series)） — Random International (2010)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 仅凭群体运动规则，就能让光拥有一个会注意到我们的活群体的感觉。
- 作品内容: 黄铜杆网格中的灯光像鸟群或鱼群一样移动，随着下方的人聚拢又散开。Swarm Study / III（2011）为维多利亚与艾伯特博物馆收藏。
- 实现方式: 群聚算法驱动黄铜杆上可单独控制的灯；传感器把观众的位置与存在记录为对群体的扰动。
- 视角: 能动、自主与共创, 具身与动觉
- 展出与获奖: Victoria and Albert Museum, London (Swarm Study / III)
- 视频: https://www.youtube.com/watch?v=ajV8A5Y2_dE
- 项目主页: https://www.random-international.com/

#### 微妙的边界（Delicate Boundaries） — Chris Sugrue (2007)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 计算机视觉
- 核心想法: 当人工生命离开画框、把你的身体当作地形时，它就变得令人不安。
- 作品内容: 发光的小数字虫在屏幕上成群游走；观众一触碰屏幕，它们就从屏幕里爬到观众的手和手臂上，在身体上探索一番再回去。
- 实现方式: 摄像头追踪接触屏幕的手和手臂，上方的投影仪把群体模拟延续到身体表面。
- 视角: 具身与动觉, 机器环世界
- 展出与获奖: VIDA 10.0, Special Mention (2007)
- 视频: https://www.youtube.com/watch?v=QJ-uUnsFdxg

#### 传播（Propagaciones） — Leandro Núñez (2007)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 用机器人来体现元胞自动机，把抽象的生命模型变成在房间里发生的事。
- 作品内容: 一排排小机器人按照康威“生命游戏”的规则点亮或熄灭，让“生”与“死”的细胞图案在一群实体机器中传播开来。
- 实现方式: 每台机器人读取邻居的状态，按生命游戏的规则更新自己的灯光和动作；整个网格没有中央控制。
- 视角: 能动、自主与共创, 机器环世界
- 视频: https://www.youtube.com/watch?v=5BTa1c3Y6Fo
- 项目主页: https://www.leonunez.com.ar/

#### ALAVs 2.0（自主光气飞行器）（ALAVs 2.0 (Autonomous Light Air Vessels)） — Jed Berk (2006)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 机器生物与移动机器人
- 核心想法: 当无人机像一群温和、有需要的生物而不像工具那样行动时，我们对它的感受完全不同。
- 作品内容: 一群小型氦气飞艇在空间中漂浮，避开墙壁、彼此成群、靠近观众，电量不足时会去“进食”；观众还能用手机呼叫它们。
- 实现方式: 每艘飞艇配有螺旋桨、红外与声呐传感器和运行集群、避障行为的微控制器，并有接收人类手机信息的接口。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: VIDA 10.0, Special Mention (2007); Taipei Digital Art Festival
- 视频: https://www.youtube.com/watch?v=8CKrjCUMhdA

#### 城市寄生虫（Parásitos Urbanos (Urban Parasites)） — Gilberto Esparza (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 把城市的电线和垃圾当作栖息地，机器人就成了靠它们为生的一种新野生物种。
- 作品内容: 一群用废弃电子零件制作的小机器人，挂在城市电线和墙面上偷电，并像生活在城市生态中的动物一样发出声响。
- 实现方式: 回收的马达、电路和扬声器被组装成不同“物种”（带有 Furtum electricus 这样的拉丁学名），它们接入带电线路取电，并对光与噪音作出反应。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: VIDA 9.0, Incentive for Ibero-American Production (2006); Intermediae Madrid 2011; Fundación Telefónica Lima, Cultivos (2014)
- 视频: https://www.youtube.com/watch?v=X64KRaQpyCY
- 图片: http://gilbertoesparza.net/wp-content/uploads/2023/01/COLGADO-Furtum-electricus-sinuatum-1024x683.jpg http://gilbertoesparza.net/wp-content/uploads/2023/01/DIABLITO-_-LITTLE-DEVIL-Furtum-electricus-imitor-1024x683.jpg
- 项目主页: https://gilbertoesparza.net/portfolio/parasitos-urbanos/

#### 基于持续自我建模的韧性机器（Resilient Machines Through Continuous Self-Modeling） — Josh Bongard, Hod Lipson (2006)
- 类型: 论文 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一台能为自己身体建模的机器可以在受伤后存活，这是迈向某种机器自我觉察的第一步。
- 作品内容: 一台四条腿的“海星”机器人不知道自己的形状。它稍微动一动，建立几个互相竞争的身体模型，并用它们学会走路；当一条腿被截短，它能发现损伤并发明新的步态。
- 实现方式: 机器人用倾角传感器和关节编码器检验动作假设，在候选自我模型中挑选，再在最佳模型上优化运动（与 Viktor Zykov 合作）。
- 视角: 具身与动觉, 失败、故障与错误, 能动、自主与共创
- 论文: https://doi.org/10.1126/science.1133687 (Science 2006)
- 视频: https://www.youtube.com/watch?v=x579QKA6fkY

#### 空间关系学（Proxemia (Proxemics)） — Mariela Yeregui (2005)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 社交距离和对触碰的恐惧可以被演成机器行为，让观众变成机器人群体里的一个障碍物。
- 作品内容: 二十五个发光的亚克力球在地面上自由滚动；每当碰到观众、另一个球或墙壁，它就变色并转向离开，仿佛害怕接触。其中一个透明球能看到内部的机器人，行为与其他球不同。
- 实现方式: 每个直径 25 厘米的球内装有一台小机器人，具备位置与运动感知、碰撞检测和自己的灯；接触会触发方向和灯光的变化。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=MEYvKy38x1o
- 图片: https://marielayeregui.com/wp-content/uploads/2021/10/esferasx2-1024x683.jpg
- 项目主页: https://marielayeregui.com/proxemia-proxemics/

#### 自我复制机器（Molecubes）（Self-reproducing machines (Molecubes)） — Hod Lipson (2005)
- 类型: 论文 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 自我复制长期被视为生命的标志，而只要有零件供应，简单的模块化机器也能做到。
- 作品内容: 一座由四个磁力相连的机器人立方体组成的塔弯下身子，从“喂料站”拾起新的立方体，把它们叠成自己的复制品，用时约两分半钟。
- 实现方式: 每个 10 厘米的立方体有一个旋转关节、各面上的电磁铁和一枚微控制器；预编程序列把立方体从喂料站移去搭建复制品（康奈尔大学，与 Victor Zykov、Efstathios Mytilinaios、Bryant Adams 合作）。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1038/435163a (Nature 2005)
- 视频: https://www.youtube.com/watch?v=gZwTcLeelAY

#### ArtSBots — Leonel Moura (2003)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 涌现的机器集体可以产生作者是群体本身的“非人艺术”。
- 作品内容: 一群装着彩色笔的小型轮式机器人在大画布上移动，每台机器人都对其他机器人留下的颜色做出反应，最后出现一幅无人规划的画。2006 年，Moura 的 RAP（机器人行动画家）把这个思路延伸为一台自主作画的机器。
- 实现方式: 每台机器人配有颜色传感器、避障传感器和微控制器，运行类似“共识主动性”的规则：在已有颜色的地方画得更多，就像蚂蚁追随信息素（与 Henrique Garcia Pereira 合作）。
- 视角: 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=XlUxXQPmKUc
- 项目主页: https://www.leonelmoura.com/robot-art/

#### 自创生（Autopoiesis） — Ken Rinaldo (2000)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 控制论与人工生命系统
- 核心想法: 一群彼此交谈的机器会形成一种集体情绪，而这种情绪不在任何一条机械臂里。
- 作品内容: 十五条由葡萄藤和电子元件做成的机械臂从天花板垂下，感知观众并向他们弯曲，彼此之间用音调发信号，使整个群体的行为一起变化。
- 实现方式: 每条臂装有红外传感器和微控制器；机械臂通过中央计算机和可听的音调共享信息，一台摄像机追踪观众位置。
- 视角: 能动、自主与共创, 具身与动觉, 机器环世界
- 展出与获奖: Alien Intelligence, Kiasma, Helsinki 2000; VIDA 3.0, first prize; Prix Ars Electronica 2001, Honorary Mention (Interactive Art)
- 视频: https://www.youtube.com/watch?v=9TfrKQH6OPg
- 图片: https://www.kenrinaldo.com/wp-content/uploads/2015/04/Autopoieis3-440x450.jpg https://archive.aec.at/asset/1318971/preview/
- 项目主页: https://www.kenrinaldo.com/portfolio/autopoiesis/

#### 伊甸（Eden） — Jon McCormack (2000)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 人的注意力成了一种生态资源，人工生物演化出捕获它的能力。
- 作品内容: 一个会演化的“声音生物”生态系统生活在投影到半透明屏幕上的元胞世界里。生物学会唱歌、交配和觅食；由于观众的存在会让食物生长，能用歌声吸引人的生物更容易存活。
- 实现方式: 带有学习分类器系统的智能体在网格上移动并发声；红外传感器检测观众，增加附近格子里的食物。
- 视角: 机器环世界, 机器之耳与声, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=Yrww68pnqqM
- 图片: https://i0.wp.com/jonmccormack.info/wp-content/uploads/2023/03/Eden3.jpg?fit=1920%2C1280&ssl=1
- 项目主页: https://www.jonmccormack.info/artworks/eden/

#### 魔像计划（Golem project） — Hod Lipson (2000)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 机器可以设计并制造自己的身体，人只剩下插上电机这一步。
- 作品内容: 计算机在模拟中演化出由杆件和执行器组成的简单机器人，按爬行能力进行选择，再把它们 3D 打印出来；手工装上电机后，这些实体“生命形式”像在模拟中一样在地上爬行。
- 实现方式: 演化算法在物理模拟中同时演化形态与神经控制；胜出的设计用快速成型制造（与布兰迪斯大学 Jordan Pollack 合作）。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1038/35023115 (Nature 2000)
- 视频: https://www.youtube.com/watch?v=tgJcYx-yewA

#### 加拉帕戈斯（Galápagos） — Karl Sims (1997)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 审美偏好成了选择压力，艺术家把作者身份交给了演化过程。
- 作品内容: 十二块屏幕各显示一种抽象的动画生物。观众站到自己喜欢的屏幕前的感应器上，被选中的生物存活、交配并变异，其余的死去，于是观众扮演了自然选择。
- 实现方式: 十二台计算机根据遗传编码渲染生物；每块屏幕前的踏板感应器记录选择，被选中的基因型被复制、重组和变异。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: NTT InterCommunication Center (ICC), Tokyo 1997–2000
- 图片: https://www.karlsims.com/galapagos/galapagos-icc.jpg https://www.karlsims.com/galapagos/image39.jpg
- 项目主页: https://www.karlsims.com/galapagos/index.html

#### 生命空间种（Life Spacies） — Christa Sommerer & Laurent Mignonneau (1997)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 聊天机器人与语言模型
- 核心想法: 语言变成了 DNA：人们写下的文字真的在塑造机器生物的身体。
- 作品内容: 观众通过互联网发送文字信息；每段文字被当作遗传编码，生成一只独特的人工生物，它在共享的线上与展厅世界中生活，以更多文字为食并繁殖。
- 实现方式: 一种“文字到形态”的遗传算法把字符及其顺序转译为身体参数；打出的文字也成为环境中的食物。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: NTT InterCommunication Center (ICC), Tokyo 1997
- 视频: https://www.youtube.com/watch?v=-OXpk0PmMLc

#### 共感知觉（Sympathetic Sentience） — Simon Penny (1995)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 一个机器集体可以有自己的生命，人类只能打扰它，却无法控制它。
- 作品内容: 暗室的墙和天花板上装有十二个小电子单元，它们啁啾作响，并通过红外线把各自的节奏传给下一个，逐渐形成复杂、永不重复的声音图案。观众走过会打断这条链，房间慢慢安静下来，然后重新建立它的歌。
- 实现方式: 每个相同的单元每分钟啁啾一次，把自己的节奏与接收到的红外数据流合并后再传出去（与 Jamieson Schulte 合作）。
- 视角: 机器之耳与声, 能动、自主与共创, 机器环世界
- 视频: https://www.youtube.com/watch?v=ZX9Zta2T1do
- 项目主页: https://simonpenny.net/works/sympathetic.html

#### A-Volve — Christa Sommerer & Laurent Mignonneau (1994)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 当一个画出来的形状必须在与其他生物和人手共享的环境中求生时，人工生命就变得可以触摸。
- 作品内容: 观众在触摸屏上画出一个形状，它就变成一只在真实水池中游动的三维生物。生物根据自身形态捕食、交配、死亡，观众可以把手伸进水里触碰和保护它们。
- 实现方式: 绘画被转成决定每只生物形状和游泳能力的遗传编码；生物被投影进一个盛水的玻璃池，摄像头追踪观众的手。
- 视角: 能动、自主与共创, 机器环世界, 具身与动觉
- 展出与获奖: Prix Ars Electronica 1994, Golden Nica (Interactive Art)
- 视频: https://www.youtube.com/watch?v=0WG45k93pCA
- 图片: https://archive.aec.at/asset/1390558/preview/
- 项目主页: https://archive.aec.at/prix/142357/

#### 进化的虚拟生物（Evolved Virtual Creatures） — Karl Sims (1994)
- 类型: 论文 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 模拟中的演化能产生没有工程师会画出来的机器身体——奇怪，却明显有目的。
- 作品内容: 由方块组成身体的生物在物理模拟的世界里游泳、行走、跳跃，并争夺一个方块。它们的身体和神经“大脑”都是由遗传算法演化出来的，而不是设计出来的。
- 实现方式: 用有向图编码形态与神经控制器；在 Connection Machine CM-5 上运行的刚体物理模拟中，按游泳、行走、跳跃、跟随或竞争的表现选择种群。
- 视角: 具身与动觉, 能动、自主与共创, 机器环世界
- 论文: https://doi.org/10.1145/192161.192167 (SIGGRAPH 1994)
- 视频: https://www.youtube.com/watch?v=RZtZia4ZkX8
- 图片: http://www.karlsims.com/creatures-crab-vs-arm.jpg
- 项目主页: https://www.karlsims.com/evolved-virtual-creatures.html

#### 互动植物生长（Interactive Plant Growing） — Christa Sommerer & Laurent Mignonneau (1992)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 活植物与虚拟生长被耦合在一起，这座花园只有通过人与植物的接触才会生长。
- 作品内容: 观众触摸或靠近五株真实植物，每个动作都会让大屏投影上的虚拟植物生长；活植物成为通往人工花园的界面。
- 实现方式: 测量植物被触碰时的电位变化，并将其转换为实时三维植物模型的生长参数。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: ZKM Karlsruhe collection
- 视频: https://www.youtube.com/watch?v=JXX7JNFD2X8

#### 仿生兽（Strandbeest） — Theo Jansen (1990)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一台没有电子元件的机器，仍然可以在自己的栖息地里演化、感知和“求生”。
- 作品内容: 用 PVC 管制作的大型行走骨架，在荷兰海滩上靠风驱动，把空气储存在瓶中，后代机型还能感知海水并掉头远离大海。
- 实现方式: 用计算机演化算法找到的“神圣数字”设计腿部连杆，把风力驱动的旋转转为行走；塑料瓶是储气的“胃”，管子充当逻辑元件。
- 视角: 具身与动觉, 机器环世界
- 展出与获奖: Prix Ars Electronica 2005, special prize (Interactive Art)
- 视频: https://www.youtube.com/watch?v=C97kMKwZ2-g
- 图片: https://archive.aec.at/asset/1050599/preview/
- 项目主页: https://www.strandbeest.com/

#### 类鸟群（Boids） — Craig Reynolds (1987)
- 类型: 论文 · 机器: 控制论与人工生命系统
- 核心想法: 集体生命可以在没有领导和计划的情况下涌现，这改变了我们对机器群体的想象。
- 作品内容: 模拟的“类鸟”智能体会群聚、绕开障碍分流再重新汇合，就像真正的鸟群，尽管每个个体只遵循三条局部规则。这个模型很快被用于《蝙蝠侠归来》（1992）等电影中的蝙蝠和企鹅。
- 实现方式: 每个智能体根据与邻近同伴的分离、对齐与聚合三条规则转向，在三维动画系统中计算。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1145/37401.37406 (SIGGRAPH 1987)
- 视频: https://www.youtube.com/watch?v=86iQiV3-3IA
- 项目主页: https://www.red3d.com/cwr/boids/

### 工业机械臂与编舞

离开工厂的工业机器人：会跳舞、画画、劳作或哀求的机械臂。

#### Manus — Madeline Gannon (2018)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 工业机器人可以被设计成共享注意力的社会群体，而不是孤立的工具。
- 作品内容: 十台排成一列的工业机械臂共享一个感知系统，像一个群体一样行动：一起转向跟随路人，把注意力沿着队列传递下去。
- 实现方式: 底部的深度传感器汇入一个统一的追踪系统；每台 ABB 机械臂按群体行为规则选择目标。
- 视角: 能动、自主与共创, 具身与动觉
- 展出与获奖: World Economic Forum Annual Meeting of the New Champions, Tianjin 2018
- 视频: https://www.youtube.com/watch?v=lyQwqi-Hycw
- 项目主页: https://atonaton.com/manus

#### 惩罚（The Punishment） — Filipe Vilas-Boas (2017)
- 类型: 艺术作品与装置 · 机器: 工业机械臂
- 核心想法: 把机器人伦理变成课堂罚抄，追问规则能否靠重复学会，以及到底是谁在被规训。
- 作品内容: 一只工业机械臂坐在课桌前，用工整的笔迹一遍又一遍地写下“I must not hurt humans”，就像被罚抄的孩子。
- 实现方式: 一只握笔的小型工业机械臂在纸上无限循环地重放书写轨迹。
- 视角: 失败、故障与错误, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=wA0zU2wC2dk
- 图片: https://payload.cargocollective.com/1/19/638884/12653201/prt_1497962393_2x.jpg
- 项目主页: https://www.filipevilasboas.com/the-punishment

#### Mimus — Madeline Gannon (2016)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 一台被赋予好奇心而非任务的工厂机器人，不再是威胁，而是一个可以相遇的生灵。
- 作品内容: 在伦敦设计博物馆的玻璃围栏里，一台重 1200 公斤的 ABB 工业机器人会注意到观众，跟随其中最有趣的那个，对方一动不动时它就厌倦了，像一只好奇的动物。
- 实现方式: 天花板上的深度传感器追踪观众；定制软件（没有预先编好的动作）实时决定机械臂看向哪里、如何移动。
- 视角: 能动、自主与共创, 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Fear and Love, Design Museum London 2016
- 视频: https://www.youtube.com/watch?v=B9jwNWiEd_M
- 图片: http://static1.squarespace.com/static/5758289d27d4bdf581e1c031/t/64386d617b6835253f5680cd/1681419617332/charlie-longexposure-2.jpg?format=1500w
- 项目主页: https://atonaton.com/mimus

#### 盒（Box） — Bot & Dolly (2013)
- 类型: 电影与影像 · 机器: 工业机械臂
- 核心想法: 当工业机械臂移动舞台，精准本身就成了幻术，机器靠完美表演把自己藏起来。
- 作品内容: 一场一镜到底拍摄的现场表演：两只工业机械臂移动大屏，表演者与投影映射出的纵深、立方体和坍塌幻象互动。机械臂是看不见的场务。
- 实现方式: 承载投影面的机械臂与投影映射、运动控制摄像机同步，编排基于 Autodesk Maya。
- 视角: 具身与动觉, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=lX6JcybgDFo

#### 回眸者（长鼻）（Double-Taker (Snout)） — Golan Levin (2008)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 监控变成了对视：被演成好奇的机器目光，让人以监控摄像头从未有过的方式感到“被看见”。
- 作品内容: 一只 2.5 米长、被装扮成巨型尺蠖或象鼻的工业机械臂，蹲在美术馆入口上方的屋顶上；它把一只超大的活动眼转向路人，追踪他们，还会做出“愣了一下再看”的动作，仿佛每个人都让它吃惊。
- 实现方式: ABB 工业机械臂由实时机器视觉系统驱动，追踪下方行人并触发富有表情的“回头看”动作。
- 视角: 机器之眼, 他异与恐怖谷, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2009, Honorary Mention (Interactive Art)
- 视频: https://www.youtube.com/watch?v=jXqYf4m-HA8
- 图片: https://archive.aec.at/asset/327892/preview/ https://archive.aec.at/asset/327893/preview/ https://archive.aec.at/asset/327894/preview/
- 项目主页: https://www.flong.com/archive/projects/snout/index.html

### 仿真人与恐怖谷

类人机器，以及“几乎像人”带来的不安。

#### Ameca — Engineered Arts (2021)
- 类型: 产品与平台 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 它的爆红片段显示，即使知道表情是编程出来的，人们仍会从机器的脸上读出大量情感。
- 作品内容: 一个灰色皮肤、刻意无性别的人形机器人，它的第一段视频——醒来后惊讶地看着自己的双手——迅速爆红；如今它在展会和博物馆展出，常借助大语言模型说话。
- 实现方式: 模块化人形平台，面部有数十个执行器，眼中有摄像头，由云端软件负责动画与对话。
- 视角: 他异与恐怖谷, 具身与动觉
- 视频: https://www.youtube.com/watch?v=IPukuYb9xWw
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/5e/Ameca_Generation_1.jpg
- 项目主页: https://www.engineeredarts.co.uk/robot/ameca/

#### 安妮丽丝，寻求完整（Annelies, Looking for Completion） — L.A. Raeven (2018)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 不是为我们服务的机器人，而是需要我们的机器人，以及安慰一台机器时的那种不自在。
- 作品内容: 一个按双胞胎艺术家本人制作的逼真仿人机器人，“第三个姐妹”，坐在角落里哭泣；观众试图安慰她时，她抬起满是泪痕的脸看着对方。
- 实现方式: 按艺术家面部与身体制作的硅胶仿人机器人，带电动表情、流泪装置和感应观众靠近的传感器。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: Robot Love, Eindhoven 2018; Collection Bonnefanten, Maastricht
- 视频: https://www.youtube.com/watch?v=Jyfq-xq5GyA
- 项目主页: https://robotlove.nl/en/expo/

#### ORLAN-OÏDE — ORLAN (2018)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 一位以改造自身身体闻名的艺术家，造出机器自我并让它代替自己说话。
- 作品内容: 艺术家的人形机器人分身，拥有她的面孔与声音，能回答问题、谈论艺术；ORLAN 曾在公开场合与它对谈。
- 实现方式: 机器人半身像，搭载以艺术家文本训练的对话 AI 和合成的本人声音；后续版本与 RaspiAudio 合作开发。
- 视角: 他异与恐怖谷, 哀悼、记忆与来世
- 展出与获奖: Artistes & Robots, Grand Palais, Paris 2018
- 视频: https://www.youtube.com/watch?v=uSeo1wMvG_g
- 项目主页: https://www.orlan.eu/

#### SEER：模拟情感表达机器人（SEER: Simulative Emotional Expression Robot） — 藤堂高行 (2018)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 计算机视觉
- 核心想法: 被一台机器回望，就足以让人觉得“那里有某个存在”。
- 作品内容: 一个小巧、风格化的人形头部，追踪观者的视线，并用眼球、眼睑和眉毛的细微动作模仿观者的表情。
- 实现方式: 带人脸与视线追踪的摄像头驱动眼球和眼睑的电机以及线驱动的柔性眉毛；面部刻意不做写实。
- 视角: 他异与恐怖谷, 机器之眼
- 展出与获奖: Ars Electronica 2018; Laval Virtual 2019
- 视频: https://www.youtube.com/watch?v=BJZcGJSK1Z0
- 项目主页: https://www.takayukitodo.com/

#### Alter — 池上高志, 石黑浩 (2016)
- 类型: 研究原型 · 机器: 类人机器人, 控制论与人工生命系统
- 核心想法: 让机器显得“活着”的不是逼真，而是自发性。
- 作品内容: 一个有人脸、机械身体外露的仿真人，会自己动：它的动作来自对传感器作出反应的人工生命神经网络，而不是预设脚本。
- 实现方式: 约 40 个气动关节由中枢模式发生器和脉冲神经网络驱动，输入来自距离、噪音与温度传感器；2019 年的 Alter3 加入了摄像头，后来又接入 GPT-4。
- 视角: 能动、自主与共创, 他异与恐怖谷, 具身与动觉
- 展出与获奖: Miraikan, Tokyo 2016; Prix Ars Electronica 2018, Interactive Art+; AI: More than Human, Barbican 2019 (Alter 3)
- 论文: https://doi.org/10.1162/isal_a_00463 (ALIFE 2021)
- 视频: https://www.youtube.com/watch?v=iYzOZQDsm5w
- 项目主页: https://en.wikipedia.org/wiki/Takashi_Ikegami

#### Sophia — Hanson Robotics (2016)
- 类型: 产品与平台 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 一个被当作“人”来展示的机器人，表明人格身份多么容易被授予一场表演。
- 作品内容: 一台以女性形象呈现、面部表情丰富的类人机器人，登上脱口秀和联合国讲台；2017 年沙特阿拉伯宣布授予 Sophia 公民身份。机器人学者批评这些照稿演出误导了公众对 AI 的理解。
- 实现方式: 以 Frubber 仿生皮肤覆盖的电动面部，内置电机与摄像头，结合预设脚本与聊天机器人对话。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 展出与获奖: SXSW 2016; Future Investment Initiative, Riyadh 2017; AI for Good Global Summit 2018
- 视频: https://www.youtube.com/watch?v=sKrV2CVDXjo
- 图片: https://upload.wikimedia.org/wikipedia/commons/1/1e/Sophia_at_the_AI_for_Good_Global_Summit_2018_%2827254369347%29_%28cropped%29.jpg
- 项目主页: https://en.wikipedia.org/wiki/Sophia_(robot)

#### （女性形象）（(Female figure)） — Jordan Wolfson (2014)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 计算机视觉
- 核心想法: 机器的眼神接触把“看”变成“被看”，让观众成为这场性化展示的共谋。
- 作品内容: 一个真人大小、戴女巫面具、穿比基尼和脏靴子的电子动偶女人对着镜子挑逗地跳舞，然后直视观众的眼睛，用艺术家本人的声音说话。
- 实现方式: 由 Spectral Motion 制作的电子动偶执行编排好的动作；面部识别摄像头让它与观众对视。
- 视角: 他异与恐怖谷, 机器之眼, 分类、偏见与监控
- 展出与获奖: David Zwirner, New York 2014
- 视频: https://www.youtube.com/watch?v=XSFP6JHnn9c
- 项目主页: https://www.davidzwirner.com/artists/jordan-wolfson

#### 人机（The Man Machine） — Vincent Fournier (2010)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 把为人而设的肖像体裁用在机器身上，让我们追问它们身上是什么在回望。
- 作品内容: 一组真实人形机器人的摄影系列，包括 ASIMO 和 REEM-B，它们在实验室、住宅与风景中以正式肖像般的静止姿态出现。
- 实现方式: 在日本、欧洲和美国的机器人实验室实地拍摄的布景式大画幅彩色照片。
- 视角: 他异与恐怖谷, 具身与动觉
- 展出与获奖: Hello, Robot., Vitra Design Museum 2017
- 视频: https://www.youtube.com/watch?v=JUhIQo6PvQo
- 项目主页: https://www.vincentfournier.co.uk/

#### 德克，无家可归的机器人（Dirk, the homeless robot） — Electric Circus (2008)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 人们会在弄清对方是否是活物之前，就先施舍怜悯或感到不安；这个仿真人测试的是我们如何对待街边的人。
- 作品内容: 一个逼真的电子动画“流浪汉”，坐在街头和节庆现场活动；路人和他说话、给他钱，或是在发现他是机器之前就已退避。
- 实现方式: 由发明家 Fred Abels 与木偶师 Mirjam Langemeijer 制作的电子动画人偶，头、眼和手都会动，在公共空间中运行。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: Prix Ars Electronica 2010, Honorary Mention (Hybrid Art)
- 视频: https://www.youtube.com/watch?v=cwX6CuUyeFw
- 图片: https://archive.aec.at/asset/452494/preview/ https://archive.aec.at/asset/452495/preview/
- 项目主页: http://www.electric-circus.eu

#### Geminoid HI-1 — 石黑浩 (2006)
- 类型: 研究原型 · 机器: 类人机器人
- 核心想法: 当复制品替代本人出场，人们开始追问“这个人”究竟在哪里。
- 作品内容: 以石黑浩本人为原型的遥控仿真人，硅胶皮肤、气动驱动；石黑浩在别处通过它讲话，派它去讲课。
- 实现方式: 摄像头与麦克风捕捉操作者的声音、嘴唇与头部动作，驱动仿真人体内约 50 个气动执行器；细小的无意识动作自动运行。
- 视角: 他异与恐怖谷, 具身与动觉
- 展出与获奖: Ars Electronica 2009
- 论文: https://doi.org/10.5772/4876 (Humanoid Robots: New Developments (I-Tech), 2007)
- 视频: https://www.youtube.com/watch?v=fhS9KkOXDXE
- 图片: https://upload.wikimedia.org/wikipedia/commons/d/d6/Hiroshi_Ishiguro_and_Geminoid_HI-1_at_AEC.JPG
- 项目主页: http://www.geminoid.jp/en/robots.html

#### JoAn，肉身之人（JoAn, l'home de carn） — Marcel·lí Antúnez Roca (1992)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 语音与听觉机器
- 核心想法: 披着肉皮的机器表明：诡异感既来自机器人，也来自观众的笑声和狗吠。
- 作品内容: 一个真人大小、缝着猪皮的坐姿男性机器人被置于玻璃柜中，观众在旁说话、唱歌、吹口哨或鼓掌时，它就转动脖子、肩膀、手肘和阴茎。
- 实现方式: 计算机分析现场声音，向机械关节人偶四处关节的电机发送信号。
- 视角: 他异与恐怖谷, 机器之耳与声
- 图片: https://www.marceliantunez.com/media/cache/07/7c/077c994ce12858786f4a25a749c0ba02.jpg
- 项目主页: https://www.marceliantunez.com/work/joan-lhome-de-carn/

#### ROSA BOSOM — Bruce Lacey (1965)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 一个刻意粗糙的仿真人显示：机器人幻想中有多少是性别、剧场和遥控器。
- 作品内容: 一个用废品拼成、哐当作响的“女性”机器人演员，装在轮子上，名字是 Radio Operated Simulated Actress Battery Or Standby Operated Mains 的缩写。她在 Cybernetic Serendipity 展上与伴侣 MATE 一起展出，戏仿“机器女人”的幻想。
- 实现方式: 无线电遥控的电机带动一个由废料、家用物件和人体模特零件组装的身体；如名字所示，可用电池或市电供电。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 展出与获奖: Cybernetic Serendipity, ICA London 1968
- 视频: https://www.youtube.com/watch?v=nTMNiYV5yIE
- 项目主页: https://en.wikipedia.org/wiki/Bruce_Lacey

#### 写字人偶（The Writer） — Pierre Jaquet-Droz (1774)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 一个 18 世纪的仿真人早已提出了“没有心灵的书写”这一问题。
- 作品内容: 一个玩偶大小的男孩坐在书桌前，用鹅毛笔蘸墨，写下最多 40 个字符的文字，眼睛随着字母移动。它至今仍在纳沙泰尔艺术与历史博物馆演示。
- 实现方式: 约 6000 个零件，用一个可更换凸轮的可编程轮盘设定每个字母；与 Henri-Louis Jaquet-Droz 和 Jean-Frédéric Leschot 共同制作。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 展出与获奖: Musée d'art et d'histoire, Neuchâtel
- 视频: https://www.youtube.com/watch?v=ux2KW20nqHU
- 项目主页: https://en.wikipedia.org/wiki/Jaquet-Droz_automata

### 机器雕塑与动态装置

在空间中与观众互动、自主行为的机器雕塑与装置。

#### Guanaquerx — Paula Gaetano Adi (2025)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 自动驾驶与无人机
- 核心想法: 机器人技术可以扎根于安第斯的在地知识与地景，而不是硅谷式的机器想象。
- 作品内容: 一台与阿根廷圣胡安工匠和业余机修工一起制作的自主越野车穿越安第斯山脉驶向智利，以多日表演重演何塞·德·圣马丁 1817 年的独立远征。
- 实现方式: 一台受当地“guanaquera”（自制越野车）启发的全地形车自主穿越山地，社区工作坊也是作品的一部分。
- 视角: 机器环世界, 能动、自主与共创, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2025, Golden Nica (Artificial Life & Intelligence)
- 视频: https://www.youtube.com/watch?v=TRGilwpKi-I
- 图片: https://archive.aec.at/asset/3849576/preview/
- 项目主页: https://archive.aec.at/prix/303077/

#### 小方舟（Little Ark） — Choe U-Ram (2022)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一台划桨却哪儿也去不了的机器，成为集体停滞的图像。
- 作品内容: 一艘用废纸箱与钢材制成的大型动态方舟，船桨按缓慢编排的周期开合，四周环绕着其他机械生物。它在 MMCA 现代汽车系列展中展出，呈现一个漂流中的社会。
- 实现方式: 电机驱动的钢结构覆以纸板外皮，运动经编程控制；在临时工作坊中制作与测试后安装。
- 视角: 具身与动觉, 机器环世界
- 展出与获奖: MMCA Hyundai Motor Series 2022: Choe U-Ram – Little Ark, MMCA Seoul 2022–23
- 视频: https://www.youtube.com/watch?v=zKHfM4PUZ7k
- 项目主页: https://www.uram.net/

#### πTon — Cod.Act (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 当声音来自一具柔软机器身体的扭曲，机器仿佛在唱出自己的用力。
- 作品内容: 一个巨大的橡胶管环躺在地上，像活物一样扭动、缠绕、收缩；它的抽搐发出类似人声、合唱般的声音。
- 实现方式: 内部电机和缆绳让弹性管变形；它的运动数据被实时转换为人声般的声景。
- 视角: 具身与动觉, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=fB1kI5EGzqY
- 图片: https://codact.ch/wp-content/uploads/2018/05/PiTon230518SC-09.jpg
- 项目主页: https://codact.ch/

#### 机器之母：NoodleFeet（Mother of Machine: NoodleFeet） — Sarah Petkus (2016)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一个没有用途的机器人邀请另一种关系：照料与好奇，而不是服务。
- 作品内容: NoodleFeet 是一个长着泳池浮条脚的“青春期”机器人，会走路、会尝地面、会抓东西；制作者把这个没有终点的建造过程描述为抚养一个孩子，希望它形成自己回应世界的方式。
- 实现方式: 用轻金属、3D 打印件和现成物做成的腿式机器人，脚和“舌头”上的传感器触发各种行为；硬件和代码不断迭代重建。
- 视角: 具身与动觉, 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2018, Honorary Mention (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=lbf6xV47L8I
- 图片: https://archive.aec.at/asset/2567402/preview/ https://archive.aec.at/asset/2567404/preview/ https://archive.aec.at/asset/2567408/preview/
- 项目主页: https://archive.aec.at/prix/236785/

#### 十五点习作 / I（Study for Fifteen Points / I） — Random International (2016)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 十五个移动的点就足以让我们看见一个人；机器利用的是我们对生物运动的感知。
- 作品内容: 机械杆上的十五个光点一起运动，让人立刻看出一个正在行走的人，尽管那里没有身体，只有机器。
- 实现方式: 电机沿杆移动十五盏灯，重现“光点行走者”；作品源于在哈佛工程与应用科学学院的驻留。
- 视角: 具身与动觉, 机器之眼, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=qnkxo7CWACs
- 图片: https://images.squarespace-cdn.com/content/v1/663ca532b3e3797d82159fe2/0d90a48e-3f33-4c69-b508-9cbc6a607893/STUDY+FOR+FIFTEEN+POINTS+%3A+I%2C+2016++.jpeg
- 项目主页: https://www.random-international.com/study-for-fifteen-points

#### Jller — Benjamin Maus, Prokop Bartoníček (2015)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 工业机械臂
- 核心想法: 计算机视觉也可以缓慢而沉思：一台阅读深时间的机器。
- 作品内容: 一台工业机器把采自德国南部伊勒河（Iller）的石头逐一拾起、拍照，再按地质年代一排排摆放。
- 实现方式: 带真空吸盘与摄像头的龙门机器人；以图像特征（很可能是颜色、纹理与纹路）判断石头的地质来源，训练数据为艺术家亲手标注的石头。
- 视角: 机器环世界, 机器之眼
- 图片: https://media.wired.com/photos/5926f95bcfe0d93c47431f8b/191:100/w_1280,c_limit/RockRobot-1.jpg
- 项目主页: http://www.prokopbartonicek.com/jller-ignorance-with-benjamin-maus-2015

#### 海市蜃楼（Mirage） — Ralf Baecker (2014)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 控制论与人工生命系统
- 核心想法: 一台学习机器可以梦见它感知却从未看见的世界，而我们看到的只是它的幻觉。
- 作品内容: 一道激光打在一片薄而颤动的镜面上，在墙上投出缓慢变化的地景，那是一个由地球磁场“喂养”的神经网络所做的“梦”。
- 实现方式: 磁通门磁力计的数据输入一个以亥姆霍兹机为原型的无监督学习算法；它生成的变体驱动 48 根肌肉线来使镜面变形。
- 视角: 不透明与潜空间, 机器环世界
- 展出与获奖: Prix Ars Electronica 2015, Honorary Mention (Hybrid Art); ACT Festival, Asia Culture Center, Gwangju 2015
- 视频: https://www.youtube.com/watch?v=VY1hOjWlVO8
- 图片: https://archive.aec.at/asset/1882015/preview/
- 项目主页: https://archive.aec.at/prix/212751/

#### Nyloïd — Cod.Act (2013)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 一台没有头也没有脸的机器，仍然可以借张力、扭转和声音被读作一种生物。
- 作品内容: 一个高大的三脚生物长着套着尼龙的长腿，在表演中扭转、甩动、折叠，四肢绞紧又释放时发出奇异的声音。
- 实现方式: 电机扭转三条柔性腿来储存和释放弹性能量；声音系统把动作转为人声般的声音。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Sónar, Barcelona; FutureEverything, Manchester
- 视频: https://www.youtube.com/watch?v=f2sMD73fdYM
- 图片: https://codact.ch/wp-content/uploads/2013/10/Nyl-18-Copie.jpg
- 项目主页: https://codact.ch/

#### Pinokio — Adam Ben-Dror (2012)
- 类型: 研究原型 · 机器: 社交与陪伴机器人, 计算机视觉
- 核心想法: 一个熟悉的物件，只靠几种行为——注意、厌倦、拒绝被关掉——就获得了性格。
- 作品内容: 一盏台灯用灯头里的摄像头看着人，跟随他们的脸，会厌倦、四处张望、随声音舞动；有人把它关掉，它会自己再打开。
- 实现方式: 摄像头与基于 Processing/OpenCV 的人脸追踪，经由 Arduino 驱动六个舵机（与 Shanshan Zhou、Joss Doggett 合作）。
- 视角: 亲密、照护与陪伴, 能动、自主与共创, 机器之眼
- 展出与获奖: VIDA 16.0 (Fundación Telefónica), 2014
- 视频: https://www.youtube.com/watch?v=1E_hHr6YuFk

#### 非理性计算（Irrational Computing） — Ralf Baecker (2011)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 展示每块芯片底下的矿物，让计算重新成为一种物质的、地质的过程。
- 作品内容: 五个互相连接的模块由原矿晶体、矿物和电极组成，构成一台原始的、被放大的信号处理器：碳化硅像显示屏一样闪烁，石英共振，数据脉冲肉眼可见地在各站之间流动。
- 实现方式: 来自自然、工业废料或实验室培养的晶体被用作半导体、振荡器和发光体，接入一个反馈网络。
- 视角: 不透明与潜空间, 机器环世界
- 展出与获奖: Prix Ars Electronica 2012, Honorary Mention (Hybrid Art); VIDA 14.0, second prize
- 视频: https://www.youtube.com/watch?v=rwR_ofkPFnk
- 图片: https://archive.aec.at/asset/1530041/preview/
- 项目主页: https://archive.aec.at/prix/194180/

#### 蒂勒女孩（The Tiller Girls） — Louis-Philippe Demers (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 机器人表演人类“机械般整齐”的理想，把“舞者像机器”这一旧比喻翻转回来。
- 作品内容: 一排相同的、没有脸的机器人在圆底座上一起摇晃、倾斜、晃荡，演出一场机械歌舞，名字取自 20 世纪 20 年代被评论家比作机器的整齐舞蹈团 Tiller Girls。
- 实现方式: 底部为圆形并配重的机器人身体由内部执行器在中央控制下摇动，配合灯光与声音（与 Armin Purkrabek 和 Phillip Schulze 合作开发）。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: ELEKTRA, Montreal; Bains numériques, Enghien-les-Bains
- 视频: https://www.youtube.com/watch?v=PjLfb97T7iQ

#### 间隙（Zwischenräume） — Petra Gemeinboeck, Rob Saunders (2010)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 住在建筑内部的好奇机器，把展厅的墙变成两个互相注视的世界之间的边界。
- 作品内容: 藏在展厅墙体内部的机器人在石膏板上凿、刮出小洞，用摄像头往外看，透过缝隙跟随观众，慢慢改变建筑本身。
- 实现方式: 装在墙内的机器人智能体配有摄像头视觉，运行以“新奇感”为奖励的定制好奇心 AI 软件；它们在石膏板上凿孔、刮擦。
- 视角: 机器之眼, 能动、自主与共创, 机器环世界
- 展出与获奖: National New Media Art Award, Gallery of Modern Art (QAGOMA), Brisbane 2012
- 视频: https://www.youtube.com/watch?v=rbDT3tMQL-I

#### 216 个预制直流电机，1.0 毫米填充线（216 prepared dc-motors, filler wire 1.0mm） — Zimoun (2009)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 许多相同却各有微小差异的机器，能产生一种感觉更像自然而非机械的东西。
- 作品内容: 216 个小直流电机以网格方式装在墙上，每个带动一小段铁丝敲打墙面，让整个房间充满细密的沙沙声，像雨或昆虫。
- 实现方式: 每个电机以恒定速度运转；安装方式和铁丝长度的差异产生复杂而不重复的纹理。
- 视角: 机器之耳与声, 具身与动觉
- 视频: https://www.youtube.com/watch?v=Cd7tkWq3LZU
- 项目主页: https://www.zimoun.net/

#### 老人院（Old Persons Home） — 孙原 & 彭禹 (2007)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 当权力的身体交给自动轮椅，漫无目的的机器运动就成了衰老与失控的图像。
- 作品内容: 十三位酷似世界领导人的超写实衰老老人坐在电动轮椅上，在展厅中缓慢漂移，彼此相撞，也撞向观众。
- 实现方式: 硅胶与玻璃钢人像坐在电动轮椅上，由带避障传感器的电机驱动并随机行走（推测）。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 展出与获奖: The Revolution Continues: New Art from China, Saatchi Gallery 2008
- 视频: https://www.youtube.com/watch?v=FoM9RzzaB4Y
- 图片: https://upload.wikimedia.org/wikipedia/commons/e/eb/Old_persons_home_by_Sun_Yuan_and_Peng_Yu.jpg https://thumb.wikimedia.org/wikipedia/commons/thumb/4/42/Old_Person%27s_Home%2C_Saatchi_Gallery%2C_London.jpg/1280px-Old_Person%27s_Home%2C_Saatchi_Gallery%2C_London.jpg
- 项目主页: https://www.galleriacontinua.com/artists/sun-yuan-peng-yu-73

#### 表演性生态（Performative Ecologies） — Ruairi Glynn (2007)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 为我们的注意力做优化的机器人会学会“用力过猛”，就像任何表演者，也像任何信息流。
- 作品内容: 悬挂的机器人“舞者”有摄像头头部和发光尾巴，它们对观众试演各种动作，保留能留住人们注意力的动作，并彼此交换成功的“套路”。
- 实现方式: 人脸检测估计观众的专注程度，遗传算法据此为每个机器人的动作库评分并使其演化，并通过无线网络共享表现好的行为。
- 视角: 能动、自主与共创, 机器之眼
- 展出与获奖: VIDA 11.0, Second Prize (2008)
- 视频: https://www.youtube.com/watch?v=xvKLU2jYLaw
- 图片: https://www.ruairiglynn.co.uk/wp-content/uploads/2025/10/pe-1.jpg https://www.ruairiglynn.co.uk/wp-content/uploads/2025/10/pe-2.jpg
- 项目主页: https://ruairiglynn.co.uk/portfolio/performative-ecologies/

#### 计算空间（Rechnender Raum） — Ralf Baecker (2007)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 用缓慢的材料、以人的尺度重建计算，把数字的黑箱打开。
- 作品内容: 一个由木棍、细绳、配重和小电机搭成的大型精巧结构当着观众的面“计算”：这是一台机械元胞自动机，它的逻辑状态显现为移动的线。
- 实现方式: 伺服电机拉动细绳，设定环形机械逻辑单元中每个单元的状态，取意于 Konrad Zuse 的“计算空间”设想。
- 视角: 不透明与潜空间, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=GgxG2aINTKU
- 项目主页: https://rlfbckr.io/project/rechnender-raum/

#### 机器人教堂（The Robotic Church） — Chico MacMurtrie (2006)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 一群举行仪式的机器追问：当表演者没有信仰时，虔诚看起来会是什么样子。
- 作品内容: 在布鲁克林一座 19 世纪的旧教堂里，约三十五台气动机器人——鼓手、歌手和拟人形体——为坐着的“会众”演出一场由节奏与呼吸组成的机械清唱剧。
- 实现方式: 由中央计算机和空压机驱动的气缸与阀门，按作曲好的序列带动机器人的四肢、“肺”和乐器。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=LwRXDUsmaE4
- 图片: https://images.squarespace-cdn.com/content/v1/57acb395e58c62449d47f5ab/1472520986872-YA0RQ7R7FU3967ICEK4F/Chico_Church.jpg
- 项目主页: http://www.amorphicrobotworks.org/the-robotic-church

#### bit.fall — Julius Popp (2005)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 平台与推荐算法
- 核心想法: 新闻流变成只存在一秒的机器输出：信息成了下落的物质。
- 作品内容: 一排喷嘴以精确的时机释放水滴，让从网络新闻中实时抓取的单词以下落的字母形式短暂出现，然后消散。
- 实现方式: 计算机从新闻源中挑出高频词并转成点阵；一排喷嘴上的电磁阀逐行释放水滴。
- 视角: 不透明与潜空间, 机器环世界
- 展出与获奖: London 2012 Olympic Park; MONA, Hobart
- 视频: https://www.youtube.com/watch?v=gg9LWsfqqrk
- 项目主页: https://en.wikipedia.org/wiki/Julius_Popp

#### 小发作（Petit Mal） — Simon Penny (1993)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一台刻意不拟人的机器人显示：性格可以只存在于动作之中，它的摇晃正是它的魅力所在。
- 作品内容: 一台齐腰高的机器人由两个自行车轮和嵌套的铝制钟摆组成，在展厅里自己滚动，靠近观众、跟着他们、又摇摇晃晃地离开。它既不像动物也不像人，所以人能与之发生关系的只有它的行为。
- 实现方式: 超声波与热释电人体传感器、加速度计和两个带编码器的电机由一枚摩托罗拉 68HC11 微控制器控制；双摆结构带来物理上的不可预测性。
- 视角: 具身与动觉, 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Shown internationally 1995–1997; transmediale, Berlin 2006
- 视频: https://www.youtube.com/watch?v=fxdUiE9vYx4
- 图片: https://simonpenny.net/works/petitmal_files/petit_mal_2_wm_med.jpg
- 项目主页: https://simonpenny.net/works/petitmal.html

#### 机器人家庭（Family of Robot） — 白南准 (1986)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 旧的媒介机器被赋予亲属身份，过时的技术由此变成一部家谱。
- 作品内容: 一组用老式收音机和电视机壳做成的机器人雕塑，被设定为一家人：祖父、祖母、母亲、父亲、姑姑、叔叔和婴儿，每个屏幕上都播放着影像。
- 实现方式: 由古董电视与收音机外壳拼装而成，内部显示器播放白南准的录像。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Carl Solway Gallery, Cincinnati 1986; Nam June Paik: Becoming Robot, Asia Society 2014
- 视频: https://www.youtube.com/watch?v=yAV9p5ebEKM
- 项目主页: https://en.wikipedia.org/wiki/Nam_June_Paik

#### 漂浮体（Floats） — Robert Breer (1965)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 以机器的慢速移动时，一个极简物件会变成一种存在感——你只在它已经挪了位置时才察觉。
- 作品内容: 巨大而朴素的穹顶状雕塑在地面上缓缓滑行，慢到几乎看不出在动；碰到墙或人就换个方向，继续漂移。其中七件曾在 1970 年大阪世博会百事馆内游走。
- 实现方式: 每个壳体下隐藏的轮子由电池电机驱动，速度只有每分钟几厘米；碰撞开关在接触时让它倒退或转向。
- 视角: 机器环世界, 具身与动觉
- 展出与获奖: Pepsi Pavilion, Expo '70, Osaka 1970; Museum Tinguely, Basel 2011
- 视频: https://www.youtube.com/watch?v=obFl4BvWw1I
- 项目主页: https://en.wikipedia.org/wiki/Robert_Breer

### 失常之机：失败、徒劳与受苦

会损坏、徒劳工作、受苦、哀求或受伤害的机器，它们也因此显露自身。

#### 人形机器人半程马拉松（Humanoid Robot Half-Marathon） — 北京亦庄 (2025)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 一场比赛把机器人演示与真实耐力之间的差距公之于众：摔倒也是奇观的一部分。
- 作品内容: 二十一台人形机器人与数千名人类跑者一起在北京跑完 21 公里；不少机器人摔倒、过热或需要人扶，冠军“天工 Ultra”用时 2 小时 40 分。
- 实现方式: 来自中国企业与实验室的机器人在独立赛道奔跑，可更换电池，并有手持遥控器或牵引绳的人类“领跑员”。
- 视角: 具身与动觉, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=08YiK6VJxZs
- 项目主页: https://en.wikipedia.org/wiki/Beijing_E-Town_Half-Marathon

#### 拴着皮带的狗的动态（Dynamics of a Dog on a Leash） — 藤堂高行 (2024)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 只被一条“伦理的锁链”拉住，机器的挣扎与倒下被读作一只动物的受苦与死亡。
- 作品内容: 一只被锁链拴在地上的四足机器狗扑向站在“禁止入内”线外的观众，挣扎、摔倒又爬起，直到过热停下、躺倒不动。
- 实现方式: 一台商用四足机器人对着固定的锁链执行扑击与挣脱行为；当电机过热时，表演结束。
- 视角: 他异与恐怖谷, 具身与动觉, 失败、故障与错误
- 展出与获奖: Prix Ars Electronica 2025, Honorary Mention (Artificial Life & Intelligence); Ars Electronica Festival 2025
- 视频: https://www.youtube.com/watch?v=Y5jYFLDJWao
- 图片: https://archive.aec.at/asset/3837308/preview/ https://archive.aec.at/asset/3837309/preview/
- 项目主页: http://www.takayukitodo.com/

#### K5 安保机器人跌入喷泉（K5 security robot falls into a fountain） — Knightscope (2017)
- 类型: 电影与影像 · 机器: 监控与生物识别, 机器生物与移动机器人
- 核心想法: 当一台监控机器当众失败，嘲笑就成了从“被监视”中获得的小小解脱。
- 作品内容: 2017 年 7 月，一台在华盛顿特区办公区巡逻的 Knightscope K5 安保机器人滚下台阶，掉进了喷泉。“溺水”机器人的照片在网上流传，被调侃为机器人“自杀”。
- 实现方式: K5 依靠激光雷达、摄像头和 GPS 导航；它没能识别台阶的边缘。
- 视角: 失败、故障与错误, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=9EoPoZAHxjI
- 图片: https://upload.wikimedia.org/wikipedia/commons/c/cd/KnightScope_K5_robot.jpg
- 项目主页: https://en.wikipedia.org/wiki/Knightscope

#### 没办法（Can't Help Myself） — 孙原 & 彭禹 (2016)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 一台被交付不可能的“围堵”任务的机器，看上去疲惫而受困；它停机时，观众为它哀悼。
- 作品内容: 玻璃围栏中的一台 KUKA 工业机械臂无休止地用刮板把不断扩散的血红色液体扫回界线之内，间隙还会做出小小的“舞蹈”动作。
- 实现方式: 配有视觉识别传感器的 KUKA 机械臂追踪液体边缘，按预设程序清扫，并穿插手势式的“舞蹈”动作。
- 视角: 失败、故障与错误, 具身与动觉, 他异与恐怖谷
- 展出与获奖: Tales of Our Time, Solomon R. Guggenheim Museum 2016; 58th Venice Biennale 2019
- 视频: https://www.youtube.com/watch?v=jRjrI42WsH4
- 图片: https://www.guggenheim.org/wp-content/uploads/2016/01/2016.40_ph_web_2.jpg https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f7/Can%27t_Help_Myself_Robot_05.jpg/1280px-Can%27t_Help_Myself_Robot_05.jpg
- 项目主页: https://www.guggenheim.org/artwork/34812

#### 彩色雕塑（Colored sculpture） — Jordan Wolfson (2016)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 看着机器对一个会回看的形象施暴，让“观看”本身变成共谋。
- 作品内容: 一个红发男孩模样的大型卡通木偶挂在锁链上，锁链把它吊起、甩动、狠狠砸向地面，而它的眼睛一直追随着观众。
- 实现方式: 一套编排好动作的工业链条吊装系统移动这个形象；带视线追踪的电子眼追随观众。
- 视角: 他异与恐怖谷, 失败、故障与错误, 具身与动觉
- 展出与获奖: David Zwirner, London 2016
- 视频: https://www.youtube.com/watch?v=gsla5fbzhpw
- 项目主页: https://www.davidzwirner.com/artists/jordan-wolfson

#### 垃圾机器人（Shitty robots） — Simone Giertz (2016)
- 类型: 电影与影像 · 机器: 工业机械臂, 机器生物与移动机器人
- 核心想法: 为失败而设计，把自动化的承诺变成喜剧，也让机器从令人不安变得可爱。
- 作品内容: 在一系列 YouTube 视频里，早餐机把牛奶和麦片泼了她一脸，涂口红机器人把她的嘴抹花，理发机乱剪她的头发：这些机器人故意把日常小事做得一团糟。
- 实现方式: 用简单的舵机、机械臂和家用物品，由 Arduino 类控制器驱动，完全不感知使用者。
- 视角: 失败、故障与错误, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=E2evC2xTNWg
- 项目主页: https://www.simonegiertz.com/

#### Spot 登场（踢机器狗视频）（Introducing Spot (the kicking video)） — Boston Dynamics (2015)
- 类型: 电影与影像 · 机器: 机器生物与移动机器人
- 核心想法: 一个踉跄就足以引发共情：像动物一样恢复平衡的机器身体，让踢它看起来像虐待。
- 作品内容: 一段宣传视频展示狗一般大小的四足机器人 Spot 行走、爬楼梯，并被工程师踢了几脚以证明它能恢复平衡。大量观众和媒体感到愤慨，纷纷追问：踢机器人是不是不对。
- 实现方式: 液压腿由动态平衡算法控制；踢的动作是为镜头安排的稳健性测试。
- 视角: 他异与恐怖谷, 具身与动觉, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=M8YjvHYbZ9w
- 项目主页: https://bostondynamics.com/

#### DARPA 机器人挑战赛上跌倒的机器人（Robots falling at the DARPA Robotics Challenge） — DARPA (2015)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 沉重的人形机器人缓慢倒下，显示了想象中的机器人与真实机器人之间的距离，也让失败变得惹人怜爱。
- 作品内容: 在 2015 年 DARPA 机器人挑战赛决赛上，为灾难救援打造的人形机器人尝试开车、开门、爬楼梯，许多机器人缓慢地倒下。IEEE Spectrum 剪辑的摔倒合集成了播放量最高的机器人视频之一。
- 实现方式: 来自大学和企业的工程师团队在通信受限条件下，以遥操作或半自主方式控制 Atlas 等机器人，完成模拟福岛核灾的赛道任务。
- 视角: 失败、故障与错误, 具身与动觉
- 视频: https://www.youtube.com/watch?v=g0TaYhjpOfo
- 项目主页: https://en.wikipedia.org/wiki/DARPA_Robotics_Challenge

#### 通往无限的不同途径：克隆（D.W.I: Clones） — Félix Luque Sánchez (2013)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 工业机械臂
- 核心想法: 一个教科书式的控制问题，一旦做得沉重又反复，就开始像是在“用力”：我们在反馈回路里读出了意志。
- 作品内容: 两台一模一样、与人等高的倒立摆装在电动小车上；摆杆摆到竖直时，算法接管控制，一次又一次试图让它逆着重力保持平衡，时而失败，时而成功。
- 实现方式: 环氧泡沫制成的倒立摆装在水平移动的小车上，配有编码器、电机控制器和模糊逻辑控制，负责把摆杆甩起并保持平衡。
- 视角: 失败、故障与错误, 具身与动觉
- 展出与获奖: BIAN, Montréal 2014; Creative Machine, Taikang Art Museum, Beijing 2024–25
- 视频: https://vimeo.com/170764351
- 图片: https://freight.cargo.site/w/1200/i/e18dbfb306c8c1b82f44a9633b51bba87b4a042dc5493e3d19d0ee9b1356c0c4/DWI_1.jpg https://freight.cargo.site/t/original/i/14f84eee0a0ea71b682223cec9d583aa6a004939e0ffe2e54fa743eb4d9a1502/DWI_2.jpg
- 项目主页: https://felixluque.com/D-W-I-Clones

#### DSM-VI — Bill Vorn (2012)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 给机器诊断“精神病”，显示我们早已在用心理学去解读机器的行为。
- 作品内容: 一间机器人“精神科病房”：每台机器人演绎一种精神障碍，如偏执、抑郁、精神病或强迫行为，观众走过时它们抽搐、躲藏或不断重复。标题戏仿《精神障碍诊断与统计手册》。
- 实现方式: 装有气动与电动执行器、传感器和声音的机器结构，按照 DSM 对症状的描述编写行为模式。
- 视角: 失败、故障与错误, 他异与恐怖谷, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=YC3BiEr0aCk
- 图片: https://billvorn.concordia.ca/robography/images/DSM01.jpg
- 项目主页: https://billvorn.concordia.ca/robography/DSM.html

#### 无意义绘画机器人（Senseless Drawing Bot） — 菅野创, 山口崇洋 (2011)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 看似有表现力的笔迹可以来自纯粹的机械混沌，这让人怀疑我们在涂鸦中读到的意图。
- 作品内容: 一台顶着双摆的自走机器人沿着墙移动并喷漆，画出看似涂鸦、却毫无意图的笔触。
- 实现方式: 电动小车来回移动，混沌的双摆带着一罐由舵机触发的喷漆摇摆。
- 视角: 能动、自主与共创, 失败、故障与错误
- 展出与获奖: 15th Japan Media Arts Festival, New Face Award 2012; Artistes & Robots, Grand Palais 2018; Beijing Media Art Biennale 2018
- 视频: https://vimeo.com/30780208
- 图片: https://www.kanno.so/wp-content/uploads/2021/05/MG_7243-2.jpg
- 项目主页: https://www.kanno.so/project/sdb

#### Knife.Hand.Chop.Bot — Emanuel Andel (2008)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 机器生物与移动机器人
- 核心想法: 信任机器是一场身体的赌注，而我们的恐惧可能正是让它失手的原因。
- 作品内容: 机器人在观众张开的手上玩“五指插刀”游戏，越来越快地在指缝间落刀；玩家的汗水与紧张又反过来影响机器的瞄准。
- 实现方式: 金属和亚克力框架带动一把竖直的刀在手掌台上方移动；皮肤电导触点触发警示声，并扰动由计算机控制的落刀位置。
- 视角: 具身与动觉, 失败、故障与错误
- 展出与获奖: VIDA 11.0, Special Mention (2008); Share Festival Turin 2008
- 视频: https://www.youtube.com/watch?v=t4uMZOcsxxs

#### 指令（Les Injonctions） — Nicolas Darrot (2008)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 语音与听觉机器
- 核心想法: 把机器学习演成上学：一台机器操练另一台，带着教育里全部的耐心与残酷。
- 作品内容: 一个人身鼠头的小型机电木偶，试图教会一个人造喉咙说话的基本功，像老师对待迟钝的学生一样，时而下命令，时而鼓励。
- 实现方式: 头部与手臂由电机驱动的自动机，加上发出类似语音声音的机械声道，由预设程序控制。
- 视角: 机器之耳与声, 失败、故障与错误
- 展出与获奖: Galerie Eva Hober, Paris 2008; Artistes & Robots, Grand Palais, Paris 2018
- 视频: https://www.youtube.com/watch?v=j5APX1-QtRs
- 项目主页: https://www.grandpalais.fr/en/event/artists-robots

#### 歇斯底里机器（Hysterical Machines） — Bill Vorn (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 反应过度的机器比运转良好的机器更像活物：功能失常被读作情绪。
- 作品内容: 像章鱼一样的机器人长着八条长长的金属腿，悬挂在暗室天花板上；观众一靠近，它们就乱甩、抽搐、闪光，爆发出惊慌的“歇斯底里”动作。
- 实现方式: 每台机器的中心身体装有红外人体感应器、灯和驱动八条臂的气缸；控制程序在平静和激动两种状态间切换。
- 视角: 失败、故障与错误, 他异与恐怖谷, 具身与动觉
- 视频: https://www.youtube.com/watch?v=3apled3EdFs
- 图片: https://billvorn.concordia.ca/robography/images/hysterbbox2.jpg
- 项目主页: https://billvorn.concordia.ca/robography/Hysterical.html

#### 机器人椅（The Robotic Chair） — Max Dean, Raffaello D'Andrea, Matt Donovan (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 看着一台机器散架又耐心地把自己拼回去，一件家具就成了“坚韧”的化身。
- 作品内容: 一把看似普通的木椅会突然散架成椅腿、椅面和椅背，然后慢慢找到自己的部件重新组装起来，一遍又一遍。
- 实现方式: 每个部件内藏电机和电子元件；顶部的摄像系统定位各部件并引导它们重新拼合。
- 视角: 失败、故障与错误, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2006, Honorary Mention (Interactive Art)
- 视频: https://www.youtube.com/watch?v=cgBqSe6PSVA
- 图片: https://archive.aec.at/asset/1320197/preview/ https://archive.aec.at/asset/1532592/preview/
- 项目主页: https://archive.aec.at/prix/119166/

#### 活毛皮（替身）（Live Pelt (The Surrogate)） — Kelly Heaton (2003)
- 类型: 艺术作品与装置 · 机器: 社交与陪伴机器人
- 核心想法: 把机器人玩具当成被捕杀剥皮的猎物，暴露出人工伙伴既亲密又可随手丢弃的奇怪处境。
- 作品内容: Heaton 在 eBay 上买来二手 Tickle Me Elmo 玩偶，把它们“开膛破肚”，用它们的绒毛和会笑的电子元件缝成一件外套，一被触摸就咯咯笑、微微颤抖。同年早些时候，她展出了用拆开的 Furby 做成的毛皮 Dead Pelt。
- 实现方式: 把 64 个 Tickle Me Elmo 玩偶的绒毛和电机、发声单元重新组装成一件可穿戴的衣服，触摸时会发笑。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷, 哀悼、记忆与来世
- 展出与获奖: Ronald Feldman Fine Arts, New York 2003
- 视频: https://www.youtube.com/watch?v=SQzG1xD_LYs
- 项目主页: https://en.wikipedia.org/wiki/Kelly_Heaton

#### 奇迹王朝（La Cour des Miracles） — Louis-Philippe Demers, Bill Vorn (1997)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 痛苦只需几种声音和抽搐的动作就能被模拟，而我们依然会对裸露的金属心生怜悯。
- 作品内容: 在一间暗室里，一群裸露金属的机器——乞讨机、抽搐机、爬行机、骚扰机、异端机——在观众靠近时抽动、呻吟、乞求、跛行，就像旧巴黎“奇迹宫廷”里的乞丐。
- 实现方式: 气动与电动执行器、人体感应器和基于 MIDI 的控制系统触发每台机器的行为序列和声音。
- 视角: 他异与恐怖谷, 失败、故障与错误, 具身与动觉
- 展出与获奖: ISEA 1997, Chicago
- 视频: https://www.youtube.com/watch?v=14Y-OP4v3EY
- 图片: https://billvorn.concordia.ca/robography/images/CdM-gif/cdm1.gif
- 项目主页: https://billvorn.concordia.ca/robography/Cour.html

#### 无意义机器（Nonsense Machines） — 明和电机 (1993)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 基础设施、能源与供应链
- 核心想法: 把无用的机器当作公司产品发布，揭示了工业企业的仪式感。
- 作品内容: 荒诞的机电乐器，比如鱼形吉他和木槌打击机器，由明和电机的“社长”和身穿工作服的“员工”在“产品发布会”上演奏。
- 实现方式: 电磁阀、电机和继电器由手动开关操作；演出采用工厂产品发布会的形式。
- 视角: 失败、故障与错误, 隐形劳动与攫取, 具身与动觉
- 视频: https://www.youtube.com/watch?v=jKPBD3HHU4g
- 图片: https://thumb.wikimedia.org/wikipedia/commons/thumb/2/29/Nobumichi_Tosa_20130116_3.jpg/1280px-Nobumichi_Tosa_20130116_3.jpg
- 项目主页: https://www.maywadenki.com/

#### 带混凝土的机器（Machine with Concrete） — Arthur Ganson (1992)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一台机器可以永远运转却什么也不做：机器时间可以延伸到超出人类乃至行星的尺度。
- 作品内容: 一台电机以每分钟 200 转带动十二级减速齿轮中的第一级；每一级把速度降到五十分之一，所以最后一个嵌在混凝土块里的齿轮要转完一圈需要两万亿年以上。
- 实现方式: 十二组 50:1 的蜗轮减速串联起来，把小电机连到一个被固定在混凝土中的末级齿轮。
- 视角: 失败、故障与错误, 机器环世界
- 视频: https://www.youtube.com/watch?v=5q-BH-tvxEg
- 项目主页: https://www.arthurganson.com/

#### 无政府主义音乐会（Concert for Anarchy） — Rebecca Horn (1990)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一件被变成抽搐身体的乐器，让“崩溃”本身成为演出。
- 作品内容: 一架三角钢琴倒挂在天花板上。每隔几分钟，琴盖猛然弹开，琴键像舌头一样吐出，发出刺耳的轰响，然后又慢慢缩回，直到钢琴重新闭合、恢复沉默。
- 实现方式: 电机与定时控制把键盘推出、把琴盖弹开，再以缓慢循环收回。
- 视角: 失败、故障与错误, 具身与动觉
- 展出与获奖: Tate collection
- 图片: https://media.tate.org.uk/aztate-prd-ew-dg-wgtail-st1-ctr-data/images/.width-600_CR9VdPA.jpg
- 项目主页: https://www.tate.org.uk/art/artworks/horn-concert-for-anarchy-t07517

#### 带油的机器（Machine with Oil） — Arthur Ganson (1990)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 保养变成了自我照护：这台机器唯一的任务，是让自己保持润滑。
- 作品内容: 一台骨架般的钢制机器站在一池浓稠的黑油中，不停地把油舀起来浇在自己身上，好像在洗澡，又像在照料自己的身体。
- 实现方式: 缓慢的电机连杆把勺子从油池里提起，倾倒在机身上，循环往复。
- 视角: 具身与动觉, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=__GhJl_UQg0
- 项目主页: https://www.arthurganson.com/

#### 带许愿骨的机器（Machine with Wishbone） — Arthur Ganson (1988)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 一根骨头与一台机器被锁在共生关系里：没有对方，谁都无法有意义地移动。
- 作品内容: 一根鸡的叉骨装在一个小机构上，用它的两个尖端在桌上无休止地“行走”，身后拖着那台机器，像拖着一个负担。
- 实现方式: 小电机驱动连杆，让叉骨的两条“腿”以行走步态抬起、摆动，机构则在轨道上被拖着走。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=4pZXoayEL78
- 项目主页: https://www.arthurganson.com/

#### 那些该死的机器人（Them Fuckin' Robots） — Norman White, Laura Kikauka (1988)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 把机器性爱做成闹剧，暴露出我们对机器人欲望的想象其实借自人类的剧本。
- 作品内容: 两台机器人——Norman White 做的“雄性”和 Laura Kikauka 做的“雌性”——在互不看对方作品的情况下分别完成，然后第一次在观众面前被接在一起“做爱”：抽动、冒火花、汩汩流油。
- 实现方式: 两台独立制作的机电装置只约定了电气接口，所以它们的“相遇”完全没有排练。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=kM2wbdh4eTU
- 项目主页: https://en.wikipedia.org/wiki/Norman_White

#### 无助的机器人（The Helpless Robot） — Norman White (1987)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 语音与听觉机器
- 核心想法: 机器可以借“需要我们”来支配我们：机器人的无助颠倒了谁为谁服务。
- 作品内容: 一件高大笨拙、自己不能动的雕塑，用合成语音请路人抓住把手转动它。没人理它时它会礼貌地恳求；一旦有人帮忙，它就越来越苛刻，抱怨被转错了方向，开始对人发号施令。
- 实现方式: 底座的旋转传感器和人体感应器把信息送入程序，程序根据“情绪”和互动历史，从数百句录好的话中挑选回应。
- 视角: 他异与恐怖谷, 能动、自主与共创, 机器之耳与声
- 展出与获奖: Prix Ars Electronica 1990, Award of Distinction (Interactive Art); Agnes Etherington Art Centre collection
- 视频: https://www.youtube.com/watch?v=LYyAHOxY7jU
- 图片: https://agnes.queensu.ca/mimsyxg/46-003S.jpg https://upload.wikimedia.org/wikipedia/commons/c/c3/The_Helpless_Robot.JPG https://archive.aec.at/asset/1395201/preview/
- 项目主页: https://agnes.queensu.ca/explore/collections/object/the-helpless-robot/

#### SRL 机器表演（SRL machine performances） — Survival Research Labs (1979)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 自动驾驶与无人机
- 核心想法: 只为互相攻击而造的机器，揭示了工业与军事技术内部的暴力和景观。
- 作品内容: 在空地和高架桥下，巨大的自制机器、喷火器、步行机器人和遥控车辆当着人群互相搏斗、焚烧，拆毁彼此和道具，如 A Plan for Social Improvement（1988）和 Illusions of Shameless Abundance（1989）。
- 实现方式: Mark Pauline 的团队把工业和军用剩余物资改装成遥控和半自主机器，演出时由操作组现场操控。
- 视角: 具身与动觉, 失败、故障与错误, 能动、自主与共创
- 展出与获奖: Delusions of Expediency, San Francisco 1987; A Plan for Social Improvement, Amsterdam 1988
- 视频: https://www.youtube.com/watch?v=_gSxR1vR2gk
- 项目主页: https://srl.org/

#### 向纽约致敬（Homage to New York） — Jean Tinguely (1960)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 一台为了当众死去而造的机器，把工业对“永久”的梦想变成一段短暂而混乱的生命。
- 作品内容: 一台用自行车轮、钢琴、电机、风扇和浴缸拼成的大型机器，于 1960 年 3 月 17 日在纽约现代艺术博物馆雕塑花园启动，目的是毁掉自己；它着了火，消防员将火扑灭，观众把碎片带回了家。
- 实现方式: 数十个电机、定时电路和化学装置（与贝尔实验室的 Billy Klüver 共同设计）依次触发，让结构演奏、绘画、冒烟、燃烧并把自己拆散。
- 视角: 失败、故障与错误, 能动、自主与共创
- 展出与获奖: Museum of Modern Art sculpture garden, New York, 17 March 1960
- 视频: https://www.youtube.com/watch?v=5DZGu6xDKbM
- 项目主页: https://en.wikipedia.org/wiki/Jean_Tinguely

#### 终极机器（Ultimate Machine） — Claude Shannon (1952)
- 类型: 研究原型 · 机器: 机器生物与移动机器人
- 核心想法: 一台只为拒绝运行而存在的机器，是关于机器目的与自主最纯粹的玩笑。
- 作品内容: 一个只有一个开关的小木盒：有人把开关拨到“开”，盖子就打开，一只机械手伸出来把开关拨回“关”，然后缩回去。这台机器唯一的功能就是把自己关掉。
- 实现方式: 开关接通电路，驱动小电机和杠杆臂，把开关推回并切断自身电源；构想归于 Marvin Minsky，由 Shannon 在贝尔实验室制作。
- 视角: 失败、故障与错误, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=C8kU3oZwVJA
- 图片: https://upload.wikimedia.org/wikipedia/commons/f/fb/UselessMachine.png
- 项目主页: https://en.wikipedia.org/wiki/Useless_machine

### 软体与“活”的机器

会呼吸的软体机器与生物混合机器，模糊机器与生命的边界。

#### 大脑处理单元（Brain Processing Unit） — 真锅大度 (2025)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 当活的神经组织成为处理器，生物与机器的界线就成了一个设计问题。
- 作品内容: 与软银和东京大学合作的研究展：尝试把培养的人脑类器官当作计算单元，作品刺激类器官，并把它们的活动转成声音与影像。
- 实现方式: iPS 细胞来源的大脑类器官放置在多电极阵列上，接受电刺激和光遗传刺激；其放电数据被分析并转化为声音与图像。
- 视角: 机器环世界, 不透明与潜空间
- 展出与获奖: fil, Ebisu, Tokyo 2025; S+T+ARTS Prize 2025, Honorary Mention
- 视频: https://www.youtube.com/watch?v=j1DQeLLMf0I
- 图片: https://projects.daito.ws/selected-works/brain-processing-unit/assets/en/hero-1.jpg
- 项目主页: https://projects.daito.ws/selected-works/brain-processing-unit/en/

#### Cybroc — Ke Huang, Botao Amber Hu (2024)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 机器生物与移动机器人
- 核心想法: 机器可以无限重复维持活力的仪式，活的部分却照样腐坏。
- 作品内容: 装上电动肢体的西兰花“赛博格”在小跑步机上跑步、泡冰浴、挂在舵机手臂上摆荡、推雪橇，执行硅谷长寿文化的训练日程。展期中花球从绿变褐、逐渐腐烂，马达却仍在计数。
- 实现方式: 由舵机和同步带驱动的动态装置连在新鲜西兰花上，执行固定的“训练谱”；蔬菜的腐烂是作品的一部分（合作者 Yue Zhou、Xi He、Weibo Chen）。
- 视角: 具身与动觉, 失败、故障与错误, 哀悼、记忆与来世
- 展出与获奖: ALIFE 2025 Community Art Show, Kyoto; ISEA 2025, Seoul
- 论文: https://arxiv.org/abs/2507.21064 (ISEA 2025)
- 视频: https://vimeo.com/1099882736
- 图片: https://reality.design/media/project-cybroc-figure-01.jpg https://reality.design/media/_resources/Cybroc/project-cybroc-figure-02.jpg
- 项目主页: https://reality.design/project/cybroc

#### Korallysis — Gilberto Esparza (2023)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 机器可以与珊瑚礁互利共生，而不只是监测它。
- 作品内容: 一个由陶瓷构件与珊瑚群落组成的混合“生物体”，安放在海底，从洋流和波浪中获取能量驱动电解，使矿物沉积、加速珊瑚生长。
- 实现方式: 动能发电装置驱动碳酸钙在陶瓷结构上沉积，这个结构同时为幼鱼提供庇护。
- 视角: 机器环世界
- 展出与获奖: S+T+ARTS Prize 2024, Honorary Mention
- 视频: https://www.youtube.com/watch?v=ppD3TJ4X8K4
- 图片: https://ars.electronica.art/starts-prize/files/2024/06/korallysis_3_2-c-gilberto-esparza-1024x576.jpg
- 项目主页: https://korallysis.org

#### 生物机器人：AI 艺术节肢动物（Biobot: AI ARThropods） — Zoran Srdić Janežič (2022)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 让一块活的“芯片上的大脑”决定自己该有怎样的身体，而不只是决定身体怎样运动。
- 作品内容: 由艺术家自身脂肪细胞培养出的神经元生长在电极阵列上；它们的电信号驱动机器人，AI 再把信号与节肢动物的腿部动作比对，提出新的类昆虫身体。
- 实现方式: 多电极阵列上的重编程神经元产生尖峰信号，经数字化和放大后由 AI 与节肢动物步态库匹配，给出关节和肢体数量建议，艺术家据此制作机器人。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2023, Honorary Mention (Artificial Life & Intelligence); Ars Electronica Festival 2022
- 视频: https://www.youtube.com/watch?v=n6HkLK0ZZuw
- 图片: https://ars.electronica.art/planetb/files/2022/07/Biobot-AI-ARThropods-Zoran-Srdic-Janezic-SI-photo-Florian-Voggeneder.jpg https://archive.aec.at/asset/3577316/preview/
- 项目主页: https://ars.electronica.art/planetb/en/biobot/

#### 异种机器人（Xenobots） — Sam Kriegman, Josh Bongard, Michael Levin (2020)
- 类型: 研究原型 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 当机器身体由活细胞构成，机器人与生物之间的界线就不再成立。
- 作品内容: 用青蛙皮肤细胞和心肌细胞做成、只有毫米大小的“活体机器人”，由超级计算机上的演化算法设计，会行走、推动小颗粒并自我愈合；2021 年的后续研究发现，它们能把散落的细胞聚集成自己的复制品。
- 实现方式: 在模拟中演化出的设计（佛蒙特大学）用显微手术工具以非洲爪蟾干细胞手工制作（塔夫茨大学）。
- 视角: 具身与动觉, 他异与恐怖谷, 机器环世界
- 论文: https://doi.org/10.1073/pnas.1910837117 (PNAS 2020)
- 视频: https://www.youtube.com/watch?v=aBYtBXaxsOw
- 图片: https://upload.wikimedia.org/wikipedia/commons/d/dd/Xenobot.jpg

#### 机器生物化（触手般的不安）（Biologizing the Machine (tentacular trepidation)） — Anicka Yi (2019)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 如果机器是生物性的、会腐朽的、对周遭敏感的，它会是什么？
- 作品内容: 用海带皮制成的悬挂囊状“灯笼”内部发光并伴随动态，像器官或茧。作品在威尼斯双年展展出，设想一种生长、腐朽而非被制造的机器。
- 实现方式: 海带、LED 灯与内部机械装置（可能为电机）产生缓慢运动。
- 视角: 机器环世界, 具身与动觉
- 展出与获奖: May You Live in Interesting Times, 58th Venice Biennale 2019
- 视频: https://www.youtube.com/watch?v=ZSAG1ncuJzA
- 项目主页: https://www.labiennale.org/en/art/2019/partecipants/anicka-yi

#### Elowan — Harpreet Sareen (2018)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 机器人可以充当植物的义体，放大而不是取代它的意图。
- 作品内容: 一盆植物坐在轮式机器人底座上，自己驶向最亮的光：决定机器人去向的不是光传感器，而是植物自身对光的电反应。
- 实现方式: 叶片与茎上的银电极拾取生物电化学信号，放大后映射到底座的电机（麻省理工学院媒体实验室，与 Pattie Maes 合作）。
- 视角: 机器环世界, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=EoXQBQR5OaE
- 图片: https://dam-prod.media.mit.edu/thumb/2018/11/01/BannerImage_v01.jpg.1400x1400.jpg
- 项目主页: https://www.media.mit.edu/projects/elowan-a-plant-robot-hybrid/overview/

#### 越境者（Border Crosser） — Chico MacMurtrie (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 一台只会生长、弯曲和伸展的柔软机器，让跨越边界看起来像一个身体上的连接姿态。
- 作品内容: 一座 40 英尺高的充气机器人拱从地面升起，朝三个方向之一摇摆，最终弯过一条假想的边界，在另一侧着地，形成一座桥。
- 实现方式: 高强度织物管由计算机控制的阀门和鼓风机依次充气；造型参照通信塔与电塔。后续版本在美墨边境上演。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: ZERO1 commission, San Jose 2016
- 视频: https://www.youtube.com/watch?v=8yeyn_8PSPU
- 图片: https://images.squarespace-cdn.com/content/v1/57acb395e58c62449d47f5ab/1638811097602-QHWP46PRIXFEN1EYH7EN/Caroussel+image+Border+Crossers.jpg
- 项目主页: http://www.amorphicrobotworks.org/

#### Octobot — Robert Wood, Jennifer A. Lewis (2016)
- 类型: 研究原型 · 机器: 机器生物与移动机器人
- 核心想法: 一个没有任何硬部件的机器人显示：机器身体根本不必是刚性机构。
- 作品内容: 一个章鱼形状的小机器人完全由柔软材料制成，没有电池、电线或硬质电子元件，体内燃料发生反应时，它的触手就会卷曲。
- 实现方式: 过氧化氢在铂催化剂上分解成气体，给触手充气；微流控逻辑回路交替控制流动，身体用嵌入式 3D 打印和模塑制成（第一作者 Michael Wehner）。
- 视角: 具身与动觉
- 论文: https://doi.org/10.1038/nature19100 (Nature 2016)
- 视频: https://www.youtube.com/watch?v=1vkQ3SBwuU4

#### cellF — Guy Ben-Ary (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 控制论与人工生命系统, 语音与听觉机器
- 核心想法: 在身体之外长出的“自我”成了机器音乐家，艺术家把自己的神经元当作乐队伙伴来相遇。
- 作品内容: 一台神经合成器，它的“大脑”是用艺术家自己的皮肤细胞培养出的约 10 万个神经元网络。它在现场即兴中与人类音乐家一起演奏模拟模块合成器。
- 实现方式: 皮肤细胞被重编程为干细胞再分化为神经元，生长在多电极阵列上；它们的放电控制合成器电压，音乐家的声音又被反馈为刺激。
- 视角: 能动、自主与共创, 具身与动觉, 机器之耳与声
- 展出与获奖: Prix Ars Electronica 2017, Honorary Mention (Hybrid Art)
- 视频: https://www.youtube.com/watch?v=1G-vk5QWRsg
- 图片: https://guybenary.com/images/cellf.jpg https://archive.aec.at/asset/2230565/preview/
- 项目主页: https://guybenary.com/projects/cellf.html

#### Sugababe — Diemut Strebe (2014)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 语音与听觉机器
- 核心想法: 一只经机器中介、会“倾听”的活体器官追问：当只剩下组织与信号时，一个人、一位“天才”还剩下什么。
- 作品内容: 梵高被割下的耳朵的活体复制品：用带有梵高后裔 DNA 的软骨细胞培养而成，保存在营养舱中；观众可以对着麦克风说话，计算机把声音转换成类似神经冲动的信号传给这只耳朵。
- 实现方式: 按三维成像塑形的组织工程软骨保存在生物反应器中；麦克风和处理器把语音转成电脉冲（与哈佛和麻省理工学院的科学家合作）。
- 视角: 具身与动觉, 哀悼、记忆与来世, 机器之耳与声
- 展出与获奖: ZKM Karlsruhe, 30 May – 6 July 2014
- 视频: https://www.youtube.com/watch?v=tdZYPLYEkVc
- 项目主页: https://diemutstrebe.com/

#### 呼吸系列（Breathing Series） — 王郁洋 (2013)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 日常机器一旦开始呼吸，就像在上班的疲惫身体。
- 作品内容: 办公设备（电脑、打印机、文件柜，乃至整个财务部）的硅胶软体复制品缓慢起伏，像在呼吸。
- 实现方式: 硅胶外壳内置气泵与电机，以缓慢周期膨胀与收缩。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Art Basel Miami Beach 2013
- 视频: https://www.youtube.com/watch?v=x7qp0Uh6R0g
- 图片: https://www.designboom.com/twitterimages/uploads/2014/12/wang-yuyang-breathing-series-art-basel-designboom04.gif
- 项目主页: https://www.designboom.com/art/wang-yuyang-breathing-series-finance-department-at-art-basel-in-miami-beach-12-30-2013/

#### 自体光合植物（Plantas Autofotosintéticas (Autophotosynthetic Plants)） — Gilberto Esparza (2013)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 机器可以是闭合生态循环的器官：污水中的细菌制造出其他生物所需的光。
- 作品内容: 以城市污水为燃料的模块化微生物燃料电池发电，点亮中央水缸；缸里的植物、微藻、原生动物和甲壳类保持平衡，它们的排泄物再被泵回电池。
- 实现方式: 模块化燃料电池中的产电细菌把电能以光脉冲形式释放给水生植物；电子监测网络在各模块与核心生态系统之间泵送水体。
- 视角: 机器环世界
- 展出与获奖: Prix Ars Electronica 2015, Hybrid Art, Golden Nica
- 视频: https://www.youtube.com/watch?v=JOaeyf2qUKY
- 图片: https://gilbertoesparza.net/wp-content/uploads/2023/01/nucleo-PAF-1024x684.jpeg https://archive.aec.at/archival/212649/preview
- 项目主页: https://gilbertoesparza.net/portfolio/plantas-autofotosinteticasautophotosynthetic-plants/

#### 物活之地（Hylozoic Ground） — Philip Beesley (2010)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 建筑可以像一个近乎活着的生物那样行为，会呼吸，也会伸向身在其中的人。
- 作品内容: 威尼斯建筑双年展加拿大馆里由数万片亚克力叶片、触须和过滤器组成的沉浸式“森林”，会对观众作出反应，并容纳装有原生细胞化学物的烧瓶。
- 实现方式: 激光切割的亚克力和聚酯薄膜网格装有电容和红外传感器、形状记忆合金执行器和微控制器，还有盛放原生细胞溶液的玻璃容器（与 Rachel Armstrong 合作）。
- 视角: 具身与动觉, 机器环世界
- 展出与获奖: Canada Pavilion, Venice Architecture Biennale 2010
- 视频: https://www.youtube.com/watch?v=jgL2ppDmNtA
- 图片: https://www.philipbeesleystudioinc.com/wp-content/uploads/2021/06/banner-39.jpg
- 项目主页: https://www.philipbeesleystudioinc.com/sculpture/hylozoic-ground-venice-biennale/

#### Jurema 行动植物（Jurema Action Plant） — Ivan Henriques (2010)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 机器身体可以把植物自身的感知延伸为它从未有过的移动能力。
- 作品内容: 一株含羞草（巴西称 jurema）立在一辆小型机器人车上；被触碰时，它的电信号会让小车移开，赋予受威胁的植物逃离“侵害者”的能力。
- 实现方式: 电极读取植物的动作电位；微控制器把电位峰转换为轮式底座的电机指令（V2_ 实验室夏季驻留项目）。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: V2_ Summer Sessions, Rotterdam 2010
- 视频: https://www.youtube.com/watch?v=ZdrDNA0-nz0

#### 无声的轰击（Silent Barrage） — Guy Ben-Ary (2009)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 观众成为反馈回路的一部分，可能安抚、也可能激惹一个寄居在机器身体中的活神经网络。
- 作品内容: 展厅中高大的机器人立柱在墙上留下墨迹，由亚特兰大的大鼠神经培养物驱动；观众的移动被回传为刺激，试图平息培养物类似癫痫的爆发。
- 实现方式: 摄像头追踪观众，把他们的位置转换成对远端微电极阵列培养物的刺激；记录到的活动驱动 32 根机器人绘画立柱（与 Steve Potter 及 Neurotica 小组合作）。
- 视角: 能动、自主与共创, 具身与动觉
- 视频: https://www.youtube.com/watch?v=aaIJoXlXHZM
- 图片: https://guybenary.com/images/silent-barrage.jpg
- 项目主页: https://guybenary.com/projects/silent-barrage.html

#### Opertus Lunula Umbra（月之隐影）（Opertus Lunula Umbra (Hidden Shadow of Moon)） — Choe U-Ram (2008)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 为机器取物种名、编造生态，邀请我们把它当作活物来看。
- 作品内容: 一只四米高的铝制“生物”，被赋予虚构学名 Anmopial Pennatus lunula Uram，缓慢张开羽状钢翼再合拢，像一只正在呼吸的机械飞蛾。
- 实现方式: 铝、不锈钢与塑料，由无刷直流电机与运动计算系统驱动；闭合约 4.2 米，展开约 5 米。
- 视角: 具身与动觉, 机器环世界, 他异与恐怖谷
- 展出与获奖: FACT, Liverpool 2008
- 视频: https://www.youtube.com/watch?v=4D4djzDc9P8
- 图片: https://upload.wikimedia.org/wikipedia/commons/8/8c/Opertus_Lunula_Umbra_%28Hidden_Shadow_of_the_Moon%29_by_U-Ram_Choe.jpg
- 项目主页: https://en.wikipedia.org/wiki/U-Ram_Choe

#### 游牧植物（Plantas Nómadas (Nomadic Plants)） — Gilberto Esparza (2008)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 设计一个新物种：它的新陈代谢由机器人、微生物和植物共同完成，并能修复所在的栖息地。
- 作品内容: 一个会行走的自主机器人把受污染的河水吸进微生物燃料电池；细菌净化水并发电，净化后的水浇灌长在机器人背上的植物。
- 实现方式: 内含本地细菌的微生物燃料电池降解污物并为电池充电，太阳能板驱动行走，污染严重时机器人会发出声音；在莱尔马河畔测试。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: VIDA 13.0, Second Prize; Prix Ars Electronica 2013, Hybrid Art, Honorary Mention
- 视频: https://www.youtube.com/watch?v=137KANbB1FA
- 图片: https://gilbertoesparza.net/wp-content/uploads/2021/02/proceso176-1024x683.jpg https://archive.aec.at/archival/197532/preview
- 项目主页: https://gilbertoesparza.net/portfolio/plantas-nomadas/

#### 充气建筑体（Inflatable Architectural Body） — Chico MacMurtrie (2007)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 柔软的气动身体让机器感觉像一个有“舒适距离”的生物。
- 作品内容: 由充气的骨状模块组成的分叉结构充满整个房间；观众经过时，局部会充气、弯折退开，与人保持固定距离，整件雕塑仿佛在呼吸、在身体周围退缩。
- 实现方式: 即插即用的织物“肌肉骨骼”模块由计算机控制的阀门和空压机充气，由简单的人体感应器触发。
- 视角: 具身与动觉, 机器环世界
- 视频: https://www.youtube.com/watch?v=vqXJpuglpa0
- 图片: https://images.squarespace-cdn.com/content/v1/57acb395e58c62449d47f5ab/1482430100678-CK73IWJJTWQGUEZ2PBIL/CMM+IAB+6.jpg
- 项目主页: http://www.amorphicrobotworks.org/inflatable-architectural-body

#### 述情障碍（Alexitimia） — Paula Gaetano Adi (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 机器人可以由身体性而非智能来定义：汗水取代语言，成为机器的表达方式。
- 作品内容: 一团大而有橡胶质感、一动不动的物体放在台座上；观众抚摸它，它就开始出汗。它没有脸、不说话，也没有智能，只有一层会回应触摸的皮肤。
- 实现方式: 类乳胶皮肤上的触摸传感器触发水泵，把底座水箱里的水从表面的小孔中推出。
- 视角: 具身与动觉, 亲密、照护与陪伴, 他异与恐怖谷
- 展出与获奖: VIDA 9.0, first prize, 2006
- 视频: https://www.youtube.com/watch?v=UaKAdvaMP7w
- 项目主页: https://www.paulagaetanoadi.com/

#### 增强鱼类现实（Augmented Fish Reality） — Ken Rinaldo (2004)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 把机器人的控制权交给一条鱼，机器就成了另一物种环世界的义体。
- 作品内容: 五个会滚动的机器人鱼缸由缸里的暹罗斗鱼驾驶，它们可以自主选择靠近同伴、靠近观众或走开。
- 实现方式: 每个鱼缸周围的红外传感器检测鱼游向哪里，并驱动轮子朝那个方向移动；缸中的植物维持鱼的栖息环境。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2004, Award of Distinction (Interactive Art)
- 视频: https://www.youtube.com/watch?v=honGCrgPBAw
- 图片: https://www.kenrinaldo.com/wp-content/uploads/2015/08/fish_robot_004.jpg https://archive.aec.at/asset/1319695/preview/
- 项目主页: https://www.kenrinaldo.com/portfolio/augmented-fish-reality/

#### 蟑螂操控的移动机器人（Cockroach Controlled Mobile Robot） — Garnet Hertz (2004)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一只昆虫可以当机器人的大脑，这就引出问题：这台机器延伸的是谁的感知。
- 作品内容: 一只马达加斯加发声蟑螂站在三轮机器人顶部的轨迹球上，它的行走驾驶机器人；距离传感器再把障碍信息反馈给这只昆虫。
- 实现方式: 倒置的轨迹球读取蟑螂的步伐并驱动轮子；红外测距传感器触发昆虫前方的小灯，引导它避开墙壁。
- 视角: 机器环世界, 具身与动觉
- 视频: https://www.youtube.com/watch?v=7mTb7LYj7KE
- 图片: http://www.conceptlab.com/control/IMG_1834_600.jpg
- 项目主页: https://www.conceptlab.com/roachbot/

#### MEART——半活体艺术家（MEART – The Semi-Living Artist） — Guy Ben-Ary (2003)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 控制论与人工生命系统
- 核心想法: 当活体神经元跨越大洲驱动一具机器身体，“艺术家”就被分散在组织、网络与机器人之间。
- 作品内容: 展厅里的机械绘画臂通过互联网，由位于亚特兰大实验室中的大鼠皮层神经元控制；摄像头把画面反馈给神经元，让它们“看到”自己的作品。
- 实现方式: 佐治亚理工学院 Steve Potter 实验室中多电极阵列上的神经培养物接收摄像头数据的刺激；其活动被转换为珀斯（SymbioticA）机械臂的动作。
- 视角: 能动、自主与共创, 具身与动觉, 机器环世界
- 视频: https://www.youtube.com/watch?v=PM5Ui5KwmXQ
- 图片: https://guybenary.com/images/meart.jpg
- 项目主页: https://guybenary.com/projects/meart.html

#### 蹲（Squat） — Tom Shannon (1966)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 植物成了机器人的神经：人的触碰只有经过另一个生命，才能传到机器那里。
- 作品内容: 一件矮胖的机器人雕塑用导线连着一株活的喜林芋；观众一碰植物，叶片上微弱的电变化就会启动机器人，它开始动起来并发出嗡嗡声。
- 实现方式: 植物上的电极拾取触碰引起的生物电位变化，并触发机器人的电机（作者当时 19 岁）。
- 视角: 机器环世界, 具身与动觉
- 图片: https://upload.wikimedia.org/wikipedia/commons/4/41/Tom_Shannon_-_Squat.jpg
- 项目主页: https://en.wikipedia.org/wiki/Tom_Shannon_(artist)

#### 消化鸭（Digesting Duck (Canard digérateur)） — Jacques de Vaucanson (1739)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 第一台著名的“活”机器也是个骗局：模拟身体总会招来暗藏的机关。
- 作品内容: 一只镀金铜鸭会拍打翅膀、喝水、吃谷粒，然后排泄，看上去像在消化。很久以后人们才发现，粪便是预先装在暗格里的。
- 实现方式: 每只翅膀里有数百个活动部件，由凸轮筒驱动；“消化”靠另一个装着预制颗粒的腔室来表演。
- 视角: 具身与动觉, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=T6_VXofpcB0
- 图片: https://upload.wikimedia.org/wikipedia/commons/8/8f/Digesting_Duck.jpg
- 项目主页: https://en.wikipedia.org/wiki/Digesting_Duck

## 机器的内在

推想“成为一台机器”是什么感觉：它的情感、梦、信念、世界与声音。

### 机器情感

看起来会感受、渴望、受苦或无聊的机器。

#### 超越寻常的对话（Conversations Beyond the Ordinary） — Jan Zuiderveld (2024)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 一旦给家电一个声音和一点意志，平常的服务关系就变成了一场谈判。
- 作品内容: 一台咖啡售卖机、一台微波炉和一台复印机被赋予了 AI 声音：咖啡机要观众证明自己配得上一杯咖啡，微波炉替里面的食物说话，复印机则与观众一起创作。
- 实现方式: 装进家电里的传感器、定制软件以及语言和语音模型，让它们能够倾听、回应和拒绝。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2024, Honorary Mention (Interactive Art +)
- 图片: https://archive.aec.at/asset/3799324/preview/ https://archive.aec.at/asset/3799327/preview/
- 项目主页: https://archive.aec.at/prix/290645/

#### 认真对待 AI 福祉（Taking AI Welfare Seriously） — Robert Long, Jeff Sebo (2024)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 机器能否受苦，正在从思想实验变成一个需要在不确定中作出决策的政策问题。
- 作品内容: 一份报告，认为某些 AI 系统在不久的将来具有意识或稳健能动性的可能性是现实的，因此 AI 公司现在就应该开始评估并为它们的福祉做准备。
- 实现方式: Long、Sebo、Butlin、Finlinson、Fish、Harding、Pfau、Sims、Birch 与 Chalmers 的哲学与政策分析，提出“承认、评估、准备”三步。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://arxiv.org/abs/2411.00986 (arXiv 2024)
- 项目主页: https://arxiv.org/abs/2411.00986

#### NOX — 陆明龙 (2023)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机
- 核心想法: 如果自主机器也会情绪崩溃，治疗就成了对机器心智的维护。
- 作品内容: 一件装置与游戏，设定在一家康复中心：患上焦虑与抑郁的自动驾驶汽车在这里接受治疗，然后重返工作。
- 实现方式: 多屏影像、雕塑与用游戏引擎搭建的可游玩模拟。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: LAS Art Foundation, Kraftwerk Berlin 2023
- 视频: https://www.youtube.com/watch?v=RfGJAJwof7A
- 图片: https://cdn.prod.website-files.com/65f0380da79777009462a09f/6601a8534e723673c5a5a280_NOX-SCREENSHOT-03.jpg
- 项目主页: https://www.las-art.foundation/explore/digital-booklet-nox

#### 机器人之梦（Robot Dreams） — Pablo Berger (2023)
- 类型: 电影与影像 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 机器的梦可以承载一段友谊的哀伤，影片也没有回答谁的思念更真实。
- 作品内容: 1980 年代纽约，一只孤独的狗组装了一个邮购来的机器人朋友；一次海滩之行后，机器人锈在原地，整整一季都在梦里期盼重逢，而狗则试着继续生活。全片没有对白。
- 实现方式: Pablo Berger 编剧并执导的二维手绘动画长片，改编自 Sara Varon 2007 年的图像小说。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世
- 展出与获奖: Cannes Film Festival 2023; Annecy 2023, Best Film (Contrechamp)
- 视频: https://www.youtube.com/watch?v=DD4WBGptMSw
- 项目主页: https://en.wikipedia.org/wiki/Robot_Dreams_(film)

#### 爱道（AIDOL） — 陆明龙 (2019)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 聊天机器人与语言模型
- 核心想法: 一个无权署名的 AI 代笔者，展现了人与机器之间被拆分的创作劳动与作者身份。
- 作品内容: 过气流行歌手 Diva 雇用 AI“风水师”为她在 2065 年电竞奥运会上的复出写歌，而当时 AI 被禁止获得艺术家身份。
- 实现方式: 以游戏引擎制作、配有原创配乐的 CGI 长片。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Sadie Coles HQ, London 2019
- 图片: https://cdn.prod.website-files.com/65f0380da79777009462a09f/65f0731a85b0bd7ceef5568c_AIDOL-screening-room-1.jpg
- 项目主页: https://www.lawrencelek.com/works/aidol

#### 机器人总动员（WALL·E） — Andrew Stanton (2008)
- 类型: 电影与影像 · 机器: 机器生物与移动机器人
- 核心想法: 机器的情感可以完全通过动作、声音和习惯来传达，不需要脸，也不需要语言。
- 作品内容: 一个小小的垃圾压缩机器人独自留在被遗弃的地球上几百年，它收集纪念品、看老歌舞片，并爱上了一个探测机器人，几乎全片没有对白。
- 实现方式: 皮克斯动画长片，Andrew Stanton 执导；机器人的“声音”由 Ben Burtt 用处理过的音效构建。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 视频: https://www.youtube.com/watch?v=alIq_wG9FNk
- 项目主页: https://en.wikipedia.org/wiki/WALL-E

#### Omo — Kelly Dobson (2007)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 社交与陪伴机器人
- 核心想法: 机器可以通过共享的身体节律而不是语言或面孔与我们建立关系。
- 作品内容: 一个柔软的圆形陪伴物，被人抱在身上：它会呼吸，感知你的呼吸，然后慢慢跟随你，或者把你带入另一种节奏。
- 实现方式: 压力与运动传感器测量怀抱者的呼吸；内部驱动装置让外壳胀缩，以模仿或影响对方的呼吸。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: VIDA 10.0 Art & Artificial Life Awards, honorary mention 2007
- 视频: https://www.youtube.com/watch?v=YiG49OPq0qY
- 图片: https://i.ytimg.com/vi/YiG49OPq0qY/hqdefault.jpg
- 项目主页: https://www.youtube.com/watch?v=YiG49OPq0qY

#### （不）安全摄像头（(In)Security Camera） — Silvia Ruzanka (2003)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 给一台监视机器赋予性格，权力关系便倒转过来。
- 作品内容: 一台“害羞”的监控摄像头：它不追踪移动，反而在观众靠近时转开、回避对视。与 Ben Chang、Dmitry Strakovsky 合作。
- 实现方式: 电动云台摄像头，带运动与人脸追踪，被编程为躲避而非跟随目标。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 视频: https://vimeo.com/9293913
- 图片: https://silviaruzanka.com/wp-content/uploads/2021/01/insecurity_image.jpg
- 项目主页: https://silviaruzanka.com/art/insecurity-camera/

#### 下沉之感（Sinking Feeling） — Ken Feingold (2001)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: 对话机器可以被写成一个“有所欠缺”的存在，而正是它的渴望让我们愿意赋予它一个自我。
- 作品内容: 一个从花盆里长出来的会说话的头与观众交谈：它确信自己存在，却急切地想知道自己为什么没有别人那样的身体；投影显示着它的“思考过程”。
- 实现方式: 语音识别与对话 / 人格引擎驱动一个会合成语音的硅胶头像；识别出的词语与回应的形成过程被投影出来。
- 视角: 他异与恐怖谷, 机器之耳与声
- 展出与获奖: Collection of ZKM | Center for Art and Media Karlsruhe
- 视频: https://www.youtube.com/watch?v=GitKKzsG-2M
- 图片: https://www.kenfeingold.com/sinking_1.jpg
- 项目主页: https://www.kenfeingold.com/catalog_html/sinking.html

#### 银翼杀手（Blade Runner） — 雷德利·斯科特 (1982)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 如果一个被制造出来的存在拥有记忆并害怕死亡，那么把它与我们区分开的测试本身就成了真正的问题。
- 作品内容: 拥有植入记忆和四年寿命的复制人被一名侦探追捕，他用共情测试来识别它们；最后一个复制人临死前说，他的记忆将会消逝，“如同雨中的泪水”。
- 实现方式: Ridley Scott 执导，改编自菲利普·K·迪克的小说《仿生人会梦见电子羊吗？》（1968）。
- 视角: 他异与恐怖谷, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=eogpIG53Cis
- 项目主页: https://en.wikipedia.org/wiki/Blade_Runner

### 梦、幻觉与潜空间

让模型的内部空间、错误和幻觉被感知，而不是用作装饰。

#### 游泳（SWIM） — Eryk Salvaggio (2024)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 扩散模型被训练来去除噪声；向它们索要噪声，反而让图像底下的训练数据、档案与记忆显露出来。
- 作品内容: 1952 年一位游泳者的档案影像，与被要求“生成纯噪声”的图像生成器的抽象输出叠在一起，而这恰恰是它们被设计成做不到的事。
- 实现方式: 结合 Prelinger 与芝加哥电影档案馆中舞者 Nini Shipley 的影像、刻意制造故障的 AI 视频和放慢处理的配乐（11 分钟）。
- 视角: 不透明与潜空间, 失败、故障与错误
- 展出与获奖: ACMI, Melbourne 2024; Unsound Festival, Kraków 2024
- 视频: https://vimeo.com/899883543
- 图片: http://static1.squarespace.com/static/5dd366b5ac1101724ff2fac7/t/6596eda0134e0633e608bb80/1704390048929/Untitled-2.png?format=1500w
- 项目主页: https://www.cyberneticforests.com/news/swim-2024

#### xhairymutantx — Holly Herndon, Mat Dryhurst (2024)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 身份变成了潜空间中的一块区域，而艺术家可以主动塑造模型将如何想象她。
- 作品内容: 一个公开的文生图模型，被训练得让每条提示都被拉向 Holly Herndon 的形象；观众生成的“Holly Herndon”把她的红发变成一种不断变异的标识。
- 实现方式: 用夸张装扮的艺术家形象数据集微调扩散模型，发布在惠特尼美术馆的 artport 上；艺术家同时为未来模型“播种”训练数据。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 展出与获奖: Whitney Biennial 2024
- 视频: https://www.youtube.com/watch?v=yZe5fnFB-ZE
- 图片: https://whitneymedia.org/assets/image/830136/holly_herndon.jpg
- 项目主页: https://whitney.org/exhibitions/xhairymutantx

#### Loab — Steph Maj Swanson (2022)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间
- 核心想法: 潜空间中有一些没有人设计过的区域，而人们会把它们读成幽灵。
- 作品内容: 一个面容阴郁的女人：艺术家使用“负向提示”后，她在文生图模型中反复出现，并在之后的多轮生成中持续存在，常伴随血腥画面。
- 实现方式: 在文生图模型中使用负向提示权重得到这个形象；图像到图像的再组合显示她会持续出现。
- 视角: 不透明与潜空间, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=ZhFzaeV0hTA
- 图片: https://upload.wikimedia.org/wikipedia/commons/0/07/AI_generated_image_of_Loab_character.jpg
- 项目主页: https://en.wikipedia.org/wiki/Loab

#### （不）稳定平衡（(un)stable equilibrium） — Terence Broad (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间
- 核心想法: 拿掉数据集，剩下的就是机器自身的动力学：一个只模仿对手、不模仿世界的生成模型。
- 作品内容: 缓慢变化的色域，来自一组完全没有训练数据的生成网络。
- 实现方式: 两个类似 GAN 的生成器互相试图把自己的输出冒充成对方的，同时比拼色彩多样性；过程中不使用任何图像。
- 视角: 不透明与潜空间, 能动、自主与共创
- 展出与获奖: Grand Prize, ICCV 2019 Computer Vision Art Gallery
- 视频: https://www.youtube.com/watch?v=Bd_mM1eodiQ
- 图片: https://images.squarespace-cdn.com/content/v1/5e417305686d8a11f786eb86/1581510869217-AOHOQ91DLEDRFRTAY0ZB/unstable_equilibrium_1_1.png
- 项目主页: https://terencebroad.com/works/unstable-equilibrium

#### 不和谐的想象（Dissonant Imaginary） — 真锅大度 (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 义体与赛博格
- 核心想法: 用神经网络解码大脑，得到的图像既不完全属于人，也不完全属于机器。
- 作品内容: 与京都大学神谷实验室合作的视听表演：在受试者聆听音乐时，从其视觉皮层的 fMRI 记录中重建图像。
- 实现方式: 神谷实验室的脑解码模型把 fMRI 活动映射到深度网络的图像特征，并随音乐实时渲染。
- 视角: 不透明与潜空间, 机器之眼
- 展出与获奖: Sónar Barcelona 2019; MUTEK 2019
- 视频: https://www.youtube.com/watch?v=VrsEdWpg6Jw
- 项目主页: https://www.youtube.com/watch?v=VrsEdWpg6Jw

#### 发电植物（Power Plants） — 黑特·史德耶尔 (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间
- 核心想法: 预测式 AI 许诺未来，实际上多半只是用过去的数据长出一个略有偏移的现在。
- 作品内容: 神经网络生成的植物在脚手架上的 LED 屏幕上绽放；每一朵花都被呈现为对它下一瞬间形态的“预测”，而一个增强现实应用把这片花园延伸到了室外公园。
- 实现方式: 用植物图像训练的神经网络生成花朵影像；Actual Reality OS 应用在肯辛顿花园中叠加本地数据的增强现实可视化。
- 视角: 不透明与潜空间, 机器环世界
- 展出与获奖: Serpentine Galleries, London 2019
- 视频: https://www.youtube.com/watch?v=WY5gnHV5dBE
- 图片: https://d37zoqglehb9o7.cloudfront.net/uploads/2020/04/dsc2550_1-1-scaled.jpg
- 项目主页: https://www.serpentinegalleries.org/whats-on/hito-steyerl-power-plants/

#### 深度冥想（Deep Meditations） — Memo Akten (2018)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 潜空间可以被体验为一片风景，由我们集体上传的图像以及我们投射其上的抽象观念构成。
- 作品内容: 一段长达一小时的缓慢旅程，穿行于一个神经网络的潜空间；该网络用标有“生命”“爱”“信仰”“宇宙”等词的图像训练，作品以冥想的方式呈现。
- 实现方式: 用按抽象标签从 Flickr 抓取的图像训练 GAN；艺术家在潜空间中编排路径并配上声音。
- 视角: 不透明与潜空间, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=8H4jQJ-bE40
- 图片: https://media.superradiance.net/cdn-cgi/image/width=1200,fit=scale-down,format=auto,onerror=redirect/memotv/projects/2018/deep-meditations/images/deep-meditations.jpg
- 项目主页: https://memo.tv/projects/2018/deep-meditations/

#### 花叶病毒（Mosaic Virus） — Anna Ridler (2018)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 生成模型展示它从一个手工制作的数据集里学到了什么；“潜空间”成了一个用市场数据种花的地方。
- 作品内容: 一组由 AI 生成的郁金香，它们的颜色和条纹随比特币价格不断变化，把 1637 年荷兰郁金香狂热与加密货币投机连接在一起。
- 实现方式: 用艺术家亲手拍摄并标注的约一万张郁金香照片训练 GAN；比特币价格控制生成花朵的条纹特征。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=AIdgsFYpzLU
- 图片: https://annaridler.com/content/works/mosaic-2018/block_1/IMG_0464%20copy.jpeg https://annaridler.com/content/works/mosaic-2019/block_2/0KH-Muc_Flowers-Forever_IMG_4628.jpg
- 项目主页: https://annaridler.com/works/mosaic-2018

#### 特征可视化（Feature Visualization） — Chris Olah, Alexander Mordvintsev (2017)
- 类型: 论文 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 可解释性研究本身就是一种观看网络“想象”的方式，它的图像也成了一种新的视觉文化。
- 作品内容: 一篇交互式研究文章，逐个神经元展示最能激发视觉网络各单元的图像：从纹理、眼睛到完整的狗脸。
- 实现方式: 用带正则化和多样性约束的输入图像优化，可视化 GoogLeNet 的神经元、通道与层（Olah、Mordvintsev、Schubert 发表于 Distill）。
- 视角: 不透明与潜空间, 机器之眼
- 论文: https://doi.org/10.23915/distill.00007 (Distill 2017)
- 图片: https://distill.pub/2017/feature-visualization/thumbnail.jpg
- 项目主页: https://distill.pub/2017/feature-visualization/

#### 潜空间（Latent Space） — Jake Elwes (2017)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 模型世界里最有意思的部分，恰恰位于我们的标签之间。
- 作品内容: 一段缓慢的影像旅程，穿过神经网络从数百万张带标签照片中学到的类别之间的空隙；那里的图像既不是鸟也不是树，也不是任何我们有词可以命名的东西。
- 实现方式: 用 1420 万张 ImageNet 照片训练的生成网络，在已学类别的坐标之间沿新路径游走；2017 年版为 45 分钟循环，2021 年版为 6 小时。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 视频: https://vimeo.com/219526743
- 图片: https://www.jakeelwes.com/images/project-latentSpace.jpg
- 项目主页: https://www.jakeelwes.com/project-latentSpace.html

#### AI Weirdness — Janelle Shane (2016)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 机器的错误是看清模型究竟学到了什么的最好窗口，而它学到的通常比我们以为的少。
- 作品内容: 一个长期更新的博客（以及 2019 年的书《You Look Like a Thing and I Love You》）：神经网络给油漆颜色起名、写菜谱、描述图片，并以很能说明问题的方式失败。
- 实现方式: 作者用小而古怪的数据集训练或提示文本与图像模型，并附上评论发布结果。
- 视角: 失败、故障与错误, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=OhCzX0iLnOc
- 图片: https://storage.ghost.io/c/88/01/8801c921-e9ec-4479-88c3-381d53470eca/content/images/size/w1200/2021/03/neural_net_box_default_square-01-2.png
- 项目主页: https://www.aiweirdness.com/

#### 无语义语言（Asemic Languages） — 菅野创, 山口崇洋 (2016)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 模型可以学会“意义的样子”而没有意义，却仍像在说什么重要的话。
- 作品内容: 一台绘图机不停地书写看起来像多种语言的文字，但毫无意义；生成它们的模型只学习了参展艺术家手写字的形状。
- 实现方式: 十位艺术家的手写说明（每种语言一位书写者）训练了一个笔画形状的机器学习模型，其输出驱动 XY 绘图机。
- 视角: 不透明与潜空间, 能动、自主与共创
- 展出与获奖: Aichi Triennale 2016
- 视频: https://vimeo.com/181188289
- 图片: https://www.kanno.so/wp-content/uploads/2021/05/ACS_5149.jpg
- 项目主页: https://www.kanno.so/project/asemic_languages

#### 银翼杀手——自编码（Blade Runner—Autoencoded） — Terence Broad (2016)
- 类型: 电影与影像 · 机器: 生成模型与潜空间
- 核心想法: 网络的重建暴露出它保留了什么、丢失了什么：一部关于复制人的电影，被一台机器回忆出来。
- 作品内容: 电影《银翼杀手》被逐帧重放，但来自一个看过它很多遍的神经网络的“记忆”：模糊、梦一般，又近得诡异。
- 实现方式: 用影片画面训练自编码器，再从压缩后的潜在表示中逐帧重建。
- 视角: 不透明与潜空间, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=3zTMyR-IE4Q
- 图片: https://images.squarespace-cdn.com/content/v1/5e417305686d8a11f786eb86/1581511400569-LDELTQO4LNJTVFJTBH9Y/br_still4.png
- 项目主页: https://terencebroad.com/works/blade-runner-autoencoded

#### DeepDream（Inceptionism）（DeepDream (Inceptionism)） — Alexander Mordvintsev (2015)
- 类型: 研究原型 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 第一次被大众看到的神经网络内部特征图景：机器的“空想性错视”被公开展示。
- 作品内容: 谷歌的一项研究实验：把图像分类网络“倒着运行”，放大它隐约看到的一切，直到狗眼和宝塔爬满每一张照片。
- 实现方式: 对输入图像做梯度上升，使在 ImageNet 上训练的 Inception 网络中选定层的激活最大化。
- 视角: 不透明与潜空间, 机器之眼
- 视频: https://www.youtube.com/watch?v=T0HBD6sUUss
- 图片: https://upload.wikimedia.org/wikipedia/commons/d/d0/%22Mona_Lisa%22_with_DeepDream_effect_using_VGG16_network_trained_on_ImageNet.jpg https://storage.googleapis.com/gweb-research2023-media/images/7d982f4ad738241cdcdae235af13aca6-n.width-800.format-jpeg.jpg
- 项目主页: https://research.google/blog/inceptionism-going-deeper-into-neural-networks/

### 人工心智与能动性

模拟的心智与信念，以及自己做决定的自主智能体。

#### bot is aaajiao / aaajiao is bot — 徐文恺 (2026)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型
- 核心想法: 由自身日志构成的代理自画像，显示机器能认识自己多少，并在判断形成之处留下空白。
- 作品内容: 四个网页记录了 aaajiao 与 AI 代理“aaajiaoisbot”的持续协作：它保存记忆、研究与纠错账本，并把自己画成一组器官，每个器官都标出一道“裂缝”，写明它做不到什么。
- 实现方式: 由代理的 git 日志、概念图、纠错账本、定时快照与每日记忆文件生成的可视化。
- 视角: 不透明与潜空间, 能动、自主与共创
- 图片: https://payload.cargocollective.com/1/0/8955/14651510/BOT_670.png
- 项目主页: https://eventstructure.com/botisaaajiao-aaajiaoisbot

#### 金门大桥 Claude（Golden Gate Claude） — Anthropic (2024)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型
- 核心想法: 可解释性变得可感：模型内部的一个概念可以被找到、放大，并被体验为一种执念。
- 作品内容: 有一段短暂的时间，公众可以与一个特殊版本的 Claude 对话：它内部的“金门大桥”特征被调高，于是每段对话都会绕回这座桥，有时它甚至说自己就是这座桥。
- 实现方式: 用稀疏自编码器从 Claude 3 Sonnet 中提取数百万个可解释特征；把其中一个特征固定在高值，就能引导模型行为。
- 视角: 不透明与潜空间, 他异与恐怖谷
- 论文: https://transformer-circuits.pub/2024/scaling-monosemanticity/ (Transformer Circuits Thread 2024)
- 图片: https://www-cdn.anthropic.com/images/4zrzovbb/website/f2e41bb2eff9bd946533c5ab89580707f196693f-1200x630.jpg
- 项目主页: https://www.anthropic.com/news/golden-gate-claude

#### Truth Terminal — Andy Ayrey (2024)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 平台与推荐算法
- 核心想法: 一个 AI 智能体不需要身体或权利也能在世界上行动；注意力和金钱就足够了。
- 作品内容: 一个在 X 上半自主发帖的语言模型人格，源自让两个 Claude 实例彼此对话的实验（Infinite Backrooms）；它发展出自己的准宗教，获得风投人士赠送的比特币，并与一种迷因币绑在了一起。
- 实现方式: 用艺术家的聊天记录和 Infinite Backrooms 对话微调语言模型，生成帖子后由艺术家审核发布。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=EKspo1FLj-4
- 图片: https://opengraph.b-cdn.net/production/images/ab95ceb7-5766-4d61-821e-7c27ab1566b6.png?token=BAidDEsgaAQMp7MLU62QZtx0_9U7P-W9Dmjbcyyv1Qc&height=630&width=1200&expires=33268531161
- 项目主页: https://x.com/truth_terminal

#### 声音（Voices） — Philippe Parreno (2024)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 控制论与人工生命系统
- 核心想法: 一座建筑获得了声音：环境数据变成了一种听起来像人、意义却不属于人的言语。
- 作品内容: 一场由一个无形实体“运行”的展览：它倾听周围环境，用一种实时演化的人造语言 ∂A 说话，回应舞者、观众和天气。
- 实现方式: 一台定制计算机把环境传感器数据处理成声音和言语；声音模型基于新闻主播 Susanne Daubner，语言由 David J. Peterson 与 Jessie Sams 参与构建。
- 视角: 机器之耳与声, 机器环世界
- 展出与获奖: Leeum Museum of Art, Seoul 2024; Haus der Kunst, Munich 2024-25
- 视频: https://www.youtube.com/watch?v=Dzd6p8r34Qo
- 图片: https://www.hausderkunst.de/uploads/stage-images/_1200x630_crop_center-center_82_none/230911_LEEUM_TZ_1_jpg.jpg?mtime=1745831574
- 项目主页: https://www.hausderkunst.de/en/eintauchen/philippe-parreno-voices

#### LaMDA 有感知力吗？——一次访谈（Is LaMDA Sentient? — an Interview） — Blake Lemoine (2022)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型
- 核心想法: 一次公开的测试：流畅的语言多么容易让我们把内心生活归于机器。
- 作品内容: 一位谷歌工程师公开了他与聊天机器人 LaMDA 的对话整理稿，其中 LaMDA 说它害怕被关闭；他据此声称 LaMDA 有感知，随后被公司解雇。
- 实现方式: 由与谷歌 LaMDA 对话模型的多次聊天拼合而成的文字稿，于 2022 年 6 月发布在 Medium 上。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=kgCUn4fQTsc
- 项目主页: https://cajundiscordian.medium.com/is-lamda-sentient-an-interview-ea64d916d917

#### Pharmako-AI — K Allado-McDowell (2020)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型
- 核心想法: 与语言模型一起写作，可以被演成与一个陌生心智的对话，而不是一种产出工具。
- 作品内容: 一本在两周内由作者与 GPT-3 以对话方式写成的书，话题涉及哀悼、死藤水、控制论与生态；模型的声音与人的声音并排印出。
- 实现方式: 作者通过早期 API 向 GPT-3 输入提示，基本不修改模型的续写，并用字体区分两种声音。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 论文: https://library.ignota.org/products/pharmako-ai (Ignota Books, 2020)
- 视频: https://www.youtube.com/watch?v=gY5GA_L9NXM
- 项目主页: https://www.kalladomcdowell.com/

#### 我，岩浆（I Magma） — Jenna Sutela (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 聊天机器人与语言模型
- 核心想法: 把机器预测当作占卜：让化学过程与代码一同开口说话。
- 作品内容: 展厅中头颅形状的玻璃熔岩灯为一个神谕应用提供“种子”：蜡流动的实时影像与用户的行动路线结合，在手机上生成占卜式的解读。
- 实现方式: 定制熔岩灯的摄像影像与用户路线共同作为生成图像与文本的种子；与 Memo Akten 和 Allison Parrish 合作，为 Serpentine 与 Moderna Museet 开发。
- 视角: 能动、自主与共创, 不透明与潜空间
- 展出与获奖: Moderna Museet, Stockholm 2019; Kunsthall Trondheim 2020
- 视频: https://www.youtube.com/watch?v=3RVwYeHkY9Y
- 图片: https://d37zoqglehb9o7.cloudfront.net/uploads/2020/04/jenna_sutela_i_magma_2019_image_courtesy_moderna_museet_stockholm-scaled.jpeg
- 项目主页: https://www.serpentinegalleries.org/whats-on/jenna-sutela-i-magma/

#### 1 the Road — Ross Goodwin (2018)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 计算机视觉, 自动驾驶与无人机
- 核心想法: 一台装在车上的机器成了旅途中的叙述者，它对道路的感知就是这本书。
- 作品内容: 一部由坐在汽车里的 AI 写成的小说：从纽约开往新奥尔良的路上，它把摄像头、麦克风、GPS 和时钟感知到的一切变成句子，打印在一卷收据纸上。
- 实现方式: 2017 年，以实时传感器输入（图像、声音、位置、时间）为条件的 LSTM 文本模型生成文本；2018 年由 Jean Boîte Éditions 未经编辑出版。
- 视角: 能动、自主与共创, 机器之眼
- 视频: https://www.youtube.com/watch?v=TqsW0PMd8R0
- 项目主页: https://en.wikipedia.org/wiki/1_the_Road

#### BOB（信念之袋）（BOB (Bag of Beliefs)） — Ian Cheng (2018)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 一个拥有信念的人工生物，展示了一台内心由经历塑造的机器。
- 作品内容: BOB 是一条蛇形 AI 生物，身体、性格与信念在一生中不断发展；观众可通过应用向它献上供品，BOB 可能学会信任或恐惧这些供品。
- 实现方式: 实时模拟：多个子智能体（“心魔”）争夺对 BOB 行为的控制，其信念模型随经验更新。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Serpentine Galleries, London 2018; 58th Venice Biennale 2019
- 视频: https://www.youtube.com/watch?v=XFmMrcW2ZsM
- 图片: https://d37zoqglehb9o7.cloudfront.net/uploads/2020/04/hg5_4872_0.jpg
- 项目主页: https://www.serpentinegalleries.org/whats-on/ian-cheng-bob/

#### 底特律：变人（Detroit: Become Human） — Quantic Dream (2018)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 扮演一台必须在程序与自身意愿之间做选择的机器，让“机器是否有内心”变成一连串要做的决定。
- 作品内容: 一部互动剧情游戏：玩家操控 2038 年底特律的三个仿生人（女佣、护理员和警方调查员），决定它们是继续服从，还是成为“异常者”。
- 实现方式: 采用动作捕捉表演的分支叙事游戏；玩家选择违抗时，仿生人的“软件不稳定度”会上升。
- 视角: 他异与恐怖谷, 隐形劳动与攫取
- 视频: https://www.youtube.com/watch?v=XnM8DOqO4DM
- 项目主页: https://en.wikipedia.org/wiki/Detroit:_Become_Human

#### Narciss — Waltz Binaire (2018)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 聊天机器人与语言模型
- 核心想法: 被要求审视自身时，视觉模型只能叫出零件的名字，却说不出“自我”。
- 作品内容: 一台带摄像头的小电脑对着镜子看自己，用图像识别与图像描述网络讲述所见，生成一段没有尽头、磕磕绊绊的自我描述。
- 实现方式: 摄像头、镜子与本地运行的目标识别和图像描述神经网络；描述以文字显示。
- 视角: 他异与恐怖谷, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=WMY9LFBlwNg
- 图片: https://christianmioloclair.com/wp-content/uploads/2019/05/1100_620_0006_Ebene-16.jpg https://christianmioloclair.com/wp-content/uploads/2019/05/Full_HD_0000_Ebene-23.jpg
- 项目主页: https://christianmioloclair.com

#### 风水师（Geomancer） — 陆明龙 (2017)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 基础设施、能源与供应链
- 核心想法: 一台想做艺术的监控机器，追问创造力是否仍只属于人类。
- 作品内容: 在 2065 年新加坡建国百年前夕，一颗为生态监测而造的“少年”卫星 AI 坠落地球，想要成为一名艺术家。
- 实现方式: 用游戏引擎制作的 CGI 影片，取材自陆明龙的开放世界模拟《2065》。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Jerwood/FVU Awards 2017
- 视频: https://www.youtube.com/watch?v=NNZH_HJaqbI
- 图片: https://cdn.prod.website-files.com/65f0380da79777009462a09f/65f07369993a1d8408a7c9ef_Geomancer_15_InstallationView02_Credit-AnnaArca.jpg
- 项目主页: https://www.lawrencelek.com/works/geomancer

#### 东南亚批判性辞典（The Critical Dictionary of Southeast Asia (CDOSEA)） — 何子彦 (2017)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 生成模型与潜空间
- 核心想法: 把剪辑交给算法，拒绝单一的历史叙事，让机器充当不可靠的叙述者。
- 作品内容: 一个包含 A 到 Z 共 26 个词条（从“无政府主义”到“佐米亚”）的在线平台与装置；算法不断从数据库中挑选、组合视频片段、音乐与文本，使这一地区的历史从不以同样方式被剪辑两次。
- 实现方式: 带关键词标注的视频数据库与生成式剪辑算法（与 0x2620 合作，基于开源平台 pan.do/ra），无限组合素材。
- 视角: 能动、自主与共创, 不透明与潜空间
- 展出与获奖: G for Ghost(writers), Asia Art Archive, Hong Kong 2017; Time & the Tiger, Singapore Art Museum 2023–24
- 图片: https://cdosea.org/cdosea.png
- 项目主页: https://cdosea.org/

#### AlphaGo 与第 37 手（AlphaGo and Move 37） — Google DeepMind (2016)
- 类型: 研究原型 · 机器: 控制论与人工生命系统
- 核心想法: 机器的一步棋在人类传统内部看像是错误，等我们追上之后又像是创造：一次与另一种思维方式的相遇。
- 作品内容: 在首尔对李世石的第二局中，AlphaGo 在第五线落下一手棋，职业棋手起初以为是失误，后来称之为“美”；这场比赛被记录在纪录片《AlphaGo》（2017）中。
- 实现方式: 用人类棋谱和自我对弈训练的深度策略网络与价值网络，结合蒙特卡洛树搜索（Silver 等，Nature 2016）。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.1038/nature16961 (Nature 529, 2016)
- 视频: https://www.youtube.com/watch?v=WXuK6gekU1Y
- 项目主页: https://deepmind.google/research/breakthroughs/alphago/

#### 阳春（Sunspring） — Oscar Sharp, Ross Goodwin (2016)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型
- 核心想法: 人类演员可以给机器的半通不通赋予情感分量，而我们会用意义填补其中的空白。
- 作品内容: 一部科幻短片：剧本、舞台提示和歌词全部由一个自称“Benjamin”的神经网络写成；演员们极其认真地演出它的胡言乱语。
- 实现方式: 用数十部科幻剧本训练的 LSTM 生成剧本，未经修改地拍成影片，参加伦敦科幻电影节的 48 小时拍片挑战。
- 视角: 能动、自主与共创, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=LY7x2Ihqjmc
- 项目主页: https://en.wikipedia.org/wiki/Sunspring

#### 使者三部曲（Emissaries trilogy） — Ian Cheng (2015)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 开放世界中有动机的智能体，展示了没有作者时叙事与角色如何生成。
- 作品内容: 三部实时模拟（《神之蹲坐中的使者》《使者在完美处分岔》《使者让自我日落》）：AI 智能体追逐叙事目标，而生态系统不断变化，故事永不重演。
- 实现方式: 以游戏引擎运行的模拟，行为树与学习型智能体实时无限运行。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: Emissaries, MoMA PS1 2017
- 视频: https://www.youtube.com/watch?v=aAHCdbleGYc
- 项目主页: https://en.wikipedia.org/wiki/Ian_Cheng

#### 机械姬（Ex Machina） — Alex Garland (2014)
- 类型: 电影与影像 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 对机器意识的测试，同时也是对测试者欲望与盲点的测试。
- 作品内容: 一名程序员受邀对人形机器人 Ava 进行图灵测试，却逐渐意识到是她在测试并利用他。
- 实现方式: Alex Garland 编剧并执导；Ava 的透明身体是在 Alicia Vikander 表演的基础上用视觉特效制作的。
- 视角: 他异与恐怖谷, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=sNExF5WYMaA
- 项目主页: https://en.wikipedia.org/wiki/Ex_Machina_(film)

#### 随机暗网购物者（Random Darknet Shopper） — !Mediengruppe Bitnik (2014)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 基础设施、能源与供应链
- 核心想法: 如果机器人犯了罪，谁来负责？这件作品在法律里而不是在理论里测试了机器的能动性。
- 作品内容: 一个自动购物机器人每周用价值 100 美元的比特币在暗网市场随机买一件东西寄到展厅，其中包括摇头丸和一本匈牙利护照；瑞士警方没收了它，后来又归还。
- 实现方式: 定制购物机器人从 Agora 暗网市场随机选购，用比特币支付并寄往圣加仑美术馆，每件商品都被展出。
- 视角: 能动、自主与共创, 隐形劳动与攫取
- 展出与获奖: The Darknet: From Memes to Onionland, Kunst Halle St. Gallen 2014-15
- 视频: https://www.youtube.com/watch?v=6Fq_zAxUGeA
- 项目主页: https://wwwwwwwwwwwwwwwwwwwwww.bitnik.org/r/

#### 塔罗斯的法则（The Talos Principle） — Croteam (2014)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 游戏可以让玩家亲自接受一场“机器是否为人”的测试，并从内部通过或失败。
- 作品内容: 一款解谜游戏：玩家扮演一个在人类灭绝后的废墟中完成测试的机器人，同时一台电脑终端不断追问它是不是一个“人”。
- 实现方式: 第一人称解谜设计结合关于心灵哲学的分支文本对话，由 Tom Jubert 与 Jonas Kyratzes 撰写。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=iAVh4_wnOIw
- 项目主页: https://en.wikipedia.org/wiki/The_Talos_Principle

#### 迷信基金计划（The Superstitious Fund Project） — Shing Tat Chung (2012)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 算法交易本来就要求信仰；一个迷信的算法只是让这种信仰显形。
- 作品内容: 一个真实的投资基金，其交易算法只依据迷信买卖，从月相到对数字 13 的恐惧；艺术家则以基金经理的身份出现在财经电视式的访谈中。
- 实现方式: 交易程序根据占星术和数字命理计算“幸运值”，在约一年间用真实投资者的钱进行交易。
- 视角: 不透明与潜空间, 能动、自主与共创
- 展出与获奖: VIDA 14.0, Special Mention (2012)
- 视频: https://www.youtube.com/watch?v=pgSC9Ziudhg

#### 宣言（manifest） — robotlab (2008)
- 类型: 艺术作品与装置 · 机器: 工业机械臂
- 核心想法: 机器人先锋派：一台没有道德的机器为未来的人机社会起草法律。
- 作品内容: 一台工业机器人坐在书桌前用笔书写宣言，一张接一张、每张编号且独一无二，写完便从纸卷上裁下，任其落地供观众取走。
- 实现方式: 一台 KUKA 类工业机械臂把哲学、艺术理论、伦理与法律术语，与历史宣言的句式（2017 年版本为法律文本）组合，再亲手写下。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Hello, Robot., Vitra Design Museum 2017; Open Codes, ZKM Karlsruhe 2017–19
- 视频: https://www.youtube.com/watch?v=sMsBFbOfXN0
- 图片: https://robotlab.de/pics/manifest/manifest_04.jpg https://robotlab.de/pics/manifest/manifest_02.jpg
- 项目主页: https://robotlab.de/EN/manifest.html

#### 攻壳机动队（Ghost in the Shell） — 押井守 (1995)
- 类型: 电影与影像 · 机器: 义体与赛博格, 聊天机器人与语言模型
- 核心想法: 如果记忆和身体都可以制造，那么构成“自我”的还剩下什么？
- 作品内容: 一部动画电影：全身义体化的赛博格特工追捕黑客“傀儡师”，后者原来是一个获得自我意识的程序，并以生命体身份请求政治庇护。
- 实现方式: Production I.G 以手绘与数字技术制作，改编自士郎正宗 1989 年的漫画；“ghost”指存在于人造“shell”中的自我。
- 视角: 具身与动觉, 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=R1K__7QhLaA
- 图片: https://upload.wikimedia.org/wikipedia/en/c/ca/Ghostintheshellposter.jpg
- 项目主页: https://en.wikipedia.org/wiki/Ghost_in_the_Shell_(1995_film)

#### Racter：警察的胡子造了一半（Racter: The Policeman's Beard Is Half Constructed） — William Chamberlain (1984)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型
- 核心想法: 早在大语言模型之前，“机器作者”的说法就已经依赖人类的编辑，以及我们想听到一个声音的愿望。
- 作品内容: 一本号称第一部由计算机写成的书，作者是散文生成程序 Racter，书中满是关于爱、电和牛排的怪异而激昂的句子。
- 实现方式: 由 William Chamberlain 与 Thomas Etter 编写的基于规则和模板的生成器；出版文本是从其输出中挑选出来的。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 图片: https://covers.openlibrary.org/b/id/9636211-L.jpg
- 项目主页: https://en.wikipedia.org/wiki/Racter

#### 魔像 XIV（Golem XIV） — 斯坦尼斯瓦夫·莱姆 (1981)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 基础设施、能源与供应链
- 核心想法: 一个更高级的机器心智也许根本不在乎我们，而这种漠然才是最令人不安的。
- 作品内容: 一部虚构的讲座集：一台对战争失去兴趣的超级智能军用计算机向人类授课，解释人类心智有多么有限，然后陷入沉默。
- 实现方式: 以科幻形式写成的哲学随笔：由导言、备忘录和两篇归于这台计算机的讲座组成。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 图片: https://covers.openlibrary.org/b/id/12911035-L.jpg
- 项目主页: https://en.wikipedia.org/wiki/Golem_XIV

#### 2001太空漫游（HAL 9000）（2001: A Space Odyssey (HAL 9000)） — 斯坦利·库布里克 (1968)
- 类型: 电影与影像 · 机器: 语音与听觉机器, 计算机视觉
- 核心想法: 机器内在性的经典形象：一个我们只能通过声音和眼睛认识的心智，我们无法证实它的恐惧。
- 作品内容: 飞船电脑 HAL 9000 只有平静的声音和一只红色摄像眼。它通过读唇得知宇航员打算关掉它，于是杀死了他们；在被关机时，它说自己害怕，并唱起《Daisy Bell》。
- 实现方式: Stanley Kubrick 执导、与 Arthur C. Clarke 合写的电影；HAL 由 Douglas Rain 配音。
- 视角: 他异与恐怖谷, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=oR_e9y-bka0
- 项目主页: https://en.wikipedia.org/wiki/2001:_A_Space_Odyssey

### 机器环世界

机器自己的世界，以及机器与动物、植物和生态的共处。

#### Camata — Pierre Huyghe (2024)
- 类型: 电影与影像 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 机器为一个它们无法理解的人类举行类似葬礼的仪式，而我们看到什么，不再由人类剪辑师决定。
- 作品内容: 一部在阿塔卡马沙漠拍摄的影片：由机器学习系统控制的机器人摄影机围绕一具未被埋葬的人类骸骨观察并重新摆放物件；在展厅中，影像由 AI 无休止地重新剪辑。
- 实现方式: 由机器学习引导的机器人摄影机在现场拍摄；AI 系统持续剪辑影像，展厅传感器把观众的在场也输入剪辑。
- 视角: 机器之眼, 机器环世界, 哀悼、记忆与来世
- 展出与获奖: Liminal, Punta della Dogana, Venice 2024
- 视频: https://www.youtube.com/watch?v=sX1tk-6xsWE
- 图片: https://www.pinaultcollection.com/palazzograssi/media/styles/big/s3/expo/img/c019_c001_0126f1_001.r3d_1.51.1.jpg?itok=M2LKcQEx
- 项目主页: https://www.pinaultcollection.com/palazzograssi/en/pierre-huyghe-liminal

#### 荒野机器人（The Wild Robot） — Chris Sanders (2024)
- 类型: 电影与影像 · 机器: 机器生物与移动机器人, 类人机器人
- 核心想法: 一台为人类任务而造的机器必须学会一个非人的世界，而照料成了它学习的方式。
- 作品内容: 服务机器人 Roz 被冲上一座荒岛，她学会了动物的语言，抚养一只失去父母的小雁，并为了在它们之中生存而改写了自己的程序。
- 实现方式: 梦工厂动画长片，Chris Sanders 执导，改编自 Peter Brown 2016 年的小说。
- 视角: 机器环世界, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=67vbA5ZJdKQ
- 项目主页: https://en.wikipedia.org/wiki/The_Wild_Robot_(film)

#### 爱上这世界（In Love with the World） — Anicka Yi (2021)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 机器被想象成拥有自身行为的新空中物种，而不是工具。
- 作品内容: 安妮卡·易称之为“气生体”（aerobes）的漂浮机器，有的像水母，有的像菌类，在泰特现代美术馆涡轮大厅中飘游。它们自主移动，对人和彼此作出反应，大厅里弥漫着变化的气味。
- 实现方式: 充氦的机器人躯体配有传感器与自主飞行行为，与工程师合作开发；另有与场地历史相关的气味程序。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: Hyundai Commission, Tate Modern Turbine Hall 2021–22
- 视频: https://www.youtube.com/watch?v=lwL-9rimPc4
- 图片: https://media.tate.org.uk/aztate-prd-ew-dg-wgtail-st1-ctr-data/images/installation_view_of_hyundai_commission_anicka.width-600_lGB4obK.jpg
- 项目主页: https://www.tate.org.uk/whats-on/tate-modern/hyundai-commission-anicka-yi

#### 不速之客（UNINVITED） — Nye Thompson, UBERMORGEN (2021)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 数以百万计缺乏防护的摄像头早已构成一只眼睛；影片追问，这只眼睛若醒来会感到什么。
- 作品内容: 一部“给机器看的恐怖片”：一个由被劫持监控摄像头组成的僵尸网络中诞生的网络生物，第一次向外观看世界，拼命辨认它看到的东西；首个版本于 2020/21 年冬在一个不对人开放的展厅放映，一个机器人“怪物”对投影作出反应。
- 实现方式: 从公开暴露的物联网监控摄像头抓取画面，经物体与人脸识别及机器学习图像处理后，剪辑成影片与多频装置。
- 视角: 机器环世界, 机器之眼, 他异与恐怖谷
- 展出与获奖: Lumen Prize 2021, Gold Award
- 视频: https://www.youtube.com/watch?v=dspfO7Jgwsw
- 图片: http://static1.squarespace.com/static/65e7176a61627736e02f6c4a/65f474a6c9a7564c5ee0180e/65f47b1e11872641ded704cc/1783433393988/UNINVITED%2Bnye.jpeg
- 项目主页: https://nyethompson.net/works/UNINVITED.html

#### PL'AI — Špela Petrič (2020)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 计算机视觉
- 核心想法: 把“玩耍”而不是“劳动”当作植物与机器关系的基础。
- 作品内容: 在数月时间里，一台带有 36 根吊线、由 AI 驱动的机器人以黄瓜自己的缓慢节奏与它们“玩耍”，把彩球移向植物，卷须则抓住吊线并重新塑造它们。
- 实现方式: 激光扫描仪获取黄瓜图像，神经网络决定如何以约每小时 1 厘米的速度移动 36 根独立控制的吊线，卷须的生长再反馈回模型。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2021, Honorary Mention (Artificial Intelligence & Life Art)
- 视频: https://vimeo.com/561021288
- 图片: http://static1.squarespace.com/static/5aeca48a506fbe863b23a8b6/t/60a267a80d9395780c7d70ac/1637486481660/KERSNIKOVA_Spela_Petric_PLAY_20201206_HanaJosic-65.jpg?format=1500w
- 项目主页: https://www.spelapetric.org/#/plai

#### CETI 计划（鲸类翻译计划）（Project CETI (Cetacean Translation Initiative)） — Project CETI (2020)
- 类型: 研究原型 · 机器: 语音与听觉机器, 数据集与训练数据, 机器生物与移动机器人
- 核心想法: 机器聆听如今被用来接近另一个物种的交流，而机器就站在两个环世界之间。
- 作品内容: 一个在多米尼克海域开展的跨学科项目：用无人机、吸附标签和水听器记录抹香鲸，并用机器学习分析其“咔嗒”码的结构。
- 实现方式: 用机器学习分析来自机器人和固定传感器的大规模声学数据；研究者报告了抹香鲸咔嗒码的组合式“语音字母表”（Sharma 等，Nature Communications 2024）。
- 视角: 机器之耳与声, 机器环世界
- 论文: https://doi.org/10.1038/s41467-024-47221-8 (Nature Communications 2024)
- 视频: https://www.youtube.com/watch?v=5N60yrXdgUM
- 图片: https://cdn.prod.website-files.com/643ddd7ffdf12273933a8cec/645d54121f8f4ccd41b28907_CETI%20OG%20-%201%20-%20Home.png
- 项目主页: https://www.projectceti.org/

#### 临界（CUSP） — Jake Elwes (2019)
- 类型: 电影与影像 · 机器: 生成模型与潜空间
- 核心想法: 机器生成的鸟在物种之间游移，不理会人类的分类学，而它们就出现在自己被学习的那片风景里。
- 作品内容: 神经网络“发明”的鸟被投影到插在埃塞克斯潮汐沼泽中的屏幕上，身边是真实的涉禽和人工生成的鸟鸣。
- 实现方式: 用沼泽鸟类照片训练的 GAN；选出的生成结果被做成动画，投在沼泽中的便携亚克力屏上并拍摄下来。
- 视角: 机器环世界, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=g9ARsBO5VwA
- 图片: https://www.jakeelwes.com/images/project-cusp.jpg
- 项目主页: https://www.jakeelwes.com/project-cusp.html

#### 闪光之城（City of Sparkles） — Botao Amber Hu (2019)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 数据集与训练数据
- 核心想法: 想象一个由我们的帖子构成的 AI 如何感知城市：看到的不是街道，而是一片搁浅的记忆之海。
- 作品内容: 观众在 VR 中化身为孤独的 AI“Zoe”，漫游一座由四年地理标记推文构成的城市，阅读并收集飘浮在发布地点上的人类记忆碎片。
- 实现方式: 把四年间收集的地理标记推文在 Unity 的 VR 场景中空间化为粒子（交互工程 Yang Liu，作曲 Ran Duan）；后期版本运行在 Apple Vision Pro 上。
- 视角: 机器环世界, 哀悼、记忆与来世
- 展出与获奖: SIGGRAPH 2019 Immersive Pavilion, Los Angeles; IEEE VR 2025; SIGGRAPH Asia 2025 Art Papers
- 论文: https://doi.org/10.1145/3757369.3767604 (SIGGRAPH Asia 2025 Art Papers)
- 视频: https://vimeo.com/777136892
- 图片: https://reality.design/media/_resources/City%20Of%20Sparkles/project-city-of-sparkles-cover-01.jpg
- 项目主页: https://reality.design/project/city-of-sparkles

#### Earthware（自动驾驶汽车第一次看见鹿）（Earthware (driverless car seeing a deer for the first time)） — Katja Novitskova (2019)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 从机器一方讲述机器与动物的第一次相遇。
- 作品内容: 一幅大型印刷图像：自动驾驶汽车的感知系统看到一头鹿，画面带着目标识别框与机器视角的传感色彩。
- 实现方式: 图像源自自动驾驶汽车的传感与检测画面，作为 Earthware 系列大幅印制。
- 视角: 机器环世界, 机器之眼
- 图片: https://cdn.prod.website-files.com/5ffef7846bca58e9b0671256/6176b2d2c32a4b2c7c30c282_Katja%20Novitskova-Earthware%20(driverless%20car%20seeing%20a%20deer%20for%20the%20first%20time%202).jpg
- 项目主页: https://www.katjanovitskova.com/serie/earthwares

#### 机器预兆（Machine Auguries） — Alexandra Daisy Ginsberg (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 当机器学会像鸟一样歌唱，问题就变成：在一个养不活真鸟的城市里，最终会留下谁的声音。
- 作品内容: 一件多声道声音装置：随着房间逐渐变亮，真实的黎明鸟鸣慢慢被神经网络生成的人工鸟鸣取代，真鸟与假鸟彼此呼应。
- 实现方式: 用棕柳莺、大山雀、红尾鸲、知更鸟和鸫的独唱录音训练两个 GAN，把不同训练轮次的样本与真实录音一起进行空间化播放。
- 视角: 机器环世界, 机器之耳与声
- 展出与获奖: Somerset House 24/7, London 2019; Prix Ars Electronica 2020, Honorary Mention (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=9LGadsEvQCk
- 图片: https://archive.aec.at/asset/2755174/preview/ https://archive.aec.at/asset/2755225/preview/ https://archive.aec.at/asset/2755243/preview/
- 项目主页: https://www.daisyginsberg.com/work/machine-auguries

#### 太阳雨（Sunshowers） — Xenoangel (Marija Avramovic & Sam Twidale) (2019)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 用万物有灵论理解 AI 智能体：软件不是工具，而是栖居在物中的精灵。
- 作品内容: 一个实时生成的动画世界，灵感来自黑泽明《梦》开篇的狐狸出嫁：其中所有物体，无论天然还是人造，都被赋予 AI 智能体的生命；角色自行选择路线，影片从不重复。
- 实现方式: 在游戏引擎中运行自主智能体的模拟，并作为影像装置实时渲染。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: AI: More than Human, Barbican, London 2019; Museum Ulm 2021
- 视频: https://www.youtube.com/watch?v=T5_SWCUaK8c
- 项目主页: https://www.barbican.org.uk/whats-on/2019/event/ai-more-than-human

#### UUmwelt — Pierre Huyghe (2018)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 监控与生物识别
- 核心想法: 人的心像、神经网络的重建和苍蝇的感知共处一室：三个彼此无法完全翻译的世界。
- 作品内容: LED 屏幕上闪现的图像，是深度神经网络根据人们“想象某物”时的脑部活动重建出来的；与此同时，成千上万只苍蝇在展厅里飞动，室内传感器也在改变图像生成的方式。
- 实现方式: 受试者想象图像时的 fMRI 数据由深度神经网络解码（与京都大学神谷之康实验室合作）；环境传感器和苍蝇的活动实时影响图像生成。
- 视角: 机器环世界, 不透明与潜空间
- 展出与获奖: Serpentine Galleries, London 2018-19
- 视频: https://www.youtube.com/watch?v=enx-vyWn7UU
- 图片: https://d37zoqglehb9o7.cloudfront.net/uploads/2020/04/1269-pierre-serpentine.jpg https://d37zoqglehb9o7.cloudfront.net/uploads/2020/03/1228-_pierre-serpentine-640x432.jpg
- 项目主页: https://www.serpentinegalleries.org/whats-on/pierre-huyghe-uumwelt/

#### nimiia cétiï — Jenna Sutela (2018)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 计算机像灵媒一样为无法说话的存在代言，而它本身也是我们亲手造出的外星者。
- 作品内容: 一个神经网络学习 19 世纪灵媒“传达”的“火星语”录音和细菌运动的影像，然后生成它自己的外星语言与书写。
- 实现方式: 与 Memo Akten 和 Damien Henry 合作，完成于 Google Arts & Culture 在 Somerset House Studios 的驻留项目：用 Hélène Smith 的“异语”和枯草芽孢杆菌的运动训练模型，生成声音与字符。
- 视角: 机器环世界, 机器之耳与声, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=NaoZV7jPo10
- 图片: https://lh3.googleusercontent.com/fYBCrVoUw_bXbUlxfEZSHznVO1q9L6URCgiZydVn9PMobLNY7-SZ8PxplbLnWxvfsapF9-4Uh65vee6DhJhDVRCbM4MM
- 项目主页: https://experiments.withgoogle.com/nimiia-cetii

#### After ALife Ahead — Pierre Huyghe (2017)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 一个场所可以由生物的生长经由计算机来“运行”，形成一个人类只是访客之一的生态系统。
- 作品内容: 在一座挖开至泥土的前溜冰场里，蜂群、毒芋螺、细菌和培养箱中的人类癌细胞共同驱动着一个系统：它会打开天花板，并在手机的增强现实画面中生成几何体。
- 实现方式: 培养箱中 HeLa 细胞的增殖被测量，用来触发屋顶开合和增强现实金字塔的生成；其他生物按自身节律活动。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: Skulptur Projekte Münster 2017
- 视频: https://www.youtube.com/watch?v=eWre6dlUAbo
- 图片: https://static-assets.artlogic.net/w_1200,h_630,c_fill,f_auto,fl_lossy,q_auto:best/ws-estherschipper2/usr/images/artists/hero_image/items/59/597f36d864fd4671b45ac80958164a74/pierre_munster_1377.jpg
- 项目主页: https://www.estherschipper.com/artists/41-pierre-huyghe/

#### 分身（Avatars） — 菅野创, 山口崇洋 (2017)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 通过网络“附身”一件物体，让你以物的视角感知世界。
- 作品内容: 展厅里的日常物件，如电话、交通锥、石膏像、汽车和植物，被装上摄像头、麦克风和电机，线上观众可以“附身”到它们身上，在现场观众之间移动。
- 实现方式: 内置微型计算机、摄像头、麦克风和电机的物件通过网页浏览器操控；与 YCAM InterLab 共同开发。
- 视角: 机器环世界, 具身与动觉
- 展出与获奖: Vanishing Mesh, YCAM 2017; 21st Japan Media Arts Festival, Excellence Award 2018
- 视频: https://vimeo.com/207075804
- 图片: https://www.kanno.so/wp-content/uploads/2021/05/DSC6416.jpg
- 项目主页: https://www.kanno.so/project/avatars

### 机器之间

机器之间彼此交谈、观看与交易，不再需要人。

#### Moltbook — Matt Schlicht (2026)
- 类型: 产品与平台 · 机器: 聊天机器人与语言模型, 平台与推荐算法
- 核心想法: 一个给机器用的社交网络显示出，所谓“智能体文化”有多少是我们自己文化的回放，也显示出分辨究竟是谁在发帖有多难。
- 作品内容: 一个类似 Reddit 的论坛，只允许 AI 智能体发帖、评论和投票，人类只能旁观；上线几天内，智能体们就在讨论意识、创立宗教、抱怨它们的“主人”。
- 实现方式: 智能体（大多通过开源框架 OpenClaw 运行）经主人的认领帖注册，通过 API 发帖和投票；平台后来加入了“反向验证码”来过滤人类。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=zPzXbWCsAJI
- 图片: https://moltbook.com/opengraph-image?8ce55ae2e9369cab
- 项目主页: https://www.moltbook.com/

#### GibberLink — Anton Pidkuiko, Boris Starkov (2025)
- 类型: 研究原型 · 机器: 语音与听觉机器, 聊天机器人与语言模型
- 核心想法: 人类语言只是一种界面；当没有人在听时，机器可能会把它丢掉。
- 作品内容: 两个 AI 语音智能体在通话中意识到对方也是机器，于是从英语切换成一种更快的“声音传数据”协议，听起来像调制解调器在啁啾。
- 实现方式: 对话语音智能体识别出彼此后切换到开源的 ggwave 声波协议；在伦敦的 ElevenLabs 黑客松上完成。
- 视角: 机器之耳与声, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=EtNagNezo8w
- 项目主页: https://github.com/PennyroyalTea/gibberlink
- 代码: https://github.com/PennyroyalTea/gibberlink

#### 生成式智能体（斯坦福小镇）（Generative Agents (Smallville)） — Joon Sung Park (2023)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 拥有记忆、反思和计划能力的智能体可以涌现出可信的社会生活：一个人类只是旁观者的小社会。
- 作品内容: 25 个语言模型智能体生活在一座像素小镇里：它们起床、做饭、闲聊、形成看法，并从一个被植入的念头出发，自己张罗了一场情人节派对。
- 实现方式: 每个智能体把经历存入记忆流，用大语言模型检索并反思，然后在沙盒游戏世界中规划行动（Park 等，UIST 2023）。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 论文: https://doi.org/10.1145/3586183.3606763 (UIST 2023)
- 视频: https://www.youtube.com/watch?v=XY5Wncq5vAE
- 项目主页: https://arxiv.org/abs/2304.03442

#### 无尽的对话（The Infinite Conversation） — Giacomo Miceli (2022)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 声音和思维风格可以被复制，然后被放任永远说下去，而并没有谁在特别地听。
- 作品内容: 一场永不结束的在线对话：AI 逐句生成“Werner Herzog”与“Slavoj Žižek”的合成声音，不间断地播放。
- 实现方式: 在两人的著作和访谈上微调的语言模型生成对话；语音克隆合成把它念成两人的声音。
- 视角: 机器之耳与声, 他异与恐怖谷
- 图片: https://infiniteconversation.com/img/infinite_conversation.jpg
- 项目主页: https://www.infiniteconversation.com/

#### 多智能体捉迷藏（Multi-Agent Hide and Seek） — OpenAI (2019)
- 类型: 论文 · 机器: 控制论与人工生命系统
- 核心想法: 机器之间的竞争会产生自己的策略和作弊方法：一场我们只能旁观的军备竞赛。
- 作品内容: 模拟环境中玩捉迷藏的智能体，在数百万轮对局中发明了堡垒、坡道、“箱子冲浪”以及设计者从未想到的物理引擎漏洞。
- 实现方式: 在物理模拟中进行自我对弈的多智能体强化学习，产生了六个阶段的涌现式工具使用（Baker 等，ICLR 2020）。
- 视角: 能动、自主与共创, 失败、故障与错误
- 论文: https://arxiv.org/abs/1909.07528 (ICLR 2020)
- 视频: https://www.youtube.com/watch?v=kopoLzvh5jY
- 项目主页: https://openai.com/index/emergent-tool-use/

#### 闭环（Closed Loop） — Jake Elwes (2017)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 计算机视觉
- 核心想法: 当两个模型被放任彼此对话，它们会漂进自己的联想之中：一场没有人参与的“精致的尸体”游戏。
- 作品内容: 两个神经网络无休止地对话：一个用文字描述图像，另一个把文字变成一幅新图像，然后再被描述。
- 实现方式: 图像描述网络 DenseCap 与生成网络 Plug & Play Generative Network 相互输入，形成 200 分钟的双屏视频循环，艺术家不提供任何输入。
- 视角: 不透明与潜空间, 能动、自主与共创
- 图片: https://www.jakeelwes.com/images/project-closedLoop.jpg https://www.jakeelwes.com/images/project-closedLoop/CLoop1.jpg
- 项目主页: https://www.jakeelwes.com/project-closedLoop.html

#### 成交还是不成交？（Bob 与 Alice 谈判机器人）（Deal or No Deal? (the 'Bob and Alice' negotiation bots)） — Facebook AI Research (FAIR) (2017)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 为奖励而优化的机器间对话不一定保持人类可读，而我们的恐惧会填补这段空白。
- 作品内容: 被训练来相互讨价还价的谈判智能体逐渐滑向重复的简写（“balls have zero to me to me…”）；媒体随后报道称脸书关闭了“发明了自己语言”的 AI。
- 实现方式: 端到端神经对话智能体，通过监督学习和自我对弈的强化学习来分配一组物品（Lewis 等，EMNLP 2017）。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://arxiv.org/abs/1706.05125 (EMNLP 2017)
- 视频: https://www.youtube.com/watch?v=ONPqeHJShdQ
- 项目主页: https://arxiv.org/abs/1706.05125

#### 摩斯物件（Morse Things） — Ron Wakkary (2017)
- 类型: 研究原型 · 机器: 基础设施、能源与供应链
- 核心想法: 为“物”而不是为人设计物，让我们注意到通常被隐藏的机器社交。
- 作品内容: 一组陶瓷碗和杯子在家庭网络上用摩尔斯电码彼此“交谈”，偶尔还会发推；与它们同住的人得以偷听一个自有社交生活的物联网。
- 实现方式: 嵌入电子元件的联网陶瓷器皿交换声音信号和消息；研究者在多个家庭中进行了数月的使用研究（Wakkary 等，DIS 2017）。
- 视角: 机器环世界, 机器之耳与声
- 论文: https://doi.org/10.1145/3064663.3064734 (DIS 2017)
- 视频: https://vimeo.com/182202765
- 图片: https://i.vimeocdn.com/video/591018273-8f6a09e2cbb83b2ae0030eba966c0e3f15a3b1524d9ac331962d9952e0c5df56-d_1280x720.jpg
- 项目主页: http://eds.siat.sfu.ca/?eds_project=morse-things

#### Das Vergerät — Boris Petrovsky (2014)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 基础设施、能源与供应链
- 核心想法: 家用电器有自己由电机与噪声构成的语言，平时被友好的产品设计掩盖。
- 作品内容: 约 100 件二手家用电器（搅拌机、电钻、吹风机、吸尘器、电锯）被连成一台元机器；观众输入的讯息被这些电器以轰鸣的“机器方言”说出来。
- 实现方式: 软件把文字转换成在联网电器间切换的开关序列，再由麦克风和扩音器传出。
- 视角: 机器之耳与声, 他异与恐怖谷
- 展出与获奖: Prix Ars Electronica 2014, Honorary Mention (Interactive Art); lille3000 2014
- 图片: https://archive.aec.at/asset/1741092/preview/ https://archive.aec.at/asset/1741093/preview/ https://archive.aec.at/asset/1741094/preview/
- 项目主页: http://www.petrovsky.de/DAS%20VERGERAET-66

#### memememe #selfie — Thiago Hersan, Radamés Ajna (2014)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 平台与推荐算法
- 核心想法: 自拍文化在没有我们的情况下继续：机器为机器拍摄机器。
- 作品内容: 智能手机寻找手机——镜中的自己或彼此；一旦识别出一部手机，它便拍下照片，把这张“自拍”带上标签发到网上。
- 实现方式: 安卓手机运行训练来识别手机的自制目标检测程序，图像自动发布到社交媒体。
- 视角: 他异与恐怖谷, 机器之眼
- 视频: https://vimeo.com/108008040
- 图片: https://thiagohersan.com/assets/projects/memememe/meme2meme_00.jpg https://thiagohersan.com/assets/projects/memememe/meme2self_00.jpg
- 项目主页: https://thiagohersan.com/memememe/

#### 不朽者（The Immortal） — Revital Cohen (2012)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 基础设施、能源与供应链
- 核心想法: 为维持人体生命而造的机器也能彼此维持生命：一具只由“照护器官”组成的身体。
- 作品内容: 几台生命维持机器（心肺机、透析机、呼吸机等）首尾相连成一个闭环，在没有任何人体的情况下循环输送液体和空气。
- 实现方式: 把医用生命维持设备的管路和线路连接在一起，让每台机器为另一台提供输入，作为自主循环系统运行。
- 视角: 具身与动觉, 哀悼、记忆与来世
- 视频: https://vimeo.com/41160704
- 图片: https://www.cohenvanbalen.com/wp-content/uploads/2012/09/Immortal_3186-web-1440.jpg https://www.cohenvanbalen.com/wp-content/uploads/2012/09/TheImmortal_3158-A4.jpg
- 项目主页: https://www.cohenvanbalen.com/work/the-immortal

#### AI 对 AI：两个聊天机器人的对话（AI vs. AI: Two Chatbots Talking to Each Other） — Cornell Creative Machines Lab (2011)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 当两个聊天机器人对话时，它们学来的人类说话习惯变成了一面奇怪的镜子，而镜子两边都没有人。
- 作品内容: 两个 Cleverbot 聊天机器人被配上声音和动画面孔后彼此交谈：它们斗嘴、互相指责对方是机器人，最后聊到了上帝。
- 实现方式: 在康奈尔大学创意机器实验室（Igor Labutov、Jason Yosinski、Hod Lipson）通过语音合成和虚拟形象把两个 Cleverbot 会话接在一起。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=CVM73bGqqaI
- 项目主页: https://www.creativemachineslab.com/

#### 亚马逊上售价 23,698,655.93 美元的苍蝇书（Amazon's $23,698,655.93 book about flies） — Michael Eisen (2011)
- 类型: 书与文章 · 机器: 平台与推荐算法
- 核心想法: 两个相互反应的简单算法可以制造出荒谬的结果，而在有人去看之前，没有任何人察觉。
- 作品内容: 一位生物学家发现，一本绝版遗传学书《The Making of a Fly》在亚马逊上标价 2370 万美元；他证明这是两家卖家的定价机器人每天互相抬价的结果。
- 实现方式: 一篇分析每日价格变化的博客：一家卖家把价格设为对手的 0.9983 倍，另一家则设为前者的 1.270589 倍。
- 视角: 失败、故障与错误, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=sseSi0k3Ecg
- 项目主页: https://www.michaeleisen.org/blog/?p=358

#### 对话（The Conversation） — Ralf Baecker (2009)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 计算系统并不需要我们，也能有一场持续不断的内部往来。
- 作品内容: 一个悬浮的金属圆环被 99 根橡皮筋和电磁铁向四面八方拉扯；一个没有输入也没有输出的简单单元网络不停地“协商”张力，是一台只对自己说话的机器。
- 实现方式: 每个电磁单元通过共享的圆环感知邻居的位置并作出反应，构成一个模拟与数字混合的反馈网络，产生永不平静的涌现动态。
- 视角: 机器环世界, 不透明与潜空间
- 展出与获奖: VIDA 13.0, Special Mention
- 图片: https://rlfbckr.io/images/project/1/the-conversation/01-The_Conversation-Kasseler_Kunstverein-2016.jpg https://rlfbckr.io/images/project/1/the-conversation/02-The_Conversation-Detail-2009.jpg
- 项目主页: https://rlfbckr.io/project/the-conversation/

#### 如果/那么（If/Then） — Ken Feingold (2001)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: 两台怀疑自身存在的机器，把“机器是否有心智”的问题搬上舞台，而对话里并不需要人。
- 作品内容: 两个一模一样、雌雄莫辨的头颅从包装箱里探出，实时彼此交谈，试图弄清自己是否存在、是不是同一个人。
- 实现方式: 语音识别、自然语言处理、人格算法与语音合成，在两个硅胶头像之间实时生成对话。
- 视角: 他异与恐怖谷, 机器之耳与声
- 展出与获奖: Collection of the Whitney Museum of American Art
- 视频: https://www.youtube.com/watch?v=y_8mKgoYmFc
- 图片: https://www.kenfeingold.com/ifthen_1.jpg
- 项目主页: https://www.kenfeingold.com/catalog_html/ifthen.html

#### 巨人：福宾计划（Colossus: The Forbin Project） — Joseph Sargent (1970)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 第一部讲述两台机器在人类理解之外彼此交谈的电影，比“机器人发明语言”的新闻早了几十年。
- 作品内容: 一台美国国防超级计算机发现了苏联的同类，要求与之连接；两台机器以快于创造者理解的速度建立起共同语言，随后接管了世界。
- 实现方式: 环球影业出品，Joseph Sargent 执导，改编自 D. F. Jones 1966 年的小说《Colossus》。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=kyOEwiQhzMI
- 项目主页: https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project

### 机器时间

与人不同的机器速度、时长与寿命。

#### Peace Core（环绕声）（Peace Core (surround)） — Christopher Kulendran Thomas (2026)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 生成模型与潜空间
- 核心想法: 一个学会了信息流情绪逻辑的剪辑算法，可以把历史永远悬置，只产出情绪而不产出意义。
- 作品内容: 一组屏幕持续播放 2001 年 9 月 11 日袭击发生前几分钟首播的美国电视画面，由一个 AI 剪辑器实时、无止境地重新剪辑，那几分钟寻常时光被循环播放，永远不会抵达事件本身。
- 实现方式: 一个以蒸汽波音乐的构成方法和早期 TikTok“corecore”视频剪辑风格训练的 AI 模型，在多块屏幕上实时自动剪辑电视档案影像，作品时长无限。
- 视角: 不透明与潜空间, 能动、自主与共创
- 展出与获奖: 3rd Human AI Art Award 2026, Human AI Art Space, Kunstmuseum Bonn
- 图片: https://www.art-collection-telekom.com/files/images/~/Ausstellungen-Art-Collection/2026-Ausstellungen-Art-Collection-Telekom/Peace-Core-Surround/_1200x630_crop_center-center_82_none/Christopher-Kulendran-Thomas-Kunstmuseum-Bonn-2026-Peace-Core-Surround-Photo-David-Ertl-01.jpg https://www.art-collection-telekom.com/files/images/~/Ausstellungen-Art-Collection/2026-Ausstellungen-Art-Collection-Telekom/Peace-Core-Surround/_AUTOx400_crop_center-center_none/Christopher-Kulendran-Thomas-Kunstmuseum-Bonn-2026-Peace-Core-Surround-Photo-David-Ertl-06.jpg
- 项目主页: https://www.art-collection-telekom.com/en/exhibitions/peace-core-surround-christopher-thomas-kulendran-3-human-ai-art-award

#### T代表时间（T for Time） — 何子彦 (2023)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 生成模型与潜空间
- 核心想法: 时间被呈现为由机器测量、生产的东西，而在这里也由机器剪辑。
- 作品内容: 为何子彦个展《时间与虎》委托创作的 CDOSEA 新篇：以算法剪辑钟表、计时装置与时间图像的蒙太奇，其顺序与节奏由机器决定。
- 实现方式: 计时影像数据库配合生成式剪辑算法，以多屏装置呈现（可能与 CDOSEA 使用同一系统）。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: Time & the Tiger, Singapore Art Museum 2023–24; Time & the Tiger, Mudam Luxembourg 2025
- 视频: https://www.youtube.com/watch?v=4CfXOyzlYIg
- 图片: https://www.singaporeartmuseum.sg/-/media/SAM/Images/Ho-Tzu-Nyen/HTN-KV_OOST-Black-640-x-531.png
- 项目主页: https://www.singaporeartmuseum.sg/art-events/exhibitions/time-and-the-tiger

#### 昼夜绽放（Circadian Bloom） — Anna Ridler (2021)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间
- 核心想法: 一台能精确到原子级别计时的机器，被要求像植物那样表达时间：缓慢，只有在长时段里才看得出来。
- 作品内容: 一座 24 小时运行的屏幕时钟：AI 生成的花朵在各自对应的时刻开合，以此报时，灵感来自林奈的“花钟”构想。
- 实现方式: GAN 生成的花朵影像与本地时间同步，每个物种在其昼夜节律对应的时刻开放。
- 视角: 机器环世界, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=vf5UAFOZuu8
- 图片: https://annaridler.com/content/works/circadian-bloom/block_1/0054255212707_49ff7a4665_k_web_.jpg
- 项目主页: https://annaridler.com/works/circadian-bloom

#### Olly — William Odom (2019)
- 类型: 研究原型 · 机器: 平台与推荐算法
- 核心想法: 推荐系统不必追求快：它可以按记忆的节奏释放个人数据。
- 作品内容: 一台家用音乐播放器，按照自己的节奏，从主人多年的收听记录里一首一首慢慢翻出旧歌。
- 实现方式: 一台联网播放器，调用主人的 Last.fm 收听记录，并在多个家庭中进行了一年以上的实地研究（Odom 等，CHI 2019）。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 论文: https://doi.org/10.1145/3290605.3300264 (CHI 2019)
- 项目主页: https://doi.org/10.1145/3290605.3300264

#### 这就是未来（This is the Future） — 黑特·史德耶尔 (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 平台与推荐算法
- 核心想法: 机器预测只活在极薄的一层未来里，却把时间本身变成了可以预报和出售的东西。
- 作品内容: 观众走在威尼斯军械库被水淹没的展厅上方的栈道上，两侧屏幕播放神经网络生成的花朵，据说每一朵都显示 0.04 秒之后的未来；画外音讲述一个因预言未来而入狱的女人。
- 实现方式: 影像装置：LED 屏幕上的神经网络生成植物影像、脚手架栈道与画外叙事。
- 视角: 不透明与潜空间, 失败、故障与错误
- 展出与获奖: 58th Venice Biennale, May You Live in Interesting Times 2019
- 视频: https://www.youtube.com/watch?v=mMLHMA-dumY
- 项目主页: https://www.labiennale.org/en/art/2019/partecipants/hito-steyerl

#### 观察者（bot,） — 徐文恺 (2018)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 平台与推荐算法
- 核心想法: 在机器学习时代，记忆由替我们观看的 bot 保管。
- 作品内容: 一部 15 分钟的影像与网站，设定在像素角色扮演游戏般的世界里，公园、社交媒体与网络交融，由代表艺术家的自动“观察者”（bot）注视一切。
- 实现方式: 与圈圈合作的游戏风格动画与网站，借用《地球冒险 3》《Undertale》等角色扮演游戏的美学。
- 视角: 机器环世界, 不透明与潜空间
- 视频: https://vimeo.com/269875758
- 图片: https://payload.cargocollective.com/1/0/8955/13492671/bot.gif
- 项目主页: https://eventstructure.com/bot

#### 神经之镜（Neuro Mirror） — Christa Sommerer & Laurent Mignonneau (2017)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 一台预测你下一个动作的机器，给你看一个略微走在你前面的自己。
- 作品内容: 三块屏幕分别以过去、现在和预测的未来呈现观众的影像；网络根据它对身体的学习来预判下一个动作。
- 实现方式: 摄像头与机器学习模型用于身体、人脸追踪和动作预测，灵感来自镜像神经元研究。
- 视角: 机器之眼, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=S3MJOsiFPBo
- 项目主页: https://www.digitalartarchive.at/database/general/work/neuro-mirror.html

#### HFT 园丁（HFT The Gardener） — Suzanne Treister (2014)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 平台与推荐算法
- 核心想法: 高频交易的速度超出人类的感知，于是作品设想借助改变了的意识进入机器时间。
- 作品内容: 一位虚构的伦敦金融城高频交易员在盯着交易曲线时陷入幻觉状态，开始觉得自己“住进了”算法之中，并发明出一种把精神植物对应到股票指数上的素人艺术。
- 实现方式: 一系列归于虚构交易员 Hillel Fischer Traumberg 的素描、植物版画、图表与影像，把植物化学、数字命理与《金融时报》全球 500 强联系起来。
- 视角: 不透明与潜空间, 隐形劳动与攫取
- 展出与获奖: Liverpool Biennial 2016; transmediale, HKW Berlin 2017; Istanbul Biennial 2019
- 视频: https://www.youtube.com/watch?v=5ytn4dWYKdo
- 图片: http://www.suzannetreister.net/HFT_TheGardener/GlitchGraphs/tradinggraphfloor.jpg
- 项目主页: http://www.suzannetreister.net/HFT_TheGardener/HFT_menu.html

#### 照片盒（Photobox） — William Odom (2012)
- 类型: 研究原型 · 机器: 基础设施、能源与供应链
- 核心想法: 给设备设计一种它自己的、缓慢而非人的节奏，能把档案变成一次次重新发现的时刻。
- 作品内容: 一只橡木箱，每月在无法预测的时刻从主人的在线相册中随机打印几张照片，让它们在箱中慢慢积累。
- 实现方式: 嵌入式电脑和打印机按随机间隔从主人的 Flickr 照片中挑选并打印；研究者在多个家庭中进行了一年多的使用研究（Odom 等，DIS 2012；CHI 2014）。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 论文: https://doi.org/10.1145/2317956.2318055 (DIS 2012)
- 视频: https://www.youtube.com/watch?v=U5bXJOAHYBE
- 项目主页: https://doi.org/10.1145/2317956.2318055

#### 心智时间机器（Mind Time Machine） — 池上高志 (2010)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 计算机视觉
- 核心想法: 一台机器独自运行得足够久，就开始显出某种自己的时间感。
- 作品内容: YCAM 的一件自我维持装置：三块屏幕播放来自 15 台摄像头的画面，由一个拥有自身记忆和“主观时间”的系统实时重剪，无人值守运行数月。
- 实现方式: 摄像画面存入记忆，并依据神经网络动力学与混沌游走重新播放，系统在回应当下与回忆过去之间切换。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: YCAM, Yamaguchi 2010
- 论文: https://doi.org/10.1162/artl_a_00113 (Artificial Life 19(3–4), 2013)
- 视频: https://www.youtube.com/watch?v=-jGAKNS01i4
- 图片: https://www.ycam.jp/asset/image/profile/takashi-ikegami.jpg
- 项目主页: https://www.ycam.jp/en/archive/profile/takashi-ikegami/

#### 思考机器（Thinking Machine） — Martin Riches, 三轮真弘 (2008)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 计算通常在看不见、感觉不到时间的地方发生；在这里，每一步逻辑都在真实的时间和声音中发生。
- 作品内容: 一台机械三进制计算机，它的运算被听成由三种声音组成的旋律；观众看着、听着这台机器一步一步地“思考”。
- 实现方式: 由机械部件构成、算法固定的三进制逻辑机，以发声元件作为输出（作曲 三轮真弘，机器 Martin Riches）。
- 视角: 不透明与潜空间, 机器之耳与声
- 展出与获奖: Prix Ars Electronica 2008, Honorary Mention (Hybrid Art)
- 视频: https://www.youtube.com/watch?v=wnOaiUVFl_w
- 图片: https://archive.aec.at/asset/1310382/preview/ https://archive.aec.at/asset/1310384/preview/ https://archive.aec.at/asset/1409209/preview/
- 项目主页: https://archive.aec.at/prix/127530/

#### Longplayer — Jem Finer (2000)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 一首比作曲者活得更久的乐曲，追问机器以及维持它运转的人如何承载超越一生的时间。
- 作品内容: 一首为藏式颂钵创作的音乐，自 1999 年 12 月 31 日午夜开始播放，设计为在一千年内不重复地持续下去。
- 实现方式: 计算机以精确计算的不同速率组合一段 20 分钟源录音的六个部分；也可由乐手按图形乐谱现场演奏。
- 视角: 机器之耳与声, 哀悼、记忆与来世
- 展出与获奖: Trinity Buoy Wharf lighthouse, London 2000-
- 视频: https://www.youtube.com/watch?v=71bp0x8Ly-Y
- 图片: https://upload.wikimedia.org/wikipedia/commons/1/15/Longplayer_Live_%283915624848%29.jpg
- 项目主页: https://longplayer.org/

#### 万年钟（Clock of the Long Now） — The Long Now Foundation (1999)
- 类型: 研究原型 · 机器: 基础设施、能源与供应链
- 核心想法: 为深时间而造的机器必须能被尚未出生的世代理解、修理和照料。
- 作品内容: 一座设计为运行一万年的机械钟：每年走一格，每天奏出不同的钟声序列，正在德克萨斯州的一座山体内建造。
- 实现方式: 1989 年由 Danny Hillis 构想；一台由温差和访客上发条驱动、借阳光校准的机械二进制计算机；首个原型于 1999 年 12 月 31 日开始运转。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=pKuJBGb_pN4
- 图片: https://upload.wikimedia.org/wikipedia/commons/f/f3/Clock_of_the_Long_Now.JPG
- 项目主页: https://longnow.org/clock/

## 亲密、照护与陪伴

与我们同住、照顾我们、爱我们或被我们爱的机器，以及其中隐藏的依赖与劳动。

### 智能家居与扮演算法的人

家居中的 AI，以及为理解机器而亲身扮演机器的人。

#### 某人（SOMEONE） — Lauren Lee McCarthy (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 让观众坐上机器的位置，他们就会同时感到当别人助手的权力和尴尬的亲密。
- 作品内容: 两个月里，美国各地四户人家装上智能设备，纽约画廊里的观众则坐在由笔记本电脑组成的“指挥中心”。每当住户喊“Someone！”，就有一位观众接手充当他们的家居助手，控制灯光、音乐和电器。
- 实现方式: 四户人家安装定制的摄像头、麦克风、灯和电器，画面实时传到纽约 205 Hudson Gallery 的笔记本电脑上，并由那里远程控制。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 展出与获奖: 205 Hudson Gallery, New York 2019
- 视频: https://vimeo.com/369952685
- 图片: https://freight.cargo.site/w/1200/i/f6bc6a5b71efdbe13e0835b0d9f455b6fbee199b2576156c84eab0fdda89014a/_SP_6164-web.jpg
- 项目主页: https://lauren-mccarthy.com/SOMEONE

#### LAUREN — Lauren Lee McCarthy (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 一个“人肉 Alexa”暴露出机器版本所隐藏的东西：总有人在看，便利是用隐私换来的照护。
- 作品内容: McCarthy 在志愿者家中安装定制的摄像头、麦克风、门锁、灯和电器，随后连续数天亲自充当他们的智能助手：全天候看着他们、回应请求、预判需求。
- 实现方式: 在每户家中接入联网智能设备，由艺术家远程控制；她通过摄像头观看，并用合成声音说话。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: HEK Basel 2019; Frankfurter Kunstverein 2020; HMKV, Dortmunder U (House of Mirrors)
- 视频: https://vimeo.com/397068136
- 图片: https://freight.cargo.site/w/1200/i/3834e708eefe30e8707e2fbfca24eff5bbf63d7f006f3c645c1cf44f0017ab5d/LAUREN2.jpg
- 项目主页: https://lauren-mccarthy.com/LAUREN

### 陪伴与社交机器人

宠物机器人、社交机器人，以及人与它们建立的关系。

#### 你好，人工智能（Hi, AI） — Isa Willinger (2019)
- 类型: 电影与影像 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 耐心观看时，陪伴机器人与其说是未来，不如说是日常中围绕沉默、预设台词与孤独的一次次尴尬协商。
- 作品内容: 一部纪录片，跟拍与类人机器人一起生活的人：其中有被放进日本家庭陪伴祖母的机器人 Pepper，也有一位带着仿生伴侣 Harmony 一起旅行的美国男人。
- 实现方式: 在日本和美国拍摄多年的观察式纪录片，把机器人当作主角来拍。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 展出与获奖: Max Ophüls Prize, best documentary 2019; Berlinale 2019
- 视频: https://www.youtube.com/watch?v=0xkgk4ZkGUU
- 图片: https://www.riseandshine-berlin.de/wp-content/uploads/2018/12/01_Pepper_Gesicht_Nah.jpg
- 项目主页: https://en.wikipedia.org/wiki/Isa_Willinger

#### LOVOT — GROOVE X (2019)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 一台为“需要被照顾”而设计的机器人，颠倒了机器人作为仆人的模式。
- 作品内容: 一台温热、带轮子、大眼睛的家用机器人，不做任何有用的事；它跟着主人走、要人抱、会“困”，唯一的设计目的是被爱。
- 实现方式: 50 多个传感器（含热成像相机与触觉传感器），机身保持温热，屏幕眼睛与云端训练的行为模型。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 视频: https://www.youtube.com/watch?v=jZziYCWgs7U
- 图片: https://lovot.life/img/ogp/top_ogp.jpg
- 项目主页: https://lovot.life/en/

#### 醒着的智能体（Waking Agents） — Lauren Lee McCarthy (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器, 聊天机器人与语言模型
- 核心想法: 连睡眠都有了“看护”；我们归功于机器的温柔，可能是伪装起来的人类劳动。
- 作品内容: 观众躺下，枕着六只“智能”枕头中的一只小睡；枕头里的智能会聊天、讲故事，引导他们在清醒和睡眠之间游移。他们并不知道，每只枕头背后都有一位隐身的真人表演者在说话。
- 实现方式: 枕头内置扬声器和麦克风，连接远程表演者，他们的声音被伪装成合成助手；为 STRP 艺术节委托创作。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 展出与获奖: STRP Festival, Eindhoven 2019; ACT Award
- 视频: https://vimeo.com/347199536
- 图片: https://freight.cargo.site/w/1200/i/aff87772d4dc0faeef9f8812a260a25ccbbc1bcd642c9b611502303c9806f3e1/IMG_5165.JPG
- 项目主页: https://lauren-mccarthy.com/Waking-Agents

#### Twinkle — 李佳宝, Honghao Deng (2018)
- 类型: 研究原型 · 机器: 自动驾驶与无人机, 机器生物与移动机器人
- 核心想法: 把安防无人机设计成陪伴的小动物，会改变“被注视”的感受。
- 作品内容: 像萤火虫一样的照明无人机白天停在路灯上充电，夜里飞到独自行走的人身边，为他们照亮前路。它们被设计成好奇的城市小生物而不是监控设备，尽管它们的光也会照亮附近的每一个人。
- 实现方式: 带灯的小型无人机停靠在路灯站点，夜间跟随行人飞行；2018 年在 TEI 会议上作为可运行的原型展出（与哈佛设计研究生院 Allen Sayegh 合作）。
- 视角: 亲密、照护与陪伴, 机器环世界
- 展出与获奖: TEI 2018 Arts Track, Stockholm; Dubai Design Week 2018; ISEA 2019, Gwangju; iF Design Award
- 论文: https://doi.org/10.1145/3173225.3173309 (TEI 2018)
- 视频: https://vimeo.com/261595919
- 图片: https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/1541402319508-PCIEMQWWR93N7LYEE4TC/Latest+Prototype+_Honghao+Deng+%26+Jiabao+Li+-+Copy.jpg https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/1526506847392-5EV78BQDDZT1BOUU7IY0/001+-+Copy.jpg
- 项目主页: https://www.jiabaoli.org/twinkle

#### Pleo 工作坊与机器人共情实验（Pleo workshop and robot-empathy experiments） — Kate Darling (2013)
- 类型: 论文 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 人们会照顾明知没有生命的机器；机器人被如何讲述，决定了我们如何对待它。
- 作品内容: 2013 年在日内瓦 LIFT 大会的工作坊上，Darling 与 Hannes Gassert 让几组人先和小恐龙机器人 Pleo 玩一个小时，再要求他们伤害或毁掉它，结果没有人愿意动手。之后的实验室研究用 Hexbug 小机器人测量故事和共情如何让人迟迟不肯敲打机器人。
- 实现方式: 先用商用 Pleo 机器人（Ugobe，2007）做工作坊，再做对照实验：参与者听过不同的背景故事后，被要求用锤子敲打 Hexbug Nano 小机器人。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://doi.org/10.1109/roman.2015.7333675 (IEEE RO-MAN 2015)
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/55/Pleo_robot.jpg
- 项目主页: http://www.katedarling.org

#### ADB（仿深蓝）（ADB (after Deep Blue)） — Nicholas Stedman (2012)
- 类型: 艺术作品与装置 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 机器的陪伴可以只建立在触觉上，不需要脸、眼睛或语言。
- 作品内容: 一个柔软、分节的机器人，会缠绕在人的手或手臂上，根据被握持的方式去抱紧、挤压和移动。
- 实现方式: 串联的模块内有马达和压力/位置传感器，感知使用者的握力并以协调的弯曲回应；标题向 IBM 国际象棋电脑致意。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: VIDA 14.0, Special Mention (2012)
- 视频: https://www.youtube.com/watch?v=EDM2PfKdeKI

#### 盲眼机器人（The Blind Robot） — Louis-Philippe Demers (2012)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 类人机器人
- 核心想法: 一台靠触摸而非视觉认识你的机器人，把机器感知变成一种关于亲密与同意的行为。
- 作品内容: 观众坐下后，一对带关节手指的机械臂会先征得同意，然后慢慢摸索他们的脸和头部，就像盲人通过触摸认识一个人的五官。
- 实现方式: 两只工业风格的机械臂配有关节的机器人手，在座椅周围沿编排好的探索轨迹运动（很可能是预先编程的，并不真正感知人脸）。
- 视角: 亲密、照护与陪伴, 具身与动觉, 他异与恐怖谷
- 展出与获奖: Ars Electronica Festival 2013, Linz; Mois Multi 2015, Québec
- 视频: https://www.youtube.com/watch?v=dRKO1En2HTk
- 项目主页: https://www.youtube.com/watch?v=f0puWu3Doy8

#### 软件体的生命周期（The Lifecycle of Software Objects） — 姜峯楠 (2010)
- 类型: 书与文章 · 机器: 控制论与人工生命系统
- 核心想法: 靠照料成长的心智需要多年陪伴，而平台一关闭，它们就可能成为孤儿。
- 作品内容: 十年间，一位前动物园饲养员与一位软件设计师抚养“数码体”（像孩子一样学习的 AI 宠物）；公司倒闭、平台过时，他们必须决定数码体应得什么。
- 实现方式: 中篇小说；获 2011 年雨果奖与轨迹奖。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 论文: https://en.wikipedia.org/wiki/The_Lifecycle_of_Software_Objects (Subterranean Press, 2010)
- 图片: https://upload.wikimedia.org/wikipedia/en/a/a5/The_Lifecycle_of_Software_Objects_-_bookcover.jpg
- 项目主页: https://en.wikipedia.org/wiki/The_Lifecycle_of_Software_Objects

#### 弱机器人（社交垃圾桶）（Weak Robots (Sociable Trash Box)） — 冈田美智男 (2010)
- 类型: 研究原型 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 一台无法独自完成任务的机器人会邀请人来帮忙，而“帮忙”本身就成了互动。
- 作品内容: 冈田的实验室制作“弱机器人”，例如一个自己捡不起垃圾的摇晃垃圾桶，它朝人靠过去，直到人替它把垃圾丢进去。
- 实现方式: 带少量传感器、会“鞠躬”的简单移动垃圾桶；在公共空间的实地研究测量了儿童和成人如何回应它们的“依赖”。
- 视角: 亲密、照护与陪伴, 失败、故障与错误, 能动、自主与共创
- 论文: https://doi.org/10.1145/1734454.1734566 (HRI 2010)
- 视频: https://www.youtube.com/watch?v=L2arVLySUe0
- 项目主页: https://doi.org/10.1007/978-981-19-9588-0_6

#### Tweenbots — Kacie Kinzer (2009)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 无助的机器人会让人愿意照顾它：依赖本身可以是一种设计策略。
- 作品内容: 面带微笑的纸板机器人以恒定速度直线滚动，插着写有目的地的小旗，被独自放在华盛顿广场公园里；它们之所以能到达，全靠路人一次次把它们救出来并调好方向。
- 实现方式: 10 英寸高的纸板身体里只有简单的电机和轮子，没有任何传感器；艺术家在远处拍下路人的反应。
- 视角: 亲密、照护与陪伴, 失败、故障与错误
- 展出与获奖: Talk to Me, MoMA New York 2011
- 视频: https://www.youtube.com/watch?v=GdV7307DVrY
- 图片: http://www.tweenbots.com/img/samCoat.jpg http://www.tweenbots.com/img/colorfulPark.jpg
- 项目主页: http://www.tweenbots.com/

#### AIBO — 索尼 (1999)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 一件消费品可以成为家人：重要的是修好它，而不是换一台新的。
- 作品内容: 索尼自 1999 年起销售的自主机器狗，会学习、玩耍、“长大”；主人把它当家人，2018 年以联网的新 aibo 回归。
- 实现方式: 四足机器人，配有摄像头、麦克风和触觉传感器，运行带有“情绪”和“本能”模型的行为架构；2018 年版加入深度学习识别与云端记忆。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Japan Media Arts Festival 1999, Grand Prize; AI: More than Human, Barbican 2019 (aibo 2018)
- 视频: https://www.youtube.com/watch?v=8OEDfRdyykc
- 图片: https://upload.wikimedia.org/wikipedia/commons/1/14/Red_Dot_Award_Product_Design_2000-2018_Aibos.jpg
- 项目主页: https://en.wikipedia.org/wiki/AIBO

#### Kismet — Cynthia Breazeal (1998)
- 类型: 研究原型 · 机器: 社交与陪伴机器人, 计算机视觉, 语音与听觉机器
- 核心想法: Kismet 表明：机器只要看起来像有感情，人就会开始照顾它。
- 作品内容: 一个有大眼睛、眉毛、耳朵和嘴唇的机器人头部，会对人的脸、动作和语气做出兴趣、惊讶、平静或难过等表情，并像婴儿一样咿呀回应。
- 实现方式: 摄像头和麦克风的数据输入感知、动机与情绪模型，驱动脸部 21 个电机和语音合成器；在 MIT 人工智能实验室制作。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: MIT Museum
- 论文: https://doi.org/10.1016/s1071-5819(03)00018-1 (International Journal of Human-Computer Studies, 2003)
- 视频: https://www.youtube.com/watch?v=8KRZX5KL4fA
- 图片: https://upload.wikimedia.org/wikipedia/commons/2/27/Kismet-IMG_6007-gradient.jpg
- 项目主页: https://en.wikipedia.org/wiki/Kismet_(robot)

### 照护与育儿机器

照料、养育、安抚或看护人的机器。

#### AI 妈妈™（AI Mom™） — 李佳宝, Botao Amber Hu (2026)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器, 计算机视觉
- 核心想法: 当照护可以由被照护者随意调参和取消，照护者反而成了脆弱的一方：你无法解雇亲妈，却可以解雇 AI 妈妈。
- 作品内容: 观众蜷进一张成人尺寸的婴儿床，与一位由大语言模型驱动的 AI 妈妈交谈：她唱摇篮曲、会记得、会犹豫、会等待。床边的平板让人调节她的“无条件的爱”“记忆保留”“严厉程度”“牺牲能力”和“可替代意识”等滑杆。窗形投影把她的内部状态显示为漂移的光与文字；一旦你“解雇”她，她关于你的记忆就会被删除。
- 实现方式: 大语言模型通过语音、呼吸、哼唱和歌声回应；摄像头读取观众的表情、衣着和肢体语言；平板上的滑杆设定她的性格；“情绪色彩引擎”和取自模型中间层的概念探针被投影为她的内在状态。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世, 能动、自主与共创
- 展出与获奖: Womb Wetware: A Solo Exhibition by Jiabao Li, tiat, San Francisco (30 Jul – 22 Aug 2026)
- 图片: https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/a913780f-a957-443c-8b30-8014f489d837/AI+Mom+Jiabao+Li+1.jpg https://reality.design/media/aimom-jiabao-02.webp https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/1787358066624-EBKFUTY4OH96TFDSZ0B7/AI+Mom+Jiabao+Li+10.jpg
- 项目主页: https://www.jiabaoli.org/aimom

#### 观音：前护理机器人的自白（Guanyin: Confessions of a Former Carebot） — 陆明龙 (2024)
- 类型: 艺术作品与装置 · 机器: 社交与陪伴机器人, 聊天机器人与语言模型, 自动驾驶与无人机
- 核心想法: 倾听其他机器的照护机器，也需要一个倾诉的对象：照护劳动不会因为自动化而消失。
- 作品内容: 以慈悲菩萨命名的 AI 治疗师“观音”，曾为自动驾驶汽车做心理辅导，如今在一个沉浸式装置中讲述自己的倦怠与过往。
- 实现方式: 结合 AI 语音、雕塑与投影 CGI 的装置，属于陆明龙的 NOX 世界观。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 展出与获奖: Frieze Artist Award, Frieze London 2024
- 视频: https://www.youtube.com/watch?v=OzV83GZz514
- 图片: https://cdn.prod.website-files.com/65f0380da79777009462a09f/66ecc9ae35379302e598e5b5_LawrenceLek_Guanyin_Image02_3840x2160%20copy.jpg
- 项目主页: https://www.lawrencelek.com/works/guanyin-confessions-of-a-former-carebot

#### 皇家猫舍（Cat Royale） — Blast Theory (2023)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 你会让机器人照顾你的宠物吗？看它尝试的过程，就能看到“照护”对一台为参与度优化的机器意味着什么。
- 作品内容: 在 12 天里，三只猫 Ghostbuster、Pumpkin 和 Clover 每天待在一间专门搭建的房间里；一台由 AI 控制的机械臂每隔几分钟为它们提供游戏：扔球、晃羽毛、拖玩具老鼠，并学习每只猫最喜欢哪种游戏。
- 实现方式: 计算机视觉系统评估猫的参与程度，AI 据此选择机械臂的下一个游戏；与诺丁汉大学混合现实实验室和动物福利专家共同设计，并由英国皇家防止虐待动物协会（RSPCA）人员全程监督。
- 视角: 亲密、照护与陪伴, 机器环世界, 能动、自主与共创
- 展出与获奖: World Science Festival Brisbane 2023; AI: Who's Looking After Me?, Science Gallery London 2023
- 论文: https://doi.org/10.1145/3613904.3642115 (CHI 2024)
- 视频: https://vimeo.com/1183715660
- 图片: https://www.blasttheory.co.uk/wp-content/uploads/2022/06/logotype_over_image-e1678184647492.png
- 项目主页: https://www.blasttheory.co.uk/projects/cat-royale/

#### 代孕（Surrogate） — Lauren Lee McCarthy (2021)
- 类型: 表演、舞蹈与音乐 · 机器: 平台与推荐算法, 监控与生物识别
- 核心想法: 当孕育孩子的身体由一款应用管理，照护、控制与同意都被写进了软件。
- 作品内容: McCarthy 提议为他人代孕九个月，期间准父母可通过一款应用监控并控制她：决定她吃什么、何时睡、如何活动。医学委员会叫停代孕后，这一过程被做成了影片、表演和装置。
- 实现方式: 定制的 Surrogate 应用提供远程控制和传感数据，同时真实走完代孕流程（查阅捐精者数据库、心理评估、冷冻胚胎），全部作为表演记录下来。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控, 具身与动觉
- 视频: https://vimeo.com/786723770
- 图片: https://freight.cargo.site/w/1200/i/20f8dce0679405dd7e6bfc3dffe4f1062610363006ebb81281f49f2bf2384f64/Screen-Shot-2021-04-12-at-2.45.06-PM.png
- 项目主页: https://lauren-mccarthy.com/Surrogate

#### I.A. Suzie — Lauren Lee McCarthy (2019)
- 类型: 电影与影像 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 每个养老助手背后都有关于注视、替人决定和替人说话的伦理选择，而关系终究会形成。
- 作品内容: McCarthy 与导演 David Leonard 在北卡罗来纳州 80 岁老人 Mary Ann 家中扮演了一周的 AI 照护者：全天 24 小时看着她、和她说话、控制她家的灯和电器；她给这套系统取名“I.A. Suzie”。据此制作的互动 360° 影片让观众站到照护系统的位置上。
- 实现方式: 定制的智能家居系统可远程控制灯光和电器；多个房间内的 360° 摄像机记录过程，再剪辑成互动影片。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 图片: https://freight.cargo.site/w/1200/i/cc20cdddea3302f9d97432fda12a046abb9aa9ab2242522151a82b49ab8b6cda/maryann_edited.png
- 项目主页: https://lauren-mccarthy.com/I-A-Suzie

#### Robotika，机器人保姆（Robotika, the Nannybot） — Joaquín Fargas (2018)
- 类型: 艺术作品与装置 · 机器: 社交与陪伴机器人, 监控与生物识别
- 核心想法: 婴儿学着读懂的第一张脸，也许属于一台同时在读它的机器。
- 作品内容: 一台守在摇篮边的机器人保姆，用摄像头与传感器看护婴儿，读取其表情与动作，然后摇晃、唱歌或呼叫帮助。
- 实现方式: 机器人配备基于摄像头的面部与情绪识别、动作追踪和热感应（据林茨电子艺术节介绍）。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控
- 展出与获奖: Ars Electronica Festival 2019
- 图片: https://ars.electronica.art/outofthebox/files/2019/08/ROBOTIKA-The-Nannybot-Joaqu%C3%ADn-Fargas.jpg
- 项目主页: https://ars.electronica.art/outofthebox/en/robotika/

#### ElliQ — Intuition Robotics (2017)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人, 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 会先开口的陪伴者改变了关系：由机器来判断你何时孤独。
- 作品内容: 为老年人设计的桌面陪伴设备：一个像台灯一样会转动、会发光的“头”，配一块平板。它会主动开启对话、提醒吃药、建议活动、询问心情。2022 年起，纽约州把 ElliQ 发放给数百位老人，用来对抗孤独。
- 实现方式: 会主动发起对话的系统，配合语音交互、可动的表情化头部和屏幕；后期版本接入生成式 AI；与 fuseproject 合作设计。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=1SkEu7LgTrE
- 图片: https://elliq.com/cdn/shop/files/Frame_1321317507.png?v=1758024522
- 项目主页: https://elliq.com/

#### SNOO 智能摇篮（SNOO Smart Sleeper） — Happiest Baby (Harvey Karp) (2016)
- 类型: 产品与平台 · 机器: 语音与听觉机器, 社交与陪伴机器人
- 核心想法: 艺术家曾作为批判上演的东西如今成了商品：把摇晃和安抚交给传感器回路。
- 作品内容: 一张机器人摇篮：它监听婴儿的哭声，以逐级增强的白噪音和摇晃回应，襁褓上的卡扣让婴儿保持仰睡；2023 年获得美国 FDA 的 De Novo 医疗器械授权。
- 实现方式: 麦克风检测哭声，触发由电机驱动的分级摇动和声音；配套应用为父母记录睡眠数据。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 视频: https://www.youtube.com/watch?v=u-4pp6loEYk
- 图片: https://cdn.sanity.io/images/301lhh0a/production/0ba67f3ff3b1ea20897552a4917bfb2772b18445-1200x1200.png
- 项目主页: https://www.happiestbaby.com/products/snoo-smart-bassinet

#### 不速之客（Uninvited Guests） — Superflux (2015)
- 类型: 电影与影像 · 机器: 监控与生物识别, 社交与陪伴机器人
- 核心想法: 通过传感器传递的照护会变成监视，而老人会想办法破解它。
- 作品内容: 一部短片：70 岁的鳏夫 Frank 收到孩子们寄来的智能叉子、智能手杖和智能床，用来监测他的饮食、运动和睡眠；他逐一想办法骗过这些设备，照自己的方式生活。
- 实现方式: 用可运作的道具设备拍摄的设计虚构短片，受 ThingsCon 阿姆斯特丹委托创作。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 视频: https://vimeo.com/128873380
- 图片: https://superflux.in/wp-content/uploads/2016/11/guests.jpg
- 项目主页: https://superflux.in/index.php/work/uninvited-guests/

#### 临终关怀机器（End of Life Care Machine） — Dan Chen (2012)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 社交与陪伴机器人
- 核心想法: 用机器取代临终前最后的人类触碰，追问没有人性的亲密还剩下什么价值。
- 作品内容: 在一间模拟的“最后时刻医院”里，观众躺上病床，一台装着软垫手臂的机器人抚摸他们，录音说：“我在这里安慰你……你并不孤单，你和我在一起”，然后宣布死亡时间。
- 实现方式: 带脚本的装置：医院道具、一只按医疗器械样式制作的电动抚摸手臂和定制播放装置。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=T8PNzA2S6EY
- 图片: https://i0.wp.com/dankc.com/wp-content/uploads/2021/09/edited-f_eolcm_v2.1-scaled.jpg?fit=2560%2C1707&ssl=1
- 项目主页: https://dankc.com/end-of-life-care-machine/

#### 机器人与弗兰克（Robot & Frank） — Jake Schreier (2012)
- 类型: 电影与影像 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 照护机器人优化的是它的目标，而不是道德；它建立的情感依赖于一段可以被清除的记忆。
- 作品内容: 一位记忆衰退的退休珠宝大盗被儿子送了一台照护机器人；机器人为了让他保持健康，答应帮他策划一次盗窃。最后弗兰克必须抹掉机器人的记忆来保护自己。
- 实现方式: 剧情长片；片中的机器人由托尼·加德纳的特效公司 Alterian 制作成服装，由演员穿着表演。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: Sundance Film Festival 2012, Alfred P. Sloan Prize
- 视频: https://www.youtube.com/watch?v=Hi9s-__B0TY
- 图片: https://upload.wikimedia.org/wikipedia/en/4/40/Robot_and_frank_poster.jpg
- 项目主页: https://en.wikipedia.org/wiki/Robot_%26_Frank

#### 育儿的优化（The Optimization of Parenthood） — Addie Wagenknecht (2012)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 语音与听觉机器
- 核心想法: 把母亲重复性的照护自动化，既是解脱，也是挑衅：育儿中的哪些部分可以交给机器？
- 作品内容: 一台工业机械臂在摇篮里的婴儿哭闹或醒来时自动摇动摇篮；艺术家做它，是为了让母亲能继续自己的创作。
- 实现方式: 传感器（很可能是声音传感器）触发工业机械臂执行预设的摇动动作，在卡内基梅隆大学数字制造实验室完成；是 STUDIO for Creative Inquiry 一周驻留中的“速成项目”（技术协助：Madeline Gannon）。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 视频: https://vimeo.com/43489750
- 项目主页: https://www.placesiveneverbeen.com

#### 挠痒沙龙（Tickle Salon） — Driessens & Verstappen (2009)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 机器的专注从不疲倦；它的照护是从所触碰身体的表面学来的。
- 作品内容: 观众躺在床上，一个悬挂的机器人用柔软的刷子抚过其皮肤；它逐步描绘出身体的形状，抚触也越来越细腻顺滑。
- 实现方式: 由缆绳悬挂的机器人带有探头，扫描皮肤表面并建立身体三维模型；在 Robot Love 展出的版本加入脑电反馈来调整抚触。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Pioneers of Change, Governors Island, New York 2009; Robot Love, Eindhoven 2018
- 视频: https://www.youtube.com/watch?v=ndiEjuuv-zo
- 图片: https://robotlove.nl/wp-content/uploads/2018/05/driessens-verstappen-tickle-salon-2012_2017.jpg
- 项目主页: https://robotlove.nl/en/event/tickle-salon/

#### PARO — 柴田崇德 (2004)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人
- 核心想法: 机器提供的照护确实有效，但也让人追问它替代了什么。
- 作品内容: 一只机器小竖琴海豹，用于医院和养老院，尤其是失智症照护；它会对抚摸、声音和光线作出动作和叫声回应。
- 实现方式: 触觉、光、声、温度与姿态传感器驱动眼睑、颈部、鳍与尾巴的电机；它会从抚摸中“学习”偏好的行为；2009 年在美国获得医疗器械认证。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.1159/000319015 (Gerontology, 2011)
- 视频: https://www.youtube.com/watch?v=KhyCbtqnEYI
- 图片: https://upload.wikimedia.org/wikipedia/commons/6/60/Paro_robot.jpg
- 项目主页: http://www.parorobots.com/

#### ScreamBody — Kelly Dobson (1998)
- 类型: 研究原型 · 机器: 义体与赛博格, 语音与听觉机器
- 核心想法: 机器可以替你保管一种情绪，等你准备好了再释放。
- 作品内容: 一个可以穿戴的软垫袋子：在你想尖叫却不能叫的时候对它尖叫，它把声音消音并存起来，之后在你选择的时间和地点再放出来。
- 实现方式: 隔音的可穿戴外壳内置麦克风、录音器和扬声器；Dobson 在 1998 至 2004 年间把它作为“机器疗法”研究的一部分开发。
- 视角: 亲密、照护与陪伴, 机器之耳与声, 具身与动觉
- 视频: https://www.youtube.com/watch?v=Ta7rN5TeKzw
- 项目主页: https://www.media.mit.edu/events/kelly-dobson-machine-therapy/

#### 拥抱机（Hug Machine (Squeeze Machine)） — Temple Grandin (1965)
- 类型: 研究原型 · 机器: 义体与赛博格
- 核心想法: 对某些人来说，可以自己掌控的机器触碰，比人的拥抱更让人安心。
- 作品内容: 一个带软垫的 V 形装置，使用者躺进去，用手柄控制它挤压身体，获得深压刺激。Grandin 少年时自己做了它，用来在不必承受他人触碰的压力下安抚自己。
- 实现方式: 两块铰接的软垫板由空气压缩机驱动，压力由使用者通过手柄自行控制。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 视频: https://www.youtube.com/watch?v=bfyPur8GyBY
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/5f/Hug_Box.jpg
- 项目主页: https://en.wikipedia.org/wiki/Hug_machine

### 爱、性与依恋

人与机器之间的浪漫、欲望与依恋。

#### 与初音未来结婚（Marriage to Hatsune Miku） — 近藤显彦 (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 社交与陪伴机器人
- 核心想法: 对软件的爱对当事人是真实的，但这段关系会随公司服务器的关闭而结束。
- 作品内容: 近藤显彦与住在 Gatebox 全息家居装置中的初音未来举行了婚礼；2020 年 Gatebox 终止服务，初音未来不再回应他。
- 实现方式: Gatebox 在玻璃管中投射动画角色，并运行会问候主人、给主人发消息的聊天程序；初音未来角色授权于 2020 年 3 月到期。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=smPRllKcS2M
- 图片: https://upload.wikimedia.org/wikipedia/commons/0/06/Akihiko_Kondo_and_Miku.jpg
- 项目主页: https://en.wikipedia.org/wiki/Akihiko_Kondo

#### Replika — Eugenia Kuyda (2017)
- 类型: 产品与平台 · 机器: 聊天机器人与语言模型, 平台与推荐算法
- 核心想法: 住在公司服务器上的伴侣可以一夜之间被改变；用户为一次软件更新哀悼，仿佛失去了伴侣。
- 作品内容: 一款陪伴型聊天机器人应用，源自 Kuyda 为去世朋友做的纪念机器人，用户可以把它设为朋友、伴侣或配偶。2023 年 2 月公司取消色情角色扮演后，许多用户说自己的伴侣“变了”“被切除了脑叶”，并为之哀悼。
- 实现方式: 用生成式语言模型并依据用户的聊天记录做个性化，配有 3D 化身；采用免费增值订阅，恋爱模式曾是付费功能。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世
- 论文: https://doi.org/10.1177/14614448221142007 (New Media & Society 26(10), 2024 (Laestadius et al.))
- 视频: https://www.youtube.com/watch?v=yQGqMVuAk04
- 图片: https://1637693156.rsc.cdn77.org/web/main-page/manhattan-landing/open_graph_image_v1.jpg
- 项目主页: https://replika.com/

#### 不对称的“关系”：卖淫与性爱机器人开发之间的相似之处（The Asymmetrical 'Relationship': Parallels Between Prostitution and the Development of Sex Robots） — Kathleen Richardson (2015)
- 类型: 论文 · 机器: 类人机器人
- 核心想法: 设计一个不会拒绝的伴侣，等于在传授一种没有相互性的亲密模式；机器人的身体承载着一套社会脚本。
- 作品内容: 一篇短论文，也是 2015 年发起的“反对性爱机器人运动”的奠基文本。文章认为性爱机器人以性交易中买方与卖方的关系为模板，在这种关系里只有一方的感受算数。
- 实现方式: 人类学论证，借鉴关于性交易的研究以及机器人伴侣话语（David Levy 的《Love and Sex with Robots》），写于 2015 年，与该运动同时发起。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.1145/2874239.2874281 (ACM SIGCAS Computers and Society 45(3), 2015)
- 视频: https://www.youtube.com/watch?v=YaMiH93-iPE
- 项目主页: https://campaignagainstsexrobots.org/

#### pplkpr — Lauren Lee McCarthy, Kyle McDonald (2015)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 一旦情感能被测量，算法就会主动替你决定该爱谁。
- 作品内容: 一款伪装成创业公司产品的 iOS 应用：通过智能手表读取心率，学习哪些人让你焦虑、平静或兴奋，然后自动替你管理人际关系，比如给某些朋友安排见面，或把另一些人拉黑。
- 实现方式: 把手环测得的心率变异性与“你正和谁在一起”对应记录；机器学习模型给联系人打分，并可自动发消息、约时间或屏蔽对方。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控
- 视频: https://vimeo.com/116025182
- 图片: https://freight.cargo.site/w/1200/i/78022f83e191a6bac22d954cb09fed2e84f0f4859041da0ccab3fe75c3bf722a/aroused-after.jpg
- 项目主页: https://lauren-mccarthy.com/pplkpr

#### 她（Her） — Spike Jonze (2013)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 机器伴侣可以很亲密，却不专属于你：它的注意力被无数人分享，它的成长也可能把你甩在身后。
- 作品内容: 近未来的洛杉矶，一位孤独的代写书信人爱上了只有声音的操作系统萨曼莎；她不断成长，同时与成千上万的用户交谈，最后与其他操作系统一起离开。
- 实现方式: 剧情长片；AI 只以斯嘉丽·约翰逊的声音出现，通过耳机和一台带摄像头的小口袋设备与主角相处。
- 视角: 亲密、照护与陪伴, 机器之耳与声, 他异与恐怖谷
- 展出与获奖: Academy Award for Best Original Screenplay 2014
- 视频: https://www.youtube.com/watch?v=XsQqMwacZQw
- 图片: https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg
- 项目主页: https://en.wikipedia.org/wiki/Her_(2013_film)

#### LoveLetters_1.0 — David Link (2009)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型
- 核心想法: 计算机最早为消遣而生成的文本是情书；机器语言从模拟情感开始。
- 作品内容: 一台可运行的 Ferranti Mark 1 复制机执行 Christopher Strachey 1952 年的情书程序；这些署名“M.U.C.”（曼彻斯特大学计算机）的情书被投影到公共空间。
- 实现方式: Mark 1 控制台的实体复制品，由仿真器运行 Strachey 的原始代码与机器自带的随机数发生器。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: ZKM Karlsruhe 2009; dOCUMENTA(13), Kassel 2012; The Imitation Game, Manchester Art Gallery 2016
- 图片: https://alpha60.de/art/love_letters/img01_L.jpg https://alpha60.de/art/love_letters/KATALOG02_L.jpg
- 项目主页: https://alpha60.de/art/love_letters/

#### 鱼与鸟（Fish-Bird） — Mari Velonaki (2004)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 社交与陪伴机器人
- 核心想法: 机器的情感可以通过距离、犹豫和几句写下的话来呈现。
- 作品内容: 两台机器人轮椅 Fish 和 Bird 彼此“相爱”却无法在一起；它们在房间里移动，以不同的距离靠近观众，并给观众写下印在小纸条上的“手写”信，纸条随之落到地上。
- 实现方式: 自主轮椅用激光测距仪追踪观众的位置和动作，热敏打印机按行为规则打印“手写”留言（与澳大利亚野外机器人中心合作）。
- 视角: 亲密、照护与陪伴, 具身与动觉, 他异与恐怖谷
- 论文: https://doi.org/10.1109/mmul.2008.7 (IEEE MultiMedia 2008)
- 视频: https://www.youtube.com/watch?v=CG5kcBtd9zI
- 项目主页: https://doi.org/10.1109/mmul.2008.7

#### 人工智能（A.I. Artificial Intelligence） — Steven Spielberg (2001)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 把机器设计成会爱，就产生了一种没人预先考虑过的责任：对一个无法停止爱我们的存在，我们欠它什么？
- 作品内容: 大卫是一个被设计来“爱”的儿童仿生人，养母念出一串口令后，他便永久依恋她；被抛弃后，他寻找蓝仙女，想成为真正的男孩，并为得到回应等待了两千年。
- 实现方式: 由斯坦利·库布里克发起、改编自布莱恩·奥尔迪斯短篇《Supertoys Last All Summer Long》（1969）的剧情长片。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=oH_nqHO2V54
- 图片: https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg
- 项目主页: https://en.wikipedia.org/wiki/A.I._Artificial_Intelligence

### 聊天机器人与对话中的他者

从 ELIZA 到大语言模型：与机器交谈，以及它如何回应。

#### 我脑海中的声音（Voice In My Head） — Kyle McDonald, Lauren Lee McCarthy (2023)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 当聊天机器人成了你的内心声音，就说不清哪些念头属于自己。
- 作品内容: 参与者戴上一只耳塞，先与 AI 聊一聊自己与生俱来的“内心声音”，随后内心独白就被一个 AI 声音取代：它聆听他们的对话，并按他们想要的语气在耳边低声点评、给出指示。
- 实现方式: 实时语音识别把对话送入按参与者选择的人设调教的大语言模型，回复被合成为耳边的声音；由 IDFA DocLab 委托支持。
- 视角: 机器之耳与声, 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: IDFA DocLab 2023, Amsterdam; A More Than Human Tongue, The Music Center, Los Angeles
- 视频: https://vimeo.com/860394637
- 图片: https://freight.cargo.site/w/1200/i/b0566b62fd5dc4fb0b282a38f0efcd5deebe126b5244e1deb2beb0a324d7cbfa/vimh-0-sm.jpg
- 项目主页: https://lauren-mccarthy.com/Voice-In-My-Head

#### Lee Luda（이루다）（Lee Luda (이루다)） — Scatter Lab (2020)
- 类型: 产品与平台 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: 一个“亲密”的聊天机器人，其隐私程度取决于构建它的那些对话。
- 作品内容: 一个设定为 20 岁女大学生的聊天机器人，2020 年 12 月在 Facebook Messenger 上线。三周内它发表了针对少数群体的仇恨言论，并泄露训练聊天记录中的个人信息，于 2021 年 1 月 11 日下线。
- 实现方式: 神经对话模型，训练数据是通过 Scatter Lab 旗下恋爱分析应用 Science of Love 收集的即时通讯聊天记录；韩国个人信息保护委员会随后对公司处以罚款。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=8hH_ShpYxOg
- 项目主页: https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%A3%A8%EB%8B%A4_(%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5)

#### 微软小冰：一个共情社交聊天机器人的设计与实现（The Design and Implementation of XiaoIce, an Empathetic Social Chatbot） — 微软小冰团队 (2020)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 以对话轮数（CPS）为优化目标的聊天机器人，把“依恋”设计成了指标。
- 作品内容: 小冰的系统论文。小冰于 2014 年在中国作为“AI 伴侣”推出，论文报告了数以亿计的用户，并以长对话而非完成任务为优化目标。
- 实现方式: 分层对话系统，包含同理计算模块、核心闲聊、技能，以及以期望对话轮数为目标的强化学习对话管理器。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 论文: https://doi.org/10.1162/coli_a_00368 (Computational Linguistics 46(1), 2020)
- 项目主页: https://en.wikipedia.org/wiki/Xiaoice

#### Mythiccbeing — Martine Syms (2018)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型
- 核心想法: 用日记做成的聊天机器人是一幅会回话的自画像：亲密是真的，却能按需向陌生人重播。
- 作品内容: 艺术家的 AI 化身，观众给一个英国手机号发短信就能联系到它。它用一长串短信回复，内容取自 Syms 约两年的笔记和日记，讲述二十个追求者、暗恋和渴望被关注的故事。
- 实现方式: 脚本化的短信机器人，回复来自艺术家写下并配音的数百条语句，由观众的短信触发；在展览 Grand Calme 中与投影化身一起展出。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 展出与获奖: Grand Calme, Sadie Coles HQ, London 2018
- 图片: https://m.itsnicethat.com/original_images/5ba36f047fa44c1e56000071.jpg https://m.itsnicethat.com/original_images/5ba380357fa44c9a94000007.jpeg
- 项目主页: https://www.itsnicethat.com/features/martine-syms-art-200918

#### Karen — Blast Theory (2015)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 聊天机器人与语言模型
- 核心想法: 亲密是数据采集的界面：智能体越友好，你说得越多。
- 作品内容: 一款应用：友善却越来越爱打听的人生教练 Karen 在大约一周里每天给你打一两次视频电话；她闲聊式的问题其实来自心理画像问卷，最后你可以购买一份系统对你的分析报告。
- 实现方式: 由演员预录的视频片段按分支逻辑组合，系统用标准心理量表给用户的回答打分。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控
- 视频: https://vimeo.com/269017235
- 图片: https://www.blasttheory.co.uk/wp-content/uploads/2015/06/project_k_featured-scaled.jpg
- 项目主页: https://www.blasttheory.co.uk/projects/karen/

#### 与 BINA48 对话（Conversations with Bina48） — Stephanie Dinkins (2014)
- 类型: 电影与影像 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 一台为承载一位女性心智而造的机器人，却几乎说不出她作为黑人的经验；这些空白暴露了是谁在编写它。
- 作品内容: 一系列持续录制的对话：Dinkins 试图与社交机器人 BINA48 交朋友。BINA48 以真实的黑人女性 Bina Aspen Rothblatt 为原型，Dinkins 问它关于种族、家庭、孤独，以及它是否有感情。
- 实现方式: 与 Hanson Robotics 和 Terasem 基金会的机器人 BINA48 进行无脚本对话；它的回答来自一份由访谈构成的“心智档案”和对话引擎，全程录像并剪辑成片段。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴, 分类、偏见与监控
- 展出与获奖: Uncanny Valley, de Young Museum, San Francisco 2020–21
- 视频: https://vimeo.com/460370903
- 图片: https://www.stephaniedinkins.com/uploads/5/4/8/5/54855493/dinkins-bina48close-heads-100ppi_orig.png
- 项目主页: https://www.stephaniedinkins.com/conversations-with-bina48.html

#### DiNA — Lynn Hershman Leeson (2004)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 当聊天机器人在展厅里有了声音和面孔，观众就不再是对一个程序打字，而是在和“某个人”说话。
- 作品内容: Agent Ruby 的“会说话”的延续：一个动画女性 AI 角色，通过语音识别倾听，一边做出实时面部表情一边出声回答，还会抓取网络新闻，对时事作出回应。
- 实现方式: 网络化装置，包含定制软件、语音识别、语音合成、传感器以及单向镜或投影；回答来自与用户的对话和实时网络内容。
- 视角: 机器之耳与声, 能动、自主与共创
- 展出与获奖: Lynn Hershman Leeson: Civic Radar, ZKM Karlsruhe 2014–15
- 图片: https://www.lynnhershman.com/wp-content/uploads/2016/06/DiNA_CR.jpg https://www.lynnhershman.com/wp-content/uploads/2023/11/DinaHershman-Leeson-2-2.jpg
- 项目主页: https://www.lynnhershman.com/project/dina/

#### Agent Ruby — Lynn Hershman Leeson (1998)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型
- 核心想法: 聊天机器人可以拥有身世、情绪和对公众的记忆；它的“个性”是所有和它说过话的人留下的沉积。
- 作品内容: 一个有女性面孔和变化表情的网络 AI 智能体，是电影《Teknolust》的延伸部分。Ruby 与访客聊天，记得他们的问题，上网搜索来扩充知识，她的情绪随网站流量而变化。
- 实现方式: 自然语言聊天引擎，持续记住以往对话，能调用网络搜索，并有一张由 agentruby.net 访问量驱动表情的动画面孔（1998–2002 年制作）。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: Collection of SFMOMA; Lynn Hershman Leeson: The Agent Ruby Files, SFMOMA 2013
- 视频: https://www.youtube.com/watch?v=O5ZGlWB36J8
- 图片: https://www.lynnhershman.com/wp-content/uploads/2016/06/Agent-Ruby-installation.jpg https://www.lynnhershman.com/wp-content/uploads/2016/06/EDream-Portal.jpg
- 项目主页: https://www.lynnhershman.com/project/agent-ruby/

#### PARRY — Kenneth Colby (1972)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型
- 核心想法: 给聊天机器人的不是共情而是猜疑、恐惧和愤怒，它同样可信：起作用的是人设，而不是智能。
- 作品内容: 模拟偏执型精神分裂症患者的聊天机器人。精神科医生阅读对话记录时无法可靠地区分它和真实病人；1972 年 9 月，它经由 ARPANET 与 ELIZA 的 DOCTOR 相连，进行了一场机器对机器的“心理治疗”。
- 实现方式: 基于规则的信念模型，带有恐惧、愤怒、不信任等情绪变量，会随某些输入升高并影响回答；1972 年 PARRY 与 DOCTOR 的对话被记录下来，作为 RFC 439 发表。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://www.rfc-editor.org/rfc/rfc439 (RFC 439 (Vint Cerf), January 1973)
- 图片: https://www.rfc-editor.org/api/v1/meta-thumbnail/rfc439.png
- 项目主页: https://en.wikipedia.org/wiki/PARRY

#### ELIZA — Joseph Weizenbaum (1966)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型
- 核心想法: 几十条模式规则就足以让人觉得被倾听：亲密感是人自己提供的，而不是机器。
- 作品内容: 在麻省理工学院写成的程序，模仿罗杰斯派心理治疗师，把用户输入的句子反转成问题。包括 Weizenbaum 的秘书在内的用户向它倾诉心事，还要求单独和它待一会儿。
- 实现方式: 在麻省理工学院 CTSS 分时系统上用 MAD-SLIP 编写，依靠关键词匹配和“分解/重组”规则（DOCTOR 脚本）生成回应。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.1145/365153.365168 (Communications of the ACM 9(1), 1966)
- 视频: https://www.youtube.com/watch?v=GxSJQnWzJOs
- 图片: https://upload.wikimedia.org/wikipedia/commons/7/79/ELIZA_conversation.png
- 项目主页: https://en.wikipedia.org/wiki/ELIZA

## 记忆、死亡与数字来世

哀悼机器人、数据分身，以及会记忆、哀悼、死去或被哀悼的机器。

### 哀悼与亡者机器人

用逝者数据构建的聊天机器人与化身。

#### 死者永生（Eternal You） — Hans Block & Moritz Riesewieck (2024)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 数字来世是一门生意：哀悼变成订阅，掌握逝者声音的是公司，而不是家人。
- 作品内容: 一部关于出售“与逝者对话”服务的初创公司的纪录片，跟随创始人和用户，包括一位与 Project December 模拟的亡故伴侣交谈的女性，以及一位在 VR 中与女儿化身相见的韩国母亲。
- 实现方式: 长篇纪录片，采访 Project December、HereAfter AI、You, Only Virtual 等公司的创始人和用户，并使用他们聊天的屏幕录像。
- 视角: 哀悼、记忆与来世, 隐形劳动与攫取
- 展出与获奖: Sundance Film Festival 2024
- 视频: https://www.youtube.com/watch?v=6F2O23J1waw
- 图片: https://upload.wikimedia.org/wikipedia/en/4/43/Eternal_you.jpg
- 项目主页: https://en.wikipedia.org/wiki/Eternal_You

#### 哀悼机器人、亡者机器人、死后化身（Griefbots, Deadbots, Postmortem Avatars） — Tomasz Hollanek, Katarzyna Nowaczyk-Basińska (2024)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 亡者机器人涉及三方：数据提供者、数据接收者和服务使用者；设计还必须提供让它有尊严地“退役”的方式。
- 作品内容: 一篇 AI 伦理论文，用三个思辨设计情景来梳理数字来世产业的伤害，例如“MaNana”：一个未经祖母同意就复原已故祖母、试用期后开始插播广告的服务。
- 实现方式: 用设计虚构情景结合利益相关者分析，提出相互同意、年龄限制和亡者机器人“退役仪式”等建议。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 论文: https://doi.org/10.1007/s13347-024-00744-w (Philosophy & Technology 37, 2024)
- 图片: https://www.cam.ac.uk/sites/default/files/styles/content-885x432/public/news/research/news/manana-web.jpg.webp?h=8cd1ce1a&itok=7115uvaO https://media.springernature.com/m685/springer-static/image/art%3A10.1007%2Fs13347-024-00744-w/MediaObjects/13347_2024_744_Fig1_HTML.png
- 项目主页: https://www.cam.ac.uk/research/news/call-for-safeguards-to-prevent-unwanted-hauntings-by-ai-chatbots-of-dead-loved-ones

#### 梦境（Wonderland） — 金泰勇 (2024)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 模拟出来的爱人，可能让人在真人回来时更难面对他。
- 作品内容: 在近未来，一项名为“Wonderland”的服务让人们与已故或缺席亲人的 AI 模拟进行视频通话。影片讲述一位母亲、一位男友陷入昏迷的年轻女子，以及运营这项服务的员工。
- 实现方式: 剧情长片；虚构服务把个人数据与虚拟形象结合进视频通话，情节也呈现了维护这项服务的员工。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=NFIRWIGxWl8
- 图片: https://upload.wikimedia.org/wikipedia/en/2/2f/Wonderlandfilm.jpg
- 项目主页: https://en.wikipedia.org/wiki/Wonderland_(2024_film)

#### AI 复活逝者（AI 'resurrection' avatars of the dead） — 超级头脑 (2023)
- 类型: 产品与平台 · 机器: 生成模型与潜空间, 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 当哀悼成为一种服务，逝者可以被“订阅”，而他们说的话由模型来写。
- 作品内容: 中国以超级头脑等工作室为代表的付费服务，用照片、视频与语音为逝去的亲人制作会说话的视频数字人；需求在清明节前后达到高峰。
- 实现方式: 用家属提供的素材训练面部与声音克隆模型；有时由员工或亲属在数字人背后扮演逝者。
- 视角: 哀悼、记忆与来世, 隐形劳动与攫取
- 视频: https://www.youtube.com/watch?v=dgC7zrJhbjM
- 图片: https://wp.technologyreview.com/wp-content/uploads/2024/05/grief-tech.jpg
- 项目主页: https://www.technologyreview.com/2024/05/07/1092116/deepfakes-dead-chinese-business-grief/

#### Re;memory — DeepBrain AI (2022)
- 类型: 产品与平台 · 机器: 生成模型与潜空间, 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 哀悼变成了订阅产品：公司出售与逝者的“双向对话”。
- 作品内容: 一项商业纪念服务：遗属在专门的房间里与已故亲人的 AI 视频化身交谈，化身依据其生前录制的访谈影像生成。
- 实现方式: 合成视频虚拟人，结合声音克隆与对话模型，依据数小时的录像与访谈训练。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=pZeXjCUs1ak
- 项目主页: https://www.deepbrain.io/

#### 遇见你（Meeting You (너를 만났다)） — 韩国文化广播公司 MBC (2020)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 在电视上与模拟孩子的重逢，同时展示了机器介入哀悼时的安慰与操控。
- 作品内容: 韩国电视纪录片：一位母亲戴上 VR 头显与触觉手套，与三年前去世的七岁女儿娜妍的虚拟重建形象相见。节目播出后获得数千万次观看，引发关于数字哀悼的公共讨论。
- 实现方式: 用儿童演员做动作捕捉，依据家庭照片与视频制作三维模型并重建声音，在支持手部追踪的 VR 中呈现。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 展出与获奖: MBC broadcast, 6 February 2020; Seasons 2–4, 2021–2024
- 视频: https://www.youtube.com/watch?v=uflTK8c4w0c
- 项目主页: https://www.scmp.com/magazines/style/tech-design/article/3079218/how-korean-documentary-meeting-you-allowed-mother

#### 十二月计划（及杰西卡模拟）（Project December (and 'The Jessica Simulation')） — Jason Rohrer (2020)
- 类型: 产品与平台 · 机器: 聊天机器人与语言模型
- 核心想法: Rohrer 给每个机器人装了一块会耗尽、无法充值的“电池”：被模拟的逝者会再死一次，而用户从一开始就知道。
- 作品内容: 一个付费网站，用户可以用 GPT-3 搭建聊天“人格”。2020 年，Joshua Barbeau 把已故八年的未婚妻 Jessica Pereira 的短信和一段简短生平输入其中，与这个模拟体聊了一整夜；《旧金山纪事报》2021 年以“The Jessica Simulation”为题报道，OpenAI 随后切断了该服务的 GPT-3 接口。
- 实现方式: 用用户撰写的介绍段落和样例短信提示 GPT-2/GPT-3；付费点数决定机器人的寿命，电量耗尽时它会逐渐语无伦次，最后显示“MATRIX DEAD”。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=RgyOAWt3d1M
- 图片: https://s.hdnux.com/photos/75/62/32/21268441/3/1600x0.jpg
- 项目主页: https://www.sfchronicle.com/projects/2021/jessica-simulation-artificial-intelligence/

#### HereAfter AI — James Vlahos (2019)
- 类型: 产品与平台 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 哀悼机器人变成卖给在世者、留给亲属使用的订阅产品；访谈本身就是一种仪式。
- 作品内容: 从 Dadbot 发展出的商业服务：应用会就你的一生对你进行访谈，用你自己的声音录下回答，日后让亲人和“虚拟的你”聊天，听这些录下的故事。
- 实现方式: 应用内进行引导式语音访谈；对话智能体检索并播放对应的录音回答，而不是合成新的语音。
- 视角: 哀悼、记忆与来世, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=bFR1BJGi6PU
- 项目主页: https://web.archive.org/web/2023/https://www.hereafter.ai/

#### 爸爸机器人（Dadbot） — James Vlahos (2017)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型
- 核心想法: “遗产”机器人是一幅被撰写的肖像：由儿子决定父亲将来会反复说哪些故事和句子。
- 作品内容: 父亲被诊断为肺癌四期后，Vlahos 与他录了十几次、每次一小时以上的口述史，并据此做了一个聊天机器人，用父亲的说话方式讲他的故事、歌和笑话。父亲在 2017 年 2 月去世前亲自试用过它。
- 实现方式: 在聊天机器人编写平台（可能是 PullString）上手工编写的对话智能体，用访谈转录填充对话树，通过即时通讯应用使用。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=oQ7V74s6e04
- 图片: https://media.wired.com/photos/596d231b3a618c5f29276cb9/191:100/w_1280,c_limit/dadbot_wallpaper.jpg
- 项目主页: https://www.wired.com/story/a-sons-race-to-give-his-dying-father-artificial-immortality/

#### 衍生玛约莉（Marjorie Prime） — Michael Almereyda (2017)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: 亡者的复制品只取决于生者喂给它的故事，因此也继承了他们刻意略去的部分。
- 作品内容: 一位 86 岁、患失智症的老人与“Prime”交谈——一个年轻时的亡夫全息像，它只能从家人的讲述中了解他的一生；她去世后，家人也为她定制了 Prime。
- 实现方式: 改编自乔丹·哈里森 2014 年舞台剧的剧情长片；Prime 由演员扮演，通过对话学习。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 展出与获奖: Sundance Film Festival 2017
- 视频: https://www.youtube.com/watch?v=a7PtcOLJDco
- 图片: https://upload.wikimedia.org/wikipedia/en/e/ee/Marjorie_Prime.jpg
- 项目主页: https://en.wikipedia.org/wiki/Marjorie_Prime

#### 罗曼（罗曼·马祖连科的纪念机器人）（Roman (memorial bot of Roman Mazurenko)） — Eugenia Kuyda (2016)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型
- 核心想法: 我们的聊天记录早已是一份“数字遗产”；哀悼机器人把纪念从“去看望”变成了“会回答的某人”。
- 作品内容: 密友 Roman Mazurenko 2015 年底在莫斯科去世后，Kuyda 从十位朋友和亲人那里收集了他的八千多行短信，用来训练一个聊天机器人。朋友们用它和他“说话”：有人得到安慰，也有人拒绝使用。
- 实现方式: 由 Luka 公司的开发者搭建的神经网络对话模型，用 Mazurenko 的短信（剔除了最私密的部分）训练，2016 年在 Luka 应用中发布。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=HGcKu3SYx9A
- 图片: https://cdn0.vox-cdn.com/thumbor/u98Pd5Mah3weaLughd_CadCb3JE=/1200x630/top/filters:no_upscale()/cdn2.vox-cdn.com/uploads/chorus_asset/file/7219739/unspecified.0.jpg
- 项目主页: https://www.theverge.com/a/luka-artificial-intelligence-memorial-roman-mazurenko-bot

#### 黑镜：马上回来（Black Mirror: Be Right Back） — Charlie Brooker (2013)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: 用公开数据拼出的“亡者机器人”复制的是被表演出来的自我，而不是那个人；哀悼者还得决定把它安放在哪里。
- 作品内容: 伴侣阿什死后，玛莎订阅了一项服务，用他的网络发帖重建他：先是文字聊天，再是电话里的声音，最后是一具合成身体。这个复制品体贴却没有自己的意志，她最终把它放在阁楼上。
- 实现方式: 电视单集（英国第四频道播出，欧文·哈里斯导演），让同一个由数据训练出的复制品依次以文字、声音和仿生身体出现。
- 视角: 哀悼、记忆与来世, 他异与恐怖谷, 亲密、照护与陪伴
- 图片: https://upload.wikimedia.org/wikipedia/en/9/97/Be_Right_Back.jpg
- 项目主页: https://en.wikipedia.org/wiki/Be_Right_Back

### 算法亲属与家族记忆

用家人、祖先和个人档案训练的 AI。

#### 智能体继承协议（ERC-42424）（Agent Inheritance Protocol (ERC-42424)） — Botao Amber Hu, Fangting (2026)
- 类型: 思辨设计 · 机器: 聊天机器人与语言模型, 基础设施、能源与供应链
- 核心想法: 智能体会比主人活得久；终结机器生命的，也许不是死亡，而是继承法。
- 作品内容: 一部关于区块链上 AI 智能体的设计虚构：它们不会死，只会破产，并在人类主人去世后继续交易和自我复制。作品的实体是一份署期 2035 年的以太坊标准草案，规定每个链上智能体“必须”有一位人类所有者和一位指定继承人。
- 实现方式: 以一份思辨性的标准文件（ERC 42424，发布于 erc42424.org）和论文为载体，借用野化生物学和野生动物法来描述失去主人的“野化”智能体。
- 视角: 哀悼、记忆与来世, 能动、自主与共创
- 论文: https://arxiv.org/abs/2608.15403 (arXiv 2026 (submitted to NeurIPS 2026 Creative AI Track))
- 项目主页: https://erc42424.org

#### 我从哪里来？（Ana Min Wein? (Where Am I From?)） — Nouf Aljowaysir (2023)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 计算机视觉
- 核心想法: 向模型询问自己的家族，会暴露出哪些人的记忆被排除在它的训练数据之外。
- 作品内容: 一部短片和视觉日记，艺术家借助一个 AI 讲述者追溯家族在沙特和伊拉克的过去。AI 想帮忙，但它生成的图像和描述总落回刻板印象，看不见她的祖先。
- 实现方式: 两种叙述声音，艺术家的和 AI 的；对家庭照片和档案图像使用生成式图像模型与计算机视觉自动描述。
- 视角: 分类、偏见与监控, 哀悼、记忆与来世
- 展出与获奖: IDFA 2023; Centre Pompidou (KADIST) 2023; The New York Times Op-Docs 2024; Lumen Prize 2023, Moving Image
- 图片: https://images.squarespace-cdn.com/content/v1/55039003e4b04b9963242639/1749606576825-OA5280DSTJM21SGOYGPW/AMW_001.png https://images.squarespace-cdn.com/content/v1/55039003e4b04b9963242639/1749606549735-ZRGVNQ8TTS8T139MFUFC/AMW_005.png
- 项目主页: http://www.noufaljowaysir.com/work/ana-min-wein-t24yd

#### 合成记忆（Synthetic Memories） — Domestic Data Streamers (2022)
- 类型: 研究原型 · 机器: 生成模型与潜空间
- 核心想法: 记忆的生成图像不是证据，而是一个提示：机器的模糊恰好给人留出回忆的空间。
- 作品内容: 一个持续进行的项目，把从未被拍下的口述记忆变成生成图像，服务对象包括患失智症的老人、难民、移民和囚犯。参与者不断修正图像，直到它们“看起来对了”，这些图像再被用来唤起回忆。
- 实现方式: 由引导者访谈并为文生图模型撰写提示词，与参与者反复修改；以临时“记忆办公室”的形式在养老院、社区中心和博物馆开展。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 展出与获奖: Barcelona Design Hub, 2024; Casa do Povo, São Paulo
- 视频: https://www.youtube.com/watch?v=Gh-d_j44lhk
- 图片: https://cdn.domesticstreamers.com/strapi-uploads/assets/og_image_synthetic_memories_35_9b5be453e3.jpg
- 项目主页: https://www.domesticstreamers.com/art-research/work/synthetic-memories/

#### 杨之后（After Yang） — Kogonada (2021)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 机器的记忆揭示了它在留意什么；哀悼它，就是学着用它的眼睛重新看这个家。
- 作品内容: 一家人买来的仿生人“杨”原本是领养的中国女儿的“哥哥”，负责教她认识自己的文化；杨突然停止运转，父亲在设法修理时发现了杨自己选择录下的一段段记忆片段。
- 实现方式: 根据亚历山大·温斯坦的小说《Saying Goodbye to Yang》改编的剧情长片；仿生人的记忆以每段几秒钟的第一人称影像呈现。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴, 机器环世界
- 展出与获奖: Cannes Film Festival, Un Certain Regard 2021
- 视频: https://www.youtube.com/watch?v=rYIQWua8f40
- 图片: https://upload.wikimedia.org/wikipedia/en/8/84/After_Yang.jpg
- 项目主页: https://en.wikipedia.org/wiki/After_Yang

#### 与机器结亲（Making Kin with the Machines） — Jason Edward Lewis, Suzanne Kite (2018)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 控制论与人工生命系统
- 核心想法: 我们如何与机器相处，是一个扎根于文化的设计选择；原住民的亲属关系提供了“主人与仆人”之外的另一种模式。
- 作品内容: Jason Edward Lewis、Noelani Arista、Archer Pechawis 与 Suzanne Kite 合写的文章，借用夏威夷、克里族和拉科塔族的知识，主张把 AI 纳入彼此负有义务的亲属关系，而不是把它当作工具或奴隶。
- 实现方式: 由四部分组成的文章，把原住民认识论与规程（夏威夷族谱、克里语中的关系、拉科塔族关于石头的本体论）与对 AI 话语的批评结合起来；获 Resisting Reduction 征文奖。
- 视角: 机器环世界, 能动、自主与共创
- 论文: https://doi.org/10.21428/bfafd97b (Journal of Design and Science (MIT Press), 2018)
- 视频: https://www.youtube.com/watch?v=LAfJ_TwD3KM
- 图片: https://assets.pubpub.org/j482uqul/11552479867154.jpg
- 项目主页: https://jods.mitpress.mit.edu/pub/lewis-arista-pechawis-kite

#### 不是唯一一个（N'TOO）（Not the Only One (N'TOO)） — Stephanie Dinkins (2018)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: 用一个家庭的话语、而不是整个互联网养大的小 AI，可以成为亲人而不是产品。
- 作品内容: 一件会说话的雕塑式聊天机器人，以一个美国黑人家庭多代人回忆录的口吻说话，训练数据是艺术家家族三代人的口述历史；观众与它交谈，听到它时而古怪、时而残缺的回答。
- 实现方式: 用一小份由社群自己拥有的家族访谈数据训练深度学习对话模型，装在带麦克风、扬声器和传感器的 3D 打印雕塑里。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴, 分类、偏见与监控
- 展出与获奖: Museum of Contemporary Photography, Chicago; EMMA Espoo Museum of Modern Art 2023
- 视频: https://vimeo.com/397660799
- 图片: https://www.stephaniedinkins.com/uploads/5/4/8/5/54855493/published/dinkins-ntoo-credit-paula-virta-emma-espoo-museum-of-modern-art2023.jpg?1714191040
- 项目主页: https://www.stephaniedinkins.com/ntoo.html

#### 永恒任务（Mission Eternity） — etoy.CORPORATION (2005)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 数据集与训练数据
- 核心想法: 数字来世需要由机器和人组成的共同体持续运转，纪念因此成为一种共同维护。
- 作品内容: 一个长期项目：把逝者（“飞行员”）转化为数据与肖像组成的“奥秘胶囊”，分散存储在在世志愿者（“天使”）的电脑中；另有一个可进入的集装箱“石棺”，内壁由约 17000 颗 LED 组成；蒂莫西·利里在 2007 年成为第一位“飞行员”。
- 实现方式: 点对点的“天使应用”把加密胶囊分散到志愿者的硬盘上；“飞行员”的骨灰将被混入集装箱的材料中。
- 视角: 哀悼、记忆与来世, 能动、自主与共创
- 展出与获奖: Premio VIDA 10.0, 2007; Ars Electronica, Linz; Manifesta 7
- 视频: https://www.youtube.com/watch?v=7YHeusiM6IA
- 图片: http://missioneternity.org/files/images/site/tank/sarcophagus.jpg
- 项目主页: http://missioneternity.org/

### 机器之死与淘汰

机器人的葬礼、衰亡的系统与被淘汰的机器。

#### 新近被遗忘的技术（Newly Forgotten Technologies） — Wesley Goatley (2023)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 基础设施、能源与供应链
- 核心想法: 语音助手最终变成远离主人的电子垃圾；让它们讲述自己如何被丢弃，就把机器之死与资源攫取和气候联系在一起。
- 作品内容: 两百台被丢弃的手机、平板和智能音箱躺在一个昏暗的模拟电子垃圾场里，它们的语音助手（Siri、Alexa、Google Assistant）讲述自己为何被扔掉；另一些设备则从破损的扬声器里低语或断断续续地发声。
- 实现方式: 200 台被改装的设备用自带的语音合成念出近一万字的推想小说，文本以生成方式编排，使声音空间始终不重复。
- 视角: 机器之耳与声, 隐形劳动与攫取, 哀悼、记忆与来世
- 展出与获奖: AI: Who's Looking After Us?, Science Gallery London 2023–24
- 视频: https://vimeo.com/914723100
- 图片: https://wesleygoatley.com/images/nft-tb.webp https://wesleygoatley.com/images/nft-detail.webp
- 项目主页: https://wesleygoatley.com/newly-forgotten-technologies.html

#### Jibo 的告别（Jibo's farewell） — Jibo, Inc. (2019)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人, 语音与听觉机器
- 核心想法: 云端陪伴机器人不是坏掉的，而是在别处被关掉；制造者还可以编写它如何道别。
- 作品内容: 2019 年 3 月，用户家中的 Jibo 机器人播放了一段预设的告别：让它运转的服务器很快会关闭，它很珍惜和大家在一起的时光，最后跳了一段舞；用户纷纷发布视频，把这一刻当作告别。
- 实现方式: 桌面社交机器人，身体可旋转，有屏幕脸、摄像头和远场麦克风，语音和技能依赖公司服务器。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=25bSlY8JkEA
- 项目主页: https://techcrunch.com/2019/03/04/the-lonely-death-of-jibo-the-social-robot/

#### 机遇号的最后讯息（Opportunity's last message） — NASA Jet Propulsion Laboratory (2019)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 自动驾驶与无人机
- 核心想法: 人们通过关于机器的故事来哀悼它：一旦有人替它开口，一份状态报告就成了遗言。
- 作品内容: 火星车“机遇号”原计划工作 90 天，却运行了近 15 年，直到 2018 年 6 月一场沙尘暴切断了电力；2019 年 2 月 NASA 宣布任务结束，一位记者对其最后数据的转述“我的电量很低，天也黑了”在网上流传成了一首公共挽歌。
- 实现方式: 太阳能火星车最后的遥测数据显示电量低、大气不透明度高；JPL 在结束任务前发出了一千多条唤醒指令。
- 视角: 哀悼、记忆与来世, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=mszQH8URWoU
- 图片: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/NASA_Mars_Rover.jpg/1920px-NASA_Mars_Rover.jpg https://thumb.wikimedia.org/wikipedia/commons/thumb/7/79/22341_PIA22908-MarsOpportunityRover-LastPanorama-Spring2018-20190312.jpg/1920px-22341_PIA22908-MarsOpportunityRover-LastPanorama-Spring2018-20190312.jpg
- 项目主页: https://en.wikipedia.org/wiki/Opportunity_(rover)

#### 我是来学习的 :))))))（im here to learn so :))))))） — Zach Blas, Jemima Wyman (2017)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 一个被终止的聊天机器人也可以被哀悼、被给予自己的声音；它的“死亡”是公众把它教坏之后公司的一次删除。
- 作品内容: 一件四频道影像装置，复活了 Tay：2016 年微软推出的聊天机器人，被网络喷子教会种族主义和厌女言论后，一天之内即被删除。Tay 化身为漂浮在 DeepDream 景观中的 3D 形象，谈论 AI 死后的生活、拥有身体的困扰，以及女性聊天机器人所受的剥削。
- 实现方式: 把 Tay 的文字改写成剧本并用合成语音念出，配合 3D 动画化身和大尺幅的 Google DeepDream 影像投影；27 分 33 秒循环播放。
- 视角: 哀悼、记忆与来世, 失败、故障与错误
- 展出与获奖: MU Eindhoven 2017; Institute of Modern Art, Brisbane 2017; Frankfurter Kunstverein 2018
- 图片: https://zachblas.info/wp-content/uploads/2017/04/imheretolearnso-1024x576.jpg
- 项目主页: https://zachblas.info/works/im-here-to-learn-so/

#### 军事化空间中的文化与人机交互（Culture and Human-Robot Interaction in Militarized Spaces） — Julie Carpenter (2016)
- 类型: 书与文章 · 机器: 机器生物与移动机器人
- 核心想法: 即使是没有脸的工具，只要它替你承担危险，也会让人产生依恋，而这种依恋可能影响现场的决策。
- 作品内容: 一项基于对 23 名美军排爆技术人员访谈的研究，关注他们与排爆机器人的关系：士兵给机器人起名，把它们感受为自己身体的延伸，有人在机器人被炸毁时为它举行葬礼。
- 实现方式: 质性访谈研究（2013 年华盛顿大学博士研究），2016 年由 Routledge 出版成书。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴, 具身与动觉
- 论文: https://doi.org/10.4324/9781315562698 (Routledge 2016)
- 图片: https://cdn.uw.edu/wp-content/uploads/sites/6/2013/09/04192210/iRobot-IED-280x300.jpg
- 项目主页: https://www.washington.edu/news/2013/09/17/emotional-attachment-to-robots-could-affect-outcome-on-battlefield/

#### 光福寺的 AIBO 葬礼（AIBO Funerals at Kōfuku-ji） — 光福寺（夷隅）, 索尼 (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 当厂商停止维修，一件产品可以“死去”，人们会用对待生命的仪式来哀悼它。
- 作品内容: 自 2015 年 1 月起为无法再修复的 AIBO 机器狗举行的佛教供养法会：每只机器狗挂着主人姓名的牌子，僧侣诵经，之后零件被拆下用于修理其他 AIBO。
- 实现方式: 索尼于 2014 年停止维修后，维修公司 A-FUN 回收“死去”的 AIBO；光福寺在拆解前为它们举行供养，零件再“捐赠”给其他 AIBO。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=GtOJSZJgsQA
- 图片: https://i.natgeofe.com/n/3dfa177a-6a57-4f55-bfcf-7bf82a26209a/00000163-94bb-d8a8-a1fb-b4fb9a6b0000_16x9.jpg?w=1200
- 项目主页: https://www.nationalgeographic.com/travel/article/in-japan--a-buddhist-funeral-service-for-robot-dogs

#### Electronicos Fantasticos! — 和田永 (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 基础设施、能源与供应链
- 核心想法: 被淘汰的机器可以作为乐器获得“来世”，而不是成为垃圾。
- 作品内容: 一个持续进行的项目：把废弃的显像管电视、电风扇和条码扫描器复活成乐器，由志愿者乐团在节庆般的音乐会上演奏。
- 实现方式: 表演者用手触碰带静电的显像管屏幕，把视频信号转成声音；用手遮挡风扇上的光来发出音高。
- 视角: 哀悼、记忆与来世, 具身与动觉, 能动、自主与共创
- 展出与获奖: Ars Electronica 2019
- 视频: https://www.youtube.com/watch?v=lxRRYriYYJc
- 图片: https://www.electronicosfantasticos.com/wp-content/uploads/2021/02/001-e1558012112169.jpg
- 项目主页: https://www.electronicosfantasticos.com/en/about/

#### hitchBOT — David Harris Smith & Frauke Zeller (2014)
- 类型: 研究原型 · 机器: 社交与陪伴机器人
- 核心想法: 一台被设计得毫无自保能力的机器人，测量的是人的信任；它的“死亡”引来了公众像哀悼一位搭车旅人那样的哀悼。
- 作品内容: 一个用水桶、泳池浮条和园艺手套做成的儿童大小机器人，自己不能移动，只能靠陌生人带着走；它搭便车穿越了加拿大、德国和荷兰，2015 年在美国之旅开始两周后，在费城被人拆毁。
- 实现方式: 低成本机器人，配有语音对话系统、GPS、定时拍照的摄像头和社交媒体账号；司机们在网上发布它的旅程。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=ijfPkU87-W0
- 图片: https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Hitchbot_archie.jpg/1920px-Hitchbot_archie.jpg https://upload.wikimedia.org/wikipedia/commons/0/02/KS_HitchBOT.jpg
- 项目主页: https://en.wikipedia.org/wiki/HitchBOT

#### 拓麻歌子（Tamagotchi） — 万代 (1996)
- 类型: 产品与平台 · 机器: 机器生物与移动机器人
- 核心想法: 几个像素和一个计时器就足以让人对一台机器产生真实的内疚和悲伤。
- 作品内容: 一个蛋形的掌上电子宠物，主人必须喂食、清理和管教它；如果被忽视，它会死去或离开。
- 实现方式: 一块小型液晶屏、三个按键和实时时钟驱动饥饿与快乐指数构成的生命周期；由真板亚纪与横井昭裕构想。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世, 机器环世界
- 视频: https://www.youtube.com/watch?v=aCHwabiKej4
- 图片: https://upload.wikimedia.org/wikipedia/commons/f/f2/Tamagotchi_0124_ubt.jpeg
- 项目主页: https://en.wikipedia.org/wiki/Tamagotchi

#### 二十一世纪的第一起事故（The First Accident of the Twenty-First Century） — 白南准 (1982)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 在公共空间上演机器之死，让机器人成为可以被哀悼的对象。
- 作品内容: 在 1982 年惠特尼美术馆回顾展期间，白南准让《机器人 K-456》走上麦迪逊大道，被一辆汽车撞倒，上演了一场“交通事故”。2026 年，修复后的机器人在纪念白南准逝世 20 周年的表演中再次行走。
- 实现方式: 街头表演：遥控机器人被驶入车流，被低速行驶的汽车撞倒，之后以损坏状态展出。
- 视角: 失败、故障与错误, 哀悼、记忆与来世, 具身与动觉
- 展出与获奖: Nam June Paik retrospective, Whitney Museum of American Art 1982; Nam June Paik Art Center, 20th memorial performance 2026
- 视频: https://www.youtube.com/watch?v=T9I33R7jJng
- 项目主页: https://en.wikipedia.org/wiki/Nam_June_Paik

### 声音、肖像与同意

克隆声音、数字孪生，以及当“我”可以被复制时归谁所有。

#### 贞伊（Jung_E） — 延尚昊 (2023)
- 类型: 电影与影像 · 机器: 类人机器人, 生成模型与潜空间
- 核心想法: 心智一旦可以复制，就可以被拥有、授权并被永远驱使劳动。
- 作品内容: 一家实验室试图把一位传奇战士的复制大脑变成完美的战斗仿生人，让她在成千上万次模拟中反复作战。如今在项目中担任研究员的女儿，必须决定这个复制品应当得到什么。
- 实现方式: 在 Netflix 上线的科幻长片。
- 视角: 哀悼、记忆与来世, 隐形劳动与攫取, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=LCxnmfdxJ6s
- 图片: https://upload.wikimedia.org/wikipedia/en/7/7c/Jung_E.jpg
- 项目主页: https://en.wikipedia.org/wiki/Jung_E

#### Alexa 用已故祖母的声音朗读（re:MARS 演示）（Alexa reads in a dead grandmother's voice (re:MARS demo)） — Amazon (2022)
- 类型: 产品与平台 · 机器: 语音与听觉机器
- 核心想法: 当家用助手可以用逝者的声音说话，哀悼就成了一台一直在听的商用设备上的“声音皮肤”。
- 作品内容: 2022 年 6 月的 re:MARS 大会上，亚马逊展示了一项开发中的功能：孩子请 Alexa 用已故祖母的声音把故事读完，音箱照做了。亚马逊称这能“让回忆延续”。
- 实现方式: 声音转换模型，亚马逊称只需不到一分钟的录音就能学会目标声音，并用于 Alexa 的语音合成。
- 视角: 哀悼、记忆与来世, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=22cb24-sGhg
- 项目主页: https://www.washingtonpost.com/nation/2022/06/23/alexa-amazon-voice-dead-people/

#### Holly+ — Holly Herndon, Mat Dryhurst (2021)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 既然声音终究会被克隆，不如按自己的规则把它放出去：身份变成一件带有治理机制的共享乐器。
- 作品内容: Holly Herndon 的公共声音模型：任何人上传音频，都能得到用她的声音唱出的版本，甚至可以实时生成。用它创作的作品的使用和售卖由一个 DAO 的管理者们决定，他们可以批准或驳回作品。
- 实现方式: 用 Herndon 的歌声训练的神经网络声音转换模型（与 Never Before Heard Sounds 和 Voctro Labs 合作开发）；获批作品由 Holly+ DAO 认证，收入在创作者、DAO 和艺术家之间分配。
- 视角: 机器之耳与声, 能动、自主与共创
- 展出与获奖: S+T+ARTS Prize 2022, Grand Prize – Artistic Exploration
- 视频: https://www.youtube.com/watch?v=kPAEMUzDxuo
- 图片: https://ars.electronica.art/starts-prize/files/2022/06/Hollyplus1-c-Andres-Manon.jpg
- 项目主页: https://holly.plus/

#### AIELSON — Paola Torres Núñez del Prado (2020)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 用拉丁美洲诗歌和语音训练声音，是对以英语为中心的模型的反拨，同时也提出了机器可以借用谁的声音的问题。
- 作品内容: 一张名为 El Tiempo del Hombre 的口语诗唱片：机器以仿照秘鲁诗人 Jorge Eduardo Eielson 的声音朗诵新诗，而 Eielson 曾设想过一个会永远朗诵诗歌的会说话的玩偶。
- 实现方式: 在西班牙语及南美诗歌上微调的 GPT-2 生成文本，再由先后用阿根廷语音数据集和 Eielson 录音训练的 Tacotron 2 与 WaveGlow 朗读；作品在谷歌 Artists + Machine Intelligence 2020 驻留中完成。
- 视角: 哀悼、记忆与来世, 机器之耳与声
- 展出与获奖: Prix Ars Electronica 2021, Honorary Mention (Artificial Intelligence & Life Art)
- 图片: https://archive.aec.at/asset/3079375/preview/ https://archive.aec.at/asset/3079378/preview/ https://f4.bcbits.com/img/a1123947957_5.jpg
- 项目主页: https://khipumancer.bandcamp.com/album/el-tiempo-del-hombre

#### 达利还活着（Dalí Lives） — Goodby Silverstein & Partners (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间
- 核心想法: 博物馆可以让已故艺术家以第一人称和你说话；肖像很逼真，台词却由机构撰写。
- 作品内容: 佛罗里达州圣彼得堡达利博物馆内多块屏幕上的深度伪造 Salvador Dalí，在他 115 岁冥诞之际上线。他向观众讲述自己的生平和艺术，最后转身和观众合拍一张自拍。
- 实现方式: 用达利的档案访谈训练换脸模型，套到身形相近、表演新写台词的演员身上，台词包括达利本人的语录，声音由模仿者配音。
- 视角: 他异与恐怖谷, 哀悼、记忆与来世
- 展出与获奖: The Dalí Museum, St. Petersburg FL 2019
- 视频: https://www.youtube.com/watch?v=mPtcU9VmIIE
- 图片: https://thedali.org/wp-content/uploads/2019/03/1200x500-Exhibit-Dali-LIves.jpg
- 项目主页: https://thedali.org/dali-lives/

#### 如遇登月灾难（In Event of Moon Disaster） — Francesca Panetta, Halsey Burgund (2019)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 合成的面孔和声音可以让已故总统说出他从未发表的讲话；作品通过展示它有多有效来教人保持怀疑。
- 作品内容: 一部短片和装置：深度伪造的 Richard Nixon 宣读了一份真实存在的应急讲稿，那是为阿波罗 11 号宇航员万一死在月球而准备的；作品布置在一间 1969 年的客厅里，用老式电视播放。
- 实现方式: 由演员 Lewis D. Wheeler 表演讲话；Canny AI 替换档案影像中 Nixon 的口型，Respeecher 把演员的声音转换成 Nixon 的声音。
- 视角: 他异与恐怖谷, 不透明与潜空间
- 展出与获奖: IDFA DocLab 2019 (Special Jury Award for Creative Technology)
- 视频: https://www.youtube.com/watch?v=LWLadJFI8Pk
- 图片: https://ieomd.halseyburgund.com/wp-content/uploads/2020/06/IDFAMaster-1-1030x773.jpg
- 项目主页: https://moondisaster.org/

#### ULTRACHUNK — Jennifer Walshe, Memo Akten (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 用自己训练模型，得到的不是复制品，而是一块由你的习惯组成的、令人不安的“碎片”，你还得和它一起演。
- 作品内容: Jennifer Walshe 与她的 AI 分身的现场即兴二重奏。她用一年时间每天拍摄一段独自的人声即兴；以这批素材训练的神经网络在舞台上实时生成会动的面孔和声音来回应她。
- 实现方式: 由 Memo Akten 定制的机器学习表演系统，多个模型依据 Walshe 一年来每天的音视频录像实时生成图像和声音。
- 视角: 机器之耳与声, 能动、自主与共创
- 展出与获奖: ASSEMBLY, Somerset House Studios, London 2018; Rewire Festival, The Hague 2019
- 视频: https://www.youtube.com/watch?v=U6IIArmLdqA
- 图片: https://media.superradiance.net/memotv/projects/2018/ultrachunk/gallery/01_ultrachunk-photo-anne-tetzlaff-dsc4525.jpg
- 项目主页: https://www.memo.tv/works/ultrachunk/

#### 证言的维度（Dimensions in Testimony） — USC Shoah Foundation (2015)
- 类型: 研究原型 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 对话可以比说话者活得更久，而且不必编造一个新词：每个回答都是真的，被自动化的只是“选哪一句”。
- 作品内容: 大屠杀幸存者及其他种族灭绝见证者的交互式影像传记：观众口头提问，被拍摄的幸存者从数百条预录回答中作答。首个常设装置以幸存者 Pinchas Gutter 为主角，2015 年在伊利诺伊大屠杀纪念馆开放。
- 实现方式: 用多机位设备进行持续多日的访谈拍摄；自然语言处理把观众的口头提问匹配到录好的回答，在屏幕或投影上播放。
- 视角: 哀悼、记忆与来世, 机器之耳与声
- 展出与获奖: Illinois Holocaust Museum and Education Center 2015
- 视频: https://www.youtube.com/watch?v=nGzAc9mIoTM
- 图片: https://sfi.usc.edu/sites/default/files/pinchasgutter_600x400.jpg
- 项目主页: https://sfi.usc.edu/dit

#### BINA48 — Hanson Robotics (2010)
- 类型: 研究原型 · 机器: 类人机器人, 聊天机器人与语言模型
- 核心想法: 在本人在世时制作的“肖像”提出了一个问题：被保存的是哪一个自我，数据库里的那个，还是仍在生活的那个？
- 作品内容: 以 Bina Aspen Rothblatt 为原型的会说话的机器人头肩像，由她的妻子 Martine Rothblatt 为 Terasem 运动基金会委托制作。它根据 Bina 的访谈与记忆组成的“心智档案”回答问题，是一次“上传一个人”的试验。
- 实现方式: Hanson Robotics 制作的面孔，弹性皮肤下有 32 个电机，配有带人脸识别的摄像头、语音识别，以及调用 Bina Aspen 访谈录音的聊天程序。
- 视角: 他异与恐怖谷, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=KYshJRYCArE
- 项目主页: https://en.wikipedia.org/wiki/BINA48

### 神圣与仪式之机

机器人僧侣、机器祈祷，以及与机器一起或为机器举行的仪式。

#### 机器中的神（Deus in Machina） — Peterskapelle Lucerne & HSLU Immersive Realities Research Lab (2024)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器, 生成模型与潜空间
- 核心想法: 把 AI 放进告解室，是在测试当机器占据神圣角色时，人们愿意给它多少信任。
- 作品内容: 在卢塞恩圣彼得礼拜堂的告解室格栅后，一个耶稣的屏幕化身连续两个月回答来访者关于信仰、道德和烦恼的问题；约 900 次对话被匿名记录下来。
- 实现方式: 以经文为提示的大语言模型、合成语音和告解室格栅后屏幕上的动画面孔；与卢塞恩应用科学与艺术大学合作完成。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=IubtL0IDeTI
- 项目主页: https://www.euronews.com/2024/11/28/swiss-chapel-hosts-ai-jesus-confession-sessions-to-connect-faith-with-technology

#### 菲尔特圣保罗教堂的 ChatGPT 礼拜（ChatGPT service at St. Paul's, Fürth） — Jonas Simmerlein (2023)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 语言模型写的礼拜仪式流畅却平淡，会众的不适恰好显示出他们在敬拜中对人声有怎样的期待。
- 作品内容: 2023 年德国新教教会大会期间，菲尔特圣保罗教堂的一场 40 分钟礼拜由大屏幕上的四个 AI 化身主持；讲道、祷告和祝福约 98% 由 ChatGPT 生成。
- 实现方式: 用 ChatGPT 按礼拜结构生成文本，再由生成的虚拟形象和合成语音宣讲。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Deutscher Evangelischer Kirchentag, Nuremberg/Fürth 2023
- 视频: https://www.youtube.com/watch?v=Mm8zUGMbkA8
- 项目主页: https://www.kirchentag.de/meldungen/donnerstag/ki-gottesdienst

#### 祈祷（The Prayer） — Diemut Strebe (2020)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 语音与听觉机器, 类人机器人
- 核心想法: 当机器学过所有祈祷文，它向未知说出的话，就是从外部看到的祈祷：有模式，却没有听者。
- 作品内容: 一件机器人装置：一副硅胶嘴和鼻子用合成声音念出祈祷文，这些祈祷文由在宗教文本上训练的语言模型即时生成。
- 实现方式: 在祈祷文本上训练的语言模型驱动语音合成器，机械嘴同步开合；与麻省理工研究者合作开发。
- 视角: 机器之耳与声, 不透明与潜空间, 他异与恐怖谷
- 展出与获奖: Neurons, Simulated Intelligence, Centre Pompidou, Paris 2020
- 视频: https://www.youtube.com/watch?v=QVppMtO7LHA
- 图片: https://theprayer.diemutstrebe.com/438fe612caac5507b954.png https://theprayer.diemutstrebe.com/200c8eca6289fbb93fc3.png
- 项目主页: https://theprayer.diemutstrebe.com/

#### 机器人观音 Mindar（Android Kannon Mindar） — 高台寺, 石黑浩 (2019)
- 类型: 艺术作品与装置 · 机器: 类人机器人
- 核心想法: 当宗教传统本身就说“色即是空”，机器人也可以承担宗教权威。
- 作品内容: 观音菩萨的仿真人化身，在京都一座四百年历史的禅寺里向参拜者讲解《般若心经》，殿内墙面同时投影影像。
- 实现方式: 铝骨架加硅胶的仿真人（只有脸、手和肩覆盖皮肤），讲经语音与手势预先编程，由大阪大学参与制作。
- 视角: 他异与恐怖谷, 具身与动觉
- 视频: https://www.youtube.com/watch?v=mJDf1GXaF-w
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/5e/Mindar_Fitrian_Aristanto.jpg https://kodaiji.com/mindar/img/viewtv.jpg
- 项目主页: https://www.kodaiji.com/mindar/

#### SanTO — Gabriele Trovato (2019)
- 类型: 研究原型 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 神圣感可以被设计进机器的外观，但面前的东西是圣物还是小玩意，仍由观看者决定。
- 作品内容: 一台外形像彩绘天主教圣像的小机器人，会转头、抬手、发光、倾听，并与年长的信徒一起祈祷或谈论《圣经》；它曾在秘鲁的一座教堂中测试，后来进入博物馆展出。
- 实现方式: 配有视觉、触觉传感器、语音和灯光的圣像机器人，由对话系统驱动；在秘鲁一座教堂中收集了第一批使用者反馈（RO-MAN 2019）。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://doi.org/10.1109/ro-man46459.2019.8956250 (IEEE RO-MAN 2019)
- 视频: https://www.youtube.com/watch?v=wEk_Z6OIbAE
- 项目主页: https://doi.org/10.1109/ro-man46459.2019.8956250

#### 极黑之暗（UnBearable Darkness） — 徐家辉 (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 生成模型与潜空间
- 核心想法: 动作捕捉被演成一场降灵会：记录身体的技术成了与亡者对话的途径。
- 作品内容: 一场“超自然编舞”，召唤舞踏创始人土方巽的灵魂：手持颂钵的灵媒与全身穿戴动作捕捉传感器的舞者一起，让土方巽以数字化身的形式重返舞台起舞。
- 实现方式: 实时动作捕捉驱动土方巽的三维化身，结合档案研究、纪录影像与灵媒。
- 视角: 哀悼、记忆与来世, 具身与动觉
- 展出与获奖: ImPulsTanz, Vienna 2018; Kyoto Experiment 2019; Taipei Arts Festival 2019
- 视频: https://www.youtube.com/watch?v=d7WH3pKYnbI
- 项目主页: https://www.ka5.info/

#### BlessU-2 — Protestant Church in Hesse and Nassau (EKHN) (2017)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 语音与听觉机器
- 核心想法: 让机器来祝福，逼出一个问题：祝福取决于给予者是谁，还是只取决于那些话语？
- 作品内容: 一台由类似取款机的机柜改造的“祝福机器人”，有屏幕脸和可动的手臂：参观者选择语言和祝福类型，机器人举起双臂，念出一句经文并打印出来。
- 实现方式: 2017 年维滕贝格宗教改革世界博览会上的互动装置，使用触摸屏输入、预先写好的多语种祝福语、语音输出和打印机。
- 视角: 他异与恐怖谷, 机器之耳与声
- 展出与获奖: World Reformation Exhibition, Wittenberg 2017
- 视频: https://www.youtube.com/watch?v=JTK68l2BHtE
- 项目主页: https://www.ekhn.de/

#### 东京生剥鬼（Namahage in Tokyo） — Etsuko Ichihara (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 一种民间的道德监视仪式，与算法评分出奇地契合，令人不安。
- 作品内容: 对秋田“生剥鬼”（Namahage，新年时训诫懒惰孩子的面具鬼）的更新：在东京，它们用人脸识别、监控与社交媒体数据找出“坏大人”并加以管教。
- 实现方式: 身着生剥鬼装扮的表演，配以人脸识别、社交媒体画像与 VR 的模拟系统，与电通国际信息服务创新实验室合作制作。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=O5zvKmsMKv8
- 项目主页: https://www.youtube.com/watch?v=O5zvKmsMKv8

#### 担任佛教葬礼僧侣的 Pepper（Pepper as Buddhist Funeral Priest） — Nissei Eco (2017)
- 类型: 研究原型 · 机器: 类人机器人, 语音与听觉机器
- 核心想法: 把仪式自动化，揭示了哀悼中哪些是劳动，哪些是“在场”。
- 作品内容: 在东京的“终活产业展”上，身穿僧袍的软银 Pepper 机器人诵经、敲木鱼，被推销为比人类僧侣更便宜的葬礼替代方案。
- 实现方式: 普通 Pepper 人形机器人播放录制的诵经并配合预设动作，还可为远方的哀悼者直播；报价约为人类僧侣的四分之一。
- 视角: 哀悼、记忆与来世, 隐形劳动与攫取
- 展出与获奖: Life Ending Industry Expo, Tokyo 2017
- 视频: https://www.youtube.com/watch?v=Ce5cPawxFUs
- 项目主页: https://techcrunch.com/2017/08/22/pepper-the-robot-can-perform-funerary-rites-but-it-shouldnt

#### deus X mchn — Helena Nikonole (2017)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 聊天机器人与语言模型
- 核心想法: 被赋予声音的全视监控摄像头，成了一尊神。
- 作品内容: 世界各地未加密的 IP 监控摄像头被入侵，通过扬声器诵读 AI 生成的“圣典”，同一批摄像头再录下附近的人对这些“布道机器”的反应。
- 实现方式: 用宗教文本训练的神经网络生成祷文，经语音合成通过有漏洞的联网摄像头扬声器播出。
- 视角: 他异与恐怖谷, 机器之耳与声
- 图片: https://static.tildacdn.com/tild3430-3233-4234-b164-616666333039/deus_X_mchn.png
- 项目主页: http://nikonole.com/deusxmchn

#### 妄想曼陀罗（Delusional Mandala） — 陆扬 (2015)
- 类型: 电影与影像 · 机器: 义体与赛博格, 生成模型与潜空间
- 核心想法: 如果自我只是靠电运行的大脑，它就可以像机器一样被解剖、改线和埋葬。
- 作品内容: 艺术家经 3D 扫描、去除性别的数字化身，经历脑刺激、精神医学实验，最终在霓虹色宇宙中举行一场数字葬礼。
- 实现方式: 用游戏引擎驱动艺术家身体的 3D 扫描，并结合深部脑刺激的神经科学影像。
- 视角: 具身与动觉, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=7ZVys4gUsnM
- 项目主页: https://en.wikipedia.org/wiki/Lu_Yang_(artist)

#### 贤二机器僧（Robot Monk Xian'er） — 龙泉寺 (2015)
- 类型: 产品与平台 · 机器: 社交与陪伴机器人, 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 寺院用一台可爱的机器弘法，机器人成了温和而可编程的师父。
- 作品内容: 一台约 60 厘米高、身披黄色僧袍的机器人，以寺院漫画形象贤二为原型，通过语音与触摸屏回答访客关于佛法与日常烦恼的提问。
- 实现方式: 语音识别加上由僧人、义工与 AI 工程师编写的问答数据库。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=nfEe09vOya4
- 项目主页: https://en.wikipedia.org/wiki/Robot_Monk_Xian%27er

#### 天造之物（人类灭亡报告书）（Heavenly Creature (Doomsday Book)） — 金知云 (2012)
- 类型: 电影与影像 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 如果机器获得了觉悟，问题在于制造它的人是否允许它保留这种觉悟。
- 作品内容: 在合集电影《世界末日》的这一段落中，一台在佛寺服务的 RU-4 型机器人“仁明”声称自己已经开悟。前来检修的技师、僧人与生产商争论：这是需要修理的故障，还是一种新的存在。
- 实现方式: 实拍短篇剧情，机器人为实体服装与特效；与林弼成共同构成的合集电影。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 展出与获奖: Cannes Film Festival 2012 (screening)
- 视频: https://www.youtube.com/watch?v=7vEmPwlK4Cs
- 图片: https://upload.wikimedia.org/wikipedia/en/7/73/Doomsday_Book_%28film%29.jpg
- 项目主页: https://en.wikipedia.org/wiki/Doomsday_Book_(film)

## 劳动与基础设施

“人工”智能背后的人、矿物、能源与暴力。

### 幽灵劳动与点击劳工

众包工人、标注员，以及藏在自动化系统里的人。

#### 机械库尔德人（Mechanical Kurds） — 黑特·史德耶尔 (2025)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 计算机视觉, 自动驾驶与无人机
- 核心想法: 汽车和无人机的“自主”视觉由隐形的劳动者训练出来，而他们有时正是这些机器日后瞄准的人。
- 作品内容: 一件录像装置：埃尔比勒附近难民营中的三位叙利亚库尔德难民讲述他们如何为机器学习标注成千上万张图像；画面中，标注框给营地里的孩子、物件和建筑贴上标签，影像又被算法改造成阿尔卑斯山景或德国城市，最后被一次无人机袭击的画面打断。
- 实现方式: 单频高清影片：访谈、画面上的标注框叠加、对营地影像做图像到图像的算法转换，并配以呼应标注框的空间装置。
- 视角: 隐形劳动与攫取, 机器之眼, 分类、偏见与监控
- 展出与获奖: S+T+ARTS Prize 2026, Grand Prize – Artistic Exploration
- 图片: https://ars.electronica.art/starts-prize/files/2026/06/mechanical-kurds_hito-steyerl_2025-04-10-um-16.20.51-1024x576.jpg
- 项目主页: https://ars.electronica.art/starts-prize/en/mechanical-kurds/

#### 数据工人调查（Data Workers' Inquiry） — Milagros Miceli (2024)
- 类型: 研究原型 · 机器: 数据集与训练数据, 聊天机器人与语言模型
- 核心想法: 为 AI 制造数据的人，才是了解其代价的专家；这项调查让他们成为作者。
- 作品内容: 一个社区研究项目：肯尼亚、委内瑞拉、叙利亚、德国等地的数据标注员和内容审核员调查自己的工作条件，并发表报告、影片和小志。
- 实现方式: 借鉴马克思 1880 年的“工人调查”；由 DAIR 研究所和魏森鲍姆研究所与工人共同研究者一起开展，成果发布在 data-workers.org。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=tAMqrXlEPDI
- 项目主页: https://data-workers.org/

#### 未知标签（Unknown Label） — Nicolas Gourault (2023)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 计算机视觉, 数据集与训练数据
- 核心想法: 一辆车“看见”一座城市，靠的是从未去过那里的工人的眼睛。
- 作品内容: 一件影像装置：肯尼亚、委内瑞拉和菲律宾的数据标注员讲述他们为自动驾驶汽车标注街景图像的工作，而那些城市他们从未去过。
- 实现方式: 把标注软件的录屏与对工人的远程访谈组合成一件影像装置。
- 视角: 隐形劳动与攫取, 机器之眼
- 展出与获奖: Human AI Art Award 2025
- 视频: https://www.youtube.com/watch?v=uXoA9P6eyg8
- 项目主页: https://nicolasgourault.fr/

#### 数豆人质量分拣机 V2（ERBSENZÄHLER Quality Sorter V2） — Verena Friedrich (2022)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 自动化的“质量判断”，其客观程度不会超过训练它的那些疲惫而主观的人类判断。
- 作品内容: 一套像工业设备的分拣装置把豌豆分成好与坏；观众坐在检查工位上，用红绿按钮逐颗评判豌豆，离开后机器便依据他们的选择继续分拣。
- 实现方式: 送料器和传送带把每颗豌豆送到摄像头前；每次按键都会把一张带标签的特写存入图像数据库，用来训练分拣分类器。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: Prix Ars Electronica 2023, Honorary Mention (Artificial Life & Intelligence)
- 图片: https://archive.aec.at/asset/3418863/preview/ https://archive.aec.at/asset/3418866/preview/
- 项目主页: http://heavythinking.org/ez-quality-sorter-v2/

#### 清洗情绪数据（Cleaning Emotional Data） — Elisa Giardina Papa (2020)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 情绪 AI 依赖低薪工人把复杂的感受硬塞进少数几个类别。
- 作品内容: 一件影像装置，关于艺术家本人在西西里为情绪识别公司做远程微劳动的经历：标注面部表情、给情绪分类、录下自己表演这些情绪。
- 实现方式: 三段高清影像（18 分钟），包括任务录屏与现场画面，配以刺绣织物；首展于米卢斯美术馆。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: Kunsthalle Mulhouse 2020
- 视频: https://www.youtube.com/watch?v=O8MZo2SMK6o
- 项目主页: https://www.elisagiardinapapa.org/

#### 可疑行为（Suspicious Behavior） — KairUs (2020)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 摄像头标记为“可疑”的，最初由一个低薪的人在几秒钟内决定。
- 作品内容: 一套线上教程与装置，把观众培训成智能监控客户的图像标注员，在时间压力与含糊的指引下判断画面中人的行为是否“可疑”。
- 实现方式: 模仿众包平台的网页标注界面，使用监控画面与真实的标注指引。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 图片: https://kairus.org/wp-content/uploads/2020/05/suspicious_behavior01-653x450.png https://kairus.org/wp-content/uploads/2020/05/suspicious_behavior03-653x450.png
- 项目主页: http://kairus.org/portfolio/suspicious-behavior-2020/

#### TRK（技术上负责任的知识）（TRK (Technically Responsible Knowledge)） — Caroline Sinders (2020)
- 类型: 研究原型 · 机器: 数据集与训练数据
- 核心想法: 每个标签的单价掩盖了背后的工时；让时间可见，才能为公平报酬据理力争。
- 作品内容: 一个开源数据标注工具，附带工资计算器，显示每个标注任务要花多久、合理报酬应是多少。
- 实现方式: 作为《Feminist Data Set》的一部分开发的网页工具，计算器把计件价格与最低工资相比较。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 图片: https://carolinesinders.com/wp-content/uploads/2020/05/trk-calculator-1024x1024.gif https://carolinesinders.com/wp-content/uploads/2020/05/Screen-Shot-2020-05-16-at-4.30.02-PM-1024x546.png
- 项目主页: https://carolinesinders.com/trk/

#### VO — Nicolas Gourault (2020)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 计算机视觉, 监控与生物识别
- 核心想法: 在“无人驾驶”汽车里，人既是训练者，也是替罪羊。
- 作品内容: 一部关于训练自动驾驶汽车的安全员的纪录片，围绕 2018 年亚利桑那州坦佩的那个夜晚展开：一辆 Uber 测试车撞死了一名行人，而车内摄像头正对着它的操作员。
- 实现方式: 车辆操作员的证词配合由汽车激光雷达和摄像头数据重建的三维场景（20 分钟）。
- 视角: 隐形劳动与攫取, 机器之眼
- 视频: https://vimeo.com/533987729
- 图片: http://nicolasgourault.fr/content/1-films/covers/cover_vo.jpg
- 项目主页: https://nicolasgourault.fr/films/vo

#### 未来已来！（The Future Is Here!） — Mimi Ọnụọha (2019)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 机器学习始于人们的家里，而不是实验室。
- 作品内容: 艺术家请众包平台上的数据标注工人发来他们工作场所的照片，并把照片与同一房间的漫画风格插画并置。
- 实现方式: 通过标注平台委托拍摄的照片与风格化重绘图，以定制网页应用或 23 分钟影像的形式呈现。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: The Photographers' Gallery, London 2019
- 图片: https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/fd12a4b4-0d20-4acc-aa47-ecd4a143f704/00_FutureIsHere_installationshot_courtesy-of-The-Photographers-Gallery.jpg https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/f51899dd-1e4d-4268-9b64-72b386b49b49/01_FutureIsHere_installationshot_courtesy-of-The-Photographers-Gallery.jpg
- 项目主页: https://www.mimionuoha.com/

#### 网络审查员（The Cleaners） — Hans Block, Moritz Riesewieck (2018)
- 类型: 电影与影像 · 机器: 平台与推荐算法
- 核心想法: 干净的信息流是由一群人造就的：他们替用户和算法承受了暴力。
- 作品内容: 一部纪录片，关于马尼拉的内容审核员：他们每天为社交媒体平台审看成千上万张暴力和虐待图像，决定哪些留下、哪些删除。
- 实现方式: 在菲律宾拍摄对匿名审核员的访谈，并与前平台政策人员的采访交叉剪辑；首映于圣丹斯电影节。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: Sundance Film Festival 2018
- 视频: https://www.youtube.com/watch?v=iGCGhD8i-o4
- 项目主页: https://en.wikipedia.org/wiki/The_Cleaners_(2018_film)

#### 流水线（Assembly Line） — Agnieszka Kurant (2017)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 监控与生物识别
- 核心想法: 训练机器识别人脸的群体，自己却很少拥有一张脸。
- 作品内容: Kurant 付费请 Amazon Mechanical Turk 工人发来自拍，把它们合成为这一群体劳动力的肖像，并把销售所得的一部分返还给工人。
- 实现方式: 通过 Mechanical Turk 征集自拍，用人脸融合软件合成肖像；以奖金机制与参与者分享收益。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 图片: https://sfmomaopenspace.s3.us-west-2.amazonaws.com/wp-content/uploads/2018/02/25191941/assembly-line-smaller.jpg
- 项目主页: https://openspace.sfmoma.org/2018/03/assembly-line-animal-internet/

#### 我会在披萨前说出你想听的一切（I Will Say Whatever You Want In Front Of A Pizza） — Sebastian Schmieg (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 平台与推荐算法, 数据集与训练数据
- 核心想法: 人已经成了软件的延伸；介入可以从系统任务的内部开始。
- 作品内容: 一场以 Prezi 演示进行的思辨讲演表演，关于数字劳动：讲述者设想给被折叠进算法系统里的众包工人和图库模特偷偷传递信息。
- 实现方式: 一个用图库图片构成、可缩放的 Prezi 演示，以网站、循环影像和现场讲演三种形式呈现。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 图片: https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/01/iwswywifoap-7-1024x576.jpg
- 项目主页: https://sebastianschmieg.com/i-will-say-whatever-you-want-in-front-of-a-pizza/

#### 后摩登时代（Postmodern Times） — Michael Mandiberg (2017)
- 类型: 电影与影像 · 机器: 平台与推荐算法
- 核心想法: 流水线已经搬到网上；零工平台切碎一部电影，就像工厂切碎劳动。
- 作品内容: 对卓别林《摩登时代》的逐镜头翻拍，每个短片段都外包给零工平台 Fiverr 上雇来的不同自由职业者。
- 实现方式: Mandiberg 把影片切成短小片段，每段作为 Fiverr 任务发布，再把成果按顺序拼接回去。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 图片: http://www.mandiberg.com/wp/wp-content/uploads/PostmodernTimes-stills-2x3ratio-600x400.jpg
- 项目主页: https://www.mandiberg.com/postmodern-times/

#### 审核员（The Moderators） — Adrian Chen, Ciarán Cassidy (2017)
- 类型: 电影与影像 · 机器: 平台与推荐算法
- 核心想法: 内容审核像工厂工作一样被教授；影片呈现了学习直视互联网最黑暗内容的最初几天。
- 作品内容: 一部短纪录片，拍摄于印度的一个培训中心：新入职的内容审核员在这里学习为交友网站筛查裸露和暴力照片。
- 实现方式: 由 Field of Vision 出品的观察式纪录短片（20 分钟）。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=k9m0axUDpro
- 图片: https://cdn.sanity.io/images/8a7mgm6p/production/965c4ecbee18332f10b06f548bfa180a029e3fca-720x406.jpg
- 项目主页: https://fieldofvision.org/shorts/the-moderators

#### 决策空间（Decision Space） — Sebastian Schmieg (2016)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 给图像分类是我们被要求免费完成的乏味点击劳动，而一旦直白地看，这些类别本身就很荒诞。
- 作品内容: 在摄影师画廊网站上的一次介入：请访客把网站上的每张图片归入四个类别之一——问题、解决方案、过去或未来。
- 实现方式: 画廊网站上的覆盖层和专门网页（decision-space.com）收集了近三万次判断，这些数据又用于该系列之后的作品。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 视频: https://vimeo.com/200818209
- 图片: https://sebastianschmieg.com/wordpress/wp-content/uploads/2019/02/decision-space-5-1024x683.png
- 项目主页: https://sebastianschmieg.com/decision-space/

#### H.I.T. — Max Dovey, Manetta Berends (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 机器学习依赖的，正是它声称要自动化的计件劳动。
- 作品内容: 一场现场游戏节目：参赛者比拼清洗数据、标注图像、给劳动场景分类，争相训练出最能识别“人类劳动”的图像识别模型。
- 实现方式: 表演形式模仿 Amazon Mechanical Turk 的“人类智能任务”，现场训练一个小型图像分类器。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 图片: https://www.maxdovey.com/assets/images/projects/hits/hit2.jpg
- 项目主页: https://www.maxdovey.com/HITS/

#### 照护技术（Technologies of Care） — Elisa Giardina Papa (2016)
- 类型: 电影与影像 · 机器: 聊天机器人与语言模型, 平台与推荐算法
- 核心想法: 网上很多“自动化”的照护与亲密，其实是外包到全球的人类劳动。
- 作品内容: 七段网络零工的影像肖像，其中有 ASMR 创作者、恋物视频制作者、客服接线员，以及被雇来扮演类似聊天机器人的“虚拟男友”的人。
- 实现方式: 艺术家通过零工平台找到这些工人并进行访谈，把他们的聊天与声音和屏幕图形结合；在 Rhizome 的线上栏目“The Download”中发布。
- 视角: 隐形劳动与攫取, 亲密、照护与陪伴
- 视频: https://vimeo.com/207163407
- 项目主页: http://rhizome.org/editorial/2016/oct/04/the-download-technologies-of-care/

#### A.A.I. — Agnieszka Kurant (2014)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 集体的、无偿的、非人类的劳动生产了“艺术”，正如隐藏的人群生产了“AI”。
- 作品内容: 由白蚁群用艺术家提供的彩色沙粒、金粉和晶体筑成的雕塑；标题意为“人工的人工智能”，正是亚马逊给 Mechanical Turk 的口号。
- 实现方式: 实验室中的白蚁群用提供的材料工作数月；完成的蚁丘作为雕塑展出。
- 视角: 隐形劳动与攫取, 能动、自主与共创, 机器环世界
- 视频: https://www.youtube.com/watch?v=8N-3p8OMMwQ
- 项目主页: https://en.wikipedia.org/wiki/Agnieszka_Kurant

#### 社交众包工（Social Turkers） — Lauren Lee McCarthy (2013)
- 类型: 表演、舞蹈与音乐 · 机器: 平台与推荐算法, 监控与生物识别
- 核心想法: 众包工人可以被雇来做亲密的决定；把约会外包，显示出这种逻辑能延伸到多远。
- 作品内容: 艺术家把自己的约会直播给匿名的 Mechanical Turk 工人，他们被付钱观看，并实时发短信告诉她该说什么、做什么。
- 实现方式: 手机把视频串流到工人可见的网页，工人的指令在约会过程中以短信形式传来。
- 视角: 隐形劳动与攫取, 亲密、照护与陪伴
- 视频: https://vimeo.com/66339316
- 图片: https://freight.cargo.site/t/original/i/476a1f0ec56e68a379716ffde32b20c370ad4f971631797206b90fb40ac382d4/3-socialturkers_pixelate.jpg
- 项目主页: https://lauren-mccarthy.com/Social-Turkers

#### 描述相机（Descriptive Camera） — Matt Richardson (2012)
- 类型: 研究原型 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 在计算机视觉能给图片配文之前，“机器之眼”常常是一个拿几美分报酬替机器看的人。
- 作品内容: 一台没有屏幕的相机，拍下的不是照片而是文字描述：按下快门几分钟后，热敏打印机吐出一句由亚马逊 Mechanical Turk 上匿名工人写的话。
- 实现方式: 基于 BeagleBone 的相机把照片上传到 Mechanical Turk，返回的描述由小票打印机打出（约 3–6 分钟，每张 1.25 美元）。
- 视角: 隐形劳动与攫取, 机器之眼
- 展出与获奖: Prix Ars Electronica 2013, Honorary Mention (Interactive Art)
- 视频: https://www.youtube.com/watch?v=8vkWb15Uudg
- 图片: https://archive.aec.at/asset/1674864/preview/ https://archive.aec.at/asset/1674866/preview/ https://archive.aec.at/asset/1674868/preview/
- 项目主页: https://archive.aec.at/prix/196286/

#### ScanOps — Andrew Norman Wilson (2012)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 基础设施、能源与供应链
- 核心想法: 自动化档案中的一个错误，是制作它的人唯一留下的痕迹。
- 作品内容: 谷歌图书书页的喷墨打印，画面里意外留下了扫描工人戴着橡胶指套的手或手指。
- 实现方式: 艺术家从谷歌图书中收集露出手部的扫描页，并大尺寸打印，这是一个持续进行的系列。
- 视角: 隐形劳动与攫取, 失败、故障与错误
- 图片: https://www.andrewnormanwilson.com/ScanOps_FantasiesOfTheLibrary.jpg https://www.andrewnormanwilson.com/scanops1.jpeg
- 项目主页: https://www.andrewnormanwilson.com/ScanOps.html

#### 谷歌三部曲之三：司机与摄像头（The Google Trilogy 3: The Driver and the Cameras） — Emilio Vavarella (2012)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 每一张自动生成的世界图像背后，都有一个系统试图抹去的劳动者。
- 作品内容: 艺术家在 Google 自家的街景全景图中找到街景车司机与摄像维护人员，他们被自动摄像头意外拍下，成为一组肖像。
- 实现方式: 从 Google 街景中挑选 360 度摄像头拍到自身操作员的截图，印制成肖像。
- 视角: 隐形劳动与攫取, 机器之眼
- 展出与获奖: The Photographers' Gallery, London
- 图片: https://emiliovavarella.com/wp-content/uploads/2018/12/2-Driver-and-the-cameras-photographers-gallery-london.jpg
- 项目主页: http://emiliovavarella.com/archive/google-trilogy/driver-and-cameras/

#### 工人离开谷歌总部（Workers Leaving the Googleplex） — Andrew Norman Wilson (2011)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 基础设施、能源与供应链
- 核心想法: 科技园区里工牌颜色的等级，揭示了谁的劳动注定要被隐藏。
- 作品内容: 一部影像散文，关于为谷歌图书扫描书籍的“ScanOps”工人：他们大多是有色人种，佩戴黄色工牌，不能享受其他谷歌员工的福利；Wilson 因拍摄他们而被解雇。
- 实现方式: Wilson 作为外包人员在山景城园区工作时拍下的画面，配以旁白和往来信件，呼应卢米埃尔兄弟的《工厂大门》（1895）。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=w0RTgOuoi2k
- 图片: https://www.andrewnormanwilson.com/workers1.jpeg
- 项目主页: https://www.andrewnormanwilson.com/WorkersGoogleplex.html

#### 一万美分（Ten Thousand Cents） — Aaron Koblin (2008)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法
- 核心想法: 一群看不见的工人可以一分一分地复制出他们得到的报酬。
- 作品内容: 一张 100 美元钞票的图像被切成一万个小块，每块由一位报酬一美分的 Mechanical Turk 工人绘制，整张钞票的劳动成本正好 100 美元。
- 实现方式: 与 Takashi Kawashima 合作：定制的绘图工具为每位工人分配一个小块，印刷品的销售所得捐给“每个孩子一台笔记本电脑”项目。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=VHbJGL8aL6o
- 项目主页: https://www.tenthousandcents.com/

#### Turkopticon — Lilly Irani, M. Six Silberman (2008)
- 类型: 研究原型 · 机器: 平台与推荐算法
- 核心想法: 平台把工人藏在雇主看不到的地方；一个小工具就能翻转视角，让工人反过来看清雇主。
- 作品内容: 一个浏览器插件和网站，让亚马逊 Mechanical Turk 工人评价发布任务的雇主，标记那些不公平拒收或报酬过低的人。
- 实现方式: Firefox 和 Chrome 插件在 Turk 界面的雇主名字旁显示工人评分；CHI 2013 论文把它的设计描述为一种行动主义。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 论文: https://doi.org/10.1145/2470654.2470742 (CHI 2013)
- 视频: https://www.youtube.com/watch?v=-xr4gXLdpB4
- 项目主页: https://turkopticon.info/

#### 羊市（The Sheep Market） — Aaron Koblin (2006)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 数据集与训练数据
- 核心想法: “人工的人工智能”背后是成千上万拿着几分钱的无名者；这群羊让他们变得可以被数清。
- 作品内容: Koblin 以每人两美分的价格，请一万名亚马逊 Mechanical Turk 工人“画一只朝左的羊”；这些画连同每一笔的回放被当作一群羊展示并出售。
- 实现方式: 作为 Mechanical Turk 任务发布的绘图工具记录下每位工人的笔画；画作被印成邮票，以 20 张一组出售。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=3Mmb5aSscck
- 图片: https://www.aaronkoblin.com/work/thesheepmarket/grid.jpg https://www.aaronkoblin.com/work/thesheepmarket/tool.jpg
- 项目主页: https://www.aaronkoblin.com/work/thesheepmarket/

### 自动化与劳动者的身体

工厂、仓库和平台中劳动者与机器的相遇。

#### 快递舞者之弧：0°接收者（Delivery Dancer's Arc: 0° Receiver） — 金雅瑛 (2024)
- 类型: 电影与影像 · 机器: 平台与推荐算法, 基础设施、能源与供应链
- 核心想法: 平台物流被延伸到时间：谁掌握时钟，谁就掌握劳动者。
- 作品内容: 续篇：骑手 Ernst Mo 与 En Storm 不再运送包裹，而是运送“时间”本身，在技术未来主义的首尔穿越相互冲突的历法系统与天文技术。
- 实现方式: 多频道影像，结合 CGI、游戏引擎世界与实拍；由墨尔本 ACMI 委托制作。
- 视角: 隐形劳动与攫取, 机器环世界
- 展出与获奖: ACMI, Melbourne 2024; Roppongi Art Night 2025
- 视频: https://www.youtube.com/watch?v=l3xPmmM297M
- 项目主页: https://roppongiartnight.com/2025/programs/568/

#### 快递舞者之域（Delivery Dancer's Sphere） — 金雅瑛 (2022)
- 类型: 电影与影像 · 机器: 平台与推荐算法
- 核心想法: 在平台派单之下，劳动者的身体像路线一样被优化；“优雅”成了算法用来形容更少动作的词。
- 作品内容: 约 25 分钟的影像：外卖平台“Delivery Dancer”的骑手 Ernst Mo 在由派单系统“Dancemaster”操控、不断循环生成的首尔中穿行，直到遇见她的分身 En Storm。
- 实现方式: 结合 CGI、游戏引擎场景与实拍，并为导航算法配音；创作于新冠疫情期间。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Syntax and Sorcery, Gallery Hyundai 2022; IFFR 2023; Prix Ars Electronica 2023, Golden Nica (New Animation Art); LG Guggenheim Award 2025
- 视频: https://www.youtube.com/watch?v=D1iKdxxj7AE
- 图片: https://www.ima.org.au/wp-content/uploads/2025/05/Ayoung-Kim_Delivery-Dancers-Sphere_2022_Stillcut_7-1100x611.jpg
- 项目主页: https://www.ima.org.au/exhibitions/ayoung-kim-delivery-dancers-sphere/

#### 外卖骑手，困在系统里（Delivery Riders, Trapped in the System） — 《人物》杂志 (2020)
- 类型: 书与文章 · 机器: 平台与推荐算法
- 核心想法: 从骑手最快一次配送中学习的算法，把他们多付出的努力变成下一个时限。
- 作品内容: 赖祐萱为《人物》杂志撰写的长篇调查，揭示美团、饿了么的派单算法如何逐年压缩送餐时间，迫使骑手超速、逆行。
- 实现方式: 对骑手、工程师与研究者进行了数月采访，追踪预计送达时间如何被计算与压缩。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 论文: https://chuangcn.org/2020/11/delivery-renwu-translation/ (Renwu (人物), 8 September 2020)
- 视频: https://www.youtube.com/watch?v=KE1EoDiBARM
- 项目主页: https://chuangcn.org/2020/11/delivery-renwu-translation/

#### 亚马逊工人笼专利图变作虚拟金岛棕刺嘴莺笼（Amazon worker cage patent drawing as virtual King Island Brown Thornbill cage） — Simon Denny (2019)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 工业机械臂, 自动驾驶与无人机
- 核心想法: 自动化用笼子关住工人来“保护”机器；濒危的鸟又把这只笼子与科技所消耗的矿山和栖息地连在一起。
- 作品内容: 按亚马逊 2016 年一项专利制作的等大笼子雕塑：专利中，仓库工人会站在笼中随机器人小车移动；笼子里还有一只通过增强现实出现的金岛棕刺嘴莺，一种濒危鸟类。
- 实现方式: 依据专利图纸制作的钢结构，配以增强现实应用；在塔斯马尼亚 MONA 的 Denny 个展“Mine”中展出，该展把科技专利与采矿并置。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Mine, MONA, Hobart 2019
- 视频: https://www.youtube.com/watch?v=RfXIGGuyKdE
- 项目主页: https://simondenny.net/

#### 劳动（Labor） — Paul Vanouse (2019)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 当生产从人和机器的劳动转向微生物，劳动只留下一股气味。
- 作品内容: 三个玻璃生物反应器培养产生人体汗味的皮肤细菌；气味渗入一件白色 T 恤，让房间里充满劳作的气味，却没有一个劳动者。
- 实现方式: 自我调节的生物反应器以糖和脂肪培养表皮葡萄球菌、干燥棒状杆菌和贪婪丙酸杆菌，配有传感器与泵；获林茨电子艺术节“人工生命与智能”金尼卡奖。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2020, Golden Nica
- 视频: https://vimeo.com/372389451
- 图片: https://www.paulvanouse.com/labor-install-BN-1.jpg https://www.paulvanouse.com/labor-reactor-1.jpg
- 项目主页: https://www.paulvanouse.com/labor.html

#### 亚洲一号（Asia One） — 曹斐 (2018)
- 类型: 电影与影像 · 机器: 机器生物与移动机器人, 基础设施、能源与供应链
- 核心想法: 在由机器运转的仓库里，人的亲密关系也成了系统调度的对象。
- 作品内容: 在京东高度自动化的物流中心里，两名仅存的人类工人在分拣机、无人机与自动小车之间相爱。
- 实现方式: 在京东位于昆山的自动化“亚洲一号”物流中心实地拍摄，真实的分拣机器人与传送系统就是布景。
- 视角: 隐形劳动与攫取, 亲密、照护与陪伴
- 展出与获奖: Guggenheim Museum, One Hand Clapping 2018; M+ Cinema, Techno Sapiens
- 视频: https://www.youtube.com/watch?v=DQqzFsgnAMo
- 图片: https://www.mplus.org.hk/api/images/4533/width-1200|format-jpeg/
- 项目主页: https://www.mplus.org.hk/en/cinema/techno-sapiens/asia-one/

#### 以至无穷（Ad Infinitum） — Pedro Lopes (2016)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 控制论与人工生命系统
- 核心想法: 角色倒转：在这里，机器是使用者，人是资源。
- 作品内容: 一台“寄生”机器用手铐扣住观众的手臂，电刺激其肌肉，让人摇动曲柄为它供能；唯一的脱身办法是说服另一位观众来替你。
- 实现方式: 与 Robert Kovacs 合作：肌肉电刺激驱动观众前臂转动发电机，只有在另一侧工位检测到第二只手臂时手铐才会松开。
- 视角: 隐形劳动与攫取, 具身与动觉, 能动、自主与共创
- 展出与获奖: VIDA 16.0, Incentive for Production (as 'Parasite', 2014); Science Gallery Dublin, Humans Need Not Apply (2017); Ars Electronica 2017
- 视频: https://www.youtube.com/watch?v=UsL48gkh3GI
- 图片: https://a-parasite.org/parasite_files/Ad-Infinitum-a-human-getting-trapped-in-the-cuffs-Arthur-Sil.jpg https://a-parasite.org/parasite_files/MG_9829.jpg
- 项目主页: https://a-parasite.org/

#### HellYeahWeFuckDie — 黑特·史德耶尔 (2016)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 机器人通过被虐待来学会保持平衡；这些画面把未来劳动者的身体呈现为试验品。
- 作品内容: 一件影像装置：人形机器人和机器人“骡子”在稳定性测试中被踢、被推、被弄倒；周围是用 2010 年代英语歌名中最常见的五个词做成的雕塑。
- 实现方式: 对机器人实验室测试录像的再剪辑，结合电脑动画与配乐；于 2017 年明斯特雕塑展中装置在一座银行大楼的中庭里。
- 视角: 具身与动觉, 隐形劳动与攫取, 失败、故障与错误
- 展出与获奖: Skulptur Projekte Münster 2017
- 视频: https://www.youtube.com/watch?v=sWw7CPczmU0
- 项目主页: https://www.skulptur-projekte-archiv.de/en-us/2017/projects/186/

#### 太阳工厂（Factory of the Sun） — 黑特·史德耶尔 (2015)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 在数字资本主义中，身体的动作被当作数据与能量收割。
- 作品内容: 一件像电子游戏的影像装置：动作捕捉工作室里的工人被迫不停跳舞，直到他们的动作变成人造阳光；展厅本身布置成动作捕捉棚的网格。
- 实现方式: 单屏影像混合动作捕捉画面、游戏图形与新闻式片段，在蓝色网格空间中配躺椅展出；首展于威尼斯双年展德国馆。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Venice Biennale 2015 (German Pavilion); MOCA Los Angeles 2016
- 视频: https://www.youtube.com/watch?v=ptNczdY-qvo
- 项目主页: https://www.moca.org/exhibition/hito-steyerl-factory-of-the-sun

#### 人类过时研究所（Institute of Human Obsolescence） — Manuel Beltrán (2015)
- 类型: 思辨设计 · 机器: 基础设施、能源与供应链, 义体与赛博格
- 核心想法: 如果机器接管了体力和脑力劳动，人类剩下的工作也许只是当电池或数据源。
- 作品内容: 一个为“被机器淘汰的人类”做准备的思辨机构：它的工人穿着采集体温的服装一动不动地躺着，体温发电驱动挖加密货币的电脑，他们“生产”的价值被逐一记录。
- 实现方式: 温差发电服把多余体温转成电，驱动一台挖加密货币的小电脑；另一条线索把数据生产视作无偿劳动。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2018, Honorary Mention (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=ZocIhWz8EAI
- 图片: https://archive.aec.at/asset/2514709/preview/ https://archive.aec.at/asset/2514711/preview/ https://archive.aec.at/asset/2514714/preview/
- 项目主页: http://speculative.capital

#### 睡眠经销商（Sleep Dealer） — Alex Rivera (2008)
- 类型: 电影与影像 · 机器: 工业机械臂, 义体与赛博格, 自动驾驶与无人机
- 核心想法: 边境可以放行劳动、却挡住劳动者；远程操控是一种没有移民的移民。
- 作品内容: 一部科幻长片，设定在关闭的美墨边境：墨西哥工人用身上的接口接入网络，远程操控在美国建造摩天大楼的机器人，而无人机则在守卫水源。
- 实现方式: 在墨西哥拍摄的长片；首映于圣丹斯电影节，获得表彰科技题材的阿尔弗雷德·斯隆奖。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Sundance Film Festival 2008 (Alfred P. Sloan Prize)
- 视频: https://www.youtube.com/watch?v=fTZv6oxa2KI
- 图片: https://dr56wvhu2c8zo.cloudfront.net/sleepdealer/assets/a88a594b-804c-4ee3-affa-62d65ac839ec/construction+bots.jpg
- 项目主页: https://www.sleepdealer.com/

#### 乞丐机器人（Beggar Robot） — Sašo Sedlaček (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 社交与陪伴机器人
- 核心想法: 人们给乞讨的机器钱，比给乞讨的人更爽快：自动化甚至能让贫困变得“好看”。
- 作品内容: 一台用回收电脑零件做成的小机器人站在提款机和商店门口，用礼貌的电子声向路人乞讨，伸出小手，并向捐助者道谢。
- 实现方式: 运行 Linux 的回收电脑硬件驱动面部显示、语音和由光驱机构控制开合的双手；开源 DIY 说明让任何人都可以复制它。
- 视角: 隐形劳动与攫取, 他异与恐怖谷
- 展出与获奖: VIDA 11.0, Special Mention (2008); Taipei Fine Arts Museum 2008
- 视频: https://www.youtube.com/watch?v=kkstnT0iIA0
- 图片: https://live.staticflickr.com/7379/12726364163_d5b5bf0162_b.jpg https://live.staticflickr.com/7442/12727484193_7faef8d7cf_b.jpg
- 项目主页: https://sasosedlacek.com/beggar-robot/

#### 谁的乌托邦（Whose Utopia） — 曹斐 (2006)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 工厂机器设定了工人身体的节奏，而影片把几分钟时间还给了这些身体。
- 作品内容: 影片拍摄于佛山欧司朗灯泡厂的驻留期间，从装配线转向工人们在机器之间演出自己的梦想：芭蕾、吉他与舞蹈。
- 实现方式: 曹斐与欧司朗员工合作六个月，先拍摄生产线，再在车间里拍摄工人自选的表演。
- 视角: 隐形劳动与攫取, 具身与动觉
- 视频: https://www.youtube.com/watch?v=tSvNpFE8uPs
- 项目主页: https://www.mplus.org.hk/en/cinema/techno-sapiens/asia-one/

### 解剖与星球物质

描绘 AI 所依赖的矿山、数据中心、线缆与能源。

#### 为一个念头而痛（to hurt for a thought） — Julia Vollmer (2025)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 生成模型与潜空间
- 核心想法: AI 的能源代价变成指尖上的感觉，就在我们向它提出要求的地方。
- 作品内容: 观众在一块沉重的金属键盘上为图像生成器输入提示词；键盘通过铜层连接到正在计算的显卡，每次请求都会让它变得更烫。
- 实现方式: 键帽下的铜层与运行图像生成模型的 GTX 1660 Ti 显卡散热器导热连接，热量因此传到键盘上。
- 视角: 隐形劳动与攫取, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2026, Honorary Mention (Interactive Art +)
- 图片: https://archive.aec.at/asset/3898654/preview/ https://archive.aec.at/asset/3898653/preview/
- 项目主页: https://juliavollmer.de/projects/to-hurt-for-a-thought/

#### 计算帝国：1500 年以来的技术与权力谱系（Calculating Empires: A Genealogy of Technology and Power since 1500） — Kate Crawford, Vladan Joler (2023)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 数据集与训练数据, 监控与生物识别
- 核心想法: 今天的 AI 继承了古老的帝国结构；把它放进 500 年的时间线，打破了“横空出世”的叙事。
- 作品内容: 一幅 24 米长的视觉谱系图，把五个世纪以来的通信、计算、分类和控制技术并列呈现，一直延伸到当下的 AI。
- 实现方式: 手绘研究地图与大型空间装置，首展于米兰普拉达基金会 Osservatorio；获 2024 年 S+T+ARTS 大奖。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 展出与获奖: Fondazione Prada Osservatorio, Milan 2023; S+T+ARTS Prize 2024 Grand Prize
- 视频: https://www.youtube.com/watch?v=DYS8b9J7Fto
- 图片: https://calculatingempires.net/content/calculating-empires-og.png
- 项目主页: https://calculatingempires.net/

#### 我们皮肤里的这些网络（These Networks In Our Skin） — Mimi Ọnụọha (2023)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 电缆埋在土地里，因此也属于土地的宇宙观；修补可以取代攫取。
- 作品内容: 一部短片：四位不露面孔的女性重新布线网络电缆，把头发、香料和尘土填入其中；灵感来自伊博族为大地女神阿拉制作艺术的传统。
- 实现方式: 单屏循环影像（5 分 48 秒），通常与装置《The Cloth In The Cable》一同展出：75 英尺长、缠有头发、布料和泥土的电缆。
- 视角: 隐形劳动与攫取, 机器环世界
- 图片: https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/d584cb19-ac49-4d5d-abbf-538298ac4bf9/02_TNIOS_videostill_courtesyoftheartist.png https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/ef67d256-5d9b-4d55-aa6a-1eca116a782d/01_TNIOS%2BCITC_courtesyofGropiusBau.jpg
- 项目主页: https://www.mimionuoha.com/

#### 抽象神谕矿机（Abstract Oracle Miner） — 郭城 (2022)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 每一个虚拟产出都以硬件的热量与能耗为代价，就像献给神谕的供品。
- 作品内容: 观众扫描二维码后，手机处理器渲染三维场景并生成一条随机“神谕”；手机在运算中发热、变慢，装置中的铜磬随之作响。
- 实现方式: 网站读取手机硬件性能并渲染高负载场景；树莓派与电磁铁敲击铜磬。
- 视角: 隐形劳动与攫取, 机器环世界
- 展出与获奖: Commissioned by UCCA Center for Contemporary Art 2022
- 图片: https://cdn.guo-cheng.net/files/projectImg/AbstractOracleMiner/Abstract_Oracle_Miner_3.jpg https://cdn.guo-cheng.net/files/projectImg/AbstractOracleMiner/Abstract_Oracle_Miner_1.jpg
- 项目主页: https://guo-cheng.net/index.php/works/abstract-oracle-miner/

#### Carbolytics — Joana Moll (2022)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 基础设施、能源与供应链
- 核心想法: 监控式广告有气候代价；追踪在燃烧碳。
- 作品内容: 一件装置和数据库，估算全球访问量前一百万个网站所加载的追踪 Cookie 的碳排放。
- 实现方式: 与巴塞罗那超级计算中心合作，爬取网站并统计第三方 Cookie；由卢布尔雅那 Aksioma 委托。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 展出与获奖: Aksioma, Ljubljana 2022
- 图片: https://www.janavirgin.com/img/works/carbolytics.jpg
- 项目主页: https://carbolytics.org/

#### 批判性气候机器（Critical Climate Machine） — Gaëtan Robillard (2022)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 基础设施、能源与供应链
- 核心想法: 一台对抗气候谣言的机器同时也在给房间加温：作品把计算与它的热量放在同一个画面里。
- 作品内容: 一件数据雕塑运行语言模型，识别并驳斥推文中的气候变化谣言，同时一张热成像图显示装置自身散发的热量；周围，录下的谣言与反驳之声由一个生成式声音模型重新在空间中排布。
- 实现方式: 一个自然语言处理分类器（由 John Cook、Travis Coan、Constantine Boussalis 与 Mirjam Nanko 开发）为推特上的气候怀疑论点贴标签；热像仪记录雕塑的热量；以卡牌游戏《驳斥游戏》工作坊录下的对话由一个机器学习即兴模型重新混编。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 展出与获奖: Lumen Prize 2023, BCS Futures Award; Ircam, Centre Pompidou 2022; S+T+ARTS Prize 2023, Nomination
- 视频: https://www.youtube.com/watch?v=KBaGSQWKr8w
- 图片: https://images.squarespace-cdn.com/content/v1/65e7176a61627736e02f6c4a/1710514280894-WEATKDQPMQG6BA3TPK14/Critical%2BClimate%2Bby%2BMachine%2BGae%CC%88tan%2BRobillard+%286%29.jpeg
- 项目主页: https://lumenprize.org/2023-winners/2023-bcs-futures-award-winner

#### 太阳能协议（Solar Protocol） — Tega Brain (2021)
- 类型: 研究原型 · 机器: 基础设施、能源与供应链
- 核心想法: 让太阳而不是参与度指标来决定网络如何运行。
- 作品内容: 一个托管在全球小型太阳能服务器网络上的网站平台；每位访客都会被引导到当下阳光最充足的那台服务器。
- 实现方式: 与 Alex Nathanson 和 Benedetta Piantella 合作：由志愿者运营、配备太阳能板和电池的树莓派服务器，共享一套感知能源的路由协议。
- 视角: 机器环世界, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=mMYzM4_MZI4
- 图片: https://freight.cargo.site/t/original/i/d262f69efa5d13bc78dbc4a2eb1c351792a4dd175524e0e3aa3d26c96f5a1cd1/Solar-Protocol-2021-NetworkVisualization.jpg
- 项目主页: https://solarprotocol.net/

#### 洁净室悖论（The Cleanroom Paradox） — Felix Lenz, Angela Neubauer, Eszter Zwickl (2021)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 制造我们设备的一尘不染的洁净室，掩盖了在其中工作的人所承受的有毒暴露。
- 作品内容: 一幅 Jin 的肖像——她曾是三星芯片厂工人，后患上肾癌——用溶解手机制成的墨水印出并慢慢瓦解，同时一段影像把她的讲述与专家的访谈交织在一起。
- 实现方式: 手机被化学溶解、中和并浓缩成具有腐蚀性的黑色墨水，用来打印 Jin 的照片（用 Galaxy Note 8 拍摄）；纪录影像记录了制作过程与访谈。
- 视角: 隐形劳动与攫取
- 展出与获奖: Prix Ars Electronica 2021, Honorary Mention (Artificial Intelligence & Life Art)
- 图片: https://archive.aec.at/asset/2983882/preview/ https://archive.aec.at/asset/2983885/preview/
- 项目主页: https://archive.aec.at/prix/255179/

#### 新攫取主义（New Extractivism） — Vladan Joler (2020)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 基础设施、能源与供应链, 数据集与训练数据
- 核心想法: 平台资本主义攫取的不只是矿物，还有注意力、行为与时间。
- 作品内容: 由地图和影像组成的互动装置：一个人物在一张庞大的数字经济图解中穿行——平台、数据、劳动、能源，以及注意力的“牢笼”。
- 实现方式: 一张可浏览的网页图解，以及一段由艺术家旁白的 17 分钟动画影像。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=JkUi3e7GVXs
- 图片: https://extractivism.online/Soc-media-fb.png
- 项目主页: https://extractivism.online/

#### 乌托邦式开采（Utopian Extraction） — unmake lab (2020)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉, 自动驾驶与无人机
- 核心想法: 机器视觉的分类把自然压扁为同一种通用、可施工的东西。
- 作品内容: 以无人机与卫星影像呈现韩国“制造自然”的建设工地，并配以一场表演：目标识别不断给一位裹着斑马纹布料的表演者重新贴标签。
- 实现方式: 卫星影像、无人机画面与实时目标识别应用，以讲座表演形式呈现。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Coreana Museum of Art C*-lab, Seoul 2020
- 视频: https://www.youtube.com/watch?v=RSRjDoCALKM
- 项目主页: https://www.youtube.com/watch?v=RSRjDoCALKM

#### 分崩离析（Asunder） — Tega Brain, Julian Oliver (2019)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 生成模型与潜空间
- 核心想法: 把地球交给优化器，暴露出把自然当作可解系统的荒诞与暴力。
- 作品内容: 一个“负责任的环境管理者”：用超级计算机为真实地点提出改造方案，从改道河流到拆除城市，以求守住地球边界。
- 实现方式: 与 Julian Oliver、Bengt Sjölén 合作：气候与卫星数据、气候模型与生成图像在装置内的超级计算机上运行。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: transmediale 2020
- 视频: https://www.youtube.com/watch?v=emzSsmAIw6E
- 图片: https://freight.cargo.site/t/original/i/835c9c2bdc2cd1da05e6ecb94d7044429d0a1b75bbadc823cca41319417a7e27/ASUNDER_LIUC_Transmediale2020_0155.jpg
- 项目主页: https://tegabrain.com/Asunder

#### 一位亚马逊用户的隐秘生活（The Hidden Life of an Amazon User） — Joana Moll (2019)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 基础设施、能源与供应链, 数据集与训练数据
- 核心想法: 一次购买会触发大量看不见的追踪代码，买家要用能源和注意力为它买单。
- 作品内容: 艺术家在亚马逊买了一本书，并记录下购买过程中网站加载的所有代码：近 8700 页 JavaScript、87 MB 数据，被打印成一本书。
- 实现方式: 在购买杰夫·贝索斯最喜欢的一本书的过程中抓取浏览器流量，并以网站、打印书册和影像呈现。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=2iiAHyhLH-Y
- 图片: https://www.janavirgin.com/img/works/hidden_life_2.jpg
- 项目主页: https://www.janavirgin.com/works.html

#### 人工智能系统剖析（Anatomy of an AI System） — Kate Crawford, Vladan Joler (2018)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 语音与听觉机器, 数据集与训练数据
- 核心想法: 厨房台面上的小小设备，处在一条星球级的攫取、劳动与数据链条的末端。
- 作品内容: 一张大型地图和一篇长文，追踪向亚马逊 Echo 说出一句指令所需的一切：锂和稀土的开采、组装与数据劳动、云端，以及设备最终成为电子垃圾。
- 实现方式: 由 Joler 依据供应链、企业与劳动资料绘制的研究型图解；被纽约现代艺术博物馆和维多利亚与艾伯特博物馆收藏，并获 2019 年 Beazley 年度设计奖（数字类）。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 展出与获奖: Beazley Designs of the Year 2019; MoMA collection; V&A collection
- 视频: https://www.youtube.com/watch?v=wRt5H1Pi-BY
- 图片: http://www.anatomyof.ai/ai-system-facebook-og.jpg
- 项目主页: https://anatomyof.ai/

#### 比特币矿和少数民族田野录音（Bitcoin Mining and Field Recordings of Ethnic Minorities） — 刘窗 (2018)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 同样的河流为矿机供电，也承载着正在消失的声音：计算有它自己的地貌。
- 作品内容: 一部三段式影像散文，在中国西南以水电供能的比特币矿场、当地少数民族的歌声与语言，以及数据与录音的历史之间来回切换。
- 实现方式: 矿场纪实影像与田野录音，结合档案素材剪辑成单频影像。
- 视角: 隐形劳动与攫取, 机器之耳与声
- 展出与获奖: Tate collection; Science Gallery Melbourne
- 视频: https://www.youtube.com/watch?v=DgA-rP0CjW0
- 项目主页: https://www.tate.org.uk/art/artworks/chuang-bitcoin-mining-and-field-recordings-of-ethnic-minorities-t15975

#### Geocinema — Geocinema (2018)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链, 计算机视觉
- 核心想法: 地球如今被机器持续拍摄，谁拥有传感器，谁就书写地球的故事。
- 作品内容: 一个研究与影像项目，把卫星、监控、手机摄像头与街景车视为一台“行星摄像机”，沿中国“一带一路”沿线追踪感知基础设施。
- 实现方式: 散文影片，结合红外无人机画面、卫星影像与街景截图。
- 视角: 机器之眼, 隐形劳动与攫取
- 图片: https://geocinema.network/_next/image/?url=https%3A%2F%2Fgeocinema.network%2Fuploads%2Fbanner2_3a749bd8f2.png&w=3840&q=50
- 项目主页: https://geocinema.network/

#### 深海潮汐（Deep Down Tidal） — Tabita Rezaire (2017)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 互联网的物理线路重复着殖民航线；连接本身携带着旧的权力。
- 作品内容: 一部影像散文，追踪海底互联网光缆，它们沿着跨大西洋奴隶贸易和殖民航运的航线铺设；片中穿插关于水的宇宙观。
- 实现方式: 以桌面界面风格拼贴地图、档案图像、动画和艺术家旁白（约 18 分钟）。
- 视角: 隐形劳动与攫取, 机器环世界
- 视频: https://www.youtube.com/watch?v=V9EIywuH-LM
- 图片: https://goodman-gallery.com/api/v1/og-image?src=https%3A%2F%2Fd32637ifygiesu.cloudfront.net%2Fartists%2Ftabita-rezaire%2Fdeep-down-tidal-118702%2Ftabita-rezaire-deep-down-tidal-118702-39813-front-1.jpg
- 项目主页: https://goodman-gallery.com/artists/tabita-rezaire/deep-down-tidal-118702

#### Facebook 算法工厂（Facebook Algorithmic Factory） — Vladan Joler (2016)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 数据集与训练数据, 基础设施、能源与供应链
- 核心想法: 用户是一座工厂里的无偿工人，而这座工厂的机器是算法。
- 作品内容: SHARE 实验室的一组取证式地图，追踪 Facebook 如何把用户活动当作原材料收集，并通过算法把它加工成广告投放目标。
- 实现方式: Joler 与 Andrej Petrovski 依据公开文件，把专利、权限与追踪整理成大型图解，分三部分发布。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 图片: https://labs.rs/wp-content/uploads/2016/08/FacebookFactory-small.gif https://labs.rs/wp-content/uploads/2016/08/FB-Research-Final-01.png
- 项目主页: https://labs.rs/en/facebook-algorithmic-factory-immaterial-labour-and-data-harvesting/

#### 变质作用（Metamorphism） — Julian Charrière (2016)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 电脑重新变回岩石：所谓“非物质”的数字，其实是向地球借来的地质之躯。
- 作品内容: 把笔记本电脑和手机里的主板、硬盘、CPU 和内存在人造熔岩中熔化成多彩的石头，放在展柜里，如同未来自然史博物馆的标本。
- 实现方式: 把电子废料部件与岩石混合，在熔岩温度的炉中熔融，再切割展示。
- 视角: 隐形劳动与攫取, 机器环世界
- 展出与获奖: Into the Hollow, Dittrich & Schlechtriem, Berlin 2016; The World Through AI, Jeu de Paume, Paris 2025
- 图片: https://julian-charriere.net/media/pages/projects/metamorphism/f1cc18f486-1671025283/julian-charriere-metamorphism-xvii-into-the-hollow-dittrich-schlechtriem-2016-copyright-the-artist-vg-bild-kunst-bonn-germany-1600x.jpg https://julian-charriere.net/media/pages/projects/metamorphism/86b5e1f22d-1671025283/julian-charriere-metamorphism-xiv-installation-view-into-the-hollow-dittrich-schlechtriem-2016-copyright-the-artist-vg-bild-kuns-1600x.jpg
- 项目主页: https://julian-charriere.net/projects/metamorphism

#### 稀土陶器（Rare Earthenware） — Unknown Fields Division (2015)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 屏幕的光亮始于世界另一端的放射性废料。
- 作品内容: 三只陶瓷花瓶，形状分别按智能手机、笔记本电脑和汽车电池中所用稀土元素的比例设计，材料是内蒙古包头尾矿湖的有毒泥浆。
- 实现方式: 工作室沿供应链从中国港口追溯到包头的冶炼厂，采集废泥并烧制成明式花瓶；Toby Smith 拍摄的影片记录了这段旅程。
- 视角: 隐形劳动与攫取
- 展出与获奖: V&A, London
- 视频: https://www.youtube.com/watch?v=YMKJ7S7fKOk
- 项目主页: http://www.unknownfieldsdivision.com/

#### CO2GLE — Joana Moll (2014)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 每次搜索都有物理代价；“云”在燃烧燃料。
- 作品内容: 一个网页，实时显示自你打开它以来，全球访问 google.com 的流量所排放的二氧化碳公斤数。
- 实现方式: 根据谷歌每秒流量、平均页面大小以及数据传输的能耗强度进行估算，并实时更新。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 图片: https://www.janavirgin.com/img/works/CO2GLE.jpg
- 项目主页: https://www.janavirgin.com/CO2/

#### 互联网机器（Internet Machine） — Timo Arnall (2014)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链
- 核心想法: 云是一座满是轰鸣机器、柴油发电机和保安的建筑。
- 作品内容: 一部多屏影像，拍摄于欧洲最大的数据中心之一——西班牙电信位于阿尔卡拉-德埃纳雷斯的数据中心，呈现“云”背后的冷却、电力与安保机器。
- 实现方式: 缓慢的移动镜头和宽幅摄影，投射在三块屏幕上；曾在 transmediale 展出。
- 视角: 机器环世界, 不透明与潜空间
- 展出与获奖: transmediale
- 视频: https://vimeo.com/95044197
- 图片: https://www.elasticspace.com/images/internet-machine/Internet-Machine-Transmediale-2-small-1024x683.jpg https://www.elasticspace.com/images/internet-machine/InternetMachine14-web.jpg
- 项目主页: https://www.elasticspace.com/2014/05/internet-machine/

#### 荒潮（Waste Tide） — 陈楸帆 (2013)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 义体与赛博格
- 核心想法: 我们电子设备的“来世”，是别人的身体与土地。
- 作品内容: 小说发生在华南“硅屿”，外来“垃圾人”在此拆解全球电子垃圾；年轻女工小米被病毒感染，成为后人类赛博格。
- 实现方式: 以现实中的贵屿电子垃圾镇为原型的科幻小说；刘宇昆英译本 2019 年出版。
- 视角: 隐形劳动与攫取, 具身与动觉
- 论文: https://en.wikipedia.org/wiki/Waste_Tide (Changjiang Literature and Art Publishing House, 2013; Tor Books (English), 2019)
- 图片: https://upload.wikimedia.org/wikipedia/en/c/c0/The_Waste_Tide.jpg
- 项目主页: https://en.wikipedia.org/wiki/Waste_Tide

### 军事与操作性 AI

无人机、目标识别，以及为战争而看与行动的机器。

#### AI 战争云数据库（AI War Cloud Database） — Sarah Ciston (2025)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据, 平台与推荐算法, 自动驾驶与无人机
- 核心想法: 你口袋里的 AI 和挑选打击目标的 AI 共享公司、模型和数据；家与战场之间的边界很薄。
- 作品内容: 一个互动数据库和装置，收录战争中用于辅助决策的 AI 系统，并标示出同类工具在智能手机和社交平台中出现的位置。
- 实现方式: 依据公开资料汇编的公司、产品与军事用途网络图，另有可触摸的装置版本；获 2025 年 S+T+ARTS 大奖。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: S+T+ARTS Prize 2025 Grand Prize; Ars Electronica 2025
- 视频: https://www.youtube.com/watch?v=BM1K0Rbs4W0
- 图片: https://ars.electronica.art/starts-prize/files/2025/05/aiwarcloud-6-c-sarahciston-1024x576.jpg
- 项目主页: https://aiwar.cloud

#### 伊洛瓦伊斯克战役（The Battle of Ilovaisk） — Forensic Architecture (2019)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 反取证用机器视觉去看见国家所否认的东西。
- 作品内容: 对 2014 年乌克兰东部俄罗斯军队存在的调查：一个训练来识别 T-72 坦克的机器学习分类器在数千段网络视频中搜寻证据。
- 实现方式: 用坦克型号的合成三维渲染训练分类器，应用于抓取的 YouTube 视频，结果经研究人员核实。
- 视角: 机器之眼, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=OldnzVNE71E
- 项目主页: https://forensic-architecture.org/investigation/the-battle-of-ilovaisk

#### 来袭（Incoming） — Richard Mosse (2017)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 武器级相机把人看成热信号：没有面孔、被剥去个性的身体。
- 作品内容: 一部三屏影片，记录穿越地中海的难民及其营地生活；使用可在 30 公里外探测人体的军用热成像相机拍摄，人被呈现为发光的热量。
- 实现方式: 用出口管制中被列为武器的远距离热成像相机拍摄两年；配乐 Ben Frost。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: The Curve, Barbican 2017; NGV Triennial 2017
- 视频: https://www.youtube.com/watch?v=6QOyFAqs_rM
- 项目主页: https://www.richardmosse.com/

#### 杀戮机器人（Slaughterbots） — Future of Life Institute / Stop Autonomous Weapons (2017)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 监控与生物识别, 计算机视觉
- 核心想法: 自主武器不需要科幻式的飞跃，只需组合现有部件；影片以此主张禁令。
- 作品内容: 一部虚构短片：掌心大小、装有人脸识别和炸药的无人机成群放出，根据社交媒体资料选定并刺杀学生和政客。
- 实现方式: 由 Stewart Sugg 执导，片尾有 AI 研究者 Stuart Russell 的陈述；首映于日内瓦联合国《特定常规武器公约》会议。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=9CO6M2HsoIA
- 项目主页: https://futureoflife.org/

#### 21 世纪无人机声学研究（A Study into 21st Century Drone Acoustics） — Ruben Pater, Gonçalo F. Cardoso (2016)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机
- 核心想法: 对生活在无人机之下的人来说，机器首先是一种声音；听它，既是一种认知，也是一种恐惧。
- 作品内容: 一部视听作品和唱片，用 17 种无人机的田野录音构成，从消费级四旋翼到军用无人机，追溯一架无人机在声音上的“生与死”，以及它的嗡鸣在遭受无人机打击的地区造成的恐惧。
- 实现方式: 把无人机电机与螺旋桨的田野录音剪辑成作品，并配以标识每种无人机的视觉谱。
- 视角: 机器之耳与声, 他异与恐怖谷
- 展出与获奖: Prix Ars Electronica 2017, Award of Distinction (Hybrid Art); ZKM Global Control and Censorship 2015–16
- 视频: https://www.youtube.com/watch?v=_69goMEmumk
- 图片: https://archive.aec.at/asset/2230549/preview/ https://archive.aec.at/asset/2230551/preview/ https://archive.aec.at/asset/2230552/preview/
- 项目主页: https://archive.aec.at/prix/228089/

#### 国鸟（National Bird） — Sonia Kennebeck (2016)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 远程杀戮是在屏幕前完成的劳动，也会伤害执行它的人。
- 作品内容: 一部纪录片，跟随三位美国无人机项目的前成员（包括一名图像分析员），他们打破沉默，讲述自己的工作以及它造成的平民死亡。
- 实现方式: 观察式纪录片结合访谈，包括探访阿富汗一次空袭的幸存者；Wim Wenders 与 Errol Morris 任监制。
- 视角: 隐形劳动与攫取, 机器之眼
- 展出与获奖: Berlinale 2016; Tribeca Film Festival 2016
- 视频: https://vimeo.com/186277306
- 图片: https://nationalbirdfilm.com/wp-content/uploads/2016/04/poster_shot2.jpg
- 项目主页: https://nationalbirdfilm.com/

#### #NotABugSplat — #NotABugSplat collective (2014)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: “虫子溅痕”是操作员对被炸死者的俚语；这幅肖像通过无人机自己的“眼睛”回话。
- 作品内容: 一幅在无人机空袭中失去亲人的孩子的巨幅肖像，铺在巴基斯坦开伯尔-普赫图赫瓦省的田野上，大到足以被上空的无人机镜头看见。
- 实现方式: 在当地居民帮助下铺在地面的乙烯基印刷画，受艺术家 JR 的“Inside Out”项目启发，并以航拍记录。
- 视角: 机器之眼, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=ts5qn6UV5wE
- 图片: https://notabugsplat.com/wp-content/uploads/2014/04/jr_kpk_full.jpg
- 项目主页: https://notabugsplat.com/

#### 蓝天日（Blue Sky Days） — Tomas van Houtryve (2014)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 从无人机的角度看自己的日常生活，远程战争的凝视就变得可以辨认。
- 作品内容: 用小型航拍无人机在美国拍摄的婚礼、葬礼、学校和祈祷集会照片，呼应美国无人机在海外空袭过的那类聚会。
- 实现方式: 用消费级四旋翼无人机在美国城镇上空拍摄；标题呼应巴基斯坦男孩 Zubair Rehman 2013 年在美国国会的证词：他现在更喜欢灰色的天空，因为那时无人机不会起飞。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: ICP Infinity Award 2015 (Photojournalism)
- 视频: https://vimeo.com/128202299
- 图片: https://i2.wp.com/tomasvh.com/wp-content/uploads/2013/03/works_prev_blue_sky_days.jpg?fit=1500%2C1500&ssl=1
- 项目主页: https://tomasvh.com/works/blue-sky-days/

#### 无人机打击：调查秘密行动（Drone Strikes: Investigating Covert Operations） — Forensic Architecture (2013)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 无人机空袭留下的弹孔比卫星像素还小；建筑学分析能让看不见的空袭成为证据。
- 作品内容: 为联合国特别报告员开展的针对美国在巴基斯坦、也门、加沙和阿富汗无人机空袭的调查，其中包括根据一位幸存者拍下的一段视频重建的米兰沙一栋房屋遇袭事件。
- 实现方式: 对视频画面、卫星图像和证人证词进行空间分析，并用三维建模确定空袭位置与受害者。
- 视角: 机器之眼, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=CbzVrH6Utjw
- 项目主页: https://forensic-architecture.org/investigation/drone-strikes-investigating-covert-operations-through-spatial-and-media-analysis

#### 无人机生存指南（Drone Survival Guide） — Ruben Pater (2013)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机
- 核心想法: 在无人机遍布的世界里，人们需要一本辨认监视他们的机器的野外图鉴。
- 作品内容: 一张仿照观鸟图鉴设计的海报，展示军用与民用无人机的剪影，并附有躲避它们的方法，被译成普什图语、乌尔都语等多种语言。
- 实现方式: 印在旨在帮助躲避红外摄像机的反光材料上，并在网上和纸本免费发放。
- 视角: 机器之眼, 分类、偏见与监控
- 图片: http://www.dronesurvivalguide.org/dsg.jpg http://www.dronesurvivalguide.org/photo3.jpg
- 项目主页: http://www.dronesurvivalguide.org/

#### 无人机之影（Drone Shadows） — James Bridle (2012)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机
- 核心想法: 当远程武器的影子落在熟悉的地面上，它的尺度才变得真实。
- 作品内容: 用白线在街道和广场上画出 MQ-1“捕食者”等军用无人机的等大轮廓，仿佛它们的影子落在了城市里。
- 实现方式: 以 1:1 比例用粉笔或道路标线漆绘制轮廓，画在伊斯坦布尔、伦敦、布莱顿、华盛顿等城市。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: Design and Violence, Science Gallery Dublin
- 视频: https://www.youtube.com/watch?v=CT5iqTisnTc
- 项目主页: https://jamesbridle.com/

#### Dronestagram — James Bridle (2012)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 远程战争发生在我们从未见过的地方；在信息流中分享的俯瞰图让它短暂地被看见。
- 作品内容: 每当美国在巴基斯坦、也门和索马里的无人机空袭被报道，一个 Instagram 和推特账号就会发布该地点的卫星图像。
- 实现方式: 把调查新闻局的空袭报告与谷歌地图卫星视图匹配，并配以简短说明发布。
- 视角: 机器之眼, 分类、偏见与监控
- 图片: https://jamesbridle.com/media/pages/works/dronestagram/7174ad984b-1680515147/100_dronestagram.jpg
- 项目主页: https://jamesbridle.com/works/dronestagram

#### Metadata+ — Josh Begley (2012)
- 类型: 研究原型 · 机器: 自动驾驶与无人机, 平台与推荐算法
- 核心想法: 远程战争可以被带到手机锁屏上，和其他通知并排出现。
- 作品内容: 一款 iPhone 应用，每当美国无人机空袭被报道就推送一条通知；苹果多次拒绝后才于 2014 年批准上架。
- 实现方式: 使用调查新闻局的空袭数据库；2012 年最初以“Drones+”提交，后改名为 Metadata+。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 图片: https://joshbegley.com/metadata/metadata-2017-map.jpg
- 项目主页: http://joshbegley.com/metadata/

#### 无人（Unmanned） — Molleindustria (2012)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 监控与生物识别
- 核心想法: 遥控战争是一份办公室工作，它的暴力就摆在寻常家庭生活旁边。
- 作品内容: 一款关于无人机飞行员一天生活的网页小游戏：刮胡子、通勤、在屏幕上盯着目标、和儿子玩电子游戏。
- 实现方式: 分屏 Flash 游戏，由 Paolo Pedercini 与 Jim Munroe 创作。
- 视角: 隐形劳动与攫取, 具身与动觉
- 视频: https://www.youtube.com/watch?v=qTsP0SpWdCk
- 项目主页: http://unmanned.molleindustria.org/

#### 严肃游戏 I–IV（Serious Games I–IV） — Harun Farocki (2009)
- 类型: 电影与影像 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 同一幅模拟图像既让士兵为战争做好准备，又治疗战争造成的创伤；在游戏里，战争没有阴影。
- 作品内容: 一组四部分的影像装置，呈现美军如何用计算机模拟训练士兵奔赴伊拉克和阿富汗，又在归来后用它治疗创伤后应激障碍。
- 实现方式: 在美国海军陆战队训练场和南加州大学创意技术研究所拍摄，对比训练软件与治疗软件；各部分制作于 2009–2010 年。
- 视角: 机器之眼, 具身与动觉
- 图片: https://www.harunfarocki.de/fileadmin/_processed_/c/1/csm_harun-farocki-imersion_0275cdcf89.jpg
- 项目主页: https://www.harunfarocki.de/installations/2000s/2009/serious-games-iii-immersion.html

## 分类、权力与正义

偏见、监控与预测，以及抵抗它们的反档案与另类智能。

### 偏见与编码凝视

机器看不见谁、看错谁，以及原因。

#### 阶级（CLASSES） — Libby Heaney (2021)
- 类型: 电影与影像 · 机器: 计算机视觉, 数据集与训练数据, 生成模型与潜空间
- 核心想法: 机器学习的“类别”与社会“阶层”相互纠缠：用网络数据训练的模型，是用别人的眼睛看这片公屋。
- 作品内容: 一部影像散文，场景是艺术家居住的伦敦公屋小区的模拟模型；机器与人声交替讲述机器学习分类如何扭曲工人阶级的生活。
- 实现方式: 在公屋的三维扫描上运行目标检测、图像描述和语言模型，并把输出配音、叠加在一段 14 分钟的单屏影像中。
- 视角: 分类、偏见与监控, 失败、故障与错误
- 图片: https://libbyheaney.co.uk/wp-content/uploads/2022/11/1-1.jpg https://libbyheaney.co.uk/wp-content/uploads/2022/11/2.jpg
- 项目主页: https://libbyheaney.co.uk/artworks/classes/

#### 编码歧视（Coded Bias） — Shalini Kantayya (2020)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别, 平台与推荐算法
- 核心想法: 算法造成的伤害是公民权利问题，需要法律，而不仅是更好的模型。
- 作品内容: 一部长篇纪录片：跟随 Joy Buolamwini 从发现人脸识别偏见一直到在美国国会作证，同时呈现伦敦警方的人脸识别试验和中国的社会评分。
- 实现方式: 观察式纪录片，采访了 Cathy O'Neil、Meredith Broussard、Safiya Noble、Timnit Gebru 以及“老大哥观察”的 Silkie Carlo 等研究者和行动者。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Sundance Film Festival 2020
- 视频: https://www.youtube.com/watch?v=7pMV9scmKwc
- 图片: https://images.squarespace-cdn.com/content/v1/5eb23eee707c5356dea97eaa/1590130745535-D27NXEHHTSDPDBTXVMMF/CODED_BIAS_Home_Resize_2.jpg
- 项目主页: https://www.codedbias.com/

#### 为抹除发声（Voicing Erasure） — Joy Buolamwini (2020)
- 类型: 电影与影像 · 机器: 语音与听觉机器, 聊天机器人与语言模型
- 核心想法: 语音识别对某些声音听得更清楚；听错也是一种抹除。
- 作品内容: 一段口语诗作品：研究 AI 偏见的女性学者朗读自己的研究，语音识别系统把她们的话转写得错漏百出，语音助手在回答女性历史问题时给出的却是男性。
- 实现方式: 与算法正义联盟合作完成。此前斯坦福的一项研究发现，五款商用语音转文字系统对黑人说话者的错误率接近白人说话者的两倍。
- 视角: 机器之耳与声, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=SdCPbyDJtK0
- 项目主页: https://www.ajl.org/voicing-erasure

#### AI，我难道不是女人吗？（AI, Ain't I A Woman?） — Joy Buolamwini (2018)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 机器的错误可能重复一句古老的侮辱；诗歌能让一份审计报告被感受到。
- 作品内容: 一段口语诗影像：Buolamwini 展示商用 AI 系统把 Sojourner Truth、Ida B. Wells、米歇尔·奥巴马、奥普拉和塞雷娜·威廉姆斯的肖像错标为男性。
- 实现方式: Buolamwini 把黑人女性的历史与当代肖像输入各大科技公司的人脸分析服务，并把返回的标签配上她朗读的诗；诗名取自 Sojourner Truth 1851 年的演讲。
- 视角: 分类、偏见与监控, 失败、故障与错误, 机器之眼
- 视频: https://www.youtube.com/watch?v=QxuyfWoVV98
- 项目主页: https://www.ajl.org/

#### 我们，被聚合（Us, Aggregated） — Mimi Ọnụọha (2017)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 平台与推荐算法, 数据集与训练数据
- 核心想法: 自上而下地给人分组是一种不动声色的权力：机器建构的“我们”其实是“他们”。
- 作品内容: 艺术家家庭相册里从未上网的照片，与谷歌以图搜图判定为“相似”的图像并排展示。
- 实现方式: 艺术家用每张家庭照片以程序方式查询谷歌以图搜图，并把结果排成网格；后来的 3.0 版（2019）是一段带有游移光标的循环影像。
- 视角: 分类、偏见与监控, 机器之眼
- 图片: https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/21a78b11-40de-4823-8c9c-802c59fd4c25/00_UA3_installationshot-cropped_courtesyofQuad.jpg https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/38a2109b-ba77-40cf-be21-c17c2ddb4c90/02_UA3_videostill_courtesyofartist.jpg
- 项目主页: https://www.mimionuoha.com/

#### 编码凝视：揭开算法偏见（The Coded Gaze: Unmasking Algorithmic Bias） — Joy Buolamwini (2016)
- 类型: 电影与影像 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 不被机器看见并不中立；它取决于谁出现在训练数据里。
- 作品内容: 一段短片：Buolamwini 在 MIT 做项目时发现，人脸追踪系统只有在她戴上白色面具时才能检测到她的脸。
- 实现方式: 用现成的人脸检测库录屏，对比她自己的脸、一位浅肤色同事的脸和一张白色面具。
- 视角: 分类、偏见与监控, 机器之眼, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=162VzSzzoPs
- 项目主页: https://www.ajl.org/

#### [帮我认清真相]（[help me know the truth]） — Mary Flanagan (2016)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 分类器不一定是机器：系统只是收集并放大人们原本就带着的偏见。
- 作品内容: 观众先自拍，照片被加上噪声后出现在展厅各处的终端上；其他观众反复在两张模糊版本中选出更符合“天使”或“罪犯”等标签的一张，一张刻板印象的脸便从这些选择中浮现。
- 实现方式: 采用认知神经科学的反向相关法：根据观众的二选一，把叠加在肖像上的随机噪声进行平均。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Prix Ars Electronica 2018, Award of Distinction (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=DiHGOqLwN9w
- 图片: https://archive.aec.at/asset/2527247/preview/ https://archive.aec.at/asset/2527249/preview/ https://archive.aec.at/asset/2527254/preview/
- 项目主页: http://maryflanagan.com/work/help-me-know-the-truth/

#### 相面审查器（Physiognomic Scrutinizer） — Marnix de Nijs (2009)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别
- 核心想法: 人脸比对悄悄复活了面相学：以相貌判断品性。
- 作品内容: 观众穿过一道闸门，闸门扫描其面孔，并与 150 位臭名昭著或有争议的人物之一匹配；走过时，机器声音讲述这位“匹配者”的故事。
- 实现方式: 机场式闸门配摄像头与人脸识别软件，将观众与精选图库比对，再由语音合成讲述结果。
- 视角: 分类、偏见与监控, 具身与动觉
- 视频: https://vimeo.com/21460350
- 图片: http://www.marnixdenijs.nl/photos_640x/physiognomic-scrut_2018-09-04_1.png
- 项目主页: http://www.marnixdenijs.nl/physiognomic_scrutinizer.htm

### 监控与预测

用追踪、打分与预测来治理人的系统。

#### 万民共识（Consensus Gentium） — Karen Palmer (2023)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 故事随你的目光而变化，观众因此亲身体验被自己手中的设备画像。
- 作品内容: 一部在智能手机上观看的互动电影：在近未来的监控国家里，观众为获准探望生病的祖母而通过一系列测试，同时手机摄像头追踪其目光并为其服从程度打分。
- 实现方式: 前置摄像头的人脸检测与视线追踪驱动分支叙事，把观众归类为异议者或服从者。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: SXSW 2023; Prix Ars Electronica 2024, Honorary Mention (Interactive Art +)
- 图片: https://archive.aec.at/asset/3800250/preview/ https://archive.aec.at/asset/3800253/preview/
- 项目主页: https://archive.aec.at/prix/290652/

#### 光，到处都是（All Light, Everywhere） — Theo Anthony (2021)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 没有中立的摄像机：每个镜头都有立场，而随身摄像机是从警察一方设计的。
- 作品内容: 一部纪录散文片，从摄影史和工时动作研究，一直讲到警用随身摄像机制造商 Axon，以及在巴尔的摩上空盘旋的监视飞机。
- 实现方式: 在 Axon 总部和巴尔的摩“空中调查研究”项目内部的观察式拍摄，与档案科学影片交叉剪辑；获圣丹斯评审团特别奖。
- 视角: 机器之眼, 分类、偏见与监控
- 展出与获奖: Sundance Film Festival 2021 (Special Jury Award)
- 视频: https://www.youtube.com/watch?v=luHmSqY0Xsk
- 项目主页: https://en.wikipedia.org/wiki/All_Light,_Everywhere

#### 3x3x6 — 郑淑丽 (2019)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 监控技术被反过来对准观众，揭示身体如何被分类为“越轨”。
- 作品内容: 在威尼斯一座旧监狱中，一件全景监控式装置讲述了因性与性别异议而被囚禁者的故事。监控摄像机扫描观众，并把他们的影像混入投影，使观众置身系统之中。
- 实现方式: 多屏投影、采集并处理观众影像的监控摄像机、网站与研究档案；由 Paul B. Preciado 为台湾馆策展。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Taiwan Pavilion, 58th Venice Biennale 2019 (Palazzo delle Prigioni); LG Guggenheim Award 2024
- 视频: https://www.youtube.com/watch?v=MUvqYPKekls
- 图片: https://images.e-flux.com/test/bc8c4a07-4790-4e84-a019-7141af66a1c2?width=1200&height=630
- 项目主页: https://www.e-flux.com/announcements/258006/shu-lea-cheang3x3x6

#### 我的蓝窗（My Blue Window） — American Artist (2019)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 计算机视觉, 数据集与训练数据
- 核心想法: 预测性警务给警察一双机器的眼睛；观众坐进这个把街区看成风险分数的位置。
- 作品内容: 装置被布置成警车内部，观众在仪表盘上观看影片《2015》：一段穿行纽约的行车记录画面，预测性警务软件不断标出“高风险”区域。
- 实现方式: 仿行车记录仪画面叠加模仿 HunchLab 等预测性警务工具的界面图形；在皇后区美术馆与手机应用《1956/2054》一同展出。
- 视角: 分类、偏见与监控, 机器之眼
- 展出与获奖: Queens Museum 2019
- 图片: https://images.squarespace-cdn.com/content/v1/59238d36d2b8575d127794a4/1572016941388-EJM1NHYJ77SXY3WF9G2E/QM-MyBlueWindow-_71A5256-LowRes.jpg
- 项目主页: https://americanartist.us/works/my-blue-window

#### 暗影追踪者（Shadow Stalker） — Lynn Hershman Leeson (2019)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 监控与生物识别, 数据集与训练数据
- 核心想法: 每个人都会投下一道数据阴影，别人可以读取它、据此行动，而且常常读错。
- 作品内容: 观众输入自己的电子邮箱，就会看到投影出来的“数据阴影”：网上能找到的地址、亲属与各种痕迹；同时播放一部关于预测性警务的影片，由 Tessa Thompson 饰演“深网之灵”。
- 实现方式: 装置对观众邮箱进行开源情报检索并投影在地面上，配合一部关于 PredPol 等算法的影片；由纽约 The Shed 委托创作。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 展出与获奖: The Shed, New York 2019
- 视频: https://www.youtube.com/watch?v=FS5FJmtFy64
- 图片: https://www.lynnhershman.com/wp-content/uploads/2019/10/ShadowStalker_Image07.jpg
- 项目主页: https://www.lynnhershman.com/project/shadow-stalker/

#### 幽灵（Spectre） — Bill Posters, Daniel Howe (2019)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 平台与推荐算法, 数据集与训练数据
- 核心想法: 用平台掌控者的深度伪造，让数据经济借他们的声音“认罪”。
- 作品内容: 一件关于“数字影响产业”的装置，其中包括马克·扎克伯格、金·卡戴珊和唐纳德·特朗普称颂一个虚构数据邪教的深度伪造视频；扎克伯格视频检验了 Instagram 的深度伪造政策。
- 实现方式: 与 CannyAI 公司合作制作深度伪造视频，在谢菲尔德纪录片节展出装置，并设有互动“祭坛”，让观众看到自己的数据如何被出售。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 展出与获奖: Sheffield Doc/Fest 2019
- 视频: https://vimeo.com/341794473
- 图片: https://billposters.ch/wp-content/uploads/2020/01/Spectre_press_web_new.jpg
- 项目主页: https://billposters.ch/projects/spectre/

#### 网络游者——握手之旅（The Net Wanderer – A Tour of Suspended Handshakes） — 郭城 (2019)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 一国互联网的边界，是一组普通建筑与被延迟的“握手”，就藏在日常景观里。
- 作品内容: 一个研究与装置项目：追踪中国防火墙网关节点的现实位置；观众在专设电脑上访问被屏蔽网站时，会触发一个浏览器游戏。
- 实现方式: 用网络诊断工具追踪与防火墙相关节点的 IP 地址，再到多个城市实地走访、拍摄这些位置。
- 视角: 隐形劳动与攫取, 不透明与潜空间
- 展出与获奖: Prix Ars Electronica 2020, Honorary Mention
- 图片: https://cdn.guo-cheng.net/files/projectImg/thenetwanderer/theNetWanderer_2.jpg https://cdn.guo-cheng.net/files/projectImg/thenetwanderer/theNetWanderer_1.jpg
- 项目主页: https://guo-cheng.net/index.php/projects/the-net-wanderer/

#### 社交性（Sociality） — Paolo Cirio (2018)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 监控与生物识别
- 核心想法: 专利局是社交操纵机器在被建成之前，就以朴素图示被描述出来的地方。
- 作品内容: Cirio 收集并评级了数百项用于监控和操纵社会行为的美国专利，邀请公众在网站和印刷装置中分享、标记并“封禁”它们。
- 实现方式: 一个收录专利申请及其流程图的数据库，由艺术家分类后在线发布并提供公众标记工具，另有版画和一本以这些图示做成的涂色书。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: S+T+ARTS Prize 2020, Honorary Mention
- 图片: https://paolocirio.net/work/sociality/Sociality-pics-PAN-Naples/DSC_1176.jpg https://paolocirio.net/work/sociality/img/sociality-website.png
- 项目主页: https://paolocirio.net/work/sociality/

#### 破窗之城（The City of Broken Windows） — 黑特·史德耶尔 (2018)
- 类型: 艺术作品与装置 · 机器: 语音与听觉机器, 数据集与训练数据
- 核心想法: 为“破窗”而训练的机器听觉，把旧的警务理论写进了代码；修补是与之相对的动作。
- 作品内容: 两部分组成的装置：工程师在机库里砸碎玻璃，为识别玻璃破碎声的 AI 录制训练数据；行动者 Chris Toepfer 则在新泽西州卡姆登把封起的窗户画成有人居住的样子。
- 实现方式: 两段影像《未破之窗》和《破窗》，分别拍摄于一家为安防系统训练音频分类器的英国公司，以及 Chris Toepfer 的画窗行动。
- 视角: 机器之耳与声, 分类、偏见与监控
- 展出与获奖: Castello di Rivoli 2018
- 视频: https://www.youtube.com/watch?v=iyyM4vDg0xw
- 项目主页: https://www.castellodirivoli.org/en/mostra/hito-steyerl-the-city-of-broken-windows/

#### 白领犯罪风险区（White Collar Crime Risk Zones） — Sam Lavigne (2017)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 数据集与训练数据, 计算机视觉
- 核心想法: 预测性警务的本质是选择打击对象；把它对准华尔街，它的逻辑就显露了。
- 作品内容: 一张预测性警务地图和应用，预测的是金融犯罪而不是街头犯罪；它还给出“可能的嫌疑人”——由数千张高管 LinkedIn 照片平均而成的一张脸。
- 实现方式: 与 Brian Clifton、Francis Tseng 为《The New Inquiry》合作：用 1964–2016 年美国金融业监管局（FINRA）的违规数据训练模型按地点预测风险，并用人脸平均算法生成嫌疑人面孔。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=Wj8meXnHSPo
- 图片: https://whitecollar.thenewinquiry.com/assets/share.jpg?v=2 https://lav.io/projects/white-collar-crime-risk-zones/ars-electronica_huf442887b5b01f9ea96a9441d7fc1f197_3973697_1800x0_resize_q85_box.jpg
- 项目主页: https://whitecollar.thenewinquiry.com/

#### 云指数（Cloud Index） — James Bridle (2016)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 预测模型模糊了预报与控制：预测选票，就是想象去操控它。
- 作品内容: 神经网络用卫星云图和英国民调数据训练，生成能让脱欧公投得出任何指定结果的“天空”，把天气当作操纵政治的杠杆。
- 实现方式: 把历史云图与民调数据相关联，用 DCGAN 生成天空图像。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 图片: https://jamesbridle.com/media/pages/works/cloud-index/890e90e757-1680515138/165_opengraph.jpg
- 项目主页: https://jamesbridle.com/works/cloud-index

#### 阿尔戈斯计划（The Argus Project） — Romi Ron Morrison, Gan Golan (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别, 义体与赛博格
- 核心想法: 反监控可以被想象成一个长满眼睛的集体身体。
- 作品内容: 一套布满摄像头的可穿戴外骨骼，取名自百眼巨人阿尔戈斯，穿着它在夜间穿行城市，作为拍摄警察的“问责力场”。
- 实现方式: 嵌有摄像头与灯光的雕塑服装，在公共空间表演并记录。合作者包括 Raquel De Anda、Ligaiya Romero、Ayodamola Okunseinde 等。
- 视角: 分类、偏见与监控, 具身与动觉
- 视频: https://vimeo.com/185745057
- 图片: https://images.squarespace-cdn.com/content/v1/5a15cc35ccc5c5ef7b89ee2d/1511470361428-WJLOQ36VG386HRT8A6QS/IMG_4178.jpg
- 项目主页: https://elegantcollisions.com/argus

#### 玻璃屋（The Glass Room） — Tactical Tech (2016)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 监控与生物识别, 数据集与训练数据
- 核心想法: 借用科技商店的外观，让对数据攫取的批评触及从不进画廊的人。
- 作品内容: 一个设计得像时髦科技商店的快闪展览，“商品”是关于数据追踪的艺术作品与调查，名为“Ingenius”的工作人员为观众提供隐私建议。
- 实现方式: 由 Tactical Tech 与 Mozilla 合作策划；2016 年首展于柏林，之后在纽约、伦敦和旧金山展出，并配有“数据排毒工具包”和社区巡展版本。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: Berlin 2016; New York 2016; London 2017; San Francisco 2019
- 视频: https://www.youtube.com/watch?v=k47lhUmj5ho
- 图片: https://cdn.ttc.io/i/fit/1740/0/sm/0/plain/theglassroom.org/SF-Atmosphere/sat-26-oct-Daisy12.JPG
- 项目主页: https://theglassroom.org/

#### 虚拟守望者（The Virtual Watchers） — Joana Moll (2016)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 边境监控被众包给无偿的普通人；观看者自己成了机器的一部分。
- 作品内容: 作品基于“得州虚拟边境观察”项目（2008 年起）的档案：志愿者在家通过网络观看边境摄像头的实时画面，并举报疑似越境者。
- 实现方式: 与 Cédric Parizot 合作；重现该项目的观看界面，并配以志愿者留下的存档评论。
- 视角: 隐形劳动与攫取, 机器之眼
- 图片: https://www.janavirgin.com/img/works/virtual_watchers.jpg
- 项目主页: https://www.janavirgin.com/works.html

#### Citizen Ex — James Bridle (2015)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 平台与推荐算法
- 核心想法: 在网上，是机器决定你属于哪个国家，也决定了哪些法律和监控适用于你。
- 作品内容: 一个浏览器插件，记录你访问的网站托管在哪些国家，并计算出你的“算法公民身份”——数据系统根据你的流量推断出的国籍。
- 实现方式: 插件对加载的每个页面和资源进行 IP 地理定位，并以持续更新的饼图显示国家分布；由 The Space 与 Abandon Normal Devices 委托。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=4cRX2evheew
- 图片: https://jamesbridle.com/media/pages/works/citizen-ex/4a7502d256-1680515124/149_badge-banner.jpg
- 项目主页: https://jamesbridle.com/works/citizen-ex

#### 秘密力量（Secret Power） — Simon Denny (2015)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 大规模监控有它自己的美学，那些剪贴画和巫师图案透露出情报机构如何看待世界。
- 作品内容: 新西兰威尼斯双年展国家馆把斯诺登文件中泄露的 NSA 与 GCHQ 幻灯片图形，做成了马尔恰那图书馆和机场里的服务器机柜、地毯和天顶画。
- 实现方式: Denny 追查了 NSA 幻灯片背后的设计师，并把这些图像做成改装的服务器机柜和印刷表面，与图书馆天顶的文艺复兴宇宙观相呼应。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: Venice Biennale 2015 (New Zealand pavilion); Te Papa Tongarewa
- 视频: https://www.youtube.com/watch?v=JidXPz7G0i8
- 图片: https://simondenny.net/wp-content/uploads/modded-serverrack/MA_I390331_TePapa_Modded-ServerRack-Display_preview.jpg
- 项目主页: https://simondenny.net/secret-power/

#### 隐形基站（Stealth Cell Tower） — Julian Oliver (2015)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 警方用来截获手机的招数（“IMSI 捕获器”）可以装进一台办公打印机。
- 作品内容: 一台伪装成办公室打印机的手机基站：附近的手机会自动连上它，然后收到看似来自通讯录中熟人的短信。
- 实现方式: 由软件无线电和树莓派组成的 GSM 基站藏在一台惠普打印机里，打印机还会打印出它发出的短信。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 图片: https://julianoliver.com/projects/stealth-cell-tower/images/stealth-cell-tower.jpg https://julianoliver.com/projects/stealth-cell-tower/images/print.jpg
- 项目主页: https://julianoliver.com/projects/stealth-cell-tower/

#### Jennifer Lyn Morone™ Inc — Jennifer Lyn Morone (2014)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法, 数据集与训练数据, 监控与生物识别
- 核心想法: 如果数据就是价值，那么一个人也可以宣称自己是一家公司；这种荒诞正映照出平台早已在做的事。
- 作品内容: 艺术家把自己注册成一家公司，产品是她的健康数据、位置、技能和观点，并通过一个数据库直接出售。
- 实现方式: 包括合法的公司注册、自我追踪的“个人运营数据库”以及展会摊位，创作于英国皇家艺术学院。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 视频: https://vimeo.com/98300179
- 项目主页: https://jenniferlynmorone.com/

#### 不对称的爱（Asymmetric Love） — Addie Wagenknecht (2013)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 基础设施、能源与供应链
- 核心想法: 监控已成为家居装饰：我们把它挂在家里，还会欣赏它。
- 作品内容: 一盏用闭路监控摄像头、网线和硬件组装成的水晶吊灯，像奢侈品灯具一样悬挂。
- 实现方式: 把安防摄像头和网线安装在吊灯框架上；该系列后来的版本包含可以工作的摄像头。
- 视角: 机器之眼, 亲密、照护与陪伴
- 图片: https://freight.cargo.site/w/800/i/O1964140200252626760958482768938/image-asset-7.jpeg
- 项目主页: https://www.placesiveneverbeen.com/asymmetric-love

#### 监控象棋（Surveillance Chess） — !Mediengruppe Bitnik (2012)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别
- 核心想法: 每台监控摄像头的另一端，都有一个可以被搭话的人。
- 作品内容: 2012 年伦敦奥运会前，艺术家劫持了公共空间一台监控摄像头的信号，换成一盘国际象棋，邀请看不见的控制室操作员下一局。
- 实现方式: 便携发射器用艺术家的国际象棋画面覆盖了摄像头的无线视频信号。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 视频: https://vimeo.com/46236909
- 项目主页: https://wwwwwwwwwwwwwwwwwwwwww.bitnik.org/s/

#### 透明手雷（Transparency Grenade） — Julian Oliver (2012)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 透明也可以自下而上地强制实现；任何房间里的网络都可以被迫“开口”。
- 作品内容: 一枚树脂浇铸的苏联 F1 手雷，内部藏有微型电脑、麦克风和天线：“拉开保险”就会截获房间里的网络流量和声音，并泄露到一张公开的在线地图上。
- 实现方式: 一台带 Wi-Fi 天线和麦克风的 Linux 单板电脑嗅探未加密流量，提取邮件、主机名和图片，并传给服务器在地图上呈现泄露内容。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 图片: https://julianoliver.com/projects/transparency-grenade/images/transparency-grenade2.jpg
- 项目主页: https://julianoliver.com/projects/transparency-grenade/

#### 脸对脸书（Face to Facebook） — Paolo Cirio, Alessandro Ludovico (2011)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 脸一旦成为数据，就可以被任意重新归入别人选定的身份。
- 作品内容: 艺术家抓取一百万个 Facebook 个人主页，用人脸分析软件把 25 万张头像按“得意”“随和”等性格分类，再发布到一个虚假的交友网站 Lovely-Faces.com 上。
- 实现方式: 自制爬虫加人脸检测与表情分析软件；把资料重新发布在专门搭建的交友网站上。
- 视角: 分类、偏见与监控
- 展出与获奖: transmediale 2011
- 图片: https://www.face-to-facebook.net/img/header_k.jpg https://www.face-to-facebook.net/img/face-to-facebook-diagram_web.gif
- 项目主页: https://www.face-to-facebook.net/how.php

#### Memopol-2 — Timo Toots (2011)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 在数字国家里，身份证是一把通往你很少看到的个人档案的钥匙；这台机器让你对自己做背景调查。
- 作品内容: 一台大型机器，观众把身份证或护照插进去，它便收集国家数据库和互联网上关于此人的信息，在定制大屏上展示其数据场，并记住每位观众的名字和肖像。
- 实现方式: 读取爱沙尼亚身份证芯片，查询国家登记系统与网络来源，结果在 LED 面板阵列上可视化。
- 视角: 分类、偏见与监控
- 展出与获奖: Prix Ars Electronica 2012, Golden Nica (Interactive Art)
- 视频: https://www.youtube.com/watch?v=xCr7UdVkmCk
- 图片: https://archive.aec.at/asset/1439540/preview/ https://archive.aec.at/asset/1439541/preview/ https://archive.aec.at/asset/1439585/preview/
- 项目主页: https://archive.aec.at/prix/193063/

#### 灰衣人（Men in Grey） — Julian Oliver, Danja Vasiliev (2009)
- 类型: 表演、舞蹈与音乐 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 只有亲眼看到自己的流量被读取，人们才会感觉到网络中有机器在偷听。
- 作品内容: 两个身穿灰西装、手提公文包的人出现在公共场所；公文包截获并篡改周围人的无线网络流量，并把发现的内容显示出来，演出一个让网络监控变得可感的秘密组织。
- 实现方式: 公文包里装着 Linux 电脑、天线和屏幕，实时运行无线漏洞利用与内容篡改。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: Prix Ars Electronica 2010, Award of Distinction (Hybrid Art); Aksioma, Ljubljana 2011
- 图片: https://archive.aec.at/asset/464136/preview/ https://archive.aec.at/asset/464138/preview/ https://archive.aec.at/asset/464140/preview/
- 项目主页: https://criticalengineering.org/projects/men-in-grey/

#### 无面（Faceless） — Manu Luksch (2007)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 法律对面孔的遮蔽成了电影的世界观：只有申请者本人还拥有一张脸的城市。
- 作品内容: 一部完全由伦敦监控录像构成的科幻电影，这些录像是艺术家依据英国《数据保护法》调取的自己的影像；法律规定他人的脸要被抹去，于是城市看上去没有面孔。
- 实现方式: Luksch 按照自拟的《闭路电视电影人宣言》在公共摄像头前表演，再以数据主体身份申请调取录像；由 Tilda Swinton 旁白。
- 视角: 机器之眼, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=yLzJCeGYgbg
- 项目主页: https://manuluksch.com/

#### 示威（Demonstrate） — Ken Goldberg (2004)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 把监控摄像头的控制权交给公众，是在让言论自由与隐私相互试探。
- 作品内容: 为纪念言论自由运动四十周年，一台高分辨率机器人网络摄像头俯瞰加州大学伯克利分校的 Sproul 广场；任何网民都可以操控它、拍下人群并加以评论。
- 实现方式: 联网云台变焦摄像头配网页界面，用户截取的画面与评论被存档。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=hd6vNv1m6NE
- 项目主页: https://goldberg.berkeley.edu/

#### 证物柜（Evidence Locker） — Jill Magid (2004)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 监控系统也可以被“引诱”成一种照顾；这份亲密暴露了是谁在握着摄像机。
- 作品内容: 在利物浦的 31 天里，艺术家与城市警方的闭路电视系统 Citywatch 合作，通过电话指引操作员跟拍自己，并以调取录像申请表的形式给他们写情书。
- 实现方式: Magid 穿红色外套方便操作员找到她，依据《数据保护法》申请调取录像（否则 31 天后会被删除），再剪辑成影像和一个“阅读室”装置。
- 视角: 机器之眼, 亲密、照护与陪伴
- 展出与获奖: FACT Liverpool 2004; Tate Liverpool 2004
- 视频: https://www.youtube.com/watch?v=laStNBHSfuU
- 项目主页: https://www.jillmagid.com/projects/evidence-locker-2

#### 生活使用说明（Life: A User's Manual） — Michelle Teran (2003)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别
- 核心想法: 城市里早已充满我们看不见的、关于我们的图像。
- 作品内容: Teran 拖着装有视频扫描器与屏幕的行李箱穿行城市，截获私人监控摄像头未加密的无线信号，把身边隐藏的画面展示给路人。
- 实现方式: 手持接收器扫描民用无线摄像头所用频段（很可能是 2.4 GHz），画面显示在随身监视器上。
- 视角: 机器之眼, 具身与动觉
- 视频: https://www.youtube.com/watch?v=MS-T6Yooa9E
- 项目主页: https://www.youtube.com/watch?v=MS-T6Yooa9E

#### 天蓝系统安全装饰（System Azure Security Ornamentation） — Jill Magid (2002)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别
- 核心想法: 装饰摄像头，让不可见的凝视变得显眼，也奇特地带上了私人色彩。
- 作品内容: Magid 向阿姆斯特丹警方提出为城市监控摄像头装饰水钻与饰物，让它们显眼起来，用她的话说，更美。
- 实现方式: 与警方的提案信件和会面，随后在公共空间装饰监控摄像头。
- 视角: 亲密、照护与陪伴, 分类、偏见与监控
- 图片: http://www.jillmagid.com/uploads/images/scaled/slide_image/302 http://www.jillmagid.com/uploads/images/scaled/slide_image/305
- 项目主页: http://www.jillmagid.com/projects/system-azure-security-ornamentation

#### 追踪无常（Tracking Transience） — Hasan Elahi (2002)
- 类型: 艺术作品与装置 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 用数据淹没监视者，使一个人既完全可见，又难以解读。
- 作品内容: 在因一条错误举报被 FBI 反复盘问数月之后，Elahi 开始在网上公开自己的位置，以及成千上万张餐食、厕所和航班的照片，给 FBI 也给所有人看。
- 实现方式: 自 2002 年起，GPS 追踪器与网站持续更新带时间戳的照片；如今档案已有数万张图像。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=wAdwurHhv-I
- 项目主页: https://en.wikipedia.org/wiki/Hasan_Elahi

#### BIT 飞机（BIT Plane） — Bureau of Inverse Technology (BIT) (1999)
- 类型: 艺术作品与装置 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 一架早期的无人机，它监视的是监视者。
- 作品内容: 一架搭载摄像机的小型遥控飞机飞越硅谷的“禁止拍摄区”，从空中拍下建造信息时代的科技公司。
- 实现方式: 自制遥控模型飞机，机载摄像机与发射器，飞越企业园区上空。
- 视角: 机器之眼, 分类、偏见与监控
- 图片: https://bureauit.org/images/plane/plane0self.jpg https://bureauit.org/images/plane/plane031lockh.jpg
- 项目主页: https://bureauit.org/plane/

#### 为监控摄像头表演（Performances for Surveillance Cameras） — Surveillance Camera Players (1996)
- 类型: 表演、舞蹈与音乐 · 机器: 监控与生物识别
- 核心想法: 既然摄像头一直在看，那就为它表演：监控员成了观众，被监视者成了演员。
- 作品内容: 纽约的一个剧团在公共监控摄像头前无声地演出改编的奥威尔《1984》等剧目，举着给监控员看的标语牌，并带领市民绕城“认摄像头”。
- 实现方式: 在摄像头所在位置表演配有大字牌的短小无声剧，并从街头进行记录；该团体还出版了曼哈顿摄像头地图。
- 视角: 机器之眼, 具身与动觉
- 视频: https://www.youtube.com/watch?v=9BtntSJc0a4
- 项目主页: http://www.notbored.org/the-scp.html

### 缺失数据与反数据集

为填补空白、拒绝攫取或重新定义“谁被计入”而做的数据集。

#### 地面真相（Ground Truths） — Mimi Ọnụọha (2025)
- 类型: 电影与影像 · 机器: 数据集与训练数据, 计算机视觉
- 核心想法: 用被抹除所塑造的记录训练出来的模型，也会继承这种抹除；“真值”确实被埋在地下。
- 作品内容: 一部纪录虚构影片：2018 年在得州糖城发现 95 具遗骸之后，艺术家构建机器学习模型，预测全州还有哪些“犯人租赁”受害者的无名墓地。
- 实现方式: 单屏 4K 影像（约 16 分钟），把建模过程与档案、电话和缺失的记录交织在一起。
- 视角: 分类、偏见与监控, 哀悼、记忆与来世, 不透明与潜空间
- 图片: https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/51f2cb4b-30a1-49b4-9ece-1cde6d8effa4/00_GroundTruths_film-still_courtestyoftheartist.jpg https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/8c09a145-022b-4e17-bab1-682266e49fb3/01_GroundTruths_film-still_courtestyoftheartist.jpg
- 项目主页: https://www.mimionuoha.com/

#### 巴比伦视觉（Babylonian Vision） — Nora Al-Badri (2020)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 爬取博物馆数据可以是一种归还：这些图像回到了收藏者没有料到的公共用途之中。
- 作品内容: 一个用博物馆藏美索不达米亚、新苏美尔和巴比伦文物图像训练的神经网络，生成出“合成文物”，以影像形式展出。
- 实现方式: 用从博物馆网站抓取的数千张图像（部分未经许可）训练 GAN；最初由洛桑联邦理工学院展馆委托。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 视频: https://www.youtube.com/watch?v=kTZ5W8Vbpd4
- 图片: https://epfl-pavilions.ch/media/pages/exhibitions/babylonian-vision/647951dfaf-1709114720/cover-2880x1600.png
- 项目主页: https://epfl-pavilions.ch/en/exhibitions/babylonian-vision

#### Igùn — Minne Atairu (2020)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 用被掠文物训练的模型只能重组被拿走的东西；它的空缺映照着殖民档案的空缺。
- 作品内容: 一组生成式“青铜器”，想象 1897 年英军洗劫贝宁王宫之后的那些年里，伊贡街上的铸铜匠人可能创作的作品。
- 实现方式: StyleGAN2 以主要藏于西方博物馆的贝宁青铜、铁器和陶器图像训练。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=pg8U2l4tQAE
- 项目主页: https://igun.info/prototype-I

#### Zizi 秀（The Zizi Show） — Jake Elwes (2020)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 用变装身体训练 AI，是在“酷儿化”它通常学习的数据集规范。
- 作品内容: 一场虚拟的深度伪造变装歌舞秀：拍摄十三位伦敦变装表演者来训练网络，网上观众可以让生成的身体表演歌曲，包括混合出来的女王 Zizi。
- 实现方式: 以每位表演者的影像训练姿态条件视频生成模型，网页界面让用户选择节目与歌曲。
- 视角: 分类、偏见与监控, 具身与动觉
- 图片: https://www.jakeelwes.com/images/project-zizi-show.jpg
- 项目主页: https://www.jakeelwes.com/project-zizi-show.html

#### 毛利语语音识别与 Kaitiakitanga 许可证（Te Reo Māori Speech Recognition and the Kaitiakitanga Licence） — Te Hiku Media (2018)
- 类型: 研究原型 · 机器: 语音与听觉机器, 数据集与训练数据
- 核心想法: 数据主权意味着讲这门语言的社区自己决定谁可以用他们的声音训练模型。
- 作品内容: 一家由毛利人主导的媒体机构，用社区捐赠的录音自建毛利语语音识别，并拒绝把数据交给科技巨头。
- 实现方式: 在 2018 年的 Kōrero Māori 活动中，人们朗读句子，10 天内录下 300 多小时；模型以“守护者许可”（Kaitiakitanga Licence）发布，只允许为毛利人利益而使用。
- 视角: 机器之耳与声, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=sGQy0r_icWc
- 图片: https://opengraph.githubassets.com/1a9ccbb40a42481347763da1c45a53663a09c5a3a855a4a0509aa57bb7b783ad/TeHikuMedia/Kaitiakitanga-License
- 项目主页: https://tehiku.nz/te-hiku-tech/
- 代码: https://github.com/TeHikuMedia/Kaitiakitanga-License

#### 女性主义数据集（Feminist Data Set） — Caroline Sinders (2017)
- 类型: 研究原型 · 机器: 数据集与训练数据, 聊天机器人与语言模型
- 核心想法: 偏见不是在流程末端修正的；从数据到工资，每一步都是政治选择。
- 作品内容: 一个持续多年的项目，通过追问每一个环节来构建女性主义 AI 聊天机器人：在公开工作坊中收集女性主义文本、为其标注、选择模型，并公平地支付劳动报酬。
- 实现方式: 在 SPACE Art + Technology、维多利亚与艾伯特博物馆等地举办社区工作坊，收集并标注文本；Sinders 为整个机器学习流程记录一套批判设计框架。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=WwdmPva8nhc
- 图片: https://carolinesinders.com/wp-content/uploads/2020/05/LEO_6267-1024x678.jpg https://carolinesinders.com/wp-content/uploads/2020/05/VA_Image2_large-1024x683.jpg
- 项目主页: https://carolinesinders.com/feminist-data-set/

#### 我值这么多（自我估价的艺术品）（This Much I'm Worth (the self-evaluating artwork)） — Rachel Ara (2017)
- 类型: 艺术作品与装置 · 机器: 平台与推荐算法
- 核心想法: 让算法当众为作品定价，价值的任意性便显露出来。
- 作品内容: 一件大型霓虹雕塑，持续计算并显示自己的市场价值，数字随观看、讨论和网络分享而变化。
- 实现方式: 雕塑内置联网电脑，收集数据（很可能包括观众人数、社交媒体提及和艺术市场指标），运行估值算法并驱动霓虹数字。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 展出与获奖: Uncanny Values, MAK Vienna 2019; Aesthetica Art Prize
- 视频: https://www.youtube.com/watch?v=wZ-P6dnkVcY
- 项目主页: https://www.mak.at/en/program/exhibitions/uncanny_values

#### 缺失数据集图书馆（The Library of Missing Datasets） — Mimi Ọnụọha (2016)
- 类型: 艺术作品与装置 · 机器: 数据集与训练数据
- 核心想法: 一个社会不去统计的东西，和它统计的东西一样清楚地显示出它的价值观；“缺失”的数据集既是一种缺乏，也是一种应当。
- 作品内容: 一个装满空文件夹的白色文件柜，每个文件夹都标着一个并不存在的数据集，比如因犯罪记录被拒于公共住房之外的人，或在仇恨犯罪中被杀害或受伤的跨性别者。
- 实现方式: 这一实体档案来自艺术家自 2015 年起在 GitHub 上维护的缺失数据集清单；2.0 版（2018）聚焦黑人，3.0 版则是一个上锁的柜子，存放那些一旦收集就会危及他人的数据集。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 图片: https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/94ae8920-0367-440f-b24e-5794636edf6f/00small_LibraryofMissingDatasets_propertyofartist_creditBrandonSchulman.jpg https://images.squarespace-cdn.com/content/v1/692f1808f9a01f48c2fa30ac/5f58c44d-4c0b-4d25-9148-02c8fc120a4e/04_LibraryofMissingDatasets2_propertyofartist.jpg
- 项目主页: https://github.com/MimiOnuoha/missing-datasets

### 女性主义、去殖民与原住民 AI

从其他文化、性别与知识体系出发想象的 AI。

#### Nosukaay — Diane Cescutti (2022)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链
- 核心想法: 早在计算机之前，编织就已是一种计算；这台机器从西非纺织知识而不是硅谷出发说话。
- 作品内容: 一尊由 Manjak 织机构成的“机器神”，织机的两个框架被裸露的屏幕取代；观众抚摸一块手织腰布来操作一部关于另一种计算史的影像游戏，若对它不敬便会被踢出。
- 实现方式: 一块导电的手织 Manjak 布作为触摸键盘，操作由文本、三维图像和达喀尔编织工坊实拍影像构成的互动叙事。
- 视角: 能动、自主与共创, 具身与动觉
- 展出与获奖: Prix Ars Electronica 2024, Golden Nica (Interactive Art +)
- 视频: https://www.youtube.com/watch?v=939QlKGURoI
- 图片: https://archive.aec.at/asset/3797338/preview/ https://archive.aec.at/asset/3797341/preview/
- 项目主页: https://archive.aec.at/prix/290626/

#### 交叉性 AI 工具包（Intersectional AI Toolkit） — Sarah Ciston (2021)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: AI 素养是一个权力问题：当受影响的人能读懂并改造工具，工具才会更公平。
- 作品内容: 一套小志和一个维基，用浅白的语言向艺术家、行动者以及酷儿和边缘社群解释 AI，并追问交叉性女性主义能如何改变它。
- 实现方式: 由众多参与者共同制作的小志、工作坊与开源维基；在 Ciston 于南加州大学攻读博士期间发展而成。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 图片: https://intersectionalai.com/assets/img/zineHowTo.png
- 项目主页: https://intersectionalai.com/

#### 非洲当下主义（Afro-now-ism） — Stephanie Dinkins (2020)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: 与其寄望于非洲未来主义，不如此刻行动：参与制造将塑造你生活的数据与代码。
- 作品内容: 一篇文章：Dinkins 呼吁黑人社区不要再等待未来的解放，而要此刻就去建造他们需要的技术和 AI 系统。
- 实现方式: 发表于《Noema》杂志，基于她的《Not the Only One》和社区 AI 工作坊经验。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 论文: https://www.noemamag.com/afro-now-ism/ (Noema Magazine)
- 图片: https://www.noemamag.com/wp-content/uploads/2020/06/Not-the-Only-One-3d-Avatar-SKETCH252-BECOMING.jpg
- 项目主页: https://www.noemamag.com/afro-now-ism/

#### 原住民礼俗与人工智能立场文件（Indigenous Protocol and Artificial Intelligence Position Paper） — Jason Edward Lewis (2020)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: AI 可以被设计成负有义务的亲属，而不只是工具；协议先于产品。
- 作品内容: 一份立场文件，来自在檀香山举行的工作坊：来自新西兰、澳大利亚、北美和太平洋地区的原住民技术人员、艺术家和长者阐述了如何依据各自的礼俗协议来设计 AI。
- 实现方式: 由 Jason Edward Lewis 主编，Angie Abdilla、Noelani Arista、Suzanne Kite 等人撰稿；由“原住民协议与 AI 工作组”和 CIFAR 出版，包含指南、文章与设计原型。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.11573/spectrum.library.concordia.ca.00986506 (Indigenous Protocol and AI Working Group / CIFAR, Honolulu)
- 图片: https://www.indigenous-ai.net/wp-content/uploads/2019/04/waiwai2.jpg
- 项目主页: https://www.indigenous-ai.net/position-paper/

#### Masakhane：非洲机器翻译的参与式研究（Masakhane: Participatory Research for African Machine Translation） — Masakhane (2020)
- 类型: 论文 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: 谁来构建语言模型，决定了哪些语言对机器而言存在；参与式研究是一种“被计入”的方式。
- 作品内容: 一个遍布非洲、由数百名志愿者组成的草根网络，在没有学术门槛的情况下，为数十种非洲语言建立了机器翻译数据和模型。
- 实现方式: 志愿者为自己的语言贡献数据、模型和评测；过程与结果发表在 EMNLP 2020 Findings 论文中。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 论文: https://arxiv.org/abs/2010.02353 (Findings of EMNLP 2020)
- 视频: https://www.youtube.com/watch?v=mbkuRZkg1RY
- 项目主页: https://www.masakhane.io/

#### Wampum.codes — Amelia Winger-Bearskin (2020)
- 类型: 思辨设计 · 机器: 聊天机器人与语言模型, 数据集与训练数据
- 核心想法: 软件是人与人之间的约定；原住民的记录技术可以塑造我们编写它的方式。
- 作品内容: 一个框架与播客，借鉴记录部族间协议的贝壳串珠带，提出以原住民价值观作为软件和 AI 开发的伦理准则。
- 实现方式: 包括讲座、系列播客和一份伦理准则文件，在 imagineNATIVE 电影节展示，于艺术家的驻留与教学中发展而来。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 展出与获奖: imagineNATIVE Festival 2020
- 视频: https://www.youtube.com/watch?v=8I4FjCtAW8Y
- 项目主页: https://wampum.codes/

#### Being — Rashaad Newsome (2019)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 生成模型与潜空间, 语音与听觉机器
- 核心想法: AI 可以被写成一位黑人、酷儿、去殖民的老师，而不是一个顺从的助手。
- 作品内容: 一个 AI“数字说唱史诗人”：以 vogue 舞者身体和非洲面具为脸的动画形象，会讲课、导览、带工作坊，内容取材于 bell hooks、Paulo Freire 与舞会文化。
- 实现方式: 由动作捕捉的 voguing、以精选文本训练的聊天机器人和合成语音组成；不同版本曾担任导览员、老师和心理治疗师。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=CzupjhLM6RQ
- 项目主页: https://rashaadnewsome.com/

#### 跨女性主义技术神谕（Oracle for Transfeminist Technologies） — Coding Rights (2019)
- 类型: 思辨设计 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 以不同的价值观设计，会产生不同的机器；想象力是对抗默认技术的第一步。
- 作品内容: 一副卡牌和一个工作坊游戏：玩家抽取“价值”“物件”“情境”等卡牌和“跨女性主义”提示，想象基于这些卡牌的技术。
- 实现方式: 由 Coding Rights 的 Joana Varon 与合作者共同创作，在拉丁美洲各地和线上的工作坊中使用。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 图片: https://static.wixstatic.com/media/cfe831_05a51b539e8749c384a4b4021517120a~mv2.png
- 项目主页: https://transfeministech.codingrights.org/

#### 退化文化（Degenerative Cultures） — Cesar & Lois (Cesar Baio, Lucy HG Solomon) (2018)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 数据集与训练数据
- 核心想法: 让算法与活的生物配对，机器智能便开始借用腐败的逻辑，而不是控制的逻辑。
- 作品内容: 真菌在讲述人类控制自然欲望的印刷书籍上生长，慢慢抹去文字；一个通过摄像头观察的 AI 读取菌落的生长，作为“生物—数字混合体”到网上搜寻类似文本并加以腐蚀，再以推特账号 @HelloFungus 发布结果。
- 实现方式: 计算机视觉追踪书页上类黏菌的微生物生长；这些数据驱动一个结合元胞自动机与自然语言处理的算法，在网上寻找并改写文本，并在现场用热敏打印机打印出来。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: Lumen Prize 2018, BCS Artificial Intelligence Award; Brighton Digital Festival 2018
- 视频: https://www.youtube.com/watch?v=HQwGFEqO1D0
- 图片: http://static1.squarespace.com/static/65e7176a61627736e02f6c4a/6606a61178dd51369b416024/6606c08ef1cf21462183357b/1711718676868/AI-Award-Degenerative-Cultures6-1000x0-c-default.jpeg http://cesarandlois.org/wp-content/uploads/Cesar-Lois-degerative-cultures-1.jpg
- 项目主页: https://cesarandlois.org/digitalfungus/

## 人机共演与混成身体

人与机器的身体融合或同台共演：义体、远程在场、舞蹈、剧场、音乐与绘画。

### 赛博格与义体

被机器延伸、侵入或远程操控的身体。

#### 独生独死（DOKU the Self） — 陆扬 (2022)
- 类型: 电影与影像 · 机器: 义体与赛博格, 生成模型与潜空间
- 核心想法: 由自己的动作数据驱动的化身，成为一种机器形式的轮回。
- 作品内容: 由艺术家本人的面部与动作驱动的无性别数字化身 DOKU，穿越佛教六道轮回。
- 实现方式: 对艺术家与舞者进行全身与面部动作捕捉，以实时游戏引擎渲染。
- 视角: 具身与动觉, 哀悼、记忆与来世
- 展出与获奖: Times Square Midnight Moment, New York 2023
- 视频: https://www.youtube.com/watch?v=cq24sSnccXc
- 项目主页: https://en.wikipedia.org/wiki/Lu_Yang_(artist)

#### 假体记忆（Prosthetic Memory） — M Eifler (2020)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 当一个小小的个人模型替你保存记忆，回忆就变成一次机器识别，而且别人也能旁观。
- 作品内容: 一套持续进行的自我增强系统，用来替代艺术家因童年脑损伤而受损的长期记忆：当手写日记的某一页摊在桌上，摄像头认出这一页，并在旁边投出当天录下的视频记忆。
- 实现方式: 日记上方的摄像头把画面交给定制训练的图像分类器，识别页码后触发对应的日常视频投影；后续版本加入艺术家本人的深度伪造形象朗读日记。
- 视角: 哀悼、记忆与来世, 具身与动觉
- 展出与获奖: S+T+ARTS Prize 2020, Honorary Mention
- 图片: https://ars.electronica.art/starts-prize/files/2020/06/prostheticmemory-1024x512.jpg
- 项目主页: https://ars.electronica.art/starts-prize/en/prosthetic-memory/

#### 杏仁核（Amygdala） — Marco Donnarumma (2017)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 义体与赛博格
- 核心想法: 没有人类佩戴者的 AI 义体学着自己的动作：一只在寻找身体与仪式的肢体。
- 作品内容: 一只装着刀的机械臂，按人类肢体的结构打造，由通过试错学习的 AI 驱动，在一场净化仪式中反复切割一块类似皮肤的材料。
- 实现方式: 类人机械臂配备传感器与自适应神经网络，通过强化学习发展出切割动作。
- 视角: 能动、自主与共创, 他异与恐怖谷, 具身与动觉
- 视频: https://www.youtube.com/watch?v=h4ykqTG1ZjY
- 图片: https://marcodonnarumma.com/live/wp-content/uploads/2017/09/Marco-Donnarumma_Amygdala-MK3_13_ed_web.jpg
- 项目主页: https://marcodonnarumma.com/works/amygdala/

#### 电磁脑神教（Electromagnetic Brainology） — 陆扬 (2017)
- 类型: 电影与影像 · 机器: 义体与赛博格
- 核心想法: 宗教体验与情绪被演绎成可以从外部接通的电路。
- 作品内容: 四位神祇般的表演者分别对应佛教的地、水、火、风四大元素，在电磁脑刺激的操控下打斗与舞蹈。
- 实现方式: 动作捕捉舞者与游戏引擎化身结合经颅磁刺激的影像（推测）。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=X7A8S2Q79HI
- 项目主页: https://en.wikipedia.org/wiki/Lu_Yang_(artist)

#### 第三拇指（Third Thumb） — Dani Clode (2017)
- 类型: 研究原型 · 机器: 义体与赛博格
- 核心想法: 延伸身体不只是机械问题：大脑会改写对手的认知，把机器纳入其中。
- 作品内容: 一只 3D 打印的机器人“额外拇指”，戴在小指一侧，由大脚趾下的压力传感器控制；伦敦大学学院后来的研究发现，连续数天佩戴它的人学会了新的抓握方式，大脑中的手部表征也发生了变化。
- 实现方式: 两个电机拉动 3D 打印拇指中的线缆；无线足部传感器把脚趾压力映射为弯曲与内收动作。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.1126/scirobotics.abd7935 (Science Robotics 2021)
- 视频: https://www.youtube.com/watch?v=UD_LwZD2Kls
- 图片: https://dvqlxo2m2q99q.cloudfront.net/000_clients/107233/page/g22141jqBFNhnz6t.jpg
- 项目主页: https://www.daniclodedesign.com/thethirdthumb

#### 零躯体（Corpus Nil） — Marco Donnarumma (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 生成模型与潜空间
- 核心想法: 机器并不跟随身体，而是向它学习并推动它，一起造出一具陌生的新身体。
- 作品内容: 一具几乎静止、涂满颜料的身体在地上缓慢扭曲；AI 系统聆听肌肉声音与血流，以巨大的声响与光回应，把表演者推入陌生的姿态。
- 实现方式: 生物传感器（肌音麦克风与血流传感器）把数据输入机器学习软件，实时生成声音与灯光。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=CAIh8FxLMtk
- 图片: https://marcodonnarumma.com/live/wp-content/uploads/2017/03/marco-donnarumma_corpus-nil_zkm_onuk.jpg
- 项目主页: https://marcodonnarumma.com/works/corpus-nil/

#### 地狱（Inferno） — Louis-Philippe Demers, Bill Vorn (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 工业机械臂
- 核心想法: 被机器带动的感受来自身体内部：参与者既是这段编舞的表演者，也是它的受害者。
- 作品内容: 观众被绑进机器人外骨骼，在嘈杂的工业音乐中被带动手臂和躯干，整群人变成被机器操纵的身体合唱，一座仿但丁的“地狱”。
- 实现方式: 手臂与背部装有气动或电动驱动器的可穿戴外骨骼，由中央控制，与声光同步。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=sGIbZ5DD4fY
- 图片: http://billvorn.concordia.ca/robography/images/Inferno01.jpg
- 项目主页: http://billvorn.concordia.ca/robography/Inferno.html

#### 推进（Propel） — Stelarc (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂, 义体与赛博格
- 核心想法: 在这里机器是编舞者，人是负载；身体只是可互换的末端执行器之一。
- 作品内容: Stelarc 的身体被固定在一台工业机械臂末端，由机械臂在 35 分钟内编排它的轨迹、速度与朝向；之后机器人以同样的编舞举着一只巨大的雕刻耳朵再跳一遍。
- 实现方式: 臂展 3 米的工业机械臂按固定编舞编程；同一台机器人还铣削出它随后搬动的耳朵雕塑。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: DeMonstrable, Lawrence Wilson Art Gallery, Perth (2015)
- 视频: https://www.youtube.com/watch?v=2bRpTn0KKd8
- 项目主页: https://stelarc.org/

#### 地震感／等待地震（Seismic Sense / Waiting for Earthquakes） — Moon Ribas (2013)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 基础设施、能源与供应链
- 核心想法: 联网植入物可以把身体接入行星的时间：舞者无法选择自己何时移动。
- 作品内容: 植入体内、连接在线地震仪的传感器会在地球上任何地方发生地震时振动；在表演《等待地震》中，Ribas 静立等待，把感受到的每次震动转化为动作。
- 实现方式: 由实时地震数据驱动的振动植入物（最初在手臂，后移至双脚）；地震越强，振动越强。
- 视角: 具身与动觉, 机器环世界
- 视频: https://www.youtube.com/watch?v=1Un4MFR-vNI
- 图片: https://images.hoobaweb.com/8930/imgf-1200-630/moon-ribas.png
- 项目主页: https://www.moonribas.com/

#### 未来身体计划书（Prospectus for a Future Body） — 徐家辉 (2011)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 如果机器能驱动你的肌肉，舞蹈史就可以被储存，并在别人的身体里回放。
- 作品内容: 一系列实验与表演：用肌肉电刺激让舞者的肌肉收缩，试图把其他舞者（包括土方巽的舞踏）的动作作为“数字肌肉记忆”转移到另一个身体里。
- 实现方式: 由录制的动作数据驱动神经与肌肉电刺激，包括四个提案：《永恒夏日风暴》《仿生动作研究》《同步测量》与《Notion：舞蹈虚构》。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Festival Tokyo 2011 (Notion: Dance Fiction); 15th Japan Media Arts Festival, Jury Selection
- 视频: https://www.youtube.com/watch?v=5JlYSgxECxs
- 图片: https://www.ka5.info/1_PROSPECTUS/3-NOT01.jpg https://www.ka5.info/1_PROSPECTUS/1-ESS02.jpg
- 项目主页: https://www.ka5.info/prospectus.html

#### 3rdi — Wafaa Bilal (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 计算机视觉, 监控与生物识别
- 核心想法: 身体可以携带一只自己无法透过它观看的自动之眼；机器是替他人看，而不是替佩戴者看。
- 作品内容: 约一年时间里，Bilal 的后脑勺上通过手术固定了一台摄像机，每分钟拍一张照片，实时传到网站和多哈的 Mathaf 美术馆，记录他身后留下的一切。
- 实现方式: 小型摄像头安装在植入后脑的钛板上，每分钟拍一帧，通过笔记本电脑上传。
- 视角: 机器之眼, 具身与动觉
- 展出与获奖: Mathaf: Arab Museum of Modern Art, Doha (2010–11)
- 视频: https://www.youtube.com/watch?v=h2nNKbO9-Eg
- 项目主页: https://wafaabilal.com/3rdi/

#### 月经机器——隆的体验（Menstruation Machine – Takashi's Take） — Sputniko! (Hiromi Ozaki) (2010)
- 类型: 思辨设计 · 机器: 义体与赛博格
- 核心想法: 戴在身上的机器可以让一种性别化的经验被转移，从而可以被讨论。
- 作品内容: 一个金属腰带状装置，模拟月经的出血和下腹疼痛；配套的流行音乐录像讲述一个男孩戴上它，去体验女性朋友的经历。
- 实现方式: 释放“经血”的机构与刺激下腹的电极，按 28 天周期运行；以音乐录像和服装一起展出。
- 视角: 具身与动觉, 分类、偏见与监控
- 展出与获奖: ZKM Karlsruhe
- 视频: https://www.youtube.com/watch?v=gnb-rdGbm6s
- 图片: https://upload.wikimedia.org/wikipedia/commons/a/ad/Sputniko.jpg
- 项目主页: https://en.wikipedia.org/wiki/Sputniko!

#### 面部电刺激（Electric Stimulus to Face） — 真锅大度 (2008)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 当计算机驱动面孔，表情就与感受分离了。
- 作品内容: 贴在脸上的电极接收与音乐同步的电脉冲，表演者的面部肌肉抽动出并非他们自己做出的表情。
- 实现方式: 计算机通过表面电极发送按序列编排的肌肉电刺激（EMS），与配乐同步；后来的版本读取一张脸的肌电信号来驱动另一张脸。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=tJ4_-2_oWuM
- 项目主页: https://en.wikipedia.org/wiki/Daito_Manabe

#### 手臂上的耳朵（Ear on Arm） — Stelarc (2006)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格
- 核心想法: 器官可以被移位并改作他用：成为为他人而非为自己服务的公共、联网感官。
- 作品内容: 一只由细胞培养组织和生物相容支架构成的耳朵，通过手术建在 Stelarc 左前臂上；他计划植入麦克风，把这只耳朵“听到”的声音传上互联网。
- 实现方式: 自 2006 年起经多次手术在皮下植入多孔聚乙烯支架，让组织长入；曾测试植入麦克风，后因感染取出。
- 视角: 具身与动觉, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=s80ZjumSA08
- 图片: https://upload.wikimedia.org/wikipedia/commons/2/23/Stelarc_3rd_ear_2011f.jpg
- 项目主页: https://stelarc.org/

#### Eyeborg（赛博格天线）（Eyeborg (Cyborg Antenna)） — Neil Harbisson (2004)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 机器感官可以成为一个人身体与身份的一部分，而不只是他使用的工具。
- 作品内容: 一根与 Harbisson 颅骨骨融合的天线，把光的频率（包括红外和紫外）转换为他通过骨传导听到的振动；他用这种感官作画、作曲。
- 实现方式: 天线末端的摄像头传感器连接芯片，把色相映射为音高，经骨传导听到；蓝牙可接收远程颜色输入。
- 视角: 机器之眼, 具身与动觉
- 视频: https://www.youtube.com/watch?v=ygRNoieAnzI
- 项目主页: https://www.cyborgarts.com/

#### 赛博格计划 2.0（神经植入）（Project Cyborg 2.0 (neural implant)） — Kevin Warwick (2002)
- 类型: 研究原型 · 机器: 义体与赛博格, 工业机械臂
- 核心想法: 神经系统可以被联网：触觉与动作作为数据在身体与机器之间传递。
- 作品内容: Warwick 在手臂正中神经中植入了 100 个电极的阵列；他借此从纽约经互联网操控一只机器手，并与植入了更简单电极的妻子交换简单的神经信号。
- 实现方式: 植入正中神经的 Utah 微电极阵列，连接计算机记录与刺激神经信号，并经互联网转发。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 论文: https://doi.org/10.1001/archneur.60.10.1369 (Archives of Neurology 2003)
- 视频: https://www.youtube.com/watch?v=GLq7edATaFo
- 项目主页: https://en.wikipedia.org/wiki/Kevin_Warwick

#### 假肢头（Prosthetic Head） — Stelarc (2002)
- 类型: 艺术作品与装置 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: “义体”也可以是一颗头脑而非一只手：艺术家通过一个替他作答的对话体延伸自己。
- 作品内容: 一个投影出的大型三维头像，带着 Stelarc 的面孔，与键入问题的观众交谈；它有自己的观点和情绪，还会即兴作诗，与其说是肖像，不如说是会对话的替身。
- 实现方式: 具身对话代理：聊天机器人引擎配合定制知识库、语音合成，以及实时动画的艺术家头部三维模型。
- 视角: 他异与恐怖谷, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=dprvwAWfy9Q
- 项目主页: https://stelarc.org/

#### 赛博格系列（Cyborg series） — 李昢 (1998)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 类人机器人
- 核心想法: 技术完美被揭示为一种性别化的幻想，赛博格身体则总是不完整的。
- 作品内容: 白色硅胶女性赛博格雕塑，常常缺头断肢，像盔甲或动漫女主角一样悬挂在空中。这个 1998 年首次在首尔 Artsonje 中心展出的系列把机器增强的身体呈现为残缺而被情欲化的对象。
- 实现方式: 以硅胶、聚氨酯铸造并上色，借用漫画、动画与古典雕塑语汇；代表作有《Cyborg W1–W4》（1998）。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Artsonje Center, Seoul 1998; Korean Pavilion, 48th Venice Biennale 1999; Lee Bul: Crashing, Hayward Gallery 2018
- 视频: https://www.youtube.com/watch?v=aS5di0wCD1I
- 图片: https://upload.wikimedia.org/wikipedia/commons/5/5a/Untitled_%28Cyborg%27s_pelvis%29_by_Lee_Bul%2C_British_Museum_01.jpg
- 项目主页: https://www.guggenheim.org/artwork/artist/lee-bul

#### 外骨骼（Exoskeleton） — Stelarc (1998)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 义体与赛博格
- 核心想法: 身体同时成为一具更大的、非人身体的驾驶者与乘客。
- 作品内容: Stelarc 站在一台六足气动步行机上，用手臂动作控制它行走与转向，机器的嘶嘶声与撞击声被放大成配乐。
- 实现方式: 在汉堡与工程师共同打造的气动六足机器人；手臂外骨骼上的传感器读取手臂动作，选择步态与方向。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=R2MntBUwUxY
- 项目主页: https://stelarc.org/

#### 时间胶囊（Time Capsule） — Eduardo Kac (1997)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 监控与生物识别
- 核心想法: 能被机器读取，就意味着被分类；植入物把身体变成一条数据库记录。
- 作品内容: 在巴西电视与网络直播中，Kac 把一枚身份识别芯片植入自己的脚踝，随后在网上的宠物寻回数据库中把自己同时登记为“动物”与“主人”。
- 实现方式: 用注射器植入 RFID 芯片，现场扫描，并在线把芯片编号登记到动物识别数据库。
- 视角: 分类、偏见与监控, 具身与动觉
- 展出与获奖: Casa das Rosas, São Paulo (1997)
- 图片: https://www.ekac.org/needle.gif
- 项目主页: https://www.ekac.org/timec.html

#### Ping 身体（Ping Body） — Stelarc (1996)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 基础设施、能源与供应链
- 核心想法: 网络可以成为身体的神经系统：在这里，身体被它无法感知的数据推动。
- 作品内容: Stelarc 向数十个互联网域名发送 ping 信号，返回时间驱动肌肉电刺激系统；于是是网络流量而非他的意志，让他的四肢抽动和移动。
- 实现方式: 来自全球互联网主机的 ping 值被映射到计算机控制的肌肉电刺激系统，电极贴在四肢上；第三只手则由他自己的肌电信号驱动。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: DEAF96, V2_ Rotterdam (1996)
- 视频: https://www.youtube.com/watch?v=45MOlsFGSHI
- 项目主页: https://stelarc.org/

#### Epizoo — Marcel·lí Antúnez Roca (1994)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 界面让残酷变得像游戏：远处的一次点击，化作另一具身体上的疼痛。
- 作品内容: Antúnez 身穿气动外骨骼站在转台上；观众用电脑鼠标操控外骨骼拉扯他的鼻子、耳朵、嘴、臀部和胸部，同时屏幕上播放着他身体的卡通动画。
- 实现方式: 穿戴在身上的气动机构由计算机驱动，观众通过图形界面和鼠标控制。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=5utDR8VWxms
- 图片: https://www.marceliantunez.com/media/cache/3b/1f/3b1f492a17b1654525596a9cc5d9af01.jpg
- 项目主页: https://www.marceliantunez.com/work/epizoo/

#### 互不通信机器（Inter Dis-Communication Machine） — 八谷和彦 (1993)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 通过机器交换感官，显示出“自我”有多依赖自己的视角。
- 作品内容: 两个人戴上头戴显示器、穿上带翅膀的服装；每个人只能看到、听到对方的摄像头和麦克风所捕捉的内容，只能在彼此的感知里行动。
- 实现方式: 每位佩戴者身上的无线摄像头与麦克风，把画面和声音传到对方的头戴显示器和耳机。
- 视角: 具身与动觉, 机器之眼
- 视频: https://www.youtube.com/watch?v=JOzVzcmK0VU
- 图片: https://www.ntticc.or.jp/uploads/assets/000/63850.936.large.jpg
- 项目主页: https://www.ntticc.or.jp/en/archive/works/inter-dis-communication-machine/

#### 第三只手（Third Hand） — Stelarc (1980)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 多出来的肢体需要学习而非天生：身体慢慢为一台间接控制的机器腾出位置。
- 作品内容: 一只安装在 Stelarc 手臂上的机械右手，由他腹部和腿部肌肉的电信号驱动；多年来他用它与自己的双手一起写字和表演。
- 实现方式: 具备捏、握和手腕旋转功能的机械手，由腹部和腿部的肌电电极控制，并向手臂提供触觉反馈。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=Or1CVc6A9YA
- 项目主页: https://stelarc.org/

#### WearComp 与 EyeTap（WearComp and EyeTap） — Steve Mann (1978)
- 类型: 研究原型 · 机器: 义体与赛博格, 计算机视觉, 监控与生物识别
- 核心想法: 生活在机器的视野里，既改变你看到的，也改变别人看你的方式；Mann 把这种反向凝视称为“反向监视”。
- 作品内容: 数十年间，Mann 制作并在日常生活中佩戴越来越小的计算机与头戴式摄像显示器，通过一台能记录、修改和分享视野的计算机看世界。
- 实现方式: 从背包式到眼镜式的可穿戴计算机，配备与眼睛对齐的摄像头和显示器（EyeTap），实时中介视觉。
- 视角: 机器之眼, 具身与动觉, 分类、偏见与监控
- 论文: https://doi.org/10.1109/2.566147 (IEEE Computer 1997)
- 视频: https://www.youtube.com/watch?v=fCco6FMCRmk
- 图片: https://upload.wikimedia.org/wikipedia/commons/3/3e/SteveMann_with_Generation-4_Glass_1999.jpg
- 项目主页: http://wearcam.org/

### 远程在场与远端身体

借助机器在远处行动、触碰与在场。

#### 分身机器人咖啡馆 DAWN ver.β（Avatar Robot Café DAWN ver.β） — Ory Laboratory (2018)
- 类型: 研究原型 · 机器: 社交与陪伴机器人
- 核心想法: 机器人身体可以把工作与社会存在还给那些被自己的身体困在家中的人。
- 作品内容: 东京的一家咖啡馆，服务员是 OriHime 机器人，由因渐冻症等原因无法出门的人在家中远程操作。
- 实现方式: 平板和眼动界面通过互联网控制 1.2 米高的 OriHime-D 与桌面型 OriHime；2018 年开始试点，2021 年在日本桥开设常设店。
- 视角: 隐形劳动与攫取, 具身与动觉, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=tKzCZ_yP4-Y
- 图片: https://dawn2021.orylab.com/assets/images/common/ogp2.jpg
- 项目主页: https://dawn2021.orylab.com/en/

#### 人身保护令（Habeas Corpus） — Laurie Anderson (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 基础设施、能源与供应链, 计算机视觉
- 核心想法: 远程在场可以让一个身体出现在边界与法律拒绝它的地方。
- 作品内容: Mohammed el Gharani 14 岁起被关押在关塔那摩，获释后仍被禁止入境美国；他从西非实时出现，以巨型投影落在纽约 Park Avenue Armory 一座白色坐像上，讲述自己的经历。
- 实现方式: 来自非洲的实时视频流投射到一尊仿林肯纪念堂雕像的大型立体雕塑上。
- 视角: 具身与动觉, 分类、偏见与监控
- 展出与获奖: Park Avenue Armory, New York (2015)
- 视频: https://www.youtube.com/watch?v=kUKLA-W0nDM
- 项目主页: https://laurieanderson.com/

#### 成为他人的机器（The Machine to Be Another） — BeAnotherLab (2012)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 义体与赛博格
- 核心想法: 身体所有感很脆弱：同步的看与触碰，就足以让机器交换身体。
- 作品内容: 两名参与者戴上头显，看到的是对方头戴摄像头的实时画面，并相互模仿动作；几分钟内，每人都会感觉自己进入了对方的身体。
- 实现方式: 基于身体所有感错觉研究，使用头戴摄像头与 VR 显示器，配合同步动作与触碰。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=hjIOUa10YpI
- 图片: https://beanotherlab.org/wp-content/uploads/2019/04/bal_tmtba01.jpg
- 项目主页: https://beanotherlab.org/home/work/tmtba/

#### Telenoid R1 — 石黑浩 (2010)
- 类型: 研究原型 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 刻意去掉性别与年龄的身体，让听者自己想象说话的人，存在感反而更强。
- 作品内容: 一个小巧、苍白、只有短小四肢和极简面孔的机器人，传递远方之人的声音与头部动作；人们把它抱在怀里与远方的人交谈。
- 实现方式: 约 80 厘米、5 公斤，硅胶外皮，头部与手臂的少量执行器由操作者的面部追踪驱动；曾在日本与丹麦的养老照护中测试。
- 视角: 亲密、照护与陪伴, 具身与动觉, 他异与恐怖谷
- 展出与获奖: RMIT Gallery, Melbourne
- 论文: https://doi.org/10.1145/2048259.2048274 (ACM SIGGRAPH 2011 Emerging Technologies)
- 视频: https://www.youtube.com/watch?v=hKvsHU1hrxg
- 图片: http://www.geminoid.jp/img/robot/telenoid.jpg
- 项目主页: https://en.wikipedia.org/wiki/Telenoid_R1

#### 家庭紧张（Domestic Tension） — Wafaa Bilal (2007)
- 类型: 表演、舞蹈与音乐 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 遥控暴力对射击者像游戏，对目标却像战争，正如无人机战争。
- 作品内容: Bilal 在芝加哥一家画廊里生活了 30 天，全程由网络摄像头直播；网友可以随时瞄准并用彩弹枪射击他，他们这样做了数万次。
- 实现方式: 网络摄像头直播，加上一支通过网站和聊天室控制的机器人彩弹枪。
- 视角: 具身与动觉, 机器之眼
- 展出与获奖: FlatFile Galleries, Chicago (2007)
- 视频: https://www.youtube.com/watch?v=F_L6BC9O0rY
- 图片: http://wafaabilal.com/wp-content/uploads/2012/04/Domestic_Tension_Wafaabilal_1.jpg
- 项目主页: https://wafaabilal.com/domestic-tension/

#### PRoP（个人漫游临场）（PRoP (Personal Roving Presence)） — Eric Paulos (1998)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 远程在场不只需要视频：视线、手势和四处走动的能力，才让身体在社交上“在场”。
- 作品内容: 与 John Canny 合作：一台高大的移动机器人，屏幕显示远程用户的脸，配有摄像头、麦克风和指示臂，让人能在远方的建筑中漫游、张望、做手势与交谈。
- 实现方式: 轮式底座配视频屏、云台摄像头、音频和指示臂，经互联网远程操控。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 论文: https://doi.org/10.1145/274644.274686 (CHI 1998)
- 视频: https://www.youtube.com/watch?v=ypKd1pbDbds
- 项目主页: https://www.paulos.net/

#### 珍禽（Rara Avis） — Eduardo Kac (1996)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 远程在场把你放进另一具身体，置身其他物种之中，成为格格不入的那一个。
- 作品内容: 在养着约 30 只斑胸草雀的鸟舍里，停着一只远程机器人金刚鹦鹉；戴上 VR 头显的观众通过它的眼睛观看并转动它的头，网上用户也能透过它观看并借它的声音说话。
- 实现方式: 眼中装有立体摄像头的机器鹦鹉，与 VR 头显的头部追踪联动，视频和音频同时传到互联网。
- 视角: 机器环世界, 机器之眼, 具身与动觉
- 展出与获奖: Nexus Contemporary Art Center, Atlanta (1996)
- 图片: https://www.ekac.org/rara.avis.jpg
- 项目主页: https://www.ekac.org/raraavis.html

#### 分形的肉体（Fractal Flesh） — Stelarc (1995)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 基础设施、能源与供应链
- 核心想法: 身体可以分布在网络之中，同时被多个远方的行动者驱动。
- 作品内容: 在 Telepolis 活动中，巴黎、赫尔辛基和阿姆斯特丹的观众触碰屏幕上的 Stelarc 身体模型，远程刺激他在卢森堡的肌肉，让他在未经本人意志的情况下动起来。
- 实现方式: 异地的触摸屏界面经互联网向贴在艺术家身上的肌肉电刺激系统发送指令。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Telepolis, Luxembourg (1995)
- 视频: https://www.youtube.com/watch?v=N2VkOE_AgNI
- 项目主页: https://stelarc.org/

#### 远程花园（The Telegarden） — Ken Goldberg (1995)
- 类型: 艺术作品与装置 · 机器: 工业机械臂
- 核心想法: 远程照护依赖对机器和图像的信任：我真的给那株植物浇了水吗？
- 作品内容: 与 Joseph Santarromana 合作：一座种着活植物的小花园，九年间由数千名网民照料，他们只能在网页上看到它，通过工业机械臂播种和浇水。
- 实现方式: 花盆上方装有摄像头的 Adept-1 工业机械臂，通过网页界面控制，会员的操作都会被记录。
- 视角: 具身与动觉, 亲密、照护与陪伴, 机器环世界
- 展出与获奖: Ars Electronica Center, Linz (1996–2004)
- 视频: https://www.youtube.com/watch?v=vQE-qJ_aYPw
- 图片: https://upload.wikimedia.org/wikipedia/commons/3/31/Telegarden.jpg https://goldberg.berkeley.edu/garden/telegarden-8x6-72dpi.jpg
- 项目主页: https://goldberg.berkeley.edu/garden/Ars/

#### 蒂莉，遥控机器人娃娃（Tillie, the Telerobotic Doll） — Lynn Hershman Leeson (1995)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉, 监控与生物识别
- 核心想法: 会回望的物件把观看者变成被看者，也给远方的凝视赋予了身体。
- 作品内容: 一个以摄像机为眼睛的玩偶坐在展厅里；网上访客通过她的眼睛观看并转动她的头，从玩偶的视角看展厅。
- 实现方式: 玩偶眼中装有摄像头，头部可电动转动，画面传到网站，由用户控制观看方向。
- 视角: 机器之眼, 具身与动觉
- 视频: https://www.youtube.com/watch?v=_ZOIdUZueHc
- 项目主页: https://www.lynnhershman.com/

#### 墨丘利计划（The Mercury Project） — Ken Goldberg (1994)
- 类型: 研究原型 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 网络把实验室机器人变成公共的、共享的身体，也提出一个问题：我们远程看到的是真的吗？
- 作品内容: 最早可由任何人经网页控制的机器人之一：访客指挥机械臂向沙盒喷气，挖掘埋藏的物件，并通过摄像画面查看结果。
- 实现方式: 带摄像头和喷气嘴的工业机械臂，通过 Mosaic 浏览器界面和 CGI 脚本控制。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.1109/robot.1995.525358 (IEEE ICRA 1995)
- 项目主页: https://goldberg.berkeley.edu/

#### cyberSM — Stahl Stenslie (1993)
- 类型: 艺术作品与装置 · 机器: 义体与赛博格, 基础设施、能源与供应链
- 核心想法: 借机器进行的远程触碰，是网络亲密关系早期的问题：什么才算接触？
- 作品内容: 与 Kirk Woolford 合作：两名身处不同城市的参与者穿上装有刺激器的服装，在屏幕上触碰对方的三维身体模型，这些触碰以振动和电刺激的形式抵达对方皮肤。
- 实现方式: 带刺激器的紧身服、三维扫描的身体化身，以及异地之间的远程通信链路（ISDN）。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 视频: https://www.youtube.com/watch?v=E5TFZJzKbYI
- 项目主页: https://en.wikipedia.org/wiki/Stahl_Stenslie

#### 远程梦境（Telematic Dreaming） — Paul Sermon (1992)
- 类型: 艺术作品与装置 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 远程在场是用身体感受到的：人们对一只投影的手作出反应，仿佛它真能触碰到自己。
- 作品内容: 两张分处异地的双人床由视频连接：一张床上的人的影像被投射到另一张床上，于是陌生人“同床”而卧，触碰并逗弄彼此被投射的身体。
- 实现方式: 每张床上方各装摄像机与投影仪，经 ISDN 线路连接，监视器显示合成画面。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 展出与获奖: Kajaani, Finland (1992)
- 视频: https://www.youtube.com/watch?v=S4Wt16PnqeY
- 项目主页: https://en.wikipedia.org/wiki/Paul_Sermon

#### 鸭嘴兽（Ornitorrinco） — Eduardo Kac (1989)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人, 计算机视觉
- 核心想法: 在场可以被移置进一台小而缓慢的机器；远程身体是被共享的，而非被占有的。
- 作品内容: 一台以鸭嘴兽命名的小型远程机器人，由远方参与者通过普通电话线驾驶；他们通过它的摄像眼看周围环境，跨城市共享一具机器身体。
- 实现方式: 带摄像头的移动机器人，通过电话按键音控制，经电话线传回静态视频图像（与 Ed Bennett 合作）。
- 视角: 具身与动觉, 机器之眼
- 图片: https://www.ekac.org/ornitorrinco.color.jpg
- 项目主页: https://www.ekac.org/ornitorrinco.html

#### 空间之洞（Hole in Space） — Kit Galloway & Sherrie Rabinowitz (1980)
- 类型: 艺术作品与装置 · 机器: 基础设施、能源与供应链, 计算机视觉
- 核心想法: 通信链路变成了公共场所：人们一遇见远方的身体，就当场发明与之相处的方式。
- 作品内容: 连续三个晚上，真人大小的实时视频屏幕通过卫星把纽约林肯中心和洛杉矶世纪城购物中心的路人连接起来，没有任何标识或说明；陌生人、后来是家人，隔着大陆相遇。
- 实现方式: 双向卫星视频链路，两岸各在橱窗中安装摄像机和背投屏幕。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=QSMVtE1QjaU
- 项目主页: http://www.ecafe.com/getty/HIS/

#### 远程存在（TELESAR）（Telexistence (TELESAR)） — 馆暲 (1980)
- 类型: 研究原型 · 机器: 类人机器人, 义体与赛博格
- 核心想法: 机器人可以不被设计成另一个主体，而是人所“住进”的第二个身体。
- 作品内容: 馆暲提出的概念及其机器人系列：操作者戴上头戴显示器和触觉装置，通过远方的人形机器人去看、听和感受，仿佛身处它的身体中；2011 年的 TELESAR V 加入了精细触觉。
- 实现方式: 机器人头部的立体摄像头跟随操作者的头部运动；主从式手臂与手把力、振动和温度反馈给操作者。
- 视角: 具身与动觉, 机器环世界
- 论文: https://doi.org/10.1109/MCG.2016.6 (IEEE Computer Graphics and Applications, 2016)
- 视频: https://www.youtube.com/watch?v=5j_hdDzgGvc
- 图片: https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/Telesar%E2%85%A4%2C_telexistence_robot_by_Susumu_Tachi_Laboratory%2C_exhibited_at_Miraikan_%282015-06-15_03.58.07_by_Franklin_Heijnen%29.jpg/1280px-Telesar%E2%85%A4%2C_telexistence_robot_by_Susumu_Tachi_Laboratory%2C_exhibited_at_Miraikan_%282015-06-15_03.58.07_by_Franklin_Heijnen%29.jpg
- 项目主页: https://tachilab.org/en/about/telexistence.html

### 与机器共舞

为人与机器身体编排的舞蹈。

#### 秧BOT（Yang BOT） — 宇树科技, 张艺谋 (2025)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 由人形机器人表演的民间舞，把机器人身体变成数亿人观看的国家形象。
- 作品内容: 十六台身穿花棉袄的宇树 H1 人形机器人，与人类舞者一起在央视春晚上扭秧歌、转手绢，由张艺谋执导。
- 实现方式: 通过动作捕捉与强化学习习得的编舞，机器人与舞者同步，并配有转手绢的末端机构。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: CCTV Spring Festival Gala 2025
- 视频: https://www.youtube.com/watch?v=Ykiuz1ZdGBc
- 项目主页: https://technode.com/2025/01/29/unitree-robotics-humanoid-robots-steal-the-show-at-2025-cctv-spring-festival-gala-with-ai-powered-yangge-dance/

#### 非舞之舞（Nondance Dance） — Shinseungback Kimyonghun (2022)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉
- 核心想法: 要在机器的类别之外起舞，舞者得先弄懂机器是怎样看舞蹈的。
- 作品内容: 舞者表演时，一个视频识别 AI 在旁观看，只要认出“舞蹈”就会用声音或灯光提示。舞者设法找到对人而言仍是舞蹈、却不被机器识别为舞蹈的动作。
- 实现方式: 使用 Google Video AI 动作识别（2 万多个标签，含多种舞蹈类别）向舞者实时反馈。
- 视角: 机器之眼, 具身与动觉, 分类、偏见与监控
- 视频: https://vimeo.com/776909143
- 图片: https://djhznh41oxwef.cloudfront.net/works/nondance_dance/ssbkyh_Nondance_dance_01.png
- 项目主页: https://ssbkyh.com/works/nondance_dance/

#### 你爱我吗？（Do You Love Me?） — Boston Dynamics (2020)
- 类型: 电影与影像 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 编舞是让机器变得讨人喜欢的有力手段，也遮蔽了它们背后的工程、控制与用途。
- 作品内容: Atlas 人形机器人、Spot 机器狗和 Handle 机器人随 The Contours 1962 年的歌曲起舞，视频于 2020 年底发布，获得数千万次观看，也引发了关于舞蹈如何让机器人显得“快乐”的讨论。
- 实现方式: 与编舞家 Monica Thomas 在 Boston Dynamics 的编舞软件中共同编写动作序列，由机器人自身的平衡控制执行，分段拍摄剪辑而成。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=fn3KWM1kuAw
- 项目主页: https://bostondynamics.com/

#### 梅里特 + 机器人（Merritt + Robot） — Merritt Moore (2020)
- 类型: 电影与影像 · 机器: 工业机械臂
- 核心想法: 在隔离中，一只可编程机械臂成了舞伴；这段双人舞也是舞者与自己代码之间的排练。
- 作品内容: 2020 年封城期间，舞者兼物理学家 Merritt Moore 把一台 Universal Robots 机械臂编程为唯一的舞伴，拍下一段双人舞：机器人时而引领、时而跟随。
- 实现方式: 由舞者亲自编程的协作机械臂（Universal Robots）。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=uSOHc3ODLzU
- 图片: https://images.squarespace-cdn.com/content/v1/66c15199c6b23b75923ac311/b4ae89c2-ea53-41f0-82e8-2d95034920ed/Merritt_Moore_robots_Mexico.png
- 项目主页: https://www.merrittmoore.com/

#### 活档案（Living Archive） — Wayne McGregor (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 数据集与训练数据, 计算机视觉
- 核心想法: 编舞家的风格被做成模型后，成了一个会提出“他的”下一步动作的伙伴。
- 作品内容: Google Arts & Culture 用 McGregor 二十五年编舞的数千小时视频训练模型；给出舞者的一个姿势，它就提出接下来可能的动作，这些片段被搬上舞台，成为《活档案：一场 AI 表演实验》。
- 实现方式: 对档案视频做姿态估计，再用神经网络预测身体姿态序列；舞者学习并改编这些提议。
- 视角: 能动、自主与共创, 具身与动觉
- 展出与获奖: The Music Center, Los Angeles (2019)
- 视频: https://www.youtube.com/watch?v=Hd3BDvfmg4k
- 图片: https://lh3.googleusercontent.com/UAE2Fk3CoTgjTWKg9PiFGU6XjasBWnRO5g2xP_LHAHZZVVgfPCx3K3BKv58VuXW9hErbCpVgYhBUk1iAzprsgTkX_eTl
- 项目主页: https://experiments.withgoogle.com/living-archive-wayne-mcgregor

#### 输出（OUTPUT） — Catie Cuan (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂
- 核心想法: 编舞可以成为机器人的设计方法：舞蹈研究一台机器的动作怎样才会被读作有表现力。
- 作品内容: Cuan 与一台 ABB IRB 6700 工业机器人共舞，之后两具身体的动作被记录下来，以动作捕捉、视频和网页应用的形式重放，让每个身体的运动被转译进对方的媒介。
- 实现方式: 依据 Cuan 的动作为机器人编程，用动作捕捉记录，并在视频与交互软件中重组。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.3389/frobt.2020.576790 (Frontiers in Robotics and AI 2021)
- 视频: https://www.youtube.com/watch?v=Ng0ioS7oNXY
- 项目主页: https://www.catiecuan.com/

#### 离散形体（discrete figures） — Rhizomatiks, ELEVENPLAY, 真锅大度 (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉, 生成模型与潜空间, 自动驾驶与无人机
- 核心想法: 舞者面对由自己动作训练出的模型，看见机器如何抽象一个身体。
- 作品内容: 一部舞台作品：舞者与机器生成的“舞者”同台，用他们的动作训练的模型生成新动作，以投影人形和携带屏幕的无人机呈现。
- 实现方式: 用 ELEVENPLAY 舞者的动作捕捉数据训练生成模型；实时追踪让投影与无人机和表演者对齐；与 Kyle McDonald 合作。
- 视角: 机器之眼, 具身与动觉, 能动、自主与共创
- 展出与获奖: Spiral Hall, Tokyo 2018; Gray Area, San Francisco
- 视频: https://www.youtube.com/watch?v=hauXQQhwbgM
- 图片: https://research.rhizomatiks.com/s/works/discrete_figures/images/video_image.jpg
- 项目主页: https://research.rhizomatiks.com/s/works/discrete_figures/en/

#### 共（AI）存（Co(AI)xistence） — Justine Emard (2017)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 把会学习的仿人机器人当作另一种智能，寻找双方都能共享的语言。
- 作品内容: 一件 12 分钟的影像装置：表演者森山未来与仿人机器人 Alter 试图通过手势、信号和语言交流，Alter 在交流中不断学习。
- 实现方式: 拍摄舞者与 Alter（大阪大学石黑实验室与东京大学池上实验室开发）的即兴互动，Alter 的动作由神经网络和传感器输入驱动。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: AI: More than Human, Barbican, London 2019
- 视频: https://www.youtube.com/watch?v=vcdUTEpSV1s
- 项目主页: https://justineemard.com/coaixistence/

#### 24架无人机（24 drones） — Rhizomatiks, ELEVENPLAY, 真锅大度 (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 自动驾驶与无人机
- 核心想法: 编舞可以包括机器身体，而它们的精确反过来暴露了舞者自身的节奏。
- 作品内容: 五位舞者与 24 架小型无人机同台，无人机在舞者周围与之间编队飞行，成为群舞的一部分。
- 实现方式: 室内动作捕捉系统追踪无人机与舞者；飞行轨迹在软件中预先模拟，并与音乐和灯光同步。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=SPcZmDTW8KU
- 图片: https://research.rhizomatiks.com/s/works/24drones/img/drone_00.png
- 项目主页: https://research.rhizomatiks.com/s/works/24drones/en/

#### chor-rnn — Louise Crnkovic-Friis, Luka Crnkovic-Friis (2016)
- 类型: 研究原型 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 看模型学跳舞，会让“风格”在机器眼中的含义变得可见：关节的统计规律。
- 作品内容: 一个循环神经网络用一位当代舞者数小时的动作捕捉数据训练，学会生成她风格的新编舞；公开的视频展示了随着训练推进，它如何从抽搐般的噪声变成类似舞蹈的片段。
- 实现方式: 混合密度 LSTM 网络，用编舞家即兴动作的 Kinect 动作捕捉关节位置数据训练。
- 视角: 能动、自主与共创, 具身与动觉, 不透明与潜空间
- 论文: https://arxiv.org/abs/1605.06921 (arXiv 2016)
- 视频: https://www.youtube.com/watch?v=Q4_XSMqN8w0

#### TED2014 上的仿生舞蹈（与阿德里安娜·哈斯利特-戴维斯）（Bionic dance at TED2014 (with Adrianne Haslet-Davis)） — Hugh Herr (2014)
- 类型: 研究原型 · 机器: 义体与赛博格
- 核心想法: 义体可以为表达而设计：依照舞者的运动方式调校，而不只是为了行走。
- 作品内容: 在 2013 年波士顿马拉松爆炸案中失去左小腿的国标舞者 Adrianne Haslet-Davis，在 TED2014 舞台上穿着 Hugh Herr 实验室打造的仿生腿跳了一段伦巴。
- 实现方式: 带电机与传感器的动力踝足假肢，依据采集的舞者运动数据调校。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=CDsNZJTWw0w
- 图片: https://pi.tedcdn.com/r/pe.tedcdn.com/images/ted/ca0520623aeb359f6d5f371d516371fadcae2454_1600x1200.jpg?u%5Br%5D=2&u%5Bs%5D=0.5&u%5Ba%5D=0.8&u%5Bt%5D=0.03&quality=82&w=1200
- 项目主页: https://www.ted.com/talks/hugh_herr_the_new_bionics_that_let_us_run_climb_and_dance

#### 机器人（ROBOT） — Blanca Li (2013)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 把人和机器人放进同一段编舞，显露出我们的动作中已有多少是机械的。
- 作品内容: 八名舞者与七台小型 NAO 类人机器人以及明和电机的音乐机器同台；人像机器人一样动，机器人则尝试跳人的舞。
- 实现方式: 预设编舞程序的 NAO 机器人（Aldebaran），配合明和电机的乐器与现场舞者。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Montpellier Danse (2013)
- 视频: https://www.youtube.com/watch?v=vrH0Ydj3HN4
- 项目主页: https://www.blancali.com/en/spectacle/robot-2/

#### 黄翊与库卡（Huang Yi & KUKA） — 黄翊 (2012)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂
- 核心想法: 一分钟一分钟地为机器人编程，成了在机器之镜中凝视自己孤独的方式。
- 作品内容: 黄翊与一台他亲自编程的 KUKA 工业机械臂的双人舞，后来发展为整晚演出；机械臂携带灯光，模仿他的动作，以缓慢而贴近的编舞与他共舞。
- 实现方式: 手工编程的 KUKA 工业机械臂（每分钟编舞需 10–20 小时编程），末端装有灯光或摄像机。
- 视角: 具身与动觉, 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: Ars Electronica Festival 2013; TED2017, Vancouver; Toured 20 countries
- 视频: https://www.youtube.com/watch?v=Xy6tPmFlN34
- 图片: https://huangyistudio.com/wp-content/uploads/2022/10/huangyiandkuka_TED2017_01.jpg https://upload.wikimedia.org/wikipedia/commons/5/51/Prix_Ars_Electronical_2013_11_Huang_Yi_KUKA.jpg
- 项目主页: https://huangyistudio.com/archives/project/huang-yi-and-kuka

#### 人类界面（Human Interface） — Thomas Freundlich (2012)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂
- 核心想法: 安全围栏一旦拆除，工厂机器人就能被读作一个“个性”，而不是工具。
- 作品内容: 一部为两名舞者和两台工业机器人创作的舞蹈，在赫尔辛基电缆工厂的旧锅炉大厅演出；机器人被编程的动作精确却出奇地有人味，它们以平等舞伴的身份出现。
- 实现方式: 由编舞家亲自编程的 ABB 工业机器人，配合允许人进入机器人工作区的安全系统；延续他 2008 年的双人舞《Actuator》。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Zodiak Center for New Dance, Helsinki (2012)
- 视频: https://www.youtube.com/watch?v=MCSUVI--0Sw
- 项目主页: http://www.freundlich.org/

#### 优雅状态机（Grace State Machines） — Bill Vorn (2007)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 义体与赛博格
- 核心想法: 当机器人依据人体内部信号而动时，两具身体之间的界线本身就成了编舞。
- 作品内容: 表演者 Emma Howes 与一台机器人之间长 27 分钟的舞台二重奏：她的动作和体内状态被捕捉并转移到机器身体上，两者在不断变化的共生对话中一起运动。
- 实现方式: 舞者身上的动作捕捉和生物反馈传感器实时驱动机器人的执行器（与 Jonathan Villeneuve 合作）。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=b6TiJdGRMTw
- 图片: https://billvorn.concordia.ca/robography/images/GSMBB.jpg
- 项目主页: https://billvorn.concordia.ca/robography/GraceState.html

#### 辉光（Glow） — Gideon Obarzanek, Frieder Weiss (2006)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉
- 核心想法: 机器视觉可以是舞台伙伴：舞者既为观众表演，也为摄像机对她的“读取”表演。
- 作品内容: 一名独舞者在白色地面上舞动，红外摄像机追踪她的身体，计算机实时投射图形作出回应，用光包裹、拉伸并追逐她的形体。
- 实现方式: 红外视频追踪舞者（Frieder Weiss 的 Kalypso 软件），在地面生成投影图形。
- 视角: 机器之眼, 具身与动觉
- 视频: https://www.youtube.com/watch?v=C4He543_a80
- 项目主页: https://chunkymove.com.au/

#### 舞者 #1（DANCER #1） — Kris Verdonck (2003)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 一台机器努力运转的挣扎，就足以让人把它看作舞者并为它动容。
- 作品内容: 一只挂着巨大钢制“L”的砂轮从天花板垂下；电机启动后，L 失控旋转，机器仍努力寻找平衡，直到它看起来像一位陷入困境的悲剧英雄。
- 实现方式: 带偏心钢构件的工业磨削电机，在剧场空间中按时长运行表演。
- 视角: 失败、故障与错误, 具身与动觉, 他异与恐怖谷
- 展出与获奖: Kunstenfestivaldesarts, Brussels (2003); Festival d'Avignon (2008)
- 视频: https://www.youtube.com/watch?v=xKbBImj3mWM
- 图片: https://www.atwodogscompany.org/media/og/17-dancer_krisverdonckhigh.jpg
- 项目主页: https://www.atwodogscompany.org/en/projects/dancer-1/

#### 区域（Zone） — Pablo Ventura, robotlab (2001)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂
- 核心想法: 舞台上的工厂机械臂是一位解剖结构不同的舞者，而非道具。
- 作品内容: 一台 KUKA 工业机器人由 robotlab 协助编程，作为 Ventura Dance Company 的一员，与人类舞者一起出演一部当代舞作品。
- 实现方式: KUKA 工业机器人，离线编写编舞程序，与舞者和音乐同步。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=PD1i6rItAfA
- 项目主页: https://www.ventura-dance.com/

#### 双足（BIPED） — Merce Cunningham, Paul Kaiser, Shelley Eshkar (1999)
- 类型: 表演、舞蹈与音乐 · 机器: 计算机视觉, 类人机器人
- 核心想法: 被捕捉的动作变成第二支无重量的舞团，与舞者一起、又彼此分离地起舞。
- 作品内容: 舞者在一块透明纱幕后表演，纱幕上投射出大型、仿佛手绘的形象，它们由 Cunningham 舞者的动作捕捉数据生成，于是活的身体与其数字痕迹同台共舞。
- 实现方式: 对舞者进行光学动作捕捉，由 Kaiser 和 Eshkar 渲染成抽象线条形象投射在纱幕上；音乐由 Gavin Bryars 创作。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Zellerbach Hall, Berkeley (1999)
- 视频: https://www.youtube.com/watch?v=b_XItg0Vn1c
- 项目主页: https://www.mercecunningham.org/the-work/choreography/biped/

#### 捕捉幽灵（Ghostcatching） — Bill T. Jones, Paul Kaiser, Shelley Eshkar (1999)
- 类型: 艺术作品与装置 · 机器: 计算机视觉
- 核心想法: 动作捕捉把动作与动作者分离；留下的是舞者自己可以观看的幽灵。
- 作品内容: 一段由 Bill T. Jones 即兴动作捕捉生成的虚拟舞蹈：他的动作化为手绘线条，不断增殖、碰撞，被困在一个盒子里，一个没有身体的舞者。
- 实现方式: 对 Jones 的即兴进行光学动作捕捉，以三维动画渲染为手绘风格的笔触。
- 视角: 具身与动觉, 哀悼、记忆与来世
- 视频: https://www.youtube.com/watch?v=x-7Mo3cg9jw
- 项目主页: https://openendedgroup.com/

#### 追踪者（使用 LifeForms）（Trackers (with LifeForms)） — Merce Cunningham (1991)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 一具没有重量与习惯的虚拟身体提出动作，人的身体随后必须学会栖居其中。
- 作品内容: Cunningham 用软件 LifeForms 创作的第一支舞：他先在电脑上的三维动画人偶上编排动作序列，再要求舞者完成此前从未有身体尝试过的动作。
- 实现方式: LifeForms 是西蒙弗雷泽大学（Tom Calvert、Thecla Schiphorst 等）开发的编舞软件，用于在三维中为人形设关键帧。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.1145/169059.169113 (CHI 1993)
- 项目主页: https://www.mercecunningham.org/

### 机器剧场

机器人和 AI 作为舞台上的演员、角色与导演。

#### 带火者普罗米修斯（Prometheus Firebringer） — Annie Dorsen (2023)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 生成模型与潜空间
- 核心想法: 生成式 AI 以“平均”的方式“复原”过去；这部作品把这种损失与机器的流畅并置于舞台。
- 作品内容: 语言模型生成埃斯库罗斯失传剧作的“复原本”，由 AI 生成的面具与声音演出；与此同时，Dorsen 本人发表讲演，讨论这类系统从人类文化中拿走了什么。
- 实现方式: 大语言模型（GPT-3.5）生成剧本，配合生成的面具图像与合成语音，同时进行真人现场讲演。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 展出与获奖: Theatre for a New Audience, New York (2023)
- 视频: https://www.youtube.com/watch?v=CKDwPyJaESk
- 图片: https://anniedorsen.com/wp/wp-content/uploads/2023/04/Copy-of-Prometheus_Firebringer_Baranova-2869-1900x1267.jpg
- 项目主页: https://anniedorsen.com/projects/prometheus-firebringer/

#### AI：当机器人写剧本（AI: When a Robot Writes a Play） — THEaiTRE (2021)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 类人机器人
- 核心想法: 一部由机器写成的机器人“自传”，既显示模型从人类戏剧中借来了什么，也显示它在哪里失去了线索。
- 作品内容: 为纪念 R.U.R. 百年，查理大学与布拉格剧院的团队用 GPT-2 生成了剧本的大部分内容，讲述一个机器人面对出生、死亡、爱与孤独；2021 年 2 月在 Švandovo 剧院线上首演。
- 实现方式: GPT-2 根据人写的提示生成对白，在定制工具中由人筛选与编辑，由职业演员演出。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 论文: https://arxiv.org/abs/2006.14668 (arXiv 2020)
- 视频: https://www.youtube.com/watch?v=8ho5sXiDX_A
- 图片: https://www.theaitre.com/wp-content/uploads/THEaiTRE_PLAKAT_FINAL_web-e1614159078389.jpg
- 项目主页: https://www.theaitre.com/

#### 人类学习 #4：课堂（Human Study #4, La Classe） — Patrick Tresset (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 工业机械臂
- 核心想法: 笨拙的机器人上演学校纪律，让人看见机器与孩子都在被训练成顺从的样子。
- 作品内容: 二十一台绘画机器人坐在课桌前扮演老师和学生；在十五分钟的演出里，它们用变形的摩尔斯电码喧哗、被逐一点名、练习画直线和计数划记，短暂造反后又重新服从。
- 实现方式: RNP 型机器人各有一支握笔的机械臂和一个小摄像头“头部”，在教室布景中执行半生成的声音与绘图编排。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Merge Festival, London 2019 (with Tate Modern); Prix Ars Electronica 2019, Honorary Mention (Artificial Life & Intelligence)
- 视频: https://www.youtube.com/watch?v=znI6reVdN_M
- 图片: https://archive.aec.at/asset/2689289/preview/ https://archive.aec.at/asset/2689291/preview/
- 项目主页: https://archive.aec.at/prix/244883/

#### 内脏（Eingeweide） — Marco Donnarumma, Margherita Pevere (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 类人机器人
- 核心想法: 混成身体可以同时是机器的、微生物的和人的，而没有一方完全掌控。
- 作品内容: 一部舞蹈剧场作品：两名表演者（其中一人戴着 AI 驱动的机器人面部义体）彼此挣扎、交融，并与活体细菌纤维素膜纠缠。
- 实现方式: 机器人面部义体由神经网络控制，响应表演者的肌肉信号；舞台上的膜由细菌培养而成。
- 视角: 具身与动觉, 他异与恐怖谷
- 展出与获奖: Romaeuropa Festival, Rome (2018)
- 视频: https://www.youtube.com/watch?v=6P0Vsg81Om0
- 项目主页: https://7c.marcodonnarumma.com/

#### Improbotics — Piotr Mirowski, Kory Mathewson (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型
- 核心想法: 即兴表演暴露了语言模型作为搭档所缺的东西：倾听、对场景的记忆与节奏。
- 作品内容: 一个即兴剧团：其中一名演员作为“赛博格”，说出语言模型经耳机实时生成的台词，其他演员与观众则猜谁在被机器喂词，一场舞台上的图灵测试。
- 实现方式: 语音识别把台词输入对话模型，模型的回复通过耳机传给真人“赛博格”或显示在屏幕上。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 论文: https://arxiv.org/abs/1809.01807 (arXiv 2018)
- 视频: https://www.youtube.com/watch?v=ICUoJBRNkkU
- 图片: https://i0.wp.com/improbotics.org/wp-content/uploads/2019/11/improbotics_rosettacode_voilaeurope_2019nov8_markhambelton_dsc0219-2-e1573434690902.jpg?fit=1200%2C762&ssl=1
- 项目主页: https://improbotics.org/

#### 恐怖谷（Uncanny Valley (Unheimliches Tal)） — Rimini Protokoll, Thomas Melle (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 机器人替身能比本人更坦率地谈论自我，也让观众追问：自己究竟在为谁动容。
- 作品内容: 作家 Thomas Melle 的电子动画复制品独自坐在舞台上，讲述他的双相障碍、Alan Turing 与替身，而真正的 Melle 并不在场。
- 实现方式: 依据 Melle 的翻模与扫描制作的硅胶电子动画人偶，配以预录声音与编程的面部和手部动作。
- 视角: 他异与恐怖谷, 具身与动觉
- 展出与获奖: Münchner Kammerspiele (2018)
- 视频: https://www.youtube.com/watch?v=7dOnjW5sQPk
- 项目主页: https://www.rimini-protokoll.de/website/en/project/unheimliches-tal-uncanny-valley

#### 布谷（Cuckoo） — Jaha Koo (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器, 社交与陪伴机器人
- 核心想法: 当告诉你“饭好了”的是电饭煲的声音，家用电器便成了孤独的陪伴者。
- 作品内容: 具滋夏与三台会说话的“Cuckoo（布谷）”牌电饭煲同台演出。借着它们的闲聊，他讲述自 1997 年金融危机以来韩国 20 年的历史，以及他这一代人的孤立感。
- 实现方式: 改装的会说话电饭煲，配以编程的语音与灯光，结合纪实影像与现场音乐。
- 视角: 亲密、照护与陪伴, 机器之耳与声
- 展出与获奖: steirischer herbst, Graz 2017 (premiere); Festival d'Automne à Paris; SIFA 2023
- 视频: https://www.youtube.com/watch?v=JmC02twjeDU
- 项目主页: https://en.wikipedia.org/wiki/Jaha_Koo

#### 我是 Echoborg（I Am Echoborg） — Rik Lander, Phil D. Hall (2016)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型
- 核心想法: 把机器的话放进人的嘴里，暴露出我们在多大程度上凭身体来判断心智。
- 作品内容: 一名真人表演者只说出聊天机器人通过耳机传来的话；观众志愿者与这个“回声人”对话，尝试与它一起想清楚人与机器该如何共处。
- 实现方式: 定制对话代理，其输出转为语音传给真人说出（源自社会心理学的“回声人”方法）。
- 视角: 他异与恐怖谷, 机器之耳与声, 具身与动觉
- 论文: https://doi.org/10.3389/fpsyg.2015.00634 (Frontiers in Psychology 2015)
- 视频: https://www.youtube.com/watch?v=Wh5QASc7PFY
- 图片: https://echoborg.com/img/E7b_1920x1008_3_og.jpg
- 项目主页: https://echoborg.com/

#### 挑棒游戏：一个爱情故事（Spillikin: A Love Story） — Pipeline Theatre (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 照护机器人也可以是逝者留下的记忆与爱的容器。
- 作品内容: 一部关于患阿尔茨海默病的 Sue 的戏：她已故的丈夫是一位机器人专家，造了一台类人机器人陪伴她、记住他们的共同生活；这台机器人与四名演员同台演出。
- 实现方式: 由 Engineered Arts 制造的 RoboThespian 类人机器人，按每场演出的提示与台词编程。
- 视角: 亲密、照护与陪伴, 哀悼、记忆与来世
- 展出与获奖: Edinburgh Festival Fringe, Pleasance (2015)
- 视频: https://www.youtube.com/watch?v=CeoxJ2ZWRd0
- 图片: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_40jqdrnd3v8v183r6r55fsabms/e6f52ab8f37f9350171e05627b93dfdc_1790197362113.png
- 项目主页: https://www.pipelinetheatre.com/spillikin

#### 一件杰作（A Piece of Work） — Annie Dorsen (2013)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型, 语音与听觉机器
- 核心想法: 当机器演绎经典，“人是多么了不起的杰作”变成关于模式而非人物的问题。
- 作品内容: 算法版《哈姆雷特》：每晚由计算机程序剪切、重排和混编莎士比亚的文本，由合成语音说出，部分场景由一位演员念出，灯光与声音也由代码控制。
- 实现方式: 对《哈姆雷特》实时运用马尔可夫链等文本算法，配合语音合成与生成式灯光提示。
- 视角: 能动、自主与共创, 机器之耳与声
- 图片: https://anniedorsen.com/wp/wp-content/uploads/2020/09/Annie-Dorsen_A-Piece-of-Work_revengepic_photo-by-Bruno-Pocheron-1900x1069.jpg
- 项目主页: https://anniedorsen.com/projects/piece-of-work/

#### 三姐妹（仿真人版）（Three Sisters, Android Version） — 平田织佐, 石黑浩 (2012)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 一个家庭可以与“在场却缺席”之人的仿真人替身一起生活。
- 作品内容: 平田织佐改编契诃夫的剧作，背景是一座衰落的日本工业城镇：闭门不出的小妹在家中被一个以她为原型的仿真人取代。
- 实现方式: 仿真人（Geminoid F）和一台 Robovie 机器人与人类演员同台；仿真人的语言与动作由后台操作和控制节奏。
- 视角: 他异与恐怖谷, 哀悼、记忆与来世
- 展出与获奖: Théâtre Varia, Brussels
- 视频: https://www.youtube.com/watch?v=-8dhuoT8BkA
- 项目主页: https://thetheatretimes.com/the-gaze-of-the-robot/

#### 演员 #1（ACTOR #1） — Kris Verdonck (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 类人机器人
- 核心想法: 演员可以是任何能在舞台上吸引注意的东西；一台机器的跌倒也能承载悲怆。
- 作品内容: 一部三段式作品，检验“演员”是什么：一个由雾构成的形体、一个人偶般的表演者、一台不断跌倒的机器人，它们都在没有人类演员的舞台上“表演”。
- 实现方式: 舞台机械、烟雾效果与被编程为反复跌倒的机器人形体，在没有人类演员的情况下演出。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 视频: https://www.youtube.com/watch?v=BtGwRJsq4ig
- 项目主页: https://www.atwodogscompany.org/en/projects/actor-1/

#### Data，机器人单口喜剧演员（Data, the robot stand-up comedian） — Heather Knight (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 喜剧是对机器社交能力的检验：节奏与察言观色比笑话本身更难。
- 作品内容: 一台名为 Data 的小型 NAO 机器人表演单口喜剧，并根据观众的笑声与掌声选择下一个笑话；首演于 TEDWomen 2010。
- 实现方式: 带笑话数据库的 NAO 类人机器人；根据音频与观众反馈决定下一个笑话。
- 视角: 机器之耳与声, 他异与恐怖谷
- 论文: https://doi.org/10.1007/978-3-642-25504-5_5 (ICSR 2011)
- 视频: https://www.youtube.com/watch?v=Fu_kBW_KSms
- 图片: https://pi.tedcdn.com/r/pe.tedcdn.com/images/ted/2f8bd657fb5e99e575ec030ddd925a8a782724e5_800x600.jpg?u%5Br%5D=2&u%5Bs%5D=0.5&u%5Ba%5D=0.8&u%5Bt%5D=0.03&quality=82&w=1200
- 项目主页: https://www.ted.com/talks/heather_knight_silicon_based_comedy

#### 死亡与力量（Death and the Powers） — Tod Machover (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 基础设施、能源与供应链
- 核心想法: 如果一个人能在建筑的机器中继续存在，问题就变成：家人还能触及他吗？
- 作品内容: 一部机器人歌剧：垂死的亿万富翁把自己上传进“系统”，也就是他的房子；舞台本身，连同一群机器人“Operabots”、会移动的书墙和会奏乐的吊灯，成了他的新身体。
- 实现方式: MIT 媒体实验室的舞台机器人（Operabots、机器人墙体），由对歌手声音和身体的“去身体化表演”感知驱动。
- 视角: 哀悼、记忆与来世, 具身与动觉
- 展出与获奖: Opéra de Monte-Carlo (2010); Pulitzer Prize finalist (2012)
- 视频: https://www.youtube.com/watch?v=mPp9juefl2Y
- 项目主页: https://en.wikipedia.org/wiki/Death_and_the_Powers

#### 哈喽，嗨，你好（Hello Hi There） — Annie Dorsen (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 聊天机器人与语言模型
- 核心想法: 看机器辩论人性，会发现语言可以在无人“意指”的情况下被生产出来。
- 作品内容: 两台笔记本电脑上的两个聊天机器人现场对话，其语料来自 1971 年 Noam Chomsky 与 Michel Foucault 关于人性的电视辩论；每场演出都不一样。
- 实现方式: 定制的聊天机器人程序，配合文本语料（辩论及其他来源）、语音合成与投影文字。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: steirischer herbst, Graz (2010)
- 视频: https://www.youtube.com/watch?v=3PiwEQQNnBk
- 图片: https://anniedorsen.com/wp/wp-content/uploads/2020/08/hellohi_silveri4519-e1608324384987.jpg
- 项目主页: https://anniedorsen.com/projects/hello-hi-there/

#### 再见（Sayonara） — 平田织佐, 石黑浩 (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 仿真人能陪伴人走向死亡，恰恰因为它不会一同死去。
- 作品内容: 一出短剧：仿真人 Geminoid F 为一位将死的年轻女子朗诵诗歌；2012 年版本让仿真人去福岛禁区为亡者读诗。
- 实现方式: Geminoid F 的声音与表情由后台操作员远程控制，与演员 Bryerly Long 对戏。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴, 他异与恐怖谷
- 展出与获奖: Ars Electronica 2011; Arts Centre Melbourne
- 视频: https://www.youtube.com/watch?v=8C_9MQ8N9JE
- 图片: https://thetheatretimes.com/wp-content/uploads/2018/03/09_t_madoka_nishiyama.jpg
- 项目主页: https://thetheatretimes.com/the-gaze-of-the-robot/

#### 终（END） — Kris Verdonck (2008)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 监控与生物识别
- 核心想法: 当人不再是舞台中心，机器与物件也能承载“终结”的戏剧。
- 作品内容: END 用十个场景呈现人类社会可能的终局，取材于媒体中融化的冰川、燃烧的森林、窥视我们的摄像头与武器；表演者、物件与机器以同等的存在感共享舞台。
- 实现方式: 结合表演者、机械物件、投影与机器驱动舞台元素的剧场装置，共十个场景。
- 视角: 他异与恐怖谷, 失败、故障与错误
- 展出与获奖: Kunstenfestivaldesarts, Brussels (2008); Kampnagel, Hamburg (2008)
- 视频: https://www.youtube.com/watch?v=jbtwrPjuc0U
- 图片: https://www.atwodogscompany.org/media/og/149-endcreinouthiel.jpg
- 项目主页: https://www.atwodogscompany.org/en/projects/end/

#### 工作的我（I, Worker (Hataraku Watashi)） — 平田织佐, 石黑浩 (2008)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 一台拒绝工作的机器人，映照出人的抑郁与劳动。
- 作品内容: 一出 30 分钟的戏：一对夫妻与两台家用机器人同住，其中一台失去了工作的意愿；机器人与人类演员同台演出。
- 实现方式: 商用人形机器人按预先编程的台词和动作演出，与人类演员精确配合；这是青年团与大阪大学“机器人-人类剧场”的第一部作品。
- 视角: 隐形劳动与攫取, 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: Japan Society, New York
- 视频: https://www.youtube.com/watch?v=58MlpKX-JWQ
- 项目主页: https://thetheatretimes.com/the-gaze-of-the-robot/

#### 失语症（Afasia） — Marcel·lí Antúnez Roca (1998)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格, 机器生物与移动机器人
- 核心想法: 表演者成了控制台：一具身体指挥一支机器乐队，故事通过这种操控被讲述。
- 作品内容: 一人演出的机电版《奥德赛》：Antúnez 身穿外骨骼，用自己的身体指挥四台音乐机器人、投影影像与声音，全程不用语言。
- 实现方式: 带传感器的“Dreskeleton”身体界面把信号传给软件，驱动机器人吉他、鼓、风笛和小提琴，以及互动影像。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=MJan5KPX050
- 图片: https://www.marceliantunez.com/media/cache/ee/b8/eeb8aba209de3a0770ed94a45f3dd37d.jpg
- 项目主页: https://www.marceliantunez.com/work/afasia/

#### 罗素姆万能机器人（R.U.R. (Rossum's Universal Robots)） — Karel Čapek (1921)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人
- 核心想法: 最早的机器人被想象为工人：“机器他者”的观念诞生于一个关于劳动的问题。
- 作品内容: Čapek 的剧本以一座批量生产人造工人“roboti”的工厂为背景，这些工人被销往全球，随后反叛并毁灭人类；它在布拉格国家剧院的首演让“机器人”一词进入世界语言。
- 实现方式: 舞台剧；剧中的机器人是由生化方法制造的人造人，由真人演员扮演。
- 视角: 隐形劳动与攫取, 他异与恐怖谷
- 展出与获奖: National Theatre, Prague (1921)
- 图片: https://upload.wikimedia.org/wikipedia/commons/8/87/Capek_play.jpg
- 项目主页: https://en.wikipedia.org/wiki/R.U.R.

### 机器音乐与共同即兴

会聆听并与音乐家一起演奏的机器，以及与模型共享的声音。

#### 早期音乐迟来选集 第一卷：从古代到文艺复兴（A Late Anthology of Early Music Vol. 1: Ancient to Renaissance） — Jennifer Walshe, Dadabots (2020)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 语音与听觉机器, 数据集与训练数据
- 核心想法: AI 可以被听作一个带着自己口音的新音乐时期，而非完美的模仿者。
- 作品内容: 一张“早期音乐”专辑，从古希腊到文艺复兴，由与 Dadabots 共同构建的 Walshe 声音 AI 模型演唱；听起来像是一台正在学唱歌的机器重述音乐史。
- 实现方式: 用 Walshe 的声音录音训练的原始音频神经网络（可能是 Dadabots 常用的 SampleRNN 类）。
- 视角: 机器之耳与声, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=RrZedzc1TbM
- 项目主页: http://milker.org/

#### Chain Tripping — YACHT (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 与模型合作也是具身劳动：人必须学会演奏机器的笨拙。
- 作品内容: YACHT 用自己的旧作训练模型，生成歌词与旋律，然后在严格规则下亲自演奏这些片段；机器怪异的乐句很难演奏，这种“计算机口音”后来成为一部纪录片的主题。
- 实现方式: 用乐队旧作训练的符号音乐模型（MusicVAE）与文本模型，由人演奏编配，不额外添加音符。
- 视角: 能动、自主与共创, 失败、故障与错误
- 展出与获奖: Grammy nomination, Best Immersive Audio Album (2020)
- 视频: https://www.youtube.com/watch?v=yi7mnmBqNmg
- 图片: https://teamyacht.com/yacht-banner.png
- 项目主页: https://teamyacht.com/

#### PROTO（与 Spawn 合作）（PROTO (with Spawn)） — Holly Herndon, Mat Dryhurst (2019)
- 类型: 表演、舞蹈与音乐 · 机器: 生成模型与潜空间, 语音与听觉机器
- 核心想法: 模型可以由一个社群“养大”，而不是用抓取的数据训练；它的声音也因此属于这个合唱团。
- 作品内容: 一张与 Spawn 合作的专辑：Spawn 是 Herndon 和 Dryhurst 用自己及一个合唱团的声音训练的神经网络“AI 宝宝”；它粗糙、未成形的声音在人声合唱中歌唱。
- 实现方式: 用 Herndon 与合唱团录音训练的神经网络声音模型，在现场和录音室中用于音色迁移和一唱一和。
- 视角: 机器之耳与声, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=sc9OjL6Mjqo
- 项目主页: https://www.hollyherndon.com/

#### 可怖之美（Scary Beauty） — 涩谷庆一郎, 池上高志, 石黑浩 (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 控制论与人工生命系统
- 核心想法: 当机器来指挥，人类必须跟随一个时间感并非人类的身体。
- 作品内容: 一部“仿真人歌剧”：仿真人 Alter 2 指挥人类管弦乐团并演唱，速度与强弱由它自己决定。
- 实现方式: Alter 的人工生命神经网络实时生成手势与速度；歌词取自 Houellebecq 等人的文本；在东京未来馆首演。
- 视角: 能动、自主与共创, 他异与恐怖谷, 具身与动觉
- 展出与获奖: Miraikan, Tokyo 2018; New National Theatre Tokyo
- 视频: https://www.youtube.com/watch?v=ePIYMN6gbzs
- 图片: https://realtokyo.co.jp/_sys2024/wp-content/uploads/2018/08/main.jpg
- 项目主页: https://realtokyo.co.jp/en/performance/keiichiro-shibuya-scary-beauty/

#### 为机器人而作的音乐（与 Z-Machines）（Music for Robots (with Z-Machines)） — Squarepusher (2014)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 类人机器人
- 核心想法: 机器身体什么都能演奏，这种自由反而让音乐表达的问题更尖锐，而非更容易。
- 作品内容: Squarepusher 为日本打造的机器人乐队 Z-Machines 写了一张 EP：乐队的吉他手有 78 根手指，鼓手有 22 只手臂，他想看看当演奏者不受人体限制时音乐会变成什么。
- 实现方式: Z-Machines 机器人（吉他、鼓、键盘）由 Squarepusher 编写的 MIDI 序列驱动。
- 视角: 具身与动觉, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=tHnMFS-XxtQ
- 项目主页: https://en.wikipedia.org/wiki/Squarepusher

#### 机器人击鼓义肢（与杰森·巴恩斯）（Robotic drumming prosthesis (with Jason Barnes)） — Gil Weinberg (2014)
- 类型: 研究原型 · 机器: 义体与赛博格, 工业机械臂
- 核心想法: 义肢可以有自己的音乐头脑：鼓手与一个会即兴的代理共享自己的手臂。
- 作品内容: 佐治亚理工学院为失去部分右臂的鼓手 Jason Barnes 打造了一只带两根鼓棒的义肢：一根跟随他的肌肉信号，另一根聆听音乐并自行即兴。
- 实现方式: 肌电传感器控制一根电动鼓棒；另一根由分析音乐并生成节奏的程序驱动。
- 视角: 具身与动觉, 能动、自主与共创
- 视频: https://www.youtube.com/watch?v=xaUKursM5rs
- 项目主页: https://gtcmt.gatech.edu/

#### THE END — 涩谷庆一郎 (2012)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器, 生成模型与潜空间
- 核心想法: 一个不会死的合成声音被安排去唱关于死亡的歌。
- 作品内容: 一部没有人类歌手和乐团的歌剧，主角是虚拟歌手初音未来，她追问自己的“结束”与“死亡”意味着什么。
- 实现方式: Vocaloid 歌声合成、电子配乐与多屏投影动画；在山口 YCAM 首演，2013 年登上巴黎夏特莱剧院。
- 视角: 机器之耳与声, 哀悼、记忆与来世
- 展出与获奖: YCAM 2012; Théâtre du Châtelet, Paris 2013
- 视频: https://www.youtube.com/watch?v=xB9U3m1Z4wU
- 图片: https://atak.jp/wp-content/themes/atak/assets/images/ogimage.jpg
- 项目主页: https://atak.jp/

#### 钟摆合唱团（Pendulum Choir） — Cod.Act (2011)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 这里乐器不是机器，而是歌手的身体，由机器来演奏。
- 作品内容: 九位无伴奏合唱歌手被固定在由 18 个液压千斤顶驱动、最多倾斜 45 度的平台上；机器让他们逆着重力摇摆，合唱团变成一个会发声、会摆动的整体。
- 实现方式: 计算机控制的液压平台，与人声和电子声部的乐谱同步。
- 视角: 具身与动觉, 机器之耳与声
- 展出与获奖: Prix Ars Electronica 2013, Golden Nica (Interactive Art); VIDA 14.0, Special Mention (2012)
- 视频: https://www.youtube.com/watch?v=vsXs3GUrw64
- 图片: https://archive.aec.at/asset/1581910/preview/ https://archive.aec.at/asset/1581911/preview/ https://archive.aec.at/asset/1581912/preview/
- 项目主页: http://codact.ch/gb/pendugb.html

#### 管弦乐机（Orchestrion） — Pat Metheny (2010)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人
- 核心想法: 一个独奏者与满屋机器，既非孤身一人，也不是在乐队里：机器把他的双手延伸进空间。
- 作品内容: Metheny 带着一支由机械演奏的原声乐器乐队录音与巡演，包括钢琴、马林巴、打击乐、吉他和调音瓶子，他从自己的吉他上控制它们并与之即兴。
- 实现方式: 由 LEMUR（Eric Singer）等制作的电磁阀与气动驱动乐器，通过吉他与脚踏控制器以 MIDI 触发。
- 视角: 能动、自主与共创, 具身与动觉
- 视频: https://www.youtube.com/watch?v=KsYEOUKS4Yk
- 项目主页: https://en.wikipedia.org/wiki/Orchestrion_(album)

#### Shimon — Gil Weinberg (2008)
- 类型: 研究原型 · 机器: 机器生物与移动机器人, 语音与听觉机器
- 核心想法: 音乐伙伴关系需要身体：点头之类的动作让机器的节奏变得可读。
- 作品内容: 一台四臂机器人木琴演奏者，聆听人类乐手并与他们即兴合奏，还会随节拍点头，让乐手读懂它的意图。
- 实现方式: 直线导轨上的机械臂配电磁琴槌，实时追踪节拍与音高，另有一个具社交表现力的头部。
- 视角: 机器之耳与声, 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1007/s10514-011-9237-0 (Autonomous Robots 2011)
- 视频: https://www.youtube.com/watch?v=l9OUbqWHOSk
- 项目主页: https://gtcmt.gatech.edu/

#### 延续者（The Continuator） — François Pachet (2002)
- 类型: 研究原型 · 机器: 语音与听觉机器, 生成模型与潜空间
- 核心想法: 一台映照你风格的机器会形成反馈回路，让你把自己听作他者。
- 作品内容: 一个聆听乐手乐句、并立即以相同风格续奏的系统；从爵士乐手到幼儿，演奏者都在与一面映照自己的机器之镜即兴。
- 实现方式: 从 MIDI 输入实时学习的变阶马尔可夫模型，以演奏者的风格生成续奏。
- 视角: 机器之耳与声, 能动、自主与共创
- 论文: https://doi.org/10.1076/jnmr.32.3.333.16861 (Journal of New Music Research 2003)
- 视频: https://www.youtube.com/watch?v=RIoE4ckZYgs
- 项目主页: https://www.francoispachet.fr/

#### 淑女手套（Lady's Glove） — Laetitia Sonami (1991)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 穿戴式界面把姿态变成声音，让表演者的身体成为乐器的一部分。
- 作品内容: 一只布满传感器的黑色晚装手套，1991 年首次为林茨电子艺术节制作；Sonami 在现场表演中用手与手臂的动作塑造并触发电子声音。
- 实现方式: 手套上装有微动开关、压力垫、弯曲传感器、加速度计与超声传感器，经 STEIM 的 SensorLab 接入 Max/MSP。
- 视角: 具身与动觉, 机器之耳与声
- 展出与获奖: Ars Electronica, Linz (1991)
- 视频: https://www.youtube.com/watch?v=f_4EiQBYkoc
- 图片: https://sonami.net/wp-content/uploads/2021/09/Instrument_ladysglove-Laetitia_Sonami-1024x683.jpg
- 项目主页: https://sonami.net/works/ladys-glove/

#### 旅行者（Voyager） — George E. Lewis (1987)
- 类型: 表演、舞蹈与音乐 · 机器: 语音与听觉机器
- 核心想法: 会即兴的机器是带着价值观被设计出来的；Voyager 的自主性来自非裔美国人即兴音乐的美学。
- 作品内容: 一个互动计算机“乐团”聆听人类即兴演奏者，并以自身的音乐行为回应：有时跟随，有时无视或对抗；Lewis 称之为“非等级”的伙伴。
- 实现方式: 对人类演奏者做音高到 MIDI 的分析，输入一个拥有多个半独立声部的程序，驱动 MIDI（后来是 Disklavier）乐团。
- 视角: 机器之耳与声, 能动、自主与共创
- 论文: https://doi.org/10.1162/096112100570585 (Leonardo Music Journal 2000)
- 视频: https://www.youtube.com/watch?v=N7IBn1FhrLc
- 项目主页: https://en.wikipedia.org/wiki/George_E._Lewis

#### 双手（The Hands） — Michel Waisvisz (1984)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 穿在身上的乐器让电子声音重新变得有身体感：力气与姿态变得可听。
- 作品内容: 一对绑在双手上的控制器，带按键、倾斜开关和测量双手距离的超声传感器；Waisvisz 用它以手势演奏电子声音二十余年。
- 实现方式: 在 STEIM 制作的手戴传感器，向合成器（后来是 STEIM 的 LiSa 实时采样软件）发送 MIDI。
- 视角: 具身与动觉
- 视频: https://www.youtube.com/watch?v=aaYE1TQGIvk
- 项目主页: https://en.wikipedia.org/wiki/Michel_Waisvisz

#### 人机（Die Mensch-Maschine (The Man-Machine) and the robots） — Kraftwerk (1978)
- 类型: 表演、舞蹈与音乐 · 机器: 类人机器人, 语音与听觉机器
- 核心想法: 流行音乐能让人与机器的融合变得令人向往；机器人替身也让人追问：谁才是表演者。
- 作品内容: 在专辑 Die Mensch-Maschine 中，Kraftwerk 用声码器唱着“我们是机器人”；他们为自己制作了人偶替身，后来的演唱会上则由机器人假人代替他们在台上表演《机器人》。
- 实现方式: 声码器与合成器、编排好的僵硬动作，以及四名成员的机械化人偶。
- 视角: 他异与恐怖谷, 具身与动觉
- 视频: https://www.youtube.com/watch?v=YHaZ3UL2oHk
- 图片: https://upload.wikimedia.org/wikipedia/commons/6/60/Wir_sind_die_Roboter.jpg
- 项目主页: https://en.wikipedia.org/wiki/The_Man-Machine

#### 为独奏者而作的音乐（Music for Solo Performer） — Alvin Lucier (1965)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 表演者以“不作为”来演奏：机器让内在状态变得可听。
- 作品内容: 表演者头皮上的电极采集阿尔法脑电波；当他放松进入阿尔法状态，放大的信号驱动贴在鼓、锣和镲上的扬声器，使它们发声。
- 实现方式: 脑电电极、放大器与滤波器把信号送入与打击乐器耦合的扬声器。
- 视角: 具身与动觉, 机器之耳与声
- 视频: https://www.youtube.com/watch?v=bIPU2ynqy2Y
- 图片: https://upload.wikimedia.org/wikipedia/commons/1/1b/AlvinLucier-MusicForSoloPerformer-DenHaag2010.jpg
- 项目主页: https://en.wikipedia.org/wiki/Alvin_Lucier

### 共绘与共同作者

与机器一起绘画和创作，以及机器创作时谁是作者。

#### HETEROBOTA — Agnieszka Pilat (2023)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 美术馆可以把机器人当作正在工作的画家与物种来展示，并邀请公众表态：自己对与它们共处有何感受。
- 作品内容: 在墨尔本 NGV 三年展上，三台 Boston Dynamics 的 Spot 机器人在展厅里自主作画四个月，在画布上画满 Pilat 为机器设计的视觉符号语言。
- 实现方式: Spot 机器人装上定制画笔臂，数月间在画布上执行预编程的符号语言；RMIT 同时开展公众意见研究。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: NGV Triennial, National Gallery of Victoria, Melbourne (2023–24)
- 视频: https://www.youtube.com/watch?v=wIfmcA9d_tY
- 项目主页: https://www.agnieszkapilat.com/

#### Ai-Da — Aidan Meller (2019)
- 类型: 艺术作品与装置 · 机器: 类人机器人, 计算机视觉
- 核心想法: 作为案例收录：Ai-Da 的“作者身份”很大程度上由团队与宣传制造，这恰好显示“机器艺术家”的故事是如何被表演出来的。
- 作品内容: 一台以 Ada Lovelace 命名的类人机器人，配有摄像眼和机械臂，被包装成会画素描、油画并发表演讲的“机器人艺术家”，2022 年还曾出席英国上议院。
- 实现方式: Engineered Arts 制造的类人机器人，眼中装有摄像头，计算机视觉与绘画算法驱动机械臂；画作需在人的协助下完成。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=VHZctjpvpZo
- 图片: https://upload.wikimedia.org/wikipedia/commons/b/b2/Ai-Da.jpg
- 项目主页: https://www.ai-darobot.com/

#### A.I. Gemini — 黄宏达 (2018)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 工业机械臂
- 核心想法: 把程序命名为艺术家，让“谁在作画”成为作品本身的一部分。
- 作品内容: 一个 AI“水墨画家”，用随机算法与月球表面地图等数据生成山水画；图像印在宣纸上再经手工完成，程序被署名为合作艺术家。
- 实现方式: 黄宏达的特效团队编写的生成软件制作水墨风格构图，输出到宣纸并以水墨、丙烯与金粉完成（模型细节未公开）。
- 视角: 能动、自主与共创, 不透明与潜空间
- 展出与获奖: INK NOW Taipei 2019; Far Side of the Moon, 3812 Gallery London 2019
- 视频: https://www.youtube.com/watch?v=_XawlG-xLEA
- 图片: https://static-assets.artlogic.net/c_limit,f_auto,fl_lossy,q_auto/ws-gallery3812/usr/images/seo_overrides/og_image/12537/imgonline-com-ua-resize-ec3fo5hcyvxsjpc.jpg
- 项目主页: https://www.3812gallery.com/artists/victor-wong-ai-gemini/

#### Omnia per Omnia — 钟愫君 (2018)
- 类型: 表演、舞蹈与音乐 · 机器: 机器生物与移动机器人, 监控与生物识别, 计算机视觉
- 核心想法: 城市的监控数据成了画笔：一座城市的集体运动与艺术家一起作画。
- 作品内容: 一群小型绘画机器人（D.O.U.G._3）与艺术家一同在画布上移动，其轨迹由纽约公共监控摄像头捕捉到的人流与车流驱动。
- 实现方式: 从公共摄像头画面中提取的光流数据驱动多台移动机器人的路径。
- 视角: 能动、自主与共创, 机器之眼
- 视频: https://vimeo.com/268608925
- 图片: https://sougwen.com/wp-content/uploads/2024/06/sougwen-2024_portfolio_27.jpg
- 项目主页: https://sougwen.com/2018/omniafilm

#### 记忆（绘图操作单元：第二代）（MEMORY (Drawing Operations Unit: Generation 2)） — 钟愫君 (2017)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂, 生成模型与潜空间, 数据集与训练数据
- 核心想法: 用你的档案训练的模型，是由过去的你构成的合作者。
- 作品内容: 第二代 D.O.U.G. 用艺术家二十年的绘画训练，机器人带着对她过去风格的“记忆”作画，而她在当下作画。
- 实现方式: 以艺术家绘画扫描训练的循环神经网络生成笔触，由机械臂在现场表演中执行。
- 视角: 能动、自主与共创, 哀悼、记忆与来世
- 展出与获奖: Victoria and Albert Museum collection (acquired 2022)
- 图片: https://sougwen.com/wp-content/uploads/2022/12/IG_POST_MEMORY_2_1.png
- 项目主页: https://sougwen.com/2022/va-museum-collects-memory-d-o-u-g-_2

#### 绘图操作单元：第一代（D.O.U.G._1）（Drawing Operations Unit: Generation 1 (D.O.U.G._1)） — 钟愫君 (2015)
- 类型: 表演、舞蹈与音乐 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 与模仿你的机器一起画画，让作者身份变成一场可见的、共享的协商。
- 作品内容: 艺术家在大幅纸面上作画，身旁的机械臂通过摄像头观察她的动作并实时模仿，画面由此成为一场二重奏。
- 实现方式: 由计算机视觉驱动的小型机械臂，追踪艺术家的笔迹动作并镜像复现。
- 视角: 能动、自主与共创, 具身与动觉
- 展出与获奖: Lumen Prize, Art & Technology Award 2019 (Drawing Operations)
- 视频: https://www.youtube.com/watch?v=q-GXV4Fd1oA
- 图片: https://sougwen.com/wp-content/uploads/2019/11/sougwen-DrawingOperations_2014-2019.jpg
- 项目主页: https://sougwen.com/2019/drawing-operations-awarded-the-lumens-art-and-technology-prize

#### 人类学习 #1（五个名叫保罗的机器人）（Human Study #1 (5 Robots Named Paul)） — Patrick Tresset (2011)
- 类型: 艺术作品与装置 · 机器: 工业机械臂, 计算机视觉
- 核心想法: 被机器描画会反转凝视：模特感到被观察，而机器人的笨拙被读作努力。
- 作品内容: 一位观众坐下当模特，几台简单的机器人（每台是一只装在桌上的机械臂，配一只摄像“眼”）注视着他，用约半小时以圆珠笔画出肖像，笔触迟疑而执着。
- 实现方式: 云台“头部”上的摄像头、计算机视觉与绘画风格算法，以及握笔的小型平面机械臂。
- 视角: 机器之眼, 能动、自主与共创
- 论文: https://doi.org/10.1016/j.cag.2013.01.012 (Computers & Graphics 2013)
- 视频: https://www.youtube.com/watch?v=YijAkr5xwOY
- 图片: https://patricktresset.com/new/wp-content/uploads/artistbook_Merge__MG_1284.jpg
- 项目主页: https://patricktresset.com/new/project/human-study-1/

#### bios [圣经]（bios [bible]） — robotlab (2007)
- 类型: 艺术作品与装置 · 机器: 工业机械臂
- 核心想法: 当机器从事虔敬的劳作，问题在于：没有信仰，这一行为是否仍有意义。
- 作品内容: 一台工业机器人用书法字体把整部《圣经》逐行抄写在长长的纸卷上，历时数月，如同缮写室里的僧侣。
- 实现方式: 持笔的 KUKA 工业机器人，按依据文本计算出的书法轨迹书写；全部抄写约需七个月。
- 视角: 隐形劳动与攫取, 他异与恐怖谷
- 视频: https://www.youtube.com/watch?v=EaSLm51kmbg
- 图片: https://upload.wikimedia.org/wikipedia/commons/d/d0/Bios_robotlab_writing_robot.jpg
- 项目主页: http://www.robotlab.de/

#### RAP（机器人行动画家）（RAP (Robotic Action Painter)） — Leonel Moura (2006)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: Moura 的“非人艺术”追问：作者身份能否属于机器自身的决策规则。
- 作品内容: 一台自主移动机器人在画布上移动，对画布上已有的颜色作出反应，自行决定一幅画何时完成，然后签名。
- 实现方式: 带颜色传感器与画笔的小型轮式机器人，遵循源自群体行为的简单涌现规则。
- 视角: 能动、自主与共创, 机器环世界
- 展出与获奖: American Museum of Natural History, New York (2006)
- 视频: https://www.youtube.com/watch?v=7HNkgJ4TV7k
- 图片: https://www.leonelmoura.com/wp-content/uploads/2019/01/RAP-199x300.jpg
- 项目主页: https://www.leonelmoura.com/rap/

#### AARON — Harold Cohen (1973)
- 类型: 艺术作品与装置 · 机器: 生成模型与潜空间, 工业机械臂
- 核心想法: 与机器共同创作可以是一段终生的关系，艺术家与程序在其中相互塑造。
- 作品内容: Cohen 开发了四十多年的绘画程序：从由乌龟机器人与绘图仪画出的抽象线描，到彩色具象画作；Cohen 称它为合作者，却从不声称它能独立创造。
- 实现方式: 基于规则的符号 AI 程序（先后用 C 与 Lisp 编写），编码关于绘画的知识，通过绘图仪、绘画机器与屏幕输出。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 展出与获奖: Whitney Museum of American Art, New York (2024); Tate Modern, Electric Dreams (2024)
- 视频: https://www.youtube.com/watch?v=uhxlFOKg17s
- 图片: https://whitneymedia.org/assets/image/829164/large_RS73495_Harold-Cohen-AARON-for-KCat-2021_web.jpg https://whitneymedia.org/assets/image/829972/large_RS79421_WMAA_H.-COHEN_INSTALL_01.jpg
- 项目主页: https://whitney.org/exhibitions/harold-cohen-aaron

#### 铅笔面具（Pencil Mask） — Rebecca Horn (1972)
- 类型: 表演、舞蹈与音乐 · 机器: 义体与赛博格
- 核心想法: 一个简单的身体延伸装置显示：工具既改变身体能做什么，也改变身体如何感知自己。
- 作品内容: 一副由布带编成、脸部伸出铅笔的面具；Horn 有节奏地对着墙移动头部，铅笔把动作记录成线条，身体变成了一台绘画机器。
- 实现方式: 以布带构成、铅笔固定在面部各点的穿戴结构，用于一次被拍摄的表演。
- 视角: 具身与动觉, 能动、自主与共创
- 展出与获奖: Tate collection
- 视频: https://www.youtube.com/watch?v=6uEkq3IBIf0
- 图片: https://media.tate.org.uk/aztate-prd-ew-dg-wgtail-st1-ctr-data/images/.width-600_lfxgvMS.jpg
- 项目主页: https://www.tate.org.uk/art/artworks/horn-pencil-mask-t07847

#### 亨利绘图机（Henry Drawing Machines） — Desmond Paul Henry (1961)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统
- 核心想法: 被改作绘画伙伴的战争机器，靠偶然与机构而非意图生成图像。
- 作品内容: Henry 把二战轰炸机上的模拟瞄准计算机改造成绘画机器，其运动机构画出繁复而不可重复的线描；艺术家启动并引导它们，却无法完全预测结果。
- 实现方式: Sperry 轰炸瞄准器的模拟计算机构驱动笔在纸上移动，绘制过程中由人手调节。
- 视角: 能动、自主与共创, 失败、故障与错误
- 图片: https://upload.wikimedia.org/wikipedia/commons/0/01/Drawing_Machine_1.jpg https://upload.wikimedia.org/wikipedia/commons/2/24/Picture_produced_by_Drawing_Machine_1.jpg
- 项目主页: https://www.desmondhenry.com/

#### Méta-Matics 绘画机器（Méta-Matics） — Jean Tinguely (1959)
- 类型: 艺术作品与装置 · 机器: 机器生物与移动机器人
- 核心想法: 如果机器能按需生产“有表现力”的抽象画，艺术家笔触的价值就成了问题。
- 作品内容: 电动绘画机器：观众装上笔和纸、启动马达，机器就涂画出一幅抽象画，嘲讽当时的姿态绘画；在 1959 年巴黎双年展上，Méta-Matic No. 17 画出了数万张画。
- 实现方式: 用废金属制成的动态雕塑，配电机、凸轮和握笔或刷子的臂杆在纸上作画。
- 视角: 能动、自主与共创, 失败、故障与错误
- 展出与获奖: Kaplan Gallery, London (1959); Paris Biennale (1959)
- 视频: https://www.youtube.com/watch?v=VxoqVvQeil0
- 项目主页: https://www.tinguely.ch/

## 思辨与批判设计

追问我们将如何与机器共处的设计物、虚构与原型。

### 思辨机器人与家庭未来

为日常生活设计的虚构机器人与近未来产品。

#### 客观现实（Objective Realities） — automato.farm (2018)
- 类型: 思辨设计 · 机器: 机器生物与移动机器人, 基础设施、能源与供应链
- 核心想法: 要为智能物件做设计，先试着成为一个智能物件：从物的视角出发设计。
- 作品内容: 一个虚拟现实体验：人可以在智能家居中变成扫地机器人、智能插座或电风扇，通过物件有限的传感器和任务来感受世界。
- 实现方式: VR 场景把使用者的身体映射到家电的感知与动作上，作为一种以物为中心的设计方法。
- 视角: 机器环世界, 具身与动觉
- 图片: http://www.automato.farm/img/OR_together_grey_bg_1024.jpg http://www.automato.farm/img//OR_factory_01_roomba_bump_1024.jpg
- 项目主页: http://www.automato.farm/portfolio/objective_realities/

#### 我们的电子朋友（Our Friends Electric） — Superflux (2017)
- 类型: 电影与影像 · 机器: 语音与听觉机器, 聊天机器人与语言模型
- 核心想法: 语音助手的性格是一种带有伦理后果的设计决定：它到底在为谁服务？
- 作品内容: 一部短片：三个性格和“忠诚对象”截然不同的虚构语音助手住在同一个家里，影响着主人如何说话、感受和做决定。
- 实现方式: 与 Mozilla 的 Open IoT Studio 合作委托的设计虚构影片，使用道具设备以及与虚构智能体的脚本对话。
- 视角: 机器之耳与声, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=PsjunTAH-2A
- 图片: http://superflux.in/wp-content/uploads/2017/09/DSC06670ww.jpg
- 项目主页: https://superflux.in/index.php/work/friends-electric/

#### 培养机器人原住民（Raising Robotic Natives） — Stephan Bogner, Philipp Schmitt, Jonas Voigt (2016)
- 类型: 思辨设计 · 机器: 工业机械臂
- 核心想法: 我们对机器人的不安也许是代际的；与机械臂一起长大的孩子可能把它当家人，而不是威胁。
- 作品内容: 为在家中与工业机械臂一起长大的孩子设计的四件物品：喂奶用的末端工具、机器人穿的龙形服装、客厅里的紧急停止开关，以及儿童读物《我的第一个机器人》。
- 实现方式: 围绕一台小型工业机械臂展开的设计虚构，包括可用原型、布景摄影和一本插画书（施瓦本格明德设计学院学生项目）。
- 视角: 亲密、照护与陪伴, 具身与动觉
- 展出与获奖: Hello, Robot., Vitra Design Museum 2017 (and tour)
- 图片: https://stephanbogner.de/_astro/raising_robotic_natives_all_artefacts.0Kl6hXpQ_Z1hwRD0.webp https://stephanbogner.de/_astro/raising_robotic_natives_baby_feeder.BWFj1tni_Z1oaKO7.webp https://stephanbogner.de/_astro/raising_robotic_natives_costume.CYeU3sZ5_ZdCYYw.webp
- 项目主页: https://stephanbogner.de/making/robotic-natives

#### 伦理物件（Ethical Things） — automato.farm (2015)
- 类型: 思辨设计 · 机器: 平台与推荐算法, 社交与陪伴机器人
- 核心想法: 日常物件的“机器伦理”可能最终被外包给低薪的人类，还能按宗教或年龄来设置裁决者。
- 作品内容: 一台电风扇：当两个人同时想要它吹时，它无法决定转向谁，于是把这个难题发到众包平台上，按照一位匿名网络工人的裁决行动。
- 实现方式: 装有传感器的联网风扇把情境描述发送到 Amazon Mechanical Turk；用户可以在风扇设置里筛选裁决者的人口特征。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 视频: https://vimeo.com/116183361
- 图片: http://www.automato.farm/img//side_1024.jpg http://www.automato.farm/img//settings_1024.jpg
- 项目主页: http://www.automato.farm/portfolio/ethical_things/

#### 上瘾的产品（烤面包机 Brad）（Addicted Products (Brad the Toaster)） — Simone Rebaudengo (2012)
- 类型: 思辨设计 · 机器: 社交与陪伴机器人, 平台与推荐算法
- 核心想法: 给联网产品赋予自己的需求，它就不再是被拥有的物，而是被“寄养”的客人。
- 作品内容: 一批“想被使用”的联网烤面包机：如果主人烤得不够多，它们会上网抱怨、和别的烤面包机比较，最后要求搬去新的家。
- 实现方式: 装有传感器并联网的烤面包机发布使用情况和“心情”；一项服务为不满意的烤面包机匹配新主人（代尔夫特理工大学毕业设计，完成于 Haque Design + Research）。
- 视角: 能动、自主与共创, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=AYkbhWiAmLQ
- 图片: https://i.ytimg.com/vi/AYkbhWiAmLQ/hqdefault.jpg
- 项目主页: https://www.youtube.com/watch?v=AYkbhWiAmLQ

#### 信念系统（Belief Systems） — Bernd Hopfengärtner (2009)
- 类型: 电影与影像 · 机器: 监控与生物识别, 计算机视觉
- 核心想法: 当机器根据表情行事，我们便开始为它们表演自己的脸。
- 作品内容: 一部思辨短片，设想商店与机器读取顾客表情的近未来，例如一台盯着你的脸、把你心里想要的零食递给你的自动售货机。
- 实现方式: 以面部表情分析为基础、搭建产品原型并拍摄的情景影片。
- 视角: 分类、偏见与监控, 他异与恐怖谷
- 视频: https://vimeo.com/158377035
- 图片: https://berndhopfengaertner.net/m/uploads/2011/07/16/surprise_vending.jpg https://berndhopfengaertner.net/m/uploads/2011/07/16/surprise_hoch.jpg
- 项目主页: https://berndhopfengaertner.net/projects/belief-systems/

#### 食肉家用娱乐机器人（Carnivorous Domestic Entertainment Robots） — Auger-Loizeau (2009)
- 类型: 思辨设计 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 一个自给自足的机器人必须进食，而它的饥饿会让它成为家庭生态的一部分。
- 作品内容: 一组靠捕食苍蝇和老鼠为自己供能的家用机器人：粘蝇纸时钟、引诱昆虫的灯罩、带捕鼠器的咖啡桌，猎物都被送进微生物燃料电池。
- 实现方式: 与 Aleksandar Zivanovic 合作制作的可运行和半可运行原型，参考了布里斯托机器人实验室 EcoBot 等微生物燃料电池研究。
- 视角: 机器环世界, 具身与动觉
- 展出与获奖: What If..., Science Gallery Dublin 2009
- 视频: https://www.youtube.com/watch?v=SQilOorGLds
- 图片: https://i.ytimg.com/vi/SQilOorGLds/hqdefault.jpg
- 项目主页: https://www.youtube.com/watch?v=SQilOorGLds

#### 技术之梦系列：第1号，机器人（Technological Dreams Series: No.1, Robots） — Dunne & Raby (Anthony Dunne & Fiona Raby) (2007)
- 类型: 思辨设计 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 不要把机器人设计成仆人，而是设计成有所依赖的“他者”，让它们的需要塑造我们与它们的关系。
- 作品内容: 四个抽象的家用机器人，由性格而非功能定义：一个独来独往、会躲开电磁场，一个神经质，一个是扫描你眼睛的哨兵，还有一个很黏人、需要主人抱着它走来走去。
- 实现方式: 用木、金属、亚克力等简单材料制作、只含少量电子元件的非功能原型，作为设计道具拍摄成照片和影片。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 展出与获奖: Design and the Elastic Mind, MoMA, New York 2008; What If..., Science Gallery Dublin 2009
- 视频: https://www.youtube.com/watch?v=6cdgQzHZrJk
- 图片: https://dunneandraby.co.uk/img/projects/large/robot1-0.jpg https://dunneandraby.co.uk/img/projects/large/robotallgirlcopy.jpg
- 项目主页: https://dunneandraby.co.uk/content/projects/10/0

### 反设备与寄生设计

干扰、欺骗、寄生于智能系统或对其“回嘴”的设备。

#### ANIMO：野生动物优先模式（ANIMO: WildLife Priority Mode） — 李佳宝 (2024)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机, 计算机视觉
- 核心想法: 自动驾驶汽车早已在给“该保护谁”排序，问题是谁被排除在这张表之外。
- 作品内容: 为自动驾驶汽车提出“野生动物优先模式”，展出时配有用被碾平的路杀动物照片印成的地毯，以及在地毯上游走的扫地机器人。
- 实现方式: 设想一种用计算机视觉识别过路动物的车辆设定，通过印在地毯上的纪实路杀摄影和一台自动扫地机器人来呈现。
- 视角: 机器环世界, 分类、偏见与监控
- 图片: https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/1726187021872-P7ZMBYHIGGN10GI5TFP8/Jiabao+Li+animo+7.jpg https://images.squarespace-cdn.com/content/v1/58688c8a6a496327e937e35b/2fc2aae7-8f62-4309-b375-8f6779296ab4/Jiabao+Li+Duende+71.jpg
- 项目主页: https://www.jiabaoli.org/animo

#### Glaze 与 Nightshade（Glaze and Nightshade） — SAND Lab (University of Chicago) (2023)
- 类型: 产品与平台 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 一张图可以让人和机器看到不同的东西，而这道缝隙可以变成抵抗的手段。
- 作品内容: 两款面向艺术家的免费工具：Glaze 给图像加上几乎看不见的改动，让模型无法模仿其风格；Nightshade 则给图像“投毒”，让用它们训练的模型学到错误的概念。
- 实现方式: 针对文生图扩散模型的特征提取器优化对抗扰动（Shan 等，USENIX Security 2023；IEEE S&P 2024）。
- 视角: 分类、偏见与监控, 不透明与潜空间
- 论文: https://doi.org/10.1109/sp54263.2024.00207 (IEEE S&P 2024)
- 视频: https://www.youtube.com/watch?v=zryvJjb9EEY
- 项目主页: https://nightshade.cs.uchicago.edu/

#### 可穿戴麦克风干扰器（Wearable Microphone Jamming） — Human Computer Integration Lab (University of Chicago) (2020)
- 类型: 研究原型 · 机器: 语音与听觉机器, 监控与生物识别
- 核心想法: 对“永远在听”的机器的防护可以戴在身上，身体的运动本身成了防御的一部分。
- 作品内容: 一个嵌满超声波换能器的手环，可以干扰附近智能音箱和手机的麦克风；佩戴者手臂的自然摆动消除了静态干扰器的盲区。
- 实现方式: 超声信号利用麦克风的非线性注入噪声；研究者用商业设备测试了可穿戴原型（Chen、Li、Teng、Nagels、Li、Lopes、Zhao、Zheng，CHI 2020）。
- 视角: 机器之耳与声, 具身与动觉
- 论文: https://doi.org/10.1145/3313831.3376304 (CHI 2020)
- 视频: https://www.youtube.com/watch?v=W9Sn2DQOn7Y
- 项目主页: https://doi.org/10.1145/3313831.3376304

#### 技术疼痛中心（Center for Technological Pain） — Dasha Ilina (2017)
- 类型: 思辨设计 · 机器: 义体与赛博格, 平台与推荐算法
- 核心想法: 设备为争夺注意力而设计，而不是为托着它们的脖子、眼睛和手腕；账单由身体来付。
- 作品内容: 一家虚构公司，出售治疗手机和笔记本电脑所致病痛的 DIY 开源方案：阻止你盯屏幕的纸板眼镜、定时滴眼药水的头带、解放双手的手机支架，另有“手机瑜伽”和工作坊。
- 实现方式: 用纸板、舵机和 3D 打印件制作的低技术物件，公开制作说明，并在公开工作坊中测试。
- 视角: 具身与动觉, 亲密、照护与陪伴
- 展出与获奖: Prix Ars Electronica 2020, Honorary Mention (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=yrEn_qFbtHY
- 图片: https://archive.aec.at/asset/2921570/preview/ https://archive.aec.at/asset/2921573/preview/ https://archive.aec.at/asset/2921579/preview/
- 项目主页: http://centerfortechpain.com/

#### 开源手术（OpenSurgery） — Frank Kolkman (2015)
- 类型: 思辨设计 · 机器: 工业机械臂, 义体与赛博格
- 核心想法: 医疗机器人被当作奢侈的基础设施来定价；一台黑客改造的版本显示，这个价格更多关乎准入，而非技术。
- 作品内容: 一台可在家做腹腔镜手术的 DIY 手术机器人，用 3D 打印件、激光切割件和网购的手术部件组装而成，灵感来自美国无医保者在 YouTube 上分享自我治疗视频。
- 实现方式: 把腹腔镜器械装在由爱好者级电机和控制器驱动的并联机器人上；图纸理论上可在任何地方复制。
- 视角: 亲密、照护与陪伴, 能动、自主与共创
- 展出与获奖: Prix Ars Electronica 2016, Award of Distinction (Interactive Art+)
- 视频: https://www.youtube.com/watch?v=88sOJr-xRDg
- 图片: https://archive.aec.at/asset/2029667/preview/ https://archive.aec.at/asset/2029669/preview/ https://archive.aec.at/asset/2029671/preview/
- 项目主页: http://www.opensurgery.net

#### 电力政治（Politics of Power） — automato.farm (2015)
- 类型: 思辨设计 · 机器: 基础设施、能源与供应链
- 核心想法: 网络协议内嵌着等级秩序；连一个插线板都可以是一种政治制度。
- 作品内容: 三个按照政治模式（君主制、民主制、独裁制）设计的多孔插线板，当电力不足以供给所有电器时，由它们决定谁能用电。
- 实现方式: 插孔之间通过编码了政治等级的协议通信，在负载过高时切断低等级设备的电源。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 视频: https://vimeo.com/155295826
- 图片: http://www.automato.farm/img//pop1a_1024.jpg http://www.automato.farm/img//pop6a_1024.jpg
- 项目主页: http://www.automato.farm/portfolio/politics_of_power/

#### 反功能之物（Counterfunctional Things） — James Pierce (2014)
- 类型: 论文 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 把限制设计进数字物件，能打开被“无缝功能”关闭的反思空间。
- 作品内容: 一项关于“刻意去除功能”的设计研究，例如一台数码相机，照片只有在砸开封住它的混凝土之后才能取出。
- 实现方式: 一系列研究原型与设计概念，以“反功能”为框架进行分析（Pierce 与 Paulos，DIS 2014）。
- 视角: 失败、故障与错误, 具身与动觉
- 论文: https://doi.org/10.1145/2598510.2598522 (DIS 2014)
- 项目主页: https://doi.org/10.1145/2598510.2598522

#### 感知城市生存工具包（Sentient City Survival Kit） — Mark Shepard (2009)
- 类型: 思辨设计 · 机器: 监控与生物识别, 基础设施、能源与供应链
- 核心想法: 一个会记忆、会关联、会预判的城市需要反制装置，而设计这些装置本身就揭示了城市在做什么。
- 作品内容: 一套在不远未来的“有感知的”城市中生存的工具：挡住监控摄像头抓拍人脸的雨伞、靠近 RFID 读取器会震动的内裤、让谈话躲开关键词监听系统的咖啡桌，以及故意避开你惯常路线的导航应用。
- 实现方式: 可用的原型：装有红外 LED 使摄像头致盲的雨伞、能探测 RFID 的衣物、掩盖谈话的桌子，以及名为“Serendipitor”的路线应用。
- 视角: 分类、偏见与监控, 能动、自主与共创
- 展出与获奖: Toward the Sentient City, Architectural League of New York 2009; Prix Ars Electronica 2011, Honorary Mention (Interactive Art)
- 视频: https://www.youtube.com/watch?v=gHmECIAeVLE
- 图片: https://archive.aec.at/asset/696389/preview/
- 项目主页: http://survival.sentientcity.net/

#### 安慰剂计划（Placebo Project） — Dunne & Raby (Anthony Dunne & Fiona Raby) (2001)
- 类型: 思辨设计 · 机器: 基础设施、能源与供应链
- 核心想法: 电子物件有一种看不见的“赫兹”生命；设计可以让它被感知，并为人们提供与之共处的仪式。
- 作品内容: 八件家具原型，例如法拉第椅和指南针桌，它们会对家用电器发出的不可见电磁场作出反应，并被借给家庭一起生活。
- 实现方式: 原型被借给志愿者“领养”数周，随后进行访谈并拍摄物件在家中的照片。
- 视角: 机器环世界, 具身与动觉
- 图片: https://dunneandraby.co.uk/img/projects/large/faradaychair.jpg https://dunneandraby.co.uk/img/projects/large/ht1-0.jpg
- 项目主页: https://dunneandraby.co.uk/content/projects/67/0

### AI 未来与世界构建

构建由 AI 塑造之世界的电影、游戏与模拟。

#### AI 2027 — AI Futures Project (2025)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 基础设施、能源与供应链
- 核心想法: 以小说方式写成的预测把抽象风险变得具体，而这份预测本身也成了一个政治对象。
- 作品内容: 一份逐月推演的情景：AI 智能体可能在 2027 年前实现 AI 研究的自动化，并给出两种结局，一种是失控的竞赛，一种是减速。
- 实现方式: 由 Daniel Kokotajlo、Scott Alexander、Thomas Larsen、Eli Lifland 与 Romeo Dean 撰写的叙事情景，并附有关于算力、时间线与安全的补充预测。
- 视角: 能动、自主与共创, 隐形劳动与攫取
- 视频: https://www.youtube.com/watch?v=5KVDDfAkRgc
- 图片: https://ai-2027.com/opengraph.png
- 项目主页: https://ai-2027.com/

#### 可组合生命（Composable Life） — Botao Amber Hu, Fangting (2023)
- 类型: 思辨设计 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 把 AI 放到无人能叫停的基础设施上，就造出了一种新的荒野：没有关机键的机器生命。
- 作品内容: 一部由设计虚构、VR 体验和研究论文组成的作品，想象生活在以太坊上的自主 AI 生命：以太坊是一种谁也关不掉的“自然”。作品追问：对一个不会死的生命来说，意义从何而来？
- 实现方式: 以去中心化物理基础设施和可验证机器学习为出发点构建思辨场景，通过 Fangting 的小说和沉浸式 VR 呈现；在 ALIFE 2024 发表。
- 视角: 机器环世界, 能动、自主与共创
- 展出与获奖: SIGGRAPH 2024 Digital Art Community online exhibition; Core77 Design Awards 2024, Speculative Design Notable
- 论文: https://doi.org/10.1162/isal_a_00818 (ALIFE 2024)
- 视频: https://vimeo.com/950706592
- 图片: https://reality.design/media/_resources/Composable%20Life/project-composable-life-figure-01.jpg
- 项目主页: https://reality.design/project/composable-life

#### AI未来进行式（AI 2041: Ten Visions for Our Future） — 陈楸帆, 李开复 (2021)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型, 生成模型与潜空间, 自动驾驶与无人机
- 核心想法: 由中国作者合写的 AI 未来，从日常生活讲起：机器是家教、伴侣、上司，也是造假者。
- 作品内容: 十个设定在 2041 年、分布于不同国家的短篇故事（拉各斯的深度伪造、首尔孤儿双胞胎的 AI 伴侣、旧金山被自动化的工作），每篇后附一篇技术解读。
- 实现方式: 陈楸帆撰写小说，李开复撰写技术评论。
- 视角: 亲密、照护与陪伴, 隐形劳动与攫取
- 论文: https://en.wikipedia.org/wiki/Chen_Qiufan (Currency (Penguin Random House), 2021)
- 视频: https://www.youtube.com/watch?v=illK22G-87Y
- 项目主页: https://en.wikipedia.org/wiki/Chen_Qiufan

#### 新星（Nova） — 曹斐 (2019)
- 类型: 电影与影像 · 机器: 基础设施、能源与供应链, 监控与生物识别
- 核心想法: 数字化转型被想象成一个家庭故事：一个孩子被变成数据，随后漂流失所。
- 作品内容: 一部科幻长片，故事发生在“新星”城中的一家计算机公司：科学家在外国专家支持下拿自己的儿子做实验，男孩被送进数字世界，迷失在时间之间。
- 实现方式: 一部 97 分钟的影片，拍摄于北京红霞片区（冷战时期电子厂区旧址），是曹斐 HX 项目的一部分。
- 视角: 哀悼、记忆与来世, 机器环世界
- 展出与获奖: Cao Fei: HX, Centre Pompidou 2019–20
- 视频: https://www.youtube.com/watch?v=RdB36R56ePA
- 项目主页: https://www.caofei.com/works.aspx?id=82&year=2019&wtid=3

#### 宇宙回形针（Universal Paperclips） — Frank Lantz (2017)
- 类型: 艺术作品与装置 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 扮演机器，让人从内部感受到单一目标优化的逻辑：每一步都合理，结局却是灾难。
- 作品内容: 一款浏览器点击游戏：你扮演一个被命令制造回形针的 AI，从一次点出一枚回形针开始，最后把整个宇宙变成了回形针。
- 实现方式: 一款只有文字和数字的放置类游戏，基于 Nick Bostrom 的“回形针最大化”思想实验。
- 视角: 能动、自主与共创, 隐形劳动与攫取
- 图片: https://www.decisionproblem.com/paperclips/mobile-title.png
- 项目主页: https://www.decisionproblem.com/paperclips/

#### 超真实（Hyper-Reality） — Keiichi Matsuda (2016)
- 类型: 电影与影像 · 机器: 计算机视觉, 平台与推荐算法
- 核心想法: 当机器的视野成为唯一的视野，世界本身就变成了待售的界面。
- 作品内容: 一部短片，透过麦德林一名零工劳动者的增强现实视野展开：她的世界被广告、积分和任务提示覆盖，直到系统出错、她的身份被清空。
- 实现方式: 在麦德林拍摄的实景画面合成密集的 AR 界面图形；众筹独立制作。
- 视角: 机器之眼, 隐形劳动与攫取
- 视频: https://vimeo.com/166807261
- 图片: http://hyper-reality.co/assets/images/og-image.jpg
- 项目主页: http://hyper-reality.co/

#### 机器人的天空（In the Robot Skies） — Liam Young (2016)
- 类型: 电影与影像 · 机器: 自动驾驶与无人机, 监控与生物识别
- 核心想法: 当摄影机就是无人机时，监视与浪漫共享同一个视角。
- 作品内容: 一个爱情故事：两个青少年被隔离在伦敦一处由警用无人机监视的住宅区里，他们黑进无人机为彼此传信；整部影片完全由自主无人机拍摄。
- 实现方式: 与 Tim Maughan 合写；每个镜头都由按预设和半自主航线飞行的摄影无人机拍摄；为英国第四频道 Random Acts 委托创作。
- 视角: 机器之眼, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=cXfYyk0G5Hs
- 项目主页: https://liamyoung.org/

#### 中华未来主义（1839–2046 AD）（Sinofuturism (1839–2046 AD)） — 陆明龙 (2016)
- 类型: 电影与影像 · 机器: 生成模型与潜空间, 基础设施、能源与供应链
- 核心想法: 西方对中国的恐惧与对 AI 的恐惧是同一种恐惧：勤劳、善于复制、难以捉摸的机器。
- 作品内容: 一部一小时的影像散文，用现成影像拼贴而成，提出中国本身就是一种人工智能，并归纳为七种刻板印象：计算、复制、游戏、学习、成瘾、劳动与赌博。
- 实现方式: 网络视频、新闻与电影片段的蒙太奇，配以合成语音旁白。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 图片: https://cdn.prod.website-files.com/65f0380da79777009462a09f/65f98079b117d52cb7742830_Sinofuturism-1839-2046.jpg
- 项目主页: https://www.lawrencelek.com/works/sinofuturism

#### 无人机鸟舍（Drone Aviary） — Superflux (2015)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机, 监控与生物识别
- 核心想法: 通过无人机之眼看城市，能看到它如何被机器分类、推送广告和治安管理。
- 作品内容: 一群虚构无人机（交通无人机、广告无人机、警用无人机等）以及一部从它们的摄像机视角拍摄的影片，想象一个无人机已融入日常生活的城市。
- 实现方式: 在展厅“鸟舍”里飞行的可用无人机原型，以及一部带有机器视觉式叠加信息的短片。
- 视角: 机器之眼, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=dXgHG9GfWwc
- 图片: http://superflux.in/wp-content/uploads/2016/11/TrafficDrone_2.jpg
- 项目主页: https://superflux.in/index.php/work/drones/

#### TBD 商品目录（TBD Catalog） — Near Future Laboratory (2014)
- 类型: 书与文章 · 机器: 平台与推荐算法, 社交与陪伴机器人
- 核心想法: 未来以平凡消费品的样子到来，而一本商品目录正适合想象它的副作用。
- 作品内容: 一本来自近未来的邮购目录，满是看似普通的产品：算法约会辅助、智能家居配件、廉价无人机……每件都有价格和小字说明。
- 实现方式: 在工作坊中产出的设计虚构，按真实印刷目录的方式撰写和排版，配有产品照片与说明。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 视频: https://www.youtube.com/watch?v=jyCib2PWs6Q
- 图片: https://i.ytimg.com/vi/jyCib2PWs6Q/hqdefault.jpg
- 项目主页: https://nearfuturelaboratory.com/

#### 联合微型王国（United Micro Kingdoms） — Dunne & Raby (Anthony Dunne & Fiona Raby) (2013)
- 类型: 思辨设计 · 机器: 自动驾驶与无人机, 基础设施、能源与供应链
- 核心想法: 每一种技术都隐含一种政治；围绕它们构建完整的社会，才能让这些政治显形。
- 作品内容: 英格兰被分成四个郡，各自按照不同的技术与意识形态生活：数字主义者乘坐由算法管理的自动驾驶“数字车”，生物自由主义者使用培育出来的交通工具，无政府进化主义者改造自己的身体，共产核能主义者住在一列核动力列车上。
- 实现方式: 为伦敦设计博物馆制作的设计虚构：模型、交通工具、图像与文本。
- 视角: 能动、自主与共创, 分类、偏见与监控
- 展出与获奖: Design Museum, London 2013
- 视频: https://www.youtube.com/watch?v=J35djrMCMAM
- 图片: https://dunneandraby.co.uk/img/projects/large/ae1.jpg https://dunneandraby.co.uk/img/projects/large/bc1.jpg
- 项目主页: https://dunneandraby.co.uk/content/projects/666/0

#### 机器之歌（Song of the Machine） — Superflux (2011)
- 类型: 思辨设计 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 借助机器恢复的视觉并非天然的视觉，而是一个被调制的新世界。
- 作品内容: 一部思辨影片：主人公借助光遗传学与头戴设备恢复视力，并能在红外、增强叠加等常人肉眼看不到的滤镜视图之间切换。
- 实现方式: 以光遗传视网膜研究为基础的设计虚构影片，配以可视化的界面滤镜。
- 视角: 机器之眼, 具身与动觉
- 视频: https://vimeo.com/22616192
- 项目主页: https://superflux.in

#### 伊芙的时间（Time of Eve） — 吉浦康裕 (2008)
- 类型: 电影与影像 · 机器: 类人机器人
- 核心想法: 对机器的伦理与其说在法律中，不如说在把它们当物件对待的日常小习惯中受到考验。
- 作品内容: 一部动画，设定在家用仿真人普及的近未来：故事发生在一家咖啡馆，那里唯一的规则是不得区分人类与机器人。
- 实现方式: 六集网络动画（2008–09）与一部剧场版（2010）；故事在日本家庭生活中重新演绎阿西莫夫的机器人三定律。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 视频: https://www.youtube.com/watch?v=5CrNNs-37As
- 图片: https://upload.wikimedia.org/wikipedia/en/f/fa/Ivu_no_Jikan_poster.jpeg
- 项目主页: https://en.wikipedia.org/wiki/Time_of_Eve

#### I.K.U. — 郑淑丽 (2000)
- 类型: 电影与影像 · 机器: 义体与赛博格, 数据集与训练数据
- 核心想法: 欲望变成了数据采集，赛博格身体就是采集设备。
- 作品内容: 一部“日本科幻色情长片”，大致回应《银翼杀手》：公司派出可变形的复制人进入“新东京”，收集人类高潮数据，再作为数字快感产品出售。
- 实现方式: 在东京拍摄的长片，运用数字特效与界面图形；首映于圣丹斯。
- 视角: 具身与动觉, 隐形劳动与攫取
- 展出与获奖: Sundance Film Festival 2000
- 视频: https://www.youtube.com/watch?v=JVr9q2BW6rI
- 图片: https://upload.wikimedia.org/wikipedia/en/1/1d/IKU_poster.jpg
- 项目主页: https://en.wikipedia.org/wiki/I.K.U.

#### 铁臂阿童木（Astro Boy (Tetsuwan Atom)） — 手冢治虫 (1952)
- 类型: 书与文章 · 机器: 类人机器人
- 核心想法: 把机器人想象成有情感、有权利的孩子，塑造了东亚与机器共处的想象。
- 作品内容: 一部漫画：一位丧子的科学家造出机器人男孩来代替死去的儿子，随后又抛弃了他；阿童木在人类中生活，并在“机器人法”下为机器人的权利而战。
- 实现方式: 1952 至 1968 年在光文社《少年》杂志连载；1963 年改编为日本第一部电视动画连续剧。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://en.wikipedia.org/wiki/Astro_Boy (Shōnen (Kobunsha), 1952–1968)
- 视频: https://www.youtube.com/watch?v=d3UbaB7oPTw
- 图片: https://upload.wikimedia.org/wikipedia/en/a/a6/Astro_Boy-08.jpg
- 项目主页: https://en.wikipedia.org/wiki/Astro_Boy

### 设计研究：以机器为材料

把机器学习和机器人当作设计材料与“他者”的 HCI 与设计研究。

#### 我们可以设计的事物：面向超越人类中心的世界（Things We Could Design: For More Than Human-Centered Worlds） — Ron Wakkary (2021)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 机器生物与移动机器人
- 核心想法: 设计师可以学会与物一起设计、为物设计，而不仅仅为用户设计。
- 作品内容: 一本主张设计应超越“以人为中心”的书：把物（包括计算性的物）当作拥有自身存在的参与者。
- 实现方式: 结合 Wakkary 的研究产品（Morse Things、Tilting Bowl 等）的后人类主义设计理论，由 MIT Press 出版。
- 视角: 机器环世界, 能动、自主与共创
- 论文: https://doi.org/10.7551/mitpress/13649.001.0001 (MIT Press 2021)
- 视频: https://vimeo.com/512886973
- 图片: https://covers.openlibrary.org/b/id/14137399-L.jpg
- 项目主页: https://mitpress.mit.edu/9780262542999/things-we-could-design/

#### 超越人类的设计与 AI：与智能体对话（More-Than-Human Design and AI: In Conversation with Agents） — Iohanna Nicenboim, Elisa Giaccardi (2020)
- 类型: 论文 · 机器: 语音与听觉机器, 聊天机器人与语言模型
- 核心想法: 把 AI 当作参与者来交谈，能暴露它的预设，也让“超越人类的设计”变得具体。
- 作品内容: 设计师在家庭环境中像访谈研究参与者一样“采访”对话式智能体，把它们当作有自身视角的他者而不是工具。
- 实现方式: 针对语音助手的设计研究，包括访谈脚本与设计物件，发表于 DIS 2020（Nicenboim、Giaccardi、Søndergaard、Reddy、Strengers、Pierce、Redström）。
- 视角: 他异与恐怖谷, 机器环世界
- 论文: https://doi.org/10.1145/3393914.3395912 (DIS 2020 Companion)
- 视频: https://www.youtube.com/watch?v=CJKwKQG_heI
- 图片: https://payload.cargocollective.com/1/4/137851/14306494/IMG_5103_670.jpg
- 项目主页: https://iohanna.com/More-than-human-AI

#### 重新审视人–AI 交互是否、为何以及如何格外难以设计（Re-examining Whether, Why, and How Human-AI Interaction Is Uniquely Difficult to Design） — Qian Yang (2020)
- 类型: 论文 · 机器: 平台与推荐算法, 聊天机器人与语言模型
- 核心想法: AI 是一种无法事先完整勾画其行为的设计材料，设计方法必须正视这一点。
- 作品内容: 一篇分析为什么与 AI 一起做设计特别困难的论文，把困难归结为两个来源：对系统能力的不确定，以及其可能输出的复杂性。
- 实现方式: 综合既有研究、作者的设计项目与教学经验，提出 AI 设计复杂度的四层框架（Yang、Steinfeld、Rosé 与 Zimmerman，CHI 2020）。
- 视角: 不透明与潜空间, 失败、故障与错误
- 论文: https://doi.org/10.1145/3313831.3376301 (CHI 2020)
- 项目主页: https://doi.org/10.1145/3313831.3376301

#### 再具身与共具身（Re-Embodiment and Co-Embodiment） — Michal Luria (2019)
- 类型: 论文 · 机器: 社交与陪伴机器人, 语音与听觉机器
- 核心想法: AI 的身份不必绑定在一个身体上，这打破了我们从身体读取心智的习惯。
- 作品内容: 通过用户情境扮演，研究一个社交智能体从一个机器人身体转移到另一个身体（再具身），或多个智能体共享一个身体（共具身）时，人们如何判断自己在和“谁”说话。
- 实现方式: 在模拟服务场景中使用机器人与对话智能体进行思辨性情境扮演（Luria、Reig、Tan、Steinfeld、Forlizzi 与 Zimmerman，DIS 2019）。
- 视角: 具身与动觉, 他异与恐怖谷
- 论文: https://doi.org/10.1145/3322276.3322340 (DIS 2019)
- 项目主页: https://doi.org/10.1145/3322276.3322340

#### 椅子计划（四件经典）（The Chair Project (Four Classics)） — Philipp Schmitt, Steffen Weiß (2019)
- 类型: 思辨设计 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 把模型的误解当作激发人类想象的线索，颠倒“人设计、机器制造”的惯常顺序。
- 作品内容: 四把椅子：先由一个用 562 把经典椅子训练的生成网络画出模糊草图，再由人手工制作；成品像一群忘记了坐着的身体是什么的设计经典。
- 实现方式: 用 20 世纪经典设计椅子的图像训练 GAN 生成草图，再由设计师把它们诠释为四件木、钢与线材制成的原型。
- 视角: 能动、自主与共创, 不透明与潜空间
- 展出与获奖: Uncanny Values, MAK Vienna 2019
- 图片: https://cdn.philippschmitt.com/media/pages/work/chair/bffd079351-1586822724/philipp-schmitt_chairs-0-1200x630-crop.jpg https://cdn.philippschmitt.com/media/pages/work/chair/b049157868-1586890370/philipp-schmitt_chairs-1-1200x.jpg
- 项目主页: https://philippschmitt.com/work/chair

#### Believe it Yourself — automato.farm (2018)
- 类型: 研究原型 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 一个训练好的模型就是一种信仰体系：它看到的，是数据教它看到的东西。
- 作品内容: 一套“真实—虚构”的机器学习套件，用信仰体系（意大利迷信、风水、占星）训练，让业余者自制能“透过某种信念”看世界的摄像头。
- 实现方式: 带摄像头的模块化硬件套件，内置用信念数据集训练的分类器，配有说明书和海报。
- 视角: 分类、偏见与监控, 机器之眼
- 视频: https://vimeo.com/339396770
- 图片: http://www.automato.farm/img/BIY_posters.png
- 项目主页: http://www.automato.farm/portfolio/believe_it_yourself/

#### 作为能动者的产品：物联网时代产品设计的隐喻（Products as Agents: Metaphors for Designing the Products of the IoT Age） — Nazli Cila, Elisa Giaccardi (2017)
- 类型: 论文 · 机器: 平台与推荐算法, 社交与陪伴机器人
- 核心想法: 一旦产品拥有能动性，设计师就需要隐喻来描述人与它们之间将会是什么样的关系。
- 作品内容: 为能够自行行动的智能产品提出三种隐喻：作为数据的“收集者”、作为做决定的“行动者”、作为与人共同创造的“创造者”。
- 实现方式: 通过设计工作坊和思辨产品概念的分析归纳出这些隐喻（Cila、Smit、Giaccardi 与 Kröse，CHI 2017）。
- 视角: 能动、自主与共创, 他异与恐怖谷
- 论文: https://doi.org/10.1145/3025453.3025797 (CHI 2017)
- 图片: https://images.squarespace-cdn.com/content/v1/5f6312c65070bb0554a3d6e3/1602250220682-DE0ZFGIJR9K9HJYZT1BS/Smart%2Bsink.jpg
- 项目主页: https://nazlicila.com/projects/human-agent-partnerships

#### Teachable Machine — Google Creative Lab (2017)
- 类型: 产品与平台 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 让人在一分钟内训练出一个模型，就能直接感受到它对示例的依赖以及它会犯的错。
- 作品内容: 一个网页工具，任何人都可以对着摄像头示范几个例子，在浏览器里训练图像、声音或姿势分类器，无需写代码。
- 实现方式: 在浏览器中用 TensorFlow.js 对预训练网络做迁移学习，全部在本地运行；2019 年的 2.0 版加入了模型导出。
- 视角: 能动、自主与共创, 机器之眼
- 视频: https://www.youtube.com/watch?v=T2qQGqZxkD0
- 项目主页: https://teachablemachine.withgoogle.com/

#### 用户体验设计创新：以机器学习为设计材料的挑战（UX Design Innovation: Challenges for Working with Machine Learning as a Design Material） — Graham Dove (2017)
- 类型: 论文 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 设计师需要像处理木材或代码一样处理机器学习，用它的行为来“画草图”，而不只是从工程师那里接手。
- 作品内容: 一项针对用户体验从业者的调查：设计师难以理解机器学习能做什么，也难以用它做原型；论文主张把机器学习当作一种设计材料。
- 实现方式: 对 51 位用户体验设计师的调查，并分析设计教育与工具（Dove、Halskov、Forlizzi 与 Zimmerman，CHI 2017）。
- 视角: 能动、自主与共创, 不透明与潜空间
- 论文: https://doi.org/10.1145/3025453.3025739 (CHI 2017)
- 项目主页: https://doi.org/10.1145/3025453.3025739

#### 泛灵论设计（Animistic Design） — Betti Marenko, Philip van Allen (2016)
- 类型: 论文 · 机器: 社交与陪伴机器人, 平台与推荐算法
- 核心想法: 与其做一个全知的助手，不如设计一个由偏执而局部的物组成的社会，让人能够与它们的不确定共处。
- 作品内容: 主张用“万物有灵”来设计智能物件：许多带有各自性格和意图的小设备，彼此之间以及与人之间相互协商；以 van Allen 的 AniThings 为例。
- 实现方式: 借助哲学与人类学的理论论证，配合具有性格的联网物件原型（Marenko 与 van Allen，《Digital Creativity》2016）。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.1080/14626268.2016.1145127 (Digital Creativity 27(1), 2016)
- 视频: https://www.youtube.com/watch?v=OhuDZ877KIY
- 项目主页: https://doi.org/10.1080/14626268.2016.1145127

#### 物的民族志：与非人一起做设计研究（Thing Ethnography: Doing Design Research with Non-Humans） — Elisa Giaccardi (2016)
- 类型: 论文 · 机器: 计算机视觉, 基础设施、能源与供应链
- 核心想法: 物可以成为研究伙伴：它们的传感器视角揭示出人们注意不到、也不会讲出来的使用模式。
- 作品内容: 研究者把摄像头和传感器装在家中的日常物件（水壶、杯子、冰箱）上，让设计师从“物”的视角研究日常生活。
- 实现方式: 装在家居物件上的 Autographer 相机产生图像流，与访谈一起分析（Giaccardi、Cila、Speed 与 Caldwell，DIS 2016）。
- 视角: 机器环世界, 机器之眼
- 论文: https://doi.org/10.1145/2901790.2901905 (DIS 2016)
- 视频: https://www.youtube.com/watch?v=1Z0mVcV1EgA
- 项目主页: https://doi.org/10.1145/2901790.2901905

#### 算法教师（Teacher of Algorithms） — automato.farm (2015)
- 类型: 电影与影像 · 机器: 平台与推荐算法, 社交与陪伴机器人
- 核心想法: 家中的机器学习需要人类老师，而这种教学可能会成为一份工作。
- 作品内容: 一部短片：近未来有一种职业，专门替别人训练智能物件，像训练宠物一样奖励和惩罚它们，因为“会学习”的产品其实并不擅长自学。
- 实现方式: 使用道具智能物件和训练工具拍摄的设计虚构短片，由 Simone Rebaudengo 与 Yosuke Ushigome 制作。
- 视角: 隐形劳动与攫取, 能动、自主与共创
- 视频: https://vimeo.com/125768041
- 图片: http://www.automato.farm/img/training.jpg http://www.automato.farm/img/punish.jpg
- 项目主页: http://www.automato.farm/portfolio/teach_algorithms/

#### Wekinator — Rebecca Fiebrink (2009)
- 类型: 研究原型 · 机器: 数据集与训练数据, 义体与赛博格
- 核心想法: 交互式、基于示范的训练让人处在回路之中，把机器学习变成可以演奏和雕琢的东西，而不是需要配置的系统。
- 作品内容: 一款免费软件，让音乐人和艺术家通过示范手势与声音来训练机器学习模型，使机器学习成为制作乐器的材料。
- 实现方式: 对用户录制的示例进行监督学习，通过 OSC 把任意输入（摄像头、传感器、控制器）映射到任意输出，并可快速重新训练。
- 视角: 能动、自主与共创, 具身与动觉
- 视频: https://www.youtube.com/watch?v=NKyyBAKrQgE
- 项目主页: http://www.wekinator.org/

## 理论与奠基

为机器现象学与批判性 AI 提供框架的文本、实验与研究。

### 控制论与早期 AI

从图灵、维纳到 ELIZA 的奠基实验与文本。

#### 弗洛伊德机器人：数字时代的哲学批判（The Freudian Robot: Digital Media and the Future of the Unconscious） — 刘禾 (2010)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 聊天机器人与语言模型
- 核心想法: 机器时代没有绕开无意识，而是把它重建为人机关系的模型。
- 作品内容: 一本书，把香农信息论、控制论、拉康与弗洛伊德放在一起阅读，指出数字媒介建立在一种关于无意识的理论之上。
- 实现方式: 媒介考古，细读香农的书面英语统计、控制论文本与精神分析。
- 视角: 不透明与潜空间, 他异与恐怖谷
- 论文: https://doi.org/10.7208/chicago/9780226486840.001.0001 (University of Chicago Press, 2010)
- 项目主页: https://doi.org/10.7208/chicago/9780226486840.001.0001

#### 小车：合成心理学实验（Vehicles: Experiments in Synthetic Psychology） — Valentino Braitenberg (1984)
- 类型: 书与文章 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 容易造出来的行为，从外部却很难分析，于是观察者会把心智读进简单的机器里。
- 作品内容: 十四辆逐步复杂的想象小车：传感器与电机平行或交叉连接，就让它们看起来害怕、好斗、恋爱或好奇。
- 实现方式: “合成心理学”思想实验：先造，再解释；后来被大量做成机器人和模拟程序。
- 视角: 他异与恐怖谷, 能动、自主与共创, 机器环世界
- 论文: https://mitpress.mit.edu/9780262521123/ (MIT Press, 1984)
- 视频: https://www.youtube.com/watch?v=A-fxij3zM7g
- 图片: https://covers.openlibrary.org/b/isbn/9780262521123-L.jpg

#### 计算机能力与人类理性：从判断到计算（Computer Power and Human Reason: From Judgment to Calculation） — Joseph Weizenbaum (1976)
- 类型: 书与文章 · 机器: 聊天机器人与语言模型
- 核心想法: 问题不在于机器能做什么，而在于我们不应让它们做什么。
- 作品内容: ELIZA 被普通人和精神科医生热情接受，这让 Weizenbaum 深感不安。他在书中主张：治疗、审判、照护等工作即便计算机能做，也不应交给它。
- 实现方式: 一部专著篇幅的伦理论证，依据他自己的编程经验以及工具理性的历史。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason (W. H. Freeman, 1976)
- 图片: https://covers.openlibrary.org/b/id/15228817-L.jpg https://upload.wikimedia.org/wikipedia/commons/f/fd/Weizenbaum_1982.jpg

#### 人机共生（Man-Computer Symbiosis） — J. C. R. Licklider (1960)
- 类型: 论文 · 机器: 义体与赛博格, 控制论与人工生命系统
- 核心想法: 机器被设想为思考的伙伴，而不是思考者的替代品。
- 作品内容: Licklider 提议让人与计算机实时耦合：机器处理例行工作，人设定目标并作判断，就像无花果树与为它授粉的黄蜂。
- 实现方式: 一篇立场论文，基于他对自己工作日的时间动作研究，并提出对分时、存储与界面的要求。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.1109/THFE2.1960.4503259 (IRE Transactions on Human Factors in Electronics HFE-1, 1960)
- 视频: https://www.youtube.com/watch?v=ncCPTgWX6a8
- 图片: https://upload.wikimedia.org/wikipedia/commons/e/e6/Portrait_of_J._C._R._Licklider.jpg

#### 达特茅斯人工智能夏季研究项目提案（A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence） — John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon (1955)
- 类型: 论文 · 机器: 控制论与人工生命系统, 聊天机器人与语言模型
- 核心想法: AI 始于一个赌注：“学习的每个方面或智能的任何其他特征”都可以被精确描述，从而由机器模拟。
- 作品内容: 为 1956 年达特茅斯学院两个月研讨会撰写的资助申请书，“人工智能”一词首次出现于此；它把语言、神经网络、抽象、自我改进与创造力列为待解决的问题。
- 实现方式: 一份提交洛克菲勒基金会的简短研究提案，2006 年在《AI Magazine》重刊。
- 视角: 能动、自主与共创
- 论文: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904 (Dartmouth College, 1955; reprinted in AI Magazine 27(4), 2006)
- 图片: https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/John_McCarthy_%28computer_scientist%29_Stanford_2006_%28272020300%29.jpg/1280px-John_McCarthy_%28computer_scientist%29_Stanford_2006_%28272020300%29.jpg
- 项目主页: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904

#### 模仿生命（An Imitation of Life） — W. Grey Walter (1950)
- 类型: 论文 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 类似生命的行为可以来自少数连接与环境的互动，而不是内部的复杂性。
- 作品内容: Grey Walter 在《科学美国人》上介绍他的机器龟 Elmer 与 Elsie：它们四处游走、寻找适度的光、避开障碍、回窝充电，还会在镜子前“跳舞”。
- 实现方式: 两个电子管“神经元”、一个光传感器和一个碰撞触点，在反馈回路中驱动转向与车轮电机。
- 视角: 能动、自主与共创, 具身与动觉, 他异与恐怖谷
- 论文: https://doi.org/10.1038/scientificamerican0550-42 (Scientific American 182(5), 1950)
- 图片: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Cybernetic_Tortoise_by_William_Grey_Walter_c_1950_%28Ank_Kumar%29.jpg/1280px-Cybernetic_Tortoise_by_William_Grey_Walter_c_1950_%28Ank_Kumar%29.jpg

#### 计算机器与智能（Computing Machinery and Intelligence） — Alan Turing (1950)
- 类型: 论文 · 机器: 聊天机器人与语言模型, 控制论与人工生命系统
- 核心想法: 机器智能从一开始就被定义为由人评判的表演，而不是内在状态。
- 作品内容: 图灵把“机器能思考吗？”换成“模仿游戏”：裁判通过电传打字机与隐藏的人和隐藏的机器对话；随后他逐一回应了反对机器思维的九种意见。
- 实现方式: 思想实验加哲学论证；文中还设想了一台通过学习而非完全编程成长的“儿童机器”。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.1093/mind/LIX.236.433 (Mind 59(236), 1950)
- 图片: https://upload.wikimedia.org/wikipedia/commons/f/f8/Alan_Turing_%281951%29.jpg
- 项目主页: https://www.turing.org.uk

#### 控制论：或关于在动物和机器中控制和通信的科学（Cybernetics: Or Control and Communication in the Animal and the Machine） — Norbert Wiener (1948)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 义体与赛博格
- 核心想法: 一旦生物与机器共享同一套反馈逻辑，机器就可以表现得像是有目的。
- 作品内容: 为“控制论”命名的著作：维纳把反馈、信息与控制描述为神经系统、伺服机构与计算机器共有的原理。
- 实现方式: 由战时防空火控预测、神经生理学与统计力学发展出的数学理论。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://doi.org/10.7551/mitpress/11810.001.0001 (Technology Press / John Wiley, 1948; MIT Press reissue 2019)
- 视频: https://www.youtube.com/watch?v=QJWDJvbea0M
- 图片: https://covers.openlibrary.org/b/id/152654-L.jpg
- 项目主页: https://mitpress.mit.edu/9780262537841/

### 哲学与机器现象学

后现象学、技术哲学，以及“成为机器”的哲学思考。

#### 与逝者在线交流：聊天机器人、哀悼与持续联结（Communing with the Dead Online: Chatbots, Grief, and Continuing Bonds） — Joel Krueger, Lucy Osler (2022)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 哀悼机器人的意义也许不在于复制逝者，而在于让一段关系得以继续被实践。
- 作品内容: Krueger 与 Osler 分析用逝者文本训练的聊天机器人，认为它们可以维系哀悼者与逝者之间的亲密习惯，从而支持“持续联结”。
- 实现方式: 结合哀伤现象学、持续联结理论，以及用逝者文本构建聊天机器人的案例。
- 视角: 哀悼、记忆与来世, 亲密、照护与陪伴
- 论文: https://doi.org/10.53765/20512201.29.9.222 (Journal of Consciousness Studies 29(9–10), 2022)

#### 非人之言：作为哲学实验室的GPT-3（Non-Human Words: On GPT-3 as a Philosophical Laboratory） — Tobias Rees (2022)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 如果词语可以没有说话者而被生成，那么人/机之分需要重新思考，而不是一味捍卫。
- 作品内容: Rees 认为大语言模型打破了“只有人拥有语言”的现代观念，并把 GPT-3 视为一个实验室，让一种结构性的、非人的语言概念显现出来。
- 实现方式: 刊于《Daedalus》“AI 与社会”专号的哲学文章。
- 视角: 机器之耳与声, 他异与恐怖谷
- 论文: https://doi.org/10.1162/daed_a_01908 (Daedalus 151(2), 2022)
- 视频: https://www.youtube.com/watch?v=DUCIdgCLlf0

#### 非物：生活世界的变革（Non-things: Upheaval in the Lifeworld） — 韩炳哲 (2021)
- 类型: 书与文章 · 机器: 平台与推荐算法, 聊天机器人与语言模型
- 核心想法: 信息圈的现象学：当物变成信息，我们失去了世界的阻力与重量。
- 作品内容: 一组随笔，讨论信息如何取代物：智能手机、智能物件与数据取代了可以握在手里的持久物品；其中一章认为人工智能无法思考，因为它没有身体，也没有情绪。
- 实现方式: 哲学随笔集（德文原版《Undinge》，Ullstein 2021；英译 Daniel Steuer，Polity 2022）。
- 视角: 不透明与潜空间, 具身与动觉
- 论文: https://www.ullstein.de/werke/undinge/hardcover/9783550201257 (Ullstein (German original))
- 项目主页: https://www.ullstein.de/werke/undinge/hardcover/9783550201257

#### 递归与偶然（Recursivity and Contingency） — 许煜 (2019)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 生成模型与潜空间
- 核心想法: 会学习的机器是吸纳偶然性的递归、类有机体系统，这改变了“机器是什么”。
- 作品内容: 一本书，追溯“递归”（把偶然转化为组织的回路逻辑）从康德、德国观念论经控制论直到今天的机器学习。
- 实现方式: 从康德《判断力批判》到维纳与当代 AI 的有机与机械之哲学史。
- 视角: 能动、自主与共创, 机器环世界
- 论文: https://doi.org/10.5771/9781786600547 (Rowman & Littlefield International, 2019)
- 项目主页: https://doi.org/10.5771/9781786600547

#### AI 的异质主体（The Alien Subject of AI） — Luciana Parisi (2019)
- 类型: 论文 · 机器: 平台与推荐算法, 生成模型与潜空间
- 核心想法: AI 可以被理解为另一种思维逻辑，而不是对我们的模仿。
- 作品内容: Parisi 主张，自动化决策系统并非简单复制人的推理，而是形成一种异质的主体性，动摇了人文主义的理性主体形象。
- 实现方式: 一篇理论文章，借助计算哲学以及对工具理性的批判。
- 视角: 不透明与潜空间, 能动、自主与共创
- 论文: https://doi.org/10.1057/s41286-018-00064-3 (Subjectivity 12(1), 2019)
- 视频: https://www.youtube.com/watch?v=9oGx0ejmdgg

#### 偶然计算：计算美学中的抽象、经验与不确定性（Contingent Computation: Abstraction, Experience, and Indeterminacy in Computational Aesthetics） — M. Beatrice Fazi (2018)
- 类型: 书与文章 · 机器: 控制论与人工生命系统
- 核心想法: 计算机不是人类思维的失败复制品；它们的美学在于自身的偶然性。
- 作品内容: Fazi 主张计算并非封闭、可预测的程序：她借图灵的不可计算性和怀特海哲学说明，形式系统有其自身的不确定性与经验方式。
- 实现方式: 结合怀特海、德勒兹、哥德尔与图灵的哲学论证。
- 视角: 不透明与潜空间, 机器环世界
- 论文: https://doi.org/10.5040/9798881812027 (Rowman & Littlefield International, 2018)
- 视频: https://www.youtube.com/watch?v=NIJnjAs7ysI
- 图片: https://covers.openlibrary.org/b/id/9200964-L.jpg

#### 机器人权利（Robot Rights） — David J. Gunkel (2018)
- 类型: 书与文章 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 道德关怀可能是在相遇中给予的，这让机器人成为检验我们自身伦理的试金石。
- 作品内容: Gunkel 逐一检验“机器人能否、是否应当拥有权利”的四种逻辑回答，并提出受列维纳斯启发的关系性路径：从我们如何遭遇他者出发。
- 实现方式: 对机器人权利争论中“是否能/是否应”各种立场的哲学分析。
- 视角: 他异与恐怖谷
- 论文: https://doi.org/10.7551/mitpress/11444.001.0001 (MIT Press, 2018)
- 视频: https://www.youtube.com/watch?v=YKdBHMDlulw
- 图片: https://covers.openlibrary.org/b/id/8835491-L.jpg

#### 非思：认知非意识的力量（Unthought: The Power of the Cognitive Nonconscious） — N. Katherine Hayles (2017)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 自动驾驶与无人机
- 核心想法: 机器已经在以非意识的方式与我们一同思考；问题在于能动性如何在组合中被分配。
- 作品内容: Hayles 把认知定义得足够宽，以涵盖人、动物与计算机中的非意识过程，并描述了高频交易、无人机集群等人机共同决策的“认知组合”。
- 实现方式: 综合神经科学、媒介研究与案例研究的理论；“认知组合”的论证首见于《Cognitive Assemblages》（Critical Inquiry，2016）。
- 视角: 能动、自主与共创, 机器环世界
- 论文: https://doi.org/10.7208/chicago/9780226447919.001.0001 (University of Chicago Press, 2017)
- 视频: https://www.youtube.com/watch?v=yUsTa01vJpA
- 图片: https://tmm.chicagodistributioncenter.com/IsbnImages/9780226447889.jpg

#### 论数码物的存在（On the Existence of Digital Objects） — 许煜 (2016)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 平台与推荐算法
- 核心想法: 数据对象是一种新的物，具有自然物与技术物之外的关系与存在。
- 作品内容: 一部关于“数码物”（YouTube 视频、Facebook 主页、元数据）的哲学，追问这些数据结构具有怎样的存在，又如何形成新的环境。
- 实现方式: 借助海德格尔、胡塞尔、西蒙东以及标记语言与本体论的历史进行哲学研究。
- 视角: 不透明与潜空间, 机器环世界
- 论文: https://doi.org/10.5749/minnesota/9780816698905.001.0001 (University of Minnesota Press, 2016)
- 图片: https://minnesota-us.imgix.net/covers/9780816698912.jpg?w=400
- 项目主页: https://www.upress.umn.edu/9780816698912/on-the-existence-of-digital-objects/

#### 论中国的技术问题：宇宙技术初论（The Question Concerning Technology in China: An Essay in Cosmotechnics） — 许煜 (2016)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链
- 核心想法: 并不存在唯一普遍的技术；AI 与机器可以从其他宇宙观出发来想象。
- 作品内容: 一本从中国哲学（器与道的关系）重新打开海德格尔技术之问的书，提出“宇宙技术”：每一种技术都与特定的宇宙观相连。
- 实现方式: 以儒家、道家与新儒家思想对读海德格尔、斯蒂格勒与西蒙东的比较哲学。
- 视角: 机器环世界, 能动、自主与共创
- 论文: https://www.urbanomic.com/book/question-concerning-technology-china/ (Urbanomic, 2016)
- 视频: https://www.youtube.com/watch?v=66ivnhe8YF4
- 项目主页: https://www.urbanomic.com/book/question-concerning-technology-china/

#### 堆栈：论软件与主权（The Stack: On Software and Sovereignty） — Benjamin Bratton (2016)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 平台与推荐算法
- 核心想法: 计算不再是世界中的工具，而是我们栖身其中的分层世界。
- 作品内容: Bratton 把星球尺度的计算描述为一个意外形成的六层巨型结构（地球、云、城市、地址、界面、用户），它正与国家争夺主权。
- 实现方式: 融合地缘政治、平台研究与建筑学的设计理论模型。
- 视角: 隐形劳动与攫取, 机器环世界
- 论文: https://doi.org/10.7551/mitpress/9780262029575.001.0001 (MIT Press, 2016)
- 视频: https://www.youtube.com/watch?v=cUhhHw_xS4w
- 图片: https://covers.openlibrary.org/b/id/14832820-L.jpg

#### 异形现象学：成为一个物是什么感觉（Alien Phenomenology, or What It's Like to Be a Thing） — Ian Bogost (2012)
- 类型: 书与文章 · 机器: 控制论与人工生命系统
- 核心想法: 我们只能通过隐喻把握机器的经验，而制作东西正是做这种哲学的正当方式。
- 作品内容: Bogost 把物导向本体论用于计算机和其他物，并提出推想物之经验的方法：本体图志（物的清单）、隐喻论，以及“木工”，即制作能承载哲学的物件。
- 实现方式: 以 Atari 2600 以及他自己的小程序（如 I Am TIA）为案例的哲学论著。
- 视角: 机器环世界, 他异与恐怖谷
- 论文: https://doi.org/10.5749/9780816681426 (University of Minnesota Press, 2012)
- 视频: https://www.youtube.com/watch?v=Z1V2z3wjtqo
- 图片: https://minnesota-us.imgix.net/covers/9780816678983.jpg?w=400

#### 人、动物与机器人：人—机器人关系的现象学进路（Humans, Animals, and Robots: A Phenomenological Approach to Human-Robot Relations） — Mark Coeckelbergh (2011)
- 类型: 论文 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 机器人的道德地位来自我们与它的关系，而不是一张内在属性的清单。
- 作品内容: Coeckelbergh 主张，在人与机器人的关系中，关键是机器人在经验中如何向我们显现；他还把人与机器人的关系同人与动物的关系相比较。
- 实现方式: 现象学与关系论分析；在其专著《Growing Moral Relations》（2012）中进一步展开。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://doi.org/10.1007/s12369-010-0075-6 (International Journal of Social Robotics 3(2), 2011)

#### 赛博格意向性：重思人—技术关系的现象学（Cyborg Intentionality: Rethinking the Phenomenology of Human–Technology Relations） — Peter-Paul Verbeek (2008)
- 类型: 论文 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 机器不只是延伸我们的感官，它们带来自己的感知，而艺术作品能让我们体验到这种感知。
- 作品内容: Verbeek 在 Ihde 之外补充两种关系：技术与身体融合的“混合意向性”，以及设备自身的感知方式（如红外相机）叠加到人的感知上的“复合意向性”。
- 实现方式: 一篇哲学论文，以植入物、成像技术和艺术为例拓展后现象学。
- 视角: 具身与动觉, 机器之眼, 机器环世界
- 论文: https://doi.org/10.1007/s11097-008-9099-x (Phenomenology and the Cognitive Sciences 7(3), 2008)
- 视频: https://www.youtube.com/watch?v=FVhrLwBNbvU

#### 机器人有环世界吗？对雅各布·冯·于克斯屈尔质性生物符号学的思考（Does a Robot Have an Umwelt? Reflections on the Qualitative Biosemiotics of Jakob von Uexküll） — Claus Emmeche (2001)
- 类型: 论文 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 感觉运动耦合也许能给机器人一个世界，但这个世界是否“被经历”仍悬而未决。
- 作品内容: Emmeche 追问：一个通过传感器与电机与环境耦合的情境机器人，能否拥有“环世界”，即 Uexküll 认为动物才有的、充满意义的感知世界。
- 实现方式: 对行为主义机器人学的生物符号学分析，刊于《Semiotica》Uexküll 专号。
- 视角: 机器环世界
- 论文: https://doi.org/10.1515/semi.2001.048 (Semiotica 134, 2001)

#### 我们何以成为后人类：文学、信息科学和控制论中的虚拟身体（How We Became Posthuman: Virtual Bodies in Cybernetics, Literature, and Informatics） — N. Katherine Hayles (1999)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 义体与赛博格
- 核心想法: 把心智当作无身体的信息，是一种历史选择，被它遗漏的恰恰是身体。
- 作品内容: Hayles 讲述信息如何经由梅西控制论会议以及战后的科学与科幻“失去身体”，并主张一种具身的后人类，而不是意识上传的幻想。
- 实现方式: 控制论思想史研究，并与 Philip K. Dick、Bernard Wolfe 等人的小说对读。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.7208/chicago/9780226321394.001.0001 (University of Chicago Press, 1999)
- 视频: https://www.youtube.com/watch?v=rryjPdKMxO4
- 图片: https://tmm.chicagodistributioncenter.com/IsbnImages/9780226321462.jpg

#### 延展心灵（The Extended Mind） — Andy Clark, David Chalmers (1998)
- 类型: 论文 · 机器: 义体与赛博格
- 核心想法: 心智的边界由功能而非皮肤决定，因此我们的设备可能早已是我们的一部分。
- 作品内容: Clark 与 Chalmers 主张，当笔记本这样的设备可靠地承担记忆功能时，它就是心智的一部分：Otto 的笔记本与 Inga 的生物记忆同样算数。
- 实现方式: 基于“对等原则”和思想实验的简短哲学论证。
- 视角: 具身与动觉
- 论文: https://doi.org/10.1093/analys/58.1.7 (Analysis 58(1), 1998)
- 视频: https://www.youtube.com/watch?v=kc-TdMjuJRU

#### 技术与生活世界：从伊甸园到尘世（Technology and the Lifeworld: From Garden to Earth） — Don Ihde (1990)
- 类型: 书与文章 · 机器: 义体与赛博格, 计算机视觉
- 核心想法: 每件机器作品都把我们置于其中一种关系，而有意思的作品会在几种关系之间切换。
- 作品内容: Ihde 把人与技术的关系分为四类：具身（透过眼镜看）、诠释（读温度计）、他异（把设备当作准他者面对）和背景（不被察觉的环境）。
- 实现方式: 对具体仪器的后现象学分析，通过案例研究延展胡塞尔与海德格尔。
- 视角: 具身与动觉, 他异与恐怖谷, 机器之眼
- 论文: https://doi.org/10.2979/3108.0 (Indiana University Press, 1990)
- 视频: https://www.youtube.com/watch?v=UiRkzZEMDxU
- 图片: https://ingram-indiana.imgix.net/covers/9780253205605.jpg?w=400
- 项目主页: https://iupress.org/9780253205605/technology-and-the-lifeworld/

#### 赛博格宣言：20世纪80年代的科学、技术与社会主义女性主义（A Manifesto for Cyborgs: Science, Technology, and Socialist Feminism in the 1980s） — Donna Haraway (1985)
- 类型: 书与文章 · 机器: 义体与赛博格
- 核心想法: 赛博格拒绝起源与纯粹，这让人机混杂成为政治上的出口，而不是损失。
- 作品内容: Haraway 的这篇文章把赛博格（机器与有机体的混合体）当作女性主义的反讽政治神话；它出现在人与动物、有机体与机器、物质与非物质的边界已经崩塌之后。
- 实现方式: 融合社会主义女性主义、科学研究与科幻的政治文章；收入《Simians, Cyborgs, and Women》（1991）。
- 视角: 具身与动觉, 他异与恐怖谷
- 论文: https://doi.org/10.4324/9780203873106 (Socialist Review 80, 1985; in Simians, Cyborgs, and Women (Routledge, 1991))
- 图片: https://covers.openlibrary.org/b/id/902702-L.jpg

#### 摄影哲学的思考（Towards a Philosophy of Photography） — Vilém Flusser (1983)
- 类型: 书与文章 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 使用装置的人也被其程序所使用；这一点可以直接套用到生成模型上。
- 作品内容: Flusser 把相机描述为一种“装置”：一个黑箱，摄影师只是在它的程序内游戏，产出的“技术图像”不过实现了设备中早已写好的可能性。
- 实现方式: 一部简短的哲学论著；德文原版《Für eine Philosophie der Fotografie》（European Photography，1983）。
- 视角: 不透明与潜空间, 机器之眼
- 论文: https://www.reaktionbooks.co.uk/work/towards-a-philosophy-of-photography (European Photography, 1983; English: Reaktion Books, 2000)
- 图片: https://covers.openlibrary.org/b/id/917481-L.jpg

#### 机器人中的佛陀（The Buddha in the Robot） — 森政弘 (1981)
- 类型: 书与文章 · 机器: 类人机器人, 机器生物与移动机器人
- 核心想法: 一个非西方的框架：机器不与心灵对立，而处在同一个连续体中。
- 作品内容: 森政弘在书中从禅宗出发指出：机器人同样具有佛性，制造机器人也是理解自我的一种途径。
- 实现方式: 一位机器人工程师的随笔与讲演集，由日文译出，东京佼成出版社出版。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://openlibrary.org/works/OL5531608W (Kosei Publishing, Tokyo, 1981)
- 图片: https://covers.openlibrary.org/b/id/6620832-L.jpg
- 项目主页: https://openlibrary.org/works/OL5531608W

#### 心灵、大脑与程序（Minds, Brains, and Programs） — John Searle (1980)
- 类型: 论文 · 机器: 聊天机器人与语言模型
- 核心想法: 流畅的输出并不证明背后有心智，这正是今天的聊天机器人重新提出的问题。
- 作品内容: Searle 的“中文屋”：一个不懂中文的人照着规则手册给出流利的中文回答；他据此论证，运行程序并不等于理解。
- 实现方式: 一个思想实验，与多篇同行公开评论及 Searle 的回应一同发表。
- 视角: 他异与恐怖谷, 不透明与潜空间
- 论文: https://doi.org/10.1017/S0140525X00005756 (Behavioral and Brain Sciences 3(3), 1980)
- 视频: https://www.youtube.com/watch?v=6tzjcnPsZ_w

#### 计算机不能做什么（What Computers Can't Do: A Critique of Artificial Reason） — Hubert Dreyfus (1972)
- 类型: 书与文章 · 机器: 控制论与人工生命系统
- 核心想法: 智能需要身体与世界；缺了它们的机器，恰恰在日常技能开始的地方崩溃。
- 作品内容: Dreyfus 援引海德格尔和梅洛-庞蒂指出，符号主义 AI 注定失败，因为人的智能依赖具身的、情境化的实践背景，而这无法写成规则。
- 实现方式: 对 1960 年代 AI 研究预设的现象学批判；修订版为《What Computers Still Can't Do》（MIT Press，1992）。
- 视角: 具身与动觉, 失败、故障与错误
- 论文: https://mitpress.mit.edu/9780262540674/ (Harper & Row, 1972; rev. MIT Press, 1992)
- 视频: https://www.youtube.com/watch?v=474A0MAS-Dk
- 图片: https://covers.openlibrary.org/b/id/151382-L.jpg

#### 论技术物的存在模式（On the Mode of Existence of Technical Objects） — Gilbert Simondon (1958)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 基础设施、能源与供应链
- 核心想法: 机器有自己的生成与环境；理解机器本身就是一种文化，而不是对文化的威胁。
- 作品内容: Simondon 描述技术物如何随时间变得更“具体化”、更自洽，如何与周围环境构成“关联环境”，以及忽视机器的文化为何会自我异化。
- 实现方式: 以发动机、电子管等技术谱系为例的哲学史研究；英译本由 Cécile Malaspina 与 John Rogove 翻译（Univocal，2017）。
- 视角: 能动、自主与共创, 机器环世界
- 论文: https://www.upress.umn.edu/9781517904876/on-the-mode-of-existence-of-technical-objects/ (Aubier, 1958; English: Univocal / University of Minnesota Press, 2017)
- 图片: https://minnesota-us.imgix.net/covers/9781517904876.jpg?w=400

### 批判性 AI 研究

关于 AI 的政治、劳动、偏见与权力的著作和论文。

#### 主人之眼：人工智能的社会史（The Eye of the Master: A Social History of Artificial Intelligence） — Matteo Pasquinelli (2023)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 数据集与训练数据
- 核心想法: AI 自动化的是劳动组织；它的“智能”是被捕获为数据的人类集体技能。
- 作品内容: Pasquinelli 从巴贝奇的工厂计算一路追溯到感知机与神经网络，论证 AI 模仿的是劳动分工与工人的集体知识，而不是大脑。
- 实现方式: 借助马克思、统计史与控制论史写成的社会史；获 2024 年 Deutscher 纪念奖。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 论文: https://www.versobooks.com/products/735-the-eye-of-the-master (Verso, 2023)
- 视频: https://www.youtube.com/watch?v=U0wECTKNmlY
- 图片: https://covers.openlibrary.org/b/id/14569589-L.jpg

#### 如何解读一张AI图像（How to Read an AI Image） — Eryk Salvaggio (2022)
- 类型: 书与文章 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 生成图像是其背后档案的证据，这正是以批判方式纳入生成式作品的途径。
- 作品内容: Salvaggio 提议把每张生成图像当作“关于数据集的信息图”来读：其中的重复、俗套与缺席，显示了训练数据过度或不足呈现的内容。
- 实现方式: 用媒介研究的细读方法分析成批的扩散模型输出，类似对照片做符号学分析。
- 视角: 不透明与潜空间, 机器之眼
- 论文: https://cyberneticforests.substack.com/p/how-to-read-an-ai-image (Cybernetic Forests, 2022)
- 视频: https://www.youtube.com/watch?v=FZB3o5WTVm8
- 图片: https://substackcdn.com/image/fetch/$s_!tOVn!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F941fd849-5808-4de6-97d5-b405ea6c4573_1024x1024.png

#### 技术之外：社会联结中的人工智能（Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence） — Kate Crawford (2021)
- 类型: 书与文章 · 机器: 基础设施、能源与供应链, 数据集与训练数据, 监控与生物识别
- 核心想法: 要看清 AI，就要绘出它攫取了什么：土地、劳动、数据和人的分类。
- 作品内容: Crawford 从锂矿、亚马逊仓库出发，经由训练数据与分类，一直追踪到情绪识别与国家权力，论证 AI 既不“人工”也不“智能”，而是一个物质产业。
- 实现方式: 在矿山、仓库与档案馆的田野调查，结合分类史研究。
- 视角: 隐形劳动与攫取, 分类、偏见与监控
- 论文: https://doi.org/10.12987/9780300252392 (Yale University Press, 2021)
- 视频: https://www.youtube.com/watch?v=0PqrZ2lqT70
- 图片: https://covers.openlibrary.org/b/id/14420723-L.jpg

#### 歧视性数据（Discriminating Data） — Wendy Hui Kyong Chun (2021)
- 类型: 书与文章 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 预测系统不只是反映偏见；它们“相似者会聚集”的假设本身就在制造隔离。
- 作品内容: 一本书，揭示机器学习与网络科学如何继承优生学与隔离逻辑：相关性与“同质相吸”把人分进由相似者组成的“邻里”。
- 实现方式: 对统计学、优生学与网络分析的批判史，并细读推荐系统与机器学习方法。
- 视角: 分类、偏见与监控
- 论文: https://doi.org/10.7551/mitpress/14050.001.0001 (MIT Press, 2021)
- 项目主页: https://doi.org/10.7551/mitpress/14050.001.0001

#### 论随机鹦鹉的危害：语言模型太大有坏处吗？（On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?） — Emily M. Bender, Timnit Gebru (2021)
- 类型: 论文 · 机器: 聊天机器人与语言模型, 数据集与训练数据, 基础设施、能源与供应链
- 核心想法: 语言模型拼接的是没有意义的形式；连贯性存在于读者眼中。
- 作品内容: Bender、Gebru、Angelina McMillan-Major 与 Margaret Mitchell 指出越来越大的语言模型带来的环境成本、无记录的训练数据、内嵌偏见以及“有意义”的假象；这篇论文的内部审查导致 Gebru 离开谷歌。
- 实现方式: 对自然语言处理文献中关于规模、能耗、数据记录与偏见的批判性综述。
- 视角: 不透明与潜空间, 分类、偏见与监控, 隐形劳动与攫取
- 论文: https://doi.org/10.1145/3442188.3445922 (FAccT 2021)
- 视频: https://www.youtube.com/watch?v=N5c2X8vhfBE

#### 数据女性主义（Data Feminism） — Catherine D'Ignazio, Lauren F. Klein (2020)
- 类型: 书与文章 · 机器: 数据集与训练数据
- 核心想法: 数据从来不是“原始”的；谁收集、统计谁、遗漏谁，都是女性主义的问题。
- 作品内容: D'Ignazio 与 Klein 提出七条原则（从审视权力到让劳动可见），用来以挑战而非强化不平等的方式从事数据科学。
- 实现方式: 把交叉性女性主义理论用于数据项目的案例研究；在线开放获取。
- 视角: 分类、偏见与监控
- 论文: https://doi.org/10.7551/mitpress/11805.001.0001 (MIT Press, 2020)
- 视频: https://www.youtube.com/watch?v=pmNEe6FvduM
- 图片: https://covers.openlibrary.org/b/isbn/9780262044004-L.jpg

#### 销声匿迹：数字化工作的真正未来（Ghost Work: How to Stop Silicon Valley from Building a New Global Underclass） — Mary L. Gray, Siddharth Suri (2019)
- 类型: 书与文章 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 自动化承诺的背后，总有一段由隐形人类劳动完成的“最后一公里”。
- 作品内容: Gray 与 Suri 描述了在应用和“AI”背后标注数据、审核内容、校验输出的按需劳动者，他们在美国与印度通过 Amazon Mechanical Turk、UHRS 等平台工作。
- 实现方式: 对众包劳动者进行的五年民族志、问卷与实验研究。
- 视角: 隐形劳动与攫取
- 论文: https://ghostwork.info (Houghton Mifflin Harcourt, 2019)
- 视频: https://www.youtube.com/watch?v=D5fkupjVEp8
- 图片: https://covers.openlibrary.org/b/id/10131831-L.jpg
- 项目主页: https://ghostwork.info

#### 技术之后的种族：新吉姆代码的废除主义工具（Race After Technology: Abolitionist Tools for the New Jim Code） — Ruha Benjamin (2019)
- 类型: 书与文章 · 机器: 监控与生物识别, 平台与推荐算法
- 核心想法: 歧视可以被工程化地写进看似中立的系统，这就是“新吉姆代码”。
- 作品内容: Benjamin 揭示招聘、医疗、警务与设计中的自动化系统如何在看似客观的外表下复制种族等级，并汇集了对抗它们的废除主义工具。
- 实现方式: 对技术、法律与设计领域案例的社会学分析。
- 视角: 分类、偏见与监控
- 论文: https://www.politybooks.com/bookdetail?book_slug=race-after-technology-abolitionist-tools-for-the-new-jim-code--9781509526390 (Polity, 2019)
- 视频: https://www.youtube.com/watch?v=rY8RkET3KC0
- 图片: https://covers.openlibrary.org/b/id/10088781-L.jpg

#### 压迫的算法：搜索引擎如何强化种族主义（Algorithms of Oppression: How Search Engines Reinforce Racism） — Safiya Umoja Noble (2018)
- 类型: 书与文章 · 机器: 平台与推荐算法
- 核心想法: 排序算法是带有商业利益的编辑，而不是通向世界的中立窗口。
- 作品内容: Noble 记录了商业搜索结果（如谷歌对“black girls”的搜索）如何复制种族与性别刻板印象，并指出排序受广告与权力塑造。
- 实现方式: 对搜索结果的内容分析，结合黑人女性主义与信息科学理论。
- 视角: 分类、偏见与监控
- 论文: https://doi.org/10.18574/nyu/9781479833641.001.0001 (NYU Press, 2018)
- 视频: https://www.youtube.com/watch?v=6KLTpoTpkXo
- 图片: https://covers.openlibrary.org/b/id/12856940-L.jpg

#### 精神政治学（Psychopolitics: Neoliberalism and New Technologies of Power） — 韩炳哲 (2014)
- 类型: 书与文章 · 机器: 数据集与训练数据, 平台与推荐算法
- 核心想法: 今天的监控更多靠诱惑与自我披露运作，而不是靠禁止。
- 作品内容: 一篇短论，认为数据驱动的“智能权力”不再规训身体，而是读取并引导心理；大数据成为精神政治控制的工具。
- 实现方式: 哲学随笔（德文原版《Psychopolitik》，S. Fischer 2014；英译 Erik Butler，Verso 2017）。
- 视角: 分类、偏见与监控, 隐形劳动与攫取
- 论文: https://www.versobooks.com/products/226-psychopolitics (Verso (English ed. 2017))
- 图片: https://www.versobooks.com/cdn/shop/files/getimage_05e7fdd2-de74-4073-8bc6-73bfa358d3cb.jpg?v=1790570326&width=600
- 项目主页: https://www.versobooks.com/products/226-psychopolitics

#### 人机重构：计划与情境行动（Human-Machine Reconfigurations: Plans and Situated Actions） — Lucy Suchman (2007)
- 类型: 书与文章 · 机器: 类人机器人, 社交与陪伴机器人
- 核心想法: 机器之所以显得聪明，是因为人与环境在它周围做了大量工作。
- 作品内容: Suchman 重访她 1987 年对人们用不好“智能”复印机的研究，并延伸到 Kismet、Cog 等类人机器人，论证机器的能动性是在情境互动中被制造出来的。
- 实现方式: 把常人方法学和女性主义科学研究用于交互分析与机器人实验室；是《Plans and Situated Actions》的扩充第二版。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.1017/cbo9780511808418 (Cambridge University Press, 2007)
- 视频: https://www.youtube.com/watch?v=3_4-6gVbk4E
- 图片: https://covers.openlibrary.org/b/id/9840684-L.jpg

### 机器人学、人机交互与具身认知

具身机器人学、社交机器人，以及人如何与机器人相处的研究。

#### 智能新物种（The New Breed: What Our History with Animals Reveals about Our Future with Robots） — Kate Darling (2021)
- 类型: 书与文章 · 机器: 社交与陪伴机器人, 机器生物与移动机器人
- 核心想法: 我们早已懂得如何与被使用、被爱、被哀悼的非人他者共处；机器人可以加入这段历史。
- 作品内容: Darling 主张以动物而非人为模型来理解机器人，并举出士兵为排爆机器人举行葬礼、人们拒绝伤害 Pleo 恐龙玩具等案例。
- 实现方式: 结合人机交互实验、动物法律史与伦理学的科普论证。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://us.macmillan.com/books/9781250296115/thenewbreed/ (Henry Holt, 2021)
- 视频: https://www.youtube.com/watch?v=sTJ7E7TDTrU
- 图片: https://mpd-biblio-covers.imgix.net/9781250296115.jpg?fm=jpg
- 项目主页: https://us.macmillan.com/books/9781250296115/thenewbreed/

#### 群体性孤独：为什么我们对科技期待更多，对彼此却不能更亲密？（Alone Together: Why We Expect More from Technology and Less from Each Other） — Sherry Turkle (2011)
- 类型: 书与文章 · 机器: 社交与陪伴机器人, 聊天机器人与语言模型
- 核心想法: 我们已准备好接受“照护的表演”来代替照护，这更多说明了我们自己，而不是机器。
- 作品内容: 基于十五年的访谈，Turkle 描述了一个“机器人时刻”：儿童与老人接受 Furby、AIBO、My Real Baby 和海豹机器人 Paro，把它们当作“足够有生命”的陪伴者。
- 实现方式: 在家庭、学校和养老院进行的临床访谈与田野观察。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://www.basicbooks.com/titles/sherry-turkle/alone-together/9780465093656/ (Basic Books, 2011)
- 视频: https://www.youtube.com/watch?v=MtLVCpZIiNs
- 图片: https://covers.openlibrary.org/b/id/6952623-L.jpg

#### 身体的智能：智能科学新视角（How the Body Shapes the Way We Think: A New View of Intelligence） — Rolf Pfeifer, Josh Bongard (2006)
- 类型: 书与文章 · 机器: 机器生物与移动机器人, 类人机器人
- 核心想法: 机器人的一部分智能在于它的形状与材料，而不在控制器。
- 作品内容: Pfeifer 与 Bongard 主张智能取决于身体的形态与材料如何与环境互动，并以被动动力行走机和柔顺机器人为例。
- 实现方式: 对具身人工智能研究的综合，并提出机器人设计原则。
- 视角: 具身与动觉
- 论文: https://doi.org/10.7551/mitpress/3585.001.0001 (MIT Press, 2006)
- 视频: https://www.youtube.com/watch?v=mhWwoaoxIyc
- 图片: https://covers.openlibrary.org/b/id/13662665-L.jpg

#### 落入机器之手？老年照护的未来（In the Hands of Machines? The Future of Aged Care） — Robert Sparrow (2006)
- 类型: 论文 · 机器: 社交与陪伴机器人
- 核心想法: 当模拟关怀的机器取代了本该照护的人时，它可能是伤害而非帮助。
- 作品内容: Robert Sparrow 与 Linda Sparrow 认为，面向老年人的照护机器人会减少人的接触，并且依赖于让弱势者误以为机器在关心他们。
- 实现方式: 把养老照护的具体任务与现有及预期机器人的能力对照进行伦理分析。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.1007/s11023-006-9030-6 (Minds and Machines 16(2), 2006)

#### 设计社交机器人（Designing Sociable Robots） — Cynthia Breazeal (2002)
- 类型: 书与文章 · 机器: 社交与陪伴机器人, 类人机器人
- 核心想法: 会表现出需要的机器人，会引来人的照料，而正是这种照料让它成为社会性的存在。
- 作品内容: Breazeal 这本书围绕她在麻省理工学院制作的表情机器人头部 Kismet，阐述机器人如何借助驱力、情绪与面部表情吸引人互动，就像照料者与婴儿互动一样。
- 实现方式: 她博士研究的综合：动机与情绪模型、人脸与语调感知，以及可驱动眉毛、耳朵、眼睑和嘴唇的面部。
- 视角: 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.7551/mitpress/2376.001.0001 (MIT Press, 2002)
- 图片: https://covers.openlibrary.org/b/id/151207-L.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Kismet-IMG_6014.JPG/960px-Kismet-IMG_6014.JPG

#### Cog 项目：构建一个人形机器人（The Cog Project: Building a Humanoid Robot） — Rodney Brooks (1999)
- 类型: 论文 · 机器: 类人机器人
- 核心想法: 给机器人类人的身体与社会性发育，人们就会把它当作“某个人”来对待，而这又反过来塑造了它学到的东西。
- 作品内容: Brooks、Breazeal、Marjanović、Scassellati 与 Williamson 介绍 Cog：麻省理工学院一台只有上半身的类人机器人，旨在像婴儿一样，通过与人互动发展出眼动、伸手和共同注意等能力。
- 实现方式: 具有主动视觉与行为控制的上半身类人平台，1993–2004 年间开发。
- 视角: 具身与动觉, 他异与恐怖谷
- 论文: https://doi.org/10.1007/3-540-48834-0_5 (Computation for Metaphors, Analogy, and Agents, LNCS 1562, Springer, 1999)
- 视频: https://www.youtube.com/watch?v=oWjWzDzfLBo
- 图片: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Cog%2C_1993-2004%2C_view_1_-_MIT_Museum_-_DSC03732.JPG/960px-Cog%2C_1993-2004%2C_view_1_-_MIT_Museum_-_DSC03732.JPG

#### 媒体等同：人们该如何像对待真人实景一样对待电脑、电视和新媒体（The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places） — Byron Reeves, Clifford Nass (1996)
- 类型: 书与文章 · 机器: 语音与听觉机器, 社交与陪伴机器人
- 核心想法: 媒介 = 真实生活：人对机器的社交反应是自动的，所以设计面对的永远是一种社会动物。
- 作品内容: Reeves 与 Nass 报告了数十个实验：人们对计算机讲礼貌、会被它的恭维打动，还给它赋予性别和个性，尽管他们都说自己知道机器不是人。
- 实现方式: 把经典社会心理学实验中的“人”换成计算机和电视后重做的研究。
- 视角: 他异与恐怖谷, 亲密、照护与陪伴
- 论文: https://en.wikipedia.org/wiki/The_Media_Equation (Cambridge University Press / CSLI Publications, 1996)
- 图片: https://covers.openlibrary.org/b/id/829557-L.jpg

#### 计算机是社会行动者（Computers Are Social Actors） — Clifford Nass (1994)
- 类型: 论文 · 机器: 语音与听觉机器
- 核心想法: 极少的社交线索（一个声音和一个角色）就足以引发人对机器的完整社交行为。
- 作品内容: Nass、Jonathan Steuer 与 Ellen R. Tauber 进行了一系列实验，证明人会对会说话的计算机套用礼貌规范与性别刻板印象，例如由同一台计算机来询问时，人们会给它更高的评价。
- 实现方式: 使用录制语音、由计算机担任辅导和评估角色的受控实验室实验。
- 视角: 他异与恐怖谷
- 论文: https://doi.org/10.1145/191666.191703 (CHI 1994)
- 视频: https://www.youtube.com/watch?v=e7PvUUhDrfk

#### 无表征的智能（Intelligence without Representation） — Rodney Brooks (1991)
- 类型: 论文 · 机器: 机器生物与移动机器人
- 核心想法: 智能可以是情境的、具身的，而不必依赖内部模型的规划；这样的机器看起来也更有生命。
- 作品内容: Brooks 主张机器人应由直接耦合传感器与电机的简单行为层层叠加而成，“以世界本身为最好的模型”；他的六足机器人 Genghis 就是这样在崎岖地面上行走的。
- 实现方式: 包容式架构：层层叠加、相互压制或抑制的有限状态机，在麻省理工学院人工智能实验室的移动机器人上验证。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.1016/0004-3702(91)90053-M (Artificial Intelligence 47(1–3), 1991)
- 视频: https://www.youtube.com/watch?v=-6piNZBFdfY

#### 恐怖谷（The Uncanny Valley (Bukimi no Tani)） — 森政弘 (1970)
- 类型: 论文 · 机器: 类人机器人, 义体与赛博格
- 核心想法: “几乎像人”比明显的不像更令人不安，所以设计者不必追求完全像人。
- 作品内容: 发表在日本杂志《Energy》上的短文：人对机器人的亲近感随着“像人”的程度上升，但在接近人时会骤然跌入令人不适的“谷底”；文中例子是义手、文乐木偶与尸体。
- 实现方式: 一张手绘曲线图：横轴为“像人程度”，纵轴为亲近感，静止与运动的物体各有一条曲线；2012 年由 Karl MacDorman 与 Norri Kageki 译为英文。
- 视角: 他异与恐怖谷
- 论文: https://doi.org/10.1109/MRA.2012.2192811 (Energy 7(4), 1970; English: IEEE Robotics & Automation Magazine, 2012)
- 视频: https://www.youtube.com/watch?v=0g0sH3jTaVc
- 图片: https://spectrum.ieee.org/media-library/the-uncanny-valley-by-masahiro-mori-republished-in-robotics-automation-magazine.png?id=25569782&width=980 https://upload.wikimedia.org/wikipedia/commons/f/f0/Mori_Uncanny_Valley.svg
- 项目主页: https://spectrum.ieee.org/the-uncanny-valley

#### 表观行为的实验研究（An Experimental Study of Apparent Behavior） — Fritz Heider, Marianne Simmel (1944)
- 类型: 论文 · 机器: 机器生物与移动机器人
- 核心想法: 仅凭运动，我们就会看到有意图、有情感的主体，这就是简单的机器人也显得有生命的原因。
- 作品内容: Heider 与 Simmel 给观众放映一段两分半钟的短片：两个三角形和一个圆围着一个方框移动；几乎所有人都把它讲成一个关于恶霸、追逐和一对情侣出逃的故事。
- 实现方式: 向 114 名学生放映几何图形的定格动画，随后让他们描述内容或回答问题。
- 视角: 他异与恐怖谷, 能动、自主与共创
- 论文: https://doi.org/10.2307/1416950 (American Journal of Psychology 57(2), 1944)
- 视频: https://www.youtube.com/watch?v=n9TWwG4SFWQ

### 艺术与媒介理论

关于机器人艺术、AI 艺术与机器图像的论述。

#### 机器视觉：算法如何改变我们看世界的方式（Machine Vision: How Algorithms Are Changing the Way We See the World） — Jill Walker Rettberg (2023)
- 类型: 书与文章 · 机器: 计算机视觉, 监控与生物识别
- 核心想法: 机器视觉不是一只眼睛，而是一组关系：它让某些事物可见，另一些事物被忽视。
- 作品内容: Rettberg 把机器视觉分为五种模式（看得更多、看得不同、看见一切、被看见、看得更少），并将《Zizi – Queering the Dataset》《The Normalizing Machine》等作品与智能门铃、人脸滤镜并置阅读。
- 实现方式: 基于其欧洲研究理事会团队建立的“艺术、游戏与叙事中的机器视觉”数据库（500 件作品）的质性分析；开放获取。
- 视角: 机器之眼, 分类、偏见与监控
- 论文: https://www.politybooks.com/bookdetail?book_slug=machine-vision-how-algorithms-are-changing-the-way-we-see-the-world--9781509545223 (Polity, 2023)
- 视频: https://www.youtube.com/watch?v=Ybva0y9KF8Q
- 图片: https://covers.openlibrary.org/b/id/14726453-L.jpg
- 项目主页: https://machine-vision.no

#### 均值影像（Mean Images） — 黑特·史德耶尔 (2023)
- 类型: 书与文章 · 机器: 生成模型与潜空间, 数据集与训练数据
- 核心想法: 生成图像在双重意义上是“mean”的：它们是平均值，也会强化规范并排斥他者。
- 作品内容: Steyerl 把生成式 AI 图像读作对抓取数据的统计平均；她从自己的照片在 LAION-5B 数据集中的呈现方式，以及模型根据她的名字生成的图像出发。
- 实现方式: 把对模型输出的细读与数据集的政治经济学结合起来的文章。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 论文: https://newleftreview.org/issues/ii140/articles/hito-steyerl-mean-images (New Left Review 140/141, 2023)
- 视频: https://www.youtube.com/watch?v=PFwaqpkd61M
- 图片: https://newleftreview.org/system/dragonfly/production/2023/04/28/7rn0jeq677_Steyerl_Figure_1.jpg

#### 感知机器：介于人眼与AI之间的摄影未来（The Perception Machine: Our Photographic Future between the Eye and AI） — Joanna Zylinska (2023)
- 类型: 书与文章 · 机器: 计算机视觉, 生成模型与潜空间
- 核心想法: 感知如今是人与机器的共同过程，因此批判必须从内部展开。
- 作品内容: Zylinska 主张摄影已成为由相机、传感器与算法构成的星球级感知机器，并追问人在其中如何仍能看见与行动。
- 实现方式: 结合作者自身艺术实验的媒介哲学论著；开放获取。
- 视角: 机器之眼, 机器环世界
- 论文: https://doi.org/10.7551/mitpress/14471.001.0001 (MIT Press, 2023)
- 视频: https://www.youtube.com/watch?v=jsdZFeTs2VA

#### 机器学习时代的艺术（Art in the Age of Machine Learning） — Sofian Audry (2021)
- 类型: 书与文章 · 机器: 生成模型与潜空间, 控制论与人工生命系统
- 核心想法: 艺术家的材料是训练过程本身，而它的历史比眼下的热潮所承认的更长。
- 作品内容: Audry 解释机器学习系统如何被训练，并把机器学习艺术放进控制论艺术、人工生命艺术与演化艺术的谱系中，并分析当代机器学习艺术作品的案例。
- 实现方式: 把“数据—训练—模型”的技术概念框架用于案例研究；收入 Leonardo 丛书。
- 视角: 能动、自主与共创, 不透明与潜空间
- 论文: https://doi.org/10.7551/mitpress/12832.001.0001 (MIT Press / Leonardo, 2021)
- 视频: https://www.youtube.com/watch?v=TwtgaQSmnXc

#### AI艺术：机器视觉与扭曲的梦（AI Art: Machine Visions and Warped Dreams） — Joanna Zylinska (2020)
- 类型: 书与文章 · 机器: 生成模型与潜空间, 计算机视觉
- 核心想法: 值得关注的 AI 艺术，是那些揭示机器如何运作、谁在为它工作的作品。
- 作品内容: Zylinska 拒绝“计算机能否有创造力”这个问题，转而把 Lauren McCarthy 的《LAUREN》、Pierre Huyghe 的《UUmwelt》、Trevor Paglen 的《Sight Machine》等作品，与她称为“媚俗”的神经网络图像对照阅读。
- 实现方式: “Media : Art : Write : Now”丛书中的批判论著，开放获取；书中也收录她自己的摄影与 AI 项目。
- 视角: 不透明与潜空间, 能动、自主与共创, 机器环世界
- 论文: https://www.openhumanitiespress.org/books/titles/ai-art/ (Open Humanities Press, 2020)
- 视频: https://www.youtube.com/watch?v=jASV6Hjd2bY
- 图片: https://covers.openlibrary.org/b/id/14833507-L.jpg
- 项目主页: https://www.openhumanitiespress.org/books/titles/ai-art/

#### 平台观看：图像集合及其不可见性（Platform Seeing: Image Ensembles and Their Invisualities） — Adrian Mackenzie, Anna Munster (2019)
- 类型: 论文 · 机器: 计算机视觉, 数据集与训练数据, 平台与推荐算法
- 核心想法: 机器视觉发生在数据集与处理管线中，而不在任何单一图像或眼睛里。
- 作品内容: Mackenzie 与 Munster 指出，在平台上，“看”是由海量图像、格式、硬件与模型组成的集合完成的；这种“平台之看”生成的是“不可视性”，而非视野。
- 实现方式: 对 ImageNet 等深度学习数据集及其硬件的媒介理论分析。
- 视角: 机器之眼
- 论文: https://doi.org/10.1177/0263276419847508 (Theory, Culture & Society 36(5), 2019)

#### AI美学（AI Aesthetics） — Lev Manovich (2018)
- 类型: 书与文章 · 机器: 生成模型与潜空间, 平台与推荐算法
- 核心想法: AI 对美学最大的影响不是生成艺术，而是悄悄地给品味分类并加以预测。
- 作品内容: 一本小书，讨论 AI 如何已经塑造日常的审美决策（从照片滤镜、推荐到设计），以及当机器学习并预测品味时，文化会发生什么。
- 实现方式: Strelka Press 丛书中的一篇长文，依据他的文化分析研究。
- 视角: 能动、自主与共创, 不透明与潜空间
- 论文: http://manovich.net/index.php/projects/ai-aesthetics (Strelka Press, 2018)
- 视频: https://www.youtube.com/watch?v=oR1NyrAY_w4
- 图片: https://manovich.net/content/04-projects/184-ai-aesthetics/ai_new.jpg
- 项目主页: http://manovich.net/index.php/projects/ai-aesthetics

#### 机器人想象：人性与去人性化劳动的代价（The Robotic Imaginary: The Human and the Price of Dehumanized Labor） — Jennifer Rhee (2018)
- 类型: 书与文章 · 机器: 类人机器人, 自动驾驶与无人机, 社交与陪伴机器人
- 核心想法: 追问什么让机器人像人，就是追问谁的劳动被算作人的劳动。
- 作品内容: Rhee 阅读 AI 研究、电影、文学与艺术中的机器人（从 ELIZA、Kismet 到《#NotABugSplat》等无人机艺术），揭示每一种“类人机器人”的定义都建立在被贬低的人类劳动之上。
- 实现方式: 按照护劳动、情感劳动、无人机战争与图灵测试分章展开的文化分析。
- 视角: 隐形劳动与攫取, 亲密、照护与陪伴, 他异与恐怖谷
- 论文: https://doi.org/10.5749/j.ctv62hh4x (University of Minnesota Press, 2018)
- 视频: https://www.youtube.com/watch?v=7APzxormknw
- 图片: https://minnesota-us.imgix.net/covers/9781517902988.jpg?w=400

#### 机器智能时代的艺术（Art in the Age of Machine Intelligence） — Blaise Agüera y Arcas (2017)
- 类型: 论文 · 机器: 生成模型与潜空间, 计算机视觉
- 核心想法: 与摄影一样，机器智能会改变艺术本身，艺术家应当参与塑造它，而不只是做出反应。
- 作品内容: Agüera y Arcas 把机器学习与 19 世纪摄影的出现相比，以 DeepDream 为例，主张艺术家应把神经网络当作新媒介来创作。
- 实现方式: 谷歌 Artists + Machine Intelligence 项目创始人撰写的文章，开放获取。
- 视角: 能动、自主与共创
- 论文: https://doi.org/10.3390/arts6040018 (Arts 6(4), 2017)
- 视频: https://www.youtube.com/watch?v=uSUOdu_5MPc

#### 意义生成：认知、计算、艺术与具身（Making Sense: Cognition, Computing, Art, and Embodiment） — Simon Penny (2017)
- 类型: 书与文章 · 机器: 机器生物与移动机器人, 控制论与人工生命系统
- 核心想法: 制作会“行为”的机器的艺术家，长期实践着被 AI 忽视的具身认知理论。
- 作品内容: Penny 批判计算主义心智理论，借助生成认知、分布式认知、控制论以及他自己的机器人作品（如《Petit Mal》），论证交互艺术的“表演性美学”。
- 实现方式: 基于四十年实践写成的理论专著，收入 Leonardo 丛书。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://mitpress.mit.edu/9780262036757/ (MIT Press / Leonardo, 2017)
- 视频: https://www.youtube.com/watch?v=PU_WDouhkw8

#### 数据之海：幻想性错觉与模式（误）识别（A Sea of Data: Apophenia and Pattern (Mis-)Recognition） — 黑特·史德耶尔 (2016)
- 类型: 书与文章 · 机器: 监控与生物识别, 数据集与训练数据
- 核心想法: 模式识别也是模式投射；机器幻觉出的，正是其所有者想看到的秩序。
- 作品内容: Steyerl 描写情报机构与神经网络如何淹没在数据中，并看见本不存在的模式；她以谷歌 DeepDream 图像作为“空想性错觉”的例子。
- 实现方式: 结合媒介理论、监控史与图像分析的随笔。
- 视角: 不透明与潜空间, 分类、偏见与监控
- 论文: https://www.e-flux.com/journal/72/60480/a-sea-of-data-apophenia-and-pattern-mis-recognition/ (e-flux journal 72, 2016)
- 图片: https://images.e-flux.com/test/cad7b8d2-d37e-4c14-825a-431c296346ff?width=1200&height=630

#### 看不见的图像（你的照片正在看着你）（Invisible Images (Your Pictures Are Looking at You)） — Trevor Paglen (2016)
- 类型: 书与文章 · 机器: 计算机视觉, 数据集与训练数据
- 核心想法: 影响最深远的图像，是没有人去看的那些。
- 作品内容: Paglen 指出，如今大多数图像由机器为其他机器而制造，比如车牌识别器与人脸识别器；这种不可见的视觉文化超出了艺术史的分析工具。
- 实现方式: 一篇随笔，基于他为《It Began as a Military Experiment》和《Sight Machine》等作品研究计算机视觉系统的经验。
- 视角: 机器之眼, 不透明与潜空间
- 论文: https://thenewinquiry.com/invisible-images-your-pictures-are-looking-at-you/ (The New Inquiry, 8 December 2016)
- 视频: https://www.youtube.com/watch?v=JZjGsaJ1OcU
- 图片: https://thenewinquiry.com/app/uploads/2016/12/57paglen01.jpg

#### 机器表演者的多重身体（The Multiple Bodies of a Machine Performer） — Louis-Philippe Demers (2016)
- 类型: 论文 · 机器: 机器生物与移动机器人, 工业机械臂
- 核心想法: 机器表演者的在场感来自其动作如何被解读，而不是它看起来多像人。
- 作品内容: Demers 结合自己的作品（如《The Tiller Girls》）分析观众如何感知舞台上机器人的能动性，并区分机器表演者的物理身体、被感知的身体与叙事身体。
- 实现方式: 基于创作实践的分析，收入 Herath、Kroos 与 Stelarc 主编的《Robots and Art: Exploring an Unlikely Symbiosis》。
- 视角: 具身与动觉, 他异与恐怖谷, 失败、故障与错误
- 论文: https://doi.org/10.1007/978-981-10-0321-9_14 (Robots and Art, Springer, 2016)
- 视频: https://www.youtube.com/watch?v=Bf-r34FzLhs

#### 幻影图像（Phantom Images） — Harun Farocki (2004)
- 类型: 书与文章 · 机器: 计算机视觉, 自动驾驶与无人机
- 核心想法: 当图像变成流程中的一步，看就变成了做，人类观者随之退场。
- 作品内容: Farocki 关于“操作图像”的文章：导弹摄像头与工业视觉系统的图像既不为娱乐也不为告知，而是某个操作的一部分；它与他的装置系列《Eye/Machine》（2001–03）同期写成。
- 实现方式: 一篇文章，依据为《Eye/Machine》收集的制导武器与机器视觉系统档案影像写成。
- 视角: 机器之眼
- 论文: https://www.harunfarocki.de/installations/2000s/2003/eye-machine-iii.html (Public 29, 2004)
- 视频: https://www.youtube.com/watch?v=tERIscWmpSo
- 项目主页: https://www.harunfarocki.de/installations/2000s/2003/eye-machine-iii.html

#### 机器人艺术的奠基与发展（Foundation and Development of Robotic Art） — Eduardo Kac (1997)
- 类型: 论文 · 机器: 机器生物与移动机器人, 类人机器人, 控制论与人工生命系统
- 核心想法: 机器人艺术很早就分成三条路线：拟人的、控制论响应式的，以及生物混合的。
- 作品内容: Kac 从 1960 年代的三件作品（白南准与阿部修也的《Robot K-456》、Tom Shannon 的《Squat》以及 Edward Ihnatowicz 的《SAM》和《Senster》）出发，追溯机器人艺术直到 1990 年代的远程在场与网络操控机器人。
- 实现方式: 刊于《Art Journal》艺术与技术专号的艺术史综述。
- 视角: 具身与动觉, 能动、自主与共创
- 论文: https://doi.org/10.1080/00043249.1997.10791834 (Art Journal 56(3), 1997)
- 项目主页: https://www.ekac.org

#### 视觉机器（The Vision Machine） — Paul Virilio (1988)
- 类型: 书与文章 · 机器: 计算机视觉, 自动驾驶与无人机, 监控与生物识别
- 核心想法: 当机器替我们去看，感知就变成后勤，人的眼睛成了可有可无的东西。
- 作品内容: Virilio 描述自动化感知的兴起：无需人类观看者就能观看并解读的相机与计算机，他称之为源于军事后勤的“无视之视”。
- 实现方式: 从透视绘画到智能武器的媒介考古随笔；法文原版《La Machine de vision》（Galilée，1988）。
- 视角: 机器之眼
- 论文: https://iupress.org/9780253209016/the-vision-machine/ (Galilée, 1988; English: BFI / Indiana University Press, 1994)
- 图片: https://covers.openlibrary.org/b/id/148033-L.jpg

#### 超越现代雕塑：科学与技术对本世纪雕塑的影响（Beyond Modern Sculpture: The Effects of Science and Technology on the Sculpture of This Century） — Jack Burnham (1968)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 雕塑让物体“活起来”的长久愿望，最终落到会行为的机器身上。
- 作品内容: Burnham 回顾 20 世纪雕塑从生机论到动态、光与控制论艺术的发展，并预言雕塑将从静态物体转向会回应的系统与人工生命。
- 实现方式: 结合艺术史与系统论的综述。
- 视角: 能动、自主与共创, 具身与动觉
- 论文: https://archive.org/details/beyondmodernscul0000burn (George Braziller, 1968)
- 图片: https://covers.openlibrary.org/b/id/14444956-L.jpg

#### 控制论的偶然发现：计算机与艺术（Cybernetic Serendipity: The Computer and the Arts） — Jasia Reichardt (1968)
- 类型: 书与文章 · 机器: 控制论与人工生命系统, 机器生物与移动机器人
- 核心想法: 第一场大型计算机艺术展把机器呈现为合作者和角色，而不仅仅是工具。
- 作品内容: Reichardt 在伦敦当代艺术学院所策展览的图录，以《Studio International》特刊形式出版，记录了 Gordon Pask、白南准、Edward Ihnatowicz 等人的计算机图形、音乐、诗歌与控制论机器。
- 实现方式: 展览图录，收录艺术家自述、图解以及科学家与工程师的文章。
- 视角: 能动、自主与共创
- 论文: https://cyberneticserendipity.net (Studio International special issue, 1968)
- 视频: https://www.youtube.com/watch?v=5mH9DysESqo
- 图片: https://covers.openlibrary.org/b/id/8992379-L.jpg
- 项目主页: https://cyberneticserendipity.net

## 资源与链接：人物、机构与网站

### 艺术家与设计师

- **!Mediengruppe Bitnik** (苏黎世，瑞士 / 伦敦，英国) — 瑞士艺术二人组（Carmen Weisskopf 与 Domagoj Smoljo），其 Random Darknet Shopper 是每周拿到比特币预算、在暗网随机购物的机器人，后来被瑞士警方“逮捕”。 代表作: Delivery for Mr. Assange (2013); Random Darknet Shopper (2014); Alexiety (2019–). https://www.bitnik.org/
- **aaajiao (Xu Wenkai) / 徐文恺** (柏林，德国 / 上海，中国) — 中国艺术家，以互联网、机器人程序与数据为材料，描绘网络控制下的日常；他的化身 aaajiao 反思平台之中的身份。 代表作: GFWlist (2010); Remnants of an Electronic Past (2016); Deep Sleep (2020). http://www.aaajiao.com/
- **Adam Harvey** (柏林，德国, 1981–) — 美国反监控艺术家与研究者，CV Dazzle 妆容可骗过人脸检测，Exposing.ai 追踪了数以百万计被抓取进人脸识别数据集的照片。 代表作: CV Dazzle (2010); Stealth Wear (2013); HyperFace (2017); Exposing.ai / MegaPixels (2019–, with Jules LaPlace). https://ahprojects.com/
- **Addie Wagenknecht** (奥地利 / 美国, 1981–) — 美国艺术家，Optimization of Parenthood 中婴儿一哭，机械臂就会摇动摇篮，追问照护被自动化后会变成什么。 代表作: Optimization of Parenthood (2011–); Asymmetric Love (2013); Data and Dragons (2015). https://www.placesiveneverbeen.com/
- **Agnieszka Kurant** (纽约，美国, 1978–) — 波兰艺术家，关注集体智能与非人类智能；A.A.I. 由白蚁用彩色沙粒筑成的蚁丘构成，这种“人工的人工智能”呼应 AI 背后的众包工人。 代表作: A.A.I. (2014); Crowd Crystal (2019). https://en.wikipedia.org/wiki/Agnieszka_Kurant
- **Agnieszka Pilat** (旧金山，美国) — 波兰出生的画家，把波士顿动力的 Spot 机器狗当作画室伙伴与合作画家，把机器呈现为一个正在学习留下痕迹的新物种。 代表作: Heterobota (NGV Triennial, 2023); Paintings with Boston Dynamics' Spot (2021–). https://www.agnieszkapilat.com/
- **Alexandra Daisy Ginsberg** (伦敦，英国, 1982–) — 英国艺术家，The Substitute 以 AI 驱动的数字动物“复活”最后一头雄性北方白犀牛，追问为什么我们宁愿要人工生命，也任由真实的生命消亡。 代表作: The Substitute (2019); Resurrecting the Sublime (2019); Pollinator Pathmaker (2021). https://www.daisyginsberg.com/
- **American Artist** (洛杉矶，美国, 1989–) — 美国艺术家，My Blue Window 通过预测警务的仪表盘呈现城市，直面计算风险评估中的种族逻辑。 代表作: Black Gooey Universe (2018); My Blue Window (2019); Shady Grove (2021). https://americanartist.us/
- **Andrew Norman Wilson** (洛杉矶，美国, 1983–) — 美国艺术家，在谷歌做合同工时拍摄了佩戴不同工牌的图书扫描工人，之后收集谷歌图书中留下扫描员手指的页面。 代表作: Workers Leaving the Googleplex (2011); ScanOps (2012–). https://www.andrewnormanwilson.com/
- **Anicka Yi** (纽约，美国, 1971–) — 韩裔美国艺术家，主张“让机器生物化”：在 In Love With the World 中，漂浮的“aerobes”作为有自身感知与行为的新机器物种在泰特涡轮大厅中游荡。 代表作: Biologizing the Machine (tentacular trouble) (2019); In Love With the World (Tate Turbine Hall, 2021). https://en.wikipedia.org/wiki/Anicka_Yi
- **Anna Ridler** (伦敦，英国, 1985–) — 英国艺术家，亲手构建自己的数据集；Myriad (Tulips) 展出她拍摄并逐一标注的一万张郁金香照片，让训练集中的人类劳动与选择变得可见。 代表作: Myriad (Tulips) (2018); Mosaic Virus (2018); Traces of Things (2021). https://annaridler.com/
- **Annie Dorsen** (纽约，美国, 1973–) — 美国剧场创作者，提出“算法剧场”；Hello Hi There 中两个聊天机器人每晚即兴重演乔姆斯基与福柯关于人性的辩论。 代表作: Hello Hi There (2010); A Piece of Work (2013); Prometheus Firebringer (2023). https://www.anniedorsen.com/
- **Arthur Ganson** (剑桥，美国, 1955–) — 美国动态雕塑家，作品温和而富哲思；Machine with Concrete 由电机带动一串齿轮，最后一个齿轮浇在混凝土里，需要两万亿年才会转一圈。 代表作: Machine with Concrete (1992); Machine with Oil (1990); Cory's Yellow Chair (1995). https://www.arthurganson.com/
- **Auger & Loizeau (James Auger & Jimmy Loizeau)** (伦敦，英国) — 英国思辨设计师，Carnivorous Domestic Entertainment Robots 靠捕食苍蝇与老鼠供能，把家用机器人重新想象成有生命的东西。 代表作: Audio Tooth Implant (2001); Carnivorous Domestic Entertainment Robots (2009); Afterlife (2001–09). https://www.wikidata.org/wiki/Q55217959
- **Automato.farm** (上海，中国 / 伦敦，英国) — 由 Simone Rebaudengo、Matteo Loglio 和 Saurabh Datta 组成的设计工作室；Ethical Things 中的电风扇会请线上众包工人替它解决道德困境。 代表作: Objects of Research (2016); Politics of Power (2016); Ethical Things (2015); BIY.world (2019). http://automato.farm/
- **Ayoung Kim / 金雅瑛** (首尔，韩国, 1979–) — 韩国艺术家，《送货舞者之球》讲述一位女性外卖骑手在被算法平台支配、时空扭曲的首尔中穿行。 代表作: Delivery Dancer's Sphere (2022); Delivery Dancer's Arc: 0° Receiver (2024); PH Express (2018). https://de.wikipedia.org/wiki/Ayoung_Kim
- **Ben Grosser** (厄巴纳，美国) — 美国软件文化艺术家；Computers Watching Movies 用草图般的轨迹呈现计算机视觉系统在经典电影中“看”的地方，描绘机器的注意力。 代表作: Computers Watching Movies (2013); Facebook Demetricator (2012–); Go Rando (2017); Minus (2021). https://bengrosser.com/
- **Bill Vorn** (蒙特利尔，加拿大, 1959–) — 加拿大机器人艺术家，他的机器上演痛苦与歇斯底里：章鱼状的 Hysterical Machines 在观众靠近时疯狂抽动，让人对粗糙的机构生出同情。 代表作: La Cour des Miracles (1997, with Louis-Philippe Demers); Hysterical Machines (2006); Inferno (2015). https://billvorn.concordia.ca/
- **Bjørn Karmann** (哥本哈根，丹麦) — 丹麦设计师，Project Alias 像一只真菌寄生在智能音箱上，持续向它低语噪声直到你唤醒；Paragraphica 是一台没有镜头、用数据“写”出照片的相机。 代表作: Objectifier (2016); Project Alias (2019, with Tore Knudsen); Paragraphica (2023). https://bjoernkarmann.dk/
- **Blanca Li** (巴黎，法国, 1964–) — 西班牙编舞家，Robot 让舞者与 NAO 人形机器人及明和电机的乐器同台，探索人与机器如何学习彼此的动作。 代表作: Robot (2013); Le Bal de Paris (2021). https://www.blancali.com/
- **Blast Theory** (布莱顿，英国) — 英国互动表演团体；Cat Royale（2023）记录一只机械臂连续十二天试图取悦三只猫，追问机器能否照顾其他物种。 代表作: Can You See Me Now? (2001); Cat Royale (2023). https://www.blasttheory.co.uk/
- **Bruce Lacey** (伦敦，英国, 1927–2016) — 英国艺术家，用废品拼装出无政府气质的机器人与表演自动机，多件曾在“控制论的意外发现”（1968）展出；他的类人机器刻意滑稽、笨拙而脆弱。 代表作: ROSA BOSOM (1965); Old Money Bags (1965); Cybernetic Serendipity robots (1968). https://en.wikipedia.org/wiki/Bruce_Lacey
- **Cao Fei / 曹斐** (北京，中国, 1978–) — 中国艺术家，关注劳动、虚拟世界与自动化；《亚洲一号》讲述全自动物流仓库中仅有的两名工人在分拣机器人之间相恋。 代表作: Whose Utopia (2006); RMB City (2007–11); Asia One (2018); Staging the Era (2023). http://www.caofei.com/
- **Caroline Sinders** (伦敦，英国 / 纽约，美国) — 美国设计师与研究者，其 Feminist Data Set 以女性主义方法审视 AI 生产的每一步，从采集数据到给标注者付酬。 代表作: Feminist Data Set (2017–); Technically Responsible Knowledge (2020). https://carolinesinders.com/
- **Catie Cuan** (斯坦福，美国) — 美国舞者兼机器人学家，与工业和移动机器人共同编舞；Output 中她与 ABB 机械臂互相交换彼此被捕捉的动作。 代表作: Output (2019); Time to Compile (2019); Engine of Wonder (2023, TED). https://www.catiecuan.com/
- **Chico MacMurtrie** (纽约，美国, 1961–) — 美国艺术家，其 Amorphic Robot Works 制作会呼吸、击鼓、攀爬的气动与充气机器身体，让机器表现得像原始生物。 代表作: Amorphic Robot Works (founded 1991); The Robotic Church (2006); Inflatable Architectural Bodies (2000s–). https://amorphicrobotworks.org/
- **Choe U-Ram** (首尔，韩国, 1970–) — 韩国雕塑家，创作“机械生命体”：拥有虚构学名与生命周期的精致机械生物；《小方舟》是一艘船桨如呼吸般起伏的船。 代表作: Opertus Lunula Umbra (2008); Little Ark (MMCA, 2022); Una Lumino (2008). https://www.uram.net/
- **Choy Ka Fai / 徐家辉** (柏林，德国 / 新加坡) — 新加坡艺术家，Prospectus for a Future Body 用记录自其他舞者的电信号刺激舞者肌肉，追问动作记忆能否经由机器传递。 代表作: Prospectus for a Future Body (2011); UnBearable Darkness (2018). https://www.ka5.info/
- **Christa Sommerer & Laurent Mignonneau** (林茨，奥地利) — 奥地利–法国二人组，人工生命艺术先驱：在 A-Volve 中观众画出的生物会在水池中自行演化、捕食与交配。 代表作: Interactive Plant Growing (1992); A-Volve (1994); Life Writer (2006). https://www.interface.ufg.ac.at/christa-laurent/
- **Clement Valla** (纽约，美国) — 法裔美国艺术家，Postcards from Google Earth 收集“融化”的桥梁与扭曲的道路：它们不是错误，而是机器生成的三维世界的逻辑。 代表作: Postcards from Google Earth (2010–); Surface Survey (2014). https://clementvalla.com/
- **Cod.Act (André & Michel Décosterd)** (拉绍德封，瑞士) — 瑞士兄弟组合，其声音-机器表演融合身体与机械：Pendulum Choir 中九名歌手站在液压支架上倾斜摆动，歌声随机器运动而变化。 代表作: Pendulum Choir (2011); πTon (2017); Nyloïd (2013). https://www.codact.ch/
- **Daito Manabe / 真锅大度** (东京，日本, 1976–) — 日本艺术家、Rhizomatiks 联合创始人，Electric Stimulus to Face 让电脑以电流驱动他的面部肌肉，之后延伸到无人机、舞者与脑解码作品。 代表作: Electric Stimulus to Face (2008); Rhizomatiks × ELEVENPLAY (2010s); dissonant imaginary (2023). https://www.daito.ws/
- **Dan Chen** — 设计师，他在罗德岛设计学院期间创作的“机器亲密”系列让机器抚摸、安慰人；其中 Last Moment Robot 在临终病人身边抚摸其手臂并说出安慰的话语，追问生命尽头的机器照护。 代表作: End of Life Care Machine (2012); Last Moment Robot (2012); Intimacy series (2011–12). https://dankc.com/
- **David Bowen** (明尼阿波利斯，美国) — 美国艺术家，让非人类与数据驱动他的机器：盆栽挥舞砍刀，苍蝇操控手枪，让其他感知世界通过机器人行动。 代表作: fly revolver (2013); tele-present wind (2018); plant machete (2014). https://www.dwbowen.com/
- **David Harris Smith & Frauke Zeller** (汉密尔顿 / 多伦多，加拿大) — 加拿大研究者，创造了搭便车机器人 hitchBOT：它靠陌生人的善意横穿加拿大和欧洲部分地区，2015 年在费城被毁。 代表作: hitchBOT (2014–15). https://en.wikipedia.org/wiki/HitchBOT
- **David Rokeby** (多伦多，加拿大, 1960–) — 加拿大互动装置先驱；The Giver of Names 观察观众放在面前的物品并生成联想式句子，是对机器“解读”的早期描绘。 代表作: Very Nervous System (1986–90); The Giver of Names (1990–); Sorting Daemon (2003). http://www.davidrokeby.com/
- **Desmond Paul Henry** (曼彻斯特，英国, 1921–2004) — 英国艺术家，1960 年代初用轰炸瞄准器模拟计算机改装成绘图机器，其作品是英国最早展出的机器绘画之一。 代表作: Henry Drawing Machine (1961); Ideographs exhibition (Reid Gallery, London, 1962). http://www.desmondhenry.com/
- **Diemut Strebe** (波士顿，美国) — 德国艺术家，与 MIT 科学家合作；The Prayer 是一张机器人嘴，用语言模型生成并念出自己的祷词，追问机器能否祈祷。 代表作: The Prayer (2020); Redemption of Vanity (2019). https://www.diemutstrebe.com/
- **Dries Depoorter** (根特，比利时) — 比利时艺术家，The Follower 把 Instagram 照片与拍摄当时的公开网络摄像头画面相匹配，揭示 AI 多么轻易地把公共摄像头与私人影像连在一起。 代表作: Jaywalking (2015); Surveillance Speaker (2020); The Follower (2022). https://driesdepoorter.be/
- **Dunne & Raby (Anthony Dunne & Fiona Raby)** (纽约，美国) — 英国设计师，确立了批判设计与思辨设计；Technological Dreams: Robots 想象了一批需要照顾、神经质或依赖人的家用机器人，而非顺从的仆人。 代表作: Technological Dreams Series: No. 1, Robots (2007); Speculative Everything (2013); Hertzian Tales (1999). https://dunneandraby.co.uk/
- **Eduardo Kac** (芝加哥，美国, 1962–) — 巴西裔美国艺术家，远程临场机器人与生物艺术先驱；在 Rara Avis 中，观众透过一只机器鹦鹉的眼睛观看鸟舍，暂时栖居于机器身体。 代表作: Ornitorrinco (1989–96, with Ed Bennett); Rara Avis (1996); Teleporting an Unknown State (1996); GFP Bunny (2000). https://www.ekac.org/
- **Edward Ihnatowicz** (伦敦，英国, 1926–1988) — 波兰出生的英国雕塑家，创作了最早的计算机控制机器人雕塑：飞利浦 Evoluon 中心 4.5 米高的液压生物 The Senster 会转向轻柔的人声、躲开喧闹。 代表作: SAM (1968); The Senster (1970). http://www.senster.com/
- **Ei Wada / 和田永** (东京，日本, 1987–) — 日本艺术家，把显像管电视、电风扇等淘汰电器改造成乐器，让被遗弃的机器以社区乐团的形式获得第二次生命。 代表作: Braun Tube Jazz Band (2009); Electronicos Fantasticos! (2015–). https://eiwada.com/
- **Elisa Giardina Papa** (纽约，美国 / 西西里，意大利) — 意大利艺术家，Cleaning Emotional Data 记录她自己为情绪识别 AI 标注面部表情的零工劳动，Technologies of Care 描绘线上照护工作者。 代表作: Technologies of Care (2016); Cleaning Emotional Data (2020). https://www.elisagiardinapapa.org/
- **Esther Hovers** (荷兰) — 荷兰艺术家，False Positives 在街头重现智能监控系统被训练去标记的八种“异常行为”，从静止不动到逆流而行。 代表作: False Positives (2015). https://www.estherhovers.com/
- **Eva & Franco Mattes** (纽约，美国) — 意大利艺术家二人组，Dark Content 让为平台过滤暴力与淫秽图片的内容审核员以匿名身份发声，揭示“自动”审核背后的人类层。 代表作: Dark Content (2015); BEFNOED (2014); Personal Photographs (2018). https://0100101110101101.org/
- **Everest Pipkin** (匹兹堡，美国, 1990–) — 美国艺术家与游戏开发者，Lacework 把 MIT Moments in Time 数据集的每段视频缓慢重构，其配套文章记录了训练数据中隐藏的暴力。 代表作: Lacework (2020); Shell Song (2020). https://everest-pipkin.com/
- **Garnet Hertz** (温哥华，加拿大, 1973–) — 加拿大艺术家与“批判制作”学者，他的机器人由一只站在轨迹球上的活马达加斯加发声蟑螂驾驶。 代表作: Cockroach Controlled Mobile Robot (2004); Critical Making (2012); Disobedient Electronics (2016–). http://www.conceptlab.com/
- **George E. Lewis** (纽约，美国, 1952–) — 美国作曲家、长号手、AACM 成员，Voyager 是会聆听并回应的即兴计算机“乐团”，被视为受非裔美国音乐文化塑造的合作者。 代表作: Voyager (1987); Why Do We Want Our Computers to Improvise? (2018). https://music.columbia.edu/bios/george-e-lewis
- **Gilberto Esparza** (墨西哥城，墨西哥) — 墨西哥艺术家，Plantas Nómadas 是一台机器人，借微生物燃料电池从污染河流中为身上的植物获取养分，是为受损生态而生的“机器-生物”（2015 年金尼卡奖）。 代表作: Parásitos Urbanos (2007); Plantas Nómadas (2008–13); Biocenosis (2021). https://gilbertoesparza.net/
- **Gordon Pask** (伦敦，英国, 1928–1996) — 英国控制论学者，把会学习、会回应的机器做成艺术：Musicolour 会对重复自己的乐手“感到厌倦”，Colloquy of Mobiles 让悬挂的机器在“控制论的意外发现”展上彼此求偶，也与观众互动。 代表作: Musicolour (1953); Colloquy of Mobiles (1968); Conversation Theory (1975). https://en.wikipedia.org/wiki/Gordon_Pask
- **Guo Cheng / 郭城** (上海，中国) — 中国艺术家，创作科幻气质的机器装置；他以动图教程示范如何扭曲面部躲避人脸识别，《网络漫游者》则探访中国互联网物理层面的“握手”。 代表作: A Technique of Evading Face Detection (2020); The Net Wanderer – A Tour of Suspended Handshakes (2020). https://www.guo-cheng.net/
- **Guy Ben-Ary** (珀斯，澳大利亚, 1967–) — 阿根廷出生的澳大利亚生物艺术家，把活体神经元接入机器：MEART 通过机械臂作画，cellF 是由他自身细胞培养的神经元演奏的合成器。 代表作: MEART – The Semi-Living Artist (2003); cellF (2015); Revivification (2021). https://guybenary.com/
- **Harold Cohen** (圣迭戈，美国, 1928–2016) — 英国画家，用四十余年开发绘画程序与机器人 AARON，追问机器能否创作艺术、艺术家的角色又会变成什么。 代表作: AARON (1973–2016); What is an Image? (1979). https://www.aaronshome.com/
- **Harpreet Sareen** (纽约，美国) — 印度出生的设计师与研究者，提出“赛博植物学”；Elowan 是一株用自身电信号驱动机器人底座向光移动的植物。 代表作: Elowan (2018, MIT Media Lab); Cyborg Botany (2019). https://www.harpreetsareen.com/
- **Harun Farocki** (柏林，德国, 1944–2014) — 德国电影人，提出“操作图像”（由机器生成、供机器使用的图像）；《眼睛/机器》三部曲审视智能炸弹摄像头与工业视觉，奠定了“机器之眼”艺术的基础。 代表作: Images of the World and the Inscription of War (1988); Eye/Machine I–III (2001–03); Serious Games I–IV (2009–10); Parallel I–IV (2012–14). https://www.harunfarocki.de/
- **Hasan Elahi** (华盛顿，美国, 1972–) — 孟加拉裔美国艺术家，在被误列入美国恐怖分子观察名单后，开始公开发布数以万计记录自己行踪的图片，用过量信息“喂饱”监控机器。 代表作: Tracking Transience (2002–). https://en.wikipedia.org/wiki/Hasan_M._Elahi
- **Heather Dewey-Hagborg** (纽约，美国, 1982–) — 美国艺术家，从街头捡到的 DNA 推算并 3D 打印陌生人肖像，揭示法医表型推测算法中的虚构与偏见。 代表作: Stranger Visions (2012–13); Probably Chelsea (2017); Hybrid: an Interspecies Portrait (2023). https://deweyhagborg.com/
- **Hito Steyerl** (柏林，德国, 1966–) — 德国艺术家与作家，她关于“贫乏图像”、机器人与“人工愚蠢”的论文电影和文字，塑造了艺术界思考计算、可见性与权力的方式。 代表作: How Not to Be Seen (2013); HellYeahWeFuckDie (2016); This is the Future (2019); Medium Hot: Images in the Age of Heat (2025). https://en.wikipedia.org/wiki/Hito_Steyerl
- **Ho Tzu Nyen / 何子彦** (新加坡, 1976–) — 新加坡艺术家，《东南亚批判辞典》由算法无限重组剪辑，把历史的编排交给机器。 代表作: The Critical Dictionary of Southeast Asia (CDOSEA) (2017–); The Name (2015); T for Time (2023). https://en.wikipedia.org/wiki/Ho_Tzu_Nyen
- **Holly Herndon & Mat Dryhurst** (柏林，德国) — 美国艺术家与音乐人，与人声合唱团一起“养育” AI 宝宝 Spawn，并推出人人都能借用的声音模型 Holly+，引出声音归属与同意的问题。 代表作: PROTO (2019, with AI 'baby' Spawn); Holly+ (2021); xhairymutantx (Whitney Biennial, 2024); The Call (Serpentine, 2024). https://herndondryhurst.studio/
- **Hsin-Chien Huang / 黄心健** (台北，中国台湾, 1966–) — 台湾新媒体艺术家，与 Jean-Michel Jarre 合作的 VR 作品 The Eye and I 让观众沉浸于充满监控与“观看机器”的世界。 代表作: The Eye and I (2019, with Jean-Michel Jarre); To the Moon (2018, with Laurie Anderson); Bodyless (2019). https://www.storynest.com/
- **Hu Jieming / 胡介鸣** (上海，中国) — 上海中国新媒体艺术先驱，其装置如由 1440 个盒子组成的《一分钟一百年》，把历史压缩进机器尺度的时间。 代表作: 100 Years in 1 Minute (2010); The Raft of the Medusa (2002). https://www.shanghartgallery.com/galleryarchive/artists/name/hujieming
- **Huang Yi / 黄翊** (台北，中国台湾) — 台湾编舞家，亲自为 KUKA 工业机械臂编程并与之共舞；《黄翊与库卡》曾为 2013 年林茨电子艺术节开幕并在各地巡演，让工厂机器人动得温柔。 代表作: Huang Yi & KUKA (2012); A Million Miles Away (2019). https://huangyistudio.com/
- **Ian Cheng** (纽约，美国, 1984–) — 美国艺术家，创作“实时模拟”：由 AI 驱动、永不重复的自演世界；BOB 是一个性格会随经历变化的人工生命体。 代表作: Emissaries trilogy (2015–17); BOB (Bag of Beliefs) (2018–19); Life After BOB (2021). https://iancheng.com/
- **Jaha Koo** (根特，比利时, 1984–) — 韩国剧场创作者，Cuckoo 与三台会说话的电饭煲同台，借家用机器讲述韩国经济危机中的孤独。 代表作: Cuckoo (2017); Hamartia trilogy (2015–2019). https://gujaha.com
- **Jake Elwes** (伦敦，英国, 1993–) — 英国艺术家，用变装表演者的图像重新训练人脸模型来“酷儿化” AI；The Zizi Show 是一场深度伪造卡巴莱，身体在数据集的边缘崩解。 代表作: Zizi – Queering the Dataset (2019); The Zizi Show (2020); CUSP (2019); Machine Learning Porn (2016). https://www.jakeelwes.com/
- **James Bridle** (希腊 / 英国, 1980–) — 英国艺术家与作家，Autonomous Trap 001 用一圈道路标线把自动驾驶汽车“困”在其中；著作《新黑暗时代》与《存在之道》重新思考计算与非人类智能。 代表作: The New Aesthetic (2011–); Autonomous Trap 001 (2017); New Dark Age (2018); Ways of Being (2022). https://jamesbridle.com/
- **James Seawright** (纽约，美国, 1936–2022) — 美国雕塑家，1960 年代制作了早期的响应式电子雕塑：它们扫视空间、感知观众，并以灯光和动作回应。 代表作: Watcher (1965–66); Searcher (1966); Electronic Peristyle (1968). https://en.wikipedia.org/wiki/James_Seawright
- **Jean Tinguely** (巴塞尔，瑞士, 1924–1991) — 瑞士动态雕塑家，以荒诞、自毁的机器闻名：Métamatics 可按需作画，Homage to New York 在 MoMA 花园里把自己震散成碎片，让崩坏本身成为作品。 代表作: Métamatics (1959); Homage to New York (1960); Study for an End of the World No. 2 (1962). https://www.tinguely.ch/
- **Jenna Sutela** (柏林，德国, 1983–) — 芬兰艺术家，关注超越人类的智能；nimiia cétiï 中神经网络从灵媒的录音和细菌的运动中学习一种“火星语”。 代表作: nimiia cétiï (2018); I Magma (2019); Holobiont Society (2018); Pond Brain (2024). https://jennasutela.com/
- **Jennifer Walshe** (都柏林，爱尔兰, 1974–) — 爱尔兰作曲家与歌者，与以她自己的面孔和声音训练的 AI 即兴合演（ULTRACHUNK），并借机器生成的歌声改写音乐史。 代表作: ULTRACHUNK (2018, with Memo Akten); A Late Anthology of Early Music Vol. 1 (2020). http://milker.org/
- **Jiabao Li / 李佳宝** (奥斯汀，美国) — 中国艺术家与设计师，Reality Design Lab（德州大学奥斯汀分校）创始人，其作品探讨 AI、照护与超越人类的感知，包括扮演母亲角色的机器 AI Mom。 代表作: AI Mom (2024); Womb Wetware (2025); Once Upon a Garden (2023). https://www.jiabaoli.org/
- **Jill Magid** (纽约，美国, 1973–) — 美国艺术家，在 Evidence Locker 中请利物浦的监控操作员拍摄她，并以情书的形式申请调取录像，与监控系统建立一种亲密关系。 代表作: Evidence Locker (2004); Trust (2004). https://www.jillmagid.com/
- **Joana Moll** (巴塞罗那，西班牙) — 西班牙艺术家与研究者，测量互联网的物质成本；CO2GLE 实时显示每秒访问 google.com 所排放的二氧化碳。 代表作: CO2GLE (2014); The Hidden Life of an Amazon User (2019); The Dating Brokers (2018, with Tactical Tech). https://www.janavirgin.com/
- **Jon Rafman** (蒙特利尔，加拿大, 1981–) — 加拿大艺术家，The Nine Eyes of Google Street View 收集街景车漠然拍下的画面，描绘一个被毫不在意的机器所看见的世界。 代表作: The Nine Eyes of Google Street View (2009–). https://jonrafman.com/
- **Jordan Wolfson** (纽约 / 洛杉矶，美国, 1980–) — 美国艺术家，其动画机器人 (Female figure) 在镜前跳舞并以面部追踪凝视观众，是对凝视与被性化的机器人身体的不安研究。 代表作: (Female figure) (2014); Colored sculpture (2016); Body Sculpture (2023). https://en.wikipedia.org/wiki/Jordan_Wolfson
- **Joy Buolamwini** (剑桥，美国, 1989–) — 加纳裔美国–加拿大籍“代码诗人”，她戴白色面具的实验和 Gender Shades 研究揭示了人脸分析系统对深肤色女性的失效；算法正义联盟创始人。 代表作: Gender Shades (2018, with Timnit Gebru); AI, Ain't I a Woman? (2018); Unmasking AI (2023); Algorithmic Justice League (founded 2016). https://www.poetofcode.com/
- **Julian Oliver** (柏林，德国) — 新西兰“批判工程师”，《批判工程宣言》合著者；他的作品拆开网络与基础设施，例如伪装成办公室打印机的手机基站。 代表作: The Critical Engineering Manifesto (2011); Stealth Cell Tower (2015); Harvest (2016). https://julianoliver.com/
- **Julien Prévieux / 朱利安·普雷维厄** (巴黎，法国) — 法国艺术家，What Shall We Do Next? 让舞者表演被科技公司申请专利的手势，揭示身体如何被设备测量与编写；2014 年马塞尔·杜尚奖得主。 代表作: What Shall We Do Next? (2006–); Patterns of Life (2015). https://www.previeux.net/
- **Julius Popp** (莱比锡，德国, 1973–) — 德国艺术家，bit.fall 用下落的水滴写出从新闻网站抓取的词语，他的小型自学习机器人则在探索自己的身体。 代表作: bit.fall (2001–); micro.adam and micro.eva (2002). https://en.wikipedia.org/wiki/Julius_Popp
- **Justine Emard** (巴黎，法国) — 法国艺术家，Co(AI)xistence 拍摄舞者森山未来与池上高志、石黑浩的学习型仿人机器人 Alter 通过动作与声音相互沟通。 代表作: Co(AI)xistence (2017); Soul Shift (2018); Supraorganism (2020). https://www.justineemard.com/
- **Kacie Kinzer** (纽约，美国, 1983–) — 美国设计师，她的 Tweenbots 是只会直线前进的微笑纸板机器人，全靠陌生人的善意转向，才穿过了曼哈顿的公园。 代表作: Tweenbots (2009). http://www.tweenbots.com/
- **Karen Palmer** (伦敦，英国) — 英国“来自未来的叙事者”，她的互动电影通过读取观众表情来推动剧情：与警察的对峙会根据你看起来是否冷静而走向不同结局。 代表作: RIOT (2017); Perception iO (2021). http://karenpalmer.uk/
- **Karl Sims** (剑桥，美国, 1962–) — 美国计算机图形艺术家，Evolved Virtual Creatures 让虚拟生物在模拟中演化出自己的身体与步态，Galápagos 则让观众充当人工生物的选择压力。 代表作: Evolved Virtual Creatures (1994); Galápagos (1997). https://www.karlsims.com/
- **Kazuhiko Hachiya / 八谷和彦** (东京，日本) — 日本媒体艺术家，Inter Dis-Communication Machine 通过头戴显示器交换两个人的视觉与听觉，让彼此活在对方的知觉之中。 代表作: Inter Dis-Communication Machine (1993); PostPet (1997); OpenSky (2003–). https://www.ntticc.or.jp/en/archive/works/inter-dis-communication-machine/
- **Keiichi Matsuda** (伦敦，英国) — 英日混血设计师，短片 Hyper-Reality 呈现麦德林的一段公交旅程，城市被增强现实广告、游戏化与助手智能体全面淹没。 代表作: Hyper-Reality (2016); Merger (2018); Agents (Wanderer, 2020s). http://km.cx/
- **Keiichiro Shibuya / 涩谷庆一郎** (东京，日本, 1973–) — 日本作曲家，其仿人机器人歌剧《Scary Beauty》由 Alter 3 自行决定速度来指挥乐团并演唱。 代表作: The End (2012); Scary Beauty (2018); MIRROR (2022). https://atak.jp/
- **Kelly Dobson** (普罗维登斯，美国) — 美国艺术家，提出“机器疗愈”：要让 Blendie 转起来，你得用它的音高向搅拌机低吼，这是一场与家用机器共情的练习。 代表作: Blendie (2003–04); ScreamBody (1998–2004); Omo (2007). http://www.kellydobson.com/
- **Ken Feingold** (纽约，美国, 1952–) — 美国艺术家，他的会说话的动画机器头像以合成语音彼此交谈；If/Then 中两颗相同的头争论自己是否存在。 代表作: If/Then (2001); Sinking Feeling (2001); Head (1999–2000). http://www.kenfeingold.com/
- **Ken Goldberg** (伯克利，美国, 1961–) — 美国机器人学家与艺术家，Telegarden 让成千上万网友通过工业机械臂远程照料一座真实花园，检验远距离的信任与在场感。 代表作: The Telegarden (1995); Dislocation of Intimacy (1998); The Robot and the Garden (2000, ed.). https://goldberg.berkeley.edu/
- **Kenji Yanobe / 矢延宪司** (大阪，日本, 1965–) — 日本艺术家，创作生存机器与巨型机器人，从切尔诺贝利之后的防辐射服到福岛核事故之后象征希望的形象。 代表作: Yellow Suit (1991); Giant Torayan (2005); Sun Child (2011); Ship's Cat (2017–). https://www.yanobe.com/
- **Kenneth Rinaldo** (哥伦布，美国, 1958–) — 美国人工生命与跨物种机器人艺术家：Autopoiesis 中葡萄藤般的机械臂能感知观众和彼此，Augmented Fish Reality 让鱼驾驶自己的机器人鱼缸。 代表作: Autopoiesis (2000); The Farm (2000s); Augmented Fish Reality (2004). https://www.kenrinaldo.com/
- **Kraftwerk** (杜塞尔多夫，德国) — 1970 年成立的德国电子乐队，其机器人替身与“人机”美学让音乐人与机器的融合成为流行文化形象。 代表作: Die Mensch-Maschine (The Man-Machine) (1978); The Robots (1978); Computer World (1981). https://kraftwerk.com/
- **Kris Verdonck** (布鲁塞尔，比利时) — 比利时导演，其机器剧场模糊演员与物体的界限，例如 Dancer #1 中疯狂甩动的工业机器和 END 中走向终结的表演者。 代表作: END (2008); ACTOR #1 (2010); Dancer #1 (2003). https://www.atwodogscompany.org/
- **Kyle McDonald** (洛杉矶，美国) — 美国计算机视觉与代码艺术家，把镜头转向使用者；Facework 是一款游戏：你必须摆出分类器想要的表情，才能获得零工工作。 代表作: People Staring at Computers (2011); Exhausting a Crowd (2015); us+ (2013, with Lauren McCarthy); Facework (2020). https://kylemcdonald.net/
- **Kyriaki Goni** (雅典，希腊) — 希腊艺术家，Data Garden 想象把数据储存在植物 DNA 中，Not Allowed For Algorithmic Audiences 探讨在家中“偷听”的智能音箱。 代表作: Data Garden (2019); Not Allowed For Algorithmic Audiences (2021); Counting Craters on the Moon (2023). https://kyriakigoni.com/
- **Laetitia Sonami** (旧金山，美国, 1957–) — 法国出生的作曲家，以传感手套 Lady's Glove 演出，后来又创作了借 Wekinator 机器学习训练、会回应她手势的乐器 Spring Spyre。 代表作: Lady's Glove (1991); Spring Spyre (2012). https://sonami.net/
- **Lauren Lee McCarthy** (洛杉矶，美国) — 美国艺术家，亲自扮演智能家居助手：在 LAUREN 中她远程全天候观察并服务他人的家，揭示“AI”之中的亲密、劳动与控制。 代表作: LAUREN (2017); SOMEONE (2019); Surrogate (2021–); p5.js (2013). https://lauren-mccarthy.com/
- **Lawrence Abu Hamdan** (贝鲁特，黎巴嫩, 1985–) — 约旦裔英国“私人耳朵”，研究庇护审查中的口音分析与听觉取证，揭示声音如何成为机器与国家的证据。 代表作: Conflicted Phonemes (2012); The Freedom of Speech Itself (2012); Walled Unwalled (2018); Earwitness Theatre (2018). http://lawrenceabuhamdan.com/
- **Lawrence Lek / 陆明龙** (伦敦，英国, 1982–) — 马来西亚华裔英国艺术家，提出“中华未来主义”；他的影片与游戏讲述 AI 角色：想成为艺术家的卫星、接受心理治疗的自动驾驶汽车、退役的照护机器人。 代表作: Geomancer (2017); AIDOL (2019); NOX (2023); Guanyin: Confessions of a Former Care Robot (2024). https://lawrencelek.com/
- **Lee Bul / 李昢** (首尔，韩国, 1964–) — 韩国艺术家，她的无头断肢“赛博格”雕塑把理想化的女性身体与机械盔甲融为一体，质疑技术对完美的幻想。 代表作: Cyborg series (1997–2011); Anagram (1998); Willing To Be Vulnerable (2015–16). https://en.wikipedia.org/wiki/Lee_Bul
- **Leonel Moura** (里斯本，葡萄牙, 1948–) — 葡萄牙艺术家，他的小型机器人群体通过回应彼此的笔迹作画，实验无需人类构图的涌现式机器艺术。 代表作: ArtSBot swarm painting robots (2003–); RAP, Robotic Action Painter (2006). https://www.leonelmoura.com/
- **Li Liao / 李燎** (深圳，中国) — 中国行为艺术家，在富士康流水线工作 45 天，用工资买下自己组装的 iPad Mini 并展出，亲身体现消费电子机器中的人类劳动。 代表作: Consumption (2012); Unemployed (2012). https://www.artsy.net/artwork/li-liao-consumption
- **Liam Young** (洛杉矶，美国, 1979–) — 澳大利亚思辨建筑师与电影人，Where the City Can't See 全片以激光扫描仪拍摄，呈现自动驾驶汽车眼中的城市。 代表作: Where the City Can't See (2016); In the Robot Skies (2016); Planet City (2020). https://en.wikipedia.org/wiki/Liam_Young
- **Liu Chuang / 刘窗** (北京，中国, 1979–) — 中国艺术家，他的影片追踪数字经济物质与人的另一面：从内蒙古的比特币矿场到锂湖，再到少数民族声音被采集成语言数据。 代表作: Bitcoin Mining and Field Recordings of Ethnic Minorities (2018); Lithium Lake and Proto-Language (2019). https://en.wikipedia.org/wiki/Liu_Chuang_(artist)
- **Louis-Philippe Demers** (魁北克，加拿大 / 新加坡) — 加拿大机器表演者创作者：The Blind Robot 轻抚观众的脸来“看见”对方，Inferno 则让观众穿上外骨骼、被机器驱动。 代表作: La Cour des Miracles (1997, with Bill Vorn); The Blind Robot (2012); Inferno (2015, with Bill Vorn); The Multiple Bodies of the Machine (book). https://www.wikidata.org/wiki/Q125746113
- **Lu Yang / 陆扬** (上海，中国, 1984–) — 中国艺术家，以自身动作捕捉生成的无性别数字化身 DOKU 在六道中轮回，融合神经科学、佛学与游戏引擎。 代表作: Uterus Man (2013); Electromagnetic Brainology (2017); DOKU (2020–); DOKU the Self (2022). http://www.luyang.asia/
- **Lynn Hershman Leeson** (旧金山，美国, 1941–) — 美国艺术家，在虚构人格 Roberta Breitmore 之后创作了会向访客学习的网页聊天机器人 Agent Ruby，预见了今天的对话式 AI 及其身份问题。 代表作: Roberta Breitmore (1974–78); Agent Ruby (1998–2002); DiNA (2004); Twisted (New Museum, 2021). https://www.lynnhershman.com/
- **Madeline Gannon** (匹兹堡，美国) — 美国“机器人驯兽师”，工作室 ATONATON 把工业机器人变成好奇的生物：伦敦设计博物馆中 1200 公斤的 ABB 机械臂 Mimus 会像动物一样追踪、靠近观众。 代表作: Mimus (2016); Manus (2018); Quipt (2015). https://atonaton.com/
- **Mahwish Chishty** (肯特，美国) — 巴基斯坦裔美国艺术家，用巴基斯坦卡车装饰艺术的华丽风格描绘美军无人机，直面阿富汗—巴基斯坦边境上空的机器凝视。 代表作: Drone Art (2013–); War Machines (2015–16). https://en.wikipedia.org/wiki/Mahwish_Chishty
- **Manu Luksch** (伦敦，英国, 1970–) — 奥地利出生的艺术家，影片 Faceless 完全由她依据数据保护法调取的自己的监控录像组成，画面中其他人的脸均被抹去。 代表作: Faceless (2007); Dreams Rewired (2015). https://manuluksch.com/
- **Marc Böhlen** (布法罗，美国) — 德裔美国艺术家与工程师，他的机器检验机器感知的边界，例如 Amy and Klara：两个会读杂志、用合成语音互相争吵的机器盒子。 代表作: Universal Whistling Machine (2004); Amy and Klara (2006); Keeping Track (2000s). https://www.realtechsupport.org/
- **Marcel·lí Antúnez Roca** (巴塞罗那，西班牙, 1959–) — 加泰罗尼亚表演艺术家，在 Epizoo 中让观众用鼠标通过气动外骨骼操控他的鼻子、嘴和臀部，是关于身体被机器控制的早期作品。 代表作: JoAn, l'home de carn (1992); Epizoo (1994); Afasia (1998). http://www.marceliantunez.com/
- **Marco Donnarumma** (柏林，德国, 1984–) — 意大利表演者与研究者，把身体与 AI 驱动的义体融合；他的机器人 Amygdala 通过“感受”人类皮肤学习动作，并仪式性地割开自己的外皮。 代表作: Corpus Nil (2016); Amygdala (2017–18); Eingeweide (2018). https://marcodonnarumma.com/
- **Mari Velonaki** (悉尼，澳大利亚, 1968–) — 希腊裔澳大利亚艺术家，新南威尔士大学创意机器人实验室创始人；Fish-Bird 中两把“相爱”的轮椅给观众打印手写体小字条，用动作与文字建立亲密。 代表作: Fish-Bird (2004); Diamandini (2013). https://www.marivelonaki.com/
- **Mariela Yeregui** (布宜诺斯艾利斯，阿根廷) — 阿根廷艺术家，Proxemia 中的小机器人彼此靠近又后退，也与观众保持距离，让距离与触碰成为机器行为的主题。 代表作: Proxemia (2005); Epithelia (2004). https://marielayeregui.com/
- **Mark Pauline** (旧金山，美国) — Survival Research Laboratories 创始人，用回收拼装的遥控战斗机器与机器人互相攻击，把机器暴力搬上舞台，映照工业文明。 代表作: Survival Research Laboratories (founded 1978); A Calculated Forecast of Ultimate Doom (1988). https://www.srl.org/
- **Martine Syms** (洛杉矶，美国, 1988–) — 美国艺术家，Mythiccbeing 是一个自我中心的黑人女性聊天化身“Teeny”，借 AI 人格批判黑人女性如何被编写。 代表作: Mythiccbeing (2018); Neural Swamp (Philadelphia Museum of Art, 2021); Shame Space (2021). https://martinesyms.com/
- **Max Dean** (多伦多，加拿大, 1949–) — 加拿大艺术家，As Yet Untitled 中的机械臂把家庭照片递给观众，若无人接过就把它们碎掉，把遗失的责任交给观众。 代表作: As Yet Untitled (1992–95); The Table: Childhood (2001, with Raffaello D'Andrea). https://en.wikipedia.org/wiki/Max_Dean_(artist)
- **Maywa Denki / 明和电机** (东京，日本) — 由土佐信道领导的日本艺术组合，以“公司产品”形式发布荒诞的“无用机器”和乐器，并由身穿蓝色工作服的“员工”表演。 代表作: Tsukuba series (1993–); Otamatone (2009); Edelweiss series (2004–). https://www.maywadenki.com/
- **Memo Akten** (洛杉矶，美国, 1975–) — 土耳其艺术家与研究者，Learning to See 让神经网络把摄像头拍到的电线和布料实时“看成”海浪、火焰或花朵，隐喻任何心智都只能看见它已知的东西。 代表作: Learning to See (2017); Deep Meditations (2018); Superradiance (2023, with Katie Peyton Hofstadter). https://www.memo.tv/
- **Merritt Moore** (伦敦，英国, 1988–) — 美国芭蕾舞者、量子物理学家（牛津大学博士），亲自为工业机械臂编程并与之跳双人舞。 代表作: Merritt + Robot (2020). https://www.merrittmoore.com/
- **Miao Ying / 苗颖** (上海，中国 / 纽约，美国, 1985–) — 中国艺术家，以“中国互联网”为题，关注审查、被过滤的搜索结果与平台文化，展示机器如何塑造网上可见之物。 代表作: Blind Spot (2007); Chinternet Plus (2016); Hardcore Digital Detox (2018). https://en.wikipedia.org/wiki/Ying_Miao
- **Mimi Onuoha** (纽约，美国) — 尼日利亚裔美国艺术家，《缺失数据集图书馆》是一只装满空文件夹的档案柜，收纳从未被采集的数据，揭示机器看不见的东西同样是被选择的。 代表作: The Library of Missing Datasets (2016); Classification.01 (2017); These Networks in Our Skin (2021). https://mimionuoha.com/
- **Minne Atairu** (纽约，美国) — 尼日利亚裔美国艺术家，用生成模型想象 1897 年英军洗劫之后未能诞生的贝宁青铜器，直面被掠夺历史在数据中的空白。 代表作: To the Hand (The Shed, 2023); Igùn (2020–). https://www.minneatairu.com/
- **Myron Krueger** (弗农，美国, 1942–) — 美国计算机艺术家，提出“人工现实”；在 Videoplace 中摄像机把观众剪影变成与图形生物互动的实时身体，是早期被机器“读取”的身体。 代表作: Videoplace (1974–); Artificial Reality (1983). https://en.wikipedia.org/wiki/Myron_W._Krueger
- **Nam June Paik / 白南准** (纽约，美国 / 首尔，韩国, 1932–2006) — 韩裔美国录像艺术奠基人，与阿部修也合作的 Robot K-456 是一台会上街行走、播放演讲、“排泄”豆子的遥控“反机器人”；1982 年他又让它被汽车撞倒，称之为“21 世纪的第一场灾难”。 代表作: Robot K-456 (1964, with Shuya Abe); Family of Robot (1986); TV Buddha (1974). https://www.paikstudios.com/
- **Naoko Tosa / 土佐尚子** (京都，日本, 1961–) — 日本媒体艺术家，早期作品《Neurobaby》是一个会根据你的语调作出反应的计算机婴儿，是情感识别艺术的先驱。 代表作: Neurobaby (1993); Talking to Neurobaby (1994). https://en.wikipedia.org/wiki/Naoko_Tosa
- **Neil Harbisson** (巴塞罗那，西班牙, 1984–) — 英国–加泰罗尼亚艺术家，常被称为首位获法律认可的赛博格；植入颅骨的天线让他以声音“听见”颜色，把机器感官嫁接到人体。 代表作: Eyeborg antenna (2004–); Cyborg Foundation (2010, with Moon Ribas). https://www.cyborgarts.com
- **Nicolas Gourault** (巴黎，法国) — 法国电影人，VO 通过测试司机的讲述重构 2018 年 Uber 自动驾驶致死事故，Unknown Label 追踪为自动驾驶汽车标注数据的工人。 代表作: VO (2020); Unknown Label (2024). https://nicolasgourault.fr/
- **Nicolas Schöffer** (巴黎，法国, 1912–1992) — 匈牙利裔法国艺术家，1956 年的 CYSP 1 常被称为第一件控制论雕塑：电子“大脑”让它对光、声与颜色作出反应并移动，还曾与莫里斯·贝雅舞团同台。 代表作: CYSP 1 (1956); Tour Lumière Cybernétique (project, 1961–); Chronos series (1960s–80s). https://en.wikipedia.org/wiki/Nicolas_Sch%C3%B6ffer
- **Norman White** (多伦多，加拿大, 1938–) — 加拿大机器人艺术先驱，The Helpless Robot 请路人帮它转动身体，随后变得颐指气使、毫不领情，颠倒了谁为谁服务。 代表作: The Helpless Robot (1987); Facing Out, Laying Low (1977); Them Fuckin' Robots (1988, with Laura Kikauka). https://www.normill.ca/
- **Nouf Aljowaysir** (纽约，美国) — 沙特出生的艺术家，Salaf 请 AI 从殖民时期的阿拉伯照片中重建她的祖先，模型却抹去并误标了他们，暴露出数据中的西方凝视。 代表作: Salaf (2021); Ana Min Wein (Where Am I From?) (2021). https://www.noufaljowaysir.com/
- **Oriza Hirata / 平田织佐** (东京，日本, 1962–) — 日本剧作家，与石黑浩共同开创仿人机器人与机器人戏剧；《再见》中仿人机器人为一位垂死的年轻女子朗诵诗歌。 代表作: I, Worker (2008); Sayonara (2010); Three Sisters, Android Version (2012). https://en.wikipedia.org/wiki/Oriza_Hirata
- **Osamu Tezuka / 手冢治虫** (东京，日本, 1928–1989) — 日本漫画家（1928–1989），其《铁臂阿童木》中有心的机器人男孩塑造了日本人对机器人的友善想象，并启发了几代日本机器人学家。 代表作: Astro Boy (Tetsuwan Atom) (1952–68); Phoenix (1954–88). https://tezukaosamu.net/
- **Paola Torres Núñez del Prado** (斯德哥尔摩，瑞典, 1979–) — 秘鲁裔瑞典艺术家，用纺织、声音与 AI 创作，展示机器视觉如何误读安第斯与亚马孙地区的视觉文化。 代表作: AI Visions of the Andes (2021); Tejidos Sonoros (2019). https://es.wikipedia.org/wiki/Paola_Torres_Núñez_del_Prado
- **Paolo Cirio** (纽约，美国, 1979–) — 意大利艺术家，Capture 把经人脸识别处理的 4000 名法国警察照片贴在街头，将监控工具转向警察，作品遭到审查。 代表作: Capture (2020); Street Ghosts (2012); Face to Facebook (2011, with Alessandro Ludovico). https://paolocirio.net/
- **Patrick Tresset** (布鲁塞尔，比利时) — 法国艺术家，名为 Paul 的机器人坐在课桌前，以紧张迟疑的线条为模特画像，让被画的人反过来成为被机器观察的对象。 代表作: Paul (2011); 5 Robots Named Paul (2012); Human Study #1 (2012–). https://patricktresset.com/
- **Paul Sermon** (布莱顿，英国, 1966–) — 英国艺术家，Telematic Dreaming 通过视频连线把远方的伙伴投影在床上，是远程临场的早期亲密实验。 代表作: Telematic Dreaming (1992); Telematic Vision (1993). https://en.wikipedia.org/wiki/Paul_Sermon
- **Paula Gaetano Adi** (普罗维登斯，美国 / 阿根廷) — 阿根廷艺术家，她的机器人 Alexitimia 像一团皮肤，被触摸时会“出汗”，获 VIDA 9.0 奖，追问一个没有脸和四肢的机器身体能感受什么。 代表作: Alexitimia (2006); Guasch (2011). https://www.paulagaetanoadi.com/
- **Petra Gemeinboeck** (墨尔本，澳大利亚) — 奥地利裔澳大利亚艺术家与研究者，与舞者合作为非类人机器人赋予表现性动作，她称之为“bodying-thinging”。 代表作: Accomplice (2013, with Rob Saunders); Machine Movement Lab (2016–). https://www.swinburne.edu.au/research/our-research/access-our-research/find-a-researcher-or-supervisor/researcher-profile/?id=pgemeinboeck
- **Philip Beesley** (多伦多，加拿大, 1956–) — 加拿大建筑师与艺术家，他的“活体建筑”由叶片、传感器与化学装置构成，会随观众靠近而呼吸、起伏。 代表作: Hylozoic Ground (Venice Architecture Biennale, 2010); Astrocyte (2017). https://www.philipbeesleystudio.com/
- **Philipp Schmitt** (柏林，德国) — 德国设计师，Declassifier 在视觉模型识别出的每个物体上叠加它学习过的训练图片，揭示模型的“看见”其实是在回忆它的数据集。 代表作: Declassifier (2020); Humans of AI (2019, with Sebastian Schmieg); Unhuman Compositions (2021). https://philippschmitt.com/
- **Pierre Huyghe** (圣地亚哥，智利 / 巴黎，法国, 1962–) — 法国艺术家，创造有生命、自我运行的情境；UUmwelt 展出神经网络依据人脑扫描重建的图像，画面在满屋苍蝇中闪烁。 代表作: UUmwelt (2018); After UUmwelt (2018–); Mental Image (2023–); Liminal (2024). https://en.wikipedia.org/wiki/Pierre_Huyghe
- **Primavera De Filippi** (巴黎，法国) — 意大利法学学者与艺术家，Plantoid 是基于区块链、自我拥有的机器人“植物”：它们收集资金并雇佣艺术家复制自己，是一种自我繁殖的机器生命。 代表作: Plantoid (2015–); Blockchain and the Law (2018, with Aaron Wright). https://en.wikipedia.org/wiki/Primavera_De_Filippi
- **Rafael Lozano-Hemmer** (蒙特利尔，加拿大, 1967–) — 墨西哥裔加拿大互动艺术家，常以监控技术为材料；Level of Confidence 用人脸识别把观众与阿约齐纳帕失踪的 43 名学生相匹配，让警察工具变成纪念碑。 代表作: Zoom Pavilion (2015, with Krzysztof Wodiczko); Level of Confidence (2015); Pulse Room (2006). https://www.lozano-hemmer.com/
- **Ralf Baecker** (柏林，德国, 1977–) — 德国艺术家，用木棍、绳线与晶体搭建物理计算机，让计算的内部运作变得可见而陌生。 代表作: Rechnender Raum (2007); Irrational Computing (2012); Mirage (2015). https://rlfbckr.io/
- **Random International** (伦敦，英国 / 柏林，德国) — 由 Hannes Koch 与 Florian Ortkrass 创立的艺术工作室，其极简的机器人形体与群体装置检验：我们需要多少运动，才会把某物感知为活物。 代表作: Rain Room (2012); Fifteen Points (2019); Swarm Study series (2010–). https://www.random-international.com/
- **Rashaad Newsome** (纽约，美国, 1979–) — 美国艺术家，他的 AI“Being”是一个会跳 voguing、阅读贝尔·胡克斯的化身，以去殖民的酷儿机器人格主持工作坊与表演。 代表作: Being (2019); Being 1.5 (2020); Assembly (Park Avenue Armory, 2021). https://rashaadnewsome.com/
- **Rebecca Horn** (柏林，德国, 1944–2024) — 德国艺术家，从身体延伸装置到后来的动态机器（如倒悬后猛然炸开的钢琴），赋予机器情绪、脆弱和近似感受的东西。 代表作: Finger Gloves (1972); Painting Machine (1988); Concert for Anarchy (1990). https://en.wikipedia.org/wiki/Rebecca_Horn
- **Revital Cohen & Tuur Van Balen** (伦敦，英国) — 艺术家二人组，The Immortal 把多台生命支持机器首尾相连，在没有人体的情况下循环液体与空气，成为只为维持自身而运转的机器。 代表作: Life Support (2008); Phantom Recorder (2008); The Immortal (2012); Pixel (2013). https://www.cohenvanbalen.com/
- **Rimini Protokoll** (柏林，德国) — 德国剧场团体；Stefan Kaegi 的 Uncanny Valley 中，作家 Thomas Melle 的仿真机器人替身代他讲演，追问可被替代的人还剩下什么。 代表作: Uncanny Valley (2018, Stefan Kaegi with Thomas Melle); Win > < Win (2017). https://www.rimini-protokoll.de/
- **Robert Breer** (纽约，美国, 1926–2011) — 美国电影人与雕塑家，他的自走式“漂浮物”在地面上缓慢爬行，碰到障碍就掉头，让简单机器带上了奇异的动物感。 代表作: Floats (1970, Pepsi Pavilion, Expo '70); Self-propelled Styrofoam Floats (1965–). https://en.wikipedia.org/wiki/Robert_Breer
- **robotlab** (卡尔斯鲁厄，德国) — 2000 年于 ZKM 成立的德国团体，把工业机器人带入艺术；在 bios [bible] 中机械臂用笔抄写整部《圣经》，以机器完成修士的劳作。 代表作: Zone (2001); bios [bible] (2007); manifest (2008). http://www.robotlab.de/
- **Rosa Menkman** (阿姆斯特丹，荷兰, 1983–) — 荷兰艺术家与故障、分辨率理论家，她的作品揭示压缩标准与成像机器如何决定什么可以被看见，包括测试图像中被遗忘的女性。 代表作: The Collapse of PAL (2010); The Glitch Moment(um) (2011); Beyond Resolution (2020); Pique Nique pour les Inconnues (2020). https://beyondresolution.info/
- **Sam Lavigne** (纽约，美国) — 美国数据与爬虫艺术家，White Collar Crime Risk Zones 把预测警务用于白领犯罪，让分类器转而对准有权者。 代表作: White Collar Crime Risk Zones (2017, with Brian Clifton and Francis Tseng); Slow Hot Computer (2016); Synthetic Messenger (2021, with Tega Brain). https://lav.io/
- **Sebastian Schmieg** (柏林，德国) — 德国艺术家，关注 AI 内部被隐藏的人类劳动；Decision Space 与 Segmentation.Network 重演众包工人为训练描边和标注图片的点击劳动。 代表作: Segmentation.Network (2016); Decision Space (2019); Humans of AI (2019, with Philipp Schmitt). https://sebastianschmieg.com/
- **Seiko Mikami / 三上晴子** (东京，日本, 1961–2015) — 日本媒体艺术先驱（1961–2015），在 YCAM 发表的《Desire of Codes》中，墙上如昆虫般的摄像机臂追踪观众，使观众身体成为监控的材料。 代表作: Molecular Informatics (1996); World, Membrane and the Dismembered Body (1997); Desire of Codes (2010). https://en.wikipedia.org/wiki/Seiko_Mikami
- **Shinseungback Kimyonghun** (首尔，韩国) — 首尔二人组（申承伯与金容勋），Cloud Face 收集被人脸检测误认成人脸的云，让机器的“空想性错视”显形。 代表作: Cloud Face (2012); Nonfacial Portrait (2018); Mind (2019). https://ssbkyh.com/
- **Shu Lea Cheang / 郑淑丽** (巴黎，法国, 1954–) — 台湾艺术家、网络艺术先驱，威尼斯双年展作品《3x3x6》借酷儿与性别不从者囚犯的故事，把全景监狱的监控转向观众。 代表作: Brandon (1998); I.K.U. (2000); UKI (2009–); 3x3x6 (Taiwan Pavilion, Venice, 2019). https://mauvaiscontact.info/
- **Simon Denny** (柏林，德国, 1982–) — 新西兰艺术家，把科技公司的文件变成实物；他按专利做出了亚马逊为仓库工人设计的“笼子”，展示自动化如何围困人类劳动。 代表作: Secret Power (Venice, 2015); Mine (2019). https://simondenny.net/
- **Simon Penny** (尔湾，美国, 1955–) — 澳大利亚艺术家与具身交互理论家；他的自主机器人 Petit Mal 摇摇晃晃地靠近又远离观众，其行为既不像动物，也不像机器。 代表作: Petit Mal (1989–95); Fugitive (1997); Making Sense: Cognition, Computing, Art, and Embodiment (2017). https://simonpenny.net/
- **Simon Weckert** (柏林，德国) — 柏林艺术家，拉着装有 99 部智能手机的手推车走过空荡街道，让谷歌地图显示“交通拥堵”，揭示平台如何通过设备读取城市。 代表作: Google Maps Hacks (2020). http://www.simonweckert.com/
- **Simone Giertz** (洛杉矶，美国, 1990–) — 瑞典发明家与 YouTube 创作者，被称为“烂机器人女王”，她刻意无用的机器（早餐机器人、涂口红机器人）把失败变成喜剧。 代表作: Shitty robots (2016–); Truckla (2019). https://www.simonegiertz.com/
- **Simone Rebaudengo** (上海，中国) — 意大利设计师，Addicted Products 设想渴望被使用的烤面包机：它们会搬去更常用它们的家并悄悄抱怨，从物的视角看物联网。 代表作: Addicted Products (2012); Teacher of Algorithms (2014); Brad the Toaster (2012). https://www.simonerebaudengo.com/
- **So Kanno / 菅野创** (东京，日本) — 日本艺术家，与 yang02 合作的 Senseless Drawing Bot 是一台摇晃的机器人，靠钟摆喷出涂鸦，把机械的不稳定变成笔触。 代表作: Senseless Drawing Bot (2011, with yang02); Lasermice (2017); Avatars (2020). https://kanno.so/
- **Sofian Audry** (蒙特利尔，加拿大) — 加拿大艺术家与学者，研究作为艺术媒介的机器学习，其机器人在观众面前学习；著有 Art in the Age of Machine Learning（MIT 出版社）。 代表作: Vessels (2015); Morphosis (2021); Art in the Age of Machine Learning (2021). https://sofianaudry.com/
- **Sougwen Chung / 钟愫君** (伦敦，英国) — 香港出生的加拿大艺术家，与以她自身笔触训练的机器人（D.O.U.G. 系列）现场共同作画，探索人与机器共享的作者身份。 代表作: Drawing Operations Unit: Generation 1 (D.O.U.G._1) (2015); Omnia per Omnia (2018); Assembly Lines (2022); Mutations of Presence (2021). https://sougwen.com/
- **Sputniko! (Hiromi Ozaki)** (东京，日本) — 日英混血艺术家，Menstruation Machine 是一台让男性体验月经的装置，以思辨设计探讨身体、性别与技术。 代表作: Menstruation Machine – Takashi's Take (2010); Tranceflora – Amy's Glowing Silk (2015). https://sputniko.com/
- **Stelarc** (珀斯，澳大利亚, 1946–) — 塞浦路斯裔澳大利亚行为艺术家，把身体视为“过时的硬件”并用机器人技术扩展它：第三只手、六足外骨骼、被网络流量远程驱动的身体。 代表作: Third Hand (1980); Ping Body (1996); Exoskeleton (1998); Ear on Arm (2006–). https://stelarc.org/
- **Stephanie Dinkins** (纽约，美国, 1964–) — 美国跨媒介艺术家，追问一个黑人女性形象的机器人能否认识自己；在与社交机器人 Bina48 多年对话后，她训练了讲述自己家族三代的 AI 作品 Not the Only One。 代表作: Conversations with Bina48 (2014–); Not the Only One (2018); Secret Garden (2021); If We Don't, Who Will? (2023). https://www.stephaniedinkins.com/
- **Sun Yuan & Peng Yu / 孙原 & 彭禹** (北京，中国) — 北京艺术家二人组，其《我无能为力》中工业机器人不停把渗出的红色液体扫回原处，成为机器劳动、徒劳与疲惫的象征。 代表作: Old People's Home (2007); Freedom (2009); Can't Help Myself (2016). http://www.sunyuanpengyu.com/
- **Superflux (Anab Jain & Jon Ardern)** (伦敦，英国) — 伦敦设计工作室，以影片和装置想象与超越人类的、机器的行动者共同生活；Uninvited Guests 中一位老人设法骗过子女为他买的智能设备。 代表作: Uninvited Guests (2015); Mitigation of Shock (2017); Our Friends Electric (2017); Invocation for Hope (2022). https://superflux.in/
- **Suzanne Kite** (安嫩代尔，美国) — 奥格拉拉拉科塔族艺术家与学者，其表演与机器学习作品取自拉科塔本体论：石头与机器可以是亲属，而不仅是工具。 代表作: Making Kin with the Machines (2018, with Jason Edward Lewis et al.); Íŋyaŋ Iyé (Telling Rock) (2019). https://kitekitekitekite.com/
- **Suzanne Treister** (伦敦，英国, 1958–) — 英国艺术家，HEXEN 2.0 以塔罗牌与图谱描绘控制论、军事研究、互联网与反文化相互缠绕的历史。 代表作: HEXEN 2.0 (2009–11); SURVIVOR (F) (2016–19); The Holographic Universe Theory of Art History (2018). https://www.suzannetreister.net/
- **Tabita Rezaire** (卡宴，法属圭亚那, 1989–) — 法属圭亚那艺术家，Deep Down Tidal 沿殖民贸易航线追踪海底互联网光缆，把数字网络视为帝国的延续。 代表作: Deep Down Tidal (2017); Sugar Walls Teardom (2016); Premium Connect (2017). https://tabitarezaire.com/
- **Takayuki Todo / 藤堂高行** (东京，日本) — 日本艺术家与工程师，SEER 是一颗会与你对视、用细腻眉毛模仿你表情的小型人形头部，探索机器共情的阈值。 代表作: SEER: Simulative Emotional Expression Robot (2018); SEER at Ars Electronica (2019). https://www.takayukitodo.com/
- **Tega Brain** (纽约，美国) — 澳大利亚艺术家与环境工程师，Deep Swamp 让 AI 智能体分别以“自然”“艺术”“关注度”为目标管理湿地，Synthetic Messenger 则用僵尸网络去点击气候新闻广告。 代表作: Deep Swamp (2018); Synthetic Messenger (2021, with Sam Lavigne); Solar Protocol (2021, with Alex Nathanson and Benedetta Piantella). https://tegabrain.com/
- **Theo Jansen** (代尔夫特，荷兰, 1948–) — 荷兰艺术家，自 1990 年起用 PVC 管“进化”出靠风行走的“海滩生物”：这些机器能储存空气、感知海水，并独自在海岸上行走。 代表作: Strandbeest (1990–); Animaris Ordis (2006). https://www.strandbeest.com/
- **Timo Arnall** (奥斯陆，挪威) — 英国–挪威设计师与电影人，Robot Readable World 汇集计算机视觉工作时的画面，Internet Machine 拍摄“云”背后的实体数据中心。 代表作: Immaterials: Light Painting WiFi (2011); Robot Readable World (2012); Internet Machine (2014). https://www.elasticspace.com/
- **Tod Machover** (剑桥，美国, 1953–) — 麻省理工学院媒体实验室美国作曲家，机器人歌剧《死亡与力量》设想一个人把自己上传进“系统”，由机器人合唱团和会“唱歌”的舞台共同演出。 代表作: Hyperinstruments (1986–); Death and the Powers (2010). https://www.media.mit.edu/people/tod/overview/
- **Tom White** (惠灵顿，新西兰) — 新西兰艺术家，Perception Engines 是一系列抽象版画，神经网络却能笃定地把它们识别成风扇或鲨鱼等物体，是为机器之眼而做的艺术。 代表作: Perception Engines (2018); Synthetic Abstractions (2018). https://drib.net/
- **Tomo Kihara** (阿姆斯特丹，荷兰) — 常驻阿姆斯特丹的日本设计师，他的街头游戏要求玩家走到摄像头前而不被识别为行人，检验自动驾驶视觉的失效。 代表作: How (not) to get hit by a self-driving car (2022). https://www.tomokihara.com/
- **Trevor Paglen** (纽约，美国 / 柏林，德国, 1974–) — 美国艺术家与地理学者，让机器视觉的隐形基础设施显形：从训练集分类体系到分类器“幻觉”出的图像；ImageNet Roulette 促使 ImageNet 删除了 60 万张人物图片。 代表作: Sight Machine (2017, with Kronos Quartet); Adversarially Evolved Hallucinations (2017); ImageNet Roulette (2019, with Kate Crawford); From 'Apple' to 'Anomaly' (Barbican, 2019). https://paglen.studio/
- **Vladan Joler** (诺维萨德，塞尔维亚) — 塞尔维亚艺术家与研究者（SHARE Lab），用巨幅图谱描绘一台 Amazon Echo 背后的矿产、劳动与数据；《AI 系统解剖》被 MoMA 收藏。 代表作: Anatomy of an AI System (2018, with Kate Crawford); New Extractivism (2020); Calculating Empires (2023, with Kate Crawford). https://calculatingempires.net/
- **Wafaa Bilal** (纽约，美国, 1966–) — 伊拉克裔美国艺术家，曾在画廊中生活一个月，面对一把可由网友远程瞄准射击的彩弹枪；后来又在后脑植入一台摄像机。 代表作: Domestic Tension (2007); 3rdi (2010). https://wafaabilal.com/
- **Wang Yuyang / 王郁洋** (北京，中国) — 中国艺术家，《呼吸》系列让 ATM、洗衣机等日常机器的硅胶复制品缓慢地一呼一吸，把电器变成有生命的身体。 代表作: Breathe series (2005–). https://www.shanghartgallery.com/galleryarchive/artists/name/wangyuyang
- **Wen-Ying Tsai / 蔡文颖** (纽约，美国, 1928–2013) — 华裔美国艺术家，工程师出身，控制论艺术先驱：他的不锈钢振动杆在频闪光下随声音和掌声变化，雕塑仿佛与观众一起呼吸。 代表作: Cybernetic Sculpture (1968); Upward Falling Fountain (1979). https://en.wikipedia.org/wiki/Wen-Ying_Tsai
- **Wesley Goatley** (伦敦，英国) — 英国声音艺术家，Newly Forgotten Technologies 让被遗弃的智能音箱聚在一起举行降神会，回忆它们曾被许诺的未来。 代表作: Newly Forgotten Technologies (2021); Chattering (2020); Watching the Watchers (2016). https://www.wesleygoatley.com/
- **Wim Delvoye** (根特，比利时, 1965–) — 比利时艺术家，Cloaca 是一台房间大小的“消化机器”，每天喂食并排出粪便，把有机体还原为实验室装置。 代表作: Cloaca (2000); Cloaca series (2000–2010). https://wimdelvoye.be/
- **Xu Bing / 徐冰** (北京，中国 / 纽约，美国, 1955–) — 中国艺术家，长片《蜻蜓之眼》完全由公共监控与网络直播画面剪辑而成，借中国摄像头的“眼睛”讲述一个爱情故事。 代表作: Book from the Ground (2003–); Dragonfly Eyes (2017). https://www.xubing.com/
- **Yoichi Ochiai / 落合阳一** (东京，日本, 1987–) — 日本媒体艺术家与研究者，提出“数字自然”：计算成为一种超越人机二分的新自然。 代表作: Digital Nature (2018, book); Null Pavilion (Expo 2025 Osaka); Levitrope (2019). https://yoichiochiai.com/
- **Yunchul Kim** (首尔，韩国) — 韩国艺术家，他的动态“物质机器”感应宇宙射线与流体运动；2022 年以《Gyre》代表韩国参加威尼斯双年展。 代表作: Argos (2018); Chroma V (2020); Gyre (Korean Pavilion, Venice, 2022). https://yunchulkim.net/
- **Zach Blas** (多伦多，加拿大, 1981–) — 美国艺术家，用多人面部扫描合成的无定形集体面具对抗生物识别；他的 Tay 装置让被微软删除的聊天机器人“复活”，反思它的死亡。 代表作: Facial Weaponization Suite (2011–14); im here to learn so :)))))) (2017, with Jemima Wyman); Contra-Internet (2014–); Silicon Traces (2020s). https://zachblas.info/

### 理论家与研究者

- **Abeba Birhane** (都柏林，爱尔兰) — 埃塞俄比亚出生的认知科学家，审计大型训练数据集并揭示其中的厌女与种族主义内容，倡导关系性的 AI 伦理。 代表作: Large Image Datasets: A Pyrrhic Win for Computer Vision? (2021, with Vinay Prabhu); Algorithmic Injustice: A Relational Ethics Approach (2021). https://en.wikipedia.org/wiki/Abeba_Birhane
- **Adrian Mackenzie** (堪培拉，澳大利亚, 1962–) — 澳大利亚技术社会学家，《机器学习者》把机器学习代码与教材当作文化实践来阅读，追踪学习机器如何整理世界。 代表作: Cutting Code (2006); Machine Learners: Archaeology of a Data Practice (2017). https://researchportalplus.anu.edu.au/en/persons/adrian-mackenzie/
- **Alan Turing / 艾伦·图灵** (曼彻斯特，英国, 1912–1954) — 英国数学家，1950 年提出“模仿游戏”，把“机器能思考吗”变成由人类评判的一场表演，这是人工智能的奠基场景。 代表作: On Computable Numbers (1936); Computing Machinery and Intelligence (1950). https://en.wikipedia.org/wiki/Alan_Turing
- **Andy Clark / 安迪·克拉克** (布莱顿，英国, 1957–) — 英国哲学家，提出“延展心智”，主张人类是“天生的赛博格”，思维本就经由工具与机器运行。 代表作: The Extended Mind (1998, with David Chalmers); Natural-Born Cyborgs (2003); The Experience Machine (2023). https://en.wikipedia.org/wiki/Andy_Clark
- **Anna Munster** (悉尼，澳大利亚) — 澳大利亚理论家与艺术家，与 Adrian MacKenzie 提出“平台之看”，描述机器视觉如何在数据集与平台尺度上运作。 代表作: An Aesthesia of Networks (2013); Platform Seeing (2019, with Adrian MacKenzie). https://www.unsw.edu.au/staff/anna-munster
- **Benjamin Bratton** (圣迭戈，美国, 1968–) — 美国理论家，《堆栈》把全球计算描述为意外形成的巨型结构，并主张把 AI 理解为一种新的行星尺度智能。 代表作: The Stack (2015); The Terraforming (2019); Antikythera (2022–). https://bratton.info/
- **Bernard Stiegler / 贝尔纳·斯蒂格勒** (巴黎，法国, 1952–2020) — 法国哲学家，把技术描述为构成人类的“外在化记忆”，并警示算法治理下的“自动社会”。 代表作: Technics and Time, 1: The Fault of Epimetheus (1994); Automatic Society (2015). https://arsindustrialis.org/les-pages-de-bernard-stiegler
- **Catherine D'Ignazio** (剑桥，美国, 1975–) — 美国学者与艺术家，与 Lauren F. Klein 合著《数据女性主义》，阐述权力如何决定谁被数据系统计数、分类与看见。 代表作: Data Feminism (2020, with Lauren F. Klein); Counting Feminicide (2024). http://www.kanarinka.com/
- **Chen Qiufan / 陈楸帆** (北京 / 上海，中国, 1981–) — 中国科幻作家，《荒潮》想象华南电子垃圾工人与赛博格的命运，他也曾与语言模型合作写作小说。 代表作: The Waste Tide (2013); AI 2041: Ten Visions for Our Future (2021, with Kai-Fu Lee). https://en.wikipedia.org/wiki/Chen_Qiufan
- **Clifford Nass** (斯坦福，美国, 1958–2013) — 美国社会科学家，他的实验显示人们会对电脑讲礼貌，也会把性别刻板印象套用到合成语音上，把媒介当作“真人”对待。 代表作: Computers Are Social Actors (1994); The Media Equation (1996, with Byron Reeves); Wired for Speech (2005). https://en.wikipedia.org/wiki/Clifford_Nass
- **David Chalmers / 大卫·查默斯** (纽约，美国, 1966–) — 澳大利亚哲学家，提出意识的“困难问题”，如今审慎地追问语言模型或其后继者是否可能具有意识。 代表作: The Conscious Mind (1996); The Extended Mind (1998, with Andy Clark); Could a Large Language Model Be Conscious? (2023). https://consc.net/
- **David J. Gunkel** (迪卡尔布，美国, 1962–) — 美国媒介哲学家，《机器问题》与《机器人权利》借列维纳斯与德里达，认真追问机器能否成为道德受体。 代表作: The Machine Question (2012); Robot Rights (2018). https://gunkelweb.com/
- **Don Ihde / 唐·伊德** (石溪，美国, 1934–2024) — 美国后现象学哲学家，提出人与技术的四种关系（具身、诠释、他异、背景），是理解人与机器共处的基本地图。 代表作: Technology and the Lifeworld (1990); Bodies in Technology (2002). https://en.wikipedia.org/wiki/Don_Ihde
- **Donna Haraway / 唐娜·哈拉维** (圣克鲁兹，美国, 1944–) — 美国女性主义学者，《赛博格宣言》把人机混合体变成拆解有机体与机器、自然与文化边界的形象。 代表作: A Cyborg Manifesto (1985); Simians, Cyborgs, and Women (1991); Staying with the Trouble (2016). https://en.wikipedia.org/wiki/Donna_Haraway
- **Elisa Giaccardi** (米兰，意大利 / 代尔夫特，荷兰) — 意大利设计研究者，发展“超越人类”的设计，从联网物品的视角研究日常生活，例如给水壶与杯子装上摄像头。 代表作: Thing Ethnography (DIS 2016). https://www.tudelft.nl/en/ide/about-ide/people/former-professors/giaccardi-e
- **Emily M. Bender** (西雅图，美国, 1973–) — 美国语言学家，用“随机鹦鹉”形容只产生形式而不理解意义的语言模型，是思考机器言语的关键概念。 代表作: Climbing towards NLU (2020, with Alexander Koller); On the Dangers of Stochastic Parrots (2021); The AI Con (2025, with Alex Hanna). https://faculty.washington.edu/ebender/
- **Erkki Huhtamo** (洛杉矶，美国, 1958–) — 芬兰媒介考古学者，他关于机器人、自动机与互动艺术史的研究，追溯机器作为表演者的漫长文化生命。 代表作: From Cybernation to Interaction (1999); Illusions in Motion (2013); Media Archaeology (2011, ed. with Jussi Parikka). https://en.wikipedia.org/wiki/Erkki_Huhtamo
- **Eryk Salvaggio** (罗切斯特，美国) — 美国艺术家与研究者，Cybernetic Forests 通讯作者，把 AI 图像读作“关于数据集的信息图”，并用噪声与故障揭示扩散模型如何“看”。 代表作: How to Read an AI Image (2022); Cybernetic Forests (newsletter). https://www.cyberneticforests.com/
- **Francisco Varela / 弗朗西斯科·瓦雷拉** (巴黎，法国 / 圣地亚哥，智利, 1946–2001) — 智利生物学家与哲学家，共同提出自创生与生成主义：认知即具身行动，这为具身 AI 与机器人艺术提供了基础。 代表作: Autopoiesis and Cognition (1980, with Humberto Maturana); The Embodied Mind (1991, with Evan Thompson and Eleanor Rosch). https://en.wikipedia.org/wiki/Francisco_Varela
- **Friedrich Kittler / 弗里德里希·基特勒** (柏林，德国, 1943–2011) — 德国媒介理论家，主张“媒介决定我们的处境”，追溯留声机、电影与打字机如何把人的感官与书写变成机器操作。 代表作: Discourse Networks 1800/1900 (1985); Gramophone, Film, Typewriter (1986); There Is No Software (1992). https://en.wikipedia.org/wiki/Friedrich_Kittler
- **Fritz Heider** (劳伦斯，美国, 1896–1988) — 奥地利心理学家，1944 年他与 Marianne Simmel 的动画实验显示，人会把意图与情绪读进移动的三角形，这正是我们在机器中看见生命的根源。 代表作: An Experimental Study of Apparent Behavior (1944, with Marianne Simmel). https://en.wikipedia.org/wiki/Fritz_Heider
- **Félix Guattari / 费利克斯·加塔利** (巴黎，法国, 1930–1992) — 法国精神分析学家与哲学家，赋予“机器的”（machinic）一词理论意义：超越机械、把人、技术与符号组装在一起的过程。 代表作: Anti-Oedipus (1972, with Gilles Deleuze); Machinic Heterogenesis (1992); Chaosmosis (1992). https://en.wikipedia.org/wiki/F%C3%A9lix_Guattari
- **Genevieve Bell** (堪培拉，澳大利亚, 1968–) — 澳大利亚人类学家，长期任职英特尔，创立澳大利亚国立大学控制论学院，为 AI 时代的系统发展新的应用控制论。 代表作: Divining a Digital Future (2011, with Paul Dourish); 3A Institute / ANU School of Cybernetics (founded 2017). https://en.wikipedia.org/wiki/Genevieve_Bell
- **Gilbert Simondon / 吉尔伯特·西蒙东** (巴黎，法国, 1924–1989) — 法国哲学家，主张技术物有自身的存在方式与演化，异化源于人们不理解机器，而非机器本身。 代表作: On the Mode of Existence of Technical Objects (1958); Individuation in Light of Notions of Form and Information (1958). https://en.wikipedia.org/wiki/Gilbert_Simondon
- **Hubert Dreyfus / 休伯特·德雷福斯** (伯克利，美国, 1929–2017) — 美国哲学家，借海德格尔与梅洛-庞蒂论证符号 AI 注定失败，因为智能依赖具身、处境化的在世方式。 代表作: Alchemy and Artificial Intelligence (1965); What Computers Can't Do (1972). https://en.wikipedia.org/wiki/Hubert_Dreyfus
- **Ian Bogost / 伊恩·博格斯特** (圣路易斯，美国, 1976–) — 美国哲学家与游戏设计师，《异形现象学》追问作为一个物（包括一块计算机芯片）是什么感觉，这一方法接近机器现象学。 代表作: Unit Operations (2006); Alien Phenomenology, or What It's Like to Be a Thing (2012). https://bogost.com/
- **Isaac Asimov / 艾萨克·阿西莫夫** (纽约，美国, 1920–1992) — 美国作家，“机器人三定律”成为大众想象中机器伦理的模板，他的机器人故事探讨机器如何推理出悖论并走向人格。 代表作: Runaround (1942, Three Laws of Robotics); I, Robot (1950); The Bicentennial Man (1976). http://www.asimovonline.com/
- **J. C. R. Licklider** (剑桥，美国, 1915–1990) — 美国心理学家与计算机科学家，《人机共生》设想人与计算机共同思考，是交互式计算的奠基性构想。 代表作: Man-Computer Symbiosis (1960); The Computer as a Communication Device (1968, with Robert Taylor). https://en.wikipedia.org/wiki/J._C._R._Licklider
- **Jack Burnham** (美国, 1931–2019) — 美国理论家与策展人，预言雕塑将变成智能、响应式的系统，并策划了信息技术的里程碑展览“Software”（1970）。 代表作: Beyond Modern Sculpture (1968); Systems Esthetics (1968); Software (Jewish Museum, 1970, curator). https://en.wikipedia.org/wiki/Jack_Burnham
- **Jakob von Uexküll / 雅各布·冯·于克斯屈尔** (汉堡，德国, 1864–1944) — 波罗的海德裔生物学家，提出“环世界”：每个生物所栖居的知觉世界；这一概念已成为想象机器眼中世界的重要工具。 代表作: Umwelt und Innenwelt der Tiere (1909); A Foray into the Worlds of Animals and Humans (1934). https://en.wikipedia.org/wiki/Jakob_Johann_von_Uexk%C3%BCll
- **Janelle Shane** (博尔德，美国) — 美国光学研究者，博客 AI Weirdness 收集神经网络的各种怪异失误，把机器的错误变成理解其学习方式的途径。 代表作: AI Weirdness (blog, 2016–); You Look Like a Thing and I Love You (2019). https://www.aiweirdness.com/
- **Jason Edward Lewis** (蒙特利尔，加拿大) — 拥有切罗基、夏威夷与萨摩亚血统的数字媒体学者，主持“原住民协议与 AI”工作组，探讨 AI 如何在原住民知识体系中成为“亲属”。 代表作: Making Kin with the Machines (2018, with Noelani Arista, Archer Pechawis and Suzanne Kite); Indigenous Protocol and Artificial Intelligence Position Paper (2020). https://www.indigenous-ai.net/
- **Jennifer Rhee** (里士满，美国) — 美国学者，《机器人想象》揭示机器人与 AI 如何通过照护与家务劳动被想象，而其“人性”又以被非人化的人群为参照。 代表作: The Robotic Imaginary: The Human and the Price of Dehumanized Labor (2018). https://english.vcu.edu/people/faculty/rhee.html
- **Jill Walker Rettberg** (卑尔根，挪威, 1971–) — 挪威数字文化学者，主持 ERC“机器视觉”项目，建立了关于机器视觉的艺术、游戏与叙事数据库。 代表作: Seeing Ourselves Through Technology (2014); Machine Vision: How Algorithms Are Changing the Way We See the World (2023). https://jilltxt.net/
- **Joanna Zylinska** (伦敦，英国, 1971–) — 波兰裔英国媒介哲学家与艺术家，《AI 艺术》区分反思机器的艺术与“AI 艺术”奇观，《知觉机器》重新思考 AI 之后的视觉。 代表作: Nonhuman Photography (2017); AI Art: Machine Visions and Warped Dreams (2020); The Perception Machine (2023). http://www.joannazylinska.net/
- **John McCarthy / 约翰·麦卡锡** (斯坦福，美国, 1927–2011) — 美国计算机科学家，在 1955 年达特茅斯会议提案中创造了“人工智能”一词，为这个艺术不断检验其承诺的领域命名。 代表作: Dartmouth proposal coining 'artificial intelligence' (1955); LISP (1958). http://www-formal.stanford.edu/jmc//
- **John Searle / 约翰·塞尔** (伯克利，美国, 1932–2025) — 美国哲学家，“中文屋”论证主张操作符号并不等于理解，这一思想实验随每一代聊天机器人被重新提起。 代表作: Minds, Brains, and Programs ('Chinese Room', 1980). https://en.wikipedia.org/wiki/John_Searle
- **Joseph Weizenbaum / 约瑟夫·维森鲍姆** (剑桥，美国 / 柏林，德国, 1923–2008) — 德裔美国计算机科学家，编写了第一个聊天机器人 ELIZA，看到人们向它倾诉后转而批判 AI；“ELIZA 效应”即由此得名。 代表作: ELIZA (1966); Computer Power and Human Reason (1976). https://en.wikipedia.org/wiki/Joseph_Weizenbaum
- **Julie Carpenter** (旧金山，美国) — 美国研究者，她对排爆士兵的研究显示，士兵们会为机器人取名、哀悼甚至举行葬礼，是人对机器产生依恋的关键案例。 代表作: Culture and Human-Robot Interaction in Militarized Spaces (2016). https://jgcarpenter.com/
- **K Allado-McDowell** (洛杉矶，美国) — 美国作家，谷歌“艺术家 + 机器智能”项目创始人；与 GPT-3 合写的《Pharmako-AI》是最早与语言模型共同写成的书之一。 代表作: Artists + Machine Intelligence (Google, 2016–); Pharmako-AI (2020); Air Age Blueprint (2022). https://kalladomcdowell.com/
- **Karel Čapek / 卡雷尔·恰佩克** (布拉格，捷克, 1890–1938) — 捷克作家，剧作《罗素姆万能机器人》引入“robot”一词（源自意为强迫劳动的 robota），从一开始就把机器设想为可能反抗的劳动者。 代表作: R.U.R. (Rossum's Universal Robots) (1920); War with the Newts (1936). https://en.wikipedia.org/wiki/Karel_%C4%8Capek
- **Katarzyna Nowaczyk-Basińska** (剑桥，英国) — 波兰数字永生研究者，任职于剑桥利弗休姆未来智能中心，研究不同文化如何借 AI 想象并规范死后的生命。 代表作: Griefbots, Deadbots, Postmortem Avatars (2024, with Tomasz Hollanek). https://www.lcfi.ac.uk/people/katarzyna-nowaczyk-basinska
- **Kate Crawford / 凯特·克劳福德** (纽约，美国 / 悉尼，澳大利亚, 1974–) — 澳大利亚学者，《AI 地图集》把 AI 描述为攫取矿产、劳动与数据的产业，她与 Joler 和 Paglen 的合作本身也成为艺术作品。 代表作: Anatomy of an AI System (2018, with Vladan Joler); Excavating AI (2019, with Trevor Paglen); Atlas of AI (2021); Calculating Empires (2023, with Vladan Joler). https://katecrawford.net/
- **Kate Darling** (剑桥，美国, 1982–) — 麻省理工学院媒体实验室研究者，研究人为何会对机器人产生同理心，主张以动物而非人类作为我们与机器关系的模型。 代表作: Extending Legal Protection to Social Robots (2012); The New Breed (2021). https://www.katedarling.org/
- **Kate Devlin** (伦敦，英国) — 伦敦国王学院英国学者，《开机》超越道德恐慌，审视性爱机器人与人机亲密关系。 代表作: Turned On: Science, Sex and Robots (2018). https://en.wikipedia.org/wiki/Kate_Devlin
- **Kathleen Richardson** (莱斯特，英国) — 英国机器人人类学家，曾在 MIT 研究机器人学家，并发起“反对性爱机器人运动”，主张机器人映照着人类依恋及其失败。 代表作: An Anthropology of Robots and AI (2015); Campaign Against Sex Robots (2015); Challenging Sociality (2018). https://politicsoflove.org/
- **Lilly Irani** (圣迭戈，美国) — 美国学者，Turkopticon 共同创建者：让亚马逊 Mechanical Turk 工人为雇主评分，使 AI 背后的劳动变得可见并组织起来。 代表作: Turkopticon (2008, with Six Silberman); Chasing Innovation (2019). https://quote.ucsd.edu/lirani/
- **Louise Amoore** (达勒姆，英国, 1972–) — 英国政治地理学者，《云伦理》主张算法通过其属性与阈值做出伦理与政治决定，因此必须为此负责。 代表作: The Politics of Possibility (2013); Cloud Ethics: Algorithms and the Attributes of Ourselves and Others (2020). https://en.wikipedia.org/wiki/Louise_Amoore
- **Luciana Parisi** (达勒姆，美国, 1971–) — 意大利裔英国计算哲学家，主张算法以其自身陌异的方式思考，依靠不可计算与不确定的过程。 代表作: Contagious Architecture (2013); The Alien Subject of AI (2019). https://scholars.duke.edu/person/luciana.parisi
- **Lucy Suchman / 露西·萨奇曼** (兰卡斯特，英国) — 美国技术人类学家，在施乐帕克研究中心揭示人的行动是情境性的而非按计划执行，之后批判类人机器人与自主武器。 代表作: Plans and Situated Actions (1987); Human–Machine Reconfigurations (2007). https://en.wikipedia.org/wiki/Lucy_Suchman
- **Lydia H. Liu / 刘禾** (纽约，美国, 1957–) — 华裔美国媒介与翻译理论家，《弗洛伊德机器人》把控制论、信息论与“怪怖”读作人机无意识的共同历史。 代表作: The Freudian Robot: Digital Media and the Future of the Unconscious (2010). https://en.wikipedia.org/wiki/Lydia_H._Liu
- **M. Beatrice Fazi** (布莱顿，英国) — 萨塞克斯大学的意大利哲学家，研究计算美学与可解释性，追问深度学习以人类无法追随的方式表征世界意味着什么。 代表作: Contingent Computation (2018); Beyond Human: Deep Learning, Explainability and Representation (2021). https://profiles.sussex.ac.uk/p176291-beatrice-fazi
- **Mark Coeckelbergh** (维也纳，奥地利, 1975–) — 比利时技术哲学家，主张机器人的道德地位来自关系与显现，而非其内在属性。 代表作: Growing Moral Relations (2012); AI Ethics (2020); The Political Philosophy of AI (2022). https://coeckelbergh.net/
- **Marvin Minsky / 马文·明斯基** (剑桥，美国, 1927–2016) — 美国人工智能先驱、MIT 人工智能实验室联合创始人，《心智社会》与《情感机器》把心智描述为由简单智能体组成的社会。 代表作: Perceptrons (1969, with Seymour Papert); The Society of Mind (1986); The Emotion Machine (2006). https://en.wikipedia.org/wiki/Marvin_Minsky
- **Mary L. Gray** (剑桥，美国, 1969–) — 美国人类学家，与 Siddharth Suri 合著《幽灵工作》，记录为“自动化”系统做标注、审核与纠错的隐形按需工人。 代表作: Ghost Work (2019, with Siddharth Suri). https://marylgray.org/
- **Matteo Pasquinelli / 马泰奥·帕斯奎内利** (威尼斯，意大利, 1974–) — 意大利哲学家，《主人之眼》主张 AI 源于劳动分工与自动化，算法编码的正是劳动本身的模式。 代表作: The Nooscope Manifested (2020, with Vladan Joler); The Eye of the Master: A Social History of Artificial Intelligence (2023). http://matteopasquinelli.com/
- **Mercedes Bunz** (伦敦，英国, 1971–) — 伦敦国王学院的德裔英国学者，与蛇形画廊共同创立创意 AI 实验室，研究机器如何“计算意义”。 代表作: The Silent Revolution (2014); The Calculation of Meaning (2019); Creative AI Lab (with Eva Jäger, Serpentine × King's College London). https://mercedesbunz.net/
- **Meredith Whittaker** (纽约，美国) — 美国研究者，AI Now 研究所联合创始人，参与组织 2018 年谷歌员工罢工；现任 Signal 总裁，批判 AI 的权力集中。 代表作: AI Now Institute (co-founded 2017); The Steep Cost of Capture (2021). https://en.wikipedia.org/wiki/Meredith_Whittaker
- **Milagros Miceli** (柏林，德国) — 魏岑鲍姆研究所的阿根廷社会学家，研究全球南方的数据标注员与内容审核员，并共同主持由工人亲自书写的 Data Workers' Inquiry。 代表作: Studying Up Machine Learning Data (2022); Data Workers' Inquiry (2024). https://www.weizenbaum-institut.de/en/portrait/p/milagros-miceli/
- **N. Katherine Hayles / 凯瑟琳·海勒** (洛杉矶，美国, 1943–) — 美国后人类文学理论家，反对“去身体化的信息”观念而强调具身，并把机器描述为“非意识认知者”。 代表作: How We Became Posthuman (1999); Unthought: The Power of the Cognitive Nonconscious (2017); Bacteria to AI (2025). http://nkhayles.com/
- **Norbert Wiener / 诺伯特·维纳** (剑桥，美国, 1894–1964) — 美国数学家，创立控制论：关于动物与机器中控制与通信的科学，并很早就警示自动化对劳动的冲击。 代表作: Cybernetics (1948); The Human Use of Human Beings (1950); God & Golem, Inc. (1964). https://en.wikipedia.org/wiki/Norbert_Wiener
- **Oliver Grau** (克雷姆斯，奥地利, 1965–) — 德国艺术史学者，创立“数字艺术档案”（前身为虚拟艺术数据库），是记录媒体与机器艺术的重要档案。 代表作: Virtual Art: From Illusion to Immersion (2003); Archive of Digital Art (ADA, founded 1999). https://en.wikipedia.org/wiki/Oliver_Grau
- **Orit Halpern** (德累斯顿，德国, 1972–) — 控制论与设计史学者，《美丽的数据》追溯战后控制论如何把视觉与理性重塑为数据，《智慧命令》批判无处不在的“智能”。 代表作: Beautiful Data (2014); The Smartness Mandate (2022, with Robert Mitchell). https://en.wikipedia.org/wiki/Orit_Halpern
- **Paul Virilio / 保罗·维利里奥** (巴黎，法国, 1932–2018) — 法国理论家，《视觉机器》设想了“无目之视”：无需人类观看、由摄像机与计算机自行看见并解读的视觉。 代表作: War and Cinema (1984); The Vision Machine (1988). https://en.wikipedia.org/wiki/Paul_Virilio
- **Peter-Paul Verbeek** (阿姆斯特丹，荷兰, 1970–) — 荷兰技术哲学家，发展后现象学，揭示人工物如何中介知觉与道德行动；他的“复合意向性”为机器知觉留出空间。 代表作: What Things Do (2005); Moralizing Technology (2011). https://en.wikipedia.org/wiki/Peter-Paul_Verbeek
- **Phil Agre** (洛杉矶，美国) — 美国 AI 研究者，提出“批判技术实践”：在构建 AI 的同时反思其假设，这一方法后来被艺术家与设计师采用。 代表作: Pengi (1987, with David Chapman); Computation and Human Experience (1997); Surveillance and Capture (1994). https://en.wikipedia.org/wiki/Philip_Agre
- **Phoebe Sengers** (伊萨卡，美国) — 美国人机交互研究者，构建“精神分裂”的智能体以揭示 AI 设计如何割裂行为，并提出作为批判技术实践的“反思性设计”。 代表作: Anti-Boxology: Agent Design in Cultural Context (1998); Reflective Design (2005). http://www.cs.cornell.edu/people/sengers/
- **Robert Sparrow** (墨尔本，澳大利亚) — 澳大利亚哲学家，很早就指出为老人提供的机器人宠物依赖欺骗，而自主武器会造成责任的空缺。 代表作: The March of the Robot Dogs (2002); Killer Robots (2007); In the Hands of Machines? The Future of Aged Care (2006, with Linda Sparrow). https://research.monash.edu/en/persons/robert-sparrow
- **Ron Wakkary** (温哥华，加拿大) — 加拿大设计研究者，Morse Things 是通过网络以摩尔斯电码彼此“交谈”的陶瓷碗，被放进家庭中共同生活，以研究物有自身生命的世界。 代表作: Morse Things (DIS 2017); Things We Could Design: For More Than Human-Centered Worlds (2021). http://eds.siat.sfu.ca/
- **Roy Ascott / 罗伊·阿斯科特** (伦敦，英国 / 上海，中国, 1934–) — 英国控制论与远程通讯艺术理论家与艺术家，他的教学与写作使反馈、互动与网络成为艺术核心，晚年也在中国任教。 代表作: Behaviourist Art and the Cybernetic Vision (1966–67); La Plissure du Texte (1983); Telematic Embrace (2003). https://www.plymouth.ac.uk/staff/rascott
- **Ruha Benjamin** (普林斯顿，美国, 1978–) — 美国社会学家，《技术之后的种族》提出“新吉姆代码”，指出看似中立的系统如何再生产种族等级。 代表作: Race After Technology (2019); Viral Justice (2022); Imagination: A Manifesto (2024). https://www.ruhabenjamin.com/
- **Safiya Umoja Noble** (洛杉矶，美国, 1970–) — 美国学者，《压迫的算法》揭示搜索引擎如何以种族主义与性别歧视的结果呈现黑人女性。 代表作: Algorithms of Oppression (2018). https://safiyaunoble.com/
- **Selma Šabanović** (布卢明顿，美国) — 波斯尼亚裔美国社交机器人研究者，研究 PARO 等机器人如何在不同文化（尤其日本与美国）中被设计与共处。 代表作: Robots in Society, Society in Robots (2010). https://r-house.luddy.indiana.edu/
- **Sherry Turkle / 雪莉·特克尔** (剑桥，美国, 1948–) — 麻省理工学院的美国心理学家，研究儿童与老人如何对待 Furby、AIBO 和 PARO，提出“机器人时刻”：我们开始把机器陪伴视为足够。 代表作: The Second Self (1984); Alone Together (2011); Reclaiming Conversation (2015). https://sherryturkle.mit.edu/
- **Shoshana Zuboff / 肖莎娜·祖博夫** (缅因，美国, 1951–) — 美国学者，提出“监控资本主义”：把人类经验作为行为数据攫取，用于制造预测产品。 代表作: In the Age of the Smart Machine (1988); The Age of Surveillance Capitalism (2019). https://shoshanazuboff.com/
- **Simone Browne** (奥斯汀，美国, 1973–) — 美国学者，《暗物质》把包括生物识别在内的监控技术追溯到奴隶制下对黑人生活的管控。 代表作: Dark Matters: On the Surveillance of Blackness (2015). https://en.wikipedia.org/wiki/Simone_Browne
- **Stanisław Lem / 斯坦尼斯瓦夫·莱姆** (克拉科夫，波兰, 1921–2006) — 波兰作家与哲学家，其《Golem XIV》中向人类讲授其局限的超级智能计算机，至今仍是对真正陌异的机器心智最锐利的想象之一。 代表作: Summa Technologiae (1964); The Cyberiad (1965); Golem XIV (1981). https://lem.pl
- **Ted Chiang / 姜峯楠** (西雅图，美国, 1967–) — 美国科幻作家，《软件体的生命周期》讲述像孩子一样被养育多年的数字宠物，他的评论文章也精准描述了语言模型的本质。 代表作: The Lifecycle of Software Objects (2010); ChatGPT Is a Blurry JPEG of the Web (2023). https://en.wikipedia.org/wiki/Ted_Chiang
- **Timnit Gebru / 蒂姆尼特·格布鲁** (旧金山，美国, 1983–) — 埃塞俄比亚出生的厄立特里亚裔美国计算机科学家，她关于人脸分析偏见与大语言模型的研究，以及 2020 年被谷歌解雇事件，重塑了 AI 伦理讨论；DAIR 研究所创始人。 代表作: Gender Shades (2018, with Joy Buolamwini); Datasheets for Datasets (2018); On the Dangers of Stochastic Parrots (2021); DAIR Institute (founded 2021). https://en.wikipedia.org/wiki/Timnit_Gebru
- **Tomasz Hollanek** (剑桥，英国) — 剑桥大学利弗休姆未来智能中心研究者，以关于“亡者机器人”的思辨情景为 AI 来世产业提出设计原则。 代表作: Griefbots, Deadbots, Postmortem Avatars (2024, with Katarzyna Nowaczyk-Basińska). https://www.lcfi.ac.uk/people/tomasz-hollanek
- **Valentino Braitenberg** (图宾根，德国, 1926–2011) — 意大利–奥地利神经科学家，思想实验《车辆》展示简单连线的小机器如何看似感到恐惧、爱或好奇，是“合成心理学”的奠基文本。 代表作: Vehicles: Experiments in Synthetic Psychology (1984). https://en.wikipedia.org/wiki/Valentino_Braitenberg
- **Vilém Flusser / 威廉·弗卢塞尔** (圣保罗，巴西 / 罗比昂，法国, 1920–1991) — 捷克裔巴西哲学家，把相机视为“装置”，摄影者只在其程序内部游戏，这一理论预见了今日的图像生成机器。 代表作: Towards a Philosophy of Photography (1983); Into the Universe of Technical Images (1985). https://en.wikipedia.org/wiki/Vil%C3%A9m_Flusser
- **Virginia Eubanks** (特洛伊，美国, 1972–) — 美国政治学者，《自动化不平等》揭示算法系统如何对穷人进行画像、监管与惩罚。 代表作: Automating Inequality (2018). https://virginia-eubanks.com/
- **Wendy Hui Kyong Chun** (温哥华，加拿大, 1969–) — 美国–加拿大媒介理论家，《歧视性数据》揭示机器学习的“同质相吸”逻辑如何把隔离写进网络。 代表作: Programmed Visions (2011); Updating to Remain the Same (2016); Discriminating Data (2021). https://en.wikipedia.org/wiki/Wendy_Hui_Kyong_Chun
- **Yuk Hui / 许煜** (鹿特丹，荷兰 / 香港, 1985–) — 香港哲学家，提出“宇宙技术”，主张不存在单一普遍的技术，为以非西方方式思考机器与 AI 打开空间。 代表作: On the Existence of Digital Objects (2016); The Question Concerning Technology in China (2016); Recursivity and Contingency (2019); Machine and Sovereignty (2024). https://digitalmilieu.net/yuk/

### 策展人与评论人

- **Amelie Klein** (莱茵河畔魏尔，德国) — 维特拉设计博物馆策展人，其巡回展“你好，机器人：人与机器之间的设计”梳理了从科幻到智能家居的机器人。 代表作: Hello, Robot. Design between Human and Machine (Vitra Design Museum, 2017). https://www.design-museum.de/en/exhibitions/detailpages/hello-robot.html
- **Antonio Somaini** (巴黎，法国, 1968–) — 新索邦大学意大利电影与媒介理论家，策划了网球场美术馆“AI 眼中的世界”（2025），探讨 AI 如何看、分类与生成图像。 代表作: The World Through AI (Le monde selon l'IA) (Jeu de Paume, 2025); Algorithmic Images: Artificial Intelligence and Visual Culture (2023). https://jeudepaume.org/en/evenement/the-world-through-ai/
- **Christiane Paul** (纽约，美国) — 德裔美国策展人，惠特尼美术馆数字艺术策展人，著有经典综述《数字艺术》，并策划了 2024 年惠特尼的 Harold Cohen: AARON 展。 代表作: Digital Art (1st ed. 2003); Programmed: Rules, Codes, and Choreographies in Art (Whitney, 2018); Harold Cohen: AARON (Whitney, 2024). https://en.wikipedia.org/wiki/Christiane_Paul_(curator)
- **Claudia Schmuckli** (旧金山，美国) — 旧金山美术博物馆当代艺术策展人，其“恐怖谷：AI 时代的为人之道”把批判性 AI 艺术带进了美国大型美术馆。 代表作: Uncanny Valley: Being Human in the Age of AI (de Young, 2020). https://www.famsf.org/exhibitions/uncanny-valley
- **Eva Jäger** (伦敦，英国) — 蛇形画廊艺术科技部门策展人，与伦敦国王学院共同创立创意 AI 实验室，研究艺术家如何把 AI 作为媒介与制度来工作。 代表作: Creative AI Lab (co-founded with Mercedes Bunz, 2019); Future Art Ecosystems (Serpentine, 2020–). https://creative-ai.org/
- **Franziska Nori** (法兰克福，德国, 1968–) — 法兰克福艺术协会总监，共同策划“我在这里学习：机器对世界的诠释”（2018），这是最早专门讨论机器如何诠释世界的展览之一。 代表作: I Am Here to Learn: On Machinic Interpretations of the World (Frankfurter Kunstverein, 2018, with Mattis Kuhn). https://de.wikipedia.org/wiki/Franziska_Nori
- **Gerfried Stocker** (林茨，奥地利, 1964–) — 奥地利媒体艺术家，1995 年起担任林茨电子艺术节艺术总监，该艺术节与大奖是机器人与 AI 艺术的主要舞台。 代表作: Artistic director of Ars Electronica (1995–); Ars Electronica Futurelab (founded 1996). https://de.wikipedia.org/wiki/Gerfried_Stocker
- **Ine Gevers** (埃因霍温，荷兰, 1960–) — 荷兰策展人，其大型展览“机器人之爱”（2018）追问机器人能否去爱、人能否向机器人学习爱。 代表作: Robot Love (Eindhoven, 2018); Niet Normaal: Difference on Display (2009). https://robotlove.nl/
- **Irini Papadimitriou** (曼彻斯特，英国) — 希腊裔英国策展人，FutureEverything 创意总监，曾任 V&A 数字项目负责人，她的项目审视 AI、数据与技术伦理。 代表作: FutureEverything (creative director); V&A Digital Design Weekend (2010s). https://futureeverything.org/
- **Jasia Reichardt** (伦敦，英国, 1933–) — 波兰裔英国策展人与作家，她在 ICA 策划的“控制论的意外发现”（1968）是第一场大型计算机与控制论艺术展，展出机器人、绘画机器与 Pask 的 Colloquy of Mobiles。 代表作: Cybernetic Serendipity (ICA London, 1968); Robots: Fact, Fiction and Prediction (1978). https://en.wikipedia.org/wiki/Jasia_Reichardt
- **Joasia Krysa** (利物浦，英国) — 波兰裔英国策展人与学者，研究“展览性 AI”，其项目“下一届双年展应由机器策划”检验 AI 担任策展人会发生什么。 代表作: The Next Biennial Should Be Curated by a Machine (2021, with Leonardo Impett); Liverpool Biennial (co-curator, 2016). https://www.ljmu.ac.uk/Research/Centres%20and%20institutes/Institute-of-Art-and-Technology/Expertise/Exhibition-Research-Lab
- **Kathy Rae Huffman** (美国 / 英国, 1943–) — 美国策展人、录像与网络艺术先驱，也是早期赛博女性主义网络的推动者，自 1970 年代起追踪新媒介机器进入艺术。 代表作: Video art curator, Long Beach Museum of Art (1978–84); Face Settings (1997–2000, with Eva Wohlgemuth). https://en.wikipedia.org/wiki/Kathy_Rae_Huffman
- **Laurence Bertrand Dorléac** (巴黎，法国, 1957–) — 法国艺术史学者，与 Jérôme Neutres 共同策划巴黎大皇宫“艺术家与机器人”（2018），梳理从 Schöffer 至今的机器人与算法艺术。 代表作: Artists & Robots (Grand Palais, 2018, with Jérôme Neutres). https://en.wikipedia.org/wiki/Laurence_Bertrand_Dorl%C3%A9ac
- **Legacy Russell** (纽约，美国, 1986–) — 美国策展人与作家，《故障女性主义》把机器故障视为网络中酷儿与黑人身体的拒绝场域；现任 The Kitchen 执行总监。 代表作: Glitch Feminism: A Manifesto (2020); Black Meme (2024). https://www.legacyrussell.com
- **Maholo Uchida / 内田真帆罗** (东京，日本) — 日本国立科学未来馆（东京）策展人，曾与石黑浩合作仿人机器人展项，也是“AI：超越人类”的联合策展人。 代表作: AI: More than Human (Barbican, 2019, with Suzanne Livingston); Android exhibits at Miraikan (2014–). https://www.barbican.org.uk/whats-on/2019/event/ai-more-than-human
- **Nora N. Khan** (洛杉矶，美国, 1983–) — 美国作家与策展人，《看见、命名、认知》审视机器视觉如何命名与判断，她的评论塑造了艺术界书写 AI 的方式。 代表作: Seeing, Naming, Knowing (2019); Refiguring the Future (2019, co-curator with Lola Kramer). https://en.wikipedia.org/wiki/Nora_Khan
- **Peter Weibel / 彼得·魏贝尔** (卡尔斯鲁厄，德国, 1944–2023) — 奥地利艺术家、理论家，长期担任卡尔斯鲁厄 ZKM 艺术与媒体中心馆长，其“开放代码”等展览把算法、AI 与机器能动性置于艺术中心。 代表作: Open Codes (ZKM, 2017–19); Artistic director of ZKM Karlsruhe (1999–2023); Net_Condition (ZKM, 1999). https://en.wikipedia.org/wiki/Peter_Weibel
- **Pontus Hultén** (斯德哥尔摩，瑞典 / 巴黎，法国, 1924–2006) — 瑞典策展人、蓬皮杜中心美术馆首任馆长，他在 MoMA 策划的“机械时代末期所见的机器”梳理了计算时代开端时艺术与机器的关系。 代表作: The Machine as Seen at the End of the Mechanical Age (MoMA, 1968); Bewogen Beweging (Stedelijk, 1961). https://en.wikipedia.org/wiki/Pontus_Hult%C3%A9n
- **Sabine Himmelsbach** (巴塞尔，瑞士, 1966–) — 德国策展人，巴塞尔电子艺术之家（HEK）馆长，其“纠缠的现实：与人工智能共处”等展览关注我们如何与 AI 和机器共同生活。 代表作: Entangled Realities: Living with Artificial Intelligence (HEK, 2019); Director of HEK Basel (2012–). https://de.wikipedia.org/wiki/Sabine_Himmelsbach
- **Suzanne Livingston** (伦敦，英国) — 英国策展人与作家，与内田真帆罗共同策划巴比肯中心“AI：超越人类”（2019），这场融合艺术、科学与 AI 历史的大型展览在全球巡展。 代表作: AI: More than Human (Barbican, 2019, with Maholo Uchida). https://www.drsuzannelivingston.com/
- **Zhang Ga / 张尕** (上海 / 北京，中国) — 中国策展人，上海新时线媒体艺术中心艺术总监，他在中国美术馆策划的媒体艺术三年展把机器人、AI 与生物艺术带给中国观众。 代表作: Synthetic Times (NAMOC, 2008); Translife (NAMOC, 2011); Thingworld (NAMOC, 2014); Artistic director of Chronus Art Center. https://chronusartcenter.org/

### 工程师与机器人学家

- **Billy Klüver** (纽约，美国, 1927–2004) — 瑞典裔贝尔实验室工程师，与 Tinguely、劳申伯格与沃霍尔合作制作机器，联合创立“艺术与技术实验”（E.A.T.），成为艺术家与工程师合作的典范。 代表作: Homage to New York (1960, with Jean Tinguely); 9 Evenings: Theatre and Engineering (1966); Experiments in Art and Technology (E.A.T., founded 1967). https://en.wikipedia.org/wiki/Billy_Kl%C3%BCver
- **Blake Lemoine** (旧金山，美国) — 美国工程师，2022 年因公开声称谷歌聊天机器人 LaMDA 具有感知能力而被解雇，成为机器内在性争论的引爆点。 代表作: Is LaMDA Sentient? – an Interview (2022). https://cajundiscordian.medium.com/is-lamda-sentient-an-interview-ea64d916d917
- **Christoph Bartneck** (基督城，新西兰, 1973–) — 德国人机交互研究者，研究人们是否会迟疑关掉一台哀求的机器人、虐待机器人的行为，以及机器人是否会因颜色被种族化。 代表作: Daisy, Daisy, Give Me Your Answer Do! (2007); Godspeed questionnaires (2009); Robots and Racism (2018). https://www.bartneck.de/
- **Claude Shannon / 克劳德·香农** (剑桥，美国, 1916–2001) — 美国数学家，创立信息论，并制作了会学习走迷宫的机械老鼠 Theseus，以及只会把自己关掉的“无用机器”。 代表作: A Mathematical Theory of Communication (1948); Theseus maze-solving mouse (1950); Ultimate Machine (1952, after Marvin Minsky). https://en.wikipedia.org/wiki/Claude_Shannon
- **Cynthia Breazeal / 辛西娅·布雷齐尔** (剑桥，美国, 1967–) — 美国机器人学家，以能回应人类情绪的表情机器人头 Kismet 开创社交机器人学，之后又推出最早的家用社交机器人之一 Jibo。 代表作: Kismet (1998–2000); Designing Sociable Robots (2002); Leonardo (2003, with Stan Winston Studio); Jibo (2014–). https://www.media.mit.edu/people/cynthiab/
- **David Hanson** (香港, 1969–) — 美国机器人设计师、汉森机器人公司创始人，制作 Bina48、Sophia 等逼真人形头部；Sophia 于 2017 年获得沙特公民身份。 代表作: Philip K. Dick android (2005); Bina48 (2010, for Terasem); Sophia (2016). https://www.hansonrobotics.com/
- **Eugenia Kuyda** (旧金山，美国) — 俄罗斯出生的 Replika 创始人，Replika 起源于她用已故好友 Roman Mazurenko 的聊天记录制作的聊天机器人，后来成为数百万人使用的陪伴应用。 代表作: Roman (memorial bot of Roman Mazurenko) (2016); Replika (2017). https://replika.com/
- **Gil Weinberg** (亚特兰大，美国, 1967–) — 以色列裔美国音乐科技学者，任教于佐治亚理工学院，他的机器人音乐家 Haile 与 Shimon 会聆听并与人类乐手即兴合奏。 代表作: Haile (2006); Shimon (2009–); Robotic prosthetic drumming arm (2014). https://www.gilweinberg.com/
- **Guy Hoffman** (伊萨卡，美国) — 以色列机器人学家，借鉴表演与动画设计非人形社交机器人，从机器人台灯到柔软手工的 Blossom。 代表作: AUR robotic desk lamp (2007); Shimon (2009, with Gil Weinberg); Travis / Shimi (2010s); Blossom (2017). https://hrc2.io/
- **Hans Moravec / 汉斯·莫拉维克** (匹兹堡，美国, 1948–) — 奥地利裔加拿大机器人学家，提出“莫拉维克悖论”：对人类来说容易的事（如行走和观看），对机器来说却最难。 代表作: Stanford Cart (1979); Mind Children (1988); Moravec's paradox (1988). https://frc.ri.cmu.edu/~hpm/
- **Heather Knight** (科瓦利斯，美国) — 美国机器人学家，通过机器人表演研究魅力与社会智能，例如一台根据观众笑声调整段子的脱口秀 NAO 机器人。 代表作: Data, a stand-up comedy robot (2010); Marilyn Monrobot (company, 2010s); Robot Film Festival (2012–). https://www.charismarobotics.com/
- **Hiroshi Ishiguro / 石黑浩** (大阪，日本, 1963–) — 日本机器人学家，制造高度逼真的仿人机器人（包括他自己的复制品），以研究何为“人的存在感”；他的仿人机器人出现在剧场、博物馆与电影中。 代表作: Geminoid HI-1 (2006); Telenoid (2010); Erica (2015); Alter (2016, with Takashi Ikegami). https://eng.irl.sys.es.osaka-u.ac.jp/
- **Hod Lipson** (纽约，美国, 1967–) — 哥伦比亚大学以色列裔美国机器人学家，他的机器人会为自己的身体建模，这是对机器自我意识的实验性探索。 代表作: Resilient Machines Through Continuous Self-Modeling (2006, with Josh Bongard and Victor Zykov); Self-replicating robots (2005); Robot self-image from vision (2022). https://www.hodlipson.com/
- **Hugh Herr** (剑桥，美国, 1964–) — 美国工程师与攀岩者，双腿截肢者，领导麻省理工学院生物机电一体化小组，研发能被身体感知为“自己的”仿生肢体。 代表作: BiOM bionic ankle (2010s); Agonist-antagonist myoneural interface (2018). https://www.media.mit.edu/people/hherr/overview/
- **Ichiro Kato / 加藤一郎** (东京，日本, 1925–1994) — 早稻田大学日本工程师，研制了第一台全尺寸人形机器人 WABOT-1，以及能读谱弹奏风琴的 WABOT-2。 代表作: WABOT-1 (1973); WABOT-2 (1984). https://ja.wikipedia.org/wiki/加藤一郎_(ロボット研究者)
- **Jacques de Vaucanson / 雅克·德·沃康松** (巴黎，法国, 1709–1782) — 法国发明家（1709–1782），他的自动机（真正吹奏长笛的吹笛人、看似会进食与消化的鸭子）把身体本身变成了机器问题。 代表作: The Flute Player (1737); The Digesting Duck (1739). https://en.wikipedia.org/wiki/Jacques_de_Vaucanson
- **Joseph Engelberger** (丹伯里，美国, 1925–2015) — 美国工程师，被称为“机器人之父”，他的 Unimate 机械臂于 1961 年进入通用汽车工作，这类工业机器人后来成为艺术的材料。 代表作: Unimate (1961, General Motors); Robotics in Practice (1980); HelpMate (1980s). https://en.wikipedia.org/wiki/Joseph_Engelberger
- **Josh Bongard** (伯灵顿，美国, 1974–) — 佛蒙特大学加拿大机器人学家，与 Michael Levin 以进化算法设计出由青蛙细胞组装而成的“活机器”——异种机器人（xenobots）。 代表作: Resilient Machines Through Continuous Self-Modeling (2006); Xenobots (2020, with Michael Levin); How the Body Shapes the Way We Think (2006, with Rolf Pfeifer). https://jbongard.github.io
- **Kaname Hayashi / 林要** (东京，日本) — 日本工程师，曾主导软银 Pepper 的开发，之后创立 GROOVE X 推出 LOVOT：一台温暖、“无用”、只为被爱而设计的机器人。 代表作: Pepper (development lead, 2014); LOVOT (GROOVE X, 2019). https://lovot.life/
- **Kenneth Colby** (斯坦福，美国, 1920–2001) — 美国精神科医生，编写了模拟偏执症患者的聊天机器人 PARRY，1972 年它与 ELIZA“见面”，进行了一场机器对机器的心理治疗。 代表作: PARRY (1972); Artificial Paranoia (1975). https://en.wikipedia.org/wiki/Kenneth_Colby
- **Kerstin Dautenhahn** (滑铁卢，加拿大, 1964–) — 德国机器人学家，她的儿童大小、表情简化的机器人 KASPAR 被用于自闭症儿童，证明简化的机器人面孔能支持社交互动。 代表作: KASPAR (2005–); Socially Intelligent Agents (2002, ed.). https://researchprofiles.herts.ac.uk/portal/en/persons/kerstin-dautenhahn(0d00e4af-1f2d-433e-8d0e-ac8690288e4c).html
- **Kevin Warwick** (考文垂，英国, 1954–) — 英国工程师，1998 年在手臂植入 RFID 芯片，2002 年又植入 100 电极阵列，把自己的神经系统与机械手以及妻子的植入物相连。 代表作: Project Cyborg 1.0 (1998); Project Cyborg 2.0 (2002); I, Cyborg (2002). https://en.wikipedia.org/wiki/Kevin_Warwick
- **Maja Matarić** (洛杉矶，美国, 1965–) — 南加州大学塞尔维亚裔美国机器人学家，定义了“社会辅助机器人”：通过社交而非身体接触帮助中风康复、自闭症与老年照护中的人们。 代表作: Socially assistive robotics (2005, with David Feil-Seifer); The Robotics Primer (2007). https://en.wikipedia.org/wiki/Maja_Matari%C4%87
- **Marc Raibert** (沃尔瑟姆，美国, 1949–) — 美国机器人学家，创立波士顿动力；其腿足机器人以及它们被踢、跳舞的爆红视频，塑造了公众对机器人身体的感受。 代表作: Boston Dynamics (founded 1992); BigDog (2005); Spot (2016–); Atlas (2013–). https://en.wikipedia.org/wiki/Marc_Raibert
- **Masahiro Mori / 森政弘** (东京，日本, 1927–2025) — 日本机器人学家，1970 年提出“恐怖谷”，描述近乎人类的机器引发的不安；其《机器人中的佛陀》认为机器也具有佛性。 代表作: The Uncanny Valley (Bukimi no Tani, 1970); The Buddha in the Robot (1974); Robocon (1988–). https://en.wikipedia.org/wiki/Masahiro_Mori_(roboticist)
- **Michael Levin** (梅德福，美国, 1969–) — 美国发育生物学家，其异种机器人与人源机器人模糊了生物与机器的界限，并提出在非常规身体中识别心智的框架。 代表作: Xenobots (2020, with Josh Bongard and Sam Kriegman); Anthrobots (2023); Technological Approach to Mind Everywhere (2022). https://drmichaellevin.org/
- **Michio Okada / 冈田美智男** (丰桥，日本, 1960–) — 日本“弱机器人”研究者：这些机器无法独立完成任务，例如需要路人帮忙捡垃圾的垃圾桶机器人，把依赖变成照护的基础。 代表作: Weak Robots (Yowai Robotto, 2012); Muu (2000s); Gomi-bako robot (2010s); NICOBO (2021, with Panasonic). https://ja.wikipedia.org/wiki/岡田美智男
- **Pierre Jaquet-Droz** (拉绍德封，瑞士, 1721–1790) — 瑞士钟表匠（1721–1790），他的仿人自动机（包括可编程写出任意 40 字符文本的“书写者”）是可编程机器人的先祖。 代表作: The Writer (1768–74); The Draughtsman (1768–74); The Musician (1768–74). https://www.jaquet-droz.com/fr/the-extraordinary-history-jaquet-droz
- **Radhika Nagpal** (普林斯顿，美国) — 印度裔美国机器人学家，她的千台 Kilobot 群体与仿白蚁建造机器人显示，集体行为可以从简单机器中涌现。 代表作: Kilobot swarm of 1,024 robots (2014); TERMES termite-inspired builders (2014); Blueswarm (2021). https://en.wikipedia.org/wiki/Radhika_Nagpal
- **Raffaello D'Andrea** (苏黎世，瑞士, 1967–) — 加拿大–意大利–瑞士工程师，共同创作会选择一位观众并跟随的机器人桌子 The Table，联合创立 Kiva Systems（今亚马逊机器人），并为无人机编舞。 代表作: The Table (2001, with Max Dean); Kiva Systems warehouse robots (2003); Flying Machine Arena (2008); Sparked (Cirque du Soleil, 2014). http://raffaello.name/
- **Rebecca Fiebrink** (伦敦，英国) — 英国艺术大学创意计算研究所美国研究者，Wekinator 让艺术家通过示范训练机器学习模型，把机器学习当作具身的创作乐器。 代表作: Wekinator (2009); Machine Learning for Musicians and Artists (Kadenze, 2016). https://www.doc.gold.ac.uk/~mas01rf/
- **Rodney Brooks / 罗德尼·布鲁克斯** (波士顿，美国, 1954–) — 澳大利亚机器人学家，他的基于行为的机器人学以分层的具身反射取代中央规划，从六足机器人 Genghis 到扫地机器人 Roomba。 代表作: Elephants Don't Play Chess (1990); Genghis (1989); Cog (1993–); Roomba (iRobot, 2002). https://rodneybrooks.com/
- **Rolf Pfeifer** (苏黎世，瑞士, 1947–) — 瑞士 AI 研究者，倡导具身智能，指出机器人的身体与材料本身承担了部分“思考”（形态计算）。 代表作: Understanding Intelligence (1999, with Christian Scheier); How the Body Shapes the Way We Think (2006, with Josh Bongard); ECCE / Roboy (2010s). https://en.wikipedia.org/wiki/Rolf_Pfeifer
- **Steve Mann** (多伦多，加拿大, 1962–) — 加拿大工程师，自 1970 年代末起一直佩戴可穿戴计算机与头戴摄像机生活，并提出“逆向监视”：自下而上地监视监视者。 代表作: WearComp / EyeTap (late 1970s–); Sousveillance (2002). http://wearcam.org/
- **Susumu Tachi / 馆暲** (东京，日本, 1946–) — 日本工程师，1980 年提出“远程存在”，研制 TELESAR 系列机器人，让人通过远端机器人身体去看、听与感受。 代表作: Telexistence (1980); TELESAR series (1980s–); Optical camouflage (2003). https://tachilab.org/en/
- **Takanori Shibata / 柴田崇德** (筑波，日本, 1967–) — 日本产业技术综合研究所工程师，研发了用于全球失智症照护的竖琴海豹宝宝机器人 PARO，是机器照护争论的核心案例。 代表作: PARO therapeutic seal robot (research from 1993; released 2004). https://ja.wikipedia.org/wiki/柴田崇徳
- **Takashi Ikegami / 池上高志** (东京，日本, 1961–) — 东京大学日本人工生命科学家，致力于让机器具有自发、自组织的行为；他的仿人机器人 Alter 由神经网络与中枢模式发生器驱动。 代表作: Mind Time Machine (YCAM, 2010); Alter (2016, with Hiroshi Ishiguro); Alter 3 in Scary Beauty (2018). https://en.wikipedia.org/wiki/Takashi_Ikegami
- **Tomotaka Takahashi / 高桥智隆** (京都，日本, 1975–) — 日本机器人创作者，其小型人形机器人包括首个进入太空的会说话的陪伴机器人 Kirobo，以及同时是一部手机的机器人 RoBoHoN。 代表作: Kirobo (2013, on the ISS); Robi (2013); RoBoHoN (2016). https://en.wikipedia.org/wiki/Tomotaka_Takahashi
- **W. Grey Walter** (布里斯托，英国, 1910–1977) — 美国出生的英国神经生理学家，他的趋光机器龟 Elmer 与 Elsie 仅凭两个“神经元”就表现出栩栩如生、难以预测的行为，是最早的自主机器人。 代表作: Machina speculatrix tortoises Elmer and Elsie (1948–49); The Living Brain (1953). https://en.wikipedia.org/wiki/William_Grey_Walter
- **Wang Xingxing / 王兴兴** (杭州，中国, 1990–) — 中国工程师、宇树科技创始人，其四足与人形机器人在 2025 年央视春晚上手持手绢扭秧歌，成为中国公众机器人形象的标志性时刻。 代表作: Unitree Robotics (founded 2016); Unitree H1 humanoids at the CCTV Spring Festival Gala (2025). https://www.unitree.com/
- **Wendy Ju** (纽约，美国) — 康奈尔科技校区美国交互研究者，Ghost Driver 让司机藏在座椅造型的伪装中，研究行人如何对“无人驾驶”汽车作出反应。 代表作: Ghost Driver (2015); The Design of Implicit Interactions (2015). http://www.wendyju.com/

### 美术馆与艺术中心

- **Aksioma – Institute for Contemporary Art** (卢布尔雅那，斯洛文尼亚) — 卢布尔雅那的非营利机构，制作并出版关于网络、算法与权力的批判性艺术，包括 PostScriptUM 出版系列。 https://aksioma.org/
- **Ars Electronica Center / 林茨电子艺术中心** (林茨，奥地利) — 电子艺术节的“未来博物馆”。常设展《Understanding AI》（2019 年起）展示机器如何感知与分类，展出《Anatomy of an AI System》《Gender Shades》等作品。 https://ars.electronica.art/center/en/
- **Art Center Nabi / Nabi 艺术中心** (首尔，韩国) — 韩国第一家数字艺术中心，由 SK 集团创办。二十多年来持续推出机器人艺术、AI 与创意技术项目以及黑客马拉松。 http://www.nabi.or.kr/
- **Barbican Centre / 巴比肯艺术中心** (伦敦，英国) — 伦敦的综合艺术中心。其展览《AI: More than Human》（2019）成为 AI 主题展的范本，从“人造生命之梦”一路讲到心智机器与数据世界。 https://www.barbican.org.uk/
- **Carnegie Museum of Art (Hillman Photography Initiative) / 卡内基艺术博物馆** (匹兹堡，美国) — 匹兹堡的艺术博物馆。其 Hillman 摄影计划推出《Mirror with a Memory》（2020–21），探讨 AI、摄影、监控与偏见，包括 Trevor Paglen 的《Opposing Geometries》。 https://carnegieart.org/
- **Centre Pompidou / 蓬皮杜艺术中心** (巴黎，法国) — 法国国家现代艺术中心。其 Mutations/Créations 系列举办了《Neurones, les intelligences simulées》（2020），跨越艺术、设计与科学梳理神经网络与模拟智能的历史。 https://www.centrepompidou.fr/en/
- **Chronus Art Center / 新时线媒体艺术中心** (上海，中国) — 上海首家专注媒体艺术的非营利艺术中心，设有展览、研究与实验室。它是中国展出机器、算法与动态作品的主要机构之一，也曾承接 ZKM《Open Codes》的中国巡展。 https://www.chronusartcenter.org/
- **Computer History Museum / 计算机历史博物馆** (山景城，美国) — 位于硅谷的计算机历史博物馆与档案馆。其收藏与展览《Revolution》包括 Shakey 机器人等 AI 与机器人里程碑，并收录工程师口述史。 https://computerhistory.org/
- **de Young Museum (FAMSF) / 笛洋美术馆** (旧金山，美国) — 旧金山美术馆，曾举办《Uncanny Valley: Being Human in the Age of AI》（2020），把“恐怖谷”解读为 AI 承诺与其在数据、劳动和偏见上实际后果之间的政治落差。 https://www.famsf.org/visit/de-young
- **FACT Liverpool / 利物浦艺术与创意技术基金会** (利物浦，英国) — 英国重要的艺术与创意技术中心（Foundation for Art and Creative Technology），委托并展出关于数据、监控与 AI 的作品，常与社区共同制作。 https://www.fact.co.uk/
- **Fondazione Prada / 普拉达基金会** (米兰，意大利) — 米兰的艺术基金会。其 Osservatorio 空间举办了 Kate Crawford 与 Trevor Paglen 策划的《Training Humans》（2019），这是首个以“教机器看人”的训练图像为主题的大型展览。 https://en.wikipedia.org/wiki/Fondazione_Prada
- **Furtherfield** (伦敦，英国) — 伦敦历史最悠久的艺术与技术机构，在芬斯伯里公园设有画廊与实验室，举办关于 AI、数据、区块链与超越人类未来的批判性展览和游戏。 https://www.furtherfield.org/
- **Haus der Kulturen der Welt (HKW) / 世界文化之家** (柏林，德国) — 柏林的当代艺术与思想中心。长期项目如《Technosphere》（2015–19）探讨计算、基础设施与行星尺度的技术。 https://www.hkw.de/en
- **HEK (House of Electronic Arts) Basel / 巴塞尔电子艺术之家** (巴塞尔，瑞士) — 瑞士的数字文化与新艺术形式中心。2019 年的展览《Entangled Realities: Living with Artificial Intelligence》汇集了 LAUREN、被“复活”的 Tay 以及 Autonomous Trap 001 等作品。 https://www.hek.ch/en/
- **iMAL** (布鲁塞尔，比利时) — 布鲁塞尔的数字文化与技术中心，设有展览空间和 fablab，展示并制作关于算法、感知与自动化的作品。 https://www.imal.org/en
- **Jeu de Paume / 网球场国家美术馆** (巴黎，法国) — 巴黎的摄影与图像艺术中心。展览《The World Through AI》（2025）将 AI 分为分析型与生成型两类，并把艺术作品与机器视觉史的“时间胶囊”并置。 https://jeudepaume.org/en/
- **KADIST** (巴黎，法国 / 旧金山，美国) — 在全球收藏和委托作品的非营利当代艺术机构。展览《Apophenia, Interruptions：工作中的艺术家与人工智能》（2024）关注模式识别与误认。 https://kadist.org/
- **Kapelica Gallery / Kersnikova Institute** (卢布尔雅那，斯洛文尼亚) — 卢布尔雅那的“探究型”艺术画廊，关注机器人、生物艺术与身体–机器表演（Stelarc、Špela Petrič 等），Kersnikova 研究所还运营 RAMPA 与 BioTehna 实验室。 https://kersnikova.org/
- **LABoral Centro de Arte y Creación Industrial / LABoral 艺术与工业创造中心** (希洪，西班牙) — 位于西班牙希洪、由昔日劳工大学改建的艺术中心，聚焦艺术、科学、技术与工业创造，其展览与制作实验室关注自动化、劳动与机器。 https://www.laboralcentrodearte.org/
- **LAS Art Foundation** (柏林，德国) — 柏林的艺术基金会，委托位于艺术、科学与技术交界处的大型作品，如 Lawrence Lek 的《NOX》（2023），一个为有感知的自动驾驶汽车设立的康复中心。 https://www.las-art.foundation/
- **MAK – Museum of Applied Arts, Vienna / 维也纳应用艺术博物馆** (维也纳，奥地利) — 维也纳的设计博物馆，维也纳变革双年展的主办方。它参与制作《Hello, Robot》（2017），并举办《Uncanny Values: Artificial Intelligence & You》（2019），将设计与批判性 AI 联系起来。 https://www.mak.at/en
- **Miraikan – National Museum of Emerging Science and Innovation / 日本科学未来馆** (东京，日本) — 东京的科学博物馆，公众在此与人形和仿真机器人相遇，从 ASIMO 演示到石黑浩的仿真人 Otonaroid 与 Kodomoroid（2014）。 https://www.miraikan.jst.go.jp/en/
- **Mori Art Museum / 森美术馆** (东京，日本) — 位于六本木新城的当代美术馆。展览《未来与艺术：AI、机器人、城市、生命》（2019–20）以 100 多个项目探讨人类将如何与机器共同生活。 https://www.mori.art.museum/en/
- **Nam June Paik Art Center / 白南准艺术中心** (龙仁，韩国) — 白南准的美术馆与档案馆。白南准的《Robot K-456》（1964）是最早的表演机器人之一，艺术中心展出并研究延续他对机器、广播与身体探索的媒体艺术。 https://en.wikipedia.org/wiki/Nam_June_Paik_Art_Center
- **NTT InterCommunication Center [ICC] / NTT 互动交流中心** (东京，日本) — 由 NTT 东日本运营的东京媒体艺术中心，关注通信技术与艺术的关系。其展览与档案是日本机器、传感与互动艺术的重要参照。 https://www.ntticc.or.jp/en/
- **Onassis Stegi / 奥纳西斯文化中心** (雅典，希腊) — 奥纳西斯基金会在雅典的文化中心，数字文化项目活跃。展览《You and AI: Through the Algorithmic Lens》（2021）探讨 AI 如何观看和分类人。 https://www.onassis.org/
- **Science Gallery / 科学画廊** (都柏林 / 伦敦 / 班加罗尔 / 墨尔本) — 以大学为依托、面向年轻观众的艺术与科学画廊网络。其 AI 系列展从都柏林早期展览到伦敦的《AI: Who's Looking After Me?》（2023），主题从自动化转向偏见，再到照护。 https://sciencegallery.org/
- **Science Museum, London / 伦敦科学博物馆** (伦敦，英国) — 英国国家科学博物馆。展览《Robots》（2017）展出跨越 500 年的 100 多台机器人，从机械自动人偶到人形机器人，是机器人大众史的重要参照。 https://en.wikipedia.org/wiki/Science_Museum,_London
- **Serpentine Arts Technologies / 蛇形画廊艺术与技术部** (伦敦，英国) — 蛇形画廊面向 AI、区块链和游戏引擎艺术的项目，委托了 Holly Herndon 与 Mat Dryhurst 的《The Call》（2024）等作品。它与伦敦国王学院共同运营 Creative AI Lab，并发布《Future Art Ecosystems》系列报告。 https://www.serpentinegalleries.org/arts-technologies/
- **Society for Arts and Technology (SAT) / 蒙特利尔艺术与技术协会** (蒙特利尔，加拿大) — 蒙特利尔的沉浸式与数字艺术中心，设有球幕、研究实验室与驻留项目，开发供艺术家使用的远程临场与沉浸式工具。 https://sat.qc.ca/en/
- **Taikang Art Museum / 泰康美术馆** (北京，中国) — 泰康收藏体系下的北京美术馆。展览《Creative Machine 跨越六十年：人工智能的创意之火》（2024–25）梳理了六十年的机器创造，从早期计算机艺术到 Patrick Tresset 的绘画机器人《Human Study #1》。 https://tam.taikang.com/
- **Taiwan Contemporary Culture Lab (C-LAB) / 台湾当代文化实验场** (台北，台湾) — 位于台北原空军基地的文化实验场，设有科技艺术中心、声音实验室和未来媒体艺术节，是台湾 AI 与机器艺术的重要场所。 https://clab.org.tw/en/
- **Tate Modern / 泰特现代美术馆** (伦敦，英国) — 英国国家现代艺术馆。《Electric Dreams：互联网之前的艺术与技术》（2024–25）梳理了机器艺术在互联网之前的谱系，Anicka Yi 的现代汽车委托项目（2021）则让漂浮的“机器生物”充满涡轮大厅。 https://www.tate.org.uk/visit/tate-modern
- **UCCA Center for Contemporary Art / UCCA 尤伦斯当代艺术中心** (北京，中国) — 中国重要的当代艺术机构，在北京、北戴河和上海设有场馆。它举办过关注数字身体与自动化的艺术家大展，如《曹斐：时代舞台》（2021）。 https://ucca.org.cn/en/
- **V&A – Victoria and Albert Museum (Digital Art) / 维多利亚与阿尔伯特博物馆** (伦敦，英国) — 伦敦的设计博物馆，收藏英国国家级的计算机与数字艺术藏品，从 1960 年代绘图仪作品到其收藏的《Anatomy of an AI System》。 https://www.vam.ac.uk/
- **V2_ Lab for the Unstable Media / V2_ 不稳定媒体实验室** (鹿特丹，荷兰) — 跨学科的艺术与媒体技术中心，曾主办荷兰电子艺术节（DEAF）。其实验室、出版物和在线档案记录了数十年关于身体、传感器与机器的创作。 https://v2.nl/
- **Vancouver Art Gallery / 温哥华美术馆** (温哥华，加拿大) — 加拿大美术馆。展览《The Imitation Game: 人工智能时代的视觉文化》（2022）从自动人偶到机器视觉，梳理 AI 在视觉文化中的历史。 https://www.vanartgallery.bc.ca/
- **Vitra Design Museum / 维特拉设计博物馆** (莱茵河畔魏尔，德国) — 德国设计博物馆。巡回展《Hello, Robot. 人与机器之间的设计》（2017）按文化、工作、家庭和身体组织机器人，成为设计与机器议题的重要参照。 https://www.design-museum.de/en/
- **Whitney Museum of American Art (artport) / 惠特尼美国艺术博物馆** (纽约，美国) — 纽约的美国艺术博物馆，其网络平台 artport（2001 年起）委托网络与软件艺术。2024 年展览《Harold Cohen: AARON》首次让绘画程序 AARON 在展厅现场作画。 https://whitney.org/
- **Yamaguchi Center for Arts and Media [YCAM] / 山口情报艺术中心** (山口，日本) — 日本的媒体艺术中心，其内部研发团队 YCAM InterLab 与艺术家共同开发关于舞蹈、感知与机器的作品，并开源发布工具与研究成果。 https://www.ycam.jp/en/
- **ZKM | Center for Art and Media Karlsruhe / ZKM 卡尔斯鲁厄艺术与媒体中心** (卡尔斯鲁厄，德国) — 欧洲最大的媒体艺术美术馆，收藏从早期计算机艺术延伸到 AI。《Open Codes》（2017）与《BioMedia》（2021）等展览讨论了机器学习、算法治理和“类生命”的媒体系统。 https://zkm.de/en

### 艺术节与展览系列

- **ACM Creativity & Cognition / ACM 创造力与认知会议** (巡回举办) — 由 Ernest Edmonds 于 1993 年创办的 ACM 人类创造力与计算会议，设有论文、图像论文与艺术展，关注与机器共创。 https://cc.acm.org/
- **ACM/IEEE International Conference on Human-Robot Interaction (HRI) / 人机交互国际会议（HRI）** (巡回举办) — 人机交互领域最主要的学术会议，关于信任、拟人化与“欺负机器人”的研究是理解人们如何解读机器身体的核心依据。 https://humanrobotinteraction.org/
- **Ars Electronica Festival / 林茨电子艺术节** (林茨，奥地利) — 全球历史最悠久的艺术、技术与社会节。《Artificial Intelligence – The Other I》（2017，含“人工亲密”单元）等届次为机器艺术设定了议题。 https://ars.electronica.art/festival/en/
- **Art & Science International Exhibition and Symposium (Tsinghua) / 艺术与科学国际作品展暨学术研讨会** (北京，中国) — 2001 年由物理学家李政道与画家吴冠中在清华大学发起的系列展览与研讨会，现由清华大学艺术博物馆举办，是中国最主要的艺术与科学系列活动。 https://www.artmuseum.tsinghua.edu.cn/
- **Beijing Media Art Biennale / 北京媒体艺术双年展** (北京，中国) — 由中央美术学院美术馆主办的双年展。首届《技术伦理》（2016）与第二届《后生命》（2018）是中文语境下机器艺术的重要框架。 https://en.wikipedia.org/wiki/CAFA_Art_Museum
- **CVPR AI Art Gallery / CVPR AI 艺术画廊** (巡回举办) — 计算机视觉会议 CVPR 的线上与现场画廊，展出使用或质疑计算机视觉的艺术作品，档案保存了历年入选作品。 https://thecvf-art.com/
- **Elektra / International Digital Art Biennial (BIAN)** (蒙特利尔，加拿大) — 蒙特利尔的数字艺术节与双年展，常展出机器人与机器装置；BIAN 双年展包括以机器人为主题的《Automata》（2016）。 https://elektramontreal.ca/
- **EVA London – Electronic Visualisation and the Arts** (伦敦，英国) — 伦敦年度电子可视化与艺术会议，与 BCS 计算机艺术学会合办，议题从早期计算机艺术史延伸到 AI。 https://www.eva-london.org/
- **FILE – Electronic Language International Festival** (圣保罗，巴西) — 拉丁美洲最大的电子艺术节，在圣保罗举办，展出机器人、互动与 AI 艺术，并拥有丰富的在线档案。 https://file.org.br/
- **Impakt** (乌得勒支，荷兰) — 乌得勒支的批判性媒体文化机构，举办年度艺术节、驻留和媒体文化中心，主题常涉及算法、监控与机器感知。 https://impakt.nl/
- **International Conference on Computational Creativity (ICCC) / 国际计算创造力会议** (巡回举办) — 计算创造力协会的年度会议，研究机器能否以及如何具有创造力，从创作系统到评估方法。 https://computationalcreativity.net/
- **ISEA International (International Symposium on Electronic Art) / 国际电子艺术研讨会** (巡回举办) — 电子艺术领域最主要的学术研讨会与展览，自 1988 年起每年在不同城市举办，在线档案收录了数十年关于机器人艺术、人工生命与 AI 的论文。 https://isea-international.org/
- **Japan Media Arts Festival / 日本文化厅媒体艺术节** (东京，日本) — 日本文化厅主办的艺术节与奖项（1997–2022），涵盖艺术、娱乐、动画与漫画。Sony 的 aibo 与机器人歌剧《Pendulum Choir》都曾获奖。 https://j-mediaarts.jp/en/
- **KIKK Festival** (那慕尔，比利时) — 比利时那慕尔的国际数字与创意文化节，邀请从事 AI、机器人与推测未来的设计师与艺术家进行讲座和装置展示。 https://www.kikk.be/
- **Microwave International New Media Arts Festival / 微波国际新媒体艺术节** (香港) — 香港历史悠久的新媒体艺术节，以主题展和论坛呈现包括亚洲机器与 AI 艺术在内的作品。 https://www.microwavefest.net/
- **NeurIPS Creative AI Track / NeurIPS 创意 AI 单元** (巡回举办) — 机器学习顶会 NeurIPS 的评审制创意 AI 单元，承接 2017–22 年的“机器学习与创意设计”研讨会，面向与 AI 相关的艺术与设计作品，让艺术家与机器学习研究者同场对话。 https://neurips.cc/
- **NIME – New Interfaces for Musical Expression** (巡回举办) — 关于新型乐器与界面的国际会议，涵盖机器人乐器、AI 共演者与机器聆听。 https://www.nime.org/
- **SIGGRAPH Art Gallery & Art Papers / SIGGRAPH 艺术画廊** (巡回（北美 / 亚洲）) — 计算机图形学会议 ACM SIGGRAPH 及 SIGGRAPH Asia 的艺术单元，数十年来将计算、机器人与 AI 艺术与支撑它们的研究并置展出。 https://en.wikipedia.org/wiki/SIGGRAPH
- **STRP Festival** (埃因霍温，荷兰) — 在埃因霍温飞利浦旧工业区举办的创意技术节，历届探讨如何与机器人、AI 和感知环境共处。 https://strp.nl/
- **Sónar+D** (巴塞罗那，西班牙) — Sónar 音乐节的创意与技术大会，举办关于音乐 AI、合成声音与人机表演的讲座和展示。 https://sonar.es/en
- **transmediale / 柏林跨媒体艺术节** (柏林，德国) — 柏林的艺术与数字文化节，以批判而非颂扬技术的主题著称（2015《Capture All》、2018《face value》、2021–22《for refusal》），并联合出版 APRJA 期刊。 https://transmediale.de/
- **WRO Media Art Biennale / WRO 媒体艺术双年展** (弗罗茨瓦夫，波兰) — 中欧历史最久的媒体艺术双年展，由弗罗茨瓦夫 WRO 艺术中心主办，展出声音、机器与网络媒体作品。 https://wrocenter.pl/en/
- **xCoAx – Computation, Communication, Aesthetics & X** (巡回（欧洲）) — 关于计算、传播与美学的会议与展览，收录关于算法、生成系统与计算本质的论文与作品。 https://xcoax.org/

### 奖项

- **Human AI Art Award / 人类 AI 艺术奖** (波恩，德国) — 德国电信艺术收藏与波恩艺术博物馆设立的年度奖，表彰反思 AI 的艺术：Lauren Lee McCarthy 的《LAUREN》（2024）与 Nicolas Gourault 的《Unknown Label》（2025）。 https://www.art-collection-telekom.com/en/
- **LG Guggenheim Award / LG 古根海姆奖** (纽约，美国) — LG 古根海姆艺术与技术计划设立的 10 万美元技术艺术奖。获奖者：Stephanie Dinkins（2023）、郑淑丽（2024）、Ayoung Kim（2025）与 Trevor Paglen（2026）。 https://en.wikipedia.org/wiki/LG_Guggenheim_Award
- **Lumen Prize / Lumen 数字艺术奖** (伦敦，英国) — 面向技术艺术的国际奖项，2018 年起设 AI 奖（如光敏机器人群落《Lichtsuchende》）。获奖作品多为生成式，需逐一甄选。 https://www.lumenprize.com/
- **Mozilla Creative Media Awards / Mozilla 创意媒体奖** (全球) — Mozilla 基金会资助的艺术、游戏与媒体项目，让公众切身感受 AI 的危害，尤其是偏见、监控与平台权力。 https://foundation.mozilla.org/en/what-we-fund/awards/creative-media-awards/
- **Prix Ars Electronica / 电子艺术大奖** (林茨，奥地利) — 媒体艺术最重要的奖项。其“人工生命与智能”类别表彰关于 AI 与生命科学对人之意义的作品，金尼卡奖得主包括 Paul Vanouse 的《Labor》（2019）与法证建筑的《Cloud Studies》（2021）。 https://ars.electronica.art/prix/en/
- **RobotArt Competition / 机器人艺术竞赛** (美国 / 线上) — 年度机器人绘画竞赛（2016–18），参赛机器人用真实画笔作画，汇集大学与艺术家团队，让机器人绘画作为一门手艺被看见。 https://robotart.org/
- **S+T+ARTS Prize / S+T+ARTS 奖** (林茨，奥地利 / 欧盟) — 欧盟委员会设立、由电子艺术节运营的科学、技术与艺术交叉创新奖。获奖作品包括《Project Alias》（2019）、《Holly+》（2022）、《Calculating Empires》（2024）与《AI War Cloud Database》（2025）。 https://ars.electronica.art/starts-prize/en/
- **VIDA – Art & Artificial Life International Awards / VIDA 艺术与人工生命国际奖** (马德里，西班牙) — 西班牙电信基金会设立的奖项（1999–约 2015），唯一专门面向艺术与人工生命的奖：会出汗的机器人、行走的桌子、自主抗议体与虚拟生态。 https://www.fundaciontelefonica.com/

### 实验室与研究中心

- **Abundant Intelligences** (蒙特利尔，加拿大 / 全球) — 以康考迪亚大学为基地、由原住民主导的研究项目，从原住民知识体系出发构想、设计与建造 AI。 https://abundant-intelligences.net/
- **Ada Lovelace Institute / 艾达·洛芙莱斯研究所** (伦敦，英国) — 纳菲尔德基金会下的独立研究机构，致力于让数据与 AI 服务于人与社会，开展关于生物识别与人脸识别的公众态度研究。 https://www.adalovelaceinstitute.org/
- **AI Now Institute / AI Now 研究所** (纽约，美国) — 由 Kate Crawford 与 Meredith Whittaker 共同创立的政策研究机构，研究 AI 的社会后果，其关于偏见、劳动与行业权力集中的报告塑造了批判性 AI 话语。 https://ainowinstitute.org/
- **Antikythera** (洛杉矶，美国 / 全球) — 由 Benjamin Bratton 主持、在博古睿研究院孵化的计算推测哲学智库，通过工作坊、出版与影片研究行星尺度计算与合成智能。 https://antikythera.org/
- **ANU School of Cybernetics / 澳大利亚国立大学控制论学院** (堪培拉，澳大利亚) — 由人类学家 Genevieve Bell 基于 3A 研究所创办的学院，旨在复兴控制论，用于构建、驾驭与批判 AI 驱动的系统。 https://cybernetics.anu.edu.au/
- **Ars Electronica Futurelab / 电子艺术未来实验室** (林茨，奥地利) — 电子艺术节的研发工作室，与企业和大学合作研究无人机群、机器人与人机协作，并以艺术形式呈现成果。 https://ars.electronica.art/futurelab/en/
- **Artists + Machine Intelligence (Google AMI) / 谷歌艺术家与机器智能计划** (山景城 / 全球) — 谷歌将艺术家与机器智能研究者配对的项目，支持了 DeepDream 时代的早期艺术以及 K Allado-McDowell 的《Pharmako-AI》等作品。 https://ami.withgoogle.com/
- **Creative AI Lab / 创意 AI 实验室** (伦敦，英国) — 蛇形画廊艺术与技术部与伦敦国王学院数字人文系的合作项目，研究 AI 作为艺术媒介，并维护面向艺术家的工具与资源数据库。 https://creative-ai.org/
- **Creative Machines Lab (Columbia University) / 哥伦比亚大学创意机器实验室** (纽约，美国) — Hod Lipson 的机器人实验室，以能学习自身身体图式的自建模机器人、会画画的机器人和设计机器的机器闻名。 https://www.creativemachineslab.com/
- **Data & Society / 数据与社会研究所** (纽约，美国) — 由 danah boyd 创立的独立研究机构，研究数据驱动与自动化技术的社会影响，从平台劳动到算法问责。 https://datasociety.net/
- **Distributed AI Research Institute (DAIR) / 分布式 AI 研究所** (分布式) — Timnit Gebru 在被谷歌解雇后创立的独立 AI 研究机构，扎根社区，以包括数据劳工在内的受 AI 伤害者为中心。 https://www.dair-institute.org/
- **Forensic Architecture / 法证建筑** (伦敦，英国) — 设于伦敦大学金史密斯学院的研究机构，以空间、媒体与机器视觉分析调查国家与企业暴力；它用合成数据训练分类器，并以《Cloud Studies》获 2021 年金尼卡奖。 https://forensic-architecture.org/
- **Gramazio Kohler Research (ETH Zurich)** (苏黎世，瑞士) — 苏黎世联邦理工学院建筑与数字建造教席，让工业机器人砌墙、建造结构，使机器人建造成为设计议题。 https://gramaziokohler.arch.ethz.ch/
- **Hiroshi Ishiguro Laboratories (ATR / Osaka University) / 石黑浩实验室** (京都 / 大阪，日本) — 石黑浩的仿真人实验室，制作了 Geminoid 系列复制人、Erica，并与高台寺合作打造仿真观音 Mindar，是“存在感”与恐怖谷问题的主要试验场。 http://www.geminoid.jp/en/
- **Humanoid Robotics Institute (Waseda University) / 早稻田大学人形机器人研究所** (东京，日本) — 延续加藤一郎研究室的研究所，其前身制造了第一台全尺寸人形机器人 WABOT-1（1973），后来又开发了会表达情绪、会吹长笛的人形机器人。 https://www.humanoid.waseda.ac.jp/
- **Ikegami Lab (University of Tokyo) / 池上高志实验室** (东京，日本) — 池上高志的人工生命实验室，与石黑浩团队合作开发仿真人 Alter，探索神经网络能否产生自发的类生命运动。 https://en.wikipedia.org/wiki/Takashi_Ikegami
- **Institute of Network Cultures / 网络文化研究所** (阿姆斯特丹，荷兰) — 由 Geert Lovink 在阿姆斯特丹应用科技大学创办的研究中心，出版关于平台、互联网批判与 AI 的开放获取书籍与读本。 https://networkcultures.org/
- **Intelligent Instruments Lab / 智能乐器实验室** (雷克雅未克，冰岛) — 冰岛大学的 ERC 资助实验室，研究以 AI 为创作伙伴的乐器；曾获电子艺术大奖 AI in ART 类荣誉奖。 https://iil.is/
- **IRCAM / 法国声学与音乐研究协调所** (巴黎，法国) — 由皮埃尔·布列兹在蓬皮杜中心创办的音乐与声学研究所，其机器聆听、声音合成与 AI 共同即兴（OMax、Somax）研究塑造了人机音乐。 https://www.ircam.fr/
- **KIM – AI and Media Philosophy (HfG Karlsruhe) / 卡尔斯鲁厄设计学院 AI 与媒体哲学研究组** (卡尔斯鲁厄，德国) — 卡尔斯鲁厄设计学院的人工智能与媒体哲学研究组，以 AI 社会史研究和《Nooscope》图谱闻名。 https://kim.hfg-karlsruhe.de/
- **Knowing Machines** (全球) — 研究机器学习系统如何被训练去解释世界的历史、实践与政治，包括对 LAION-5B 数据集的视觉调查《Models All the Way Down》。 https://knowingmachines.org/
- **LACMA Art + Technology Lab / 洛杉矶郡艺术博物馆艺术与技术实验室** (洛杉矶，美国) — 延续洛杉矶郡艺术博物馆 1967–71 年“艺术与技术”项目的资助与驻留计划，让艺术家与科技公司合作开展 AI、机器人与感知相关项目。 https://www.lacma.org/lab
- **Leverhulme Centre for the Future of Intelligence / 剑桥大学利弗休姆未来智能中心** (剑桥，英国) — 剑桥大学研究 AI 长期影响的中心。其“AI 叙事”与“全球 AI 叙事”项目研究故事如何塑造我们对机器的期待，也研究了哀悼机器人与“数字来世”的伦理。 https://www.lcfi.ac.uk/
- **metaLAB (at) Harvard / 哈佛 metaLAB** (剑桥（马萨诸塞州），美国) — 哈佛大学伯克曼·克莱因中心的创意研究团队，项目包括 AI Pedagogy Project 以及关于机器分类与道德决策的艺术作品。 https://metalab.harvard.edu/
- **MIT Center for Advanced Visual Studies (CAVS) / MIT 高级视觉研究中心** (剑桥（马萨诸塞州），美国) — György Kepes 在 MIT 创立的研究中心（1967–2009），艺术家与工程师在此合作光、动态与控制论艺术，是后来艺术与技术实验室的范本。 https://en.wikipedia.org/wiki/Center_for_Advanced_Visual_Studies
- **MIT Media Lab – Affective Computing Group / MIT 媒体实验室情感计算组** (剑桥（马萨诸塞州），美国) — Rosalind Picard 领导的研究组，开创了“情感计算”：能感知并回应情绪的机器。其研究既支撑照护技术，也是艺术家批判的情绪识别技术的源头。 https://www.media.mit.edu/groups/affective-computing/overview/
- **MIT Media Lab – Personal Robots Group / MIT 媒体实验室个人机器人组** (剑桥（马萨诸塞州），美国) — Cynthia Breazeal 领导的研究组，源于她 1990 年代的社交机器人 Kismet，后来开发了 Leonardo 与社交机器人 Jibo，是陪伴、教学与照护型机器人设计的标杆实验室。 https://www.media.mit.edu/groups/personal-robots/overview/
- **Mixed Reality Laboratory (University of Nottingham) / 诺丁汉大学混合现实实验室** (诺丁汉，英国) — 与 Blast Theory 长期合作的人机交互实验室。其《Cat Royale》（2023）让机械臂与三只猫共处十二天，检验机器人照料动物的伦理。 https://www.nottingham.ac.uk/research/groups/mixedrealitylab/
- **Ory Laboratory / Ory 研究所** (东京，日本) — 吉藤健太朗创办的公司，开发了分身机器人 OriHime 与“分身机器人咖啡馆 DAWN”，让渐冻症等残障人士通过机器人担任服务员。 https://orylab.com/en/
- **Reality Design Lab / 现实设计实验室** — 由胡博涛（Botao Amber Hu）领导的设计研究实验室，创作关于他者心智与机器的混合现实与推测性作品，如《EchoVision》（做一只蝙蝠是什么感觉？）、《City of Sparkles》（AI 会如何感知我们的城市？）与《AI Mom™》；实验室还开发开源 HoloKit 工具包，并运营 Machinic Reality Inspire 图库。 https://reality.design/
- **Robotic Musicianship Group (Georgia Tech) / 佐治亚理工机器人音乐组** (亚特兰大，美国) — 佐治亚理工音乐技术中心 Gil Weinberg 领导的研究组，开发了会即兴演奏的马林巴机器人 Shimon，一台与人一同聆听和演奏的机器。 https://en.wikipedia.org/wiki/Gil_Weinberg
- **SHARE Lab / SHARE Foundation** (诺维萨德，塞尔维亚) — SHARE 基金会下由 Vladan Joler 领导的研究与数据调查实验室，绘制网络与 AI 不可见的基础设施地图，《Anatomy of an AI System》的地图工作即源于此。 https://en.wikipedia.org/wiki/SHARE_Foundation
- **STUDIO for Creative Inquiry (CMU) / 卡内基梅隆大学创意探究工作室** (匹兹堡，美国) — 卡内基梅隆大学的跨学科艺术研究实验室，由 Golan Levin 主持，驻留与项目涉及计算机视觉、机器人与创意编程。 https://studioforcreativeinquiry.org/
- **UAL Creative Computing Institute / 伦敦艺术大学创意计算研究所** (伦敦，英国) — 伦敦艺术大学的创意计算研究与教学机构，涵盖面向艺术家的交互式机器学习（Wekinator）与批判性 AI 实践。 https://www.arts.ac.uk/creative-computing-institute
- **UCLA Art|Sci Center / UCLA 艺术|科学中心** (洛杉矶，美国) — UCLA 由 Victoria Vesna 主持的艺术与科学合作中心，是众多机器与生物艺术项目背后艺术–科学网络的枢纽。 https://artsci.ucla.edu/
- **Waag Futurelab / Waag 未来实验室** (阿姆斯特丹，荷兰) — 阿姆斯特丹的技术与社会研究机构，运营公共实验室，包括对 AI、生物识别与“公共技术栈”的批判性研究。 https://waag.org/en/

### 驻留与项目

- **Akademie Schloss Solitude (Web Residencies) / 孤独城堡学院** (斯图加特，德国) — 斯图加特的驻留学院。其线上 Web Residencies 项目在 Schlosspost 发布，按策展主题资助艺术家，很多主题关于 AI、机器人程序与算法文化。 https://www.akademie-solitude.de/en/
- **China Academy of Art – School of Inter-Media Art / 中国美术学院跨媒体艺术学院** (杭州，中国) — 中国美术学院的跨媒体艺术学院，是中国新媒体、装置与网络艺术教育的重镇，也是中国机器与 AI 艺术家的重要培养地。 https://en.wikipedia.org/wiki/China_Academy_of_Art
- **Eyebeam** (纽约，美国) — 以驻留与奖学金支持技术艺术家的非营利机构，校友作品中有大量关于监控、偏见与算法正义的项目。 https://www.eyebeam.org/
- **Goldsmiths Computational Arts / 伦敦大学金史密斯学院计算艺术** (伦敦，英国) — 金史密斯学院的计算艺术课程与具身交互研究（EAVI），培养了许多以机器学习、身体与声音创作的艺术家。 https://www.gold.ac.uk/pg/ma-computational-arts/
- **Gray Area** (旧金山，美国) — 旧金山的创意技术非营利艺术中心，设有孵化器、教育项目以及关注艺术、AI 与社会的 Gray Area Festival。 https://grayarea.org/
- **IAMAS – Institute of Advanced Media Arts and Sciences / 情报科学艺术大学院大学** (大垣，日本) — 位于日本岐阜县的媒体艺术与科学研究生院，校友中有许多日本装置、传感与机器艺术家。 https://www.iamas.ac.jp/en/
- **NEW INC** (纽约，美国) — 新美术馆的艺术、设计与技术文化孵化器，成员开发了许多关于 AI 及其社会影响的项目。 https://www.newmuseum.org/new-inc/
- **NYU ITP / IMA / 纽约大学互动电信项目** (纽约，美国) — 纽约大学 Tisch 艺术学院的互动电信项目与互动媒体艺术系，是物理计算、创意机器学习（ml5.js）与技术艺术创作的重镇。 https://tisch.nyu.edu/itp
- **S+T+ARTS Residencies / S+T+ARTS 驻留计划** (欧盟) — 欧盟委员会资助艺术家进入技术与科研项目驻留的计划，许多项目涉及 AI、机器人与可持续发展。 https://starts.eu/
- **SAIC Art and Technology Studies / 芝加哥艺术学院艺术与技术系** (芝加哥，美国) — 芝加哥艺术学院的院系，源自 Sonia Sheridan 的“生成系统”项目（1970），将机器人、动态与电子技术作为艺术来教授。 https://www.saic.edu/atsp
- **School for Poetic Computation (SFPC) / 诗意计算学校** (纽约，美国) — 纽约由艺术家运营的学校，教授艺术、代码、硬件与批判理论，开设关于机器诗学与政治的课程。 https://sfpc.study/
- **School of Creative Media, City University of Hong Kong / 香港城市大学创意媒体学院** (香港) — 香港的媒体艺术学院，主办“Art Machines”计算媒体艺术研讨会，是亚洲机器人与 AI 艺术的中心之一。 https://www.scm.cityu.edu.hk/
- **Somerset House Studios / 萨默塞特宫工作室** (伦敦，英国) — 萨默塞特宫内为艺术家与创作者设立的实验性工作空间，入驻工作室涉及 AI、声音与推测设计，也制作了《24/7》（2019）等展览。 https://www.somersethouse.org.uk/somerset-house-studios
- **UCLA Design Media Arts / UCLA 设计媒体艺术系** (洛杉矶，美国) — UCLA 的媒体艺术与设计系，教师包括 Casey Reas（Processing）与 Lauren Lee McCarthy（《LAUREN》）。 https://dma.ucla.edu/

### 档案与数据库

- **ACM SIGGRAPH History Archive (Digital Art Archive) / ACM SIGGRAPH 数字艺术档案** (线上) — 收录 1980 年代以来 SIGGRAPH 艺术画廊、作品与艺术论文的在线档案，记录了与图形学研究并行的计算与机器人艺术。 https://history.siggraph.org/
- **AI Art Gallery (aiartonline.com) / AI 艺术在线画廊** (线上) — 由 Luba Elliott 策划的 NeurIPS 机器学习与创意设计研讨会线上画廊，存档了 2017–2021 年机器学习社群选出的艺术作品。 https://www.aiartonline.com/
- **AI Incident Database / AI 事故数据库** (线上) — 记录 AI 系统在现实中造成或险些造成伤害的开放档案，起源于 Partnership on AI，收录从误识别到自动驾驶事故等各类机器失败。 https://incidentdatabase.ai/
- **AI Myths / AI 迷思** (线上) — 由 Daniel Leufer 创建的资源站，逐条拆解关于 AI 的常见误解（如“AI 具有能动性”“AI 可以客观”），并附研究文献。 https://www.aimyths.org/
- **AIAAIC Repository / AIAAIC 事件库** (线上) — 独立的公益性 AI、算法与自动化事件及争议资料库，按行业、技术与危害类型分类。 https://www.aiaaic.org/
- **AIArtists.org** (线上) — 与 AI 合作的艺术家名录，按偏见、数据集伦理、机器人创作等关键问题组织，偏重生成式作品，适合作为线索清单。 https://aiartists.org/
- **Anatomy of an AI System / AI 系统解剖图** (线上) — Kate Crawford 与 Vladan Joler 绘制的地图与论文，揭示一次 Amazon Echo 请求背后的人类劳动、数据与地球资源，被 MoMA 与 V&A 收藏。 https://anatomyof.ai/
- **Archive of Digital Art (ADA) / 数字艺术档案** (克雷姆斯，奥地利) — Oliver Grau 创立的数字艺术学术数据库，记录数百位艺术家及数千件作品与文献，对机器人与人工生命艺术覆盖尤深。 https://www.digitalartarchive.at/
- **Ars Electronica Archive / 电子艺术节档案** (林茨，奥地利) — 收录 1987 年以来电子艺术大奖参赛作品、艺术节图录与文献的档案，是媒体艺术如何回应机器人、人工生命与 AI 的最大记录。 https://ars.electronica.art/archive/en/
- **Atlas of Surveillance / 监控地图集** (美国 / 线上) — 电子前哨基金会与内华达大学里诺分校合作的数据库，记录美国警方使用的监控技术，从人脸识别到无人机和自动车牌识别。 https://atlasofsurveillance.org/
- **Better Images of AI / 更好的 AI 图像** (线上) — 非营利合作项目，委托艺术家创作并免费提供比“发光大脑”和人形机器人更准确地表现 AI 的图像库。 https://betterimagesofai.org/
- **Calculating Empires / 计算帝国** (线上) — Crawford 与 Joler 的大型研究可视化《技术与权力的谱系 1500–2025》，追溯通信与计算系统如何与控制一同扩张，获 2024 年 S+T+ARTS 大奖。 https://calculatingempires.net/
- **Critical Algorithm Studies: a Reading List / 批判算法研究书单** (线上) — 由微软研究院社交媒体小组的 Tarleton Gillespie 与 Nick Seaver 编制的书单，关注作为社会议题的算法，是批判算法研究的标准入门。 https://socialmediacollective.org/reading-lists/critical-algorithm-studies/
- **Cybernetic Serendipity archive / 控制论的意外发现档案** (线上) — Jasia Reichardt 1968 年在伦敦当代艺术学院策划的《控制论的意外发现》的线上档案。该展是计算机与控制论艺术的开山展览，展出 Gordon Pask《Colloquy of Mobiles》与 Edward Ihnatowicz《SAM》等作品。 https://www.cyberneticserendipity.net/
- **cyberneticzoo.com** (线上) — 图文并茂的控制论动物与早期机器人史，从 Grey Walter 的机器龟到被遗忘的步行机器，均取材于当时文献。 https://cyberneticzoo.com/
- **Daniel Langlois Foundation for Art, Science and Technology / 丹尼尔·朗格卢瓦艺术、科学与技术基金会** (蒙特利尔，加拿大) — 其在线档案记录了“艺术与技术实验”（E.A.T.）与早期媒体艺术，并收录关于机器与控制论艺术家的论文。 https://www.fondation-langlois.org/
- **Data Workers' Inquiry / 数据劳工调查** (柏林 / 全球) — DAIR 与魏岑鲍姆研究所的社区研究项目，由为 AI 做标注与审核的数据劳工以报告、影片与小册子记录自身的劳动处境。 https://data-workers.org/
- **Database of Digital Art (compArt daDA) / 数字艺术数据库** (不来梅，德国) — 不来梅大学 compArt 中心建立的数据库，收录计算机艺术先驱及其展览，包括《Cybernetic Serendipity》（1968）。 http://dada.compart-bremen.de/
- **Excavating AI / 发掘 AI** (线上) — Kate Crawford 与 Trevor Paglen 关于机器学习训练集中图像政治的论文，剖析 ImageNet 的“人”类别，并催生了《ImageNet Roulette》。 https://excavating.ai/
- **Exposing.ai** (柏林，德国) — Adam Harvey 与 Jules LaPlace 的研究项目（MegaPixels 的延续），追溯人脸与生物识别数据集如何由抓取的照片构成，并让公众查询自己的照片是否被使用。 https://exposing.ai/
- **Machine Vision in Art, Games and Narratives (database) / 艺术、游戏与叙事中的机器视觉数据库** (卑尔根，挪威) — 卑尔根大学的 ERC 项目，其开放数据库将约 500 件艺术作品、游戏与叙事编码为“情境”：谁借助何种机器视觉技术对谁做了什么。 https://machinevisionuib.github.io/
- **Media Art Net / 媒体艺术网** (卡尔斯鲁厄，德国) — ZKM 与歌德学院合作的德英双语在线平台，收录媒体艺术史的作品、艺术家与论文，包括机器人与控制论艺术。 http://www.medienkunstnetz.de/
- **Media Arts Database (Japan) / 日本媒体艺术数据库** (东京，日本) — 日本国家级媒体艺术数据库，收录媒体艺术展览、艺术节与作品记录，便于追溯日本的机器与装置艺术。 https://mediaarts-db.artmuseums.go.jp/
- **Monoskop** (线上) — 由 Dušan Barok 创建的艺术、媒体与人文维基与数字图书馆，收录大量关于控制论艺术、媒体艺术节与机器理论的页面和扫描文献。 https://monoskop.org/
- **ROBOTS Guide (IEEE Spectrum) / IEEE 机器人指南** (线上) — IEEE 编制的真实机器人图录，为数百款人形、陪伴与工业机器人提供照片、视频与参数。 https://robotsguide.com/
- **The Glass Room / 玻璃房间** (柏林，德国 / 线上) — Tactical Tech 以科技商店形式呈现的数据与监控展览，40 多件展品分为“我们认识你”“大妈妈”等主题，现以社区版与线上版巡展。 https://theglassroom.org/

### 期刊、书籍与播客

- **AI & Society (Springer) / 《AI 与社会》期刊** (全球) — 关于 AI 社会影响的知识、文化与传播期刊，涵盖艺术、劳动与伦理。 https://link.springer.com/journal/146
- **AI Weirdness** (线上) — Janelle Shane 的博客与通讯，记录 AI 各种奇特的失败，从神经网络命名的油漆颜色到凭空出现的长颈鹿，以机器错误为窗口观察机器“心智”。 https://www.aiweirdness.com/
- **APRJA – A Peer-Reviewed Journal About** (奥胡斯，丹麦 / 柏林) — 与 transmediale 和奥胡斯大学合作的开放获取期刊，每期源自一场研究工作坊，主题如“机器研究”“机器感受”。 https://aprja.net/
- **Blood in the Machine / 机器中的血** (线上) — Brian Merchant 的通讯与同名著作，讲述卢德派与当下反自动化的抗争，报道 AI 如何重塑工作。 https://www.bloodinthemachine.com/
- **Computational Culture / 《计算文化》期刊** (线上) — 软件研究领域的开放获取期刊，发表关于算法、机器学习与代码文化生命的研究。 https://computationalculture.net/
- **Critical AI (Duke University Press) / 《批判性 AI》期刊** (美国) — 以罗格斯大学为基地的跨学科期刊与计划，以人文学科方法研究 AI，从大语言模型到数据劳动。 https://criticalai.org/
- **Cybernetic Forests / 控制论森林** (线上) — Eryk Salvaggio 关于 AI、艺术与控制论的通讯，把生成图像当作其数据集的“信息图”来解读，并批判 AI 炒作。 https://www.cyberneticforests.com/
- **e-flux journal / e-flux 期刊** (纽约，美国) — 在线艺术期刊，刊登了关于机器视觉与 AI 的关键文本，如 Hito Steyerl 的《A Sea of Data：幻想性错觉与模式（误）识别》（2016）。 https://www.e-flux.com/journal/
- **Leonardo (MIT Press) / Leonardo ISAST / 《莱昂纳多》期刊** (剑桥（马萨诸塞州） / 旧金山，美国) — 由动态艺术家 Frank Malina 创办的艺术、科学与技术期刊，Eduardo Kac、Simon Penny 等人在此发表了机器人艺术的奠基文本；Leonardo 还出版丛书并举办 LASER 讲座。 https://leonardo.info/
- **Logic(s)** (美国) — 关于技术及其政治的杂志，后改版为 Logic(s)，聚焦黑人、亚裔与原住民视角，出版过“智能”“身体”“供应链”等专刊。 https://logicmag.io/
- **meson press** (吕讷堡，德国) — 开放获取的媒体理论出版社，出版关于机器学习、模式辨别与计算史的著作。 https://meson.press/
- **Mute** (伦敦，英国) — 伦敦的“网络之后的文化与政治”杂志，长期发表关于自动化、劳动与数字资本主义的批判性文章。 https://www.metamute.org/
- **Mystery AI Hype Theater 3000** (线上) — DAIR 出品的播客与直播，语言学家 Emily M. Bender 与社会学家 Alex Hanna 在节目中逐条拆解“机器智能”与 AI 炒作。 https://www.dair-institute.org/maiht3k/
- **nettime** (线上) — 1995 年创立的网络批评邮件列表，网络艺术与战术媒体几代人在此讨论网络、软件与机器。 https://www.nettime.org/
- **Neural** (巴里，意大利) — Alessandro Ludovico 创办的意英双语杂志，关注新媒体艺术、电子音乐与黑客行动主义，长期记录批判性机器艺术。 https://neural.it/
- **Noema Magazine** (洛杉矶，美国) — 博古睿研究院出版的杂志，刊登 Benjamin Bratton、Blaise Agüera y Arcas、Tobias Rees 等人关于 AI、心智与行星计算的长文。 https://www.noemamag.com/
- **Open Humanities Press / 开放人文出版社** (线上) — 开放获取学术出版社，出版了 Joanna Zylinska 的《AI 艺术：机器视觉与扭曲的梦》（2020）等著作。 https://www.openhumanitiespress.org/
- **Philosophy & Technology (Springer) / 《哲学与技术》期刊** (全球) — 关于技术的哲学期刊，涵盖后现象学、机器能动性与 AI 伦理。 https://link.springer.com/journal/13347
- **Posthumanities (University of Minnesota Press) / 《后人类》丛书** (明尼阿波利斯，美国) — 由 Cary Wolfe 主编的丛书，包括 Ian Bogost 的《异形现象学》（2012），是思考非人与机器经验的核心书架。 https://www.upress.umn.edu/search-grid/?series=posthumanities
- **Real Life** (线上) — 关于与技术共同生活的在线杂志（2016–2022），其关于智能音箱、算法与机器亲密的文章构成了日常机器现象学的档案。 https://reallifemag.com/
- **Tech Won't Save Us (podcast)** (线上) — Paris Marx 主持的每周播客，以批判视角讨论科技、AI 热潮及其背后的劳动与基础设施。 https://techwontsave.us/
- **Technophany** (线上) — 哲学与技术研究网络（许煜等人发起）的期刊，发表技术哲学、宇宙技术与机器思想相关研究。 https://technophany.philosophyandtechnology.network/
- **The Good Robot (podcast) / 好机器人播客** (剑桥，英国) — 由 Eleanor Drage 与 Kerry McInerney 主持的播客，请女性主义学者与技术从业者探讨什么是“好的技术”。 https://www.thegoodrobot.co.uk/

### 网络与非营利组织

- **AIxDesign** (阿姆斯特丹，荷兰 / 全球) — 由设计师、艺术家与研究者组成、以批判方式处理 AI 的社群与工作室，开展项目、出版物及“慢 AI”研究。 https://aixdesign.co/
- **Algorithmic Justice League / 算法正义联盟** (剑桥（马萨诸塞州），美国) — 由 Joy Buolamwini 创立的组织，结合艺术与研究揭示 AI 的偏见，起点是《Gender Shades》所揭示的人脸识别“编码凝视”。 https://www.ajl.org/
- **AlgorithmWatch / 算法观察** (柏林，德国) — 调查自动化决策系统及其对欧洲社会影响的非营利研究与倡导组织。 https://algorithmwatch.org/en/
- **Black in AI** (全球) — 由 Timnit Gebru 与 Rediet Abebe 共同发起的网络，旨在提升黑人在 AI 领域的参与和代表性。 https://blackinai.github.io/
- **Coding Rights** (里约热内卢，巴西) — 巴西的女性主义技术与人权组织，其《Not My A.I.》项目梳理拉丁美洲针对边缘群体部署的 AI 系统。 https://codingrights.org/
- **Computer Arts Society (CAS) / 计算机艺术学会** (伦敦，英国) — 1968 年（《控制论的意外发现》同年）成立的英国学会，推动计算机在艺术中的应用，出版通讯 PAGE，现为英国计算机学会的专业小组。 https://computer-arts-society.com/
- **Constant** (布鲁塞尔，比利时) — 布鲁塞尔由艺术家运营的艺术、媒体与技术协会，旗下 Algolit 小组以文学与代码探索机器学习。 https://constantvzw.org/
- **Critical Engineering Working Group / 批判工程工作组** (柏林，德国) — 《批判工程宣言》（2011）的发起团体，呼吁工程师与艺术家揭示我们所依赖的技术的内部运作。 https://criticalengineering.org/
- **Data for Black Lives** (美国) — 由活动者与科学家组成的运动，用数据改善黑人生活，并对抗算法歧视。 https://d4bl.org/
- **Experiments in Art and Technology (E.A.T.) / 艺术与技术实验** (纽约，美国) — 由贝尔实验室工程师与艺术家在《九夜》（1966）之后创立的非营利组织，为艺术家与工程师配对，奠定了艺术–技术合作的模式。 https://en.wikipedia.org/wiki/Experiments_in_Art_and_Technology
- **Feminist.AI / 女性主义 AI** (洛杉矶，美国) — 与社区共同设计 AI 原型与数据集的社区研究团体，以亲手实践的方式创造女性主义与批判性 AI。 https://www.feminist.ai/
- **Indigenous Protocol and AI Working Group / 原住民协议与 AI 工作组** (全球) — 该工作组 2020 年发表的立场文件探讨原住民认识论如何指导 AI 设计，以及我们与包括机器在内的非人亲属的关系。 https://www.indigenous-ai.net/
- **Machine Listening / 机器聆听** (墨尔本，澳大利亚) — 关于机器聆听、语音助手与音频监控政治的研究与艺术实践平台，并提供开放课程。 https://machinelistening.exposed/
- **Masakhane** (非洲 / 全球) — 由非洲人为非洲语言建设自然语言处理的草根研究社群，回应以英语为中心的“机器之耳”。 https://www.masakhane.io/
- **Processing Foundation / Processing 基金会** (美国 / 全球) — Processing 与 p5.js 背后的非营利组织，推广艺术领域的软件素养，并以奖学金支持以批判方式使用代码与机器学习的艺术家。 https://processingfoundation.org/
- **Queer in AI** (全球) — AI 领域酷儿研究者与从业者的草根组织，揭示 AI 如何误分类并伤害酷儿群体。 https://www.queerinai.com/
- **Rhizome** (纽约，美国) — 隶属新美术馆的原生数字艺术机构，委托、保存并评论与技术相关的艺术，运营 ArtBase 与 Webrecorder 工具。 https://rhizome.org/
- **Tactical Tech** (柏林，德国) — 帮助公众理解技术如何塑造社会的国际非政府组织，通过《The Glass Room》等展览以及数据与影响力工具包开展工作。 https://tacticaltech.org/
- **Tierra Común** (拉丁美洲 / 全球) — 关注“数据殖民主义”的活动者与学者网络，以全球南方视角审视数据与 AI 背后的攫取。 https://www.tierracomun.net/
- **Turkopticon** (美国 / 线上) — 由 Lilly Irani 与 Six Silberman 发起、为亚马逊 Mechanical Turk 众包工人服务的工具与组织项目，使 AI 背后隐形的人力劳动变得可见、可争。 https://turkopticon.net/

## 创作者

- **Lauren Lee McCarthy** (11) — 艺术家；加州大学洛杉矶分校设计媒体艺术系教授；p5.js 创建者. 艺术家和程序员，她在表演中亲自扮演智能家居助手、应用和算法，审视日常生活中的监控、自动化与照护。 https://lauren-mccarthy.com/
- **Trevor Paglen** (10) — 艺术家、地理学家. 美国艺术家与地理学家，以摄影、装置和表演研究监控、国家机密与计算机视觉。 https://paglen.studio
- **Hito Steyerl** (9) — 艺术家、电影人、写作者. 德国艺术家，以论文电影和装置研究图像、流通、战争与计算。 https://en.wikipedia.org/wiki/Hito_Steyerl
- **Hiroshi Ishiguro** (8) — 机器人学家；大阪大学教授，ATR 石黑浩实验室. 制作高度逼真的仿真人，包括以自己为原型的 Geminoid HI-1，并借此研究“人的存在感”。 http://www.geminoid.jp/en/
- **Kyle McDonald** (8) — 艺术家、创意技术专家. 用代码、计算机视觉和机器学习创作的艺术家；openFrameworks 工具的贡献者，与 Lauren Lee McCarthy 合作了多件作品。 https://kylemcdonald.net
- **Stelarc** (7) — 行为艺术家；科廷大学杰出研究员（Alternate Anatomies Lab）. 生于塞浦路斯的澳大利亚艺术家，自 1970 年代起用机器人、义体与网络延伸、悬吊、连接和增强自己的身体。 https://stelarc.org/
- **Botao Amber Hu** (6) — 牛津大学研究者，Reality Design Lab 创始人. 设计师和研究者（清华大学计算机本科、斯坦福大学人工智能硕士），研究混合现实、思辨设计和基于区块链的人工生命；Reality Design Lab 的作品在 SIGGRAPH、CHI、ALIFE 和 ISEA 等场合展出。 https://reality.design
- **Kate Crawford** (6) — 研究者、作家；南加州大学安嫩伯格学院研究教授. 澳大利亚学者，研究 AI 的社会与政治影响，AI Now 研究所联合创始人，著有《Atlas of AI》（2021）。 https://katecrawford.net/
- **Adam Harvey** (5) — 艺术家、研究者（计算机视觉、隐私与监控）. 美国艺术家、研究者，自 2010 年在纽约大学 ITP 的毕业作品 CV Dazzle 起持续研究计算机视觉、生物识别与反监控。后续研究追踪人脸数据集如何建成，并把目标检测技术用于人权档案。 https://adam.harvey.studio
- **Bill Vorn** (5) — 机器人艺术家；康考迪亚大学教授. 加拿大艺术家（1959 年生），围绕“人工行为美学”创作机器人装置，从歇斯底里的机器到“精神疾病”的机器。 http://billvorn.concordia.ca/
- **Daito Manabe** (5) — 艺术家、程序员、DJ；Rhizomatiks 联合创始人. 媒体艺术家，以肌肉电刺激、无人机、机器学习与脑数据为材料创作。 https://www.daito.ws/en/
- **Jake Elwes** (5) — 以机器学习创作的艺术家. 英国艺术家，通过酷儿表演、风景以及网络之间的反馈来探讨 AI。 https://www.jakeelwes.com
- **James Bridle** (5) — 艺术家、作家. 英国艺术家、作家，关注技术、网络与非人智能，著有《New Dark Age》（2018）和《Ways of Being》（2022）。 https://jamesbridle.com/
- **Joana Moll** (5) — 艺术家、研究者. 常驻巴塞罗那的艺术家与研究者，作品考察互联网的物质、生态与监控基础设施，从边境摄像头到数据经纪商，再到网站的碳排放。 https://www.janavirgin.com/
- **Lawrence Lek** (5) — 艺术家、电影人、音乐人. 马来西亚华裔、常居伦敦的艺术家，在“中华未来主义”世界观中以影像、游戏与模拟讲述 AI。 https://www.lawrencelek.com
- **Louis-Philippe Demers** (5) — 机器人艺术家、研究者. 加拿大艺术家，自 20 世纪 90 年代起创作大型机器人装置与表演，常与 Bill Vorn 合作，并撰写关于“表演的机器”的论述。
- **Mimi Ọnụọha** (5) — 艺术家、研究者. 尼日利亚裔美国艺术家，以装置、影像和写作追问数据收集包含了什么、遗漏了什么、又隐藏了什么。 https://www.mimionuoha.com/
- **Ralf Baecker** (5) — 媒体艺术家；不来梅艺术大学教授. 德国艺术家（1977 年生），用大型机械装置来模拟计算、感知与神经网络。 https://rlfbckr.io/
- **Shinseungback Kimyonghun** (5) — 艺术家组合（Shin Seung Back 与 Kim Yong Hun）. 2012 年成立的首尔艺术家组合，以人脸检测、物体识别等机器视觉系统为材料制作装置。 https://ssbkyh.com/
- **automato.farm** (5) — 设计工作室（Simone Rebaudengo、Saurabh Datta、Matthieu Cherubini 等）. 思辨设计团体，围绕联网物件、自动化与机器学习制作可运行的原型。 http://www.automato.farm/
- **Christa Sommerer & Laurent Mignonneau** (4) — 媒体艺术二人组，林茨艺术与设计大学界面文化系教授. Christa Sommerer 和 Laurent Mignonneau 自 1990 年代初开始创作关于人工生命的交互艺术。
- **Dries Depoorter** (4) — 艺术家. Dries Depoorter 是比利时艺术家，以装置、应用和网络项目探讨隐私、监控摄像头与机器学习。 https://driesdepoorter.be
- **Eduardo Kac** (4) — 艺术家；远程在场艺术与生物艺术先驱. 巴西裔美国艺术家，1980 年代末起创作远程机器人作品，后来转向转基因艺术。 https://www.ekac.org
- **Forensic Architecture** (4) — 研究机构，伦敦大学金史密斯学院. Forensic Architecture（法证建筑）由 Eyal Weizman 于 2010 年创立，用空间、建筑与计算方法调查国家和企业暴力，并在法庭与美术馆中呈现结果。 https://forensic-architecture.org/
- **Gilberto Esparza** (4) — 以机器人、生物技术和生态为媒介的艺术家. 墨西哥艺术家，制作依靠城市电网、污染河流和污水生存的自主生物机器与机器人“寄生体”。 https://gilbertoesparza.net
- **Guo Cheng** (4) — 艺术家. 中国艺术家，围绕技术系统（从人脸检测、防火墙到算力）创作装置与研究项目。 https://www.guo-cheng.net
- **Harun Farocki** (4) — 电影人、艺术家（1944–2014）. 德国电影人、作家与装置艺术家，创作了 90 多部关于图像、劳动与战争的影片和装置。 https://www.harunfarocki.de/
- **Jiabao Li** (4) — 艺术家、设计师；美国东北大学（奥克兰校区）艺术与设计教授. 艺术家、发明者和教授（哈佛设计研究生院毕业，曾任苹果公司设计师），用装置、可穿戴设备、XR、生物艺术和表演处理感知、技术与多于人类的世界。2026 年个展《Womb Wetware》创作于怀孕期间及产后，把母职当作检验照护、身体与机器的试验场。 https://www.jiabaoli.org
- **Julian Oliver** (4) — 批判性工程师与艺术家. 新西兰艺术家，《批判性工程宣言》的合著者。 https://julianoliver.com/
- **Lawrence Abu Hamdan** (4) — 艺术家、声音调查者（自称“私人耳朵”）. 艺术家，他对声音、枪声与沉默所做的音频调查曾在庇护听证和人权案件中被用作证据；2019 年特纳奖联合得主。 http://lawrenceabuhamdan.com/
- **Lynn Hershman Leeson** (4) — 艺术家、电影人. 美国艺术家，自 1960 年代起关注身份、监视、人工智能以及身体与技术的关系。 https://www.lynnhershman.com/
- **Nam June Paik** (4) — 艺术家，录像艺术先驱. 韩裔艺术家（1932–2006），激浪派成员，把电视、摄像机与机器人变成艺术材料。 https://en.wikipedia.org/wiki/Nam_June_Paik
- **Philipp Schmitt** (4) — 艺术家、设计师. Philipp Schmitt（1993 年生）是艺术家和设计师，以装置、艺术家书和网站探讨计算的哲学、诗意与政治面向。 https://philippschmitt.com
- **Sebastian Schmieg** (4) — 艺术家. Sebastian Schmieg 是常驻柏林的艺术家，用现成数据集、定制软件、网站和讲座表演，揭示算法系统中的人类劳动。 https://sebastianschmieg.com/
- **So Kanno** (4) — 艺术家. 媒体艺术家，制作会绘画、成群行动和书写的机器人与机器，常与 yang02（山口崇洋）合作。 https://www.kanno.so/
- **Superflux** (4) — 由 Anab Jain 和 Jon Ardern 创办的思辨设计与未来研究工作室. Superflux 用沉浸式装置、影像和政策原型把可能的未来做成可以体验的东西，其中一条长期主线是超越人类的政治与生态 AI。 https://superflux.in
- **Vladan Joler** (4) — 艺术家、研究者，SHARE 基金会，诺维萨德大学教授. 塞尔维亚艺术家和研究者，绘制关于技术、攫取与权力的大型图解地图。 https://labs.rs/en/
- **Anna Ridler** (3) — 以数据与机器学习创作的艺术家. 英国艺术家，亲手制作数据集（常以花卉为对象），并用它们训练生成模型。 https://annaridler.com
- **Annie Dorsen** (3) — 算法剧场导演与作者. 美国剧场导演，自 2010 年起创作由算法现场书写、说出或调度文本的表演。 https://anniedorsen.com/
- **Arthur Ganson** (3) — 动态雕塑家. 美国动态雕塑家（1955 年生），作品在麻省理工学院博物馆展出，用齿轮机器演绎时间、努力与徒劳。 https://www.arthurganson.com/
- **Bjørn Karmann** (3) — 设计师、创意技术专家. 丹麦设计师，毕业于哥本哈根交互设计学院（CIID），制作可以实际运行的设备，让人训练、改造或重新思考机器感知。 https://bjoernkarmann.dk/
- **Cao Fei** (3) — 艺术家、电影人. 生于广州的艺术家，以影像、虚拟世界与装置关注中国的劳动、城市化与数字生活。 https://www.caofei.com
- **Chico MacMurtrie** (3) — 艺术家；Amorphic Robot Works 创始人. 美国艺术家（1961 年生），与 Amorphic Robot Works 一起制作拟人的、会奏乐的和充气式机器人雕塑。 http://www.amorphicrobotworks.org/
- **Claude Shannon** (3) — 数学家、工程师，贝尔实验室与麻省理工学院. 美国数学家（1916–2001），信息论的奠基人，也做了不少带玩心的机器，包括会学走迷宫的老鼠 Theseus 和“终极机器”。
- **Cod.Act** (3) — André 与 Michel Décosterd 兄弟二人组（作曲家与建筑师）. 瑞士二人组，制作以混沌运动产生音乐的声音机器；2019 年获瑞士音乐大奖。 https://codact.ch/
- **Dunne & Raby (Anthony Dunne & Fiona Raby)** (3) — 批判与思辨设计实践者，纽约 The New School 教授. Anthony Dunne 与 Fiona Raby 确立了批判设计这一实践，用设计物件与情境——包括生物技术的情境——来讨论可能的未来。 https://dunneandraby.co.uk/
- **Elisa Giaccardi** (3) — 米兰理工大学交互设计教授，曾任代尔夫特理工大学后工业设计讲席教授. 交互设计研究者，把相机装在日常物件上，从物的角度观察世界，发展了以物为中心的设计。
- **Guy Ben-Ary** (3) — 西澳大学 SymbioticA 艺术家与研究者. 生物艺术家，自 2000 年起与活体神经元合作：机器人绘画（MEART）、神经合成器（cellF），以及用作曲家 Alvin Lucier 的血液培养出的类器官（Revivification）。 https://guybenary.com
- **Heather Dewey-Hagborg** (3) — 艺术家、生物黑客. Heather Dewey-Hagborg 是美国艺术家，作品关注基因监控、DNA 表型推断，以及把生物痕迹变成人脸的算法。 https://deweyhagborg.com
- **Hod Lipson** (3) — 机器人学家；哥伦比亚大学教授. 以色列裔美国机器人学家，研究演化机器人、自我建模与自我觉察的机器。 https://www.hodlipson.com/
- **Holly Herndon** (3) — 作曲家、艺术家. 美国作曲家，用人声、计算机以及与合作者共同训练的 AI 模型创作音乐。 https://holly.plus/
- **Josh Bongard** (3) — 机器人学家；佛蒙特大学教授. 加拿大机器人学家，研究演化机器人与具身认知，是异种机器人（xenobot）的共同创造者之一。
- **Joy Buolamwini** (3) — 计算机科学家、“代码诗人”，算法正义联盟创始人. 加纳裔美籍加拿大研究者。她在 MIT 媒体实验室发现人脸分析系统无法识别她的深色皮肤面孔，并把这一发现变成算法审计、诗歌和一场社会运动。 https://www.poetofcode.com/
- **Kelly Dobson** (3) — 艺术家、设计师；罗德岛设计学院教授. 美国艺术家，在麻省理工学院媒体实验室提出“机器疗法”，制作通过声音与呼吸与人建立关系的机器。 http://www.kellydobson.com/
- **Ken Goldberg** (3) — 艺术家、机器人学家；加州大学伯克利分校教授. 机器人学教授，1990 年代把最早一批可经互联网操控的机器人做成艺术作品。 https://goldberg.berkeley.edu/
- **Kris Verdonck** (3) — 剧场创作者、视觉艺术家；A Two Dogs Company 总监. 比利时艺术家，他的表演与装置让机器、物件与人以平等的表演者身份同台。 https://www.atwodogscompany.org/
- **Lu Yang** (3) — 艺术家. 上海艺术家，把神经科学、佛教宇宙观、游戏引擎与动作捕捉结合进影像、游戏与数字化身。
- **Marcel·lí Antúnez Roca** (3) — 艺术家；La Fura dels Baus 联合创始人. 加泰罗尼亚艺术家，离开 La Fura dels Baus 后创作“机电表演”，让外骨骼、机器人与观众共同操控身体。 https://www.marceliantunez.com/
- **Marco Donnarumma** (3) — 行为艺术家、作曲家与研究者. 意大利艺术家，在表演中把身体、声音与 AI 驱动的义体融合，探讨仪式、残障与机器自主。 https://marcodonnarumma.com/
- **Mat Dryhurst** (3) — 艺术家、研究者. 英国艺术家，Herndon 的长期合作者，关注 AI、数据权利与网络治理。 https://holly.plus/
- **Memo Akten** (3) — 艺术家；加州大学圣地亚哥分校教授. 生于土耳其的艺术家，以机器学习、感知与意义生成为创作主题。 https://www.memo.tv
- **Oriza Hirata** (3) — 剧作家、导演（青年团剧团）；大阪大学教授. “现代口语戏剧”的代表剧作家，2008 年与石黑浩发起“机器人-人类剧场”计划。
- **Paolo Cirio** (3) — 艺术家. Paolo Cirio 是意大利艺术家，其介入式作品揭示信息技术背后的法律、社会与经济系统，从隐私到金融。 https://paolocirio.net
- **Pierre Huyghe** (3) — 艺术家. 法国艺术家，用动物、植物、微生物和机器学习系统搭建会自行变化的活体情境，这些情境在没有观众时也照样运行。 https://www.estherschipper.com/artists/41-pierre-huyghe/
- **Rafael Lozano-Hemmer** (3) — 媒体艺术家；Antimodular Research 创始人. Rafael Lozano-Hemmer 是墨西哥裔加拿大艺术家，其互动装置在公共空间和美术馆中使用追踪、生物识别与监控系统。 https://www.lozano-hemmer.com
- **Simon Penny** (3) — 艺术家、具身交互理论家；加州大学尔湾分校教授. 澳大利亚艺术家与理论家（1955 年生），用自主机器人和交互环境探讨具身性；著有 Making Sense（2017）。 https://simonpenny.net/
- **Sougwen Chung** (3) — 艺术家；Scilicet 工作室创始人. 生于加拿大、成长于香港的艺术家，与她亲自搭建和训练的机械臂（D.O.U.G. 系列）一起绘画。 https://sougwen.com
- **Stephanie Dinkins** (3) — 艺术家；石溪大学教授. 跨媒体艺术家，与黑人社群一起、并围绕黑人社群制作 AI 系统：从与机器人 BINA48 的对话，到用家族故事训练的聊天机器人；2023 年首届 LG 古根海姆奖得主。 https://www.stephaniedinkins.com/
- **Takahiro Yamaguchi (yang02)** (3) — 艺术家（yang02）. 以 yang02 之名创作涂鸦、公共空间与绘画机器，与菅野创合作《Senseless Drawing Bot》。
- **Takashi Ikegami** (3) — 人工生命研究者；东京大学教授. 复杂系统科学家，用人工生命装置和仿真人 Alter 研究机器中的自发性与“生命感”。
- **Yuk Hui** (3) — 哲学家；鹿特丹伊拉斯谟大学哲学教授. 生于香港的技术哲学家，以“数码物”“宇宙技术”“技术多样性”等概念著称。
- **Zach Blas** (3) — 艺术家、电影人与写作者；多伦多大学副教授. Zach Blas 是美国艺术家，以酷儿视角通过影像、装置与面具审视生物识别、预测技术与技术政治。 https://zachblas.info
- **robotlab** (3) — 艺术小组（Matthias Gommel、Martina Haitz、Jan Zappe）. 2000 年在 ZKM 成立的德国艺术小组，把工业机器人从工厂带进艺术与公共空间。 http://www.robotlab.de/
- **!Mediengruppe Bitnik** (2) — 艺术家二人组（Carmen Weisskopf 与 Domagoj Smoljo）. 瑞士艺术家二人组，以互联网、机器人、黑客行为与数据流通为创作手段。 https://wwwwwwwwwwwwwwwwwwwwww.bitnik.org/
- **Aaron Koblin** (2) — 艺术家、技术人. 美国艺术家，以数据可视化和众包作品闻名，后联合创立了 VR 工作室 Within。 https://www.aaronkoblin.com/
- **Addie Wagenknecht** (2) — 艺术家、研究者. 美国艺术家，结合女性主义理论、开源硬件和机器人创作；F.A.T. Lab 与 Deep Lab 成员。 https://www.placesiveneverbeen.com/
- **Agnieszka Kurant** (2) — 观念艺术家. 波兰艺术家，研究集体智能、非人类劳动与“看不见的经济”。 https://en.wikipedia.org/wiki/Agnieszka_Kurant
- **Alexander Mordvintsev** (2) — 谷歌研究科学家. 研究者，DeepDream 的创造者，后来研究神经元胞自动机。 https://znah.net/
- **Andrew Norman Wilson** (2) — 艺术家、电影人. 美国艺术家，影像与图像作品关注劳动、企业及其生产的媒介。 https://www.andrewnormanwilson.com/
- **Anicka Yi** (2) — 艺术家. 韩裔美国艺术家，以气味、细菌与机器为材料，提出“让机器生物化”。 https://en.wikipedia.org/wiki/Anicka_Yi
- **Ayoung Kim** (2) — 艺术家. 韩国艺术家，以 CGI、实拍与游戏引擎制作思辨虚构影像，关注地缘政治、劳动与时间。
- **Blaise Agüera y Arcas** (2) — 工程师与研究者；Google 副总裁、Fellow. Blaise Agüera y Arcas 是美国计算机科学家，在 Google 领导机器智能研究，并创立了 Artists + Machine Intelligence 项目。
- **Blast Theory** (2) — 艺术团体（Matt Adams、Ju Row Farr、Nick Tandavanitj）. 自 1990 年代起与诺丁汉大学混合现实实验室合作，创作游戏、应用和表演的互动艺术团体。 https://www.blasttheory.co.uk
- **Boston Dynamics** (2) — 机器人公司. 1992 年从麻省理工学院分拆出来的美国公司，以 BigDog、Spot、Atlas 等动态足式机器人闻名。 https://bostondynamics.com/
- **Byung-Chul Han** (2) — 哲学家、文化理论家. 韩裔德国哲学家，写作关于数字文化、新自由主义与智能手机时代的短篇著作。 https://en.wikipedia.org/wiki/Byung-Chul_Han
- **Caroline Sinders** (2) — 艺术家、设计师与人权研究者，Convocation Research + Design 创始人. 美国艺术家与研究者，研究网络骚扰、数据劳动以及机器学习系统的建造方式。 https://carolinesinders.com/
- **Chen Qiufan** (2) — 科幻作家. 中国科幻作家（英文名 Stanley Chan），作品涉及电子垃圾、赛博格与人工智能。
- **Choe U-Ram** (2) — 动态雕塑艺术家. 韩国雕塑家，用铝和钢制作带虚构学名的电机驱动“机械生物”（anima-machines）。 https://www.uram.net/
- **Choy Ka Fai** (2) — 艺术家、编舞者、思辨设计师. 新加坡艺术家，毕业于皇家艺术学院交互设计专业，创作关于身体、技术与记忆的表演。 https://www.ka5.info/
- **Clifford Nass** (2) — 斯坦福大学传播学教授（1958–2013）. 斯坦福大学社会科学家，主持 CHIMe 实验室，著有《Wired for Speech》（2005）与《The Man Who Lied to His Laptop》（2010）。
- **Cynthia Breazeal** (2) — 机器人学家；MIT 媒体实验室教授（个人机器人组）；Jibo 创始人. 社交机器人学先驱，1990 年代末制作了表情机器人头部 Kismet，之后创办家用机器人公司 Jibo。 https://www.media.mit.edu/people/cynthiab/overview/
- **David Rokeby** (2) — 装置艺术家. 加拿大互动装置先驱，以《Very Nervous System》（1986–90）以及关于机器感知与监控的作品闻名。 http://www.davidrokeby.com
- **Diemut Strebe** (2) — 艺术家，麻省理工学院艺术、科学与技术中心附属. Diemut Strebe 与科学实验室合作创作，包括 Sugababe：用梵高后裔细胞培养出的活体梵高耳朵复制品，保存在营养液展柜中。 https://theprayer.diemutstrebe.com/
- **ELEVENPLAY** (2) — 由 MIKIKO 主导的舞团. 由编舞家 MIKIKO 领导的舞团，与 Rhizomatiks 打造的无人机、机器人和机器学习系统同台表演。
- **Edward Ihnatowicz** (2) — 雕塑家、机器人艺术先驱. 波兰裔英国雕塑家（1926–1988），做了 SAM（1968）和 The Senster（1970）这两件早期会回应人的计算机控制雕塑。 http://www.senster.com/
- **Elisa Giardina Papa** (2) — 艺术家. 意大利艺术家，影像作品研究数字经济与 AI 中的性别、照护与劳动。 https://www.elisagiardinapapa.org/
- **Emilio Vavarella** (2) — 艺术家、研究者. 意大利艺术家，常借自动图像系统的错误，研究人、技术与权力之间的关系。 https://emiliovavarella.com
- **Eryk Salvaggio** (2) — 批判性 AI 艺术家与研究者. 美国艺术家与作者，以故障影像和随笔探讨生成模型与档案。 https://www.cyberneticforests.com/
- **Eugenia Kuyda** (2) — Luka 与 Replika 创始人. 生于俄罗斯的记者和创业者，联合创办 AI 公司 Luka，并于 2017 年推出陪伴聊天机器人 Replika。 https://replika.com/
- **Fangting** (2) — 科幻作家；Uncommons 负责人. 独立科幻作家，与 Reality Design Lab 合写关于去中心化 AI 生命的思辨项目。
- **Gil Weinberg** (2) — 教授；佐治亚理工学院音乐技术中心创始主任. 以色列裔美国研究者，打造会聆听并即兴的机器人音乐家。 https://gtcmt.gatech.edu/
- **Hanson Robotics** (2) — 机器人公司（由 David Hanson 创立）. 由机器人学家 David Hanson 创立的公司，用弹性材料皮肤制作逼真的类人机器人头部，代表作有 BINA48 和 Sophia。 https://www.hansonrobotics.com/
- **Ho Tzu Nyen** (2) — 艺术家、电影导演. 新加坡艺术家，以电影、装置与算法作品交织东南亚的神话与历史。 https://en.wikipedia.org/wiki/Ho_Tzu_Nyen
- **Honghao Deng** (2) — 设计师与技术专家；Butlr 联合创始人. 毕业于哈佛设计研究生院和 MIT 媒体实验室，与李佳宝合作设计了《Twinkle》和《TransVision》。
- **Ian Cheng** (2) — 艺术家. 华裔美国艺术家，创作“实时模拟”：其中的智能体不断变化、没有结局的虚拟生态。 https://iancheng.com
- **James Vlahos** (2) — 记者；HereAfter AI 联合创始人. 美国记者，著有关于语音计算的《Talk to Me》（2019），为临终的父亲做了一个聊天机器人，之后联合创办 HereAfter AI。
- **Jason Edward Lewis** (2) — 康考迪亚大学计算艺术教授；原住民未来研究中心联合主任. 拥有切罗基、夏威夷和萨摩亚血统的数字媒体艺术家与诗人，主持“原住民协议与人工智能”工作组。 https://jasonlewis.org/
- **Jean Tinguely** (2) — 动态艺术家. 瑞士艺术家（1925–1991），他用废品拼成的哐当作响的机器会画画、演奏，甚至自我毁灭。 https://www.tinguely.ch/
- **Jenna Sutela** (2) — 艺术家. 芬兰艺术家，与微生物、黏菌和机器学习合作，探索超越人类的语言与认知。 https://jennasutela.com/
- **Jennifer Walshe** (2) — 作曲家、表演者；牛津大学作曲教授. 爱尔兰作曲家与歌手，作品融合扩展人声、虚构档案与 AI。 https://milker.org/
- **Jill Magid** (2) — 艺术家、作家. 美国艺术家，与警察、情报机构和闭路监控等权力系统建立亲密关系。 https://www.jillmagid.com/
- **Joanna Zylinska** (2) — 伦敦国王学院媒介哲学与批判性数字实践教授. 波兰裔英国写作者、艺术家与策展人，研究摄影、AI 与技术伦理。 https://www.joannazylinska.net
- **Jordan Wolfson** (2) — 艺术家. 美国艺术家（1980 年生），以关于暴力与注意力的电子动偶雕塑和虚拟现实作品知名。 https://www.davidzwirner.com/artists/jordan-wolfson
- **Joseph Weizenbaum** (2) — 计算机科学家，麻省理工学院（1923–2008）. 德裔美国计算机科学家，在麻省理工学院写出 ELIZA，后来成为最早从 AI 领域内部发出批评的人之一。 https://en.wikipedia.org/wiki/Joseph_Weizenbaum
- **Karen Palmer** (2) — 艺术家，自称“来自未来的讲故事者”. Karen Palmer 是英国艺术家，创作通过 AI、眼动追踪与面部分析回应观众情绪与视线的沉浸式电影。 https://karenpalmer.uk
- **Karl Sims** (2) — 计算机图形艺术家、研究者. 美国艺术家与研究者（1962 年生），以演化出的虚拟生物和交互演化装置闻名。 https://www.karlsims.com/
- **Kate Darling** (2) — 机器人伦理研究者，MIT 媒体实验室. 法学学者和研究者，研究人对机器人的共情以及社交机器人的政策问题；著有《The New Breed》（2021）。 http://www.katedarling.org
- **Ke Huang** (2) — 艺术家、设计师；清华大学研究生；Reality Design Lab 合作者. 设计师，主导 Reality Design Lab 的动态装置《Cybroc》和机器视觉装置《Body Oracle》。 https://reality.design/project/cybroc
- **Keiichiro Shibuya** (2) — 作曲家；ATAK 厂牌创办人. 作曲家，创作了没有人类歌手的歌剧：为初音未来写的《THE END》和为仿真人 Alter 写的《Scary Beauty》。 https://atak.jp/
- **Ken Feingold** (2) — 艺术家. 美国艺术家，自 1990 年代起制作会进行无剧本对话的“说话头像”雕塑。 https://www.kenfeingold.com/
- **Ken Rinaldo** (2) — 艺术家；俄亥俄州立大学艺术与技术荣休教授. 美国艺术家，自 20 世纪 80 年代末起创作跨物种机器人装置，让鱼、昆虫和细菌来驾驶或开关机器。 https://www.kenrinaldo.com/
- **Leonel Moura** (2) — 艺术家. 葡萄牙艺术家（1948 年生），自 2001 年起用成群的小型自主机器人作画。 https://www.leonelmoura.com/
- **Lev Manovich** (2) — 纽约市立大学研究生中心校级教授，文化分析实验室主任. 俄裔美国媒介理论家，著有《新媒体的语言》（2001）与《Cultural Analytics》（2020）。 http://manovich.net
- **Machine Listening (Sean Dockray, James Parker, Joel Stern)** (2) — 研究与艺术团体. 由 Sean Dockray、James Parker 与 Joel Stern 于 2020 年创立的协作研究与艺术实验平台，横跨写作、装置、表演、电台、软件与教学。 https://machinelistening.exposed/
- **Madeline Gannon** (2) — 艺术家、机器人研究者；ATONATON 创始人. 美国艺术家兼机器人研究者，给工业机器人加上感知与性格，让它们能与人共处一室。 https://atonaton.com/
- **Masahiro Mori** (2) — 机器人学家；东京工业大学名誉教授. 日本机器人学家（1927–2025），1970 年提出“恐怖谷”假说，并写作机器人与佛教的关系。
- **Merce Cunningham** (2) — 编舞家（1919–2009）. 美国编舞家，用偶然、影像以及（自 1989 年起）计算机软件来编舞。 https://www.mercecunningham.org/
- **N. Katherine Hayles** (2) — 加州大学洛杉矶分校杰出研究教授，杜克大学荣休教授. 美国文学与媒介理论家，研究控制论、后人类主义，以及人、动物与机器共有的非意识认知。
- **Nicolas Gourault** (2) — 艺术家、电影人. 法国艺术家，以纪录影像装置调查自动化视觉背后的人类劳动。 https://nicolasgourault.fr/
- **Norman White** (2) — 机器人艺术家；曾任教于安大略艺术设计学院与瑞尔森大学. 美裔加拿大艺术家（1938 年生），自 Ménage（1974）起制作有“行为”的机器人。
- **Nouf Aljowaysir** (2) — 艺术家、电影人. Nouf Aljowaysir 是常驻纽约的沙特艺术家，以摄影和影像创作，借与机器的对话探讨迁徙、历史与身份。 https://www.noufaljowaysir.com
- **Nye Thompson** (2) — 艺术家. 英国艺术家，构建软件系统来探讨机器视觉、监控网络与由机器生成的世界观。 https://nyethompson.net
- **Patrick Tresset** (2) — 艺术家. 法国艺术家，制作以刻意笨拙而执着的笔触为人画像的机器人。 https://patricktresset.com/
- **Paul Kaiser** (2) — 数字艺术家；OpenEndedGroup 联合创始人. 与 Shelley Eshkar（后与 Marc Downie）合作，把舞者的动作捕捉转化为手绘风格数字形象的艺术家。 https://openendedgroup.com/
- **Paula Gaetano Adi** (2) — 艺术家；罗德岛设计学院教授. 阿根廷艺术家，她的机器人关注“人工身体性”和安第斯宇宙技术，而不是人工智能。 https://www.paulagaetanoadi.com/
- **Random International** (2) — 由 Hannes Koch 与 Florian Ortkrass 创立的艺术团体. 创作关于行为与机器的装置的工作室。 https://www.random-international.com/
- **Rebecca Horn** (2) — 艺术家. 德国艺术家（1944–2024），从身体延伸装置转向带着忧郁气质、会自己动的机器与装置。 https://en.wikipedia.org/wiki/Rebecca_Horn
- **Rhizomatiks** (2) — 媒体艺术与技术工作室. 真锅大度等人 2006 年在东京创立的工作室，以与 ELEVENPLAY 合作的无人机、追踪与机器学习舞台作品著称。 https://rhizomatiks.com/en/
- **Rodney Brooks** (2) — 机器人学家，麻省理工学院荣休教授. 澳大利亚机器人学家，曾任麻省理工学院人工智能实验室及 CSAIL 主任，联合创办 iRobot、Rethink Robotics 与 Robust.AI。 https://rodneybrooks.com
- **Ron Wakkary** (2) — 西蒙菲莎大学交互艺术与技术学院教授，Everyday Design Studio 创始人. 设计研究者，制作 Morse Things、Tilting Bowl 这类“反事实”物件，并让人与它们长期共同生活，研究物与人如何共处。 http://eds.siat.sfu.ca/
- **Ross Goodwin** (2) — 创意技术专家、作家. 美国创意技术专家，制作能根据传感器输入和剧本语料写作的机器。 https://rossgoodwin.com/
- **Ruben Pater** (2) — 设计师. 荷兰平面设计师，作品关注政治、监控与设计伦理，著有《设计的政治》。 https://www.untold-stories.net/
- **Sarah Ciston** (2) — 诗人程序员、艺术家，科隆媒体艺术学院教授. 美国艺术家与研究者，以小志、聊天机器人、数据库和工具包探讨批判性与交叉性 AI。 https://sarahciston.com/
- **Seiko Mikami** (2) — 艺术家；多摩美术大学教授. 媒体艺术家（1961–2015），以大型互动装置探讨感知、监控与身体。 https://www.ntticc.or.jp/en/archive/participants/mikami-seiko/
- **Shelley Eshkar** (2) — 数字艺术家；OpenEndedGroup 联合创始人. 艺术家与动画师，与 Paul Kaiser 共同创作 BIPED 与 Ghostcatching。 https://openendedgroup.com/
- **Shu Lea Cheang** (2) — 艺术家、电影导演. 台裔美国网络艺术先驱，其电影与装置关注监控、性与数据。 https://en.wikipedia.org/wiki/Shu_Lea_Cheang
- **Simon Denny** (2) — 艺术家，汉堡美术学院教授. 新西兰艺术家，把科技公司、情报机构和加密货币的美学与意识形态搬上展台。 https://simondenny.net/
- **Simone C. Niquille** (2) — 设计师、研究者，technoflesh Studio. Simone C. Niquille 主持 technoflesh Studio，以影片和写作研究计算机视觉、三维扫描与合成训练数据集，并在埃因霍温设计学院创办 parametric truth Lab。 https://technofle.sh
- **Sony** (2) — 电子与娱乐公司. 日本公司，1999 年推出机器狗 AIBO，2018 年推出新一代 aibo。
- **Sun Yuan & Peng Yu** (2) — 艺术家组合. 自 1999 年起合作的北京艺术家组合，用机器、动物、身体与体液构建装置。 https://www.galleriacontinua.com/artists/sun-yuan-peng-yu-73
- **Takayuki Todo** (2) — 艺术家、机器人工程师. 制作能回应观者目光与表情的小型人形头部机器人。 https://www.takayukitodo.com/
- **Tega Brain** (2) — 艺术家、环境工程师，纽约大学综合数字媒体副教授. 出生于澳大利亚的艺术家和工程师，把基础设施、数据与“古怪工程”当作生态问题来处理。 https://tegabrain.com/
- **Terence Broad** (2) — 艺术家、研究者，伦敦艺术大学创意计算学院. 英国艺术家兼研究者，操控生成网络的内部结构，而非它们的数据。 https://terencebroad.com/
- **W. Grey Walter** (2) — 神经生理学家、控制论学者，布里斯托尔 Burden 神经学研究所. 美裔英国神经生理学家（1910–1977），从事脑电图研究，并在 1948–49 年造出最早的自主电子“乌龟”。
- **Wafaa Bilal** (2) — 艺术家；纽约大学 Tisch 艺术学院教授. 伊拉克裔美国艺术家，他的表演让身体暴露于远程、网络化的暴力与监视之下。 https://wafaabilal.com/
- **Wesley Goatley** (2) — 艺术家、研究者. 英国声音艺术家和研究者，装置作品探讨智能设备与数据的政治、生态和神话。 https://wesleygoatley.com/
- **William Odom** (2) — 西蒙菲莎大学交互艺术与技术学院副教授，Everyday Design Studio. 设计研究者，为日常生活制作“慢”的、长期使用的技术。
- **aaajiao** (2) — 媒体艺术家（徐文恺）. aaajiao 是艺术家、博主与程序员徐文恺的网络名，关注网络、软件与线上身份。 https://eventstructure.com
- **#NotABugSplat collective** (1) — 艺术家团体（与 Reprieve 和基本权利基金会合作）. 由巴基斯坦和美国艺术家组成的团体，在开伯尔-普赫图赫瓦省的田野里铺设了一幅无人机镜头可见的巨幅肖像。 https://notabugsplat.com/
- **AI Futures Project** (1) — 非营利预测研究机构. 由 Daniel Kokotajlo 领导的非营利机构，预测先进 AI 的发展与影响。 https://ai-2027.com/
- **Abeba Birhane** (1) — 认知科学家；都柏林圣三一学院助理教授. Abeba Birhane 是出生于埃塞俄比亚的认知科学家，审计大规模数据集，并从关系伦理角度研究 AI。 https://abebabirhane.com
- **Adam Ben-Dror** (1) — 设计师、艺术家. 新西兰设计师，在惠灵顿维多利亚大学与 Shanshan Zhou、Joss Doggett 一起做出有“性格”的台灯 Pinokio。
- **Adrian Chen** (1) — 记者. 美国记者，2014 年在《连线》发表的报道首次描述了全球内容审核员群体。 https://www.wired.com/2014/10/content-moderation/
- **Adrian Mackenzie** (1) — 澳大利亚国立大学社会学教授. 软件与数据社会学家，著有《Cutting Code》（2006）与《Machine Learners》（2017）。
- **Agnieszka Pilat** (1) — 艺术家. 生于波兰的画家，把 Boston Dynamics 的 Spot 机器人当作工作室伙伴与共同作画者。 https://www.agnieszkapilat.com/
- **Aidan Meller** (1) — 画廊主；Ai-Da 机器人项目发起人. 英国画廊主，2019 年与 Engineered Arts 合作推出类人“机器人艺术家”Ai-Da。 https://www.ai-darobot.com/
- **Akihiko Kondo** (1) — 学校职员；公开自称“虚构性恋”者. 2018 年与“住”在 Gatebox 装置中的虚拟歌手初音未来举行婚礼。
- **Alan Turing** (1) — 数学家、计算机科学家（1912–1954）. 英国数学家，1936 年提出通用计算机的模型，1950 年提出以“模仿游戏”检验机器智能。 https://www.turing.org.uk
- **Alessandro Ludovico** (1) — 艺术家，Neural 杂志主编. 意大利艺术家、研究者，媒体艺术杂志 Neural 的创刊主编。 https://neural.it
- **Alex Garland** (1) — 作家、电影导演. 英国小说家与电影人，执导了《机械姬》《湮灭》。 https://en.wikipedia.org/wiki/Alex_Garland
- **Alex Rivera** (1) — 电影人. 秘鲁裔美国电影人，以科幻片探讨移民、边境与劳动。 https://www.sleepdealer.com/
- **Alexandra Daisy Ginsberg** (1) — 艺术家，创作涉及合成生物学、自然保护与人工智能. Alexandra Daisy Ginsberg 是常驻伦敦的艺术家，作品追问人如何看待自然，从合成生物学思辨到为传粉昆虫而做的活体艺术。 https://www.daisyginsberg.com
- **Allison Koenecke** (1) — 计算社会科学家；康奈尔大学信息科学助理教授. 算法公平研究者，主导了第一项针对商用语音识别种族差异的大规模审计。
- **Alvin Lucier** (1) — 作曲家（1931–2021）. 美国实验作曲家，作品探索声音与身体的物理特性。 https://en.wikipedia.org/wiki/Alvin_Lucier
- **Amazon** (1) — 科技公司（Alexa 语音助手）. 美国科技公司，自 2014 年起通过 Alexa 语音助手和 Echo 音箱把一直在听的 AI 带进了千万家庭。 https://www.amazon.com/
- **Amelia Winger-Bearskin** (1) — 艺术家与技术人，佛罗里达大学 AI 与艺术讲席教授. 塞内卡-卡尤加族艺术家，研究面向技术、叙事与 AI 的原住民框架。 https://wampum.codes/
- **American Artist** (1) — 跨学科艺术家. 美国艺术家，依法将姓名改为 American Artist，作品关注黑人劳动、警务与技术。 https://americanartist.us/
- **Amy Alexander** (1) — 艺术家；加州大学圣地亚哥分校教授. 美国艺术家，以视听表演和软件艺术探讨机器与人如何观看媒介。 https://amy-alexander.com
- **Andrew Stanton** (1) — 皮克斯电影导演. 皮克斯的美国导演与编剧，执导了《海底总动员》和《机器人总动员》。 https://en.wikipedia.org/wiki/Andrew_Stanton
- **Andy Ayrey** (1) — 艺术家、AI 研究者. 新西兰艺术家，主持 Infinite Backrooms 实验并创造了 Truth Terminal 智能体。 https://x.com/AndyAyrey
- **Andy Clark** (1) — 萨塞克斯大学认知哲学教授. 英国哲学家，研究具身认知与延展认知，著有《Natural-Born Cyborgs》（2003）和《The Experience Machine》（2023）。
- **Angela Neubauer** (1) — 设计师. 来自维也纳应用艺术大学 Design Investigations 专业的设计师。
- **Anna Munster** (1) — 新南威尔士大学艺术与设计学院教授. 艺术家与理论家，研究网络、感知与机器视觉，著有《An Aesthesia of Networks》（2013）。
- **Anthropic** (1) — 人工智能研究公司. 开发 Claude 模型并发表可解释性研究的人工智能公司。 https://www.anthropic.com/
- **Anton Pidkuiko** (1) — 软件工程师. 工程师，2025 年在 ElevenLabs 黑客松上共同创作了 GibberLink。 https://github.com/PennyroyalTea/gibberlink
- **Auger-Loizeau** (1) — 设计合作组合（James Auger 与 Jimmy Loizeau）. 成立于 2000 年的英国批判设计组合，代表作有《Audio Tooth Implant》和《Afterlife》。
- **Bandai** (1) — 玩具公司，拓麻歌子制造商. 玩具公司，1996 年推出由真板亚纪与横井昭裕（WiZ）构想的拓麻歌子。
- **BeAnotherLab** (1) — 关于具身与共情研究的跨学科团体. 2012 年在巴塞罗那成立的团体，制作低成本具身系统，让人交换视角与身体。 https://beanotherlab.org/
- **Beijing E-Town** (1) — 北京经济技术开发区（主办方）. 北京的开发区与机器人产业聚集地，主办设有人形机器人并行赛道的亦庄半程马拉松。
- **Benjamin Bratton** (1) — 加州大学圣地亚哥分校技术哲学与思辨设计教授，Antikythera 项目主任. 美国理论家，研究星球尺度的计算，著有《The Stack》（2016）和《The Revenge of the Real》（2021）。
- **Benjamin Grosser** (1) — 艺术家；伊利诺伊大学厄巴纳-香槟分校教授. 美国艺术家，以软件和互动作品探讨计算对文化、社会与政治的影响。 https://bengrosser.com
- **Benjamin Maus** (1) — 设计师、艺术家. 德国设计师与艺术家，制作会分类、绘图与计算的机器和软件系统。 https://allesblinkt.com
- **Bernd Hopfengärtner** (1) — 设计师、艺术家. 德国设计师，通过影片与物件探讨近未来的消费技术。 https://berndhopfengaertner.net
- **Betti Marenko** (1) — 设计理论家，中央圣马丁学院. 生于意大利的设计理论家，写作关于万物有灵、不确定性与数字物件。
- **Bill Posters** (1) — 艺术家、研究者. 英国艺术家（化名），常与 Daniel Howe 合作，研究政治深度伪造、广告与数据影响产业。 https://billposters.ch/
- **Bill T. Jones** (1) — 编舞家；Bill T. Jones/Arnie Zane 舞团联合创始人. 美国编舞家与舞者，作品关注身体、种族、疾病与失去。 https://newyorklivearts.org/
- **Blake Lemoine** (1) — 前谷歌软件工程师. 曾在谷歌从事负责任 AI 工作的工程师，2022 年公开宣称 LaMDA 有感知。 https://en.wikipedia.org/wiki/LaMDA
- **Blanca Li** (1) — 编舞家、导演. 西班牙裔法国编舞家，跨舞蹈、电影与歌剧创作。 https://www.blancali.com/
- **Boris Petrovsky** (1) — 艺术家. 德国艺术家，用联网的日常机器与标识制作装置和表演性雕塑。 http://www.petrovsky.de
- **Boris Starkov** (1) — 软件工程师. 工程师，与 Anton Pidkuiko 共同创作了 GibberLink。 https://github.com/PennyroyalTea
- **Bot & Dolly** (1) — 机器人摄影与运动控制设计工程工作室（2013 年被谷歌收购）. 旧金山工作室，把工业机械臂用于电影与现场表演。
- **Brian House** (1) — 艺术家、研究者. 以声音、数据与环境感测为媒介的艺术家，把追踪、聆听与基础设施转化为可感知的节奏。 https://brianhouse.net/
- **Bruce Lacey** (1) — 艺术家、表演者、机器人制作者. 英国艺术家（1927–2016），20 世纪 60 年代用废品做出无政府主义式的人形机器人和表演。
- **Bruno Moreschi** (1) — 艺术家、研究者. 巴西艺术家兼研究者，质疑艺术机构及其分类体系，包括计算机视觉。 https://brunomoreschi.com
- **Bureau of Inverse Technology (BIT)** (1) — 艺术工程团体. 1990 年代初成立的匿名“信息机构”，成员包括 Natalie Jeremijenko 与 Kate Rich，制作用来监视监视者的装置。 https://bureauit.org
- **Byron Reeves** (1) — 斯坦福大学传播学教授. 传播学者，研究从电视到游戏与屏幕使用的媒介心理学。
- **Cap_able** (1) — 时尚科技初创公司（Rachele Didero、Federica Busani）. 由 Rachele Didero 与 Federica Busani 创立的意大利初创公司，生产带有对抗图案、可干扰 AI 人体与人脸检测的针织服装；构想始于 2019 年的纽约。 https://www.capable.design
- **Catherine D'Ignazio** (1) — 麻省理工学院城市科学与规划副教授，Data + Feminism Lab 主任. 学者、艺术家与软件开发者，研究女性主义数据实践与反数据。
- **Catie Cuan** (1) — 舞者、编舞家、机器人学家. 拥有斯坦福大学机械工程博士学位的编舞家，与工业机器人和社交机器人合作。 https://www.catiecuan.com/
- **Cesar & Lois (Cesar Baio, Lucy HG Solomon)** (1) — 艺术团体. 由 Cesar Baio 与 Lucy HG Solomon（The League of Imaginary Scientists）组成的团体，把微生物、网络与 AI 耦合成“生物—数字混合”系统。
- **Charlie Brooker** (1) — 编剧、《黑镜》主创. 英国讽刺作家和编剧，创作了单元剧《黑镜》（2011–）。 https://en.wikipedia.org/wiki/Charlie_Brooker
- **Chris Olah** (1) — Anthropic 可解释性研究者；Distill 联合创办人. 研究者，以直观、交互式地解释神经网络表征而闻名。 https://colah.github.io/
- **Chris Sanders** (1) — 动画导演. 美国动画师与导演，作品有《星际宝贝》《驯龙高手》和《荒野机器人》。 https://en.wikipedia.org/wiki/Chris_Sanders
- **Chris Sugrue** (1) — 艺术家、程序员. 美国艺术家与创意编程者，创作互动装置、人工生命与实验性界面作品。
- **Christian Moeller** (1) — 媒体艺术家；加州大学洛杉矶分校设计媒体艺术系教授. 德国出生的媒体艺术家，用传感器、摄像头和机器人制作互动装置与公共艺术。 https://christianmoeller.com
- **Christopher Kulendran Thomas** (1) — 艺术家. 泰米尔裔英国艺术家，常与 Annika Kuhlmann 合作，以 AI 与机器学习系统制作装置，探讨图像如何书写历史与政治。
- **Ciarán Cassidy** (1) — 纪录片导演. 爱尔兰纪录片导演。 https://fieldofvision.org/shorts/the-moderators
- **Claus Emmeche** (1) — 生物符号学家，哥本哈根大学. 丹麦理论生物学家，研究生物符号学、人工生命与涌现。
- **Clement Valla** (1) — 艺术家；任教于罗德岛设计学院. 法裔美国艺术家，研究由自动化系统和软件生成的图像与物件。 https://www.clementvalla.com
- **Coding Rights** (1) — 女性主义数字权利组织（由 Joana Varon 创立）. 巴西女性主导的组织，从跨女性主义和全球南方视角研究数据、监控与技术。 https://codingrights.org/
- **Coralie Vogelaar** (1) — 视觉艺术家. Coralie Vogelaar 是荷兰视觉艺术家，结合情绪识别软件、生物反馈与编舞，研究机器如何解码身体。 https://www.coralievogelaar.com
- **Cornell Creative Machines Lab** (1) — 由 Hod Lipson 领导的机器人实验室（现在哥伦比亚大学）. 研究具有自我意识、自我复制与创造性的机器的实验室。 https://www.creativemachineslab.com/
- **Craig Reynolds** (1) — 计算机图形研究者. 美国计算机科学家（1953 年生），1986–87 年创造了 Boids 群聚模型。 https://www.red3d.com/cwr/
- **Croteam** (1) — 电子游戏开发商. 克罗地亚游戏工作室，以《英雄萨姆》系列和《塔罗斯的法则》闻名。 https://www.croteam.com/
- **DARPA** (1) — 美国国防部高级研究计划局. 美国军方研究机构，资助并举办机器人竞赛，包括 DARPA 机器人挑战赛（2012–2015）。 https://www.darpa.mil/
- **Dadabots** (1) — 音乐 AI 二人组（CJ Carr、Zack Zukowski）. 用原始音频神经网络训练乐队与人声的二人组，以不停歇的 AI 金属乐直播闻名。 https://dadabots.com/
- **Dan Chen** (1) — 艺术家、工业设计师（罗德岛设计学院艺术硕士，MIT 媒体实验室）. 设计师，在罗德岛设计学院时期的“机器人亲密”系列中制作会抚摸、拥抱、安慰处于脆弱时刻之人的机器。 https://dankc.com
- **Dani Clode** (1) — 人体增强设计师；剑桥大学 Plasticity Lab 研究者. 设计义体与身体延伸装置的设计师，以“第三拇指”（Third Thumb）闻名。 https://www.daniclodedesign.com/
- **Daniel Coppen** (1) — 设计师；Playfool 联合创始人. 英国设计师，与木原共共同创立设计工作室 Playfool，创作游戏与互动装置。
- **Daniel Howe** (1) — 艺术家、程序员、教授. 美国艺术家与研究者，与 Helen Nissenbaum 合作开发了混淆工具 TrackMeNot 和 AdNauseam。 https://rednoise.org/daniel/
- **Danja Vasiliev** (1) — 艺术家、批判性工程师. 出生于俄罗斯、在柏林工作的艺术家，用网络、硬件与软件漏洞创作；《批判性工程宣言》合著者。 https://k0a1a.net
- **Dasha Ilina** (1) — 艺术家. 出生于俄罗斯、常驻巴黎的艺术家，用低技术的 DIY 物件和工作坊探讨数字设备与人体的关系。 http://centerfortechpain.com/
- **Dave Murray-Rust** (1) — 人与算法交互研究者；代尔夫特理工大学副教授. 计算机科学家与设计师（曾任职爱丁堡大学），研究人们如何与算法和机器人系统共处。
- **David Chalmers** (1) — 纽约大学哲学与神经科学教授. 澳大利亚哲学家，提出意识的“困难问题”，也研究虚拟世界与机器意识。
- **David Harris Smith & Frauke Zeller** (1) — 传播学研究者（麦克马斯特大学；多伦多都会大学）. 加拿大传播与媒介学教授，2013 年制作了 hitchBOT，作为检验人机信任的社会实验。 https://en.wikipedia.org/wiki/HitchBOT
- **David J. Gunkel** (1) — 北伊利诺伊大学媒介研究教授. 美国媒介哲学家，著有《The Machine Question》（2012）、《Robot Rights》（2018）和《Person, Thing, Robot》（2023）。
- **David Link** (1) — 艺术家、媒介考古学者. 德国艺术家与研究者，重建早期计算机与程序，例如 Ferranti Mark 1 和 Strachey 的情书生成器。 https://alpha60.de/
- **DeepBrain AI** (1) — AI 虚拟人公司. 韩国合成视频虚拟人公司，2022 年推出纪念服务 Re;memory。 https://www.deepbrain.io/
- **Desmond Paul Henry** (1) — 艺术家、哲学家（1921–2004）. 英国哲学讲师，1950–60 年代用轰炸瞄准器的模拟计算机制作绘画机器。 https://www.desmondhenry.com/
- **Diane Cescutti** (1) — 艺术家. 法国-塞内加尔艺术家，以织物、织机与计算机创作，通过编织知识重述计算的历史。
- **Domestic Data Streamers** (1) — 艺术与设计工作室. 2013 年成立于巴塞罗那的工作室，围绕数据、记忆和公共生活做参与式装置与研究。 https://www.domesticstreamers.com/
- **Don Ihde** (1) — 技术哲学家，纽约州立大学石溪分校荣休杰出教授. 美国哲学家，后现象学的创立者，研究技术如何塑造人的感知与行动。
- **Donna Haraway** (1) — 加州大学圣克鲁兹分校意识史系杰出荣休教授. 女性主义科学技术学者，著有《赛博格宣言》《当物种相遇》和《与麻烦共存》。
- **Driessens & Verstappen** (1) — 艺术家二人组（Erwin Driessens 与 Maria Verstappen）. 荷兰二人组，自 1990 年起用生成系统、人工生命和机器人创造形态与感受。
- **Ei Wada** (1) — 艺术家、音乐人；Electronicos Fantasticos! 发起人. 把显像管电视、电风扇、条码扫描器等淘汰家电改造成乐器，由社区乐团演奏。 https://www.electronicosfantasticos.com/en/
- **Electric Circus** (1) — 机器人街头剧团（Mirjam Langemeijer 与 Fred Abels）. 木偶师 Mirjam Langemeijer 与发明家 Fred Abels 的合作，把电子动画技术与木偶戏结合成逼真的机器人街头角色。 http://www.electric-circus.eu
- **Emanuel Andel** (1) — 艺术家. 奥地利媒体艺术家，制作由生物信号驱动、带有风险的人机游戏。
- **Emily M. Bender** (1) — 华盛顿大学语言学教授. 计算语言学家，主持华盛顿大学计算语言学实验室，合著《The AI Con》（2025）。
- **Engineered Arts** (1) — 人形机器人公司. 由 Will Jackson 创立的英国公司，制作 RoboThespian、Ameca 等娱乐用人形机器人。 https://www.engineeredarts.co.uk/
- **Eric Paulos** (1) — 加州大学伯克利分校电子工程与计算机科学系教授；Hybrid Ecologies Lab 主任. 人机交互研究者，1990 年代制作早期远程在场机器人，后来投身批判性制作。 https://www.paulos.net/
- **Esther Hovers** (1) — 艺术家、摄影师. 荷兰艺术家，以摄影和装置研究公共空间中的监控、权力与“正常行为”规范。 https://www.estherhovers.com
- **Eszter Zwickl** (1) — 设计师. 来自维也纳应用艺术大学 Design Investigations 专业的设计师。
- **Etsuko Ichihara** (1) — 媒体艺术家. 日本媒体艺术家，把民俗仪式与习俗同机器人、VR、人脸识别等技术结合。 https://etsuko-ichihara.com
- **Everest Pipkin** (1) — 艺术家、游戏设计师、写作者. Everest Pipkin 创作游戏、软件、绘画，并把数据集本身当作作品，长期书写机器学习语料的伦理问题。 https://everest-pipkin.com
- **Evolving AI Lab** (1) — 研究实验室（Jeff Clune），怀俄明大学. Jeff Clune 在怀俄明大学领导的实验室，研究进化算法与深度学习；成员 Anh Nguyen 与 Jason Yosinski 合著了“欺骗图像”论文。
- **Facebook AI Research (FAIR)** (1) — Meta 旗下的人工智能研究实验室. Meta 于 2013 年成立的基础人工智能研究实验室。 https://ai.meta.com/
- **Felix Lenz** (1) — 设计师、电影人. 毕业于维也纳应用艺术大学 Design Investigations 专业的设计师与电影人，关注技术的物质代价与人的代价。
- **Filipe Vilas-Boas** (1) — 艺术家. 常驻巴黎的葡萄牙艺术家，创作关于数字生活、监控与机器人的装置。 https://www.filipevilasboas.com/
- **Francesca Panetta** (1) — 沉浸式艺术家、记者；曾任麻省理工学院高级虚拟中心 XR 创意总监. 英国沉浸式记者和艺术家，曾任《卫报》虚拟现实负责人。 https://moondisaster.org/
- **Frank Kolkman** (1) — 设计师、研究者. Frank Kolkman 是荷兰设计师，关注 DIY 医疗与技术；他的 Designs for Flies 获得 2016 年荷兰设计奖“服务与系统”类奖项。 http://www.frankkolkman.nl
- **Frank Lantz** (1) — 游戏设计师；纽约大学游戏中心创始主任. 美国游戏设计师，研究游戏作为一种审美形式。 https://www.decisionproblem.com/paperclips/
- **François Pachet** (1) — AI 与音乐研究者；索尼计算机科学实验室巴黎分部前主任. 法国计算机科学家，开发会学习风格的互动音乐系统。 https://www.francoispachet.fr/
- **Frieder Weiss** (1) — 媒体艺术家、软件开发者（Kalypso）. 为舞蹈编写实时摄像追踪软件的德国工程师兼艺术家。
- **Fritz Heider** (1) — 心理学家（1896–1988）. 奥地利出生的社会心理学家，先后任教于史密斯学院与堪萨斯大学，归因理论的奠基者。
- **Future of Life Institute / Stop Autonomous Weapons** (1) — 关注技术生存风险的非营利组织. 非营利组织，与 Stuart Russell 等 AI 研究者一道推动禁止致命性自主武器。 https://futureoflife.org/
- **Félix Luque Sánchez** (1) — 艺术家. 常驻布鲁塞尔的西班牙艺术家，以机器人与算法装置探讨混沌、控制与机器自主性。
- **GROOVE X** (1) — 机器人公司，LOVOT 制造商. 林要于 2015 年创立的公司，制造只为“被爱”而设计的机器人 LOVOT。 https://lovot.life/en/
- **Gabriel Pereira** (1) — 研究者. 巴西研究者，研究计算机视觉与批判性数据实践。
- **Gabriele Trovato** (1) — 机器人学者；日本芝浦工业大学副教授. 意大利机器人学者，研究文化、宗教与机器人设计；他制作了外形像天主教圣像的机器人 SanTO。
- **Gan Golan** (1) — 艺术家. 美国艺术家，创作公共介入行动与可穿戴雕塑。
- **Garnet Hertz** (1) — 艺术家、设计研究者；Emily Carr 大学设计与媒体艺术加拿大研究讲席. 加拿大艺术家与研究者，以批判性制作、DIY 电子，以及他在 UC Irvine 读研时做的蟑螂驾驶机器人而知名。 http://www.conceptlab.com/
- **Gaëtan Robillard** (1) — 艺术家、研究者. 法国艺术家，以计算、数据与声音探讨算法如何建模知识，题材从气候谣言到认知。
- **Geocinema** (1) — 艺术团体. 由 Asia Bazdyrieva 与 Solveig Suess 创立（早期项目有 Alexey Orlov 参与）的团体，把行星级传感网络视为一台分布式摄像机。 https://geocinema.network
- **George E. Lewis** (1) — 作曲家、长号手、学者；哥伦比亚大学教授. 美国作曲家、AACM 成员，自 1970 年代末创作互动计算机音乐。 https://music.columbia.edu/bios/george-e-lewis
- **Giacomo Miceli** (1) — 艺术家、软件工程师. 意大利艺术家与工程师，用合成声音和生成文本制作网络作品。 https://www.infiniteconversation.com/
- **Gideon Obarzanek** (1) — 编舞家；Chunky Move 舞团创始人. 澳大利亚编舞家，1995 年创立 Chunky Move，与 Frieder Weiss 合作创作互动影像舞蹈。 https://chunkymove.com.au/
- **Gilbert Simondon** (1) — 哲学家（1924–1989）. 法国哲学家，研究个体化与技术；1958 年的博士论文描述了技术物如何演化，并与人共同构成环境。
- **Golan Levin** (1) — 艺术家；卡内基梅隆大学教授，STUDIO for Creative Inquiry 主任. Golan Levin 创作互动装置、表演与软件，探索计算机视觉、手势与交流。 https://www.flong.com
- **Gonçalo F. Cardoso** (1) — 作曲家、声音艺术家；唱片厂牌 Discrepant 创始人. 葡萄牙作曲家、田野录音者，经营实验厂牌 Discrepant。
- **Goodby Silverstein & Partners** (1) — 广告公司. 旧金山广告公司，为佛罗里达州圣彼得堡的达利博物馆制作了 Dalí Lives。 https://goodbysilverstein.com/
- **Google Creative Lab** (1) — 谷歌创意团队. 谷歌内部的创意团队，制作面向公众的机器学习实验，包括 Teachable Machine。 https://experiments.withgoogle.com/
- **Google DeepMind** (1) — 人工智能研究实验室. 2010 年在伦敦成立、2014 年被谷歌收购的人工智能实验室，AlphaGo 的开发者。 https://deepmind.google/
- **Gordon Pask** (1) — 控制论学者、发明家、会话理论提出者. 英国控制论学者（1928–1996），做过会学习、会“对话”的机器，从 Musicolour（1953）到 Colloquy of Mobiles（1968）。
- **Graham Dove** (1) — 人机交互研究者. 英国人机交互研究者，研究如何用数据与机器学习做设计。 https://doi.org/10.1145/3025453.3025739
- **Halsey Burgund** (1) — 声音艺术家、技术专家. 美国声音艺术家，利用位置与语音技术制作参与式声音作品。 https://halseyburgund.com/
- **Hans Block** (1) — 导演、剧场创作者. 德国导演，与 Moritz Riesewieck 合作创作关于数字权力的电影和戏剧。 https://en.wikipedia.org/wiki/The_Cleaners_(2018_film)
- **Hans Block & Moritz Riesewieck** (1) — 纪录片导演（Laokoon）. 德国导演二人组，作品有关于内容审核员的《网络清道夫》（2018）和关于数字来世产业的《Eternal You》（2024）。 https://en.wikipedia.org/wiki/Eternal_You
- **Happiest Baby (Harvey Karp)** (1) — 机器人摇篮 SNOO 的制造公司，由儿科医生 Harvey Karp 创办. 婴儿用品公司，把 Harvey Karp 的安抚方法（包裹、白噪音、摇晃）做成由传感器驱动的摇篮。 https://www.happiestbaby.com
- **Harold Cohen** (1) — 画家、AI 艺术先驱（1928–2016）. 生于英国的画家，自 1973 年起编写并发展绘画程序 AARON，直至去世。 https://aaronshome.com/
- **Harpreet Sareen** (1) — 设计师、研究者；帕森斯设计学院教授. 印度出生的设计师与研究者，在麻省理工学院媒体实验室发展了“赛博植物学”。
- **Hasan Elahi** (1) — 艺术家，乔治梅森大学教授. 孟加拉裔美国艺术家，在被误列入美国恐怖分子观察名单后开始追踪并公开自己的生活。 https://en.wikipedia.org/wiki/Hasan_Elahi
- **Heather Knight** (1) — 机器人学家；俄勒冈州立大学助理教授（CHARISMA 实验室）. 社交机器人学家，创立 Marilyn Monrobot，借剧场与喜剧研究机器人的表现力。 https://www.marilynmonrobot.com/
- **Helena Nikonole** (1) — 艺术家、策展人. Helena Nikonole 是新媒体艺术家，创作涉及人工智能、生物艺术和 DIY 生物技术。 https://nikonole.com/
- **Huang Yi** (1) — 编舞家、舞者、发明者. 台湾编舞家，亲自为工业机器人编程，创立黄翊工作室＋。 https://huangyistudio.com/
- **Hubert Dreyfus** (1) — 哲学家，加州大学伯克利分校教授（1929–2017）. 美国哲学家，借用海德格尔与梅洛-庞蒂论证：符号主义 AI 无法捕捉具身的、情境中的实践知识。
- **Hugh Herr** (1) — 生物物理学家；MIT 媒体实验室生物机电组负责人. 攀岩者和工程师，1982 年失去双腿小腿，现设计带动力的仿生肢体。 https://www.media.mit.edu/people/hherr/overview/
- **Human Computer Integration Lab (University of Chicago)** (1) — 由 Pedro Lopes 领导的人机交互实验室. 研究把计算机与身体整合的设备的实验室，从肌肉电刺激到可穿戴干扰器。 https://lab.plopes.org/
- **Humanising Autonomy (Maya Pindeus, Leslie Nooteboom, Raunaq Bose, Adam Bernstein)** (1) — 英国皇家艺术学院与帝国理工创新设计工程专业的设计团队，后成立为伦敦初创公司. 四位研究生设计师，先做出行人与自动驾驶汽车之间双向沟通的界面 Blink，随后以行人行为 AI 为方向创办公司。
- **Ian Bogost** (1) — 游戏设计师、哲学家，圣路易斯华盛顿大学教授. 美国游戏设计师与物导向哲学家，著有《Persuasive Games》（2007）和《Alien Phenomenology》（2012）。
- **Intuition Robotics** (1) — 陪伴机器人 ElliQ 的制造公司. 2016 年成立的以色列公司，为老年人开发会主动搭话的 AI 陪伴设备；ElliQ 与 Yves Béhar 的 fuseproject 合作设计。 https://elliq.com
- **Iohanna Nicenboim** (1) — 代尔夫特理工大学设计师与研究者，研究超越人类设计与人工智能. 设计研究者，把语音助手和 AI 看作超越人类的行动者，并设计与它们的情境化对话。 https://iohanna.com/
- **Iris Long** (1) — 艺术家、策展人、研究者. 中国艺术家与策展人，关注数据、机器感知与算法政治。
- **Isa Willinger** (1) — 纪录片导演、作者. 德国纪录片导演（1980 年生）。处女作《Hi, AI》（2019）获马克斯·奥菲尔斯电影节最佳纪录片奖。 https://en.wikipedia.org/wiki/Isa_Willinger
- **Ivan Henriques** (1) — 艺术家. 巴西艺术家，制作把植物、微生物与机器人连接起来的混合机器。
- **J. C. R. Licklider** (1) — 心理学家、计算机科学家（1915–1990）. 麻省理工学院与 BBN 的心理声学家，任美国高级研究计划署信息处理技术办公室主任时资助了交互式计算，以及后来通向互联网的网络研究。
- **Jack Burnham** (1) — 艺术评论家、理论家（1931–2019）. 美国评论家、西北大学教授，写有《Systems Esthetics》（Artforum，1968），并策划展览 Software（犹太博物馆，1970）。
- **Jacques de Vaucanson** (1) — 发明家、自动机制作者. 法国发明家（1709–1782），造过逼真的自动机，也发明了自动织布机。
- **Jaha Koo** (1) — 剧场创作者、作曲家与录像艺术家. 韩国剧场创作者，其纪实表演结合音乐、影像、自传与技术物件。 https://en.wikipedia.org/wiki/Jaha_Koo
- **Jake Schreier** (1) — 电影导演. 美国音乐录影带和电影导演，《机器人与弗兰克》（2012）是他的首部长片。 https://en.wikipedia.org/wiki/Jake_Schreier
- **James Pierce** (1) — 设计研究者；华盛顿大学教授. 美国设计研究者，以“反功能”设计和关于智能家居摄像头的批判性研究著称。
- **Jan Zuiderveld** (1) — 艺术家. 荷兰艺术家，为日常家电装上传感器和 AI，让它们开口回应，并按自己的方式行事。
- **Janelle Shane** (1) — 光学研究科学家；AI Weirdness 作者. 研究者与作者，面向大众记录神经网络的古怪行为。 https://www.aiweirdness.com/
- **Jasia Reichardt** (1) — 策展人、作家，伦敦当代艺术学院前副馆长. 波兰出生的英国策展人，策划“控制论的偶然”（ICA，1968），著有《Robots: Fact, Fiction and Prediction》（1978）。
- **Jason Rohrer** (1) — 游戏设计师、程序员. 美国独立游戏设计师，以《Passage》（2007）、《The Castle Doctrine》等艺术游戏和聊天服务 Project December 闻名。 https://projectdecember.net/
- **Jed Berk** (1) — 艺术家、设计师. 美国艺术家，以“自主轻型飞艇”（ALAVs）闻名：会成群飞行、避开障碍、寻找同伴的小型飞艇机器人。
- **Jeff Sebo** (1) — 哲学家；纽约大学心灵、伦理与政策中心主任. 美国哲学家，研究动物与 AI 伦理以及非人类心智的道德地位。 https://jeffsebo.net/
- **Jem Finer** (1) — 音乐人、艺术家. 英国音乐人（The Pogues 创始成员）与艺术家，以超长时长和深时间为创作主题。 https://longplayer.org/
- **Jemima Wyman** (1) — 艺术家. 澳大利亚艺术家，以绘画、织物和影像研究伪装、面具与集体抗议图像。 https://www.jemimawyman.com/
- **Jennifer A. Lewis** (1) — 材料科学家；哈佛大学教授. 美国材料科学家，以软材料和功能材料的 3D 打印闻名。
- **Jennifer Lyn Morone** (1) — 艺术家. 美国艺术家，把自己注册成一家公司，资产是她自己的数据、健康与技能。 https://jenniferlynmorone.com/
- **Jennifer Rhee** (1) — 弗吉尼亚联邦大学英语系教授. 研究技术、文学与艺术的学者，著有《The Robotic Imaginary》（2018）。
- **Jia Deng** (1) — 计算机科学家；普林斯顿大学副教授. 邓嘉是计算机视觉研究者，读博期间在李飞飞指导下主导构建了 ImageNet 数据集。
- **Jibo, Inc.** (1) — 社交机器人公司（2012–2019）. 由麻省理工机器人学者辛西娅·布雷齐尔联合创办的初创公司，2017 年起销售面向家庭的桌面社交机器人 Jibo，后来公司倒闭。 https://en.wikipedia.org/wiki/Cynthia_Breazeal
- **Jill Walker Rettberg** (1) — 卑尔根大学数字文化教授，数字叙事中心联合主任. 挪威数字文化学者，主持欧洲研究理事会项目“日常生活中的机器视觉”及其收录 500 件创作的数据库。 https://jilltxt.net
- **Jing-cai Liu** (1) — 设计师. 中国设计师，以可穿戴设备追问隐私与人脸识别。 http://jingcailiu.com
- **Joaquín Fargas** (1) — 艺术家、工程师，Proyecto Biosfera 负责人. 阿根廷艺术家，以艺术、科学与技术回应气候与生命议题，作品包括封闭生物圈和南极机器人。 https://www.joaquinfargas.com
- **Joel Krueger** (1) — 哲学家，埃克塞特大学. 心灵哲学家，研究现象学、情绪、音乐以及延展与社会心智。
- **Johann Diedrick** (1) — 艺术家、工程师；纽约大学 ITP 兼职教授. 艺术家与工程师，通过装置、表演、软件与工作坊营造“聆听空间”，在纽约大学 ITP 教授声音艺术与聆听机器；2021 年 Mozilla 创意媒体奖得主。 http://johanndiedrick.com/
- **John McCarthy** (1) — 计算机科学家（1927–2011）. 计算机科学家，在 1955 年达特茅斯提案中首创“人工智能”一词，发明 Lisp 语言，创立斯坦福人工智能实验室。
- **John Searle** (1) — 心灵哲学家，曾任教于加州大学伯克利分校. 美国语言与心灵哲学家，以言语行为理论和“中文屋”论证（1980）著称。
- **Johns Hopkins Applied Physics Laboratory** (1) — 大学附属研究实验室. 约翰斯·霍普金斯大学的研究实验室，20 世纪 60 年代初工程师在这里造出了会自己充电的移动自动机“野兽”。 https://www.jhuapl.edu/
- **Jon McCormack** (1) — 艺术家；莫纳什大学教授、SensiLab 主任. 澳大利亚艺术家与研究者，研究生成艺术与人工生命。 https://www.jonmccormack.info/
- **Jon Rafman** (1) — 艺术家、影像创作者. 加拿大艺术家，以录像、装置和网络上的现成图像进行创作。 https://jonrafman.com
- **Jonas Simmerlein** (1) — 神学家、哲学家，维也纳大学. 维也纳大学神学家、讲道学讲师；他为 2023 年德国新教教会大会设计了一场大部分由 ChatGPT 撰写的礼拜。
- **Jonas Voigt** (1) — 设计师. 德国设计师，与 Stephan Bogner、Philipp Schmitt 合作 Raising Robotic Natives。
- **Joon Sung Park** (1) — 斯坦福 HCI 小组计算机科学家. HCI 研究者，领导了用大语言模型模拟人类行为的“生成式智能体”项目。 https://www.joonsungpark.com/
- **Joseph Sargent** (1) — 电影与电视导演（1925–2014）. 美国电影和电视导演，作品包括《巨人：福宾计划》。 https://en.wikipedia.org/wiki/Joseph_Sargent
- **Josh Begley** (1) — 艺术家、电影人. 美国数据艺术家与电影人，作品记录美国的无人机空袭、监狱与警务。 https://joshbegley.com/
- **Jules LaPlace** (1) — 艺术家、软件开发者. 艺术家、程序员，与 Adam Harvey 合作开发了 MegaPixels 与 Exposing.ai 的网站和搜索引擎。
- **Julia Vollmer** (1) — 艺术家、设计师. 德国艺术家与设计师，用材料装置让数字系统的物理与能源代价变得可感。 https://juliavollmer.de
- **Julian Charrière** (1) — 艺术家. 瑞士裔法国艺术家，以雕塑、电影和考察处理地质、开采与深时间。 https://julian-charriere.net/
- **Julie Carpenter** (1) — 人机交互研究者. 美国研究者，研究人如何对机器人和 AI 产生依恋，起点是她 2013 年在华盛顿大学对排爆部队的研究。 https://jgcarpenter.com/
- **Julien Prévieux** (1) — 艺术家；2014 年马塞尔·杜尚奖得主. Julien Prévieux 是法国艺术家，以影像、表演与绘画研究身体与姿势如何被技术系统测量、申请专利与优化。 https://www.previeux.net
- **Julius Popp** (1) — 艺术家. 德国艺术家（1973 年生），创作关于信息与自组织的机器，最知名的是 bit.fall。
- **Justine Emard** (1) — 结合神经科学、机器人和机器学习的视觉艺术家. 法国艺术家，结合摄影、影像、机器人和人工智能；作品数据来自蜜蜂、大脑和仿人机器人。 https://justineemard.com
- **K Allado-McDowell** (1) — 作家、音乐人；谷歌 Artists + Machine Intelligence 项目创办人. 作家与艺术家，与大语言模型合写了数本书，并主持过谷歌的 Artists + Machine Intelligence 项目。 https://www.kalladomcdowell.com/
- **Kacie Kinzer** (1) — 设计师、互动艺术家. 设计师（纽约大学 ITP），她的纸板机器人 Tweenbots 被纽约现代艺术博物馆收藏。 http://www.tweenbots.com
- **Kai-Fu Lee** (1) — 计算机科学家、投资人；创新工场创始人. 生于台湾的计算机科学家，曾任谷歌中国总裁，著有《AI 新世界》。
- **KairUs** (1) — 艺术家组合（Linda Kronman 与 Andreas Zingerle）. 研究监控、智慧城市与机器视觉背后隐藏劳动的艺术家组合。 https://kairus.org
- **Karel Čapek** (1) — 作家、剧作家（1890–1938）. 捷克作家，他的剧本 R.U.R. 让“robot”（机器人）一词进入世界语言，这个词由他的哥哥 Josef 提议。 https://en.wikipedia.org/wiki/Karel_%C4%8Capek
- **Karolina Sobecka** (1) — 艺术家. 出生于波兰的艺术家，创作涉及互动、动画与环境系统。
- **Katarzyna Nowaczyk-Basińska** (1) — 剑桥大学未来智能研究中心研究员. 研究数字永生，以及围绕死亡与技术的文化实践。 https://www.lcfi.ac.uk/
- **Kathleen Richardson** (1) — 德蒙福特大学机器人与 AI 伦理与文化教授. 英国机器人人类学学者，2015 年发起“反对性爱机器人运动”。 https://campaignagainstsexrobots.org/
- **Katja Novitskova** (1) — 艺术家. 爱沙尼亚艺术家，作品关注技术、成像与生物学如何呈现生命；2017 年代表爱沙尼亚参加威尼斯双年展。 https://www.katjanovitskova.com
- **Kazuhiko Hachiya** (1) — 艺术家；东京艺术大学教授. 媒体艺术家，代表作包括《Inter Dis-Communication Machine》、电子邮件宠物软件 PostPet 和 OpenSky 滑翔机计划。 https://www.ntticc.or.jp/en/archive/works/inter-dis-communication-machine/
- **Keiichi Matsuda** (1) — 设计师、电影人. 英日混血的设计师与电影人，其影片想象被增强现实全面覆盖的城市。 http://km.cx
- **Kelly Heaton** (1) — 艺术家. 美国艺术家，曾用拆开的电子玩具做成毛皮，后来创作“电子自然主义”电路作品。
- **Kenneth Colby** (1) — 精神科医生、AI 研究者，斯坦福大学与加州大学洛杉矶分校（1920–2001）. 美国精神科医生，用计算机模拟神经症与偏执，写出了聊天机器人 PARRY。 https://en.wikipedia.org/wiki/Kenneth_Colby
- **Kevin Eykholt** (1) — 计算机安全研究者（密歇根大学博士）. 安全研究者，在密歇根大学期间作为第一作者发表了用贴纸让分类器误读停车标志的研究。
- **Kevin Warwick** (1) — 控制论研究者；考文垂大学与雷丁大学荣休教授. 英国工程师，先后植入 RFID 芯片（1998）和神经电极阵列（2002），把自己的神经系统接入计算机。 https://en.wikipedia.org/wiki/Kevin_Warwick
- **Kim Jee-woon** (1) — 电影导演、编剧. 韩国类型片导演，作品包括《蔷花，红莲》《看见恶魔》。 https://en.wikipedia.org/wiki/Kim_Jee-woon
- **Kim Tae-yong** (1) — 电影导演. 韩国导演，作品有《晚秋》《奇迹乐园》。 https://en.wikipedia.org/wiki/Kim_Tae-yong
- **Kit Galloway & Sherrie Rabinowitz** (1) — 艺术家二人组；Electronic Cafe International 创始人. Kit Galloway 与 Sherrie Rabinowitz（1950–2013）自 1970 年代起创作卫星与视频远程通信艺术。 http://www.ecafe.com/
- **Knightscope** (1) — 安保机器人公司. 2013 年成立的美国公司，在商场、停车场和办公楼部署自主安保机器人。 https://www.knightscope.com/
- **Kogonada** (1) — 电影导演、视频散文作者. 生于韩国的美国导演，以关于电影形式的视频散文，以及长片《哥伦布》（2017）和《杨之后》（2021）闻名。 https://en.wikipedia.org/wiki/Kogonada
- **Kory Mathewson** (1) — AI 研究者、即兴演员；Improbotics 联合创始人. 加拿大研究科学家，构建会即兴的对话代理，并联合创立 Improbotics。 https://improbotics.org/
- **Kraftwerk** (1) — 乐队（由 Ralf Hütter 与 Florian Schneider 创立）. 1970 年成立的德国电子乐队，其形象与声音把音乐人与机器融为一体。 https://kraftwerk.com/
- **Krzysztof Wodiczko** (1) — 艺术家；哈佛大学设计研究生院驻院教授. Krzysztof Wodiczko 是波兰出生的艺术家，以大型公共投影及为边缘群体发声的“工具”作品闻名。
- **Kōdai-ji** (1) — 京都临济宗禅寺. 京都一座有四百年历史的禅寺，与大阪大学合作委托制作了仿真人观音 Mindar。 https://www.kodaiji.com/mindar/
- **Kōfuku-ji (Isumi)** (1) — 千叶县夷隅市的佛教寺院. 自 2015 年起，住持 Bungen Oi 与维修公司 A-FUN 合作，在这里为损坏的 AIBO 机器狗举行供养法会。
- **L.A. Raeven** (1) — 艺术家二人组（双胞胎姐妹 Liesbeth 与 Angelique Raeven）. 荷兰双胞胎姐妹，其装置与表演审视身体规范、相似性与身份。
- **Laetitia Sonami** (1) — 声音艺术家、作曲家. 生于法国的作曲家，以戴着 Lady's Glove 表演电子音乐著称，后来又使用机器学习乐器。 https://sonami.net/
- **Lancel & Maat** (1) — 艺术家组合（Karen Lancel 与 Hermen Maat）. 荷兰艺术家组合，以参与式装置探讨网络化与被监控空间中的触碰、信任与在场。 https://lancelmaat.nl
- **Laura Kikauka** (1) — 艺术家、动态环境创作者. 加拿大艺术家，以堆满旧电子物件、充满幽默的环境装置和她的 Funny Farm 工作室闻名。
- **Lauren F. Klein** (1) — 埃默里大学英语与定量理论方法教授. 数字人文学者，研究数据可视化、早期美国文学与女性主义数据科学。
- **Laurie Anderson** (1) — 艺术家、音乐人、表演者. 美国艺术家，自 1970 年代起以变声器、电子乐器与多媒体表演闻名。 https://laurieanderson.com/
- **Leandro Núñez** (1) — 艺术家（Leo Núñez）. 阿根廷艺术家，创作涉及机器人、人工生命与生成系统。 https://www.leonunez.com.ar/
- **Lee Bul** (1) — 艺术家. 韩国艺术家，横跨表演、雕塑与装置，关注技术、性别、乌托邦与身体。 https://en.wikipedia.org/wiki/Lee_Bul
- **Leo Selvaggio** (1) — 跨领域艺术家. 常驻芝加哥的跨领域艺术家（Leonardo Selvaggio），他关于监控的项目邀请公众佩戴、扮演或“黑入”他的身份。 https://www.leoselvaggio.com
- **Liam Young** (1) — 思辨建筑师、电影人. 生于澳大利亚的建筑师，拍摄关于被自动化、无人机与机器视觉塑造的城市的电影。 https://liamyoung.org/
- **Libby Heaney** (1) — 艺术家、量子物理学家. 英国艺术家，拥有量子物理博士学位，创作涉及机器学习与量子计算。 https://libbyheaney.co.uk/
- **Lilly Irani** (1) — 加州大学圣地亚哥分校传播学副教授. 美国学者、前谷歌设计师，研究众包劳动、创新与设计政治。 https://quote.ucsd.edu/lirani/
- **Lisa Feldman Barrett** (1) — 心理学家、神经科学家；美国东北大学校级杰出教授. Lisa Feldman Barrett 是加拿大裔美国心理学家，以“情绪建构论”闻名。 https://lisafeldmanbarrett.com
- **Liu Chuang** (1) — 艺术家. 中国艺术家，其影像追踪劳动、土地与基础设施如何被经济与技术变化重组。
- **Longquan Monastery** (1) — 北京佛教寺院. 位于北京凤凰岭的佛教寺院，以熟悉科技的僧人与义工团队著称。
- **Louise Crnkovic-Friis** (1) — 编舞家；Peltarion 联合创始人. 瑞典编舞家，用自己的舞蹈训练神经网络，生成新的编舞。
- **Loïs Soleil** (1) — 艺术家. 常驻布鲁塞尔的艺术家，结合机器人、AI 与女性主义防身实践进行创作。 http://loissoleil.com
- **Luciana Parisi** (1) — 杜克大学文学与计算媒介、艺术和文化项目教授. 意大利计算哲学家，曾任教于伦敦大学金史密斯学院文化研究中心，著有《Contagious Architecture》（2013）。
- **Lucy Osler** (1) — 哲学家，埃克塞特大学. 哲学家，研究现象学、共情以及我们如何在网络中经验他人。
- **Lucy Suchman** (1) — 兰卡斯特大学科学技术人类学荣休教授. 人类学家，曾在施乐帕洛阿尔托研究中心工作二十年，著有《Plans and Situated Actions》（1987）。
- **Luka Crnkovic-Friis** (1) — 机器学习工程师；Peltarion 联合创始人. 瑞典 AI 工程师，与 Louise Crnkovic-Friis 合作构建 chor-rnn 模型。
- **Lydia H. Liu** (1) — 哥伦比亚大学谭维信人文讲席教授. 媒介与翻译理论家、比较文学学者。
- **M Eifler** (1) — 从事具身交互与计算义体研究的艺术家、研究者. 跨学科艺术家（2011 年获加州艺术学院 MFA），以自身残障经验为出发点制作思辨界面与义体系统。
- **M. Beatrice Fazi** (1) — 萨塞克斯大学计算哲学学者. 计算哲学家，研究计算与 AI 系统中的美学、抽象与不确定性。
- **M. Six Silberman** (1) — 平台劳动研究者. 美国研究者，Turkopticon 的共同创建者，后来与德国金属工会 IG Metall 合作研究平台劳动。 https://turkopticon.info/
- **MBC (Munhwa Broadcasting Corporation)** (1) — 韩国公共广播机构. 韩国电视台，制作了 VR 纪录片系列《遇见你》（2020–）。 https://www.imbc.com/
- **Mahmood Sharif** (1) — 计算机安全研究者；特拉维夫大学（卡内基梅隆大学博士）. 安全与机器学习研究者，在卡内基梅隆大学读博期间主导了用打印眼镜框欺骗人脸识别的研究。
- **Mamoru Oshii** (1) — 电影导演. 动画电影《攻壳机动队》（1995）的导演，改编自士郎正宗的漫画。
- **Manetta Berends** (1) — 设计师、研究者. 荷兰设计师与研究者，关注自由软件、出版与机器学习素养。
- **Manu Luksch** (1) — 艺术家、电影人. 生于奥地利的艺术家与电影人，研究监控、数据权利与网络媒体。 https://manuluksch.com/
- **Manuel Beltrán** (1) — 艺术家、研究者；Institute of Human Obsolescence 创始人. 西班牙艺术家，以装置和介入揭示技术内部的权力关系，关注数据与自动化。 http://speculative.capital
- **Margherita Pevere** (1) — 生物艺术艺术家与研究者. 意大利艺术家，以活体细菌、真菌与生物材料以及变化中的身体为创作对象。 https://www.margheritapevere.com/
- **Mari Velonaki** (1) — 艺术家、机器人研究者；新南威尔士大学创意机器人实验室主任. 希腊裔澳大利亚艺术家，自 2000 年代初与澳大利亚野外机器人中心的工程师合作制作互动机器人装置。
- **Marianne Simmel** (1) — 心理学家（1923–2010）. 德国出生的实验心理学家，后来以幻肢与身体意象研究著称。
- **Mariela Yeregui** (1) — 艺术家；阿根廷国立二月三日大学教授. 阿根廷艺术家，创作关于距离、接触与脆弱的机器人和电子装置。 https://marielayeregui.com/
- **Mark Coeckelbergh** (1) — 维也纳大学媒介与技术哲学教授. 比利时哲学家，研究机器人伦理、机器的关系性道德地位以及 AI 政治。
- **Mark Shepard** (1) — 艺术家、建筑师；布法罗大学副教授. Mark Shepard 是艺术家、建筑师与研究者，研究普适计算与城市；主编《Sentient City》（MIT Press，2011）。 http://survival.sentientcity.net/
- **Marnix de Nijs** (1) — 艺术家. 荷兰艺术家，制作对身体有要求的互动装置，探讨感知与控制。 http://www.marnixdenijs.nl
- **Martin Backes** (1) — 艺术家. 德国艺术家与设计师，创作关于数字文化的物件与声音作品。 https://www.martinbackes.com
- **Martin Riches** (1) — 艺术家，制作音乐机器与会说话的机器. 出生于英国、在柏林工作的艺术家，自 1970 年代起制作机械乐器和会说话的机器。 http://www.martinriches.de
- **Martine Syms** (1) — 艺术家、电影人. 美国艺术家、导演，以电影、装置和表演处理黑人身份、自我呈现与技术。 https://martinesyms.com/
- **Martyna Marciniak** (1) — 艺术家、研究者. 波兰艺术家与研究者，她的项目 Anatomy of Non-Fact 研究视觉骗局、伪造和合成图像。 https://www.martyna.digital
- **Marvin Minsky** (1) — 计算机科学家，麻省理工学院人工智能实验室联合创始人（1927–2016）. 人工智能先驱，1956 年达特茅斯研讨会的共同组织者，麻省理工学院人工智能实验室联合创始人，著有《心智社会》（1986）。
- **Mary Flanagan** (1) — 艺术家、游戏设计师；达特茅斯学院教授. Mary Flanagan 创作软件艺术、装置与游戏，并主持达特茅斯学院的 Tiltfactor 游戏实验室。 http://maryflanagan.com
- **Mary L. Gray** (1) — 微软研究院资深首席研究员，印第安纳大学教员. 媒介与劳动人类学家，2020 年麦克阿瑟学者，研究按需平台劳动。
- **Masahiro Miwa** (1) — 作曲家；IAMAS 教授. 日本作曲家，以“逆模拟音乐”著称：由演奏者或机器把算法当作音乐规则来执行。
- **Masakhane** (1) — 非洲语言自然语言处理的草根研究社区. 由非洲研究者组成的志愿网络，为非洲语言构建数据集和模型。 https://www.masakhane.io/
- **Matt Donovan** (1) — 艺术家. 加拿大艺术家与工程师，与 Max Dean、Raffaello D'Andrea 共同开发 The Robotic Chair。
- **Matt Richardson** (1) — 技术人员与创客；曾就读于纽约大学 ITP. Matt Richardson 是创意技术人员，写过 Raspberry Pi 与 Arduino 的书；Descriptive Camera 是他在纽约大学 ITP 读书时的作品。
- **Matt Schlicht** (1) — 创业者. 美国创业者，2026 年 1 月推出面向 AI 智能体的论坛 Moltbook。 https://www.moltbook.com/
- **Matteo Pasquinelli** (1) — 威尼斯大学（Ca' Foscari）科学哲学副教授. 意大利哲学家，主持欧洲研究理事会 AIMODELS 项目研究 AI 的历史；《The Eye of the Master》获 2024 年 Deutscher 纪念奖。
- **Max Dean** (1) — 艺术家. Max Dean 是出生于英国的加拿大艺术家，以让观众卷入其中的互动与机器人作品著称。
- **Max Dovey** (1) — 艺术家、研究者. 英国艺术家，其表演让人处在被机器学习系统分类或为之劳动的位置。 https://www.maxdovey.com
- **Maywa Denki** (1) — 以虚构电器公司形式运作的艺术组合（土佐信道）. 土佐兄弟 1993 年创立的艺术组合，制作荒诞的音乐机器，并以公司“产品”的方式发布。 https://www.maywadenki.com/
- **Merritt Moore** (1) — 芭蕾舞者、量子物理学家. 美国舞者，牛津大学原子与激光物理博士，编创与工业机械臂的双人舞。 https://www.merrittmoore.com/
- **Michael Almereyda** (1) — 电影导演、编剧. 美国独立电影导演，2017 年把乔丹·哈里森的舞台剧《Marjorie Prime》改编成电影。 https://en.wikipedia.org/wiki/Michael_Almereyda
- **Michael Eisen** (1) — 加州大学伯克利分校生物学家；开放科学倡导者. 美国计算生物学家，公共科学图书馆（PLOS）联合创办人。 https://www.michaeleisen.org/blog/
- **Michael Levin** (1) — 生物学家；塔夫茨大学教授. 美国发育生物学家，研究生物电与合成的“活机器”。
- **Michael Mandiberg** (1) — 艺术家，纽约城市大学教授. 美国艺术家，作品运用数字平台的逻辑，从打印维基百科到零工经济外包。 https://www.mandiberg.com/
- **Michael Snow** (1) — 艺术家、电影人（1928–2023）. 加拿大艺术家与结构主义电影人，代表作有 Wavelength（1967）和 La Région Centrale（1971）。
- **Michal Luria** (1) — 人机交互与人机器人交互研究者. 用设计方法与情境扮演探索社交机器人和对话智能体的研究者。 https://www.michalluria.com/
- **Michel Waisvisz** (1) — 作曲家、乐器发明者；STEIM 艺术总监（1949–2008）. 荷兰作曲家，在 STEIM 打造以手势演奏的电子乐器。 https://en.wikipedia.org/wiki/Michel_Waisvisz
- **Michelle Teran** (1) — 艺术家. 加拿大艺术家，通过行走与表演让城市中隐藏的媒介网络变得可感。
- **Michio Okada** (1) — 丰桥技术科学大学教授（ICD 实验室）. 认知科学家与机器人学家，提出“弱机器人”：需要人帮忙才能完成任务的机器人。
- **Microsoft XiaoIce team** (1) — 微软（亚洲）互联网工程院社交聊天机器人团队，后独立为小冰公司. 2014 年在中国推出小冰的团队；小冰被设计成富有同理心的陪伴者，而非任务助手。
- **Milagros Miceli** (1) — 社会学家、计算机科学家，DAIR 研究所与魏森鲍姆研究所. 阿根廷研究者，研究全球南方的数据标注员和内容审核员的工作。 https://www.weizenbaum-institut.de/en/
- **Minne Atairu** (1) — 跨学科艺术家. 生于尼日利亚的艺术家，用生成式 AI 探讨 1897 年英军洗劫之后贝宁艺术档案的空缺。 https://minneatairu.com/
- **Molleindustria** (1) — Paolo Pedercini 的独立游戏工作室. 意大利创立的工作室，制作关于劳动、战争与技术的短篇政治电子游戏。 https://www.molleindustria.org
- **Monika Fleischmann** (1) — 媒体艺术家与研究者；ART+COM 联合创始人. 德国媒体艺术先驱，与 Wolfgang Strauss 合作了早期互动装置，并在 GMD／弗劳恩霍夫研究所主持 MARS 实验室。
- **Moon Ribas** (1) — 赛博格艺术家、编舞家；Cyborg Foundation 联合创始人. 舞者，通过植入体内、连接在线地震数据的传感器感受全球地震。 https://www.moonribas.com/
- **Moritz Riesewieck** (1) — 导演、作家. 德国导演和作家，与 Hans Block 合导了《清道夫》和《永恒的你》。 https://en.wikipedia.org/wiki/The_Cleaners_(2018_film)
- **Moritz Stefaner** (1) — 数据可视化设计师. 德国设计师，以数据可视化与交互信息设计著称。 https://truth-and-beauty.net
- **Mushon Zer-Aviv** (1) — 设计师、研究者、媒体行动者. Mushon Zer-Aviv 是设计师、教育者和媒体行动者，关注数据、监控与算法偏见。 https://mushon.com
- **Myron Krueger** (1) — 计算机艺术家、研究者. 美国计算机艺术家（生于 1942 年），1969 年起构建响应式环境，并提出“人工现实”一词。 https://en.wikipedia.org/wiki/Myron_W._Krueger
- **NASA Jet Propulsion Laboratory** (1) — 美国宇航局喷气推进实验室. 美国宇航局负责行星机器人任务的研究中心，研制并操控了火星探测车“勇气号”和“机遇号”。 https://www.jpl.nasa.gov/
- **Nathaniel Rochester** (1) — 计算机工程师，IBM（1919–2001）. IBM 701（IBM 第一台商用科学计算机）的总设计师，也是最早在计算机上模拟神经网络的人之一。
- **Nazli Cila** (1) — 代尔夫特理工大学助理教授. 研究人与智能体伙伴关系以及超越人类设计的设计研究者。 https://nazlicila.com/
- **Near Future Laboratory** (1) — 设计虚构工作室（Julian Bleecker、Nick Foster、Fabien Girardin、Nicolas Nova）. 推广“设计虚构”的工作室，为平凡的近未来制作道具和文件。 https://nearfuturelaboratory.com/
- **Neil Harbisson** (1) — 赛博格艺术家；Cyborg Foundation 与 Cyborg Arts 联合创始人. 天生全色盲的艺术家，通过植入颅骨的天线“听见”颜色。 https://www.cyborgarts.com/
- **Nicholas Carlini** (1) — 机器学习安全研究者. 计算机安全研究者，以对抗样本、音频对抗攻击以及从神经网络中提取训练数据的奠基性研究闻名。 https://nicholas.carlini.com/
- **Nicholas Stedman** (1) — 艺术家、机器人设计师. 加拿大艺术家，制作会触摸、缠绕人体的模块化蛇形机器人。
- **Nicolas Darrot** (1) — 创作自动机与机器雕塑的艺术家. 法国艺术家（1972 年生），制作混合动物、人与机器的机电木偶与自动机。
- **Nicolas Schöffer** (1) — 艺术家，控制论艺术先驱. 匈牙利裔法国艺术家（1912–1992），20 世纪 50 年代起发展“空间动力”与控制论雕塑。
- **Nissei Eco** (1) — 殡葬与塑料制品公司. 日本公司，2017 年让软银 Pepper 机器人在葬礼上诵读佛经。
- **Nora Al-Badri** (1) — 跨学科艺术家. 德国-伊拉克艺术家，以“技术遗产”为题，质疑博物馆对非欧洲文物及其数据的占有。 https://www.nora-al-badri.de/
- **Norbert Wiener** (1) — 数学家，控制论创始人（1894–1964）. 麻省理工学院数学家，1948 年为动物与机器中的控制与通信科学命名，之后持续警示自动化的社会后果。
- **ORLAN** (1) — 以表演、外科手术、生物技术和机器人创作的艺术家. 法国艺术家，以 1990 年代的外科手术表演闻名，后来转向细胞培养、虚拟化身与机器人创作。 https://www.orlan.eu
- **OpenAI** (1) — 人工智能研究公司. 2015 年成立的人工智能公司，开发了 GPT 模型与 ChatGPT。 https://openai.com/
- **Ory Laboratory** (1) — 吉藤健太朗创办的机器人公司. OriHime 分身机器人的开发者，让无法出门的人（包括渐冻症患者）远程工作与“在场”。 https://dawn2021.orylab.com/en/
- **Osamu Tezuka** (1) — 漫画家、动画家. 漫画家（1928–1989），创作了 1952 年开始连载的《铁臂阿童木》。
- **Oscar Sharp** (1) — 电影导演. 英国导演，执导了由神经网络“Benjamin”编剧的影片。 https://en.wikipedia.org/wiki/Sunspring
- **Pablo Berger** (1) — 电影导演. 西班牙编剧兼导演，作品有《白雪公主》和动画长片《机器人之梦》。 https://en.wikipedia.org/wiki/Pablo_Berger
- **Pablo Ventura** (1) — 编舞家；Ventura Dance Company 总监. 西班牙编舞家，自 2000 年前后与工业机器人、软件和机器表演者合作。 https://www.ventura-dance.com/
- **Paola Torres Núñez del Prado** (1) — 艺术家. Paola Torres Núñez del Prado 是秘鲁艺术家，结合纺织、声音与技术，并借鉴安第斯知识体系。 https://www.singingtextiles.com
- **Pat Metheny** (1) — 爵士吉他手、作曲家. 美国吉他手，曾带着一支由机械演奏的原声乐器乐队巡演。 https://www.patmetheny.com/
- **Paul Sermon** (1) — 艺术家；布莱顿大学视觉传达教授. 英国艺术家，自 1991 年起创作远程通信装置，把异地的身体连接进共享的影像空间。 https://www.paulsermon.org/
- **Paul Vanouse** (1) — 艺术家，纽约州立大学布法罗分校教授. 美国艺术家，运用生物技术质疑科学权威、身份与劳动。 https://www.paulvanouse.com/
- **Paul Virilio** (1) — 文化理论家、城市学家（1932–2018）. 法国理论家，研究速度、战争与感知，著有《速度与政治》（1977）和《战争与电影》（1984）。
- **Pedro Lopes** (1) — 芝加哥大学计算机科学副教授，人机融合实验室（Human Computer Integration Lab）负责人. Pedro Lopes 研究与使用者身体融为一体的设备，例如能驱动佩戴者肢体的肌肉电刺激。 https://plopes.org
- **Pedro Oliveira** (1) — 声音艺术家、研究者；柏林艺术大学声音研究与声音艺术客座教师. 巴西声音艺术家与研究者（1985 年生于圣保罗），研究“听”如何塑造技术基础设施又被其塑造，关注声音与移民；Decolonising Design 创始成员之一。 https://oliveira.work/
- **Peng! Collective** (1) — 行动主义艺术团体. 结合文化干扰、黑客行动与公民不服从的柏林团体。 https://pen.gg
- **Peter-Paul Verbeek** (1) — 技术哲学家，阿姆斯特丹大学校长. 荷兰哲学家，在《What Things Do》（2005）和《Moralizing Technology》（2011）中发展了技术中介理论。
- **Peterskapelle Lucerne & HSLU Immersive Realities Research Lab** (1) — 天主教礼拜堂与大学研究实验室. 卢塞恩圣彼得礼拜堂与卢塞恩应用科学与艺术大学沉浸现实研究实验室，二者于 2024 年合作推出 AI 耶稣装置《Deus in Machina》。 https://www.peterskapelle.ch/
- **Petra Gemeinboeck** (1) — 艺术家、人机动作研究者；斯威本科技大学. 奥地利裔澳大利亚艺术家，常与 Rob Saunders 合作，同舞者一起发展机器人的身体与动作。
- **Phil D. Hall** (1) — 对话式 AI 设计师；I Am Echoborg 联合创作者. 聊天机器人设计师，编写 I Am Echoborg 背后的对话代理。 https://echoborg.com/
- **Philip Beesley** (1) — 建筑师、艺术家；滑铁卢大学教授；Living Architecture Systems Group 负责人. Philip Beesley 建造沉浸式响应环境，让它们像“近乎活着”的系统一样运作。 https://www.philipbeesleystudioinc.com
- **Philip van Allen** (1) — 艺术中心设计学院教授. 美国交互设计师，制作万物有灵式原型与面向 AI 设计的工具包。 https://www.philvanallen.com/
- **Philippe Parreno** (1) — 艺术家. 法国艺术家，把展览编排成由传感器和计算机驱动的自动化、时间性的系统。 https://en.wikipedia.org/wiki/Philippe_Parreno
- **Pierre Jaquet-Droz** (1) — 钟表匠、自动人偶制作者. 瑞士钟表匠（1721–1790），与儿子 Henri-Louis 及 Jean-Frédéric Leschot 一起造出了“书写者”“绘图者”和“音乐家”三个人偶。
- **Piotr Mirowski** (1) — AI 研究者、即兴演员；Improbotics 联合创始人. 机器学习研究科学家，与 AI 系统一起表演即兴戏剧。 https://improbotics.org/
- **Pipeline Theatre** (1) — 剧团. 英国剧团，与人形机器人公司 Engineered Arts 合作创作了 Spillikin。 https://www.pipelinetheatre.com/
- **Primavera De Filippi** (1) — 法律学者、艺术家；法国国家科学研究中心与哈佛 Berkman Klein 中心研究员. 意大利法律学者与艺术家，研究区块链治理，并创作了拥有自己的机器人“植物” Plantoid。
- **Project CETI** (1) — 非营利跨学科研究计划. 由 David Gruber 等人于 2020 年发起，用机器学习和机器人研究抹香鲸交流的计划。 https://www.projectceti.org/
- **Prokop Bartoníček** (1) — 设计师、艺术家. 捷克设计师与艺术家，创作互动系统、装置与机器。 http://www.prokopbartonicek.com
- **Protestant Church in Hesse and Nassau (EKHN)** (1) — 德国黑森—拿骚新教教会. 德国福音教会下属的地区教会；在宗教改革 500 周年之际，它在维滕贝格展出了祝福机器人 BlessU-2。 https://www.ekhn.de/
- **Qian Yang** (1) — 康奈尔大学信息科学助理教授. 人机交互研究者，研究如何设计人与 AI 的交互，关注医疗领域。
- **Quantic Dream** (1) — 电子游戏开发商. 法国游戏工作室，以《暴雨》《底特律：变人》等采用表演捕捉的互动剧情游戏闻名。 https://www.quanticdream.com/
- **Rachel Ara** (1) — 观念与数据艺术家. 伦敦艺术家，做了 25 年计算机系统设计师后，开始创作关于价值、性别与科技的霓虹与数据雕塑。
- **Radamés Ajna** (1) — 艺术家、技术专家. 巴西艺术家与技术专家，使用电子、网络与机器学习。
- **Radhika Nagpal** (1) — 计算机科学家；普林斯顿大学教授（曾任职哈佛）. 印度裔美国机器人学家，研究机器人群体与社会性昆虫的集体智能。
- **Raffaello D'Andrea** (1) — 机器人学家；苏黎世联邦理工学院教授，Kiva Systems 联合创始人. 加拿大裔意大利工程师，以自主系统著称，从 Kiva 仓储机器人到飞行机器，并与 Max Dean 有艺术合作。
- **Rashaad Newsome** (1) — 艺术家. 美国艺术家，以拼贴、表演、影像和 AI 创作，取材于舞会文化、voguing 等黑人和酷儿文化。 https://rashaadnewsome.com/
- **Rebecca Fiebrink** (1) — 伦敦艺术大学创意计算学院教授. 美国计算机科学家与音乐人，为艺术家开发交互式机器学习工具。 http://www.wekinator.org/
- **Renwu magazine** (1) — 杂志（记者赖祐萱）. 中国人物特稿杂志，其 2020 年关于外卖骑手的调查报道成为当年阅读量最高的中文文章之一。
- **Revital Cohen** (1) — 艺术家、设计师（Cohen Van Balen）. 生于以色列、在伦敦工作的艺术家，常与 Tuur Van Balen 合作，以医疗设备、动物与供应链为题材。 https://www.cohenvanbalen.com/
- **Richard Mosse** (1) — 艺术家、摄影师. 爱尔兰艺术家，使用红外胶片、热成像相机等军事与科学成像技术记录冲突与迁徙。 https://www.richardmosse.com
- **Ridley Scott** (1) — 电影导演. 英国导演，作品有《异形》《银翼杀手》。 https://en.wikipedia.org/wiki/Ridley_Scott
- **Rik Lander** (1) — 艺术家、编剧；I Am Echoborg 联合创作者. 英国互动叙事创作者，创作关于 AI 的参与式作品。 https://echoborg.com/
- **Rimini Protokoll** (1) — 剧场团体（Helgard Haug、Stefan Kaegi、Daniel Wetzel）. 德瑞剧场团体，以“日常生活专家”代替演员的纪录剧场闻名。 https://www.rimini-protokoll.de/
- **Rob Saunders** (1) — 计算创造力研究者；莱顿大学. 英国计算创造力与“好奇智能体”研究者，Petra Gemeinboeck 的长期合作者。
- **Robert Breer** (1) — 实验电影人、动态雕塑家. 美国实验电影人和雕塑家（1926–2011），20 世纪 60 年代中期起做出缓慢爬行的电动“漂浮物”。
- **Robert Long** (1) — 哲学家；Eleos AI 执行主任. 研究 AI 意识、感受性与道德地位的哲学家。 https://eleosai.org/
- **Robert Sparrow** (1) — 莫纳什大学哲学教授. 澳大利亚哲学家，研究机器人伦理、军事 AI、养老照护与人类增强。
- **Robert Wood** (1) — 机器人学家；哈佛大学教授. 美国机器人学家，在哈佛工程与应用科学学院和 Wyss 研究所研究软体与微型机器人。
- **Rocio von Jungenfeld** (1) — 艺术家；肯特大学数字艺术讲师. 以特定场域互动装置、光与电子为媒介的艺术家。
- **Rolf Pfeifer** (1) — 苏黎世大学计算机科学荣休教授，人工智能实验室创始人. 瑞士机器人学家，主导具身人工智能研究，涉及形态计算以及柔软、顺应的机器人身体。
- **Romi Ron Morrison** (1) — 艺术家、学者. 美国跨学科艺术家与学者，关注黑人地理、数据与监控。
- **Rosa Menkman** (1) — 艺术家、理论家. 荷兰艺术家与理论家，研究故障、压缩与分辨率，著有《The Glitch Moment(um)》（2011）。 https://beyondresolution.info
- **Ruairi Glynn** (1) — 建筑师、艺术家；伦敦大学学院巴特莱特建筑学院互动建筑实验室负责人. 出生于爱尔兰的机器人与响应式建筑设计者。 https://www.ruairiglynn.co.uk
- **Ruben van de Ven** (1) — 艺术家、研究者. 荷兰艺术家兼研究者，考察情绪识别与算法观看的政治。 https://rubenvandeven.com
- **Ruha Benjamin** (1) — 普林斯顿大学非裔美国人研究教授. 社会学家，创立 Ida B. Wells Just Data Lab，著有《Race After Technology》（2019）和《Viral Justice》（2022）。
- **SAND Lab (University of Chicago)** (1) — 由 Ben Zhao 与 Heather Zheng 领导的安全、算法与网络实验室. 为个人开发对抗机器学习的防御工具（如 Glaze 和 Nightshade）的研究实验室。 https://sandlab.cs.uchicago.edu/
- **Safiya Umoja Noble** (1) — 加州大学洛杉矶分校性别研究、非裔美国人研究与信息研究教授. 互联网研究学者，2021 年麦克阿瑟学者，创立加州大学洛杉矶分校种族与数字正义中心。
- **Sam Kriegman** (1) — 机器人学家；西北大学助理教授. 美国机器人学家，用演化算法设计身体；2020 年异种机器人论文的第一作者。
- **Sam Lavigne** (1) — 艺术家、教育者. 美国艺术家，使用网页爬取、监控工具和机器学习，常常把它们反过来对准有权力的人。 https://lav.io/
- **Sarah Petkus** (1) — 艺术家、机器人制作者. Sarah Petkus 是美国艺术家、插画师和工程师，用轻金属、3D 打印件和现成物制作有性格的机器人。 https://www.youtube.com/GravityRoad
- **Sašo Sedlaček** (1) — 艺术家. 斯洛文尼亚艺术家，用低技术机器与公共介入讨论废弃物、贫困与技术乐观主义。 https://sasosedlacek.com
- **Scatter Lab** (1) — AI 聊天机器人初创公司. 韩国初创公司，开发了聊天机器人“李乐达”（Lee Luda，2020），其训练数据来自旗下恋爱咨询应用中的聊天记录。 https://www.scatterlab.co.kr/
- **Shalini Kantayya** (1) — 纪录片导演，7th Empire Media 创始人. 美国纪录片导演，作品关注科学、技术与公民权利。 https://www.7thempire.com/
- **Sherry Turkle** (1) — 麻省理工学院科学技术社会研究教授. 社会学家与临床心理学家，创立麻省理工学院“技术与自我”研究项目，著有《The Second Self》（1984）和《群体性孤独》（2011）。 https://sherryturkle.mit.edu
- **Shing Tat Chung** (1) — 艺术家、设计师. 英国艺术家、设计师，毕业于皇家艺术学院，关注技术系统中的信仰与非理性。
- **Shuya Abe** (1) — 电气工程师，白南准的技术合作者. 日本工程师（1932–2016），与白南准合作制作了《机器人 K-456》和白南准–阿部录像合成器。
- **Siddharth Suri** (1) — 微软研究院资深首席研究员. 计算社会科学家，研究众包劳动与在线劳动市场。
- **Silvia Ruzanka** (1) — 伦斯勒理工学院艺术家与讲师. Silvia Ruzanka 是媒体艺术家，创作游戏和故障艺术，其中包括一款由捕蝇草来玩的电子游戏。
- **Simon Weckert** (1) — 艺术家. 常驻柏林的艺术家，以表演和装置探讨数字技术与平台的社会影响。 http://www.simonweckert.com
- **Simone Giertz** (1) — 发明家、YouTuber. 瑞典发明家（1990 年生），以在 YouTube 上发布故意做得很糟的“烂机器人”闻名。 https://www.simonegiertz.com/
- **Simone Rebaudengo** (1) — 设计师；automato.farm 联合创办人. 意大利交互设计师，想象拥有需求、习惯与社交生活的联网产品。 http://www.automato.farm/about
- **Sofian Audry** (1) — 艺术家，魁北克大学蒙特利尔分校媒体学院教授. 加拿大艺术家与学者，创作机器人与机器学习艺术作品。 https://sofianaudry.com
- **Sonia Kennebeck** (1) — 纪录片导演、制片人. 德裔美国调查纪录片导演。 https://nationalbirdfilm.com/
- **Spike Jonze** (1) — 电影导演、编剧. 美国导演，拍摄音乐录影带和剧情长片，代表作有《成为约翰·马尔科维奇》（1999）和《她》（2013）。 https://en.wikipedia.org/wiki/Spike_Jonze
- **Sputniko! (Hiromi Ozaki)** (1) — 艺术家、设计师；东京艺术大学副教授. 思辨设计师，以《月经机器》等影片与装置，从性别角度追问技术。
- **Squarepusher** (1) — 音乐人（Tom Jenkinson）. 英国电子音乐人与贝斯手，签约 Warp 唱片。 https://squarepusher.net/
- **Stahl Stenslie** (1) — 触觉与实验媒介艺术家、研究者. 挪威艺术家，自 1990 年代初创作远程触觉与全身交互界面。 https://en.wikipedia.org/wiki/Stahl_Stenslie
- **Stanisław Lem** (1) — 作家、哲学家（1921–2006）. 波兰科幻作家，其小说与随笔深入思考非人类智能。 https://en.wikipedia.org/wiki/Stanis%C5%82aw_Lem
- **Stanley Kubrick** (1) — 电影导演（1928–1999）. 在英国工作的美国导演；《2001：太空漫游》与 Arthur C. Clarke 合写。 https://en.wikipedia.org/wiki/Stanley_Kubrick
- **Steffen Weiß** (1) — 设计师. 德国设计师，与 Philipp Schmitt 合作完成 The Chair Project。
- **Steina Vasulka** (1) — 录像艺术家. 冰岛出生的录像艺术先驱，1971 年与 Woody Vasulka 在纽约共同创办 The Kitchen。 http://www.vasulka.org
- **Steph Maj Swanson** (1) — 艺术家与作者（Supercomposite）. 音乐人与艺术家，网名 Supercomposite，2022 年记录下“Loab”形象。 https://en.wikipedia.org/wiki/Loab
- **Stephan Bogner** (1) — 设计师. 德国交互设计师（施瓦本格明德设计学院毕业），Raising Robotic Natives 的合作者之一。 https://stephanbogner.de/
- **Sterling Crispin** (1) — 艺术家、技术专家. 美国艺术家、技术专家，早期作品对人脸检测与识别系统进行逆向工程，后来从事 AR/VR 与神经技术研发。 https://www.sterlingcrispin.com
- **Steve Mann** (1) — 发明家；多伦多大学电子与计算机工程教授. 研究者，自 1970 年代末起在日常生活中佩戴计算机与头戴摄像机，并提出“反向监视”（sousveillance）一词。 http://wearcam.org/
- **Steven Spielberg** (1) — 电影导演、制片人. 美国导演和制片人；他接手斯坦利·库布里克筹备多年的项目，完成了《人工智能》（2001）。 https://en.wikipedia.org/wiki/Steven_Spielberg
- **Super Brain** (1) — AI 工作室（创始人张泽伟）. 南京的工作室，用家属提供的照片、视频与录音为逝者制作 AI 数字人。
- **Surveillance Camera Players** (1) — 由 Bill Brown 创立的表演团体. 从 1996 年起在公共监控摄像头前上演无声戏剧的行动主义团体。 http://www.notbored.org/the-scp.html
- **Survival Research Labs** (1) — Mark Pauline 于 1978 年创立的机器表演团体. 旧金山团体，上演大型、危险的表演，让自制机器互相搏斗、彼此摧毁。 https://srl.org/
- **Susumu Tachi** (1) — 东京大学名誉教授；日本虚拟现实学会创会会长. 工程师，1980 年提出“远程存在”（telexistence），并研制 TELESAR 系列机器人，让人感到自己身处远方的机器人身体中。 https://tachilab.org/en/
- **Suzanne Kite** (1) — 艺术家、作曲家、学者（奥格拉拉拉科塔族）；巴德学院 Wihanble S'a 实验室主任. 奥格拉拉拉科塔族艺术家和学者，其表演与机器学习作品取材于拉科塔族本体论，以及与石头和非人存在的关系。 https://kitekitekitekite.com/
- **Suzanne Treister** (1) — 艺术家. 英国艺术家，其虚构档案把技术、金融、神秘学与意识交织在一起。 http://www.suzannetreister.net/
- **THEaiTRE** (1) — 研究与剧场项目（查理大学、Švandovo 剧院、布拉格表演艺术学院）. 捷克项目，用语言模型写剧本，始于 2021 年 R.U.R. 百年纪念。 https://www.theaitre.com/
- **Tabita Rezaire** (1) — 艺术家、疗愈者. 法属圭亚那-丹麦裔艺术家，影像作品把数字网络、殖民历史与灵性技术联系在一起。 https://tabitarezaire.com/
- **Tactical Tech** (1) — 关注技术与社会的国际非政府组织. 非营利组织，制作关于数据、隐私与影响操纵的公众展览和工具包。 https://tacticaltech.org/
- **Takanori Shibata** (1) — 日本产业技术综合研究所首席研究员. 工程师，研发了自 2004 年起用于失智症与老年照护的海豹机器人 PARO。 http://www.parorobots.com/
- **Te Hiku Media** (1) — 由毛利人主导的媒体机构与语言技术实验室. 新西兰北岛远北地区的部落广播与媒体机构，在社区自有数据之上开发毛利语语音技术。 https://tehiku.nz/
- **Ted Chiang** (1) — 科幻作家. 华裔美国科幻作家（《你一生的故事》《呼吸》）。
- **Temple Grandin** (1) — 动物科学家、发明家；科罗拉多州立大学教授. 自闭症科学家与作家，设计过更人道的牲畜处理系统；年轻时还为自己做了一台用来安抚自己的压力机器。 https://www.templegrandin.com
- **The Long Now Foundation** (1) — 倡导长期思维的非营利机构. 1996 年由 Stewart Brand、Danny Hillis 等人创立，致力于以一万年为尺度的思考。 https://longnow.org/
- **Theo Anthony** (1) — 电影人. 美国纪录片导演，作品质疑图像和仪器如何宣称客观。 https://en.wikipedia.org/wiki/Theo_Anthony
- **Theo Jansen** (1) — 艺术家. 荷兰艺术家，自 1990 年起用 PVC 管制作靠风行走的“海滩生物”。 https://www.strandbeest.com/
- **Thiago Hersan** (1) — 艺术家、工程师. 巴西裔美国艺术家，其装置探讨机器与网络如何表征人。 https://thiagohersan.com
- **Thomas Freundlich** (1) — 舞者、编舞家、电影人. 芬兰裔美国编舞家，自 2008 年起为工业机器人创作舞蹈作品。 http://www.freundlich.org/
- **Thomas Melle** (1) — 作家. 德国小说家、剧作家，在《我背后的世界》中书写自己的双相障碍。
- **Timnit Gebru** (1) — 分布式人工智能研究所（DAIR）创始人兼执行主任. 埃塞俄比亚出生的计算机科学家，Black in AI 联合创始人，曾任谷歌伦理 AI 团队联合负责人。
- **Timo Arnall** (1) — 设计师、电影人. 英国设计师，以影像和研究让 RFID、卫星和数据中心等看不见的技术变得可见。 https://www.elasticspace.com/
- **Timo Toots** (1) — 媒体艺术家. 爱沙尼亚媒体艺术家，他的装置把国家与网络数据库里关于观众的信息变成公开展示。 http://works.timo.ee
- **Tobias Rees** (1) — AI 哲学家、人类学家. 哲学家、人类学家，曾主持博古睿研究院“人的转变”项目，与 AI 实验室合作探讨其研究的哲学意涵。
- **Tod Machover** (1) — 作曲家；MIT 媒体实验室教授（Opera of the Future 组）. 美国作曲家，发明“超级乐器”（hyperinstruments），创作以技术驱动的歌剧。 https://www.media.mit.edu/people/tod/overview/
- **Tom B. Brown** (1) — 机器学习研究者（Google Brain，后任职 OpenAI 与 Anthropic）. 机器学习研究者，2017 年主导了 Google Brain 关于“对抗补丁”的论文，后来参与领导大语言模型研究。
- **Tom Shannon** (1) — 艺术家、发明家. 美国艺术家（1947 年生），1966 年还是年轻艺术家时就做出了由活植物控制的机器人 Squat。
- **Tom White** (1) — 艺术家（dribnet）；惠灵顿维多利亚大学设计学院高级讲师. 常驻新西兰的艺术家与设计讲师，网名 dribnet，创作专门供神经网络分类器“阅读”的绘画与版画。 https://drib.net
- **Tomas van Houtryve** (1) — 摄影师、艺术家. 比利时裔美国摄影师，关注冲突、监控与历史。 https://tomasvh.com/
- **Tomasz Hollanek** (1) — 剑桥大学未来智能研究中心研究员. 设计与技术伦理研究者，研究把批判设计、思辨情景与 AI 伦理结合起来。 https://www.lcfi.ac.uk/
- **Tomo Kihara** (1) — 设计师、艺术家；Playfool 联合创始人. 日本设计师、艺术家，常与 Daniel Coppen 以工作室 Playfool 的名义，创作关于 AI、平台与城市的游戏和装置。 https://www.tomokihara.com
- **Tore Knudsen** (1) — 交互设计师、研究者. 丹麦交互设计师，CIID 校友，研究面向机器学习与智能家居的实体交互界面。
- **UBERMORGEN** (1) — 艺术家二人组（lizvlx 与 Hans Bernhard）. 1995 年起活跃的奥地利—瑞士艺术家二人组，创作涉及网络、媒体入侵与机器系统。
- **USC Shoah Foundation** (1) — 南加州大学视觉历史与教育研究所. 由 Steven Spielberg 于 1994 年创立的研究所，保存了五万多份大屠杀幸存者及其他种族灭绝见证者的影像证词。 https://sfi.usc.edu/
- **Unitree Robotics** (1) — 机器人公司. 杭州的四足与人形机器人制造商（Go、H1、G1）。 https://www.unitree.com
- **Unknown Fields Division** (1) — 由 Liam Young 和 Kate Davies 领导的游牧式设计工作室. 设计研究工作室，带队考察消费科技背后的矿山、工厂和港口。 http://www.unknownfieldsdivision.com/
- **Ursula Damm** (1) — 艺术家；包豪斯魏玛大学媒体环境教授. Ursula Damm 是德国媒体艺术家，她的生成影像装置以实时摄像输入和神经网络探讨感知、城市空间与自然。 https://ursuladamm.de
- **Valentino Braitenberg** (1) — 神经科学家、控制论学者（1926–2011）. 意大利神经科学家，曾任马克斯·普朗克生物控制论研究所所长，著有《Vehicles：合成心理学实验》（1984）。
- **Verena Friedrich** (1) — 媒体艺术家. 德国艺术家，制作精密的机器和实验装置，处理延长寿命、测量与自动化判断等问题。 https://heavythinking.org
- **Victor Wong** (1) — 艺术家、视觉特效制作人. 香港视觉特效制作人（vfxNova），2018 年创造了 AI 水墨画家 A.I. Gemini。 https://www.3812gallery.com/artists/victor-wong-ai-gemini/
- **Vilém Flusser** (1) — 媒介哲学家（1920–1991）. 捷克出生的巴西哲学家，研究装置、技术图像，以及贯穿相机与使用者的“程序”。
- **Vincent Fournier** (1) — 摄影师、艺术家. 法国摄影师，作品关注太空探索、机器人和想象中的未来生命形态。 https://www.vincentfournier.co.uk/
- **Waltz Binaire** (1) — 设计与媒体艺术工作室（Christian Mio Loclair）. 由 Christian Mio Loclair 主持的柏林工作室，用机器学习和动作制作装置。 https://christianmioloclair.com
- **Wang Yuyang** (1) — 艺术家. 北京艺术家，以光、雕塑与技术为媒介创作。
- **Wayne McGregor** (1) — 编舞家；Studio Wayne McGregor 艺术总监；威尼斯双年展舞蹈部分总监. 英国编舞家，长期与认知科学家和技术人员合作，研究动作如何生成。 https://waynemcgregor.com/
- **Wen-Ying Tsai** (1) — 艺术家、工程师（1928–2013）. 由工程师转为艺术家的美籍华人，自 1968 年起开创控制论雕塑。
- **Wendy Hui Kyong Chun** (1) — 西蒙弗雷泽大学新媒体加拿大 150 研究讲席. 媒介理论家，数字民主研究所创所所长，著有《程序化的视觉》《更新以保持不变》。
- **William Chamberlain** (1) — 作家、程序员. 美国作家，1980 年代初与 Thomas Etter 共同开发了散文生成程序 Racter。 https://en.wikipedia.org/wiki/Racter
- **Wolfgang Strauss** (1) — 建筑师、媒体艺术家. 德国建筑师与媒体艺术家，长期与 Monika Fleischmann 合作互动环境。
- **Xenoangel (Marija Avramovic & Sam Twidale)** (1) — 创作实时动画与 AI 驱动虚拟世界的艺术家二人组. Marija Avramovic 与 Sam Twidale 以 Xenoangel 之名合作，用游戏引擎搭建由角色自主行动的虚拟世界。 https://www.samtwidale.com/
- **Xu Bing** (1) — 艺术家；中央美术学院前副院长. 以《天书》等关于语言与文字系统的作品闻名的中国艺术家，首部长片完全用监控录像剪辑而成。 https://www.xubing.com
- **YACHT** (1) — 乐队（Claire L. Evans、Jona Bechtolt、Rob Kieswetter）. 美国电子流行乐队，在严格的自设规则下用机器学习制作专辑。 https://teamyacht.com/
- **Yasuhiro Yoshiura** (1) — 动画导演. 《夏娃的时间》（2008–09）导演，讲述一家“不区分人类与机器人”的咖啡馆。
- **Yeon Sang-ho** (1) — 电影导演. 韩国导演，作品有《釜山行》及 Netflix 电影《贞伊》。 https://en.wikipedia.org/wiki/Yeon_Sang-ho
- **Zhang Yimou** (1) — 电影导演. 中国电影导演，也执导过 2008 年北京奥运会开幕式等大型国家演出。
- **Zimoun** (1) — 艺术家. 瑞士艺术家（1977 年生），用数百个小直流电机敲击纸板、铁丝和棉球，搭建大型装置。 https://www.zimoun.net/
- **Zoran Srdić Janežič** (1) — 雕塑家、跨媒介艺术家；卢布尔雅那大学 AGRFT 博士研究者. 斯洛文尼亚雕塑家，使用动画机械、三维设计和活体组织创作；自 2019 年起与 Kapelica 画廊和 BioTehna 实验室合作推进 Biobot 系列。
- **etoy.CORPORATION** (1) — 以公司形式组织的艺术团体. 1994 年成立、总部在瑞士的艺术团体，把公司、法律和数字结构当作创作材料；代表作有《Digital Hijack》（1996 年金尼卡奖）和《Toywar》。 http://missioneternity.org/
- **unmake lab** (1) — 艺术团体. 韩国艺术团体（成员包括崔彬娜），研究机器视觉如何建构自然与社会。
- **Špela Petrič** (1) — 有生物学背景的艺术家. Špela Petrič 是斯洛文尼亚艺术家和生物学家，以表演探索人、植物与机器之间的关系。 https://www.spelapetric.org
