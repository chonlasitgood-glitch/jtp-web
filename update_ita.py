import re

with open('/Users/kruboat/Desktop/website/jtp-web/public/ita-online.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add mock data and JS logic at the end before </body>
modal_script_and_html = """
    <!-- OIT PDF Modal -->
    <div id="oit-modal" class="fixed inset-0 z-[100] hidden flex items-center justify-center p-4 sm:p-6 opacity-0 transition-opacity duration-300">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" onclick="closeOitModal()"></div>
        
        <!-- Modal Content -->
        <div class="bg-white rounded-2xl md:rounded-[2rem] shadow-2xl w-full max-w-4xl relative z-10 flex flex-col overflow-hidden max-h-[90vh] md:max-h-[85vh] transform scale-95 transition-transform duration-300" id="oit-modal-content">
            <!-- Header -->
            <div class="px-6 py-4 md:px-8 md:py-6 border-b border-slate-100 flex justify-between items-start gap-4 glass-nav bg-white/95">
                <div>
                    <h3 id="modal-o-title" class="text-xl md:text-2xl font-bold text-slate-900 leading-tight">O1 โครงสร้างและอำนาจหน้าที่</h3>
                    <p id="modal-o-desc" class="text-sm md:text-base text-slate-500 mt-2">รายละเอียดข้อมูลจำลอง...</p>
                </div>
                <button onclick="closeOitModal()" class="w-10 h-10 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-600 transition-colors shrink-0">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            
            <!-- Body (PDF Viewer) -->
            <div class="flex-grow bg-slate-100 relative p-4 md:p-6 overflow-hidden flex flex-col">
                <div class="w-full h-full bg-white rounded-xl border border-slate-200 overflow-hidden shadow-inner flex flex-col min-h-[40vh] md:min-h-[50vh]">
                    <iframe id="modal-pdf-iframe" src="" class="w-full flex-grow border-0" title="PDF Viewer"></iframe>
                </div>
            </div>
            
            <!-- Footer (Actions) -->
            <div class="px-6 py-4 md:px-8 border-t border-slate-100 bg-white flex justify-between items-center flex-wrap gap-4">
                <p class="text-xs text-slate-400"><i data-lucide="info" class="w-3 h-3 inline mr-1"></i> นี่เป็นเพียงข้อมูลจำลองสำหรับทดสอบระบบ</p>
                <a id="modal-download-btn" href="#" target="_blank" class="px-6 py-2.5 bg-primary-500 hover:bg-primary-600 text-slate-900 font-bold rounded-xl shadow-sm transition-colors inline-flex items-center gap-2 text-sm">
                    <i data-lucide="download" class="w-4 h-4"></i> ดาวน์โหลดเอกสาร (PDF)
                </a>
            </div>
        </div>
    </div>

    <script>
        // Mock Data for O1 to O18
        const mockOitData = {
"""

# Extract O1-O18 titles to populate mock data
o_items = {}
pattern = r'<span class="w-12 text-primary-600 font-medium shrink-0 pt-0\.5">(O\d+)</span>\s*<span[^>]*>(.*?)</span>'
matches = re.findall(pattern, html)
for match in matches:
    o_id = match[0]
    title = match[1].strip()
    
    # Generic description
    desc = f"นี่คือรายละเอียดข้อมูลจำลองสำหรับข้อ {o_id} {title} ตามการประเมิน ITA ประจำปีงบประมาณ พ.ศ. 2569"
    # Simple dummy PDF
    pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    
    o_items[o_id] = {
        'title': f"{o_id} {title}",
        'desc': desc,
        'pdfUrl': pdf_url
    }

for k, v in o_items.items():
    modal_script_and_html += f"""            "{k}": {{
                title: "{v['title']}",
                desc: "{v['desc']}",
                pdfUrl: "{v['pdfUrl']}"
            }},
"""

modal_script_and_html += """        };

        // Modal Logic
        const oitModal = document.getElementById('oit-modal');
        const oitModalContent = document.getElementById('oit-modal-content');
        const modalTitle = document.getElementById('modal-o-title');
        const modalDesc = document.getElementById('modal-o-desc');
        const modalIframe = document.getElementById('modal-pdf-iframe');
        const modalDownloadBtn = document.getElementById('modal-download-btn');

        function openOitModal(oId) {
            const data = mockOitData[oId];
            if(!data) return;

            // Set Content
            modalTitle.textContent = data.title;
            modalDesc.textContent = data.desc;
            modalIframe.src = data.pdfUrl;
            modalDownloadBtn.href = data.pdfUrl;

            // Show Modal
            oitModal.classList.remove('hidden');
            // Small delay for transition
            setTimeout(() => {
                oitModal.classList.remove('opacity-0');
                oitModalContent.classList.remove('scale-95');
                oitModalContent.classList.add('scale-100');
            }, 10);
            
            // Re-init lucide if needed or just disable body scroll
            document.body.style.overflow = 'hidden';
        }

        function closeOitModal() {
            oitModal.classList.add('opacity-0');
            oitModalContent.classList.remove('scale-100');
            oitModalContent.classList.add('scale-95');
            
            setTimeout(() => {
                oitModal.classList.add('hidden');
                modalIframe.src = ''; // Clear iframe
                document.body.style.overflow = ''; // Restore body scroll
            }, 300);
        }
    </script>
</body>"""

# Replace <a> elements globally but dynamically targeting the structure
# We find:
# <a href="#" target="_blank" class="flex items-start group">
#    <span class="w-12 text-primary-600 font-medium shrink-0 pt-0.5">OXX</span>
# And replace link targeting.

def replace_a_tag(match):
    full_str = match.group(0)
    o_id = match.group(1)
    
    # We replace href="#" target="_blank" with onclick="openOitModal('OXX')" href="javascript:void(0)"
    new_str = full_str.replace('href="#"', f'href="javascript:void(0)" onclick="openOitModal(\'{o_id}\')"')
    new_str = new_str.replace('target="_blank"', '')
    # Add cursor context just in case
    new_str = new_str.replace('class="flex items-start group"', 'class="flex items-start group w-full text-left cursor-pointer"')
    return new_str

pattern_a_tags = r'<a href="#" target="_blank" class="flex items-start group">\s*<span class="w-12 text-primary-600 font-medium shrink-0 pt-0\.5">(O\d+)</span>'

html = re.sub(pattern_a_tags, replace_a_tag, html)

# Inject modal before </body>
html = html.replace('</body>', modal_script_and_html)

with open('/Users/kruboat/Desktop/website/jtp-web/public/ita-online.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Update completed. Intercepted {len(matches)} O-Items and replaced tags.")
