import random
import pandas as pd


# ### These are lists of musical notes and temploral durations
chrom_scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
all_notes = [note+str(r)for r in range(0,8) for note in chrom_scale]
all_durs = ['1/32','1/16','3/32','1/8','3/16','1/4','3/8','1/2','3/4','1']


# ### 1)
# This will select the pitch range
def pitch_range_slicer(first,last):
    i1 = all_notes.index(first)
    i2 = all_notes.index(last)
    result = all_notes[i1:i2 + 1]
    return result


# ### 2)
def set_scale(notes,pitch_range):
    result = []
    for i in pitch_range:
        if i[:-1] in notes:
            result.append(i)
    return result


# ### 3)
# #### This will randomize pitch but with constraints:
# set_ = the specific set of notes
# distance = after picking one random note from the note set, each subsequent note will be chosen randomly from a new set within a range with this distance
# repeats = determines whether or not repeats are allowed (boolean)
# results = the total number of notes to output
def randomize_pitch(set_,distance, repeats, results):
    result = []
    rand = random.randint(0,len(set_)-1)
    result.append(set_[rand])
    if repeats:
        for i in range(results-1):
            pre_note = set_.index(result[-1])
            min_ = pre_note - distance
            max_ = pre_note + distance
            if min_ < 0 and max_ > (len(set_)-1):
                r = random.randint(0,len(set_)-1)
            elif min_ < 0:
                r = random.randint(0,max_)
            elif max_ > (len(set_) - 1) :
                r = random.randint(min_, len(set_)-1)
            else:    
                r = random.randint(min_, max_)
            result.append(set_[r])
    else:
        for i in range(results-1):
            pre_note = set_.index(result[-1])
            min_ = pre_note - distance
            max_ = pre_note + distance
            if min_ < 0 and max_ > (len(set_)-1):
                rrange = range(0,pre_note) + range(pre_note+1,len(set_))
                r = random.choice(rrange)
            elif min_ < 0:
                    if distance > 1:
                        rrange = range(0,pre_note) + range(pre_note+1,max_+1)
                        r = random.choice(rrange)
                    else:
                        if pre_note == 0:
                            r = 1
                        else: # pre_note == 1
                            rrange = range(0, pre_note) + range(pre_note+1, max_+1)
                            r = random.choice(rrange)
            elif max_ > (len(set_) - 1):
                rrange = range(min_,pre_note) + range(pre_note+1, len(set_))
                r = random.choice(rrange)
            else:    
                rrange = range(min_,pre_note) + range(pre_note+1, max_+1)
                r = random.choice(rrange)
            result.append(set_[r])        
    return result


# ### 4)
# #### This randomizes duration but with constraints:
# set_ = the set of durations to select from
# distance = after picking one random note from the note set, each subsequent note will be chosen randomly from a new set within a range with this distance 
# results = the total number of durations to output
def randomize_duration(set_,distance, results):
    result = []
    rand = random.randint(0,len(set_)-1)
    result.append(set_[rand])
    for i in range(results-1):
        pre_note = set_.index(result[-1])
        min_ = pre_note - distance
        max_ = pre_note + distance
        if min_ < 0 and max_ > (len(set_)-1):
            r = random.randint(0,len(set_)-1)
        elif min_ < 0:
            r = random.randint(0,max_- 1)
        elif max_ > (len(set_) - 1):
            r = random.randint(min_, len(set_)-1)
        else:    
            r = random.randint(min_, max_)
        result.append(set_[r])
    return result


# ### 5)
# #### This is THE function that combines pitch and durations to give our final desired output
def randomize(scale,pitch_range,pitch_distance,dur_set,dur_distance,repeats,n_notes):
    pitch_range = pitch_range_slicer(pitch_range[0],pitch_range[1])
    set_ = set_scale(scale,pitch_range)
    pitch_result = randomize_pitch(set_,pitch_distance,repeats,n_notes)
    duration_result = randomize_duration(dur_set,dur_distance,n_notes)
    result = zip(pitch_result,duration_result)
    return result


# ### Example:
pitch_range = ['B1','C#7']
scale = ['E', 'F#', 'G#', 'B', 'C#','D']
pitch_distance = 5
durs = ['1/16','3/32','1/8','3/16','1/4','3/8']

dur_distance = 5
n_notes = 20

a = randomize(scale, pitch_range, pitch_distance, durs, dur_distance, True ,n_notes)


# This converts the final output to a dataframe. 
# The below commented-out code can be used to download an excel file of the output
df = pd.DataFrame(a,columns=['Notes','Durations'])

# file_ = 'DadaSoup'
# writer = pd.ExcelWriter('downloads/{}.xlsx'.format(file))
# df.to_excel(writer,sheet_name="sheet1")
# writer.save()

# This gives the length of time of all of the notes in the final output.
def length(a):
    length = 0
    for i in a:
        l = i[1].split('/')
        num = float(l[0])
        try:
            den = float(l[1])
        except:
            den = 1
        frac = num / den
        length += frac
    tempo = 160
    bars_pm = tempo / 4
    minutes = float(length) / bars_pm
    seconds = minutes * 60
    hours = minutes / 60
    print 'hours: ', hours,'\n', 'minutes: ', minutes, '\n', 'seconds: ', seconds