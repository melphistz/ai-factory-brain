---
name: director-styles-knowledge
description: Famous film director visual styles + deadpan visual comedy family (Keaton/Tati/Andersson/…) — keyword refs for Style/Camera/Lighting in video prompts, incl. when director names actually work
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# สไตล์ผู้กำกับชื่อดัง — ความรู้สำหรับอ้างอิงเวลาทำวิดีโอ/เขียน Prompt

> สรุปจากการค้นเว็บ (มิ.ย. 2026) เพื่อใช้เป็น "ภาษากลาง" เวลาพูดถึงสไตล์หนัง — แหล่งที่มาอยู่ท้ายไฟล์
> ใช้คู่กับ [[seedance-knowledge]] ได้: หยิบคีย์เวิร์ดสไตล์ของแต่ละคนไปใส่ในช่อง Style/Camera/Lighting ของ prompt · MV ดราม่าดู [[mv-directors-knowledge]]

---

## ⭐ ใส่ "ชื่อผู้กำกับ" ลง prompt จำเป็นไหม? (อ่านก่อนใช้)

**สรุป: คีย์เวิร์ดคือตัวที่ทำงานจริง ส่วนชื่อเป็นแค่ "โบนัส"** — เพราะชื่อผู้กำกับคือกล่องดำ เราคุมไม่ได้ว่าโมเดลตีความเป็นอะไร ขณะที่คีย์เวิร์ดรูปธรรม (neon, symmetry, deep focus) คือสิ่งที่โมเดล "ทำตามได้" ไม่ว่าจะรู้จักชื่อหรือไม่

| วิธีใส่ | ผล |
|--------|-----|
| ใส่แค่ชื่อ `"Nawapol style"` ลอยๆ | ❌ เสี่ยง คุมไม่ได้ โดยเฉพาะผู้กำกับที่ data น้อย |
| ใส่แค่คีย์เวิร์ด (ไม่มีชื่อ) | ✅ ปลอดภัย ทำงานจริง |
| **ชื่อ + คีย์เวิร์ด** | ✅✅ ดีสุด — คีย์เวิร์ดคุม, ชื่อเป็นโบนัส |

**เกณฑ์ว่าชื่อจะ "ได้ผล" แค่ไหน = data ของผู้กำกับคนนั้นในชุดเทรนมีเยอะไหม:**
- 🟢 **ระดับโลก data เยอะ → ชื่ออาจช่วยจริง:** Kurosawa, Nolan, Kubrick, Wes Anderson, Fincher, Tarantino, Spielberg, Wong Kar-wai (ลองใส่ชื่อได้ มีโอกาสโมเดลรู้จัก)
- 🔴 **อินดี้/ภูมิภาค data น้อย → อย่าพึ่งชื่อ:** เต๋อ นวพล, อภิชาติพงศ์, วิศิษฏ์ (ต้องมีคีย์เวิร์ดคุมเสมอ ชื่อแทบไม่ช่วย)

**กฎเหล็ก:** ไม่ว่าผู้กำกับดังแค่ไหน **ต้องมีคีย์เวิร์ดอธิบายเสมอ** — ห้ามใส่แค่ชื่อลอยๆ แล้วฝากชะตาไว้กับโมเดล
**วิธีเช็กว่าชื่อมีผลจริง:** generate 2 รอบ (มีชื่อ / ลบชื่อเหลือแต่คีย์เวิร์ด) แล้วเทียบ

---

## หว่อง กาไว (Wong Kar-wai)
**อารมณ์:** โรแมนติก เหงา โหยหา nostalgic เมืองยามค่ำคืน
- **Step-printing** — ถ่ายเฟรมเรตต่ำแล้วซ้ำเฟรม ได้ภาพ "เบลอแต่ช้า" ตัวละครเคลื่อนช้าท่ามกลางฝูงชนที่เร็วเบลอ
- **กล้องมือถือ (handheld)** ร่วมกับตากล้อง Christopher Doyle — ดูสมจริง อึดอัด แออัด
- **สีจัดเป็นภาษา** — แดง = หลงใหล/โหยหา, เขียว = เศร้า/คิดถึง; ใช้นีออน แสงธรรมชาติ เงา
- **เฟรมแคบ/บางส่วน** — close-up มุมเอียง สะท้อนเงา shallow depth of field โฟกัสที่ "ใจ" ตัวละคร
- **โมทีฟ** ฝน น้ำ นาฬิกา/เวลา
- หนังอ้างอิง: *In the Mood for Love*, *Chungking Express*, *Fallen Angels*

## เวส แอนเดอร์สัน (Wes Anderson)
**อารมณ์:** whimsical น่ารักแปลกๆ เหมือนหนังสือนิทาน/ฉากละครเวที
- **สมมาตร (symmetry) จัดเป๊ะ** — ทุกเฟรมสมดุลทางคณิตศาสตร์ ตัวแบบอยู่กลางเฟรม
- **Planimetric staging** — กล้องตั้งฉาก 90° หน้าตรง (ตั้งแต่ *The Royal Tenenbaums*)
- **พาเลตต์พาสเทล** — ชมพู ฟ้า เขียวอ่อน + คู่สีตรงข้าม (ส้มอุ่น/ฟ้าเย็น); สีกำหนดล่วงหน้าคุมทั้งฉาก เสื้อผ้า พร็อพ
- การเคลื่อนกล้องแบบกลไก: whip pan, snap zoom, dolly แนวตรง, top-down (ภาพมุมก้มของสิ่งของ)
- หนังอ้างอิง: *The Grand Budapest Hotel*, *Moonrise Kingdom*, *Asteroid City*

## คริสโตเฟอร์ โนแลน (Christopher Nolan)
**อารมณ์:** จริงจัง ยิ่งใหญ่ ตึงเครียด ปรัชญาเรื่องเวลา
- **ฟิล์มจริง 35mm/65mm IMAX** — เกรน ละเอียด สเกลใหญ่ ไม่ค่อยพึ่ง CGI
- **เอฟเฟกต์จริง (practical effects) in-camera** — ฉากระเบิด/แอ็กชันถ่ายจริง
- **เล่นกับเวลา** — เล่าแบบไม่เรียงเส้น (non-linear), เวลาคู่ขนาน/ย้อนกลับ
- มุมกล้อง: handheld อึดอัด, aerial wide, barrel roll, Dutch angle สร้างความสับสน
- สี muted, เลือก 1 สีหลักแล้วสร้างพาเลตต์รอบๆ; แสงแบบธรรมชาติ; เมือง คนใส่สูท สถาปัตยกรรมโมเดิร์น
- หนังอ้างอิง: *Inception*, *Interstellar*, *Tenet*, *Oppenheimer*

## อากิระ คุโรซาวะ (Akira Kurosawa)
**อารมณ์:** มหากาพย์ ทรงพลัง ภาพจัดวางแบบจิตรกรรม (เคยเรียนวาดภาพ)
- **Deep focus + เลนส์ไวด์** — เห็นคมชัดทั้งหน้า-หลังเฟรม สร้างมิติ
- **กล้องเคลื่อนตลอด** — tracking, dolly, crane สร้างโมเมนตัม
- **มัลติคาเมรา** — ถ่ายฉากแอ็กชันหลายมุมพร้อมกัน (บุกเบิก)
- **องค์ประกอบกราฟิกเด่น** — ใช้สภาพอากาศเป็นตัวละคร (ฝน หมอก ลม ฝุ่น โคลน)
- **Wipe transition** จนกลายเป็นลายเซ็น; ตัดสลับจังหวะแอ็กชันเพื่ออารมณ์
- หนังอ้างอิง: *Seven Samurai*, *Rashomon*, *Ran*, *Yojimbo*

## สตีเวน สปีลเบิร์ก (Steven Spielberg)
**อารมณ์:** มหัศจรรย์ อารมณ์ร่วม เล่าเรื่องด้วยภาพล้วน
- **กล้องเคลื่อนทุกทิศในช็อตเดียว** — รวม dolly + crane + track เข้าด้วยกันลื่นไหล
- **"L system" blocking** — กล้องเคลื่อนเป็นรูปตัว L พร้อมตัวแสดงเคลื่อนสอดคล้องกัน
- **The Spielberg Oner** — ลองเทคยาวที่ขับเคลื่อนด้วยอารมณ์ ไม่หวือหวา เล่าหลายอย่างในช็อตเดียว
- **Eye trace** — นำสายตาคนดูด้วยการเคลื่อน แสง สี โดยไม่ต้องตัด
- "Spielberg face" — close-up สีหน้าตื่นตะลึง/อัศจรรย์
- หนังอ้างอิง: *Jaws*, *E.T.*, *Jurassic Park*, *Saving Private Ryan*

## เอ็ดการ์ ไรท์ (Edgar Wright)
**อารมณ์:** สนุก เร็ว ตลก จังหวะดนตรี (comedy ภาพ)
- **Hyperkinetic editing** — ตัดเร็วรัวๆ ทำเรื่องน่าเบื่อ (ทาเนย/ชงชา) ให้เป็นซีนมันส์ด้วย extreme close-up
- **ทรานสิชันสร้างสรรค์** — whip pan, wipe, match cut, snap zoom เชื่อมฉาก
- **ตัดตามบีตเสียง/ดนตรี** (sound-driven editing) — sync ภาพกับ sound design
- Steadicam tracking, dolly zoom, มอนทาจแอ็กชันเร็ว
- หนังอ้างอิง: *Shaun of the Dead*, *Hot Fuzz*, *Baby Driver*, *Scott Pilgrim*

## เควนติน ทารันติโน (Quentin Tarantino)
**อารมณ์:** เท่ดิบ รุนแรงสไตล์ exploitation บทพูดยาวๆ
- **Trunk shot** — มุมกล้องจากในกระโปรงท้ายรถมองขึ้น (ลายเซ็น)
- **Crash zoom** — ซูมกระแทกเรียกความสนใจ; low angle โชว์อำนาจตัวละคร
- **ลองเทค/ทแร็คกิ้งยาว** + ไวด์ช็อตให้เห็นรายละเอียดโลก
- **สีหลักจัดจ้าน** — เหลือง canary (*Kill Bill*), แดงสด, น้ำเงิน royal เพื่อกระตุ้นอารมณ์
- **ดนตรีสวนทาง** — เพลงเพราะคุมฉากรุนแรง; ยืดเวลาในซีนเพื่อสร้างความตึง
- หนังอ้างอิง: *Pulp Fiction*, *Kill Bill*, *Inglourious Basterds*, *Once Upon a Time in Hollywood*

## เดวิด ฟินเชอร์ (David Fincher)
**อารมณ์:** มืด เย็น เนี้ยบ สะกดจิต thriller
- **กล้องนิ่ง เคลื่อนเมื่อมีเหตุผลเท่านั้น** — match กับการเคลื่อนของนักแสดง
- **Low-key lighting + เงาหนัก** — มืด คอนทราสต์สูง
- **ย้อมทั้งฉากด้วยสีเดียว** (เช่นเขียว/เหลือง) เพื่อแยกโลก/อารมณ์
- **กล้องลื่นทะลุทุกอย่าง** — ไหลผ่านผนัง ท่อ บันได (มักทำด้วย CG เนียนๆ)
- **เพอร์เฟกชันนิสต์** — เทคเยอะมาก (25–65 เทค สูงสุดเคยถึง 100)
- หนังอ้างอิง: *Se7en*, *Fight Club*, *Zodiac*, *The Social Network*, *Gone Girl*

## เดอนี วีล์เนิฟ (Denis Villeneuve)
**อารมณ์:** อลังการ เงียบขรึม ลึกลับ sci-fi ปรัชญา
- **สเกลใหญ่ minimal** — ภาพกว้าง ตัวคนเล็กในพื้นที่มหึมา (มักร่วมกับตากล้อง Roger Deakins)
- **พาเลตต์จำกัด เน้นคอนทราสต์มากกว่าความสด** — โทนสีตามธีม
- **จังหวะช้า อดทน ลองเทค** — voyeuristic, camerawork สงบแต่มั่นใจ
- มุมเอียง/กลับหัวเพื่อสื่อความโกลาหล; สกอร์ทดลอง ambient หนักๆ (มักโดย Hans Zimmer)
- หนังอ้างอิง: *Blade Runner 2049*, *Dune*, *Arrival*, *Sicario*

## สแตนลีย์ คูบริก (Stanley Kubrick)
**อารมณ์:** เนี้ยบจนหลอน สมมาตร เย็นชา จิตวิทยา
- **One-point perspective** — จุดรวมสายตากลางเฟรมพอดี (ทางเดิน/ห้องพุ่งเข้าหาจุดศูนย์กลาง) สร้างความสะกดจิต/อึดอัด
- **เลนส์ไวด์ 24mm** — ขยายมิติ ทางเดินยาวขึ้น เพดานสูงขึ้น
- **สมมาตรเป๊ะ** + ความแม่นยำระดับขยับกล้องทีละนิ้วเพื่อหาจุดศูนย์กลางที่เป๊ะ
- แสง/พื้นที่: โถงโรงแรมหลอน ค่ายทหารแข็งทื่อ อวกาศปลอดเชื้อ
- หนังอ้างอิง: *The Shining*, *2001: A Space Odyssey*, *A Clockwork Orange*, *Full Metal Jacket*

## ฮายาโอะ มิยาซากิ (Hayao Miyazaki)
**อารมณ์:** มหัศจรรย์ อบอุ่น เป็นมิตรกับธรรมชาติ (อนิเมชันวาดมือ)
- **วาดมือทุกเฟรม** — โลกละเอียด การเคลื่อนไหวลื่นไหลมีชีวิต (ดินสอคือเครื่องมือ)
- **ทิวทัศน์ธรรมชาติ** — ทุ่งเขียว ฟ้าใส เมฆนุ่ม โทนสีอ่อนนุ่ม บรรยากาศเหมือนฝัน
- **โมทีฟการบิน** — อิสรภาพ หลุดพ้นแรงโน้มถ่วง
- ธีม: coming-of-age, สิ่งแวดล้อม, ต่อต้านสงคราม, นางเอกเข้มแข็ง, ตัวร้ายมีมิติ (ไม่ขาว-ดำ)
- เทคนิคเล่าเรื่องญี่ปุ่น **Kishōtenketsu** (เน้นพัฒนามากกว่าความขัดแย้ง)
- หนังอ้างอิง: *Spirited Away*, *My Neighbor Totoro*, *Princess Mononoke*, *Howl's Moving Castle*

## เดวิด ลินช์ (David Lynch)
**อารมณ์:** เซอร์เรียล หลอน "Lynchian" — ความน่ากลัวซ่อนใต้สิ่งดูปกติ
- **เซอร์เรียล + Americana** — ฉากบ้านๆ ปนความประหลาด อึดอัด
- **มืด หมอก เงา พื้นที่ปิดแคบ** + แสงแบบ expressionist
- **กล้องลอยตลอด** สร้างความหลอน; ตัดต่อแบบไม่ต่อเนื่อง (disjunctive) เล่าแบบ elliptical
- **โมทีฟซ้ำ** — ม่านแดง สัญลักษณ์ลึกลับ; **sound design** สำคัญมาก (เสียงไม่ตรงกับความจริงของฉาก)
- ภาพกำกวม ตีความเอง
- หนังอ้างอิง: *Mulholland Drive*, *Twin Peaks*, *Eraserhead*, *Blue Velvet*

## ไมเคิล เบย์ (Michael Bay)
**อารมณ์:** ระเบิดภูเขาเผากระท่อม อลังการ "more is more" — เรียกว่า **"Bayhem"**
- **กล้องไม่หยุดนิ่งเลย** — tracking + panning ตลอด เติม "ความเงียบทางภาพ" ด้วยการเคลื่อน
- **มุมหมุนรอบ low-angle hero shot** — ตัวละครยืนเท่ๆ กล้องวนรอบ ฟ้าสีส้มทอง
- **สโลว์โมชัน + ตัดเร็ว + เฟรมเอพิค** + แสงเรืองรอง (lens flare, แสงทะลุ)
- **เอฟเฟกต์จริง+CGI** — ลูกไฟจริง เศษซากปลิว; เสียงดังกระหึ่มซ้อนชั้น
- ปรัชญา: ทุกเฟรมยัดการเคลื่อนไหว/รายละเอียดเต็มไปหมด — chaos แต่คุมได้
- หนังอ้างอิง: *Transformers*, *Bad Boys*, *Armageddon*, *The Rock*

## เกรตา เกอร์วิก (Greta Gerwig)
**อารมณ์:** อบอุ่น มีชีวิตชีวา coming-of-age ผู้หญิง บทพูดคมจริง
- **บทสนทนาธรรมชาติ ทับซ้อน** — ตัวละครพูดแทรก/พูดพร้อมกัน (เคยถอดบทสนทนาคนแปลกหน้ามาใช้)
- **ฉากสุนทรพจน์ไคลแมกซ์** — เป็น mission statement ของหนัง
- **ธีม coming-of-age หญิงสาวค้นหาตัวเอง** + นักแสดงสมทบเยอะ (ensemble)
- สีตามโลก: *Lady Bird* โทนกลางจริงจัง / *Barbie* พาสเทลสดใสจงใจให้ดูปลอม
- หนังอ้างอิง: *Lady Bird*, *Little Women*, *Barbie*

---

# ผู้กำกับไทย

## เต๋อ นวพล ธำรงรัตนฤทธิ์ (Nawapol Thamrongrattanarit)
**อารมณ์:** อินดี้ที่คนทั่วไปดูได้ มินิมอล ใกล้ตัว อารมณ์ขันเงียบๆ
- **มินิมอล มองแบบผู้สังเกตการณ์** — วางกล้องดูสถานการณ์อย่างมีระยะห่าง
- **สุนทรียะอนาล็อก** — กล้องเคลื่อนช้า ภาพอาบแสงแดด พื้นที่ว่าง (white space) เยอะ เฟรม/สีแบบ "ตัดมาลง Instagram"
- **บทสนทนาเข้าปาก เป็นธรรมชาติ** — อารมณ์แรงสุดมักซ่อนระหว่างบรรทัด ผ่านท่าทาง/สายตาเล็กๆ
- **การตลาด/โปรโมตหนังไวรัล** เป็นภาพจำอีกอย่าง
- หนังอ้างอิง: *36*, *Mary Is Happy, Mary Is Happy*, *Die Tomorrow*, *Happy Old Year*, *Heart Attack (ฟรีแลนซ์)*

## อภิชาติพงศ์ วีระเศรษฐกุล (Apichatpong Weerasethakul / "เจ้ย")
**อารมณ์:** slow cinema เหนือจริง จิตวิญญาณ ความฝัน ความทรงจำ
- **กล้องนิ่งสงบ ตัดต่อเนิบช้า** — จังหวะ contemplative เหมือนฝัน
- **เสียงบรรยากาศธรรมชาติ** (จิ้งหรีด ลม) แทนสกอร์อลังการ; นักแสดงไม่ขึ้นเสียง
- ธีม: ความทรงจำ ตัวตน สิ่งเหนือธรรมชาติ ความเชื่อ/ผีไทย ชีวิตชนบท
- ระดับโลก: เจ้าของรางวัลปาล์มทองคำ (*Uncle Boonmee*)
- หนังอ้างอิง: *Uncle Boonmee Who Can Recall His Past Lives*, *Tropical Malady*, *Memoria*

## วิศิษฏ์ ศาสนเที่ยง (Wisit Sasanatieng)
**อารมณ์:** จัดจ้าน เกินจริง โหยหาอดีต ป๊อปไทยคลาสสิก
- **สีจัดจ้านเกินจริง (hyper-saturated)** — เหมือนโปสการ์ด/หนังไทยยุคเก่าย้อมสี
- **เสื้อผ้า/ฉากเซ็ตอลังการเซอร์เรียล** ดึงจากวัฒนธรรมป๊อปไทยและหนังคลาสสิก
- บุกเบิก Thai New Wave ร่วมยุค
- หนังอ้างอิง: *ฟ้าทะลายโจร (Tears of the Black Tiger)*, *หมานคร (Citizen Dog)*

---

# 🎭 สาย Deadpan Visual Comedy (ตลกหน้าตาย เล่าด้วยภาพ)
> ตระกูลเดียวกับเต๋อ นวพล — เหมาะมากกับงาน "ไม่มีบทพูด + หน้านิ่ง + still เยอะ" เช่น [[tuensai-project]]

## บัสเตอร์ คีตัน (Buster Keaton) — ต้นตำรับ
- **"The Great Stone Face"** หน้านิ่งสนิทไม่ว่าเกิดอะไร + ตลกกายภาพ + **หนังเงียบ ไม่มีบทพูด**
- ตลกมาจากร่างกาย/สถานการณ์ ไม่ใช่สีหน้า — รากของ "ตัวรีบ แต่หน้าเฉย"
- หนังอ้างอิง: *The General*, *Sherlock Jr.*, *Steamboat Bill, Jr.*

## ฌาคส์ ตาติ (Jacques Tati)
- ตลกด้วยภาพล้วน บทพูดแทบไม่มี · **ช็อตกว้างสังเกตการณ์** มุกซ่อนอยู่ในเฟรม (deep staging)
- หนังอ้างอิง: *Mon Oncle*, *Playtime*, *Mr. Hulot's Holiday*

## รอย แอนเดอร์สสัน (Roy Andersson)
- **static tableau** เฟรมล็อกนิ่งสนิทช็อตเดียวยาว · deadpan absurd · สีซีดหม่น
- หนังอ้างอิง: *A Pigeon Sat on a Branch...*, *Songs from the Second Floor*

## อากิ เการิสมากิ (Aki Kaurismäki)
- มินิมอล หน้านิ่ง · กรอบนิ่ง สีหม่น แห้งๆ เหงาๆ + ใช้เพลงเก๋ๆ
- หนังอ้างอิง: *The Man Without a Past*, *Le Havre*, *Fallen Leaves*

## ทาเคชิ คิตาโนะ (Takeshi Kitano) — fast-slow
- หน้านิ่ง + **long static take สลับ burst เร็วฉับพลัน** = จังหวะ fast-slow ชัดเจน (ญี่ปุ่น)
- หนังอ้างอิง: *Hana-bi*, *Kikujiro*, *Sonatine*

## เอเลีย สุไลมาน (Elia Suleiman)
- นิ่งเงียบแทบไม่พูด · tableau สมมาตร + มุกกายภาพแบบ Keaton ยุคใหม่
- หนังอ้างอิง: *It Must Be Heaven*, *Divine Intervention*

**จับคู่เทคนิค ↔ การใช้งาน:**
- อยาก **fast-slow** → Kitano (นิ่งสลับ burst), Keaton (รีบกายภาพ)
- อยาก **still tableau นิ่งยาว** → Andersson, Tati, Kaurismäki, Suleiman
- ทั้งหมดเข้ากับเต๋อ นวพลได้ (ตระกูลเดียวกัน) — ผสมคีย์เวิร์ดข้ามกันได้ไม่หลุดสไตล์

---

## ตารางคีย์เวิร์ดเร็ว (เอาไปใส่ prompt วิดีโอ)
| ผู้กำกับ | คีย์เวิร์ดสั้นสำหรับ prompt |
|---------|---------------------------|
| Wong Kar-wai | neon-lit, step-printing blur, saturated red/green, handheld, melancholic close-up |
| Wes Anderson | perfect symmetry, pastel palette, planimetric front-on, whip pan, storybook |
| Nolan | 65mm/IMAX scale, practical effects, muted palette, non-linear, naturalistic light |
| Kurosawa | deep focus, wide lens, weather as character, dynamic crane movement, B&W graphic |
| Spielberg | sweeping camera move, single oner, awe close-up ("Spielberg face"), warm light |
| Edgar Wright | hyperkinetic fast cuts, snap zoom, match cut on sound beats, kinetic montage |
| Tarantino | trunk shot, crash zoom, bold primary color, low angle, long dialogue take |
| Fincher | low-key shadow, single-hue tint, locked-off precise camera, cold desaturated |
| Villeneuve | epic minimal wide, tiny human in vast space, restrained palette, slow patient |
| Kubrick | one-point perspective, dead-center vanishing point, 24mm wide, symmetrical, cold |
| Miyazaki | hand-drawn anime, lush nature, soft palette, dreamlike, flight/sky, gentle |
| Lynch | surreal Americana, floating camera, red curtains, deep shadow, uncanny dread |
| Michael Bay | "Bayhem", constant moving camera, low-angle hero orbit, golden hour, lens flare, explosions |
| Greta Gerwig | warm coming-of-age, overlapping natural dialogue, ensemble, Barbie pastel / Lady Bird muted |
| เต๋อ นวพล | minimalist observer, slow camera, sunlit white space, analog, Instagram framing |
| อภิชาติพงศ์ (เจ้ย) | slow cinema, static serene camera, dreamlike, ambient nature sound, Thai spiritual |
| วิศิษฏ์ | hyper-saturated color, retro Thai postcard, surreal extravagant set/costume |
| Buster Keaton | deadpan stone face, silent physical comedy, static wide, vintage |
| Jacques Tati | observational wide shot, minimal dialogue, visual gag, deep staging |
| Roy Andersson | locked static tableau, deadpan, muted pale palette, single long wide take |
| Aki Kaurismäki | deadpan minimalist, static framing, muted color, dry melancholic |
| Takeshi Kitano | deadpan, long static take, sudden quick burst (fast-slow), restrained |
| Elia Suleiman | silent deadpan tableau, symmetrical, observational, dry wit |

---

## แหล่งที่มา (Sources)
- Wong Kar-wai: [Taste of Cinema](https://www.tasteofcinema.com/2016/the-10-most-distinct-traits-of-wong-kar-wais-cinema/), [Studiovity](https://blog.studiovity.com/wong-kar-wai-cinematic-style-guide/)
- Wes Anderson: [StudioBinder](https://www.studiobinder.com/blog/wes-anderson-style/), [Pixflow](https://pixflow.net/blog/the-ultimate-guide-to-wes-andersons-color-palette/)
- Christopher Nolan: [Wikipedia — Cinematic style of Christopher Nolan](https://en.wikipedia.org/wiki/Cinematic_style_of_Christopher_Nolan), [StudioBinder](https://www.studiobinder.com/blog/christopher-nolan-directing-visual-style/)
- Akira Kurosawa: [Wikipedia — Filmmaking technique of Akira Kurosawa](https://en.wikipedia.org/wiki/Filmmaking_technique_of_Akira_Kurosawa), [Critic Film](https://www.criticfilm.com/akira-kurosawas-filmmaking-style/)
- Steven Spielberg: [StudioBinder](https://www.studiobinder.com/blog/steven-spielberg-movies-filmmaking-style/), [No Film School](https://nofilmschool.com/how-does-steven-spielberg-block-and-shoot-scene)
- Edgar Wright: [Critic Film](https://www.criticfilm.com/edgar-wrights-filmmaking-style/), [Wikipedia](https://en.wikipedia.org/wiki/Edgar_Wright)
- Quentin Tarantino: [StudioBinder](https://www.studiobinder.com/blog/shot-lists-quentin-tarantino/), [Critic Film](https://www.criticfilm.com/quentin-tarantinos-cinema-style/)
- David Fincher: [StudioBinder](https://www.studiobinder.com/blog/david-fincher-movies-directing-styles/), [No Film School](https://nofilmschool.com/david-fincher-filmmaking-style)
- Denis Villeneuve: [StudioBinder](https://www.studiobinder.com/blog/denis-villeneuve-directing-style/), [Taste of Cinema](https://www.tasteofcinema.com/2018/5-traits-of-denis-villeneuves-signature-filmmaking-style/)
- Stanley Kubrick: [Pixflow](https://pixflow.net/blog/kubrick-symmetry-one-point-perspective/), [Open Culture](https://www.openculture.com/2012/09/signature_shots_from_the_films_of_stanley_kubrick.html)
- Hayao Miyazaki: [Greenlight Coverage](https://glcoverage.com/2024/08/21/trademarks-of-hayao-miyazaki-movies/), [Styles and themes of Hayao Miyazaki (wiki)](https://ultimatepopculture.fandom.com/wiki/Styles_and_themes_of_Hayao_Miyazaki)
- David Lynch: [StudioBinder — What Does Lynchian Mean](https://www.studiobinder.com/blog/what-does-lynchian-mean/)
- Michael Bay: [StudioBinder — What is Bayhem](https://www.studiobinder.com/blog/what-is-bayhem-michael-bay-directing-style/), [No Film School](https://nofilmschool.com/2014/07/michael-bay-bayhem-visual-storytelling)
- Greta Gerwig: [IndieWire](https://www.indiewire.com/gallery/greta-gerwig-films-directorial-style-barbie/), [StudioBinder](https://www.studiobinder.com/blog/barbie-director-greta-gerwig/)
- เต๋อ นวพล (Nawapol): [Asian Movie Pulse interview](https://asianmoviepulse.com/2020/02/interview-with-nawapol-thamrongrattanarit-2/), [วิกิพีเดีย](https://th.wikipedia.org/wiki/นวพล_ธำรงรัตนฤทธิ์)
- อภิชาติพงศ์ (เจ้ย): [Wikipedia](https://en.wikipedia.org/wiki/Apichatpong_Weerasethakul), [4Columns](https://4columns.org/chan-andrew/apichatpong-weerasethakul)
- วิศิษฏ์ ศาสนเที่ยง: [Wikipedia](https://en.wikipedia.org/wiki/Wisit_Sasanatieng)
- Deadpan visual comedy (Keaton/Tati/Andersson/Kaurismäki/Kitano/Suleiman): [Buster Keaton — Wikipedia](https://en.wikipedia.org/wiki/Buster_Keaton), [Roy Andersson — Grokipedia](https://grokipedia.com/page/Roy_Andersson), [Elia Suleiman — SBS](https://www.sbs.com.au/whats-on/article/meet-elia-suleiman-palestinian-silent-comedy-auteur/0z4maoa0j), [Kitano — Unseen Japan](https://unseen-japan.com/kitano-takeshi-the-complete-ranked-filmography/)
