import json
import pprint

def load_transcript(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def merge_captions(transcript, max_words=50):
    chunks = []
    current_chunk = []
    current_words = 0
    last_end_time = 0

    for caption in transcript:
        start_time = caption['start']
        duration = caption['duration']
        end_time = start_time + duration
        words = caption['text'].split()

        if (start_time < last_end_time + 2) and (current_words + len(words) <= max_words):
            current_chunk.append(caption['text'])
            current_words += len(words)
        else:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [caption['text']]
            current_words = len(words)

        last_end_time = end_time

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def main():
    file_path = 'transcript.json'
    
    transcript = load_transcript(file_path)
    
    chunks = merge_captions(transcript)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        pprint.pprint(chunk)

if __name__ == "__main__":
    main()
