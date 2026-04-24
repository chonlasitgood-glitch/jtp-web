import re

with open('/Users/kruboat/Desktop/website/jtp-web/public/app/e-saraban.html', 'r') as f:
    content = f.read()

# 1. Fonts and Tailwind Config
config_old = """    <!-- Google Fonts: Sarabun (มาตรฐานราชการไทย) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Tailwind Config for Font -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Sarabun', 'sans-serif'],
                    },
                    colors: {
                        primary: '#0f172a',
                        secondary: '#334155',
                        accent: '#2563eb',
                    }
                }
            }
        }
    </script>"""

config_new = """    <!-- Google Fonts: Prompt -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Tailwind Config for Font -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Prompt', 'sans-serif'],
                    },
                    colors: {
                        primary: {
                            50: '#fefce8',
                            100: '#fef9c3',
                            200: '#fef08a',
                            300: '#fde047',
                            400: '#facc15',
                            500: '#eab308',
                            600: '#ca8a04',
                            700: '#a16207',
                            800: '#854d0e',
                            900: '#713f12',
                        },
                    }
                }
            }
        }
    </script>"""

content = content.replace(config_old, config_new)

# 2. Sidebar bg-primary to bg-slate-900
content = content.replace('bg-primary text-white', 'bg-slate-900 text-white')

# 3. Colors blue to primary mapping
color_map = {
    'blue-900': 'primary-700',
    'blue-800': 'primary-600',
    'blue-600': 'primary-500',
    'blue-500': 'primary-500',
    'blue-400': 'primary-400',
    'blue-300': 'primary-300',
    'blue-200': 'primary-200',
    'blue-100': 'primary-100',
    'blue-50': 'primary-50'
}

for old, new in color_map.items():
    content = content.replace(old, new)

# 4. Text color on primary-500 and primary-400 buttons/badges should be text-slate-900
content = content.replace('bg-primary-500 text-white', 'bg-primary-500 text-slate-900')
content = content.replace('bg-primary-600 text-white', 'bg-primary-600 text-white') # This is fine

# Specific fix for JS string replacement where blue was replaced
# navInternal.className = "flex items-center px-3 py-2.5 bg-primary-700 text-white rounded-lg group transition-colors mt-1";
# wait, the JS logic: switchTab uses classes. Let's fix JS directly.
# Let's adjust JS: bg-primary-700 -> bg-primary-500 text-slate-900
content = content.replace('bg-primary-700 text-white', 'bg-primary-500 text-slate-900')
content = content.replace('text-primary-400 mr-3', 'text-primary-400 mr-3')

with open('/Users/kruboat/Desktop/website/jtp-web/public/app/e-saraban.html', 'w') as f:
    f.write(content)

print("Done")
