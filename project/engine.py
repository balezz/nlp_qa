from pathlib import Path
from tools import data_preparator, segmenter, recognizer, transcriptions_parser
from tools.utils import make_ass, make_wav_scp, delete_folder


def recognize(temp, wav):
    wav_scp = str(Path(temp) / 'wav.scp')
    make_wav_scp(wav, wav_scp)
    segm = segmenter.Segmenter(wav_scp,
                               './model/final.raw',
                               './model/conf/post_output.vec',
                               './model/conf/mfcc_hires.conf',
                               temp)
    segments = segm.segment()
    wav_segments_scp, utt2spk, spk2utt = segm.extract_segments(segments)
    rec = recognizer.Recognizer(wav_segments_scp, '../model/final.mdl', '../model/HCLG.fst', '../model/words.txt',
                                '../model/conf/mfcc.conf', '../model/conf/ivector_extractor.conf', spk2utt, temp)
    transcriptions = rec.recognize(Path(wav).stem)
    ass = str(Path(temp) / 'wav.ass')
    make_ass(Path(wav).name, segments, transcriptions, utt2spk, ass)
    pars = transcriptions_parser.TranscriptionsParser('', '', '', 0, 0, 'wav.csv')
    transcriptions_df = pars.process_file(ass)
    return transcriptions_df