import re
import json
import argparse

def parse_verse_number(verse):
    match = re.match(r'^(\d+):(\d+)', verse)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

def convert(file_1:str, file_2:str, output_file:str):
    with open(file_1, 'r') as f1, open(file_2, 'r') as f2:
        text1 = f1.read().replace('\n', ' ')
        text2 = f2.read().replace('\n', ' ')

        verses1 = re.findall(r'\d+:\d+', text1)
        verses2 = re.findall(r'\d+:\d+', text2)

        verse_pairs = []

        for v1 in verses1:
            num1, sub_num1 = parse_verse_number(v1)
            for v2 in verses2:
                num2, sub_num2 = parse_verse_number(v2)
                if num1 == num2 and sub_num1 == sub_num2:
                    pattern1 = fr'{v1}' + r'\s(.*?)(?=' + r'\d+:\d+' + r'\s|\Z)'
                    #print(f'Pattern: {pattern1}')
                    verse1 = re.search(pattern1, text1, re.DOTALL).group(1).strip()

                    pattern2 = fr'{v2}' + r'\s(.*?)(?=' + r'\d+:\d+' + r'\s|\Z)'
                    verse2 = re.search(pattern2, text2, re.DOTALL).group(1).strip()

                    verse_pairs.append({
                    "verse_number": v1,
                    "ngalum": verse1,
                    "english": verse2
                    })

                    verses2.remove(v2)  # Remove matched verse to avoid duplicates
                    break

        with open(output_file, 'w') as output_file:
            json.dump(verse_pairs, output_file, indent=4)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Combines a bible text with its translational equivalent.")
    parser.add_argument("file1", help="Path to the first file")
    parser.add_argument("file2", help="Path to the second file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2
    output_file = args. output_file

    convert(file1, file2, output_file)
