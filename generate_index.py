import os

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
files.sort()

guide_file = "github_gist_detailed_guide.html"
dash_files = [f for f in files if f != guide_file]

with open("index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>📊 Dashboard Index</title>
  <style>
    body {font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; line-height: 1.6; background: #fafafa; color: #333;}
    h1 {text-align: center; margin-bottom: 20px;}
    h2 {margin-top: 40px; border-bottom: 2px solid #ddd; padding-bottom: 5px;}
    .grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;}
    .card {background: #fff; padding: 20px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;}
    .card:hover {transform: translateY(-4px); box-shadow: 0 4px 10px rgba(0,0,0,0.15);}
    .card a {text-decoration: none; color: #0366d6; font-weight: bold; font-size: 16px;}
    .card small {display: block; margin-top: 8px; font-size: 13px; color: #666;}
  </style>
</head>
<body>
  <h1>📊 Dashboard Index</h1>

  <h2>#목적</h2>
  <p>뉴스레터와 관련된 대시보드를 제작 관리합니다.</p>

  <h2>#가이드</h2>
  <div class="grid">
""")

    # 가이드 파일 출력
    if guide_file in files:
        f.write(f'    <div class="card"><a href="{guide_file}">GitHub Gist Detailed Guide</a><small>{guide_file}</small></div>\n')

    f.write("""  </div>
  <h2>#대시보드</h2>
  <div class="grid">
""")

    # 나머지 파일 출력
    for file in dash_files:
        f.write(f'    <div class="card"><a href="{file}">{file}</a><small>{file}</small></div>\n')

    f.write("""  </div>
</body>
</html>""")
