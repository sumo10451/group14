import streamlit as st
import time
from TTS.api import TTS
from googletrans import Translator
import pywhisper

languages = {'English': 'en', 'Japanese': 'ja', 'French':'fr', 'Danish': 'da', 'Italian': 'it'}

#googletrans engine
translator = Translator()

# Using object notation
select = st.sidebar.radio('select an option: ',('Text to audio conversion', 'Text translation'))

# Using "with" notation
if select=='Text to audio conversion':
    st.title("Text to Voice Conversion")
    option = st.selectbox(
        'Select a language model you want to convert to..',
        ('English', 'Japanese', 'French', 'Danish', 'Italian'))

    if option:
        st.write('You selected:', option)

    text = st.text_input('Enter text to convert to audio format!!')
    st.write(text)

    if st.button('Convert text to audio!'):
        if(option == 'English'):
            model = "tts_models/en/ljspeech/vits"
        elif(option == 'Japanese'):
            model = "tts_models/ja/kokoro/tacotron2-DDC"
        elif(option == 'French'):
            model = "tts_models/fr/css10/vits"
        elif(option == 'Danish'):
            model = "tts_models/da/cv/vits"
        elif(option == 'Italian'):
            model = "tts_models/it/mai_female/vits"
        # Init TTS with the target model name
        lang = translator.detect(text)
        if(languages[option] != lang.lang):
            st.warning('text is in ' + lang.lang + ' language')
            st.success('converting language to the selected language '+ option)
            lang = translator.translate(text, src='auto', dest=languages[option])
            st.success(lang.text)
            text = lang.text
            st.success('text converted to ' +option + ' language successfully')
        tts = TTS(model_name=model, progress_bar=False, gpu=False)
        if tts:
            with st.spinner('loading model...'):
                time.sleep(5)
            st.success('Model loaded successfully')
            # Run TTS
            tts.tts_to_file(text=text, file_path="out.wav")
            with st.spinner('converting to audio...'):
                time.sleep(5)
            st.success('Converted to audio successfully')

            audio_file = open('out.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            st.success("You can now play the audio by clicking on the play button!!")
        else:
            st.warning('Model failed to load!!')
    
elif select=='Text translation':
    st.title("Text translation")
    text = st.text_input('Enter a text!!')
    st.write(text)
    if text:
        option1= st.radio('Select an option', ('Detect language', 'Translate text'))
        if option1 == 'Detect language':
            lang = translator.detect(text)
            st.success('Detected language: '+ lang.lang)
        if option1 == 'Translate text':
            option = st.selectbox(
            'Select a language model you want to convert to..',
            ('English', 'Japanese', 'French', 'Danish', 'Italian'))
            if st.button('translate'):
                st.write('You selected:', option)
                if option == 'English':
                    trans_lang = 'en'
                elif option == 'Japanese':
                    trans_lang = 'ja'
                elif option == 'French':
                    trans_lang = 'fr'
                elif option == 'Danish':
                    trans_lang = 'da'
                elif option == 'Italian':
                    trans_lang = 'it'
                lang = translator.translate(text, src='auto', dest=trans_lang)
                st.success(lang.text)
else:
    st.warning('Select an option to proceed!')

