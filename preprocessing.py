import h5py
	
import csv
import numpy
import os
filename="/Users/StephanieZhou/Downloads/MillionSongSubset/data/A/B/A/TRABACN128F425B784.h5"
f = h5py.File(filename, "r")
def printname(name):
	print name
f.visit(printname)
for name in f:
	for subname in f[name]:
		dset=f[name][subname]
		print name+"/"+subname+' '+str(dset.shape)




f2 = h5py.File('/Users/StephanieZhou/Downloads/msd_summary_file.h5', "r")

genrefile=[line for line in open('/Users/StephanieZhou/Downloads/msd_tagtraum_cd1.cls') if not line[0]=="#"]
genredict={}
for pair in genrefile:
	trackid=pair.split('\t')[0]
	genres=",".join(pair.split('\t')[1:]).strip()
	genredict[trackid]=genres

files=[]
for (dirpath, dirnames, filenames) in os.walk('/Users/StephanieZhou/Downloads/MillionSongSubset/data/'):
	for n in filenames:
		if(n[-2:]=='h5') and n[0:-3] in genredict:
			files+=[dirpath+"/"+n]


#f['analysis']['songs'][:]
#array([ (22050, '624e1d3e1adf85da9c948c16d026e8eb',  0.,  259.44771,  0.212,  0., 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,  0.412, -8.422, 0,  0.329,  249.667,  106.689, 1,  0.612, 'TRABACN128F425B784')],
      #dtype=[('analysis_sample_rate', '<i4'), ('audio_md5', 'S32'), ('danceability', '<f8'), ('duration', '<f8'), ('end_of_fade_in', '<f8'), ('energy', '<f8'), ('idx_bars_confidence', '<i4'), ('idx_bars_start', '<i4'), ('idx_beats_confidence', '<i4'), ('idx_beats_start', '<i4'), ('idx_sections_confidence', '<i4'), ('idx_sections_start', '<i4'), ('idx_segments_confidence', '<i4'), ('idx_segments_loudness_max', '<i4'), ('idx_segments_loudness_max_time', '<i4'), ('idx_segments_loudness_start', '<i4'), ('idx_segments_pitches', '<i4'), ('idx_segments_start', '<i4'), ('idx_segments_timbre', '<i4'), ('idx_tatums_confidence', '<i4'), ('idx_tatums_start', '<i4'), ('key', '<i4'), ('key_confidence', '<f8'), ('loudness', '<f8'), ('mode', '<i4'), ('mode_confidence', '<f8'), ('start_of_fade_out', '<f8'), ('tempo', '<f8'), ('time_signature', '<i4'), ('time_signature_confidence', '<f8'), ('track_id', 'S32')])
relevantfields=['track_id','analysis_sample_rate','tempo','key','key_confidence','danceability','duration','energy','loudness', 'mode','mode_confidence','end_of_fade_in','start_of_fade_out','idx_bars_confidence', 'idx_bars_start', 'idx_beats_confidence', 'idx_beats_start', 'idx_sections_confidence', 'idx_sections_start', 'idx_segments_confidence', 'idx_segments_loudness_max', 'idx_segments_loudness_max_time', 'idx_segments_loudness_start', 'idx_segments_pitches', 'idx_segments_start','idx_segments_timbre', 'idx_tatums_confidence','idx_tatums_start']
relevantfields2=['bars_confidence','bars_start','beats_confidence','beats_start','sections_confidence','sections_start','segments_confidence','segments_loudness_max','segments_loudness_max_time','segments_loudness_start','segments_start','tatums_confidence','tatums_start']#,'segments_timbre','segments_pitches',

for r in relevantfields:
	print r+str(f['analysis']['songs'][:][r][0])

header=['genre']+relevantfields+relevantfields2
result=[header]

count=0
for filename in files:
	count+=1
	if(count%100==1):
		print count
	f = h5py.File(filename, "r")
	fields=[genredict[filename[60:-3]]]
	for r in relevantfields:
		fields+=[f['analysis']['songs'][:][r][0]]
	for r in relevantfields2:
		fields+=[list(f['analysis'][r][0:])]
	result+=[fields]

with open('records_scalar_only.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for record in result:
        writer.writerow(record)

