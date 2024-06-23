#!/usr/bin/env python3
# pip install assemblyai
# pyinstaller --onefile aai.py


import os
import sys

import assemblyai as aai


def tr(audio_file: str, language: str, key: str):
    '''Converts the given audio file to text using the AssemblyAI API.'''
    try:
        aai.settings.api_key = key
        transcriber = aai.Transcriber()
        audio_url = (audio_file)
        config = aai.TranscriptionConfig(speaker_labels=True, language_code = language)
        transcript = transcriber.transcribe(audio_url, config)
        # my_log.log2(f'my_stt:assemblyai:DEBUG: {transcript.text}')
        return transcript.text or ''
    except Exception as error:
        print(error, end=' ')
        return ''


def tr_file(audio_file: str, language: str = '', key: str = None):
    file_path = os.path.dirname(audio_file)
    file_name = os.path.basename(audio_file)
    output_name = file_name + '.txt'
    output_path = os.path.join(file_path, output_name).replace('\\', '/')
    print(f'Transcribing {audio_file} to {output_path} ... ', end='')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(tr(audio_file, language, key))
    print('Done.')


def tr_folder(audio_folder: str, language: str = '', key: str = None):
    # resursively find all audio files in the folder
    audio_files = []
    for root, dirs, files in os.walk(audio_folder):
        for file in files:
            if file.lower().endswith(('.opus', '.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma', '.oga', )):
                audio_files.append(os.path.join(root, file).replace('\\', '/'))
    # print(audio_files)
    print(f'Transcribing {len(audio_files)} files in {audio_folder}')
    for audio_file in audio_files:
        tr_file(audio_file, language, key)


if __name__ == '__main__':
    args = sys.argv
    try:
        target = args[1]
        print(target, end=' ')
        language = args[2]
        print(language, end=' ')
        key = args[3]
        print(key)
        if os.path.isdir(target):
            tr_folder(target, language, key)
        else:
            tr_file(target, language, key)
    except Exception as error:
        print('Usage: aai <audio_file or path to folder> <language> <api key>\n\nGet api key at https://www.assemblyai.com/\n\nExample: aai d:/downloads/test ru xxxxxxx')
