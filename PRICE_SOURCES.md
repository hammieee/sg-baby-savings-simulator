# PRICE_SOURCES.md — 模拟养娃存钱 · 新加坡价格出处

> 研究日期：2026-11-20 · 货币：SGD · 版本：prices.json v1.0.0
> 用途：仅供模拟存钱游戏，非报价。真实决策请以医院 / 商家为准。
> 规则：查不到的价不编，标 `Unverified`；范围价给范围，不给单点假精确。

## 怎么读这个文件

每项有 5 个字段：**价格 | 出处 | 查到日期 | 为什么是这个价 | 状态**
- `Verified` = 官网 / MOH / FairPrice 等一手出处
- `Estimate` = 二手指南的模型价 / 范围价，可编辑
- `Unverified` = 扫过但没找到干净价，App 里显示 `—`，不要硬编

## 1. 产检 Pregnancy

| 项目 | 价格 SGD | 出处 | 为什么 |
|---|---|---|---|
| 常规产检 公立津贴 每次 | S$37.20–101.49，私立 S$111.40–222.14 | KKH 收费页 2025-08-08；MoneySmart 2025 | 仅问诊费，scan / 血检 / 药另计。津贴需 polyclinic/GP 转诊，不能选医生。 |
| OSCAR 唐筛 11–14周 | 公立 ~S$200，私立 S$300–400 | MoneySmart；Income；AsianParent 2026-08 | 可选但推荐，唐氏检出率 ~90%。不是必须。 |
| NIPT 9–10周起 | 公立 ~S$680，私立 Harmony ~S$1,200 / Panorama ~S$1,400 | AsianParent 2026-08；Thomson | 可选，自费，**不能用 MediSave**。品牌不同价差大。 |
| 大排畸 TIFFA 18–22周 | 公立 ~S$150，私立 ~S$350 | KKH；Income | 常规，人人建议做。 |
| OGTT 妊娠糖尿病 24–28周 | 公立 S$35，私立 S$90 | Income；HeyBaby；ATA Medical 2026-01 S$27.25 | 常规。新加坡妊娠糖尿病约 20%。 |
| GBS 35–37周 | S$0 / 包含在产检里 | KKH；HeyBaby | 报告说包含，未找到独立价，**不要编**。 |
| 叶酸 / 孕妇维生素 每月 | 基础 S$25， premium S$60 | Guardian / Shopee 2026-11：21st Century S$16.90/60粒，Blackmores S$72.80/120粒 | 按瓶价折算每月。 |
| 产前课程 KKH 一对夫妇 | 公立 S$240，私立 S$306 | KKH 官网，2026-11-04–12-05 场次 | 可选。 |

产检次数：KKH 官方 8–10 次。8–12周建档+血检，11–14周唐筛，18–21周大排畸，24–28周贫血+糖尿病筛，28–32周生长 scan，35–37周 GBS。
来源：https://www.kkh.com.sg/patient-care/conditions-treatments/your-pregnancy-journey-in-kkh

## 2. 分娩 Delivery — MOH 中位数

**关键：这是 MOH 典型账单中位数，不是套餐价。**
- 数据：2023-01-01 至 2023-12-31 新加坡公民实际账单，含 GST，MediSave / 保险前。
- 公立价是**津贴后**，私立价**无津贴**。
- 医院套餐价只包医院收费，**不包医生费**，不能当总账单。

| 方式 | 医院 / 房型 | 中位数 | 范围 25–75% |
|---|---|---|---|
| 自然产 | NUH C | S$946 | S$770–1,385 |
| 自然产 | NUH B2 | S$1,025 | S$796–1,478 |
| 自然产 | KKH C | S$1,385 | S$1,138–1,799 |
| 自然产 | KKH B2 | S$1,486 | S$1,243–1,898 |
| 自然产 | KKH A 1人房 | S$5,780 | S$5,297–6,628 |
| 自然产 | Thomson 4人房 | S$7,580 | S$5,385–9,945 |
| 自然产 | Thomson 2人房 | S$9,263 | S$7,876–10,904 |
| 自然产 | Thomson 1人房 | S$10,802 | S$9,425–12,494 |
| 自然产 | Mount Elizabeth Orchard 1人房 | S$12,597 | S$11,272–14,022 |
| 自然产 | Mount Elizabeth Novena 1人房 | S$12,724 | S$11,358–14,126 |
| 自然产 | Gleneagles 1人房 | S$13,367 | S$11,954–14,636 |
| 剖腹产 | NUH C | S$2,240 | S$1,796–4,096 |
| 剖腹产 | NUH B2 | S$2,317 | S$1,659–3,211 |
| 剖腹产 | KKH B2 | S$2,733 | S$2,140–3,749 |
| 剖腹产 | KKH C | S$3,148 | S$2,322–4,763 |
| 剖腹产 | KKH A 1人房 | S$9,814 | S$8,304–11,457 |
| 剖腹产 | Thomson 4人房 | S$11,502 | S$8,578–13,665 |
| 剖腹产 | Thomson 2人房 | S$13,540 | S$12,221–15,281 |
| 剖腹产 | Thomson 1人房 | S$15,074 | S$13,491–17,230 |
| 剖腹产 | Mount Elizabeth Orchard 1人房 | S$19,494 | S$17,167–21,545 |
| 剖腹产 | Mount Elizabeth Novena 1人房 | S$18,694 | S$17,278–20,941 |
| 剖腹产 | Gleneagles 1人房 | S$21,556 | S$19,592–23,986 |

出处：
- 自然产 SI836U：https://www.moh.gov.sg/managing-expenses/bills-and-fee-benchmarks/cost-financing/tosp-si836u-bill-information/
- 剖腹产 SI834U：https://www.moh.gov.sg/managing-expenses/bills-and-fee-benchmarks/cost-financing/tosp-si834u-bill-information/
- 复杂自然产 SI833U / 复杂剖腹产 SI844U 见 prices.json

无痛 Epidural：公立津贴基本包含 / 很少；KKH B1 ~S$800–1,200，A ~S$1,000–1,500；私立 S$1,200–2,000。麻醉医生基准 S$817.50–1,090（MOH）。二手范围价，可编辑。

紧急转剖腹产：**MOH 没有单独的紧急剖腹产价。** App 逻辑：按同一医院/房型的剖腹产中位数收，不是自然产+剖腹产叠加。住院 3–4 天 vs 2 天。默认概率 8%，可在设置里改。凌晨 / 周日手术附加费 S$5,000 只有 Lemon8 一则传闻，未在医院官网验证，**不要硬编**。

## 3. 补贴 Subsidies — 净开销算法

### MediSave Maternity Package（SC + PR）
- 产前最多 S$900
- 自然产 S$1,120；辅助自然产 S$1,390；剖腹产 S$2,380
- 住院 S$1,130/天（前2天），第3天起 S$400/天
- 算例：自然产2天最多 S$4,280；剖腹产3天最多 S$5,940
- 出处：https://www.cpf.gov.sg/member/infohub/educational-resources/what-you-need-to-know-about-the-medisave-maternity-package

### MediSave Grant for Newborns
- S$5,000，2025-04-01 后出生的 SC 宝宝，自动进宝宝 MediSave。**不是现金，不要从现金成本里扣。**
- 出处：https://www.cpf.gov.sg/service/article/what-is-the-medisave-grant-for-newborns

### Baby Bonus（2027-04-01 前出生，孩子须为 SC）
| 胎次 | Cash Gift 总额 | CDA First Step | CDA 配对上限 |
|---|---|---|---|
| 1st | S$11,000 | S$5,000 | S$4,000 |
| 2nd | S$11,000 | S$5,000 | S$7,000 |
| 3rd/4th | S$13,000 | S$10,000 | S$9,000 |
| 5th+ | S$13,000 | S$10,000 | S$15,000 |
- Cash Gift 是分期发的，出生时 1st/2nd 只有 S$3,000，不是全额到手。CDA 是专款，不能当现金花。
- 出处：https://www.msf.gov.sg/what-we-do/support-families-and-parents/article/programmes/Baby-Bonus-Scheme

### SG Child Support Package（2027-04-01 后出生）
- 总额最高 S$62,000，不分胎次：Baby Gift S$10,000 + Child Credits S$2,000/年 ×16年 + CDA First Step S$5,000 + CDA 配对 S$5,000 + PSEA S$10,000（17岁）。
- App 必须按模拟出生日期切换两套表，**不要混用**。
- 出处：https://www.life.gov.sg/family-parenting/benefits-support/sg-child-support-package

### 身份差
- SC：公立 C 房最高 80% 津贴，B2 65%，需经济审查。
- PR：津贴低于 SC（专科诊所 PR 最高 25% vs SC 70%）。Baby Bonus / CDA / MGN 只有孩子是 SC 才有。
- 外国人：无津贴、无 MediSave、无 Baby Bonus / CDA / MGN，按公立无津贴价或私立价。

## 4. 0–1 岁

| 项目 | 价格 SGD | 出处 |
|---|---|---|
| 奶粉 中档 每月3罐 | ~S$220/月 | FairPrice 2026-11：Aptamil Gold+ 900g S$73.45，NAN 850g S$71.85，S-26 900g S$71.80。预算 FairPrice Gold S$31.09/罐 ~S$93/月；高端 Enfamil Gentlease S$89.90/罐。默认 3罐/月，范围 2–5罐。 |
| 尿不湿 中档 每月 | ~S$95/月 | FairPrice：Pampers M 64片 S$24.45（S$0.39/片），Huggies Platinum M S$28.17。用量 0–3月 8–12片/天，6–12月 5–7片/天。预算 MamyPoko ~S$70/月，高端 Merries ~S$95–127/月。 |
| 湿纸巾 每月 | ~S$20/月 | FairPrice：Huggies 3×80 S$11.15，Pigeon 6×70 S$17.80 |
| 婴儿床 IKEA SNIGLAR | S$129 | IKEA SG 2026-11。床垫另加 S$40–170。中档可转换床 S$319–419。 |
| 推车 | 预算 S$299 / 中档 S$799 | Shopee：Aprica Nano S$298.90，Luxuna S$698.90；FairPrice 预算 S$179 |
| 安全座椅 | S$299–499 | MissLobang 2026-11-16：i-Max 360 S$299，Maxi-Cosi S$399–499 |
| 吸奶器 双边电动 | S$389–799 | HoneyKids / Sassy Mama 二手指南，Spectra S1+ S$389，Medela Freestyle S$799 — 需在商家处复核 |
| NCIS 疫苗 政府诊所 SC | S$0 | MOH NCIS，SC 孩子在政府诊所全免。PR 约 S$10–30/剂（二手），私立 S$50–150/剂（二手） |
| 政府诊所看诊 SC <18岁 | S$9/次 | NHG 2026-08-01 起 S$9.00。私立 GP S$40–80，儿科 S$50–150 |
| KKH 儿童急诊 | S$176/次 | KKH 官网 2026-08-08 生效 |

## 5. 托育 / 幼儿园

| 项目 | 价格 SGD | 出处 |
|---|---|---|
| 托婴 Anchor 全日 津贴前 | S$1,346.15/月（含 GST） | MSF / E-Bridge 上限 2026-01-01：S$1,235 未含 GST。Basic Subsidy 工作 -S$600 / 非工作 -S$150。净价工作约 S$746.15/月。Partner 上限 S$1,290 未含 GST。私立 EtonHouse S$3,225 未含 GST。 |
| 托儿所 Anchor 全日 津贴前 | S$664.90/月（含 GST） | 上限 2026-01-01：S$610 未含 GST。Basic Subsidy 工作 -S$300。净价工作 S$364.90/月。Partner 上限 S$650 未含 GST。MOE Kindergarten SC S$160/月 半日。 |
| 3–6岁 幼儿园 Anchor 半日 | S$163.50/月（含 GST） | PCF 公布价 |
| 私立幼儿园 | S$900–2,600+/月 | 目录价，不同校区差很大，标范围 + “向中心确认” |

补贴：Basic Subsidy 全日托儿所工作 S$300/月；Additional Subsidy 按家庭收入分级，最高 S$467/月（托儿所）/ S$710/月（托婴），用 ECDA 表，不要只硬编一个最高值。2027-01-01 起 Additional Subsidy 收入上限从 S$12,000 升到 S$15,000。
出处：https://www.madeforfamilies.gov.sg/child-raising/preschool/subsidies-for-preschool/

## 6. 3–6 岁兴趣班 / 坐月子 / 随机事件

| 项目 | 价格 SGD | 出处 |
|---|---|---|
| Kumon 数学 一科 | S$170/月 | Kumon SG 官网价，2026-08–10 核查 |
| 游泳 ActiveSG | S$70–90 / 4节课 | SwimSelectSG。私立游泳学校 S$120–200/月 |
| 钢琴 Yamaha 一对一 Grade 1 | S$232/月 | Yamaha SG 官网 |
| 华文 Berries | ~S$265/月 | S$35–55/节，S$560–880/学期，无单一官网价，用范围 |
| 陪月嫂 住家28天 | S$3,880–4,600 | PEM / NewBubs 2026。MOM levy SC孩子 S$60/月，非SC S$300/月。红包/药材另计。 |
| 月子餐 午+晚28天 | S$1,478–1,828 | ReLacto S$1,478；Chilli Padi S$1,828，2026-11 |
| 宝宝发烧看医生 | 政府诊所 S$9 / GP S$40–80 | NHG；Parentlah |
| 手足口病 / 中耳炎 | 儿科 S$80–150 全包 | SBCC / Thomson，MissLobang 2026-11-06 |
| 摔伤急诊 | KKH S$176 | KKH 官网 |
| 补牙 政府诊所 | S$20.20–36.10/颗（树脂） | SingHealth Polyclinic；私立 S$80–250 |
| 生日派对 10个孩子 | S$490–860 | ExploreJungle 2026-11 |

## 7. 未验证 — 不要硬编

- 首次产检血检单价、GBS 单价、生长 scan 单价、政府诊所产检单价
- 紧急剖腹产凌晨附加费 S$5,000（仅 Lemon8 传闻）
- PR 病房津贴精确 %（只验证了专科诊所 25%）
- 三胎以上 Large Family MediSave Grant S$5,000（二手提及，CPF 页未找到）
- KKH 产前套餐 S$818（二手，未在 KKH 官网找到）
- 0–6岁各保险公司 Integrated Shield Plan 儿童保费（只有 S$200–600/年二手范围）
- 校车费、儿童地铁优惠、假期营价格、丢东西 replacement 价
- 婴儿浴盆、奶嘴、护臀霜、Johnson's 洗发水（2026-11 扫 FairPrice 未找到干净价）

## 8. 版本历史

- v1.0.0 — 2026-11-20：首次研究版。MOH 分娩价为 2023 年实际账单中位数；FairPrice / KKH / ECDA / CPF / MSF 价为 2026-11 公开价。
- v1.1.0 — 2026-11-20：新增双胞胎、黄疸、NICU 分级、妊娠糖尿病/高血压、孩子状态、礼物/满月/百日/抓周、常备药箱、女佣、母乳 vs 奶粉、二手、通胀 2.0%、利息 2.5%。见 §9。
- 下次复核：2026-12-20 前跑 `scripts/check_prices.py`，见 `docs/WIKI.md`。

## 9. v1.1 新增 — 出处

### 双胞胎
- 双胞胎约 1.4%（ICA 2015–2024：5,161 对，~516/年），三胞胎约 0.025%（86 组）。IVF 单胚胎 <1%，双胚胎 20%（KKIVF）。
- 出处：https://www.straitstimes.com/singapore/community/12-sets-of-triplets-born-in-2024-amid-the-changing-face-of-multiple-births-in-singapore

### 黄疸
- 新生儿约 60% 有黄疸，约 10% 需要照光（10% 为二手市场报告引 NCBI，标 estimate）。
- 公立医院照光 S$200–400/天，私立 S$500–1,000+/天（二手指南）；在家租蓝光毯 Doctor Anywhere S$298/3D2N，Baby Specialist S$299–399。
- 出处：https://doctoranywhere.com/home-treatment-jaundice/ ；https://thebabyspecialist.com.sg/collections/jaundice-home-phototherapy

### 早产 / NICU — 按 MOH DRG 总账单，不按天算
- 早产率 8.5%（2024，MOH）。
- 晚期早产无问题 S$721，2000–2499g 其他问题 S$1,331、重大问题 S$4,885，1500–1999g S$5,534，1250–1499g S$17,030（Ward C 中位数，2023 年）。
- 出处：MOH DRG P64Z / P65C / P66B / P66C / P66D，见 `prices.json` 的 `nicu_tiers_moh_drg`。

### 妊娠并发症
- 妊娠糖尿病约 20–25%（GUSTO 18.9%），额外约 S$500（二手，可编辑），Thomson HOPE S$380。
- 子痫前期约 4%（KKH 3.6%），双胞胎 7.5%、三胞胎 19.4%。无 MOH 单独账单，用剖腹产中位数作 proxy，标明。

### 礼物 / 满月 / 百日 / 抓周
- 生日礼物 S$30–70/年、圣诞礼物同范围（玩具价推算，modelled）。
- 新年红包给自己孩子 S$88（范围 S$68–188，SmartLocal / You.co CNY 2026）。
- 满月家里简约 S$1,344（礼盒 30×S$11.90 + 餐饮 30×S$22.90 + 蛋糕 S$100 + 布置 S$200）；礼盒每盒 S$5.90–30.90；百日同满月价，二选一不重复算；抓周 S$5–20 二手（Carousell），抓周是 1 岁生日，不是百日。
- 生日派对场地 S$490–860（10 个孩子，ExploreJungle 2026-11-11），蛋糕 S$65–100 另计。

### 常备药箱
- 不含每日益生菌：S$10–30/月；含每日 BioGaia：S$60–75/月。
- Panadol S$9.75、KoolFever S$7.08、Sterimar S$19.55、DDROPS 维生素 D S$37.30/90 滴（~S$12.43/月）、BioGaia S$50.15。体温计 S$12 一次性。
- 出处：FairPrice / Guardian / Watsons 2026-11。

### 女佣 / 母乳 / 二手 / 经济
- 女佣：菲律宾 S$650–900/月、印尼 S$550–800、缅甸 S$450–800；levy 标准 S$300/月，优惠 S$60/月（SC 孩子 <16 岁，MOM 规则是 <16 不是 <7）；中介 total S$1,000–3,000；全包约 S$1,205–1,430/月。
- 母乳全喂每月省约 S$150–190（推算：奶粉 S$220 省下，减吸奶器摊销 + 耗材）。
- 二手：通用 40–60% off，高端/套装 50–90% off；二手安全座椅要查过期/事故史，不能当全新。
- 通胀默认 2.0%/年（MAS 2026 预测约 2.0%，2025 年 0.9%）；利息默认 2.5%/年（CPF OA floor，SSB 10 年平均 2.25%），标明是模拟假设，不是银行利率。

### 结束模拟 — 选项 A
- 仅玩家主动选择，不随机触发流产/终止事件。早期流产率约 1/5（KKH）仅作资料，不做游戏事件。
