from clearvoice import ClearVoice

##-----Demo One: use MossFormer2_SE_48K model for speech enhancement -----------------
if True:
    myClearVoice = ClearVoice(task='speech_enhancement', model_names=['MossFormer2_SE_48K'])

    ##1sd calling method: process the waveform from input file and return output waveform, then write to output_MossFormer2_SE_48K_xxx with the same audio format
    output_wav = myClearVoice(input_path='samples/input.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_input.wav')
    output_wav = myClearVoice(input_path='samples/speech2.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech2.wav')
    output_wav = myClearVoice(input_path='samples/speech1.mp3', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech1.mp3')
    output_wav = myClearVoice(input_path='samples/speech1.flac', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech1.flac')
    output_wav = myClearVoice(input_path='samples/speech1.ogg', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech1.ogg')
    output_wav = myClearVoice(input_path='samples/speech1.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech1.wav')
    output_wav = myClearVoice(input_path='samples/speech2.aac', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech2.aac')
    output_wav = myClearVoice(input_path='samples/speech2.aiff', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SE_48K_speech2.aiff')
    
    ##2nd calling method: process all wav files in 'path_to_input_wavs/' and write outputs to 'path_to_output_wavs'
    myClearVoice(input_path='samples/path_to_input_wavs', online_write=True, output_path='samples/path_to_output_wavs')

    ##3rd calling method: process wav files listed in .scp file, and write outputs to 'path_to_output_wavs_scp/'
    myClearVoice(input_path='samples/scp/audio_samples.scp', online_write=True, output_path='samples/path_to_output_wavs_scp')
    
##-----Demo Two: use FRCRN_SE_16K model for speech enhancement -----------------
if False:
    myClearVoice = ClearVoice(task='speech_enhancement', model_names=['FRCRN_SE_16K'])

    ##1sd calling method: process an input waveform and return output waveform, then write to output_FRCRN_SE_16K.wav
    output_wav = myClearVoice(input_path='samples/input.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_FRCRN_SE_16K.wav')

    ##2nd calling method: process all wav files in 'path_to_input_wavs/' and write outputs to 'path_to_output_wavs'
    myClearVoice(input_path='samples/path_to_input_wavs', online_write=True, output_path='samples/path_to_output_wavs')

    ##3rd calling method: process wav files listed in .scp file, and write outputs to 'path_to_output_wavs_scp/'
    myClearVoice(input_path='samples/scp/audio_samples.scp', online_write=True, output_path='samples/path_to_output_wavs_scp')
    
##-----Demo Three: use MossFormerGAN_SE_16K model for speech enhancement -----------------
if False:
    myClearVoice = ClearVoice(task='speech_enhancement', model_names=['MossFormerGAN_SE_16K'])

    ##1sd calling method: process the waveform from input.wav and return output waveform, then write to output_MossFormerGAN_SE_16K.wav
    output_wav = myClearVoice(input_path='samples/input.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormerGAN_SE_16K.wav')

    ##2nd calling method: process all wav files in 'path_to_input_wavs/' and write outputs to 'path_to_output_wavs'
    myClearVoice(input_path='samples/path_to_input_wavs', online_write=True, output_path='samples/path_to_output_wavs')

    ##3rd calling method: process wav files listed in .scp file, and write outputs to 'path_to_output_wavs_scp/'
    myClearVoice(input_path='samples/scp/audio_samples.scp', online_write=True, output_path='samples/path_to_output_wavs_scp')

##-----Demo Four: use MossFormer2_SS_16K model for speech separation -----------------
if False:
    myClearVoice = ClearVoice(task='speech_separation', model_names=['MossFormer2_SS_16K'])

    ##1sd calling method: process an input waveform and return output waveform, then write to output_MossFormer2_SS_16K_s1.wav and output_MossFormer2_SS_16K_s2.wav
    output_wav = myClearVoice(input_path='samples/input_ss.wav', online_write=False)
    myClearVoice.write(output_wav, output_path='samples/output_MossFormer2_SS_16K.wav')

    #2nd calling method: process all wav files in 'path_to_input_wavs/' and write outputs to 'path_to_output_wavs'
    myClearVoice(input_path='samples/path_to_input_wavs_ss', online_write=True, output_path='samples/path_to_output_wavs')

    ##3rd calling method: process wav files listed in .scp file, and write outputs to 'path_to_output_wavs_scp/'
    myClearVoice(input_path='samples/scp/audio_samples_mix.scp', online_write=True, output_path='samples/path_to_output_wavs_scp')

##-----Demo Five: use AV_MossFormer2_TSE_16K model for audio-visual target speaker extraction ------
if False:
    myClearVoice = ClearVoice(task='target_speaker_extraction', model_names=['AV_MossFormer2_TSE_16K'])

    #1st calling method: process all video files in 'path_to_input_videos/' and write outputs to 'path_to_output_videos_tse'
    myClearVoice(input_path='samples/path_to_input_videos_tse', online_write=True, output_path='samples/path_to_output_videos_tse')

    #2nd calling method: process video files listed in .scp file, and write outputs to 'path_to_output_videos_tse_scp/'
    myClearVoice(input_path='samples/scp/video_samples.scp', online_write=True, output_path='samples/path_to_output_videos_tse_scp')
