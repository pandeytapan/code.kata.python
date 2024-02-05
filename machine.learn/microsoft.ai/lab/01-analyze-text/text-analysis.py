from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        client = TextAnalyticsClient(
            endpoint=ai_endpoint, credential=credential)

        # Analyze each text file in the reviews folder
        reviews_folder = 'data'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name),
                        encoding='utf8').read()
            print('\n' + text)

            # Get language
            detected_language = client.detect_language(documents=[text])[0]
            print('\nLanguage: ' + detected_language.primary_language.name)

            # Get sentiment
            sentiment = client.analyze_sentiment(documents=[text])[0]
            print('\nSentiment: ' + sentiment.sentiment)

            # Get key phrases
            phrases = client.extract_key_phrases(
                documents=[text])[0].key_phrases
            if len(phrases) > 0:
                print('\nKey Phrases:')
                for phrase in phrases:
                    print('\t{}'.format(phrase))

            # Get entities
            entities = client.recognize_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print('\nEntities:')
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))

            # Get linked entities
            linked_entities = client.recognize_linked_entities(documents=[text])[
                0].entities
            if len(linked_entities) > 0:
                print('\nLinked Entities:')
                for linked_entity in linked_entities:
                    print('\t{} ({})'.format(linked_entity.name,
                          linked_entity.data_source_entity_id))
                    print('\t\tURL: {}'.format(linked_entity.url))
                    print('\t\tData Source: {}'.format(
                        linked_entity.data_source))

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
