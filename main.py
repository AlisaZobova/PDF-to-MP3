from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path: str, language: str = 'en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'Original file: {Path(file_path).name}')
        print('Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', ' ')

        audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')

        return f'File {file_name}.mp3 saved successfully!\n'

    else:
        return 'File doesn`t exist, check the file path!\n'


def main():
    file_path = input('\nEnter file path: ')
    language = input('\nChoose language, for example `en`: ')
    print()
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
