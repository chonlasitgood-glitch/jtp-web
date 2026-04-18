🤖 Agent Instructions: JTP School Website Project

📌 Project Overview

โปรเจกต์นี้คือเว็บไซต์หลักของ โรงเรียนจังหารฐิตวิริยาประชาสรรค์ (Janghanthitviriyaprachasan School - JTP) เป็นเว็บไซต์ประเภท Static Website ที่เน้นความรวดเร็ว สวยงาม ทันสมัย และดูแลรักษาง่ายโดยไม่ต้องมีระบบ Backend ซับซ้อน

🛠 Tech Stack & Architecture

Frontend: HTML5, Vanilla JavaScript

Styling: Tailwind CSS (ผ่านระบบ CDN)

Icons: Lucide Icons (ผ่านระบบ CDN)

Fonts: Google Fonts (Prompt)

Data Source (News): Google Apps Script (GAS) ดึงข้อมูลจาก Google Sheets เสมือนเป็น API

Hosting: Firebase Hosting (มีการเปิดใช้งาน cleanUrls: true)

📂 File & Folder Structure

โครงสร้างไฟล์ทั้งหมดที่ใช้แสดงผลจะอยู่ในโฟลเดอร์ public/ สำหรับการ Deploy ผ่าน Firebase:

/
├── firebase.json         # การตั้งค่า Firebase (ชี้ไปที่โฟลเดอร์ public และทำ Clean URL)
└── public/               # โฟลเดอร์หลักสำหรับ Deploy
    ├── index.html        # หน้าหลัก (Hero, News, E-Service, ITA, About)
    ├── news.html         # หน้าข่าวประชาสัมพันธ์ (ดึงข้อมูลผ่าน GAS และมีระบบ Filter เดือน)
    ├── ita-online.html   # หน้าศูนย์รวม ITA ประจำปี (ITA Hub)
    ├── 404.html          # หน้า Error Custom 404
    ├── logo/             # โฟลเดอร์เก็บโลโก้
    │   ├── jtplogo.png   # โลโก้หลัก (Transparent)
    │   └── jtplogo.ico   # Favicon
    ├── photo/            # โฟลเดอร์เก็บภาพบรรยากาศโรงเรียน (Grid ด้านล่างของ Hero)
    │   ├── photo1.jpg    
    │   ├── photo2.jpg    
    │   └── photo3.jpg    
    └── poster/           # โฟลเดอร์เก็บภาพสไลด์โปสเตอร์
        ├── poster1.jpg   
        ├── poster2.jpg   
        └── ... (dynamic)


🎨 Design System & UI/UX Guidelines

Primary Color: โทนสีเหลืองทอง (Yellow/Amber) รหัสหลักคือ primary-500: '#eab308'

Backgrounds: เน้นสีขาวและสีเทาอ่อน (#fcfcfc, #fafafa) พร้อมลูกเล่น Background Patterns (Grid, Dots) และ Animated Blobs

UI Elements:

เน้นดีไซน์แบบ Glassmorphism (โปร่งแสงและเบลอพื้นหลัง backdrop-blur)

ใช้ Soft Shadows (shadow-sm, shadow-[0_10px_40px_-10px_rgba(0,0,0,0.08)]) ไม่ใช้เงาที่เข้มเกินไป

การ์ดต่างๆ ต้องมี Hover Effect ที่ขยับลอยขึ้น (translateY(-5px))

รูปแบบปุ่มและกล่องข้อความเน้นมุมโค้งมน (rounded-xl, rounded-2xl, rounded-[2rem])

⚙️ Core Logic & Important Features (ห้ามทำพัง)

Dynamic Poster Slider (index.html): - ระบบจะใช้ JavaScript เช็คไฟล์ภาพในโฟลเดอร์ ./poster/ อัตโนมัติ (เริ่มจาก poster1.jpg, poster2.jpg ไปเรื่อยๆ)

คำเตือนสำหรับ AI: ห้ามลบฟังก์ชัน checkPosterExists และ loadDynamicPosters เด็ดขาด เพราะเป็นหัวใจหลักในการทำสไลด์แบบไม่ต้องแก้โค้ด HTML

News Fetching (GAS API):

ดึงข้อมูลข่าวจาก https://script.google.com/macros/s/AKfycbxgcdL_LkCeJD1BLM-8--KSgggwYa4d9HdnMyvxoiklxgqfC3s5BQH2Qgxiu5fRsn8u7A/exec

ในหน้า index.html ดึงแค่ 5 ข่าวล่าสุดแบบต่อเนื่อง

ในหน้า news.html มีการใช้ตัวกรองตามเดือนและช่องค้นหา

Image Modal (Lightbox):

ทุกภาพในข่าว หรือภาพใน Hero Section สามารถคลิกเพื่อดูรูปขยายใหญ่ได้ผ่านฟังก์ชัน openModal(imgSrc)

📜 AI Developer Rules (ข้อบังคับในการเขียนโค้ด)

ห้ามนำ Tailwind CLI/NPM มาใส่: เว็บไซต์นี้ตั้งใจใช้ Tailwind ผ่าน CDN (<script src="https://cdn.tailwindcss.com"></script>) พร้อมกำหนด tailwind.config ไว้ใน <head> เพื่อความสะดวกในการใช้งานแบบไฟล์เดียว

รักษาความเข้ากันได้ของ Path: การอ้างอิงไฟล์รูปภาพหรือหน้าเว็บอื่น ให้ใช้ Relative Path เสมอ เช่น ./photo/photo1.jpg (ไม่ต้องมี /public/ นำหน้า เพราะ Firebase มองโฟลเดอร์นี้เป็น Root แล้ว)

การออกแบบ Responsive: โค้ดทั้งหมดต้องรองรับ Mobile-First โดยใช้ sm:, md:, lg: ของ Tailwind เป็นหลัก

ภาษาไทย (Thai Language): โค้ดที่เป็นส่วนแสดงผล (UI Text) และคอมเมนต์อธิบายโค้ด ต้องใช้ ภาษาไทย เป็นหลัก

Clean URLs: เนื่องจากใช้ Firebase cleanUrls: true การอ้างอิงลิงก์ภายใน (Internal Links) สามารถ เขียนแบบไม่มีนามสกุลได้ (แต่เพื่อให้รันบนเครื่อง Local สมบูรณ์ แนะนำให้เขียนเต็ม news.html ไปก่อน Firebase จะจัดการลบให้ตอนแสดงผลเอง)