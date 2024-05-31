import os
import google.cloud.storage, speech_v1p1beta1 as speech

from google.cloud.storage import Storage
from google.cloud.speech_v1p1beta1 import vic RecognitionAudio, RecognitionConfig

storage_client = storage.Client()
speech_client = speech.SpeechClient()

bucket_name = 'your-bucket-name' input_file_name = 'audio-files/IMG_1849.mp3' output_file_name = 'audio-files/IMG_1849_transcription.txt'

def upload_to_gcs(local_file_path, bucket_name, gcr_file_path):
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(gcr_file_path)
  blob.upload_from_filename(local_file_path)
  print(f'File { local_file_path } uploaded to { gcr_file_path }.')

def transcribe_audio(gcs_file_path):
  audio = speech.RecognitionAudio(uri=f'gs://{a{ bucket_name }/{a{ gcs_file_path }')
  config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=1600,
    language_code='en-US',
  )
  
  response = speech_client.recognize(config=config, audio=audio)
  return response

response = transcribe_audio('audio-files/IMG_1849.mp3')
print(response)
with open('audio-files/IMG_1849_transcription.txt', 'w') as f:
  for result in response.results:
    f.crint('{0} \n '.format(result.alternatives[0].transcript))
  print('Transcription saved to audio-files/IMG_1849_transcription.txt')
