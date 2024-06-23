# AssemblyAI Automated Audio Transcription

This script leverages the AssemblyAI API to transcribe audio files into text. It can handle individual audio files or entire folders containing audio.

## Installation

1. Install Python 3.
2. Install the `assemblyai` library:
   ```bash
   pip install assemblyai
   ```
3. (Optional) Create a standalone executable:
   ```bash
   pyinstaller --onefile aai.py
   ```

## Usage

```
aai <audio_file or path to folder> <language> <api key>
```

### Arguments

* **audio_file or path to folder**: The path to the audio file or folder containing audio files.
* **language**: The language code of the audio. For example, `ru` for Russian.
* **api key**: Your AssemblyAI API key. You can get one at [https://www.assemblyai.com/](https://www.assemblyai.com/).

### Example

```
aai /Users/john/Downloads/test en xxxxxxx
```

This command will transcribe the file `/Users/john/Downloads/test.mp3` (or all audio files in the `/Users/john/Downloads/test` folder if it's a folder) to English using the provided API key.

## Supported Audio Formats

* .opus
* .mp3
* .wav
* .ogg
* .flac
* .m4a
* .aac
* .wma
* .oga

## Output

The script will create a text file (`.txt`) with the same name as the input audio file in the same directory. For example, if you transcribe `audio.mp3`, the script will create `audio.mp3.txt`.



# Автоматическая транскрипция аудио с помощью AssemblyAI

Этот скрипт использует API AssemblyAI для преобразования аудиофайлов в текст. Он может обрабатывать как отдельные аудиофайлы, так и целые папки с аудио.

## Установка

1. Установите Python 3.
2. Установите библиотеку `assemblyai`:
   ```bash
   pip install assemblyai
   ```
3. (Опционально) Создайте автономный исполняемый файл:
   ```bash
   pyinstaller --onefile aai.py
   ```

## Использование

```
aai <audio_file или путь к папке> <язык> <api ключ>
```

### Аргументы

* **audio_file или путь к папке**: Путь к аудиофайлу или папке, содержащей аудиофайлы.
* **язык**: Код языка аудио. Например, `ru` для русского языка.
* **api ключ**: Ваш API-ключ AssemblyAI. Вы можете получить его на сайте [https://www.assemblyai.com/](https://www.assemblyai.com/).

### Пример

```
aai d:/downloads/test ru xxxxxxx
```

Эта команда транскрибирует файл `d:/downloads/test.mp3` (или все аудиофайлы в папке `d:/downloads/test`, если это папка) на русский язык, используя указанный API-ключ.

## Поддерживаемые форматы аудио

* .opus
* .mp3
* .wav
* .ogg
* .flac
* .m4a
* .aac
* .wma
* .oga

## Вывод

Скрипт создаст текстовый файл (`.txt`) с тем же именем, что и исходный аудиофайл, в той же папке. Например, если вы транскрибируете файл `audio.mp3`, скрипт создаст файл `audio.mp3.txt`.