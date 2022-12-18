# 匯入.txt
dog_html = r'x:\pycharm\html.txt'
dog_html_open = open(dog_html, encoding='utf-8')
dog_html_text = dog_html_open.read()
dog_html_open.close()

# 匯出.txt
null_txt = r'x:\pycharm\method\export_dog_html.txt'
create_txt = open(null_txt, "w", encoding='utf-8')
create_txt.write(f'{dog_html_text}')
create_txt.close()