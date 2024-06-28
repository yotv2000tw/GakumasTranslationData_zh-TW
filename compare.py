import os,json
from colorama import Back,Fore,init

def compare_localization():
    new_dict = {}
    trans_file = './compare/trans/localization.json'
    raw_file = './compare/raw/localization.json'
    output_file = './local-files/localization.json'
    with open(trans_file,'r') as f:
        trans_dict = json.load(f)
    with open(raw_file,'r') as f:
        raw_dict = json.load(f)
    for key in raw_dict.keys():
        try:
            trans_key = trans_dict[key]
        except:
            trans_key = raw_dict[key]
        new_dict[key] = trans_key
    with open(output_file,'w') as f:
        json.dump(new_dict,f)

def main():
    try:
        compare_localization()
    except FileNotFoundError:
        mention = Fore.LIGHTYELLOW_EX
        endofmention = Fore.WHITE
        print(f'請放入資料到指定文件夾中。\n{mention}- ./compare/raw/localization.json - 原始檔案\n- ./compare/trans/localization.json - 已翻譯過的檔案{endofmention}')
if __name__ == '__main__':
    main()