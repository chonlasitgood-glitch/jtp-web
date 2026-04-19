import re

with open('/Users/kruboat/Desktop/website/jtp-web/public/ita-online.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<span class="w-12 text-primary-600 font-medium shrink-0 pt-0\.5">(O\d+)</span>\s*<span[^>]*>(.*?)</span>'
matches = re.findall(pattern, html, re.DOTALL)

mock_data_content = ''
for match in matches:
    o_id = match[0]
    title = re.sub(r'\s+', ' ', match[1].strip())
    desc = f'นี่คือรายละเอียดข้อมูลจำลองสำหรับข้อ {o_id} {title} ตามการประเมิน ITA ประจำปีงบประมาณ พ.ศ. 2569'
    pdf_url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
    
    mock_data_content += f'''            "{o_id}": {{
                title: "{o_id} {title}",
                desc: "{desc}",
                pdfUrl: "{pdf_url}"
            }},
'''

replace_pattern = r'(const mockOitData = \{).*?(\};\s*// Modal Logic)'
html = re.sub(replace_pattern, r'\1\n' + mock_data_content + r'        \2', html, flags=re.DOTALL)

with open('/Users/kruboat/Desktop/website/jtp-web/public/ita-online.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed mock data array. Items:', len(matches))
